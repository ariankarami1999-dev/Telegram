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
<img src="https://cdn4.telesco.pe/file/jWzjyXyU8AIkvGy5S8l6PfrHmHeK6jb2awPJr0bo0rgfbQ-R5Y-yH5Qh7ypRG07UDBYvRmb3gUuTRXLx7FzE4Rk_JiHodGhG8_yeIlx0yT_xOx_QyRZIfqrC41TC4tdFTB6f1CpvaOewuYjyBjf-Lnnj1j75HAHEwnGnK94BeKl0WBZQtyVu2a0quHRkEtuq1J2x1BmfhkuKJLJ3Qc1e7YpdUjyUTCJ1o8WWUG289gw-nPZikcnG-I9Gjju_EoJorehY39c8y6svTBv1-yFC7_X5MWBIfhEMkedfiBPOiP28K433V0OQL_P-cCrBgkpXPaNlV4bHbNCn5h3rg3uKIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 22:13:24</div>
<hr>

<div class="tg-post" id="msg-454276">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a5e6e348.mp4?token=gL-9wcyqSQQdvkAAjJptLRgOr5jj-zGEkBI-bK_zaoxzczOZgm9LcLF3OYtF5qZKts4ouEOgd79B6EICJFn1B16b6PV07_PSbGFzPS-TUoWPvx9Z0l_6VUYSHGTFvexbdKWGA5D9A7tpdCgUe-o8gVFOL7OcPQGVP15VSMJW28XaQRPCgE8L9jRA408RVhOhYygZ-Ox0LfJktF89Ir-Rr36CovKEoED1H-j2JXgvaW5mIA1vUMIxp2eVTQhjzPKinNy3DKu95duqCREnPnhu-sS_qgIFYI6I15PhodOo12Cx3b06fyKr8O_cV25yacEq24n88vvvCxyn46op119c7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a5e6e348.mp4?token=gL-9wcyqSQQdvkAAjJptLRgOr5jj-zGEkBI-bK_zaoxzczOZgm9LcLF3OYtF5qZKts4ouEOgd79B6EICJFn1B16b6PV07_PSbGFzPS-TUoWPvx9Z0l_6VUYSHGTFvexbdKWGA5D9A7tpdCgUe-o8gVFOL7OcPQGVP15VSMJW28XaQRPCgE8L9jRA408RVhOhYygZ-Ox0LfJktF89Ir-Rr36CovKEoED1H-j2JXgvaW5mIA1vUMIxp2eVTQhjzPKinNy3DKu95duqCREnPnhu-sS_qgIFYI6I15PhodOo12Cx3b06fyKr8O_cV25yacEq24n88vvvCxyn46op119c7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگهٔ هرمز در کنترل آمریکاست</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/farsna/454276" target="_blank">📅 22:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454275">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bac9fbb15.mp4?token=Nq992CdRndTXDDB3Q9pDvSZrKrzj-NCSQk6Hy4llqbL_A5uwuG6Dev1Ccw_FOboevqhvh6BKDnrYsyf2XpyhyMLQLiNfAek9IbtitGUXUyKtFUP06wfszum7pIpXJuR7J9b0x9myiR9eaK6VFOW446WC_VgDY6yOfMf2fZd9S-8QtbM2oUI325WDya6xnoQmkwTiomBJCJCfg0_aJ8XvBWIgT3-ykcfSYzAbrM-ZMR2UExIdVXktvXb01t7zr732usJQJUjV-7my1RCmNfClxjmjJoLuyw1bQnSo--rRYaHvHlPIjCwYxmYks9TfzRgeoZ121yH83p0UiXgkSHY5gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bac9fbb15.mp4?token=Nq992CdRndTXDDB3Q9pDvSZrKrzj-NCSQk6Hy4llqbL_A5uwuG6Dev1Ccw_FOboevqhvh6BKDnrYsyf2XpyhyMLQLiNfAek9IbtitGUXUyKtFUP06wfszum7pIpXJuR7J9b0x9myiR9eaK6VFOW446WC_VgDY6yOfMf2fZd9S-8QtbM2oUI325WDya6xnoQmkwTiomBJCJCfg0_aJ8XvBWIgT3-ykcfSYzAbrM-ZMR2UExIdVXktvXb01t7zr732usJQJUjV-7my1RCmNfClxjmjJoLuyw1bQnSo--rRYaHvHlPIjCwYxmYks9TfzRgeoZ121yH83p0UiXgkSHY5gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره‌بازی بغض‌آلود عراقی‌ها از روز تشییع امام شهید در کشورشان
@Farsna</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farsna/454275" target="_blank">📅 21:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIwNFIOaK0KqDhtbyCqcHBNnY0UHMX4W1h91K2QFXljyOVWGXbsoUjaGEeAbD00cxahU5oczWhKIpXn-IBI_Nq003WXY6fnza7zZW4rF5tuydVwmQ6tj2doz9-cb94kjs2fN1DbTpIB1z822PSudcPtYTt9iUDnxHZsIWL4O9fTzrPKJ73n6vGe7UGG_aXiwIu7ODBTKYw0QjUvTLNwx9RuygubGprh_xjrb8dvb2hnJzp9Vf_p8PYjinAIU8azzRT9iXdICgb443ZZb2QLJ4LwAipsH9IwGT5FTvqN67MHmfZFaFt5xCRguBxpw1lv1D0gwn1aDcq3LQfQhRkWN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5KfGUVanxEGPss-YYg8cB_OTARHj64rCekFeAQoFpxHex82OJD9iLq-cpsY7hreC_j_xsMRps9gjZHBkE7SlzQXP6WV4_DakwjZiQexRLQK0VYD7Pd7_8Z7uIj5kzn6XGhLZE8L7FmnumMGBx6OLkMXRnRFS4dxgmXDYjs0FzWaJCbabqQvAgrJOcYRLCzPltXsmN95Iudsb5MVvtwBdJdIpzHo_8AZy8fj22lLYmxvV-0lqxYbkWcChAs4KS2_pagKbJo28rs5pV6atvRf2mXh2ydLy5x-QF9LQo0GhoKevFiakWXwudak3tO9CE07SZIQtDFEV7_hAAyr2FFKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAEjlUFAh9XGX0BgtrtVYTuNJpg3ZLUBpd8UpZa31mu1xEg4LwnqcJQCFSOzOHPkwBt6BkyJos5SjZOGtAMX-sCVXIBm12uN_zVscoo080BKiyBxOyovvqurAeTygOWCID95VKIAMr6Om-DsOganfMMxywivbCWyZiLSwB9snJKvFYEKSx1BCqKTTXO35CGeafYR9VmE2-r9N2v1Dgis2VRW5WFVJ0FOtS1WKaueHdWTVNjUcG_Z1gan2cqRTJdbiUUyJB78ceUygnRWO9XuIxqcnkv-wMW9Qq1U1RRXA2pYIx0kazcFD9cmr2T8GiXbKT2YCTkl2NXRJIvVdQrc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0L24nstr2fXXi_XO1R_QIyiKXJU8VZc9HstVgrtyEZkPxmuuRpqDOm1FW5EEzARfLq9I4cXx5W64QbOZpoE7-zpmE0ly-cy7oE8wJ0OhqIaXaqmV8bcj8cv-qAw3CQ30qSXd9pnQ0sSd3FO82T0JmivS6leN0lBO0Ve9V69S0SRRtjXMNADd79NU6xlGwle64k2hf8uBvgwnntPt649uGJFToXcTsoxcsbZZIiqonPXwlbc7Yq0JMZJWZvw8ioo53aeDJZk1z7-Ue9mfUUSs1MCJBqocfF9LrGDiQS5nsnxIjUnSfYKPUEw2MpU4UzpCO7fBczmNQb1CKo2G57aOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsC154MMlx3Qj7sdjFMt6K68bKliZsAe6FDMyW8399ex5xXfgWgKFZ92w4zjPjtBeYxqeT-qrQmSPgOKX6f5W8BFPme9-FfDNmygPVsom2RU-o7sH8fLzCyP2h0phF1FDCqgiQyLuagb4tPGhQu33pS9cfilw_Qe7FESuz3-CvhGc7zYZ13MKNZCjFMT1wclgjGal9IKSXVTjacrTSMvmrPoUkv3C3NUARUXNvYx0WCtZebOWoYTg0xSvXPK2IdpycrPduojhQCKWtW1jH-NvSc5ZRnSGb4lAPaa0UnvoBY4-eC_x-LBpzdDFjiOF8RxmebkJXvxuDsXAA56lYwRng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زائران اربعین در حرم حضرت عباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/454270" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454269">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPAmvO3jMkDipn2z_JY-QXQmnjx5BUWUKUX8h8lkOrIs0m_A1zM3wfkOdfJ8nTxgSlrH6x17YHtEqXb6E1siYccAoAeiWJkwOBw25TvSqFVeXNTE3It0SoZjuqLcy7LW8W6ffDJPBLMulKsPENas5VWqnhzKsbjhg3BqFuZS9NrS8S5D-7FqqPex5bbXKZt6Jz2PTbr2pnQveTiS4ffc6I6OJNJIeH8ZGkcQCPG_Xy_lsHVNHpZUoSxXj4ajlSySOkMKpJIlScKkSKrF1uKdMI2H2iFJHiy3C0_Z7skWeI2eUyGOyYtnSE-eaxf1-z3STQIgi8_bLUDvv9_iN9ry_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
واکنش ایرانسل به ابهام درباره مصرف اینترنت: دقیقاً به اندازه مصرف ترافیک بین‌الملل از حجم بسته کسر می‌شود
1️⃣
بر اساس مصوبه‌ رگولاتوری، هنگام استفاده از ترافیک بین‌الملل، به ازای مصرف یک گیگابایت، دقیقاً یک گیگابایت از بسته اینترنت کسر می‌شود.
2️⃣
ترافیک داخلی با ۶۳درصد تخفیف محاسبه می‌شود؛ به‌طوری که با یک بسته یک گیگابایتی می‌توان حدود ۲.۷ گیگابایت محتوای داخلی مشاهده کرد.
3️⃣
ترافیک پیام‌رسان‌های داخلی با ۷۵.۲درصد تخفیف محاسبه می‌شوند و با بسته یک گیگابایتی، استفاده از حدود ۴.۰۳ گیگابایت ترافیک امکان‌پذیر است.
👈
جزئیات بیشتر و متن کامل اطلاعیه
@irancellnews1</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/farsna/454269" target="_blank">📅 21:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🎥
گزارش ویدئویی از مراسم امضای تفاهم نامه همکاری بیمه دی و گروه اسنپ
#کانال
اطلاع رسانی شرکت بیمه‌دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/farsna/454268" target="_blank">📅 21:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454267">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/farsna/454267" target="_blank">📅 21:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454266">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06725d913.mp4?token=RvVSIrcFTo4tMb1E-dOlDHwC3QWYoSfwbEogD4IMWh1f31FnYXk7BO0MxqeqxExloUxGe4O76C7UBPJXC390qqv3RPayrjW9jCX3uY2CZYd0QUYZsKtx_3oK0SamHPzJX0rw2zGAnCXq9W_kkzIbDiXCkcWTlAHO_C2VBUeJqto7bVBM9zaupug1_XGrzuxa8MJBJbIsGv3-mqTJKIGRH4y3Zj1al7JnpRuqgyLZuIexeC4eIu5R2ET7iYVx7b6-hqRnNypd1I7A_zt_aa6ZVxzyGF1-C36QE6F-vAOEupJimHyHBWWjOG3UW1kcMX3INs3HFpRpRfsSt4nB5Kmk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06725d913.mp4?token=RvVSIrcFTo4tMb1E-dOlDHwC3QWYoSfwbEogD4IMWh1f31FnYXk7BO0MxqeqxExloUxGe4O76C7UBPJXC390qqv3RPayrjW9jCX3uY2CZYd0QUYZsKtx_3oK0SamHPzJX0rw2zGAnCXq9W_kkzIbDiXCkcWTlAHO_C2VBUeJqto7bVBM9zaupug1_XGrzuxa8MJBJbIsGv3-mqTJKIGRH4y3Zj1al7JnpRuqgyLZuIexeC4eIu5R2ET7iYVx7b6-hqRnNypd1I7A_zt_aa6ZVxzyGF1-C36QE6F-vAOEupJimHyHBWWjOG3UW1kcMX3INs3HFpRpRfsSt4nB5Kmk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اجازه نمی‌دهم ایرانی‌ها در تنگهٔ هرمز عوارض بگیرند؛ اگر قرار باشد کسی عوارض بگیرد، آن آمریکا خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/farsna/454266" target="_blank">📅 21:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454265">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fc616a97.mp4?token=DbjBKqZ6-JOuqZFGyrWKAB7NtFg3F_-hWrhwV8kl-wu-EbuXQpMY1MEN5xdVnzsvSD7LgQi3TuAHYs6-gUeNUM6z6zBABGQ2IP9WGn0GkbHLl_Ua1_c2XfTk8T5ibtnqsdypJjiKt34GaCsxt-yejp4LUdSXTuXCicJJuHMDOhdP8ctRgnUIcIdtVyZ75_kQrsBob3aDe3lWlSB87T7twQTTXkZXWBULrIffvzd8rNXfifxHEIqQyG5QnxzO9xxfOjZ7lB-FPyUKJjraQOUR9mxWfNCWbNEU1jjSf2sXlewMP4Ix8PfIl2GVs5JKYF1ZSjDGDZehwHZThuV5xuCOrUdvmHpI59ZQxmgOFoYeI4oncfiw6mNkQjp-RFldVVt3UoQevs1eTWkwlemSaHKACNRL8qjMK_Uuub3mkCow8AMQINuZG7vifbPyy1rbH7tHb_dODnDkAyJAMXhXyzWJrhy6fcEDMUB_MUfccq3xLlt0awDsvfwV8q3YEK29ndZ55MnQ2voZe2MRlfLvLrt7mWOzhHVvJKnW4cflsUinVYUJ3zY2ZEuALDvI3RJRj9gqRr9zNcA6NgbOlp0iyeWcDdFOR5IylF0sA7OqGE5zy52EGgI_Bfl9HiIOoXFPERs-BdT1pidPq6M8ZJ4e0HcCTCE9IhZNZbM1iixa1GyhNwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fc616a97.mp4?token=DbjBKqZ6-JOuqZFGyrWKAB7NtFg3F_-hWrhwV8kl-wu-EbuXQpMY1MEN5xdVnzsvSD7LgQi3TuAHYs6-gUeNUM6z6zBABGQ2IP9WGn0GkbHLl_Ua1_c2XfTk8T5ibtnqsdypJjiKt34GaCsxt-yejp4LUdSXTuXCicJJuHMDOhdP8ctRgnUIcIdtVyZ75_kQrsBob3aDe3lWlSB87T7twQTTXkZXWBULrIffvzd8rNXfifxHEIqQyG5QnxzO9xxfOjZ7lB-FPyUKJjraQOUR9mxWfNCWbNEU1jjSf2sXlewMP4Ix8PfIl2GVs5JKYF1ZSjDGDZehwHZThuV5xuCOrUdvmHpI59ZQxmgOFoYeI4oncfiw6mNkQjp-RFldVVt3UoQevs1eTWkwlemSaHKACNRL8qjMK_Uuub3mkCow8AMQINuZG7vifbPyy1rbH7tHb_dODnDkAyJAMXhXyzWJrhy6fcEDMUB_MUfccq3xLlt0awDsvfwV8q3YEK29ndZ55MnQ2voZe2MRlfLvLrt7mWOzhHVvJKnW4cflsUinVYUJ3zY2ZEuALDvI3RJRj9gqRr9zNcA6NgbOlp0iyeWcDdFOR5IylF0sA7OqGE5zy52EGgI_Bfl9HiIOoXFPERs-BdT1pidPq6M8ZJ4e0HcCTCE9IhZNZbM1iixa1GyhNwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیات برگزاری پیاده‌روی جاماندگان اربعین در تهران
🔹
معاون فرهنگی سپاه تهران: پیاده‌روی جاماندگان اربعین امسال ساعت ۶ صبح روز اربعین از میدان آئینی امام حسین(ع) آغاز شده و تا حرم حضرت عبدالعظیم حسنی(ع) ادامه خواهد یافت.
🔹
«اجتماع بزرگ خون‌خواهی رهبر شهید»…</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/farsna/454265" target="_blank">📅 21:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454264">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b00c95db.mp4?token=KQxw9_2I_QQW0wynyAlH46IaT-7HOWADIB56_jC_jeG_vu7xQrdd6wnH1ldXA9dEdaVSGaaXxNaiP0rnp6zRaCDg7Zyf402N9jnBUPpvIvYnkBo9gupYc32pfxKoZVXuknVHRGZyr3E0orWqlcZfV-OwZrUt0BH8iz7pc6cEsQB7jHSsqOMBYywxLZ1m8r0NZ1U7mqMyUYR7c1FTsNvQcaFX6t6xbm1tcbER1oVW9-I3Lhup4n3yV_dk5XJi7_4_UefcKNchoxexoWH08TBt23aD34vHHwDVuAoAmeSxsQdoupS3g-zlIkno_Q9AckWB4244s1Hyr6jFQPAK1iXwTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b00c95db.mp4?token=KQxw9_2I_QQW0wynyAlH46IaT-7HOWADIB56_jC_jeG_vu7xQrdd6wnH1ldXA9dEdaVSGaaXxNaiP0rnp6zRaCDg7Zyf402N9jnBUPpvIvYnkBo9gupYc32pfxKoZVXuknVHRGZyr3E0orWqlcZfV-OwZrUt0BH8iz7pc6cEsQB7jHSsqOMBYywxLZ1m8r0NZ1U7mqMyUYR7c1FTsNvQcaFX6t6xbm1tcbER1oVW9-I3Lhup4n3yV_dk5XJi7_4_UefcKNchoxexoWH08TBt23aD34vHHwDVuAoAmeSxsQdoupS3g-zlIkno_Q9AckWB4244s1Hyr6jFQPAK1iXwTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک اربعین دلتنگیم رفته به سوی کربلا، چون بر مشامم می‌رسد هر لحظه بوی کربلا
@Farsna</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/454264" target="_blank">📅 21:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454263">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22cacd7384.mp4?token=VGjitkeo4Wz_glJLoalcoVUCQnguhpUcqJbhEY3hsfSQqOcWm-9FhO27yYg_7InK6MLkYpitH37mEUCnafAdK1EzqDgqomvqquZyVmHCjrxbtXA__BJ-bPLtcPa59lyatYYkrOe5lM6yr1dm3U6HyE_DjuVewrCv0GVomY_aeqfsKI9tXJTIrGHoNLf_17r8a4Pa6OBttw2Nd-SZaFW6SqfLUeE6be8uCwLKbWFFB-iGSQSthd3pHC4UNARNmjaVK9fhAimbz3_HI112z1Rtdl8XY1EzA823H97Q0BHpWCQkyFkfvcZ5AW62lDJH6kG188jIyh-vtvqxis2BGLQCog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22cacd7384.mp4?token=VGjitkeo4Wz_glJLoalcoVUCQnguhpUcqJbhEY3hsfSQqOcWm-9FhO27yYg_7InK6MLkYpitH37mEUCnafAdK1EzqDgqomvqquZyVmHCjrxbtXA__BJ-bPLtcPa59lyatYYkrOe5lM6yr1dm3U6HyE_DjuVewrCv0GVomY_aeqfsKI9tXJTIrGHoNLf_17r8a4Pa6OBttw2Nd-SZaFW6SqfLUeE6be8uCwLKbWFFB-iGSQSthd3pHC4UNARNmjaVK9fhAimbz3_HI112z1Rtdl8XY1EzA823H97Q0BHpWCQkyFkfvcZ5AW62lDJH6kG188jIyh-vtvqxis2BGLQCog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
می‌شه به‌ نیابت از پدر شهیدم چند قدم بردارید؟
پاسخ متفاوت عراقی‌ها به در خواست زائر ایرانی
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/454263" target="_blank">📅 21:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454262">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926ecfcfe1.mp4?token=cDZLg0gvyD8GZDLTvYqP6CNvBBcUoF2DzKbiVA6_rw45Bq6XD9L3nbnKjMoPZibR4CveUyUvP7B-IJPOR0OFrryAfYQQ3rRoCtc_FWgljTW2tf2gpH1AlqrDcW56KqNDd_iGJKLDTy_WYijZ-1kHmpXn_7csRTEK4arl9Qo14gQazkPC5JiAJDUQJDfU7vZWIvXcDkd4uq3qESqgNdibBIgS_fPzGNspGtB6eKbYDXXBURm1hqLp40v1cDCdzihU9586kw7QuyqvH9atknYJqkl21NWpm6Em6mMxzz8Tqm4XayZMqmRqtRO9SDatRdRaBAlC2E9rA8MNKN3wNiYkm5s_psLXfJIxNFqjlXN2Gkmi8nDtHMkJztV7BHPJPM4be_nLKmtq_l9Z432RewND19LF3XA9vHzE3p4_AcYq9x2M4ja-cj1zbq6DwnkdDDM_AUayBGcap80oEZsduFsqyLcxStiGg-EQZeSh1L-fBG1ucx00YtX-7hQMaZzq-WOFW3h5f91--es5TytmrVVMFlSuOGKfG_bR00i67p8k0Wdf2_K68x4hHRZkqPCDda8HyaPB-NctJt_zIhQwk-VZSehByULXKkZuq3V_ZtY01f4VFPk8b2wKxs76GtvS827iL-VeBmZ7Y44Oz-he9iKLf8SiL7zKcJoN6BunBPCrwuc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926ecfcfe1.mp4?token=cDZLg0gvyD8GZDLTvYqP6CNvBBcUoF2DzKbiVA6_rw45Bq6XD9L3nbnKjMoPZibR4CveUyUvP7B-IJPOR0OFrryAfYQQ3rRoCtc_FWgljTW2tf2gpH1AlqrDcW56KqNDd_iGJKLDTy_WYijZ-1kHmpXn_7csRTEK4arl9Qo14gQazkPC5JiAJDUQJDfU7vZWIvXcDkd4uq3qESqgNdibBIgS_fPzGNspGtB6eKbYDXXBURm1hqLp40v1cDCdzihU9586kw7QuyqvH9atknYJqkl21NWpm6Em6mMxzz8Tqm4XayZMqmRqtRO9SDatRdRaBAlC2E9rA8MNKN3wNiYkm5s_psLXfJIxNFqjlXN2Gkmi8nDtHMkJztV7BHPJPM4be_nLKmtq_l9Z432RewND19LF3XA9vHzE3p4_AcYq9x2M4ja-cj1zbq6DwnkdDDM_AUayBGcap80oEZsduFsqyLcxStiGg-EQZeSh1L-fBG1ucx00YtX-7hQMaZzq-WOFW3h5f91--es5TytmrVVMFlSuOGKfG_bR00i67p8k0Wdf2_K68x4hHRZkqPCDda8HyaPB-NctJt_zIhQwk-VZSehByULXKkZuq3V_ZtY01f4VFPk8b2wKxs76GtvS827iL-VeBmZ7Y44Oz-he9iKLf8SiL7zKcJoN6BunBPCrwuc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این عمود در مسیر پیاده‌روی اربعین حال‌وهوای متفاوتی دارد
@Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/454262" target="_blank">📅 21:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454261">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bce25d15ea.mp4?token=mQ3dg4UGiOqg7bVHtnzkTNEbWcB4n4rtS4p10E_7Jvvrt0sxZ1AeAjW4IetYSzdXx6MCxkQFnusCTl14Zd2BG0yC8F9gj3soZrv0EPHtZMk2iQTWIb8QAbGbSqgLZMiSnWw7BgkhHYSOySNlRE8T0-Og1F3DU2os5qKaI4-ijhGoZDQCALRorEl-e4ewqMD14whLb_pwB0IZXRGTSz--S4I3gqRKsN9HwrRfscQI4CDsnd9IWD9Dk3VmD-DtBCh2um0oBc4HY3jWAF7TItcmmnUJq3qfBHwOFNfr6hNWjOVQUvYVhDmVFFCbcbVgm4WFG0sywDICZsOiTuZkWUt38Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bce25d15ea.mp4?token=mQ3dg4UGiOqg7bVHtnzkTNEbWcB4n4rtS4p10E_7Jvvrt0sxZ1AeAjW4IetYSzdXx6MCxkQFnusCTl14Zd2BG0yC8F9gj3soZrv0EPHtZMk2iQTWIb8QAbGbSqgLZMiSnWw7BgkhHYSOySNlRE8T0-Og1F3DU2os5qKaI4-ijhGoZDQCALRorEl-e4ewqMD14whLb_pwB0IZXRGTSz--S4I3gqRKsN9HwrRfscQI4CDsnd9IWD9Dk3VmD-DtBCh2um0oBc4HY3jWAF7TItcmmnUJq3qfBHwOFNfr6hNWjOVQUvYVhDmVFFCbcbVgm4WFG0sywDICZsOiTuZkWUt38Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اسرائیل‌هیوم: تسلیم‌نشدن ایرانی‌ها ترامپ را آشفته کرده
@Farsna</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/454261" target="_blank">📅 20:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454260">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c316fa21b.mp4?token=jOjPZyuKohQeFFFgA2jJjDY-sQggjJhg3X8LEd-yChQauFzZ5pBoYyNuyK8P_uKdQRLQ5vWJaDGOCwUjMxDQ19JXRwUJoK0Em-IWCYROpGa6TxFstoaBf2yDI2rIQnK8QygW5ACWeTQhNady3-wOpIoGrnzqt1JJlorfbgIsis6U2w5ZqRUAa3bnYIXeswhqGfxpnJQyMROxbIjVA-FWyfJQ5AzhfxLl6Ty1_oelu-2OPlzO8ZC59AahPIhJBi6eC3ijgVoRgb8Q_flGK4KTl1FRoBNH7hPhG0LPE4MSu4v5b3BtkV3IVf0l3YxZvHzRPyqxFBnUOzwcSMWn_fkqRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c316fa21b.mp4?token=jOjPZyuKohQeFFFgA2jJjDY-sQggjJhg3X8LEd-yChQauFzZ5pBoYyNuyK8P_uKdQRLQ5vWJaDGOCwUjMxDQ19JXRwUJoK0Em-IWCYROpGa6TxFstoaBf2yDI2rIQnK8QygW5ACWeTQhNady3-wOpIoGrnzqt1JJlorfbgIsis6U2w5ZqRUAa3bnYIXeswhqGfxpnJQyMROxbIjVA-FWyfJQ5AzhfxLl6Ty1_oelu-2OPlzO8ZC59AahPIhJBi6eC3ijgVoRgb8Q_flGK4KTl1FRoBNH7hPhG0LPE4MSu4v5b3BtkV3IVf0l3YxZvHzRPyqxFBnUOzwcSMWn_fkqRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: دشمنانی که گفتند می‌خواهند از طریق اقتصاد ایران را زمین بزنند، آرزوی خود را به گور خواهند برد
🔹
برای حداقل ۲ سال برنامۀ مقاومت در اقتصاد داریم و برای هر توطئه‌ای که دشمن علیه ما اجرا کند برنامۀ متقابل داریم.
@Farsna</div>
<div class="tg-footer">👁️ 6.55K · <a href="https://t.me/farsna/454260" target="_blank">📅 20:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454253">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KmMSOvItiAdaHXz8GhowPO2j3pL4HVTZUuBtaH61iunkABylufcn5ECDbLSIg30p4Dn8V0c6GurSO8uZfLY0mQXTTeqQ7czFrqkIFfw8iyp_AtnIkKoWPufmkR75EBtyjPgc-69rsxi0dI-cNWZoh9KNGlwSjdgU10n78tcY0_Z4ejQ8TRd8XENCwgOX4YLr-O-AQo10y4ymRW7m4pFYxrVNEsvfKIQ5ELLSgBwSRzkZWI-vayyH2F_sqbaeVip__JCw20duediSFha33c9ITp6hAJJrMmA9fNd3vUSxMHIq5H99V6jSForQ2jtXQIW6zLx9er74cL57LNqvrLsnww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LrnCHSqOwJrrd6MuqxlOOyM0YcNLUYfGuJXpxa-Xcsv3tXrAjmngV1IpJsZuZqUsc1A4qvjXpMIjr3McDgsBoaCSfzw-PpxpzR1bO0XC1RaY0cV8Va47WZiJsKnghTwoaxrxY5NqzCrcumNxNWERHc-Uh7OLG2nerbgZzJV8w_aCFIC6X1KQKpOrb7fEq5uRMWvVzGEoMwpZ2oGEoj9JVDVb4VnW8GE-_VU4frnozQhvaN6vSeFwmDlGvLM3JJZV3qMeAl1GnKqyL1KpTxCqtXb714H8j32rYt-jIPYY2LIFHEY7jYAulopcjxM6V9cJBxDPQJUEa8UhDNYl8HFAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQF5p7rr0exrFhj_r6chMm1jyQVnDVVq4hWOGANWoB5QEJ-1zovZJlN_soCobn6Ic5JIRz-M6eMvIdeZte6EdDpPGGUhmv_zGxjyO4oSburajjF0EcCSXKSPGnmjHXkBG4uNjRhkV_hY5cdLjiqZSuveCpWF55bI63YyaB7MBERx1Jl0B7if7mSv_k9A-lQHnrvXnnS0GqpG16SGDj-rdW_1eyf0_O_dng3V9lpqbtWAAZ7IjU919Et80r1nL5MciqxLRiiZX24ib9PWj-_J0ak0iGNDeWGs0UuzYdy1W99Wrdax9BEOonn3vHVurfOcsZvaAo911btx-9o4KS-GBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OvMKb6XrtvBA3OiP9nq2Ur7craw-yuXFRXCL1EIygCTpa7xYx1b54lG_hNhmtvCSMRjlHCEnBO1MYCM2N5XM8_6ggWQOGoQQz_0fpGSMhAFKOu0247Ajc4ky5v_APIHH9DhXZUY7oNYgdp0lkXgtxBj-w8QoQF40x1wPn5cArQM39K1q4AI8Tq5jlp2-X8RcH4WuXlmg4BpqSy-Q0keArLpZ3zqjdfJ_Pafb84DIewrhsJxt5WCbq2VOVjl0cTkt3ThrxvSWSK5o-MEpJr94O8yGURLfKB3JtrDE74jA2rUBLxucYXlA8c6wUY9xOxuYTLgXcIdVO6u6YATlwgurZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/II6eksHeObI46NnCBg3--s1c6qodr55e_ShFL8334oUIXvTJ0ZcMej5jvhH-uKQdBEnxieZD_eZGnCj_C-FZU6Pgoj4L9rvdxW62E3ubkX_ZM8wSaTx4Afthk7OjdpHq9Wkzn8RvOk8dntduQSprir0Ldnj7Z8DOXvnQUEka8E-0DAY5nJfJ-DURdbgXuo3KCxhHQ3N3QLaad33ZLzfDT9cV0wNkPOL73tsBTb5CqAIuFlxmceUOmQmgUfs2h-EwoXUPWcGNJUof7xIYi8zxuDq8SiMN8uhM03F5-u2UKmibevDjCouNjO4LekFH8zVc7msnuCje0TKgQ4OMg6YUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlXDNYDEwEmWSfz3jCVFMj7L5L_cq7-XbAeVnzp1pZ3zhTaa9qv1HecdTYYGEIVUQkgKh6l79umowZGcIjySm9gIgMWllAk_gVpY64BeSRf5mrORb6cgFzgVajJCrIqVcB_usffHm-dvfZC0Bf_Uj97B4uQEhuSar6YdfeYWDkGzCf4KG3t0QdGZ7nWQ0uUvM08rUmYjQbFiPwKiZfcebNvEfVL0pT8TRLEOtBTqXsyXDN3Y0J-PSvD2KTi_MMQyib6YwPfoTBXpypoo5t4YBVaNDTwJePfpfA94AHJGtGa5gh1cr8rzKuvouO3mZEO-RFBmgCdkW55blUjjbAD8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iMl3xvfwk2Axk0QHaHe1emVnwI-Nnw7A7lln4kb7DQK-jtXnHpmO-g5l-rW0pI0I93m_9Smc1aByM0qYo6uJOl00lnKFEjr9_uUz_5qZralhYfdBNn_vI-9ekm78bg0f652h6CWisrIyNi9-HtKP__T_dZfY54ys6750S12Of7aS7nKrTEXjM0uTkkKcmIC4kJ4lf4tYoI-WUi3DP-tiqYTkrLcbC82KpDpQ8Vz705UVb1sxLcSjZE22gbl-J5JRwv-3RT0R_D7EFbuAoCuAnt_VCeunOzVhS8nzKAcqXr9s1BJhLpQIa1sUKnfsWZO9xaeUPPXjjnc7Vr1-aUp4-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تردد شبانۀ زائران در مرز خسروی
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/454253" target="_blank">📅 20:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454252">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">درهای استادیوم را به روی تماشاگران باز کنید
🔹
«زمین و تماشاگر که ندارید، لیگ را پلی‌استیشنی برگزار کنید». پیمان یوسفی، مجری برنامۀ ورزش و مردم این جمله را در واکنش به‌احتمال برگزاری فصل جدید لیگ بدون حضور تماشاگران عنوان کرد.
🔹
سخنگوی فدراسیون فوتبال گفته جمع‌بندی نهایی درباره حضور تماشاگران بعد از جلسات سازمان لیگ انجام می‌شود، اما تأکید کرد: «لیگ با تماشاگر، لیگه.»
🔹
لیگ برتر اواسط دی‌ماه پارسال به‌دلیل ناآرامی‌ها بدون تماشاگر شد. بااین‌حال بهمن ۱۴۰۴ به شرایط عادی برگشت و چند بازی از جمله مس رفسنجان و استقلال خوزستان با تماشاگر برگزار شد.
🔹
با وقوع جنگ آمریکا و اسرائیل علیه ایران به طور کل بازی‌های لیگ برتر ناتمام ماند اما تماشاگران در بازی‌های لیگ‌های پایین‌تر از جمله لیگ یک و دو حضور داشتند و بدون مشکل خاصی به تشویق تیمشان پرداختند. حالا رئیس فدراسیون فوتبال گفته آن‌ها تمام تلاششان را می‌کنند که فصل جدید لیگ برتر با حضور تماشاگران برگزار شود.
🔹
برخی معتقدند باتوجه‌به شرایط بازی‌ها باید بدون تماشاگر باشد اما برگزاری با حضور هواداران تیم‌ها باعث نشاط بخشی از جامعه، هیجان‌انگیزتر شدن بازی‌ها و از همه مهم‌تر درآمدزایی باشگاه‌ها و فدراسیون در روزهای سخت اقتصادی می‌شود.
🔹
وزیر ورزش پارسال در این باره عنوان کرده بود: «همین کری خوانی‌ها باعث نشاط، سرگرمی، تحرک و صمیمت می‌شود. خواهش من این است که برگزاری بازی‌ها با حضور تماشاگران در شورای تأمین مطرح شود». تاجرنیا، سرپرست مدیرعاملی استقلال از زاویه‌ای تازه به با تماشاگر بودن بازی‌ها اشاره کرده و گفته: «ما مدعی AFC هستیم که چرا میزبانی را گرفته. برگزاری مسابقات بدون تماشاگر، پیام می‌دهد که شرایط آماده نیست».
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/454252" target="_blank">📅 20:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454251">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d7974cae.mp4?token=hfKSZsg1NjDVeSOWReAe4k7CJGOluRHwuy0hGFEQknoNHHcnggvV8-_I5yFMc6M75IZ0RovXGkDKPnnYKnhQvm4LB92hzTWbPD0dgPqg4rRHH7QNVRT_YvFyLVi-ZFJY_4aH8rNP-idyIjoXJMMneS5-WDb2zFqeKcWpdd8b41fW1aDBi8M_UwVmO2qQX87eKgv6r8cZszUZh0WirxK9oH3f6S1X9w7NN1x9jCdv1yA-6yOKj3n-FQxpX6FOs642uapC51yEd8Y3OX8xxbITVIWA74wVyRW54pr4gTNtXTkKxmXFiqxgGERdcgxY3F6hDNwK_4OHHbq6Zx3wel8YXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d7974cae.mp4?token=hfKSZsg1NjDVeSOWReAe4k7CJGOluRHwuy0hGFEQknoNHHcnggvV8-_I5yFMc6M75IZ0RovXGkDKPnnYKnhQvm4LB92hzTWbPD0dgPqg4rRHH7QNVRT_YvFyLVi-ZFJY_4aH8rNP-idyIjoXJMMneS5-WDb2zFqeKcWpdd8b41fW1aDBi8M_UwVmO2qQX87eKgv6r8cZszUZh0WirxK9oH3f6S1X9w7NN1x9jCdv1yA-6yOKj3n-FQxpX6FOs642uapC51yEd8Y3OX8xxbITVIWA74wVyRW54pr4gTNtXTkKxmXFiqxgGERdcgxY3F6hDNwK_4OHHbq6Zx3wel8YXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این کودک ایرانی گم‌شده، شما او را می‌شناسید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/454251" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454250">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2714274f4c.mp4?token=SBVRc80rqbMWHbzaPCw6Fq6t8MMbQJWu5hPEYn3kzDme9rftRZWUyUXhVRVxOhGCgjGdkHYWGTnTUaeNawlbBWpgnpQzWQA1WhzyUrDg3FkVB2NxzS_BS3-kDBBvEEcr3CYJEHV7MS9jTAQvTTYnA27koccfd0UoSPPCDSSNwgXdYjks0VeRwSVp-Lff8I8yWLx9Kfb0gcYzp5-SIil-TOxLQqM9NP9Fj0eXBUAx7rNUg1gA2nVdYGdkTRzDOdNBvD2m4SHTth314N0eEff7JgxF-19H2x7HSmONuAsIF6YGHhHaRTu2t0FRS5IW-KH_rs8LyTdX8jvlNiNALy9_eblEgfG_YnDEOC1mGAWNnRVrvXxjTZ89nfFag7EwFdXC8JtbYNq0YuTSInjuVVbvR4pz35vFE55ocV25YNsdeZ8_WUMJjVrRDAnoMcjqATEV8Pc8f1UZG7PpiBIvUypM-uE5JLzDDO4TedloKQFTVD0pBrXCFcGa42vVf6HnU3FFjyhT0hFDX3eJcqlGdMt1zcOoYFp5vEFlc8O73qTgz9f0x7tQulQtzm-U9CuUrfaWlX8Hvkj9rbrA0BlhZ60EHx8TsE4Ixi99dwLdfYlrLlBziTUXCbf-Ntg6Uh3q-YZ3Th8GIAg2CEICjL4pKJHKGDGUJ2tQfT7qvCDfUyxwALk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2714274f4c.mp4?token=SBVRc80rqbMWHbzaPCw6Fq6t8MMbQJWu5hPEYn3kzDme9rftRZWUyUXhVRVxOhGCgjGdkHYWGTnTUaeNawlbBWpgnpQzWQA1WhzyUrDg3FkVB2NxzS_BS3-kDBBvEEcr3CYJEHV7MS9jTAQvTTYnA27koccfd0UoSPPCDSSNwgXdYjks0VeRwSVp-Lff8I8yWLx9Kfb0gcYzp5-SIil-TOxLQqM9NP9Fj0eXBUAx7rNUg1gA2nVdYGdkTRzDOdNBvD2m4SHTth314N0eEff7JgxF-19H2x7HSmONuAsIF6YGHhHaRTu2t0FRS5IW-KH_rs8LyTdX8jvlNiNALy9_eblEgfG_YnDEOC1mGAWNnRVrvXxjTZ89nfFag7EwFdXC8JtbYNq0YuTSInjuVVbvR4pz35vFE55ocV25YNsdeZ8_WUMJjVrRDAnoMcjqATEV8Pc8f1UZG7PpiBIvUypM-uE5JLzDDO4TedloKQFTVD0pBrXCFcGa42vVf6HnU3FFjyhT0hFDX3eJcqlGdMt1zcOoYFp5vEFlc8O73qTgz9f0x7tQulQtzm-U9CuUrfaWlX8Hvkj9rbrA0BlhZ60EHx8TsE4Ixi99dwLdfYlrLlBziTUXCbf-Ntg6Uh3q-YZ3Th8GIAg2CEICjL4pKJHKGDGUJ2tQfT7qvCDfUyxwALk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توزیع ۵ هزار پرچم خونخواهی رهبر شهید انقلاب در موکب مردمی سازمان رفاه، خدمات و مشارکت‌های مردمی شهرداری تهران در مرز زرباطیه
@Farsna</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/454250" target="_blank">📅 20:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454249">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b4a4714e5.mp4?token=JdMELVhaBvfdld6mGeiiumpTKplBwKZvBTvlG51V3JeTvcO9ZHThn9fZQ0BwUG_AlS3nNkmYjCJXv8M90-jUEMdyqni1NvMXORsxsqjVldqkVpr3icx4M3-jryiizTVro2quO9h8JX6kEMjAD6XcuvdCILXUkSXWE_4qtsCMc_gjyIiACVEi_dlONwJJMW4h-1W1caCodSfn36ajxWARhdp-HOtRvv9BsgJYyIz_Tj4uRH5xMZfkiH3VEa2s0nfKfY6IA8fSiaZcnoHzjortIH2F4aOjHMdNAWZFLSXvFlD99P3CYrGAoMPdyp2C7OaYgRIlWRfu2OJmkGS-xH-GKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b4a4714e5.mp4?token=JdMELVhaBvfdld6mGeiiumpTKplBwKZvBTvlG51V3JeTvcO9ZHThn9fZQ0BwUG_AlS3nNkmYjCJXv8M90-jUEMdyqni1NvMXORsxsqjVldqkVpr3icx4M3-jryiizTVro2quO9h8JX6kEMjAD6XcuvdCILXUkSXWE_4qtsCMc_gjyIiACVEi_dlONwJJMW4h-1W1caCodSfn36ajxWARhdp-HOtRvv9BsgJYyIz_Tj4uRH5xMZfkiH3VEa2s0nfKfY6IA8fSiaZcnoHzjortIH2F4aOjHMdNAWZFLSXvFlD99P3CYrGAoMPdyp2C7OaYgRIlWRfu2OJmkGS-xH-GKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
این کلیپ از حضور قهرمان مسابقات مردان آهنین در اربعین و خدمت به زائرین، میلیون‌ها بار در رسانه‌های عربی دیده شده است
.
@Farsna</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/454249" target="_blank">📅 20:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454248">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromشستا رسانه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/750dcb2b9d.mp4?token=bbE0OgrIN7s8AuU9hfqswRHt010YT7rkhoh-8NA_gA237WMfTzoyH1hShO9XYQNX1patB3C9VCtYYk2EdH0GCJ3z8Xf7g-DXkDhaNTEnoSxMWsjG5emmC1RqLeW5zamuJ90uFoct84JVQnNSRZ-8sU-n065kA9bATumDlfGNs3mLIQv2oX03b99b2Wr4-DTGGEzpEEl6gN2B4LHFWGBnFTih4wTWdaNoQu5c_sJZcwlE161zGvhJJDb96aV_HrWFPtMYHZj5Ij9tmt2jUM3uwybnM4m5lmUA2S93Z1Un7GppBJ7AjoesuT0V-iTxEn94zlPJ8vsvGVkp6lklpsci8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/750dcb2b9d.mp4?token=bbE0OgrIN7s8AuU9hfqswRHt010YT7rkhoh-8NA_gA237WMfTzoyH1hShO9XYQNX1patB3C9VCtYYk2EdH0GCJ3z8Xf7g-DXkDhaNTEnoSxMWsjG5emmC1RqLeW5zamuJ90uFoct84JVQnNSRZ-8sU-n065kA9bATumDlfGNs3mLIQv2oX03b99b2Wr4-DTGGEzpEEl6gN2B4LHFWGBnFTih4wTWdaNoQu5c_sJZcwlE161zGvhJJDb96aV_HrWFPtMYHZj5Ij9tmt2jUM3uwybnM4m5lmUA2S93Z1Un7GppBJ7AjoesuT0V-iTxEn94zlPJ8vsvGVkp6lklpsci8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مواکب گروه شستا در پایانه مرزی شلمچه
🔹
اربعین حسینی(ع)
#شستا_کنار_مردم
@shastamedia</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/454248" target="_blank">📅 20:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454247">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/454247" target="_blank">📅 20:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454246">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ دوباره رفتار همیشگی‌اش را تکرار کرد
🔹
رئیس‌جمهور آمریکا بار دیگر ایران را به «رفتار دوگانه» متهم کرد و مدعی شد مقام‌های ایرانی خواستار مذاکره هستند، اما آن را در رسانه‌ها تکذیب می‌کنند. او همچنین ادعا کرد تنگهٔ هرمز در کنترل آمریکاست و در پایان نیز از…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/454246" target="_blank">📅 20:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454245">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‌
🔴
مقاومت اسلامی عراق: پاسخ ما به عربستان و آمریکا قطعی است
🔹
برای حفظ امنیت زائران حضرت اباعبدالله الحسین(ع) و خادمان موکب‌ها و جلوگیری از هرگونه اخلال در مراسم اربعین، پاسخ ما به تجاوز آمریکا تا پایان این مراسم به تعویق خواهد افتاد؛ اما این پاسخ قطعی است…</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/454245" target="_blank">📅 20:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454244">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
خادم عراقی: شهادت آیت‌الله خامنه‌ای و ایستادگی ملت ایران دربرابر استکبار به ما انگیزه می‌دهد تا درخط حسینی استوار باشیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/454244" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454242">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c001b59ea.mp4?token=TvwPSrXeH1bm_I8q-Yoimm33g4k2U9N990czhyt5xpZJ8HzAq2n20BJ1hGxsaXaE4Ye8P1hYa-NIQmaT4VZc6y_oDZxVcwpV-0jCud586LmOA7GtkTmjXGynqIL1SOvPDosmdCxK5nany-cjV6pxR4XuIsnnBUJQKDiXNf2EyhPviqaGtcq6got0a4LuxAemxLWOKGCkxrkdfDFRE108w0kcoy8k_RV2XB3Mw6MydMgNF2H3mCY2ETguxhLjpCo2maH1vjAKtj9xS22UV60-iyuLOjoRdPvG3XMkATrXPPKbD22-rfCIUnLMl27Pl0MSICthrM0-JUs0V7O8X7EYZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c001b59ea.mp4?token=TvwPSrXeH1bm_I8q-Yoimm33g4k2U9N990czhyt5xpZJ8HzAq2n20BJ1hGxsaXaE4Ye8P1hYa-NIQmaT4VZc6y_oDZxVcwpV-0jCud586LmOA7GtkTmjXGynqIL1SOvPDosmdCxK5nany-cjV6pxR4XuIsnnBUJQKDiXNf2EyhPviqaGtcq6got0a4LuxAemxLWOKGCkxrkdfDFRE108w0kcoy8k_RV2XB3Mw6MydMgNF2H3mCY2ETguxhLjpCo2maH1vjAKtj9xS22UV60-iyuLOjoRdPvG3XMkATrXPPKbD22-rfCIUnLMl27Pl0MSICthrM0-JUs0V7O8X7EYZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
بزرگترین پرچم خو‌ن‌خواهی امام شهید در بین‌الحرمین  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/454242" target="_blank">📅 20:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454241">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1ef204199.mp4?token=eAu5NC0xixu4FdaMVjlFSZOwPAli-SvEvI1-ALDqt2NfUJk-IbNhilHSogUVVHQljOf_7YNLezGkUf7Qsx-MlfBqJdBNqyBU_vqKqAmJOq5xdhypXSLpCdKsQQOMV5Q7TP4F-yOOd7CcZ-o-Bk-0zZ4LsTy5xSzLyH1gmF3iTKozKLTRKO8aU56lTyhmojmO8O0Bvnjx6Tij23WeeSxDhrrLNmIarnxZDRQsE_NzwQHN703a1Vok9ZyflxYuNU3yel1di6FlinkJDO2khcCpMXNMsH3Vhs_tZ1jo0P7Gebie11VzYdGgSlxRBdqx1KeavZmzxcLz8ljhGM9-dXYZTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1ef204199.mp4?token=eAu5NC0xixu4FdaMVjlFSZOwPAli-SvEvI1-ALDqt2NfUJk-IbNhilHSogUVVHQljOf_7YNLezGkUf7Qsx-MlfBqJdBNqyBU_vqKqAmJOq5xdhypXSLpCdKsQQOMV5Q7TP4F-yOOd7CcZ-o-Bk-0zZ4LsTy5xSzLyH1gmF3iTKozKLTRKO8aU56lTyhmojmO8O0Bvnjx6Tij23WeeSxDhrrLNmIarnxZDRQsE_NzwQHN703a1Vok9ZyflxYuNU3yel1di6FlinkJDO2khcCpMXNMsH3Vhs_tZ1jo0P7Gebie11VzYdGgSlxRBdqx1KeavZmzxcLz8ljhGM9-dXYZTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کوچک‌ترین خادم اربعین، مسیر پیاده‌روی زوار را نظافت می‌کند
@Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/454241" target="_blank">📅 19:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454240">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNydNhZOCf-6RsGZd4w7y7Ac9SgBtICa3_r0ZM-mloAy-G7NQqhC91E2oBngSuRvIPygwxxe8r7mlKdkM1kb-c2l6BHgDYqQolNiRJQFJtnmvs7I-x2M_INeseAnhgcXXGaPed5iliFBJRV1uqrtx4Nd6kEJw9q6HAmE9N98qbV4shK6FeLBQH0_3A9oX_dwwptnG5zn6Q6oOcPzOPmXfwdKptAwv01YPxXf4pR-LBcskq9nqz1TZhjG5tzr8h0cvSKXyM-E9yG4FPtZPrlilT78Gq0VeTxKAlAxrvNMlnfE_WHNT6Pe7wJ9O1lZzdp_fu_HaHjbcxJlYBDBraxxSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: هزار مگاوات به ظرفیت شبکۀ برق کشور افزوده شد
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/454240" target="_blank">📅 19:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454235">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FB3nF8ewoZ4KTNHnHdFgEStEVa5t7CUstKafzY_XRue8PJprsl3Vo_2Z4HIPGQnVpIW77hEatITunvm1qOwi3xp5knNkHpH50hQ2-zgW9y0kfD2lcfUVruHj-UQvTgvbBIslF5sCMjABqiCQ2um-8MO8qdXCazF67DfGjq81VLHmyeuaUfxOF3RAP0EnenrKAsQGMJavWTmAUelt3S0MRQMs177GComEFWZLrdZcGS4RYlkHSIRWPa3CbHkOAQBoyGOUu1rViKXK9tPaS2U9FZGdCB8pnaTT5-IXgDx6nparn09kwrpffSwQQJ6L-YbzYqU8eztZ3MjYIdgcCo3E0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nzlbcfFLn57LrH6NjXdVVhLYCyoXYV-5yqRbRRAV_vG1Kthp9Am-4g659ZDR4lSFDmoJoPHyhnz3djO6WdzPUnyWMvhlQE0kicpCn09GGEUZW_mmyZJGoGu6TNk6yleQLDtKutH73AjoC-XP28uakFBEhL48TWJp8mIFDFJxl3V6OlWWxyKFrqiA2DJsuZWGlter4dx9i_gdrsR4KwJ8qUFazjMEI2jFsJx9szn5U4dUnVFDlMw3GsyAQVS8p85Jo7tEunzA4vh1Ab9re5pStE_G93UVw96mOc3GlGKQbdC-FJ-RX5NwqPCruDbtONqIb6h9vHawIBJWs9ZzxiCcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7-UV3skdKZvKNJa8_nLoXmgOsU2vgvZPakx3QAAMC_Uzhij9guGEi25_f7VvVsT8joHeKtUw3lZIWYTE8Dfj-b79d8962QDmDhBxSi5MHiA2IiALfF2BlgtMqx9R_YEh0pnxh9KZhGU_7VfsZZex1-Fj6YlRD2iDi2Hd1FCGJSHklVQE9ckBmiBzfjoNyILlOq0159qy3OctgPUYXacBP0NQkhzZP1DNNkwgvHdVI9Cv10gS3Y9RDvgD8xlnbAwNLVbrHBilwKteruLJHsDkZRhTUDN3L2lL89XOY1z0sAAXWsX0KdyFT5Wy1Xd_3bmFclm5DJhsqweRxxdrWU3NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNCtnmx4xqoBtdVKcB9f3eygyn6Px61RTivVRGViJIm80179NBfbuqxGINoQBa_wyeJUNOE95PFTAjy4Rz8Z3--SIvYrHM4DSEqOM_I8LtSRY2LVkrdu3mqD4kL8XcclxhVwhsCpzMbSSg58_RagxP_ixHUb0grK2MLRU8R_3e9GBbYiMb1l2xPIEY6HDD_YlP0r6WRjVGuOdt_YY6WhqCNkBHsBHMbW8n6tZeJPeZrvXyvJK_75jNfqKXZi4EoMQ1upGdQUyO3S71doWgt_U1eHySrackgdRSkvD7UHht12wEeTbdv49hpMqu3gPhBfyHcCKaXlDNy8bNzIGY6J7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQp6xWjMsGdmctNifHsoAJvjjeHNkg1FXgzNyYSD2Ng_EfuQaygfiRNfVBLVX47SejHzPYw3kplVk48ANDB4rvV7fbULAggivE3vaFTDu4vhiG6664f_x4pvAjZAVTV98wxwanXg004jfVLkbiQOWqfWp2Dx7XMo7-MPicn7h6YnV171LHvtxbz_ZuNQcI2lV5efI4GnnAC1YGkj5gM0RXPYHW-REybuSzBDiAdvwiYs6oMcpMGiRW-_BGBUfi_AzhYlFA53nogdjeIHp3WXRs86XelZ80AYWDhQwQUJwYUe21s-sVkipFBWyNuDAtBebgenjLal3Z6zSg7VnaP_lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگترین پرچم خو‌ن‌خواهی امام شهید در بین‌الحرمین
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/454235" target="_blank">📅 19:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454234">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOBw_rWShrmnpY9AzAPxVRlqkmMXtzpzm9P-E9RtiwJqY1i5Oeii_23xwuAIcgbI3daN38MWuvl9gjbx9OP8QbVok8CMoT3UJkM6sNl-_0Kr1YbP99cUAOcOh9Pm_8xl0oJMVxQXGPZ6LuXjt550P7BLKecqzNd3dzFgWq6jkbErbVk8WjSiwQ7AA-PJ_v6kZyERd3JpPjd6ZE5s8SIqDHfVAKjeZpkz4Mgr6Rzgn3RNrF_7NgKdlrcMlUbTT0mHMlZ0gC8I6Yk2FMLRppu2Tbq7sJY4M9ajnGBDumD6uevW7D3vaLKsURRYKbrmnTIYzTvX562oRh0EoUOMeBNtEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پاکستان هم ادعای ترامپ در مورد مذاکرات ادعایی را رد کرد
🔹
درحالی‌که ترامپ مدعی شده بود که «مذاکرات با ایران دوشنبه آغاز می‌شود» مقامات پاکستانی اعلام کرده‌اند که «هنوز هیچ تاریخ یا مکان مشخصی برای برگزاری مذاکرات مستقیم ایران و آمریکا نهایی نشده است». @Farsna…</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/farsna/454234" target="_blank">📅 19:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454233">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎥
تردد زائران در مرز خسروی در آستانۀ اربعین حسینی
@Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/454233" target="_blank">📅 19:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454232">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNGQrxhbmwccyovq83gT4f9z48LJOatM8GUxsnVL-_eVfFfxmZ2rG5zNe5vo4wMTQT69pE3oTZxMBWM38yjOR_oLaHER9yqe9jWG6k1EQrcjOUOwteZL61Caq76TGfYYzpZD9T2Hmq00yv_HMmDj41ooNaiaxG62BiWVBnvB2FllPp0ouoWFU83nzZWLMCFX-zDvmWymUX8Wn1lNvbrhpDHPDvPySKBnDl0xh6KteOTTnkaXFUoFDKyTHnLt_cP2jolJXBsO-xA-Kn0V0Y3ezN_nBPzPTLqnPjtzdMrIi8G404IDUAXL0u7SnbtE_Ifco3x9BHn6jOHN_iYOeuS0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلگراف: میراث سلیمانی آمریکا را در خاورمیانه رها نکرده است
🔹
نشریۀ انگلیسی تلگراف: باوجود گذشت چندین سال، یادگار سلیمانی، فرماندۀ سابق سپاه قدس ایران همچنان در منطقه درحال نقش‌آفرینی است.
🔹
گروه‌های مقاومت، به عنوان میراث‌های او در بافت سیاسی، اقتصادی و اجتماعی عراق تنیده شده‌اند، شبکه‌های تجاری ایجاد کرده و کرسی‌هایی در پارلمان و دولت دارند.
🔹
دولت ترامپ به مسئولان عراقی فشار آورده تا این گروه‌ها را مهار کنند، اما کارشناسان عراقی می‌گویند که نیروهای بسیج مردمی را هیچ‌کس نمی‌تواند منحل کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/454232" target="_blank">📅 19:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454231">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABNRLrEmfQe20X6CcYWWmjRLoV9gSVJuqqoLsaLn5WTsiREjWPIhKA1ByKhKTGtKmnC6Y17vSEwVx8ziE9xi8UidJQ144TBUHYe-JwJ1wevfm1Ascmj5MbqQsVFWYP34n3ZwNGA-a-jv9Zts-PrrguZXuun87_luryvgU09vDRNAd8Zo__GrwFAZDvwt9rykVxdjhEEkPExETg4LPa5KSPa6covzsVjJ-OCDo7S5xHAYrNRvGFHsEOECGKo5iTe05RhbPPq1M5oMhZ9CKL7qbQ7I_K8a7Y5ycnpiZyVPz3JTDUw30VeFMaLtrwD2_hsAue06U9GWJioMWhNaalwNCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار رادان: تصادفات اربعین ۲۵ درصد کاهش یافت
🔹
فرمانده کل فراجا با اعلام کاهش ۲۵ درصدی تصادفات اربعین نسبت به سال گذشته، از رانندگان خواست با استراحت کافی در مسیر بازگشت از خستگی و سرعت غیرمجاز که مهم‌ترین عوامل بروز حوادث هستند، جلوگیری کنند.
@Fasrna
-
Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/454231" target="_blank">📅 19:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454230">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hb9aCT50v4JFfZHpAOHLhsu2Azrj2eQoCg-ysaKfcGDjFm1PSjUYjk8IIpnSmiKxYd0V-wBxTdeFQkBwaAcxw1JU6gut_aIlexKHo2jfxOUYLU1kI98rl_PGZg1-FvUIgbvIImb1prsDfmst6UJeveDZnATjOwFgznsipofIJ9C8yJPYfl_9H90Z188gfvp4tSco6VjVkFldA479tAGomQlNG-UEbT0yBPdqt_Z1Pc1OCRzhOSjG1HPVvWF7p0qiqkowgX1P9F__PO-zE-pj1Re5XfrovvRh4kDNTXqDS7XcmJJLn5IYaeIL5oxw2pRiz2dCJPv51SF2PP2BzrutNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده نیروی زمینی سپاه: درصورت هرگونه خطای گروهک‌های تروریستی این سرزمین را به گورستان عناصر مزدور بدل می‌کنیم
🔹
سردار محمد کرمی در بازدید مناطق عملیاتی شمال‌غرب: به حول و قوه الهی با تجربه گرانقدر سال‌های متمادی دفاع از سرزمین مقدس ایران اسلامی و بهره گیری از ایمان و تکنولوژی و علوم روز، رزمندگان قرارگاه حمزه سیدالشهدا علیه‌السلام نیروی زمینی سپاه، تحت فرمان فرمانده معظم کل قوا، آماده برخورد با هرگونه خطای محاسباتی دشمنان خارجی و سران و عناصر گروهکهای تروریستی هستند تا این سرزمین را به گورستان دسته جمعی عناصر خبیث و مزدور مبدل نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/454230" target="_blank">📅 19:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454229">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad128bef1.mp4?token=q9pPc5skLzbVh1iB_nbCEdLHUwWpvHpgEE0axYtsml6zu978sR6ko45J9wDwEJIKPSS36b2uXAwS8LGl2wUFIKUtSntyApo4dDVBOpThDQgp8mcSNS2VX1RDzet6uEbnXAfHpYjmRutoIeAQU6NF8RI_rf8umQodyFn3P9xIO6dg5L3SZG1uMPRYu-OLU_UP8Uj-58xiSPjbohgwtsQJ11-op9akJlcV_hLUt18mG3Z9NbcYNlufpKj-h6yqBia6__CPBUg3DLnuf-9-mbcCehGZcgdueTtA-laDTuMM6JjR4PwEYMTL3tPYN3-FVTNrsgzPZOUG1E6-_CMxz1Is9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad128bef1.mp4?token=q9pPc5skLzbVh1iB_nbCEdLHUwWpvHpgEE0axYtsml6zu978sR6ko45J9wDwEJIKPSS36b2uXAwS8LGl2wUFIKUtSntyApo4dDVBOpThDQgp8mcSNS2VX1RDzet6uEbnXAfHpYjmRutoIeAQU6NF8RI_rf8umQodyFn3P9xIO6dg5L3SZG1uMPRYu-OLU_UP8Uj-58xiSPjbohgwtsQJ11-op9akJlcV_hLUt18mG3Z9NbcYNlufpKj-h6yqBia6__CPBUg3DLnuf-9-mbcCehGZcgdueTtA-laDTuMM6JjR4PwEYMTL3tPYN3-FVTNrsgzPZOUG1E6-_CMxz1Is9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای مضحک نتانیاهو: اکثریت قاطع مردم ایران شیفتهٔ اسرائیل هستند!  @Farsna</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/farsna/454229" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454228">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76554f0287.mp4?token=qYiB35ANUKFrgutilK2ZYG6T0Z6s6Y64ACQtG_xfDgDJgqptF8WTD7ZMaURH1yqzLJsGJ7D-3WEKJf8aZX0Ym1eFUPoxNo2hD3MvzcCMOAqrhJKZuE2W-Qlv0kNKgzmhURZMBJu7SS6284uD59789mUUhnHohjJ9z6mG1Qd80gOO8lGUNLh4PgBqj3nzRCHUJvuNbQ8BkXMJJq4O5VuDcVoO88TMYGeY9C2etrPjxAPazTNJjXejXTkTZcR_nHKwyAmu3mp8DRBckmoA1XVAzaeCuAWxkfY68yjx0BIy9AA3wr-e7aRWc-6AMmV4VICVw_-6sinF9VbczeCVuizJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76554f0287.mp4?token=qYiB35ANUKFrgutilK2ZYG6T0Z6s6Y64ACQtG_xfDgDJgqptF8WTD7ZMaURH1yqzLJsGJ7D-3WEKJf8aZX0Ym1eFUPoxNo2hD3MvzcCMOAqrhJKZuE2W-Qlv0kNKgzmhURZMBJu7SS6284uD59789mUUhnHohjJ9z6mG1Qd80gOO8lGUNLh4PgBqj3nzRCHUJvuNbQ8BkXMJJq4O5VuDcVoO88TMYGeY9C2etrPjxAPazTNJjXejXTkTZcR_nHKwyAmu3mp8DRBckmoA1XVAzaeCuAWxkfY68yjx0BIy9AA3wr-e7aRWc-6AMmV4VICVw_-6sinF9VbczeCVuizJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای مضحک نتانیاهو: اکثریت قاطع مردم ایران شیفتهٔ اسرائیل هستند!
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/454228" target="_blank">📅 18:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454227">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گفت‌وگوی تلفنی وزرای خارجۀ ایران و پاکستان
🔹
عراقچی و وزیر خارجۀ پاکستان، در تماس تلفنی آخرین تحولات منطقه و روند رایزنی‌های دیپلماتیک جاری را بررسی کردند.
🔹
وزرای خارجۀ دو کشور در این گفت‌وگو بر تداوم همکاری‌ها و رایزنی‌های نزدیک با هدف برقراری صلح و ثبات پایدار در منطقه تأکید کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/454227" target="_blank">📅 18:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454226">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31ea1a5cc.mp4?token=MDT7sYnArKUYB5TkzhlHsATJ46jmgk71r55detzDJEwwawcAIUK7XQBfT4GcjJhEKV8pVg5aTast5P7N8wz4aXZ50qEoOq996KJW0f8U8Uhr_LpBruihMlYgMtTnQBwdcadPKjIIQc-V1-3rozMzZrZNoRE7nrd7ps8_AfIoeLx7-lvppLKdVICtg5U7Hn021JRooHpWyQmRmaxvLWP4eWz7bK2w6G0AQXniiHF4seW4WGgsP-Eh2rvM-_L4v2DfuatrHrPGYgR_PsETld3vg9j7IGMQkaAvPICPBgKv2dJ8ZiVgfuhiJ7cfKQUeshE_7DCKM4ykP9nN3KJTJ13qKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31ea1a5cc.mp4?token=MDT7sYnArKUYB5TkzhlHsATJ46jmgk71r55detzDJEwwawcAIUK7XQBfT4GcjJhEKV8pVg5aTast5P7N8wz4aXZ50qEoOq996KJW0f8U8Uhr_LpBruihMlYgMtTnQBwdcadPKjIIQc-V1-3rozMzZrZNoRE7nrd7ps8_AfIoeLx7-lvppLKdVICtg5U7Hn021JRooHpWyQmRmaxvLWP4eWz7bK2w6G0AQXniiHF4seW4WGgsP-Eh2rvM-_L4v2DfuatrHrPGYgR_PsETld3vg9j7IGMQkaAvPICPBgKv2dJ8ZiVgfuhiJ7cfKQUeshE_7DCKM4ykP9nN3KJTJ13qKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاص‌ترین اربعینی که رفتید کِی بود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/454226" target="_blank">📅 18:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454225">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCDOJmaoN7jKIxeivlGHXyHIed5gO6-lvYtlsdkNjm3MHuulDYIpwxFjbeWe6Ljb2yq8aqRe9HJwtNIZOWSxzwerjCGz5SCBQIHF6hE_McOsVgsh7D2R0po9IIY_K_RSMA14hdVZxQ5LM-N4QfBbN617TLKqpNJnX8JzuNM4Tz9pi2ISK0bFB1ymEmGNsJkicC-iEPSXIoi7bG-qqM2puH1Ws33dRK79gCb-cKlYXxya7dCm4HGz5IOL8przb_7ZkiiYuLsoEiN7dywMcGkorghou2U7lqALTFqTI7CifB8KqD7LY2OmKOd_PP15cESE73ULGd6aOLFDWFf-FJRTgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: شرکت‌های نفتی آمریکایی باید همین الان قیمت‌ بنزین را برای مصرف‌کنندگان کاهش دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/454225" target="_blank">📅 18:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454224">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff59fa69c9.mp4?token=n64-ZX56zNcyLMFs67P32sDogH6yez3JRCUVQ6UAYhNmS5pwnzjWtcOcfjVDqzD0Vp3Zds9VDQfnnvYpXvj0JgvvJoLhtzeR37M4EjGJKAqL1zI1-l9aF6wyZf8J25rQC0pGATja18TqX8mq3wCObMT5v_ViOclQEsiKcY0wSauTT5dIopyz_IuXolhPyF9Tmc4g13CLrR8nQ14SVgPkcMoL28ox-15btOwRDsDnd7cM8_qpV6KpVPlfmiif4dAZA3Y5z5beG0zwX7IPmKVoj4PBeblmNVdsVlvZjzNqq-aYn1d1yZVqxAcUqP2SBUz-UnGETyLuzFiNnYIRkjOF57m3rAYPrfG6ZrvN0cFW7TnGhowp5K6fc4UN783BloXW1Sasxntl-5xIGOjWHmdzI_M0dKHJIcBp6SEDydbNLkjBEAwB569kvsTE4VP5WFam3cesJ0k1pi0U_eXe-y6d0lrgaaJ09rxpNYPBfev_0JKkH-OGUB-8GC4lk59Wmt5aHGaiLpD6exWItb5GmBRqUnwdXJY44k2EWDlSldNd1k6JFRC-NNhIu6xOFfWIl_HmcKJy1kQ0Xlqqgsi4BXs6CAljOgIESFnSB_-vPXtZJ7n-uHM9FBYgqqchBif4dza5Eb6GD6RcQVv2WnSBVVeOj_s_VJlO7NAv0mGqZd1tnJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff59fa69c9.mp4?token=n64-ZX56zNcyLMFs67P32sDogH6yez3JRCUVQ6UAYhNmS5pwnzjWtcOcfjVDqzD0Vp3Zds9VDQfnnvYpXvj0JgvvJoLhtzeR37M4EjGJKAqL1zI1-l9aF6wyZf8J25rQC0pGATja18TqX8mq3wCObMT5v_ViOclQEsiKcY0wSauTT5dIopyz_IuXolhPyF9Tmc4g13CLrR8nQ14SVgPkcMoL28ox-15btOwRDsDnd7cM8_qpV6KpVPlfmiif4dAZA3Y5z5beG0zwX7IPmKVoj4PBeblmNVdsVlvZjzNqq-aYn1d1yZVqxAcUqP2SBUz-UnGETyLuzFiNnYIRkjOF57m3rAYPrfG6ZrvN0cFW7TnGhowp5K6fc4UN783BloXW1Sasxntl-5xIGOjWHmdzI_M0dKHJIcBp6SEDydbNLkjBEAwB569kvsTE4VP5WFam3cesJ0k1pi0U_eXe-y6d0lrgaaJ09rxpNYPBfev_0JKkH-OGUB-8GC4lk59Wmt5aHGaiLpD6exWItb5GmBRqUnwdXJY44k2EWDlSldNd1k6JFRC-NNhIu6xOFfWIl_HmcKJy1kQ0Xlqqgsi4BXs6CAljOgIESFnSB_-vPXtZJ7n-uHM9FBYgqqchBif4dza5Eb6GD6RcQVv2WnSBVVeOj_s_VJlO7NAv0mGqZd1tnJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این‌گونه جلوی خاکستر شدن طبیعت را بگیرید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/454224" target="_blank">📅 17:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454223">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجار کپسول گاز در دبی کشته داد
🔹
دفتر رسانه‌ای حکومت دبی اعلام کرد انفجار کپسول گاز در یک نمایشگاه در دبی، یک کشته و ۵ مجروح برجا گذاشته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/454223" target="_blank">📅 17:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454222">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a9e00a49e.mp4?token=KEjjnL8oJReNBUARgAZll39fDVTpwIdTbFXwRJTEfVHA0gD-Woh3IaCoBokHsfQ7JJNzvTRnOc90-32Isvgk0QTphNaX4hG0M4WJSCxw2Frbs-fAsROTOaxK0OLBrrRrbPY4QfhWvGopD0o7G45jH8gS_5DMiIAPE2kb4MXTsEEvYoLsk8THNWOUURD3PVDfxveerSeGwCtWJSei1FxibmckiMkZXDgoVN-5_u97KqI7BoB_lg2HIKbcMpRT-cnH9pX_BGq0AIE4jJv9XFvQhxoGVUjIqcteC_Q86pgLNMlYBpq8tEZ8b30pjkb2faBwnqf9vt494hxSVN6eBqe37w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a9e00a49e.mp4?token=KEjjnL8oJReNBUARgAZll39fDVTpwIdTbFXwRJTEfVHA0gD-Woh3IaCoBokHsfQ7JJNzvTRnOc90-32Isvgk0QTphNaX4hG0M4WJSCxw2Frbs-fAsROTOaxK0OLBrrRrbPY4QfhWvGopD0o7G45jH8gS_5DMiIAPE2kb4MXTsEEvYoLsk8THNWOUURD3PVDfxveerSeGwCtWJSei1FxibmckiMkZXDgoVN-5_u97KqI7BoB_lg2HIKbcMpRT-cnH9pX_BGq0AIE4jJv9XFvQhxoGVUjIqcteC_Q86pgLNMlYBpq8tEZ8b30pjkb2faBwnqf9vt494hxSVN6eBqe37w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بین‌الحرمین در آستانۀ شب اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454222" target="_blank">📅 17:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454215">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OR7okJffFQefJNva-lkzs85PzVQ4Xmj66cGlS4Fae1gyuYsO72wqfqB3wdHOjJjdvP7tsku0tPTM6XlApIsEhCupfUNU0scqHrv-MjLgV5Mo3BHV0S1RuNZJCB8X5Io507i_mW9yhxCUPltc2HmRcQqWj8abUpSNZ6MYOYXFABLHLTz1DYYTfhhEb29_q4lTou9H8fUtDc_YnulKkGsS8kGVgnlVHLFafP-GbFjE5ADG2Rm5gf52r2btbz9IWzvGtbFiej7FIOFQt-w_uRZNu33EB7lts3t5K_sj4ld5h2DCUshBq16dfmWNDB4yXlfSSOFpJVu8q6o9mZ-kfIYUbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ibVl2Gqx4hNsQPlAr-6I4VL730RIMttiybZN8M5SE6uJSszhJz7VBjhEMAfgBQBIAjOM_pYT1VB564yO3mTeBDQKWm16zWe_M-kfklx7F9Ca-S8MIsLYYqxd1O-_mgax-D9nU-LCrtJTbJEIiKYbBpLAvN_UXgxGMy0SeFnHDecYQUE3F6I82-Niw3qvlLf5Ccd0ZOe1pX6bk9uM60JJawfhHnB3RqHge9vc3rTtO2RWd91XeAgd2koEQ5orPjDRQB2x5m_xtyFED6DvmoKn4FkcMP_56c7UBzbXyIntfTL9Oa7xI6vEtwQvq_8687_6frqpK-kZ6dya69gLPUVHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzq1OHMX4ezilhSR3R-5hQsDCbgxA_P1zQwsmvv_0V6pu7q2vI-64I3DUlXbRGV5L8AO84_6R4lz-cD5GgMyvFCtKrHBGfZkGNZzZQbtcIvvcLznYTk2Xs3ahAXh4HVT2qTXVDIpOAdnPZ6BFtjZedXcPLWOJ4rCS3o74my8NtrlFOzebmXY4pvKimiooLmmeSvtR49fYmfN8GcymYJrS1Cx9cgAByCXS_pxT_HxfPKxgB0ptvbaALsp5NtiLN8OphplcmeS45bgN4odRyds8w5U6MpIDPwMPghduF037WNleA-AeSK314eUmxoUeOXCVw_7YMtvd6tRsANEM1OjEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NxWOtrZ5hVOCYtEGdO7ZlwjFSfEwlSq02MvjVaDVeL9XxQBs50LwzQCTd9CF_mOqtzvGiHszKcZNbQsLFu1GJ_Fvp51DsHkvFzjSGej8KAFnUHd8PYGr9nI2EvI8rvnz1GwcSvoD2uwOcmsiPg4XJ8HDxmks4eZsdKoR25D8wAeBE6objxXw8ZWAprHS0RJIUcl2T4vGNFEn0KgnRLhRGZtMnClwGKEsY1tvnqmLO7Cx33cNoP4dAhBGTN8L3EJnIfVabPRPse-TR2EWFlBY66xZEwdjt2juhK0_pYRM6cQdbsz9KWjJjdsimspyP0-Y90CB3Hs4T50V4Iacoff--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L6pr0xHnE_8pkjsOnUUxvkyLIKeTD7Z4KvuMpmYEdY_UzskoJiIIWGzTXb54S-jG8QHtuhARgqawGRBEmjOR-v4kNoOIBkICZ6SIZrgIW0g6Rwk584CMvCaboTNP7fksH1Pz_xi7mdqqnFOtXT-23_i44b7QC7_1RRv29mVKrXRVZlRbXi1vniA4IyN9CVkWHqcXBxi77_PI2QiB00b4warF0lXwv2CyFvL4skotPHewTg1PSMStzkc0rbTWSLbI2pA8mhz2tsRQ946oT3rBlJ86p_0mIXuSnkGn5FLRSzHp98lWg3mUGIgKxQ4hFaKL19YUbxK9HBNPfx9Yw7G-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rz_Bpw1eEVESBhwq5Os7g4WA9zfL8nH84uLzTVL6ulXpLFy-1b5jYt-4xJK3szrnFs-noR6mzveJ2GziOZM3xadOKZ1nXnMywzQQ6W-di_JzXWBrBFdbKTljs6sF3IQ5RGczN4l_BQQBX1G1DVFzuBee4YixjIpv11NQAItYYOfEZWwCBcYIdUXFzpygNPCeLfHkDwaX035-p8jsAofTs57FRxpBPMn-t5bYot9odTFnT25tfx1j1E67zQYNf5Y58kSPgaBrgoXUcC0WyCAlgTGGGXORbMBChIgyJglHywZ6n9XlxJlOxW2wBexpy8DTmBcychWjtcbcq-9Mg0FGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNCV8EevwexJloPoDyNmmFo0r-9fMHE7bIEGmt8-y7VmyVTn99uuYhO9VGQWlNmINiyOWtTEwXbQSbgpxHBTzbxHqkhRgKgfwsFCG7L-N_iqhEPHBjjzayLMyRr_edKXxuvySRRdqFO1UsO8pQQwHmhojvYWWN42xYqKJekYjqDucw2TQ_h6cPTH764its04QGT2yMywBXxlXVmYdH5dK182PpcgceXnFL24AAvih_mrOVt6LHSNZuY3k1Wmrq0inl8fGmxkbRztHKOxZx2g2wkWH2E715Fw8euDFBYmHwJh5_f4xIvMuU8wTY0YmG_xY9irozlvrpqgR5-T7AV7vQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دستۀ عزاداری زائران ایرانی در کربلا
عکاس:
عادل عزیزی
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454215" target="_blank">📅 16:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454214">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH9xz_DcCkcQH_KERBpzBTerTrXqx6ZcpsIZH07Y853DmIJlQKvGH0WiauF6m5JHLdNpRldCwyHw1dNjlBsUucDNa2SPhglemZjDRaJVR6LxNTvJqB7UcXYRR2yl3fopUlyRxoHt-Vg0CCJYy7hsSjgkZzRg8JZY7CZdzJ4O_jOWi_oD4vWO--hBUZ9Wmo7Ve50Nqc3_6WmMiSfM9_I9mUykLu9V-c9oo1E_7YWpKXSHOeNV6KIzkkz7mcUqDNwk-fiuC7MQoYbKSiHxCDLtllHw_4UNtKLh3xqCWfQsLWcrI2KIjtDt5OazPlVxrGl0c1pHmpVjx4aN_viC9_cJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت متروی تهران: جهت تسهیل تردد شهروندان برای حضور در پیاده‌روی جاماندگان اربعین، فردا خدمت‌دهی مترو از ساعت ۵ صبح آغاز می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454214" target="_blank">📅 16:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454213">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiKOy4-x_oDMDRq09uoSF7RhzVcUfVIJMrp0rOpf3q68RAl5wlFc5a_XwBL1nMgfMCuQ51wgWDmiO9sl50f_12deaiPQAFauklFvDZHJFIzoKDZL3GXCDWYubN0og53Sm1hsLzeKcYMCsgeaj3NH7pVvEVGlON1fwqLET0xtFtPFqq4dmRo1x6GikELRkb8vudVAeqZ3t48YEGqhLg_Bf5_ZPRw0zMIlIJY0V07BPcUYkrRBO3jiL7bzc7hDMBjlQALE7XA6MFPqw6lpOzwLJMoch_aLwDIGFYID2rx7p7Wm31Cy5ZRWuWuZJMFZTjma2TXvnRgqmgZNEcTEz5MbKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر بهداشت: طرح پزشک خانواده از ماه آینده در روستاها و شهرهای زیر ۲۰ هزار نفر اجرایی می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/454213" target="_blank">📅 16:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454212">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🎥
پاسخ سخنگوی وزارت خارجه به ادعای ترامپ دربارهٔ آغاز مذاکرات از امروز: امروز عراقچی راهی سفر اربعین است و باقی اعضای هیئت مذاکره‌کننده هم در ایران هستند!  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/454212" target="_blank">📅 16:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454211">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">سازمان سنجش: نتایج آزمون‌های ورودی مدارس سمپاد و نمونه‌دولتی اوایل هفتۀ آینده منتشر می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/454211" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454210">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎥
سید بشیر حسینی در مستند راویان پرچم‌های سرخ: عظمت رهبر شهید را بیش از همیشه در عراق دیدیم.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454210" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454209">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7RbSLj-fKL4uAeHwu6n1lCD77FPQrWaws2LiN4h9bOFXOtIO2csVofzU5_R3Db9SCLBfeY4gQS3gM-nZoEFiqQH0QUouoTkWHcI-2-hi8O_H8Mxc-i5Q_jmNF-U4CdoYtUA7o87sQ3fSG95kzFOn3BWAzvZKxxHQOJctDYUTsWUTAKX4Snltv_TJDQYBrVOWeqWSfxfpd448UmmVftXBrcuOwRG6pI9EBAPxoGY5in1d7Nd-bVW5sLvthlC_Wmg8SbWAq6RmG6nogWapK5UNFtqqn-5_hPzXsGseSTqzRUf9Z6re_QDIQIoXPPB8QfMn9Sy0Z-ScSempL_rvpwy8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمبود اتوبوس زائران را در مرز مهران معطل کرد
🔹
هم‌زمان با آغاز موج جدید بازگشت زائران اربعین، کمبود اتوبوس در پایانۀ مرزی مهران باعث افزایش زمان انتظار شده و زائران برای اعزام به شهرهای خود با معطلی روبه‌رو هستند. @Farsna - Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/454209" target="_blank">📅 16:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454208">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5cba04d5.mp4?token=XjngzR-jPQylfLeQezTQ8oI-mgB8rokDTEgqYzJHcuXnujHdxTF5Aqcs3cGjTcrTXgU9etE3AESefvhV85ypX0kfAQNIrDhsoe-NizAMJk79Vixf2qNYF2hi5gRa4KrRg3by8b_h3e3_kRsllKlu5UO2r3yHTuu0A0q-7sC-MIrjNHffGKWrYWmn8xW6WUwpRVp_LoMsJexOm6b9KCZMTXkTXA0vVbcVlZpO6NeqTkRmn5Kyjr_4IO5fNcgQPP6f-9Z34Dv-17AibAPVnvCWBx-Qe8TfI1N2IINmvmgT4pEPaFUtlv1jes6OxFaVnTyN41-d8GsX7e_RpDy3iibkAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5cba04d5.mp4?token=XjngzR-jPQylfLeQezTQ8oI-mgB8rokDTEgqYzJHcuXnujHdxTF5Aqcs3cGjTcrTXgU9etE3AESefvhV85ypX0kfAQNIrDhsoe-NizAMJk79Vixf2qNYF2hi5gRa4KrRg3by8b_h3e3_kRsllKlu5UO2r3yHTuu0A0q-7sC-MIrjNHffGKWrYWmn8xW6WUwpRVp_LoMsJexOm6b9KCZMTXkTXA0vVbcVlZpO6NeqTkRmn5Kyjr_4IO5fNcgQPP6f-9Z34Dv-17AibAPVnvCWBx-Qe8TfI1N2IINmvmgT4pEPaFUtlv1jes6OxFaVnTyN41-d8GsX7e_RpDy3iibkAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدم‌های آخر سفر اربعینی از مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/454208" target="_blank">📅 16:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454207">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f93f35ea0.mp4?token=ZI_xQfRqn3pQC0ebvGtxuQrdn7tG40lvQudr7_kRNlfPOllCdDduUNt67IQ3mB56e6ISm6d0Uz3dm8V4oUB1LmX4FU8CRF2BBGF0xliuVjLsiuWEcxuM5ojjBrrgJXhxE2znxYK79RM4XzujFOcYsuUpJ8j7775s--MVuUmAj6Gi96JuTTPJvW8sQgiMjawhMNBu_AyHwdp37i5e1HDwjol1SXciKirf-y3N55Embyg7aKABqZs65byUSh-aA6kIjT8bQ24vbkg2LtmqwDb1qwDGOtR9m5BNuCMJdNwmgzVI4wAEsQkfw5gFdjhwdN0F-8VQOFWHpWc5QPGIGe1BRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f93f35ea0.mp4?token=ZI_xQfRqn3pQC0ebvGtxuQrdn7tG40lvQudr7_kRNlfPOllCdDduUNt67IQ3mB56e6ISm6d0Uz3dm8V4oUB1LmX4FU8CRF2BBGF0xliuVjLsiuWEcxuM5ojjBrrgJXhxE2znxYK79RM4XzujFOcYsuUpJ8j7775s--MVuUmAj6Gi96JuTTPJvW8sQgiMjawhMNBu_AyHwdp37i5e1HDwjol1SXciKirf-y3N55Embyg7aKABqZs65byUSh-aA6kIjT8bQ24vbkg2LtmqwDb1qwDGOtR9m5BNuCMJdNwmgzVI4wAEsQkfw5gFdjhwdN0F-8VQOFWHpWc5QPGIGe1BRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسمان بجنورد در تابستان بارانی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/454207" target="_blank">📅 16:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454206">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
وقتی گنبد امام حسین(ع) را دیدید یاد چه کسی افتادید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/454206" target="_blank">📅 16:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454205">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iesOatCY7QNeEh0F49wW9pybBRAWka77ikCdKOMyn2OAte9sE8XY-M_d833ZoIh8h4jBdTYjwDWe6xCoqNed1ji0TWnOW2Heu7HJVP9gkGCX91Z8OKB619rAOyE1oXk2hpxX3IMqLC5iMdisqFh2NoczDze9WOYnMGr0RmuyNljPHflMe6o-sApraMFq-QDIDsXinqaI0mT_XI83fTvt952RaY2H32yU22xExM6UNzOissGcPIdqQI_VvwwYiut9eohRb93E4rUhynJWh0y1LXVHAM8qLyZkeh06hPhonjtmdw5Zx0VYdgap4aYLQ_sTICT0WBZppG4ZlTXIP5gmrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افشای زدوبند رئیس فیفا با ترامپ
🔹
اینفانتینو درحالی مدعی بود هیچ منفعتی از طرح فروش حقوق تجاری جام جهانی ندارد که براساس افشاگری نشریۀ تایمز، در صورت اجرای این قرارداد، سالانه بیش از ۳۰ میلیون یورو حقوق دریافت می‌کرد و علاوه‌بر آن، مشمول پاداش‌های مالی نیز…</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/454205" target="_blank">📅 16:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454204">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌ قم چهارشنبه تعطیل شد
🔹
معاون منابع استانداری قم: با توجه به تصمیم کارگروه مدیریت بهینه مصرف انرژی استان، ادارات و بانک‌های استان قم چهارشنبه ۱۴ مرداد تعطیل است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454204" target="_blank">📅 15:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454203">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e43657be2.mp4?token=FvMDCVRsLGYCKhBYAXPFGkhXHVJahSU3N_snjEdR7PmEXY6Gd3LvogN9NxlzG7nDnc_nCGF87K0Lo-onhW_aVtnnBGtvWRJiIRAixkeWxjyyPHqUoYuQ0Vy2fV24r37-aEPfo1PxIHdRcJgi3VytI7vBdUNJjorMGGXmhwLeLSPHCkTn4LgYPY7D2hsISi18dpx-79VPuf63U5CYXVVptLbBt0epes4Yr0YWLUqnprb62-JgDlsuTasAYPsAIGb_XOz_3BMN2IDtSaz0_XJpNluu5FfQQNAmg2DUE67RcNEebwPCo3sfeTxrG6qmMUMB2jsQVISdKX8cp_yMIhb5CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e43657be2.mp4?token=FvMDCVRsLGYCKhBYAXPFGkhXHVJahSU3N_snjEdR7PmEXY6Gd3LvogN9NxlzG7nDnc_nCGF87K0Lo-onhW_aVtnnBGtvWRJiIRAixkeWxjyyPHqUoYuQ0Vy2fV24r37-aEPfo1PxIHdRcJgi3VytI7vBdUNJjorMGGXmhwLeLSPHCkTn4LgYPY7D2hsISi18dpx-79VPuf63U5CYXVVptLbBt0epes4Yr0YWLUqnprb62-JgDlsuTasAYPsAIGb_XOz_3BMN2IDtSaz0_XJpNluu5FfQQNAmg2DUE67RcNEebwPCo3sfeTxrG6qmMUMB2jsQVISdKX8cp_yMIhb5CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام شهاب مرادی در مستند راویان پرچم‌های سرخ: ایستادگی مقابل ظلم و دفاع از عزت مسلمانان، مسیر یاران امام حسین(ع) است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/454203" target="_blank">📅 15:57 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454202">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trX0JPRoxDCMKgqZ-YpQ0bxa2fDkxlCRW99Ddb7fYfqiQMYzbBnLd4HiJe3t7fI78GCJCOOP-11Qp1ffR1pp7A7JEya3ae1EZqY7CczDPdwhfEiXwJ_UKxvg15KyRFWI8UaqQMUVE_BYzmyIDDWCfKlGjulpewboidxfWL_So0AlBCZMpTxHy_ng9t9s_t7oVmdffBbfHEoTcwqcll53x9t8QBO-Kk7qWOQ62-1RJMgDAjdLJZu-NEpDAB9_mq6nEz75PuZkNXvpMGr2UVgPNiiBQR0A3HaZEOBrVS3ochcwQK3Ul8NO9YarBf1o7lE3vihoNI3xr1aVqLKyD50s2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: در آستانۀ سومین سال ریاست‌جمهوری، گفت‌وگوی پزشکیان با مردم به‌زودی پخش خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454202" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454201">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhpeHRcbTvIP-9Yp9iGtG3wC45BBUm8nPv0aky_tcG3v19dqL0CqX_irL_gWSdniJNsfU69qwSSdKYPg0-qXJRxZeGKFnbsc9nhvZhSSHDzimYM-Y9aJSJzryID5F_R4KbSC7-8WnLswr9cgSyTg09hM0XkSYQYRxjC-ZyJ_u6w76wx8O8njnJPfGBfe4p7-jqNmgMAzmx7Ti2hw6EOMLE5_gRYrpoiQO59xD89vBVWWoTzLbFPLUKqV9oTCBgFKuIL6GtGxnGS6SydbP6wkiLttyDGOXuDxmrREtCzcS2DODsjHi19HHom6LpWC_hgzpypYgeElU1etHEOEH62GpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالیت رسمی مرز چیلات از ۲۸ صفر آغاز می‌شود
🔹
مهر رسمی گذرنامه مرز چیلات دهلران امروز باحضور سخنگوی دولت رونمایی شد.
🔹
سخنگوی دولت: امیدواریم زائران بتوانند از بیست‌وهشتم ماه صفر از مرز چیلات رفت‌وآمد کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/454201" target="_blank">📅 15:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454200">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKk_RW0JCtBoGUhGi-Hjci9O7aEa4wlbpIjl_WWCx2qrYCdAv_WYJiYXfYgSLjkAVr_sMKfQKTzLfo5zTcUWQqjqxoGJMN3wyfAwO9oRx2_Xcng-9rFLo40lH7Xf3fcGDxaUWChvhVsPOUmUc0C3fefJyWfBOv6FF5Ktqh8jfQ_8uHCMt6JphCKloRYVC4ffftYqx0UIKp480javZPeR-9j1F4SiIH7YGSkp5oUZSLwaWjUH4tJg9vD6ICEj2BvNFjZgSYB1hutkil1Wnk5TezK0t1dpcb8uq9EUC2w39IKzdQiPGnCrNiJ7rzRmSHpU7igLtb1zh65Y5Iw3Llu8kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال قهرمان ملی مبارزه با استبداد پهلوی به تلویزیون می‌رسد
🔹
«پخش سریال حماسهٔ زاگرس با محوریت شیرعلی‌مردان‌خان احتمالاً به سال آینده موکول شود». این را مهدی نقویان، رئیس مرکز سیمافیلم در گفت‌وگویی با فارس بیان کرد.
🔹
سریال «حماسهٔ زاگرس» با کارگردانی حسن آخوندپور از جمله سریال‌های الف ویژهٔ تلویزیون با محوریت مبارزات شیرعلی‌مردان‌خان بختیاری است که نقش اصلی آن را رحیم نوروزی ایفا می‌کند.
🔹
به‌گفتهٔ نقویان، این سریال در حال فیلمبرداری است و تا فیلمبرداری آن تا بهمن طول خواهد کشید.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/454200" target="_blank">📅 15:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454199">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vbu4lGF0o4CiSaM-SEfUx8fKTXXv1cgzyIqT8-0WqMCOQQffdodYxylu5q8uYjiu0VQo88EfrIdl68cNTM1TPgS0FKexAn7YmwUhrCb7onzFzLqDiLUm3vzRmD7CVTa7YQXrO_gJK0pUmGh0_kpcL_EREOlnyvi3YaPo-H8Tesm2OyBXzvSHB3tcNyLjsldc2MQ-4iuY-UqZ7VXorpvUgphp4lF44u70AAnQbssLESJDnjWLCycmU6EnA-aIOlGO4wvk8-xwsGf4ocuf-DywGJZIhYCEpR6V1ybPtEi3vz6IFqtomexT89aC6dcqg2HjelY8PbMH_XdprrGb4uapfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز گوشت را در آمریکا گران کرد
🔹
مارک وارنر نمایندۀ ایالت ویرجینیا در مجلس سنای آمریکا می‌گوید: «قیمت گوشت گاو در آمریکا ۱۲ درصد و مواد غذایی ۴ درصد افزایش یافت».
🔹
اختلال در حمل‌ونقل دریایی از طریق تنگه هرمز دلیل اصلی رشد قیمت از سوی کارشناسان این…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454199" target="_blank">📅 15:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454198">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‌ کرمانشاه چهارشنبه تعطیل شد
🔹
استانداری کرمانشاه: با تصمیم کارگروه مدیریت مصرف انرژی استان، ادارات و دستگاه‌های اجرایی دولتی، بانک‌ها به‌جز شعب کشیک، بیمه‌ها و نهادهای عمومی غیردولتی روز چهارشنبه ۱۴ مرداد ۱۴۰۵ تعطیل خواهد بود. @Farsna - Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454198" target="_blank">📅 14:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454197">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19878aefa0.mp4?token=XEdgZ7882-NnyxbBg7daczgObH6eUcsxoST3xdeTJZ7skBhtQFVR4jF9_VJD9tROyDqcHxCh7-UQciVVhoRk8_F26yvXM-eNRmRjnZ-JiRDemOG3T8n8zMnIZXt0TpwUmQ25QICuvwFbeCyhIHrzUQwGw5XwBaiuMOMoyzDfSLkY7axuWBO3tlKzNTsFuL5yVFjCHf7pgy5Ksd9O16h2y2iYd4bZ9vd9HuVKpZyFuVfx3wkTRy-flvHwz3dIBMkFNKCfF4mOeuS3wKE9XwzNXk-ikFgaT5yuZ8Zp9Hz5qPwEGxNb5UMypzfBCngjVcXt-FJg6Oa-j4nj-V0owICsqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19878aefa0.mp4?token=XEdgZ7882-NnyxbBg7daczgObH6eUcsxoST3xdeTJZ7skBhtQFVR4jF9_VJD9tROyDqcHxCh7-UQciVVhoRk8_F26yvXM-eNRmRjnZ-JiRDemOG3T8n8zMnIZXt0TpwUmQ25QICuvwFbeCyhIHrzUQwGw5XwBaiuMOMoyzDfSLkY7axuWBO3tlKzNTsFuL5yVFjCHf7pgy5Ksd9O16h2y2iYd4bZ9vd9HuVKpZyFuVfx3wkTRy-flvHwz3dIBMkFNKCfF4mOeuS3wKE9XwzNXk-ikFgaT5yuZ8Zp9Hz5qPwEGxNb5UMypzfBCngjVcXt-FJg6Oa-j4nj-V0owICsqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعترافات امید بهزاد و پوریا صفوت عاملان رژیم صهیونیستی که صبح امروز اعدام شدند  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454197" target="_blank">📅 14:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454195">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciaKxRvdNKhYgAgWfJ4_uGhSmzqbECryTy4yCI5tkJQiSx_UWQjHggFbLJgdVuUhFd9l3dtuF7d_8tqbWQcA4ei3-Sf__5T9oxIvyKneMl5lBnq344FFSAV86An139OB7Y_GbrbvYWBbFBlmDZkzVsCGZg7s9VRTp6hYEx9qKSsHmxAKTjJkDPlyGXTTHizcxwl-HixjQ2ZaKDR2Ggc3YN9Lm2qMy4ZXxHrreWQp8-bxooeVIRVW_y7NrnIRoHUkTUUmpt4rnIhodmD6Hz5DF81viwZzDlH9XsC7S4EjRbXj4vtKiPKGLJIjMq9Xq7bX1H2GIHZxvj9yxIHYGbpxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت فردوسی‌پور را باز کنید
🔹
«من را در صداوسیما ناجوانمردانه کنار گذاشتند. از چه می‌ترسید که اجازه نمی‌دهید کار کنم؟ من بله‌قربان‌گو نمی‌شوم، حتی اگر بخواهید مرا بازداشت کنید.» این جملات را عادل فردوسی‌پور پس از بسته‌شدن وبگاه «فوتبال ۳۶۰» در برنامهٔ ویژهٔ…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/454195" target="_blank">📅 14:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454194">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4270bcb2cd.mp4?token=urCcf2AWiPsIOVyBIV2W9CYi7prte8MtFshXRtP-9ZtJrFMi2A5ecHmdvIPZUxzX9mV9uKNV8_2vnMWSZmykrNsaOQyvIDKmSpdDMSaXydpF1U5qyM_KxL7BePfiaOp-xm30_mO8GLFomAYuirUtCtRIovA8Rqzmg01_4bdrmk-fQINmXQ9D_EbTA_HazS5NFP1MTR3YkucJVQkYg4w-tVqwXoK4B6J6z0KBegkX6DNcluP5hwtzlBo3py7QDDnBXARm-vtKrTGz3vEn9mw6ZX7aLxAIEJgfe9LUmncMalAJIJ4TGlLFLvqkUDgckNzPLEGmfXsW2sgTLQODA0jKkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4270bcb2cd.mp4?token=urCcf2AWiPsIOVyBIV2W9CYi7prte8MtFshXRtP-9ZtJrFMi2A5ecHmdvIPZUxzX9mV9uKNV8_2vnMWSZmykrNsaOQyvIDKmSpdDMSaXydpF1U5qyM_KxL7BePfiaOp-xm30_mO8GLFomAYuirUtCtRIovA8Rqzmg01_4bdrmk-fQINmXQ9D_EbTA_HazS5NFP1MTR3YkucJVQkYg4w-tVqwXoK4B6J6z0KBegkX6DNcluP5hwtzlBo3py7QDDnBXARm-vtKrTGz3vEn9mw6ZX7aLxAIEJgfe9LUmncMalAJIJ4TGlLFLvqkUDgckNzPLEGmfXsW2sgTLQODA0jKkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: تا الان ۳ میلیون و ۲۶۰ هزار زائر از کشور خارج شده‌اند
🔹
۲ میلیون و ۲۰۰ هزار زائر اربعین به کشور بازگشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454194" target="_blank">📅 14:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454193">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b99256aa.mp4?token=GP86JqzhpH0MyRyt1iQqs_zCpj5TMjiOseUvg3fOchqI9ArFTuanIZV5JbSQUCNd3oZWp4bBdf5o6Jo-lLORvb1_Ag2vPUsY5V6DA0dzc-UpmQ7uAir4z_p-z0UcST8jHGsZzIjG6yhVdbPlHrgdwm9VmVcMNJBOsAfyfoXMBGP0BarXJPydPpXtn8G7HBGxcjL9Xy5tQqURB07V23QpuVuS4Kq3p-0tOkfVkZdE2PCbtsALIDebYz8JSccg1Ext8faQd7d36hBLY4-QubVma--qJQObBXYAr-JPT8xmmLQB3rPyflfoVdL1spc3h0WAOrqm8GrtqSlDHi6PLMiJYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b99256aa.mp4?token=GP86JqzhpH0MyRyt1iQqs_zCpj5TMjiOseUvg3fOchqI9ArFTuanIZV5JbSQUCNd3oZWp4bBdf5o6Jo-lLORvb1_Ag2vPUsY5V6DA0dzc-UpmQ7uAir4z_p-z0UcST8jHGsZzIjG6yhVdbPlHrgdwm9VmVcMNJBOsAfyfoXMBGP0BarXJPydPpXtn8G7HBGxcjL9Xy5tQqURB07V23QpuVuS4Kq3p-0tOkfVkZdE2PCbtsALIDebYz8JSccg1Ext8faQd7d36hBLY4-QubVma--qJQObBXYAr-JPT8xmmLQB3rPyflfoVdL1spc3h0WAOrqm8GrtqSlDHi6PLMiJYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز عراقچی راهی سفر اربعین است</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454193" target="_blank">📅 14:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454192">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur-fELOY2FZOjdiWhOcLHqegFrlBfnYdXVCn_AVIgjAqEJ_lxmkemhMI8KRFCL5600gFN0pf5lPxEsEjTIun7r6obCun7Z0o4y-AgIpJt_4EJRyKzUd6AA-72uTT9VrhcC1kY6eYhy60XBf6yFXWVPM4-xQ8qBbEggeVQbacmNLkc3UJX7PszIqFHXyyopEuX20N76wETl5iLI7pXgHksMT7_AogbqDAXjn9tv95QPGJF24zhMMH4fLfgZZxVdDYh_Fknm_nphNYKflmcSoIdACmDhsQ50XzGibuhA3BuyzBmvkrUrcugCT2yYn4xzXl4gooGAJblSmWQYWmHhetNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت مذاکره با آمریکای ترامپ بن‌بست است
🔹
نگاه دولت فعلی آمریکا به مذاکره با ایران نه یک نگاه تاکتیکی و نه حتی صرفا راهبردی، بلکه شامل عناصر کاملا ایدئولوژیک است که با نگاهی به ماهیت آن، می‌توان نتیجه هر مذاکره‌ای را از پیش دانست.
🔗
شرح کامل این یادداشت را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454192" target="_blank">📅 14:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454191">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba17c5d31.mp4?token=ir1zNN4T4ZLjrbJ9UZZqEYfGKAPXkUTqK1o2qv3NyD53Iv926j5ULKCZVTFI9P7W-Bjh2NSeD09xR_ZMIkLfs4iGVT378uokkajTrGzukllfkY9H8qqrm6RQFopq1qcWKkwTJ7NyFbwkb8er3lEdP8lJ9t-kF_HRuFGGs2lbZ10psyaZ-VWbx2D0QPG5PRv8R4eqhB66tMt6-mQ6Ov57jQ0UTEuUecdo5ULjrdlSnpDfzt5j-Eqd3AITcwPaqxjWZOXWUbIre4fPGeg29Jmz-ngRCBSMxs36jY9TGi_kW5RYMLACv8q7fl1USoesd302AfUz1Y8g30WSzgWW5U4jKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba17c5d31.mp4?token=ir1zNN4T4ZLjrbJ9UZZqEYfGKAPXkUTqK1o2qv3NyD53Iv926j5ULKCZVTFI9P7W-Bjh2NSeD09xR_ZMIkLfs4iGVT378uokkajTrGzukllfkY9H8qqrm6RQFopq1qcWKkwTJ7NyFbwkb8er3lEdP8lJ9t-kF_HRuFGGs2lbZ10psyaZ-VWbx2D0QPG5PRv8R4eqhB66tMt6-mQ6Ov57jQ0UTEuUecdo5ULjrdlSnpDfzt5j-Eqd3AITcwPaqxjWZOXWUbIre4fPGeg29Jmz-ngRCBSMxs36jY9TGi_kW5RYMLACv8q7fl1USoesd302AfUz1Y8g30WSzgWW5U4jKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر بهداشت: طرح پزشک‌خانواده از این هفته در روستاها اجرا می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454191" target="_blank">📅 14:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454190">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNf30l0NgGlxoHsfBFlCcPj7mKNiaPsjb0r9RO0AzqmQ1mjiWeXe3VuOusHH2MgaxirBb8K47cMXmVRvX80oCSLwyQPcu3CceI00F86fdKI8iZ6RqmOvCPwBmbLFMA5yObpvNYSRwqYo39ngXY74CRnHbAhXpQOfZf278pL3wTmpII0I2xpN3ITasMHh-w4cxxRePBlQmZd_eazUOzb0bBy5-h8_WtUsu_MK54VdyWySyAOMCG_kC1n7NJf3lsSty8Ffqaa8Fz68Bx79mi0X6MTLmuTNUNLZipBAWbYkXW0ghefnfm_vp3vt5wYB63zTzgc1gONxeiA62m1a4pLG6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکورت هوایی آمریکا در تنگۀ هرمز
🔹
پایش داده‌های ناوبری هوایی نشان می‌دهد که هواپیماهای پشتیبانی نظامی آمریکا در خلیج‌فارس فعال شده‌اند.
🔹
پیش از این هم چنین پشتیبانی‌های هوایی هر زمان که نیروی دریایی آمریکا تصمیم داشت نظم ایرانی تنگه هرمز را بر هم بزند، دیده شده بود.
🔹
هنوز کشتی حامل گاز قطر که جمعه‌شب می‌خواست با اسکورت آمریکا از تنگۀ هرمز عبور کند، در بخش جنوبی این آبراه زمین‌گیر است.
🔹
براساس تصاویر ماهواره‌ای، هواپیمای هشدار زودهنگام و کنترل هوابرد آمریکا از ساعات اولیه امروز فعال شده و به‌سمت تنگۀ هرمز در حرکت است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454190" target="_blank">📅 14:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454189">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H46eCeYWJx5GDcOuMpVACoT4RRy1rdBdgK9vKpvklQqyM_bcCUlInHYtcxXNe-HhGQu5xwXAfnk90tWt51RY4JActBJX_-rDzQqTvMkpFVg3H3AfSAXHjW0Uvj4RZrpBycCgTIAuaeIfnMIxUwDxSwkeI5VmvkV8RmizPsHpGjH4spBZKdNxb5lZ-854O7GQcTd64AQ23T_99M2FKprrd2olNTsZ9ie2ZbIoLuG9ouCMJImbkyZnT2Iqrs5wigd0O-i7Dfcpg-eO9fEuBJF452thfyY_LT9JGBmQBbytsa9x935srvacjyOf3bWljntDOhqNE3NclHZA9bG8Hbwqlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک تجارت به کاهش ۱۰ هزار میلیارد تومانی سود پاسخ داد
بانک تجارت درخصوص خبری با موضوع تعدیل صورت‌های مالی این بانک، با اشاره به ابلاغیه بانک مرکزی به بانک‌های کشور در خصوص اصلاح رویه تسعیر دارایی‌های ارزی، به تشریح اجرای دستورالعمل مذکور در بانک تجارت پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/454189" target="_blank">📅 14:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454188">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rom41H-7u4McrLHdUeN-6tOpsjf9-EEu5PvBpKc_5_GfAVSLLGevw-Z08YTHAF5xuPT4IYSeHFRKuHUZBXzu6bj6CDVddVdsWUQm4Zt3s8RZ0MsLDBQaaXhI-6T3yHTnmBK4D781thsvoVT58CutprfO6n0ExNA4PjL0tu_6dfixYliHCHZHh96bt9xc0XwagpkAKFVMbmsB3SBScLOFIOwhUSSNlFK_My6MFoeaqk2tRX1dPbRB7ZPuWunpG2BjrBq5SKlxy33nPDMTf9KlC6pMbiyezaMptYVHI7FEKRXA4SiOF-oPXWOPPiRRh_5WrJ-SAkilAE7zaI03ZeOGvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
فهرست برندگان پایان دوره قرعه‌کشی طرح «فرالیگ» بانک رفاه کارگران اعلام شد
🔹️
با پایان طرح "فرالیگ" بانک رفاه کارگران، ویژه مسابقات جام جهانی 2026 و جمع‌بندی نهایی امتیازات شرکت‌کنندگان، اسامی سه برنده نهایی این طرح اعلام شد.
🔹️
بر این اساس، نفرات برتری که موفق به کسب بیشترین امتیاز در این طرح شدند، جوایز ویژه خود را به شرح زیر دریافت می‌کنند:
🥇
نفر اول: آقای حسن بابالوئی (برنده جایزه ۲۰۰ میلیون تومانی)
🥈
نفر دوم: آقای احمد نصرت‌فر (برنده جایزه ۱۰۰ میلیون تومانی)
🥉
نفر سوم: آقای مسعود نجفی ده‌پهنی (برنده جایزه ۵۰ میلیون تومانی)
🔹️
بانک رفاه کارگران ضمن تبریک به این برگزیدگان، از مشارکت تمامی شرکت‌کنندگان در این طرح قدردانی کرد.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/farsna/454188" target="_blank">📅 14:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454187">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/454187" target="_blank">📅 14:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454183">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df7882a7db.mp4?token=lzWpPsxqm7-hh91PpcpdDtH_3669wVPiXe4Q1Sm-bXLy9Af93Qy8md53d4CbzoAJaeI6RmyyI-Q1zAOr6dyXg6EWLNKjIWxcygd0XmU4BP5qagK5O0IOQwuY0tIDq9lPGVIJBXfAbYUrNtXuRWAwHjPyJwa2iklWyX5qIuyEq_UGvqJbyiivff479XJGxkBF9VrsBLMaiwtdIdOvIOtCbs-ZBKrGiQf0eg4CJvWEPn97h0buBi8ZiBvU3b3YPYHwpr6Sr8mb90Rtf4X6MO0w-AaRpfaTy2BelzT_w5MUy0fJzWLJxfdRIxWTKB9P6qWORCkac0kYSBLLFiQ03zzGXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df7882a7db.mp4?token=lzWpPsxqm7-hh91PpcpdDtH_3669wVPiXe4Q1Sm-bXLy9Af93Qy8md53d4CbzoAJaeI6RmyyI-Q1zAOr6dyXg6EWLNKjIWxcygd0XmU4BP5qagK5O0IOQwuY0tIDq9lPGVIJBXfAbYUrNtXuRWAwHjPyJwa2iklWyX5qIuyEq_UGvqJbyiivff479XJGxkBF9VrsBLMaiwtdIdOvIOtCbs-ZBKrGiQf0eg4CJvWEPn97h0buBi8ZiBvU3b3YPYHwpr6Sr8mb90Rtf4X6MO0w-AaRpfaTy2BelzT_w5MUy0fJzWLJxfdRIxWTKB9P6qWORCkac0kYSBLLFiQ03zzGXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چندین ایالت آمریکا همچنان در آتش می‌سوزند؛ ۶۰ هزار نفر تخلیه و دست‌کم ۶۰۰ ساختمان نابود شدند
🔹
مقام‌های آمریکایی اعلام کردند آتش‌سوزی‌های گسترده در شرق ایالت واشنگتن، به‌ویژه در اطراف شهر اسپوکن، تاکنون دست‌کم ۶۰۰ خانه، واحد تجاری و دیگر ساختمان‌ها را نابود کرده و موجب تخلیه حدود ۶۰ هزار نفر شده است.
🔹
آسوشیتدپرس گزارش کرده که آتش‌سوزی‌های اطراف اسپوکن در روزهای گذشته حدود ۲۱ کیلومتر مربع را در بر گرفته و بخشی از ده‌ها آتش‌سوزی گسترده در غرب آمریکاست که توان نیروهای امدادی و آتش‌نشانی فدرال، ایالتی و محلی را به چالش کشیده است.
🔹
در این گزارش آمده که همزمان در غرب ایالت آیداهو و شرق اورگان نیروهای امدادی برای دهمین روز متوالی با استفاده از بولدوزر و بالگرد در حال مهار آتشی هستند که نزدیک به ۱۳۶۰ کیلومتر مربع از مراتع را سوزانده و بیش از ۶۰۰ خانه و ۸۰۰ ساختمان دیگر را تهدید می‌کند.
🔹
همچنین در مرکز ایالت یوتا، وسعت یک آتش‌سوزی بزرگ در ۲ روز گذشته از حدود ۴۱ کیلومتر مربع به ۱۴۵ کیلومتر مربع افزایش یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/454183" target="_blank">📅 13:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454182">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هرمزگان چهارشنبه تعطیل شد
🔹
معاون منابع استانداری هرمزگان: به‌دلیل تداوم افزایش دمای هوا و ضرورت مدیریت مصرف انرژی تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی چهارشنبه ۱۴ مرداد تعطیل است.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454182" target="_blank">📅 13:08 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454181">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf79599adc.mp4?token=GkzXZk2Amlu_VzCgGp-LmXrTaJvAieZtQU7Jw63TYjhwoIA46Fgr8aOOQ16jpDEVGa9L9gmXWmZLqfXPWq-vFrtwRxO9oj2ZONS7-izIGIZjjdhCJiVPxdymPgosz8xi2aXUWJ5T5Wn1Ha6lD7kX8RLn14tnfWfWYCV0-1upqGiReKJvWRzu00CYajtMfk-DCjeno9La75--Tf5OzymAmIVSqNcM99V3LLERwcVWfFfujs4MpJQxFQeSevhzhPNIdZSSZtGC_C1zGEstoDpZfNynU1lszu5F1aeVgXk5YYz8F2TzYsOUop9piYZ7mVx3R_Qpwl7XQed9LRsFYpHqwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf79599adc.mp4?token=GkzXZk2Amlu_VzCgGp-LmXrTaJvAieZtQU7Jw63TYjhwoIA46Fgr8aOOQ16jpDEVGa9L9gmXWmZLqfXPWq-vFrtwRxO9oj2ZONS7-izIGIZjjdhCJiVPxdymPgosz8xi2aXUWJ5T5Wn1Ha6lD7kX8RLn14tnfWfWYCV0-1upqGiReKJvWRzu00CYajtMfk-DCjeno9La75--Tf5OzymAmIVSqNcM99V3LLERwcVWfFfujs4MpJQxFQeSevhzhPNIdZSSZtGC_C1zGEstoDpZfNynU1lszu5F1aeVgXk5YYz8F2TzYsOUop9piYZ7mVx3R_Qpwl7XQed9LRsFYpHqwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جاسوس موساد: باز شدن تنگۀ هرمز بستگی به خواست ایران دارد
🔹
منشه امیر، جاسوس و سخنگوی موساد: ایران قدرت بستن شریان‌های حیاتی جهان را در اختیار دارد!
🔹
آیا تنگه هرمز باز شد؟ مسلما نه! آیا باز خواهد شد؟ بستگی به خواست ایران دارد!
🔹
حکومت ایران به تاکتیکی موفقیت‌آمیز رسیده؛ آن‌ها می‌گویند ما موشک داریم، می‌توانیم همه تأسیسات کشورهای امیرنشین عرب و اسرائیل را نابود کنیم!
🔹
خبر رسیده موشک‌های پاتریوت آمریکا کم شده است؛ بنابر تمامی این عوامل، ترامپ بار دیگر جنگ را عقب انداخت.
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454181" target="_blank">📅 12:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454180">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKL3xH4SAV8yjlp4bECHrZexYgzZdU4z7Qqu3T5ioXkJYRrYz_YZkmhXlQNwiJVHPvExIu_7yj-2m_KCBFPrEWJbSUszKZbXuE58qzW_v2iR9c6Ud6kCSkrNV8vJJuX5MVNeDnwQ4_9RBbJ6FjjWeH3JmD14zcRjit1u7BKo8z_SNwg7FJth52No97n4Ev7RBwAuoQjAiUcsIQNpVG9fXyXzLDdJulV-ETSJFaGf0knHtSIW6GmV7aOslAIjXNATS94XeVbGt_UfctoLbqTRzkW2OhZ8ar8lQlYxJHp8nb0qNPDc5e9TVt4Z2BmROLW_qk7ROr_zc5v9maThoGK9vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامهٔ جهش‌های سه‌رقمی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۳ هزار واحدی به ۵ میلیون و ۲۷۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454180" target="_blank">📅 12:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454179">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJiV8PuUgvZOeZFTykPQWyx7GuyVZrxdPrWTHKtZCWGdd_D7VujDzr3xJAOgUVsLuIBSBMydWntkAO4LrYDpPsVbWFMIWYaERVgSQBkakFCJfQvrk3frIbIf_6qp6v_6kooNJkNODoDbwOAQIAglR2g-Oy77wl-KorO2MbGNEl9xZNfPDnHNA4cqAKPInavqSutmwdx1_-9ZjnnCRLO-2LidMY67YJKB5hdw-xSTl-p2reXND1Kld2n7AgcumCG5iU5Z1aoWvImEtukHpYVR7Xj4yN3GyuLQlfzCNOW9EPVYtEzklrbKTVWV3jJ0BaA1oToX_sfcdi7jEowkLtHcTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انهدام پهپاد MQ9 بر فراز تنگه هرمز
🔹
یک فروند پهپاد MQ9 توسط آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه بر فراز آسمان تنگه هرمز رهگیری و مورد اصابت قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454179" target="_blank">📅 12:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454178">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUhCxWgeOJennZpmAOFDFs07hNY808AVktz7Y1fDmqKXvMbF3skI0BHeZNfU3iT28sRrYAVSlQuBit_gWLy-cbl-cXDEK-jE4b02OsHDG-F4DAY2XatYcUygd35EMyeiOF-P-M9vWHJ-1wkt1TvG0nYPtByVqaHee94V7OCiJSSJrFBzBKHMrf-VUt3U8JpXXVInkr4FAUq71twg0hhaiNYJfqsznuEbVyVZfa6RG4ZzE9AD2GO--NVSrWWWDuE9vNmhlvHsUqeePKzEQkySRw-PCGySzusxc7ISIp5exSSXVOitJilOQdb4Q3sRapIe18m-BAHWDk2CwO4GWpYm5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن ۶ نفتکش سعودی را به مارپیچ آفریقا انداخت
🔹
تصاویر ماهواره‌ای و داده‌های ردیابی دریایی نشان می‌دهد که دست‌کم شش نفتکش حامل پرچم سعودی، مسیر خود را از تنگۀ باب‌المندب به‌سمت دماغۀ امید نیک در جنوب آفریقا تغییر داده‌اند تا از حملات نیروهای یمنی در امان بماند.
🔹
پیش از این و با بسته شدن تنگۀ هرمز، عربستان بخش عمدۀ صادرات نفت خود را از طریق خط لولۀ شرق-غرب به بندر ینبع در دریای سرخ هدایت می‌کرد و این مسیر به تنها راه باقی‌مانده برای صادرات نفت این کشور تبدیل شده بود.
🔹
حال با تهدید این مسیر نیز، نفتکش‌های سعودی ناچار به انتخاب مسیرهای دورتر و پرهزینه‌تر برای رساندن محموله‌های خود به بازارهای آسیا هستند.
🔹
براساس گزارش ویندوارد، تغییر مسیر نفتکش‌های سعودی هزینه‌های سنگینی به‌همراه داشته؛ به‌طوری که زمان سفر در مسیر تایوان به بندر ینبع از ۲۴ روز به بیش از ۵۶ روز رسیده و هر تردد را ۲ تا ۲.۵ میلیون دلار گران‌تر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454178" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454177">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18286dd58.mp4?token=TLBZ3-QAOp8sUkpwYUfb_0cLuJdMP1cb4RicwvvmdLSUSqM0lDnfWk4jfYcpCJ7EXrxof6QT_A8iFGD09O-W3Esbp2wxSCRlmb-hiU_Qd1G2IgJm_3YUNnz9fNxCBNc9OE5quVECw7sFKP3ZUrs9q-Nyv6uHuXEkvyMZUox-WdrFIVrG2vxxmpp8DSqoQ4YpzD0yIhgDBaEtExu-DRZMGkoLnDyYNNsFfxgI3OWwjoFJtdZaUL7YmE3qSDwzgIHl0xPdO7XZ7TKzN3rwGVeceocHoOsFgyCX76VRPjGaPcKa_nS1gj739cEVjFDJDcNL8mLQS6ei9uu4Xn6Gl0CXsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18286dd58.mp4?token=TLBZ3-QAOp8sUkpwYUfb_0cLuJdMP1cb4RicwvvmdLSUSqM0lDnfWk4jfYcpCJ7EXrxof6QT_A8iFGD09O-W3Esbp2wxSCRlmb-hiU_Qd1G2IgJm_3YUNnz9fNxCBNc9OE5quVECw7sFKP3ZUrs9q-Nyv6uHuXEkvyMZUox-WdrFIVrG2vxxmpp8DSqoQ4YpzD0yIhgDBaEtExu-DRZMGkoLnDyYNNsFfxgI3OWwjoFJtdZaUL7YmE3qSDwzgIHl0xPdO7XZ7TKzN3rwGVeceocHoOsFgyCX76VRPjGaPcKa_nS1gj739cEVjFDJDcNL8mLQS6ei9uu4Xn6Gl0CXsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاور پیشین سازمان جهانی بهداشت: کووید ۱۹، ساخت آمریکا بود
🔹
در حالی که آمریکاییان بارها گسترش کووید ۱۹ و همه‌گیری بیماری کرونا را به گردن چینی‌ها انداخته‌اند، اکنون جفری ساکس، استاد دانشگاه آمریکایی اذعان کرده که این پژوهشگران ایالات متحده بوده‌اند که با دستکاری در ژن ویروس‌های کرونا، ویروس کرونای جدیدی را ایجاد کرده‌اند.
🔹
به گفته جفری ساکس که ریاست کمیسیونی در سازمان جهانی بهداشت در زمینه کووید ۱۹ داشته، پژوهش برای دستکاری ژن‌های ویروس کرونا، «با تأمین مالی مؤسسه ملی بهداشت آمریکا (NIH) و توسط یک تیم تحقیقاتی در دانشگاه کارولینای شمالی انجام شده است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/454177" target="_blank">📅 12:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454176">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPlab_Ye0wkV4toP4dLT9ZT9PnBm4P1sg5zxpTCfETF2gVlD45ZJTVY0X5yJHNCxUWApB7qx1Ik2zaXmofnHRKZn2ElWUHnrKWGKzMZKZLUxCZXyxXx3KgAO45KW5YLfGaowG_DTzlOYBcoYZXxZJucDt6OSl5oWOMQ4Mdy16tELQxPnByLh_X5qYkB1CAVadIc5sR5vSBy_NFrDviIbli6M6s9GMqO68NSLRROqtBqeQJESKccxwD7nFTGx1FkFrrlhadZDpId79_ctrqjirxV3J3dyY1f1XredoMqtPb6kkuD8qE_q2thUOCuHTgj1lsOJDjkMtH61h_glXmT7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
روایت محمدصادق لواسانی؛ خبرنگار فرهنگی سینمایی از پخش یک سریال متفاوت در شبکه سه
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/454176" target="_blank">📅 12:17 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454175">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12bacc8c1f.mp4?token=VgGQrZS6KyAt_9C4AafR1XAP1rBqbSNlRXrJp1R_F5aiiYAe2BBpyFEhfQZ82B2-9L9s4N827PoZWmWVNVbRoZMYb-gthOzjfTVgX-vdWCuIIxJpxmJt8f_4cy_queoaM2MBRhFm9etjBCh9SVlQyoVAu6zplBBJMRy99yr9smvmANl3kgjnd0q_y9PjgBvGpvcRSFis1qNw3zntsxmjlGM2UBLKjuXPKm834OBFCTGnP0UIw5ld0-k-orp8nw0Q5axsWy-uRu7YSPZlkFUoTx9fjR6wHiomxtb1HHJlVhvMDf0Zg5U7WO3OILF94geV4rgqz9XCceBaMs5OLsbCKA09EdhfXwxCfC3MO0w2txBgx1rQUioAdZJ38nn4aM22flreCmdY7W6kRp6YTreYqkXphsQHDkRY46HsmV_AJPeMRixD2GYfvq8KNADQsTyQBrdIh3Tb2vJt9GAPssLm9g-R9Ikfo3yigF3Xx7D-xqqCItbbqXstWxsodX09O2TbE87bHU0012_pjXcdrwQ97kWKniU-zisgpzSMMXqTOwZ6j1wQ2kleFqWj_AtAN3R4a7sVI1Io1l-S3mt1JjawDAE-FJf2Lyp39XlhziBYtiHtZHHue6v_TZE6mzr8JfHPJA7IeeXjF7_NXqAIdy7Q9QjvZTcbT5uG_WRSjqCOcpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12bacc8c1f.mp4?token=VgGQrZS6KyAt_9C4AafR1XAP1rBqbSNlRXrJp1R_F5aiiYAe2BBpyFEhfQZ82B2-9L9s4N827PoZWmWVNVbRoZMYb-gthOzjfTVgX-vdWCuIIxJpxmJt8f_4cy_queoaM2MBRhFm9etjBCh9SVlQyoVAu6zplBBJMRy99yr9smvmANl3kgjnd0q_y9PjgBvGpvcRSFis1qNw3zntsxmjlGM2UBLKjuXPKm834OBFCTGnP0UIw5ld0-k-orp8nw0Q5axsWy-uRu7YSPZlkFUoTx9fjR6wHiomxtb1HHJlVhvMDf0Zg5U7WO3OILF94geV4rgqz9XCceBaMs5OLsbCKA09EdhfXwxCfC3MO0w2txBgx1rQUioAdZJ38nn4aM22flreCmdY7W6kRp6YTreYqkXphsQHDkRY46HsmV_AJPeMRixD2GYfvq8KNADQsTyQBrdIh3Tb2vJt9GAPssLm9g-R9Ikfo3yigF3Xx7D-xqqCItbbqXstWxsodX09O2TbE87bHU0012_pjXcdrwQ97kWKniU-zisgpzSMMXqTOwZ6j1wQ2kleFqWj_AtAN3R4a7sVI1Io1l-S3mt1JjawDAE-FJf2Lyp39XlhziBYtiHtZHHue6v_TZE6mzr8JfHPJA7IeeXjF7_NXqAIdy7Q9QjvZTcbT5uG_WRSjqCOcpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎬
#تماشا_کنید
💠
رونمایی از طرح «
کیف پول مهارت - کاراکارت
»
با مشارکت بانک تجارت، سازمان فنی و حرفه‌ای کشور و شرکت کارت اعتباری ایران کیش با حضور آقای دکتر عارف معاون اول رییس جمهور
✅
کیف پول مهارت یک اعتبار اولیه و محرک است برای کسانی که انگیزه یادگیری دارند اما برای شروع مسیر آموزشی با محدودیت مالی مواجه هستند.
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/454175" target="_blank">📅 12:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454174">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/farsna/454174" target="_blank">📅 12:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454173">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727ab2e627.mp4?token=eJWj2iCi6EWqS-o4SEWLqxbWsa6jmMijoNIb9_1-QIuTpd87uWUtfpeUhhKtbbKvECecX3WzAoxkV9_xwp-O3Yp0ecHXAdtuiw27IAE9W14l8SELF29Y1iGG3DXCwyqIy4-ZGQAkFDtz0ehA0Y4pBRPPFDCO-ddHuMITbTEFEjDr_yFJDAkO65ljERnjNDnbRuvHSNUd1nu_BCoNjll-1TyeJbYaEc5O94OS7zlpvSOr_lvwovIbKgOd4wJfiuDgigi6VCAlYStkmcl6qjj2X36_d2-8yHBsDUoVn3odrw2i8YyxwDtRW-Ic8xHbiCE9Q9wU62yINhgKAmV6XwWADw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727ab2e627.mp4?token=eJWj2iCi6EWqS-o4SEWLqxbWsa6jmMijoNIb9_1-QIuTpd87uWUtfpeUhhKtbbKvECecX3WzAoxkV9_xwp-O3Yp0ecHXAdtuiw27IAE9W14l8SELF29Y1iGG3DXCwyqIy4-ZGQAkFDtz0ehA0Y4pBRPPFDCO-ddHuMITbTEFEjDr_yFJDAkO65ljERnjNDnbRuvHSNUd1nu_BCoNjll-1TyeJbYaEc5O94OS7zlpvSOr_lvwovIbKgOd4wJfiuDgigi6VCAlYStkmcl6qjj2X36_d2-8yHBsDUoVn3odrw2i8YyxwDtRW-Ic8xHbiCE9Q9wU62yINhgKAmV6XwWADw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۴ مسیر ویژه برای زیارت مرقد رهبر شهید ایجاد شد
🔹
با تغییرات جدید و گشوده‌شدن رواق دارالذکر به روی زائران ۴ مسیر ویژه زیارت مرقد رهبر شهید در حرم رضوی ایجاد شد.
🔹
در مسیر نخست، زائران آقا از صحن آزادی وارد رواق دارالسرور شده و پس از عبور به روضۀ منوره مشرف…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454173" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454171">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هرمزگان چهارشنبه تعطیل شد
🔹
معاون منابع استانداری هرمزگان: به‌دلیل تداوم افزایش دمای هوا و ضرورت مدیریت مصرف انرژی تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی چهارشنبه ۱۴ مرداد تعطیل است.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454171" target="_blank">📅 12:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454170">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">هیئت‌رئیسۀ خبرگان: زمزمه‌های تسلیم‌طلبی به اسم صلح، خیانت نابخشودنی است
🔹
هیئت‌رئیسۀ مجلس خبرگان رهبری با صدور بیانیه‌ای ضمن تقدیر از حضور بی‌نظیر مردم در مراسم تشییع تاریخی قائد شهید امت، بر حمایت کامل از مواضع عزتمندانۀ رهبر معظم انقلاب، حضرت آیت‌الله سیدمجتبی خامنه‌ای، تأکید و التزام عملی همۀ مسئولان به رهنمودهای ایشان را خواستار شد.
🔹
در این بیانیه که به‌مناسبت ایام اربعین حسینی صادر شده، آمده است: پیام‌های حکیمانه، بصیرت‌افزا، امیدبخش و عزتمندانه رهبر معظم انقلاب، راه‌گشا و راهنمای مردم شریف ایران و امت اسلامی است و باید نصب‌العین مسئولان محترم نظام قرار گیرد.
🔹
هیئت‌رئیسۀ مجلس خبرگان همچنین با اشاره به زمزمه‌های تسلیم‌طلبی از جانب مرجفون و توطئه‌گران به اسم دفاع از صلح، آن را خیانتی نابخشودنی دانسته و بر مواجهه قانونی با چنین اقداماتی به‌عنوان وظیفه مسلم مسئولان تأکید کرده است.
🔹
در بخش دیگری از این بیانیه، بر ضرورت حفظ اتحاد مقدس و پیروی از رهنمودهای رهبر معظم انقلاب به‌عنوان فصل‌الخطاب و تنها محور وحدت تاکید شده و التزام عملی کامل همۀ مسئولان به نظر ولی‌فقیه، واجب عقلی و شرعی خوانده شده است.
🔗
متن کامل بیانیه را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454170" target="_blank">📅 11:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454169">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f7297b6e.mp4?token=fthllon9GkzzNVlfUleTelCtfN1H61ZhKrYRulCyYSGGagHn-NBrqIehuvFI0WppE9vZ3h2kv1_zbLp1i8PKZNjA1AqRrkGfpX5kMhXTHTaMshAxwOBgzukOX2RD2R0th2KqBuJJAN7fwbyWgUpSKYgF-DosQ1raLIFYDI8I-iXlhhCM5aqvD7a_9e7uo-6C3G__E32kSM4k1JQx9hapJnE7KD9AiiEbu36Y1VPDyiVpIWiEn5kIvx41kDH1x68Fs5p_N8z5p0xhvC6sODyq3CaBGN4UOqdh7R7SdF__tSAbTMfmA4BNC4KbQTQSNZ3jMgjwyaeDt96iEOsSz_iPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f7297b6e.mp4?token=fthllon9GkzzNVlfUleTelCtfN1H61ZhKrYRulCyYSGGagHn-NBrqIehuvFI0WppE9vZ3h2kv1_zbLp1i8PKZNjA1AqRrkGfpX5kMhXTHTaMshAxwOBgzukOX2RD2R0th2KqBuJJAN7fwbyWgUpSKYgF-DosQ1raLIFYDI8I-iXlhhCM5aqvD7a_9e7uo-6C3G__E32kSM4k1JQx9hapJnE7KD9AiiEbu36Y1VPDyiVpIWiEn5kIvx41kDH1x68Fs5p_N8z5p0xhvC6sODyq3CaBGN4UOqdh7R7SdF__tSAbTMfmA4BNC4KbQTQSNZ3jMgjwyaeDt96iEOsSz_iPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجهٔ اوکراین اطمینان داده که حمله به کشتی ایرانی غیرعمدی بوده</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454169" target="_blank">📅 11:43 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454168">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3HvJWcthDygjDARLC-771eSs40Z8yMt7ljQkwjO6jsZCdFzestvgHMLQYnGDWXBGyfV8-gjmve8zXLfTvyWGtgyB8Sjm5_9Q5ZmECVf_MQ8mRmnv3rWm0jrGGE-tijfNWrx6G9DGNzYXYmFLV5s0hjeVfCs_miRPQ5Zey94rJzsV3Aqwh5fn44-fZVayV1UANIltwUztFoAjOHFWOrOOx-J7uDZw0uEaGDwawxplL7ebVC9FctGWy820phRT3XkCjYYsUzsnqY1X1hXth3zv3DMZ2_zY3S3QlBQpO0oVOHd9LkRCAiU5F8OU2krN8_58KIEsmBNiz4zGPdYyaeRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز گوشت را در آمریکا گران کرد
🔹
مارک وارنر نمایندۀ ایالت ویرجینیا در مجلس سنای آمریکا می‌گوید: «قیمت گوشت گاو در آمریکا ۱۲ درصد و مواد غذایی ۴ درصد افزایش یافت».
🔹
اختلال در حمل‌ونقل دریایی از طریق تنگه هرمز دلیل اصلی رشد قیمت از سوی کارشناسان این حوزه مطرح شده است.
🔹
طبق آمارهای رویترز، آمریکا به‌دلیل خشکسالی و افزایش تقاضای داخلی واردکنندۀ خالص گوشت گاو است و سالانه ۲.۷ میلیون تن وارد می‌کند.
🔹
افزایش هزینۀ انرژی،‌ حمل‌ونقل و بیمۀ کشتی‌ها قیمت گوشت وارداتی و تولید داخلی را گران کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/454168" target="_blank">📅 11:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454166">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عملیات انهدام مهمات در شرق تهران
🔹
روابط‌عمومی سپاه حضرت سیدالشهدا(ع) استان تهران: انهدام مهمات عمل‌نکرده تجاوز آمریکایی صهیونی در شرق تهران حوالی محدودۀ پارچین امروز از ساعت ۱۴ الی ۱۶ صورت می‌گیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454166" target="_blank">📅 11:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454165">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca09dbe42.mp4?token=tEvAu80GzpcCNHF2-mERsPxo9jDsXFjEZFs14n5vvSX0DUCFmDooGCajR6ox888aNfqUErCOGZZQFFwJWXJ2ad9WUDVzOOMIkEj8IE3zKTBFSnyug-OiFHmbQMWPjLEtTwpeGRnPvcVESTy0GSldiF7qrQrjBY22bFfuwxaPPlV7Vw5XfUsub1hjKFkjcKTKVwqMNJDaeOkbUKbQwD6hqpe_0evEwtwUxTjmJcOWRWsPp7WTOLJ-D0F5_Oa8C-GPnfXZPCKD8qL0egi_fMSg6PwvYkzUNVL3ClbzlUiVqlIJSxpvF-tuTlqBt_KtMIr5USfVLCEG62wLzzMxAegiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca09dbe42.mp4?token=tEvAu80GzpcCNHF2-mERsPxo9jDsXFjEZFs14n5vvSX0DUCFmDooGCajR6ox888aNfqUErCOGZZQFFwJWXJ2ad9WUDVzOOMIkEj8IE3zKTBFSnyug-OiFHmbQMWPjLEtTwpeGRnPvcVESTy0GSldiF7qrQrjBY22bFfuwxaPPlV7Vw5XfUsub1hjKFkjcKTKVwqMNJDaeOkbUKbQwD6hqpe_0evEwtwUxTjmJcOWRWsPp7WTOLJ-D0F5_Oa8C-GPnfXZPCKD8qL0egi_fMSg6PwvYkzUNVL3ClbzlUiVqlIJSxpvF-tuTlqBt_KtMIr5USfVLCEG62wLzzMxAegiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: به‌تجربه برای ما اثبات شده که چیزی جز اقتدار دشمن را از شرارت بازنمی‌دارد.  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454165" target="_blank">📅 11:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454164">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10fa703e3.mp4?token=jdoi3fDCfjdlAqFqooR4BCIZIJet8SmDdY6jm0RpCK3NkB0CCFLRabUMZmwXSMxIu4FXVnH8F2w47scL-t5sUrnwR9SOct1a5koWueO1JHnelB30ET5QGKzWNuqd8S1EXp0Ayx88oox1Be4bO65nzoYAogTaTR6ySsXCjvw7Cm2lIv9VSN3uSf530LyerfXyA6vgLcpjNuEXHMGjpkCIBImwhk8IN-3vxHAjy4vmMK2ihHRXyDzMwUcyA41GedJDJV4tiIo2K8p8zV3WwnKcxW5bj5mh7XfkOcsi4kwmQqlJ9nScAxgaVJC0x5jsCKCLZ3jHX9OtHEDJTkM3CurrQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10fa703e3.mp4?token=jdoi3fDCfjdlAqFqooR4BCIZIJet8SmDdY6jm0RpCK3NkB0CCFLRabUMZmwXSMxIu4FXVnH8F2w47scL-t5sUrnwR9SOct1a5koWueO1JHnelB30ET5QGKzWNuqd8S1EXp0Ayx88oox1Be4bO65nzoYAogTaTR6ySsXCjvw7Cm2lIv9VSN3uSf530LyerfXyA6vgLcpjNuEXHMGjpkCIBImwhk8IN-3vxHAjy4vmMK2ihHRXyDzMwUcyA41GedJDJV4tiIo2K8p8zV3WwnKcxW5bj5mh7XfkOcsi4kwmQqlJ9nScAxgaVJC0x5jsCKCLZ3jHX9OtHEDJTkM3CurrQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مذاکره‌ای با آمریکا نداریم
🔹
مذاکرات فعلی ما با عمان و متمرکز بر مسیر تردد ایمن کشتی‌رانی در تنگهٔ هرمز است. تلاش داریم در اولین فرصت با همکاری عمان مسیر موقتی را تعیین بکنیم تا براساس آن بتوانیم ایمنی کشتی‌رانی در تنگهٔ هرمز را فراهم…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454164" target="_blank">📅 11:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454163">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89df9c9324.mp4?token=EZmnxRFzCO2W-US3d1Itpm649b4F76c_l8Ljsbi0iOPQDjY5-KvZevNKKJxaXVjRqjP61xBVijtR9KhOImsKW4jylfMHQx9UmnKdDjKWkdpPRtXhIYvgydtcXq7e0cBvskihaAOOTNBiAdus2w7kFD4kzt3dRa6k48UdnjyME_sWlihGwBLduhIaD9JBgSVzEsYvVzcSvvmhDlmtaHCHpJzvWsfFsotHmXj_ceqN2frZbjNbieXK8Xgyt3lqDayUzwEoeoi4wGbZmFnqjTWvG98bcZuBaYXayzHtjhHn9Pupd520ul8F8-0ncke4rfNeA8PFEYaF8rbY_oP7RAj47Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89df9c9324.mp4?token=EZmnxRFzCO2W-US3d1Itpm649b4F76c_l8Ljsbi0iOPQDjY5-KvZevNKKJxaXVjRqjP61xBVijtR9KhOImsKW4jylfMHQx9UmnKdDjKWkdpPRtXhIYvgydtcXq7e0cBvskihaAOOTNBiAdus2w7kFD4kzt3dRa6k48UdnjyME_sWlihGwBLduhIaD9JBgSVzEsYvVzcSvvmhDlmtaHCHpJzvWsfFsotHmXj_ceqN2frZbjNbieXK8Xgyt3lqDayUzwEoeoi4wGbZmFnqjTWvG98bcZuBaYXayzHtjhHn9Pupd520ul8F8-0ncke4rfNeA8PFEYaF8rbY_oP7RAj47Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مذاکره‌ای با آمریکا نداریم
🔹
مذاکرات فعلی ما با عمان و متمرکز بر مسیر تردد ایمن کشتی‌رانی در تنگهٔ هرمز است. تلاش داریم در اولین فرصت با همکاری عمان مسیر موقتی را تعیین بکنیم تا براساس آن بتوانیم ایمنی کشتی‌رانی در تنگهٔ هرمز را فراهم بکنیم.
🔹
تا زمانی که شرارت و محاصره توسط آمریکا ادامه پیدا کند، وضعیت تنگهٔ هرمز تغییر نخواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/454163" target="_blank">📅 10:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454161">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjrDo3Wt1moLj0ykARyWeQ0mvRnWUCe8Nw7Cy3sz2xN_d9YACzRs4y6tvPEQfB2yc1Rgk2EzyVv3qFsIM0Xz5g50pHGb7iCciRO9EiuDA6KBErCPBuS7hKoFehBg08XC0YKbHkznEbmoRbAajThGsSzOHrVjoM-FRajMVl7pTyPrQ55E-RCnR24iHc5j76M7TwzUIbd_A81ZcRSuq8rR1Kvkyc7I0FpYJP_gVRwq6WcBi63jxNDRMitQai5CILs6VdpWJx8C6XxkqjW699DbkN2SgwCoiVNMdYYd19dNWPitB8aR7izIxC_Y3y5HU4pQ0H_ebyEIshF4DQQpw_0dtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wi92PVOVZtdl6wA_jseSG08hcsEeD8gPaX3S7e3y0D5hqwuvx-fUyzMb6y6TpwZshZfOkr6r5hui-cuKWZh8tffntxXJfwGgQmLZ-kjgV0yOEJyBBZjpS-kFro0A1Ybo9PDWUop2O2G5f-6gXx2rkIUpzF1MsBdtBoeeQIdfb-dEdUO54cQsalA574ajHlXLzjPtLrRqIWtAYa3FjkfwwrhPo2P8BlWPID83udOjxnPJfUj6eUDSCtcXavsY4mwa69XEWXtJtpsZQPH_cS3W8CTtbBEKMiRGuQYti9Cqesd8hEngGjzQT9U7L9mYoaGtFaChJF0z12rV6Bnun1G4Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۲ بانک صاحب نیشکر هفت‌تپه می‌شوند
🔹
هیئت واگذاری واگذاری سهام دولت در شرکت کشت‌وصنعت نیشکر هفت‌تپه به دو بانک ملی و صادرات را مصوب کرد.
🔸
پیش از این سال ۱۴۰۱ شورای‌عالی هماهنگی اقتصادی سران قوا با واگذاری شرکت نیشکر هفت‌تپه برای افزایش سرمایه بانک ملی و پرداخت بدهی‌های دولت به بانک صادرات موافقت کرده بود.
🔹
طبق مصوبۀ هیئت واگذاری، ۹۵ درصد سهام دولت ۱۰.۳ هزار میلیارد تومان قیمت‌گذاری شده و قرار است به‌صورت مساوی به این دو بانک داده شود.
🔹
شرکت هفت‌تپه در حال حاضر از شرکت‌های زیرمجموعۀ سازمان گسترش و نوسازی صنایع ایران (ایدرو) است و ۶۶۶۸ نفر به‌صورت رسمی، قراردادی و فصلی در آن کار می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454161" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454160">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9d889b23.mp4?token=kRrGrWY5yCAUHPODIhWwliRAEg4kNkC9SAhq3TV83osYrFjwL2O_XJWKxNJo1Eb5XyD_uL9WBw3qXSAYqFbPwb90D2F8VEckQWu-CiYR7kBRgndoIats_gcseKoEf84pNRcLKj4Wg-2m6TWzne2FA3FOuBdx1Cblx5gGKsABbbckYX_jbWlx8jJnX6mLBdUrkaZCFbVZicBceTDkWvfDh7AtB5G_ksXZI5izhDeh-pwq59YriCCn6gzVcQlbvWdgJ0CYF-Xts-serQkZMTU8tqBk2o5gBjXuKwf_CyxVug5ik33vI2T8cwUEYqvkDMDPegeL-XXze7gMPBrNWt_1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9d889b23.mp4?token=kRrGrWY5yCAUHPODIhWwliRAEg4kNkC9SAhq3TV83osYrFjwL2O_XJWKxNJo1Eb5XyD_uL9WBw3qXSAYqFbPwb90D2F8VEckQWu-CiYR7kBRgndoIats_gcseKoEf84pNRcLKj4Wg-2m6TWzne2FA3FOuBdx1Cblx5gGKsABbbckYX_jbWlx8jJnX6mLBdUrkaZCFbVZicBceTDkWvfDh7AtB5G_ksXZI5izhDeh-pwq59YriCCn6gzVcQlbvWdgJ0CYF-Xts-serQkZMTU8tqBk2o5gBjXuKwf_CyxVug5ik33vI2T8cwUEYqvkDMDPegeL-XXze7gMPBrNWt_1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر جدید از لحظات اولیۀ حمله به مدرسۀ میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454160" target="_blank">📅 10:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454159">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">احتمال شنیده‌شدن صدای انفجار در اصفهان
🔹
سپاه صاحب‌‌الزمان اصفهان: امروز تا ساعت ۱۴ احتمال شنیده شدن صدای انفجار کنترل‌شده در محدودۀ صفه، بهارستان و اطراف آن وجود دارد و جای نگرانی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454159" target="_blank">📅 10:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454158">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmkmaCrL9a4d8hDeXgPIdalpyRaKM3_wMVFKkggdscym3_aKRVcR2_AtrXzUqnxw7d_DV_rIcscetrgkwg3sm8vJlFBECJmdphcE8p4yjQnuuoRLiOGqmw-fVEJXUSaJjIIZwT3hFD_qH0U51JTBB0HfE54VWhnmXC8l1huNJ7TmAzYEVI7cMp_BkCPEWbIsEgZmJiUCMTNtJkHj-bBPfQCN78hXF292k5SHFaEBU51TliokH_EUcPQRt43v57JrDjV_OWVgr8E6SJRp1BqyHs1dUxhl3U_rQcrXv-fW6WEA3Y95oZPtywsV5NnfN9dAmb-4fkyzxJJ9aju-ghdMYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: قدرت‌سازی در بسیج ارمغان شهید سلیمانی بود
🔹
فرمانده قرارگاه خاتم‌الانبیا با حضور در منزل سردار سرلشکر شهید «غلامرضا سلیمانی» رئیس فقید سازمان بسیج مستضعفین، با خانواده معظم این شهید گران‌قدر دیدار و گفت‌و‌گو کرد.
🔹
سرلشکر عبداللهی: قدرت‌سازی در معماری جدید بسیج و تبدیل بسیج از یک نهاد صرفاً عملیاتی به دانشگاهی برای پشتیبانی از کیان ایران بزرگ‌ترین ارمغان رئیس شهید سازمان بسیج مستضعفین بود.
🔹
شهید سلیمانی با برنامه‌ریزی دقیق، توانست بسیج را به دانشگاهی مهارت‌آفرین و شبکه‌ای تخصصی برای پشتیبانی از کیان جمهوری اسلامی تبدیل کند.
🔹
آنان که با جنایت و ترور به‌دنبال توقف این مسیر الهی بودند، امروز می‌بینند که بسیج و جبهه مقاومت، به برکت خون پاک این شهید و همت والای همرزمانش، روزبه‌روز بالنده‌تر و حماسی‌تر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/454158" target="_blank">📅 10:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454157">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">شارژ مرحلهٔ جدید کالابرگ از پنجشنبه آغاز می‌شود
🔹
مرحلهٔ جدید طرح کالابرگ الکترونیکی از پنجشنبه با شارژ اعتبار مشمولانی که رقم آخر کد ملی آن‌ها ۰، ۱ یا ۲ است، آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454157" target="_blank">📅 10:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454156">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c51d0ea242.mp4?token=ljYLFtqHuDJ0YqOvyAb7rSeo1y_znZaa5zULfPEFKizE6d7QGrpzM4oEv_lo42yLC_dgrFkaYzsNeKV57TNlG_qQtVdVApkDrxtwHnfQaUDFcodvCpjUQLDn7LZ_Vdu073GxSYxLxNt23_6Fc3F_dGrPXoWsxaeTKSWARL2NZpJXKjNxlHYQs1uOuIZp1LKC-LgDGUeTzW_mLHJlDrZwXdjMBaX1U0IdhakL4u4CMuV7PfXZkk0tj6dBLZE-6BbVjcVxuHv2cibF_6dRw0xDxYhrv9ym1XuZdUEhLHZwJP-STUFZ9TvbAwAx59RGjmbbvYClI1qTXY9HnKzGs9GV5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c51d0ea242.mp4?token=ljYLFtqHuDJ0YqOvyAb7rSeo1y_znZaa5zULfPEFKizE6d7QGrpzM4oEv_lo42yLC_dgrFkaYzsNeKV57TNlG_qQtVdVApkDrxtwHnfQaUDFcodvCpjUQLDn7LZ_Vdu073GxSYxLxNt23_6Fc3F_dGrPXoWsxaeTKSWARL2NZpJXKjNxlHYQs1uOuIZp1LKC-LgDGUeTzW_mLHJlDrZwXdjMBaX1U0IdhakL4u4CMuV7PfXZkk0tj6dBLZE-6BbVjcVxuHv2cibF_6dRw0xDxYhrv9ym1XuZdUEhLHZwJP-STUFZ9TvbAwAx59RGjmbbvYClI1qTXY9HnKzGs9GV5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲ عامل صهیونیست‌ها در جنگ‌های ۱۲ و ۴۰ روزه اعدام شدند
🔹
امید بهزاد و پوریا صفوت، ۲ مزدور رژیم صهیونیستی که در جریان جنگ رمضان و جنگ ۱۲ روزه با ارسال مختصات، تصاویر و اطلاعات مراکز نظامی و امنیتی برای افسران موساد و کانال‌های ارتباطی وابسته به این سرویس جاسوسی…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/454156" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454155">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ5J5BQpJUGSZGRhENu2Y5q5EqbZOJtwBq20LISYmkQsFGnNDQ_6VaGmTnXdGMD0lm9fl6r9oZemphfKE1oNP7shCezy15Yvz4FiSgdbsrJw5wLuahhomebcKUzrV9ALBH2wI5nZw5ciJ__VjfX47UIe450_6bEppQOKHLMD3IU8InCisPkaCAqkOD_3R1uhODahPH1q5q1GV7qlsfK75xcdp3yqXfbVpIGdVJ_0SmvPPKLNPY2bZM4E_wVuVvdRJRcB1OWFZBwct4wJZSEcpxk6QIvP32BBgJy8h1bUi6eq_Pca3zeYJL874IHzsflY1GLB-QIeBPfYQm6r-b_T8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رقابت شدید روسای‌جمهور آمریکا برای فحاشی
🔹
نتیجه یک مطالعاتی تحقیقاتی نشان می‌دهد که استفاده رئیس‌جمهور آمریکا و مقامات ارشد آمریکایی از الفاظ رکیک، طی دهه اخیر روند صعودی گرفته است.
🔹
طبق تحقیقات استاد علوم سیاسی دانشگاه کاردیف جوزف فیلیپس، ۸۷ درصد از کل موارد فحاشی علنی روسای جمهور آمریکا از سال ۱۹۱۹، فقط طی دهه گذشته ثبت شده است.
🔹
طبق نتیجه تحقیقات او، اکثریت قریب به اتفاق موارد فحاشی در انظار عمومی (۷۸ درصد) توسط دونالد ترامپ و جو بایدن انجام شده است.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454155" target="_blank">📅 09:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454153">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e9b676cc8.mp4?token=Z0-60A9DPedE8cFkYfkZuWU6_EDaBozoNKlDInHLcgVbmOGZRFg4KNLneIP8moHB-DPbjaQic7PKgU6ipXCQlr63dyQ1zCXwdqU9S99OSUltQO8ilwDAF01-Xdg1Kq-1L1I9Fy-4njubB6ad34EY5jgVHjeBKLfG06kJC3beXlLAt0kO_Mse_GPe_rxSyMTvdzGSWQkilEwPK-RTN-Bxlx2d_DBNSr9RXGMxwUz6LIZzA6Oy5e958UBr51rqRT6ooSwWGb1HBFkG6PmzGHTDwQDE07vodBUMQgXmCjHEJUfAZ0qIvuLH6lmDzOSauayKj3fpvpCp5aIMaVOmOfTMnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e9b676cc8.mp4?token=Z0-60A9DPedE8cFkYfkZuWU6_EDaBozoNKlDInHLcgVbmOGZRFg4KNLneIP8moHB-DPbjaQic7PKgU6ipXCQlr63dyQ1zCXwdqU9S99OSUltQO8ilwDAF01-Xdg1Kq-1L1I9Fy-4njubB6ad34EY5jgVHjeBKLfG06kJC3beXlLAt0kO_Mse_GPe_rxSyMTvdzGSWQkilEwPK-RTN-Bxlx2d_DBNSr9RXGMxwUz6LIZzA6Oy5e958UBr51rqRT6ooSwWGb1HBFkG6PmzGHTDwQDE07vodBUMQgXmCjHEJUfAZ0qIvuLH6lmDzOSauayKj3fpvpCp5aIMaVOmOfTMnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: امروز در مازندران، گلستان، خراسان‌شمالی و ارتفاعات شرقی البرز شاهد بارش هستیم.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/454153" target="_blank">📅 09:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454152">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">۲ عامل صهیونیست‌ها در جنگ‌های ۱۲ و ۴۰ روزه اعدام شدند
🔹
امید بهزاد و پوریا صفوت، ۲ مزدور رژیم صهیونیستی که در جریان جنگ رمضان و جنگ ۱۲ روزه با ارسال مختصات، تصاویر و اطلاعات مراکز نظامی و امنیتی برای افسران موساد و کانال‌های ارتباطی وابسته به این سرویس جاسوسی کمک شایانی به آن‌ها در رسیدن به اهداف خود کرده بودند اعدام شدند.
🔹
بررسی‌های فنی انجام‌شده بر روی تلفن همراه امید بهزاد نشان داد او در جریان جنگ رمضان، بار‌ها مختصات، موقعیت جغرافیایی و اطلاعات مربوط به مراکز نظامی، انتظامی و امنیتی را برای کانال‌های وابسته به موساد ارسال کرده است.
🔹
پوریا صفوت، از جمله سربازان نتانیاهو و خائن به کشور بود که در راستای همکاری اطلاعاتی با رژیم صهیونیستی در شرایط جنگی، اقدام به ارسال مختصات مکان‌های نظامی و امنیتی به شبکه اینترنشنال می‌کرد.
🔹
در یکی از پیام‌هایی که محکوم‌علیه برای موساد ارسال کرده، آمده: فیلمش را هم دارم که از این مرکز دارند به‌سمت پهپاد یا جنگنده شلیک می‌کنند، ولی اینترنت ضعیفه و ارسال نمی‌شود؛ ممنون از شما سربازان حضرت موسی!
@Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/454152" target="_blank">📅 08:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454151">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda4f01039.mp4?token=OqDpfl257Mf9YEzLECz8CG2ZIlbCVXetfVMeljpx9Ug5J8csItzwZH9PZaaJ_LGTeMtrPKzJea2uyeU8ghVUI6-eSzWEj9-2qXdh84pkDbdRvLYPRPSBCbkPlkmiZK4o92GjLUo67zFbUvclDPKTurgVehEMd9VNpyZvicEIYsNJDbQZELqEr9ZuV6pBkah_XOzoLAj3qYOTOoVnUWAJ8HKeRB5Q6d_VGkrdoB2F7PQ410Xas95HxLZxeAPj9VLptbfGt-YVFK9sWt162VQ0MmDQCzVRVow-c2C4wopEK06atefWMgA03QNe_CdpQeMgSpoOc1j1Ki4rDwuADwifCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda4f01039.mp4?token=OqDpfl257Mf9YEzLECz8CG2ZIlbCVXetfVMeljpx9Ug5J8csItzwZH9PZaaJ_LGTeMtrPKzJea2uyeU8ghVUI6-eSzWEj9-2qXdh84pkDbdRvLYPRPSBCbkPlkmiZK4o92GjLUo67zFbUvclDPKTurgVehEMd9VNpyZvicEIYsNJDbQZELqEr9ZuV6pBkah_XOzoLAj3qYOTOoVnUWAJ8HKeRB5Q6d_VGkrdoB2F7PQ410Xas95HxLZxeAPj9VLptbfGt-YVFK9sWt162VQ0MmDQCzVRVow-c2C4wopEK06atefWMgA03QNe_CdpQeMgSpoOc1j1Ki4rDwuADwifCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج بازگشت روان زائران حسینی در مرز خسروی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/454151" target="_blank">📅 07:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454150">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رئیس فیفا با طناب ترامپ به چاه افتاد
🔹
نشریۀ تلگراف از تصمیم قاطع یوفا دربارۀ رئیس فیفا بعد از طرح فروش جام‌جهانی خبر داد و نوشت: زمان اخراج اینفانتینو رسیده است!
🔹
طرح فروش حقوق تجاری جام‌جهانی به شرکت برادر داماد ترامپ، هفتۀ گذشته از سوی رئیس فیفا مطرح شد…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/454150" target="_blank">📅 07:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454149">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d75154934.mp4?token=gLIWuEfkTF-mU0ODxbggWe9SiaNPoPS6D_K3IZZtVM3cVob5m-D6aO1sv_im5opbErGhvHRH2c-jzbqHoJaSyfZSFzRz_k3ilPHUuDA8BDOVtkwESoMt4QagazMtFnFmHVErQ9bMedmUcZcNNOpCUUFIhzDNM5OKKRyXldqi59YBprSeSTVPczHcibXVm89htpbI2oOH3WrwRmXoqF1yeYHMyJ47WXTFEqoSLlj0SCR7l7SknjzswBqG_eREbXeXSRb-7Cll8Kte526hNMlhtez9f6X2gpUxRjLCJxznSDAmaeYI4mzXMeQjHeR3-UB-7_CtBfTZPOiDUXf-abEFvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d75154934.mp4?token=gLIWuEfkTF-mU0ODxbggWe9SiaNPoPS6D_K3IZZtVM3cVob5m-D6aO1sv_im5opbErGhvHRH2c-jzbqHoJaSyfZSFzRz_k3ilPHUuDA8BDOVtkwESoMt4QagazMtFnFmHVErQ9bMedmUcZcNNOpCUUFIhzDNM5OKKRyXldqi59YBprSeSTVPczHcibXVm89htpbI2oOH3WrwRmXoqF1yeYHMyJ47WXTFEqoSLlj0SCR7l7SknjzswBqG_eREbXeXSRb-7Cll8Kte526hNMlhtez9f6X2gpUxRjLCJxznSDAmaeYI4mzXMeQjHeR3-UB-7_CtBfTZPOiDUXf-abEFvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تردد روان در گیت‌های ورودی مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/454149" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454148">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vidcbmN1qiYOzA-ThPf7OWNYptu6RqvqnaH-6qiG3UsA_sxX8n6GB7rSnqZ5LWLOAgnVaOVNNX-IMzyyyCvxIQOO3hYG3Q1L2mL6ejVZfi_9_E__SRDgIDqddYgbI8kbZo8OcnLG6thdmlRJjtVng1zBXJUoUlF8_6j2HuHx9xDYMKgX0GLoi1M501qYHSx7et1k4mtGcL2zlm7B97-7iTD_GBKBsquMapHmmfEp5MMIrrM7HAxhf9SF2_YdG3GblYIl10-6HC07Ql_5P4cc3wyS1ks-rfjFCtkpeZinuDlcxH-sYJsnjKy2l2FmjZi_pLAW_oQQAGQLG3RfWl5wvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش‌و‌پرورش: شیر یا تغذیه رایگان در مدارس توزیع می‌شود
🔹
سخنگوی آموزش‌وپرورش: در مناطقی که امکان توزیع شیر نیست، از کیک‌های غنی‌شده حاوی خرما، نان‌های غنی‌شده و سایر مواد غذایی مغذی استفاده می‌شود.
🔹
تصمیم‌گیری دربارۀ نوع تغذیه در هر منطقه کاملاً تخصصی و با نظر شورای عالی سلامت انجام می‌شود، اما اولویت با شیر خواهد بود.
🔹
اعتبار این طرح برای دانش‌آموزان مدارس ابتدایی دولتی پیش‌بینی شده و امیدواریم با فراهم شدن شرایط، از مهرماه اجرایی شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/454148" target="_blank">📅 06:02 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
