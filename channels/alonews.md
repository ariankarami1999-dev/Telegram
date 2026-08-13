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
<img src="https://cdn4.telesco.pe/file/Vtct5wxYmIQrzi7qus3NG2rIQnYQ-ge9PcgR1DTO9Q98lShMqILHygY7232Jo7oYwOEr3pab3uWTVwvFt83WSxNUvSIBNcJSnuYIwJQUuuYafXQkIGOXqjX2m1MbqF6UN5knUU1SIH32h9FoTJWD6cMa8cAx2l_DZxxRFb7Ye_2ZaAfacDKPCzTrm0w74Q6Eo7JtbzDvkztrAVYb5t96hjfFc1v-roHzPXx5gAUIdM468jBMgGDfL9a8mlFOymx5zJ29jj_2aSzZxiNtNgB7W7rUkXl1ZLV_Yv1vEbOHldEVdJ0KejZy1fzhnwVeiNQyWDqAUC-IFWwXFWvprPCS5g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 965K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 01:05:39</div>
<hr>

<div class="tg-post" id="msg-141572">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82036588a4.mp4?token=S08FXNmz1rmrlEXTqzR4oQFJOpFi7LtycHEfSvx2yyTWUVydHpZfmiDU-KrDE7atKPPl4G0y3vt7Tg8D76jBCYCTtdH9ETkfb_Vc4fHrS6IhDI8-kPlpqlvpb-2-Lpf0dQQySeLGG1RmbHKDLf_4IU_cAWvijyutNvhhsvkz70McyOm_eCG-hgMeKAuWjT8hCiJdWetjhNFDs32hTrqg1jbShCg8zIms5Ixc-dXmqIjg5Neus0Fx2E1HkW1qNsjzRjJMixGnTefn-eHFinSfPLkHkTHzwmTKB6lmmv-A69pWCVx4kO5uf1qKPvfcAAFhz9svhP7Ub6ccpSI8zFsg6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82036588a4.mp4?token=S08FXNmz1rmrlEXTqzR4oQFJOpFi7LtycHEfSvx2yyTWUVydHpZfmiDU-KrDE7atKPPl4G0y3vt7Tg8D76jBCYCTtdH9ETkfb_Vc4fHrS6IhDI8-kPlpqlvpb-2-Lpf0dQQySeLGG1RmbHKDLf_4IU_cAWvijyutNvhhsvkz70McyOm_eCG-hgMeKAuWjT8hCiJdWetjhNFDs32hTrqg1jbShCg8zIms5Ixc-dXmqIjg5Neus0Fx2E1HkW1qNsjzRjJMixGnTefn-eHFinSfPLkHkTHzwmTKB6lmmv-A69pWCVx4kO5uf1qKPvfcAAFhz9svhP7Ub6ccpSI8zFsg6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیش بینی عجیب مرحوم روح الله زم
🔴
یه سناریو طراحی شده که آمریکا به ایران حمله کنه و ایران هم تو منطقه بزنه پدر آمریکا و عربا رو دربیاره و قدرت خودش تو منطقه تثبیت بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/alonews/141572" target="_blank">📅 00:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141571">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRKBIZOxQFkA7oc_KGCZM6QbqGHOz0m9KS8yFkFxK6uJur0ChnfoWUEcAavVa9l7St9bGf4Z36vS9Yrz3Z2SfpmA7viUiU1HQ5kLkZD2qX5NctAbTdvB25FUQ3IJg2fJpxT2LaDu7iWyk9BTg1_Anq6CQw_midgL3qFqwNafKKw9oWUwV0xzhGWYSifwZDqm108zGke8jG4ulHdh43zE8Nc4mGh-IwnkUyQ2FjtRiQfkIv7ueaz1IUAs8ragoXAqHaH3lsJgc6tt0sfjvVt9T8kRHESp7Duna6VG8-gLKmfL3lVX0Lc1lXDdRfVQt5y5R6BHQY5qxGf5DZO9geinSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: دو مرجع مهم تصمیم گیر در خصوص بنزین اختلاف نظر دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/141571" target="_blank">📅 00:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141570">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be651093e6.mp4?token=GHK29jHfPNGCjgt-IC09S063gevyHHI1BjAzuY6TTlTu1KB_IySPkJD2NFWF7ul4m4S3H-gzi4Ak_6ateibqc3zyAk3UNrJkvdXKEObsPHCPYUUiT1o8FWx8AN5RXZ4H4R2O5RZuS4XtwXT2cQXwHY97umfWtR59IMHjZFYpk6WUH_-fgO9Nbxq0QRwBEPt90uDjnHt0vzWsKAItVHMpwp8hwN3BY7a9M8LQ1b5HAanVprj34tfV1ISEhcEYOo1nA6IDJk3QMx_ihCjAzImIwTpk_9Q8_tY3niWJ1OlFM0x8Y7nIqDPcVcCOo3aZmI11qJX2_rwA3krB-ssy8sRAnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be651093e6.mp4?token=GHK29jHfPNGCjgt-IC09S063gevyHHI1BjAzuY6TTlTu1KB_IySPkJD2NFWF7ul4m4S3H-gzi4Ak_6ateibqc3zyAk3UNrJkvdXKEObsPHCPYUUiT1o8FWx8AN5RXZ4H4R2O5RZuS4XtwXT2cQXwHY97umfWtR59IMHjZFYpk6WUH_-fgO9Nbxq0QRwBEPt90uDjnHt0vzWsKAItVHMpwp8hwN3BY7a9M8LQ1b5HAanVprj34tfV1ISEhcEYOo1nA6IDJk3QMx_ihCjAzImIwTpk_9Q8_tY3niWJ1OlFM0x8Y7nIqDPcVcCOo3aZmI11qJX2_rwA3krB-ssy8sRAnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس در مورد ایران:
قیمت نفت امروز در مقایسه با روزهای اولیه درگیری به شدت کاهش یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/141570" target="_blank">📅 00:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141569">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
سی‌ان‌ان:
مشکلات ترامپ در رابطه با ایران در حال تشدید است و در بحبوحه پیچیدگی‌های فزاینده درباره جنگ و تحولات مرتبط با آن، وضعیت دشوارتر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/141569" target="_blank">📅 00:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141568">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFDLSZyXs4d1Hsfh6om0MGJyADZO4MxDoR5RrbaRjnC36_9zVrbTyNWo8IPxJZ8_41nOK4qvdqlazVSAertVsRzDeAp51BhbyMtiKPrCye4niZSaFmnkx6siUDg-0a_6v14Fp-OHvMZOu38S6SeMcQ9rsTf2DJLCGRvKaxJUDZz1BwUnmiNgGLBILNE__pFEVBv1HWcvEGi8CbekpHxc4iHuDJkpofi1j4tJeORP3MefzcP4og-uP41x8hzqIwkn2I3eWq1-xrqKp0f0z1pp_DTPj8mAu1bNyDJRRj8poOERlRjMlhYZeazYcSj3sD9VX-NiwoYOovadSqtXXrZh0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه رستوران توی کیش، تمام نوشیدنی هارو فقط برای خانما رایگان کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/141568" target="_blank">📅 00:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141567">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
معاون رئیس جمهور آمریکا: من کاملاً مطمئن هستم که این بحران با تقویت موضع آمریکا و جلوگیری از دستیابی ایران به سلاح هسته ای پایان خواهد یافت
🔴
بازگرداندن ثبات به تنگه هرمز، ثبات قیمت نفت و گاز را برای مردم آمریکا تضمین خواهد کرد.
🔴
مشکل این است که ایرانی‌ها وعده‌هایی می‌دهند که به آنها عمل نمی‌کنند و توافقاتی می‌کنند که بعداً از انجام آنها سر باز می‌زنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/141567" target="_blank">📅 23:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141566">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
جروزالم پست: مقامات دفاعی اسرائیل از سرعت بازیابی توان نظامی ایران پس از جنگ، شوکه شدند. ارتش اسرائیل اکنون شاهد تحولی سریع در قابلیت‌های تولید موشک‌های بالستیک ایران است.
🔴
بر اساس این گزارش، خسارت واردشده به صنایع دفاعی ایران به جای چند سال، تنها فعالیت این بخش را برای چند ماه عقب انداخته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/141566" target="_blank">📅 23:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141565">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92209cf4a.mp4?token=ubZQFzu7QVl7ovb5_k-I4FtzEY0cxTW2t2OIAIoUXVLkc7Qo0UzMfD2c72IkhLI4S1XSL_uXz6ocv2QPTdXnAUDcEUaM8B1GwD65CkHE7t-mdDSi8d1wNGj7xgujSaXAl3rAYkqdY2iwXyEsArZPeYeIvtCn0f1VPgzCd04j6w8-3_0MiN4AtKosdUMmQ73yrPRgW8Raz3t1RzfTOmjQNQW7m27_69PSQUcrHiEZxZGMT7QljMV9M3x5AJXAcfvEhq4sWXxDuDuS2p7Rh-56y1ye7TWACCo8gQDOXOjax5HWfZQ4lJhNipTAbfWgF1E6KigKHa9o83qwDoPNgaGSJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92209cf4a.mp4?token=ubZQFzu7QVl7ovb5_k-I4FtzEY0cxTW2t2OIAIoUXVLkc7Qo0UzMfD2c72IkhLI4S1XSL_uXz6ocv2QPTdXnAUDcEUaM8B1GwD65CkHE7t-mdDSi8d1wNGj7xgujSaXAl3rAYkqdY2iwXyEsArZPeYeIvtCn0f1VPgzCd04j6w8-3_0MiN4AtKosdUMmQ73yrPRgW8Raz3t1RzfTOmjQNQW7m27_69PSQUcrHiEZxZGMT7QljMV9M3x5AJXAcfvEhq4sWXxDuDuS2p7Rh-56y1ye7TWACCo8gQDOXOjax5HWfZQ4lJhNipTAbfWgF1E6KigKHa9o83qwDoPNgaGSJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای خبر بنزین 87 هزارتومانی و سپس عقب نشینی دولت به زبان ساده از مهران مدیری در سریال هیولا
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/141565" target="_blank">📅 23:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141564">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/141564" target="_blank">📅 23:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141563">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f229500ca2.mp4?token=ikxxCXXAwZ507opukdCrAmoy1mwoc5IC6nTYiyNBw2av3CAJhjo6La4gO8pLRM3p0OHpHF9gwjkE2QAnahplX1exkKTO1nxCbtHEzQLlaE7fK6xcS5yWpiIss-ZLZgAqAA2UeIa7cPeBLX7EytCJJlL9mKogojtwDcUf4adhyND9XEnE_Tr8dasjzxLQV-u2arxeMeMrDYf9rov7t35YufocJt8hp9Xg9TSedeyqsHUKj4pHcEvwHT14OJ47rCsKcMXbupVnAp5QFF0v0IwqixXbEW_XufRWGg92-JoczembY8MsloOyulB3YIRjm-uvKupXdynVCgFaPgbFsKe6ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f229500ca2.mp4?token=ikxxCXXAwZ507opukdCrAmoy1mwoc5IC6nTYiyNBw2av3CAJhjo6La4gO8pLRM3p0OHpHF9gwjkE2QAnahplX1exkKTO1nxCbtHEzQLlaE7fK6xcS5yWpiIss-ZLZgAqAA2UeIa7cPeBLX7EytCJJlL9mKogojtwDcUf4adhyND9XEnE_Tr8dasjzxLQV-u2arxeMeMrDYf9rov7t35YufocJt8hp9Xg9TSedeyqsHUKj4pHcEvwHT14OJ47rCsKcMXbupVnAp5QFF0v0IwqixXbEW_XufRWGg92-JoczembY8MsloOyulB3YIRjm-uvKupXdynVCgFaPgbFsKe6ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجاری در مرکز خرید عربلا پلازا در شهر جدید قاهره، جان حداقل سه نفر را گرفته و چندین نفر دیگر زخمی شده‌اند.
🔴
وزارت کشور مصر اعلام کرد که یک سیلندر هلیوم در داخل یک مغازه فروش هدایا در طبقه همکف منفجر شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/141563" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141562">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ان‌بی‌سی: خستگی جنگ با ایران به ارتش آمریکا رسیده است
🔴
ان‌بی‌سی گزارش داده فرماندهان ارتش آمریکا نگرانی خود را درباره کاهش روحیه و فرسودگی نیروهایی مطرح کرده‌اند که ماه‌ها برای پشتیبانی از جنگ با ایران در منطقه مستقر بوده‌اند.
🔴
این هشدارها به پنتاگون و کاخ سفید منتقل شده و نشان می‌دهد طولانی‌شدن مأموریت‌ها، علاوه بر فشار تسلیحاتی و لجستیکی، به مسئله نیروی انسانی و توان ادامه حضور نظامی آمریکا نیز تبدیل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/141562" target="_blank">📅 23:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141561">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
رئیس سازمان بهینه‌سازی: مصرف روزانۀ بنزین ۱۳۵ میلیون لیتر است
🔴
تولید داخلی ما کمی بیشتر از ۱۲۰ میلیون لیتر است و میزان واردات تقریبا ۱۴ میلیون لیتر است. یکی از اهداف دولت این است که واردات صفر شود و پول آن به اولویت‌های بالاتر مثل دارو و کالاهای اساسی تخصیص داده شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/141561" target="_blank">📅 22:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141560">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k44aaIrtJSqJeubVRFOthOMEdkbZZIuetcR5P4A7TTw8t2a1OFtIl7Pv0-i7GdTaJoTA9-uQnuZ-8cJge2vPakVIvSUqsk5wHqTKFIJMhSJKmBcU0d5KVKeBdK3h34FNdB8TBYUmRLpT190rv-0H0tO9zsaUg3qscq9N2PYCBedLDj28MZNhJxxqZrLzMtUOO655vPphsXlBfJN6deGMX2DIXnDn-L3jTRERiKd_bvB2JIbIIARHg4AtUd5nwGHXyRFPxKm1vp_BRNDmvuVBa_K6LPNB2xk9k_LWwT7hFHUWxab3mtcr9A2VFiVD_Cbwjc7kQ69i5uTFpqo0K5KudA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه‌ اجتماعی اینستاگرام هویت بصری خود را تغییر داد و از قلم جدیدی رونمایی کرد که ترکیبی از حروف متصل و چاپی است.
🔴
این اقدام، نخستین تغییر در نشان‌واره‌ نوشتاری این پلتفرم در ۱۰ سال گذشته به‌شمار می‌رود
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/141560" target="_blank">📅 22:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141556">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4DB-h4C3plvKYQJ8yKlKrO3n9HD04K_SU6Gw5LDnK8plUFibCwZXS3omgZDG7YBYB4ZJTeoWvR-jsr9VqdHz63msZtbswqNRK6oF07KNoCOyfwmEshhdc7JIyyTFxVG_SyyKGRS2xTIMNek1ZxmWMLrKTiw17_hvLKeBgGEh659Jkv9F2arGGpTVpA_Bx_MDXTENG1xN8e6yLJn4Vop-gFV8r6O6H01MnaMr3sm9xR1AYlmJAhEcSBQms-NhrgDtM3IZogd66-ZzyouZpHZTDTN7pO43vLD4jXTyd4G9D2XzxylzGzwmUkUyIdPNzvfEMyrmJe4ij3S8nqB4QWIqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dtxQiQcKXDg2TddQC9fmDvLsJ2HJJQUXj8A8CWBd5tfgDu0zZqGTevCWOprYPx7pXvC_AvajNt7B_4_gWTGqX5G2UtS6fma3nBVioq4q8N75KDdIzf9leYenFkOP9d1lOA_TDnyTsb5a-zedFthwYgpuO9t38CeLqh_aePf1rSRamUZaJm-FE2rTzH9xIufix3_WPsbJnpJoW11pLxaPvBdUUO55S2GgQ4ViCwR2I2nAiiTTrynZ78MyWy53q3WbwUGN4Z_ipu1Eb_8vUjuuwf1d4HTWMzuutE07Q08OJ5zmbQdX0S7-DjujSOm5TrvMxZ4fCkIusyPEH2UrkT9_pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VDFANl1iyj06Nwz8pE9SSde2XvVl0vlGNtTJLVW1OmTNf2mSAFtzxkqxKqNtm_CLal6yeB4s0Qebh6wz_axY5fWlJGol9eyYRInt0POWMOafqNLRH2GPayU5vC_pGw5Qe_v5hTuhYI7y0K0gVr2p2Co-1wSyLGCEetTxqJWxU4FGFwafKoI3nawJ0SpAYmcx4GFJ8PHcjhhHqh-rIK1ZpclHnB6fmJT3gGis3X-b7l-rbSY3rBTkfmbZ6MPRs7LItyJKLKw-Rm8AAjnqpx3Q77GOETKXTlxSrjPXoWBnmdjrBPFRs3dYV6wQeHJGYAUh-VA3Cj_IreUJ9cbXzPu7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B4QOoxJxrVE-aURpJ6GzRod6MdNit5DSaoAjJtBEatWRqU0PeR6AQmb-E8mImgeNI6gkGb_--_TU6qjcpJpKOw6nQ6mMKfXB85U3R6yfI-ULnffGB-CYKBX-XmZxaWFn0nqoNFSQgC4w-fAyLRADEddciWuWgO0gqXN2VYhgvIqjpttAtRZoUN0n9NUpjWGLl2LWRQXF6MNyTHIGAxbjPM_PWPX-gLPIZp3BuB1iDlO5FAmikH5LzYQTunHzyPi6QzV9W7X7WWWdFhLeTdgJMVc7Z22ZqjyCzmPQ0vTADo4RDAPS4rO1hIFCtWawe3f_Dul2fizBOS7JW8InZ02Bjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
مشاهده کرم در غذای دانشجویان علوم پزشکی اصفهان/امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/141556" target="_blank">📅 22:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141555">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5531921f69.mp4?token=MkEfZb2pTtSdH0alFVpHaGgiuWN7gQq_MtU-vICTc0OU3DegWfZWANU8-1yDS-eBeFSvhKUONXEgsX-V7XMOcmEwcuYLA7YHnLXepRRi44Hf6FGDoqzI_cLINS5HKAZSxpJ6nei-Y_FRnCi0PgF5N88b0BpCsy91UT0hIbRnOA8NeFhpyh97PmvxNfizHqK32HYXfP01js2upEGdwH8ZYcbtb5Xf-YC1bwtx1VA-t8E_vU5a7qIQ2nkB0Yp0P7T1kqTs7GuABR15mjgLjpLFlAycIkIVqj9xJKjL_YvJKNDWV0qOyk48atBzr8HTokzEdZomLQTOKSVzsQ3Ih6U1vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5531921f69.mp4?token=MkEfZb2pTtSdH0alFVpHaGgiuWN7gQq_MtU-vICTc0OU3DegWfZWANU8-1yDS-eBeFSvhKUONXEgsX-V7XMOcmEwcuYLA7YHnLXepRRi44Hf6FGDoqzI_cLINS5HKAZSxpJ6nei-Y_FRnCi0PgF5N88b0BpCsy91UT0hIbRnOA8NeFhpyh97PmvxNfizHqK32HYXfP01js2upEGdwH8ZYcbtb5Xf-YC1bwtx1VA-t8E_vU5a7qIQ2nkB0Yp0P7T1kqTs7GuABR15mjgLjpLFlAycIkIVqj9xJKjL_YvJKNDWV0qOyk48atBzr8HTokzEdZomLQTOKSVzsQ3Ih6U1vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقاب اصفهانی
:
تغییر قیمت بنزین در کرمان به‌دلیل برخی بی‌تدبیری‌ها متوقف شد
🔴
رئیس‌جمهور تأکید کرد از اقداماتی که مردم را غافلگیر می‌کند پرهیز شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/141555" target="_blank">📅 22:35 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141554">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‏
👈
سقاب اصفهانی در شبکه خبر: به دلیل خسارات وارد شده در جنگ هم  دچار کمبود تولید در بنزین داریم هم در واردات بنزین دچار مشکل هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/141554" target="_blank">📅 22:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141553">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkPMab11iSH9Wnwis_rVvygi-Nd3JOhw6iTI4unn5JIchxenpQOHb9bs25R9gQP0RGh3tWlx9dM0aoeP4CB__W8UBjyjHroY7kCMTAgf1OsNsSMRF-FvH9BU-jQW9fr9ug1fRgbchNcFVZvVEU-QdgC_wfC1VZNOJUJhbhu8CZmbQhO5AfT6YgJV6_mvJQPJ75t71luhBvoRvCHccSJOWYGLyjWGRKYJSbbsJ6PcAAnR5NdNfC8ufdLHpQ7P08mtnSfLl13Cg77O4ShDuEqVUCKB0-ZztgZpaIFmp9XrRnDRhuwla-4ZRdfQ-KnQU-wI31rVuwQAmF_rLZn-cv_-OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مشاور قالیباف: با تصمیم سران قوا، گرانی بنزین منتفی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141553" target="_blank">📅 22:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141552">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUt6RjSm_NF7ypjHnLaFpAMJTmSpwQPPQx7q6nsutUwduBuSRueKarZXfziod53VjwC9n5iazJQbBy0QUSH_Xwa0NW5mFa7t7txyfImRfNcD7_7e_jqRL7Rez57lWJAGORySDbB_oI_GKdQlLLlCrbJdvvNhN5GwwtY8Eerr3MAqx9IOBk1zftwbc0wqhfa3NUpJ6H7tjqtd_cfMB7pI_mBRW1DlZBgeNiKEIIiSg89422lkt3WnNI8GYGRBBkPJ1DRRO2JCabRBUY1GdLGz6Dsgkd9IQGEFAvNXtcyY7vaEr8O6sqXAp-ngjfphTkd4OnmhRMXsqKZ75i_9uiNkDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ، اعلام کرد که سیستم "de minimis" لغو شده است: امروز، پیروزی بزرگی در دادگاه تجارت بین‌المللی ایالات متحده به دست آوردیم، پیروزی‌ای در برابر یکی از ناجوانمردانه‌ترین معافیت‌ها در سیاست تجاری آمریکا، یعنی همان "de minimis" مشهور.
🔴
سال‌هاست که شرکت‌های حمل‌ونقل خارجی می‌توانستند بسته‌هایی به ارزش تا 800 دلار را بدون پرداخت عوارض و مالیات به کشور ما وارد کنند، و این امر، نظارت کمتری را به همراه داشت. این موضوع به یک راه فرار بزرگ برای فرار از پرداخت مالیات تبدیل شد و همچنین، کانالی بود که قاچاقچیان مواد مخدر، تولیدکنندگان کالاهای تقلبی و سایر جنایتکاران از آن برای وارد کردن محصولات خطرناک و غیرقانونی به آمریکا استفاده می‌کردند. آمارها بسیار تکان‌دهنده بودند.
🔴
تنها در سال 2024، سیستم "de minimis" حدود 10.8 میلیارد دلار از درآمد حاصل از مالیات بر واردات را از آمریکا سلب کرد، و بخش قابل توجهی از مواد مخدر و کالاهای تقلبی ضبط‌شده از طریق این کانال وارد شده بودند. بنابراین، ما آن را بستیم. با یک امضای قاطع - بدون استفاده از دستگاه امضا - این معافیت مضحک را لغو کردیم و باعث شد که کالاهای خارجی طبق قوانین عمل کنند. واردکنندگان شکایت کردند. امروز، آن‌ها شکست خوردند. دادگاه حکم کرد که رئیس‌جمهور اختیار قانونی برای لغو این "امتیاز" را داشته است.
🔴
اکنون، آمریکا امن‌تر است، کارگران ما بهتر محافظت می‌شوند، و میلیاردها دلار درآمد حاصل از مالیات بر واردات که قبلاً از این راه فرار می‌کرد، می‌تواند برای تأمین مالی ارتش بزرگ ما، کاهش مالیات، عدم مالیات بر انعام‌ها و عدم مالیات بر تأمین اجتماعی استفاده شود. سیاست تجاری "آمریکا اول" و اجرای قانون "آمریکا اول".
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/141552" target="_blank">📅 22:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141551">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3e60e3f4d.mp4?token=gpklsjwiWm8bXdybKC7ddYIqKIG9c5z8ZpmJuWh616ycRxuysvnZB1CCXxFgyvt7G-_tphK-f94N-xWQ1gSdqJDTNL4g7nkQ8KPfqVVA-4I--czW7414lEoTFbjZ506jE8yhyRtXduANZbgl2xj1LX-xi6V2BMtA_5d9F9I7qB-WGS0NLYn-FYxmUmIUsfd_ccFKlaAvOFHe7L7pwxyKNY68vzRDDQJugvCDrUaiIALZp092UJk8tvjzqV6P5eHj8fTdWT4FCMXS0SIV3gm_WRc7yBKWJ6ArNye8coin3qryU9JBS-6xukMkpvgMVV-wwXf6JQaOly74SDJWbr00_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3e60e3f4d.mp4?token=gpklsjwiWm8bXdybKC7ddYIqKIG9c5z8ZpmJuWh616ycRxuysvnZB1CCXxFgyvt7G-_tphK-f94N-xWQ1gSdqJDTNL4g7nkQ8KPfqVVA-4I--czW7414lEoTFbjZ506jE8yhyRtXduANZbgl2xj1LX-xi6V2BMtA_5d9F9I7qB-WGS0NLYn-FYxmUmIUsfd_ccFKlaAvOFHe7L7pwxyKNY68vzRDDQJugvCDrUaiIALZp092UJk8tvjzqV6P5eHj8fTdWT4FCMXS0SIV3gm_WRc7yBKWJ6ArNye8coin3qryU9JBS-6xukMkpvgMVV-wwXf6JQaOly74SDJWbr00_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خروج قطار از ریل در انگلیس
🔴
یک قطار مسافربری در حومه شهر «لویز» انگلیس از ریل خارج و واژگون شد.
🔴
به علت مسدود شدن درب‌های قطار حداقل ۴۰ مسافر درون قطار حبس شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/141551" target="_blank">📅 22:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141550">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNZgCnavOoQQV7agw2Eo38qOJ6_tC5TRLTv3GATqTWg9Ev_EglL36FXtatjtus1pyC2NL1EsDXsofHhvfgqToVEyUe6y1dn19HBb5qJYql2Ee2flJ4E5LFskmtr7SP2PjmBVpTVCg0EK4tAu-XqIrCWP79GGbWkYX5u_AHHkZs4eQMyYu8fX6JXamwSmqDHyLtNmq1WeIRXx03h9X-cPqf0fSNRECbieG6L7q42gvYAenbk7XXsG52Dj5qLlbwfpvrFYIgknDU0dtLEoxQL5454ckQmsjdoNkDF-Fvg0lgI3kbugU4rITwkT_7FX98u3c1PUkv8aJZGZyQs7m87jeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هشدار رئیس کمیسیون امنیت ملی به جولانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/141550" target="_blank">📅 22:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141549">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ای ۲۴ نیوز: ترامپ و نتانیاهو از زمان دیدار در واشنگتن که به دو هفته قبل بازمی‌گردد، با یکدیگر صحبت نکرده‌اند
🔴
این قطع ارتباط در شرایطی رخ می‌دهد که ترامپ همچنان در حال بررسی گزینه‌های خود درباره ایران است
🔴
در عوض نتانیاهو تماس‌های مکرری با جرد کوشنر، داماد ترامپ داشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/141549" target="_blank">📅 22:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141548">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed9c73d19.mp4?token=Alab6BBXCKCQcZyAvJftIrffGPh6ZEBbbeC8UYo1gcFMKYC58QVcBOyNVYGQHwBieONzcGgtyE8mBR3j2BfPhQ8cwg3V6wzDjulLCgtTWbRSwQoILkAU2s5ljnDhqLMzX59cUslAJA0aUDG26VHa1ioEJ0tooLAqQGf8rZ7mVIIYROsF3YqjZYRbpOvj0B3CJLpoFuOMxB9Aj02dOAv9Q-mi3Cg2-2Xx_bnTUl06QMUq_H7qlogZghxJtDlP8wjNJ1Br59i1nG_Lbv5MwkR2BYdCY3RcJUbeveqoc48fMB71VmgjaNesqZPFkK3OHh6JtFN7l3J4nIDB1hU7Q3pJ6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed9c73d19.mp4?token=Alab6BBXCKCQcZyAvJftIrffGPh6ZEBbbeC8UYo1gcFMKYC58QVcBOyNVYGQHwBieONzcGgtyE8mBR3j2BfPhQ8cwg3V6wzDjulLCgtTWbRSwQoILkAU2s5ljnDhqLMzX59cUslAJA0aUDG26VHa1ioEJ0tooLAqQGf8rZ7mVIIYROsF3YqjZYRbpOvj0B3CJLpoFuOMxB9Aj02dOAv9Q-mi3Cg2-2Xx_bnTUl06QMUq_H7qlogZghxJtDlP8wjNJ1Br59i1nG_Lbv5MwkR2BYdCY3RcJUbeveqoc48fMB71VmgjaNesqZPFkK3OHh6JtFN7l3J4nIDB1hU7Q3pJ6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کیث کلوگ، نماینده سابق ترامپ در امور اوکراین: ترامپ عملکرد خیلی خوبی داشته است. مشکل اینجاست که از نظر ایران، این آنها هستند که دارند پیروز می‌شوند، نه ما، بلکه در ذهن خودشان، آنها دارند این کار را انجام می‌دهند.
🔴
و فکر می‌کنم از این به بعد، باید ترکیبی از فشار اقتصادی و فشار نظامی، به‌طور هم‌زمان اعمال شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/141548" target="_blank">📅 22:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141547">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3-P7zwX7Q4IbahzDzloI6WjMx6KbWilAMeO112oKgvfd1k-Kw0sYI8Mh28o-bAo9n8egbZq1njGy5WHh7OcwiL9Vo9w2sniAQCTC9oYAfuUNJUuk0VLOkmEL_iB6Y3jyWG2llnvRvQBWLaRfmL-eiwI3ETUoVVeZxFEhy_ap-wcd9evtFht3rdQFs1nHJ7jLvvGkJPoPneAy4XNOTyYyy_g852ZhbnmvmTloXl_U0ingaqIefCZh5QNdfLauiVJ1T0LAw5StoOThhvWG6h2enCiSenhxsOP4aOJRZR4XH4AnwXv-JJQk8n7bfPKCwZJc96szxGpEHkMz21Sy4uXKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی سعدوندی، اقتصاددان:‌ چطور‌ رویتان می شود وقتی خون مردم را در بازار خودرو در شیشه کرده‌اید، از مردم بخواهید افزایش قیمت بنزین را بپذیرند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/141547" target="_blank">📅 21:59 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141546">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
کان نیوز: برد کوپر فرمانده سنتکام به اطلاع مقامات اسرائیل رسانده برای آغاز مجدد حملات به ایران فشار می‌آورد و از نظر او فشار نظامی بیشتر می‌تواند تهران را مجبور به تغییر موضع کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/141546" target="_blank">📅 21:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141545">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وزارت دفاع ترکیه روز پنجشنبه اعلام کرد:  ترکیه، عربستان سعودی و پاکستان بر اساس پیمان نظامی‌ای که هفته گذشته میان این سه قدرت منطقه‌ای به امضا رسید، وزیران ارشد خود را در قالب یک گروه مشترک گرد هم خواهند آورد، رزمایش‌های مشترک برگزار خواهند کرد و همکاری‌های خود در حوزه صنایع دفاعی را گسترش خواهند داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/141545" target="_blank">📅 21:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141544">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L14AAxMzTTI6cuRxDKNJQqbBsXzEENZ9YraqHPEhLbHreB6ckMI3trBoECeVs6iSQ95EqiqN3jG3qhMCGjwsfI5KfpVy8EVP0tvErEXAfeoduCWXMv3PHtHQxigusFkpJH5KV_6_eEPhP9Wd255N1uFUgVEW1z_N6h1OO2NKGrcFMooIkgsnUkNuLBvFcXmkS3PpoVPFChT36EHQPbntVOrMfduaKEmM24X0OOlhxLFUFJYAiS_2xVhbL5fN8TgnFPaO1JNvuEGWEISlxeL1s3Ok8iZLTRhHlYgekOIUREDXoIO09PdnpyceU-ylzpCpD05Ukz2r1Tq0pnu1Vb5hmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی:
رهبرمون هرچی بگه همونه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/141544" target="_blank">📅 21:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141543">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حوصلم سر رفته بود رفتم تو این بازی جدید صراف شانسی این چنگک رو زدم، 3 دلار داد
😐
😂
گفتم لینکشو بذارم شما برید تست کنید ببینید چی میده بهتون
👇
https://B2n.ir/mn1122</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/141543" target="_blank">📅 21:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141542">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پیت هگست گزارش‌های مربوط به تخریب شرایط در ناو هواپیمابر ابراهام لینکلن را رد کرد و آن‌ها را «کاملاً تحریف‌شده» خواند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/141542" target="_blank">📅 21:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141541">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/524d681ef1.mp4?token=Ds_wsfXw3q76PDXEOWiBj5IvhZY_DQwDdMZkEfHaxmH-duL4R32S-Lxsk-v0h0V8QUMKB-ryi1GQfjl2XheNyyjNz1H94OvLAXml3Vi9CSKHTApOOr3qrB4emy9uD7RtrGDsI8axTaH6a7qrJySYmndUIJMEJHNO-4pqzGxt-06uNu_H9bSo19KNPcqs6rrZfvr7xltxcjXKF7G1xeQCt3QoYQ-nv5dsdsPimO2gOLA_us9wmGSbfqJtySLolfGUDbMXiQqg3mGDTvDElpH2JmtUtdI_ntYMoDYWzdnTAdvAipN8g7k8_l7WlUJOgMO3t7DnSJNGDXh4fNJdWhtk_Qbau4z7A34MjazOU7NCJ7_nx3aWCLTYQRsFcR97TTBJZo7pK0n0n8f80VX3vY8NaZHUXWFJFhS2A6lYOJnNdwjXxOjuXL4GWd7_EgaebBLV29vVj5NK3wbhvY7N9SZB_jF56tU7eQDqn_qxVhtcG5lfiio2AP5lHdVBlhcXt3we3T7pxY7qLGPIzwr0vHJFyp-arubKPTKvp044ctWxHRV4WXicPuLJ93FGu96uK2CoOsmJ6QPiBLXzd56P7QaMe2l-483fBr4Ce2HN7dDVJCQQsfOPNQ4rVhznqSoImCFVIVJq77SoTDdocKUqjvWjJqzKhbRoP5gfpoKhiMD9hNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/524d681ef1.mp4?token=Ds_wsfXw3q76PDXEOWiBj5IvhZY_DQwDdMZkEfHaxmH-duL4R32S-Lxsk-v0h0V8QUMKB-ryi1GQfjl2XheNyyjNz1H94OvLAXml3Vi9CSKHTApOOr3qrB4emy9uD7RtrGDsI8axTaH6a7qrJySYmndUIJMEJHNO-4pqzGxt-06uNu_H9bSo19KNPcqs6rrZfvr7xltxcjXKF7G1xeQCt3QoYQ-nv5dsdsPimO2gOLA_us9wmGSbfqJtySLolfGUDbMXiQqg3mGDTvDElpH2JmtUtdI_ntYMoDYWzdnTAdvAipN8g7k8_l7WlUJOgMO3t7DnSJNGDXh4fNJdWhtk_Qbau4z7A34MjazOU7NCJ7_nx3aWCLTYQRsFcR97TTBJZo7pK0n0n8f80VX3vY8NaZHUXWFJFhS2A6lYOJnNdwjXxOjuXL4GWd7_EgaebBLV29vVj5NK3wbhvY7N9SZB_jF56tU7eQDqn_qxVhtcG5lfiio2AP5lHdVBlhcXt3we3T7pxY7qLGPIzwr0vHJFyp-arubKPTKvp044ctWxHRV4WXicPuLJ93FGu96uK2CoOsmJ6QPiBLXzd56P7QaMe2l-483fBr4Ce2HN7dDVJCQQsfOPNQ4rVhznqSoImCFVIVJq77SoTDdocKUqjvWjJqzKhbRoP5gfpoKhiMD9hNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
تصاویر جدیدی از آلودگی نفتی سواحل قشم که یک غواص ثبت کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/141541" target="_blank">📅 21:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141540">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6aa7b78e25.mp4?token=AVe6se-6bTwfc3iq8pfSfP0EPpYv-3FqGr5jjpzCvUueUf_ZxNkSJKturULNSVfUfIZpavKThb0kMEFln5e7uRwFQBGuvcGoGO8zGBBjCFaYSKKOXnmkGIy1EoQVywfxyBx_K3y4wWcMfGks5Zw0aa08AViz22O4KkTISpWQ1lumZ0NGtWsXmiMH--MW-TtnbFLfVrpVS5ErtIOSeSUdGPRfiK5wHvGORay0vmSk13jjKjf4ImKz23gMiUc-b16SdiYcFRClNCexXlfROsFbfIbG0Ja5QTjjUe_ugOZ35TI4_N-nrMgbTWviLJSBvQiIxdUxw2V_HHS9DUviX4dKT4m-ai2GrYPIA_P78jmnJtyElHB_TdtD_T87aTx4GQphmlIsq9i2nAOSRr_g4e_D0Uq-lQkX0S6gysqdC5U0N8yWcghzxudKoVRx8nLFbKxXv-PfIeVKHuxjEo--9ReFktvxZzm5KtGdY03BL_Z912vPmlxp97oHownAMh23W9ZvESvK2h1L5JS_L9uoJnEv3X8_NG9Fkqq2v-bygsxCHGZbUv5M5CjC5d02HZxKluuYs3WXotfIu2Vv9e4dS1dC5w4RdKB_GwmeAGojAixDOJjvzvt4r-kFXjqQnMxXYOcG-1sWkSJYP41MBwRUzgxQw_01pxDeUMaS0oauofBBgcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6aa7b78e25.mp4?token=AVe6se-6bTwfc3iq8pfSfP0EPpYv-3FqGr5jjpzCvUueUf_ZxNkSJKturULNSVfUfIZpavKThb0kMEFln5e7uRwFQBGuvcGoGO8zGBBjCFaYSKKOXnmkGIy1EoQVywfxyBx_K3y4wWcMfGks5Zw0aa08AViz22O4KkTISpWQ1lumZ0NGtWsXmiMH--MW-TtnbFLfVrpVS5ErtIOSeSUdGPRfiK5wHvGORay0vmSk13jjKjf4ImKz23gMiUc-b16SdiYcFRClNCexXlfROsFbfIbG0Ja5QTjjUe_ugOZ35TI4_N-nrMgbTWviLJSBvQiIxdUxw2V_HHS9DUviX4dKT4m-ai2GrYPIA_P78jmnJtyElHB_TdtD_T87aTx4GQphmlIsq9i2nAOSRr_g4e_D0Uq-lQkX0S6gysqdC5U0N8yWcghzxudKoVRx8nLFbKxXv-PfIeVKHuxjEo--9ReFktvxZzm5KtGdY03BL_Z912vPmlxp97oHownAMh23W9ZvESvK2h1L5JS_L9uoJnEv3X8_NG9Fkqq2v-bygsxCHGZbUv5M5CjC5d02HZxKluuYs3WXotfIu2Vv9e4dS1dC5w4RdKB_GwmeAGojAixDOJjvzvt4r-kFXjqQnMxXYOcG-1sWkSJYP41MBwRUzgxQw_01pxDeUMaS0oauofBBgcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیدان درباره پیوستن مصر به ائتلاف مکه : مصر شریک طبیعی ترکیه‌ست و امیدواریم به‌زودی به‌عنوان عضو رسمی به این ائتلاف بپیونده
🔴
فعلاً چند مسئله فنی در حال بررسیه و بعد از حل اون‌ها، مانعی برای عضویت مصر وجود نداره
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/141540" target="_blank">📅 21:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141539">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89761a2149.mp4?token=OISCJAkutVgbtwPkfkaOHOt721qA24TOKLvh4m68n1s1q90nRCkXQfZooF8v-h8cJf-ty8RvmF4CmwFqfAli9C0OHtHI6EeDkSXiY-NcWHMvxd1npilRi2_3rySPNnInTugql7avCO7_DgNcm8dwyvd9CtsKq5ipdPrvojDAQxyISESzSQOBTdASrOI20Fr9ewzX_HBMuUfTISDxqhVGP88qcpeGTYnGtiVWdyivrrEjbxo2TOa-orcrwgOOJH_xvyTN6b8lwPgGueimOLDhaN-rpbHdsefN0_wvoBAJxtESlyZkUAiaDRn2EPVkefGCsS_RbxOKUyVy_0QrOmc9Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89761a2149.mp4?token=OISCJAkutVgbtwPkfkaOHOt721qA24TOKLvh4m68n1s1q90nRCkXQfZooF8v-h8cJf-ty8RvmF4CmwFqfAli9C0OHtHI6EeDkSXiY-NcWHMvxd1npilRi2_3rySPNnInTugql7avCO7_DgNcm8dwyvd9CtsKq5ipdPrvojDAQxyISESzSQOBTdASrOI20Fr9ewzX_HBMuUfTISDxqhVGP88qcpeGTYnGtiVWdyivrrEjbxo2TOa-orcrwgOOJH_xvyTN6b8lwPgGueimOLDhaN-rpbHdsefN0_wvoBAJxtESlyZkUAiaDRn2EPVkefGCsS_RbxOKUyVy_0QrOmc9Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هجوم بیش از ۱۰۰ هزار آفریقایی به اروپا !
🔴
راشاتودی از ستون عظیمی از مردان آفریقایی خبر داد که با اسکورت نظامی در حال عبور از صحرای شمال آفریقا به سمت اروپا هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/141539" target="_blank">📅 21:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141538">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usCY4D1v-dhAHzp6rxS8MTW-MIC7EIaQLOdgTs5QR39roiUwWWPk3oAdTdko2BHBVogK2IPLUkJb5S8g2x4QZ1xBQaDRW8UcWJ4j6k5lzLHfcxhKYcOXdQ9GLbpFs2lHi5AV1vv_8RXRZtCdh--iTSpJUFY7pl2G0Sk0yU15aqx-stIwiDPZU9JumHpC9I3ih2tOrpr_-VOlEqd6szBTQU5MRy2hGftp_xnM4QFurw4WeFnmh8-7IX0ditJb_ULWIH2SWhsNh0t6e63GEtImaSEWjDy-Lj3G4sI2owDH2Lg20OLy9RPd4pvRk9aQm4RULcAzfcoPLjRKnYsWVdxusQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور خارجه ترکیه، فیدان، با وزیر امور خارجه مصر، بدر عبدالعاطی، در شهر العلمین دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/141538" target="_blank">📅 21:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141537">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
هگست: آمریکا بر خلاف بقیه، وارد هرجا میشه باعث رشد اون کشور میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141537" target="_blank">📅 21:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141536">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل: برد کوپر، فرمانده سنتکام، به مقامات اسرائیلی گفته است که او برای حملات مجدد به داخل ایران تلاش می‌کند و معتقد است که از سرگیری جنگ می‌تواند موضع تهران را در مذاکرات تغییر دهد
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141536" target="_blank">📅 20:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141535">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
قانون‌گذاران دموکرات از پیت هگست، وزیر دفاع آمریکا، خواسته‌اند درباره کاهش گسترده نیرو و امکانات دفتر آزمایش تسلیحات پنتاگون توضیح دهد.
🔴
آنها همچنین خواستار بازگرداندن چند دهه ارزیابی غیرمحرمانه تسلیحات شده‌اند که از وب‌سایت عمومی حذف شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141535" target="_blank">📅 20:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141534">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وزارت دفاع ترکیه: بر اساس «توافق مکه»، رزمایش‌های نظامی مشترکی را با عربستان و پاکستان برگزار خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141534" target="_blank">📅 20:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141533">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThGlhu2uQK6Y7AAVvDIc0-tCmsm_GfYPPKIaLtt0FZO89y2YKVZwT0LBf2kpQtUf6kCJ1n_VBd_poOYdEakmXGYDfieOijy2FFRrq4igjvOxbibcXPatKeysdE7ZjXqG4rpE0-64ykH5f7z8odV0fBe2lGfx5k_-AgzM0GtEfNRit5rmk5Uh7-SM1MxLKyW0i2QLRgXr6byqcVTQb9TKZ05Abyi1R9C-qxbnP8tF_5O4EK0QAIJoebED0JgrHz9ikA1fy-GQ2j1Mwe-WtYhFHejvS4m-6jPHt_Y0QX5rRaGqezqWMIqLbuvlwQJWYyEFUph7PbBMkkuBU1_uLCrUMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عبدالرحمن منصور، شهردار منصوب طالبان برای شهر فیض آباد، پایتخت استان بدخشان، توسط جبهه مقاومت ملی ضد طالبان (NRF) در یک کمین بمب‌گذاری شده (IED) ترور شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141533" target="_blank">📅 20:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141532">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
مارک کارنی، نخست‌وزیر کانادا، تأکید کرده است که حاضر به پذیرش یک توافق تجاری نامطلوب با آمریکا نیست.
🔴
هم‌زمان، مذاکره‌کنندگان کانادایی در واشنگتن در تلاش‌اند به توافقی برای کاهش تعرفه‌های آمریکا دست یابند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141532" target="_blank">📅 19:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141531">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZYQ5fAFvbzqmC1fd3f5QW8XpC-9nxVZDCY0_EYU9JEboeH17i-Guwg8o4U3OQSS2_Vpuvk_V5ooUArj3gQcWNA-RrwCYpALu99nsAAv2lmJCH64lD0cQmhTHje5xQJc3pxI5yINb1IQIRQxr4wBUtXKbuPahoEdiBgbhTi9aVybghfu8g1_0bpAEcNbHBMbZhGvCcq2fJA8bDWiVm3c6fKIVUmj6zqCAcBQa3U5EqP7gIG61KrCjJV2cKaSw7uDPFerGhWrIxhp_dtxyOcCFs40fPKOiqwMmo2GFu9WHwGQJdcUs7vepbS001ogsmJuzNqiAuKGF3v5w4Y5zJ7EBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
افزایش قیمت نفت برنت در ساعات اخیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141531" target="_blank">📅 19:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141530">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
برخی منابع عربی: تهران دمشق را به هدف‌گیری ۱۰۰ نقطه، ازجمله کاخ ریاست‌جمهوری سوریه، درصورت مداخله در لبنان، تهدید کرده‌است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/141530" target="_blank">📅 19:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141529">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
نشریه WaPo  : آمریکا ۴۵ پهپاد ریپر از دست داده
🔴
آمریکا در جنگ با ایران حداقل ۴۵ فروند MQ-9 Reaper از دست داده؛ حدود ۲۵٪ کل ناوگان
🔴
ارزش این تلفات بیش از ۱.۳ میلیارد دلار برآورد شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141529" target="_blank">📅 19:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141528">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
برخی منابع عربی: تهران دمشق را به هدف‌گیری ۱۰۰ نقطه، ازجمله کاخ ریاست‌جمهوری سوریه، درصورت مداخله در لبنان، تهدید کرده‌است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141528" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141527">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnS3isT2n9BRJfqNMt_azyGxgAbb44qXOeTKW5bd432iaATZK9-KZK41wK6EsjK2dlLTXBiCNElB0utUZA0vf_5KrYtzZRdj5ZIdG9aVaISHip3fgGuptyuklLxgMGjEZ9x4wgysY6A4-tW8Usq2WMx222E_PgIF6KoujU_ttov48gZH1hxDw5hsJBTp8hzW4ak4YrdQ0JbmDv1QcLUCAEx4GW_m3wFB33_OnBhFFaK1CJPClvw41mycPmD-XR2F3F0Cb8Er3idIeS5V-5oitnWQcmHfJMRPU9CtCw4qnNoawLkbRCEv6KftrRDquIHGCsPEu_RyNNFQcxJ7REECAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر بهداشت و سلامت آمریکا، رابرت اف کندی: تا جایی که ممکنه فست فود نمی خورم، مگر اینکه دونالد ترامپ مجبورم کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141527" target="_blank">📅 19:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141526">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
دبیر سابق شورای عالی فضای مجازی ، فیروزآبادی: یکی از نهادها فشار آورد کلمه «هایده» و «لوزام آرایش زنانه» را از موتور جستجو حذف کنیم؛
🔴
چون ابتذال و تبرج را در جامعه ترویج می‌کند؛
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141526" target="_blank">📅 19:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141525">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ناو هواپیمابر جرج اچ دبلیو بوش ظرف سه روز به خاورمیانه میرسه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141525" target="_blank">📅 19:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141524">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزیر دفاع آمریکا: ما قادریم تحریم‌های ایران را تا زمانی که لازم باشد ادامه دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141524" target="_blank">📅 19:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141523">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFHIidye8VNQPmZdyt9s2HM-whqHAQSsHEXdU3pQfF2JWTrJjkhm796UbcOzcMxf2__c6rS5p7EOSzcawDgkPSlwFMxHxyFi6k3FayEU3inZ_89D2BDCLDp4U0dQLaK0-eUX-VV8d9SSjdpM1oRKDRkUwv3meQvY76I6k2giita7ja5xJAyqLjvEW4BnkLgViZunCaBMU6PmKf9YwxQ8qQv7jt_wb3j22s3XaIXP9-pTnrUsGDIpps6Zg2e3phsKiAvmDnBNiqYuiSw-UTqh_ZxVISXa-eXnyD-BC9nwuobd_RhrFEAikmMSwhbnfeUtkpRXgJHpX4BF4Aq3HhL74Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسرائیل رئیس پلیس غزه را هم ترور کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141523" target="_blank">📅 18:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141522">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
تحلیل بنزین و تاثیرش روی تورم  شنیدید از قدیم میگن فلانی «هم چوب رو خورد هم پیاز رو»؟ الان داستان اقتصاد ما و قضیه بنزین، دقیقاً همینه!  بیاید خیلی ساده و خودمونی اقتصاد رو بررسی کنیم ببینیم ته این بازی چی میشه.   قضیه از این قراره که کفگیر دولت بدجوری به…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141522" target="_blank">📅 18:46 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141521">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
به گزارش رویترز، شرکت هسته‌ای «نوکلرالکتریکا» رومانی روند خاموش کردن تنها راکتور هسته‌ای فعال این کشور را آغاز کرده است.
🔴
با توقف این راکتور، تولید برق هسته‌ای فعال رومانی به‌طور موقت متوقف خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141521" target="_blank">📅 18:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141520">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
نیروهای مسلح یمن: ما ۳ قایق حوثی‌ها را که حامل مواد منفجره بودند در دریای سرخ منهدم کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141520" target="_blank">📅 18:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141519">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نیویورک تایمز: غول‌های نفتی خلیج فارس میلیارد‌ها دلار صرف ساخت مسیر‌های جایگزین تنگه هرمز می‌کنند
🔴
این پروژه‌ها میلیارد‌ها دلار هزینه و سال‌ها زمان برای تکمیل نیاز دارند، اما شرکت‌ها و دولت‌ها آن‌ها را ضروری می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141519" target="_blank">📅 18:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141518">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
فیروزآبادی، دبیر سابق شورای عالی فضای مجازی:  گروهی در ایران می‌خواهند اینترنت ایران را بالکانیزه کنند، این افراد طرفدار توسعه انسدادی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141518" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141517">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8563204fb3.mp4?token=WgY4NM7obaq94AQHmLS1bNOvD0LetrBHI5YCsBxgRc_BIJEc6dXSrkAJq-Jwq7AKFydw_dGj6TaIIa8yMPxR53_NlgVSAabBQa4YP3bZCUo8C3Tj2ejWW-zDhPxF9Y0VEoyMNOAvJN2CdqE-Q6_lhSVGRsH0ysg5FnY4vqXWth-VEaBADzld8QliZpd_C-0zS1t3e6tHrJzNCqY9vb1h03Kp0TwzeYZT0Lfyqo6ytc8gfNJMeT8zXFllSnlCE7nykYD8AtlW7_5ZRUYNXqvsfXmUG0TNxbXLXsVv1mVxNhtSms7kG9ERJO8eP1GiDpaxYvujfWLfBqlQzBUCHQXt0h7U1r64t5x9Ohg8xTApD85IwRI7P3AHz0vO08zZnbnHR_DlNQ4UnCYmZJuaB1YhhKidc8KqB94xFeYRS4yKPIIcGBJDMsYXTV7VT91lJHuWL2NkiTPiNRvbDi6Pt5Ds2ZcLHd9AsayOlT-H2j-AM5zrOmmrNLPnFeyT7GnA0_T4Xp44e2fhOqdHdM3sZMuNZhKKufHV7d8Ar0hyRLsQ5eWvXX-OgIfkU9iIei_Ca5xqI0tJRmQrkCFfbyVjelnxGI3GQ4eqw-YzaIGLPqNJiCmdlZXZvrL8vYwDnbZQSI92byW65CkcOkQPPbNJ3FjS1D1h6IMweUblA0t4-o7Bi6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8563204fb3.mp4?token=WgY4NM7obaq94AQHmLS1bNOvD0LetrBHI5YCsBxgRc_BIJEc6dXSrkAJq-Jwq7AKFydw_dGj6TaIIa8yMPxR53_NlgVSAabBQa4YP3bZCUo8C3Tj2ejWW-zDhPxF9Y0VEoyMNOAvJN2CdqE-Q6_lhSVGRsH0ysg5FnY4vqXWth-VEaBADzld8QliZpd_C-0zS1t3e6tHrJzNCqY9vb1h03Kp0TwzeYZT0Lfyqo6ytc8gfNJMeT8zXFllSnlCE7nykYD8AtlW7_5ZRUYNXqvsfXmUG0TNxbXLXsVv1mVxNhtSms7kG9ERJO8eP1GiDpaxYvujfWLfBqlQzBUCHQXt0h7U1r64t5x9Ohg8xTApD85IwRI7P3AHz0vO08zZnbnHR_DlNQ4UnCYmZJuaB1YhhKidc8KqB94xFeYRS4yKPIIcGBJDMsYXTV7VT91lJHuWL2NkiTPiNRvbDi6Pt5Ds2ZcLHd9AsayOlT-H2j-AM5zrOmmrNLPnFeyT7GnA0_T4Xp44e2fhOqdHdM3sZMuNZhKKufHV7d8Ar0hyRLsQ5eWvXX-OgIfkU9iIei_Ca5xqI0tJRmQrkCFfbyVjelnxGI3GQ4eqw-YzaIGLPqNJiCmdlZXZvrL8vYwDnbZQSI92byW65CkcOkQPPbNJ3FjS1D1h6IMweUblA0t4-o7Bi6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ ایالات متحده آمریکا:
ما کارهای بدی به آدم‌های بد می‌کنیم.
برای مدت زیادی، آدم‌های بد کارهای بدی به آدم‌های خوب در داخل ایالات متحده آمریکا و در سراسر آمریکای مرکزی و جنوبی کردند.
ما قصد داریم به آمریکایی‌های بزرگ و شرکای بزرگ قدرت دهیم تا کارهای واقعاً خوبی انجام دهند و در اعمال خشونت علیه کارتل‌های مواد مخدر و سازمان‌های تروریستی تعیین‌شده بسیار توانمند باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141517" target="_blank">📅 18:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141516">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5Be-xGy-VsjeUS-71FSAvdKIWu1Obij_FEGwK6owlR6n8T-zKyp_FhqrOuqGj_q3ULwC9tjDEbM8VIuWYw-JqfUueZVKxstJ82WwBPJc_R_47ioZtiz27TlpS19YD1qi0EHmpHMIoVlF211uD9ZYPr0eihkHxYT25e52rcOHUslgWf8THKAl9OQKUk78HLzWmB5fKsqkYX8piTGu9KptbnHt2MsywQN2bAPSP1nFJb0Ag_qvoNZgO12mQZXwx6KuQ5pD0JQAbgdn-mheUrAuPFIX-cYQE9fqBuGTbF23R8igAVGxx68E64_gXBAprmTIpiRwJ2z0Fze-Yro3HqiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
الحدث: سفر اسماعیل قاآنی، فرمانده سپاه قدس در بغداد با هدف منصرف کردن گروه های حشدالشعبی از تحویل سلاح خود به عراق، به پایان رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141516" target="_blank">📅 18:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141515">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd4d419c2.mp4?token=dOFMTNj7XPn4ZfMuw5aKRVi6xvAQ8_LoQ20OvdXMu3exIOBnbxhBil8uvLcdGC8GG9ldKnRZ82M2dJ-_8XfPdgwRkqhszFD75NvAbViNe7Jl15RvPgK1SLkoa6DIYrQxlgEwaJZxsnCOWRNdKVLmnrfJrwAIIUS6UzZfnL9IxrkkJoK8VwdtsD1jNQOOeB3_jnvDQ9jAH3Gluz_jlaQKqfxLXY37TT17oQXfBOpUJULsAFHH2p78iThLkPECR7KXNeFWxRZxq4ehqDr_Ut3QWfJhUz8d374fd80BY-YifVHegbK-akgkI_GMh2HMYfcatGyDDu2HfFhGkGNF5HTDOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd4d419c2.mp4?token=dOFMTNj7XPn4ZfMuw5aKRVi6xvAQ8_LoQ20OvdXMu3exIOBnbxhBil8uvLcdGC8GG9ldKnRZ82M2dJ-_8XfPdgwRkqhszFD75NvAbViNe7Jl15RvPgK1SLkoa6DIYrQxlgEwaJZxsnCOWRNdKVLmnrfJrwAIIUS6UzZfnL9IxrkkJoK8VwdtsD1jNQOOeB3_jnvDQ9jAH3Gluz_jlaQKqfxLXY37TT17oQXfBOpUJULsAFHH2p78iThLkPECR7KXNeFWxRZxq4ehqDr_Ut3QWfJhUz8d374fd80BY-YifVHegbK-akgkI_GMh2HMYfcatGyDDu2HfFhGkGNF5HTDOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه پَر کالباس 80هزار تومن
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/141515" target="_blank">📅 17:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141514">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075e2967ac.mp4?token=KIcXMhIZOO1Ei7HURywI-1cotGzIrU1CDu0D8oOOe_Z6q-BCBghAW4OdsEMbIfo8wpfADRJbLzbNqqqsiQTAYyvvOIq9TiKVLyL_tjN_4s3xnc18ssxOtpZD3LMT2HNSA8iNgADPz5bkJsV6zNEJghuVKxExhHPM3Bx8-4QBMlIHzxdm03-Xn5hSP4_CzE7SXFmL31xFyp8R8MklguNIBB173sIzLzhzUFdZQkvoUdLa63Rd1PAyiH4gk5oNKwsISMPyGoB2FEQiy6_pBngfq4NfCSzFM7O_Xi2ae8tCPIr9w53hnBAs6ATy276Xdl_h66M2lTdIpPZZUKQcskFRgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075e2967ac.mp4?token=KIcXMhIZOO1Ei7HURywI-1cotGzIrU1CDu0D8oOOe_Z6q-BCBghAW4OdsEMbIfo8wpfADRJbLzbNqqqsiQTAYyvvOIq9TiKVLyL_tjN_4s3xnc18ssxOtpZD3LMT2HNSA8iNgADPz5bkJsV6zNEJghuVKxExhHPM3Bx8-4QBMlIHzxdm03-Xn5hSP4_CzE7SXFmL31xFyp8R8MklguNIBB173sIzLzhzUFdZQkvoUdLa63Rd1PAyiH4gk5oNKwsISMPyGoB2FEQiy6_pBngfq4NfCSzFM7O_Xi2ae8tCPIr9w53hnBAs6ATy276Xdl_h66M2lTdIpPZZUKQcskFRgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه زنه بلند شده میگه من رهبر سوم جمهوری اسلامی هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/141514" target="_blank">📅 17:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141513">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neY3ejk5dmK03Kla9t0ymn_3albBNSSYAblB10sjH0pRHu4BJ8-PggWZEVnR0yOX4foE5vSml1nFUhyz9ifpeEML5hP523oYtfuFlSa55rdOMDvrsILrVhBp8HN6WSo2BFLG1hAr1vnnSQEXckQbe0O4xI7dU0ldrReYqH_F7NotHK8ecYPtswip0yOaZCk40TMUav733lmQsfQzGbsQdngZ-_E-Ial-Ece8R5gqIOhtSFRSPm1nL_nIYV9XFuMVgM-RslvGHsPBezooXlSIT7D41DoFRZNeMmXWYChMDMwOvGlEdTlSnVfM9R_UPbW4nTaPdRuH2dtQzqRfP_I9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مخبر:
راهبرد قطعی رهبری مبنی بر تهاجمی شدن جنگ در صورت تحقق نیافتن شرایط ایران، بدون شک معادلات قدرت را در جهان دگرگون می‌کند با اثبات ناتوانی آمریکا از محافظت متحدانش در خلیج فارس، پایدارترین‌ راهِ نظم جدید در منطقه، اجرای سازِکار‌ اقتصادی-امنیتی هرمز، مستقل از تضمین نظامی واشنگتن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/141513" target="_blank">📅 17:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141512">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
روسیه یه شرکت لجستیکی اوکراینی رو تو شهر پاولوگراد هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/141512" target="_blank">📅 17:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141509">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a179373787.mp4?token=Lxqj9M7UYyKZUkU_DRyEvXAbwEZz8d2tk-98_pVC_OKvlrfnJoUcGaWToZ07vxrgQTBcP430U7FWRLFQmEe9UzF_-Sq6eqIX8z_tZiY54ZWNOwT4AXURGkKArR2e8vHxZO2B9tNVpBtGG58KuyDg4YrgT7XQqSlX9ryr2NoX8ExdYQ8DOM_SeVioH3U7Ilxmdge3LkCrJ96TbxG5dT5qKaSHIylzgSrCE8n36pVXK1zqo0PsibOwDc1E_oRj3N5ACebVwN4zxDGFDpsv5OSshUPl1fECiJjzpZlasmBqIINh9FJG85viHi3ZMgYUrejYbrsONzvCJFlB_L9we0dTGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a179373787.mp4?token=Lxqj9M7UYyKZUkU_DRyEvXAbwEZz8d2tk-98_pVC_OKvlrfnJoUcGaWToZ07vxrgQTBcP430U7FWRLFQmEe9UzF_-Sq6eqIX8z_tZiY54ZWNOwT4AXURGkKArR2e8vHxZO2B9tNVpBtGG58KuyDg4YrgT7XQqSlX9ryr2NoX8ExdYQ8DOM_SeVioH3U7Ilxmdge3LkCrJ96TbxG5dT5qKaSHIylzgSrCE8n36pVXK1zqo0PsibOwDc1E_oRj3N5ACebVwN4zxDGFDpsv5OSshUPl1fECiJjzpZlasmBqIINh9FJG85viHi3ZMgYUrejYbrsONzvCJFlB_L9we0dTGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز، اعتراضات خشونت‌آمیزی در پایتخت سومالی، موگادیشو، رخ داد. این اعتراضات پس از تلاش دولت برای اخراج اجباری غیرنظامیان از خانه‌هایشان در منطقه وابری آغاز شد.
🔴
پلیس سومالی به معترضانی که در برابر اخراج مقاومت می‌کردند، حمله کرد که در نتیجه، یک زن مجروح شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141509" target="_blank">📅 17:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141508">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh1_wMTx1MUA77geAALj4MpcYaofKruEEhobjUYhlCT3E3appbpwxAVE-lEQwhObzwl45ePRhdd1uszmEoNBjPIGjejHJgEtQt3w0ZM3F0dfJeN4acy83_D1FRIapqi2xXSa7YFu_btm_IZUk7D2VJ9A8N77ljjebKGnV_y3XIzr8jTFpWUwKN0DUDkuaVUVMgNsQTCucyZQJGboN_UbNp4qr6axSwPwX4tcoLnigLM1Albar82TChXAnEdaFnIuCSiZz1EZ7livE_HgrFFK5O2CzGl_j7AZavvKfuAbEMJey-CKZLxjd2qw43Q8dObLmC4JsTGEyu2Bp2mR8m2otQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد ارتش اسرائیل دقایقی پیش به یک خودرو در شهر غزه حمله کرد.
🔴
بر اساس گزارش‌های اولیه، حداقل یک نفر کشته و چندین نفر دیگر زخمی شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141508" target="_blank">📅 16:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141507">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
حشیش و گل به عنوان پرمصرف ترین ماده مخدر در ایران اعلام شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141507" target="_blank">📅 16:48 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141506">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aN0J1We5eA3BHY-qtFZFbYrvMxqGV5xlNRGOuQlsgANqy6r6j7BrpnGd59RgyRlNYivlf8K-HKMuRAlT1DbhGMdT2SC9jEH08WoSKQV5JutqteZ-JuRSj-nWC5r05wbkERYIA-AwlD2qvKNcrbhhAIk-572OaLgfYWNph2zWR4Y4E7f3LWJuE9To31WjASMidAMAWO50JHLlImby4JpvXzIuOeEI14VynUZPJmQgzUMLqP8fUq2ksOqgGZLYdLOhEIMTayqvqbvqaaLdWAa5fI3bGnU02HQeKVFPqAEp86ooJD8Fd50pRxGxP612vWiUJUiqFohwld2VQwzTr0F7NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‏ ️
نامه عروس معصومه ابتکار به مردم آمریکا: عاشق آمریکا هستم نگذارید مرا اخراج کنند!
🔴
فرزندانم فارسی بلد نیستند، و مادرشوهرم در اشغال سفارت آمریکا فقط مترجم بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/141506" target="_blank">📅 16:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141504">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHr7nGhwk5S29JmaTv498xJg41pLYYenOuAl9NbzsjOTl7ob_EvxFqUuazxKJInbMb3GqXc4wFb6och43OzzTxtw9b_muntD0WJ-q0gmlUdt8cNyaAdOVgopA3QyTj2QgRDYHWuSQVY9oNYVgJjqwWbkhhjUjP_Bwx6k-z2NqaUQkgIn8UyfXLphfRhkQOAcgb0tDI7PnlDjaSa_ffMmD1riCCNyH8SGUyw9wHLJeT3fLeQhLO9cwTeNlBlFuklgOVSQajWt3v5IwKCuoPtXAifrrHSNWcvaBQajdXUZ0_VLYmHVcwVKffoGqGUZEOrLPTywawDdPn1ASIc7xxah4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DSLXWzzW6CanWl9--WvhhIJDC9PTP_sEdMlghDEz3L-kHoNkSp6FfHG0pals5Auw1DTMWiav90r7XiPrPu6UFQXOuDX-Kh5_rXO3dNJbqikgrD-rDKW8yK7T4CTRQrLiyAO-XeIxCn2uk7VzbGJJfWWsrLDr2Hir5wKpSiNgSEpLz-vbM6pqpHF9gjv4t20MdW02sQvA9A-d9Ad_jsMwWXUXfTBw64ySt8FrJUdfMis2o0cnnjYLvyicKIqlT8x0j2w7aYMTubfV3Z_md4uiD_5x0PiAOlTwbp8aGQBEZzvpLwlSOdxq1jJiLK_XkwPZ2lk5-YRoN08RA_jvp3PZLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از عملیات تخریب نیروهای ارتش اسرائیل در شهر بنت جبیل، در داخل منطقه امنیتی.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/141504" target="_blank">📅 16:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141503">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏
👈
الجزیره:  ایران هدف خود را طولانی کردن جنگ قرار داده تا درد را برای ترامپ حادتر کند
‏
🔴
واشنگتن هیچ ابزاری در چنته ندارد تا تهران را وادار به انجام خواسته‌های خود کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141503" target="_blank">📅 16:21 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141502">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: خانه ها را در جنوب لبنان خراب می کنیم و با تمام قوا به شهرک سازی در کرانه باختری ادامه می دهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141502" target="_blank">📅 16:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141501">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edd86b4e6.mp4?token=bsX0UklrQ2cWyPBYYRIgWJUaabtSWK_NwFnpnzzZSJJ5dW_QE767KpwqDn-Ez0hn0Y0qpfR6ByLaPzvjXKVMbjEAe4h_0rxIGNy8Z8jOAaLL5seRt6ebByKUtYfXOYdhmWP4ob290ScPvAaVx84q8pro9i4NxkldNQc0eNW8mHzvjP-Gg5DoW1wvh1fUcw4M4hsxdaJJIpsO20sD6wXxkxNrEPLmUObyc7Gu99a_FYf0JC_KGSweD1zcRQK6vcIZ0k32uBQmvO52bYEbeiChDfQsrbQZnM2USIj6bySJVa626_XWKo7dg6eUPU3g02gwJMtUKRZAm0IfWMRzzD40iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edd86b4e6.mp4?token=bsX0UklrQ2cWyPBYYRIgWJUaabtSWK_NwFnpnzzZSJJ5dW_QE767KpwqDn-Ez0hn0Y0qpfR6ByLaPzvjXKVMbjEAe4h_0rxIGNy8Z8jOAaLL5seRt6ebByKUtYfXOYdhmWP4ob290ScPvAaVx84q8pro9i4NxkldNQc0eNW8mHzvjP-Gg5DoW1wvh1fUcw4M4hsxdaJJIpsO20sD6wXxkxNrEPLmUObyc7Gu99a_FYf0JC_KGSweD1zcRQK6vcIZ0k32uBQmvO52bYEbeiChDfQsrbQZnM2USIj6bySJVa626_XWKo7dg6eUPU3g02gwJMtUKRZAm0IfWMRzzD40iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی قرارگاه مرکزی خاتم‌الانبیا: هیچ کشتی بدون مجوز و نظارت ایران امکان تردد امن را از تنگه هرمز ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/141501" target="_blank">📅 15:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141500">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
خبرنگار العربیه: ارتش اسرائیل از آغاز یک عملیات نظامی سه‌روزه در شهرک قصره در کرانه باختری خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/141500" target="_blank">📅 15:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141499">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dska8IY-oFyT0I-pO8G_smBzu8P45E_s1s_9ysDNPUN3h9dVlxRTTN1x2CTb5bJS-nwzptmoIRik5pgyWle14wUDNTMGOt_jcACtYRDZ2EFdEoh-9lyOBtisgJMd_IG8EJMg29yaDgDBVCp8TaF0SDsrJqG_zo8f5PuYpGIEIkj3TeYHcZ5mSgwUxwuAKC-sfA649Y9Y5dS9iYESTk4w0wLAyO_O9nERB0gN5ZoNGruN5YGtMm893LPZt68gEcWHxuLLrPS1XXCVuw_ZlKW4PkP7HBKOxz82_RI_UMDV_Nw4Yq57bWCs1qx5D-Y5n0bPxjPFaaCRjWnqN2obKjYS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ناو هواپیمابر آمریکایی "جورج واشنگتن" به همراه گروه جنگی خود، در حال حرکت به سمت ایران است، این در حالی است که مهلت آتش‌بس بین آمریکا و ایران رو به پایان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/141499" target="_blank">📅 15:31 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141498">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T14NxQ7FNO03Al0zyP7jL_mF2aFF_fxFQeq63iaRUPu3zLkzfPeBwrzuDr11L6QqdJlWYebL4dvpb_FQQ-MLJBKSlISCkro-vdDCKCpVk5oCUZHKeih1TgDEFap2riFOhF0XuRSplUoPxR4eSW_a9r1AXZ1xQFWIwMtgfHXy4iyc6E_W1-yhiCvlPj8aVCGX3PyQUXyz8YqEV5dwrEmaO372sLOEU1_rFl7IUr9S-68ZeJEIAz2eT3sgFi3KRDUkui1AUFDcN76CjOoqq1nqYes6bnPIyuEeXo-Ex4bxWqva5jtwWGhi3qzVZGbVNIPbbFM0GgogrZUiQvdlsYQ8UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۷ کشته و زخمی از نیروهای "درع الوطن" که به عربستان سعودی وفادار هستند، در پی حمله‌ای توسط نیروهای یمنی با استفاده از پهپادها به یک اردوگاه در منطقه "العبر" در استان حضرموت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141498" target="_blank">📅 15:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141497">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sm14OJQhw4pnWwlqA4QsmAd83NnIVZLBPJZaolsH1EdzCdAPzvjnmH_4b6JMNaPB3FLMbEnRkbKd2432qXJID0UQnpcjmStpxyu0wqqrsVrKeNdC2-W91pvLlSY6cw8V2WiW9prVLdXbYYCF56Gbp2sIXo1vUErcxptet6GLlKAVP1dOlxkqSe_2AwVDZfk9hNgYbmCe-3ewHJ-MycOPm3RL4L55uKldedXpYQQYhd4YdOV-c05B624RH0U3TolnAMr1EPhgff-XDXjQyOE7dS0VAFx-EccZ-4fqfR2ZBZ2OHpFpHv5C7gCIMy9vL4ZSoKIqdT_-WXbL0eo26YMHUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش یمن با استفاده از پهپادها، مواضع نیروهای وابسته به عربستان سعودی را در صحرای العبر مورد حمله قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141497" target="_blank">📅 15:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141494">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WVfEFclfK5e-2f3DsDcBDg6Mdk4kkKt9cM2MlG5JvjVhWygr008-x7ijfxuuzl0zzoTmME9_tctYzqiFKPgQ6hetDyFE6rH_3mt1HsT4sS9LfGp4RdznErR3lUX-BdDQ3EM1eirbOX0qi9RLVvY-P-DnE5k1P3GegAW2vR_uZiVTasyqfAIQWdPue7qOKTW_arf6VeeaaNzPz5h5ZrzJTAEavyr8CQXrgqJ9tspc3eLpTjlocOT_YWAjHt6NAMKyWkQsJPrYpmTOdoppjBUK44oROGM_j7hCcsvMJzvHB51rtAdA93-S1q9CAaVn7CxCOK4_QvpNVXOBMsnmpDoKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NotEXejBSb9vVlwHT5W6jL3Gt3X0GzGsvBrHRCzwbWw-kp7pMHwfbnyNVqPnvYnLbJLNugrxjY-fO-dcGh2Zgv-9OLovrGYh2ZNuBxPQffhFYB_JQZZcKw4F1UAqeKbTbJhK_tx20mPM6CBRY64IxY5ilQa4sIvZ9HbTBlrg75vqgEfMSeuWdeEO-OwYu3E99otxbIOXE9pvlD2xnPbXiqpRF4s25A7Eb2oRHkw5BosgLHJq1KOwdu4Y4mj2x36Ya9CGo2j6n17HAPT_2msOQJPFbgh1lQAppHyNxMdawNvOnRXiqijXA_S8-A7l56GbGQ--dSv7IFRneHPDmo9nXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGi3KHn2TIufZD-xUOq3JlEKw3gymhu1NtqK12_EMGBpaAA2Pt6dhGnx2OCoDLPq8v0jXdHqMG5AUjFAgRHSUzTrgN-lEPoOGDbArfkl8ApaSe4QRy3ZB5DjTHKSPTcaSq-ryiZmerv7N9VRm7dIEMDG9z2b5n8vLKLZ2htOqW2UScA5yoH1X-gW0c5Y8_z_ILoVCA7uUpDaeCdWyJTsIRMrGaRUHARqNLCbguV31Q4kc1h5iSRFGwhq2-DMNU1SsHhGD3YLQof1vXqNRCreXN53_C-GxCgtBhIrk7mfDuWN_8GfTHsCNgxVDcXxQ9mF2TQ2sjqg3QD9MWej8lZAHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
وزارت دفاع اسرائیل : هزاران تن تجهیزات نظامی، و وسایل نقلیه جنگی از آمریکا به اسرائیل رسیدند. این خرید و حمل و نقل توسط وزارت دفاع و ارتش اسرائیل انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/141494" target="_blank">📅 15:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141493">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پلیس هلند از کشته شدن یک نفر و مجروح شدن چندین تن در پی وقوع انفجار در بندر روتردام خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141493" target="_blank">📅 15:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141492">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/244de8d332.mp4?token=LYoV_BibPsTvJpd-pwjOh9f1XUlln4eayXcRP80wVcf1PFCr-s55uBvn3mDfaUneYZED0lI3NkOwYFIy22l0SWPN1DyTSL31o3raJixjihYR4A_7AqYRzqRQ-k1KRKK0v5JhvY5TNTP_gCparOvU9RR1f7nkBJGXLPogNgxVhk0UOZ5Id6SCb4Itz5p-NaRNUyExr42oBthyX9FYtIpPGkUxUGf4vLb9z-BCBjdsoNgLj3dZlUIIrXAK9eaPGlnXTkeiWcYmfE3T4QfMxd8VP1Nk2nPAtrWztofkiA_ulvdfHQLBAjgHTnwEbJ5pKTl5ZDNobPWeddrqwIW3-AeApSAosgmGBg2B4dy3P0_9RdlUvBAJ_mRuCQ1Y-AjOKylx97giRi7smE8lF-1Bv98zkYsnG0_I9jDtQ1EwBjvDseMKNvvSPkF_-fFmM8vhoAuugJqY23fltnQbxw86SvZDfNSkIXgB1FUPNUTEC5Jy7p03XAFcBl1-n_Ixj4pEcn-XtSrQ-jXwTQnN8r7f6uRKtDH7Ho8Dta8TGyTJm78iuKZwIp9tTNUm4-pPTzFeNM6ovf37Nt5G3Kegfp90WtxFAYh2vWPpVO7Lpg2jWuBgVCThFv2ZticdCDY3QWuma4HBIRwRdszeF8iCA4mG3gfukU0SYCUutf-6WodLRXGpXMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/244de8d332.mp4?token=LYoV_BibPsTvJpd-pwjOh9f1XUlln4eayXcRP80wVcf1PFCr-s55uBvn3mDfaUneYZED0lI3NkOwYFIy22l0SWPN1DyTSL31o3raJixjihYR4A_7AqYRzqRQ-k1KRKK0v5JhvY5TNTP_gCparOvU9RR1f7nkBJGXLPogNgxVhk0UOZ5Id6SCb4Itz5p-NaRNUyExr42oBthyX9FYtIpPGkUxUGf4vLb9z-BCBjdsoNgLj3dZlUIIrXAK9eaPGlnXTkeiWcYmfE3T4QfMxd8VP1Nk2nPAtrWztofkiA_ulvdfHQLBAjgHTnwEbJ5pKTl5ZDNobPWeddrqwIW3-AeApSAosgmGBg2B4dy3P0_9RdlUvBAJ_mRuCQ1Y-AjOKylx97giRi7smE8lF-1Bv98zkYsnG0_I9jDtQ1EwBjvDseMKNvvSPkF_-fFmM8vhoAuugJqY23fltnQbxw86SvZDfNSkIXgB1FUPNUTEC5Jy7p03XAFcBl1-n_Ixj4pEcn-XtSrQ-jXwTQnN8r7f6uRKtDH7Ho8Dta8TGyTJm78iuKZwIp9tTNUm4-pPTzFeNM6ovf37Nt5G3Kegfp90WtxFAYh2vWPpVO7Lpg2jWuBgVCThFv2ZticdCDY3QWuma4HBIRwRdszeF8iCA4mG3gfukU0SYCUutf-6WodLRXGpXMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حاکم دبی در لندن مشاهده شد
🔴
محمد بن راشد آل مکتوم، حاکم دبی و نخست‌وزیر امارات، در منطقه چلسی لندن دیده شده است
🔴
تصاویر منتشرشده او را در حال قدم زدن در خیابان‌های این منطقه نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/141492" target="_blank">📅 15:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141491">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
پاکستان: مهلت ۶۰ روزه مذاکرات ایران و آمریکا قابل تمدید است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/141491" target="_blank">📅 15:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141490">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
اوکراین: ما مجتمع گازپروم در باشقیرستان روسیه، بزرگترین مجتمع پتروشیمی را هدف قرار دادیم
🔴
ستاد کل ارتش اوکراین: مجتمع صنعتی گازپروم توسط پهپادها در فاصله ۱۳۰۰ کیلومتری داخل خاک روسیه هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141490" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141489">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است
🔴
کنعانی مدیرکل حفاظت محیط زیست مازندران: تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141489" target="_blank">📅 14:51 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141488">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نتانیاهو: شاید بتوانید بریتانیا را «جمهوری اسلامی بریتانیا» نامید
🔴
یک نفر گفت که اولین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141488" target="_blank">📅 14:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141487">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ناو آبی‌خاکی از رده خارج‌شده USS Peleliu (LHA-5) با وزنی نزدیک به ۴۰ هزار تن در جریان رزمایش RIMPAC 2026 و در آب‌های هاوایی، در یک تمرین نظامی به‌عنوان هدف مورد اصابت تسلیحات مختلف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/141487" target="_blank">📅 14:42 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141486">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزارت دفاع ترکیه اعلام کرد که بر اساس توافق مکه، رزمایش‌های نظامی مشترکی را با عربستان و پاکستان برگزار خواهد کرد.
🔴
این وزارتخانه همچنین تاکید کرد که توافق با عربستان و پاکستان بر تولید مشترک صنایع دفاعی متمرکز خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141486" target="_blank">📅 14:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141485">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
نتانیاهو: شاید بتوانید بریتانیا را «جمهوری اسلامی بریتانیا» نامید
🔴
یک نفر گفت که اولین جمهوری اسلامیِ دارای سلاح هسته‌ای، جمهوری اسلامی بریتانیا خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/141485" target="_blank">📅 14:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141484">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ادعای یاهونیوز: امارات میلیاردها دلار از دارایی‌های بلوکه‌شده ایران را آزاد کرد
🔴
پایگاه یاهونیوز با استناد به برخی منابع رسانه‌ای مدعی شده که امارات متحده عربی میلیاردها دلار از دارایی‌های بلوکه‌شده ایران، از جمله محموله‌های طلا را آزاد کرده است.
🔴
یاهونیوز نوشته روز پنجشنبه بعد از انتشار گزارش‌هایی درباره اینکه امارات متحده عربی دارایی‌های بلوکه‌شده ایران در بانک‌های اماراتی را آزاد کرده است، قیمت نفت کاهش یافت.
🔴
بر اساس گزارش رسانه «هرمز لتر» (The Hormuz Letter) و سایر منابع در شبکه اجتماعی ایکس از جمله دارایی‌های آزادشده ۱.۵ تن طلا بوده است.
🔴
برخی منابع، این اقدام را سومین جابه‌جایی از این دست توصیف کرده‌اند. ادعاهای قبلی در گزارش ماه ژوئن خبرگزاری رویترز حاکی از آن بود که امارات با آزادسازی ۱۰ تا ۲۰ میلیارد دلار موافقت کرده و بیش از ۳ میلیارد دلار آن در میان جنگ آمریکا و ایران تحویل داده شده است.
🔴
با این حال، وزارت امور خارجه امارات در آن زمان این گزارش‌ها را تکذیب و اعلام کرد: «هیچ‌گونه دارایی بلوکه‌شده ایرانی از طریق امارات آزاد، منتقل یا تسهیل نشده است.»
🔴
مقامات آمریکایی نیز ادعاهای مربوط به توافق‌های جانبی یا آزادسازی وجوه ایران را رد کردند.
🔴
گزارش‌های اخیر نیز تا تاریخ ۱۳ اوت هنوز توسط ایران، امارات یا آمریکا تایید نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141484" target="_blank">📅 14:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141482">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYWxWfDOSyj3c7wqkMQKN2bBoij0JU8yzYe3E48lih4csNJPInz25HDYvfCNeIfIn8N5sQ4lsHP9gWFJKTxq5mtajEwNpjZd_as-oWoc2A47zj2Hbdxusk1ADpBQRlqzHSoBa0z_4XBETeXfWq5206wPQ-_WrbCJVUH6tnXbPIb78KJbZm_Wtq4-1-ZY2uNHPI2zGHCN2xbPLf5qNCjKz7mE57ThqRlWYIrU909a_9bYgOLwqz5KyEihx4FMfWz4OYCcOqZlqt9voAtbo-Hghr77kebzBPUab6WqqWoTF5viwnIJJgrYYTClhDibDnwFHEG8wrmzz8XBa1evcpgV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=KXKKPIiv88iCgf7Zmcyp6N1OyAyrmxkgYjxe444b4q1VuGmwEVK7ye00rn_2uwzScNCbJoxI1kdVRN74OZCrZsYwuZGM8XZHBhsaYLP6yX8uispcT9vkZm_mfYcpJyZ6lmPEJiEo3EFS_qOQrtpFx8xINvs1VkL04lvJ7EsOj-3h5D8qPBCB0SfZCW1xjISxW8qpLiGXumiiVhAdckAh4Z0FkT-N-JqTCZeo0NpxezSq28lCK3J9P4HnNWAS7BqvjAs6WYxQwmdpU49gqwtp6NGeLD4DH_lWiB6Qf1bht8ti42GK-jQH6IVhOqcHDmvnNqnZ0oJAGzstUjPKx4YzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=KXKKPIiv88iCgf7Zmcyp6N1OyAyrmxkgYjxe444b4q1VuGmwEVK7ye00rn_2uwzScNCbJoxI1kdVRN74OZCrZsYwuZGM8XZHBhsaYLP6yX8uispcT9vkZm_mfYcpJyZ6lmPEJiEo3EFS_qOQrtpFx8xINvs1VkL04lvJ7EsOj-3h5D8qPBCB0SfZCW1xjISxW8qpLiGXumiiVhAdckAh4Z0FkT-N-JqTCZeo0NpxezSq28lCK3J9P4HnNWAS7BqvjAs6WYxQwmdpU49gqwtp6NGeLD4DH_lWiB6Qf1bht8ti42GK-jQH6IVhOqcHDmvnNqnZ0oJAGzstUjPKx4YzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل درحال حمله به زون، جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/141482" target="_blank">📅 14:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141481">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
عضو کمیسیون انرژی مجلس: هزینه تولید و واردات بنزین به ۵۰ هزار تومان رسیده و من صحبت هایی از هزینه بنزین ۷۰ هزار تومانی هم شنیده‌ام!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/141481" target="_blank">📅 14:24 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141480">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است
🔴
کنعانی مدیرکل حفاظت محیط زیست مازندران: تراز آبی دریای خزر به پایین‌ترین میزان خود طی حدود ۲۰۰ سال اخیر رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141480" target="_blank">📅 14:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141479">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
خبرگزاری اینترفکس اعلام کرد یک مقام نظامی روس در انفجاری در کریمه کشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141479" target="_blank">📅 14:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141478">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
قیمت آتی نفت برنت با ۴۲ سنت یا ۰.۴۷ درصد کاهش، به ۸۸ دلار و ۵۶ سنت در هر بشکه رسید و بخشی از رشد حاصل شده در ۶ روز معامله گذشته را از دست داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/141478" target="_blank">📅 14:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141477">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
الجزیره: بحران تنگه هرمز، بازارهای آلومینیوم را با تنش بیشتری مواجه کرده، قیمت‌ها به بالاترین سطح در ۷ هفته اخیر رسیده و ذخایر جهانی به سطوح تاریخی کاهش یافته
🔴
این وضعیت ناشی از نگرانی‌ها از اختلال در تأمین‌ آلومینیوم و پیامدهای آن بر صنایع خودرو، هوانوردی و ساخت‌ و ساز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/141477" target="_blank">📅 14:10 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141476">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba390ce5a.mp4?token=kG1XQrCIeIuy_uJvfF0ATitkp-i0iiMfqQ60_m2yNGCXnhe2QMZ0Oq0_6LQA1B8d6H7cU0kZDE2I1TBvBPLd2_XVWQz3xW357cxwFWMymHHM6T3zREzpvJLupFdY5cua5R_RAqp9NjLLeVhzOa0WsRUDcPNRzPRRUOk4gZZbGwNG3uWFIG07ngFQzIq9UxHCHhbe3eE8XmUrtVayVXXxbNF9hxlwT7fkbLwt2fAroZrNbIT7Sm-LoDC1NxoIedGJ3uWc-LvdRp2Sy-bEBRsbj-JZ60k7vJmqIetUkio2zWsHYs94HS2skQsiSyICiGCF4J854plSEt-jxHyXu8HW95_1K_DWtDsQmabPCpbpZuqFlzW33fcff00vIJyyBBrUvKYlGfw5T1-tDPkt5ZUdcgGFNu7DSkGrV96_KjzBx7znBQ8QDN9BrY9fFWsr5yME26J8Ev27irvhiV-A7TpIydFzJNEovU1TqkS21CV-DpHG19Qp8RYI_Gfaeagk5_3lPFRw5qf9nIuVdKs93cFauHfUTKb4Eo0iDSrjnIfXiUiMU8tRw3Jp5qP-I2SW0Hxq3zq3y47gw47BtPUM4NXiCEcYvqliQ4dvRtHWchscHB84eoEQ6mdpY2auKOKYm0n3YTkqP835xX9ErbIKG8WcEjO8YZrl9QBFKl91UbV6kNc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba390ce5a.mp4?token=kG1XQrCIeIuy_uJvfF0ATitkp-i0iiMfqQ60_m2yNGCXnhe2QMZ0Oq0_6LQA1B8d6H7cU0kZDE2I1TBvBPLd2_XVWQz3xW357cxwFWMymHHM6T3zREzpvJLupFdY5cua5R_RAqp9NjLLeVhzOa0WsRUDcPNRzPRRUOk4gZZbGwNG3uWFIG07ngFQzIq9UxHCHhbe3eE8XmUrtVayVXXxbNF9hxlwT7fkbLwt2fAroZrNbIT7Sm-LoDC1NxoIedGJ3uWc-LvdRp2Sy-bEBRsbj-JZ60k7vJmqIetUkio2zWsHYs94HS2skQsiSyICiGCF4J854plSEt-jxHyXu8HW95_1K_DWtDsQmabPCpbpZuqFlzW33fcff00vIJyyBBrUvKYlGfw5T1-tDPkt5ZUdcgGFNu7DSkGrV96_KjzBx7znBQ8QDN9BrY9fFWsr5yME26J8Ev27irvhiV-A7TpIydFzJNEovU1TqkS21CV-DpHG19Qp8RYI_Gfaeagk5_3lPFRw5qf9nIuVdKs93cFauHfUTKb4Eo0iDSrjnIfXiUiMU8tRw3Jp5qP-I2SW0Hxq3zq3y47gw47BtPUM4NXiCEcYvqliQ4dvRtHWchscHB84eoEQ6mdpY2auKOKYm0n3YTkqP835xX9ErbIKG8WcEjO8YZrl9QBFKl91UbV6kNc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مسعود نیلی: امسال رکورد تاریخی رکود تورمی را در ایران تجربه خواهیم کرد!
🔴
با خروج آمریکا از برجام ۱۰.۵ میلیون نفر به زیر خط فقر مردم اضافه شدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141476" target="_blank">📅 14:04 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141475">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
هواشناسی: گرما تا یکشنبه در بیشتر مناطق کشور ماندگار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/141475" target="_blank">📅 13:56 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f465758dd.mp4?token=c0u5f6Qgh1CnrXeVcoeTXeXq7BvIApflCiWFtIJFnq1E2dszj-WTgJ0pjPS5HoXqUcQ7coqiaSjqWFNeapibAt3lMu4Fammk8-3JvuynxaMLMPCva1hcQwprwxVtjj9QBtXrjOKkOJE-YVoWhIIbqzRWBOPqW-DHWnub_A3NNtO8j5XIZtfJ2AyJCaBsoaV0F5jtKL9cHPcz_-1c0bqw90udyZf5Lu4aLbpLzH3Hoia1ZIhNzVoMeJ_xjIwBtWBOpG8Q2SJPhPEc85ssbvp_TBueDrV1BoTXWx7YFaQpnPgi5kr2DRcRR7nOojeE4ugn_CMUm-oqQERiR9O0mDedoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f465758dd.mp4?token=c0u5f6Qgh1CnrXeVcoeTXeXq7BvIApflCiWFtIJFnq1E2dszj-WTgJ0pjPS5HoXqUcQ7coqiaSjqWFNeapibAt3lMu4Fammk8-3JvuynxaMLMPCva1hcQwprwxVtjj9QBtXrjOKkOJE-YVoWhIIbqzRWBOPqW-DHWnub_A3NNtO8j5XIZtfJ2AyJCaBsoaV0F5jtKL9cHPcz_-1c0bqw90udyZf5Lu4aLbpLzH3Hoia1ZIhNzVoMeJ_xjIwBtWBOpG8Q2SJPhPEc85ssbvp_TBueDrV1BoTXWx7YFaQpnPgi5kr2DRcRR7nOojeE4ugn_CMUm-oqQERiR9O0mDedoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه قایق ایرانی رفته تو تنگه هرمز برای ماهگیری که یهو هلیکوپتر آمریکایی میوفته دنبالشون، واکنششون خداست
بنده خداها اصلا جرئت نمیکنن نگاش کنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.8K · <a href="https://t.me/alonews/141473" target="_blank">📅 13:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141472">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2g9nxwRdUojksoytjCzbGSjfrfENtd-Sx5mb42zUs2Nt4Rdn-PI0sofj1wGcvegmVbxPvQg_uzw5CTj9HlcE-rXdLuMaA7PiTrj8mCBYEbsbrx2glXkdNSeqL9oGcLSrOxgz9HnVzLNR7TxbKuf2Ilvtp13EaQ3HDRz9ESOsadcIiDgtyzGHc-2iCPEr-RAfEtZnRJcaRAXUcPcjq_nnDXSr0_sDj9v3OFKD6PEEdxxUwda0mtuo5dUnQkOLM3lSnD5xUO_Hg1ELl4gRKwHy89owViTi_4141EDs3LO1beqtZVOLMf2707XsWEAw6Db34k0Swk6HHQQ6ipKrZyZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پرواز یک هواپیمای باری ایرانی از فرودگاه تیانجین چین به تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141472" target="_blank">📅 13:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141471">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgCc-fA0ngyqTHB6wQU_dcSqx1LHIUcxt1NxlMhVM6OcpOzk7EGWWi8RmzC836ZbF8L8af7gpkscbCzDB4T3M6m_mP4Ktr-I7laUDVOdYR2a5enbFG_N9fggs7UYRCdVRUzuQLGacMEt5Fgd71DvuNBWgJ03MYjCjm19CAN2M_P-1ZO_NeDW3tqy6GMTp1anlNMH-YwCApjwzc5viRB5tmw3u15U4hCMWknUYGg1Wjr6JKhVo3aVU25Oh1iNjSZgImu36taZYxVeZRhTTXHuatUg3CZYW70ViC2iFnRhkYuC5y2W8DUGuNRA1NBYuAs4NLuZzC40M67T_M6EVTUiEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
مردم ایران با میانگین درآمد ماهیانه ۸۵ دلار در در بین کشورهایی که پایین ترین دستمزد ماهیانه رو میگیرن رتبه ی سوم رو بدست آوردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141471" target="_blank">📅 13:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141470">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
وزارت دفاع ترکیه:
توافقنامه مکه با هدف ایجاد روابط پایدار بین ترکیه، عربستان سعودی و پاکستان امضا شد. ما به دنبال انجام رزمایش‌های نظامی مشترک با متحدان خود تحت این توافق‌نامه هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141470" target="_blank">📅 13:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141468">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbmIOEPSKBtrDPYgyHsAzBMZM3Fe0pi2dIvfy0CHpSN4rcZDq6gOk0TZj1HrkZrRVjcG4GDRiS9wSoVWv_9436czPJYpd32rkATvYPQpejpGdlqQWWyx0DaOMyx7Bmt3w1yfHwtbg2VZ3wP5-A9wlJJholaAX1d8xdhnwjfl2LZHcnilVcXTquMEJZu3OvVZMlq0MufzLQirJ18x2Axz2FizUQxc0yJIuyHuGPBCAjJ6mawkvqD17T_AAHuV-vUxCb14nv5YBJlxbbXyJv6bvIaTODovFzey8KTVJ5bSJyPh1TZ8K0YUd1N4iCbdQgqG3SHPrSRiCxjRyO32omgjqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=Aw-11VuX-YXOFVa_anbIOOPrqLvDftpeoNQQCDV7tVQ5cURnGJVLJkGXztF79rMEoeb8UiJSW_NqBWHn9Oj5Vf9QpygG07KVazDem9dvD9wtHD2vlWFHocns9DIQIKNjHGtg1Vm2Tpjmwi9NQZqJ02ALpJa8dO2rRsF2tSY1EFlTn-Bw5W-EOiCSlgwCy3nHHTka04E4VKU6DjeHbkJrPwDBBDGQ9ZN9MUc5XrHMdLKh5gMw3GxqlN0EF0LPQq5xdfcOT-HhB80Sue3E4WgnkaDrvh2Z0LaugrPlvMuc7XNbdb5qqNm-ez_lxqTvDkuuvbc-9jO1su3jogt19k-Z9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57dfcf5d58.mp4?token=Aw-11VuX-YXOFVa_anbIOOPrqLvDftpeoNQQCDV7tVQ5cURnGJVLJkGXztF79rMEoeb8UiJSW_NqBWHn9Oj5Vf9QpygG07KVazDem9dvD9wtHD2vlWFHocns9DIQIKNjHGtg1Vm2Tpjmwi9NQZqJ02ALpJa8dO2rRsF2tSY1EFlTn-Bw5W-EOiCSlgwCy3nHHTka04E4VKU6DjeHbkJrPwDBBDGQ9ZN9MUc5XrHMdLKh5gMw3GxqlN0EF0LPQq5xdfcOT-HhB80Sue3E4WgnkaDrvh2Z0LaugrPlvMuc7XNbdb5qqNm-ez_lxqTvDkuuvbc-9jO1su3jogt19k-Z9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش اسرائیل درحال حمله به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/141468" target="_blank">📅 13:05 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141467">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‏
👈
انجمن تهویه مطبوع: مردم بخاطر گرانی و نداشتن پول کولر رفتن سمت خرید پنکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141467" target="_blank">📅 12:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141466">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
نشریه فارن افرز نوشت: «آمریکا ذخایر تسلیحاتی خود را در منطقه از دست می‌دهد. ورود به جنگ برای واشنگتن آسان است، اما هزینه‌های پنهان اقتصادی و کاهش توان مهار چین و روسیه، روند افول آمریکا را تسریع کرده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141466" target="_blank">📅 12:49 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141465">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgHaR5tXw-p8hq0k2T100VNNn6PzxrWhPO0BQjKHjuxJa8NtEOlhaPxZGD8f3T9KxyR53w75JcmaIvipCRaST1hAtHKeFa9ewOiKOOV9F7YW2Tb-RZnpkIQLk1k75o5UAIh9gnCL2VEDvafI9DKT_eJEmg0zy5O3LwQQrokIuR-8dRqAJxVTvuMiI5_6xgGEwThQZ9WSsarG9ksc-yrW5yjukDhe7DyXWcB8UqdgqU9JULY0Iohp3idtQ-KHL9g0p1VADTH5gm5s93BpcJ3_0NBLbv7xWVqhvHSR3-dKRdPYAlohhwAVFwYREkneqRg60epQwueHAYeD2KSE7MQ-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
عضو کمیسیون انرژی مجلس:  طرح گران سازی بنزین از اول شهریور طرح مشترک سازمان برنامه و وزارت نفت است ربطی به سازمان بهینه‌سازی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/141465" target="_blank">📅 12:44 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/985e98ad84.mp4?token=q-wy0AYRuwLDegre8oAd9ZDv-5QkRKIjQiO1Wn71gE_qyf0YuS2HdKkWBsgQ7q_vP7iWE5pYYqfRkXdlQ4j6ne4TQvO5usFQs1vKgKYizlwKQc7w_aoGar7QkkGODCzHI-y95V0xrOJ9c0Gzuze_HCgO6z5i3dx3f7Tl3jopNnGf9JI4YD2EjCj6NXhcmndL7t2YXepIEmZ_fUSwo1n4mqNAN_3YTxVoDYn6UKx3zptM38tvW9NtSlbrIu89EgVYqvSLy1DoPEB33cmonJv0dFRm91fADsj3fc37Ot2T6HIHUn_tA1XKADsqEKF80h7Rk0n7-8Qe10e2w58OphkLRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/985e98ad84.mp4?token=q-wy0AYRuwLDegre8oAd9ZDv-5QkRKIjQiO1Wn71gE_qyf0YuS2HdKkWBsgQ7q_vP7iWE5pYYqfRkXdlQ4j6ne4TQvO5usFQs1vKgKYizlwKQc7w_aoGar7QkkGODCzHI-y95V0xrOJ9c0Gzuze_HCgO6z5i3dx3f7Tl3jopNnGf9JI4YD2EjCj6NXhcmndL7t2YXepIEmZ_fUSwo1n4mqNAN_3YTxVoDYn6UKx3zptM38tvW9NtSlbrIu89EgVYqvSLy1DoPEB33cmonJv0dFRm91fADsj3fc37Ot2T6HIHUn_tA1XKADsqEKF80h7Rk0n7-8Qe10e2w58OphkLRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری متفاوت از خورشیدگرفتگی از داخل یک جنگنده و یک ایرباس!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/141463" target="_blank">📅 12:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141462">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزارت خارجه: لفاظی‌های نتانیاهو درباره تعلق همیشگی بلندی‌های جولان سوریه به اسرائیل و نفی فلسطین را به شدت محکوم می‌کنیم
🔴
او در جایگاهی نیست که راجع به تشکیل دولت مستقل فلسطینی اظهار نظر کند
🔴
موضوع فلسطین همچنان مهمترین مساله انسانی و اخلاقی دنیای معاصر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/141462" target="_blank">📅 12:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-141461">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57340e99a3.mp4?token=btWrf1sBp-Lxz6BqGfP0E3Db6bQbrkoBhK3eo76eOvEsRUay7kTaJ6ONFII7NaUvXw96OoYhZCQP9J_pNpfkH8kAjnTkkyyOVTjJStFvRtwpUhX18R4dTSIj7kwVRt3MGQ6Au_7od37vJiXPq2dU83L3jysoJ1Tt9EKjbAYpheaGfsTvg9t119F41V3LM03Fr5knieqpt1ZN5k_jzT6SwH3kXCiIHZm625bRbzI6NbBu9tT7kXRwnwH6As_Qp5puqplIVfQDdHO4uX1TNPHQPlsX8-u4vSOAqRC3qhBCGwbZ-BlZpDOI7I--v1I6mZKuFg0ZnDZCKunXbyl6zeUn9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57340e99a3.mp4?token=btWrf1sBp-Lxz6BqGfP0E3Db6bQbrkoBhK3eo76eOvEsRUay7kTaJ6ONFII7NaUvXw96OoYhZCQP9J_pNpfkH8kAjnTkkyyOVTjJStFvRtwpUhX18R4dTSIj7kwVRt3MGQ6Au_7od37vJiXPq2dU83L3jysoJ1Tt9EKjbAYpheaGfsTvg9t119F41V3LM03Fr5knieqpt1ZN5k_jzT6SwH3kXCiIHZm625bRbzI6NbBu9tT7kXRwnwH6As_Qp5puqplIVfQDdHO4uX1TNPHQPlsX8-u4vSOAqRC3qhBCGwbZ-BlZpDOI7I--v1I6mZKuFg0ZnDZCKunXbyl6zeUn9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک عضو کمیسیون امنیت ملی در پارلمان ایران تأکید کرد:تنگه هرمز تنها در صورتی باز خواهد شد که ایالات متحده به شرایط تعیین‌شده پایبند باشد. مذاکرات بین ایران و عمان به هیچ وجه به معنای باز شدن تنگه هرمز نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/141461" target="_blank">📅 12:27 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
