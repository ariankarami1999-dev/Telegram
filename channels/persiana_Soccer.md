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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 03:14:36</div>
<hr>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcR6_mOgBqhmIbQicjw1J6gb8yD6_gpOstgH-R4PTvYY094kvb2PiMrh3Qi1zbLUxFF_E-Fssrk8PBC7fxZ3FkLy77teYRYIW8LIM_q60vhVTy49_2k29bnuwdd8ni7frxYV-iRCNrpPjT-nX9wu3192X21NnoNZdnvCcj6ikypz49azy7tTr-q7amkCDdnMrGgHL7O7k-nyz4aaLnlbq2tkmAQ-Hmjh5HJjBg0DMGckJEOu8i8BYCHFUAYso0zmt_pLmClII-bTOVePh19316-rzJciX35d8v4eyKAR_IG_mvfBgPBHUqejUqpsTLM_stajbh3VXbCxaXRa1HicCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش چیشد که به این روز افتادی؟ چیبگم اون شب به جای درس‌خوندن‌نشستم بازی آرژانتین - سوییس دیدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=v4FSpkFmIDmJloFBBWI-DfWb1b4OiycuwJJNzWI1SH0DawPexdcXNQzapOxIl_GqwqHKGHrsbvjKu6wmdOqZe08iup7inWYfkYB7VK7ETRjV-DAhnhR6F0MExt_Jusv3ZJzvCJLpQ9Iut-vZ5ayCDjmfkmd-QuWVY_ZmWhtv1xBibAWuYpaFjmcO8lF20JI1f0_7QekNHS83pKmtHO4uHl_3QDnE0mznWs5-2JktOBoYoyDo2XiPn7T9zMZumao6BXcYv-u7tijRrdKtbPdfWMobFp6vAW2VCLE1-BY_MivBG8Oh_Es8yeLS_52z-huAUIVv78zrSqPvYoyNwVbRFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=v4FSpkFmIDmJloFBBWI-DfWb1b4OiycuwJJNzWI1SH0DawPexdcXNQzapOxIl_GqwqHKGHrsbvjKu6wmdOqZe08iup7inWYfkYB7VK7ETRjV-DAhnhR6F0MExt_Jusv3ZJzvCJLpQ9Iut-vZ5ayCDjmfkmd-QuWVY_ZmWhtv1xBibAWuYpaFjmcO8lF20JI1f0_7QekNHS83pKmtHO4uHl_3QDnE0mznWs5-2JktOBoYoyDo2XiPn7T9zMZumao6BXcYv-u7tijRrdKtbPdfWMobFp6vAW2VCLE1-BY_MivBG8Oh_Es8yeLS_52z-huAUIVv78zrSqPvYoyNwVbRFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSw_7ia6wdoDUhipFnvN1dGrNxu1MOJYnOfG97df1_-fYciq-KKpVtSMirLWANvpzGLmQvOhGHVd0bu05FAlEUh8lhsl4qgUlGF5QdvJzRT8OS59y6yhrFP0ryKKyLAssKBiTKF0EuGtTYaNEXsLpv5zmog6e1po9sFH5RFNCQjTNGI8PkTuRVAaGBHLl51P-MavYLrdpuxvesetdpyOd_JkhfioT863cuVGsYebf0Nzn_y2f5c-igV0mDlbEJkl4df5si5zmokNoT7d3SS7tHR3P4udBcGVtH1bX7dfliFe2DTz2fe-5bWocjm-yJSA4QMuAGcSCoVdGJWEcmg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyau-GVGPPYT5zwCd9GpQN-Wzq1AWT-pJ7f2Ypt7xqSOT8-S6nUunn_N6MgipbR_2vv0Qjdl9v-0YcZujCyglkrQIiPr7uRhtYNyY7z3Z0a-BKe00msi1svcqQjGtV1y7c42GZSENiEJsv2AX36Fgdd6K82bx956Vuk_VU9jhjRZJlz2jUmOtwwWIukMgiiJ_YIRDpECbPzbnM1WTEzhKqc5PgdKmf9lddXHATxVLhIuELYoCAp5PGsHQPv0wgbV1K3MTfFYct-0zDu0gjggDEj8nq8i6NMKIFFGVbjToAJC4IQYvlEK3p9JKh7xfUxaet36rCiuiChyY7fzPZ4zRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTMYrb5y2vmy0VPc7GxHXFkC0s5uBUENqAMif7uLEME7gkQFcYOXQ25d-gec5rfFZFhOsvTmT4FyY9S3fhZGxN38cIlfb4nyLKzD-EQbub8dPMt83z569JGoTTz96EwNJ7ypcJrhBB9ZDYScypyw1NIvfSU6AZ83W7-6yKaEd8UdkMcOCzW4mjDx-yIDF9OpXgY2fNDpvT4OFMGGU_SauANIi8bXlxAdsbexvmYWbPGSLuy4BE2DCy1ZcJU60xdL1wHxIvtoxeiirVwEeYtj01jS4Ni5NcWxaQL3K1bLvrkquYMrDjNpQ2vzMb8bliM-K-pT87wAZsAwyikUHzr5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvgjxT3aZR030Mx6fJoAKp3iz5PIP7jedz26VjyBWINBGEiIREO4nOfzSmgBv9iD2n7FJhrIly-ZhitD3Un0KuPVIK-NKIemucz6yXSELLStqNwSENsALnlIPIHmBvj0N7fjEGW9niuTaz7sKsuROcmm8Ifvf-5z1jZl0JLnijVESFsM4wufGXdTV1l-kMLapqvqHZ1cneybmCZWsRrlI4W86bC25C0EpSueVFKT9junY18tbm5XnIyk5Qkcbf06BnYOxTbX97prXCr54idCEDCb0Fj8VVo5eSmurwaEZqA6BZPzeuY-QutJXYs__8En2IHbLVFYJ3FrMFjXsspfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQk1jGRnlsm-gNW9PUUQakEjOhdFUIDNISjrJgL8jAwC3qmAcKs0188ZnDJ2mlx6OZaLXLxHkijDna7YjW-4AJ2fEWQT69tVgeTIR_uw0OLXzMnACRDgxFCl9zGTPyIhz7JeBoT0ZnUGf3Yf4E-XLK30foKKFAhzfn_ux-cgkf9PxszqtU6yX9gOLrk6UFbwRa3lDUZndDY6vn9I7IdtCaMWM9IgnZIABAAH_B_CB1lsFKX2LGAkAliegH_ajBQTgFUeciQ4zgof2xn1i7iJOuywAG2brDovnr1bIsLBHtZy3dvFjOBovvIvDStxr9z4-ZhNIB39x7UfBonfsMvJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ieh8r97hnYKrRgz43i9Hdz5hraqt66RPjK1T3fnXugxntPCAc23WDWj2gik2G9-DumbFrHbxeK0Ex82SyZMp4RKD__Qbifavwnv7UfBtuwXcjxTEFjXsgxcV9OL3nCVJD36ttENDBRQJsmSERyjij0Eq8ZsEd3Le7Q6zXHO2Ie2A2oZZsXtAfhwgwnlJXKXYB_M0XZf5xVtRikjiya84Q6hyo0AAI9kBqzigvcFUJuEcXgFCT9wGOkwtgE3fQtUQ_G5KRmRQdW-JqCF15KnejFiTHkQEHsPRS6PVNP3SMpA79lBi-IL2bUm8pHSEwxRADlMA3Yk5zQD1w234AAmwBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHZiwdDkVBa6hFMh2GkrWND4wi05SNV0YPALq9sAPRHOup6drqcKykqh23yGLwCz_RFKZNtXyi96cxEcnY4DZ6tpfwPGLy4BpOsxqa-d6X9fRHPy2J0rwGRgP_zxiytS98ofeWcW8Y2IoNMb8cKuz6P3_aJ_7I5T1GYumTY4YcFleg-WZKQRQXkSHuxM2USxw0R9diZf7N1Ia4joGmDXPhqJA9_QVrUDpRUAmQmHF5LsyoRMnzcF8_Oh_j9UAG_RDTP_hPVqwVoHJhHHZphw7lFRYE8SfxFq0c3hVhzW95Pr-R3GWynrnaVHklo6-rNZ2iN5qPg59g4ozQ3PUsnPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSFibhxK1DfNTy7oeZWx_t7esT9G4V3UFHNiXApyuOXyTulG91Ud1E_kTk7_UgfLKK-mgn4QsMuDrd4iXEmzCl4tmXj2N0rISBwND2FQhCvRiAIYS1cBTX3DypU5rgxFguswNkzBVuujx7JazysQXtTeryGWEMLiYkE_iGhm-UvfHhg33_pHRHuH9OF6NkPLXY5bVL-PbRKbhPz15QhYcvn0-n4r5dZEncVzbBIN-TIm5jgBwTiZLK4f-bRRmrj78qxchAkFaGaTMW5AdN4CLv3FMM4MswYV1f0nuaBRG3eVNB0RQ0U2PBvUAJnXdwBJf-K2PKPn8icVoQ-3wvn_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rac2itQruu8G_Bdos62hFBt1F3iFHTr5kCYFF2CB8AePqed3EOmnYKJ2UjnPqqkKLN7XIJsESFIZG8BGmu1tlsiwnfc0JCsaqTjlo3UL9CgPVONj7YrbDp1mjNn0XUtRLBHTKGOnetahF1hw1la7gBPXY72bGoG6EguMPX49Gq1hF-7WiAWO2cAdbZvkA5hLRs6-u5dYG-F5B3AYwiQvNoLKSCzigUHauq3Kmd7__RJvPjw4N15bA1xWQISDdG8Pi3Mm6z-igTjy6gY3m-m43Vs-vZ7uTN5a_XCWucWCx-iJofeHeb_GbB91Tea5vJ6CV89ix6N_Q4zKXBjiDsbWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDOUBhMRhEQiEUYEuw3-AtBwcH-K_96V551TXnipRJf6NurUO6V66VvoS1xu3fTIaQpYy0buPauNZjqmcrqtgBKX8QcUMlvZZ2yiXYnXZh5BgzEC-3o2GrooZJe9Cak9uYidk2vNX4Kn6Kus_VADk1Dh6PScuhkgiQZrNLrnqC5ZU2V0Z5XBw0bKA59VsJjZ-K7mitq1NHGJE5LIz2909ENWz0D_AFR_eZA43Xg7lAt_5gy4k6e3sTv7WOwSTOLIEIVxaut8__GedmSnxal4JOwkRNDSwipcbfumoCreT-eE8X0mkfO3Z7F-XP0A75miRIvKlnNiTcXUpGocE9cd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2t8uD1vQ1slxmhdwC1fgc_Xsgl9g_sCOajMhTDSrXAIifv1ySE6UhPA6MvX5gk-LiZ8b1Ry1LSu-wEqrvmTz-9iB4YRmVFu2LjwBUcDCxQj19qkcuJcLQvvkL0QSsHcYPcwXXI9PaYaU7kMkpLeov_k0HHJgvNb7mG51GUhWWAHhXnzA2JvU6wfN0NE99K29-S7P5hnySNC7H4RaLrCKnF4WEsvkthDMqfw7vq68So3aQKvsDVmJiTv-Vl0u7Y2D89yUlExtod9YFNy2wYijMjYHC4QLR5-4AVIEVSZnfuq5iwqIl49hWM6XQXY66-3zFXpPt8VO06pBCok6YN0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C91RQJHsBe5o-4_lPfQFPpBg8Vva4hYDwm2aTRcr93qJV53LdHLWbQxSx-h6FYVe6VxApfkOA8TJVYCA3ynexUJmkxh8oxWonDNuk_Vqlgq9vwpOz1DesRUwwrUWKdCGSnqDIAn2h9lKy-fdJL75zOp_wjWqs5Z2w1l2T50nqQQzSfRajVlyQk7U7PNsyCoti4CzsYMsp9EWlcpHgopMIM6vfOUmXEF9rIzwa4oCi-k3xKO0_33SFZgXfqk8kWXzl9MQUfJe5CKRSu83SfHzfJ1OdU_o7qeGpaee1iXscrGBzK0G_G7mjrBFw8ofL5rpDpyuekQxMGzlWSP6a52mMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=jAHr_vbbcRe0R-bQ9TB4D9lq-lVItaPv3X4siBRijnrvapzPJHiijROlmoB6nY6kKyX1qTTKVnzhx0DJQZAKuLTV47PSSjcmKlfGrv96sX44N6RkmbTE_P6e-vE7ZMghKiz3-skqP5gBWNlTLophcM1nPTiAedaXFRzNqQ9dDp_l-Kb1Cm2ZVa121HbfnQXBQjJP3FW1ui3c03tmfobkYdhVLdmPHrstWIFYOKxVOb5iuT3GBC96__L40qcBXUwh7am88QCps4qDecpnePNuw55G9ZDQ9otZ00sUgOy7MBIVDeSsrwgJLHaE6iBNFuePVTVdURAyjrw3EqNnzNm-KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=jAHr_vbbcRe0R-bQ9TB4D9lq-lVItaPv3X4siBRijnrvapzPJHiijROlmoB6nY6kKyX1qTTKVnzhx0DJQZAKuLTV47PSSjcmKlfGrv96sX44N6RkmbTE_P6e-vE7ZMghKiz3-skqP5gBWNlTLophcM1nPTiAedaXFRzNqQ9dDp_l-Kb1Cm2ZVa121HbfnQXBQjJP3FW1ui3c03tmfobkYdhVLdmPHrstWIFYOKxVOb5iuT3GBC96__L40qcBXUwh7am88QCps4qDecpnePNuw55G9ZDQ9otZ00sUgOy7MBIVDeSsrwgJLHaE6iBNFuePVTVdURAyjrw3EqNnzNm-KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3FdtNyarYvNaim0QAkpa-Bi5YXq_6ZW3OpnKTJgBoXdKMPjX0Wrx1orowB6815RmOR5L-b-bHLJlOZaHIBx9DTkDqZ5qijdCz_mUSlShV1SKS9urdpOAJmP8MMMW8hkOeE_AboDkskEXrdQwoP2JD2pYcgqsrK7dd0ME7RAr74LC4l3bIxDsfS1TXcGHudGcK0zs6BgK78sR36F1m1q7vPcw7mhHUlA0W8VB-L3CRlDsWl7PcBXJ87TgsvAVMKs_zCtQsadEwFEfyrZhi7bP-M-FKABmIAvPPGkA_VYyW3X8rTF44S7etekIT4vhljzGeX7BKlebgiex2w91xV4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIhco7KVl0Dmj-kO-xFH5pPZWHbVZFcLvUXAr5098R3XSsuJBHy5nGkhi-kaw_cE9YSDZte1-yptG-LOa367uw0S9Y8-XsEF2VlX3xloSwg_0Xt1INveKh4bVeh6A5vfDhtz-N767597CxEvFmfcIhUj0uAUisgblhtk8gTKnLTpy80pJv-sCplncvhlRtOTrIqqocvvcBJPWUgwpx8FVch4_2R5xaZrAgcEMeuyFBlLT6GdF-iHbdHC87srylIJPmUGBVgmJ_IXWwIshwig8qdOe_u0wi5BjNGLmk6TWk9mCep-_LRVwGCGNufJHlyEgmeP0eunqQJq5oOcIJSuxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9_kdq6oQwjluySRo-8XvHvw5SFfgyqVLMFMuS9ey6bzQWmJV-3-KiunCB2xfDqdtHF7laucEQkNxVRPDUdL7P8e5QsV68IriZCrCtfRq00liVXMb02Tl6C7GeWLZsnAbmrgMbF5uQNnKOB-UUF0jVlf-TxR724Dgs4hmc4zfcHO4M5hbii9KtwPszbXIJAMWl8rSztBdvbZyPAF61qpz4s7aWRA1t8sLJip8G6gVi6G0zngw_mGeGVITaqPMyLnILtrMQUzLrTUB-O9KnyHcXxLV63fWmHevNJ2NezFoWCt_SexwAjTJ-C1rKof2FKeETAC-kOOYcyIoMIYBRZ8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL4YcqFGqTQaVvTOTwBhkZWPC0uGGlx0PUYttkgcJD802BtWl3dH9NqO9BahPOXdPdcfLAK1IEw1qAmM_uQ9RBXDSDzaSNyROtFbVoDYwHg13QeAHeVuWT2cdziVG2hEYI_V3nkFy9u3CBAbhq_Senur94gcJR9PQuXuit8qDYXPd9rTioS11-LqmCZvxNHMABG3qPGlPcaeOcggIzQCfxhXq9vp-RmOrWV5RXj6juWDnWqOsgTVP6n67h1Hmi0LYJhYagCFlm2o9Ud1bBoxlRxmkcVJbhkHGjpYF2yglieXfUmyGTn97V00eUGLsX89p-DRz0xs3rv2c9ZSUSC4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi47YcMEfx9WVCWILr95XknuCeVKvQblM9aqe2g6QHL8HjhhYCzVlEDzF8ldM3FZkpZ2Q5W2TpvIkAGyUX97J4BWEelEt24UkFiOFo-UaS810fi94FYfUorq3aoANkRgwJNO5yvssW8HfYRk7NAYrAPn1t-xiOtqlxenVxm-VSK8oeyK2FHRC1y6_BqptRh-Jo1NprPel9C5kXd7Cunad4YjwD-ap5g3JzUpOS1rTvfc6C2wyWUawpnLZls38MS4GRV0Hku_n1bD1_HEF0C9SSV7a9f-AWkZMzxoaSR2gyajLxsONiurp3gI62fVWffzmMgQ14s0T9QKUOU23WrbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMM4A8ONKAoDMD5h0WqBO7xjFCUSPehl6L3gR_bUSKbEmuGV-whIsCN-Q4Ya_q7wFc9iLjDzyATefskcUiu91_t3RIzi3RpxaoQjWLDH-p2aC09AXN3cxQKidsqlM7x3hk6r5qNljdVmJ7KmyqqVNfZNA82Wg_Kmo3mdQEjgeGmB8EKusNxUWyTTheikmxheaHXCLx8tPgoe7glIooyRGqD8SDLINc9TAoXr-hcqXBxD3vcL6SebgIKsJZu7cIPbdXrTyw8kLSGyk-P2tSrQLKuwDKlTB5y8NY3drHcju-3l_kuEjpLA54e-eAnc4xrOLssztf3YXbyJefYTKaXsHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BroDk_LRpNNxwiF6vyDnzf8Iw82G5FD4H5VAQBWpThPfKWKAa825s6AVqFHoFgohbJOm5WWs_RRjYQHAxr_Xwg4CZjpNBpNdllVZtdb9DH1GraFz1DiIdkoX5pxC8PffjLt0OQM8BIfZANjoHnkUgWTvgYPNdTF6MCcm6_pHyKizrt8nYYd3aCp547fNFJfP4JfVwSz2huRRI3oGHcCtdyR79FFkGaWrQXcAfkZZebGxc9OQrduC2zftziJ0Zc3dAcxGHK5ZPGUa-YQSqrAVCM56CXymwKUe10O0Z_gJelgpSSnCn8giCHiOzZ7F4m6tFNOBBd3_S4O26UinlJ1IYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxjXcRbaGBuAcA4C4Dgf7wHAbomN3MN8uIeH27Co7j1agxLykCOI_m2INOeKSsdDx3jJ70ev4tJoo7Lsuy2AbcK7F562JZ9P69tGvUjpOjI0lPRpmDsG4ewS3dHAuIwVw9jMfM5RrZMgMMFs-chQH25eD0UV4M4aJRGcRfnsJajo6qdVj4xh3_fToGsEBhS0BNOdwV1wLHNZOc7Ut819pue5Td6LNswwp47V5rCAIQ0iIKr7o27UhfgsEODomN3loZchTvHc1ROrg3o6ABxBdSkxgLIU7BovYRFY9_3G2F9ALqAWJEF6shUxhpbhs6EJ7bk62PqmB2d33WAYQvj2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25458">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25458" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=lroPmLAoWXG13MTImIATpAguhD5i4Tn3XUfSLna-phbo8e3lSBekRlHmO5ivEz_cF6WWIfp4GTi2QTK48Ba3LS1tPVrl-ZuCedFvwrs-BnU_D7Gpv74sp5aKfKTCzA0U3LBbfaASa_61yQZ2FoDFXDlLG0WeSkeFla0CojCRNIB3SIh_LuEn9prWZ2u7D7EwDwLKTNSFn4wd63wnb1IinBUeKqTdGhUzsM1d3v0pwxO1yf608xKvkK_USnmlHd5REvYzMmXmQpT9dwI9xW0c4K2HnDFPUyemTWG2pDAz1kWpCxCHc97YmbMjNNVcq3uyiJMXjIVzjhhls10r1BmHtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=lroPmLAoWXG13MTImIATpAguhD5i4Tn3XUfSLna-phbo8e3lSBekRlHmO5ivEz_cF6WWIfp4GTi2QTK48Ba3LS1tPVrl-ZuCedFvwrs-BnU_D7Gpv74sp5aKfKTCzA0U3LBbfaASa_61yQZ2FoDFXDlLG0WeSkeFla0CojCRNIB3SIh_LuEn9prWZ2u7D7EwDwLKTNSFn4wd63wnb1IinBUeKqTdGhUzsM1d3v0pwxO1yf608xKvkK_USnmlHd5REvYzMmXmQpT9dwI9xW0c4K2HnDFPUyemTWG2pDAz1kWpCxCHc97YmbMjNNVcq3uyiJMXjIVzjhhls10r1BmHtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4aL4KftYmYd6TG0jz8fAczn6NBZqIGX-bUp9F0VUY3edDyp_aLsAj1xzMWb8hKNcd8IU5pomysSAB1zOXkPzqhg2la-lx76UcWhHglIwUhQV7QvipxugiO59k5K_YOgc_0OSpfFfRjYLPeQgAh3seXXQuLV4bVDwcu7lrLYUDuPT8RaXffEzdrEyRk67l58KBidrVbUdp56jWqWN94r8fd39NKt-IF7vJSPjJDos8FY0sn123mGpzWE6iU4St2jwIRGGh0WIicGrpkzSK1jwsfg9xlVRb1hLk3E5yDYCd-w_o8KyVjZADJJZn8LzdCS-Ev-vrxK1i-VRktGnvbF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5h91ST3pc43bTWcKDJsgLS27kmTi9wbngZMRpE6P7u_72KfrVY7WjsfJL_CKGop4KmnIP6d3LGMNxUI3tsQZESmWnD5KnRXITCfRjq0Md_0IXHMRvMo3TSmA_8C86DmjZDALWsiybAUavRpWFe3NV2gMBy31Pzfdlw5sHq9k5Pvopg21FV2lfkJdi5Ao42BZjkS5Nb770_uvsID7b0o3fVXpw-SnoTIxKsii65d1gAYKLrNRM438chn9XzfnSfWYJ2tSgAoYD8JR9AtSNpHeCDmFeQ3KdRN5a-zD7r6okrajGx2F5CnuYYXRktgXH6v4r3jwx9AluWfbyWyHa4Y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8mIg9gVQCTw6PbB3YmdiLcNRiEd-hpUt3KqcnYlVlJpV6aGLxPulRF4SRG8aGw2gStHbxcC76VphCxGg7seFs0wJyul1Cannq_9u2tP2L1BU1lcBnHtkw_AANtD1oJHPUp3HNQn6NWGtbib5ckODP4oZzJXAvz6EFGm4NFwf3_FKJ4FnpvjcIdHvfdJCk1f13DLBlHD1njgU0BL2uIXPSAuDAxevtHPA68gEdzuhkKTPMWpJfkTpYq-roXznYLMmZooaL1sl0quL_LXFuCPcbTNgmTVas3AWA3OkCCOEvgu_KtPZ5CQSx_0s9UyoqNYOgWcDWSuGaQTrw_LwFlaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upV1-GovYcUxAsA-MqOnI6ICDWgsDHaNhH_HO3l_kGwOqVSgmF80vxP7kEvqfw9Jpe3a3abtuS3_JB7HlwW6cMyvq_UQHcodihnQx8pF-TZVKVbapAW8kvzLYoieCQ5cT9aKywhw6DyF79SOpDbGkQtBnxAFpr8nVDMKUtt22l-JynjuwglJoAK0DCSPgG0F6sS7999zlh9AMOgF9VCE24UFh1zghV4HktdNVRBKumT9ZmJX6hk52LaCz8e-2uGvGElpsPIEc_nO0z_PmJ5lxt7SnsBa4QW1F3D13PfrE6GJpb2lxHN2fCoBd6JTZ_QCWFk0RQaThUcY7yU7VWafRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzhdk8VNqLtMwY65DarwxXSPstJTJ0jAoT4Jmb65jS312RZO-8x6uHCTwcERB3-SNL8Mn-H65rAXuQmacuDtDL8VA1Q953P4OzWjWq-KHg8fqE7eaVkRRRS44ew7V2qtp1WOskzco4RGZIoCD9MsCYN9uwKW8HbxtJvxFMurKm8Ed3_Hex523rBpY25DA2-E6PJEvu4E3xONCK1yB9hDYw0VyQIbZt6s35p3mU7ATMVDyDEDXXL7f_vXXjkXtD4J0nX4yS3YR0__dPM6gXAUed5NS6eZoVTPrApj2vf1jZ3v-6_8-VqXUbJhYVOIOj8HG6Ly-rquwAXU-fWn5M5siQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROOItZ8VNtR9-cyqZjhwjf6RW_hN5Pw3DPWmgMykZLaoyrLgCOJhWsP39dY6b2tEQobJxoJiAFrlcsO4nxm5MBUJe5Xy5D3v-WZQ7IX_UDiB4_T0rpEbZMZSsu_E30_GaZV23OlOVpHacSiOVkAsBzgkkbZVt7dlG0VnE_QJqQTe5cBT_lGtqZBBQUNjM_xodm94SiXtEzwB2DrNfOjIG-hppu06zit7X-TlO6m_b-1nFXO5FuFRay3fXhTXnSAXrIFsCTN-SHKwmFhUE6q7CeOC-0O3SzM2nFWnsc7Ie4Dq39Tsu4_zjhDpL9O051fdPK-2K7Fq0CYs6VwFk6CBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1I0Pqww0Hm0PhXTRE1fPOP7aZYvYT5dt9eW1fp40-wnZ56RMwpNayRSdQDDeUcpkYJIuWKHHFg6UwA0dnUYwzbpNIWLgQXRXh79i4LzJXn9rA252F_SG4J3M6dVvrb9XdAB_vyzOQo7napvKr7Ze7Iir02Zd0vkUlbj5MbeCmq0c2mpahzYPEF28Mb8QkH0T6XmRQr-ZFtiYmckEDVJA4odqtcK4SfHjmTNhPsY9jpmL-vWsW04oCXnbFuYc79kZNPkDBptHy9GWx9MTuxklx8ZUe1Sa5w18Bg6mPZTxqxQ1szA0N2TpDdJ6qjI79dgiFxGhJXXUvhn-ye484LYPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqLkfvZ24CUCWnOW_2HmPpmXWh8fba5NH8y-Qdwg2OqDjcVVHzOwkss0yOqhlPEUxOw1n5an9P7qPlInYa_neoXPlUPjgE-L4G0QqsWVgdCytB7AfY9IbOtlvGgKwYkbefNNt7nUg8SB41Un6y5NT_rxGDnnJI5GHuYeYd5l-wn6WzXY8O-hnoPiAuQp9ofPrXTkC0cDs-2BWUxwYpg45bT_2XJPwWJ_DHiT7V66cUdn3iOB954QM2eH2ZFq5fVhbx3OFqR2q1rvt8exHMAXmpZeD523cPqMqCSfSp02O4vA-V9Y6KqQ5v9nH_zPF_2yNAa4Z3HqDLjHxs54jPa62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6mqtNOra06Uto_MAKzyCGtrfbw5p-l0DOFTnLhzK8ndrgrR6Tw9Vfmi3CaIEoeA_UtYkhZ2b6xnfHL2UVmj5dEPIEWiOahiUbLJX2DZuzvYagbfR6yaOnFzlmPfb1pzqfpzRtp8dyVK_IUBKKr_RK4IGC3cl_SwN20QZ5mdZ4kWcAm5QPsDqDvYgZqOLzYqhbuy3rUoQHqKf37hngKgW5V4KmvNWD0GegxfvMfVbF8UTrnwu2K51vBRGFGPIZjaNQBDm-BQs61EDYRgR5ZaX2yufN8wKSV_PpmO1NfjhRJqwwK9d0uNQjj3sv2yx1gnmdTyTDE0SQ2Ffw9RvQI-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGELx7QJfVJSP9bg_y9e8bCx6BX8Kg1x_RLeTPbFXsEhHFkurgcmRiOAnUj8gkH1r7W9V9G_06zOPE3SgdrHrHLPNAhnEkAU-17MyVOxlW27J1CS63DLZGMIxlfjeYXUH1U98J5QCc5G0GCaD8_Ea4_3icnvDIJiATA3BrSyHU-NTXI5cZgrGlXRBKsq_a_bARM-D4lD4smNYZRHx93aYOZGOoELoxiaLJn8FyRhgvV70IF2G8BEdhGJOv6ICMJMU8M-NY3KOfifBqq2DEC1qK2XeJfijpv1KcO_fB8Q8zR7dIVTswDeWHNti-xQHZRVBqnYWxnJjLAHw5yKT5bzdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WozHZx_A1xHpIvA1ItXeTj8-881c4seiIikImRUCsH9Vo-JWzI5jDKiubgmEu2x1NP9Fe3S5q3TtwkqgjDvi0Cup8V_7zX7OmttBQlEjYSCs2Y21pWs8y-WRu8DYqULyKtvuFB3G6BsqDd-KzDLCET7ALnHCsBZEsg3n4NjWilVaozAHqMuWsALFbwxtPbQbKHNfm8ULlq3TqxQRgPJoIqfoMvoXNWMq4yOu8l9l8HINyTbs_OytwuRzgpvGPbfd2H3J3ljh4_qZig9SzQ-DR_BpyNqpw_aELw2fVSKv31MbSpGrgM75tkawsQs4sq9iKcRUglvoB_5XS1q3VdYTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nY5LvNclVQ35gJgzu-cvnHQWz6Cp2amGWmg7o73HS8PHdhGp-vvQe_5lR5LM-5IYOQNXpwNM4VNqvq6ZW3KEJ8gMUx23WtTCg6tOmZJavMUgoaDE3S9Qx-vpiw5gRH37X2jd3kG983IxUlgmvHcaYuaTkKJmd2wEsnZH4DO7YJK3We_okuSajbyOqsmbHkUJoPhN8zYSuJEogkr-Fp8FuoMNe6aL81mAyJJyFpt6vwtsc786T0u48CCvsYeYPgiRFpBnHSRoxp6KICdlyX9uFgZqMSvB7-hLv1M_8XROpZNF3j9mgZXCQns6fgAj6-Mf4PBa7Poj8L813vIeAYXVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izuNWk6WiDwQZiKaoNy4R4fwfIeMwPDPkSffxGloR0YBLvwrSBkMF8hP__k_TqmEp4Gbz57abP6Sr9IF3FUeDGNeSu9kDQNVoiD4nfuHgC4RIVmHZaiWTBP-igFgdoBVb_bIqSxba8IsDvBGWXb-Y-JIEdhBMEWV_94Gq4QYL0ixtTKK8ddHJnAF4OPF9KAx6TwEO-7gkMvvtOKW6Rs_FwaOLxwumveEt_5Td1VynA02kr-S_JCd4SjTGpIz_UYz9uJwhVRdAdX4SR1g-54xDQPd9CCzO-qeWbP4cL3R9_JXxfNLjyg7PkzkRjojWS3cV-Fmn_GLbsMjCjSIVsJlfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RI6ug871Xudi8-o7w_BPuzXMNKWVGJ-4IQgv-liJtvSqz7uNZhyzJwGHZ-IS5JFaITS-kdhgrS3G61wqxuFjrEDocStxPy4Fq3S1usx_zpMOxIc2zas1NPgTcfSWJSQfxGnrjV_o4kQ0GAidcBJhbtKafYTO0YwFUeCr_5aLYlWXjW3MhQXSaGCld5iVzNwL_xxoZxSUmmZtNkKwCxmBB0VoDHCwNTs01oXU9Nt9uiii5JMxbrQcG8LHWzlAZ9182JNMpVOPFf8RYYKAlsewxJmtKvnfmx0JuH1ppsUvJwqqD5sLcaksavYXoZjZ6ibJfQgI2I3_kordo1_OKlE3Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKkjY6JQFMcNOa8JWLCE-QZzeuUkT3fWP0nQYBbpweqsUUZaiC1F6txGqzJo5e0R99L0phpIV41S7thzaRg_0xaQysx2GrZ4JmsCqjVa0Mige4PlgPc2wkc55lUYOspBrPJn4QR-jcRdd0bTZ-u0dU3aBU1PPQyQzFFb37oq6yEmWMJIYNT_oF76D76AZkXDzwJISLJztqqnAQbpn5Vn2FgtkBw4NnlZYWV0NNHhKS093VSRIwROKgwG9Pq19TjOUcGN4OXtZc35NmlIzHXjJrIESTWITk-tafDZe572lAx0xlGWdQ2-6vsANrLp7jmqERJ0YtfsPmcFh1uHFX7gyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u93-R-mwlDo5jBF9WC2iRL2li1lYQ8-ELgXJdewD_oRxhRy4f2NsIvpHtqutTOBrAzyw2rZ0UqtsJqimzZ-kYj3HKJRbEMS2MNPwhaZGiilPOQK2CWHOXxLpe0MJOQFyt74tn4Xz24FBmX9csUYir4nA4TY5kP8N3DyirwtD1tjWCSonrqkt8YVNKlLXe1mAuKJTrZyrW0aU5xh6KNgBcuwMOvGWL-yJhSFMNa22lp1k7LL2UOmdFW0nCuDucuTRKrAo17A303riGCdSnW1ngCoY2_pP3fwHK4jqT3_2NRsaKsBjW6QDQip5i6G9WWQaANkXN5BNt9E3gPN5DGjtLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkndc8EPTRRS2nNy-rLC29saQRRrsm5u-DJfld9nA0RRiaZImE_WU-z8WfWAXwUs3n-Ccpt8gVtQlxML2bpHCGL6hXJi4eca_S1GNizbdcKtJ3VJ_CvIXwz4lHHdS_yRXD55XJznqPDCE3xQc5VrfSGh-l3wEr6Hv5HfD9mDq-U8rVFpHUaQsyyVNa20NHH3sy0_R4viQ7FhfqBxqu7vYHaQRSxlVV8fzSupQV3V9Auh8CqXs1-1mWLL-QR9IN0QXisO6XmwOYGrKxXXe3VTmIlsC4aRyxK1fIbJlTqrf1r9O-gAvV553bBIAUzpH1_ZtqUr-rarVDmRW3b3huA2lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlHjRJ8EtG2UKA3oxvMACdzA9iXdTPRnhigb2zl4NbzFZH7H5dG5KmEZcCHmMYex4QJ0Iz-4U9GzrP28l22EvfZPrCtJcECPsgFyDTuELOHtyAJI53Eah2e5CPTLNaN-PWG1_4UGm6nVZrCW4ROCiJEhK9vh1w_46oM42Tyv2ZED2tW8r1RkSCCdZO-0Ft8sV_4rL9B-Z-UzzVzsjLSUt5aWq6eqYgVtZZOVqkA7jS9DCC7zNNxSQJPoyOtHBjeUN9cT5HAc60OSVyq6WosJqoFNR0EMlXQoU9--gg4Sh6TUjIB9uEAmtlgDV53sPB2p2-Kkd0z6BDWpZhiF_Adj5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ee78Exyyl3B2bQcrgWe29PxXzzMJBFUJdP32I6XFmOk6QPfqkFNyc8iqXk4wh5qX_RM7FR6305TXrgG8k2wYCCBu1EsyW_PPq8cbAo2IsxMPKDIt46EO_4dwC-xaUSFqbWoYyoSdmpA_uPT-B2kzwP2utKjKUXwl_nEoAVrEO3ZB_L5UOh3M7t713uTiS5WISrq1eG3HCAW25x8kH2-VMJsst1dk9nKPdtTfOpxTCxzw-tLQlz_wROleMle7bpO7InkACT5tyRI5AtEagFI7h4a2zUFL0JHcqtEOocbKkjlpodeQ90PfMJM9mWFJF9VuY0_Q9LkTPup2YyJmfTWNYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I034miNVhAUuTmt2JTfBnND41Y0u9GOawgsszGG_yrTOzUL1aBWoVESZC5O-MElLriHBFMLEagCvx5KbYP4JzWmTXX8XPjAxl4KwKM4rfEpubtwZp3NGT2d32KMh__4k0bsusrzJldjTogmOySwlFF_P8sw15yaEoFum4GeiHmUn5euJiNxFP0mPJDu5iLFw5LJHvO-XzxFC18I9jAhXN3E37EIoH3NN8XQ5aBQghJ9icNun9RC5LHUTmQfivtWvFrnT4Dk__CvM5uXCn01pvlOcReAsYswG0xW0_lIOWHGXjHoRT125rXns8nb61rGhAikdgBmWIFcNgZaC6QcxQw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=OHttJIidNxeboukQDLwGaWGafNm6EUNk2LfLfhhe_5s1a00863ohALcZ2D19XrfaEmzZ8FHhGHll0Nlyj-00cv46dDqwpD46vsm6_C5jhuhD8EwIV-VSX5RUc5guX6RR9tErlCWw9m6baRfXLcVADIW2LqI2JH__KAeJOO0JpXXnk2NTxc9vyl4nzbVQZeMzHxT-VHqa7TgszaLXm8IPozmzCsfOj6KXZeMubJGVkLOEbMvwZNcBna6Q8ZO4mQtNAsWrPaUy_09n8atbRO_Lc2k8D3FMOiIOI1m5SD8AZu7nuEZO-xpOFUwg-oxPiXXc6gjA_pghZMwCNvrRCKmC3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=OHttJIidNxeboukQDLwGaWGafNm6EUNk2LfLfhhe_5s1a00863ohALcZ2D19XrfaEmzZ8FHhGHll0Nlyj-00cv46dDqwpD46vsm6_C5jhuhD8EwIV-VSX5RUc5guX6RR9tErlCWw9m6baRfXLcVADIW2LqI2JH__KAeJOO0JpXXnk2NTxc9vyl4nzbVQZeMzHxT-VHqa7TgszaLXm8IPozmzCsfOj6KXZeMubJGVkLOEbMvwZNcBna6Q8ZO4mQtNAsWrPaUy_09n8atbRO_Lc2k8D3FMOiIOI1m5SD8AZu7nuEZO-xpOFUwg-oxPiXXc6gjA_pghZMwCNvrRCKmC3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kukv9NLoc1bdR6OIS4qHgl23J0J3lO1QnunCpvy64NGg7ZsPukOyCOQpin8TrNQK8_hKcGU0tEtNHHL2z9CQNiFPBRHa-Uk8Kbj7kYymiAEv3jf8GoZS-6VOvFW21IQW8-7uzBrRKcHOZUcNNZR_vtqpPcpJgwHwenLiS6i5-3fBArHYuIQ-Fz8EroEbpLc1h0YFpmcBuliIFV3O6QDSjkUP8Kkc1HZFNMlm2lPuD-2ysaUp2SmEKqR3fPG__kVwvuiiliWRHCD1lXyZAHTssc9FqakvYk1mUw9kX_e1Akbt9I7ikojiEbA0a8rLALbC2LQqzXcN6tIT99jco0cPmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvD541cZMmx76ui8v4TTia-Y7ajCKzGVsfhmMWyDVht9C26jWsC0IaDSnAwJ9EMMTcsRINxv510Tj13zpULlJMjIkBGWKn_wB3uOwfz5qZv8nHjpGtQKp06_X0bUo529yQzgntxYkRXwPThDZ1OsuxD7cwkJiB16ZziItyiIflLHFuVq2qHeDFARA6sS11F0AFhMbtWqQ2PWGUrogQbmBAopjt0Ae7gHKSLOFR8GJpmC0Rf2z7qCJsqWFWlDwTfvGdQl18JKEnKuAiOCpvaiqh-GujbVWheHcRrKej8MLo9P4X0X0ZKvHP2kZiIUManC1HOnXsPR1jv8a9j2F7R6CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVWjcOXxmzvrAmwW41s5oykFfnW_Aq5F0hESifOR6XE-vmkLyX6RPvPqEI4ZR7E9kihRnjHO8MdntefDvrRWX_gZM2SJo0Cd_3TyMLMBVAm2CLnJVJgqRqOah1FhP2HYUdgBHbs1qprjCyQt2dYHVA_MKm54apbk27qVuXfbec33YiPq086O429E1mzj_0jzUD5B94L54M6WOooudoARt7qAAgikR8q3hy8FSi8VWkudbGtNcNK7SVZgJg2xHto4QENq2fMBDqIvxwSO69u1KosJWOx1Oz2C8Kj8foWaAJUERx9OxsAqlXM3Lx69o2PrriABCHp4o_4ZKM-qgn-Fxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSBwq18pkEib8aIwlmKRFgAkwqw_NGRkcr_eQeTEBNdSsK-GwmoXWSnypj5r5IzIfI8wOCrMJZLYWwDuknTjAWxNHtl9qwwtIMr8Cmq6aHs0FtlVuKfOzKiVcpzaq14X8o5B80y0BklIpqVy_4ARSb1NdHp0df9FWG3WBr19hxTWF6GJPci_03z3MtKtECW_mo4Xsdpga2Ndvu7Di9VTzaiamPqbGgjZorhnh3lOyfdjwpFUhs9Mc2q0nJX3rDXqTT_G779idRl8V0n05i8_To6Wh98roIipTJi2YTLmoT1GUVBK13zNxAmFFS1QSj6zmTIG8TxQ35LoawEDrY6L8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq5d8Kb5ajw78BMzceTSxdpf71fcSUkAI3Eo5URn2T3zRInaiyzrBBwleXDlmMjR--971FDVvNBQtOsiwfRdQpTZ3Q2DhlSRxT2KFLb63YKGbfuWwbWZuC5wEj2NHgYq3dhKQSo-K5cb5fCYPN4MQE7oeJU3EXMjVPIQUYjqLhlw__dGzWMyA3bAtdUOIUC5ARWAtSSObrPZE8r8RNp0I0kTBafjIORGvl-3YoVVntQGb4hwb_wkMxEXasv9He7uxO0XiAmYlRHO7B5wkyH-bBiPFj_DqyOU93GMXNy-Uh5ZLPYsDxipB7mSaRLN7ydbmPl5Yazo2egCH1488Djv1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CanC7b3EhhGNHEv11HJ3rtd3PDBSHTnBl61jWaR1uU_JHH-dq8RMWeOGcYKLwWKqwuev29W6CJr52kIUQX3llbEuPtwWGZzITjnFpLmgSPMeAlmuSpqIBkc1N6gguu3EWqlyq9VF6nFEBxr0usB6nXQEOwU93nVo0dgYKEVuy7RVOChKxE7W9f4EyInl6tQ9Vn_8a6oz9Sld-gYmOvfPfdHdhtFHeEIjmW2vsD4ezHIfnXSba-6LoVXyUVS29ntDipIVxyXOStGbSJI4NDQLFodwfrkkymMnfai5z0W2MaqfQa1bP8Kre-oCf5n1nDLqYYPsRFPn-pIjv94ucPAn6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6jGdMJ2W4gY6jslGbhBokPytKvj6cu3KF-3TLMowMIcJRP4twf3kPvhG8Lb-je0Twgi1jdi70_7Wi77g7X4fD0uEM1fr8hJyMvlKn8qWsJeCIcgeMmxXRr0j1hP7YGkcMGMsHPSQ-d3Yh-TnnzlcHZ_Lss7cCBZgynk1zh3pM0y1mqkc5Q6O8-u1dioinY1I1hC8Kwo3tgcFqKDxuSPq7a4_fmAA5-FizZBQ96boKFIEIGepczyZ6joHLQ3sjTAEo-zajWDE0ZNOlqcR8N9wmKkgR8ABUfaeqG6h_rWzemqCRXv26Xudjvl7I5Kpqx4GqKYydu5UpeI03_DiQKDGfd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6jGdMJ2W4gY6jslGbhBokPytKvj6cu3KF-3TLMowMIcJRP4twf3kPvhG8Lb-je0Twgi1jdi70_7Wi77g7X4fD0uEM1fr8hJyMvlKn8qWsJeCIcgeMmxXRr0j1hP7YGkcMGMsHPSQ-d3Yh-TnnzlcHZ_Lss7cCBZgynk1zh3pM0y1mqkc5Q6O8-u1dioinY1I1hC8Kwo3tgcFqKDxuSPq7a4_fmAA5-FizZBQ96boKFIEIGepczyZ6joHLQ3sjTAEo-zajWDE0ZNOlqcR8N9wmKkgR8ABUfaeqG6h_rWzemqCRXv26Xudjvl7I5Kpqx4GqKYydu5UpeI03_DiQKDGfd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qK8q3S2IDETeE5u-CVCQ7_jXYq2Oy_gUUBBOUINSrErZRVK90Hg-7I9ml_q-3zdYUfBUiyB-7ZRM7sflyhow9kazrwyBrHk2ukTwNLZ7ym4Wu-p8JWfvrgwzi-C83svl1in42X2G9YS8lWuKdxu5VRqaA01X9K476qnLUEeig98acnLLmAzFoTN0U9ic4zRYVzgj317CP1pRi3Vo7Ls4y-G4LhnHLE9-4shewLFO9vNRFzMoL8wXuEFZZ1-XY_6kBLipg-OKHLHj13J11xIWZShSxCtczw5LA_6mmqWcT_fMaKNxLAVaUsxw8Bv7Vy2fvRjcd2l3PD9wsrCp1Yzayg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp0XRocAs4_SeWqaUs7ARbfuzOUiFHHRn73G1oVKmwGMUz_47BVmzpkvnNb268uqBNN2CgmwWgqFtMTYmIov3arnVrq34w35Anr6H5YOXfrisge8E3eSba6nEqpKK5MISXvuI-AJUe9nHmpNVKGwumHxNuMOY7HSQrl02g0UvragEY4Rhyp5UfSgvrq4XSy3hZ-RAXvWGFTDEXSzWsH7EpK_YT8IlIV1QnnO3-qyyEYp7mqMDU149G8qHKUMbo64tr56KgTnaJejybcgAXy-cZiX0Wjj6pEWg6gFGwk3wtZxLclElGrILJP7EUQGiNAr8qQ_ONK3ddskCsVoKOnFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=JKtjRjW9JuohBmFD0XRnKs9ZqC44YOBBQJeHt5IMKPgZQ5p_9i7EUDeuojhinAsfmI1R6SHy5pjRxIVBr2bJ-xnTiGUkQdzWCJe-T7Yqoz4a4hJpFnA3BJCGueKs5bwimzet2e-VbJdO3y5Did_jLnVGSTr0lw8GPqy0D7k9y64ZkFyC7pHRt08O9ceutFWX8E0_s0hZArci9NTb3pwpgI48eUuW_wfQ6x8L6XIXuKy5m-KHzbdDaTFWqrHa3ZomakYY91ubXgiGhPFg07RYyUrTOBVPx4QWgDhDcs0uv3aVXjB75YdM418apCyUMZQURFwIJeinkmMpHAqXcK-M2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=JKtjRjW9JuohBmFD0XRnKs9ZqC44YOBBQJeHt5IMKPgZQ5p_9i7EUDeuojhinAsfmI1R6SHy5pjRxIVBr2bJ-xnTiGUkQdzWCJe-T7Yqoz4a4hJpFnA3BJCGueKs5bwimzet2e-VbJdO3y5Did_jLnVGSTr0lw8GPqy0D7k9y64ZkFyC7pHRt08O9ceutFWX8E0_s0hZArci9NTb3pwpgI48eUuW_wfQ6x8L6XIXuKy5m-KHzbdDaTFWqrHa3ZomakYY91ubXgiGhPFg07RYyUrTOBVPx4QWgDhDcs0uv3aVXjB75YdM418apCyUMZQURFwIJeinkmMpHAqXcK-M2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjW7TuWnqO7jiAHAKkCywsKxWASTzrZUadkmGF22qXVlNSRLILXSy_PcaCCh9Afyt56_T-F67liLPXl2xUzWeqz5LSuFqc3Blk50TEIyZUQVDbeCV18YzetURQV09zM4QcZBlf4GsGW2cxjig5fIjS9pjd42HQ3b42cIiCe5ChYr28Jmpm7HYLJyJirj0uGcngNpWCtzllrC4VvQCV0dSN7Sz68iARxvB9hBYDFmsybVR1Z5athhvtcY48QtGud0UqwugbGEXRx2Vwdt0snMBINExuF9pDGf0i-G7mX1gHAZk_tywq6nOnFOtCTDfTLGk-MKO5vk9TBgKNQ7-wH56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/he1lmr2HI9VEnhezg6JFK4deyACZz0LT0Yh_q14iwKa70vG0wRbTjTrLahm6Onp-v1S5n15oAcfvCjgNJvKgugMI18JzCTN0M3_P9hSTrF5nHO5brPtt-os0jgkVrP3rFa7ogdJz9QqyrO-v_7IUIpJw3LlmbulpQcNyLJ8wN5RQxcOcYHskUiTojqELpXRyJ1Up7STNPFBdy5j_WiqHE_IYJNwIcovuIWJkXynRZIgjB5_RWvg5kWj-zLOOwNznmML8adGk3U0RR9QO_4vnKOI5SBXLLk2ZgPINFocAXH3CMxUJ5_u97iD7jas2hWV9c12Z9tePjgvSzP6G-6UuWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_6fR56tJgkDiyE5_IvZNMP6MGcRr6JW264NUBADkLIH5h0szG-w6ODTNwO_3-Lok1Akz6rCfIS9JBAQvN9saOEul3bII8jjZLfUceQ8kCUPVHOJxwfHlkKpHqgJtAHY6p1JJg20Ao290MMAE20YlS9idXsreuT-gHqbogLRBFSA3ZUEzSnzl9LVIroppUFcwIBBzL9xJsJsBkvnu0C7N5-H4S6KE5cjw6DnJ4JhV22LhhzO2H8T8Qf965__nYxgt-5_QFy6JNLupXSMcuPybZE1mnAe-N11_yxxuUSHy-zU8YNSGu5pq2VjgTM8yEge02Z2lERfFXnextS4jPwxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPpTJqG3CujFKvM7cwLGbQtAUwNvXP_kPriTYrMkx0vBX9BtluzWSdyy56CSssPgqnDhrUMVozedA9QPpjPGTSKKL07_qJrjUGRH4MbyGDgNizvX5MitOlM9Bt5-Sev-YGEQKM5a_4sFchhNKBy4F3jOSv5af9UbAp_HytmO9oRucmgeF7WVYl-QI4MtLFCoeqqBSET9j4Tj49U83gPc9VsT0lWi6UnfDBzJdHpozwKRdcUviLJ-MrJAs2q0GgJBPXYSdBMTl27isD0JFRIjf5fh8C1LLB-Alahpgo7KkHu-h68e6nuA5OLF3PR9O2scFzC1-vwMoVp4mbU_6LQMvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNq6S3OzPapLdtKPGZ9l7Z7iymtFfZodVv1ajx61YwjgtTV1sXPGdWDCwNikdIUr6WEizdbXzB7Q7LHN67vd0iXxTw8NDWlK3cf480T8HhkJuPZnwnguFEA_HNVrp9TDtdxpbjK-1F1vXRvA4W_P010fWgqAn2RcXCMhyXwKDOgXsBDeC0l9dulqGM3oIq5pX44UXotPlwn-naAdOoX34KOp8JYVL3h-8rSMmGePilgGuTDXTtGIHirRny5k4k2NXNxFrM4eTf1QxbeF5OH6grgHYj-v4mQJSQdH-umzbMF0Sa72IEBuEuLqmlOstJJF3MDMq1g1P9Kt_Ms5weJnhQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQAyZ3DFvHifq_kwoSCwMItxbA3CJjxFwsXBt49SGXGnI3TWSUG3zwSOchjuqxs4w7JzKttqN0QbhlonpnP1YCjdWXXuzUU9m_KtADy2sO3lEpgWlDxkk2hBgTWBrzaJRWRXd2eyraPcPdXwnLf3RNn_4GU-BTyJEyTRNFm0lm647-SYlrzzovW3_7mx8actWGSIwabv-Mb19sVIecYETmLgUqEI-cmSU-hsSYTsL8JiaCCC19JI7z9CNknr1j7WfWi_-xE8O24iNhRE4KwgDyeK3YoPmfCDA3eulLiD8tyjWsvuBkq5cnYmmW4A4SMxMk-ccMoZwhvEJTw3fpgWiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=FR2q8HN_TS294L_4Gzu9HCwkaWRYY2KMKPr5T5Ud_fiDuSda-xoo9Ed75EJNRv1ToPcaP97qJoX5QpUbAvT4_TUwc7jjSieemV_SoOebeHWt2ujQWwU4B_TaeGtAy5-RB3AJXycHbUbaJgvMy8xI4cgn83vSNVdRzTOrdArUwGCExaEccARhdL512KitsHpaEsmZ3hfQqavTkx4x9qwDmVuT5RHGLd6j7a5g7cq8y-61BdR0zi_He5Kdpmt1g2j1yU8bb76kMMfoXji1Gf3xHJVE31Wy5YeJZbu-8cWP2CMQ1EpDxZGA8e4DvUzRD7QZHx9RWPT-AMvydCkbukw4qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=FR2q8HN_TS294L_4Gzu9HCwkaWRYY2KMKPr5T5Ud_fiDuSda-xoo9Ed75EJNRv1ToPcaP97qJoX5QpUbAvT4_TUwc7jjSieemV_SoOebeHWt2ujQWwU4B_TaeGtAy5-RB3AJXycHbUbaJgvMy8xI4cgn83vSNVdRzTOrdArUwGCExaEccARhdL512KitsHpaEsmZ3hfQqavTkx4x9qwDmVuT5RHGLd6j7a5g7cq8y-61BdR0zi_He5Kdpmt1g2j1yU8bb76kMMfoXji1Gf3xHJVE31Wy5YeJZbu-8cWP2CMQ1EpDxZGA8e4DvUzRD7QZHx9RWPT-AMvydCkbukw4qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=IbvJ3o2p1kHrfGCsRXM-P3s11R_OUftn-xBFvm1NYuVPcIv6mdJxPnx-k4JFn7-HIoswSv_u7lfyDzsWD4L60uiYLXAz_Ydb6JnFTOPCQLXMToIZNyUsIdiAloKwcWRFPjIE4wqDzBJQtJAeAh7_f2XF80puh2O_5e97K2H2dcuFVquFVZcx9j0GzIcTSAtDwT0ey84O1ZdC6E6jmm6w_UMaqAWsTh9jK0hSVfKzj4z0IPD49zHrHACUr-1JimcfouND95mqoSPotxCgzV3l9_YK1_MKDZWBHdxXLdko1Ao9GSpcuGp1gCqnvkDeUYWNqwHv9d3GwLRW2NCOnKMdeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=IbvJ3o2p1kHrfGCsRXM-P3s11R_OUftn-xBFvm1NYuVPcIv6mdJxPnx-k4JFn7-HIoswSv_u7lfyDzsWD4L60uiYLXAz_Ydb6JnFTOPCQLXMToIZNyUsIdiAloKwcWRFPjIE4wqDzBJQtJAeAh7_f2XF80puh2O_5e97K2H2dcuFVquFVZcx9j0GzIcTSAtDwT0ey84O1ZdC6E6jmm6w_UMaqAWsTh9jK0hSVfKzj4z0IPD49zHrHACUr-1JimcfouND95mqoSPotxCgzV3l9_YK1_MKDZWBHdxXLdko1Ao9GSpcuGp1gCqnvkDeUYWNqwHv9d3GwLRW2NCOnKMdeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS-HUBSHdlbV_YX8ysLHso1TooL6a9X5dqJ-vifqsWoU5oz8d6xiqxsOTVPXnFeeybVgvOGsfV8CAu5rY0JAtT4kq5g7MiA-s98U7QtoX5FM-g9y6u5ikzn9dR8J_5ERaMWa1PRy2-lGr2tr85kfzvuoo8oDDFNZmhdab67CxG51jDx-AxvFJ5SBNYNePwx0gFL4RCFtrvGZS7zIdtm3tIPooDypzYZRk6sGXX-uNgBrBQKUQICy3Kxx40wUVnbhALE7aXaUN5vC6kBcyQrKiqe0xrJL0iOkKX_VRusVCNxctfybbE5suGMui_uz-dAM-GiJjs5wiMRVjK7-XqRDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gal_q7ZB8dstFjaStGErckmv-latkztj1IZUCUFP6t76bclCH6qr6Jhqj7VeL6XbC5iyuucuiksmoC4CyQgYsTzckiamP4kk66NnndoKRnZQ0NMELg00DZE7k2eArHnNnKj8Phq_pzCZa7ZErGFscAh5OIqNkUKrgLnIC4osD8I05dCq101n6s348uH1jQhy9J2DPITDxi98CVJqDvm9Bswmt2TeuWMm2y1AChIt3TUHPpjlz1xZfA0bUO72Js6GUDumEpNGkRTc1sdpd0PI4Zkwd1rGJE87W9od0K5Qc6397rbJ3qD_ex0ykOMrfU5D6sY9fFO7sJHq7BNcX0s4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=bGb_6AYCnMxdokgLDQFFXQCeStB4mQFllcjCkQraHoZ0Y0zbMVS0Kq4fPngEUDK2Jv4_HLuVw8X4tj4yiAuVpdZ0Ru7-F0hhuze1e69l9cTWHelqvEjPwWBbAdQEOdm7dp9IiQ0WZlb7dLonW3Jg6L6Aqt5KTU5gWIXdMDe9RERdtE8whwRIVZs0ZgHQSeR0kizFGPCq8spew37iGxLIrMle7nprpUESTRktz33oaL_bi1Sbm6ajZENObw9mkdVginH-Ywh2M3ucshcoD8IYNlL4BUN5-fQQ9VRlaXzGz3X7qY3cbvklgaiP7FCYGH539pzNHj5eL9SIzYjHv7WWpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=bGb_6AYCnMxdokgLDQFFXQCeStB4mQFllcjCkQraHoZ0Y0zbMVS0Kq4fPngEUDK2Jv4_HLuVw8X4tj4yiAuVpdZ0Ru7-F0hhuze1e69l9cTWHelqvEjPwWBbAdQEOdm7dp9IiQ0WZlb7dLonW3Jg6L6Aqt5KTU5gWIXdMDe9RERdtE8whwRIVZs0ZgHQSeR0kizFGPCq8spew37iGxLIrMle7nprpUESTRktz33oaL_bi1Sbm6ajZENObw9mkdVginH-Ywh2M3ucshcoD8IYNlL4BUN5-fQQ9VRlaXzGz3X7qY3cbvklgaiP7FCYGH539pzNHj5eL9SIzYjHv7WWpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mco08Pc5SldONw44AhwaS6VgQdH27_8bFr39qXaZHkHDsZJckkNYXjJKIhUX6bruZhxzbM_5elEpNdpy-VuRUr5qFM-wckPtFz6KJKD0iYfDdq0z9MDI16AdUHfvaBX_7lA6aXVstn1yqmCMxHTU-91yDigIXqRS7bZE3jGeb0TgYtSiBaSskpqWg_PihNH-jrQn6OXm-BrlT1ixha5CCkFNpkV-Evn13sqX2kkFH25gL221bGWWonNVk83BWvjKh6-bDo52GW1sBU62CmXiJ_m5RnpsBN1t9QwknKETwYM-asRXL2aXG1FwJ4re8_Oi1sVsKwOrlhsQxepdu6ODbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHS-9Cjd4XlDi02tLru8bivCnKzy2hpABPZiTDRx3OtkUmnvIBeOW_HJ4-VF66fXwQzxcNrqnCmkz9vf3njHMCy2tTLvA0yE8wxIRW9ajwwO3umuk-yZextRrfihJb55OKbBs0xir79cWjVqbmEwGy-uSXq3-CxXuiPz4zhLBdrOVRqs_E_wnM_hoh8bNjZTXuZ4fPgCxRUU6tlJ_iADR0-TGut150_xhx7ESseuB1nFmhhbOF5Kt73uznB7uTcwm1aQgtxVURegjkXoGY1fItBK66HbidkiGbFOWXs78I4Z4Zs7qJm-IWGf5qRYXcjeyc7wRB9aEoo5B5Fl2gmrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UpNKYEvJco5t9giJoOkrPvbV96TogcBWspAiSk-iAkepusThfL6u9C9OD3o7OQSjriE0rMITTiKDLUXn9cUCzLsE6DCvILJZRYY17kbJASk7CxxmwhGOfoNQJYR-e3Vd9RrHvOuDNjj5_2cIMGdXDxMRNo3h8Hw8cQ0_2dlSlVMxG2Zroq5V7ew3SCezsMQEAJe3Cs-eBfwJr1Cdjee08CKsGMQuirgEkMU2iPZm-rBzZazeYoyrhyzRg-SGOz0e8YOzqgPAeZrv_UFpTxr8xelIYKiSnWCRjHQ7TlUU-5IQb7DgDgmYVtxOmmK-LOOxF88-jXrOXOzgNjg9MeFLzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoIhoO7aS2QXmA-AWiQUaxJ0VvJ2DjeTBHBQ9IaH4RPQlL4jCnsQQwXWyA11FeX_aI2T8v95P7awJWG_Cz5lUdDMnEMDAUIEtIyx4XPrM_FfLHQ0qhhMfMuMaBBt6M1OOeNSYHuNsFTXTpsWQaICAv7hM-HDXW9_vN0Md4rFpULW7qc75WQMdv7p_a8WF-shqWO3QR0CLFW8A7eG960c9cLbOz26i4wBcgAeiH3QywFvZfVfspw7lG8JZ9GOjCWXzdXAfk1lmckmJQONgnsGoDR6MzSMlv9VOJgws2ww9AYZw4aItUJL-NONW8BKojXSpHFjWWpCqv5-Bczm1dZFqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9_wVSYXfq9otR0Aq-wdyKY5hJxsnrov_oLGuOTu-3p-0WJl-DIrAISdpmBPnYdZfC_5LDh1l_e7iNigOJLyGYvmrlvuOznE8ESaLjxOpo6LMaI60qE_eMJSPfBD6h_0QevtxGk598n04h9T3IE6HeQMIXQE-5e3rv3gN2JuFCc1ujQEBipWu4RW2q6gw_UTA4mtvEpttJTaNavDt_Bi9Dv5PDfZ_afG2bo5f-qMUo4o8K8ScDSZf7Vjs3HxBwhRodt-cHGKzVIBHdiizOF9pPCF6ndkiiFoSs4oHdZRGdkLmwRr_Kxp9ttwMODyzyfLJuTNEKS6qYyJEPsawGvz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1qeUxY-QjU6-pzyfbDtglls8_JSrcXSuUslLDn0ddeCw5ozTbmRQKpHskPK4L4PAzKy8gC8mGcFxkCC5eOmbm999wVwi1gby8dy9t_e3kIg2CQqRP7wvR2HF34TA1hjUzJZIlwMJC7o5dubStHlfj8c7JdcCT1lUmL6BQH43mpDgwl538TtGQ2NSWvlrcjXbpsUAhxVvmlrUVET19FV_nNMd3QxBLAAamGxD6B-1WWdL9ox4MtGZZXS06yr4kYQ7BQ3NyicIP6ua8B9B2tNvJToCpJvek9uBzueNpjyZoiwll2Mx7tiSfaMbKqlf6BFKE556D92ncOA3IBgQUXUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRVtJpmpd_QmlbgmAFy-iJmeFe-f7uzRguHaqpQKuUCRso0xmJi2HYyKeBariyAryLdAmjDVisEpwPyDk_8N3MDZNn-LOLvQ_QlDbAmWT9afaThp04GFI4Ew4T4QCc-piBXYsDyhNgELiOsaMkgbJqNiRGlBmuffqQ3ws7dNwNvg0kYUk_doKHboaNyMlmWbQHzwZDm8YZ9yTqW6bPqns8STqxJE7F2DwJ02pLyv2rdhR92joY7qGd8vihP9biaqUZqO4xKgFxshCJCT_BPCFjTu5ow-xTi_1-yqH1Vn2W1dZN-8u9xocpKgAqtZNNB1vazJvwLf3K_xBGIGTs_oeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ror9rglwHMtpj7xkHllY0aFyys0OHRP_1t6dxdHZY1M170bax8hsN9LBPNuZyLpQsvawtsdJRBLTx9j9nYEgp6AVLZCZGY98bDRiWseI4ZjNU9miWF2ms_FqrqWEuVD0scBsdGtQl0PmV9m85Q64aNF_GOPyo5KkGPgDumJ30DGTuLIGJZiYHt0WNXvYKOomEN8EPmihLf35UxR4R0DjmD2JbV6VKA-ACXAgLvSFP6IOvoJd3xqY4LGk_XcALbGwPeBsLaUFmcHohQpOnM58ofeX7KXd5HhPjUsJmm66LOGsaGKmgH71JDYW55PKVDzLJzykbKyuEqXyuou2PAO3jQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi3cE0EkYbn7SYUQXTOmeeaVgv6wTJdmCHKAd2zuZM4qdK_ahYAN0esRl9GIAZLVfhohejGXrqEehrlDceKhsLqrOzMO3NdKhe-ekeMSMV2E0FFrCl2FCsYd0F8R5sNZBytxQUmXyQvk0O4Ut5umscuEdLElInEOKwvw9Iv-q0N0l8xkXHktSf3KNoGE8eFUyBC6TebZAT2-W6yW3JWp-qFxFGlA1US9JVAEYAZSM0XrW1jUo-aUrX8v9lWGfnJvmCt686JQ4bCJ16f-OleGOdMyknVg49tHuo58J3EGxcnBapFVeOvhhKkhjGE1BWRdORBq1-m-M26_S1jwD8wtWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmk1Co-16RvXdVmx0FwWm6cMqXCAeQ0yJbcuufuMQBvOcumyCzfbjbjRPQJq690jx0axlXr82UVOrnik33ID00_qhZtMnmIesytyYcDqkjSAZQaqSuI3Lsu_SubJmY930AhtOo9uLAt0MpinsTO1TWisUwU_8RJe6d46A-hT586n_fWIYg7ySTdgCdzBjKwgrh_QuQonkNZHES7ktiDXGvf2BLpIkhlcQp95KKATJtIvuexEegr6zRZjHLkphNXl0t6WWMbYLxuMIUYrH5qWzHysFHrFncGn5balqqlxs6jr_WwEwcF7u7nDcn3He0VpsDBIbwQLaF3r9eYZtwcnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9vKwAXNQ-sEx7yr1mLG4hwQRVJ9cC8f0G9P-J7nMfwSCrPXHJtTv2RCs65d9j0dOt3XW5eakiVDq3fTri8RULg-Ox8TkzIpZ0SpFrpnZJ4qV9KQU4p4wOZdGy_kbjlm1XfvHLSZB7uwchAsRXkT-lzeedhrUf8uLfiBUDLrQeU71CmN5Z_JfvCsZL_rISYQLYRrEPGcfYiKJXVzzzor9HzvV8LJ26mg6hEUCuvgAzPByhKIVNa5oWu5eTxWjS7Qz7RxyHmBf8QO17HTAKaxY8p7WgY-5i6ncbV7NvXcpxBrMMkd_UoyS78KjHgls08tbJ-kSbHULgO-bVbVSgN7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsONnC0hPwPVk0eKt6SsUfINR8pCQR-HLgmwmgbyicl7phnSqavH6DpIfjV5nLRITYb9kY_gPD_hzqCXSHGqRcvBvbDsjBq4a2o0DIXWZuXRvfei2XC7JZAvUKJzuyDJ9zwPGpLUJOMi4OmFwOpqljLX9j2WOBJj0cQFPv28sGYB4IRyOTzAcTcxPD8tFeW7m1-NQuaDLXVemFVOhcVaDl9Ji3i7p85njTDb59WLmtJMp0HSFbueRQ1FcoHJGrWKnJF7dqAaYt8cC2iP89ozSWcfkbsEKG0eWrEDVaMSEryTj_t4gg2FHWgavR5vbPYcRd8CzNLIQrqecELbDKQOrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l7TwHOBEvl-YejS91VTG5H-Vybx229I5fzXoxt8VW4h-Oxo73IFKnsO0vUfU_8AsVmnqbRdRtAyranp5t_sA1a80nbhSgpVjG2X5An2wbw8OkzTsigaeOWb5aEmH5gsA6cblTNreVJVXn4kxqyLzGtGPwi-oyrzemVpHlaRz9uXtzUHCXRCsmprjgO_WhEnxv5YLGkVfm-XN1ahmNhz9c9FyK3vPlIH__Z2SQYj7A6vD-A_top9QduDNz_moPudpDryk5OfbWy2OmuuU_DAVHIWW0Rmt35ZA8RO26GBYbxg-b6UdxmnpkTaH9EVC5ZzvfN8ZPmbOGcsIDd2E9E309Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6JRXscmlgGEtCbV5DU7sthXW5bXuyJXMAPlZ7PaGHNeAVBU1zjwXTYCVo-X563oSGqV_vPuGk8tBMIAJRoCRW1u_CHAtduRzvnp9fwnpJ9klr5uA1tYnPqRCf9d7AOodnxOBsVUrAy0T-cLAj9dahQJgDELl-g7lyO1rPll_ssVeMp5OgTYBnE0DvsfrVq7cXc9lYHppSasJgwKDTO1LMSjCrmazoOxax-oVt-EAvi8AGihi6K0oVF6qXgnFAaB3fiE09E6LgZYSUBd1HkkiXJDtz-zxezxNVZivXS2nGdfE57tooWvQ3FdLYm_L81PsSxwyKd3lxcpvRndx518Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzmRHlGR41cze_vgdP-q38CPB3x04IIqojEFArZBRxJ8grrY3wDSTnitVYfXmuaTEf4_BBsCNjnBZye4V-SQ80xdPUeXe35bO3FqzL22MHBVl2_aqKx5B97tLRgZg-BFNbsGi2j5ghrjO6QIymiyryhTxwF2dzHvbbL_lrDONhYSkt5Sdl2O3bb8gK_H3YLR97K0uOJfZTq5zesSciEhGO92cGqv0N2-VvZWtgYfi9KBZXQtbuaJA7RPK8Y8tQ_Vg05KfpmWwM113EvaY1LlqSY-obc9FsyhJD9E28ofVl7hutFWsjebntQL6twCmQyA-JeZZ5gru0ocM5XLu4ECVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jua3-uNPzAsquXqva1gO5HD8D-Xat0qr4gl2saOX7AiBwfNQ1Lau_qKONHOH-lpEdF5I0LXm4nyvUDynXJheuwqogR1bXdqkZjF6z5qiy-kpX6kqSksWO0_WhHbFV7_QFQH1QKvBLaySp_13PqHUQkUhJEqtPtRAALdX-eyuNWo05ILVjn0rkbiuBfINAkQCfrJIRkOvQj2m28y9ywfIpvV3Ky299PwowutWtPzraS_6psExUDbLkXWh38ba_o0GZo0Wt5FhHP_BVRBHSS5ic86-uwWhMaT_FeTwyuYbcH-wtswjtcKY74khn1yDyLshDYeqC_hC6nhbPvoWaHieEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSODkZt4SlGilENi0t4e2rdfxhxrz3pYu6tFrpANN-y6aKJlrWyf_aWMgnaVTH_qrjc_FlhnjC8jEn072h9nCntPfMxdn7QfiIDxYMF9igx_Un52_X8Ign4eDJa4St5q9rA1zn8fijXGDg0tACHQwsD1YzhhSR-gh1iCsjKa7jnY9SAXzy0qC60EOyheB7My0otXGpsq6kyZJUALDyuPZSRGCMpipcFqHci2mN5kNZI_E-F6MpSWsQa2LXZnBhlIz8bwTQVpSbmd4QLI5uN-cQGIsuvT-mBT2PLDSXsP1wag_xq7XfXW8-Vfmsu1r5pW4KNuQ-eq7qoqfIhC2nP25g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8BK8olco1knPDzDEHVUTgTGs6kMBK03Gd7ggjBiUazGgD1c7qwQQbaNOulbzNMpU6QSvy6p2r4q3Y7Z42uKOsyjkKsHTeskUxP7ug2AtEIzd-JeWYRQ9IM1WfHPEsSbgA8PxufYfSt4gME5hI_D6AMpUjTsLml5tt_1om2boh5UNrohCSQ6WhiHnPwNgDoAy7_pJkPL6Cnmbi8GDmf8sC9evDyNsg2Ws5U8DkCrkSBmUDw9nEFi52s12VJdhxNoViofbdEf9hlnYd2dhwzn6NzWkfRDSrYTIpGqiYhnLN-mAvslXDI_Fxy8qZNr_bNMtWZ_XH-jsjuri-3Swvq6CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DW6-XygeqakE86iUYc9HUQFk4tcfwc-ZFrp_Xl_JaBeoQDoM_QR-odOIwM0rFuQKRmbkBaEZYYy6fOQeYW8oNj2QR9_04o-UYz5SGq9mvDLRzECRo24SvxfsfhxLN2dmEtADCSogIiO79-0eyvVHeM_EHCIrDuGVB4Wi3wfZgsgYgPP_NHqZddgZZsaarqh2k9sUIdgK-LDTq63SR8lYYyZ41gWqWiBeV_8ztmTGfOxx7s4C7gkdc69B1UT2yIW4vG79UOEXhyvVbCc9kjG6SRYBgWJ-W7XvNhq1mZ_PR7oL2GhEtQbrGcta5htQLSeAONN0rmzXUpGYFB2We0M5YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cTC59Ok4eYKQWNAXBd7Sh776L1E-mLiXI3fgzjeRG-JEY5OhvEZPPgOLEeISdXIS0yQj1RlpKm6J8bfDo_tJKm7_TPuOUUm0Nt6PrRz0-Dg6fWK-pzSOalsblhOcE0lsUJaYxOKjh4hqI_XzwtGJt6X4-SoP2KTykH_i8leVHaxp5GWgWVaK_26FCJ88Lx56IHQ4xc3YDHdp_1EcdhaC9DTd1H5_kYkK0AfEL_iYeB43af-VfBf_tpi3vsbUNqW_f259fhhm8i0qkelN66JhxK9LLGfLGZOggqtgPteEtY2PAD0LNZuMmCiWSxsTpIpYu_6QSO8MQgOmIV2WUbSbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFHEpAcBFuVnImKHCQUwo_1ByYJHGIoHLppeKZj3h7-X4EYlRhWbtTzHJtFEz9Q6Jh5x0z8__DuNIMT5MdIl8XBVyjkRtii-j3vqXGHnciqA-7czXB3wroGeQUTFWPhc0UwNRA5fvWHs50Tbnggsje6A9tzDvYtzcsZTXwSXyq_UBp9GXENCOpIJQLTJHhk1vUoC5eLWQzI2u8nBThj7mumKQqnaGTVhQ6B7PF7cH67rKXd_ryg0u0go3t22xFD1wanp9M-gRf1wL46-fweEKvIELV4f4erNECX-xN_9GGpan8FoO1bxQEr_f8u8Mxbql73aIZTuddA56di9InssTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mV-GadPW9ksSRcRU05nTjZVa4rZW-r6FLcGGr_2G_dWepbbwwspyHq4rlG55MyxLxcGyZ6m039VWONJ_ISAlfGDcOzGqkv_3sjyIVrPDO_slrQD63YTAexFNU89D51GiCXe198CXc9JnZ5wESrrrGxXsD05s19Aope5F1vGFxbWn1sTvt7jas9eIj2WcX0tbg6cER4ZDQKf7wuQv_cASzOraTpxLVtULjmVv9eFuMWYZKli09UAHBpp91zkM05PZTdhliJCljkhuX31ahQZKvOdmgL4Ddez_J1qgHW1qdL02wbnTOPFV-DQKhRccz2Dz-RJo2UbZPx7apRZk-cui2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFEdeE9kwtA9ASe4mijf-lvvSMcZgS0ZaxaBZfxZjw1w0sbV--QM_lqv9jBsSqCHTQq7Yl_ZLlQkQd7aO1Mvr0oEaqnhHbdSFcn3W81s6OW33BwQmHwXssK8Z8SW4L03dcr_zu_-ts6FVniGtHhCf2b0601Hv8VTduQkZOieIFQ3lAe0J60rfcCYcWUzfejANgrkqLD0HMwUr96aOst917bdjHCeJbLljblAFGaIZ3MFL2fcLNCnHbkLHhUv-2yimYJYrbQwTPyjNkETdj7ivxuTssjX2YnxkNKpp8pJja_cjO4K7F3c6JVGSQf5-5zBV_D1xVuQk52oyfoYn1lrAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPMiN8a79DP3RaNUpTIYZwe3QFezpPrexqLxWX2-wNlVa87UXvzqOmr01tA9BfPA-JLChE9sJpgDHd2U3YrbGAFbvrPDw9nsoRmWrYw69cv9GPVdmWfMgPcF8neSMC2G0toDxPqntJQNlDzzhcahmlOpbEUMB9fk_TIILSCEz7yOoiYbebjB7RGxrdi2tP_KvoNmB0N_6rzevg4uOXRn29Rz-qm4hI7dgQChxb4OXiPrR1pLjV1kkPyJhx_jyM_vUgSw27kP0huofSdNLbhSsXHZOnOg-rCH5psUG2BKfKTBDCXR66WkA13JMvxbi8Q2FQUGi3sniAh-Z-oMoVfGpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDz8iO2qnKcGnmbdCS5VkDyyaX50qH0-bksD_XlDYkncocf2H3jQ8yp9mYs3vCy3dSPHmryOsggRgKKFxnZ46XmXn791_piEDq4SvhHuAGmPg7KeNRjHFQoOE_Mur50x7aBLZIQm6PkNUp7k1zCKmEGm969uqMtBCbsHPwoAzc4GPPY3H5Vae_D9LUVA542tTNqx5PxjUe3_7xxSApqdnXf8JldF6ysQT-IWfHNxgjg9_H0EIqZzJKOXFeXguM13_WwhbCY7qFcS_-gZfqU5LtM4X9D-j7WniIsUapqM5fR7gyXbb_ykvZuJdaFGaRL-jUJTEdrHHKvUmGrS9o2S7w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIRbHUMF2fwhLV9ki9CGEECaUMBXqRv3y2efUwVDj0bS7GBPg4rbSCmOkzeIZCUBO3viP2EuW9QZsL28ePWn61YEscP76yL0ZwMUTaO2twrVPrF_55uV7thx1GEFGLSBILOmnFiGNZnB01T-UdIO6HeE7rn_weCTxQDmYsa5KE4BapJGlATNR6fZwe5hKqe21XC6OPN8eD6vo0j5SYiJVVWJViAUvjNOBDhQ6lsEXX75ppbr47T_MnfwzFIy8A5ejQF-4WGRaH0mKqNV4cwg75EuOpBSw-Le5aFXD255OpEkvonUFFzi2qFFrgyqjTHiiX7K14RD1qx3Xa057TQgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwR6ppK3J2fvrxhZhpui0LJ4h7C3GmvRQIEQvRnm0r9HSGz60IWRYi8OPY9OOA4rC5YGtdDe7ez71yDst9GXbfe82SJ0R61rqNR1w3_SHIokzk223AtCNtRIsw4VKhn_t62wWQszojLNkQvSj2tgbduFsxi1O4b-eyvH4jpnhsELXW2MTqOwIAlgdK8KS6GV6pie1asNgr2gA49SP-o0gp4-BrBzPU_flVnBKmG1pDQOlSKIIDWCffkdTLQncJMoql05iGtK-sjSsaH7gA-qQILeM9hjKJryqtoriIVZxX3fVCQTkPvZWEvG_6RFeUozs3Vub9OqA8T5wopkqRVlkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HehhAbbMLhmviQBFS79fRAJCcTPCTEdia687ABvtL7M6DjPTaJmTbkXjcjXqL5NEEKDLr0c9S0WAChqR-VfMeawqTxJ-Yg_ZDOzRaUylQTgh4F3fCSauK-aZh5SNv1DsMiXMhvPRnVOmrRdKwbwNWkMNkyq-pGIBp7Ib3cvtu6OEXS7eBPFe35gINSDglkHhMIiCr2TrcCWmxuqADl4X6nwvYpFh7Qrg2FdHCTJJafmkvmQwFUub1OTBZl25NiuYDftPrF2PHwRJnuzdVgPVpnD0OylndLjrioJWHihr0Rzt5NZA126c7rqfuqI6E2z0c9BthzasEpEZac4mLjFvVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpkY1DVflVO5xeb8WKNGbI6gopRMWAQAhfs_lw81-vrJRT66MYzK4PCreoAAMNIA-5LBHLSHFbT9rts422Wn1hxbMz6AZXEcxGY91OR--ZSIgD7i0-uh_6mV2VWpjdb0cjTzR5vrpB5hq74gylkTORBdIU2g1yo-Bl33o87xPwpq4fbOpw32Xis3BbvDMIe34ZxiOfwND-ALVTX6UbH3g2QYlDd5FleIhpWI81YvevOwh3mCWnBpMW5FP9Ax_22quRrDUNRuyJwo5MyrBNHq3yxGBe1r3IP-IR63o09p7WEXR4JQE2LZva6G21kC_eBKOB4RH9oZvH1az6VURkAz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
