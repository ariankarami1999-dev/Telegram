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
<img src="https://cdn4.telesco.pe/file/e6jl1dYsBZ9azK4PTMlG0qUNCGQ0njZ7HlM0oKxDhUrMXUwMpt50G8-4V5QwQ2UFpHcd2Gvpgw9E1-gMcman9ooMshQQumGURn1educ4WY4HuCGOOXd8YDpDBs1mNcznSCAQUw7WyUrc8B-RM7zHtBZEaLYFKnAVOLymFU26MD-fSQXV22aFwzCsWRz1xeFK1DmSV-9uT3owYeHUfQwM5iIwKSyghDSFM56Iwxnu6AmgV5kfLR0jm95-WyOKR9OVW3QqRQlzCrEIC_Dqaej5HOCpgvwk-PneUKFDXPFl00_dFWq2lzaHYSPxBM7rdS7IyQ9ih48DqJApWvYy3XO_eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 978K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 18:02:50</div>
<hr>

<div class="tg-post" id="msg-126834">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39fa6c3d78.mp4?token=pcukOUlPnaUdcqxKo3mHJNYJDy-XqP9ESfOq3nqnrLbn3odwoCijmnsV-gzyggak-TTdnqCyxJCkMVqilOOmQyNvkwhr6TcDUhWCEUaJ8SRi9hMmR3PsvoQDeW-f1v4uj9WPpjJ2vhMUIqewVO_jcdC3UpRgZtsZb-WWhXLFULIDcb2-JQQOaT1644lpv1Sac5VSATSeAEzssg5WwQILOn6kw2ekmQxn1Y6mJqCf7pXANc5Akn3q01WOPv0EgGW796Q76QO6T616Y5RjUe75q-jtA9FtZzb5dnuleC6sBCyehzaPAl7N33rJhiMmNP-LF831lr2oFbH5zdT9Xaxo2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39fa6c3d78.mp4?token=pcukOUlPnaUdcqxKo3mHJNYJDy-XqP9ESfOq3nqnrLbn3odwoCijmnsV-gzyggak-TTdnqCyxJCkMVqilOOmQyNvkwhr6TcDUhWCEUaJ8SRi9hMmR3PsvoQDeW-f1v4uj9WPpjJ2vhMUIqewVO_jcdC3UpRgZtsZb-WWhXLFULIDcb2-JQQOaT1644lpv1Sac5VSATSeAEzssg5WwQILOn6kw2ekmQxn1Y6mJqCf7pXANc5Akn3q01WOPv0EgGW796Q76QO6T616Y5RjUe75q-jtA9FtZzb5dnuleC6sBCyehzaPAl7N33rJhiMmNP-LF831lr2oFbH5zdT9Xaxo2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دی ونس: در حال حاضر، احساس می‌کنم که ما در موقعیتی هستیم که بتوانیم توافقی به نفع اقتصاد ایالات متحده به دست آوریم و واقعاً به مسئله هسته‌ای ایران بپردازیم — نه فقط اکنون، نه فقط در زمانی که دونالد ترامپ رئیس‌جمهور است، بلکه برای بلندمدت.
🔴
تا جایی که فرزندانم وقتی بزرگ شدند بتوانند بگویند ایران سلاح هسته‌ای نخواهد داشت.
🔴
این هدف سیاست است و فکر می‌کنم ما بسیار به رسیدن به این هدف نزدیکیم، اما هنوز کارهایی برای انجام دادن داریم و به انجام آن ادامه خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/126834" target="_blank">📅 18:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126833">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
هم اکنون حمله پهپادی حزب الله به شمال اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/126833" target="_blank">📅 17:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126832">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
فوری /  ترامپ اعلام کرد امروز ساعت ۵:۳۰ عصر به وقت شرق آمریکا، در یک سخنرانی اضطراری با مردم و رسانه‌ها صحبت خواهد کرد.
🔴
جزئیات و محورهای این سخنرانی هنوز اعلام نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/126832" target="_blank">📅 17:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126831">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: پایگاه‌های فرامنطقه‌ای آمریکا رو هدف قرار خواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/126831" target="_blank">📅 17:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126830">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7CdQAkWUqLYUAimleIQRptdKwvKrk93LoLnov6FYMkAOOVHvx2TjtMZV2uF_1TXdi5mVAG7MtE1w6dGLFuNJNTxCwywZyAvpxqSZstHx2HaNP_iTGzbcredxZXib8xR90cDHf0OAnaEJhCLYFMFk5DPnybizPmlWheSXov-LMuQrqPx3PZLs43f4Fjr20LHgWmAoumSVwRRltchJHftEGp-7B_GWyE5dF-U35vckjUfER8UZmffiMnU6yJAM4vcA0042e5t0ek2f-wZyqf1oMWmWWdyWbiJP5mci2rgAn2GXdGDY39P8iQQAKpbkB3ULkS7LYfjMaB7zlRRoXZcnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت جهانی هر اونس طلا در معاملات امروز با ریزش ۱۲۳ دلاری حدود ۳ درصد کاهش پیدا کرد و به ۴۱۳۴ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/126830" target="_blank">📅 17:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126829">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/424a37ec4a.mp4?token=D0T7mHvn0LS6fg086y5IGLwQd0jBoblvL5bnkOvnKzS0LtjnzNA8XqjnTT8im3QyelZTu08haQKR0KOF1z_y_QwKrHjcvM1BDnBhufZQtV-0qttgWnxQPkbAT3a5D7YqHB2-Gm980PFhv993mr9_-tGgcxizHyLul5gQpm8Bcwk80IL-gr_6aWR-WKJCVVHz26dX2m5E3ukDIcxT6s7K_xQDFmEKMGd5ovhd5RNbTd9s8YKsail4z8Xe05es-0GnzF5tsYBmd7AHiPQSmY6mkizYhmKAHXcq3pttzyWSSBuTpQzj9-gjGju47gXe4pj3zFWD68eRUP92nazni8lnIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/424a37ec4a.mp4?token=D0T7mHvn0LS6fg086y5IGLwQd0jBoblvL5bnkOvnKzS0LtjnzNA8XqjnTT8im3QyelZTu08haQKR0KOF1z_y_QwKrHjcvM1BDnBhufZQtV-0qttgWnxQPkbAT3a5D7YqHB2-Gm980PFhv993mr9_-tGgcxizHyLul5gQpm8Bcwk80IL-gr_6aWR-WKJCVVHz26dX2m5E3ukDIcxT6s7K_xQDFmEKMGd5ovhd5RNbTd9s8YKsail4z8Xe05es-0GnzF5tsYBmd7AHiPQSmY6mkizYhmKAHXcq3pttzyWSSBuTpQzj9-gjGju47gXe4pj3zFWD68eRUP92nazni8lnIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عصبانیت کارشناس تلویزیون از صحبت های زیباکلام:
🔴
یک لعنتی در مورد رهبر شهید ما گفته «او دیگر نیست» بابا ما هنوز پیکر این آدم رو دفن نکردیم، چقدر شما رذلید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/126829" target="_blank">📅 17:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126828">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
معاون قوه قضاییه: خشخاش نکارید،ممنوعه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/126828" target="_blank">📅 17:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126827">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mCJEnnaHLWU5CfwqD7QTszNicl8MZo1htlNnK4i2SAmlaW1VU-n2D2xHTPjZ3lO92bgS-qwa0ANxzvua3yQMbStQy1HhQC1O_XEPPCl-ahoUltNh6p2yHLO_NcIVZqT21ulpr0n3Y2YKHkPsrZN0AGNWUhq2zbeOYJ6o3VUSh1PbmclAK_D7Rw0CDftPOIfpS-stCSaeTa4IQYxRAgUxwIdw3AcEQ17ha11-ukmVgk_NjKVygu36ycB62T4BqVrb_0g91DTXQK0OWrche3fhY78q5eP4-KIRoHez_3p4JHrMTQUorLQEvv_8yf66XI5dEK94TZ0iRJlUQ3Lq1vHmIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قشر تندرو دیگه رد دادن نوشته: غیرتی که ترامپ روی یدونه هلی کوپتر داشت کاش مسئولین روی رهبر شهیدمون داشتن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/126827" target="_blank">📅 17:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126826">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
تامیر موراگ خبرنگار کانال ۱۴ اسرائیل:
ترامپ همین الان توییت کرده که ایران برای توافقی که می‌توانست برایش عالی باشد، خیلی دیر مذاکره کرد و حالا باید بهای آن را بپردازد.
🔴
مشکل ترامپ این است که تهدیدهایش دیگر نه تنها در نگاه غربی‌ها، بلکه در چشم ایرانی‌ها نیز اعتبار خود را از دست داده است
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/126826" target="_blank">📅 17:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126825">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxT5GDdI9PZRB6NBSQh2dDBdu7VDoS_4XBW0dCv6kWcFBnoFjEuHeP7MZZuRartb2xPwJCBBn1JSbPdtKwSo-KoZQZDevYJXP3JkBBHOj85S-b6vTHvehIwmZF-NftVMmYSZwMon_shvcYmtH5xjccFNadj8iREbQXNWfMe7q2bHM7Uc4bI4aHh2LrPYyitK0HlPsj0d65mwRprG8PW7a7IA_0VI2osOf03i7MNtpLsyjG0Vd0jILSr5s06BKG0MzcHnR4_rCgX3ztwT7WA4rj4QBy8Co_9tnzkEesQFvYrPTWfjhul_oV94pcneF_C0OgHavgqW_hQoLds1ATk45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سفارت ایران تو ارمنستان اومده یه توییت زده که همزمان داره "باسن" ترامپ رو میدوزه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/126825" target="_blank">📅 17:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126824">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/S5BHr6twUlF1kEx6Iyc6VdYhGnnp2vOu-QC0RYrPQO_B8Yt0j8DKFIVbsu2WxhcI53nhFfsQuuLkeuMjysmdcnXQ75plhEKVPEeHkw4lN_wCywCDwD47bPePJ535R6zXrBPeW-b-oQ4hctaj_GfRavnLXRCZmY4bMwU1YfU6vp0xrXoFeF5LVqDQ31quIdj_9ObN6AWJDcnYR8EJ2nNVeJwBezwUw1yQ2GAzZJ37j8t3qrxro1UmZq-NAui4itwGM4qBA6j_LIJ5Zh7L8aQ7LzOFIGLRoG8lKjb4d83O8KpAW_GjszvGZBshQhHfKLgfsjRK3a0sV4jdFg6H9JocSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محسن زنگنه، عضو کمیسیون برنامه و بودجه:
ما باید حقیقت رو به مردم بگیم، در شدیدترین حالت جنگ با آمریکا هستیم. ما با بستن تنگه هرمز روی اقتصادشون فشار آوردیم و اونا هم با محاصره، واردات و صادرات مارو محدود کردن.
محاصره باعث کاهش درآمدهای نفتی و ارزی ما شده و به شدت با کسری بودجه مواجه شدیم.
با پایان جنگ دوباره درآمد های نفتی ما برمیگرده ولی تا اون موقع،
۳ ماه خیلی سخت رو پیش رو داریم!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/126824" target="_blank">📅 16:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
3 بمب افکن B52 آمریکایی در ساعات گذشته از آمریکا حرکت کرده و در بریتانیا فرود اومدن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126823" target="_blank">📅 16:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز: ایران فرصتی برای امضای توافق و زنده ماندن داشت‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/126822" target="_blank">📅 16:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز گفت: تهران مذاکرات صلح را به تعویق انداخت که در نهایت منجر به پیشرفت بسیار محدودی شد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126821" target="_blank">📅 16:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126820">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
فاکس نیوز به نقل از یک دیپلمات آگاه:
پس از رایزنی با ایالات متحده، مذاکره‌کنندگان قطری امروز صبح برای دیدار با ایرانی‌ها به تهران سفر کردن تا در تلاشی برای رفع اختلافات باقی‌مانده در فرآیند مذاکره باشن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126820" target="_blank">📅 16:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126819">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6201d48750.mp4?token=AU6FK-q4mGNUCPN285OyuqT_OVglV9Fp6N0LCFKHdRsiaq8EV6rQ_KsKoLieJvf51LnuEXrQJoaKBJ-cgdVgwfm2S9BjEtyVrPM812AbK8-b6fOKr2atpdkSoLQeVgG9rN3uQDoaZZr54ifAgawPFZ56EidiXKmRzuRALYtkcom63qo8zEEuoJxhT_g1dNUDzEGEUJcT7u4AMnacWvweF3qygJBOQxhNbqnqbEm0l9-qf8iazC0qrvT___fokGez08eRBbWloYnvRfPbeb09o4umGCVH0n5leGRyUy7d4PZej-ERfI29D6yNmhvAjWjZJMqO8kdridqWau0I3rhE6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6201d48750.mp4?token=AU6FK-q4mGNUCPN285OyuqT_OVglV9Fp6N0LCFKHdRsiaq8EV6rQ_KsKoLieJvf51LnuEXrQJoaKBJ-cgdVgwfm2S9BjEtyVrPM812AbK8-b6fOKr2atpdkSoLQeVgG9rN3uQDoaZZr54ifAgawPFZ56EidiXKmRzuRALYtkcom63qo8zEEuoJxhT_g1dNUDzEGEUJcT7u4AMnacWvweF3qygJBOQxhNbqnqbEm0l9-qf8iazC0qrvT___fokGez08eRBbWloYnvRfPbeb09o4umGCVH0n5leGRyUy7d4PZej-ERfI29D6yNmhvAjWjZJMqO8kdridqWau0I3rhE6IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صادق زیباکلام بخاطر این مصاحبه که گفته بود موشک‌ها فاجعه به بار میارن، بارداشت شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126819" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126818">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
رضا دالمن دانشجوی کارشناسی ارشد رشته مهندسی کامپیوتر دانشگاه صنعتی شریف به خاطر اویزون کردن عروسک یک موش و بدون هیچ دلیل خاصی از دانشگاه اخراج شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126818" target="_blank">📅 15:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126817">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
ترامپ در گفتگو با فاکس نیوز: بالگرد آپاچی AH-64 ارتش ایالات متحده که اوایل این هفته سقوط کرد، توسط یک پهپاد که بین دو خلبان خورده بود، مورد اصابت قرار گرفت.
🔴
با وجود آتش گرفتن و ایجاد گرمای شدید، پهپاد منفجر نشد و به خلبانان اجازه داد تا در دریا فرود اضطراری داشته باشند.
🔴
خدمه حدود دو ساعت بعد توسط یک شناور سطحی بدون سرنشین نیروی دریایی ایالات متحده نجات یافتند.
🔴
ترامپ زنده ماندن خلبانان را یک "معجزه" توصیف کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/126817" target="_blank">📅 15:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126816">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
معاون وزیر ارتباطات از بازگشت ۷۸ درصدی ترافیک اینترنت به شرایط پیش از محدودیت‌ها خبر داد و ابراز امیدواری کرد حداکثر طی دو هفته آینده وضعیت به طور کامل عادی شود. وی همچنین شایعه اعمال فیلترینگ جدید را تکذیب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/126816" target="_blank">📅 15:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126815">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGlBoa9zWRTuPMYMMUBHCVQhSVdfFZZgtMlqcarvWl6szyQ-Y0z1BNMsWCayRLn_4sUAK81y_MxCAIAj5WX4csuDS7QxTcjant6dzqkxw_0ZkyiwO_bCtgh0AmGh5MbetzNiEluLDw7ZPgc7ygsNeqWW1lfYTEPl6Rzn9X0UM7Cf5nxltXtIhqiS9gJ7f-fC4OZ3BAipm2yOnHnbo6doUiz6By6fFebWg_jNUTp05v-dPmj8XQISKzQIzn0blRyWYVlMugOje8rQNFXxn4pTq54c9lJtNtSXWctHdt3F1RbxaY_-SDqXcqUP-SDTjx_zTwcZzTvuWT5h_qwCQZ7CuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، عراق در حال تسریع روند بارگیری نفت در بندر اصلی خود و افزایش حجم صادرات از مبدأ خلیج فارس است. این تحرک تازه، جدیدترین نشانه از عزم تولیدکنندگان ارشد اوپک در این منطقه برای انتقال و عبور بشکه‌های بیشتر نفت از مسیر استراتژیک و حیاتی تنگه هرمز به شمار می‌رود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/126815" target="_blank">📅 15:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126814">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBYRjhF5uHaB0OgyoEXFEcoI3uJaoT5PqrkponvxXmSDCCwwgZo01XJDTeigF56b3lLK8JeTkXGVVzkh7WKUJYWGOrcexXZPcnTvXuI0YEHUfaItsaw4G0QvnPJtQi6HeN2M7eJ0_MxkcOTfCGvWzlgvUYpTX8OaDeUSCdimakPlfuIodht1m6EeSlV8pL1oGygraAFFG0W_-q0HnM72-GHJGz2-dDPPG3skWfHHWWvgaM-HWTQdueGHNZSx_5P5OklZadwuFth1Us4w10rssqPbWTSsn9lzCX2TMofoZqIemZy1G942E00NUM237E-dfWNzKqyZjtiEwSIjq016Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
هنوز داری گیگی 10...15 تومن میخری ، وقتی اینترنت کامل درست شده
😱
چون داری از واسطه تهیه میکنی
😍
تخفیف ویژه فقط گیگی 2t
با لینک ساب
🌟
با ضمانت و بهترین سرعت و کیفیت
☑️
نامحدود واقعی فقط 290t
⌛️
برای 200 نفر اول این تخفیف اعمال میشه ، سریع اقدام کنید که دیگه قرار نیست هزینه زیاد بابت وی پی ان بدید
👇
👇
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126814" target="_blank">📅 15:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126813">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ به فاکس نیوز : کارم با ایران تموم نشده؛ ما ۵۵٪ از چیزهایی رو که ایران در زمان آتش‌بس دوباره ساخته بود، نابود کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126813" target="_blank">📅 15:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126811">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
قطعنامه آمریکا علیه ایران که حمایت آلمان، فرانسه و انگلیس را نیز به همراه دارد، امروز در شورای حکام به رأی گذاشته می‌شود
🔴
در این سند از ایران خواسته شده درباره تأسیسات هسته‌ای بمباران‌شده و اورانیوم غنی‌شده آن‌ها به آژانس اطلاع‌رسانی کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126811" target="_blank">📅 15:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126810">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1151f8b5eb.mp4?token=PlN53bQ4gDlIvW1Vd8cF2-Zsk67Osw4UzxNoZxfdK3j1SfNbxcGZJwQRfIIv92lKj2MJT7Lq5ouJYxmVgZ253_GFyJF1-0F7wVXqW79NRehpCxBEzpCApLYb-OqgqREr85MnJ7gaFHrB9hestatbaMNOt4g7NkkcWcgm5J8c6R6A_QnUZCpdc7YPoSIqfcNivsZorRCdQUW41ruhp3EE_8eq_XrAmBQm6OnMJytyXGe_YYYrj8JLESzdYc_6L0lL9ppctB6L2LJ-v78RAHQXDGlr1SirusHCxVFRT6oBoGadnoctuIabgvDW0hqDdFfkvwZ_hkQaPKKkEPrDeTzVTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1151f8b5eb.mp4?token=PlN53bQ4gDlIvW1Vd8cF2-Zsk67Osw4UzxNoZxfdK3j1SfNbxcGZJwQRfIIv92lKj2MJT7Lq5ouJYxmVgZ253_GFyJF1-0F7wVXqW79NRehpCxBEzpCApLYb-OqgqREr85MnJ7gaFHrB9hestatbaMNOt4g7NkkcWcgm5J8c6R6A_QnUZCpdc7YPoSIqfcNivsZorRCdQUW41ruhp3EE_8eq_XrAmBQm6OnMJytyXGe_YYYrj8JLESzdYc_6L0lL9ppctB6L2LJ-v78RAHQXDGlr1SirusHCxVFRT6oBoGadnoctuIabgvDW0hqDdFfkvwZ_hkQaPKKkEPrDeTzVTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروی هوایی اسرائیل بین یساریه و سرفند داره لُبنان حملۀ می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126810" target="_blank">📅 15:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126809">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
یک منبع مطلع به i24NEWS می‌گوید:
رئیس‌جمهور ترامپ دیشب با نخست‌وزیر نتانیاهو صحبت کرد و او را در جریان حمله احتمالی امشب قرار داد.
🔴
این دو همچنین درباره موضوعات دیگری مرتبط با مذاکرات با ایران بحث کردند.
🔴
در آمریکا از وضعیت مذاکرات ناامید شده‌اند و صبرشان رو به پایان است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126809" target="_blank">📅 15:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126808">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFLids7k7TKZuRHoEXoFu4M0d-W002CHCDDIgg_a11w8j13Ov7Ket0QKoAowUxFXmaaF6agPhVG_bv2IwdZ4uNmcWSq9pFDaw82MPh_nuqsbEBLdWAU5bglBdvqxk61TpM-jUPNYs2x1gU4_un3L0ECG_JmpUVc_umEgbrU_Wt7PB6ohUnK0ZnUBQF6OEfCrtw7g89Y7mgw2bOYDizoItJdg2GIOlB8xYrNpFKgshvN89MGQQiXWzwdGPTp2GLTl_NFSUQQevqGNCTEyyBLSt4Zyzbmya0O92J3vZQQ_goanZaXY3kSRi6RMooCswpmdH5PNjksx854ADtQym51X1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیت هگست، وزیر جنگ آمریکا؛  پست ترامپ درباره رسانه‌های جعلی رو تو صفحه خودش پست کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/126808" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126807">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_c8vbtz0hAk4XseNHnfC_sG45oY0rjOKRs_stTrbL47lQHw_GsVcXAywvgRmwktDnrjJM9BwJm8icibh6w_FgEFRUSj35sDEMm0Udxnb92dxc5EqkwS6t4dYln8L4SwtMUAMi5I0lrKV7HKeKuVgxTZ9rfmUBLI2FkCFnATxxxQr2qU6yQ-blAf1QBA23vLeGTMtSIDWsjR5uxTrt-6QST_Gl2RtT8xpgYx4wMBtybao7CYyMD4fo12Q-hn0avq5sROT_1uGT8Q7bPZW5yBFuhHmNWj8Zol60Uyog502r421y1FKeMYnRJPsXgArljkcpxpo0JOQeD4yDOBnUU_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ ایالات متحده، امروز به پایگاه دریایی گوانتانامو در کوبا سفر خواهد کرد و پس از آن از فرماندهی مرکزی ایالات متحده (CENTCOM) در تامپا، فلوریدا و احتمالاً فرماندهی جنوبی ایالات متحده در دورال، فلوریدا بازدید خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126807" target="_blank">📅 15:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126806">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
نتانیاهو: اسرائیل به شدت علیه ایران و نمایندگانش که خاورمیانه و جهان را تهدید می‌کنند، به فعالیت خود ادامه خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126806" target="_blank">📅 15:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126805">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نفت صعودی شد: ۹۳.۲۶ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126805" target="_blank">📅 15:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126804">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
اسرائیل هیوم: وقت تمام شد مذاکرات شکست خورده و پاکستان از میانجیگری دست کشیده. ترامپ بعد از حادثه بالگرد و حملات دیشب بسیار عصبانی شده و میخواهد هرچه زودتر به جنگ باز گردد. پنتاگون طرح های حمله جدید راه به ترامپ گزارش داده و اسرائیل را نیز مطلع کرده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126804" target="_blank">📅 15:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126803">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
عراقچی: دشمن خطای محاسباتی کند، پاسخ سنگینی دریافت خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126803" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126802">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
افزایش قیمت نفت در پی سخنان ترامپ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126802" target="_blank">📅 15:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126801">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21ea4aa970.mp4?token=EmVHvAMRI4aQImUtGPwM_i2eEg_1W0r1wdzqQOYCqwrSebTp0SQ8tSUHuUef7uUSv-eRhU7cHKPTeb7stL6PrEAxVDF_Om4ACo5dsUH1lSds6weMGItTsZp_QsKg7hcVjqQjzKJ8KVGGXtBZ3v_ydOUrhy1MvKhpoFvD8LnTHY4KX_ZY-RgvVFQYHMfWn9l6JhC60depC7edJe9c_T_lAWK-v-mh0jI_jwSY5TFMMsJCdNTcShJBUpHkbjGNtNcyyI1zV-h3LVkODJXl7qWNJn7s77bjPFPVUH4KnqvNfaXrRYAauVoA7O6JcKFhnyPtQYbW5XUPe9ZVeDS91rPI8lD0Ke0ZgmGOESddTgKJ8SRjP42lTEZcM1bIq2e7BdH8DBkmjOutC1-AGNFF4TEuTmKHNxqrXNlKSjyA66nDAodRzBuDvESGRrOtSM2bjmm-npO7o9ZBPoboTfRIOoYjdrY5uFv0uQZUAycj6czHm0Q-Y5UWOYJ7vCoj5D0FhuPM2KLAzSF3D1hBCf9sqfb1eVKiSp5k2hRCElI7Ye7doRIK5LqRhozla77EPU0xxLi_wWsX3HfijyprIeEkERqQJNOpJ-nwGAaX0bufS_uv1r_NOgqG40gkQXyLZnbU19vGm2bEqBnHOiNKFwLsDJsuK-ZwyLPFFDHSj3Qs921BoQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21ea4aa970.mp4?token=EmVHvAMRI4aQImUtGPwM_i2eEg_1W0r1wdzqQOYCqwrSebTp0SQ8tSUHuUef7uUSv-eRhU7cHKPTeb7stL6PrEAxVDF_Om4ACo5dsUH1lSds6weMGItTsZp_QsKg7hcVjqQjzKJ8KVGGXtBZ3v_ydOUrhy1MvKhpoFvD8LnTHY4KX_ZY-RgvVFQYHMfWn9l6JhC60depC7edJe9c_T_lAWK-v-mh0jI_jwSY5TFMMsJCdNTcShJBUpHkbjGNtNcyyI1zV-h3LVkODJXl7qWNJn7s77bjPFPVUH4KnqvNfaXrRYAauVoA7O6JcKFhnyPtQYbW5XUPe9ZVeDS91rPI8lD0Ke0ZgmGOESddTgKJ8SRjP42lTEZcM1bIq2e7BdH8DBkmjOutC1-AGNFF4TEuTmKHNxqrXNlKSjyA66nDAodRzBuDvESGRrOtSM2bjmm-npO7o9ZBPoboTfRIOoYjdrY5uFv0uQZUAycj6czHm0Q-Y5UWOYJ7vCoj5D0FhuPM2KLAzSF3D1hBCf9sqfb1eVKiSp5k2hRCElI7Ye7doRIK5LqRhozla77EPU0xxLi_wWsX3HfijyprIeEkERqQJNOpJ-nwGAaX0bufS_uv1r_NOgqG40gkQXyLZnbU19vGm2bEqBnHOiNKFwLsDJsuK-ZwyLPFFDHSj3Qs921BoQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تخریب‌ها در طول جاده زبدین-نبطیه در جنوب لبنان به دلیل حملات مداوم اسرائیل قابل مشاهده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126801" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126797">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0587976996.mp4?token=RUEsK0440OZEoV6RN3bcu6M-pWpcNidveRqCCMZehSUF2eIF13jo-Oh3CktooffBk3rbrzpc_qH9dMbS5EDIqgtgk2oalwQUKzyzLMV-_oRS4Zzzv52iZy0QYQpXDDic5cHALP8YRJGy2qQ5fICVY1HNnTwaGUvdagZtScwg3AJdq9yWNkZHghj1Gli9DlDRc_dvME4Wu7d6eIOHyMFhPrn6JrqGE1MjqaBIcmcDfQ7-GOLH5v8baNBW6ZsoXZcOW3GDl7zkjZCU3cCW4KubESUFAnnVkubQeFxDPsnslCUrJl1aPpycNowqUzgthnfyLLqq8aDXRRp-G4zs5CVfcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0587976996.mp4?token=RUEsK0440OZEoV6RN3bcu6M-pWpcNidveRqCCMZehSUF2eIF13jo-Oh3CktooffBk3rbrzpc_qH9dMbS5EDIqgtgk2oalwQUKzyzLMV-_oRS4Zzzv52iZy0QYQpXDDic5cHALP8YRJGy2qQ5fICVY1HNnTwaGUvdagZtScwg3AJdq9yWNkZHghj1Gli9DlDRc_dvME4Wu7d6eIOHyMFhPrn6JrqGE1MjqaBIcmcDfQ7-GOLH5v8baNBW6ZsoXZcOW3GDl7zkjZCU3cCW4KubESUFAnnVkubQeFxDPsnslCUrJl1aPpycNowqUzgthnfyLLqq8aDXRRp-G4zs5CVfcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله پهپادی اسرائیلی به تازگی خودرویی را در صیدا، جنوب لبنان هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126797" target="_blank">📅 15:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126796">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edBYsKctFRx7lobuhLGsDRBHFnoz6k6Fi__IYsOynquX5-u1RdlEYGiY_KqIGoC4QSC9v9WJXvesRcTA_GtR42LvrsPiI6aivQ0pCSkGMxSGWcBFFXxYeLgidmMV1V75_P7ZH6Refojlk3McicWHS-ES0fFxHPDYfJ2CnQeg_DDeCRBmWGmH4qn4B-YXhZ_OmwMWZGYnYhPYJg9ozz0gv_bad3cJpKXd3dmSCK7fGRhRygYnArgACvQ-5TPBfV1xaMbnLoM_TLka1RVq5Rz_FFJN6c62CZdDCNh2TjW-MGkxk5xE48rQQwOhYssfFeb3HGRMzHP5VH9-lEBwPSsRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید  ترامپ از طریق تروث سوشال: رسانه‌های خبری جعلی از گزارش میزان اثربخشی محاصره دریایی ایالات متحده که موفق‌ترین محاصره در تاریخ جنگ‌های دریایی است، خودداری می‌کنند.
🔴
هیچ چیزی عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است! ایران هیچ تجارتی انجام نمی‌دهد، به ارتش خود پرداخت نمی‌کند، یا هیچ قبضی را پرداخت نمی‌کند و به سرعت به یک ملت شکست‌خورده تبدیل می‌شود! مقدار زیادی نفت خارج می‌شود.
🔴
الحمدالله!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126796" target="_blank">📅 15:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126795">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری / فاکس نیوز: ترامپ در حال مشورت با مشاوران خود برای بازگشت به جنگ با ایران است و گزینه حملات به نیروگاه‌ها و پل‌های ایران را بررسی می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/126795" target="_blank">📅 15:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126794">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
تایمز آو اسرائیل: پایگاه هوایی رامات دیوید بر اثر حملات موشکی ایران در شب یکشنبه دچار خسارت شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126794" target="_blank">📅 15:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126793">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
فوری / ترامپ به فاکس نیوز : به صدور دستور برای حمله‌های جدید به نیروگاه‌ها و پل‌های ایران نزدیک شده‌ام
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126793" target="_blank">📅 15:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126792">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری / ترامپ به فاکس نیوز : به صدور دستور برای حمله‌های جدید به نیروگاه‌ها و پل‌های ایران نزدیک شده‌ام
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126792" target="_blank">📅 14:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126791">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
یک منبع آگاه به رویترز گفت که مذاکره‌کنندگان قطری امروز به تهران سفر کردند تا پس از رایزنی با واشنگتن، توافقی را نهایی کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126791" target="_blank">📅 14:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126790">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126790" target="_blank">📅 14:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126789">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
قالیباف: جمهوری اسلامی ایران به هرگونه تجاوز با قاطعیت و بدون درنگ پاسخ می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126789" target="_blank">📅 14:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126788">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
فوووری/ترامپ: ارتش ایران کاملاً آشفته و بهم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و هوایی آنها، دیگر حتی وجود ندارد.
🔴
آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و عمل نمی‌کند. قلدر خاورمیانه مُرده است!
🔴
آنها برای مذاکره بر سر توافقی که می‌توانست…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126788" target="_blank">📅 14:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126787">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6aff5606c.mp4?token=rB_iKbJy4HDBj_pOITTy7gI9KZmAZJn5F_wPFmRMWzMzsvjFEk4pwpjq3wgh7Ita_lZMxlvZK3vpRmBq7UrcSTyyBXrOyV_nV_1EUg7qAHa8pubWslenPbXNiYvlNPbqAgFNBx96R8FxZ7k33yRqnvT8EXleVgIMvrSUfaTAXChxaBuxMAZG2LyjZUInOJOPROGULRcv2atEt3zbIUSanKK83Kb_NvvF9GcBCZoHNuVpdthl-H-1NdMiOA5KxLfN-gdWTmDaRGPssfE6xtZCkpksjM-BQ1aVl09ATByqMprjoF0tNfZ5axDwoJcHicJgJsR0O1IDuO_WudprFRjdkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6aff5606c.mp4?token=rB_iKbJy4HDBj_pOITTy7gI9KZmAZJn5F_wPFmRMWzMzsvjFEk4pwpjq3wgh7Ita_lZMxlvZK3vpRmBq7UrcSTyyBXrOyV_nV_1EUg7qAHa8pubWslenPbXNiYvlNPbqAgFNBx96R8FxZ7k33yRqnvT8EXleVgIMvrSUfaTAXChxaBuxMAZG2LyjZUInOJOPROGULRcv2atEt3zbIUSanKK83Kb_NvvF9GcBCZoHNuVpdthl-H-1NdMiOA5KxLfN-gdWTmDaRGPssfE6xtZCkpksjM-BQ1aVl09ATByqMprjoF0tNfZ5axDwoJcHicJgJsR0O1IDuO_WudprFRjdkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
همزمان با پست ترامپ، توئیت جدید نتانیاهو : ایران نباید سلاح هسته ای داشته باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126787" target="_blank">📅 14:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126786">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9rxoWXPgbyashvba03ht2gONMM_kpnVA2R9dVjOMxsd0PIjCOp7kN1Uwttxj_vLHxtyMVXKFh5fAd7HfeOGcotfppNwA8vFN9PfrYoKEVp-1PrBDkCFsGfua-b3nAIWR782FLCLbuKvjb0Gb8LbbXumeaow8tL0aQJhkKQMffBRBdb8l4fbC0x2bRXV0tYnJ4fMCj_6i8-qpOUb52F35agBmVU3HdPlqxR-0nikCJA_2uIFcIr3F2f4FXTdzk8NOsClezrXPbHERwtr_fBRgYfuEoaWJz8o47BQ13qP5wJuHBbR1mfDX-Y3vGBrkyaZ2sWd2sjQ-ILhMcuCfVMZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووری/ترامپ: ارتش ایران کاملاً آشفته و بهم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و هوایی آنها، دیگر حتی وجود ندارد.
🔴
آنها کاملاً شکست خورده‌اند. ایران فقط حرف می‌زند و عمل نمی‌کند. قلدر خاورمیانه مُرده است!
🔴
آنها برای مذاکره بر سر توافقی که می‌توانست برایشان عالی باشد، خیلی دیر کرده‌اند، حالا باید بهای آن را بپردازند!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126786" target="_blank">📅 14:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126785">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
دیپلمات آگاه به فاکس نیوز: پس از رایزنی‌ها با ایالات متحده، مذاکره‌کنندگان قطری صبح امروز به تهران سفر کردند تا با ایرانی‌ها دیدار کنند و با هدف پر کردن شکاف‌های باقی‌مانده در روند مذاکرات تلاش کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126785" target="_blank">📅 14:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126784">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
فارس: ️انهدام یک پهپاد در آسمان خوزستان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126784" target="_blank">📅 14:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126783">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خوش چشم تحلیل گر ارشد صدا و سیما:
جنگ سوم تو راهه. این سری قراره شدیدتر و بزرگتر باشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126783" target="_blank">📅 14:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-fWphkNSs6ORSAD7_tfBJGn9KOZGTFH5QAhD72Bbc7pcpVmDumJSSpZam9Zz4ulJze_iblPhEeCwixZO8aAzWF24KdAaP0KUDEHDeAKcSqHhGTbn03yoKjAWhq3dnS5ju8HltkmPB6eEzyoGWpZtNBqQ8erMLij4SgRLI-7fkgAtaPIu3seNNdemltjmH46nD3DkBFwV6ZrBJILRn8xnTHtfbzC4hmV2oEFfAI9KUWIvPqvRhh24HHIU4WiWWNQGCngWJy8aE9Etolmt6TfWKuEuY5PQlZQNm0uP_g0ghU6RZ3kYBZSW4578HVxY0ekAt3yPxsFSpyx4snQXdJ3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آمار به‌ روز شده از تجهیزات نظامی منهدم شده ارتش ایالات متحده آمریکا در درگیری با ایران (۲۸ فوریه - ۹ ژوئن ۲۰۲۶)
🔴
آخرین تجهیزات منهدم شامل چهار پهپاد MQ-9 Reaper، یک پهپاد MQ-1C و یک بالگرد تهاجمی AH-64 آپاچی ارتش ایالات متحده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/126782" target="_blank">📅 14:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
دبیرکل اتحادیه عرب، حملۀ ایران به کویت، بحرین و اردن رو محکوم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126781" target="_blank">📅 14:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126780">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/887a04c96d.mp4?token=AN-xZp9HRVEOPUQhkkC91qD1PZ_kfsIM5-GMysmZKyhCiecZK2uhy-gKtn35erJeVa0an4N-VIhq7lXP9QFCL2NIfYNm3BGZ3Kbew86CMhzTS4qIgxeCCs3zkr_PnFKWEBK9k0UsWKMu-vNvOASGWvPz3pQWoFVzqIkvDwsBBptmbKHRXitkwuNMv4p5WvRHpQxLzHNfUR2S73rCn3JT2FbJZMxOT5Oo4KLOLKqU8CmSE_V3s-JVVJf5QtaWqh2pC1qsvk9h_KsXSbHUqu-1wFAlVw9SPE_kBBOKcAdkvM6Oq0eqlcNDLcn_OWmxDVq4rlx0Fvgbw8k28JRiRLushg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/887a04c96d.mp4?token=AN-xZp9HRVEOPUQhkkC91qD1PZ_kfsIM5-GMysmZKyhCiecZK2uhy-gKtn35erJeVa0an4N-VIhq7lXP9QFCL2NIfYNm3BGZ3Kbew86CMhzTS4qIgxeCCs3zkr_PnFKWEBK9k0UsWKMu-vNvOASGWvPz3pQWoFVzqIkvDwsBBptmbKHRXitkwuNMv4p5WvRHpQxLzHNfUR2S73rCn3JT2FbJZMxOT5Oo4KLOLKqU8CmSE_V3s-JVVJf5QtaWqh2pC1qsvk9h_KsXSbHUqu-1wFAlVw9SPE_kBBOKcAdkvM6Oq0eqlcNDLcn_OWmxDVq4rlx0Fvgbw8k28JRiRLushg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
علی خضریان، عضو کمیسیون امنیت ملی مجلس: مطلع هستیم اردن پایگاه و آسمان خود را در اختیار آمریکا قرار داده است و حملات به اردن پاسخی دفاعی بود/ تاکنون ۱۶ پایگاه آمریکایی در منطقه مورد هدف قرار گرفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126780" target="_blank">📅 13:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126779">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553c628858.mp4?token=la2hQACZN299M5hHoq6gswjOXNMXL5PwZ-8Z7Qn9y2-INhgbmA3u-DORFBI3XLKWhaf1LWurcWf2hxZoK4xnWItDCcc5Vx_PzFwEHO5nklKXXnppO-0DHOOhHRNwf_kW5VKoJRJxStVSSytFwXwZG6kHFwLKK52_eViEDzZ20SzsbGyA_G2NPviUPw1QpyETAzaMWGankVf9wrJkt5osWfxDwHJa0ajfFR9paAbkXPtARjqSR2J38TLuN5wWO9jmj1TVY1tOd-1ni_2N7fMF1vqFQpyOyswX-tlVWrANX8QcznE0EP1RXhz_XK4qQlwwRGJ6-_8bYzzzkMwkpwoemg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553c628858.mp4?token=la2hQACZN299M5hHoq6gswjOXNMXL5PwZ-8Z7Qn9y2-INhgbmA3u-DORFBI3XLKWhaf1LWurcWf2hxZoK4xnWItDCcc5Vx_PzFwEHO5nklKXXnppO-0DHOOhHRNwf_kW5VKoJRJxStVSSytFwXwZG6kHFwLKK52_eViEDzZ20SzsbGyA_G2NPviUPw1QpyETAzaMWGankVf9wrJkt5osWfxDwHJa0ajfFR9paAbkXPtARjqSR2J38TLuN5wWO9jmj1TVY1tOd-1ni_2N7fMF1vqFQpyOyswX-tlVWrANX8QcznE0EP1RXhz_XK4qQlwwRGJ6-_8bYzzzkMwkpwoemg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان، رئیس جمهور ترکیه: امنیت ترکیه نه تنها از هاتای، بلکه از حلب، دمشق و بیروت نیز آغاز می‌شود!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126779" target="_blank">📅 13:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126778">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e17a15e0.mp4?token=LBJ0u25PWL9MZpzYMjkDiWYyOF5i6zm0BsAHIwMV3Nu7vF-CW97r_5Zl92fPZFMvEuvUE08W9YecQ4eOrQWe-cpxDFhd4a7hCSJEFzp5CywaAzlIrNwVKlk2gqrURp2X4kvedu7tXYmVUrbVf5jDoTS5mHZPB46SLcxHGFjntIwak3R2-PVNLI0Ok4RuJly5mgLulpykHaIX9yzfALwLOS_M9el3U3bExcDukp5AAu51tCGyKiVzYoorgd5Gck4psFblLBV6Gd-51tj7NaSHN3Ez2XgzKBepf0-kvPbTZ8ra-Bd_2fgyXZ7LvlHrNZ8UixJQTfLS4075N6ocFo3BlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e17a15e0.mp4?token=LBJ0u25PWL9MZpzYMjkDiWYyOF5i6zm0BsAHIwMV3Nu7vF-CW97r_5Zl92fPZFMvEuvUE08W9YecQ4eOrQWe-cpxDFhd4a7hCSJEFzp5CywaAzlIrNwVKlk2gqrURp2X4kvedu7tXYmVUrbVf5jDoTS5mHZPB46SLcxHGFjntIwak3R2-PVNLI0Ok4RuJly5mgLulpykHaIX9yzfALwLOS_M9el3U3bExcDukp5AAu51tCGyKiVzYoorgd5Gck4psFblLBV6Gd-51tj7NaSHN3Ez2XgzKBepf0-kvPbTZ8ra-Bd_2fgyXZ7LvlHrNZ8UixJQTfLS4075N6ocFo3BlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان: ما کاملاً آگاهیم که هدف نهایی توهم «اسرائیل بزرگ» چیست.
🔴
ان‌شاءالله هرگز اجازه نخواهیم داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126778" target="_blank">📅 13:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126774">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bihr3WNM6a0V5HoKPKkV4W9750qK_xgOqf8cquAfrYgufrHWZ0-aRGlH7Kyoe8BdvN8pjF5qEXE18SWsOl-uWheoJ0taTJUdL9-rH_m61M6sx0rcgswPm-gGf78ffM5R3gFOgmyioCdM7OLJzXm0GbQhg9TnISnBfc3sMwEHIxaLpoXfr9bhUHyt8h6QswjLZjKQqjrh1nSEjXYMYhZeUObCKisLQGGzon6ow0nQCuP8rQPvliFqWMcAm_XdNIiFl5oAfc8dtKKgdYVlso3x3C-JrazoehVH0ANKaip62OYJdkRsE_1Rbih3fuBbgI6Oo9WcE_sG1roHuGz9aITQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AuMtHiqbo-iESIPbJHTm4n2dy9Cp8jlKCm1K5gBoI0-N_m1JHSh2ujFR5fmY5_KW8RbpY9BkeKfLajVagOTPI0b98hAaJi_RKDjLzba5CB3HkNIy1dlX_K6sJNtlBWMoNlT-cxEUzRIOCVeYFCnGRC-cVSmnJ8jmXZTKW7BH3F_lBQYqAm6FgXiphllv6bAYGEEYV02jqU-6dD-K0B7v9BTmuDXbZfnoWuWcDtffSASIdXx2ylHMZDbzQB48K1xFzowVWKrBqHIW92OpmCX8FcZe4E4yRqrKsX4amJfxKRr9rhFa3xHYsJ5-_cw9adyd5RXKk6BNm6rE2mVDbNDw2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5241ba3243.mp4?token=TynWlZJG-t3uXXcwW4zqVS3lqXTKxmTB6fLMzTabfOqPrwTIlNILACk81cFUXEpE3J-iaV5GCbZ6PjlxHoLAap3AgP6vS5PsBnDQ2fl-TAH5c6ROODe9E4yXuz9s43IuGp0iG-wraQD2KjU0Wu-icR--5-dJyXkxhxUuyM0kPyEMWCpIs_zdARiKNhIp7ZULddiTq2yZj01eS2fWU4c1uWFxMv9yr6Bw9aZpd-w8h3wtzUkb5JduJNkuno3UBKNhGQD03YRTwfMqYZa3Jb9qZJB5WM0p_LJYCptGpQ6Up-37puiqjikqnTtL87NX-xWiqxBG2riCUd1k_jSiqzzSyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5241ba3243.mp4?token=TynWlZJG-t3uXXcwW4zqVS3lqXTKxmTB6fLMzTabfOqPrwTIlNILACk81cFUXEpE3J-iaV5GCbZ6PjlxHoLAap3AgP6vS5PsBnDQ2fl-TAH5c6ROODe9E4yXuz9s43IuGp0iG-wraQD2KjU0Wu-icR--5-dJyXkxhxUuyM0kPyEMWCpIs_zdARiKNhIp7ZULddiTq2yZj01eS2fWU4c1uWFxMv9yr6Bw9aZpd-w8h3wtzUkb5JduJNkuno3UBKNhGQD03YRTwfMqYZa3Jb9qZJB5WM0p_LJYCptGpQ6Up-37puiqjikqnTtL87NX-xWiqxBG2riCUd1k_jSiqzzSyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل به حملات خود به جنوب لبنان ادامه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126774" target="_blank">📅 13:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126773">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f3800f788.mp4?token=U6FLc4pheES_tJmWe9aTiaSkID6hfI_SU9iVK0XovxLv3rPBmB_jHqw7uo9tTpLOMnNw9mKbtUQwDJcq1nc4S78PgmnIcyC4sR5Wh1icIwg9xaeYWckAG9HUlSnyTzu_KzBkMRPZzg9O4jZKlqMl4f6O1jj76iRJLVBv74IHDLii5d6ISeiIa7SsqBfTSNildZAx2FV_ukAVg4je5CmAIqU2AIBMPk7FPLZNmmoAhAQB6wOmDVIcN3yBYDEAoNGJW7U9amwX0-Nbmdepo3uw4fH8luWnyEI5wrgLHMv-JVBAQgr1X_kzauztvyvHSkX8fdSc8SnuRI1LUlZkg8mCCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f3800f788.mp4?token=U6FLc4pheES_tJmWe9aTiaSkID6hfI_SU9iVK0XovxLv3rPBmB_jHqw7uo9tTpLOMnNw9mKbtUQwDJcq1nc4S78PgmnIcyC4sR5Wh1icIwg9xaeYWckAG9HUlSnyTzu_KzBkMRPZzg9O4jZKlqMl4f6O1jj76iRJLVBv74IHDLii5d6ISeiIa7SsqBfTSNildZAx2FV_ukAVg4je5CmAIqU2AIBMPk7FPLZNmmoAhAQB6wOmDVIcN3yBYDEAoNGJW7U9amwX0-Nbmdepo3uw4fH8luWnyEI5wrgLHMv-JVBAQgr1X_kzauztvyvHSkX8fdSc8SnuRI1LUlZkg8mCCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم از آتش‌سوزی کشتی در سواحل عمان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/126773" target="_blank">📅 13:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126772">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
اردوغان: اسرائیل از زمان تأسیس خود نقشی را ایفا کرده است که صلح و ثبات را در منطقه ما تهدید می‌کند و امنیت ترکیه از بیروت و دمشق آغاز می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126772" target="_blank">📅 13:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126771">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
شنیده شدن صدای جنگنده در آسمان اصفهان؛ پرواز متعلق به جنگنده‌های کشور بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126771" target="_blank">📅 13:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126770">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
اردوغان: حملات اسرائیل به سوریه و لبنان اکنون به تهدیدی برای ترکیه تبدیل شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126770" target="_blank">📅 13:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126769">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b592a4502.mp4?token=Ns45-Xg8ALB-gguKtCDeKufVlOr2rdR516FqjQmoH3GDfVxrvcHr9dXWZJ-gr7J-B5AjesEWoQuDEh7MUo0b5m6F55awfmZLKT23wFnOqP5p-yQlJY-BMQxoiHkPa32OmPr_7IOZ_lnr7nFlaX1i7T22DdQKQlIXgkJWgXj_VLKa5SL8DsfeZWbf_cAm2kRMqOk1H6SXFl0LbrlULc7PTlQmV3zst2QHhYcsdyYfxWNzolxdNWP3KGdDriK7SEZpYFMrDtpjZwsMATwG3IQaQV2kTgrqc3x-U5N5kjz7R7hMpM0oTHqNlL9VZjJECkdPoqn-pw-yisF3r9-lA6C2SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b592a4502.mp4?token=Ns45-Xg8ALB-gguKtCDeKufVlOr2rdR516FqjQmoH3GDfVxrvcHr9dXWZJ-gr7J-B5AjesEWoQuDEh7MUo0b5m6F55awfmZLKT23wFnOqP5p-yQlJY-BMQxoiHkPa32OmPr_7IOZ_lnr7nFlaX1i7T22DdQKQlIXgkJWgXj_VLKa5SL8DsfeZWbf_cAm2kRMqOk1H6SXFl0LbrlULc7PTlQmV3zst2QHhYcsdyYfxWNzolxdNWP3KGdDriK7SEZpYFMrDtpjZwsMATwG3IQaQV2kTgrqc3x-U5N5kjz7R7hMpM0oTHqNlL9VZjJECkdPoqn-pw-yisF3r9-lA6C2SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی شهرک حومین الفوقا در شهر نبطیه در جنوب لبنان را بمباران کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/126769" target="_blank">📅 13:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126768">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
افزایش آنفلوانزا در کشور؛ کرمانشاه و البرز در وضعیت قرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126768" target="_blank">📅 13:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126767">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: ما حملات دیشب ایران به کویت، بحرین و اردن را به شدت محکوم می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126767" target="_blank">📅 13:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126766">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
نماینده روسیه در آژانس بین‌المللی انرژی اتمی: حملات آمریکا و اسرائیل خسارات جبران‌ناپذیری به برنامه هسته‌ای ایران وارد کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126766" target="_blank">📅 13:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126765">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">خواستم بگم صدا و تصویر منم کسی نداره اگه لازم بود منم میتونین رهبر کنین.
سابقه اجرایی در خلوت هم دارم.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126765" target="_blank">📅 13:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126764">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4WndFjmkSZMN6F1-VQHU2WryAvIRxSWFkQSYTeBsh1plmU3MnUW5qYLsrvPgM2Nr5g4HUQwlzNJEOph4-L53pDtsu_m_t4-kDzVKtxa_gZ4AMI8rPjBs7mCA4E9j6scz8W_TO20djdTsYCN-hjXwWfztO4NGzbh0TqIL-wNVf3OoB-XsOdgyAJGc9IQvE6qxVoRK7uBSe0QGRxsdTmzFUZ6heegF8YbbkdM7fDkLNqTVPVrQYlYChXuj7ogr4lwQsYmgOxVd9qsx5RmOluWavVsLVVP7vsjedgkn9nt9Pm_yI_Z5F4paFAUei8BuWeH26v_t27qDVE_Z5_I5KMuLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان تجارت دریایی انگلیس:
یک نفتکش در نزدیکی ساحل عمان از ناحیه موتورخانه هدف قرار گرفته است و ۱ خدمه کشته و ۲ تن مفقود شده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126764" target="_blank">📅 13:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126763">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZPKjEZak1kbnNgfVVhX9rbwiq1o046Dsx_TCuvUlDEwa8iIeS_2ta8JaBq7nAAQ1AIzhjPonWNGcWUnPkpbNK2iWz_WoHIr7xwSw6PgjcX0d2YbaOpOEFtZMAcpn-DZhSEHbtyjuOO1VeM6rziQLxU5ee7Eati757scVTaKKwiwRVq2rCc7UBp88iatYGcIcdkZNxZSYAciDlLtWoxdQqWePpZsIW8MYoBuh1FZRFUE4N9faJkCF_XNh8LCE95Qi9HGYZZGydRwSVyz2XuT-PyoxxfMs6ISWvVfdaJDud1d46OvhaQBneA_ifz_Y4UKKDNipzJWEVWNUn83gQ3nyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی هوایی اسرائیل داره به منطقهٔ خومین، لُبنان حملۀ می‌کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126763" target="_blank">📅 13:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126762">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
فارس: منابع از وقوع آتش‌سوزی‌های گسترده در مرکز اربیل و شنیده شدن صدای انفجارهایی در نزدیکی پایگاه آمریکا در اربیل خبر می‌دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126762" target="_blank">📅 13:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126761">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تایید نشده/ گزارشات اولیه از حمله  آمریکا به بندر سیریک در هرمزگان
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126761" target="_blank">📅 13:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126760">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
پزشکیان: شهادت فوز عظیمی است ولی اینکه دشمن بتواند به این راحتی فرماندهان ما را شهید کند به هیچ وجه قابل قبول نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126760" target="_blank">📅 13:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126759">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR4juiw10g2XCktbbOQLVbHfdEkK64JdjYHqq8razj8Ajw6aIObpV9tHP4mpKRwph3BDlj8m-Tlqb5WCLiN4DBABuXjF2eutxW6o5ocwEGx-WH27IuWQPhoYqpjnm8azXQBQZhKjrtyKwJIhX7K2-1BuaZbWGbLIicydS71XtF33TTYC5JF7Y2LyrCpijdfqHDqO6hpxUlLI3yorNEGA1nVUWmyBM33HYLvZgqRggOv9CVuGcRdDfujcNnnanxU_SIs8N8HNpIyKbf7PaJtoFy96-fLv3hDwVIBTF9JWLGtJJ0PGN1FMU3puPLAUX7zWDjL0RUTFqqnfKIgFb1ibqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صابون گلنار ۱۰۰ درصد گرون شد و قیمتش ۲ برابر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/126759" target="_blank">📅 12:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126758">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
پزشکیان: ما الان در تحریم هستیم، مسیر ما را بستند؛ امتحان سختی در پیش داریم/ نباید  قصور ما باعث فشار بیشتر بر مردم شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126758" target="_blank">📅 12:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126757">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
پزشکیان: قادر نخواهند بود ایران ما را با تهدید تسلیم کنند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/126757" target="_blank">📅 12:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126756">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
تایید نشده/ گزارشات اولیه از حمله  آمریکا به بندر سیریک در هرمزگان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126756" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126755">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
روسیه: آماده کمک به حل درگیری آمریکا و ایران هستیم
🔴
واشنگتن و تهران خویشتن‌داری کنند
🔴
حمله به زیرساخت‌های غیر نظامی، کاملاً غیر قابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126755" target="_blank">📅 12:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126754">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
دقایقی پیش منابع محلی از شنیده شدن صدای یک انفجار در محدوده شهرستان قشم خبر داده‌اند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126754" target="_blank">📅 12:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126753">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cbbdd0458.mp4?token=QxRifY_UBh2lCrttSfr7QAO-jqdwd37gtkPSJ4X9Ur-vxP-GWRevpgss9EGguXi2q8CqqH_-ujWrZG54ZuxI9Zq9tKQ3nfKNDhiAQI9rGdVup58gfBayWDTaIvfUyNXyjgtUvjRyorfWuULAUAohM352apnPL11JpnrBHLZIDO3GUS9lqRQU7YLjMexnO-Edb_vvsB7wxFr0NBzJB46oxv0rl00rdemGrmqTQaV7fKLDOgOJMbDN5ljlxQmlvKS68bTieRh4nXyOpmgdK2dDQodQtIc_O714X5ysbuESVEQYh1ig013y2To7OcYawq9JyvBO6JdG3ecyBKCBXhAYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cbbdd0458.mp4?token=QxRifY_UBh2lCrttSfr7QAO-jqdwd37gtkPSJ4X9Ur-vxP-GWRevpgss9EGguXi2q8CqqH_-ujWrZG54ZuxI9Zq9tKQ3nfKNDhiAQI9rGdVup58gfBayWDTaIvfUyNXyjgtUvjRyorfWuULAUAohM352apnPL11JpnrBHLZIDO3GUS9lqRQU7YLjMexnO-Edb_vvsB7wxFr0NBzJB46oxv0rl00rdemGrmqTQaV7fKLDOgOJMbDN5ljlxQmlvKS68bTieRh4nXyOpmgdK2dDQodQtIc_O714X5ysbuESVEQYh1ig013y2To7OcYawq9JyvBO6JdG3ecyBKCBXhAYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: قادر نخواهند بود ایران ما را با تهدید تسلیم کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/126753" target="_blank">📅 12:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126752">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
اوکراین :  یه نفت‌کش مربوط به ناوگانِ سایه‌ روسیه رو تو دریای سیاه هدف قرار دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126752" target="_blank">📅 12:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126748">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TDd4EqOWloNw7T8AuJv90g7eH9QhcmYuazWGT9qbuhIVV1kXxJqUmaCMJ5ygeUJ8LQctWKXwszCz2yuu63RVzMyo4ePpnLBeU7VLUPNj9dTiAl0KLvPsHpF-sJeCnntVPi4sPpcu4CxLvRTyZLCc5ow3i4NHNMZPfYcIbr52CRNs7YY8sGQXGmXa2Q2RDGRq7fc_WknkesvMV6oDGPbBJk-zAlpxTV5qI3t9XIAEedyKD4h9eriIpZ5p1YEHQunit6g0IhIOgjz3aQfpblhOp9OVR4kIPXmKofFh7YDMzkhMpEYUuL3Zm05BzTM8GQCdPxh7dYIl7Qwsbfsd1LNL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfPASS7b2YnmctTp4oSh7Bjr7kzIkkk7QmIqzRldPXu-rQThSEd5O2gZ2hiAohW2we208mKYEvgk6_Hyj_046tfkfx7UoZTtjnXRdX1jw4prGhiKVcevEp1DZeTQFfDT8gONI2Ty_h_TRzpSxlzX4Q0AJYCGkl7sScj4YGdJvX0zs4Bhe_MFwg3IPwwNmqHX2l6hL1eHlYKLgPz5J3BFY6BjKuNdOa-_RJVorVwpWjT9mfWLAk9CzcZmGT2rhzVtGbK8Tvh42dktCcayNoeMA08YTIv8gpmZY_09cFEnlWCQgENA5c7Kp8C7xS41DZ-deAKpcPZ-__aer8akdfb8Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvuzyEPLQl4wJKZHDDOcnsHc4wVQFI9KiVns2HYJtohHYYgb-m3WUhdGs2mrYawoPVnPHVwybqWbj7-6R7rOOCIYWOdZo7kkTgntbIhVjbRdmfUZ6Z8a185p06L0SZ8ubMbyK8WN9rUhFf7sG6Pptvcg2T_y4VDgFj4ziFMFy5qhqHWf7gqSb-CW8_PQJQ7bd0f35bd7krZAx9tzXmClh0RrCnlFKR7siA0mpPdIhsrKewsB8cAZbRLpYa1Q7FMtzKvXpCY_wNyKfld282Y22yeQ99nuNx66zSFzb7pGrTfLVmba4PCN7hRA6L_C857oyRZnPiF81fnVSW4Caz88Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUxLjRgnT9rEVdFDnQO1DBJ1YLENhl3mMiRmqG0IQvEBHg7bIJ0xGZY6ZcshGf9LHR6jjif75DkGovRQERUz1uTXTKMsNcaPQcwuz5GVh3XJNIvl8zd2fDZeFnTeherVFmVs9nBwqlw_TDx3tjLSDc-m8K4R8oU2_GhxN-fMmhRs0CUu7xBHu39V2_1SI7tbWtA7fyzOATGXPolHoXU1WYWD0_GoOvok0YuEQ2nSMZq5IF5zVuAE-GRuOrSFgE17fjIcnkHf58xEwJnJX6AQd_ztyO-wK2zHeV3T0aj0-HVqj9fXjmWmJxB1rr0UwivDqvHFheZtnz0RvvUQXOQ62g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملۀ به منطقهٔ طیر دِبا تو جنوب لُبنان انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/126748" target="_blank">📅 12:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126747">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ایال هولاتا، رئیس پیشین شورای امنیت داخلی اسرائیل: وضعیت امروز ما بهتر از یک هفته قبل نیست، و تمایل ترامپ برای ورود به دورهای بیشتری از رویارویی اکنون کمتر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126747" target="_blank">📅 12:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126746">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATrdl8A-xjnqP-q6IGrMaCNVBklp-R_LKNCJwG8fBs2G0oi2MykU-qG9zv8VIoCoitCIyszzP3l_tXGl0u6CuUvLRMCReDny7t9QtWC4GQB1J0IMzhpVXiux5ZwXPnl7VtKVxsfEokoUjDE0IDFAazlZkmOi6G1h0Tt6QiU6cw541_qBwpI-fH1S-EeXKfHATrXz2s9pqxBzJ0LTGt8S4HUJAIZcjLu5d-2W_IR0ROkd2z-ovcCSHRy9yLoIYZYlw99w5sfacABjekDKFjvZaVFwmtPgi0OPambfu0BKdhQoaYdclCvunjd6GS1DAZ7J-gCtROXdeyH7zWeW7AkiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از کشف تجهیزات پشتیبان هدایت جنگنده‌های اسرائیلی در لواسان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126746" target="_blank">📅 12:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126745">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سخنگوی دولت: لایحه منع خشونت علیه زنان در مسیر استرداد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126745" target="_blank">📅 12:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126744">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cl3Rb1pgayhlOOnPJAufjQzgUFGA_BzQQqvYIz6kqo3mWkHwsEMFEQ869EGORjVD1TgUzvPHgnbNCJYWS2eynPq8KW5SbP-ADKAn0j0frj6SDHqw4D_4zT7z-t4Mmw7LGn72tz2Z-w9kNQKCezIHMIRLsT8xYS5qlYZ4Ad-flt-jIp4q63ouLFrOZ56_KZsRI3nHfiRp-CjPkWu9OYZ5esQ8IOStbKuTvT6I9m2LISR-2zeD4Rsz7SqMXKz66epd85rBeklEG6aRUoWwAlLNfRYPKknDRv8tx3t1EW0rb9Bd03qisirG96L-2bv8hNtt3fPZBJYzu7lsIktT6qjskQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آسمان کشورهای منطقه بعد از حملات بامدادی ایران و امریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126744" target="_blank">📅 12:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126743">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:
🔴
دیپلماسی و میدان دو امر جدا از هم نیستند؛ این دو در کنار یکدیگر، ابزاری برای صیانت از منافع و امنیت ملی ایران هستند.
🔴
در هر کجا که لازم باشد، نیروهای مسلح ما با اقتدار به دشمن پاسخ می‌دهند.
🔴
اتفاقی که دیشب رخ داد نشان داد که نیروهای مسلح شجاع ایران در دفاع از کشور درنگ نمی‌کنند.
🔴
در حوزه دیپلماسی نیز ارکان حاکمیت کاملا هماهنگ هستند و در هر کجا که لازم باشد، از ابزار دیپلماسی و هر جا که اقتضا کند، از نیروی نظامی برای دفاع از کشور استفاده خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126743" target="_blank">📅 12:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126742">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
شورای امنیت روسیه در بیانیه‌ای که توسط خبرگزاری «تاس» منتشر شد، هشدار داد آمریکا و اسرائیل از پوشش دیپلماسی و مذاکرات صلح برای آماده‌سازی یک عملیات زمینی گسترده علیه ایران استفاده می‌کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126742" target="_blank">📅 12:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126741">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3507988ffb.mp4?token=KgKndtD9TBur9lT3fa8rfTYRi5pYcs58yONHAyHVAgdS5RJEDSZNdb6lquT1u_NyQuWo2IRBS4SgmboaCXCx9unkW3QuHXWSNeTEUYo26WDEqNhT1FrsYI3PiB6NVGNPhHMZGqa06k78lC5Df2EVbkBoE_bQS2zDBHSMgAAZuycOdjexrnU8eYFGfJz2VoaqItUNDkafyTEbJT69Ud2cEj29GxP3lDAjKn51Ju5Ooxkqk8bVcYaalkv5NY3pg3ZqV2_qakS0LtffKMcVaIknvLDcgjAFYcVx37fqQV8SCZQKoReFDEX0Xzpjd7DwvGRWOJEAzrfLwQNzHsqELbLg3g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3507988ffb.mp4?token=KgKndtD9TBur9lT3fa8rfTYRi5pYcs58yONHAyHVAgdS5RJEDSZNdb6lquT1u_NyQuWo2IRBS4SgmboaCXCx9unkW3QuHXWSNeTEUYo26WDEqNhT1FrsYI3PiB6NVGNPhHMZGqa06k78lC5Df2EVbkBoE_bQS2zDBHSMgAAZuycOdjexrnU8eYFGfJz2VoaqItUNDkafyTEbJT69Ud2cEj29GxP3lDAjKn51Ju5Ooxkqk8bVcYaalkv5NY3pg3ZqV2_qakS0LtffKMcVaIknvLDcgjAFYcVx37fqQV8SCZQKoReFDEX0Xzpjd7DwvGRWOJEAzrfLwQNzHsqELbLg3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه
،
بقایی
:
با توجه به اتفاقات دیشب، باید برای ادامه مذاکرات بررسی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126741" target="_blank">📅 12:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126740">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
چندسال قبل ولایتی یه توئیت زد که مردم ما باید از یمنی‌ها یاد بگیرن که با پای‌برهنه و خوردن نون خشک دارن مقاومت میکنن، اون موقع خیلیا گفتن چی میگی بابا، اما انگار داریم با سرعت به اون نزدیک میشیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126740" target="_blank">📅 12:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126733">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dA36C7vjr7GrMlelNkfytjTLmcVQS4WZNSmRNZPEZKXTK-T3T0ga7sDduEChm8xBgUYySdSCM-_2DiSFg3lOa0mZsfNxSs_REuSXkuecHQ0pjl7KbLVouMMkaCj_u0p0BhCq1h_iluLmUmgVzM_PBjF0-udTdQg8etcGJZ28zGfzY7YjJTtKcGHhVcoZni0DfmjdOgk635SaYFXg8PJg5pff_PQu3dq4alohvI_G67JAqH4mhYxIDDbUZg85bUnvo4Vqx9VwRyk5u-Gw9ECuScoAQMvpOKU-ADF9TBu5ZLW57gy7wcbWv-0gJw83q-FyV1TEaah8VHd6fHi31pht7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VxlcAyCI4gvO86Fw04R4fk9Q_8yqwd9POu6wM4ON-j3DvckhhT0KQoOEHYosSd9nPGUKF8GJu5swf8JIGFBg3r_TiP_H3HH5T_GFVA7QxBBrkqcRcip4VDOjZsnosKjKoigsQF3J4FYntxxDz6dsF1aIRbIr_g51PdJeM4XTlI_8jbJq_tsf0efpOERsCihRtWKq_bnZ4n-QX0aW2MtdTcwaFDIig5ajdvRzvils46fql8O5DSHpqkIc82xK8k8pi2Y0RA35_dYHJJVIeYctJAlD-hhS-p2HvFeVNGG-njoyjH0LzgAftGH6GQlrW4t5Jdp94hNH5ivvFinGk-u9Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G1uD1uIzwGLxpfFbjaTvMKg3odeM-drw6pnrG2w1UJJIBjeG4uVGhXO-BqNzXSYGv0EvDc3uXYIzyYJkf0J709V0r5DeYImEzeUs5I4ChGVHW-E_ia0izipFC75P__7OiYaWl9Vnk9Z5WohbPQ4x5_5ZsM9HqGQvCbLV-LKP8KojKmDD-htPbQhtKFmvPfGPkw_LoVKf-2CBZL29DReNsJbs7w6YmPItabBqcxZwHSQalE463gjZsUXEk3Bx9W8U9Gi1-xAxYpkamCo__vGVBu9m2qaNgzrHx0hvkoVbwLq8sX3inPkSOpiCsPU86n_qtanrWB6O_J_dwvgYkSwwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FekIRqwHYK3PWLIFrgldBKYnE-y-0v4wqTMXqo-ibOJm53yGu9btlPUtcGAtqfNvHe4Vc1q8pnZnl9PWGFQscsEYrycQAfwzTZYrMABVR8N6TZboaJwrVReqieskbW-rYcmbE4Z9jFZ1IaUmiOXo7-it-9WtVJfeFbSgt9xomGENbaFNGBLMdEPJ3AiDxY3nlq8nFz38Z8joSw8BdOVHpl3RINRbpLLZVHD0tVj5dEjmljMQSHqGsA6Jnj9C1MEl69WPQmXLdPJFTUduvGT4Ky8nkD9_6Dndt755yXNowjI2xMaRxHMrsx5xXRL91rCBvXW6w-SRR3xjj7X2cizjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WsfjphGmS22p0xvSNDa9L0oO8KDYi1P5857WepyIfxRVtQs5Vr_mvqzDdy5bR47CkIk1GfGUMqpkXYhv7wxJXpPTWd8uXe8P9hoqQTVPbxMoN6e-c26FjPnik2DmH_ICdJzHfoYfmN35-XRZn5O6uQu8uBxACtf4qwl6_fHuLIADznV5jleoZnRT7url9zwVpKtaKXM7s3-mgXFinylIyrpRI9ugpqwDPX1zQ-e4C3ahF_vtdnxzL5lHYCRwes5u7eVByTu2BK-xnhwx3pbQuN0GOrGRQ6LL32tdqYmswhI4KF6c-3ANXZVwrI6e1E6TeLI5yjCG1G9bPIY_tEGM8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HxbMGVsJV5xjmykRoNCHSMdQQfeqbarv4avgA-1VQp8HDYH41WtHpADrNBbLW6h1NL3ezpgUpNmNX8p4dl144VmQacjvlRwOE8Ei3w87l5eOpauRRjs5QhCPze0ApOhUl2oH_RrxYoM4phiW8Q6z0qtVMiz3P5d4OGNld2dKQhpYqMeNTFmw0iKx4-LebgjscjcIi3PIq74fYV5HLzO1LTXGMzYBuWEgg36BWDn3ldwqRuZMWRrqWr0ePIdXpbdJJAmeMYu2MnReT0CDp8vdEmLg7iL1SIIkEh9l8qW0dcbyUEuSwzjdpPkbR9XRjYnlV_r36CfuyW7H8hz6wPitqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SfVbeJPGE9RLZ9j--nmCe9ghOegIH4DXUlAmV1LZUx3dxlHMXKMyQuIOGxSl2eURoTK8h0QFycW0YR4_HcmH4G7XBZHcvK605uqGl_w2RTSlBvX8tt_vymUIqGmazWTyBkkxb53e78mg-aK4xh52Hhxrx6Ue0iEA96QNx4_SB3f1FFx_MVapCi_n2k0bSpsUlNYRJs21GSIBns5pSMAIESe_D4wgPYXaU9ktSqGukuQJyqQ2YV1x36tXVMj1Ih0-Z9UGdXNoUEKV07fURrfu-CrOUeIHMuuFKRGYqY7K9pRv0bKw4isHOzmjyLZ9vsM3MbBdp-wUZqK21KQTKTftGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
در حملات هوایی دیشب پاکستان به افغانستان، ۱۱ کودک کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126733" target="_blank">📅 11:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126732">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMQfrH_ZYtqpiM-eHuCjTKvpPoPBO4Av8iMbWFoEAFTNc110LbC9Y8KSw77NyBJ1USnBbMMBA65niQjVUP41HaBcvVGPxFVPLxn0BBf5Jg5bmCEvwV-m7wDby7GUVnvf5qes_G2j4zvXrR7K3nwNg3zpxRdBz0gh9wrAhd5YMChMmm9-Sa5rseOiyQ_Iw9HdjZCplGILG5b3zmZUf3w4xcGuRUPofCsQCnTW8hJNfGuVOAeEnimQgKq6R5JRqoQE7RmdIuV3H1-GDEMhtZFZIJwMS0gJ8pQRBFTdUVfC9gxamn89uLJTP02CDscLM5Oxcz_bzLSq39OcpXtnzm4O7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت به ۹۱ دلار رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/126732" target="_blank">📅 11:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126731">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0GRa83FxqaAQFb5ZkfbZM7o8QgPthJKJBdLh6yRZG7ST6fgNfG36NOMh2vrGTjtxILhHjMsQcaLE42kRhOWTHDVhrxND9V1S7O_bQmSLFQfouR5VT9m1deYMZY3fZhBkYm1HfKfWGzsACOdIetirWl7ABWKl_kn8EWfi3lwFKqSENP2CUj7ANMap_i1GAoXKwCvIk_YB8ui-iX55aQkSI7Hm2CkwMHadl14q5XkEb6NzP_CR8DmPr1k5Yz0Qyvjb_j5GrhRnk1V0ls7cUmfiATIcWOCwIDgoDiVzlamKmJsKUk9Ma6XayU9ljjA3qJFw_Q1K297_kFjgM6HV4dHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت خاورمیانه واقعا عجیبه
‼️
🔴
افغانستان و پاکستان که دیشب باهم جنگ داشتن، امروز بازی دوستانه دارن!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/126731" target="_blank">📅 11:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126730">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/124deefd6f.mp4?token=MEAfZr_AmmwjYW44wIODyX3Bngbc6IJhCYBWJ8afx5P-8uhZ9qxH7xWAiLl1KUWTWGKPs4sPdUPlF0OURIH4MJjCAngmQiSK-lxFunLO6g__4gB8R-fEwLbX0SMls4Jg7FgIAPbB638BkeKxMojQj66QJ3lnK8t3mMvhfmWtraFaGVvdQdwLxXku7W8FiQsh8lABwbDh-jgu-ElXwtAdEvOSFXz4-FfMSuxp3m4RxKGjmkKbofMWKue1v4lueffo7foWt-ro3Hb1O2gGUxEDikHt-FPLf1POloEBrbkJInprIA3QbOthiQcajvNFdHwM-_-gNiRcFdK0dXBjg6Fe4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/124deefd6f.mp4?token=MEAfZr_AmmwjYW44wIODyX3Bngbc6IJhCYBWJ8afx5P-8uhZ9qxH7xWAiLl1KUWTWGKPs4sPdUPlF0OURIH4MJjCAngmQiSK-lxFunLO6g__4gB8R-fEwLbX0SMls4Jg7FgIAPbB638BkeKxMojQj66QJ3lnK8t3mMvhfmWtraFaGVvdQdwLxXku7W8FiQsh8lABwbDh-jgu-ElXwtAdEvOSFXz4-FfMSuxp3m4RxKGjmkKbofMWKue1v4lueffo7foWt-ro3Hb1O2gGUxEDikHt-FPLf1POloEBrbkJInprIA3QbOthiQcajvNFdHwM-_-gNiRcFdK0dXBjg6Fe4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر لحظه انهدام پهپاد MQ9 آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126730" target="_blank">📅 11:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126729">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDMAsyjtO0UB6uEDjic-1lI9xvzwpzXxQKmCt8Kjb5Dp1iiR61GAbwF-UuYoE_DfGlpEZuInKiz40RCi5BcqBieQQ8Zv8gYEVAlMvdUTtCXIm6Tl7OmAZIYYs-TA8tPnO2fE82D48nRMe0P5gc4WySUwcttH7j3d0WY14GfiA-NZZAoMqs3KbJxMQmDRMc7e408EdDPK5XeggORo0XXW4VyGlQ1Jhm1PrRjaynOGSEtxm1aOPgOcEh_R3obA8OXBO8ZuKrCODlbUnISNmKTB50D-vqgNGprdi8VOQM7JvogPuIY2RYGyTOJLmeRm8ga-81bi20pscQy0HFYewLNeew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
هنوز نگران تموم شدن حجمت هستی
😱
یا استرس ضریب و تایمشو داری؟؟
🥸
کافیه اشتراک TVPN رو تهیه کنی
نامحدود واقعی با ساب
🔥
که دیگه نه نگران حجم باشی نه تایم
🎈
اشتراک نامحدود فقط 290t
🎁
😀
حجمی از گیگی 2t
@tvpnshop_bot
@tvpnshop_bot</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126729" target="_blank">📅 11:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126728">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d417fd03d8.mp4?token=nalph6w_AJd7w7Jn8FnWccrJzljUBWd0w8syQIzDSgNMNOxNl3DcDONgp1YHNUhKH7I9leaJec0RUmDr_rPx1h1CHIazfSGQcLHg3TVeBmnceoYynXGMCvLQZ8h-JU_Vh5VadmBDf5zqOGVQD5wmVzfN5W5yKwKqjUsAL8ajr4ZwE3GoIAr-e1uYjl3MoOLXYTKkFEN4SGQCuYo7apZ_S6lSMaOsKZpdkYAy-_6BnfStWyZhMezWgyxH1b0ZLLItlggbizBjn2_pczYf3tgHMvypYpFzbx3-SzBVVYUy3tED-_wfwmtkeC3o-9TXXp6UYVxvWeirtbDlfaf0a0kCoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d417fd03d8.mp4?token=nalph6w_AJd7w7Jn8FnWccrJzljUBWd0w8syQIzDSgNMNOxNl3DcDONgp1YHNUhKH7I9leaJec0RUmDr_rPx1h1CHIazfSGQcLHg3TVeBmnceoYynXGMCvLQZ8h-JU_Vh5VadmBDf5zqOGVQD5wmVzfN5W5yKwKqjUsAL8ajr4ZwE3GoIAr-e1uYjl3MoOLXYTKkFEN4SGQCuYo7apZ_S6lSMaOsKZpdkYAy-_6BnfStWyZhMezWgyxH1b0ZLLItlggbizBjn2_pczYf3tgHMvypYpFzbx3-SzBVVYUy3tED-_wfwmtkeC3o-9TXXp6UYVxvWeirtbDlfaf0a0kCoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئو جدید
:
- صبح حداقل ۱۱ موشک سوخت جامد دوربرد به سمت اهدافی تو خاورمیانه شلیک شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126728" target="_blank">📅 11:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126727">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
دقایقی پیش منابع محلی از شنیده شدن صدای یک انفجار در محدوده شهرستان قشم خبر داده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/126727" target="_blank">📅 11:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126726">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbpCQmxekk8otRRjSdgOv2mX9l0F4hCdvGBR_5BYdvNPWqliKL2W92XIdS3NmsiZTOgcbmpq-CVzu2or_Ge5Q_Kah3Wm_aji0cjGolYBE4bWLVU2n70Pi5LcB8mGn3WheVJAXVfcDN-7kU-J5Esm8-4P88c5n_9Cn2sLXA2ob4Vs0NkKV5xsaW_bMxuPXUm0AjdG4eYr9YwR6J4n0Bapy-vMy-CD5OHXd4iuMut4sSKZU9Cfed_K1gocoj3bJXbJTMOSYt5O3e4Tn3LF5PLehb6wmEWttrG3yrs1LnH3lE4eXloujgVj1C55j1WZcz_tzWQ7fiRA_FRkm64v_GsQsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روستای بیت یاحون در جبهه بنت جبیل، قبل و بعد از حملات اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/126726" target="_blank">📅 11:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126725">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت دفاع کویت نیز تایید کرد که کویت هدف حمله هوایی ایران قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/126725" target="_blank">📅 11:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126724">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
چین: از همه طرف‌ها می‌خواهیم که به تشدید تنش‌ها در خاورمیانه پایان دهند.
🔴
ما نسبت به تحولات جنگ در خاورمیانه نگران هستیم و خواستار توقف تشدید تنش‌ها هستیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/126724" target="_blank">📅 11:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126723">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erDi7Dy8vqFICSkoXcu9msX17Fdj1xpCklFwb9duxWZl1GGk82zsb3GFaWH7rqHwIe78OOEpD7VKM60TpP9qdUIWTBN9iPVHNxQyhsaUnxHYBbzrcmBGGWkO9Bb7GhEX4ljJM8LWSGZSPTN4MlNSOewG4lqTSt4ku4L9YTMwEv47mAXAV-Xj-ASJx5xV2RfHxNbPLRG1GhkUvHcG3XummdGDqNxJTEHfIgl9__NJQZQTkU4WaIAXnEAvr7CqQOXkBzEq7MzkYLwnMGL8Wc1D0cmcvZGcJmvzry_OwltRtWpr7vUuAzUatoozs_Fj0E3UqUFNV_BOaYc5SOWNDQKSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۱.۳۴ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/126723" target="_blank">📅 11:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126722">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزارت امنیت داخلی آمریکا: بازیکنان تیم ملی ایران مجاز خواهند بود یک روز قبل از هر بازی وارد خاک آمریکا شوند و در هتل‌های تعیین‌شده اقامت کنند.
🔴
این تسهیلات به درخواست ترامپ صورت گرفته است و دیدار ایران با نیوزیلند، اولین فرصت برای اجرای این برنامه خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126722" target="_blank">📅 11:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126721">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
سفیر پیشین آمریکا در اسرائیل: وقتی به آنچه در خاورمیانه می‌گذرد نگاه می‌کنم، می‌بینم که اوضاع همچنان آشفته است.
🔴
اختلاف نظر بزرگی میان اسرائیل و آمریکا وجود دارد و کاملا روشن است که دونالد ترامپ مدت‌هاست آماده پایان دادن به جنگ و رسیدن به نوعی توافق با ایران است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/126721" target="_blank">📅 11:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126720">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
پولیتیکو به نقل از ترامپ : با وجود حملات تلافی‌جویانه بر سر سرنگونی هلیکوپتر، توافق با ایران «همچنان نزدیک است»
🔴
ترامپ با وجود حملات تلافی‌جویانه ارتش ایالات متحده در واکنش به سرنگونی هلیکوپتر نظامی در دریای عمان همچنان مدعی است که دستیابی به توافق صلح با ایران در دسترس است.
🔴
مقام‌های کاخ سفید با تفکیک مسیر نظامی از مسیر دیپلماتیک این درگیری‌ها را صرفاً دست‌اندازی در مسیر مذاکرات می‌دانند و معتقدند همزمان با پاسخ متناسب نظامی می‌توان به گفتگوها برای بازگشایی تنگه هرمز ادامه داد.
🔴
این خوش‌بینی رئیس‌جمهور آمریکا در حالی مطرح می‌شود که تهران با لحنی تهاجمی از آمادگی برای تداوم درگیری‌ها خبر داده است اما تأکید مستمر ترامپ بر نزدیک بودن یک توافق قدرتمند نشان می‌دهد که دولت او همچنان اولویت خود را بر مدیریت این تقابل و رسیدن به نقطه تفاهم در روزهای پیش رو متمرکز کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/126720" target="_blank">📅 11:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126719">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
منبع آگاه نظامی: ایران با استفاده از موشک‌های دوربرد سوخت جامد خیبرشکن، آشیانۀ جنگنده‌های اف۳۵ آمریکا در اردن را هدف قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/126719" target="_blank">📅 11:01 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
