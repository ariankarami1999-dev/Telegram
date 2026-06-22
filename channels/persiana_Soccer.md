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
<img src="https://cdn4.telesco.pe/file/n1pOccFqBAwEGxZOe1vG5LSZqG0ZazPMcnoiVpVD3Hw9rvDfnWeDOd06NgkD56J7bxtL1XDgMPYTX6xtPNH7CfBaGjbP3AHcbwMwdptlA79GIzwWpL5v5s3HT-_0Eo1b-bjy6O7FuwMYrtmxLLmg8pRMGhunVLBqLh160IEnCbwQt06Jw8VAiRI2CXD06w1FK4ry4Sddl7xZJWgldZjlewVZFHD1azdOl05s2Yl3QUedUE4vhnTpIRET7lo-y-qCIKPSazZPSaxdkX_Na2QDeLisPVb7hiAv-TtmgLBpYKIXY66PmcWoVN3AGOUumTDp6l-Yqyfbzk18Ihl3Wgmp1w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 312K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 21:30:16</div>
<hr>

<div class="tg-post" id="msg-24076">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSMJ6tkQNswtaWQLRCBoftzfoaNQkLON2GQRqP9f1hBiQCr6Z_SWW4byQqrO1wzEfYNZlvCEoyC_4lKK39tSXSP1BD7q3KT-nk4TxnAQAiiabg-d8SlKL0meXzvByg4vV7XWrHr1m8_utKB_5PqUQSF6XaixerAaCjLjXDLJzWfcppSWroSGNWXWk5Djl13x0DCPdXkuMTMJYwrfRZ7DJl_dLPA1hvXz9th07AEXPDqZlXWEV4gPr413QPRn3UuMsWMYRWevoIWTHmqU9nk-NCz7_TCAKBvrfgUKSkKxNHF2bPWwc5zWx7YRt-wbgl3LQT64FCJtXHHtERn45b1zyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل‌دیدنی لئو مسی به اتریش با طعم رکورد شکنی؛ با گلزنی در بازی امشب آرژانتین مقابل اتریش تعداد گل‌های لیونل مسی درتاریخ جام جهانی به عدد 17 رسید و بالاتر از میروسلاو کلوزه آلمانی در صدر برترین گلزنان تاریخ رقابت‌های جام جهانی ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/persiana_Soccer/24076" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24075">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=o0CXKqe48OUGRGt26fVnbZ9S-i3tnT1edYguoJnxpX6-aUuKK4NhtZd8uZl2x-RbR6Yiwd1s4Tack85J1OX1SngBODOTzZnReQiZXWvLl_MSnLIXKNWqL2A1k0s_DW2c7X9VbCKdAJ0Sbn38bGO-myaF5qb6wv7ooX1hkHoTohjjDX6ByW5H6a7hE6j_EjhwNgf1dhLw82DfJeWLrz2qloePor9UZ0xT_XNVsK6X2cyt_luqXkM0jI6uleJNKoFP0D3QTkYwW6EfAwgY2rO42fLVj8BqrpuBpAyyVx23G0rg0k_wscp27SoimKZZTncaHmORSErBN9ugemOUUCfeGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f39b8ab1.mp4?token=o0CXKqe48OUGRGt26fVnbZ9S-i3tnT1edYguoJnxpX6-aUuKK4NhtZd8uZl2x-RbR6Yiwd1s4Tack85J1OX1SngBODOTzZnReQiZXWvLl_MSnLIXKNWqL2A1k0s_DW2c7X9VbCKdAJ0Sbn38bGO-myaF5qb6wv7ooX1hkHoTohjjDX6ByW5H6a7hE6j_EjhwNgf1dhLw82DfJeWLrz2qloePor9UZ0xT_XNVsK6X2cyt_luqXkM0jI6uleJNKoFP0D3QTkYwW6EfAwgY2rO42fLVj8BqrpuBpAyyVx23G0rg0k_wscp27SoimKZZTncaHmORSErBN9ugemOUUCfeGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/persiana_Soccer/24075" target="_blank">📅 21:14 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24074">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b9463294.mp4?token=A29-TAcxA2QFLsAXg38LjxFiBBLPfPlwGhPpE9_QCu8yBSNHQJGA35NEbiQhdXdlP4Wf9gJrcuVazsKpQyAr5vS9l2fh0LRFmPk4udGQNRs5kHmvPE1DCmlFI9V6rxghQeHMq63h3JrGauoaqMPOwxFIaaujLLznll6vJvsF_qJhUWG77OfE7LfcOWTdDxRB7HnRHKPHxM4bjCimcURdSbhTf7m6-o29I4PlvrHh9wPmondXk2geOaG0MsGwLBvy3O7kMYLP4Im81qZR9XsesDeAxIXDbzWzyByJvkW38IqMyQNjkN4H2pA829qEFRwVABrRV9Qk0qEQac6GnOucAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b9463294.mp4?token=A29-TAcxA2QFLsAXg38LjxFiBBLPfPlwGhPpE9_QCu8yBSNHQJGA35NEbiQhdXdlP4Wf9gJrcuVazsKpQyAr5vS9l2fh0LRFmPk4udGQNRs5kHmvPE1DCmlFI9V6rxghQeHMq63h3JrGauoaqMPOwxFIaaujLLznll6vJvsF_qJhUWG77OfE7LfcOWTdDxRB7HnRHKPHxM4bjCimcURdSbhTf7m6-o29I4PlvrHh9wPmondXk2geOaG0MsGwLBvy3O7kMYLP4Im81qZR9XsesDeAxIXDbzWzyByJvkW38IqMyQNjkN4H2pA829qEFRwVABrRV9Qk0qEQac6GnOucAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تکرارخلق‌این‌صحنه‌تاریخی‌وشاهکار امین حیایی دراخراجی‌ها در بازی شب گذشته ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/persiana_Soccer/24074" target="_blank">📅 21:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24073">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkkdyNuHqCaXK2qEkh56DGrKT-Pmn53EWLBvm3BHrtpv-W0sfspfdnmnErqxjflafccC8u7oNWnDxRd_pJ0WgBkoDwPyVOW5k7jpG8OIG3-uuGyfwveuDmH6sbalmWDKcliLwV_dEtJBDuH5Xs_VvVu1JY4V8Yn2w_b_X64-6eNA57X6BYYQmytR9zaJjrAH0UvHLLdPWONikoIwwZU22FKMWvSTlV7MEdFGTMY8EnoQkKYkxnIb_cDSKveV930MucidUgAoyea5Qn0Rgtq5O72i5C1DktpxOXHsqsFziRQNu7LHmcDYLwrGs1flgG8b1MMfL5DG5LGPMvd0iMct2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی در دقیقه 9 بازی امشب با اتریش فرصت بثمررساندن هفدهمین گل خود در تاریخ جام جهانی رو از دست داد و پنالتی‌اش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/persiana_Soccer/24073" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24072">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دکتر انوشه مهمون برنامه جیمی جام اسم ابوطالب رو از قصد میگفت یونس یا چی؟
پامپ که برنامه جیمی جام رو ساخته، ترمز بریده و داره یک کیلو طلا بین مردم پخش میکنه،
هنوز سهم خودتو نگرفتی؟
این کد سهم: pump
اینم لینک :
👇
👇
👇
ثبت نام و دریافت طلا
دیگه خود دانی...
@pump_vod</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/persiana_Soccer/24072" target="_blank">📅 21:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24071">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=kqZwfysiDTXkmRB4k5us5hFvk1pD1gHQcVHoCIItpmP3LETkEPXbGcGAd73BUPBGuXtB9LxSVmao6z4ppMskQRnQWCSxMvmTAQy257cWVxypAal_H8r774iuzOvRZocvkOQn6yw0ubccMrYBWb6pZBUw-VM8K_TgeeC2A98nnaa9KKqJj2VC-07ZXTN9eqAiK_K4Hm_KVULs-no0EArmEIGWpzeckkJs9TCYIG0LGA7ZuvGOlWNSr-a4xNNcJ_kspIEv_tu5fTaiF9wDQ4L9dbmuNCzoaxCxWvb9kALzDEn5l39dSOoATBTlESN8xgY9Hjk4XMpfR2EQXTvKiqo4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275cd8fdaf.mp4?token=kqZwfysiDTXkmRB4k5us5hFvk1pD1gHQcVHoCIItpmP3LETkEPXbGcGAd73BUPBGuXtB9LxSVmao6z4ppMskQRnQWCSxMvmTAQy257cWVxypAal_H8r774iuzOvRZocvkOQn6yw0ubccMrYBWb6pZBUw-VM8K_TgeeC2A98nnaa9KKqJj2VC-07ZXTN9eqAiK_K4Hm_KVULs-no0EArmEIGWpzeckkJs9TCYIG0LGA7ZuvGOlWNSr-a4xNNcJ_kspIEv_tu5fTaiF9wDQ4L9dbmuNCzoaxCxWvb9kALzDEn5l39dSOoATBTlESN8xgY9Hjk4XMpfR2EQXTvKiqo4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
لیونل مسی امشب دربازی بااتریش میتونه دوتا رکورد رومال‌خودش‌کنه. یه پاس گل بده تا تبدیل به بهترین پاسور تاریخ‌جام‌جهانی بشه. یه گل بزنه تا به تنهایی تبدیل به آقای‌گل تاریخ جام جهانی بشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/24071" target="_blank">📅 20:43 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24070">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpzSVfl2d8GdCqIbhwIdy0cC2cYqDOjfS0hElIbjL9UeVVydotgpK8Y6zYW0U323r2Xud_SoObxB5Od9qQMiheuNHYiu7ZYpVZfTtpuIkEPKXYqTAEH9t9dwbIV9lI5DZHwMhCJPXWglbUMFauP9TtwGi9GAwj68CXaK3PeG7uUDfykW8FBjmx46dnyApyfi9T68xeavIVljf1t2gfhlhuIGpXFs-R6OR805fqyDuREKCarNV16q7DzHJE00v1cpmjXzCE-lNxKjngvt7F-RtB9jJgNuLqBjCVsYuqRaDSHRGN3VAQ8j5kkpM9tAyRtA2pz7hqTmeeN3tU1_kEK0HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
اولین گل مسی تو جام جهانی: 18 سال و 11 ماه
🤩
اولین گل یامال تو جام جهانی: 18 سال و 11 ماه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/24070" target="_blank">📅 20:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24069">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=PTi47VaF7XwtnXROmoFrsR06xC-hS9sEbbKxFmg3lHPGbJNxElWiKKlg-Vqv_XVmwwhYP98gkksxFkHyPZKVwxHvnzf798N6CGJZRopWPwsTD5BAIRGP3ZZKeRWi0gUQwOJXziLETGYkbZbYbmnRZ_0SvQqYGcC97grWJoV6bvIQkXF0njcC4PCrn5j8D0g5G4nmHidXIYNeLG1-GQRABod6SKuVswHUQO6caOZsBMqA5dhkIxlIWZS8rPG7y6Mb6oR5sGKUw9jCqjLg_mWKPdAN-ztjMBKzK4nX8gCO9bWmqfSIlrdaEcayNXMnvu5NUyy0uAfE2WP9acif_6y6Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436443b2d6.mp4?token=PTi47VaF7XwtnXROmoFrsR06xC-hS9sEbbKxFmg3lHPGbJNxElWiKKlg-Vqv_XVmwwhYP98gkksxFkHyPZKVwxHvnzf798N6CGJZRopWPwsTD5BAIRGP3ZZKeRWi0gUQwOJXziLETGYkbZbYbmnRZ_0SvQqYGcC97grWJoV6bvIQkXF0njcC4PCrn5j8D0g5G4nmHidXIYNeLG1-GQRABod6SKuVswHUQO6caOZsBMqA5dhkIxlIWZS8rPG7y6Mb6oR5sGKUw9jCqjLg_mWKPdAN-ztjMBKzK4nX8gCO9bWmqfSIlrdaEcayNXMnvu5NUyy0uAfE2WP9acif_6y6Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/24069" target="_blank">📅 19:45 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24068">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tq-Rn3yrlgCF4L59MKIk7NV4gYmpyjKxEmIT-Q-rr9YcH3LrjMEDzARiy0ZMZ7bFtNh5JNiUicweAOewcT-FifCg-_6fHli-tyUlT3A3pPV4eSqMu2S6yHzwSqkqcMMo1N0CZ8dpeW7sEYU50XoiIRfDBCLBhYv8CF_oE7jPr-OA9yO5X8W6ds_A4uzNVmuPNNTGY2UZ1kGf0ARczimm07l7gF_SOSIpdqMf_B7oSfHm9B_hNRTSIckeJUwGF7cWkpMhzfq2Woi9IaPd3fdzQJY3VeZwUGdJRSDxtNj3eYTALE-T6CcRWa-QRWK4HK2uXNOKH8Gofo1u-0a15X3_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛
شماتیک ترکیب آرژانتین برای دیدار مقابل اتریش؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/persiana_Soccer/24068" target="_blank">📅 18:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24067">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDxhA-0omTUZ4n8tjRwOYAIFEGmylBOmz4VuyZSeHIEhRFRvdGCHpfdD3jXFfaHaJ6fAXlKn8ZuIlb62zhwfxugKI0f1_fsfH_9hJ2PXgRszda8qt-R36OxzsI--hrdcQcz10t16clKWcJ1XWJWKkx0BIuubj_LZ1V1QA15FDW6L96P39DzeNrCSVm9sIXExu6Hz0aU_OQBOhj0QycvhZd_ILw-2e15nayt-Z-L-uJGkVNz3WCtXx3MZ0ox5IgCeUcbZoN00gKDsa_-Vub-xxKJ_wUVVDi-RC2IaBHIxuiHAhuVeBntVu-F8B3U_J9Etz2Lw03C0xU2xq9uSIJiM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/24067" target="_blank">📅 18:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24066">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚽️
خلاصه‌بازی اکوادور - کوراسائو ببینید لذت ببرید ازنمایش گلرهای دو تیم؛ بازی‌ای اگه قراره صفر صفر هم بشه اینجوری‌بشه‌قطعا به دل تماشاچی میشینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/24066" target="_blank">📅 17:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24065">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa115feff.mp4?token=jJq-_SRkXKdnwvk7HZS-E4qpSfPfwDr_7YX-_mh69RZ_rJjJ0ekZZcu9sGuKOw25gzraNtXzZ2P6NgSwd_2Od0MZb8AW-bHKzx0HbL0LR4BdxkQGa7JxidBevsfu5WjpepIHPCsH-2OLLSxlYO4_lF3bMggdu6s9mY01Y26uHKh4f-FVyj0HuD_f6fHRJbAhMNwNYOnOhF9MxHMXkYe2Oe90FVFxJOEdbYhNEXqUieUsvrDtT6IddcDcVSkGQPlFn7c4Kr6U0XxxkG7w-0rq2oVgai8ZBPEYOka3wIZ_yvsXsYkDhJsiKJ7pnDAXdQt4RbkXJQiMDHZQF4K03O_j0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa115feff.mp4?token=jJq-_SRkXKdnwvk7HZS-E4qpSfPfwDr_7YX-_mh69RZ_rJjJ0ekZZcu9sGuKOw25gzraNtXzZ2P6NgSwd_2Od0MZb8AW-bHKzx0HbL0LR4BdxkQGa7JxidBevsfu5WjpepIHPCsH-2OLLSxlYO4_lF3bMggdu6s9mY01Y26uHKh4f-FVyj0HuD_f6fHRJbAhMNwNYOnOhF9MxHMXkYe2Oe90FVFxJOEdbYhNEXqUieUsvrDtT6IddcDcVSkGQPlFn7c4Kr6U0XxxkG7w-0rq2oVgai8ZBPEYOka3wIZ_yvsXsYkDhJsiKJ7pnDAXdQt4RbkXJQiMDHZQF4K03O_j0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/24065" target="_blank">📅 17:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24064">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaSXMXMtcj5hITMdzvm24Al2L5II1D-ojrqrg-CevX4mePoOsj5IHtgZDaORgtCQe-0Q15WSeIMtQIakCCbudLbJu5AHmaz9lB4sEj2Y_kev17YftHB7TwWMASEYi9kDyP_-GEjwqTPyG15MX5p7kq4SqDtlZJ8rQGBWNmNcSrliIimjmdFMPqYuvR5JoQXICH4cb5dipp2fadbuk_ECCI2fQwlCkTXyCi29-WIhUEEIGM3k4U6A2rGJhpGcgzySSTJynkyfYl5j1CHoZDbR3kAGGO8M_ioO7eE8dl1nnQRjX6afosIRWf07wi9pKjWdAqtyKsXThMyTS1kj-rCjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/24064" target="_blank">📅 17:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24063">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZns7ESvqyNCmyp2EBWO3-NKo84H_riopFPAc359jEQg_mCfQPGiRQ5aTEgWsJNGzj7JTDUVhb3UBInOoqmSSGXP3_X2-z9sGJl7TZ_ABt_rnxwleYy1e2U2hctpM6cbmt2hUkikX4O6FMfthcz9k7dQ62TNH517rnZPaXCQj8kVYcDPHgODG_ImSP1i7A7bX1Vd08XzeoDiC3l5xRwZxfkX-CZ7TGoIV15SGkiwsZ2At_KRDi8JZB3DChY-PP7z4R3Fw-1Oq4zcXDt1Na-jQiPCbcLpPs3AK0U4SvQqq7JbNQwtJfgrLnXz1vvbc9rziOYkxzZCxcOWb9F7VunzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
10 گلزن‌‌برتر‌تاریخ‌رقابت‌های‌ جام‌ جهانی؛ لیونل مسی به رکورد تاریخی اسطوره ژرمن‌ها رسید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/24063" target="_blank">📅 17:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24062">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqwVXMmIxzUXbrlksQ7BFEDp5y4Okg048UVw9X8mdYOK96R-gQviBcpeIDb-tzxYkC7N35TLxC4tYctemtazW7tyV-wWHkYwv3iEGryhIxdyP47X1d98rrmmSeM7AmSyKlR6e_zXReIbKFhOqWlvDB6Cn8uhx1qxKiK1BGfiIuzgenzwDrroMHFrEGiixDWM8H9LgFTv4jSD-zWqf35Dgec7cVrdOPMqY_uiKWkGK95o4Do1hfZqpM_jgYDM-uQ6i7XLsobX_IKx0XvP0JTRRcOSIi5PRd6Aa0uLyKcS67X2X346by_EvR0ifQCHT0NEm7bpOQuxdYMAhqqpBLkgRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی وینگرآلبانیایی‌استقلال با انتشار این استوری‌خبراز موندنش‌دراستقلال رو داد. مشکل پرداخت مطالبات این بازیکن برطرف شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/24062" target="_blank">📅 16:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24061">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f988706b3.mp4?token=YKI2sKuBRJpKiZB9TB6uWx_m9nnlmKQU9V55CXwkOR5etHL2oDM39mvXT03ZSb4W419way8D6ceQCEB8-YS_T0oQqjSEM6E4n4pVWJlBerQ11LwC1seXg9UZgUoVppk-5yGsfPMrO6ILG3JSRXfxEAKiy1v0St0WNny2qv1LpB8FiH4EmPDVcaamSfI8FGIyp69pyFs0jhxNbWzKbJTMNIvWfblpW5V7X0Lh4DuAL3riYl1K21vdc1nQ_FjXgy-mcH2xsVSUP0FGp-AOdm4X-LuArRxqYzPHAZT8FMhjgUBLruhIXGwC_0GZ_ECkIiHXiW-B5A5flwZhRHsVvKP_LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f988706b3.mp4?token=YKI2sKuBRJpKiZB9TB6uWx_m9nnlmKQU9V55CXwkOR5etHL2oDM39mvXT03ZSb4W419way8D6ceQCEB8-YS_T0oQqjSEM6E4n4pVWJlBerQ11LwC1seXg9UZgUoVppk-5yGsfPMrO6ILG3JSRXfxEAKiy1v0St0WNny2qv1LpB8FiH4EmPDVcaamSfI8FGIyp69pyFs0jhxNbWzKbJTMNIvWfblpW5V7X0Lh4DuAL3riYl1K21vdc1nQ_FjXgy-mcH2xsVSUP0FGp-AOdm4X-LuArRxqYzPHAZT8FMhjgUBLruhIXGwC_0GZ_ECkIiHXiW-B5A5flwZhRHsVvKP_LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای هفته‌دوم و سوم تیم ملی والیبال ایران در لیگ ملت‌های والیبال؛ هفته اول تموم شد که یک برد و سه باخت برای شاگردان پیاتزا حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/24061" target="_blank">📅 16:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24060">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCgb-k24sYBmYjXrCPnDnumGTaNbysBQmP-c_bDTEmlooLXbb2TcYZs3zcrARY6nht0Lmd9G7KiTI_9N_dCBScC91UMQyMg41gBQ7syk-KfZs2PZ-4aNYPMuNhQU5lbijtFSgf3SDKtRQmO7m30yncBl_ugpPblkD3SLJDjxyG_fje1baN8CvR79xG0rUw7RWdkPeT5TNrr-0HAPohd_a0Mobm89YhFIijaebVOp6Ag-XNOc84kGsQq_dWc3MQ75OxYY2HLNBhB_SiyEeZBBd8cDR_U4Dqaj-7uDC639CFw5OwI6RZad3qsrQUnZcNroT0oYUAKVWKFtdht0DddIrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24060" target="_blank">📅 16:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24059">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3R0D4P17fMCICnQPCBfhDmQhEidQp_qX02FIsmgIblsahQLxpR6kqCOZiq1fjZA2CHWnpgstn0yJYKsWdfDbSG0EvbUxC6eQTcudgiHCcGcyHonFMKEupJah6EZHVS23B5V3lTyomibvf1E6UEtP_KgQKoVgBH0zHuW1_utSEPftqO5IvKOfKQUi1PyFpXsIocN4wzNHurgIErN4r9HJwO_OStgJHN8jtYakuDrwfbZWuIH1kfI1axRT52RMjxgg87b_pQPegh4fTWnc_XTPzVcMJRfQ62su4LtQN0fZy0f7BAhOEn5RutZPB5eh7DCiMVzaV2_D4Z9EBE3VNA2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/24059" target="_blank">📅 16:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24058">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiyRE1Z-pljjyVPh6WyFJ64bkfnJWomfFfRdEFA4OGopDOw_HpqsTDrV37_sIxTBlOUDvjtF3IRvKw39wJxV8S9zbs8MqmNTiqTbCFskm4Fqi6vVGkOg3rJEXEV1az-41H_G1x9oiTvk4LB3TjZbPJayuqQ4igfPU6_lcT1gzefhwuDMgCpjulO1SVfgp_yIGpeFzH1s2F6mKW8T2B1z6WCAME-sjY3LEkpo9wVRuQOs_Hy7gQHb94Mg9fBMOnhPJ5dBb_ksohu1GIYjcMZGcW6DxLvvHQo2FYfVV3AJp8y_vHf0DYBrgCNOSkKC4nRsmiyx2lNVxH7D7nV32pDV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تمام‌حالات‌ممکن برای صعود تیم ایران به مرحله حذفی جام‌جهانی؛ازتقابل باعربستان تا یاران امباپه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/24058" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24057">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALBkCWwskFeeYUAen-S1-TPLmzg6_aumPtAFocAp90W_yr5UyCtrMYgTf1n-iKDcH5qwCsh0H1tveTvvB3EZsw5bsCmcPZkXnLWsPzY0Kx1CKu8QmD7La_A_Spwui8dJRqYoZNQWRoiLZ3HQ2EDcwGdN7nPtE-RJigxl67xRM4aNRowgaRpWdL9xeyA6LhjyHHfd2ePMznDhqw8upklj9Sn_SP5kIwoX7DIi6_A172dZ3lY9A8ybP06SPqUBcnK2_CY3V8vqkauvwaBO_o4U6EVR68e1iOU0hO6e1wcTWPrlLpyMpY0dFmv-T8CRXq2JiW0f0MeQsduVR5Js5UPT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی درمورد عملکرد علیرضا بیرانوند در مقابل بلژیک: این سری خیلی تنگ بود خدایی
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/24057" target="_blank">📅 15:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24056">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2fba3c01e.mp4?token=SObbQ9xxr6jQ0z3QI03OwEElQv7odLnBD1BLemOfTUW5mNB9Mi2R56wh7C9913EuLvQM3wQGuBJFaTGB-3Mu43-hWEjBmqxUMnqNiSZBYebYT9i93NQGd7U8bTfqLtUvVl3tVgvwpr2qd0tUwBu6QXAkjDcwxxPOoqUCta3ss8iQaXiYZRclusgcDLaV9UX65qQUARyhUmCvW7vJAN14SZqWKlkZN9NPnpa1QZ1zRTunkRju2fV-lj-X6-YlIhoE8QwWP4pee1LirEc5bekQu1nIU210obG3BGYKVJuGiaHgD5zbb68zASEgtbWFqWDcmHkZjShzrE3Y5LEE0GRKlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2fba3c01e.mp4?token=SObbQ9xxr6jQ0z3QI03OwEElQv7odLnBD1BLemOfTUW5mNB9Mi2R56wh7C9913EuLvQM3wQGuBJFaTGB-3Mu43-hWEjBmqxUMnqNiSZBYebYT9i93NQGd7U8bTfqLtUvVl3tVgvwpr2qd0tUwBu6QXAkjDcwxxPOoqUCta3ss8iQaXiYZRclusgcDLaV9UX65qQUARyhUmCvW7vJAN14SZqWKlkZN9NPnpa1QZ1zRTunkRju2fV-lj-X6-YlIhoE8QwWP4pee1LirEc5bekQu1nIU210obG3BGYKVJuGiaHgD5zbb68zASEgtbWFqWDcmHkZjShzrE3Y5LEE0GRKlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد خیابانی چرا اینطوریه؟
واقعا دیگه خیلی عجیب شده، یه‌چیزی میزنه به حضرت عباس؛ لحظه آخر قیافه خداداد عزیزی خیلی خوب میشه
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24056" target="_blank">📅 15:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24055">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KC7ZcRlJaK-PxNIGGFugGqHaxDEEG4mk3PRWAtCI5ms1BZ91Jf5xtOQSBCP2kFpkt9o4N4uPSX9sxzAusfeG-aUWoJJXfy4vIDLijCwzJjKJq7pT0xvW4JMqUoLV_MCzJ-zIlo49n115mR4LbVQl5DdEtm15yKDM3bHIq5PLd4DYuzAEDHJL1OQHfadtxKFO_3RXx3gsBdzaNFBt162RmY2w86RDsBLAtimTxZkBRt0S7wXQxwP5p6nmPbZs1D249O8UhVDDfGsouucKMGcE88DlmwT7dcu-PpR0euyu1qA3SddRQjyXlMzEPQRgwi9fRpCr5hSVUJRbuAdfE3-uuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
#تکمیلی؛ علیرضا بیرانوند با 7 سیو و کسب نمره 9 ازهواسکورد و نمره10 از سوفااسکور بعنوان بهترین بازیکن دیدار بلژیک - ایران انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/24055" target="_blank">📅 15:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24054">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6565fae72d.mp4?token=T7i37vBdmXjDoc6jVKu9D64MifQLH-jtoFrFYf1HJdKR-gocjgn_Wptg_gTRRJCFE9t2XYHM6hGeUFQ5GaThPMQVAVZ9SokerF-MnGZPhnaU5wIyQ1THiHOqoOUW7exhR6EZDMeLJVR6FQ0J7Ip5Mfxpr9dGl5GiI_gb_DYatNZai4iJoSUMZWsRcamziLRYGRDkdt0C9WMsXGBSyxpJp2tZCO8VyEAj_nlG36PlOOsqwTYdiy0bH49mxUwQIZU1zRGYdnFGBC6gKQZruw3GndEEc6cO0LmzGauCPSqejUkmJvJptQ6xW6xEQ9JtOqG-py1PgKtCLFKQF4KrKiMMPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6565fae72d.mp4?token=T7i37vBdmXjDoc6jVKu9D64MifQLH-jtoFrFYf1HJdKR-gocjgn_Wptg_gTRRJCFE9t2XYHM6hGeUFQ5GaThPMQVAVZ9SokerF-MnGZPhnaU5wIyQ1THiHOqoOUW7exhR6EZDMeLJVR6FQ0J7Ip5Mfxpr9dGl5GiI_gb_DYatNZai4iJoSUMZWsRcamziLRYGRDkdt0C9WMsXGBSyxpJp2tZCO8VyEAj_nlG36PlOOsqwTYdiy0bH49mxUwQIZU1zRGYdnFGBC6gKQZruw3GndEEc6cO0LmzGauCPSqejUkmJvJptQ6xW6xEQ9JtOqG-py1PgKtCLFKQF4KrKiMMPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚪️
نمونه‌ ای از وضعیت متناقض جامعه ایرانی درحاشیه بازی شب گذشته دو تیم ایران
🆚
بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/24054" target="_blank">📅 15:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24053">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d16aWjPoQRmUWBJLky0pfGNE78av3J8wMk08KJiFSmLrZZ19s5QZZwgi6Dam8HLweH6gkikd45AyZHw17vNK_yvnQWLpUqlqHe628y_HD3NseVwHh9-YJk1WEKAHtHLCrMOtDiIhnhF_pm0QJ6iFHVRH6HWvrvjUMUymmiPQdfrGlXQo6Wc0ANhs3qwvpFyYAWh7OzrPRIZUEd3XURKtm5R6V3u8GPrCvGPDwMaUIuU778pAkOa0LSR3V9ygCbznFSvNHVDFb5YZrRq1sQ6QO13TVlgjvIVvfNM5bxCW0ERY54Cp4UkYzmmvUogJcvn2nMcBrxHJgsxNRa24pJWgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
استوری معنی‌دار اوسمار ویرا بعد از مذاکره باشگاه پرسپولیس به دراگان اسکوچیچ: خدا همیشه خیلی خوبه... متعهد بودن، حرفه‌ ای بودن، با دیگران مهربان بودن و قابل اعتماد بودن یک انتخاب نیست، اصول شخصیت انسان است. داره به مدیران باشگاه تیکه میندازه میگه وقتی با…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24053" target="_blank">📅 15:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24052">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaQCaYT22uW6wEiOjehp7nJzsqQZKNkpYHuUnpZ06U0amqRxX-OFCjxBsgCMmNKQPUh48-IvlfSCTp6sUbL1K_MqsQc63QddE0zMTxU-6MNvmx2m69oY1HWMsTuQc4XbjchAEa9dvFV6pW6A-gKOqUSbKPLkTGMICU4QCbzTmlEc0lbPvUUEUKz_FPe_5oW-Xzwu-YwtEBVknyvpQ5f7g6ALNaumDyqffKyicYUhmDeoNXzvQA5Q7KTLrcMxl66eAIVv0-zxUfDVSAUgmxQuCTMFHMYswG37u6R8YAfW06txrr91K8XQvReNY1skoxw3IASsZXvObgHg2SC02bEzDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24052" target="_blank">📅 14:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24051">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrsK6s5r7fnRajp4p0SLziPUUhddHL3sQqAwYlph9dQixLOeytmik4Sw3w64gnBsmVnNwKPaXTv_f_hlRP3G4Xs_1HuTH36SVbe10gjYWeF1ki0U37pxI8IextknawneFZNz-Rfy5mRtXyN2n2xIWPNPuwj6NI3X82WCTsWEjGPiL1tfOOQT4Q4-bi-LYE200cGUT9kj32v---hMqfp5uaV1PInmKPjS-Fieclr6fp_0a_uZO_26CMxNQTI9-uNkzbGOGKhE9zLhP94k6SkVTs-9UcXK4WEomf7MUTNa-wyRN8WHEi6bepfB7j71wnQkEhvdfYLtOVBywWFoXYMymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
در آرژانتین یک دین جدید به نام مسیسم متولد شده؛ این دین جدید که پس از قهرمانی آرژانتین در جام جهانی ۲۰۲۲ پدید آمده در روستای لا اسکوندیدا درایالت‌چاکو آرژانتین درحال‌گسترشه.درحال حاضر 3900 نفر در این روستا زندگی میکنند که مسی را مقدس می‌دانند و به آیین «مِسیسم» اعتقاد دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24051" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24050">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⚽️
از دخترانی که اطراف ورزشگاه‌ های جام‌ جهانی هستن سوال میکنن که جذابترین فوتبالیست کیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/24050" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24049">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM_EjY-ZQLKAGfWayghD7MlvH817yCuz35Yljy0BxJsAFk46Fyyaejuf-s7MWX2qb9VfkszrFrUhUIim1lcIDr-NnBYeU2NhWkd9hTaoGh8nU-MLzM9d2EOQaQd-m5dzbp4bnx9ci-eIWg2imeZHfb8BVMFp6dMwWqYKdjAM7k5r2vP22szg-Y7aAM6OakultQOb3pb8fjNzNmew49jJtngABbx5ovpgUqrM4frhZJHkSj8f_W36QKl7kl2W9AZDBOeWBdgv8zWludgUnn84aiVH2GRL4cV6X5-kZxMBDTDEIh-QnwlBeDXZWghgJJgc23yfPOft9ja5v8ZUDIK3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این‌پاداش‌پول‌نقده‌ولحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا er1
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24049" target="_blank">📅 14:09 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24048">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS4vfviphsew9QRCrE8hndzCpE8QJ0Tve9T43mtxQn8UOFsTlXyjzp6Jtk1v-j1P0Hd95NeX3vgfxTlntWu-MaZdNMA0ztXQqEAshO2Fq4KrOJMu0gZrPdRU5GVyoVSYP-Z8nxA3ZLM2hgNz7Hb6VkcFtH3RH7IGOyssAdNB8_fWWJvPp8iizE-F1m5jpkh9QjX0cuiue5E337Yvkb_hWDrJgBnO6LRkhUGEHxMrwFa3JeExUJ1yl9ZFctYqZvgarMxoBizdLb4WRNFtXUD0XybBwJNDTKa5im7FjzZ20Km0lcJWJDttFzu4PX_5MPc9q4NHDyouSHhB3DKeD-5c4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ علی تاجرنیا رئیس هیات مدیره استقلال ظهرامروز با محمدمحبی و ایجنتش جلسه آنلاین یک ساعته‌‌ای داشته و پیشنهاد مالی بالایی رو برای 3 فصل حضور درباشگاه استقلال به ستاره تیم ملی داده است. محبی ضمن تشکر از پیشنهاد آبی‌ها اعلام کرده اگه با تیم خوبی در…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24048" target="_blank">📅 13:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24047">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGI_flAFaFTD8iI3FC6ZUimOq4G2Pq5p57W8S0ePb24jSgvaoKmAI6jJqQP-F1cyu96LqbiGytcypdGkWFtlUNqHzgJL_9PrRnQWAMG4PuFCKT_icqcigUpIbsBSiYKAjYi7RzJXe141Y4T37kflxScn71c5dQYw-Z3Xylkd__jPrxF-YopozScGFnltyrWxxckExak4eiHlvlC1Mi5rhGQ_xTdxvgpr8sqWbNhIa8x2D9OFc0ctGFRGaclSSv5fd4KrCJBJwx-6JfHEy5VPJqsKSN2ksGmhnILBXy2MhqSVeTkzHfQoGULFGy4ihuYN5EpefTOQobRZol-6-l6AEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تعریف و تجمید بوفون از علی رضا بیرانوند:
قبل‌از این بازی هیچ‌شناختی ازش ندارم اما عملکرد درخشانش در بازی شب گذشته باعث شد که راجب او تحقیق کنم. انتظارداشتم او دریکی‌از باشگاه های اروپایی بازی میکرد. دیشب فوق العاده کار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24047" target="_blank">📅 12:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24046">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ej7LNxIfKHR-fSNXZXx7icM795bgXxq5h8C9fcz-m76fBTFYqWFKynEeNT1BfOQgO5yBH6m-efIpSbv1mM2iVJnZFQN8ofv4ox8Grl_TypjtH9b3JneFpdCmLy2IoBe9YQymJwRjZD94q_OoNC-XoqTtdy3pOXYeG_wnAgSZj19_XecZIL-uBXv0JLhZNVjvP_FjPtGH5RHJSd-xJZ08uDzu_98nHh7Z20ipp_jgaHKwJGfEJYNocL5SWzHAljT8aN0RLxmiqElz_3bGfzl85N1JfCarI5hFW9EYww_8FSAPu-UaJvIW6143-nbr4eMg1WhPyPLnoDYTRNTJRg6aRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24046" target="_blank">📅 12:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24045">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYgUBGISZRZJSveGdnwVNRYgUwronU6Qxj8J7_chjiMRRHmQ9d9GEZYQaBQfHbJvLXh4MsXDmbzw1w7dXx8TC9ofZrfZVMH8TUCsWZOvC0QV1jI15gPYOrcfE0VqlPEreeQG_m0x0Dz86nuZVmR5dfuGWOb3lebQ_IOIKGjHNGBY6TwdgxaBNBV3CiJ-SCnvDfI6rapYyxvtKICw1H_U5d5gGCQfgAkfTIiOKmDpPpmb6Hi_qFardV5ewEllVlUp7r1vkMSLGozkDhBN4mdQ2IZ2hiGLPgSZuTWHNNg3Dfvulg5WNn7hAcAzC-fPVllE6fUfZBFR_VHVTNhydwQciA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه پرسپولیس طی ساعات آینده مبلغ توافق شده رو به حساب‌باشگاه‌روبین‌کازان پرداخت خواهد کرد و سپس پوستر کسری طاهری رو منتشر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24045" target="_blank">📅 11:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24044">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I88vWWQZ6Z7RrD1YYcECZMYTgtFYEYH-rXe5yfHfq9WANMRihS-6ztDBOHNWtVhsx5AaLx-zjsfwr7wsziKxHEqHUURBoeBUWkKUKe7oszv5naawAGLpS6zFGc72pFr6XtBFe8BO0USOs_hTHKjlt0f1CBz03uldPoaukAJ2P-AFprsABWUYZs8Arhp2ypYTYGymzbZWlOx1SWXvns5MJCOweJYCCoPf3PuTUZY4sPmOQ6NKTlYmhqCKxZh_J6a9r_Ex7DyC169gYAwSH8ONdr5j_X77kEjGlvPdOEIFVtp0Qmhu6lRNXGgyQwwgH8qQJAU0WgaAVeJiCv5SzwkOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورزشگاه آزادی از هفته چهارم لیگ برتر در فصل جدید دردسترس خواهدبود و استقلال و پرسپولیس بازی‌های خانگی خود را دیگه اونجا برگزار میکنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24044" target="_blank">📅 09:38 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24043">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pq2_B6SOvNLwobKTL5FOp_Xek1HXMG_IPSgXZPhn4Fi1aWBLPnUZgb6qz3WaWL8MQc1ZJuhxADW0o1XXr5w0tAo_1tubVpqQ9jXCCJ9dtszsYk5OnDvXQAOkNViXN2iRi7sl8h9dNRa0hO-U-ue1eitlhC4e-Dov_iFOFq8pdIXOsBfMm4w6cwFUUxIzAQDy_597vvj40BYX8JciWdnK_c1ZuwEoRmMdZzqsKGwsDeHmwvakvw5wwI-lOmYUrIAF6Xa-96XAYwu-x6-KlyGP1QF-dVni3hRmE3NE8tvIXhpQpixKIwgu7zlLlkPB8lMJ0rRGjlZYV9nRDBp5bL7Ibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24043" target="_blank">📅 09:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24042">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fqhz2PRm6ndYMcYWmmmceEDpWPSq3fgzOZfM9tAyhUmIxNRO_0Ao-RM2sHzX7TV_fmI88GMppyMr3_Q_JeIKkh9XDYy6R7-edlQC2NdjlYdNwwrD0Xeo6E4OeCYXC9ivA9XCAgqot-PCq6ThHV77eqdGCKfloW_Xj3iPl1M-KaqOkvfiY2WtT-2OGT6woArBB_Jf7t0iM5xcU93AZOlnpR5kHE6FNhA_tBkeJAl1InbA-Jlh_e6Ozu-SsOmJjCfNkLCPKKnr-ryoiOFs_fgPsCUKRVksgWJeuoSbdXQ_Apn3qc3ISyKiyZ6Qt9tQM-VYuCnNoArbMvCcBNG-HZD9fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24042" target="_blank">📅 03:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24041">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8-MyjfT93rHeHwwIkLuC9Q3QLoNKJZ4cFAkMBMPLJ6G1N9CBCclNSIeMPsYTfMwQCLLONE7SchLy13NZAZHTpEeIJyEovBF9ldZcE5pcLpbI01l7AKeVlPNTU4Kp2X8x_YEP2FES_C0kfLxlDm8D0QMzQyRI7Td9-vsKKMJJXzukHGHunkgvWysFpqiaCyTFT5VKKP13J8OMXwlp_djUd1lJTA0-vB_7RYfiA6qqvn_0Yjx5K1ECLlqFqHSUr_9AksqSv3K61YKWfQJaOdGvSdJ3qk9YKLadV6jJEW_8NZ8Zd8bOALUw088_PFaxY4h_kX5NomzPQzgQwMNmhH9Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24041" target="_blank">📅 03:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24040">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⚽️
گل مرود ایران به بلژیک از نمایی زیبا و متفاوت ببینید؛ جوفوق‌العاده ورزشگاه رو هم مشاهده کنید.
‼️
اگه‌که‌فرم باسن مهدی طارمی دقیقا مثل سهراب سپهری‌میبود احتمال‌اینکه‌شاگردان قلعه‌نویی‌ امشب شگفتی ساز میشدند و بازی رو میبردن زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24040" target="_blank">📅 02:44 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24039">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=pJHZczcJKhThm9LDod_BcYGK8EI0Vk935JT2WMQCy4IzeNbctjxxaFwd7mdx_vInhb_k2IZzfiVVutWipgCqT8uCN36ik4iMjMscp7ROyRroG2ycTxaykYjQRo0Nt4chBCI6KdDMnnGOJUkIAfNjYNf7tEPkwtDCJcl_N0uHggU6s7TUx_Smlp5Slzb3HPXGOhYQlR6-iIa1nM5EPevU_nUS5F5t4PO3BdrjALQt2p68MV9MvNWO61c7GFv0GTsK5CZo0Ux5gtGEeCDUNBJCFU86hEVbQ8fphDI5BzDb6ZGxVbCAOmYLRX36_O-4o5YPmZq5mLQqoa_9LZn4i-fWuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e90d0111.mp4?token=pJHZczcJKhThm9LDod_BcYGK8EI0Vk935JT2WMQCy4IzeNbctjxxaFwd7mdx_vInhb_k2IZzfiVVutWipgCqT8uCN36ik4iMjMscp7ROyRroG2ycTxaykYjQRo0Nt4chBCI6KdDMnnGOJUkIAfNjYNf7tEPkwtDCJcl_N0uHggU6s7TUx_Smlp5Slzb3HPXGOhYQlR6-iIa1nM5EPevU_nUS5F5t4PO3BdrjALQt2p68MV9MvNWO61c7GFv0GTsK5CZo0Ux5gtGEeCDUNBJCFU86hEVbQ8fphDI5BzDb6ZGxVbCAOmYLRX36_O-4o5YPmZq5mLQqoa_9LZn4i-fWuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24039" target="_blank">📅 02:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24037">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KIN4Ww-9qehChu8q5hoD31LDmwrzv8kkryt4PaTZrR1L28XZV65vP7zr7H4676P6XQQ2fLDK6zjsko_xY5NZ-DCm2vuy0nHIWdgDQcQBSU0JCGAtIpmNdqnyYdbfyDA64tXmzThVnL0qJFUCIdOFu-Zarl2d6Cr8epnJpWCGqto9-CZdDcryBjFXSX8E5ofRsnU9UNX1ZZgU8i_sLptvFTjXlfmX8UUaLwbzBBgBeCTwv6LedOlJNph6P74wScB9TbXnIYA9hLnlF2ou--Hv8GMvzLfdkcgV7z71T6X7aXalNaJLX3rM7yWFNjUIRPSUkOffdd8XwpkZzGekoiRdEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
گلرایی‌که‌درتاریخ‌جام‌جهانی‌نمره 10 رو گرفتن:
🇵🇪
🇳🇱
رامون کیروگا، دروازبان پرو مقابل هلند.
🇺🇸
🇧🇪
تیم هاوارد، دروازبان آمریکا مقابل بلژیک.
🇨🇼
🇪🇨
الوی روم دروازبان کوراسائو مقابل اکوادور.
⚪️
🇧🇪
علیرضا بیرانوند دروازبان ایران مقابل بلژیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24037" target="_blank">📅 01:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24036">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWNpHlyN0yp3D_6apeEEFrMiAktooOG4T0FyLDynu-aO00IN3bcEP8m3eRqWec0zKO_wbM4HvQRNOTn-2mok49LyRedGb8eWhbw6o3TKaOUu9xu6SXrJcQNw0Pwik01LMxYGyYM9VnD_VMzdkj1IELY75HhEAOi8tpqwf7JTBbdHH8f7ifqwfrOzrmlK1_4IG0ZZcaTPt_GsBDU2Xn5IsN_-MY79kp0v87d2VeTA50xuaXrM-zMB98A8WUhF84MglIBofzVOmrE8nhaoQqzD50PaS_QNWQb7pDvOh3vlJUFS0EoSHyvCD9izgnIt6nYKrZNbye7Yxm3BPVPQS0n7vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
#تکمیلی؛ علیرضا بیرانوند با 7 سیو و کسب نمره 9 ازهواسکورد و نمره10 از سوفااسکور بعنوان بهترین بازیکن دیدار بلژیک - ایران انتخاب شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24036" target="_blank">📅 01:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24035">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=ldum2j3sos0At2Gkl4oJW4iHUsuQZJn5nWifENkPalzV8SwHnZ7aLuQ5ZQ_EElrHXctrCQuwm6vwJiw0Eh6yLknlp5rQk9hcJS6EBPHFNmGwX4F2tTfhow0uDh4Vg-A_uZF_PMFQ6I7kfYakyCNPdFLu0Mbaa6AL2zWe84EL8Atgt3L6XWcPqgungKevM-ZOHKrR6wEeYAXCTSnxzMlDr_ouilmEVWA6lOP28rX-9lpNGRAasfsBcdDgcMOvPs5i82dgCJb8KaGctXkXto4wUXCxAoCagK-MEbkDnot2PON11EL5hb_ZQ2CDCOGCfzsXnPcVfVXGvzPwzgnsI7ANvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d43c42ae5.mp4?token=ldum2j3sos0At2Gkl4oJW4iHUsuQZJn5nWifENkPalzV8SwHnZ7aLuQ5ZQ_EElrHXctrCQuwm6vwJiw0Eh6yLknlp5rQk9hcJS6EBPHFNmGwX4F2tTfhow0uDh4Vg-A_uZF_PMFQ6I7kfYakyCNPdFLu0Mbaa6AL2zWe84EL8Atgt3L6XWcPqgungKevM-ZOHKrR6wEeYAXCTSnxzMlDr_ouilmEVWA6lOP28rX-9lpNGRAasfsBcdDgcMOvPs5i82dgCJb8KaGctXkXto4wUXCxAoCagK-MEbkDnot2PON11EL5hb_ZQ2CDCOGCfzsXnPcVfVXGvzPwzgnsI7ANvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
گل‌اول‌ایران به بلژیک توسط مهدی طارمی در دقیقه 27 مسابقه که‌افساید مهدی طارمی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24035" target="_blank">📅 01:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24034">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-7mydWLfnYOWn38Mr2SPY1oB6QV7SrPQx3yc3ySKOZuVyzghEhFI1nL6M2Pc6G9Ru-dEcJnBsD86e6ODHgO56gODvYYdwNds7qfLwAOkiCoTaDz_Duq5qDcosfuyJqjQCz4-lzPD3ExT_JxY13WN5nF2U2nl7eYllumHPqLT_pSCe9Ts8I6LOrpbyA_BH9qz1oeWjCwghC53U9z_IT7Qc9B-gnibPkl9eRfXRBRZZoJ5BYQs9IyWgn3l8SMSLCISMrCkmZDM0UEr8_Y0bIqWTOY34HcCPcGqS76sNt0DU5a6IrIYUtlFIoqyxLYb3AE6AzxzGuDYkeM9uVPPK0I3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازنبردتماشایی یاران مسی با شاگردان رانگنیک تا جدال فرانسوی‌ها مقابل عراق
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24034" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24033">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xut-WmmB2V42eDa4uRjudubo8QlT7-VoDYud6A9giqrpNvsv2qaTtKJteWyJJNrqATLjwgceHK-qLu1sNKFklcqOwF2ZsecP9SJ2pTRjOzOguqsXuAwM5JVpkLMt8VKdpb77BITSCiiXyy0QtSzkugC-R6Ssg4XIqdJRZIFR9oaEjTjTJxF4m3xQdnn5BlJIPykMT5DO6bUCgSIEAFNtFp8N8GAlj9QLzsVPT1wReIVArL-CDVaI4mCG2GJ3w7alitHvPyCcO_5rv3HE52F1aR5qeq1h_Gzkj5vn65Zz1XSA3rUHbo0WTAdkAoV1UmFVkRIIPko_SFOhhi63FahiTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از برتری ژاپن و اسپانیا تا توقف بدون‌گل بلژیکی‌ها در جدال با یاران قلعه‌نویی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24033" target="_blank">📅 01:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24030">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=Ux0iVJ-cGlfIVfnE5zO6HVLr8VxLDUUePhOMzNoVlJuxP1BHiQMmbZfzsau24je7VPNW9agZ8Czd_Idw9G-CV1XjxVv3SRaIx5jjW7KNlN9GIjOnpBAxu3J-2uF1hNxcIfFeExozIf0FGkv_qzlaKcafcpxd5jA6cIJzi7kgE-RarlL82U4XyX2JOSpY45yA8X3QB9gI2hqjuYkJOuLRGg61lbHiKhV3M8oHbmxc9Dmr7QlFl5n9bmizpSDHirfWF2EzZFi_lQWz3I_4eJpAP8L7AZv5Lbhtplg3kyoIjL-cW7znbMddY7fG67MmWHRDifcS8Uug1WJQWA1SAwKWbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77de046aa0.mp4?token=Ux0iVJ-cGlfIVfnE5zO6HVLr8VxLDUUePhOMzNoVlJuxP1BHiQMmbZfzsau24je7VPNW9agZ8Czd_Idw9G-CV1XjxVv3SRaIx5jjW7KNlN9GIjOnpBAxu3J-2uF1hNxcIfFeExozIf0FGkv_qzlaKcafcpxd5jA6cIJzi7kgE-RarlL82U4XyX2JOSpY45yA8X3QB9gI2hqjuYkJOuLRGg61lbHiKhV3M8oHbmxc9Dmr7QlFl5n9bmizpSDHirfWF2EzZFi_lQWz3I_4eJpAP8L7AZv5Lbhtplg3kyoIjL-cW7znbMddY7fG67MmWHRDifcS8Uug1WJQWA1SAwKWbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروزکریمی‌پیشکسوت‌فوتبال: بیرانوند درتاریخ بی‌نظیر است ولی لطف کند کمی تنگ تر از این باشد. این چیزی که ما دیدیم خیلی هم تنگ نبود واقعا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24030" target="_blank">📅 01:19 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24029">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQGjXLVMo99Hh9dzqGQc3hYKW1CRQ-oO14AuDnHmZvPdHIEuKOesqqoxssGgGswTX7qg3giCz_vqNdpdzd6fk04XzOcXhWZzXdutEIOTU2GtkP89yRiUbQR-zoQClkYSpuC18GSoNSObyLjNHYqEwULfn7HXPsMWviOB0yw1o5rJQFI2R5E03mXwWgyPJMSGT264P7AnnggUnXLlcEsXhQjEnQkI6nXcf3TiqHRAll9t0BXgfQhCV16fhYNsjvnGrX_AWc3MQCYv_5JUmUvdo8IVoaqp3yPUT3Ray7C4QWzv7oEgQLQIG6MZ2viGWtxHAU9-lUzVUaUCACLLXX01Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24029" target="_blank">📅 00:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24028">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSthk7jnKtPoNB0hqhDl4eC2tu2v97eQvwdYEJlwU0rDNtQ_trbehlgSz0C7912Chq_X9g8CvpWkNVKeSwOw_KQ3PypVenIO3fwBXjZTaF1_Q_zSa3pSL5tlSo4uUaAtx_jhqp-qXZZ-0HFgTvLCuQSwlLFFaLa20X7IlORhXIta54eC8tE0v0sG8m7LkqlLfAZ_4UZK3Ggu_aH2LccCeFi1JgCFg4-hhfHpTttVyvEq6u6C8SqsuXYoyFctPQHOuE-ZwI8_VVvlqzjAGYf7gZNCkketjG9V8i-jgVXTKsZR1ZHOtw8oWHpOki2JdhkelV9fVl8vN0hLI7plKlc4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم جام جهانی 2026؛ دشت یک امتیازی شاگردان امیرقلعه‌نویی مقابل ستارگان فوتبال بلژیک درشب درخشش‌علیرضا بیرانوند؛ سوفاسکور بهترین بازیکن زمین رو بیرو معرفی کرد.
🇮🇷
ایران
0️⃣
-
0️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24028" target="_blank">📅 00:36 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24027">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aowJv88LhQ3MRrwsEPjxfVtjg_56yq6CcQ6R6oEbgz_UfOR2qeCuZh3nhl5oS2t7GIBgE3E4XjzrIv3iV1TVGGsirHKPRe9SIvqrRyMlPHmRjcdMdgYORg04mOxubaGAsQ_CY7qRYbX-EqNqZY2SP-QGkApF_X-5JLdMGlzZ9Hye4mlm_FhHNT_-5ZhLPMc2sA1WSQUTshjHPUatPj1ZybXepaf2Er3ykvg8msVoJ12v-4L2KuLu8Jc9ZQX5BhD7WaeXplTwS3i_NOTlzJ4y3q_ildit2oNWJDN2r0NhUbRE49DCQAF7YrdmkXoy0VkBkdGGjC3nnOcvg-DyueAJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
یک واکنش دیدنی دیگر از بیرانوند که دروازه تیم ایران را از فروپاشی نجات داد؛ تمجید رسانه تاچ‌ لاین انگلیس از دروازه‌بان ایران: علی بیرانوند مقابل بلژیک بهترین بازی‌ دوران حرفه‌ای خود را انجام می‌دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24027" target="_blank">📅 00:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24026">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=Sdy80QrTC0Ez6bJfTKOZkWiGgHTcJzHDAMo3I4-odfiPiAwxxTKJbF5OXKLZjyvOlrNq_VHs7aWrSIWfIC-5Vy6ghB_r-jx3bt79C8zKpOlsf3kKkvl-QjhELmvqCl5EZ0H3nYG2Vz0ZUqecVPM97Hi04DZPT_FstS4vOjo_xoon3yCnTdY8LeO5sofvhdHZlRuR80kskCwwyqwj90u6Sj6U7B2OKc7pfGb1kDTk6BO63hZb0omAeFgJjQzFK0IiIy-sW9DHaLNXGSc4fCIOB2eeAKwVaZrF4LJRZi_6hbN36xnjXYZvqSuRi8BY8yrH_EkFvNuGVuM3c9BwCkTg1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54539b7e86.mp4?token=Sdy80QrTC0Ez6bJfTKOZkWiGgHTcJzHDAMo3I4-odfiPiAwxxTKJbF5OXKLZjyvOlrNq_VHs7aWrSIWfIC-5Vy6ghB_r-jx3bt79C8zKpOlsf3kKkvl-QjhELmvqCl5EZ0H3nYG2Vz0ZUqecVPM97Hi04DZPT_FstS4vOjo_xoon3yCnTdY8LeO5sofvhdHZlRuR80kskCwwyqwj90u6Sj6U7B2OKc7pfGb1kDTk6BO63hZb0omAeFgJjQzFK0IiIy-sW9DHaLNXGSc4fCIOB2eeAKwVaZrF4LJRZi_6hbN36xnjXYZvqSuRi8BY8yrH_EkFvNuGVuM3c9BwCkTg1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سیو عجیب و غریب و استثنایی علیرضا بیرانوند که میتونه کاندید بهترین سیو جام جهانی 2026 بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24026" target="_blank">📅 00:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24025">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94db339245.mp4?token=OOHyRbxENwfl-kkbGhHcR0T8ene4ODN6p0M0nNmY7iuB_YUDy1S4QIGrQYtTtWv9bas7s1dZMtAW34y3NQIozq4DUV9kNotf7nrYd8lq48xR5D5RV_moZBc92cZ6hqJhJaejpTT6uFx0QBt2I8f1v2Z7Egw8H6o0flZt8bbFENWXhb5cpvj8D_2aDJPVcGTW-LLTiPJyrTEdRkSih9nND2eYtjeazf41WZ4zCxq3pJ6dBYckmXPjbnuDHiYfHQ2wMWBIOXr2B1NvLFHB5YL2rzcX5JahGOIpVC0AGfdAEhDTLlNzTLNxu4dZthTQQ0TSKMwxbv9W_40lTcYyETn56w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94db339245.mp4?token=OOHyRbxENwfl-kkbGhHcR0T8ene4ODN6p0M0nNmY7iuB_YUDy1S4QIGrQYtTtWv9bas7s1dZMtAW34y3NQIozq4DUV9kNotf7nrYd8lq48xR5D5RV_moZBc92cZ6hqJhJaejpTT6uFx0QBt2I8f1v2Z7Egw8H6o0flZt8bbFENWXhb5cpvj8D_2aDJPVcGTW-LLTiPJyrTEdRkSih9nND2eYtjeazf41WZ4zCxq3pJ6dBYckmXPjbnuDHiYfHQ2wMWBIOXr2B1NvLFHB5YL2rzcX5JahGOIpVC0AGfdAEhDTLlNzTLNxu4dZthTQQ0TSKMwxbv9W_40lTcYyETn56w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نمرات بازیکنان ایران
🆚
بلژیک در پایان نیمه اول بازی؛ علی بیرو دومین بازیکن برتر زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24025" target="_blank">📅 00:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24023">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqQm8kxUITzxLxc0nPw-jm4JdejQpMoEu1nORDg5BpzBJMx-Itvkfl4fFLfcahZidyYiB2_qqYMjV_nCY04rhWE2lktqXPdqr5l_Q-YtFx0u4LLiV_09Dk3hpSuGA8yH0VixTDssQHYt2wHnxC_g_ASjvNRAdioW87heMuSFx9uiM0rkZ-fzjWfzfR9Nt1xd1pq8ruANsVv5aBWsigesxvO5I3esO7L3lDH4sZyoO0p8RyzkPs3P-yKo3D5JSmzBqGT4r8oxEb_WcKvQH_HHCcmHP1s7c8pIJ6vOkX-qTXH1ki_lDTPQP6AO_0sxki8pTzHwObFeODCw0dtW2UwooQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6bhAp_T_TwEweUZSlV7VAWOfv6H8BwueXhuFL0csQiWN8C3DMviJHxRTlC4-1aC91T5Reob_Htdbbz19rLUSoENAxQUelTaSBKIoJOtgV1N07J-UAlXd-0y1JebmCKflaKjAylMSKqzxNJC6ANKHQpoSBBeo3yltRBSVJzgQH9thxlUuOyAF7aLOiUOQfsfl9MfO9V0PfOAE01VNogKNY5-0Us74tJlxWs-7zjS_g9ZS5c8ZxofXmLEZMgBRevCt3M-H7CqszbBe-rG9zJA2TrYtCNu78IHdRi9irJZnzN2B2l6gPOSpb4Wurzbo9qalfosHpibENiNS3cOWhiboQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نیمه اول دیدار امشب دوتیم ایران
🆚
بلژیک در هفته دوم رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24023" target="_blank">📅 23:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24022">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUiWelg0YhRalCbBH4aAy9bEeTKLj6Kef4lxeWS66MNZPYLn0w1-7D4eIw__eG1ijliQ6xbCygRbDaMONGEuZGAx2WghP3ZGLySjQqOxD-u0U96SnZpl-OqNuYPTmd999ANtpCuhuOLUArU5u7402vib3irgzUkWFyQxBPNuDx3YWA06gXuZUCSXcDMz6E043UeutoM_7lQufVf0LTSJzXbQL05dHrVLIzOxdeQgVQyeeRBpRqwPMGSdmpmvjHuvi7D3YE6CmtV8JOtijmjXEbvKf2LQODoaxb3ok0FUUWrzNROJrxhYgO7e2-daxM9WC5gxHdla-7x1JZQBt55DMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
امیرقلعه‌نویی این تاکتیک تیم کومان در جام جهانی 2022 که منجر به گل شد رو برای شاگرداش گذاشته اما غافل‌ازاینکه‌باسن طارمی توافساید بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24022" target="_blank">📅 23:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24021">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a43b24a8b3.mp4?token=TaHqCiVIIVoJPFGy3CMuZgpFp9AWW0_4PlyhJ8gu9Msex8UQwfmZH4KUFf_zDJUGpCFPY8yqVZkeu8X03WGsLitbDvBLU9keL0oXQEdBdq88k8Z4ibDbmww3FvYGI71vN5_oDAPxw16Lx3yyTMudmmiEakjEygjW1kcufUTmO3mIfciWWdhtkdvuU3n1LS-nE7qDFZHjtz2GmkyDiJgG3aeHXF0RZ75mey97cD1L5jSyKPBdxe29d9vB_pw8pQjaeWX2CVoD7CpfxYYCrAslijn5BmLDtcVUhjUPMF1_uMTqmunhhSturUE7_Fbp7bQ8gtE1L4H3Ny0bM2MoPACUgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a43b24a8b3.mp4?token=TaHqCiVIIVoJPFGy3CMuZgpFp9AWW0_4PlyhJ8gu9Msex8UQwfmZH4KUFf_zDJUGpCFPY8yqVZkeu8X03WGsLitbDvBLU9keL0oXQEdBdq88k8Z4ibDbmww3FvYGI71vN5_oDAPxw16Lx3yyTMudmmiEakjEygjW1kcufUTmO3mIfciWWdhtkdvuU3n1LS-nE7qDFZHjtz2GmkyDiJgG3aeHXF0RZ75mey97cD1L5jSyKPBdxe29d9vB_pw8pQjaeWX2CVoD7CpfxYYCrAslijn5BmLDtcVUhjUPMF1_uMTqmunhhSturUE7_Fbp7bQ8gtE1L4H3Ny0bM2MoPACUgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
گل‌اول‌ایران به بلژیک توسط مهدی طارمی در دقیقه 27 مسابقه که‌افساید مهدی طارمی گرفته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24021" target="_blank">📅 23:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24020">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61647a74d.mp4?token=C_b-byjcRoNtdrvLAXDFmDn0bBOIGyDr7gogsw8fWxT4qXthM9cxH_2PsJN_PJAoGXZVDygKBv_JBlq0Di04jXAasxCmY9ZofrFPzr20CMruittoq5rEDDUvhHnMPS6Ti76Ad6zQvBDN4S60GbgsyXC90vBYv2oZCNlHWCwefx70ZqRe-PkgElIJUio8ikd-XKoQH6DiXtlZO-d41808V2HSY1BIQfKfqpF24ZYsa_COy0aAb7SsdElU8zv3EC1-ja2X-L-tz22GZ-WQ26EXEpaKiI9cvmt680xEKI4uhwP8LPtZ7ZoXN7OiqVfpwFtnDBB1DMCoXYzxoL2OxJyXng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61647a74d.mp4?token=C_b-byjcRoNtdrvLAXDFmDn0bBOIGyDr7gogsw8fWxT4qXthM9cxH_2PsJN_PJAoGXZVDygKBv_JBlq0Di04jXAasxCmY9ZofrFPzr20CMruittoq5rEDDUvhHnMPS6Ti76Ad6zQvBDN4S60GbgsyXC90vBYv2oZCNlHWCwefx70ZqRe-PkgElIJUio8ikd-XKoQH6DiXtlZO-d41808V2HSY1BIQfKfqpF24ZYsa_COy0aAb7SsdElU8zv3EC1-ja2X-L-tz22GZ-WQ26EXEpaKiI9cvmt680xEKI4uhwP8LPtZ7ZoXN7OiqVfpwFtnDBB1DMCoXYzxoL2OxJyXng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24020" target="_blank">📅 22:59 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24019">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrRhLwlb4b9JuUA-WtfRtCbNVoddksv4ttyixD5CelehKKjZ5-CopWWtJ3JCmrwZQVhH-s45arDpywHK8tIuz5kO53B4XR2xJrPIT8jvYHezfa9bCtaasPkPzsj_ZHpObGBdWVzGqlQ4m1Ow3MCYsJuglGcr7XnSxazmNl1innmUMzEfrhktvE2FZ36MzJ0IThQDRliRx5Yn2TaBA2Wyc74sLzp9Foa-kZ2Lg2yKNCZyCxDCpURG1kjfBOhDhL3EGaeEBRmJkw0udWq_UmWuM77VJdb6EsLDzkGwrH7kyoDeiwxpvb8fZ5k7bYQtN68glTu6ZGMIFXiVJ-5UvCBIkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇪
شماتیک‌ترکیب‌بلژیک‌برای بازی امشب با ایران؛ درحالی روملو لوکاکو و تروسارد به بازی رسیدند که سرمربی بلژیک گفته بود ناراحتی دارند و احتمالا در ترکیب‌ نیستن. احتمالا خواسته به ژنرال رکب بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24019" target="_blank">📅 22:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24018">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvDOBFpjbk7EDRjYuAsO9kq14LI5utHhvbG1nc74ftC0fw5vWl54wPllC8sqHfo3iPGcMPo3cn4Qu3By0vEmkrhgyTXQPIrq8ba6YxBVwFS12_AavOyu0AMoq8AbEoDGQFjKVHz11DRoycaIl6OvNIZ7EWTCk_0ks9NZO7tNTt-qPPdJXzxU7kuY9K0tTzbVSRK8a0iK3Z0Zs14gLceVyLO4F8TguUvbvnZDGaUNidIoOPxn5U7bISP_NdTGicVQYNQ2tAcMUnvfvVFJi3pmjveU0kRtG6eNR5JLnvxBL0D1aBiW0GRqBSnE57FyWojiKKoNbdknjnt6YWPrvHztuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیمان حدادی مدیرعامل تیم پرسپولیس: تا پس‌فردا بین اوسمارویرا و دراگان اسکوچیچ یکی رو بعنوان سرمربی فصل جدید انتخاب خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24018" target="_blank">📅 22:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24017">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1xU_53mNlHKVXMhVEhzkkBRRlDsk2vOelxA3pY5LOOpn_n7xZEbZ9LZzapC_rFgg8oBUAwjIQooS-_hGWeDfccw5FLyLvzrg6DY852F4oiU7JDG3TJEBhyB8uS1qI1XZ8jMXgvd-QztApYrrEIiBGcMtA7TOu8Y2jWcItKFbt-MQQA7120KlxTRwOLwsyfFATdQ1KY7K0oFm_Ie4xToi-UHoT2JC44PfoZPrbPKgfOkt6Dk1i0D_Q1W-dOHYm9PW3iExr7MFUV08igetYfzEtWc6bvfrbOkF9hnCUBWhI77-DvkGtLlg39cK27bGdAosoMgAHL8jkUYULJ2DknSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی؛ پیروزی پرگل و شیرین لاروخا در گام دوم رقابت‌ها مقابل عربستان سعودی.
🇪🇸
اسپانیا
4️⃣
-
0️⃣
عربستان
🇸🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24017" target="_blank">📅 21:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24016">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی؛ پیروزی پرگل و شیرین لاروخا در گام دوم رقابت‌ها مقابل عربستان سعودی.
🇪🇸
اسپانیا
4️⃣
-
0️⃣
عربستان
🇸🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24016" target="_blank">📅 21:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24015">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckVScvF0tCDwL3FcfpIluf2XyakweYjtt3vQ11w0opb6JHs5ZP10LI5XoR3UO4iSUZWBBy4rKqvBS9CXrnlWRzvoAGFqmj5a8h4xtqSajvkgQM7GBviDN_Na3iJcwFKx-zplp_BeYEeNIoXfUIj0221WBAUlHJe1GZyVA5DnbmUMml9iz2DBTY6IH69t5vS89W0r9GMAmEIpooSVw07eTP7hFLs_aD8undXWmZqszfRTlLn3CzaW8BliNgXveN8pJKNpkKKTvDwjZsrk-0oVDa-MdRihrY_QaCvjQtx6agtjoqR7oRxuxAPXF_vt7s8nr-1TsVWFBqq-ethBphEEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب تیم ملی اسپانیا برای دیدار با عربستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24015" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24014">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qzij86dTJsVgw6hqkcltAYQnE7hn4dikAgopVaudtd0tfzg1839HP3se5cZksrYRWLCq7Vm0WC6ivbULXBPh7v66q15CAoqHxTGR8u-0YFrcwtlIfzmndlZxwR6AWvTHfErNtFpeOwk-UiVREZSsEzIeU_gt-RkKtz2khygpl4xvVQgl7WnJkHdLigAQDfm0u6mibN0MYgs-PhAPAJa0biGf4xzroc2dcBfiVwiHgLJJaiFK8NcTN1ZYpAsVZ70FkLNYMhjt93P5ZIMvNrWXUJ1eaVuR9o4udwSB73_3adyS8PGoHnPtTXGIhBDlERtsASAEMjALWO8aQ7wWhpQOyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24014" target="_blank">📅 21:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24013">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4Dg0pca_4d3by76ZfSVWb0n4nJPeCxaM-MqyF8mLFok2OkURqDDKs13nBV3_0L5ZLDp5ugfe9hmrlH-CR7CWJ_QfXj-zYxcmE6Umldb6x6Cn67faceHthEPgIPvalPKuuGDqZGR13AQibRov9YOz3k6y-Ip_U5ijYcvdVWqzEDFsvyssWBYSxLQ6zUWiTxz5siOyf5DvPmz1Htha80KDerFgsIIvFfUPeH3FTCJiKvseuZlAllJiJmlyotDS0AZvYSbWr_HYQ9gJnaAkvE9LDnIS7WtKPYpYpUJUkcwKgrSdgL_CKhXQkebz4Ssg76Xd7KXFn1IN8MYNPo5PL1RAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24013" target="_blank">📅 21:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24012">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDEJEPm5izOxe1kih9LWKBAdN44Vi0E-T4c9IgUS_cpYMS-KTKqYj4pvHXTO1gt4lkLm5-93Bu_El2GXVqCDM3QlEHztcna4g-ICtgXUewQZsMNfORRK90iTDcqhHJoGOtNxJFwgxkhP-FhxQ1F82H3S8GQZJB4Eq6HO1wCy-3hIOesMMQYToLr8zEDeoqLlWwpvEDmK8N3Ou83zoqpbgAAsHZMaiTxd74ojoe9JbWHNPyR30Yy1wFLLp-G21GqlBXvwz6s6nWO3DzMgEiylraHv1Nreol4CMAcznQnD_owvzIL15lTcJvTC2rNh2s_dx6JR560vUx3uf7oArQOmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌جام‌جهانی2026
؛شماتیک‌ترکیب ایران برای دیدار مقابل بلژیک؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24012" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24011">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFpLFflc7v7gvy9HlsgRssV_p7jBgEMEPVm3k7Aes7jDFW44vStljMhK5vvEyLBkxX79Ou1vWn5Ii-s-KiftQLtxTXFkkh1uDe0JUHfKHSfl_oDUQ4JyZ_aU8gGNk4RvL8qVEPRgxJrWb-LROHuC2dz_xsKWhQr6YEatGdOcV27jae4L7YbyAXUHb9ip5j5n2PP20cLOjTFL07480Dxnm9qQN1LzQJKnkWyAoRNh-aBrWu6LuxHKqOTH_kaWaN3UM7C3AC12rZ0e8PSnJ5l4neht7fIXKc0G1bGEz9mNQG5pSEJ3ZdEg7Ggyq5ROnuES2T5sWTafXbDtlg2Wp_hyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24011" target="_blank">📅 21:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24009">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXxiEczkjf3U9frXq5Taew7fqhv6uLSvwCe_5gwQkorOauFBaZUa7RpV6RualOYBPh64-F31mRoV-_m_Anl_bZywiBZjxjCKEANW3-Y_GKu_5wz16QJt5d8RptknQgB0GPG_DvvnbUBcL_fPsZPWIllqreZ_BiQFimKABx6BBldUBUwW_qTduMAG4jxiBGF5ihzX_mHVpMZd3VaeGvLdqrCsFnLGahEK_Cvw9UrDLjEKtUU19-hSOyaEm_Dq96fMhxZP4otpMtFjaWCwDHcSChhCKQQG120ALhXjRMUAcVB86ePgfQ62XldcoVj7Soiwi9LiEzMihvl7hLSvfIx9VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛همانطورکه‌بعنوان اولین رسانه خبر ازمذاکرات محمد دانشگر با باشگاه تراکتور دادیم و صبح نیز درباره پیشنهاد مالی این بازیکن خبر دادیم دقایقی قبل تراکتور موافقت خود را با این آفر اعلام کرد و دانشگر به زودی راهی دفتر محمدرضا زنوزی خواهد شد تا قرارداد دوساله…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24009" target="_blank">📅 20:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24008">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-LC7uPIrgiomO8U1WQfjwP1ggxtTn4ZfZLiSqy51yW-LjrsWkye_xbTGNZBV1v3HQA8kE69Liy6zqyK87PLGJybpmPKvnRF8yYJgX0HazxhyjTyx1oCmAfOmUh7CMRp7K4HdHNPfGnxi1aSfmv3DyH3bMpzk5kMYwOND6GBD8hsRPFePOQglVZUOXRzbSMqBDneDwY3BPXJ_0m50zEzfGH7booEWFJPaRPDWOAIyKwvQkrPWKJMwQ5s_IM75OHx3Ni4jfqb7iNXmsRHvXuaepOoFdjPiT4GgEfXXPKvX6S3tmBAmYrDQwzBIZdT0B9aPWYolBXBsybGAR0bgWDqBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24008" target="_blank">📅 20:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24007">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHSnA331ueeKkxom0quLecW82VaTvVlxf-_m1FNJraRtR_m-ZEv7Ed5sM2h-bEVlfdDm-jEvugN3gZfLQ_pn1P-lrQ4R8HPR3NOjBIlhkevcTctQZfchVnfIQ0Pnzm-mE53n2moNCU-nmMtirEjnAdHwOiQmlBFn1ZstOV1nfkp1q5FnAaexM9V3ugwur8S3ahJMcuKMReQKuqJXIXpvkWgWwE1SXfkvnHuN7SToj5VP54MIXrf_q0WGF3AUhK7-ACtOEfYBv5VFqWD78Gz9sFKlYcV_TGc4_OMPH5MZuV5JbBV2oINAkQ40qIkfLdieYwe7cc8TpuD4bMuvtp96wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24007" target="_blank">📅 20:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24005">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JR8RR5UUpVlIcPZBOZyHQrPaiTvbbmhOuDekYkbXamLMhZ1eexIaurV4bZoSepGvNtJWJGgrW28wNoh81Q2si1ugGtKyZYTArYjoQqYvVQ5l5t2a6bEmB0u9eGLWmDDfwAucj2nLsyZXdguaZEOKgo22vSX4sbJtq7UmP3ZxbLB5A7dwNqlYjy-wu5C5IVybmy_QCrDJQFCsgWuz9D_ei3nRYmGbGWCgrp0qbAnjSNWJBkwVT1P0fhiPrv4jfN-5Wxv5H4Ko72T-pPMe1vw8vTfutSPr0NMFt1GiBvy48Ci_Si9pX2z_M50E_iFspW6FXPerduTpclNo0uVRP66a9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ جلسه‌مدیران باشگاه پرسپولیس با اسکوچیچ و نماینده‌اش‌دقایقی قبل‌درترکیه به پایان رسید. پیگیری خواهیم کرد نتیجه جلسه رو تا پایان امشب بعد بازی ایران اطلاع رسانی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24005" target="_blank">📅 19:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24004">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isC6S-ge5AvHrhd3igc8cSdfTz5vTuQ-S0c_wF3Atr4SIJEwsJ19itDQpQ4Zaqp1YbUX4q-AJk5JTmHTx68nAq3fNPr9gDVtFzDTNIadEfXxxZsyc32qLfs3YRXFKdvwndXTvJT8BDajDKLTQcublKhE6K5q3vIG1YHPFu5eTnNJ03YhkLyDwdboeiac2hkbnDNx92bT6B9kxfTXNVnJeky58oTKEjb0UlLeW7QyEKaXgqXBIhvi1RxfaCawibg02Cxm90bIBp4Di5AZV2rYyz8tG_V5OPnpXbzSjiLe6mCD34UA8Ezp6_-AR2rlYxWYUoXT8kGpuWfPXjIDDdHMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد دانشگر در مذاکرات خود را بامدیران‌باشگاه‌تراکتور برای دو فصل حضور در این تیم خواستار 190 میلیارد تومان ناقابل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24004" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24003">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M2NJpKjciD9VrCtLnXPiwTx_Pck-9wXVf_ChHY2BBveHH22waw-pWh_eoeaRaBFM2qw2xWgV9D3PhjyJ7r__pqIakbwCfMzJKplz0UGaGyZ_mcjzAd7lQzVfK8zLXct4CJBRRyqVMigiEQliWAiJadi4cH30grHqPsNoXB3CIHTEjeVDZIOoz1htEiQEM0ONamQGqSP1YRHWQK-1gCFN4azqD7Ru7dUAyq0eDFhAiFSF3wHcFkkGM6_9Gt2wLrWBweKe-UUb90QR1rm5R5aNeh_It0fILgfYUcWxd3TeET2RywbzdkytChPCG1r362rDoKzEcpga-yaUjD8mWflq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
کشور نروژ اعلام کرده هر کی تو روز عرضه بازی GTA6، بچه بدنیا بیاره، یه‌نسخه‌رایگان از بازی بهش میدن. وقتی‌نمونده اگه نسخه رایگان میخوای، همین الان پستوبفرست‌براش تاکارای اداری‌شو انجام بدین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24003" target="_blank">📅 19:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24001">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtxhaDKEbWXrxAuMdknYYhfz_oY0xdhlk5ka2Ghz4bAVyvrlWGPYnrtmeWVvUtuseGfevBkW2ELVRVkl2Nb6dwuUdxuA614UMS9F5vIACRpbvii7ZC6T6LOcbwkxb_IyRkGUCUaGiBTQukR3r2d1KTF4Wc6blL3DcCXGYD8_Yj9o9FWsajWfyo1rqOoOWfs2mJYXtu0W0o9Wnd0gdNuIrooL4f5lBiNPQTKZN9oRQQecewzCypPak5lkEunH6uNLPNha5NEEpMX9dyJwSklx6y2sPd80CLmYAHGZ_asQOfd-wfSsh9ZpQI3uctC_sJleDb9xAVUO5p7ytH_ZPUNYfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانی</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24001" target="_blank">📅 18:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-24000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVhCip_-R86kmfWrCPEUN_J-GGjytin-TNaRy0YihZBa06Gl4Qq9IL7mXF6oX-6lE93FKZ3jb6NJPYS4pvkzPeXhPGiETmRDZHPhMPXd_KC8RS8sNJnwgvBFx2uxo0sKKh1SWbFu1nk_3wk4P7d-2pTw9xyXAO171oFUAEtclalUcUYqTwDjoX4c_yrMP2bVqZ35cftt_5EeDhlFx-1RJ7cHe77CLr-ZD3K7FbZORKBR_2JsLjzSSuxWf7QHbRIXahoGOtljVnX7ZRKKn_ZZewQg_koEiROo61SXj5y-k7jK5D3IVM9JuuUSIaKdY9cEIRyXtA3IvVl5X8CKOM6txg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رکوردجهان توسط یک مرد اهل جزیره کوچک کم جمعیت‌در دریای‌کارائیب‌شکسته شد؛ الوی روم دروازه بان 37 ساله کوراسائو در بازی دیشب مقابل اکوادور موفق‌به‌ثبت 15 سیو شد و رکورد بیشترین سیو در 90 دقیقه‌یک بازی جام جهانی رو شکست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24000" target="_blank">📅 18:44 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23999">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=tybP7_9hI0SwxKerAKNfKvtNslOYEsak6K3B6wMi1Qp24chrHGlpCaPOfHpOLk84ArYEO95t8O3kiBhJpATJoega2a26vbCWKYKj5o0coRoXAQx1cPzHX8UBCQh0wFsVtOIUplbErms72UHBhsyasb4DtiaXKFfZpYsn5-cJnNr5YMMZBstMJctwNtlILOzzgSGF0R0BUoDt2n0NMrv_EET-f3JClD0bU5gwfKgQYnVlkGtWAyjzVM-kuyoZeQiWDe_-2Z46gtl0WzNdJf4MsyTvR7H-Id1ZEPd4_OCebJSLUh_hB1KaCq6h2LUPeD9-c4HV3k7pz7pUFMKAXQnwDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe31d4a415.mp4?token=tybP7_9hI0SwxKerAKNfKvtNslOYEsak6K3B6wMi1Qp24chrHGlpCaPOfHpOLk84ArYEO95t8O3kiBhJpATJoega2a26vbCWKYKj5o0coRoXAQx1cPzHX8UBCQh0wFsVtOIUplbErms72UHBhsyasb4DtiaXKFfZpYsn5-cJnNr5YMMZBstMJctwNtlILOzzgSGF0R0BUoDt2n0NMrv_EET-f3JClD0bU5gwfKgQYnVlkGtWAyjzVM-kuyoZeQiWDe_-2Z46gtl0WzNdJf4MsyTvR7H-Id1ZEPd4_OCebJSLUh_hB1KaCq6h2LUPeD9-c4HV3k7pz7pUFMKAXQnwDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعدِضربه‌موزی‌شکل؛ و حالا ضربه پنبه‌ای
😕
😂
رونمایی سرهنگ علیفر از دیگر نوع ضربه در فوتبال
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23999" target="_blank">📅 18:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23998">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMx5JkCbZkDbclGUWkrVwrMqrisPdP24dclO99nLoXjvQTzMLFvmcnPffrJioNZOenNmWl262tpw9x61iPtN26fH_LkBTFtNhCT7vJHpcbbXSbanXZuC2z30VDo1e16YwfQ-WkjBJnNkYsazMbKMDzElgGj9DZnMtPT9b-a_PLl6OkuzdRdLw47mWMjbJWe_G4U1FZ1HZNsxdHCBXJfxBJD_ZTp7KrMZjLHiHJ884zzpj5Qb_9jSTZJiiznr_26x8kDj4fk-0dhovkQgHVxUGggTkrYr1bawBk5hPokwF_93En9OFQPSxwVD2fXT_CRoNh1JgDk9o92rgDhZNtTfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23998" target="_blank">📅 18:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23997">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCdM35Fqyud_GYj_0PklBRFBCCWASt0N1JldO3MY74qIHIj2lHGATuvjYHZUA06cgHqgTy-2_hTKVj6B1NVf2P3IXDdDhXmL5NXVEmAET-qzsNKVnlSEp5tEVyd1wmvyNyF1Yoh4_jtwrhajGEGHizDLbMuJbb0EGGKunBoKYmSGYk5DLdb2_ub4bGcDkSN4ykhyXJNAoQFiUwwiYcl9xHLKlkxA8Phn4Jw3BUk-6tlaZhMMzRBcVxcnDa7aHzSj4AdEfakfkpLB9miKXEsSzaHdleO00eYJWptVQj6vg8Tuwrq90w-mQ1_PHUQ4RbKcIQaTDUylO9kCiBiYwiAzcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب تیم ملی اسپانیا برای دیدار با عربستان؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23997" target="_blank">📅 17:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23996">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjuV0mKAZg3dZYj7m8z6-kGzq4fE3SKGbtmTpVcdu6KNqNRNjgVtlyheTjRb4DSr5DHvfany0-QXt7GfkKVy-YsAz9lm3YyRMT-PwdhlrQzn-gvKE5sUCP0m8fMhHpca--48lIRj7aqtYR83P0e2t5c5IDT3Bo9zwSWktJFh8KafTLpOOfHurxbWpDWlukK192c161JtwBnWAfAvmfVnkFhy0Tp5YEbu6mZ8qpUbaDWDM3llo7NREwovcHZfP-M8tGn51BaON__zh44bGMG6wl93iziDG2PUYnCx_gQ4Pp8kiRr7dDv-HS0mnA32sKV9iETfhSlg_pQpJB2wSa-mww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛
رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23996" target="_blank">📅 17:53 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23995">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odJsMKun7DxR4g6W8oZw-FFoHLhhg4pas9Dwaf8Mpm8IsLtqfxHE1jnrNt_ieV8ztylb36khgUzBUbBvKDoAav3552mlNXwC09y58locxc0RAhn4zgyKHWgouqpsj-B3vuDfi6VsZVgvGf7GnpJEoMBiLhihgXhUEydks1beaNQvjy0DENA2r9knJxv3JPzjxcVflvIw37Hm_p4EZMbHyWkQs99sTmY08q9poz6QvJTK_teiASOpshxvzADaXqNXAyY-jUJd0rRNWH87Z5qGFDTQV3YcyiI3DYBbZ4KOGb9FMFsLTGH2_ZbRJuJaqSUo97KZlVGqZlzn_ugfdvX5bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23995" target="_blank">📅 17:43 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23994">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etLWZi6I0rOCfhZnvKLZAGwGGrQNQ8IkFawC2LegrECSWiY34ZY45MvAHCEPdFQ_xZKZBUglbZjrllL-kERoCSI2EY85aG4bykYynTgUGIZ98LtCsr0MPc3hSyZZBmWG4WOfrjP3EfLb9ib8bNCQe7pya35h974UjypXdvai1njbFyDSfntTmojiMr3hKJgVsWo-MUkmMi87Z3l_16ixc-R6Rw2zkouZiCr71PjOO0cU6j1fAdk5UC1DDvS6s0b2RvXV5_ML87iO2-kKFLGEzQEHb4_muy2t7slLYRnIa4z_aCw4uRv3-hgvmawP5iNB-svRvGdoAwc5BsX5balYWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
جی دی ونس معاون اول ترامپ: باز شدن تنگه هرمز و پایان دادن به برنامه هسته‌‌ای ایران؛ این کارها قبلا انجام شدند! سوال اینه که ما اکنون چقدر می‌توانیم باهم به‌موفقیت برسیم. آیا میتونیم روابط درخاورمیانه را بطور دائم و همیشگی تغییر دهیم، یا به‌انجام کارها…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23994" target="_blank">📅 17:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23993">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420ab2f182.mp4?token=taohcuc74YvMQb18AxGlqx8Vfnx5Q0dINQ5U052sx0fde5P2pHqwJwpX6wIDcylDnE214Gfo6dKED7lFq1gkQKzGknbIo_8PHCh4oDCXqZVnLBLBreisg8W6r5xFVR50q1EY1hKKWcgfE18vojHA8Yyv6x9GuKdM1lzjC-xYd2KiHTguXA4a4lZu8d3BDMYz55INX752zE2tBEJmNfmLcbXK0VHBWBWF7VB1ur5CZnx20Sd8B430E4MBDP_Gqo6S4kS1noId7PvAGogNE_0OJY88WgNq-uHEGlWcGno-_urYPb5tP3C8rF2GOZoAQF0h2kfjFE2alZgvhSrTR3ZYHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420ab2f182.mp4?token=taohcuc74YvMQb18AxGlqx8Vfnx5Q0dINQ5U052sx0fde5P2pHqwJwpX6wIDcylDnE214Gfo6dKED7lFq1gkQKzGknbIo_8PHCh4oDCXqZVnLBLBreisg8W6r5xFVR50q1EY1hKKWcgfE18vojHA8Yyv6x9GuKdM1lzjC-xYd2KiHTguXA4a4lZu8d3BDMYz55INX752zE2tBEJmNfmLcbXK0VHBWBWF7VB1ur5CZnx20Sd8B430E4MBDP_Gqo6S4kS1noId7PvAGogNE_0OJY88WgNq-uHEGlWcGno-_urYPb5tP3C8rF2GOZoAQF0h2kfjFE2alZgvhSrTR3ZYHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باز هم ژاپن و باز هم ماجرای عبور کردن یا نکردن تمام توپ از تمام خط؛ توپی که بصورت میلی متری از روی خط دروازه برگشت داده شد یادآور وضعیتیه که این تیم چهار سال قبل مقابل تیم اسپانیا داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23993" target="_blank">📅 17:05 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23992">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aexH20Kw9NDwPFiLiFN3BYod6gm_y2VV36kWaqWwkLlC1ubMr0vib7QuM8V5XkGxtc8LN9pcdF6Shlc-mhKXDiOWhbo5-Z6Mz8uMqT0Y7sHUEsGMZXYqnNQITQZzQFgmPqwogq_GkUq0VuXjmTdKiOs1TOOdgGltoOK7iOKfZqg5rPUp_qRzEjZrRu5T8BptjtOrRWotBS-vFU0DlUZ0ylmhWZoIU9LfRsbysPOvhUOyuIpQDiPIE2CJUFRWTH2Yb1gp-TwETM8asD6JA3NQq-rAFoWabIlz0PENJFNuhAzBvok8lOPscfwXqCF_gmruGbnNQ530WQyqGBmzdkl6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ وکیل ایتالیایی باشگاه استقلال به علی تاجرنیا رئیس هیات‌مدیره آبی‌پوشان اعلام کرده که فعالیت‌نقل‌وانتقالاتی خود را شروع کنند و دغدغه پنجره رونداشته باشند فیفا بزودی‌پنجره روباز میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23992" target="_blank">📅 17:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23991">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b889f1521d.mp4?token=SVPqrkcBmCakPjfFe2sCEdz6Dx2f6YaQtV9ECwwGpx9XoO2blST3m9m7JMUfnsUyx7_MX19AuqUAHUqmvZpSRZY6sU5WNIXmEqS1qb2_5-MfOOKJwDe49O3rAgn5BBCgM6dlFeiq_oZ3XpDTbrDc8UDdBB0wy26qtbejIF4t-8eN5pIV-KU74qoorhZqI3GU4RnDguST2E-L8Jtj1k0HDMO5eAyhaGxCuh2nRMBaNtQcAoFInYjtgpl2ajUjOwciAfg0Jwvgdetsrmrsxl3hkSa4ZY4x3uC5a2v23nnp8Q24qYazL1-AZJkgRv4fNfzKQN8VmU61dDk4LTpSKpouJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b889f1521d.mp4?token=SVPqrkcBmCakPjfFe2sCEdz6Dx2f6YaQtV9ECwwGpx9XoO2blST3m9m7JMUfnsUyx7_MX19AuqUAHUqmvZpSRZY6sU5WNIXmEqS1qb2_5-MfOOKJwDe49O3rAgn5BBCgM6dlFeiq_oZ3XpDTbrDc8UDdBB0wy26qtbejIF4t-8eN5pIV-KU74qoorhZqI3GU4RnDguST2E-L8Jtj1k0HDMO5eAyhaGxCuh2nRMBaNtQcAoFInYjtgpl2ajUjOwciAfg0Jwvgdetsrmrsxl3hkSa4ZY4x3uC5a2v23nnp8Q24qYazL1-AZJkgRv4fNfzKQN8VmU61dDk4LTpSKpouJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دهنت سرویس ابوطالب
؛ فیروز کریمی‌ رو دعوت کرده گذاشته رو دورتند آخرشم خدافظی کرد و تموم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23991" target="_blank">📅 16:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23990">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knhAfoLWfv6hQVmULIJofHxC9EG5qeF-F1ePHOwuYj8Z9-tOAJ_0O_wAxIT1mH6q7NF_Wq71FYCSfCK7p5bRDOT0ww2XYczma3cVxOymY6m-Z8R4rIl77Y_fDyO3hfm37mv4WjGjokTidWqP_rS_O7p-5bq_e1w14NiJjAWKwmmA0eorr0oymrWnTCKxu6tVhBsBc2iOtzGPP5MzAJjWo7o1PyOWnu6BFq8gAsO8bxE5bU1425lglCC7DKsKtn5V6a5Y77sncZvWjcnSsarMAdwgIJqThvZeNgWTao0f2hvvqSTYz1TY2suiClgMx7jCOj5bRWYJwQycd-R0UsgVmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
جی دی ونس معاون اول ترامپ:
باز شدن تنگه هرمز و پایان دادن به برنامه هسته‌‌ای ایران؛ این کارها قبلا انجام شدند! سوال اینه که ما اکنون چقدر می‌توانیم باهم به‌موفقیت برسیم. آیا میتونیم روابط درخاورمیانه را بطور دائم و همیشگی تغییر دهیم، یا به‌انجام کارها به روش‌قدیمی‌ برگردیم که ترجیح ما نیست‌ اما مطمئنا چیزیه که می‌تواند اتفاق بیفتد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23990" target="_blank">📅 16:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23989">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=gPv2b1v0cdxGUeZcHKs2kdlO3NSERYqAMq0EvkfbTVrvol8OpJbDT8wpg5jz6Bc9xDAV9JnUrjDiUp_RutDsf-tSMnO19POdoaOFCBwRTjBjGrlprZ__5oEghD_RnRqudPW45oK_IzDVQxUUfaaPgXGGq_qQzCvg8qsSpjQHVb3Ifp_E6czg5RgUM62-ki5X-1eZ1Hwd0B3TA2uvCqhFaFZ2dlHltlot3kpuecrs0MEdcQI8gpui6VmPgpsoUZQnt55-NhfMTxfu9YnZ3duRQcN19cXUmA6Vo_QE75XYE43UIzz63hQei-YYudd4EBWXRoqtSDRGPIIcb1Pr_k9Pcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c577c16fe.mp4?token=gPv2b1v0cdxGUeZcHKs2kdlO3NSERYqAMq0EvkfbTVrvol8OpJbDT8wpg5jz6Bc9xDAV9JnUrjDiUp_RutDsf-tSMnO19POdoaOFCBwRTjBjGrlprZ__5oEghD_RnRqudPW45oK_IzDVQxUUfaaPgXGGq_qQzCvg8qsSpjQHVb3Ifp_E6czg5RgUM62-ki5X-1eZ1Hwd0B3TA2uvCqhFaFZ2dlHltlot3kpuecrs0MEdcQI8gpui6VmPgpsoUZQnt55-NhfMTxfu9YnZ3duRQcN19cXUmA6Vo_QE75XYE43UIzz63hQei-YYudd4EBWXRoqtSDRGPIIcb1Pr_k9Pcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ساعت‌داوربازی پاراگوئه دزدیده شد!
در جریان یک مسابقه‌فوتبال درپاراگوئه یکی از بازیکنان، ساعت هوشمندداور راکه درگیرودار نیمه اول بر زمین افتاده بود، برداشت‌به‌مچ‌خود بست و  در نهایتاز زمین خارج شد.  بااین‌حال در نیمه دوم ساعت دوباره به مچ داور بازگشته بود، اما نحوه پس گرفتن آن مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23989" target="_blank">📅 16:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23988">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-iosI9_j1lYqQSFLpasWN5uO1vo5v6pbZRZmPa6JxzKFLFFGgQ5mwDwxCTP9oTWy-PtWu3JaCQ_iHXeYy8WQkotaBNkQtyz8aM3A8135kd-clHAM7QOqmlMKvgjx9DIWspUeXs26B4YQd_294RZtyorSfPNlvRhf8hj9eta4AqGdahAXKn0bh4DkDQZf7euLqWKsOjOqtzIaLKiJHJgomO8mZgC0fSjn0NdpJrd8JRSnLPsN0UHQ46FkB3DC_4MS4RoofWKUcXbtzMIQseqckqwhBqloxE6gHgdB26tH8NJHNu4oJPy-AdE4Up8AJKQGt-AEBORCJjuPs5-dmbaXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23988" target="_blank">📅 16:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23987">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k2rJODoFHETqmL9gEAr9qtbgX3k4nH4piDN6QbGEqBngu53oU-q7rwNJuDQUBId5l2gNt9n-7lm4huB5KfYxQrc7cdaLUIE1CzhfMLIgAPD03Pu8IcaohRKqVF5tdfcxFVEE65hmWqtD_XHHPYBKFs2gaCIiFdYiwcS6cdN_awp9gd4WBe_DLNmnh4YJ8ergM7IYBl9d-XU_L4b-ruY0oDJXckIaiulB22Pe28EpZR0otYgKyyg8HFFFvFrG3qWiE0ORZq6Sm5c1JjB5BvbNmH4NjZsyKVRD77PPa1sw0edCf5FTc358IBe_6LSFmA5fvETqYkR5avF6-YNmU8E1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه‌قدیمی کوکوریا در سال 2019: حاضرم موهام رو که علاقه زیادی بهشون دارم از ته بزنم ولی هیچوقت تحت هیچ شرایطی به رئال مادرید نروم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23987" target="_blank">📅 15:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23986">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=ZNIryQNZZZMmy5E_hkZcxEflTZ2_qjilDy_vNcEdDjfFxCrx2IKt5F9cSC3sI6MqUBvtEEPf88gAj6-_YMjzkOUmAaYGB0Q1ggn8s9KnNbqWOXryKKVD8tFgtRirQRONfIZ83-CYWt6J-YptwUvCdP3cQT_KpVbtYnZhULzvShu3mntatW6r_Xe7YdW99vfHC1jZnVsQydq8UUxYQNGKvZqEIXWWWZJNSMiOhbE651NmEmxYqTolAaKtmBb8NazxZKoNx8rr-SsXy6c16wKYPydNmdCJfsL0kZBrtlbIx_JTJbqzQJhpZayV1tGF464_cHmPmNHSjEBtvBCJiKGROg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8dba54f8d.mp4?token=ZNIryQNZZZMmy5E_hkZcxEflTZ2_qjilDy_vNcEdDjfFxCrx2IKt5F9cSC3sI6MqUBvtEEPf88gAj6-_YMjzkOUmAaYGB0Q1ggn8s9KnNbqWOXryKKVD8tFgtRirQRONfIZ83-CYWt6J-YptwUvCdP3cQT_KpVbtYnZhULzvShu3mntatW6r_Xe7YdW99vfHC1jZnVsQydq8UUxYQNGKvZqEIXWWWZJNSMiOhbE651NmEmxYqTolAaKtmBb8NazxZKoNx8rr-SsXy6c16wKYPydNmdCJfsL0kZBrtlbIx_JTJbqzQJhpZayV1tGF464_cHmPmNHSjEBtvBCJiKGROg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سرهنگ علیفر: از اونجااصلا نمیشه گل‌زد؛ واکنش صادقانه آیاسه یوئدا بازیکن ژاپن به علیفر
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23986" target="_blank">📅 15:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23985">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRVXQon3OYOcdzuv7VdFp0dzaaXAjR4-1RFk8mf47KPS1bAv_MauWd0DaW_jVSX34V7ZO3sODAwJ0kORAiezE7Y4uySvY7mHZf47UZM6HYaEBPGNpx5t-ZFssw5wcstzz1vFAWcJgeEG8N8am6efhIafTJufliwH_jsFfYRL1hD5v65dp5OyEb9enE0OIFGoPsR7a_RpNDx_XVioATuLkTyvGfnJVlLrQGZFHioD3nGqae7XhsxkW_PCeF7h4sYX2q04Vpm6SG7tr77w9HEGX1z-Ug6MzvzMLsfZlqLupv2s8LXeMBREw4Gk9vUf5LP1WaLWqhFrxc1aRxA2lb937A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم جام جهانی 2026؛ آتش بازی سامورائی ها مقابل شاگردان هروه رنار + جدول رده بندی گروه F در پایان هفته دوم رقابت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23985" target="_blank">📅 15:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23984">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=eAVaKbjPE5fPhFUPA4AukY0OOXaeme7KIB2wY6OdXNgX9sg-mhXuw74soamNmQT9GfK89sHqCsLYCHDQRGB6kz4BU9nWeT4wtHYTGvHQBHu5ykTFC8nb2a1uz2Ck9bYo801oSLuas5s6UVvPhlBFiOMUED0bPOkApeafjXkERxPVeMm3bCaaHEGahVUwWSn4VXUjOj0ElUrsNCy_cGCbigmuPzcFdwmy86DepfwSPNPR5nfk9QdPpJ-sas9giqbboAExN6xB4LZxia9ghl62-vZkBf_P38NEehpagU0jKohXQau4SHaeGXMSKhKItoTtOouto5a2PetiJ2aD1Tux3QFJjZZw8UjBiPhJMROs-8vG4sdsXLxx-8_YKUi585bJVZ7JdclaxC2fQt5dDbvnNTQzhkIu44ZQggQLi4Vs-Uu8Csse5Ic6za0gyBaoO81KiHKJuCBDXK8l02DzKORt_ZUJkZYKsWTbeXLmLa_qi2gJ3ckeJ_w9b8VLiKMwOz64ND42t4XwmpufBUXnXce-8LZL7qQ0tvp8pSWgFaFTO7PJAp53ZC46gR3czme_5P5lFlbYC2HzNtBfCiHUB3oo--eCApA88mw6RLEKe42S8NjZGuA8k91TGSK8koI0Uv0Sn3uApbNb8gS4igRnAEC9OosddV1mwhPpdktR85JAnsM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4e6bc8b00.mp4?token=eAVaKbjPE5fPhFUPA4AukY0OOXaeme7KIB2wY6OdXNgX9sg-mhXuw74soamNmQT9GfK89sHqCsLYCHDQRGB6kz4BU9nWeT4wtHYTGvHQBHu5ykTFC8nb2a1uz2Ck9bYo801oSLuas5s6UVvPhlBFiOMUED0bPOkApeafjXkERxPVeMm3bCaaHEGahVUwWSn4VXUjOj0ElUrsNCy_cGCbigmuPzcFdwmy86DepfwSPNPR5nfk9QdPpJ-sas9giqbboAExN6xB4LZxia9ghl62-vZkBf_P38NEehpagU0jKohXQau4SHaeGXMSKhKItoTtOouto5a2PetiJ2aD1Tux3QFJjZZw8UjBiPhJMROs-8vG4sdsXLxx-8_YKUi585bJVZ7JdclaxC2fQt5dDbvnNTQzhkIu44ZQggQLi4Vs-Uu8Csse5Ic6za0gyBaoO81KiHKJuCBDXK8l02DzKORt_ZUJkZYKsWTbeXLmLa_qi2gJ3ckeJ_w9b8VLiKMwOz64ND42t4XwmpufBUXnXce-8LZL7qQ0tvp8pSWgFaFTO7PJAp53ZC46gR3czme_5P5lFlbYC2HzNtBfCiHUB3oo--eCApA88mw6RLEKe42S8NjZGuA8k91TGSK8koI0Uv0Sn3uApbNb8gS4igRnAEC9OosddV1mwhPpdktR85JAnsM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرمصدوم‌شدن‌کورتوا کذب‌محضه‌اسکای اسپورت همچین‌خبری روکارنکرده ولی باتوجه به فعالیت‌های دعانویس ژنرال‌ممکنه‌یک‌ساعت دیگه خبر بیا کورتوا و دیبروینه سر صبحونه کینه های قدیمی رو دوباره کشیدن وسط و سر دختر دعواشون شد و گارسیا به دلیل‌مسائل اخلاقی‌اونارو ازبازی‌کنار گذاشت. ویدیو بازکنید متوجه منظورمون از کینه قدیمی میشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23984" target="_blank">📅 15:24 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23983">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=BHJdSEXnBDbfN_OHu542NpNucWBVdEdqZW5TXmM_jmlU0oCdUizHan2uBYXh7XA629nNlLC1Ksd23gdHL_Fk1faFFxYlnk1EsCwgv53Xg2hKg5UheNIByFVs_cape-GULlIdROQmetUZQi6iayfXrbipXNVx85sI9zuIs3VfsrNE1VVUUyHY6yuFGKC5CU-0X4FNu_gbY8Ul0cOnslFzRyLnMcjcKOW3WW9F-0UhOHr6wQW-zXVlb-pGv3Nb8vZwVqwq5Wiv5T714Dp1GRI4wwVSc-cF4X58hnXpO01PAzsKfHsQUJP5KABkJ6Pl3-DVZ6unQoGJ_QSZDxdkGPp9GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc33af7706.mp4?token=BHJdSEXnBDbfN_OHu542NpNucWBVdEdqZW5TXmM_jmlU0oCdUizHan2uBYXh7XA629nNlLC1Ksd23gdHL_Fk1faFFxYlnk1EsCwgv53Xg2hKg5UheNIByFVs_cape-GULlIdROQmetUZQi6iayfXrbipXNVx85sI9zuIs3VfsrNE1VVUUyHY6yuFGKC5CU-0X4FNu_gbY8Ul0cOnslFzRyLnMcjcKOW3WW9F-0UhOHr6wQW-zXVlb-pGv3Nb8vZwVqwq5Wiv5T714Dp1GRI4wwVSc-cF4X58hnXpO01PAzsKfHsQUJP5KABkJ6Pl3-DVZ6unQoGJ_QSZDxdkGPp9GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
#نقل‌انتقالات|اسماعیل‌ سایبری هافبک تهاجمی جوان مراکش‌باعقدقراردادی 5 ساله به بایرن مونیخ پیوست. هزینه انتقال 55 میلیون یورو اعلام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23983" target="_blank">📅 15:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23982">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=v06GCRFt6nv9s0K1hGKQRMXQhblWbQ9KCy1zDVa1xlCp-4RmzqIYn5niCDIdoJEFFnB-mu5DQpjbbOi8v9PAuYjLIDRVAXzs8sz3MKuqveB5qcbx-LUtzWphWwp_ffYpVrvv7WL2jQm8_SD1cgu8QpAVDjGSZVrhiKsd2beOysUBQ0LtK8myfGzsORZXul122PriIBa79gSz3unfs19NDiKWYJtRkTMQU1YwoROCaZZivaSEKabMwJDw2f7LdLUP3O38yAqySqappR8LqY5vs-lMVb7LoCpVG4IDhs2ir5WORVwE2MCl7_fZa3KSZrwe4SNHFI1rqprcmZPGeHMYZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eba240be.mp4?token=v06GCRFt6nv9s0K1hGKQRMXQhblWbQ9KCy1zDVa1xlCp-4RmzqIYn5niCDIdoJEFFnB-mu5DQpjbbOi8v9PAuYjLIDRVAXzs8sz3MKuqveB5qcbx-LUtzWphWwp_ffYpVrvv7WL2jQm8_SD1cgu8QpAVDjGSZVrhiKsd2beOysUBQ0LtK8myfGzsORZXul122PriIBa79gSz3unfs19NDiKWYJtRkTMQU1YwoROCaZZivaSEKabMwJDw2f7LdLUP3O38yAqySqappR8LqY5vs-lMVb7LoCpVG4IDhs2ir5WORVwE2MCl7_fZa3KSZrwe4SNHFI1rqprcmZPGeHMYZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
50 ثانیه از دیوانه کردن خداداد عزیزی توسط جواد خیابانی در ویژه‌برنامه‌روزای‌اخیر جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23982" target="_blank">📅 14:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23981">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxHtyRmACrTZnZsM-3ZmJaPWiNQxoAet3QadLqQugRvcu53Hl84O84kRtjmsu2cLWYNIehRZ7ql4Lfa6wGuMoryzoQ3Opg2Cv6_fP68epKNLU3uZyTRhJP1wDe0ZSapE3speL0mWJO7JQsnCeX_2eFP8oV_j-SIhpwoe57-7D1D55yiSgRcxbShxNXgiNEZO9zdIomSTvRE78HsmA2AEW2UMgWK-GIndsbxSwSpICaf6Fak7NK7JdQypIo4l-TU9uUYY5rX91qzUHTJeN4zaQ4mC3AjNnF7c_HKTiuDVCzAwOxxQEVhAJTzsBhnMcLomHwuG8jYgt4qPCraetlgplA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌ بختیاری‌زاده سرمربی جدید استقلال امروز صبح باحضور در ساختمان این باشگاه قراردادش رو با آبی پوشان پایتخت به مدت دو فصل امضاکرد. بختیاری‌زاده‌درباره تقویت کادرفنی و جذب بازیکنان مدنظر نیز گفتگویی مفصل با تاجرنیا داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23981" target="_blank">📅 14:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23980">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYleFWS1mD7xQ0FoEMZ_HmZA1vQJXcNYwKOSoocBZdsUhmGuw3Gc4wcwWCqIg8Lmc1wzNwXzoFg8VyzeIJmeb01OCEEVIAa1qFFOI4drPJWztBZ8N0q9sAr0m8cBqG1ThLRC7gilodPNqTHOw67gXlVqSfVNS7E6YB0uli7WBjuQokFSYGDOqneNMJ5-mft11h-Qc9JdvI3sLWlj_ytHx459dn8f513A1XEbv1CZ0LCBxY7UJx6Zw6qnmfqT1M_AlHkVYL553nVxLrdgCvjvg6x5jQOvMGEQM-IW1-W42Hfj9Gxh0RdnrdoBhDog7kUQu_eXmyw1fr3VNVbnIT1GgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ تاجرنیا امروز صبح در تماس با سهراب بختیاری زاده سرمربی جدید استقلال گفته درصورت موافقت او سریعا با گابریل پین قرارداد امضا خواهد کرد. بختیاری‌زاده علاقمند به مربیان ترکیه‌ای است و احتمال داره دستیار دومش هم اهل این کشور باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23980" target="_blank">📅 14:13 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23979">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ci9au6pUkMcaaUP1oBje8zP0hiaM1T0GCpZazGpmgzfF2uBT4OAKs5hVBM73qNM7iB54XM4XRJLlBnRErrwcB1vPv579DN45TStydGm2odVwwPjTrSatH12NlekRVaiwnZYzgEBNDqQVP6QBg_Y7PsvBY230rV7ABRtzzMur4UAv--hDbrLEgTnTH_L1d9IPtWrzl0uA_cuvuoKdj35i69qxd4XvMRKXhjsE-5A_JJ1sP8HbVvE0k21chQHe60Ayn6W_o8cBV1Lu44cK5uh5BPVZhNCvUGxUSLjPIpG7dWIkLZDye38tw0zC8HlJl7Zm5s9eqSOCA-P_E3VquxxeOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ باتوجه‌به‌تعدادسوالات زیادی که درباره آخرین وضعیت نیمکت‌پرسپولیس پرسیدین لازمه در این باره به یه جمع بندی برسیم؛ امروز پرسپولیس با اسکوچیچ مذاکرات نهایی روانجام‌میده اگه به توافق کامل‌برسند بر سرجزئیات قرارداد امضا میشه اگه به توافق نرسند اوسمار…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23979" target="_blank">📅 14:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23978">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=c87tO-1jxQmLIvMvZ5zOJYgyZSMfDfQbFYtmiUNgnEBkli12SBpiLqwNjvalnzWtkLeerLBzhFjTC7OF9fAu74IfMevbDjDAjFvdUvFKR3dd2a9iR5jQ3T1r5qbSsGKLbaGL_qxZZxG8_ptI7FbaIbQRv7eqMCd0TsOoC_7YyzpS8oy8d1hPGFOeWnw1zVah6_NWfrJZoEdpZyRCYF-VtjGrDs0VRSezbwzrdwRfyXViWW4ktPNNuhfOnesvoKfjs4pfCJfzKvfq7LSKIOUeFOBwPU6A5fd37gG_pItpSz7SwrHJ8R5ms5T0-QgkXvUIEFO-HnrcI-9dsiAT7Z_63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9df1a6812.mp4?token=c87tO-1jxQmLIvMvZ5zOJYgyZSMfDfQbFYtmiUNgnEBkli12SBpiLqwNjvalnzWtkLeerLBzhFjTC7OF9fAu74IfMevbDjDAjFvdUvFKR3dd2a9iR5jQ3T1r5qbSsGKLbaGL_qxZZxG8_ptI7FbaIbQRv7eqMCd0TsOoC_7YyzpS8oy8d1hPGFOeWnw1zVah6_NWfrJZoEdpZyRCYF-VtjGrDs0VRSezbwzrdwRfyXViWW4ktPNNuhfOnesvoKfjs4pfCJfzKvfq7LSKIOUeFOBwPU6A5fd37gG_pItpSz7SwrHJ8R5ms5T0-QgkXvUIEFO-HnrcI-9dsiAT7Z_63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
هاجیمه موریاسو سرمربی تیم ملی ژاپن با دیدن هری کین کاپیتان تیم ملی انگلیس فورا تبدیل به یکی از هواداراش میشه و باهاش سلفی میگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23978" target="_blank">📅 13:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23977">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDqYLVdGXT3pSRjhOU7udaDirDbX669g8wZPvZfw0pWgu2r30gwCx93L0PZA75AfR5WR8rscHBmz2Z3aCqVhPJiVLuRWGsBwIOZ5qa6k9wMPeZJTLoMtyiR7Ki5a2_GLBhV6_5dwsNLaBb8oJlRFvoGWyJiQ9kf_HtEJEgsEh1PMDcLh1brKgqVQ7i5rQgjnj04GCivFXFQRm1qjAJFtbrpC-C1-dVhZUtUladqnjdGKXEBqLp24fshxsSGegWb2D-kaopv1iDSCce1wnolgS6CuSv0E1FOr1HgngzzxVgSX8acDXaJQUXa2km7RhlfIh64Tn1mvZZ59AqLypXUwGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه‌رسمی‌تیم‌ملی‌بلژیک: آقای قلعه نویی عزیز دعانویست‌رو از تیم بکش‌بیرون‌. ما اصلا با شما بازی نمیکنیم سه امتیاز بازی‌برای‌شما. تک تک بازیکنانمون رو به دلیل مصدومیت داریم از دست میدیم.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23977" target="_blank">📅 13:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23976">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXj1r_qcru0yOfVqBagox-o8AAgCkjrNDuxV4nRRyyz1do-FATEorBmiAjgmFQ6vd5SPgKn5aAALlREQRaD7ts6sUyZO2W7lCazq5CmADOcVcdfZrxr4ODWuXAaz-rCUvLWnnfWi-rKX00244DPQpPYufpYvUmx0z6wDl-F5SeB6Ni79cGdi_0aWY8UZh92DH8XDV2ajPxbegjEy9qzqHScV3z1AI5dtEhO4w1udk_wwT_Zpry7Yd7n7pZKLbisqnEtDR0JiPiB8eK_NiOToY15Ywh9gl0pW0kajZb696YV_3hPikl86pMdicbRSNlZbZIzTLSbkifpxcrg0Lb4jrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ مگه‌میشه؟! رسانه‌معتبر اسپورت بلژیک گفته لئاندرو ترسارد ازناحیه‌کتف‌احساس دردمیکنه و ممکنه دربازی‌امشب‌مقابل ایران فیکس به میدان نره. پزشکان بلژیک در تلاشن او رو به این بازی برسونند. تروسارد جانشین جرمی دوکو مصدوم شده بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23976" target="_blank">📅 13:26 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23975">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUNDGtx_Ynktybs_KgggrmgHikbK3yyhZoWHg_KRwjZJUc4FEZbMT9AIUn2F5wna5eH3JZ-qaHqRq1evXqr64AtsAcdR9Jvzw7VLp1UtgjF5bY7f-_fi_oqg9CPHZ4RHRBdlgb-NcyITT7DEIwCr7l2vtajyGXemYZ0sCQkbT6PPvmvDGV2y3_j1AZATS_AuJtHArBaINySw8jSGoabNc1jO1AaLMLXosCfjFXJCGUrCey3XarVcUaTRtAGfKQcgpFEtmPcKx4ybKiDx0U816hwhoYuB_fLpjEWmsCPvpDJHz-I2YIw6TQQKvH9NUcAxHfGZx64RQPcV_q0EO9iaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌پرشیاناازباشگاه پرسپولیس؛ امروز ساعت 14:00 جلسه نهایی مدیر عامل باشگاه پرسپولیس بادراگان‌اسکوچیچ و نماینده‌اش در ترکیه برگزار خواهد شد. باتوجه به مذاکرات مثبت روزهای اخیر انتظار میرود امروز قرارداد رسمی بین طرفین امضا شود و اسکوچیچ بزودی راهی…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23975" target="_blank">📅 13:18 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23974">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKDjTwBocb23KBDIIiEitiCpDU1o67bWw_LCvwFPuCohb1Ga6WDsWq_XGvbdcksXjVtis18kQqlM4EIHUoK3cO_oslSHTkxDQBqBcrlTb8nJ4Wk1qTA7s6t-OQSZABHZlg6fCz5zou66mYl0Ourr2WGqioz-enl7DkWfXw1oj-847l4zFVF8oMxw2JAsFKcxd6wcOoHr331MHIwgDSpiSuS1ivDUe9bWPYlGgw7JEgn_W_8aoNf7emDgumRahOD01jf9BYdm9rHg2HHLsiXv4dBpvD7wf-_sVx5LAjAi0TJriX4M23P3I3TkPrR58xngwjXfT0e4s3cTZpetFZjCMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی‌پرشیانا؛ با اعلام فدراسیون فوتبال رقابت‌های‌فصل‌اینده‌لیگ‌برتر 18 تیمی خواهد بود. هیچ تیمی سقوط نخواهد کرد و دو تیم از لیگ ازادگان نیز به رقابت های لیگ برتر خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23974" target="_blank">📅 13:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23973">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=R-ZJmI-_W4XTf_qk8LdIVRE-YfvuvPwibHLyLJq2wxUaEgyXxzpyHxWXBFWXE69w06y_wzaYS84ZUkBLI2eA7K-R6IJISNrpO_2sxmXNbnoLirBtjxBa5mptN1diwIHM3OxxT7omMzqJYIIuMjVzAE-LOGOI-dNeiCnn9QkSQUsMvh4IMf58_kS3x0vON-7Ow2COowPXAYh0ae2fe-zQIri7Fv1PwpaMnAzxc6hAzyVpycbyz9NBnGMuNAuW1ALQq65X8UTYXXBei1tZGlbcvsIrvSl6TraTqLd9k01RqrwGoceqTta0FMp0qaiakq_QvwGERfga2BpB5NmIb6iQaX01mpmlQkqtAntjIkLIT8Uf7T5LKea2Zj8SLmTyb0chLyl5QvleIY-E8QgX-N9E6TZpA8T1PptxbG5sdoCEzDD_4E14n6NLAVzmxT3ZWG5YnFS5Yhoqlqvhu9jUVUbT5gLfRB6esC2iaQaWu1o2hdAtHb-gAPACGrRVuf0xuZXEw6dxuk2k9a7eX9mNQKPLtL3EcCpcAwG_UVMI7fA1YVO-I4rR7FwZJH9arE0l6Gebnq4ieQtjC2F0hc8-OvsW1-ui6FN_KVkiH_oceEpxoyUzKLI-ieG2jIzrQxBdwbbXNP6mL1SQS6FYiF80cHq2DPAiJDC6UPqEp1UJWrHCDkk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/415bb37d05.mp4?token=R-ZJmI-_W4XTf_qk8LdIVRE-YfvuvPwibHLyLJq2wxUaEgyXxzpyHxWXBFWXE69w06y_wzaYS84ZUkBLI2eA7K-R6IJISNrpO_2sxmXNbnoLirBtjxBa5mptN1diwIHM3OxxT7omMzqJYIIuMjVzAE-LOGOI-dNeiCnn9QkSQUsMvh4IMf58_kS3x0vON-7Ow2COowPXAYh0ae2fe-zQIri7Fv1PwpaMnAzxc6hAzyVpycbyz9NBnGMuNAuW1ALQq65X8UTYXXBei1tZGlbcvsIrvSl6TraTqLd9k01RqrwGoceqTta0FMp0qaiakq_QvwGERfga2BpB5NmIb6iQaX01mpmlQkqtAntjIkLIT8Uf7T5LKea2Zj8SLmTyb0chLyl5QvleIY-E8QgX-N9E6TZpA8T1PptxbG5sdoCEzDD_4E14n6NLAVzmxT3ZWG5YnFS5Yhoqlqvhu9jUVUbT5gLfRB6esC2iaQaWu1o2hdAtHb-gAPACGrRVuf0xuZXEw6dxuk2k9a7eX9mNQKPLtL3EcCpcAwG_UVMI7fA1YVO-I4rR7FwZJH9arE0l6Gebnq4ieQtjC2F0hc8-OvsW1-ui6FN_KVkiH_oceEpxoyUzKLI-ieG2jIzrQxBdwbbXNP6mL1SQS6FYiF80cHq2DPAiJDC6UPqEp1UJWrHCDkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ماجرای جالب آشنا شدن اوسمار ویرا سرمربی فعلی سرخ‌ها باسنگربان برزیل‌ و لیورپول؛
پسربچه هفت‌ساله‌وتپلی‌که حالا یکی از بهترین‌های دنیا شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23973" target="_blank">📅 12:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23972">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KywvR6PFCeyHV8POwYbBKsL3bZKXfJHBeHK77W46SoRg75vF-EApTua5TkB-zujTRwi8LmbS41sx7F-lNfL2Yu_cmESqgYaQqUEoE2q_S50CLvXKM9S1myozMJTxY86_SuYR1oSa24FrL7pyZlixM6EDaCArxFo-g8fSEv-fsHCE66qW4ZgAUYVo2oX5V8GTGViibJ1fkvtUk_vpYz7k3zrr3kuTBkbwgXJNqavM_MimEdVc3LtUh8DsLR7bEreQxzg8QYhHnKBoqF9qqWhfI-LsKzL8yLLXlZz9fl2cWmgpBgBhoibUeeKbL6NdVE6U3Y_NhAir6g-PE3e2Sqdp9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکوردداران‌کمترین‌درصد مالکیت توپ در یک بازی جام جهانی؛
پاراگوئه با مالکیت ۲۱ درصدی در بازی با ترکیه، در رده هفتم کمترین میزان مالکیت توپ در یک بازی جام جهانی قرار گرفت.
‼️
ایران با ۳ بازی، تنها تیمیه که بیش از یک بار در جدول کمترین میزان مالکیت توپ قرار گرفته است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23972" target="_blank">📅 12:38 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23971">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqG74qPbPBBQnOw5qMPN-5KpeDfnLdu_Xk52_BJgNmbwKDx5FPDSTH-fJf8pVIoIFIvAeAZ7LB9ZW0za3nKGD7CCncpiNx5jgVd0TS5AV4WoUcXfuP-MWjlc5WmPdKTdcgEOfkDQ1kou47_vdgX4dLpeeZg2mlTcVlSjePVU0PKEHUBxsWR95wW9bmBiKgAm7v-jzYpPSEF-O9vu6Bsw03FevZMcyQ3i6lmq-9oW4RFfQkVzsLinmDZmzAZ9OZAM2V7XvJ-_OA42V7Sumyv8gNGWppXDgW8Ka9BDQ4oDy0JQLycRpiBfOKaiIvcBW8N3JMTeAe9CZr9No6o2G4R5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
فوق‌ستاره‌های‌فوتبال‌جهان بابیشترین تعداد فالور در اینستاگرام؛ کریس رونالدو با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23971" target="_blank">📅 12:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23970">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MBp4HN_oN5W5Ez-_olZOyXZkeP7Wpd-pHJ-ds1QollBv_jR_ambycYBVF1-fdf1QsBPyPbW4P366iF5p0fksWHRipRQoxU8PdkfGIGB66w9b6tI_J0BK2mc4ZE0Ry0w0H3F9PTtJPnaJTCNRpUl8mdOodQSc_8QYc9DzUHtHJLFP4gK93CbW_h2JS3EWi-1wvoMj26ZBpiHcvkIPJqMAj_8RgE1GeosZuIgwJ_l0BNhKeYl2H7Rr0F9GwCj0PdHEUgpHT1KrTkAX73KeuevgyCdgDL7Xqcq8mDA9iu0FECdzqIsIblSRez6dX9tFmJJRgic6m1PcObXh9VlTSWS8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23970" target="_blank">📅 12:04 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
