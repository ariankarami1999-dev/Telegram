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
<img src="https://cdn4.telesco.pe/file/P188c6ks6rkT5Ja_bHCdfIzk3UpLqLIGVsUlnHYVGSqbJpdaqLK2ViVZhAgHNWnNP7lc02s5ZJUU03ZhWAtqbVfdHMxsOL5rbkgW5qfeMq8LRdjowyQujaLKv7yYqJjVD53W5usaGfRVY_Qt4b9YzBrL7czuarcJzqGWLRFTezGQbmy5LDFDiuVGrmFYkxmZJcJqycj93_8Af2NLJFeyfYOfR9cUwk6beWXI9qNiD-UwlTP_jLuwltRBa2tuc3RW9tyzBtoM6QJzNMnQSafdjW44Veh1PNSZtMx1o_v742gd54m-OGWSwonjsZVRRQO0pEQ3ti_GU1SMbHCVZj19BQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.26M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 16:26:06</div>
<hr>

<div class="tg-post" id="msg-656841">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تصاویری از انتقال مجروحان به مراکز درمانی در حمله وحشیانه رژیم صهیونیستی به ضاحیه بیروت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/656841" target="_blank">📅 16:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656840">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
بیش از ۳۰۰ نقطه از آثار تاریخی ایران در طول جنگ آسیب دیده‌است
خسرو معتضد، تاریخدان:
🔹
بیش از ۳۰۰ نقطه از آثار تاریخی ایران آسیب دیده یا نابود شده‌است.
🔹
هدف این اقدامات، تهی کردن ایرانیان از هویت و فرهنگ خودشان است، این بمباران اماکن تاریخی حماقت است؛ هیچ‌کس تا به حال چنین کاری نکرده است.
🔹
ایران با مردم یهود دشمنی ندارد ، ما باید در تلویزیون برنامه های عبری داشته باشیم.
🔹
کاخ گلستان فقط یک ساختمان نیست؛ بخشی از تاریخ سیاسی و دیپلماتیک ایران است./خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.23K · <a href="https://t.me/akhbarefori/656840" target="_blank">📅 16:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656839">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4706c6d2d4.mp4?token=VIOfALuI3V1vBQ7Cb3rD0BehFYTweMB6fBU74GqDFsb5Id-9poBCmf0hGrgbmqki-bJBVg1qGwBeOASEpFYIq-b7hlaxOJTSFkEbvWR13HfPa2N6sicgz9WcXZNihqow5FUvxSmJq9X7Yxz-94BsGdfPyHTQWrnELJcaEIZ145gjzGY8cWl5gpG6hZ2kkRzEnFthT8HGUSnVg4L-PmR7pd1pPz0UbDbmPRdOfx2aOOBtdLjuP_iPBGOGXb1RZElgk9rLik1a3EdBmyHWX2gkXn5xJ-4EQjsukDOiGY9I9SONsalQnoOqt_GeYP0dndsZlVcIRAACLYidl936iMYe-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4706c6d2d4.mp4?token=VIOfALuI3V1vBQ7Cb3rD0BehFYTweMB6fBU74GqDFsb5Id-9poBCmf0hGrgbmqki-bJBVg1qGwBeOASEpFYIq-b7hlaxOJTSFkEbvWR13HfPa2N6sicgz9WcXZNihqow5FUvxSmJq9X7Yxz-94BsGdfPyHTQWrnELJcaEIZ145gjzGY8cWl5gpG6hZ2kkRzEnFthT8HGUSnVg4L-PmR7pd1pPz0UbDbmPRdOfx2aOOBtdLjuP_iPBGOGXb1RZElgk9rLik1a3EdBmyHWX2gkXn5xJ-4EQjsukDOiGY9I9SONsalQnoOqt_GeYP0dndsZlVcIRAACLYidl936iMYe-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رژیم صهیونیستی مدعی هدف قرار دادن اتاق عملیات حزب‌الله شد
🔹
وزیر امنیت رژیم صهیونیستی مدعی شد که نیروی هوایی این رژیم اتاق عملیات را در ضاحیه جنوبی بیروت هدف قرار داده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/akhbarefori/656839" target="_blank">📅 16:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RAm_2ApwqQ96orZtqf_rq2r-6I2gk_Hx4Kwdi9p4HCV-qXpS01gjgv2OEUeNMyafTlu3eK3p2UywzogSkOJ8dPQaVtw0hh_Ju6vQ2o6ERSIxqq-BoQXHIDdgBe6y5LwtqgC9k1DPMbbSM9Ar2rADcP4PHxd3r_tADc-lGPCc7aSroH8V4xlejhzTLeZIXo-7mjdcBsi57LjumdKwG1FYAxLTcMBS1A8hd_nO8HnDk7ehYWwY2nO2af-C3KGg3kDJqJnxlWzFzpnJHW1p0UPU2eeG7itkJh5nrwFgFrXZ2aO_YbbaEPyk11J4trHzx_l98UXenGPuQJ7fwBzqT2-LRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VyDwtc94dN_4LrbDaeiG8MUc8G4D4DkDskNmXYA5pn_ZoOfErqvUe0PHMdM7tB0DmTjZo5q10kT3hAcmiGqZHaZodn19ITI1ajQcbIhj-xfcXlhOq3MsWhohcdTr6zZ2KeVJPrriKO9VB0y2kCB9BEET_16ClMXETeL0JzlqrGLFfHHbNdiZb4sDaMK9f5e1gsblHeWcqU7POgv7shcyDDNDLMonExq1AIGxd6gVhSC36OR6cVpEX5T28gIZwop7mj6ZIulD45Magy66psasm5R1lTUCipnBrtZpwdr7vAGbz3KRzzrVs71J5Fb3ejGEsmEAR-qZqzxqIuGXOmyLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b7R_1asBJDBgOBJGEEwPOGWkQpZ8SnVCfQdTO5oUOP_ggGt6UCmiL19NHwEw0BqDD5tf2p3HVwok3MlxHLVnXadF9BDAaj5Da06aZdTqSqRhneZJ-1EMagN_rfP8Tfnz1h7Y1l_j9xHMyMenK8bQmUTebwMN6hCWh6bLwnocu5SEAclf55SKaUFWV9p8Jy3xrWohc-6zb8eCY5yVoCnG3Qjc1Kp5bIlo97gM8lJyTyNT-FBEm_CapSmPQTwddm84rsyAOB-uihPIK0X0lFAnnuMQN5oiHKjxdpkt3QuQfUCaOhfrpz-N2Tyd2gAV_TB6mnC9wVLyzJjHGMiPjm9WRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qj5rlvRwRv-FtaUxXhgNMR7k7TeamfOwZgcDqoOsu58I5fogb3G18krF5QrndcONYIKd2R1FcgTGhcv5RfCXqf5EuWU3myvh0RE2LgGJuro9sTsgguHChEK7iEzOZW_3bJ6PHlF2URs1ArWf8SS5O1fKzsyKIiwbQRPVfwVXhddsRmuWpHY9u9M5mTk91hwXi7e79gL9rhsm8YJ9gN-XLN9kqjcML0dP7t5gs0hZUxvnaG459zRA9XdkX9N8QyNgJzG885p3_fMHRNpoui7X49vt3SNG52hTjJVRdx0zh7UftC-dzi-lZt0LFIBq38OwmZ-tTBBpTWFxqBY7V56Klw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هوش مالی بچه‌ها رو به این ۳تا بازی تقویت کن #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/akhbarefori/656835" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656834">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
تکلیف افزایش حقوق بازنشستگان مشخص شد
🔹
درحالی که طی هفته‌های گذشته میلیون‌ها بازنشسته در انتظار مشخص شدن وضعیت حقوق سال ۱۴۰۵ و صدور احکام جدید بودند، تأمین اجتماعی سرانجام اعلام کرد احکام جدید بازنشستگان و مستمری‌بگیران صادر شده و از عصر امروز قابل دریافت است.
🔹
در احکام جدید، افزایش حقوق سال ۱۴۰۵ به همراه مرحلۀ سوم طرح متناسب‌سازی اعمال شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/akhbarefori/656834" target="_blank">📅 16:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656832">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/186c03c558.mp4?token=WWBvxREJnqfYOrnCI32soHv2ev8J7P9kyLvQDz83cThiLR0uSSdYDcBnSvlSd-PmSeoynvevsjqWZZuCHjMsqb55gfKkg1rsyR6gRPuK8ztqbSSCPwXZyl5mPhcqnIk5jHakiIlZTIF6O8IWsir-_JGnFqGhJmVgtFoZTfvsVFK1p81VoHFUYm5R7LZhmjBiRg8WQY9c5BRMRpI-nOXuQ4IRXtTy1-g-NSMBIdhyBSvi2DWdX2Eov_B84qmf0DEgLbKjAsLZIiHOqZ8XHfe7ixHohwFLENgPw2tz0RJKTgPvcNdqWexeX8FPbQnueh-0X39sG-U0JWwqo8W1zkOIgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/186c03c558.mp4?token=WWBvxREJnqfYOrnCI32soHv2ev8J7P9kyLvQDz83cThiLR0uSSdYDcBnSvlSd-PmSeoynvevsjqWZZuCHjMsqb55gfKkg1rsyR6gRPuK8ztqbSSCPwXZyl5mPhcqnIk5jHakiIlZTIF6O8IWsir-_JGnFqGhJmVgtFoZTfvsVFK1p81VoHFUYm5R7LZhmjBiRg8WQY9c5BRMRpI-nOXuQ4IRXtTy1-g-NSMBIdhyBSvi2DWdX2Eov_B84qmf0DEgLbKjAsLZIiHOqZ8XHfe7ixHohwFLENgPw2tz0RJKTgPvcNdqWexeX8FPbQnueh-0X39sG-U0JWwqo8W1zkOIgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای بنیامین نتانیاهو: در لبنان، نیروهای ما تنها در هفته گذشته ۳۵۰ نیرو را حذف کرده‌ایم؛ ما ارتفاعات بوفور را تحت کنترل گرفتیم؛ جایی که یک تونل عظیم زیرزمینی کشف کردیم #Demon
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/akhbarefori/656832" target="_blank">📅 15:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656830">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CG6wp6VNTMYTZopQUdazHxnzSHiEFtc1fnKRvNTdqHCLq6Eky6XwSLyj6u7qZDBlxNkZEnE6bw_Z4-jTBqhxp7olo54-3sp008dBkProW9A9pbws7Pl_Er0EmRgUO3HHsPKTjw-hoelflET6Es-c_cruFfECfHvkBgh2NNglu0kQsEWsCrIQy7PSeoYtkk4Hq3yUL52Z8eYeS_huRO85AP4wv1sPbizOnN00A7Df9qmiIz4f4anQTv7Fcpvj1ZwNrHifuBsogHv-z395SBR56ima7fvRrMFnYirDiFXKqctTjyY_s-mMGqfLiimIQ_sT3ogo63XML6L5_cDSomGu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YobEf397A69ZbRNW0yhdQx4QqQw2aQNIP9oPqMZVICBqxALHU1b0DmEIs2hnPwKsQyoJOGISz4VWG98u-pmwIavDNb7ByyrGFsd3Lj409b8cwmBeNLKg9dYMtzpvLRMzfyrAyPzmuwWOqo4zJu6dLH7db-ieBK-7RRO9uo6Y-iSaADd4eay6ttiF5Y5vrp16VjCBN9Bhu5XJpRKi5eGxPftQIcCx-JlaK92x5KegF2nV9E8mgnvzVXS-iPBARgI9LZX10_kCBXl-y87BMiPjDJZNheh8rD7XXqsilc1DyqSIh70mZKe4kalemeq77Dx-RHk7_mKSperSgXIyUYPFqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انفجار بزرگ در ضاحیه در بیروت
🔹
اسرائیل اعلام کرد که ضاحیه در جنوب بیروت را هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/akhbarefori/656830" target="_blank">📅 15:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656829">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
انفجار بزرگ در ضاحیه در بیروت
🔹
اسرائیل اعلام کرد که ضاحیه در جنوب بیروت را هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/akhbarefori/656829" target="_blank">📅 15:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656828">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16df92bf92.mp4?token=b8ef07wSkpwh6mIIybs2Y0-sNHxsILsAH5eh5rngMmulXX9lNB6O1MBIvaZcAlUVqq3jQbniUpUJxqY17Tl8UlqQ_uc8IJOC6LYZAjRrfprAit84GGoE_GeWjUCFxq3Lj3wcCqlTG72Z6c6BgExWwDBmYfvjmunXx4io_XK7Ua5ZVcGREhDYLI0oEG9aYhdCEnE4ZzZ5bPUk5tkvvIGAEq4Zca7osrGamlrBRduXxnvPj4a7iHVZeC4PKAdBd6h-vMRAwSq2d-NED4TTCnnyxiNQoCesuuDC3Mp405jOJQMH4O2yK27kRsO78oowQutvU2E0ZEJUqJt7BPO1e3fhOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16df92bf92.mp4?token=b8ef07wSkpwh6mIIybs2Y0-sNHxsILsAH5eh5rngMmulXX9lNB6O1MBIvaZcAlUVqq3jQbniUpUJxqY17Tl8UlqQ_uc8IJOC6LYZAjRrfprAit84GGoE_GeWjUCFxq3Lj3wcCqlTG72Z6c6BgExWwDBmYfvjmunXx4io_XK7Ua5ZVcGREhDYLI0oEG9aYhdCEnE4ZzZ5bPUk5tkvvIGAEq4Zca7osrGamlrBRduXxnvPj4a7iHVZeC4PKAdBd6h-vMRAwSq2d-NED4TTCnnyxiNQoCesuuDC3Mp405jOJQMH4O2yK27kRsO78oowQutvU2E0ZEJUqJt7BPO1e3fhOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انفجار بزرگ در ضاحیه در بیروت
🔹
اسرائیل اعلام کرد که ضاحیه در جنوب بیروت را هدف قرار داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/656828" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656827">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
تیم ملی فوتبال ایران به تیخوانا رسید
🔹
تیم ملی فوتبال ایران پس از برگزاری اردوی خود در ترکیه و برگزاری چند دیدار تدارکاتی در راه آماده‌سازی برای حضور در جام جهانی ۲۰۲۶، از ترکیه عازم اسپانیا شد و از آنجا به مکزیک رفت.
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/656827" target="_blank">📅 15:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656826">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aebb5eb86.mp4?token=wCaTyY0V9z1i4832V4UfyT8eX3paLGjLQA1qBFKnZm3bglT3SN1IcocNIt4ZRi_GUmJFCUTdKJci5WOge1bV5cEwNZNFrmlgj3WBpllWEQ9PLhQ8zCfo_1LRy2-NdprzS5sT6Zm4ZnSZWwyp4y_EwJZ9coAB63yXZN8jvPGWY_HQClAEPrwRuTO4uWsgVCinRKYpT_dSSe8ilnHX2JgQNBdvMa5cBA0bekrD-WnQSVyO4AQZNduvOX8A7CI777GiwbKQ66greMJqcwEw9IjeXoBbtLeTtYyAVUI5_tAFeqnbXT40WFjTL7LtmQJgHvCr-Qhc0tES6diuxoIdOIlFzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aebb5eb86.mp4?token=wCaTyY0V9z1i4832V4UfyT8eX3paLGjLQA1qBFKnZm3bglT3SN1IcocNIt4ZRi_GUmJFCUTdKJci5WOge1bV5cEwNZNFrmlgj3WBpllWEQ9PLhQ8zCfo_1LRy2-NdprzS5sT6Zm4ZnSZWwyp4y_EwJZ9coAB63yXZN8jvPGWY_HQClAEPrwRuTO4uWsgVCinRKYpT_dSSe8ilnHX2JgQNBdvMa5cBA0bekrD-WnQSVyO4AQZNduvOX8A7CI777GiwbKQ66greMJqcwEw9IjeXoBbtLeTtYyAVUI5_tAFeqnbXT40WFjTL7LtmQJgHvCr-Qhc0tES6diuxoIdOIlFzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات عجیب بدرقه تیم ملی به سوی آمریکا؛
یک دوربین علنی و ثبت جنجالی‌ترین اتفاق اردو!
🔹
دوربین شبکه DRM ترکیه لحظاتی از ترک هتل آنتالیا توسط ملی‌پوشان ایران را ضبط کرده که صحنه‌های آن روایتگر مکالماتی جنجالی است.
🔹
قلعه نویی: برو بهش بگو فلانی گفت دیگه تو اتوبوس تیم نیاد!
🔹
البته که به طور واضح نمی‌شود از این فیلم متوجه شد که قلعه‌نویی از چه کسی عصبانی و ناراحت است، اما می‌شود حدس زد که منظور او امید نورافکن است. در ادامه این مستند قلیچ‌خانی برای انتقال پیام قلعه‌نویی نزد مدیراجرایی و مدیر تیم ملی می‌رود، جالب اینکه ثانیه هایی بعد مدیررسانه به صحنه می‌رسد و با متوجه کردن آنها نسبت به دوربینی که مشغول ضبط تصویر است، می‌خواهد که این مکالمات پایان یابد!/ورزش سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/akhbarefori/656826" target="_blank">📅 15:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656825">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
ثبت‌نام مسکن استیجاری زوج‌های جوان از فردا آغاز می شود
🔹
با اعلام وزارت راه و شهرسازی زوج‌های جوان واجد شرایط می‌توانند از ۱۸ تا ۱۹ خرداد برای طرح مسکن استیجاری ثبت‌نام کنند.
🔹
این طرح ویژه خانوارهای فاقد مسکن و دهک‌های درآمدی پایین تا متوسط اجرا می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/akhbarefori/656825" target="_blank">📅 15:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656824">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شورای صنفی نمایش با پخش بازی‌های فوتبال ایران در سینما موافقت کرد.
🔹
بقایی: مواضع متناقض آمریکا مانع اصلی مذاکرات است.
🔹
سیدمصطفی حسینی، مرزبان خراسانی حین کنترل و مراقبت از مرزهای جنوب شرق کشور به درجه رفیع شهادت نائل آمد.
🔹
حماس: در حال رایزنی با مصر، قطر و ترکیه برای تضمین اجرای آتش‌بس هستیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/656824" target="_blank">📅 15:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656823">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
هزینه‌های ثبت نام کنکور و مصاحبه فرهنگیان سال ١۴٠۵
‌
🔹
ثبت نام در کنکور فرهنگیان: ۴٠٠.٠٠٠ تومان
🔹
هزینه مصاحبه گزینش: ۶٣٠.٠٠٠ تومان
🔹
هزینه مصاحبه ارزیابی: ۶۷۰.۰۰۰ تومان
🔹
آزمون عملی ورزش و هنر: ۵٨٢.٠٠٠ تومان
🔹
هزینه معاینات پزشکی: ۶۵۰.۰۰۰ تومان
🔹
ترمیم نمره به ازای هر درس: ۹۵.۰۰۰ تومان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/akhbarefori/656823" target="_blank">📅 15:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656822">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXxL2KTddLb1xRjm4JbsduwlSi1oWB52pJ6mlLaIUP1kghLjQxSZjvfpZkO81KwqcHckSbdHSTK_KdOqQ1_IXWpzmJcuIomUTTUhm4BWbLed_vty_q7NzmGes5rIgaLRS-DYFNLrns3BlTcdUin1DTaSuE0f_7tcS3c2F-jPsyhcy3p_wkXzBAu05xAEDxYWyHjBl0KmCq7GToGLwS0NILkmk98p4fIet1VHtVYVzLcg8zJJ9Ghu_wqJV6HFxdlvYb2PvVURJ1FnzZAcjVGBr1WuAbIPvwZKErcxSibsIO8oHUQ_a6Sn5C1xbDM4y6z14ylwezTtUcArdQEtocF_fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جعفر پناهی بابت فعالیت تبلیغی علیه نظام به یک سال حبس و ۲ سال ممنوعیت خروج از کشور محکوم شد
/تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/akhbarefori/656822" target="_blank">📅 15:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656821">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
دستور پزشکیان برای افزایش اعتبار کالابرگ
🔹
رئیس‌جمهور بر افزایش اعتبار کالابرگ الکترونیکی و تقویت حمایت معیشتی خانوارها تأکید کرد و خواستار به‌روزرسانی و یکپارچه‌سازی اطلاعات اقتصادی خانوارها برای تخصیص دقیق‌تر یارانه‌ها شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/akhbarefori/656821" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656820">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین مطالبه بازنشستگان کشور چه باید باشد؟</h4>
<ul>
<li>✓ افزایش و همسان‌سازی حقوق متناسب با تورم</li>
<li>✓ پوشش کامل هزینه‌های درمان</li>
<li>✓ پرداخت وام و تسهیلات قرض‌الحسنه</li>
<li>✓ ایجاد امکانات رفاهی و فرهنگی</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/656820" target="_blank">📅 15:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656819">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7af76ab1.mp4?token=tzY7YfbpajGjDr82EpN0946g29j-BbuM-SAx8Ki6_dgVOLxi7I9OJeCr-vtYq_gnx8kRS5M0vijg9zRuI2EfEmcBfPZRi53CLWjIBImsXXC5jib84LkbkwlOQ7_75l5lweXxy0HPZEf_RwzwQuuBWLoLVnzKBith4pwih2ua26VX25QLIzRBCvCVTH_NJap8uLg7BRg9kZc-xc4oL1kRWzB3LYbr24eY_yjyzBWwMw_F0aynVirvCTRHf2yTXT1HaufjZOjq0NEEp_kG6NBN3gTxBdLvbr7Vh5tHDVzEwf6aK-1iIBfLypXHtNVqJyxhZQCZHIDGZzYC9Uh2v-gvBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7af76ab1.mp4?token=tzY7YfbpajGjDr82EpN0946g29j-BbuM-SAx8Ki6_dgVOLxi7I9OJeCr-vtYq_gnx8kRS5M0vijg9zRuI2EfEmcBfPZRi53CLWjIBImsXXC5jib84LkbkwlOQ7_75l5lweXxy0HPZEf_RwzwQuuBWLoLVnzKBith4pwih2ua26VX25QLIzRBCvCVTH_NJap8uLg7BRg9kZc-xc4oL1kRWzB3LYbr24eY_yjyzBWwMw_F0aynVirvCTRHf2yTXT1HaufjZOjq0NEEp_kG6NBN3gTxBdLvbr7Vh5tHDVzEwf6aK-1iIBfLypXHtNVqJyxhZQCZHIDGZzYC9Uh2v-gvBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف طولانی کشتی‌ها در تنگه هرمز از لنز دوربین یک گردشگر در عمان
🔹
ویدیویی منتصب به یک گردشگر عرب در فضای مجازی منتشر شده که در آن از صف طولانی کشتی‌ها و نفتکش‌های غول پیکر در تنگه هرمز فیلمبرداری شده است.
🔹
در این ویدئو تعداد زیادی از کشتی‌ها با اندازه‌های مختلف دیده می‌شوند که متوقف شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/akhbarefori/656819" target="_blank">📅 14:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656818">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
اتحادیه مرغ: قیمت تعیین شده دولت برای فروش مرغ، غیر ممکن است
ناصر نبی‌پور، مدیرعامل اتحادیه تولیدکنندگان مرغ گوشتی تهران:
🔹
قیمتی که دولت برای ما تعیین می‌کند به عنوان قیمتی که ما باید محصول را بفروشیم، غیرممکن است.
مردم تاب هزینه‌ها را ندارند که خریداری کنند.
🔹
قیمت تمام شده ۲۳۵هزار تومان است و ما داریم ۱۸۵هزار تومان می‌فروشیم./خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/656818" target="_blank">📅 14:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656817">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c33fa146e1.mp4?token=QahLphQ2I6IGGUYL5IubQhgzH9Wi49yMtB7b_rdfGMGpGASDSAaWgyFzGNr1it4ObFjXeV1BrOfBBp0OP3sHiB6tI05euPinH00xUg-Fa-uRPkeLLk2RGx6U7x_nIKIbP5jhl07ojSBp-qpdTzzCs2AWO3FbqNN-s6XzXEoOyuz2S4qAgw3aMAMtOXmMwIOGpd0Hp9g-vw28hwwRZ1H3wSOQWzANBXk-HfmagNivLN6maSqPE2y91D-KD7iPt_GM-WuMBzeNmh4_Nl2-qjW0APYIh7DccPeMZMJU6lTXGa87XzzCcMhnc11cOPwPXNbKglSTdLULAXXtSXNsDDIFsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c33fa146e1.mp4?token=QahLphQ2I6IGGUYL5IubQhgzH9Wi49yMtB7b_rdfGMGpGASDSAaWgyFzGNr1it4ObFjXeV1BrOfBBp0OP3sHiB6tI05euPinH00xUg-Fa-uRPkeLLk2RGx6U7x_nIKIbP5jhl07ojSBp-qpdTzzCs2AWO3FbqNN-s6XzXEoOyuz2S4qAgw3aMAMtOXmMwIOGpd0Hp9g-vw28hwwRZ1H3wSOQWzANBXk-HfmagNivLN6maSqPE2y91D-KD7iPt_GM-WuMBzeNmh4_Nl2-qjW0APYIh7DccPeMZMJU6lTXGa87XzzCcMhnc11cOPwPXNbKglSTdLULAXXtSXNsDDIFsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو یکی نه‌ای‌ هزاری، تو چراغ خود برافروز #ایران_من
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/656817" target="_blank">📅 14:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656816">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rS_2T7irQNuaQ3qbG7osiUYVpIRafxJQ5lWOeWrdM7s-de1rH6-nKAD52DYK9WA7tozXpmCnS0ojmxE8veG8v2ZtPqo3DEWlm8CjdknJ5cH3_Ru2WQ-Fa6v9rBIuSRCARuRxFo_uGClUcmG3h4pQAh05wZYO_qVLMUJM5zBgDsLg1FV-Jhr8O-GA7L-MfliPJUBGq54Wo2npaw4QkqcLqUEgA_hHuNHpBxHENfmSFus1KTlPQ0BvjFoV2xFKr3dPKvv9Nw9IG4-D9gjkkGRmLNSSfuT9ncN7j5ErsnYjIr3FVXE_dkc8CCjpD7XS3JUk-oCukOBhNd-b2MXOUgR4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بیشترین گل زده یک تیم در تاریخ جام‌ جهانی
#جام_جهانی_۲٠۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/656816" target="_blank">📅 14:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656815">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
دستور پزشکیان برای افزایش اعتبار کالابرگ
🔹
رئیس‌جمهور بر افزایش اعتبار کالابرگ الکترونیکی و تقویت حمایت معیشتی خانوارها تأکید کرد و خواستار به‌روزرسانی و یکپارچه‌سازی اطلاعات اقتصادی خانوارها برای تخصیص دقیق‌تر یارانه‌ها شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/656815" target="_blank">📅 14:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656814">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9WiQmnGpaFCACQ2AXzz3V2rmJ1Rr2x6-KWyxTAKAsKfnv_2gbO6nX4ppfIqGnJRo_NUpaILKMJsNZ9QI1c1dUcJT12k5iTUnMqC9SQrjWuWObjZF_SnXBz5yRtolbvhfaIR2p4hid9RRKjk4kzB3KoB47RVCtIOEHJQKJUIAzL5Rhz_zSDxRTFuCTOVlM_MJ-QFXeDSI9dIv_DWpRlUQopJEoTmwezQMZmIMmbDjHuAq9jCEH4odfb2257amlnjCtPT-jnruBrqaROP2FNUf2AsZvLUzgagOuoglbNCUctqaO3g4m5uFAtjMgo8d4VePElzh695GtJ96yLD-s5STQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه ویژه پاکستان به رهبر انقلاب تحویل عراقچی شد /تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/656814" target="_blank">📅 14:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656813">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
تیزر قسمت نهم از فصل چهارم
🔹
در این قسمت سرکار خانم فاطمه سجادی با وجود اینکه تجربه سفر به دنیای پس از مرگ داشته است ولی به دلیل مسائل اجتماعی که نظاره می‌کند به حقیقت دین اسلام شک می‌کند و در میان جستجوی حقیقت، تجربیات جدیدی کسب می‌کند و با ما در میان می‌گذارد
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: فاطمه سجادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/656813" target="_blank">📅 14:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656812">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfkI2pW9fNnaK6JOlzfuRbRAGY9SrP42CJovapLC7mE4xhFlqRoYD0YzNde3yYJMdapg975h_-D6ArOS2okJdlGwOx9xpEItwFGKBXY2_F1e5SREuSGmD5-CBrmtB-HNgfboe658QI_h7nwKYwf_nQ6Ny8vbhqwzQlDxpahbWP7HTQtRxgLX40Xy0MK-Rlkb8zv6eL7dALdbBmno2VLetpZZPxVPpjwAhjdLJFk9EdtQYB25-sy8_u9s2ospmFNaQ9NeoiFxf-R7x3G4FoWS-Tua3QFV8sx2N0LPhqElakIuCQUDUgoBEw8f7HkfhB4wRTAHKcIWZHJgvVBkW_RKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پراید سوخته ۱۳۹۵ با قیمت ۲۱۰ میلیون تومان آگهی شد
🔹
با وجود آسیب‌دیدگی و سوختگی شدید، یک دستگاه پراید مدل ۱۳۹۵ در بازار با قیمت ۲۱۰ میلیون تومان عرضه شده است؛ رقمی که حتی با حقوق یک کارگر، حدود یک سال پس‌انداز کامل نیاز دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/656812" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656811">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDPrNMs9irvhyxsKzGy4GKYarKHQReHkhfE6i1eHIv0jyB6RXBSrQ8I1SKsI-GPYXkzSgDqUpti2Qm9XLGcBoyHlJolvUrNQLFIDCJp5yzK-M6bviUSfSuQZjqw2V9tbWx-PmJjAu2X31vK3cXg_5qTz5am1qdDCLzsIgF5mSr67dWGlkWxIqeRlC7jTbA6iIxcuCNuqrDjLYNQ29Au7WTwqAJQJwcb-L3ah-litaOmzwHv_W-b91zGREXi3Ct7YwgKKWnTaSUuxlwkzIyoJgrxJnCdZd6-qBrdU1_MPtjfsq6qSn_DZNJpeCK9fx6DnqAQEy0wkVH06gwaAynPbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رحمان عموزاد طلایی شد
🔹
عموزاد در فینال رقابت‌های کشتی آزاد رنکینگ اتحادیه جهانی در وزن ۶۵ کیلوگرم با نتیجه ۱۷ بر ۱۰ مقابل شامیل ممدوف از بلغارستان به پیروزی رسید و صاحب مدال طلا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/656811" target="_blank">📅 13:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656810">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
۲ زلزله پیاپی پردیس تهران را لرزاند
🔹
۲ زلزله پیاپی به قدرت ۲ و نیم ریشتر پردیس تهران را دقایقی پیش لرزاند.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/656810" target="_blank">📅 13:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656809">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvbVPYrbTNngQH65sn88VZHiRDGTinlX0AmjelbUMtGzYZPQBmijaMNM4qgWdZk02SccdaQqdXsbTY3AGEpfPPnT9tBpkBF3Z8JuAiUuudifUbQ5PLgS3fdYshP4cFs-nJ-_5LTD_G_WhjnoWfqx2WYfLskNp3koriOfDin4K3Q0EsPo9bXMij4rNCYYyuYIl5rAd44XXEcD62foCCxbjqOi6YqU_vduKe2efF1O4nRrPjECJM7bLgK3DFS1pZldrvdFCvrd0ueNL4UWPXXBPL26Br3agcDjdbPZzIaSAjyBhKsLlJfzlJcEZfSHdzuI6QWp9PjQ4gjoSXiFORRMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مرغ گران‌تر از گوشت گوسفند!
🔹
میزان رشد سالانه قیمت گوشت قرمز از مرغ کمتر بوده است.
🔹
ماهی نیز کمترین رشد قیمت را نسبت به سایر محصولات پروتئینی داشته است./خبرفردا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/656809" target="_blank">📅 13:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656808">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
هلاکت ۴ تروریست درپی درگیری با نیروهای امنیتی در سراوان
🔹
به‌ گفته یک منبع آگاه، درپی درگیری نیروهای امنیتی با یک گروه تروریستی مسلح در سراوان، ۴ تروریست به هلاکت رسیده و مقداری سلاح و مهمات از آن‌ها کشف شد.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/akhbarefori/656808" target="_blank">📅 13:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656807">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb376fa143.mp4?token=jlRg7qV3Ua6FlDRvSLrB2_M9x_KCwlD14bDEXv3df5-ihwYn6fvxa7RcOK_Y2MImQ3LOJov_Dnla8HTuM4fO3n25N95_N_RSeC1qoOTXRcoPzTHeDeMty8lxO1RWSjivm93WZn2Xsrk_Ynty_qrhRuuIz8IgWCwQ-9UtWetOG4kTh2cexER7JlRGDI3ks0o5MRiIdsiMR_dEXND3UiA39iWZF2-13Lr-mvgXdCJ3GFRHHqpBLyqNXiHt7G0XXZdzKZ5wzlVoep9IJJgqI3gEr1PwsZBY76THw2Upg4KhUdq5R1ReQVDZp3AD7JAaKu7t2FlY0egxSenuXMLkaUDfKgaKuCzG6XOokFIdUuDOgHzAReejfNMErh7odidAQXsOdt2fONmqrIVQLjnbReiT6rreZQKWVvTzboI-ahfvaEVFPsP5Wj32yu3MtpAEqiTc91_g6s65lkwAYY-KfTkFloSKxj3wtlpXPqxZfE6G2W5vpT-pOK6o9lgz5OlBmoHNs4gaQJhX4Zuq5oa3KwhPlPXFjoDsODP8HeT5w28dFGT_OAnBKvZlKnJFsCLFQp1LmHvdbnOCoBmrfLDTlKSVSMuaezIeByr-zDB3YAf3WXyS5a-O30uua6wlqo6FA_YKZ6_JpWZjh1ropY9ZmXTN4X_SQE66nhPkTVQWC8KTY2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb376fa143.mp4?token=jlRg7qV3Ua6FlDRvSLrB2_M9x_KCwlD14bDEXv3df5-ihwYn6fvxa7RcOK_Y2MImQ3LOJov_Dnla8HTuM4fO3n25N95_N_RSeC1qoOTXRcoPzTHeDeMty8lxO1RWSjivm93WZn2Xsrk_Ynty_qrhRuuIz8IgWCwQ-9UtWetOG4kTh2cexER7JlRGDI3ks0o5MRiIdsiMR_dEXND3UiA39iWZF2-13Lr-mvgXdCJ3GFRHHqpBLyqNXiHt7G0XXZdzKZ5wzlVoep9IJJgqI3gEr1PwsZBY76THw2Upg4KhUdq5R1ReQVDZp3AD7JAaKu7t2FlY0egxSenuXMLkaUDfKgaKuCzG6XOokFIdUuDOgHzAReejfNMErh7odidAQXsOdt2fONmqrIVQLjnbReiT6rreZQKWVvTzboI-ahfvaEVFPsP5Wj32yu3MtpAEqiTc91_g6s65lkwAYY-KfTkFloSKxj3wtlpXPqxZfE6G2W5vpT-pOK6o9lgz5OlBmoHNs4gaQJhX4Zuq5oa3KwhPlPXFjoDsODP8HeT5w28dFGT_OAnBKvZlKnJFsCLFQp1LmHvdbnOCoBmrfLDTlKSVSMuaezIeByr-zDB3YAf3WXyS5a-O30uua6wlqo6FA_YKZ6_JpWZjh1ropY9ZmXTN4X_SQE66nhPkTVQWC8KTY2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه شمام تو هوای گرم تمایلی به خوردن غذا ندارید سالاد کارتوفل می‌تواند گزینه‌ی خوبی باشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/656807" target="_blank">📅 13:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656800">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاقدامات هیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ixlNgBcEGF5nZDvu6knidXDLpGn4H7UJhABAIWQaY8N5Wd0Ufzf95ZczBgx8_aWp1PH9bjaU_anbQiaqBd9iVcy5jQ5O8hl6we3p7hvIcgc8UqOFotBUiRMYTm_rXOZ8OhOvaZiffl6ZiKjXkNAHRFWka-EFmFBEgAB3AAO_qkYyMS42BAG3Pq5DjFNNeEGPekDXgefjWjMYzg1uOxVpkPz9CrGbAUJb9f82XBhdwqUSOT9uJn708Oa4MZVUyDC3rYro031dvjvXBUQbCRDAuTnAMZcy-XvgIjK8nvjtPUGtf7kgiq9MoH7troUT-Wl_s20e8YA6EV-IzEq308is3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXFeIwAZkrTZuzOGEMOmBt2bOM_bcsI3sEFdJ13pVRXWjxCeoECiruapwbfWi-DlxaBqyZ8-lmFGeeu_iPL51DA3NfEMfhEocgu96cAMC478KElQsXx5tKXzjZVtoNRZ9UcIul9hQ-DPPLH9qkcYpzB45npDux2zfiHwaUgQI8fVl_K7AUN0PylMUTQzi0lvsgPr7FsKQb7a_jy4Ep0WJYFRZwiHyiCcWr1nHUJ2o1zoDlNrL4-P8TTs2a2hnv-zyOi17vpD1OGgIZuV_ft9i-pBuin6b0aTca8koVm9jyazBIk1eGFarmoZX5SHRmboe__J1F5XQqzNkys8UEsR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HH8xyfgauDjBS2BJZ990k6LmpztS82TkHqx0pGCayYoiYDL5A3bvIH8n2hjmIh4BY4wd3LiToNTLUiBYDZmP5xq3HJz4huvyBTP42F5sL8FRtgYkLCVI3S5uEILjNw5toclunDW_fWM--TK1qKGvQST5R5Cd_niY8L6YNjrr3JYb0jAN6pPj3kBTJTbcfqrTHYxdNSfYprWFqpRvyt68Dpik4xi18m8bj32hHwHrO4j7XjqrZ_TUtlvto3RxDEL7g2HoQ-ShLGfGSy_ZxukRHPRBQYWIefnxUzgLPY3ShUC2vZF57X7vG515-7yq4-uvgOOB1OqV61ZPW0Dfg2NEJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hh4JphdZbnfF65-kP53nmYI5-D1NjYad3ABorzxg4uNUSZDXhz4DA_NzNsAccGk0o-LbXAeTiaH_qN67ZLSPv6cHH3Txo6KhNJZr1BOe3_IHZO-YdMXjC3gQJet5vHohSznXPV0ejdZ4Fhlz5iWBm2W7ci4Hm9QQGD0y8iQJkxabT5Y9j7maIVVe5o_VLlKf3b26xpAsAIMOywCy5QVDbZWzM5aShv7U5hhgsSHlUGLVIDF-coLylviYbcZxPjMDk8jI6KgJcw6EF7KWZfJOyDzuZm3DGPZuWl-UA2HdBTek_R_QelbbOze29Lr0VImga3CaPHYM7kMPQYxj87IrOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCuoP8ghGNzFQ4JhmxTfmGgjyhzSx3Yjd1zvqD7MuXfFCDgKBSdaZt5o2TReiIKN_iR9wkn1Rd25g2lLbIfcmRyLW36P2_zA3td15cTdDF_rJFhQRdmGwNpRm8gAJLwD7IhUpc2O6orNkG5VE3IXXDz1UPsoMmGV9iy26qrLxNpX8uufJPPev8u3ErnkBDNVx5fCk4R2xuQfVBjUV-zCl8fzq2jXjSDApVadFbrxkV6jgtYuYEn187EzT9UZqRbHuz6rRQWkjG2FcR7h1HH0TZqFCvQJUYJYMHGsAH_j0EAjZrgTmBHbIIQZjbDv9dt9_FjLab5ZZH6KYsyzuWnwkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFPCSkkM4BirlpRFqrV6CZaLjjG9fxjbY2699xLU6Ljj88Djr6dHIKbUe7NbQ3XC1bzAH-aeUtZiwlQiCYDzvxDKw1KW--aC03PEXn90Z8vbknZdt6GRBUceTtVrheOf-mnVw1dCCIvZeth0wEQWFzyX_w0wtykVEl7lCPrt5Q37ssRr8O7IP1YNfkZlmCfLTrtfvs7ODU0hx3DM4ldn6rrlpKy4NOpuk9-P9kXXWSbxI3p67r1S0cTcmLSMtSsxLhrrr7MAE5dit3DioprVDVTmcVyOv8eSL4DHXDMWTPbOmPglxW1xfwMurEAbKF0Q__FAkcldkxgE7mPI_mj7iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jXkwDFbu6BK0HtL9svOkVY57MDrYa87cZG9noNfEnIPphzweSvjsD5bEEBrfbWyIcGUIZs3xHQUFlludGaL_Y297yLmV64FUCNDVuJp052ETUBvQFy7NIzoPFcue7oq2DDMzMCDoHpR1_n0e7SBj6PJBy2JMLGFFXG65AyxtYA-g1pu81a04sU6X5fU4V7Do2FWqnejShjrrbJt65RHRA4e3eCxFX7EoHqCQ0OHCmeukkUkVWCfMo2UrAV7C5URK3kgknObypVLP2nl_4gEOJTXZZU4CTECrepfN9bvbhk0nnpfNNxpT3GwapQYfXMj7hXTUSAcsP4dCEXttuT-kGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💫
روایت سهم‌های کوچکِ ماندگار
💫
✨
این روزها،
#همدلی
فقط یک واژه نیست؛
حضور مردمی‌ست که کنار
#هیات_قرار
ایستاده‌اند تا هر روز با ذبح ۳ رأس گوسفند و توزیع گوشت قربانی، قدمی برای حمایت از خانواده‌های ایرانی و خانواده‌های حائز صلاحیت بردارند.
همدلی شما، ادامه‌دهنده این راه خیر است
🤍
💳
گزارش اقدامات هیئت قرار را در کانال زیر ببینید
👇
@Heyate_ghararr
شما نیز میتوانید در این کار خیر سهیم باشید
👇
5029087002135690</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/656800" target="_blank">📅 13:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656799">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
سیر تا پیاز واردات خودروهای خارجی
رسول رئیس جعفری مدیر عامل منطقه آزاد تجاری - صنعتی سرخس:
🔹
اگر فردی یک خودروی وارداتی از منطقه آزاد سرخس بگیرد علاوه بر اینکه در استان می‌تواند تردد کند چهار نوبت دو هفته‌ای نیز می‌تواند در سطح کشور تردد کند.
🔹
واردات خودروهای عمومی نظیر اتوبوس‌های شهری و بین شهری، تاکسی‌های عمومی و هتلی و کِشنده‌های ترانزیتی و تجاری نیز در دستور کار است.
🔹
فقط سرمایه‌گذاران می‌توانند مجوز واردات خودرو بگیرند، سرمایه‌گذار کسی است که ثبت شرکت کرده یا زمین دارد یا در پروژه‌های سرمایه گذاری و عمرانی منطقه مشارکت دارد./اخبارمشهد
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/656799" target="_blank">📅 13:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656798">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
دریافت هزینه از کشتی‌های عبوری تنگه هرمز وارد فاز اجرایی شد
زنگنه، عضو کمیسیون برنامه و بودجه مجلس:
🔹
از هر کشتی عبوری از تنگه هرمز به‌طور میانگین ۱.۵ تا ۲ میلیون دلار دریافت می‌شود؛ طرح مدیریت تنگه در ۱۲ بند تدوین شده و برای اجرای آن مجموعه‌ای با همکاری وزارت اقتصاد و زیر نظر شورای عالی امنیت ملی تشکیل شده است.
🔹
مبالغ دریافتی طبق قانون بودجه به خزانه واریز می‌شود و بخشی از پرداخت‌ها نیز به‌صورت تتر، کالا یا تهاتر انجام می‌گیرد./ فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/656798" target="_blank">📅 13:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656797">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jroC26yRCQ2AFgNJ3A6m0kEdsZVVDkP3cJmriuqw_N2u_hbH5z-HrYkpUfzapCYUaS2wLh0eGmtTE_qxQDJkZ4CICxxEtPzuoOhaWf_maN7gVkr4Y2Hcs3R8InFeNPX96nOVAkVAt1T7b7gjze4qYPTM9q-JGz5gfyFDFFaNrJ7Ivhq3MKBs4nMDOG13NRL7HHN0n5k-bW-CtDS_Y8OSq4hNy-ixp5A15pWhq8cpvxcX0ICi8JCH0DciEH34nhmtVWmCfmKF-lUqnZ7kddIiHLqM6D1husmThzCX7Yh5km-yvz6y8HCWmw5w3U6FkgenSQ6sveUvuaxSyu82Fx5HCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه ویژه پاکستان به رهبر انقلاب تحویل عراقچی شد /تسنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/656797" target="_blank">📅 13:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656796">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83207df46e.mp4?token=DnyjEfWMRXkZKopmmXfPnFYYqx8Q5uFkcrf6Nz91Zl2G0M-pB9nBUUxyf5hTtQ5c76HsVZHrjhSo3Nir6FYX5dOpUGoNql_4ZVw72UPHIUaZK6fvHcdIj2oVrfMjmmfSzENMGQm9XrqTSqpc0ICiN6rONZte7o2PQlBuHCr77ayv8lnheb4EZg3tzxE0MD9TksW3kD8MEHvW77ayfqthGqPpT7vxTbMGKAgh8bqzzHFB0hn-LZCVjsUW6vTPgfL6qPq77At7uRV2SSZf8ItnVxQAuYW8RVi2_9fA7C2e5Seqnoo2X_mqgVAWxSlXUdGzLCp3VpwU-ul5yQBTj7yBHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83207df46e.mp4?token=DnyjEfWMRXkZKopmmXfPnFYYqx8Q5uFkcrf6Nz91Zl2G0M-pB9nBUUxyf5hTtQ5c76HsVZHrjhSo3Nir6FYX5dOpUGoNql_4ZVw72UPHIUaZK6fvHcdIj2oVrfMjmmfSzENMGQm9XrqTSqpc0ICiN6rONZte7o2PQlBuHCr77ayv8lnheb4EZg3tzxE0MD9TksW3kD8MEHvW77ayfqthGqPpT7vxTbMGKAgh8bqzzHFB0hn-LZCVjsUW6vTPgfL6qPq77At7uRV2SSZf8ItnVxQAuYW8RVi2_9fA7C2e5Seqnoo2X_mqgVAWxSlXUdGzLCp3VpwU-ul5yQBTj7yBHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سونی‌اریکسون با نمایشگر شفاف در سال ۲۰۰۹
🔹
تصاویری از یک گوشی سونی‌اریکسون با نمایشگر شفاف و شیشه‌ای منتشر شده است؛ موضوعی که با توجه به فناوری آن زمان، توجه کاربران را جلب کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/656796" target="_blank">📅 13:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656793">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77f4a7f60.mp4?token=vDffjqh3q-6i80COaMvSrSJmFuUcB5oJODqJlvR4bGg5ujymQuswoyUsv_kUrl9SYDCT1fA9RyT5wUzLia7sm-vdpEZUsfNWtpWQbLCRuMPZG5B7Q6jFas90uu5XCTxAg4JzjW4uH_5lux9zAJDQT3zIFZA4smHf3HhgSntju2WR7xf3auqpg-l3mAhdyTIDVfZzHNlbleipKLaCXcUSZR7NtldiAriF6J8Umt9GXKoHoyomqjPKpNPq8E95pV62O6q6ZTXtWDDvHqFTmBLOWwEdIoimgQAEPYUlitnV4zd6vyok6-wPhnvDUSteNbTG4cZKL0JWyh2vyoZGEcQoTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77f4a7f60.mp4?token=vDffjqh3q-6i80COaMvSrSJmFuUcB5oJODqJlvR4bGg5ujymQuswoyUsv_kUrl9SYDCT1fA9RyT5wUzLia7sm-vdpEZUsfNWtpWQbLCRuMPZG5B7Q6jFas90uu5XCTxAg4JzjW4uH_5lux9zAJDQT3zIFZA4smHf3HhgSntju2WR7xf3auqpg-l3mAhdyTIDVfZzHNlbleipKLaCXcUSZR7NtldiAriF6J8Umt9GXKoHoyomqjPKpNPq8E95pV62O6q6ZTXtWDDvHqFTmBLOWwEdIoimgQAEPYUlitnV4zd6vyok6-wPhnvDUSteNbTG4cZKL0JWyh2vyoZGEcQoTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گلر آرژانتین عکاس شد
🔹
امیلیانو مارتینس در لیست بازی بامداد امروز آرژانتین مقابل هندوراس حضور نداشت ولی کمی آنطرف‌تر مشغول عکاسی با دوربین یکی از عکاسان بود.
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/656793" target="_blank">📅 13:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656792">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b5785b55.mp4?token=rzyGlCDKW11P3V3CkMH3TOzC3kLNj3MEm4d4IsmW1JPX3xO73AxFPD3RnC_zk4G87OCBs0RGG8XanJdogkK3pK-jsUj1yWkKv0p50gdRiMTTaiFDjih0dk5SnNTFYPmAm9AUxUI6VwCgI3CrA_c1ws86EtKtzrFb-VwnsFArqgisWg6jI9gU0SQfPhUbSKM-4he9nF6U6XpMm5mWNbqvSQZ7XIJqwoongiAY2G4o7Q_UmVTS7jJHaXMggJwmdJVLCID8aW8-LD46RUdqTzJSPbiusbrfPVErRH_w2HUVjDeg-or_i4DOAh_5-Ns-ox1LTD7C2EkH9vlQmX7Nyc5Z-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b5785b55.mp4?token=rzyGlCDKW11P3V3CkMH3TOzC3kLNj3MEm4d4IsmW1JPX3xO73AxFPD3RnC_zk4G87OCBs0RGG8XanJdogkK3pK-jsUj1yWkKv0p50gdRiMTTaiFDjih0dk5SnNTFYPmAm9AUxUI6VwCgI3CrA_c1ws86EtKtzrFb-VwnsFArqgisWg6jI9gU0SQfPhUbSKM-4he9nF6U6XpMm5mWNbqvSQZ7XIJqwoongiAY2G4o7Q_UmVTS7jJHaXMggJwmdJVLCID8aW8-LD46RUdqTzJSPbiusbrfPVErRH_w2HUVjDeg-or_i4DOAh_5-Ns-ox1LTD7C2EkH9vlQmX7Nyc5Z-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ندای خونخواهی بلند شد؛ نوبت مراجع است
حجت السلام رفیعی :
🔹
آقایان
#مراجع_تقلید
و علمای محترم اکنون نوبت شماست که به پاخیزید و اعلام مهدور الدمی را برای ترامپ و نتانیاهو اعلام کنید موجوداتی که خون نائب امام زمان عج الله تعالی فرجه الشریف،
#شهید_ثالث
را بر روی زمین ریختند و جنایات عظیم دیگری را نیز مرتکب شدند.
‌
• آیت الله سیستانی
• آیت الله مکارم شیرازی
• آیت الله نوری همدانی
• آیت الله وحید خراسانی
• آیت الله شبیری زنجانی
• آیت الله جعفر سبحانی
آیات عظام...
‌ما مسلمانان منتظر
#حکم
و فتوای شما هستیم
✊
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/656792" target="_blank">📅 12:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656791">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnSXHpF44hps-p0ENDRlih6u2UpZkZWSXTMKiOixAd3ChvwuT2FEx9PmRvYN7t6LSJze_NFl8HkUvVS5mRn_fB2jwIiagLYi5dXr-QoWOeDe6rLUrCZOOX7KNIUFAj222H9Hs6N5DGd-agIMkIMGGSlokdiQNl86SkejPQCJfxD5veDWfzMniuJeziyRsOG0ih26ikCjCZJnmwWsPZ0c3gryeaRnRKjMqI2V4kLEYVjRJ7u_PlEQDHFBt0MrmLyCKUWgbi8KbUNQAlwZ_6hoU5uv-8zlr4QPSDDmEcVfr_r7Muobct0aCswdgtrVn1E52jIUDk8_6__CjT1gYRdq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لرستان، دره خزینه پلدختر
🇮🇷
#ایران_زیبا
#اخبار_لرستان
در فضای مجازی
👇
@akhbarlorestan</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/656791" target="_blank">📅 12:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656789">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bf-z1LnNMCgYzKiVhoHS5-cmUOtFedUbCmteXEhWqHJA2gilp7q7AlolA6pdzI40vqvT8Afp2Q5LrnOyJctS-iKJ4NaWo2emW5Yr4IBZlZi_-IVvvG_get0sOQhvdvVOoniht9EwWfKORLBfd_YIIprgXbcTuud3qaOgfw5uMBDAQ53xeQND-JoYaJa35K1vjEu6pQvvz_HT-7A1q_-vM1cOsdHy_olbU4LEdrKuoggfq0kKSVLdp4rUIdd_FRVBkMtbPf3d4D4NaIbTu7S3jLNqF-RGjSwmSxafG-BBsBrjnhj33n29BL9cgNXLQhVDgzbDur9Xx5xTzTH97M5IoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UiqeojJQcPBYpgMY3fwMAGUDCw9KJXscM8-pkdTs0FYB2YV9t95HYXnoTyhG9nKcRSqSkZlqogDRhSm_0Ky77UG9gpVwOK2N6QU2_1FhaIsVNCfi08cJIWDq36ncm0pz8XqpoL2f9wHd4bvDby8M253d80DWmkRv3JHa7qvTzQdUIiZmaxU8m-R1CbvmcmouDGw3ulY0ofJERDi1D6MjXQ01_5Opalec0efz05az78raUjKw7K6jkQiZf-CI4EvbYtSg6yqb3RgFRly70xe4585KftK7yoDUsBJY4mbYeLwy0eJheDgHTZlzF3WmCGIcBVBcsRjN-njgpftTrfYxlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترکیب‌های‌احتمالی تیم ملی فوتبال ایران برای جام جهانی ۲۰۲۶/ تابناک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/656789" target="_blank">📅 12:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656788">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSg0TTBcA1mwcO2ZMSV_qUWF0U3pMS3YeWRfLm_xKQpA6xZUJKWUBnlH1LhvvLBHk7Clgd1pmNJKFaMNjVH3K9-68qmVm_kSFcBA8pjmbLSJX8WFdIfSJ3PSvhuYPSn4UqvkuaimZBeU1cEND56vtrArdqGN870u3zl0uhSnMUgAeFR7VI6YEVVf0FijZkzIDptsNKcAkCri1ye4b6ulV4uhg1zQ251gAZpgMaWUgGxMT51l2HMYK23Wx72aaafxMywD8XnUTAQ4TDHiRHY0iYzIxNMLIz8N9pf6cmvMcuWUgnmIVIsXmdcTTnyqsGhBeFtj62mZLkhLT4y0p_m8aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس همچنان سبز؛ جهش سه رقمی شاخص کل بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۰۲ هزار واحدی به ۴ میلیون و ۴۹۴ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/656788" target="_blank">📅 12:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656787">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJmVnEDNpuGJHd4Q73re8ASq0neDB0okwsEOgqmd7kqXXAoJ-z4bEKuHsE7FSgllCTnXWNACXD3Lm_stF88Od9rFdyKDjXt-MFRMp8MkJv9-_EdXukk-Ba-WiArxP3wZd-xNek89PmCIs4fyngmukbFRLVPUnRX02orz4kvTO0J-V3e9j_ibK8a3rXSo3VFTYcSygfqEM0NfRVnRagT0JdbAYsbpZcfN01Hqy9PNixVLNdCjdBbd65eFgiedTyaYLqIPJGxDS0Eh-fk7jlqRuXKKEk8oplTTOCLV8ZGTQZpfePTQv8vbSZtI_5-dRJBVZQxdtT-vCukksJvt34bfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین وضعیت پرونده تتلو از زبان وکیلش
وکیل امیرحسین مقصودلو:
🔹
موکلم مشمول عفو اعیاد قربان و غدیر نشده است؛ توبه تتلو از سوی دادگاه پذیرفته و پرونده برای تصمیم نهایی به رئیس قوه قضائیه ارسال شده، اما هنوز حکمی صادر نشده است.
🔹
وی همچنین خبر درخواست مرخصی برای مداحی در ماه محرم را تکذیب کرد./ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/656787" target="_blank">📅 12:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ymnp2VXSkZmVvcAmoy1db_P9sg6TAAzRjnRiXwlYapMZjqLeBGN5TyAqPs5D5roBikDcLQ1XVrYOLNS11oUSaocTypQUv_2_V3YX7uxl2zt3-VJ3Sxsdy4M7aCc3Ie0jbIPH69e9vG82_AW-1hq88lWdcjohki_AmD78j18ax6SVrrlW1DvmyVDB2a3Zw7yR5bpVOp2lv16aiNyQWkzMse5vhLwoCGpDqpTGQqpBzDQfULjEYGLySWT602_3I6y_Gp-Ijz2Mwpf1nCUtvZ1H_NzSiYvRXfOEhgjy57KumkNSq3zeNOXk5v4pwQhv1mRsc-98CGAERqb_3cH1XGVZjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیر تحولات ظاهری علیرضا بیرانوند؛ از تورنمنت آسیایی امیدها در ۲۰۱۴ تا جام‌جهانی ۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/656786" target="_blank">📅 12:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656784">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2-M0EkTm1BG1NJzxjQVMHPuUi-oP8xCtlWt4mF4QQgTVdJ7OrfsZM4PTw57KakqV4MOoRyq1POpBvKcHIELvFrdaQtciiD-Jjwlio3d1YsmKk5TkZqHeVUVDMzPhLgvpOksRH9vHPfw1EpUHhkRp7OYhb2YCDh_nJXmsuxw8-GOtC1wDCK3n4LqKF8CrKLcJwpd2A7V69D-YXj3U1br85v-1g1H-hw5INklNBZySotlPkpWj3Ha3-BmURxkpGVb04lPiZiiJW6LfinVTOlNjwNOoUvtg6eC5Iv51dhL4suf_5Oc01Uy99oQ_ZtlE7IaH1TxVa_2K2ZSqJr2-yxc6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ نمونه مشهور از اخبار جعلی
🔹
شما کدام‌یک از این شایعات را به خاطر دارید؟ #آگاهی_رسانه‌ای
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/656784" target="_blank">📅 12:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656781">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cF1Xwk0WrmMqzPxHCjR0TubB3LfPHyBI8fokfHLPhKNvIAljUUMqaDPx1PV--2YQFgfOL39W842xyQnjriM3AgyAYONrFTX63y_KlhZsAEO0zzZOlBw3TDbAJ6qJFdeJ2HdkCNrHq2VoQ_YJFYi7fMEVPYB93llSthGwCLOC4FdFFYCfhwNV-sdTM28wB-aBsTl9qEmAHeiy3EymwllCTyCSMfwHBu5KgjTrX6W0W_xA7QBOyX3zjaS16bI-YBK0vWDLxSkUWjC27BkC1CIcgGIrz5QkXplCIRNEYCUjnueBrYPCf8oXgRKlO296Pj3rfeK_nkjr_LeYQ7D78Vemcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور پاکستان با عراقچی دیدار کرد
🔹
محسن نقوی، وزیر کشور پاکستان امروز یکشنبه با سید عباس عراقچی، وزیر امور خارجه ایران دیدار و رایزنی کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/656781" target="_blank">📅 11:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656780">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
آغاز عرضه گواهی اسقاط خودرو از ۱۷ خرداد
🔹
عرضه گواهی اسقاط خودرو با نرخ جدید از ۱۷ خرداد آغاز می‌شود و نحوه اعمال آن برای خودروسازان مشخص شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/656780" target="_blank">📅 11:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656779">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKSVmL72poh9xVavKIAHLfYK9aF8IgqxHc7yVS1OK4tNzOy3dwnUYqok1AybGLnEYlBWqZKvRh2MBfFcZpQV3TDWvNX3dewUVp-PF9ge80aMI5xCuKbzdV64mMiPLBNOJM4L6AvijNMi64Pls0iZaUyhiDfaP_iy62LoLXxiwnvP2HnwurtrwzoiFneDk-Z9nSL6J8Ci2Ze2RomAizaGdvjbKkgS6catmhpoo9UFEJUZhhwwV8gL_5c7OmHn8Zxf7mOGxdX_csP8oX9e3WP9X_LvB5tyU8127S7RjCZaXRr6CmXqqxYpR5dopQZoyOo-ibd_DfGZmaTDJxZJljd6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر کشور پاکستان با عراقچی دیدار کرد
🔹
محسن نقوی، وزیر کشور پاکستان امروز یکشنبه با سید عباس عراقچی، وزیر امور خارجه ایران دیدار و رایزنی کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/656779" target="_blank">📅 11:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656778">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
جزئیات ویزای تیم ملی برای بازی‌های جام جهانی در آمریکا
🔹
برخلاف برخی ادعاها درباره «ویزای ساعتی» تیم ملی، پیگیری‌ها نشان می‌دهد اعضای تیم یک روز پیش از مسابقات وارد آمریکا می‌شوند و پس از پایان بازی به مقصد تیخوانا در مکزیک بازمی‌گردند.
🔹
پیش‌تر سفیر ایران در مکزیک گفته بود تیم ملی باید در روز مسابقه وارد آمریکا شده و بلافاصله پس از بازی این کشور را ترک کند.
#جام_جهانی_۲۰۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/656778" target="_blank">📅 11:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656777">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
معاون رئیس جمهور: تا تراز اكولوژيك درياچه ارومیه هنوز ٣ متر باقی مانده!
شینا انصاری، معاون رییس جمهور و رییس سازمان حفاظت محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
سطح تراز درياچه ارومیه ١٢٧١/١٠ متر بوده كه نسبت به ابتدای سال آبی یعنی اول مهر ۱۴۰۴، ۱۶۰ سانتی متر و نسبت به سال گذشته در اين تاريخ ۸۰ سانتی متر افزايش تراز داشته است.
🔹
مساحت پهنه آبی درياچه نیز تا تاریخ سوم خرداد، ٣١٠٠ كيلومتر مربع  می باشد كه نسبت به سال گذشته در اين موقع حدود ٢٦٠٠كيلومتر مربع افزايش سطح داشته است.
به لحاظ شوری نیز در حال حاضر غلظت نمک حدود ۱۶۰ گرم بر لیتر است که نسبت به سال گذشته حدود ۵۰ درصد کاهش داشته است.
🔹
با وجود افزایش قابل توجه ورودی آب به دریاچه در حاضر تا تراز اكولوژيك درياچه هنوز ٣ متر باقی مانده است. از این‌رو شرايط درياچه اروميه هنوز به پايداري مورد نیاز نرسیده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/656777" target="_blank">📅 11:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656775">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ9DOqZs7zHEaahbIfoveWavp71hW2nSE3QS-9u_GwazTsHK4QoEuGB-s4UIaOj2Ywjy_bLrDWuYoPTEJeEVb34leoQud9jAo1_LHy7QIlg_ZD7oEYHMIkHMKI9oLc0UdCYmFxlJz0D-dV6qTstjsAmkINalodZ2pMwukwoKxr6XxAeg4ygjnst20hflcPySEfkRvacBPVgDbKBNPKEDi_DV90WDdfPOCkPomn_62_Z0i75yFZXOAbn8HMmCxdrz1Pk2jhwhCc0_PwB_QA1OIvxg8KNmXqNT2qUOmWXKzcygQ5Vd1ONQhFFMBRw_gGgj_CHPBqIfCfgJEsLNlPdorQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تمام فینال‌های جام‌جهانی در طول تاریخ با پنج قهرمانی برزیل
#ورزشی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/akhbarefori/656775" target="_blank">📅 11:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656774">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e851e12eea.mp4?token=VhTBHcJZhK99-FBB15qkrOzjODfpV8aqtsVtxf_suJ6XweTD5SPSRyn5oqH2YtagM5g4SeoJc_KThHnlICiAy4X3z2kDidwdvm5q7CJKAf1AQN-QGsGsjmQwEZiwpotmVGW0r4IKUOJQZpfhYCBQO8TOugzUaykacRMOs3nUbMDVlVWbr0RuvNVR1QE5eSBmYai9D3jQBSGMTB3XoygMSWYFVcvYKn83tzyWIwDYCKx8lIGw3neEOwuEvW9sYNoViASgCr-hz0D3GsSI8oeRF_FEpXxlweTsNBAxIVM5tOpRxK6i7ee2iXVZHNX61Hp9V4Xbzc_QTfciFz9emfpBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e851e12eea.mp4?token=VhTBHcJZhK99-FBB15qkrOzjODfpV8aqtsVtxf_suJ6XweTD5SPSRyn5oqH2YtagM5g4SeoJc_KThHnlICiAy4X3z2kDidwdvm5q7CJKAf1AQN-QGsGsjmQwEZiwpotmVGW0r4IKUOJQZpfhYCBQO8TOugzUaykacRMOs3nUbMDVlVWbr0RuvNVR1QE5eSBmYai9D3jQBSGMTB3XoygMSWYFVcvYKn83tzyWIwDYCKx8lIGw3neEOwuEvW9sYNoViASgCr-hz0D3GsSI8oeRF_FEpXxlweTsNBAxIVM5tOpRxK6i7ee2iXVZHNX61Hp9V4Xbzc_QTfciFz9emfpBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه دیدنی فرو ریختن یخچال طبیعی در گرینلند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/656774" target="_blank">📅 11:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656773">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGMCw1B4CPO4NBQScy558t1JdqRPReMYiU_VTrux33eUloGhv45_9ySGv_j4RcAnk3H1pgExUxhuM3k49ryFdstXOjrMindPA7wfdw7fOuS63spzCgmkMNttWlIJR6N_tUYX0yVVK5X3xL1AJ3fhn2OlOzO7yotZWsuBSpqfisxbvIq_7964GNIXtSw2pplAsy3jaWOvoLVf4kaYlK86QWYjcPjEG8UiqTGNUNQqpQdFxpPZ-g4Balvkx4cFMvDtKqRJkjaYRLyCU-h9qj-06myyS7shIEJ8_FvvkpZ43o-W7u1d5tfLo6Yi9aRofvb_1hvf7TtTyzgYycr5OFoDsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir
نوشهر
📍
۶۵۰ متر زمین
۷۰۰ متر بنا
تعداد خواب ۴
مهندسی ساز متریال عالی
فول فرنیش استخردار
شهرک ویلایی تکمیل
سند تکبرگ و مجوز ساخت
محوطه سازی حرفه ای و زیبا
🔻
برای خرید این ویلا و مشاهده قیمت و عکسهای بیشتر به سایت زیر مراجعه کنید
👇🏼
:
https://melksell.ir</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/656773" target="_blank">📅 11:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656772">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aisadZ6Mfgla89aQo8GWtKoZKias1lILeI5369Qk7JhSeJJpkAzb-lBlI8z-v-K_INitZ61VM3EU3C1r9KNrOa4otEXIUsoJTcoByV80ZfZreKv7sLGfg_3emElQJqfbRwpuqpyNAAAN0GG7l8IQ5KdfuiCSd-HnowVn18IQ0dhbAUgKNWOtYcSX4qradnr9BcpVTYdeYoLHOtbKCy5aXBpTjGcEwN10BC8hn5JFd7mQ13I9-bRqMOPEMd8_1Ep5YpzVPHN32XIAPy7ZsSZegE2SYUI7e-6m9PZbRZhA99ZHpoeN9hCGZPypnO2T8Um0YSYFF898krsnYEzyt_WWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: تا عقب‌نشینی خفت بار اسرائیل نبرد ادامه دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/656772" target="_blank">📅 11:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656770">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b5b35804.mp4?token=j4cUAuauWqhpX4URlnIawEF5GTIuqXYjB7tevSp4oBjZVkE9Bt4-wmqnywmm7ZvXfkh_0r5aa9q7EUKE8ze_FPE-05pCZLIhOpQxsqogrwZkGuqUIP8oNHKXsHwbbevUlWhhE56_t9bJMkXnPzt4iV9r4i3zMuQQm0xlNmwO4qwxsnNHNeAj1IWxa-8qFRR_L-8muIsLXWfVMc4dreWgXrRPPOdxHrWFTQ1OQR36cUmqw2k0KxHJXJHNFQtpx0hEJrvNb-1Rn4u7bWXE9279rpNV30ZyUXdcAuYM6jNhgPKNANU7_Oi9R1myW2sfY8FkAfE5f005LRUbnoJtk4goWTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b5b35804.mp4?token=j4cUAuauWqhpX4URlnIawEF5GTIuqXYjB7tevSp4oBjZVkE9Bt4-wmqnywmm7ZvXfkh_0r5aa9q7EUKE8ze_FPE-05pCZLIhOpQxsqogrwZkGuqUIP8oNHKXsHwbbevUlWhhE56_t9bJMkXnPzt4iV9r4i3zMuQQm0xlNmwO4qwxsnNHNeAj1IWxa-8qFRR_L-8muIsLXWfVMc4dreWgXrRPPOdxHrWFTQ1OQR36cUmqw2k0KxHJXJHNFQtpx0hEJrvNb-1Rn4u7bWXE9279rpNV30ZyUXdcAuYM6jNhgPKNANU7_Oi9R1myW2sfY8FkAfE5f005LRUbnoJtk4goWTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله پهپادی به چادرهای آوارگان در شرق غزه
🔹
تصاویری از حمله پهپادی یک «کوادکوپتر» رژیم صهیونیستی به چادرهای آوارگان و شهروندان فلسطینی در محله «الزیتون» در شرق شهر غزه منتشر شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/656770" target="_blank">📅 11:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656768">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2138dffc55.mp4?token=e-rvPZm0djVM5f4nEb0y8WYKSWm0Y869QsvEYKAw-zJ7-h13cYwG1sD-gKYZadbnp-m-p76Gg3CNKSLuPiB8bX6PMLhPNUXxwU_tfEpA1Ob1NdC57K0xQnNj7kQ08Z6E-v93ffwpBOpwCcSoP9kvoMstonVs5h-w6HS1Z6nxzivW9mjCV0bNac6uiBY2qwr7IV-ZjF7GZwylb2Tq3XKbr4MfuP1XEfcWKLLaMukt6V3J0zsEmQz6Hrr3TDFLu-iMw5EdEoaRkzlDjFXurdrcdi0D0hgjOXT766ZLR_jczrKFL1_Rhy42eud7AdYHVSHn24iG0vWM_J7oDvXHBhrhLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2138dffc55.mp4?token=e-rvPZm0djVM5f4nEb0y8WYKSWm0Y869QsvEYKAw-zJ7-h13cYwG1sD-gKYZadbnp-m-p76Gg3CNKSLuPiB8bX6PMLhPNUXxwU_tfEpA1Ob1NdC57K0xQnNj7kQ08Z6E-v93ffwpBOpwCcSoP9kvoMstonVs5h-w6HS1Z6nxzivW9mjCV0bNac6uiBY2qwr7IV-ZjF7GZwylb2Tq3XKbr4MfuP1XEfcWKLLaMukt6V3J0zsEmQz6Hrr3TDFLu-iMw5EdEoaRkzlDjFXurdrcdi0D0hgjOXT766ZLR_jczrKFL1_Rhy42eud7AdYHVSHn24iG0vWM_J7oDvXHBhrhLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیویورک‌ پست: پنتاگون به‌اشتباه با موشک ۵۰۰ هزار دلاری یک بادکنک پیشاهنگی را هدف گرفت
نیویورک پست:
🔹
دولت آمریکا در جریان ماجرای پرنده‌های ناشناس(UFU)، یک موشک
۵۰۰ هزار دلاری
را برای سرنگونی بالونی شلیک کرد که بعدها مشخص شد متعلق به
سازمان پیشاهنگی
بوده و ارتباطی با پرندگان ناشناس نداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/656768" target="_blank">📅 10:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656767">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/aba2cc55d4.mp4?token=snFUWeZsdZzOxzZ19LnZd8in21r3IwvXNmnylbu-lozhQgzRGOSmntcOesbgW8sbs08VlfuZbhUIsYpMLqKO53Shz-aivR6jxxUlMnyIlCJPLlG-vZgBYhUaBXAN0LhUflS1vRn8DpPSpgBfSuiaPOv5LxotA6TVy1F85WaAFXBslyM3zdBnsnWL_3gcDKK7s4gHGvSJYPbwKi9286oi6J1Z8udsA0FYOxZc-7GA4vDh9NWCd63us5IZh97QSBHGuvGHLsIIWeaJnn77e5c6va-8Iz-4Hl7ARGjet6us9ieRqUgmyWPpYXuuP6NJBWv2Vb2KabVjFZjeu1WuJl_0oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/aba2cc55d4.mp4?token=snFUWeZsdZzOxzZ19LnZd8in21r3IwvXNmnylbu-lozhQgzRGOSmntcOesbgW8sbs08VlfuZbhUIsYpMLqKO53Shz-aivR6jxxUlMnyIlCJPLlG-vZgBYhUaBXAN0LhUflS1vRn8DpPSpgBfSuiaPOv5LxotA6TVy1F85WaAFXBslyM3zdBnsnWL_3gcDKK7s4gHGvSJYPbwKi9286oi6J1Z8udsA0FYOxZc-7GA4vDh9NWCd63us5IZh97QSBHGuvGHLsIIWeaJnn77e5c6va-8Iz-4Hl7ARGjet6us9ieRqUgmyWPpYXuuP6NJBWv2Vb2KabVjFZjeu1WuJl_0oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ما را به محرم برسانید فقط
🔹
شستشو و غبارروبی گنبد حرم حضرت اباالفضل (ع) در آستانه محرم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/656767" target="_blank">📅 10:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656766">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4292617c2.mp4?token=IhzytgxXuRy7htdt1jq42mLzkPaK-gNdOFetas6fCGwy1q5MlOKn_CDinxexh2Fez6p8XFEVFY7jbbE2MuGXRv2igAUl02g-bReozFS_agixwbFijDOGTzmj2ixVsQTUjS9l_GNG0dVaWxFtGH_-gISu1teAhVZwJAVlPecTOlXjBICx_d1WH9IOUjCczAbLWpbAw3qO-jYWTN3IVzDJxh07pezus2wWPXwZ0AHdYPVJONoLT_XYKQfq_gOw8Sbsrbd0iiAbp05ggNLIr2UHtr1i-qvTIdgahNIMVLx0u1_V4uyfY7Ui8IujWxuBLgfCE6rtx8Qu0a5wCYRv5bubDjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4292617c2.mp4?token=IhzytgxXuRy7htdt1jq42mLzkPaK-gNdOFetas6fCGwy1q5MlOKn_CDinxexh2Fez6p8XFEVFY7jbbE2MuGXRv2igAUl02g-bReozFS_agixwbFijDOGTzmj2ixVsQTUjS9l_GNG0dVaWxFtGH_-gISu1teAhVZwJAVlPecTOlXjBICx_d1WH9IOUjCczAbLWpbAw3qO-jYWTN3IVzDJxh07pezus2wWPXwZ0AHdYPVJONoLT_XYKQfq_gOw8Sbsrbd0iiAbp05ggNLIr2UHtr1i-qvTIdgahNIMVLx0u1_V4uyfY7Ui8IujWxuBLgfCE6rtx8Qu0a5wCYRv5bubDjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حکم کشتن ترامپ و نتانياهو صادر شد
آیت‌الله جوادی آملی:
🔹
امروز ریختن خون ترامپ و صهیونیست‌ها خواستهٔ امام‌زمان(عج) است
#WillPayThePrice
#هزینه_خواهید_داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/656766" target="_blank">📅 10:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656762">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7301e98b8.mp4?token=f5MRdgfMUVhWEK7VNugRsa-P5UdjYXbAkV4Hj3CMEp6wI7ApF6kiQ-VMG3WUbuhJvJ8aeODJfVc48Xig5dyrDcT6emPEU2lk1ebZCtRs8Rk5kgGb_Co1EtrzhgaS_W1vzIzr5t_Ter-YCSDrdJQPnNGTt40IwMpEulhNnJRJEHQ1wLtLFAIl64DatdMRIUEyr7mqdkLcM0CGZ4r69dWU4wSMRW1SQQx__dsvSedTM66ZNp1XCQ5YjuHKBi_Qe5nSzRPjzup3NZa5g8m1sLMuP-F80JlyBX5KHHEGT1RiF_G3Ug9LISzdFRn8_y4noOoZ9I75Co7QT0QeM05yjBzu7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7301e98b8.mp4?token=f5MRdgfMUVhWEK7VNugRsa-P5UdjYXbAkV4Hj3CMEp6wI7ApF6kiQ-VMG3WUbuhJvJ8aeODJfVc48Xig5dyrDcT6emPEU2lk1ebZCtRs8Rk5kgGb_Co1EtrzhgaS_W1vzIzr5t_Ter-YCSDrdJQPnNGTt40IwMpEulhNnJRJEHQ1wLtLFAIl64DatdMRIUEyr7mqdkLcM0CGZ4r69dWU4wSMRW1SQQx__dsvSedTM66ZNp1XCQ5YjuHKBi_Qe5nSzRPjzup3NZa5g8m1sLMuP-F80JlyBX5KHHEGT1RiF_G3Ug9LISzdFRn8_y4noOoZ9I75Co7QT0QeM05yjBzu7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین خیمۀ عزای محرم در کربلا برافراشته شد
🔹
درحالی که تنها ۱۰ روز تا محرم باقی مانده، این خیمه با نظم و تزیینات ویژه برپا شده و کربلا را در آستانه عزایی باشکوه قرار داده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/656762" target="_blank">📅 10:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656760">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
معاون وزیر نیرو: هیچ برنامه‌ای تا امروز برای اعمال خاموشی‌ها نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/656760" target="_blank">📅 10:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656759">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P36hX8MHCCmbWfLK2dbROOrfEzMVOVtFV23hZLPaQLbvTCmdCnET6ZNftEvPG2cXirEKYWyppKAsjofH6vdo3RcEuSY2cXzA7p3Qe7QSbinAnxHFmDRj_kZiRcFkcKHQaCvLx64BdscF3TvDyypKon_Q3kTPftusry9_4MiWSjtvhdwjhXc2-HNAeMcTzh9OYmbKWbRSU8GWIJRYnBsHYyUlfJrH9w7Zuf8m_NLL0JottVVccU9_YxyG0UonCfUglwSQ8bE5t2IFxj28LhO-vlaEk6w92CjEZNDiaQRm2jiiUo3ZhGQPAHeuMpVrm7MgtuvYbN_b3zsgY_A7dUlYNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز یک شروع پرانرژی؛ فقط یک لیوان آب ولرم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/656759" target="_blank">📅 10:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656757">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
آغاز مسیر تیم ملی ایران از سانتیاگو به تیخوانا
🔹
تیم ملی فوتبال ایران پس از توقفی ۲.۵ ساعته در اسپانیا، سفر خود را به مقصد تیخوانای مکزیک از سر گرفت و پس از سفری طولانی وارد محل استقرار خود خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/656757" target="_blank">📅 10:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656756">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9518161dc9.mp4?token=MolouWFvjeRGZNnf-0dT7RGn-tAORP4yfnDqbkw9w0ImqcqxFvdJ654ozg6_CSI7AK8_CbnJvWmsQIvcJaWOtt4XsGlSzJMQYW2T9CWhNvOjHiszSISRxqt9P4Au-YWHjyjp7rC_l-tRIFovPbKHjYx3KHnO1u8_zFk76aKBJ6DeR2nKqt4iTFO8ZzPVeloZCim027KBRi7c9GiR7a0OrPLKneAVg-2A3USxLj6GnPCJ2nIUU1-MtEEUxs9_LopuLLy0gw4_7J7cn1Dw3bC6mSvH4TM6w8_1J3atVa3AyGnRD7c5o7tTLJ1-rZJgqbY9Ngrn0S1vjoCH_crqbI6X8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9518161dc9.mp4?token=MolouWFvjeRGZNnf-0dT7RGn-tAORP4yfnDqbkw9w0ImqcqxFvdJ654ozg6_CSI7AK8_CbnJvWmsQIvcJaWOtt4XsGlSzJMQYW2T9CWhNvOjHiszSISRxqt9P4Au-YWHjyjp7rC_l-tRIFovPbKHjYx3KHnO1u8_zFk76aKBJ6DeR2nKqt4iTFO8ZzPVeloZCim027KBRi7c9GiR7a0OrPLKneAVg-2A3USxLj6GnPCJ2nIUU1-MtEEUxs9_LopuLLy0gw4_7J7cn1Dw3bC6mSvH4TM6w8_1J3atVa3AyGnRD7c5o7tTLJ1-rZJgqbY9Ngrn0S1vjoCH_crqbI6X8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار هالیوودی با خودروی پلیس؛ متهم دستبندش را باز کرد و پشت فرمان نشست!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/656756" target="_blank">📅 10:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656755">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_KudCFnwLsPIB-uhBbDpNObHiJ5tlvRYKs-9_ffw_D08OhW9at55gBL7fB7RnVRWsgRxQKIEpapI2Z5YYyOPqfN5e2emrTF3qVj_5Vd2dCy3eaXd9Fer66Q6wNhGIGIFOffg1nC0zvfv4lsLt1w7fr31s0XfKIJSA36jGl5am6DrgC7QJirt5vMsEY9fDzVwUYqKYOCdana0riEDAf6m5Ju3qQmElv1tPm6vVKUDczbPfDfpouxWaEuU10XcVERgAcbglD47RnEwqNf5ds264iIC6ByZSdLhgfNK6eNFZjZewa551tZ-AFw4I-xbra_87Znc27L8mUCHCMsEtdHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/656755" target="_blank">📅 09:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656751">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7e0e5bb6b.mp4?token=H-bTI3yvJMjUVWjy4522O4boDKnKXQ1cVES3YZ91FzSWMQyl22VQck_DhtDJTTRPHBmtA953fySjnJAEL7wcUAKVBvILNPWuiPeul2GoX_ifC7bgvBseuGZb-qK0RVmXFzOOVL-wCRiXP_BtcVMJituiVmNrTVq06GSfA4rQf3pXYbKSWPgs0yrVkVkXqa8fTVeVAt_RGMh4k8tZeUYhjRtmYJ6xZb04H_7Y0GlsHZdUOJyLK0KALF0jkuekUJ1BIYUMyUbVIo1q7AMWxd19sDrdoPATQFzdDCs8MMImq5W6yQd4WC4dI80ymxL_niHkmD3BT8ayqqKsy19t_u4RBoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7e0e5bb6b.mp4?token=H-bTI3yvJMjUVWjy4522O4boDKnKXQ1cVES3YZ91FzSWMQyl22VQck_DhtDJTTRPHBmtA953fySjnJAEL7wcUAKVBvILNPWuiPeul2GoX_ifC7bgvBseuGZb-qK0RVmXFzOOVL-wCRiXP_BtcVMJituiVmNrTVq06GSfA4rQf3pXYbKSWPgs0yrVkVkXqa8fTVeVAt_RGMh4k8tZeUYhjRtmYJ6xZb04H_7Y0GlsHZdUOJyLK0KALF0jkuekUJ1BIYUMyUbVIo1q7AMWxd19sDrdoPATQFzdDCs8MMImq5W6yQd4WC4dI80ymxL_niHkmD3BT8ayqqKsy19t_u4RBoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران فعال‌ترین آتشفشان ژاپن
🔹
آتشفشان «ساکوراجیما» دوباره در حال فوران است و شهر «کاگوشیما»ی ژاپن را در خاکستر آتشفشانی فرو برده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/656751" target="_blank">📅 09:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656750">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSc8aQ-RFXOrD1xXCoUzYWO4KNljvV1HfIq4fzlGmFpD8QzMQuC4uLeb272lro6nXhVF8-kiQN171sR65dGjkwH1BZYA38vVj60updwDnF1IsdygdKToGB1Qv3vqq6qqDBZH0rBrYAD2UI_cUVkYqQSs2YJiDuhB6Z1YAWa697vElLhMpcRLeGnPCy8BdPjyXCdp0kbG33xFkkBfCIvfItahU6pNXBDEsv7zY94E69QLebkYgwfql8Dh0oL1uoPuDcP-MKNuDDtdnTg_Ah5FfOcdbanyTkOGxFSzKf_b_ZNL7EMJmqxsvc-Auusrmb9qK-YWeduGFUCPopSUsuLy_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیک‌تاک با اولویت دادن به ویدیوهای احساس‌برانگیز به جای روایت های رسمی باعث شده ۶۴ درصد جوانان آمریکا تحت تاثیر آن مخالف جنگ با ایران باشند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/656750" target="_blank">📅 09:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656749">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c78TekoP0wXd3QUcoU5eH4r_nhYVtUr2ZERW6Eh9JGjhOVo7YaNe-o_AodaqWTuWiY-LSP-gL1DK_B8uWlPJyPfM3J87puTLYRiE7DsqBy7sNGNPbXP-316Sc6wCMY9AzB1yqNoaTyVU3Jk-CTujuv1uhlq4mZHMIsK80daU0LNeTU5xKg58VL27bHxdJdmMXstca_IxIbf-_cpAAJJ3AxXwKgUahtU71yxUcD5edmjSUnzYGJV5yHhJFnivbdeWUM7DaDqm8aqS-V0qmU7WgQZT4roRPgoP-fPSBYrpm9Wv62peb5vvkZ1dVhPfpoL6SODI-TyEBnaCumsWUpLQyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس روز ناسا
🔹
عکس روز ناسا مقارنه سیاره‌های مشتری و زهره را در سال ۲۰۱۲ با پس‌زمینه‌ای از غروب خورشید به نمایش می‌گذارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/656749" target="_blank">📅 09:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656747">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MsU0ogIKONTKi3A6uVWEefnwbxTBtoIOnhbUgW5Vx53CM6pWOE4D-pidNHvjlY9itckKAHqvo80l9Kpk0Y8w5qD4c5KcN1jx9KkHKFV2-oOZMo-RfyZ7IwTFr4ZDv74BuLzO7YD7gRmB0Om8U5t9r-zryGwjucFj0BuBvdNMTd-ANqQAZtyZfhsOOW0MtA_B7h_3FnqeVrmQvcbFLb4ANUIRJWFLNY4NTbwnZLcYvSjf7cvuccYdGUKJoL4F1UKwvo5-CMTL_-uGjchJLfOav1uf9YtQFPR-lvl8-StgywIua8DMmY9ihyB6m4LSU1lZuVcePt7aN6bSLTZXQNvUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایالات متحده از آماتورترین میزبانان در تاریخ تورنمنت
سفارت ایران در سیرالئون:
🔹
کاملاً شرم‌آور است که فیفا جام جهانی را به کشوری سپرد که حتی قادر به رعایت ابتدایی‌ترین تعهدات میزبانی نیست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/656747" target="_blank">📅 09:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656746">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
جمیله علم الهدی: رهبر شهید انقلاب پس از پیروزی آقای رئیسی در انتخابات صریحا به من گفتند در امور اجرایی دولت دخالت نکن
‌
همسر سیدابراهیم رئیسی:
🔹
رهبر انقلاب در نخستین دیدار پس از پیروزی شهید رئیسی در انتخابات، صراحتاً از من خواستند که در امور اجرایی و مدیریتی دولت دخالت نکنم و من همواره خود را ملزم به اجرای این توصیه می‌دانستم و از ورود به انتصابات و تصمیمات اجرایی پرهیز می‌کردم/ خراسان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/656746" target="_blank">📅 09:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656745">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94f9cb3895.mp4?token=L0uOixEfCDQwF0OUVLcV4jZpEP2XZ1Jz6kuaXBxS6z0kMlQo-gjOlGX--x1-jGkwoNn3v9474XKHETT5pRfhDi-lXaPwVj3Cfvt0FoMxWHO49KqD9VfoFtQdKR7O7vRMn6rX-JGq1iJfULxjtfiaDdJ95WTjvNjs_pE2cVDGDEEosA6Lb1rTAi18uwsAbNsjMINl8q-g0aFG2IG6tS8MeqGsMofOtzpIXow3EhRM4Qjud5mDuaRvCCA2FO0xsRhl9iglV53BOHRRN0kOUVMps3ahPEROnm9NluX9GW0HRV3roxWPK3pcmHBvcabR_-53o2h7IqF8zLeKjmyETg-gRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94f9cb3895.mp4?token=L0uOixEfCDQwF0OUVLcV4jZpEP2XZ1Jz6kuaXBxS6z0kMlQo-gjOlGX--x1-jGkwoNn3v9474XKHETT5pRfhDi-lXaPwVj3Cfvt0FoMxWHO49KqD9VfoFtQdKR7O7vRMn6rX-JGq1iJfULxjtfiaDdJ95WTjvNjs_pE2cVDGDEEosA6Lb1rTAi18uwsAbNsjMINl8q-g0aFG2IG6tS8MeqGsMofOtzpIXow3EhRM4Qjud5mDuaRvCCA2FO0xsRhl9iglV53BOHRRN0kOUVMps3ahPEROnm9NluX9GW0HRV3roxWPK3pcmHBvcabR_-53o2h7IqF8zLeKjmyETg-gRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اوضاع لس‌آنجلس، یکی از شهرهای میزبان جام‌جهانی فوتبال
‌
🔹
علیرغم جمع آوری بی‌خانمان‌ها از شهرهای میزبان جام جهانی باز هم خیابان‌ها شاهد حضور افراد بی خانمان هستند
#جام_جهانی_۲۰۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/656745" target="_blank">📅 09:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656744">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
کالابرگ از ۱۶ خرداد وارد فاز تخفیف می‌شود ‌
🔹
خانوارها می‌توانند با ۱۰ درصد تخفیف لبنیات خرید کنند و احتمال افزایش تخفیف روغن و تخم‌مرغ نیز در دست بررسی است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/656744" target="_blank">📅 09:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656741">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/656741" target="_blank">📅 08:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656740">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
امتحانات دانشگاه جامع علمی کاربردی غیرحضوری شد
‌
🔹
امتحانات نظری دانشگاه جامع علمی‌کاربردی (۶ تا ۲۱ تیر) آنلاین برگزار می‌شود،  امتحانات عملی ترکیبی از حضوری و مجازی خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/656740" target="_blank">📅 08:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656739">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSTu9OHXhXb3CgukL6e9XXXcFIic1B8DB6ZMh00eQp41oz7Kt9tX49c-owaI2_uT3sharjxUK0NLr2vF3eo4Se_08h-_XyrmknfX_ntFYwR9hXJbhKSD6jYP4SW9zikDsDqxI1u2zhEb1S_jPDdZZ8KFh8_kgRvWZlyTJsLbBp2lq61w3vh9_z2XfYlsuxq-Ng-q-EnY4Vye-X90cmxOQWqCIYEsncvkEVPhNJ3IlpojzNolF5sdHXcsIsa6O1lHaYUtl9E31qqLktDLamKQbul3R-ZmfU9iLRHUTokhOAqGbYnjd6s83-Ocos9rlneRIeR1MM27YPFPuX2IVE4EnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از سردار سیدمجید موسوی فرماندۀ نیروی هوافضای سپاه، همراه با شهیدان سیدحسن نصرالله، محمدرضا زاهدی و محمود باقری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/656739" target="_blank">📅 08:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656737">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovoFF97MULu1p-na0C-GXheUVsUgirq_7UPa2eQdu1TLOzObEvcbP_YlvTF6aQ8vbqvWi5W76d1dWCWIx-Xb_PIZsDnBYjCvejM6p1yUlr3j5qfWS5TnZOU0Zu7klxaK7JQhekHTnY4_IhJvkqIM11APSJG552wEuysA319elYEZKpCm9cpHutqXTIGpFPG5uKUGRCeFxBknBKiERi_GwUau-u2rlODd6kDx1Ajroy4C3ptinvqK5rLZmR7LIJrQX3oqQ7r-v9ndxss9rrPiI-3a5U3zyjHFRosWhtEhLxe-GfZrDB5fCAbgSRkYU2D0xijfeU1AfF42SJMztqhafA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امریکا در فکر بالاکشیدن اموال ایران برای بازسازی کشورهای عربی
🔹
آمریکا در حال بررسی راه‌هایی برای انتقال دارایی‌های ایران به متحدان خود در کشورهای عربی خلیج فارس است تا به تأمین مالی؛ بازسازی و تعمیرات ناشی از حملات ایران کمک کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/656737" target="_blank">📅 08:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656736">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf320a24b.mp4?token=Eldyrgf0NEVsBsyklYODaSNE-dMGu8kbxdqVp2N9KWLBFHMCSCY2ZBbhxBa4UXhLP0hnrfgBxQpyqF5QWzHX0fN7ADKRR9DRsTTGlmnIjoBM4NnFxJy9PJxix7Z8W4tX7GApv2ifuUkuVoxQJqN0i16n6fq_6OgDNx3S3XprMFUkTidTXVBENlwJmHe_Tzxki_UeebanV9WtERXKtMDnY_ZF5b6621sJn6OGQFl1zV5NiAGW7J_ckrWv3fiZ0gOGAT0UYnodCI_ZUspZNLoJTjEgGb1Hlyf5GlqLqVQfpUWGKaHgYuS8tX22QV5OsixqqWCOjl2CC4fMeAF-FQZgIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf320a24b.mp4?token=Eldyrgf0NEVsBsyklYODaSNE-dMGu8kbxdqVp2N9KWLBFHMCSCY2ZBbhxBa4UXhLP0hnrfgBxQpyqF5QWzHX0fN7ADKRR9DRsTTGlmnIjoBM4NnFxJy9PJxix7Z8W4tX7GApv2ifuUkuVoxQJqN0i16n6fq_6OgDNx3S3XprMFUkTidTXVBENlwJmHe_Tzxki_UeebanV9WtERXKtMDnY_ZF5b6621sJn6OGQFl1zV5NiAGW7J_ckrWv3fiZ0gOGAT0UYnodCI_ZUspZNLoJTjEgGb1Hlyf5GlqLqVQfpUWGKaHgYuS8tX22QV5OsixqqWCOjl2CC4fMeAF-FQZgIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یک حرکت عالی برای تنظیم لگن و ساختن عضلاتی که پاسچر رو اصلاح میکنه #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/656736" target="_blank">📅 08:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656735">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d89eaf78.mp4?token=tsa_obDRCHKXiRhW3NANGiCbKeJIb_Niz_XJ3hn5Wzc-Mh7p2WrBLSqktPPXUsP4LZjRPiSLcpMDdu7YhRBpfne_V4UgTnE8b4qj35-JmjnvDzU4cq02xJH0_Mqo8xmZpIrfm7eMMgmpZSn5RgIH-xELH6he3HV1O9ImpYg45-c8-n7axDNt7nxTyMV21Bpq3yd_2g_IZvOUOJfSXpS9q2DE-UnTuWQzABjoSyFXsiPgm2si3sF5nyWY39OzPcfE0-fUyz3DJnnnPbgpYQzg2Ilg-5ih_T_UXaezqYhwzadvgWHcvsmBxbzpl0TKt1-BCCIYzgJBkC4NnWv653-Q0mHBJUCWiHpKhW-uFIIyDssbvcU8T3-nGlJithVhSrQ-VXNfHF9z35utxD6sj1omtxdBJUS1s_1QFe7CxFqszrjMGxS4BAwtjRaK8Q87PBEBSW3E3IMSSBaySKoCZkLEuGr9wHaeGyckwSLeJeu_ZkoxlBBQji0SA56fyEFs32q2Lvm8t9_M0D_jfyqbH1qlPTTAsbAKvmXqlQt2CW4fEqb6HGu02tP9AEBvnoqNtKQoFocjxrC6oHYpbQBXJCO1GcfwQRP7lMoYk2-GTr9AqRyJFoPoDlQ74bkTASdOJFXPhWRlv1_qxPD56Jpld8ZNa2WoUz3p7j6E2L6ZTVIDUhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d89eaf78.mp4?token=tsa_obDRCHKXiRhW3NANGiCbKeJIb_Niz_XJ3hn5Wzc-Mh7p2WrBLSqktPPXUsP4LZjRPiSLcpMDdu7YhRBpfne_V4UgTnE8b4qj35-JmjnvDzU4cq02xJH0_Mqo8xmZpIrfm7eMMgmpZSn5RgIH-xELH6he3HV1O9ImpYg45-c8-n7axDNt7nxTyMV21Bpq3yd_2g_IZvOUOJfSXpS9q2DE-UnTuWQzABjoSyFXsiPgm2si3sF5nyWY39OzPcfE0-fUyz3DJnnnPbgpYQzg2Ilg-5ih_T_UXaezqYhwzadvgWHcvsmBxbzpl0TKt1-BCCIYzgJBkC4NnWv653-Q0mHBJUCWiHpKhW-uFIIyDssbvcU8T3-nGlJithVhSrQ-VXNfHF9z35utxD6sj1omtxdBJUS1s_1QFe7CxFqszrjMGxS4BAwtjRaK8Q87PBEBSW3E3IMSSBaySKoCZkLEuGr9wHaeGyckwSLeJeu_ZkoxlBBQji0SA56fyEFs32q2Lvm8t9_M0D_jfyqbH1qlPTTAsbAKvmXqlQt2CW4fEqb6HGu02tP9AEBvnoqNtKQoFocjxrC6oHYpbQBXJCO1GcfwQRP7lMoYk2-GTr9AqRyJFoPoDlQ74bkTASdOJFXPhWRlv1_qxPD56Jpld8ZNa2WoUz3p7j6E2L6ZTVIDUhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت فلامینگوها به دریاچۀ ارومیه
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/656735" target="_blank">📅 08:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656734">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
خبرنگار الجزیره مدعی شد پیش‌نویس تفاهم ایران و آمریکا در تهران در حال بررسی است و در صورت تأیید، احتمال تحولات مهم تا اواسط هفته وجود دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/656734" target="_blank">📅 07:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656733">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69fbb7113a.mp4?token=nwhYoEFjuCWurrz_7TAe0HiIjYwg-sMK4C9fhKqqBMhF7n1QCCvv2L1eW1yH8YHoRMhBQJWT8nSucPok1s-nAPgJyBXRPGNYh2EzO8XIYRA9pLMGHFPLxGACGHC5FxraQGzaytdS2IM7QSBBuAbyJZqpQqCaY-IsQOEdtLqdeJ-rLNAfW3O9L0uEg4sMCjGPeGcb5xoVCNiCyM1puLYHULQ0g8Q0kWEhXuCi-Ppw1vntzF-gtmHv1KrfC3jzBF9lrO0kcbl0ZFcGQC_Jo-Pdc4AuuB4FVYvdtll3nzVanLxUmf9ESonzS8Puc3_0iqPleRZ-1gUTpsOToa8GK4fS_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69fbb7113a.mp4?token=nwhYoEFjuCWurrz_7TAe0HiIjYwg-sMK4C9fhKqqBMhF7n1QCCvv2L1eW1yH8YHoRMhBQJWT8nSucPok1s-nAPgJyBXRPGNYh2EzO8XIYRA9pLMGHFPLxGACGHC5FxraQGzaytdS2IM7QSBBuAbyJZqpQqCaY-IsQOEdtLqdeJ-rLNAfW3O9L0uEg4sMCjGPeGcb5xoVCNiCyM1puLYHULQ0g8Q0kWEhXuCi-Ppw1vntzF-gtmHv1KrfC3jzBF9lrO0kcbl0ZFcGQC_Jo-Pdc4AuuB4FVYvdtll3nzVanLxUmf9ESonzS8Puc3_0iqPleRZ-1gUTpsOToa8GK4fS_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آلبانی علیه داماد ترامپ؛ معترضین البانیایی: پروژه لوکس کوشنر را متوقف کنید
🔹
در ادامه اعتراضات مردمی در آلبانی علیه «جارد کوشنر» داماد ترامپ که در حال ساخت استراحتگاه مجلل در خاک این کشور اروپایی است، مردم دست به تظاهرات زدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/656733" target="_blank">📅 07:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656732">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2O6KgwMSGavpArWcb_RuoKgtgVhdjjrmBHeFguEY4bdwwwHGYIfbcOWIjfsEnu8fEGwRwv5f7lAVGJfpKvax4Sjzw2hNpgUR6ijNyrPccHNWLwottAqmxoUipHffFpD4Yrtzr-1UGdWUbcY5Ft9vVdotlWFtayiBdPgSE0mGh-Wqf8HNBjylF0yhqkIGBzWU3fo67C10pCgHccO4arGaRCym7mc-lK-voJrSQLRFTJN6sj4b04EpBlw2kyyni1b5C7w-T59yPl7W-ssP8OllonupedVzvgGSbgCZ2KHuiZSFke6eKVaL9qm4wqIzpMZaFIXxT8aXtvPhTcgpdQfyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز مسیر تیم ملی ایران از سانتیاگو به تیخوانا
🔹
تیم ملی فوتبال ایران پس از توقفی ۲.۵ ساعته در اسپانیا، سفر خود را به مقصد تیخوانای مکزیک از سر گرفت و پس از سفری طولانی وارد محل استقرار خود خواهد شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/656732" target="_blank">📅 07:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656730">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
ادعای سنتکام درباره پهپادهای مهاجم ایرانی در تنگه هرمز
‌
🔹
سنتکام مدعی شد نیروهای آمریکایی دو پهپاد انتحاری ایرانی را که به گفته این نهاد تردد دریایی در تنگه هرمز را تهدید می‌کردند، سرنگون کرده‌اند.
🔹
ایران تاکنون واکنشی به این ادعا نشان نداده و آن را تأیید نکرده است./ مهر
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/656730" target="_blank">📅 07:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656727">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت سی‌ام - پادکست کافئین</div>
  <div class="tg-doc-extra">کوروش کبیر</div>
</div>
<a href="https://t.me/akhbarefori/656727" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
کوروش بزرگ (پایانِ فصل اول)
🔹
مدیرِ سازمان شما از کدام مکتب فکری استفاده می‌کند؟ «مکتب آشوری» که بر پایه رعب، وحشت و یکسان‌سازی است، یا «دکترین کوروش» که بر پایه اتحاد در عینِ تفاوت‌هاست؟ در قسمت آخر از فصل اول، بزرگترین کلاس درسِ تاریخ را برای مدیریتِ منابع انسانی، ادغام رقبا و جنگ روانی مرور کرده‌ایم. برنده‌ها نیازی به شمشیر ندارند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/656727" target="_blank">📅 07:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656726">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6e5ccfc4.mp4?token=Z1Dym0g2fDum1-ynj5h-UNcysG6cgAuTg3yAHTWD96OtoBys6c3z8NidOvAcqWOozuPLpCOE1wGm_ZcCgNZILomheSeelvvwGDDjUGN9e6LD---Ce7c12tZSMLSVGBLCj3p9uAu5a63fVybak0NaptVuXSVoD4b437J6m7RdEbHQQjxrL8BpicNbO3uYMdigvN2Fr_axCAh7XUOufh_GlvxJ3K9skxASF7pPKPBVli3-ieuLLS7eX0NhWbrRvr3oPhN_Or6f7yaWVHNdZp0uqYQAVb3o_dACeiE1I5-1G2X-pVXEkDV-xQNiTM4ja2KMw4DR8EzUX5I69_XKU8Ek6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6e5ccfc4.mp4?token=Z1Dym0g2fDum1-ynj5h-UNcysG6cgAuTg3yAHTWD96OtoBys6c3z8NidOvAcqWOozuPLpCOE1wGm_ZcCgNZILomheSeelvvwGDDjUGN9e6LD---Ce7c12tZSMLSVGBLCj3p9uAu5a63fVybak0NaptVuXSVoD4b437J6m7RdEbHQQjxrL8BpicNbO3uYMdigvN2Fr_axCAh7XUOufh_GlvxJ3K9skxASF7pPKPBVli3-ieuLLS7eX0NhWbrRvr3oPhN_Or6f7yaWVHNdZp0uqYQAVb3o_dACeiE1I5-1G2X-pVXEkDV-xQNiTM4ja2KMw4DR8EzUX5I69_XKU8Ek6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوروش بزرگ؛ استراتژیِ «فتحِ بدون شمشیر» (قسمت پایانی فصل اول)
#پادکست_کافئین
| قسمت سی‌ام
☕️
🔹
در ایستگاه پایانی فصل اول، افسانه‌های کلیشه‌ای را کنار گذاشتیم و به سراغ نبوغِ کوروش در «توسعه سازمانی» و «قدرت نرم» رفتیم. پادشاهی که به جای شکستن استخوان‌های دشمنان، مغزها و قلب‌هایشان را هک کرد و به تاریخ نشان داد: «برای اینکه رهبرِ همه باشی، نباید همه را شبیهِ خودت کنی!»
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/uot54a9
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/656726" target="_blank">📅 07:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656725">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idMf4L4lu4BbSo526NNYZm01XvA0UOx2pk9hb1EUtCaRJM_e5Fwht8SkuwkKgumL0Nq_yCfEn9b_CnJ3VkE_5BsOMDMrd5znP4KrUB-6-z74dPwg0_kWi0IgHfXRHVCBPxmnlWcEzXreZXRWhLypVcktjfnrPyAb896e9O7S_GaI2yAlQIbn-H2BgtNU8NZfQOy-WgDizkOgSXhitpvNt4yrjzPHkQzUFIa-Q5FHaH5vwynreNUQqfawIfWRsHyXYZd9FNj2W69ILUUl6vfCA1u0Dte_80h2voqNR8veg1UD6Wx2Tj-5fVOLydpH4aHgnFIgcQ4QxVBzmMTHLeWuoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۷ خرداد ماه
۲۱ ذی‌الحجه ۱۴۴۷
۷ ژوئن ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/656725" target="_blank">📅 07:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656724">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from-Salar-via@chToolsBot</strong></div>
<div class="tg-text">تست هوش زبانی امشب
🎯
🚀
معنی اصطلاح Hail Mary به نظرتون چی میشه؟
🧑‍🚀
روی جواب درست کلیک کنید
👇
👇</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/656724" target="_blank">📅 00:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656722">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwnsQJFcMeEBE5LAm-_FsqKRSzXR7wz8ipZ5x-31ag9Jv9J5SZVxXEqxaipJanL6cDsAMCJwD0vc4W81wkZn1C6_WlkPC9yGfS3FugtW2JkYkxetT93HxXZ7K346Ecczt1FX7UAOdgYnajcdbvO1uF0HjdDUtuQnYMfvKkT95SxEu9HWQ9HhW-_VKniqUlqa2wO45g7-ScdwRyxUVjKllueiVtfxMEXEdFEQGnuRee0BG4Gj0Db1XiyuRgOltejEVePmo7UR6VkWRl3vba987ouQmo7bvsfAPMaJZIvLNBZGc1hy5iTbKyxzvaMaMYKlo1qNJ2VC82kcNla37YXMEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/656722" target="_blank">📅 00:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656721">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1Fj-ZujftFSzudirOcazjtAfkEF-eUy6lupRnHhqqKFyG4rWKng6inZeYblrvBO13vTEsV18z8MXv4E0M-b_qrGTSblxu_KydlSNcHCquhk3oHB29Qt_9_o07fNMt_wO9KS1fyqNzhXcCrEw3zRFk0k8VM1TuWuz7Qz77sFqxojMw5N1uqyxVaemRtWkVg412-LbzZP5a7j8KhpDOcVRJszWRynRDmBhp4aTY5R0ugjhe7fKICyx7kY1oAMJ3Y6W-9WXUiNyFpTvREPaXVonwfwZ1zHK1lq8geHHGPDXV7--0MQvqLI52GNHebh7BbAswWIpms8dSLdG32oXWUgPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انقلاب در انرژی پاک؛ برگ مصنوعی CO₂ را به سوخت مایع تبدیل کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/656721" target="_blank">📅 23:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656720">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبر تکان‌دهنده معاون رئیس‌جمهور؛ آلودگی هوا جان ۵۹ هزار نفر را گرفت
شینا انصاری، معاون رییس‌جمهور و رییس سازمان حفاظت محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
مطابق با آخرین گزارش‌های وزارت بهداشت و مراجع ذی‌صلاح در سال ۱۴۰۳،  بررسی‌های اپیدمیولوژیک روی ذرات معلق کمتر از ۲.۵ میکرون (PM2.5) نشان‌دهنده ابعاد نگران‌کننده این پدیده (آلودگی هوا) بر سلامت عمومی است.
🔹
تلفات کل کشور در سال ۱۴۰۳، تعداد کل موارد مرگ ناشی از تمامی علل منتسب به ذرات معلق PM2.5 در افراد بالای ۳۰ سال، ۵۸,۹۷۵ نفر برآورد شده است. تلفات تهران از این میان، ۸,۸۵۵ مورد از مرگ‌ومیرها مستقیماً به آلودگی هوای پایتخت اختصاص دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/656720" target="_blank">📅 23:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656712">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1hpJFczElYXqz5HNhDlDz_X7v9KHZr0doa4wfdIBlfucmA9JtX_K6R8716z7RQwLREqg-gAfR-mQttNrXXx46kpiyIENHN-2BL4YMqRsLDFD4JeTaqhve7CA2tQrso1hJ0aZOH2x0Kb5O8bY4VqQOYqvkMBIpE2JDcqSHSfZZzFeY8tl6WTeJOs8v55EEoesLeTfnDBU3Bk3v811r56aNMc7pRPKNt2LmvpXjx3FEAZeWNCSCj5kZ-FXcvwdstGPqqH8MN3CLViuq7bbXS8Lje-Vw0Iw7xV0IR0sVc4pMPQATUOxm_0L0VJKWJ3_SK7X7ojc0aj3GTFEObxAr1_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOO0txudDsGVaKleDsFYwlElhNSO3btjJdNnSrwSMlhci0lZaBtuHqO9nQ1M0aCF7EvkmgCEDUYEs9paLcHTHU5G-mBIUTs_mb7E13O5G6iVr_6kAXb30AmJQ51FqDNCg7rmOecPeYNH5JcJ_HQchdyIJeu8oUBZ0m_wDsaitIXVNQhsaUKIFvhadoqKfIPAG-lE2OfIwyHJZmXB_Z8WoB9YxTaaLvqHE2ZL9na9eShaHParPHbdxU2zwSwuuCqZzSBPrgY71Gt47aV6lqEevBdrfukF_Lr4IwT6lbL3W4k1IMPHeuTorYciwyqSFHQ0_hTI2bW2uSQudX9y_qu4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIRrSV686i8SgqtJhwZxCRoVTYQUd5JTZRaYl1vEtXlOb4GV2JsuzNYk0FBC7aZAgBYzBTNb_Y011RsfMXj8o3zRfJ9wpvIcpUoUuK8y1XSLsmh4gchsTxJ1S69E0sLJ_0Tai3z62ocsi2Ph3SaS0BBmSmBb3yIv0OhEt9p_CNMTBvcTyMut_ZuvOhoPaxjmB3Vt95UzOeM1SPh_qskNwAOuIcbuo_woASfe6r1Z9e1MMeKdcKAf-bbtJ4OFBq5ZKtpvhqDaFi8SRcV4JuIfjID8txLp0zSCKyl_FskdczqGTQvCKVteFi3t7v_7bEihfmRPpeg-6gTs7EXb_SSHgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofTUaRNmTp_fAMqidVH-8od2gK2PrQNVTKjnM_-mmHjy0o5FIhXm39bL4_6Nf8f3ddhLnwfNJrFYySxpQHm0S1trwGzTdhLL4KnD25SeVKqzvFij2ALyiO7HMSYhYlaOrJ6dCbFojvHwQlnQOhP8tlkl_s3-9Z9mJ4bv28-wSn2EIzPv2wALAfSuGv9_rBlPv_0AwSopMFrArtibBOOjdMvKZQui-5FXgKxDYZv9WHtQnTF6HeTs3koMoZ6dX_r_iETFFEwW2tKn9MbWOXZyvHg0tW09nuyveER_AUpB6EKe0xZIrzdVvOkYTItAaAdBts9xOnjvAFMbdCNdOpDWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feuom3g_sHIYf7KMhC9hSC1S8JvTX-epb-BT2cW9M25YjzKTuh3MF5Mo-b2rme5fTrTx_2w_01ORYYi2mpl7vyW03zVVyGnVZb6Is5VfZYYw9u5GtrOcIdbbcBWb7q5OT_vQ9DqyubeHvEM9JhVEm3JSErxJUPN_CQ9NFIehLxWcr4WI5_n4I1GTFiKv4oQqmi3i4UGEgI9UU_oGZVgdAbXWGytKBQ9rXTRxvDjLZ3q6QY7kdwgtVfQAACShsQ0CyfwssdMAOvprMPKeNbDGoiLpSFFHB6Wy6t5Sa9xCIv98gFSMoBrxiZrxlV4PR4j62xjltjsRmamLJUszy4bPyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6Rzeij8eYPyW-Nl2WXVhXJ5LbyVW0iOIjZppDP5YYcK07JuB594GyvzvnRqso_zfhNxB7ofXHtH7whQkkSAYdUvbODu0S5Sqr1gt63v77te5X1Xsy6dnZAwnF9pbWLml83lpj4uCttJE2mxWKQXyUD4VfVN7RT6whYEDNxi7tUPE4RTlvsd34LE7ObzLLbO6pSgDaglkeSjjnyUFJSObOSYl0Nk4Gq8yuINQSAHfSa48T3qQhcTnIni8oAmrUwS_u5KD8VO4XyVSS7gt3zQFrUNdff3gulvK91yPraJWcjQDmCGBwTns6rVQWl4WFILIz3seBPFPxgVR-WvpAbcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVc0zaEa36lhPHmWBLKz1k2ZLyofy97b-4APXnQBdn-uCaia4FbJbuPTdSVtMt0xweqT-JuovjKNLXUHXm-H1HZy1480XW01eFfDgkmTlVhboOOJHEQHSXINUi_9N8FpcLXavv_MkannJo9M30CaIBCIE2g6isskpqH00diq0TZrnE0vXK08636g3lSrY_0UOu4XQRdM5fFvWfkgFpUMhl-uXVC6x6OBAlS4GP0fe18TCUaCMqqVKEcjQ0BQlsaVXjBFV8pqyjsgODl4gZgfoo4maXJCVnYePAeIIA6yok6qX5xoL6isplpYtGrc0I8ssVqwKlvg8s0unPATvwWXWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
به یاد ۱۶۸ دانش‌آموز شهید میناب، یادواره شهدای میناب در هامبورگ
🔹
برای دنبال کردن اخبار و گزارش‌های بیشتر، کلیک کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/656712" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656706">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EysLYX0cKCpoCjjS6xK6fQ4YOvUHuFNrV1Tc5XC7ReWWkBPUpewk5aP7T1KQ5aSeL3ANByuobkMYqWzxa17ZZS65R2zO52Gv1kP8Yilc-CTaIuUDjcNgy828ZFaQQZ58t_E-IioIeEaIwXBsOdr_gzhtS_ZkxHdOORPpRqqhAA0UTdYqeHUGyK7W7ma2sY50CFlFYYe-GMf0S4UqfAaX_ty2vnDdgXzTzyPoxASymn-YDXRMOwBaIlSJtUeokVa6l4waEBAmGiZTvOZp_mrPZZMCTfs9oW3cHZo78BeaKCoYppfWiX-naBROHLceXP_vf50Gil130dnzCjmxnxyo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLZtsLt1p6dv9oxtdQphUoLEY_zQxhOZmXgASlSY2uJzRFhslV-8hs_j3LQNehKNoUC7feeAHL59ZXbjIefGrP7-p3SKwK8AMWNOWDkJk6va8rLnMtSNVrxeGVJ2cKWXXZbrIK0r1gbkzBIrqUA-iHhf7zUJZyMky-Jm6Lui1BQLazVjNB-5EL1bCUmtYlJ3XaTx_BYeM2T17no1hZUxD--NC8yg-xsaAMOhrVWZP7pXYRnj3G5dwzTX8YQZ8luJz83MRbJ5X_F3hg0SPCjugyYf5tZHFPakpNij8Wrg2NkIboi74klHQOfYY5EfDSWvKXAqxPjp45ia1lbJ8iLjVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkH4aCqHXPH7X9zib98LsHWT5L3araotlSRe8D3ddIg4lnhSdyTfPiADJFCF7dhcB6dKDhjicFRti49uLYlUdGmGyZZOXoDpzeO9T4u5rlJyxduWCJbQ-RQCJugFZbViPCONtWXwpAJCeWagHxwV2WQ8CBGucggZVecaPqxltEs1O7J0EbpceVWsnLMvEOCyDZbg3CpRpJOF56LsmbPbyYlOJI5Bsfo5Nt5jspY5_0_4HZkXmwGhBSgZlAh3zeYviXuZQV8PS1b3jhKaooj9TPzsltElw-E5_KuJI2XImRjnKFgK7ulL0aimi7OMc-SAQWZVev6qhmNT1wR_fs4rDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvy7skO7RwkfewHPlT8fIxIhAedPmT4JcXKQxihpIueARKUOr5ke6ISAqVTXkVZq8FlG-z22US7laB0TLIFmSyCfKOcKnfDLJH30C_BxVjPw_IhBehI72NNvxqedyrfpD4lDQQAStNU-meKWHQMel_RXUB68v-vb2kgHFG8Q6V5drOc92sNzs05szaau7ebJHHbvx5xC8JGs4tPvW_K7SgqBct9ETQy3r3q58fyHXSDeEOaoMJu_kJWjV-0aQclsTXnjyvQn-T_YYMtx4nhwQNDWYWFn12Sb3LACpKP20rkzya8XLWo9b5XlBugh-1IeSJzgoP_sz3iDojlZeFumZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDhFfsCHtVYKIWbuZhz2YNb_95VxipGQhTaeuS9bFTFx4M-nNj0Cd4QkwOHSiNEJFYD7HDzf5XjaY1WE3L0bejd8GPJ2eGs03nGI_tL83IMZYcvhe60K3wYfOn3xIlDp-68gBp5RusAR0hgmMT4pL9-b8IaIWIoYW63rBwkUo34UXoa2zmQKXGElu1EzsHUoLAr08vLIEja8HaDQwk2QALtLSIhedhPReC7QeRdFfYTzIpUFKUyrAXfPRCloFbzjCkRhcrd56Th7syHGtCCeit3VtidCAQ8RHnYtlGh5KcYanST3PnqRxMz2cYKcvA4daHhr0B3dxwFxe-dRuMlNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wr0qddcujTu7P2kktSLxS6YrjRka-h7VTG00bXdvA40fN971W8AA_jtV4XeFR4HgArxbEB22Wj23tysyr66gZxj4rYrg6PyKJtizHWp3mDxtf6l8jroe-UHpqBESQKaYhN9ArcVpfR8GTI9HU066J0x1RstOdjXrPWvVwUdVe9JAoARFI3c8KgY32mq98tMUsFT_zvNWnAXC4jMVHQ49IX_ACSTG1PYrh0FIQFSs5g89jaGOlv6JWly27iE1yLuMQJcndH3GOIfPsOTYggwXYa3_kQgIgfbAwTWfQB59fJLF0DcORGr4ph48YV-n2bZJnvbxpRyXzN2oDGgamvPyGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترسناک‌ترین سلاح‌های قرن/ یکی جلوی هوش مصنوعی را بگیرد!
🔹
وقتی هوش مصنوعی فرمان جنگ را به دست می‌گیرد، الگوریتم‌ها افراد را پیدا می‌کنند، خانه‌ها را ردیابی می‌کنند، اهداف را انتخاب می‌کنند و بدون دخالت انسان حمله می‌کنند.
🔹
۵ نمونه واقعی از هوش مصنوعی‌های جنگی که همین حالا در میدان نبرد استفاده می‌شوند را در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/656706" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656705">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
محمدجواد لاریجانی، کارشناس ارشد مسائل بین‌الملل: پاکستانی‌ها الان میانجی‌گری نمی‌کنند
🔹
نخست‌وزیر پاکستان، آدم خوبی است، اما لازم نیست ما و آمریکایی‌ها را مقابل هم قرار دهد تا مذاکره کنیم، باید میانجی‌گری بلد باشد.
🔹
اگر ما بخواهیم خودمان با آمریکا صحبت می‌کنیم…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/656705" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656704">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
ادعای منابع خبری: معاون موساد به دلیل شکست پروژه علیه ایران برکنار شد
🔹
باراک راوید، خبرنگار صهیونیست به نقل از منابع مطلع اعلام کرد که رومن گوفمن، رئیس جدید موسادمعاون خود را برکنار کرده است.
🔹
دو منبع آگاه گفتند که معاون رئیس موساد یک سال پیش بودجه‌ای معادل یک میلیارد شِکِل (واحد پول رژیم اسرائیل) دریافت کرد و گروهی شامل صدها نفر برای پروژه سرنگونی نظام ایران را تشکیل داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/656704" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656703">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
ویدئوی منتشر شده از حمله دیشب آمریکا به قشم و سیریک
👇
khabarfoori.com/fa/tiny/news-3220813
🔹
ایران و آمریکا در آستانه جنگ سوم؛ دیشب در تنگه هرمز چه گذشت؟
👇
khabarfoori.com/fa/tiny/news-3220762
🔹
گزارش لحظه به لحظه از مذاکرات ایران و آمریکا؛ نامه مهمی که میانجی برای آیت‌الله خامنه ای فرستاد
👇
khabarfoori.com/fa/tiny/news-3220753
🔹
جنجالی‌ترین پرونده تیم ملی فوتبال قبل از جام جهانی؛ فهرست محرمانه ویزا نگرفته‌های آمریکا لو رفت
👇
khabarfoori.com/fa/tiny/news-3220848
🔹
پشت‌ پرده اولتیماتوم جدید ترامپ درباره پایان مذاکرات | پس از ۶۰ روز جنگ می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3220986
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/656703" target="_blank">📅 23:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656702">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhdJ-r-LUwhbXAiCtFEFnW7y6OSREGibLcVPyF9TUdx2O0_izFbqBV5DAS1s4yJ9z8VTTp3Dc7UhuwIG0qQgVMNaD-8vSmeDLQ3eiBJYNXhhkcllEw0-WEoMzAHJusowUhhON5jBi0NhpYz6tUsxs8YA_n3ghIowSytZ3TArYCApL0PV0KVAi_SG4Jc9-y4-O0FyW9PwdbCS-NIz8FhbvnkHt5ttx1S3EszmREsqxsBU8vdcUAfv1t94X0vEkVER5BToi8tTte04C1-0gOEgAXKwz86cw9Mpq_e1mT7JpLH-9Fq69c-6RYp03ZmKeRBbG7e9Sylw4ZRF1M-f0lev9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فقط ۱۶ درصد آمریکایی‌ها فکر می‌کنند در جنگ با ایران پیروز شده‌اند
الجزیره:
🔹
۱۰۰ روز پس از جنگ علیه ایران، ترامپ در جلب حمایت آمریکا شکست خورد. یک نظرسنجی دانشگاه مریلند در مورد مسائل بحرانی روز پنجشنبه نشان داد که تنها ۱۶ درصد از رأی‌دهندگان آمریکایی فکر می‌کنند که آمریکا در جنگ پیروز شده یا در حال پیروزی است. عدم محبوبیت این جنگ ممکن است به جمهوری‌خواهان در انتخابات آسیب برساند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/656702" target="_blank">📅 23:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656701">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">💎
دارایی واقعی فیروزه چیست؟‌
🔹
خرید نماد
#وفیروزه
:  چهارشنبه، ۲۰ خرداد ماه
رامین ربیعی، مدیرعامل گروه مالی فیروزه (سهامی عام)، در آیین معارفه‌ی عرضه‌ی اولیه‌ی سهام این گروه، خطاب به سهامداران و سرمایه‌گذاران گفت: «دارایی واقعی فیروزه، تیمی ۵۰۰ نفره است؛ تیمی که هم از نظر حرفه‌ای، هم از نظر اخلاقی و هم از نظر تلاش و دانش، در سطح بالایی قرار دارد.
ما کارخانه نیستیم. برای رشد، به ماشین‌آلات نیاز نداریم؛ به انسان‌های درجه‌یک نیاز داریم تا فیروزه و ایران عزیز را بسازند.
شما با سهامدار شدن، در دانش و توان این افراد شریک می‌شوید.»
🎁
خرید نماد
#وفیروزه
با
آمادگی ۱۵۰٪ در کارگزاری فیروزه
💎
گروه مالی فیروزه
سرمایه‌گذاری، برای همه مردم ایران
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/656701" target="_blank">📅 23:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656700">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961752bfc3.mp4?token=fWymlzcHwRg-is46LirlrHJVupdXOfMZH5D63d4I2UdUbttwC-EJVVHgU-OsjUXjt_ceDETge1b2gCHbVQjYa0k5lozGYG9HosBAnV62Ybp3nIFBPWPN2Aejq0tiINPrVt3G7YAokIoSB7KxXn-rthtvlV9ORQE0LNg587g82xs88RjChSFysdZV8yIt-FkvQdehDRA3MoaBfdKJZx1KQbDZ9QX0VkZc2wiLr84hzhrRKCTqo52IWYpVPUio9Dwu0DHwMUiBnvweb-2IB3Up5KVfydWyl-6IPGlBhUmiTicnF9GzRhG05NYTnZQUrIOuoTeTgEkH1AY4c7n0cB660w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961752bfc3.mp4?token=fWymlzcHwRg-is46LirlrHJVupdXOfMZH5D63d4I2UdUbttwC-EJVVHgU-OsjUXjt_ceDETge1b2gCHbVQjYa0k5lozGYG9HosBAnV62Ybp3nIFBPWPN2Aejq0tiINPrVt3G7YAokIoSB7KxXn-rthtvlV9ORQE0LNg587g82xs88RjChSFysdZV8yIt-FkvQdehDRA3MoaBfdKJZx1KQbDZ9QX0VkZc2wiLr84hzhrRKCTqo52IWYpVPUio9Dwu0DHwMUiBnvweb-2IB3Up5KVfydWyl-6IPGlBhUmiTicnF9GzRhG05NYTnZQUrIOuoTeTgEkH1AY4c7n0cB660w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش شدید امشب شهر سیرکان جنوب سراوان
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/656700" target="_blank">📅 23:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656699">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_q8YLYI-aj2WKvzxhsnb02KBbULs-6qFvdKfMir0yhyki1NIM5T25EpLzZb6ocrHEDpPWMOANllQgMogDRtn-9I-IHJNRx9w605YlO61csE2LzS8DmR5_0VdwRfvv33n76EMA46W9tics0y55qZOxhmY3I9lPP36fvSols6RpCIRgk7_M0bIYdWhHvoL3nVKEry9ZSXOvwnibGwUYDYAzJWfduTwYzbymh16gCncMrXedvxs7eFrQhlQ9uwTQ2SWRChvXA5cNxmTIYydTEv31k9EZKil34gSdmNHNzAVXghpV_iTkNCJjdC7wy-0jWha51S1BREbcKnrvGienOfJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آزادی قسمت همه
🔹
با رونمایی از نخستین پلاک اختصاصی خودرو در منطقه آزاد سرخس، گامی مهم برای شکستن انحصار خودرو برداشته شد. بر اساس طرح جدید، امکان استفاده از خودروهای خارجی در این منطقه با عوارض صفر فراهم شده و تردد آنها در استان با مجوز شورای تامین امکانپذیر است. در شرایطی که بازار خودرو در دست دو تولیدکننده محدود است، اجرای چنین سازوکاری در مناطق آزاد میتواند به رقابتی شدن قیمت‌ها، کاهش انحصار و بهبود شرایط برای مردم منجر شود.
🔹
هفتصدوشصت‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/656699" target="_blank">📅 23:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656698">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIWV45YlPxeo-dsXozc-tZMxW7JP8oKKLrdhgLQnMY31jZlwBHOmo7YJdDLgJAe4Y1_kvZbmkb7JD0rBhX3GnQI6-_fNjoSnXZbgUp2nq2KOmeM2M-uNFrkKU9H6041qm2upk2bV4Iwm4KSYurlMGiZOix6dEDGqeFKCIdaIltkh6qCgqR9nW2qW5av8z7deUwrbsgiLkJlZeOmbWGGlN8wMEgoIQ9S4utiJ0No57nHMX-GaliO0RUsA9tCkfTlB6P0BvIIJLeLVXPOG67RSwyAH5AoewU2VGIc1X5j7lNjRsyejT8nxkEHiHW6mxgie1zfIQqICHNhcAoU4R86cyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عاقبت بسته ماندن تنگه هرمز؛ شاید غذا هم گران شود!
🔹
هرگونه تنش یا اختلال در تنگه هرمز می‌تواند قیمت نفت را جهش دهد و در ادامه، از مسیر افزایش هزینه تولید، حمل‌ونقل و کودهای شیمیایی، فشار را به بازار جهانی غذا منتقل کند.
🔹
بررسی روندهای جهانی نشان می‌دهد هرگاه بازار نفت دچار شوک شود، با یک فاصله زمانی کوتاه، شاخص قیمت جهانی مواد غذایی نیز صعودی می‌شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/656698" target="_blank">📅 23:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
فرمانده صهیونیست: جنوب لبنان باید اشغال شود
🔹
فرمانده جبهه شمالی ارتش رژیم صهیونیستی خط بطلانی بر مذاکرات لبنان و رژیم صهیونیستی کشید و خواستار اشغال جنوب این کشور شد.
‌
🔹
او گفته که خلع سلاح حزب‌الله بدون کنترل و اشغال جنوب لبنان امکان‌پذیر نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/656697" target="_blank">📅 23:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656696">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDl4u4jGul-yoEYHXv-CBWdJN4Nc3CZ0glg3-MakD7huiYT1DcubW6jeFvRtr3FXxLZlL2iMvm1ZKwRHzBe9pYwmh3oA3ZRUyVWBqUIfPigpEJ_EnfbBc4rVY3-DdNZY7htE7zVWQNezXntNsr63NSdMLWKdATg_cnpzLUkDCcmBkeJzl3AO_cQz2KO0H9uGHNIfPSTKL6PfmRigIdblLydnjAEFoWTqLSS70JTVDZAtuqVoBHvrIip_sN4YHGjxd2NVV5M1rmRlVXvwftKllrKO5LNuapUvtEnbHmrAVs8UgIMquk9GpoaI3aAQUiScIn7FQ4SKpI-dsUNANP_fuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیکزاد: بیش از پیش آماده جنگ هستیم/ دست بر ماشه به هر اقدامی که لازم باشد، پاسخ می‌دهیم
علی نیکزاد، نایب رئیس مجلس در
#گفتگو
با خبرفوری:
🔹
آمادگی کشور برای پاسخ به هر اقدامی در بالاترین سطح قرار دارد؛ ما دست بر ماشه آماده پاسخ هستیم و این یک ادعای صرف نیست. استراتژی ما با رویکرد آفندی و پدافندی تدوین شده تا دشمن از صبر ما سوءبرداشت نکند.
🔹
درباره احتمال حمله پیش‌دستانه نیز باید گفت زمان و نحوه واکنش، تنها در ساعت صفر و ثانیه طلایی تعیین می‌شود و هرگونه پیش‌بینی پیش از آن خطاست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/656696" target="_blank">📅 23:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656695">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
لاریجانی، کارشناس ارشد مسائل سیاسی: مردم خیالشان جمع باشد که ایران برنامه هسته‌ای خودش را به هیچ وجه از دست نمی‌دهد
🔹
برای گرفتن پول خودمان از آمریکا التماس نخواهیم کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/656695" target="_blank">📅 22:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
لاریجانی، کارشناس ارشد مسائل سیاسی: مردم خیالشان جمع باشد که ایران برنامه هسته‌ای خودش را به هیچ وجه از دست نمی‌دهد
🔹
برای گرفتن پول خودمان از آمریکا التماس نخواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/656694" target="_blank">📅 22:57 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
