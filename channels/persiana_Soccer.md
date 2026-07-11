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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 02:08:25</div>
<hr>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcR6_mOgBqhmIbQicjw1J6gb8yD6_gpOstgH-R4PTvYY094kvb2PiMrh3Qi1zbLUxFF_E-Fssrk8PBC7fxZ3FkLy77teYRYIW8LIM_q60vhVTy49_2k29bnuwdd8ni7frxYV-iRCNrpPjT-nX9wu3192X21NnoNZdnvCcj6ikypz49azy7tTr-q7amkCDdnMrGgHL7O7k-nyz4aaLnlbq2tkmAQ-Hmjh5HJjBg0DMGckJEOu8i8BYCHFUAYso0zmt_pLmClII-bTOVePh19316-rzJciX35d8v4eyKAR_IG_mvfBgPBHUqejUqpsTLM_stajbh3VXbCxaXRa1HicCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش چیشد که به این روز افتادی؟ چیبگم اون شب به جای درس‌خوندن‌نشستم بازی آرژانتین - سوییس دیدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSw_7ia6wdoDUhipFnvN1dGrNxu1MOJYnOfG97df1_-fYciq-KKpVtSMirLWANvpzGLmQvOhGHVd0bu05FAlEUh8lhsl4qgUlGF5QdvJzRT8OS59y6yhrFP0ryKKyLAssKBiTKF0EuGtTYaNEXsLpv5zmog6e1po9sFH5RFNCQjTNGI8PkTuRVAaGBHLl51P-MavYLrdpuxvesetdpyOd_JkhfioT863cuVGsYebf0Nzn_y2f5c-igV0mDlbEJkl4df5si5zmokNoT7d3SS7tHR3P4udBcGVtH1bX7dfliFe2DTz2fe-5bWocjm-yJSA4QMuAGcSCoVdGJWEcmg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyau-GVGPPYT5zwCd9GpQN-Wzq1AWT-pJ7f2Ypt7xqSOT8-S6nUunn_N6MgipbR_2vv0Qjdl9v-0YcZujCyglkrQIiPr7uRhtYNyY7z3Z0a-BKe00msi1svcqQjGtV1y7c42GZSENiEJsv2AX36Fgdd6K82bx956Vuk_VU9jhjRZJlz2jUmOtwwWIukMgiiJ_YIRDpECbPzbnM1WTEzhKqc5PgdKmf9lddXHATxVLhIuELYoCAp5PGsHQPv0wgbV1K3MTfFYct-0zDu0gjggDEj8nq8i6NMKIFFGVbjToAJC4IQYvlEK3p9JKh7xfUxaet36rCiuiChyY7fzPZ4zRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTMYrb5y2vmy0VPc7GxHXFkC0s5uBUENqAMif7uLEME7gkQFcYOXQ25d-gec5rfFZFhOsvTmT4FyY9S3fhZGxN38cIlfb4nyLKzD-EQbub8dPMt83z569JGoTTz96EwNJ7ypcJrhBB9ZDYScypyw1NIvfSU6AZ83W7-6yKaEd8UdkMcOCzW4mjDx-yIDF9OpXgY2fNDpvT4OFMGGU_SauANIi8bXlxAdsbexvmYWbPGSLuy4BE2DCy1ZcJU60xdL1wHxIvtoxeiirVwEeYtj01jS4Ni5NcWxaQL3K1bLvrkquYMrDjNpQ2vzMb8bliM-K-pT87wAZsAwyikUHzr5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvgjxT3aZR030Mx6fJoAKp3iz5PIP7jedz26VjyBWINBGEiIREO4nOfzSmgBv9iD2n7FJhrIly-ZhitD3Un0KuPVIK-NKIemucz6yXSELLStqNwSENsALnlIPIHmBvj0N7fjEGW9niuTaz7sKsuROcmm8Ifvf-5z1jZl0JLnijVESFsM4wufGXdTV1l-kMLapqvqHZ1cneybmCZWsRrlI4W86bC25C0EpSueVFKT9junY18tbm5XnIyk5Qkcbf06BnYOxTbX97prXCr54idCEDCb0Fj8VVo5eSmurwaEZqA6BZPzeuY-QutJXYs__8En2IHbLVFYJ3FrMFjXsspfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQk1jGRnlsm-gNW9PUUQakEjOhdFUIDNISjrJgL8jAwC3qmAcKs0188ZnDJ2mlx6OZaLXLxHkijDna7YjW-4AJ2fEWQT69tVgeTIR_uw0OLXzMnACRDgxFCl9zGTPyIhz7JeBoT0ZnUGf3Yf4E-XLK30foKKFAhzfn_ux-cgkf9PxszqtU6yX9gOLrk6UFbwRa3lDUZndDY6vn9I7IdtCaMWM9IgnZIABAAH_B_CB1lsFKX2LGAkAliegH_ajBQTgFUeciQ4zgof2xn1i7iJOuywAG2brDovnr1bIsLBHtZy3dvFjOBovvIvDStxr9z4-ZhNIB39x7UfBonfsMvJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ieh8r97hnYKrRgz43i9Hdz5hraqt66RPjK1T3fnXugxntPCAc23WDWj2gik2G9-DumbFrHbxeK0Ex82SyZMp4RKD__Qbifavwnv7UfBtuwXcjxTEFjXsgxcV9OL3nCVJD36ttENDBRQJsmSERyjij0Eq8ZsEd3Le7Q6zXHO2Ie2A2oZZsXtAfhwgwnlJXKXYB_M0XZf5xVtRikjiya84Q6hyo0AAI9kBqzigvcFUJuEcXgFCT9wGOkwtgE3fQtUQ_G5KRmRQdW-JqCF15KnejFiTHkQEHsPRS6PVNP3SMpA79lBi-IL2bUm8pHSEwxRADlMA3Yk5zQD1w234AAmwBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHZiwdDkVBa6hFMh2GkrWND4wi05SNV0YPALq9sAPRHOup6drqcKykqh23yGLwCz_RFKZNtXyi96cxEcnY4DZ6tpfwPGLy4BpOsxqa-d6X9fRHPy2J0rwGRgP_zxiytS98ofeWcW8Y2IoNMb8cKuz6P3_aJ_7I5T1GYumTY4YcFleg-WZKQRQXkSHuxM2USxw0R9diZf7N1Ia4joGmDXPhqJA9_QVrUDpRUAmQmHF5LsyoRMnzcF8_Oh_j9UAG_RDTP_hPVqwVoHJhHHZphw7lFRYE8SfxFq0c3hVhzW95Pr-R3GWynrnaVHklo6-rNZ2iN5qPg59g4ozQ3PUsnPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rac2itQruu8G_Bdos62hFBt1F3iFHTr5kCYFF2CB8AePqed3EOmnYKJ2UjnPqqkKLN7XIJsESFIZG8BGmu1tlsiwnfc0JCsaqTjlo3UL9CgPVONj7YrbDp1mjNn0XUtRLBHTKGOnetahF1hw1la7gBPXY72bGoG6EguMPX49Gq1hF-7WiAWO2cAdbZvkA5hLRs6-u5dYG-F5B3AYwiQvNoLKSCzigUHauq3Kmd7__RJvPjw4N15bA1xWQISDdG8Pi3Mm6z-igTjy6gY3m-m43Vs-vZ7uTN5a_XCWucWCx-iJofeHeb_GbB91Tea5vJ6CV89ix6N_Q4zKXBjiDsbWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDOUBhMRhEQiEUYEuw3-AtBwcH-K_96V551TXnipRJf6NurUO6V66VvoS1xu3fTIaQpYy0buPauNZjqmcrqtgBKX8QcUMlvZZ2yiXYnXZh5BgzEC-3o2GrooZJe9Cak9uYidk2vNX4Kn6Kus_VADk1Dh6PScuhkgiQZrNLrnqC5ZU2V0Z5XBw0bKA59VsJjZ-K7mitq1NHGJE5LIz2909ENWz0D_AFR_eZA43Xg7lAt_5gy4k6e3sTv7WOwSTOLIEIVxaut8__GedmSnxal4JOwkRNDSwipcbfumoCreT-eE8X0mkfO3Z7F-XP0A75miRIvKlnNiTcXUpGocE9cd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2t8uD1vQ1slxmhdwC1fgc_Xsgl9g_sCOajMhTDSrXAIifv1ySE6UhPA6MvX5gk-LiZ8b1Ry1LSu-wEqrvmTz-9iB4YRmVFu2LjwBUcDCxQj19qkcuJcLQvvkL0QSsHcYPcwXXI9PaYaU7kMkpLeov_k0HHJgvNb7mG51GUhWWAHhXnzA2JvU6wfN0NE99K29-S7P5hnySNC7H4RaLrCKnF4WEsvkthDMqfw7vq68So3aQKvsDVmJiTv-Vl0u7Y2D89yUlExtod9YFNy2wYijMjYHC4QLR5-4AVIEVSZnfuq5iwqIl49hWM6XQXY66-3zFXpPt8VO06pBCok6YN0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C91RQJHsBe5o-4_lPfQFPpBg8Vva4hYDwm2aTRcr93qJV53LdHLWbQxSx-h6FYVe6VxApfkOA8TJVYCA3ynexUJmkxh8oxWonDNuk_Vqlgq9vwpOz1DesRUwwrUWKdCGSnqDIAn2h9lKy-fdJL75zOp_wjWqs5Z2w1l2T50nqQQzSfRajVlyQk7U7PNsyCoti4CzsYMsp9EWlcpHgopMIM6vfOUmXEF9rIzwa4oCi-k3xKO0_33SFZgXfqk8kWXzl9MQUfJe5CKRSu83SfHzfJ1OdU_o7qeGpaee1iXscrGBzK0G_G7mjrBFw8ofL5rpDpyuekQxMGzlWSP6a52mMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngZExvXYrKb95P0UkX6Lo-i-Slobbm4dLHiRxV36wzp6jw-MN22FGKo_6MkUdxtPA6JkjSB51FCRe4P664vq61_PglWacWSd6ux_JaAxeEUeEOovrVCbHaE9xN09LGjk520zMw1uZ-n8jYboPp06GGhMnoS57CmWKNpM6oaY0kxu-ybSzeBgTGwQVy1jhg3_nJVmt-VIxXzMkiGObSBR1eSrM-KwoOVsnKJP07Mh4gWInljJuEWeSv61gQ6Uvw1GuAt-_pIvNLZTPfHrGSzvPs1tOb5Ddrm6SCGrsqXxEoJi1FYn1xKVfrnZffQIcfwRpuFIh9h4aYvfOXqBa0pPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjxKglsdb6Mbd_UNUzznSEFJba-hUcAlksaFDxgogYHRW_1hWPOy1r3HYgMaum3LCflVMbe4vfjg39cp94ZwqluWYR91_Ar6kfmcIyolrmF5yZ3dUZ2wGvF0mC4d3mWvi3hpnDmEWy8jeEfcQsOnODnZ2qbSuI4tZR7vExqgOKU2nPkWFFpNy3vGt-JAlvRpEsuxoErpbToDAnlQFk5JMp1aEtlnBn02czNBv464KW8-6nCua34BvFViKJK1DVEUx-agNm7v5DqJL08XHZ2VMdvqqwZJPJiiBHo8Dcav7JTrzBnLX8f1Ea2jfHjVd9fIXAsqbDxStn6cmTbsfhWXjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U96hKYMfFSWOJnz_zWk2pW9JQM7vex1V5H4S_X3gGEB-KSggWff7HGNdszgoD1aI74xNsZOOwsbbYSyzAIawoxFtXlkzx3k_BBuFeYDwkNqZ6FLq2N68E81tWE6QWDzPUQ3m414UItrjHj8Nd1BMpx4Lb81DUQc7kGtDqmGtfgun4VoXbDlAE_sd1ATTdrsynrCtQZX2GsqHeeQnNubI6W8iZDrxCIx_KOwFfleY_Dj-k3JjFMVFsCuFoQGNd2yLt1hGfJTg1jcDhzjdAlGZO9VymQC3r1t8t3kuBk3DwjibnaMat2lg_zlOEb5nXr8DLQs33SNESIkhjK11ZEZnFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTxGXxJ3hoILIB72CYQz0qHjgi_FtmHAEq97suaoFoMfCpwZWUQL6BexJVUmynmNes0tKtb2cSrrtTwmQQcAU_VaP3OetCS76XLRqKSLYIjNPWz2V6ah3vbNNqH7kBARXHB7wu9OTouk5Jj5-5j35DM4wTMF4ubGttGjIV83JKfjFlWEeFj7tqXwDbjMHRLqnMxWL5nlfW8JtuawU2DoXRRxyOGho1VIGV7wUWNWC631U99dgfMTJhSo1pIAJ0xR8yYI-JvsDAcIfbAbrceb6hIb_-guIwpBWVniTUlV8z8cmzAAdYGoLqhBNT-2tryXVie_4-Vw4JTTngkIko6MBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BroDk_LRpNNxwiF6vyDnzf8Iw82G5FD4H5VAQBWpThPfKWKAa825s6AVqFHoFgohbJOm5WWs_RRjYQHAxr_Xwg4CZjpNBpNdllVZtdb9DH1GraFz1DiIdkoX5pxC8PffjLt0OQM8BIfZANjoHnkUgWTvgYPNdTF6MCcm6_pHyKizrt8nYYd3aCp547fNFJfP4JfVwSz2huRRI3oGHcCtdyR79FFkGaWrQXcAfkZZebGxc9OQrduC2zftziJ0Zc3dAcxGHK5ZPGUa-YQSqrAVCM56CXymwKUe10O0Z_gJelgpSSnCn8giCHiOzZ7F4m6tFNOBBd3_S4O26UinlJ1IYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obV_3tY_7TVC9N4T_o5OXBP26OreUk4iCQOrDss-b-TNpMIrypE5QNJu-uwHOnR_UW56nuCktO2Qiet0FMfENvCHQgCfn7EGGxt2qeb02tXTSeJgIriEzBnUW04gXc4CS3GN6BfNy_oRlO5YtTMlzGEDOZth8MAY-cBCZ0deVWZCiRjvNB2ZfB8A2l20OKfb97RJhlEbapiqd7Y8aSz86Z8Ai_1ULkN2t0oPIeEmfeJB4x4CrbkYLhrL61JN96Qk7SRkXy9dtHW6QszQRHxo7Z3UuIMXwZKaCJFzlEhj3xzGX6OezfsVq4uFjHt93OfTQFkj9jI9irCaJ_-7clR-Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25458" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4aL4KftYmYd6TG0jz8fAczn6NBZqIGX-bUp9F0VUY3edDyp_aLsAj1xzMWb8hKNcd8IU5pomysSAB1zOXkPzqhg2la-lx76UcWhHglIwUhQV7QvipxugiO59k5K_YOgc_0OSpfFfRjYLPeQgAh3seXXQuLV4bVDwcu7lrLYUDuPT8RaXffEzdrEyRk67l58KBidrVbUdp56jWqWN94r8fd39NKt-IF7vJSPjJDos8FY0sn123mGpzWE6iU4St2jwIRGGh0WIicGrpkzSK1jwsfg9xlVRb1hLk3E5yDYCd-w_o8KyVjZADJJZn8LzdCS-Ev-vrxK1i-VRktGnvbF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5h91ST3pc43bTWcKDJsgLS27kmTi9wbngZMRpE6P7u_72KfrVY7WjsfJL_CKGop4KmnIP6d3LGMNxUI3tsQZESmWnD5KnRXITCfRjq0Md_0IXHMRvMo3TSmA_8C86DmjZDALWsiybAUavRpWFe3NV2gMBy31Pzfdlw5sHq9k5Pvopg21FV2lfkJdi5Ao42BZjkS5Nb770_uvsID7b0o3fVXpw-SnoTIxKsii65d1gAYKLrNRM438chn9XzfnSfWYJ2tSgAoYD8JR9AtSNpHeCDmFeQ3KdRN5a-zD7r6okrajGx2F5CnuYYXRktgXH6v4r3jwx9AluWfbyWyHa4Y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRGj0O1ns7PG0MrADifk8JMG6f-uvpSELaPwBIa2P4cSXVL0J4pIj08MohQPparVhrp3CEWAG435JchC2UIiK_EKEjXY1zmpFq3ZMsxJDyRPEc16v7GUxn6G5KzmQ9b1Z__02-o5zeKiWZDGqnN1U4nmVr2gRc7fdb702jCyBHiB3vrpp855chzn6YLBpIYIhOkWfFluJKBUFPEZpIHzX7CBo8wdJ-IC4lhdNS8wrLBJ9Dk8zVgJc2oNP-kNQ244xcqL8LU-OVnTyOqLYc57qtq6LQ9UgpdsTjFXKaSLIj-AdAvudiG0tZv0hd96QO0DPVTihrQ5p5jtWSXogylyeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA92UrkPVvO5oncbNgEdmpwN_E0t_0Ec_xy7NH4x5C2SuV225LWRuXS_5xiUL25GD-zjHYJQ1FXgCvcJE3TB2X90ZT2rieXVkiknl-KHDW0rOcbeJiCAOhGxARf70RcbCh9VcnpTqoRjndtUZNKqhVtoQJURFCbxbGMNbZ1kBdRHIp4k5pJVgrsB1gMJMWkO6dIT03_pNnVYAuAx6UHs5vYzy4VzRKA-0kmCRht2Dde67-45G9l_xXLmgS_rZSvMYMuQYRSMl9I0q-LV_6zmDR__sNOy21JQD_EgW88NQu5Xeg8H1P3hYZBowcQzWgScRUbe65rXyf4R9flzsoXWbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hiQ40lKidiwAgpCBV9qfkTIsc_t8uCWSV3RJMvg9jEN0U8uoiJ_1smTajhTJDt3G6kTvMA2mP-U0b5HEoqjuH6TvA7NFHxXPd6BHWabiaDx49k-5cbKemO0LYZ5NFikl6QydUblR601rAqJz0c1BPsgB-QJyrs1sGdSH74aQEBRq_JyG8fxAvrndn84ZD7Ey1hoG7ZXJbAzcFUC_So-afu-0c29j0CBkMkJlHSjN-WWYIOKmBP7qYy9IA1QAD-pYTSdAqJF227wpiSbFQNB9GUlJOY9GxB529_uS6B6GrPgA5p1JbwafypWKxCvUnLAfSClwe8ftHDzAsv3DXwLEhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROOItZ8VNtR9-cyqZjhwjf6RW_hN5Pw3DPWmgMykZLaoyrLgCOJhWsP39dY6b2tEQobJxoJiAFrlcsO4nxm5MBUJe5Xy5D3v-WZQ7IX_UDiB4_T0rpEbZMZSsu_E30_GaZV23OlOVpHacSiOVkAsBzgkkbZVt7dlG0VnE_QJqQTe5cBT_lGtqZBBQUNjM_xodm94SiXtEzwB2DrNfOjIG-hppu06zit7X-TlO6m_b-1nFXO5FuFRay3fXhTXnSAXrIFsCTN-SHKwmFhUE6q7CeOC-0O3SzM2nFWnsc7Ie4Dq39Tsu4_zjhDpL9O051fdPK-2K7Fq0CYs6VwFk6CBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7bSr3WeT0WfIBT7Yd-GxAQmo3yFhANXMbvcwybw5gBvjoHT7aB3Y3sD0-8II7pPn5VvtMWpl3zvoEFOg0zBaE7ot8GnNoQQtngcGJ4wlMmhs4i-RIVMd1c6THVlcH6ksbshhtM64wkGIR6jkRHysrWMKzLgzu-LKG4JqOu0AqlaK0ZKG6Uylq4FQ2tb4UxZOXDUoMZDhOs24PnglDat0YRPKAZBUD4KUu2F3KvpyPiE-yRTf-z05afYBlBoT1-2fHsMQo6yUHLXFZ3CxQCNZ8U4ajH-RaFQ1bDK5vjuTuLhUsvUaRP35ZsuSs9ZVaTPtj-15slZ60KT9qMNllekBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQodNstOKCQ9JRe3_j19yHJtPtvSMIMQAOh7hBjT4y1XSeGFIRwxxPdn-fDNkjK_QCkQ65p6zsZfGXeR5O88ihfq5YPbhKnWIAOOPTq9kaq6ULhnXfKCGUFk0l-5Ut5x0pH05oz0TUIPHHnjKG-Q797zMbz1xX4Zk30i6cKppxDW7p8YIYxVZ6Vjbs6ss--gLlsVC_XYuF3avn_pnaU0zM1MV8lXJnAxAhAW9RCety6oVJEPFAB729l4ajAAb85o3pt2FC1IM9V5SJ3WBxmWLR_PCN4XRh6iS-mZyJLV4Z5Ob0nRJBYdvJyhKvNPTf83wxyShvFMtQYndyderSg0Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKsesh42eXmFBvJJ4GAVLjW0dXPEScCWbzJWlCksl9I3Sy9j17QXVItcqZ-UgynVo9Qgrz1wgopH2s9CPbPnxjeaHwH5OdGx0H5hGJoV0O-ugTw2QQsfwgdHhAq1Kl3GFSW2uC_PDz0m9nod_itL4eWKVly4_cNTfFmTELjxQRwJoUIoxzipEtvy_tWXDWi9qZa8tcQ_71Z8xx0QYa23-BoGXVRSOOp_4IxEqOHfDwzQnwELz00HTz3HFiuVGIQTIZySFB5D5rRB2ZHNZQnf4-wDKCtdzmnhc5I_uYUdRSFL1rQRs1mTZ__WEJ-hgWFgUsudjwVYZFJ6VCc40K-Taw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lk3GnIEwrxW5c4Ctgg_MM6nvcagjPCBEUHH2TUNjeGpYUNpppBarelBSOISREOorfaqs08krUccyVKze1IzDr7fUWJrA7hVS76EP53fW-KuiOIo1SFz6xkqxafBQHpGGE856a3ofOGPBn9njXDJZxLfsle1_ikZECEkOuz9T_IARRe6nO2l7gwlyPCfZH89rYviBZJR9jH6HQqOgCeVtaJSpjlz0J2U5p1tmdxWXt5K7Udy65wESNmDQrGUpzNqJS5NP5TiDgDi9YKxHmpuTXbWknX4HWWFTDGcD-arSEOQo8ttf7AhpZMbCigW1RSQ_qP7IGiEC_MhUdZefLtiH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHMEsWN4OON0EWRTWhBJD9Ap9nGlmkNWMsLhz6B1cy5RPvhICp1WhQ_gSJWpzedWWoquPpOnPS3qONDvjBy2VnNVNGsluao49Y4GbV7dBEe6RMR39TBOx8ZgsUYcjBU7Jzjg16KWjVXBjwFB2KnfVH71w3fbOS5cXSXgHCa7BWvlu5F09HcrI3UZYv7HGy32W5UMRWz1wGNgFTtcMTiR4MkFo8Ic4_1ZEGgZznIhRGFpyHCKyaJy1IOF2M-dLm3AQiZgJyTamm_ddPVWwKKDikRpoNjYuZ2YDITCeXKtVdp1e5o99JnV7h7ZKkSSWo9LMIsuox4WVZ0DKKlIbNLRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVW6acHyb8Mp0IzHnzGZXhgQU6F6stg9iK-yX5Y2GGyTWyBrYPb1DGPcxnPyHs1D0U5uTQnoZKR4eFYK5mvzyznO8xioqPkvhejjA1YwaVAboYS18_dQPRdi7C8UCQLyRPo5DGMBqqP4dENB6drmfqoLrU1Xg0GAt4hhP21XvgsDd-dD1iz3VZTDwf1FzoUuDO45UlNd4xi71cQkkyx3bd6kpF07z_uRiX4V-3oSi1whvD0WMmJWULE66vtB-yUDYGPjOFnTJ0Mqm8pWTSVzyD4JQ-EZxs6vh8vZkI50MwXwEaqbNvbMTJO8r9FltziVf3dVVnXsObZWNn9O6Ay-hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 77.1K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQGxuYjim31atRpVv9NfsIAlleUJQ4iqNsk6QCw-MC4U2MOJA63Ypqk-kpi9jgYodRaX4FU5fNyrk4wDrhuFuBLb8IrexQiCb3pqwHOR2Q0qKA7WF5zgJGXhLI7r9bx7ngpwi3Sb8UHeJYouMYjvjkC1dcwVycZhBV8a2Pk5nnRE3sMENT0R7Z85bl5FAEfh_kBMhycGXlOfQRwEIy_C364rdfW7yAwgt8m07FV8v932LvUme8XL9QIuZptE-36L324XPoLrRTPQnlzLb46Z5Qbt4P5Ru8A9Fc95N2Uoe44XH-yhN5gOMQT5IWFOfHUskvR3rnHznfUVAwQqIRQI8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poK82-X8Ln-UR9FpJD5IWt70aJnbx_V4UbIjo16fLWKo7V4c8BoUGxZR_rnchuBM3pl_bsGXTZG4fMOeJyu_2-pdToeXu-AvII5FK5JbR-7iICIKfay8EdbF-9lUvCvNKHPG3h6YFOsNW25wWnu5sI_6AytlyuuaYEFz4ZeWq3sOM5jHFBAHQpWguclCr87D5zUj-DRUrRpdnGQzvEARfVgP88Yyw1jBYm36MeE-IzuYCe7NoUqvMnXyUM2RPBFUG4DRXPXYJy4DO0xFNR_dkmdj-r0xfH3EiKxz6C-ueZa4IvPvethhVy9tz1Rh7K5724I4VBtNlebug-YuXFhRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcWLDrnWaKXaHunG10faVG1ZJL4KScdaRTf-oDOK2ylrNysmjYOpN8uO641ulKoJ26LiqeN-hRraLZX8gv2PhtYRj6KnQlTN4yinvdacmubXS7tqLJ3sbKqZrnSheVWiCNuSTzi1ATMahcJU_0av3tye9FhCMSDt7omPeEqY_w-IHBu9mv-3k-Ogepe9f_4qib0P77ezznXqFbT1JdljDhlhnBk4WsbaHqJjzVQ01ojGTS9niA81-QS62EJGBS9DfQ5syjjfJDTwc__m-ecSG9eCGLDi-NbDZHeF0q1n01gx_xF1khrccmusd0nqNnfWCm1UAMfVwL4jKe8aqmmvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cf9UuxbrnBO4xqb6f3oE_wUmdSWr-ae6tRlWVrVSYP9FJKFfUV2yiIzTS5HmImVZVcrn41yBy_tRDcrMbaEOQB5xjp5sh87Hf5omwCxwlzyhN8-Hw7IMUadx9RwEf9jfIGvmGP4P8Wbrw1wmWDaWL5DXXMkknyy6kLs3VIQazGyinzsnS2p-kT4Ikg2pxNKNTJFv1-co2-fnejoTkfLZ99nJS0-DOBm57c2KTfXQqGQCCRcc9awj5F5RlFLEff_Yb7i7BtvsPKm6JYDmrIYl6kwlaYu2lbfhTktw0raXYvWCfWI-xG9kfIIYBGuBc9t2H_q7rBcY9O4V6K9ohJinKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG7fM6M4ySz0IeHVFHO8KZ9rwdLrtfyDq8nK6l0_gVcwKaLXZvb1Vwb-cLQMOiiHikE9Df-ZWvEddSEalUbEkVdfrPXxmwEODnN0_B6I0GEvRjOIinIuA4VDr34yvd3NgwnubZdD_tytWcWaRryOfT1-tc2NmI9U-ffI1ijD7qbHp-eYuTNqbcZZoUEBkzmfHljgWys7aqORu8D6m8eY15c0p3OIufFWtWeo6MjREywaY06ejm1jeCrpttyK9ofBnMXNmZsaONsySckLvWj5V8V_Zz1549uwO34WjfgEc4ZF0XcbU-n-N_ASmUqk4SjKyX6hSkXAQA1J980vyWotYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSqzQo9-TJGk5ozRYMqtIfXhehOq5MpPuXQjDpyB4bIHC7ZhqrOoYEuJPmd6Lff0NtK_fLl5Bz6vAm0HdYLLmOp-jdEjmXGBKjEESbMgNy1vVp_7ciuOPCBSv70cDycau9JurEW20StIC8kSy4pf0U8eAVbfibSg-KmDhVZ78UHo0bz2ChkEyFHpEn8rMZ0wrjrFPBZrRgmhuvhIdlsKMXcGZ8ow9SAZGIl4aSE_VNsnBwjUmrz2PoTt2JqFrKm6-2kaax1VmJDEaLmVCAaDGQebpkwXaJAsNkwhhbK6TmfiDBwN6fMK-0HaZ4SswowoGC5ZHAVQmkP9uE5xNFKPHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=lkrNY43f_56mVj9bDaGzjlqJYdPwfsrEHRB3mUfukMDrgCPKW0tJ_8l63nG40oH2q-54YIvQQAeL6YU94XSB7J7NaML4RXbUmNVROERypz1bkm2NDWyTvOPkWZAPa7uvnxF_ZiEDfZwUZQh_ZcNoyYMq7fhtFZuCLlv9CWnQPd1YNRTN6MKYFQ5XCjlYgMyJayTWldyWu9tcWFTNgZ7aIiMR7zLzj9s_51tiajOMC6BS6tNMLYE8Dcwx0CdlK3RgSBbQnVS_6w_iMjk0ktXqIng-CdeHsD-1ty2d6xyKLDdiIhwSJf1Mqn_MGw9n7Xz-gCl62gtYnYo4m536y879gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=lkrNY43f_56mVj9bDaGzjlqJYdPwfsrEHRB3mUfukMDrgCPKW0tJ_8l63nG40oH2q-54YIvQQAeL6YU94XSB7J7NaML4RXbUmNVROERypz1bkm2NDWyTvOPkWZAPa7uvnxF_ZiEDfZwUZQh_ZcNoyYMq7fhtFZuCLlv9CWnQPd1YNRTN6MKYFQ5XCjlYgMyJayTWldyWu9tcWFTNgZ7aIiMR7zLzj9s_51tiajOMC6BS6tNMLYE8Dcwx0CdlK3RgSBbQnVS_6w_iMjk0ktXqIng-CdeHsD-1ty2d6xyKLDdiIhwSJf1Mqn_MGw9n7Xz-gCl62gtYnYo4m536y879gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Psw076NNyx3q8smea_P6pqrkqLgOAgSG79kLWeI19UsgMN6S_Dnj6Q9vCt_EI4k8yoIE0UMAk233ovlxx3jeCEY5MVYa9i4vTlZIp2luQgZN-Bu6tAkgbqUBlMoqZ_m2aCNxeHWSN79DeYEgp9cHdKPii_pILSgCRxqLC8Xv_hzjpKi1iEi5grkIb-OkMsBa1WwCsMZl3BtZrrfEUfjzrsZVZgIlYl7wO6XYCWrkkXIRMVcyLJUWRJ1KIRijrd4HoGFtAZ9x34YtSBS2M9FMjRMQYwH-qbP2rHafWQhZiyS7A37CW6w8ifMa3L_eS79KcDNiTAiJWeJZHz2hseB-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qubQ4IjTA-gB_j5nR-lbUypQgu_DUPUbzUtdd1YrZuJ8_9jVklFy0zy2d9cgJ6SAH96hBeu9uU4Til0QhF7m_Hdxk85KWvGi9rlWVVCeu1SJGTAcFlrGQSb5pzpCDL80Nz_f8ax9EsBfElh4KFPwnenjzpg1eBMyAMNAvKC60jACYPtkJSZZXNKVY-w5rRT97N3Ty6ZcRMYXZjG0q4niXSxIrVGcpSNxVIkxx1SKCXrD2R2sxfU7kaKQrIOlDpm2iBimgKeElEAQXaH2-fET3chB6n7a8uPAfKjD1mhNHZ0A7zetgZPdgeZIngCf3d0fplbZAZKqBm8kj28PyFeb3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpcThPw9Bq2b-8kh0v50uKiAsadJK2OSVY1MNF_xGtI8Is5rs1VbHYgrGyYwwbEUNRpCO27MhdMn2PvYxyAlsZJxxTaPrgwLLrOMcdwSiWz0aFNYAXh0c2iSmQHI_MVtCeROonJl0OTFksMoRxZPRxbaTRlY2UMlKtmrXvMtJtKdHsxTMBwH-4kt7yJbCPChgAzDRWvwq2oPZGyX-M3fFR2ZRZLpHflpUWaT4D2_uCi8E7Ly-K1EMgTYDZI4501jLi1Z6daY7M9p9eNgFd7vopgfGZe8oKn8At_7jemHkRXFT_InoqMHqgM_VvdxBRybXNhrz4jutcHXmJ5zcky6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq5d8Kb5ajw78BMzceTSxdpf71fcSUkAI3Eo5URn2T3zRInaiyzrBBwleXDlmMjR--971FDVvNBQtOsiwfRdQpTZ3Q2DhlSRxT2KFLb63YKGbfuWwbWZuC5wEj2NHgYq3dhKQSo-K5cb5fCYPN4MQE7oeJU3EXMjVPIQUYjqLhlw__dGzWMyA3bAtdUOIUC5ARWAtSSObrPZE8r8RNp0I0kTBafjIORGvl-3YoVVntQGb4hwb_wkMxEXasv9He7uxO0XiAmYlRHO7B5wkyH-bBiPFj_DqyOU93GMXNy-Uh5ZLPYsDxipB7mSaRLN7ydbmPl5Yazo2egCH1488Djv1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uk1CclMbvqe3-G8iCGLHvQQaQ_XQ9MRBqEw2alv7Gu68YQ9sTLuZl9Hy_PPKJ_CtLk648vY5ik5bHNkaB3r2bIENiLRFf-dzlpfwrEJcBK6SYeFND4TEBFREdWNlzRv3q4LfMQgSWjI8KFwJEn0o82IwS_hn-bLtqUFZJAJlt8M1m8O4-hjEgfBT96N_wrw_vDC0CtZcMrB-4BcI7BR1Gv3N9v3JCVGwkBbcUVFRjLpgJY19W0BOjr_uh7i5zShJpkF9FynL51BasLxDZZckyE-qPncOxJT9NkgrKog0CwyF6jJAANmKMSIbgnh7BA68e51brFx8PGa-EIXy4w_Vbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6idvcADAqHGUXUfcOAdASiXZyqhqsyArtw-yD2oVgtpD1pWQdidLj6tSTU2PicykY_e3ANW0wBinD5nBwpNnZMVUTRmcQy7XXNa1Utni8ZmJlKKh6ILds-xcTOSXe1Yox6Wq7phKpNM_WnkBTPUegVNngz_fiMg8px2C9qkPnjSFXRmfKaTm8sGnNIViqpeh9hsLQo9n8TY8yUZunwNc99NOGeeB_yahyymCBEjMP0Htsqn-CkRQKVaN8lVmKQRSXLC0ugCdxezyhap0F2AGG9Pxp0G9Pnc0ew5hI8iVXUGCEh8NQ7ZX_hNqLay77Gn1oVrMDw5WsMx2aMvSw7gek2Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6idvcADAqHGUXUfcOAdASiXZyqhqsyArtw-yD2oVgtpD1pWQdidLj6tSTU2PicykY_e3ANW0wBinD5nBwpNnZMVUTRmcQy7XXNa1Utni8ZmJlKKh6ILds-xcTOSXe1Yox6Wq7phKpNM_WnkBTPUegVNngz_fiMg8px2C9qkPnjSFXRmfKaTm8sGnNIViqpeh9hsLQo9n8TY8yUZunwNc99NOGeeB_yahyymCBEjMP0Htsqn-CkRQKVaN8lVmKQRSXLC0ugCdxezyhap0F2AGG9Pxp0G9Pnc0ew5hI8iVXUGCEh8NQ7ZX_hNqLay77Gn1oVrMDw5WsMx2aMvSw7gek2Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAq1_wLuC5-rc_MFL_VtazXV2UuBKdKik3HZ6nOvrP8c3WWmiNhopOshfYj9dopTlu5pKN0E3p7dCSyWvF9Lp_3kvi5LG2scPu0CY6H3zqv91gGyuQF_eBDnuIN_6QE1KGCQDeNit3k_hYTQU0cvZDAolwYlDyxUYwNc35YaT2AokESzr-T8gNBP7Ddb1pv8XYJzPZvl5lOAU_dVTUSwg7vlppcgeCnSTm5m-jCSq-Xn2AGG0w0Xmhx0XV_EIvdEfEyP0ozZ5uJdhsVhUeEZ3Dv-SCcwu2GvX-dD4tH_BehgPw8RykAUljDOqCiHEzMmx1rG2voRqpfBdsJM4LnWgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sp0XRocAs4_SeWqaUs7ARbfuzOUiFHHRn73G1oVKmwGMUz_47BVmzpkvnNb268uqBNN2CgmwWgqFtMTYmIov3arnVrq34w35Anr6H5YOXfrisge8E3eSba6nEqpKK5MISXvuI-AJUe9nHmpNVKGwumHxNuMOY7HSQrl02g0UvragEY4Rhyp5UfSgvrq4XSy3hZ-RAXvWGFTDEXSzWsH7EpK_YT8IlIV1QnnO3-qyyEYp7mqMDU149G8qHKUMbo64tr56KgTnaJejybcgAXy-cZiX0Wjj6pEWg6gFGwk3wtZxLclElGrILJP7EUQGiNAr8qQ_ONK3ddskCsVoKOnFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=HCE7EMUai3cqD-fZtJNR8ZSrKM9lUdCzSpp2SSpIyIl1v0dmA1-dhIHXN8j7n71Ys7BB27jJPIVwny6w1Ctn7VZOkzA0xtDb-gufT8xHc5bnR1Mmw1w7bbg8QV1UcUQaXjD5FS2g-zpgs3gBxyU-eieVbPmnFB4_p0t4zYaTsKud3wt0XtKOCBhvf6yOLwHSVA9rcPImxithJRWysKWQqS4l2AbLanGl-FNpmQi3qGT68XKWMhXIS57UWNOGwBBAc-pRdLEYjS57nc_AbtgChjFiYkAvyNcWoAY2S2z3QokGQquhWdzA7zcPaGB4FStAiDI4PPIZFM9VeaC2oLKYKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=HCE7EMUai3cqD-fZtJNR8ZSrKM9lUdCzSpp2SSpIyIl1v0dmA1-dhIHXN8j7n71Ys7BB27jJPIVwny6w1Ctn7VZOkzA0xtDb-gufT8xHc5bnR1Mmw1w7bbg8QV1UcUQaXjD5FS2g-zpgs3gBxyU-eieVbPmnFB4_p0t4zYaTsKud3wt0XtKOCBhvf6yOLwHSVA9rcPImxithJRWysKWQqS4l2AbLanGl-FNpmQi3qGT68XKWMhXIS57UWNOGwBBAc-pRdLEYjS57nc_AbtgChjFiYkAvyNcWoAY2S2z3QokGQquhWdzA7zcPaGB4FStAiDI4PPIZFM9VeaC2oLKYKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwRVcjANXQ8OBRbzJm8-uIqy0ImKI9LebIHuO4o5VusSKUMAmaVnEHHWr7VnDuV-asfmz5-hMG79E_JVP1W2Y8cW8a4D0mikEMDOi9bdcRnntddet_ZG7iL37oMLfaotMUHfVaSyrZ47YNUu4W4nztd7-SIP0PKC5uxCWmrY59ntXUZXzaE2xfc73MBStO3TFoiC7Y7PWFCCpqCgHaxfx27CrYUR1-xLvhroUtaLTrRdfOxENvileHD5q--vudQGKwKw20UV909B7_vmHRhhnBFe1QQmSaYtKXT8dZikl2K8PUMnlzmyeJVnoKbetKhNR9ZhDxGHgefYjTCwUPXeUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBC8LSKZr4okVvI4NEpH8ZmhpsJHI3TqYOOK2q7WULc1uYhESw0sznY7qJ-oL8T-hARMfPZQS8yq6OUX2IGILTsP77Zay2nG28RwfKiSQPKgT8NupTfG71v7l6PMC55uXE6gqYqmZL-1Z6ip8cL5HGqG4WicZ9vqz33qSZxFKodnKnV6vmlMOEC9jfINiyLaKRM4ZFQ3OcCmCKm6ztLQ_GQPoKDl_11nkWO7yAcZbqUCZhA3MRDKDQzo-zMTbg8Fa6Zk8PmqqYLvwVfBpOxcyOFHEZY6jamnhgTyhKoBQK5Z8dYfY7pNKTPCpsLgh-QFIC5WFwvFjBrPs1R7i5ESaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/islXzdkfKYWTbTsyp2Th0Ufs3ikdKUZ47KqthMsHYL5XlMbl7v1u3d825rEC2On7GJhW9Sp-isp0c2ZCUlRsWnQxVNaZN--QBElb5GITy14XASGiR9JGAR4vidYFODu_9jU-tZBD4OERVJYDIBxqhJe4V4ZBY_8PLEx1EEyy9lXyYKKKpr6x-sY2EVZn5ElkZoQoWS1DiyvleGAqNBfo4HDAbSysuDVDs1kVnCmZ9gBIPHkfju3sQWNsgCMJYb7nqICX_9FSSAtj9d5mJENeKyRzuvJ5Q8atUV0EaHGvPnCAP2tv5PHuhlNMThiyd15mWojjMG9K6fG2SQcmTTpy-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0i1TKj9d3bEJRYn7LqtYyUUMbn04_CAE6CBJR9Nfmu2p_pqTbFp9uF8unf60JSGqve32NxQ86xT8tM9kxK6s80Zz73NKuas28Z5dkJWuTlZco1lGVPSaOpGCh-OuJJgyxXqPnhVrU-tC-7ODzULORFrvvDtvYDxY5DYYi0ltXxKjFn1_f06Z08d5RUsP3cygQb-IksB65DuJZeq41eZwWTBGX6PyxaKtke3yG9JNmjaq9jlYU4z8qgFXF_2MMN_pOOgCDyVy-fg-USnOgRk4ZVgE-tmuikIXTIHHk3RP-9c-R1JphK2UbqayC2aH_Q-Kbc7qfhWwSseq_lTNYT3PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxQF4XO929KfE5XNFsA-3xpbhwObwUV-ZCMR2b2Uol_SagRszLDdutAORn2ylm2uxli5V9kREMTRsI5FMqvjE38i4nP4Qf8VN7q4PbS33kj46ZuzOluEKBJDRF0Oz-PYq9PcJVy0fAQZ0yGuwW_2oP_VXjcCorx1Zm7jc-DU1ioeCprLW1pIX27Mt32s4gca-o4kWpiRMrEU0zw5MyBBs2-SZUdRTWkPHxWS7HUEPOy0yNiRgAWFk7aVcaQEwQ0KU1OiwbqOzlvUShVcOFZtRhe9k93x9o4IV0MEQyBNyuiJUE_RSyadxwb9RgUJiVncHIkKiHOnat9SqrGiQAiTdQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=QoUwDdvFBCRjut2lSmbYOWhFt3L1bQxpvTK5mA2cR-1nvA9tF7YK_6a9O8YvskpaLg0nVgxii-R5A2DOgS75RLc0hRo3Ma8fXJK8HnPEAst8tgg26vtf3lag1SHpqY4whjlSupPydo9Zb_aFmId7p49I9iif3mKgi5OnhsMMCbJcWtsaW_Rrn8hPC8KJapyIdTl2PIcTbDglER5hOtsyuQoK_Sx6tqwwJPT1O-tCyRB5bZxcN4KxpMnps0qUWj4Roe54V_9865dzMK1VyieFmfxw9GX4rCA6ZjtHvmDYXkfXvhg6dI70KRpEhgXs_OkOxbPzwWuUQExfjch2L0Tejw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=QoUwDdvFBCRjut2lSmbYOWhFt3L1bQxpvTK5mA2cR-1nvA9tF7YK_6a9O8YvskpaLg0nVgxii-R5A2DOgS75RLc0hRo3Ma8fXJK8HnPEAst8tgg26vtf3lag1SHpqY4whjlSupPydo9Zb_aFmId7p49I9iif3mKgi5OnhsMMCbJcWtsaW_Rrn8hPC8KJapyIdTl2PIcTbDglER5hOtsyuQoK_Sx6tqwwJPT1O-tCyRB5bZxcN4KxpMnps0qUWj4Roe54V_9865dzMK1VyieFmfxw9GX4rCA6ZjtHvmDYXkfXvhg6dI70KRpEhgXs_OkOxbPzwWuUQExfjch2L0Tejw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=rhVzz9rInocaY89N_9jyXIs-8Ft6vs2-mjgpEfwXSWDKc0A-5fjvNbehGtS96xgRkJpUSv0U28EzgiIgVi55aw6WIRzSQ3ur_HgAuy3_1Xw10jLFETafrLtwKoQkwcnB64PWExXq8LS0mmRknLpQUCdhLpHxWEaW9-huSvSSZ6d7B-x2KM2_eV92YDkAjofeSxV5UIt_oGO7VrFPXg3xUm4Ctqrgh0vcBT71drmZh97NGBBlkndzygs85PfhiwIquTZqTxa1hHzZIg-9S7g3seV10zPMaSXvVbxeP7jmclljvsBjGguQFKALj_zjizXnsmMZOrPMadngoJnMI9dbTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=rhVzz9rInocaY89N_9jyXIs-8Ft6vs2-mjgpEfwXSWDKc0A-5fjvNbehGtS96xgRkJpUSv0U28EzgiIgVi55aw6WIRzSQ3ur_HgAuy3_1Xw10jLFETafrLtwKoQkwcnB64PWExXq8LS0mmRknLpQUCdhLpHxWEaW9-huSvSSZ6d7B-x2KM2_eV92YDkAjofeSxV5UIt_oGO7VrFPXg3xUm4Ctqrgh0vcBT71drmZh97NGBBlkndzygs85PfhiwIquTZqTxa1hHzZIg-9S7g3seV10zPMaSXvVbxeP7jmclljvsBjGguQFKALj_zjizXnsmMZOrPMadngoJnMI9dbTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3XUykjHiGPWpw0OTu90BzgBm2PuyXM0qg6rgRrxpeN5gBcCJhfiSUsxu3qPkbcDHfwjg3n5abh_SI8ZCAtqaHjadpbSbg8irTfpOGvr_ThN4X3vjwCr-nmxqwynYG8Arm3utjXM7I3sYj7JhLZes34tJdgqS_Wqse-bZm80QF530C3JJl896uCuF2a68GAGMuqwjEAG99Aw5vV83sSc_MmhYL1vedxtufyVdxeGQEZ2aqmpVL0J6xKDYMVUzY4p6h0EA6CiuHA031QMyYRVOKh0OKSRYUun0Nh87QDnRpyT_3C6UlgwgYyygHJQWnAbRGx4kU_4GWEvgHOIPG0AcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8ggNnCckOs6Oydi1mMQ-V62K1v1h-Rgp4oRnNvEmCLo3sdhiAd9E37UwlOr9SAA2c_NHOqVSAIP9RjD9j9dGlJwW-3wj_8CTc3aUXznNlwf23iiLK8EcIQCJonI-aB6aLNMk-i-_9CNvt69l6RL0Fre7i3GXas-qRgQLm2HeV4QGAbe5CSE4kIgLDVVay2dmbyfoNKwpF2KA4kdQN_yimzDtVGrHHxZaq8vVSAPf9sdi9U2oXR6RfGJyiRdblWcL_s1YwUcLQYxP3wpDI8avlp8KfwV5MMJEXmDoel0lDaCvgCZbG4Xf-aTTlNWgvyFZH5nDnypx9_i4ovpiycZeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=gcuPw0Dh6JxL5VFaX30C8w8rixwfZSlBJxUVsjDGzOUepMqFR-3LiZZKvNx47oIL-ii4ZxQEPI3AaXphq7TRa2lL2gJYKbXOcI_CoX9U5EPj8n5NIIkzmcqjOmuaRXkoy9Qh5aFgDL0ygdn3Xz-ZYi_zkDWVybknlaWcMutwwQZqdK3ZNIAEHoRYD2vJkP878PQpVVh4GYqDmDKSHinUVtlEI3K0dc3YOQBwhwt5jruyZRLF4J8cLNAI3hUdLFiL2XCOuiZgAI4FJBmVsBF2kjlZRkUUyXktDf40LVyKlAt6ZfyuCxR9m57exLtgU8f94gJBnp67RiV9dlp15u4GNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=gcuPw0Dh6JxL5VFaX30C8w8rixwfZSlBJxUVsjDGzOUepMqFR-3LiZZKvNx47oIL-ii4ZxQEPI3AaXphq7TRa2lL2gJYKbXOcI_CoX9U5EPj8n5NIIkzmcqjOmuaRXkoy9Qh5aFgDL0ygdn3Xz-ZYi_zkDWVybknlaWcMutwwQZqdK3ZNIAEHoRYD2vJkP878PQpVVh4GYqDmDKSHinUVtlEI3K0dc3YOQBwhwt5jruyZRLF4J8cLNAI3hUdLFiL2XCOuiZgAI4FJBmVsBF2kjlZRkUUyXktDf40LVyKlAt6ZfyuCxR9m57exLtgU8f94gJBnp67RiV9dlp15u4GNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mco08Pc5SldONw44AhwaS6VgQdH27_8bFr39qXaZHkHDsZJckkNYXjJKIhUX6bruZhxzbM_5elEpNdpy-VuRUr5qFM-wckPtFz6KJKD0iYfDdq0z9MDI16AdUHfvaBX_7lA6aXVstn1yqmCMxHTU-91yDigIXqRS7bZE3jGeb0TgYtSiBaSskpqWg_PihNH-jrQn6OXm-BrlT1ixha5CCkFNpkV-Evn13sqX2kkFH25gL221bGWWonNVk83BWvjKh6-bDo52GW1sBU62CmXiJ_m5RnpsBN1t9QwknKETwYM-asRXL2aXG1FwJ4re8_Oi1sVsKwOrlhsQxepdu6ODbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHS-9Cjd4XlDi02tLru8bivCnKzy2hpABPZiTDRx3OtkUmnvIBeOW_HJ4-VF66fXwQzxcNrqnCmkz9vf3njHMCy2tTLvA0yE8wxIRW9ajwwO3umuk-yZextRrfihJb55OKbBs0xir79cWjVqbmEwGy-uSXq3-CxXuiPz4zhLBdrOVRqs_E_wnM_hoh8bNjZTXuZ4fPgCxRUU6tlJ_iADR0-TGut150_xhx7ESseuB1nFmhhbOF5Kt73uznB7uTcwm1aQgtxVURegjkXoGY1fItBK66HbidkiGbFOWXs78I4Z4Zs7qJm-IWGf5qRYXcjeyc7wRB9aEoo5B5Fl2gmrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8Qjt8G7j4FhCFW9a1jB1FwWPZbYPNHoyrt-i1PXvxMc-tuKpFE-xla-HetlSze233MgYhp_J5rJQUCuECaxgmlCAr3pXCdTAy25OLjssvNfj6eBmSUvR1gGlmb2fhk7ODKFCli4K5PIt9aPUF0ZdSM_SI1brMlNC21cTeu0GhbX0PMR5xU4eh6UupXW4hP-SWUn3lM3d2LBqGvF5k_ygoMqRVyOznxZT5StQusz1YwCqjdcjGMU1bpWqXboAhnuSd4FuD6F2prs4X_hNNdEo6drfs6JQ64sVNOmlxQR_N349CWSkvwMCsx0FBAfgu1-nHhUCCDzhxJW_ye7SZgGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9_wVSYXfq9otR0Aq-wdyKY5hJxsnrov_oLGuOTu-3p-0WJl-DIrAISdpmBPnYdZfC_5LDh1l_e7iNigOJLyGYvmrlvuOznE8ESaLjxOpo6LMaI60qE_eMJSPfBD6h_0QevtxGk598n04h9T3IE6HeQMIXQE-5e3rv3gN2JuFCc1ujQEBipWu4RW2q6gw_UTA4mtvEpttJTaNavDt_Bi9Dv5PDfZ_afG2bo5f-qMUo4o8K8ScDSZf7Vjs3HxBwhRodt-cHGKzVIBHdiizOF9pPCF6ndkiiFoSs4oHdZRGdkLmwRr_Kxp9ttwMODyzyfLJuTNEKS6qYyJEPsawGvz2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1pvFa0--2HSMs0NcDMGWCDNAtOIeESKsaE42zfZwnwLaJciHRYX1RJEtDzFDKnuDmqTi5mADQVrz_i8Vyybm-bek_ymi9q6Gm72D5PTa5FrthKtVERnghoKOLhdtmR9XpF3wUQaKirdjI723ocyDTQv-9AFiL4hjr4YnvMxOR5d_wetwKuqipKuIzVg6wcS89iTB989lw3z55n16p99iNm1Hc5vOiv3Rwpi8lMdNdIDim8thWu8JGr9bxnwRNPdFhN_x-Qr_R5vzigcpWjxinW1rGAwgK3nZfteMZg260ihosPTDGdrA9pOh7dafnPQJYIOg85xqHaOVLJ1WsewRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ir51L8xHRlAb1J3Tp2viuWorIqjIj1Ox2Oftgg2OcUS91vWbqyDZdGLexPsXjdVhUfvr7P4oK4RseTh7q5JNwaZrxH4t5hAX0H10CXURE2bqAGk_dBWqOWwMGWXz7ae2u1urK3kv-sKY251AP3-r-3JNHQanzTCWBXoNyBarjTB25_qHOBm5fOHuPkDKwl5vw7jFsG7zXN0s-ix0FGzyazUJaUMwtLQusCN8AMhJTN7Gqdb9bQXMibscDoIcJcB0ajdNytHkm437aXrFikyrSEuFJ662QA5dqFjoBGDhob2dkHBMES134p6rRF7r0_nSTQ2jOvn2dy5Z88nup_mCRw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2O1hzukEI6iuk4stiRMVJp0OpP78aT82N-pevgDQ1saZJT-cZnPifpc0Z5TcgwZ2K5Oq9W_59wXOByTIIwX_HX4ew_l8tAnuMMOuYXXVXjJN4eG8-nV4NrGGGVnYrCxor9NBHg0wE2Ol3JthcrOCqrZY858L8padcIN0JrbaKRr_1P5pYYVl1CTckhKFeT84DO7mfp_mC8IUsOMt0ewNj59U-StI_HZXFBz17NkzexPQHRas3aItmBye7sZCQ9yReAYs8I8M3FHF_-IB7-EqneblSZIMsssrCs_4f6J1Zcc1JkPThq_RKt8xBj7lBQ76QIpGZFcigyrg2MwZeNMHg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kletx2GO22goSbguyq9sHT5N5mBPaQKwEHJhrAQgThrdDmoqcFm4RedYNl69zZvjdi5hBEl5D2Q0LSCE1GNHQ43crsWj4XiSyqGWZn7BoDPjvLBBzboVYNAuo4S71elomuPKmt5XvDz9aghcdbeuluLP3JXqdx6eqjqMP4L5mtfxDKB51tL5W8WMoes5gAFoghsYzVsmvM__SUGbKK60rAXSkaKDcvS7ONmXUGygxXEaz4ZfyeYzy5o_JVRdQGFO1DF1tTOrPVkoCOvbjDdtqTeiL3AT44UmrEdObjnG1x9bh9IH3k5EtvNMspj5ofcoSR8DOXAgTfstFM16Bp9gOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmk1Co-16RvXdVmx0FwWm6cMqXCAeQ0yJbcuufuMQBvOcumyCzfbjbjRPQJq690jx0axlXr82UVOrnik33ID00_qhZtMnmIesytyYcDqkjSAZQaqSuI3Lsu_SubJmY930AhtOo9uLAt0MpinsTO1TWisUwU_8RJe6d46A-hT586n_fWIYg7ySTdgCdzBjKwgrh_QuQonkNZHES7ktiDXGvf2BLpIkhlcQp95KKATJtIvuexEegr6zRZjHLkphNXl0t6WWMbYLxuMIUYrH5qWzHysFHrFncGn5balqqlxs6jr_WwEwcF7u7nDcn3He0VpsDBIbwQLaF3r9eYZtwcnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbD_fmIDyKZBIj_zmj4KKZFCpa0fsyIn_K7WqWlGis7_PG74Zvnot5sUsILwkzqAa9POnBUsF6mZPVUvO49rf5kPBvEs1wqIReWWL1lVGwwOEvmyQfEU-3JJEtxGG5diIENREzahZ0hUZJgALhgDcq2pl-TTc2_wKSxB4KiVko0IHLajq3H5U-_fJxGq9ZRvzUv1AdU8YaV5ey0yW8Wn8Frsspyjmwwr-3xSH0EC4G_rArFgRf-_dd2KmvXXwxIieAbRPg3vbs0erMvJkuAXm79pRHQxV81EFOqbx2Vq2NGrNE3usPv0pvCspzVOA2XWD6H1MxVPFboU2b4CKEH5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3D9Djbiq9CJPyqpAY2uzaaA_Z2ZvdnOj8HaipJ_1Uzc_A7OKLL1fSFiSJL3nl-IefpC48TJaDSEzej2TNTNrV4a7E9j-NyUkLKrQZYDvBiurOcUHiAmam_N3vLTv2uEVeeg2bEUje6eXGng1eTjc2mlHu9DemesEJSeLLAI_MVKl1ejGGijPmUfrSA5w0yzxglUu6j02KvGBqLuieutWzM_eWqu6f7E0SCns_mqWdwX1IJoOXS3ISQahP6eAFiLtB09lMUs5QUXHsKiGtq6F255HZWWf9cPmI-dolGOAX9gKhuz0nfKrhWgJ1QFBjP1u8tAB5lzCaCsMflEt4kx7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYGwJ3UbiPttsP8DFVWl7_AcJtIJMNmtebQxkZ7enUyQHlWqQjKQ2h79fiHc1-SqEExePLIiJyrzR3X6Njm-JzYJSTENiFtSsY-FpfgFBp1MCZ0b7r49oUxw9tD4nfbQzF9ZKi2pB2CgEJd6qLpFODqS0sVG1Whxgo8H2h06Xyw7V1fsIMs3KWl8YJnQRSDEoJjwg3Accf4YS49hMSEXYgag9NVCy662QVSM8tIQCZeukKdIE8auBWSvIFcJKdefkNz08nrgQwELVctx9T8_OSq5bo96I5sUU4YoaSrCgAIXlPzmFV9Hcdw6_dniI0Wi6SCDUthOfsPk7-C2mme9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X7z_5clGQt2sBXDByo2gWgC76pIjhIOLfOTu6hUwSGzpSKC6d9GpEkVqROVpCrn2gnX-9v0scJgl2ICQeCXozd_A79fGhTSN_E7RYZpH4wnjL4QgnaGGgr71T1X4OnZWdJ0SfJaqa2dbeXk-vpFjmno_JyIeNtYpPK6ZmZ-Kz8B1juYLwY4XppL0BKB0wWbmKo1x6WPUCwd8JMoObw3wqV3VPCNeF4hUgHlAY6G7I_pIlzTqLEu55UZLCROuJy18n73wGKCzBbNn6h3WpSYgukgJI0t1bAcC30GBBwTUCnZfR6vDik8W6wKBkzaTSEjjyVLPCkGnkWQj_Z_bX6-fXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzmRHlGR41cze_vgdP-q38CPB3x04IIqojEFArZBRxJ8grrY3wDSTnitVYfXmuaTEf4_BBsCNjnBZye4V-SQ80xdPUeXe35bO3FqzL22MHBVl2_aqKx5B97tLRgZg-BFNbsGi2j5ghrjO6QIymiyryhTxwF2dzHvbbL_lrDONhYSkt5Sdl2O3bb8gK_H3YLR97K0uOJfZTq5zesSciEhGO92cGqv0N2-VvZWtgYfi9KBZXQtbuaJA7RPK8Y8tQ_Vg05KfpmWwM113EvaY1LlqSY-obc9FsyhJD9E28ofVl7hutFWsjebntQL6twCmQyA-JeZZ5gru0ocM5XLu4ECVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6vT9enCAnlomt9IMRXMc2km4L-Sqj8cx1RffhQsKd_4igrH2uz2rLe-cd8l-GAVSI_hnXuSh94hkIgyCQJf4A4eLkY40VzWvDb6pfqjuctMuryfOaPjNrd0SBTj0Bph51QBP3qJdvd1iYQTbjHzCNlW3AqrHkohMr5zDE7PSGgshyN0kowjWbS700i_-0vxy1KlAvgjhKl7XI1zDpEvNaalKrdJckfHZa56YpIBMVX-r8veDVPSeQwCMe3savA_dSnS4XJ-kMfCyEjsejLWM-LG1II4i-Z7dyHx4v14atvKIREgGIC1BeQHPA4iGdKcv2k040VNX1QcordaNVPYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEhN_IIe5DTdi4elSeq2MfIpsoMAt8nXpV4OrbQSDeVsVnADM7V7x5OlHonJOwzaSFlVMAMXrqEig0udr3vQF_hpJ9LIKLFbdTIx05BAkqBMpdNS0uqd0S5kZhf_PLFQ_pnW3CU5ezqi_AHhXgxfD0_sInFHx91tbAFPvHySCgwV7PSq2qUeHVpeQyW3FPgPcu0No7xuwJiaX-gU2IR-skgNSN6KTSkByE0azlidf2OpoYwBuGRfy3NxzITZBI2HBXmZbr2qOfrL9JMIR1NmJJ-11TVP-oYgAXnyLqxhz1Z89sKewlncug51YHho2RoRq6bMtkLUbTsgusdQDZHH0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkMGZFKclMXw0k2jlWjeZdzMD7TMVmnK6QyBuKIX6uL6FEgusv90lbkFGpCmHt2ip9w_Vp-VgM4SyHPLJztrQSFuxdiJbklA4BxGSe2d-N00KyyreUp8WjC3RTstbBHMCaOYeUWsEJWokkcaKu8Z88eHlVWVQg79SXsT3tWXZNm-YTBROtc4Cf6l6JvqHpE46LIbCTH6IX-8llvkPgDSqoOFm_Y5zPGy2sa_DuekVycXyFi6SCA5N6vyitsBg-MWUIOMw1e1eJ-wd7d4N2V5bQHMS0dlfVlntlR5JI_pesX4w5n3w-_XgbR_yVN59DnSQ-PDVVeP7mR-oQE3Ep5acw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6EpIIlVU0ciwKJijv-wA3of2Na5TZbj4uZaYoSDups-nUX3DwcMlgI-DkA4eQpl5FJ1clwOEFefXqPuZVjIYINVOck1OkFWYvbdTrWt_6k15MCK9UpE8tNPNo1jrkvLSSGdXpQfZEvwv5PJySXgrpzEVQtsQj7jtqajqXCEadsfJ8IkL-m3UXQJCIdExRPnCiqlG2zmgKxRmh6zj6LHt_68L0noJ9QJP3vO_jN6-uLHolKfd3g4a0bkVI7rOWBSRCPtU0zeGmZ-lc65V5tj9bKNndEcXnvryVSnv9PB_JDfvvd1BKK9tPxSAPzKjvj-WTax-_tM0jJCbwAfAkypEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZFHEpAcBFuVnImKHCQUwo_1ByYJHGIoHLppeKZj3h7-X4EYlRhWbtTzHJtFEz9Q6Jh5x0z8__DuNIMT5MdIl8XBVyjkRtii-j3vqXGHnciqA-7czXB3wroGeQUTFWPhc0UwNRA5fvWHs50Tbnggsje6A9tzDvYtzcsZTXwSXyq_UBp9GXENCOpIJQLTJHhk1vUoC5eLWQzI2u8nBThj7mumKQqnaGTVhQ6B7PF7cH67rKXd_ryg0u0go3t22xFD1wanp9M-gRf1wL46-fweEKvIELV4f4erNECX-xN_9GGpan8FoO1bxQEr_f8u8Mxbql73aIZTuddA56di9InssTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4HZlmaVpRiqPtL_HJOixAGSLvFVwM78KFOz5AmCtyrtTRG3bX_jVqth6DcjxyEuOsC8qSNdvZlafY7z1PJl3c3T6s9mI3g-JDRSisV_BgUvB7zXKqO39y8p8hCaVg0FunNxMDim8IOnANL_azSiVIjr-XHpMkxo43Ixyqx2cFNuZ57twOLrh0Ocft-Z3nDsGfyoqRw8RSpAkwPQuO9Kw5tgGpvtDaXxR4DgwtynEVr046Fpmah-x2VfZ7JdOEJq3Cnzumu-r-zsh0BQfJeiYofaefYTf_ShU0zQPphSGRR98Wap5D79HzFfXyLP3pqHEDtdNs7ESjzYkqwqnFEwUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9nNBDdH-9MSNQNNRrTkF2d1PkkmdFo4zFDOuxYg-Xk00CS6mF6Z6zsav6iJyxNR0LZq3-YqVx2lDJTl0w8KFbrsAUws-AGHII3D9UcJ1Q8COwIk_5beoXXnvMg3gnDwxsxlpEOWIkZlOxdCcJ2CXURFPjR5wlY0o2mm_BYBjmHp7oZiGT2FfiQ0KGUNyeXvGY9wLs_xln4ClGEbkeDvCNihMejRkIOOOVxnE4vBwY--ROgTcTX_sLeOsaBqebdOvUP4RwpT3P5vJOwSu3wGUS9Urec3BYqMWcYtDw2isqvkkWPgIFUVl2EwUa-FmFOVBAy_M6gFWoUspjEiwo2wzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SK3UeCTOPH35GvDbiRJuWFjuzG8cJx2nkHojxiAGo-6awCSoWr74NYJI17ghEIBKI7EWyJdGnOO-UGkw4Ysb-cwhdeKeRtneO_f5KhTZVP4kEZZdhtSayiI1V_OWpyWttM36aVcQoaueJ_lzUdNPvKKb_wuuSi2SaqBcDsnkOTZLF1ul0fNlqXeyifpqKQruAQKwKJRfKO1xdFO7NuyPca_zUlIPHbfBQiVDDFUSakx73_Qbgv6HSTRdCUMFcerPX_w6CRpXaaoeoHbJHkvEyhAYi-5QG--OkhGleo46RoAuk71PNFmBtANEQGNyScpIecOg2qZv82C8ar3de6YaKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25381">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv4aPMOkRJ7kxiq2xP-gs6o64bIf5k9iR07ON9EUgZFWNP19FZa5rY161N1s-b7YyVtXB2Wr-7lzck3hDDYm9XE-Zg6dMuJyZuxAqP5pfQeCkvFZvmQGbIIaL4MHd27JD2ZuWIT07ACygVt8443qM4B6G44ZJPbv61y1XBK7i8avkLtt1NgiU7h4S3bABIl7Kgxl3DaP_QcCdy2cqHMbS5dKUT3qK7tRf3bbGFZQD_Glgsg6SW4GCsdykzmDKG8vWgJa50JEwNFKqJhybZinMqVNjWBFHsD0DE7WomVXTaXKe842P1B0uSIQBKZcO4zIHnYFyvWUwKGCTrr9_aZUhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25381" target="_blank">📅 20:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25379">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUiNpsfChjVYFQMN4OuAFvrZvm0_7pp1fZIRTl4f0uY9GvPFrLSEfoOKbIyn6O3zdAaaN2yXSU_PQtNLBrW2LvD3Vxqs-RMH1XzU9onm0IVeC8GP2vqY1cosKURzPuK-s6zb5axgzdnM4jlM89z7d8FDE9z09ARo5pXzQZSFOHyYkwyU8ytfBfOoMACEvgvv6W3pMg0dIjJ_rrvCFfLFnl-HcSllSXpq1f7bkLDfFg7mzx5efFtvhlPUiIQbENiBJaRh1--nc02E_Y7TuVoYmn_TAzT9SLJcO-pd-VX0th6foLIwi-7VsHyv6GuKad6PDHGqZBXUj4Eh8ZBGittlPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25379" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25378">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN8gr2UaJ0mMuIxNK5YsmtTrHiwSPZXCiK7TfKHNhVzqBT3tllqsAHZnyMpUhfZmaw6btLbvs4IbXMWhS3Mniyc2QWzhEZyJZjfum9Rk380fiZ6sajMZLdZaupkCAGt3Me4Ini2q1IMxF5WkmaGvARqZcrKiE5EZkSk09goi_JE_fQ7oDtIP6EmqmAdNy4GOn6E7FfsnM6eRLRU1C40gNqd8wVmS-Z8YVQWeyzlDhs_8Yhm8XwkMyLqET3wnuVVvr66xVLPD10UCHBpDEc5QyUVHKlq5HcYDU0II2S48bFx_Kd7d6SbvlTK56_u16z-jRW98GgXSyPtmxIl0rSBaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25378" target="_blank">📅 20:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25376">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9Dz2SRngPy0qDP4hxJgHSJsJ-P0Z6PuHnbbRcaG0XU2asfZI3UvNbBwzWj4I3-2ugQt28dxJqJjnGiMRZMBrLNZH23FC9MGDNlTixig2PMW0txnzwKiKIrmHyuoa17y7ovpdEMpCXy9Bd1qt-PpvdqzsFK_sjg09uvwOEFcvQT-703oPA21xHvgJeh_D4tgwO1ci2mT7A9tLirFUUMEtO-M6MLKhS5m4GD_tb6Kjncw5JmQer_yYsULGL5jf5Kz9wQ4qYVm8RAk-loL59BPe8FrUGlIrZBCJJQ0J7BbWDRDBCkuCfDn_eOtf1Y9HWipR8ouN-uPeGH4aiGYTG3WjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتوجه‌به‌صحبت‌های ایجنت حسین نژاد؛ با اینکه مبلغ بندفسخ قرارداد این‌بازیکن 8 میلیون دلار ثبت شده اما باتوجه‌به‌اینکه تنها یک فصل از قرارداد حسین نژاد باقی مونده به احتمال فراوان با دریافت سه‌میلیون دلار رضایت نامه‌اش صادرخواهدشد. سه میلیون دلار میشه چیزی…</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25376" target="_blank">📅 20:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25375">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITWeVF7uIsCbCWJvv35OvCXiU9FlZnhzUaCfJ3DZU_fpwYLU_WL0iOxcCAaMAXUzZN_sVtBwXKZAWn9CRgM26H4hk_ElV1iP5sXSLpcMctDK16HGx2NZBUWvDqsfKa5N-moyD4Cs8FcKbUUS9d6AU4xO89TyHN7Yu5MdQXy8QIMOSfc_mfw-sI7dXlYqywf5QX8Y0J_Artr-glnzoA1lYOXQGZOBicsS1gVFsvbzcUyB_NKGguvHEvBQrSqaCHXtzmwt8fgRCX2e89AHvKw40Ci6Z7m4TwnueySBIsU17ZRAk5pBXHoGh4m9QSic1NqBpEXicSoTD6iWExVLWVsXmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
🇩🇪
#فوری؛ سران بارسا برسر انتقال کریم آدیمی به جمع شاگردان هانسی فلیک با سران بورسیا دورتموند به توافق کامل و نهایی رسیده و به زودی از خرید جدید خود رونمایی خواهد کرد. جذب آدیمی ربطی به پرونده جذب الوارز آرژانتینی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25375" target="_blank">📅 19:50 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
