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
<img src="https://cdn4.telesco.pe/file/H9Ahly5Wc1DSwAFNpKHCakUUdubgpiEP12LWYJhN2XKCg6hzHkmahxrLCyp6mpp72K5IUdQFS0GMJHmNsFLDyVdFYmAsMfR_2J19TscXGg7v9sT-J2JVG16KraT-Fv1GMriWm_rmvOFeOwCVdJjy2yL7MzNcIrLcnPIzwg6pQdq_xvilZkc56SPIpgkzqQATE0HVcuyZ670vPAHJNxLhMhvzUZBgpx8AXe0AP-vc9OFlfrvmX9IKPB4BDQA-QRyr3HcCS3aPl8neAvq_9q7kclzFKCM4mWvJ-Nv8gNpf840FSQ1a_ewNWJbQ3MnyXoEO22CVEAGmUnuBIYbf6Qj-Qw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 20:54:24</div>
<hr>

<div class="tg-post" id="msg-439705">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA-i7csaV88WwZIw2hRFu60v3-HcDPszmjKu0xDVwoFZXYzSRuUU6xaYpuov4hJ0UmTUiRjepAd7p9nZLPnIYLD1R2de3RNVcK1F_LMW8NVPSMbaCNbiDfnvVxC7DzA36543s9Bmnq0-SqfcLg8xqT4OxDiGJ2dZXf8mTodjgkxciIxRe_jI-jztYP3yEpcftxD8wY35GERkAuxboCq_PPzqudhVz0hVNSFeo0WO5JbgCWwpXWbPABjvO4jFP8bh3nlJG4GHPeb0KM5-OXGYSj3jMCj1SAYAsbK5qcVGth6TITzBuul35_5RYXUacke4u7NHS6BV8anagNihTto9BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان رفیعی با پرسپولیس تمام شد
🔴
با پایان یافتن رقابت‌های فصل جاری لیگ برتر، قرارداد سروش رفیعی هافبک تیم فوتبال پرسپولیس نیز به اتمام رسید.
🔴
پیگیری‌های خبرنگار فارس نشان می‌دهد مسئولان باشگاه پرسپولیس در شرایط فعلی تمایلی برای ادامه همکاری با این بازیکن ندارند و به همین دلیل مذاکراتی برای تمدید قرارداد او در دستور کار قرار نگرفته است.
🔴
در صورتی که اتفاق خاصی رخ ندهد، رفیعی پس از چند فصل حضور در پرسپولیس به همکاری خود با این باشگاه پایان خواهد داد؛ اتفاقی که می‌تواند یکی از جدایی‌های قابل توجه سرخپوشان در نقل‌وانتقالات تابستانی باشد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 333 · <a href="https://t.me/farsna/439705" target="_blank">📅 20:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439704">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47bd2679fb.mp4?token=qrwNrKbX-dMCJe31BenhoXIeZE4QUcXroVd0hbb-3wdV7rwZskPHe05UunXFuZUlKcTG7wuR7-xiy5BZMx4_YfjHssmLLy7WOAv5fS75ppP0AcsnCNTV5hIQIn_EYtZC_5sJkVKLP4-nKA5Vuhvj2fN_rNSKhw3YADTwQFH75ynmOg2RgKlF-WcGPQbpJnYMLe9PelHrXbojp9GAYSbJR7Upyv_yEHD6debliO_BvSoH_fljauiCzNnCML-hIi7oHtFbQ7aEl8nw0ckx-PP5ihT7zsXaaIrZ9z5vi_mnTbZwcxdQ0jVSqirv_wc9Okr6El067BwdCLIhWDuyqRVA0CoyKAgHKTEHqOO9AVdHc06fVVQryzRnUAEQV4JGUWck35rjiNkYGyGg4Aa3wCLFoaLaO29fqWXu6fsJYyZYigbfh85PGEKqw3iTc6e_F5n9e5TyL05OGzOof4c52kILOVeEhrxR712tVo81wC7B-aMt3IaGlAmumaGzjiRnY-F7O80g8OXe8ydTWN93xJDTBrUXw6N6s7BhBIPMdwvnbQbJD9_CNp04JRJ1JKuNZz2ABVTJJ0VLeVMGR3CD_lGs844z_SotRGzSCzDRBmNDwfQ2bu4LlFbd0Yb-KQTt3V2aXuWBFCKw7TUv9g3Yd62j1zOrVfwDhLrYTzwKcL4rZtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47bd2679fb.mp4?token=qrwNrKbX-dMCJe31BenhoXIeZE4QUcXroVd0hbb-3wdV7rwZskPHe05UunXFuZUlKcTG7wuR7-xiy5BZMx4_YfjHssmLLy7WOAv5fS75ppP0AcsnCNTV5hIQIn_EYtZC_5sJkVKLP4-nKA5Vuhvj2fN_rNSKhw3YADTwQFH75ynmOg2RgKlF-WcGPQbpJnYMLe9PelHrXbojp9GAYSbJR7Upyv_yEHD6debliO_BvSoH_fljauiCzNnCML-hIi7oHtFbQ7aEl8nw0ckx-PP5ihT7zsXaaIrZ9z5vi_mnTbZwcxdQ0jVSqirv_wc9Okr6El067BwdCLIhWDuyqRVA0CoyKAgHKTEHqOO9AVdHc06fVVQryzRnUAEQV4JGUWck35rjiNkYGyGg4Aa3wCLFoaLaO29fqWXu6fsJYyZYigbfh85PGEKqw3iTc6e_F5n9e5TyL05OGzOof4c52kILOVeEhrxR712tVo81wC7B-aMt3IaGlAmumaGzjiRnY-F7O80g8OXe8ydTWN93xJDTBrUXw6N6s7BhBIPMdwvnbQbJD9_CNp04JRJ1JKuNZz2ABVTJJ0VLeVMGR3CD_lGs844z_SotRGzSCzDRBmNDwfQ2bu4LlFbd0Yb-KQTt3V2aXuWBFCKw7TUv9g3Yd62j1zOrVfwDhLrYTzwKcL4rZtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور حیدری مردم در شرق  بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/farsna/439704" target="_blank">📅 20:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439703">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a467ccdd67.mp4?token=oeFiXuz6iwu9eCOKloG02qjUrkakySBrimtw1lLIFmZfW1x1fgWDbYMbgBnMKqwotT1rD_MlGVltiPmNwaGPWuewz_IwgHqGRyD9DYvuQ153jyx0zlzcRsdwxC9NqDCYOxjpMRH9RZg1K9SL_pvIDJrZF_p885X3GbRI5KXoB7fUFqoLJ8C3FrULOCkwHJXuigIu4Rj-rskl4ooQxTp1IAVncBITFRKaW5nDBSJvNw3MN1rDPfnOs1VFLnHyJ7EfitS9QFvVHRVzAsf2A6LyPDhuFVL8LVhcuOVIFa_l5LIg6yIb78lpX8iaREfhIDW7ehtoLkrkm8Skt9va-w49gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a467ccdd67.mp4?token=oeFiXuz6iwu9eCOKloG02qjUrkakySBrimtw1lLIFmZfW1x1fgWDbYMbgBnMKqwotT1rD_MlGVltiPmNwaGPWuewz_IwgHqGRyD9DYvuQ153jyx0zlzcRsdwxC9NqDCYOxjpMRH9RZg1K9SL_pvIDJrZF_p885X3GbRI5KXoB7fUFqoLJ8C3FrULOCkwHJXuigIu4Rj-rskl4ooQxTp1IAVncBITFRKaW5nDBSJvNw3MN1rDPfnOs1VFLnHyJ7EfitS9QFvVHRVzAsf2A6LyPDhuFVL8LVhcuOVIFa_l5LIg6yIb78lpX8iaREfhIDW7ehtoLkrkm8Skt9va-w49gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خلیج فارس وارد مرحلهٔ جدید شد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/farsna/439703" target="_blank">📅 20:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439702">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎥
آغاز «خیابان انقلاب» از امشب
🔹
برنامهٔ اینترنتی خیابان انقلاب از امشب، ۱۳ خرداد، به مدت ۱۰ شب ساعت ۲۲:۳۰ روی سکوهای فضای مجازی پخش می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/farsna/439702" target="_blank">📅 20:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439701">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrk7DPG3j5X-LQ3RUmBrP1huHd2vxdt3rtOAhg_9rYW_VIwKbXG4zDVmlw4bBoAIyW1Mj_42E_0MwPnNEeULcWA9RjwYDXAYQ_nM0L4udEaiaRk0OTSbJozz7KNns4P-g8W8urln5bY8RAJknETdPBIvXnLg5xFGvDb6Q6BFdfPV2QU1_-xAt-30CuPQEhXeni7t2--OY9L2n7ALx71DjtM9df74j_NUOMviflJ_78Cn5KRHNpkU10VQsSpfSjeP3jHe0R0R4fiEhg8yyV17JOzYMzszlMXf3GleSYpeQBpD8DhrUwoAW44chi9LdB7xGCrQ761kBbWQJsdFHYrbiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
از اجتماع بزرگ غدیری ها در میدان امام حسین(ع) جا نمونید
📌
اجتماع بزرگ «ایران؛ ذوالفقار علی»
🇮🇷
👥
با اجرای:
مژده خنجری و آرش رضوانی
👤
سخنران:
حجت‌الاسلام مهدی طباخیان
💬
با نوای مداحان اهل‌بیت:
حاج محمد کریمی، حاج عبدالرضا هلالی، کربلایی محمد اسداللهی، کربلایی امین مقدم، کربلایی امیر برومند، کربلایی محمدرضا نوشه‌ور، کربلایی حسین ایزدخواه
📝
با هنرمندی خوانندگان:
زانکو، احسان یاسین، مجال، شروین معینی و سبطین غلامحسین (خواننده پاکستانی)
🔢
وعده دیدار ما:
پنجشنبه ۱۴ خردادماه (روز عید غدیر)
از ساعت ۱۵ لغایت ۲۲
👀
میدان آئینی امام حسین (ع)
@Farsna</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/farsna/439701" target="_blank">📅 20:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439700">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrvN1-7TxlaaxCtpBxhqZkoUPnyW_xj2DjYv_0WMom_IotJwME2P2pX4BMgixpwcN0nGF3p2YpIc-PT9mr8gDhoY1byrDo5dELrQXHPjTt_-dw4fUcW7zAH0rQV4geG85Lgr281IinjdIcdXMT_7Ywnx7GACqKuzOUkR-0yn6aJ49Har3-0wDcOhnJ8m4dUZCYZTNBi1KNRZs2O9hNm0paDV2Znc66CAowKlJXs0Wag38-nR2PckE25nQUlMS5_p7rM0m-MVax8rGZZw2Jo9l-Can_v68OY33vQNJoSulbPWRHIa4sKusmPVwQm88gCXIIObo3-6xOEsJrl7KhixMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
تسهیلات ۱۰۰ میلیون تومانی غیرحضوری در طرح افق۲ بانک رفاه کارگران
🔹
بانک رفاه کارگران با هدف تسهیل دسترسی مشتریان به تسهیلات قرض‌الحسنه و توسعه خدمات غیرحضوری، طرح «افق ۲» را ویژه اشخاص حقیقی از طریق سامانه فرارفاه ارائه کرده است.
🔹
در قالب این طرح، متقاضیان می‌توانند با افتتاح حساب قرض‌الحسنه و ایجاد میانگین حساب، بدون مراجعه به شعبه و به‌صورت کاملاً غیرحضوری، تسهیلاتی بین ۱۰ تا ۱۰۰ میلیون تومان دریافت کنند.
🔹
مبنای پرداخت تسهیلات در این طرح، میانگین حساب مشتریان است و متقاضیان می‌توانند میانگین حساب دوماهه خود را از طریق سامانه فرارفاه مشاهده کنند.
🔹
این تسهیلات با کارمزد ۴ درصد و بازپرداخت ۱۲ ماهه پرداخت می‌شود و تمامی مراحل از افتتاح حساب، ثبت درخواست، پیگیری و پرداخت تسهیلات به‌صورت آنلاین انجام می‌شود.
@Refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/farsna/439700" target="_blank">📅 20:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439699">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/farsna/439699" target="_blank">📅 20:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439698">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74d018121.mp4?token=Ah_6U8-jMoG6z9DyN27d-uQyUpjYYz9eDKDto9uQOyAoKjJgBR47U5qfPGD_zAhRjMQH5jXYRKmugsHUM2KoeUDolvzCEnO9ioRM_BudH2DLhq7qr8Ap11Gd4_kh2MiWyuaqGcLb_F8ns9jmXCndGU2s3dVY77ur58cs2IgM9N1i746yI2zCneK2JMRz7S1Mn_R1ecGFelSlJWyDVkB7HekMpinaSRr7ayKihEQJJFlk9ECBuIhHZ1GuS4zp83cXG_-vKVUbdHgqmjc4kwAdfhi99hXEXVupQG92hYF4M9GHX6F4JtRWAtSiEkzjfYGUotmw4B3r9DI5Eap0viWRag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74d018121.mp4?token=Ah_6U8-jMoG6z9DyN27d-uQyUpjYYz9eDKDto9uQOyAoKjJgBR47U5qfPGD_zAhRjMQH5jXYRKmugsHUM2KoeUDolvzCEnO9ioRM_BudH2DLhq7qr8Ap11Gd4_kh2MiWyuaqGcLb_F8ns9jmXCndGU2s3dVY77ur58cs2IgM9N1i746yI2zCneK2JMRz7S1Mn_R1ecGFelSlJWyDVkB7HekMpinaSRr7ayKihEQJJFlk9ECBuIhHZ1GuS4zp83cXG_-vKVUbdHgqmjc4kwAdfhi99hXEXVupQG92hYF4M9GHX6F4JtRWAtSiEkzjfYGUotmw4B3r9DI5Eap0viWRag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توافق واقعاً برای ترامپ مهم است یا نه؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/farsna/439698" target="_blank">📅 20:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439695">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QVw6dxC0pbBo6fHEWNFB8jhrB7Qyn4JbExGeyQCuOBN4hrk0Uxytstq95gSiHJnG0_JWysjn_D0f3E0fFmbAJgZvD6YJru9FyPtyEuQGrwFEQh4HboSQktyfDgiAtGgo5WVjw7ZLApIhweIPrylK4TeVxs2dNe_yfHrRe5glZ0muqnUXx86l58A15dJqvDoAsMa2GL5MDCXJOZtTA48GSil0TMvSJySVKvl9As4Mm2ImSPC4nZsHxGp6PrYsQxH6g7WGbMLA5GOOO2lKdfp2KlWboF7p6CRBJKJdiSr7M4hMl-SgcmX-rCf8Whl6sDYcprCWVxUdCkK4Xx2OMVQuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XFLuV9d3XHTg7D-WJKDgozqBCNZfjfY0ZXU92ZwFu1w2WQaLzWV4u91J1fFOG1lgFq_o6SjFZjd1LJXzCgnmTiXTB8FRglwkqORr6mAKeVHT89a7YKnWsT3HBlFDfFET804crOJ29KNK8F7h3Pre_KWfszlCnr0fY6uNt2MzAgFzE4_RAnNB3v8g9IRSfdZ8VcfzvwZFmqMTC_M17FMDeiOsMakMDnawk2NQRsMxn3h9HEMGl3jGgxRcEb3nexjK_LfaMXDjDck7eBBBNgQjGcYcq1debIqvEcq8gfOhnxMNIpYij9NfXOP_UlithqVl1Xh8p0NXEGECEs_f6pp0dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG_cHpC9K3jHv7gcppU64SyGxwHBu8nR3jAzpKc6MEvLLaslCOiWD2Ba6z4uWo0c4ZQQBMHCVnem2zP663povJtpMUz49gYkpLnr9gRXHCbz1ihKq3xmuPoc5NmZS2opT9ajUh_OVRXjB5djqULP77aXb73pZLuYNaIQ6Z0WqhZHyC_7S1B3Fye7tn-yCQuuJVge80rt6L8Yc8U3oSH47VlCKuJX3P4-PBvMM43-JOvm-IPNXaRXsgMkXklWF7usQ8JzAptqVtIP2rJovTFgbDvDwa114S4r_YI6o6EVPSbxJkCFjh8lRwcIDgJK0d321xlPBehxINL9SxCseT83_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
نظر رهبر شهید انقلاب در مورد جشن ۱۰ کیلومتری غدیر چه بود
@Farsna</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/farsna/439695" target="_blank">📅 20:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439694">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌  قالیباف: میلیون‌ها سرباز مکتب خمینی در میدان و خیابان پاسدار آرمان‌های انقلاب هستند
🔹
اگرچه امام خمینی(ره) و امام خامنه‌ای شهید در ظاهر در میان ما حضور ندارند، اما راه آنان زنده است و میلیون‌ها سرباز این مکتب، در میدان دفاع از کشور، در خیابان ها، در عرصه…</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/farsna/439694" target="_blank">📅 20:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439693">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قالیباف: دوران تهدید بی‌هزینۀ ایران به پایان رسیده و هر تجاوزی با پاسخی پشیمان‌کننده مواجه خواهد شد
🔹
رئیس مجلس در پیامی به مناسبت ۱۴ خرداد: امام خمینی(ره) به ملت ایران آموخت که در برابر زورگویی و سلطه‌طلبی عقب‌نشینی نکند و امروز ملت ایران با الهام از همان…</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/farsna/439693" target="_blank">📅 20:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439692">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUZwX59FTqOlu2IkN7wC4XgIm80CGgrCCGjXVJREvxo4JlscgR4bCKc3iajb987MXQ-iN9dgnW7_UWVZPu_6x2oV0KChKeH37dQG7wNGcDXCf9khtURb2xRVB2sl6goEAIbzB1DuqG_k4o-jOvOawLG6bU5BqSb6eX40Ok3Dg-PZl4w7g5DyVYnLe_j9KE-eIEjpFAC1Q0nJzhuU1tiNBTTdCHJFbkURxxH9WmDmygt8CCuANO1-QMkwWbRVEmxHiaURBsbNjkNveSbWgkoluVVzHGErx5Zb-4MGXxJbbLk2BPesiU92vO_jS000WdY5oxd9RZsYDfMOEQze9_DzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگزاری آزمون ورودی در دبستان‌ها ممنوع است
🔹
آموزش‌وپرورش اعلام کرد برگزاری هرگونه آزمون ورودی و مصاحبه برای پذیرش دانش‌آموزان در دورۀ ابتدایی ممنوع است و این ممنوعیت شامل تمامی مدارس دولتی و غیردولتی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/439692" target="_blank">📅 20:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439691">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">قالیباف: دوران تهدید بی‌هزینۀ ایران به پایان رسیده و هر تجاوزی با پاسخی پشیمان‌کننده مواجه خواهد شد
🔹
رئیس مجلس در پیامی به مناسبت ۱۴ خرداد: امام خمینی(ره) به ملت ایران آموخت که در برابر زورگویی و سلطه‌طلبی عقب‌نشینی نکند و امروز ملت ایران با الهام از همان مکتب، در نبرد با آمریکا و رژیم صهیونیستی نشان داد که دوران تهدید بی‌هزینه ایران به پایان رسیده و هر تجاوزی با پاسخی قاطع، پشیمان‌کننده و متناسب مواجه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/farsna/439691" target="_blank">📅 20:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439690">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-DAFlVtfkxeyxJKF5afBrDPilEcLFROG-256I0BkGhD-FbJD19kX_Z7wUHm_ywXaLpWvHv7l6rRt1NyU0oqa0NmjY6cmppgM4fwmT0s4V_vSRPjJKxxkFHLHWy_Q_HSI5BcZFRcvn-hNyQ9Zx-huU9f4FucjgExJ8BXy77Kn-935IBGETH74_xN92p9iXVBbQnBxX9A5T9wagyuL7f00uCHH5tWBZ413LAmXo4ws7GrGKWrz9xznT0c6-17UAZ48PdAxOuFlCCvFnbOF_xFztquGFaG4mCn2nqF5dX762fMB5akOpHXPB9OnyJzizFG9WrpwcpGe2Cb1_DCr5Ad7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه سپاه به شبکهٔ انتقال تجهیزات تروریست‌های تجزیه‌طلب
🔹
قرارگاه حمزه سیدالشهدا(ع) از کشف و ضبط یک محموله بزرگ تجهیزات نظامی و جاسوسی متعلق به شبکه انتقال اقلام گروهک‌های تروریستی تجزیه‌طلب خبر داد.
🔹
در این عملیات اطلاعاتی، تجهیزات دید در شب، دوربین، بی‌سیم، دستگاه‌های فرستنده، لپ‌تاپ و تبلت‌های جاسوسی و دیگر تجهیزات مخابراتی و نظامی در یکی از روستاهای مرزی کشف و ضبط شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/439690" target="_blank">📅 19:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439689">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5rXx96VmWUQid_NmhZ-fDIfFhsqrlBnefYzmJdwWoxmoTi3I28cuCSqP5f7WqlSVMODUcYD89vnp31YQKlanueWYk8lVSWz9ulbKnlrcSXxfKeIbfxA-Wrguc5NJYQiAyvvlU1x5FK4BBHdOcUDiCDbKS44hq-MAMyFunvCPSb3SSORns6RKQrIhI8Ft2IROxulZLLoElxkW_HtGkiK85KRCzPT9lpiVPglBrImFCCPARXQS9l3-FG6SKyjoKHBCop4-lXHQHufYYMJ8WvJD-BG-QeNsq_vHrX9DvgKHPwYO_hlHyeDZP__I4UHzeZWOpi1wzY_lx1Urve-FMZaEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش «پاورقی» طبق روال ادامه دارد
🔹
نجفی، تهیه‌کننده و کارگردان برنامه «پاورقی» ضمن تکذیب شایعات خارج‌شدن برنامه از کنداکتور شبکۀ دو، به فارس گفت: طبق روال برنامه «پاورقی» پخش خواهد شد.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/439689" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439688">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_u6IAacDyQR7do3L6BDiJDkbcb_SIoUyvdvt80OnVuN91U_7KapYJw1Grvz452NazvhAeNdVgDhhOHZldSvNNbnvaTw-klang_TJenb_TlHRRv01A4ZCNcLpEksVLjsQ78R8NP2vYYZoSQNlheS-a6IUe8vI_hW63v_2IYpjntZ01gG8qDCvp1ThPoNOm52IdQmQiM3wE8P4A2dAnEh56n9ADsZSGfl4grWUZzCGgW5a7xdZ7jLFd88CFrzH1cmRDKhovbdoqzJaZQyU99TUUpefErHy1IQNVYxDwdbVKRJn0r2NqXhjLWCLKZaDxi4AwJJFfutPHbMToNvYrmDvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی: هرگونه اقدام خصمانه با پاسخی فوری و قاطع مواجه خواهد شد
🔹
نیروهای مسلح ما در حال انجام حملات دفاعی در چارچوب حق مشروع دفاع از خود علیه مکان‌هایی هستند که از آنجا به ایالات متحده اجازه داده می‌شود برای حمله به کشتیرانی غیرنظامی و نقض آتش‌بس استفاده کند.
🔹
آنچه با تحریم‌ها و جنگ نتوانستند به آن دست یابند، با جنگ بیشتر نیز به دست نخواهد آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/farsna/439688" target="_blank">📅 19:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439687">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اطلاعیۀ شماره ۱ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه
🔹
برنامه‌ریزی‌های لازم برای برگزاری باشکوه مراسم وداع، تشییع و تدفین امام مجاهد شهیدمان توسط دستگاه‌های مسئول و گروه‌های مردمی، درحال پیگیری است؛ لذا شایعات و برخی گمانه‌زنی‌های رسانه‌ای دربارۀ جزئیات این رویداد فاقد اعتبار است.
🔹
برنامه‌ها، اقدامات رسانه‌ای و جزئیات این رویداد عظیم در اطلاعیه‌های بعدی ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه اعلام خواهدشد.
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/439687" target="_blank">📅 19:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439686">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دستگیری ۱۲ برهم‌زنندۀ امنیت روانی مردم
🔹
پلیس تهران از شناسایی و دستگیری ۱۲ نفر خبر داد که با فعالیت‌های سازمان‌یافته در فضای مجازی درصدد برهم‌زدن آرامش روانی و امنیت عمومی جامعه بودند.
🔹
مرکز سایبری پلیس اطلاعات فاتب اعلام کرد این افراد در بسترهای مختلف مجازی اقدام به انتشار محتواهایی با هدف جنگ روانی، ایجاد یأس و ناامیدی، تحریک به هنجارشکنی، التهاب‌آفرینی در مراکز اقتصادی و حمایت از اقدامات علیه کشور می‌کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/439686" target="_blank">📅 19:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439685">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cec0d0cf2.mp4?token=HXIQXXE0OKfXSzXnntwbeCpyQ46TCeaWlBFrOP7Ah-2LC-kSELsI0c2gFTiOoRPrPCoe8f59jYl71RVnWQt3r-tYVHXh-IZ9N_NYlGwn0RM0BJTtsjdjNmz-PRemHjIbeqBI148E0hyvUmF0e0Yiyc9rTN-WVjmirFWpRtFLzKrdQygpwyHpEvyPOnXv8QvXK-NT9fs-ZgbnWlkThVjuYiI-as0xD0M0eT85-Np6aiI3n1v-Ij6hWP-jcJsRrw4um9-P6YSWEdXRbbv-MYKEDhBBSOhIMqeOxBAbSr_t7FDWsRERbj5o6CHL5MKMw4MF1Bevgw4AyAJdmypKz2CafQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cec0d0cf2.mp4?token=HXIQXXE0OKfXSzXnntwbeCpyQ46TCeaWlBFrOP7Ah-2LC-kSELsI0c2gFTiOoRPrPCoe8f59jYl71RVnWQt3r-tYVHXh-IZ9N_NYlGwn0RM0BJTtsjdjNmz-PRemHjIbeqBI148E0hyvUmF0e0Yiyc9rTN-WVjmirFWpRtFLzKrdQygpwyHpEvyPOnXv8QvXK-NT9fs-ZgbnWlkThVjuYiI-as0xD0M0eT85-Np6aiI3n1v-Ij6hWP-jcJsRrw4um9-P6YSWEdXRbbv-MYKEDhBBSOhIMqeOxBAbSr_t7FDWsRERbj5o6CHL5MKMw4MF1Bevgw4AyAJdmypKz2CafQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یا علی نام تو بردم نه غمی ماند و نه همّی
@Farsna</div>
<div class="tg-footer">👁️ 6.79K · <a href="https://t.me/farsna/439685" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439684">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMM4L9luaDu6UBWPo_Ghv0vElMWt14qMrr_OvEZnyfHrJV_6ob-nHttxYBwStlUVTZ8uARsKcl6kgQ6rUe02j9Bo23HLb5teC0Af83xPwQUBNulUs4lE5dw0PdZc8AQ5C2PwjJM1uQlEYbAvw-6i4_by6ONsw8rLrWCWef7OcAgZrJ3-_zimgfl-Dh4shL39nhir6esTLlC9u2-9LW5jVFqC1Ac-2EJ_P5ktecnYMzwMUvcJYPpknHjHS8iMquu5c3zWy6qpq96jzv9BgciXfoWd6KeJk6rm7FuGlNO_R4zkHWLP8o4tdsdpIcIKQMRVO9yXkuK0npTMatbnSfjhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۱۰۰ هزار تخم‌مرغ فاسد در شهرری
🔹
پلیس تهران از کشف بیش از ۱۰۰ هزار تخم‌مرغ فاسد در یک انبار غیرمجاز در یکی از روستاهای شهرری خبر داد.
🔹
این محموله‌ قرار بود با تغییر تاریخ مصرف و استفاده از برچسب‌‌های جعلی، به‌عنوان کالای تازه وارد بازار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/439684" target="_blank">📅 19:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439682">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa762543f8.mp4?token=tUDttBANCHA088dkE5s2vr_SOi1n-vOh9CHORAetcxP3A3NHgo2kfiFc1iTKT7V1F6HqOK0P7L9y0k_kuLybmd3DA_SlcBLbt-a52VUygAjoDlBBjb_U7I00FRLjzPag34fpNymDbr5fMYZTYluvZ-uveYvegeE148TKFy8A4rLXc9dQ0dPRDohQ_pWcUGpIIkk3f28gPqk-iWPdKo5LBscDm9TSZaSQ-cwUz0EnX3prWZWs38A3TIWbf_bFYqcyJNMyPp8s5NB4Uj1EkU5MqRXyqu6DfDd_BuSf6DPB4tIYfuOEy4rlK3Zd1LVlQlGx0grmMFS_Wv89YmDXzUBuPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa762543f8.mp4?token=tUDttBANCHA088dkE5s2vr_SOi1n-vOh9CHORAetcxP3A3NHgo2kfiFc1iTKT7V1F6HqOK0P7L9y0k_kuLybmd3DA_SlcBLbt-a52VUygAjoDlBBjb_U7I00FRLjzPag34fpNymDbr5fMYZTYluvZ-uveYvegeE148TKFy8A4rLXc9dQ0dPRDohQ_pWcUGpIIkk3f28gPqk-iWPdKo5LBscDm9TSZaSQ-cwUz0EnX3prWZWs38A3TIWbf_bFYqcyJNMyPp8s5NB4Uj1EkU5MqRXyqu6DfDd_BuSf6DPB4tIYfuOEy4rlK3Zd1LVlQlGx0grmMFS_Wv89YmDXzUBuPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ شکار شبانۀ پهپادهای انتحاری حزب‌الله در شهرهای الشقیف و زوطر در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/439682" target="_blank">📅 18:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439681">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K32NRaxrG5c3RJRmnAj0zn6Xzv43WOM81xnFebNNnbeNnwRE4hLehCcj_h5rT9quUC3z8wMdT_tdXKk-UfvoBOg91SGhVc0DWp5PbAQ7YmaDoD9hDMfxZ6J2leZ_lYSjgG8KtG3IPuhin9UMZQquYSvr9BW1XdEp1XGkVRFXMtXBZf-QsoxFEyvZxjZIyOjgUiG__De1UykAX16qKuQiaYLuqEWh-nNPSyQAGeGeaF-ey_0nV0Pi5Maz0V2qYjft8xCMsp3iJ2oH6hSNGJgrgMposKMe0eKUoT7b3eUP3wuqaX6aoLygkl-B6rtGWrju-Y0sh2rZdP1tz7Mcsl_8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمان‌ شارژ کالابرگ خرداد اعلام شد
🔸
رقم پایانی کد ملی ۰، ۱ و ۲:
از ۱۵ خرداد
🔸
رقم پایانی کد ملی ۳، ۴، ۵ و ۶:
از ۲۰ خرداد
🔸
رقم پایانی کد ملی ۷، ۸ و ۹:
از ۲۵ خرداد
@Fsrana
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/439681" target="_blank">📅 18:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439680">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7z2-bqSlzht-h2JVYep0jHTt_QzT47EdttB0AKtYEdPDo3LpBg6ZvzdWo9iFFJHvCLaR-TQZCxHh8JhbMw1wYaMurxPj8R9C-jE9dsaYOpgrN5waUVav6BF4OBTcFhbJoA-fPoEIzQ8Ffq2oE4PK418cOPPo_35nWx7yTciVxRG8n1SAgGGSvk_vd37jmClpbbsZwnc-o1ACKUUVdSnjx7ei-RsMXgzrKkCjnQzX4gWwJfPrAhkdSzVzNVeprG5QvnFA9lgi9sMtNy_15de8EwQ1zO-jaRZ5TZwGPqPfnv36Dx18nGJoen7sbhRIS7FeT-xrPUjJAXMdnTKMn9CYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
طرح ملی "کارافن" با حمایت بانک رفاه کارگران به بهره‌برداری رسید
🔹️
پروژه پیشخوان مهارت و طرح ملی «کارافن» با هدف توانمندسازی کسب‌وکارهای خانگی و توسعه مهارت‌آموزی، با حمایت بانک رفاه کارگران افتتاح شد.
🔹️
دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه کارگران در مراسم افتتاح این طرح که با حضور وزیر تعاون، کار و رفاه اجتماعی و معاون رئیس‌جمهور در امور زنان و خانواده برگزار شد، اظهار داشت: استانداردسازی آموزش‌های مهارتی در حوزه صنایع‌دستی و مشاغل خانگی و همچنین ایجاد بستر فروش محصولات این حوزه، از مهم‌ترین اهداف طرح ملی «کارافن» است.
🔹️
وی با اشاره به ظرفیت‌های بانک رفاه در تأمین مالی این طرح گفت: ابزارهایی نظیر «اوراق گام»، «برات الکترونیک» و سامانه زنجیره تأمین مالی تولید (SCF) می‌توانند نقش مؤثری در حمایت از فعالان این حوزه ایفا کنند.
🔹️
مدیرعامل بانک رفاه کارگران همچنین به «کارت رفاهی» متصل به اوراق گام اشاره کرد و افزود: این کارت تا سقف ۵۰۰ میلیون تومان با کارمزد ۵.۲۵ درصد برای متقاضیان صادر می‌شود و به‌زودی امکان خرید از فروشگاه‌های زنجیره‌ای کارافن نیز از طریق آن فراهم خواهد شد.
🔹️
دکتر للـه‌گانی با بیان اینکه تاکنون بیش از ۹۲ هزار کارت رفاهی توسط بانک رفاه صادر شده است، از آمادگی این بانک برای توسعه همکاری‌ها در راستای حمایت از کسب‌وکارهای خانگی و مشاغل مهارتی خبر داد.
🔹️
وی همچنین ظرفیت‌های پلتفرم خرید اعتباری «وایب»، سامانه «فرارفاه» برای ارائه تسهیلات غیرحضوری تا سقف ۱۰۰ میلیون تومان و سامانه «رفاه‌کار» برای فروش محصولات کسب‌وکارهای خانگی را از دیگر ابزارهای حمایتی بانک رفاه کارگران برشمرد.
🔹️
در پایان این مراسم، تفاهم‌نامه همکاری طرح مذکور به امضای دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه کارگران و مدیران عالی دستگاه‌های مشارکت‌کننده (سازمان آموزش فنی و حرفه‌ای، وزارت آموزش و پرورش، صدا و سیما، بانک توسعه تعاون و...) رسید.
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/farsna/439680" target="_blank">📅 18:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439679">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_LCmY69BJrSJP8pMGo4iphNW29tO1K9N9qXFqLazK2sL-wGiBBsfIY_vhiAAKGV3a3w4P-4RIBtrmjSjuHtbu08d34eh7FajqbnzAKEasnu8JDvLoV1y6VtffYG20ARbuJg_0JAz48RxK6zIrkyKSiDXdMdjjCyF22nRf7zpJHdy-kdM-a7dKe-VLYs4DKA-95BNGXAHbpKag3d8YaaAnDJaJb_zJLyVE3LdGPhwtIlf--pZEH3AhEcMe33F0ATNeIJGcaFkYN_SEMNbqTrhA0q4eeTCCTu6NdKz-XDapufPF5gPPeCIVs44jLny060qR1E3lhFSgsjUJPtT8NNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر فوری: کوچولوها مهمان ویژه پارک آبی اُپارک!
🚨
💦
فقط تا 15 خرداد!
📆
میتونید بلیت هدیه اُپارک مخصوص خردسالان رو دریافت کنید
😍
🎁
برای دریافت بلیت هدیه
روی لینک کلیک
کنید</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/439679" target="_blank">📅 18:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439678">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/439678" target="_blank">📅 18:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439673">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VW7P_xM6utltARRppqG4lOdfkV7_4DgHmdOL4CAnpcI3og28mRtB5Tsx7YhqPcdI0HMeqeM7E_Utn95qmoWkcLLVEa-DjYBGQA8mCoHzpsP0x0B-gSjeJcTrTh8P2ZT211sbD05pvS-RdNigfRXZoFNbeYmuEY9O4JvTK0xxEINP5P6LumoE1NTZ5c7RT2UXJ3sXcT01TG8Z6ullbjDdAdLDuc8RFFgiq5mfyX78TJN06hzYG13LvxIxE6uKP1YILvDc9NLnx2QT4IHzXSxSM4l9bBKVCEB8u_ZdawmUMEV6PmGNoMgTcRXR9UGQRyO4pjq50P2hJgh3yPHBTZbE4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8HyTuDSCBEBrmoh_T5XHu6Tj4gqaIE9fOEWhH6i45G6GmpeeW3TpmqyRkKWamu-yJShYlKhQRYULHKbhR6U9sc0oOjI0IiCoCQwvlkHAv1y9GTrtLQSxIM47kIxkxm0AQhxyxsyFSXgQ8OaGeD4NsIcG7Dvvn5oT-ROwOSCoXtz9SJng56Ym-dOB3c0zjWZsGXE92avkg9nkXUMh7TidUfy64hO6hKj7VEsWF3Guo34t1L_dykvy9vcQMRkSQH0--7wxRqesyJTeJ8zSmMqzZScNd6YzNCmRyrlV33uiNtHsUgqex4Xav_OWvkBbmnxz_nbfgYWoX-zFeKrK7SNsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oV7apylLbm_UCvH4FIOrURH5RLU1FVXs4ZXu4r0NBqQ5bnbXQi8klrjILG7nGbb6ANHqqPFtTr-vhY4WMF9MxByo95Owz-mQBCGg73QNEqGZNC_Qzzo4IxaYcdhU1uX5HGAJKw783kW5O-POmOfjOs6cNfEWakhFJQv86rVMVN3bOzwHJ17v1iaeVcdZUU_36dl8-UXrePimY-uxtrRupaQ-pc5jrK-cImu6xVlmMRkR7GdX0j8bsip_csSkXtn9s_xlvPSAYZUuXl3MNOFWnBeklemKfSXWEZXO5wk9V5PkuKyrJ7la_kSFNjJdN79qnqUYAun5J8xN5exV6Dyd1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbUQvn0cpDQFveLXhCVMPgcVBX7cHxmBtyL5-tFk7Q-YqPba0OPFQxhGuZlUa-32Wx7RsJ_7tnIqMj09intdb_9MTVFKEniXtddjmWfk2i7oCJKYmtAJ4v1kDQNs8koQn03P6Qq5zkmzZsoj7GwmjiXk9JdaFUocWCBtR8sNsETsWUSPZ37QyQ7RDPGO90KjWmpagjoVTseP4Q754DaMZx8uk1aEauGeLjuF6NqSJJ2YvgtPO-YWaRQycRDp2XLA0qIm2e0Oup9Hk-0op3-CxMehwTv82UCq0Wkfa7IHjz_vcI9kPfCiazUR41Ei_R3gNCKGYqcWq2YkqsLrIVp9wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcL1mqi1zw5uYYJrJtqPK5nP2-3Gw1gEV70k7dwJTet9mv7MPiwlCxzkrjn-LSKYPebW5HyGovVGDHewxjz0PEoQTae0gmU31yFq8fJbohOu_24PHzsu_olvSWL0eOngPR-woQNLLKmUY6ilovELYjHTu_1Sq_DFn_GBYHb3hdKL1_Lsl_a_uwnLYcosZ3Jmzo7kJbymG1A3dEgaDUvnSVMh811_UUCyygTdeRAYvxTgWFrjnA7ky1oPCW_9wE__Mc9BKilZB3Rm16YvRVTx5jaB300FDL3WCVuTU2RaAWFIQJo1u3rY556t6QcvyW-h618ChlOrqrkFHK2Wqo3HTA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید سخنگوی شهرداری تهران از خبرگزاری فارس
عکس:
محمدمهدی دهقانی
@Fsrana</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/farsna/439673" target="_blank">📅 18:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439672">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgKwc4BxcTNaVXOgKmknqpuT314i-oUmiz2VvNrDYBYuXTx6IfcS1wGR35OjYp0FiE0IPpSTGdJZx3qewhYRWj5JJHl6QKlwAX7pVKw3kThnT0Wb_t0UGDQLNQhnPFWNXBDvLfK7I3Si06aqlaiO8SiObodS3HNwknTitGY22I443qVE-KEFCUlhogsU846hv-9DXvKR-MEwpbYNrJZp5BU8oTG3C-Hl6Y4JtAwvvavj3f_zdDDtQPAUr9b5KyktSUVZOk_RFf_HwiHmd_OMqzFWBB3nBCkTK47RfePClyTehd8sR-hATctj-MGh6Ohz51eh249AtsBiwTDLn1JmgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: من و ترامپ دربارۀ ایران هم‌نظریم.
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/439672" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439671">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8AAL19CabktcUJDwr71Wn7AqDsProCC2Z3ZArweIWvxR6EJWSG1zBnJAHk5h1BiZcBV84F_e3yYU9hqr7nJ_LLxm8i5rc0o2rkEDrSzoEUz-ynJtBFaZzOW29NkPsuoPbqtlEaJQozyXYqKkaMLr3dtkIIaSudQiW-pnzVJOnSI8UMrp-rcLiWfBxXY483fHTwJ5rKYq0-FWu5r6vNtg8kdWo4HaCTcC354W2472PgyWDCJ90PYprJPNPom2uCEGhQH5ntjGU9BetCm65XPMUI_Rg_hq5__WOxhu7r0ueu3h5mHQyfSkDFf3dpyXvA1I5w1tspsu-lY9O0rKAMNDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ نظامی انگلیسی در اثر سقوط بالگرد کشته شدند
🔹
سخنگوی نیروی دریایی انگلیس: ۳ عضو نیروی دریایی امروز در جریان سقوط بالگرد در یک تمرین آموزشی جان خود را از دست داده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/439671" target="_blank">📅 17:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439670">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبر خوب برای والدین شاغل؛ ثبت‌نام دانش‌آموز نزدیک محل کار هم ممکن شد
🔹
وزارت آموزش‌وپرورش در دستورالعمل جدید ثبت‌نام دانش‌آموزان اعلام کرد فرزندان والدین شاغل می‌توانند در مدرسه‌ای نزدیک محل کار پدر یا مادر ثبت‌نام شوند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/439670" target="_blank">📅 17:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439669">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌ حزب‌الله ‎۳ تانک ارتش اسرائیل را منهدم کرد
🔹
حزب‌الله: در شبانه‌روز گذشته ۳ تانک مرکاوا در منطقۀ «بالوع» مورد اصابت قرار گرفته و منهدم شدند. @Farsna</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/439669" target="_blank">📅 17:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439664">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCaVxXG8Z4C2VE2E4qfCGC1UadqMygYAKMH2dZINWBhQTZDKbvPy5KSNqAQRQcQLWeGfQmiHK927m5BatCI-LZNlXV5798tL6c4YhSgTNZ8Od6n3kikpEJkcYTa1d87QwRfMd5bTW7T8sc7JQ3ybTyv7tNKq1ON2S_ygQzp3eVjbPMMeanylIi5jnEjnFQXZNTY4yhYMSXli8ONtb1Xnr26vt8LSZFGx3uUUT2P2RqWrVl9f7Xlx5o0xVajDTjoxs1EhazF47SXIZbQrbXDSQ-MGcb7Dsv80obG8ws-gMP_KDNWp0sR6oRhAr9GsyshpBkSPO3QDqcuTH3gdchWogw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePu0AjMyD4Z-4BXBIC4XZHxxFGv-r68x2_4p66ZeeAPvAKhnWqLoHNVzWrJ6K2Mj-tNOgy7lWcRjBZDGaPLj-e4_I_rkxl2qoPIZkksg29OAKIGzl1Cf2xR1A1C1v77dmbh3uItJKDqxnWM-clsWPgoAuOxd5aGoyU1251dRxio6mrwYRbX5Jaz3wQFw3DGKzPNIUgnJdCSXSATyF7Gofn4e-yoV5Ku6At3Np4dE6RNbre8xSiqOIIbxfcCU-MlQgLcVXmcUY_U1XORK_P6M6s5jL733IW8qbqjBp2HbkJp2pJWksOiRWwCWOBxBtHrDDGpETtAmQr_yTtIidvENzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CT6JA7jZ9mYsrL_B23oEhjTEakMqpPfArlaaqo7btfu97js54_phuPlix08U3epttxhubxzRGc8vKjeMlQRplRKnKhV5ZagMvnz5zLWnWWtRfzNgdPeNH7Co8wBE3peh1zffmiPb6IXqZ-fJt0ydpBo9_7-P67S8z41qiROsuIJyBu4WufLO-88u_GYrgK9xyYntm5g3a70iARmLpZk3fp0HLfh_AY4488Z3q14n5tS9NeXlk45Kn-f1RqSQb1HOKFjEkRg_EvotaYOqGPqR072yFOZmZG1IhxchTFMOiIKZwuUCHQS9Z2Ug51SFR94vU5QY9DwMHJTNCohxPfFDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icQkJsO8QQqnhnp98mnOYIos4At4OiChLinDfkwl9GtJ6p3Qu9J_2z5zyDxQmHEtMo5d6fxbOEjg3th5Ow70Vfv0HvhzoH3F867j41CIN7-vDN5NG6xM_nOQnScDEt12cJZcvwvMoqCNfSwnG5khwVp51CrvFOFOE87kUkbwKWg2ByPlhtilmXgLqtxLjF-nOTlr2aLOPSTq2wnYM--0bgpbMpoheGEhGbI5Pod2Km0OIhE74l4Kxc5yzYLjQH0ZcMy3IxJD-gswRDg1LTbCccDa-XgHpz9AWp2D4z1vuTKlTvhiAD98FtDsv3J4fGTjJjWuslPkWxUDzGQvf8Zkjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J7lZFKHL-3oc41xuz_sNaz67oglxmN6hVhF2TgsWxDTAvq3FHzth_uizgdcGZFlnnAud0FUs5ib72H80VxyobYz53aSGm8NWp9bEATnqHAfQL-HF7FplUPQk9Gpaqw-CEvqw8y8Oz5ygdXCHTfyNDLxsR7uCrqrYHA67SdldwJGlDqD1-0WV_d9eed1nhePyRSKtX3EpCmQheiZrmenz16VfV3nSd7EEJtZpZvfUGL7Xr8HQC-CdNQF5p7UHUuWgzdLtzpNjBik7lxTe8HCyD0mraB58Y9tiRW9i6bIntSHBexx8CvbXAf1s8WM0pOpWPEsUffiRzIvxs03TY8WUbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قاب‌هایی از مهمانی ۱۰ کیلومتری سال‌های قبل
🔹
فردا عیدغدیر بزرگترین عید شیعه است. برای خلق زیباترین صحنه‌ها در پایتخت شیعه و در جریان بزرگ‌ترین مهمانی خانوادگی مسلمانان آماده بشوید.
🔹
همزمان در تمام شهرستان‌ها مهمانی‌های کیلومتری برگزار می‌شود و حتما دست پر بیایید تا در ثواب میزبانی در مهمونی ده کیلومتری شریک باشید.
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/439664" target="_blank">📅 17:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439663">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e31c543a50.mp4?token=vQmvq5BcTz1q9WO_JSMJTbE95W55w-GinaEg-YFfZYFiyWBOmieLKBFFbc8dSv1_jRh5sJtMesc8W4Dtp7x0n7G5MRF5HShhyPzhQqH0gOv-BOrLcFNMJd7ljDEUuunJOu1YUzbClmfeStpUv1TErFPR-5YnMg7walXkekOBw__S3i87VufBvRWn4b_toKUUEtdwhIFzhKjCItoAb2-zKrEcgO0m7FIzoX67U1NiDHsa6V3MmPi67lQiPg870AYA6n-mW8ZlO9MF1a7qD24RBzKQK4oKhKSCb4orMZfOtrND48CBNmy_ZF-qpQr49v8a26_4YzPF2I4THyAWlka1BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e31c543a50.mp4?token=vQmvq5BcTz1q9WO_JSMJTbE95W55w-GinaEg-YFfZYFiyWBOmieLKBFFbc8dSv1_jRh5sJtMesc8W4Dtp7x0n7G5MRF5HShhyPzhQqH0gOv-BOrLcFNMJd7ljDEUuunJOu1YUzbClmfeStpUv1TErFPR-5YnMg7walXkekOBw__S3i87VufBvRWn4b_toKUUEtdwhIFzhKjCItoAb2-zKrEcgO0m7FIzoX67U1NiDHsa6V3MmPi67lQiPg870AYA6n-mW8ZlO9MF1a7qD24RBzKQK4oKhKSCb4orMZfOtrND48CBNmy_ZF-qpQr49v8a26_4YzPF2I4THyAWlka1BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفیر سابق ایران در لبنان: نتانیاهو تلاش کرد با تهدید به حمله به بیروت در صحنۀ جنگ دگرگونی ایجاد کند اما تهدید ایران باعث عقب‌نشینی صهیونیست‌ها شد.
@Farspolitics</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/439663" target="_blank">📅 17:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439662">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCTz9ai0tFwfjbZOFDkBlBFrwNaNzpBdESRSK94ikNsm4bfx7R8Zg76qLpdW4VLOFLDJAbl1_THLIaXBimmjZaj6JBZWPRaeLc35OmWaocH0ffZQ9LqR5Q-g8P9u30FEH3ZsKIf68oO0bLOaTbKLMXt_x6r3fuFkqMKbcHFd4f39yiqx1eG4fbUQah5Vt5Qsw0TpGHsqeXCHX-RotwCEUQbU_J2kpg8QBnjC49Uc11Wgmo-CfSW8UDzIfYDCX9rbNMqDvq0vxp-ECyQ6u8prxuzilZFUGqYqtJBME50GhydvyOVRnJ-iBdZipW4rxDY3fc230yllzv648edRnN1igA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعتراف غرب به توان مدیریت محاصرهٔ ایران
🔹
شرکت رهیابی محموله‌های دریایی، تنکرترکرز می‌گوید: وضعیت ذخیره‌سازی نفت ایران بحرانی به نظر نمی‌رسد.
🔹
شبکهٔ خبری بلومبرگ ساعاتی پیش با استناد به تصاویر ماهواره‌ای نوشت که نفتکش‌هایی که در جزیرهٔ خارگ پهلو گرفته‌اند…</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/439662" target="_blank">📅 17:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439661">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">تصاویر آسیب‌های شدید ناشی از حملۀ ایران به پایگاه آمریکایی علی السالم و فرودگاه کویت  @Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/439661" target="_blank">📅 17:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439660">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5s5CgtYSLmparfn2aUCWPx7_Te3D-274O4R0xzLWEekNsGUvym1rts8Gv6orADjf_1gnzkfRQqVHEPivxRx4XODuxFw8b5-fAUFvc_4sqcaVEWJBsQKiintF-axPxJRg0f5GiSWWIcRV-4KYpVgxbaH5V6AVEsQqzXnSFZNe96-wYACXNi3pFVAmKOcwWr6xgo3VB_wr5vuzgkEOwpqy-0bXqsO-_6UN10nLszyqHu0I9-O5Z-tcRDMn-qydI-eGU9SIWespyponGnzK2CV7FPvXs3QZizgJuGC6NYyxDtFMSNwmL9la3TnnbUGfWcR2SG6M9eKlCMBLN7F8Hc7tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برپایی بزرگ‌ترین شهربازی دنیا در روز غدیر تهران
🔹
بزرگ‌ترین شهربازی دنیا در مهمانی ۱۰ کیلومتری روز غدیر برپا خواهد شد. برای درک ابعاد این رویداد نگاهی به بزرگ‌ترین شهربازی‌های جهان بیندازیم. مثلاً خیابان اصلی «مجیک کینگدام» در دیزنی‌ورلد حدود ۱.۵ کیلومتر طول دارد، درحالی‌که «مهمونی ۱۰ کیلومتری غدیر» بیش از ۶ برابر آن است.
🔹
حتی اگر مساحت پارک‌ «فراری ورلد» در ابوظبی (حدود ۲۰ هکتار) یا «پارک والت دیزنی» در پاریس (۵۶ هکتار) را مبنا قرار دهیم، این شهربازی خیابانی با درنظرگرفتن عرض حدود ۳۰ متر، مساحتی در حدود ۳۰ هکتار را پوشش می‌دهد که رقمی قابل قیاس با ده‌ها پارک معروف جهانی است.
🔹
علاوه بر این، ظرفیت پذیرش مخاطب در این شهربازی خیابانی به مراتب فراتر از استانداردهای جهانی است.
🔹
درحالی‌که پارک‌هایی مانند «لگولند» یا «یونیورسال استودیوز» به طور میانگین روزانه چند ده هزار بازدیدکننده دارند، «مهمانی ۱۰ کیلومتری غدیر» با ده‌ها قلعهٔ بادی بزرگ، استخرهای توپ غول‌پیکر و صدها غرفهٔ متنوع، به طور همزمان میزبان میلیون‌ها خانواده از سراسر تهران و شهرهای اطراف است.
@Farsna</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/farsna/439660" target="_blank">📅 16:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439656">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqN8x2uPcT-9Bi6DgJTs01yH7ZqLz_IDUfSyjV3bD60SDMua2UdDdqbNGUwNhSYCQ5AXceCUxHNhgyTnwq4pwSC9oGlZAt1iJaTazsr-WRzx0szKPyFpl12JVDWvN4Ec2zyVx6sbSgGcg9RvxDNj9PpVokFPbMSmYPCbxDGufqwyilmv_g1x6mwtPNwSmFnEHe-gYIEl6W553-5uzDIGxWtmcBoVtRJz026u5Y4bt20LRxG1cSJwjYSGnTsXeiQoH6kaW-a6-2zGzLUXL4F6ZvZDBUIed3H3hXRQ38OrgKMvS2z1e7PkBb11hwm8aCgBQh2aUceS9hQ30SEzHJ8t0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mblQanvtCYHfES9W-quDWIlEZ6_aw1yypEn3-uiV_GfwokKciJdFUvjCmZ0NWg2V3fv71DqAxiw77QBIPLLAjmSd7oKDMDnuK6_IGTmM3jRKA3nCXi1tSHzrzpbSYkBp8BtyxuvjHMoUT00QGEQrrdnzKcrc2QjQyGP1fUjE5VWDHuzzYajahOa7uH7EwtbGuwno7595e2et_32VB1UgLLi5A2dSFxk0U3oU8ot2qupGVYtK_I_NYXmoVvK3feLlBeNmb447I4YiFnwnZZFo4ptWRpchX_ANSrfl2BXRRCLQFGZPBSBkv0Pa0kE3wDaaYU13FGHtcx4ETnpjEaidNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d50b1bddf.mp4?token=RWa3I9xGk53_ILAfHLzRgWOw7khBUs9cM2Xs_eeUXRysr0EsV8LfPjQufZ5tzeQ19KkAEkwWrG5F1NbtfDT7UskxQX-KaGy_vOK3BaBHEIBSHpj6JDQlaSqavxzfevZCpTK9SjHlYzV8Avn97nvVFWYIxudJ2gPZVJjJmrPydB9d-vAN3m2fzfBzSgWtagZxCtvrnizEXdtOPY2kkdXcdYNjJrat9Qw7-RKaJuXCfiyOhmVtp32afnGIH6fpiVMT0meRCazydmcRN_Hgwn-ITJ-wStrqx4-hQa3zntK-PiiiGOw3ixcKOPlBGc-_Q_LV2qJb1yuhjBueosJSZXfArg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d50b1bddf.mp4?token=RWa3I9xGk53_ILAfHLzRgWOw7khBUs9cM2Xs_eeUXRysr0EsV8LfPjQufZ5tzeQ19KkAEkwWrG5F1NbtfDT7UskxQX-KaGy_vOK3BaBHEIBSHpj6JDQlaSqavxzfevZCpTK9SjHlYzV8Avn97nvVFWYIxudJ2gPZVJjJmrPydB9d-vAN3m2fzfBzSgWtagZxCtvrnizEXdtOPY2kkdXcdYNjJrat9Qw7-RKaJuXCfiyOhmVtp32afnGIH6fpiVMT0meRCazydmcRN_Hgwn-ITJ-wStrqx4-hQa3zntK-PiiiGOw3ixcKOPlBGc-_Q_LV2qJb1yuhjBueosJSZXfArg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
وزارت بهداشت کویت: درپی حملهٔ امروز ایران ۶۳ نفر مجروح شده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/439656" target="_blank">📅 16:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439655">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c4bedeed2.mp4?token=UWs_lPO2YcHeIhZX8j48Po6JwyRoo1Tz8r9EUcZesM2PgmVlPxfV_oMvxNKBr7qX3o6onB93vF7ZzoZo0_CIadoMmnbEXamj0wzIqdsB2x8MlB_fuVEPItM6-MWtyB7X9Ufo0MFZeUHYUP1zw4wiVWYOglRQF5IMi0v8D1-noiV6xkPaGbhI_JwBeZT0Wnis-g23nnyQcC7Xz1P4XuflmMKk7YHkcNrllQaSHcz5Z_lpOojp6hetWQYZwXFK8SrbzOJoqafRas0moyiZv3dTgcU_43nX98BpvFgUVD2mpNxTej5xhBUNRE1FTkjZWEZXm1Pwj6toE4sdWmiw3VOttA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c4bedeed2.mp4?token=UWs_lPO2YcHeIhZX8j48Po6JwyRoo1Tz8r9EUcZesM2PgmVlPxfV_oMvxNKBr7qX3o6onB93vF7ZzoZo0_CIadoMmnbEXamj0wzIqdsB2x8MlB_fuVEPItM6-MWtyB7X9Ufo0MFZeUHYUP1zw4wiVWYOglRQF5IMi0v8D1-noiV6xkPaGbhI_JwBeZT0Wnis-g23nnyQcC7Xz1P4XuflmMKk7YHkcNrllQaSHcz5Z_lpOojp6hetWQYZwXFK8SrbzOJoqafRas0moyiZv3dTgcU_43nX98BpvFgUVD2mpNxTej5xhBUNRE1FTkjZWEZXm1Pwj6toE4sdWmiw3VOttA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شیعیان اندونزی درحال تدارک برای پیوستن مهمانی کیلومتری غدیر با نام ali day festival هستند
🔹
امسال مهمانی کیلومتری غدیر همزمان با ایران و مهمانی غدیر تهران در ۳۰ نقطه جهان برگزار می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/439655" target="_blank">📅 16:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439654">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4141858b06.mp4?token=Gu23_YJyrpxs0Sy1ip66LAzLzgTEat49mMDkMdsddgvpZORH0tp_9fTstIDc4pFLh0iQLZNdKZtNk8g3mIXT69t6LD2MUVd2QYg3Qm3bShlor_6uBW3ZGHAzSNI-XoR0DT2OgxrRhDgML802I_F6MG8XFIMg6w8VJc5gataaW6K8LYlAJgwS7hpLCeE6fJT6jRwskWaIeufV-4ATTUtsT_eqHDA1xtW954hKwh0Xy4U0GiyWVOXk8tOBhfgwpqIn68KZScCiV7tkILHj0-mny_C7NohmuEjgmx5A1km6AfTJ1Ugzc_dE6pcbK35_0HftGJl2mVy7V68FvztL1cZAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4141858b06.mp4?token=Gu23_YJyrpxs0Sy1ip66LAzLzgTEat49mMDkMdsddgvpZORH0tp_9fTstIDc4pFLh0iQLZNdKZtNk8g3mIXT69t6LD2MUVd2QYg3Qm3bShlor_6uBW3ZGHAzSNI-XoR0DT2OgxrRhDgML802I_F6MG8XFIMg6w8VJc5gataaW6K8LYlAJgwS7hpLCeE6fJT6jRwskWaIeufV-4ATTUtsT_eqHDA1xtW954hKwh0Xy4U0GiyWVOXk8tOBhfgwpqIn68KZScCiV7tkILHj0-mny_C7NohmuEjgmx5A1km6AfTJ1Ugzc_dE6pcbK35_0HftGJl2mVy7V68FvztL1cZAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم امام علی(ع) برای جشن غدیر گل‌آرایی شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/439654" target="_blank">📅 16:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439653">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=H7gi-pNDBLXfvCnfERsWPwKe4Pywaf4h5hvb7kiqM9QXMXH52S5txAdat8CxrlbiA5gPGZL3uZTXneatXi_2z41GMCo3siyWmxqpw9cxWijNBmLtnWDsReCPvLmxTXwbHhjn8VL-k9LyxYkKVbyAVut8TdeQsVtJm45DuN-d-5CK9rO8VMk1ZMPkvYj9zmIK95XOOgAk64m18fvbcFZ4phWFOBGV2hovISZQcvxuq5hyJiZlj71AFL3n0h0gim2zHInR5LlzpA5DiK-AxghnAOkouCciOK3Vd20NZcRkK-TsbcoFjApaHMRn6pCNkXVRtSREvaOQcoftdir1vSUeVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5371cd0bb.mp4?token=H7gi-pNDBLXfvCnfERsWPwKe4Pywaf4h5hvb7kiqM9QXMXH52S5txAdat8CxrlbiA5gPGZL3uZTXneatXi_2z41GMCo3siyWmxqpw9cxWijNBmLtnWDsReCPvLmxTXwbHhjn8VL-k9LyxYkKVbyAVut8TdeQsVtJm45DuN-d-5CK9rO8VMk1ZMPkvYj9zmIK95XOOgAk64m18fvbcFZ4phWFOBGV2hovISZQcvxuq5hyJiZlj71AFL3n0h0gim2zHInR5LlzpA5DiK-AxghnAOkouCciOK3Vd20NZcRkK-TsbcoFjApaHMRn6pCNkXVRtSREvaOQcoftdir1vSUeVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب زاینده‌رود به اصفهان رسید
@Farsna</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/439653" target="_blank">📅 16:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439652">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5627f4c359.mp4?token=S6fRikZyRAcAHAHFMAnC8LrdY2jnJ1gvYOix_T6z-ol07TBl6qTvtMfSDU1XoXs8KH6PUVkJyrl2gNSZKO7UhnkOfByYZ4wxC1G7ZFPQ7Hpxw3C9bAE_Oo7Glv2gyFCiVlBY1fgoRGJcvi4M3B_lMG2TiM5vyPA3DVaUuoU3-f2sMg7qQUNf9WP8p9gbGd6XenSe1SeauwpwD3L2HpK1GkKIkNATwhQbwfQrxBcJnJmopg3x-2eSfYUKJVABYAOwkbm2dolW05IID7eUJW5OOJulkQSl371gyMrL47DmKog22vzWs2QjucVtVyC-XpcmjxEAbgz3wp6q4NtmYW7bqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5627f4c359.mp4?token=S6fRikZyRAcAHAHFMAnC8LrdY2jnJ1gvYOix_T6z-ol07TBl6qTvtMfSDU1XoXs8KH6PUVkJyrl2gNSZKO7UhnkOfByYZ4wxC1G7ZFPQ7Hpxw3C9bAE_Oo7Glv2gyFCiVlBY1fgoRGJcvi4M3B_lMG2TiM5vyPA3DVaUuoU3-f2sMg7qQUNf9WP8p9gbGd6XenSe1SeauwpwD3L2HpK1GkKIkNATwhQbwfQrxBcJnJmopg3x-2eSfYUKJVABYAOwkbm2dolW05IID7eUJW5OOJulkQSl371gyMrL47DmKog22vzWs2QjucVtVyC-XpcmjxEAbgz3wp6q4NtmYW7bqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم رضوی غرق در عطر باران شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/439652" target="_blank">📅 16:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439651">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGHfNBxbujG_IrkNsdtJN4u8VMZ0dPiUs9rmHQJdoK8xOhhUHM_vYV1NHPcz6mmbgjCBnLX6Sf-PjuZIyUqPlJ4MxmnuSoE7ZT5G6qeXPxOPncdNG6iCKwlTtc3u0ZFNwTufPmjcrL48gwuarWy4IBLQUGkkAYGb5Cw2ZRG0vGn9kqAhDW-2k1r0X-dE0Y1F7h9sCo2YoILOY0ZgPOcwJVgIy8u97pmdiomeb_QcGkKnlSgs2wtW5GDmm4UgB7P4ehyajngUXIzn6kU5dUWwVoD2JI2szhpdOwael9LXbW-Cc9Jjs6MQySnORv1VmRZz5ijBkGeTZRhs2aL6Ys5Myg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندگان مجلس: برای انتقام خون امام شهید باید بُرد موشک‌ها به دفتر کار قاتلان برسد
🔹
جمعی از نمایندگان مجلس در نامه‌ای خطاب به رهبر انقلاب، ضمن تجدید بیعت با ولایت و تبعیت از رهنمودهای رهبر انقلاب، بر حفظ وحدت ملی، تقویت توان دفاعی کشور، حمایت از نیروهای مسلح و پیگیری مطالبات ملی تأکید کردند.
در بخشی از نامه آمده است:
🔹
«ما امروز علاوه بر جرم نابخشودنی تجاوز به خاک ایران اسلامی و قتل‌عام کودکان و مردم این مرز و بوم، با دشمنی که در برابرمان است، پدرکشتگی داریم.
🔹
ما خون‌خواهی و انتقام خون امام شهید و دیگر شهدای این جنگ را تکلیف دینی، ملی و سیاسی خود می‌دانیم و از نیروهای نظامی و صنایع دفاعی خود آن‌قدر حمایت خواهیم کرد تا روزی، بُرد موشک‌هایمان به دفتر کار قاتلان نایب امام زمان و خامنه‌ای شهید برسد.»
🔗
متن کامل این نامه را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/farsna/439651" target="_blank">📅 16:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439650">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBNNxzywu6Eo99WArL0ZUCIRv2PEy121AlTXRHlSk0mc5qMc9MR4pPMVYMQlaeIXtjit1wlleZuaqUBptTKjSqt9DverbnSq4S9QusXdkAOlJw6qwCohf5fAatUlrfRLsOOc0h97KAAehOOl-Tn5Q6zOENWKyE3AP9XYkK8X72c_L9dsLprOmFP1YOYMxuCehD3ZjX7NjWDkj8vU6Uecrsc8lJ-WGpbRS06653uPKpXOmAWHJHbq4LDWuWiKvaHG66An6L821Qb_quIb4yzWjeg8sPZtfwB8-EEqmNjTaabNq_9sokbhZbJX5N_s1ABRWOTXqY1cCu5F7pyYrc4DQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
وزیر آموزش‌وپرورش: با توجه به شرایط جنگی، به شورای‌عالی انقلاب فرهنگی پیشنهاد کردیم استثنائا امسال تاثیر معدل یازدهم در کنکور از قطعی به مثبت تبدیل شود.
🔹
این یک پیشنهاد است و شورا نظر نهایی را خواهد داد. @Farsna</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/439650" target="_blank">📅 16:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439649">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n335sI4gqzfYDnCKC1esxYlSNH_ZQ2Xg3bylWAWBbIsmCCYKe3D5FrFhel7eas1K7ZUlCcPiqYSNLHDZM7ZuMqKmOBZxBBSyOTLpzGf8VbnFyX9MFIvslHSnGMhKmmRGhjGtL5PbMP_CWALb0p80wMcU4GO7zqTA_S-xC34mRllBYFbY5lkUf1SnZQym2ycYf6SLjnv4YAgtp64we9dS_cYxOPfYhyo8aDOyR8GsZVPdZPxq64cXbZ5fctuN5veV-M1qGESiwtea7NGTvjz3UT1h0pLLlTcHAyUuPuaImcv4n1cAFsxzY0ibJGlV9wFgmZRUPi16_CrCkGMY1PvWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زوج‌های جوان در سال جدید نیز از بانک‌ها روی خوش ندیدند
🔹
از صف وام ازدواج سال گذشته حدود ۵۴۰ هزار نفر وام خود را نگرفته و به امسال منتقل شده‌اند.
🔹
با این حال پیگیری‌ها نشان می‌دهد بانک‌ها تاکنون به‌صورت جدی پرداخت وام ازدواج را شروع نکرده‌اند.
🔹
پیگیری خبرنگار…</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/439649" target="_blank">📅 15:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439648">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cc6cb7158.mp4?token=LIS6WM2Tuodd6KsGyvXVZFepbwWOiHtovKcC9Ao7uy73xcQ6Mz5Gme-PlTkyZnS9Oosg9-Y4UdH6tkfElq1JSjyrielsa6woaFbYRq2k8MI2hIUIYYhWsFCp_DXy9tYUE24QZH0pBySz75LmciUunHfZ5M5mLosk77c5OUcveWzrDr-rKN3DsfZwMzgbhTbl_sHSxFSC7NXCcwhA88u_gL4hJFu8ZxMs7gMOYRviC8TGBhOPUgp9pDULuLCjs8Enlddji35SdWIAkReYdkm-LpgxSBkDuRLRP0X5xaVSqQ5xMoM72cGyb2EGRpYCNNHbqRXA8HY1oewwRcsmH6xv_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cc6cb7158.mp4?token=LIS6WM2Tuodd6KsGyvXVZFepbwWOiHtovKcC9Ao7uy73xcQ6Mz5Gme-PlTkyZnS9Oosg9-Y4UdH6tkfElq1JSjyrielsa6woaFbYRq2k8MI2hIUIYYhWsFCp_DXy9tYUE24QZH0pBySz75LmciUunHfZ5M5mLosk77c5OUcveWzrDr-rKN3DsfZwMzgbhTbl_sHSxFSC7NXCcwhA88u_gL4hJFu8ZxMs7gMOYRviC8TGBhOPUgp9pDULuLCjs8Enlddji35SdWIAkReYdkm-LpgxSBkDuRLRP0X5xaVSqQ5xMoM72cGyb2EGRpYCNNHbqRXA8HY1oewwRcsmH6xv_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شما هم به این مهمانی دعوتید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/439648" target="_blank">📅 15:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439647">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCKa3BWpUV0xcQSNcAyvGtYAF-qke5YKlTW-tm58iTERg996dgggK6mpFQ9Li8BlD4ukTmBO0IlFNOq-ofRaVEWf91Lh9So7_EwI6LrebkmBqIfpSRRDc3j2UKfC3VX071BBFjRY7IvM08KWYhHly-zij8lqiTT7nEwjuMaBlkV_hd4cIplPOOTMUn9EuzFSLk_CirqD7nhWD8L4J80sO-nPW9EtMNJX9iXtqbmsBokY39790soFcJZ_dof6njFLl4FVuDvTP_gTRPO0QR4myGfUxVviumFYBhkU9pG4u9HvsfAB59Z3nT6KyV--lri3RqSJhQc34Fboq6RWfeha6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عادی‌سازی بی‌حجابی؛ این‌بار در آپارات
🔹
تصاویری که منجر به فیلتر یوتیوب شد حالا از آپارات منتشر می‌شود. یک برنامه پادکستی مدت‌هاست با بی‌حجابی و پوشش ناهنجار تولید محتوا می‌کند.
🔹
در بخش‌هایی از این برنامه، مهمانان زن بدون حجاب حضور دارند.
🔹
کارشناسان می‌گویند «حتی یوتیوب هم در کشورهای مختلف مطابق با قانون کشور مقصد فعالیت می‌کند و جلوی پخش برخی برنامه‌ها را می‌گیرد و دلیل فیلترینگ آن عدم پذیرش قوانین ایران است، در این شرایط بی قانونی در پلتفرمی مثل آپارات که مورد اعتماد خانواده‌های ایرانی است تنها فرهنگ ایرانی را دارای خدشه می‌کند.»
🔹
نظارت بر تولید محتوا و ارزش‌گذاری آثار داخلی می‌تواند این مشکل را برطرف کند؛ مشابه سازوکار «سند تسهیم» که از طریق ارزش‌گذاری محتوا و پرداخت هزینه به تولیدکنندگان، نظارت ایجابی و انگیزشی را تقویت کند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/439647" target="_blank">📅 15:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439638">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXB-7IhycSczxFJqZ4PZAjYN-prDyTBz72Ov8SSwP41rGhJcSqGOu4fvQ-KOE6LZy_RrgziuHej4eSrOjaYA9tkbLpWrGQv976U4EBCU1k7qr4yQrRxivPceVm7fu9aVICxWAox5wlj6u-pijP6I8ReplXm3hLC_9zbcNxltpx0TuSZPP0Y2UovveJoq6tfivpl9xPFcuegnoLgQ6JMpKRfdmyTQgqThkqVd7SU44ubbvrz9kvC_6-CHNLfTPyZWDqN5QXbQVtnfyidpgg42_-506EemInd98jC9aU6lkw8xmV7sbFwagtRyjZgRnxYSb5JBwExZqhr7FHsAf0WxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yw1VStLLX-4zRal_yzDgH5EWtThELTrOT30U0tSCmdU65ykbo3YQR71vRCPdxMEwucn_63VgFYN7r7dcYgzeB2fjQYQ3n9X0xLeES0M5MRedDDX2cuzt9mTDDJua0iqP9FPNluoUx7qVeLjkvFouu6A-jmJplcyZDIVUxHnOXc3OMHnwiC80LuLqUqz2_p7jET1fMtw0ZOXYMVX7EIs6jA-_EYbfEyref1I-CqjIpimJJxdTo-SItM-uJqm30fEWwq0peOcFDn2vUruXyoGc9Ta8uCFDjKzYAGwof4eTUL3vFqw7XJsaFw0pmDl5V83nnlvjvoW_6FsPhW9qp4qQZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PmUhqsGvI7AtmP4ET-sXdaUfA5JaUO3zOceMbp0q5LmMYsUkre3Fn4lG80ikNtDLTMaUWA-qtBtaPk2sC4IAwJQBI72tPuldrymXuLcRkcm8cmcmYKxHTWP-H9SECXjFQG9dRRzS5DbnnTC8VzhgaDel_B1RFmrj5hazBzLMQRRz9xsV2qcGR0S86cwkqkFFsEIaD9aP1r-p-i-REoxi0AoiI_PfoSYkwscxQc_xXKP_xcYgdPVxOW6oJ4jIa0HXUoEsQ6eYjV3XOsO3XGL8Pm3ON1-KgAiidHDfvGZZ-2ui1s4GCz_SvvNXrJ7qN31heN3GAH-KseXvXQvpqsArFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPz9tu4WyakUyeGH_2wgiFlAxUXDN8giY5cA-I_x6dzV_SmybmtQPSH8Y_jEtCGRT0yXUTV0Q2kBEpSCA_-i-XLL-1X7cQNy-0W-s74o9n1zmZanj_8jCht3ah2ZovNw-BEOC0H9haSdJBqxUGX7tEeOgZ7jbHB8TP5Cek7zZR1eKylA4TmiRY0jDRyjCshiuKVumsZMiSTH9eGEi_PH8BW0Zi3n30bDe0gQyGGxGunhFSUcKjwEOfMH2A8Dm77W_jqMaBOBVW7lrs6JWMD0wvGwHdt-OpHas1gH29ne5wPFKO3m0OO_dqQUd8l2aiY-pgBibZXxFw9LHHjfkPanwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Poh-ctLT1K21u1AY9JSTpNMm2k4io8QspdypBkZySsme0CTHndA86QFtqPL6ybPZQY6-IsiaTl2_0uZ4oQJ1AT9SWxqKR1npucm3zRA9fXznaK2Ghj05S_ZnUrzBI8lQJIXoNqQKpTefyekSpJCeLo_FiQkLrnar2LgYYe2s7pDL9Tmgt0V_spBwOLqbUxacSb7jpC9eeJp3SL0XprvvxDa3IrXAKTfzEBZ4iE582tItZ0GdV0JtTknW7A5diDf3OiK4HZmd_CQtlFEbImHEuEBSYhOxSDCYrjyNkZDa0JA90SqDzvo-MrRMrhgj-8uYp_3QHDPFBtdOHL8I7pzorg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f29bFIeneNAohFty9-WDByB3ns3N6s0ZAcu8Uedzp0td7F-yywZOh8h4VuB6qIHWAiosb1eajfIbreFXmuscIkeDAzsBLYb2nGVqX5nWRctOCwioqgE3u4H4_9P9ohhsczNIuKhHZe-KGxOeeX4o2cVahZjgaLcDxgdGCY-NdzPcwJCYDuOIXc9PsPxy0WKXdj6OThahlUwum6fIM22j9ExRD0KgcI1kJjujcPZAYG_1scE_hpMsTNfaEIX0N2z4C1vjKqUopR4QTAdzzgY5RBiT_it-HMm5KlPsjMNIOXyX51Pgs6LRIhrrnNrHWSKp2CxHID680XKvpZ-Bc_zZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ScfNGcXK-oYTJAbycgbtVkS65EARu5hf-sX1qkCpx0ghQHilksDGN4cCN4KpClfu6lqNz9JrndroqYNTJuuEBydu1K8NKWhU7hRYpHXlvDhrpTOhhfEU_NCewV9IA_tXPq_Zk5oY4Juz7UI_4-nzH6vp0L94RJO7mHo1h8xHdn_S7UAgeJP5YEkfUCr7GBDt9ed2qv3uLuy9DAVDw_8_3PtoeWGJWfa85fKH0u5pbziv0cpPW6ZoEeBVdBA0szv8tPJsUnPKxeeGNHUdoRcEDNCf1SGry6LqFemqKudP8KouCAyAtXMkGsU7197VprWRncew629OSRBRnaH-1utgZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdvDjRYyo5kLZOlboCNfeYQ9c76KSV2RNMNvqS9-RQyt_SbIYP1sc9eLbbw8V3Lx9tBJD_mPSp2WicLx3vRwb2SD0JtI0iRE8mqatiQ-0OGZft7xL9306Wq-10aLqWGWPDdS9jf0BwJ0_qSTGPr96Cr_w6vvCREWmqzfnxKpscxV9uWw7aMqd-H3Ssi9KIhWJlURmnwVf1-dD_wnFl_spsDU1QTGi5SrWpjtfuA372A5inNxPaqQtFPW4BgwE0qkFZ0oT1-vKL6W3XIb_6HuN2OJC8637NQ4scb_axCwvjmkVAK_3V2hDKB9JInKMaFiFbacGDO6Nk9RaiqMO62QjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQo0apfNZzqwnAy75k79K62iAEyM6ww5WUQpoZF2VB7DJnweVhj8tSCT-ssbDjBuupeKqGFZdiQtBgp3eX54Snf8Aw_EdOZVQ8ioUq16qEMqSRFhTY-UCePLTLf4uApdGnTEQp7j89qzlAT03I2Nxhk9qgLP1g5Dvo4CUFPwR7r8j9UPuqvOMhI9rTRkYy8LevR17WNtRi5qU3-U1_CDDDB07Mj11Vj9KZ_CVu-d31NwrPOHeYc7ZvXdAyeYpuqN8pKyP0x46_TazMoLoTOkpSDh1R1yR6m2iVBizVHOq0upquZOZPcOOVjgC8BHG_O8YApDRdsBvMTmqenBOq5OcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
هوش مصنوعی شهدا را در مهمانی ۱۰ کیلومتری غدیر به تصویر کشید
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/439638" target="_blank">📅 14:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439637">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‌
🔴
سازمان هواپیمایی کویت: حمله به فرودگاه کویت چند زخمی داشته و خسارات شدیدی به تاسیسات فرودگاه وارد کرده است. @Farsna</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/439637" target="_blank">📅 14:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439636">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">محمدباقر قالیباف نمایندۀ ویژۀ ایران در امور چین شد
🔸
پیش‌تر شهید علی لاریجانی و عبدالرضا رحمانی‌فضلی چنین مسئولیتی را برعهده داشتند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/439636" target="_blank">📅 14:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439635">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سپاه: مقاومت تا اخراج بیگانگان از غرب آسیا ادامه خواهد یافت
🔹
بیانیهٔ سپاه به‌مناسبت گرامیداشت سالروز رحلت امام خمینی(ره) و قیام ۱۵ خرداد: حضور مردم در خیابان‌ها پشتیبان میدان رزم، سنگر دیپلماسی عامل ضروری رقم‌خوردن پیروزی کامل و نهایی است.
🔹
ایرانیان هرگز تسلیم واژه‌سازی‌ها و دستاوردسازی‌های دروغین دشمن نخواهند شد.
🔹
دشمن ناگزیر به پذیرش قواعد جدیدی است که ملت ایران و نیروهای مسلح بر میدان تحمیل کرده‌اند؛ به‌ویژه در عرصهٔ مدیریت و کنترل هوشمند تنگهٔ هرمز.
🔹
مقاومت تا نابودی کامل توطئه‌های استکباری، اخراج بیگانگان از غرب آسیا و آزادی قدس شریف با نابودی رژیم صهیونیستی، مقتدرانه ادامه خواهد یافت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/439635" target="_blank">📅 14:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439634">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7df7790086.mp4?token=OqXCPEDLwysk2SihtJG5iLUA0oa0wTmL745G7axpNMG2nsnL7L37dWDWVQPxlx18RIy8yg_JmP4nSB8MUTfPflBeTsRSZ5PEezJRAAdD3pgl5zc-IIsp6VHEgQ_dB0dX1hdjNzvci623zbpXkF_ZqDpgg5-z0qk11sTjV4L5qeSn682-at629ufpDAe_AfAYQwn0UHjS17mqfoevP0hXQVmA9uF-GqCU7V4zHuVRdRkMhPdqiZpX4q6VP8dcgom5Wi4678Nd0gQM48ffQhGqXlDd7TcOAl_1BS6X74gme9pP6Bi14WWevnHKDYeZrlf0frF2KCf4U_Iy2JcBF07IHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7df7790086.mp4?token=OqXCPEDLwysk2SihtJG5iLUA0oa0wTmL745G7axpNMG2nsnL7L37dWDWVQPxlx18RIy8yg_JmP4nSB8MUTfPflBeTsRSZ5PEezJRAAdD3pgl5zc-IIsp6VHEgQ_dB0dX1hdjNzvci623zbpXkF_ZqDpgg5-z0qk11sTjV4L5qeSn682-at629ufpDAe_AfAYQwn0UHjS17mqfoevP0hXQVmA9uF-GqCU7V4zHuVRdRkMhPdqiZpX4q6VP8dcgom5Wi4678Nd0gQM48ffQhGqXlDd7TcOAl_1BS6X74gme9pP6Bi14WWevnHKDYeZrlf0frF2KCf4U_Iy2JcBF07IHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا اسرائیل سال‌ها به‌دنبال تسخیر «قلعه الشقیف» بود؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/439634" target="_blank">📅 13:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439633">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMfp9ERa2itxkLAjvCTlWpd-d4kYn01os_4BitNV5P6k13Bv_Tzifcb-vNlF4sqneY58rRaE2JLFdwpmc3VPKpAUXWQxyRk-2JrCAQY8esxKy14rc7HOKcdoORuUYf-O7BLxyi0Jks_ZtYEnnFyYomrkWXUm6MAmgiamnnvPugODoUN7q6TD9IwF9aAQZD1m71mfc541P19Ggglt3xqEHNvj_RDkkOTyU-yWEc5xHs1weo7yB0HximW2rwrSU90uPnFnMzgnhH4KQXR8PmNAJgEqjG12n3Btgj1K38ae34F4vMcm3DzW2vYJKrqUUxtPJi5qCNO5vuTti51G7i3aTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚙
پیشگامی بانک صادرات ایران در بازسازی اکوسیستم دانش‌بنیان؛ حمایت راهبردی از آموزش عالی و پیوند دانشگاه، صنعت و اقتصاد در دوران پساجنگ/ تأکید قربان اسکندری بر توسعه آموزش عالی در دوران پساجنگ با رویکرد حمایت بانکی از اقتصاد دانش‌بنیان و فناوری
🔹
در راستای حمایت بانکی از اقتصاد دانش‌بنیان و فناوری و با هدف تسریع بازگشت دانش، پژوهش و فناوری به چرخه‌های اقتصادی، بانک صادرات ایران اقدامات راهبردی خود برای بازسازی مراکز علمی آسیب‌دیده در جنگ رمضان را پیگیری می‌کند. این رویکرد، ضمن جلوگیری از توقف فرآیندهای آموزش عالی، زمینه‌ساز تقویت پیوند دانشگاه و صنعت در دوران پساجنگ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/439633" target="_blank">📅 13:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439632">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-text">🔻
«بیمه زندگی و سرمایه‌گذاری پروژه محور
#بیمه_البرز
»
•
💰
۴۰٪ نرخ سود قطعی در سررسید
•
🗓️
مدت قرارداد کوتاه: فقط یک‌ساله- معاف از هرگونه مالیات
•
🔒
امنیت بالای سرمایه‌گذاری با پشتوانه بیمه البرز
🔗
خرید کاملاً آنلاین و سریع در کمتر از ۵ دقیقه:
👇
👇
👇
lifeapp.alborzinsurance.ir
نیاز به مشاوره دارید؟
🏢
مراجعه حضوری به شعب و نمایندگی‌های بیمه البرز در سراسر کشور
📞
تماس با خط ویژه: ۱۵۷۴</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/439632" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439631">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/439631" target="_blank">📅 13:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439630">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sjw9kcN3ne3LdPn3di-YpeMgtjJ8ONKunjzxKjCzpDVFacnzPZ_ousYbDrf7VBYBbE62bFciyJKW2UvGFj5l6oAAecPJUEGslz83GX_DQJHYQtiTU44plBq_fMo2FWYJ3qUeSNGKZnAAWVroc04d9Nq2OESW-Oeog6Bji9Rzu4xyWId2NmzJ28vJo3OhjrfOh0bmjEST9gaSd_XozGx63KkatYYjOeGgYJFoRJVZuEiHK_fPByCf7uBOe6ODREo64YoEhbsMf1R9wjjeBcxeQ5zS0Fbev7Pn8XX38PwOcAEF7f0-RDNsy99JWFvYpdg-JnaQJy47UyDZS_m08yIoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۱۴ هزار واحدی به ۴ میلیون و ۳۵۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/439630" target="_blank">📅 13:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439629">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c56b293a99.mp4?token=PSnVn6vPKWW51Sed99vDx2oR_J4uQTrjgSK8DyW7BQAnyW3VomYWWZ2v5PMqIClKRVYW-R-N8aiLR0JQRtzf88CQmj9mz8k7czcIB8UAfIFeezm4w2Gc_emdMJ17jGIbj-og8x6iieG0EvmY9zFq9e0nvJyKsii5E9OwqBxu6ewD2N-by69zMvS-fzVziy_h_LYNgHuYL5PmB08CIu4HO2XZujlN5FMkHNaVqFd89VntYV6OLF1qqJnJJRL2Y8m_39EwZeXjq9jlKmaVphLDVWgnwIFNEdeQHkswY3lJM9Fgsb_yFUV-3tVB6AMAN3ijXGqDS_2bviAVZIDkAv2-mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c56b293a99.mp4?token=PSnVn6vPKWW51Sed99vDx2oR_J4uQTrjgSK8DyW7BQAnyW3VomYWWZ2v5PMqIClKRVYW-R-N8aiLR0JQRtzf88CQmj9mz8k7czcIB8UAfIFeezm4w2Gc_emdMJ17jGIbj-og8x6iieG0EvmY9zFq9e0nvJyKsii5E9OwqBxu6ewD2N-by69zMvS-fzVziy_h_LYNgHuYL5PmB08CIu4HO2XZujlN5FMkHNaVqFd89VntYV6OLF1qqJnJJRL2Y8m_39EwZeXjq9jlKmaVphLDVWgnwIFNEdeQHkswY3lJM9Fgsb_yFUV-3tVB6AMAN3ijXGqDS_2bviAVZIDkAv2-mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: نباید با عنوان «نظارت» بر سر راه تولید مانع ایجاد کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/439629" target="_blank">📅 13:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439628">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9SgACtrBk_RPQVDl82-vG1SicwFVJO96BMFbBxItSBF4eB1NdAz1zg4NdnNHn1Z6-uhgbYuI_FqgbkBkwApJfSACBO7AXv2PsqrPnJJ1rUpXdIbDaWUdOqIwDQZdayyCkQTedZj8N_hn4NuMMYdW3xCKYabrHhcHaht2Ia3JI8Tab0qai0zzbxjW4AwHIITwr-IpOPKaMtn-Z2UVWPr7VrGIDATNIeWWZb7f6JB3kRzJJKYebhk_9H-EcfiMA6BJFWMYfwYWHYfGa1tXISywABjUQUG3VmEkHvrYdgn1-CdvmwcYs4qQ0hlWObYaE3x1rawHunAQuHwg5Ymw3bAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ستادکل نیروهای مسلح و قرارگاه خاتم‌‌: نخواهیم گذاشت دشمن به آرزوهای شیطانی خود برسد
🔹
بیانیهٔ ستادکل نیروهای مسلح و قرارگاه خاتم به‌مناسب سالگرد ارتحال امام خمینی(ره) و قیام ۱۵ خرداد: ملت شریف و مقاوم ایران، در سالگرد ارتحال امام خمینی(ره)، فقدان قائد شهید…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/439628" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439627">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbf6rmL4b4Xu91u1KcyiaQksl4u5yC83gmS3z3jNyXDT9vZw8lNtz7wgIqDybKF-vPCpzzP8w3JGlSmU-2-7sB3YlqoOLgLJBLGxaM7vef_YEF8VCCU7XmTXjUIkqCrpo71sl_jrPyCR6wnk2oqHEaibJPIhXC3ufxNvI484onLf--duLvBALQ_fRjrI7X41BjBfYT8dpYz07ZoEmgJCgLdFOMeqFpngMpb3NiGoT0exSzvD-kuj73ukv2yNGK6Jqg-JBza0fMi-IzXmhCOpv2oWY6VcmEHDtOHWl0HoEjeeWctFD_9bfGFszBgmdni1x08_cRm-omdkRIuMxmSwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اینک پرچم های زرد برافراشته خواهد شد
🔹
در تمام نقاط مختلف مهمانی ۱۰ کیلومتری تهران و مهمانی‌های کیلومتری تمام استان‌ها به احترام لبنان پرچم‌های زرد توسط مردم برافراشته خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/439627" target="_blank">📅 12:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439626">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4759031cd.mp4?token=qYZS1wJP7Ba0B6xVA77mT-nSOrX5wtsh7Pf4tdQJf8hIXdYRgQZu1VeYiLsCEeteR3t_B9gQfbjVY_GUMEH-mUxZAQock_ubZe3BaKKedTTBa7x7PNS6soxHfE9jTYa9O6D8bPoJdOpZSZjPXyy7o4OgHn0rQzdcMlKTcRf59JMLXkymsblpmsVCiIS5RBes5r3dkDj9NnZTFLdq2fzR3lCSUhnudIQHG3P3Vjz0KPI2SRJG3VxkrQY5RoeYkN--faTIUgIzYRA8qYHhhvlDQD6otc7jAiGjyutQXevby6zaQ7PPLB0dL2TTcNnjKFtgSGSP25kyVYaMztw9ncusnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4759031cd.mp4?token=qYZS1wJP7Ba0B6xVA77mT-nSOrX5wtsh7Pf4tdQJf8hIXdYRgQZu1VeYiLsCEeteR3t_B9gQfbjVY_GUMEH-mUxZAQock_ubZe3BaKKedTTBa7x7PNS6soxHfE9jTYa9O6D8bPoJdOpZSZjPXyy7o4OgHn0rQzdcMlKTcRf59JMLXkymsblpmsVCiIS5RBes5r3dkDj9NnZTFLdq2fzR3lCSUhnudIQHG3P3Vjz0KPI2SRJG3VxkrQY5RoeYkN--faTIUgIzYRA8qYHhhvlDQD6otc7jAiGjyutQXevby6zaQ7PPLB0dL2TTcNnjKFtgSGSP25kyVYaMztw9ncusnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار معروفی: شهید پاکپور تا حل مشکلات مردم پای کار بود
🔹
معاون فرهنگی سپاه: یکی از ویژگی‌های بارز شهید پاکپور، مردم‌داری بود.
🔹
شهید پاکپور تنها یک فرمانده نظامی نبود که صرفاً در جایگاه فرماندهی به صدور دستور اکتفا کند، بلکه با همۀ وجود در میان مردم حضور…</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/farsna/439626" target="_blank">📅 12:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439625">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVQtFbNgstAqoUUI3WjpEoIbGbwBF4l6hEL7AFK2YcjZFAfXw83tgIwfTt0N5F8NXHIrcuhlbE7fRWPSxwj160hscZlkv5ktp5l5kjq397Joo2IOmO9j6-7mVpNr_nN5BtUQHyPdk9-upJV0xYMo22glbBrAsJDyiB90ZlIwOZJfWZIUtVh1HjDUznPNYL_8lxoArnYwysk22eK-DAHw6aDLHQI_6GKJ_A765ZFhRBUXOd69d-s1YwemGVs7DXn5JY8Bpe15zeT6jpT99TvKZmhyxd0RB3U1fdglvvpKolIW_spfqKY9s0HhlPpsegi5Hz0_YwkVsQl6tuCiLsZxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی(ع) فخر ایرانیان
🔹
به‌مناسبت عید سعید غدیر دیوارنگارهٔ «علی(ع) فخر ایرانیان» در میدان ولیعصر(عج) رونمایی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/439625" target="_blank">📅 12:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439624">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l40WfJ0z1Qkhk8qHTCpYCughVcyP7aJfMSAJeD5Mip3S2g3vhs8mV1AQFP2_eL6pIKse70lSQ-Vi0wEWiBN2L41bRK2Ue0Wn52NRPLz8uUmu52RbWRuy5tdB7SesvXyViRzKk6S4dXiKUPBT0al-QiCwTkqjrh8VpqxC5X8NvXz0wRF-wY0rFnpBqp_URmFIGrEbGgkSQ7gDw81NeiB4DqPmXD0iSMSAUqS9jrTfkkZAaVhjxDTOXGr-W-lueIFrRfJwLs7YouWsuOMfC4M3a0a1HOhPfdwS1ZHByQ8IHXiw4oIapJy2T1PRPJH_P7GjCXX9CQkwmxa4n9ONdONIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرلشکر رضایی: پاسخ هر شلیک و تجاوزی، رگباری از موشک و پهپاد است
🔹
‏نه در مذاکره و نه‌ در روند آتش‌بس اجازهٔ زیاده‌خواهی به آمریکا را نخواهیم‌ داد. پاسخ هر شلیک و تجاوزی، رگباری از موشک و پهپاد است. تاریخ به عقب باز نمی‌گردد و متجاوز به سرعت تنبیه خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/439624" target="_blank">📅 12:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439623">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1026a8aeac.mp4?token=rJ2NR-9WOJXWBbJ_y8C3GAEWp6cTruPYBx-B_sK1ph66RFOk2scpYAcUuk0wBpu6DknEGuG7lHp2PYVk5MsQP_vQzFDokKgaqVrLq_ataW6vY6fYukqONcuBQsLITdPKclN6aK-mg5HzgXnifmGqOqY1yxqIUzeXrs-GMyyn-izBuUYXAkb-nbxVyFviey3UfEOQiktB13lF2PG1A6tJqEg0eyDYwM_XNnwBOPtgY6zZynEe15T1UK5O5QMGhoNw6Y_gFf0OVwRugGdsK75qjCFHX79BKcwrxAe0waiMF07VY5woXxymjv3c0lf5pRz-Mo4fw01PSdmHJjX0CiwcwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1026a8aeac.mp4?token=rJ2NR-9WOJXWBbJ_y8C3GAEWp6cTruPYBx-B_sK1ph66RFOk2scpYAcUuk0wBpu6DknEGuG7lHp2PYVk5MsQP_vQzFDokKgaqVrLq_ataW6vY6fYukqONcuBQsLITdPKclN6aK-mg5HzgXnifmGqOqY1yxqIUzeXrs-GMyyn-izBuUYXAkb-nbxVyFviey3UfEOQiktB13lF2PG1A6tJqEg0eyDYwM_XNnwBOPtgY6zZynEe15T1UK5O5QMGhoNw6Y_gFf0OVwRugGdsK75qjCFHX79BKcwrxAe0waiMF07VY5woXxymjv3c0lf5pRz-Mo4fw01PSdmHJjX0CiwcwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیکزاد: نام ایران به‌خاطر ایستادگی مقابل آمریکا در تاریخ خواهد ماند
🔹
قطعاً در تاریخ نوشته خواهد شد که کشوری به نام جمهوری اسلامی ایران بود که مورد حملۀ دولت نامرد آمریکا به ریاست‌جمهوری ترامپ و رژیم کودک‌کش صهیونیستی قرار گرفت.
🔹
علی‌رغم اینکه آنها تصور…</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/439623" target="_blank">📅 12:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439622">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صدور کیفرخواست پروندۀ شهادت شهید بخشیان
🔹
دادستان همدان:  شهید محمدجواد بخشیان در هجدهم دی امسال در جریان فتنۀ آمریکایی‌صهیونیستی در شهر همدان و هنگام اجرای مأموریت و درحالی که آشوبگران را دعوت به صلح و آرامش می‌کرد به شهادت رسید.
🔹
با اقدامات سریع و دقیق…</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/farsna/439622" target="_blank">📅 12:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439621">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
ستادکل نیروهای مسلح و قرارگاه خاتم‌‌: نخواهیم گذاشت دشمن به آرزوهای شیطانی خود برسد
🔹
بیانیهٔ ستادکل نیروهای مسلح و قرارگاه خاتم به‌مناسب سالگرد ارتحال امام خمینی(ره) و قیام ۱۵ خرداد: ملت شریف و مقاوم ایران، در سالگرد ارتحال امام خمینی(ره)، فقدان قائد شهید عظیم‌الشأن و شهدای مظلوم خود را در کنار پیوند عمیق میان ایمان، بصیرت و ایستادگی در برابر استکبار جهانی تجربه می‌کند.
🔹
جنگ‌افروزی اخیر آمریکا و رژیم صهیونیستی، چهرهٔ واقعی مدعیان دروغین حقوق بشر را برای جهانیان آشکار کرد که شهادت ۱۶۸ کودک مظلوم و بی‌گناه مدرسهٔ میناب یکی از صدها جنایات آن‌ها می‌باشد.
🔹
ملت ایران در برابر تهدید و تجاوز نه‌تنها عقب‌نشینی نمی‌کند، بلکه با اتحاد و ایمان، مسیر عزت را بیش از هر زمان ادامه می‌دهد.
🔹
نیروهای مسلح همگام با ملت و تحت رهبری فرمانده معظم کل قوا از آرمان‌های انقلاب و کیان کشور تا پای جان دفاع خواهند کرد و نخواهند گذاشت دشمن کینه‌توز به آرزوهای شیطانی خود رسیده و خون امام شهید و سایر شهدای والامقام پایمال گردد.
🔹
دشمنان آمریکایی و صهیونیستی در برابر ارادهٔ الهی نیروهای مسلح و امت بصیر و آگاه، چاره‌ای جز تسلیم نخواهند داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/439621" target="_blank">📅 11:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439620">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8XWt2QVFAA8p4tS1ZHd4a3Sl36I0b41EGWV7jsd2tSOS-yUMCezxSyWvvVrXRCYuxfmbxOf9cTNFDsaCFsp7NAK7V1GefraSHyufLjVPQ5lz0c_XLaiLXOrWNrHRRBydoiXJZ6xuLFMukAlDumjZ1kT7go3Ozm5Z6PtyWo1grci0dgqzn5NE7G_ku7IJvrFuQTwvddcgfD8JwpCmcgNSu0TU8mt1rZJFiiMmLXF8-I8HMAsPn6mstbx5pNMSHeeqe_AvY1bzv_X4Xj-sGcAofV7sJcZKjfr6Pz5i4grSjWQMGhkXSqg6cprZxWQeu_euIvWUpQZ8My1r7RhxuEDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
نیکزاد: امور کشور از جمله مذاکرات با اشراف رهبر انقلاب پیش می‌رود
🔹
منطق ما این است که زبان دیپلماسی باید ذیل فرمایشات و اذن رهبر معظم انقلاب طبق بند ۵ اصل ۱۱۰ قانون اساسی باشد که از اختیارات ایشان به‌عنوان ولی فقیه است.  @Farsna</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/439620" target="_blank">📅 11:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439619">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nibAIAC4o6CyrZm4G3eztsPoluW9w_UuxjnDbWmivOSwPNvm0hqVFL0tgAigIkDER8AYMZbtLj81pHIy0sAw-hONUwRBZnrawRuqkvP18Avz27n0J80fq3LPD2gdakFrcSJNOMRlSYAH6sa4Ko-hH3GEz_RvNkthmR5nz1JpqQBNHWn-f4jZkAHQVJSZwJ2o517AhaiHoAyx_sR3HzUXn9Mo407E7IYW4p7PsAeVRH4fK46Fiv827BsbAzvpmapruYdtlkrHBYbtMykmQ3O_2hrZLNqsFl9lrpFjk-b1dl9dWJooFVU0GgxyIBmzhfwc_xWKmM12FaTYb3F__DCpNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موافقت هیئت‌رئیسۀ مجلس با برگزاری رسمی جلسات صحن
🔹
گودرزی: هیئت‌رئیسۀ مجلس، تصمیم مثبت و موافق خود را برای برگزاری جلسات به‌صورت رسمی و فعال‌سازی چرخۀ قانون‌گذاری اتخاذ کرده است.
🔹
مسیر هماهنگی‌ها و مقدمات لازم در حال انجام است و به‌زودی جلسات رسمی صحن همچون…</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/439619" target="_blank">📅 11:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439618">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIaX_wo-lVVvJPhPZH0xUB9PUHP25HGqhJYlbJ-9Tm9AeW4Pl7pPFd3JGA_eylTmevLkVxIN-Z0Qn6uHK00Xe5wQiNv6C2VfnnacNUJEQj2S2kHYisozzAeOWimmJzaTjIBJtIQvLW7K72mF17A193FnAP1_29mo0uOXbGrd7xI0xe8fjaKGgqcIChZ5g7vRYMEvlP86JfTZV4eVvsiHHQKA6ArMNFxig_86c_ieJGgENj4GMNSCbv0jWQZjARdzeISFgUeJwE3AGSW1h6_XUFpMADavwGB1OsinEiHV4Jm7W8EVlxsSTxSfUFEmf7yVIsxbmiPh5USLMcKRUG44aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفت
🔹
سپاه پاسداران: در اواخر شب‌گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگۀ هرمز مورد اصابت پرتابۀ هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.…</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/439618" target="_blank">📅 11:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439617">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc6258e9b.mp4?token=QpNLF4vfDNBlUd0Vdvs3tHC2m9GoxPQOdvB0MBDFDZzJfG04FSYKa05qu-TxaAE9qg_qTRz_Pgzf-tOxCjM1rZsHh3b-I21apCtuAy5f459w5cM_BhGDp1iw3xAuP5G6B7cOOMR9JWI7qOmaxojNFx_lXpurhR6uKcIpdrJglvMXxcIMaCd-vSjMbx-r02np6q68hI52wJaqSkJBm_yHEtuxIRV480_mF5qJBCuKEUUttAx903xEMMQNdLBDSrEq5rlenp6xJ5WB1fKqxuRxk-_Uz9KtPbOWiBdhrs4OgDyLahyi8T8p3OLbwq4Jeo162xA8649s1NyCpl7zUSawWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc6258e9b.mp4?token=QpNLF4vfDNBlUd0Vdvs3tHC2m9GoxPQOdvB0MBDFDZzJfG04FSYKa05qu-TxaAE9qg_qTRz_Pgzf-tOxCjM1rZsHh3b-I21apCtuAy5f459w5cM_BhGDp1iw3xAuP5G6B7cOOMR9JWI7qOmaxojNFx_lXpurhR6uKcIpdrJglvMXxcIMaCd-vSjMbx-r02np6q68hI52wJaqSkJBm_yHEtuxIRV480_mF5qJBCuKEUUttAx903xEMMQNdLBDSrEq5rlenp6xJ5WB1fKqxuRxk-_Uz9KtPbOWiBdhrs4OgDyLahyi8T8p3OLbwq4Jeo162xA8649s1NyCpl7zUSawWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد: تاریخ باید بداند رهبر شهید ما در پناهگاه نبود
🔹
نایب‌رئیس مجلس: این یک واقعیت تاریخی است و باید در تاریخ بماند که حتی خواص تصور نمی‌کردند حضرت آقا در منزل خود به‌همراه خانواده‌شان از جمله نوه، داماد، دختر و عروسشان به شهادت برسند.
🔹
حتی به من گفتند…</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/439617" target="_blank">📅 11:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439616">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc5ed11f6c.mp4?token=fFfQebaG5iv1uaG92jPCxwyic2FXcqceT_jDTl68PEeUjn2xYZAh1ptTAdzZ0255cPVfSuYWD1D4yNXUuWYtKZVw4-cPqKrUEgAQ-N236xXOCseZkC0s64E7zK0GQG84_QlEKwLHaFPkd-TCctPF-JIRMR7_PdnJcrhAMm8FMbIEM4tOC7e3g1VKJr9E5KmtC12LWT7TRvHWEdxR_BaOS1wG5nmhykGsLKXzHOuSO3T20C_S9O09HvLnkQOLiby90twwG25a3iyndHha4P8amZZyYACAqcCb5LIsgK8U9riKzraxaAdf09ZHaSG4cajA3HAHm6olFmYpgdSHXg5Xxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc5ed11f6c.mp4?token=fFfQebaG5iv1uaG92jPCxwyic2FXcqceT_jDTl68PEeUjn2xYZAh1ptTAdzZ0255cPVfSuYWD1D4yNXUuWYtKZVw4-cPqKrUEgAQ-N236xXOCseZkC0s64E7zK0GQG84_QlEKwLHaFPkd-TCctPF-JIRMR7_PdnJcrhAMm8FMbIEM4tOC7e3g1VKJr9E5KmtC12LWT7TRvHWEdxR_BaOS1wG5nmhykGsLKXzHOuSO3T20C_S9O09HvLnkQOLiby90twwG25a3iyndHha4P8amZZyYACAqcCb5LIsgK8U9riKzraxaAdf09ZHaSG4cajA3HAHm6olFmYpgdSHXg5Xxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیکزاد: تاریخ باید بداند رهبر شهید ما در پناهگاه نبود
🔹
نایب‌رئیس
مجلس: این یک واقعیت تاریخی است و باید در تاریخ بماند که حتی خواص تصور نمی‌کردند حضرت آقا در منزل خود به‌همراه خانواده‌شان از جمله نوه، داماد، دختر و عروسشان به شهادت برسند.
🔹
حتی به من گفتند موشک‌هایی که محل بیت را مورد اصابت قرار داد سنگرشکن نبود بلکه موشک‌های کروز بوده است.
🔹
دنیا باید این را بداند که رهبر ما در زیرزمین یا پناهگاه نبود بلکه در حال رسیدگی به امور روزمره و جاری بوده اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/439616" target="_blank">📅 11:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439612">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E54DYMjDm9mGifRB72fFJRX1stWp28IwTyCMGu-mocjWvrbJF8RVLHzHKEw3nHCi6RMSEYi_RByqi0oF77iPMQf2Uwu9_CNRPLFaUefIbO8ankFqdD7KcPPE3UhzKL_T8WDXWJiK90KzHVGSujg5GbF1IQHKNJRYvSTfUcAonlcEXzwvOltWog3zD6_GOe_WAaGIt4etHz9c8N-4gmfwLh7GpuG3rYmAgVIu77x2B7FGBCVRmg4eaZKJQ7MGPjRrjAQh799r9QCTRuPYWoMqo2Gu9eEgvLFVQnRN_xUjxjQkl94PjkpNeLiBPDk4BQXQ7DyabuSG4VRfoz0f420f6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X6QL7mMyj617ae4mJFM2ub2hvLj4f3jltMLS_N7jxWhfc2oRVTQXdwqYqzDIZW6hiNHfvH-NmDw7-TI9j6SN9HigJIir6ATK3l_HXFU93c0Pn5V19CX5yPrYvNHw9wjjPYO8lKq9jGMn43gyFLLoDAugon6nUWPbNjlcSSMrlDVrCU5PW7klRKyoaLDIxqVj-Mv4OQrmyHgEeUIQZJFfow64QiQsg1rs01iYeH1H0v2otfnXxOT_JkL_9oJ4sD_-DfwvFonUi3daUVkmfKzqHbNQu_gOuQbnC7cjw1-k7C3Ou4lw90nHYsciU_U-HEd787AabAXq3TM6Idxg_zpUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gMxHtaCIXD01VsIGRMD-IqHyPBov6CSu9QNVvXYZ34e14vLWsmkCtGMT84QGOcpzjkdntD5PxAjTr5EP1lq-0MU6Sfm5qRNPylkopiKMOKUUZ178K6jl0RXLtS_Dq3VcJ26hSc7oTUfEfrHbcBhzOzgOdIdkMnspfqtsDB6Q7s86jVepkiQelyd6poPDc-7qFfpeWkADypavQiReyMi7qoKc6elXjwaZ3sIRMv5vbv_wUI4flk3yzjNMmnx3z-xP9Hn2S-3_D0Ix8HAi4-91zxy0cUl-7HBULPp_kLgSv2DeyrJ9KVaKWJI3zFRGUC3RmqgtRkkwLuuFTQGPc86brg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTP1fsCn5l-AMO7smtPzghlRTX2suPVRam_0wTWFVe2rdAkMiiWr4xKd8wNjqudi8ag0t2fhz5mfagVGeJPDlwigxA-tIAlEKOtQOzsIedoevKQzOeWUV-6o3t1lxVeQGmllb4SXgLqSwKg2cuvCX_UlKKwPw93uFcIW7BEFYCgdKN6Ij7Qv4lOViSdhr6T1L4S5eu1mGlKdEVj6IY6gD9tZsdxuWDN5GeTnP3F4c1Z4hMFL0DGAIiGbckOyuSrbsXfRnKvbG2_c7o1cyHjgtb81DbQ0t2jpKTmns0fUTEAFZFPEVZyLDGk7cFeRMgyActu0bLzhtUvUE4pRucUjSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: دولت به‌دنبال ابلاغ صرف بخشنامه نیست
🔹
دولت به‌دنبال ابلاغ صرف بخشنامه نیست، بلکه تلاش دارد از طریق اقناع، گفت‌وگو و ایجاد تفاهم میان دستگاه‌ها، زمینۀ اجرای مؤثر سیاست‌های اصلاحی را فراهم کند.
🔹
هر میزان که بتوانیم بهره‌وری را در بخش‌های مختلف افزایش دهیم، اقتصاد کشور در برابر فشارهای خارجی و محدودیت‌های بین‌المللی مقاوم‌تر و تحریم‌ناپذیرتر خواهد شد.
🔹
جلسۀ شورای هماهنگی دولت و دانشگاه در حوزۀ مدیریت بحران آب به ریاست رئیس‌جمهور و جمعی از مسئولان دستگاه‌های اجرایی و دانشگاهی برگزار و احکام اجرایی ۳۲ راهبرد مدیریت بحران آب به دستگاه‌های مسئول ابلاغ شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/farsna/439612" target="_blank">📅 11:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439610">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kyRBuUxssCzZ4qbspwVk7iLZxPv7l9BmursQ2f61ffuNpjY6eCNkdgjJHs5Abkh4CGSDTXKJn1HLmy1FENQBSu042-xQVwgJuQarlh7hrttOIi3MOQasalUkE_TvHFx4F75PeGT_cpeLjv3p8mhi03AE4Bkx_-tpkXIqyEfYkSqdZBZjDjrZCTVIdGKGcO_ybgR0w3MA_lQzWw-laQu7MzE_Ms9b03409pkX5aD5YHEh9mEazGods860rCCnLtJkm3wlMXC0VPMZGh1-EBhBZL_DrFNH_nknJ14cq9nM32n9m0S1HVinyXCPNo6Ih351f6DrpRkOMt_o9VcnKrS0HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuNV4O6zl1vmrrP1zeJQ1Bbj7MK5rFQaQbl2ArhZTWT7JgMfVEgYNNmlv5Z7zbgC_f_3LZieyz9-ImPvKke59OeeruZXKGfbzZt3g6KjIRYrL1FW6bXrl6PuYZ0QDApMN2XwRFp0q1pD7XrDgcOYIJ23Ojtcm_kcfPraEfAM59S9l-yE82O4xh8D2BLwxJBiiG3cE1XUPI6PJ5sbiJ_8ZTMWm89wsFNvl63moZxTijgc-MUkkDmLh_1dcNGlGh0qAG0RH3X_UPIPHi2p5572Yf06eo7CFz2-A0gUFHvz8Xy9Ae0eIUfYfRR9QcK9EZAonYPZcp43gvJ9NExIo5gMEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار فرمانده قرارگاه خاتم‌الانبیا با خانوادۀ شهیدان نصیرزاده و دره‌باغی
🔹
سرلشکر خلبان علی عبداللهی با حضور در منزل سرلشکر شهید نصیرزاده وزیر فقید دفاع و سرلشکر شهید دره‌باغی معاون شهید آماد و پشتیبانی صنعتی ستاد کل نیروهای مسلح این دو شهید را اسوۀ شجاعت،…</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/439610" target="_blank">📅 11:16 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439609">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwHvp_f5ctdEgb70bd1mFyWgTs0NnGE5Gmuy0SknGLFm1697pq9XAz_ARlp26lpguaKAfS9CEMFt3t2duBHtoIFy74sv9M2esNQy6iGOOLLL1eXwHLcyIpWBERTWp8KMDatjn_ZY5cXVCm9P7S5AhwmQ55QXEEkVLYxfSKqIX8tARRkOK2ZVmsXx1pLrfDEzAUoW41Pqq5B73QjFk76aM_lgug5SMWSfpSTe3HS7v_Pa-wjCl9rMONbZG4Xpqgo_O1Q6mXv2cPT6zmX6y2k-X-66y04-tQ8uXL887NDtPyjeXYlinRHz8D7vsH--A77MJl_FNuXTbYom8dujSlcSNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان هفتهٔ طوفانی در انتظار تهرانی‌ها
🔹
براساس تازه‌ترین داده‌های هواشناسی، از بعدازظهر امروز تا اواخر روز جمعه پایتخت و شهرهای اطراف آن شاهد وزش بادهای شدید و خیزش گردوخاک خواهند بود.
🔹
در روز پنجشنبه با افزایش ناپایداری جوی، در بعضی ساعات با تشدید وزش باد و بارش پراکندهٔ باران همراه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/439609" target="_blank">📅 11:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439607">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/598fe58ddd.mp4?token=n4emXvsFDkhBcszIRhEGMpjxHFqQad15BziT8GBo4GRni5iL8sLvaeDOZ72EY6LDUD6fyCubfBYYlYF4eEt4Xbqv8UtxghSJo9ozo2zf726v1FqhSj-Z1bnzOWFwP3iiwyt2fWbGfKaJhyl_s6gpDyk9BBNVEbSPWN6-0YTme8PAJogOBP4dJi0FWp5DW5U2dOhmuw__uLJshugjZdaDIsgMlux1MZSk4oMwVuOHsprmGRMFPRXI8zByPveFh161oGxoxM4-bM8DLV0evjzkCUCxV1KE8WTIOU7CvbFI3s8oYTQQjtYNxGRJ04AXMGWJXTtro-nHXzILCuUZBZ0F1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/598fe58ddd.mp4?token=n4emXvsFDkhBcszIRhEGMpjxHFqQad15BziT8GBo4GRni5iL8sLvaeDOZ72EY6LDUD6fyCubfBYYlYF4eEt4Xbqv8UtxghSJo9ozo2zf726v1FqhSj-Z1bnzOWFwP3iiwyt2fWbGfKaJhyl_s6gpDyk9BBNVEbSPWN6-0YTme8PAJogOBP4dJi0FWp5DW5U2dOhmuw__uLJshugjZdaDIsgMlux1MZSk4oMwVuOHsprmGRMFPRXI8zByPveFh161oGxoxM4-bM8DLV0evjzkCUCxV1KE8WTIOU7CvbFI3s8oYTQQjtYNxGRJ04AXMGWJXTtro-nHXzILCuUZBZ0F1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ اوکراین به سن‌پترزبورگ همزمان با حضور نمایندگان ۱۳۰ کشور در این شهر
🔹
درحالی‌که نشست «مجمع اقتصادی بین‌المللی سن‌پترزبورگ» از امروز با حضور پوتین برگزار می‌شود، ترمینال نفتی این شهر هدف حملهٔ پهپادی قرار گرفت.
🔹
منابع اوکراینی گزارش کرده‌اند که این حمله همزمان با آغاز نشست ۴ روزهٔ مجمع اقتصادی بین‌المللی سن‌پترزبورگ بود که نمایندگان تجاری و دولتی ۱۳۰ کشور در آن حضور دارند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/439607" target="_blank">📅 11:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439606">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5667dea2.mp4?token=ffCYOC0mRKRhlS26HkEZOpnhuN7_mFViZFKBbHDD6XW3reWas42bYzA06cFjFhM67OtBzqNTDjI2cPIGtLZwoz4_LLrQAmXP_MsWK9dfMC0PlUgN4ca_m4B2BdTycWyR6DM9uhnMVPAlQVlRFY36p8iLSAFgdtD1ZOWXAeL9R8qnC3PbzGwn1u4Rc8QjS-EQCreZxqpz4Z-X7oegYUdWpoviU26Ao3T5o6AEaO16PtP5tWFKvLAxX9wxKoRfVT_VQZ2B9P8obyknw0Z55DijUvXBLXCzOUUS5gMPJLwmpqPvMU2uUDlawgliqQArdMPn7xEOy3B3vqp0E38ndlJGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5667dea2.mp4?token=ffCYOC0mRKRhlS26HkEZOpnhuN7_mFViZFKBbHDD6XW3reWas42bYzA06cFjFhM67OtBzqNTDjI2cPIGtLZwoz4_LLrQAmXP_MsWK9dfMC0PlUgN4ca_m4B2BdTycWyR6DM9uhnMVPAlQVlRFY36p8iLSAFgdtD1ZOWXAeL9R8qnC3PbzGwn1u4Rc8QjS-EQCreZxqpz4Z-X7oegYUdWpoviU26Ao3T5o6AEaO16PtP5tWFKvLAxX9wxKoRfVT_VQZ2B9P8obyknw0Z55DijUvXBLXCzOUUS5gMPJLwmpqPvMU2uUDlawgliqQArdMPn7xEOy3B3vqp0E38ndlJGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مردم در میدان انقلاب
🔸
مقاومت مسیر روشن ماست
🔸
لبنان همیشه پاره ی تن ماست  @Farsna</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/439606" target="_blank">📅 11:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439605">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f300d528.mp4?token=jVi9rxkPfofcyLphBuKKqwjaUgk8wFQ2pCSwHiI9x5vTSBKRfA3aEiiomEmqsIApI51omINsGL4XqZI8dBkagaR7gDHRnO6vZvHlPWVSV7I6SWou4MhCxrqDrYvrbpISWaHEDyMU3cWOVeX2z_VBfHla7q0yvbz4xkYTQS_VBY2Q7X-LEgftXcEODHwpUO5BVunAxnpyeSxhV_7IOkf9T1n88VGtyPUEc9yy0tVBZ3EpRcdzHAm89rB5NEe_nl4ljWp5bYiMExtuasP041UXc5piwvIcus3E4jB7fVrSdUfvnInMpHggQNZkNdFumZhcONXjyjkvRZsbAQ6QGGNahS8RFYuPhyeDQ3yEcWsmaqlxh_qkWGnetAtIRar5VXFt9AlDQTAd_V7hSDmjGxffeaaIcvwNqsE7xXJ_WPdIyd8BXVLnQdMO679L-LsLrRhZWgQ4YFgIIyYvUuh_1htoD_xDfpuPuk_qCwZKnmC6ze-QYHRaw6Ma-KuvTf7DXmBb37iNRbeCH5dgCP5x2L7LuPZk8X10K-Obnikg7dyzHR-HoYz0ifRV3q8F9pMvTg5H-9_vzP9dSMLWkNbBPRGlOFpPzKKEMRkRZmpJI6hMuNDWZEVxO7munb1s4NZAp8QKdtMbP04OsIipy3dTi4BlKp-KbO4TKG-7tw_wDyvQFtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f300d528.mp4?token=jVi9rxkPfofcyLphBuKKqwjaUgk8wFQ2pCSwHiI9x5vTSBKRfA3aEiiomEmqsIApI51omINsGL4XqZI8dBkagaR7gDHRnO6vZvHlPWVSV7I6SWou4MhCxrqDrYvrbpISWaHEDyMU3cWOVeX2z_VBfHla7q0yvbz4xkYTQS_VBY2Q7X-LEgftXcEODHwpUO5BVunAxnpyeSxhV_7IOkf9T1n88VGtyPUEc9yy0tVBZ3EpRcdzHAm89rB5NEe_nl4ljWp5bYiMExtuasP041UXc5piwvIcus3E4jB7fVrSdUfvnInMpHggQNZkNdFumZhcONXjyjkvRZsbAQ6QGGNahS8RFYuPhyeDQ3yEcWsmaqlxh_qkWGnetAtIRar5VXFt9AlDQTAd_V7hSDmjGxffeaaIcvwNqsE7xXJ_WPdIyd8BXVLnQdMO679L-LsLrRhZWgQ4YFgIIyYvUuh_1htoD_xDfpuPuk_qCwZKnmC6ze-QYHRaw6Ma-KuvTf7DXmBb37iNRbeCH5dgCP5x2L7LuPZk8X10K-Obnikg7dyzHR-HoYz0ifRV3q8F9pMvTg5H-9_vzP9dSMLWkNbBPRGlOFpPzKKEMRkRZmpJI6hMuNDWZEVxO7munb1s4NZAp8QKdtMbP04OsIipy3dTi4BlKp-KbO4TKG-7tw_wDyvQFtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراف صریح اپوزیسیون به پایان رضا پهلوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/439605" target="_blank">📅 11:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439604">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLe-2j9G_eVyrykNIBevuFz2EeJWCuEnOmkMo5vo27FL9TKjqA30VXCfBZAFllryyGq_c-xYE_VM0m5wIiSFhK2ftOC3BBjARrRZrPqYQjG1m4QoTwqZO6DorpMKaEmEluCP7B11wriDasUKNwZGNylR8CYEQW6FxcCkYTAQ7Sa2-kPhMWFH3l5Jz4AK-irhqFrw_0iHKrkPzJTPiiiszarfA_5OU2TAntaA8NQjTyb7BQpWaEmflUY2BinO_DJW9ptiH537FlzM6oy4LGFKvZjxLeTXpHMU39M-PFa20_1d4Ag5WVTXKi8FuuFWVDs6XLtk2elEZ5jofzg8KmNCKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم باز قدرت‌نمایی می‌کنند
🔹
مهمانی ۱۰ کیلومتری و مهمانی‌های کیلومتری در استان‌ها تکرار حماسه مهم روز قدس است. حماسه‌ای که تصاویر فوق‌العاده زیبایی خلق کرد و در پس این تصاویر یک پیام مهم داشت.
🔹
بی‌شمار امواج مردم ایران در بیعت با رهبر انقلاب صاحب‌قدم هستند و برای جبهه مقاومت جان‌برکف و استوار ایستاده‌اند. این عید غدیر شاید چندوجهی‌ترین و مهم‌ترین عیدغدیر در سال‌های گذشته ایران باشد.
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/439604" target="_blank">📅 10:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439602">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lLAr9GuTRXKTwysz33WENqjdek-ujeLITafkNbawbJ2o0AkSkul5Xl-6fjDStaZMi65KgJENOwI-482UsXCyAcjHjYUte-HN0ieinTa40LCQSl_H5sxZ-A6j1vr4oZU4BDGOA8D4beIpAHxXPmlcjrpfkfV1ZOhKvA1ejrEdwVBAkKvlaC-fgUSOjoWQuNwqM1cnXS3Z9F_jyaMgaq99U21EOJ9RM1vCEY2nUM038uEoWJfsLXw0hCaiN4bd9Bu2719cyDZkvNGFK5Cz2WiZa4fbg5XTuBdGT_k4XU6mJegQxschTe8FzlxgRTCR9gf7zBBiwAuZMGUicfBpdolQ-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqvjKZta5yMtUdIL440foiGvy6QLE_qrmcr5tCQNpucA94w8fv09SdyrlZh6daIaazObzvgfdWgYa-bSSQZwY533ZTQx-5yUx9Ee14RPU51IF1eO1Nh7F80PAMmNkWBj5OggxPiH16VIwdDfCUESvFg6rkoag8FB_-5f3n5GwokbgSitJnCKC6tvpFnGAD44jO-USQE99mthvpndulQlrboliL3-2nig5JvXe--Jqx9qSCQvJN_nPYlO0pQ2knue4RSJuPUSv804eolOPCXNT0fKT8IRxmyJS04Sia_sMTjOwqqmS7G-eGgol4SqqHxDAEUQrGP6QpLOS4sdhkMmAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار فرمانده قرارگاه خاتم‌الانبیا با خانوادۀ شهیدان نصیرزاده و دره‌باغی
🔹
سرلشکر خلبان علی عبداللهی با حضور در منزل سرلشکر شهید نصیرزاده وزیر فقید دفاع و سرلشکر شهید دره‌باغی معاون شهید آماد و پشتیبانی صنعتی ستاد کل نیروهای مسلح این دو شهید را اسوۀ شجاعت، تعهد و تواضع توصیف کرد‌.
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/439602" target="_blank">📅 10:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439601">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">صدور احکام جدید بازنشستگان تامین‌اجتماعی، از هفتۀ آینده
🔹
تأمین اجتماعی: صدور احکام جدید بازنشستگان از هفتۀ آینده به‌صورت رسمی آغاز، و احتمالا تا ۱۵ خرداد به پایان خواهد رسید.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/439601" target="_blank">📅 10:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439594">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YD93TD1s6-cOVxV-eCgPRaLAeaquaJOgh80-m9nCVBBpv6znYz0mQgtMlNIwTdm2v_m1XnK--55COUIpoC_4O5AuHnoIWUaCg5mXxycMDckxY46CZCDDTVuiAU0UEY8VcagWwFx_ryJvepeO9cYMxs9A0ZlXvAsQqjxHqxk0SoZALOKsUgPd8SsTHgx1ViK4I14r_ZrNG3-LkriMAS5ckq6CdkCXzK0W2cVVN92haOHkQ00Su-2GgVFcG5KqovlZgGLyeaw1xXvjSB8RPmG_3d6xnmKK_KAXSAP4I_k1xiszKOpfaLaM2e3o_gFJHDl1fhKlaoC76Lsa0raNiUgnTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAwBepa6zexfV59Pf53BmfLRxmJU79z8AgxpcLDV4MJHcJS9S3dE4NxbWm_9HwYFv8R8R4hZDoHbskqlXrxf0LSqJQLu-Y-Kbsx5Edu_qKJ8KsxHy7MzHca92uSKSmNvQx0hQi3Yaq_0WUJcIlxJy1DGenSn6rLQx7hUDXwe1ijWTlmvWgUfkh-RX3e5D5rEOu9GHtFKAcI_VK6_oxK-6SNOXSrIHLp63Ywrnhdeuz4RfpMLhSpB5acJMFizPcpDBWrVNyF2tlctkduXfkspJ6caSKwjVrocNbP_FxJhh7r7Q4tmwYeaHkp5doqnCkuLqE3Gu9ZIQZwvrjU0i9vDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vdolrgcBLFm7C4krRD524Fe8gpDuEgUebP2CFHLl_VO_Ckl-fPOVlywiQsadTgzwQJwiNAS633qHfxs99Dzec9ujRBxvRG_neJs6kioXHTrDngm88uLzBnj02rbcWcAtGRglRpMXoctgBSr2vuKdGJ7TEaNnwTgdqNI1Wx97OFcAqzO5OG7MMZqUw-oSEts4XddAA6-QMIr0Wrvzcb_at01wXzGLHgkTukqRKeDOPkssLiIR7Fv3IRxfZF-JMBu_nIRI9ShtCGj9v4BdMl_mOheij22zx7W6fD6j-wEmhDt-b9mrC9AghMqUHoh8u-LWhbpvOxuo6DT6uPmM4hiryA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzNJxhSfodHqtCjpecR6pfRI45wPp8BF5HtQ3PSTZVgmWMUZzls61jHetekISOsKWL8sU5iHw73-N1nsDVVsnhzDPc6_VK-MsrTbMP0mmTBloGQ38gE6yNL0PE-uIPLusyW14U5bPpmOuPJ5364aDI8SbtPdb2_qDxVNL2QTPwy58InDL7CYuqJYqEcXSNi_intEHNVi8ycuunnxxcnCvD-OG-tu9FOYtdljKTO3MJ1voD0o4oK-i_7_WgkbuefY7qGxpMMHmZC7j1Ptx2I2YM_gSLxFs8g2af0ankh9yP83Lg7Gtt1Rqi01ezH-U-oF5mUCG1OBJtHCoSzVW-n_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h2H2FTT18iWDahCsDwcfsYl6od9pBJQ4hUSRs5HXRvNuW7vw4mjD3zl5DyCzrWC1LeKUn2hu2bi_6icqPGU07iZXvsxWfA0oZ9QSfkd7hIDqjsmkZv8aSXSioM3QIDewQpYNSCswEUMVyVd3Frq083Lrz2iVOrZWrtLcb-eGRfqbqeEIzhpNLLeIaxHTFNlpR2ZLXMbaF4Icq28wgnLdt811GTdctkyIQNRavDqG1Udswq0upRry9KZ_7dmF2PdzF1FBnh186WJqYxLB8on2bIK7FeML7IwwcV_eIIICY4En54awd-B0ghEjU7TuVRvFBzEl_giL--QOiXdZx05arw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K2B5twrB2evE_uLmXuQyDRASmgVF615ikmYEhp1lYKh4FiZ02L3cXIWzXaTpBYTqTmNXL8RNnVt78cUxCVj2vAYtW1juWyEPpDbuPahyj35_b7SR37qZzhzxS97Ue8RUfCuvezwEAUPI8CbXvvHLfHLzDbVssaPMZFdI2RleXXzf_2Juyz4R18HtpRjWaQdGKk8Vkew0wJvGQcbPUn_artnkMirgdVvLXTLhCxCq0VQlnaToxSNXq7s3E900cIiDc05SLF4-5vSFQL4mWlNNB4Z0CYcUaUjQzmk5BxFkoHnpzCyc9-H5urJrQBKeDSe08D4bGVpUFFnTEQFnAl0NRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q_eltr_pzVaW6DqiFf7P2HZupe0Dv1g1eMd9A5ltkb2rR7_-mBgOKted7JlM7d2kjhwattSJcPd_AUWkry9lhRCN-Zw1lg19_p5b5H3RAgW8oQ332Or7OuIqW6JYvg3zbqrLq_ONS-KMgBCkMP0yFrKLADSVA_4X4OFaryHfAMv0sc9XN1jQrOIKNB8jviXcyqE5Jyn-i9XT28QyRPE7Q_ag3uHMKui3rG8wpJqen2sR3eQJguX3TR97GBIL2cU2wXJJ31ZR72XEFfj7dpIDEIixYL0VciU1UpTcojx2pdXoWlDSYuKhjTTQ9sAWzSOG1TJiRNlVOgaUSUC0S49Vwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار اعضای دفتر رهبر شهید انقلاب با خانوادۀ شهید نکوئی
🔹
حجت الاسلام ذوعلم و محسن پاک‌آیین اعضای دفتر حفظ و نشر آثار رهبر شهید انقلاب، با حضور در منزل پاسدار شهید مصطفی نکوئی، به مقام این شهید والامقام و خانوادۀ ایشان ادای احترام کردند.
🔹
شهید نکوئی در اثر حملۀ هوایی رژیم صهیونیستی در اولین روز جنگ رمضان در بیت رهبر شهید انقلاب به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/439594" target="_blank">📅 10:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439593">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0fUkYHXsw6soR3eBEo12BtRwSw99fkliWOrUq9zNzaLVn3LWGknvS1ytjFDblMbYqEADSATPrUAbXZIPwwJzpkwWjTnh_90l_jVd-Xq2dVlJLHgdvFeqAzAQ3UpHjNd4CN_dVyID0bDmSi4xrmODxddiZ8Xpy0RhYTYio_9BI9sbem8AvobRfC5E1A16eiqlghfrI8cpEIRt7KG-0xUQh5yYAFzyIIvC8YUSSa5noDPIb6O7oOoN5lFr2yYVxBAS-vZh82viuGkseaFf_x1uVFHBPG3gVm1W463RZhsTSKcyhDN20xjIWjhi9JMYeP85trQrg0ZbP2r7NaKKINYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارش‌های سیل‌آسا در راه ایران؟
🔹
مهدی زارع، کارشناس زمین‌شناسی: ایران در پاییز و زمستان امسال ممکن است تحت تأثیر «سوپر ال‌نینو» قرار بگیرد، پدیده‌ای نادر که می‌تواند بارش‌ها را به‌طور چشمگیری افزایش دهد و خطر وقوع سیلاب را بالا ببرد.  ال‌نینو چیست؟
🔹
ال‌نینو…</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/439593" target="_blank">📅 10:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439592">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‌ ابلاغ سهمیۀ بانک‌ها برای وام ازدواج و فرزندآوری
🔹
براساس ابلاغیۀ بانک مرکزی به شبکۀ بانکی، در سال جاری ۴۳۵ همت تسهیلات قرض‌الحسنۀ ازدواج و فرزندآوری پرداخت می‌شود که از این میزان ۳۵۰ همت برای ازدواج و ۸۵ همت فرزندآوری است.  @Farsna</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/439592" target="_blank">📅 10:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439591">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اجرای محدودیت‌های ترافیکی در جاده‌های شمال
کشور
🔹
پلیس راه مازندران: به‌دلیل افزایش پیش‌بینی‌شده حجم سفرها، محدودیت‌های ترافیکی از ۱۳ تا ۱۶ خرداد در جاده‌های شمالی اجرا می‌شود.
این محدودیت‌ها به‌شرح زیر است:
🔸
ممنوعیت تردد موتورسیکلت‌ها در جاده‌های کرج-چالوس، هراز و سوادکوه از ظهر امروز تا ساعت ۶ صبح ۱۶ خرداد
جادهٔ کرج-چالوس:
🔸
ممنوعیت تردد تریلر، کامیون و کامیونت
🔸
یک‌طرفه‌شدن مقطعی در صورت سنگینی ترافیک در چهارشنبه، پنجشنبه و شنبه
🔸
منع ورود خودروها به سمت چالوس از آزادراه تهران-شمال از ساعت ۱۲ جمعه و یک‌طرفه‌شدن مسیر مرزن‌آباد به تهران از ساعت ۱۵
جادهٔ هراز:
🔸
ممنوعیت تردد تریلرها، کامیون‌ها و کامیونت‌ها (به‌جز حاملان سوخت و مواد فاسدشدنی)
🔸
محدودیت یک‌طرفه مقطعی بین پلور و پلیس‌راه لاریجان در صورت ترافیک سنگین
جادهٔ سوادکوه:
🔸
ممنوعیت تردد تریلرها (به‌جز حاملان سوخت و مواد فاسدشدنی) در برخی ساعات چهارشنبه و جمعه از مسیر جنوب به شمال در صورت افزایش ترافیک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.88K · <a href="https://t.me/farsna/439591" target="_blank">📅 10:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439590">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TvHCG5OyTY2BvcEJpZff5p5769c-0vcUFznKby-wGFacZLTQICof1e2pQAENcGhXXS_-GqQw3p9igDHYp9pgMHsLJZJIu1NE4kAuBeCj9ZdW3UKyC_UjXVVYZX3JNXJn1_KSaU6v7E-CMd-m9NfA0wP1XezxpIe5Jp14DDMbwaWRq8JthA2QqQMZ22cDINR4VOpnXc02VvFlu4rYERpxv50Xs-tjwXmBh_fiv9uRr3F89VANJQgzwnPR0oz6_uXQmcp2Nwnv1oYfQLPIx51Fc7ggOF76a8a2pdFu1ZnIgovQMEL4aZDPx1rnpMv8LCEoaZu7Uzh4u0-1yR7737zidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشد سه‌رقمی شاخص‌های عملکردی پیشخوان های شهرنت‌ بانک شهر / استقبال از کارت هدیه افزایش یافت
🟡
پیشخوان‌های شهرنت بانک شهر در اردیبهشت امسال با وجود محدودیت‌های عملیاتی ناشی از شرایط خاص، در شاخص‌های کلیدی عملکردی رشد سه رقمی داشتند. منابع مستقیم ۱۸۲ درصد نسبت به مدت مشابه سال قبل افزایش یافت و مبلغ صدور کارت هدیه نیز با رشد ۱۰۹ درصدی مواجه بود.
🟡
به گزارش روابط عمومی بانک شهر، در بازه زمانی اردیبهشت ۱۴۰۵، بخشی از پیشخوان‌های شهرنت به دلیل شرایط خاص عملیاتی، با محدودیت‌هایی در ارائه خدمات مواجه بودند. در حالیکه در این دوره حدود ۱۰ درصد از پیشخوان‌ها به طور موقت از چرخه بهره‌برداری خارج شده بودند، روند توسعه و رشد عملکرد شبکه شهرنت حفظ شد و شاخص‌های کلیدی این پروژه بهبود یافت.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/439590" target="_blank">📅 10:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439589">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9LBg7Ew4IW4yRo-g31S1ruR9JCJTM-5cU5UFP9ySvr3dlnyhTQNo5Av2wuNpfXXwROnDRqYlq-wGwSBy85bWArUoTm16Wxn-xDiUfkjAPEgP2mHHFS_ytqppFceO6jRVoPH9-w3XjnnNwJJdMzcxYW8-vHtHoDr2029-yU715e_FhlMu_qBJ5aGYN9hejKyWfcvmtjyoz-au4avqB2y7AuZ5jfzDhZ3mq4OUpgoV17G-hLtqoRsMAxcRQW0z0DccP1UT4XQnl3Ftd8dZvdsHRbpfGVpjfwAZFqUGHW2NT3r8tCRMkQjBwgrt_dR5iNZRopzVdQ1c_EdP8Kn_1gFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه ملی فن‌‎آفرینی تاثریا برگزار می‌کند:
❇️
بیست‌وهشتمین *رویداد ملی تاثُریا* ، با هدف توسعه اقتصاد دانش‌بنیان.
🔹
*استان‌های میزبان: * قزوین، زنجان
🔹
*موضوع:* شهرک‌های صنعتی در مسیر اقتصاد دانش‌بنیان
🔸
*محورهای رویداد:*
۱. اتصال شبکه فن‌بازار به کلینیک‌های کسب‌وکار
۲. ارتباط صنعت و فناوری
۳. شهرک صنعتی هوشمند
۴. صنعت در مسیر اقتصاد دانش‌بنیان
۵. توسعه صادرات دانش‌بنیان
📅
* زمان و مکان برگزاری* :
۱۷ تیرماه ۱۴۰۵ | به میزبانی استان قزوین
🌐
*اطلاعات تکمیلی رویداد* :
tasorayahub.ir/events/event/qazvin-zanjan-tasoraya
✴️
*قابل توجه فناوران، نوآوران و کسب‌وکارهای دانش‌بنیان:*
علاقمندان، فعالان حوزه کسب‌کار فناورانه، نوآور و دانش‌بنیان در "سراسر کشور" می‌توانند محصولات فناورانه خود را جهت اتصال به کارخانجات صنعتی حداکثر تا تاریخ *۱۰ تیرماه ۱۴۰۵* از طریق وب‌سایت رسمی شبکه ملی فن‌آفرینی تاثریا ارسال کنند.
🌐
tasorayahub.ir
#تاثریا
#رویداد_ملی_تاثریا
#شهرک‌های_صنعتی
#دانش‌بنیان
#سرمایه‌گذاری
📫
هلدینگ پیشگامان
📢
@Pishgamanhub</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/439589" target="_blank">📅 10:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439587">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/439587" target="_blank">📅 10:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439586">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🎥
پهپادهای شاهد ۱۳۶ سپاه پاسداران در آسمان کویت  @Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/439586" target="_blank">📅 10:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439585">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFcEJYZEDPybsU-TmHqZQN_tQPL7cmNpoO2Kuqf5LMmQ1r-PPQt3UZslGXpZOcgkHbdrFx7DFt1aBKvJty6XnhwP1ters7w2SvwMb0MZTnvegTKmnxOJ007EYGfq16QAxg4XGysGhlmAysnsxVMODHOAy4anv-vXACMV9fnZqVhYhryqzjZPt3ivB7is4bk9V77neUqtoeLHUFOYDZPNiNQ1kpL9WmtAuse9YYu8A4M6L93i0EPGhfDjX-Iab3gohndeAeXizBt5S-TwcM7WIqvVqtA7D25GkPswnCHt2Mmr4lINIC22U12bklAYcGbahaDeMqzR9Gt5ZPigFk5K8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مهمانی ۱۰ کیلومتری غدیر، فردا از ساعت ۱۵ در تهران آغاز می‌شود
@Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/439585" target="_blank">📅 10:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439584">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ارتش صهیونیستی هشدار تخلیهٔ روستاهای ارزی، مزرعه کوثریه الرز و زراریه در شهر صیدا در جنوب لبنان را صادر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/439584" target="_blank">📅 09:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439582">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">احتمال شنیدن صدای انفجارهای کنترل‌شده در دزفول
🔹
فرمانداری دزفول: درپی امحای مهمات از ساعت ۱۰ تا ۱۲، احتمال شنیدن صدای انفجار وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/439582" target="_blank">📅 09:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439579">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2379837c74.mov?token=h6fwYH2RZp5c7q_6No3_Ji45SRaBF0rP-uCJaPTSUsLEFn4AsroF97bHZNuxdIMgcwsnG26AwxN5jcntgY6TbY4Yg_HIZaeHw_YfDrJLQx9LsixT5-IZWUfRhMa4dXMutILLG_8VU0oCUn_uTLB5HyQybDciNkJzTj8qvdZHMm3J16hMHYgdVaJv2nSPGyQ1S8BuYd803CqGztEisPuiVGB4k7kuAEKT7MmoXcX5wq6nN496hrO4sus6525wuBlCknPxZ6GE6DVV_Rok85eaSEwRoo10TfJWQpn0MgYOv--cFeDdrJ8dh1B8rEY2pl3QSzv20rEbCU2SkJR7kjhVRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2379837c74.mov?token=h6fwYH2RZp5c7q_6No3_Ji45SRaBF0rP-uCJaPTSUsLEFn4AsroF97bHZNuxdIMgcwsnG26AwxN5jcntgY6TbY4Yg_HIZaeHw_YfDrJLQx9LsixT5-IZWUfRhMa4dXMutILLG_8VU0oCUn_uTLB5HyQybDciNkJzTj8qvdZHMm3J16hMHYgdVaJv2nSPGyQ1S8BuYd803CqGztEisPuiVGB4k7kuAEKT7MmoXcX5wq6nN496hrO4sus6525wuBlCknPxZ6GE6DVV_Rok85eaSEwRoo10TfJWQpn0MgYOv--cFeDdrJ8dh1B8rEY2pl3QSzv20rEbCU2SkJR7kjhVRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست خدا و نفس پیمبر فقط علی(ع) است
🔹
نصب کتیبه‌های عید غدیر در حرم مطهر امام رضا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439579" target="_blank">📅 09:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439576">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6ff7172d.mp4?token=p7T9Anj3DPn9rjhIvvX80fFpYHPsAgvWoClSsG2QhHqtZUCFY_xZ3X5Fqa48ODchYVUIBRaQyIXzwaw0OmIvd06jLv2BmidnnAzJHlswP6XNPVITY9YyPHWiyYJFVbcW6E9u6ZL52nGBSc9-pSr0Pn7EZB9V8924hv6JwSZqJ9SckGltFHCtTftrlIO2e-ryulsOqnYnKty_hopF6TcCO-1uB93zgjkDXsewcneGvaIp615iLTi1SwSnU8sjU_Ce99Eo0zB_yCuwk72y0zI8v9tCZLJs9jTBwWX-KDjXSdagCLaiVbG2CveigxdnmRYxNDi0l_tFmNQlc0WQi3EiMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6ff7172d.mp4?token=p7T9Anj3DPn9rjhIvvX80fFpYHPsAgvWoClSsG2QhHqtZUCFY_xZ3X5Fqa48ODchYVUIBRaQyIXzwaw0OmIvd06jLv2BmidnnAzJHlswP6XNPVITY9YyPHWiyYJFVbcW6E9u6ZL52nGBSc9-pSr0Pn7EZB9V8924hv6JwSZqJ9SckGltFHCtTftrlIO2e-ryulsOqnYnKty_hopF6TcCO-1uB93zgjkDXsewcneGvaIp615iLTi1SwSnU8sjU_Ce99Eo0zB_yCuwk72y0zI8v9tCZLJs9jTBwWX-KDjXSdagCLaiVbG2CveigxdnmRYxNDi0l_tFmNQlc0WQi3EiMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گروگان‌گیری و تهدید به بمب‌گذاری در کالیفرنیا
🔹
پلیس شهر بیکرزفیلد در جنوب ایالت کالیفرنیا اعلام کرد یک فرد ناشناس که احتمال می‌رود کمربند یا جلیقه‌ای حاوی مواد منفجره همراه داشته باشد، تعداد نامشخصی از مردم محلی را در ساختمان یک بانک گروگان گرفته است.
🔹
پلیس آمریکا در ابتدا پس از دریافت یک تهدید به بمب‌گذاری در بانک چیس در نزدیکی خیابان چستر و خیابان هفدهم، به محل اعزام شدند و سپس با ایجاد یک محدودهٔ امنیتی گسترده، عملیات مدیریت بحران و مذاکره را آغاز کردند.
🔹
سخنگوی پلیس بیکرزفیلد اعلام کرد که یکی از گروگان‌ها آزاد شده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/439576" target="_blank">📅 09:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439575">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارهای کنترل‌شده در جنوب اصفهان و بهارستان
🔹
مدیریت بحران استانداری اصفهان: انفجارهای کنترل‌شده مرتبط با مهمات عمل‌نکردهٔ جنگ رمضان در جنوب اصفهان و در محدودهٔ شهر بهارستان تا ساعت ۱۰ امروز انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/439575" target="_blank">📅 09:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439574">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
تصاویری از عملیات حمله به ناوگان پنجم دریایی، و پایگاه هوایی و بالگردی ارتش تروریستی آمریکا   @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/439574" target="_blank">📅 09:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439573">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🎥
فواد ایزدی: آمریکا به‌دنبال عادی‌سازی حمله به ایران است
🔹
کارشناس مسائل بین‌الملل: کاری که آمریکایی‌ها می‌کنند شبیه آتش‌بس در غزه و لبنان است. حوصلۀ ایران همیشگی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/439573" target="_blank">📅 09:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439571">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0876c332eb.mp4?token=ufVZd860gDwOTY38hMvimkAoN2NF673kWJOHgBEsCUaneQV3ewIHWWHBaMv69uKv9OpQn8TdYCJvjCLQR8DerbYDh3IO2DoKPnAtRAFnVy8cFyvKW4PDk1_pbcaMiqj7mNxBfF8EhVnqXyUsYPY-gOTt88w9H3riWGeDhrLkNIR0eVCFHCdCUf3qKGrVg4b6LDhigtl32khqfVCo7Hx7_Jgq2WN4yCeuHpK4fXGdy9dRUeaq2pc3Dlsxp5jty5hM5C0t-dW0_aYaK4VAJHTzzojuupWqNUASRN0XEOp3_jnUAc_G4v6y-cDP7w68H3Y0Ujz3tA5E1DWLdzw0QaCMtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0876c332eb.mp4?token=ufVZd860gDwOTY38hMvimkAoN2NF673kWJOHgBEsCUaneQV3ewIHWWHBaMv69uKv9OpQn8TdYCJvjCLQR8DerbYDh3IO2DoKPnAtRAFnVy8cFyvKW4PDk1_pbcaMiqj7mNxBfF8EhVnqXyUsYPY-gOTt88w9H3riWGeDhrLkNIR0eVCFHCdCUf3qKGrVg4b6LDhigtl32khqfVCo7Hx7_Jgq2WN4yCeuHpK4fXGdy9dRUeaq2pc3Dlsxp5jty5hM5C0t-dW0_aYaK4VAJHTzzojuupWqNUASRN0XEOp3_jnUAc_G4v6y-cDP7w68H3Y0Ujz3tA5E1DWLdzw0QaCMtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از عملیات حمله به ناوگان پنجم دریایی، و پایگاه هوایی و بالگردی ارتش تروریستی آمریکا   @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/439571" target="_blank">📅 08:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439570">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b66b238e.mp4?token=QhBTMydKHTB0D0wkz842wBgVHSV-ibbh7mctBGNrNyPrXlMbeOzkvp5ZqcuaJRNISJEf04Fu7dkUGY5p3TklpQz1NQbG8Z-w_-OlyJCDBG1oNN8PjXfM2Tr7LI23URXzydAQ4-LKL1wue8byjKTl-ggRQ4aJ3LcnY60mS5-mEi23cx-Ug3yjhY00SLhnmBBUwTcpqtt1GorgM1LpT3XOdGlyvlhbMK1n-yjzM2THSKs7KQGOGS2yXcHoTRfg5GCeApyNN1b8VXpxlGCQsrbNbt-4_24YbQS68nMPsB5MoJ915niHzXB5gA863Zq7cBKl60nD3OJfFu2Q4z0qpJhupw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b66b238e.mp4?token=QhBTMydKHTB0D0wkz842wBgVHSV-ibbh7mctBGNrNyPrXlMbeOzkvp5ZqcuaJRNISJEf04Fu7dkUGY5p3TklpQz1NQbG8Z-w_-OlyJCDBG1oNN8PjXfM2Tr7LI23URXzydAQ4-LKL1wue8byjKTl-ggRQ4aJ3LcnY60mS5-mEi23cx-Ug3yjhY00SLhnmBBUwTcpqtt1GorgM1LpT3XOdGlyvlhbMK1n-yjzM2THSKs7KQGOGS2yXcHoTRfg5GCeApyNN1b8VXpxlGCQsrbNbt-4_24YbQS68nMPsB5MoJ915niHzXB5gA863Zq7cBKl60nD3OJfFu2Q4z0qpJhupw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: کسانی که می‌خواهند به شمال بروند، فردا و پس‌فردا منتظر بارش باشند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/439570" target="_blank">📅 08:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439569">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4702f8e30a.mp4?token=nJ0WS-cvHHUWsOp4hFF-KAAJt_A-wdzmQHwd_8B3xz_f2qjlBoDjGSVjz41OcqNVdsHXRUO7KUVowo1HV2WllPg8kbSR3pJdVkWpgjyTI0IKCcOCrabh_V6MN0d9FxTUoGP1C53743juekYrIk_iqOW52qFDiyKU8gXTSC36VKasvU8q72NRyDAPjhKwexPeNAouaMVNkGOkpV-dL6nHf7lFgxTQoVz62K6fGo_0gEp6C0D2S784R3WdcnNFIrXN1h1tShb-sPBEMmKtDqCQODZ95UtK4qAWpje0AGUWiyv2YG2v1f2lL31V61ZCXXkqHBSug1ePqtPV1NuPranIvJrr00JNzBP9tU3F7zrWA2XUqD1BM4Fq4-EImgt-m_7gzLh-cylnYbdJ0glfi_boh9X9JmpiJlZQPmH_L5VAgBLg9xuMIx00stmQfY5qX1cJUweJ_YeN-MSgBzAXryQj_R-jvDkUCr8vFm2N0bKvghRpBFIrrZk_nLPtUHmQGja7GkAfXFGEJQURb7MC4GqmiHXNDZB8SA1MDGzABR_VXOV8KbFR2mZJHKo63snoNjWvMPND9NI6eJvJVeLMy9XAaob1rc1BC4ye9EaKsTgYKb9z-q8IigdkD3vC2Uua3WyT0zVRWuY6hXackAViQlKVL2jmPJVhfjqESixokfxOnf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4702f8e30a.mp4?token=nJ0WS-cvHHUWsOp4hFF-KAAJt_A-wdzmQHwd_8B3xz_f2qjlBoDjGSVjz41OcqNVdsHXRUO7KUVowo1HV2WllPg8kbSR3pJdVkWpgjyTI0IKCcOCrabh_V6MN0d9FxTUoGP1C53743juekYrIk_iqOW52qFDiyKU8gXTSC36VKasvU8q72NRyDAPjhKwexPeNAouaMVNkGOkpV-dL6nHf7lFgxTQoVz62K6fGo_0gEp6C0D2S784R3WdcnNFIrXN1h1tShb-sPBEMmKtDqCQODZ95UtK4qAWpje0AGUWiyv2YG2v1f2lL31V61ZCXXkqHBSug1ePqtPV1NuPranIvJrr00JNzBP9tU3F7zrWA2XUqD1BM4Fq4-EImgt-m_7gzLh-cylnYbdJ0glfi_boh9X9JmpiJlZQPmH_L5VAgBLg9xuMIx00stmQfY5qX1cJUweJ_YeN-MSgBzAXryQj_R-jvDkUCr8vFm2N0bKvghRpBFIrrZk_nLPtUHmQGja7GkAfXFGEJQURb7MC4GqmiHXNDZB8SA1MDGzABR_VXOV8KbFR2mZJHKo63snoNjWvMPND9NI6eJvJVeLMy9XAaob1rc1BC4ye9EaKsTgYKb9z-q8IigdkD3vC2Uua3WyT0zVRWuY6hXackAViQlKVL2jmPJVhfjqESixokfxOnf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ رنگ پرچمت زیباست ایران
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/439569" target="_blank">📅 08:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439568">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1460006634.mp4?token=czzqrVEiYqZS8k3UW73HL1bOWG5XI6hejtku-Jhb3XivNvNKzixs7DWoaoKE3USajvRhn-NbVATsWZRVdZDSN_E8UhUhBEB8N1kikWyM8MquOsaVALBCzbOpv2NFS2_38Vbd0C4FNA9MHzDE8QcjWcrbX2AChLCOnJxtaKRL-YoBMshhvd6gDnLo7becPvLf-YDNWMCClO-9Ez_kfTUhQ-s0HaOJJ0TluNMrZ4J7K1I84o_4Frfc5vj7shshNhd6o_Eb6t3TN0APSBpxuLPbhJALaAwgzoVB6OcxgygTi2Ei7xnldmXmqFe7TETJKQimWgAIymTSXhbRO2w7JZ_X4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1460006634.mp4?token=czzqrVEiYqZS8k3UW73HL1bOWG5XI6hejtku-Jhb3XivNvNKzixs7DWoaoKE3USajvRhn-NbVATsWZRVdZDSN_E8UhUhBEB8N1kikWyM8MquOsaVALBCzbOpv2NFS2_38Vbd0C4FNA9MHzDE8QcjWcrbX2AChLCOnJxtaKRL-YoBMshhvd6gDnLo7becPvLf-YDNWMCClO-9Ez_kfTUhQ-s0HaOJJ0TluNMrZ4J7K1I84o_4Frfc5vj7shshNhd6o_Eb6t3TN0APSBpxuLPbhJALaAwgzoVB6OcxgygTi2Ei7xnldmXmqFe7TETJKQimWgAIymTSXhbRO2w7JZ_X4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار خودرو در جایگاه سوخت‌گیری تهرانپارس
🔹
سخنگوی آتش‌نشانی: صبح امروز خودروی نیسان در حال سوخت‌گیری در جایگاه سوخت گاز واقع در بزرگراه یاسینی بود که به‌دلایل نامشخص دچار انفجار شد.
🔹
در این حادثه دو نفر مصدوم شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/439568" target="_blank">📅 08:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439566">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZYIFPhL2izOomGCtNQ74feGx5kT_82Ur2ag3b18iPlQmBJCUGX4dj1CC_dFUwJIFacOB7XoyAXmVjMwBClLX6mwvXidaoPR8QttlkUrgYs3fJSICFnqBTzypyQt3SekDLrpFiNYUJKibvHKtS49BQS30xYoIcKmX7yM0lMPLlxjZv8S7elgQMnOOEngzlhCYaPT94XoDHxO3oBNHuH0LPCuNdti34pdZj2AHAixJxugGWZ6yEZduDoSrb0l6NPH8V3DI4_NdKUqh8c62gjhVMtTFYCZXVBdWRgoz0rM9HIDB9CGCqd--EGWUZXQo0pI5svEMf5ks-24E5J67FLYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ هزار مدرسه به پنل‌های خورشیدی مجهز می‌شوند
🔹
براساس تفاهم‌نامۀ جدید میان سازمان نوسازی مدارس و سازمان انرژی‌های تجدیدپذیر، ۱۲ هزار مدرسه در کشور به پنل‌های خورشیدی مجهز خواهند شد.
🔹
در فاز نخست، تولید ۶۰ مگاوات برق هدف‌گذاری شده و اولویت اجرای آن در مدارس مناطق کم‌برخوردار، مرزی، شبانه‌روزی و آسیب‌دیده از جنگ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/439566" target="_blank">📅 07:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439565">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8daabd898.mp4?token=Le_6WrJOPhvaaySliWCAxzRTaTEUxK3DdweFE7b65By0OYxolnRJsv16A6vdq8Y5OK1JjZSd-rD0aRJXimp-IvpCrRjVaBd_XecTjeBiBx0RXiY2MFv41SOsGcaKJwfyQ633sfQ-jNGo5Lzu0Wg_evMKL67GQQDZw6E_d2FcqVc46WqElf-8zpvtneQMbCNfWEDQhL2KUfqqlUAZjdf7RswV-tmMenHpGwvJU3XgXlBhIvCtVaqlkhwW8lhZTwc5SNzacBlnf9z3sAIDIBeQU6_6xL67sGBsiY7MeJ_0gRnDvFPUAdlq5kotqYRSJrEBrTNc1aHhEUCcyMSs3vhLwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8daabd898.mp4?token=Le_6WrJOPhvaaySliWCAxzRTaTEUxK3DdweFE7b65By0OYxolnRJsv16A6vdq8Y5OK1JjZSd-rD0aRJXimp-IvpCrRjVaBd_XecTjeBiBx0RXiY2MFv41SOsGcaKJwfyQ633sfQ-jNGo5Lzu0Wg_evMKL67GQQDZw6E_d2FcqVc46WqElf-8zpvtneQMbCNfWEDQhL2KUfqqlUAZjdf7RswV-tmMenHpGwvJU3XgXlBhIvCtVaqlkhwW8lhZTwc5SNzacBlnf9z3sAIDIBeQU6_6xL67sGBsiY7MeJ_0gRnDvFPUAdlq5kotqYRSJrEBrTNc1aHhEUCcyMSs3vhLwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مرکز ناوگان پنجم دریایی آمریکا مورد تهاجم موشکی و پهپادی نیروی هوافضای سپاه قرار گرفت
🔹
سپاه پاسداران: در اواخر شب‌گذشته ارتش متجاوز آمریکا یک نفتکش ایرانی را در حوالی تنگۀ هرمز مورد اصابت پرتابۀ هوایی قرار داد که این نفتکش از محل موتورخانه دچار خسارت گردید.…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farsna/439565" target="_blank">📅 06:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439564">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🎥
روایت نفس‌گیر آتش‌نشان فداکار و نجات جان ۱۵ هموطن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/439564" target="_blank">📅 06:03 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
