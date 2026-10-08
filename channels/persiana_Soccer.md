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
<img src="https://cdn4.telesco.pe/file/bC8nGo8IFHZlc0sW81leGcvMS5Uvexffysfy767EXYUttGequJWde1AnYyJ4EFza-qJg4jn_YCXxZpBweT7ow3qkGDa73zsDb4gakyBNnJITcYnse0-XBk_1mPBHP-aBn-f4AvAoNYqH9G0DuPIULpmVKDh81uFmmOghuehFYdDFayqPbBhBB7H93570uKy0CVu5wNxOFiIMkvC0D9EsCDVEj42eOM-ciPx7J6VD9T25lJIAj8o2zJtaYg1TUdonVqU01b1-lMUrJKnpiQ8CMLi3rUterJEgHx04B7IEsA4i9rHjQVfamwiWXc44uwhCYw6qeo_HjgRdzHsp8M2d7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 499K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 12:43:35</div>
<hr>

<div class="tg-post" id="msg-31173">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb012b6f1.mp4?token=P42zWGQYp_6tuVqAJI32N0uhwLR8TlL77gXdZQElCxWM2thD5r-SxYmKpG1pqfu97dZa5rd6nnJlUaYfDTHKXHccy9fyuoMOb7JWYIHAFxHmlPe5ZHCz5P0ySWhVoNjhzntVUL3eprb97j0Loynl961ZJL5uxAQhgrdkdP4vtcfqY92gRpU-a8hsox5Bf9IhqKH5gjwReWnKtT2EQf3aE7XLjFIG_m5gDkc2OtQSvdtpQciPNRV0iEaTgAUJ1zJXCY_DwD_KnLjYFFG4KrwPbmIbStXJSa47yjncUcDnQ3ZRP0JWIurev6qe9URaYumRuaHtVQJRKZ7AkRJvbOmEM1vNZebwFYYr05qcyM3TETUN41kom5r17QxeIc4NwQPN8cCAlFOEkoTghGrJGIwbERfZqH8diJ6X1RVpADDQIGpoOfvhsra2LUhGCauEhevepsxiqYSCKt4eJ216W6qwgzQPt8NwVl5Fo6LVREzOHMA7PgneATXaQkvUULOGaArdARRrRyswOPz7dPiM1dSb2zuoTlfOPXVGz1geI0fa4Qm6TtFzJ_P23hlyP6e44GyxYJkaQhuEU76Wd7-Y-FyXcoJ97dUVnq8VhEkS94I5805Y5ZBVLsLYw9chzSVbUepoERtNWXAAVc_rtH7zqHrtbPZldp4uPVzdekmrdnWVkB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb012b6f1.mp4?token=P42zWGQYp_6tuVqAJI32N0uhwLR8TlL77gXdZQElCxWM2thD5r-SxYmKpG1pqfu97dZa5rd6nnJlUaYfDTHKXHccy9fyuoMOb7JWYIHAFxHmlPe5ZHCz5P0ySWhVoNjhzntVUL3eprb97j0Loynl961ZJL5uxAQhgrdkdP4vtcfqY92gRpU-a8hsox5Bf9IhqKH5gjwReWnKtT2EQf3aE7XLjFIG_m5gDkc2OtQSvdtpQciPNRV0iEaTgAUJ1zJXCY_DwD_KnLjYFFG4KrwPbmIbStXJSa47yjncUcDnQ3ZRP0JWIurev6qe9URaYumRuaHtVQJRKZ7AkRJvbOmEM1vNZebwFYYr05qcyM3TETUN41kom5r17QxeIc4NwQPN8cCAlFOEkoTghGrJGIwbERfZqH8diJ6X1RVpADDQIGpoOfvhsra2LUhGCauEhevepsxiqYSCKt4eJ216W6qwgzQPt8NwVl5Fo6LVREzOHMA7PgneATXaQkvUULOGaArdARRrRyswOPz7dPiM1dSb2zuoTlfOPXVGz1geI0fa4Qm6TtFzJ_P23hlyP6e44GyxYJkaQhuEU76Wd7-Y-FyXcoJ97dUVnq8VhEkS94I5805Y5ZBVLsLYw9chzSVbUepoERtNWXAAVc_rtH7zqHrtbPZldp4uPVzdekmrdnWVkB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:  «من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود.…</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/persiana_Soccer/31173" target="_blank">📅 12:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31172">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3-rj7n5EcyxinDKpbAWUkLoe-s3B_yUxtrgs356D-ZSmRgMHspqQHvorpAerKX2tMt4keNeRCVs0W1dZPm9sldbVWRfS-ow-42U_oDvuNGWilq4bikYA9O0ZAwoZHDvUuF27zCyY7A4uy3qgAlrUgg7Myrym40fWvMS4D909W4jR6jJtJoYmn0Bw5DudL2idNIU3EyOu14egJ8IXzGXBinZNlT_4fWRNlj_impzRNsdMqaufXu2lEDsZvXSBrjZrjl1vtF06bUTWeznDsUHHI_QeudReTxG1u4YjfKlGDxEpB5kRa48ysakzWaoqiMfu-SsX7iPRv884CusmJGPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:  «من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود.…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/31172" target="_blank">📅 12:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31171">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKcmIrZAdUydv2DtKtcK53DJSV-w-uhT_bbSoIa8mq7yvIEyDPMgRgoiWHbssh9ZrRV8EwmcL322QxhJGPJlB-JGuDFR2SHzvoypKnKeSFyC5UNJjGFXhEESg3kgGR0J54NXBwLvnyPNkQkefaYhP0AzsbQvKLc4FYCmHJzbPMhrmozE3Rsvo8FHMScD4BzCiPwNm8WaNT0iQmePME78DS8MX3W8S_iH-mwPD84mKLjm288Q-Ek6Vtqp_Zv-jzyx_qONF7Anct9Q0P6osAjox1OO6PAaKjDp-ay8ThGulh3VZvVRnia4e1HmzX6sHFvZq7Pnn-5JMRG8-qyLRe7aFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:
«من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود. اما می‌دانم که به‌هر شکلی در مراسم افتتاح حضور خواهم داشت؛ چه جسمم آنجا باشد، چه روحم بعد از مرگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/31171" target="_blank">📅 11:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31170">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nE2ciBELWaFqHyq-nP4H2F8LaCkw-7UqoJJMJvvdSeCpLWVr--Z3erF5k0YAI-YObRx1j6UV-80fRCPmzB8BKYL3rqU2dPBnCStWaLm-o_s_F4tbR0chdJy6ADhIEqBNsCw6fC9j1AVxj9i9tgM1GXNgQll3jSmrBCKI3oC_sf6i7nm8zBVegYAuVbe7eP33SRjC4sX4xunk96E4dTuZxwHUVs2TF1cotNXmFVfkDepOCCLIBdkJbNQtJCylyWVSQneZxIe4PYxW9Us4mPDAfU6qE1AXMJGkUUZJfp-sz1S1oTQR_aKoncD3g4b5Nh5xhgREMb-QDvAzbtmYt4YRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/31170" target="_blank">📅 10:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31169">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEZTvkUISxqPolfqSvzQsm4EheiPHn-2DNQjdzVYUFYoM0RVcS9-DyYj8vvcdbLUMKV7JaPwEdBuf5C8TxCkaesD14snHfFr-Elo4iAqjvPTc0uv5p7d5C3zErTfduRfdLw4wyCNVrAqKMGJSc7suCHPzdWCYO_VuzBxB7cCKEvAXdgfoff5avhsZSkI8gCuNT7TiKpQTq_oSH-YbsI5gEJFS8UzVnggzyx6t4ocy8VckSwKoqVWNfFQZQ7ySOoFl0qqZcgkiM_MwchbzOg98CqW5jR5vEHt2beo6yQOOIhADZLttBP0qDRsmvIDGwrJhsNmbZIHOe3DCsyklKT_6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل تراکتور در هفته هشتم لیگ: حبیب فرعباسی، صالح حردانی، سامان‌فلاح،عارف آقاسی، رستم آشورماتف، حسین گودرزی، امیرمحمد رزاقی نیا، روزبه چشمی، اسماعیل قلی‌زاده، یاسر آسانی، سعید سحرخیزان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/31169" target="_blank">📅 10:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe9b0bc7f.mp4?token=Kh-_vB-396W16kFCimkZKfkcpUceDsH1UBD57cO0fClpDM0zjXvob8Mg7QT7g0KiwdKz-VgLxGSZwsOzdYpagxTeqcRimYr5R-UztlKGICQwHFPtKsxKZcD-r0DR-mE_v80BnT6430ap_XEcZiEyoN7P4q0IIHyyrOBSEPJ1ddkNRNbmIJP1ZqsYJrukE-na6mf9gQF73TN9hwxCTugYRx1XQNTo8HZJ0Qmr0sYHvN1yDOkSI7noUr25rWVPPhvTu3VAkSO4i64gggK6JEz19bLgFXVSTLiVntJLv1xbqJOKaSk6MhxvYdvf1M8Gkcw3sMppKe1OCgj7wpdm6-5GXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe9b0bc7f.mp4?token=Kh-_vB-396W16kFCimkZKfkcpUceDsH1UBD57cO0fClpDM0zjXvob8Mg7QT7g0KiwdKz-VgLxGSZwsOzdYpagxTeqcRimYr5R-UztlKGICQwHFPtKsxKZcD-r0DR-mE_v80BnT6430ap_XEcZiEyoN7P4q0IIHyyrOBSEPJ1ddkNRNbmIJP1ZqsYJrukE-na6mf9gQF73TN9hwxCTugYRx1XQNTo8HZJ0Qmr0sYHvN1yDOkSI7noUr25rWVPPhvTu3VAkSO4i64gggK6JEz19bLgFXVSTLiVntJLv1xbqJOKaSk6MhxvYdvf1M8Gkcw3sMppKe1OCgj7wpdm6-5GXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استایل‌جان‌سینا و همسرایرانی‌اش دراکران «مچ‌ باکس»؛ جان‌سینا و همسرش شهرزاد شریعت‌ زاده در اکران فیلم«مچ‌باکس»محصول اپل تی‌وی درکنار هم ظاهر شدند و توجه رسانه‌ها را به خود جلب کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/31168" target="_blank">📅 09:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31167">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9398a1a1.mp4?token=ngtAtCXc3ylGHAu-fSkcEmvsVeQeaLCdh72umV9SbUoAF9Wf9Ge6uyA7TME0e09b2TzgFFfM1avIzEN-zDPf6msBX1e3NpKlara1TP72j-kzhg7Oz__kh8SJWePQRyM1b0tbI2MdGuihTTGnanYQXxdsMIRf9cKtIfyU92rrgMB5lIkdiftfD10P3hC4hL79ifL8FcBaRroJOuaLJwBYd856K5me4Gcm9bAlmKxjSKzyVuBLU-lN6XK38R4E7QfB8_eahxe81RE13DEr5Mja9RyVKMr6dPSeLJMg0LWC0bFxs6TWiNZ6C5fK9-kxYD-ChaOnJL5y3zVJ7pZymE3BPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9398a1a1.mp4?token=ngtAtCXc3ylGHAu-fSkcEmvsVeQeaLCdh72umV9SbUoAF9Wf9Ge6uyA7TME0e09b2TzgFFfM1avIzEN-zDPf6msBX1e3NpKlara1TP72j-kzhg7Oz__kh8SJWePQRyM1b0tbI2MdGuihTTGnanYQXxdsMIRf9cKtIfyU92rrgMB5lIkdiftfD10P3hC4hL79ifL8FcBaRroJOuaLJwBYd856K5me4Gcm9bAlmKxjSKzyVuBLU-lN6XK38R4E7QfB8_eahxe81RE13DEr5Mja9RyVKMr6dPSeLJMg0LWC0bFxs6TWiNZ6C5fK9-kxYD-ChaOnJL5y3zVJ7pZymE3BPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/31167" target="_blank">📅 09:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=XtFd3Edv3rDH3EorAoLZZXbOBSIVk5VCEICj9-NEVcu12-LbfT8Mim-ej01UvGQPeURY1tmQQVRKEkaEFO8SqDfOdIOez7MdUFTe1GW7auOorMl8oQk78JooGPeOUjUgWNF43FgrV3UtYfPIdQ4GlWemgNhCvn1c4l-tKWt-eunINheTfuMCgrLJKpurMNkVmQC3tI5XFhxAuHedRRm15RAPy1dZx7kA2dz5iRmpLIVgh9hEhHWthD3u_hQ_38E5ozCmTs1lk4YOyiK0mW3uYlXIYiOwYD4yxc8kJKVC9IXja7PAeYPgR_W5SOAujN0BYubYTuPqRFDoWV_OR8Xiig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=XtFd3Edv3rDH3EorAoLZZXbOBSIVk5VCEICj9-NEVcu12-LbfT8Mim-ej01UvGQPeURY1tmQQVRKEkaEFO8SqDfOdIOez7MdUFTe1GW7auOorMl8oQk78JooGPeOUjUgWNF43FgrV3UtYfPIdQ4GlWemgNhCvn1c4l-tKWt-eunINheTfuMCgrLJKpurMNkVmQC3tI5XFhxAuHedRRm15RAPy1dZx7kA2dz5iRmpLIVgh9hEhHWthD3u_hQ_38E5ozCmTs1lk4YOyiK0mW3uYlXIYiOwYD4yxc8kJKVC9IXja7PAeYPgR_W5SOAujN0BYubYTuPqRFDoWV_OR8Xiig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های امیرمهدی‌ژوله‌درخصوص وضعیت اقتصادی سخت‌واسفناک‌مردم‌ایران در شرایط فعلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/31166" target="_blank">📅 00:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31163">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8K6lBDkSOK1jWc24lWFirJeRHOyPBcYktFWcTETESa9_bphMxMhUZRHBKC-cBFKehpENMpeuBPJdctXjeufsQnTHEgTe9VKUc3VUxNwyeYYPPiS0PalEGs1zCfMC3x21MULEc0d6epOyLdz-DXDpyPXiBjfEOPf6R07JAYRFCM0oB5NTF3Jisf0NkcsPICI1Y-SXcwDBfcIjKfi-ZySOBKTBoyOknCtC0LQLUpzeY4pW_hk8UUtDRSiCDtDBT7iVDzJUT73cYM7xSGDEiTKcki9mLrtsW9q6zz9AjtFDC84syx8sYrZR-J1UKKNjEZ1Dqr59s3Sa9eMzN7Bt0nBxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ بازگشت فوتبال باشگاهی با تقابل حساس استقلال vs تراکتور در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/31163" target="_blank">📅 00:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31162">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUxtNolLQXhXkeGdwuMbchC0xMyEXE-_3xEdGAsjDT5BfHA9RdaZvbbl2wjLqG2yQh45p3ppzKMziKQLfcd5sSfdslpA6CC6ImWgjfDdcqsEC59pXK99slsqxQz-lYPzHvSAP0hBKTobiaTY3Dvj-ZJeidkPTHXNwGf3kH3XeJ_HeDXjwtztpck369MMo8BOoFeG6J02czPzFgez5n6Mv33JAMuVYP38XBqk6srkR90erMMeh4-B0Us1qmYe0Fe96AKxNoIcwmz7vCKhbUAqVMDQ9zGpgE85eKFnQn46HBufByPIKahf3ZqsniIHhLyMdQCgKV0D7i0EfqpVYYeN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ لست دنس مسی با پیراهن تیم آرژانتین با تاثیر روی هر 3 گل در جدال با بنین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/31162" target="_blank">📅 00:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31161">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpoQp6k0w0owUIHswEZ4ImtjbAIwyGi15za_RIJF-MFVKVff8e_b6jbzEU43rrc08YgANPJ-I1BLYsMnfAqySCS58qp_q9qbQtdzPwfGYkxHWSZpX-3oKnvj_LSUl8_CgDi2B_UxdEqM0NevUtwgyxDebXSsM0CFVFiBxcIvUkuwLxdF4kVvrSxWRhjbgu_1gYTVl5YvNtPa5FvlPh0xqbTl5xzjdb_jfVwCwgxhE_R2icSST3qISiNcA4swHRZueiMeQSRirszv9UyE0iuakQo_ZIkmDPw1cPMin2CCCAgNhJAuDWqnkl-UgNBSlhC8ZpSXpaeMd7BV-zzt-r_Mew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/31161" target="_blank">📅 23:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31160">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbs4H_RbZBDUNGYE8VbvNZ0Myf6sxjkWgvI3J8asxbaxeVWRGi5mlTBstBjeVoYfRYqVgst2j8gGH9sTGe13h-C9EOJkBSD0D5rBBX9GnxNwDAxGT3H-QUUbvBY5Gz7lsmW4zOHY_VZtLx4jbFw50X-TYVKUDbODss78toU2JIQ41G3L9MR66ms7X90qf7_cnukr-RA7eX0OhuhTql2SfKJugC0JS-FBZFYuLbAMGQuIIEMURBnt7yt6hG6nABhQzgcfX7HM6JCEKWcs2XLF_-rSUWFjhHG-PvpK4o8jWA-vR-jNCwa0S4hn9lv53vP15C08CgOwOnI-z7HP1F7YVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه استقلال به جمع مشتریان مبین دهقان هافبک‌دفاعی 21 ساله تیم الوحده اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/31160" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31159">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=P8a_wQ2wy0KGsIPxai4HowQ3KLKILtOsdNkNsx-x3ZaAEBKyKUsLO7kn5a8lQSBu3XEO1LsyQo0q6LVmHCJnHfBnihaArHkdaetx9KwZ1ccel5VlFznLDuE1ZxCRYY4HfFG6qIC169icZU9dobcJVXG6omJvLjVD2vo1E0_6EpeF63SnPNsnR1LOsKMJCreVqwOl9Ta-i2aOlcx5FXe48uuvD7eQEwgz3T_Msl5AV6IgsW9lnwNPkqwoJVAWhxC5Zt8KJvOvA8goIIz9FqcMneG8rJbeLCAFHHdxbfktJ2zMCuJ39Lft4KCgFFwaQW5rVl1p9O0iIT43wtw6tu6vAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=P8a_wQ2wy0KGsIPxai4HowQ3KLKILtOsdNkNsx-x3ZaAEBKyKUsLO7kn5a8lQSBu3XEO1LsyQo0q6LVmHCJnHfBnihaArHkdaetx9KwZ1ccel5VlFznLDuE1ZxCRYY4HfFG6qIC169icZU9dobcJVXG6omJvLjVD2vo1E0_6EpeF63SnPNsnR1LOsKMJCreVqwOl9Ta-i2aOlcx5FXe48uuvD7eQEwgz3T_Msl5AV6IgsW9lnwNPkqwoJVAWhxC5Zt8KJvOvA8goIIz9FqcMneG8rJbeLCAFHHdxbfktJ2zMCuJ39Lft4KCgFFwaQW5rVl1p9O0iIT43wtw6tu6vAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو زیرپست‌لیونل مسی: لئو، سال‌های زیادی برای کشورت جنگیدی و یه میراثی به جا گذاشتی که برای همیشههه موندگار می‌مونه. بابت تمام کارهایی که باتیم‌ملی‌آرژانتین انجام دادی نهایت احترام رو برات قائلم. یه بغل گرم رفیق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/31159" target="_blank">📅 22:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31158">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fB-mBCYEM2kpeFfaosmDDpRETgVlJYuZG-H0rF2DWzKaSJBrPyHssxdb7l9orwBrjhhruQ0kLduqun9SI9zuCxvsHKsxxAf30aMhPSe-7f3nk5CN6JQ9bK1x8yxvI5HnRpI1S8i2DWVsYzucbAQk2OxNjltRQ513pCpRAZRBYM3fCX0N9VYR--xAgHtG16bbS6b5ov2DOmQJZAO2FzoFcz32HYYcAoofu0hKasd01YNLsZA-qEEGPaXYGjUG-kLjCumN1kKbHtqw11HoF-QH2S7keJRVhqz01366jdMt0jOm0JFcfnXFhFLq3m5vKMzFmuBQiZx4GBkpDjO3A55ilw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان
؛ اسپانیا، آرژانتین و فرانسه سه تیم برتر رنکینگ باقی ماندند. پرتغال با ۲ پله صعود از برزیل عبور کرده و به رنک پنج رسید. ژاپن کماکان بهترین تیم‌آسیایی با رنک ۱۷ جهان است. تیم ملی ایران با یک‌پله نزول به رنک ۲۳ ام جهان سقوط کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/31158" target="_blank">📅 22:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31157">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ml9a7mK2bdtFSWvHjsdGP5ULkUOprXpc9bqCKS6T9i-zu3ZLApTjze7cn_KqNzilwb_6w9oTBv2bLSMugDgFb75OrjkAHr0OFN-DMtPWAIGRI7mCdAqA-0blzqu7N3mF_GyXEsje6Okjb7fsNZlV2gIOZbL-nDcT8hhwRM3qIM8w6BTMXSHwM755-O2CRq-P_7IZCyAbPAAG9v0IA5C4lKAENbHIG0HMO8vNQKjvbELSI4dnorBss8GHVzvUMDlfXJUYIltl1vXVh9Q_SDhmpER5mCFliW_UqIwTInIh5bQEjJSQBDeys9YVYixrV0QIpNPPbbJeUx9VYakM_pDL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان: لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/31157" target="_blank">📅 21:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31156">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lELgbs21LN3kBv1r2AR7oGmEqkczu0H7uQSphTGpiTltKbPAafXcrpLy7I6SztjzHpO_cnX9Pdk3BzF5Ajo6hOqoajbiyJsZaFFs-iVuaswfG2UQLv47A7wECEQrzJH3brE_XOudnofTwAcc1aOCHXB3k-sl10zs3T-h6KJfbhIJ95CW0kVqnnRpSK5IBTF3IlggUW2f3YWEYLmOFc43QEJ007H3QBl5XZLne7dVGEXq9zG_18eDmwIiaV1F4Z6pXP9q57PfzXR_utgPfKpZbbpjMhh-iL7olFNR8tObRd1yIsZCb5s9DddgM6Dj8r26qozPwxeSa7Xom_Y1UrbzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/31156" target="_blank">📅 21:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31155">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LydKul1Lysa2dI3CPaQVwSm__QSaMCmvynYj1avUPoZQgvoa95o3ctzblqaPNIY42UTNiOH9dun5GgQjfvQENMa_3fsE5E-jjeMEI0dxbEL5ilj0U6PQox04yIaNHTDCGz5W1bYzpGRmsPCo7GXmXLDIS32VWew-X9LTn9XNxp2KsUjMVr4FfZcs6ddrdve4zy1Vp7glkMwtEuAv4pw9KkNRszTUfK8yURlnYUvwjL_Js2q53nEKIfZVa66JwO7vGpnaedmJ1LG8gHgmoOLWvNk46E6qs47Q2mAxjdnsSfeg-WwKibJXb_yX7nfLmyZd5OT4HHPsE2uTrTZYkX0svA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان:
لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31155" target="_blank">📅 21:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31154">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
هوادار تیم‌ملی جمهوری دومینیکن در پایان بازی دیشب‌این‌تیم از ماریانو دیاز خواست‌که بوسش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31154" target="_blank">📅 20:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31153">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPlWzZWKpB96_hbeFNbCI94C8G2Vq13CnwVERBlMKS72ioYCIgpLGmuYT-muhJNgk7HAMq9pcXeoZJD6iCQksYJswjYRUmtMTBSTVkmzw-QPvI6JhmjxedoUbBjA170FEX5OZzs2HEEIDKYP4u4IfDYTn_2pBX2NP_ISBtK2EFCGCOAxIyw9oF1CLJm2eFDN1N7hbHN07ZPraM26EX0vaZkTqv5FpWixCms7-PCJY85J1D1l-MZPNn1u18spvzABtFAF1N6zl9soc2l2_pPNYJknfMEu3tniStObHEcygMfKo0kv4LguRCkw0ezbT7rPIa6_3uDoEeizIxcG-mI4Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ادعای‌رسانه‌ها
؛ علی دایی و همسرش دیروز برای‌حضورتوهمایش‌یه‌مجموعه خصوصی رفته بودن قم؛ امروز دادستان قم به خاطر حضور بدون حجاب همسر دایی دستور پلمب تالار رو صادر کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31153" target="_blank">📅 20:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31152">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=gNeftPnxFtCtW3VsJnghVIZjoN04m9Mgz40DvAYG4YBc7WgYcStgJTlRmdjKnmFlsRgNxx503YwkkiB2aHGxRFw-vuO1Bt-tcFc43orH8tzlDTe61973pIYyPZpQguK3wmyp8DSfdSyESEFzS498YR2HlKtL6bMPoFUmKtFpdfBx7wCUEc29mTkzBi6jYEbQrt3r1_WTGJwuO_KkoTlm7PzdfZfqBSulHvVUV3stmUoPScXMf5hTA1lRzKPwAHs24SpFxCLPokkVfz9PusnWpSNs2N-VwgRrAO_-3ZF7aPnHZd7Wlrpba0HSNAprt87NYREi_NNsxctnr0HELcbP0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=gNeftPnxFtCtW3VsJnghVIZjoN04m9Mgz40DvAYG4YBc7WgYcStgJTlRmdjKnmFlsRgNxx503YwkkiB2aHGxRFw-vuO1Bt-tcFc43orH8tzlDTe61973pIYyPZpQguK3wmyp8DSfdSyESEFzS498YR2HlKtL6bMPoFUmKtFpdfBx7wCUEc29mTkzBi6jYEbQrt3r1_WTGJwuO_KkoTlm7PzdfZfqBSulHvVUV3stmUoPScXMf5hTA1lRzKPwAHs24SpFxCLPokkVfz9PusnWpSNs2N-VwgRrAO_-3ZF7aPnHZd7Wlrpba0HSNAprt87NYREi_NNsxctnr0HELcbP0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید شد؛ با اعلام حمید مطهری سرمربی فولاد؛ رامین رضاییان ستاره این‌تیم 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31152" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31151">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBISdLGaBq1-UQTOVGvsJblreau02yRfA54MCsWVHMTmPh1JyoOixe0ZO6TV4gkAu7moGIx6ZbUM_K8ZhiXJxKXYpH8AFSVbow8pXIUUJJLOAu84eoFs8W791s5JI7Kr6tuKUlxjwCxE41jNi8DE_q8grzb8eIHndioNGFfddQ9KW9uB09Bd0HDuVr7QyxPAmFgvg8GRy9ZxKPthKYQbvNQQrV9ZJZgVvC5UvtV8tLpXgLocqoq0tbl5Bc1XCM3HdfZpNeukULCwPh1rmgKQKaTadks2qnsRlfgxPt9OTJt-1oJZjsJ-QfrLpH9iuatRS3havYAIl8oIOEEEBXCHDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پدرو ستاره اسپانیایی سابق بارسلونا، چلسی، آ اس رم و لاتزیو در سن 39 سالگی از دنیای فوتبال خداحافظی کرد. پدرو تنها بازیکن تاریخه که تموم جام‌های معتبر مستطیل سبز رو برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31151" target="_blank">📅 19:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31150">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=e3Mh9ZoWbiUclu_QTpb1RIrLSijbQL0_71SC1ytrD2kAOtLB2cjrDIQePOJwimWcjG5r188yrSMM3Lgtduep_Fa8kTVqcjQaQevRF_LI8KPRdPXplfYTt_Uw3oV29cGAFaXzH1DhN7FFxLo9nzlYmuRczjnMdhn7gByWTZy3RXTYGJmdxInYVEqpPIVrk3QA4qRqkc71hE4Dh0XSDbZ0pWZfpP6h2-NjcOobvaHn2N-1mPRsUWH4N2XvisXIZ_nCpnAPueufSSLBe6Ef9zCWaS1IoGnNLbyoOigeUyubFZtbCr0C_q-yTSfC-RYU-nMu6Lq0GHvT41hVxvi0Zuqrvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=e3Mh9ZoWbiUclu_QTpb1RIrLSijbQL0_71SC1ytrD2kAOtLB2cjrDIQePOJwimWcjG5r188yrSMM3Lgtduep_Fa8kTVqcjQaQevRF_LI8KPRdPXplfYTt_Uw3oV29cGAFaXzH1DhN7FFxLo9nzlYmuRczjnMdhn7gByWTZy3RXTYGJmdxInYVEqpPIVrk3QA4qRqkc71hE4Dh0XSDbZ0pWZfpP6h2-NjcOobvaHn2N-1mPRsUWH4N2XvisXIZ_nCpnAPueufSSLBe6Ef9zCWaS1IoGnNLbyoOigeUyubFZtbCr0C_q-yTSfC-RYU-nMu6Lq0GHvT41hVxvi0Zuqrvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عصبانیت شدید نادر قاضی پور از سوال مجری صدا و سیما که گفت محمد رضا زنوزی مالک باشگاه تراکتور ثروتش رو از راه راند بازی در آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31150" target="_blank">📅 19:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31148">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ5VFYd03Fh1z9xYT0ND51vGq-mhxFqDsTclKrq5BQQMFjbnWG09wtbBIknMqQO2IutSDJfVUF8YyRkWY-Vjps2bsNlz6TKf3Q8QW9xxNtKENgPa3Rg5GUrhFJ-RaYWhKrvbg-pQk8G8Lk5p4hPkShyfNEASTwN8EDDU9TJu6DiS5x_gjr2dMOB5P3nu3plB0-hk2EEoYcO4rGyHCfeQdFQX3LKW9oZKfFWM-D2UtRQuISIk7-sLWUVn6P27rB1vnthRvM2TiF6YbW-46NQppqV8f4Uq1P8nF2ooU1rjWzmJN9FutD4vltMLYxOddQ49LdlLqVkVBzhIC-7XHHp7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رضاییان از بس گفت تو دوران حرفه‌‌ایم مصدوم نشده ام. این‌بار یجوری مصدوم‌شده که هم کشاله‌اش کش اومده هم از ناحیه خصوصی بدنش آسیب جدی دیده که ممکن تا اواسط آذر دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31148" target="_blank">📅 19:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31147">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6e0CMlq-7Bk0XlfJdjdBoyGf5i3Lr93DZUB_UQa3eLTRiC_8WhBoMEvGo2dRT9ZpH3gCX8uF_lGiwWxAP_7KXddcXihzasbeJCPcdAC-A21x-4ub-zL0p-eJXGrJA_56xHelMCn_y_tM8H0jWCm6u7qFRVk6LhGIJjPmfck8v9J-7JhsucXv7gamboN_-vLOxDN1jMdI99Ap4s2J6Dl1eReE9791AOmdrNkyCFJqbaCDwx8S0qHAqnWtXdH4KUzO27wpVnYg1mj_bqoKJGQ5OOfosSh8W7bpZYrpj7vHZdGMekf2Asvvh-D0sfbVL9xgIZ_LQFH8kFfvnfQJR0OUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدِ 3 هفته‌کسالت‌اور و حوصله سربر فیفادی به پایان رسید و از فردا فوتبال باشگاهی شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31147" target="_blank">📅 18:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31146">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=s0L_lLL1QXvJ_C_Tv04njgoHEVgS1T6BfLA6rCtygXzx5SWQ7F545pD4ktEyT4kI5luWGZoGdn9DMTc-uVFoUzTWxPui9h6gSE8x4sH3luHmDAh3VR8EMWAWGc62N6nrNjJDHEsQAmOYCTY4VPsF4BWfKkOQXbMnwj3Rk5W6GAHFgE6cgKoithdp1q8J7_NJX16nuBnoWprx2jutKrpbr8COHOjruTZrj3ll-7FFt_Dp20fKKIQpKZNeKjQPrTeE2bnZrBJLwvXYy9zFCC6NE_6Uyw4zgUwaoSuUB584XLKHSPBEq6QYZt6Cd-xu-0p0eaxtASQxDpcUYV5pYdGD_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=s0L_lLL1QXvJ_C_Tv04njgoHEVgS1T6BfLA6rCtygXzx5SWQ7F545pD4ktEyT4kI5luWGZoGdn9DMTc-uVFoUzTWxPui9h6gSE8x4sH3luHmDAh3VR8EMWAWGc62N6nrNjJDHEsQAmOYCTY4VPsF4BWfKkOQXbMnwj3Rk5W6GAHFgE6cgKoithdp1q8J7_NJX16nuBnoWprx2jutKrpbr8COHOjruTZrj3ll-7FFt_Dp20fKKIQpKZNeKjQPrTeE2bnZrBJLwvXYy9zFCC6NE_6Uyw4zgUwaoSuUB584XLKHSPBEq6QYZt6Cd-xu-0p0eaxtASQxDpcUYV5pYdGD_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31146" target="_blank">📅 18:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31145">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuTBJw_BYnAnCQ_0YXB0Jd-cgM02QIaNGfb_j65IvzgTxWke0neYlci-JjJQCbOVztalh7eWFk5SltWzyctwEuP6Vt7SUkPigmAJ8kU70uYnUIiDgwXMA7YwgBhHhPAfim_1G69EuHJvZLkscxaXiF9hv2jrxXJJ_whw-m2P4IONAor9uVxjCyTk2qYl9KL81Jp6FClvXoxmn4_ySbV9lFf61NV8Ekmg7oaBHn94RicnIt0FpgwM-K459yOFHywJBR2CkGllb6cXpN7OOASFlXv-whayPgMmgRD5IOqEXwRFK46Gjy6r5g3f0a_zdSDV0Ca8W2sqI0XmqYqd6pQRCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇫🇷
نمره‌ فوق‌ العاده‌ و‌ خیره‌ کننده مایکل اولیسه ستاره 22ساله‌تیم‌ملی‌فرانسه و باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31145" target="_blank">📅 18:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31144">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=Sgu-YFZbbNG8WqGYlFC_f5UsNk2eCiZN3vowf1HhXufX8aBaRrvhaGY4h9PlFxcFkw84LfkkLg4WGbkqQfwZEmznbxPJqfM2dNlPefKEhhwpvRi1dn_lKCEQRJrY7Vlvj0c6bYRhz22zqYZ1_-FTTbiEZgJ5fXTb_Hlpv-RyRU_FBxz41qMBP5r6fIKLMPTLIQi_uIVphN20TaIj7BGxyKzoGCZtK0Y0VW_eYthx9sGoJfem7jCY3DOdF-mNwziD7tPMN_Cb8ytTVJ8W-O9uVBP3LEp6EN_MxlVn76pmOrBSveu5nqCYQvCWtWz1iFg1xr3o372ouuiJ-m1sxGu27g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=Sgu-YFZbbNG8WqGYlFC_f5UsNk2eCiZN3vowf1HhXufX8aBaRrvhaGY4h9PlFxcFkw84LfkkLg4WGbkqQfwZEmznbxPJqfM2dNlPefKEhhwpvRi1dn_lKCEQRJrY7Vlvj0c6bYRhz22zqYZ1_-FTTbiEZgJ5fXTb_Hlpv-RyRU_FBxz41qMBP5r6fIKLMPTLIQi_uIVphN20TaIj7BGxyKzoGCZtK0Y0VW_eYthx9sGoJfem7jCY3DOdF-mNwziD7tPMN_Cb8ytTVJ8W-O9uVBP3LEp6EN_MxlVn76pmOrBSveu5nqCYQvCWtWz1iFg1xr3o372ouuiJ-m1sxGu27g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
استایل جدید مجری ممنوع التصویر صداوسیما در عروسی؛ ایشون سال 1401 بعد از اون اتفاقات تلخ پاییز از سازمان‌صداوسیما قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31144" target="_blank">📅 17:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31143">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=FDNeXWlORUApSZ9WcDp74okYj3glYgrREcr_mX5m7YIJCfU5vOFpGYtITTmqi-izn6eOetSNeJ_WeECptPOWd3jsdBPxFtIOxquoBUb1XHet7pwMEMwFxTO40FFfzqSQ--LIkUuj2JtzCkEWks_2QVF04qzhe5FRIpJAIixbNs2B0_E3_Y32swWoPX7DkLK1s4pgNgpsrYQJaDj6Gbl5j_G7cBlVkHvNcnHKoWJcJmqvLVEIwpE99VB9kM2PwIjZ3xVGLlR85s7lnN1xvMxsfGO-U6-sv8mPVXZMC0JaF_gYVCFWYrDx7fiBMtUZe7fcxUs5TXFOnqptDFSSTSZZog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=FDNeXWlORUApSZ9WcDp74okYj3glYgrREcr_mX5m7YIJCfU5vOFpGYtITTmqi-izn6eOetSNeJ_WeECptPOWd3jsdBPxFtIOxquoBUb1XHet7pwMEMwFxTO40FFfzqSQ--LIkUuj2JtzCkEWks_2QVF04qzhe5FRIpJAIixbNs2B0_E3_Y32swWoPX7DkLK1s4pgNgpsrYQJaDj6Gbl5j_G7cBlVkHvNcnHKoWJcJmqvLVEIwpE99VB9kM2PwIjZ3xVGLlR85s7lnN1xvMxsfGO-U6-sv8mPVXZMC0JaF_gYVCFWYrDx7fiBMtUZe7fcxUs5TXFOnqptDFSSTSZZog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های جالب رسول مجیدی مجری شبکه ورزش درباره اسم یکی از پسرهای لیونل مسی که چیرو هست. چیرو به فارسی یعنی کوروش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31143" target="_blank">📅 17:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31142">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgXPRv8soUcSpuC3ytVPXgvBWE69-uKsLCGIk0uMHgd-8f-CHQrfecNGTlULw6Ubfi2hjvVy94emgJ1WSYlDjp8Q4bqRuj4i2aYXV3ZsGANDf7BzKa5u30mDy0_J4-AnHm5QlqG_eBH9Z0jaz6mBovadi2f_B5nQa1Rd4nhJWgAnhwBycP8vYFM_tnyzrKuKxcfgi8OoSXWmI475jY8AT-eeWcjY9XMxHOYB6NQIziZLlq6hw7nLRL2PPYjlKbMUjs1pgihrpAKf_8v7h-QWr915sW3iIweN013eT2ZaCitpcrHKM10GgXdcPQ7KwxvuU1ibdNL2a4bUBoUTXD7Kfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌عجیب‌دیفنساسنترال: کیلیان‌امباپه تصمیم خودش رو گرفت، اون آخر فصل از رئال جدا میشه و میره لیگ انگلیس؛ امباپه فصل بعد تو لیگ جزیره:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/31142" target="_blank">📅 16:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31141">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=DbpfCFCRwtBt1au64aW7NT4ZY0vpPxgIDE-02PNRKcRLh6TfXWguqUT0OLAvE8UchQgfYlDcO1GYNce1PsyJqQGmcBW9KjduSZ70-J6AVquL-_4tBQqB0IOKH2R0PSp2hZFQsCEXg5X8jZMx0PW7eYEtWaF_Kv_HciRKJ9xJpKihfZuGhT9FWvxWJJM4QJEgtvhsKlfwW2siQMDIaVPgjhNdextrSu2SJuFSGHbmihtsooUJcmisvfZJOsla5ttg_wqh6PdkP5UIBmfV5u9m6ljyXcL0C9tEiwOyUAnU8zIrHo75Uc7GITwyluR61B-iN6Yp9qFmOlArhvVTn9qf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=DbpfCFCRwtBt1au64aW7NT4ZY0vpPxgIDE-02PNRKcRLh6TfXWguqUT0OLAvE8UchQgfYlDcO1GYNce1PsyJqQGmcBW9KjduSZ70-J6AVquL-_4tBQqB0IOKH2R0PSp2hZFQsCEXg5X8jZMx0PW7eYEtWaF_Kv_HciRKJ9xJpKihfZuGhT9FWvxWJJM4QJEgtvhsKlfwW2siQMDIaVPgjhNdextrSu2SJuFSGHbmihtsooUJcmisvfZJOsla5ttg_wqh6PdkP5UIBmfV5u9m6ljyXcL0C9tEiwOyUAnU8zIrHo75Uc7GITwyluR61B-iN6Yp9qFmOlArhvVTn9qf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی شدید علی آقا دایی اسطوره مردم ایران از خدافظی لیونل مسی آرژانتینی از مسابقات ملی‌.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31141" target="_blank">📅 16:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31140">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQpUn1ppHxkj5aLqBB9p44jpzTMzjronOC1J95W6-PC9dR3G64BO_OelFm8sY6mAVU6c7UoFYz72Fzwj-vhh1jxNEGprZmd3RgBWo59fOz3pdp3kD1i6dusaS0lJx3HGQZcTJdBj-v62SVU6HW30WG9ZBQ_JiGH1e799gXUprg62BcDfN52jb5uJQD651v6QEAdMQ2Fw28q0u6aVOTcfI-segshJgjo26GYP-KHmeejm8NXgxyWzzMxYtmOFzEyA0Evr_f9M6440TAe1fTUi2Hu0_zeQl6nKq0f1YzBLBHNqFKRP8XQFI-m-odprMiRYADZIKCgy3P6UUkYXZuahWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه آرسنال دقایقی پیش با انتشار این ویدیو خبر از تمدید قرارداد میکل آرتتا تا سال 2030 داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/31140" target="_blank">📅 15:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31139">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EV4VIsRS_hE_5cb8J-qFC2MuPtdqkAdDsvEvsBJfCuOsISMLSTKdwXRGPo7N_XG-NmI_i4Q08lX0x1t2KHYyOBReq3CeciGKy4tJXyH4oHxDbRsrFH64jL1Z8dl7ihiqVut2ueNVukKXLmQuFFFteIKougYnUJm3urG9YyzdvqkgDHeF3W9m1ON24GuqDwxZVymw8sArAVUmqwrNO_0SAPM6AD1VaDxFy5u8947lyFp6lt6LoiNJnYvvKEAlEIN5zlFFU5Iw-xqG-Q8OooWUIJ3XaTZxxY0FnKeEqM6NFes-UewC3j39Oj9-ZxP_5YU0r7t_HalGtqCu-cQi96Ud0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج10دیداراخیر استقلال و تراکتور در تمامی مسابقات: 4 برد استقلال، 2 تساوی، 4 برد تراکتور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31139" target="_blank">📅 15:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31138">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=QF9-9HBstLxH62mtjE7HQ0B0RPlUJtpKTOpHnVp3ElyypzcEPjsFSRCqSbXRtuVQr10HWJigOjKl1lmUxVP8XNwcePeXmINVgQenUSZYxRjbi3SKoh1Oo7CtM_TuLDkieb59N4cK0jumE3-1RKUocE3GXOXv5lOoNUwoQo74WGZ6T2PpTjzzYe6UbqCLzWem_CPDXrRZXZQQshyGxFTOAgP4WB6ODkjacjvXg5F-uM2u4O3BtpaLelU5EdKWWtBce5ubwGLuLipyIM3l0VkpLSIRdfGjMh9Pdqk2CndUgF_p-kKNN9Bcn7bIzE04wd6HNvGpFilTz0gyLq1pLQSqfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=QF9-9HBstLxH62mtjE7HQ0B0RPlUJtpKTOpHnVp3ElyypzcEPjsFSRCqSbXRtuVQr10HWJigOjKl1lmUxVP8XNwcePeXmINVgQenUSZYxRjbi3SKoh1Oo7CtM_TuLDkieb59N4cK0jumE3-1RKUocE3GXOXv5lOoNUwoQo74WGZ6T2PpTjzzYe6UbqCLzWem_CPDXrRZXZQQshyGxFTOAgP4WB6ODkjacjvXg5F-uM2u4O3BtpaLelU5EdKWWtBce5ubwGLuLipyIM3l0VkpLSIRdfGjMh9Pdqk2CndUgF_p-kKNN9Bcn7bIzE04wd6HNvGpFilTz0gyLq1pLQSqfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
میکل آرتتا برای تمدید قراردادش تاسال 2030 با سران باشگاه آرسنال به‌توافق کامل رسید و بزودی با حضور در باشگاه قراردادش رو تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31138" target="_blank">📅 14:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31137">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfl5d1dCTeD-NAJVk3opUOjRURsSe4Y0J-Z_CSVhas9nU2Nl5CIkSmcfSIh_8MsnUdZlGg9doREzoIfh92s5UPGEn8vFmeqImv_QREVVuUMNBh5D3vJF_5BrCFmvEiyzL0z01wWGuXZDVCm4qiK0UobMhwuetO9pV6AXptRJqH2uXGCt1_a4PdVE2r5eXezB2GYwPKbLx0VZoEw3V5prjnzuI4jkxBeeGuZdyGX8AtDjtRLmj_rTSeL08LJp4-mMC1LtclhXi5QWo0ozuA0v-RFIHXQlQsu7JvMx0QEnLiFW0NVkpXcPNYwG7J0-Y_cShAdAtNgyM45HewkqfG0Pzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31137" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31136">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQwjopw99ky7L8SZ-x4N6X8t9pSY_X59kl-6hox6TaFtqU7e4U4BFbpIlQJiKdiKBme-gZ5rVYyeOJMEK9fsLgvs7nDrAA9Z7VJbzWTUT2IDW-VdSH9wiR8tkhdU-WhHficRsAWCE1mwiK-tDv5kifiDcBzjRnxh5nzrja6B-G71BOLbg7UwWx3BnOfw1euS0XKB3SVpektesNEOMJWRW-zCrx4eZYPYVOMvcPBOwjN0_2gzTMknfyul03wR7nyYKR2HZfmTyfVhgGlEcIMMDlRE99SfyR2gtZbx0JvQplvuFHpZqMb8XzLw8kNki6D6XNe0ghFUD_XglM5yRtHn5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛ پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31136" target="_blank">📅 14:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31135">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=jAsANt3DaGSGsB45AO3qmCY8ta27OO_u7E3AuzntZ67d5zBempBoOxFapD_n3KYRILjqs0Sht37lYKzI8wBjBOfQEx9AtnDKulR1Zff6TNG0bHtQQHC9foBlEGkGVLnEDbPaTxFrbXhyrWPiQGz15czyUKXruJrXhs5ySd8M9CSMxBk3xAwrICs67yJ_biEPxedT0DDaJ7452gxGww5_KjoSvAQmqetK8keoSp_LzmgRhN-yAV4Iadc4Ytxm0ry2lVAy3pzuHzAPLxJG4yP6AZ8KBKyUC3Cbka1WlmwXvz6UEglxkuk6sJT20kX7e1vU_ua6d9c-HXCgTZGhttsKww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=jAsANt3DaGSGsB45AO3qmCY8ta27OO_u7E3AuzntZ67d5zBempBoOxFapD_n3KYRILjqs0Sht37lYKzI8wBjBOfQEx9AtnDKulR1Zff6TNG0bHtQQHC9foBlEGkGVLnEDbPaTxFrbXhyrWPiQGz15czyUKXruJrXhs5ySd8M9CSMxBk3xAwrICs67yJ_biEPxedT0DDaJ7452gxGww5_KjoSvAQmqetK8keoSp_LzmgRhN-yAV4Iadc4Ytxm0ry2lVAy3pzuHzAPLxJG4yP6AZ8KBKyUC3Cbka1WlmwXvz6UEglxkuk6sJT20kX7e1vU_ua6d9c-HXCgTZGhttsKww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه‌ارزش‌بازیکنان دوتیم تراکتور
🆚
استقلال بمناسبت بازی حساس فرداشب دو تیم در لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31135" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31134">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=DAMQ-xDcYOMoLPgZWRkxgSJpQjOgw6wmiVHQ1QIzqHuyKbLK4IlPU66pE3Jy1L3tYch0A42m19ugMbatGChwxG0BM3Se4QLZhPbW4tLchIS40awzIifzvpYIe5mEOsWZedXkSkjYcBlLjZnDOvysaZSOBuz3Zjw3WE7672umP-o99K4IIlsnSh6f1YBy0G4KO72rnFMoWSKeQrNxyGuc28nCy64bFwjjNoJPzpAyWXNBi8oW7-gfw017x6aD6IFGD0TMFunH9QO-GFvgRd4mj0b6-wxy2kwZhMrXq_Qebp_lPy7BWO3jM3Zpw9I7iz6690-9Q1Bmsm3aXDcXlw14FKGGbQwhXjshGV_upXroAtv0SHHCRlPZNjmLg8KMyCj7J2BLb_BzxoWech9XeRIiwQ8GAoFEf2o27Wk6YmrIE7Bwa2YRs10IMfvg1HWMfxbbJx78SKXFnPeVFBgbkX9-CddH8opLTTAWKTgVbG3oU4Rl-kSbfYo20ipvarJtLCO4KdCLlJMiTfdlYsjGE56OpUlmLPhauf6Vghlb9YAL6B0C1fVP3AsPBZcMoVCo5Brf9mSn-1EK3DFiYEBFDufrBmjRWOG-zF_5RK1IkZfvDIEgzDbrz3dCKO0Mq10b09rzhAcLcUlROoQDd8dHtKPOgwUI-LfT2-f3aLWF7PbXGVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=DAMQ-xDcYOMoLPgZWRkxgSJpQjOgw6wmiVHQ1QIzqHuyKbLK4IlPU66pE3Jy1L3tYch0A42m19ugMbatGChwxG0BM3Se4QLZhPbW4tLchIS40awzIifzvpYIe5mEOsWZedXkSkjYcBlLjZnDOvysaZSOBuz3Zjw3WE7672umP-o99K4IIlsnSh6f1YBy0G4KO72rnFMoWSKeQrNxyGuc28nCy64bFwjjNoJPzpAyWXNBi8oW7-gfw017x6aD6IFGD0TMFunH9QO-GFvgRd4mj0b6-wxy2kwZhMrXq_Qebp_lPy7BWO3jM3Zpw9I7iz6690-9Q1Bmsm3aXDcXlw14FKGGbQwhXjshGV_upXroAtv0SHHCRlPZNjmLg8KMyCj7J2BLb_BzxoWech9XeRIiwQ8GAoFEf2o27Wk6YmrIE7Bwa2YRs10IMfvg1HWMfxbbJx78SKXFnPeVFBgbkX9-CddH8opLTTAWKTgVbG3oU4Rl-kSbfYo20ipvarJtLCO4KdCLlJMiTfdlYsjGE56OpUlmLPhauf6Vghlb9YAL6B0C1fVP3AsPBZcMoVCo5Brf9mSn-1EK3DFiYEBFDufrBmjRWOG-zF_5RK1IkZfvDIEgzDbrz3dCKO0Mq10b09rzhAcLcUlROoQDd8dHtKPOgwUI-LfT2-f3aLWF7PbXGVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم از روزیکه جواد خیابانی وسط گزارش مسابقات یورو 2022 ول کرد رفت. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/31134" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31132">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6OjhFvCsL_0vQEEba1ljvcOMh1KRmFcP2jHZHKAGCBesVDzyM-p9kT8oQ9el2t0yNSHPC9OuclJ2F_e51A-cMHLHprM4NFnY5s1Yqtbn2BKjyr6JapJczNqEk2wNVmSxnPJKafZ1M__cbFVnfP52QmE5F_ihIYBaHXi1JDj_eRCi_3vDnnvqP4K5Kiw95_74N2lmHzQwDIUZ1i6pyDZsK8vz1TWV7EC72uFdyiuve8gLGR76EtB-Kxpj4xgMgjLKA15wOV5z06-Dt1Wk-Q6Xm23GHkKuuYWlir-SXbL8hocpbKS7lB7yL9uDe1YhLtGJ3BoBvJbU2V8-s1rqnr9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فرانچسکو توتی درباره‌ افسردگیش:
بعدِ اینکه فوتبال کنار گذاشتم و پدرم رو بدلیل کرونا از دست دادم، همسرم‌کنارم نبود. بااینکه بهش اعتماد داشتم همه به من‌میگفتند همسرت‌داره بهت خیانت میکنه.
‼️
من تلفنش روچک‌کردم تاببینم راست میگن یانه، کاری که قبلا هیچوقت انجام‌نداده بودم. بعد از چک کردن تلفنش ديگه نتونستم بخوابم وانمود کردم که هیچ مشکلی نیست، اما دیگه اون آدم قبلی نبودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31132" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31131">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRWCLm8wKbwOACCaHCfQaL-l_2g8AIQtnuqwZaaZVmtPT3gy4kaObtq7amq50UQHno8HpkFpWQeQNdWO4EAIFCfOk9aP0JoHehjSlky1NYcp9EXLxcqnDOx7Bz2Tgwt931BrKG7pCkGPnwH0uh-aS_sc2T5n-1mGKQ4fISG3rCg3-B8MZ4Z0kxldsj3p10CVcl-CZlGz8zQgRjqpx6z2VsvQ9k4pvmbkkwalGlIHBfy9P_pP7lcr-tn2WTWD4ObHGACcmtX_fdF5GCbQnnhXg5ELNXBqM1To2sXErR79RlIsQ5priUfqmn5pN6wEiqaGZNG8cw7jEbsnd_RNAi2pqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/31131" target="_blank">📅 13:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31129">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=U_u4KWUw3Q2Ri9rdNwpjNw6f3wQAgvIN-2XRAz92ifkTUDmHmCmInqUN_7uEbUSV320vnp-TAnfodYfYEc7Cfhm6ivZzs2iukv30nGdTM3AlvDv1dAXJ5QaC32p3zecSTvBdqp8sNBtJdpQbJLl42EZIovROlR7yuESbiHLdBKxQiuFdGS24xqh6AiJDNcRry1WKDrVdk8tAIkOq6StSG2ttMXTiaC9buB06bv_C62gTSqDSDkBloMGnB_b27b3Qtch8nKm51ffP_h7BL32RJYIhgnytiWLbxzkn3aWmxCk5zKCgOr0dP-ghCFEmIEf0UqIm2xEvMRy6eb8VXZ1h3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=U_u4KWUw3Q2Ri9rdNwpjNw6f3wQAgvIN-2XRAz92ifkTUDmHmCmInqUN_7uEbUSV320vnp-TAnfodYfYEc7Cfhm6ivZzs2iukv30nGdTM3AlvDv1dAXJ5QaC32p3zecSTvBdqp8sNBtJdpQbJLl42EZIovROlR7yuESbiHLdBKxQiuFdGS24xqh6AiJDNcRry1WKDrVdk8tAIkOq6StSG2ttMXTiaC9buB06bv_C62gTSqDSDkBloMGnB_b27b3Qtch8nKm51ffP_h7BL32RJYIhgnytiWLbxzkn3aWmxCk5zKCgOr0dP-ghCFEmIEf0UqIm2xEvMRy6eb8VXZ1h3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دو ویدیو از علیرضا بیرانوند دروازه‌بان تیم تراکتور در پادگان حین خدمت سربازی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31129" target="_blank">📅 12:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31128">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGBPEhjMNuypcmV7PyrOIx1GYQvyvjEBiejXXnffms_9S6r9XbA27S5IYLXC7FIKaJYwsRWHlyXrqP75ibTnEwS2AQTsTxWOqoYh5AIIPld_4M9ja_4eF-uYSyRQ-Eq_ONm34swrbBMoakyBF8CIHyCUNVzfOns9mRFAcj8acGHJDODj6yA26PNjXzuxCQmBzQIedBUKb4jbNAd0ixGUXQ573MJeJrrfWg5LSkA62Iyp74lr-QqZAFev_Dd6lT_htTufMayI809lZAX_gGCxz9H1kx1amUEwk_MFTFVrfHtQyHB7DjRg9P1h7ZN2rakqWnfL5FR63zAhk3D85lGtTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ رامین رضاییان که‌دربازی با روسیه از ناحیه خصوصی دچار مصدومیت شدید شد حدود یک‌ماه دور از میادینه و احتمالا دیدارمهم مقابل تیم پرسپولیس درهفته دهم لیگ رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31128" target="_blank">📅 12:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31127">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU0R4WOpFi1P9w5gYOjgQ2tZAZLhNExB4pn3XcQm5QWYPJMOYP5FALDYfoWVD2304hAkXkSm2CWuG39uD4Eru9ZX_mN1knt3cTVP_vCWDXET0J0ZlfVcRfPqSXd6u3dhZfmYYx8s8jGt1htx7Y7VCRjmVSelJRUWa5IHwmiBzZwYAK1kwBJzQpslW7GzWEiYOdaK6CUUSg1M1NjhRkpkMd6gDhHlPFhATIEhoqlIj_ER2GFs6xnLlCXDQchZn2fnS_AMR1HOCgYUjSjyoFwVqOhGMJeX_CYGEdKBFhOf8B5AYj0M1Jf3nqGz0f7XVlfsh8MxbgrBIMVFJoU1O5aytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛خبرنگارباشگاه النصر امارات: کادرفنی‌النصر از عملکرد مهدی قایدی رضایت نداره و تصمیم‌نهایی‌اش رابرای قراردادن‌ستاره 27 ساله‌ خود در لیست‌ فروش این تیم در پنجره ژانویه گرفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31127" target="_blank">📅 11:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31125">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=FDNHuYZ_iAshoPl5HGhgyiJZtNF_rwZngZtQ2GFe8A17HueGzzKki2yKyNVIAacE4xIwbsSmZKScIb0Kk2i4i-6R6MOhcdm_x_WRvk-Fm2bYqYqrA2uPpe10hH2kHuopd3IriEr8hzsXhTjo7ZadDW6rZuUXx_9Y4MB7c6DsJYin-1RSvqMR35xBewXOy6Qfv7i2B1oav-tpe3gouMFraC4BvLtviudrRLBKJd5TFB3Lgj-MJ2kK1ezXYzATiZEd6BwKUIH3uBB6C64Llk4-xYJI8uZW1_YqQvwkjnHZxGSvcxPIViPXQzpNCWBXLYZ7JHRL6Adbif2WzEsfiF2-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=FDNHuYZ_iAshoPl5HGhgyiJZtNF_rwZngZtQ2GFe8A17HueGzzKki2yKyNVIAacE4xIwbsSmZKScIb0Kk2i4i-6R6MOhcdm_x_WRvk-Fm2bYqYqrA2uPpe10hH2kHuopd3IriEr8hzsXhTjo7ZadDW6rZuUXx_9Y4MB7c6DsJYin-1RSvqMR35xBewXOy6Qfv7i2B1oav-tpe3gouMFraC4BvLtviudrRLBKJd5TFB3Lgj-MJ2kK1ezXYzATiZEd6BwKUIH3uBB6C64Llk4-xYJI8uZW1_YqQvwkjnHZxGSvcxPIViPXQzpNCWBXLYZ7JHRL6Adbif2WzEsfiF2-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تشویق و خنده‌های آنتونلا همسر لئو مسی درشب‌خدافظی لیونل مسی با پیراهن آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31125" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31123">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg8ug2wSDCdpY5JzzJY2X99USE4Cr4veJUSK7oxpZeIArSECdZCzBNqpSSOabe-lmYGuhZMxDnGpY97VObi3rBzti-nUC1j6Qc4jEZbIsi3SUNJuBEQFLPfBlyE0c0qPF0pmSeHbj7uSTVcZ6VWK4R7itrs8_TaU2qUpECUE1PG-oPdIto10FLX-Z6LSA9LLQgopcwRVOKBhaeIaxboyvkHtf34J6Q6Stau4s9rIjpX0wra-qs4tEJfyXSE0Qq0hE1TMq1LulDplTD8-iyA5Rb_pthIMaUCEalTVTIH5nvoU_Do35nwor7IKs75ohF6P2ScQoBTbm2lc0s-uNrDNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دو تیم ملی آرژانتین
🆚
پرتغال در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31123" target="_blank">📅 10:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31122">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YffqGT9abPdzXOIoQl25DUu0vZrT0kWGjvB0G9dO3CWIgK0cpc8ghmqppl60TbHony0w_4hSIT6-hy9J6mXue70hd3-3VPOBmDOGCIjUVIk4kghGxVdgPcvPZ3f4fdEq5MmRwFYEqxMcFHb9u83FevSp_SJWjdbvR92otLCxy71Yr2GiwpaMvjYCN_Jza4Dt-_BI4j01j09h7L9uswdUiPOy_38qHp0QWrKet7ys5qFm4B19MRmXNLu69XOJbU4N9gVMe0k8RnSyqmOVKqdchM6b8r_1IE7wjPMSgM-MW0i86QXmxhWpoEFqL4Wsdfi_pHUxRimupMGWdQGk8arqtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمام 126 گل‌ملی‌لیونل‌مسی به تفکیک هر کشور به مناسبت خدافظی همیشگی او از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31122" target="_blank">📅 09:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31121">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfHq6Zl-7taOmdJJs0LyuRc-A-Ko3HnVSKVENvUFzuZ74iETEeC5sOrt0bwVRn5TzbJyiPR6r5pI6_JPr-uVGWt0hz4fyZPvtmJiBegBZKD1Uuwh3jjNOGqZf5vpxaMZL6tyvSdG3XMWgG1Sa2HT41W2opj-4CXi3bCiBzb9PxB6loRZ-68HvsmqyS7M9gY5AAVDQQXz1Kg3q0z7NTGmPEJR-jy7HAslXnAqfE221aU1nISOK8n0PbKOWAxzGImy-BaqmdwB8taBa_2jlZu72d6Dw9cZaj0kHHoQT-rrlLmcHuTZROhssvys6jh6RnYm1zm33LVux4-l3z1-gsTHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
هایلایتی‌ازآخرین‌بازی لیونل مسی فوق ستاره تاریخ برای تیم‌ملی‌آرژانتین که بایک گل و دو پاس گل همراه شد. دقیقه 10 مسابقه متوقف شد هواداران لئو مسی روتشویق‌کردند مجریان شبکه ورزش فکر کردند لئو تعویض شده. ببینید خودتون عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31121" target="_blank">📅 09:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31120">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">📹
گل‌های‌دیدنی دو دیدارمهم و مهیج امشب رقابت های هفته چهارم لیگ ملت‌های اروپا 2026.27
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31120" target="_blank">📅 09:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31119">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a56csq3L3u7-etpYWLYvwQ_JFEf2lUxBYZvm5XUGxSycyRiG83Dop_8J7xd65_R5bLV0Ez0sx8Gdqahr-lsr4fs8VtUJFjxyxL73itFzUx2LXvegGrRVAFGniqfv-eQYuWBgh5LkLPh5LWIPHpilgW6TfyWgrQRBJG3jeHBZJJllcTeGqxLtnhd_NoAmlZ1bhWM7pD0p3S1We86si8BOzKFzD05PTG0YuEUYf9UrByz2uTuWWupPV6dI61DpExif7xzqJhMhh0Ld_XQYOFHpLJ796kVOtmLKBFuzgSCP_iiDWXJtiMIw3OurTNAMad9xFclMsP3_UU51JP-wfsMSuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ شب خداحافظی لیونل مسی افسانه‌ای با لباس تیم آرژانتین و فوتبال ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31119" target="_blank">📅 01:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31118">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVRdxnNwL3lX4uT3H1u7wITcFfeKi1jwJCGbQIJUNgzyqo3hRFKSGFarorr5T2_A_hBJkusajIoNLzNnu5NKgf3UJENqVSOJ8OmCBXNSxx8IH_dC89zaTRcHb9RlT0N56EDLOW6dFMaGtpz2CRWyWZOHYkctEdFixpEsMaqIgbVGbZU3S0x2jndo2Q4N3O7MDGpKcv-d-dYfY7E4Mu4y2k8rax9eOqphvK2vJ7ELhlwhs0XSDqzqS8CK9DvD5TLx3U5Hc5KHfMHQSX-iYbObBQkO1tyz45HWrtTwskK_ltSp5a0YruxagbPzGmk3C2P9lESGGs7DuqojJOFDEfUuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌‌دیروز؛
کامبک‌اسپانیا به کرواسی با دبل میکل مرینو و برد سه‌گله سه‌شیرها برابر چک
🟠
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31118" target="_blank">📅 01:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31117">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
هفته چهارم لیگ ملت‌های اروپا؛ پیروزی ارزش مند لاروخا مقابل یاران لوکامودریچ باطعم کامبک و پیروزی قاطعانه سه شیرها با درخشش هری کین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31117" target="_blank">📅 00:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31116">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUbM6OXtXQjgJWC0FVKRVkuKpPDqmFEIZRuSLDR8XuLvuabQVR43H1GHoQmAUvmjPxBZ53fk0Zz6cfzebciY21L-45D0jG_Ez6tE9B0G542Y8oyC1zWBsWFcuK0dzX4Huo0Rn3Tn0153GgqyBjHMQHJamJRQifAzwypPbbSHu829o18wLfxVBDp68oTFEajBe8KBoRy1_Lr6aYETbi2L5PhzeFJBeZrpnTpEqOp4dOjxriqKkKpjISNwmPOqJI0sJAfrjRckZoN3SG7Q9UvjtYzIFbTaSEx8kCdcJMR6mbj1WKf6uB6XuNGuDv0PDThlr9yLQ8J2gMBaAh_7L5T07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31116" target="_blank">📅 00:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31115">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkp4QYk59KDZHr9pX-3pv0ORPtArp9_H2j-nXbrVMu11zWdZoQSC7YRCxReerWE1ybxB7dghusO7SI3PbGIUrUZPQ02i2JEJzyc8WXXp6W2OFOAcyc8g21P4CgHu-JjDroeyD6gWMuGl0iumsMXweA-Pr2tEUqFDXEvO0GBQ2nCLL8z6HhpE23eXmAdA-1BUZw24-G-sPma35ZZmsPdocauSL4OdcyC781gED3nmwPutdLWSriJqNfQIFL-AgmvTkbnDjkoT2Yw-_VVaBuj_xHd6-awjACouko16PfGbcrXVK7itNE_qxYTA_k0_qXYOprCXZ0nZx5rEBRmCps_t_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه العربی امارات: رضا غندی پور و مهدی قایدی دو ستاره جوان ایرانی شباب الاهلی و النصر از شرایط خود در تیم‌هاشون راضی نیستند و به فکر جدایی از تیم‌هاشون در نیم فصل هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31115" target="_blank">📅 00:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31114">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pShAX6L7upaFeh7ogjO2C7T_5Z4CnbpKBBWtXdnxUPW6XrjMvYV8DIOswcUroL952ZfWjqFC2bgTEj8MCHkolvPc6wFiae2Q9zMvBCldlj4hyj7ywMTs_1FZ44rHXjo7Qlqw-cSguykvphKdCxfcKIW3e0fN-bpPkbVRt5ljKsW0xjuEzYA1DerQWFXPqrAZ6baNojl9mAJaNw8qNPWmmN8_Nuf3xh66aXiZEDHvHK6vSXUIkurVA3Gm0jOwQUZg0VcuO5Zqzhf92HWu-JwRAKfZSM0IdSNLUfNmQFbt1LKzc0Al_gMIlxFw0aj1rP_NHtbzRuYdeExLV7mFbevjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته هشتم رقابت‌‌های لیگ برتر بعدِ تعطیلی چندهفته‌ای‌وحوصله سربر این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31114" target="_blank">📅 23:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31112">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LawACOP05lihh1-eCaWyppi1QcG9wHnDVEM1uLhnD8WSmQeafHE88Ti3Z92HZdSUtXHoI2vwsFPnw01mLN3YNx4T8PqJmoKdNmfGagPr5PoGK2BlPmV4xR6nqMkO55U8Z7gP_v1HC5yw2NGYTvGhlFfKex8GkId3IGh84MJJvV_7UnVJGcA1Ocog4KHp9dIc14oW_Dxk0IlH_4xTrzKCjwTuA_288Fmf3fEY0yo4-djmKAoeQ0-PxDY7KzDlluCJnrpE4YaluiLCjpf_kJ5ysBQUFoRYukkxJmtYty966r9icLqvTfGAzUoJYqyVIrUoRRxEnpsmRBguSWgrsXHTAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdaMT27D62o9Vg7ZXVyQ7-8Iw7ChXPw6eWCdz74O13feryfTuK3rdFqfQEogPGHKP3rmE4nVUxHZr1EnCGcWBQ6IVQ9hcIiO0Qb3K-cjtzw7gQJiyYQKBU1TLvl6VSnbugDiWuEhd76m9AlwaEDKztJGm-rcuk_I713Upq03iHiCDAGYx-5wIPmz6dU7uaEjWzOPhmxCznbRjpHio1t81dY82E6FIEZlNg70DYXv3pOJ9LM5cA3AxkDWIUnVNfGJNUvRFg3ibEQjuTg2zgr76mKErvSTKAJVl0AZKh3ivTv7LopJ5Mnn8cEiR8VDjGwP_k_oWHMo1wxz9HtjvF7yNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در آستانه چند ساعت تا آخرین بازی لیونل مسی برای تیم ملی آرژانتین؛ دانشگاه بوینس آیرس دکترای افتخاری خود را به مسی اعطا کرد که بالاترین نشان افتخاری این دانشگاه محسوب می‌شه! دکتر مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31112" target="_blank">📅 23:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31111">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvkHF8wAEbq9U5bm9BoRbANATt8rzPPaiFYvqZNwWDQmlo9Aq9JxSO46141dyoVVdL8TIgqybGNwgYQ192TDBCB81t1RhsKdJhOl5I38_LzuSX36Xgu_WqZo-U0ilE9MQpx_zQNqLEUtsnsGL3UaHG2Vot6ZuH7TiYDRXlIyUQuP7ouY4_Dgz1Lr88afKw4syX_zE022d_IfZRGiNI7ljDe2GEQomeSUIQHZXLAF_Xa1tbifblR7_x2uTq0plhCGf8WQZMAJcrMf6Vc8iSkqI-5Lyv9SNaLjKQVNhDRyyC3Be5Zuqgx-StseQlUgN2VMxzUDseS3HefdJEE5XO-DJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال
🆚
مایکل اولیسه از ابتدای‌فصل2025/26 تا به امروز در تمام مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31111" target="_blank">📅 22:47 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31110">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USBOslQIlPtOHgZNLU2AcPcGBbRHRJ2KpPPoUouic9jTXfAyQSWLWT-WKEaTgkLLNQSdalUHqjfvsR11eUUAToY9sNDBIGkvpLtPuqjSh34eAyjGoBUhRHsi1NYVBfyum3B3byf5znKjCUCMNyckkET_rAwLodwimzjvcjzW_raN4-MX01ccwYx7ES1pzcFwcKDzxICbq6fyPxFGcnDzkwEyX1AcUzkJxHjTz1i_mAYNfI-ITH08sj8NXqJT_yPVBajaOBpcR9IVHYmLnyi33Pnlmjj59lyj1LmgYEW88zEUL9UbDENOaTlsx02Bq18R4iljRjbzYoQEkvy_Dmlu8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو: به هوادارانم قول میدم در آینده چند بازی مهم یا یک بازی خداحافظی با پیراهن تیم ملی فوتبال پرتغال انجام خواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31110" target="_blank">📅 22:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31109">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulyuaJzQDH8pUHt3QxWp6j5ASnpfrIAWK43WMqwukQ1QWoXLiTFX6q2lu0lYH5cgMX0_lqBDaFC6jlscAl1HFFEvNtAXZXh5eZdGd82IB9y4oZUXbf3WvTZwrLZxTScNJyIe2344ZgrNgbX-uaYUfk2QnTkxcA0v0ebLbqj0_Mu8QXA4I4vbXvL2pufVE-DCidKd6LWUIzYr05sZquvSWxf6d2hWX_axfq0pkFDOev3fUUGGeEGeon2FD8ecQCrmd96qirUc3laGf0vmiknHikk6CyPI_QnqkzwhqOpx2Lmm-Yy2FFZoLjKNHvufDRAKMvwwqc5Q3T_vLB2dPqxHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
آب پاک کریس رونالدو روی دست فدراسیون فوتبال پرتغال و خورخه ژسوس: تا زمانی که این آقا سرمربی تیم ملی باشه هرگز به پرتغال برنمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31109" target="_blank">📅 22:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31108">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oex62IiGJgdiSq4AdQE4fy6wEC-d8HgaWS6658IfGRR5c9A7Q8k6BoCLndo8v58kWx2AhhU12JnpmVCX9QdsFvRXJnr7LJayAoNYyrem4teiGG3oRyiB8M9t9D5Pno19-v-r0efdTP4VrYlmTUrfI2KYgLJ47TQaADdKfUQCKYINPvaTxmvfjxoMOx3onRVYrGJViau2FKENuA6wYXT0iClF3i3at0BbER92E-dPQ5erJZxQoei2aQTcqol74FFoshbQgxWJknT-qzcpgV-G6dXlSHW4dNPExYzMhbUstxqRiOjv53lOMb3FNwr0h6sd-m896zokxr9WorI8HSyt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
وضعیت پشم ریزون خیابون‌های آرژانتین رو ببینید که مردم‌دارن‌میرن‌سمت ورزشگاه برای تماشای بازی خدافظی لیونل مسی با پیراهن آلبی سلسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31108" target="_blank">📅 21:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31107">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENgCN-txJm8UBk1kvVCJok0FXY-T8BbQv1nIn3xa_GC4o8GlUjgdUu77N0Xak8uKPxV-QFfHi2MymIBd1aoF3BJZkcferbd0vO3nmB4j7g1UPo9eVnvL9uX_Aj4c4TIs7xh-vz53K7NEs1IYTofhlXqicySDU9eedxwIGxa9nEx6ptJFZ5kLH0wF3ltsfYWpxPUAvibKIQ2IRGeicBeIr86lknQjt0tslVPjLNuZ4Qv2A5fpBB_ozEeTxBim794EAH6BebeUqnTcnVlSKg9t4qJUdIAKUjVyQZ0YItwlLri1CZW8OOFkhZepvVeZAhbNv-a0BzSk8AaftpPyfAoUNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وقتی بارسلونا رونالدینیو را به خدمت گرفت، این باشگاه چهارسال بدون‌قهرمانی در لالیگا، پنج سال بدون قهرمانی درکوپا دل‌ری، هفت‌سال بدون قهرمانی در سوپرکاپ اسپانیا و یازده‌ سال‌ هم بدون قهرمانی در رقابت‌های لیگ قهرمانان اروپا سپری کرد.
‼️
باورودستاره برزیلی همه چی تغییر کرد. جادوگر درسه فصل‌اول خود، دوقهرمانی لالیگا، دو سوپرکاپ اسپانیا و یک UCL را برای هواداران به ارمغان اورد. یکی‌از بزرگترین‌ بازیکنان تاریخ تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31107" target="_blank">📅 21:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31106">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=ff1hG9yNI9a5WXQg0h5ilc8rGtu0GgsMmcZKwvNg3d-sEfZblUEzLs5oIDs6Okf3pBXowWcauUcDd9ZbCWLXKIXvh244vAZ-dp4Kdf6wQpaRT5cF2Bi2T3MrTynu3O_dXpjYsKQc_IxT-SOYqzIY7fOZtZW2gdrqCtdWT1KgGdAov4hM_yhsqjwQnjjj2nA_QLDxRJYjipJL4VJxLjnuD6uLfCvoFprfJ6QFXDO3idUvxC2VXCgowXMleMdb7Bmsmiiy3SM_rMDHBwhKsAdjZXJmKG1nIpZx_HCL7nbT04_Ycp8CPfk2DCKnTUMXxB1Npi_fcus-vN7qHck9jlnls7ZfcNXkpAHr1YNMx21uUqCHTG_g97SSPMNTHw3T_qKu7idsvC2MJZrf5Rs8YbuyMEEbuGi2lI1cXJUQU-SLv7cA8VhaFHsW5VL3BSEZjgjYTBAeVbsav_O5dV496y6ghUANGR3C_VFAEoAJaPoeWj55h6c4-s8YXK7B2lX3k6k2zlP53LFcprPZiQAsRpKOvbNQZU3my1c82Um_l1MwWJZKBATxhtSAzZJvagkeuImTLa89Fe3_HbZ2bHrtSzZp8780VFJEUcJv4ynnXlBuYMAj7L0Nu9j58VszOP2RMEY9UBX5GOlpQVhBMAE5kLO9hubfc_E_qq3tkQgMGIwcUc4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85a77e7bd5.mp4?token=ff1hG9yNI9a5WXQg0h5ilc8rGtu0GgsMmcZKwvNg3d-sEfZblUEzLs5oIDs6Okf3pBXowWcauUcDd9ZbCWLXKIXvh244vAZ-dp4Kdf6wQpaRT5cF2Bi2T3MrTynu3O_dXpjYsKQc_IxT-SOYqzIY7fOZtZW2gdrqCtdWT1KgGdAov4hM_yhsqjwQnjjj2nA_QLDxRJYjipJL4VJxLjnuD6uLfCvoFprfJ6QFXDO3idUvxC2VXCgowXMleMdb7Bmsmiiy3SM_rMDHBwhKsAdjZXJmKG1nIpZx_HCL7nbT04_Ycp8CPfk2DCKnTUMXxB1Npi_fcus-vN7qHck9jlnls7ZfcNXkpAHr1YNMx21uUqCHTG_g97SSPMNTHw3T_qKu7idsvC2MJZrf5Rs8YbuyMEEbuGi2lI1cXJUQU-SLv7cA8VhaFHsW5VL3BSEZjgjYTBAeVbsav_O5dV496y6ghUANGR3C_VFAEoAJaPoeWj55h6c4-s8YXK7B2lX3k6k2zlP53LFcprPZiQAsRpKOvbNQZU3my1c82Um_l1MwWJZKBATxhtSAzZJvagkeuImTLa89Fe3_HbZ2bHrtSzZp8780VFJEUcJv4ynnXlBuYMAj7L0Nu9j58VszOP2RMEY9UBX5GOlpQVhBMAE5kLO9hubfc_E_qq3tkQgMGIwcUc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رودریگو دی‌پائول ستاره‌آرژانتین: هر جور شده به مراسم خداحافظی مسی میرم و از دستش نمیدم. اگه زنم بگه یا من یا مسی!!! من مسی انتخاب میکنم و اگه بخواد بره خونه باباش‌هم مشکلی ندارم. من با مسی رفیقم و کلی خاطره باهم تو تیم ملی داریم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31106" target="_blank">📅 21:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31105">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxOP0AoHy2UAGBjYYbBqvPdTo3Akq7UMu6LZCw4ZFCvwAwIAbLE2MRoZTD0Eo8zcU-PUkZ_1h4LkrojaRcCX18u3cKMASJDG3R30EfBYFrACSoJD_gI-Xk4H-GttHCLrTPgPthOeVJIW3siQSn7nDV_w08X1Igo-CKJjtzBmwFgJFc6YjueF_2FpkLnwCP6ffS0oSApGrs6UT6zLkDfZUWjT6SCPDsIrW3Udc4BHhFJBt8ciSLPzKKEpJ8dkzDK_O2mVFR0p614U-bN5umsDH0KCEpuPdzEb6T13k_RHt3_qEswUCb0BULUr-Y4VuUVGTMxFe2JXDsd3o9ET2q6_1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31105" target="_blank">📅 21:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31104">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SSu0KJ8iIx1XLYWs6rpm7N2fr3Kio_Qc1WFzffcQGeLqzfSY6N4dg_r9F8VRyceCv3ktwt7dodIozbLHbPNK5fnBq4fqtBXJ-s0h_M1jyUpsYL0qcRO1RPHl11rVJVOP7F4--gWKt0PnmAYJMbNjwghPpWodau82Y7styvExlkPBgH4xR3oL43DVenCMK70LSXlCY4b5T4rwhv5QckliKvMr4rL0IZsZYQdj7UG8rL3mRdOgeQcglQQvoYjNh_wis3YjIF3RYx09BVlWDq28074XnmADTwaQwn5c1l5u65pBdTRQfLv7qmFEuE76tJUCnypAWM-fuEuKwKkYAnA7Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش کریس رونالدو به صحبت‌های ژسوس که گفته از او عذر خواهی نمیکنم اما در فیفادی بعدی به تیم ملی پرتغالی دعوتش میکنم؛ رونالدو: حتما میام!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31104" target="_blank">📅 20:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31103">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAKRuwN0TLpZDQdEVmrnNfsiDVr-Nso-pBpJaWewkFoo1DI7wV1JcXOV8_50UxTdUr_fGZ9IGz-PmeMg5-geu7gSLoqxJJkn15FAfgNXKgGgVCVjlQEWpDAlt1lzoSlr60bbp1gMZJVfCitNa3Pc35HXcCUXfWrTHQ7SOFUjBtZXfXP9H3NARjHoTfQQrLv3HNmGI_mpgc-ccCdOY8vIJtv3XTzdz2obn7yN9x9BwDUGANV-aaz4Mi8dnMhjbVgx85cUZRHH0EXL_DJY7sNDfJ5ptaHo13KkTgYVCxTLPwzmm1bcXQWl9uoEGPl6i0EBMcTC7KzUzQtTdjLHIAYuhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی باشگاه پرسپولیس؛ حسین کنعانی‌زادگان و دانیال ایری به دلیل مصدومیت دیدار روز جمعه مقابل صنعت نفت آبادان رو از دست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31103" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31102">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm3m0JeFlUKvURwnYIbASL2uvocxbpaiO2JUw86k8hT_AXkCqnEeerKmaqph1l6bmWZx7aJpC8QaVtbKtf_HNIVdueO96SDm-RwtGXjqMRhgCxIOYZ9whoSVDthZFAg3sZCxsuuF-OcxkbbdQJMBFs88VpqqCz0Tj5btazMux_XBbLWKgnVWb4Q99poGT4aRYCIyyGe9TQnACcW-Ma9yE6nt8l_eU_TDc_w3hhxv_NIzDWoj-uRDbf1h7mHZPFcOImk4wTVt3pXDGDMm6AvVVUYhQhQHQP2XzdDvx9pqvCwImCeQxttaHcOi9ryHU0KnDIXgPej1vTLGARH23YaZ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جود بلینگهام ستاره تیم‌ملی انگلیس که این هفته یک گل و سه پاس‌گل به ثبت‌رساند و نمره فوق العاده 9.8 از سایت فوتموب گرفت به عنوان بهترین بازیکن هفته سوم لیگ ملت‌های اروپا 2027 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31102" target="_blank">📅 20:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31100">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEAKp1ydp0wXnmcM7DQb7Ubl9pIx-PQ57GYUV6xv9ccaZYEyVdqHAT6TKcpVMFOlGK-gJBp_X1HrVm4Fx5SKFCImDWFPFMilya5HFwF5rtyObhTuPpZf_ezxoyp2GSPeUP6oieKBK_kbf51T3owumNUsra8Vl4x8PGLvck1vaNaoIQHs6IKi6GdUHN4KKyAHsSL_6_0Mk3W7IGclXEsi4uEgD_aDkD6fJeUmUiAQODVJUX8qBRD7pntWtnlgQTZGuofx6YHZAZ-VF7EEjI85inWp5g4apKnVx8XuhC11XReTyqq54fCnAAu1h91E7lqf1zPPBLjMV2mvy6-9DRUbLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌خانم باتیمای‌بزرگ فوتبال ایران قرارداد میبسته و ازشون پول‌می‌گرفته و در ازاش با داورا سکس میکرده تانتیجه‌رو به نفعشون‌بگیره. بعد از دستگیری این خانم اعتراف کرده که با بیش از 40 داور سکس داشته و باعث صعود خیلی از تیما شده.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31100" target="_blank">📅 19:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31099">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH8gKkwxxZ_75hat4y7z-Lyd1Ff199ziGygUhJlmOfGSL6uX1fCwOqNwGXbaVPdfoRiPRCDSPWoqBgLR1TKmPYQg_Q6e3A6B8SbdJw6DLIRo7rNW4O704UdJGscd7Wij7VqlpJP8pHqOvYBRElHXPWEng0neLpN7WzenWW6LrU7F85OjlXSeLeKGYPPtvkciwH_WSf-4XnkxIi6_e4R9pAzBdYi4HpXDuhiRxxLmbB50pJgiKu0JxbmNST_u-8wDFNSl2EGUkau8on98altK6RhBjNYwotmwhMAfx3AKTqlmRqliXhxB5MAqeMjdr6qsBjoUk3HIgevYuu7eOleYng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
فدراسیون‌فوتبال آرژانتین قصد داشت که بعداز خدافظی لیونل مسی شماره 10 این‌تیم رو برای همیشه بایگانی کنه اماقوانین فیفا اجازه خالی موندن این شماره درمسابقات رسمی مثل جام جهانی یا کوپا آمریکا رو نمیده و باید حتما به یه بازیکن تعلق بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31099" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31098">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCmy_vMTh-rXS4NkzWc44F2QMf0NAUuamKzrdclCWQMxYVEU4vJNdHbSu8cDVU8gVTg6TinBFLfdxHpGoTAVl8C4uTW4urvaioDkE3KNS26tDk8lNdA_450TpDzg3oqcLL4SwF0Oo3vdlehkyGFSBza8TcwLLArPpf1JvbHde77oF1Ogv0kDZGq22jZWdWhBQNcxqEb5_22i5Uiec9-IOPYmY6MzH-L4ZHI_KyPtohOXUr6Ln5inGdQ69upVGEmYFOuSd1olTAo2mmo1TY6jgS43XzXmi97qEuuy6gC7-0jJveLj7upCPs7oC9Sw2Q8FnQknubaZ3DfBq8SmkLBcNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
فابریزیو رومانو: دنی‌ کارواخال مدافع راست 33 ساله سابق‌تیم‌رئال‌مادریدآمادگی خود را برای عقد قرار داد باباشگاه آث میلان با کمترین دستمزد "سالانه یک‌میلیون دلار" اعلام کرده و درصورت‌موافقت روبن آموریم کارواخال به جمع روسونری خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31098" target="_blank">📅 18:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31097">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plq3A-pJVVDdHtuNJxRZ_RXUCUKzv7T2NiS874NtZ1fWVmvWDiIXei02ADx9oKQluFmr1NGli95tfRNv4sEBCaFFaLpWW1zEoa88bQCU4ra5YyDxhtUEyp-g5LU7tCNayA757COQQwdAexWUy3DSdrTvmeKgs9XzWdVMKwTA5skjQg-1sQAGpz6Q3zbxT8_gIcvQYqe-Zc9u7A--0sq6AT9ymdNpiJWB_IF3zsrPpSgyhu1n0VbfAPvw_PqTFLtOBnaQVupnRhaRD2nfNZ5ex4K-8AZU3hcq2nODurZut6YX71M6fr4GiuluW-2mtMf7JLSjBpKFEGiV-4AnKaYZ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
امشب فقط یک بازی دوستانه نیست؛ امشب قراره که برای آخرین بار لئو مسی با پیراهن آرژانتین وارد زمین بشه؛ پیراهنی که باهاش قهرمان جهان شد، اشک ریخت شکست خورد و در نهایت به بزرگ‌ترین‌آرزوی‌فوتبالیش رسید. بازیکنان بنین گفتن امشب فقط میخوام از حضور کنارمسی لذت…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31097" target="_blank">📅 18:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31096">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=l_aaws3_8yku3uZfPNED_U87gqDt3VRPgk_qgBB8h5QB84jEL_zOK2utavn5fNJwdIi8vZ3-irWkFj7vJ952m4Xj4UrRtUMmXL_p7We7l3oXMoSgN6NoMsHXU6v2DXCA5KlPnrCd2WldUKFsZ1UixoZU_HVOqO1SF2KZ4oBKl0cGKcLNO9EbNCOECiCYmC5-eKmKgmZhJimxp6lGUNrsDKjE7y0BQJ9c5bChyulfBg7FHkTB_yZYUltnK5jbbM82ryuA484czWX6QEsteDlAL5m5PFrI9dDYfByaxA6G_AG_cHkTgRD16yFc3tO11Y39w-RrLpSUcXv6x9lxLPfVdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12aaf08506.mp4?token=l_aaws3_8yku3uZfPNED_U87gqDt3VRPgk_qgBB8h5QB84jEL_zOK2utavn5fNJwdIi8vZ3-irWkFj7vJ952m4Xj4UrRtUMmXL_p7We7l3oXMoSgN6NoMsHXU6v2DXCA5KlPnrCd2WldUKFsZ1UixoZU_HVOqO1SF2KZ4oBKl0cGKcLNO9EbNCOECiCYmC5-eKmKgmZhJimxp6lGUNrsDKjE7y0BQJ9c5bChyulfBg7FHkTB_yZYUltnK5jbbM82ryuA484czWX6QEsteDlAL5m5PFrI9dDYfByaxA6G_AG_cHkTgRD16yFc3tO11Y39w-RrLpSUcXv6x9lxLPfVdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ شاهکار زین الدین زیدان در بازی دیشب؛ فرانسه درحالی یک هیج عقب بود زیدان در ابتدای نیمه دوم مسابقه 4 تعویض انجام داد همون بازیکنان کار رو برای فرانسه در آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31096" target="_blank">📅 18:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31095">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=lbH-EHZ1K_ZlkToJpich-5wznHwJ9--6UEu-aGHLlfmWfUjqpvTHT2nPk4mvAByhMGxlm7-5BfK7iGd0OzuCxvEabVkOscpH4x960tMEYO2w6Vq2mBlA_D1jpMnCbM71y7ZAtBASbsokWBUdP_0uiZsE85EAyiPKBBaasT9uLnGnfGUkeZD8Vivg1Q64nLcCwm5eiEUX6A_yrAXyay9InVDxJ2Eh7t1zzJg29lhZ4T25eMY96nFdJ8KFeWepUxXz0HN536gdCAjnSgvm6eMJvt9kO6PYKpO9Kt1ZnZYoc6vdH4LBWAAvwDSLscP9SU9thPobJUa4lzfCwqZRjw7TNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd044daffb.mp4?token=lbH-EHZ1K_ZlkToJpich-5wznHwJ9--6UEu-aGHLlfmWfUjqpvTHT2nPk4mvAByhMGxlm7-5BfK7iGd0OzuCxvEabVkOscpH4x960tMEYO2w6Vq2mBlA_D1jpMnCbM71y7ZAtBASbsokWBUdP_0uiZsE85EAyiPKBBaasT9uLnGnfGUkeZD8Vivg1Q64nLcCwm5eiEUX6A_yrAXyay9InVDxJ2Eh7t1zzJg29lhZ4T25eMY96nFdJ8KFeWepUxXz0HN536gdCAjnSgvm6eMJvt9kO6PYKpO9Kt1ZnZYoc6vdH4LBWAAvwDSLscP9SU9thPobJUa4lzfCwqZRjw7TNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
لئو مسی از سال 2005 تا 2026؛ تیم ملی آرژانتین راس ساعت 02:30 بامداد فردا در دیداری دوستانه به مصاف‌تیم‌ملی بنین خواهد رفت. دیداری که آخرین‌بازی لیونل‌مسی باپیراهن تیم ملی آرژانتین خواهد بود و این فوق‌ستاره آرژانتینی در پایان بازی برای همیشه از دنیای مسابقات…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31095" target="_blank">📅 17:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31094">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvCqlb8tq2oW8qnvL5oAH-OfzkQ2AzRu8Vm-_csYHoRymvweH_1XjBvLktLHlJxnrmfrJvnovgFq1uLIwn66NTubGYwtbragjuL5-j7dbvH5JB1ZZPj9qSmvq-ZQxb2MMdxS_7GgprHGpgEel1oxpJaLgiyTb5bzRvxKpx05w2-lm-DbAR40B3rCzWg2WWBMt6thdCr-xkrzuVEP4mKRHC5IpO5b-7X9fGbTRNnG2OcJkllC7WPfoCkMyuoAazHB7WWAl-K4ZjHDyk7YM-TfDj5t_hm6GKlmfTGCGKP9lQzNuLWv6ov6eq18olpPSgQVMUVb8Z9BAExmKCEieEMV2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو:
نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون یورو دریافت می‌کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31094" target="_blank">📅 16:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31093">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=TkE_tQGl-8DUsApOd3GoMfGPzV0reh8PSXsBbpfseRAd0eJubwd9gT61Vx95hSpjScoNp0JpDwR-I2BQAjWimIFIM92szt75PPiGARE_G6facRoap7lXf3f0O_jC0RAVUEjoMogmhT7qgSNz8AyxhfaEya8MHzp0wlIe9sMJoFngKzv0T-a4Hk-cS6aS5sqIZQB_f5I7tt9FWGWEYL1YKjmzRLy3i5l6FEN-rBvjAxRrSJiyu4d5rC_CLcFR2F1agFGM4pFV6CTEgm7kt-OVH3zjkCLfAIJYWQQzEWznoFlDKXYK3jS8J3fuGKuttpABIKZzvYICDPUpm40AXoUk5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1a596a3d.mp4?token=TkE_tQGl-8DUsApOd3GoMfGPzV0reh8PSXsBbpfseRAd0eJubwd9gT61Vx95hSpjScoNp0JpDwR-I2BQAjWimIFIM92szt75PPiGARE_G6facRoap7lXf3f0O_jC0RAVUEjoMogmhT7qgSNz8AyxhfaEya8MHzp0wlIe9sMJoFngKzv0T-a4Hk-cS6aS5sqIZQB_f5I7tt9FWGWEYL1YKjmzRLy3i5l6FEN-rBvjAxRrSJiyu4d5rC_CLcFR2F1agFGM4pFV6CTEgm7kt-OVH3zjkCLfAIJYWQQzEWznoFlDKXYK3jS8J3fuGKuttpABIKZzvYICDPUpm40AXoUk5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیدواژه‌های تکراری امیر قلعه‌نویی در چهار سالی که سرمربی‌تیم‌ملی‌بود؛ همه‌ی همه مقصرند جز ژنرال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31093" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31092">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMPfJqZXQtbMowO5ek2JRmnrPueE4yXxqTiQWRzEVoNCzgJSEh3x_0La4qoeg_jlzsMAxCEb40X7KNMyCZIdJ2zagLtK8NOg7CK9TYJZDJHNwbHDag-DQl1KGa7SPwc0EAbhAjTVBpvLBRYt1Sfi4dADMHLyoEwPmeMAopTUhlP1a-D0-EcPijK5U0pbIMe-EU2KAKWd_hQmgosD8wBzCkNzLbXB2RVWjIvkcGjTjMIXuAGlSoowBfJczz0yt0omMucDbVP_ePbgJyjnZN0a7rvN0tRtEG1TnKiU8DGb4gMitT7eIFWV65yKb3AyrtCiFzzMBoYSzEN77GqrYBfJlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تصاویری جدید از دوست دختر کیلیان‌ امباپه ستاره فرانسوی تیم رئال مادرید در فیلم جدیدش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31092" target="_blank">📅 15:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31091">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ghq__iAUfBOtLPPpTff1q-9Iy2M7ffDeMByvnJUcp198h4oz30EjINgrh6-Rh5hAOGDhFmJR8hRB1Q_mS23wHW2nslLqCmuBcnJZXIsZ8Zh-AA1CU5cUFDwDkVvYy6ly4SYmy8MbA7sAYTpB6HU0aPrmCFuYiBRxgBLUvLm6UcPW5nXas7tei4Lrb1Okl9mNLJK266H4tjpehEVvioS8G4YgtwLdt717au0NUhOP32rb38S0gR_0rYkItA3GVGAx4pTWTtvEJHm_UBDWxyuTYV4O_N6-2wYHVMqPYvPcxnShfAoV9NNbMfmxVOhIHmn7Lt6_K5Vl8Yx5O2daYYzm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یاسر آسانی و نامزدش بعداز چهار سال از همدیگه جدا شدن! یاسر گفته بخاطر استقلال میخوام برگردم ایران که نامزدش‌همچون‌همسر منیر الحدادی مخالف برگشتش بوده و آسانی سر همین ازش جدا شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31091" target="_blank">📅 15:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31090">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=UGtSBBDsFWWzwAMcNC-OmexlJaBucF1Sfgb37yknqXC-u0ydRuSUMgM5sVup_p3V0YYVitmb8v7El0Jn7UGqgIIlnpaMefsTdQ3z75Y7qWACcdc6LXKF1TqGRW7ytBKTTYhlfw5eEGsbB0sFd83O21uvRLhJbz9qsei2IznT6is2E-cN5XdpVLyHx9fMrUvrLIsMi5jRv-nsSUNv1tuWpj2A2AaEBjXLN7fdhR8xooIUijlhQQBwhIYR2X2MoGrvL9XPRCesIa9_fiYUrU2dhZBOK9vi4KPArQn4DlYIqkucNFi9PtYbSneIYOMAu9rPyjsaoLEmxwXhZB0w_AN_7YXOqiWFCc_d2om0QT-ie9CWTv8cjlc9mpSBXTx7SsBmvK3bakPzwRDjmfx_aV6JZ_JYsKRSPvHeyzum7hUGbKx-on7CLeL5aYBh3NF40ZQsumxrZs3UGMnv9ibsTygbPd82MffTvTn0UaWUMvr3nn7nucoYWpxwVGBsGkByQIKbXhoe2i8fGuqlp0NgMD0FdfJov8haRn_d-yTLg-AVYG8u5RWzatJLnsOuFz8ipswHB4PMGZXQbpjbft3r1J9semhUjlNTTwSK-8oR1t5Z32PjN94P5-Y5T180Thf8sk-sEnEHipop619j6S2PZiol0t_zrwnkqE9u0TztxYC1BCY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1967f5895.mp4?token=UGtSBBDsFWWzwAMcNC-OmexlJaBucF1Sfgb37yknqXC-u0ydRuSUMgM5sVup_p3V0YYVitmb8v7El0Jn7UGqgIIlnpaMefsTdQ3z75Y7qWACcdc6LXKF1TqGRW7ytBKTTYhlfw5eEGsbB0sFd83O21uvRLhJbz9qsei2IznT6is2E-cN5XdpVLyHx9fMrUvrLIsMi5jRv-nsSUNv1tuWpj2A2AaEBjXLN7fdhR8xooIUijlhQQBwhIYR2X2MoGrvL9XPRCesIa9_fiYUrU2dhZBOK9vi4KPArQn4DlYIqkucNFi9PtYbSneIYOMAu9rPyjsaoLEmxwXhZB0w_AN_7YXOqiWFCc_d2om0QT-ie9CWTv8cjlc9mpSBXTx7SsBmvK3bakPzwRDjmfx_aV6JZ_JYsKRSPvHeyzum7hUGbKx-on7CLeL5aYBh3NF40ZQsumxrZs3UGMnv9ibsTygbPd82MffTvTn0UaWUMvr3nn7nucoYWpxwVGBsGkByQIKbXhoe2i8fGuqlp0NgMD0FdfJov8haRn_d-yTLg-AVYG8u5RWzatJLnsOuFz8ipswHB4PMGZXQbpjbft3r1J9semhUjlNTTwSK-8oR1t5Z32PjN94P5-Y5T180Thf8sk-sEnEHipop619j6S2PZiol0t_zrwnkqE9u0TztxYC1BCY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این هم از ویدیو کامل قسمت سوم برنامه فان و جذاب با ابوطالب حسینی؛ عالی بود از دست ندید.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31090" target="_blank">📅 14:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31088">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIRydWWtI498Cwby2HCIz2d_f4qF70XbKVSLPdNILC23YoSnHXzrX4DyDaEZ0CVQ8D2_QGkvCY9bTlZInCbieSpuG0tD6ePi6yqSlz_33bL0vCypWPASV5RvGxivQozh6PItyLov0Q4-p-k3SitpSTVrslqFR1Q7tS__94yi9dPZTNU26eE2q3NhPiSNudyb1hRM1r7tLnA3Rnh9fJTgS7dj3s587_WEoSeB3Mju078KHmO7Bw8WsWchvsa6iH5_CyhJy9_wB-gb0ncWtHIml2mPLbbX6j9DRXbfbjZMKz-7GOpfTOiKBSQ2P2n1qy9QsJKbRd7azD7Leg6Rb0KLhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WoUct3kq_Xwdjci0yhZthkbdoaOabYtrb6PdR-uTnILEfBk3nVHsY2ufVPu2QNUv_jHfkMilfEj6aqpNLhSWiw_uOkPsZ1uxx4-bGiZAYaYwI1drzJ1bV5cLZBLHSokgy4eb7ZiCwzE4QI-cLu4MR3SMlE876difWDLRpSdL5cS-BNllJtZHwVukY8YusOc8lYxDkDwKqYG572-DgYyCVwjEayKuGCxRGjaQUbLnpR8HghVphKvonxL9yUFzxB88QaQFcRboo_204R8cngCj47wSZ2p6j-4W63Jd2wjicIy4Q8TJJ10uF54HNpT6ACew2YN_ekBlMuwTNtRDQS9ORQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31088" target="_blank">📅 14:24 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31087">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh5lbOj29r6XjsN-A1z6nw5xgVPM2qo7CmpscwORl0nSuR1giK0kA_qmUSq3CDSrbKpd2j7eRraATgHPohCs16yu-LcQHrcSxu4Txjh8nJhkMQ87V14sBW1mJWKsOBKbF5ymzOE9LRIY-kIN8qYC5hHEDZHQQxObeAhZocEe0WSQFWTsW2dTSytaDpb2Yx7oweWkscaX2WgJ4-HzpKLZr6H_X-Trvu7nOxJTJznlz5qKjW8-N4GWc5b4DDpJTLZIEOKEGVI803rZAQgtvMqttOU4T6mSIrGI3SQi_AJe2rE0puBOCCuLykcpd8t9p_-HIbo1mL71Zr-4e1Yg9ByLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
مصدومیت حبیب فرعباسی دروازه‌بان تیم استقلال کامل برطرف شده و او هییچ مشکلی برای دیدار با تراکتور نخواهد داشت و با صلاحدید کادرفنی این تیم میتونه برای آبی‌پوشان‌پایتخت به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/31087" target="_blank">📅 14:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31085">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KLEe-KdeBPNZQ0L4b3n9dzLeBypLASJ_fA_IFOtcTekL3I8E7zAziH-IHl95YxYSCpSlEXLP-y4KM9fhW-7y2RIkw0LWpyVMwYXqOvm35pO-27rOzt3GmS-itL-n2VLZZsdtgoOCmywk9p0o4-_bTliWUGXKz8-RGUyMV-GWLzLdbDKsYijQQ52KqSkaMfhykH9yj29_1vpMKRnN-eb-MhTgoUwvHEX7ZJxgfxArnLzK0gqqffNQp8taBtQPUy_UPbluWE1bE0gWLVyvnY4w7QngFHfDTjkah2kRJYGQDJcWKCAGunkUv4KFKVe8mMPgSKMW8nI6kojw9bo-uKYtuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3b98YO7ifBUHNWpSlmZPs5EKYvpzH_Gjalhst6yz3ccXxVraI7RS6zuyPKE-8D43A6fJ5RLd0v8YfoKebFNhOymlcK0Fe517Jzyilp4KRnJvCiZylq8hc7jVFWNxRh4FjEo2RsmWrpAzJ3Thc09bZkn_U74li_-CBhp0GpoWI3pm44xFl2pVzZbEmtzrzH3YWDIgofT7ZZ44a7Me4WqW114pVZespmWTo0bVp9GHzyfHZ3BGyXeXjQQ0GB40l_jPUlnDefYR99YWyYEMzDguaIrHbt-8Fa1bUzGV3D-4IIp5yY-3Jjv8Y6e4tozCpeUBXaWFCpxCHeYxJ1afgYilA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج فوق ستاره برتر قرن بیست و یکم از نگاه هوش مصنوعی در دو قاره اروپا و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31085" target="_blank">📅 13:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31084">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JidrmvvekMB-OTLIhyVXuSCQ766OE4ncf_Gn5NZS_ew_pMZDRsTY17dG972aoEVDM35jZck9p00th4BPDV3CsIcxJ_uWwnbrGS7Qqg7A-ID71j6auCPYt2WCvetXEmTD-CnCMA3Do6qZGB1ay83Rq1Tvz2c6mimHbhglLycreJtSB63-Q8vFlFjPweJEIdn4zlQFFBO_pEsHJ8GnVHoVvTWVQs_6x-_lIWI-SCvQXqhgx_qGliZnABx0lSsm3xNzEB4AJu6jZyW04xs4Y_aaK_mcsI1rwadvVTuE-xNORVk_qhwDzsnkLvZl1uDGJffHcfCxYWy4wbI0akdQ3wu3tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام وکیل امیر تتلو؛ دادسرای تهران حکم به آزادی امیر تتلو صادرکرد و او بزودی آزاد خواهد شد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/31084" target="_blank">📅 13:22 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31083">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRHle9fmwHC5Sp_pb9DcENU5BpxPcnrYRpJ_pwn3rMhl3E6oTgz5F2GbBly2_13_4_v_P7yferCMNqJMKD7DDM2wSoat2naQtiaQnmIaKLOC6wCRrSiXqknb5Zpw6fa0zngpg4VH5oEm_hRW5zysT-oz8D6fHdSOF8WVgTopiMnxm_HcKCHL7t2bnM_wHS_8e_oZY0nWqVuYSS5oJSfre0KA2F-fMRWjnoUwabVNf0-g68tsV5b-he01WHvzbUodGxtQLkCYVYOzdvjBmP5LhbH-Csg2RFPVYIWqmIR_UntZ_yyn14gL3XZ0cGld1pMofokwLETx37BaGAE3hd9eCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌امتیاز تیم‌لیگ‌دویی پادیاب خلخال روخرید و از این‌به‌بعد با نام پرسپولیس B در رقابت‌های لیگ دو کشور حاضر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31083" target="_blank">📅 12:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31082">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2ImDjb8_ucheyfEQcZV7Edr3Hi6bqY4yqerMCnmlBMg8c6OVRHyZoM7xxR5doTNoEjg2BBh2TZGxw43IHCo50jvrl_y8UT1gG-95TpeQ14LZopDC8dsBHFfK63lhLHcHPqiEtha3lKAOkvJQ4TJr9Gdn5W3qwRojXzTuzV-fKGy-7YWXb_H7DP9WTtsWp77V7X-Hek0GCZ2VeeCc-iHDQxYYh3ng8ZWOzxeMRhPwqoz9MmEsakd6DpPpbm_1H9g7DrcI4ILrPWXeLbz8lF38R9pyjyOcUwWReOsV8mOCn8RWyJAIc-Ys3H-Q0Ve3AXyBeM8pbu6OVgGKchvSRiUKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ تمام‌خانواده لیونل‌مسی درمراسم خداحافظی او حضور خواهند داشت نه تنها همسر و فرزندانش‌بلکه‌برادران‌خواهر و مادر و اقوام‌ دیگرش نیز حضور خواهندداشت قراره‌این‌مراسم به یکی از بزرگترین خدافظی های تاریخ فوتبال تبدیل شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31082" target="_blank">📅 12:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31081">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=bKyH0cVaPcvUCQN1CCeEsCwzZ6tlhH7yTR1Ksu8VIaQv4ZjEmxl1tA2nu6kCAaX0SWLiY9uQdyHTlrC-HhZ-YIqAXYUElX0pukYj-eaqJO2kO0mPP9GvpjyivtzoiNlNlVIsLO5dz7_USVbvzsHtrPHCEVvcy-KPfX4NPc2pax24i1iUmQ2o0dO8M6ncEX150Y0fo6d1DzxZS35Gw_1XMz7P9zoc8_eYZc7eLvc_QS79jmDWMaLW_ajwJTYr8A1xj-psdifjbUxyVnoTj3ehCRK1Cwi19TVOkoex0sQ9T8SfeTouT2P9wrvxDuf5R6ONXXApKkYe1WoHwplksxRwbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed844901.mp4?token=bKyH0cVaPcvUCQN1CCeEsCwzZ6tlhH7yTR1Ksu8VIaQv4ZjEmxl1tA2nu6kCAaX0SWLiY9uQdyHTlrC-HhZ-YIqAXYUElX0pukYj-eaqJO2kO0mPP9GvpjyivtzoiNlNlVIsLO5dz7_USVbvzsHtrPHCEVvcy-KPfX4NPc2pax24i1iUmQ2o0dO8M6ncEX150Y0fo6d1DzxZS35Gw_1XMz7P9zoc8_eYZc7eLvc_QS79jmDWMaLW_ajwJTYr8A1xj-psdifjbUxyVnoTj3ehCRK1Cwi19TVOkoex0sQ9T8SfeTouT2P9wrvxDuf5R6ONXXApKkYe1WoHwplksxRwbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظاتی فوق رمانتیک و شبه هندی در شبکه سه؛ روبوسی های واعظ آشتیانی و علی خطیر در پخش زنده؛ قبلش داشتن هم دیگه رو پاره میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31081" target="_blank">📅 11:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31080">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeVVw2Jx8K91wsj8sr4UJiltWpTS1DbB86y0Xhu1N3IB_3_vbBxhyow_OXKwyyN_suG0pjZo_ZiPlcv0IsEd5GeMHbvgQrplcBZHSURiUSTVsEZx4w1bBX9HkvctMTBbq9kGsE46j32_dkBotkJ4pz1HAYXZilH-wM08AyVfimwiN-3Z1KUzmXzdQe2kNNxJ-OCEsj6fVbTMRvADuU4F_hbHYFIu906-hiu1RUMUKVYtDoguqSJ8Laa59JJDjl5ng2P5qr2KIJXC-HswuQadVlPg4NOkzQEoobg5lE7ys2VTK5nLCkxofKSDA4OsE9FGuX0MigCtrZZK8twV2wT4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31080" target="_blank">📅 11:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31079">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=sQEdAEop2eRdoE6fsdLshXbTXpHaS27XUzW7Fwbf8hK89NNV3xKB02mkwqTWGgUFchH9D2XU4-IJnyfAU0YHdtWAGJFSJV4nOlLIaeiuqyW0mVtHTxWmox_84gDVhB7u-LEysqIpqi7wSIrM2ofV2CMJ_amx0QlvkcXDwfMku55d7cjMNKuugEcN6qc9OLaqZ9JKp8U6vqKeB_0Gla8MN4rdmxnktVoJzn5clMGAkQYjp1yKFZYZWe2o0JpXwNhGcoxYOPH4I1BJVRkzoHcfGXPdXxAZ1gA17bMCEyrFNH3j66WAn03yMYR1ggts0OJhpDR200RcyurdyKQ_OY7CDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e2faae04.mp4?token=sQEdAEop2eRdoE6fsdLshXbTXpHaS27XUzW7Fwbf8hK89NNV3xKB02mkwqTWGgUFchH9D2XU4-IJnyfAU0YHdtWAGJFSJV4nOlLIaeiuqyW0mVtHTxWmox_84gDVhB7u-LEysqIpqi7wSIrM2ofV2CMJ_amx0QlvkcXDwfMku55d7cjMNKuugEcN6qc9OLaqZ9JKp8U6vqKeB_0Gla8MN4rdmxnktVoJzn5clMGAkQYjp1yKFZYZWe2o0JpXwNhGcoxYOPH4I1BJVRkzoHcfGXPdXxAZ1gA17bMCEyrFNH3j66WAn03yMYR1ggts0OJhpDR200RcyurdyKQ_OY7CDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
25 سال پیش در چنین روزی؛
دیوید بکهام با این کاشته‌ تماشایی در وقت‌های‌اضافی‌تیم‌ملی انگلیس رو با اون همه ستاره و اسکواد خفن به جام جهانی برد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/31079" target="_blank">📅 11:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31078">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soxTZ03ttM3JZ2he3HR4wiseoeirRAwoOLDIGRafcZ9WtihKzBr9eeuUGXbfZn6yp0nUAbmCKRClke2kIbmJwHSKP5iM-i_jqGXXl3A6vcTquFb7-D2oaH5Bd4rkXWeyL8xlc1uqjFcwlldia_QDMPuqELgFh9_8GabQKgjUbwdJvg9tS_Ws912klCmI2LHpCgiY3XhScSpLwkMLF2lQQ58iVQw88JZTWRw9qgtKkHBSFH_Vg6b2fOOVKwNPeKnFgWrnVkhpae5Mien1FmQ_q2nqMPhXJc0mTiuxsbn-Ln_l7OW0iohhqkHWwx2SO_LMsNl5lwwWvGFVapL6YLvG8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛ وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31078" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31077">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=tkMoEAYAA6myxvHgWL4d4EIkxekVezpGkftCnYwrG6iAv8ziZArpP7Q8zQLecEcrgIyI8Nv5H-3qkq_5UJ2yl663swG0vdG4CsOyf92IDd07b4fTi-6ofH9SHxwn7b9tjkvI2VjXMFRtWMQxVbj7hWp0vPKBoNWSGi3Y4zhX_i4taaKBKaLLXegRoMTi8Xz6SZhE60ip3zDpMdiiSSNvnqRKF784WaYrzTGDMBp-tdDueF0s08euxGWPCwNsMd9pbf-co0C9mBR3ZwACjHFXVFSGYQ2XsicfdL8lV_9JKDPOS7Cdk-3cTtXJigp8GtwrARHdmHR2HELKvhA60ByQzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb0144545d.mp4?token=tkMoEAYAA6myxvHgWL4d4EIkxekVezpGkftCnYwrG6iAv8ziZArpP7Q8zQLecEcrgIyI8Nv5H-3qkq_5UJ2yl663swG0vdG4CsOyf92IDd07b4fTi-6ofH9SHxwn7b9tjkvI2VjXMFRtWMQxVbj7hWp0vPKBoNWSGi3Y4zhX_i4taaKBKaLLXegRoMTi8Xz6SZhE60ip3zDpMdiiSSNvnqRKF784WaYrzTGDMBp-tdDueF0s08euxGWPCwNsMd9pbf-co0C9mBR3ZwACjHFXVFSGYQ2XsicfdL8lV_9JKDPOS7Cdk-3cTtXJigp8GtwrARHdmHR2HELKvhA60ByQzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک دقیقه از سوپر گل‌ های چیپ و تماشایی در مستطیل سبزروی هنرنمایی فوق ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/31077" target="_blank">📅 10:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31075">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEEu5vSw8teuarmedBsUOfX_eez6WSAy5R7tsUZ6B-UlEPaskYz1NyOuR0PHngEN4xCwzWB_FedcJ_Xkbj_TSYPRlMpTMBzeMfxpuGaE7kLwzTezrf3LM8r70exxmuFKEkg3_gG0Ujl1qE0jFAn3lXSDuIM6hncRmZIGrWC2nauWMNbBtzfGN8IA7Q_KliAC6qmghr-oPSemvMPKgvGhYqtxmanDot7MnLFLHHy6usS0GVZWOMdyoHReaILDmAfriXCmdQMWVuzyszIVqGCzNUq0bqhVlcpVhjF8rOE_4X9bhpbWXMhBmsrN9DfgTgqW6_Bi6xvaGImRbfSiK_aa2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
خبر خوش برای هواداران بارسلونا؛ با اعلام دکو مدیرورزشی‌آبی‌اناری‌ها؛ این‌باشگاه با رافینیا دیاز فوق‌ستاره‌برزیلی‌خود برای تمدید قراردادش به مدت چهار سال دیگه به توافق کامل و نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31075" target="_blank">📅 10:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31074">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjlZxSCYPjaGS6_CKwhLv9jyTW-bdkJ-AJN0YqAZkOB8UF4SRPA_WTiYz6qaZevanb205EZjnw7U8xKaMWaTEsGo5YSkds0Rv3BlswK240dlsyC9QyucJ3HgPRlJ-icqKXflHn_6fy3JrNQrqSnbLzZjkSNy2S4PHj_u61Zyj0Q9Lo7ziZcK5ZVt5NvrErzstmuuBXqGItQ_p6fzfDnJFHk-N7sL3vY4k0SwgmPCUPNRUXZEzVNupDYbdEoq5ic7tu6h0Rh5kBG7nvohiXygdiaW_bvscMgrr-6_XhEUnCG8IyLMfOPYaM9ZpDE2YgLExZthKF0vymzwALVOYkozSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسامی داوران هفته هشتم لیگ؛
وحید کاظمی داور مسابقه تراکتور
🆚
استقلال شد. احمد محمدی مسابقه پرسپولیس
🆚
صنعت نفت رو سوت میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31074" target="_blank">📅 10:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31072">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZvCzGNJz7NkUfr4k7yP3NQeEfJYPFNa8zSnLs9OS1IIg54ZHCkU53229rCqUhz3wsEffwn29Cem77q7RksFdkON2o9_TI1OCiPGMm72DMZ_h494kqOSPYqKrjtpd9oPEJu6ADPCRvWuYN8xBFfAcaVoMNq-KYUGdj7t16T4MraKiq_FBnPa60Oj88QVO_ucfMG7svPtkYnjX6W_2C1X1b3y5pm7h1Ecg_faiCrtK9-tzvPRsRRdupJjo2-wsINrM4b2hCMrd5IM_gVjkYCs-k0CGi0NynXvoe6Qx3zgGJobI8BSq4X24SSa52yM_59fd6F9NqQ8EKo1QlJLUz4t8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ot3o0VP1vPvKJv3EhjDk9DyI2e6TFdx3oTIUlUBFAual1rGAixQ8qgVJxZpklKJvuidwQkQxnwEvm7C6KhLpElUPRM053mbF7ig7wuTVSJJdICeiNaNnhoWXzhazc80bMqvWQuAos_U2VO4YooKTakmjYjH_TdXd7Tkx6LzutAigSgLJfHr9gvm5y7fjzynghYoZEa5PUpM2fVbiFEJACqADqQ_XJxdSa5-dZReYGCBEeuali-o4OucXTAz3CDQ-_52oJ5kLkn1aLQTUvcJhcePg4tZBiSV0lyEbyW_E07SbupcT4Yz_oeyzZGK7HBBJ3rnVLwBPTOGy78MAP24vMw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
👤
سنگ تموم پپ گواردیولا برای لیونل مسی: تنهاجایی که ۶ اکتبرخواهم‌بود آرژانتینه تا در مراسم خداحافظی مسی شرکت کنم. من به مسی مدیونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31072" target="_blank">📅 10:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=T97WHBmyI8ZuTW5x9J9FPi7J9QWF6IPTHPVl2AHiLWxLmvku5C3Ta0M-nCRu8VhjAFOXGScCNv8cjC76AddxedSxaqPXwDDN2SrKmepRpvfi-ZinxkYrcvbmgl2kZN01F1yUlv3d_xDeAs2ROEs_b2EF2VXlZH8P0zHWa4R1ToWikb6PGPtp9eXQrQud7SpBUwrRJKM7Lfhp782zPrtK5bRRpVS2HTQ4J99G-rQzgfXiD-0wi14WkZF3EbO8QZ-H48YzGG_tb83Xuks3MOFmjLZECilFAAcRVECv-BgxrmTTC-qLO_PTnsOq3CuzisTgEhxghC7j_Vs_sWxtb0hg3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10ac8f2e13.mp4?token=T97WHBmyI8ZuTW5x9J9FPi7J9QWF6IPTHPVl2AHiLWxLmvku5C3Ta0M-nCRu8VhjAFOXGScCNv8cjC76AddxedSxaqPXwDDN2SrKmepRpvfi-ZinxkYrcvbmgl2kZN01F1yUlv3d_xDeAs2ROEs_b2EF2VXlZH8P0zHWa4R1ToWikb6PGPtp9eXQrQud7SpBUwrRJKM7Lfhp782zPrtK5bRRpVS2HTQ4J99G-rQzgfXiD-0wi14WkZF3EbO8QZ-H48YzGG_tb83Xuks3MOFmjLZECilFAAcRVECv-BgxrmTTC-qLO_PTnsOq3CuzisTgEhxghC7j_Vs_sWxtb0hg3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌ های‌ سنگین‌ و جنجالی ابوطالب‌ حسینی‌ به هادی چوپان
؛ هانی رامبد دیگه‌بهت برنامه تمرین نمیده؟ ایرادی نداره بیا خودم بهت برنامه بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/31071" target="_blank">📅 09:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31069">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xg5eB4TgMXmGlE_8Eyd7ym-92pCo8jzYiSSe8N6M5JbLVrSYCYcwhhIhTTB1e7XyJo9gy5KstkILfmD0B4PP7im0K1Fr0UPoZxcRBhMC7cyOggXq7v2fmJ7ie0OfVwldO-NGmFlYTzLzScXy_0jV_polI0Dd3qJfNeqE3Vn38IzKGNVZb-2Q5pGcerBJGPCGi-co8Fi6lC8m5DJ6rP3YFWNVdxuAGM_q7q5daNEYJc4LmlQYeaPB6LHltaH6F8sEToiw1Xy5pAOYW6dgl6BDbcXeUrWfKK5ZGQ1J1EcaBYYg9yFU4yNnNFug8sfBdlyuGdn4VlPeKau0NQRF3KhPkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
جالبه‌بدونیدکه؛ سال 2013 تیم رئال مادرید میخواست تونی کروس رو از بایرن مونیخ بگیره که مخالفت شد اما سال بعدش این انتقال انجام شد.
‼️
سال 2020 کهکشانی‌ ها باز هم خواستن داوید آلابا رو از باواریایی‌هابگیرند که‌مخالفت شد اما سال بعدش قطعی شد. سال2026سران…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31069" target="_blank">📅 09:35 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31068">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIdP_ali26EVs6_z_WSn4G2gEr5rqJIPSSP2PnPzAdP4IKnsYAtyd-qLPS6V5gImayZyGOuCNi1pbNUzjhowlMa9FKc13j_lU9YsPG2vLV1kCCWk9CRHoycrHIDlz6VyKZU_UnyR4uj0fY07ZCo7Kab4E-XcJzCihRI2MhlJa88Q10Lbc5AxMKzFEhVm_MfK3-2NxUPPEVnwIrG6Ldu4ocx0EfBl5K0V01MMd609KhxeFwS8gWy2o4ZV7KOAVXxpzP6DYET2icen_tEyMSvILWGe3fM18aAgCI3jh55wgCVwIQUihHfIRFre8G_Y43dXcRrGe_2rC4T8E-4zK0L4IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛نشریه‌بیلد: باشگاه بایرن مونیخ امادگی خود را برای‌ تمدیدقرارداد مایکل اولیسه همراه با بند فسخ200میلیون‌یورویی‌اعلام کرده. سران باواریایی‌ ها حاضر نیستند با رقم زیر 200 میلیون یورو فوق ستاره فرانسوی خود را بفروشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31068" target="_blank">📅 09:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31066">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zm7A4SeFQFuzbe_VyVU8F2tNz9DErQ7EZbCijU5s9noqYOqbMwf8RkvwdRijswWBVOrn2pqpTz4-kPYSrd6nwrXtrhNbcKEM45wq5SdpmL65FNplDFoyoD5q900y8V9lgc3nL9-mSi-EAzKlWEWSos5UAe1yQeamO2YQ5JqkZAiRs18dfTHPeU3o0C-kjWi4ditVJ0AM6me9LdzkthQNxQ0i5KbnzkXcFEVsGw_cQT47ZLvlp1p3UfERCpqx7Zi1mljQFNB9Df4jB_YUZZnirfyRhLVWzyGusCvq3FeQGJ9abpDvI7l2CszcV5EHA5AeFH-PpP7e4u7VKccLPeF2rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84daabae54.mp4?token=noj8xb0Qowy9-nIcFVnIEj2xHpK1QM44y569pUqYfcRaHpc6DHyuX2rCBFZ4hTloErgnaXsnb6OPRY59YnFbAkWb5y--s2mY8hFcdiYW2IuRV6BMkJbHNrG4mI72VmIjKzsUxqaIqVNJkGH8nku7ceInTjbU1GIIxmU-_MTdEXJ-JhhLyVQNIV0XMEL4JaPk3CMwuAktDqekp6DA4B2Kwc5oes_lxECK_h43b_vhfLikjI5q4w4ZFUrVQXHdyVcF-tZlYiQ3hS2oN--qD6oZ6JzxW1vwYJO39Rarip-8d576Y9KSm9w30t3ldN-tTOX9uZxa-iXtW6eUcz4phciXFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84daabae54.mp4?token=noj8xb0Qowy9-nIcFVnIEj2xHpK1QM44y569pUqYfcRaHpc6DHyuX2rCBFZ4hTloErgnaXsnb6OPRY59YnFbAkWb5y--s2mY8hFcdiYW2IuRV6BMkJbHNrG4mI72VmIjKzsUxqaIqVNJkGH8nku7ceInTjbU1GIIxmU-_MTdEXJ-JhhLyVQNIV0XMEL4JaPk3CMwuAktDqekp6DA4B2Kwc5oes_lxECK_h43b_vhfLikjI5q4w4ZFUrVQXHdyVcF-tZlYiQ3hS2oN--qD6oZ6JzxW1vwYJO39Rarip-8d576Y9KSm9w30t3ldN-tTOX9uZxa-iXtW6eUcz4phciXFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
گل‌های دیدار امشب دوتیم فرانسه
🆚
بلژیک و دیدار ایتالیا
🆚
ترکیه در لیگ ملت‌های اروپا
👤
شروع‌فوق‌العاده زین الدین زیدان با فرانسه: چهار مسابقه، سه پیروزی، 1 مساوی، 0 باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31066" target="_blank">📅 09:06 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31064">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aeEaPBgR0vHIpNVzvD1TDb7yiCSWcCTFN0CnI2xcH5UW2izuAVAmPa0ioYff8FEF_kHstWHVptcqW77ugCIWQqorBHhg2V7jX_N2_nx1lcDZ3vKpQlTbUgi6fRdHgZ2KJa-qthDB3aQq4cp84KLZUsa981AlceZ4ZEONLpHsyDFl-Zwpm36t10PO_qi8goQJ2Xkan0SwPToV228RTIwJZK1A-MqYTuzpx1L4tMmPotxQET3ptAddJF9t7ZRCzZrJlV0T8571E-l-7ZfKJh32NFY55mrED68_zKns1I_TPcoVmAthpFvMkCiQVTTslIpdTEYVVzGUkp0v85WySFpfOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برد چهارگله خروس‌ها مقابل بلژیک و دومین برد ایتالیایی‌ها با مانچینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31064" target="_blank">📅 08:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31063">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j8hRfCV8RJ61C_MgqoBbxqx88SoyiMUl6FZbT2mzUTBmtZuH2adYryttzeKDB3c2ZHlq7KIqGX-0az19jwTijBobbvhoDmQnCCdwOVRyJTYhFS0yZ3RYSIsnCklM32DlqS2B6hDPTFRrPddjSSFrd7d_TntcmJ-p0sJ_hYVgj95AR9KzXGMtNsp2l3Kf9P9MZevP-dTDkKYBMMFpaB9mn_4UtLk8FaxnBkqUDHLBYlHPi7Zpkf1jdD72kmdigXC3dDbsIqClMFRRAHjWPQ2Ry8T4h3LfAXq3A0o9zSOp1NzgqDRkq52lZ034U82pUuGXRmkylnYXQXH0-jacaP1tuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدار ها‌ی‌‌‌‌‌‌‌‌ امروز
؛ جدال خانگی کروات‌ها با اسپانیای دلافوئنته پس از تحقیر مقابل انگلیس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31063" target="_blank">📅 08:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31062">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=kXNHl1JpZPDITMRM3mNTO0uszldWp514ljuvfGPz2o08HnR4WEfhx8JJWJ8G5SN38FUDGfqx2uSFkJtfBaFSF4tqILS2kWxXuOyhdZIwhKgrJekTm6X6FkZeGaDaOc9VTQONacu0zZcwEwidLsdPp5D2M-Wx6pkZNCc49lYdLTtHSdXS82_5JKOCB8pyf1HcUsNWfTfXLSNZj3DGR9G0sMhjrT-8hkr90C_UTmluJi-TzWcyxDx1l4458dj23_snIFVuC-7jjVmASDHW6n54fdQfzYsxQShilIlyDEmUy0hBaSlIknKkkFIcv37l_gpCHkeaaQcePnE8c0Q4r1EvMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e146e3bea.mp4?token=kXNHl1JpZPDITMRM3mNTO0uszldWp514ljuvfGPz2o08HnR4WEfhx8JJWJ8G5SN38FUDGfqx2uSFkJtfBaFSF4tqILS2kWxXuOyhdZIwhKgrJekTm6X6FkZeGaDaOc9VTQONacu0zZcwEwidLsdPp5D2M-Wx6pkZNCc49lYdLTtHSdXS82_5JKOCB8pyf1HcUsNWfTfXLSNZj3DGR9G0sMhjrT-8hkr90C_UTmluJi-TzWcyxDx1l4458dj23_snIFVuC-7jjVmASDHW6n54fdQfzYsxQShilIlyDEmUy0hBaSlIknKkkFIcv37l_gpCHkeaaQcePnE8c0Q4r1EvMYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه‌استقلال‌خطاب‌به‌فدراسیون‌فوتبال: شما جام قهرمانی فصل‌گذشته لیگ‌برتر رو به ما بدهید ما خودمون نمادین اون روتقدیم شهدای میناب میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/31062" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31061">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=am4rZPz16e3em6mTWNb4ejMd52AIp5bumHgIKdmb3DuLzOsYAql6pKU8n4iO3-kEDd_P4_c4mGuQWIXO-aG-ApseuDog9GifqGMJvW9NKDn_5Y4SSt_a8gr549M9zKjnA8V1lHMZZkzwPqNdRtuZt2GXmc4949gY6JWUBXeCABLl4VhwuBBEt2NZ2il9TCYGS6dEARxIMZRd60O2w58seue9lTPNjKurmbp1jEHb5whysRot5y2oIWy55GSsktvf8WCj2mtdAA0g2B0vQL2awQKvyUIq7pHbR0iIo9Ya18hvpcnFj-gfQWugsOlf3dI5TVD0symd4WGrQFWokuIdyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612b743bd9.mp4?token=am4rZPz16e3em6mTWNb4ejMd52AIp5bumHgIKdmb3DuLzOsYAql6pKU8n4iO3-kEDd_P4_c4mGuQWIXO-aG-ApseuDog9GifqGMJvW9NKDn_5Y4SSt_a8gr549M9zKjnA8V1lHMZZkzwPqNdRtuZt2GXmc4949gY6JWUBXeCABLl4VhwuBBEt2NZ2il9TCYGS6dEARxIMZRd60O2w58seue9lTPNjKurmbp1jEHb5whysRot5y2oIWy55GSsktvf8WCj2mtdAA0g2B0vQL2awQKvyUIq7pHbR0iIo9Ya18hvpcnFj-gfQWugsOlf3dI5TVD0symd4WGrQFWokuIdyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیو کامل برنامه امشب عادل فردوسی پور با برسی اتفاقات اخیر فوتبال ایران برای دوستانی که علاقمند هستند برنامه رو کامل تماشا کنند.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31061" target="_blank">📅 02:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31059">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_sW4pCPMrW1tVNWCrPaNrRMJzd9gaSh8HYB15N6G3ncnWm2t1yevwNnqjnRmqld1pclEyE4Fx3L-tbd-E91RxDundnX4sJImKeVl_QTnblMkbBAEMhDtbPUph4EXZ3s0dyPWmt2Wl4MQ7C8NG1YtenJd0drs3cThsSJuQztGyrm7LxL4Z-5OAIXn3kmQA9a6-2Tst2rEOJb0Ovmg5JdwJGcCAkuOryIrAxdyzha0E8CCTUYIZWs83x64FXqO2EpwS1_nz1m7wZFqC7pUvgxqxMrOCjLQzhw64GBHLo-OmOowtoViLunEBmMWWTD12BPGkD4Juycdnmm9OjUdHd9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روماریو:
امروزه مد شده به فوتبالیست‌ها میگن بهتره شبِ قبل بازی رابطه جنسی نداشته باشید ولی من باهاش‌موافق‌نیستم. من‌شب قبل بازی با همسرم میخوابیدم، صبح هم که بیدار میشدم دوباره باهاش میخوابیدم، آدم باید تو زمین احساس سبکی کنه. به بازیکنان توصیه میکنم این حرکت رو بزنند معجزهه میکنه. دو راند نیم ساعته قبل هر بازی توصیه منه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/31059" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31058">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1edc763594.mp4?token=NyQ9Q4fERpbcMy1bIO2Pe0x2WwG_YxLDoGRQHco5ztYJE9KYbmeT5hODWlIfIxzoh4fSFPOZOslvz-wdzPDrxy5t9Z97tqW7JZ_6K7gWJOZWJDfeY_xWmB0pRCGs8sDW1s3HG9UV0vYTKHSpxggMpXzpmD50o_hvCFI7ObLSK8k_LsFpbLpBFTjU3NBxFppmXOX85hgruO5v5-wJAS-s1LbTVrnKj-R5cQ89zJsg1a7ASr02-I8yAGdz4dQWQIHcep8Hetjmx-bJ3GMyBZ4vjBweOFE6Bwsc35Dwl0twY1RJvmiRYf0ST2axVhvL20dqq4DO86reE1MKHoePjvp9hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1edc763594.mp4?token=NyQ9Q4fERpbcMy1bIO2Pe0x2WwG_YxLDoGRQHco5ztYJE9KYbmeT5hODWlIfIxzoh4fSFPOZOslvz-wdzPDrxy5t9Z97tqW7JZ_6K7gWJOZWJDfeY_xWmB0pRCGs8sDW1s3HG9UV0vYTKHSpxggMpXzpmD50o_hvCFI7ObLSK8k_LsFpbLpBFTjU3NBxFppmXOX85hgruO5v5-wJAS-s1LbTVrnKj-R5cQ89zJsg1a7ASr02-I8yAGdz4dQWQIHcep8Hetjmx-bJ3GMyBZ4vjBweOFE6Bwsc35Dwl0twY1RJvmiRYf0ST2axVhvL20dqq4DO86reE1MKHoePjvp9hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ تیکه های سنگین عادل فردوسی پور به مجریان صداوسیما: توکه‌حامی قلعه نویی بودی. رنگ عوض نکن. حق انتقاد ازش رو نداری دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/31058" target="_blank">📅 00:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31056">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇪🇺
درهفته‌چهارم لیگ ملت‌های اروپا؛ شاگردان زین الدین زیدان باطعم‌کامبک‌مقابل‌بلژیک آتش بازی به پا کردند. ایتالیا هم بادرخشش کالافیوری ترکیه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/31056" target="_blank">📅 00:40 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
