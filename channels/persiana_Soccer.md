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
<img src="https://cdn4.telesco.pe/file/hUcQJAotKD7h7GL5cEA6p4d3o0U11RDs7ngz5-q1r-Y028dCMBD_mJVLia48NmHP1aij7zwMGqP3l9kMkTDMNcxKMiXLe2GSQB20N_VLfcSxtBlBhg_TqzpE2CP7yf2eWHT2rlYhnjWzy4okItHyCh4NvU5YWBUKzJ_luJ9xFHClgKG9CO96dB1Kso0wgmCVSpSqOSh2kfvIWeKz5FNaij-OMJANyfBbabscv-WzLHZoTwc97x3LA2RS-FyvUoIzR6SR3u3JlNd125uLl09r5Ma6paSXNj8eoS9O0Ite82BldqFe4CtUYJ-SMxFj-fFS7IGm76jEF5WJhnmpJBGRUg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 615K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 23:28:45</div>
<hr>

<div class="tg-post" id="msg-29006">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnMLQuTwr1HyG_z0pufQR1Z_0-L8dcgYvxbl3QzCXXXYV62QCzYLkkw723LvY017X4RjHydQJ7mazLsJ1dDr4o2vx8mK1FwA6Cd-41obqwDcGXJoXi19nv9j1LaibA3kMHQRqUObYmZtJOyIhEKMxI3znj4N9gJz8cjKa6iuS2NZpThsVivffEH0Yc6rHfZQfTkL6hYvWPOJdPhlKCUTfnSBFD6S_FSMU1klFWuIOmbLMFX-H1jewobDvl-pWQ1bdGKBrFERsm9oNBUH19L5H55lWPLuMhMKMTd7-hA_dGonAtuqS3Lu-bs21urmV3kLgvlZ9-DA-oVtsn0POJ9IZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/29006" target="_blank">📅 23:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29005">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw0aN6coJA3iv28mKLQ-sYVyQHtMyyd8qyUcAKjjvy8dJ-VDtei6HquEc5oYbDanPEor2Hvyuw5R0NZHDHJT8wPeUWQkCI9fdDbwX3CoNvtZgczmDR2VjT5FO4FGl-niz5POQgNrB2BpAIPgguwG19tnuLXGO6ilNV8Hp-AY9f5PeCPg8UbDIoBzGGFeLLCzfMvwLqOovqjjH9OgkxchO-fMFZSlNFRqhZlAn34uID1C2EDxhUgPa835QQESibb3SvhbV5amsVerO2D_ltlSewhMbOha9Yz9Krv0IcxaMqR_lZvRx9L89yBELI3lPuVq5Bhzg6fTsRx2M5ZPmzmRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇾
👤
تیم فوتبال پافوس قبرس با هدایت ریکاردو ساپینتو امشب در بازی سوپر جام قبرس به مصاف اومونیا رفت و با برتری یک بر صفر قهرمان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/29005" target="_blank">📅 22:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29004">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bs6G0XY8lO1FyZytWRgliXL3jb0Yrl6Mx6hbfg1vLdiYFgibKzrXxpYZPX6ZVmyILKgcisMFylk9zDWQnthTmhs-ClrqtQChep5Q6pnuwO1wyd4fE591zVejBw3Ggy9CuGAnZdI4Ucz8kHTZkG74Anf2qr8IeWl8IPijG_A96XokFmvDe5LLk6ZPPMr0NA53S7z6Gwpe6U12weE2QD5eODqxYbtM3dR_8u4YyzV-RJtT22yM35KfiK6WEdNZupSJ0WSBmdFKgA2v0waVpOfQjPfsIxj4YPvwngKIcMIQJ9Q3cLtO-RzAxQ7lUXVlkuBu2XsQFwHSjzdfGNh8qRIv6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دیدار برگشت شهرآورد لیگ برتر بین دو تیم پرسپولیس
🆚
استقلال به‌احتمال‌زیاد 20 اسفند ماه در ورزشگاه صدهزار نفری آزادی برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/persiana_Soccer/29004" target="_blank">📅 22:24 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29002">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g4sFG5AZpYhsSRUTpiKK19vmokkIoR59SEmv06h41Mhf1-ugv6AaYl784unz5f56YNEXMhQDSCwW49c8QSaIIoG7mF8eR4WnFFD35GfIv5xiiECI2UjWsGtLe2JcJWpoXAdws42_v3shUj5rvzzmbCepbx2-VVlyL-8ibG9spmH6Lqb8jl0PPDI3_2LKk7TLblGKIZph9WHNL0C1NZAO9W7Xuo_FbEpsTiFQzvPCs2JJ0iuAcTkbjMeTk_lsOg6krwNGSZ6IwTceAK1pLJoZRjG5B8etyMM1L1WKX6DTUw6MGyEZWFOeRrsKz7zcpmrwCjqFPHxd0sRvMdg7pUr_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eE1MjswtM7QXyzjblrK3-_xzzLqh3bA2GGQpJbt2crlUYzCLr1sMTtfgFI7WnLHJFPJCASEQ2G8cy7cU2KVTLZWDupAmKEDjuqEB2KDwbHFTsrZVQByqP5sh0boOZm3eNOvmt5KxUMaUvPFsS_wQlowNO6O5oGH4xveSNd6P_Pxxp0yQVXVXWgNqObgqxTFG70NVzNhLMD5tcchsyiPfj0wmEoBRT9h8aizBZXF4UybqVnb8yGP-tJ_YOpmkf39m4aWcUoDdl0yfVJdL1Mnu7vJ0DAen9Do3rXsyFQvDQO0qiB82WW2GzdR2vBPf-9z-TACkAlcJYqc9WegrV51lDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/29002" target="_blank">📅 21:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EDmw7M3CT20B0ZfL-AIJ4YtvyLfBUM7Rfo0SfdpNuJeWq9_ISaUvR_zswXZoiQV98xleSGZw2hN-bEEQ-nfxRmGWAfQmjlrKPAFKWKy2nRDjE1zZciOEx1pP-_2wPfrhezJZtY0ITyEUDXzKLn4Ipt7J3hrelh5SVwV5hXklj22q5thrNm-oNOmW9Fl63xBDzanjiQkdKef3IUAj-KxyEssI2es_iJ-GrUj-_MoD2v7QxegUtg6V6L9VSBswycwPF4P9oOtWaTobJXguMyta_SV6O1fllQJGkk8jrwi67Vgw2c3cdw5diF2BKxwwKRK-BIBcDGRLzStqIKrp87BU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcMCu3uHB70y2L0tvn91bmvvy5-nODopTxgf-37Mz9lzngpPwlSW8zgFNpNASXFu1VsR0Yi8VxyJbNS7I82mKmDdbNfj0wtHDwKO0rJa9rp3bqgvwuVbY3bLpZz6Zq5O00S2weDL-WSTr1QfFHR1lsipcvkEEdjIsBuggSMjJkAKKPZLoOqISc1Hkh_WGtQPhNxLU8jqOHkSoizcpNFSbmjSaR8oF1_o8WB6BJ8We9Y4YNsspLmyto603Gfys75QW9vBdTJeNHz9_k3lZ5x7fDn_EXdtkZbO8w11XI6rcqfm8vp4OUQQMn79nwVPFN38j7M1OFxZhnphu1BkcyVm5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه‌بدونید 3 باشگاه بنفیکا، منچستر سیتی و چلسی روی‌هم‌برای‌جذب انزو فرناندز ستاره تیم‌ملی‌آرژانتین 282 میلیون یورو هزینه کرده‌اند که خودش یه رکورد برگ ریزون و بزرگ حساب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/29000" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6HM2GJvL_idLSfgPaVPTCGlUPZl6v3k_0kJGtzyf-WnMmgLfUPnC2vRRqW_ClxGRQZnzgKh6ofPYu0G1oSOIyyrFIS05kcWJaFDO97nbjz7WzJy9s8KyfdUdEmbuNZX4v798Ac8HGCRZmoW-QZaGAMmjZ0oEl1WWyjdnyi29u_fVcorucBIFQjrcfifZun7t0rPIimMg62Yx34WIoDLS2lXhDOpl5n0-x0x45yRYsHgkeom4wJ4g9j666ewmelLES8LItngb-6TsHMkwCscZn7Os-GrPcU32LQUZGhkZpeNeR_jjW8EAwUoDZ6u1DKhkooHFc6lPiq81MFw7Ag13Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درکمتر ازیک‌هفته‌باشگاه الهلال از گابریل مارتینلی و اولی واتکینز دو ستاره گرانقیمت و جدید خود رونمایی‌کرد. عربستانی‌ها روی هم 150 میلیون یورو برای جذب قطعی این دو نفر هزینه کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/28999" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKoKFOQn6Nj4PKUTIpJ3FyWNCqqhKSuW7-tLEcI1zwM5DXWw4wlVeAqVvVGTCBQa7gkaBnWYtlYgEtCk0gR_I7CRS8hiRmrod7BCW99L86MG_ZJm1JUnCzh-Q_liVGNLXXFM6XspqA9BvMW-6E66qEN0Y9-z5LoYOlfNjuTr4wWZb_ijkGIfP9BwI2YIt0Nt6KD1SyRmxYdpa5NBxaMAXLdOWuLT9KO5RCRBELtbNBdM5WK6IwkfYQ8iRPNU30M50oc8dIrU8S-mmUgi9sePwyFBp1cKZLxmnT-4AaaAcMdYktDEalO1NIP_66Z219SsR6LcerE4c_VEijxdskveDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدارهای مهم روز
جمعه ۱۳ شهریور
💥
بیشتر از ۴۰۰ آپشن پیش بینی برای هر بازی در بتگرام
✔️
شارژ حساب از طریق کارت بانکی،ووچر و ارزدیجیتال
✔️
۳۰۰٪ بونوس رایگان بر روی اولین واریز
✔️
۱۰٪ بونوس روزانه واریز رمز ارز
✔️
امکان فروش شرط های خود
✔️
تسویه حساب سریع و بدون معطلی
⚡️
همین حالا ثبت‌ نام کنید و و از بونوس‌های ویژهٔ بتگرام بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/28998" target="_blank">📅 21:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAc1_ANE3Sp0R2WuqI84rqlKUt_4LnOwYK4_iFbikEx_-YMRWsh8jzZLKrCVMGIxMARhI2VYQj5ESvWrwIc5NlYsBWAUXJxz42ovLwBUcWhXqS_UKmNaMwBfiwwE0U-7R8fEBKRWZNfYDJPDO7rJvHJQ2zjoXzKLPIZgLfdcm_wAYzVVOU8NO4bhu3KkbZs8Pwdgq2Fw5tLDEdrOzwrn8AC8PbJvSuElFfdHJcBouJMWGeAkH8LDw0Hzl6DU4LsEWzakurxSmU9l9foBiX7Lq3XTjIbvdEwRuw_QL2c4GT5ZnCY742IVG8lDyVPSw5ThLMgcRXxbWl9VSAt1IGzy9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/28997" target="_blank">📅 21:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbo7ZkB_GeRPtInTKX59-ZVOpph67Y8e5zCi9zVUsCwi0RfgU0GuUYTG5SJjXHtkT_05NwHOxwG7nzFHQZizGt2X2ccy5CR4ucgZevsUaXVr5-31jheUg0pwiBBSIjJ8SVbCvGlliDV9n9qy9D6BMe5f1YbtvKndAWiKgRpU1_soYlH_14_puRlVFsU78hG_Zre7qjCG0T84oiMnRmFILJ0KXDBwXRKuFIH9ZKmj3E9y7d-dVTDr_9RwgJNN3qeUkLdRz1R7hWA8S71cftEh4StfLJyIriM0hOVO2REY3z_0UTyVScF_huXedBMdLjldB38hAWuN3cYe3Ssdn9Y0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/28996" target="_blank">📅 21:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=ggWf92W0wJ0Xp1n7BNqOpZ6ME0JMJbyCCxhvtkaCiF9R2ZEYa04LRee6uXezyA5fQOyKjlW7V1EDDd0pJYxSmTGBisMXJBprNMaoGIQMsGIleEveRDMLOB5tgHa2zbOppE4NWqWtZwuiah-AFActzOe6k_hkAkvYLXNgIxLR_UGv8I3rFEMs4P6CV2Q2y0tHyiV0RnmFRbiPRAzMY8sEg87r4Zk6g1O1KBBtbHKfipYl8gS5Bzk8BDf9b7gaY44R_PcR3AwTCqZ_9YTOqOWD_BAaf61A6giuOy1UfmLDSicyvVMH3s1_sLfY-W86G1Beztq81MBQo5IFWPhJHg9IIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a1c45db64.mp4?token=ggWf92W0wJ0Xp1n7BNqOpZ6ME0JMJbyCCxhvtkaCiF9R2ZEYa04LRee6uXezyA5fQOyKjlW7V1EDDd0pJYxSmTGBisMXJBprNMaoGIQMsGIleEveRDMLOB5tgHa2zbOppE4NWqWtZwuiah-AFActzOe6k_hkAkvYLXNgIxLR_UGv8I3rFEMs4P6CV2Q2y0tHyiV0RnmFRbiPRAzMY8sEg87r4Zk6g1O1KBBtbHKfipYl8gS5Bzk8BDf9b7gaY44R_PcR3AwTCqZ_9YTOqOWD_BAaf61A6giuOy1UfmLDSicyvVMH3s1_sLfY-W86G1Beztq81MBQo5IFWPhJHg9IIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/28995" target="_blank">📅 20:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28993">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmDNqF7Pgo4bUCjBcu6ZpnAkS-uGowgXeHcEVkC0O0PZU4YzTqEeotI-hpKm0Ix6ZwNj1f8SAv804GOL28gOz-XUxAnd6Fts8ZWgR-hG0dPg-bvaeEVLyY9D47j4IDR4nWE9Jd1Hfnh2gr0S4qIKAFkzyqawFhQer_Sf3-_uUzST0ZLMRPISRj15X7IJiyrDiJhmuCa_zWMkEIVyFtihwZRTeidXF3RQsep9NXeVfeZySzwbCJ1Aka7RoMU6vivF-O9b32OJaqQNKB3H-sa6_WGEAaYRPOotbCotJblMGX-bMWDyIk5Ev55iU-i2KpwkjZ7VX2RdQskvWlqnjYlnmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پوستر رسمی باشگاه الهلال برای اولی واتکینز ستاره انگلیسی جدید خود؛ قرارداد سه ساله امضا شده و سالانه 20 میلیون یورو دستمزد واتکینزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/28993" target="_blank">📅 20:14 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28992">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vv29e3rxOdxXbGUcGMDDyGnUq5-siogELaVwPichUeHlie8u9TzTgjcIpMQTCZFCip31ppeZXmVJQmFwhcKvuDKgM7cH-cBy020TUKU956hnq7fjVmzxneorysPp0hh7d2DNuLOI-XP1kItkso0zuK4zTmJsSiKt_-ymly_7M7qGqWLMfWym8d5TQmNq8iN_hBBwxU1CLr14t8hqUBhybBVLijTf6mVEMsLkkZCyctcUtCITVWyQ8ptvzFBQXuboKAGc4ClMj3-FnJWR6I0yhG4JDbvUEAQe1-fk8x2ecjz1nI3GnwCvtpT840zZpIPuYL0rs8mPUTwTliJl0aSd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/28992" target="_blank">📅 20:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28991">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOZTvN-WIY-fuxCMLtSvWptcMtv7SxQvp3M0XrLmpFnXgErYGWUk6w7Diwc97SepcALoc3pF0flCmcSqW2OB4DMgt7HipmZEhDWjS4UnB7DgGrFOrts8wUEEqmGAV26Egpz9Ttd00jQJWJXZNCm5VESoUiY_FPSVrhplpo2soSMYlScizzRqcYxOTTbKAv8Pc-BmPqxkSyhhlcnoKDxPgYYQcRWQjRlvGYPX7ABgdsqgkuG24bnsjvxSNsHRqiaxmc4JZFyGmMyZD6qvSLTvY2dFnB_2rY5iq5qOgAAmqGw87h270Q_zhvS1wgijauy-OrYreU3TLOj4fXd652JurA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌باشگاه الفاسي مراکش، کوین یامگا وینگر ۲۹ ساله فرانسوی‌سابق‌استقلال به تیم کنگ آن هانوی ویتنام منتقل‌شد! کنگ‌آن هانوی فصل گذشته قهرمان لیگ ویتنام شد و با پیروزی در دیدار پلی‌آف مجوز حضور در
لیگ نخبگان آسیا
را دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/28991" target="_blank">📅 19:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28990">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇦🇷
ادای‌احترام‌فوتبال‌آرژانتین‌به‌مسی تو دقیقه 10
🤩
بعدازخدافظی لئو مسی از بازی‌های ملی، قرار شد تو همه بازی‌ها‌ی زیرنظرفدراسیون آرژانتین، بازی‌ها تو دقیقه 10 یک‌دقیقه‌متوقف بشن تا مسی تشویق بشه. اولین بازی، دقیقه 10 ولز سارسفیلد و بوکا جونیورز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/28990" target="_blank">📅 19:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28989">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaktirB7Bzlc1t68GRMsirBvrEHQRg1OiORaZ2tXwlnGhN-ZEGfQL6q_1k4XPFjDHYSyP6A6yZDtLI5m1rxYPwv9TlckVEpEdkYO_-En-i8hEyB2RI3SDil6DZvBoew2Hnm4AFoc8yVKELdEJjCAdRroZqoduwLEgf5-_sJHdrrr8AEOvxDMhXqyjlvjIrVbXwe2MsagFbu6wqiqpDAGfSIARnWGaVumGFSnp84dGal45AEmtwubbe6nR1_IQIyJdT04Yl3gSpk0Tv9X5psOi4Hg6WWqVhu4Gwxgd_8LTyNCPKhmmHUOzMbSm6I-uOHMcql5IGDUBQDc4qomHE1EzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بانوان هوادار پرسپولیس در ورزشگاه نقش جهان اصفهان در بازی روز گذشته با آبی‌ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/28989" target="_blank">📅 19:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28988">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=ZpjQnyhDzVOa9tj8A6NXpn_QGpqDlhEz5I8qQH8nvAfUZxgeo7uu8Bj8-tHrj6mB9a_yvmKnctSyiFFV0xPprVNZqEPG9x2xkyNlbuS2SLMAg39rjIzPkM3PeT6qX825Fl6WrOe98YXC0ICLJK-kkpF5pOLHChzB2TifUedpa25NzKI0b1gwrs_lDirxZvcHP2XcXlnhxx9xJEer6CeciGbtWpMLErGArn8rAJYMUbgN8hCU_AXqaF7oM_bANihn-21xxkPSP3uEOpAy367qpYDZrpOZYJNX85xWNPn0bsXliVGVdDFOlCr50UoXPsbIYmxzydv9oR9XkDBowYK7fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b51bad968.mp4?token=ZpjQnyhDzVOa9tj8A6NXpn_QGpqDlhEz5I8qQH8nvAfUZxgeo7uu8Bj8-tHrj6mB9a_yvmKnctSyiFFV0xPprVNZqEPG9x2xkyNlbuS2SLMAg39rjIzPkM3PeT6qX825Fl6WrOe98YXC0ICLJK-kkpF5pOLHChzB2TifUedpa25NzKI0b1gwrs_lDirxZvcHP2XcXlnhxx9xJEer6CeciGbtWpMLErGArn8rAJYMUbgN8hCU_AXqaF7oM_bANihn-21xxkPSP3uEOpAy367qpYDZrpOZYJNX85xWNPn0bsXliVGVdDFOlCr50UoXPsbIYmxzydv9oR9XkDBowYK7fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
شماره 17 منچسترسیتی که سال‌ها بر تن کوین دیبروینه فوق ستاره بلژیکی سیتیزن‌ها بود به انزو فرناندز فوق ستاره آرژانتینی جدید این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/28988" target="_blank">📅 18:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28986">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQN3hOpv35G8anayZ6RV07Ur1FTVsyS9p-pcoTzfMYT2XUieBwpXU_ZkxyeQwSmxMdJDnRvGxOMOCaPMjv38jNVaSmlHtqPRea9eLVl5O_mpbk7lNVh7YEBZS4uz77FLDDtgwwD4Eqh70rglIdxks3b0UtoLgDp5_3TXRzgHwHDT9Om3WA2FUjVR4XNR6FJz41x57HCCERfiESC-1PPsZbFniZqE8Ag25bf2iW4s4ZuyDlfGf-ikxaQxm0N9NEjUO6L9zq1YW3NXZFUrCDrD7zyeIfhvfTYKMBIylg4uXq8p3i_6_pYFCR_AKxx82TQjrpdVx75hfnw3K8Zt2Vki0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=evF6-NRjCreRenBcLVBQ7SCd8JccAEM_nCOhH2QH7NoqRO2T71fSp17m6v0zBXq0hdENOYv978UIgEXenRAwXcTmwVJj8qmCD11Ch82FHzYrSuI-pZeFDHarBME8sbhg-w9MnbtTSGtAvtvgXas1x5jEXyYCLqOL2FJ17MUQqT3PGeOJMCugmSwkty8yW327GT6qIZDZEpXd0gImX3B_nNHP3tps5D_eNsjgbOE5-Dg7Cw6b_xDJ4s_DK-vVz2T67ubLZUOBHyfkdyHuS8aRVrDJGLuoDhXkmFXvFpfN8wBg2IypTvU9t2Z4O_w1TP2hbTHszwiCuELTlmUC4CaPOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d340cfa4.mp4?token=evF6-NRjCreRenBcLVBQ7SCd8JccAEM_nCOhH2QH7NoqRO2T71fSp17m6v0zBXq0hdENOYv978UIgEXenRAwXcTmwVJj8qmCD11Ch82FHzYrSuI-pZeFDHarBME8sbhg-w9MnbtTSGtAvtvgXas1x5jEXyYCLqOL2FJ17MUQqT3PGeOJMCugmSwkty8yW327GT6qIZDZEpXd0gImX3B_nNHP3tps5D_eNsjgbOE5-Dg7Cw6b_xDJ4s_DK-vVz2T67ubLZUOBHyfkdyHuS8aRVrDJGLuoDhXkmFXvFpfN8wBg2IypTvU9t2Z4O_w1TP2hbTHszwiCuELTlmUC4CaPOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا:
هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/28986" target="_blank">📅 18:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28985">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CusADTsp400e3MUh6helqJizgZy2Xipw5P-U_34FiCwO9fWm2bXI2hCqnr6AreaKevFlEw7U79N5Ojt_YnDxlTz0Ur2a8TYu7uSU8Nh4ssvNdqxe0d0T8-t-MsNYbNcYPI_RwnUaop5zqw6w9Qz_Aw5kzAijXq2pWZBs2qw2JqfiNDatZrrnD14x742zIjOmD-vfVpYqI7Eli49ZvQdjuCsjjlYsI2a2Rz5oMIy4mjEk0Z8N6smaGdS9XDRMQEEb2WPERQwc2--WpG8WiXmQdn-5SsN6VT5mz0419oH0Pc7RS7hkC9QDqfyRgsI10kYeyYiiXoalvJaN3WZgagTWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/28985" target="_blank">📅 17:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28984">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAdGLb7cwc4wiFEu2_t4NlHH41CfW_xbka-u8KStNDsW4SQmXL3w0y0trNAcPhMy8VhCTminBWE4BQf49ejstWmsT5a43pOvbo6NGdTvx2BegWvch_lPdykQY2mkvj4xaLFUjbZXicyU5G84BukPeCsW3z_DIwxphVqmBDlew48zmn28c9o5GcChlUBQiVFwJIh2c3h3CTPUbJf3GV_AijgFJBl4nwVTcjHwQVq9G5abm1M1jnFuC-y_uONs949I4Epo3h5gv_27vLJhAcAwLnYdZM3qp3K9W8dDsaz8QbMkud1qremJK_zrOPpc49JGY1R8zYQ9XjU1gSpOpYziKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/28984" target="_blank">📅 17:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28983">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🔵
هایلایتی‌‌کامل‌از عملکرد ماهان بهشتی هافبک تهاجمی جوان ملوان بندر انزلی به زودی با عقد قرار دادی پنج ساله به استقلال تهران خواهد پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/28983" target="_blank">📅 16:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28982">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLnAQYai_aacQ4ZGsCobIf3WbLsi_mZBhtEofuaCr-8DuON7Phg0YoCq-j30NnHVJY-UGNg3cJOwaFhAOYsfkbQV6AKdZIio6IoAl0nCJx9oA8wgHRbJT1sFz0TWP4Fnwm2ErYJ3wjfZOtFWD620kF0Zt8iFSFJdPUPyoNR3DHznAJKgjpRMxe3nKhq6Td2tUlA5-PikI0YufipU95mWyIImfSw_DoAP8-sqWfcFqoPtJfXdK-WRCe32zQdWDQqHaebOqEdN3lSEXOXAKDNPZwBxSMXfSyZ-8au58PQ3LCpQMJv_gDwtlioaZnEWCd1XXiJIYSLaqAqonlQdqLFOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوئیس سوار:
من قبلا با لئو حرف زدم و هماهنگ کردیم که با هم تو یه روز از فوتبال خداحافظی کنیم. قرارداد سوارز بااینترمیامی درپایان‌فصل تموم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/28982" target="_blank">📅 16:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28981">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BX4nLYQQbOaLMzZLAA1xGTxt7iSyiXU8iW_hJ71wrV1MQUoiriqE0HWK7x248kaTjulkIyx8SgwcxVPjiE99d68Kc25YNGOaTG42PGwY6HjHzk5eBzPqDJLWipxNEN1xzG-l8ChysXzE2G8Qv41nagK7PjR9cWDMuBTeyG_IG_oWKBhTp0aOJYAy4JWHrFQPI54oRhFdArBF4ddD1dJ_qb888OTYIB_OpJ_1-am5GzHw48YwS4BubfTtbGed5-45epQapjHM7GbAUAsNp5oA9dBZe5FtVCCGPWRAEAOFemDFFpUw6BsRAl0-v0w_2J4JvOt3nNT5vKoWFE6E9w8biw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل‌گرا مدافع‌ تیم‌پرسپولیس برای پنجمین هفته متوالی از لیست پرسپولیس در رقابت های این فصل خط خورد. درصورتیکه هر بازیکن خارجی 60 درصد مسابقات به میدان نرود یک سهمیه خارجی میسوزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/28981" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28980">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp06kt4Kww5KJsFiHfHV0C1rPQkwfw5H2Af-MZUAapr1-CK-Bxqmm-_RfAxlnHPKIFDTpQn3R53fQGUNcHd-P6vfc418l_MbK5F_6ShAW96rEXWkfGZ8E1p7HhylWjYKhhOvJRy2gn9XlvizZpJEMG3hW9mo_IcIYxFz3Upqhp5Bugvrmja305IYNMotohif7CyhFq9Y0otPOazBZkgrMOSwjL58jJPFoZ0KxQ5G0geU7o7tWVGNSh2Gipfsnj5TJrhLGjmcsHZJc3pB8FZZ46WZuja4UBCxerk6nnL0EGzLdw9iT5vLE-JmWwZ81HOT_NxfXFJM9Uj-0dP-xL4BHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/28980" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28979">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjlxDs2g6qhOdqFyKEEuqqpOnvV6WpW5f7uEb_AxbLt8nalTsDtVOgoq-vdmDI145gTvjYAUbkSB0rg3PpLMaMvcm8t0_Fe4I8WvCYWJChCifLRULqJ9LxbDvvpA7fbFlxjrtb7B12D3qfxdomNzfFLSzy6HNiPGgqSo9-X6bnDMgDn8ZPuxyqncnTovm-kPrKShg33_-USF2ba7mGM45NqajoNCYGDZw2PH4v31fZsEeynTq73H7VfAIA-KKOo2_p3KmuNm-mm7tHylpEHx7zhVUnLllCK2XdHmZsfwex_kWQcq9NL6ZMgDHY6eDrQiSDn-4OKJXEe56IiNK3kAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ پرسپولیس با تساوی یک بر یک در بازی روزگذشته برابر استقلال رکورد شکست‌ ناپذیری خود در شهراورد پایتخت را به عدد 20 بازی رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/28979" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28978">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i67uQAx2EQJW8QAWZ2mAbrQ8CdIBD02EbDcVS_jb7dvyIfESmpxhaXIdcbbQVAi1bR92tSaWEziFUKvhd1p17ICaX9024rE1SwK_EsAlnXXr-i1ivLeScmsTvTkojcv09yYH36ud4yisXvfoVKzQsOcYcteeGmei6ldrwM87CknyfGHqjOb0Ag_EqDp1iRG_Uskn3t0LCYzyXxtcBoPM96ygEkGSOQAIdgBZTed4FCNDBbrFm6rXa-IM9m7mlfdJdotge89bo0ltwmPjXAIaOGULTudz8zSMVMaRqP9wrHTz9ge8HSjOrLpNHXdST5pbU8ffzotTzG6Htq3X2d_yuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
هفته سوم لیگ فرانسه
🇫🇷
تولوز
🆚
لیل
🇫🇷
⏰
ساعت ۲۲:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/28978" target="_blank">📅 15:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28977">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=XFQ-4thvZVcp9hJRggSGQuiaTMnrR2hcB-Z9vUJKNoNjYlzBSATTkHIpKpYrAdHsOfGPQ91O6JqErw03rwuS9_eRn7EWZhrUvYj0EWNueBZTY3WMWWgJ6ZLWcpckWuW6YpHJWful4OqQSuQ4iWaRWpR8P_BbFfajS_rFr8RNsszveHA3lqMZKgdw0kGtjpejiREVeSt8nQLQbYwmMZyXZMVIiercuVhOy41xNI1W5rQylBNGBnxsdWVpz5QDnW_cbax7cSPxPdyfM-EiObDL8qhn1rb-3hckH4XEu3PWfb6wT_R8Mr-8YwOy8RRoVIViumG7OotHoeeq7X65IS3lzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e310c473.mp4?token=XFQ-4thvZVcp9hJRggSGQuiaTMnrR2hcB-Z9vUJKNoNjYlzBSATTkHIpKpYrAdHsOfGPQ91O6JqErw03rwuS9_eRn7EWZhrUvYj0EWNueBZTY3WMWWgJ6ZLWcpckWuW6YpHJWful4OqQSuQ4iWaRWpR8P_BbFfajS_rFr8RNsszveHA3lqMZKgdw0kGtjpejiREVeSt8nQLQbYwmMZyXZMVIiercuVhOy41xNI1W5rQylBNGBnxsdWVpz5QDnW_cbax7cSPxPdyfM-EiObDL8qhn1rb-3hckH4XEu3PWfb6wT_R8Mr-8YwOy8RRoVIViumG7OotHoeeq7X65IS3lzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های علی‌آقادایی درباره تقابل روز گذشته دو تیم استقلال
🆚
پرسپولیس در هفته پنجم لیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/28977" target="_blank">📅 15:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28976">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=tA8LFPgbPkjop7aBsSVhv3BgF2kyyjdQm8S_BFRZAgAnAt7uI2mFf3_YPa_sSleLnWPD2lPVmkb0Piyykq6bA8Js0590awTXkjFbxQCv6db5t9KlCDU7W-AoLPlldmPRfCjBx9skIbqIBmJ_F57dan3LbiSnRgcvRcr9Xs898brr4RbJYUdlvBf79Jxa2myLRKIWtwDY2P0BZWZUwVjj25POGun-JJ3rbtffolkbOjXEnuWLRvncllzofdEkQISR4Jgt0Jf4c-VOgOJGGKFEqNEWd5Z8Gw09bb9-8WeeoxPDWYO81OvrTDix7YY6vFp9JmRECkMzfqICL1h5WpAaIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9de6749c.mp4?token=tA8LFPgbPkjop7aBsSVhv3BgF2kyyjdQm8S_BFRZAgAnAt7uI2mFf3_YPa_sSleLnWPD2lPVmkb0Piyykq6bA8Js0590awTXkjFbxQCv6db5t9KlCDU7W-AoLPlldmPRfCjBx9skIbqIBmJ_F57dan3LbiSnRgcvRcr9Xs898brr4RbJYUdlvBf79Jxa2myLRKIWtwDY2P0BZWZUwVjj25POGun-JJ3rbtffolkbOjXEnuWLRvncllzofdEkQISR4Jgt0Jf4c-VOgOJGGKFEqNEWd5Z8Gw09bb9-8WeeoxPDWYO81OvrTDix7YY6vFp9JmRECkMzfqICL1h5WpAaIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسین ابرقویی مدافع نیمکت نشین پرسپولیس دربازی روزگذشته بااستقلال خطاب به محمد عمری: مدافع چپ تیم استقلال خسته شده دریبلش بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28976" target="_blank">📅 14:49 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28975">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhGIohENDXW3hHgYn_H16y1VFU0BfoL0XXs9EjxCtIzjfcJf9k-WvZF_3lgyDp9FLzmTGDgBjQbcK05HeHlCvbuRxwPHgBpMHfgGDddk2k_DH6lJo6AJDfKMeEbYilE8JBPbqpbYThSIsD3mdkOu8SrjHFl49ZO2clX4hP6OUECPSE_O5si-Yfwr18r9NEAPiJ77n4oBaT47xiqYU43qIZhNVm6rxPAigEt7u3HczV49isp03rWR3J4AWnuSzqS2SvhPmgzjkUbTB-o8f4w241nHKu9ZcNnCHvUw0o8vx907WXyNo2ErockTZZzvIK3xNTTLAVhWcfRl9yWX9OJtRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28975" target="_blank">📅 14:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28974">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=RuVolY_7znyuA3DUP_rlPF6tYYpt8JLOr_etJBQFl8gim8HkzjO-PJJuVDPXP88miYqPgm7pU4w9qsXgnKkEhKgqsv9ZNWq20HwKDDQ6AJhIPgnXM7lzNbTewYxfShi50WdOOwtVTpyXxG_dj1LuxRYoFuyrIgcwVo5gZ36bYCRR9d_E0DlGyI2P_jHlwg1aOHDe7tC3zx0JJa32sH0t0-wJcv7BoNLF0ZAKB3femoOn9PTrFUKPAoeQKUTfc78CB0RM7sr0KprI8hzOJYqt48hjHTaYNvUbajoYy5yd6hIj0FjBQqFu8xjX0is-MpvNMTnPW8XFcGdnUEM-CaMgpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a21e3ccdf4.mp4?token=RuVolY_7znyuA3DUP_rlPF6tYYpt8JLOr_etJBQFl8gim8HkzjO-PJJuVDPXP88miYqPgm7pU4w9qsXgnKkEhKgqsv9ZNWq20HwKDDQ6AJhIPgnXM7lzNbTewYxfShi50WdOOwtVTpyXxG_dj1LuxRYoFuyrIgcwVo5gZ36bYCRR9d_E0DlGyI2P_jHlwg1aOHDe7tC3zx0JJa32sH0t0-wJcv7BoNLF0ZAKB3femoOn9PTrFUKPAoeQKUTfc78CB0RM7sr0KprI8hzOJYqt48hjHTaYNvUbajoYy5yd6hIj0FjBQqFu8xjX0is-MpvNMTnPW8XFcGdnUEM-CaMgpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28974" target="_blank">📅 14:20 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28973">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZNuyigEbUXowq--jyMQ--dWK8S164TFhi4lSTiUFW4TPUu0JMrJVGwZMrvMzy2Nd5TY4_RUf9WjkzjErcOWPz7GASxjjXhXTQAR_mBtOWZc6JtyEyIUsEAKr0QGdQi1m7Zkz37iyHyBbPYjhaMplZxKiL9Edz26yMvJzxICazDzhPvPCuHTNhe3qjmixmIKcz9CDzU0s8Vt0OjpRYcWidbth5ctrnhgLbDqwpYfBay6mWsrNr-pxIHPlOsom5YV4TcXgRlSPQDIITljnuDcHHgh6WiJ-J6-Nrpu3FCe6IpMx9b4zzqiiEeeDE1Ic2iLMeb-BnJzKIPfK-X9HKu2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام‌جوینده همسر سپهر حیدری کاپیتان سابق پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین‌ازسپهر طلاق گرفت. دوس پسر جدیدم یکی‌ازخواننده‌های خوش صدا و خفن ایرانه که‌مردم خاطرات بسیار زیادی با آهنگ‌های او دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28973" target="_blank">📅 14:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28972">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-5KM_xqFz2IiEkIZT6WKblpLeNYaTLMgLPDgK0q0NybLncJQnP4IYFwFqIH29e57XSEOlMsr8hMHPhf5bN877BJSt8RYmXfEHP0Ra_CmGreaAWkNJQcpMvfp4WumXnYTuHKW5VmbHDqaDyNWVYuQTmNjJTH7UCHcVctlNomouHCx_19YU8KkjpQjLdLcQJBQMuMTApvNLJmQeDfQ3pBoTib_9ivtQ0z8y7mz-9DcxOH5MPeHHSpUzl_s_ZhO4l4Gq0LY4ad3a1IGl1zCPKrFaMcCTrcHATE-z0kZ6BJVbqffV9pw1ZD567xgRIB15wKDPyLThBYjOAjNHKSm9iK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ: رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/28972" target="_blank">📅 13:46 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28971">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEPLBAVxsiArRV_4UuuxqEgrNNRfTUdevbj6lPyKo40dL1g9gvl4L409G-01qxA2Z8ZN8paKy58xjW03Lk2Nskel8XKjiW6F_UChBljhnt6I5AXQY5FkCuHyRFJ3kN927sCfnPRZxMlZeIXcB1mFMOJPM5OPQDI_WQ6oCVb2PvYLUoUS9dgQXuK7ibNz8fOJ4TuElGqhMlV7N-7o0vSOGEewA_Im2EB-Ww-HdfoA4XTaRayjaQrhcI1QnxpcMXyik-tL_3FdD3D1C-ULf_Xls9SjiP1rf--QPjAY1I5ZXZFVVb4z1CvMNQDem6RsKh4GCaC4WvFZPvDS7k5BgyYevw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش قیمت وحشتناک محصولات شیائومی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/28971" target="_blank">📅 13:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28970">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1mT4kC9otYzmCA043tCrPkADqOF4XVM_y9OXrdq-sWWEr_6kmRM7Bo7MVSqZMGs83maDRUR3mvnA135AAo72Z57gH5JQRBw1Mv97-PtNv_VXwWXtZFOJZDck_6smCDOR_sscCA28gR4YyhxIJf8J4i15cXTXovjUrwneEfWd3yEk4qH0WTDQ3oPJtbVpnLTBlygbjmBY_1LYT27XOP-re-3Coo0twvY_iZfNSvx7-jc-BPKEP7K638mi7BVU2vG1lpy7j4FMZ3XRMtLLm3jdMomTuCpSMI1dKqgEKARhXQLCJHjfMixM8Szxh0kDYSP8YlC3higCc458Q-qvPu6XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28970" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28969">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=biQo1CBzEyD1eiHg_9XLRK8kIWoyapqvvkS6zXHR6vm0OAlbL3ID7Ts1VqLXlYA1cbYiFqC8uML6oq0d1Nh9uBOSYWbVoRf5rjdvuwVDosbqJJ97ETvWSJGeHBUyiR2LxJfwITWA-U7vq0gpHiU2g90nwEAqXr_jciQv7KhGVzQWEj-nAqhTzvIsYlGB0f2RV0KSwOYmdoLOjaAHIc3A9NP2oBJ-PQnk3STXTV9zPv3Ti6JqQuoN8hCyLvmWNZ0O_c6N7ie7pqVQAQFpGJj9n5YbvqcNP-lyZPhvb8fV_tdKTtbw8tk5r51nfoKr0gYnJMfklyrY5geChP4XwoWfZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=biQo1CBzEyD1eiHg_9XLRK8kIWoyapqvvkS6zXHR6vm0OAlbL3ID7Ts1VqLXlYA1cbYiFqC8uML6oq0d1Nh9uBOSYWbVoRf5rjdvuwVDosbqJJ97ETvWSJGeHBUyiR2LxJfwITWA-U7vq0gpHiU2g90nwEAqXr_jciQv7KhGVzQWEj-nAqhTzvIsYlGB0f2RV0KSwOYmdoLOjaAHIc3A9NP2oBJ-PQnk3STXTV9zPv3Ti6JqQuoN8hCyLvmWNZ0O_c6N7ie7pqVQAQFpGJj9n5YbvqcNP-lyZPhvb8fV_tdKTtbw8tk5r51nfoKr0gYnJMfklyrY5geChP4XwoWfZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قهرمانی ارزشمند و شیرین کیانوش رستمی وزنه بردار ایرانی که عده‌ای نذاشتن برای ایران وزنه بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28969" target="_blank">📅 12:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28968">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=Hwo4cLY2nW2tilU4dQcbW8uO5BZYHOlz3tZ77VvG-GZw_s_wL9TkUrRaaH0qg-4YiBi0MlHJ-QfuxzF47n8GIvYHLhs_l4MOb_NQPO40FEOj0vcCor-Y9dqHYjPGzfv_Jme91w889KB7d_V69oCb29HXW8_-5lmUga3-Ax-FSuCRVPQRT2nCt6FhPvZf_DO-Sp6JTAv0yMMDpl5hU-eCtF9H0gpVlv7-hEZNlVvZF31U-JhN_qPTqyzhnKK088QT_DvO42G2jbAFCyMrVEHn281tKLpvyUTASgGohCDWQbc4-MDallJ8rX2F7YcxvQ5y4xtr5acT-V4fY_1FieTZIBJwj4THsaAm8_pzyai0PghlTUkYovdCCNa_3Rg7tSNZ3FEAJIBrdIZ8FUP-1sM8UPirq99SA0AxxlN_m3awTND_PHeORnKXeMbjW7PNXi1i5Xe3l6FjW71vzybfSv4J_G5gBGFHf_BhHbNPRGaIqOtOG25Uo32JMVn6eUDEnE5eTWdbbywePF3Tkg_Kqm_QrpXnce3YUCg0bGBF-4xBlu85hel6eMBx_umFu9uYXdF34zcEuRKivSFMuNV_EPF8Alz0qtwGPy-dHwFJpv-eT175dB0FYDlsZFOrpqFom6TgkTpCf-hBmExERadR6iFVpz5oJrI79zFjdv0flTsqWhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=Hwo4cLY2nW2tilU4dQcbW8uO5BZYHOlz3tZ77VvG-GZw_s_wL9TkUrRaaH0qg-4YiBi0MlHJ-QfuxzF47n8GIvYHLhs_l4MOb_NQPO40FEOj0vcCor-Y9dqHYjPGzfv_Jme91w889KB7d_V69oCb29HXW8_-5lmUga3-Ax-FSuCRVPQRT2nCt6FhPvZf_DO-Sp6JTAv0yMMDpl5hU-eCtF9H0gpVlv7-hEZNlVvZF31U-JhN_qPTqyzhnKK088QT_DvO42G2jbAFCyMrVEHn281tKLpvyUTASgGohCDWQbc4-MDallJ8rX2F7YcxvQ5y4xtr5acT-V4fY_1FieTZIBJwj4THsaAm8_pzyai0PghlTUkYovdCCNa_3Rg7tSNZ3FEAJIBrdIZ8FUP-1sM8UPirq99SA0AxxlN_m3awTND_PHeORnKXeMbjW7PNXi1i5Xe3l6FjW71vzybfSv4J_G5gBGFHf_BhHbNPRGaIqOtOG25Uo32JMVn6eUDEnE5eTWdbbywePF3Tkg_Kqm_QrpXnce3YUCg0bGBF-4xBlu85hel6eMBx_umFu9uYXdF34zcEuRKivSFMuNV_EPF8Alz0qtwGPy-dHwFJpv-eT175dB0FYDlsZFOrpqFom6TgkTpCf-hBmExERadR6iFVpz5oJrI79zFjdv0flTsqWhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/28968" target="_blank">📅 12:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvMtjZPPkwTq8_VCJ7sRnmcx0ogGK6VhTJ5O7k7eHQD_dd3SaVRRKYB9BgieliuRgkhukxnIfRc3zdV7eLX1dnAxaMFm6fiZyoX2e9B1T5RaImMk12GLVGhHJcmWLrAk00bBHX56hRRng7bhwx_MWmKaE_m7sOgOvrQOxk5txAm9q5doWRrKpiEjZByu2ZLhrFmvfoNJ4qLtw6yLOfIpUI_legcXi55p8zbsM5QBwf7q1i4EgI9kVYseOX_bMJkiQfTLvaMEqd0adSfzy7BnwjiPuHdkBK-f_XiewoUfQRFxPKKDjsW38kWOUdgVIC4gQpYSxVIYH2fIOz834KGaxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/28966" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUnp6zNZsCOnob6ZUmqQ48vxUEULBKUWaB22FQdZhdZEZ8GYRhkyLINqTH3jk6LljMxEKkyT-lesEBltbg2CaeHKAd5MuNIn_sHh0IM_icuJk_sZYqMdk6Kd8w5xU8BLffd2qj3CofuFnSTITEwFEkdpJ5JTsTYPHAuD8vVnJsGPM53D-lhCQGbYtv_ukCQ_YHWAlKHZdUsXOH7Jwr46CXDuq11Wf6qV4We8wky36F9FQ98Z_aPALZNsWVE3GEIdUWbIBnABv3kIVKSgZcWuwDI0Vt2oOZXDVHq3LhtvuhZ79K9Dx6kgBS7-7Tf9BIWSGGGlvU8KRuXQCZ5QNrQEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/28965" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnX4CapZMYFO9u6JVBe__qMm8gudWZYZd4fI5Gocg0Jnx5TLFD_HwMwY4x5prwCEo6cXtQmDTVAEWdAHXqQFlX4KyIDRiMVxrtslZUfBLYHf9vE03u_jZixTAO00Wsx6K_xyX1Uw8YpWw9d9YHKwRPC5J73dfttZnoC9QXTDWnTjPKDqhYV5ue_1TtKXMxGPG7XImfQrobYlH6uT-pN11VrSj6hPtYcb-1fcNy6TeItzKEhABkfhg3lpzCiGkzpRHR-kbQhMO0DrmqewIDwSOyYIGmakqwNzxLxHZsGcZ8RmMLXBG1wTlV4iXjFLCOo99TIW8Z0EhrmOcu-h3NGwxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28964" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d582283b.mp4?token=YHJQFJLY6CTlKctIn3At25E-j6yKChVzTTXbUCI4BBqKQemXSb2rsiKyFHHsYNiXqWRYGpUeQYSMbwt8wEwAHGrl4fMBLi-U6PR0irszKBml1hTOsOAwqB4bR4Pd_m50xUC4igA_upqJd6FVmVXRbZnF987BGeKRmIiY3JbiV34wv1-JPC_k9JIpedpK3MRita-r36ZqqTWVccFyv1A-09SMFNqj4nfvoeRHHqnirX_2VqaJ2IVcqcxIKaNuYpC9vYOKjCibY7uZx8ccypIEXp6n1bYadR-knehCzJY-f4tKdXfAntRghNIJzhJQXjw9EqbjYyv0UJja0_Ky4DwPMHcw14TzqCYuDRWRkpg312YgzZwCRRn0EIY6V8vV3ULqFXZvhZ2iuOAwLVbtpni4fcxK1L8t9MmZASJ41-auv2bVEdGNlOOYHJMqL3YvH8RSGmCzUcm4qttKzukjlpm9JGZyssKOmLbdxEq0IYyWXOmn9TzrhycPdqm7JHEcWdpv9gkTzdYpBGkc4FSzeqOnFVbu5mKQ8XVwxi88V9thVxMuWVax4ANrXAevU96q30dzzwJws3MKt7ZD7wGliJr3MYlSkCwvucqDixmGfthnG2VRzmyygc1_anIyY41U7sBUUUc6IaBssISM2e-LeNO-l79P8OYnE19uZQlhu15ogXc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d582283b.mp4?token=YHJQFJLY6CTlKctIn3At25E-j6yKChVzTTXbUCI4BBqKQemXSb2rsiKyFHHsYNiXqWRYGpUeQYSMbwt8wEwAHGrl4fMBLi-U6PR0irszKBml1hTOsOAwqB4bR4Pd_m50xUC4igA_upqJd6FVmVXRbZnF987BGeKRmIiY3JbiV34wv1-JPC_k9JIpedpK3MRita-r36ZqqTWVccFyv1A-09SMFNqj4nfvoeRHHqnirX_2VqaJ2IVcqcxIKaNuYpC9vYOKjCibY7uZx8ccypIEXp6n1bYadR-knehCzJY-f4tKdXfAntRghNIJzhJQXjw9EqbjYyv0UJja0_Ky4DwPMHcw14TzqCYuDRWRkpg312YgzZwCRRn0EIY6V8vV3ULqFXZvhZ2iuOAwLVbtpni4fcxK1L8t9MmZASJ41-auv2bVEdGNlOOYHJMqL3YvH8RSGmCzUcm4qttKzukjlpm9JGZyssKOmLbdxEq0IYyWXOmn9TzrhycPdqm7JHEcWdpv9gkTzdYpBGkc4FSzeqOnFVbu5mKQ8XVwxi88V9thVxMuWVax4ANrXAevU96q30dzzwJws3MKt7ZD7wGliJr3MYlSkCwvucqDixmGfthnG2VRzmyygc1_anIyY41U7sBUUUc6IaBssISM2e-LeNO-l79P8OYnE19uZQlhu15ogXc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ:
رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28963" target="_blank">📅 11:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVDbQ4QckgfWRW_-VpDwJR8zsCdujS299DczKtj3pq0wU6yMotWvz390Lyh_55cBzj_gYJQsj17jeELQfcKwCCxkU6_6aAVqP9K4mcDg-A1U8etvCqDjDQSgjZijjeBtDRoSEQY2UybE1enbqA4nCt8OXX5hGX9hUI2RVZLs7AK6cZAB7LZZtGNTMLkexePz7DSMHidfbxn5DoszKu4EWYQpr2tP_O88-J2jQj517_cmh-Y1SUe_RFDhwoJdJ1KIBTiCTauAz6EauK5xJNquIn2TG0v4-X-ZzpDNWh8wq9R2exM2Q4U4YCRDVhEJ6SoTyvLqFpMJJp9t-rrFFUqglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم منتخب بازیکنانی که در حال حاضر بازیکن آزادند و با هیچ تیمی فعلا قرارداد امضا نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28962" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWUTisB3McwrNvuma5MCpSAHkJ6fEAicwfsPL0cU0IyQgpqYTIRQVbcSEqDYa1580QZhRZUydnYxSgMwozEniFLT95-T_Sc0raJTrD2eR-pNXakpxj7ezc_eK7FNJgpZzOiH-bfjJSVv2uP7AUIFeygEKqUEhHZ6yAfUkoJBYCLwAMM-BPYKJkqDPdbx3QXerBNhdvko05zUppzG7D8-5rymOsRKWJUCnI580bvQ7ukE8MLqIh7ESg6JV1kyOeR-dnbhgdR4DSX7VTPHNAGocxCxbAdgZ1zso9mNPLxJb1XEhpcTZgmyokCqS-3tEhudeCoX8OG5rvLKn4yoAy_j8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌برگ‌ریزون‌لپاریسین:پلیس‌یه‌فرد ۱۸ ساله رو که عضو باند آدم ربایی‌بود دستگیر کرده چون در حال نقشه کشیدن باچندنفر دیگه برای دزدیدن امباپه بودن تا اعضای بدنشو به بالاترین قیمت بفروشن:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28961" target="_blank">📅 10:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuwuFqghEjeiZ6r4pbx8YNk78ke7xwrBqqWNjZtTtnYsifJYDPU1Go06y6MqaXBqa7Wlq4lheYaAtfL69bXGDaohf-eN54JfyjOPbBbfmQUAybY_xCsr95aCZ2jDIKpfzuxGGuj9mPfSEP0Vb7jGRQRi_-2NEmY6WFA0tnZHEPJXswU4_5-_GhJzljukDIfAafndbHJXHX3qskhsFLQAxakH4Nl6sAN8juhn58g6gejVxWxnBYKeVOxP_NcDUImtCOQnxSw_mn7N_ebPcSjkjqMGDIooK9iljfIgI2eXrxWphP8GIWqq1IAr9SKxY7vPyjUC07grhh56XC8MGquMPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
👤
بااعلام‌رسمی‌ فدراسیون‌فوتبال غنا؛
قرارداد کارلوس‌کی‌روش تاپایان‌جام‌جهانی 2030 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/28960" target="_blank">📅 10:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEnIn66TKuteu9RJxQudFpQdclty0Fu7ssxBXgAIcgWl2kWqoBVJ-X5uwjvYba2sJBFEvJ-b4cDXyalHEpKRT35izpxtXuxgD2FFLbdIxcEUUwC3qI47XdKh7Lz600_ocsimRAF1abyZPE3tAzhhJ0awGtDkKjIexRRe9srmFcsWpoIy94D1elvL272IzlnwG_siKjilzOeuocR6HVEZKLkccChHu_IuRVLJNyeeQGgH-TGhJbmeaK_Dkfyv059c2L_nWyAEKO9S0WluAo-gMZBZrUCF-qNNv31m8io9fYnmw8OPryh0FjoPI5ESVlAxOpI2Wai6Wj-g3T5ERySQHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28959" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMXGO7sAIu-m_ZoRYgS8y0esSAegi4gpr4cET7k4-tdO5YKeo7sn7jciItSMmMzD9Ks7gTMJShAcVaYIwXKXQDA5aIvm3Zh_VvvaQWzn1GHHLc-hmxB0Y2ZLN26PvRfJSAdsuGPWEO_hMTWwwaqciOFi9H4ZKaXFY2nPT16D6n5PnPrt-GSkuc2Pj4cyz7y_yBxSlOSdh_2OR-dpls8R1i35bN54z6cZnxr_NPSuIYgc5GGEyBt2KIFjlROjB2B2OmUiRVeo3zEltW3gSg6eCsQTZ_jFU0d7OzCqBAapr-9BS4Gcsls-O8rNCE54EJeo9AQRMppUR7D0cuMyE3EtHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
کامنت‌منیر الحدادی‌برای یاسر آسانی پس از دربی:
«به تو گفته بودم که تو دربی گل می‌زنی
.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28958" target="_blank">📅 10:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHYub4oOmsQ9Tu1uislo6IBt67rFVzqCVZ761QT5ZFb5XprbuMDd7oCM-tQS9uamIwomKMxr62gC4Z3PXhj0ifwNKkT2moOZo8CrFHP4K7dkjV-ikc3uvz258S9VykcNPl-SE8vJ2XYvn6DkgNPj9y6_zDh0q94OcdWmI_OIoIznFznNlKjBqO0G9mEh0YHN5Kbpw-yKRnmuB3zLE-VgAYjM1tINh3E4-wt8PJ22TlVreg7oj2XLofHhnoRrBA2A2vwNRlnsEc71bh6YZX6mbmr-1wmY94rH4cCZlB9sa_LdlVDtYLlWBdGKWTXGNigY3LlikdvBB18_mLm8E-YLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28957" target="_blank">📅 01:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVggffYqmowiUhrXCGQC-DKdtOjFP16ons8gvNLDbDo6zadsJpRA_W0LnXOhk6oktKAO_1ZYB0s0jn1RuAf2lmW1TdxMELNep6bKDvUrkFfQjQ_vatec9tZkMXjeRCkqjWQEY-17W96IKJ94dG9ffQR5DUm9aDADFxq64YFq3rEJuQpsBK5m9nwA8RDW4wA_B0ff6QAttmanUcOc-D30XhkwtVM9ohv7grWr6UgP6650UFtuLMkYCRo827PDWkyrCV7It3BuLchwTq_b0sqaG85B9ELJT8D_71LUP5FzlMYTYaXOyIIqEZVGSUkGNEDNlxdHtGU1YueGoV1cbswEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28956" target="_blank">📅 01:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28954">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbXi6-5y0dxtQWpaofBEQcxmIo-vXAZxYVohGVodJpj0Q8xbJNdXGRwXjOH87E65o-ZSdr9dCHFg0BysWUYHPLwJKchz0I-IgcisLuuLvQ-oObeMjqVtGCRLn_aI-9ah0GWPn_u1LbbMVp_yNtkkF5i92pp1uQMHknS5PuP_3RWN5fa2aNjyzVXxATFFCc9TdLw9965bbwkymDgYDmVjwNyzhUG8mCYwd3eWe6Wu0zfN7eX-3QSYmb6mpedJImwaU6_RpI6j-eU6GEJoQ45NWsQjrSTU176_HTQTkkKChMvDyveNucq2dM_e7aniUOnwNF8R442R2uzK-Gd6C9bxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛آخرین‌دیدارهفته پنجم لیگ و شانس صدرنشینی یاران صیادمنش در لهستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28954" target="_blank">📅 00:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28953">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwnWSdUl70tFw04STmRNvYgqLcSIs1jnpzSbXAf6oECz0rhxbOllL9Nwp3E91q6mhA3yqVlQMG5ztICYkLbFxhNGmXBGWk4mbx4NSQ6AL9kX17USzUIk8j2teehtu55iAWU94CLJtWZu3-htsodFRsI22Te3-OhJLLIJWLmSZExhi5z0YNahLz9xMFGs_hTWcTBMPyE8EFip7vFCl0CeBVwue7Jb76E3ZRrOZ8NrVGFwW4vpauzPdG4C8dsUJThzXsFfbMINXCJrwg58_x8U4gUAJVrHkp7SdQvO_4TvmXJqyLrJ3R1ujEuRGqNWmj0knxdRQk5Z3jbEFldKN2TzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌ دیروز؛
تقسیم امتیازات در دربی و صعود بی‌دردسر باواریایی‌ها درشب دبل هری کین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28953" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28951">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXjdpQ50Hjn2Rs-YZGBUz0SdyZTbPb2RHqZMetXjRM_EqXHYYzKwOdjwTCYtR2ZlfOzcTx8SG1eFHwLm_yXTg74y7HIXVl3X1DlsmW0XB1vr-wNhiLU85qIv7hb26g9mb6WDhEuuTtBx3PqFRFxtlDOXOadM3s9X0MLe6PPlFElvxhN8-YjQTP8uyYOm3puQiiLBN4EaBxuZuTVmbyU0XVriXyl3bPc1yKA2EWsNOv-J4OnVYVaAk1uhKnUHBnrbzQIxDnISl0p1BrqGOMeduDFlesLXiVeYNM9FMkdroGcPXNuqT9IdQ3ZMQA06JzBTWW6cSI4F5Ccb1qP_TLmcaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28951" target="_blank">📅 00:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28950">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHgwkcozsST9XXqOaJuXIeGTL7kzkytBDP52Ban4pE3hzz4c2kX8imV52uKcOPmh9jKuQzAbhhsAoS_j3eTRe6OWfBeGdIO-lYOutK1zcan7jch8ZUAkYjv9xipZ1GEOk3jB7PatdCt9qLp9AFwr4DzDxGZwZN2HN9enbzHv7qEJSubcYS3wW-Smu609i_O_3X-A0DfCyG4ENmLkLDuc0UXLaPIG9_usJnTss4QlVZLF0m4XtDSAKDnYPpCYGySlovA3eM5PMxFH-cQ1zQe1UOLUDguSCuIIL1mPT9tGOB83P2YICYSDEN_n4Q0x9bjEe2AbbZZV5qenyX9jJvtnIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌براینکه محمدحسین‌صادقی وینگر 21 ساله تیم پرسپولیس ازلیست‌ سرخپوشان خط خورد. دنیل گرا مدافع‌راست‌مجارستانی نیز از لیست کنار گذاشته شد. همینجوری‌پیش‌بره یه سهمیه‌خارجی سرخپوشان برای فصل آینده رقابت های لیگ خواهد سوخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28950" target="_blank">📅 00:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28949">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=slVNa96Ym1CUAEX6FyiFTSysFmHlhrR8LlmehrLtriLnK6UqHFaOxNv4g6CDLTVaCjKZ69lmG5vPWWDcvWhEX1Y_8y5bbEhRoIaNDO_gM_gCwxgWFQizqXFqkeNlXOYGfGcZ57W_NK6OTMzo97wyQXu3j6mo_RPtJZn9dpRixmdBMuMYA3gpxHWJ4szL3D59ffWvB1yZJeq5u0Gdb6rTzgan1ua_fEGYnv-D1W-cBeOGsO1AUfUROuVERmh5wxmkjLvCmQ8dLzJvk3TYR3jQLAaf0eNNuNoT4t3RClpnnk9deo87_3QNRwEMbkCAh9b4mYSGN87KE5MPGefvL_Lnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=slVNa96Ym1CUAEX6FyiFTSysFmHlhrR8LlmehrLtriLnK6UqHFaOxNv4g6CDLTVaCjKZ69lmG5vPWWDcvWhEX1Y_8y5bbEhRoIaNDO_gM_gCwxgWFQizqXFqkeNlXOYGfGcZ57W_NK6OTMzo97wyQXu3j6mo_RPtJZn9dpRixmdBMuMYA3gpxHWJ4szL3D59ffWvB1yZJeq5u0Gdb6rTzgan1ua_fEGYnv-D1W-cBeOGsO1AUfUROuVERmh5wxmkjLvCmQ8dLzJvk3TYR3jQLAaf0eNNuNoT4t3RClpnnk9deo87_3QNRwEMbkCAh9b4mYSGN87KE5MPGefvL_Lnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری جنجالی از بازی امروز پرسپولیس و استقلال در گیرس عجیب بازیکنان دو تیم که منجر که خونریزی گردن عارف آقاسی مدافع آبی‌ها شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28949" target="_blank">📅 00:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28948">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzLTY7pwYKKk9vJc5fReS7yuBLCYjG3zeyxAV5DX2YkUW_xrl5AkXGGHdd_Oq1F-PfHd1AZOe73US8ziOp3IwXPpiF2V5XYt_8rzJxsNOvHkIE2Q0o23tjCMS7ZyU1TyN31WQA_S7zx0UpJVRuXHSMAN3F_qJzr5LY7n_KAcSiIfCxnuZP2nlD2-TLsYomADCHEsrFHmCt6_O3Du3KAtH_L5vSD1go1h7V7ea2g1s-v7BqYXo8APnIf0oYP98fqb4Cdhucrxccc1cZRv1V7q2S2FKb_ovwg6aYDG0YRtznBJvw9OhZhAn9oHMDTLBCYRzJjhSYVhI21O2TG693Obmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28948" target="_blank">📅 23:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28947">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=oo8zUfrhxQ2bzjMLlAWK5LEsfLP5tWexcrvgto3u821rHFIS_P-WI0j7nyRWPc1YdAHkvSkmXNom_HgxRNN7Bk4OmpSeslQ31wdzOTtH1xVR266o5iGONufOMZGqA0n9ihdn8362V56Pu2KUgpIXdHSuQIkCAhyYS6un6tYwi_qjkmvAFPh4mQauuMH1uUsW38Pdq3shN7JFsDfgECdDwfB7Jp_qWRFQv_Mhg9NedfCNtpebN38Yiu7eRjkK5SMosaGfevan1gFzKzTkU2xBrXI0Nxze6tz7hHZL7wDvMsnt333e3Xn6mymgB3drYsjkZTWdoWWI5WgZ3SaKbG1W3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=oo8zUfrhxQ2bzjMLlAWK5LEsfLP5tWexcrvgto3u821rHFIS_P-WI0j7nyRWPc1YdAHkvSkmXNom_HgxRNN7Bk4OmpSeslQ31wdzOTtH1xVR266o5iGONufOMZGqA0n9ihdn8362V56Pu2KUgpIXdHSuQIkCAhyYS6un6tYwi_qjkmvAFPh4mQauuMH1uUsW38Pdq3shN7JFsDfgECdDwfB7Jp_qWRFQv_Mhg9NedfCNtpebN38Yiu7eRjkK5SMosaGfevan1gFzKzTkU2xBrXI0Nxze6tz7hHZL7wDvMsnt333e3Xn6mymgB3drYsjkZTWdoWWI5WgZ3SaKbG1W3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این کل‌ کل بامزه نقی و ارسطو دو بازیگر پایتخت با عادل فردوسی‌پور در برنامه نود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28947" target="_blank">📅 23:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28946">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3A3jra7XWZGMaZhEiwVw76t4RvE7iYvtVzdBoSw0gnyEEBknkgaN1lAF-wakMpsK1M2LnhatOY1TE6p1MEJ5NunC_E69NyXO4THfvUa8uC3U_fsMZSYaLY8V2QryV6JTVjPAngyd9gZ7Zkio8R4VxOXtEMps8NgWGYllU5h_pHI1xZO65OZlw0R4szclxCSsCkrFK10KHZ1e7M1QOAa8fUnY37Z0_vtZAOMcMd1bGqDrdt4KVpkU4KpLC0aK27mxQiZgOMefOm0jQ2Wx4bASVWInwy3z7ZOuajui7HkDvhsybfM309RnDtCniJcwIrQJNPd4teBXfdjRGbPooYhZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28946" target="_blank">📅 22:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28944">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T04yBTL7qAAEJe1HuSKhUiDtuCdHe3ip6XspYLa2-4NFMNhrylYTZm_YxGFX7EQgRxK_RdgzaPY10eTvqJ0RSIGkhst-D9J56fDIZm-SY_OT2BJfolVWAB_HtBwvM4NN4CYUNZtbbfWJUBfFyICsaRVRlzDcANGPg73yiZMNKqcbNMC0aCtbxZXQ7psapzwQJcxMZbg1vPFtjWy4zZUuW_pRtT7vTRgNeOWSieAhRvu-cJT_N9QM1BFYnvFouLG8qZ4-2Q3CUpx80vG7WjrmtHls0AR-HeFvnADKw7bo2K_9ChPYbZmvWZfcf0099kl14HmbIyf2zARpCQvqRgZ8Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBV-N0f3Pm6d5Du6T47wT9RtL_R9O8_OfQb6jGehDByRGuNNZYFowMt6GQsA83r1B80rXXlCM1Fb-P9hK3XSQv4j5ujpPA9oGI8BKhM4zJXlzStB7d4baJLPgbPfTEPx9KO2FsTXJmD04rP9rra6xSobAVocfd4luy4ilQ8DfdQVJDUSSLJ3EThQidSUmMAk6RFIjDtJOnqfL2np7KP4cyQ5GAVxXz453mas7f-IWKn64aK9U4oFTR2WHeK-TSpjsVeCg-hknPRoQQIBV6i78vcfxJodEViJOC9Q4x4bri__xtKumxtj0NoJvzqZ_1nZ6YBqc88CT0kSQxZzbnUMPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28944" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28943">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmw9UkoEbRg2UDxFR33zVRMBDkXiS82x3dUJlbd4UQCQGLY42jlL44kLtYwLx5bdvaZJqPuvO3bFzjSShZm0rssTAvQ3mCPb-fJ-QF2csT6nFH4I8IvYGNMsdwJfsEvF2VeIu6x11RJi5DbzJAnazF97luSGEFkuIsQitGJKRsl9QiQxYnMhcU-TnEzj_awIaYOqPQT9lZU53ggA5tgirD8OkjAbH6j5_PJHe8TklRpzZlEl_ZyxteA4p3kcoEev7CCmi2pDbuHvpuUe_dmkvxpWsz7ErrQ-DU3tHr55civwAGV5mW9D5_sMvYho2qt4lYoCvz8lilZ1Uf6EVa5n5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28943" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28942">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3j5uJCiRvYvcC1FmUoHB2h_ccls18hwocMkYcZeMV-ZX7pceZyaUITTfXHTHoQmBDre6PNpWwcQ6T3qJbtGce28Ud-VuXt0oKPJ6yutk2ObO_P_7qKJieDkFoh97HusFMxI55XxCfP5MfeVMtUkJKh_WC0v05unkuz65uTmFCLd9fBkDdAxe1spAZ7sajBTgwzNWCbvHS7l7n57Aa5IfwTb5uyOUZjEbMpOQ2egDAZhZQkTT1fQlGTRemH0-SiiCvmNR2U_D7vAau5m2b0PHWveosxFqi5XFw_pqnNZvql88syYcG7HkrCGJ20hItG6tFVUDo7JnD3HMGrHtxyHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی دوهفته پیش پرشیانا؛ اعلام رسمی کمیته انضباطی فدراسیون فوتبال در خصوص تبرئه شدن استقلال و یاسر آسانی در پرونده شکایت مس شهر بابک و سپاهان.
‼️
دادگاهCASهم از هرباشگاه 100 هزار دلار میگیره آخر سر هم بهشون پاسخ منفی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28942" target="_blank">📅 22:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28941">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=FCqMydoWlAWdH2PGuEInYleRX_CrCPmTH-r0feoDDLx7rIYFUytcP2ocTzz9xg_r2cbiznZL6s2WTXSy2QX3eULmVFlpKNqKCN5DhmSH9M3gDAZscXGE0RNAT9k4ZM2cLorm7vqGhHSxjIooQrtW4mITR5Nl_iuriyFEJb0yU104eUgF1_ppHeZgMkJNlQNVO98R-vq1MsavDUJzTV_wJAEaSVvyVVAE4ynhGvc8-70spr4-QoXqDD2sXizFpZDAKlWgHx3MzTvCy7xPET6hLcm4ujuYZhy7Jxz3lBFjocXA0FX6Knjzkv01zhYo1U6_574RFvZe9imqlccemjyOrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=FCqMydoWlAWdH2PGuEInYleRX_CrCPmTH-r0feoDDLx7rIYFUytcP2ocTzz9xg_r2cbiznZL6s2WTXSy2QX3eULmVFlpKNqKCN5DhmSH9M3gDAZscXGE0RNAT9k4ZM2cLorm7vqGhHSxjIooQrtW4mITR5Nl_iuriyFEJb0yU104eUgF1_ppHeZgMkJNlQNVO98R-vq1MsavDUJzTV_wJAEaSVvyVVAE4ynhGvc8-70spr4-QoXqDD2sXizFpZDAKlWgHx3MzTvCy7xPET6hLcm4ujuYZhy7Jxz3lBFjocXA0FX6Knjzkv01zhYo1U6_574RFvZe9imqlccemjyOrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28941" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28940">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">📹
خلاصه‌دیدار جذاب دوتیم استقلال و پرسپولیس در هفته پنجم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28940" target="_blank">📅 21:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28939">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ieJ0odj5hQhUuz88xc2aozSz0x6U55_cU_kKlEWTyWphx2RLAw-4YY28t7IEk8Q9E3VOr2gM7gPyEnNfi7fyh-ShfvD3yh6Xa-j98-B1NPJ-2uUK4gwPBU-W9RLm-kjj08wOwyx06qPIwY3sOReAptg6KKVINm3wj5YnHRYYgD_PhifzF1mrwq6xB8bA9YPv3MI4YSPPwOh9vOC0F10HcEnsfGPf1dLx-9Z3BWfn1aOZXf2Yy18YQ0g0-ejoYzkhKu0QgUSUjJ1BxkMNvncuUBMgIXNWTFyVSi0F1EvEOFl-jE2R3g5TPZH7BF_K6gjxHOXi-y40SEYZqjTCrs3-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28939" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28938">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot2IZOgcyszO44UqInYNIQNhC7qDmbBGHF5vWwgbHae5KNJSnj8LKpTy0k5FFXJZP_fBgHKfSrc9zwm-vej4_w329TFc7CnqBfbjYCPVAAtKPOlu6JLfAF03fyyUWHNF5VOAyxPOPFyXgeYz5GSKcV7iYEXww1olXCrLdYh22uYQ5drVWlA5cp_1pzn00DsP6h4ToxHA-K2ul_YwJN19JC80R23UHzYLVn6J4jPR-Is95zMrOnb_OrBJtjkf2QV-qsHvBCDz5L-_es_3ul2bHbDR3LvCO2Txn9WAYd3ceAF4XLmAopXbS3d_Oi907pqJQvXOtiQEhBMWgep1mOPspg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ستاره آلبانیایی بازی رو مساوی کرد؛ گل اول استقلال به‌پرسپولیس‌توسط‌یاسر آسانی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28938" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28937">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sUnfniIDwyPybCFvq86eR4d5R-xoTgme58Kjo4GOnaLDmfWQearBt4xOip1DkBMpXO_GDSA5BO-1mcODTRXSi4T6f3xTz9M6FLiymRR2V_1ooFokmJId8ub6-JoZMYw4u_rYYKims5HYu7nhuk--8OEe1IJCSJb7DKwwm638ZG2VAiRk1x1PS4a-LcrIFcsDDZ0bzaejSR0eHARx94R1Y8XsCZ5C1uyhHbF_1qyqPsumo9fV6oLWkISa4Rq4phPVRNekQ484ygcE8FCmCmwWf4PiDhSJJtrbxy-Fy_bGMEbq4xt9hffL-TTiAWVXQT-ADl_MmWLVChotBzmipSnkzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sUnfniIDwyPybCFvq86eR4d5R-xoTgme58Kjo4GOnaLDmfWQearBt4xOip1DkBMpXO_GDSA5BO-1mcODTRXSi4T6f3xTz9M6FLiymRR2V_1ooFokmJId8ub6-JoZMYw4u_rYYKims5HYu7nhuk--8OEe1IJCSJb7DKwwm638ZG2VAiRk1x1PS4a-LcrIFcsDDZ0bzaejSR0eHARx94R1Y8XsCZ5C1uyhHbF_1qyqPsumo9fV6oLWkISa4Rq4phPVRNekQ484ygcE8FCmCmwWf4PiDhSJJtrbxy-Fy_bGMEbq4xt9hffL-TTiAWVXQT-ADl_MmWLVChotBzmipSnkzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دروازه آبی‌ها بعد چهار بازی باز شد؛ گل اول پرسپولیس به استقلال توسط محبی در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28937" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28936">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=T56r-91lrWMd8JnI4LbN8muaehT-pXHkoyM5J4QLHgckAdaGAVR_CeACQaOKLKOe6ArPSg-fc-7TJBoZcm6-2HOtOSUD2RFckh3LsPH6bkfNc2xtMhZH6JJ-V6NHY_7Ix9jwvSrLoEk38cIblgen6-f9VcWtvtoPQGGZQHksuIS7zNNUNK8GgKBZ1gi09LR6OVkjDh87qVTwEXIfPWHUjmR93JtpN8xW0dWTZzUgfv4SVfQFqJL-rehAFfUT7880H0jvzxBwCIH9BpPi_yeQ2ZypiRSGXXSJapAcMDuluebQh7uq6kGT8did2mz84a7UTiZHK0-B62cir4KQ6pVnmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=T56r-91lrWMd8JnI4LbN8muaehT-pXHkoyM5J4QLHgckAdaGAVR_CeACQaOKLKOe6ArPSg-fc-7TJBoZcm6-2HOtOSUD2RFckh3LsPH6bkfNc2xtMhZH6JJ-V6NHY_7Ix9jwvSrLoEk38cIblgen6-f9VcWtvtoPQGGZQHksuIS7zNNUNK8GgKBZ1gi09LR6OVkjDh87qVTwEXIfPWHUjmR93JtpN8xW0dWTZzUgfv4SVfQFqJL-rehAFfUT7880H0jvzxBwCIH9BpPi_yeQ2ZypiRSGXXSJapAcMDuluebQh7uq6kGT8did2mz84a7UTiZHK0-B62cir4KQ6pVnmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28936" target="_blank">📅 20:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28935">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=cB5Pfho3J3J-_N-fTUsPM1F51s7YY5XjP20hE1FIjcnvk2dmz7QGrR2taPybxvgwLMABPfcviOjjvG2QAhtGN0njfk4YH_XL2ggPpBNmccuxyrCHhA_4Au1d-qET8GxwnXWbBY4rdqDXwQK99m-byCy5ZX2Co_rx8HEfk9rDIgSzCDKRpc7YLulqWsjuLVpEq3YQUpBGqXOqfOuR0KuVoiD765-Tan59P_TNLhTeKC_3Oc75BXc-ytbxg3pgHbcr-pdwuStDPvoZOGBY0ue47K2S-R5S1ankHIHe_wXlaxDgzxKFdMHlywHu-5gGKe7RP52EPJ_55oVhATmZe6NiPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=cB5Pfho3J3J-_N-fTUsPM1F51s7YY5XjP20hE1FIjcnvk2dmz7QGrR2taPybxvgwLMABPfcviOjjvG2QAhtGN0njfk4YH_XL2ggPpBNmccuxyrCHhA_4Au1d-qET8GxwnXWbBY4rdqDXwQK99m-byCy5ZX2Co_rx8HEfk9rDIgSzCDKRpc7YLulqWsjuLVpEq3YQUpBGqXOqfOuR0KuVoiD765-Tan59P_TNLhTeKC_3Oc75BXc-ytbxg3pgHbcr-pdwuStDPvoZOGBY0ue47K2S-R5S1ankHIHe_wXlaxDgzxKFdMHlywHu-5gGKe7RP52EPJ_55oVhATmZe6NiPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشید اسماعیلی هافبک تهاجمی سابق استقلال با این‌گل دیدنی‌اش در دقیقه 90+8 سه امتیاز ارزشمند رو برای ذوب‌آهنی‌ها دربازی با پیکان به ارمغان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28935" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28934">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8WLb4kApn_4X9ys6FQuVI7pvkC_5HZzMy8tkjJsibqhF7LCTkQmmgnqXY_ck3vU_dRKOXMtqZUFShq60_XSh6eEKQP7OiBqVZvXMBmb0OrvGD5CNxXBSB7V8aVPbWA_H-NF8AgFsFGYIqhXVy8ZoUJua28pfzIAiWqZ_CW7P8VZAmrZ4_O6SJoMOR-DPf6g_iRXCTmNf_3SbP57FBzCxCD4muR4Nx2HQS4mEWNlyvNumqhbuSu9czTaaK9go2LaIS4FbArAleQVva96RXNM2FUAnd-mVfnxSRVA2SYlQt2WGKrhMvlmXl0dnVBbHGPOIkK_mKvXQD6-mrfg6x0KFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28934" target="_blank">📅 20:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28933">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX9iJ5pihwglsNwVM9i9GbMkPI-SC_u126C2dMR55gwB00E5h0wCtGC81hUMeHz5Rm5zLvEVbH02lUD2x5x5h-ueuWIQDKdGNl-tA0jzjm6TqxyC6HyQ-j6fB07-2zwGAyJKVa-E53d2KJJ7afauGo8MpCZNxNIEfE_m6IV6Xg79ndaohz_jh5mAhi2NjjJLEZ90aFrBwsPulUuqb6ZbFStVlwLVMy3ycJaaekyLEzK3sM6TK_MmKJbdXQky4Mzs3shtHA-muDXLV_NQ8KzxFbH7J4MOTyB_n1hOLIulICgcXYwdBQ3Tt5EKT5qa5vKI0tqmva_OltYWf-Om_E1mqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28933" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28932">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elQBjKXT3Sd7F1sI6N-VmSUfCikr9Gk5qFyGZNGqr88dafYiu-_Er8GBeFMojH-5X5Su2ZZJBksgfvKgsqIlb0-ryKVp0N5GkjPXklzGJCy5vq_8bgOj9KbjYOa_bA3CQyPmdhun8-DrKCLnnXMFEw50kXav3asvl5d6XSSt5_JloyNhZXqBPQgrSoiYHpZXrCzeSYvyk8nW3pjqmXhenFRnHLBV9-ClPuFJBrfrUZsgszGJacCXihauWKnQeBKds9KfJKKPR-ml9M_4GwYcrXY7-tK5SU7ysWfU7xiXzsZD94pA5cgTa655q7YxmREAb7ultZBoEsAiVYrafqEvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/28932" target="_blank">📅 19:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28931">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=erl09xK2SfGdMO2n95T9R-wuzv58Lz6CoSvqXAa7gT5Edau3VtsMiTLDxruowqn-aOCrNjniXQNQzdR0iYxW346HbYW7kkPbR9u9zGeGdXocxJbvW0wmbLsyJyHuSKsfk3uZrb9Q4Jbc1grNJM5U1tJ0A2U_mAt_LNh0kzG0st83UfyRA2rE5Nr1bbSUIhIosPmfSrMzdyVhvATrqZmsxJmy2lByJLGqAkxIiXRFB3mpcDRRY8VbylrX88fHR6u6WDiJWeyk74qYk6QbYDhKpiaK1WrhJmgmMxGWdmWpIGoBqLCAnM5l6zpyhc-rahZ6xOFXAr5DNxWcvXK5zhixVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=erl09xK2SfGdMO2n95T9R-wuzv58Lz6CoSvqXAa7gT5Edau3VtsMiTLDxruowqn-aOCrNjniXQNQzdR0iYxW346HbYW7kkPbR9u9zGeGdXocxJbvW0wmbLsyJyHuSKsfk3uZrb9Q4Jbc1grNJM5U1tJ0A2U_mAt_LNh0kzG0st83UfyRA2rE5Nr1bbSUIhIosPmfSrMzdyVhvATrqZmsxJmy2lByJLGqAkxIiXRFB3mpcDRRY8VbylrX88fHR6u6WDiJWeyk74qYk6QbYDhKpiaK1WrhJmgmMxGWdmWpIGoBqLCAnM5l6zpyhc-rahZ6xOFXAr5DNxWcvXK5zhixVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره سیروس دین محمدی از بیخوابی در شب قبل دربی و گرفتگی عضله در دقایق ابتدایی دربی. ماساژ درمانی؛ جان هرکی دوست داری ول کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28931" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28930">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQtxQx3Ng0zvXaQkDQZ_JCd6Ldx_BYewPzbcC-T2OG6fVM9n4rgEwE6Al837wJoqM9SoWnGb_mZ7Xk236-oVi5u8yAyPAlz2ejdu5aBvtPfOt6RBfrIwHtpX_0RIliI8FDkoW8xzLuYzz9LNANb3mD3_d4QJME7LCzxpS1Sibus4-JoqJ5ms5eeSL9J6HBa5vgXxJkcraPAv9VLwuOtSZq-wJ9n6RwLHDNtjRUhPULl0qITMgfNmjIAB0d_c0IBLLvMvKIIAFfRg6QSQzqqSTG0bA26yYPats8X5JaSJVGhwlsGmc0dKEWSlc_-rjk-xu2MXihMJnq1OG8Cb71NeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست کامل بازیکنان اصلی و ذخیره دو تیم پرسپولیس
🆚
استقلال در هفته پنجم لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28930" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28928">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeFNyc-vqQW1qCUv_BdaLobcEgZ8KSZt9wYQpAB6mJMzMcLa1s1HaRoM4kD75fF3FoUCSbUfrKuxc9l_nDk8cabOYiHYx_3ek_CyVk1z0Y68xLI4uYMrbRLc5xDYSCt4EpqPCHV5HO9V_4E0Bzx3fKlRlD-jOePIbY1eLsBIoHe2v2WHpbSgJLyQpryya3NM1lSsjulBcElHxipG5Pch4WFu6mHvdZ58A4lLIaBa-HKDswdAmShgGmwFAvf_fI6Xbb5r3w2OEeYlwiuD4A49g7xEBdnhbBu6wZyfH5WtyE3HeEKOGyGC5BNwvLzJzl2BQplCXzwGszTAM8KMsXkaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28928" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28926">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N5rAKYvC6tXlrp-APFd5u3wmuW4IymVUEM3zXurucKZW9m_Q-tnmDdnLMzcno8-fBvWXlKZs7_8vs_DnAHVN7XtLCaSAZYRPUBUfwgYm7PTcC6kpH5ek-LE40-djFmHm5MGq0pqm7CWb288eJZeNv0t3RZcsMeFn_EyYt7c1WaU_ghkglHszhQJs_8CEyfBZff0uuzdZXRpnHqKRJ_ea-3DzEWMwsGvGcA9IkgWAOmB90cYfadae0A6zrtH_DI4CPYr6QYEf1SmMmxXGnZLNgq10xlTqHtYhpSq3NjNj_w5v4zTo_MdH2PwZHCRRlLk7NtLnBaim3sHgQhTILGP3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qRD-QfXBnipkBnoPK3OGOkGXohM_LpMsk-aFpVm08ySLkUFKs91ut9cYTtYXFEiB5qdBK6qvSBpmrsanJnUb0KusxkxqKD9_jQRp2KjzBRYSP2CjIwG6y-kJSA9zGKjcTMANvpBcniFDy8wtSb_xzagKLK3D0M2cqyjHieSSTXYn0cfNVQKD3o8cEZZPulD9LGLDAghxS-B3bTLBsUSdSnZAscWo9ppEUQBXZ56rVRNI7sxcxcYl_PG3TzyIshXmmVvDWYFkRTU0eMizWXlT6Hv-Vt7H5ZhCH1JI91VG8LS9bOuR2XH8KXpH3azCzlBF2gK5pbLbPtSFV1hWX2uBnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/28926" target="_blank">📅 18:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28925">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EveOYUpQPyCm99rcpda1l_axFz5iGX8llKYTroDYgCji74Z02gb2ryHUHFMkDeRj9aQO8_EQfMqs0fGpzlH_CzVTXmA1tEVJqNb4busXP56sUcOkJOBDSm9BEpPMDE5xq7P2vP3bMxaqX28fQn4BWi6HqLXovNIgs7vVMd7K6VqdC11F5-Q9b29v0v8Ydp-kAn7Oc77yr7z71eREZaXtQ-mtGehw6e3NHDmd3ejrTFYbKHxDoOoUV-xOFehEoGOdMKh7Aq4o1ffuqZHGrOD6YliB8IqyzwqyU-QGdqo7OAHTg1EdVfOqnNiFQ_PRUBAqWQVlRRbOMpYR585XKYwhFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر لائوتارو مارتینز: لائوتارو در آستانه پیوستن به بارسا قرار داشت اما اتفاقی در پشت پرده رخ داد که باعث شد این انتقال منتفی بشه و باشگاه بارسلونا با گابریل ژسوس قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/28925" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28924">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ojp1kz0wFfwTzngpYeJn7djWLWcMluSWmZNaz_r7Fk7w7JanuyTBeVHxj5OUsX4qf-08eezfitui0tPIPjvrN2FsbXl7oDPjbOg9p9nzuAWyjE-lrpZVRLqcdRBm-jwt2cnKthy8fqD2Rpx68ttOndtzeZ6rTZ6E3_s8itKhogOgsbXHV-19omD2o-INIr62-ohwdodleq0yBzvAmbetKnQ-WtMeB9uVcsDs0--piVw7V238HNHUKcgkxzg1Q-geD0pHOoe6AZ6QuOeaYV_L1KG0gkPMUjCWRBey5d4ghg7PUKqiZKWcrC66I0aIN76EXrvbasrMRuw1tLbwXGL2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/28924" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28923">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUKgizRudzA3rSDwiaStWRWn0NJ9ojBCvwCD-J6fEBpJENuUYdaq7EPEuX8RZwCIqAsAvNorTXa9_jYeaCw8pmWG741iRRwpDSgFXOt_WWLIg1uaZwVvapYDid5seBemPimOm1JndcT6B-zVSrYEnT4VLhObJUSyPuckeiWfb-rJ-29a-lNsYPXU7mrErRJLNbyEyYDMJckWTEExTdwDDW_SExKr_Dq6rsAVhpCusXRROquf_FAxmLJlGjUA44QyrGE_LkHEEm0OTY5DqLBk5GQG-vGK2FacHs5cGL_fpGa3juvQ4MOYiQIP_AhaCZVkjOxRp463EVS9X3ueCyN2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
شماتیکی دیگر از ترکیب احتمالی استقلال و پرسپولیس برای دیدار حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28923" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28922">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-gwWgu2uC9jA7JkzvPFYmxsNODhu1MKc_11COQPHuXdDJiAGXwbd0yE3eYiS7QX5PDVIpSZ1bCpT4YRnwhjmWt2lGVAxk066APgFQJSLuJgw22ZTeIvLDgY0GpAY3KJuG3UkdSY_uQUU1YCE7TpJX1bjc7zAgez-6Wbmlr_usqccWa5ox7pdROJvM0XztnxXh399AM8cdb4PHXkuL-WXpvxjjtxhi7ogPRB0LzSu1uaZSfz8xCUNGCgfjtVHpulS7srzPpXSXRNC8qKFPZigKhlN2BOzPt6bwZYdkmld4BJrhVryiK9EDmSw7L__RILSSKASPsllhdGv4UoZc_ejA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/28922" target="_blank">📅 18:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28921">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=GKeG7LuS05apfeuzodJkfLYYJ-eipJ6FLIl-8zU_c01gntLVXFEO1QkcZjhzdgwwS5pPtJtht21rguFThI1MtbbnQw6vzOQRjkGOvimf_T5p74S-KurLUEatCahSr2HpeNu3CSSKEF8HoZ9zlSgI1TRUsBrDcGzL_xzIVEUHyOdc-dhZO7ZFf-OOTpJqx3RtfxjoZnl6RwDXlZTjOAoCT4dwmyekleDdD18Bj0JlaZszYA5sqlB0Tz-GsCerlpmljl5SS-YhmX2-KligsDrR6LLov_7tdg1xeNr1urLb-wk67p8_Qaa6w0QbX0qeYm1knq7AUdxZKq8LIKnkG52uiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=GKeG7LuS05apfeuzodJkfLYYJ-eipJ6FLIl-8zU_c01gntLVXFEO1QkcZjhzdgwwS5pPtJtht21rguFThI1MtbbnQw6vzOQRjkGOvimf_T5p74S-KurLUEatCahSr2HpeNu3CSSKEF8HoZ9zlSgI1TRUsBrDcGzL_xzIVEUHyOdc-dhZO7ZFf-OOTpJqx3RtfxjoZnl6RwDXlZTjOAoCT4dwmyekleDdD18Bj0JlaZszYA5sqlB0Tz-GsCerlpmljl5SS-YhmX2-KligsDrR6LLov_7tdg1xeNr1urLb-wk67p8_Qaa6w0QbX0qeYm1knq7AUdxZKq8LIKnkG52uiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
کری جالب و دوستانه بانوان دو تیم استقلال و پرسپولیس در فاصله دو ساعت تا شروع مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28921" target="_blank">📅 17:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28920">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BABb_KkFz94CbLyeN9QTPXzX7U0jSdtPK05ZVWSQcJ197mi80_ey16hpGX1VfpVcKpcXWo_nM7lv0kyJhJ8gR6oVK7s_Osa5H8r815RJ2sn_1j78AjluwK10_jsEuhthwWq52uLbRkjE7FojeoHGEj8drvcFhYb808YGj58xzRYcKebtuJ-daAUBR-Hj1XsNTZc2n306D2op7X9ytBLAMkcAzkSjsr6ZuxCK1pSFFadO1pM8XzdZ-LarU8bZ5IMc7wGC_vajym8EuSysrnpAcCBiiubjIQsJNM1HfQx6EatGUwEm99RcT0EZ_DUPFhC_8YkyEwgl2LgVtK5hO1sHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
چهار دربی‌جنجالی دوتیم استقلال و پرسپولیس در تاریخ این تقابل‌ها که نا تموم به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28920" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28919">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isDRubeeGg0yAqzu5cRDap6A5P3beHCTcdDIT2JILGbY1Q3AIiGwDbB-3IKFx0YdHT3xAB0QInW6sedgaa8yTjxlBSxEJ6znhLezd4nZDnLN6cWR4nB-hpdSWoLSSeWK7LVy4GFDseVuxRZxfBbMsuraqh3BsseL03cOJJ0Rfyp3NrUr9OyajQQ2cpeGo7k-nBVt-pQqfaEcohXjqxsCPE0mGBfb9hF9yaXlD0seTRYstNDuYeeVLiaj_dKQN9Cyj_PI4lJS82zHv7Jb2-lVbZgjlIELKdJL4wUy_m3cCG5DS4dIa3DFcEalGMa0DEr-c5y3dWhx-R0B2xfdImxa3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد پیام نیازمند و حبیب فر عباسی دو گلر سرخابی ها در تقابل‌های خود با این دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28919" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28918">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvxOg1nlro8IYgDo_er52IteM5_hZyNToAF0K0DWGyqwCMRKcS9d3JXW1vdreVJmLxpOotjT7Ys45veeINKAdZd5hEn72jS5Ti7iGt11K7ZZYD1b43tN00ATHj80CnRaz1qa_kkXPwWpxxQ2-Ph2YfQNTKI1Wv7I67qxQ5ccPU365PeUMOKd_vOmGer_pmuNSo5bt5L7og6UrEIlvGAkOrQQn8rXdWrjvusBTpCZCgka1jECKFD5GVUSqviCwqOiFMTkqnGxSCrS5wR_spkuEdECjDRzmGpQCkdZP7tzFPOaHIUP1jxHOjX9EvXDtb9IMOZ941S0KCHbZ_vmFAVb3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28918" target="_blank">📅 16:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28917">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mh4HKVEYwDbMGzOMiH93m6Bk5iDMc3xsSuSaF6dxnk2CzZqnoGdn0GPVGchqb8FqEMTCAyTsAtf3Rva7gLcMhNtMr_nQx44X5fcDIemCLB0__2IWUy792x9urT4ZPbIkbUnrMy50QOuSkHu2_qZF5hGx4Ivf4eVYbws6K8zWA4XbCmZDDzuqk7AAB7hNxkYVuuErhosS5P2rQ4UTzkQlYaFCyqR30EeaIiMKhDTayLihUdZup1S3BQ4xk4vdigEZPAO0xBaPqqRqwA8mOt2Ho4eF52v--MVtX8qJoCL1VPmnYg5wpmVjUV8iqdPq7JvnMwRvpwXr7P0OgKT9ybrQfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی بیندازیم به عملکرد تارتار و سهراب بختیاری‌ زاده در تقابل های خود با استقلال و پرسپولیس به مناسبت بازی حساس امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/28917" target="_blank">📅 16:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28916">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjjTUugExd9l4_ZfW0w11KqMaV1MJBEZjJYbtwYbBLNV40LWz-VEU6DUKFxmh3LkN8CUBT9iYy8aXhWPczeIStt6xyrUmE-jCCx4EZxYCKoQtkteHvex01Kq82SEyxMRCoyMuXy2FAn_COBlpJdPs9nX3hYtEjqR7W-gdT8hi9iDEvKbrkNCCdZBA9RDR-H4svGnhXKfw8_LcAB6lagtw1tItXr-44a-xHvVWmpkqj1h8f7qv0KiSZWitloOAJYzTYKMeOiHTkB89wBtANZt9wtFM_a6UkjhXMixdE9MNLckOQNfF0kgq9HMk24du6Ki4Ghvg_GCRt2zOYInzDMfHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
درآمد فوق العاده 200 میلیون یورویی باشگاه رئال مادرید درپنجره‌نقل‌وانتقالات تابستانی امسال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28916" target="_blank">📅 16:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28915">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOPHYq-fXNeZjKXXVPzdJ2XvTAjG6cprTIAPDo8F-R1m-WZiZVeRMJWpFz9zrKRog6F-4jC2nvaiaPcJa0iUi4Tunthc4vCk6ITx7AMlnwEJSJOEVFEvsiD3rUKN-hdDZ1dGPAwfV082Y5xNn43TFfFmFHuft9em5hLMgWDKiEeG8m-XW6PM4P5kKkJdJwg6n7ICti8r9uphZCKFRQ6f6752WaLrYBIoQkmTJHxWL-sM4kd93MCx6cvSkEhXguJBQdKhvnLPDLFnXeLqloWoHp9a6oT_gBbnIDz6L9_HrSH29hm63SwpV9XcECHW8zSHMvT4llvX-GkxKVcde9dkpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیتسو موسیمانه سرمربی سابق آبی‌ها رسما سرمربی تیم ملی آفریقای جنوبی شد. پاکو خمز سرمربی اسپانیایی‌سابق‌تراکتور با عقد قراردادی نیز سرمربی باشگاه مراکشی رجا کازابلانکا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28915" target="_blank">📅 15:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28913">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v1b1TV5yC4uL_nWy9VFdvsyHNoOriPRjC_yTDpG9bTH06Op__IVtScHEFfsPgW2hAY9TGPrZHaE175OdV26wpS3myRmh4yOIELc-9wlSWnaLZ7tSbPk8kHlNlNuBGtB876EDOPiEyb1t5FBi_Yr3KUX6tbSzPbzgYRfYtre6vibUuiW623saLb6CmoZ3H1TlfuU_Gz32d4V0fLnveqia945pBXaBiEESd6gkLTHTtjQz7xYqZk7flymBoOwHvB2JiMqAL40-QaCvi0G2R6Qa-Ypp27Ddf9E0rhEOSV3vhc8no4gdCvU3exBbi2nQTG4ipyvgi0JtHy6bxLNo4mhsCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D3473RoUpDgI5qRuIKmp9A95WT6Z7GEse0oFClKnzvGtzOCZXRtfT_lhEe61VGnwS-wIW4BOn6l0tKLgddSc_3ZN-lkWF6p-5fFRuaPG4qIxUAMrzQopHFjborQdxc3FuFmsVQyd-tz2itAIu_WHfsbNVxmv2FebcIxckmYWobpEqgWV9TqZcPSFHjr5nwKAc9FsRUKE-NY1hzs4sOJCTEJlLnQqVqwnxeFXc2xxdKo9TXP4IlH9HLHSNkcOo4GFoBkqJqC-9huMo0b6PvYMKE0v9qWTAV39N258tyBUM0ciDFBt4y_TGdXqj3DRqfnQvs1vD1V-pdaQejtbZqXAWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28913" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28912">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJZQlVt5RaauRpAr0xWS-xdEYYHIQDC7pqdvkyC9e5xlhz9tWiliN-HDCx2myIFcTYX5FejrczVhlLijViy3qSbsZUR6MQqBkwovxtcFqYgij3U-f1wN1Dce8l9bE_wTmbhPiE74c_dgaKepUsMQXf3RREsHbdbXWLT5D4qU6y3udYmS3klWz8um8qKSu0K7nyIM4hWsTN03n_g99iJ9KyoTq78bzNPgqE8-HfGvOcQP989AbrxYX6bEMfdz8_MBu5uHuCWKWQb2GVF8xymBDbZVsUxIktQw1sVmAvhKI9xr4Quxtrq3sKnSHhOebzuhScyEC6vuDMy9fjlRxJ9mVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28912" target="_blank">📅 14:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28910">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1M8AHpuBpat2DL5IIeqRrll0P6WABZUjIxwoZdFsQ6DdeI6V-C3U1Ht9sALINt5sGP5n-Fb5AJ3LCSpa36HczIYStUMQAZeLgezVvMFg8AfC0fDjsEJJWFmmZZUjKjLwuuhWkID4W9DiYQqPqjcO7i1KfzHzCfWK8MDUReMu6ixoG7-Xl9C4djcMKCKLuI_HrCWjqbQi0KmELt0ivsQkds0YULlOkNdrNMwFHB8fvJ4pauPFsPUMsnyiZMSaS1_YU7J2LPbmhNFZ76gHda1inqY4iA3Yplz2LMyRokjj7CsyzKK9urh5xBZPHxl2HGqLsx8G2085Xmobj5TfGDnSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28910" target="_blank">📅 14:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28909">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=rhLnoh410J8yJHR1bchTMlKBY4eo4Thlbxr2m--xhp0JbUlenu_c2ynzGuHq8m7OSwEf475rDOAQOsTkiLLRidGItiQk6_PCGAjXhYsibUFyOIDUfYJRWwhwIVZ8VJNUGfrJB2GpdKO9Z2MUmiKg7yyslCdRWo5tU_puCXLv2C7BAAtXU_X5eGG-vVUbq0lu0Muf0pleuuf8fq4YkyoPMiaurwOXRCmxQzLs026dUIXfAr-iLEy_RPZElw7__SfR3vIy2FcFDhQybCaOxFDelG8q0KdpaYre2S7-LSPY1_t3h79gr36rJYYGczL4rt7aEBfpGbddTaAgCKiSPbY2hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=rhLnoh410J8yJHR1bchTMlKBY4eo4Thlbxr2m--xhp0JbUlenu_c2ynzGuHq8m7OSwEf475rDOAQOsTkiLLRidGItiQk6_PCGAjXhYsibUFyOIDUfYJRWwhwIVZ8VJNUGfrJB2GpdKO9Z2MUmiKg7yyslCdRWo5tU_puCXLv2C7BAAtXU_X5eGG-vVUbq0lu0Muf0pleuuf8fq4YkyoPMiaurwOXRCmxQzLs026dUIXfAr-iLEy_RPZElw7__SfR3vIy2FcFDhQybCaOxFDelG8q0KdpaYre2S7-LSPY1_t3h79gr36rJYYGczL4rt7aEBfpGbddTaAgCKiSPbY2hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
به بهانه دیدار امروز استقلال
🆚
پرسپولیس یادی کنیم از این سکانس به یاد موندنی سریال نقطه چین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28909" target="_blank">📅 13:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28908">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH72OpkeQm-TFyVJYtOxAenfeUiDJtIsYdOURD45Q5lztc8cWQyl8DKviHPdnZM1rA2AQ6keCeUuAP_MkvhyvpmUsVL1ctpx41WWOcpNpBjjngnd8PVOhEN7Wc6qmvkSMEyw-NDgPbcJrkX19GDuAFdPzYPPO5RAM1XTurRLJuJt_FTxWkBEJyNgYgaqDF29gZVHa0HwheL4_y3OPAURyU070tamds3D7_sK3BoWughHIMPr1KNcovbU1dH1f7sdW_Ou6cpRr39kviHmL8VkibcYhEUNDUBxiyATY8POo-43BONj6oAZV61Qkpzl_DdBGydEQDzY__ClFEpwXsi01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28908" target="_blank">📅 13:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28906">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rnJdx2s7sIT9yDNum7fnCdJ6QHKhKX-P0tA0FrKcdSXnogVchDuSnvhv1AoiBrA-exsEkNJLhfrWgxU8VbwHib6No3f5so-L_87-waKgIhv8MvfhhN1hWUeaXYIdextp7wogQW1QIJXlHrqVCPpgrzz_c-qFArGxCrXRERXmrdlq72JM9A_W6b_caLpwtRv9E-5O2ycY1_gLIgkGGClkTtJ9qy7QGVMugM88i9avkqTk1tq3raBgHi6eid9CGTqUByBiU6wVkWat9Ohu5UKb6aD47xnGrYQBfuq-Dl6wHX4cp5JcoNUupoxIYe4WvGBRWZYtYSbacV1PBGEB5NWPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C4ZUoLV6aBtybN6MVXCDJynk6mrPLXJNQD0ZHUVoNoUjr411J6woQUrOOavyG78QNMBcHAyrj8D8WrWOgLCFEbcET5ww_eVXvajLfmP-SsY3BxLIWDn0DLYoYrQWOc5hMTv3_gNAWL3RN9QuNs_j-Wi_m99I5khcanZ-zwIeO3EvYOjpLVd9MAnyrOvjC5WWARA5FI-iV4H1c-NXwmXrKElEZfxVVaPigJTIUBmM3eMUPudlg0qFC_XvG0DGxTZ4rTzEcgQsLomRmUFTLNv6bMUphWfv8VBx9Labuxdl90y0O_uJdGCSFyhcr5FIr5fOO_DC3aFRy5BJ6wFhmzhUBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28906" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28905">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGkQgSYEKGOxyleNhdHWm9AYldgd_vdPsAHsIJdIxxQqHFEXFmb-3Hjhdsi-SGyRy8617amKvLjMWeZJiYE7EyI-yOImevm2ECe2wn_DZT5AGhAElfIpOkKjTkRN2NeWLJqsab1xr91HQwngWBkIghp-8nn1POHO0F4qaR_xrSq_FdWfAmOxJsOGfhUq5Lyj9bqen3Iw-AkyrU22TTpqBDMpPUuQ2l8alVOsItUp3h7OlH0I6aJ77IT82t1kU36IAr-CRyEAlMrLVYUsjB9cY4MrT93k6TpukC6En5d8ou8eQZ-hN5yAmmL66byKzQyWP1Vi8ggb2qc_nnrW49otOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28905" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28903">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj4No7oLZKaxlSzcmKcFz_MFcxOTE_3cuJ7LzTW-8UQzKmS_X46FI-jV4_jNfnG6Jl3y0hjdSCvJhsk6mW_-MlGnNWz0sxSInqogA_5RnUDhibKTUqjLnAJFQb_pFLPmapVHDjc2D2zCBOCfCDNxXnH-gfU9llHWTNGNlVrwOD2Yb8qw9Zy8xnXZIi0q8oHMtczDGMQjyDQuhtoB4gHla7vviNwIPXC6Z1XzB8k2sTuApCd3UPZK9usa87lX-iZGLq9cfUKJGwNJ3v12RyMz0yDOIQfYdSzYZpEMvzntZmqpl5uL7tj8tTaQfFrJURQmM8e8Qim5dvrrGej0smAhYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از ۶ روز پیش که همتی گفت ارز به اندازه کافی داریم و توبازارمیریزم. ۱۷ هزارتومن رفته روی دلار.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28903" target="_blank">📅 13:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28902">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=tuSLl4yGmcuU8EVw_MVs6hgtWy9d2Eqm_TvN5UlzYrTycnypFHpfY9u3Lb2UqGGMJpXSN4bnyeqjV7KlV7NTy_ITijHLYHdbJjIiqRdwkIJD3XC48jDSCybcPMDMNRecmVftR80EVe4zhqKeWXDgRI2KQijS1nUqjn1dTmQnJfg2U0PqO_TBsFXBsL0GwOb8WmExNnIGbAsPGNyZJQyTzpDtDvIKAQ3VGk5nVEfA4OdNZu9cJ4WCIPAn9JmdPwnBA6hjgi0uqU1zWumlyXMU26AIQ5twvICmUv04hSaGiTjzMUXBPYhHdu0-8rH6Ll086djt-js_fM_CvrPhrnXP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=tuSLl4yGmcuU8EVw_MVs6hgtWy9d2Eqm_TvN5UlzYrTycnypFHpfY9u3Lb2UqGGMJpXSN4bnyeqjV7KlV7NTy_ITijHLYHdbJjIiqRdwkIJD3XC48jDSCybcPMDMNRecmVftR80EVe4zhqKeWXDgRI2KQijS1nUqjn1dTmQnJfg2U0PqO_TBsFXBsL0GwOb8WmExNnIGbAsPGNyZJQyTzpDtDvIKAQ3VGk5nVEfA4OdNZu9cJ4WCIPAn9JmdPwnBA6hjgi0uqU1zWumlyXMU26AIQ5twvICmUv04hSaGiTjzMUXBPYhHdu0-8rH6Ll086djt-js_fM_CvrPhrnXP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28902" target="_blank">📅 12:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28901">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JsepHU-SNh7JUC2BKzruY5-hNB6Xg9EE1j3CKKXQ5wVUMEZITlp8Gv2XRn9qaY6XAdBu_fPQpBLI_YGbfefVPHRQT-Y1LcOZ-jCk1u_Q4RTHzsvMU_iEBrI1kHSQ830yaZ3QSuOnYLg7lG_D2tTjU9mHHyAyAs_uzU4zcOMaN05J7X-5ZkeLWJOZpbGEnd1_erC6zZhhlxW_S9oaHM48Rr5P5ATXCA-1NSW-nXE6EkS3Kd_-51UQ2Obx89GK_jM8YePO2xbileibubvQae4e_NUSHYDSKypQoLHs_cqTnLy3lVeXqN2PBGecXRMBB9-H4JMn1q5jRau_WCnVCWIkQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28901" target="_blank">📅 12:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28900">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h53x0oFZ1nszx7aVzwR2Kx4RcoHK0u9TgfYK3X0d-ZxFvjlHDCrGvwL_ky-m30PirO2suvCC949LA_kOaA1mgScS1uZETXi2K2YSWbLTARWnYU_3B9DFl8lGFJlob1A3NPctFwfqvQV6vrj3gsD8pIvpjB2Bt-ESM2S278Aq6Hp01piBv4p2qmLlETpErMkx82Hjtau6-j825NwQDnij4TGzhNtV7ZnixNmdfmpRL-LP1viP3wZo3-PcrSlaV5b7YhZUq02LxVCPDTzovZFxWO5EHgtCdF6TPqCWAGh9To37lUT49P2IckUc21nqFiNsSvGb_g3NhCrkc1YKejGgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌گرانقیمت‌ترین‌بازیکنان‌لیگ عراق اعلام شد که شرزود تمیروف مهاجم ازبکی‌سابق پرسپولیس با دریافت سالانه 1.2 میلیون یورو به گرانقیمت ترین بازیکن حال حاضر لیگ برتر عراق تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28900" target="_blank">📅 11:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28898">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpAQ5Y9UKFZ1mfl6Kbu0UZiOUZxCoThJb5epDIQihIP67f-0jIyGXrGY9HS6ahuzj0Tt2WyOxQ97Jy_PBAb0fhKwat0KZlgmG0tJb3YtZrLeNQzuZxl7TwS9VEVQA8oTTiltqQegeaVop3SnmX9W1_c62tilK1FooBgaPHW7oiaueuMSVyH8KHLgcR-cphtvPzzrgG-wXXXz8bbORlsO-zp1a_5HNaaJyuqzq2lOS-0e0Ua97deX04YKVlqrM1ve1r0v46ELhV7vaR_fUhOYEIU3oOsLQ4v2IMO7dOTzSyzJD48EehlYzXTPagToaLAqlqas7a2p8j-R6Z0Uo2Wx2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=ZJLC-erdIxVqr4Yi7acuR7WNChksj8y-_W_CiRdx7gU2oNHFS0pm1M8EY0gw6Bc7CAr2ESkCQcguDPnEidlDOn_s-DE_ol2kPySBY3oYyrCyye1ZqCB_LKaUhZP_PozA8gmK9EB2OBXIq-F-36alOTvN987iGgItUlgrRB5A_McbU7uEk9i5Y72vl6z3rZz0D_0A_PTxZkctIRbbzkHKylMatB2gRvECvlxOanb57drW9tMjd2xa8AyQzSkrQtV5q8mRLgPaNWckxY8qZqI09Woji80u-C69YtLvj06tfMC7klqEXcCeggku8Z_8KYQr5p8K0LOxbr2MqTy1rD8kBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=ZJLC-erdIxVqr4Yi7acuR7WNChksj8y-_W_CiRdx7gU2oNHFS0pm1M8EY0gw6Bc7CAr2ESkCQcguDPnEidlDOn_s-DE_ol2kPySBY3oYyrCyye1ZqCB_LKaUhZP_PozA8gmK9EB2OBXIq-F-36alOTvN987iGgItUlgrRB5A_McbU7uEk9i5Y72vl6z3rZz0D_0A_PTxZkctIRbbzkHKylMatB2gRvECvlxOanb57drW9tMjd2xa8AyQzSkrQtV5q8mRLgPaNWckxY8qZqI09Woji80u-C69YtLvj06tfMC7klqEXcCeggku8Z_8KYQr5p8K0LOxbr2MqTy1rD8kBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نظرت راجب آلوارز چیه؟ لامین یامال: ما دیشب ثابت کردیم که نیازی به مهاجم نوک نداریم و همین ترکیب برای دست یافتن به UCL کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28898" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28897">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZQptj-zh94aWKzgyubudVoMp3X5-75n8jefDpTFo_n30gBqXAeO0FDzkDwh78SxHn2h3KrLmg16pKluQyViWIQy-ZewmbjiJ_o98i6JQoCGmdeb9kncG19CidxIZQreFskcGjzT4Zp9Hgfjz7UydOzRI3qONA5wH2Z3tXM_mFeInVDMeiS3zs3PhVCoovZuVOcqCkUg8p0VksH0Z0AQ2ZoGX-TXcxgXhi_ZjVc9D9DnhsR2iQkQl0-ZwGXlHELafL16-cH2U8D2_qNkZh2NZr51HQEOlyjntFpdcWTQm4TBBmc9vJVJk8q6SpwODC261zfZuoO_wOR1e11nkZ1AgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه‌باشگاه استقلال این هفته با عزیز گانیف ستاره خط میانی ازبکستان قرارداد امضا کنه بازگشت داکنز نازون به جمع آبی‌‌ها منتفی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28897" target="_blank">📅 11:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28896">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SETVZYpg3mQKaEPFCJXu3LG0kcVUEWZaiIoUh5bMmZzn8tMeRWLXnxuVlIC9z6xPIukXmJfqavKNnYekMsaQbmwfIlzhPLXs3R_lx9P7Ro4VqZ6kGmZ3r5Uhe64Efv8mTUNaDCrdIjHGGMnohrrw8RxW7be_TwzMzR7klMpNP-Gbr6FowTz7AucSqKFfLadWW17ZYXZre2oO5X3XLtW5unhHxcAhPlvqXGn67pQW-rcCb4mjIj-syMx-Lg8J8omrSeBlxPp6J6mEYlEEYVML6nyRHu0V5ZNN1glCWRoReyXmzaC3AdTJl-SPrYwNWr61vP_NE2-YOrcErGCoaakXYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو شماتیک ترکیب احتمالی از استقلال و پرسپولیس که به احتمال فراوان فردا کادر فنی دو تیم با ترکیب‌ها به میدان خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28896" target="_blank">📅 11:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28894">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQCRXFbml9xYZYhS0KYJRSeSQnGMymLBcePdG_Y-notLg7dWGI6tQyLvA3EkGw0vbRBsFGgIpFyKGTYcFQ_cD1PoP26MG8ER8Y7J7CyozQ914e-GCiFnpRrFHHMvzN58lz7CK_rbn3ycUrN6iMWSzkElG1Jvey7v_sypvZxXwFxrLl-aXGl1dmeWbEsnNbxWb0nFFFKAmdevEAVNYaDTy6rKB_RWbhFTPzWY22RjChbF6h_WtsYc6BkLbcfAFGsSyvAhmvEqdH7_ASZS3g9TNXknLgZAHdCjY21Gadz6yQOcLpBZnVtmvGPHGgcJHi5fdi19_6cWhy7Ab25GYBd-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dbI3c2FBtS1BCVspyQTPnIDu--qVAgZsysmY4ZuxGyvGAQyQIG-VdOZ3HTybZY9MCsklIUsxwhnpzqb6L0xC347dT5-y4uxHlJcHgShh-eU8orJSVcgW2LQPrZHnyUg5XUmcyY4PFbhRvs49xls891fIdy9As3r5JRTwiGP3Hm-olPSucdbOd8cfbPZMmjycdgOyN86vawbmzGFX6wHXiEk8-_42Fw63SinGkhrtN2XlFYNw1e2Zgn0Gnnjbhuacsxs2o-7RvItekkFJZXH60PIC1X0tXOYJWjDOn18JNlGDOcrFtK06diLHCCD5KhcYqR3VlpWXpo0TiIAuIekhKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/28894" target="_blank">📅 03:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28892">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_w9lBJXwNyAaPgkt2ZhbcyuDrre0wq-RWlBRkRfDxJlenPyqPk_1ZHMeyXiHw0MEbDysyooHoU-2UzHInnWL2xrPcLsXfMukX6HW5nISP9Hs0DZDE5P03uYd5BGXAA4Hb5Yo45kW5ftkVSISvr6ng0DADhwsT7Hj5lsloB0yanFQCs-LYeJ6EFJkWWMVynFfKWAYFf3hunWroUq_ZnmI7XQwnpn-A70k10_7rcruj3mZHC3Z7ZzrH-Fw1HvoH_zyjoFK6Kbhu0gubLbQb3NeeLeWIUJbL2mqaHQNlR0lIk3z0vl43ktUmiuEVJs6yc6OJVrno0e1yCgnBdRqpDmlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/28892" target="_blank">📅 02:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28891">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=uPkXqgOEX5hrHpFmZDPLOzeuMTsMIPjz7KALSW_QSXFcg2-ij5JMc635QasifAQ1PWzTXfqvGdHeORlifpVmistUBh_CXidJ0GL1wJ8Evk75Xx2u5M7HsK5D1HtXQWuvBjqeSb2_NDzOMU6_bQDZfmh4baMEX4jOk3kTjcsgplfeGEfknZHrMr6HhAiCpkoLt9OcbL5vCmMYqgllXFapfQNu3DqJUxGuCr4C3w6KRwiVG-mO1b1sqYXSqlzqoKxTcmUy3YFeJP6lqi1jj3x4DUnW-Kjuj1uVTVlQwi6JfmEQTIQ7VU3jCtYDo91oPFCgYfDUGcCS_poRFoQfwWHX3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=uPkXqgOEX5hrHpFmZDPLOzeuMTsMIPjz7KALSW_QSXFcg2-ij5JMc635QasifAQ1PWzTXfqvGdHeORlifpVmistUBh_CXidJ0GL1wJ8Evk75Xx2u5M7HsK5D1HtXQWuvBjqeSb2_NDzOMU6_bQDZfmh4baMEX4jOk3kTjcsgplfeGEfknZHrMr6HhAiCpkoLt9OcbL5vCmMYqgllXFapfQNu3DqJUxGuCr4C3w6KRwiVG-mO1b1sqYXSqlzqoKxTcmUy3YFeJP6lqi1jj3x4DUnW-Kjuj1uVTVlQwi6JfmEQTIQ7VU3jCtYDo91oPFCgYfDUGcCS_poRFoQfwWHX3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار!
شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28891" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28890">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SswZdLnbMwOWWkHTbrk2W8eULK_mYpNiDMRb_48ZxTOhZqNWmyxqWS2KfgsXIAjfytvean2hYpvlhSTe4ItV0F361jtz7PLNdHHV26SupYdF6aKckgs8jQeHo1kCcLgFbxDfWvquy_yISXChxzAVExRZ7vuYJusLr8e-3qX6E-_ccqZUQH2BDRHRrV1F988MH-GpkLvRqNDrH2rno0nyfVBmt_cC5WFvLGPgUIYd9tUTZJguLjTyNIfISRyzT-Men_TSriEGtpEwkMXQoWWi4Oj5-3q25On1yfhr-ThvZrU0liPMzgbM6sfOAAteReYmBp9lFR-rRd5UkOrB51Q3BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ دربی شماره 107 با جدال حساس استقلال و پرسپولیس در شهر اصفهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28890" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
