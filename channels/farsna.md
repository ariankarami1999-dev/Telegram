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
<img src="https://cdn4.telesco.pe/file/JfuyMv93vPmWeg1UJk6BDN-jkRcMQYWKhEbql625EKlJm7GhHJzMoVZD1G15vAN_9NC7Rne_-90oE9sJLnTW_3xgkd4CG058IXIiS_sabH2SC6eRxvA7Te9JwkoxqSNbWK7Eph1Ciw202CAb6yn3hQktZk9f5ExbiFIZjrMwuG4ghwzS4bPhwdm4NMmzlCVQU1m_Jp_NcnneUvQClYEm6bKYxd8aI8rlv8jx5qtkfP7BoUr3RFzKrOFU0NNDTt7WNy1fZyMBP63Rd9fNZlr4EORZ5ofW8cdpaaHaUAaGB5z5xS4GjP7mxPSBM9C2f_d9yTqr73mfp9p8ho5o-vvv5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-02 14:31:48</div>
<hr>

<div class="tg-post" id="msg-457939">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎥
وزیر نفت: ۷.۵ تریلیون گاز در جنوب فارس کشف شد
🔹
بیش‌از هفت‌ونیم TCF یا به عبارت بهتر ۷۵۰۰ میلیارد فوت مکعب گاز کشف شده که با احتساب ضریب بازیافت حدود بیش از ۷۲ درصد امکان حدوداً ۵۷۰۰ میلیارد فوت مکعب استحصال گاز وجود دارد.
🔹
این میزان گاز معادل این هست که…</div>
<div class="tg-footer">👁️ 29 · <a href="https://t.me/farsna/457939" target="_blank">📅 14:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457938">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات فردا در جم
🔹
سپاه جم: احتمال شنیدن صدای انفجار ناشی‌از خنثی‌سازی مهمات از ساعت ۶ تا ۱۸ فردا وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 349 · <a href="https://t.me/farsna/457938" target="_blank">📅 14:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457937">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a612469ccf.mp4?token=C9kDtMzjL9wwhjpolvqiG_QAel1GfBYzhrLUFVVv0E28oSecH4X5mnCAehDvJ7t5_BND3o4OjaGYFYDOWVu6pEnfXMLCL3MpcJNcKZg9fasMI1YsZ-QeafMDf9nodujcDnNCky9_BXjOXRRGpvBfoMvJWiyz4PJHDRs63bz-zmGN6z3oqUCwBJgJ-K2DlMczmfzuPd4kLYMRZrO88x_3w1jGJa5rFMBPe-Szd2a84-ilWJqqnNQqr28foEmWkDWAJXKgD6tylpqlDrfnCB4dx2u-ugCT32yMmbITaESqQyhKPExZkf4YevZf1qASwKL6Cg073X9Mvj0slHqPMD98aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a612469ccf.mp4?token=C9kDtMzjL9wwhjpolvqiG_QAel1GfBYzhrLUFVVv0E28oSecH4X5mnCAehDvJ7t5_BND3o4OjaGYFYDOWVu6pEnfXMLCL3MpcJNcKZg9fasMI1YsZ-QeafMDf9nodujcDnNCky9_BXjOXRRGpvBfoMvJWiyz4PJHDRs63bz-zmGN6z3oqUCwBJgJ-K2DlMczmfzuPd4kLYMRZrO88x_3w1jGJa5rFMBPe-Szd2a84-ilWJqqnNQqr28foEmWkDWAJXKgD6tylpqlDrfnCB4dx2u-ugCT32yMmbITaESqQyhKPExZkf4YevZf1qASwKL6Cg073X9Mvj0slHqPMD98aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خورشید هفتۀ دولت امروز بر ۴ استان کشور
تابید
@Farsna</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/farsna/457937" target="_blank">📅 14:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457936">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGJQ5FJrR7ozKyTBBePyGiD0DcCLwWiCmi9o1mfsTpW4EHv2Bk6Nqo_vM36GI5xIn73Z2TzPdykYTXKDIeYZJ0qWnCP1-x9zs08b4LCDDL8oaZeyR2V_5UBOV3ycyuWRZN5gx4yZTIattezbsd3CQOzBHZcX36P8Fx9DCNw5T7cQd7URBI17bPCeCacPIM1rDMNv7fSVFcsRZBk4nGJl6yYBDWU41L4lqAQRsszYJe1CrbeiZpSFVyH_GhKBPsfA3v5Ryl7ZII1-epXM2AP7R5L-y533IMVI9FHAIN-CaXKscceIrXzidHaoMRjagjvxlTBJbkV4PaQMYQd2Vb6scA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ رقیب جنگی‌اش را عوض کرد
🔹
رئیس‌جمهور آمریکا پس‌از جنگ ۴۰ روزه بار دیگر سیاست فشار حداکثری علیه ایران را با کلیدواژهٔ «Economic D-Day» دنبال کرده و از تحریم نفت، انتقال پول، صرافی‌ها، شرکت‌های پوششی و شبکهٔ کشتی‌رانی و مالی خبر داده است.
🔹
با این حال، بخش مهمی از این تهدیدها هنوز در حد ادبیات سیاسی است و برای اجرای واقعی به سازوکار حقوقی و اجرایی نیاز دارد.
🔹
بسیاری‌از این ابزارها پیش از این نیز علیه ایران استفاده شده‌اند و اقتصاد کشور طی سال‌ها با تحریم‌ها سازگار شده است.
🔹
آزمون اصلی ترامپ، توانایی آمریکا برای وادارکردن شرکای ایران به‌اجرای تحریم‌هاست که در این میان چین به‌دلیل نقش مهمش در خرید نفت ایران اهمیت ویژه‌ای دارد.
🔹
از سوی دیگر، ترامپ با ایجاد نگرانی در بازار و فعالان اقتصادی تلاش می‌کند بخشی‌از اثر تحریم را پیش‌از اجرای آن ایجاد کند.
🔹
بنابراین پاسخ ایران باید علاوه‌بر حفظ موضع قدرتمند در برابر فشار خارجی، بر اصلاحات داخلی، افزایش بهره‌وری، کاهش رانت و مدیریت ناترازی‌های اقتصادی متمرکز باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/457936" target="_blank">📅 14:17 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457935">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYI2iyfYDnjfY7lw0KlXDYujvQKEjM46OkSj74ZvovrYY_lALIFg68St5z3fa2XM3d3zL1WSP0N0CbpR6n0HcJBKLRRL4b1jklwEGexFi0VXVBUr7j2CihC23BqX9LcnkXFTrMK3Sh13l_SGuHros5Y75D23XY363ElEmh6Rsno2NEnT4nRegklpHbE1lYOxvxXXIc18WcPzROOelQia6nAe6awxYC8CAiZvW0_OfGUOV-TuA3Tvs1MBhr5RPl-xzBzHTxvlFL3IenN9W2bfqBHU5MGfFtvxyhvBlfxbrLHfGtlQef_IesAScTVHn6nt-E6R0ppMbZ6TrlEmlV_DdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۴ ریشتر در عمق ۸ کیلومتری زمین، پل‌ سفید مازندران را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/farsna/457935" target="_blank">📅 14:12 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457934">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7420f2b14d.mp4?token=MMsCAGTnO8Ib2IdfvpfI8bsSyBMtjtlifErr1HtPMp3hJb018HBjvWUpb9yMCJUHmMmXcf1Yzf0FcfRQox_ysLkl4gLb5Qy5fpqOs4k6uCiNRXeJc0RDFjWoBFV6fpjwnh2NmbAnV8Ko_NSzEWESCPR6lcr8RsaB7w43Oa1VD9LltT_cdAHX5w0oZ7g5u894aT_zugScQp9z49KiW5__TrJrMztR0C8JBtZWLv91VgnTsupvHypO_xjKo4u7uR_KpSL1wHfOw8383pkaDD4acDQqKa4p6xpERBSonzRkJyoFxYXap0dyhsp_o2Gc-hWSbMJ3lnoy7fVBM2t5Um-9NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7420f2b14d.mp4?token=MMsCAGTnO8Ib2IdfvpfI8bsSyBMtjtlifErr1HtPMp3hJb018HBjvWUpb9yMCJUHmMmXcf1Yzf0FcfRQox_ysLkl4gLb5Qy5fpqOs4k6uCiNRXeJc0RDFjWoBFV6fpjwnh2NmbAnV8Ko_NSzEWESCPR6lcr8RsaB7w43Oa1VD9LltT_cdAHX5w0oZ7g5u894aT_zugScQp9z49KiW5__TrJrMztR0C8JBtZWLv91VgnTsupvHypO_xjKo4u7uR_KpSL1wHfOw8383pkaDD4acDQqKa4p6xpERBSonzRkJyoFxYXap0dyhsp_o2Gc-hWSbMJ3lnoy7fVBM2t5Um-9NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس‌جمهور: وظیفۀ ما خدمت به مردم با هر گرایشی است
🔹
خودمان را بالاتر از مردم نمی‌دانیم. باید مشکلات معیشتی مردم را حل کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/farsna/457934" target="_blank">📅 14:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457933">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88da696fea.mp4?token=O2hTbv5vYAD2Lfci3flURj4GSXtiEA-cJzFppTvhV2qt9IlExJ5ILndNRBY3LeH5sUHf5Me1EkGwQYhtOjmzm-zmHCEBI8gGpXsfehdm1d7IDu_dzLKUXrtqzDRKSTpmi34TBhfI9V2U4GFzQ5NYPQvU-QcXABFCdsXZGYP219r5fsLApJshNfJDkq4Z1lo_qFwiUkbZilJyVDB8iOBF-egssuLbpDWGSS8xJ7_E3n5SVUDp90709TwAxRhIs2xJKo_9fZAYPOTQuAqBj7xBpNySCFIjzESMxU7G3uhVNBK0ihelBCqnmOnvq2d6wMZt-0I-HJBlVaKVSBKW99BX1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88da696fea.mp4?token=O2hTbv5vYAD2Lfci3flURj4GSXtiEA-cJzFppTvhV2qt9IlExJ5ILndNRBY3LeH5sUHf5Me1EkGwQYhtOjmzm-zmHCEBI8gGpXsfehdm1d7IDu_dzLKUXrtqzDRKSTpmi34TBhfI9V2U4GFzQ5NYPQvU-QcXABFCdsXZGYP219r5fsLApJshNfJDkq4Z1lo_qFwiUkbZilJyVDB8iOBF-egssuLbpDWGSS8xJ7_E3n5SVUDp90709TwAxRhIs2xJKo_9fZAYPOTQuAqBj7xBpNySCFIjzESMxU7G3uhVNBK0ihelBCqnmOnvq2d6wMZt-0I-HJBlVaKVSBKW99BX1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمانده کل ارتش: باید آن‌قدر تلخی در کام دشمن بریزیم که از آن سوی دنیا نگوید نقشۀ ایران را عوض می‌کنم
🔹
ما باید دشمن را ناکام بگذاریم و آن‌قدر تلخی ناکامی را در کام دشمن بریزیم که بداند ایران جای این نیست که از آن سوی دنیا بیاید و بگوید نقشۀ کشور را عوض می‌کنم.
🔹
ما ۱۰ نسل ۲۰ نسل می‌جنگیم و حتماً اجازه نمی‌دهیم این اتفاق بیفتد؛ تنها راه این است که با زبان زوربه دشمن بفهمانیم که نمی‌تواند کاری را که می‌خواهد انجام دهد.
🔹
همواره اهداف کوتاه‌مدت، میان‌مدت و بلندمدت دشمن را رصد کرده و آماده مقابله با هرگونه سناریوی دشمن هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/457933" target="_blank">📅 13:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbR-uAcpv20rBjHNqbRf7PTjRGxlNjMneEAm4cxuF72vrhVMZZU5guHOL2PyShkcfbGpFUl9W9m2e8NXjq5_eGxoadjoF-RQBCejx0aSX_dPbJrtBm1Eh0sJPgPsDP6osYbrYUhLMlC0kJatFM46foCc-Vm9zoDxmlrQZ3au2WjLnJbcTD8Wvvfi3B79B9hgJLwc8KYIZ9OCmNiZvAqZqYqs-cd7QZaJcfL8Eo3sZQVJFT2GWpdcLT8_PDWzqrPAsVnWxCPhL51Htr1PkOPGr8kAhgIzSph_ovJ66gRuYU-zN5K1VMP4a98ra3YD7Zqp9_6Etc_xR_pDWEd9ljoraA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تزریق دلاری پسته به اقتصاد ایران
🔹
آمار یورواستات نشان می‌دهد، ۳۴ میلیون یورو پستۀ ایرانی فقط نیمۀ نخست سال میلادی امسال، در اتحادیۀ اروپا فروخته شده، با این رقم می‌توان ارز کل نیاز گوشت وارداتی را تامین کرد.
🔹
صادرات پسته نسبت به‌مدت مشابه سال گذشته ۶ درصد افزایش دارد. این افزایش در بحبوحۀ جنگ ایران و آمریکا اتفاق افتاده که از اسفند ۱۴۰۴ آغاز شد و آمریکا با محاصره دریایی تلاش کرده اقتصاد ایران را تحت فشار قرار دهد.
🔹
یک تاجر ایرانی به خبرنگار فارس گفت: هیچ مانعی سر راه تجارت وجود ندارد؛ دولت پول بدهد کالا تحویل بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/457932" target="_blank">📅 13:34 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9fe0cf116.mp4?token=Q_2XJWxoVmy5SVyZBuMkr3A6B9pmb3z5TggM4b07yKxLJlewGTLapW6qSKLwot7wMWn8ep0AUr5FoNlHndQe4TxHhstryyfBvz-lHrWcfUt9D6XQPFQLXwHsecrIlWU83P-P27QDZl1yDvrUd9XLD0qfjf73dIzWcihkmVo41nZH6qoKqybxm6JPh7-3rdZImDC2LAw6mzANThGKc7l6nblNYPuURM90GHbMktxSVMfyiVHZvUhKWPo0RKo7b1fH-3e4wZSknSpRZXau2huChsuyuuvxi1UXdx3zzvYuWBP3OsCoRBYYo9SDWLoKVbW6uG6lT-tcCJuk80hHsYezvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9fe0cf116.mp4?token=Q_2XJWxoVmy5SVyZBuMkr3A6B9pmb3z5TggM4b07yKxLJlewGTLapW6qSKLwot7wMWn8ep0AUr5FoNlHndQe4TxHhstryyfBvz-lHrWcfUt9D6XQPFQLXwHsecrIlWU83P-P27QDZl1yDvrUd9XLD0qfjf73dIzWcihkmVo41nZH6qoKqybxm6JPh7-3rdZImDC2LAw6mzANThGKc7l6nblNYPuURM90GHbMktxSVMfyiVHZvUhKWPo0RKo7b1fH-3e4wZSknSpRZXau2huChsuyuuvxi1UXdx3zzvYuWBP3OsCoRBYYo9SDWLoKVbW6uG6lT-tcCJuk80hHsYezvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: بالا رفتن قیمت‌ها در بازار ارز براساس هجمه‌های تبلیغاتی و جوسازی آمریکایی‌هاست.  @Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/457931" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766881483a.mp4?token=Y5t6Ke5SuynbiC82GMHjYQgxYheNXhmQLmVmPsmvKyf82e1FxRA3LipHrvOB38frHoJwoO6ihHNQIXmt-vzBafoHN8AzmM_1b8UJE0ZCktJKpLEBAtlBmUcACIebxG4fgcylf9yJo4H4oydHMBQ07OOL128mVM7lVyLy3sX1hkQEiVmWmzj7XNo8gNBSFfzuy5Zpj6XubypS9-luGMLnj75XZQkpZkfEOEnVNsaTrtEJ1ry5w6OpCbb6y2hLuZDAhwANR3ROFfuRJ48gK7G_QLihpkUgDfhHz-z8K1heD34ltLce5X5WtSWPyWmbQn8SsLo29324SZZNK9NubQR4-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766881483a.mp4?token=Y5t6Ke5SuynbiC82GMHjYQgxYheNXhmQLmVmPsmvKyf82e1FxRA3LipHrvOB38frHoJwoO6ihHNQIXmt-vzBafoHN8AzmM_1b8UJE0ZCktJKpLEBAtlBmUcACIebxG4fgcylf9yJo4H4oydHMBQ07OOL128mVM7lVyLy3sX1hkQEiVmWmzj7XNo8gNBSFfzuy5Zpj6XubypS9-luGMLnj75XZQkpZkfEOEnVNsaTrtEJ1ry5w6OpCbb6y2hLuZDAhwANR3ROFfuRJ48gK7G_QLihpkUgDfhHz-z8K1heD34ltLce5X5WtSWPyWmbQn8SsLo29324SZZNK9NubQR4-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس بانک مرکزی: مشکلی برای تامین ارز نداریم
🔹
همتی در نشست با اعضای اعضای مجمع کارآفرینان: ۲۰ میلیارد دلار برای صنعت تا پایان سال تأمین ارز انجام خواهیم داد.
🔹
از ابتدای سال روزانه به‌طور میانگین ۱۷۵ میلیون دلار ارز برای اقتصاد کشور تامین می‌شود.
🔹
برنامه‌ریزی…</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/457930" target="_blank">📅 13:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYPdckV4eibDm905ajaMtsw9b216sWBKbGs-27aZjxWlR-iJ_dLEa7QkjfbI7ADHmQIzl9aTn90sxG0SlpAPytGMgAPW40ISwWtiC6T92jkHbwmWMpAYm_BxoZWeEhQUMtjtD6G1tsugbDqvhRkJ-oheVpfCxa9p9Kyupz7WwI_qNjKyXZ46EABKe8HYfoC2mrD6Jk1eGj1meoT_3Z-7qryNmch9gnyoeVxIUwGlP7M_7jT18EQO6Bqq1Zl4GkudxaMMdm5Hsq_1STQKRSRDTJp_YZv3_pUobGSWHCk7ZX6Jl36682SxJunliBduB1AmH9TZZJ2EEMkGXbYvlLGq-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مرقومۀ رهبر شهید دربارۀ شهید پاکپور
🔹
سرتیم حفاظت سردار پاکپور: رهبر شهید دربارۀ شهید پاکپور مرقومه‌ای داشتند که شهید پاکپور به‌خاطر فروتنی اجازه ندادند منتشر شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/457929" target="_blank">📅 13:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b7c83d867.mp4?token=uh-_bk9EKzkQcDtQEOQboHir4_gnMLJFg08NakRxPwhYJbbIy6VLkrEkC6nFLzbI7EJfZ2BEeQOVcj2WTpDKNLn3xEN6JHoha_7vqnxrRIOoEc8R65WFIwxoOf6SvnSgHdb4XNEYJsUsWYitPIVyJxudCsDnVy-JgHMTj2LLBIFyCNZ16qcXCjMAw08exmaBg4pQQgq3rxCUBTkuIb4a_7CtplTARjZUhHxe-dOfuDvb5XAs4jZuBlEBa9IDds23KpNKIoW8KDRFJP7uE5UHzkbKDeu27Mam3jaaTiWGdH7Tq9Q9pGu3Q-AiKS49POnwbKY_57iemUWdeBYuFnOWCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b7c83d867.mp4?token=uh-_bk9EKzkQcDtQEOQboHir4_gnMLJFg08NakRxPwhYJbbIy6VLkrEkC6nFLzbI7EJfZ2BEeQOVcj2WTpDKNLn3xEN6JHoha_7vqnxrRIOoEc8R65WFIwxoOf6SvnSgHdb4XNEYJsUsWYitPIVyJxudCsDnVy-JgHMTj2LLBIFyCNZ16qcXCjMAw08exmaBg4pQQgq3rxCUBTkuIb4a_7CtplTARjZUhHxe-dOfuDvb5XAs4jZuBlEBa9IDds23KpNKIoW8KDRFJP7uE5UHzkbKDeu27Mam3jaaTiWGdH7Tq9Q9pGu3Q-AiKS49POnwbKY_57iemUWdeBYuFnOWCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبداللهی دادستان انتظامی قضات شد
🔹
با حکم رئیس قوه‌قضائیه، علی عبداللهی به‌عنوان دادستان انتظامی قضات منصوب شد.
🔸
پیش‌از این مسئولیت دادستانی انتظامی قضات را جعفر قدیانی برعهده داشت و عبداللهی عهده‌دار مسئولیت حفاظت و اطلاعات قوه‌قضائیه بود. @Farsna</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/457928" target="_blank">📅 13:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SA7BJmfVKzswUXkX6JFkH87KyNF7jgiRdnmU0p9AWWEFfYfSInHdzMLb64uRcqCbs3Z6a0StcoaH0AcByKyzq7y-fbcjG37T5ipPxMS2OY70fThK-Fnp9aWpudnIHtv-93djc7AGttYVXIjznwq_oamtmV58FEVqp4cyKfo95Xa9KC43G7PsdYbRRDSyP82ZhOnYOO-57DCZsvGCYW7a1OQn4jK6zlXpT8Rs_xcu4OjJLChcZgZuy26zZeiwsLK4dMwLiiyXpv_a6cz9LS1s6imyCdMq6f0TFEViBgj2v5P7TGbk4o1l7kLdNwc-ji3AYt7E7gndtn6lezcGuUlOUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک بسیجی اهل سنت در زاهدان
🔹
نیروی زمینی سپاه: نادر سارانی سخی، بسیجی اهل سنت، دیروز در منطقهٔ شیرآباد زاهدان درپی حملهٔ افراد شرور و کوردل به‌شهادت رسید.
🔹
پیکر مطهر شهید فردا ساعت ۱۲ ظهر از میدان امام حسین(ع) زاهدان تشییع خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/457927" target="_blank">📅 13:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/469cda217a.mp4?token=I_QhRHEhQYA73Z4FGuF-4WAI63FcmIPFiOUzJfMKgAj7WsFh59iuHlKwLLzCARm5F0De9xDXCOf3hhGtljroyaMd3T6mchvDH7mbPu4aUd0ouWo0ZcSKpI6FC4KYur7q5p13-PrQDVZtwDvXpTShDlY5c_N7TbE--TW0fS5LWAkFywIACfceXhRn0mnQeTzh2iDGpKOo9onddwkWsWTegxx_rlSCkaM-4edBXy6Ncj_Ojua8LjBGGDBK5kPaOtfG5ISia2qm7jwv4cXRSvOMni2qm48rpWT0f2OdQASSNkYbdWY296f1N-aOfpG_N-16KVyK9NygxqvE0duDL6hATQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/469cda217a.mp4?token=I_QhRHEhQYA73Z4FGuF-4WAI63FcmIPFiOUzJfMKgAj7WsFh59iuHlKwLLzCARm5F0De9xDXCOf3hhGtljroyaMd3T6mchvDH7mbPu4aUd0ouWo0ZcSKpI6FC4KYur7q5p13-PrQDVZtwDvXpTShDlY5c_N7TbE--TW0fS5LWAkFywIACfceXhRn0mnQeTzh2iDGpKOo9onddwkWsWTegxx_rlSCkaM-4edBXy6Ncj_Ojua8LjBGGDBK5kPaOtfG5ISia2qm7jwv4cXRSvOMni2qm48rpWT0f2OdQASSNkYbdWY296f1N-aOfpG_N-16KVyK9NygxqvE0duDL6hATQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: ما با دروغ‌پراکنی‌ها و شایعه‌سازی‌ها میدان را خالی نمی‌کنیم
🔹
وقتی ۶ میلیارد دلار دست افراد معدودی قرار می‌گیرد و ما می‌خواهیم آن‌ها را ملزم به ایفای تعهدات قانونی‌شان کنیم، آن‌ها واکنش نشان می‌دهند و بخشی از واکنش آن‌ها، خلاصه در حاشیه‌سازی و دروغ‌پراکنی در قبال مسئولان‌امر می‌شود. ما تا استیفای کامل حقوق مردم و بیت‌المال، پیگیری‌های خود را ادامه می‌دهیم.
@Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/457926" target="_blank">📅 13:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f6915bf1.mp4?token=tmKIT1Z__ZLZ4gQLV0HPZvUOSk6MzdgWH_IAE19JK_JTt3grw77zSUga4tNpKTh2isUFFwEYAtPoNPxUmbg986jaCnqXS0jXhBAsWDactHjIRrdyrks_t_IqVZxA3ub5EMQ5B7HT5nKLQqvsG73heWWVD6Q0quATr0rIF320EViauGKtqL39TITc26dLyP3UsojxjDI-Z-aYPW5vRCaWAB0r9WNOLzJrOhBp-XURs5gyltbZzwXT8Zk04Oa_7ahG4Fbpr55yLIWfzG26sKnxjc8lf_8afVHYx2mZ-kYklYslugDxBWZkk4P_TJNZrJ3QF5iNQ4Obgwax6wAjB8r_-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f6915bf1.mp4?token=tmKIT1Z__ZLZ4gQLV0HPZvUOSk6MzdgWH_IAE19JK_JTt3grw77zSUga4tNpKTh2isUFFwEYAtPoNPxUmbg986jaCnqXS0jXhBAsWDactHjIRrdyrks_t_IqVZxA3ub5EMQ5B7HT5nKLQqvsG73heWWVD6Q0quATr0rIF320EViauGKtqL39TITc26dLyP3UsojxjDI-Z-aYPW5vRCaWAB0r9WNOLzJrOhBp-XURs5gyltbZzwXT8Zk04Oa_7ahG4Fbpr55yLIWfzG26sKnxjc8lf_8afVHYx2mZ-kYklYslugDxBWZkk4P_TJNZrJ3QF5iNQ4Obgwax6wAjB8r_-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در موضوع رفع تعهدات بیش از ۷ میلیارد یورویی، من به دادستان تهران تکلیف کردم که فهرست و مشخصات دقیق و کامل بخش‌هایی که رفع تعهد کرده‌اند را ارائه دهد
🔹
در همین موضوع رفع تعهدات ارزی، حدود ۲۰ میلیارد یورو هم تعیین‌تکلیف شده؛ یعنی درج نام برخی بخش‌ها…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/457925" target="_blank">📅 12:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54ad069d7f.mp4?token=o78qaL0ojMHzpPW1vbbCaPG6JBB8cjHHag73_Lmf_afCh927erBBuO1nXf_wEA14pHgwXnjOQnr4PqC7U2SAiiyEbudZTxXbQPs9SXg3pKriEy3MVxIcpd7-kHoUVr61yuMHzgnqCON4AZdjG0M_zw10SWOck_37mJtPBzhrQdU7tcamzEtTSnkdR299ZpitaXEseYzh0VH9DVLXMC1XXTcL1LHLZSfFRg2LwAtEHfvqrX4yLZ4pDwmXFdFLL5-PV6AE2SWfe-NJIO71d0h7j4nfxBi0dCK9Ih5aTMfNi3I_LqH0w3axFkpmrpdic2oc_xJoxS2c3L27gcytqvM32w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54ad069d7f.mp4?token=o78qaL0ojMHzpPW1vbbCaPG6JBB8cjHHag73_Lmf_afCh927erBBuO1nXf_wEA14pHgwXnjOQnr4PqC7U2SAiiyEbudZTxXbQPs9SXg3pKriEy3MVxIcpd7-kHoUVr61yuMHzgnqCON4AZdjG0M_zw10SWOck_37mJtPBzhrQdU7tcamzEtTSnkdR299ZpitaXEseYzh0VH9DVLXMC1XXTcL1LHLZSfFRg2LwAtEHfvqrX4yLZ4pDwmXFdFLL5-PV6AE2SWfe-NJIO71d0h7j4nfxBi0dCK9Ih5aTMfNi3I_LqH0w3axFkpmrpdic2oc_xJoxS2c3L27gcytqvM32w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: تا اواخر مرداد ۳۵۸ پرونده برای تراستی‌ها تشکیل شده و در یک فقره بیش از ۷ میلیارد یورو رفع تعهد ارزی اتفاق افتاده است.  @Farsna</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/farsna/457924" target="_blank">📅 12:57 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a66bdffa3.mp4?token=kESFZwAxfwTn8C35712uD9xFCF8aKdlDNpVNJwF9y3v3iCCQn0rCFiGRN5vKBP3lvDOCsyW6MQKeQ5wrQVQ1eN0KFLexLn2uboJC14K_yBNmFQ7qMvRgNYGt9Nf_f_fr-JGMx1HLuSGk6KmbVnBU1pcd056Vwtv2n-EYN8-iHwNfmR_n9TrIniPnFShWiwIe7GH8c342J5mTVahorah47p94E-H00ep1p4fUJdZeKF4uDeInGK4WHvzPWdRsBUsLONClBWJF8SRGJSQnQDVjWagij4q1Afg7wtLfWfr1lFv2vs0ikol6ZFZ9gmfxN7rDbBPKzDm3zbk2njSVkWnaFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a66bdffa3.mp4?token=kESFZwAxfwTn8C35712uD9xFCF8aKdlDNpVNJwF9y3v3iCCQn0rCFiGRN5vKBP3lvDOCsyW6MQKeQ5wrQVQ1eN0KFLexLn2uboJC14K_yBNmFQ7qMvRgNYGt9Nf_f_fr-JGMx1HLuSGk6KmbVnBU1pcd056Vwtv2n-EYN8-iHwNfmR_n9TrIniPnFShWiwIe7GH8c342J5mTVahorah47p94E-H00ep1p4fUJdZeKF4uDeInGK4WHvzPWdRsBUsLONClBWJF8SRGJSQnQDVjWagij4q1Afg7wtLfWfr1lFv2vs0ikol6ZFZ9gmfxN7rDbBPKzDm3zbk2njSVkWnaFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مسئلهٔ تراستی‌هایی که تضمین لازم از آن‌ها دریافت نشده، نباید رها شود.  @Farsan</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/457923" target="_blank">📅 12:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58124046a6.mp4?token=S76QaxBH_go3lW3nFfGYgqHPxx6EMLJNY68ays-HzrAyvoDTY0moG7DPMOfBWai1H6D2AKZ-20NBIaY2U2LJjQq8d0lO8QqgAXTaMrYyDWsH2iBNI-vHWaDfJrx5Bw2AY5ZJxvPRnodhL-k2OFtvRYmLDVRqURfxrksYvMqTrnvj3iThY58pKh_Sbp3KwaB7i-hrO0eHFA5AHz0DUFYmd06zKlY7WYrq_6EUIIZEXwfxZjup3CdAD2wh_f1yU3M8mG48cIMANgwcqTetTr7vtpFLS2TLHMxFLBCaYl5XsH0nvNfbLcWW-Gec_LGDddLBJS-0QC_SPC-Zx8DAoHQ-Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58124046a6.mp4?token=S76QaxBH_go3lW3nFfGYgqHPxx6EMLJNY68ays-HzrAyvoDTY0moG7DPMOfBWai1H6D2AKZ-20NBIaY2U2LJjQq8d0lO8QqgAXTaMrYyDWsH2iBNI-vHWaDfJrx5Bw2AY5ZJxvPRnodhL-k2OFtvRYmLDVRqURfxrksYvMqTrnvj3iThY58pKh_Sbp3KwaB7i-hrO0eHFA5AHz0DUFYmd06zKlY7WYrq_6EUIIZEXwfxZjup3CdAD2wh_f1yU3M8mG48cIMANgwcqTetTr7vtpFLS2TLHMxFLBCaYl5XsH0nvNfbLcWW-Gec_LGDddLBJS-0QC_SPC-Zx8DAoHQ-Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تراستی‌ها چه نقشی در اقتصاد ایران دارند؟  @Farsna</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/farsna/457922" target="_blank">📅 12:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af8c2e951.mp4?token=gDlW0_HlfqVY6D4WO1Q0XcMl7rmCr2fLSQBA3qjTnkPPKMo8RbOygMC5SB4mseMYXPdQZ-NDvmgdDexjaGtBhZtSfAF126ulxvLAua9qHqt_cnezLUuqW4Zwq9kYHYLKQVrJ4QE66GPWbDLuQzEngLcZWVRZOdWawhBOG6HjggeGAMNV2njiPzUrJofkWh-L56X6v9ZcXb_fK97kRpnPEoiUZL2MLBswSJ4LkCg-y7F1od-A9h2q91EB-ctiwcqWc5qma0olRNEd-iyGVPzQNxNm9YJfnk_Un4U9NP7YnUDj2AWdtB6f6m4EgXUB_w9SnMoxEJTLIZtr08IWGeflBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af8c2e951.mp4?token=gDlW0_HlfqVY6D4WO1Q0XcMl7rmCr2fLSQBA3qjTnkPPKMo8RbOygMC5SB4mseMYXPdQZ-NDvmgdDexjaGtBhZtSfAF126ulxvLAua9qHqt_cnezLUuqW4Zwq9kYHYLKQVrJ4QE66GPWbDLuQzEngLcZWVRZOdWawhBOG6HjggeGAMNV2njiPzUrJofkWh-L56X6v9ZcXb_fK97kRpnPEoiUZL2MLBswSJ4LkCg-y7F1od-A9h2q91EB-ctiwcqWc5qma0olRNEd-iyGVPzQNxNm9YJfnk_Un4U9NP7YnUDj2AWdtB6f6m4EgXUB_w9SnMoxEJTLIZtr08IWGeflBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس بانک مرکزی: مشکلی برای تامین ارز نداریم
🔹
همتی در نشست با اعضای اعضای مجمع کارآفرینان: ۲۰ میلیارد دلار برای صنعت تا پایان سال تأمین ارز انجام خواهیم داد.
🔹
از ابتدای سال روزانه به‌طور میانگین ۱۷۵ میلیون دلار ارز برای اقتصاد کشور تامین می‌شود.
🔹
برنامه‌ریزی کرده‌ایم تا ۷۰۰ همت از طریق ابزار‌های تأمین مالی و بدون اتکا به چاپ پول برای تولید تأمین شود.
🔹
مشکلی برای تأمین ارز نداریم و هر کارآفرین هرچقدر اسکناس بخواهد تأمین می‌کنیم.
🔹
قول می‌دهیم که ارز مورد نیاز کالا‌های اساسی و دارو را تأمین می‌کنیم؛ همچنین تا پایان سال ارز مورد نیاز صنعت را هم تأمین خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/farsna/457921" target="_blank">📅 12:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T3LUC19h0b0Tt0EymbH_anLhC1ymB2lNxplNwWQUI8JNq73HWpBxmr78qTeey9sJ6kJ664ZMiMCfcA4xpYjkM64LEWajS0j0BQmtcVrdobOJlMCncK1On5nZzEw5_pIXoVwvAbWCEUNsTzQdKcPg2vu7NrtgMmFUJPrAA8gdpJ0HU3BX7Ee863gP8Jl1Gs-qmu-zFW7wCLFuXLVaInAmMKUUckrYLOjUzVzKFvklfIdemaHrib22SFBWHFi42k7OpWozFVkvIBLyWzZ377uQhhdDIcpkNWGuiCWoypv4ptngBLoc0g3Pl0t33tLgWsbFsXKtCMoJ9OVgtzNw3IzpkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد جدید بورس در ۶ میلیون و ۱۰۰ هزار واحد
🔹
شاخص کل بورس در پایان معاملات امروز با رشد ۳۰ هزار واحدی رکورد تاریخی ۶ میلیون و ۱۰۰ هزار واحد را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/457920" target="_blank">📅 12:35 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b227f579e.mp4?token=bzflJFU0lEsamdiWCYwHP5djnZLrUDfU0cDZO4atf0f_suXp8rQZC6H66BIk9yxUUYaW0VUlMuMwMtdP9-VLJXZ2HeanEUg-xjc3kJ4rNGKH-P88Emr5j9K2T1HNYS1NrKYQpeYYxZMeLv-3sQupu8sWOZwu5IIqRubGjepmhXEe9f7x693fc44QWoskAkS_fYDDrpeL7Jt9zMEkcCd9SQfeWXOUBFq5yiZ-hWS2EaR_tNdSiI_x9LoXNcbWqSRz9vO0-85LXmcdjLNzzt3-03-q6IPnUTFnSR4gBudS5XeOsuiKMIA16QoAjWiGh_qKbRw-PboTOaYBWOR6B8-Ncw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b227f579e.mp4?token=bzflJFU0lEsamdiWCYwHP5djnZLrUDfU0cDZO4atf0f_suXp8rQZC6H66BIk9yxUUYaW0VUlMuMwMtdP9-VLJXZ2HeanEUg-xjc3kJ4rNGKH-P88Emr5j9K2T1HNYS1NrKYQpeYYxZMeLv-3sQupu8sWOZwu5IIqRubGjepmhXEe9f7x693fc44QWoskAkS_fYDDrpeL7Jt9zMEkcCd9SQfeWXOUBFq5yiZ-hWS2EaR_tNdSiI_x9LoXNcbWqSRz9vO0-85LXmcdjLNzzt3-03-q6IPnUTFnSR4gBudS5XeOsuiKMIA16QoAjWiGh_qKbRw-PboTOaYBWOR6B8-Ncw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مگر ما جنگ را شروع کرده‌ایم که خودمان را به‌خاطر ادامهٔ آن شماتت کنیم؟!
🔹
مگر غیر از این است که در ۲ سال گذشته بارها حسن‌نیت ما را با بدسگالی پاسخ داده‌اند و به عهد و پیمانشان پشت‌پا زده‌اند؟!
🔹
حتی کانادایی‌ها به‌عنوان همسایهٔ آمریکا…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/457919" target="_blank">📅 12:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">عاصم منیر وارد تهران شد
🔹
فرمانده ارتش پاکستان برای دیدار و گفت‌وگو با مقامات ارشد ایرانی وارد تهران شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/457918" target="_blank">📅 12:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457917">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjwW7CT-9zbB3kBb2QbOLKoCWY_c64_K-dZ4cwRdXadL4CsIJzLdqkjI5AIUbXcIso1uQgJnlFRSwcGqwmLLUKfNUGlsqd4u5FwNJgX28WXXHh56rYCMRs-dhzmqfPOelbOOOEcguOSTS8Wg8ANDCYWDHRyd-gXaCNPAlzLzCRSznsVsEWta83EpCSba9AFdvReIe8ZhY43eF8-sU5iwn5vzjphPWuMikRqHffkvpuYivjS22nuGhANcO33RQuXf9R1xdZEyclyIbVW4oq4UkNPkmVgTnlyUyh2CtfVu-tY0RAutP07W7I3kVhGfxY3oKtZGoyQd99gGS_zW051rCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه: عاصم منیر فردا به تهران سفر می‌کند
🔹
این سفر در راستای تقویت همکاری‌های دوجانبه ایران-پاکستان و ادامه کمک‌های پاکستان برای کمک به تقویت صلح و امنیت در منطقه صورت می‌گیرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/457917" target="_blank">📅 12:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457916">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9BFt5a2NksKkrKXcPOf7HFCpSxQLXUrLdmqqElXgBZeQJo83FZLhA2O5pHNayD0rFyzl69lAqlErg80CzZitXJv6TTwV70_xbg0Pe7ak8zs8es-rA-b_c0w65epi54lIbLBC2LJ_t2ORIt8oGSwgGKt-j-Thqd1v4UeDBFCuSkK8c2Zf3uhYU_QRMTS7WmNlpf1U-9xrwbp5H2NMCtaFcNhbTdjqh2hVfT2RVXU4Xm9YKEMYRdiMxcTaIpaA3Dozxpyb00nRI8Bp9sqkD3rBKKZRsSAQUgBQrYm0beixzqMmEa9kJa-ZcAVvI1XJC_1YOHL4zW0jmu1LQsMFv6XLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلید اولیهٔ سؤالات کنکور منتشر شد
🔹
کلید اولیهٔ سؤالات آزمون‌های سراسری و پذیرش دانشجو-معلم سال ۱۴۰۵ برای هر ۵ گروه آزمایشی منتشر شد و داوطلبان می‌توانند آن را از
وبگاه سازمان سنجش
دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/457916" target="_blank">📅 12:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457914">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVUGbyHDrxpxQi4H6XAJxm2JmUC-nGeFyFJxAKTug53ENvDXiR-QZs86P2HLhpW5rV8_3NZp0D_G7milecTLnqwGuZmppAv4BVvRNpJ1sxPH3kU3xRSnHMD0UbKhsfk-03kR3rfqHRGbc1iU1GejaaTCdGkFxNI3fzByx-ZnE9ZA5DpD5lr1exqZJCzok7Y_9_xAq0olqReCOC_1OQTay8tIVpqSJqJTb3pxqUASG7dOiG_dbaxnp0G5vokmwGL8PBuCLMFxbN7fR7VeDITJsAgiC6dNosVTkzwMgv3Gq2DJptIHgIPYieN8Cr3gGklxBJPLklvz0-OCPRFIRbRrQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
واکنش سخنگوی سپاه به ادعای آمریکا درباره امکان عبور نفتکش‌ها از تنگه هرمز
🔹
رصدها از طریق ماهواره‌هایی که آمریکایی‌ها تصور می‌کنند، انجام نمی‌شود؛ روش‌های دیگری وجود دارد که شاید طرف مقابل هنوز قادر به تشخیص آن‌ها نباشد.
🔹
اگر ایران چشم بینا برای رصد تحرکات دریایی نداشت، چگونه می‌توانست نقاط حساس شناور‌ها را مورد اصابت قرار دهد؟
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/457914" target="_blank">📅 12:02 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dmgpHx74W9BsNlZTzlEXVYyagD3rBYVnUs2QTg3PUXOi9H9DB-Qbh-nC0iYUp4eKpzdavd-6g0dsYgXhkEnveBGbVcthTPNhp6wqb4-_AJSApD6RXKAJg4zHfsesR6ZSpWJLkhGEvuyJnvUSFNjDLTWVZKfQ1II9dcp70dSGxNM3T_kIaMo54vv2ime42Hi9NBKGo4TigdEArjwxBcPhPwX-oOygCJVbc6Ry1gAcww3EOAX6erfR3KK8gPscWBBfYoEB717kgiG6AcQtskFXiQKVutfrlsPTtlKW0ixq3oLgXPgEkQ1NG9qi-aRW7EgFaNgVtGLiX6FVf1E4cqaQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JtGgqXuYF10tLsfkojdYy6f7A2cqUMZT6i0bIkthpaasitv2ceOkBqdFb_PMCDvJNlVkK-bK81jC8cE2FKlQ9HVoJvoJ4TnQ0FwOPA72beUZg1CN33VY7tfhifx3aBGugjItcf0xkb0Yw6JHqixKoZvl3uOWZwzyRMBoRYRr4Av_8T4Lf2qk0unBrf_gAOFu8o--2XYfQvCnTPDNTclfDeFjBiLNF-iYUIKotuZqpHDyGpAlFif3JbOWfeeyP6xnt7BUlBQCgTwMFcbaylJoLzBVbhxDwQ6vF0l0XWmAimF6BJXMK0eN10kz44O_Tsp8TGKI7hhaNBWHa2e6kjInaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاربران خارجی پاسخ تهدیدات وزیر خزانه‌داری آمریکا را دادند
🔹
اظهارات اسکات بِسِنت، وزیر خزانه‌داری آمریکا، درباره آغاز «بزرگ‌ترین حمله مالی» علیه ایران و ادعای نابودی توان نظامی و هسته‌ای آن، با واکنش کاربران خارجی مواجه شد.
🔹
در واکنش به این مواضع، برخی کاربران خارجی ادعاهای بِسِنت و دولت ترامپ را متناقض دانستند. آنها پرسیدند اگر همان‌طور که بسنت ادعا می‌کند و می گوید توان نظامی و برنامه هسته‌ای ایران تقریباً به‌طور کامل نابود شده و تهران در آستانه شکست قرار دارد، پس چرا واشنگتن همچنان به دنبال اعمال فشار اقتصادی بیشتر و قطع شریان‌های مالی ایران است؟
🔹
برخی کاربران همچنین ادامه تلاش‌های دیپلماتیک برای دستیابی به توافق با ایران را در تضاد با ادعای «نابودی کامل» این کشور دانستند و تأکید کردند که ادامه جنگ اقتصادی و تلاش برای مذاکره، خود می‌تواند نشان‌دهنده آن باشد که برخلاف ادعاهای مقام‌های آمریکایی، واشنگتن هنوز نتوانسته اهداف خود را در قبال تهران محقق کند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/farsna/457912" target="_blank">📅 11:51 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457910">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99eb90451b.mp4?token=HaInwr6z7AyiLrVywlIXFjsC80BNvUccVdOy989HsD0PftWR4XgE9l4AnbFcsFV3lfEV6w-bOtjjcQwF_TofmhCrnFuza3Lycf3Lt6MUMPN8N0TB4aRlv73ss_tAtaoGcvRd5ppaYgNmJWQQeB4l3q4EPDlxIGSslQflZsgOYlD2LyUjyyOANsnAZ2an0KG-D8B4q14dQsIkLZ3oeM9JOqOXWFc0sOFTRCuKbxvE8sTIV_CgoDTOR0Lerp2hQ_v5kZRg_71a4E-2hXwC9N04w2xH6fwNQWt9nVfFeV4T36mGVhyPUREq4QPBAjbAgspeSi6sCWjbU2g3VlEZg2kf7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99eb90451b.mp4?token=HaInwr6z7AyiLrVywlIXFjsC80BNvUccVdOy989HsD0PftWR4XgE9l4AnbFcsFV3lfEV6w-bOtjjcQwF_TofmhCrnFuza3Lycf3Lt6MUMPN8N0TB4aRlv73ss_tAtaoGcvRd5ppaYgNmJWQQeB4l3q4EPDlxIGSslQflZsgOYlD2LyUjyyOANsnAZ2an0KG-D8B4q14dQsIkLZ3oeM9JOqOXWFc0sOFTRCuKbxvE8sTIV_CgoDTOR0Lerp2hQ_v5kZRg_71a4E-2hXwC9N04w2xH6fwNQWt9nVfFeV4T36mGVhyPUREq4QPBAjbAgspeSi6sCWjbU2g3VlEZg2kf7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور: چه کسی گفته دولت باید بنزین را ۱۳۰ هزار تومان بخرد و ۱۵۰۰ تومان بفروشد؟
🔹
برخی تحلیل‌ها و موضع‌گیری‌ها از تریبون‌های مختلف دربارۀ مسئلۀ بنزین غیرمنصفانه است.
🔹
جدا از بحث محدودیت‌های مالی، چه کسی گفته دولت باید بنزین ۱۳۰ هزار تومان بخرد و بعد آن…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/457910" target="_blank">📅 11:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457909">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24c647992.mp4?token=f7h8YxASHx6ps_kza-48xl7VSpQhvi4SGqV55YkiSG-MQ8-p-QxWwBNWhOGFnBMzWHC3Jh5mJyv2tQMj3Y5TDZLg6m-56jMe1TFiJ5FBC8z8Cwps7tlls9889e1neOULyowhdZHTsrDEVXSS2PuHM95l2mdpHdOcpEvr215XMe1AbqAKprX56n74E7WJcOxQTndPd9cK54k3yd0h9EWcdrPMCD3xXvCutQTZanv9YtxbIgvH37EjVff3cMGqqluby-zgbcaOZcHxe95UBvsaUOHw2MRsLCvcZpUkiVb45oXmXKJkpfewD7FQp6ZLCG0GuDSchQLCzFonXpI_zzZ9dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24c647992.mp4?token=f7h8YxASHx6ps_kza-48xl7VSpQhvi4SGqV55YkiSG-MQ8-p-QxWwBNWhOGFnBMzWHC3Jh5mJyv2tQMj3Y5TDZLg6m-56jMe1TFiJ5FBC8z8Cwps7tlls9889e1neOULyowhdZHTsrDEVXSS2PuHM95l2mdpHdOcpEvr215XMe1AbqAKprX56n74E7WJcOxQTndPd9cK54k3yd0h9EWcdrPMCD3xXvCutQTZanv9YtxbIgvH37EjVff3cMGqqluby-zgbcaOZcHxe95UBvsaUOHw2MRsLCvcZpUkiVb45oXmXKJkpfewD7FQp6ZLCG0GuDSchQLCzFonXpI_zzZ9dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: از «تحریم‌های فلج‌کننده» تا «فشار حداکثری» و جنگ اقتصادی، آمریکا به‌دنبال تسلیم‌کردن ملتی است که تصمیم گرفته از حقوقش کوتاه نیاید.
@Farsna</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/457909" target="_blank">📅 11:45 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457908">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f3ffcbf39.mp4?token=QYHUaeGIY3aoRADLllIm6uyN0f8-M56WWSHNFr--kINNK9qhAfzgG57c4nzDLwRWGnmT_jCrIUtQ_tIOPrd3poSxFcqEfLZOlkbHuVothDpIHlGfxVZ4VPtcuOdrKkbtfrKRlo5XLAcYh8Yu2EIokrs_Z2WPB7tSOuq-NwmLscdlUD556-9utOxeAr_ZsW9bGPBFNjs18jtQgweRFIhfziBIYNiS7TarKvBSnLRMu3zMtHaf5Xe6dUwW2Nry1t_GB7Y3g3Zwcu7hgnU6JuTlWJm1CEQGr-NQUOXQpcC3lA_Ua6OUZUZSyHj-L4nQqxXTE0bJQBQ4tU9oZCJ89D_R1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f3ffcbf39.mp4?token=QYHUaeGIY3aoRADLllIm6uyN0f8-M56WWSHNFr--kINNK9qhAfzgG57c4nzDLwRWGnmT_jCrIUtQ_tIOPrd3poSxFcqEfLZOlkbHuVothDpIHlGfxVZ4VPtcuOdrKkbtfrKRlo5XLAcYh8Yu2EIokrs_Z2WPB7tSOuq-NwmLscdlUD556-9utOxeAr_ZsW9bGPBFNjs18jtQgweRFIhfziBIYNiS7TarKvBSnLRMu3zMtHaf5Xe6dUwW2Nry1t_GB7Y3g3Zwcu7hgnU6JuTlWJm1CEQGr-NQUOXQpcC3lA_Ua6OUZUZSyHj-L4nQqxXTE0bJQBQ4tU9oZCJ89D_R1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس شورای‌عالی استان‌ها: بیش‌از ۶۰ طرح در شورای‌شهر مشهد به‌دلیل غیبت اعضا بلاتکلیف مانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/457908" target="_blank">📅 11:42 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457907">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">انفجار کنترل‌شدهٔ مهمات در جاسک
🔹
فرمانداری جاسک: احتمال شنیدن صدای انفجار کنترل‌شدهٔ ناشی‌از خنثی‌سازی مهمات تا ساعت ۱۹ امشب در محدودهٔ شهر وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/457907" target="_blank">📅 11:38 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457906">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkvNplUquhRB5KfcGd06eqwJXhwhzEbz3Ofwp9ReGEYgdu3sg9jFV7gbFpS1A7YMfS3xaLSD8VE_wkgQ5lmaBqaIC5JWzhYnsTkzpxwvpkJrzbhGs2XecqLsOkiEaXhJmUyYFXcZQYUU0Eg04RqPe0Wsb-BT3_5hOMvTZHDwxpMJOIgs0pgiure5WmcDhL6iT5pasGkro3OKngAGmhxbwLBldY6UhqiA-KdKUd4VxZ5ff_OyqFfwbuuWCCmjpG0RBFdWSkT0KhIRu_4AZv-xCABd3pIfJfgXAo_22HErryHJtGBNb-NfvVv0Y7XLAymNlvBOmOJ1CdCoXPREPHs_eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی انگلیس: یک نفتکش در ۶۳ مایلی غرب ینبع عربستان سعودی هدف حمله قرار گرفته و دچار آتش‌سوزی شده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/farsna/457906" target="_blank">📅 11:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457905">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/496effd822.mp4?token=UWcNG6gnmlvfBp937QBBecLGyTXLLBtxb1rkeWuZQblWNjNWGKgJJQLea8uqyBtEzctGs0BK0TdwWgAfkSnfn-GtPO1AgAJ3uNrtwAwlRXmStZ_0dFzCUF9DT1TWBxNW8HI5U72oZiFQ6iA0ZSTef-a4NGScKX3-XDaBloZExOqrOqM1RyKEU71krEKfKpEwjmuv4rXCM7kLvZUqdj0zSShaOCGECGQQssIYcRHIl4fqa9XZp02WSLTGD3QdFRnXjusrqlCxqkQSaJfL25WQBBHATVElRMCdamufrwDVMdlwjZXCHPYiQcJ8AWv-q6TMq1mtdtRP2ewNK1vKj5QorA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/496effd822.mp4?token=UWcNG6gnmlvfBp937QBBecLGyTXLLBtxb1rkeWuZQblWNjNWGKgJJQLea8uqyBtEzctGs0BK0TdwWgAfkSnfn-GtPO1AgAJ3uNrtwAwlRXmStZ_0dFzCUF9DT1TWBxNW8HI5U72oZiFQ6iA0ZSTef-a4NGScKX3-XDaBloZExOqrOqM1RyKEU71krEKfKpEwjmuv4rXCM7kLvZUqdj0zSShaOCGECGQQssIYcRHIl4fqa9XZp02WSLTGD3QdFRnXjusrqlCxqkQSaJfL25WQBBHATVElRMCdamufrwDVMdlwjZXCHPYiQcJ8AWv-q6TMq1mtdtRP2ewNK1vKj5QorA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مگر ما جنگ را شروع کرده‌ایم که خودمان را به‌خاطر ادامهٔ آن شماتت کنیم؟!
🔹
مگر غیر از این است که در ۲ سال گذشته بارها حسن‌نیت ما را با بدسگالی پاسخ داده‌اند و به عهد و پیمانشان پشت‌پا زده‌اند؟!
🔹
حتی کانادایی‌ها به‌عنوان همسایهٔ آمریکا هم دربارهٔ آن‌ها گفتند «امضایشان را با مداد می‌نویسند».
🔹
ایران هرچه می‌توانست در مسیر دیپلماسی برای جلوگیری از جنگ تلاش کرد؛ آمریکایی‌ها برای نقض تفاهم‌نامهٔ اسلام‌آباد حتی یک‌ماه هم صبر نکردند.
@Farsna</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/457905" target="_blank">📅 11:29 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOosTvz_dY_RXkf_0GQkQ0C0KqM-TO7G-4WCow8rOZiDy_GGSlhJwlIoR3flpnXnK-POj7-CoP6jSpDdyB5hu-je53FJOs4oNbzVwxL9nL3wFw8s100FqzlsfLb1lpXI-Q0Gk0bp4EtftBtStIXwPK3kayNdeLyfUSdaSz1PMWe3q6bP0OEY7V9TYooAJPydfAV7H9VlHwaaXviG8ym3OQChXxhjuR_H0qW1iRloU7xddfq9JVYEUQGXBRR2dDg4zEh9J5tSMJISDXbokkT3bIip5NMbzvlpbt3PqtM1_UQ5xiH5U93UYubf_NEMI1vZri5vfi8Nsid6nV0zUQMvzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت بهانهٔ ناترازی را به مدیریت ناترازی تبدیل کند
🔹
رئیس‌جمهور بار دیگر با اشاره به ناترازی در حوزه‌های آب، برق، گاز، سوخت، محیط‌زیست و بانک‌ها، شرایط ابتدای آغاز به کار دولت چهاردهم را تشریح کرده است؛ اما مسئلهٔ اصلی نه تکرار ناترازی‌ها، بلکه نحوهٔ مدیریت آنهاست.
🔹
ناترازی به‌خودی خود به‌معنای خاموشی یا توقف تولید نیست و دولت می‌تواند با توسعهٔ ظرفیت، مدیریت مصرف، بهبود بهره‌وری، مدیریت بار و استفاده از مشوق‌های اقتصادی، آثار آن را کاهش دهد.
🔹
این مسئله مختص ایران نیز نیست و اقتصادهایی مانند چین، آمریکا، انگلیس و ژاپن نیز با شکاف عرضه و تقاضا مواجه‌اند.
🔹
تجربهٔ سال‌های ۱۴۰۰ تا ۱۴۰۳ در حوزهٔ برق نشان داد که در کنار توسعهٔ نیروگاه‌ها، مدیریت بهره‌برداری و مصرف نیز اهمیت دارد.
🔹
در این میان، پرداخت پاداش به مشترکان برای کاهش مصرف نمونه‌ای از تبدیل مصرف‌کننده به بخشی از راه‌حل است.
🔹
بر همین اساس، مسئلهٔ اصلی دولت میزان ناترازی تحویل گرفته شده نیست، بلکه چگونگی اداره و کاهش این شکاف‌هاست؛ چرا که مردم در نهایت با نتیجهٔ ناترازی مواجه می‌شوند، نه با عدد و آمار آن.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/457904" target="_blank">📅 11:25 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc4c126731.mp4?token=tInvHTkpPYSgvd9r0F7gTaEdfJJE3NNLW1XTGcCsKoYxR_PEjNMtVBqM0rLsWgeKjXvHJTRwbWSEU-XQFzDZa9Z-HI_h8BHnfuEluKHPGBUhg7_xo9mU2lHCXraGUJZFps2_zdGDYtUhJB46kOVuni41UI81S_vImjOAHPFqgXB8OyAuDZ5hHf_kH1h-NhPzQySUcFFVTNtkfjU7jgiUQL7eHngaQJzZJCiL7O0KpeHc9xt0nVV5CWwQGhwg78ZpJu_1dGHSvkSvVzs8grY-hCiQGT6cMhTc1JJC05X5PiSPvAmEwXbmbMUZWktkdq7zZHg3ZxiAgvaSV4HhMBuDhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc4c126731.mp4?token=tInvHTkpPYSgvd9r0F7gTaEdfJJE3NNLW1XTGcCsKoYxR_PEjNMtVBqM0rLsWgeKjXvHJTRwbWSEU-XQFzDZa9Z-HI_h8BHnfuEluKHPGBUhg7_xo9mU2lHCXraGUJZFps2_zdGDYtUhJB46kOVuni41UI81S_vImjOAHPFqgXB8OyAuDZ5hHf_kH1h-NhPzQySUcFFVTNtkfjU7jgiUQL7eHngaQJzZJCiL7O0KpeHc9xt0nVV5CWwQGhwg78ZpJu_1dGHSvkSvVzs8grY-hCiQGT6cMhTc1JJC05X5PiSPvAmEwXbmbMUZWktkdq7zZHg3ZxiAgvaSV4HhMBuDhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه در واکنش به خبر عبور روزانه چند میلیون بشکه نفت از تنگهٔ هرمز: این بخشی از جنگ روانی دشمن است و چنین چیزی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/457903" target="_blank">📅 11:10 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457902">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eda71af95f.mp4?token=ae4xv_H8tTT3Ei7JKbuwyJ47awL-8akdLLF3F7nrCvvYn9Q9H67DFNnyEOW_JOcpuaN5sDAAaiTPfrpq__nYOR_vFrafb7V_EMlfPFQsSyNsw9nwox1S1Mvbs-aJlkpO4fXLoNI0AEL_Ryj83uxC4w2PBzTg790lP-u0x89YKrkqCm-QIxEe1dFBhgZu6lsp-SuZqssM7MUWd3AwSDQIksPmdR1lyqwF1AuDIr5oqem9P9w-KRci9giXggrdSUdqqvrebh54B_2blEZXJDPJAnt9oru1rVbK6pITGEW75OgRCIYNxYPIDiNV6Z_hSxuprHlCHEaa8aEKo0_TWrc7Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eda71af95f.mp4?token=ae4xv_H8tTT3Ei7JKbuwyJ47awL-8akdLLF3F7nrCvvYn9Q9H67DFNnyEOW_JOcpuaN5sDAAaiTPfrpq__nYOR_vFrafb7V_EMlfPFQsSyNsw9nwox1S1Mvbs-aJlkpO4fXLoNI0AEL_Ryj83uxC4w2PBzTg790lP-u0x89YKrkqCm-QIxEe1dFBhgZu6lsp-SuZqssM7MUWd3AwSDQIksPmdR1lyqwF1AuDIr5oqem9P9w-KRci9giXggrdSUdqqvrebh54B_2blEZXJDPJAnt9oru1rVbK6pITGEW75OgRCIYNxYPIDiNV6Z_hSxuprHlCHEaa8aEKo0_TWrc7Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما با ترکیه، پاکستان و حتی عربستان پیوندهای عمیقی داریم و دلیلی ندارد بابت پیمان مکه نگران باشیم
🔹
پیوندهای درهم‌تنیدهٔ فرهنگی بین ملت ایران با ملت‌های پاکستان و ترکیه کاملاً روشن است و این تحول نشان می‌دهد که کشورهای منطقه نمی‌توانند…</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/457902" target="_blank">📅 11:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457901">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df75e8de6.mp4?token=h5soH2PlhLVnGS98BmEm6gTwx_t6G8OrqqTdS8_Gw7V0Z0LwgCYr5ofsFRlKvLeSELv5JW1rW-wB8TDizqbYMWo82Q992hN50CtzDVLWXWzxjccQ0yj6TxfcvCOMbbFinDbnM04IL9m7pa95jsWhHgT_INMrT7xW3XaqaJ7DbW5UVULYZVTzKSE-_AhX4xiYL0HYTItEUNuaZY2KvsVnu8vLzBkD7lpgViA3rk7N2OvBT_DhHUPiYBlRC-RDPQffHnwCeeCdRpUQSvptctUgiPLGIxQ37kauJaIpe820ELEPUJsrzxYRJBepm1YrrkBQRL0eFpLkwJwE1wcLmc1BAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df75e8de6.mp4?token=h5soH2PlhLVnGS98BmEm6gTwx_t6G8OrqqTdS8_Gw7V0Z0LwgCYr5ofsFRlKvLeSELv5JW1rW-wB8TDizqbYMWo82Q992hN50CtzDVLWXWzxjccQ0yj6TxfcvCOMbbFinDbnM04IL9m7pa95jsWhHgT_INMrT7xW3XaqaJ7DbW5UVULYZVTzKSE-_AhX4xiYL0HYTItEUNuaZY2KvsVnu8vLzBkD7lpgViA3rk7N2OvBT_DhHUPiYBlRC-RDPQffHnwCeeCdRpUQSvptctUgiPLGIxQ37kauJaIpe820ELEPUJsrzxYRJBepm1YrrkBQRL0eFpLkwJwE1wcLmc1BAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: همکاری بلغارستان با آمریکا برای حمله به ایران، عمل تجاوزکارانه است و هدف‌قراردادن مبدأ هر تجاوزی، حق ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/457901" target="_blank">📅 11:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457900">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-text">🎥
جلسه‌ای که رهبر انقلاب استاد راهنما بودند
🔸
این فیلم مربوط به دوران پیش از زعامت رهبری است.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/457900" target="_blank">📅 10:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457899">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oz9N2-2KEM70i8MOCwCj_VuCvp2OMWPIuJ22c28jCUvsdl-w-u7kXJzO-NgMOJD0Iec42iJG5OsZ27hqgcEPIQLcHOVNf11v6_k_DaxpQgY3R4sYYI-NmgqfCCTmrBA0pS4qAD2dgKQYHv6NOjVUz34qHVZuyzRhkstM660Q4rcXLqztE6V5IrShyb7hi0PQ2q5WI82O5IVJa518kUVEdSbm21TRAk85FlgZ3bVbl28U0gt6ezdwA6_DXB7Mu05DTBe4d5fBaeEdvKLRlzh9OJws6Tq6REEWm3007c6tXFIbWAq8oYYyqGqmZg7aOfTT47y9bGBnRgxvj648yQxvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: آمادۀ کمک به دولت هستیم
🔹
بیانیۀ ارتش به‌مناسبت هفتۀ دولت: امسال در شرایطی هفتۀ دولت فرارسیده که ملت ایران در معرض آزمونی بزرگ و شرایطی متفاوت از گذشته قرار دارد.
🔹
شرایطی که اداره امور کشور، حفظ اتحاد و انسجام جامعه، تأمین نیازهای اساسی مردم و استمرار فعالیت‌های اقتصادی و خدماتی، در کنار صیانت از امنیت و تمامیت سرزمینی، نیازمند همدلی، تلاش خستگی‌ناپذیز، تدبیر و هماهنگی همه ارکان نظام اسلامی است.
🔹
هم‌افزایی و وحدت ملی یکی از مهم‌ترین مؤلفه‌های قدرت جمهوری اسلامی ایران در عبور از شرایط سخت و خنثی‌سازی فشارهای دشمنان است.
🔹
ارتش بر آمادگی همه‌جانبه برای همکاری و همراهی با دولت در مسیر اعتلای ایران اسلامی، تقویت اقتدار ملی، رفع مشکلات مردم و عبور سرافرازانه از شرایط کنونی تأکید می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/457899" target="_blank">📅 10:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457898">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN_A1sNduVw-p9edcUuXC_ku0WWaGll0KBjuZj5VNEYEU0-J2g-rzP7TRdtpCEc4HDNBB0dMbVmbtK3PmzNvYKecEQsC-8Q9Bvs2HPz1zXYRRh73hm6P1Gsk9upapJSfmTHeggvuAJvl3lWS12Q9gnqzVXS3nFt4s73aUP3vnH2sSdkDDwkKxPmBY2NmgWXwN8jjyv4Ls54FpiwHjQxd0bIBeiK_PeOrXMY5lkA4EX5fF8zwPOnPCpoLJQ8PBnjg2sRj3cif6SgHblMKBus98PDV0zbynb3h4ARQzYpM0SHQvtb2rCyYJ6YaQImiUcx8bi0pbZR_4QbKqiAF_IgfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بذرپاش: تنگهٔ هرمز نماد وزن ایران در معادلات منطقه است
‌
🔹
خیابان هم‌صدای جامعه‌ای است که دنبال پیروزی است. دوباره دوگانهٔ معیوب جنگ و صلح را شروع نکنید.
‌
🔹
اگر دنبال پایان جنگ و پیروزی ایرانیم، باید حاکم تنگهٔ هرمز بمانیم و یادمان باشد که موفقیت از مسیر مقاومت می‌گذرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/457898" target="_blank">📅 10:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457897">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60671806ec.mp4?token=Ke2szQQVBeiMZCM3CuCaDu5Ia71J_qgV1Vye64pQBrTBUrCNJGw_eJ2ddT_t6eUgkyNqBw1NU6Rr1ayxpBmbLvzWaU5bs1CCYfbgwr3HbpnnvyKMNocV0xKaXvdWN5TBQIX-linZOZvs7U84WsL0W0H-YPasYNRertBhwlVNbERL01IZCXkW_qf7IQN1WkCKSIjxkxkVXZvqawmBlhm4jGZQzxnxxbxCi983ve-s2NLKPCZBAKdMeQu6mKeb9fG3w-4Jm41wulpQgS-wLKfHNJENbAwRb6S-AW8l-aFe_7vjq9LNUaiibXVjk_-AevpkjOyL843a84n32I4_LnlKZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60671806ec.mp4?token=Ke2szQQVBeiMZCM3CuCaDu5Ia71J_qgV1Vye64pQBrTBUrCNJGw_eJ2ddT_t6eUgkyNqBw1NU6Rr1ayxpBmbLvzWaU5bs1CCYfbgwr3HbpnnvyKMNocV0xKaXvdWN5TBQIX-linZOZvs7U84WsL0W0H-YPasYNRertBhwlVNbERL01IZCXkW_qf7IQN1WkCKSIjxkxkVXZvqawmBlhm4jGZQzxnxxbxCi983ve-s2NLKPCZBAKdMeQu6mKeb9fG3w-4Jm41wulpQgS-wLKfHNJENbAwRb6S-AW8l-aFe_7vjq9LNUaiibXVjk_-AevpkjOyL843a84n32I4_LnlKZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرقومۀ رهبر شهید دربارۀ شهید پاکپور
🔹
سرتیم حفاظت سردار پاکپور: رهبر شهید دربارۀ شهید پاکپور مرقومه‌ای داشتند که شهید پاکپور به‌خاطر فروتنی اجازه ندادند منتشر شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.27K · <a href="https://t.me/farsna/457897" target="_blank">📅 10:00 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457896">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IH62q46HArKCoIebOn59vJUG0BH78ALo6D3NwhClwKHYLjn4UIxaJ9pFpi4dASYfRVI6wZGAh6aUma19A9ANDNZQPo86A1lwHYrKlI4UCEYI6NchPmR1HjS-h14pK99Seyadk4ox-rTXdDVW4OdsANvv9p4etJoCw-8lPI41r2YOJ5I5Rlx70k3nDtKK0ShgysoXL0aJMNJnNXpnNDd9ceaE6TQG1s6YaQe66nwHq3iCWvjJBMHW-8wSlJ-Zq32faoETjF7QAS8o4CN_tybVr_pX_ZB6wbfQ_raps-P6WGO3XmgjoQjHbn2XygJBg7NJAKud48pFw9_zuRa1_xNu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محاصره‌شکنی کشتی ایرانی در «روز دی»
🔹
طبق گزارش پایگاه سوپربرو، یک کشتی کانتینری منتسب به ایران توانست با عبور از خط محاصرهٔ آمریکا در تنگهٔ هرمز وارد آب‌های ایران شود.
🔸
این درحالی‌ست که ساعاتی پیش وزیر خزانه‌داری آمریکا در یادداشتی از آغاز فشار اقتصادی جدید علیه ایران موسوم به روز دی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/457896" target="_blank">📅 09:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457895">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">محکومیت دولت آمریکا به دلیل تحریم کودکان پروانه‌ای
🔹
دادگاه حقوقی روابط بین‌الملل تهران رای به محکومیت ۶ میلیارد و ۷۸۵ میلیون دلاری دولت و مقامات آمریکایی به پرداخت خسارت مادی، معنوی و تنبیهی در حق خواهان‌ پروندهٔ کودکان پروانه‌ای صادر کرد.
🔸
در پی خروج دولت…</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/457895" target="_blank">📅 09:54 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457894">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNuXj8dh0dtNJlFj7AUo3WhsatNvdCOI4X8XYY7DHzLcri7Z15CJLSq4dpi9eBYj1pyK_oma72h5-1OkZVjkyvN285pKXI1U9MxReyJz3FW7s_wljpKbu25jl95GI_J4_bo5NNfUN_d4m-MHGW7WeMuYgtnrk6ma35EQkPjMItfTrXVY-S_M2XkukCus5-NCEROKpRZSr4TuiWHFZ8nwB6z65Xsc2_u4RfRBh6kjaN1svCumFLwwN-LedLK_E4K52xrBuI4WpnZd1mMFoCjIgXDgTQgGf2jCg02yLd_FKnSlfNNGDHHVUqyLEJoG8r9rze2jOqoox5ZAlJAQGYpvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجۀ عمان فردا به تهران سفر می‌کند
🔹
سخنگوی وزارت خارجه: این سفر در راستای تقویت همکاری‌های دوجانبه ایران و عمان و ادامۀ مشورت‌های مستمر سیاسی بین دو طرف، به‌عنوان دو کشور ساحلی تنگۀ هرمز، برای کمک به تقویت صلح و امنیت در منطقه انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457894" target="_blank">📅 08:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457893">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a856e524d9.mp4?token=HRFDqzwJsiqAPjuV6kaqErrzkCG8qe6Q8Ak6xO6-XOpO0S7ynzGIpxOPHaA-2gXj1scRiqIN_b6qrM9jQFkZcQVSTUL0Cyy7Mngn48crTN-cEbcz58Vw15Ri88cI33lyWEyYa_72Lqh9uW3aMeVfjf63pt2jsZ32LUM50dFNSvaoTxigHogsUIfG86L7kuuEsQs5X3lQHxOYbTM5yH3VhvKStZlpxtzYUMykVcaWpOTF8RHqXOCQE2W1yPQU-b7t48FeypMf6Dnt82fFxdBO1Tav1DDiRbgzi2IrjgJbdsWE3rNNwwu7UgokQ-nqc1Qu695fTkEyEyX8DlD7nS1M2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a856e524d9.mp4?token=HRFDqzwJsiqAPjuV6kaqErrzkCG8qe6Q8Ak6xO6-XOpO0S7ynzGIpxOPHaA-2gXj1scRiqIN_b6qrM9jQFkZcQVSTUL0Cyy7Mngn48crTN-cEbcz58Vw15Ri88cI33lyWEyYa_72Lqh9uW3aMeVfjf63pt2jsZ32LUM50dFNSvaoTxigHogsUIfG86L7kuuEsQs5X3lQHxOYbTM5yH3VhvKStZlpxtzYUMykVcaWpOTF8RHqXOCQE2W1yPQU-b7t48FeypMf6Dnt82fFxdBO1Tav1DDiRbgzi2IrjgJbdsWE3rNNwwu7UgokQ-nqc1Qu695fTkEyEyX8DlD7nS1M2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: در بیشتر مناطق کشور امروز هوا گرم خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/457893" target="_blank">📅 08:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457892">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هوای تهران ناسالم شد
🔹
شاخص کیفیت هوای امروز پایتخت روی عدد ۱۰۵ و در وضعیت ناسالم برای گروه‌های حساس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/457892" target="_blank">📅 07:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457891">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8e697756d.mp4?token=DB6TzOzSr5XnxT-WwBlkGEIAEYyga8dJrl1Cq9Y-rg1DECuNW2miw0a6eWhamELb86i0uefjLH_GQsu7lJyeKcX1isnDI7-eNifG-_4NxaIxNmHTRSSQ5sjXqt6D1lZuQAnKVFe_OACS0w_zYq92DugTu515-sQqpdUB-TCTg-OmFbOUx2Z9QroaJ5bhLwAteSeejwO5tMRix4JBY0RdS4EbFeZQGYcbpNuc-zN42uQyEw5dZJY9_ivAkE-OAAXkPC3AC8_uNKmryqP3Uuhtdfxu7jQJ0eGQUcfnri9BafNODNSdMO-cTHF9aOfcbQRVY1coO8aPGzGrmCi8GMYqFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8e697756d.mp4?token=DB6TzOzSr5XnxT-WwBlkGEIAEYyga8dJrl1Cq9Y-rg1DECuNW2miw0a6eWhamELb86i0uefjLH_GQsu7lJyeKcX1isnDI7-eNifG-_4NxaIxNmHTRSSQ5sjXqt6D1lZuQAnKVFe_OACS0w_zYq92DugTu515-sQqpdUB-TCTg-OmFbOUx2Z9QroaJ5bhLwAteSeejwO5tMRix4JBY0RdS4EbFeZQGYcbpNuc-zN42uQyEw5dZJY9_ivAkE-OAAXkPC3AC8_uNKmryqP3Uuhtdfxu7jQJ0eGQUcfnri9BafNODNSdMO-cTHF9aOfcbQRVY1coO8aPGzGrmCi8GMYqFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیعهٔ امیرالمومنین(ع) خودت را ارزان نفروش
🎙
حجت‌الاسلام کاشانی
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/457891" target="_blank">📅 05:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457890">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">حملۀ اسرائیل به چادر آوارگان در غزه ۲ شهید برجا گذاشت
🔹
در نتیجۀ حمله به چادر آوارگان فلسطینی در نزدیکی بیمارستان شهدای الاقصی در دیر البلح در مرکز نوار غزه، دو نفر شهید و چندین نفر زخمی شدند.
🔹
این چادر محل اسکان آوارگانی بوده که از مناطق دیگر نوار غزه به این منطقه پناه آورده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/457890" target="_blank">📅 03:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457889">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO-O1_tHf8CDuLiXFB5lOX8VyhhyAZzsVNlXVAC1myKlGXE7qPKRgBZwVJxm3dky3bsjdswqUL_F0b1PQJ2doGcLuwN4WUytXam5OZCi7cUHMApUUyR6_4txRdsKRc4pWrKN9v5x6dA9dY5ZjuKWnt-UdGJteBPPOAYO-B6JJRFC9griQBYrjof-IRonGt0JYwwt6Ebq08_BngZDKGwqgI8I2JnDPENZHPEy5rR5A_G289UyC4mMqQCnDGJsI_rsSfYYmCGpRNaMZhXX45_9BzX_np2H8Yt3QVveMbxrj3UtX15J5OHHDQCLaXH8JYaq0nJOJf6dNHG1Yobv5kG35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن چاوشی برای مردم جنوب ایران آستین همت بالا زد
🔹
محسن چاوشی، خوانندۀ نامدار و دست به‌خیر کشورمان از راه‌اندازی پویشی تازه‌ برای آب‌رسانی به مناطق جنوبی ایران خبر داد.
🔸
چاوشی چندی قبل نیز در اقدامی خیرخواهانه از راه‌اندازی دندانپزشکی سیار برای ارائۀ خدمات رایگان به نیازمندان مناطق مختلف استان تهران خبر داده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/457889" target="_blank">📅 02:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457884">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stCiW-ptDAynKhqapRKL_LOWPidaK6ZVNTV2XCrsJZoy4KG8DUPqqDD9ZJ2qWF5w4wWCp6oq99ZNZ7a7iJ-COUEgfEUXB9vAzcvMGiqNgEqx5BzhDQf1jr_-NFMCUTxM-D-8YI8a688NNaOPAcWIwv-fiMLlX-Mt1S4j-xppV3jwLFmyhz6RoTutsxAoB_GZfCDM1Y9_dH54wE2pnbHHkRpeDOte6mFhpY7aLwfi_opPVxZ0AJhZgYRhvL1laqJhgue-FIovOEeZ8BfpLaWOBe6PciTtVaFWOesYZEFktwdWDOruwfVf9_Z6GFMzbKtO80SmGd2tHU3DGJHUMUnxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cj6TXhb0pbOvexgHDGzUL2nAMeQGF300Yfmz9m_htYiUNhfrA6kYU5fvdLwbnTZ2zRI1lpZGh8ALAdUGIEJ7jFqZ8TiNMu3wmhIwH40rw2_JQSYxe3lVB0TlJM2gzdsxn2uik9p24cJDNmse7weAV88i0ay7WSJ7xSSYeYOeyAvn4qCJ2q5X-0PEWUfucCbLnItOrViUT4crRCHC092CImXhZCR0Fbg3DhjQhnHcf9KPwv-s9zE4sUxEx-RyNyfYIFo98tqD9bb7582xbCWZzyf-VfemoFf-k5FjLNB-L7UnmelLwYpacbYpuUmt3JqwAv_pHDTuLJIoW7Y33NcoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y6XhOqEC8gMnhS78rdfTsx1b8UrfdYEcl9UQp58JSnU0icIv0kQ61ayETetf3K_IFJQKhEfluh6QViPdEpU7UZLzFznO3haGLbCwJ_4-k1pFWlF_g3RCjxXOTW4Zwd2MoPm2bwN4QRBa_AqqfMhnP_AacJMLP-VHc5LA6w04d3tDSead2RfQWNvrXE2Hhxj0gSUuIwO6D06IJ1UgrHArPAMailzbQ_tHGZi91e9XLEoT7e33QXPgWkreneA_tANlhjlWZdVxzxaZilbWeT0oTG1Dt-GD_v3W5zXZyL7gGli_SL1FfsYB-OeRUVqbTCxAq0CJDOfFKcCOM-G_jfHzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dp48WfD_HSXVbAqbWFct3UYyAXLsx4mvQj9jVxidSHKj6S5LCK_Etqn0bG3xoQkt-b-SozQCaS3QUvqg32DeEpBNNwzRfuauHzZLLO7_G6RkQNfQ2yG61GoA5JCXLf1c72aOeLC4HiOwAe6LfMU903uGkByWP0LpDE-w5wNva78HeUK4-kUAEJJ6Yo0SHWfabrsyAgGhcS1cXn6UGaMg-n7Mrt7k5zgeedcXe6BHIl3N1Nw8NI9MLPVC6KcZmNcxU0cDvj0KXyhkO2jFJzeqEkWzVVvqjI4MamTLd4GsYdeUjQjUsUn9qk5gcf1YdnlznUm-aEVmorrmQf9IX99KYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y97RSGPZWozEQdxBuxkBmeBMZ5iCBLaPyAEMT3UnC4v0tXpq-huGhjVFZ8PHjfmgQqvVdZwjdeG57G6mV0RNfpAKcXydR2LX8Tmp25OncFdr0Gb7CadApzXoRuTSgxxyqkAUc0OaIk0KymG2uic05P3y0WxeGxmFoh88J_zplggS9DHiVCqMdcNojjT74L8Xo90C-4fGOcKp5TmeHST3mlchurZTs8yo7eQdAelaw_AYFIXNbpcgKTytjMIZrwURMNICFFouhMTR4kkHbnaom-dYIuC0JVJ1rx8-95swwkFo86BJLqgyakhdo96_1awwmdSKkzQHrzD8LOzvPP5HAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | دوشنبه ۲ شهریور ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/457884" target="_blank">📅 01:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqVdC-unc_AGGOWj6lR2ciM-cfQDkT5rilUOAqD7tUBwMxpSP0bzJGkcaoLecR-4ExU9742Oz-RuplunqmyVRb9pXM61kzzaH2HidBw7T4w3h_WWCgh7Tr72wa-pu6grUYb5dG_kDHrLP9JJjF6Vrnuq_56DOXn6Mk7n2yhgPP5MMVpZuBfulA3-5yA6SHGPBO3wX4MbSbVGxJmOqFoAaeUhzwB1QJBfVy_VW7TlN49PucsSkZLHjEWuNSOsXZtmZadTWmMQRKGSs-lKLhSw82LaxiDFdCyC3ap7xNUNQXlHBCATNx9t_qT0C6hLX3kjmoqAozbe_3RcV-pN4uzTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O3n4gRi10Lel_NU1KNP9cSb88KLdGyCF0cOY_c4YVyhgsP5_8X5yJQ3adqgkAAFPHkjlfjkSHTYljQzxTnyHjTI5tFIcbBMsVIQ7sQfFfq6d_xuZbdEaiWNOtbwLMEw8v3QG84grlu5IY1YJSMlKKBdwYUR5K26lk_Q1XdbKdJ6IhFLNzNNXSbN3ciWq4-q_WMCCdfUHnDWFkJzjSA_S58X3Jd6GDJefGEywXV7tJcJE6qxtw2GDYIZeWvKKEYKkg8g4hVUzCMDXD4PbY91XwnwDe4MLJLhJEfCR8L085DJiIuoT0NppEK55sSN6Den_g5oPhWCQYich0XiAkSpXfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLfD7s0RS93AVsHOCXYYzO91KTHdXGIoBfaFhZTwvu1caOi8tN73kwTp7FTHeAYo_qZqRaTIfOoHV3oVieu_tVnX_elVnbJ1Do_9uKsCcQKCinGC5P6datQuQpVLC9v_R2qf3Le9NeOCygUq0z3Yyx1T9fSbI2JmsiXo3bbJaUvWT3Ir009uSHqGYw9mQaJXun8NcRafjKF-LxMvcSJQ_FZHsXvHXv-s7enBodhTD3q55ZO8YRfAyPJp3IJCb8FAMRB1s6sYN2Nt8iwtbo4pTNElJjHofnXPFUcwT4CRK4tvbPMRf4uxB3iD2IahMnDFKxl8f5As75tajHRok6EO1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FHIy4pSt6K7ftOq_nSbd__-ucPW4Z8GDXjEIdLYuyGDh5mjxJG7bCwC3vwAIVueB9wb61RzwT2e4RGvYKckHhgm7DwocVWcEg1gLanNBVwvzUfCTFJ33L7Tv5w4OoYtrcg9iyhsbsUWUKSDdzADcELY7aJnwuq16iH7LeVwh1soUU8-hbhWV9Sx9YUDGu4DhrSia1at6gG7gZ6putB_KGP-X5J0NwE3mDUpdGjlkCKRPOwIPIJcQpd7_dNYbE8issiLF0aQClQZED2LSfmzc6wbZRHtx5EVJhUOYeXg_orOFqpZfp0deLoNnjFcTVOX0GeK1PFJT15iYUMbljxx9ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AX1K2OG57qqObH_NL5X7mNoM6m_ufY5w7owxUbEe-n2LKotW7GV54jbLRVThi_cwjY9EX4UWTWU3G7uENkKepS_ILmOGyRu5xzp3LZXgnqmwusOM-6Sze5WsvGxUzvuP9ICORfnzgUeS4K8UlKx-gv6rpms0uWpAXGxtRAbhwavJ4wmoQPLlzEWAxFgZUrhEmsbeXLz6QVWFaTg3u6kHIN8rAlG2dUjCDBEV764ziH5a61mP_vhtepQbfuMU7PWkPvMtlHkByXXLam9V2bm85ufqL6VmVyDaxDJalu1Skn07XhsTAfp4JiM-QegVlnrVxN3QT5hl8rDY2QVi0cRKLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSL_K3ow5aYQCrIuA7PRTvzZZJ2amMQLF9MhOjs5nl-b0pCegOT9dw2uaM3-VP5d9sw8hnvipFoUiYZ5ODdZN3OzQ9FUVaWOG87Tm5Hiyeu7CaSf9R9QTcdZJjCXKl_4F7WbaWbY6Fps1v78DqX_sbaVP-RZ8ujbke8nbgC_RFt-PMVnOqUDRYupOe09uOSJSGWHETWPtsf_bhgnFtS1LvFEganvwZzOngDWmb11D4rfGsYPYYO8zwd9dZv0Ig2Wb_HqwR-OmAgWfo3F11PXiDTiFAG5d38GXaLuEVIO-ncimjv5sCOxX2zZN-aY0OrMV26dvBUv8FRO8FOFgEVclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QIV8zwXikcNZ3ZKZ-p9ry7XuJdcbGhvYFRikmJbTaBVyzUn8w4Gjv1EoWM8IJcXviYM-aIQGNbllXjrwZRtzXcck6mwnliU_bnwiT6moYozHh77RokAeti1K7Lok3bbjGkAlLG93fU2jV1w9R_-CaPHKFe7RBBIYYi9R8grrWY6WWBMJsGeVOZL5wTTORyC24UdEzyqQYt_uhppssti7Xv80WNC0L8z6SF6MAT8wuAoye2-xgJp2d71JHp9bV4zAjxoanhPAdulKku-MvTSxrBvjpDQykQWDAgqzOYaCAzoZFzXJUqvdyRv2J2WuUHg5WyHh6Y-Ho3KC5z6i510r6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTUDNzB-RaTEr0ZrUUNS6x-uONDkfBzxo8H2qDkfe5AxNNVvwX7v4JOKSXMhKKRsl-fHzGzAXnXL4vFttXF7Xy13NxYVbWlqOFMlkQc-DKX8988QMuRlqSjNOesV7TvFkXwiNKVpHfMaB6lAXMpYxnID54bRUCRM9xm4QtUqD08Cq1-fFj3V8HGt3LNUfo9Q7Wa0-sW0JdCxiyF3uXL1owZJbOYbIf7hhVRtGg330ze6N8ECdcyKEyfGIfEnHV672RgyJ5UsyVP0zc88WI_GshFZukLhoSBOfFcsTwe_FES31z6qwUBN1y6DCGgjxGJeNhzk_qtB3hnBj2_O0ez5vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzBhpYPmyd7j6kq-i5me5hSO-Ma-RvFBehxIdM4UNGNOOebjAOcMnTlKiwdvNEf1lsNVogueuv3SaS1xecFUyRrxR7e6jrE30TnmbF_RUe47acqWbwGujDU_KP49sMsffk6VMRLbMLykGY3lF5oPP9gz2PZwfs_Fkb08-nw5bJL3ZTzOd8Ukri8uC8pkx-BDUNXkKAEyPgIsZiss66P3lSn3Rofbsn4hNFnApLppyLIS4Ng5A0TwEK45PVX4QrxWeCAd9uWfRxhcTIDNqDZ866cpb9OXNgDWQ9FkifC6quGhWBhG0dyLEv5mswAiZP0-MQaQiPGMN8LXoVAq--otZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTnrWiZWkWQGk091tHAokALNTXaxuDUuAIeUxF3bxEzi7zj2wzpGYH2Rhjb68aS0IrrL8PMSyutcode2S8O7BTOxl8E_EIRuMJwWaCPSSyiQHJAEhwVgRE52NdYOnEWRyM25s-4NRgpvWpIAK8LiDAdfec0WQTqrIhZbAMMZthHvwMPF0hN87-7Rm-otKjblwELnrai-vIsbmCgGxxJ2yQScXdlhXRnuysV9vIY0xD7_1PwxBGxqLAE0dc99eiAm_rPiRSZxDHIxguuHwEbcgCQHqCknwpgU4_O-Yqx4l-gNJ2u7pTrc2n3MCcX5AVJ28yQWr4v8pgsNOrMvBMjQtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/457874" target="_blank">📅 01:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حملۀ توپخانه‌ای اسرائیل به جنوب لبنان
🔹
خبرنگار المیادین در لبنان از حملۀ توپخانه‌ای رژیم صهیونیستی به اطراف تپه‌های علی الطاهر و شهرک المنصوری در جنوب لبنان خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/457873" target="_blank">📅 01:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f837c1cec4.mp4?token=UuI-GNlwUJMl2fbbULoxwUJXpORnlDXYjfOiWeQgvuhK8Ji2erQMnixym2JngA2Y_3khyRGD0S71Z9iFP7kV4dcpUp4RHLB-GY4tGNSjWZIUv-MPtmoAcsprmgGkOtedceAurkkqiaploJFzySsIQdGLUvLDRVB3fMv01V8j6QECsndm719njcmS0kotvEgYvCPYTfafcJo6PmUihTVjVai1jZspXVJ7c9OBwFmzCHCEW0H3OR3TtvgiXgnX3Qit_ktDAvvPYVVNYZMXVnJlVAwHldpWF3uJLyS3Qngr6QDH0KSqS__xj-yLTst2K2BhmsUvpN4OnrLTCJjkjgchNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f837c1cec4.mp4?token=UuI-GNlwUJMl2fbbULoxwUJXpORnlDXYjfOiWeQgvuhK8Ji2erQMnixym2JngA2Y_3khyRGD0S71Z9iFP7kV4dcpUp4RHLB-GY4tGNSjWZIUv-MPtmoAcsprmgGkOtedceAurkkqiaploJFzySsIQdGLUvLDRVB3fMv01V8j6QECsndm719njcmS0kotvEgYvCPYTfafcJo6PmUihTVjVai1jZspXVJ7c9OBwFmzCHCEW0H3OR3TtvgiXgnX3Qit_ktDAvvPYVVNYZMXVnJlVAwHldpWF3uJLyS3Qngr6QDH0KSqS__xj-yLTst2K2BhmsUvpN4OnrLTCJjkjgchNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور: فعلاً تغییری در کابینه نخواهیم داشت.
@Fsrsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/457872" target="_blank">📅 00:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfd26757de.mp4?token=Da8Oo-PF6YCoJZEdGf028qhqBze7So2Baw7TGCNvFAUMjiikgUwmsg9lpCheBsMj5s7k1kZZnxl2Elw8-vP60Cxcc6ayWpA_woE6Vk5_i_hQnMb1EpswZXTErFRxY-5avI--oNemzbEMEc0TVBQDTy3wd-kMXwnm04qAZTzeEJswGzbVJGGVpcehEdYvkdH1SRAMfPGjen2Nzi_Okm-q9AH3MIg4IGKDnqxK1V2VK9PKyAanCxZSKySbBrJAhu2KdbobL-IZrMMuzj-QtqwTP1sKCFRxbFQ96pAUXpM2jIj6dDin1Fn6Okjbvf-SiyX8UMjXs8cu90ingyJaXIbTsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfd26757de.mp4?token=Da8Oo-PF6YCoJZEdGf028qhqBze7So2Baw7TGCNvFAUMjiikgUwmsg9lpCheBsMj5s7k1kZZnxl2Elw8-vP60Cxcc6ayWpA_woE6Vk5_i_hQnMb1EpswZXTErFRxY-5avI--oNemzbEMEc0TVBQDTy3wd-kMXwnm04qAZTzeEJswGzbVJGGVpcehEdYvkdH1SRAMfPGjen2Nzi_Okm-q9AH3MIg4IGKDnqxK1V2VK9PKyAanCxZSKySbBrJAhu2KdbobL-IZrMMuzj-QtqwTP1sKCFRxbFQ96pAUXpM2jIj6dDin1Fn6Okjbvf-SiyX8UMjXs8cu90ingyJaXIbTsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسابقه‌ای که یار میدان است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/457871" target="_blank">📅 00:27 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457870">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIi37ltUyyO9ynZorCLn_Fy_rggE1E3vn07IoGCC-m6hvzGmV7e_risgPVq3eVPPjhskqPaapJBBF2UZ_3bPqoFxfkaaJS0jFCYCnEAo07rM1wYm0_WN1gGIjtiYRS3jDTlbPHsRNUVu665F9_5fD6FgiMlWD8BUxwdN-MoW0XPcQqk14jRhlMSzA0udfP1E3TckePHkAefvbf7dQgxBPIqezczYnUNXfdtAou0rDCeejTPOj3d1NfP3MCAY0fBV-2mWefaX2IxJWDVIfhz64kQxxbKRLW37WUR0ucrDnS_ABN1LocCC02ZDNkD0AwyEKm3Q8AjttdOJSBNXkI984Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور چهره جنجالی در کنار استقلالی‌ها
🔹
‼️
در حاشیه دیدار استقلال و سپاهان یکی از مدیران سابق استقلال در ورزشگاه شهرقدس رویت شد.
⏺
فرشید سمیعی، مدیرعامل اسبق استقلال که قرارداد منتظر محمد در دوره مدیریت او به صورت یک‌طرفه فسخ شد و یکی از متهمان ردیف اول بسته شدن پنجره نقل‌وانتقالاتی آبی‌ها به شمار می‌رود، برای بازی با سپاهان در ورزشگاه شهرقدس حضور داشت و در پایان همراه علی تاجرنیا استادیوم را ترک کرد.
⏺
علی تاجرنیا پیش‌تر نام سمیعی را به عنوان یکی از گزینه های مدیرعاملی معرفی کرده بود که این مورد با مخالفت مواجه شد.
⏺
باید دید دلیل حضور فرشید سمیعی در کنار علی تاجرنیا که قطعا نمی‌تواند تصادفی باشد چه بوده و آیا سرپرست مدیرعاملی استقلال بعد از تلاش نافرجام برای مدیرعاملی سمیعی باز هم قصد دارد شانس خود را در این مورد آزمایش کند یا خیر.
@Sportfars</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/457870" target="_blank">📅 00:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457863">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0qVjuzzZGNEwwUZPM197CyLbdB0cqsOu7NlBJX2POjwjphSdaYFqn-2yfnPip6nblJMhKrlL9mkTNgohC9PlXtXMk58rNQ_xN4MzxDKKLXkzyVthOaArPo-Ri8FsuNGoJXf27eWZlgA_TKaP3aPjovagrsnNajdtkuJ2cvrJ1BfMontIlDaO8IYZpswXTbCr5CU5SRhvTP50px-CzIs34SWr42WxmxgCvTUcw7zN3uPx4SwK_6TTQa09OTj_MTuYRtfmBGnnTBEFEnTH-amYCOe_veVpUdcq83hDVeM132Bcoia4ljKxU-OvJhPkL-vs0GtuDPwFilrRYx-lEjxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gHu3JtCdoCgQuJ3sL9fS0HTO6AoayPp3Ae6mle5gzv6HWkMNimT_VnVJ2XgWhvYxeywCtCu-imLrnH_NDzGPKbnNzt1S4GTktX-19vDqHLtY2606SZTRIgwELWG7dOS__GAZCCmFLPF0ivzoz2Wt8lj09bBJb9W2nOyvOvYnde6WbiHwaIpqSbtzPrLonWi0aMR3tc_yC_TKxbXYq5l8dvNUSjCegu-4cEG5AKZB9wMOvxgLLOGRWNA5CltKdu4sahJnm40cuvUiohNjh7yiltGoA5UU6i_3-SwjxagGZTwFSI67vRYwTziBy0y4y41FR9ZTAqHGmV44RNmpwQbf8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pV20lYdgIkvfwQHZyWKVE3RTZJW90_Jq0iex0lxkZ8f9FBuqHNdCE7mFY_5J6LdMK_Z98eDTltJ5xMJC9xjvN3yUkz4q7tCK824T01NEE4YOd_wuInnT9vNqnJaldZKAjGfWuwybHAXq1YU2bCs65ChpiXFfZ21AZmvgCpWAKknEgsAJ0s-57WY1tFpOK61nIVwkEe3yxY4IWYRhwhVH6_Q7K0kRawFEVd3hWSBRGhsDeiZQym_YmsluLObNmtdot-MsPSx4-by0kOMQ0fROfr7Cic5E0Ua5XOW4rnHCIRZHMLvMcvnv7Z7qLQeaO4FkL-HLdZt5S9nFPlaMhH22RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WlZuHQDDut-FJP0PvhGpn4-sRNphPfS5Uwl4UmmdMFjW0dLtVl8xslrSvQHZAbEJD4uRG3Azz8U8hChcByy90PCVJSxtILJfM3yuBY_pjz0eDJ20bTl8IE7dIqhVwM_Acy9OfYDRz99E8x-pVgUpAu5JoenefxJDKGh_cBz8kmfwCSXkPMNpn9-2JoiIP8W45Kixp2jDh4CESmhBUiR4b9Zl9vQXiCdkuwnd5Kfb3BKfjksKl2DW9YkpfbEywKMWYgP8Wl6cKO4Eem36t_zQwpNbrWxmReWXAvgl2bV_b5v6G-9CWEWbHPt-fx5BDAMUAnpJDoxIF5z1Nqsj0DjhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V8thUrpzPWKJem-IMgGPPAjIlySivzi9tcG3R8yy0LiSBlrbr1vBfIY6l9BKVPvq1PxUvOD93_nCF8R22QIUKF344xy83VcP2i5foH77RRWb2EqLWZELFYv9T_ti2sOpR8IJEUa-Bwf765uapuWBwFfY-dMX_8szjnuEigxPrpVyAj7QVdAvfokVYIhz3_BAH2HZH_puL0sLkYyvvEniU2svUmaXhZDAaCtscsdor5ULpuem2-UnnLgKIpcvmdhKP7lOcugHoKqSvG6Otu3SuQ-uojSqp49vBoWRc3wQSlAiDjZKI8wIJzMjLz8zVrQrUnwwrevphmrklCv5zdJvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eN4M98S7MZYLCaUr54rfvLX1tZEEE9cxdpxKHtt64tVx1R4vW6GfaJFFYSsOrKy8m70s_wkZkGAjgP5KsghcgT2Ndxhmz7VWtD9kgful9ifoyHSiSFpju1Qln2oQFNrbiCl9ViaDPvgR9mG3Y0S8SN6NaCyLNIt-Qwt_f7B9RWzEaVkqw0m7ufU0aaNGVIoIg2HGlK98eBsYbEGpmz_Sx1nBAt8_y-ae8XDIWfQ0axHxfh3olSJ9JBSnFeSZ3cHE8j1v__j07KyE8b-evHS5qOOFdsaZs9hhGEgmM85ulv3o2F1cSG6NKMzJFlpUzkSG0dI1SE4Otn7hKSL5ED_MNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l9fGyGPKaMI5Wj9ZwqITaYldwZVnUoA0ZBAkmZfq4Q52O3aDuG2H8jC92hQ7CmBRU6-xzhFr3nphw5fibOjYPfRODOtj3kXb4VJfCXN-mEZ2nZnwO195bihPZDV8_WGOvKVEbK3R9xCxnVmivYqlArkQEpfAo4HiRqCO9NyIzqL9thbSv1RutS9FvnaRBr1591OKBakfPi5uvHQ1_rcl6TYIY08OOxmF5Wz3ey-2ytT_A_ZMU8WANk6-p9o7rBwoFX5gdVbYApYPe8WjKqmKQNWXaD0tjPbXSBdZEYKiqFU3N9H94DfUtgLL1WvNPHDZpLxo8-8G1iQ5PnFkCgOwsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازی شمس‌آذر و آلومینیوم اراک در قزوین
عکس:
امیرمهدی زارعی
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/457863" target="_blank">📅 00:16 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457862">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af406c72a.mp4?token=fhiFjUH-4BCSvVUAOycQBSVfzHOg00C6I1SoSQSLDpk9eN6vvQtOqUoGnPPqVI5QHvE3x90JMTak-t-ge1h9y7BPn_nfdrLM0dHkgtLB4exqfM8P-O5_ZBDYzMV8-dxneRYChbndezrmGvjY3iZyDXAz1GawrMtmguJLO9eAt5j52MApc0ICfVXyJiQFmsQRHcBiXON--63yJu91WA0wr-mdA57Q5t8eOw5LSKOtAVz1ditqKI0nPR0TOPv92wzKRqdNCaMiZXn3bxa0Pbx5x2CTVJg09Zerrpx9-6w7LRJeGTE4Gb-FZU5q3GrpjVoKQEzdez7ghi9wrUdzatYmmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af406c72a.mp4?token=fhiFjUH-4BCSvVUAOycQBSVfzHOg00C6I1SoSQSLDpk9eN6vvQtOqUoGnPPqVI5QHvE3x90JMTak-t-ge1h9y7BPn_nfdrLM0dHkgtLB4exqfM8P-O5_ZBDYzMV8-dxneRYChbndezrmGvjY3iZyDXAz1GawrMtmguJLO9eAt5j52MApc0ICfVXyJiQFmsQRHcBiXON--63yJu91WA0wr-mdA57Q5t8eOw5LSKOtAVz1ditqKI0nPR0TOPv92wzKRqdNCaMiZXn3bxa0Pbx5x2CTVJg09Zerrpx9-6w7LRJeGTE4Gb-FZU5q3GrpjVoKQEzdez7ghi9wrUdzatYmmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم بوشهر: با عشق رهبر زنده‌ایم، تا زنده‌ایم رزمنده‌ایم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/457862" target="_blank">📅 00:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457861">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74bf93ac1b.mp4?token=oaJr5zOnh__Uybwm7gpYWyn0ZSJix6214eVsDRcZ5MkD8oUX9mOXtVvc8xJhIJY_m6FxLJDfTvOzLEC15yNR4gMb2vTI2W-1ltig_0S85wysiDeegeuDC92Scw-BGNQXBp04PzMpUGN6_LkxLhvQTVVGMrJA2RlgbHFBgKvVU7lCKerVZzo_S45NaefI-MKFSbWHlK91iGWfi0Lr0Euf8sFSBr4p9Vv48eMKlIJJamEMqM8vTqtlQYQgrAoTA6YZ_7qkoo3JIee3u84PL9VouHS1llJTUAf5gbCveRufAkXfklx8E6Dew5Y1oxjX8l_Ny9ZAvX4UGIq98hPNFX95PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74bf93ac1b.mp4?token=oaJr5zOnh__Uybwm7gpYWyn0ZSJix6214eVsDRcZ5MkD8oUX9mOXtVvc8xJhIJY_m6FxLJDfTvOzLEC15yNR4gMb2vTI2W-1ltig_0S85wysiDeegeuDC92Scw-BGNQXBp04PzMpUGN6_LkxLhvQTVVGMrJA2RlgbHFBgKvVU7lCKerVZzo_S45NaefI-MKFSbWHlK91iGWfi0Lr0Euf8sFSBr4p9Vv48eMKlIJJamEMqM8vTqtlQYQgrAoTA6YZ_7qkoo3JIee3u84PL9VouHS1llJTUAf5gbCveRufAkXfklx8E6Dew5Y1oxjX8l_Ny9ZAvX4UGIq98hPNFX95PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خوش‌چشم، ‌تحلیلگر مسائل استراتژیک: حتی در محاصره می‌توانیم نفت بفروشیم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/457861" target="_blank">📅 00:05 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457860">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBRo6xCqSkDNPHwbYjzeL1yrUij7xMR62TzpAw3RtRCYvTQnlIzcXgKdFfcklafWRSSuhUyAu4FSjDzi54f0yYTY6HMczRWHHK4huKPauMXaX-iqnQKU2b3N3ZvdnfSSP67cUoLaHqwC5NxY66IQUN24hr1RRAS_In15Mav--Zh1cLTa-JH5Uh0abQlL9m2TMQiXeUrQykRguTbSRJkwa_cZ7WlFV_jZs6CEpQ6HB8W4eFAgeGaGr0TDfeQDEGSprtJ0lSLfczyvfJUfXqgwdvxWKKxNKwzCdYWWy9QkXYVD5sOYTztVIfn4etnSnZ5yKm7t-tYrB-vlx7I3cetTtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: این ملت سست نشد و درخواست مذاکره نکرد؛ بلکه این آمریکا بود که درخواست آتش‌بس کرد
🔹
حجت‌الاسلام طائب: در مذاکرات به سند رسیدیم، اما طرف مقابل ۶۰ روز هم این سند را تحمل نکرد و آن را نقض کرد. فکر می‌کردند می‌توانند با بازگشت به مذاکره، این ملت…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/457860" target="_blank">📅 23:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457859">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/283b659299.mp4?token=Wom06Amt7rHkfdWfq4h4Hxrqf_fh5lgqrcEn9ZvZBxHBFBWEaURIdLraZYM1Y6MB6lzbEJHiwoFJwNtPUIFTzIyxP-FPqK7Pdg9jK7SmOnX_LhpL7EC_6kPtj61WwpKWEiQvupe1Rwd1QUDO0cIjrWy0r7VOG9Dbs17l_9ZspL_QELn8QwkkZogX53twXHgz-eB5j83b0YlQeadCvNnRvNauxoA_mOLZj5mRhciNZhxdr4ltsFcARBatLMLIHaZGppvUMHkCamhUWpWEJbkHKXSafpf1tK8OOsTKrM5Z0SxM6fedzyY7lHPTlbvTTOUeErPjO9Cn7fX1p2eGk7LRBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/283b659299.mp4?token=Wom06Amt7rHkfdWfq4h4Hxrqf_fh5lgqrcEn9ZvZBxHBFBWEaURIdLraZYM1Y6MB6lzbEJHiwoFJwNtPUIFTzIyxP-FPqK7Pdg9jK7SmOnX_LhpL7EC_6kPtj61WwpKWEiQvupe1Rwd1QUDO0cIjrWy0r7VOG9Dbs17l_9ZspL_QELn8QwkkZogX53twXHgz-eB5j83b0YlQeadCvNnRvNauxoA_mOLZj5mRhciNZhxdr4ltsFcARBatLMLIHaZGppvUMHkCamhUWpWEJbkHKXSafpf1tK8OOsTKrM5Z0SxM6fedzyY7lHPTlbvTTOUeErPjO9Cn7fX1p2eGk7LRBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صف مردم همدان در میدان فلسطین برای ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/457859" target="_blank">📅 23:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457858">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8-ng-8jw4aVH4wfzS0KGJbLkmuAQJ1h4JJ7ECV9OIrMS9E5lHWscVzUtW2o6NYyOe77ysqyu0vy_qt8M96FtaXh4HEpKHH7CopL-jvlk1-gOZ8m5wm6lG3nYp57hzidDwOfdMUcg2R-93eWsWEz3JISv4bcF6y3ITjYACdaZb9MxbufEDRHKKqurt66bdoHIwTX4swO5_7xaO-WruVRK7Ie1ay0JhW7SX1R_G4aJnmNYs9ABqhjft-n4DolX6A6fREEQcIOsgmku1RszEZwWLedF0mhJtY616mOaCZEyy3eWMhKi-EnAYzRPBOmUAsv-yGe_eQ9Iip2IEWf0chyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: این ملت سست نشد و درخواست مذاکره نکرد؛ بلکه این آمریکا بود که درخواست آتش‌بس کرد
🔹
حجت‌الاسلام طائب: در مذاکرات به سند رسیدیم، اما طرف مقابل ۶۰ روز هم این سند را تحمل نکرد و آن را نقض کرد. فکر می‌کردند می‌توانند با بازگشت به مذاکره، این ملت را خانه‌نشین کنند.
🔹
نیروهای مسلح نیز ایستادگی کردند و با عملیات‌های خود، ضعف‌های ارتش آمریکا را به رخ دیگران کشیدند؛ ارتشی که بیش از یک تریلیون دلار برای آن هزینه شده است.
🔹
آمریکا تمام توان خود را وارد میدان کرد و تصور می‌کرد می‌تواند ظرف سه روز تا شش هفته کار را تمام کند.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/457858" target="_blank">📅 23:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457857">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c2560c6d4.mp4?token=aJV4CLelEi4K7hkxbhQTYYVyzkxqMryVdOv2Q64asD5I05OOszqVslkrPzQ3rsiV3PCLVRKUwivfHti0KzRBOZIlskjFHXLdCqdMuIHX18W5QEfs21IvIZbr647ivIqWHW_0VWQMv2YzpHI_SvPqnFbH-_2ePJV7kBSDJdKfar8o4XzHVobQEmYau4DHCh8Mm97yJcquxWu1jSCbfk3Zx-3OuDh8-wLMrnlohri2fwScbdMe6aQsnosm-GsfvFtEXGCOm8Ref8v-J3E-kXRCzNhb9WUZMiEw4g18AZ4L5AoU_MVzvs90ZDds3m7R2cQETkBHqt4oy1GhvaYHrhrPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c2560c6d4.mp4?token=aJV4CLelEi4K7hkxbhQTYYVyzkxqMryVdOv2Q64asD5I05OOszqVslkrPzQ3rsiV3PCLVRKUwivfHti0KzRBOZIlskjFHXLdCqdMuIHX18W5QEfs21IvIZbr647ivIqWHW_0VWQMv2YzpHI_SvPqnFbH-_2ePJV7kBSDJdKfar8o4XzHVobQEmYau4DHCh8Mm97yJcquxWu1jSCbfk3Zx-3OuDh8-wLMrnlohri2fwScbdMe6aQsnosm-GsfvFtEXGCOm8Ref8v-J3E-kXRCzNhb9WUZMiEw4g18AZ4L5AoU_MVzvs90ZDds3m7R2cQETkBHqt4oy1GhvaYHrhrPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زیارتی از صحن انقلاب تا قلب دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/457857" target="_blank">📅 23:41 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457856">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
آخرین وضعیت مسیر ریلی شلمچه بصره از زبان رئیس دفتر رئیس‌جمهور  @Farsna</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/457856" target="_blank">📅 23:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457855">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0cb427ea.mp4?token=TYlCdLgQJxEfiessUTn--s6BDu6z76SvYJfDv02YOb6WuD0WiKBK5c-yE3olgI6L2n8FZ4HnLBxEE8ikIiz4ZIscdlA6o4z_mKYBmjCgRBOqqz7Zt8Pq2lhPQgsIrJYzMJzlZPMtkmCkrs-kYMnXMTbYfYXzEJGiHny_p_Ss8aZUZ5IarYhAnoORMlaaF1zL8YM79hzgYKDBi0UZqDVb6L9DDxzslSbtXnuCFcPQht80AJmiLql5loE-EWh05Wyx48rcE_warIqO69foY_pohNyf2FkclREEilA0624uPfSGaHiuwtYAuDXhgzQjQkC-3O9ihu5olu1p3dBah8ImHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0cb427ea.mp4?token=TYlCdLgQJxEfiessUTn--s6BDu6z76SvYJfDv02YOb6WuD0WiKBK5c-yE3olgI6L2n8FZ4HnLBxEE8ikIiz4ZIscdlA6o4z_mKYBmjCgRBOqqz7Zt8Pq2lhPQgsIrJYzMJzlZPMtkmCkrs-kYMnXMTbYfYXzEJGiHny_p_Ss8aZUZ5IarYhAnoORMlaaF1zL8YM79hzgYKDBi0UZqDVb6L9DDxzslSbtXnuCFcPQht80AJmiLql5loE-EWh05Wyx48rcE_warIqO69foY_pohNyf2FkclREEilA0624uPfSGaHiuwtYAuDXhgzQjQkC-3O9ihu5olu1p3dBah8ImHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس‌دفتر رئیس‌جمهور از حفظ پایداری دولت در سخت‌ترین شرایط کشور   @Farsna</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/457855" target="_blank">📅 23:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457854">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3bf0806a3.mp4?token=JeCrpLbFdaLikfVEYlhaEv9I2xDhceYxbALgBioQX20QFHJafNiVMxag6SDdd9TfA7Ko5RORmppdwo7oD_hlpitV9vAl96hu3SniTMs2endwbWelBr4f_l2-lEKg7QP3e2nKJBR7FWO2DV0ArNzbjeylNI2Nz5vCcqWP9trptCBTVpmnVRK9dVnXT9slR0C0-vVb0ZwCnxXDJskJlfmG2mQyfJvEdCXk-VsO0wVwXP_MgCGQD7iP5yOKbSb7stI2ZytfT776ZjFbSpTz4Btg1jjiYH89S8TS9mJ07oFbPXcZcKTa-fI3Y8whdlReds1xursiZYKt_nVhgBUV3_jXzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3bf0806a3.mp4?token=JeCrpLbFdaLikfVEYlhaEv9I2xDhceYxbALgBioQX20QFHJafNiVMxag6SDdd9TfA7Ko5RORmppdwo7oD_hlpitV9vAl96hu3SniTMs2endwbWelBr4f_l2-lEKg7QP3e2nKJBR7FWO2DV0ArNzbjeylNI2Nz5vCcqWP9trptCBTVpmnVRK9dVnXT9slR0C0-vVb0ZwCnxXDJskJlfmG2mQyfJvEdCXk-VsO0wVwXP_MgCGQD7iP5yOKbSb7stI2ZytfT776ZjFbSpTz4Btg1jjiYH89S8TS9mJ07oFbPXcZcKTa-fI3Y8whdlReds1xursiZYKt_nVhgBUV3_jXzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب پرشور حماسۀ ایستادگی مردم تهران در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/457854" target="_blank">📅 23:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457853">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03aeaeab9e.mp4?token=NLbyODa9hC_qcmv1Pbbi9AUnACz6g-waViUScMeTo0OoXEGeUNQSS8wRTmtxeuTW0bf8HHX_2YtbfT3xBNF1aSzlM7jBL1s3GnQj3MMw46zg_IlQ9DRj8iEhcZ77hENV398HOgQi-wxbvggsWpQdrQPWJN2tn3y7GiMQUq_J8jvc4PQx5KIq_UgjGxfiRTgjC2CJLzosIhhUwgEZTIDnp55EjJGNy4Dy7nh-lTtnhEoJgPXBZusUTKEvv4WTh1uJT0VjWaancxu96B5A7iXaZekyqwNJsvWedkhZN2l61-rGjuwwqA4kiMWzvKWJq21B48a_lKwenuj_FqcTRekPJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03aeaeab9e.mp4?token=NLbyODa9hC_qcmv1Pbbi9AUnACz6g-waViUScMeTo0OoXEGeUNQSS8wRTmtxeuTW0bf8HHX_2YtbfT3xBNF1aSzlM7jBL1s3GnQj3MMw46zg_IlQ9DRj8iEhcZ77hENV398HOgQi-wxbvggsWpQdrQPWJN2tn3y7GiMQUq_J8jvc4PQx5KIq_UgjGxfiRTgjC2CJLzosIhhUwgEZTIDnp55EjJGNy4Dy7nh-lTtnhEoJgPXBZusUTKEvv4WTh1uJT0VjWaancxu96B5A7iXaZekyqwNJsvWedkhZN2l61-rGjuwwqA4kiMWzvKWJq21B48a_lKwenuj_FqcTRekPJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس دفتر رئیس‌جمهور: قرار نیست کالابرگ همه مردم افزایش یابد.
🔹
برخی از مردم نیازی به کالابرگ ندارند. @Farsna</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/457853" target="_blank">📅 23:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457852">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44cc75b4bd.mp4?token=BDYCGD2pZVOYeEzo1yDHFrj6CN2wJNqSWrUCmpxW-UHV6TetroiLZG4GF4rk-xIlyKiDD45izVhUxQDmBjae5z4J4yIycUoOncRqwNyAV-ruI2U2T9g6l8kZroc9RABWKcrxWPioxhevpcrg0Z5ZyJXfgYNntcvWr_WzVBuZ48gSoVosuGs94mqAikXTIxDFOX7iqXXnOMQTuZ3HvqJOo_5lCgFot0sbyHKgFNJr4MiCADpMVKPBSz0ajR7y7ykTARttlnUo5DUVdQQTtdaj_Py2AnUy8EcbY8GhNYBcmmCPefKtKZDi942RJ1G_TKIN2sByrfiDX7AMrhPgRsHDjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44cc75b4bd.mp4?token=BDYCGD2pZVOYeEzo1yDHFrj6CN2wJNqSWrUCmpxW-UHV6TetroiLZG4GF4rk-xIlyKiDD45izVhUxQDmBjae5z4J4yIycUoOncRqwNyAV-ruI2U2T9g6l8kZroc9RABWKcrxWPioxhevpcrg0Z5ZyJXfgYNntcvWr_WzVBuZ48gSoVosuGs94mqAikXTIxDFOX7iqXXnOMQTuZ3HvqJOo_5lCgFot0sbyHKgFNJr4MiCADpMVKPBSz0ajR7y7ykTARttlnUo5DUVdQQTtdaj_Py2AnUy8EcbY8GhNYBcmmCPefKtKZDi942RJ1G_TKIN2sByrfiDX7AMrhPgRsHDjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های مهم یک متخصص در خصوص علائم سرطان معده که در صورت مشاهده باید در سریع‌ترین زمان به پزشک مراجعه کنید
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/457852" target="_blank">📅 23:22 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457851">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/362a915d77.mp4?token=mmVkbWvrAoL2gMyZ18zfbxpRA_yeqyyvcJX7waDbYZ1WG8IT7z6n_53XjT1lcqctyi1SoGxU-LcQGiYDO7Xb1iH8NklJXzXUbXmiz6UP36nahlyp85qVty2wTBP7HxoqGzEsNm5a4J4kILlCW7oXKccsPdIhBKP2Uo_5lI4sNTTo4ylBMSWjKT6l6yPp9J18fHjWwzWxPArMuAQzi-3QeSAK2NNgvDv7VeYbRKc9h9Rw-n7NRPokFmBlHhO-jNW6Aw8tSWLRfUY8OnIaKfF0wa62aRfGQsj93PSROQ_1d-cxAtDfMNQ_Z-RZ2oIB3MtNwTev95OvR8NWXhSMpH8urQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/362a915d77.mp4?token=mmVkbWvrAoL2gMyZ18zfbxpRA_yeqyyvcJX7waDbYZ1WG8IT7z6n_53XjT1lcqctyi1SoGxU-LcQGiYDO7Xb1iH8NklJXzXUbXmiz6UP36nahlyp85qVty2wTBP7HxoqGzEsNm5a4J4kILlCW7oXKccsPdIhBKP2Uo_5lI4sNTTo4ylBMSWjKT6l6yPp9J18fHjWwzWxPArMuAQzi-3QeSAK2NNgvDv7VeYbRKc9h9Rw-n7NRPokFmBlHhO-jNW6Aw8tSWLRfUY8OnIaKfF0wa62aRfGQsj93PSROQ_1d-cxAtDfMNQ_Z-RZ2oIB3MtNwTev95OvR8NWXhSMpH8urQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آخرین وضعیت مسیر ریلی شلمچه بصره از زبان رئیس دفتر رئیس‌جمهور  @Farsna</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/457851" target="_blank">📅 23:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457850">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0ce9d12c.mp4?token=XGmZdwyPZegyc9WwjAqRofwF9_vHyJpPN305qrr3sE2iN33H_a8_JF1C_4lGbhbB6zzkiD8DYvWKdmb-E8eQVvEY5Vwe0mldbWHkx6SYoNUqdwHxBTQqvOUBFk_fVaktMyIIfMbSeZEH8HKAj1jGzO38op4FUfD0jZlUT8PeHi_jwNI1Dwccx34xIxyAllnrEem-4KRpYRqha6TYHjcAHn_X66UpmGcNakKvzSADaOJ_nD8p0OkVPKvfThb8Lcns55zNtf8vbR-o-5Ic48XCvwgMOn7qFFxXGSsXh6HaEaBAfpjIJ29oDLu4lE5ug8aGK5BxFa83vHHEiMgVwFEtUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0ce9d12c.mp4?token=XGmZdwyPZegyc9WwjAqRofwF9_vHyJpPN305qrr3sE2iN33H_a8_JF1C_4lGbhbB6zzkiD8DYvWKdmb-E8eQVvEY5Vwe0mldbWHkx6SYoNUqdwHxBTQqvOUBFk_fVaktMyIIfMbSeZEH8HKAj1jGzO38op4FUfD0jZlUT8PeHi_jwNI1Dwccx34xIxyAllnrEem-4KRpYRqha6TYHjcAHn_X66UpmGcNakKvzSADaOJ_nD8p0OkVPKvfThb8Lcns55zNtf8vbR-o-5Ic48XCvwgMOn7qFFxXGSsXh6HaEaBAfpjIJ29oDLu4lE5ug8aGK5BxFa83vHHEiMgVwFEtUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: کریدور آستارا-رشت، شلمچه-بصره و به احتمال قوی زاهدان-چابهار را امسال تمام می‌کنیم.   @Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/457850" target="_blank">📅 23:18 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457849">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237e90a4a7.mp4?token=G_B0FuetbiEsnPhcYO6TmJ8G8Rze5O_nIt4hp1qXBz5IgnrGB0i-xH9l2gPOF3EF0KSMC8vXXuqkN3yZBxyQYH8qODHTxlcFm4sGQ_aezNh7e8d95LNwqqKF1aHgeVm4CQq_Z7btE2EsDZJ2rO7wQVnXbsM03IUh2UK_ZzHLcfgPF8TmNIz1Yahr5hwj79kgsuh1s-egFltyY5KrLtviSKr2XH3UFPkyeJ8mreNk9og_NK2o2dg6Oc2KFN5QPYsKtCgYFxYi7Ozp9uHSobHjycZ374ygdWNvEbGcjEy9GxQkDD8x51tUyqyDOO1Q_9k3pZjYtKZm6uQqCOgdT757fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237e90a4a7.mp4?token=G_B0FuetbiEsnPhcYO6TmJ8G8Rze5O_nIt4hp1qXBz5IgnrGB0i-xH9l2gPOF3EF0KSMC8vXXuqkN3yZBxyQYH8qODHTxlcFm4sGQ_aezNh7e8d95LNwqqKF1aHgeVm4CQq_Z7btE2EsDZJ2rO7wQVnXbsM03IUh2UK_ZzHLcfgPF8TmNIz1Yahr5hwj79kgsuh1s-egFltyY5KrLtviSKr2XH3UFPkyeJ8mreNk9og_NK2o2dg6Oc2KFN5QPYsKtCgYFxYi7Ozp9uHSobHjycZ374ygdWNvEbGcjEy9GxQkDD8x51tUyqyDOO1Q_9k3pZjYtKZm6uQqCOgdT757fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به آن شیطان بگویید که سرت خواهد رفت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/457849" target="_blank">📅 23:14 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457848">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
مشاور امنیت ملی عراق: ما پیشنهادی را به ایران و عربستان ارائه کرده‌ایم تا یک شورای هماهنگی امنیتی واحد ایجاد شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/457848" target="_blank">📅 23:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457846">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd9e3eaa9.mp4?token=lG5z9jrNhbYJy1oxs7ic10gFQak2v4uupWVor3Lm3cA-G9ny59IvoyZ6POnwxz1pGoCrnbmZJ1g1iK8b6DVTLaam8AJ8s8dByhZsXBLPoyC6-xwrYcis-8yIceZTjAwO6rJEMT1W4CJzjVh4EYeM2QgbrXvNQcPkR0KUSxT3-09_XQVlpBSjnVcMXfNfvQkqyuvtX09yExuN9ApiYXPWG3QhDqJ2OHps3h1IaYyq8hcyewGWQlZ3af0PL0en56kformcV3BWedwk3QGBvma1rfFZ1z1OSWMQ60UhJJYbMZ1NbUSSQwojaa6lAFcF5gAby0VydcmBvp_ku4vSu0UblK8uEcJ4axFH42N50oRj3efD7Czp6N2EUkrXGX0YhiTDwLlBNB32_6YUv7bOf8yVQafFxUsmiaOaGmNtMKXtsvROw_6X7QilqbgvGozXTv4gM49ryAHDaWwLVkPRzEnnT7-L1dAsXwh6BcIyb7mIAaHCa_KrC6fC-3eXoPHrc5WSel5wCRNs3LAk1vtwBB2RThjLBd_5P_44WsCm4WhulT95wxa0U_aumidp6-arAodZ9A4OFvuIZygR3XqzswvIad2RGgqX6oWXEPEMMdUhNgUUtb3XGaiNaokZj6HMaFmFdLozMt0JbI2Th8dkJbsA7V7kZv7Ho2N13tgo5mlicZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd9e3eaa9.mp4?token=lG5z9jrNhbYJy1oxs7ic10gFQak2v4uupWVor3Lm3cA-G9ny59IvoyZ6POnwxz1pGoCrnbmZJ1g1iK8b6DVTLaam8AJ8s8dByhZsXBLPoyC6-xwrYcis-8yIceZTjAwO6rJEMT1W4CJzjVh4EYeM2QgbrXvNQcPkR0KUSxT3-09_XQVlpBSjnVcMXfNfvQkqyuvtX09yExuN9ApiYXPWG3QhDqJ2OHps3h1IaYyq8hcyewGWQlZ3af0PL0en56kformcV3BWedwk3QGBvma1rfFZ1z1OSWMQ60UhJJYbMZ1NbUSSQwojaa6lAFcF5gAby0VydcmBvp_ku4vSu0UblK8uEcJ4axFH42N50oRj3efD7Czp6N2EUkrXGX0YhiTDwLlBNB32_6YUv7bOf8yVQafFxUsmiaOaGmNtMKXtsvROw_6X7QilqbgvGozXTv4gM49ryAHDaWwLVkPRzEnnT7-L1dAsXwh6BcIyb7mIAaHCa_KrC6fC-3eXoPHrc5WSel5wCRNs3LAk1vtwBB2RThjLBd_5P_44WsCm4WhulT95wxa0U_aumidp6-arAodZ9A4OFvuIZygR3XqzswvIad2RGgqX6oWXEPEMMdUhNgUUtb3XGaiNaokZj6HMaFmFdLozMt0JbI2Th8dkJbsA7V7kZv7Ho2N13tgo5mlicZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۷۵ شب گذشت؛ اما قلب میدان هنوز با مردم می‌تپد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/457846" target="_blank">📅 23:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457845">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0400d3d73.mp4?token=fD9btH67eCNBUJvxz0xNsNLTPCIIV3TY1fLK8uyl9i3hDdT07AKT9p3gDCcraymlXcTWQLE67MWZt8SxJZgyUKu3hLsuEALByBN7EGb5Yn-_PtzT0MGOt6mD3FFDz0r5k8cJLRpMqB07aaOrsFXy9mDaKwbj_JHZMhgr8LcUA9TMuGbUpNO18L5MVPx1M_gpjgsoDHgdKrW55WWXOhIaE1KNo--AiQkOXeSG2rgH3lE8cZKCpi5pZldpC2Ekpr-b5-wXPY3QcJBmrpBRc9gdfjDzpD4cWZxqQb7EY0Y3emzBmaJYtw_CWICj_NZ27lJVQR0b4v4MQ_42JCBMTUtIJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0400d3d73.mp4?token=fD9btH67eCNBUJvxz0xNsNLTPCIIV3TY1fLK8uyl9i3hDdT07AKT9p3gDCcraymlXcTWQLE67MWZt8SxJZgyUKu3hLsuEALByBN7EGb5Yn-_PtzT0MGOt6mD3FFDz0r5k8cJLRpMqB07aaOrsFXy9mDaKwbj_JHZMhgr8LcUA9TMuGbUpNO18L5MVPx1M_gpjgsoDHgdKrW55WWXOhIaE1KNo--AiQkOXeSG2rgH3lE8cZKCpi5pZldpC2Ekpr-b5-wXPY3QcJBmrpBRc9gdfjDzpD4cWZxqQb7EY0Y3emzBmaJYtw_CWICj_NZ27lJVQR0b4v4MQ_42JCBMTUtIJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبر شهید انقلاب: در توانایی‌های پزشکی در سطحی قرار داريم كه جا دارد ملت ايران افتخار كند
@Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/457845" target="_blank">📅 22:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457844">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnuXhEUkBJ9DB0DCIs-TGzxfJJhL4xBLC5UtPM-aPKWzIv5mYPhv_WRa0b2JBej5U2bU57iNihd1Z68SY_K6sSSKch7_zExM5nfCsG1W2Poj4-5VZPFBSX3xlJUJI8M0HQ9CMNlRBUQNDvCMC0wApCutn91nDvrx6URU0icnAlF9se8VabXoWVH_Q1veDsKSPUUd76BV_1vpzhFkcwy7fYkqigUkZXlDS5NGXyOjadRfLCvgMCxITgBSaIMe65N9hEcbHXEMOKabaU6GaB-xVTHNU5W6kn-acHYk-QVjk0V7C2D6jVnUQ4ruEoEfP2tq3dtH9sivxUnnscYk2sEz_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاهان از استقلال شکایت می‌کند
🔹
باشگاه سپاهان به دلیل استفاده از یاسر آسانی در دیدار مقابل استقلال از آبی‌های تهران شکایت می‌کند.
🔹
پیش‌تر آسانی در دو بازی اول لیگ مقابل مس شهربابک و نساجی هم بازی کرده بود و طبق اخبار منتشرشده به همین دلیل شکایت‌هایی علیه باشگاه استقلال به دلیل استفاده از ستاره آلبانیایی مطرح شده بود.
🔸
چند روز قبل سخنگوی سازمان لیگ استفاده استقلال از یاسر آسانی را قانونی دانسته بود و حتی نقل قولی از کمیته انضباطی در همین رابطه منتشر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/457844" target="_blank">📅 22:54 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457843">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81bb53e31c.mp4?token=TjPnd97hJRluiPYbnKkcZ2k0LeZC6UOhBP4sKY0apZnlOiY8csLfFJFwGDhpsyyj33j1D5TR-t9hLmSsylPPdRqcSEiOa-j0XvZVMDkkcckQeYBD6czQw4PAFc8zde4e1xEehb7JifAwfnS1oScDC-djF4nx7oAJiRAoChI9Vu8gZ8tstTlrdx00UGqqZypAtmSugs3NMQH7_iVbeAHPIKCezJtplY7TQReW4rgYvngGtQhhBOR4z95_YjWLidNB7RFhWnbdpercqXaxGdhyklVqjWNM0VaP3oKVXBvnyi6_yTxRN-j-xLZE2VaSJX7MetNFGoIQVbSNr4wFXmvjNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81bb53e31c.mp4?token=TjPnd97hJRluiPYbnKkcZ2k0LeZC6UOhBP4sKY0apZnlOiY8csLfFJFwGDhpsyyj33j1D5TR-t9hLmSsylPPdRqcSEiOa-j0XvZVMDkkcckQeYBD6czQw4PAFc8zde4e1xEehb7JifAwfnS1oScDC-djF4nx7oAJiRAoChI9Vu8gZ8tstTlrdx00UGqqZypAtmSugs3NMQH7_iVbeAHPIKCezJtplY7TQReW4rgYvngGtQhhBOR4z95_YjWLidNB7RFhWnbdpercqXaxGdhyklVqjWNM0VaP3oKVXBvnyi6_yTxRN-j-xLZE2VaSJX7MetNFGoIQVbSNr4wFXmvjNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اهالی قاین ایستاده پای وحدت و انقلاب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/457843" target="_blank">📅 22:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457842">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe7l655TxDj_McIYjxpBX-6pFbLjjtoajejtl0g1ANa_2kFRJ_NjskDHYeXJYdWUnxOF_U0dqX-BwTZdOdhM1QmL1IowYXCeujRq-Tt14rNsCM_Yu6ftxfCzsUZbcwfgUOiOPOcLn30p3waxcX4aKDqADJ0qSyukSFEZJJ5akEx7iJdRQ4UxxGO89xdRI_xFGvw5vMnu91GJSZE9QlpxmjkBtOL-shGC0Pk2MdH5_A_3W4FGUkZm4aOILM0Mum9VDiuSPcDcu8gm10dLrGpHtQuP_W3YxhaYr3hFADdA7sZtppTWPporiBnWUJ3m1IyQP1Y9Ztd3nICavjNzBZi6Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
با یأس، ترس و بدگمانی مقابله کنید
@Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/457842" target="_blank">📅 22:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457841">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eneYKiYnnVlmQg_OBhEyOe9QTQbenvMKPxiayGFhLySEqegzpvskFVnSYVZAprKLewhFDnszvC2W36flynRofMEogiH5oSHWiPsimE6zBdQdbJsAlBTt07HeAD83sz0ZYTQ72Pt-4weKhVZ2eDspAsB5m5gFAXK-8VZANa5eNkwGXFKGhFYLrctHa9ySR6Mc9S3QQNpcmjocuGomWv5rYGTT-F7B8tbxQ1M2RjSZe7bZbnwz-cN4t6_1FbunzfL2OfxLOlGzuAKn6BRHrzDRpfZzoR8-39kzc5U4hs0yJ_xYLsgKSB7hXXr6eRz8LxG_1JJ5kFxFHCr7GaEK6J9ZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای عالی امنیت ملی: ایران مشارکت یا حمایت هر کشوری در جنگ اقتصادی آمریکا علیه مردم ایران را به عنوان یک اقدام جنگی تلقی خواهد کرد
🔹
اگر جنگ اقتصادی ادامه یابد، حتی یک قطره نفت نه از طریق تنگه هرمز و نه از هیچ کجای خلیج فارس صادر نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/457841" target="_blank">📅 22:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457840">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa72d2be1.mp4?token=TldNWJg4ovT6r70cyjFS6QprZuelzBP7bpv5IaEoC2vkBbjM-OedN7I1dmnGDBhKmfPo6EHLo3gIEI9vKGkihehebwIKD_XRDuVuJdKaoFPljpjnqDBG12VqGWKH4Bs-PwKT0uG86_iP45_WjQMFUzK8TWsbxhtX647Hl1mxZwHcEie5GhYJlXjTERr_hrDDPHyAOhs7iU1iIUsp_4aIW89cXf4tDg6D_AuiE31zdzCf_TePWNlad9RaXhYQ-QOmd0-3faRSr3mcUMTzAvr_9DNxSgmk8DYHV_DbkYzgndF9SL3p4bxKq04WZr-p31-gy_zp-90wETTX3IfkH81tmIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa72d2be1.mp4?token=TldNWJg4ovT6r70cyjFS6QprZuelzBP7bpv5IaEoC2vkBbjM-OedN7I1dmnGDBhKmfPo6EHLo3gIEI9vKGkihehebwIKD_XRDuVuJdKaoFPljpjnqDBG12VqGWKH4Bs-PwKT0uG86_iP45_WjQMFUzK8TWsbxhtX647Hl1mxZwHcEie5GhYJlXjTERr_hrDDPHyAOhs7iU1iIUsp_4aIW89cXf4tDg6D_AuiE31zdzCf_TePWNlad9RaXhYQ-QOmd0-3faRSr3mcUMTzAvr_9DNxSgmk8DYHV_DbkYzgndF9SL3p4bxKq04WZr-p31-gy_zp-90wETTX3IfkH81tmIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبض مقاومت در طبس؛ ۱۷۶مین قرار شبانه رقم خورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/457840" target="_blank">📅 22:36 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457839">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">توقیف و مصادره در انتظار شناورهای متخلف در تنگهٔ هرمز
🔹
نهاد مدیریت آبراه خلیج فارس اعلام کرد شناورهایی که از ترتیبات اعلام‌شدهٔ ایران برای تردد از تنگهٔ هرمز تخلف کنند، در ترددهای بعدی با محدودیت‌هایی از جمله جریمه، توقیف یا مصادره مواجه خواهند شد.
🔹
این نهاد از صاحبان بار در مقصد یا مبدأ خلیج فارس خواست پیش از کرایهٔ شناور، فهرست به‌روز شناورهای متخلف را در نشانی
pgsa.ir/non-compliant
بررسی کنند.
🔹
همچنین شناورهایی که از این تاریخ به بعد از طریق انتقال کشتی‌به‌کشتی، ترنسشیپ و سایر روش‌ها با شناورهای موجود در این فهرست همکاری کنند، خود نیز به فهرست متخلفان اضافه خواهند شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/457839" target="_blank">📅 22:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457838">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001d757206.mp4?token=nHFrOFA3KGwOjAtCeBv9cxr0pupqR_79MBbRiMkiDnwi9ouVdL6VfIra8ZFsiJl7VBK9OJBheXBijaVrab4_HYlm44lq7RK87FbsVwMzs4s_bFXWnff_TvRH8EEyqRAN5oXIzTU0AMzzILVI3e53vB92erGrdDtt6fBkNFl2bLBOzjCl6bfK_Hq4ZqBhU62n1fsl_-zMpVmi1WSMrannylFYMDhI6TIFvb_UtlOUME9OjEwH-Pvkbi3E05R6kH4E8tIY99xkwaF9yVqw-Jwtse3VhsoTVQIHppwt-kQk6fH09UhiDKXJunMA6nkzqkFdUaDQQnF1hAaTZh8xczbUpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001d757206.mp4?token=nHFrOFA3KGwOjAtCeBv9cxr0pupqR_79MBbRiMkiDnwi9ouVdL6VfIra8ZFsiJl7VBK9OJBheXBijaVrab4_HYlm44lq7RK87FbsVwMzs4s_bFXWnff_TvRH8EEyqRAN5oXIzTU0AMzzILVI3e53vB92erGrdDtt6fBkNFl2bLBOzjCl6bfK_Hq4ZqBhU62n1fsl_-zMpVmi1WSMrannylFYMDhI6TIFvb_UtlOUME9OjEwH-Pvkbi3E05R6kH4E8tIY99xkwaF9yVqw-Jwtse3VhsoTVQIHppwt-kQk6fH09UhiDKXJunMA6nkzqkFdUaDQQnF1hAaTZh8xczbUpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار نماینده حزب‌الله در پارلمان لبنان با عراقچی
🔹
حسن فضل الله از نمایندگان ارشد فراکسیون وفاداری به مقاومت در پارلمان لبنان عصر امروز یکشنبه با سید عباس عراقچی وزیر امور خارجه دیدار ‌‌گفتگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/farsna/457838" target="_blank">📅 22:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457837">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae4dda833.mp4?token=vI2N5I_thYYhyhgiF3AJFutbMY2Lt-t7vpiN1gXU9gOtux3H7c3fNo0w-Nnk6_vCsYzRIJREWk9x6bz0trbdAkrRGwYaW3wdY1g-rmqP2CyyJcOFf2XQLLN93UDa3MzEFm3rAlNCh0YAsHwkBYCbdjTZokNeKyAqRZg18t24KLDz3AxYcQm3QfAoHnGhxGlANCSMrnIW1CZhb0LfM8MpDgdgLvc1ddrltaFeCOw9kMkUObd7H_BlI-zp0g49rcQJpL975AYFN6tPDaCF74P8fDV9k77InRD6I3ylO8BWRenZRnAEFP_9qSLLaq2euTfV7-t04JvkQ2i1CezRhaGHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae4dda833.mp4?token=vI2N5I_thYYhyhgiF3AJFutbMY2Lt-t7vpiN1gXU9gOtux3H7c3fNo0w-Nnk6_vCsYzRIJREWk9x6bz0trbdAkrRGwYaW3wdY1g-rmqP2CyyJcOFf2XQLLN93UDa3MzEFm3rAlNCh0YAsHwkBYCbdjTZokNeKyAqRZg18t24KLDz3AxYcQm3QfAoHnGhxGlANCSMrnIW1CZhb0LfM8MpDgdgLvc1ddrltaFeCOw9kMkUObd7H_BlI-zp0g49rcQJpL975AYFN6tPDaCF74P8fDV9k77InRD6I3ylO8BWRenZRnAEFP_9qSLLaq2euTfV7-t04JvkQ2i1CezRhaGHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درگیری بازیکنان و کادرفنی شمس‌آذر و آلومینیوم اراک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/457837" target="_blank">📅 22:11 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457836">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
لطفاً به کشاورزان سیب‌زمینی‌کار نیز توجه کنید. با وجود اینکه اجاره زمین‌ها سر به فلک گذاشته و قیمت سم، کود شیمیایی و حتی کود مرغ و غیره به شدت گران شده، بعضی مسئولین از فروش هر کیلو سیب‌زمینی با قیمت ۵۰ هزار تومان هم توسط کشاورزان جلوگیری می‌کنند. این در حالی است که گاهی حتی با این مبلغ، کشاورز باید ضرر کلانی متحمل شود. حرف ما این است که اگر قرار است با گرانی مقابله کنند، با گرانی همه اقلام مقابله کنند، نه فقط بعضی تولیدات کشاورزی مثل سیب‌زمینی.
🔸
مردم رحمت‌آباد منطقه کربال (یکی از شهرهای شیراز) از عدم رسیدگی مسئولان جهاد کشاورزی شهرستان زرقان در تخصیص سهمیه کود شیمیایی، گازوئیل و آب کشاورزی شکایت دارند. شغل ۹۰ درصد مردم این منطقه کشاورزی است و الان دو سال است که این مشکلات به وجود آمده به طوری که مردم کشاورز این منطقه دو سال است درآمدی ندارند و با خسارت‌های زیادی در کشت و کشاورزی مواجه شده‌اند.
🔹
ما در یکی از مناطق شهر تهران (منطقه ۵ شهرداری) ساکن هستیم. متأسفانه داخل منزل از آنتن‌دهی همراه اول و ایرانسل محرومیم و مشکلات بسیار زیادی از جمله عدم ارسال پیامک‌های بانکی، رمز دوم و تماس موبایلی داریم.
حدود ۱۰ سال است که از طریق اپراتورهای مربوطه اقدام کرده‌ایم و به هیچ وجه پاسخگو نیستند. واقعاً جای تأسف دارد که در مرکز ایران و مرکز شهر تهران موبایل آنتن نداشته باشد.خواهشمند است این موضوع را رسیدگی کنید.
🔸
همچنان در شهر نورآباد لرستان خبری از مسکن ملی نیست و ما با ۴ فرزند تقریباً امکان اجاره کردن یک واحد حتی در روستاهای اطراف را نداریم.
🔹
در مشهد بیشتر اتوبوس‌های خط ۱۰۴۹ و خط ۳۳ بسیار شلوغ هستند و کولر و تهویه مناسبی ندارند. واقعاً محدوده رسالت با وجود تراکم جمعیتی بالا، نیازمند خدمات‌دهی بهتر سرویس حمل‌ونقل عمومی و اتوبوسرانی در کمیت و کیفیت است.
🔸
میدان مثلثی سه‌راه شهدای باباپیر تویسرکان حدود یک سال است که ساخته شده اما تاکنون خاک‌های اضافه اطراف آن تخلیه و جمع‌آوری نشده، جداول رنگ‌آمیزی نشده و چراغ ۴ شعله میدانی نیز توسط اداره برق نصب نشده است. مردم تقاضا دارند به این موضوع رسیدگی فرمایند تا این میدان آماده شود و به زیباسازی محل کمک کند.
🔹
لطفاً در خصوص شرکت فردا موتور پیگیری کنید. از سال ۱۴۰۲ تا الان خودرو‌مان را نداده‌اند. هر کسی برود شکایت کند، نامه فسخ غیرقانونی برایش می‌فرستند. ده‌ها بار در دادگستری‌ها وعده دروغ داده‌اند و هنوز خبری از خودرو نیست. من یک دبیر ساده هستم و ماهی ۲۱ میلیون تومان حقوقم است. کل زندگی‌ام، طلای زنم و خودروی زیر پایم را سال ۱۴۰۲ فروختم و ماشین ثبت‌نام کردم که ۱۲۰ روزه تحویل دهند. الان شده ۱۰۰۰ روز.
🔸
با وجود اعلام وزیر نیرو مبنی بر عدم قطع برق در هرمزگان، با این گرمای شدید هنوز برق هرمزگان به‌ویژه میناب قطع می‌شود و کسی هم پاسخگو نیست. صبح مناطق شهری و بعدازظهر مناطق روستایی برق‌شان قطع می‌شود.
🔹
بنده سال ۱۳۸۶ یک میلیون تومان (برابر با پول خرید ۹ سکه تمام بهار آزادی) برای خرید فیش حج تمتع پرداخت کردم. چرا الان که نوبت ما شده، حج یک‌دفعه باید ۸۰ درصد گران شود و دوباره ۷۰۰ میلیون تومان واریز کنیم؟ لطفاً رسیدگی کنید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/457836" target="_blank">📅 22:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457835">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6d9ab446b.mp4?token=hNd93RaKebDi-mFTyrBc87jNIsg865ptUext2T4x2Iem4rPNLKk8sGjOw0DxhjpnYnnUoyLLu3YNUhtBk0zMq052EtWVqbSeWiOZx9tbCFAG15atjlnc1FTqMOurs7iG662HqvZXtwT0pUZJKDHS9V3q8PNEbt8DylK4msj55K7KGDGR4C7LrhORl_GgZDo-cQ9_OT50VelWpXYC1NGpoEXCv1lvvSbaeKOfdM8ruGQZ7UuLLP4DuUbLkpg51Ilj69yRFsnzDFcMrF2SPPpuTZ7yV_Mq0WCUMf7udIq3sVSjD9GAALFJsZzAy14A1I6VrmT_NFF_D3U2zFcMd3bN2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6d9ab446b.mp4?token=hNd93RaKebDi-mFTyrBc87jNIsg865ptUext2T4x2Iem4rPNLKk8sGjOw0DxhjpnYnnUoyLLu3YNUhtBk0zMq052EtWVqbSeWiOZx9tbCFAG15atjlnc1FTqMOurs7iG662HqvZXtwT0pUZJKDHS9V3q8PNEbt8DylK4msj55K7KGDGR4C7LrhORl_GgZDo-cQ9_OT50VelWpXYC1NGpoEXCv1lvvSbaeKOfdM8ruGQZ7UuLLP4DuUbLkpg51Ilj69yRFsnzDFcMrF2SPPpuTZ7yV_Mq0WCUMf7udIq3sVSjD9GAALFJsZzAy14A1I6VrmT_NFF_D3U2zFcMd3bN2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تودهنی رضا پهلوی به اینترنشنال و خودش
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/457835" target="_blank">📅 22:02 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457834">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/677a4fdb31.mp4?token=WHhgA9XnNKnSgMqijD4kaZ-bovhsQ4Wf9aQTOojfMw_wcFp66OGhh6AoDBhFUSHSY5te74yd5yylEyCZQZYkNtP9q909N6ki6o8wdtjbwY4G7ggjkbIxuJ2RXiW8DJ1pETicqt-egGTdE7L-acCkpadT-CJ8nSAzEHXHAC-24fpSkrsXFvhKNWx8p71U3kY-WgQ2xm8eWBlkG7U8zDZl2rY9nq5olhdWduiRZuPJ8JfBqx9GlRjcDyRgz6rXpfyNOFp-z8lJ598dPLvbtOkVfKsWyFTLw66A-PQvy4tyi9WaIqZnDoeQZceLgqSIvVH8w_RNRjMTR6ZvmK1r8kCD9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/677a4fdb31.mp4?token=WHhgA9XnNKnSgMqijD4kaZ-bovhsQ4Wf9aQTOojfMw_wcFp66OGhh6AoDBhFUSHSY5te74yd5yylEyCZQZYkNtP9q909N6ki6o8wdtjbwY4G7ggjkbIxuJ2RXiW8DJ1pETicqt-egGTdE7L-acCkpadT-CJ8nSAzEHXHAC-24fpSkrsXFvhKNWx8p71U3kY-WgQ2xm8eWBlkG7U8zDZl2rY9nq5olhdWduiRZuPJ8JfBqx9GlRjcDyRgz6rXpfyNOFp-z8lJ598dPLvbtOkVfKsWyFTLw66A-PQvy4tyi9WaIqZnDoeQZceLgqSIvVH8w_RNRjMTR6ZvmK1r8kCD9zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع ۱۷۶ کرمانی‌ها در میدان کوثر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/457834" target="_blank">📅 22:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457833">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/075eb425b1.mp4?token=NFAhTTXu57WE1CJia5_iYrYOqhBa9dCnVqQDi-F7VlDsJrJF8x0r2vbL5hqgGL_Bxp43k-8S4-XWOi3VJthYj9lpg6aOmqqGmBD5pVDbd4CqEMO6npUBqLhX3VDbzuQ0C8ei9mPkj6dvp-grMdapQan3R9rArXA9xNHSQjpPBh1azfSQi6f5WQecMPnMSVuQ2ByG45kk28WJ6ryXMA3Zf6HO9fF1fxwShGvhuH8CqPaY0kaebX94tlqQ1Wvq-NkPwYP5kpwHFf5m1J4euYUmg_Cs3gelKOyJmuAjqydZN0VL9K-zXpKrUUIue5T5fiqBXY2tpXxmvo2hm0-ebgwwzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/075eb425b1.mp4?token=NFAhTTXu57WE1CJia5_iYrYOqhBa9dCnVqQDi-F7VlDsJrJF8x0r2vbL5hqgGL_Bxp43k-8S4-XWOi3VJthYj9lpg6aOmqqGmBD5pVDbd4CqEMO6npUBqLhX3VDbzuQ0C8ei9mPkj6dvp-grMdapQan3R9rArXA9xNHSQjpPBh1azfSQi6f5WQecMPnMSVuQ2ByG45kk28WJ6ryXMA3Zf6HO9fF1fxwShGvhuH8CqPaY0kaebX94tlqQ1Wvq-NkPwYP5kpwHFf5m1J4euYUmg_Cs3gelKOyJmuAjqydZN0VL9K-zXpKrUUIue5T5fiqBXY2tpXxmvo2hm0-ebgwwzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای قطع کالابرگ به‌خاطر سکونت در خارج از کشور ‌چه‌بود؟
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/457833" target="_blank">📅 21:57 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457832">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueWmWRmBdq1BSJ7TvXkPxYTDekLoJJxsySEFyueUWqb9fwE1S3UP0OInYikmXJnhGhnp4PcWxY-ThdOOQtC4P8kD-eOazFYf3ffRYtlmg_qUNTOwMwlazCmLXEvKz08XXWNXUIGC22fgx3c5CY-KDbx46lvnsP_K-eVWroMRuQP95iJRrVCHR3bBylFUw2ySWMf1sQbSXpJ7wfzuHfhP-9GEyBtLg8b3wqGlbttCFY6BwdYx0vIg9rKxSjwQQTqmqQ7zJZZ6gEujNeVkeLclVt9toTqRbwybM-QH1LkLAp634a6_BclGfdSKB-cZC9Yn04tpv_myp68fGxb5lP3bFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پرسپولیس از کیت دوم خود با نماد ۱۶۸ شهید میناب رونمایی کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/457832" target="_blank">📅 21:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457831">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۲۵.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/457831" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۲۴.pdf</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/457831" target="_blank">📅 21:53 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457830">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQYGm9XdgncswYlsZya4lkez1IxZ9rbBYNcN8lCsCwiMxYejYIPp8SjVeEezNoYCEaIPVLC8i3VBGx_KzDMGLV4SE7Z4ZkHMkn1PYaVWsn1Nuht7CKaiu1kO1sTwIgCR4hHp_IkkjH-0lXVVDhzXjSY_rwFpxKp0cI076oRzoT5wnmKuT8Z27lynLtk8Bmt0JOvTqZK5X75Vki6xYJ5rqLOphvYS_2bKFX_k9kY0MmDg-KmwQD0_Op1d5tZ9Ys4EsN7ExFFOeQZJHM9yCebSbsMC8WZCHdkh6VJFWBirmYMWeXrxgJglXOyVYct-omcx9EkWzp1wlN9UbL0MObJqYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس مجلس نمایندگان آمریکا: انتظار داریم وارد مرحلۀ جدیدی از جنگ با ایران شویم
🔹
مایک جانسون: ما انتظار داریم که به زودی وارد مرحلۀ جدیدی از جنگ با ایران شویم و به کار خود برای پایان‌دادن به آن ادامه خواهیم داد.
🔹
نمی‌توان به ایرانی‌ها پشت میز مذاکره اعتماد کرد.
🔹
جلوگیری از دستیابی ایران به سلاح هسته‌ای هدف همه دولت‌های قبلی بوده و ترامپ به آن دست یافته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457830" target="_blank">📅 21:38 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457829">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سخنگوی هیئت‌رئیسۀ مجلس: کلیات طرح مقابله با نفوذ سرویس‌های اطلاعاتی و دولت‌ها یا نهادهای بیگانه در صحن علنی مجلس تصویب شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/457829" target="_blank">📅 21:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457828">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm9gvV2CcaxQk5DfxvRrEaIfg2v68Tfh-1qecDyGSSD1BRe0wNJaetgn15uUKWRtSfpTr_XYMuIWiYiotWgkpPJEIQhADH9yhCrr7kRyTLmeRIikUg5fzfHIxWrnyaFSP8VuRbrLMkrNZxAvn9LvT6sYoN6DQLrtZGm6jHQ9VzH5I62Js9sZTGqaVZadrJ1EFdXIdY1_i6AbPclY2_WiiMfZQ5y5qwYZsEwv1ImQ4VqCrzss1vIyn80NcLrEOcSp8IMhRSOxJCpAUzPOW55BCcu-PiRy9C9eidqTJrZne9ugMstgN4G1OAZyUs-far4PKfnIKWv7W3_1drEMr9YmfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال آمریکایی: باید با ۱۵ پایگاه نظامی خود در خاورمیانه خداحافظی کنیم
🔹
مک‌کافر، ژنرال بازنشستۀ آمریکا: به نظر من ارتش آمریکا دسترسی به ۱۵ پایگاه نظامی خود در خلیج فارس را برای همیشه از دست داده‌ است.
🔹
چند روز پیش نیز واشنگتن‌پست به نقل از منابع آگاه خبر داده بود که پنتاگون به‌دنبال کاهش حضور نظامی در خلیج فارس پس‌از جنگ است و دلیل آن حجم بالای خسارت‌های واردشده از طرف ایران است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/457828" target="_blank">📅 21:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457826">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yjr57a5FPHZMEOZgvykoMProANiuGIvIZpTnb3NpDd46pcsiBvutedwFDaHtbXPv4coCThtcLQ5C0VaKvrl9pg098d6mpzA6UIvpK6j3OV-nfUBPXUxb6PMMxjUKNZ7uQ4D69rUKtvkeOQAF9-3ljBbcw9iUK642viO1gxcymEk7yAm7vcDQQ_ZRYzBcCisE6uzO2wGMeDm53lwVYVF2UKpN8Af9iqooPv4ZvnvcfYKbA5iMsjZWu8yDj90tbEdVXpZr6pUDg6IOugrMfhJHYwtB3-fPNmq68kADmdRQCFGFv_La0cE3FEeFnoZeFxir6bvORTyLq8Rl1oICj7KGjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل دوم استقلال به سپاهان توسط قلی‌زاده در دقیقۀ ۱۰
⚽️
استقلال ۲ - ۰ سپاهان @Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/457826" target="_blank">📅 21:29 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457825">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJ2iWKe7Ek2udNBNqIlb5G9BOWGJsv6XBAzhj4YDDW5ozldw0NAlsPFaRLBRYewNwiVL642stFHlV63lMyx7MUzhAVgOBs5lQld2A4nXeAe_tUxjl71rMq1YtchBBeNAmYEwhFsy8qMUl3TU_7lLT3UWJOvUu-hnJjp7IpWpRgE7BxNtJUM-s6AzFnJy8lF3Nz2Ew8QvFCSLk-ivtH3PPMLSPBoakt31oqgBu9e4b7QS7ZEvouh8GNO8vm_iwBve3pi6XGYA69zFHHPOOHiVUO5xshleVGsOA01pFBBfMSOUNgWc8SeKwzkwuqVLmIcG71o-Egj8M7YDUxM_cMaChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلیلی طلا را صید کرد
🥇
سینا خلیلی در وزن ۷۰ کیلوگرم رقابت‌های کشتی آزاد جوانان قهرمانی جهان، در دیدار پایانی مقابل کرمیوف از آذربایجان با نتیجه ۷ بر ۳ به پیروزی رسید و صاحب مدال طلای جهان شد.
🗣
این کشتی‌گیر پس از کسب مدال طلا نام امام رضا(ع) را فریاد زد. …</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/457825" target="_blank">📅 21:26 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457824">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjg9iWW6gAWLFK_UW4oDNM2Liz9dT25YFOjjRzV6EB9LPclWTg8pP-tBT7cF4q0LqGkNZOhrHgCKCpE3tx0KXKz7wUoYInhPPGPODZe3R1JocUh-VnomGbRA6TBWsG1CEmG36ytL3qK9cFsq1YG6bR38gUgmfiQDFB54TlIdl-BH8icl-70QqXOQtmCJ69MaC4RhknFrrIKM_RZI5F3zZ5PV9hHn9dm_JCnEv8cik1hkkqfBXHVFmSdP33L5YByXyc0v0H6E2hb3aKDSU41XifSRfUg2NVNZ7fKXlCS5zlPr0eE7RmZ6OawVGsr8RTb4URlLjFtec_n4ue4NJ2iRuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روحانی می‌خواست شکست برجام را در اکتائو جبران کند
🔹
داریوش صفرنژاد، کارشناس مسائل قفقاز: پس از شکست برجام، با شتاب برخی از موارد اختلافی در متن کنوانسیون خزر که داخل پرانتز قرار داشت، از متن خارج شد تا راه برای حضور رؤسای جمهور پنج کشور ساحلی در اکتائوی قزاقستان باز شود.
🔹
گویی قرار بود کنوانسیونی که حتی برخی از چهره‌های اصطلاح طلب به محتوای مبهم آن اعتراض داشتند، به سرعت به تصویب برسد تا مگر اندکی از شکست دولت روحانی در برجام را جبران کند.
🔹
همان زمان الهه کولایی، از چهره‌های نزدیک به محمد خاتمی گفته بود: هشدار اکید می‌دهم شرایط فعلی زمان مناسبی برای توافق نیست. در قانون اساسی ایران قید شده هیچ دولتی حق ندارد از منافع سرزمینی و حقوق حقه ملت چشم‌پوشی کند.
🔗
اما ۳ ماه پس از خروج ترامپ از برجام، چه تحولی منجر به امضای کنوانسیون خزر شد؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/457824" target="_blank">📅 21:25 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457823">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/888787a1ab.mp4?token=t3q9TXTzB4Shu2dp6699InlQEl7nPhorB_Rw3e1nJwlSwsFlBHKaBFh_Tk5QUgwhh4iiSU2eP7NfC8OTD3wQtDpAyulsY6OAlqnix8aJV1AUWr5ow0n65zeDaYUF49wqTo6Ui4CD_5ylYNdSdFcaGvvRvgU93LkbDRyGGPilLmya9maRnJRS6LDJJo2QhsEgYdDTmCitmn6WnR_X87smLiotzSRPt2zjkhDlfcbkDDMAjhA2JhF28__6VBfV7HokzbAo34ZM0GOWuKviVerp9bUA6tmjOQ2OAB3nS8NUZ_0FqVoSEZIi5c1Vg51pcNVCRKrFnX-zHs1ZruJUT10gUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/888787a1ab.mp4?token=t3q9TXTzB4Shu2dp6699InlQEl7nPhorB_Rw3e1nJwlSwsFlBHKaBFh_Tk5QUgwhh4iiSU2eP7NfC8OTD3wQtDpAyulsY6OAlqnix8aJV1AUWr5ow0n65zeDaYUF49wqTo6Ui4CD_5ylYNdSdFcaGvvRvgU93LkbDRyGGPilLmya9maRnJRS6LDJJo2QhsEgYdDTmCitmn6WnR_X87smLiotzSRPt2zjkhDlfcbkDDMAjhA2JhF28__6VBfV7HokzbAo34ZM0GOWuKviVerp9bUA6tmjOQ2OAB3nS8NUZ_0FqVoSEZIi5c1Vg51pcNVCRKrFnX-zHs1ZruJUT10gUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کابوس ترامپ از کارت‌های رونشدۀ ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/457823" target="_blank">📅 21:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457822">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff5cadc4c.mp4?token=IcYLLMEEMNhuyHRMw2y9hwa2eEKHpdEHwPeti5Z9pdVVCQGWYfk-ncMM2PLGtw8GjWfNqx5XuP1zDyZN_kUPER9e_xkoEP1KrCYU6fLc5nDnB3Su40cqFdPk_dZs4xWK-6wWQAmSKk7IDyBHprNQtFZD3yA7m_dzUxBYn7Tzxs0yZT5LMZAm6e2icEyUTLqYkTYYKHhbIuchBZ58SuwCOQznA6aRjxU9aqKmuSSv-iPlYIQ1xAAWn25Pjc9xWnxN843YlLdUCziQPL6kanZiCYC3Ks2KUHTn_s3IInQIxjcxF4b9Qbdsp9AZzfs_m96b74ebc0sHb6HhHMloTTao8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff5cadc4c.mp4?token=IcYLLMEEMNhuyHRMw2y9hwa2eEKHpdEHwPeti5Z9pdVVCQGWYfk-ncMM2PLGtw8GjWfNqx5XuP1zDyZN_kUPER9e_xkoEP1KrCYU6fLc5nDnB3Su40cqFdPk_dZs4xWK-6wWQAmSKk7IDyBHprNQtFZD3yA7m_dzUxBYn7Tzxs0yZT5LMZAm6e2icEyUTLqYkTYYKHhbIuchBZ58SuwCOQznA6aRjxU9aqKmuSSv-iPlYIQ1xAAWn25Pjc9xWnxN843YlLdUCziQPL6kanZiCYC3Ks2KUHTn_s3IInQIxjcxF4b9Qbdsp9AZzfs_m96b74ebc0sHb6HhHMloTTao8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجهیزات کشف‌شده از مجید آدینه؛ تروریست آمریکایی اسرائیلی که صبح امروز‌ اعدام شد  @Farsna</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/457822" target="_blank">📅 21:04 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457821">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4639c149dd.mp4?token=nW0f-TpG9UyzsjGGAqBBX4a6Dh0_sw9Hs33LQrh-wg7z6KNY2EpzbYZEZJZggeh39UWYEFpwrkb4uNYuKcE3a7shTpD5v31K7ur535FXD7cMxKQLZqhgAIcLhG10WyXyicbg694eJ-p1v6blQxYMeAJVbmpENYn5xNTHM9UWd6juPHTqfVWPehsiU1X37RHetavDXd8l1RiSBga4E_LsCJlnUKNkq6WvqSxjnSS4i73k7X_HDp0OKo2F-c9aHZqY9SjNLiYx8OIFz56tF31jP_9N_ypxLRal_U0FmXOrGebdEkfDmXEB5uF3bLAhzjoDx-tSNjA6ZewzVUrM5p4URw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4639c149dd.mp4?token=nW0f-TpG9UyzsjGGAqBBX4a6Dh0_sw9Hs33LQrh-wg7z6KNY2EpzbYZEZJZggeh39UWYEFpwrkb4uNYuKcE3a7shTpD5v31K7ur535FXD7cMxKQLZqhgAIcLhG10WyXyicbg694eJ-p1v6blQxYMeAJVbmpENYn5xNTHM9UWd6juPHTqfVWPehsiU1X37RHetavDXd8l1RiSBga4E_LsCJlnUKNkq6WvqSxjnSS4i73k7X_HDp0OKo2F-c9aHZqY9SjNLiYx8OIFz56tF31jP_9N_ypxLRal_U0FmXOrGebdEkfDmXEB5uF3bLAhzjoDx-tSNjA6ZewzVUrM5p4URw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ورشکستگی یک پلتفرم فروش آنلاین طلا در نبود ناظر
🔹
پلیس فتا امروز اعلام کرد که یک پلتفرم فروش آنلاین طلا «به‌خاطر خالی‌فروشی ورشکست شد» و در حال حاضر با ۲۰۰ هزار کاربر فعالیت آن لغو شده است.
🔹
پیش از این کاربران فارس اعلام کرده بودند که یک پلتفرم خرید‌و‌فروش…</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/457821" target="_blank">📅 21:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457820">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1f2f1d8e6.mp4?token=dUwTkzLEm1rE2vrWQVWTOAjkpri7qra9t4SYbr7U8-clDnJGT2st8W4fhZOnpHoNduDALRwEU3aTVOZBN0eEAA9-yKKpr2rx3BE7IF36exOiRC0R43odiOoeysPOJWtrSfQeTbnAg0x7hTI8o7XDaqjaF3jYI9TGqrDu5msyIPco3NaryxMMtSZes00S29DdxMUvAftWWs-irNZjL7h1zEYVIcF4KiyIC0iKyo3X4kcN2VqMCv60QCMSt0pAK2glLSfsl1Gg5uJpvQ3Q-khUZ-Pe4eaEVF0PptDo00CNYKxLfwd-zvx6pamXqsIcirP967P7gz3w2rHW_FZ0MYt3hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1f2f1d8e6.mp4?token=dUwTkzLEm1rE2vrWQVWTOAjkpri7qra9t4SYbr7U8-clDnJGT2st8W4fhZOnpHoNduDALRwEU3aTVOZBN0eEAA9-yKKpr2rx3BE7IF36exOiRC0R43odiOoeysPOJWtrSfQeTbnAg0x7hTI8o7XDaqjaF3jYI9TGqrDu5msyIPco3NaryxMMtSZes00S29DdxMUvAftWWs-irNZjL7h1zEYVIcF4KiyIC0iKyo3X4kcN2VqMCv60QCMSt0pAK2glLSfsl1Gg5uJpvQ3Q-khUZ-Pe4eaEVF0PptDo00CNYKxLfwd-zvx6pamXqsIcirP967P7gz3w2rHW_FZ0MYt3hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس بانک مرکزی: صبح تا شب داریم تامین ارز می‌کنیم و سیاست پولی اعمال می‌کنیم؛ به جوسازی‌هایی که درست می‌کنند خیلی توجه نکنید.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/457820" target="_blank">📅 20:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457819">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bac1897d.mp4?token=JURaYJXqKO7oomRRTyFsExyFBCdvb4eL6b6amEMkvcLzR025SUMpTwA2JmSfsaiLFkaP29NYfRvhGxbC2dJrZGvVRhSOehdE1MU6IjeIqxtiiZhl97q9Zvj6XooYvmY2AVuruZFmM-1VPMdzPHg3sKwbokYyDtEw4RVpmXEDVnCKkYKGh5DGlpoJvCSuHAMu7taFGwDdKWtANkjhP3QTBGQBXgOQA_9mkQF5blu5OFBCSfh5kqGbOAO9f3Xjo7WfsmIjQUBsdcGoqNxUuqk9ZQ1f1yC5TRGg7CEPkLEa18OGq_5h0fyGFZVSG2qklX8enA721UauNqEgPWj434wbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bac1897d.mp4?token=JURaYJXqKO7oomRRTyFsExyFBCdvb4eL6b6amEMkvcLzR025SUMpTwA2JmSfsaiLFkaP29NYfRvhGxbC2dJrZGvVRhSOehdE1MU6IjeIqxtiiZhl97q9Zvj6XooYvmY2AVuruZFmM-1VPMdzPHg3sKwbokYyDtEw4RVpmXEDVnCKkYKGh5DGlpoJvCSuHAMu7taFGwDdKWtANkjhP3QTBGQBXgOQA_9mkQF5blu5OFBCSfh5kqGbOAO9f3Xjo7WfsmIjQUBsdcGoqNxUuqk9ZQ1f1yC5TRGg7CEPkLEa18OGq_5h0fyGFZVSG2qklX8enA721UauNqEgPWj434wbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک سوال از وزرا: تا حالا برای ویزیت قلب‌تان سراغ رئیس‌جمهور رفته‌اید؟
@Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/457819" target="_blank">📅 20:56 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457817">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86287c9d09.mp4?token=stYNVeMsRqhtoZmUSDXC9N1MMpWpxpKiOpuQ7hhZxzEL9cJkP9DWCsBevuH8c6ycyzleSl20USqYzIkJmkS_6QYACRWLVbOH_v6GOO3jcex_q-9Jn_nxYHQdW02OJvJ1PjW3T6cENUMOypsniIy8RGzuRnuz-cUaPy2HQKWYhh2kxeY2cXjOq1SBLrCYxre1JEkhohqov9v-BhtfapEjowjc64oOjK0NghRbD-aoKwjiosRrYV-42LeUoMN_QCkPNcMBNMwaAKpne-USrXvhxzx1dfqJOZNiJMBMpvlpvxfVJc5uSOXJ89eIgUNqfTaHOC_56qHG2tVBCyWabmWHdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86287c9d09.mp4?token=stYNVeMsRqhtoZmUSDXC9N1MMpWpxpKiOpuQ7hhZxzEL9cJkP9DWCsBevuH8c6ycyzleSl20USqYzIkJmkS_6QYACRWLVbOH_v6GOO3jcex_q-9Jn_nxYHQdW02OJvJ1PjW3T6cENUMOypsniIy8RGzuRnuz-cUaPy2HQKWYhh2kxeY2cXjOq1SBLrCYxre1JEkhohqov9v-BhtfapEjowjc64oOjK0NghRbD-aoKwjiosRrYV-42LeUoMN_QCkPNcMBNMwaAKpne-USrXvhxzx1dfqJOZNiJMBMpvlpvxfVJc5uSOXJ89eIgUNqfTaHOC_56qHG2tVBCyWabmWHdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
چرا قطع برق شهرهای خوزستان باوجود وعدۀ وزیر نیرو و استاندار همچنان ادامه دارد؟ در ساعات گرم روزهای تابستان خانه‌ها برای چند ساعت و گاهی حتی بدون برنامه‌ریزی برق ندارند.</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/457817" target="_blank">📅 20:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457816">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c8219b57.mp4?token=MSxtnviFytFZ_xC3WgP7IvpbCZTME3oWGqhlwHgiGIQV3pxehib-JNW5hvecbWLb1sKwRVN3qYs2FENKNDWhqLLm7hCI7SQUssTjL0U-uba4eWlOrx2VIVURKbCQT3-uYNJyctlJ8LYqFg_oH2XEGvp_VEgeAMdnLum4X3_0JKTvbnfYRzqaLnRYXn1Vov068kCjHAqSAkrV6uoceiTb1pJTImOtTFFH-Qt8eLuCRHq_rqVPsnBEEMq3kl-4bMuUPi78kKZsnYiISvEbAWiq07OV2wR9m5LoV6vapUk1qTphL0abn-tIcp42lIh8axkeV3698sXi_LxJdbaref-DQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c8219b57.mp4?token=MSxtnviFytFZ_xC3WgP7IvpbCZTME3oWGqhlwHgiGIQV3pxehib-JNW5hvecbWLb1sKwRVN3qYs2FENKNDWhqLLm7hCI7SQUssTjL0U-uba4eWlOrx2VIVURKbCQT3-uYNJyctlJ8LYqFg_oH2XEGvp_VEgeAMdnLum4X3_0JKTvbnfYRzqaLnRYXn1Vov068kCjHAqSAkrV6uoceiTb1pJTImOtTFFH-Qt8eLuCRHq_rqVPsnBEEMq3kl-4bMuUPi78kKZsnYiISvEbAWiq07OV2wR9m5LoV6vapUk1qTphL0abn-tIcp42lIh8axkeV3698sXi_LxJdbaref-DQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان انرژی اتمی: شیوه‌های نوین درمان را در کشور برای استفادۀ همۀ مردم گسترش خواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/457816" target="_blank">📅 20:48 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-457809">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbrv0JiQVGeNvcAcSL9XO9O_Gc7B-VIjRULs7B-7issGj-tmWSP_a9FyuGA0i-LQM2a1GmonkgnVRDkmvfoIg4CxsnvKm7l2eQo_R-qFaIMF-u6OgmRCT46keQDKOkiYEVl7pz9N2Nj4c6ITsO-72ISTW4w_2S6L0AmK9ghqJe8d7cCiUJxdgE2PFoUGKY7rOCayEPn3pjFp1-fmKjJ1fMSKXa4D5V0OJP8Ip1skxgFxupULYRUnB4d8ltB-1mxeC28EzgzDwVeVYhrRyXMSKChUGcENbmb3p9Z8gjEl1KOPOxo8Do6-AsBbtio0gtfIpS3qBnwvdFifWoXR3UCL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ubfg3VKwKphv_Pzz73GpCUurqYRkrk_WzwnTo-hiXBhH7tDyMbgSerJc95atNk8xLp1D7H8_2qertGNEj2EQiZPZbl0YR3ZyllS3wIRNjXlPkvQZN-YwtwZuVkcUr_SytooClECfuZOXq7TZilxg6pZCAcRr5HPdvYumYNSh4nGAbMjZ5IKp1-Cg2LmBcku4WRqOp4Ii1nRYajg6M4meVWjKjzTTKSpDPtHzHLa3lLDucPieY-iUOd_0U-kkIinDKKoFnA5T7x00UBzn3jGP4bzTPiNEgCBMSsFL8sf2cWk1JnEKB3pJfi61zLfPsKZ6T7JdTi0gQa3JlyaL3zRuiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YdifkQxLM1KfUBmN20b0jBwZ_By4PRkoffBS3cT-QO9Hdp5FxlogRrSFrXyl-HbhvWMln3bLKRSohLTL1ibN6O4AqDxpz1BjSxRe1GSnvHqEpzDXQD2yYPyBQtRvrXChiV47GnDXPEdktkzU1eRADm61ZMETdUR5DjhpEsJ8ALs9xoBvxmQHcoQ6rD-8f-CVi1gARAHJGDl1VgnlBRAkmFMCGXyz2zS5x-afVx-Bn56RZs1uv-LTJ-M0l8YSzzzN98r9WNLKdSKBj9JeKc5TX5gEtvlEM39LylX_XmnWBJKsa54MUg_Ro7KVPahk1Ewp6UyzC6XWZh-W2xl9rxGJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1Q_vy52F57dlSfm-QDHhZL5_bTsis-fTwptTrTg_gJlupj8sPlRXRRaOs7xt2i9oAo-gDSdwG3Q4y_c6Vpzx_iCbjHONVYQfnr9RZVER6dsVo5aetGN6q5YrhtCuR-HGlBPKCcbI2en6rYXSQ1skWL9sNoPU_qb8JU4Cm6i7mjqwK965URd3yS5lW8nln6WOplhsPzcKnr_b6tFC40vyCmQQhowggpofE1hG1YhgClA4ntPkgdLEC6LrnnziZEpRdhVSWAOciizAlznUgnsBLguYwdda6e3oKzacJZn62DpDebB9LQQ4N8BM8La8eNf3z2ohZJkuUIVHfBnEIQ7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eUUFrC-n3CS3jWEfxwH-T0xtwjoB5rQ6W1390nrJHu9xQBzg-GPKclhjXNlWM1ozZ6n-l9iHzfqf-Kjz3CKOXrTk8yk9QKDBY0GvIes_qzg1DtRXXxWX8f1qXxWt_tSX6I2ZLNmMlZIwn9W_Dz44wkDYatJJQbblf7X4we2imOdHEx1Fxf6_AIL_8GmcqsBpGBpl1xkA4HZI6ZtgJmBzksUYvM1o6RrFVKB5K8wAT2_AQG_rJhpXyDZJbLVUWttD4JQIM9fGPhB2GAcXevTVoWXalEo_4wGMRJ_UcjhZVxmobpvlykHidTTOkBugdlRJtwdGKzkHOvPwMSsnC60ekw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iK6HE4yPAIujSNemFTkFfuVKIquU148FSOaJTBL-sKsb-7tbE-O-quD72xtQTVqobmm0pSUGskMbLjx_3pOJKlyZdpN6amndXDIL4WcJON38Jrr4pgaFn9FuJRRP5hVhaFWDgIr5PTisxghUzjfsSGjZEkQvSInYWqKPNPNq02vRIlc7voAKlp3Wrp1FOzQpIxdDEztAkjY7P8_5arKko39fgbIGxpRxoX7Ga4bcbbr7wpNkOdWBuUsmsox1CFZONd_S1fAb5RAUCNFqP18g5bi6YyelEFRt7L4oSdb4qo7aoDuIr8yWo6d8ItVLAJLt6_va2mZBcM6LiXEKMatCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vVQI4ZM3ym0oEAHMCdlRKcIPJmgvvojMwRGpgp1HwfjECj3lizgV3JJmBiYNCEFMNtfHJmYlczkwrcV_qP4Vt3DnKfAu9RVXWrjBYuNRd4aPlPa-UuO2fS1cmTwqC1IDRo2JeXO04YIoC9qlwpocMzdXFXCPRSmFl5VpWUBtk0Cwnorp_zLAKMxgpMYImWQSdq7xBC2OPeqJXxTHZuiZnQx-Pig1EANrGWqWLboRR3z5_XcjggXu8aYVKliSLUp5WY2Lis0NfsUXVtxokwddtnmXkTFadIM54n392l8sUFJD8N8EChBtZ045UwFONHNMQul5ujCXc3OblEQFjTzgLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مساجد تاریخی اطراف حرم امام رضا(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/457809" target="_blank">📅 20:37 · 01 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
