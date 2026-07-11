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
<img src="https://cdn4.telesco.pe/file/UVE4kDOR6uh7OvvoDUfGIXEaULS_ae5vGc8mSAzYrelbWk1gt4_Lc4dK_Rr_yDCzocEo25LoQyOLjVAyU1R35VACJl6sb49IaOqOPRmvPtjufM001mHfI4nK3wWTiflKjiaoGUNTZ-sVu5ACHdu2zJGmuB0w6Du8iZLx7Pr79RTH5lxF9y6BMNvDQIio6Fok9ztIyK4CygvczkAORQVu7jQ-vToGBQcbPCuJdLrFFkeXGu98o74J3R-RNXoTaAuEulT9JcrkIomqPTiVADI7p5KjSJstfgF9lzQNvi4Ain8vB2HrVO7Yd-hS5UOXTyr8aqVynL-fiCHC5jrWiE0Zsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 425K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 00:09:02</div>
<hr>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvgjxT3aZR030Mx6fJoAKp3iz5PIP7jedz26VjyBWINBGEiIREO4nOfzSmgBv9iD2n7FJhrIly-ZhitD3Un0KuPVIK-NKIemucz6yXSELLStqNwSENsALnlIPIHmBvj0N7fjEGW9niuTaz7sKsuROcmm8Ifvf-5z1jZl0JLnijVESFsM4wufGXdTV1l-kMLapqvqHZ1cneybmCZWsRrlI4W86bC25C0EpSueVFKT9junY18tbm5XnIyk5Qkcbf06BnYOxTbX97prXCr54idCEDCb0Fj8VVo5eSmurwaEZqA6BZPzeuY-QutJXYs__8En2IHbLVFYJ3FrMFjXsspfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQk1jGRnlsm-gNW9PUUQakEjOhdFUIDNISjrJgL8jAwC3qmAcKs0188ZnDJ2mlx6OZaLXLxHkijDna7YjW-4AJ2fEWQT69tVgeTIR_uw0OLXzMnACRDgxFCl9zGTPyIhz7JeBoT0ZnUGf3Yf4E-XLK30foKKFAhzfn_ux-cgkf9PxszqtU6yX9gOLrk6UFbwRa3lDUZndDY6vn9I7IdtCaMWM9IgnZIABAAH_B_CB1lsFKX2LGAkAliegH_ajBQTgFUeciQ4zgof2xn1i7iJOuywAG2brDovnr1bIsLBHtZy3dvFjOBovvIvDStxr9z4-ZhNIB39x7UfBonfsMvJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ieh8r97hnYKrRgz43i9Hdz5hraqt66RPjK1T3fnXugxntPCAc23WDWj2gik2G9-DumbFrHbxeK0Ex82SyZMp4RKD__Qbifavwnv7UfBtuwXcjxTEFjXsgxcV9OL3nCVJD36ttENDBRQJsmSERyjij0Eq8ZsEd3Le7Q6zXHO2Ie2A2oZZsXtAfhwgwnlJXKXYB_M0XZf5xVtRikjiya84Q6hyo0AAI9kBqzigvcFUJuEcXgFCT9wGOkwtgE3fQtUQ_G5KRmRQdW-JqCF15KnejFiTHkQEHsPRS6PVNP3SMpA79lBi-IL2bUm8pHSEwxRADlMA3Yk5zQD1w234AAmwBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHZiwdDkVBa6hFMh2GkrWND4wi05SNV0YPALq9sAPRHOup6drqcKykqh23yGLwCz_RFKZNtXyi96cxEcnY4DZ6tpfwPGLy4BpOsxqa-d6X9fRHPy2J0rwGRgP_zxiytS98ofeWcW8Y2IoNMb8cKuz6P3_aJ_7I5T1GYumTY4YcFleg-WZKQRQXkSHuxM2USxw0R9diZf7N1Ia4joGmDXPhqJA9_QVrUDpRUAmQmHF5LsyoRMnzcF8_Oh_j9UAG_RDTP_hPVqwVoHJhHHZphw7lFRYE8SfxFq0c3hVhzW95Pr-R3GWynrnaVHklo6-rNZ2iN5qPg59g4ozQ3PUsnPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSFibhxK1DfNTy7oeZWx_t7esT9G4V3UFHNiXApyuOXyTulG91Ud1E_kTk7_UgfLKK-mgn4QsMuDrd4iXEmzCl4tmXj2N0rISBwND2FQhCvRiAIYS1cBTX3DypU5rgxFguswNkzBVuujx7JazysQXtTeryGWEMLiYkE_iGhm-UvfHhg33_pHRHuH9OF6NkPLXY5bVL-PbRKbhPz15QhYcvn0-n4r5dZEncVzbBIN-TIm5jgBwTiZLK4f-bRRmrj78qxchAkFaGaTMW5AdN4CLv3FMM4MswYV1f0nuaBRG3eVNB0RQ0U2PBvUAJnXdwBJf-K2PKPn8icVoQ-3wvn_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rac2itQruu8G_Bdos62hFBt1F3iFHTr5kCYFF2CB8AePqed3EOmnYKJ2UjnPqqkKLN7XIJsESFIZG8BGmu1tlsiwnfc0JCsaqTjlo3UL9CgPVONj7YrbDp1mjNn0XUtRLBHTKGOnetahF1hw1la7gBPXY72bGoG6EguMPX49Gq1hF-7WiAWO2cAdbZvkA5hLRs6-u5dYG-F5B3AYwiQvNoLKSCzigUHauq3Kmd7__RJvPjw4N15bA1xWQISDdG8Pi3Mm6z-igTjy6gY3m-m43Vs-vZ7uTN5a_XCWucWCx-iJofeHeb_GbB91Tea5vJ6CV89ix6N_Q4zKXBjiDsbWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=A8RBY0wgcwYZZtSb52extsIBF2kq5bUBjaTEFMv9yspE39YQNs69NcuxzSvjhCRcTjlnowHmvDlFEbjqUgqLk_A4EaSgraSBArY_mJe_ClPZIyg8QuMRqbp5gHxJhk6QvOaIP3MSzumP9Jl2HCzEEcDMfLYzxcKQGGQaDh_myx2zhRMqXbY1iVsm_va-aKCU01iyX773z_4FSkzQF4inQv45t6S-C2ihIbj6qymuUEgjya8DFvarxZTYxisjtS1_Q-1jzTqCnwS4TB9SIPNrRBECGIgEkUfZydX0s5xSUrUQLu-BB_ZlZSBgL4A-1YNCj24hQTdcCzVcJzkjYbMypg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=A8RBY0wgcwYZZtSb52extsIBF2kq5bUBjaTEFMv9yspE39YQNs69NcuxzSvjhCRcTjlnowHmvDlFEbjqUgqLk_A4EaSgraSBArY_mJe_ClPZIyg8QuMRqbp5gHxJhk6QvOaIP3MSzumP9Jl2HCzEEcDMfLYzxcKQGGQaDh_myx2zhRMqXbY1iVsm_va-aKCU01iyX773z_4FSkzQF4inQv45t6S-C2ihIbj6qymuUEgjya8DFvarxZTYxisjtS1_Q-1jzTqCnwS4TB9SIPNrRBECGIgEkUfZydX0s5xSUrUQLu-BB_ZlZSBgL4A-1YNCj24hQTdcCzVcJzkjYbMypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDOUBhMRhEQiEUYEuw3-AtBwcH-K_96V551TXnipRJf6NurUO6V66VvoS1xu3fTIaQpYy0buPauNZjqmcrqtgBKX8QcUMlvZZ2yiXYnXZh5BgzEC-3o2GrooZJe9Cak9uYidk2vNX4Kn6Kus_VADk1Dh6PScuhkgiQZrNLrnqC5ZU2V0Z5XBw0bKA59VsJjZ-K7mitq1NHGJE5LIz2909ENWz0D_AFR_eZA43Xg7lAt_5gy4k6e3sTv7WOwSTOLIEIVxaut8__GedmSnxal4JOwkRNDSwipcbfumoCreT-eE8X0mkfO3Z7F-XP0A75miRIvKlnNiTcXUpGocE9cd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=hoqKhNRnr5jRd2YXs9sLSAFoBym3tntowWt1L2lq12mfyNiw2gtecC9jG2PjPn44ZIkz0OopYP2qkOIcj545OtuKKHzGtgKKxWil52gHD8MPtNtgzFbkEYD3kKV-mlcgVKbncNlB1XoQzmv0BtUCX_5h4W5FnrJ5EYeu4x_DWlvIXwF0PWtF6ZCa5t7fq8A5U0QmnvZzD-Tv-xlRxrpHI-rJKtySPk40NgytFy9KfkampXSww_QeLOOd-DLP0BzoxNhh1Zs4mMJMGJo9vhkgoj7GuNeBtn-ivAwqz4iyFu_de2jD4b8FGLtA_WEBvfFipaXPioiOBxjhwlPuml8vYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=hoqKhNRnr5jRd2YXs9sLSAFoBym3tntowWt1L2lq12mfyNiw2gtecC9jG2PjPn44ZIkz0OopYP2qkOIcj545OtuKKHzGtgKKxWil52gHD8MPtNtgzFbkEYD3kKV-mlcgVKbncNlB1XoQzmv0BtUCX_5h4W5FnrJ5EYeu4x_DWlvIXwF0PWtF6ZCa5t7fq8A5U0QmnvZzD-Tv-xlRxrpHI-rJKtySPk40NgytFy9KfkampXSww_QeLOOd-DLP0BzoxNhh1Zs4mMJMGJo9vhkgoj7GuNeBtn-ivAwqz4iyFu_de2jD4b8FGLtA_WEBvfFipaXPioiOBxjhwlPuml8vYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeIwvvZIKDQn3HXe2KB0nyaF-JHojZz9NuJ88o9zMqM-vJpYY6TJzBCJLRTtLh2s4pQDsT_M4H3vI2Mz3BDz10KVKTuTTvXceXrPGR5wj_5wCz2lafNkDxj9u7GvlD5dRwPk2WEb69d9Z6MHPhwedJbtSWRdKsHZ7nIEDT0uJ3VMbSj9EpfCQVIWW47f6gnFjKa2Oex50i-ttKkG0sTGwbLos_o4XILV9mnszkvrEYzN4RR6y9ZUvr88x6DpwpeOLd3A4z0XMysZ18hBU2OyxmDGweg4GvCBf1LAXZEot9eRea4dhS46yhW6tm7H2VpG7hAFSNGjmEa8wK1QC-pvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2t8uD1vQ1slxmhdwC1fgc_Xsgl9g_sCOajMhTDSrXAIifv1ySE6UhPA6MvX5gk-LiZ8b1Ry1LSu-wEqrvmTz-9iB4YRmVFu2LjwBUcDCxQj19qkcuJcLQvvkL0QSsHcYPcwXXI9PaYaU7kMkpLeov_k0HHJgvNb7mG51GUhWWAHhXnzA2JvU6wfN0NE99K29-S7P5hnySNC7H4RaLrCKnF4WEsvkthDMqfw7vq68So3aQKvsDVmJiTv-Vl0u7Y2D89yUlExtod9YFNy2wYijMjYHC4QLR5-4AVIEVSZnfuq5iwqIl49hWM6XQXY66-3zFXpPt8VO06pBCok6YN0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C91RQJHsBe5o-4_lPfQFPpBg8Vva4hYDwm2aTRcr93qJV53LdHLWbQxSx-h6FYVe6VxApfkOA8TJVYCA3ynexUJmkxh8oxWonDNuk_Vqlgq9vwpOz1DesRUwwrUWKdCGSnqDIAn2h9lKy-fdJL75zOp_wjWqs5Z2w1l2T50nqQQzSfRajVlyQk7U7PNsyCoti4CzsYMsp9EWlcpHgopMIM6vfOUmXEF9rIzwa4oCi-k3xKO0_33SFZgXfqk8kWXzl9MQUfJe5CKRSu83SfHzfJ1OdU_o7qeGpaee1iXscrGBzK0G_G7mjrBFw8ofL5rpDpyuekQxMGzlWSP6a52mMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=jAHr_vbbcRe0R-bQ9TB4D9lq-lVItaPv3X4siBRijnrvapzPJHiijROlmoB6nY6kKyX1qTTKVnzhx0DJQZAKuLTV47PSSjcmKlfGrv96sX44N6RkmbTE_P6e-vE7ZMghKiz3-skqP5gBWNlTLophcM1nPTiAedaXFRzNqQ9dDp_l-Kb1Cm2ZVa121HbfnQXBQjJP3FW1ui3c03tmfobkYdhVLdmPHrstWIFYOKxVOb5iuT3GBC96__L40qcBXUwh7am88QCps4qDecpnePNuw55G9ZDQ9otZ00sUgOy7MBIVDeSsrwgJLHaE6iBNFuePVTVdURAyjrw3EqNnzNm-KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=jAHr_vbbcRe0R-bQ9TB4D9lq-lVItaPv3X4siBRijnrvapzPJHiijROlmoB6nY6kKyX1qTTKVnzhx0DJQZAKuLTV47PSSjcmKlfGrv96sX44N6RkmbTE_P6e-vE7ZMghKiz3-skqP5gBWNlTLophcM1nPTiAedaXFRzNqQ9dDp_l-Kb1Cm2ZVa121HbfnQXBQjJP3FW1ui3c03tmfobkYdhVLdmPHrstWIFYOKxVOb5iuT3GBC96__L40qcBXUwh7am88QCps4qDecpnePNuw55G9ZDQ9otZ00sUgOy7MBIVDeSsrwgJLHaE6iBNFuePVTVdURAyjrw3EqNnzNm-KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3FdtNyarYvNaim0QAkpa-Bi5YXq_6ZW3OpnKTJgBoXdKMPjX0Wrx1orowB6815RmOR5L-b-bHLJlOZaHIBx9DTkDqZ5qijdCz_mUSlShV1SKS9urdpOAJmP8MMMW8hkOeE_AboDkskEXrdQwoP2JD2pYcgqsrK7dd0ME7RAr74LC4l3bIxDsfS1TXcGHudGcK0zs6BgK78sR36F1m1q7vPcw7mhHUlA0W8VB-L3CRlDsWl7PcBXJ87TgsvAVMKs_zCtQsadEwFEfyrZhi7bP-M-FKABmIAvPPGkA_VYyW3X8rTF44S7etekIT4vhljzGeX7BKlebgiex2w91xV4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIhco7KVl0Dmj-kO-xFH5pPZWHbVZFcLvUXAr5098R3XSsuJBHy5nGkhi-kaw_cE9YSDZte1-yptG-LOa367uw0S9Y8-XsEF2VlX3xloSwg_0Xt1INveKh4bVeh6A5vfDhtz-N767597CxEvFmfcIhUj0uAUisgblhtk8gTKnLTpy80pJv-sCplncvhlRtOTrIqqocvvcBJPWUgwpx8FVch4_2R5xaZrAgcEMeuyFBlLT6GdF-iHbdHC87srylIJPmUGBVgmJ_IXWwIshwig8qdOe_u0wi5BjNGLmk6TWk9mCep-_LRVwGCGNufJHlyEgmeP0eunqQJq5oOcIJSuxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngZExvXYrKb95P0UkX6Lo-i-Slobbm4dLHiRxV36wzp6jw-MN22FGKo_6MkUdxtPA6JkjSB51FCRe4P664vq61_PglWacWSd6ux_JaAxeEUeEOovrVCbHaE9xN09LGjk520zMw1uZ-n8jYboPp06GGhMnoS57CmWKNpM6oaY0kxu-ybSzeBgTGwQVy1jhg3_nJVmt-VIxXzMkiGObSBR1eSrM-KwoOVsnKJP07Mh4gWInljJuEWeSv61gQ6Uvw1GuAt-_pIvNLZTPfHrGSzvPs1tOb5Ddrm6SCGrsqXxEoJi1FYn1xKVfrnZffQIcfwRpuFIh9h4aYvfOXqBa0pPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjxKglsdb6Mbd_UNUzznSEFJba-hUcAlksaFDxgogYHRW_1hWPOy1r3HYgMaum3LCflVMbe4vfjg39cp94ZwqluWYR91_Ar6kfmcIyolrmF5yZ3dUZ2wGvF0mC4d3mWvi3hpnDmEWy8jeEfcQsOnODnZ2qbSuI4tZR7vExqgOKU2nPkWFFpNy3vGt-JAlvRpEsuxoErpbToDAnlQFk5JMp1aEtlnBn02czNBv464KW8-6nCua34BvFViKJK1DVEUx-agNm7v5DqJL08XHZ2VMdvqqwZJPJiiBHo8Dcav7JTrzBnLX8f1Ea2jfHjVd9fIXAsqbDxStn6cmTbsfhWXjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U96hKYMfFSWOJnz_zWk2pW9JQM7vex1V5H4S_X3gGEB-KSggWff7HGNdszgoD1aI74xNsZOOwsbbYSyzAIawoxFtXlkzx3k_BBuFeYDwkNqZ6FLq2N68E81tWE6QWDzPUQ3m414UItrjHj8Nd1BMpx4Lb81DUQc7kGtDqmGtfgun4VoXbDlAE_sd1ATTdrsynrCtQZX2GsqHeeQnNubI6W8iZDrxCIx_KOwFfleY_Dj-k3JjFMVFsCuFoQGNd2yLt1hGfJTg1jcDhzjdAlGZO9VymQC3r1t8t3kuBk3DwjibnaMat2lg_zlOEb5nXr8DLQs33SNESIkhjK11ZEZnFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTxGXxJ3hoILIB72CYQz0qHjgi_FtmHAEq97suaoFoMfCpwZWUQL6BexJVUmynmNes0tKtb2cSrrtTwmQQcAU_VaP3OetCS76XLRqKSLYIjNPWz2V6ah3vbNNqH7kBARXHB7wu9OTouk5Jj5-5j35DM4wTMF4ubGttGjIV83JKfjFlWEeFj7tqXwDbjMHRLqnMxWL5nlfW8JtuawU2DoXRRxyOGho1VIGV7wUWNWC631U99dgfMTJhSo1pIAJ0xR8yYI-JvsDAcIfbAbrceb6hIb_-guIwpBWVniTUlV8z8cmzAAdYGoLqhBNT-2tryXVie_4-Vw4JTTngkIko6MBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BroDk_LRpNNxwiF6vyDnzf8Iw82G5FD4H5VAQBWpThPfKWKAa825s6AVqFHoFgohbJOm5WWs_RRjYQHAxr_Xwg4CZjpNBpNdllVZtdb9DH1GraFz1DiIdkoX5pxC8PffjLt0OQM8BIfZANjoHnkUgWTvgYPNdTF6MCcm6_pHyKizrt8nYYd3aCp547fNFJfP4JfVwSz2huRRI3oGHcCtdyR79FFkGaWrQXcAfkZZebGxc9OQrduC2zftziJ0Zc3dAcxGHK5ZPGUa-YQSqrAVCM56CXymwKUe10O0Z_gJelgpSSnCn8giCHiOzZ7F4m6tFNOBBd3_S4O26UinlJ1IYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obV_3tY_7TVC9N4T_o5OXBP26OreUk4iCQOrDss-b-TNpMIrypE5QNJu-uwHOnR_UW56nuCktO2Qiet0FMfENvCHQgCfn7EGGxt2qeb02tXTSeJgIriEzBnUW04gXc4CS3GN6BfNy_oRlO5YtTMlzGEDOZth8MAY-cBCZ0deVWZCiRjvNB2ZfB8A2l20OKfb97RJhlEbapiqd7Y8aSz86Z8Ai_1ULkN2t0oPIeEmfeJB4x4CrbkYLhrL61JN96Qk7SRkXy9dtHW6QszQRHxo7Z3UuIMXwZKaCJFzlEhj3xzGX6OezfsVq4uFjHt93OfTQFkj9jI9irCaJ_-7clR-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25458">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/25458" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=RUTwyZRqGPi2vZ3QLitp4ELcloGQ_S2tr4M_UukXExyTa8xP5mm8GCyT-Kdsvua7AZIUb0qcb1FmM_yhBJKhIuxF14OiwvAMncpFt_ulePmJ1FTAB6buJC6jX59ezNbsUK2PwYp1bVfQsqgDJddz8Dz5MUTFfapUhos3S7Yz6xb871eVwNKHwjeSpO0LgYWIrT4wBYRdJntO0IAnWXxBZNpoIc-m2X70gnBlo4UCsE6dbbGCrB1cvy2ih19IJJE5cwroCiCIflnMkLPwNKafECtqJz-o6Ouz3cBlOcQVQpo0-ggjKEOSUhS-x78h2Hs4gw9NYQ58ILdiGytiolkL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=RUTwyZRqGPi2vZ3QLitp4ELcloGQ_S2tr4M_UukXExyTa8xP5mm8GCyT-Kdsvua7AZIUb0qcb1FmM_yhBJKhIuxF14OiwvAMncpFt_ulePmJ1FTAB6buJC6jX59ezNbsUK2PwYp1bVfQsqgDJddz8Dz5MUTFfapUhos3S7Yz6xb871eVwNKHwjeSpO0LgYWIrT4wBYRdJntO0IAnWXxBZNpoIc-m2X70gnBlo4UCsE6dbbGCrB1cvy2ih19IJJE5cwroCiCIflnMkLPwNKafECtqJz-o6Ouz3cBlOcQVQpo0-ggjKEOSUhS-x78h2Hs4gw9NYQ58ILdiGytiolkL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4aL4KftYmYd6TG0jz8fAczn6NBZqIGX-bUp9F0VUY3edDyp_aLsAj1xzMWb8hKNcd8IU5pomysSAB1zOXkPzqhg2la-lx76UcWhHglIwUhQV7QvipxugiO59k5K_YOgc_0OSpfFfRjYLPeQgAh3seXXQuLV4bVDwcu7lrLYUDuPT8RaXffEzdrEyRk67l58KBidrVbUdp56jWqWN94r8fd39NKt-IF7vJSPjJDos8FY0sn123mGpzWE6iU4St2jwIRGGh0WIicGrpkzSK1jwsfg9xlVRb1hLk3E5yDYCd-w_o8KyVjZADJJZn8LzdCS-Ev-vrxK1i-VRktGnvbF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5h91ST3pc43bTWcKDJsgLS27kmTi9wbngZMRpE6P7u_72KfrVY7WjsfJL_CKGop4KmnIP6d3LGMNxUI3tsQZESmWnD5KnRXITCfRjq0Md_0IXHMRvMo3TSmA_8C86DmjZDALWsiybAUavRpWFe3NV2gMBy31Pzfdlw5sHq9k5Pvopg21FV2lfkJdi5Ao42BZjkS5Nb770_uvsID7b0o3fVXpw-SnoTIxKsii65d1gAYKLrNRM438chn9XzfnSfWYJ2tSgAoYD8JR9AtSNpHeCDmFeQ3KdRN5a-zD7r6okrajGx2F5CnuYYXRktgXH6v4r3jwx9AluWfbyWyHa4Y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRGj0O1ns7PG0MrADifk8JMG6f-uvpSELaPwBIa2P4cSXVL0J4pIj08MohQPparVhrp3CEWAG435JchC2UIiK_EKEjXY1zmpFq3ZMsxJDyRPEc16v7GUxn6G5KzmQ9b1Z__02-o5zeKiWZDGqnN1U4nmVr2gRc7fdb702jCyBHiB3vrpp855chzn6YLBpIYIhOkWfFluJKBUFPEZpIHzX7CBo8wdJ-IC4lhdNS8wrLBJ9Dk8zVgJc2oNP-kNQ244xcqL8LU-OVnTyOqLYc57qtq6LQ9UgpdsTjFXKaSLIj-AdAvudiG0tZv0hd96QO0DPVTihrQ5p5jtWSXogylyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA92UrkPVvO5oncbNgEdmpwN_E0t_0Ec_xy7NH4x5C2SuV225LWRuXS_5xiUL25GD-zjHYJQ1FXgCvcJE3TB2X90ZT2rieXVkiknl-KHDW0rOcbeJiCAOhGxARf70RcbCh9VcnpTqoRjndtUZNKqhVtoQJURFCbxbGMNbZ1kBdRHIp4k5pJVgrsB1gMJMWkO6dIT03_pNnVYAuAx6UHs5vYzy4VzRKA-0kmCRht2Dde67-45G9l_xXLmgS_rZSvMYMuQYRSMl9I0q-LV_6zmDR__sNOy21JQD_EgW88NQu5Xeg8H1P3hYZBowcQzWgScRUbe65rXyf4R9flzsoXWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiQ40lKidiwAgpCBV9qfkTIsc_t8uCWSV3RJMvg9jEN0U8uoiJ_1smTajhTJDt3G6kTvMA2mP-U0b5HEoqjuH6TvA7NFHxXPd6BHWabiaDx49k-5cbKemO0LYZ5NFikl6QydUblR601rAqJz0c1BPsgB-QJyrs1sGdSH74aQEBRq_JyG8fxAvrndn84ZD7Ey1hoG7ZXJbAzcFUC_So-afu-0c29j0CBkMkJlHSjN-WWYIOKmBP7qYy9IA1QAD-pYTSdAqJF227wpiSbFQNB9GUlJOY9GxB529_uS6B6GrPgA5p1JbwafypWKxCvUnLAfSClwe8ftHDzAsv3DXwLEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROOItZ8VNtR9-cyqZjhwjf6RW_hN5Pw3DPWmgMykZLaoyrLgCOJhWsP39dY6b2tEQobJxoJiAFrlcsO4nxm5MBUJe5Xy5D3v-WZQ7IX_UDiB4_T0rpEbZMZSsu_E30_GaZV23OlOVpHacSiOVkAsBzgkkbZVt7dlG0VnE_QJqQTe5cBT_lGtqZBBQUNjM_xodm94SiXtEzwB2DrNfOjIG-hppu06zit7X-TlO6m_b-1nFXO5FuFRay3fXhTXnSAXrIFsCTN-SHKwmFhUE6q7CeOC-0O3SzM2nFWnsc7Ie4Dq39Tsu4_zjhDpL9O051fdPK-2K7Fq0CYs6VwFk6CBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7bSr3WeT0WfIBT7Yd-GxAQmo3yFhANXMbvcwybw5gBvjoHT7aB3Y3sD0-8II7pPn5VvtMWpl3zvoEFOg0zBaE7ot8GnNoQQtngcGJ4wlMmhs4i-RIVMd1c6THVlcH6ksbshhtM64wkGIR6jkRHysrWMKzLgzu-LKG4JqOu0AqlaK0ZKG6Uylq4FQ2tb4UxZOXDUoMZDhOs24PnglDat0YRPKAZBUD4KUu2F3KvpyPiE-yRTf-z05afYBlBoT1-2fHsMQo6yUHLXFZ3CxQCNZ8U4ajH-RaFQ1bDK5vjuTuLhUsvUaRP35ZsuSs9ZVaTPtj-15slZ60KT9qMNllekBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQodNstOKCQ9JRe3_j19yHJtPtvSMIMQAOh7hBjT4y1XSeGFIRwxxPdn-fDNkjK_QCkQ65p6zsZfGXeR5O88ihfq5YPbhKnWIAOOPTq9kaq6ULhnXfKCGUFk0l-5Ut5x0pH05oz0TUIPHHnjKG-Q797zMbz1xX4Zk30i6cKppxDW7p8YIYxVZ6Vjbs6ss--gLlsVC_XYuF3avn_pnaU0zM1MV8lXJnAxAhAW9RCety6oVJEPFAB729l4ajAAb85o3pt2FC1IM9V5SJ3WBxmWLR_PCN4XRh6iS-mZyJLV4Z5Ob0nRJBYdvJyhKvNPTf83wxyShvFMtQYndyderSg0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKsesh42eXmFBvJJ4GAVLjW0dXPEScCWbzJWlCksl9I3Sy9j17QXVItcqZ-UgynVo9Qgrz1wgopH2s9CPbPnxjeaHwH5OdGx0H5hGJoV0O-ugTw2QQsfwgdHhAq1Kl3GFSW2uC_PDz0m9nod_itL4eWKVly4_cNTfFmTELjxQRwJoUIoxzipEtvy_tWXDWi9qZa8tcQ_71Z8xx0QYa23-BoGXVRSOOp_4IxEqOHfDwzQnwELz00HTz3HFiuVGIQTIZySFB5D5rRB2ZHNZQnf4-wDKCtdzmnhc5I_uYUdRSFL1rQRs1mTZ__WEJ-hgWFgUsudjwVYZFJ6VCc40K-Taw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lk3GnIEwrxW5c4Ctgg_MM6nvcagjPCBEUHH2TUNjeGpYUNpppBarelBSOISREOorfaqs08krUccyVKze1IzDr7fUWJrA7hVS76EP53fW-KuiOIo1SFz6xkqxafBQHpGGE856a3ofOGPBn9njXDJZxLfsle1_ikZECEkOuz9T_IARRe6nO2l7gwlyPCfZH89rYviBZJR9jH6HQqOgCeVtaJSpjlz0J2U5p1tmdxWXt5K7Udy65wESNmDQrGUpzNqJS5NP5TiDgDi9YKxHmpuTXbWknX4HWWFTDGcD-arSEOQo8ttf7AhpZMbCigW1RSQ_qP7IGiEC_MhUdZefLtiH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHMEsWN4OON0EWRTWhBJD9Ap9nGlmkNWMsLhz6B1cy5RPvhICp1WhQ_gSJWpzedWWoquPpOnPS3qONDvjBy2VnNVNGsluao49Y4GbV7dBEe6RMR39TBOx8ZgsUYcjBU7Jzjg16KWjVXBjwFB2KnfVH71w3fbOS5cXSXgHCa7BWvlu5F09HcrI3UZYv7HGy32W5UMRWz1wGNgFTtcMTiR4MkFo8Ic4_1ZEGgZznIhRGFpyHCKyaJy1IOF2M-dLm3AQiZgJyTamm_ddPVWwKKDikRpoNjYuZ2YDITCeXKtVdp1e5o99JnV7h7ZKkSSWo9LMIsuox4WVZ0DKKlIbNLRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY5LvNclVQ35gJgzu-cvnHQWz6Cp2amGWmg7o73HS8PHdhGp-vvQe_5lR5LM-5IYOQNXpwNM4VNqvq6ZW3KEJ8gMUx23WtTCg6tOmZJavMUgoaDE3S9Qx-vpiw5gRH37X2jd3kG983IxUlgmvHcaYuaTkKJmd2wEsnZH4DO7YJK3We_okuSajbyOqsmbHkUJoPhN8zYSuJEogkr-Fp8FuoMNe6aL81mAyJJyFpt6vwtsc786T0u48CCvsYeYPgiRFpBnHSRoxp6KICdlyX9uFgZqMSvB7-hLv1M_8XROpZNF3j9mgZXCQns6fgAj6-Mf4PBa7Poj8L813vIeAYXVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f29VcSfIkNzXjSsbl8FKlqsxBeWDUvoUErXKoD_pmvpN0gPNAaTNxzSOftrVR8DkQIRpWtq9uI3k3kcOuhclprIYy4WnPl_4Q6xBXb8eeCH1WtEAAyBENFMlukO2An0Elh1etoBQLsnKvbRduUuMZFgso12_Z8aLHHzuj6QndrsO3jK0T4gwXFKwpnVK75he5hCnepLTnnHwZGf6ig8McQb3gDkNIopmp6wjttl4PjBWA7MugYrUDplh5LFMqYs6Xs5V-v2b_pMwzKaEtx654dbLyEI8qYoc2eQbyJJQCgPx60Agk3Licul418Z3Huya9vNQwXpqSwGIfsl-outSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9PkffCtbuCZC4-lffGKH9C14u25mzi_Z4tph4tDe0pOFPKDN4LmQMfpe2RdAJSg2FBt2FrAfhHqQJeI6lmkgfZO0XM48mPNEm5JJXxnYm-DmrSLj9p3t-b6oe2ULR_9EDS2wto8ratuPv3EpMXVtg3J1NiSUbhVP8xm0S53LfT0aAFIvh2SvmDo-TwTsLcanaG5zlACeSQW-Fzia-d7OzoSIyouZVtp1edWb-jlOkWuPrw-pQbmC2x0MGKAQhuXTO6V8to_CoT9EaNlPbP8cf67B_43zm4_lZsp_w_U4TGrEyE5LfZ-uFjQJUxqyUqd8VuCjB-fSchbJL2Km52DrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=KVCQxjLXR-tT5V1hHcag3dNri6BJ5LLH--Y8kr9iUnq_ydjoXhWUfoWjlSUQnmxck85dZGLzNzorlLu5jRLDngU8nsOHbEwOP0YPvr7tUAF8vJn1cwMjfvIQP6rWQoaW9qcfeLwhmp0Wwk0HJABBWBax_-PovEMxh8wet8Z70DAFMwrDQ7vi3oEzWDqbs7ErhqI47IsiUR4wHAzlcoeHhDifE4NV5cKjBW_8ejkiXfPf_mgziF9MU1kXpt-VpsMTqWwNRacGl542lZ0WGqHVMSSY-AmeTheWA-9l6mjCmQVO0w0bf-ESKsXaLN1eqsnot7PvZQU2WnmJHu0fqdj1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=KVCQxjLXR-tT5V1hHcag3dNri6BJ5LLH--Y8kr9iUnq_ydjoXhWUfoWjlSUQnmxck85dZGLzNzorlLu5jRLDngU8nsOHbEwOP0YPvr7tUAF8vJn1cwMjfvIQP6rWQoaW9qcfeLwhmp0Wwk0HJABBWBax_-PovEMxh8wet8Z70DAFMwrDQ7vi3oEzWDqbs7ErhqI47IsiUR4wHAzlcoeHhDifE4NV5cKjBW_8ejkiXfPf_mgziF9MU1kXpt-VpsMTqWwNRacGl542lZ0WGqHVMSSY-AmeTheWA-9l6mjCmQVO0w0bf-ESKsXaLN1eqsnot7PvZQU2WnmJHu0fqdj1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H44V9VDDA3ckxe6Q0xiJWXTmalHc8QRdHy5Y_TaS9WfzaZBA0MVJAY5etcwQaiXxueeN8NSz7UviT01PzjKSnNGV06J3SFf5B3nG_vkalzlzwJDTyWVGRtTzSLz9QZa8vYgBBHZ4_bln8WIIj_X3aKmLBhS76bq2z5oSnTvi-ZkLOkF715si8NhdORSQ6wRiug_uN83R8zdSC7jXLrQHzACwb1W0qFpZSvjmUHxUieURjD8_feFE8JkDNt4agk8I-TXZY7gmkTHtoU2Vbm36K2YfDRbOSfC9lvN5NKHq_sA6UUjmfYJ1eImUMq8a6cQNcnkX1BIyYqbq-lQGKCR_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3-UiCZQ7V-fCeBkpPHdxAAvxeFEefk4E6fOh3n_TadMpsJI3eAGmfbfl7PmkgzhVPyc46oavDIQHXiV1SsxPwEV1J-FLB3Uy-KW7K8Gsx1MjOAe42XQ32moBdDAYHibuZSYCuZ-mup4lAwhe4QhGZQ9U0aQ0CEYnEOPn90K7aUC1Jr3w5PQs5BzxZ88_jYU6RKNNkaJYMeZOmk-gJ8D9A2l3Xpzi_Gu4Rg3eUUwbxqiGwwvp9OzC5yMbyorp-OnmQUt-O1u3X2CESNjQ-IeGZOBkCiSsz32453mgASTydZkwlHjlg3ykUX0wGU69By4Gp-Wloh9r25lJZsmtYlWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X443etQ4sM2OAJ7SZDYLdU9cv5xY7DZiOcpB8dYhj8ir_8yNM7WSLMMvA9MQx2vRmKzyGGEaA2kHZH94tGyyW9U4ztssqO-Cp1lbq3SIEPJwuJG2YVwl2XU9SPwTkNQUeRfn9ZbZA2JbXwMHBLu5H3THhVNvEIQIAXAaQNRW5VkzfNCzSkz60n96MbY27jC6aIbA693TnwOnwqR9vlJ0xtFcCZP1BYKkkjyzIFItetag5n9OJfB563ovITvEO6zVmzFc64k688bNDNWU-YuagyB2HRi99gggpm1yE-lUdGLs5WM7Jy56L8wcDFKjmB6PEaqGcTc-PbtL1RmVDG6t5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r36ArEaf3Zpc146X1fLUU4B3KHNusHJMhKQ1XRbA1nKtuotBrZ_fdSrThuvypQt3ooY8HRPaB_5ZK921FgCmgImRnl1dUKJ2luKGdDOVSLJzzDLTOIn1WejFIS4k1zS4l9mZyHHMPb30r1KHLEeU_4cSzfPUL17eEBsRSNxgbAtX8zrwz5eSrYrSLy9nMxZTzbiQ33jER1Oh3V8gQttJr1UAXbWQ3Nt2d1u8fnkYHn_T7GFMcL0V3MMKxgWZZQcugz_8hfXd59HBw8wKzIT4tjHgy9YZk0uhVGpCF7tnAGRFCYM1Kv5YyHwvm3Cz2M_1li7DbBtOWfOuInDVO2BGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HABA5UxS5tcOEfCq8A395l_dcDJYi7Yo08Z3VwW4GjoqnLQrCkMUVd3KNjGOjWaaznW2LYamCsGfW_UwZmip1lTK8sgUiu-nn_H-jcmUY9njdCC2GeAyeMW3PGzHWXf_Ya9NWzONo9kxml7bNcIsDC6Z2177FTSkA7EvYHqX0D6qjZBuhxiK4ia8M93h8jRjhpwxDAqwbb39KDcNlpZHCkX6yv4bzST3VTTVahDxJoLwiP6e0pM3ma3Tvm1S2D_SAXvfxLA7KVmgDPsACjYHCCmReyjBnNg17B9_5OL_MV2Uho0o9a98l6chNCp_E-88MudCARhCfNi1Ncx3RiVbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DS3_aUyHBc1VaIWHlWz811SbwTr2kzkc-NCnFJwfFQUnu3_nw78rDM2q7jpGzlbaE-W9X3Ptox99_slQd5jYg3A4Jk-COVHvo9IZfGJPv865nbnH4ONEhPjlgE1TZb9ksT6QRz8-V8bRodvpfBxU_frn4f6V0f87m0kKDqTixhtwrrhaquvUtdc6URGaRoLRBwCmgj0nDkUKrC_2BXQJfGp98WL0GzTZL2-0im1O9hQopzeVSu9fKj7EhzH7hAeOXFbKTQ_Dy4AZ369uxdWsBUSOVYAJTvONclgiWkBNNNk023u3d8b8DztAVjXTXvT2rTRNESa3Ib2PHuXJyXDFeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=oZg-9amlhvKqrMuNEFqm9ycEkrNijMIfzOE87vfa4xlT2_jK1xp5-ZWSvRJAlrBy18qTd6gSpSqPZHgYcLJ3gJMYZKEmJSnGzeHOz9Tn0IWYsAcMEJjNOL4K0yYu80Pq7DSElZc8TGBoJ8P1Y8CwQ5SqkISmN9fn6ardSh3cOyb2WhaDP5cGNgklH6WhjyCC8Fn5J1qlH5WJK1FpFPHnuxxJvMcS0fMDDNGoKD_bkLoOlfAThPKnL-11WVG0zxqBcf761PqWljWr8yfvCvEmIvQtyUjFgOGSDJM6irkIw86HRVWvvjVlWtBZxCUx_U5xx2WhQHM8TYWA9QppJUj0DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=oZg-9amlhvKqrMuNEFqm9ycEkrNijMIfzOE87vfa4xlT2_jK1xp5-ZWSvRJAlrBy18qTd6gSpSqPZHgYcLJ3gJMYZKEmJSnGzeHOz9Tn0IWYsAcMEJjNOL4K0yYu80Pq7DSElZc8TGBoJ8P1Y8CwQ5SqkISmN9fn6ardSh3cOyb2WhaDP5cGNgklH6WhjyCC8Fn5J1qlH5WJK1FpFPHnuxxJvMcS0fMDDNGoKD_bkLoOlfAThPKnL-11WVG0zxqBcf761PqWljWr8yfvCvEmIvQtyUjFgOGSDJM6irkIw86HRVWvvjVlWtBZxCUx_U5xx2WhQHM8TYWA9QppJUj0DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6QzfNUCpVQcxkMZAGJ6O0EkV3Ku0oVpQjT6ZRZIHSZfCPxQfey8c8nxaibWgtrttA82VMHpb72Eu0WcqvYLisdes7qcKYpIiTbSi_gtUbokENS4X32pklAak82w2a9t1LgUD8ysIfGhZLN6_9I9th_7uR_3x_wtEjuZdZDjXeVZ-J-h-DJStjVH4tKmw8BIUY7vLakf876XCbG4utjuv8akX3Sle1CEQi3dmevi9boM9PAPFLA_I9D90uJaQZ3qXPmcg3dMbKjLSLYn8ZmRx-R_Tsaqp06u_jSWx2AAppGnyxKYWo00vLR2bnx9PG3OOeCr0LUxYfQYsmEewZqbWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3-9aZa30grhsT3P1ByZI7o4RTea0yHIGKCfySbeBIOuPWgUt5n3untVRj-6RHyHaEbo4pm_Wxasrbiaz09b0diGkqdlrfu4yPaLFJYH4k2EmvF02EiICKkA4idL6gLd6oqN9JLS1UsLgX_xqiD9QgSztakaahylEtVCFIHR-UUEUL2pUd88lgf1NuvYWEwhXPnpGkxFXKWpkdhsI6zyRDYR_LXQZjRMBCMnvnpPhhVjkilXfY3Nb95MXQVHbJ5NEhSBpAEIGKKtTlJUvBonNGTUowgVa-MOZKbTChAA2KC_Tl2yTX_XrvH7Q9S2rjSeweHN1SprmM85jqdzL1S9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVWjcOXxmzvrAmwW41s5oykFfnW_Aq5F0hESifOR6XE-vmkLyX6RPvPqEI4ZR7E9kihRnjHO8MdntefDvrRWX_gZM2SJo0Cd_3TyMLMBVAm2CLnJVJgqRqOah1FhP2HYUdgBHbs1qprjCyQt2dYHVA_MKm54apbk27qVuXfbec33YiPq086O429E1mzj_0jzUD5B94L54M6WOooudoARt7qAAgikR8q3hy8FSi8VWkudbGtNcNK7SVZgJg2xHto4QENq2fMBDqIvxwSO69u1KosJWOx1Oz2C8Kj8foWaAJUERx9OxsAqlXM3Lx69o2PrriABCHp4o_4ZKM-qgn-Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvYpN2P9abGUNcDs_UoIqN_iRQz1IMYM54cW9Fe9j_h_QqkqK7-oGiA_cXjtIsjWJS8UUWo9QG9w_TIrLx88n2zZLdcQMXCL78Kx2foUrqmWCy_LjDqn9yNQhNet_Xlu24BCBSuJqfKpLnZVyfDL2ee-WG3rdHC2wvuHs2ta8QgKX-khEkzXVj0WtO0N9lsfypaQpkZx8kO4J33DPeS9jAvtjYXpCDAZ2AdsfpxGJ3k7HmpeSbCtv2YOWtFOc1P0pEn5cMLpKVRRALPlOATNPHyyPuSPOpYO4S_YAiO3IaG2sPvf0M2qzKh_2FbPeY6O1xUFzDDI5M-5nEpsyx-VZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq5d8Kb5ajw78BMzceTSxdpf71fcSUkAI3Eo5URn2T3zRInaiyzrBBwleXDlmMjR--971FDVvNBQtOsiwfRdQpTZ3Q2DhlSRxT2KFLb63YKGbfuWwbWZuC5wEj2NHgYq3dhKQSo-K5cb5fCYPN4MQE7oeJU3EXMjVPIQUYjqLhlw__dGzWMyA3bAtdUOIUC5ARWAtSSObrPZE8r8RNp0I0kTBafjIORGvl-3YoVVntQGb4hwb_wkMxEXasv9He7uxO0XiAmYlRHO7B5wkyH-bBiPFj_DqyOU93GMXNy-Uh5ZLPYsDxipB7mSaRLN7ydbmPl5Yazo2egCH1488Djv1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siWDEf7iMizoa1r3Vb-YiXCL2PXv0GzuInnihEGdzwxDEjyZF4r6YvTbjwhuAEB1NHIh6bAeHtLzKiMopRt333xnU4etZGza-HHQZ6Z0tZUB_WvNOZnpwuVYPYVeAIGeNQmiQ3yhTqgIFkU4F0lQU5_rk86VbiU3UxV-isR4Y4WQ7q1Hcx9ti6IlbOHvPqBksYZ3oVsmSIay_ahE3V47B6ASLTXMQ1jZn6g-DSXB67kmIYcLJd5qzgpuWoV2FiH8ZW5zjpxjNwlPlQJ1P-IYIBSyIJSOApY3S3UGk_e85rpDaw-OC-iujRF14PS4jip_VS4Ifu0CwPIF6vewyyXGoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPMl1hP2-zH8ZpceS-8OA-7fRNevG_yiNhCn4ChQoUXeieTlhAt70CfSHL1PI0xRxWNslupa-C2jj7msHlKFLoGdrrJX19psF9p0fJafsPaTT8bziIpWuDxJ0UZKsU9sS8ygf1_IiY62lb3xbfX8S8DMAYsxflMX7jn_eXAGm4ok-cjBT656w8AhuXgJYT5QF9FsJWOhDsTeSIq6QsF7Lk1tjUsavQd_2zekzk_AKC_mfjjiKSXosLUZp7gyUhNyBMucA1bpdUd0iv6b1ZIRIyhJHZN8uK9C48LuuHNvC4j99jM9cg0q_hWs-1a1A2hzc4HqsdlB0Sitv078hrLSDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=p3CQwlgzwwoRdzeyzFYsXCmk6xho9X6UKCjmGRLnKguvgqQzrnoh72sFtgGJnd1Q4hXEewuFuJfuJJJ6tiKo3JJeXfB5eHKCch9N2KhccaEBXGi1_5FySw-63NzKI03wut6rzKxBpht4_Vn__V4_elXWZtviuyp87PchSV9dO9-ZbAqrAvT0d0EC_wqA5rMXL6hnajr5lIt0av0lfNy5VuHvv4G7s61GIYkweB6sKStIQX-FjA-cLAZ0ygsykUsnXKyp1J8OhVp13dCn_eC9apn00GuoYOIMCXY3-eBJJ3o5z3AmnA8vk_QXwJw470lOg9-scoSoqqaZZ6YFKiMWeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=p3CQwlgzwwoRdzeyzFYsXCmk6xho9X6UKCjmGRLnKguvgqQzrnoh72sFtgGJnd1Q4hXEewuFuJfuJJJ6tiKo3JJeXfB5eHKCch9N2KhccaEBXGi1_5FySw-63NzKI03wut6rzKxBpht4_Vn__V4_elXWZtviuyp87PchSV9dO9-ZbAqrAvT0d0EC_wqA5rMXL6hnajr5lIt0av0lfNy5VuHvv4G7s61GIYkweB6sKStIQX-FjA-cLAZ0ygsykUsnXKyp1J8OhVp13dCn_eC9apn00GuoYOIMCXY3-eBJJ3o5z3AmnA8vk_QXwJw470lOg9-scoSoqqaZZ6YFKiMWeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6gWwudHi2sxbsRKupAmZRLEFpWzziN6CLBQlAXu3hm5qk7wm5wuEbs5NiRaDL925Qx9K0wP3fqD-7i0ESQCr01oIYuP-YKGScduQdBiHEy57Yh56ciN8vZ_Otc3Hvp13MjxSC1M10ZQarg8cWgt0PRx7RE8dlDYrwPewS9pbH1EdGxrNaa-AdNEEc2i7wXhVVyaaI9LGYM42E42gGTjKS8oF9ZsO4OkySVjjCZqjAN_Xy-YUKpGc9NUuh8DGqSbm6RP-Suv9bX1i1Hm8dCUYkr0KlMBphpMg56WVJ7EnR8H9bHLnuWBHP7QT_lw51fpBmZ3vqxaGOtL8vEOkJZvAVzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6gWwudHi2sxbsRKupAmZRLEFpWzziN6CLBQlAXu3hm5qk7wm5wuEbs5NiRaDL925Qx9K0wP3fqD-7i0ESQCr01oIYuP-YKGScduQdBiHEy57Yh56ciN8vZ_Otc3Hvp13MjxSC1M10ZQarg8cWgt0PRx7RE8dlDYrwPewS9pbH1EdGxrNaa-AdNEEc2i7wXhVVyaaI9LGYM42E42gGTjKS8oF9ZsO4OkySVjjCZqjAN_Xy-YUKpGc9NUuh8DGqSbm6RP-Suv9bX1i1Hm8dCUYkr0KlMBphpMg56WVJ7EnR8H9bHLnuWBHP7QT_lw51fpBmZ3vqxaGOtL8vEOkJZvAVzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DN8mPvhTZUhwhdmvrELi26oTCZv-NWpRqbV3Z1KDUWU3kk_BjqukG9_-0tk4YlSIWH3n1DsOc7P9jRFVZFDLXNOdLGMifWfP5vxshGKwunJCIvt6Zm0h7ZXkCQf3a-AjuOFw3QgG801Dp1BGE40CtRy_03CWHCqmWIoNvCYP38C5gCIDJDZEQgX0C5QVFCNqXuc1X5P3yKEd2PlnykLr5HUZWWHyn0R2-WFnINv0MmjCPNmEc0PC2V9sMC2_Q4fz1s67gS-xggziDih3fpdDIubPEpn1XacTUTr9Fs3KOg--8mogkKTDO-2y2byw_LSY-1-COUNP1FH654ANE511MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp0XRocAs4_SeWqaUs7ARbfuzOUiFHHRn73G1oVKmwGMUz_47BVmzpkvnNb268uqBNN2CgmwWgqFtMTYmIov3arnVrq34w35Anr6H5YOXfrisge8E3eSba6nEqpKK5MISXvuI-AJUe9nHmpNVKGwumHxNuMOY7HSQrl02g0UvragEY4Rhyp5UfSgvrq4XSy3hZ-RAXvWGFTDEXSzWsH7EpK_YT8IlIV1QnnO3-qyyEYp7mqMDU149G8qHKUMbo64tr56KgTnaJejybcgAXy-cZiX0Wjj6pEWg6gFGwk3wtZxLclElGrILJP7EUQGiNAr8qQ_ONK3ddskCsVoKOnFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=s2iExqhIbpeFy7i1CaRCNNeDW1L-eEnk_xUvE6qoiSZWgpMM9f0Gox9emIn9ihOZ3rGNrq19BtG8aP4JTCIwBcgNmAMXVC1PPggGA2h0pZ2jKn0ncau4K67QJu9VAIEuzDl-U3ShmCUoifY0KBsqiDYApE6IIP2E1X4IPG3pVMF5yldpCvtziiGy14OLMXNQbtyl73r_TynPpffmAjlQUJyuxCzatXn0oeMYVnMYE3Li_HHEaEOhvbNf9wHxQTOFiNxz4EQ4oxclXx2AMHydM2AyFC7ndV2wNiKKkPOL9nW2BTJplfwMZUAXkv9jdyEDIQAu2icSd_2uY-LA7JvaoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=s2iExqhIbpeFy7i1CaRCNNeDW1L-eEnk_xUvE6qoiSZWgpMM9f0Gox9emIn9ihOZ3rGNrq19BtG8aP4JTCIwBcgNmAMXVC1PPggGA2h0pZ2jKn0ncau4K67QJu9VAIEuzDl-U3ShmCUoifY0KBsqiDYApE6IIP2E1X4IPG3pVMF5yldpCvtziiGy14OLMXNQbtyl73r_TynPpffmAjlQUJyuxCzatXn0oeMYVnMYE3Li_HHEaEOhvbNf9wHxQTOFiNxz4EQ4oxclXx2AMHydM2AyFC7ndV2wNiKKkPOL9nW2BTJplfwMZUAXkv9jdyEDIQAu2icSd_2uY-LA7JvaoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGQuhRsTIUkKjhltcScVst5maQmzRMUVar_dxZ7pz6yuGoVptwjfn8ZdeMmRBrjLbpqE4Db77D5Z3sWNzhhWiAhJqkU2txCuu8Q7itHH1TJb0hecFvrcXtr_CPXCzw8OFJLMMtJ75a0qNkrLzWmh07uWJ9mCNsm9dGkgF3L30PdY7zsmEmJ1aqiZXwVkYOp9lYfyfrKunZ9qzR0Rn771-khYv7HJ6ELw5AnSgCnhvKjsM_5iwZHczqITRGK0rteASX8pV4P-PHo6kUwf8JQf7kGAJ30yAXf0ZFDY3m6JZhJi-NpEIyljWxaBFmYUEYNrgbVKaT3EW6ETTfhaPXSbqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCA-3wob90VJ8NcK6bD53gpYbfgAMzZLh69nI19_NV7v2MjvMv7bssF0Xjo785TElZhDZoH3xT3CLASVq3aKwQV5sVyzgDEAcZ17BDXZXwEH93IoaFRihxWiXA3oi5etZvJAP0pzNp-a-3Du-fYmPKSetsFkC0XnlHzcyC4OiGLKpGA5Q_5KqpGl14pGFs0yTQqAef3aJWKu24rmjzrzK2_ef1Q5V_aPzQbfnAB-5QZE7SgiOxRllxZS1dsIfu0LKbbxD4_QDsFlqIQDf9g0cadw_DlbXvkcDUzKHwlfIUZKA8okSUHHY7NMQKfxCU4YziX98TpPlSOOfGAWFrPW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf4x8RdlICgaJ8vZo5_SCPo423osCHBGxEBR0h1usEX45lfhRuauQRCku8HzAmZ9xFJQV-DyB5TEwJi4IxBT3ZVlp25ylf1TF2UZNm8NKGtZnSpxa7QTqUHtsiAA-AjUUyi96NC8yuDgN92LVP642JVlthHDaSqBhkcGNWvfd7w2O1VpmTTVqeusSzdITghUlyHdLr6Xu0sRS4pKTNXQ4kxTVooPs3CeQRRSB4U3D_hWoNnOt-sJFy89z8CgIlrJJYwoMqBLYSqJNpNaWSRZpQZKeuGEfgLYy7b67zpKOrEsYaNS6VG6EsHqI06rg_3ycsnlgUb8zLgK_yiaMdD12PqTE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf4x8RdlICgaJ8vZo5_SCPo423osCHBGxEBR0h1usEX45lfhRuauQRCku8HzAmZ9xFJQV-DyB5TEwJi4IxBT3ZVlp25ylf1TF2UZNm8NKGtZnSpxa7QTqUHtsiAA-AjUUyi96NC8yuDgN92LVP642JVlthHDaSqBhkcGNWvfd7w2O1VpmTTVqeusSzdITghUlyHdLr6Xu0sRS4pKTNXQ4kxTVooPs3CeQRRSB4U3D_hWoNnOt-sJFy89z8CgIlrJJYwoMqBLYSqJNpNaWSRZpQZKeuGEfgLYy7b67zpKOrEsYaNS6VG6EsHqI06rg_3ycsnlgUb8zLgK_yiaMdD12PqTE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های‌تامل‌برانگیز این داداشمون راجب حذف تیم‌ملی‌پرتغال از جام جهانی؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HN1pVFHaZjuNA5ioNQ45a7pScaKJU1AD4kedCqqI43MtqiTfazpgC3YRfE-HoEIgvEYBOOfVBQqb1RFzGnjb3YF5AgEcVvxftFceb1cgPCTcB6e95PJ0X1GYN2UE7ww01PcBHfvgayqaW9OHasNLgwebTdnZACmaDVttZCg0eWWwyqw_8zfx4n4Dqzx0cIUiGEWLlPgiCtYpmQYfER3_1TqVNJcaotBzprCRlOCydUCrkysx0vNKUcsSBiTwjPix6ah9E_LMcXU4zriUBmiA2aF5UkuLvoia5XjaR0hgMQknFxTMTQOjN2NCFjrLnDPkzBZmq_1uf5vEh8B2ACxMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxWm08-J5eJI_lgHHvHkpuf3nhSihucJCd-44a-rMVZ57XYsVgJpPP3clopKPLBMnHTdySP90BDx5SaOUSUdUSEAPTnAZIN-JKaSByBcTa76WQGXYOj3zKBPStMZKSAH_1KPv7ZP4HNuYyV08oeNxY8T_H6YLzsYLcQAAy7tPYZ1RedEmkGaOHZMuWnPv4QhzLy1-WYKG8wa6OuylCx18VB25hLB2HfljuJYB-gmpT-pZwWdvzsXfAUwghNVC5fZrpyD_1e-JSgIy6I95h62XSTpcDyNekeLdBZaDFe74n7xLVEqSsBJm0p2jS8c91jf5x4WJMcB80Zs_g9kwyUd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URhnlJcSdLPfetuHLuXkkDLyxTUzb5aq9HmxMmVjJQKdfmfLvfbftRh8YFBtr3I0efjmLISHRPolg4bX0wNXCBF-ARK3tBqqdwsuyVUGOYWbhxC50Slxn6EYZi4b9lVtt2LxATn_F-73V4mqqjLxSpZU5cpwcG7boYX5POfajj8dt2zSWP_Z5blue11hR3OsJNQpJ8f8sfPdndhdlzT0Kfz77dithALdlI9LICvO0vTP2PyYVknEwUHJHOAJYlea4yVBTp665y5s9TyPKqEFF7_AKPeswZ6Ow7ouvq7vA8ULC05XE4qPhViGxarfVuM4KKh-DeTfhAjds7IS45jXWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
بدون‌ریسک‌جذاب‌ترین‌مسابقه‌ی UFC را با بیمه ی 100% ی وینرو مسابقات مهم را پیشبینی کنید.
🥊
بازگشت مک گرگور به قفس
🥊
مسابقه جذاب UFC
🥊
مگ گروگر
🇮🇪
✖️
🇺🇸
هالوی
⏰
ساعت 06:00
✅
1میلیون‌تومان‌روی‌برد کانر مک گروگر پیشبینی ثبت کنید در صورت پیشبینی درست 2.5 میلیون تومان برنده شوید ، در صورت پیش بینی اشتباه کل مبلیغ را از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQAyZ3DFvHifq_kwoSCwMItxbA3CJjxFwsXBt49SGXGnI3TWSUG3zwSOchjuqxs4w7JzKttqN0QbhlonpnP1YCjdWXXuzUU9m_KtADy2sO3lEpgWlDxkk2hBgTWBrzaJRWRXd2eyraPcPdXwnLf3RNn_4GU-BTyJEyTRNFm0lm647-SYlrzzovW3_7mx8actWGSIwabv-Mb19sVIecYETmLgUqEI-cmSU-hsSYTsL8JiaCCC19JI7z9CNknr1j7WfWi_-xE8O24iNhRE4KwgDyeK3YoPmfCDA3eulLiD8tyjWsvuBkq5cnYmmW4A4SMxMk-ccMoZwhvEJTw3fpgWiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=SN9cWB7l5Z6y6KUHQMWsCJwpNeM_bdsIr4lwbjIiR-vsqlpDt6zFKjw5z_KsE4QHd1PtSIabZAjAOdtKiHf-R-KG1oS1tHx5-yQzKPUzsIV4R2P8-K7FUyKW8BqTZlLk6Lra0MaXhCFB35CHUcEkBMA8eNruJVw_XvqywGz9017igPgciEd3PPJDV1N1ZAkliAEj7jIPne6WGhUz8HiTiOzCI93MKmp8tUquepwbgdIHYkxSgVNC-GaBTIotq6cQsYLsMJnoQK7CP6Do4AvUObOtMAydBEu9GCt66dy1AdQFHC8WSkZ3KxaOHqLHTni2ah3LtvHpRi7u-xYmYIRKPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=SN9cWB7l5Z6y6KUHQMWsCJwpNeM_bdsIr4lwbjIiR-vsqlpDt6zFKjw5z_KsE4QHd1PtSIabZAjAOdtKiHf-R-KG1oS1tHx5-yQzKPUzsIV4R2P8-K7FUyKW8BqTZlLk6Lra0MaXhCFB35CHUcEkBMA8eNruJVw_XvqywGz9017igPgciEd3PPJDV1N1ZAkliAEj7jIPne6WGhUz8HiTiOzCI93MKmp8tUquepwbgdIHYkxSgVNC-GaBTIotq6cQsYLsMJnoQK7CP6Do4AvUObOtMAydBEu9GCt66dy1AdQFHC8WSkZ3KxaOHqLHTni2ah3LtvHpRi7u-xYmYIRKPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=WP8l70CbHIZi01yz0FY6DkNXyiNzzlr27Ag1DBq4HjGZAPDkJoM8RBAaYa_gG7YEX7xvHjQ1XUWuTGFXgkKcSDfwxk_QGZ7EdHzytU0NwzG-7PGRzdgjJIjYxsHCuG5lrsWOKyOQ3f-l5jzVvrZOP76JENZYYhakX2AwSanYlx8oi8wvvHGSrTHUJWFfLdkBH7TRPU-C9lbtf9Z0pYudzybJGw0Jj1X-Ka5RntXHWcPoHObKxZ105ePngoz-8T0bRQz2Iop6dPXLh4hoIZPURI6LIcjTRq5MQMLVoUia_Z91Y_TyRotLKMs0JPtdAxjcDYW2jhqwDt3iItsBFqwDPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=WP8l70CbHIZi01yz0FY6DkNXyiNzzlr27Ag1DBq4HjGZAPDkJoM8RBAaYa_gG7YEX7xvHjQ1XUWuTGFXgkKcSDfwxk_QGZ7EdHzytU0NwzG-7PGRzdgjJIjYxsHCuG5lrsWOKyOQ3f-l5jzVvrZOP76JENZYYhakX2AwSanYlx8oi8wvvHGSrTHUJWFfLdkBH7TRPU-C9lbtf9Z0pYudzybJGw0Jj1X-Ka5RntXHWcPoHObKxZ105ePngoz-8T0bRQz2Iop6dPXLh4hoIZPURI6LIcjTRq5MQMLVoUia_Z91Y_TyRotLKMs0JPtdAxjcDYW2jhqwDt3iItsBFqwDPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcRvtzhTSDjL6g3DeaX_O5OlfsIbnRHicgnFRy1WbLIW-UBWE6JWH9SbghL-so2CtleIabXCPPI-CQzPFHJ--a4XbCS2OD5dA2ClveALviuROl5SkKk7sDn4YDXpZj7165mF5qQdk4m-IWocut3S-HdkmgV8X6IiKqT_gh_bew08bFVX7jH1HDgSLY3PIFJtgpLt1qOxq6nQtqd78Yi6abvjMbfqgDCd21Cvuf-XSZD8tdp1NLlbc4u04Ica7J1CzaKlA6gbCZcV1AFs5lYEwh6qPDuyCVvwqnjkGuhVihTcQXtg2J-2iB-ZTmbBkd2KStyxp-Isly93E9kVnYPFKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3KiQzdppy18AbDTAka0J9tMiHRcRaEeMrWT5BehBBCwXKPIsj-511iYsZ2YMSV0RSUkbCiXJypv8tiCn1YSJPAji0h6OCU1jhEq-rYMtfiJ3Nw4J1kX8Y-qvovK2Bdjs67VSzU5QdqOd0vo8YU-KoxCdpMhlX-vGqW8Fp8rYOQA0ecZdxYwtaiux17xnPOCiibeJF-GgIM8BAVNlDX4TUoBEE_FHA1GUdEAgx4NXgEOVTWcqZTvBNt5bpSo_Hj-jrwQK99DzSWU4zym9tSQHUD8-MWLVsRFlQvy6Qix8gCSWZ5-26xGMeFRwW5mvFL4xNmhSJebalV5mqbYLCgtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=D916aAXQR5Pnspvdp0Q5jxRaFcndaddRr_VZr9JKveBv_2-hYGlX18CSvfJL16eeuzpLg7Se48_wi51uDfDe1kMBsbAm1GfQnuPOH_KcBibjcqm_MPgKhBoPZXJDT2wR-t68eGk3HKyLiKLB1GwT2rr6PwpaLLxJSTDFdxNOOk22FIbbeelRuFo5jYSnHWNlgDwv7bW5pvxExpwLngEqP-BsarGayfyHJVOzROz83ktotn2kRuo1Tbdrh6CO0BfpYj8Jn5NoxWvga8MXr_MT44hYsY01jvl_Yo6yMLJoyX8sfTL5x9b95Mf1iLTUI7iem9mN1SjyayQdEnVu0faWuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=D916aAXQR5Pnspvdp0Q5jxRaFcndaddRr_VZr9JKveBv_2-hYGlX18CSvfJL16eeuzpLg7Se48_wi51uDfDe1kMBsbAm1GfQnuPOH_KcBibjcqm_MPgKhBoPZXJDT2wR-t68eGk3HKyLiKLB1GwT2rr6PwpaLLxJSTDFdxNOOk22FIbbeelRuFo5jYSnHWNlgDwv7bW5pvxExpwLngEqP-BsarGayfyHJVOzROz83ktotn2kRuo1Tbdrh6CO0BfpYj8Jn5NoxWvga8MXr_MT44hYsY01jvl_Yo6yMLJoyX8sfTL5x9b95Mf1iLTUI7iem9mN1SjyayQdEnVu0faWuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mco08Pc5SldONw44AhwaS6VgQdH27_8bFr39qXaZHkHDsZJckkNYXjJKIhUX6bruZhxzbM_5elEpNdpy-VuRUr5qFM-wckPtFz6KJKD0iYfDdq0z9MDI16AdUHfvaBX_7lA6aXVstn1yqmCMxHTU-91yDigIXqRS7bZE3jGeb0TgYtSiBaSskpqWg_PihNH-jrQn6OXm-BrlT1ixha5CCkFNpkV-Evn13sqX2kkFH25gL221bGWWonNVk83BWvjKh6-bDo52GW1sBU62CmXiJ_m5RnpsBN1t9QwknKETwYM-asRXL2aXG1FwJ4re8_Oi1sVsKwOrlhsQxepdu6ODbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHS-9Cjd4XlDi02tLru8bivCnKzy2hpABPZiTDRx3OtkUmnvIBeOW_HJ4-VF66fXwQzxcNrqnCmkz9vf3njHMCy2tTLvA0yE8wxIRW9ajwwO3umuk-yZextRrfihJb55OKbBs0xir79cWjVqbmEwGy-uSXq3-CxXuiPz4zhLBdrOVRqs_E_wnM_hoh8bNjZTXuZ4fPgCxRUU6tlJ_iADR0-TGut150_xhx7ESseuB1nFmhhbOF5Kt73uznB7uTcwm1aQgtxVURegjkXoGY1fItBK66HbidkiGbFOWXs78I4Z4Zs7qJm-IWGf5qRYXcjeyc7wRB9aEoo5B5Fl2gmrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpNKYEvJco5t9giJoOkrPvbV96TogcBWspAiSk-iAkepusThfL6u9C9OD3o7OQSjriE0rMITTiKDLUXn9cUCzLsE6DCvILJZRYY17kbJASk7CxxmwhGOfoNQJYR-e3Vd9RrHvOuDNjj5_2cIMGdXDxMRNo3h8Hw8cQ0_2dlSlVMxG2Zroq5V7ew3SCezsMQEAJe3Cs-eBfwJr1Cdjee08CKsGMQuirgEkMU2iPZm-rBzZazeYoyrhyzRg-SGOz0e8YOzqgPAeZrv_UFpTxr8xelIYKiSnWCRjHQ7TlUU-5IQb7DgDgmYVtxOmmK-LOOxF88-jXrOXOzgNjg9MeFLzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLEeK_k3TotiAWaIh37lJOkzJ0rn1IhGeKy3NHYC8nPiuKIQun3UkOkcvqNiLetFDoNwnhC82eoRzOm2XkgWvLqTBanX366mvP1ZEFlwGk4QMY9eZi5ylxCzFTTE7ZGJVo-er8xLFbrWsVqBLCX2y6pQ2RmhyfHgCxCrh2S6YEw05MIM3j6v5dTUA1pbkQsSsNEqJ5JSCB0kB-zUV3W7EMoN_gjTZ_9G8xLRSwcJpkBuiqAuQZ1IOZ1eofEl1dsmps070tNXBFNzqjKSjhaRP7NP4z3_-mXq7xS9IJ6Sy3YWCocodw78-m0h5QwzPtLePcVzyyA20PpR1OqD5FNm9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9_wVSYXfq9otR0Aq-wdyKY5hJxsnrov_oLGuOTu-3p-0WJl-DIrAISdpmBPnYdZfC_5LDh1l_e7iNigOJLyGYvmrlvuOznE8ESaLjxOpo6LMaI60qE_eMJSPfBD6h_0QevtxGk598n04h9T3IE6HeQMIXQE-5e3rv3gN2JuFCc1ujQEBipWu4RW2q6gw_UTA4mtvEpttJTaNavDt_Bi9Dv5PDfZ_afG2bo5f-qMUo4o8K8ScDSZf7Vjs3HxBwhRodt-cHGKzVIBHdiizOF9pPCF6ndkiiFoSs4oHdZRGdkLmwRr_Kxp9ttwMODyzyfLJuTNEKS6qYyJEPsawGvz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWLhy2jbAApeJ4YJ64uzohodYYisMJhFd1Y5ug1x3pWMwl26piOAinXiaQcvokhy65L9Yv-qsnYK3LbdHx-XnVPCWFORGs1KfkuLcrUsY6lg855YnGKBVXcIUPNvD3NQqHQYU6dNdFOIgW3zAKM_KX55OCwfnj7nYM-mfmJa4Dr2vXRQtVP7nCbpWrJI4_dfJ7hFnC8tMk33hfIMDxXZKUICr8RCzcDkzxqyQbuBvI4eH4YDNcwxJGyF7Ex15kGKGuI7CuvGsyyrhWCCWoM59ROYar2xhuUJmKzwC2Xu1fqzQolwVKpQRth6xi-q4nsVirCGiZLW5rEtKZ_sZmjigQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b70VF8VytLsF1mwdhlO-GXwKozPazEfsV29Ssalq7m-S53aHe2sP1F-euwTCdBK2XwgSvoTPy-hj361wWJ5808bdkvISlT9ZVLfojPBPFsQSE--q2KWJFYw0IA81cJ5F2-SmAMgPxk8Sus6E90tXR2pzyjciVnZSi8J90J5IKq9y5gE2VUhD4wz2UpkqGwkkaZLzjmiUnSpiYisCcy09_Fh8oPU3Mkg5X4_kC5gekJglM5TVydB3E9LK1bdYm8K7qjxq4t90Q7i1bxR2BdnT8qW0VrQ1kGv-Qt0U4X7N2xX_yxEEVlIzT9mpmvH6dOc5TaiqmuLdAftfrbMW6InMiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-Ab4On1LZXPbVnE4WWP3enQVOLoPttcPURvmKlJJc3PlG4aHUY2MZw867cVVC0tC8f4gaj2_IlRI9SqxBuVZKbhQyuaWCKqES5kJJIwgmi6H9667tocY2ysRkjGATOrsSVD4LHS3_0zkLU3rEBGsqVNLLzt6pVVGJk8Qen94IRrgoHtOqnZrrIvFKfDASV-I3XwgjRM0uVb041LQ5L0HGmZLSf9cKPtalZNPw3lFD6_caqGoZsHeHeUHVYihI7T25aXKQTfPOfSIuC8_gDZW_PxCrh91kNEA1ociGKLFNgQBJlHDenEPobOyynB-xcm2agqJasSmFzY-93_Quyv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛
صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNUfcXEfdWSAVQZcVl9eE_FUrAitGgfzkrFHuDriieUOKQ2CJcvnOXXM8FkZGDbOUTvm_pn7_t0BvK5JNfOlJa40bPdu0jl2eqs1tPkHcctJRx8M2kZgjnkQ-CJgklzAOdOzSiWlom74WqvXt9wTu-k3r7UIL1nAES_B1luPbuIY7PLDpnR2fyGRq5Axt2Eg7_dX9L7GspleQz1P_remhGX3cMCfm0t0-9fJM295LRbi8HD2_ghUQDsGIc7XVAG9IJIwqCNVskc899yY_cs6HDLT08J9ojQg4zTK244Q5OmLz11VL75x7cVWs5X2fqraB2KyBUzmns5Z9QVrG8yRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmk1Co-16RvXdVmx0FwWm6cMqXCAeQ0yJbcuufuMQBvOcumyCzfbjbjRPQJq690jx0axlXr82UVOrnik33ID00_qhZtMnmIesytyYcDqkjSAZQaqSuI3Lsu_SubJmY930AhtOo9uLAt0MpinsTO1TWisUwU_8RJe6d46A-hT586n_fWIYg7ySTdgCdzBjKwgrh_QuQonkNZHES7ktiDXGvf2BLpIkhlcQp95KKATJtIvuexEegr6zRZjHLkphNXl0t6WWMbYLxuMIUYrH5qWzHysFHrFncGn5balqqlxs6jr_WwEwcF7u7nDcn3He0VpsDBIbwQLaF3r9eYZtwcnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dHN-F2X_FQ1QU4E9VuEyqpxgVpJfeNLbtexLY8SmnyRx97x6bs1ur3XDvHkHA_bq2VLa2iFXvKNC8dfDBQIJOxV1zDNWOAyHgWsKjendezvVle-iXRNEn5h1RLZEszNCmvSzx3TKJWiw9isKtKHvxq3ISbYGlvii2EvyZK0Z54ckte1c3IW6jRXhbWNysuvNUQ3Hk08hTFihrOfFVVeei7NMlyBAVJg4sDfIYvjDBenOA6Kq0q3l2myHOkOHKxJ-qpoI-4Zi0J0T6ARuUIu1VdvF736R5Y_b1masmRBRD2VVcz_na36j5RK7TTVfeb5-Bo8wzNYsQyedLKbOc10sUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7Ps3yMOD1xTErzCT_kD48PC4k8xfQ1aZM5RPUfbKNXNwdxvkK_5L5vpuSIX-sN_fWsyGDrZYUKLapgBjW6XAPm7gD5WslQUrnsSQQ8M1F2a0x07uKbmwn39mRuocZhvehIlJy79e0pNlmb0IB4OEqCz5geQ1s5KRyCWxLSDXUVr56zrmT-7U8qljHR2UTkZEFKv9xqgQsaFr4PuvyiLzsrdBfmal93DnGyp5rCAvkz-SEDj-W6LAHWCqRUeNoE2Qm7SlekvTs_fFvoxskTYe-rJ8uMbOBCjAZEHGtWzCEENRBNLzRkoVEo-xpI-RZmx1ZJFDcIH6pr9OYZ9SHFRag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HyleY2G8xDNj9JOkNi3cI34P7c993TDX15X1qG8RJV-brYghQ1gN4fSmi_BNden64W3MVKPwOPGGRJYf6j4qsreClVHNicZQsKWe0yfsKSz1ezjsEpAjS5OhR618hqwOP_ixHvxk4h-WZcRCQ_Q4E6K5offy20KlvgJuJMgW6IaWndKjg5gSK2o1dJePgCuICNIvEoZSRqwO52NgzXZ7kgFP6D3kFWiCaI2C8GC3TxUwjIKZEJoen92xDCh16AKexLDsfzScKz88_dkmzNdcImTY1hU7L2Dvdgc8ecWvktM3rZcty8uPq4SoQ6t1GLp8zJYsdAk2y7nC3uBLowwlUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LCrRuVbv2EHOJovyjWMOr81la5wMG9HjZXFGuwedzWKJSSy0vuuuROqAgw39IQajNbt9UvXwEJu6SvgwNA0QI_wTY4qhPIm9awS0LNKLS7QdRmCeM4mRsI8mQSKMH6OloynKSf6MZNKuPzmyT7J2DY5bLMkFJQmUFjtGO5Z6Sa_5S_2NfCezAfokNLjrrHqvXKcJI71sc1MdHdvw00HZdp0vEDSvQFJMB-SnvAYM1TOZ6ej3mr7JWssNUZXDR0BAnGVvU32thzCOd0kjopXTmU_GPSB1O1Bdz1VL-yX8ZrMxjesoLegp2uoFaV7kxR4IStPjsse_pUFsYIAbB7W30g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCec0u_9AMX25aZVbrm1GGJjG5vZ6bYsdWFgO3DC7q9QniZDWu2YaKXSSWEZLR2UuIuQRfm-afUYBZV9ptcAUxIdnj2fp01LPTYgv7eyTPdbPS3fnJfjkevZZLzC6UX2Ey_TnosKAFwITcomK_mmAhhrQ3GcZCX3S_rAAZP6ZogXuYkK10D5UNyCiVnvBvsvu__B5WAgchZoHEEhEXmE9yvE2ZGX6t3zZhKREwOTwTB0tqvCrihE-dZSse9JtdBMImOReiyCBEvM9d-BaJI7_zduSoIsbrH9rLT-oiaQ_cE3JDNqvEZ6cfqSb73NJz3OdRVJwEEuvMsnwpqwX7NUOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXGGqS5fRuJX8EAw8j0dtBca4im-jlIFb71qU-9TTENEcV8GsNbHIZvQtuoi6Rq7WL_4qCWiZA8a2OeaQKNQWh98w7L-y-dYYQ9kts9MJP4GytM3_4FDpyggdV1wTW_E43-Art8egr9gihQgK7j1K8dx7t0ePKABZeO8TSY95p_o15vp43i1B5kFNrhPUSKoSxM8z1yKBTh_vFOqnl1nFnKAg3tJpwRWqJU8NOelzjTy3K_0BPndEauaWUi9l9e-bX_mowVoAAP3kMu0ykwiOjJ768ovDJaKm__e_9lrGEgCe9IvAIUN70idr2WwOASvnaxJ_yVDlKCU0ulKW91_uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSODkZt4SlGilENi0t4e2rdfxhxrz3pYu6tFrpANN-y6aKJlrWyf_aWMgnaVTH_qrjc_FlhnjC8jEn072h9nCntPfMxdn7QfiIDxYMF9igx_Un52_X8Ign4eDJa4St5q9rA1zn8fijXGDg0tACHQwsD1YzhhSR-gh1iCsjKa7jnY9SAXzy0qC60EOyheB7My0otXGpsq6kyZJUALDyuPZSRGCMpipcFqHci2mN5kNZI_E-F6MpSWsQa2LXZnBhlIz8bwTQVpSbmd4QLI5uN-cQGIsuvT-mBT2PLDSXsP1wag_xq7XfXW8-Vfmsu1r5pW4KNuQ-eq7qoqfIhC2nP25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Utcep6kMXlcq0LFHL5jLv4l4F5CbR56PxKJNXq1iZKz4bfxUtB68pGaMFsFe-xQVnkZbw9YTsvIfwTzrr5qCYaDK9_kFdYWw_7D3jFy78zGBs3f1YMEaDiMfx29QoZIk-82UXM1QpOVOQ-S9o6cKPp18caCfk5BRVf-XTQTeTj7CGqX8w092OTZLEiEynRCzUl-7Jd3uj2KwbbyiksO0ZHoyPlaskjGSXa4T8XajCmJOsWtw4ZQrvNjY6AaDdKPp5uZz2tvfX6v47zbshaf4KeQnEjtUs2dNJ26UZBOyVHlboj772GBvDHVzq2NpIF9-PuuCrBdMwqzXNq-q7fNFkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPNsJE9-4ZPiLJaQgkXNtPNa0M8wEDlxVaThhwMUXe6g3z8DcnaPdP53Li-L9TFQnBXoW8RDbNeANIdhzIJ7o1BNYYL2dIecRRz2Uy6wrHiVuXbBhCBjOoJHdwEyzsfUf274aL5-fjYi-nCLWB1iOJh4sm6j4u0mhtxkaT1mahtsMFu8T-sCBXesweJIccfyKPiVRzD4QeqorcvrQgXTzqQla5vBYxBgJmHpACna8W8utJiKRWH0sHyswIN2-Mz99mkNPso5BQ0uTuzCFt_GhJd8gatRuENw286PPxQDERBLDdTzs6rKRYEg0hWAsxGaBrLqpnN2KEirgmeC8J-KJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZY-1VOtwQc9kx2fKjDQMgldXHg566y7h5kA9DFOg1ztcJWT3iCjeugV0gGpvZT1VuhnoWR2JQcbJFzzdaqSkFYWq228qhdHpXm6w-BLIJ8uzcKuwKB_57FrpThYAmPq9NK9YCQhdkh2imltreX8Si6zudusk-MtSqGNyfAsm2yV2Y3NKzpEIzYXteJ8eqx6Vweh_XFzHqbNxA59BHm2QQ1I-Zy96nF4-7kCaDSjjd-jghVeDeBCE-zFGtl3sEIqMgd4dtyAUcr8ZoJcXsyYzc7wUMJQi_CAPh67Gj1p_FQOBI7afh9a3ZCpdkSe7HiFtWXkYCGY0poQGbGiqQeVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFHEpAcBFuVnImKHCQUwo_1ByYJHGIoHLppeKZj3h7-X4EYlRhWbtTzHJtFEz9Q6Jh5x0z8__DuNIMT5MdIl8XBVyjkRtii-j3vqXGHnciqA-7czXB3wroGeQUTFWPhc0UwNRA5fvWHs50Tbnggsje6A9tzDvYtzcsZTXwSXyq_UBp9GXENCOpIJQLTJHhk1vUoC5eLWQzI2u8nBThj7mumKQqnaGTVhQ6B7PF7cH67rKXd_ryg0u0go3t22xFD1wanp9M-gRf1wL46-fweEKvIELV4f4erNECX-xN_9GGpan8FoO1bxQEr_f8u8Mxbql73aIZTuddA56di9InssTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRtWae6PqSlJjC7_7AwLJdpBRKz8aswJ73KBHG6gZfJL9_1eqNnaV_b3d4VJPC5aT22Cv2WSzV2VuDCM82l9ay9SY5Kr5Y5eD6JbxROJyyzJ9AiNSJal54-9ly6uCuRZkQPq27aR8Anj7JGRr_nDF6jFQzuda21vsoB1crcKrYf4uvP-IiuYv4uzP8ASpcES85KoCOtJ0O9xMXTpGIACkTfvh58u9xit8w6rcMnMw168B_j4VQRxi77eUiUlzD57Htq2JZcxfFQmTLXQ1sVkcuIjqLEk8tqy42ETkI-BNMuV4XOpdG0dICr4xDEj7qyLVphgDG9f1ANSeo5eAUt56A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OedxEkgG4TmrEvM_uCupeQbIDQ8pSAn7ueduvLXgDbsFsh-0o7q9QzRrV1hGsYWWYa1wYV_HtiiaL5iQjv1tnM3kfrS77j55PLZ1FLZwLrQTSPAPBF6UdR3Sr1dVyhdVr6j72Za53V6UPPCsJU2AzyvCYQuRH2JQVlr6rJ222VtBSenP68hNspb35eUmCkBqzLJd2NDCz9CeK97-xxS42thV9V_TY4Z8xA2mwyTgz9n-Vr6gVmxVug98dNVcMVprU_qU8wnrImp3gMt52cxZhFFSuUJg0erEg0MZP0gvVSLkGEjvxGbWrWO_rPyxdBpX_TMGWRgObdpXj2xEQUGF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYDxuy3Jpye2-zNSC7PEz91VQHiAjhc7iwAqfrHJ3EX4SwqW1dmQQYFCzlEqTq1m9ZpSa8WKvRovgSs-RxOkMuzyPWTmssF-OjStpuH3HEMAjUqaqJGvjp5bOHIvffp0YoVE8g61miQQ_8Bn7_KSvvAwAAay04jNqq3fvYDKLz8iJdhEag1ox4sX-XZvC7xQhD38hyjubGgXhWM3Zvo1H_PCoqP0Nj9LcYZA9cBWftlZx1YFf43NJIAsjIYDw4Wl1eoEah5POp3IOzpoXPvRHbHViXB5eY5LJxryF-UfFaxPaptOQikDv6A6sjKeo_OdPvIZh-d0EDHFnA4WWp_Lgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTOgnr0bHbU3HqyvO9Xvb2xWmEuQVEz6pOlvFlSkSGgNOR1KjW4c87h-D8-5WzBKl2nunTOMfEMPefbEj5nsYxSH7v_clNNlnpGaGGnJbWXKt0rDE0pi-hcovELr0roKH1kWJEXKTnnHtPtsYDP2TGLATT5-OYmvPfkd1P4scqaN__L3JjBAjIHny0-JHEyEiup_QBkEQLQ9k6yuKP9MqVfepfyol9k43GIYakEMznM4dUAUWY6jBzu7a8o0m7VYy_pZUKNH56b7-c5kvOPHv03H4bQ322YNW7b_Qfyd480DXDOi-KRaFL3lg80B2VMAxDGwyP-r961AWAn0MPc17A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری
#اختصاصی_پرشیانا
؛
انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت کنه و درصورت صلاح دید کادرفنی با او قراردادی دو ساله امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVYAFZ6qDm1WmbTMWTZ_pKvAToZdnSA61MV_-DBQrLAkS7Ykf0enfdTdwdRny9maBdSj1Abz1bQyYUnMHiB1NvGfjmuHr6U27bM_S-jZyYFSWYfFdE-ggzhJ2XgOkYlpTBVAaLhHucETLJwcdEwSS8f6b4ygtfOWCHwcuSWDS0EgwqF_nvPztT6B7i3AMh5qy83dUFSSIeuNgsIxEZg22zv7SnIpxowha6m8_Zf-H_1ThC69UKcouWXLpWzngc-QWvpE5zWUtLJHSlVqwHKvIFrVve8r08-nvN7ExUNPc78W-oc9wEpO4v-dGQeIbKAT8x5nTkgublTda3Au87VTxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmL1Jpn4fL502OCMv8LJcm49_GO0UdQYAKtgo3fuIdR9MH0Ci2BgzqxRl63vWD9ltEHlvLsK4JpsquJgcfB0gxn6EUERs2EsjNvc9ITf_VkbtYO0F6P05A_w8tTG80fjG--2N8S1KcVe2X7p9xhdrIHBKmqegtvgzt7aHGjcJ6Da_kjK1-krbuzpXcrR99lTu_nFvTkS5wiIfNGt0CPZnAr1uGkYS_9v5UdGaA3-7lDsSwLkUpuGCoBKBf90CYD1__p4qmig_9AZbSMs2NM0n4Q9NShkqq6Aq8CuSUb2_CZKIaU3CnSzc_u9y50Xrv5SPa-ftZGW2_0gtI9ZUouZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhc6iYA5mGRmK6lVRMIhZxTW-E0-J_ziQYmvIsZkUtNkfn5iUXM4mR84S1YvEQfUkOCf2R5_b-n83Pf5y9J9xVePoeVGNGnnNi2agIXuz92h8lTxS6vw6JgGe0iFq6rNWzXtVkPvL6YJW2AnhAcX18eIfP1V9fmnZ9-_xast7WUkcvSjqBxFhC6tKdkRlbfihtrDF2-kA2KDcIqao9fCfFmwKlAInGK90oQuPi7UsrCJP3-DmJrAoRon3G7olScQZ9hBXt7GA7KKSzoaylO1fzOv26LdBI2I5cuiUPTB5keAGKFgwRc68l7Ixm_V9XZsSVeQyFgqpJ3ECLLBO4JcYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB3zWoN50iaazwAHMefG3OPhnaaXEGiY8h1WJvuZSLHL-K5S9ew7K8R1oz1djlQvlBaJhgrYrMwiqt6WsgCyRGN7E63SyGnRiobvKF7BhXdK9qsPtwXoYamf84ywN9Z-KoEr938Q0kZyY6DXnpCXXjfq7OOkTG3XuVuwxrCgZ71lF0UtlwHoGOxK3FYGHG5Ym_aFFJroyPnuvZUfWCH8J7H2Jd5brLZLS2aBeg10NcGhw7HCgFxhnpdfnDOITXggrq5-PfxWpNG63D9CRyfHBE1LyLG83V0JeFWUDnPmSyrZ4CN4JG48kRXjQZkCJvGfdVpktFupNDm444l41Du4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25374">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6L5EHg477duMLq8xqRwcka7YR-L-8aNVFQu2TqTyt4e0r0OzjvwL3g4DSmSvhB8prKkjtHEPNxt2WUEPZidjWYCxJeK-fHdOSc9H1YuzA5rDfG5zHAumeATQIM-W38rTDF1U4IKWkVJTLQAnBb9HfOW0QmljhQocqaE6Oa9l0QsJWJco5MPyRp4vZy56DqSk9Nl5Tw0OmGnyBRmr1GbQ8vDUx291MrCCb3vhwFN-3Eq4Z80SNTbNEUT9Kl2_d6HgbRlHKVFzWVXMEfR46ubtjzun8H9fbNcvmlcX4LR96riEEzOX3Vmj0GHN3-vLe5TEclTSDqP5RYcgWnoXA06Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ ظرف 48 ساعت‌آینده "تایکشنبه" تکلیف نهایی دانیال ایری و پرسپولیسی‌ها مشخص‌‌میشود.باشگاه نساجی برای صدور رضایت نامه 500 هرار دلار خواسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/25374" target="_blank">📅 19:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25373">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=OVTs7AcO37yaclS0ID2QVaXjb8sb4H8g6uNZNXNTxIUh-di9mYzPo-y5MNRFOF7vJjeCbmW7W_QjZ5-MUpJ6IIqg5UGCGKrBaMIDC1oJEceu-k5gxfnVbSb_7UA71hL0Mq_CELcRwy3lztb46JZ__wXkqUUjEQ9jRoJ4PqHxXl_oIKg7Zl0U0xS9JpUpJ8LrpORD1jrEe5keAC7lUnaRYOes5Yar_HASnViAoA5hBlnc8zUPeZwWbDTsjXoUY6ZKOIu1ukPROnZ95AeWO38ovrTQVVbZ_kKOfDsNI0I7ifMvYOyvdnxdxHOsABoMh1C_hHaSS7oB56hxMipreEC3hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fa93e8bb.mp4?token=OVTs7AcO37yaclS0ID2QVaXjb8sb4H8g6uNZNXNTxIUh-di9mYzPo-y5MNRFOF7vJjeCbmW7W_QjZ5-MUpJ6IIqg5UGCGKrBaMIDC1oJEceu-k5gxfnVbSb_7UA71hL0Mq_CELcRwy3lztb46JZ__wXkqUUjEQ9jRoJ4PqHxXl_oIKg7Zl0U0xS9JpUpJ8LrpORD1jrEe5keAC7lUnaRYOes5Yar_HASnViAoA5hBlnc8zUPeZwWbDTsjXoUY6ZKOIu1ukPROnZ95AeWO38ovrTQVVbZ_kKOfDsNI0I7ifMvYOyvdnxdxHOsABoMh1C_hHaSS7oB56hxMipreEC3hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین فیروز کریمی در برنامه دیشب شبکه جم‌تیوی‌اسپورت درباره مربیان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25373" target="_blank">📅 19:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25372">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlnr_QYzb99SJh0wEj3bR1BPI3kRt6Q3dpx2ixiWodQiYoyfL-dba1NnlavAAtlfQsJENwYSsoZSa4wsEPKpATuhKFpyjzZxCbD4RUJeM-cxNMlShn8Xudg3qHujqiAnRvHh7W4Ps8Op_BJN_qJj25OUXyOusxHbHu7-Teaz3KMMGZ74n82_KaQg9ZkObYYwkKOLFU-g87iv5bQFFyaB3B9Oa-UcMcJE6FH_ixlE5doxLyW5euEVGV_I0L5mwcTpZLrR5YMBQN8iINcunZbMbyDJiHfmLPfbrHOiCv5nyTicU9CAcBEUnMBuQps5xbZVERi2meVduBdJwjXSgS0X2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25372" target="_blank">📅 19:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25371">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSdBC6m-2j4S_km0OX5_V80ksRnjNSTKyr-ElaK8UF5DhmSeiiDjSewBxjZFt85DL8vfZcCSqPfiX_EfnLGuEWoGtQsgCet_reEZw-JBxvYoYSJGEil6ALqulkT6EiOEOMI3BsCLlvcvnyQjBug7OxphXB7ZkT6gneoOOxGzJRnwPP_Iprh5-5WfeRIkw0QjfjpUFDuRXvH4f0vzeoq3QeLqKRL7-nMx4aiCFX6c9RoAWH0frmdaPMgF9wqACq9VPA855jaNXpKW_DeTp8etRc8wsFNWI7TXiRKeIWOlGtOBUe6blKobhSRo-_Hp6GHgaDz_GojAThzMYNKWYXwKtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برترین‌گلزنان‌تاریخ‌جام‌های‌جهانی؛ رقابت برای شکستن رکوردها همچنان ادامه دارد، اما فعلاً لیونل مسی با۲۱گل در۳۱بازی در صدر جدول برترین گلزنان تاریخ جام‌ های جهانی قرار دارد. کیلیان امباپه با ۲۰ گل در تنها ۲۰ بازی، تنها یک گل با صدر فاصله دارد و جدی‌ترین مدعی…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25371" target="_blank">📅 18:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25370">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKUFeqYDEMUVnQ6IPrnmD_ZjNkvEEICMrjTrasUFVuFlF-IKWJ9FlDbXikGhHM3FKIqgkpNOhIeh7tjJtrSFAP7-HN_dBO_0iXmD9mhPXMlKIQDkXwaOQA8QFBdP9SI6JvGw1X2HkAtMiKiBcxwC16r9_o3ixz3Yh0qIo9hRoRp3ac8khOoVEIjzhz9MKETFnKs3EWajd4CsanW7XVz9j1EXj_SkIPAkkqeyRjwyPp4E4-PXOsj_kjwtVet3ipM_Dah42ZTjPOs4SfYattMmFm88-NsWkMfvggmC5e_C9CDjvD91vhYHMqg60BTQbQKWNojNVNaSh1eXe6WjKxsMpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال با ارسال نامه‌ ای رسمی به باشگاه ماخاچ قلعه خواستار جذب‌قطعی محمدجواد حسین‌نژاد ستاره22ساله این باشگاه شد. آبی‌ها با خودِ حسین نژاد به توافق کامل رسیده‌اند و تنها رضایت باشگاه روسی باقی مانده.
🔵
باشگاه استقلال به روس‌ها…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25370" target="_blank">📅 18:31 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
