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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 05:23:27</div>
<hr>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcR6_mOgBqhmIbQicjw1J6gb8yD6_gpOstgH-R4PTvYY094kvb2PiMrh3Qi1zbLUxFF_E-Fssrk8PBC7fxZ3FkLy77teYRYIW8LIM_q60vhVTy49_2k29bnuwdd8ni7frxYV-iRCNrpPjT-nX9wu3192X21NnoNZdnvCcj6ikypz49azy7tTr-q7amkCDdnMrGgHL7O7k-nyz4aaLnlbq2tkmAQ-Hmjh5HJjBg0DMGckJEOu8i8BYCHFUAYso0zmt_pLmClII-bTOVePh19316-rzJciX35d8v4eyKAR_IG_mvfBgPBHUqejUqpsTLM_stajbh3VXbCxaXRa1HicCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش چیشد که به این روز افتادی؟ چیبگم اون شب به جای درس‌خوندن‌نشستم بازی آرژانتین - سوییس دیدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSw_7ia6wdoDUhipFnvN1dGrNxu1MOJYnOfG97df1_-fYciq-KKpVtSMirLWANvpzGLmQvOhGHVd0bu05FAlEUh8lhsl4qgUlGF5QdvJzRT8OS59y6yhrFP0ryKKyLAssKBiTKF0EuGtTYaNEXsLpv5zmog6e1po9sFH5RFNCQjTNGI8PkTuRVAaGBHLl51P-MavYLrdpuxvesetdpyOd_JkhfioT863cuVGsYebf0Nzn_y2f5c-igV0mDlbEJkl4df5si5zmokNoT7d3SS7tHR3P4udBcGVtH1bX7dfliFe2DTz2fe-5bWocjm-yJSA4QMuAGcSCoVdGJWEcmg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyau-GVGPPYT5zwCd9GpQN-Wzq1AWT-pJ7f2Ypt7xqSOT8-S6nUunn_N6MgipbR_2vv0Qjdl9v-0YcZujCyglkrQIiPr7uRhtYNyY7z3Z0a-BKe00msi1svcqQjGtV1y7c42GZSENiEJsv2AX36Fgdd6K82bx956Vuk_VU9jhjRZJlz2jUmOtwwWIukMgiiJ_YIRDpECbPzbnM1WTEzhKqc5PgdKmf9lddXHATxVLhIuELYoCAp5PGsHQPv0wgbV1K3MTfFYct-0zDu0gjggDEj8nq8i6NMKIFFGVbjToAJC4IQYvlEK3p9JKh7xfUxaet36rCiuiChyY7fzPZ4zRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTMYrb5y2vmy0VPc7GxHXFkC0s5uBUENqAMif7uLEME7gkQFcYOXQ25d-gec5rfFZFhOsvTmT4FyY9S3fhZGxN38cIlfb4nyLKzD-EQbub8dPMt83z569JGoTTz96EwNJ7ypcJrhBB9ZDYScypyw1NIvfSU6AZ83W7-6yKaEd8UdkMcOCzW4mjDx-yIDF9OpXgY2fNDpvT4OFMGGU_SauANIi8bXlxAdsbexvmYWbPGSLuy4BE2DCy1ZcJU60xdL1wHxIvtoxeiirVwEeYtj01jS4Ni5NcWxaQL3K1bLvrkquYMrDjNpQ2vzMb8bliM-K-pT87wAZsAwyikUHzr5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvgjxT3aZR030Mx6fJoAKp3iz5PIP7jedz26VjyBWINBGEiIREO4nOfzSmgBv9iD2n7FJhrIly-ZhitD3Un0KuPVIK-NKIemucz6yXSELLStqNwSENsALnlIPIHmBvj0N7fjEGW9niuTaz7sKsuROcmm8Ifvf-5z1jZl0JLnijVESFsM4wufGXdTV1l-kMLapqvqHZ1cneybmCZWsRrlI4W86bC25C0EpSueVFKT9junY18tbm5XnIyk5Qkcbf06BnYOxTbX97prXCr54idCEDCb0Fj8VVo5eSmurwaEZqA6BZPzeuY-QutJXYs__8En2IHbLVFYJ3FrMFjXsspfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQk1jGRnlsm-gNW9PUUQakEjOhdFUIDNISjrJgL8jAwC3qmAcKs0188ZnDJ2mlx6OZaLXLxHkijDna7YjW-4AJ2fEWQT69tVgeTIR_uw0OLXzMnACRDgxFCl9zGTPyIhz7JeBoT0ZnUGf3Yf4E-XLK30foKKFAhzfn_ux-cgkf9PxszqtU6yX9gOLrk6UFbwRa3lDUZndDY6vn9I7IdtCaMWM9IgnZIABAAH_B_CB1lsFKX2LGAkAliegH_ajBQTgFUeciQ4zgof2xn1i7iJOuywAG2brDovnr1bIsLBHtZy3dvFjOBovvIvDStxr9z4-ZhNIB39x7UfBonfsMvJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ieh8r97hnYKrRgz43i9Hdz5hraqt66RPjK1T3fnXugxntPCAc23WDWj2gik2G9-DumbFrHbxeK0Ex82SyZMp4RKD__Qbifavwnv7UfBtuwXcjxTEFjXsgxcV9OL3nCVJD36ttENDBRQJsmSERyjij0Eq8ZsEd3Le7Q6zXHO2Ie2A2oZZsXtAfhwgwnlJXKXYB_M0XZf5xVtRikjiya84Q6hyo0AAI9kBqzigvcFUJuEcXgFCT9wGOkwtgE3fQtUQ_G5KRmRQdW-JqCF15KnejFiTHkQEHsPRS6PVNP3SMpA79lBi-IL2bUm8pHSEwxRADlMA3Yk5zQD1w234AAmwBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHZiwdDkVBa6hFMh2GkrWND4wi05SNV0YPALq9sAPRHOup6drqcKykqh23yGLwCz_RFKZNtXyi96cxEcnY4DZ6tpfwPGLy4BpOsxqa-d6X9fRHPy2J0rwGRgP_zxiytS98ofeWcW8Y2IoNMb8cKuz6P3_aJ_7I5T1GYumTY4YcFleg-WZKQRQXkSHuxM2USxw0R9diZf7N1Ia4joGmDXPhqJA9_QVrUDpRUAmQmHF5LsyoRMnzcF8_Oh_j9UAG_RDTP_hPVqwVoHJhHHZphw7lFRYE8SfxFq0c3hVhzW95Pr-R3GWynrnaVHklo6-rNZ2iN5qPg59g4ozQ3PUsnPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rac2itQruu8G_Bdos62hFBt1F3iFHTr5kCYFF2CB8AePqed3EOmnYKJ2UjnPqqkKLN7XIJsESFIZG8BGmu1tlsiwnfc0JCsaqTjlo3UL9CgPVONj7YrbDp1mjNn0XUtRLBHTKGOnetahF1hw1la7gBPXY72bGoG6EguMPX49Gq1hF-7WiAWO2cAdbZvkA5hLRs6-u5dYG-F5B3AYwiQvNoLKSCzigUHauq3Kmd7__RJvPjw4N15bA1xWQISDdG8Pi3Mm6z-igTjy6gY3m-m43Vs-vZ7uTN5a_XCWucWCx-iJofeHeb_GbB91Tea5vJ6CV89ix6N_Q4zKXBjiDsbWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDOUBhMRhEQiEUYEuw3-AtBwcH-K_96V551TXnipRJf6NurUO6V66VvoS1xu3fTIaQpYy0buPauNZjqmcrqtgBKX8QcUMlvZZ2yiXYnXZh5BgzEC-3o2GrooZJe9Cak9uYidk2vNX4Kn6Kus_VADk1Dh6PScuhkgiQZrNLrnqC5ZU2V0Z5XBw0bKA59VsJjZ-K7mitq1NHGJE5LIz2909ENWz0D_AFR_eZA43Xg7lAt_5gy4k6e3sTv7WOwSTOLIEIVxaut8__GedmSnxal4JOwkRNDSwipcbfumoCreT-eE8X0mkfO3Z7F-XP0A75miRIvKlnNiTcXUpGocE9cd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2t8uD1vQ1slxmhdwC1fgc_Xsgl9g_sCOajMhTDSrXAIifv1ySE6UhPA6MvX5gk-LiZ8b1Ry1LSu-wEqrvmTz-9iB4YRmVFu2LjwBUcDCxQj19qkcuJcLQvvkL0QSsHcYPcwXXI9PaYaU7kMkpLeov_k0HHJgvNb7mG51GUhWWAHhXnzA2JvU6wfN0NE99K29-S7P5hnySNC7H4RaLrCKnF4WEsvkthDMqfw7vq68So3aQKvsDVmJiTv-Vl0u7Y2D89yUlExtod9YFNy2wYijMjYHC4QLR5-4AVIEVSZnfuq5iwqIl49hWM6XQXY66-3zFXpPt8VO06pBCok6YN0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C91RQJHsBe5o-4_lPfQFPpBg8Vva4hYDwm2aTRcr93qJV53LdHLWbQxSx-h6FYVe6VxApfkOA8TJVYCA3ynexUJmkxh8oxWonDNuk_Vqlgq9vwpOz1DesRUwwrUWKdCGSnqDIAn2h9lKy-fdJL75zOp_wjWqs5Z2w1l2T50nqQQzSfRajVlyQk7U7PNsyCoti4CzsYMsp9EWlcpHgopMIM6vfOUmXEF9rIzwa4oCi-k3xKO0_33SFZgXfqk8kWXzl9MQUfJe5CKRSu83SfHzfJ1OdU_o7qeGpaee1iXscrGBzK0G_G7mjrBFw8ofL5rpDpyuekQxMGzlWSP6a52mMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9_kdq6oQwjluySRo-8XvHvw5SFfgyqVLMFMuS9ey6bzQWmJV-3-KiunCB2xfDqdtHF7laucEQkNxVRPDUdL7P8e5QsV68IriZCrCtfRq00liVXMb02Tl6C7GeWLZsnAbmrgMbF5uQNnKOB-UUF0jVlf-TxR724Dgs4hmc4zfcHO4M5hbii9KtwPszbXIJAMWl8rSztBdvbZyPAF61qpz4s7aWRA1t8sLJip8G6gVi6G0zngw_mGeGVITaqPMyLnILtrMQUzLrTUB-O9KnyHcXxLV63fWmHevNJ2NezFoWCt_SexwAjTJ-C1rKof2FKeETAC-kOOYcyIoMIYBRZ8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL4YcqFGqTQaVvTOTwBhkZWPC0uGGlx0PUYttkgcJD802BtWl3dH9NqO9BahPOXdPdcfLAK1IEw1qAmM_uQ9RBXDSDzaSNyROtFbVoDYwHg13QeAHeVuWT2cdziVG2hEYI_V3nkFy9u3CBAbhq_Senur94gcJR9PQuXuit8qDYXPd9rTioS11-LqmCZvxNHMABG3qPGlPcaeOcggIzQCfxhXq9vp-RmOrWV5RXj6juWDnWqOsgTVP6n67h1Hmi0LYJhYagCFlm2o9Ud1bBoxlRxmkcVJbhkHGjpYF2yglieXfUmyGTn97V00eUGLsX89p-DRz0xs3rv2c9ZSUSC4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi47YcMEfx9WVCWILr95XknuCeVKvQblM9aqe2g6QHL8HjhhYCzVlEDzF8ldM3FZkpZ2Q5W2TpvIkAGyUX97J4BWEelEt24UkFiOFo-UaS810fi94FYfUorq3aoANkRgwJNO5yvssW8HfYRk7NAYrAPn1t-xiOtqlxenVxm-VSK8oeyK2FHRC1y6_BqptRh-Jo1NprPel9C5kXd7Cunad4YjwD-ap5g3JzUpOS1rTvfc6C2wyWUawpnLZls38MS4GRV0Hku_n1bD1_HEF0C9SSV7a9f-AWkZMzxoaSR2gyajLxsONiurp3gI62fVWffzmMgQ14s0T9QKUOU23WrbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BroDk_LRpNNxwiF6vyDnzf8Iw82G5FD4H5VAQBWpThPfKWKAa825s6AVqFHoFgohbJOm5WWs_RRjYQHAxr_Xwg4CZjpNBpNdllVZtdb9DH1GraFz1DiIdkoX5pxC8PffjLt0OQM8BIfZANjoHnkUgWTvgYPNdTF6MCcm6_pHyKizrt8nYYd3aCp547fNFJfP4JfVwSz2huRRI3oGHcCtdyR79FFkGaWrQXcAfkZZebGxc9OQrduC2zftziJ0Zc3dAcxGHK5ZPGUa-YQSqrAVCM56CXymwKUe10O0Z_gJelgpSSnCn8giCHiOzZ7F4m6tFNOBBd3_S4O26UinlJ1IYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25458" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4aL4KftYmYd6TG0jz8fAczn6NBZqIGX-bUp9F0VUY3edDyp_aLsAj1xzMWb8hKNcd8IU5pomysSAB1zOXkPzqhg2la-lx76UcWhHglIwUhQV7QvipxugiO59k5K_YOgc_0OSpfFfRjYLPeQgAh3seXXQuLV4bVDwcu7lrLYUDuPT8RaXffEzdrEyRk67l58KBidrVbUdp56jWqWN94r8fd39NKt-IF7vJSPjJDos8FY0sn123mGpzWE6iU4St2jwIRGGh0WIicGrpkzSK1jwsfg9xlVRb1hLk3E5yDYCd-w_o8KyVjZADJJZn8LzdCS-Ev-vrxK1i-VRktGnvbF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5h91ST3pc43bTWcKDJsgLS27kmTi9wbngZMRpE6P7u_72KfrVY7WjsfJL_CKGop4KmnIP6d3LGMNxUI3tsQZESmWnD5KnRXITCfRjq0Md_0IXHMRvMo3TSmA_8C86DmjZDALWsiybAUavRpWFe3NV2gMBy31Pzfdlw5sHq9k5Pvopg21FV2lfkJdi5Ao42BZjkS5Nb770_uvsID7b0o3fVXpw-SnoTIxKsii65d1gAYKLrNRM438chn9XzfnSfWYJ2tSgAoYD8JR9AtSNpHeCDmFeQ3KdRN5a-zD7r6okrajGx2F5CnuYYXRktgXH6v4r3jwx9AluWfbyWyHa4Y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upV1-GovYcUxAsA-MqOnI6ICDWgsDHaNhH_HO3l_kGwOqVSgmF80vxP7kEvqfw9Jpe3a3abtuS3_JB7HlwW6cMyvq_UQHcodihnQx8pF-TZVKVbapAW8kvzLYoieCQ5cT9aKywhw6DyF79SOpDbGkQtBnxAFpr8nVDMKUtt22l-JynjuwglJoAK0DCSPgG0F6sS7999zlh9AMOgF9VCE24UFh1zghV4HktdNVRBKumT9ZmJX6hk52LaCz8e-2uGvGElpsPIEc_nO0z_PmJ5lxt7SnsBa4QW1F3D13PfrE6GJpb2lxHN2fCoBd6JTZ_QCWFk0RQaThUcY7yU7VWafRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzhdk8VNqLtMwY65DarwxXSPstJTJ0jAoT4Jmb65jS312RZO-8x6uHCTwcERB3-SNL8Mn-H65rAXuQmacuDtDL8VA1Q953P4OzWjWq-KHg8fqE7eaVkRRRS44ew7V2qtp1WOskzco4RGZIoCD9MsCYN9uwKW8HbxtJvxFMurKm8Ed3_Hex523rBpY25DA2-E6PJEvu4E3xONCK1yB9hDYw0VyQIbZt6s35p3mU7ATMVDyDEDXXL7f_vXXjkXtD4J0nX4yS3YR0__dPM6gXAUed5NS6eZoVTPrApj2vf1jZ3v-6_8-VqXUbJhYVOIOj8HG6Ly-rquwAXU-fWn5M5siQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROOItZ8VNtR9-cyqZjhwjf6RW_hN5Pw3DPWmgMykZLaoyrLgCOJhWsP39dY6b2tEQobJxoJiAFrlcsO4nxm5MBUJe5Xy5D3v-WZQ7IX_UDiB4_T0rpEbZMZSsu_E30_GaZV23OlOVpHacSiOVkAsBzgkkbZVt7dlG0VnE_QJqQTe5cBT_lGtqZBBQUNjM_xodm94SiXtEzwB2DrNfOjIG-hppu06zit7X-TlO6m_b-1nFXO5FuFRay3fXhTXnSAXrIFsCTN-SHKwmFhUE6q7CeOC-0O3SzM2nFWnsc7Ie4Dq39Tsu4_zjhDpL9O051fdPK-2K7Fq0CYs6VwFk6CBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6mqtNOra06Uto_MAKzyCGtrfbw5p-l0DOFTnLhzK8ndrgrR6Tw9Vfmi3CaIEoeA_UtYkhZ2b6xnfHL2UVmj5dEPIEWiOahiUbLJX2DZuzvYagbfR6yaOnFzlmPfb1pzqfpzRtp8dyVK_IUBKKr_RK4IGC3cl_SwN20QZ5mdZ4kWcAm5QPsDqDvYgZqOLzYqhbuy3rUoQHqKf37hngKgW5V4KmvNWD0GegxfvMfVbF8UTrnwu2K51vBRGFGPIZjaNQBDm-BQs61EDYRgR5ZaX2yufN8wKSV_PpmO1NfjhRJqwwK9d0uNQjj3sv2yx1gnmdTyTDE0SQ2Ffw9RvQI-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGELx7QJfVJSP9bg_y9e8bCx6BX8Kg1x_RLeTPbFXsEhHFkurgcmRiOAnUj8gkH1r7W9V9G_06zOPE3SgdrHrHLPNAhnEkAU-17MyVOxlW27J1CS63DLZGMIxlfjeYXUH1U98J5QCc5G0GCaD8_Ea4_3icnvDIJiATA3BrSyHU-NTXI5cZgrGlXRBKsq_a_bARM-D4lD4smNYZRHx93aYOZGOoELoxiaLJn8FyRhgvV70IF2G8BEdhGJOv6ICMJMU8M-NY3KOfifBqq2DEC1qK2XeJfijpv1KcO_fB8Q8zR7dIVTswDeWHNti-xQHZRVBqnYWxnJjLAHw5yKT5bzdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WozHZx_A1xHpIvA1ItXeTj8-881c4seiIikImRUCsH9Vo-JWzI5jDKiubgmEu2x1NP9Fe3S5q3TtwkqgjDvi0Cup8V_7zX7OmttBQlEjYSCs2Y21pWs8y-WRu8DYqULyKtvuFB3G6BsqDd-KzDLCET7ALnHCsBZEsg3n4NjWilVaozAHqMuWsALFbwxtPbQbKHNfm8ULlq3TqxQRgPJoIqfoMvoXNWMq4yOu8l9l8HINyTbs_OytwuRzgpvGPbfd2H3J3ljh4_qZig9SzQ-DR_BpyNqpw_aELw2fVSKv31MbSpGrgM75tkawsQs4sq9iKcRUglvoB_5XS1q3VdYTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WflKcjAD2tM75HHJnnsEY71UKD3IfEc8FTZDCRpuLdnpt6RXT3clUOsHPu5tEVBZRMMZFlQBJmkG3NkkNMTBou8HQvUKNudm8pB2LRlsk8rOkVaZf-RQXhDKOXhOfOGNucXcRaBoMbkk1-54tXtpebSBmGHUSXOjakB9cwoEXXLbyt1bypKNk34xS_AR1ujttiBb1eGAw9xJz7CHV-N5XxL-OrRvqmNm9LRrbP3cOlvd0yJzOTs5eG7WWZewacfQxQ47mYUdftJttfUZmrZEO8nyfxtlZqWh5xfmUEcBpSDYXKFTAAFjG7rlBcXvC56aUlaCjaXuNdmVVOiXtqRMzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MARumHhubyQUx3mTRlqzLKDCb6fUAknQigwvXGri3j4mQntTVMf5w9QfNlaMPi2yMlMhUIWHIkyqkXd1BYrOXcrQAdw0tOkGVOmu7XAa7VFuco99nagJkSz6P4n9WGNBuphZEAiAGgfDAYkb13TB98brHj0PyY0SiTH0d204ZUfM64eUpn3787390vukN7SqvBkkeRMOr6YN1d9BJ3_Bxhwo1bWSWSGFHzLtZrpLHLhAzwWx24otjHAne3SFZ_QJ5tDu-MZSkJT4ke2j34m8a7R_K1KyWeYaymxfR2AhKiVvSwGNW4KMakdXL3Acw69QWNUR33u-Nw5vy7ztRD-prQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmNyk3Jedd5x6PlqbB2zaYYSDkNBdfWSBFf8SQRqpL9mHuLFlo1nxTzromT8hx1PJ69FXTIyM5r2Mg1cjY_ZHEjB8IyGdi9SwvuGbvBeb78WZcdICDFHvErAMWXUoVPtVWVLotvMNfxQ5_JgJP3b6QalR4u9x3nJv9c1ZQhIeHrL4S3Tl1OmpFndGyTEOOmNyMRSAvbFTHw6EVAuFJrdfVXMgxCC7enR_ZHdDlFa6eZ5HBqSiWLNRk-w-lwbh4cxZBY4kqes9ZQnQ3MGKwVjlyHFyMp9hb7_BnIsdhkrRYTQ-y3SH1wT-P-hnixbx1uxPEFca0QTDnnVfKRbjrqPww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5TK0xcV4OtMm-5OlE4vjsmcdXxJI8AhT_IvDKTBjjhzyM2ohxXJFZW2IhNGQKeRR-0jSTZGW8txTtms07UNvek9IfPYhpFQO9njlbzuvF1qdbxltj3zifvI0pU3dRGKzPNL7tswy6IOh6udxBgvNkSq2oBWIcNY76jOM9EjKBzD3U8zmA7ZyH1-UcYQS2EpNCdCGwUVphYvM8dHiZfifV4kE_fGM1FybocOII0pkphZ0bTejkbTNh4isoth3M76UQockU8Ri-UszAxqfvCxx4WmUypHqS-MAPFwSi_iK2RZhorjl5VgQMHydDiUghCb61VG4rLiNXmDb4jp14xkyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqGp8spkXFNYCjgVS-KEbWmqeRtsdrPemAH6LFqGSmODK9igV56GskkHS1lBEKRr39rab05E4KW0PTEUx_2P4Q9EyX3H4GFE78KgMPYEH324NbEBiWMQHfZs_VAIn_vl_WbsSX_dBj3qvfo3ai4OijJ7Vgio9mw-IM-Zr7N9BE5oRuwKXgjsvOmbf09cB3gBbfbHdxvY9YzZ_h6A_vpwaDBNo5AdCdEGEneOVrCEvSJzTtlmEV8rMp6L6ezhrI6sgE2ecmsx5c9rWQowNWuXKhIv2V9WqRSfsZf2yZoWlRl2n5jOpwx349sS66KGeLHRTEMwjtaGvl88Ng0Or4Q0PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bcya9sVqgYYcj51QoNYoCuB-MyYgp-oxz6bT3kqNFK1EmaihQKaiJAsx6vVdQONndYBxhrbJTMS4hQNDuPHnN1Ftuew6GdK8Epa6p0UxzY5KAqbVt_KE-Ha9j0pnCLxJJxlKHN6yhiJ7YTUtRbdA6RNDgl6b0mASzaaDb43vFtNVO1JD8Wj8Y_ie7xmAFziHnQhSvBT_OWBGQmybkcJioMnAAfoHGY04C6DJd6s8OcIao_CKUzT4giPSXV1PikNHtQw1nOxqY_Icu9XJIkRBkhqLO0AcmAglwBVXIiWvcZG1p-JK-1ysnndLDHb1G13rh5bKyrQEvDoTLonIPLFkdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgh9pfVYE5JypwLHPdYfFHS61LZDUzoscQ1nSQIkUY89OptJw26_2Vuxrm0uVcjELHPmkdwIdoMDTyKGyO4ThZIu1mMwnNB9wkCejSPDvymWhAWEvAWUBV6mMeRPUmj0IJwg64fYhuxI05khAhiZ_IGJPyP--iUKAjcRCMFew0IOxIeSulFz7vLRJNbSus9Q__FdHcBL5PCXMKxyW8H0b0WVZom-bMOkLlko1K4Gomd1UaINeLiZNclN-0PUwpGI4hwiaquQEc1fTS3-BlEYs_gC78o543KnZqwuntjEStprHPc96Ucv2JXfrt6pwfTFFgPYjxtCdbHGC6_R_O40UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YPe4J1FVB8e-KLgTruojTbR7-G11lcAiCbJsL1L6sfhRavcKhr2E8LHDH3wuYzIqgigeQbx3BkGNqWF5qpeTUcLrI_7kOgMoZasL3ATujZ009-pYEn-K7ywYKc69cc45vAxkkTJbWokSZJoTyVmIL0OBysgxgZb5kjRRCYRpYiGi4DhnbHglGtQdx1FA0sDVw3i9WCw3X_K77MUVAXinmbBR5N-BPX691_fXetXpGjnjQ0lH93UCm_blMRSczo05MqlWejYg_MhMOcC57blTPgwxvlRLGHvlhdxZrpLjnWgIuF9rKtowB4mTeKQ69_sTjp2XR1ha4ub1MV6-t6O-SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pb9OExwXwmAc4iBY0_p9aJDUD1nUR6uLyiIMolUDRKWCPZB6C9gHzvhTbyzmdLAXMDgcLcnrWVP89B_lkxg1Qzh23ZYJIQyFGB_c0q7FZmR2DNlvadzgJOGSs43C0aSey6zWI8MfgEaTToiLxPbIG7DN0D37XPZ2CqzV9iBo45q0k29u104YkF_UrYgB2qMLTVIreDJAk1MFvdVlSNP4ZXodXLV0eIMcsLxREuuA0nNoOKPoJWE-DPZy0vfzxuIZ8cJnTJhPWGtLMUqh8zzX8Qh77jyRJaVRjgK_iKBGLOAntiMt2iXRpyicN2bt9XNSrMPjFDHGQT7MgC9jFkGdXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=FQTUkHMZIb4cOZy3Ln-dY4-zlYJUF01V8MbWsSH161J5YV_yCwz0r_1ygPcC1gUaCVM9-MTHSjHuJIsCBzLHzwAAIuCbrfnwip6e0kPL3o2wrkT_8tYszB1Neazmy1hp7XI2wnPSsWCGJmn1LPejB5_bMJlWRFuqNqzH3_3h5gdwsTcFnYO6Dkxm9eeUlpW5BEZJYaC_DqsGMw7ELTyPmPlZc35nQAdL1QZLeBCg84uJtPN5hbJ41pABmYRwJ1DparyLh6zjuFNqrAZ95kWD6q14a343-PFyv7z9p61sya71_-wWdJfEGq4Y8vFQ69eo_hgGblAiBBYH4dBCP1PNCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=FQTUkHMZIb4cOZy3Ln-dY4-zlYJUF01V8MbWsSH161J5YV_yCwz0r_1ygPcC1gUaCVM9-MTHSjHuJIsCBzLHzwAAIuCbrfnwip6e0kPL3o2wrkT_8tYszB1Neazmy1hp7XI2wnPSsWCGJmn1LPejB5_bMJlWRFuqNqzH3_3h5gdwsTcFnYO6Dkxm9eeUlpW5BEZJYaC_DqsGMw7ELTyPmPlZc35nQAdL1QZLeBCg84uJtPN5hbJ41pABmYRwJ1DparyLh6zjuFNqrAZ95kWD6q14a343-PFyv7z9p61sya71_-wWdJfEGq4Y8vFQ69eo_hgGblAiBBYH4dBCP1PNCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhHBUOz1JrkcNhgB_r5S_AYdnMpg5nuDaTc4mnWQD3sn4unmn3tvb6RHZFXmhdjN8g5YCqf2OJHkoeSQTLyaGz7Nw-yWKOqVJDRi4jsQ5R4UsezXeFNzidMnxJfas7ckxVA2ykwbjnZKen0J60PZN1BAe6LCVEmz_ZUP-1bXEmB_bo8PhKmS4m2HU_MvXnCpk_-63qwSI8JsTFS_V3XGbKCx-r-U6iGwDN7m_MjD3y9x3bnU-7WDqjHoF5HkUYha0_AqfOLoJwV7V09q3L_P1nzAy-_1KmjTefmw8Zih7um13rxBLfiZW27Oi2AeKjWUxakf4ZjhrmjeMoRTe6vPag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PevYDougsnkGCe7_QiOe6JZYQ76dOHjZxgxFPuUv0WXO3EB6gBtg05VBljyttzQwCsOReLUHJX1HlP1Q2yCqx5Qhf08Xjc_MdCeOg4M47MBv8G1MlFcG_gp3omP6S7fnygnwxfRl-HJMauYAdG9vzrhJqtGUttcvY3WvkfRlZPZ2NDRM2HnVL9gTFBDpiuK1WyYWVcX_t2vLeLhDk8rxrtfJrnsnQ-dQb6kwfILMcgxt9ZIUQmAB98FxtJHprlru0VFfVhJFDIQP7J6XNeaWmkdksEPpYTQsQnQK9Z63v6G7NnQexVYFxqTwcPWTUDXzh9cOxyRV-1inz5O4s6I88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFgiAfiN-ULYJAfDMNNz8Rk7q_oioIBeqSvtdWUa4PX_Ukll4UgFH98SmmJ1L4IomLV2bHP8hr1uQ0NuRE9lDRJyjIBFb4ImNLiKRLPovj0vGGo0U6RbhFAo5iPPajvsF_JyoGr2WWx1d3zh3FtFpahCFg4SHQyk1YL0kBjF11iNUxIbjZnREhe4wCfyv4SuwuHg0JlLaACq3h-MpFJcMC5m5dmoV9a3Cq2qm0rqMeG457AxZ4WW45TtOSMTp2azyfQOVsHZnjl-Fw0rNXNIBI5I87hAtO_QsdEuS5buKu41HJUfDmuI4l-nTllpgrvnLkuU4thRzo0YWe-RvAGV-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt2qWAiyi2VZTEfq3MuhZ4Wv5DqsiaztaBpRDZ2e8sbtAXxv46M1awGEBq-ErYDuf2CqPbLslIYcfXS9IcfRGGMHPKZ1mR-rtM_5H7-cG1if1FTRFkWJoAfEWgwn8OII5LnHUhDx6Cm-0spYRVmhvCcgRWv0dkSsjaMxILJvlvTXYTiMCnQykqD06Ab0ChWuBDDp83QJB1ADF1DK9lFc5hy_TG9fDDFfgMtBH3SJ7G_FAFM6GrbcRdwzPaC_THqG48JVde302J6ArYhL7ceOCXZo8_UlI_o9BJiCBWt0lM-2JzWQ3t82KtPS9uneiXr2uAQIyXtGFlesP9pVuAPxFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN8a9SyBbnG740LqDIXqcfHQZm5aWCEwjWtgHBfVR7bd1X2SmtgN9ALii2oz3L2pGNT9PNaDpDHGUHZOLxnIN-OkauYTBf2MEOsGoJmJOdvKKdby0h_GsDggTJxTE6AGqiPiOBOVvLGSRcZzdq7v0ZXcUaTF3kZV1D-t7qpvEcRrZpLJkE1_gO7XIj06cPVGS1q-3z2748SoLQr141GlbsyWYlhSs9cjYgljDdVKDUfl5WhE7tGvIj3hnCwlRLNokDMxbyl8_sWIBMaGcaolXlrbxh3SNP-zyTX35I_52IbVF9jGozE5Qu9QkOk92HxTaxuTJ60cumYk-7mMCP6iLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPNC2SbUUyXpZDTnuvcKrnfjyb22hg1ALV17y-ksgwdSxSYrzbCnmGYBPuLVe6S9ghH9D664mCVNc8vfTCnr_RX6c_7v60CAL-O-3-AZgsMyD37nUJaYO7yFiV9ulaE_IfRX3RjltvyCwgrT995IlBmzaE4rDxJc8TGM5-Fvu-yNIoPOEvUEPtMnM7BgAb4YDo_n71Hy6vgJN1D1xKNqN4mcI7D6UQ4E1K8FxehwibY8-7zznyZscTBj9aOVp7HKn-kA7EN36wt-DMzpzCOPvDpIpWZ5Lo4x_blH2Ftfcgon4oxhqy4e8-F0mJ1-aOwajXIRkal_C1Du9D3acGLL_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8bBh0gbbItNdy_ydJI4_8-jtBH4Rl7PLz4-SBYWs_WxTtudpH7Q0YnNYRbTLhSnpwAfshzc3Ym7oCiKS_phj96hZztrnKE97-yeEF_Hs_G3goYDSxkn8qfXYskU8If0aiweEx3_mvApa6o1lT-1C1bc1c7lDoKi4oSFulA1jLylwebgw7BK-JrCuUTGoxRORUxmuiKaTHKRHwl1MpyUGHRSwYKEpqB0kV0sda6lPwBkW9mC4ygdEe2yGVIK9mfPqFFPNETeZCshjipBVyrSCpkQqmVE2Tqq69Ymj2seZX8mIHcYBQf5EfoThqUonRtAJs2u_pEE4Gx4VCJY1Ghkmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=CQu1rzA3o8MbvgJdzoL6Eefverxf55bnWoDj6xcUxbjxKQyoYqT474aL5xnG1CQHNkit911oFaHxue0CzeexO38X7XetBQAoEqOokx24vPe2zdGCA_qg42PHc2PyQ90XY2Th5ljy3oWjh2Q1zZNW5FGZPO6-mBPoZ7zMYysaBLqQKhowaFUp5kfgkrvH8ODlrLUR80oqeKSSFO7bkf3WJGT2hKcEYj4AGpBiKqus3NfkabXRXUe4DDNQ8Yf0lNcirZhQtjaZduCOYI-d2XUxcSc9kMlPKIqTbjfs6dSzVGWNbif4KL-rEMhwFIGpHEdZbNLOdUa2giX16G79e3aiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=CQu1rzA3o8MbvgJdzoL6Eefverxf55bnWoDj6xcUxbjxKQyoYqT474aL5xnG1CQHNkit911oFaHxue0CzeexO38X7XetBQAoEqOokx24vPe2zdGCA_qg42PHc2PyQ90XY2Th5ljy3oWjh2Q1zZNW5FGZPO6-mBPoZ7zMYysaBLqQKhowaFUp5kfgkrvH8ODlrLUR80oqeKSSFO7bkf3WJGT2hKcEYj4AGpBiKqus3NfkabXRXUe4DDNQ8Yf0lNcirZhQtjaZduCOYI-d2XUxcSc9kMlPKIqTbjfs6dSzVGWNbif4KL-rEMhwFIGpHEdZbNLOdUa2giX16G79e3aiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6jGLiEPp4vMlLGnigTGljAy7H9rH5CgLvoEphMjPjjFiPSwH0jWUk7FaPdCyt9yotvggklr7e8G5X7eMSmZm3ZIjcCvWRWZ_QO6IvtNLc0LZPr_559jYM4rRhQZ5kgfDW2B0E0LQo2pG-bpETskf81SdQKNSsSXjDIfy_ygY53SVeFRT0UGF5WXFzlo8YiTiWOwlRxbc49w9rW-QbSeXISOKW1oj4krVrE50RGUrNSw5zkcFv1m1LBAf1f6hsEuHADLfm4zKBUgDHzVkqGysf5fV-5rg4EjhDSo0LC2xnfq0OEYsOdADLHJpxikfe6U4X0CNkYWM1OYuHT5uN_vqldc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6jGLiEPp4vMlLGnigTGljAy7H9rH5CgLvoEphMjPjjFiPSwH0jWUk7FaPdCyt9yotvggklr7e8G5X7eMSmZm3ZIjcCvWRWZ_QO6IvtNLc0LZPr_559jYM4rRhQZ5kgfDW2B0E0LQo2pG-bpETskf81SdQKNSsSXjDIfy_ygY53SVeFRT0UGF5WXFzlo8YiTiWOwlRxbc49w9rW-QbSeXISOKW1oj4krVrE50RGUrNSw5zkcFv1m1LBAf1f6hsEuHADLfm4zKBUgDHzVkqGysf5fV-5rg4EjhDSo0LC2xnfq0OEYsOdADLHJpxikfe6U4X0CNkYWM1OYuHT5uN_vqldc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9Ufm7Wi2k_WgemFjE2kORBuMQcYDqX4rqUYAyUVX7OTqUB6wCeUvVvLR32fryCM6s0wOCo86AB4bcxBxD8LRheI0avq-KOJDIuQ_E8D-UJVtGvbv9J2RNyH4Vn6ryhoV8ymwh6M8v_EmkXV335U6hVHDT8K35El_bQo6oWgft-H9I8IffzXNtmODlRWT4UQi12bSnIwEUqwRwU5uyM77z3GXESk6PVXcth0IB7sPDvF82Or3bU1JUIkVG-7mxpGnI6MCCvwrwFMed1oYCFwFa3FsiSlsqN3Yy_wkkg0jilpeBwTF-FzyzZjG1nmnWbhrJyJHUq0VugdAL7iaC1Dcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckxgV7OBIzqQhM7l9DD5BIOj6FnPrSPT0A6_6L0m1q4Wlk3wrz7UBxmVapTE47QUAT3oxoaaw4poy-iZztsWnZDdNMvEYIhN4htMM9JzKHw3sXcNs0qwYoDR53nLyezbVwSyOpjqmQm1q6vUSLdUnDtJQqPt9e0GmkDxemefgs9y7dOIoOx-fiN6ord0hqVr-vnXngt4T1gfkiFAbCbKYCZn0FzcSCWWg0apW3VkWuXFP4sAysTkr3A1yWI8yN8X5NfemBjkCEzGOugJjkSOUJbrekaahW4X01lTTZzT9yVWTqlhOypdPMkZVkOWSal4StKf8ScOXuap2XsUkRj3Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=kN62udt96fU2uPrkbtytib5qD7HbsHBHSSdaSNsKxTKMghxQ6k6_a3IP7ENw5_Esh2FpGPNGJZhON6AmRMuT1sT3pRT9TrkOO-_g7eLMM40QPd50Hy-hF5rxGyaQeXr-kbTVJT51vI1TFtcS0S6xh7R8y1QcPMRMtnLjCWEmvS0vmVn2-b1A9CSWFXVC_C9-vn3t78fhyRHoDa15ACLELNG9OC9zAbrYtj2QJaD_1x34rhtNohnHq09UkTIE6bYKyAdAZC3-R3N2uHxFBixLhNakW0dgEAQSP-JLCusAT-7W_ao6Us44JBeWHiL-mu-DmT7b4oYbx98vPglIldOu7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=kN62udt96fU2uPrkbtytib5qD7HbsHBHSSdaSNsKxTKMghxQ6k6_a3IP7ENw5_Esh2FpGPNGJZhON6AmRMuT1sT3pRT9TrkOO-_g7eLMM40QPd50Hy-hF5rxGyaQeXr-kbTVJT51vI1TFtcS0S6xh7R8y1QcPMRMtnLjCWEmvS0vmVn2-b1A9CSWFXVC_C9-vn3t78fhyRHoDa15ACLELNG9OC9zAbrYtj2QJaD_1x34rhtNohnHq09UkTIE6bYKyAdAZC3-R3N2uHxFBixLhNakW0dgEAQSP-JLCusAT-7W_ao6Us44JBeWHiL-mu-DmT7b4oYbx98vPglIldOu7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4j8eMZ6medhbOF5o3VqQuu8jG_UBHX9pfvvssa6DiexgGvtNdg8J-MxvdWgF8zKaekyNI910XNI6uoQreFOO6iI77RIndXVvc3afdTVyWxkjlf6Jtzr_0Zp3AMqMvpUhXSctvum_w3KRNtNyOHxXCmJokrKcLOQ3VJLUfsyxBjcivpF7lsGuQyxuzo5AE8GAWpMOg8XOgcmL7-iXO06Q5ztmchqEjB8RyZr_qBiKIVGClslmQMcm0NCMGWmxxKLe4M4ywqR_K5g8MfilqKvIY57V4rq4s0pNKnyAqyyUxaQUQZVwjSHF1j8oE_u5ofxq9Hnp0u1sxKvcgV-9-6aLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlKwqN8Y6owNHBls_EX3EPDtOfKbq1dXl-k-Cbnt3X6CK-Qb5pxiRqDmpmKVAu7jsRtQiUWbViSlps9VYwiGX2h96V-Z0Ldau3zsZl9-jn3F5ClumBo5ezdm1rP9k-2Dt84d_wTywi8zzM6JlCr-V9X5x9xZwaN8GmmEJOrQNn036-0ETmlLC0XGC9tGqosJV5Cg0dETjwt6PmP8alaM3J7xZenQz94z2KeigSTViKyzKQmfs1Q8_Nj0x5b3CiCyASYUoAsuC8Xro-74I4vYkpwrVl42vaZo7zHc4sRX1a6GfmSSprDEm86UCm96p01XTJqyqBVGC0RfSOCMNK9Dug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avzl27soLvq82F9fZCuyg52R4XGAXiw6Hh3ZSr_vlBsKKUSEEUDHAv3Yey-BJIqxlvOqioWLdvmte6lrLh47g3JpkCT37Ve3b8i9vH9W0huCceaswdJklgH-kfLByTd8IzFR-6usLbk6UjaxvFDRt52tWzW7TmVEL3gMjj9KsObnds1sQdXEfCbgEAc0fDgjdnTMaKQ26567GhDcJmRAOopOylAC1fhtEQX8DN9EirGEupuf0TUigD1VBffdEPghIzTbpcHiZTjdiMTp6MS4eHOFJGt85-3JLT9fmtBrtBY5mcKH8nQz-zxS4b2YW3vAh56k5iecGKtIk2Q7Ev-wbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGJhMHXcaK87wJ_HYAt5ODonKF64yYUfFXVUcNzbW-yA4d_dZJujh-O50jLwHdv3Q5zMzLWulSgZcMbe872UZW6gU-KiZQKvj3nuCAtFMbHYEmbuLD7kSp6z1cwzj-neKkSiCaE18ZFp61dREHLBK9HkPn6K9n89MiOlsVUvD4WGe81Fr5kMHHKOjVNi8lZwpKfJyiZboEwcLgCMWaUPf2nq48jkqDmneMx_25uSTtrlh8yUBt3Ak6UQ1SZksJU6gvjBnUp-8HSmT2m1dUrjS72eDFQols7YK0nPXTK5r_YiKyU0OjNePHl485cC8PqI4qv4tOb0WdbSsbXsfDiXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyVg6z_kFXUxPfhrTN4C37R3k4ljABilJhRYpXi4DIG4qW_xUUQoKGJH4Xjx697vnQ7-GDVzVCMmvGj7QNsBguWv3ivqKCBLbDJh4cwnb9-VVYjJGU_KXux8Cb4seH3FNl-Mv2m-L3EJkHy0YwEc4w_HFEKSkE-S-t7K3jqU0RwSKEzORQSEWUYJUxhfoy7rWQCmiwflK67w-pUaTmlxwPK4hHtZsJe4j7XMuWmvoDgCig876xMn5AVdD5ldBeZpl0GM0TnAqW-T2REruBJduri-dWv0jOQMxYJTvAzEnpFnol_oYtawcc6muv1rEiYXG69MxhEqfkTnskLSwa1SIQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUwJ4_HWt3bY41tisLZ6neraUhfkqydJgUgSS23m6oZdsM8WdF1N6q74JKYyDWd42j_OXkEx4FeE77LK9NRV0a2Y9NtOJFwQ6bRbIXRD0AshZqQYofAJF1-tlFKiuRj0pu36dKswHLU-zqpN2A0V6DQde8l56SPoTSKQl8oqc8VgS60ii1bnYCBTKybs6Ryu4nOcubnXzzkL_R5wMT9QF-bPFg6ctTQwazXuvJCsXh-Ze2Kh5iCXhgo8qS02YpB3j6vzKN4ZC0i5eUsJ1ukMbhhSxGO6r7upJJ2E_QGj4xNXLyjMu-OVofLLFv8kaYw-dUUiXibqBLvrRFgkyvA8ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=bngtqiVI9VjxjVeVz_iBO25EEwhpWkMAXEgaBbYb_7r9-ssvOGlhyQErRhUjDS1XtGcmu5nDCReiZ3JH1gcwBUzqC3DQeA1YcmdX_5-PgIaLLtixZH-bllqq48aClQvCcoYi97m3-5q2vbmVd3eSAOgu9YK8f5rp5NjfB5Z_42BlPaxunk6vaAxmXWaKr2e2eJi7fX_onCzq8YX04n47VsSSPXbOCp7ACNttma2lTF2qg4bJIoSRAIO7-r9qU-Bh_8Zygxd_sKKZKEbDoPW0Gr47vSQyAz9XE5YjYp4Bn0pI4gfd-V719VO9s00pdVLhpivUtuEg7SwHJ5we_uMtiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=bngtqiVI9VjxjVeVz_iBO25EEwhpWkMAXEgaBbYb_7r9-ssvOGlhyQErRhUjDS1XtGcmu5nDCReiZ3JH1gcwBUzqC3DQeA1YcmdX_5-PgIaLLtixZH-bllqq48aClQvCcoYi97m3-5q2vbmVd3eSAOgu9YK8f5rp5NjfB5Z_42BlPaxunk6vaAxmXWaKr2e2eJi7fX_onCzq8YX04n47VsSSPXbOCp7ACNttma2lTF2qg4bJIoSRAIO7-r9qU-Bh_8Zygxd_sKKZKEbDoPW0Gr47vSQyAz9XE5YjYp4Bn0pI4gfd-V719VO9s00pdVLhpivUtuEg7SwHJ5we_uMtiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=Py_kDZFcxnJWzvV1pK5OVCfdxmGI1VU8x8dN14HYAM3xoiRVPw2Bf5EoY3XxNaJMn_IJEGZH9zkfynKbduSSjeBr-Uz76_UMJhKBu6X8qGvwAK4HhhBOi_nMciUB-5_P4J5KlHbrk8Sr6cFHkPsvAgooPwV_MS6rtId-EV2-VekZeCuUpARDLNQjYYj5IK_QHa-pxh4wy1bphACiXWB3f0cSiNMsBfhPC7C0ejIpAsj0AN-F5RvmjdgYvr4JEL7yk-ASnQu3wBiVeuVZfNka5lXIpJJdtxAjhgMXD7kJqrsdLGi9Ec3ZcZXhPxttT2fL7VZdC4ymnjBH-t2RyHGG3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=Py_kDZFcxnJWzvV1pK5OVCfdxmGI1VU8x8dN14HYAM3xoiRVPw2Bf5EoY3XxNaJMn_IJEGZH9zkfynKbduSSjeBr-Uz76_UMJhKBu6X8qGvwAK4HhhBOi_nMciUB-5_P4J5KlHbrk8Sr6cFHkPsvAgooPwV_MS6rtId-EV2-VekZeCuUpARDLNQjYYj5IK_QHa-pxh4wy1bphACiXWB3f0cSiNMsBfhPC7C0ejIpAsj0AN-F5RvmjdgYvr4JEL7yk-ASnQu3wBiVeuVZfNka5lXIpJJdtxAjhgMXD7kJqrsdLGi9Ec3ZcZXhPxttT2fL7VZdC4ymnjBH-t2RyHGG3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvrzB2y271Bl6zW1FidMVDvrfrmV9cQaXKzvcB8ixuhaV7-jq1qIigD8caoIvrhNgNEdafVHdxPQXYvZuuoBATZ8Lg1FjOpIDBpBMrJ6aq1fuzfWfVy3ykJTfH8CY2_dN8R5OQWXZdS4clGBSyMgcsUas7AVCDyeRaK25BIUSL8BTXl6m5Gox9FixUo6TmLlyll8IFh4deAJ7GjB-cY4bfB7nzInP1qpm2lMztgxjZ_9xRG0B0bS3_lV7Kv-oc-uFfbzhl8eHJm5ILq3rCluy4BdVppRO7__I_qczVFynhqoaEjISrMJ44PgCc2M9HPveUeS9w0i-TLjAp9-28tC2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABrU3koKGFW0TE5jifhmtjP07QTcGeMOGomamu3AL13cAXnE8gndgeRXAijxZCv3Hk-y7OmYuSNQ_UtUhd9O1pbbtoPMye8aJBg_nRihhdAnTJrRAF_GkAso-WqFkvHUF9adAreXKtmr8HB8h9rlFfD40uIR9_NOvpWfrNFFEekGJlOImIUwAzOA_9GTf-2WDU2dVAsBGmg_gg_Jy8p-G1BParffASxb2WIS6bhXEFtdwuj-vAyAuaW1X_qGCctdJ6_hBOTEIwZAkZxVbpW16GAOYEwtceAWxfVPjRAsF2nB1_YHT1PpVMQQohoyPYWPHYPS0OgjKzSEMDYgZO2I8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=TTuYp6-YaSWJHByMX35prAYRgDKcKoduYJ-hjMMkgu5Se2DwjYFdq2aWCpBvdyWH0TkAFiblVGZtsPYbTR7ZugThqzDx_TRVkZ0l5Kj6RMMmVTTBoXeNHosg7wSouRZ_YoirxBD2bFBOJbiWFdoXlj0gcQ--S03tDrI2crtvgUqmwSO-EYtezertkFVV-vvJRg_RnuhRXrM1VSjdUEePa-TL-pHi1le7817pwv7ty1__veK_Cgr9iTDQFjKLCPdpAeEk8-mYPx2SlSs1SF54fVXvFXdnmR31XEYCjiqn-F1n4MaPXnFbS7FqWL16kD97rEbD9N1JXXC8irLDJKm-Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=TTuYp6-YaSWJHByMX35prAYRgDKcKoduYJ-hjMMkgu5Se2DwjYFdq2aWCpBvdyWH0TkAFiblVGZtsPYbTR7ZugThqzDx_TRVkZ0l5Kj6RMMmVTTBoXeNHosg7wSouRZ_YoirxBD2bFBOJbiWFdoXlj0gcQ--S03tDrI2crtvgUqmwSO-EYtezertkFVV-vvJRg_RnuhRXrM1VSjdUEePa-TL-pHi1le7817pwv7ty1__veK_Cgr9iTDQFjKLCPdpAeEk8-mYPx2SlSs1SF54fVXvFXdnmR31XEYCjiqn-F1n4MaPXnFbS7FqWL16kD97rEbD9N1JXXC8irLDJKm-Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyNwHpnTzz3UrFmA0C1ri3Bvnzmsoe8FvKD--kJMYKcarZLi4cMhK87Z1ozDVzQIMzSkDgfAiVWm1upPMIRTlHQnPCHttR4kYFwqYj5m1QnjAdPPRes4Zn1AnBCScm0v4hxiN9z6erWkYgLV2uPmyUpu9-1zLGZFFSArRwxAg1aAR9XJ5prSLx83snTDTf9R32daeT5nYQnEltp1-PgE77ZL4n_3Ek1yRGarxPzRtNkBWQBLqMBNN9CrvFlP1WujjsOjA85DtXnD7-OdlYsdvScUm4AkSwuLSH6T7yu7_n0hYSXW4t9Zjl3NnVYvswyPYrQjy-ziRg3FpQjUqrnMeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJX-x3T49ZOKrQmAzNCGrOPM7Fij_6Q8iHlWWbISvfLpKP_8REAULGgJpBgRJn99zGHPRvUPkdBtT5ruUXa--E44lb_PJD_RL1Lblw9N7-0CDRILp680Y5V-geUGcSbi72aR8FlxLtCmc3YUgkDVO0bVD4jfCAmmno8Mx1gvwqBcHE1K7ZhKdx_r4ovzG_M4KzfK0d0o0nxOXL1_Azazxp284qSPxCtq3wIerK7TwAjjcQOavv7nCi3KYmB26yu42O6nbuSJ4I0mCEKFtPCf9-KePEjBqPqXlDMMpYHo83Z5R5djhOCwAUrpDZ5oC9EaKO9TD6MTWdbDiBrOtraUDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzYbfmBc4uM2jXEdLEcHJNTN_ne2bWO-5HuJeY3bOxeNqFXlG5pJCbqHcUtZYfPcWPUOzP94Cfd-UpWQDwVjkXCANPlJPrSgHVUYkM1z_19FeII8JJc1hzJ1dnA4Q7U8jPNQPsoQQEm-DvvIkSEplrivrStA34eknEHkOnCH8xPtL7ZwCgkCIBi1bvQpynXDJ4GJhgBebUx6ARgeEbqmcnduD9hpm27aZnXh8dCaILhc6TWCMFu805-nRSDa1ZatwEVud3rPW1qMr_iSQlSLg151-OqBjEb7W_LbNAk6g33dUb2iZWJiBPpnMOoP5lizG5k5Ii7Ny1J_9_1kDbw7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bk8pMPKMeuxb6Dc5G5aotn0xkGGIHRX1pb9CoXz1uWrrZusZ2xQO2AwZ0yMfWNr66Jbt1WnNoXKevGzWB8fXhGXwkcj9-vFmCodtLEr1ehNuxUBQ8FhpNqFquTiY95rDW644Gfd0ZWt2xWYGDbfwF0DVRjMxqwZgMw8VhMV2O5zxE1L1xMHbxFWHpX_nXxObE1dg6iRPoZklMDKVy2zdfcX9mtmRO-QAUl0ISGJTCE3RNubblmADJdwQRn7PVmXu2GEzSzuTFZpct20BYmSOT13cWBQ2_lrLEhjmu8bAiIS8I-lGD_uZ8xjhP48LxwwjSJAnMBwZRRZ3B3yCht4l9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlSuvZSzaVCdZaLgr6nqDeJHi5PisGV5DeGSYvuT6rm_ibrgLQd5fkIpXUT8DP_NIeVL2Q-4HWVXIOKwMh3Fls6o5botAnHFkXpV7_GJshsrig7sNlvG1MdRoMZP6mv2aj6sOsJT853mKjh0FZD1l0dFXOZux-k2D7yh_6G3ADJ5DwrLLeeo3s3_moU_lPjXEeO08Vak2YbiTthRaaOy5SYy8U3nhgzKBN3JU2zelJZpb5muZdRg7ME1Kmk0BzhoHJyziYngd6jDz9n8HLziPKu_hJblw0X1Lt7Q_5GkdKQKAbm41Hfc7I8QMhkRUXXlBKdxq-vmjzMnVjzU0Cy2Rg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaezJiT8PnSXKBan5tEzboe8-WiT4dyW78wOAHYrFyHvUOzVJSxhPJJv3x5qN08EPNig5HkzymFswcbhBIPAUKjXMpfIsUJWAkMxEcG1gDIIYLAt5fdomWTbARGqocvXfgOfdjYkvZs80UJ95DX2Si3rrT4le20V7TspeR4E1NOP76TshytXYEbXBA5f3gtaNcUEWvp1D3UglhDuwmULBiKTFc8t2_F2upxUHTWL-RSXgcRcTB9nK9hfYUrbUqZ8oFqUWohllM_lexQ_REPGSP7Yaq1zUL7T669XlLDcEpmcq6lYsL_O7KBZV_omdDZHyOISUDFQk7VtLbXScZ_XkQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_UI00AeoSWIWiIYmIR6ZuzNorkRQ9SoSq4a8Fjy3LkT7U5in2Mog4vmk7HNyr8i3Q4PgpZuOVjMXsAasLY0rRulbH7VkiUjubzF-sIwFzLuTyyuB9gWLLGTcmofHGSnR0iCxtoqOe6fSnADFjaxd1hTQfEht5L0YHN1RignRDcYqUjkxAkR2Ax7eWCZfTK1wt-ak5Q1s6NdqJ-bunGWhbMyyGfIiI3w1EcLgRnkGvfZ1Meamnly5PYVrhK0SvWlDP_yjx9oYMxjOCWtu8ZksP3GitFlEGNQ_xeTgyxloti5AsQVBDE3VSJADFLbmsT9qoATJmzOegzwYgBOsmZ1JQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3ERksa4PL60Kyk-rIaDJQn9lAXr4Q8hFs5TUQolsQfVPzKOopJtvRAicYzpPeL99gY4sLaac7QshrQGfHwZPsv3bk1aQDazY_12JSg7gy39U3UeVrE7rVshwrrLe_bCilI8q2DRBBTrD1SZ4jwJNS7kq6LdEYh3x7rR63EeQbdCme7eMR-Ko-f7YH-4LlkiHCiGp4Emha_u3PSuq4K_FwzLav-CsFNUVRaeigiqnGZhOZXaG4Uz00L1z5atvOP_Bdp7nuHbF23iNyVXamaYPhF1LcmfSVZGqk_w3AmZ3YZrjehO0igxCpk1R00uNBF7SNIob0UKFzbt57vP0l7ZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmk1Co-16RvXdVmx0FwWm6cMqXCAeQ0yJbcuufuMQBvOcumyCzfbjbjRPQJq690jx0axlXr82UVOrnik33ID00_qhZtMnmIesytyYcDqkjSAZQaqSuI3Lsu_SubJmY930AhtOo9uLAt0MpinsTO1TWisUwU_8RJe6d46A-hT586n_fWIYg7ySTdgCdzBjKwgrh_QuQonkNZHES7ktiDXGvf2BLpIkhlcQp95KKATJtIvuexEegr6zRZjHLkphNXl0t6WWMbYLxuMIUYrH5qWzHysFHrFncGn5balqqlxs6jr_WwEwcF7u7nDcn3He0VpsDBIbwQLaF3r9eYZtwcnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W2-Z91B-fXzJPzeYIqjU83511OK135gCt0KnbbCM7M8Q6R-RMT0GpLWodc5O26yQTivVXFr47ANy5L6_Mg5y9n8Yb-sIklPt_MrGqnXeHaE4vNhHAFJU5awty0MCM_JqqYdukcK-aQuze0BFt1Yk2t7MvE_qfIXmr7eET5-RknbEIdNQ-PUhcLft3SXP1r24-diVNp4N1Q5i8qc97jlf_EvfdnZdHJ2bKtZ2Q1dMVS4LnpDm0JcOH1ozDmV_o853qgTc1AvBcWSJusvLdMNO-VMfcw9I1tRxjHvCBGeb97OMmVS5abqZ2-OZLDwl_SgfNalRa5l6O4ih8q0wve5lBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5FB6nILx6GBpe7w11RL0EZ09-XpNRiOIizxDDeI9Pt4dOzjkZQTJk6FJUiwzHLGiTX0uBjsxs6n3671K-dKhXOWVEYk_UP7e23-gYkpMuQlzLsTBv8Gs-sOcH9foKrApnkcAAWTxNzX6g1HziPE_tp2LAqwmcFRP9zAdSRQdyAcy_exs4JX2xLbjdyOccPooB5SMKRgy959VZhx75QK9Ji6TU8f_JdkSb7Y5c-_oxUA9FSPlT77XgrCR99_LMI3g_HIFMbR7i6FdltTJ2PcWaslYNGfksGlkA8960pWV_81iFa6omVfFycJarUJvCi2nfXJg939DUuohkr6GLcuLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkUUwE3U2vfOFYE8_jHCEc9fVw5DG_PO6uxYTAjm9DKp1rHB6IrmcJIWbFmEQVXxcmgF7V2XEOmJQQLXzIOzPUqi2Oy6m1lE2w2jxYpSshMLWU0uK8yxXrB07V7yKEx8U-qVLpP967UheeOKUhn2dHu3c7Fr6D7KDSMW3N_0GldKeLJpTud0L3pWT_uvCrOD6cPYYB_yW3tIX4PLeJmkvRRpGA0o9YvUuw0dNdjctGa55Syw3IsCfEjlPogqHG0aQYg_uGaigEWPHGDSHHEjx3O36TebLeZkV98hDHirdHjvUeHgjQ6E6ZFaq1_JEq74Pv-STrVwgO4VHFVVRoJiSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7fMGd92y-1VmF3lwEpBRuNmhN3zQMWLU5oRtGuhnlrBsI8kgRlFDun8PlFeLchRe82eJROjhY-3JrsKV4AFbfm7Ykx2DLpYwSCqDAMb73b36AWsu7rWvaqzl7Pyiwd-2nui-s7-2OAWKsfSuwJNf9kdTOCvibTus7xY1oU6XjWCPvgcjiLcpzHDv5KzIHX5nkreHNB08DwzEe2v7_ERdMvcoKYXxse__1A5P3Fp76qiqn4yGPu3ItG_D0NJQ60iKOODS67UemN989WoVIgqskCiQ-AMns5Ga_lXOdFKfDKMoEZB-zDPgBFx_HkEDj7nMBlQPl6Ws-4ULdqy4VmcoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbTufKkiAsxnnRXim7GVgzuTOrOs-yhCue6QMAqr_HgAQlYFhlaKGt8i9JijsW29G79yRVhOyLtyFlTsWdw_Jzl3ltT_nL_KUs5T6O69l_5MBOy_uW3k_1HQinvF2Pc4Mla8EInZbjhLlIa1f7-C1Vc5HaG13wuvrFTERFyuuAthUWzizFT8vxxZLsg4Z5QxdN6qHjw0E4IgTIwD0nY2_U22v09OSGdCFGYgGt9eEeHqn1KNp5y6MPxRrJKA1guBKP7hkn66gniuLbABBmBb2-P5IjgZTNCtmr9vSW_xBj7mlcatDfnNzdyDWiumUOFyfD5-6W8XdKyq1Ge1SxieiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hyLVkIjLIfE8uDSQUIGjgN2O4PvivhGzcbkEQaLRFOk4Zmw7WNP8VPslLdtoWXaMQ3CGm_PufO0VzkAkUjFxJrfzxPPJEpqbMMm4dqYhfi6oww_oyNB6nZtB_Ir_O9VICXXC_iuyPnPpKCFGshs6HIIGt3gTARo_m6xaz-VKTghguWsJ9eG_yVymt-oDGsq9quzlhTLhXSH_B2r9aVkUqXmwOfD0EbONUCPi8-gLhpWbe95TYCWadRpKYIkjqXR5pA_VZiEmr-yCMDxJ_gI5QQOXkcrGKpv4gY1hx1i4umeZeFwPC3pu5YN0dYll3uhFt-EStuXCX8eHaqw2Zsf74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGS_bRFjVJow4Lttf1KURhIWplAsxu1uIeX54WLW60VYlNpwA6pqF3eYqEYZnHzQG6l7AyIK77czYAHTzXTDtHR5bIhGO0o3DhIpD_4hVRC1GRngiATsVEPk6Dqwp4XT3n8_88QCl63CxQFZWJbJP205oRH6Z3WhvfBtv5OLnKhEKXcEJ7vMb6pljPHUBFQPQuAzxl58cx1gZkkD9cn4J_6iqkvOq9U6q1YV9Z1M3O0jq9Vu0JlmKhCIZebcg6yIYkKeUpTTYl7cUw-0_TbaNByGeRPvZVLxx134Wyu1ikF43ozFPZ-FXKM7T5Dswb4YdicVKmbkFa9_hX4n33EGnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpVXJvCuH2te95qcELMAqGQg3jcvoTmfpLfgnLhSguJKgOkINqaX7slnUu2wPwWrrkpqgLwoZm64nZyY2XO_vx7azCGuRngmlEBUhWTn_T842Ld9S8fPN3yqnxI-E7QzS6tpvass8dom3V1KciwpPaTcc3pFkXwyZIVJnsvnNy6PpAO7Wam4ht1jOCV2j4lQ1cPOHqLa_z_RIH8hrZNCZCckhHD1wsfJL5QagzNdXkWpODXmGDfHsBwvCVn3rsUt4tXsTzWnfZc6JJ3P8phhwBubQTQowgUxtFsAgOY7xH7cxdmUsVT4rcptWanrhnTgUa3WgH96iqC92Ft4d-Cg0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MX1xIusRD57y57iSNJiqZItaAiSb48bK7GFFYLvZUCqT6SGlTUEAnJ2SNJx0p2CPzHh636YUtraPl1ItPJSRI62VyJWgqli24TcwzYnkUMnSn8e81Ve2m9lL5ZhwZr5DDzH0XrEeIp2zD3Ls0QR7wT9mH0j92B9spr4Kvq70u8dt1mW-pUUfuW5zvU7gI0Yfei5nEti7pYXFfThSSaEffPeYvu1nMVpdwg3w0ikYY50bKxWaeBj7Al0sK07syEnAHTacvcW1N5LpJH26MAjVlJSWYGK8Hbd4p0RyKwlFUaCmR89wh5CfstH883iLcBCZUdXl9dDIHOQ8jDx9YsABNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eW737c59F0cBvPshbP8T0GYjU87c824YCf-XGJu-JMxknBSYi_QWkBtX-gca-Y-wn9nTJMy235CHj_ol6vWzL1svZXvtgIPKSD7H3KITJ81O-u4fve_dtWdd8MEFEy9d-M3KJ2nyJymETQvbUqGwTuw8KRKpp-9ry06JIVmdgzK25YrHpmDdP-i4QXvExeyKTXpEXGt7li8ZIN7xrNbISp0WXdJSCMJzvSe4snmeJb_PEDKlCzQj1OyTLfPhy_dV8ly8JYSJgq67V1DM9XSExUY_3mwCHRqje5Onhrv_q59JaUKkwd0Afr9c19UmuQvBNrjmghdYgJDVBb8MGhEzSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_iX34uK10IJkoVUBYmLumpqxFwO4o6IimOyU5QERTv5WX63eZSNxjK4UBNKYeNQtY0RbHpwU9ZQvkMAnIsev0j43NFoFI-I9gwKYQRNoFdkvQulfPDs7EhK9hEty9m6lwTJUUx2ix-gNhN0gHKCYVumxbgsEyDVypYUkbvop2-tkT0BiDzOT3qJdIAhF4Ine53uFTK6RPEetwtgZ6EEUAs8b7CZrddnfvtzeoz3xuSVVXHkdSGR81gqGwGSt8ij2lZtwbXjaJ6NLJEYIicusktHI-TS7PhB1NKpFSH4a1QKBt9ZVypDCsDxGP2zPi_9Gt__wsZqeHLOrJcM0FSmYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoJ2XyhpRJcch0RHYyOcoUKu5QGOY29jucysBW2DvQD5TSjA0jNC39QLbQvE9mVSWfV2POE8cCRBRVCdsV4JsoSlpAVGrSy0FQW6KFo7Xg39eqMM6C-homLss1JdiGm6wyXKCUOeGZCSZECYtzO3Q9oVJtKkk55BGmpR47A1pMDImloShshsM82NsOFV5NTGVpnn8cwrFbW1B3hBw8e2mfpVYVjJ15qR9t3W6lossCTqUam3sHOZo3joT5yVxYTFFkXZcrJdlV2GnncPU5yLaVHn58jwzmasilLIRoJmo1DANiBOPiHxLhDrDt9Tgao-imD_DMljJu6XT7K8p6OdTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_l9pF4zDx4ifyjNf1LImlwYhXah2uTe7tVsGviANj3rByBrvmqVBr92nqdEHnvyR1VTeBCJFWBEdNYO0z1BYug-QWuejnORlt2CAsasXePCWRPmYeJ4yWWXDAaPR3TPzPqKqGruUSr7CyaA6UDyc24FKWk7jMNWUZgciJKybmuXzPiKcV_8hx7Skiz3uVWF-i8EaSp-q7xDCRQpugvP4lBxTYHH0EgprH-AQwDLfkx14SrLbB23RhJ7BzUsW4vVEhxYnaYYSbyHadX5NnTLfLooRDg4RtQ2_c9qctfCdVCOBgTXe9jk4w8pH2TTeWUsFVh244sBt4MhlxZf85AZIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlD_uzxS7KTaoCU-Ov2y_k5LLateFt_OMSLsqzxCCzpRRGnbyK8yFxfp6fhQWugx4OvsVUe-8wdpIASWWl2vJYNWfG6HIWeoazzf8kRyJkRDdIZQRll6w0q1tjEvSSwL6T3e1C-Tu1MmQ7kw1HjBQg_rkz06lkH-wTOGiFiI1L1hC7otq2mE8DSVfb-NDj9N3dgzBdXyHpGpnQek9kA-GdPo25V57dH7An3c3bDrJkG6weULdJGwgprIvNan3e5SSu5w8DGSMA_YX0IZxXUM_ksH8IwvPBXlsaGb4L6lP3_K5rkI-4rHcICCrJpbo2rMa2TftigisobQQQxazyjlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9RhX4BVdnOns8066VUfQP0taOw-FIuzAZoI-yNZf7TyJOiKGa5KInOJe6s8hpHsT3RX5r_3in0X5G6ImIbYKX27iboTJsrGcT7kT4zixbzprDPUC99TqA4KTZKg72I7Vrf5rEhMqmWa0gI1dKgKmwem1jibkuX4opFXtviqLLtUuJQm7U1FEfCSApn75rtHJB14gQZO6awxiL_OxwaQWXYlJ_Wu2HphOgXAqh9o3oG01boG98MK3WjM_GKMTC_N5EDxnuqByL_pugPvnUADcsUtiksQOqULHDNpyM4J8FljZkD_WdvLdrRoYSWc42LOisiffARJFkjkE9l4zM7nEg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL7u9ih9pylxhz0AnOb10ZE6okWrqX8Vf6nokQQmm3KS3SslcCwxZOz9lqS03j2IOLBC7KmTmIVyNDKaTWCVINxO6bWCo37pOCIi4BslBSVbmYY8oztN6vt2iBjfrtlzu4mKhW2XDFHpZKb72P7wb_3qR1E4xp7QP6bEi-1hxPKpZVkoa61ebjvuTfIrc4ib89Ew7J9oqn2N3UMlwvDIn6oBLKTgBaA0U-afn3Cuyu534qpWHmqMlKrQ6EXpA6UCe1WnrkAJOWMCxuqyzSAU_rPFXUqy-05DIW3ej5rp9j8V_crkHYMTlijA0qirsAcG335AmfSjwAGkvvaZQSyxqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgHEcJW08UWBNRWSBojAjRxIL7GiXKodO144OXU78dR9UKSddV4Q0m8KMNBbIj_bIq62QjfsQj_hZxlxRGBtWBJLIcGcHb4KuGRjH-hYGUs9wqHNRE91LpYKMi84Y5PjgZYU0J7aWBPkiGCCB2jugnsxr3yL-GMPMB5uVBJQ1g-nUOR6iXFtQNSB-k-iyaMR0mmCqbtEH4Tezu7yKYxmcELlmPxlKaXVObGgSPRceovZUZHJIf_e1vR-DK4nXvg0MEoVMNBwrdvsypA7ZRstoAWmcet4vzm5j2OcfAP8fuoed4lEqBJ90eDR7x_GbFTucJcqREgXYrRIlZU-fcB52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UN8L_s5Tshk6p8KbptbQyiWr8Gmb-FXlUpYaA9Yvfz68RFVqmjwmYVUffUvQRQTktk92JmJnktBgaqsEhsn9u4o3TwJlkly79olVxFcDqgAAhvC3vkZ2PHG9i5_5smysjOzK1tkGlQeByaRX4Y--v0fjm6iqEmyaTkxUbh6PQD53HWunEiLdZAWnMPd02seYa5tlrCeqvgBDHKK7Xl1yaIG2eoIQGcef954dTSnkKDnP2fn6XhiasXQ6DGriu1L4L7qfLVBwE9qXmH38CQ17eiL-qYh94N-dQFG3tDwUnzzOU8X-dpp29YW-J5rlO91eksC5-kS_kontfw7-fu4gZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToS2IDb0nX2U7N0hWS37qH8PENlKBgrivr-Xt7uWt6O3vBnbOUU6R-Vgm-xvuF25Uq61jeTP6pJ7N63bae_dCcvxeLcH8_SWsJ28tahB5YBtseuoXF6kHaby9-Obae7R4Fbvh3vvTBCgPR4j266_f5RwvTY4Dw5lk8AdPCCZJ5RsSIAI2KFNvQaqWRPx_2bIuV9OXB-PgpMVpcUuh2p-MUipeAMT4TqRmbzymK0TRI7pxKltAZBhyp4zNh4P4AR_OX0oFv-MU9UXHG8-Ye_FMII8lpu7ywJgCwvxCvfJHKTSvUOQ4_ccVaJJmEY4X129lX1RU3xWr2MUaPgF7XWi0g.jpg" alt="photo" loading="lazy"/></div>
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
