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
<img src="https://cdn4.telesco.pe/file/U5RxoE1iJEI-7fuDf2Nu3CUZgIY21fSNpUzBk3d7MsUOesjVB_JTLs1WrH0iSJ6TQ58el6lburtmLbi_ji3nIjJmCcouh--SjaOMlD9uJ7zs10IxhaoPn_mKQAIsX7NPbfS67bDOqeIkXPqG5DshmCe2Xl88gkzsCAEVDDb5pXm5cIBbDuMFS1nI2hk0Uu27FO63WGbQkd_hBQGQEH9JNOk1OUJXfJ2tNXHolytDMwauVwOA69O0OPpTjNB7FNfIDptGTkKltf54R4kZkultVfFaJrHTyRXdZfpVjKiUnYQPF5hxQ5fa0wob56sHdKQP5x_zL691FNsqiRnu4y_nUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 487K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 21:02:44</div>
<hr>

<div class="tg-post" id="msg-31330">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1NLVIGL0J-uF8h3n6NoH6zH6fIAPfy26PvKz_cXxSBzplw5eOkBKn9qtThbJ-6r-ia5-JL7fe66mJNFWOX_0kboauM2kgjMa4uM0H80ahsmpROhd4EmlScJ9cfnDmkj1ONptNPdcWDMsAUrP8Iv45Bk8NycmkH4pck2LD_SCsBwvWzAAQ5HE5QSqQrD61gFBfz-UruY3th318g7RujX_zQuz8yF7nU_7g7mcm8D3tRx-nhTVCrN64M0JJGqqCpfFk0mqSQIB1WDGjjI6mYsO3q-InPxT-sak4fck8DCPXnI9K0Mf-m67wYUlr9Edq2kAUOKW6NkoON-pvbNJBntwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
فدراسیون‌فوتبال‌پرتغال موقتا کریس رونالدو رو بابت ترک اردوی تیم ملی این کشور محروم کرده. گفتنی‌ست که کریس رونالدو بین یک الی شش ماه از همراهی تیم ملی فوتبال پرتغال محروم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/persiana_Soccer/31330" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31328">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QQWz_k9qEn9tZzLogDoiYmu0eWzwBrK7-aXA1stt9RQoqqq-363S6Xvhg_bhcWnFX2KGXQJl9s55Fy1iqZ02RQwkpQdzAfjTzzCQX_aC9ez3DiAJoFeTueN6IixK2vMyN1XfoUBevORe4raeiaV_-CAfBT-fKRO9vwKFq5C6m7YZAX0JZlDAhO5S0V82eGtC6s6ZNGFUTbtj_p-ic2EMw527OWCuT7aAevuF3u711bDqncaDJtlT9Idd-uL4OsNQDikmfnBvxTdPF5cdjy_dVh7SZipkqgG9qWHf_mndVWECRlJFOOouqwnRi6ZsM3Lsud6PWfIijsiOJ-3uUJR1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Alb00lRfurTh_WojyE6bXMfofZ8Z5AHCVXcjH8KL2Zkacp1GM6H-VJz3GVuUWj_BO4VQkCVMisUIu7-Y54q6QzDnZIt91rpsSpBMqdN7kZ2zUxF4ubH7DmgNNaC8Aa6XxvtlWIIuqkx5-NOhJvnzUNiPlhPhO3wPjXmpwBMufQAMA8UVWdU3xcBc_Yczqz2tVXVTvoAvJs-tKrCca-4yI4LZUY9Gg4iJtqvLgUbZ7A5G71fCAsTZGi1UY94bhESiRLieiYOjKzZT6ybMFVgPKixCvMznTgGcIF86VxDfv9puiWkxna8XsPTBks3jIy0n55ii7Y7Pjwc6YpQ-_dMb6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سیلی دوم در انتظار مهاجم سابق پرسپولیس؛ درنیمه اول دوم بازی امروز با شمس آذر رضا شکاری به این شکل پنالتی خود را بیرون زد تا در پایان بازی پذیرای یک چک آبدار از سوی ساکت الهامی باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/31328" target="_blank">📅 19:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31327">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/31327" target="_blank">📅 19:29 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31326">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzcv_La8rzp1kk74PMjvrCWXIUu2_PxUqQ1bRPW3HzyQKO2wlDPnsVOar9xh2E4BvvuDofp9otoGBMx4CMB_R7XIJeIQ2Y1WYaNbLZUZlKd65M0fE7Erpa6bcCvSzbgs9gQo23jay9-jmdfpza8IY1VvZqmSqYZuT2upFOwSQXgLwfLoSNKO-2SAJ8NlKO94rfbrAmjCDsvpfJJCwDOoxXglMloOV_11bKDsgOKUfOktwIh4RRLUEMFnw3W5MeOGTHMK4ZV04rIyHDENqxmHRdkbizSRziySwUy5ltLigBsQgvjxdTnG4Or4rhrO6IFbjJs43A6FEMooKbrYmFeHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلهائر زننده‌سریع‌ترین گل تاریخ بوندسلیگا؛ گل ثانیه ۸ رابین فلهائر به بایرن مونیخ با عبور از رکورد کوین فولاند، تبدیل به سریع‌ترین گل تاریخ مسابقات شد. فلهائر، ثانیه ۸، فولاند ثانیه ۹؛  هر دو گل سریع تاریخ، مقابل بایرن و مانوئل نویر به ثمر رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/31326" target="_blank">📅 19:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31325">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz2iTteWPAexzV5bepEUM2e8a3FKgl3mQjt5xxiTkqhOy47Wm-cW_55LHH6ArHpJ7Idps3VUIgjyw5p1C7H4TnwhM7IFT45E65sLrgL8IbYhsIa_QK_mwRdkAk5jSIH5MYcn72tDWh8kAv1df0Tbgf6pucK7wnysNcmzFa0KQBZwB4Q71HMjAUpoAtOdCKrSM46_jJAweRcG5tk3G5dFWmFFH-2JHkGZ8XETFIORnF-shB1Ng3BEav4ILtt_QN3bor5bbuVVDRHPp3pc8Gkzt0N3Zpr0SbOEGLRfvAFmm4zGdecWzn0Zv66TPazs7HMRc3-m5sZuYdMJvB5xhH7muw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/31325" target="_blank">📅 19:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31324">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSJ9FxsDOXDl2iUgPmJAgpXC3nP-Zc6oiLibAy7Fh99h-_PC3wGp8ZpFdZi-vgGtTtrEunL-Ks8fY81CS74NODv_vqXGvSv0lMfTHmePhkIykMFBP1sva3RW9w6DZJa77p9zvEBLy2rnFg5Om_CKy-hzy6G1DZxkH709iY6RQhKo4WWNjcU4uQB_VtqKHuPfluBfbUqV3zZi-i-9SKJySy0p_-KT6KPEPyCqn2XXHNSEASkf20Vv0RbMJlVj1eyNG-g0jqZ_9QCzvf9dsGUGanANY6A4jAfMO9sRBNPJWRj5vUf292y66zjga_b2mJnXXOkUflUQtPNVAi99Oqsj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
خبرنگار و گزارشگر شبکه اسپورت که از فن های شدید بارسلونا هانسی فلیکه و معتقده که فلیک امسال بارسلونا رو قهرمان چمپیونزلیگ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/31324" target="_blank">📅 18:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31323">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=pAQPOxXHSrpptnKNW_NyTZyuWkiX_F4xVSG1sEoyzq_jLP4TZdLHbgbLFIFHvNTxy3fXVUmJyuBTUaYTKMB18p6KanuOaa7uiuSjxArBxgNin9bLyZkUGFvTqMWS68Z49lJ_53rTQ8ttUckj2Plt5UImakgCqN9cL7vM7znC4o-mfkKGbdMGQTTB57XQcSKWkgczLGSnihV5Z2U6QAHOYZbqKQvWAC7CYHFQVT8T63P90Ggq5DE0Fe7U1HwJ1NNW-f3DqbeWvEi_3EbLa1Ukc6NL_Cw8kj4UhyD-NkIN-x_K1ycydwFopCrZA0XfOtOPkTtTjwL_d0_cRVwBrh4rrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5837e5cdb.mp4?token=pAQPOxXHSrpptnKNW_NyTZyuWkiX_F4xVSG1sEoyzq_jLP4TZdLHbgbLFIFHvNTxy3fXVUmJyuBTUaYTKMB18p6KanuOaa7uiuSjxArBxgNin9bLyZkUGFvTqMWS68Z49lJ_53rTQ8ttUckj2Plt5UImakgCqN9cL7vM7znC4o-mfkKGbdMGQTTB57XQcSKWkgczLGSnihV5Z2U6QAHOYZbqKQvWAC7CYHFQVT8T63P90Ggq5DE0Fe7U1HwJ1NNW-f3DqbeWvEi_3EbLa1Ukc6NL_Cw8kj4UhyD-NkIN-x_K1ycydwFopCrZA0XfOtOPkTtTjwL_d0_cRVwBrh4rrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساکت‌الهامی‌سرمربی‌پیکان درپایان نیمه اول بازی باشمس‌آذر اینجوری رفت سمت حجت احمدی و یکی خوابوند زیرگوشش بابت اعتراض به کادرفنی حریف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/31323" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31322">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfyJ7j51FAJLJJItlQKxDuh0_wPWTuHdCETN0EugtNlnOrt358FXbUCgnvLmi4df4koqawa9nm1EVQSF6YykaxX0UyfwQsKUze5o4eTLAZIbDW-T54_7ENcnsx5jerP6jN1SfPn_hkWdw5eQcr-wK2PucsqzSw3WDC7ird8ByTTkczWqTJVF2PYRXJFeooLFCt12AkKoQkerFJvSMxgGo-YawxBlsXBZU_bSxvXtS2nksUqTBZujTRbDRPz37M_UcXn6yaHPOzdTN08Y31q0iRBVNYG53iSoFS1pThAAdjgu6vRYnG8aRoxRX6BWLZRUv_EA1-yrSeelQzL-QXaqmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/31322" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31321">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpzvvBGpAvUZ-47mM-q35kS33qTNhlSxyQt_QV0v9rNthHkGAZe62yz9okjEKzP3OT2o7dNQE8Qyr37c70u7_SESGEFIuNvAURdl19w_kMFR0OwxYV9kI53ldSz3piQYpCAS-P9gGEDn3i2H5200Ydqgqa1wmQIWZCASYf527FmbboRDm-ZciKsF3t5glsfSaYMT9gM4dXqrf_hXQ-fR2sBQI733w_k1a-jFIO-z-eYbr9ewNBvqxO7KhiwDExUVDTtNMQsL9t2Us6WbiHH0gte4L_bAMHlu761lKU4D3iQeYKTN1e4rlz2EFjMVsxXThDXw37eCwcDCyPFHLxcvSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G18
🅰
🛒
ورود به سایت
👇
✅
https://ieoruyxtsud.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/31321" target="_blank">📅 18:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31320">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGtGVUZI8BOugdslUYaXN1hkuIfcdikzrUghVx-7aQgWJBUJJjqyvxz5gLbSwVqHRNGTi1hsbGojKcQaAOfZ_hHKAvLpwZxr4lZKP8_Daowx7_uW01LoGJmQ03MEhuj1Af6hDceFecEshwzzSTF2Zc-Wlu5hhL0G4SHEccxGdGsbKKH0SfyjCf65kYj1Cd9-bPV0uMojJFLx-GxNm5CKkkUZlcsl-F3_c0MOcBhsITntdWU5S45CB1lZO5aE9UW_7XIKvXh_5cnH7L8hpFfoSD6s6D-Zo_eyWgWvOznx9FDpeQUkcGUnB-iAVJRR34zioatsr_upx0xUMqjnEY9dHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال:
به‌مامانم‌گفتم تو هرمحله‌ای که دوست داره براش‌خونه‌میخرم و اینکارو انجام دادم، قبلا تو خونمون آشپزخانه و اتاق خواب یه جا بودن و زندگی سختی داشتیم، ولی الان خیلی خوشحالم که برادرم اون زندگی‌مرفهی روداره که من آرزوشو داشتم.
تو زندگیم یه ملکه دارم و اونم مادرمه
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/31320" target="_blank">📅 18:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31319">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=IRuAoQ-riCFv0YqHJhcL9Bopf9IYihxuvp9Zml_bTeFpAt0Qkw_emBlZks6L6XvdtecnNiPtVyawraMaZ5jfABxgPIKURb1TeeANuPYRoUUe2ZoJY5MWfYYjv9JsAuHYWDf9u4hW5JxQzyH6Zb_Mf3NRLTL5n6X6c7jCUOlhIsHDFc55jmfOqVz4iX2xGuB189D6O8iuTWv-kvSk6k27O38rnWl3G9i5w46LDNCyhuesomtyHFRPeT-ffcgULre8ppudO4neAd1CcvjHl5BticZHEwaGoRmBBmwDb0hrJIUAKOUlIIpL6RUKW_gboLoFD63vW4KHgz9xeoiJ1dGFSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17a54f38df.mp4?token=IRuAoQ-riCFv0YqHJhcL9Bopf9IYihxuvp9Zml_bTeFpAt0Qkw_emBlZks6L6XvdtecnNiPtVyawraMaZ5jfABxgPIKURb1TeeANuPYRoUUe2ZoJY5MWfYYjv9JsAuHYWDf9u4hW5JxQzyH6Zb_Mf3NRLTL5n6X6c7jCUOlhIsHDFc55jmfOqVz4iX2xGuB189D6O8iuTWv-kvSk6k27O38rnWl3G9i5w46LDNCyhuesomtyHFRPeT-ffcgULre8ppudO4neAd1CcvjHl5BticZHEwaGoRmBBmwDb0hrJIUAKOUlIIpL6RUKW_gboLoFD63vW4KHgz9xeoiJ1dGFSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
واکنش‌ابوطالب‌حسینی به صحبت‌های اخیر ساکت الهامی سرمربی سابق نساجی که گفته بود در زمان حضور دراین‌تیم در رقابت‌های لیگ برتر حدود 10 روز در زندان‌های ساری تمرین میکردند.
🤯
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/31319" target="_blank">📅 18:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31318">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=t2pwqjEoKp6Bwu7rd-oDPK11xQOZBGkM4OW5Z0HqsjewbIsSj8ej91-ohZc1EulD__wEL9e7Snry_2CxiDU4BOq12giOQ-74tEniqtSBU5T9tZ4ggG7CF_ShfEqtuks4mWbJ0_fvOmXlYdDhFXGHj7_2yv0nttXYM0MBBdpXSg9BIl1A03FzrMZAu50ze1ySn8_CgPwkIlBRyIztEzRsyhAifVX1WNL35a94xmnETJgWjWBds3lur8CjriZZVb7vM193TuMVRDo7JeGd2j6xfVsAxh9jJ83DrlSoPD_cRWkjQ-yGO7woKBwdE6uvk_2zvHmP3OTn3cerf3cLVNB4TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e05ef0c40.mp4?token=t2pwqjEoKp6Bwu7rd-oDPK11xQOZBGkM4OW5Z0HqsjewbIsSj8ej91-ohZc1EulD__wEL9e7Snry_2CxiDU4BOq12giOQ-74tEniqtSBU5T9tZ4ggG7CF_ShfEqtuks4mWbJ0_fvOmXlYdDhFXGHj7_2yv0nttXYM0MBBdpXSg9BIl1A03FzrMZAu50ze1ySn8_CgPwkIlBRyIztEzRsyhAifVX1WNL35a94xmnETJgWjWBds3lur8CjriZZVb7vM193TuMVRDo7JeGd2j6xfVsAxh9jJ83DrlSoPD_cRWkjQ-yGO7woKBwdE6uvk_2zvHmP3OTn3cerf3cLVNB4TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌ششم‌لیگ‌جزیره؛ آرسنالِ آرتتا با درخشش دکلان رایس و گلزنی برونو گیمارش دو بر یک از سد لیدزیونایتد گذشت و در رتبه دوم جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/31318" target="_blank">📅 17:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31317">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/He2EK6W_eYLfXR_dGAyUxg4U6dq_bHaYQHHry7kTm-HUnIXThX01WcO9ltu33TXiBEhWtw0cl3qqOjsecAsHKjgDvMpP_5fKq_GIMlOEwQ1go6aAs-E-tuzhInf-1gHssuNCOCRI9fJxsBdPvke342gydzV6YIC_j27c403TVSiY9JQInYDq7m4rEmiikxt17x3w-jnpL6xotJNKHH7fRtXxxN_vgtz26HcdOuprq5fQVK8U-ZMOO6a6NosRw2J-taIiI_Yrd8qxBsPuWAuPadM9QJaGAtnLIdqEjkRzxu78rYb_U5FpnrV9qiSxgSRzS4oU6v5QeDjWEeVsmiMwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/31317" target="_blank">📅 17:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31316">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmTzqMpsXCrvWiLUnwAKQEC64Htt_EFwXEL8RpuvoY2RI9iKzMhU5hE-woHSVC3XdQEl52wqjWhTDvKz0yEgRiWnUKlc__DZH1pXMOEd0BJfoZrTkCfWgwQaVoc5Ch_JSpImkGiwd8DyiOJzCs27HX6kJwgJTGUf23o7mS4aU_rOoeNFwTLL18qJRznN5qA-1NwRfrh_0AIpiTZ8PoFlEzLO5mUuf1MiE7yx8kGjcYDtP7dUzrC54Q1KGQHpgnFeGBbhJ3o4XRPipj1hzaRGG1LoqN37EUG-3zmkx_1KroBpuLZSow76uZ98kBXOXKDHDMOicCdQYfkR1azzpIHU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/31316" target="_blank">📅 17:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31315">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/31315" target="_blank">📅 17:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31314">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmmNMIgVSxGIMd2VnqBCPD55xh73a5LMkYcaahGZjiAfHoHTHfrA-q0WTlsDMkDwRe56xaGfRfKSvZAwCmJa4NlzwWxI09L1yGcHsgEdWe1ggHc3pA304TfqJfCqNvWIP8DXQdXOqzu4osNHDpqGLPIkgA1hV_1Na_NOGf9lo_TbMA4XQY8Cp3tVYPKA-34IU1lwUb72ic9rCQcSVOtd2SMGT-mdCmzw8BGOMLmjhN0orQGQGgDF4M7YpPN128f2skkFAjWJPDrGNsYkKvL4S9vPL-dyc_ZBP0xb56lD0yvoUOmpdlSvMV-UNj7ISzIZhlKAHMAaxkGF7DxRltIyLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/31314" target="_blank">📅 15:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31313">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRdq-Zj8eAkqrfcgV206J8Lo_c4YTFiBmGuddQsTBDdbfND1trCiLPr-hV14H9nmXwnt1LLs_ADSP9Z6rfuSZeTMJazUmAN3glwObkbsI7r8DjoYlKh0B9O2Kh1MLtEjhGdw_xYtYgn0jtEcoPaE5aonMDOwuUDL9maYW9M3aY_Kwm0eWsLUhEK1HxBVMZprNYtiJMx3970eH8lliAKRojEmGM7Xf0S9072_Cc2A5ivDtY5ZgqWpNgg4FDNDGJOF9Gok-nfsVfQs0SM3pTYDgwEudNuFQSkUvNaqlUacr40GwcAkDNNAoAdT81K7OnKXRwvAhBMvMhU8ucS6nVZoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/31313" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31312">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cldavU2EBl8EFmp7ZP3vUu0kvZsIAodDP9ZARTpJGLPxzz-FmX00P_5jtctr7cK5bqiSwK-yrniO6onKd8kA7ySj4v7A1CxLKeO8n6Gk-DsZHyyyjJKC5F1V_DQ0hu4A_qhrCzQv44DwIUxfSvY5mB0EfYLEQ5vsQbNn2LDHM4M2pGeZF6fNRTlKiuYTjFPwoTN69-i1C3nZPCjixW80RVTCKdb4IV7T1rD-v1ErFcV7KR9CoFUK2bRTGCOfsLVJw6jPVVHb9IiMTpbiGM2BRkvFiagddaJQcw25ADyfVCGsWBJjSiI6cUcWfteArfzv1hqgdKSdTfxiY8xQJ_DqfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه‌های پرشیانا؛ علیرضا بیرانوند ساعتی‌دیگر باحضور درسازمان لیگ قراردادش رو با باشگاه تراکتور فسخ خواهد کرد و راهی سربازی خواهد شد. او از اول آبان سربازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/31312" target="_blank">📅 15:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31311">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY-92YCHK81HXWDZg2LDs33-trlHwW-hEHNGoJRzjXR1dDTgfH6cu5EIbUoCCVauLqAbw2teLl1tHLTSC5qJFripwDBw1f6axvJhVWqTZCdkB9R7oVORqurGh19KU89Xxmrde9RgzUHxF0qQpnaxnLCTnXMsnDndvhQtS4PmOEWSw4l_hGGsItKiCZH_CDSwUj0Xq3O6sM4z1s0IJBIOFwYLcgqxquIE-mklhDbwjShzyUvvk_iX-r8ftSwWoLsb6w8JwG5FO5dmL7QuZes_8ou3o8kx_a5jBUCP77Y3I4jDZWr5HT9VvaVRIaNSYI8qB_Tupp-_A64IS2gTrJGkfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام‌باشگاه چلسی؛
کول پالمر فوق ستاره انگلیسی آبی‌ها قراردادش روتاسال 2034 با این تیم تمدید کرد. یکی از دلایلی که پالمر در چلسی موندنی شد علاقه شدید دوست دخترش به چلسیه. پالمر از منچستریونایتد نیز آفر رسمی دریافت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/31311" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31310">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAgEy4syLZAFjEGiaTmyFJsLtuwmYW_IftXE7adEHA5_MkphsnuEBTZHzRo44XhGguQpjpime8UUvmW1J-15Vtli6cBbCPZnmLMQIL1PSGvI34E6g0lXqGT0Gv9HP7k1Uf9ptOTS9sYQYKwZ1yTDD61AHbFi_qY-j6viU9XpS3009cGMb8PS1bONlfdQsANTTihXtJ2SXMP0PKHllaaxwqukObtw55ofkCDpn47kKb2DE23VSZmg_5EBrPeX1_MIv0VSgzsh-IM07rMBgar4Nd3dnh50vCZzem8Yg-ta_ZMk5dUI_r0-O8Fw4dxdi2ByVbKBE57CtdxshQ6x2wJqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیگ سرمربیان تیم‌های لیگ برتر در فصل بیست و ششم؛ محمد نوری دومین اخراجی فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/31310" target="_blank">📅 14:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31309">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQijyyUscIcDEZ56XXDg3pkJdKK2AuVEwE9k5Y1bWBNewJV2c2Oq__h1mkbT5c6Jgi3dPH9oiUmc2i_Pgqnl0v1Ymsk-gJfJ5jBiYAVNkw1BZsP3USvyfG0BG8mAdeMpZ4VMxxf4GG8p8BCwGRpyeLME3WBh_kOW6lpOcFnPeXAHvCgv5DJxKCkkxZthQo9fYtAcw9FZAxQHKLLYSDvdQMacXLiXTqpYgqMzqxJbsARIG6bNkCOpwo5X81nkEh1JswlX5kfaAkGHNpSkW_7NkfeIs_v3HTjK2omlTIcufBJb0902dNIjY2gTpXrI7ohpaZccMbJlvy0Y2CWn9cNS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
گل‌ پلی‌استیشنی‌وتماشایی پاری‌سن ژرمن در بازی شب گذشته روی همکاری دیدنی عثمان دمبله و فران تورس دو بازیکن دیپورتی و سابق بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/31309" target="_blank">📅 14:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31308">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrqTIK82KexzZO0Jco4EO7VPZvd0ItB_P1aPwpVApEslQt_IiesfgzrhhC4hh9pzCpAl_eE-JX88MrWtg6ze4g93u6j8Lwy1N_bunP_pJs1UCygrvSvLC2ofnIDji9c_HKHscdkfFxCjeu52T4zY1eE_HqNWp601uPdACyzV-jWOVqQDWfO8KMGJDnBkvjaRDdz5bDnvy4A8vhs4ooV8cw_GzXyXzjavcsGptHzcNilE7xGMVN0OiH2bX2o4-49lZXJy1Xhkti3o9Z5NOynHB9Ejxbkut4o8EUJ-2JqBm6lVF2iom-6p_YZIEXSkoY1bV6SYtguhf5m2G-M7KUI1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ یاسر آسانی ستاره آلبانیایی‌استقلال دیدار روزدوشنبه مقابل تیم الغرافه قطر رو از دست داد. این بازیکن ممکن‌ست با کاروان این تیم به قطر برود اما قطعا بازی نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/31308" target="_blank">📅 14:12 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31307">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTmyO_fekyb2uO7eVkuM6as9OSf7aWECeU_cNZ-Q892GipV_7ToJi7sBTWiK_o4JzPpYzRBXv6YB0chJDXta-aXK8hTFVGjmpP7UtDYol8PtIg2HQH3KIJ2ULCPAn6BMT-cibvspcydo9wlgA62zR3OwHdNVfUmXPI5w2B3c0H9_VPO4leAe2jecys-Bcesr5JgjV1AXEPpJCPyiNHcgCFWfos7XVbil1T_aoUzsBpmza-S-OmSYLxhVKeb4oElmGjh8uwC5AplCwa89uVmAgMGyAfIJPLfD5xYjnQyeHkcCQNljtdguSl95ACEtlktWXu4jb3MRdV0sYVoEWsHVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31307" target="_blank">📅 13:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31305">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ne2JTTFTvURc0Vr622vtA0O0NAD_UtAKFSJ6hVMTZCQov59Mn3leRTypcWef6JmgoqzJ0lc4VbiooK7jcgkP4qVgR4VTnid66zABm1yP_BqROguPUBEbeX8ACVb5UG6GxbwD7OmKb7om9C1duiTZKJZWt3NRdciAh4agZjUfAZMhLEFE6PZF-JDjGRnU1mMz4v66LX5aykdx5UkmpGmefVF131npQHg66_2cCeKvddIHISvkhCZ5f0x14kHemxQhNNUkTQgO7YpkyZGq78c0EhI5CyazouVfn_UReM6NpNYCQOI_j91w9k_SYCyxpOHMvPTNzKaLLaghK4E5J_PN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKY5_fmCI4U5PlHxbIcoUHWgBUi3zHeiSPz4JiMkGlZsX353wkvS8rn8FSe281XAdTuRebKmYLksAv8dh6vlhmndknsi1EP6hx_uY9dUHDMsMqhhBscIUu3rbHFwLvSeUtp6CTJXKXf7zItA0cnsNLCk_Kpj-KWXgU2ye6AIJIQI8zZgkPnvBClvdN1BJuAKV0P1KektRJC1C6H2t5ekrSXE59QBLufNxXXv5ioz-r6bi3ce2zw_RHBSVKa7_3b6DtXNuepT02_W6WahXohL0wA6r9-Az1c-b6-zzv2zgMZSuKBVMrKWZfYvF8_Eit6SKnKUPjIKDQvzq_Cq7qdvjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/31305" target="_blank">📅 12:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31304">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4eXTAFVWS30YvXPEjOcsJ7P7gygmKqX07Vrx88zy9y8795reVUfoMftLsTUCBtQ2NFcl0FtQEFh44L7NEu_KBskL29QlL1W8QO9SgJxuW6P2xBIcvBYxZUoLkvwft4p2cRmeP7yQFiFr0PYE8JAqcf8BQikPoFRuNKTida89z-VHB-Zv6KF0LShNfL4c1I-N4MmZL_Waui5VpBxqKF_1GZKgwYYmfCrzrliDGZ-X0QB08y4NoFa7PmtxenaaEWCV2Vdb2C_s4NadaPGG_SZxSGB0wMqCaGCgOlr-V6IQoE-eg_7GPAKUjAxOOTLyevCbqkJB6SIRLHO6wKKNuYEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
گلشیفته فراهانی با جان سینا فیلم بازی کردهه؛ چه لبیم گرفت ازش. الان دارم میفهمم چرا حکومت داره تلاش میکنه گلشیفته رو به ایران برگردونده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/31304" target="_blank">📅 12:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31303">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vu7x32cJFjWyLkuYAMcLyilhlwrkINRIgi7At7sJU2El6PG-aain00P4OXKF1Vwd_nkVmMuf-FdVBvcxVvoK2XrZU9733sJqg3vvR6i43TyAokUkJOeEpejNjh2mPfQTqP2kWWI8F--B96vO6JKhaqlsyjIaaQVemaFBGkrwhqzl1cgb5KA-8r2_cW1f1M1X-cISEVxgVZQqiBKiynIE7Pvarc-c90KiHQzD3HNPf8CLfYAwr8TTHcwWqxc__dA8ReHTpzfMAon2AbdKTWiUv1PcaFR37tsfM3CyNugO16ujiH8IBBZVw4RdiPRQASqUofeQ2x0EdATFNehlucugWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گزارشگربازی‌دیشب‌النصرلحظه گلزنی کریس رونالدو: دردوبلات‌بخوره توفرق سر سرمربی پرتغال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31303" target="_blank">📅 12:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31302">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPJsjaMYfzH0GPtNS72OEHt-X3XkUaz3oJ_U8xtEjCzsTBVDIrmOXtu1lZRaFKcsk6GVNXVeJkkUrQU8za-WgQuk2sOFKMgN-dRVWETLDGxqQNgPyNT-gMYzDkEU5eCeSm63dZw8H8lnNwXgrB5YIwIGgeWVMINeL7gligtILMI5VBYTS1cOj6EhMbU53xXACMHTrQwJc82QaXEJs2I3ysI7PmpRue_Qd2kYHN6WZsrwYTCd7_kFzI4yS9I-JuHYHwH3BKxLZ3theI_Ii29iWB0cFvIkNyuUFaLLWFG5TXnbDcIIA5VIa9iDMPe0NxE0bnm-rRTx-KI_kdCYG7E2vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگااام! مگه میشه؟! صدا و سیما: مرغداری ها برای افزایش وزن‌مرغ‌ها توی‌غذاشون تریاک میریزن، برای همینه اکثر مردم بعد مصرف مرغ بی حال میشن!  نمیدونم چرا حس میکنم هرروز از این چیزا میگن که مثلا مردم از گرونی مواد غذایی غر نزنند
🥸
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31302" target="_blank">📅 11:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31301">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgzwYzQh0aDCYyR00Z6QTJheb-PqFjJYI8Oy8IM4UQYDyJpQYJhTKa4tC0cyIXcNYXpyyxuXXbGffHW5n0NOYZMLY9-NmdEgNTfK6utBpNYT_JjqxlhDL3JoD7zcx6rrSo44OUOHdMRBRmThjZR0C3F3eOF_bbxy_aWnhqfVD_5grw5WVz7iUkfuLS4WivpPOqQXDsjzX6ZAw7H8MaslLX12syZQNmyOKprvn1e_F37f0DFQ9LoNYTiO7lZCw6bY8sN2UZD6qgSUfrhjyZVosSYzwMJfxhjwIMz81utprFNP7HmwIDjlVYf-cGRXUsEfAyBwcVqbV2p76hEXltXtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ایکاردی‌بالاخره از وندا جدا شد؛ درخواست واندا نارا برای دریافت 250 هزار یورو نفقه ماهانه رد شد.
‼️
ادعای‌واندا نارا مبنی براینکه اون «شغل خودشو فدای زندگی‌خانوادگیش‌کرده» ردشد.  مشخص شده که دلیل‌افزایش‌شهرت‌واندا نارا ازدواجش با ایکاردی بوده‌که توی‌ایتالیاخیلی معروف بوده. همچنین واندا باید دو سوم هزینه‌های دادگاه رو هم پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/31301" target="_blank">📅 10:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31299">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=hervEbgGeWuSQ8ybHf5g8glqsD65j80dsT7NoXi6rFJZuGVHg-Xn6k7HAwhkU4lt5cs_2fUFHVt03V9Vxc3z5qDpVSzVHjA5dw_wo7pZ2xMqH_tic3CsOPAD28qjRFuMGKjjU-V_jJQYB7g62JiKC-jIVSP8H_2cQbAH7myif9FqXk6ETVxxuj01sC0neYEnjlCOEIwJhKfogyVQ0uagMGGDXeLdNydlXi9Bnqk7QpI0DN0oNCiRXpEPIRjez_YU3eomY3gRIa-7TkX47TVn6BTMQGx5dwDcxCzauoW1lNnngoIbvT671Kq9bNTZuCahsvxCxQ_m8Oe1-Bm5RDK6mj-L28E1zpFbtqEbSXI0aGbsI-AFppkCp0bAp2d4XQrVAvaYKo4N31rkdek7q2N9U9peSCnxL9gMmCgEQbbYm0hd_lThPVAJbExPCgXr169Qq6UKYI4qprK0Fok_bV9MbdmvmoCCw0Biw05CBVN6GwOQmTrAtzAzqjnHgBOL0S6qgkJMKfWikYQOEO0ag2uJt-iiMnisCMyOfghn9qCp3Mcqrkkz9ykS9-W7_NE6oLSOKNctFRQ5DpPWEuZtu4WzOhvnvN3Q43m7rLuDkd5RgKCvSMaLzagroRAMDl_HspPdSieSxu9AJ0Qp0UE79U-Fv_FPfFcmtMqRrT0NXAudYV0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3341162dbb.mp4?token=hervEbgGeWuSQ8ybHf5g8glqsD65j80dsT7NoXi6rFJZuGVHg-Xn6k7HAwhkU4lt5cs_2fUFHVt03V9Vxc3z5qDpVSzVHjA5dw_wo7pZ2xMqH_tic3CsOPAD28qjRFuMGKjjU-V_jJQYB7g62JiKC-jIVSP8H_2cQbAH7myif9FqXk6ETVxxuj01sC0neYEnjlCOEIwJhKfogyVQ0uagMGGDXeLdNydlXi9Bnqk7QpI0DN0oNCiRXpEPIRjez_YU3eomY3gRIa-7TkX47TVn6BTMQGx5dwDcxCzauoW1lNnngoIbvT671Kq9bNTZuCahsvxCxQ_m8Oe1-Bm5RDK6mj-L28E1zpFbtqEbSXI0aGbsI-AFppkCp0bAp2d4XQrVAvaYKo4N31rkdek7q2N9U9peSCnxL9gMmCgEQbbYm0hd_lThPVAJbExPCgXr169Qq6UKYI4qprK0Fok_bV9MbdmvmoCCw0Biw05CBVN6GwOQmTrAtzAzqjnHgBOL0S6qgkJMKfWikYQOEO0ag2uJt-iiMnisCMyOfghn9qCp3Mcqrkkz9ykS9-W7_NE6oLSOKNctFRQ5DpPWEuZtu4WzOhvnvN3Q43m7rLuDkd5RgKCvSMaLzagroRAMDl_HspPdSieSxu9AJ0Qp0UE79U-Fv_FPfFcmtMqRrT0NXAudYV0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
تفکیک 980 گل کریس رونالدو در کل دوران حرفه‌ای این بازیکن؛ CR7 تنها 20 گل نیاز داره تا به رکورد فوق العاده و تاریخی 1000 گل زده برسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/31299" target="_blank">📅 10:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31298">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3l2a8N3rZmtaE3E6jmR-B1gfy_56lg0Dxe5gz1pUtnc3VGYm7MsMXGdxAL9P247q2bB9mZOD44MvAmaB11D6hOGxtvdsNSLWOI5I8SjJrHIPkTapONNfofhkoXDTeit3-tpX216JTnHmqKFntzvI2Qm6xHUpvcdfr-inrhs6xNDO7ZWw2X8S2FPZSh0hbUoA-VjQTEhGfZSdCgRuztTVLwr4w6zcahBVd_5z1-7QcSdrkloVVLDdI5I1W3sf69O7_cJMVWYWih11DLA0g27DUvWDJi-uj201p3vA_OBi-kEuZQ6b7Mf5uHsbGi7US-tLAvXw3nx34CWCf6vFevXnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جدایی محمد نوری از نفت آبادان؛ با اعلام باشگاه صنعت‌ نفت آبادان، محمد نوری پس از شکست مقابل تیم پرسپولیس از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31298" target="_blank">📅 10:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31297">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KZZXCJhnzTQjwXDnfrIP_QYymPNNrIghuRGduyshYe6Q6hWl4mlO-A2o-NVdPJjrRrvB3KtEnMJYz4il2HRrOcTdKu04b4PPHHzA8hVSxkP9Q6ftDNOu3jhRA6v2aXBpTrpz-43KBTLToMuUjV0QiwQb57_nUtfgL3y3XLaaGgm5TBHSdyTeAuxQdtUf9AOlVuZ1y5UgkLheRD9Qy72bAk4s-3FcVh7sQJXPfD_U0oAPuhlgH-4q-uZlCD8CUSEitp0Okg0T_MQOP__pPnoNvryjOXWU6FJfyS7eD1PhXe1ResbRNIlxwyzDPIvy5vyddbWcg-pJzxDQgejJca7K7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31297" target="_blank">📅 09:41 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31295">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uULLWFK_hMwmKGsgAa8CWZZRYUKHmC9vsv5g4KycXfUx6PmZcIzqesCPCnCe74duQgj1ocf8BmPmw7XpNTQpAmElXwvTgWSesa8nVDVmv6K0GzAtb7HXHJ5VfQy8-2ubXPRpI7k4BSXe965JoeZl0lgC47--3yEIaPVegRKBWp3ANpZ02QkrpYx8c9oz61pEIN16ZfqDBypBENAfvI_zxXj-rV_GZKfv3kclA2hwkBydsAn8iilJhyJp50ffohvUlRS0ZsHnDW2K09c-LYB9chzIBVNoTeM5jwIsMtggeVeWBCdoJaIjtbXoBplqd5qmKomPAMskTutNFMvECmCKNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛از تقابل شیاطین‌سرخ برابر تاتنهام تا مسابقات رئال مادرید و بارسلونا در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31295" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31294">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLmAKcaiStnYiUWPWAo39nahfBi0A9vrwv7ngLgke5-Q-fSlcL-2xV6bALmimmyn79RZk0YoMt5HHPd9Nu4uYs2Yo42wTrqjGWOZ-iFgQ_qkmA2PxGyhyBgAPSPVn0QqmzgwVOEncGUkiE5m1P5pXmh_bG1NHOIucLFzARdvNJbAAxPHDHQyL1IAlo8LZr3k6eLT-bTQEAGiBacdDHT9V5Tk3YWQYM9ZlWv46dI6xfnPJTi_ofA1xuaQlByuPDGZmPOhdVV2bNGOVdaQpomLwIWwULnTbvvY_kXP5gi2Q8dT40cO8GAd78IS2G4sfNueTflVz-BIz7CG7APE85pnmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
نزدیک‌شدن پرسپولیسی‌ها به‌صدرجدول‌لیگ و برد النصر در شب گلزنی رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31294" target="_blank">📅 01:24 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31293">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7qadi7nNkuu-SErlmtZyVq6BTzhyFuWcsYa_h_LeN5GSL_LZRgTht9Jv62gH33NzIiyIXimLQ1QEBU1hUPbuFV-WfzThiOjLrciTT9QMAaCVY_ybzFf9aUUUMKIq7_D6FtbDecz6XrigbEHsikunmsYhVVbYLqeA3RULF4sBC1AR2Jd0T8nFgxxMZvttKpgp7C4NZER9OHANzYHyu6sUGaPd01UuDnQrY6Y38liX8Q-n1iAmBLaXTB3KNPi1R98HcgmwShBXBl0dzA6m5wRHenjbJFGUeBDyx6RkTiv2hIpWuekN49BvF1U2IXhy_auvX1q5Ew1Mmvygl4zpjGNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛برنامه بازیای معوقه هفته هفتم رقابت های لیگ که روز سه شنبه و چهارشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31293" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31292">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yz0d6ZhUdde9rX6Z0vMNkqBgiYFqSR0KipwKXzzJHSC5PFH4csombh6jXYsVGAS1ZMI2oA2RzmD9ohr0feZbKtWUOmwEIc8hJve8kwTPGAcLt14yb06un3YHIXPeZRibCwA-vgh6IbKuVBkOYRE3n3h425WgIE1nm23ITIgQ9AlVcb5gqdJ1uP_7Ecq4OasMXXviXb8YXKp0dPaUBP7dnWjHksA9PMtzOwkF-4WkeM5mQiSi9yWk-DZ39iQTYiXNH0TGTOjyjHmo9HNH5pzdUGcu6HR4TL6ZskIMWqpfm76zrESHYdGorbxECVWoSIeB88DOEcInxBJ1WQlp5ACxWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31292" target="_blank">📅 01:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31290">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQhUUDLMF46kQWNz2WGKbn4c5UEd72V7YVDkx8qqy0GDTzs9ltSKIFJyZviBjIiTGnLWJ4spk_CSs9BNll0w0gcx-FIBilg1D9fTASb_nVpw-Arhn4cfI1AhCXkrgP8iiW5UG2WpNf09_z1FMMfnUHbQ4NAzZz3T4Op9E-yoy0sGi-nb2NmRn49XuoiyJ5m0Z5JZryN8kZtUVWcApuRv1uO1eA4mNLOd5SWGuPnZO1diBvlOHhkjbOt0c9C8dBLBkOGbJ04Lu5vl8QkfnJoCL7R6-DxEDMRTH5q3M-Wkhz-W776KW9Iz3NdlDXfQeyaHYQCB_siCMq-A1sJqL3-NTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
گلزنی کریس رونالدو دربازی‌امشب النصر با الدرعیه؛ این 980 امین گل کل دوران حرفه‌ای CR7 بود. همچنین رونالدو به اولین بازیکن‌تاریخ‌تبدیل شد که مقابل 160 باشگاه مختلف موفق به گلزنی شده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31290" target="_blank">📅 00:36 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31289">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDyjIWhksiCzYzKNFJxbg1wg5yWogtHm2811MhYtQ2Y4BV3atjceuCyG8erRFobsm0XOsvveaQDJicCPZmxhJ3VUgu0bOQdcXfiOljRcXwXSbKIKz_krDavu7fTb2LSgDWNiR8iKULkB7t4SmETUvhvEIFkNdNIZv3OdmlBcfZBneejRMb8B3FOSR51n6QGG_nmcPqRfzaxlA8E8VXa-NOP3EPewy_aGw0IIqgdizrhzNnOjUtLKbJxDfbBbzCrMNmPGyTewpb0aiaq4URkgEAHkz2uw-fQQNcLetkcy35qnbR5XqRqyrasqGd3IFxMk1idQpJx4l5yhDVBteVHZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دختر خانوم پا اسکولز اسطوره باشگاه منچستر یونایتد: جود بلینگهام بازیکن مورد علاقه منه. بنظر من او در حال حاضر بهتریت بازیکن فوتبال جهانه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31289" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31288">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcUfRoutML9IOS5ZluyshPKFBDL9yxYYZaU_z_-VosLRnKIVKd3MuqUWTZ-OQhutAJlylAPOiswiiHm1MJBt472crUYrwr0VtQ1_21lksY0bsalBsQjQDIzo4cb0dcpN8gB-lRCUylmC-HD8NM22O-GCH0cp0K8r9EA9ItHdBabWBRrrSWxmYSdzYGGWfo5mGjM1AmuEfLyQ1S3KGh8VCIy7cis_s_XxROwDodqEVsZsJyEYS4buHOJj98SzxNv_T33xsj-Tlv1BnKeDQsC9_NzBdfeBK4O8Z_LDLUJAxoTiScWXexrSz0L6-lgyMimLOhMTWwxSQy_GAQTDuQRoAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31288" target="_blank">📅 00:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31287">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
سازمان‌نظام‌وظیفه‌به‌علیرضابیرانونداعلام کرده تا زمان مشخص‌شدن‌وضعیت کمیسیون پزشکی‌اش حق خروج از کشورو ندارد. از طرفیم نکونام به مدیریت باشگاه نامه زده و گفته بیرو رو دیگه نمیخوام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31287" target="_blank">📅 00:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31286">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzQNAF_EicJpAaDkl-R514qvNiWypJ3oj6NYTzCrHOnOtheJMy09zvZF0A44EYXRmbCDIVNO5z5L8D2_jcotZ9lOETpDB9hmMFG2PoFzhXiNtELRJ47mL_8qcGKxUUtsVKSkKxXBBnAdQY28TSr9hnnX53duiFc-nmg-ze72fXdxXM434ZHpP68ZNzNMFroeug4wDQ3f7Dd3LyTAt--mKFTqp7K1JOqbDcnWRwRmhlar-7td_0WMyZXFqLu1WIrOrhaZYCmwsFs2duoaVjKGYlKqky1FipTdJsPZrTz_F-xgaBY2COqQiCnidihjohWaYF48hrkd_dAsI9aG-v7VxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ علی رضا بیرانوند از هتل و اردوی باشگاه تراکتور تبریز اخراج شد و با صلاح دید جواد نکونام برای همیشه از این تیم کنار گذاشته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31286" target="_blank">📅 23:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31285">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUIk85HOso4TwVVDlkBKfbVf_VcU-3ZodZvIBNAEGG0ndPuk9xEaCLNK8iuiu6sMRJ6UCBsrccrCy1JHv-yLkhtVooX4zi44YinUwUnAYlb62Zrk_kPdw3UqiYyjeuXiFa2T_x8G-LdekAeV2eHY8cC_nK6KzsOhpxtPyFzT-o7i_skfvOirk20eZqpaxoPp6tJuLWqX7itjclEWVNKLwFmC1EWNu6-e7nOFduAstURO7Dbc8TTpj4hFHd8I3uPnf53oeXDuSDLxNyyCfk2MDCURgK9q2jdcBOJ1K88X6MG-YtvLzVdtWEsTqI4ASyB6NIWrioC_sePr_kKsNFanOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جوانگرایی‌بسبک‌تارتار؛ حضور پویا اسمی بازیکن 16 ساله به جای ابرقویی نژاد در ترکیب پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31285" target="_blank">📅 23:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31284">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pn4-S_WY86x86wu3fTlTq-SxNN50DtS77NLPx7IgDql3hwuYgD0Vd7PUfbsh6qoiwBG0iJiirWSewTqLW1ZRGoAlZ4tUKzS5qCZeir2tRHc1zJGeLj6PW-UosNkL2OZxtv9Mb4y6dMokSl0b8yofg9ClWzF_AZouu3FfPnOxyGaPTyCTBTCYvX-HKbgZUI5jk6FA8a-2N0UKUnuDp4O-70SXFTxlLpAnfaNeD728nCcZ3QPq63-MG1M5YQFmT5kvptEyzAfJLXQLzVneuQWb3zXzgY5bIVbOPqQCUw_093ioch7_3-2bvCjhLOWdWLlOSTXdfnOY-4y9MFteTFuY0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج رئیس فدراسیون فوتبال: هیات رئیسه مخالف دادن جام‌قهرمانی به باشگاه استقلال بود ولی این مورد مجددا در حال بررسیه. اگه بخوایم‌جام هم اهدا کنیم توی مراسم برترین‌های فصل اعلام میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31284" target="_blank">📅 23:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31282">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKQHTBjiZH23hsbovGxb1b_4xV-9LhCiQPVWFXJK5P9_HdWeS8HGRdKPaeiy-T6wPZGpD82FkNlgiKbr285wXSFL8V9FNunDq88R7EioJju1ddsV-_mNuFKIEJd3PjHYsIpioKkOFEhtNJLXxNqJHX-mYGyqAvAct83NDPfEDIJJk76Mo4w9jQmJCcu9OhlKPKqq1643IVb5pgjK897PYqQqZlPfmVFDYNFCvmr8DuVgYmIENSCAQSotX7wrLlyg0kwXeAXWWkZg7QGsP9NDsUwS_f9JZCRQmbs4ADiKorszsEcpVb2yjHVpGPVb8xPhGdP9o9_U4SKihDHzI6lXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvgdfb2LJv69F1AeOXkBtmcFBpGtXRJYvTfgeJZ8tBwAe_x_jPX0kVtTlfTdjT4mCH7ItHenk8Cq8IPbsGryw4_jAZp9l_XPTXOOO5XMIO9DgA4BQt6kqOSot_pbNfnT7PjUbzBfDbr8ThVsljZbAIcjAnIp1grSGqqnQATjG695gGPok1YO4YrBXclY3s4Gkuv6ltn9nVSdjGzpoaKbfE2DbGkoVY574MsdtZPSQmWYFo_A9ZrOSAw9Q9GyLcEF6M-xJg46g6j3rL9DRNt0ruFMafkEezU0z4lZuDfQPKK-yl5--0rhpCDq9hHl6NEJiG8GzKNjqIuHrjFLuPg08w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31282" target="_blank">📅 22:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31281">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGOEwG5MbXjcOL9uAoFnRVbwen0g9UMcsMtA8rMwU29vM4bl9lkShP33a6z2RsljJul1fs0PnrNt2p_5nfsowywDLZPNAdCAu00x5KRplis1v_Sp2l3zGy9sRraTZLO7IW80qsRT8e8eQ-8Gi-LoiwqfylbrvqBIBrKNmDgc9iFzSPTRLR15YNIXRqCFhOcUk4C2hZ-YyNMhYJTScujq2Xas963INA_bi6mTzQQ97H4yyWflYIRPjBRupyhJ1pobIB4sCC0GL5YBRQR9ExfFmLXGdS4IkMI9DcdcvTu0nngM5qjUHGRwE5gfxyjZv0v9d3-leT_DdgTF654w6CF4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31281" target="_blank">📅 22:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31280">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMUWHl0B4XY_UZX2dB3HOlZkF8uvZ9FiQlMuISSggN8WqUbmVVBPxnC0TCX-Oa2eU-5dpl5bhnsfXK5pZBlc9W8zegmBE-Bi40M2iJFXkzO3emVqQpiT50b9E4-Ji3m_oPaDLFMXRDppPyhdzauPsEfdV44cbce6dU0sdXhGDsvJpv93vyE9VkyEACrkplnMQ-xxHmq-SmCKYHnkARJaB0DyMkC9UKUdyJ3ptXHbMZ5KHCCfGEofby9W4Z8-feq0-EcmnQcDIhtet7EQnZKTjfmEBxlN_A7sSGpJiotzTZQGie2VE5a0qNeTNxaMsvykalHJFHJP0lD_CXQp40j1cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31280" target="_blank">📅 22:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31279">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31279" target="_blank">📅 22:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31278">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31278" target="_blank">📅 21:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31277">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgfbCj_ha2fafQwThDe6j_7EMML06ZqT8j9BwXMNxzcxKJLw8pdVpiSUKpDUsNDVcRA_4VWibO1rebSQhThPodwxeXszmn5Jr1e02FOoj-Psj7o9ElXJ8HZ4YfUPmBY4yNKSz5c7aZnrs3xMKPL_d_DheR0u3Irck1LwoqYjrGkhQy7lnh1O15ktH_FcUyG5RSnE6-FzqTL0Aa3o-5J8BqtwOUVr9v5f0N3w708Z6BeNG8KxVgwH3SWfF5iqu3W0HsA87eyW8yQoO7qHF0w9NAqPIzO9P0zxi6RTwGlJISpoC6JceRP-6PHjhTqqSWubkE-EBr0y1-LEVhMKTu3sYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت باشگاه‌های فوتبال ایران از ابتدا تا کنون؛ آبی پوشان پایتخت قدیمی ترین باشگاه ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31277" target="_blank">📅 21:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31276">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJ8lgLVOmdgiUCX-KkkAfkMXR_nfJasGx8Ffat3mBkn-crTegdiJtlJGkofRllEPob4HLThdzowEGRYYNYCfq5EyGKRuVBadu5R76NTorNz4HoPScbK2zZaXhCMop9P9DVMLNxbNdoYHjJiwaQ5naXa_AtYkffNk6PHBnsOBeckfwUUsroShdmBAfc3-uQukozm-ttLEq9r5w81YfA3DpdvLf8CrWYNpb_Cu-_9l4t0Hg4h-zH8B2zQXwB4BnK70sV8EdrjvUhylf765o68lKaLIIWJydhfiFOZNfX3-sPjvcD2bKfg2KVyTq9o4DLYoFSCKND9M7PpgzPx3PLg2Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وزیر آموزش و پروش؛ به احتمال زیاد مدارس بزودی و در روزهای آتی تعطیل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/31276" target="_blank">📅 20:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31275">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0vMYVSC6AuBWLHYziKvJd6y0Zst9GzjvyX9lg0GMU21UiQorJM6QRKEKU_7YUenX1imiEUMU5zKBCN6t8-48A7RQvdBfzevvvyRY6dik8E4-CVV-xdiDX2uQjL8nscWFTkETsXR8p_OBbg-eL__yoixjbu65UcbjpWS7eVVKW4gxeyWx5oit9hI5c7EXiMyfuDGJjQ83DUjkPgn_QjvXu05xnEKt5GfiGJg15-LPMak2IdKhxpVmwCbAvQ92J5ziwNWmlmbMedw2Lu7E6p26Uv0dAIP4pOAakexEen2-oIx_8zsM2dMVE2jbKaPPs0RrcdUOWoIjSolN-To9UNYow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31275" target="_blank">📅 20:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31273">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wx2LbnvhR47PhWsHXwnhsBmQC-2PteawVjfXvznND5puV3-EbIDyUPsVKEix_qDaCkHxk8kGB3YFQVIRuY2eMMou0548CXFmNKUjVfIrZWQH8bQoIzFsgLDtDILJcKHbvfNXPwEMfR5KVJtZZsNMQUPKACQWYPPjyNMgsaVXGHXZanCsQm8wDPs-xAWDw0aGCP3GFqzaBCEO8J0y4inAYUslCD8Vo2BkTlIXGw-46hgoO0Nom_tFn25aGA3eb2wjFUjwFDzRpK79P0MR3og8bYIA_b6jKoWqwPdLLYSZVJO_WltQkzhFtccKkv9yL0M3p7-Ra4GCGIPPkKXdoYRR7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dhw9RrzEYPHnV7Y06QT0xdGuHJ6MST3cyCCs4EDvxrDKswb5OWWAf8Mgxn-t-RQ5z-vGSP_68SOSrCwFrQ_Sml5t0z_0ej2IYiBZh0RIqpsaSm84thQTcjDaWG4ZOK5Rtk8PqQXDfg--Wx1vUhWkYveaDol7U0G9tl7LeON_vV8JILKZLMgu_8yktBGcjUH5cckKjGzgacjmLxPaAjcVPO2K3qb5LuBKqtvZ6yx73xP0WEija7mkzmK2_Rit3E7ACfViUTkBppq47HJscN8ROKtGUOdSzQXk7iIBfDtckVjzhmuWRVoTAS67ksqK3nHpDX8tuiXM0vajTaA2kFPpiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
تفکیک‌ گل‌های کریس رونالدو و لیونل مسی در مسابقات ملی؛ رونالدو 146 گل در کل دوران حرفه ای خود با پیراهن پرتغال به ثمر رسانده و مسی 126 گل برای آرژانتین به ثبت رسانده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/31273" target="_blank">📅 20:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31272">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=jXLPK2KuPT1p6w0aiMXW9fNLEupYtZOeAh6YALtzual1QKCUO0MAX4GWsHUZSF9YVBWejQh1VzIfA2iK2GerThao5OWjsEbn_dPGQGrN09jIKGM3RWBO4ksNeF6GYjjvLqL6O-OjpDzUp2lpUul3gsi5QBWnU-obmMlpYRkj9q9OPFJDe27Jk1LXvSLeGnNZxAIcL4Z8RyroJ1gPlQb0IiEHzTMWzH5KWWn74L4Hk3EaM7oFwL9GbkvKKIQJbAY3c3Bb_K27rk95npZW-CIYj22qvp5sscWq4LSSID3soQLhzPXcq0reLGgs_PRBv7p_Seb-8RN60C2Cw7KagOzbKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e9e6b867.mp4?token=jXLPK2KuPT1p6w0aiMXW9fNLEupYtZOeAh6YALtzual1QKCUO0MAX4GWsHUZSF9YVBWejQh1VzIfA2iK2GerThao5OWjsEbn_dPGQGrN09jIKGM3RWBO4ksNeF6GYjjvLqL6O-OjpDzUp2lpUul3gsi5QBWnU-obmMlpYRkj9q9OPFJDe27Jk1LXvSLeGnNZxAIcL4Z8RyroJ1gPlQb0IiEHzTMWzH5KWWn74L4Hk3EaM7oFwL9GbkvKKIQJbAY3c3Bb_K27rk95npZW-CIYj22qvp5sscWq4LSSID3soQLhzPXcq0reLGgs_PRBv7p_Seb-8RN60C2Cw7KagOzbKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌های عجیب و غریب دروازه‌بانان باشگاه‌ها درهفته هشتم رقابت‌ها بعد از اتمام فیفادی مهر ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31272" target="_blank">📅 20:03 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31271">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8_XuJZki7XF3CAbsPBuOERRMcnwi3pGAELNxmqFaCe5q8rRw-0iJKl-dZoQkSwjP3-Knue6e69fGw1RWukklMz36hwD1g5iHu_LOVkh63U6J_GVCDTAxNFDWoIeEPMNS7odAkVQb3nqqKeuZwcSBz5I8AXFuRLvqo0q6NMZMDNqh0FbzACWOcHloHP7vxRdCmY_309lyQCQE35yDAIgAi5fkKJGy_9zVM8YxcN926y0Fi2yRem-ivZeebUBi2Zx2zUDpk5xnH5efm5o6tA-42iM_wY-uPJvIemrpKuEGls77KgO2Dy0Q03SQe0DQo0exZo1gA_d-o0hEqZlzn95NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ کادر پزشکی باشگاه‌استقلال به‌سهراب‌بختیاری‌زاده سرمربی آبی‌ها توصیه‌کرده دربازی‌روزدوشنبه استقلال مقابل الغرافه ازآسانی استفاده‌‌نکنه‌ تا مصدومیت امروز او از ناحیه ساق پا کامل برطرف شود. بدین‌ترتیب‌به‌احتمال زیاد آسانی در…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31271" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31270">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان هفته هشتم؛ البته بازی‌شمس‌آذر با پیکان و بازی‌های معوقه هفته هفتم بازی مونده تا جدول رقابت‌ها تکمیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31270" target="_blank">📅 19:55 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31268">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwZ-UEEcvt9znnPfVk-neCS54YekpDyPrhfLNWEPIY0QURvoMjxn-WtjnRFn1rS3GxYMeF2ZAn7HR39zLHyuxMmgIsQvpUA9mpTtlasUsK8ek5iyzNIdULkhKFNsWiuaL8LNmpzs1DR_7hAEaMdE7H5UDfG32xyMR2RZalFaDAKTSqUfqzi1dp8YJpcaaDvhaVRxagHcOUBIKTruAGRIxnLOBPMjUIOo00yM71CJ45PiWsinQCYY8kLgjhmEPKP4bI7Z9Dr56BfbBGgguRt9mcQjb0nLtYQzlsq1_zExZ5qI9YXBzJkTh37pQQykBuCUc6KzNijVxUauM8vy0Kx7eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ وزیر آموزش و پرورش رسما از تعطیلی احتمالی مدارس به دلیل تهدیدات جنگی خبر داد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/31268" target="_blank">📅 19:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31266">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g24UUBVjCgmNhYYFOBq_UFvmmSCFkB2WQAriKHHLAmr31mhPyMUHLWKzb0HqOcqkJNsrV-ABK282pNAwXV9657bEdnOVuyvrBhlGGO1js9Ot407uYYZCS7EBbbPn8pD1tvITsBvzPpwTivwtwyUvv5mmBcWLz2ZJvx8jdfuzVftCNBNRSN8ww78-88jzOK6AvRDYpvFmyT9YFdeUngJWxBOnfI__XMbmCzrsMCsbClo62ohsRDTM3SZuja7IEFZ-ly16npMSwwUxFV0YZcC49oHt0GFC_aXXJn80cvfWWeVpGR7DdmM52OqjdRj_o90zhZrDyWVPJPyQF2aXEn3Yjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOP9WqTXYlYh9IBAC05ffdiSOkh5Z5KMlrdItjhX0vVyA4wMRTT2OrQ-MJkuP6x3_-vYotTOW15zCoS9IsaBtG9ye2ol5Ux8rcyyC_frtwLV0mpm8mpdZLhmEaw66d293Ei7AuC2Nh72vlb6vZc4m72lOlOSQ8JbSxXxjbHXbb1YbJcNWnjI0Xd3JNqpbPWKtxJ9gJFIv2qljt5SH8AyAF67aMMw6-OijjgO05TWl5kAMx5FXoRDWO1Ba_V8XXsOGQhyiR0ape40l-E2GJxwGErQzkp06K1ahygmwSEKkLUOBnDYnT69Qp0hoOCLo5SGcdtImcJ3UV3ZbAhENvTYug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بانوان هوادار پرسپولیس درقلعه‌حسن خان.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31266" target="_blank">📅 19:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31265">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ho8prDxgxMtSK9bJ6NuNk7acTaO27zjNbeds8ttl-HvEmyGONH_n7WwjS4PAzvLs9CyseR6XenOYc53eKBVU2gUmagtvctG5pQ1G_-N4pWwD2bPlg2NP54ZCnlOHhBKn8fZV3cLhrjO9QvhVNLNca1GHFrcEoD0iwPLrw-hNUJBy2oDZ5L0kyR7pb7mATTfw7TcCppDipt1tGZ_u36DG8UuS12gIWq8Qun7zIekkWy63exORsd1Wx3fPBdIGNZb_KaTWzmuCC9H3ZvYC_-PGyRicn-8dzkjqWi2iRrKrQwcj1IL346OK1c3p4FXoG5psKA7YagmWrFcJWni5wbkrEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31265" target="_blank">📅 19:08 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31264">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTSLEyGmr-uIy-9vspeORZzpaNsN3-nGXLf7p9UbCi1IRnskZ4dLt55fLKv4dZKTlPAerV1Ozf7-Rsb8yJYSiWNLoL9D-3XITvgeuOlJKdjv6ejKM7tTZG2fyW67yras8pzOFeY6mL1S7lP0zFGwg-atGkAIXCaS9UOHCi6OfkR07vZpyxE6cS4NDwSWGueaC1sT-vmRAtnDTDXPy0qu6Qm2rqy_xy0BqH6HTgKJ3FFWdvGOrFj-zbWAa-g_DGOT_oqwHU2Klam-nowL--0pb1pdzG-LmU1RNpCd5rYAWw1XkJdjUrBvyuLlRS5ksjXPVm-xTVC7pk69JfDLtxl5Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم لیگ برتر؛ دشت 3 امتیازی و ارزشمند شاگردان مهدی تارتار درتهران مقابل برزیلی‌های ایران.
🔴
پرسپولیس
3️⃣
-
1️⃣
صنعت نفت آبادان
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31264" target="_blank">📅 19:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31263">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ46AyOM1pw15janC1JVYCxBlvKrosRRJpVdFAPTCLFqhSN7vRJCzAw0u9V0bWjmC_24D14RQSfuIk5SgHYlC-0ndbVq9_V9vJTx48tJIsinGbI94WQlBRzYUDRdtMU7qeoM-0gLVoTiGAGezmywxbnfGkFwdnmKKBe-Hn-EMXKhbTY7KS1Ti_66XMZ9G4x1wuR6FdvhJbN96FHxOjFX8viWE-7mztXENgqhD3j5zCd2984vAlRDTFxPt1RyCD40U8RiIQU0mX6t16UFHlw3tYz05I6FNuIF-XN0t5BBGHu255jh3Tm0qODrYeh849YAN6ukxIBURzi0ZQ5Wgs_eBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31263" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31262">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/866119f609.mp4?token=U2j925MPY1c6Qj5gfD9Nj-P5iJIOKORd8lEmYZmPGf8zOxrK6y5yKsfV5OQmKeoJtzfdyDCxJnDA7fcMmw-a1jcbOetqThGQ5GAkZun9UgbT39hdWHpZOO3HaZ6RyXj79nH3MM5aR0NcNmbrFb4P53E_xYZ7cQkVeifVRbHMBB9ZG6HEDBWRZpXDRaGXWYTA2W4-ZG2OZ4eDovWELqn3lystZwsslJomnOh-6CaNfjVxeNVu1OurehuFUHGELn83EWVjC8L2MD4FbzsoWRcBqTH7U3-JxSAlz5nruezJcwByElL8CCEKLuNppWYjH58GmF6_rZ6YIcvDPlBlpORQ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/866119f609.mp4?token=U2j925MPY1c6Qj5gfD9Nj-P5iJIOKORd8lEmYZmPGf8zOxrK6y5yKsfV5OQmKeoJtzfdyDCxJnDA7fcMmw-a1jcbOetqThGQ5GAkZun9UgbT39hdWHpZOO3HaZ6RyXj79nH3MM5aR0NcNmbrFb4P53E_xYZ7cQkVeifVRbHMBB9ZG6HEDBWRZpXDRaGXWYTA2W4-ZG2OZ4eDovWELqn3lystZwsslJomnOh-6CaNfjVxeNVu1OurehuFUHGELn83EWVjC8L2MD4FbzsoWRcBqTH7U3-JxSAlz5nruezJcwByElL8CCEKLuNppWYjH58GmF6_rZ6YIcvDPlBlpORQ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اولین گل‌ستاره‌ ازبک سرخ‌ها درفصل جدید؛ گل سوم پرسپولیس به نفت توسط اورونوف دقیقه 85
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31262" target="_blank">📅 18:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31261">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=F7Durz8R3qNcCrAqTDCXXXM-JoF0chDe4UHuJNeGsb1BAdJLzW-APgXDvD5fgS0F7qmI-Lp7-lHRUQfV06YB70ZCwEkd70OvH0tWUTxGFugNF1zbPJkV5IH0Vxk1OBeSjMu9_id2vrirnp3k1N3KWBn8vMWWTGjpxINJlzZbIOsJlKmWxz1z5bCHpEkElICSYd0LXoheG8_U7FY9pbQbCuQPXYNnYbrbDts0H-Tphd4F9OfD5CFpe3R6QSzE9tfJ88GiUxzMsfxFZVdl0muD_SuLUMjMmdizdf6uFEHLx7SidmknpYviVZIbDsepYH2E88Ig_5L6tP0XolWRvH0W7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aaaacac90.mp4?token=F7Durz8R3qNcCrAqTDCXXXM-JoF0chDe4UHuJNeGsb1BAdJLzW-APgXDvD5fgS0F7qmI-Lp7-lHRUQfV06YB70ZCwEkd70OvH0tWUTxGFugNF1zbPJkV5IH0Vxk1OBeSjMu9_id2vrirnp3k1N3KWBn8vMWWTGjpxINJlzZbIOsJlKmWxz1z5bCHpEkElICSYd0LXoheG8_U7FY9pbQbCuQPXYNnYbrbDts0H-Tphd4F9OfD5CFpe3R6QSzE9tfJ88GiUxzMsfxFZVdl0muD_SuLUMjMmdizdf6uFEHLx7SidmknpYviVZIbDsepYH2E88Ig_5L6tP0XolWRvH0W7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
سرخ‌ها روی‌کرنربازم گل خوردند! گل اول صنعت نفت آبادان به پرسپولیس توسط باصری در دقیقه 66
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31261" target="_blank">📅 18:52 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31260">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=j1yfRpCvowkDa4xWMdNaY8ayKHAqhnX2RWeaD5n9amS26LchXbm3Q-oEijLXVm7M1cnbNrr89izFgGnGbBl-IqRIEMqRvHDFzQbeM8gAXZJZFzRBTCrNKQKbwZ2hRiegUOq1YqMcOHQVkQCaX_im_fz3cq1FTUYuEbwpTdeiCbmwy6TL57e3Bl1K1gUY1t7_W3nnuZQbTzvYO17GmcPf078kPcFuFWhmocubTuB5kgXL_GRl8hRVnxr2lRzM_B4J7BYs7ITGcH6rjjf0LN4PcyIsYUWbsZbEafVbrzOkSD7J2EwDJX-79jWykC-U4JrMtdaW4yHXiXQzfIPw44NWww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd9e6967b.mp4?token=j1yfRpCvowkDa4xWMdNaY8ayKHAqhnX2RWeaD5n9amS26LchXbm3Q-oEijLXVm7M1cnbNrr89izFgGnGbBl-IqRIEMqRvHDFzQbeM8gAXZJZFzRBTCrNKQKbwZ2hRiegUOq1YqMcOHQVkQCaX_im_fz3cq1FTUYuEbwpTdeiCbmwy6TL57e3Bl1K1gUY1t7_W3nnuZQbTzvYO17GmcPf078kPcFuFWhmocubTuB5kgXL_GRl8hRVnxr2lRzM_B4J7BYs7ITGcH6rjjf0LN4PcyIsYUWbsZbEafVbrzOkSD7J2EwDJX-79jWykC-U4JrMtdaW4yHXiXQzfIPw44NWww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تثبیت‌پیروزی‌خانگی سرخ‌ها؛ گل دوم پرسپولیس به صنعت نفت توسط علی علیپور در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31260" target="_blank">📅 18:34 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31259">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=f5tYzMEfdhTZcsv606133O5ttMbJwOIeQ0Ik09NBk40T9vytBP0ITVbzvxwPLSXIWFa37sOGy-cGBbnPyM7_rdSVZkoQKI9xTrYzE4JU2rH0ZXObwLBnqYvF1vlU90T-veA-qrpd-DBbD2_0PJZdV2hnPE2DEPuP_oXnQLO7RMwOkPZSuNF2N_81PRrMeAG05CGWo5It6D9jEXkH5sgGVFIhqQIEBM0u-m-0pMwLdgGAsWb73IVJvD3ZVKxoW-RgVbMZl8v-UN7viwrVqpCY5pYiwN7GKV8tMdYBUuxXkEblJsVmD1XSbGrFEI17OSz9AMbCs6qkY6oi7ujrBFijsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db73f92ec5.mp4?token=f5tYzMEfdhTZcsv606133O5ttMbJwOIeQ0Ik09NBk40T9vytBP0ITVbzvxwPLSXIWFa37sOGy-cGBbnPyM7_rdSVZkoQKI9xTrYzE4JU2rH0ZXObwLBnqYvF1vlU90T-veA-qrpd-DBbD2_0PJZdV2hnPE2DEPuP_oXnQLO7RMwOkPZSuNF2N_81PRrMeAG05CGWo5It6D9jEXkH5sgGVFIhqQIEBM0u-m-0pMwLdgGAsWb73IVJvD3ZVKxoW-RgVbMZl8v-UN7viwrVqpCY5pYiwN7GKV8tMdYBUuxXkEblJsVmD1XSbGrFEI17OSz9AMbCs6qkY6oi7ujrBFijsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شروع‌طوفانی‌شاگردان‌تارتار؛گل اول پرسپولیس به صنعت نفت آبادان توسط تیوی بیفوما در دقیقه 5
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31259" target="_blank">📅 18:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31258">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjjS-LULEfVvyiZe1JZODxg71Dh4C5_2s_36XLTTNwtA5EByhHlgq3JPnuQdJu7mhI7bnQYy46_TiVlb2uQb9o9UisEMski5wgNOi-L2MURX6h7EKvmRkhNwBEQ9RGRSkJQH6KyX7Vq6Txs9SqBTBc6neIgATXw16yHwDqjLUhGbyTSXlQ1mCSxp1-mZB31ICW1dVILRxYotCAk03mfRDVEhxmhSkXFwMEbNIh6EXAB2n5yIIC-07bnmExkMJ1OpyV759VBujai4c-MEjN5L4F6ZfqADydtIlpdRWQHSCghn9rb2AIx0krsTC9JWd3QXQQwvEHMako5TfqXp4ebJkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
تصاویر جدیدی از بازی GTA VI؛ این تصاویر در بخش موسیقی وب‌سایت بازی قرار گرفته‌اند و نگاه تازه‌ای به فضای جهان GTA VI ارائه می‌دهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31258" target="_blank">📅 17:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31257">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=s_-TA-yBkQKJOSYgaGCdZlygfTPOIeuMV5TzP6_OtJ9RMxErvBFWZdmYB8dh0Mn2lP4HWAwEgAghWatMNnZRCQhaUig2IWmZTbSlCiVy4oQdR5JjMiqEPQoz41uq70JCAZnpmjwTk4IKeupLrb7A7GsSO7QO7_c04z047RbP8c95qMFUW8qmo6rO8GXnrbb5YsZB9E763fcRgBNT5ZtQGpMNGcDwY5xZ8cYOFirTLCqFgTTis5vHFkT_8GN0QcKuPHba5eDWoc0JnsHBYi0U4yLbg8NYTfXA7-0U0SeUeyPjkNKEhOAYE42r_wxu2sCpufZ1Hj1enl-XeN6qIoKGCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0462dcd97.mp4?token=s_-TA-yBkQKJOSYgaGCdZlygfTPOIeuMV5TzP6_OtJ9RMxErvBFWZdmYB8dh0Mn2lP4HWAwEgAghWatMNnZRCQhaUig2IWmZTbSlCiVy4oQdR5JjMiqEPQoz41uq70JCAZnpmjwTk4IKeupLrb7A7GsSO7QO7_c04z047RbP8c95qMFUW8qmo6rO8GXnrbb5YsZB9E763fcRgBNT5ZtQGpMNGcDwY5xZ8cYOFirTLCqFgTTis5vHFkT_8GN0QcKuPHba5eDWoc0JnsHBYi0U4yLbg8NYTfXA7-0U0SeUeyPjkNKEhOAYE42r_wxu2sCpufZ1Hj1enl-XeN6qIoKGCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از وقتی که مسعود محبی مدافع تیم خیبر توسط رسانه‌ها بولدشد و باشگاه استقلال نیز به دنبال جذب او افتاد هر هفتههه داره سوتی میده لامصب. این چه اشتباهی بود که تو بازی امروز کردی پسر خوب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31257" target="_blank">📅 17:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31256">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=JOW0yyWJY8m8-iRw1ouvIg26aZm5qUBqosb70kVOu0R7MYK0KM5aquC8GEj-MfmYaYa1Og9EzHdp-G28xb0FG4XRugqxSXywL9hbnHrXeflduiCYwm_fI8z_w2Gw8ZNFXWBBWW8MgviTqAEKYpGBfjmqFJB-g5L4clNFSLBrpzeCo3CG8Ldq_i2wC10G3cFAN3neqV5KYE1cQxwx-8FfbJ0c0pvdRHGoNjPmxnUUG5CX8anI0RqSn_d2tznbLFTWVfVh7qHBk7WabeaN0wdG2yAgs2l75dsFvNudk9VlK7mWWuFDv7yS5tePMHaDwxMBzjpaJsy1ppa18h9GlqqD3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a1fc96c.mp4?token=JOW0yyWJY8m8-iRw1ouvIg26aZm5qUBqosb70kVOu0R7MYK0KM5aquC8GEj-MfmYaYa1Og9EzHdp-G28xb0FG4XRugqxSXywL9hbnHrXeflduiCYwm_fI8z_w2Gw8ZNFXWBBWW8MgviTqAEKYpGBfjmqFJB-g5L4clNFSLBrpzeCo3CG8Ldq_i2wC10G3cFAN3neqV5KYE1cQxwx-8FfbJ0c0pvdRHGoNjPmxnUUG5CX8anI0RqSn_d2tznbLFTWVfVh7qHBk7WabeaN0wdG2yAgs2l75dsFvNudk9VlK7mWWuFDv7yS5tePMHaDwxMBzjpaJsy1ppa18h9GlqqD3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
شماتیک‌ترکیب پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ علی علیپور، کنعانی زادگان و ایری بدلیل‌مصدومیت این بازی رو از دست دادند.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31256" target="_blank">📅 17:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31255">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=oyfT83yjMgzq4ncNhPcEgtMh9DM-KZFNZkCFIUwXbC0Wjh6cOYme-AK3DCFP0a0IAjJxqeUdYyMYJhCvwRnFp4OlWOsHG3Yy_aS3daRNna5RRUScXEADDALA6Ra-6zxL3KUkS9KpdfRkl9wregaiJUw_TPh21AwEY_KvNSq6uCrR6MwfIfUsawOuZ80dpmv1tY1YnGf53MKSqWLJLiAC5yqrszK6y8ef496gw3W_uxqfQSv9-_4dR6lyM-9AmygahLpHcdkBcroomTZnW8PUz5K8QkoCeIQ2cKg0rF-5pyLu_-yRcTpdek9RrfxUrQb5HUJo0dVpbBDMmbyPDHnSzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7613725c1a.mp4?token=oyfT83yjMgzq4ncNhPcEgtMh9DM-KZFNZkCFIUwXbC0Wjh6cOYme-AK3DCFP0a0IAjJxqeUdYyMYJhCvwRnFp4OlWOsHG3Yy_aS3daRNna5RRUScXEADDALA6Ra-6zxL3KUkS9KpdfRkl9wregaiJUw_TPh21AwEY_KvNSq6uCrR6MwfIfUsawOuZ80dpmv1tY1YnGf53MKSqWLJLiAC5yqrszK6y8ef496gw3W_uxqfQSv9-_4dR6lyM-9AmygahLpHcdkBcroomTZnW8PUz5K8QkoCeIQ2cKg0rF-5pyLu_-yRcTpdek9RrfxUrQb5HUJo0dVpbBDMmbyPDHnSzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بخش رسانه‌ای باشگاه خیبر خرم آباد در اقدامی جالب شماتیک ترکیب این تیم مقابل چادر ملو رو به این شکل "یه نوع شیرینی محلی" منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31255" target="_blank">📅 17:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31254">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTSeNLO0EsNedGq5ou8HvkXp7hS9tOiwzvEg8dMCJfQN7Oao6c_qyNjEyfo8eoEr4A98t-aNZeKg2KpzS2U-pG9dHTm4VUQv6Fc6xGiQBIYtRKi7NGzSgnbqIjPPV7TYoKLIQd_gJwXwUkm8XewuubMDU9TeiQ6t8LbMYwR5PYUFKpCVikt6S8wfEP3TjvDckkF3prguBU4jI0Ucxm2DEHHQiqWJbyxqDvl9kS8vW1eYvxZKFTJzyIvxpsRJNg60Q2c_OYM2cBYe8RmPDRTWfukWb-J8hs6sOyQoDV_euDiWbhNiPBUq7bpmYudCaEgyhrrCDbbOt4zbFKHmOB348Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان دو تیم پرسپولیس و صنعت نفت درهفته‌هشتم لیگ برتر؛ مارکو باکیچ و دنیل گرا از لیست سرخپوشان برای این بازی خط خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31254" target="_blank">📅 16:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31253">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
#تکمیلی؛دستور واتساپی‌شجاع‌خلیل‌زاده کاپیتان تراکتور به‌بازیکنان‌تیم‌تراکتور:همتون علیرضا بیرانوند رو آنفالو کنید. او دیگر جایگاهی در تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/31253" target="_blank">📅 16:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31252">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwfSqK8MYizz2gKfKCuovOGsCbWRO4hxy8Iztw_Nl9C4FRhRZe9fmxYy6WwCfhYPie7QtmzR4E-Ny70Gy9YIPAEHwxJ51DPOhzQzKTNPhVihacDce8XwFyJgo9cvBBfk4a1d7IBrcoE9Q7netVP8lgcBocU7TbvY8wllxd_vTTF_5ahqq0gCVp6ysGBoTreeqoSSQZmS8cPvgdbhEEnPp9kG0HiherQITqNNRCOdV8QsANIB7VfwsUadS6M7LljoiITY-AcyK2F6IJ4eVgKXrHxtwCZdL0zxut5DKCwY1hlY4LoYiV70Y71YYqjW4CoAvqaV6OsWzYh0ap4fdW2QVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ ترکیب تیم پرسپولیس برای دیدار امروز مقابل صنعت‌نفت آبادان؛ ساعت 17:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/31252" target="_blank">📅 16:30 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31251">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImHwxb0tGiTaoUNFuCYFKrsZPh6vogBjEB04sjv-IOTARb1193MnqC3WwJuznGt0dBP1KsdH1Imqz7IM7l8sFAIsphfN18M0SpsCfB1Sq7kF9q-Ee5IA0KrA-OPe0592yVkZVym8fRfmOjFkJDCsO4eemZmHnS3vDJcpIX3EdhC8BGSpnA456YrY6FfqOlfqoJFfUhLAOQmTmJrqsIYtoDgPAPh7kpDu9HzS7a8K0EFMPS8no-WthHDc5fNW3t_92wGg_xClXVVYBIsrnLiaFczkpeKC76Y88SGdB_MSz0go9bpZmXkPe7s_edK7juJzL7EWopnaATN6-FnIE4kwdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ همانطور که‌چندهفته پیش اعلام کردیم که جدایی دنیل‌گرا و باکیچ ازپرسپولیس در نیم فصل قطعی شده؛ مهدی تارتار نام این دو بازیکن خارجی رو از لیست سرخ‌ها برای دیدارفردا باصنعت‌نفت خط زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31251" target="_blank">📅 16:24 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31250">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhEtuEK9qP3fh0tKd4-b-CBk2mUzZb-rKVkOOPSOSZ0ApkvEkH7Vp8qD8pi_CBuCN53lzExxP4liOp8abhGohvgyI80SKaSz8lkcKNd0zZlmL3DhKL4lVtG3KYo9tuoBDyEgAi5pV8FcpDxryLqs62VylvHLju_cdKKnMM6DXnAh9ABjl0haMAlXlRP0bUnCkQ1Gw7eB_KzORup7UjX9LE2LOkBnBbfbzHDSu5ZNdSJ35IYes5ShTGEpKYAiLtasqZW4bDzOms1l48ppIG6FCgkj9b5uj2WnN_dxR0Cyt7ELzYxb4SGrI6o5i246Qg3MOoYxzAcZ-CgV2Na_mM2Pyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/31250" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31248">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptkXNYLeMQPWjSO7DPGPgwrA6DaPc98UGP5iJEtPGJuSv4Onf5GIxEwkju5oMBi8FpXW6EVD63WN5uNlIFwmcee6nP3UMvymCbGZAgrhcCJVCARl4EAp3mVmtLv61B0OFs5NGck6sAcox4_0dV_oejJ2PH5x5NzJOroncEhRftsSq2KgM1MUdXGYQAikMdRrm2p9zq9J_J9uXryqtcNGNbvhkBtSQNH-nPsrqpguxSy6Naqn-rtxC0s0BP23nAxec63ICIAmJ_HSp1LaTu8Ene9O_rMujxNIR5qfHO7ovY5l9V0NtGbmYNX1jedqZNGXnrYIdYjMme4pi0oGRV4W_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EXIqhL5aVMRo_aviB3zvALbFoZLlc4QbVEMZRxTO7FZv0HGsfe1hcQjYg0ZZrQIa7xRpMdLSqvt_xv8dI2YbTLLtceLMOG1lygLjeFrLOqE06W3zQ3i1dPDGZ8hotZGVfXc1uOEjqiL2AoyvQrfIqXDExvUBjP6hjJ7Rg_05uGkWDLDrkbiuSskq6dJUFmZdSHkyc5aRbt2IuTPo-m5eDZiPNlUZEwHeZ5Es68Pl9DgUT_h9wS5hZukcb3UtbAST_YZnklqYtT4DVJGsMDMHmtxr7x7C4pWzlgyDJsCeh972blhJtcWYL6g3PJL9XbrMr5B4DzljbJA1W7ehh-gOUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تشویق‌ده‌ثانیه‌ای‌لیونل‌مسی شماره 10 آرژانتین و ایستادن به افتخار او در برنامه ورزش و مردم بخاطر خداحافظی او از تیم ملی فوتبال آرژانتین در اوج.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/31248" target="_blank">📅 16:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31246">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trpOnE0Dvs6TusYed8apAIz6yencYBtmwPY3HrUrvGQNP11bQE95VKfEPm2Hh3W2n_SId3BplZApSzFhYl1w_725amZ4Zj9C3AquUudJVqs0-luSd3KDb04PPvqrXNlPKnZ_E-qP__Hji8pwngAfFrdbQ7guVm938AvMmkftSnE5EqJhy4bRBhQbt-Tufzya-7td8v3hs0PegpcxyxUBCiMzPjYv3ELmGu-VEWf5PJ8zs5T27x_0pKkYuoGorScTAxED3bWGwyxrVJGqsQh3KHWKnMVDo_gbzXAT62LHSjWTlm5wqXEMO6WiiN2881VuemMbwc5-aQA8FeyuZ6WQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور، گرت بیل، محمد صلاح و ادن هازارد درکل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31246" target="_blank">📅 15:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31244">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2089087958.mp4?token=kCRaI9lup7xBIr2T3VQhddpFvyrc9NjkrEJYiId2OEP8QNzhloKXi3UPv2X1p9R7AjSZpCkwDJ0WXNsyVsc4LGT6OLIadEN6QTLMNPBnQlKMvDX7Z34WdbUM6fFLdMEqwAOjn9gO9M_CqUEdao_M0sdzlxVHe1arlGmHiA19Olnl3FAK1vtOpDfjnudqYsM-V63BDcFOD1wS8JiX--w_x9lKzV5K4hlvzu2_Gb8uRXzXMaM27umFB82bSCMqy_Cb4snFTNTNsMAuJCfULUoubtZIKdxzLn7BGShaVvbaOVZKY13iHDX2ZNgLAj8IiyyS1Y76EYo3XTF7KHi7XGYVPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2089087958.mp4?token=kCRaI9lup7xBIr2T3VQhddpFvyrc9NjkrEJYiId2OEP8QNzhloKXi3UPv2X1p9R7AjSZpCkwDJ0WXNsyVsc4LGT6OLIadEN6QTLMNPBnQlKMvDX7Z34WdbUM6fFLdMEqwAOjn9gO9M_CqUEdao_M0sdzlxVHe1arlGmHiA19Olnl3FAK1vtOpDfjnudqYsM-V63BDcFOD1wS8JiX--w_x9lKzV5K4hlvzu2_Gb8uRXzXMaM27umFB82bSCMqy_Cb4snFTNTNsMAuJCfULUoubtZIKdxzLn7BGShaVvbaOVZKY13iHDX2ZNgLAj8IiyyS1Y76EYo3XTF7KHi7XGYVPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31244" target="_blank">📅 15:07 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31243">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6caEBgH8IW6Q6R-nTFNTB9Xj8PEznNz_JRzJGL3Q6vKYXokjAb9TgN8_oh8C5rNKqVq9b_rOQ27F23V-bEkppyfjaoOxoQFtu9TKuN8QwoyVh339-RW7m-E3FnzKYuYaij92_IGWDJEQD-1KyIYWWVfBg2w3tj_P66eDrKXwCMPKHDfbLwoVdeIoRm1eVUBeambhhgvK_7p1aHf7kr7Sx_5BcvjfFaSiuXPijADj3Ul8kupELVl4dhUbBQSpJDIMepYwH0fSlGRpsBfwbTaTwfmdJGjbowGMZmfQAGqwzuGFCZ86J6lAokvrEZXwIb1TpQbmaMqYlREIXMo3NIllQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
🇧🇷
#تکمیلی؛ با تاییدیه کادرپزشکی باشگاه بارسلونا؛ مصدومیت جزئی رافینیا دیاز برطرف شده و او مشکلی برای همراهی آبی اناری‌ها در بازی مقابل ختافه در هفته هشتم رقابتای لالیگا نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/31243" target="_blank">📅 14:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31242">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=Mu-5MEsTyyn5K4WuMVvIxCqa4M-nlUFLC7KZhuP74TEcK-WcxzA_anVAREUJxamDL5InWTlSCGAM252TlEAOr3cEDmEaYf5Lg3b7zCA7uwecfoC3xWWcwcsm93plpf84n9UhdBxdAvViZ00HgMWujmItVFWgSxzzFYMT0NHLlWv9SxqQumOzeHQl7oDRLVqroS581jTzdfr8hg_yxP-OykfhpEMGKYmDQ-AgBs6VCgsfFAv1ttZTQZAP30U9FuIy2sAsiJY-kPMFrOZhM-D8tDJkFhCd1zgjHTJPG6cgmBv3JJMVXL6M_tP-LPShch2lkHERcbNDufSJYZ7UMJLHAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33992a38c0.mp4?token=Mu-5MEsTyyn5K4WuMVvIxCqa4M-nlUFLC7KZhuP74TEcK-WcxzA_anVAREUJxamDL5InWTlSCGAM252TlEAOr3cEDmEaYf5Lg3b7zCA7uwecfoC3xWWcwcsm93plpf84n9UhdBxdAvViZ00HgMWujmItVFWgSxzzFYMT0NHLlWv9SxqQumOzeHQl7oDRLVqroS581jTzdfr8hg_yxP-OykfhpEMGKYmDQ-AgBs6VCgsfFAv1ttZTQZAP30U9FuIy2sAsiJY-kPMFrOZhM-D8tDJkFhCd1zgjHTJPG6cgmBv3JJMVXL6M_tP-LPShch2lkHERcbNDufSJYZ7UMJLHAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهترین‌نمایشی‌که‌یه‌مهاجم مقابل ایران از خودش نشون داد. استپ سینه‌ هاش آدم رو یاد پرایم زلاتان مینداخت. همون استپ سینه‌اش رفت تو گل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/31242" target="_blank">📅 14:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31240">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ggnj9Rhoa4tjcTHgp8Y6Hx8w2VcSLicPdCt3SFbj4qhFQcDlHSoTSRv8lpxTMHHmtyomsEAjPD9jvo8tsSb2dxLmuFDPkn3UpYtRi_wDcZg3SQqbXrE7nyf0yMZedeRmuwjJU-jFzCJTgk3ip8qRm3fuyhqutieKzsZ4PcUZ8x2g-WRWCn5QbFZdMjpGO-n1r9XumHe0UIou4q9uhR5TESsdDLdRBVchCZs_pQBlTAv9EDTROfb7atzkYPGXJtvhkkCYhA-z7MTVyFcFfiwu5JJnQyzx6HtPAMI8GeK-mO-5kRwkvW0uohRXUaSkBQ7kgMGLdEkxlxf1q-WWpm3piA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7wLHS3xymOVRHf0r7UyPXXME6uPCO4Vazty4DRVeWeEAKzkwaB4qFhAG4SlCteHi-f44GbqaizXqy3uzWzZCXCXDhZt9u9_hsIXrCyBhz1zVWuV8rnj-NwVd0JwTHKw3vAIylXhYRX1jslgbZyxf1OzJsjGSZX5JTPkdprbfXgh7WMS86c4r-iR0G_VL4NXlPzYbBe_qcu5KDMDYZIN2e8i3voUClndh7hc5d4td7Y0BpCKCpP6vc_KDZqMH6SRJ2AZ4UENxqFXbhtBeNn72k5tMf9FKK1Cr_ZF82qAtQE_lci5-2lMktnu7JL1B_xReEX8VJUOr28psBfbEiNf8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حضور بانوان هوادار تراکتور در ورزشگاه یادگار در جریان مسابقه روز گذشته پرشورها با استقلال.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/31240" target="_blank">📅 14:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31239">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuSe83zKgUw80yCwXD_zfjZi42fdtn2GetEGcJzD4MqmYRaqWJbEZtvNUhgZx5W0Mt-vaPLivdIbfIpPFk0cgKkGod9Cch3j-ukpoHURdx46kiUQjFggIq0dxCTwyVZS6xWtzvWMZLpBZftu2G24sJdWG3dxsu3_mMKb73KfqcUCLPfzUZ7Wy_-iIAb8xCpnwGShUnRr7aIT_js-iOQ_UIk-ab4FpKhNGZQxFfTR1mA7cFW_0r1qzvqbX7I7P6aRnfhpgSfkmRxWliGSOhopLG1NzYFBPFCFW34nOTjc9gxaPw2EqAc-m7DDKFpgetdE3TeMt8EWzK8QZeirOEc54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم پرسپولیس
🆚
صنعت نفت آبادان درتمام مسابقات: 48 مسابقه، 31 پیروزی پرسپولیس، 6 برد صنعت نفت و 11 بازی مساوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31239" target="_blank">📅 14:33 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31238">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ5g4GHQqqT1ihz1xJs-rBnZ3TVJRVe6jgOJk1FBAxfVBaPxp4KU50eIHODOqeyQc5vGWDEKKJFsJ1gIdeKPtcEFicvCO8cfUf2l90HvHR0z2Az1YNvX2ZAEOV4UDeVmXMi-yS-3abVhcWpWH9QBpcw6OpAKtJbHvAbBzVTZlv8KAyPDGGPrvNcBzr5eEP9TW02S5TVEqFyre64j7BnUIEwGjZ7I2AtqwHk5MlK5NdEPhQ4urwkeTxqv_1RHaX2enoZUh1xy_mDrUYyC0fbfGP2Y4tmoYWTbQLIQUfqj4teodxlI2fciYIT7m8334iLkxmlMIF5vHSTNCjCnNxOANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
دبل نیمار دربازی‌بامدادامروز سانتوس در لیگ برزیل؛ جفت گل‌های نیمار از روی نقطه پنالتی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31238" target="_blank">📅 13:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31236">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A1Gnlg5tx2-VjjLP9JtAZORo9tFdfm-4aOARZXIEzIkiqqfr6_n5QeUom1EdbkWB2dX7syf5v4l-rncdKk1n10uYocuUoAQ7vh2GmaFKt4E8DJs3bgDolQ-7BtglPQbg3HvBCXrCz6z0HxyHgErhdJOVxuXtjp5Mtd1Jz1Rr5P7dxSsVOQyIYASYqvDRnJs_l-LltYotmh39ePaYQBXzUK9G0eQKGf4zBomWEpMB7bei330CORIcaF6hTkw3JdrwneeCFxkkOfUfIoit-SYrEFz3LSmDj1LSkcDWQlJyRwj8e51SpvE39pUAyMyZBOCHyzJJcyrhadjRJV-0rm4X-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uaJJJpLTKTMlBV_IwAajF79xpUWarFSPG9YOtPsanv6WAEXuAFx-U6xUeo6Pl_qUPNLraCaot2O9mmHcmb2RY6o8jfVCmX_WIDPmmDvuSk8garYexFo0p-AQECnQPn_bPwsW4expCWc0RD2wcrlbbN_ybMoZMwDvwQGkZyYgruaAn-hEarZMOMLP0l0l76-PkXZHQ-ncBcsA1yqrhoRx0IbIqMopqEamFYspXodblm5th8GkXXNrjV7eeosFOtIupTosAMFN-CeOZmrSOoTyCPLW8-x_Ed1hs71ewaAvY1kBAYF7pL9ICgt2V5LqOL0ShNuJBbaORt4XXITg2f6EdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31236" target="_blank">📅 12:13 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31235">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSrAqW5YUxu3AY-XZFQ7H4WOJbSwxEN7Xde7VRwR9yANqcBb-BBqnikEscqG341XXMiev3-k7IJ7QYmidXs2Mbqk_duGJQSuJNt26uVrc7qAJx1XM63oSEhh5dLs_ngBZ6dgqJ5i1jo5Moic6FTukTZ14PuqInJBgtntiKFy4ZQTiEruJFfEf2mNAH8JwXQfceESkjOYFNbb1TkPV2k_G8nwpVkwQcqqETmDPDFKY_wo8r197hcfJR_eKwYONQ-DREQWw7OrG2XUOMMMibEV2lncl-CiUXrgsQCxH6yFPWFDGht8YEpjkIp6eogQmSN-M6WopEDYDK58duPT8CQ4Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادجام‌های‌معتبر کریس‌رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31235" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31234">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fczzWALkyerAXDHVs6K8U1VKh_1ed6aSTh_p9SuS9nE38_vxe4t_qychy0Q8da8xD7KrMbEQtTzYR2cDrBxgjx_tqs3YQjZKOwUUpysL4xbAeeqmNE6-4q1eV22ZmmcCht3f5L-2IEvpouX4bkBWwAcTieB1SDGWloIb_5B-nTfp4bPGNZMl_HUcuQZ5LH2KIhBEbp8rpN772ss_GFPhQBElISbGXtErUGEYJ-JjJkSgm_u6VMmzpL6yOCtHcUaP3AV5-gQLlcysXvNI4NQmndelBoMLEaQNCb-iaHVzqBjMr7aS2Dw5JnTGx_LSvMEi6WARr71hMc-nCJQMlg4gCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
باگذشت‌دو روز ازبیانیه کریس رونالدو هنوز هیییچ بازیکنی از پرتغال این پست رو لایک نکرده!
‼️
این‌ویویو روببینید تامتوجه بشید که چرا کریس رونالدو اردوی تیم‌ملی پرتغال رو اون شب ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/31234" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31233">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/31233" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31231">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXVDRr2IriKy1Z1ktcHGBhtU70xkiWoZwrdfScvnejaZZy6rEFOkRptgLqGn8-46hUKqWHXqljHsPci0hOz4BRa2BBX-Quc9EcZbFol6xLG1WUskwyyn1M3RZ0VbF9hFRftHf7PpvRzUwWBtMe5fDy6Qn-25AgN_9S6X19uizrvXJxIuwE_qtMPaAumix5RKaA8wIM6obsPu371oupo2c98U_6Ym9nuJ88ewDDFF4hgfClNg4ga6L8yo14as8lH2cMuu94mFKGQEpENfT3N0Ree5Gg-th6VgJE5DTksYF8OXqwDFVG1kT7lYGPzREfOub-WxZrSF4Zmu01u86OWSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31231" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31230">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHV5Ea6ZgrQ-Q-947EV6Cr5HVpE62MwGDA9nDyn7Bb6mYeBrT2ZC4wA1RYvsi-rAGhimjpHsKX_rvt_m8cI6jY3WGCpO2WJDseE6fEO-52bVYq6NWS57nxphmEwAK0Vsl0kHB3bmV3JFHf2ByR0FlgKIn73vHwNHCbd34H-DwhyR01IpJSWFKt2-tg4DDmZt0usTXcarQa_9Y5WJvAOEHQ06IHy3ArtPD1BThWSDKmURBeFjqhhqeOpeZUSLwmn5DjiMEQtC5SZTYIpYfwm0t4hn6wmm90tXinZz1WTenNXSRiYpMjMwKbKatPyuwtMQqotZK77Rgnp_LRJir4zkdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/31230" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31229">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=ChAbLsfm8FvjAevZS7PZ6qnIpx6chQUQcnPmOKw5QYIXIytzCnkvAHISS6Zb3FYn4bGRUMCFWBDUMTQWqbUdvcscygRwef_0X9AUhWEv5H4WMdkePcgKnSaxzdxFFw6_RospbTCMsMN3mgbW2JH3yboF42vBpsWnlOGI6WwByNqaXDfIHUvaZKyH9Algv24gqzDAT9IFJGXcf_hPdvKAo4FKQSTtVLAkFS-zSDShnRoTJLgyYv9GwHHNVQW3bkE5kAZRDAA7f7-hcSJjsVf8tcpyuCOu2Q-gXih4M-qcMDD62ShYzlyo90k1C7dXNH0Pzi0JT92qfTn8Owa2aHxEZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=ChAbLsfm8FvjAevZS7PZ6qnIpx6chQUQcnPmOKw5QYIXIytzCnkvAHISS6Zb3FYn4bGRUMCFWBDUMTQWqbUdvcscygRwef_0X9AUhWEv5H4WMdkePcgKnSaxzdxFFw6_RospbTCMsMN3mgbW2JH3yboF42vBpsWnlOGI6WwByNqaXDfIHUvaZKyH9Algv24gqzDAT9IFJGXcf_hPdvKAo4FKQSTtVLAkFS-zSDShnRoTJLgyYv9GwHHNVQW3bkE5kAZRDAA7f7-hcSJjsVf8tcpyuCOu2Q-gXih4M-qcMDD62ShYzlyo90k1C7dXNH0Pzi0JT92qfTn8Owa2aHxEZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو: نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31229" target="_blank">📅 10:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31227">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3DQ7sUVXhMjgdY-T7gTVASxnXkqH98t97SwoKa2dlCQ5hsDfsRHQBcmYIrZJJLP9V-L-LmQAh6TW8w6Hxan37zPdg4VGtAzOrYq_fOgcJn8OxWnvTXX_dAZdfEZLVkeKzCgtN3VimAZN5TtCNSXOhmbQJAesKe09Ai1COWEngkJekbjQqaJpcz2RpdaYrQRya91ltw0gAMFLX1B4WrLH-REFtzI-Uw6tgToKJE2_HrXRyHoJdLL-FvdRJtu-zhFCvGJQ3P03qajA_p5Jcfx1FMsWbDPCbcRgfTymO49_UcUNLdzG7OzVOFn6H7yN0hdQmEjUghrPTFe0iGk-j72cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31227" target="_blank">📅 10:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31226">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkW_a2XT75kKqEtVaBtC7Hx9v7Fw__0WXHVHNfOMHPZOT7udKJgiPa7fvmNn3kZI4bYT8QYneCmFOqdvis74bX751My-1FvHKpbGXWP4K6reE5pm39aD0NwOlvC7hz7SRA9FQDGjjFFMhfbsVlfUN1YX1y5uwPGOdrk0ysjXMeMMQWo44zn-dcB7EnjC6xxeDoTbJ974dH2Kbhy0BZG4dYBBYdvSk7o9XlSt3ViQIZDbG4KuQFiDnwtQsBf4PY8lFidXzTsfWVKWPmX-b1b9IKxmF4DSoe964j6pvdovnrnNDtNY4DGUq47nvoV-4pS8nlQeX2PK5t2lWGRrfhihIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/31226" target="_blank">📅 08:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31225">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moKpzCMJZBb4ku04593HWM-5W4gjXGHj6sXYrC6fZKIWXpo5TJ1-dkslHyuoz4xRitmNXGsnlnfueTGCRhkNShhHJsFr706okQnJjZ3PHM1vhd-beSq3HKT-bk7MFjChwJynJ4CWBpVx9h3jDraDzHW4Q0yvA-96fiHX8y-wDio657bEmTJP3S8GXG8hD9xF6hBtkD98hPCMJH4OQel327YI2ZlAdLw6xKEys1OhKmPoODNDxFyXaiq-voVEa2RCzuPEWU-hF6tha2XGTk9eR1k4yvN0mhJ5fAzkSkiIxpS0SmF4WnYjj5Ccc73-SYgjyeU5q5I6XDfL2FiWG6ig0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از تساوی‌در نبرد استقلال و تراکتور تا آتش‌بازی سپاهان با درخشش حاج‌صفی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/31225" target="_blank">📅 08:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31224">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛تساوی‌شاگردان بختیاری زاده و نکونام در یادگار تبریز به کام پرسپولیس و سپاهان.
🔴
تراکتور تبریز
1️⃣
-
1️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/31224" target="_blank">📅 01:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31223">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIkyVhaXzNcVy9E5V4hPEciQMNqQNxx0n0rr0cqJEXb4YgBIMEJiIWrNLXbmavpfTXMxg16ojBfrOROZEp7zSdc-cTBQE3HdqmOYtnMd48ondQtvsfrdXAyuGMZsFqiX2vzCzm_Bt1U9O7jfvdxiMDNeVLbymexDRFGUod8_K6IVPdSC7pfpMGqejl5J6aWoMPr-GWmyuanE84nN3FzKk6M_q_yNk2zdelqIj7RZDPxOlzYrMutsqmXWgkROJ1fH_xYfkMCa_23YJUczAAOibX8_y-DvabYUeAMdmgPTytfmpIrbGODi7sSiSQUIlGHFbuHvZgDwtgWcduH17EWQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/31223" target="_blank">📅 00:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31222">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‼️
علیرضا بیرانوند به‌دوستان‌نزدیک‌خودگفته تا تیر ماه سربازی‌اش به پایان میرسه و در نقل و انتقالات نیم فصل با قراردادی سه ساله استقلالی میشه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/31222" target="_blank">📅 00:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31221">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=luL00B5DdqhcflGQV_6_0yXi3-GcT0i5Ev-WwaebVIZj0pnragaUujBacsoOni78il9kDf5TQ19V_xLmCB4QHw5A5RK_OTVKQKnFfYyc_RlDY94-Sgteeenzi84XnmWFajnU34KBF7Sxrwmz4slWdvOlKv56Qk3adUgu6J6FgPfl-EjnSiVC_7b-vsa5HNj69mmYihEUWHcV0Rl0B8NV-eGvoxXzN7kE17yYyTGe0fKg4wNjwnZrr-6lSrWpe-dxEN2chF0fTisR-EKTdggIe_VKYmm_VcShzi0uwwqMXm5Rt3VbvruyIwKxOvP84Z9MKh0XvdKonuiq6FKdI2vuYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=luL00B5DdqhcflGQV_6_0yXi3-GcT0i5Ev-WwaebVIZj0pnragaUujBacsoOni78il9kDf5TQ19V_xLmCB4QHw5A5RK_OTVKQKnFfYyc_RlDY94-Sgteeenzi84XnmWFajnU34KBF7Sxrwmz4slWdvOlKv56Qk3adUgu6J6FgPfl-EjnSiVC_7b-vsa5HNj69mmYihEUWHcV0Rl0B8NV-eGvoxXzN7kE17yYyTGe0fKg4wNjwnZrr-6lSrWpe-dxEN2chF0fTisR-EKTdggIe_VKYmm_VcShzi0uwwqMXm5Rt3VbvruyIwKxOvP84Z9MKh0XvdKonuiq6FKdI2vuYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/31221" target="_blank">📅 00:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31220">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFomQN0rHRKTLpDL5u4f3yrot74ukzrBkSq-_N3kv9eO-R01P79dWs6lu1oVRoC-1fXq2CTyXRnPoka5-9H_JpSZsjoKgFD6H-ybtoTsOYZBXEK5yT1odRhyjJwGsSxMzbjOr30so-KZNqZWGCfp9JOre5nvAbs_-zkNkooDLh0LHcaJwjI5OLUmHjBc3kXLwJLNuLgHBx-cUpL1F4qMFgnXSpyv_5EgaC2UflKlRZK6BhPXhC6QlD4ypCC2YJPRFsh9_LP3pJHpr4OxwYylu1OJ8JEzZu_EUaYRvqT1_bO2FLNv5HAa1-yIoNl41WAm_I9eDjbj_V_pbsiq2xtO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/31220" target="_blank">📅 23:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31219">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcW0GiqGi-ub224hoFvdHRX2nO94y-H6RAzrH1zXyeP8MiEvdCrOmicOE6GgBXAcYR2km6yj-elZ5A2ArkczqS095mfHpTYQ5XlSROWdGe8q8wiNP4IC0fhehFqWgIThaqCwJTUPAwWp7FWILLbozKWaoOA3aPtRzPCip7zq7IaxmnMkQt2MYXqusp27DbzSrf0Qn7fpq2503i4U37krx9FBbDnBr9Ur7rKRoDTcTzMm89kZsZqXFCvlSJ32H_WQvA-V81OMIShMReXtpbvpKszmOpp-boIFM80vp9JD_yx5SRG2sbe70244tZWuFb71Lvtd0XByWTAjIp-xKJBkqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شجاع خلیل‌زاده بیرانوند رو آنفالو کرده و از همه بازیکنان خواسته‌که‌این‌بازیکن رو آنفالو کنند. بیرو بعد بازی بااستقلال گفته تصمیم نهایی‌ام رو برای پیوستن به این تیم در پایان خدمت سربازی ام گرفته ام.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/31219" target="_blank">📅 23:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31218">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJOKhDZQkcLMxUFPyP_oLDssuVvihDuXT2NzoiaMxqJT4ETG87V0J9foascEr7mvyl0yROJEKPf7Nk68NRrk3gOuDLl4nvdjq3Caa1Ff-DQmgnwJZdIcadA7EpLIwzB3AChJ9ENRAl07h_xbBG7J5AUGxqcDzdWUNLEbQFjYmynFmT6NMoKM8KUQmfB-AC0GevJTwlOzmIuIHeJtKCR5jtt1xZllBQay9-z-hrdHbTjLzZa_gsHGyNamn0Zvs-iyoFEo4JsQ_mwIcWThd8rYSuyhISyJtd5vi-8AJduzbv3HIBnz1WNmGeIEeA7OVNeH_N33zEcGR_EpQteVVUh4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت
؛
کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/31218" target="_blank">📅 23:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=DFXXbGjYZprA3nZxXUoCR6tuiipQ4WRjoHIJLx2tD5NAHkhER8Nj16f3eX0vGSV1eY1dopfA7Q46jLu1F2T5fXybRp5bjA92XNlYiEidhAmduAhMZbs0OtW3yIgBdFvJ8IrMBNbPJaodef4NcsV2hZkGrNekEOrKjiA8bs9Q2KeKRvNaveyNyaTQnyQ5GywP2ny6e5RROo1scSINeXH4ZrXJsWNSzjctmTlaOMcLTw5r71zMHGnjiCBqLdn-Y6iu9bHEhHH5SyLiSBGS0gsK7w-fdtA-Zyvdq6IKVr5X0pMZcImwOuawp_P0uZcbJjzl07FO7yKeHcQY4RfRNjptGhpSaRyxXhSBea8b4c62uNIWVr1K__QP0g1XQCTMWQfd0dKJdIQ621NKL24fNZZDxHSxvg_XNKRoS9CvFbO20DWr2sGpG7GNK2_zBbJgHH4ArFaINiYHn1DwWhWLk6teFMr7Cx1EpMpp4kSZLd6epH_EwQX0jvsHWVYVNkPze-t2QbqVtq5CNasomSdWJiWzNe84CJ0kBGmuVL_5kOIWsy2jyWK0m9kZ1j832m2Opk56baz3MHCLdcHMCQYY0sQN8EZb7sdn83LTAd_TVIt_g71AFewn_gAIikv2mB9EZHeRiE7zkFe0rTeGcSPeR5ikcR1R4qCZdn9mvyhyF2RI7n8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=DFXXbGjYZprA3nZxXUoCR6tuiipQ4WRjoHIJLx2tD5NAHkhER8Nj16f3eX0vGSV1eY1dopfA7Q46jLu1F2T5fXybRp5bjA92XNlYiEidhAmduAhMZbs0OtW3yIgBdFvJ8IrMBNbPJaodef4NcsV2hZkGrNekEOrKjiA8bs9Q2KeKRvNaveyNyaTQnyQ5GywP2ny6e5RROo1scSINeXH4ZrXJsWNSzjctmTlaOMcLTw5r71zMHGnjiCBqLdn-Y6iu9bHEhHH5SyLiSBGS0gsK7w-fdtA-Zyvdq6IKVr5X0pMZcImwOuawp_P0uZcbJjzl07FO7yKeHcQY4RfRNjptGhpSaRyxXhSBea8b4c62uNIWVr1K__QP0g1XQCTMWQfd0dKJdIQ621NKL24fNZZDxHSxvg_XNKRoS9CvFbO20DWr2sGpG7GNK2_zBbJgHH4ArFaINiYHn1DwWhWLk6teFMr7Cx1EpMpp4kSZLd6epH_EwQX0jvsHWVYVNkPze-t2QbqVtq5CNasomSdWJiWzNe84CJ0kBGmuVL_5kOIWsy2jyWK0m9kZ1j832m2Opk56baz3MHCLdcHMCQYY0sQN8EZb7sdn83LTAd_TVIt_g71AFewn_gAIikv2mB9EZHeRiE7zkFe0rTeGcSPeR5ikcR1R4qCZdn9mvyhyF2RI7n8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول رده‌بندی لیگ برتر در پایان مسابقات امروز؛ تقابل حساس فردا پرسپولیس مقابل صنعت نفت آبادان در هفته هشتم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/31217" target="_blank">📅 22:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdflT1fdnjzU1J_BxQkLqJi5tBBgqmmy_hvAfhSiAtpwxOdyLcr7wxiGesrA55XXa9Ub0NrVLT-tUSNnKJjAB9Bz__9LJL_bTaXa3xieWc-dDVod9JHRpll8ziFm3utclJa8Khxv2yV1njV8cFp9HqELl9ZmmYEtRxIx15gLlSJQgNWq_QAfK707mCJM0wWdO3Usr4b1wLCDpsTUDGXW7c733P4-PXcXjOdj5caWqad4heSKzGuxvtRwuX1_FnTcubnowo8LEwo4kItHYvLZkpRsm0qfKnIsIB1qHZMPP60p0rhxQFz735dSqr0IolIzxH2VOgrsbgU7t2OZO_sdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/31216" target="_blank">📅 22:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31215">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3-mxk2c0CO5ZxYdnpC1v8BbULNSltRJX4xwJ9BJje1Z7i26cBa-nJgEfmc9GrUFRg3WsS2N2G_XAFS7uagpWah_AB0L7V3YcjLUM_3r4v6q0HuoRYYyzWE6DMlb4VHk-9JYVkJh-2A8lzH1ua9KoKeD4q_OqLmQYxyKOEaP8zz4wrT7Yg3OIqIE7MLljowaJkjAtLSFj7M571PNSRHxlr5ZOPj_S4K5hqrHQ4BpjdDqMovA4E66Imrduq9MD7T9f_JFwn1zXB1-E_dbuRrQQyHzQIH2ofDu8xMONA8bbyR24aZ95KTHZyjuuWuPc1LTRIW85FBLps28EJvY3pY4NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت ستاره 19 ساله تیم بارسلونا قرار دادش رو تا سال 2030 با آبی اناری‌ ها تمدید کرد. اسپارت قابلیت بازی درچهارپست مختلف رو داره و در واقع آچر فرانسه جوان تیم هانسی فلیک است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/31215" target="_blank">📅 22:34 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
