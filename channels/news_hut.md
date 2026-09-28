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
<img src="https://cdn4.telesco.pe/file/TnPraY2FCYOGaAWYQVVPuKAdO4LnYxurvatDaHwk85tOlUhKTrNuV3qIxV6m0BQO1umIh6zrTOnNshR0Ugr2Z1wDtc3YB1L5nN3_c20m3WEt4wuIwCEC-hMKbOHrCDY1Y6kirqBI9ZsEF8NpeIe33mDfpnekPWmooPyvT2pEU5AaF3P1G9VIWVcmRT6R4pDf1Rjco0Gxkq2IwPOQC8tSkEWMotzPL55mlFVahU02yQs6QI-FA5HaeWBzpwNoFl-6vC4dPhjjgqmX8Ke6NJZ7LXy6vDdwc5icge0ZyN4NV3MCX5f6drbCKIDRljTAv9QFoFYsy3-1Bzf3se9ZQIlabA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 12:39:35</div>
<hr>

<div class="tg-post" id="msg-72400">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">۱دلار=۲۴۰.۰۰۰ هزار تومان
@News_Hut</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/news_hut/72400" target="_blank">📅 12:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72399">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=BBvV3au43NV1Qn2Q7BHGN5QcX5QijkeNcuTiSGxHsVJ_v1MFjxwTskb0LuHPDtugZkNqd13AbeKHPnU7qYMmb5kbnBOtakzW9-_k4XLLuMp7AkaeFm6_4tdPbLDuPDPm3X5_S3FTRr9jVnWMewVWDHgY-GFcPNYTsbjOWpNLro-GtSPtXusda4U7dya-RmlliyavPpq7PaFeIsCED8Kbmx7cjKY8boTniO8Tvn7C8RfqcTTwy92gRUyDwsghk505AaU3XO1QDsA2Kw1Bk2arIm72lzRurO5v7wqKuuQSXD9Xo_ciz8UMjrJLtOBkrIxayWDSzizTeFqd0HO8SO3x4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc45d0630.mp4?token=BBvV3au43NV1Qn2Q7BHGN5QcX5QijkeNcuTiSGxHsVJ_v1MFjxwTskb0LuHPDtugZkNqd13AbeKHPnU7qYMmb5kbnBOtakzW9-_k4XLLuMp7AkaeFm6_4tdPbLDuPDPm3X5_S3FTRr9jVnWMewVWDHgY-GFcPNYTsbjOWpNLro-GtSPtXusda4U7dya-RmlliyavPpq7PaFeIsCED8Kbmx7cjKY8boTniO8Tvn7C8RfqcTTwy92gRUyDwsghk505AaU3XO1QDsA2Kw1Bk2arIm72lzRurO5v7wqKuuQSXD9Xo_ciz8UMjrJLtOBkrIxayWDSzizTeFqd0HO8SO3x4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلما، ماده‌یوزپلنگ هفت‌ساله ایرانی، چهار توله‌اش را به‌دنیا آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/news_hut/72399" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72398">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پرزیدنت ترامپ:
به‌جز نفت — که [قیمت آن] پایین‌تر از دوران دولت بایدن است — و این واقعیت که دیگر لازم نیست نگران سلاح‌های هسته‌ای ایران باشیم چون [آن‌ها] از بین رفته‌اند، قیمت همه چیز در حال کاهش است.
@News_Hut</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/news_hut/72398" target="_blank">📅 11:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72397">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=Uj9eBNSu0uOq_nCYdNwuPWAE72nJhwIwpJKDRRtrVgu3SQZOC1kZaMA4QJ6heRx8d_MZTSdVXL2nYPN-dMRNKk37DHJqsZy6perkSq061W87wW3JQfenhGIw8h6BRajlLkJbrhCUQGxnaU2rdXcvVWCMuLdXEOPZqj_OEj7LFGm5gnLlCSFFZZM6X63Ak0XQKb7tHsmJWkjUAG9iQq2l8jIHGHuULIdJPxRJNTCrMeBKV-UyaCX5EwDjegB3_f-24nLFYXpRN36rCmx0ryPoefvumxTesJUiN-FbpIzsB7MKYdtpptz4_GuZGNT00Usgqs-VuyONY9DBA7Ok3jzgOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe7cda202a.mp4?token=Uj9eBNSu0uOq_nCYdNwuPWAE72nJhwIwpJKDRRtrVgu3SQZOC1kZaMA4QJ6heRx8d_MZTSdVXL2nYPN-dMRNKk37DHJqsZy6perkSq061W87wW3JQfenhGIw8h6BRajlLkJbrhCUQGxnaU2rdXcvVWCMuLdXEOPZqj_OEj7LFGm5gnLlCSFFZZM6X63Ak0XQKb7tHsmJWkjUAG9iQq2l8jIHGHuULIdJPxRJNTCrMeBKV-UyaCX5EwDjegB3_f-24nLFYXpRN36rCmx0ryPoefvumxTesJUiN-FbpIzsB7MKYdtpptz4_GuZGNT00Usgqs-VuyONY9DBA7Ok3jzgOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صداوسیما:
در مقابل محاصره هوایی، می‌ توانیم بین پروازهای غرب و شرق کره زمین دیوار ایجاد کنیم و روزانه ۲۵۰۰ پرواز را مختل کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/news_hut/72397" target="_blank">📅 10:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72396">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=B5nWKWLXjyNdC6UwvPS7zzlgYzl4ztC7xnaTTKP6IANNkGycfu95ij7gJ_GfNZvDS_tHnX3wNPtcQ8Jf_sPUijpF6Hb-Mhzxs0y26d4PAf8YpxuuY37DKyIz_q3bJZhhg-4FBiWaQKSxdsO8zNwZbZOQFl1YwkNaBVWoeVWglXb2sKavcHx38bA6Nc4ekZHwLpDT2bVm3eKQhJ1V4diGIvaaLYORfVp0aatLB8A_mRnxg69UHpbZtyIpTnCi06cUAPNQy0ukHIlDiZ31lm1BN2a8jxfIHUY4h_Q2cIzTT8ncfBx_Jr1C2OoB4kf3JPS6WJRTXMvB_LiqxEU3H5mKWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb550a215f.mp4?token=B5nWKWLXjyNdC6UwvPS7zzlgYzl4ztC7xnaTTKP6IANNkGycfu95ij7gJ_GfNZvDS_tHnX3wNPtcQ8Jf_sPUijpF6Hb-Mhzxs0y26d4PAf8YpxuuY37DKyIz_q3bJZhhg-4FBiWaQKSxdsO8zNwZbZOQFl1YwkNaBVWoeVWglXb2sKavcHx38bA6Nc4ekZHwLpDT2bVm3eKQhJ1V4diGIvaaLYORfVp0aatLB8A_mRnxg69UHpbZtyIpTnCi06cUAPNQy0ukHIlDiZ31lm1BN2a8jxfIHUY4h_Q2cIzTT8ncfBx_Jr1C2OoB4kf3JPS6WJRTXMvB_LiqxEU3H5mKWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:ما هرگز به مردم خودمون حمله نمی‌کنیم
ویدئویی از شلیک مداوم از روی کلانتری به سمت مردم ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/news_hut/72396" target="_blank">📅 10:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72395">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=kzXY39OqVCZDfpKe4lewnnGxTyytJlZ8TWdbUClP61GK4oqb9RxbwYaAXsvFT-ALoKQF2ICH7iGsEZEshj8FTCEKzrazFJ8AfxkgBfSQSXau4nuCfLb5P32v-zU9I_tGB9bXxr4x8ZNjifKiQyfxsmK6KCsnBMaIT8Inod6zuRUVz6Y3dPKurORkBN2uke5tlWt1VbDBUguVr_xYY4d5FUWKYypEe7R_-0hBoygMWjDjFfqA7i_qbtch4pF9Z5nO-AvWStww3jE8TY64JXm-XpWy3EXsFc02PFHMrNFtdDpyS4DdMFG1-4k_SzaOC_MF-3BBCIpotOnwXh9FFAnBwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=kzXY39OqVCZDfpKe4lewnnGxTyytJlZ8TWdbUClP61GK4oqb9RxbwYaAXsvFT-ALoKQF2ICH7iGsEZEshj8FTCEKzrazFJ8AfxkgBfSQSXau4nuCfLb5P32v-zU9I_tGB9bXxr4x8ZNjifKiQyfxsmK6KCsnBMaIT8Inod6zuRUVz6Y3dPKurORkBN2uke5tlWt1VbDBUguVr_xYY4d5FUWKYypEe7R_-0hBoygMWjDjFfqA7i_qbtch4pF9Z5nO-AvWStww3jE8TY64JXm-XpWy3EXsFc02PFHMrNFtdDpyS4DdMFG1-4k_SzaOC_MF-3BBCIpotOnwXh9FFAnBwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰۰ بیلبورد تو سطح نیویورک دارن خطر ایران هسته ای رو نشون میدن ، این میتونه آماده سازی افکار عمومی رو برای شروع یه جنگ بزرگ باشه
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/72395" target="_blank">📅 09:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72393">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=bMhOP8CRgZjwDcnmo4brcwQmspt75l0BdfMxUHhBYKzjx6xGl9x_j4wYUiPxO36_1sPbSTOlb-krp5SkxPF3AF0t5dVrOOaZuSBPIESY-okB_Q_4EE5My18ZYAjnXy63xR_Pu0zjmAYzpRtd8KKpqt9N5E18uHQ0APbvgml_xCTkLQ3bnGsSOYGEAVeWm3Eu56Lt4mw59fxYqrd5nZrFZkFZQByfhCW_4MXTVrWnLQGEl5rMNbukaSHAWXBshgfm4oI31rEE_SY3xu0Id9fWpS-mPTZ3OhZ1MSwmD7Y9UPhGbfzjVoluRTGOod6EsURczd5l7xIXuhdIziUAzHaBZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398d534a8b.mp4?token=bMhOP8CRgZjwDcnmo4brcwQmspt75l0BdfMxUHhBYKzjx6xGl9x_j4wYUiPxO36_1sPbSTOlb-krp5SkxPF3AF0t5dVrOOaZuSBPIESY-okB_Q_4EE5My18ZYAjnXy63xR_Pu0zjmAYzpRtd8KKpqt9N5E18uHQ0APbvgml_xCTkLQ3bnGsSOYGEAVeWm3Eu56Lt4mw59fxYqrd5nZrFZkFZQByfhCW_4MXTVrWnLQGEl5rMNbukaSHAWXBshgfm4oI31rEE_SY3xu0Id9fWpS-mPTZ3OhZ1MSwmD7Y9UPhGbfzjVoluRTGOod6EsURczd5l7xIXuhdIziUAzHaBZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ناو هواپیمابر «یو‌اس‌اس تئودور روزولت» (CVN-71) از کلاس نیمیتز، در چارچوب استقرار برنامه‌ریزی‌شده نیروی دریایی آمریکا در حال حرکت به سمت خاورمیانه است. این ناو پیش‌تر از سن‌دیگو خارج شده.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72393" target="_blank">📅 06:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72392">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72392" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72392" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72391">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvoDVS_ymwbUXQhXOa6wz8AqpINX_3LwzNHxf6I_fWbjaupNzKhAfdEQGjl5KlT4T3slFiTZrtGbzNzrAYKpZNRkRt5NS-jJu6sSmvEnnkefOtpwt6BDHumasP3pkvLHwHTQv-wSn5yLPXyURlnIc9WaCFwsBsDhNG3bzLJDjcu-moBGljm12ItcF-51fKp3ILG8aQg_z6GizCyn-1_Xgb8obBIpT4ZRUetaZhh7DJUzXTPpwFO-DNN4WpnckWxP1mpMLrsigW-_83ZhGOKusuev7fECiXcASQ9ON4uLGrqokVpb3r7bC5AJsS3IuUE2XBd3B3EPZO0c1z5QJ6RqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72391" target="_blank">📅 01:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72390">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b361018705.mp4?token=JN6M3OrCZrqj3Q15Kd5ULROuFe9qKtK5mewOitC5ODQDEvVMEvjJ89f--z_YEHAftTYUKHC-UgfhBnuzNambJpQwqhvH5CVjvj-WwQaz-AN0hiJz-CFwGetYcdSf1PxHBb-KlZoaQ1xoClH7PM__iq1VbkpqDGSSsYlp95X64fU-ywgwGC2b7UTkFsLjtTq1z1Y_SjanhOs-MenBnsjLb39YcEJyxihuJtoMr0qSGfo92Qz2L9HWN3gpkV4xdJGBwPDXoCyv7mQ4UmRMq8OHPEXPMgN2Ixjy6R9u0xFTMxvmW3rqUzKOFyv_Ty6F6qoWqXFSRbHaSrXcz46sbdai1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b361018705.mp4?token=JN6M3OrCZrqj3Q15Kd5ULROuFe9qKtK5mewOitC5ODQDEvVMEvjJ89f--z_YEHAftTYUKHC-UgfhBnuzNambJpQwqhvH5CVjvj-WwQaz-AN0hiJz-CFwGetYcdSf1PxHBb-KlZoaQ1xoClH7PM__iq1VbkpqDGSSsYlp95X64fU-ywgwGC2b7UTkFsLjtTq1z1Y_SjanhOs-MenBnsjLb39YcEJyxihuJtoMr0qSGfo92Qz2L9HWN3gpkV4xdJGBwPDXoCyv7mQ4UmRMq8OHPEXPMgN2Ixjy6R9u0xFTMxvmW3rqUzKOFyv_Ty6F6qoWqXFSRbHaSrXcz46sbdai1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاکس‌نیوز:
آیا انجام حملات پیش از انتخابات میان‌دوره‌ای همچنان برای شما مطرح است؟
ترامپ:
نمی‌خواهم چنین حرفی بزنم. یعنی، ممکن است [چنین اتفاقی بیفتد]، اما صرفاً نمی‌خواهم آن را به زبان بیاورم.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72390" target="_blank">📅 01:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72389">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13e157d195.mp4?token=O1e4wqXBGTzWqNYp4yOeSrFzw2J-ZnnoDtcktF7wbUhRjzd66CJSFnsO9-J0LEr0Gw2HT5kmybCETy9GlPMtVbaTqMzwzE8RqwwVWGiuOTfGHN7EIMsUYKkORk9UTUzX7fp9hZdHf77W4XfKZmVE1L_jKKV-Mpx06mtrCNYLew-9RQ8cZOEleofF16eaYv9cJMqyAv8aHQvfcmPrPwKBRY9uDgZOlx5IazokW5kQbDyFLLMA3mCHAEuZ84SciovUFbDJk-BSTJOMlaN4a7Dn6mCOFG91OGq0BTuOts2Zk4RAUo2y8nB8fVcOo6pBLXeQVi01UT3rqp5dT87kWw1cKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13e157d195.mp4?token=O1e4wqXBGTzWqNYp4yOeSrFzw2J-ZnnoDtcktF7wbUhRjzd66CJSFnsO9-J0LEr0Gw2HT5kmybCETy9GlPMtVbaTqMzwzE8RqwwVWGiuOTfGHN7EIMsUYKkORk9UTUzX7fp9hZdHf77W4XfKZmVE1L_jKKV-Mpx06mtrCNYLew-9RQ8cZOEleofF16eaYv9cJMqyAv8aHQvfcmPrPwKBRY9uDgZOlx5IazokW5kQbDyFLLMA3mCHAEuZ84SciovUFbDJk-BSTJOMlaN4a7Dn6mCOFG91OGq0BTuOts2Zk4RAUo2y8nB8fVcOo6pBLXeQVi01UT3rqp5dT87kWw1cKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا فکر می‌کنید ما در این جنگ [با ایران]، از طریق جنگ اقتصادی که وزارت خزانه‌داری به راه انداخته یا با حملات نظامی پیروز خواهیم شد؟
ترامپ:
فکر می‌کنم هر دو. به نظرم از هر دو طریق پیروز می‌شویم. از منظر نظامی که عملاً پیروز شده‌ایم، اما این بدان معنا نیست که آن اقدامات را متوقف کرده‌ایم.
ولی قطعاً داریم با اقتدار کامل در آن پیروز می‌شویم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72389" target="_blank">📅 01:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72388">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3da141396.mp4?token=H6VRxjGIJ2xbXvBBnwygB38GVsKAdVFRq7yD-v64K49irYC5M5OT-v1IeHD19gD_5BIsYwom5kpjt-RjbbxkUTlzYD6RcBMcz6hyfuV0ArFBzmZ2R5XS8mW2lNVO5VWZ_UG9B3KFZScDnUBuHlsBoSEWIc8GDF-vAuRjtS2LuigDIKHO3f8mBkFMDIDIEeaqhWw32MzBlOK8X5gzipr8S1PBfNzDoFsrP6ShKGHWU8_Vw3BdjXvchKI5MafFRRyktPnnXJu5ZqZXrCB3gEkE4xNBBlcyeKbIZjMAiwkEp8QjL3DSunJK_mSFBTPTvE0D3PCjBOOMPEwpjkS1ziM2Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3da141396.mp4?token=H6VRxjGIJ2xbXvBBnwygB38GVsKAdVFRq7yD-v64K49irYC5M5OT-v1IeHD19gD_5BIsYwom5kpjt-RjbbxkUTlzYD6RcBMcz6hyfuV0ArFBzmZ2R5XS8mW2lNVO5VWZ_UG9B3KFZScDnUBuHlsBoSEWIc8GDF-vAuRjtS2LuigDIKHO3f8mBkFMDIDIEeaqhWw32MzBlOK8X5gzipr8S1PBfNzDoFsrP6ShKGHWU8_Vw3BdjXvchKI5MafFRRyktPnnXJu5ZqZXrCB3gEkE4xNBBlcyeKbIZjMAiwkEp8QjL3DSunJK_mSFBTPTvE0D3PCjBOOMPEwpjkS1ziM2Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
به گمانم آنچه رخ خواهد داد این است که ما خیلی زود در این جنگ پیروز خواهیم شد؛ و به محض پیروزی، قیمت نفت کاهش می‌یابد و به شدت افت می‌کند تا به سطحی برسد که پیش از جنگ بود.
و نکته کلیدی این است که ایران به سلاح هسته‌ای دست نخواهد یافت. این کلیدِ ماجراست.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72388" target="_blank">📅 01:16 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72387">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91575662ab.mp4?token=ZkLRaFCq7AkRb6BA0Grm3wCTS2RwrCtBsv_F6D4ktn4ua22MtDWyxBBAhzXvt5gZvL1wJZg5Vpr1bcZqCIjhrVVgGc1mb1vnN9FQRIFk51UHUUEFBdVl34UBR1hNW0gFCFeAYx3ArOo0VFe0JBdgklEW61R0LOqdDvFcx8XJRtsomURsoWAow05IbscbYbehbymYdMpu8zHi53gLdrlpH3d0g6rLJxy9Mu9yFZKmSIVpsu1rCzfWFJWZOKC2z1yrvGvY0_S2RuhPEm1Zi68Xz5cFVkQ05HQ-FCTVoNWoQz8gpUwTYUzzN-3Fse8k4wgszrmWXfL8Wbg5VZy7zHQc1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91575662ab.mp4?token=ZkLRaFCq7AkRb6BA0Grm3wCTS2RwrCtBsv_F6D4ktn4ua22MtDWyxBBAhzXvt5gZvL1wJZg5Vpr1bcZqCIjhrVVgGc1mb1vnN9FQRIFk51UHUUEFBdVl34UBR1hNW0gFCFeAYx3ArOo0VFe0JBdgklEW61R0LOqdDvFcx8XJRtsomURsoWAow05IbscbYbehbymYdMpu8zHi53gLdrlpH3d0g6rLJxy9Mu9yFZKmSIVpsu1rCzfWFJWZOKC2z1yrvGvY0_S2RuhPEm1Zi68Xz5cFVkQ05HQ-FCTVoNWoQz8gpUwTYUzzN-3Fse8k4wgszrmWXfL8Wbg5VZy7zHQc1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو سالگرد ترور نصرالله رو با انتشار چنین کلیپی به مردم اسرائیل تبریک‌گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72387" target="_blank">📅 23:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72386">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5vwxGCO5IEkDKUoYsr0Kft8BxfiG17Ken07extL-XDLISRNweeqOsDy35Vnk-AmcHvhWx_sbN7Kk5JMNfe7oY3lhD2yxt0KEbOvVtiPjGCHtLov2qT3SIQq-PHlEloFF2VXFFqlQN31KBhCCSACY7z1SfM-i59w3W3VtetMnDw7be61NB4CGc_FG2E6gxlJ1J0v_tbx5H56ivYZOaXb5y7nX7RwNR-FGdv1G3gpymCq321Y6b5L6CjrLeL2-FoIPWDkwICmxz_bPZDWS5-8fctaYR9e7eTGu-Ht4veT8skAYSTXk2Qh2Mn9-pc7YrDLAdW2BcxogFxCcM7o4TXK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛به گزارش شبکه ۱۲ اسرائیل، بنیامین نتانیاهو، نخست‌وزیر اسرائیل، امروز سفری محرمانه به ابوظبی داشت و با محمد بن زاید، رئیس امارات متحده عربی، دیدار کرد.
نتانیاهو صبح امروز با یک جت اختصاصی سفر کرد و بخش عمده‌ای از روز را در امارات گذراند.
محور اصلی این دیدار، ایران بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72386" target="_blank">📅 23:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72385">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PQ2_zBPEl1L5bTKBrprpdwyVQlP-uoNG24GX9gIlFLnikYZvHYzDd1no3ypnoAwgrT33dvKLeiiNfpY88HMCsOlCHHsA83cIQAPCq0m8JoydawC0YduZ0OLqXrv2lqt7WGua7o9SCGmetA-sRVqCtAvAw6n-DMLWMvgmI0Fc34VrVgXGEyh3ogBQSik-wnhZneHNzQg05D8pszk9UdEsnP2Xc9F_IU9cSqOdqohtfSYLzb3hPSsMzUx4eNz6kBLL2BGjyBCDlm8bUwapdniH6zAUWGEV6FvTIKBAXKcTOUE-VixAXLzmnRLvvkEvYbzVjiHhx1_soRjuvSebiIJAnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حق‌ترین و مفهومی‌ترین عکسی که میتونین ببینین:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72385" target="_blank">📅 23:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72384">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الکساندر ووچیچ، رئیس‌جمهور صربستان، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72384" target="_blank">📅 22:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72383">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شلیک چندین موشک ضد کشتی به سمت شناورها در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72383" target="_blank">📅 21:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72382">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=kjyfDPWNwyVvut7NH1fQo6pRx_ptjtwLMyzBnIw6Ps9hJAlkNGTzvTVIGFNc5owF8Bk1nBCmOAjuhEnvUBaBNoL5p4mTkW4LUWS2VXL9iCq0aMBjj11z_tFP9Zkeem2SXouQD7wcn5MbcGe5P5Gf3HCrz9QNoR-QQVCPHntb_Jm4RAfJuroi28_uvzZ0g76Sz0CyfiS1AQzGxB9QE_yWwp1HW7lysywrknTqW4fMhbG7WzWgSmjV5F7GwH4KABgwTJ8CBpKm6P3EhcjKoCIJ9eIq0MMzYXAeFxUh_3lwPt4iMipkMXrHCxuGBaX30x2fW6BwFCpLckdwxko96vNq9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/824029a6f9.mp4?token=kjyfDPWNwyVvut7NH1fQo6pRx_ptjtwLMyzBnIw6Ps9hJAlkNGTzvTVIGFNc5owF8Bk1nBCmOAjuhEnvUBaBNoL5p4mTkW4LUWS2VXL9iCq0aMBjj11z_tFP9Zkeem2SXouQD7wcn5MbcGe5P5Gf3HCrz9QNoR-QQVCPHntb_Jm4RAfJuroi28_uvzZ0g76Sz0CyfiS1AQzGxB9QE_yWwp1HW7lysywrknTqW4fMhbG7WzWgSmjV5F7GwH4KABgwTJ8CBpKm6P3EhcjKoCIJ9eIq0MMzYXAeFxUh_3lwPt4iMipkMXrHCxuGBaX30x2fW6BwFCpLckdwxko96vNq9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم یه حماسه‌سازی دیگه از مسعود :
🎙
مجری شبکه فاکس نیوز:
آیا شما اورانیوم غنی سازی شده 60 درصد رو تحویل میدین؟
مسعود پزشکیان: بلهههه
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72382" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72381">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=pn5a_IUhlvR_cCCxDszJh8KwyzLzBmTW59RD_QxMrurWEVrsYgWFhWmcazwpYEAZqYBoh7DU85aDNrY9vw-veC_7SndYc5xJ7_IpFRdmJKc4tm9nK_2h7bLADKYaQEvaq85nSy6iyvx7LK_WD9wg9apkxLYL-_sHUwuBpz331eHFkK4Rf1FfrqqpQh-9O7GeJNArMBKg4caqGGCn-I5rGx5nL_TZMsmh3hXkji3GS6aL_q7U3R-636A11DVaEmjNZyhtY5HWSCWshzth6u_VeiiX7ivjjTLTlLXtH40zioXDGrGA0Sqxwers2Z1CLhgGsqg2Wbc5qCc1du7TEpZDtX2uJi8FPjvUHGvmqRqOChsFYS_sRcJL55OtaMSehWEs1kCsDsXPay9pGmj6nTGhFejF0zaETAR6TXbJQOyaHzcRouqMn_4y2NHe2k5ugFTGA8kqVDPKGseh2vwaRLOM939D4fhBvsgjttXT7PXyLRgjDIiQd-NFbwVSALxw3OOxUUchgNjQqzWQiYj9cBGm67nz0S8mzWheLjFbfUQIN_AI_RSHlgVzTrZ1zBWhixXjKIJObd_Kl6bhqqiuhYNnrGq6__KxNq0VNltQ48hduveKXZQd1jr5O84AbXUc-6HWW0pn7MWV6xeFAsKWRUDGqram8SvvwoZkm_7ZfTwxCJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ab5c624e.mp4?token=pn5a_IUhlvR_cCCxDszJh8KwyzLzBmTW59RD_QxMrurWEVrsYgWFhWmcazwpYEAZqYBoh7DU85aDNrY9vw-veC_7SndYc5xJ7_IpFRdmJKc4tm9nK_2h7bLADKYaQEvaq85nSy6iyvx7LK_WD9wg9apkxLYL-_sHUwuBpz331eHFkK4Rf1FfrqqpQh-9O7GeJNArMBKg4caqGGCn-I5rGx5nL_TZMsmh3hXkji3GS6aL_q7U3R-636A11DVaEmjNZyhtY5HWSCWshzth6u_VeiiX7ivjjTLTlLXtH40zioXDGrGA0Sqxwers2Z1CLhgGsqg2Wbc5qCc1du7TEpZDtX2uJi8FPjvUHGvmqRqOChsFYS_sRcJL55OtaMSehWEs1kCsDsXPay9pGmj6nTGhFejF0zaETAR6TXbJQOyaHzcRouqMn_4y2NHe2k5ugFTGA8kqVDPKGseh2vwaRLOM939D4fhBvsgjttXT7PXyLRgjDIiQd-NFbwVSALxw3OOxUUchgNjQqzWQiYj9cBGm67nz0S8mzWheLjFbfUQIN_AI_RSHlgVzTrZ1zBWhixXjKIJObd_Kl6bhqqiuhYNnrGq6__KxNq0VNltQ48hduveKXZQd1jr5O84AbXUc-6HWW0pn7MWV6xeFAsKWRUDGqram8SvvwoZkm_7ZfTwxCJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری:
رئیس‌جمهورایران این هفته اظهار داشت که ایران هرگز به دنبال سلاح هسته‌ای نبوده است؛ با این حال، ایران اورانیوم را تا سطح ۶۰ درصد غنی‌سازی کرده که این میزان ۲۰ برابرِ درصدِ غنی‌سازیِ مورد نیاز برای تولید برق است. چرا ایران به ذخیره‌ای ازاورانیوم با غنای ۶۰ درصد نیاز دارد؟
عباس عراقچی:
اولاً، غنی‌سازی تا سطح ۶۰ درصد غیرقانونی نیست و همچنان در چارچوب معاهده منع گسترش سلاح‌های هسته‌ای (NPT) و برنامه صلح‌آمیز ما قرار دارد؛ ما این کار را برای اهداف مشخصی، از جمله مصارف پزشکی و دیگر مقاصد، انجام داده‌ایم. با این حال، ما پیشنهادی برای تعیین تکلیف مواد غنی‌شده تا سطح ۶۰ درصد در سال‌های ۲۰۲۵ و ۲۰۲۶ ارائه کرده‌ایم؛ موضوعی که اگر آن‌ها حسن نیت و عزم واقعی خود را برای صلح ثابت کنند، قابل بررسی است. پیشنهاد ما این است که مسائل پیچیده‌تر به مراحل بعدی موکول شوند و در این مرحله بر اعتمادسازی تمرکز کنیم. به همین دلیل، ما این طرح هفت‌روزه را بر اساس تفاهمی‌که در گذشته با صاحب‌نظران آمریکایی داشتیم، ارائه کردیم. نخستین گام این است که دارایی‌های ما که به‌طور غیرقانونی مسدود شده‌اند، آزاد شوند؛
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72381" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72380">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">صدای انفجاری از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72380" target="_blank">📅 20:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72379">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNn2yzzAiDfomiPbfcWs0SgNp6ixI03tyivYi6W5tTyKYMTB7z2ThR2XyznUQsyt7V-kLV7AQxhbK-gFwZOB_A9eMRAMkUClu45Zx6RVxCquIyuavOGM5myv4ohA_Ayts4-nhCry-mAwJi_YALSQXCWgEALdWlDMfcEEnRi922hb2Y8S16eqs3IvEOJy8apqJH7SWc_ykPKKaXeRGJSeswa5UKrl2pOy3Vd30DOT-OCsRqxP0sh2fbmtBJJbN0gDik3chyLAM78eIOF7TazR9VQn_ZEcCz7sugZYiYi95slIJHpbBN1EHOoYK7ZL29IcZiyBlVSktpnlcwgxztoLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای آوش به نقل از اداره حقوقی مجلس: حمید رسایی به ده ماه زندان محکوم شد
آوش:
این پرونده که دوبخش دارد مربوط به سال ۱۴۰۲ و زمانی است که حمید رسایی هنوز نماینده مجلس نبود.
حمید رسایی که از حکم شعبه دوم دادگاه ویژه روحانیت تهران، برای عذرخواهی نسبت به انتشار مطالب خلاف واقع درباره مجلس شورای اسلامی امتناع کرده، با حکم قاضی برای تحمل ۱۰ ماه حبس تعزیری به اجرای احکام احضار شده است.
بخش اول پرونده مربوط به انتشار مطلبی با تیتر «دستکاری قالیباف در اسناد مجلس» در صفحه اول نشریه «۹ دی» است، و بخش دوم مربوط به انتشار کلیپی تصویری در کانال تلگرامی متهم که رسایی در آن از تعبیر «دیکتاتور پارلمانی» برای باقر قالیباف می‌کند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72379" target="_blank">📅 20:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72375">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCH96pkv5gUHVrk4raXFuhoIdryT4mf3q8lWnQ4A_Pwc6Sd-b1meO7Xc3ph7j7R-X54FFdKvfQ9hVMxQA4w6tcvB8riDEAWNweSXPgPX7RSIC1elBSj3X79J8ZSIGqryFBXuAZxvzdmKk4TwzWbUjDAwxHh-fTrtQYZmh6es4ikqBp8WnXtZhl2xFD2KR-pXnKH8OGVgYMtGHIUeNlU8yBEuAGY7tiUrbp9w8GHioeHvqRv6gXiruiVxHW1KsERrpfSJl3UqrnU6XF8iF7muKy__gkD2CSKugDy6Cq1Exzi4A7Ficn0f6ObpncaJAYZQ5G_TREaw0RJiZXMqPRl6hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mea0ZbmkMGu3UdjYZivSvAIXzcDc_4laDdytlKi4pZ-rRbd4QDyU-Sy9KsievyHNY6eGpDRUaWGIv7DUmgNBnlZ47KLocm3ZTFMHbBC7YV_8kXKUQSSUu2dORngWBMlVuZXUnsAKgqiOUgMS8odXxr9ck1YZVfx8b23We1xoH4k5aTLVRJWJRdpUvcc8ohUwFDsI9jAEyOkpfLza9AyiOdUk6be5iUi-URI_LKKDzsVJ6U79ODLLl16d11rIQ4W0pDNoCswn86Roy-Z81CJLHOwPDZo7qRMYL_1bbM2dsWwgz7NTP6lJ2SML8bUfgDpWSV1UZl8nUV25bep7NkBQ5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=isY47yglFXCzkbmzT3QrI2vZRNDynMMcpvR_Y4a2itGd9hOnA8D7FIa73MHvTHCpHBEg85B89nftDhgydu-vW-zHrKssN5T4V1eQyRuicDI6Ewy4AfpKPRjDZNTX1tEjdfviazdN26vEOuN4uaYWzCJiLI5yR5UObpfctCPZhZt5x5w_6-2vGmFpz8YdgkERGNV0HTh2F3Pg4C_HhbanzZmdWBq4AdRPLGQikb6z577RVvxFdpHGfODDtZZYytF0LGMgiynZijfG-khfp7WREJ4HEq-kEH7BVxjHZvBXT2E_Tem9--UBB3nuih9-Gkqwz1IdpCgohnvGQ46nqHGe_1dI1oNuHHaQdx9IyBQAz6gA6LXrMfFKBATQvXi8ycqUacQuS-LoVnDPKf4x_7GFazziG5pmLj3VQvl_OWukNNnBWwQAhwlgYvuiSCLgz4riOCV7e0dD25eK6BBKWsrJptfE0Wx8LWj5S360XiCStAqAub5T6fAH3hViidnRJYZBWIZM3XWIWfVvAJo_g4YeMNuKUYflRS934lHnRAozad6MXBVda3wkhlOu0kTPaMq6fJ-jji0K4Y7IXWzCvITavIeCbpcrtV0WcuoI1XLQNHhATgJS58afO2VwepinwXmkQsv8W_TIvYdLXk-VMkv0ONEuX4FE4a8RTP4OygGHJp8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78db64d5d.mp4?token=isY47yglFXCzkbmzT3QrI2vZRNDynMMcpvR_Y4a2itGd9hOnA8D7FIa73MHvTHCpHBEg85B89nftDhgydu-vW-zHrKssN5T4V1eQyRuicDI6Ewy4AfpKPRjDZNTX1tEjdfviazdN26vEOuN4uaYWzCJiLI5yR5UObpfctCPZhZt5x5w_6-2vGmFpz8YdgkERGNV0HTh2F3Pg4C_HhbanzZmdWBq4AdRPLGQikb6z577RVvxFdpHGfODDtZZYytF0LGMgiynZijfG-khfp7WREJ4HEq-kEH7BVxjHZvBXT2E_Tem9--UBB3nuih9-Gkqwz1IdpCgohnvGQ46nqHGe_1dI1oNuHHaQdx9IyBQAz6gA6LXrMfFKBATQvXi8ycqUacQuS-LoVnDPKf4x_7GFazziG5pmLj3VQvl_OWukNNnBWwQAhwlgYvuiSCLgz4riOCV7e0dD25eK6BBKWsrJptfE0Wx8LWj5S360XiCStAqAub5T6fAH3hViidnRJYZBWIZM3XWIWfVvAJo_g4YeMNuKUYflRS934lHnRAozad6MXBVda3wkhlOu0kTPaMq6fJ-jji0K4Y7IXWzCvITavIeCbpcrtV0WcuoI1XLQNHhATgJS58afO2VwepinwXmkQsv8W_TIvYdLXk-VMkv0ONEuX4FE4a8RTP4OygGHJp8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ساعات اولیه ۲۷ سپتامبر ۲۰۲۶، ساکنان از سه وسیله نقلیه مشکوک که به سمت پایگاه نیروی هوایی سلطنتی فیرفورد در حرکت بودند، خبر دادند.
یک توطئه تروریستی برای انفجار پایگاه نیروی هوایی سلطنتی فیرفورد وجود داشت.
پنج مرد در منطقه ویلفورد به ظن ارتکاب جرائم تحت قانون مواد منفجره دستگیر شدند.
پایگاه نیروی هوایی سلطنتی توسط بمب‌افکن‌های آمریکایی برای حمله به ایران استفاده می‌شود.
پلیس مبارزه با تروریسم در حال بررسی این موضوع است که آیا ایران پشت یک توطئه بمب‌گذاری مشکوک با هدف قرار دادن یک پایگاه نیروی هوایی سلطنتی مورد استفاده نیروهای آمریکایی بوده است یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72375" target="_blank">📅 19:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72374">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nJtRUhN97xp6PgPrmz8aQygo_fknetrlybq9DoUTo8rGBMgz3BrrtC80pKsgJwVOsBSsotydhOGfog3itMmUXpSlvG1x4wMj-3qCDxs7A5-d-WpI_T_MR3bAMfy6mnTQ4c39GrmYIrx3MDEjgKhEOrLbJI7uBd8oy5qIaWMMK1TT4oKkg3W4fx5ikFm1N0LveKJ6v68GZgbwzA8gK020XaZegj4WgXew_82oDx_mRrYQVkQMGR7bcXB7MxTIbjxjnTvdqo1OLN6TtdWaPgMkmC0RlRR0-mSavxLi5VkLQoHDnxN0YGVjTVfJ_ARlkAgGh1kiusD093kL_yIpr8xRUic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9233dc65e9.mp4?token=klBtLA96IeZKfDT0krf7otmswMZktCaUgZlHlS9yKi31DZeyIUs7gMPQI7NFSbTaOD7FOQ8wmAATp9APpc69XmN3nVq_0qbt1X9fqp8PofzFzikNSMTvI5SS2J3NOoxRdrqZGWlym4Nc5iEegUJfqnJJWUQo4xXUgjApVq5vy27iV6iKqwVMWPiNoycWhCfhhw2ydMWInnqrElWV3_1qgfbJMiIldBzkdbZ6TvPnqlN5qs1Fugp-JLhfSMLaavBkCMM7CdDoAp1tjJu6Zzba_oHSjxpAiHrxZ5UVaNqIUNGgspon1ILw4pyxjQLUoadSXksy_8rJ35F_R8x8noy0nJtRUhN97xp6PgPrmz8aQygo_fknetrlybq9DoUTo8rGBMgz3BrrtC80pKsgJwVOsBSsotydhOGfog3itMmUXpSlvG1x4wMj-3qCDxs7A5-d-WpI_T_MR3bAMfy6mnTQ4c39GrmYIrx3MDEjgKhEOrLbJI7uBd8oy5qIaWMMK1TT4oKkg3W4fx5ikFm1N0LveKJ6v68GZgbwzA8gK020XaZegj4WgXew_82oDx_mRrYQVkQMGR7bcXB7MxTIbjxjnTvdqo1OLN6TtdWaPgMkmC0RlRR0-mSavxLi5VkLQoHDnxN0YGVjTVfJ_ARlkAgGh1kiusD093kL_yIpr8xRUic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
ایرانی‌ها می‌گویند که تنگه‌ها را ظرف ۷ روز باز خواهند کرد؛ [در حالی که] تنگه‌ها باز هستند.
ما اکنون به‌طور میانگین روزانه ۱۵ تا ۲۲ میلیون بشکه [نفت] صادر می‌کنیم.
نتیجه این است: ایالات متحده بیش از ۱ میلیارد بشکه صادر کرده، و ایران صفر.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72374" target="_blank">📅 19:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72373">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15b7065503.mp4?token=e67toM9JHn0tfsA7-fo57OaMi1o1q3-6puayBTBiPEH1u2klbcBcSHSKuQm6TkieCX1ffZGMnzhxm9TiBsuhg7x_71JchXmAEzbW_E67TWWSHp0LGPD4-E9AzWH8sqxfTbzt7pAMkUV4CGJYxbgo8uzGjsszS0VtohbSZe6hZoaAqKibdl_1EjUbeedGxYHDa7XuKaF6iX3F8K3iBdZcEikvvUiX2P0tTOXXC9KsyG8Lc5p9lAPHu02gOTCpTactphuUtbqFH1jbdvlI_RZZMnovzVUuDkIonVb40SjtX-DDBdM7FKJX5aA6dxsvNbzTOZVYW2BROpK31PMIML7RlIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15b7065503.mp4?token=e67toM9JHn0tfsA7-fo57OaMi1o1q3-6puayBTBiPEH1u2klbcBcSHSKuQm6TkieCX1ffZGMnzhxm9TiBsuhg7x_71JchXmAEzbW_E67TWWSHp0LGPD4-E9AzWH8sqxfTbzt7pAMkUV4CGJYxbgo8uzGjsszS0VtohbSZe6hZoaAqKibdl_1EjUbeedGxYHDa7XuKaF6iX3F8K3iBdZcEikvvUiX2P0tTOXXC9KsyG8Lc5p9lAPHu02gOTCpTactphuUtbqFH1jbdvlI_RZZMnovzVUuDkIonVb40SjtX-DDBdM7FKJX5aA6dxsvNbzTOZVYW2BROpK31PMIML7RlIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت درباره ایران:
تنها ۱۵ میلیون بشکه دیگر از نفت ایران روی آب باقی مانده است. ایران دیگر چیزی برای معاوضه یا دادوستد نخواهد داشت.
احتمالاً ظرف دو هفته آینده، آن‌ها آخرین محموله‌های نفت خود را به چین تحویل خواهند داد و پس از آن، دیگر چیزی در اختیار نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72373" target="_blank">📅 18:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72372">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdQUYeDRwbjlA3vNLd-7aTe-fuhMyMufVFjUYSjy5BOZyZxwJK9H9FITD2ntWjLHVTkG69X3l22o421uhF8mheDoKnbn3GIlTw_2fAu6SlUBquQCXFtWaiGDvg7OtWYENbHhz2WHvYf0hwLUVh9OYRdoXdt7zJfeSDFc6i1Umj580hb7IMbE5RMO_TufnOHkEPQW9qTJ1kCqUqIp-3YBvgiaUQK7rhfHu_RdG_SChHxsjvkq_s1xUOMFHIaSfdKa8loaYPQ32FogUC2o-J_hfjSKFT6wmj9TRTn4BZ4gLuCAtmgjWdD-KOqfyj1sZCFPefFOvPxUJKY7LoOr8GKv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به «اکسیوس» گفت که با وجود رد پیشنهاد ایران، انتظار دارد در هفته جاری مذاکرات بیشتری میان آمریکا و ایران انجام شود:
آن‌ها خواهان توافق هستند، اما این آن توافقی نیست که من می‌خواهم. آن‌ها در بازی خود زیاده‌روی کردند.
ترامپ در پاسخ به پرسشی درباره ازسرگیری حملات:
همواره به آن فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72372" target="_blank">📅 18:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72371">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=orkKIKlZ-ZbHLatIhLYFP_sTCTGUHcCm2V6vDpyY9ALb_UkdJaDXdnUiRuxE2rkHYOxxtYzuma_1Y4qEzC71XFt1CEKllIGCLQmiY05x5QPA_WG3XCLB2rzCNRE8eMmaD06TXtwqp_5SS8dEzaxuwsxRil9-z9HsWEcyWb60iJi_XroGOveyG4EpD9kw2XaiqNfJzUmGK6G-jAycgxFaYkD3-wJXAJczpp3v_azJytNyN2e6YOxptURwvvXJRCba-9of6-vOk-5BKBiJDwNNgtA0yAuIJBbz3P37s8P-oLdg2G1Tyg1C_HAVOOnNeqj8T_cYHeM7E4o27B2DY4-MBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd27ff889b.mp4?token=orkKIKlZ-ZbHLatIhLYFP_sTCTGUHcCm2V6vDpyY9ALb_UkdJaDXdnUiRuxE2rkHYOxxtYzuma_1Y4qEzC71XFt1CEKllIGCLQmiY05x5QPA_WG3XCLB2rzCNRE8eMmaD06TXtwqp_5SS8dEzaxuwsxRil9-z9HsWEcyWb60iJi_XroGOveyG4EpD9kw2XaiqNfJzUmGK6G-jAycgxFaYkD3-wJXAJczpp3v_azJytNyN2e6YOxptURwvvXJRCba-9of6-vOk-5BKBiJDwNNgtA0yAuIJBbz3P37s8P-oLdg2G1Tyg1C_HAVOOnNeqj8T_cYHeM7E4o27B2DY4-MBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی:
ما همان‌قدر که برای مذاکره آمادگی داریم، برای رویارویی با هر چالشی نیز آماده‌ایم.
ما در برابر هرگونه تجاوزی علیه خود قاطعانه می‌ایستیم، حتی اگر کار به جنگی آخرالزمانی بکشد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72371" target="_blank">📅 18:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72370">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حملات اخیر پهپادهای جت‌سوز روسی «گران-۴/۵» (Geran-4/5)، یازده مرکز داده اوکراین را هدف قرار داده است که شامل ۱۰ مرکز در کی‌یف و یک مرکز در دنیپرو می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72370" target="_blank">📅 18:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72369">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=hWB0oxnaLJtEAvxN2RNrQoEjB9_Cl6iDDHdRBefYym-my29kyvhA30AOrvmUf7uZDF51FGXNDgh3NwjtMZnrv-HW-tu9KbCGMpS-qaOpLqhT6D3A7oeCd8F8Ecppm9LcyXv52KMUy7KxupVA3a6VzSTXSDJMLE0ADugN73BxgkaWAFL3faU2MOZxZwBEfZ2ynnAyjsBA9z5T5aCPpEme5EuTLOjZ-3wf8YLMZfv7t7ADrYdk9QE7BClQLDFWQhe24lZBircBBeZKKS65PujuldPqEg5HwIIInQJnmniezyG4kfFjmFfqM7uEzMQftSi9Q2EU8O_b7CmHTWynQ-jZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c66f5a0a1.mp4?token=hWB0oxnaLJtEAvxN2RNrQoEjB9_Cl6iDDHdRBefYym-my29kyvhA30AOrvmUf7uZDF51FGXNDgh3NwjtMZnrv-HW-tu9KbCGMpS-qaOpLqhT6D3A7oeCd8F8Ecppm9LcyXv52KMUy7KxupVA3a6VzSTXSDJMLE0ADugN73BxgkaWAFL3faU2MOZxZwBEfZ2ynnAyjsBA9z5T5aCPpEme5EuTLOjZ-3wf8YLMZfv7t7ADrYdk9QE7BClQLDFWQhe24lZBircBBeZKKS65PujuldPqEg5HwIIInQJnmniezyG4kfFjmFfqM7uEzMQftSi9Q2EU8O_b7CmHTWynQ-jZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جعفرقائم پناه؛ معاون اجرایی پزشکیان:
به عربستانی‌ها گفتم انشاءالله برد موشک‌های ما به آمریکا برسد تا دیگه به پایگاه‌ آمریکا تو کشور شما حمله نکنیم بلکه مستقیماً به خود کاخ سفید موشک بزنیم
😐
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72369" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72368">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72368" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72367">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GVjAcqBwtiXeHDX2NlIyVeuNusGXjfKFLiM26pgacvxpBVAYF1-Z6cJTMYySS8dM1M4QYIf7bXonMDNc8NBUXGO0XuepzeTiwU6RIM1LW7PVhOruhF-xdu0jZ7-YM8FTWgOGJNyebiXqO9U9sdFJ643xsMaM2KrkwZfL1VGSVe6OLdlj3d_ramjxBUBob5xvuqtYeKkpCZEh8xel8oEhUaeYX2zYLVmeqWLpnyeopqKh702WkYi_eLXJY9lDP0zLUF_tbpOF2qCe5IBvYwUwQWcpk9_SYhjnP2C4dzHEa4VE0eoQVydMV1hicApZ9gwE04iAAmRDuPVADSf1OQYOIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72367" target="_blank">📅 18:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72366">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=ZIozHMWGy3_YNbQoX95KRtzvnwxhdBPe3zPP8pjMlJFunY5g-vhJkjkQJfj0uzK0zp_P3GedjfVPalKc7X7gXWi122n5uckn2yWznS-0SAsvAAuzI9coaDZEA6FqyF-5-2FCJmJRaIOW8x87g6wVx_XPDzLapSSdq00aSbZ_9Rjb0pUMphGWyDTjzUYaZZQW4KVgvIwNC_PoPMJTxBkWRqUxzUXooaI_NhiBn2N1m_Nh8-rRms1B-4gLrJMu6kSmuZijUKkGc7CndfbqzcmK0setoHHHGmVEKHIuB_gFGbsNmnOV9Q80Ou5sR4p9hw2CLQuXTUMd1kLYt8hD5Y6qOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=ZIozHMWGy3_YNbQoX95KRtzvnwxhdBPe3zPP8pjMlJFunY5g-vhJkjkQJfj0uzK0zp_P3GedjfVPalKc7X7gXWi122n5uckn2yWznS-0SAsvAAuzI9coaDZEA6FqyF-5-2FCJmJRaIOW8x87g6wVx_XPDzLapSSdq00aSbZ_9Rjb0pUMphGWyDTjzUYaZZQW4KVgvIwNC_PoPMJTxBkWRqUxzUXooaI_NhiBn2N1m_Nh8-rRms1B-4gLrJMu6kSmuZijUKkGc7CndfbqzcmK0setoHHHGmVEKHIuB_gFGbsNmnOV9Q80Ou5sR4p9hw2CLQuXTUMd1kLYt8hD5Y6qOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره ایران:
به‌محض اینکه ایران تسلیم شود و جنگ پایان یابد — که به‌زودی هم چنین خواهد شد — قیمت نفت به‌شدت کاهش خواهد یافت.
قیمت نفت سقوط خواهد کرد و قیمت همه کالاها پایین می‌آید؛ البته قیمت مواد غذایی هم نسبت به دوران بایدن بسیار کاهش یافته است. تقریباً قیمت همه چیز پایین آمده است.
قیمت نفت اکنون نسبت به دوران دولت بایدن کمتر است.
ما مقادیر عظیمی نفت استخراج و عرضه می‌کنیم؛ دیشب رکورد جدیدی در انتقال نفت از تنگه هرمز ثبت کردیم؛ مقداری بیش از آنچه پیش از آغاز جنگ از آنجا عبور می‌دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72366" target="_blank">📅 17:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72365">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ccd821b0.mp4?token=RHs9BSnNrU94p-_jBOhSx50lZHz2oWWOUVZ4cWtfDdbkMaWAiR9CahSAOhNafAqw4iCW_r0RGnLLTxEzf_s6SWEurlj3c3vWfWawvl329eW1LBC5JZOHXztjPUlFZ2xygSwaW9Unay_Sz23VKouwCXetU3x894L_Mo2O2OmnEYQsz4iS79Br6dEq3jFlyuqJvhp3QGpJeeO8w_OAZMc4r63jfJ-v_-MLJnXWrX_GhOL4PULmSz3ejmvh9o0HqVC7tXciXGujIhujvxgyKAxUeMQRlliF-G6eBAps6bMntbB7FIo6xRFVme7cSaV9J1Ip-GrgAlPpwNzFKH2dSA5Jsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ccd821b0.mp4?token=RHs9BSnNrU94p-_jBOhSx50lZHz2oWWOUVZ4cWtfDdbkMaWAiR9CahSAOhNafAqw4iCW_r0RGnLLTxEzf_s6SWEurlj3c3vWfWawvl329eW1LBC5JZOHXztjPUlFZ2xygSwaW9Unay_Sz23VKouwCXetU3x894L_Mo2O2OmnEYQsz4iS79Br6dEq3jFlyuqJvhp3QGpJeeO8w_OAZMc4r63jfJ-v_-MLJnXWrX_GhOL4PULmSz3ejmvh9o0HqVC7tXciXGujIhujvxgyKAxUeMQRlliF-G6eBAps6bMntbB7FIo6xRFVme7cSaV9J1Ip-GrgAlPpwNzFKH2dSA5Jsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمود کریمی، مداح حکومتی، در مراسمی برای علی خامنه‌ای نوحه‌ای به زبان انگلیسی خواند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72365" target="_blank">📅 16:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72364">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=OZ0h8owKs7neBdmvLqnVZb7SmJJz5he-VIcvaxmcZ-dYwtlPZIo4gbg2cwEWHbg96wxLfJhrLrMPoPWRHgiob8Ed8V2r09qxVgQNZb3c07dRxXq44ipgFTIzz4xnMCTrzpasEEzwA_xuoe6ON95f4WIrh6IglLgVXDH6-_Uc0Eqw2zy0qdQFbos7WGhumKXm4RtQ8j8fHt3nYYTHGzppyBKmJ6ElWxTOUB5-L9j_RcUpqQ1AwriNXUaHJL8-ERheK792QNqkr4i2zgVF70pxbyBDaw9mghOvdol0Iu6G5A7iVnzRLAayoOzWeCw_g-571ncOHMA67Om9jDGJK0XtgrAS-_req7_iw6G4tkHQrasinhl54sMXOM71Ae9HX8uF9zWdAjstajRVsohPcmFFiOehR8OEYniHuG5hxcGjuzuzSuNJZs_y3gF3BAnG2dIsY5Ane78NBig1gD3Aj_Ns0Wof_YQ9_Nv-ydXG8ZZSTIRpfSMUdG_6517PEyNa8u7RCY7oiI2Ob4Zbj4I9pzaS66MDgQpUL-kXcaf2KutM_N-q--lS4_6mmbur-qWIMbjaL9WF0F5yvXRNJUd3k5kYrOJZP3Wv1U0kLW_a0A0Lop5yc36PfVAy5nrVncH8J6dOIF0kI9DecCzRUZ_QVJ7IlvFCrwfXZwd-bQA8oJxSQlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94d47f6b44.mp4?token=OZ0h8owKs7neBdmvLqnVZb7SmJJz5he-VIcvaxmcZ-dYwtlPZIo4gbg2cwEWHbg96wxLfJhrLrMPoPWRHgiob8Ed8V2r09qxVgQNZb3c07dRxXq44ipgFTIzz4xnMCTrzpasEEzwA_xuoe6ON95f4WIrh6IglLgVXDH6-_Uc0Eqw2zy0qdQFbos7WGhumKXm4RtQ8j8fHt3nYYTHGzppyBKmJ6ElWxTOUB5-L9j_RcUpqQ1AwriNXUaHJL8-ERheK792QNqkr4i2zgVF70pxbyBDaw9mghOvdol0Iu6G5A7iVnzRLAayoOzWeCw_g-571ncOHMA67Om9jDGJK0XtgrAS-_req7_iw6G4tkHQrasinhl54sMXOM71Ae9HX8uF9zWdAjstajRVsohPcmFFiOehR8OEYniHuG5hxcGjuzuzSuNJZs_y3gF3BAnG2dIsY5Ane78NBig1gD3Aj_Ns0Wof_YQ9_Nv-ydXG8ZZSTIRpfSMUdG_6517PEyNa8u7RCY7oiI2Ob4Zbj4I9pzaS66MDgQpUL-kXcaf2KutM_N-q--lS4_6mmbur-qWIMbjaL9WF0F5yvXRNJUd3k5kYrOJZP3Wv1U0kLW_a0A0Lop5yc36PfVAy5nrVncH8J6dOIF0kI9DecCzRUZ_QVJ7IlvFCrwfXZwd-bQA8oJxSQlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک بالگرد رسانه‌ای تصاویری از بمب‌افکن‌های B-1B نیروی هوایی ایالات متحده ثبت کرده است که در محوطه‌های پارکینگ شرقی پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) مستقر شده‌اند؛ این در حالی است که یگان‌های خنثی‌سازی بمب همچنان مشغول عملیات پاکسازی مهمات منفجرنشده در منطقه «وِل‌فورد» (Whelford) در مجاورت این پایگاه هوایی هستند.
این پایگاه برای ایالات متحده در جریان جنگ علیه ایران، نقشی حیاتی داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72364" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72362">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWrkeuyr6YaR2bZDTP2KZOaI9FHzOBsKItiBYKL-ntYRaApTf7vH8u-uA7t_tqXrnSRpUNpC4XgoUt-cLJ4ifseThm0XbvytMMpn-253BjA2Wqjy5v08txAyZg9pPVZ4f-yXVRGqbJJ_LXTCOgiCN-gVBEA5AL-i1lVFwZEYgfNRAXy98aKYvLkXfNDB3UVYtY56y1uBdT2qlso5rYMZLvITvSDtn_7FWFPx6oQnObTivvQKBhM6tv1uGpbHPq8sV8iGNhCITCPXOwGBTfpvufH-XYLrpFN-hr10f2HvyZXwQHiYxdog3NDseSzFKxtiuH3PYo6lEL0DlHwftpkuKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=UDV-KEu66OY8KIjut6vd-3YW5nWmxCILZzCOVPfOq8WhHJkkDPKbK9QwG0QoEEPf0tB414e3S_QDOvi6WkiJo-XdAQW1syPeHVJ5B3LW6zlLIqyW_hnpaZ6q-pwGnw9YX0ql9QgpF7COFEl7o7mCMvwRyRvHhe9zyHw7WfcUtdGxZaC0SOF-P_pKJsgdc0P451htaw_8DsFVBSKjOScYPnkoJmRzaGNaVpYXSv2xJ7jZhh8dQ8MvbJp-U21d0RcQe-a9dOEARkrVN1QEJ5iW8BCCdkKvKGLW2lu2lX6Vzlqt7EJugKbeSaakvdZgpTP12ECygGX8P9nzzlnE-w-duA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a6bd02b6.mp4?token=UDV-KEu66OY8KIjut6vd-3YW5nWmxCILZzCOVPfOq8WhHJkkDPKbK9QwG0QoEEPf0tB414e3S_QDOvi6WkiJo-XdAQW1syPeHVJ5B3LW6zlLIqyW_hnpaZ6q-pwGnw9YX0ql9QgpF7COFEl7o7mCMvwRyRvHhe9zyHw7WfcUtdGxZaC0SOF-P_pKJsgdc0P451htaw_8DsFVBSKjOScYPnkoJmRzaGNaVpYXSv2xJ7jZhh8dQ8MvbJp-U21d0RcQe-a9dOEARkrVN1QEJ5iW8BCCdkKvKGLW2lu2lX6Vzlqt7EJugKbeSaakvdZgpTP12ECygGX8P9nzzlnE-w-duA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی ارتش اسرائیل لحظاتی پیش منطقه «حداثا» در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72362" target="_blank">📅 15:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72361">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=VmLaOwd0K26hYzOkwlVZaSLPfzQLUOaMmoaB99Hm11ob5IMQRRAmphe4YAXNY4ipRvlRI2ezeyTNrwkoB3QIVOHsxBXSquPxlB9J3TNDY3EjmUr0rbcJG9yxiA1YIERwcO97whlIqdK0ayGGhiUHIsbHjswnjHCGdj-ya5-0w5m1ixQBxS6Ci6VL-cCNfrLY9DVTolnhVAH_eXUruGzRR7A-UxpatjK4vTIC5Erxqnv1EkPMHyXSZ8QWTb5TEAaMjv6xRgErHTtxwpslWMwy0yePFp0U3SQQA-hbVh7WdTCkl8khe2lGwhm8fh4L5qViK6jdwfJAnLY0aPexQmZLxrhkloSB0F9FskNWVunv4_PsYcEaV6LDlXAzHK4egTe2N7O5K5kF21d-C36JcWnhhaiQu0Y1p8MzVUChj9BduR3-wg-5K2y3yJfh60fWW551lsRLIqdyZ5rmxCfQ1xojE_tTyjPqn8ecpDp6aWJxluKbXS_3U0Ao3AUVflIq-EVT1I4yvJQa7X-ogq-GhanWDttv2jVPJx7lGkcXUpW7aj4hag__rA73fRF6B3ljpMx2ePdV2jINA0AOudBzKGSOMwRMFzouJSI3YaIBdM8IMpw7Ievlk9gzlOLbWz_oE0NzvUPHumO9V8drC3d6lmwYQnt6nKJUNQix6DmsSyl34JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85f2632d6.mp4?token=VmLaOwd0K26hYzOkwlVZaSLPfzQLUOaMmoaB99Hm11ob5IMQRRAmphe4YAXNY4ipRvlRI2ezeyTNrwkoB3QIVOHsxBXSquPxlB9J3TNDY3EjmUr0rbcJG9yxiA1YIERwcO97whlIqdK0ayGGhiUHIsbHjswnjHCGdj-ya5-0w5m1ixQBxS6Ci6VL-cCNfrLY9DVTolnhVAH_eXUruGzRR7A-UxpatjK4vTIC5Erxqnv1EkPMHyXSZ8QWTb5TEAaMjv6xRgErHTtxwpslWMwy0yePFp0U3SQQA-hbVh7WdTCkl8khe2lGwhm8fh4L5qViK6jdwfJAnLY0aPexQmZLxrhkloSB0F9FskNWVunv4_PsYcEaV6LDlXAzHK4egTe2N7O5K5kF21d-C36JcWnhhaiQu0Y1p8MzVUChj9BduR3-wg-5K2y3yJfh60fWW551lsRLIqdyZ5rmxCfQ1xojE_tTyjPqn8ecpDp6aWJxluKbXS_3U0Ao3AUVflIq-EVT1I4yvJQa7X-ogq-GhanWDttv2jVPJx7lGkcXUpW7aj4hag__rA73fRF6B3ljpMx2ePdV2jINA0AOudBzKGSOMwRMFzouJSI3YaIBdM8IMpw7Ievlk9gzlOLbWz_oE0NzvUPHumO9V8drC3d6lmwYQnt6nKJUNQix6DmsSyl34JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریه های یک خانم به خاطر شرایط اضطراری که واسش به وجود اومده و عدم وجود سرویس بهداشتی در مترو.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72361" target="_blank">📅 15:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72360">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تمسخر پزشکیان در شبکه فاکس‌نیوز؛
در مصاحبه ای که با رئیس جمهور ایران پژاکیان(پزشکیان) کردیم همش جوابای مبهم و بی معنی میداد.
اصلا اون به هیچ سوالی جواب نداد.
حتی نتونست بگه رهبر رو دیده یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72360" target="_blank">📅 14:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72358">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pY0pNNNcV97l5Drkt4IqjgAIMCPuLNU_ElMUlJMHUz8hVNeyztlZJr_rFaWGFB02ul3Iruj_AvT1nMYEZZ490SFtigAUM_jYrJWGEIDbuXXAL0--Z0m1c_jmx-EFwZmT0jeDKx1fTrFGxUcvtVyJSriazslpJ7zuuB0YLIohe2RwPArUG2hedyg9DkM560RTbMQZE9Wj708aKp-h_8__cWLdx2vz0Eu7Z-YiMDP60AGLGsWtkiBgLeyC3esmPYYO3v6WV4n9fm7jsFtY14MQOAAr1wFbmsUhLvVbiWFxJKuWK8sdjWOuPtBWAWXWaq26T7nz8c7ONJeSsOinfh4dIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=pz0g1beynpU0kLKlbhfr72FEp1HZs0_CMDJTI7mO6ptiM-aH59VVXuk-u_eGICE2P-AURRaLraselTikUmTq47pOUzHfFxmHyF9mET3bt95AmCACCrIdcdfGaYC0K3TsPJLCiZULC_j5AiqVzmTrFENfs8cXCkE6PUltkjwVxiQsWhZdzYShGwVTpK8LGoNcSvtF_58p7jh46G6dLcTFQEkGPtDuPcA2Cg_JJM22yLrRxhIs4SpIo_Aeu53wX_1270SGqlOnND7qqfJHZvI5orOJuRU9WjOBFZ9WwTzeKCLT2JtNDN2GyjGin-q19eb1tkuIWqbvQJVPFA5CdgH_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2634d568.mp4?token=pz0g1beynpU0kLKlbhfr72FEp1HZs0_CMDJTI7mO6ptiM-aH59VVXuk-u_eGICE2P-AURRaLraselTikUmTq47pOUzHfFxmHyF9mET3bt95AmCACCrIdcdfGaYC0K3TsPJLCiZULC_j5AiqVzmTrFENfs8cXCkE6PUltkjwVxiQsWhZdzYShGwVTpK8LGoNcSvtF_58p7jh46G6dLcTFQEkGPtDuPcA2Cg_JJM22yLrRxhIs4SpIo_Aeu53wX_1270SGqlOnND7qqfJHZvI5orOJuRU9WjOBFZ9WwTzeKCLT2JtNDN2GyjGin-q19eb1tkuIWqbvQJVPFA5CdgH_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی
سپاه پاسداران:دومین زهپاد(زیرسطحی )ارتش آمریکا در تنگه هرمز شکار شد.
شناور توقیف‌شده از نوع پیشرفته «Remus 600» است که به گفته سپاه، متعلق به «ارتش آمریکا» بوده و با اهداف جاسوسی فعالیت می‌کرده است.
این شناور طی یک عملیات هماهنگ و با بهره‌گیری از قابلیت‌های اطلاعاتی و جنگ الکترونیک توقیف شد و هم‌اکنون برای استخراج اطلاعات در اختیار کارشناسان سپاه قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72358" target="_blank">📅 14:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72356">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4389424237.mp4?token=ZtRuMhYC9FC2DILXHCMzn_7KJBpRjZUbn-gRgylLFDZHQhwEEoybcApYCLwR4CJjjTy5DfraeHOJmldUK-x-eRckhjhJcoCnET2VmWyCnzHRHlwLh97bJMVMeuLaG1wKwiXJRtBH4W6yBo6dUZvy-dM2Tg0jDX-LBYgnN7r-Lku7OY6H2qQ0cKv64TcI3-0pgJKnGvOr5UVvSLMlnfLOZsiDWEsgcgmTKLz-tDBGQ8SZPRzHDBVuLeiVAtbfdVbGjuUf2f_3xSOty1qIYoE7b2bateA2fH7sGjpdij5aiiyj70X0-TxyzQOnkOoWdjfDr25Ir7HQZVoR-U_nhOtnsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4389424237.mp4?token=ZtRuMhYC9FC2DILXHCMzn_7KJBpRjZUbn-gRgylLFDZHQhwEEoybcApYCLwR4CJjjTy5DfraeHOJmldUK-x-eRckhjhJcoCnET2VmWyCnzHRHlwLh97bJMVMeuLaG1wKwiXJRtBH4W6yBo6dUZvy-dM2Tg0jDX-LBYgnN7r-Lku7OY6H2qQ0cKv64TcI3-0pgJKnGvOr5UVvSLMlnfLOZsiDWEsgcgmTKLz-tDBGQ8SZPRzHDBVuLeiVAtbfdVbGjuUf2f_3xSOty1qIYoE7b2bateA2fH7sGjpdij5aiiyj70X0-TxyzQOnkOoWdjfDr25Ir7HQZVoR-U_nhOtnsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش در چنین روزی سید حسن نصرالله به همراه چند فرمانده ارشد حزب‌الله و سپاه پاسداران در حمله نیروی هوایی اسرائیل کشته شدند.
در آن عملیات ۸۳ بمب سنگرشکن ۲۰۰۰ پوندی به مقر فرماندهی زیرزمینی حزب‌الله در زیر یک شهرک ضاحیه بیروت اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72356" target="_blank">📅 13:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72355">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=D_gUlLCZS5f-Zw53qw30JwzJZy02-0ZBKxdV5A5qBUXkeiYfGZqQR2f4-2c21Cu777RATUCB6nY6GDTKcmvifrcZ87i_mztqEsPXKzYQQAkdGNwC3tNV3JpNWqlh5mEfhWmmL_gR0ngOiRuNDWe_9p0UzXns19LgPqZpeZjT0e1mgEEECA156dOYIEzkhfumvjJdRgukEnlimcqGcOhwrUmPq6oyZEdg-_r7UOtLTv47TSjqQZHSOSpVzBkA74wOZMBftmWbOUaw94M8kzFU0YbV_P-xTPiFScZEwqbrUItOPOhCRbWe8AE28NBKFgNEZCsZhH5JvFvobFiSytwNZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a80862.mp4?token=D_gUlLCZS5f-Zw53qw30JwzJZy02-0ZBKxdV5A5qBUXkeiYfGZqQR2f4-2c21Cu777RATUCB6nY6GDTKcmvifrcZ87i_mztqEsPXKzYQQAkdGNwC3tNV3JpNWqlh5mEfhWmmL_gR0ngOiRuNDWe_9p0UzXns19LgPqZpeZjT0e1mgEEECA156dOYIEzkhfumvjJdRgukEnlimcqGcOhwrUmPq6oyZEdg-_r7UOtLTv47TSjqQZHSOSpVzBkA74wOZMBftmWbOUaw94M8kzFU0YbV_P-xTPiFScZEwqbrUItOPOhCRbWe8AE28NBKFgNEZCsZhH5JvFvobFiSytwNZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ابطحی میگه: سال ۸۸ توی زندان گفتند اعتراف کن که خاتمی به اسرائیل سفر کرده
گفتم خب سفر نکرده
گفتند اگر بگویی که به اسرائیل سفر کرده، آینده دینی ایران را ایمن نگه می‌داریم...!
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72355" target="_blank">📅 13:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72354">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWLVJcZUVxAIrPcuQWPz9P19TCU37ZTmhzJi6Z8DJnFE5kBBQhFpAVIouQzIgcaJaLdhx1ZGj6RIap3qdvxIyQVZVmlm_slILOkvUNa41nfVJBbYur1eTUi3sqLv7ZGUjv2zfosKs7ybyCzR2yjbGlo6N-oFkiM5bLlDrp6qFyryHRy1UALwmD2r2b3_v0dDM9Bu9Oa2P0PD3MZPXnjwpZl0_cvd-H3s7SNi2ijF8j-mYKH5Waq1qwB1hR_XMxyXgUxvsO_TSsV-ppe2mWxvpwaHvWs2_otFTbUio1tBwfEWqxyhQSxLlxyhOC9Ym7MzemmxuoBS6F9LheiUlZWjrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا:
در پی آغاز «عملیات طرد اقتصادی» (Operation Economic Outcast)، وزارت خزانه‌داری ایالات متحده اقدامات مالی هدفمندی را علیه بانک‌ها و شرکت‌های ارائه‌دهنده خدمات هوانوردی اعمال کرد. به دستور من، تیم‌هایی به سراسر جهان اعزام شدند تا با کشورها رایزنی کرده و خواستار اقدام علیه رژیم ایران شوند.
این تلاش‌ها در حال به ثمر نشستن است. ترکیه و عمان از توقف پروازهای «هواپیمایی ماهان» به کشورهای خود خبر دادند. امارات متحده عربی نیز تمامی پروازهای شرکت‌های هواپیمایی ایرانی را متوقف کرده و بانک‌های تجاری بزرگ در امارات و ترکیه، انجام هرگونه تراکنش مالی با ایران را متوقف ساخته‌اند.
حتی رهبران ایران نیز به پیامدهای اقتصادی این وضعیت اذعان کرده‌اند، چرا که ارزش ریال به پایین‌ترین حد تاریخی خود سقوط کرده است.
من از دولت‌های بریتانیا، ترکیه، عمان و امارات متحده عربی قدردانی می‌کنم. ما به همکاری‌های خود ادامه خواهیم داد، زیرا برای جلوگیری از پیشبرد دستورکار تروریستی تهران، هنوز کارهای بیشتری باید انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72354" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72353">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72353" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72352">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZJmUb8NbFaWj933h5to1oxG5pRVjtLdaXoch9OZzLTWSk_l8T2ecKdez6-Dby63AwLj4pM0mVR3lgR6_I7JpCSY56G-jr6yU5MZKyQ_5r2zk5PBZaTyyK7f6_WZ7otjEns5LSQIkWlSLVEVcjbLacrq89auTr2Ki3nb2OExVuk33nrgZNvT5xfcbkB1nU_Uc8ijR54j9GvvdLjcFHOMs6DjQL0Gk3RQsmYYto-STIiBMS31eDpxPcWozPplatabhPeJBo3jVaqr1fon-WilDQbJSkOSzdMVgrT4hEB8Xhx144FyKNfDV692_ME-OsOrjMpATnOC5HNdhD7UNXE-Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
پرتغال
🆚
نروژ
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۸ گل زده
نروژ: ۳ برد، ۲ شکست و ۹ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72352" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72351">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مدارس ریاض به دستور مقامات سعودی و بدون اعلام دلیل رسمی، به مدت یک هفته به آموزش از راه دور روی آورده‌اند.
این تصمیم یک روز پس از آن اتخاذ شد که پدافند هوایی عربستان دو پهپاد حوثی را که ریاض را هدف قرار داده بودند، رهگیری و منهدم کرد؛ اقدامی که در بحبوحه تشدید حملات حوثی‌ها به این پادشاهی صورت گرفت.
در دو پیام جداگانه که خبرگزاری فرانسه (AFP) آن‌ها را مشاهده کرده، آمده است: «به‌تازگی از سوی مقامات سعودی مطلع شدیم که مدارس باید در تمام طول هفته تعطیل بمانند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72351" target="_blank">📅 11:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72348">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9gYDwSUb4LNzqS4ctUh0Wxe0J-QIvOU5Rc5k0wcfa5xOL2H-wjITd-sTVBLP_MiKIoBkD_uaYFf6imm3UyH_OubUhjn9PwMsW-2fwuPcRoZ2SEytneWMrSj8au_BmE3eHhtRrVPnrdFofYRNSewDqGDtFQkaQtHoFms7tf0qmAHg-yNGi-Qch3kS73AQEOtHCkw1ulWZLx5eHQvHWBZO3xaVwmkFIJ9-MzAkQzZy9nnEz_6efq8D9CumKHtcwJX7mRG2Ul4RhmaR4CzIyXwC_7YUfyPtybeaXfCcA692N17eBkuQlIqo7gr0Axrmplh5CBPk1WfTInegeCxrTvseQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a0FXYj9J3uu2k-LeyYqYUdd2zGkeCpJHRiTJq1ocMB_WJ8jfpNa34RzIQL6CUEUAAvQtdfYnFCfeeuoMqTYWhmkt3GSVcOaonCb5imfNm8lDXrQSl8wNRFTW2146CDPfGdxSXpxFsV6_bv98fhbGxSyOSi_bIjexBYLX2rbo_Z49_fYwvwmga5Lm2zX7p8YTS3m7bTYFvIwNOKZeBzl6UJVQicjzSumBhkhae1Hs-aab6WzgqDIqCjFe4so3tTmOeekG6O7M-jqAnftmtLMtJiKgPxf69iI-EcPcjOVnB-_iFVTqsmoP-x98OLbYBR9GPlS28xfL9os4hgOp5RaPBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PjG7NJCZSbVqzDqz2I-_F-P9NoWoPHZCDK3WFDmZXohlJzUZDQt0bP-WiUIgILXSGbYbdEMq5B71bo3WW4izPN1v3OmyDDchfCeT-JR_HjdZujKUpEXewsDEyok5wB3kpFmnysmaHMYJkTD5CvUz68rmPazmLrD2eH0d1Ud_1aq5_zDPWSHtki1FiVQ-qk0hGMj14FRaDImRsdyNNifcSX46rNu7KTy2RRVcgCb1CTHwivQaQEr3TScUMNPy8ditJFm6FUVOKmSkjjbU1nMH_WPniBhOuqt09_ej2BL_Q3ynSYzoK2DE0SRHgNjd8HLBy2eKklVxbSM68evuDbz6fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رژیم جمهوری اسلامی که خودش فرودگاه نجف را ساخته بود و هزینه‌ی آن را تقبل کرده بود، از استفاده از این فرودگاه محروم شد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72348" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72347">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=gHY6R5EABz6qN6nmdVf0VsOeCJ5c0wWYvisFIaO6PN-ficHRiH6zL2SaU7-1KifCly2HZtUii-XavIkFHXRGhhOYkceTh2N6S8jdVkGTXthi0oQOH0BqxUVCHPRpdEqH_vW600oF0P0YnT2gIHXpWoHiSsHdFcL4kSd0bwcP-wfV3oT9DmSBgg1OLzwObC09-hpH4u2QS8N83kVjLL6gMY1RwVFSPFePvyA5q6uS_5pAIdQ6q5e5Lf-FPSNuvOh5y-Co1b90_3g0VEz9XwznWTNKmYsMbfMaoxX4ZaBeUlF5klcRDfgrzZ5OXxp2enV5EYa8inNi2G7T-Co6f6B7jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c28b66c8.mp4?token=gHY6R5EABz6qN6nmdVf0VsOeCJ5c0wWYvisFIaO6PN-ficHRiH6zL2SaU7-1KifCly2HZtUii-XavIkFHXRGhhOYkceTh2N6S8jdVkGTXthi0oQOH0BqxUVCHPRpdEqH_vW600oF0P0YnT2gIHXpWoHiSsHdFcL4kSd0bwcP-wfV3oT9DmSBgg1OLzwObC09-hpH4u2QS8N83kVjLL6gMY1RwVFSPFePvyA5q6uS_5pAIdQ6q5e5Lf-FPSNuvOh5y-Co1b90_3g0VEz9XwznWTNKmYsMbfMaoxX4ZaBeUlF5klcRDfgrzZ5OXxp2enV5EYa8inNi2G7T-Co6f6B7jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌سخنگوی ارشد نیروهای مسلح ج ا :
آمریکایی‌ها باید خواب این را ببینند که در مدیریت تنگهٔ هرمز دخالت کنند و در صورت دخالت سیلی از نیروهای مسلح ایران خواهند خورد؛ آن‌ها باید از منطقهٔ ما بروند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72347" target="_blank">📅 11:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72346">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=Wk2qQ3d0mo0vG1shn3_mrGs0I9rfzyWbmbOmsvUApUoj14H8Ex-kXnEIkyg0SGaRnaM-bzJn6ygi3SmH3grm3dN-6aAzsVYu_3T5TXcumQyap_wK3-sgjyYqLGtAYozkW68PTt0DtDTKwNTcytzdX2k0sdTFyT9L6164FZDJ6NQNmF1fhKVV6VCIos36LKsScuWiM4XPNtn7o1RPQ3CXPTfs3UCcEUEENo6Hh2rsjoHjy1fxQu2_Za3NHuQO0LHMYKveAgJ2z1HFZPS3XwRQ5GNHUdm-n1iab2UePyhKMDfLvhewEbLv0KLeWfrbFfR6ET0CP2lHfwI9ptQ5IsfRlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/58f2375d54.mp4?token=Wk2qQ3d0mo0vG1shn3_mrGs0I9rfzyWbmbOmsvUApUoj14H8Ex-kXnEIkyg0SGaRnaM-bzJn6ygi3SmH3grm3dN-6aAzsVYu_3T5TXcumQyap_wK3-sgjyYqLGtAYozkW68PTt0DtDTKwNTcytzdX2k0sdTFyT9L6164FZDJ6NQNmF1fhKVV6VCIos36LKsScuWiM4XPNtn7o1RPQ3CXPTfs3UCcEUEENo6Hh2rsjoHjy1fxQu2_Za3NHuQO0LHMYKveAgJ2z1HFZPS3XwRQ5GNHUdm-n1iab2UePyhKMDfLvhewEbLv0KLeWfrbFfR6ET0CP2lHfwI9ptQ5IsfRlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای ایشون در مورد مظلومیت پسرا، بیشترین لایک ۲۴ ساعت اخیر رو داشته:
پسرا از یه جایی به بعد، از بس کار دارن و به فکر آینده‌ان، حتی یادشون نمیاد که کِی تولدشونه!
ولی همینکه یکی باشه و بهشون بگه تو چقدر برام مهم و با ارزشی، اندازه هزاران کادوی میلیاردی براشون ارزش داره!
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72346" target="_blank">📅 10:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72345">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OD8eN0z3oqJ0P5AsNQz6CQK_oB2G_Q1LYAkKUbC4i5ft5IqfiLW3xx2WgzMdhLlLNan1LTd-6tEWJmbq4clP5NY2Jj8O26gzdAZo0WGDHEKjGz5xq5fWTKBzZWtjhvawQsc6JdG3lg0rJ6dypPqghgBNbEg3PmvNRZk-r2L2k9OmG1NpI2pkckdX8iFaiItr28qSTuYeXdwgA2NLRU-meofHlM8fwASrIc-7XyY6X3lAg7V1aF2YsDBF6WT3E60IqIZSQ3ton1_gKr65arYiDCXgi1cAeUxhZppPYPh_zMuD5ldi-_-FhE4Doo-fagV5q3vF-XjvtlXTWKdSjsBHeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی ارشد نیروهای مسلح جمهوری اسلامی :
قدرتمندترین ارتش جهان مقابل نیروهای مسلح ایران زانو زد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72345" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72344">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=GOPOD5yp76sI-yU4QY11XILj0dTwCLY1MVkedHQPXSyrFvqI40xMhX0240Ta1DZGWh1AwvVq_A8SW10JTlEH2H3e-xT879pRa19HAT3CzlyprQ7Wz8S9Vhc2r_HCUs6ScdDxXu8HQmTMmg-kWT0SZUdQd06Wbvtm1cP_DI6kc43KcbQ55gFz53fqXbyoZE4KO50KLhAmmYMw6pxrL8OBZGttpq1B16IW3iOEzqaPiOk4NwAySmmambD7B7bWKQWvl2xaGqnFeUlCFB5ts3bVl35-EqHAZmTCgm4EWjZJax9YHoGTwikHyXDDJT-9FrTOnHUpQJmBQwiYwI8vXXC_dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c277f60d17.mp4?token=GOPOD5yp76sI-yU4QY11XILj0dTwCLY1MVkedHQPXSyrFvqI40xMhX0240Ta1DZGWh1AwvVq_A8SW10JTlEH2H3e-xT879pRa19HAT3CzlyprQ7Wz8S9Vhc2r_HCUs6ScdDxXu8HQmTMmg-kWT0SZUdQd06Wbvtm1cP_DI6kc43KcbQ55gFz53fqXbyoZE4KO50KLhAmmYMw6pxrL8OBZGttpq1B16IW3iOEzqaPiOk4NwAySmmambD7B7bWKQWvl2xaGqnFeUlCFB5ts3bVl35-EqHAZmTCgm4EWjZJax9YHoGTwikHyXDDJT-9FrTOnHUpQJmBQwiYwI8vXXC_dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آقای سفیر، پیام دولت آمریکا به مردم ایران چیه؟؟
سفیر آمریکا در سازمان ملل: این رژیم تروریستی باید بره راهی دیگه نیست
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72344" target="_blank">📅 09:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72343">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3TBsBTjfQrLVBWq0VdSfXIqoRElAXk4V__xpDW8f5BzxGb7L-Tq9DQb_GdnOiNK7v2D4CmSoyhuW_b_HvLpr7kFtCCq_gVmYzsWsDcZ1rKEi0ZCUTWhLiVl_0kHzwA6z3pXFHuunasyACAZAx6-UldxMpfS2EKix-MnzIa_WxILrO2TLAy7RfvLOBGEz1JmdFniaLDL-n40iHzIZof4j2aP-k3DpaqgQWs_71M0vsTcOpsRjPqX4Hfj3YlPi8ZAhEMNW05g56pT_MNHXDGFRvWD58_U6EnQ3WuMHwzQiOge9ZQfEU7q7yeRezvxGkqXB8Iuizx8JNAEOeE9s-7nCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال‌استریت ژورنال، دولت ترامپ فشار اقتصادی خود را بر ایران افزایش داده و از کشورها در سراسر خاورمیانه و اروپا می‌خواهد تا روابط هوایی و بانکی خود را با تهران قطع کنند.
جاناتان برک، مسئول ارشد وزارت خزانه‌داری آمریکا، این ماه از چندین کشور بازدید کرد و به شرکای تجاری ایران هشدار داد که باید بین انجام تجارت با تهران یا واشنگتن یکی را انتخاب کنند.
در پی این کمپین دیپلماتیک، عمان، امارات متحده عربی و ترکیه، پروازهای ایران را محدود کردند، در حالی که مقامات امارات، تراکنش‌های مرتبط با ایران را توسط بانک ملی مسدود کردند و ترکیه، مجوز فعالیت بانک ملت را لغو کرد.
آذربایجان و گرجستان نیز پروازهای شرکت‌های هواپیمایی ایران را محدود کرده‌اند، در حالی که بریتانیا قصد دارد معافیت‌های بانکی را که به موسسات مالی ایران اجازه فعالیت در لندن را داده بود، لغو کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72343" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72342">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72342" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72342" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72341">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUYRgLjcJgC-DsyqsKR1csqLbjRijKN9Fyq6AlltS43i15XqmCiq-aOZV7yuR7_Ltdpf77ijsOYcndifpE0FWK5Y1mLnMikOc4r9xvRvA4DCZNdFpjdBQw3u4Eb77TkzBmvA19_xDhWx3C7P06YA4Pb4qZKISMfBFiYyleQoadvnziWsNeEQXXSn_6yAiajqwEXy8rZYtrCQGVKpTZKZzB8HklvqGnm3xAt752Y2UbYNtUg-_mGVxjdr-nhNOmoAPuMifmxpRgZcEurbPfuncRgtVeXtHvvNEgMMo6l4cvEmm99PSahrHESSERd_oY7uYWTnyJCdDZEzHJP5JFdVag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72341" target="_blank">📅 01:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72340">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجار های جدید در تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72340" target="_blank">📅 01:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72339">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سپاه پاسداران:توی جنگ بعدی ناوها و ناوشکن‌های دشمن حتی توی اقیانوس هند هم امنیت نداره و قطعا هدف قرارشون میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72339" target="_blank">📅 01:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72338">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72338" target="_blank">📅 00:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72336">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ایلیا هاشمی:
ساعت در محدوده ۰۰:۱۵ الی ۰۰:۴۰ بامداد یکشنبه، چندین انفجار مهیب همراه با لرزش در محدوده تنگه هرمز شنیده شد.
تحرکات نظامیِ سواحل جنوبی هرمزگان در کنار تعداد و شدت انفجارهای امشب، نسبت به دو ماهه اخیر بی‌سابقه است و می‌تواند گسترده‌تر شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72336" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72335">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شنیده شدن صدای چند انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72335" target="_blank">📅 00:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72334">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">عراقچی رفته نیویورک گفته اگه این هفت تا کارو بکنید تنگه رو باز می‌کنیم، اونام گفتن مرتیکه جاکش تنگه که دست خودمونه پس صیکتیر کن تا پیشنهاد بعدی
و این شد پایان این دوره از مذاکرات:
#hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/72334" target="_blank">📅 00:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72333">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=BGBcVYVx1iglXmvksLPwCpjpneynZt9EupmqEXviMNlcG-oEHli2ayIadFQK5EvCKHo8AeQo0Az3oN5U5yFMymE8rUH32FZZHKEqvg4L2qs9RQT5xx2iIDg6Z0GbjiAZpnGr-pkmpG8qIc4xt8w-nv7Jiwh5Qj8wE9tnsduIuymBypEgiOm0XeMaycENsak5I4TPQWEvThle3kscSB22dzFIN7Q7U02XXXSaMPD4ezLJwcdpg2IwHuwoIvmf5ayB38g5SNby28opVcriHkaKBN15KhDRSeu71Jxes74I4E_689cryAQGn-z6q-ynMTFusTLtS-qAWthCco91RyQwRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b153f7fb8.mp4?token=BGBcVYVx1iglXmvksLPwCpjpneynZt9EupmqEXviMNlcG-oEHli2ayIadFQK5EvCKHo8AeQo0Az3oN5U5yFMymE8rUH32FZZHKEqvg4L2qs9RQT5xx2iIDg6Z0GbjiAZpnGr-pkmpG8qIc4xt8w-nv7Jiwh5Qj8wE9tnsduIuymBypEgiOm0XeMaycENsak5I4TPQWEvThle3kscSB22dzFIN7Q7U02XXXSaMPD4ezLJwcdpg2IwHuwoIvmf5ayB38g5SNby28opVcriHkaKBN15KhDRSeu71Jxes74I4E_689cryAQGn-z6q-ynMTFusTLtS-qAWthCco91RyQwRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پریشب تو تهرانپارس، یه خانواده برای مریض بدحالشون با 115 تماس گرفتن تا آمبولانس بیاد و ببرتش بیمارستان؛
ولی از اونجایی که خودِ آمبولانس خراب شد، همراه‌هایِ مریض مجبور شدن تا نزدیکی‌های بیمارستان هُلش بدن:
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/72333" target="_blank">📅 23:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72332">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=YT3ivC_0Rzmbaa97Co4o2x2YaCQJeP8qvrlb4bRudY7CmhSMGFaqM0Lu7cUn2CwCRAAmkjf5IcYw0g38gHYsDtEgCrlFcPyRCDfLq87H7GikU6yu3oubXstKPQjGh8B_Y_VksBmqufoobWotpwC7AjlWIly3HfVl1fdAyuE_luDwiU4BC3plxaUHgMJ6pXWCBz-kKO6sZwmAzFQzjgi6awCbBVZwTabItZulemS84udtHTf1j7NvbQiCv9UxQwW3t21Pt3smKcviV5Y42-x0SUe-5knTldKmUYT-cyy0LTYQxTDgLi1zka8MbE3Ix4EaJ3KTZpqanvgfyj5bOcYmeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e49705c5.mp4?token=YT3ivC_0Rzmbaa97Co4o2x2YaCQJeP8qvrlb4bRudY7CmhSMGFaqM0Lu7cUn2CwCRAAmkjf5IcYw0g38gHYsDtEgCrlFcPyRCDfLq87H7GikU6yu3oubXstKPQjGh8B_Y_VksBmqufoobWotpwC7AjlWIly3HfVl1fdAyuE_luDwiU4BC3plxaUHgMJ6pXWCBz-kKO6sZwmAzFQzjgi6awCbBVZwTabItZulemS84udtHTf1j7NvbQiCv9UxQwW3t21Pt3smKcviV5Y42-x0SUe-5knTldKmUYT-cyy0LTYQxTDgLi1zka8MbE3Ix4EaJ3KTZpqanvgfyj5bOcYmeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز داخل تهران اولین مرکز آموزش نظامی برای جان‌فداها افتتاح شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72332" target="_blank">📅 22:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72331">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=Rd0Mc923xgMe-wf-0zr3z9abghixNOE87Z42dOBWZNZDD1WilD0OSnOCsJWKd5uMSVcq9BeG0v1IAOMs3b6Zobv0QqPC_eeQ7k_GsJHJ64A0qR9PsaNDma8DFDV6mKYNPfSEELI9nzT9I8z6qBI5k3_YTULkIXEbYlbqVS2mhJfcpgZAUZQaj0o-afISblM1j8mGezfMBpY0iXXnXbZoQjKVVMpxUcLDZA72AycGRlukHhm3wTz4rHpycRzzPj7MCsWHuQYF3roCXNcuVBi5qWlMBhkNg6hyrmeyZtwa7x-zS8fKDxh78YHFm_HISA-Hf75RXvXiZrvvZoEqJbG38A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff29e8be2f.mp4?token=Rd0Mc923xgMe-wf-0zr3z9abghixNOE87Z42dOBWZNZDD1WilD0OSnOCsJWKd5uMSVcq9BeG0v1IAOMs3b6Zobv0QqPC_eeQ7k_GsJHJ64A0qR9PsaNDma8DFDV6mKYNPfSEELI9nzT9I8z6qBI5k3_YTULkIXEbYlbqVS2mhJfcpgZAUZQaj0o-afISblM1j8mGezfMBpY0iXXnXbZoQjKVVMpxUcLDZA72AycGRlukHhm3wTz4rHpycRzzPj7MCsWHuQYF3roCXNcuVBi5qWlMBhkNg6hyrmeyZtwa7x-zS8fKDxh78YHFm_HISA-Hf75RXvXiZrvvZoEqJbG38A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرازیر شدن موج جدید افغان ها از کوه‌های صعب‌العبور به سوی خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72331" target="_blank">📅 21:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72328">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mtvk_GbgdranNYHzoYXLh7i1fJOu_834AVS6BgUTCpd0Nk0cFoTjMpSj8Yo0cnKDmOd2Op1uA4UIWut1t9aGpdY8zIuIwWFhZ4KsUUAtfrUWZCnyb3ZC102l0VErqocuuj2QUQuAsYG9eVapYzjJKN7bF_ekDarnYSpEtaEUsliHNg-HCwpS5Mgbhx0U2iqebV54J-ccoYPART1vUghtNl9dgTCFHObfJjzfAXY1cPZ9JEpt0wUzTQJoNKRH3XyS5zeSf-4sD5ItsQhw_Tmk64WfDQGLxTcFfbcsVTG4IiSFCr1OpT-uqDEtUMj6F4JBBoEHW3B9-ad4FOabn8stpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=TEDjCOJfnMp6Ap5uPoFmwDR2FbzcvPtLxkwumC6OWESo8rEgdGHpNdHTuat9r0IIpNz1rwcEZCWyJ9TsIWSePcs3stR_5Cc7L357CMjyw5Rxs2wc9GQCsyqPTOA3yYV0A9SvDTo6_TAwVXTqEuKt9NVLgvFIimshwdx23WVhSr1sB0azUwgmYgdZtEsGmysEV5RcKUr6bMBooGzHUWaGZumMrAM6VVagJenU-2OOehCKF-y5Vm_U0kk5mCjSHXVyxEY814Mm2IKC0gg723MAr8WtzkLaW1KahhfTGi6tudwiq7vAjxsonRVgbh5kDNVWqtDg5QVGw1tBofYp-UOPyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7fb8f6948.mp4?token=TEDjCOJfnMp6Ap5uPoFmwDR2FbzcvPtLxkwumC6OWESo8rEgdGHpNdHTuat9r0IIpNz1rwcEZCWyJ9TsIWSePcs3stR_5Cc7L357CMjyw5Rxs2wc9GQCsyqPTOA3yYV0A9SvDTo6_TAwVXTqEuKt9NVLgvFIimshwdx23WVhSr1sB0azUwgmYgdZtEsGmysEV5RcKUr6bMBooGzHUWaGZumMrAM6VVagJenU-2OOehCKF-y5Vm_U0kk5mCjSHXVyxEY814Mm2IKC0gg723MAr8WtzkLaW1KahhfTGi6tudwiq7vAjxsonRVgbh5kDNVWqtDg5QVGw1tBofYp-UOPyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۱۸ ساله یه مدت به خونه صمیمی‌ترین دوستش که مامان باباش طلاق گرفته بودن، رفت و آمد داشته.
بعد از یه مدت، دختره رو بابای دوستش که ۴۷ سالش بوده کراش میزنه و مخِ بابای صمیمی‌ترین دوستشو میزنه تا باهم ازدواج کنن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72328" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72327">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=DxR5DBr9okrbH25gwQi31-WE8okgSNZYc5oCQar5xOiZHJxCd-unMh2HUUqYrDQf2sXFnOybrHS_4AdTzsnwhtOsPVQvQz9frohYHhOpiIdAGlEV8nUsx0pNjvOXnSurPaJiaabveKlU216S_0PocqNxUm_OxHv8xacYeAIVgiECA-kXG-mCB_Kw7cTp6M2iGwZ_BEb-dmL17hXXZ2VHLzzmVPIZazA8doCYEE7gJ2-gXY3oQaF1FytatW58brWF7zx3PZQnvYEQ36POU65n1YditOOke_XGZP7mFSW_VzK0RKJ2-xy6ZiwWLRLPlX6C2p6Yfk9wp3TieRiRuIl9fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77bb2e5af4.mp4?token=DxR5DBr9okrbH25gwQi31-WE8okgSNZYc5oCQar5xOiZHJxCd-unMh2HUUqYrDQf2sXFnOybrHS_4AdTzsnwhtOsPVQvQz9frohYHhOpiIdAGlEV8nUsx0pNjvOXnSurPaJiaabveKlU216S_0PocqNxUm_OxHv8xacYeAIVgiECA-kXG-mCB_Kw7cTp6M2iGwZ_BEb-dmL17hXXZ2VHLzzmVPIZazA8doCYEE7gJ2-gXY3oQaF1FytatW58brWF7zx3PZQnvYEQ36POU65n1YditOOke_XGZP7mFSW_VzK0RKJ2-xy6ZiwWLRLPlX6C2p6Yfk9wp3TieRiRuIl9fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه مینی رپر کوچولو و زیبا
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72327" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72326">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72326" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72325">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-JRQZAs6ey6tpwWpOZbgfdbECEbw3-_1SYXQwrI9kQLK_RyC-36fT6PKj7Mrffy_8J3wuQFbuTJTgLUdsG-pb9HC_R5YDLbt3XdGIXUsg4dzz535yFTyXswBSrXBNCIByzMS6pb9NSsB6rElAXq7qyeIuL-ib0zmt2a5l2cmuHLAhx4GggXw5ZnqfhGZVD5DaXoh81VTV4vHwiElz0vwg_b7182xKmisuPr3gm9HbJo6dttuKnG5uhQ_V30_kizTiJO1ruOcscq04vtAzQirZJ1p49OdvBK__rhGj67WdT5lpG6jkUjBxji3NrzMcmw1uWtXz3rzShp9udG-JY5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا باید عضو کانال ما باشی؟
🔹
تحلیل‌های روزانه و اختصاصی بازی‌های مهم
🔹
پیشنهادهای ویژه با وین‌ریت بالا
🔹
استراتژی‌های مدیریت سرمایه برای جلوگیری از ضرر
🔹
پشتیبانی و پاسخگویی سریع در گروه VIP
همین حالا به جمع حرفه‌ای‌ها بپیوند و پیش از هر بازی، استراتژی برنده رو از ما بگیر!
🚀
همین حالا به جمع حرفه‌ای‌ها ملحق شو:
📢
ورود به کانال اصلی (آنالیزها و فرم‌های روزانه):
🔗
اینجا کلیک کنید و عضو کانال شوید
💬
ورود به سوپرگروه (چت و تبادل نظر کاربران):
🔗
اینجا کلیک کنید و به گروه بپیوندید</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72325" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72324">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">طبق گزارش های تایید نشده، عباس عراقچی بازگشتش به ایران تاخیر افتاده و قراره سه‌شنبه ۷ مهر ۱۴۰۵ (۲۹ سپتامبر ۲۰۲۶) از نیویورک به تهران برگرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72324" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72323">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9470296462.mp4?token=lC6VXlMx3L1yteR6ggrh1LdE46HboWryurdKPvAhX47W7F8iVpLabt8b74MpIcUcUjJaKwf3Bd3X5WITjJ3aKaqZAunsK6LfwwdSUSQlWsSyj8haOvaQmxhiPhWPMRJTka8OxzMxUx7nMfuW7hrDXWA-S7mmJqeFXeiQpYuv5DuDzqvGwOg07sJQfDn-bXVlfrBOJq0Aj2oBWF8k7kfBHGx-el0JyVylf-gPGfqa2a0-8wb38Duy3sIP8_3fybhKCwrexj22OkZjXB9fTNl-44xS_BnlWdhm1ZUzHCBPYv2uvvfYK0G-TBrRvOO5IoEkrV9sE_-h51tyg9XRD-Xlkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9470296462.mp4?token=lC6VXlMx3L1yteR6ggrh1LdE46HboWryurdKPvAhX47W7F8iVpLabt8b74MpIcUcUjJaKwf3Bd3X5WITjJ3aKaqZAunsK6LfwwdSUSQlWsSyj8haOvaQmxhiPhWPMRJTka8OxzMxUx7nMfuW7hrDXWA-S7mmJqeFXeiQpYuv5DuDzqvGwOg07sJQfDn-bXVlfrBOJq0Aj2oBWF8k7kfBHGx-el0JyVylf-gPGfqa2a0-8wb38Duy3sIP8_3fybhKCwrexj22OkZjXB9fTNl-44xS_BnlWdhm1ZUzHCBPYv2uvvfYK0G-TBrRvOO5IoEkrV9sE_-h51tyg9XRD-Xlkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع عده‌ای در فرودگاه مهرآباد و شعار علیه پزشکیان و عراقچی
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72323" target="_blank">📅 20:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72322">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=iR1id6LYv3OtSCY5HHsedNMWhu95V6mxGas1Gl-cvbRM8JAac1nVW6hy049d30Swsc4Pl3xi8CEubzVSRSK4Csmn1MU2dPjR9a5S4BLn-dARX49gvkooTnedzoAv3C95CqhwMUu1wkQYGyOIAjJ_VFYjoJtmbdjMghJerqGj7gCGWS9Ua_lkgYZzBQPfvhijUfcC-2xhODuHUcxaeE9JfWzoLfOGDpy619OG3DDbl_FoDZGf3JjsKNriV3XhM43ArlQ6E5WwGRZ4qth49Ir95UczMKznfE3QZFYo8qeZ6IrejRSq89Qh0_Rz4ndmVrx_BlcZEaFpLQG56lUFREFtCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=iR1id6LYv3OtSCY5HHsedNMWhu95V6mxGas1Gl-cvbRM8JAac1nVW6hy049d30Swsc4Pl3xi8CEubzVSRSK4Csmn1MU2dPjR9a5S4BLn-dARX49gvkooTnedzoAv3C95CqhwMUu1wkQYGyOIAjJ_VFYjoJtmbdjMghJerqGj7gCGWS9Ua_lkgYZzBQPfvhijUfcC-2xhODuHUcxaeE9JfWzoLfOGDpy619OG3DDbl_FoDZGf3JjsKNriV3XhM43ArlQ6E5WwGRZ4qth49Ir95UczMKznfE3QZFYo8qeZ6IrejRSq89Qh0_Rz4ndmVrx_BlcZEaFpLQG56lUFREFtCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از پاسخ دادن به سوال خبرنگار درباره زمان آغاز جنگ خودداری کرد.
خبرنگار:
آیا پس از انتخابات میان‌دوره‌ای به ایران حمله خواهید کرد؟
ترامپ:
من توافق آن‌ها را رد می‌کنم. آن‌ها می‌خواهند توافقی کنند که در آن بلافاصله تنگه را باز کنند، چون دارند به‌شدت متحمل شکست می‌شوند.
آن‌ها خواهان توافق هستند و به نظر من این اشکالی ندارد. من هم از توافق کردن استقبال می‌کنم، اما آن توافق [مدنظر آن‌ها] قابل‌قبول نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72322" target="_blank">📅 19:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72321">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPxHRaYZzQqAT0aqHEDDPfl7F_k5pWORMI3Nc0pJBWR8-7wAcjq2gtQUAvuILbofSq7Z56vUjLOHGVZNd0-A079rpsFgRku2OsEbUuR9-G7YdwOHFeQRaJKqiA7Qu-kHq-TuC_ciVOYYFbOZod_2-ZYu3WNzCSdnBRO31KSaYBs8AO9RuHLQOjrAiDECyr3fHIfvvgQfnV91jWLvw5s0TIut0XSr5lZgmz5jnpSZksMNRSWkQoy3_Tb9Sq_BEsXLJmo0nHowhXg_eGoIZC43U1yu1c5zNxnnhdk7chJ1BiacXgY2iwCfN0q8MoqwQ8UksPtYHHnRQa2zFNV4pdD5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای ترابری نظامی آمریکایی(C-40 Clipper) که بر پایه Boeing 737-700C ساخته شده و عمدتاً در اختیار نیروی دریایی آمریکا (US Navy) است در بحرین فرود آمد. مأموریت اصلی آن جابه‌جایی پرسنل و محموله‌های لجستیکی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72321" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72320">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ما کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز عبور می‌کند؛ همین دیشب، ۲۹ کشتی از آنجا عبور کردند.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72320" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72319">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=QF0f9F07RjNMgFH19NEeUkn0mbhrg74Ip9Ori10d6Esda8kZNHx__XNWpYkJtKyJ-b9OTzZfhC0_IdNNxR86tiUsJFyrT88lhBZWl8nGqexgq1OeVBydTshXCAdVKkW48ZyJ8ozXHnFtLEH2GqHmfLAvEqsDS0BFxCIiK_akuLJhmtsY3eu22tckfEQ-l9WjpL4otV403aWGZdA8rhK-2VyFCWBGVTrphvMeWYbQFW5DZbhw9GHn6EAa6rkuChS_dxMoj0rtM5JkcCizOpRhVmC02jZmhwZzhSmMvAk4oVH4MrWM6sRDF7ltVHpulsYyLke3sH-ZsSwyty6YH8I4kw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=QF0f9F07RjNMgFH19NEeUkn0mbhrg74Ip9Ori10d6Esda8kZNHx__XNWpYkJtKyJ-b9OTzZfhC0_IdNNxR86tiUsJFyrT88lhBZWl8nGqexgq1OeVBydTshXCAdVKkW48ZyJ8ozXHnFtLEH2GqHmfLAvEqsDS0BFxCIiK_akuLJhmtsY3eu22tckfEQ-l9WjpL4otV403aWGZdA8rhK-2VyFCWBGVTrphvMeWYbQFW5DZbhw9GHn6EAa6rkuChS_dxMoj0rtM5JkcCizOpRhVmC02jZmhwZzhSmMvAk4oVH4MrWM6sRDF7ltVHpulsYyLke3sH-ZsSwyty6YH8I4kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانوی گاثی که دریک براش هاپ هاپ کرد:
غذای مورد علاقه‌ام کباب کوبیده‌اس! بابای من ایرانیه و عاشق انواع کبابم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72319" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72318">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72318" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72318" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72317">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfeWJJA8P7bLWRv29y_gQqKkTuCZFxzslAum3HWbWNRGjcw8UEYbCdN3u-X-M7Oo0uP3v7sRpa9H1f-_QFcgYFaQVEbT_z6WhUPS9l6_z3kmICwirqhJshvo09yEcQ90m4695h1XCIZCbhV0MP33uBlf7FWHzPiKbyPJEayVQKc6hJYM0x3L_BUo05EPZeYo5xIdFYJ_hXhahOjorqQ-4WTlEK9eIGKvleZ0GgBC50kF_R7ic9pVgSGfOOoxaGsnO3-OPbwdMV9JVFaCDTGMq1wmbSsdf1hNVnmjF4ADYvW_FkZVcqt5hiSbA6OXWlprH3ADBnU2xl4GVOOBhINaXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72317" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72316">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=S3czu10lfy9GzVw16K6ydlQZXUmE3SN8tHmJ_6Yncm8UoOXR4jsQPvwWsMAOWz0QdRJGv10ZPUgr0YdWWJrHL7iKMDviJOZecYneklvVhx3P7tVlobyFJxJx3PgszmIbcbvycRpzU9kStCrDYQJ9-Lagkw0hbdKUzw0fSqP2BW0_BJB2VO-Mqb_QsEIdRZgGdSiel84BOAzsK_SGbxxpejRDEFSWH-Y-vKpIkwI9B0PkhTmgNt3I6-BXmr_d2ANoZmeP5V-TP5Tv_zhFRbFl0gIsqv2fQKjkfy1vnizrMvE4upafsy9a_T0EElNYRPDPDkc6z-tqLIXUW7m6l3MxZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=S3czu10lfy9GzVw16K6ydlQZXUmE3SN8tHmJ_6Yncm8UoOXR4jsQPvwWsMAOWz0QdRJGv10ZPUgr0YdWWJrHL7iKMDviJOZecYneklvVhx3P7tVlobyFJxJx3PgszmIbcbvycRpzU9kStCrDYQJ9-Lagkw0hbdKUzw0fSqP2BW0_BJB2VO-Mqb_QsEIdRZgGdSiel84BOAzsK_SGbxxpejRDEFSWH-Y-vKpIkwI9B0PkhTmgNt3I6-BXmr_d2ANoZmeP5V-TP5Tv_zhFRbFl0gIsqv2fQKjkfy1vnizrMvE4upafsy9a_T0EElNYRPDPDkc6z-tqLIXUW7m6l3MxZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
بعید میدونم مجتبی خامنه‌ای بیاد بیرون؛ بنظرم مجتبی خامنه‌ای تنها رهبریه که توی تونل رهبر شده،
توی تونل رهبریشو طی میکنه
و توی تونل رهبریش به پایان میرسه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72316" target="_blank">📅 18:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72315">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9475808af6.mp4?token=HWEw7sn3Ie43Df9jaR3fLtu881zyPBOMu7zxY29_8yfM8rymnpyqX2e0fPyrEeADfFWBtcgsvqNLdEyOwyXXRHwsfXhJzOLr08RUiN0cqJjOa2uQqM84rLuDr9aX2HrswFPYWuygKb5d00W6nSmiqrTc6HcMbhOSDN811wm7HRgMpn5y5yEOzIKlMTZAFcfgsXtlk-jeSJNYLT77GFb9iZpkiJqKu0Z-DdYPoZa6Bi4-LWV9KgFvMDeMFMteMK6nM4UdMqeQwRfOsYO3aRzfu5qW68gsbfSxSGFFrthtGCKc35RYW6jjzS52kzn8acgwF40xUfRCpJPC5Kv8bBhC-lzww_Hd3BWPqBw0hscdUAnQCB4xCF_CdekjI0HdihkohkyUCQH2n_WqTtUbvxByOGwO4uyhfu-XX37zNqLcXLq9D6ltppvV9I0DS6AAAOoQjsabPeEyNd_p7zEx0EDMPlInS-cx4V2Jsncy5TS7oF17LseZuB-VnDVF9FiePCzGnF0PwJ1FeX-xxpqCl2gLhbuXrz0pw0ExY0cu15TmG-CZDYHOlKKGpbwKM_fXSsrHpv6CC6WoLL86B4Xl43yV2dmTvT7ZYa_14U2DEbGwNfjKsDzMFnxjXsRAXetAhVCW4he7hx9dxXBJOCU5geypow76XjYDOO76hN7Ya30DDks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9475808af6.mp4?token=HWEw7sn3Ie43Df9jaR3fLtu881zyPBOMu7zxY29_8yfM8rymnpyqX2e0fPyrEeADfFWBtcgsvqNLdEyOwyXXRHwsfXhJzOLr08RUiN0cqJjOa2uQqM84rLuDr9aX2HrswFPYWuygKb5d00W6nSmiqrTc6HcMbhOSDN811wm7HRgMpn5y5yEOzIKlMTZAFcfgsXtlk-jeSJNYLT77GFb9iZpkiJqKu0Z-DdYPoZa6Bi4-LWV9KgFvMDeMFMteMK6nM4UdMqeQwRfOsYO3aRzfu5qW68gsbfSxSGFFrthtGCKc35RYW6jjzS52kzn8acgwF40xUfRCpJPC5Kv8bBhC-lzww_Hd3BWPqBw0hscdUAnQCB4xCF_CdekjI0HdihkohkyUCQH2n_WqTtUbvxByOGwO4uyhfu-XX37zNqLcXLq9D6ltppvV9I0DS6AAAOoQjsabPeEyNd_p7zEx0EDMPlInS-cx4V2Jsncy5TS7oF17LseZuB-VnDVF9FiePCzGnF0PwJ1FeX-xxpqCl2gLhbuXrz0pw0ExY0cu15TmG-CZDYHOlKKGpbwKM_fXSsrHpv6CC6WoLL86B4Xl43yV2dmTvT7ZYa_14U2DEbGwNfjKsDzMFnxjXsRAXetAhVCW4he7hx9dxXBJOCU5geypow76XjYDOO76hN7Ya30DDks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
کاری که آن‌ها می‌خواهند انجام دهند، باز کردن فوری تنگه هرمز است. می‌دانید چرا؟ چون دارند از پا درمی‌آیند. می‌دانید چرا دارند از پا درمی‌آیند؟ چون هیچ پولی عایدشان نمی‌شود.
آن‌ها درآمدشان را از طریق تنگه هرمز به دست می‌آورند؛ بنابراین با این کار، عملاً علیه منافع خودشان عمل کردند.
آن‌ها گفتند: «بیایید تنگه را ببندیم و برای دنیا مشکل ایجاد کنیم.» اما من وارد عمل شدم و ما بزرگ‌ترین محاصره تاریخ نظامی را برقرار کردیم؛ یک دیوار فولادی.
و حالا چه شده؟ آن‌ها دیگر پولی ندارند، چون می‌خواستند تنگه را ببندند.
و من گفتم: «بسیار خب. ما آن را به روی شما می‌بندیم، اما بقیه می‌توانند از آن استفاده کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72315" target="_blank">📅 17:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72314">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6488dcc10a.mp4?token=EJV5-w6c7DdSxzPSsT0H5tBnBTBieP2UjN7sPYCSqm62GkrtRP2-MBjdzFKioUnLaDHu5N8Bxp-ijV1SxJRCo77gwgaoQYawgEA4eYTbKTjA5XlVXlMzZJvYiXLzGqHGBqQT3aHcnU10IEhD2jDshBoHSP7HVz4eVKyOlOkCTnPfuNhvIyNf9sVAoMB1_F2ZoqtakQIO-pE3TpRV8WyYjNNQf855AVCEUkEcBQGNtaoccnbDL3iTVpPA4rVQY9u-y110U_dZWPtx1A2ZeBAvIGO6DMMCerkh9cu8kqaVr6FgBdhsG-NqLcGyyKKe2VTTXAFoGpmNtP0Wn_O3zh8FpyhQs3tSDa-xuujhOuvhm2JpUbACabpNu1G1vm6VzPHD0zq18IeyxtzZTqsfbgHZQLBMemoKzAN-9uza-miFGkUnSiBcFqggpWnqK4xt0UYYFDT5vP5JRHypESYjUvrBI_khwDE6k7EfjAXlwDGM5mNTtwx4TdgmerOVhWt2LCmrdt7k7jS88_SHWl24UC47Uw6BnDludPydpRP7fmYEUIZa44wXOQF9cRt1uZ-siWnbBQPW9yebK_hBiNRUJA3tSwrZrqybffE4rOvkzOy2YyTSikqAq1_BP0ACeOfPUGIJYvwrDYEUlvDmxmxamLkshUCrbhZN3mqON0r16ELk9C8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6488dcc10a.mp4?token=EJV5-w6c7DdSxzPSsT0H5tBnBTBieP2UjN7sPYCSqm62GkrtRP2-MBjdzFKioUnLaDHu5N8Bxp-ijV1SxJRCo77gwgaoQYawgEA4eYTbKTjA5XlVXlMzZJvYiXLzGqHGBqQT3aHcnU10IEhD2jDshBoHSP7HVz4eVKyOlOkCTnPfuNhvIyNf9sVAoMB1_F2ZoqtakQIO-pE3TpRV8WyYjNNQf855AVCEUkEcBQGNtaoccnbDL3iTVpPA4rVQY9u-y110U_dZWPtx1A2ZeBAvIGO6DMMCerkh9cu8kqaVr6FgBdhsG-NqLcGyyKKe2VTTXAFoGpmNtP0Wn_O3zh8FpyhQs3tSDa-xuujhOuvhm2JpUbACabpNu1G1vm6VzPHD0zq18IeyxtzZTqsfbgHZQLBMemoKzAN-9uza-miFGkUnSiBcFqggpWnqK4xt0UYYFDT5vP5JRHypESYjUvrBI_khwDE6k7EfjAXlwDGM5mNTtwx4TdgmerOVhWt2LCmrdt7k7jS88_SHWl24UC47Uw6BnDludPydpRP7fmYEUIZa44wXOQF9cRt1uZ-siWnbBQPW9yebK_hBiNRUJA3tSwrZrqybffE4rOvkzOy2YyTSikqAq1_BP0ACeOfPUGIJYvwrDYEUlvDmxmxamLkshUCrbhZN3mqON0r16ELk9C8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
من توافق آن‌ها را رد می‌کنم. آن‌ها می‌خواهند توافقی کنند که طی آن فوراً تنگه هرمز را باز کنند، چون دارند به‌شدت متحمل شکست می‌شوند.
می‌دانید، شما این موضوع را در «اخبار جعلی» نمی‌خوانید یا نمی‌بینید؛ اما ما داریم با قدرت تمام پیروز می‌شویم.
ما کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز عبور می‌کند؛ همین دیشب، ۲۹ کشتی از آنجا عبور کردند.
آن‌ها خواهان توافق هستند و به نظر من این اشکالی ندارد. من هم از توافق کردن استقبال می‌کنم، اما آن توافق [مدنظر آن‌ها] قابل‌قبول نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72314" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72313">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5297b02f7.mp4?token=vMmvKwmvJz8D5QbcEur8DxT7ogGkiPyXUupPF1_T62mphlane3u5VOod37mg23XOeCCn-nRPBndYECB_POUAH1HOus1o-EAWmUnJOwMCDErVwqgnObHCTTwRfBMstOfeoxL9No05DyCw8xlqeESw0ZfKqT1uLxvrt0AWkNKuDJFdSW1pzCyzFeitUn6mRqsHhZrHG6848-g1jB5oxinSfk30UMhp8djnAIDGdMsk3ORL0bFNGawn7x33-pd9Ugej7YOUOVwA10jfNjGCsVymekIPSv80LAgQboqOm1F_VozI16xXY7nBOwNnqtYNfZRKQNe56gChBgt7MEhmlnwvLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5297b02f7.mp4?token=vMmvKwmvJz8D5QbcEur8DxT7ogGkiPyXUupPF1_T62mphlane3u5VOod37mg23XOeCCn-nRPBndYECB_POUAH1HOus1o-EAWmUnJOwMCDErVwqgnObHCTTwRfBMstOfeoxL9No05DyCw8xlqeESw0ZfKqT1uLxvrt0AWkNKuDJFdSW1pzCyzFeitUn6mRqsHhZrHG6848-g1jB5oxinSfk30UMhp8djnAIDGdMsk3ORL0bFNGawn7x33-pd9Ugej7YOUOVwA10jfNjGCsVymekIPSv80LAgQboqOm1F_VozI16xXY7nBOwNnqtYNfZRKQNe56gChBgt7MEhmlnwvLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره طرح هفت ماده ای ارائه شده توسط ایران:
آن‌ها پیشنهادی ارائه کردند، اما من آن را رد کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72313" target="_blank">📅 17:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72312">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_8crLo4gMSyg6IFZ0ELSprl9jZxy13yT_Ud3WCtEeD4iCyy65ov48MUO4gGK4VxuRSczh-D6rMlxh1-frsWjqo5LQjK-Ulzg_C-kTjfWqRNMHy-k98J4oaoMDsUBdn618dgOurMbMpO0KhWWdM8DC_vOvFVeZJNmxX8ZXLobx9tOUCYK5Zp8lqZKUeidTEVntb2ewToSuzR7rxtYCPZO7b4IgtGrTYlxHyLIKfR8VmEFXCzNbN105kExFqgYiK2rU8khfRHsnlNZH-7DYEbNfFXDMavMeNle5Bt0Og8jXihmSHaiSoO_KSeLZoGz6FmjGGXRmt0n962xoAxkl3eYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران نمی‌تواند سلاح هسته‌ای داشته باشد!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72312" target="_blank">📅 17:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72311">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b70e110ec.mp4?token=h3tPnT1eHAbdSKspPXbwSR19RBA7idwBs2a1OPEzrNTMLDDqeS54myWCj9dcsqV6Of79BqBy3brhXVjqxANhpXIvy3W0GlRN9ZQMDb63M6Xn4bVKRKDDm9TLMBzZItiNE7UGnk7tIDWznMb7Sr7ugiyfko3ysRRH_TcR2AQJ3wgEl4bufKb9plH34BcX-tnUKiMMlo4msJ5EyliYOOucpctHy2HjJ_WJkTCVE7dUDatWKjsHBeMLWdhV38vJkIYXWGqL7kxKYkbROPl07XAHzPLBpmmD5QrcbZxMifBfxzKTowsPKHC_yxlDLwvCzqLIgCDCER8UEO7VQ8_4ji-v4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b70e110ec.mp4?token=h3tPnT1eHAbdSKspPXbwSR19RBA7idwBs2a1OPEzrNTMLDDqeS54myWCj9dcsqV6Of79BqBy3brhXVjqxANhpXIvy3W0GlRN9ZQMDb63M6Xn4bVKRKDDm9TLMBzZItiNE7UGnk7tIDWznMb7Sr7ugiyfko3ysRRH_TcR2AQJ3wgEl4bufKb9plH34BcX-tnUKiMMlo4msJ5EyliYOOucpctHy2HjJ_WJkTCVE7dUDatWKjsHBeMLWdhV38vJkIYXWGqL7kxKYkbROPl07XAHzPLBpmmD5QrcbZxMifBfxzKTowsPKHC_yxlDLwvCzqLIgCDCER8UEO7VQ8_4ji-v4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عرزشی داره فخر میفروشه نسبت به بنزین مفتی که میگیره در حالی که بقیه مردم ایران و دنیا باید گرون تر بخرن
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72311" target="_blank">📅 17:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72310">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204024e85e.mp4?token=SYd_yGQtXzAYOBk03U05K8eRUGS41fDIb2M8-skBs13d8CWThni7uH0WPiHsrAzSOSd0nMXyoFpqqoRgvfW5KdqGWJ1GDcz87BI6niAOh8p6wJx4zteqHcwiEZ-OMHl0xYJsgQUy3ukfZQmyqqsvhklmPd7cdIfc8x4FqdmBMoL_8K0X7ZAvQST0tXjdrL3WoI3rRS5wUusplHPTu_TTKRrOXzIM6q1K9MXODazv6bw3Wnu1ut_lIxO_dtE8E1NobSXrEgPP3h7GlFYu1_0mGLC2OdhtbUq4JGNDsiMMl3bqD5wjMN3TgSLoV3VgiTujFcKsY2XCyDHMQA14pjeDvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204024e85e.mp4?token=SYd_yGQtXzAYOBk03U05K8eRUGS41fDIb2M8-skBs13d8CWThni7uH0WPiHsrAzSOSd0nMXyoFpqqoRgvfW5KdqGWJ1GDcz87BI6niAOh8p6wJx4zteqHcwiEZ-OMHl0xYJsgQUy3ukfZQmyqqsvhklmPd7cdIfc8x4FqdmBMoL_8K0X7ZAvQST0tXjdrL3WoI3rRS5wUusplHPTu_TTKRrOXzIM6q1K9MXODazv6bw3Wnu1ut_lIxO_dtE8E1NobSXrEgPP3h7GlFYu1_0mGLC2OdhtbUq4JGNDsiMMl3bqD5wjMN3TgSLoV3VgiTujFcKsY2XCyDHMQA14pjeDvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه تعداد هم وطن به مناسبت شروع سال تحصیلی لوازم تحریر جدید گرفتن پخش کردن بین بچه های محلشون
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72310" target="_blank">📅 16:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72309">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11382bd536.mp4?token=V0aXkOnhtU9sjglKbpPEN2XL-l1nd93dyHH6W_zX31PTuzPjVdEUbk6x0KRPmr94bPp-xcen8qVETTSlgNN3qsp6Mer-T0dyfm04a9yLEnlwWpgGhL7OezvHXUbkI47bD5PQygOa-DQhKyZnX9iHxRlKFOmWKB6niaI8hH-fXFueb0X7hurpSWhAJtyfy2nh9otcIFxuj95Re_oQ2bTQi32fEelzV4_XYMfcuebQXXQqYUYX55muJKmxFmFFyjyvu6ErMdj0AkqqYkfTyweRrdk7AvQIfro-tLM0l6deihchNDWyZ8Pck34FoXwp5cI_PbzF28FXD4Fupt8q0HFwbgTBhcgoko2l-EzZgEUPjNk6SfnK6Qee5xlnVhbwW0hNgx0YWhwrbT2_wu27hfzJqzUaY6qIMgJrn7B_L5XaonON_eSuQTz1QGyzTyru7Qdrfh8iJ47yInOzPGuCC4by3uyN0wJQhWiJKgbzdn4KMkic22KHXnktEnttk1P7ztUHsc9gtjoy0HrBx4Nl9EaxAJmOABk4o2P0RQJucElSXIHIEMj9fueVV0rUp7rvb4DMbF3sazfFBU4cRNiRsqjLpMCnU1Np-25O_9wJOoTmjLjkfD0M-ZCj18rVe4YWRrCNj_QNBF0Ya9414iIlXGDD4H6OM9lz1JGbveeXaIRPh70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11382bd536.mp4?token=V0aXkOnhtU9sjglKbpPEN2XL-l1nd93dyHH6W_zX31PTuzPjVdEUbk6x0KRPmr94bPp-xcen8qVETTSlgNN3qsp6Mer-T0dyfm04a9yLEnlwWpgGhL7OezvHXUbkI47bD5PQygOa-DQhKyZnX9iHxRlKFOmWKB6niaI8hH-fXFueb0X7hurpSWhAJtyfy2nh9otcIFxuj95Re_oQ2bTQi32fEelzV4_XYMfcuebQXXQqYUYX55muJKmxFmFFyjyvu6ErMdj0AkqqYkfTyweRrdk7AvQIfro-tLM0l6deihchNDWyZ8Pck34FoXwp5cI_PbzF28FXD4Fupt8q0HFwbgTBhcgoko2l-EzZgEUPjNk6SfnK6Qee5xlnVhbwW0hNgx0YWhwrbT2_wu27hfzJqzUaY6qIMgJrn7B_L5XaonON_eSuQTz1QGyzTyru7Qdrfh8iJ47yInOzPGuCC4by3uyN0wJQhWiJKgbzdn4KMkic22KHXnktEnttk1P7ztUHsc9gtjoy0HrBx4Nl9EaxAJmOABk4o2P0RQJucElSXIHIEMj9fueVV0rUp7rvb4DMbF3sazfFBU4cRNiRsqjLpMCnU1Np-25O_9wJOoTmjLjkfD0M-ZCj18rVe4YWRrCNj_QNBF0Ya9414iIlXGDD4H6OM9lz1JGbveeXaIRPh70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقایسه ارزش برگ‌های اسکناس با یک برگ دستمال‌کاغذیِ دورانداختنی
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72309" target="_blank">📅 16:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72308">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=GZeXrgZ84m4TeWTvU-sYPHja0xy_JN6C0ifGQSIgIlePEw2VI42Xeu-3rTgrOB5W9VcgA70XKaFszRzCd59uatI8CmbELlV4JNpA6sqy5n2MNAL11sSPPvgxhZ3XyHq94Ca0ouoCXi_UZoWRqeUOQNTHdsDvcomMRPd4jzrv0ckMzE_Ir3UNkefLjGCRY07EYnjO10gjSlsu_QdYziIGgzQOWnhu_4VU4HDxQUUe38sL2FqQQZdnD0Ws1YplHCEG3y66oynYbVj9hOdx2rowHNiCXCDkoK6BrVDxhKERHafg65ew6_2IcMlwXCrwugPkTxGX3G6YDjFWJYiLUDFp8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=GZeXrgZ84m4TeWTvU-sYPHja0xy_JN6C0ifGQSIgIlePEw2VI42Xeu-3rTgrOB5W9VcgA70XKaFszRzCd59uatI8CmbELlV4JNpA6sqy5n2MNAL11sSPPvgxhZ3XyHq94Ca0ouoCXi_UZoWRqeUOQNTHdsDvcomMRPd4jzrv0ckMzE_Ir3UNkefLjGCRY07EYnjO10gjSlsu_QdYziIGgzQOWnhu_4VU4HDxQUUe38sL2FqQQZdnD0Ws1YplHCEG3y66oynYbVj9hOdx2rowHNiCXCDkoK6BrVDxhKERHafg65ew6_2IcMlwXCrwugPkTxGX3G6YDjFWJYiLUDFp8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضخامت رنگ کوییک اسباب بازی از تولیدی کارخونه بیشتره !
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72308" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72306">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Mdyie2iJikJRJJOhOhGKWMtme9Cey-G-eyT-8sgirCWQhIB_B4de9AJ4C-Abkakgj56YiJL30Zk48Wjwtt9sthKc8V5pSSXzy_-S5-jMTYmqqY2kTh69sPONpIxWV3IdEIe-hbBhtYZUIWA3YtczjuLrmd2j4IdH79js1VR8htgIR8bRNSuc9ivYnW8hua0OqdmOsqZ-NlY4WRnZsZIk66Qnb7Ls8p4cSvYADtDLPwOHzUlPkgb6cHWdc61PiZPuTSPTM0rx993YX9EIgEjyR7uoPMigwkblQWMo_jGih8oh5zXnMn_ed_CFdvPhZPZwrq_d1gUtBFwQbfSV0aEO7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=qpuIlAVdaHnc3HvnDH7ZzQIePFGIPPfRwd39_InOUspLL25hecMeN0byLVa8M_5wwPeFr-9TOmiaUoMxPmQhB9cfayrMPjhKVsQ-7mKKE1e8XH5T1IQoNd8-fmE1GH0bcTU_q2wd2S_qR6kOXM9Juw41g4OE3gEH1eOuZipr3gyLGpiDEoUfNbhnJklAeE4I136rbgVvwFZfcwiu35gsvZccDJiwG7B3_tpWiRaHU9PbstrZoEKYUqRGarL73tg18DjiV7-xZuYnLie5-BJBONY8Wi_S5s7yEVhYYDkI_08b_F9inp6gezM0a3WgSVwsgqNMhpAiXBx34n-6LcoG0w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=qpuIlAVdaHnc3HvnDH7ZzQIePFGIPPfRwd39_InOUspLL25hecMeN0byLVa8M_5wwPeFr-9TOmiaUoMxPmQhB9cfayrMPjhKVsQ-7mKKE1e8XH5T1IQoNd8-fmE1GH0bcTU_q2wd2S_qR6kOXM9Juw41g4OE3gEH1eOuZipr3gyLGpiDEoUfNbhnJklAeE4I136rbgVvwFZfcwiu35gsvZccDJiwG7B3_tpWiRaHU9PbstrZoEKYUqRGarL73tg18DjiV7-xZuYnLie5-BJBONY8Wi_S5s7yEVhYYDkI_08b_F9inp6gezM0a3WgSVwsgqNMhpAiXBx34n-6LcoG0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72306" target="_blank">📅 14:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72305">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اثر جدید ابی به یاد جان‌باختگان ۱۸ و ۱۹ دی
از او بگو به دنیا..
از او که قصه ای داشت او جشنِ زندگی بود..
سروی که قد برافراشت از اُجرتِ گلوله ..
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72305" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72304">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=RXqtdsksXywEmgR1PRK3nCNnTtuUMJ5fEdadSFOxE1C52xLQp7ylzTPpGZKJrKQoYFn6zgiVtPvCdPAYjf5C86pS2oVP61mwjUdcGtTUUIwcDblWDeqJoWZyfBkBkeiTyaCVwD45OcSfzdlzVFSbiTTpcot3Mv6Q8ZDlzKTAKAmxSmhgoRctqbwh1TdDqPAtQNLbbvgeYCZ9YcKKO6SQh7_Y6MK74y_kVgDgRiHkm8nQ3Wu623HOluvT8fpTLm5r5vfIj8KwB_k35uUVbgtT6uNRnfcG85aCMuTbTH2WQdkpgjYbVV2NzDNYg3TaHkPdew-6Fo20Q-9dE2br2_Ys2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=RXqtdsksXywEmgR1PRK3nCNnTtuUMJ5fEdadSFOxE1C52xLQp7ylzTPpGZKJrKQoYFn6zgiVtPvCdPAYjf5C86pS2oVP61mwjUdcGtTUUIwcDblWDeqJoWZyfBkBkeiTyaCVwD45OcSfzdlzVFSbiTTpcot3Mv6Q8ZDlzKTAKAmxSmhgoRctqbwh1TdDqPAtQNLbbvgeYCZ9YcKKO6SQh7_Y6MK74y_kVgDgRiHkm8nQ3Wu623HOluvT8fpTLm5r5vfIj8KwB_k35uUVbgtT6uNRnfcG85aCMuTbTH2WQdkpgjYbVV2NzDNYg3TaHkPdew-6Fo20Q-9dE2br2_Ys2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ در پلتفرم ایکس منتشر کرده:
در این ویدیو تصاویری از انهدام یک لانچر سپاه دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72304" target="_blank">📅 13:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72303">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش های تایید نشده از انفجار در نزدیکی جزیره خارگ/همچنین صدای انفجارهایی از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72303" target="_blank">📅 13:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72302">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc192b406.mp4?token=iRHvLMVc6WpyObEmIeFJ-vbUUCeeOfp3PqBxEIKXRQ96w0eRvUolLZKcNFhxwmHBPXL1QrfaaV87bxW4yNOsliF9xvogPryUphpS1NkRAD82alJ5Vl5YxckudbMz_7rZBu8tU2c2a4_7u6o3udFTcbYPnacUu3AOqat3UiJbmmgGHMuCacA5bSwEATvyzd3dB6uk3vmKmclVOgHNWkc2gTGu2kZmMbLX2uh-vl5qVlG65k9ZwrMpzptkPhCdAOh_NTQh3NCvyEj_NgjL6lqv8uCkYRu-W6poFG9ty--5SCNUbLh6Onx1ihST3SSFt7XZas0trIX2Pbm1ITO_57hccA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc192b406.mp4?token=iRHvLMVc6WpyObEmIeFJ-vbUUCeeOfp3PqBxEIKXRQ96w0eRvUolLZKcNFhxwmHBPXL1QrfaaV87bxW4yNOsliF9xvogPryUphpS1NkRAD82alJ5Vl5YxckudbMz_7rZBu8tU2c2a4_7u6o3udFTcbYPnacUu3AOqat3UiJbmmgGHMuCacA5bSwEATvyzd3dB6uk3vmKmclVOgHNWkc2gTGu2kZmMbLX2uh-vl5qVlG65k9ZwrMpzptkPhCdAOh_NTQh3NCvyEj_NgjL6lqv8uCkYRu-W6poFG9ty--5SCNUbLh6Onx1ihST3SSFt7XZas0trIX2Pbm1ITO_57hccA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی خراتیان کارشناس صداوسیما از نامه ای محرمانه که چند روز بعد از اعتراضات ۱۸و۱۹ دی از طرف جمهوری اسلامی برای دونالد ترامپ فرستاده شد می‌گوید :
ما از طریق سوئیسی‌ها، حدود دو سه روز بعد از حوادث ۱۸ و ۱۹ دی، نامه‌ای محرمانه برای ترامپ فرستادیم.
نامه به تقریر رهبر شهید بود و فکر می‌کنم آقای پزشکیان هم آن را امضا کرده بود.
متن نامه چند محور داشت و لحن آن بسیار جدی بود. در این نامه به ترامپ هشدار داده شده بود که اگر جنگ را آغاز کند، شرایط مثل گذشته نخواهد بود و ایران درخواست آتش‌بس را نخواهد پذیرفت.
تأکید شده بود که جنگ را به منطقه خواهیم کشاند، به پایگاه‌های آمریکا حملات بی‌سابقه خواهیم کرد، به نفت رحم نخواهیم کرد، مسیرهای انرژی را خواهیم بست و چه جنگ باشد و چه نباشد، به اسرائیل حمله خواهیم کرد.
رهبر شهید نیز در یکی از آخرین سخنرانی‌هایش تأکید کرده بود که این جنگ قطعاً به یک جنگ منطقه‌ای تبدیل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72302" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72301">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/72301" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72300">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tm65YCIb7FAqsGNJVxS-zyRCv7dmPnWvg91u57IuCblNc3I3n0jhPuu2HX8oWIvwvkg69o6dR6Hv52TA1k7YM4klQpWubcEIv8hlhnAmXGCXPrq-DRQt-A5UJZ6-mVsYhbEV1iT-qTm05AWtbK58GSp2gBDPAJG8iNM3aJdXNwMZTxNXCSykJhizkiNYKPhsbV1I5VgKnbZv1K-47hLzaz-pNlctUVOq4FOktQtm7dkG6ooXhzZubxdYXs4GWLQkLP7Z4gMBoQgoIJf2Xn6noB0jrbdM3fZWI1dN8IFBzGbW1kZtFbENQqazp8xWRIQtBCO5T2uYJGaR-98h-dHiaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز اسپانیا
🆚
انگلیس را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
اسپانیا: ۵ برد و ۹ گل زده
انگلیس: ۴ برد، ۱ شکست و ۱۴ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72300" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72297">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/do0WHTcXjV2iuCiFbyR6In5wrYo_qDd12mNlJdNFqVJwxbl9a9LkwARDs9N4lQigHU8EKaBy3vv1Wy54bwgfRKtWjENiFCNK1w50Txi8C5FYGv5ApdjM-qvep5kBs-svYPER5YymwHzfU1V0JsNwUl6oeaRjPrd3zzs3zDOAHts-pvIaHxKj4kDcFkiQ4w6R_kHdzmpKxuhumR97o2AJhesu97rONkV5PGJdL54kJOwqyqvrLrpGdmW1StgQBgj1ksvJEsJ18IQnHuSFVWsKv9lA_sWjaUQ84gbVuV1jZnsjjOh4RYFyut4daPu0NNFwzEoe3HRcIA1T8ete4B3JMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXRQDqjAEmaRE9JCjFhCttAOtkm-W5n0DGy3aF_YyPY47hrlRY-8e4EEdO9RiKdo_t2T3BGHlkJo1Wr4VO6WPVA1eiH4MDLDPCPTu7sBSLjtyAvty73GyNuKxvcuDHvETVHVX2Yc01nB7_5-CP1DV_STIvEoxlyqHwumrF5-g-7rt7JkuiUl1Ajd7p0X1Q24NQbmM9aE3Je2gvlfrKmVDhCurK9QFWcueH_kQgc9w3zRe_093Be4VqtmV-IlS-r9gbz4gCRLHmiSx39N71pggQ4sAdOQKJB-srksBuHzrHaO6TR4yiDc-nyniGBbeMAcZvBikx2GIHq51Fdx-zGB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/csg3HWhA5i-UUFv-o0iVfi-XW7RBQ40gP3KouwedzYl7QqahN7fWPS-8tsiwj082xgGKFfd8IMF5Pcht48UzANJ1ekzmz7fY4LV7U11zdaQgOMhmCTGVq23F4nUB2aSVeGtlaHFE2zwMH3AldGkhd2koIgpd2opkh3l5Jc14bYrn_7pfKsdT0ohs22tzB-C54qokxGHKP74x9jiG7FoKgk3OyheVEVuRRBERs-6n8r3v2lkeX81sVDBCQHU0lIPhEuQnro5p1abi0ARqReZd58OtonXgNuiTF2a-5Lbs12bqyl-NZI6dDIgPRVuafT98gIqYttyS1ZMfnIZWHSr56w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سیرک جان فدایان ادامه دارد
ترامپ توسط جان فدایان دستگیر شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72297" target="_blank">📅 12:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72296">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=etfQUUbScafSz66I8rWNWPb8Sf0maBWoHP8udWiXV4NleZ0vW6QhtSe8-FagUFKWX491S4cunMer9-nh3XjeMr40Bmiin_RD8mgyDHhRLytbvgh1KriSfmMDxedoqamm-GF5thk-R_IR-t4E2mPT0NZqtsl7Eg8t3Y7LMFBiwipGDd0-Lx_buGlyAPaWdaaJsr4kGHT7ABld1FKuzZrtZCsTmMRWshN3qHlBUTfcS0ZdwcEl2W9EroMwotRVv5rpolxVSJe503IvbUDgs2Nm8Xxo0h7HjDCSRLrR6JpXsulaVVoJWZlBJ-uF0P2Z7Nzm4dBEZLT4PfH5pnTFJqs8fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=etfQUUbScafSz66I8rWNWPb8Sf0maBWoHP8udWiXV4NleZ0vW6QhtSe8-FagUFKWX491S4cunMer9-nh3XjeMr40Bmiin_RD8mgyDHhRLytbvgh1KriSfmMDxedoqamm-GF5thk-R_IR-t4E2mPT0NZqtsl7Eg8t3Y7LMFBiwipGDd0-Lx_buGlyAPaWdaaJsr4kGHT7ABld1FKuzZrtZCsTmMRWshN3qHlBUTfcS0ZdwcEl2W9EroMwotRVv5rpolxVSJe503IvbUDgs2Nm8Xxo0h7HjDCSRLrR6JpXsulaVVoJWZlBJ-uF0P2Z7Nzm4dBEZLT4PfH5pnTFJqs8fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکر کارلسون گفت که پس از تلاش برای متقاعد کردن دونالد ترامپ جهت پرهیز از جنگ با ایران، او به وی چنین پاسخ داد:
«بله، حق با توست؛ اما در نهایت همه ما می‌میریم، پس [این موضوع] اهمیتی ندارد.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72296" target="_blank">📅 11:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72295">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=Gs6eoPAS7o_I9p-u4dZchVnBqP2EY_UEAf_BKe4ZWbYOtOGKzVWS49LXrOTMywnnQxM-C2-UsCKQzBWhaAFYbwOgdXuzu2UxA4X75xW28pKc-E5NRD1LDGtaj0gWOqzcq6gxTfB4wizl6d1PSk-AhVAAGAei5-M_VXafllBC2YVtskSvSc2ssPodXcEH-Cd3vRUz1KgIb2eAWguP6iyAZJEPtK7eGTJW9srMRFp547e8JupU5nBhmNaX_pPdWOJibRgHXD2-sVxdqekhofSvZAsk4ZsQDXsLSqlwF9AjfOMLXD1chfKfr0iqUho7WaSPJ66RozNhgu6SEnh5yAfW0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=Gs6eoPAS7o_I9p-u4dZchVnBqP2EY_UEAf_BKe4ZWbYOtOGKzVWS49LXrOTMywnnQxM-C2-UsCKQzBWhaAFYbwOgdXuzu2UxA4X75xW28pKc-E5NRD1LDGtaj0gWOqzcq6gxTfB4wizl6d1PSk-AhVAAGAei5-M_VXafllBC2YVtskSvSc2ssPodXcEH-Cd3vRUz1KgIb2eAWguP6iyAZJEPtK7eGTJW9srMRFp547e8JupU5nBhmNaX_pPdWOJibRgHXD2-sVxdqekhofSvZAsk4ZsQDXsLSqlwF9AjfOMLXD1chfKfr0iqUho7WaSPJ66RozNhgu6SEnh5yAfW0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان درباره مجتبی خامنه‌ای:
مجتبی خامنه‌ای هیچ‌گونه مشکل یا چالش جسمانی خاص و مداومی ندارد.
در آخرین دیداری که بیش از هفت ساعت طول کشید، البته ما عادت نداشتیم که آن‌قدر طولانی‌مدت در حالت نشسته بمانیم.
ما زاویه و وضعیت نشستن خود را تغییر می‌دادیم، پاها را روی هم می‌انداختیم و کارهایی از این قبیل؛ اما قطعاً او از سلامت کافی برخوردار بود که بتواند پس از آن ساعات طولانی در آن وضعیت، بایستد.
از منظر پزشکی، او کاملاً سالم است. این را از زبان من به عنوان یک پزشک بشنوید و بپذیرید: او هیچ مشکلی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72295" target="_blank">📅 11:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72294">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=na5mBjX82dRvmScgjT2CXwtlIUkIce3xmVdP5WfLzLqxyZaC_hbpkyMrrBr0gew4qI2XnB-46rKmEZVY3ItD4UnNHZewjOTumjUGBpbjJYzMEQwU58OpYcVCY1PZ8n7UsnkhcV02nsB055eCbGoBV0w3WrlmowmXbNl1j8eveUdQa3xnvOyMagPvQu1uCLVZ6rjHtlMe3_r3eGoWYPMoSZWnmmRHTeTgpXY4rnvYmmG7Yub5b3iK3safnz3AA_8oyTqkhOpHeKArJKzeLqpJMgYJp2YLrMhaXxD3WTxF9xquIXZIAsUyTzNtm8NK_mnav538SOJ7pzuUZdFPkDQUsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=na5mBjX82dRvmScgjT2CXwtlIUkIce3xmVdP5WfLzLqxyZaC_hbpkyMrrBr0gew4qI2XnB-46rKmEZVY3ItD4UnNHZewjOTumjUGBpbjJYzMEQwU58OpYcVCY1PZ8n7UsnkhcV02nsB055eCbGoBV0w3WrlmowmXbNl1j8eveUdQa3xnvOyMagPvQu1uCLVZ6rjHtlMe3_r3eGoWYPMoSZWnmmRHTeTgpXY4rnvYmmG7Yub5b3iK3safnz3AA_8oyTqkhOpHeKArJKzeLqpJMgYJp2YLrMhaXxD3WTxF9xquIXZIAsUyTzNtm8NK_mnav538SOJ7pzuUZdFPkDQUsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا ایران بعد از امضای تفاهم‌نامه با آمریکا سه کشتی را زد و تنگه هرمز را بست؟
اینجا احمدی‌مقدم در حال توضیح دادن یکی از دلایل آن است:
نود میلیون بشکه نفت‌مان از محاصره خارج شد اما خریداری نشد.
چون ناگهان نفت زیادی عرضه شده بود، مشتری‌ها با قیمت‌های پایین می‌خواستند بخرند.
با بسته شدن تنگه، همان را با قیمت بالا فروختیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72294" target="_blank">📅 10:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72293">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Llt3vgtF8Z9XVdd1zB5DelfLxQYZ8vdP4EvmeauC5JHZzZ2jO_q1E38K_yK5YQnPCiOJvbRpZa8_cApM3eninI17PuoohY-saWb5i2QTuhNIyt4mDuua0xP2M9mPkZAV9Em09n4L6Oe4gVkXJPtoqF7r3D9WwiRQkm7zPe32gU7pxweFJFN3x7BAIvN3uloXC4Kq1PI3bEZc5dvN8w9nlQJyXwaEZAVGz4ucnuqq5095WfvhI3LM91KABgbxBSHufxxVXuOJLQ1EaI3hNPbB_w7072Srf5-EE5_6EoHIUhIMCxWSbxOpK2TBJ8Ou9fw2F6kw5eK4vMHb1NC6jKpe7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وال‌استریت ژورنال:
به گفته مقامات آمریکایی، ترامپ پیشنهاد ایران برای برقراری آتش‌بس هفت‌روزه را رد کرده و اعلام داشته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران ایران از سر گرفته شود.
پیشنهاد ایران شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران و کاهش فشارهای اقتصادی از سوی آمریکا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72293" target="_blank">📅 10:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72292">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=USg466anCvObsuKq9LuberEPDthBBLxkiomf9Gb1hpraDgeW2btLTWIH8ffu9lgA2S5Wqc2VVMtLN6csv2ORzYITxMrj4HEDPqNoEpys4ce2j6lp5ZRmBsj7bmMrSNDLCA35gZWQ3ww88CpXADb4EJ9BdzeC0DRdUIEMqejAfkLdSORJLTLP4WB1heA3m2iTRpx664SGtebIBARkOCFViF3ZJsX1vAp7B7qEst_on95hwJqMO8qBg8SbhWfDVu0EIYtrnGPE9PetgJW6cd06slaBa7GubqmChBZwA1BPxzQMqL-RDUnfIymYy2kWC8Lj0uPuE-CAvBO1-EVhZ9DWJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=USg466anCvObsuKq9LuberEPDthBBLxkiomf9Gb1hpraDgeW2btLTWIH8ffu9lgA2S5Wqc2VVMtLN6csv2ORzYITxMrj4HEDPqNoEpys4ce2j6lp5ZRmBsj7bmMrSNDLCA35gZWQ3ww88CpXADb4EJ9BdzeC0DRdUIEMqejAfkLdSORJLTLP4WB1heA3m2iTRpx664SGtebIBARkOCFViF3ZJsX1vAp7B7qEst_on95hwJqMO8qBg8SbhWfDVu0EIYtrnGPE9PetgJW6cd06slaBa7GubqmChBZwA1BPxzQMqL-RDUnfIymYy2kWC8Lj0uPuE-CAvBO1-EVhZ9DWJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامبد جوان :
سانسورچی‌های صداوسیما واقعا مریض جنسی هستن
طوری که با سیبیل خانم تحریک میشدن. میگفتن سیبیل فلان مرد زنانه‌ست و تحریک کنندست.
یادمه توی یه سکانس یکی از بازیگرا میگفت «بیا بشین اینجا». میگفتن اگه یکی فقط صدا رو بشنوه ممکنه از «بشین اینجا» برداشت بدی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72292" target="_blank">📅 10:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72291">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=KWJ4FC37bF_cjey5fHwNdLZndy24hAsLZSQFQ67QiKs03whFl70xQoHYBIYX34J0t7gCqwWrZlR-L78ieaxLhKz_JwNWuPCYFHjvY5GK0nYiHkRobH0Ltz4k1-2tQG5tJ3tyS8EYoKqFln3MwYk8CDfCW5YhAD98G80i-rRWkeq4j1zfSeLJUUjLEC910KHLanC3gxI8shWXx-PpzG-cEYn2obURwjbOJ4qUhZ1ny9WCZD3__okCKHrENLCVFa-Afjre5VHcLYQY3q5pi9HxhYZmd8mERsKUbVZoAzADFpO4pOxElT0FLoZKhtAr567GrJ7jnSpoyRw626JzLDZt9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=KWJ4FC37bF_cjey5fHwNdLZndy24hAsLZSQFQ67QiKs03whFl70xQoHYBIYX34J0t7gCqwWrZlR-L78ieaxLhKz_JwNWuPCYFHjvY5GK0nYiHkRobH0Ltz4k1-2tQG5tJ3tyS8EYoKqFln3MwYk8CDfCW5YhAD98G80i-rRWkeq4j1zfSeLJUUjLEC910KHLanC3gxI8shWXx-PpzG-cEYn2obURwjbOJ4qUhZ1ny9WCZD3__okCKHrENLCVFa-Afjre5VHcLYQY3q5pi9HxhYZmd8mERsKUbVZoAzADFpO4pOxElT0FLoZKhtAr567GrJ7jnSpoyRw626JzLDZt9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72291" target="_blank">📅 09:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72290">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7db87608.mp4?token=RRT_gFft8Lui_NbAyz83gtbJo6CKsClsgFzcWx4dS8_D6I5J3E3CjYO-kzFedrs-ZSovs5U2qMk_JvsENXR9F51LTSRU5SvxMAkiICTzjowUDDBN-rEmz6zrKp24MndVoyUGnhX8jmGm_xntAFRapQ8a60eS0d0kUp7GQXi4z7nHAgS-btDOSGQQXbabaf53VuUTdxLLcpCxzITZdQiJA4l30da1-wYgX8UjbuyBxiFg2jBvsuPsawDk6j6ZI9csx08IWARF6XluIivfOS8DMkVr5zNB7KhYUkq8CjoBkRHpMltjjYqlFQSOsVufXC27otZk2opoSNjFIaVRlAUWkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7db87608.mp4?token=RRT_gFft8Lui_NbAyz83gtbJo6CKsClsgFzcWx4dS8_D6I5J3E3CjYO-kzFedrs-ZSovs5U2qMk_JvsENXR9F51LTSRU5SvxMAkiICTzjowUDDBN-rEmz6zrKp24MndVoyUGnhX8jmGm_xntAFRapQ8a60eS0d0kUp7GQXi4z7nHAgS-btDOSGQQXbabaf53VuUTdxLLcpCxzITZdQiJA4l30da1-wYgX8UjbuyBxiFg2jBvsuPsawDk6j6ZI9csx08IWARF6XluIivfOS8DMkVr5zNB7KhYUkq8CjoBkRHpMltjjYqlFQSOsVufXC27otZk2opoSNjFIaVRlAUWkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احسان کاظمیون فعال اینستاگرامی، یک هفته با یک پیج فیک دخترانه با پیمان اکبری، مجری سپاهی صداوسیما توی تله انداخته!
آخرش هم باهاش تماس تصویری می‌گیره و پیمان وقتی می‌بینه طرف پسره، خشکش می‌زنه
پیمان اکبری همون مجری حکومتی بود که بابت اعدام ها از اژه‌ای تشکر کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72290" target="_blank">📅 09:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72289">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72289" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72288">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fC7s359egyhjxCsRMumIc0Xs9CtvK_wO7ID0i4wIlCEOYid2SC3CU53PSEMRStemPaGnmQthAdtd4qAbNL90Y2cAZ48jgfazPCduluH0VCOp2uX4c0MQwAF9OQjplMXwJp6cY1S77Qub7923Yo3471hmxPDq3fpgyc50PeYi5nCdkJdbQ4u2Stsv_27mhtWVS0RrQQ9nJxa_35TJsvxJpNVdIGx6BIsbb7YUVMWqTNo840_cdpUfLVP0-G252DGbLIEqQVRROfMnM81FQaJp4u4jtHStrxG_PKzUzPUlpvQT1opaxXXha-ADXXdbG76H4AAPB56IKf_U0uMG1hGS0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72288" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72287">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/H0aBGdMVCfXgssVq5A5w2py0BIs4zfdCrr388k2Qymu2LZsYkJgQZ_K39K0zxXExpssdmQhLTYbLzA1lzYGl5E2lrIk34S2BTp85frv2Vc5lkh7hucF-f2TsUr0SMrvHk_rO7u6qLaK7hQgt26yZjL1AzSdsPFseTTvimRNxnj63_5ikJxgXAtlUQv6g50qjoGZ4TzivA1Iz3RX2mBO7RCvnRy0pG6LOcjL2uV2jnRQ_vf9BLGoogEzBk3Gdnx5COLDTnjWeCC3Hj0ipsdvYIhhn1IbuIzJKReHR1TTbHqFE7fhZTxvFbXTUKfgNM9PVYltnmY8dFjKh1am4wErf-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه توی ریاضیات و بخش توابع مشکل داشتین؛
این عکس به بهترین شکل تابع f(f(x)) رو نشون میده.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72287" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72286">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:   طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه. در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه. توپ در زمین آمریکاست.  @News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72286" target="_blank">📅 00:34 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
