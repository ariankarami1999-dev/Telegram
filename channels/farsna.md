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
<img src="https://cdn4.telesco.pe/file/XWhGhTsSaTwA51xnpkJhel1-cY925AvHSfMT07ZnVCD4fBRGBpTjH69mWjSCTpGG_d6mJEscm0GuLNX1uZQTPBxQzPqJS3Z325svfw6YW1n7PINAan_7hJV-HEsJ7MqbrGYEno2BtLrPPtUiksfykdc319cE-kTGykW4N1_tGj7DQBCDKxAiC6T-aqhHWMy-wSmsjTa91sI9gjuKW1Lb-jYZQINsROuXcHV-wdEhSQsRdGu9TmJ3FEhYNVFnqODwsL0fltPh-9jCzjV89fKIi0iJZFIZ1fxSSIC__18a_aUW-n0JJiiqQq8NtAycWFyDdZAhZ3bOlKC5fRvJvEnAug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 06:06:21</div>
<hr>

<div class="tg-post" id="msg-445570">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7963c2a9.mp4?token=NECkxalbnwu5zH3fFM5xJv9vaPA4JgYrNbN0IIWka6KBPEvhNlClXOvl90qq7DApUyAPEWjQhpAsXL6B3BaD3_1GLgsGb1gHUIXQ5FoAuubSTLuYmY7rPBxfnJi8MjVNtcOMDRg4-0RqDs9mAiTuoBBCtwmGlMlH5MKT3JQ6P5qzhq_H04J-3O2xWr3rKW7JojEITzrJaRNlzKZ7z-m8vGq9bg0uf3x0DQxhfCSM2x7b_lyaKx4M8exMfIMrLckA6lLR94JMnFpRnJzYDo2Cs-M_on2SukGPjrTo40Tnfm2R_pKlLGaDBXBeKB-qpI-rDPOV9iCoBYqMAi9-UC5bxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7963c2a9.mp4?token=NECkxalbnwu5zH3fFM5xJv9vaPA4JgYrNbN0IIWka6KBPEvhNlClXOvl90qq7DApUyAPEWjQhpAsXL6B3BaD3_1GLgsGb1gHUIXQ5FoAuubSTLuYmY7rPBxfnJi8MjVNtcOMDRg4-0RqDs9mAiTuoBBCtwmGlMlH5MKT3JQ6P5qzhq_H04J-3O2xWr3rKW7JojEITzrJaRNlzKZ7z-m8vGq9bg0uf3x0DQxhfCSM2x7b_lyaKx4M8exMfIMrLckA6lLR94JMnFpRnJzYDo2Cs-M_on2SukGPjrTo40Tnfm2R_pKlLGaDBXBeKB-qpI-rDPOV9iCoBYqMAi9-UC5bxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار یک بسته در موناکو
🔹
در پی انفجار یک بسته در مقابل ساختمانی در موناکو، سه نفر مصدوم شدند. به گفتۀ برخی منابع خبری، مصدومان تبعۀ اوکراین هستند.
🔹
بنابه اعلام مقامات محلی، انفجار پس از آن رخ داد که فردی کیسه‌ای را روی زمین گذاشت و سریعاً محل را ترک کرد.…</div>
<div class="tg-footer">👁️ 169 · <a href="https://t.me/farsna/445570" target="_blank">📅 06:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445569">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">پایان مأموریت اوسمار در پرسپولیس
🗣
طبق پیگیری‌ها اوسمار برای جدایی از جمع سرخ‌پوشان با مدیران پرسپولیس به توافق نهایی دست‌یافته. به‌احتمال بسیار زیاد او امروز، توافقنامه نهایی را امضا کند تا جدایی‌اش به صورت رسمی اعلام شود.
🗣
طبق توافق صورت‌گرفته، باشگاه پرسپولیس متعهد شده بخشی از مبلغ قرارداد این مربی را پرداخت کند و در مقابل، ویرا نیز با امضای این توافقنامه، از دریافت سایر مطالبات خود صرف‌نظر خواهد کرد و ادعای دیگری علیه باشگاه نخواهد داشت.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 1.42K · <a href="https://t.me/farsna/445569" target="_blank">📅 05:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445568">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvgq1-CM3aMZQQKuBhJNSOL3iXq5ER9giMi4igFM3l5afWf1wXdPbjxI4KJpqEwZtanWa9IAXOnyQeS6Jb8a7SIEmlOP_iMi19WBde9w2ETr1yGnQCqe0FOxYhInNUGTeCHK7DwPKL_tJo_pSpUvixmbfpJ9CWF6aQq9Eg4GrN_c4CWMvg7M4V9CwL7Qu-LmbiqlJF9wrFkv9mtQ-6SGACD5E6P0R33PMK2cF6qIyIYlF_We9RPbd7ujB8MFbzq2ajnyC5HNa4RLuND5I9dRSINzJSjD3eOF3XlPi94m7asJrUVmbxf_i9MyY3j6U8KSffzFHN4TNFrQrIoJrtn58Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ ستاد اربعین: هزینۀ بیمه زائران اربعین امسال ۲۰۰ هزار تومان است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 1.87K · <a href="https://t.me/farsna/445568" target="_blank">📅 05:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445567">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ez3nOuTzlSWTOfePlUhwePb0xSNxZQES_-9uLNucCBKGRiGefUKnFC2So3O4k1G6Zi309cNIK_4H-d6RcO8S5tdJzv3C7s4nzZEowwfsiSZatT32Q-En3sFCPmV-L7JFTYn7qjWBhV-X6EPuds-yG9ntn8dGwpq4IzL9y9kvE_DsHBtBRCe7KBakYo_YOmvOIKwMlJuwyHyVC5ohGSMqbu9Jk2QubRbmXnAkTCNF2-gfjGK37_WzwebAGRfcBVERh76FeZbtTaHsQI4ZpKc0oalDfYkjo14S-k8tt7VNH920zLRIDvz9IABIbxGXHIstofJQ1vPklVH9TgWWUnV0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده‌سازی ۱۳ پارکینگ در حاشیۀ آزادراه تهران-کرج-قزوین
🔹
راهداری استان البرز: به‌منظور مدیریت تردد در ایام برگزاری مراسم تشییع و وداع با رهبر شهید انقلاب، ۱۳ پارکینگ در حاشیۀ آزادراه تهران-کرج-قزوین آماده‌سازی شده تا ضمن ساماندهی توقف خودروها، از بروز گره‌های ترافیکی در این محور جلوگیری شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/farsna/445567" target="_blank">📅 04:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445566">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815edfc035.mp4?token=DQO1XA3IoRKkzVzI4QCHgX5c3nRZ2YExFJRK_eovBRldctpyJhLSJSWlIT0nyhAoyddqOo0rXKTJBdiNsfq_9glJYfXC3nrj-i7EYH-ovU7NVPtjJuDFoNRZpMbiVSkfxoI1mJuiBT-mtGnAT5vS9QTxRiKVd2MLrqD3XBZ3BcvZyBIM97T2kAMkvE6qADo07wWjVhdd3HrMaOMgftgWlvrNnJVt-ZJiHqAVR0AdfB05XpD-P5pwOc20X2LDYrHVldauZ4XgJNlKfI5rSNoWwjrXhg6IVZYa8nxLGV_GLuhpc6fHahcqjI62vNYYUO9Z4MUT6_gGLperypJRyvZcFIaGGCZ3k1pk3EJ4GbcJi43ToyJzrPRcRfZACLSu2QB2DnqHHtcU4BBxmU8C0VvsxEjf8Sw1nKee0E1DpdqAB-RJaxk1zAY1boeAXKbiiZ-gqt0UdyHP7kaWXtSKa2XD5Ws3cI4Po4WtYj6Xpx7rxOqbdfeOanhTo8Cr-4NKaNNVxuUArLNnY0I9DYphFg-julynodRg739vOThwY887eT5fGnebXxz0ZCqz0N1kFp3v36M_SQmJww9k7DBtBjvrJtUr0Wjf-rLBn1fhxatdWFo9HEGNlm3qgIh_BtZtEiqAZ27UftexYE56XuuB8h5rXblmlRPfQxj9Wuc0TSsbzmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815edfc035.mp4?token=DQO1XA3IoRKkzVzI4QCHgX5c3nRZ2YExFJRK_eovBRldctpyJhLSJSWlIT0nyhAoyddqOo0rXKTJBdiNsfq_9glJYfXC3nrj-i7EYH-ovU7NVPtjJuDFoNRZpMbiVSkfxoI1mJuiBT-mtGnAT5vS9QTxRiKVd2MLrqD3XBZ3BcvZyBIM97T2kAMkvE6qADo07wWjVhdd3HrMaOMgftgWlvrNnJVt-ZJiHqAVR0AdfB05XpD-P5pwOc20X2LDYrHVldauZ4XgJNlKfI5rSNoWwjrXhg6IVZYa8nxLGV_GLuhpc6fHahcqjI62vNYYUO9Z4MUT6_gGLperypJRyvZcFIaGGCZ3k1pk3EJ4GbcJi43ToyJzrPRcRfZACLSu2QB2DnqHHtcU4BBxmU8C0VvsxEjf8Sw1nKee0E1DpdqAB-RJaxk1zAY1boeAXKbiiZ-gqt0UdyHP7kaWXtSKa2XD5Ws3cI4Po4WtYj6Xpx7rxOqbdfeOanhTo8Cr-4NKaNNVxuUArLNnY0I9DYphFg-julynodRg739vOThwY887eT5fGnebXxz0ZCqz0N1kFp3v36M_SQmJww9k7DBtBjvrJtUr0Wjf-rLBn1fhxatdWFo9HEGNlm3qgIh_BtZtEiqAZ27UftexYE56XuuB8h5rXblmlRPfQxj9Wuc0TSsbzmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام کاشانی: اسلام دنبال چشم‌و‌گوش بسته قبول‌کردن افراد نیست
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farsna/445566" target="_blank">📅 04:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445565">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGHUE1okRU37Ta5Z3G6h1weTQiTRqvGPZlvcwkXPO6fvd25YSbOutqAENGeh22UEI0E0as1doOn4Ca2F3S0kyXiVKixBvCSL-5zp6iCvfjXBFAqmAnhw2JLbkXdILeHYxGnQ8kahCaX_SkLtLpP5opZZCViADzRITBcDNAmJtrNmcjmrYXBVipSEhj0y-E7ESIicnGfnua5LaQvhhWuKSpmwii4QRpuTCVR9KpXRAyNgvX4KVoOjjWMyY-yafFzB54wsnJ1hm31-oK87I3PWuJy_ecOKF5JlhTymmVNkl-w-j3oR_wMtcMT2BMKHkqTYbWnwFPSxkMaJWaC1I4Z9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عملیات زمینی و هوایی ارتش پاکستان در امتداد مرز افغانستان
🔹
پاکستان از عملیات زمینی و هوایی ارتش این کشور در مناطق مرزی با افغانستان و کشته‌شدن حداقل ۲۹ شبه‌نظامی خبر داد. @Farsna - link</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/farsna/445565" target="_blank">📅 03:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445564">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/seHapIieHXctRH2y5Pb7EIkB2pq-RQSMaA5dG3oifNNPbhZTSo2wHu-UTmljrFkL2qETomq5LNRt5D4hEvZ0a6CvWf1om8h1YrCfuvYv6HpJ5-DJdi-qz-dRm0zBZbFHMFLOt7yaOdMK5Wl_J526cESPdrzx_HVi35w4kH1p_14k4fIWc2BuWczI6wuYatWBZeKnU4tyuPHR4VIzhgUCmnaFvDdfIF20wLmsNZeLIoJQMo8NaeGGxHRa30GiJh0XwpYylsZsXsj8oJ2iiYf9yS8ZthqncNb9zLsS7QfjlGUAjZtiPiaVPDb1Mo782pXZtlWPdYbJnMJ1AaqioydGow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: ناتو، تسلیحات دوربرد را در اوکراین آزمایش می‌کند
🔹
وزارت خارجۀ روسیه اعلام کرد که ناتو اوکراین را به میدان آزمایش خود تبدیل کرده و از آن برای آزمایش تسلیحات پیشرفته جهت حمله به عمق خاک روسیه استفاده می‌کند.
🔹
به گفتۀ سخنگوی وزارت خارجۀ روسیه، ناتو در حال کار بر روی سامانه‌های تسلیحاتی پیشرفته‌ای برای اوکراین است، که جهت از کار انداختن فرودگاه‌ها و پایگاه‌های هوایی روسیه، ازجمله آنهایی که در عمق خاک روسیه قرار دارند، طراحی شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/445564" target="_blank">📅 03:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445563">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDRQ6Oa1Uv1Koak0uZ8XBt20GcfI5mkGA_iKEaNh7hCiKmO8JwV8PvGmVbFNearF2dXm0HdrQCxyUcABm4MXemOgWmS6nPKCDW1146INADfRa8T3BzatBeHqmTjJGhnp6h4v9YfTVGYcCJ4YrBZFiLGmgyrMpty4lovfIBYHfW0nCAxEcYbttYgxJS8psqvlCv1Oi9TKixj9q7W0384S8UFEk0ch8DK5DMoRhei3XwdznO0t3SxVEbhGecdYpsEMFdr3JqF4Dhz9IzJt04i4RJxyDAhNwmy70640pSMc56DA22CHRYKZD7aii24uiwDWM1lQdEnqLEtclZTjXrXK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شگفتی رقم خورد
حذف ژرمن‌ها به دست پاراگوئه
نتیجه نود دقیقه:
آلمان ۱ - ۱ پاراگوئه
ضربات پنالتی:
آلمان ۳ - ۴ پاراگوئه
@Sportfars</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/445563" target="_blank">📅 03:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445562">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSV_aLPuJIxIatRC5EF3FMeoPQEn-OSsVMnBS8H_Koft-bnEI-rWMSNGvLuv5JBwS8LYNCGWKLPO7-t6KtNCQoRieIOTuLAQgWpZczhXZs9iSYRj69011ldB04MGHQDh-Ts0-rw691dJYkaNrjCzng6sgtLc9sigT2F-jLiMn_rGuFEz81R6GCMEgyrzsy8uT1bBww_NguAEDLQuktk-1lwR_nsB7vDvclkGPNLLOWAkURk-OLmmUQk1xIqRjbpqjNRn3INZe4u04lXdWI3SjXG9mr9MBttxpY_-sLU_Tnr_38Oom20IYlWOJe_o67xwYujwCQFx3ZCa6SIlw7GePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقش محوری پایگاه موفق‌السلطی اردن در جنگ علیه ایران
🔹
منابع مطلع به یک شبکۀ روسی گفتند که پایگاه نیروهای آمریکایی در منطقۀ «الازرق» در اردن، به‌عنوان یک پایگاه اصلی برای حملات علیه ایران عمل می‌کرده است.
🔹
به گفتۀ این منابع، در مراحل پایانی جنگ ۴۰ روزه، این پایگاه بود که به نوعی نقش پایگاه منطقه‌ای را برای عملیات آمریکا علیه ایران ایفا کرد.
🔹
در این گزارش آمده که واشنگتن هیچ چارۀ دیگری نداشت، زیرا نزدیکترین متحدان آن در خلیج‌فارس یعنی عربستان سعودی و امارات به آمریکایی‌ها اجازۀ استفاده از حریم هوایی خود را ندادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/445562" target="_blank">📅 02:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445561">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLLaHBf6u2Rt8iYKRxym721fN5db4kBa-gShZAPw7pbGNXdI3L2ZU2y9BLA7zHZH5qnnBglmqDhFRrEpOxQ3dwsZKWuaiCJrhvc4IqmpkcNSJjhLhDeE9j20ZGoST0JrlOUYuPAHzmI6JP2XV03bwpFpXPekZlEACePCbAnaliUsloipp0-8NajTE_RP615DACoHW4V8vRmMH7wGp9pxnOQ4Io9H2kSPT-qR-mGCxk1-RwlPmVZERX9hdcpy6huXWPae_dNwt8bIxCjp2AbICxO4dScmfaGi3Sw6tt346TohrCu7d8PlthgkXQi8JENL5SYljV50EcGDBiiW6Cgxnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر عمانی هرمز با اخطار سپاه از کشتی خالی شد
🔹
بعد از گذشت یک هفته از رونمایی کریدور جدید عمانی برای عبور از هرمز، داده‌های دریانوردی نشان می‌دهد که به دنبال اخطار سپاه، این مسیر اکنون با توقف تقریباً کامل تردد مواجه شده است.
🔹
بر اساس اطلاعات رصد شده از پلتفرم دریانوردی مارین ترافیک، روز دوشنبه تنها سه فروند کشتی از مسیر عمانی در حاشیۀ شبه‌جزیره مسندم عبور کرده‌اند.
🔸
این درحالی است که از زمان اعلام مسیر عمانی در تاریخ ۲۴ ژوئن تا پیش از این تغییر اخیر، حداقل ۱۲۰ فروند کشتی از این مسیر تردد کرده بودند. اما به نظر می‌رسد حالا اوضاع به‌طور کامل دگرگون شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/445561" target="_blank">📅 02:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445560">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olqLIrP56sSdqpajDih1sL_igOxAtAh9iMmo7pxL8ZqFt2QO4C2wIsCZS3Npe5nIGFr1yaefCMj8ILjwsyhSA91dWh5vwc67MjR5kvp5bdEop4Tl39TRn6DKNKqiZKjzk1u8qLziCEkcyqFSwyxITQGZ6YaDIVBrOilP1x-cnJJJbkwXRzdx91ZqnVNzD_3hnRH5A8wxtF338FEdnpO2-hSjXtsE0jt3p09SoAaH3VZOA0QXe9gAsrrv2ivGz2jzoG4GMh2N3hwsSlB6gNIU79IiaK_ijYtj8jVorlUaebbqW20yzSjSf2J47LDePiAUuPx6b2sVc78TtwFOk0l24Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این سلاح‌ساده، سربازان هم می‌توانند پهپاد شکار کنند
🔹
پهپاد رهگیر روسی یولکا نشان داد که می‌توان تهدید پهپادهای انتحاری را با سلاحی بسیار ارزان‌تر خنثی کرد.
🔹
یولکا با سرعت ۲۰۰ کیلومتر بر ساعت، تا برد ۳ کیلومتری پرواز می‌کند. این پهپاد با سیستم قفل خودکار، از فاصلۀ ۱۰۰۰ متری روی هدف قفل کرده و آن را با ضربۀ مستقیم یا انفجار ترکش ۳۶۰ گرمی نابود می‌کند.
🔹
برخلاف موشک‌های دوش‌پرتاب که به سنسورهای پیچیده و سوخت جامد نیاز دارند، یولکا با قطعات تجاری در دسترس ساخته می‌شود. این یعنی تولید انبوه سریع و ارزان برای مقابله با حملات فوجی، بدون نگرانی از اتمام مهمات که مزیت نسبی بزرگی به این سلاح می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/445560" target="_blank">📅 01:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445555">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nxbsri2LWJhq9E-9EdgBHTP62Qrt64utEFCgr7W-yY5Q_EWSHBA1J5O1MbVDCumNCKjX4TiddQQDr7gQ4fGTo652CWcMQqY-WCOOvNO46GQ25myVqj9SD54JjMJPo9tLUlLP_XOGo_frTop-4z16Ih62BKvZPtKjcbU6hBo-HWUs2Z8s9AOwJZqIwHgw4xYQtKLLpS9E0vR4YNcZ6nw8d_JMiEZSwvUtEXArlZymVPDsigiywMsgv6Cz-AyEswiZu8hQZOPVk__bniLpGJpmyCxaaxgA9nYIHCBEdTR3_4v1YUpNLMkiPO2BXt3dgnb6qDjvgzUFOPB0ht_8ClJc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPAiAQj0Y47Bkgijv79fbHzxsR84othD6Lx4VLvLg8vAPPz6AUc-94Ph8d4tgTt5D_SMQTZUpXosUYq6Z0r0Bq2QzyewiLI9FJMR9nZtY1_rH_H2OmOo6ktWnzU3eGWuoseIf4EGbI4kMLRZCMNI81qTCUOT-uuuTNaxS9gKUzsXs8f6S8sUMLTzcCmzUc-fl70FnnMaN_sdOgEvKcL-JmaotMecMUyiypmVQpGQVCFvWVPtN5LwCGuLnHp6TSuD3GPu5umaKYvIjguQ1dXpfgyLCOFav7ZD4ai-4bCWKMEwjAIeO_2hAIHOLvCJVQJbv6z2Ck46Zgh_264PyhfEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ImYCPq-0D1Fl_Z_xGsWWjGaPm8KDUZEbGYa6q_wWPrxf4rSOGc8ZmF-JVK7gh8Y51hNFJJCI_yt4uZYCN5lJr0QYkcwQvrMtM5QnxYmvc0TtsKCxhuBrMPp_LbmzIc2fKBtXsmRpCxS0RvHyBg6ExFi899KWOAdRr5TjtWQ16St754ooFjXi0AUilyQXzFW2KSODbYd-r-7nogZWIcsE_YeRnGfLlZcxQAPP88Ma89aCCNixDeTWR-5uXdT73BZN5TTcaIeE87ogcjHTNDBnatdNXizV_IqlIy9pO0JRuDY5E2Kv4DkTP043y_URdyMUtqJ1YqOIawWh0q4H14qyQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feLAmCUIE3Oi-dNIM-hK9RaaziOEETRksix1_A6Q8-9JzEb1aBMEwDDSIg8ipXuV8Idqq9pODMOeSbW6SoAFUmZ2uIqV4WeJaA36h4fo1YdY-LuBaGlsdlDztmg4y5Ya-1Pz-sWPj_T3GmOfoKitNN8bYxBSpQTSpBQ9llUsTp9mxBsxVnzJGmjUsf-2FlPdkV9XykHtFKPpwb4jha7GUoULvioZUBCSKNu1K76D7D6_4xE7TL9Y8JXPWgHw0v7Ex5yg9HdgoOaX39NhYbl_YfZb31AqzP1l3dR6DXbSxMrHwetWVLJIWziEerTH8WeqtxRtpeopw1Hul3lH9YckCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hGCISpwTdCIDzH3WL3L_GtSLrI0S9vwFad7VD5kLD-p9mW1TOboRlNj13NnAA4BAqVKR8Ga2MG7bue0-Vf94YHGI-n8eq2_hY5pNfAdUBVKdirAEsjjsLdjMbeLan4JMCG98bicoNtlHH5oOwPIKN4ucU-SdJdZJ8OlkW1zVHHiTUn314cdD7MiX0YJQifw73MUOYnyMGykUXtBe1npuCHP_MD91hgO2KfK6Iy6pVfj3deIbUvcu1izgV0-htuvlX2CMc0bs0kLQkTyCHVf-fbvmC3XkwCAS1pEll-4mUa4kQQIvJCxgHxKAXib7fA7LuKcTcdY-tECVdOLUkGABpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۹ تیر ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/445555" target="_blank">📅 01:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445545">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IS7MQJZDSjSRMLmeLEn4kr03LzQCip037gBoZ5nl6AbXmp-IiK95YDu5_eLXS72w-3d6ACHxNGgvBKYYqA6nT40FNBVw6yugYW2oSQ4ao3gsnaVESIXyzkeWYCMGsHH26RghHL9Ku1RDNYcgJfk8byIIEOnVypnHn26QYNsT3V7e5c7N1tOQYoM88Ht4JWQz6fwgM3osjssMuRrYtZM6T-WPgiwGI9zAo_sRl8MTUrRYPbvqYK4viYGyVj-DNhbCe9IMsjQaNKdUU7GewdMI9QcbvRB_4IYLQSAzeA1gw02eu98_W7xl3eYDq29c7htKwLbVC57_s2zgnE8gq-Okdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HksCLHyjxsi5SE9o4bGEzWtAb-Y9eWuIBKlgmqTA_xfh906s1CHuke_pbVl44xiMY_ofJARMDXyF28o-41ntfpsm6yBagtFytGD-Yb5FQzx1tjY1ary6FLkfJ3__yRLO_CR1zFaqhcwdyhlhVthbBERBfsEkFUPxrNfzo9cis0W7G89up6alUfLBZEKC2xVsQS-dNmUzoR99srMU_YAgyah0oFQEIaWuyREH_izE_dxgxOAMMfYbkvcU6aC-vJhsb2SX3oyf1MGAwbi5JOS7o3lSJVupZkJfVL6_LQ-T7zxqD4m64B62O7jHEX4T4JO-H3AKtpsGk9qM2R2m0OUshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYJl7Fh2iJsDNbOGj_y8urquy8yCqQXmp7u2HCzZPNIVhU0L-cYKSq25tyxGr6DrvCOhzl7y6nMZA0IyczqBAgt15afBeHZCNIWcsI8v5Fg70LDJ-j-GWhQUH45Lb_F-L0CDRE6MoXvuS_7a3yDAwZO7AqPrGjIM1QrxNYb-9aNvxfZvSUIKpotPBoLcRXZfHbAzE201qjMTHvdk8trsw9Z-yzCLa5qpIHtLBktgK9abmYjBkRc6PbnKgeUgOw3Ijxu-J2NOjSmEFhJLN2uAEBP4sM6LnPKfpDvR7G-GFxw9CB95SHHorSaMG3h62DN5zMfaTTB0ZoydoQjscDxidQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJiZRtLVj2ZufKAJSZdDFnArqh8WF9qVqiKO-fKvUOOrRtzHB9MSuYSl1IAuLmFAHBw_yZK5GfHrby3xhMujXO9_3b8vg_zmHlp5ueddss_KvOml8e0NTjJW5gsCu8g-C-J5wjb3Q6Orn28v-xun8ScUu6GJBtKyFjz2g970FNNa_j3pTMVu7_gyYu-mf2P4KQjnoGn2x4YxohK1pDQe-BdQ3Rj9D9v46bfDLFOY0ZObWsoSJVKZqKQN6KGMhf3ot109NsH0xW8y8yKJL-0v0uYhPWhpgwNErD0zDsOr9Au3joY_0In7ZnC3Zajix13Rj0xbCcBndsXdg_1NYH-h2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbipsB3ja54ZUL4XJd9NKVjfanmSEfJwmT99lt2L1M7Spf2YnBpBVqYiKbcO_zCg7XBZUvIsRUuYxq2QAVsXIyhbJuI1RJ6p7GwTDQWKEKZ9AFpf6IDQh4XH_9RYECkipgSbBonstqLEit0DBYl5ajD6vwU0tILIfbmJdOGtF6M_SU3e0SpUFNAbc5_UXHocgz8bbxV0Rew_ut7rXGX4Q1q5b4MkguWUZDERToGAoMnElOP8StbJVYTk4sQ08EVOs1OwqnOFCc5F_X-hnnc8SSyZf9DSa_DmXtyVey_5uSKwTr4U-PJg68WE2fyE6MM-gML__yr489NXOMb7GoYRkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GP0FMUXGyB3tubQ7vihFTDF97pfVMBRu8K4ZcS8Hsf_4ETak6on6_eWKmH0xPCmyJbsBoUeOwFk3kCrdm8L2qzh_lJljDOwQksjX7hZSV-qt2eJ81hhwX5QN4tRjtsezTaOIH0OhXmxVwd8_xXld1nxZJu2J0PgVng0h-r8amKc-3QwqYGQvaTc7FTqDd8BG27KSBIYfiX1TooBkes55w3NYS2ONMYazWs3zDl1Vh0giwoCnG4hFSX2UT2mFCTBtIQvMp_XiJTCit7lcOGtR4tlQVwb9OqgAJwDs9PqjI8xFbaobbDPqYjw6FzAIzdLc0w5GBK2s7lusRLqYlvhdnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fhCZFHoGg5129TIz_UQkCdbMZV3w1J7DsjjQo0exmFeA3rBu8IkThd-D5NNC6mNs6kO8OOvgRypwARgysqS3cjGMMmyXObm_Eoy0oltaX1YlcQXIN0VGjWpaQBb_ruXiGZb0eV9MlzVg8aAt2vDGFrDo7a-Y_vGmh0Tuy5rUO5vxvbx5kOHQcqi9kRnQiK1uXGtHvEzjSkA-d1qWLYeX28eNot_Y5AyYv75f4hw0JXTVSOrQc7h6hFCdzhG_ZP4D3XBZgI_ecs5NLepHPomGT1eX6GgVsJpd2R7IS365PFzurGOsZBQXos2rJLbX70FW5mqkZH1gQgGGQYFyr4qEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZAnoi1JM6fdQC_ndoxNiLtZQrDVc7psugg3VdqaBYFMDvlY46YwuXnhncXZphbKcVZiRPmyKDHDWlRSNWQ8WB1QTI-dk6KLTWDB0lF1bcOk9LUANtI7PFsyCFVP-zA78q52qIYrXYHlcjv0GRyL1_gzPk533enTCnBFx0DEyRkMqzhK8UMrIcxmt6rwUVjDFOtNLOqQ42k15kyJgUgaaqMKiPdvKwmwBSqNX7zqr-cn5drKT5zcVzvDTBMEASjyw8Jy498vov3s0-hmDLkIZ9mzstjvfcyPUJPkQG72GfAPpUIPezCR8OFJD5x-agp7rEZvPs2SlVHnaP4pevO82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTpKHpo07uIn9TsoOYaXQxoZ3CpcN7i8q4OslBwwP_uxSuStaC6fstR7U-3QL95IZ_V3oJLjped3--5mPQ3O7Jl8x1lu6B-vJa_e9_ZCIIVSt8U2KHqtuisy6HrLF5CKHuGtzSHdXZTdovcdCPaqowlrG2Y0D59MGAOWLRxh-FyxBgmP9Z-pCOmC6ZspJ9NoIi4l6eI_r-PoHLgLtPqvVRzBrazMnbFz0HIZowpvytOQZQEu7mP_SFG2ohe8ZiQbg-TW2P09LWqwYoDh2s17xNvoSBadLC7RjtYR05nku-bb02NWhDLqyWzCE0k4ocUr-nNw8PHvL9BaJH9jlMJ4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZbuzpAWkEt1tbSFiG8fPr27mjZwE_ybOUCHgosLz3RNUjnN_krIm-my3AArlx_p78k0IvXfdmWkQSGbmcsJSXjTrUT35BQuziBT2ilq1cvxsB6ygUpfRqCJUMOUaAJ6XJcYzVCKywXZAfbitOioRcnAnMEg6bsCzLS1szXdzqnHazFayVvhF1qPW4GK5xQdkE86zQa8mOfLoiQGfD7HtAxAZ6MHTI7MnxXuvDd-V0HmAxZdLXiWVYzpvwe5OoowvITYUz3SMPm34pu_BLv_v8SaeAihZlEuFk-wf-FUnb2c9_2PVbAf1EGeXAFUSQdoMAvK4uPsEugRp1_Qic2N8yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/445545" target="_blank">📅 01:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445544">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1956d75e.mp4?token=D2LB-pwgFwLPe29cyMTdtwmrSRQy9nhrxWymHcKEUVbWd8DBjM4UOYX2BMwYunxWVNiuHR2xuquxbspKi6KsDbLLpN6-T3NVad4abxd6pEVLELU4sN8D1whUjm36hIJNDgg0tZHXAas_YkK14upwKVfSs9St-utqParggxmFvoSaCDuQjmE9VbSJv4iOigx949UPKQkjb-Cf4U4WFAnxQknNNJEh5Fsjmxw54hzEWAU9tMKyCCGnUcoVWj1FgjTumJfpjKi1m9SoSVF_rFMHJOdEDI_g5Mxt-2Qu2C1duZWaRP1VaVgsMsCa9ubT4ggRG6W1zejXqazIO2nQpKdGHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1956d75e.mp4?token=D2LB-pwgFwLPe29cyMTdtwmrSRQy9nhrxWymHcKEUVbWd8DBjM4UOYX2BMwYunxWVNiuHR2xuquxbspKi6KsDbLLpN6-T3NVad4abxd6pEVLELU4sN8D1whUjm36hIJNDgg0tZHXAas_YkK14upwKVfSs9St-utqParggxmFvoSaCDuQjmE9VbSJv4iOigx949UPKQkjb-Cf4U4WFAnxQknNNJEh5Fsjmxw54hzEWAU9tMKyCCGnUcoVWj1FgjTumJfpjKi1m9SoSVF_rFMHJOdEDI_g5Mxt-2Qu2C1duZWaRP1VaVgsMsCa9ubT4ggRG6W1zejXqazIO2nQpKdGHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات رژیم صهیونیستی به چادرهای آوارگان در منطقۀ المواصی در جنوب نوار غزه، دو شهید و ۲۰ زخمی برجای گذاشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/farsna/445544" target="_blank">📅 01:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445543">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfde88a6d1.mp4?token=K4T9tP0jl9xIM_B5otcfaqragJAfkyZ7YrIpVioyi6ojAhHuyHObfm-A2q9m_5byU1t0JJazFfFOGWSO2C_RaGVLO8zSiln1H56RHAWpBXaQ9zfYVAxTlu3Ca1sdjDCnY0OvHB5ZdJ6E6S667gJszSVXoydjMQ-g6N3ZWwitpgTgBWF0CyIgRzLrj6meNakXiPWCh-LwmhmcHc-mkfL5jPrmJYv77QEQ3T742jZOzgYOfSRJtMuKUWJd88WNGT7hGktWaOqSoCnAZoYfRag3AzJgq_GURixWr2EvP8_5K2XSx1M2tghYlA7fyUjxS9GxJQoxmDAp6in0ZEMCH2xktA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfde88a6d1.mp4?token=K4T9tP0jl9xIM_B5otcfaqragJAfkyZ7YrIpVioyi6ojAhHuyHObfm-A2q9m_5byU1t0JJazFfFOGWSO2C_RaGVLO8zSiln1H56RHAWpBXaQ9zfYVAxTlu3Ca1sdjDCnY0OvHB5ZdJ6E6S667gJszSVXoydjMQ-g6N3ZWwitpgTgBWF0CyIgRzLrj6meNakXiPWCh-LwmhmcHc-mkfL5jPrmJYv77QEQ3T742jZOzgYOfSRJtMuKUWJd88WNGT7hGktWaOqSoCnAZoYfRag3AzJgq_GURixWr2EvP8_5K2XSx1M2tghYlA7fyUjxS9GxJQoxmDAp6in0ZEMCH2xktA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرح جایگاه وداع با رهبر شهید انقلاب منتشر شد
🔹
سردار حسن‌زاده: طراحی جایگاه وداع با پیکرهای مطهر امام شهید و خانواده شهید ایشان بر مبنای چند محور صورت گرفته است.
🔹
از لحاظ ارتفاع، جهت و استقرار در حیاط اصلی مصلای تهران، از همه‌ نقاط صحن، رواق‌ها، پشت‌بام شبستان…</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/445543" target="_blank">📅 01:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445542">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۵</div>
</div>
<a href="https://t.me/farsna/445542" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۴ – کتاب آه</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/445542" target="_blank">📅 01:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445540">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجار یک بسته در موناکو
🔹
در پی انفجار یک بسته در مقابل ساختمانی در موناکو، سه نفر مصدوم شدند. به گفتۀ برخی منابع خبری، مصدومان تبعۀ اوکراین هستند.
🔹
بنابه اعلام مقامات محلی، انفجار پس از آن رخ داد که فردی کیسه‌ای را روی زمین گذاشت و سریعاً محل را ترک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/445540" target="_blank">📅 01:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445539">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uH5JxljXYLhRPlyuGCaqQQey6CALgZnP1onxS96sfU9JGNDsVXJroMcBcMvdXVOaChSY4hoBIXPuZb_N_OB0HnpQBxnmPl-gIYx_sfb6IAzzlbV9gjWwOG1bsNwhfgpgMrnyInD7ozKADkc_FNVMOQuVikkPBqiKLFOtQbYmOUzKj9eIf8UBmcC0R5bnhqj3eV8duXcrdJZzJuYK7aJ9ckeepHyr47ZVBNsnoAN61etyC0aoQCc6jWIuvpfrSBihGVhDTUNrVEYZ4ofYNZJorkBLYDrq3OhhHBEv7i9lRJCmNCBIlYVwyJUjgX2psvKB78t5Llduztqn-g0FATBQxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریشه‌کنی درخت آزار و خودخواهی
🔹
در مدینه مردی از انصار به نام «انصاری» خانه‌ای داشت که در گوشه حیاط آن، یک درخت خرمای متعلق به مردی دیگر به نام «سمرة بن جندب» قرار داشت.
🔹
سمرة طبق قانون حق داشت برای سرکشی و برداشت محصول درختش وارد خانه انصاری شود. اما مشکل اینجا بود که او هر زمان که می‌خواست، بدون در زدن، بی‌خبر و ناگهانی وارد حیاط خانه انصاری می‌شد؛ جایی که همسر و فرزندان مرد انصاری در آنجا آسایش نداشتند.
🔹
انصاری بارها به او التماس کرد: «سمره، وقتی می‌خواهی وارد شوی، حداقل یا الله بگو، در بزن کن تا اهل خانه باخبر شوند.» اما سمره با لجاجت می‌گفت: «این درخت مال من است و حق دارم هر وقت بخواهم سر بزنم و اجازه نمی‌گیرم!»
🔹
مرد انصاری به پیامبر اسلام(ص) شکایت کرد. پیامبر(ص) سمره را احضار کردند و به او فرمودند: «همسایه‌ات از تو شاکی است. از این به بعد وقتی می‌خواهی وارد شوی، اجازه بگیر و اهل خانه را باخبر کن.»
🔹
سمره قبول نکرد و لجاجت به خرج داد. پیامبر(ص) فرمودند: « این درخت را به من بفروش.» سمره بازهم قبول نکرد. پیامبر قیمت را بالا بردند و حتی وعده دادند: «این درخت را واگذار کن و در عوض، من ضامن می‌شوم که خدا در بهشت به تو درختی بدهد.» سمره بازهم با لجاجت گفت: «نه درخت دیگر می‌خواهم و نه درخت بهشت را؛ فقط همین درخت خودم را می‌خواهم!»
🔹
در این هنگام رسول خدا(ص) که دیدند او از حق مالکیت خود به عنوان ابزاری برای ظلم و آزار یک خانواده استفاده می‌کند، رو به مرد انصاری کردند و فرمودند: «برو آن درخت خرما را از ریشه بکن و جلوی پایش بینداز»
🔹
بعد از اینکه درخت را جلوی پای سمره انداختند پیامبر به او فرمودند: «حالا برو درخت را هرجا که دلت می‌خواهد بکار.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/445539" target="_blank">📅 00:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445538">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0841fac41.mp4?token=DRChtGcEuTHYJ61rCRIB8TRnKjxprU0U-lnpfIZHv_Cz0CEFQNrkes7CDTBnRL8x9e2yFIT6cvfBy5aoqp83S0ugzwIMpD1srBJ3wjk2a-bNhEkGx584hz1YoYcAyaBzXkhApSxdkMbmWE5hAv7D-hr0GuOHh1wW-Oao3vCh0ac57igWaa56v8_E08E8hBvKlNOcKFqu2svKQbiXSuv1bJPkWQ7D2tf-UqV44adzHUeF_1gQFlvc_PglpLeU2vjL4FbP5_LlvvOG77eiUQVyZ6KO28rI_7JchwtaieowrXuNvuC-pOHveIVfnBryquKrMHRMs6zX7zJCwFG0QYXHIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0841fac41.mp4?token=DRChtGcEuTHYJ61rCRIB8TRnKjxprU0U-lnpfIZHv_Cz0CEFQNrkes7CDTBnRL8x9e2yFIT6cvfBy5aoqp83S0ugzwIMpD1srBJ3wjk2a-bNhEkGx584hz1YoYcAyaBzXkhApSxdkMbmWE5hAv7D-hr0GuOHh1wW-Oao3vCh0ac57igWaa56v8_E08E8hBvKlNOcKFqu2svKQbiXSuv1bJPkWQ7D2tf-UqV44adzHUeF_1gQFlvc_PglpLeU2vjL4FbP5_LlvvOG77eiUQVyZ6KO28rI_7JchwtaieowrXuNvuC-pOHveIVfnBryquKrMHRMs6zX7zJCwFG0QYXHIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: در طول هفته جاری هیچ برنامه‌ای برای مذاکره با آمریکا نداریم
🔹
حضور مقامات آمریکایی در دوحه ارتباطی با حضور هیئت‌های کارشناسی ایرانی در دوحه ندارد.
🔹
کارشناسان ما برای پیگیری تعهدات آمریکا از سوی قطر به دوحه خواهند رفت.
🔹
هیچ نشست و برنامه‌ای…</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/445538" target="_blank">📅 00:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445537">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bedeb4c3.mp4?token=OogosuUwJJyeYJ4yKoZMSloH8HDLdwiJA7sr5VV7KX5vyOZ-uhDNbrkraA4gIAD31zffONR-j52lGhpXmNHeMd9MulC7zmVjQ6WlWFwYXRhgmF-d4iCZ7slpFFtae_OligK-DlXgg-s1UF_ZjryGA-5CwX-z7dY3xYgg2AedAXAee3sW0F4YCJEsqEtnx_UN2sqo-Fe7dVJQC7Mxu92HKLjeg1N2RaiUqvipAJsa4HnluUDQOfdy2wpmcskS-J9nr9x9J2YkNj6BurMu2Q6qYWz5EqFo77OUdmn8Q_wObfAZbW6ZRONTjDxpfBhgd77L3vkrNCF-MdRq7PSQt7wjQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bedeb4c3.mp4?token=OogosuUwJJyeYJ4yKoZMSloH8HDLdwiJA7sr5VV7KX5vyOZ-uhDNbrkraA4gIAD31zffONR-j52lGhpXmNHeMd9MulC7zmVjQ6WlWFwYXRhgmF-d4iCZ7slpFFtae_OligK-DlXgg-s1UF_ZjryGA-5CwX-z7dY3xYgg2AedAXAee3sW0F4YCJEsqEtnx_UN2sqo-Fe7dVJQC7Mxu92HKLjeg1N2RaiUqvipAJsa4HnluUDQOfdy2wpmcskS-J9nr9x9J2YkNj6BurMu2Q6qYWz5EqFo77OUdmn8Q_wObfAZbW6ZRONTjDxpfBhgd77L3vkrNCF-MdRq7PSQt7wjQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: اگر با عمان در مورد مسیر و ترتیبات تنگهٔ هرمز به تفاهم نرسیم، در هر صورت حاکمیت و سیاست جدید ایران را در تنگهٔ هرمز اعمال خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/445537" target="_blank">📅 00:15 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445536">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f482687e8a.mp4?token=gy7bS7GIKfCa2117SPyaxevTTabQ3SWd14ufjDLyS2oanv6TADHL_PROIStwey9mfUCPxbkWpCtkDmZeoQTFeJeNtmHwALRfnVO5ZP6mddTLKCsRbzY2sLbO2xELJ1c3kELY_4tcVUznp3ZEa1rHsKm1vMF2XcKWDk2JkR9nU9WJghBJq26b6MoftGE8vR_QKybC9Q1viJhxB6IPy3dRhsUF49z1BiXIhkbFXHhJiGm-CD335gXw6UzpZlIt2uqp47Yi7yYTXGYisxRKVJVTAJEN48VfDP08BKbA7gXt29m2SRlLR55q32i6zBqQQzTPKE30b-GDibgNAkpS-y89ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f482687e8a.mp4?token=gy7bS7GIKfCa2117SPyaxevTTabQ3SWd14ufjDLyS2oanv6TADHL_PROIStwey9mfUCPxbkWpCtkDmZeoQTFeJeNtmHwALRfnVO5ZP6mddTLKCsRbzY2sLbO2xELJ1c3kELY_4tcVUznp3ZEa1rHsKm1vMF2XcKWDk2JkR9nU9WJghBJq26b6MoftGE8vR_QKybC9Q1viJhxB6IPy3dRhsUF49z1BiXIhkbFXHhJiGm-CD335gXw6UzpZlIt2uqp47Yi7yYTXGYisxRKVJVTAJEN48VfDP08BKbA7gXt29m2SRlLR55q32i6zBqQQzTPKE30b-GDibgNAkpS-y89ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادعادل: رهبر انقلاب دائم مردم را به حفظ وحدت دعوت می‌کنند؛ از «علی‌الاصول» برداشت غلط نکنیم
🔹
بیانیهٔ رهبر انقلاب باید همه‌جانبه خوانده و تفسیر شود.
@Farsna</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/445536" target="_blank">📅 00:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445535">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c425e5a737.mp4?token=D1ITrrh6STRtTtFVTnehnn9HG8e5pHnfIIyaJdZPjg-jnDT7WM0WTpd4NiaLggjPLXeVdC5GURR8lY7EQj7InFTSfY-wsj1y87M-xGuWiUKnuvuKLFMNL0YSsk6_lWIuhMC5w_Z22WTYiTnHQTEFHSlmLaClo2bux3qjl_fR5gsxNrhDyLrG1pbDnJE1iIlrFhwBDqUxzI1-JLa1grd8oTgE1s1x02JWtpSmiCCs1z6U3y9YuH65hJjMabSdFjv3bPBKyDMi1VEX0io0HFvQXSTQAZ5hZrJbkpC09kEm4jdIV94AXG4aeI6s9AYZTkUulg6W_dO_kcd1wzrmH39-Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c425e5a737.mp4?token=D1ITrrh6STRtTtFVTnehnn9HG8e5pHnfIIyaJdZPjg-jnDT7WM0WTpd4NiaLggjPLXeVdC5GURR8lY7EQj7InFTSfY-wsj1y87M-xGuWiUKnuvuKLFMNL0YSsk6_lWIuhMC5w_Z22WTYiTnHQTEFHSlmLaClo2bux3qjl_fR5gsxNrhDyLrG1pbDnJE1iIlrFhwBDqUxzI1-JLa1grd8oTgE1s1x02JWtpSmiCCs1z6U3y9YuH65hJjMabSdFjv3bPBKyDMi1VEX0io0HFvQXSTQAZ5hZrJbkpC09kEm4jdIV94AXG4aeI6s9AYZTkUulg6W_dO_kcd1wzrmH39-Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: ما ایمنی و امنیت کشتی‌های عبوری از مسیرهای موازی در تنگهٔ هرمز را تضمین نمی‌کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/445535" target="_blank">📅 00:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445534">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3aad4ef7.mp4?token=VdFkGrOMC317xiJxEgriaFAqROJfJ3bQy20ZTix3UD20YcB0TTeDbjREZhpDSJzfXhWec8S85QkspNQkysHKIeFMlX4zAFqCPFgIrB4mHnd7kXnMxbvuIC1E3ZMvu_NaFQggbZz-J4Nz-Jw7UXpvYwrKTz4dinad7AYL4ikW3Bk9NBzuV-glOE338sICZxoSajTCHqo_RCDYCUM2N2n0QYNaiQliP8aK_m8aXDbus6PK7B1VmpPffI5Vcc2BrDTbXxR3cn54qd-mTCbrzi9vw2qxlfX-bN55-Nsos3n3XBOp92yLAuK1Dbmv1IQ4d2jf7nhsGFIAapUHFqrmmEGzWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3aad4ef7.mp4?token=VdFkGrOMC317xiJxEgriaFAqROJfJ3bQy20ZTix3UD20YcB0TTeDbjREZhpDSJzfXhWec8S85QkspNQkysHKIeFMlX4zAFqCPFgIrB4mHnd7kXnMxbvuIC1E3ZMvu_NaFQggbZz-J4Nz-Jw7UXpvYwrKTz4dinad7AYL4ikW3Bk9NBzuV-glOE338sICZxoSajTCHqo_RCDYCUM2N2n0QYNaiQliP8aK_m8aXDbus6PK7B1VmpPffI5Vcc2BrDTbXxR3cn54qd-mTCbrzi9vw2qxlfX-bN55-Nsos3n3XBOp92yLAuK1Dbmv1IQ4d2jf7nhsGFIAapUHFqrmmEGzWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر خارجه: ما ایمنی و امنیت کشتی‌های عبوری از مسیرهای موازی در تنگهٔ هرمز را تضمین نمی‌کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/445534" target="_blank">📅 23:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445533">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uImYkW63G6j-EcHxi6wcob23hC_f_2lwtVKhMkXAfmDzvYfxqUV9l53ioIuHdl8GfKhQ4--c8wdWloq3DnamJ76aoc7fmFeoZM7ruVd64ZcWbz-c9jPNf-Lm0Q-LnC67AEkTtYt2saEQueTUaAr9lbXmT7I5EZClM-5CRdTtg6Ohk1y6Q1ATERWneCRL2RDpw_LM2j18E4qHpn67YDhExpmak-NaTHaP8ubxjHFtpeCH0uX6hj2Yg6-PB1oWS9L6tYOH5GCwuNXgri66rHXL7XGxRnv9yWy75crCLViIAcO7r8sReXsS0K4PbVF5haOh2vHopWnjvNV5o9YpI-jYvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: اگر طرف آمریکایی به تفاهم‌نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم
🔹
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/445533" target="_blank">📅 23:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445532">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a156660ccb.mp4?token=RlLm1VUVFLRP14CEMGgzzzvbax4rGH9K0i2qrYZg7qqN7j9zex3e2Wmg3a1TMCS3gqKMEQm5MAlzn0F4t3w4y49I9pNAwVI1Khy686ccBeVxvibOOOwSlY0Jn7FI1Bjk3_Y45F0s6DRqJvxCpvvlKwDBv_6a7bMg0pfGeaPoMD0eJcdEg7367w6KYJDvGxg1STUD8MwLE1Tw_6jYl8Q_lMPQvgDrI6q7ehgMcNuxJbQ2K36SQyFGTtErYSqCltvy3cwgdXVyqw8mS4pEBP6gqpHdwmSf70c84qxfvHdqkUOM74rGXZ8gbpUJA2XhFf5NTcFBpmjdGPjgYAaxbzfvQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a156660ccb.mp4?token=RlLm1VUVFLRP14CEMGgzzzvbax4rGH9K0i2qrYZg7qqN7j9zex3e2Wmg3a1TMCS3gqKMEQm5MAlzn0F4t3w4y49I9pNAwVI1Khy686ccBeVxvibOOOwSlY0Jn7FI1Bjk3_Y45F0s6DRqJvxCpvvlKwDBv_6a7bMg0pfGeaPoMD0eJcdEg7367w6KYJDvGxg1STUD8MwLE1Tw_6jYl8Q_lMPQvgDrI6q7ehgMcNuxJbQ2K36SQyFGTtErYSqCltvy3cwgdXVyqw8mS4pEBP6gqpHdwmSf70c84qxfvHdqkUOM74rGXZ8gbpUJA2XhFf5NTcFBpmjdGPjgYAaxbzfvQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۱۲۱ شب ایستادگی هرمزی‌ها در تنگه هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/445532" target="_blank">📅 23:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445529">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrJz9knxI5LqF8R3RegdCLkrHTtk-3AVaSwP6NEoY8kzgTYLscvNAWIm2N4BR_DSLvVpHgLezg6WMqVco6T9Ej03m2nJoOV4dZnjnWICxfKbmexBQ7Zu0DZnfQJ6jOVFSoAoNueXo3Uc0PvGF1rrPCpJ8mRBrEw_U2tqZyIzIxMEBtGsEdq2IjJJKpAxtOvcgWeb5OfvCU0tpEACU34ydBKIevGWGnKT-2dzXskiQkG5CtCtfZ9TUIRx7uq8QdbHo1FkyxW_PWjIfcwBpWctVv72BQY4IpML2iEI3ETPTwaPqCaeqM2HBqXBN628i7TU0i-jBH_CVOCUL7DYfIQ34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عذرخواهی بازیکنان ژاپن از هوادارانشان پس از باخت
@Sportfars</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/445529" target="_blank">📅 23:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445528">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b43b289a4f.mp4?token=KKEHMEVlcR6yV74MFwfQR5RekFQFUKZ_4UfFYwDMwFgdFBxS5JnO3VOnZII6IVx8UrvgPEbv8oLIVMni-sJKVGHmT0cfTkkzCbSdLfh_5L53KAqNzDPQ6E6cu_4iPAZpqvRmAL5_Om0V9SZf_qrLy12AxRGIXqIpgTrHvV28q2HUR8nTIqydzPbb7qNxied2CiPeZYhegNfMMAJUDROP3ysCOPbGaTK13Upu0bI6ckDjuZIWAQN1muxuaKilEx70-zW_SnbPpwcqsEnqM8ZgaSWQ09HNP4Gcu2e3snSOmAo47gAlhx97nGvzfmDhkq0p_Tasry-94yKDiQOLuEdi5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b43b289a4f.mp4?token=KKEHMEVlcR6yV74MFwfQR5RekFQFUKZ_4UfFYwDMwFgdFBxS5JnO3VOnZII6IVx8UrvgPEbv8oLIVMni-sJKVGHmT0cfTkkzCbSdLfh_5L53KAqNzDPQ6E6cu_4iPAZpqvRmAL5_Om0V9SZf_qrLy12AxRGIXqIpgTrHvV28q2HUR8nTIqydzPbb7qNxied2CiPeZYhegNfMMAJUDROP3ysCOPbGaTK13Upu0bI6ckDjuZIWAQN1muxuaKilEx70-zW_SnbPpwcqsEnqM8ZgaSWQ09HNP4Gcu2e3snSOmAo47gAlhx97nGvzfmDhkq0p_Tasry-94yKDiQOLuEdi5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قرار شبانه نیشابوری‌ها به عدد ۱۲۱ رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/445528" target="_blank">📅 23:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445527">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzOBXu9Zp1ozTGE7ppiWL6F0xhaKCaXBQpK31OTCSr8C15ulO3LO-fAZCo5bJO-0YU-bLWM_-XHdz-ht2P8p-Z-poPzYBpaobfDZO2NEEXKSw_oFBFkwXaEryRc4Y5yIhU5E9U_uo3z0Ir_m-yYkl8lVPdOy9elMUsew0VpeATAcBb9JHiTngRuG3EK09xyLAuWV9j3qah9I29iFxmOxpEYB2affQFoH3zdqNoRVyCeBwIe7aTdsctF-wRA8HCL79c7ADrgU9qHJR_cbWRltdYI-JE-SBlJdEru9hEO6hPFw0i81VU0nqxMUWTatzsW_nn_S2DwoWunKhOslydYM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا توکلی شایعه وخامت حالش را تکذیب کرد؛ صحیح و سالمم
🔹
رضا توکلی، بازیگر تلویزیون در گفتگو با فارس: من حالم خیلی خوب است و شایعات مطرح‌شده درباره بیماری‌ام را تکذیب می‌کنم. متاسفانه دوستان در درک ماجرا دچار اشتباه شده بودند.
🔹
مریض دیگری داشتم که با شرایط دشواری رو‌به‌رو بود و باید تحت درمان قرار می‌گرفت، به همین خاطر برای پیگیری روند درمان او به خارج از کشور سفر کردم. بحمدالله با لطف خدا و دعای مردم، حال مریض‌مان بهبود یافته است.
🔹
این هنرمند در پایان از پیگیری و تماس‌های متعدد دوستان، همکاران و همه کسانی که نگران سلامتی‌اش شده بودند، تشکر کرد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445527" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445526">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حمله تروریستی به یک خانواده در سیستان‌وبلوچستان
🔹
ساعتی قبل یک خودروی شخصی حامل اعضای یک خانواده که درحال تردد در شهرستان سراوان بودند هدف تیراندازی افراد مسلح مزدور دشمن قرار گرفت.
🔹
در این حادثه راننده به شهادت رسید و همسر و فرزند ۳ ساله او نیز بر اثر اصابت گلوله مجروح و به بیمارستان منتقل شدند.
📝
نیروهای انتظامی و امنیتی در تلاش برای شناسایی و دستگیری عوامل این حمله تروریستی هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445526" target="_blank">📅 23:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445525">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b364cfef50.mp4?token=FCKUI53k_fKUJtawp8XTBSh5Tn5nWUFBwGH9NAqO05ezVzyio6yOwsBl-0FLkPkmJ9cB8lb9KE8IztKSJKeZEhevpzAyOPL0XSQtBU45MomvQ1bW8aIC4gcXmGen43QXjIbkw8homaiG7tmpP6Z4yIK2DLZkSWv1N9t7LezIvE5jda2T7WcenSSlMGeWQWAEH63S4J3SkL0uWJQ9wHWODv6s11oFdEJDCY0qT7b7Jv5_Q6SAJvsoQ0E-yBcu4_71y729lGDwDYh8ZDZ2AhWcU8-rGyTITcR5kg2ltI8aqmqcBWXCLfdAwILEDc87vWPjLYAf3LvkFdXxJGEDwfReoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b364cfef50.mp4?token=FCKUI53k_fKUJtawp8XTBSh5Tn5nWUFBwGH9NAqO05ezVzyio6yOwsBl-0FLkPkmJ9cB8lb9KE8IztKSJKeZEhevpzAyOPL0XSQtBU45MomvQ1bW8aIC4gcXmGen43QXjIbkw8homaiG7tmpP6Z4yIK2DLZkSWv1N9t7LezIvE5jda2T7WcenSSlMGeWQWAEH63S4J3SkL0uWJQ9wHWODv6s11oFdEJDCY0qT7b7Jv5_Q6SAJvsoQ0E-yBcu4_71y729lGDwDYh8ZDZ2AhWcU8-rGyTITcR5kg2ltI8aqmqcBWXCLfdAwILEDc87vWPjLYAf3LvkFdXxJGEDwfReoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فوتبالیست‌هایی که در آمریکا آواره شدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445525" target="_blank">📅 23:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445524">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fe93f5b28.mp4?token=pb1BzKKBI7ZlkkkNYIXR712BRzsrTuwjQbWJJLIlnGT2PUkchzYxqcfNoloxOAPYRg0wkzKZ5tc0mn2CdBzv94g9bTyA65F816yL787lg-ppPHauHzeOetQUTaj96Z5N1yUxo0pCS8TPrKOUZiQIq6OaJDFWfzvivS2MTrDdje_6XvW0w9YjSf6pIas4z12hIXfAlgINqgF8x9V897T2cJaP8Ob4vfv-5jQ9MUQlTy36t8AQiWamC_gkDBYlrPxtMqxwY1njiQPTFLhjPsQrcPtMOkiVVkvHZ6kZxuE8MxXYy9nPjcudV96d1c9EkirxWJ2oXY3gHCxKizIpHr4T2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fe93f5b28.mp4?token=pb1BzKKBI7ZlkkkNYIXR712BRzsrTuwjQbWJJLIlnGT2PUkchzYxqcfNoloxOAPYRg0wkzKZ5tc0mn2CdBzv94g9bTyA65F816yL787lg-ppPHauHzeOetQUTaj96Z5N1yUxo0pCS8TPrKOUZiQIq6OaJDFWfzvivS2MTrDdje_6XvW0w9YjSf6pIas4z12hIXfAlgINqgF8x9V897T2cJaP8Ob4vfv-5jQ9MUQlTy36t8AQiWamC_gkDBYlrPxtMqxwY1njiQPTFLhjPsQrcPtMOkiVVkvHZ6kZxuE8MxXYy9nPjcudV96d1c9EkirxWJ2oXY3gHCxKizIpHr4T2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرح جایگاه وداع با رهبر شهید انقلاب منتشر شد
🔹
سردار حسن‌زاده: طراحی جایگاه وداع با پیکرهای مطهر امام شهید و خانواده شهید ایشان بر مبنای چند محور صورت گرفته است.
🔹
از لحاظ ارتفاع، جهت و استقرار در حیاط اصلی مصلای تهران، از همه‌ نقاط صحن، رواق‌ها، پشت‌بام شبستان…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/445524" target="_blank">📅 23:12 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445523">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4911f76bd8.mp4?token=vESmycQ_QkO7nTtjvCUCKhWJlavllLF3-M4otLzC-2uCIpcGTHhoI90-CBEdPfUV6p_iGws9_crxrv7fQJdRsIgjxWX9jhuOGjunoYWpVopXAsg0-5AZGYhkg_j_Bh8NJjWU7pTRvPSDesvzUmrUCtudL0cTEchg5WlxMEiYoQgOTCG640kdmC9L2UyOSY9zSEJGPIBnhqaIDSQzNZgmOT_AY-yFJyOKjMLZ6UOZ24spsLRYvKYRCeRT8ncqdoM2t4e-10OflqYp1yyatMGj_vvWbZ0N4mfxkP0_eVnTn-6j7qKWKaEJ4kZH75-k39yZk-rDiA7hdU10d-NJ0dIaPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4911f76bd8.mp4?token=vESmycQ_QkO7nTtjvCUCKhWJlavllLF3-M4otLzC-2uCIpcGTHhoI90-CBEdPfUV6p_iGws9_crxrv7fQJdRsIgjxWX9jhuOGjunoYWpVopXAsg0-5AZGYhkg_j_Bh8NJjWU7pTRvPSDesvzUmrUCtudL0cTEchg5WlxMEiYoQgOTCG640kdmC9L2UyOSY9zSEJGPIBnhqaIDSQzNZgmOT_AY-yFJyOKjMLZ6UOZ24spsLRYvKYRCeRT8ncqdoM2t4e-10OflqYp1yyatMGj_vvWbZ0N4mfxkP0_eVnTn-6j7qKWKaEJ4kZH75-k39yZk-rDiA7hdU10d-NJ0dIaPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: در مراسم وداع با رهبر شهید انقلاب، امکان ورود کیف یا کوله‌پشتی یا وسایل حجیم به داخل مصلای تهران وجود ندارد.  @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445523" target="_blank">📅 23:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445522">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kf0QXBR2iZ88Ob5MZJ74yK0USwv44Buh85Be1FrW_duZN9QxIitCYElu57HQU6HdIAAarMf3eWZxkb0kjHG1O6MYB_uydRmjZu2rF1Q2S5qe_wGKFmH-N4kKyqgDJnmMeq0n2vd-0yXrJvOKtkXAz-gVDivZf5LXAn7kVBD-0fro3osehvZkHk4q7OwwY5EVvl-81QNU-F3L8rfj43MgXsm9KGYLUHr2fI_6dw7uHfjZ_Pn_yIkYk718dg68VW-JbMujh0MjAO3NEsHfch490p2GpgghTNAVecxEgyh7GSmxX4rkl8f3pMYxifJLVSlz7tB3cqBoGftAdSRr4Hmf-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور سابق امنیت ملی آمریکا: کشورهای منطقه دنبال توافق اختصاصی با ایران بر سر تنگهٔ هرمز هستند
🔹
جیک سالیوان در پاسخ به این پرسش که آیا کشورهای منطقه ممکن است دنبال ایجاد چارچوب امنیتی بدون مشارکت آمریکا باشند، گفت: «فکر می‌کنم به‌سرعت درحال نزدیک‌شدن به این…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445522" target="_blank">📅 22:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445521">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJfiTo0iO1NSZkOiQls_FbCn9YNiy49rEppSvZJvcQP5WaMhVm_xrDhbYMvTSoTlxTEcBobqIE-xXcMXFygCYx_OEvT315E7Eo3IxEEdLR1BVliwvEaSE24NtyK6UQgu-l0e1C0Yvw0vkYLtLP3qMiiqeUFWGLrvMsr7lZZiAoBSLhkQwemTqQ-npNZj6Ru1v3goZWXHl0WmXdf9iA9EpNVRSxdqoaymktxV_2EbXESsDIkpK_SAkdnbe_6iA8I-jhtcLbjGfBgAS4mKv53-C8MtgnB87wP-eRUX5dA3xM0VZAwBrHtJa4wX5JZpFJoMwgBrT_0J5yHEntpxYZRWgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح جایگاه وداع با رهبر شهید انقلاب منتشر شد
🔹
سردار حسن‌زاده: طراحی جایگاه وداع با پیکرهای مطهر امام شهید و خانواده شهید ایشان بر مبنای چند محور صورت گرفته است.
🔹
از لحاظ ارتفاع، جهت و استقرار در حیاط اصلی مصلای تهران، از همه‌ نقاط صحن، رواق‌ها، پشت‌بام شبستان اصلی مصلی و هر نقطه‌ای که زائران می‌ایستند، دید کامل به جایگاه وجود خواهد داشت.
🔹
همچنین سعی شده با الهام‌گرفتن از همان جایگاهی که امام شهید در دیدارهای مردمی حضور داشتند، همان فضا تداعی شود.
🔹
فرایند برگزاری و اقامهٔ نماز نیز در این طراحی دیده  شده است. در واقع، این طرح، طرح وداع و طرح شهادت خانوادگی امام شهید و خانواده‌شان است.
🔹
۸۰ درصد این طرح پیش رفته است و تا روز ۱۲ تیر به‌طور کامل اجرا خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445521" target="_blank">📅 22:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445520">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RY5heYlpfcYq0xOCm0_5Cso1X2-fNyn-pPOO9nn6fsQvI7E5gnWewu8H07VemNy8lfajtDZllMtEnZKktVzpVlajp80Hygxw4xMEpnH3gb7gxRwm9SJI3yRHHRaAGm9R6H-30bEzs1yncSGluEo51iOuIvgQTwiPNrCFcKGzxaYnkMsQxhQJD8gGhWOT-ac0J1kmmDmrPyDL2FXGON6lpotczyImLzoyYVJI1qe_qNTozyLIvwBwZ65fpGTpGqgMq0bfhqE32QEp_UHc_9t9o1MucuUctLImF5UAFvKaZodeO0MxO144JO_J-mgyWpJoIlQNjFwwbep_erjPMXcLBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
برزیل در دقیقۀ ۹۶ گل دوم را به ژاپن زد
⚽️
برزیل ۲ - ۱ ژاپن @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445520" target="_blank">📅 22:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445519">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c2e900f3.mp4?token=SdPcoLMGYpMpkc2qNdsz5fmS57sx5IzNZKdWMwsHHFwUwZm4RvZ23D2GF-7RfLewviUnpnX3DZPBbhd3TYz0Ed5Fud360tn63l3L6MQbcHlkCgyu67hxpWnIA8hwJSS1Xkx4WR27XoBfewD4a8k_w0y7kCdY9u7HGkXWGdrdAaPcBtlZFRSQc_9xQqoh67BaBywIh4oPgIdBgjYeXos5LcautVzL3gPe6Yt9igCl_S1Xo-CTEO5eVaKi7xBE_0KWIrOfpXGvg-1mtp3-B6vYVfs27cUD8U_mNcARyoc7_mpB1Pc-vCNfVPmfpbVJSgIMW4W7y66Grq8KAVcDJdNh3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c2e900f3.mp4?token=SdPcoLMGYpMpkc2qNdsz5fmS57sx5IzNZKdWMwsHHFwUwZm4RvZ23D2GF-7RfLewviUnpnX3DZPBbhd3TYz0Ed5Fud360tn63l3L6MQbcHlkCgyu67hxpWnIA8hwJSS1Xkx4WR27XoBfewD4a8k_w0y7kCdY9u7HGkXWGdrdAaPcBtlZFRSQc_9xQqoh67BaBywIh4oPgIdBgjYeXos5LcautVzL3gPe6Yt9igCl_S1Xo-CTEO5eVaKi7xBE_0KWIrOfpXGvg-1mtp3-B6vYVfs27cUD8U_mNcARyoc7_mpB1Pc-vCNfVPmfpbVJSgIMW4W7y66Grq8KAVcDJdNh3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
برزیل در دقیقهٔ ۵۶ گل‌ مساوی را به ژاپن زد
⚽️
ژاپن ۱ - ۱ برزیل @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445519" target="_blank">📅 22:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445518">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqCr1CP1neVu0dI3BL1cPVmmAjDbKMYFRAuCDI-K7h3i1jy_U1bdkrL44OvgL1Z8oCsIHNRvChDuLDRNIp7pjFO_jKKKe7EnxNOPsEOw1R2LfVGD4p-5T8lJIzeF4XiC3uV54hUFJZMpU7F-3JISBIr8Yi1GBvyAoQZc6XYRbL88qRlELbmV2hxULTp1aokbgnVMz0-_rxx1YGBDn4B-y5H-7HMRmLq7-NimDRSCKUFRHLnCbN5g2sZd7DDwIma4zm2NiA_cWgZQzkwkSciQIOdukKQj2vFFFgQJR7x40CI2FbZJfcTz3oBSTxgH5Zr4BXwKgauH36K-B5G_4qThQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاور سابق امنیت ملی آمریکا: کشورهای منطقه دنبال توافق اختصاصی با ایران بر سر تنگهٔ هرمز هستند
🔹
جیک سالیوان در پاسخ به این پرسش که آیا کشورهای منطقه ممکن است دنبال ایجاد چارچوب امنیتی بدون مشارکت آمریکا باشند، گفت: «فکر می‌کنم به‌سرعت درحال نزدیک‌شدن به این نقطه هستیم.»
🔹
او افزود: «انتظار دارم هر یک از این کشورها در سکوت تلاش کنند تا توافق اختصاصی خود را با ایران برای عبور امن کشتی‌هایشان و تضمین بازماندن پایدار تنگهٔ هرمز انجام دهند. حدس من این است که چنین گفت‌وگوهایی همین حالا نیز در جریان است.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445518" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445517">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppE0cf2FhCzLIGt6rU-xyUkeapMGIVG4mREYDS8pbAlCS6HI7nl5haQqXssDV92sVG8Uk68YqmSQP1aih_XgxN9eCdDZVNH5ss73DxowAEKmy9JqUqWI-UzmKmWrE86i-rVXQa3rCKZ2xFQZbgB0bGAqTfBBN_Tqwt0tkN7lHvTK3VPwqAH8o8VCTWteJTG3wHePfHTAohQzmmqtBzmh1HqlRCjog0v6_VwkeeS8UnwVbT4D_3wxTe4P5H2SMuwES6mkByKNNDuF8PEy7nxhiHhD6zv97hdyV0Q3W2_4RKZinNeCQLYUVjWhyJRCkT4ApwnWByMN2ZrM5rWrDnzdyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پرسپولیس به آسیا نرسید
🔹
پرسپولیس با باخت در اولین بازی تورنمنت ۳ جانبه، از کسب سهمیه آسیا بازماند.  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445517" target="_blank">📅 22:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445516">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409336ec31.mp4?token=uDm-ePQWUV7QVRIM_Wgf9UaD9obPH9u2ubgB38u5eusY0GfzJwy5nGxLyCdhvdMN_GrjOVK_FfQcJCGLgBRhUtXlurfCSOTsJafxwy8s9eko6OKmrF0ju_vdVVCyipGsHFDNWYDQSGOOgdCcu7X8gjsvGItsUB1myh05hZXhEb1R8ImbyxTsggopUXI57OU0zw0raHXoJBU-ZLTSQOx5C8e1zYlS4w1Z8mQVJekbUuybO4HBcDNg7xrTaOPePRS_mEdzTJz0bE_3Q0H_VubpjupZvnuziMxGs8p9oPsCXGAgrsn4ne2MP_AasANxQu4upuiWudboAr4BDvSGm-Yrfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409336ec31.mp4?token=uDm-ePQWUV7QVRIM_Wgf9UaD9obPH9u2ubgB38u5eusY0GfzJwy5nGxLyCdhvdMN_GrjOVK_FfQcJCGLgBRhUtXlurfCSOTsJafxwy8s9eko6OKmrF0ju_vdVVCyipGsHFDNWYDQSGOOgdCcu7X8gjsvGItsUB1myh05hZXhEb1R8ImbyxTsggopUXI57OU0zw0raHXoJBU-ZLTSQOx5C8e1zYlS4w1Z8mQVJekbUuybO4HBcDNg7xrTaOPePRS_mEdzTJz0bE_3Q0H_VubpjupZvnuziMxGs8p9oPsCXGAgrsn4ne2MP_AasANxQu4upuiWudboAr4BDvSGm-Yrfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: ما نمی‌توانیم در مراسم وداع با رهبر شهید توقف جمعیت داشته باشیم
🔹
برنامه‌ریزی این‌گونه است که مردم از یک نقطه وارد مصلی شوند و پیکر مطهر را ببیند و ظرف ۱۵ دقیقه از آن بخش خارج شوند. @Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/445516" target="_blank">📅 22:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445515">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwS_i56ugYGsFvv49YfbfKMSJE7iKPIrYNlxCtHF4kvwiEM_VdyhigGzLFAs0f38zjazf6RCL_OnEx2LgggF95NNBRJwgSwvk32I8nb_9aaeHGIhoiBizjdI2M00GZHr7vo-F3a0gP0mrFD6S1cxa6HyWKPLBZcCb3L15QljvNoLmvYT4RcScqMDQEsEZhhrhtnZi5Z9nS0x_HZ3td6jQ9rx-RZyIoc_x1nE56O_PDJj-FU1tZ75TID9IzXJvwnmfS9Yb_genq4Jk5p1gI50D-vBmTxWcIw-EWJiTTnLUswMcQoSrMtxk2HJvRZM34fF14N-mmA0FbATbhscPv_8wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤓
بعد از گل برزیل ژاپنی‌ها وسط زمین جلسه گذاشتند
@Sportfars</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/445515" target="_blank">📅 22:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445514">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376a0180e5.mp4?token=WX2oCc-glLejKNiZd1SEKhqt8vZt9H3voot1jWAzNtZy_wikdu1G4VTDf4SIVMGwer1hTbQPkUkMqTILKOVvqr0tQrr0XRCdHe7hzqxx82CBpuzpurGSqbbHDbkWYdpMMSvDFEBXqKOEfbpaBUgnzzz_CJbS0Rf_2IyszpFzzIJy8Az4GhuOlC0hFMmoVmaX_YuDi9CGwwNUKNjm0-ju6JKlUyrkYt_40bSQjOjeavjVzDqC18cZS_Z25sMKbx_Y_xtduEXUN2LYFcqZ6EPPDLCHgRV0qDiphgvzFU9RZNdK9qYMHbbqNfhlR0BzaTGDT3QsF1tKPbHYwbz34vXJYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376a0180e5.mp4?token=WX2oCc-glLejKNiZd1SEKhqt8vZt9H3voot1jWAzNtZy_wikdu1G4VTDf4SIVMGwer1hTbQPkUkMqTILKOVvqr0tQrr0XRCdHe7hzqxx82CBpuzpurGSqbbHDbkWYdpMMSvDFEBXqKOEfbpaBUgnzzz_CJbS0Rf_2IyszpFzzIJy8Az4GhuOlC0hFMmoVmaX_YuDi9CGwwNUKNjm0-ju6JKlUyrkYt_40bSQjOjeavjVzDqC18cZS_Z25sMKbx_Y_xtduEXUN2LYFcqZ6EPPDLCHgRV0qDiphgvzFU9RZNdK9qYMHbbqNfhlR0BzaTGDT3QsF1tKPbHYwbz34vXJYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ژاپن به برزیل توسط سانو در دقیقه ۲۹
⚽️
ژاپن ۱ - ۰ برزیل @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445514" target="_blank">📅 21:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445512">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
پسرم کارمند شرکت تجاری تو دبی بوده، از روز دوم فروردین تا امروز توسط امارات بدون هیچ توضیحی و جرمی بازداشت شده، نه اجازه ملاقات بهش میدن و نه ارتباط تلفنی و نه حتی اجازه گرفتن وکیلی تا الان حتی صدایی از مقامات دولتی هم در نیومده.
🔹
ما معلم‌های غیرانتفاعی اکثرمون کمتر از ۸ میلیون می‌گیریم. مدیر بیمه را از حقوقمان کم می‌کنه تابستان حقوق نداریم امنیت شغلی هم نداریم ولی مدارس میلیاردی درآمد دارن.
🔸
تو رو خدا روی این موضوع خاموشی چاه‌های  آب کشاورزی  کار کنین. ۶ ساعت خاموشی چاه در شب از ساعت ۱۸ الی ۲۴ و قطع برق در طول روز کشاورز رو به خاک سیاه می‌نشونه و بعد کشور رو وابسته به محصولات کشاورزی خارجی می‌کنه.
🔹
زمان جنگ اینترنت خانگی قطع بود و با توجه به این موضوع هزینه اینترنت روی قبض لحاظ شد و مخابرات گفت دستورالعملی برای این مورد نیامده. لطفا مسئولان پیگیری کنند.
🔸
من اوایل آبان ماه پارسال باید ساینا دوگانه تحویل می‌گرفتم، هنوز حتی فاکتور نشده!
🔹
بنده مستاجرم و برای وام ودیعه مسکن ثبت‌نام کردم ولی هر بانکی مراجعه می‌کنیم می‌گن برای وام ودیعه مسکن هنوز بخشنامه نیومده، آخه یه وام واسه یه مستاجر اون هم  با سود۲۳ درصد که این همه اذیت نمی‌خواد. اگه لطف کنید از طرق کانالتون پیگیری کنید صدای ما هم به جایی برسه.
🔸
تمام پیمانکاران علوم پزشکی بیش از ۴ ماه هیچ دریافتی ندارند و از ۱۴٠۵/٠۳/۱۹ هم دسترسی به تمام حساب‌ها بسته شده یعنی اگر امروز هم این وضعیت ادامه پیدا کنه در بخش پیمانکاری متاسفانه با مشکلات غیرقابل حل مواجه می‌شیم.
🔹
پیرو اختلال ایجاد شده در سامانه‌های خدماتی چند بانک کشور هر چند روز یک بار مدیریت محترم این بانک‌ها خبر از رفع اختلال تا چند ساعت آینده داده اما دریغ از رفع مشکل!
🔸
من یک مستمری بگیرم گفتن ۶۰ درصد افزایش حقوق دادن، در عوض حق عائله‌مندی و کمک معاش رو حذف کردن و کلٱ ۳ میلیون به حقوق اضافه شده که به بیست میلیون هم نمی‌رسد با وجود داشتن بچه دانشجو و محصل با این گرونی چکار کنم.
🔹
روستاهای اطراف ورامین بیش از دو هفته هست که آب ندارند و هیچ مرجعی پاسخگو نیست لطفا پیگیری کنید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445512" target="_blank">📅 21:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445511">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b58c6c32.mp4?token=WrOzXY-tlkrPo2b9yssMtXfaDKwxnTPUrY2GzW6RqcP2tKyUzFnaBtevchlP0x9-0MHoZat0Y5P-fh22ao10iMvMX0qdChwRwPl8xy_9nKSwyr7v6qHOU1Xk46sKjbGlbnz1ci7suh1MYCaBNApNQ1ArVmNiSctbNoElfrlWq2vNEX0-XAz9Qi6oud-dHI19KHXK_jaioGW-1OR-YQFdHM5wVIX_16xgfUJ69Nr8DloIHtBcBt1WCrE3oA8u2J2JLQfbr523mn6Lfup8XeVoTt7vIszNz04QQGZCvhTCRvWw3d-WfIGKTY8wt4q3hJi_02n_yjcm-UX32xVpxNI6FUHDyS5b8mXkwZGHjrEo80r-eSylhu9fH-Hoqw3q70BTOqXIeHeasCvachbH6pI2dAhDWP0xt7_2BA2-7qdi4OQFJukoD3uHN0gg7p39I68r7lDDm85MXPo8EArPR-yt6m9XiJZ_Hlqlf4GP4cafhD2ty4jCcOSNbx3Odb_5l6y_DrFXN9gvHmues2CnHLZERm2AyCsRI_g19ixVgrIX2P3Ru5bAPmgRM5Pru3sEvUOImVdhEdk9rDa4MS4HkN6xeKFVo3e_UowMOJnKi4GsDkFUd5W7fkVYhKP-Sn689kUnB25qck2y6CFCQVVYGXrtsjt-h-rtVNJONfw7XZpTXqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b58c6c32.mp4?token=WrOzXY-tlkrPo2b9yssMtXfaDKwxnTPUrY2GzW6RqcP2tKyUzFnaBtevchlP0x9-0MHoZat0Y5P-fh22ao10iMvMX0qdChwRwPl8xy_9nKSwyr7v6qHOU1Xk46sKjbGlbnz1ci7suh1MYCaBNApNQ1ArVmNiSctbNoElfrlWq2vNEX0-XAz9Qi6oud-dHI19KHXK_jaioGW-1OR-YQFdHM5wVIX_16xgfUJ69Nr8DloIHtBcBt1WCrE3oA8u2J2JLQfbr523mn6Lfup8XeVoTt7vIszNz04QQGZCvhTCRvWw3d-WfIGKTY8wt4q3hJi_02n_yjcm-UX32xVpxNI6FUHDyS5b8mXkwZGHjrEo80r-eSylhu9fH-Hoqw3q70BTOqXIeHeasCvachbH6pI2dAhDWP0xt7_2BA2-7qdi4OQFJukoD3uHN0gg7p39I68r7lDDm85MXPo8EArPR-yt6m9XiJZ_Hlqlf4GP4cafhD2ty4jCcOSNbx3Odb_5l6y_DrFXN9gvHmues2CnHLZERm2AyCsRI_g19ixVgrIX2P3Ru5bAPmgRM5Pru3sEvUOImVdhEdk9rDa4MS4HkN6xeKFVo3e_UowMOJnKi4GsDkFUd5W7fkVYhKP-Sn689kUnB25qck2y6CFCQVVYGXrtsjt-h-rtVNJONfw7XZpTXqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مخبر: دشمن تسلیم عقلانیت شهید لاریجانی شد
🔹
دستیار رهبر انقلاب: شیهد لاریجانی هر جا مسئولیت گرفت ترازی را به‌جا گذاشت که کسی نمی‌توانست به آن برسد.
🔸
همسر شهید لاریجانی: ایشان پس‌از شهادت رهبر انقلاب، به‌شدت دنبال شهید‌شدن بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/445511" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445510">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOpl_To22VESfXQze3Ar4jyDoSCN3rgq-kwyvoJbEMnuNfSk97OWvjZcMOE4w4CC4kuzbxIPl86IOH3O5B10UuYyIFfnGySZj5BuZba87F-TjrguWrS8Mve8E45EBxQzTlGvhXRYenU2I6H0yLNDbVezx-1MgAAWhA6BTMdAot98xFl5PQlTo8iF2KGay18a1v5r7_Qt7GGt0l4F_Dr1FzflMm9wn-ffU0taUUuwcmfr6SQDgEvx-N_LaoUY-uhcoDU60IMlIfRlsy2auoyNLxvHHILge5B00Jm32TT-QbKjHBNC6rNfyjHYk_biGxsU3C70vR3N6Y2UQkuOWhy-Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
همدان، میزبان پروژه‌های جدید توسعه شبکه ایرانسل شد
🔸
با حضور وزیر ارتباطات و فناوری‌اطلاعات، سایت 5G ایرانسل در شهر همدان و یک سایت ارتباطی روستایی در شهرستان بهار، به بهره‌برداری رسید.
🔸
این مراسم، ۸ تیرماه ۱۴۰۵، با حضور وزیر ارتباطات، نماینده ولی‌فقیه در همدان، استاندار همدان، رگولاتور ارتباطات، مدیرعامل زیرساخت، معاونان سیاست‌گذاری و استان‌های وزارت ارتباطات، مدیرکل فاوای همدان، نماینده همدان در مجلس، مدیران استانی و جمعی از مدیران ایرانسل، در قالب جلسه شورای اداری استان همدان، در محل استانداری برگزار شد.
🔸
پروژه‌های توسعه زیرساخت‌های ارتباطی ایرانسل در استان همدان، شامل افتتاح سایت 5G در شهر همدان و بهره‌برداری از یک سایت ارتباطی، برای پوشش روستاهای باباعلی و قشلاق همه‌کسی شهرستان بهار، به نمایندگی از سایر پروژه‌های ارتباطی ایرانسل در استان، به بهره‌برداری رسید.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/445510" target="_blank">📅 21:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445509">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSarmaye Bank | بانک سرمایه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UbJNaeOMmkcss8p4kkskvnqKKt3JKR7Mqks_uWAjE3QgILJ_ilfunLPHNjKOyAmOK3zPhC7Dj0tXefxbbNDOywRCNIfR6ttOxIIwwJ_QSzD9nyCA-eGoKo72kTCQdhtVI2tzG05kmm8TnA9vRryE_7En6GNG6V57RvV0lnftPslzn8zkjYOMLOjluDsX3osR7_bCF5dfAcyE3DeKJN0SiMJ1p5hg6_3NfeJFrdaLHS3IfUK2Zzep7GUWCrYOG0pd9BVn2HQNHzEAfORnKtZj0TNxmHm-7W48G-jza8fY3wpjaPL-FgnrHYISV_-2rj9NWWQeZIYt28sR0ki_zVPdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
😎
بانک سرمایه در مسیر بهبود؛ موتور درآمد سمایه روشن شد
⬆️
رشد قابل توجه درآمدهای عملیاتی
⬆️
بهبود شاخص‌های سودآوری عملیاتی
⬆️
جهش دارایی‌های بانک سرمایه
⬆️
تداوم اعتماد سپرده‌گذاران به بانک سرمایه
◀️
بررسی صورت‌های مالی ۱۲ ماهه بانک سرمایه برای سال مالی منتهی به ۲۹ اسفند ۱۴۰۴ نشان می‌دهد که این بانک در مسیر توسعه فعالیت‌های عملیاتی، افزایش حجم کسب‌وکار و بهبود برخی شاخص‌های کلیدی عملکرد قرار گرفته است.
🔗
متن کامل خبر را اینجا بخوانید...
#بانک_خوب_سرمایه_است
‌
🔽
بانک سرمایه را در شبکه های اجتماعی دنبال کنید:
📲
اینستاگرام
📱
تلگرام
👨‍💻
وبسایت
📲
بله
📲
ایتا
📲
روبیکا
💖
آپارات
📲
سروش</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/445509" target="_blank">📅 21:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445508">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/445508" target="_blank">📅 21:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445507">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53498f66b.mp4?token=cHRKoyNuO3GbPgz2GSNprOtIyJZXbqzqedfAAj3lthcBqHc23Nz1vjgVrnYrrRKuYydFhzvBtFasMF27l-A1uNqn6k2PCnyPXutNRkjLjCm4dFoFGEXrQa_Bx2hCV-3BB-eGme7k0TDujHMmG9TRoxTx0p5bDi8GMVbnHhQ5pap8CGhWCOMIqPKiIdLnYCBSxmsdWl6gML8_7amGYduBbXslKfxRswNc5ZOEVRdijEOQRe7Z9H7kxxElfy7abUrArnH_sXkdJpfHtb7G3iDMx4MENpWzrlTBgvR3zlRxrYNF-GfqsjflaDjrILI2eTVO0CpTBJ0gVtI1NyFGcdmr5a0eePDN0P7RjeRZLk-knZ99K--iSMINJEWbMnN3_ahJOJkOtWRdjMPfTJ0_Rhnolwrxtr3i5RK4IG67C0apCo7IIK0wYKYajIrJIQTsjjirs7-lYBse40pMWLaMVRj3u1fha6Ko4QsxTILECOn_80J9kgzbrUI5z2ZgUqItSbIfe3BaaIIr3gkCu88XNp9YV4IFmiL3EWLKMsjJhieGoho9XsX_X6gHlP_Tqpk4bAwBwbvQyRCabYFwhc9zWQD4xCzoFJobMEw7y1l8qH8OAmX0HWO7rTrRTXtN-G22kPdY2XkczqQWIBWa29K0Xw0zJpMobVqXsfkLVSPQ-YknXO4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53498f66b.mp4?token=cHRKoyNuO3GbPgz2GSNprOtIyJZXbqzqedfAAj3lthcBqHc23Nz1vjgVrnYrrRKuYydFhzvBtFasMF27l-A1uNqn6k2PCnyPXutNRkjLjCm4dFoFGEXrQa_Bx2hCV-3BB-eGme7k0TDujHMmG9TRoxTx0p5bDi8GMVbnHhQ5pap8CGhWCOMIqPKiIdLnYCBSxmsdWl6gML8_7amGYduBbXslKfxRswNc5ZOEVRdijEOQRe7Z9H7kxxElfy7abUrArnH_sXkdJpfHtb7G3iDMx4MENpWzrlTBgvR3zlRxrYNF-GfqsjflaDjrILI2eTVO0CpTBJ0gVtI1NyFGcdmr5a0eePDN0P7RjeRZLk-knZ99K--iSMINJEWbMnN3_ahJOJkOtWRdjMPfTJ0_Rhnolwrxtr3i5RK4IG67C0apCo7IIK0wYKYajIrJIQTsjjirs7-lYBse40pMWLaMVRj3u1fha6Ko4QsxTILECOn_80J9kgzbrUI5z2ZgUqItSbIfe3BaaIIr3gkCu88XNp9YV4IFmiL3EWLKMsjJhieGoho9XsX_X6gHlP_Tqpk4bAwBwbvQyRCabYFwhc9zWQD4xCzoFJobMEw7y1l8qH8OAmX0HWO7rTrRTXtN-G22kPdY2XkczqQWIBWa29K0Xw0zJpMobVqXsfkLVSPQ-YknXO4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳۷ سال هدایت ایران توسط رهبر شهید انقلاب از دید رسانه‌های خارجی
@Farsna</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/farsna/445507" target="_blank">📅 21:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445506">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMoSuwI8JAOL0UdKFnA3CocLSAy8IZt1G240xAWn82FT43GgFq1HWXhaUm8tsDzsPgAr7UpeXmQN8sgtQMm_Edyg2zPB_tl4G4xx6ChwAVXyoLFZX93AOJhp5gZ-cB3tRkmg4J7TX4aS1RQA983GeUE99cLv2WC0JRwO3vJsv6_IgYJypZGNzPTDAhxTbaDSTJznsq6GKfMnI3tQFFkmTBLsqawJTwRfOmWXDhGZtQ3rie0QMmrKOJ0hqhlgnYBRuw9GB9qNNHV2aKZ0Du3xZj6P2-Yxys7oNgZeWvMWvChKPe2sbpPsMQATyfIjmn25ZNhY_hsdRhf8QTQcyp0log.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقاد شدید عارف از بی‌توجهی بانک‌ها به امنیت سایبری
🔹
معاون اول رئیس‌جمهور: اتفاقی که برای بانک‌ها رخ داد را حتی نمی‌توان حمله سایبری نامید؛ یک دانشجوی جوان که فقط سه واحد رمز پاس کرده باشد هم می‌تواند چنین کاری انجام دهد.
🔹
بسیاری از کسانی که در شرکت ملی خدمات انفورماتیک یا بخش‌های دیگر فعالیت دارند، از دانشجویان من بوده‌اند و بارها به آنان هشدار داده بودم که ممکن است چنین اتفاقاتی رخ دهد، اما به این هشدارها توجه نشد.
🔹
توجه به امنیت سایبری برای دستگاه‌های دولتی دیگر یک توصیه نیست، بلکه یک دستور اکید و الزام است و مشکلات فعلی باید هرچه سریع‌تر برطرف شود.
🔹
برای بلندمدت باید راهبردهای جدی تدوین شود. متخصصان امنیت سایبری در کشور حضور دارند و با دانش و فناوری بومی توان مقابله با حملات ده‌ها برابر بدتر را داریم، من تخصصم این است و مسئولیت این ادعا را می‌پذیرم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445506" target="_blank">📅 21:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445505">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4adaa31060.mp4?token=gjFJo9FiWkvXABOs14838AtQk_zxcnymNLWhhwDaFvdVItsDjADC4XuZl1VN5lqxmDIYcyvJJJmnxqB_mX-VeVCasiEtJJo9gpLFAxjYsr6u6QlteFWx52DSCdXWnMFqTgobrKgRmHwnCECpTZJMrR3ly-1fmdrcK1E5iwPm87iZB7qITp7kbsrGixwLvABIBaZYc7CR7fJLOkc9ZYINE0Itry-g2B8_klog2lLlZFP27fD2pvviM_xkURcXldWr8BP_Mu08uWgsFZ7mZmUEbiGLcifAIY3-vIQNNDWA67jXqpuYn3YwEsmBZmpsE2v0J3rLZeKJ0x5JB7bt1gYNfl1J8_W3trVYLYmICVrZFOZNT0IRRfmGxs7hDBbUKQ4CBMAHMBjR4Kq9DT8KeVQOeuv_uq2H0s4hm7Zi_9lzLF-jaXlx2B28tSixHjQbnNSrv7B0_IMJJ2QNX1udoQs3T0PSZC62ZfXyJxGF9aLnSrTqRhrKJQBv7e5tcUZuUyW4VSFmMN6DnMSkk0Hz-txrGaVL5TdF7BnlzbASwN13gFmmzeizsXYb0tHOXoafFv9A77EoYvfU02SDhX_o8-BVqCIyPMTvhOoh8Q_HEINkqudqcRsNe7DalEQ5un12OA9Kiv9OM7YJF-hpkHJNfH8k-5boxj4hLbX1GAv_aM1emLY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4adaa31060.mp4?token=gjFJo9FiWkvXABOs14838AtQk_zxcnymNLWhhwDaFvdVItsDjADC4XuZl1VN5lqxmDIYcyvJJJmnxqB_mX-VeVCasiEtJJo9gpLFAxjYsr6u6QlteFWx52DSCdXWnMFqTgobrKgRmHwnCECpTZJMrR3ly-1fmdrcK1E5iwPm87iZB7qITp7kbsrGixwLvABIBaZYc7CR7fJLOkc9ZYINE0Itry-g2B8_klog2lLlZFP27fD2pvviM_xkURcXldWr8BP_Mu08uWgsFZ7mZmUEbiGLcifAIY3-vIQNNDWA67jXqpuYn3YwEsmBZmpsE2v0J3rLZeKJ0x5JB7bt1gYNfl1J8_W3trVYLYmICVrZFOZNT0IRRfmGxs7hDBbUKQ4CBMAHMBjR4Kq9DT8KeVQOeuv_uq2H0s4hm7Zi_9lzLF-jaXlx2B28tSixHjQbnNSrv7B0_IMJJ2QNX1udoQs3T0PSZC62ZfXyJxGF9aLnSrTqRhrKJQBv7e5tcUZuUyW4VSFmMN6DnMSkk0Hz-txrGaVL5TdF7BnlzbASwN13gFmmzeizsXYb0tHOXoafFv9A77EoYvfU02SDhX_o8-BVqCIyPMTvhOoh8Q_HEINkqudqcRsNe7DalEQ5un12OA9Kiv9OM7YJF-hpkHJNfH8k-5boxj4hLbX1GAv_aM1emLY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیام مردم به ملی‌پوشان فوتبال: ممنون که تمام توان خود را گذاشتید  @Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/445505" target="_blank">📅 21:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445504">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d7ddad6e2.mp4?token=hMOjdKTQhtNcMErUmELZg7LjMHkrLoIk39p_9mlra3uotAUPvL_XOCGJZf5oDD6EogikLai69cgZ6HwA6OpepjnNFtwfb7BbdqcgkRVcBjbtluL18OHxu7AR4c2PoZ9fgCz_TgEyGrpwqbQaNCOv_yTOS_K4ZYKyTgcBYLKOzzNx3aeeOW5FixfvnGyH97KhSjosQ5bV95k7ubI8v7YCbZcpZYXIv4AFYRadppNryE2tRQ4DucrGDfUwUq8nvmo9CgwIodUjz58XHceEsRL1vUebP1eFqagleHJbSu7DMzjGTo_AGENBvIjU273Kw3Colv5WhgWyVnrOCscc0yTsTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d7ddad6e2.mp4?token=hMOjdKTQhtNcMErUmELZg7LjMHkrLoIk39p_9mlra3uotAUPvL_XOCGJZf5oDD6EogikLai69cgZ6HwA6OpepjnNFtwfb7BbdqcgkRVcBjbtluL18OHxu7AR4c2PoZ9fgCz_TgEyGrpwqbQaNCOv_yTOS_K4ZYKyTgcBYLKOzzNx3aeeOW5FixfvnGyH97KhSjosQ5bV95k7ubI8v7YCbZcpZYXIv4AFYRadppNryE2tRQ4DucrGDfUwUq8nvmo9CgwIodUjz58XHceEsRL1vUebP1eFqagleHJbSu7DMzjGTo_AGENBvIjU273Kw3Colv5WhgWyVnrOCscc0yTsTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ژاپن به برزیل توسط سانو در دقیقه ۲۹
⚽️
ژاپن ۱ - ۰ برزیل
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445504" target="_blank">📅 21:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445503">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۸۱.pdf</div>
  <div class="tg-doc-extra">4.7 MB</div>
</div>
<a href="https://t.me/farsna/445503" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۸۰.pdf</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/445503" target="_blank">📅 21:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: هنوز وارد مرحلۀ مذاکره برای توافق نهایی نشده‌ایم
🔹
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آن‌هاست. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445501" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه:  اولویت کنونی ایران، حصول اطمینان نسبت به اجرای مفاد یادداشت تفاهم است
🔹
در رابطه با تعهد آمریکا طبق بند ۱۰، یعنی فروش نفت، مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم.
🔹
در رابطه با بند ۱۱، یعنی آزادشدن دارایی‌های…</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/farsna/445500" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه:  اولویت کنونی ایران، حصول اطمینان نسبت به اجرای مفاد یادداشت تفاهم است
🔹
در رابطه با تعهد آمریکا طبق بند ۱۰، یعنی فروش نفت، مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم.
🔹
در رابطه با بند ۱۱، یعنی آزادشدن دارایی‌های مسدودشده ایران، نیز فرآیند اجرایی‎‌شدن آن درحال پیگیری است.
🔹
در این چارچوب، همین هفته هیئتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/445499" target="_blank">📅 20:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aad982d1d.mp4?token=e8D8oWDZjhOqXqV98x7IRDuAGS8uuDq7JffKOunSDFSuMXRHaM1fRx4OTVWKtn752zkXAR_tpcO27Z23eqfzOhYyPdi5hKIC7xEa8rF31b9bM9qMsrrA2-z_Cu3XDMD4kWPYcVO3cc8J66ITkLAxhH3Ofl36IZcEVYXP6f5xXtpId3At7mXUe1krDjhA5KijWfYXApg1nx6uE0-0GbJ8KXg8ccXd7aky0Y8bkNI-OH07D_ejVHpEXIpOdSmo8Sq6UN38Oa1lJkocp3KC3gMoz59XmVEDwR7BCyNKwXq-lJxdobQwU_9aAVzGIRRRpu67aIdA8OVZXY2uZbQ3DzjZBmI--1FiI9DI-NSpqZmwQAF8mM87HH1xdyY55LLBTtUD6g6y4Ndy3wR-cZzD0GLVJz9cOie3bgKezvl0jrY91o83g8g1aQsJADebZ0j9DT_vCHVJ9JtPQMPrIllC_v3oHeV_hCQVd_guKAEorA69wRyFXKmibXtVsiKXEH9PYxP9m6PrcpFipls9Z5yQgAfSjn4eQxNhmTZ-57BZ_GlFjLxwQZsYP_bRP6REQUO0_tRUKBeK_bEcq7hAQYBGZs53_WZA4dgWLp6LeWRvxQoK5jWxmgpm_ETzbp5jr44pn9YeLlkNXFR5U2AqwJEA2Sfz8ZIXAmvGnMihKGE3YrTzWfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aad982d1d.mp4?token=e8D8oWDZjhOqXqV98x7IRDuAGS8uuDq7JffKOunSDFSuMXRHaM1fRx4OTVWKtn752zkXAR_tpcO27Z23eqfzOhYyPdi5hKIC7xEa8rF31b9bM9qMsrrA2-z_Cu3XDMD4kWPYcVO3cc8J66ITkLAxhH3Ofl36IZcEVYXP6f5xXtpId3At7mXUe1krDjhA5KijWfYXApg1nx6uE0-0GbJ8KXg8ccXd7aky0Y8bkNI-OH07D_ejVHpEXIpOdSmo8Sq6UN38Oa1lJkocp3KC3gMoz59XmVEDwR7BCyNKwXq-lJxdobQwU_9aAVzGIRRRpu67aIdA8OVZXY2uZbQ3DzjZBmI--1FiI9DI-NSpqZmwQAF8mM87HH1xdyY55LLBTtUD6g6y4Ndy3wR-cZzD0GLVJz9cOie3bgKezvl0jrY91o83g8g1aQsJADebZ0j9DT_vCHVJ9JtPQMPrIllC_v3oHeV_hCQVd_guKAEorA69wRyFXKmibXtVsiKXEH9PYxP9m6PrcpFipls9Z5yQgAfSjn4eQxNhmTZ-57BZ_GlFjLxwQZsYP_bRP6REQUO0_tRUKBeK_bEcq7hAQYBGZs53_WZA4dgWLp6LeWRvxQoK5jWxmgpm_ETzbp5jr44pn9YeLlkNXFR5U2AqwJEA2Sfz8ZIXAmvGnMihKGE3YrTzWfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تذکر پزشکیان به مصرف غیراستاندارد برق در سازمان استاندارد
🔹
در بازدید رئیس‌جمهور از سازمان ملی استاندارد چه گذشت؟
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/445498" target="_blank">📅 20:54 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHEJWQnt7glYNEtAIR0YCGBCH_nvbhC9XDLcYG2v0dptLT8FcrAbRf5NjKqSN3egac9hBm74NnWg2neuBJpGLs15jFmxPJo7cNpnlqSYpYkIwgTJGd-bY-p-b2PjPSeO7HUwp4Wf8X1SpT4JFYXm76MOm1fD47KWqBQdxpA4194YEjQTTh3zDejv1lWyyVNf6-sRe8Guzu36fePD3bz-3C1HDTyaLHSf-WisjdEbnfHiUKxL5qeUpaLR8yuP6Pp2wZbw9ru-iNJbWOSyLQgLmGyY2mPNxXuDHZqvQinSjiJSbhpxY_2Fm4Fo3SLU8Tj5Uq-kWkwLwEd8f6bmaoiMzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون سیاسی نیروی دریایی سپاه طی سانحه رانندگی درگذشت
🔹
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان جان خود را از دست داد.
🔹
پس از وقوع حادثه، نیروهای پلیس و اورژانس در محل حاضر شدند و دریادار دوم اکبرزاده به مرکز درمانی منتقل شد اما وی به‌دلیل شدت جراحات وارده، جان باخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445497" target="_blank">📅 20:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9395da4b1a.mp4?token=dU94GBO3JAvSPpCaBm7sRm-w_s6JLE0iS1MzhLhiXO9W3Gdh-sDZWgVx-z1W0v12a-hy0L6R4leSKlbtM2IHBoKorAkYj12WiVy3b8y6JkKc2YpoKq-W3r1S80Php0h2hrj2XY1IX0bpQeaFGmDXNtysdGKiaTV_zkb5C0ZvrqTlIoL-4lxwxJrtqLyfVOeyIL8GCRPHXAK9A6EwuxEv7hXWL6LrVZEN7vEC9--vq-V3Rp_7xWp4sZm4LcUlRATUOZkLaj4XzD4nffS1reqEUypDsAJbUfNI9tkG1ZmO9YvpXoJYvOl9EjkRhvDvkyjMpDeM_Dv2xfbmYHHMEEFB9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9395da4b1a.mp4?token=dU94GBO3JAvSPpCaBm7sRm-w_s6JLE0iS1MzhLhiXO9W3Gdh-sDZWgVx-z1W0v12a-hy0L6R4leSKlbtM2IHBoKorAkYj12WiVy3b8y6JkKc2YpoKq-W3r1S80Php0h2hrj2XY1IX0bpQeaFGmDXNtysdGKiaTV_zkb5C0ZvrqTlIoL-4lxwxJrtqLyfVOeyIL8GCRPHXAK9A6EwuxEv7hXWL6LrVZEN7vEC9--vq-V3Rp_7xWp4sZm4LcUlRATUOZkLaj4XzD4nffS1reqEUypDsAJbUfNI9tkG1ZmO9YvpXoJYvOl9EjkRhvDvkyjMpDeM_Dv2xfbmYHHMEEFB9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آجرلو، عضو رسانه‌‌ای تیم مذاکره‌کننده: فروش نفت ما کاملا به شرایط پیش‌از جنگ برگشته
🔹
ما قبل از این مدت‌ها ارزان‌تر از قیمت جهانی، نفت می‌‌فروختیم اما حالا بالاتر از قیمت جهانی می‌فروشیم.
🔹
همچنین حدود ۲۰ تا ۳۰ درصد بازار جدید در فروش نفت پیدا کرده‌‎ایم.…</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/445496" target="_blank">📅 20:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rt3SKvLpk6ZoVL2JKATErbCWBFePgjJX8Hswej19lESz_YPyqggrgp8fFIrKF0gL6OO_IOxBof2508fpeFEBBHol1SMeBm0zgzvIhxidk0mHn3hXOPvqxRnqqqaTU1psgzOfCp_jYdVTFKcEGuZbe2DCIBak5fQm8SD16ePFAhjFCNa_uEDq9bbmdKjVmh-jRCSOE8s7KxqkWVA6vwXQyDIS4e6W8LvAWlniSkcNvybWN1s5ftS1JTwZhUlMkRJIU8SA_HYL8gNyrYAmeucSCTLjcmEcvDpZBG64sy6yUDoeqIl7kO5WTJquOXtM50i0aCXWq33EDK-QjcOIizQi4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت شرکت اسرائیلی از مانور قدرت نفتکش‌های ایرانی
🔹
شرکت اسرائیلی پایش دریایی ویندوارد می‌گوید که یک نفتکش تحت تحریم آمریکا با پرچم نروژ در حرکت است.
🔹
این دومین مورد در یک هفته گذشته است که یک نفتکش ایرانی خود را در ریجستر اروپایی نشان می‌دهد؛ مورد قبلی یک کشتی حمل گاز مایع بود.
🔹
این شرکت اسرائیلی می‌گوید که این شیوه جسورانه آشکارا در برابر دیدگان نهادهای آمریکایی و اروپایی انجام می‌شود و یادآور نفتکش‌های غول‌پیکر ایرانی (VLCC) است که ۴۸ ساعت پیش از امضای تفاهم‌نامه از چابهار حرکت کردند و محاصره را شکستند.
🔹
ویندوارد معتقد است که این اقدام پیامی دارد و آن این است که ایران بی‌توجه به قوانین آمریکایی به صادرات انرژی خود ادامه خواهد داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/445495" target="_blank">📅 20:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">معاون بین‌الملل وزارت خارجه: مین‌زدایی از تنگۀ هرمز صرفا توسط ایران انجام می‌شود
🔹
غریب‌آبادی: «ماکرون گفته در مین‌زدایی از تنگه هرمز، با هماهنگی شرکایش، همکاری می‌کند. طبق یادداشت تفاهم اسلام‌آباد، مین‌زدایی صرفا توسط ایران انجام میشود و نه هیچ کشور دیگری، اصولا اجازۀ چنین کاری را هم نمی‌دهیم.
🔹
شرایط حساس و پیچیده است. توصیۀ اکید می‌کنیم فرانسه آن را با تحریکاتش پیچیده‌تر نکند.»
@Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/445494" target="_blank">📅 20:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq2BTwx8bUp0HIjMsTYM7zF8lAY-FYkX895EMBav2K7JaabtNMJUBKtSbmJUHzHK10779XQ5vIhVQarJodpmNH6wXAfig83Y6G4L7GKR7CNGKaMrCGST9xdGC4q5K3gdF2CDoEdfOVl_0C5-0ohzd843PpgTjmflcoipNtSk2exx1726GfjnyAPCUVJfs1O4WptNhs3j_OFTKy0pcF6-9npfNr4Lcs1Ga7nO8f5S7Gx12ZRg8qprYI16aFpSb0mmZqlkKPREQ_261HAyyOxdte_2qAk4FaGO0kIsMvkx9chC9Rbl9s55mpZFHp8-oKnsSI_X8hQT5tvnFUfpvHOacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از تردد در حاشیه رودخانه‌های این ۸ استان خودداری کنید
🔹
سازمان مدیریت بحران: برای روزهای سه‌شنبه و چهارشنبه در ۸ استان هشدار نارنجی صادر شده است؛ روز سه‌شنبه در ارتفاعات استان‌های مازندران، سمنان و بخش‌های شمالی استان تهران شاهد بارش‌ شدید باران خواهیم بود.
🔹
همچنین در روز چهارشنبه، احتمال وقوع بارش‌های نقطه‌ای در نیمه شرقی استان آذربایجان شرقی، نیمه جنوبی و مرکز استان اردبیل، گیلان، مازندران، البرز و بخش‌های وسیعی از استان‌های تهران، سمنان و گلستان وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/445493" target="_blank">📅 20:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b1589b2f.mp4?token=OVRZSlV9lNf8P4faNKzr3qRCTEnnq_YYZ0ouxKJNdiAMKAgh-JaUq_izBCzhiDl77qrmOCaEinmLIlGGlRJcPCFH492kCqrg0Z7BOTGoTKg4zYbElLFTvJ8bvRyjFatHgjAVRxBRxFn0c4ls4wzvBIzGFZZOk1szTWGub6J0HpafqQU2Klwau_sQ_L8AgBBGGZSuvnOeiwOzC40g1J19JC05g-uBykgcFThSPMH5Aqqi3qugDv9OTHuQw0YsFR5Ah2ein7vbNptF8GQxKenewqAyta6Q7Tyaz5UcVDU3T2PSlNdUS7mRzCAGDRuTGAz7FiVZ7DdxCZnMnMB05NEP7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b1589b2f.mp4?token=OVRZSlV9lNf8P4faNKzr3qRCTEnnq_YYZ0ouxKJNdiAMKAgh-JaUq_izBCzhiDl77qrmOCaEinmLIlGGlRJcPCFH492kCqrg0Z7BOTGoTKg4zYbElLFTvJ8bvRyjFatHgjAVRxBRxFn0c4ls4wzvBIzGFZZOk1szTWGub6J0HpafqQU2Klwau_sQ_L8AgBBGGZSuvnOeiwOzC40g1J19JC05g-uBykgcFThSPMH5Aqqi3qugDv9OTHuQw0YsFR5Ah2ein7vbNptF8GQxKenewqAyta6Q7Tyaz5UcVDU3T2PSlNdUS7mRzCAGDRuTGAz7FiVZ7DdxCZnMnMB05NEP7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آجرلو، عضو رسانه‌‌ای تیم مذاکره‌کننده: فروش نفت ما کاملا به شرایط پیش‌از جنگ برگشته
🔹
ما قبل از این مدت‌ها ارزان‌تر از قیمت جهانی، نفت می‌‌فروختیم اما حالا بالاتر از قیمت جهانی می‌فروشیم.
🔹
همچنین حدود ۲۰ تا ۳۰ درصد بازار جدید در فروش نفت پیدا کرده‌‎ایم.
@Farsna</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/farsna/445492" target="_blank">📅 20:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2XADNTrK5b2aAqh651dnIXdjvFT2OFnIXmq_vn53RM0b_sjhHbDJVyyXeK18dNCZFPewiPtd8ahYCW3p4m25iCvuZN4bHhX4Y5ReELvF5qZrDFSVoecFpeUjOrjrNiG9hV7Wa7XNg7Eftzs0ohFkbIj8d3iulZF4TS4gR7VUSEaMmPNJg0ohdKmpmELlQf4c9YnxvYIhjoKIccOyjMhnsy3jZ5vnc0rEIdWqy7FeoW6hyfUpw2BXaOG1nHoNrwvgJ3HuE_NqzXOzZNCLIpzP-JnA0vhZiBa8UESmGFkMnI3OeSstwNSb7U0ie4_nkqG2cxAdf8UDBHmq2D7FWw5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امتحان نهایی المپیادی‌ها حذف شد
🔹
وزیر آموزش‌وپرورش: امتحانات نهایی اعضای تیم‌های ملی المپیادهای بین‌المللی حذف می‌شود و به جای آن آزمون داخلی می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/445491" target="_blank">📅 20:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4mB7gjUWdmej4-bX78Yap046YxOHDSjfGYK5tTm_16y-P3Q1eBsZAwa_R0OFeZ91luE5sX7tqj3CRswYD8ee86PhtfMVVOY8rWg3drU9s75yjzUkT9B8Mpk4VrKqQEOZeDZcmniWJyShhh6bmnRXeOT6Ll5CB3xsqRMqt_GQBG2Hl0NUiYoBPD1H-pe_kXb2IsoBKM1zvFJ-WKjKtituZSb4TJIAn2pF9GLfxTSlNF_2X1Hh21Aa3VQWd0lYBdgNszwhd2B25GaDipp8D5gH_t1U8Kjn2Mxmbk5u6EvsHhf-VVQEod_-25TqNoyQJbDzG790fB1lLq38DGVldikOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایپا چکی نیسان می‌فروشد
🔹
سایپا شرایط فروش فوری خودروی زامیاد EX دوگانه‌سوزر را اعلام کرد؛ این فروش از ساعت ۱۰ صبح چهارشنبه آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/farsna/445490" target="_blank">📅 19:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سنتکام: هم‌اکنون بیش از ۵۰ هزار نظامی آمریکایی در خاورمیانه مستقر هستند.
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445489" target="_blank">📅 19:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445488">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🎥
رضا پهلوی: من باعث حمله به ایران شدم
@
Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445488" target="_blank">📅 19:42 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445485">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2aCL58gX3--MMYXirYu5nnrQfwHvTJYyXmNJ9KFxh5wAL11uPw7QUATou1Rl5eoh-b8dJbY9mVfSRQfyMDYL1mWI-nsBHIXasPqEzYpSpVgcdE58zJwSqv7p34ODvG6ef13iAHbKAuyr9rtWCd8UwVOs_kYDFxMt7KqpFaLmj5cZuTZu0mQ_I5uKcrjVTxdAlc5I3S1t8MA9zGz_7wD5cwj_yqDyEOePCxvkyytMrO_TUtKvveJNQJJ1iaBNt30nB_-VFjYDHu-Fa30U9l5bpGWzyaXllxf_HfHMQ-BqDt8mdhGsVMtVdWhVz3INURSNoWA1zEfNIVTohGZ0rCAbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAEBmKaOvQbVzMCPjh9LTy7s7tT1rwMFIqsz-YMbIzg2168W7ulMYKLNjNO-UT16goWMg60ER91XtEhxIgFG--rv0dVNduJDSSdNzFx7dy5b9RP3zc5NQkn7XlmXgh3odwy7YvdwL2ctVLQxY8uHA1LvibEfkzTx0knG3KoScvoFuqVzyhTQJQEJL84-Nmd2MgDmgslfmnGzm5pNGilqNGzk5U9WGD_NJv7q69xSl1y5FQ36pvF_XYL_ztl3AOcCmDJLWVWZVcHdkac2HZcl6a2POD5hKxHjfj12yo60oM-76L1ibnNv98Y-f4BPwGTln6VHaihko6CzUANF-tlXWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lopwAisdP14mr_jfW2bv5CH0KpWo0N92dZnU0bGaLRLXoP2pfkDSJQK_K2fJUNmen4O50TOGmiKWHnTgosz0KjatAsBfL6AL9q6z8RkvKLGwgHPovo0eUlYeseowEZsVcER6s2ZBoi9gCYyVZwoPLT5vfKwlMf-xdmcTLUUe2YZbIp-Z6AndWwTDRwI1bTVv6CEXHNlxHc58nvUW3j5NIMI2NKNwL6ufKM6jiWb61mT45H-zJrHLnpVG8ACuxTm8yOJSjDryxwM1elSbF-jsTCgAEAa-rLwjXOFvQvI6OeJYJgoq2ft5gKj7Vn6z0nagsaCHK2H2uewdFWKWQTIlVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زیارت وزیر کشور عراق از حرم حضرت معصومه(س)
🔹
الشمری، وزیر کشور عراق در چارچوب تعاملات دیپلماتیک به ایران سفر کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445485" target="_blank">📅 19:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445484">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvYj35SGbmgAz_z9_F-0xSK3ehZyEm4nNy4RXpfPd4zX2xT4bmv1d8F_FT2oo7bh5ZRzIbbeNEBntkPP59yBv-4uc7gxqa88tP-fP27UcmPND0S1PrksVnUQ10p_Rrezx-1zz3NaKi8UoBVEGgVbLnSAxEKPdlORMjukUBs3C1cVqpAO2CDIUgGvexKJDFKdTl7mI4cSXr-Yf4jDEZwaYVHwwMDsY6fgY63dbQ3Ipl6YvPIAltH9vBknLS8h75XavjwozhsTUV2cr4QNJxC152-zOW4bg7Jb1HPov76O6FVIbR_zP2ZhNcU7LlrqAJj9lN2nLhS0d3Ux6iPYbetrmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مخاطبان:
قطعی مکرر بانک‌ها مردم را کلافه کرده است
🔹
کاربران فارس‌من در پویشی خواستار رفع اختلال بانک‌ها شده و گفته‎اند که: این روزها اختلال در سامانه‌های بانک‌هایی مانند ملی، تجارت، صادرات و ملت، انجام بسیاری از کارهای روزمره مردم از خرید و انتقال وجه گرفته تا پرداخت‌های ضروری را با مشکل مواجه کرده است.
🔹
حامیان این پویش می‌گویند: با وجود وعده‌های مکرر برای رفع این اختلال‌ها، همچنان بسیاری از مردم با قطعی خدمات بانکی دست‌وپنجه نرم می‌کنند. از مسئولان مربوطه می‌خواهیم هرچه سریع‌تر این مشکلات را برطرف کرده و تا زمان رفع کامل، راهکارهای جایگزین برای ارائه خدمات در نظر بگیرند.
🎉
اگر شما هم از این اختلال‌ها متضرر شده‌اید، این پویش را
امضا
و از آن حمایت کنید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/445484" target="_blank">📅 19:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445483">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fw9naTOGht1ABksPs1fiSM6zlEehUJOOp7PurpkcWHE5xm0H62J5l75mlnCci6H1HfZl-QTYywk9SQJqolLfESO4wGxr7hnQztYK7501rn9xWJU38gyJ4OauiMLZa0RL6j0E05TCguajXX6P5GMBseET08T0vdMm2PSru33S7C07uYHGOrh8h4KN_5a5A5JvpQ_wxB1rTVuaOQSHtxevTykSFZjFSC24wvC-td3gHXRWkNq_KeaFll0jrTz_tmOokhNYK4B9mcRFZy_hJ6Rw4k1RFmRwiuBy3xDqoBjhI3KqPPUretfTcjyK7eqUtfyBpxvimW_U4yzlC-dCMRFrSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدرقه آقای شهید ایران
🔹
مراسم وداع در مصلای امام خمینی(ره):
از ساعت ۶ صبح شنبه ۱۳ تیر ماه
الی اذان مغرب یک شنبه ۱۴ تیرماه
🔹
مراسم تشییع تهران:
از ساعت ۶ صبح دوشنبه ۱۵ تیرماه
@Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/445483" target="_blank">📅 19:25 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445482">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8ASpbD5rlCV52w6iaZZmy3Ppq67nKJmJmNOumi0_90lSAzJ1L1sThd15OhyivAHGKCAac6FY_OhC32TBQZeDmiCOMrj3ISiEmDMyWDDbEcyWvogqMg5Zb_3TohjW-CZmN-urc1tYQbjl16vzvPGBH6mv6AkcQPPm49DbwttWeo1Wuoqs8i3SrEnOLJv6ijgTj9mTTA3JymTpoKU3CEq6ts6d_7pa7l1mQAcFLvvWCWYY3Ui-EwXEo1UFfThyQ5DpdaAqTfF5zCT-NxuS_Xa6PALpj1ENBuzrTvu5fp6V1BwK6c4tabv8z8o7p4OR8Kiecc5-gtOIknD4wvuDCkWeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
داغ‌ترین شهر ۲۴ ساعت گذشتۀ جهان در ایران
🔹
داده‌های سرویس جهانی هواشناسی Ogimet نشان می‌دهد، در شبانه‌روز گذشته زابل با میانگین دمایی ۴۸.۶ درجه، گرم‌ترین شهر جهان بوده است.
🔹
همچنین ۵ شهر طبس، بافق، دهلران و بم در میان ۱۰ شهر گرم جهان قرار دارند.
🔹
طبق اعلام سازمان بهداشت جهانی در ۱۰ روز گذشته، ۱۳۰۰ نفر در اروپا به‌خاطر گرمای هوا جان خود را از دست داده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/445482" target="_blank">📅 18:59 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9vHjtUItjztnMIxymH2mLTxWKvV90j2GfTA7D2Wtxk7byQy1sL90Rv4iOPqKXg7g87V3J4s8ufLr4MTpqptSktYPPHfYvqGUTQcm3TudgrecEpuae3hA7HR0S1xPArAwxihb38-yXpLa-JtFsodulk9bC5LL4SbzbVLhcmtW96Br4tw3B2uHf4nMsS4iEej3t5ScsSAYS-A8HUQskS8jjXp6NcVM8XWXVKtte0uZIIjcpZPtM6u1AHJN0x9DySjgZlA30rPH_Dt55E0BwmXlSrLIWL7oDj4YaSdqrFHU0O6qpQW35ytximUAUp-QVwAO1I4LWYObYp7xZEZu_h3Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر عراق: ائتلاف آمریکایی ۳ ماه دیگر کاملا از عراق خارج می‌شود
🔹
علی الزیدی در دیدار با برخی سفرای کشورهای اتحادیۀ اروپا: نیروهای ائتلاف موسوم به ضد داعش به رهبری آمریکا تا پایان سپتامبر آینده (هشتم مهرماه)  به صورت کامل از عراق خارج خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/445481" target="_blank">📅 18:53 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445480">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🎥
وزیر کار: ۸۶ همت از حقوق بازنشستگان احقاق شد
🔹
میدری: با پیگیری قوه قضائیه، ۸۶ هزار میلیارد تومان از سرمایه صندوق بازنشستگی با رای قوه‌قضائیه به اموال این صندوق بازگشت. @Farsna</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/farsna/445480" target="_blank">📅 18:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445479">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8ZGs-2lbW6kIGYOIp9KibCUSruA4D2FAdaBW-EcYy3eAa_h3GfU8BXzZNh9K4YZhia2g1MvV-GHFDBQskzqQD7hvh8x_g3cDV6Mro8_vLSI6JbC97XpMkK3SZq74yuWaHwvdbBKx1skvnE2RW06wMdSDXZHnZf3N3vRgKTKJm3MTdR7tTZNvbEgx6GWxCm0dwTsWpSkuHtBtQUAXo4PqngR_Jw97CqeZJ6GtB8bkVsjC9oKfQPl1qUM9xlqa4E_ecJrx6XPpLjk3KVRTzLd3w7Qd0paiSY7dkta8CyVs2SgP4ToKslcU-6grzkcOi74qdqafF4yLls2rgaIW0luYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف احتکار ۲۰ هزار تن نهادۀ دامی در مازندران
🔹
فرمانده انتظامی استان مازندران: ۲ متهم اصلی پروندۀ یک شبکه احتکار نهاده‌های دامی و توزیع خارج از شبکه دستگیر شدند؛ از این گروه، بیش از ۲۰ هزار تن نهادۀ احتکاری کشف شد.
🔹
ارزش محموله‌های کشف‌شده ‌هزار و ۶۴۰ میلیارد تومان برآورد شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/445479" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445478">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قطر فعالیت دریایی در خلیج فارس را متوقف کرد
🔹
وزارت راه‌وترابری قطر عصر امروز با صدور اطلاعیه‌ای اعلام کرد به‌منظور حفظ ایمنی عمومی، تمامی فعالیت‌های دریایی در این کشور به‌طور موقت متوقف می‌شود.
🔹
این وزارتخانه از تمامی مالکان و استفاده‌کنندگان وسایل دریایی خواست تا اطلاع ثانوی از حرکت در دریا خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/445478" target="_blank">📅 18:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445477">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c9180868e.mp4?token=C9PE-4lh_k_vzkTLeD64ROFkmV43j84x5QdsqHk6Metq6dISJUWOrh07W17rqdxHMwSZPAY7hPsvpPo7omRG08-65YFD0j7gDwmA1__MVI7WS5fK3UhoSv565bQJlbLJSdZCSpOmPoIbOVEvnwJFnvLJaoo7L2FqTxExy5L7rHGDUJ8mYyJHbGjBd6NImy28u66A0_FrrL_9Rup5j9si-bqbULn8pAmMF_rWcENnKyq-JLISAJ7AgA975gioOT1uTJba30csukflt7C2sYq5OLOqEl8t47t3sRAsTFz_NtolimAm-Jh192aRYsKyy0XwlK8THG4_J6QPk5vuDilOxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c9180868e.mp4?token=C9PE-4lh_k_vzkTLeD64ROFkmV43j84x5QdsqHk6Metq6dISJUWOrh07W17rqdxHMwSZPAY7hPsvpPo7omRG08-65YFD0j7gDwmA1__MVI7WS5fK3UhoSv565bQJlbLJSdZCSpOmPoIbOVEvnwJFnvLJaoo7L2FqTxExy5L7rHGDUJ8mYyJHbGjBd6NImy28u66A0_FrrL_9Rup5j9si-bqbULn8pAmMF_rWcENnKyq-JLISAJ7AgA975gioOT1uTJba30csukflt7C2sYq5OLOqEl8t47t3sRAsTFz_NtolimAm-Jh192aRYsKyy0XwlK8THG4_J6QPk5vuDilOxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمار عجیب تیم ملی ایران در جام جهانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/445477" target="_blank">📅 18:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445476">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6Ytif1rJMBDerNhoInOY468902cNZh0dFaGdch_P7hel7uYH1u3cKPXtChT8StYfb1RLn5i35OpMvFWX0UyjkNhAjbSHO-f1GJ3_57FR1m02pIjkmdxOd5H7QzxZJ-hegwbsN-_VEMRzLdmt0aXje7ZF8sRlT40PO3KIWypugKt0QShsbFa0wVSVOT8YG-wu40MJ-k4S451uQIWxgyHhyzcFkV_hCAwrHPhryPak-o2_JOygYW4_vHD7a4mQD5FsQUs0OULvtbznfnPTxtzTTtkKIb0kWC5ScKKCBjkOQ2aKy0cGMGoDy9tcPBoQPq2tnbuY9WDF_lQusP9kEgGeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان شایعه جدایی ۲ پرسپولیسی کهنه‌کار
🔹
در ساعات اخیر شایعاتی درباره آینده امید عالیشاه و مرتضی پورعلی‌گنجی مطرح شده و برخی مدعی شده‌اند باشگاه پرسپولیس به این دو بازیکن پیشنهاد فسخ قرارداد یا انتقال قرضی به تیم‌های دیگر را داده اما پیگیری‌های فارس از این دو بازیکن نشان می‌دهد چنین ادعایی صحت ندارد.
⏺
پرسپولیس تاکنون هیچ پیشنهادی مبنی بر فسخ قرارداد یا جدایی قرضی به امید عالیشاه و مرتضی پورعلی‌گنجی ارائه نکرده و اخبار منتشرشده دراین‌خصوص صحت ندارد.
⏺
عالیشاه و پورعلی‌گنجی هر دو برای فصل آینده با باشگاه پرسپولیس قرارداد معتبر دارند و طبق قراردادشان در جمع سرخ‌پوشان حضور خواهند داشت، مگر اینکه در ادامه نقل‌وانتقالات شرایط جدیدی به وجود بیاید که تاکنون چنین موضوعی از سوی باشگاه مطرح نشده است.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/445476" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445475">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFkPairSl8G1sAu8dZiCLymuNHbUTWPcqJ9wXQKFAgVanBtLS83zKrOJXCIB3XDFyyhOGBlDee8XReTsY-NIKbSoTClxfPjK9-DXj-DE3UtMpZx8Bm1KXPVBplaDwRkYIColDPeH0o553FtBlr7X_d_7vXwxrUwnlnaKo9yy3gavW6AU9oDl3gkKm_2RBW6SAwiah3SLofgBW0lc7F0nGDEWo-4VBVgTKMMkDTRIw2yI6IbCRuOVfb4D-S433lsncQSKC-sJICI0GyB38vSnUoyWUk_At-HAuPJs754fQQn-qGOiETGkuTPw9LE4T5tgvvWs8kT1vNIJvDjFed6EUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روش پرداخت کالابرگ ۱۴ سال به صورت یک‍جا به مردم
🔹
با مسکونی کردن فقط یک درصد از مساحت ایران، به هر ایرانی ۲۰۰ مترمربع زمین می‌رسد. با توجه به متوسط قیمت زمین در کشور، ارزش این زمین می‌تواند برای هر نفر به بیش از ۲ میلیارد تومان برسد. این رقم به اندازه ارزش ۱۴ سال پرداخت کالابرگ است.
🔹
در حالی که از ابتدای سال ۱۴۰۰ واگذاری زمین به مردم آغاز شده بود، فرزانه صادق مالواجرد حدود دو سال است واگذاری زمین را متوقف کرده و زمین‌ها در احتکار دولت باقی مانده‌اند.
🔹
حدود ۷ میلیون خانواده از جمعیت کشور مستأجر هستند و ۵ میلیون خانواده نیز اصلا خانه‌ای برای سرپناه ندارند و در خانه دیگران سکونت دارند. با واگذاری زمین و فراهم کردن بستر ساخت، می‌توان بخشی از بار سنگین اجاره‌نشینی را از دوش آن‌ها برداشت.
🔹
کمک به معیشت مردم هم‌اکنون از اصلی‌ترین دغدغه‌های دولت است و برای این‌ کار، کل دولتمردان بسیج شدند تا رقم کالابرگ را اندکی افزایش دهند، درحالی‌که زمین دارایی برای دولت است که می‌تواند بدون نیاز به بودجه بزرگ در اختیار مردم قرار گرفته و اساسی‌ترین نیاز مردم را رفع کند.
🔹
وزیر راه و شهرسازی فرزانه صادق جلوی واگذاری زمین به مردم را گرفته و معتقد است که به جای آن راهکارهای جایگزین مانند توسعه مسکن استیجاری برای زوج‌های جوان را دنبال کرد.
🔹
در مقابل معاون سابق مسکن وزرات راه هادی عباسی می‌گوید که زمین از جمله دارایی‌های دولت است که هم‌اکنون غیر مولد مانده و به اقتصاد کمکی نمی‌کند و اگر عرضه زمین شروع شود، بدون نیاز به بودجه می‌توان مسئله مردم را حل کرد.
🔸
طبق تجربه مسکن مهر و نهضت ملی مسکن، دولت می‌تواند با واگذاری زمین به مردم و راه‌اندازی سامانه‌ای که سازندگان را به‌صورت مستقیم به مالکان زمین متصل کند، تنها با عرضه یک درصد زمین‌های به هر خانواده سه نفر حداقل ۶۰۰ متر زمین بدهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/445475" target="_blank">📅 17:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445474">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOnRVjaURM8nUDiFpn1rk2gZmAyEFftgHlRQHdLsauhIPNeLUu9GO_L_-_sxu9oAgfIjB6qiToFKeDgzWr7FEsv_eSdo88fsnqQeJna3QYUQJMCIeGd-P6sB_f7TlzGzDsFlCHsE4TqUvkWD0NntRopWfRQgEJ1XNKqTdXrmdJcYYWJaIxO18qZ8Y9z_2oaD9oxXb4vv9Ntf-WcUY0iy7xrwT9lZB3l_QTdSbZU9CaQ2Kg-8a1_Fjm9P6hLvEP8ZHp4Ru4xYQcbvUYHW2ojUFWTKbXHpJ0V1fbUd_gNXiamUBzDipUfFEIcEQ1s6zE9NJO-F9sjAC_daBwtwbTeCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک شهر برای جذب نیروی «بانکدار» آزمون استخدامی برگزار می‌کند
🔹
بانک شهر به‌منظور تأمین بخشی از نیروی انسانی مورد نیاز خود، از میان متقاضیان واجد شرایط، در رده شغلی «بانکدار» نیرو جذب می‌کند.
🔹
به گزارش روابط عمومی بانک شهر، بر این اساس، فرآیند جذب از طریق برگزاری آزمون کتبی و با همکاری مرکز سنجش دانشگاه آزاد اسلامی انجام خواهد شد و متقاضیان واجد شرایط، اعم از زن و مرد، می‌توانند در این آزمون شرکت کنند.
🔹
داوطلبانی که در آزمون کتبی حد نصاب لازم را کسب کنند، به مصاحبه‌های تخصصی و عمومی دعوت خواهند شد. در صورت موفقیت در مراحل ارزیابی، فرآیند به‌کارگیری آنان مطابق ضوابط، مقررات و آیین‌نامه‌های داخلی بانک شهر انجام می‌شود.
🔹
بر اساس شرایط اعلام‌شده، دارندگان مدرک کارشناسی با حداکثر ۲۸ سال سن و دارندگان مدرک کارشناسی ارشد با حداکثر ۳۰ سال سن (مدت خدمت سربازی آقایان به سقف سنی اضافه می شود) و همچنین داوطلبان صرفا دارای سابقه بانکی با حداکثر ۴۰ سال سن، مجاز به شرکت در این آزمون هستند.
🔹
متقاضیان برای اطلاع از شرایط ثبت‌نام و جزئیات آزمون می‌توانند از روز سه‌شنبه ۹ تیرماه به پایگاه اینترنتی مرکز سنجش دانشگاه آزاد اسلامی به نشانی:
https://azmoon.org
مراجعه کنند. همچنین این آزمون استخدامی در تاریخ 9 مردادماه برگزار خواهد شد.</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/445474" target="_blank">📅 17:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445473">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/445473" target="_blank">📅 17:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445472">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زمان پیش‌فروش بلیت سفرهای جاده‌ای برای تشییع رهبر شهید
انقلاب
🔹
سازمان حمل‌ونقل جاده‌ای: با توجه به مراسم تشییع پیکر مطهر رهبر شهید انقلاب، پیش‌فروش بلیت اتوبوس به مقصد تهران، در بازه زمانی ۱۲ تا ۱۵ تیرماه انجام می‌شود.
🔹
پیش‌فروش بلیت برای حضور عزاداران در قم طی روزهای ۱۵ و ۱۶ تیرماه و برای سفر به مشهد نیز ۱۶ تا ۲۰ تیرماه انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445472" target="_blank">📅 17:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445471">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">افشای تخلف میلیون یورویی یک شرکت دولتی
🔹
سندی به دست خبرنگار فارس رسیده که نشان می‌دهد گروه صنایع شیر ایران (پگاه) از سال ۹۸ تا ۱۴۰۳ بیش از ۱۵۷ میلیون یورو ارز حاصل از صادرات را به چرخۀ رسمی بازنگردانده است.
🔹
چند روز پیش نیز حسابرس دیوان محاسبات در نامه‌ای به صندوق بازنشستگی کشوری امضای مدیرعامل شرکت صنایع شیر ایران را غیر قانونی اعلام کرده بود؛ چرا که این شرکت شبه دولتی با وجود منع قانونی یک بازنشسته را به عنوان مدیرعامل به کار گرفته است.
🔸
شرکت پگاه زیر مجموعه صندوق بازنشستگی کشوری و وابسته به وزارت کار است که حدود ۳۵ درصد از بازار لبنیات کشور را در اختیار دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445471" target="_blank">📅 17:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445470">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-ozLAPI0Du1FuZEqRza-ImUrg21x1OpkC5daxjBGGvCJCWQIJyy9O1aBpArm1k8wKgBRLkHejTXXxIEkVinirC15lpzZNx8VqTvoWMrtQPdFmcMWBdgv8ndk_HYbJMG5r4qodY8O6hGM9UamkJVpYeNFJXhcFPNSmUIyw3SKZCFUj4NllcJGWDVb9xU4rLPDoQDYO0XQ6AuvnO23ZiCFsVQAVsiU77Gnpj-D4SrnhHXE1gI2vzj14kPYLQwOc3fraMY1GANiyKxAKWFlNq3ZeItQxm9IWTCEjPt2AL8rY_FQCSE46eiJ9DfnR2Wy0KUcPEYuxK4myh8KRjxQ6wdaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین نشست کمیتهٔ مشترک ایران و عمان دربارهٔ تنگهٔ هرمز برگزار شد
🔹
معاون حقوقی وزارت خارجه: در سفر به مسقط اولین نشست کمیتهٔ مشترک هرمز با وزیر مشاور امور خارجه عمان برگزار شد که ضمن مرور مسائل جاری در رابطه با تنگه، دربارهٔ مدیریت آیندهٔ تنگه در چهارچوب…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445470" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445469">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73f3e58e4c.mp4?token=dXbo_uZ1Idnn3dXdEBGB_2EuQkNeHIosidKEj4FDQD2Ar-NWDImTxgNHYDT-MmIPeI1pijv1SRb-qkW9U98m62QZCXxgDM-IK2pATwgAlYbEVt3NJKtrwafjKjIRazATa5uYXZE4DhMOvfcLE4JodZsBTJAKab3M3a2hTxKkbNwuEe_LCRng5270CONqNfx2XUBHMaAhhvJ-m-2HiBxxL1UmSJ3EQX8EigX-ZtU6tPCYCE_FsEIwLC8rlXAXUbgAoUa89BxrdZf5REKYurTrVr9lo_-N1DxYDW-yWAABRjc7VIiDJe9891Fi1BG1R3fvXHRTrCRXKpg7zg4OjOkPjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73f3e58e4c.mp4?token=dXbo_uZ1Idnn3dXdEBGB_2EuQkNeHIosidKEj4FDQD2Ar-NWDImTxgNHYDT-MmIPeI1pijv1SRb-qkW9U98m62QZCXxgDM-IK2pATwgAlYbEVt3NJKtrwafjKjIRazATa5uYXZE4DhMOvfcLE4JodZsBTJAKab3M3a2hTxKkbNwuEe_LCRng5270CONqNfx2XUBHMaAhhvJ-m-2HiBxxL1UmSJ3EQX8EigX-ZtU6tPCYCE_FsEIwLC8rlXAXUbgAoUa89BxrdZf5REKYurTrVr9lo_-N1DxYDW-yWAABRjc7VIiDJe9891Fi1BG1R3fvXHRTrCRXKpg7zg4OjOkPjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحبت‌های شنیدنی حجت‌الاسلام میرهاشم حسینی در خصوص موهبت داشتن فرزند
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445469" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445463">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">عروج</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/farsna/445463" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
موسیقی رسمی تشییع پیکر «رهبر شهید» منتشر شد
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445463" target="_blank">📅 16:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445462">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8Gok1OUZcPfZ04CE6CDt9-I1aUX07_mZ6oTKYmc-8kq7HZ5SHU4few5NERbvLRi3cTHWd6uK7_POIDL1bF-E1XiNLb1h0-h4ngxsxXi7sk_Q2DDD5Ivr7rDimGYwqd3YzdBJOH0M-_cYgB7LmkLTsd2qvmhY9-gQmN5lfWdxdNI9aAtXHaInXevdQaAlr32JPKonTiytveW1c_jWT7AKFfyL2oJts1fQ8Z9EXYlgclby2tGFQsIsYMIwSQvFFTLEHKpOky6kYAbzvBNc1ZLJYqu_Yje4gF5CUMlu9_FqjJFIBAzBnE__OdxrKUYDkowlpW-jVuePm0LKTBm3BR1nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک سوال از آقای مجری که حالا منتقد هیئات شده است
🔹
ویدیویی از رضا رشیدپور منتشر شده که در آن می‌گوید: مداحی‌ها چرا سیاسی شده؟ مداح‌ها چرا در هیئت‌ها نظر سیاسی می‌دهند؟
🔹
امام موسی صدر تعبیری دارند که هر سال در ایام محرم بسیار نقل می‌شود: «در هیئتی که دغدغه مبارزه با اسرائیل نباشد، شِمر هم سینه می‌زند.»
🔹
اما اگر بخواهیم با منطق خود آقای رشیدپور به موضوع نگاه کنیم(باز هم این نقد وارد نیست.) اگر معتقدید مداح نباید وارد سیاست شود، این قاعده باید درباره مجری و بازیگر و ... هم باشد.
🔹
در این صورت، یک مجری تلویزیون هم نباید در عرصه سیاست نقش‌آفرینی کند.
🔹
جالب آن‌که آقای رشیدپور در بخشی از صحبت‌هایش می‌گوید: «حاج حسین فخری را گوش می‌کنیم، گریه می‌کنیم.»
🔹
اما ظاهراً خودِ آقای مجری، چندان هم پای منبر و هیئت حاج حسین فخری ننشسته است؛ وگرنه می‌دانست که او تنها مداحی نمی‌کند. حاج حسین فخری در هیئتش از استقلال و آزادی می‌گوید.
🔹
بنابراین، اگر ورود مداح به مسائل سیاسی محل اشکال است، این اشکال باید به همان میزان متوجه هر چهره رسانه‌ای و مجری‌ای هم باشد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445462" target="_blank">📅 16:43 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445461">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انهدام مهمات عمل‌نکردهٔ دشمن در بندرعباس
🔹
سپاه هرمزگان: از فردا به‌مدت ۲ روز در حومهٔ بندرعباس عملیات انهدام مهمات جنگ رمضان انجام می‌شود؛ احتمال شنیدن صدای انفجار ناشی از این عملیات وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445461" target="_blank">📅 16:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445460">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حملهٔ حزب‌الله به مقر افسران ارشد ارتش اسرائیل در جنوب لبنان
🔹
برخی منابع لبنانی گزارش کردند که نیروهای حزب‌الله امروز یک بستهٔ انفجاری را در مقر جانشین فرمانده یکی از تیپ‌های ارتش اسرائیل منفجر کرده‌اند.
🔹
در جریان این عملیات، ۲ نظامی زخمی شدند که وضعیت یکی از آنان وخیم گزارش شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/445460" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445459">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOqYJUrFNrs1QvldTEYFHvISyIwFXAHBXQbpC4QEw0U_Es-liL6v1SkZePvpEV3CLmTfS2n_2vOBkecHfGOTJDUVkP6JckvX1wlbB4iShZm8a5COuomHkAZcBdoSt8SNwW614rXXGrvCBQGgmiK1_Qc3gSylI9i0ATIYtitdEYph3QV3eMS27k_YLvBoev89t6CDHLjEmHnF4ynZzRvstz4d39QyyTCaR2leCjYs1oSewqn4wnsn7IjSYGbD3sn8P1W-RPAsWrYsXdP2JPY6Cf3Y0Q04Yx0TuQkXee7V3sUhWUfvgEwWmDsE6WhBnggeZjx6LxRIDjyZ5d3rb-_XaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک مامور نیروی انتظامی در چهارمحال‌وبختیاری
🔹
شهید احسان احمدی، صبح دیروز حین انجام مأموریت تعقیب‌وگریز متخلفان در مسیر جونقان به فارسان چهارمحال‌وبختیاری به‌ درجهٔ رفیع شهادت نائل شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445459" target="_blank">📅 16:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445458">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5cTCZqqTcQ2BeEHWHMbp8NPNqnhBK3VtgFwQAqg-VoddpBEi9KdDAqtQEt6UVzZX6EAa0DoHRW9t2t_NmD-TZUZuiaeRKx-5zT4AlrE_cKlmiyyX4RP6bJtMRNpU_EivexQXkUNot90xKLcI7BRH2K5p-fU5RWepQrDumD8cxoMLmTEZdZQ7w7AzJ4B-ujK5hr-hIOoUrre3JgxR0MiA3AvkqgTn33fIf_I0-waxQOE4C2_N14eJ0kGJ7d3EgC8uAMCMnu91Fdm0cCkXABCQSLv__mvOXvRp0FEd53juHaHsBl3lngLvbCe81Z08lqwY7MBKQJTHR-W3SIX3Blsvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعهٔ جدایی ۲ پرسپولیسی کهنه‌کار صحت ندارد
🔹
پیگیری خبرنگار فارس نشان‌ می‌دهد شایعات مطرح‌شده دربارهٔ آیندهٔ عالیشاه و پورعلی‌گنجی مبنی‌بر اینکه «باشگاه پرسپولیس به این ۲ بازیکن پیشنهاد فسخ قرارداد یا انتقال قرضی به تیم‌های دیگر را داده است» صحت ندارد.
🔹
عالیشاه و پورعلی‌گنجی هر ۲ برای فصل آینده با پرسپولیس قرارداد دارند و طبق قراردادشان در جمع سرخ‌پوشان حضور خواهند داشت، مگر اینکه در ادامهٔ نقل‌وانتقالات شرایط جدیدی به‌وجود بیاید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445458" target="_blank">📅 16:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445457">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab32ba603e.mp4?token=Ywwk_WeTKqtRaw4xMAtwtGutFE0hn9DC1no5Y_7ccoBhGfUOn1EDMJwixRMUvdKPmgYv7ZBHvUoZCt7us4ICwJ3nzE_Ybv8hV5ReI8dt2o-dJqDnzDRBPEcb8eWIT9613Ky9u6ovm0Iq4r7lqZP9dEZugrXJ_NRbgyDnWmSm-xCBZE6kIkl0n8jxWcWMaFbdsZC34wvykXIIkbKQGbMz5fyLuFstGH9ytTPCeMWWN5jWp_yeNZmTJSa4AcPMklxhcSz510dgEuHGRe8-yDyxPz9zdl7C5SzqGnB4DzWNrtY9sGmNgAFwzHrprg1Mcv5UeHa7Vw08FiqIBWMBfIYcLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab32ba603e.mp4?token=Ywwk_WeTKqtRaw4xMAtwtGutFE0hn9DC1no5Y_7ccoBhGfUOn1EDMJwixRMUvdKPmgYv7ZBHvUoZCt7us4ICwJ3nzE_Ybv8hV5ReI8dt2o-dJqDnzDRBPEcb8eWIT9613Ky9u6ovm0Iq4r7lqZP9dEZugrXJ_NRbgyDnWmSm-xCBZE6kIkl0n8jxWcWMaFbdsZC34wvykXIIkbKQGbMz5fyLuFstGH9ytTPCeMWWN5jWp_yeNZmTJSa4AcPMklxhcSz510dgEuHGRe8-yDyxPz9zdl7C5SzqGnB4DzWNrtY9sGmNgAFwzHrprg1Mcv5UeHa7Vw08FiqIBWMBfIYcLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایندهٔ سابق کنگره: آمریکا در جنگ پیروز نشد و ایران کنترل تنگهٔ هرمز را در دست دارد
🔹
گرین، نمایندهٔ پیشین مجلس نمایندگان آمریکا که زمانی از حامیان ترامپ بود، از اقدامات او در جنگ با ایران انتقاد کرده و گفته که «ایران نشان داد هر زمان که بخواهد، می‌تواند تنگهٔ هرمز را باز یا بسته کند. تیلور گرین همچنین گفت: آمریکا در جنگی که به‌همراه اسرائیل علیه ایران آغاز کرد، نتوانسته به پیروزی برسد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445457" target="_blank">📅 16:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445456">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHHe0aNlBYp0f0pctWwrIm7B-KGgp50R-oYvpBVTlbkTS8SbTxWIri6X22L-KviXaQ7DUfnzRD8jg-8dvaDvBMEn9ypLVcSCyQt6iXsdp-I29ci0roFg3Ywqz-a7h9ZralgKG1bKNadDG-Whn6HdigBowscbas-npEJ3ZC2d2wHBZprxTcW5NgPwehYZvK8qdZVZsuBMjKd06ls2yOrNXyYGvZvHu4VtirEJGRQtjV0bb87ivx9YSXUt2Z696DzqeZrcPvEXsbElHc62RWd_0TjStiYxYvGq2fE2aH5kC3oSduujHlOzePQClCyagRqEqY_wOYTWmam2arKU3tvg-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادق زیباکلام بازداشت شد
🔹
صادق زیباکلام صبح امروز با دستور قضایی بازداشت شد. پیش‌تر دادستانی تهران از تشدید قرار نظارت قضایی او به‌دلیل نقض ممنوعیت هرگونه فعالیت رسانه‌ای و تولید محتوا در شبکه‌های اجتماعی خبر داده بود.
🔹
براساس اعلام مراجع قضایی، زیباکلام…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445456" target="_blank">📅 15:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445455">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d571babdf.mp4?token=N_IAy57IMPnX3NVljpkLiGgDK_OKJZYBR3ND7s1obHC7HiPtNwg_Tqn34rFQkoKN7fIJra103oZroEE38i0bUbHmyDbK6W1YdQa6J6nHSMd5y-mfTlA2rk7kqAJkUAtXVnsZNoGN1kN_9ez7PrNVaxfKtvduhEVw-bJRwSI-p3G4--VeT2VCKk0DvALIX5ufiQAkhTc_--yPclrUVzffQ-vIYPXeegzPo2W631F9s_bFxzW1eTpkeJe8hx7WBQAmcdsMrfkInL6BoXdOCqzu0hb1bzkjiZNXuth9GLoypBtEt0btsqpanrtfQaURHnq5FfrdOTQCgVB5DbRvtBchOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d571babdf.mp4?token=N_IAy57IMPnX3NVljpkLiGgDK_OKJZYBR3ND7s1obHC7HiPtNwg_Tqn34rFQkoKN7fIJra103oZroEE38i0bUbHmyDbK6W1YdQa6J6nHSMd5y-mfTlA2rk7kqAJkUAtXVnsZNoGN1kN_9ez7PrNVaxfKtvduhEVw-bJRwSI-p3G4--VeT2VCKk0DvALIX5ufiQAkhTc_--yPclrUVzffQ-vIYPXeegzPo2W631F9s_bFxzW1eTpkeJe8hx7WBQAmcdsMrfkInL6BoXdOCqzu0hb1bzkjiZNXuth9GLoypBtEt0btsqpanrtfQaURHnq5FfrdOTQCgVB5DbRvtBchOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: پیام رهبر انقلاب نیازی به توضیح ندارد؛ اگر حیاتی باشد سعی می‌کنیم تمام نکات این پیام را عملی کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445455" target="_blank">📅 15:26 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445454">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953a240d06.mp4?token=XttflS9UQGQ6fpCKOsCFC3TQDFV0Zw5i_A2a9LzB7_FAjpn62Z5um-kHqTP3ErPtROTwQrjEFXjr4pBGfqFfriE2H7n-GN6Z88PtE8XSP1y9txHrx9OQioiEY8Dn_n7tIUj_R7PO1bVz7-lD1QrAOX0Rp0IzRK4hyEyxcbHntkP6-leAvfz69Ywf_UUk2NrvCDZuB2rsGvtUTk2enIfdIm_FuM8iOy1hWZjB4dqs7pBKpa5OKryTIV1g9PFoKk9RUNDCutqilz8oT36feHzglOy6VljnS-QPFjDq6VFwagjM4SsR_x6zyw7UeLm57930Z6Ud5ohJ2-_h1vo1CqxBOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953a240d06.mp4?token=XttflS9UQGQ6fpCKOsCFC3TQDFV0Zw5i_A2a9LzB7_FAjpn62Z5um-kHqTP3ErPtROTwQrjEFXjr4pBGfqFfriE2H7n-GN6Z88PtE8XSP1y9txHrx9OQioiEY8Dn_n7tIUj_R7PO1bVz7-lD1QrAOX0Rp0IzRK4hyEyxcbHntkP6-leAvfz69Ywf_UUk2NrvCDZuB2rsGvtUTk2enIfdIm_FuM8iOy1hWZjB4dqs7pBKpa5OKryTIV1g9PFoKk9RUNDCutqilz8oT36feHzglOy6VljnS-QPFjDq6VFwagjM4SsR_x6zyw7UeLm57930Z6Ud5ohJ2-_h1vo1CqxBOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: پیام رهبر انقلاب را باید چندین بار خواند و به تک‌تک کلمات آن دقت کرد.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445454" target="_blank">📅 15:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445453">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c77f3062d2.mp4?token=LvZ-gZIoHui-jXReznjgGymXIryQWiGMfRkgeEYjH86kH1n6KLx0rZaBroTId9h58AhXOjYYILeaIIar2u56fmgcsj8VUfVO7yQNwbMxBR7wasC1Nt_4Ag5eSuuo3EE3FfDC_SISRGKi6uW6cM_-XlYwgadzayF_ZEIbGRHkfDfYQ5ugz14ReoXD2BvZQSe2wSlmapEBZLK_91oakgreY-uS5xVlUwAWFho03ii_yzOoVUdTea9uWgVFSBhm-43I6A0e8t7e2Ngsy883Au1K1tiZviR6PkQd3xLAwJULKqfVqKDoGaeLTsrJ8YS6SsDVpNsaGz7b31KnT48N4uvKMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c77f3062d2.mp4?token=LvZ-gZIoHui-jXReznjgGymXIryQWiGMfRkgeEYjH86kH1n6KLx0rZaBroTId9h58AhXOjYYILeaIIar2u56fmgcsj8VUfVO7yQNwbMxBR7wasC1Nt_4Ag5eSuuo3EE3FfDC_SISRGKi6uW6cM_-XlYwgadzayF_ZEIbGRHkfDfYQ5ugz14ReoXD2BvZQSe2wSlmapEBZLK_91oakgreY-uS5xVlUwAWFho03ii_yzOoVUdTea9uWgVFSBhm-43I6A0e8t7e2Ngsy883Au1K1tiZviR6PkQd3xLAwJULKqfVqKDoGaeLTsrJ8YS6SsDVpNsaGz7b31KnT48N4uvKMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام اژه‌ای به رهبر انقلاب: خود را ملزم به اجرای فرامین واجب‌الاتباع حضرت‌عالی می‌دانیم
🔹
رئیس قوه‌قضائيه در پیامی به رهبر انقلاب نوشت: برگزاری مراسمات مربوط به هفته قوه‌قضائیه آراسته و مزین شد به پیام نورانی و هدایت‌گر حضرت مستطاب‌عالی و فرامین لازم‌الاتباع…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445453" target="_blank">📅 15:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445452">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dea0f6b74.mp4?token=trWWBKxqzYRCmt3clg3bEiRKwb9hNgjB9dtydnvUw2xyMNaLkXCVLksHODPOd4hK28NN8xNU7H7j6tcdwePozlh5WHYDtTqZvciN5nlfCB0sUpkjjX_F3gKP1JlqQsZp--KNsypFcGJNPgqGHLTdjhkkOIIxFwkqKHQbOGgPR1uefpKlWDf1psOnVf9Q9SpDaoz2A3NsNivDWZRY_NWjT5oSF96vJJQKd-DBF-OIXIgottTreh_t6OJ2zSoi0m6XEW0K7qpLNom8q6qqcPRW7D1dfYVrbzkqgsB4ZqC_PP38Mh3rvTHXI29ccrUzxoVnWAWHkzZHqNwUd1mEJPE3NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dea0f6b74.mp4?token=trWWBKxqzYRCmt3clg3bEiRKwb9hNgjB9dtydnvUw2xyMNaLkXCVLksHODPOd4hK28NN8xNU7H7j6tcdwePozlh5WHYDtTqZvciN5nlfCB0sUpkjjX_F3gKP1JlqQsZp--KNsypFcGJNPgqGHLTdjhkkOIIxFwkqKHQbOGgPR1uefpKlWDf1psOnVf9Q9SpDaoz2A3NsNivDWZRY_NWjT5oSF96vJJQKd-DBF-OIXIgottTreh_t6OJ2zSoi0m6XEW0K7qpLNom8q6qqcPRW7D1dfYVrbzkqgsB4ZqC_PP38Mh3rvTHXI29ccrUzxoVnWAWHkzZHqNwUd1mEJPE3NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کولیوند: در اطراف چند مرکز درمانی که بوق زدن هم ممنوع است، ۳۶ بمب سنگرشکن زدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/445452" target="_blank">📅 15:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445451">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ea32e5961.mp4?token=i3LaROKsmsi0iqttZ_iB5for8-jJuHDYuxF5T3RKccdLqcZ_n7Uqzz8cshKnf8dawIU7A2tEz1evolZvdmejtVzgCqwmspPqp9vq3FBfNgfbUGYO_Sqqn2CAKxQGXg49fz76kgrVlgDPIxZohQzdkTNYso2UFXQuBO68HUnG9qM0Vqjrtdh_OVxLw6wHIn87c1igtJce4XLtYN2FvuBXUGabgRC9EY1Jfo8a1c37fqiXdk0vWp2kVOxQOzG6wHlJVBcc-CFtzKK_0Z5jc3vKKcJt7DzlfUR_kYceJxPQxQx0qBrO_y7YbS8f6CmdJjoyL16FF5nHheYKruF-oIS7gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ea32e5961.mp4?token=i3LaROKsmsi0iqttZ_iB5for8-jJuHDYuxF5T3RKccdLqcZ_n7Uqzz8cshKnf8dawIU7A2tEz1evolZvdmejtVzgCqwmspPqp9vq3FBfNgfbUGYO_Sqqn2CAKxQGXg49fz76kgrVlgDPIxZohQzdkTNYso2UFXQuBO68HUnG9qM0Vqjrtdh_OVxLw6wHIn87c1igtJce4XLtYN2FvuBXUGabgRC9EY1Jfo8a1c37fqiXdk0vWp2kVOxQOzG6wHlJVBcc-CFtzKK_0Z5jc3vKKcJt7DzlfUR_kYceJxPQxQx0qBrO_y7YbS8f6CmdJjoyL16FF5nHheYKruF-oIS7gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود دستهٔ عزاداری قبیلهٔ بنی‌اسد به حرم امام حسین(ع)
🔸
طایفهٔ بنی‌اسد یکی از قبایل اطراف کربلا بود که ۳ روز پس از واقعهٔ عاشورا با راهنمایی و حضور امام سجاد(ع)، پیکرهای امام حسین(ع) و یارانش را به‌خاک سپردند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445451" target="_blank">📅 15:10 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445450">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7baaf678ea.mp4?token=WhrQtUHTDirUfsTph2sCElonjVTUvTXhdXeh3URbuIj8ro4e1fraVJTg1Hp3Zt5J42c2lEZY4KEHk_v4arDYKq6QfwF7CbwFJZ1oO-0m870xRpBCWX2YOL5anXmer5nTLXYMYJDD4kuEno10lFYEtZZR_kkGTihFRQ6cyYyq-ZozSbAB2CEPIcs-WyjhF_mshAK1MwCa9d7z6sxchpZJSMpHbqvRAT8I36baTlBlYVIKaJ7jgr--1hGH87e_G-jl4OCLxVgcRJv65iGHxJozEDxYclZ6QGCjGh6e-vkfJlUZ9cH5T2hWj7l2ZFtjov3CHTf3PhofOZtnDHYNxbdqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7baaf678ea.mp4?token=WhrQtUHTDirUfsTph2sCElonjVTUvTXhdXeh3URbuIj8ro4e1fraVJTg1Hp3Zt5J42c2lEZY4KEHk_v4arDYKq6QfwF7CbwFJZ1oO-0m870xRpBCWX2YOL5anXmer5nTLXYMYJDD4kuEno10lFYEtZZR_kkGTihFRQ6cyYyq-ZozSbAB2CEPIcs-WyjhF_mshAK1MwCa9d7z6sxchpZJSMpHbqvRAT8I36baTlBlYVIKaJ7jgr--1hGH87e_G-jl4OCLxVgcRJv65iGHxJozEDxYclZ6QGCjGh6e-vkfJlUZ9cH5T2hWj7l2ZFtjov3CHTf3PhofOZtnDHYNxbdqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جنگنده‌های اسرائیلی در جنوب لبنان، بالن‌های حرارتی پرتاب کردند
🔹
منابع لبنانی خبر دادند جنگنده‌های اسرائیلی در ارتفاع پایین در جنوب لبنان پرواز می‌کنند و در مناطق جنوب این کشور بالن‌های حرارتی پرتاب می‌کنند.
🔹
بالن حرارتی نوعی سلاح مدرن است که در زمینه‌های نظامی به‌منظور ایجاد آتش‌سوزی و تخریب استفاده می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/farsna/445450" target="_blank">📅 15:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445449">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd4d55793.mp4?token=CnuHtL8xz8XzdVlrTSr1Tu7Nmx4uOhjf8j08UT31bq22b_UGAQBuc-D0ShXyYJNfuwl1469KKc6iA9mihAKWk2EGZA3KIC24Bj4q7yCGjyguoEKytzue4RdgkIM2AphjWWU52qixMcxAb428qFHLpDyCJvqf_M5RKR1mKktBWhfdPoQUjY-mUnFPJy-585qKxpnR2vZtcfM_8-Ll33PktoOPsd4xP_vavR-Fii4h4uLKGMbFV9UzFlXQWUpMZVEwIezuj4MwMVqIhv6vR5CA_rOXdDalytTVboz4hNI2fCGO3yqmzZBdKoLUnLzsE0JgAnoz7kOGcLXsylyqT2ffPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd4d55793.mp4?token=CnuHtL8xz8XzdVlrTSr1Tu7Nmx4uOhjf8j08UT31bq22b_UGAQBuc-D0ShXyYJNfuwl1469KKc6iA9mihAKWk2EGZA3KIC24Bj4q7yCGjyguoEKytzue4RdgkIM2AphjWWU52qixMcxAb428qFHLpDyCJvqf_M5RKR1mKktBWhfdPoQUjY-mUnFPJy-585qKxpnR2vZtcfM_8-Ll33PktoOPsd4xP_vavR-Fii4h4uLKGMbFV9UzFlXQWUpMZVEwIezuj4MwMVqIhv6vR5CA_rOXdDalytTVboz4hNI2fCGO3yqmzZBdKoLUnLzsE0JgAnoz7kOGcLXsylyqT2ffPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اردوغان: کشور مستقل فلسطین باید تشکیل شود
🔹
رئیس جمهور ترکیه امروز گفت که ریشه اصلی تنش‌ها در غرب آسیا، مسئله فلسطین است و تا زمانی که اشغالگری ادامه داشته باشد، صلح پایدار محقق نمی‌شود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/445449" target="_blank">📅 15:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445448">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNuHHSshby0pNqhApjPoLGyG1lYvzJvuw2oAKAYWjWiqn-IRjbbF2vR6T9MyripsHg8jIkzQF-XpyVrnE3bo0jAMbMVpH3T44TmVUkz3O8H2y_UrdpkAd7WJYib4By6gQ96vcP889OxAoF2bwE7Z0QWXSS9PyXTEZcJKWlwx-ExOwinRNYbebWUVgJW2LjkMtEJ8C5ohrcwy0asBUlLIXR8rG6EwuggpQ2VKHc0hK--1NqmBWjXXoDxDou5Bo5ASVRRCpY6bMAuAVIgO5NtkLASG6e3psAxQz4UYVnIz_OipbavKwZUReLTfezVqd6dtAFuhvgBedV_nbT2JmM6HPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوالات خود درباره مراسم تشییع را از این شماره‌ها بپرسید
🔹
مرکز پاسخگویی ملی «ستاد بدرقه» با هدف ارائهٔ خدمات اطلاع‌رسانی و پاسخگویی به پرسش‌های مردم دربارهٔ مراسم وداع، تشییع و تدفین امام شهید انقلاب راه‌اندازی شد.
🔹
مشترکان همراه‌اول می‌توانند از طریق شماره ۹۹۹۲ و مشترکان سایر اپراتورها از طریق شمارهٔ ۰۹۱۲۹۹۹۹۲ با این مرکز تماس بگیرند و اطلاعات خود دربارهٔ مراسم در شهرهای تهران، مشهد و قم را دریافت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445448" target="_blank">📅 14:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445447">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34092159b.mp4?token=uKf4yvAUFakciD_P7Lc8U-xLM-3nJ7r_S5n-wRekjQRsClMkjmY2ZLynDaSf9fTLsFefztzJrl4d-hiTLeqcf8nn3By8BHv4cbczgojb36BtLx2v2rx0SmuXHYqM-FtLyM7wZD_VTGxj5zR3-IqKji0QmI1njuw06srQK1UgB-j4NdsQidEWW1oIcxL5RVmNN2iXyON-xNYVl-Oo1aZPzCzGCfFCF1s1pOWT4yhWOny03S8ViTRhg6wDlu4TTsQvEPAWpxdfZqN3g--CSX1-AWvAPCyB5ZSV4sJx9U4pJs2iG2lCt4bg_NEJ4Pvb-WrUR1vROmi9Q98S6EZdKExl_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34092159b.mp4?token=uKf4yvAUFakciD_P7Lc8U-xLM-3nJ7r_S5n-wRekjQRsClMkjmY2ZLynDaSf9fTLsFefztzJrl4d-hiTLeqcf8nn3By8BHv4cbczgojb36BtLx2v2rx0SmuXHYqM-FtLyM7wZD_VTGxj5zR3-IqKji0QmI1njuw06srQK1UgB-j4NdsQidEWW1oIcxL5RVmNN2iXyON-xNYVl-Oo1aZPzCzGCfFCF1s1pOWT4yhWOny03S8ViTRhg6wDlu4TTsQvEPAWpxdfZqN3g--CSX1-AWvAPCyB5ZSV4sJx9U4pJs2iG2lCt4bg_NEJ4Pvb-WrUR1vROmi9Q98S6EZdKExl_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
متقاضیان عبور از مسیر تعیین‌شدهٔ ایران در تنگهٔ هرمز همچنان روبه افزایش است
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445447" target="_blank">📅 14:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445446">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">مسافران کاراته به ناگویا مشخص شدند
🔹
اسامی ملی‌پوشان اعزامی در دو بخش مردان و زنان برای حضور در بازی‌های آسیایی ناگویا را اعلام شد.
📰
بخش مردان:
🔹
مرتضی نعمتی در وزن ۷۵- کیلوگرم
🔹
علی‌ اصغر آسیابری در وزن ۸۴- کیلوگرم
🔹
محمود نعمتی در وزن ۸۴+ کیلوگرم
📰
بخش زنان:
🔸
فاطمه‌ زهرا سعیدآبادی در وزن ۵۵- کیلوگرم
🔸
آتوسا گلشادنژاد در وزن ۶۸- کیلوگرم
🔸
فاطمه صادقی در کاتای انفرادی
🔸
فاطمه صادقی، زینب ‌السادات حسینی و سپیده امینی در کاتای تیمی نمایندگان ایران هستند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445446" target="_blank">📅 14:42 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
