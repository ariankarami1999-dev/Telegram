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
<img src="https://cdn4.telesco.pe/file/ZtlW37VfZnXBGn-pDwlfbQ-QbkcxYOJrrZO8qIVSPbMekE_Mkmaz6TFb_Bk7NrtTmQBssp5kAoKY3iTAw1LvbMbtVv74rIk2GpZ7DFJmVKMZiI3hwsFiB5gVG-FThpN67aZZeqQs438s_qm-rtaQRaW9SRJ9Ukrj0VbKclcAzEbYfCJbNEomI-EuV7zduPiSOy1dTFm7_KCzL8kf8pK1Qa3VnMght3UQK58_PiVn63vdcRQ9lM-j_1A1X_BaSQtSQ-td8TUwwNwHfTlCPLQO6aSs42qk81A8vOQCWLWKZqTmB__Mvkd5UYvyn9mBbp48SW6ut3UkPCSKipNMHMd1Dw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 964K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 23:42:23</div>
<hr>

<div class="tg-post" id="msg-129001">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
سفیر پیشین روسیه در ایران: یادداشت تفاهم ایران و آمریکا یک پیروزی تاکتیکی برای تهران بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/alonews/129001" target="_blank">📅 23:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129000">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHoNcmxSyxydfCOnn3JekVxkmcLus8YMbvmjdPK3oLT4D1hWVEWFhnbCmxrE760WXvIWwdwuEstN93pgcTkQslGRqrCrKmRQX2uom3l6bWllCn8DwYGvuZ9qICD_qoOXBfR7iDt8ky3v5OgQAoVbHb6qEeGa1DY1YR2boAm0rVp11scNz4kFmx0A3BlxuDvLNvuqUIZ5BeUVV5MaID0BDPvKE9oFHXdvv3cr110FnjGVx35nNG0gUfZ6iBK6e3mmcyBceHzkPfC3gjrT3R2F9ZIqdaZtRfZ9rQk0d92jzgGo6Wg-OFdOnP8GBmss2aV2pS9kCBXyfGk8a4TNuKr0UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شریعتمداری: شهید لاریجانی دنبال این بود که حساب گروسی را برسد؛ اما جنگ شد و کشته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/129000" target="_blank">📅 23:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128999">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/L8WkO4OeSiWpSS2vts_HpKBP8-9vk5IaxkL6-et5U3WODywxT5W07d7caAJPKpjEgLlAhH1jCRQE4RfqDNYbrD4SB9VglXZjEp2G8vDHhrDL64FRJq2D2wDrcQWLLD2Fw-YSPos8E99isjBf5Ojomb0Dz_D9uV7c8p37RyyTFgCkZkflngRASrMc3stgdebeNO-k2AbG0LpN8HsB8ZZQ0PaATEXfWvxRZc96zlVvlU3p7xFx4AUwwP-mFBv90ExMq-a4J-4BU3b1gnYi1N3sLIz-8Nt9JGyypqYbVa3Gga_LIM96quPbDHZ3nAAMY0a8GNR8qbaFRY32ZnfRfCXGGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه مدارک تحصیلی معتبر از «دیپلم تا دکتری»
🎓
مدارک رسمی و معتبر  هستند و قابلیت استعلام  بصورت نامه نگاری و آنلاین از سامانه های مربوطه را دارد
قبل از پیش پرداخت ثبت نام شما انجام میشه و تاییدیه سنجش دریافت میکنید
سپس پیش پرداخت واریز میکنید
✅
مؤسسه راه سبز تنها مؤسسه صدور مدرکی هست که رضایت ویدیؤیی متقاضی هارو داره
صفحه تلگرام :
t.me/+2yeLgZeivDkzNDYx
وب سایت :
Rahe-sabz.com
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/128999" target="_blank">📅 23:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128998">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
مسئول سیاست خارجی اتحادیه اروپا: ما تحریم‌های مختلفی علیه ایران داریم. اگر توافق هسته‌ای وجود داشته باشد، فکر می‌کنم کشورهای عضو اتحادیه اروپا در مورد این لغو تحریم‌ها بحث خواهند کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/128998" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128997">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08672f5757.mp4?token=a5DKrKGKGdW7VGSrJ1DSK9GAy_LqplnGEJeeQZAJKk9UQ2U_Eb7mDw7R6xk85C48n7DRC8Cjv2zIwOi5SRrmo1K3nxq6jkFmPNvDFZ-WeYcwGkX3TDguKEk1xgNAAu7BUXahvN3est9BHLrZ9y3doql_ITgJT-t8kesg72fGlm60B1h8byJbwAGxWS-SrhrzZ4PhJ5oflKDVN-oFUuWxupizFWicvDwoiUctCE9kQOBdXzkrT1_FBIFbnnLYV2pmVeBlQ54Fs-vaAKEi5-CWHmmj7mX_cioU1QYWcXSCcJSqQbbbLWmMTkMrweAL4hxantl48_KyKyR_l8gfBQJVgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08672f5757.mp4?token=a5DKrKGKGdW7VGSrJ1DSK9GAy_LqplnGEJeeQZAJKk9UQ2U_Eb7mDw7R6xk85C48n7DRC8Cjv2zIwOi5SRrmo1K3nxq6jkFmPNvDFZ-WeYcwGkX3TDguKEk1xgNAAu7BUXahvN3est9BHLrZ9y3doql_ITgJT-t8kesg72fGlm60B1h8byJbwAGxWS-SrhrzZ4PhJ5oflKDVN-oFUuWxupizFWicvDwoiUctCE9kQOBdXzkrT1_FBIFbnnLYV2pmVeBlQ54Fs-vaAKEi5-CWHmmj7mX_cioU1QYWcXSCcJSqQbbbLWmMTkMrweAL4hxantl48_KyKyR_l8gfBQJVgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در جریان حمله امروز صبح پهپادهای اوکراینی به پالایشگاه مسکو، یکی از موشک های پدافند هوایی عاجز از رهگیری پهپادها دچار سردرگمی می شود و بسیار دقیق یکی از از مخازن سوخت را منهدم می کند !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/128997" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128996">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
شریعتمداری، مدیر مسئول کیهان: با مصادره اموال آمریکایی‌ها و متحدانش از طریق تنگه هرمز باید غرامت بگیریم از آمریکا
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/128996" target="_blank">📅 23:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128995">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
المیادین به نقل از منبع آگاه: هیئت مذاکره کننده ایرانی سفر خود به سوئیس را به دلیل تداوم حملات اسرائیل به جنوب لبنان متوقف می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/128995" target="_blank">📅 23:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128994">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d437a78db.mp4?token=d-Rz6FNGZGj31kzROfCyAF_InXbowIjFX44Yonpvu_jdVgTFkeo5Qeo9DYpn3A-cwn3GEcmqLnenWBgGN0WTLzF2RFn7K9rxRuKnZOyqjVbRvVVNKIpfzCIeJ784zxz6c6M3TKk6-T9RtzlKXhdS7JZf8ltbc3dtnjopGmCB8_Z-GrPYDpz6VzAQoi1TCd0vMu1HF9oiuHb-tefhpX25Apu92FbSIUPzE4CZaRfJQTlodD9KVFZ2CbIWBhFMDaZsMXGdLO3ROu1dCTkarXG8EDch3Z8aGDCDhiQpnzRI_yMr15f2X5r8qrhwdl-or_oDFfiJfLVHvmuaFFpu6mzAjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d437a78db.mp4?token=d-Rz6FNGZGj31kzROfCyAF_InXbowIjFX44Yonpvu_jdVgTFkeo5Qeo9DYpn3A-cwn3GEcmqLnenWBgGN0WTLzF2RFn7K9rxRuKnZOyqjVbRvVVNKIpfzCIeJ784zxz6c6M3TKk6-T9RtzlKXhdS7JZf8ltbc3dtnjopGmCB8_Z-GrPYDpz6VzAQoi1TCd0vMu1HF9oiuHb-tefhpX25Apu92FbSIUPzE4CZaRfJQTlodD9KVFZ2CbIWBhFMDaZsMXGdLO3ROu1dCTkarXG8EDch3Z8aGDCDhiQpnzRI_yMr15f2X5r8qrhwdl-or_oDFfiJfLVHvmuaFFpu6mzAjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین پاسخ پزشکیان به بیانیه مجتبی:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128994" target="_blank">📅 22:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128993">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIFrX3BifHMXFSGLrujkwBm5K7_sM4LywaWdM_WoGL7a2gCCZG9vI3Nz67TTD4eEOJKfekTIhwjJPwpfYu9EakDvQv7uHn6nSF87e-6nwWqT6rOkE-zi4OO7YI7kcaL1W8SVsQXTbvJd4y99EyAL8zRapOc_SSifu_1ZjtyEMYhsLnY27ssGQn0gXh39kyhdWEkHyWpWs0i-g1JzGPhMOahO473t23DLPT1J3iQoEpPMlTkpFpgRw7vJ3CJy67up8UJS4AFpbdJGpG7266e4w3D40oqSifHJuv7HaSJ7QYsl80ffVGPc1MK-I5P-oNwB_4Zb3cL10t_2n1Bf06_Rlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: شرافتمندانه نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128993" target="_blank">📅 22:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128992">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
رسایی :  باید پزشکیان رو اعدام کنیم.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/128992" target="_blank">📅 22:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128991">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
شریعتمداری، مدیر مسئول کیهان: با مصادره اموال آمریکایی‌ها و متحدانش از طریق تنگه هرمز باید غرامت بگیریم از آمریکا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128991" target="_blank">📅 22:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128990">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTCWpxuHuhWTkB7KTQ9KATzDHb1fID769zp-m9u4LhRQKV2SJkee3C688SUM3s6ijT9q__EeBDyCf7aSDaF8y63N6jsGQVhCAhYQpHeG1AkgB5-5HWkF8uhDLlybqPnAC16hdY-RjK8vWFVNtsM1jtgCOuYkgBJWMnMH3SoYZoEP4n1lIUdFFcL68Wfq76S7O2V_kvzjFe6aUYuuklAQPImOyGg2g8gOEZErz0sg2UO9EoGUy7bwy2qXUHg27u0XSvb6H5frxLE1KlyzD-mXf0ht4JGviqm9b_d7f2nvo3SidpQDMoRMywKi-LVgWs_J_bKfmDM-4XzAit7zEdWynA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی :
باید پزشکیان رو اعدام کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/alonews/128990" target="_blank">📅 22:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128989">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReWBxRbdkMtY4k9S7y8iJaW5hecCzxyj4iAGnSF1RMfngB6mCItwbYkW3OuJW1i5g58zdpGjdIF3KG0qQdLll2Yb3ol601ysDemMjCO0ygy1bcC8KO9t9mLgjhN5cdAGxTp6aKN4kTvztoa1B0MWD9xYZNLboO7tV__BNabv-Xk81frHUAhn5zXSL9VAsVEa1NfqeEZYnRNDRgYEnCmjbw1Bzw25xY-a-5yBSazBNwNg03cFMpFbJuNMNTGPJJPYwLqSgv5fHi6V59NBl0xi3WPbVMK4B_a-GtEFKswdjbHAV2xNjkEfV-vyqmKHEh5JVF_Jg8WudgoBV6vhr4X9AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما مجتبی‌ خامنه‌ای با تفاهم‌نامه را زیرنویس کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/alonews/128989" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128988">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/شورای عالی امنیت ملی: بر اساس تفاهم‌نامه منعقد شده، تا ۶۰ روز هیچ‌گونه عوارضی از کشتی‌های عبوری از تنگه هرمز دریافت نخواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/alonews/128988" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128987">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bW7vZfnGdgIUQlgNBQQlXxesXZShp9XctTFyxqmtLzBYSY1pDtqpNXg74Rii1TCkwfWk41zrOr67jO0_R5D7OkNXpZP8aPBb7lqjb1Zcnv-UWsU_yNdDBGnKYu8qxLtnyfTOVZE_SXEbPQ8coiXQ-bMwD22xg5h3lVOchSX52iB8amv7fEjm8EEWyikY5BksIQXRV_LAHzx3EY86hWyNfgkZANImrdcDakBMUKJlW_E67SmkQl4oIA6cCM3AQURB1wHympHPxDrePT7vwgFdl8hKq9CAND30klPcCq4lW2EL_C9hvKEMcVIYfep3wSNhcnAM6DwlX2b4ZAk7jycMwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حساب رسمی کاخ سفید در X
:
ما واقعاً آمریکا را قبل از GTA 6 نجات دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/alonews/128987" target="_blank">📅 22:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128986">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ: «ایالات متحده به صلح متعهد است، و ما از همه در منطقه خاورمیانه می‌خواهیم که به تعهد خود برای اجازه دادن به روند مذاکرات ما تا به شکلی عالی پیش برود، پایبند بمانند.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/128986" target="_blank">📅 22:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128985">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4qivLTGTyEzpEZG-lnvf1r37IJU9XXWrKTu-fchzVu3BZy_sjBrW43dppnAThjVardtqH6UN8tVRjxGfgGdnMPDE7x5g0a3X8cqf_HDNW9y0d0l6FLJEvoGoIumECduyreQkVVpNgOT6e1IFJPICcgelXiHxedMEFHU63x86ApKB7xA3whYYjJqMRNegmqD19In36fUy7PZC8pF15kZLOZCCK1NUpOgEfkF_Omc0IZCejqQwvSM9Yd1YVkSh_wLNjDl_xkhPKA9rJrO-f9YNUfq75we3QW_KFzPrOderc9gItPZcfGdzViAuQZJJ0d93GqrNkCiGmx2pmTjgJ5uCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کسی خبر داره ازشون؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/alonews/128985" target="_blank">📅 22:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128984">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9sLAYDfd07OJc26MCDbbirHF2KJUoOIm37WSIch_51L_PLwI9PehrS5vthrTinINW8VAF8KdcH-13wjiHJjxk9TixeKEn4F18Xs3sWQRGSDE9YaTAT_-AZ6bSQQ0nPLLp8fw9fZh-CDzU4H_MXGL4WQvxXfOhHRoxu0AmGzJoyHFU1fvxEY8US8ytaou6qSp5BzGoWt6H9RlhNmUao9xOrjJ6hBjPtTA70YjMOeMgY8Z_NcnRfz54No16waA4rekwW0tqcDaQov7INTqCCGJ8DlPc5kXxj-MjFncKhJ2WNnmZPLk11uaAixb8i-mlkGXwg5_Wu44oXG7rfXB8oj0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد از منطقه‌ای که در نقشه با نوار قرمز رنگ مشخص شده، عقب‌نشینی نخواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/128984" target="_blank">📅 22:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128983">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
طالبان  به دلایل مختلفی مثل جلوگیری از درز اطلاعات محرمانه، کاهش اتلاف وقت کارمندان و کنترل اخبار اعتراضات مردمی، گوشی‌های هوشمند را برای کارمندان دولت افغانستان ممنوع کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128983" target="_blank">📅 21:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128982">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
فارس : تیم مذاکره‌کننده ایران تا حصول اطمینان کامل از توقف حملات به لبنان، هرگونه گفت‌وگوی تکمیلی را به حالت تعلیق درآورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128982" target="_blank">📅 21:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128981">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
آسوشیتدپرس: کاخ سفید توافق با ایران را به کنگره ارسال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128981" target="_blank">📅 21:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128980">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ: «ایالات متحده به صلح متعهد است، و ما از همه در منطقه خاورمیانه می‌خواهیم که به تعهد خود برای اجازه دادن به روند مذاکرات ما تا به شکلی عالی پیش برود، پایبند بمانند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128980" target="_blank">📅 21:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128979">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: انتظار داریم میان اسرائیل و حزب‌الله هم آتش‌بس کامل برقرار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/128979" target="_blank">📅 21:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128978">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
رهبری سیاسی اسرائیل به نیروهای دفاعی اسرائیل اجازه داده است که در داخل «خط زرد» در جنوب لبنان تیراندازی کنند، طبق گزارش کانال ۱۴ اسرائیل.
🔴
انتظار می‌رود مقامات ارشد نظامی در ساعات آینده قوانین درگیری و راهنمایی‌های عملیاتی به فرماندهان میدانی را به‌روزرسانی کنند.
🔴
این تصمیم همچنین شامل برنامه‌هایی برای نابودی هر «زیرساخت مرتبط با حزب‌الله» است که در داخل «خط زرد» شناسایی شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128978" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128977">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری / رویترز: کاخ سفید متن توافق با ایران را به کنگره ارائه کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/128977" target="_blank">📅 21:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128976">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bec225d06.mp4?token=ngiaG5hvFMbXV3G7T-bjw-kfCwOO22wlO8MQtENDjaX5vBvbZV8JJctVfMIJddzFOcHAQtwnDhoNS5iHaF9tkruGBGu3Kwwe3CiCPqJsTY5p8eDAK_N4j09KumqU25s-Fq-qzK92g03fYkvPhN_wabnXLqlQP1DVJaBuM7jVsCG0ZHr5xv8LK6YQRkiOPa3EkjXRmb4bK4bmS7V1ZaiOn0uO9_qRxjBPjLfw_aTQJN5W3KEm5XbWe5Dbe99TQXU3j_QP38bu5qk1MASnTWoL2kLhpu7WBa7Q0mYLjhNqNc_ckaXRvts8_eHEFCp-1qFeQHSHSosPYnTd46mBjaywZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bec225d06.mp4?token=ngiaG5hvFMbXV3G7T-bjw-kfCwOO22wlO8MQtENDjaX5vBvbZV8JJctVfMIJddzFOcHAQtwnDhoNS5iHaF9tkruGBGu3Kwwe3CiCPqJsTY5p8eDAK_N4j09KumqU25s-Fq-qzK92g03fYkvPhN_wabnXLqlQP1DVJaBuM7jVsCG0ZHr5xv8LK6YQRkiOPa3EkjXRmb4bK4bmS7V1ZaiOn0uO9_qRxjBPjLfw_aTQJN5W3KEm5XbWe5Dbe99TQXU3j_QP38bu5qk1MASnTWoL2kLhpu7WBa7Q0mYLjhNqNc_ckaXRvts8_eHEFCp-1qFeQHSHSosPYnTd46mBjaywZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
داده‌های جدید نشان می‌دهد که ترافیک دریایی از طریق تنگه هرمز پس از تفاهم‌نامه ایران و آمریکا از سر گرفته شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/128976" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128975">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_A0IWcGsQeVC4a0rqSG2aZ4oEPECQAGatgLQedTLerviliybBlfOZspu8KBuFzeDUQ5yLZoQkyPbfk0WA9VzKN7ByMweVxK0OGOl4HCiPloNm-9a4PDxBHlcAUskqaGMXx1Uhn0aoVGE2PNFMNfwhD1yn-JS83a5t_CHfjRu_eUvS01h3csbW3OS8e3lsJ_P4d7OVRnhIFD5NuZomOBkuqeavSS-U2T2Vv58i7Bt6GT8ckY049RLElFuhCLDJlWbCG-RMQTS1f4UD255PjOw3_bvu4j22LTf1UcsQxu7Cz1bC1mEmltn9QYINqBjC-B2Puz2rdwl9KRFkAnQXAN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فارس:  پیام جدید رهبری منتشر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/128975" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128974">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-51rL8JuYNVdAf3hkPFi3e4pDuSsLoDcdDv3TTxpEu1GkJ7yAJqsmZgb0law4b1bBFnik7MRJLYKBe19-V16Ld2UoYqZ0Yu0loGEfT0Gahlfx48OZCbok8SdVVQ35q7hmIKK7cTQZOJyPd6sLXEeZqbSCydUJWJlHtDI_hsdfN9Hd9AiVnb3kFRJW_t3tjCznaGDTAx-iLMfVDGWSl2OrdF-4x4gJPTFdPfs04iZgYs9UkxVlpYVFSW_C3kzRYxls-WIZ23MhdsniuOZIOkPCdtSAPGC9khHVx4eUpjko9Tzw5yammNee8RCJFryNJNsC7YpgtgxXocp1XuXCweYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین به زیر ۶۳,۰۰۰ دلار سقوط کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128974" target="_blank">📅 21:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128973">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فایننشال‌تایمز: طبق توافق آمریکا و ایران، ایران به تدریج به ۶ میلیارد دلار از دارایی‌های مسدود شده خود در قطر دسترسی پیدا خواهد کرد
🔴
این پول فقط می‌تواند برای خرید کالاهای بشردوستانه و سایر کالاهای آمریکایی غیرتحریمی استفاده شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128973" target="_blank">📅 20:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128972">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
خبرنگار : چه کسی آن صندوق ۳۰۰ میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
🔴
جی.دی ونس : تمایل زیادی از سوی جهان عرب و همچنین از خارج از جهان عرب وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128972" target="_blank">📅 20:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128971">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری / رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله به ایران و حزب الله آماده شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128971" target="_blank">📅 20:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128970">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
جی دی ونس: نتانیاهو بهتر است بداند بدون ترامپ و آمریکا قدرتی ندارد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128970" target="_blank">📅 20:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128969">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
ونس: تعداد نیرو‌های آمریکا در خاورمیانه را به سطح پیش از درگیری باز می‌گردانیم
🔴
برنامه ما این است که به سوئیس برویم؛ دقیقاً نمی‌دانم چه زمانی
🔴
درباره تأمین مالی صندوق ۳۰۰ میلیارد دلاری، تمایل زیادی در جهان عرب و خارج از آن وجود دارد که درگیر سرمایه‌گذاری در ایران شوند
🔴
در سه ماه گذشته، دو سوم تسلیحاتی که از اسرائیل محافظت کرده‌اند، با پول مردم آمریکا تأمین شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128969" target="_blank">📅 20:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128968">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
وزارت خزانه داری آمریکا تحریم های جدیدی را علیه حزب الله اعمال کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128968" target="_blank">📅 20:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128967">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw8DOvv5KboeYqXG9q-Q166BDF26lMQ72vaYC-Om7xOEqvoN4ni4WE35qkigFdVhdi1VMj4UhjiYdPxhQ81Gj7Y7tHpX5-_NB_RSyr-1NUcMNLcMxfwPB4qoyrfVVl7jC4-y_KAuxXVPT6qPABx_K98_iZE-dl-suN1A9T0XsmCS-EvaITanIcyu9fS_cbFze9frrYwrp0k5oIAOKLC9AQfnqruMCR8wGVdkvzQ9g43Mi3oxIvSFebIGX450nwv8UMOOfa94Zbz_vX-E0Ff-taEpou9TfbFxqtV-57Jh9FaQPyjAZzKADnHDVZMvrGMtxle1FlZp6fZrEM_Jdif8cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / سنتکام : امروز، نیروهای آمریکایی بر اساس دستور رئیس‌جمهور، محاصره دریایی تمام ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128967" target="_blank">📅 20:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128966">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نرخ دیه سال ۱۴۰۵ اعلام شد!
🔴
رئیس قوه قضائیه با صدور بخشنامه‌ای، مبلغ دیه کامل در ماه‌های غیرحرام را برای سال ۱۴۰۵ تعیین کرد.
🔴
بر اساس این بخشنامه که در اجرای ماده ۵۴۹ قانون مجازات اسلامی مصوب سال ۱۳۹۲ و پس از انجام بررسی‌های لازم صادر شده است، مبلغ دیه کامل از ابتدای سال ۱۴۰۵ در ماه‌های غیرحرام، ۲۱ میلیارد ریال تعیین شده است.
🔴
این بخشنامه از سوی رئیس قوه قضائیه به مراجع قضایی سراسر کشور ابلاغ شده و از ابتدای سال ۱۴۰۵ ملاک محاسبه دیه خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128966" target="_blank">📅 20:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128965">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/le5y6NkIsyEHLWJCmPamzajrRTleSud9pGV_Tw1mPryWH9rIvYIituPoNfZLQR7MuG0t2biwAsmQoRv6OkQU3y4rpneK6umO3yamjmNigK8irbqL-Krpvv27-phEmSqGtbVLL4c4kNlWkycmSrHC7BZP0Z-_ZD5MW4tjv7CFjsQIqwE-HWzdVZpcAuGjzsCGWQD2_B_oficPHku_V0cU_gvjB_polmaXCl7Ainn21aEhOOSLT8RF2w9CbPbu65GouBsoDfptNUQabDXhBGfivlOHz_FC4WUMQipKBh-LH6Pqe5NOaEdOLW8qkLlG5A8IeCxftqDcZIpWpM5RmVRsrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: هیچ پرداخت ۳۰۰ میلیارد دلاری از سوی آمریکا به ایران وجود ندارد. این اخبار جعلی است! همه چیزی که آمریکا دارد، موفقیت، کاهش قیمت نفت و پیروزی است. به بازار بورس نگاه کنید. تبلیغات دموکراتیک در حال اجرا است!!!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128965" target="_blank">📅 20:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128964">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ونس : من تنها کسی در کابینه هستم که نمی‌توانم اخراج شوم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/128964" target="_blank">📅 20:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128963">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
من معمولاً نسبت به درگیری‌های نظامی بی‌پایان بسیار بدبین هستم.
🔴
فکر می‌کنم این مورد متفاوت بود چون واقعاً هدف مشخص و پایان روشنی داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128963" target="_blank">📅 20:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128962">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b7e326eb5.mp4?token=Zget0VgOu4B_4w1ej_qxGHfm8OV98iV5txCb3CpZ6R6DWNAbmo1jsFAcH79Z9pAr3sXu7At9cjgHbmIA3ylUsJQolXpRUwejTBKUhuEjU574COIs63sYseU0VRO0S6_jNgYLe4Y72eH8XxNChhRdhUiip-DeH0bdMUKJg5oLPDYr-5LjBSAflkrV_VB8BDy48UXxQ_07KRP3PXDvRSVePHivBM6MRJAuJTpiVE75i1tYGXuW-fB54ng4m_hUBSnYIrsCzcN9ZkvXliCLx2BineIWmOnyc6ViIA_aiVc5os03ZLOu65mrvDdp9dIrR5WFS1zlOj6CeRSTHeSkmWG9zDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b7e326eb5.mp4?token=Zget0VgOu4B_4w1ej_qxGHfm8OV98iV5txCb3CpZ6R6DWNAbmo1jsFAcH79Z9pAr3sXu7At9cjgHbmIA3ylUsJQolXpRUwejTBKUhuEjU574COIs63sYseU0VRO0S6_jNgYLe4Y72eH8XxNChhRdhUiip-DeH0bdMUKJg5oLPDYr-5LjBSAflkrV_VB8BDy48UXxQ_07KRP3PXDvRSVePHivBM6MRJAuJTpiVE75i1tYGXuW-fB54ng4m_hUBSnYIrsCzcN9ZkvXliCLx2BineIWmOnyc6ViIA_aiVc5os03ZLOu65mrvDdp9dIrR5WFS1zlOj6CeRSTHeSkmWG9zDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: ایرانی‌ها پیشنهاداتی ارائه می‌دهند که حتی شش ماه پیش هم در حد رویا بود. پس بیایید این مذاکره را ادامه دهیم.
🔴
ببینیم آیا اقدامات ایرانی‌ها واقعاً با گفته‌هایشان مطابقت دارد و کمی به ایالات متحده آمریکا اعتبار بدهیم، کشوری که به نظر من مدت‌هاست شریک فوق‌العاده‌ای برای دولت اسرائیل بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128962" target="_blank">📅 20:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128961">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ونس: مقدار دقیق دارایی‌های مسدودشدۀ ایران را نمی‌دانم
🔴
اعدادی بیش از ۱۰۰ میلیارد دلار شنیده‌ام. حتی اعدادی بیش از ۲۰۰ میلیارد دلار.
🔴
بخش عمدۀ این پول در حساب‌های ایالات متحده نیست؛ بیشتر آن یا در کشورهای حاشیه خلیج فارس است، یا در اروپا، یا در جاهای دیگر.
🔴
اما مقدار دقیق این پول را نمی‌دانم؛ فقط می‌دانم که رقم بسیار بزرگی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128961" target="_blank">📅 20:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128960">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e65fb14352.mp4?token=QchKiwy9vb176QOdPU6knR5yaXIGzNAVIvCgTMI6DTkH8yvXiIDHJZ8mCa0qvxIBgFcZolpxD3aUTBRSfsM49pw4bun62keu2AvQNYH90IIi0A-eQcC01DyDn442jqN5tkia1NHkfov_Qb-147c7cLLWyGQtqtGaiNp1HRrL7h-LT3tJ_-QhwTULzhClQoznY2gVzSRtoBTJKAucDEl0q9V6hwLCxW4xd05ncMEWb73f-P8Z3nnEmV32-4eTtJsjVm9eIEeM6gy87WOwnvlz55-Fw0cpPkJpu-NVlyCeVJV4hdW5QaapMq-y_5nqiH01Q3I4qUZqUfgQDG6R_w4qzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e65fb14352.mp4?token=QchKiwy9vb176QOdPU6knR5yaXIGzNAVIvCgTMI6DTkH8yvXiIDHJZ8mCa0qvxIBgFcZolpxD3aUTBRSfsM49pw4bun62keu2AvQNYH90IIi0A-eQcC01DyDn442jqN5tkia1NHkfov_Qb-147c7cLLWyGQtqtGaiNp1HRrL7h-LT3tJ_-QhwTULzhClQoznY2gVzSRtoBTJKAucDEl0q9V6hwLCxW4xd05ncMEWb73f-P8Z3nnEmV32-4eTtJsjVm9eIEeM6gy87WOwnvlz55-Fw0cpPkJpu-NVlyCeVJV4hdW5QaapMq-y_5nqiH01Q3I4qUZqUfgQDG6R_w4qzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو پربازدید از یک‌ مخالف توافق بعد امضا
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128960" target="_blank">📅 20:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128959">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ونس: امکان تعلیق موقت تحریم‌های ایران بدون مصوبه کنگره وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128959" target="_blank">📅 20:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128958">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ونس درباره نتانیاهو: من گزارش Axios را دیدم که می‌گوید نتانیاهو عصبانی است.این بازتابی از گفتگوهایی که من با او داشته‌ام نیست. شاید او چیزی به شخص دیگری می‌گوید که به من نمی‌گوید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128958" target="_blank">📅 20:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128957">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
اننقاد تند جی. دی. ونس به بن‌گویر و اسموتریچ: شما افرادی را در ساختار سیاسی اسرائیل دیده‌اید، بن‌گویر و اسموتریچ، که به این توافق حمله کرده‌اند.
🔴
و فکر می‌کنم پاسخ من به آن‌ها این خواهد بود: پیشنهاد دقیق شما چیست؟
🔴
شما کشوری با ۹ میلیون نفر جمعیت هستید. نمی‌توانید صرفاً با کشتن، از پسِ حل تک‌تک مشکلات امنیت ملی‌تان برآیید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128957" target="_blank">📅 20:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128956">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
فارس: پیام بسیار مهم رهبر انقلاب دربارهٔ تفاهم پایان جنگ، خطاب به مردم ایران، تا ساعتی دیگه منتشر میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128956" target="_blank">📅 20:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128955">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18aeee1535.mp4?token=IkK7YY7lhTwqOZTNemISRjZPmqV6SeLRykhi54cpjxrxypMN3cy9Hr1DEOJILJzr2WWlMGN6EBhS8BiCs0FMZvmXWYvPsGbBqZ1TzTOcc2A4mKhOZoUsPfdk_n1PrrVtUVejyk8o4SftcrV0XVbDyLNoLNVo2KWKTsAQtpVq_Smw8CoWZ1e0eNBqlQJFjJPMy85HnSzDc-twrOF57Z7iXpeGv_rmow7wIoXI4nOuNShPpy3osGwJWyT-P-soICYyh3bBSqheBCgCA3_OZgUUi_BeUK4S6-UpH3r8-vSA4FT0SinzBdauwqIYG5L1vABZwP5xrGTKorrOtEOIjj03dKO7px7ySbns90dFQgmD6gHYPWaJsPfmFJF2mPNQapirydy_JVP-S9uyQgxXkKquGnorgu53f-MSKqixUYZaQ2wnpe8Xu_izCePNRXA3W6_Bw89FKWFcETT8iK5509J0B5-fzB2h_0O7XRHK3M1tzby6aYuFhKIPXgVonr_KE0AJz1I0M9Dy3-ZwCpDM7DIIsCyfhzxMSfUM4YfQJZcCkW6JoQhA_MUe1hx2PB2GFjvrXhqeEqWsG_w82DiifXP-6qnnX2LEDBeYtQYqqBeHGowgL1GuidDzjBjJvZrN6xPmSWspI0HB0alNOeaulU3FGZwV_7hdQN8aJrsBFvjXt5M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18aeee1535.mp4?token=IkK7YY7lhTwqOZTNemISRjZPmqV6SeLRykhi54cpjxrxypMN3cy9Hr1DEOJILJzr2WWlMGN6EBhS8BiCs0FMZvmXWYvPsGbBqZ1TzTOcc2A4mKhOZoUsPfdk_n1PrrVtUVejyk8o4SftcrV0XVbDyLNoLNVo2KWKTsAQtpVq_Smw8CoWZ1e0eNBqlQJFjJPMy85HnSzDc-twrOF57Z7iXpeGv_rmow7wIoXI4nOuNShPpy3osGwJWyT-P-soICYyh3bBSqheBCgCA3_OZgUUi_BeUK4S6-UpH3r8-vSA4FT0SinzBdauwqIYG5L1vABZwP5xrGTKorrOtEOIjj03dKO7px7ySbns90dFQgmD6gHYPWaJsPfmFJF2mPNQapirydy_JVP-S9uyQgxXkKquGnorgu53f-MSKqixUYZaQ2wnpe8Xu_izCePNRXA3W6_Bw89FKWFcETT8iK5509J0B5-fzB2h_0O7XRHK3M1tzby6aYuFhKIPXgVonr_KE0AJz1I0M9Dy3-ZwCpDM7DIIsCyfhzxMSfUM4YfQJZcCkW6JoQhA_MUe1hx2PB2GFjvrXhqeEqWsG_w82DiifXP-6qnnX2LEDBeYtQYqqBeHGowgL1GuidDzjBjJvZrN6xPmSWspI0HB0alNOeaulU3FGZwV_7hdQN8aJrsBFvjXt5M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انتقاد ونس به اسرائیل
🔴
ونس : در سه ماه گذشته، دو سوم از جنگ‌افزارهای دفاعی که از اسرائیل محافظت کرده، با دستان آمریکایی ساخته شده و با دلارهای مالیات‌دهندگان آمریکایی پرداخت شده است.مشکل اسرائیل دونالد جی. ترامپ نیست، و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلشان رئیس‌جمهور ایالات متحده است، باید بیدار شود و واقعیت وضعیتی را که آن کشور در آن قرار دارد، حس کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/128955" target="_blank">📅 19:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128954">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7cd6ba7c.mp4?token=t2Dkk6d3HsnMsjeeSRNJcxEAHYUIKIbq-UjHkOdH3zM3XfhEO5diixwF0FS-nM6Y6ZZhSx1kVdZDEGVEp8x4BPVe669-V9CvGKr4vrhfmwQjpPDcrzljFF-AOYbRiBHQQBBz_aCKelMjTUUEBLpNKwdSegeKfbcYYLxFlyCitISpndFBF8_QyXVt4P_GcOJNtRBUApzA978b3Fm3byqqnECCNKfjK4af9wi1tjKyFQkIKKHvveWodHqHhabMmaTgp4kNHIQxVC2f_K2pB-fgSVwOQU4hZ4jvIccl8GDVq3zW6UNUtt3d13wb2J4hinoJFyLZkfADQCF-vuFC-hDEQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7cd6ba7c.mp4?token=t2Dkk6d3HsnMsjeeSRNJcxEAHYUIKIbq-UjHkOdH3zM3XfhEO5diixwF0FS-nM6Y6ZZhSx1kVdZDEGVEp8x4BPVe669-V9CvGKr4vrhfmwQjpPDcrzljFF-AOYbRiBHQQBBz_aCKelMjTUUEBLpNKwdSegeKfbcYYLxFlyCitISpndFBF8_QyXVt4P_GcOJNtRBUApzA978b3Fm3byqqnECCNKfjK4af9wi1tjKyFQkIKKHvveWodHqHhabMmaTgp4kNHIQxVC2f_K2pB-fgSVwOQU4hZ4jvIccl8GDVq3zW6UNUtt3d13wb2J4hinoJFyLZkfADQCF-vuFC-hDEQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: چه کسی آن صندوق 300 میلیارد دلاری برای ایران را تأمین مالی می‌کند؟
🔴
جی‌دی ونس: تمایل زیادی از سوی جهان عرب و فراتر از جهان عرب وجود دارد که اگر ایران به‌درستی رفتار کند، واقعاً در آن کشور مشارکت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128954" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128953">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
جی دی ونس: ما یکشنبه با ایران توافق را امضا کردیم اما نمیدانم به چه علت، ایرانی ها از ما خواستند که تا روز جمعه متن آن منتشر نشود البته شاید به خاطر تهیه یک متن فارسی
🔴
اقتصاد ایران رو به فروپاشی است و تورم آن سر به فلک کشیده است و یک هزار میلیارد از جنگ آسیب دیده بنابراین فروش چند میلیون بشکه نفت نمیتواند تاثیر خاصی داشته باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128953" target="_blank">📅 19:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128952">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e45fd9b924.mp4?token=T0szU5E8XsVrxxoH9ruHw9u43qlR2MO1tJNERZxO15FQColB66ckMwIwGFWfZKOEepZaaPK7OVN0sgzivBgvjFwf12ykXl-pYC4H07ZtAefEEI7w7Wre-oA9MCUIbHZFdxel2cgVAsagMYQ0JNJdyE9ebkfJaJV42nCASU2m1KiN6_2OZbLYKWf06zkUI6z8-I2S8QgHcZr8fqvkU-2HwF-QDPaXWg3sdNqPKmsG_a3HOHCwXR-xCkVY0kk1gnynq5G1e9kfb0OvsRsT7cZ5qGGvGUyuQJRn1xcxCNWrwtJbZMkoARX2jWhFWbnVoPm_AV_IbJ6gVVpb3LvSzqatdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e45fd9b924.mp4?token=T0szU5E8XsVrxxoH9ruHw9u43qlR2MO1tJNERZxO15FQColB66ckMwIwGFWfZKOEepZaaPK7OVN0sgzivBgvjFwf12ykXl-pYC4H07ZtAefEEI7w7Wre-oA9MCUIbHZFdxel2cgVAsagMYQ0JNJdyE9ebkfJaJV42nCASU2m1KiN6_2OZbLYKWf06zkUI6z8-I2S8QgHcZr8fqvkU-2HwF-QDPaXWg3sdNqPKmsG_a3HOHCwXR-xCkVY0kk1gnynq5G1e9kfb0OvsRsT7cZ5qGGvGUyuQJRn1xcxCNWrwtJbZMkoARX2jWhFWbnVoPm_AV_IbJ6gVVpb3LvSzqatdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ چند روز دیگه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128952" target="_blank">📅 19:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128951">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
جی دی ونس در مورد اسرائیل: به نظر می‌رسد که ما درست در آستانهٔ یک پیشرفت بزرگ در توافق بودیم، و بعد ناگهان یک انفجار بزرگ در یک منطقهٔ غیرنظامی در بیروت رخ می‌دهد، و تعداد زیادی از مردم که هیچ ارتباطی با حزب‌الله ندارند جان خود را از دست می‌دهند. این قابل قبول نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/128951" target="_blank">📅 19:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128950">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961d1c224f.mp4?token=f0zdeBGEhQZ19iUgTGOzc2Jo8U1JEmxlxMhXZmBM3v3qJQkKjw-kaBlqJ2LJ4o2BbpHH-3eDFmxNcTgTOXxZlt1jNOYfmml0a6nKFPlsI4tpQtA1YZwZs1jBH_xKoKXjXf_ECMpHAyPyoSMM93McuaQbCiID1W38hz7pfxRHYY04c22MxE72FvQbTR2FNh1dwlWMSejb-w91vwjNs087wh9o4ujvDlH_h1KnG05-eycKI4_UyIgQ93bFjK06h2mv8RqIwDIjpOOAtOKXzJDvQ-0rBYSJdYJ9ztn2uFH0Tu0oWHOr5SQnXm2aaAdYtxHNH9xvVAwU-8TFrUbe0PkdKwIAUh8rDAe9k1Q-m_p0hM20ZYAVX84eymA3U571Y8r4BN0hnvfytE3bz6U_qeJNDBgH9PGjEah1QdmmWBKK-IkCHgJCseoZXij72F4xOg_wlBUaXsScdMJ-3Uh9SiIFY5xVlPYwijtv2_BiwTsdMvmhRtbmmlY_ib_p3BpZievo8u00rRT8FnmcMdHryQ2jYH0OgCGr-AdL3kKACZDrIIJYF38ZCd-6RzgHrxUzv5brT5FtvaqjNxRik8799OR3WR1QzMLb_olVo6XAfY6x8B6dfQjOiIPsl8_GiXuvjQeCttHyZtlxk4BlogyPP5S6UuiHGLrf8O3klhRJ03D1mlI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961d1c224f.mp4?token=f0zdeBGEhQZ19iUgTGOzc2Jo8U1JEmxlxMhXZmBM3v3qJQkKjw-kaBlqJ2LJ4o2BbpHH-3eDFmxNcTgTOXxZlt1jNOYfmml0a6nKFPlsI4tpQtA1YZwZs1jBH_xKoKXjXf_ECMpHAyPyoSMM93McuaQbCiID1W38hz7pfxRHYY04c22MxE72FvQbTR2FNh1dwlWMSejb-w91vwjNs087wh9o4ujvDlH_h1KnG05-eycKI4_UyIgQ93bFjK06h2mv8RqIwDIjpOOAtOKXzJDvQ-0rBYSJdYJ9ztn2uFH0Tu0oWHOr5SQnXm2aaAdYtxHNH9xvVAwU-8TFrUbe0PkdKwIAUh8rDAe9k1Q-m_p0hM20ZYAVX84eymA3U571Y8r4BN0hnvfytE3bz6U_qeJNDBgH9PGjEah1QdmmWBKK-IkCHgJCseoZXij72F4xOg_wlBUaXsScdMJ-3Uh9SiIFY5xVlPYwijtv2_BiwTsdMvmhRtbmmlY_ib_p3BpZievo8u00rRT8FnmcMdHryQ2jYH0OgCGr-AdL3kKACZDrIIJYF38ZCd-6RzgHrxUzv5brT5FtvaqjNxRik8799OR3WR1QzMLb_olVo6XAfY6x8B6dfQjOiIPsl8_GiXuvjQeCttHyZtlxk4BlogyPP5S6UuiHGLrf8O3klhRJ03D1mlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی.دی. ونس در مورد لغو تحریم‌ها:
«راستش را بخواهید، ما این را یک امتیاز بزرگ به ایرانی‌ها ندیدیم — ایران هم... این را به‌عنوان یک امتیاز برای خودشان تلقی نکرد، چون چیزی که مانع فروش نفت آنها می‌شد، تحریم‌ها نبود.
🔴
آنها بدون هیچ تخفیفی نفت زیادی می‌فروختند، چون تحریم‌ها اساساً ناکارآمد بودند.
🔴
در آن مرحله، کاری که تحریم‌ها کردند این بود که سیستم مالی ایران را به نوعی به سمت سیستم بانکی سایه‌ای (غیررسمی) سوق دادند.
🔴
با لغو تحریم‌ها، در واقع خواهیم توانست کمی ببینیم که سیستم مالی آنها پول را به کجا می‌فرستد و از کجا پول دریافت می‌کند. این یک مزیت واقعی است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128950" target="_blank">📅 19:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128949">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
جی‌دی ونس درباره لبنان: ما انتظار داریم حزب‌الله راکت‌ها و پهپادهایی به سمت اسرائیلی‌ها شلیک نکند و همچنین انتظار داریم اسرائیلی‌ها در لبنان به شدت عمل نکنند.
🔴
هر دو طرف باید به تعهدات خود پایبند باشند.
🔴
همان‌طور که می‌دانید، گاهی این آتش‌بس‌ها کمی پیچیده هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128949" target="_blank">📅 19:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128948">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98cffc6fa1.mp4?token=ac_Kv4ePSkNWp7gDfRjOAr4llloEVl6PdyXlULui5qA2sozyzS2kpPuzcuRzOmRb-2lJCfgt0T4MaUPPWXb2noECmYleL9SiiWZQyjh88P8SHCZx4T2F90X4p0WQiYXKu2CjHrG35OdXmCJlGlanzd9e5Ln1kMdYjdi718gDxRcQdghl0PoNoXnnHLUbMMskXqKZYVyW_ramcrSrYw_W6Eq1DPC_XX9Zl-PJtJYlPyFhwh-OgkI93ThyoKDU1jTivXcQJtPxPX6xrA8AmEoZL3m_m1uYki-wxUqI2oRiaDlspOk3w57osomhwfEQcpkdFJiOfsY26CmmG9CaxziGe6_UmOg7kbcLMf1QqlwqwyGmxvXx3TLnz-cg33Jn5dynFfHSzcYsaA7ro2UugMEm3X7VfsHdeF0p6jeq68mhomUAiAXXTMsMmO-SGBxXtdwr2kEoU4wxLXCU4SME8rEAh9TnZgJTi4IgmCotOekE5kGIiiTxrsSxeBoK134HuWOeadSRaAPnGiv1Dur3oZteNarv2fMB3monuoxqyBfKZQ8ZuW8aq-XDllvgJJPTo8aTaPStNlCGk_t-W9iiiO8x0SeEuTzH9ww_2W0d4LzPcV6FOHwJ1u32SLWqZOPh_IPPm0k0fBa_940HjAO3U5yPb1F2_IpDFVoQRq1MwxSOmEk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98cffc6fa1.mp4?token=ac_Kv4ePSkNWp7gDfRjOAr4llloEVl6PdyXlULui5qA2sozyzS2kpPuzcuRzOmRb-2lJCfgt0T4MaUPPWXb2noECmYleL9SiiWZQyjh88P8SHCZx4T2F90X4p0WQiYXKu2CjHrG35OdXmCJlGlanzd9e5Ln1kMdYjdi718gDxRcQdghl0PoNoXnnHLUbMMskXqKZYVyW_ramcrSrYw_W6Eq1DPC_XX9Zl-PJtJYlPyFhwh-OgkI93ThyoKDU1jTivXcQJtPxPX6xrA8AmEoZL3m_m1uYki-wxUqI2oRiaDlspOk3w57osomhwfEQcpkdFJiOfsY26CmmG9CaxziGe6_UmOg7kbcLMf1QqlwqwyGmxvXx3TLnz-cg33Jn5dynFfHSzcYsaA7ro2UugMEm3X7VfsHdeF0p6jeq68mhomUAiAXXTMsMmO-SGBxXtdwr2kEoU4wxLXCU4SME8rEAh9TnZgJTi4IgmCotOekE5kGIiiTxrsSxeBoK134HuWOeadSRaAPnGiv1Dur3oZteNarv2fMB3monuoxqyBfKZQ8ZuW8aq-XDllvgJJPTo8aTaPStNlCGk_t-W9iiiO8x0SeEuTzH9ww_2W0d4LzPcV6FOHwJ1u32SLWqZOPh_IPPm0k0fBa_940HjAO3U5yPb1F2_IpDFVoQRq1MwxSOmEk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: رئیس‌جمهور ترامپ دیروز گفت که اگر مذاکرات این دور به مشکل بخورد، شما را مقصر خواهد دانست. آیا نگرانید که او بخواهد شما را قربانی کند؟
🔴
جِی‌دی ونس: نه، اصلاً. منظورم این است که فکر می‌کنم رئیس‌جمهور شوخی می‌کرد، همان‌طور که اغلب اوقات این کار را می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128948" target="_blank">📅 19:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128947">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
جی‌دی ونس از "حق دفاع از خود" و حق داشتن موشک‌های بالستیک ایران حمایت می‌کند: «اسرائیل اگر حزب‌الله به سمت اسرائیل موشک یا پهپاد شلیک کند، از حق دفاع از خود دست نمی‌کشد. ایرانی‌ها هم از حق دفاع از خود در کشورشان دست نمی‌کشند.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128947" target="_blank">📅 19:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128946">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: من می‌گویم دوره ۶۰ روزه رسماً امروز آغاز شده است.
🔴
پس بله، توافق دیروز شروع شد — ما امروز ساعت ۶۰ روزه را شروع خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128946" target="_blank">📅 19:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128945">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
جِی‌دی ونس درباره ایران
:
من کسانی را دیده‌ام که به این توافق شک دارند — افرادی که می‌گویند ایرانی‌ها هرگز رفتار خود را تغییر نخواهند داد.
🔴
خب، شاید این درست باشد، و اگر چنین باشد، آن‌ها هیچ یک از مزایای این معامله را دریافت نمی‌کنند. اما آیا ارزش امتحان کردن ندارد؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128945" target="_blank">📅 19:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128944">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0fa45935.mp4?token=v3s7EX4p8tKqaY2RjPE7IRjBEESlI_w6VezKfHurkclOJQ3yfgDZI4AuJssWdISMh8xPwmOxypmahlYM_hDqzAkn23mPVlj3B8OuVKhWNngWcjUEEe_47NlmVLbvA7BOVAgOjbBqbIgTol-BApAPBFVJFQz2BwKX-r6j58siGxdBVxz0yTy6TwPhDWLzNFIx87najhVdDrJSP31qOrnsmcQ2H8vgjAl8HQEGUcDkqshveubsgzVMXIeJXEnfHAJRZK1LIfq4PUjV9-vyRc0I7iO-qFJmoaOVH7WXouKsn4y80Ya2YfUCF67aWMfBHKzc7SvBSw949pv8odmRAhPzyTpDgcooZXO9hLApHGTqBBgwACxbHcaVnoeYRHp9MmB0KQSSbzl_OZ-udkkltf5OdGZHXEO17QS_D1y2T_1xpHNIiFC5Okxi_FzFyj1MSAAxw9QQx1X-XkJeAnh1EyB_TfFVkt56xUKh6jUGwyDKBv3XWTaFbgYEB5Qmx1zk36ha2MXaSGSNuhJMxFA0UDrGlF4pYGCMpp1l9fdxEO1Iqj9tu4LobJcewDQazKq06lK7UfPFvqRt1A7s5wr-WJy7lA-hkKCGzqD_2_EdEWtGuWrSR4aGH9yoP-ysOQOo5lw_ZmnQtK-nvJLsys3MKe1Ehcft5cucgpFJfgO2JVXNLbs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0fa45935.mp4?token=v3s7EX4p8tKqaY2RjPE7IRjBEESlI_w6VezKfHurkclOJQ3yfgDZI4AuJssWdISMh8xPwmOxypmahlYM_hDqzAkn23mPVlj3B8OuVKhWNngWcjUEEe_47NlmVLbvA7BOVAgOjbBqbIgTol-BApAPBFVJFQz2BwKX-r6j58siGxdBVxz0yTy6TwPhDWLzNFIx87najhVdDrJSP31qOrnsmcQ2H8vgjAl8HQEGUcDkqshveubsgzVMXIeJXEnfHAJRZK1LIfq4PUjV9-vyRc0I7iO-qFJmoaOVH7WXouKsn4y80Ya2YfUCF67aWMfBHKzc7SvBSw949pv8odmRAhPzyTpDgcooZXO9hLApHGTqBBgwACxbHcaVnoeYRHp9MmB0KQSSbzl_OZ-udkkltf5OdGZHXEO17QS_D1y2T_1xpHNIiFC5Okxi_FzFyj1MSAAxw9QQx1X-XkJeAnh1EyB_TfFVkt56xUKh6jUGwyDKBv3XWTaFbgYEB5Qmx1zk36ha2MXaSGSNuhJMxFA0UDrGlF4pYGCMpp1l9fdxEO1Iqj9tu4LobJcewDQazKq06lK7UfPFvqRt1A7s5wr-WJy7lA-hkKCGzqD_2_EdEWtGuWrSR4aGH9yoP-ysOQOo5lw_ZmnQtK-nvJLsys3MKe1Ehcft5cucgpFJfgO2JVXNLbs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جِی‌دی ونس درباره ایران: در ایران تقسیمات واقعی وجود دارد.
🔴
آنچه در چند ماه گذشته دیده‌ایم این است که عمل‌گرایان درون نظام ایران — افرادی که واقعاً می‌خواهند رابطه خود را با خاورمیانه و جهان تغییر دهند — در حال پیروزی در این بحث هستند.
🔴
ایالات متحده می‌خواهد این افراد در این بحث پیروز شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128944" target="_blank">📅 19:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128943">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
فوری / ونس: ما در حال حاضر یک تحریم اقتصادی فلج‌کننده علیه ایران اعمال می‌کنیم و تا زمانی که این کشور رفتار خود را به‌طور اساسی تغییر ندهد، به آن پایان نخواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128943" target="_blank">📅 19:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128942">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: برای بخش نظامی، چند نکته وجود دارد که همچنان درست است و چه ایرانی‌ها با بقیه توافق همکاری کنند یا نکنند، این نکات پابرجا خواهند بود.
🔴
برنامه هسته‌ای آن‌ها کاملاً نابود شده است. ظرفیت غنی‌سازی آن‌ها، تأسیساتی که برای توسعه غنی‌سازی و ساخت احتمالی سلاح هسته‌ای استفاده می‌کردند، همچنان نابود شده است.
🔴
نیروی نظامی متعارف آن‌ها همچنان نابود شده است. ظرفیت آن‌ها برای تهدید همسایگانشان عمدتاً از بین رفته است.
🔴
اکنون می‌بینیم که آیا آن‌ها مایل به رعایت گام بعدی طرح صلح رئیس‌جمهور هستند یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/128942" target="_blank">📅 19:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128941">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf09694b6.mp4?token=Hh7LqTPoLhG-wIcBeXMVaUjhmfm0xew0SuwoRw12p999SEjeOIv0YWu5f-nR5dPMnSUaNFeGVP6NutKFjSCpStrq9XygD6UxWMeqbqC6xmf1-GrCxHRTrR7JKWRCO_8Eu_V6QjCZNEU7Pn-BADUlzz_1UNS8vJnWe0dTWp5qHuiqOlD4bY5d-ZrPLzBuUhvDoM9CNdj0h-_edX6wYrp3eLS6UhiSawyl-EvxNcTFgH0CzLVPfO1ouIuKnfdMWtaQ7Cv1qgxvlcFKlGYskq0r0T_7DO7v2OdG1krXWGLxdhvCkIDxq2ATXNL_L3zFst5HIV5ZR3ciU1lEPJQ7u1A1mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf09694b6.mp4?token=Hh7LqTPoLhG-wIcBeXMVaUjhmfm0xew0SuwoRw12p999SEjeOIv0YWu5f-nR5dPMnSUaNFeGVP6NutKFjSCpStrq9XygD6UxWMeqbqC6xmf1-GrCxHRTrR7JKWRCO_8Eu_V6QjCZNEU7Pn-BADUlzz_1UNS8vJnWe0dTWp5qHuiqOlD4bY5d-ZrPLzBuUhvDoM9CNdj0h-_edX6wYrp3eLS6UhiSawyl-EvxNcTFgH0CzLVPfO1ouIuKnfdMWtaQ7Cv1qgxvlcFKlGYskq0r0T_7DO7v2OdG1krXWGLxdhvCkIDxq2ATXNL_L3zFst5HIV5ZR3ciU1lEPJQ7u1A1mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمریکا حتی یک سنت هم به ایران نمی‌دهد / جی‌دی ونس: "آنچه از همه شما می‌خواهم این است که صادقانه گزارش دهید که ایالات متحده حتی یک سنت هم به ایران نمی‌دهد...حتی مزایای اقتصادی، کاهش تحریم‌ها و غیره که با این معامله همراه است، فقط در صورتی اتفاق می‌افتد که ایرانی‌ها عمل کنند!"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/128941" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128940">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
جِی‌دی ونس درباره ایران: فکر می‌کنم طرح صلح رئیس‌جمهور در ایران در حال حاضر برای مردم آمریکا ثمرات واقعی به همراه دارد.
🔴
دیشب، ۱۲.۵ میلیون بشکه نفت از تنگه هرمز عبور کرد.
🔴
این بالاترین میزان از آغاز درگیری است.
🔴
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا کنون، به تعهد خود پایبند بوده‌اند.
🔴
سنتکام اجازه داده است که دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به تعهد خود عمل می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/128940" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128939">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e783b213a.mp4?token=tLDgNKslpG5Tx142377mXj7KBs0HidpVp3vkhIY-rQft5psbPvGIAdPUjUsJlY8Ac3QHNo2lDblsz6bZFUSicdC4VV9lv3G8ESoJ6iUjXSp1Nszaa8cUU3_DXcuGEIU6dAw19kdgtf8-OmFYK9aUidgF36pW0neXF1kt9v9CRMDKtR86_bvN-0aUmS9AIik0HgzTIQ45LGrfkKfW3GC6ch9aLavSmorgb4RrNHAmCcOgL_og4OjUOxPj03cuinB5nShXc0QflrsXcOAigLHy-2nysVf87MGnxBeO6BTXuE2J-NaCR6HGtbOxheMZPjJ3TyRQCqXFobjNv3s-I8l8-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e783b213a.mp4?token=tLDgNKslpG5Tx142377mXj7KBs0HidpVp3vkhIY-rQft5psbPvGIAdPUjUsJlY8Ac3QHNo2lDblsz6bZFUSicdC4VV9lv3G8ESoJ6iUjXSp1Nszaa8cUU3_DXcuGEIU6dAw19kdgtf8-OmFYK9aUidgF36pW0neXF1kt9v9CRMDKtR86_bvN-0aUmS9AIik0HgzTIQ45LGrfkKfW3GC6ch9aLavSmorgb4RrNHAmCcOgL_og4OjUOxPj03cuinB5nShXc0QflrsXcOAigLHy-2nysVf87MGnxBeO6BTXuE2J-NaCR6HGtbOxheMZPjJ3TyRQCqXFobjNv3s-I8l8-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غرفه نقطه آتش اوکراین در یوروساتوری ۲۰۲۶ در پاریس، حملات پهپادی FP-1 و FP-2 امروز به پالایشگاه مسکو روسیه را به نمایش می‌گذارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128939" target="_blank">📅 18:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128938">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
پزشکیان: تلاش‌های پاکستان در مسیر دستیابی به توافق پایان جنگ در حافظه ملت ایران ماندگار خواهد شد
🔴
شهباز شریف: صبر، استقامت و رویکرد مبتنی بر عقلانیت و تدبیر مسئولان و ملت ایران ستودنی است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128938" target="_blank">📅 18:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128937">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
علی‌هاشم، خبرنگار الجزیره: مسعود پزشکیان شاید تنها رئیس‌جمهور ایران باشد که چندین حیات سیاسی مختلف را در یک دوره تجربه کرده است
🔴
به قدرت رسیدن پس از جان باختن رئیس‌جمهور قبلی در سقوط هلیکوپتر
🔴
ترور اسماعیل هنیه در مراسم تحلیف
🔴
حمله مستقیم ایران به اسرائیل
🔴
سقوط سوریه، ترور نصرالله و حمله به ایران
🔴
شعله‌ور شدن اعتراضات
🔴
تغییر رهبری در شرایط جنگی
🔴
امضای توافق صلح با آمریکا
🔴
در دوران پزشکیان، ایران هرگز از حرکت و گذار از یک مرحله به مرحله‌ای دیگر باز نایستاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128937" target="_blank">📅 18:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128936">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری / معاون نخست‌وزیر و وزیر خارجه پاکستان: از آنجا که یادداشت تفاهم میان آمریکا و ایران به‌صورت مجازی امضا شده است، مراسم رسمی امضای آن که قرار بود روز جمعه در سوئیس برگزار شود، لغو شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128936" target="_blank">📅 18:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128935">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
یک منبع: بررسی اصلاحیه قیمت‌های ایران خودرو نشان می‌دهد که نرخ نهایی اکثر محصولات این شرکت بدون تغییر باقی مانده و تنها چند خودرو با «کاهش محدود» قیمت مواجه شده‌اند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128935" target="_blank">📅 18:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128934">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7a13d15.mp4?token=hpdrZZvpb6-NyUuQ-2RB10fjEFSg6yK23KPUyXFdFjnhjJ6U3AsV3HWzK3ieQj16n89UCx1vGcNduG_4Rvvta2FCEAy1UNRA1Xai6w2980T4BDddLRuvpRM6e5xeK_ctf8UWDnDt7UbJRSsXwpYSJSzHqS160t9-Wh72HDulaXIcAWLSCOtNxKtE3YFjZh_H7iSfdI0U0MJ97YskUAF52kz-STcR0X7wy3ZtBtclu4cMYdwtKUrbvouzVqR12tml6rdF6TeVoAuMAvkb9xRse7QLkXdxO42ftneukgONYt0oi4paLCGwdCGdPgRL_-t0e-kLjLtT_3VITAW7vBL4gEiaBaLolyBoL8VVVGGBZSsi852FgS7czVrp1sYA6K-nWMMEuTbHK0ijmdLS6jwnSaBEyn8BsGC1RW0Me_qKj2H3bnsAqIf7BN1QFONLQinPf7ByUGN3vx94kkyZQwAy1oCZFXMqsKdpZpcngvjDENLWkb2OZ_cHLZ3KEqD8Vjy3S8wZoOeF2dqKb2WdIC9dIRJXVhlaKuoKfeB4Ri8Vjl7tlaVW65ChSDApLC7EtBY6FAt2Ug7FQQh6DTsASaCggPoRCxWs95aBykp5rS-MJEv9XFgRYSINB6KovWxUVQXe5wOYkcTkLSAMngEbMSFzJkaz6jqxABDwXxj5C31WzPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7a13d15.mp4?token=hpdrZZvpb6-NyUuQ-2RB10fjEFSg6yK23KPUyXFdFjnhjJ6U3AsV3HWzK3ieQj16n89UCx1vGcNduG_4Rvvta2FCEAy1UNRA1Xai6w2980T4BDddLRuvpRM6e5xeK_ctf8UWDnDt7UbJRSsXwpYSJSzHqS160t9-Wh72HDulaXIcAWLSCOtNxKtE3YFjZh_H7iSfdI0U0MJ97YskUAF52kz-STcR0X7wy3ZtBtclu4cMYdwtKUrbvouzVqR12tml6rdF6TeVoAuMAvkb9xRse7QLkXdxO42ftneukgONYt0oi4paLCGwdCGdPgRL_-t0e-kLjLtT_3VITAW7vBL4gEiaBaLolyBoL8VVVGGBZSsi852FgS7czVrp1sYA6K-nWMMEuTbHK0ijmdLS6jwnSaBEyn8BsGC1RW0Me_qKj2H3bnsAqIf7BN1QFONLQinPf7ByUGN3vx94kkyZQwAy1oCZFXMqsKdpZpcngvjDENLWkb2OZ_cHLZ3KEqD8Vjy3S8wZoOeF2dqKb2WdIC9dIRJXVhlaKuoKfeB4Ri8Vjl7tlaVW65ChSDApLC7EtBY6FAt2Ug7FQQh6DTsASaCggPoRCxWs95aBykp5rS-MJEv9XFgRYSINB6KovWxUVQXe5wOYkcTkLSAMngEbMSFzJkaz6jqxABDwXxj5C31WzPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در ۹ مارس: این موضوع واقعاً روی ما تأثیر نمی‌گذارد؛ ما نفت و گاز فراوانی داریم، خیلی بیشتر از نیازمان.
🔴
ترامپ در ۱ آوریل: ما اکنون کاملاً از خاورمیانه مستقل هستیم. به نفت آن‌ها نیازی نداریم.
🔴
ترامپ در ۱۷ ژوئن: اگر به بمباران شدید ایران ادامه دهیم، ذخایر ما در حدود ۴ هفته تمام خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128934" target="_blank">📅 18:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128933">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7d1aae69.mp4?token=vrRFuCXI5yvHCPSLjqB8Hpxwe7yxGUx5NnS1NxYASbJv96M5EufU4Bksxx4LIOA8cYHxQqma8RylfJA3T_Yb6u52VqKy6DBkrKvkl2TnT72jtw5cKv0j4HvTYKn4nzx0QvKeg2m6PrM2Y-iK9QkOYnxzWPtaHxl0Bec47arhu71bF-tynkrytCcNw2VrkHBhYbv8wozA085K9Ex3u7Qx5DI8T1BH2u9uNpwbeHUA7jISHOJjWnPf9hH9E7LT6-T7jdQbTi0ncZC0ufvfVuzjlqlolF1J7dntiInrs7Kb_PWoOhNQ3Rf93UBIgqfU5Z1sf43_50BrModhUdNPatO0IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7d1aae69.mp4?token=vrRFuCXI5yvHCPSLjqB8Hpxwe7yxGUx5NnS1NxYASbJv96M5EufU4Bksxx4LIOA8cYHxQqma8RylfJA3T_Yb6u52VqKy6DBkrKvkl2TnT72jtw5cKv0j4HvTYKn4nzx0QvKeg2m6PrM2Y-iK9QkOYnxzWPtaHxl0Bec47arhu71bF-tynkrytCcNw2VrkHBhYbv8wozA085K9Ex3u7Qx5DI8T1BH2u9uNpwbeHUA7jISHOJjWnPf9hH9E7LT6-T7jdQbTi0ncZC0ufvfVuzjlqlolF1J7dntiInrs7Kb_PWoOhNQ3Rf93UBIgqfU5Z1sf43_50BrModhUdNPatO0IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چرا با اسرائیل دارای سلاح هسته‌ای برخورد نمی‌کنید؟
🔴
گروسی: چون عضو ان پی تی نیست! خواهش میکنم عضو شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/128933" target="_blank">📅 18:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128932">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/996fa2aee7.mp4?token=WBKBpBY43tVwiYiByG9VpBheeykwENO05yYvO8rCM7Nfr7X4wqsWWu5-YsQjDVqFIOnU2_5z5ueNe3HlCHN8FX30-0BgL1HJU9y1LdlDxYYrhNjWfoaBGruwJsQenjB0LPqWzzOkkQM46GrU5YO3MjNUR6yTUqpthYypkZRG-EIb2G8iVMZecWkU1QTmi3dr7rQ5uI-Nwouvw6IpaTfxsNPfnve7T-vHONkSaF1Ej1BJW35CM1-uaFEE4PVESMCDRxGHkQ1LP8bmG2ADAOWcobAqPDr0oygUnuXDUG_TrkWL9_3SiBDiidVCf7OCxDDmXdDWh92F26s2xNGesCXVsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/996fa2aee7.mp4?token=WBKBpBY43tVwiYiByG9VpBheeykwENO05yYvO8rCM7Nfr7X4wqsWWu5-YsQjDVqFIOnU2_5z5ueNe3HlCHN8FX30-0BgL1HJU9y1LdlDxYYrhNjWfoaBGruwJsQenjB0LPqWzzOkkQM46GrU5YO3MjNUR6yTUqpthYypkZRG-EIb2G8iVMZecWkU1QTmi3dr7rQ5uI-Nwouvw6IpaTfxsNPfnve7T-vHONkSaF1Ej1BJW35CM1-uaFEE4PVESMCDRxGHkQ1LP8bmG2ADAOWcobAqPDr0oygUnuXDUG_TrkWL9_3SiBDiidVCf7OCxDDmXdDWh92F26s2xNGesCXVsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لبنانی‌ها همچنان به سمت جنوب لبنان هجوم می‌آورند تا به خانه‌های خود بازگردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/128932" target="_blank">📅 18:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128931">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEGN_kJmefK3jSDeYYmaTzILEgjtQBHp6pjkAjZ7LJKbuzvMxUF5acAdRS8h895JDlFaoKbhild3yqvE3AFn2b8q-N8fxl-gvNp5In3ayKjaesam_nmX034rBx2dPgVIQZmn7YrHkRMpk0yEd1zzN7uutcmx5UxhvtfI_P6YVwVdp5Oblqn3XPkKapxhxsQFsJ08rApyge7Kz-XmuPB9dKhAd2vXAs2hcnUTrqfHyNi5SxLOk16o87K7LnYtDmcGd-0Y3oXfsZ5F-cIy15bdCrYic-6dKNG_sIasEhQf_REw0s3HvWiKUnQumGNFOXOszz8waCfBDwrryjCueG5n2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پیش‌فروش‌ بازی Grand Theft Auto VI رسماً از ۲۵ ژوئن آغاز خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128931" target="_blank">📅 18:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128930">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ایهود باراک، نخست‌وزیر سابق اسرائیل:
احتمالا نتانیاهو در آستانه انتخابات، به لبنان حمله خواهد کرد، و در تلاش است یک جنگ ابدی را با ایران و حزب‌الله آغاز کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128930" target="_blank">📅 18:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128929">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
الجزیره به نقل از یک منبع در دفتر نخست‌وزیری:
معاون وزارت امور خارجه نماینده پاکستان در نشست سوئیس خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/alonews/128929" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128928">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ به کانال ۱۱ عبری: آماده دیدار با نتانیاهو هستم
🔴
او باید منطقی‌تر باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/128928" target="_blank">📅 17:56 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128927">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxTcQ9oYsFTZj1up_iWJgkdLSQ_hiQsogJ1T4acjPXk3ilANgbfwWImBkyzaPdxs3sQ1XYMRDpmdnJ6llnZu4bWn7bzn2oxYWXyzL8wpKV4KorDHJu_VmvU4oiChgMlhqA2R-WcuCYbyTR4Ug6OEkAJwTdXhgxGnSekQel6INqAzb1LkIGibWrMzBAueGiD6nV_qnr0upmw7V-UPORFOuJ7Nb3jPYJFxQBspNeApY1Lo2XU13oNFrIn2fBe4DzAT9ZmCQUdP0yE5zUSo9YZ6GsXXDpmCWpAic7Vo-RdIFiGl9OtQuZ7uEwY2sPSxQwnUk1xOnlXqh-AfIeet1XLEnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ به کان نیوز:
من به احتمال زیاد در انتخابات پیش رو از نتانیاهو حمایت خواهم کرد، اما باید ببینم چه کسانی نامزد شده‌اند.
ما رابطه خوبی داریم، اما او باید منطقی‌تر باشد. من آماده‌ام با او دیدار کنم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128927" target="_blank">📅 17:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128926">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ:
هیچ ملت و فرد عاقلی نمیگه بمبارون رو ادامه بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/128926" target="_blank">📅 17:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128925">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKxtSS8wepKvFKitEUVwTxkmMKSJyZTWFMYXAETWq_2YtT-goB9Ug145Btt_9-NKeVp4ze2XWt5ihW5vNhPYHI1O5dCxaNW_8o7LvoJg2kogwxhFJIvEjcUDaqJBU4RJppLI_btBdVEb6IFjC0Q3bnqQNSIkFQDSgyS6m-hPaMYgsXtuTNx1VxnH4xKmt3Adv1-cr24pHZzWcLMrBezJSm77PHc0RO38GQcqgpvJIhJZfxpNHLTZKW4NTlvJuBGVBZaUOtowD2Rpu4RrAe1vrhcMLXxCOngmxts8a3WPRhJCa4lAF6qVj-tgbMe0G6asetlzv9wGQVHlikg1RxUWUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: نفت در حال جریان است ، ایران هرگز نمی تواند سلاح هسته ای داشته باشد (جهان در امان خواهد بود!), بازار سهام در حال رشد است ، شغل در رکورد است ، و قیمت ها در حال کاهش است (قیمت مناسب!).
🔴
کشور ما قوی ، امن و محترم است مثل هیچ وقت پیش. خواهش میکنم!‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128925" target="_blank">📅 17:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128924">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ایرنا: ایران به پاکستان اطلاع داده است دیگر نیازی به برگزاری جلسه حضوری در سوئیس نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128924" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128923">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
تلویزیون پاکستان:  سفر برنامه‌ریزی شده نخست وزیر شهباز شریف به سوئیس بدون ذکر دلیل لغو شد.
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128923" target="_blank">📅 17:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128922">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f05f75b6.mp4?token=jlxODeuSLzxdRzhMnsbEoiF_ru4vlkKgvxLwfE0u9nbtbtnpWP2UDpc9yqudlXX2uuSnppqW1rxJbr9NepmrV06x4o1jcprj33xZ7MMpXl0qc2alcOQ7uBfII9ITfYABKgzQXDDvRsM1O3LgBKKGGF2__xP-gQrXCFgmUjfgPCxDYA9hl4i58bQlkasLo7SJ-OCsLHeIL21SnFFUf2IF_IiQLsfOiXuJkleA7wANcwjRldZ91x9UeNJQINvPZoD6BSptYSnmcv8h_udQbPgysmDM9MusFaBnWX_57r3yiF5vSyAnx11jC1RhJRClyG7a9iHzKQsEp69-zVhqaEk3sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f05f75b6.mp4?token=jlxODeuSLzxdRzhMnsbEoiF_ru4vlkKgvxLwfE0u9nbtbtnpWP2UDpc9yqudlXX2uuSnppqW1rxJbr9NepmrV06x4o1jcprj33xZ7MMpXl0qc2alcOQ7uBfII9ITfYABKgzQXDDvRsM1O3LgBKKGGF2__xP-gQrXCFgmUjfgPCxDYA9hl4i58bQlkasLo7SJ-OCsLHeIL21SnFFUf2IF_IiQLsfOiXuJkleA7wANcwjRldZ91x9UeNJQINvPZoD6BSptYSnmcv8h_udQbPgysmDM9MusFaBnWX_57r3yiF5vSyAnx11jC1RhJRClyG7a9iHzKQsEp69-zVhqaEk3sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رویترز تأیید کرد که محاصره دریایی ایالات متحده بعد از ۱۰۰ روز لغو شده و کشتی‌ها بدون دردسر از تنگه هرمز عبور کردن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128922" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128921">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
تلویزیون پاکستان:
سفر برنامه‌ریزی شده نخست وزیر شهباز شریف به سوئیس بدون ذکر دلیل لغو شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128921" target="_blank">📅 17:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128920">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDLK3JIetUZHLwpgTwNM3r7rjo4ccOOiEqqQ0VEQaWSM_NYTiMmTX68q4f9HfKF_T7FvJLjXFEV1-ghlRa_4mYHV4peReb5eIdT569J5ajQTtUv1GCi1KOWSrq5KHNPj0WUkz1CECAaoO_4_sk-A3YOJTL6ziu3vFs0-R-BnIzZo7yW1xvKVdwHfXTQ_p8L39UTJQT_3MOzTIfeQep5rIMsGyRiWYbQSrgP2WqcPGuCHsaxxokjO9G5TQFTgSOvg5iyf7xCPUBdqY3-QG4BJ2EF_vpNlRuJhxnr5U0D38clvn_elCsyX89Sy9Lj8pZGmiNOq9ZeCo_PiUOsCk3E4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این عکس رو هم آمریکایی‌ها خیلی زیر پستهای جمهوری‌خواهان و جنبش MAGA دارن میذارن.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128920" target="_blank">📅 17:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128919">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZ7zk3vGRxGmi8A_5mnahmSW3VCdyfVsn6vz6dVVep57k2WW8RIZu5ugcneNKucvDhsaD2NL6MOQ9wJ2HXWzFAT9tq0t6N0GAS5oIJtD0DQeoDQxYcfzQgAR7C1non1Y-84HDPG8ZkI1BXte8AUBrsm4Ir8tpKzDRyU_c3IP9sXaDa5l5JiXIBUl75MOpNfwT8LWAHlexJYSmYP0KWfay1rktWANN0pz9IzMzC_8SkRQNRr-q014IRIFf7U-vEWCkt8yfmtUi5Dkr3zzuAwB7DgZ0XIhmcW6OyTphJNHa03qTm3TBRvMW39l2c4H-WIhDhWgYPZ8OkvqC8_22moBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: هنوز تصمیم قطعی برای رفتن به ژنو در تهران گرفته نشده است اما در صورت رفتن ریاست هیات ایرانی با قالیباف است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128919" target="_blank">📅 17:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128918">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O30oha4kH0UdBJa0I1VZV9F7AgtxDwDyg4y425kpDJfcF1k3o8IucuIMHZKGdd-Lc1jL_UmEBbKQFdCsDn_ueYsupuwBmOpaTElTfArDhp6lBK2EVWGimg6BsjFaAAL7rmhTVIuvhcOZ7EUxTm0Jn615HjsHYdhlHrj10gD1vTvjhR3IY02Re1m86pxI3xXqujRoVLhwqW1eJrvEr-3SlR9g1-tsT2a_Uky9L2B5KSFOlfKqewXvCV0yOv2hSREl-mlGrZQRquRY9Ubv_nILruGGAdGb3rGErMKBntWqvH_QE6s6jGmEppNffDr5yDyJ_hInyXWD5-BJP_qfIqCqHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مِی ثاقی:
یه مشت وطن فروش به برنامه ما هِیت میدن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128918" target="_blank">📅 17:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128917">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هنوزم آتش زرتشت ز سینه پرتو افشان است
هنوزم فره‌ی یزدان به ایرانشهر تابان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128917" target="_blank">📅 17:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128916">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128916" target="_blank">📅 17:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128915">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نتانیاهو: ما امنیت را به شمال باز خواهیم گرداند و این مستلزم حفظ منطقه امنیتی در لبنان است. ما نباید از آنجا عقب‌نشینی کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128915" target="_blank">📅 17:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128913">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ipy1rs23h2hbz2Q-aZbTKT_jrfRT1NHAc0zTQzH154VRBCFvA9vkSMxfM5ciIH6S_94fiWxpiKOCDHvV0RRSnbSYwjL6rxc4HLQqNEXtQA42o1xBPKC0_x5zU-1WYb7jKEpbwpYHIxw4Da4I2KsysAAiTZBHVzv9LR4IwYICH8WVlsUAEqUxcAxcpuK_rJkobqDJ9FIfKvkUK0eqHE7p4h_BWJ8XIZkXpeX0CTmR9QPet1xCJLbEw3oAGXBpxCdwReCwt0J821nD6cf4Tlw4hBxT1gBHEoU5CMA0yO29JmebmMTDvUxA-bqhtoxWPD2vS0m210DwCsezNe4kqT6Zkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoXjpykIFOtVZLxmfHtvl5LY-RQnh_8eJznACJCl7Z1lU9CEiDjAib_p3WlcUdi5n1jFuhL7DE4H9V7aNry2zX-rboQLfSLsU0wS1WNrExSzqZXyNZaR48ozBd5ov6nkpBgWMJAM-KxkBvLiC3LE4pCugDz_8vMVz9HW7F5CEvHPDIKLeHSGufACT06Q9WNffIG1c04UVA2QCrZT1G2jwQS68N9m3O2nekq3zxn6DFvcXBcA98EsRfXTh26SJdaCVV2RWQIWR16dyjYyrjmkiDR0VqdxUBCyqPdZ9Rgj_19Sn0PIr-NLfurj7dFr6WNI8Grl0RC1UI8EDz3ZGWMCfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/128913" target="_blank">📅 16:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128912">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7be62b11.mp4?token=QZAeCrMnsptxXnhvU3qaTJ802PXyfLDLJG-v5DrPRnHgM6yNp9W0IZGpvEwBBoEqc_SWJXaB2d1j3z6_F_uxGN7n4wnG5UGdlbcPt6GTIUeXZhvc91saQftEBsnQ5LtjbiCkMG5OE1Gug821e854PjbsrtEO1Ri71dNlEz81shaIO7vsbqU6kA8dkC4mGLlY1_93PTnhvGFk8__x2OlQ-5NSwUlqwuAHZVAiz9svAejLH9PZhnrkbzYKJ-UkJqDSXza1E00HT4O3zAjZZ-bgShyxqOL_uVopR73YRjWkdhcPQ5ezEgHG8O81T08TKADSk67sn044sctGaY7xjwG9hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7be62b11.mp4?token=QZAeCrMnsptxXnhvU3qaTJ802PXyfLDLJG-v5DrPRnHgM6yNp9W0IZGpvEwBBoEqc_SWJXaB2d1j3z6_F_uxGN7n4wnG5UGdlbcPt6GTIUeXZhvc91saQftEBsnQ5LtjbiCkMG5OE1Gug821e854PjbsrtEO1Ri71dNlEz81shaIO7vsbqU6kA8dkC4mGLlY1_93PTnhvGFk8__x2OlQ-5NSwUlqwuAHZVAiz9svAejLH9PZhnrkbzYKJ-UkJqDSXza1E00HT4O3zAjZZ-bgShyxqOL_uVopR73YRjWkdhcPQ5ezEgHG8O81T08TKADSk67sn044sctGaY7xjwG9hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیکه سنگین حاج فتل به میثاقی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128912" target="_blank">📅 16:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128911">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
پولتیکو: ترامپ به وضوح از تماشای عکس‌های سوختن کلیسای جامع دورمیشن کی‌یف که زلنسکی به او نشان داد، تحت تأثیر قرار گرفت
🔴
این فشار نهایی باعث شد که او از یک بیانیه مشترک سخت‌گیرانه‌تر درباره اوکراین حمایت کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128911" target="_blank">📅 16:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128910">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJP2LOjljt0mbEMDmgmePi0ar6GmlJJpQskUw45GO754XtW-FTesSCtRxUye_3Sz7sHgrks1nzDeRRFdUsFKn4A6r9kapzdWWG29gDU1dnUu_h2dmVxtk66v_FkYP5w_uo1CNC_MJ3YOzLGVaeIT9Xy1ncW_D7m-XFpkvRviIYKHkZwvY4p04lq7DP8TkCrUKd0PX4buy6kI2QsiTOJzTI4D13kygq7OiMZj9rBXXDMxLcXwNRLwLjILj6qL4LiJx_8dy002-l72bqmJgkBU6S4Z1AD3CLFp-tueHE0L89n_gQib_ZVHqpqBd57qS8ctoFhTzshisJhWPzftwCfDUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از تأیید پاپ لئو بر توافقش با ایران خوشحال است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128910" target="_blank">📅 16:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128909">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90181d0fb1.mp4?token=OMjJysZJDfl2WsfL5APMdz8IHZpyZJS5S6-_kPU6iWZ__QAEPfmZN-2cWzKMWnUUrWijCgKOrCqCJ2fDntMkEuuyp45mNddocAkj3pbgBvMnBj7-e6G3_2MTZMJ0r8hL9pYtqUquepaJ67hU4BVT83G47592qhWb3JrJh1RVXod4SIytsyJUVk8gQwKLrNUHiPGzW_PamRLSJ3NtIuYtF6DiwWwspoSPBH1e5k3BGUocZEkv3KL-EJ-ouBvzsiuYb_7B-HZxxT2Y1vHOfgVcFslSi6Gu8dPExM9uizEfnAIZ1xIPbsQSkrAczCDlUkMmjwD43ylVJ_FBGKEuGkoGXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90181d0fb1.mp4?token=OMjJysZJDfl2WsfL5APMdz8IHZpyZJS5S6-_kPU6iWZ__QAEPfmZN-2cWzKMWnUUrWijCgKOrCqCJ2fDntMkEuuyp45mNddocAkj3pbgBvMnBj7-e6G3_2MTZMJ0r8hL9pYtqUquepaJ67hU4BVT83G47592qhWb3JrJh1RVXod4SIytsyJUVk8gQwKLrNUHiPGzW_PamRLSJ3NtIuYtF6DiwWwspoSPBH1e5k3BGUocZEkv3KL-EJ-ouBvzsiuYb_7B-HZxxT2Y1vHOfgVcFslSi6Gu8dPExM9uizEfnAIZ1xIPbsQSkrAczCDlUkMmjwD43ylVJ_FBGKEuGkoGXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی آب و فاضلاب کشور: رقابت های جام جهانی مصرف آب را در کشور افزایش داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/128909" target="_blank">📅 16:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128908">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
ارتش اسرائیل: بنا به نیازهای عملیاتی، نیروهای ما در منطقه امنیتی ۱۰ کیلومتری عمق خاک لبنان مستقر شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/128908" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128907">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
صداوسیما: ۱۱ فروند کشتی از محاصره آمریکایی‌ها عبور کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/128907" target="_blank">📅 16:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128906">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت امور خارجه قطر: نخست وزیر و وزیر امور خارجه در تماسی با وزیر امور خارجه عربستان سعودی درباره توافق واشنگتن و تهران گفتگو کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128906" target="_blank">📅 16:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128904">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UCgdOjH2Ql4KkmRzo3sToqaNGrzHrX3Ur6N7otb-hIsDhQK_wioI3q77fPROg18q-8NAQ9KELQ1nkACmp789q2VqMHXKcRCKtcbkaYlwHFG6hrc9ccpaT_dfcrof9b8v9hNoKemgJKhPqBvJ8-KpzgG5inspEm9_63MeIdcSX7_SAHNfOgTGJn9-gNeibZk3yq0APLxrQGTeGTqko-3tGpBDvhgYXhlu9g9rSNXp-Izx6ejJ1z5uAHAUcGlQr6TtqrMBMKKjvJvUCj8fCY9N4RvEtxWp7vV2xaQ-Hfj9ZRaRNUDf9D6O8O8o92c6fXe6vWR3545wcw_pEUdS0CB2lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRIrojb0NKI2T5932NqtoPk6tlyLwl1dqlASn3TM8NK3CfNlrKXh8wlVoYXYxHIGZ0CTezwKF9cCiBC7Eaxqay9Dr0DiLffRuWzc154Mxb0L6JP3gZi7w2boKYLMhHpW_qOUhtLyrGScCG5PB4I9wZvFFoq5YozCMkQNl1a04KuN8MAlx0Qf8ZUSXx_qSnWk2xYIYmavy1Sjgg-CIwRndBiC66in4O94EYPt_CHUIyiimH1CcpVXK-rpHsFnwAUsspxVSRLkpVLvvP4DQsMZCIyDjrhbXLPQiCHAhUEyMzk7Xq-fxM4gU2_KCc2VLTijnCUu_uFRpuWZDNbhNx9N2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
فوری / رئیس جمهور پزشکیان متن اصلی تفاهم‌نامه بین جمهوری اسلامی و آمریکا رو منتشر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128904" target="_blank">📅 16:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128903">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سی‌ان‌ان‌: نتانیاهو در تلاش است که بر توافق نهایی ایران و آمریکا، از طریق سناتور‌های حامی اسرائیل تأثیر بگذارد و بر ترامپ فشار وارد کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/128903" target="_blank">📅 15:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128902">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
یک منبع اسرائیلی به سی‌ان‌ان گفت:
نتانیاهو معتقد است ایران با محدودیت‌هایی بر برنامه هسته‌ای خود موافقت نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/128902" target="_blank">📅 15:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128901">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزیر جنگ آمریکا: کشور‌هایی که از تنگه هرمز بهره‌مند می‌شوند، برای باز نگه داشتن آن اقدام کنند؛ ما به این گذرگاه وابسته نیستیم
🔴
مذاکرات با ایران، حول موضوع عدم دستیابی به سلاح هسته‌ای خواهد بود
🔴
حضور ما در خاورمیانه به میزان پایبندی تهران به یادداشت تفاهم بستگی دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/128901" target="_blank">📅 15:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128900">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
توقیف کشتی حامل ۶۶۰ هزار لیتر گازوئیل قاچاق در خلیج فارس
🔴
محکومیت متهمان به ۴۲ میلیارد جزای نقدی و حبس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/128900" target="_blank">📅 15:36 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
