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
<img src="https://cdn4.telesco.pe/file/XjeLtBYYcbukWyZxQEsOZrPo92up8E-43-Y4Ed_F5q82qrJ4E7vmMjm7oBKaFmr8uj5Cd0f9f96N5vnVy7GrRV8mt1-gryKsEJ7GY_-uX4n54NV5rlN1xGO6Yxjcz5JcXPJPIhchfsjMjGqv6jdPhDv-Fgk198m3IqV5QjpWqdWTViIpqt5PC6CxKBauPuCCLi4CIC8i0214k-jv82m4ZcDxhNBPFegq3r3cDDqNImvS7zfO4HesJ9KoTHmiMohJN2fdCMztfmQAvreKB3XZlOmzuZAz95AEdALqFXtna_oMl0Nck-YtMxH2Yv2Zp9nOdlOiJJXzar7LFeZvGMAMsA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 624K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 18:05:15</div>
<hr>

<div class="tg-post" id="msg-28534">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=Ou---jP1bEGLeZBa4X6SQD6ld97iRKZEDUgrlWdfFjwZEhte6nKntAX59xCBx4xOBn4EhEo3qrJnMJE8uxE1_kTBrc4RBUvRPdS6mFemjNx2981ORDxP0bRKlzuv4SumvfTa4EoiYG8tK-Ey-BBhZeD8q89T0XtNftLiMovFEWVtqtW3ew8We7rAaK7I8XHdEobSQRsK0ZRlK6lrDmgcddXxDMpKsvxA7VwJcapGSkCNpfwJyduxDRvGjb61UMFLuTzmSXvQJfwf4g0vv5DhBaKdY5Vt4c9czPPjhjZ5smkM9nje4UzFGpWbydYh18a0X93fz8IMT2t7lkRN7Sr2DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=Ou---jP1bEGLeZBa4X6SQD6ld97iRKZEDUgrlWdfFjwZEhte6nKntAX59xCBx4xOBn4EhEo3qrJnMJE8uxE1_kTBrc4RBUvRPdS6mFemjNx2981ORDxP0bRKlzuv4SumvfTa4EoiYG8tK-Ey-BBhZeD8q89T0XtNftLiMovFEWVtqtW3ew8We7rAaK7I8XHdEobSQRsK0ZRlK6lrDmgcddXxDMpKsvxA7VwJcapGSkCNpfwJyduxDRvGjb61UMFLuTzmSXvQJfwf4g0vv5DhBaKdY5Vt4c9czPPjhjZ5smkM9nje4UzFGpWbydYh18a0X93fz8IMT2t7lkRN7Sr2DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
صحبت‌های جالب عادل درخصوص یکی‌از پیمان کارهای ایرانی استادیوم 105 هزار نفری نیوکمپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/persiana_Soccer/28534" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28533">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4qqFdrJFsCao6fUG-Lfu0OTBtT-8f7Z-rhFuoDzUOMylIn3xxx50rGTmwcRet8jpFOTSvytx3dnuWNuE6Z2K74XYfHYzuFOCsCb3toh7Jsd7tC4MBLmVxuedo8y8f4o5Ba048nqyJLgAwZk8mG5pGYOwjdOeod6fNUUQPZZN9gU4gOuefU0iSox-4Z0FvmwdjrFI2yh0fmLFtbYCI3AG7f7pnymq1SGnT_fqqv-PaPcTa3nDH9tcWsmbDThBiIRRIcqWJEbnUNpj9FXCBJ5LnTcVXmBvhBaOr_MxfcEfzmLw97ympH4CPCeOI6HzEyQkKi4ENDN1uYlQAO-dlL3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
عمق اسکواد بایرن‌مونیخ در‌فصل‌جدید رقابت‌ها؛ این فصل آخرین فصل حضور نویر خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/persiana_Soccer/28533" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28532">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLa1tLP_9rF6o9a2pMqB2gRwHG82tIoEWPgIFwhwo098nn4_WOrEj2pdQXPIA6wNeW32vfrfvB8Yw6yWtgjJsHb6bEEx2viXRmLWhVTfrB6RaiGpKPFNPOYxOVKyMsOWGW6sKyQaq0t3WIAZzmPCUUwp4JrxVd8HZYkov8k4i3gS6l3CJBBarAT00QWwdpjPL7gXYC3ItuDZRFQYCtfWMXtDCkkVSTQ-7qKjYro_ayuJRRvXwx2N9_Zmx4KsXm-Zl7tDScVQDa3gzmvHs7-D7jyh_xJFTqv1MSLkxTk4mlOXa4YSGOlse_TDw7ngI1N-LGB2YWRsKgbrv63dd_UxCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پلی آف لیگ قهرمانان اروپا
🇫🇷
لیون
🆚
فنرباغچه
🇹🇷
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/persiana_Soccer/28532" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28531">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSkzQQYTCdoqPOchKV0DhBo8nlhqCizIYQDdSHQF9zWDyEwjSULacmrooYyOMiFi0hUgMeHA9nCnK4feXAcJcklyKdcJuzHsnuLP5M_LppHGcF5jfqnQjBNwmFJdbwQhrDeB7_04cjD1aAX77laD92bkdjO_GeGeamhNuwWeFrw5nXK0OruwgGtZbT7Z_x4cNUSB0BQLIFx_Wvr1sP6dASIGv3_BQ11OunEMpm8x3kuzJbLI7ERlVqtXE2CIHZR6Bd8axBna5NbSPBhESA_qh8oT9UW8BGggka8wRg7o2rTftjs8Fs8imY7WzUcxUwTOA-iRFuSTPYT6E7yUMygCZIaj0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSkzQQYTCdoqPOchKV0DhBo8nlhqCizIYQDdSHQF9zWDyEwjSULacmrooYyOMiFi0hUgMeHA9nCnK4feXAcJcklyKdcJuzHsnuLP5M_LppHGcF5jfqnQjBNwmFJdbwQhrDeB7_04cjD1aAX77laD92bkdjO_GeGeamhNuwWeFrw5nXK0OruwgGtZbT7Z_x4cNUSB0BQLIFx_Wvr1sP6dASIGv3_BQ11OunEMpm8x3kuzJbLI7ERlVqtXE2CIHZR6Bd8axBna5NbSPBhESA_qh8oT9UW8BGggka8wRg7o2rTftjs8Fs8imY7WzUcxUwTOA-iRFuSTPYT6E7yUMygCZIaj0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/28531" target="_blank">📅 17:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28530">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7ABhuDYJDP1yAUhOcwFYZhbnXdFwX-GBP8oVT-imkZs_34P04gS0rHEYAHpC7l8XaO3Frer5z0X0wafH3bsdePt8pZcVlzBBo5DXYbmtTMDPiz4R3vXfoz57yWxnu17aqTIyE50JqUcbfxoQKX9M69SYEfemqeyTUVFBi5vVntSdTDFaAtiI67uMTy7qpWig0OnKV5FZlt-D9k9cjFe2h_a0X_8cvOTiyhhJw4PqlgDvHk5T7ChMdXs369enfL1X_p5NIhmp7JOb-EJyvirMtVRdYeD_8QWvqmNNhhYomCZieVndqXw6FpmZ9IpmJwMqAyLPMLCORnqelegQmi88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/28530" target="_blank">📅 17:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28529">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=lLbbdA1yQ4-tJqFLdNycbump89GA_lz8nI5ZWvHDzdzXmkHQqkFta8DGj8Ib3znZvI-F8IhrcIXHsiBV4hsY7DRSdA8riO7oTaSD-F8QLjGIkMRVRGhGQ80yug_BqRUefFtG0LYHEul19R5oH0YYby6Eo4_W1iDiCMMZmTLJICAuggZWBILjoYTVd-ayyYQTrtYJ8sMFeyapkBt-mEV1O0Zi5QyZXIftoirtNN3ATeH5vrBc074B8nKaD81ilyTMe71EfCUuMDFWh9fuvPm725sC9_gFbWzVIF3ygHGY9VfjSl0UQdAZJFXnZjxjaDQjr4QFLr0VaqpKe3K_he7IQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=lLbbdA1yQ4-tJqFLdNycbump89GA_lz8nI5ZWvHDzdzXmkHQqkFta8DGj8Ib3znZvI-F8IhrcIXHsiBV4hsY7DRSdA8riO7oTaSD-F8QLjGIkMRVRGhGQ80yug_BqRUefFtG0LYHEul19R5oH0YYby6Eo4_W1iDiCMMZmTLJICAuggZWBILjoYTVd-ayyYQTrtYJ8sMFeyapkBt-mEV1O0Zi5QyZXIftoirtNN3ATeH5vrBc074B8nKaD81ilyTMe71EfCUuMDFWh9fuvPm725sC9_gFbWzVIF3ygHGY9VfjSl0UQdAZJFXnZjxjaDQjr4QFLr0VaqpKe3K_he7IQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/28529" target="_blank">📅 16:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28528">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQngA9d8Hcnoc-fzENA_LtcDxjs2EPfpCAhTJEcuqUcpeHRjquKj3UiosdzuKCc9xNTupvBFnedQDTRpRiqccuPGgUndXL6qHaL3mA-k806mhI3DPIKaXz11PWBNq4_57Pdls9ueSkFLUFPyLREajAElEoKE41eugLTx_ujdF5OnWEdHBlBY8mrmzOSBVoYlyq86e_OC0rW1DrDhiqyCmQuvpA1ICJXFftgdHvL8qhFCKDuSQqMVL2QMXQA-bVfkUmEjYHKNeL0ABtkoBMbAUp2Dux_emB_LqA1v8yZ_earYBERZWaljYlpOM0WxgtqXHSHlFNFwuG7Y9rQt4dKhCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌روزپیش‌گفتیم‌باشگاه‌خیبر قصد داره که ابوذر صفر زاده مدافع‌چپ‌جدید این‌تیم‌رو به شکل معاوضه با حسین ابرقویی‌به‌پرسپولیس بده که همون رسانه‌ای که خیلی‌ادعاش‌میشه که از همه چی باشگاه خبر داره تکذیب کرد و گفت اصلامدنظر مهدی تارتار نیست الان زده تارتار گفته…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/28528" target="_blank">📅 16:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28527">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWibeUhgeDsjs_N9EZH8BRvHxt8K45RS0tGRoyxWJ4Fsd6e_keoW32V6P6bn_gE4rvJQ934A2ncI1a6t8b6s5cjaOFhXCRr_YmyGhf50yekiyrzmhpVxAN2UCeacsb8_knc3XYGXstfavbqjyEedPJ7M8u_xsgcAF3sf9Ckwbv_MpmBWnXE_WGYWSJBVJAAQ5OsTbjlM5OrXqKR3T-irfuzxvJ1HwpKCNp--z3FmHr9GkuurmfKE6SNZbfJ1H7mg3O2LrD3vaCv-lHEVx2ONCYCZqMIiisHM8M3jvBJyUAlFuYHktkxxk3SE6gFerqcDJVdILd3nlgeCWL3usLnmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/28527" target="_blank">📅 16:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28526">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zhtl2nOFMkMnGtRB66siXdc8zamk7Cl0H-qO7A_KqJb-nPicql0CB7wWFe-TuoiD6jB0hC_DpLfMVNkK6vD6xxC-vRFcpgqhiiHQwIq4R7rg0WUItajx1p7H0jvz4dmUSEB9vhNUMwIB3iLf7ZgXIfoY-y5JdjkKIFKpX9drZM3FwEe15cyJp4DTJzqVLCWhvUQQ-0uPdQJOuEvuC5NQUL37G2yOf94LJ-hYbkHQiZucvOYbEJBSjKsiQF1uUP88p37wnhfGCF7hEEd_eUySbLNI2ReWUFMPQ1GDODQLDqvpg_y26pmfCgRDCtyFNRH-rZ6RezP6UtItSy2wflGq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل شده. زنده باد مادرید!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/28526" target="_blank">📅 16:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28525">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDMSZhXqv4csaECS0RGzk0-kVgIozwKIJnoKxU6hrKYRdWLvZ3Xv6bwJ_tXUfOxQi6gJblV9DRqI93TNnY_eKFQBgYoejANdy8Z9FC1UBjE5tzQOsZ0k7a4wmfqYA1zbSKT_I49sEL-xK-HveRevS9WFwmb4Tc45yeNazm00VsEoTvpN--Ym6IaDZy_LQibNy5hl3buPJZvowdz3nnAmfmwK3DWANqwZFLQrsHgBs9NIbepgQMNfT4mtgz0zUx_xJM5y4qtlho2m69HeVtN2JhPtky8J-Mj8yRPefL100TTEbUmYt2plvvRRplsotXLZlqewOTwhXzQfNjuCNUalZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛نیمار اندرز مدافع‌راست‌سابق لگانس که اخیرا با قراردادی 5 ساله‌به‌استقلال پیوست بعد از توافق بین دو تیم باقراردادی قرضی شس ماه به اس. خوزستان پیوست و نیم‌فصل به‌جمع‌آبی‌ها برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/28525" target="_blank">📅 15:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28524">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=n5I0PIxC4SmTzyduawhy2ljSfOA8Z6K8XuOVU-pr8ImNfQsLq08DR4DFNEhwN4EplYlSqDVxLl_PLhtJB87QaJAfEM16gFZcGIVcu8rFkxCA1zGL-wjiPdLLELv6z81mX5ZBr45uQPul3qJt53eVY24kDq7BpD_YoNW9A5Am14dls-uwpsoJKdKwJWDYuvEW3ZcYgaDg0xgSoYrMKerghm5ZqrRdOWCmhBN2X_KpF57uxiZIz87Tly6MgdiggsVXTvSGarS-in2kUA2vTb1TRn1nReKlb46Wrx0ukoIcWKb2hOq7nT2g2lMHoXgVWSmqLhie4A5kF6qitJQyufKXnp6aiKUiQje3yJNscaqzH1ENHJlXLpA0x_jOdFxLIUoQh4KTiZ7nmUjUCj49lA2-9zEp0ytR2pNrdANqHjF6N0lBbjuyk2hlQC9ybhBXHJAjQOjIbHyIkBjwSHD7CHv0Km19LPLhQtVKyibku2ct4VpYIkuswv_j2apDI3JxAUquLWtMeHvMcbUGgGWxFYAtEl9BI0C-5CDRPc3beK9AQUl00k1JrP2-afuD9Kxbw-NSjlfPb8Wmzrn-GqJbNoVrdFaQzTXaFNjHeVSIc-bIg6P1WWKM0r-fHG9OqMy2_JtvbQxD5pv9_Q3_7t2OR1WWI7MHXK4_GgExSIFZfpwvSn8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=n5I0PIxC4SmTzyduawhy2ljSfOA8Z6K8XuOVU-pr8ImNfQsLq08DR4DFNEhwN4EplYlSqDVxLl_PLhtJB87QaJAfEM16gFZcGIVcu8rFkxCA1zGL-wjiPdLLELv6z81mX5ZBr45uQPul3qJt53eVY24kDq7BpD_YoNW9A5Am14dls-uwpsoJKdKwJWDYuvEW3ZcYgaDg0xgSoYrMKerghm5ZqrRdOWCmhBN2X_KpF57uxiZIz87Tly6MgdiggsVXTvSGarS-in2kUA2vTb1TRn1nReKlb46Wrx0ukoIcWKb2hOq7nT2g2lMHoXgVWSmqLhie4A5kF6qitJQyufKXnp6aiKUiQje3yJNscaqzH1ENHJlXLpA0x_jOdFxLIUoQh4KTiZ7nmUjUCj49lA2-9zEp0ytR2pNrdANqHjF6N0lBbjuyk2hlQC9ybhBXHJAjQOjIbHyIkBjwSHD7CHv0Km19LPLhQtVKyibku2ct4VpYIkuswv_j2apDI3JxAUquLWtMeHvMcbUGgGWxFYAtEl9BI0C-5CDRPc3beK9AQUl00k1JrP2-afuD9Kxbw-NSjlfPb8Wmzrn-GqJbNoVrdFaQzTXaFNjHeVSIc-bIg6P1WWKM0r-fHG9OqMy2_JtvbQxD5pv9_Q3_7t2OR1WWI7MHXK4_GgExSIFZfpwvSn8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
صحبت‌های محمدنوری سرمربی صنعت نفت خطاب به بازیکنان در رختکن به سبک نقی معمولی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/28524" target="_blank">📅 15:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28522">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUpdZTADbNCgdb6qvd3TD0Xwu9oawFYpA9cHZGYlMQYJsaOacqLYzcEbE2DbWd3TEXGJs6SPdscS8YW9a5iown4eV6WguVhCLqI2P6t2-aaXDKw6qN9LGx5JBlKhKkb7VNdrLagE4GCalbtR15j0SXldrOXcWUK3mAfufrrJQ7x8Cl5t2M5ehThnn-wPaT8swl0kZycG7Q-sJgRrVoj15GCIhw6aR5SchDiXmrb0m9Mk3fML5Yx3K0S53TgjhX7nsGqwV1M5WPfo2yzmtsYR3MHw1IGXu9aiPUOUnvbvtNqKB7bMqRBtQqGAbU9hYAruKu_oiPskYukUJzy9Sj66Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaHkp0q2ZpwPPIurcgvOvTUc8bEKS20fDwBBxv5HdYiA3vAgDQvX22duREQYIgzCCfL6EvXK52sonYgGRkj2KEqsvTjil5oIsKV_gv7perGKfnXVlnXpyziELnQNqS6bItXr7fbK2KprnXrL867RTYF4uv0FlFtotUEIyAJbErUkmqUlmBc_4fYRlIoREtWXkoRzBCt_yXvmQvEx1REZu21BFTQsfwTKb-e-o7k3aLGddYlDjUBAysbswGev1Pw_owzc5U1jBsVEXvQAd4nOEak2nPcW9PDiB8CP8lb8s0ZkzDB165RuMjsjOPhspGPo37gTnmRzYJMFU1OfFZCFkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/28522" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28521">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOzANpcasWpaDtG07eMpwY0QQbiXkczGsNXXCEY2aHAK5rwYWyQr_BsuQYo0SGqCXS6onmPSkK-dYdktXSr_NXUSAGOaO5x8oAd9Td-Vc_mlDQ3DffjOqBUXU0WYfWz27gp8LlZuxkxcEY5FVkFkEfz8ayyqTLwATEAuVIdxAwXQEevXlgxfuknFc9QdqMMe24KoV9NdvbyjcT_if_pLA1e9DrxSYW7XBDkrhINM68yNRDVADflos6KdRAgmpRSOdLvu8H5VnK95GIX4xDzXUjh7roo6jReBzY0Lqn1punff7sw7j0_vdqktt6DV2Dj4LPFWAnWbFBsSupoq5bRfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحاشیه‌دیدارهای‌این‌هفته لیگ‌عراق؛
یه بازیکن عراقی بعدگلزنی‌واسه‌تیمش لباسشو در آورد و دویید سمت جایگاه تماشاگرا تاباهاشون خوشحالی کنه ولی هیچ تماشاگری تو جایگاه نبود، بعدشم که برگشت به زمین‌گلش ردشد و بخاطر درآوردن لباسش کارت زرد دوم هم گرفت و از زمین مسابقه هم اخراج شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/28521" target="_blank">📅 14:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28520">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8oTVhY6uLsn-HVeLuHRZA61VbUTC_4I02wYP4LE8S2TqXZ-o0rNeGBDED_cI6MfIzQn7xgBmSVVDFppze2WxYI_m_bGM6WPAhEVavnBZSEK6EZIghHwN8MxlXbCsCfT6MV2Q59ir1Hw2uL-0DkcWVgnKYbcdT01IBQ37j_THUrbEHCxIyc3QNIXR5L5UxKvrNJAzOvkgB6h_gZJKOnIbdBCTvfZbFYxzHAWLQ1OKN83Kz_MJdK7OiG2kOY6wyVmvZyov8FwCfSYpc2GQyUvnsvPfLU3tuw10QxiT7fALM4JP7qAkvvFdGtwvdYmTwbn9o8u0Z1YoGIA2Y2uajkqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان ستاره 36 ساله‌فولاد از هواداران این تیم خواست که دربازی روز جمعه مقابل استقلال کل ورزشگاه فولادآرنا روپر کنند و از مدیریت باشگاه فولاد نیز خواست که بلیط فروشی رو رایگان کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/28520" target="_blank">📅 14:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28519">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTqvw8m0_mpT1dSX8YNQM2lTFAy6GEHHI_f3qmyB1oJxPFpyygW0-LS_QfvmmRYeDKjCxvuYuIwrETtR71gsqMERgeoTKb-UndQVUgxAu8iQBw4U3TJn45_zmxkNaSMeHeGRijCYHjB1DZFvnOW55MKmE9GitdmUoC-FHxNsFLbNjSKbOUqLd50-WKCd7JE4Ti2WR2Xss64IW_4OeA6fKw1zmBIYbu2eUcE3aAox6pfusyDvWLdQLZ8FCkh2UC9rmk_LF1pFqcJbAx5PokLFuK5WLrK44wWeBuAaiGYBHzOAXZfQrUIftAkMqWCKGhDDFrTQJQjH0kN2XDoXfr20Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دولت دو کشور آمریکا و امارات براش ویزا صادر نکردند و مسابقات‌جهانی‌مستر المپیا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/28519" target="_blank">📅 14:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28518">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bU3y_jKePIQ3xA2X7xzzx81zeAgRL1pBXztBgEOyS25oaIlQUp8jpHS74CZ0d80-wTMn1zO-WtiO3eD_5cf0GynKbB9WiXSxZno89a8RMzJTGXLBx7LsBcOFT9bmsLbvk5AkSG-hhtIt7fwNIA_WcPjjS8PnA6UvOkfPGXyhe-waO9YQMDNGqqn_pnHyymVkBnvvVD9w0mFDymude0DyBtXe4C27GZeYQQFUbYVuBn_SL8yaWvAmvWFqXAwl9xDm3scOhVFug95gbT8oBJkUIh_3q2XkdoEOdQyELGcXXsGqvTnpOi_5olxq23x6h4yqBqzf3RYdl7p6KQ-hGp0NKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/28518" target="_blank">📅 14:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28516">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=j071qAeLj9wTbIylzb17uaiZsWTENLZmEoJGWQzPS0TbEzRCa-TgxRt3Oz6sg_B9AdhOLH-NDsTm329uCb4VrM6sbWolxkCTY16MsipTYsjE1urmuhKnDeisVSAKGTzWfUw0bTe9rOxW23snHZQ7MjL_07NgGwzcDK_Wjm21rgtPJjNQY2MHfvQ4wB2NugZfzqT6xYPBFwHnhcddLCFwPRDU5_Gc69KdzwqQCWC3Byx7GbIizGeQCaYcW60pPmRZc_xpPmVTU29vOJKYEVpx0izzoED6QoPf7qfe8z-1rxGib-qMQq02OOZgifKROSV6wbGlirFOIDl4A6RUY0vijDWqwqI3gj2yc0IfEJRq0sL12BYwx0iwtRkwmCYoEvjLvvAW-b7JqeU6PzyFBlA6igqL5nOJznKQr22L3uaE3NSTa5tX6x--Fwf0H2pUeCV4epw2gMnGEi6e8hjeDlTOG6UCFTdP171CSSjgvLYG03TPyrF4BFk902Ta96DET5gOuth3GOXVXdY8Hkqy0aXNZD8GGn1v5_0tyCnWPw_cYi-p5FKNQNtrjxaYwuWf_ddA7lkezxHEUdr3rOCkppfd1fsVxhCs4ZkpKjw_o7x4W_T0-4dU48vkCy7-glmTxlbj7sdgb9f58VL0EFsYJH1b_3idwHHbbBB9guCfdqf0WRo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=j071qAeLj9wTbIylzb17uaiZsWTENLZmEoJGWQzPS0TbEzRCa-TgxRt3Oz6sg_B9AdhOLH-NDsTm329uCb4VrM6sbWolxkCTY16MsipTYsjE1urmuhKnDeisVSAKGTzWfUw0bTe9rOxW23snHZQ7MjL_07NgGwzcDK_Wjm21rgtPJjNQY2MHfvQ4wB2NugZfzqT6xYPBFwHnhcddLCFwPRDU5_Gc69KdzwqQCWC3Byx7GbIizGeQCaYcW60pPmRZc_xpPmVTU29vOJKYEVpx0izzoED6QoPf7qfe8z-1rxGib-qMQq02OOZgifKROSV6wbGlirFOIDl4A6RUY0vijDWqwqI3gj2yc0IfEJRq0sL12BYwx0iwtRkwmCYoEvjLvvAW-b7JqeU6PzyFBlA6igqL5nOJznKQr22L3uaE3NSTa5tX6x--Fwf0H2pUeCV4epw2gMnGEi6e8hjeDlTOG6UCFTdP171CSSjgvLYG03TPyrF4BFk902Ta96DET5gOuth3GOXVXdY8Hkqy0aXNZD8GGn1v5_0tyCnWPw_cYi-p5FKNQNtrjxaYwuWf_ddA7lkezxHEUdr3rOCkppfd1fsVxhCs4ZkpKjw_o7x4W_T0-4dU48vkCy7-glmTxlbj7sdgb9f58VL0EFsYJH1b_3idwHHbbBB9guCfdqf0WRo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تقلید فوق العاده صدای گزارشگرهای فوتبال ایران همراه با نظر خود گزارشگرها درباره تقلید صداشون. جفت ویدیوها عالین حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/28516" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28515">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tT__dp-f914Wj0epxOkxe7tFTQxtSaJ_KuFrIeREHxF2GmpJ39YFnLjfPEXZm4IcJFH7DLR4vooT6V1JLOsHCJq6gNS9axZhKH5sGcwc8FNli4hmN-gPFPsPKS3IymPGReEgxzQqyPxTRYK-0TEjse9JwaTf9turxC5B7xoKDuib1GBw6RIqdgZHNUIAOoB9N2iv3IftM4aKhmUO-_NDqzTBbmunRxeUGlbjFkFdFxSVs2_RfrXcPH3RMgOJ74COXzM4NKtrj2qPpMqxFnf7ZBh2-mpgsK74KVIHDIJ2Ty6M2J2IhCa2fQF_UelRTTsFZRS8AxTnuWVS8Nq2qzk2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
النصر دیروز درهفته‌سوم لیگ عربستان درحالی تونست سه امتیاز شییرین این دیدار رو بگیره که از دقیقه 12 بازی10 نفره‌شد و دو هیچ‌از حریف عقب بود اما در نهایت با درخشش مانع سه بر دو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/28515" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28514">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpPihQYC4vZxbtRnfLHeoYUEmV94zZchBiyhaLSWVYiITrLv5qqY-ayAleXPX8Av1RyoJNZE4QtW_pDX58-EjhpatiDE7XVtXVPSZ4mW-chUelp6lxQEtOv8G1Z-ESXQ7AJQzySHhqz44UsHaL2BkyZbcfHj_N2bWP4IT2V0aRadzEZBMsLmEWDQhVg-xZCq4f8hT6YMssKjDXF5fwg6tYE-FsUOk6KmoMw803mx6FJUB89KbWHNiLDYz-KZTXRO-EEroTxLA16I0eY0AwRONILeFrj5xX19kaDXAs_zwdcjwvFND0bUY4Yt5F2_4z1M5LPMIsyetIiurI4fPIdBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/28514" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28511">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o29H2HI29GgM0P7rfBiOaSCSZ4_eu59mklRMzmV7VZUSuO-a9fzeRXxe65rKM6GHGXu_adx-8sjeoHe5MhVMTNgeRBdtx3ue4AEcnIBquktDbwt_ytu76x-uwbZuXar7MwL2xgMwAbunrH-CYRFBbWYloRjGInZoYAPq4921QVUH0dGelkXkj5Ii7xlNkB3D85fHjVOdobCLGPIrdKwIxyrtCQxIlsfynCiCzwkBfh50o2v-0IGFDSfIW-NjzOHbQ46e9Useo_KZyOQFh9uAMiboLfQQus_JeMi9YPrD-8upjMZSa4xsMX-s7jSjQG40FnO_CtDuyRcLiPuqBsGe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/28511" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28510">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ua5uGqLxich7OHRgQxA3-S_S9PUNCPwPxqrTcNusE9V2-7zFCVtZHQ-MaITmGsz5WA0w68XhSIBlCYfzAAjtsujsjcTaxSrG1shImyekMN5A_a5vsFXZedgntqbQkW7lqQyIEfpWM02bjnQomg4_sHInnpF5vePYmqKvNc8EzMpexzbpCdNH1x_zU039AQpkJN5AOWBdU53drjd16QFF-Umrlgmc0zGIXjT4NPeqhwD8gyqKzBmSxfh_qNqYHReli5pByQ5va79ajFePh8iwaUWvbvRCjYtzs8dD_c6CSG7AlgsKTsc5AJ-52TRbVrsTALP5QfD0fEeC2QF-QikOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشریه اسپورت: باشگاه اتلتیکو مادرید آمادست که خولیان آلوارز رو با دریافت 150 میلیون یورو به تیم‌آرسنال‌بده و توپچی‌هاهم برای پرداخت این رقم اعلام آمادگی کرده‌اند و حالافقط‌رضایت الوارز باقی مونده. سران اتلتیکومادرید به آلوارز گفته اند تو رو به هر تیمی که…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/28510" target="_blank">📅 12:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28509">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5DkAHsLrPWhzu3359zuaHS55clGAXj775FhcCSYLtf5GdYwsSBvx9eg2TZa_32dYww6GEgxQMfhonBbRGMU-RasjEUqtaXmX-eOVQnS4ZI5B8VTZPargESzIEIhGHFr1AYIaqqTIvkYFOEZntpNVrRPVZUOTW6Xky39UzGdf9oCZfEEO5m3egjV9Vkmceezuhwk7pN-9E-piQ8yqsYHBBzN06Q3hjPzTvLYlukH531TKq0WUXXf8Dezb1evckZcHbeosi0wzZshY6inXc83vIX2JV1kPjPDInDwYYZTk-gJObFY6lCei4hhPwGOzvkc1EhLv64YSxO9yUjXe74NIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/28509" target="_blank">📅 12:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28508">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okoLGpYMU_gRhVfnDQWzirYfAwl7FZJpgi2D47OEnDrDoJia_DYx0PzT3Ad9mB7pBxcociGiU6wEKnOGL1YzF78fe4SNcTrYNAqrmqnQKGCg0vUu1raCm551FzfIzt4ZygG1XJf1xLYeWDQq1vKeFBesJTxfiYeaeYze7MkjZ0yE2Nn0L_uZrpUHNQKKcj4uze2gtwU3imy8nG53N4gWioTvGbsn__-ZSVHd_Qf6QWdBvODzRyzMyALXloWCP66E-8WnDQ0GaTZL7CjK02b8s2LpTKraGVJaCd52ieTEsLLQqyA_fTS-kADpHqFJCfUW0ZMGR347_IeFrSGNB3dfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار کوپه:
آدمای داخل باشگاه میگن که تو خیلی ریلکس و آروم هستی. مورینیو: عه؟ پس تو یه منبع داخل باشگاه داری. خوب شد که بهم گفتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/28508" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28507">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=BSe6eIW-qYb5RPxXdz7O7M6XJV_VUu68Aj8aXdVuMcWGBVXzGzRA3ZJiZNtPXtkpD3bNr-gKCa6hB_WRnrWmci6xBt-xMruqp7KRcdpOIRxAhPhNv6VCDUMYzXIBMqv8WofFTUKSb0zaHOiLCbO-04p7XpsUOjBEEaU2A7XMTCmE9qOf6FnH6B1YbbOhQy7PK8ytwvNvi8YmjQowyktvMTFi5CDwo0Bng_0JCC8mGXnX2iJ2KBFnvBYzhEFMMcAWUZvRuqzbHnCvaDGTBr99XjdA6QTuILqrTK57WLKtsvc8nUOPEcIVz5QjuDtZV4ktkUq6IWejTdKdL7kx7aak_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=BSe6eIW-qYb5RPxXdz7O7M6XJV_VUu68Aj8aXdVuMcWGBVXzGzRA3ZJiZNtPXtkpD3bNr-gKCa6hB_WRnrWmci6xBt-xMruqp7KRcdpOIRxAhPhNv6VCDUMYzXIBMqv8WofFTUKSb0zaHOiLCbO-04p7XpsUOjBEEaU2A7XMTCmE9qOf6FnH6B1YbbOhQy7PK8ytwvNvi8YmjQowyktvMTFi5CDwo0Bng_0JCC8mGXnX2iJ2KBFnvBYzhEFMMcAWUZvRuqzbHnCvaDGTBr99XjdA6QTuILqrTK57WLKtsvc8nUOPEcIVz5QjuDtZV4ktkUq6IWejTdKdL7kx7aak_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
گل‌های دیدار فوق‌العاده تماشایی و مهیج امشب دو‌تیم چلسی
🆚
فولام درهفته‌اول لیگ برتر انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/28507" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28506">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-mMkNxyse1oouyD1PaOxJUJd24-ZBtlrE9WsQZ9dqpxehn7fVjq3ccDhkpos0LIQhHxS5NttOSFPfN5VehmxycDPJrry95dlyLCWD9-vrPvdDgOXO1YRQsWvp-M2M4ErCV77HeU6BedSElSLVD82-GAeUlokNe_HjEc_Uwf7nrcU_9VRcPRW85zsigOfEyIRkobW9MjSrXoxbJnTbBgEwTExjpKFo1jgYOO-x_9wCcilb_wTsD9_3IrzON-BTbIb8zFSuSFd_MRmSyQXDxZhr5jpT65R32nR94BjE-npNrd75MksGX30lLxurqEVFKItNJYdvJSrd2AbVfovPKYmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/28506" target="_blank">📅 10:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28505">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lnNvUXcXlGngtl5stqo-CtBvAQ7NlJmIQ_1jALJduoSaSQ20TsPCNNW6cJdlF1xCNN4FS6srwDqVFXlJGA26kUZMCxS01TQCFoXDLm471rwalnA5Gii_iPQojrmtAyTyXDXMHU6JxUYv6BtBZBbbVN5wQ0Amf1a4v9FolMV5eLJIQfOIF8bRC2I0G5vxvXhSVhKDp3oi0ts07TP0FSV2pIQGhHb9yhEHzTNX-WZRCwq_4rcuWnG8a6hGesmGM-onE7uFYsrt6JmfEqYkAxu2ftcF_VOa8Ml2Z5qRsLcR728_O5k1mqjPJqHspkLDIWVjEY_U93fuzt0vgBKTkiSQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فکت؛درصورت‌پیروزی‌استقلال دربازی روز جمعه مقابل فولاد در اهواز؛ سهراب بختیاری زاده به تنهاسرمربی‌تاریخ‌استقلال تبدیل خواهد شد که فصل جدید لیگ برتر رو با چهار پیروزی پیاپی آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/28505" target="_blank">📅 10:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28504">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Motxfw7cuNvCwZKmmH1zK5PSWJwBXb5ZIcDQWXA1Tn2JEmn6o2JymhCJgZGdoI_FKyPGf_zA1tjv7onoQG-cPe_stfl8xpUFKSivJEPF6VkIhZhOwIIzwcV6aF6J1nL_7tgQ_dmCxsAkFH01ZC6m_F6ygV5zy8PFemuEVK-NzpgtMXm9tkZIrd4-QZbFcdbBKwb6b8DU13ZVG-DEqIVf-Tc34uBYyzjAfHHK82dOXQvkNFJU4lz5aOo1pNoWbMHIDcd0MLCKMScXse61pvSD8Ra6lyIopxYlr6OzM9W2wEj1-awIQ_1PlNbzt5pfkEaF9X_xGQXukaZ6jD-bMMFPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌چهارم رقابت‌های لیگ برتر که روزهای جمعه و شنبه پیش برگزار میشوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/28504" target="_blank">📅 09:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28503">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6eUwBpfw1-uDuZcxUdWdW0qKaYwjcKXSljp2gHi-Dygq8119JTaudS6ajme4QLqpRgM80JedRLgXFyFH7XPW-y_mY82qdWhCpyHoiQeuzImDCuiSFs7yd-fINz-N0Q1uDqne40GHkJ3eKlzuChhTKlN1qDhcAx786cv9CgdSX8VL1dueISc1IdJ3nOsLsOtBp-RKxZI4JexBjCh2r39rmSGCrkEg0BmXR-C7InfCjU-sF8nL_ksTrCYoyLWxrT8u4Zp-DnT--iiX8SesO4w-O2vEfLhCRfbBbIlOqar8H6SgNb9x4eAJ8Qvag-HZEqOxQwS4AsMvKohm-G3jRKqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوانگی‌مطلق‌درسوپرلیگ‌بلژیک؛
رویال آنتورپ با نتیجه ۴-۱ مقابل خنک شکست خورده بود و تنها ۱۰ دقیقه تا پایان بازی باقی مانده بود، اما در اتفاقی باورنکردنی‌توانست‌بازی را برگرداند و به تساوی ۴-۴ برسد. سه گل در تنها هشت دقیقه برای‌رقم‌زدن یکی از باورنکردنی‌ترین بازگشت‌های‌فوتبال درفصل جدید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/28503" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28502">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrMDWBI61gx_WTktSiVYtYm1QeC3bCXnU3_loy0mXb1yaxNCMC3OgSdv9bEJWq01E_bdQrvPVYUyH753v8O9wxGgRgw2Hl2RfVYQwqj8PPNq0Hv0Z58fJKtyjVNiXaPmtyoz5QrR3kcBONTY4_FZzkwge3riVXDbhH069CCrd3lwYJ3fCo_8EmuZgTbjoEFhQVK33tUDLOBmvpqcI6odc0GlNbEqZAQF1IaUZcTjBcsRAuw7WXkT7HPUOT9sENiHr4u3gNWxXyc7_Y8aqjrIDpnc8_dQLU9PUrMSeOzNbhL1N7x-B7wjNf72O-u_BHD4162baYA2sKhzp6ryEjIF_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت‌تیم‌های‌حاضر درلیگ‌برتر فصل 1405/06
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28502" target="_blank">📅 09:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28501">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nKtXz-E7OO4jmIpxw8wdk8-IbAyRDUYe5yEn2bk_QrII-X-HFZbGwFGiyNaz8wavQ1wVKrQipjvmx0ay3WvgfoXiHxuZJoK8L7il-e1HRaFDxNu8hWYZDNG0RMKqZPlM78zdFhY2b0BfCgdVGRVjg-1ZouQdwncyVNyT8CWyY1rMlMcUW9PKNv-7Jdsed0u3psYuHk95XB0NSyYVVG-7Eb7Oqycl_AjKZUygLdKVRIXVfbHRuT-0I2h4KK3RK8nDLZHkCvjVKK2TsNX-67FuObWIaJZ-UOpyQetpZsiukaNqap82H-Hy2391_xaP4x-2zM-t_CbJun5SkxalV9G45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
مارکو رویس در گفتگو با رسانه‌های آمریکایی اعلام کرده به احتمال زیاد در پایان قراردادش "خرداد ماه" از باشگاه لس‌آنجلس‌گلگسی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28501" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28500">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMisVKv_4w9X3Xt9Hh0hwEd366lZHZ1G8jHGEyKD_g9wMJTgexlilFX8t7XWDYpXDIlqMK0Q_VVZyU1-hVhnEhZGKzXKJVWl1tzupanTew_CKiqYN8ixll1FGTOZdnQvCrBslPMR6hGEdj4QWp_Xu9NPlvZWtjGavlm-CEVbko_ti0fHDAJWQuqpNlVERcnfENTMQObzINS8KkqOMCC6W0LfEp_xq5kvp1D_iSgbJ937jBy46zZH4Gt_VO0ZwkARHt_dCbX7ekkIBYah4zNEnfiVrePIHSCTogZ4XMxsi-zFIiZMuCwyVnaEqsOsTv6hVk6V7rpBRemjF1YqNAJmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
دومین آزمون مورینیو با نبرد کهکشانی‌ها برابر سوسیداد در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28500" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28499">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibgdhKmwveuv3E31Za5MjmJtJ792hObZ2n11mgiSpXx0PBY9thjiRD3fcoUES-WVE79ZM28dM1HgSxy09pcq_tsx5-hQzkm2TlNX2L5_0wV0wUy3tZ_UFjPa6P_m1ghBhi0FRHoHV6N2c4XR9IwufNM6LZGNpIfMbVCFCi747UqavnjS2RR2DdcFC5hUPjFPrSAcnFI6EyMfeCj8Aqg17EYX0DzZ_XxYDd3W_J_aoAPG8OOWDIMCiYIgMBml1uzlGyVy72-mmNKutz-tinjJ9-rfjlHIOgqROCAQx5PfRPDjNyHJh1MvxqlsVmO1cxxax1Hwni-MTaeBzp4Z643iTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
بازگشت‌دراماتیک شاگردان پوستکوگلو با درخشش ژائو فلیکس و سادیو مانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28499" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28497">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaTNy5N2yow_1J1mA46XluLJjGQP544eZ_NBvIqi7rECJbVDppbv77Kj_b4d4pelZ0qfBsMWd8xTJA_08wOk8_I4IwXFZy09KJVx2CCMYPG8AD2WciPQMPCc7ZFs5f4mNUr3v3HaBGMGsLrLjf64pH4qz-jE4T5O283WLvsFDACm1lRrZCVMadB5LzZvd-dZLPqGNUT1NU2d7WsCaLOYfW7HvLaRUrlsZX2_dkKDUDluNB9340EjgxN2hxNzwu1y9esJMiTowIt4avYSEmCpIjM2F_BcYg0fgh5wNguRWHC8gNvSO2zuNerzuQjHrtLTipy_VSaI2u6LHrp2dZvFyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛ باشگاه آستون ویلان پیشنهاد 45 میلیون یورویی الهلال برای‌جذب اولی واتکینز ستاره خط حمله این تیم روکرده و قصد داره با 70 میلیون یورو این بازیکن رو به عربستانی‌ها بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28497" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28496">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=LlVyYQN8MrbbUyue9_tuTtOTESS8TfmekWudma9eSu3w84vHCVBWT_3IWFfubCSBXm274p_VFbgPLNymWUZEIxz8MVWjB3WDjHzzDJ4mwlK35VeI0oRe3Gf51UxIRtnRQHY4LrxSHE25hRlcX5B1EUNU8vHXdj7voYGdr5Fm_ZlXsx6mioHZyrDoHAghqJaHxsMDEZ5qWBxj7Bw8gwFI20viB5vI-4engDi6XDscdnTmeIsPxuPw_ppeaDfniaU6uFekN9OCPx5VUQrs2w9sKXPZhdxka223-BzcFPCKttUVpxxo2AoiBoFpQ-aLNCE7gWIpyj8kzNZK9YtDEt3jJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=LlVyYQN8MrbbUyue9_tuTtOTESS8TfmekWudma9eSu3w84vHCVBWT_3IWFfubCSBXm274p_VFbgPLNymWUZEIxz8MVWjB3WDjHzzDJ4mwlK35VeI0oRe3Gf51UxIRtnRQHY4LrxSHE25hRlcX5B1EUNU8vHXdj7voYGdr5Fm_ZlXsx6mioHZyrDoHAghqJaHxsMDEZ5qWBxj7Bw8gwFI20viB5vI-4engDi6XDscdnTmeIsPxuPw_ppeaDfniaU6uFekN9OCPx5VUQrs2w9sKXPZhdxka223-BzcFPCKttUVpxxo2AoiBoFpQ-aLNCE7gWIpyj8kzNZK9YtDEt3jJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28496" target="_blank">📅 00:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28495">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=XQ0FCQyHtnoNsFaYSZ3oDv2drd8WAEr5NN6kxQrFnin5kjyYuqg0J12c1B-e7fNlXVkLwAxH99XAbLs5tRxJVpokozXcpSVAxADkEnBVeckHFDdNm5hhR4bqi3JY2XFEejSPbInNCFEwoGDTMHX-ORE7hvsDE3cuQT04Y7y26NFo9RDZRh9AVIpYoV7WboND0vX5mFHqqXqs2Uo_pquF6tTXmvDPTpL1bu7Ijk2GK_DMR-G7u78pBcmC8dYhBR4Y-S7tWOC5xt8nAYiJiYjo4IXQDF6l3otS-IW4m4pjtGu4gvQQy8b8M9dMHm9By1K6JvFrxmZGrqUgeF5nSZX1qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=XQ0FCQyHtnoNsFaYSZ3oDv2drd8WAEr5NN6kxQrFnin5kjyYuqg0J12c1B-e7fNlXVkLwAxH99XAbLs5tRxJVpokozXcpSVAxADkEnBVeckHFDdNm5hhR4bqi3JY2XFEejSPbInNCFEwoGDTMHX-ORE7hvsDE3cuQT04Y7y26NFo9RDZRh9AVIpYoV7WboND0vX5mFHqqXqs2Uo_pquF6tTXmvDPTpL1bu7Ijk2GK_DMR-G7u78pBcmC8dYhBR4Y-S7tWOC5xt8nAYiJiYjo4IXQDF6l3otS-IW4m4pjtGu4gvQQy8b8M9dMHm9By1K6JvFrxmZGrqUgeF5nSZX1qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز اولین‌تیزر سریال «مرد سه‌هزار چهره» به کارگردانی و بازی مهران مدیری منتشر شد؛ مجموعه‌ ای که ادامه‌ماجراهای «مسعودشصت‌چی» را روایت می‌کند و قرار است از اوایل شهریور ۱۴۰۵، به‌صورت هفتگی از شبکه سه سیما روی آنتن برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28495" target="_blank">📅 00:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28494">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQUpB5ed7j5r-TKWcdTppiX1AM-Q67x3h3N2fsh4UD-0b8GCC808DA_aGhd5Egicwv313BW-7JXu8gGTj_69ACnvb3MAXQHPaxltkcCUP6dFLgChb4dwnHbcvy3kKJgOpfls4QBwl2_xD-falPiVhu2b_vpMIaj0tcMQ0tMXeuy9odU7NRgVIek49ZKJdALvSjTUxQm0sE7PUZQPGNL_mmDARTs0HBM0QTR6GXXIrQ3MHcl3iIjSVvJN0pLlioqEOV-OCmJ2qNy-7daJUpIwCXr_egpC4sHGm47sscfUJnHTG04MJ5KLuUK_KWxDASLZmrTHjwAOfL-wMUNb7OLIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28494" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28492">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ig9FGP_uulgRNUe5GbDtu1uUJLqb-TV1ohwXyi0p0KUaHRB3Rkzb_U4BZlO1ePO5D1MoU9PMM6v_AaVFitQyR1JxYIBxh1G15eHYG8DYq0kYtKbGE5ayVvR4Rjm8BrVZHuAsGJ5_vmsIJVeJ5V-xDTTyZ3VIXwcvJWwifbzjnPYom2kQbgQcvTaNIWwCse-EdPlsyEA0E6pIkI1JCvAHMs-fheRxYWvOgUTUIx3H4rZ9dYqZT91AKQ9BlvOFbenMBb__7WBt5wEV-HJ-I1TtFZzgQN0C538Q4tGpMoJcE7_-L14WyohVqboXJ_TYbssbcjRB6Mfgy9-fk0jXRsHFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d1xkUmXMgVDCPzZhcUxl5_ZfMlExxNkxtZjJwZndWarCkZ5oozALgeocA6AJJ7djDaD8XVT5uv__cwuo-jk8lAEYk7gDgSIw4ziKhA8PGFUT7xByUYNBb-5JIXaNRUu7v2Hl2F51HDpqX1d7VhUCG0k4i2HVO6yjZ9rWDS9oCQzSsrBM5PkvLyIyUSU4NhGtflb3yzkZVeWMWbhCcq3yKfgBAHOqT-lCmabP0tK1k13wHVUQkbeZSw9kP9SCUPoqArYuhvRwhCmMAeee-48s-V4fK89RwXm1qYWVdubBc8PIga5G-qMeqvaZDf8ICSu5vagY0hH0HoFh8YeVjikNFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28492" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28491">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tN-RNdENhNNThLc1wLkdl-VZ44uA_z2MdkB1sNa9PmM3qh5_ur3RGLSDsEghnfigMCJai2698iLPYVeP8H9--TMkbsNPV07QFxSUI0yAerMEIBApTsjezXdSSJWqEJlN7lTwcC8pW7gX216kTcy_rnzNFVBD0ePfYPkOg8gf_xnzzGBZVXrXFFon64ZSo5kPxDKho20AwCRrz4Mbjbi30rXDeda90qUo2oow50xatTcsTEgUUVjBMHY_kQZaYgh1ceAvs6GZ4v4vnKrL2YFKq53YeyEIZwiF-ii1tEClHXlHxtMC8NcJFzYbMzvlKeH5Ky1ii-6AMZ-U2pgPILjSPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مصدومیت اوستون اورونوف از ناحیه‌قدیمی همسترینگ بوده که بارها در این ناحیه مصدوم شده. فردا از او MRI گرفته خواهد شد و میزان دوری از او از میادین مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28491" target="_blank">📅 23:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28490">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d926debd47.mp4?token=UtL7WNNWGDWuNfvuVFoYMdEx5YRVRxbnA5ZP2AyU-Pk6Axncp0Kyt4QfBeoVT-FkwKhAL4YmffVeRdFAhPF9ZjLsaocoKw1d9Yc7yY-Wb94dW4SOvAcA5FExfHnCmg4V7yLJQHcQgzOQQkpoedLZ-5U-1D1TwMoCFpGcwkLs1GLe1TqkKKeCBC6Kx43tu3Ay7NQKkGXr6vSkAIX788f_M4O-mia9kfAxJgyTmViX0Sro-Y4wQLd5QoLyFZvUWGJFrA8BSssxjXCVTYs5o7JYT8rCwpfTt9lSNgUrQ42ke_-C4fBC_DpJqh8bVHeErXZ9nCR9m7eJfc591oPWeEkvYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d926debd47.mp4?token=UtL7WNNWGDWuNfvuVFoYMdEx5YRVRxbnA5ZP2AyU-Pk6Axncp0Kyt4QfBeoVT-FkwKhAL4YmffVeRdFAhPF9ZjLsaocoKw1d9Yc7yY-Wb94dW4SOvAcA5FExfHnCmg4V7yLJQHcQgzOQQkpoedLZ-5U-1D1TwMoCFpGcwkLs1GLe1TqkKKeCBC6Kx43tu3Ay7NQKkGXr6vSkAIX788f_M4O-mia9kfAxJgyTmViX0Sro-Y4wQLd5QoLyFZvUWGJFrA8BSssxjXCVTYs5o7JYT8rCwpfTt9lSNgUrQ42ke_-C4fBC_DpJqh8bVHeErXZ9nCR9m7eJfc591oPWeEkvYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ژاوی هرناندز سرمربی‌سابق بارسلونا با عقد قرار دادی تا پایان جام جهانی 2030 سرمربی هلند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28490" target="_blank">📅 23:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28489">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28489" target="_blank">📅 23:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28488">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmOXA7URvTn-y_3mIYQwGfCe-J-jB8Ie7BCYB628XAAzwoLG_QzJn5aLf4sQ3wwmGOwqDOhrb-bow9xLWwcDrv-Twi19NVhPvXX9CSeqIHRW0OsRxxUnOS5SRs7tBzV2uEd5VNjI-6rV6yQpdbyPpq8nqxi31v1EbHvmy0uIqGBKYjnzPIWVJQN8Vc0tn3e59p52PfTOpJofi2tmqUk2JnTl_9ItK0ePCdXaqynKQz7HY5v49QSIwmWGsu-aegtNpIHylt0r66kNlOIvbYNFOQNUgNS8oQj-A14QESHQXlQQ-HuNMBEBojMOvdRDk29Ma5O5RyGd2_l8zIFQBGDAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇵🇹
برونو فرناندز ستاره پرتغالی منچستریونایتد بعنوان‌بهترین‌بازیکن‌فصل گذشته لیگ جزیره انتخاب شد و جایزه ارزشمند خود را نیز دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28488" target="_blank">📅 23:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28487">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlhHJjHBJy2OYJGjdbUKLBWID44Prxh34dt6HhxhmRysqJoTXgOR-M1MAXV4ax7X8e6vKTz4vfuF0GAbUUhwWkeb2rem08Nd5vlQUTX7E90FjVeEPQA7nu_zmc8zd2U1lf_MlG8GlsZ220Lzl3-59f4Dt_G3zmdMQFc_x4pgQepfdWk7hgoZxSwn2j6xvxfnPg1Vsk91k0EOvldbTik57xYPZlx4VRkNJ7CUxbJqcrUSwJOhiGkHFSddGLU2T3-Jg5aQoDsTY_DmDBWqq4wuGNuOzrYBYGgldGwfiYsy5dybNteEzqB_hqF2U12MuWz2qRZjVjVYzFbug63rgsuM6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
ترکیب‌تیم‌منتخب فوق‌ستاره‌هایی که فوتبالشون رو ازباشگاه‌پرتغالی‌اسپورتینگ لیسبون آغاز کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28487" target="_blank">📅 22:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28486">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=lBRKWWXY3dzUq0pDE166vFThlqqA6FSYMT8jsHD1YFsxA1Uk6NfiFtPEs9As2TWxJg1--BZ3oxlWl2aEI6PixHoaJN05YO9YFj10dtAj2Ve9TZ88XSpM-7cgOyq4FTTb5fOal52Z4F0alMPAdOAyI0q0yqovoEab27kV8SqeMVahbq5pAyPLd9_IqKpYsxvAXm0PozsuV9dGoEmkKBOUHQCAmISONR_tqZm7Xq8E_JkusU9_v_tyDmbCEJcqvuj2NkkiVGyWfYMjLLh9NepM13o5E5dQG-0Sp-n5IGP-tFtOVvE01N9PZNMbmSLUuyD32W2Hna5-QdlJKN6dpLwsfKKyTEPGrPFT2fxFONk4mnMxLDqYi2DGo0ROnSL8eTzXCIgxY-c3sYOxu0dVhYF7UETxEm_pPK8JZ2KOATeQsrTe4_mOZjHuV2oq4lgb0cOXeA2VV8rN3tl7uErqhJolR1oPUzAjSFJNG_8X9wEhwptZz66E6VmtHt3Z8z6uJ7LEXNl-pDTTo2kSpnDdqPPSwrsXM5JOhJm2vZgr8pBEfaQvh1fEVPvJjiXGCjYdxsweG4Cx3rQA1Yi15_5TCZbLQ2hewj1xT8TDh0sZAsAkZMkqTgqVqr0R0tAOzsTItakxRCQ1e_XwL3BgIP3MJIZ_Sfd0PNEk4uv7rj0u7mI4Rf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f05b52e15.mp4?token=lBRKWWXY3dzUq0pDE166vFThlqqA6FSYMT8jsHD1YFsxA1Uk6NfiFtPEs9As2TWxJg1--BZ3oxlWl2aEI6PixHoaJN05YO9YFj10dtAj2Ve9TZ88XSpM-7cgOyq4FTTb5fOal52Z4F0alMPAdOAyI0q0yqovoEab27kV8SqeMVahbq5pAyPLd9_IqKpYsxvAXm0PozsuV9dGoEmkKBOUHQCAmISONR_tqZm7Xq8E_JkusU9_v_tyDmbCEJcqvuj2NkkiVGyWfYMjLLh9NepM13o5E5dQG-0Sp-n5IGP-tFtOVvE01N9PZNMbmSLUuyD32W2Hna5-QdlJKN6dpLwsfKKyTEPGrPFT2fxFONk4mnMxLDqYi2DGo0ROnSL8eTzXCIgxY-c3sYOxu0dVhYF7UETxEm_pPK8JZ2KOATeQsrTe4_mOZjHuV2oq4lgb0cOXeA2VV8rN3tl7uErqhJolR1oPUzAjSFJNG_8X9wEhwptZz66E6VmtHt3Z8z6uJ7LEXNl-pDTTo2kSpnDdqPPSwrsXM5JOhJm2vZgr8pBEfaQvh1fEVPvJjiXGCjYdxsweG4Cx3rQA1Yi15_5TCZbLQ2hewj1xT8TDh0sZAsAkZMkqTgqVqr0R0tAOzsTItakxRCQ1e_XwL3BgIP3MJIZ_Sfd0PNEk4uv7rj0u7mI4Rf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تومیسلاواشترکالی
؛مردبازی‌های‌بزرگ؛ اشترکالی مهاجم 30 ساله‌تراکتور که شب گذشته در دقیقه 80 بعنوان‌یارتعویضی‌به‌زمین بازی اومده و در دقیقه 90 گل‌برتری‌تراکتور روبه‌پرسپولیس زد. سال گذشته نیز دردقایق پایانی‌بازی‌برای‌تراکتور به میدان اومد و در دقیقه 90 گل‌پیروزی‌بخش‌پرشورها رو بثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28486" target="_blank">📅 22:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28485">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oalY2yiZ_T28g1V5NkUbM4xX7tpo6ZMqMsoaZ1bNJNv1Z8RD6C1zI84W4E9fzaNoi-XLQvu8Zn4sKfO31NtPMvvcGwwv3Wyy8Z8k_LeAaOF6BVlI8bXOsLr-FCcbxKtxrvS_8Fd3xqz1-Mx9XZ6UYA86cHh5kavusMaOFV3ETIl41feOsTPBdzKqHpJdkAAbwKbuwasXZcTYWMOnXVTfNSGHWoslZW7_J6dOhJcfzjz0Ezz9bXwvBNhHLIPKsu3sqFTL6GSSqhtm5IdOLFgHPVkBjjTFBa_wo8T5tfZ0tCjVfWd5orO1ciJmtRn8QV8BYsZV2ONlQM4lEDw-BTEP4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ انزو فرناندز ستاره25ساله باشگاه چلسی در یکقدمی پیوستن به منچسترسیتی فاصله داره. آلونسو گفته دل انزو باموندن درچلسی نیست پس بفروشید و 140 میلیون‌یورو درآمدزایی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28485" target="_blank">📅 21:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28484">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4bE4ynxWLdahbq6VKG28aXeve_8HpJqNl02ZYybEEQPwxTqz1IzIkDb_xkq87JAXdIvfZXJ-VSrYIHb0tdbOikKW1vEgVXLJBi9-Issq6sm7MO1yXK8aSovCjpCBcqsqhZPSrVSA65ljNurLZeC--6KFe05oKt0fyr0PyZH1K5hqt9mWocQ_TAm-1qciFA80cJU04A9Cg75PTUYyWO9YquJA3ag1HX5Y2OU4fTZ1VTW219z4lvHR8tVw8c5GULnspeChvODuA_VNVxEJ3IV0-1GGRWxfGTYn9XSKH9yY8ptlVLzcrkLU4BgeQT6VyPia7Pc0_zXUHWn5qjb3WwghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌میلان باموافقت‌روبن‌آموریم؛
کریستوفر انکونکو ستاره‌فرانسوی‌خود رو با قراردادی قرضی تا پایان‌فصل به لایپزیگ‌آلمان داد. انکونکو از ستاره‌های فصل‌گذشته روسونری بود که روبن‌آموریم نخواست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28484" target="_blank">📅 21:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28483">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPzFg1Ty2bOGJvH5zotmPhyyOmg-QcbJjgimZxeM9lt6aoSevGHR-1Tj8yIUbXdosbfXGK2BwAsNcxRqcFaGrcnyfpnKsN7VpAUzm5C0fOrI8JH-1ixLvz8gPN6cGOAien94puOTyNluVYnB6UuC2KsMiDXTyJcoKqHNCJw4Rp33f1wajLsz3Xp4puBCVWia_C2O_BO8Nu4wS_LpVbsalcW_L0-DmUOtsozpDDZ7qBP3nI68tA0t89SvlqSmmAf_CTmOQeGy47Sm925_WBBlPQdQBOnbR61y3vCV0nkA7dFj0dMqGlOYmSCu5Avw8z6M_5mbXU_rQw3mrbXtCPhI3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛ با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28483" target="_blank">📅 21:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28482">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-bowVKWIPBnIl1qla4AiWN8fDtfoS8CYNg2aWA4WlUakHUwQMQOMI8ez20kQsdRPK07l-PmA0hypKUwgoJENeg5P7QCg8YAJAuqvHWekl1oxDhk2wC-uAsI6QYMzhYLgK6vHKiXK3luLTwhZLJVmjPPzjmxY-VOwMzfYveAilEq9-ljW0IPsQlbCKKtT0i8C-Dh_SnzzzejzDM_yy4zTGPzdAi-gxYFMKCJHhKwPLO1j0ETl_ZB79bFnFvh6IkgdviFkVjSq4RQACYFpcnGKacxkL_GZ8K9hU1RWrsiCxXbSHTA_NSJqGohLyXXCK3GEfsSwDIv4Wej8_3pen8DaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
در فاصله 8 روز تا شهراورد پایتخت؛
با اعلام باشگاه پرسپولیس اوستون اورونوف ستاره ازبکی‌سرخپوشان درحاشیه دیداردوستانه امروز این‌ تیم‌ دچار مصدومیت شد و تعویض‌شد. هنوز قسمت آسیب دیده و میزان‌دوری‌او ازمیادین‌مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28482" target="_blank">📅 20:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28481">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXESDcOudHuE9pooAbbHip66A5GIA_7Na3x-RVNXqp86cpT8cYrMxh10i48ds6whiFy7lzPK8F1lmE8lewrSx5VzCnEFVnePytkZMbGLP0twKCOLfVCvp5VnGXnb-o8JY9rUgyP3idSdes91V-DJBXVhFfPrk2lxR3ZNUCUd6e3B_Xjg_5Evot2ckMwhItlHxCJ78PktlcZjm930I-CzwscDYZNqaEgItRbezSavrwALipGOQM2PWlaFcrpnA78_gaO7_J3ctBNg7QovveVQOUu_-Mwiji7Vpz2ml-1z28cgf7-E2oPsPrKpE2vTWdKrwBHhG2585TsGgdzKNw5IlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28481" target="_blank">📅 20:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28479">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EROs0A8UwPJlnb2ya27NoMjzRsJOCuvl41g-8e_d6loX8ZCRGW1QWMXbo2ZKMUrQnUItL76Fio7_oFPE6j-8ShWjtb94cmRRWjXu_wRvgl8JbQ9I7ABff7hD_a5ALrtfsgvyGPRal18K_DKsEPaCVe7PwKKOgugA1RasbQ5LidZ4OSxTYwMcKE7JZfH4u8fj8l4b_5oRCJ21R-CwF_5xq7xyV6ZUm3WxawmwAfJ33C9JAffvsgtzENJk2x7Aji0qhvB1gNcy9ADLhdSKRBU26Ah3_w5ocfm-WulAEE7XNlisnsjuUkVwfxYq6P0d--SDt6L1hc731zHlnU5y9W4CCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIh0GzWuNMcNOsvYuQ8_DKdDH9vEPnSzXJz4n09_EKNkOiPcmIbkJqNcZshemPNsHXtMTO0glepl59ao35KLdHRBN27-VAMDm4Xrhrc2wjH4OEEg0CE3rXkwQKdWXszkd1uLz0ABOmMdxdvmtPl4RS0aICxIIT9E3AHfZOMvg9mBiDyu1Ah41K5ty9sXzqtUAJ5wsuijBN_xSvYye_Ej62s8BMnn3JPeo4dvwDet1I5x_BHtv234hRSziP-ocHDFdYUKdPxuKpBl2JaTj7pYwNgjhU1L1raqEwyXEUy9ly0Nk-muoSQ9KWUWwFQjsBvoq9qBNfy6tWCh606Rq7SjMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇦
خبرنگار معروف و محبوب شاختار دونتسک در کنار خانواده اش؛ جالبه شوهرش بازیکن تیم شاختاره اما اندازه خانومش محبوب نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28479" target="_blank">📅 19:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28478">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMoeBotTtzolcxW4c--lMONVjGkL1h_At9yJQEYn5rma6UAHu6TAlGuOqSInQQmGcxjA3pjoz5kdZM20gQQUwh4UfIdPly42AimEnkW64hFE83XTCCN0pufecVm2eC57H6AMrpILNHKcT04pIoHerB2IXTS-ccGIl5U9WmYujozl2ztYpSsYrm8Y2kD5cIrgcZh3bLfV9cIMhv1MTIlAImi8pSfcl3iqEbQAtuc-n-uyN7ajDLFQeP73LqhppfQhX7wQ2YdK0MRoGQ-TX75qChxocsSZeWhODdfbbYKxLEqxf35NBsJyhERkSZ2Wt5KrXHEGZ5k3UwQYwbkWldt3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم؛ هفت روز تا پایان نقل و انتقالات باقی مانده و هنوزسرنوشت بازیکنانی مثل بارکولا، آلوارز، انزو، مینته، امبایه، گاکپو و پست مهاجم نوک برای بارسلونا و وینگر برای لیورپول مشخص نشده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28478" target="_blank">📅 19:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28477">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxetivueDNaQbFRbSJR113pOhzmEq2nwB7qU5ME9LpTM33JZ9879mRKCfd3I-TIo9s5q2Bzb6jQtP_ELaMpJCztUTWr0iL4RH6tisZ65NB5Sb_3wxOgIW_iNUQMDQ4ZhaVBoSxiRuNQg7eb9eRC5I2wauXo9nw9LlcyGbUzCoRYVjhXSLknb06hKdk1wPypfiOhJqj89pgf3_Ny6slRhnMLT8PJ2ksy6hWGCiu56rhw58tLXa8yxofOMAfs3TOF9e03gBFIQUl0hSv9scVSYCvgrXce9gW4qdv4k8gu8FHfMZtLNAx-I0tD_Dlc4i992gOT56fzE5L-De9INVYDz_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28477" target="_blank">📅 19:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28476">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ5Rd0uQAV4rN5caG86jqR_dbj2vb9YR_3cY1BBQZN8BrPxrPJ9b8SCTXCUotBYg0a8osyN-dJ7KlEWXPP4uEuSw2SUuIqZAEx05RSom2VlE20X6uy5YNdgaa3e8DhxqzTOdPiGHDnz_tT-Xf7A645jRRAXTP_Gcnr9GYhmTmTRSQgp6oMUvoznqGp69ZjOFk1EsF31ZZqXhenDHIg5o4O5PBuo58PuR1KnMnsHf2NcAIMUGBgA-HdGohokjMnDnQpLyKIkoirgbguv_6_2UDBb9BoIbme3eVDRodbI6KVrXSPOdIm162PMc2pM-v_2oJoSUuKpU_jAjOXjIraiLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حرکت دور از انتظار عارف حاجی عیدی هافبک سپاهان خطاب به هواداران باشگاه استقلال در پایان بازی امشب؛ حاجی‌عیدی در دوران حضور نکونام در استقلال تلاش کرد به این تیم بیاد که نخواستنش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28476" target="_blank">📅 18:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28475">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
قیمت‌موادخوراکی‌درتنها 5 سال‌اخیر رو مقایسه میکنی آدم‌کرک‌وپرش‌میریزه. کسی ندونه فکر میکنه 50 سال‌گذشته و این‌قیمتا تغییرکرده. قیمت خودرو هم که بماند همین امروز روهرماشینی 50 رفت بالا.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28475" target="_blank">📅 18:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28474">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufG7qSsjSjWadvTnsuVEzxHJzOJud-bT-CnQyCMfO918ELp1s2kz5WomCopgDqJdvo8IY6Akr0uSNbTJt7XCG24YVhk1gORCgZ0hnx6HMm6d2kYQWsE0hNZtMTPyErxVq604WML3jDO_kZWLMou8j7gZUKo6y6khRYv9ywivHjGGxPkBXFLgkgovdHnEjffB799Ije-KEVlUhsfU8ntfqAMqJVPrM7hNWuWIGfFQeMPwC5HybLrs4tLXZcLEddmHUfoKUhBRY8rham2fxbOl_3aTBWIR7n-4Zg8SqIHk0IJ6N1KdmriJjF0ef1qheoi0ShlyYA9rBFMbaUccJgF7ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2017 در چنین روزی؛
بارسا باپرداخت 145M€ به بورسیا دورتموند عثمان دمبله ستاره جوان‌فرانسوی این‌باشگاه رو به خدمت گرفت.
عملکرد دمبله دربارسا
: 185 بازی، 40 گلزده، 6 پاس گل، 141 بازی رو به دلیل مصدومیت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28474" target="_blank">📅 17:37 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28473">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1ixucLymQupRypJNtEfYOB88So0reBmLo-yJU0VpoYLlFFwj9NspoxHSA5xy8VRUkLweVx3xmVFnH5MrQu9HIAx9DaI_u6O9Hbrt1ZhqBDIlK_hu9EmYBsenXsTv_mLWtzXflemwTKw39QW1_NuOFmNG5ns_AL3R1rqiy3NoiRdAQm8MHGTkhv2p9fOWC7ZECrQAGDuDPAwwDJv0qpxoXUnyf4kZogif-e7gMenheyhMCr01WyArTkHtG7uObq0e8_UDnuzzZ4sh7R4yvXIqKVwyuy8NXXxfDoA-XIntg7ZOhNJNHDqmE-0fYmcGZnh8tH1739yk2TYPPcWJ-0YUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تاتنهام‌امروز100 میلیون یورو به باشگاه‌منچسترسیتی‌پرداخت‌کرد و از ساوینیو ستاره 26 ساله برزیلی جدید خود رونمایی کرد؛ سیتیزن ها دراین پنجره 12 بازیکن خود رو فروختند که بیش از 400 میلیون‌یورو سودخالص کردند. الان هم میخواد حدود 140 میلیون به…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28473" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28472">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjYgvcfMir7JngeXPcCA78hn2IWxttZq8WNSd9qcRkm44pYKc4XbJqlGmebTbGMe5ZFmxKHVW7MF5rpOveV14g7AWA3gTUpJK9ByhWba1hMIs6XA0oJGeyVjCz2PKTPKfDbUIoKX1F5x6T-ZJYiLFGShxQms7adoceDTPMvmtak15G73nP8Oe2iADQ5mqrNlEDJ9MmJrZ7mF_S_IdB-8M8KQUO_LylXDuwHGXqWxrNPLERaJaVxGxUi90E1q10FJUp91b_-aDV3eKkVHRWyQJlLG5pGZMcKM5rRpt1yzKnGw3tKmeXhyWN9DetO0pxYcSN64MO5IXoPdQammaa5U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
ترکیب‌احتمالی تیم‌اینترمیامی درفصل جاری درصورت پیوستن‌پل‌پوگبا و آنخل دیماریا به‌این تیم؛ دیویدبکهام‌مذاکرات‌خودرا بااین دوستاره‌فرانسوی و آرژانتینی‌آغازکرده تا درصورت توافق‌نهایی باهاشون قراردادی دو ساله تا سال 2028 امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28472" target="_blank">📅 17:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28470">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh0P1V7wDBY5n-FMk59eC6ZU3B3OVf6wiAElJjxVUrQYBgjNhbWxHqvyQ4OEhFaB_yswXfh0o0huHvMCf-b--A8j-Us4jzCvB-TUNJzfv7ci3ymPYaTm8sOCjuA22tmtGfWhVXMjVhoYm9aRd7uEHkDrBJ1hKfMkWT3hcdaV26pGPmmsfwXfDYdzVAO6FTzUaCwBCFpRlABeTQ_3yw645tvZskfPU8KYG34TzdMMFy1UP0amEXL7uH9iEZwXDMJ-UD3PIp-5reFYMGPBlszgW-vhLTDuBVLgQrQ2OZXExPJH4D-t3JnczmksrKu8enb67OcyqCzoqlo64zpzOVtHlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری دردناک محمد فرهنگ یکی از عکاسان زحمت‌کش فوتبال‌ایران: دلار شده 204 هزار تومان! الان من‌چطوری اعتراض‌کنم که بهم انگ وطن فروش نزنن و از کار هم بیکارم نکنن. خداوکیلی دیگه خسته شدیم از بس دویدیم و تهش هم هیچی نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28470" target="_blank">📅 16:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28468">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=TL-DIE7DwU37Xih3dUzpB2mqM6lnouLDVFKoq8eeEozrycVTALNbbulqf1kwGH2ej4R6IwmEidTUZRO6rg2A39iZaHvXVsex5HLHLyorZRhqxt2yFo_f0VVoAefzqRBJlN4qQxCYi4gbApljuqhkmAP-ipgSc-U4lcij3lzuzyN399JMbZKQTWXQwQ35vxHY0YDVPRH5dAR0PJd__gwXXUjYfT_K-wWUUwhH0MyZNmirtmTOrQMyD8YgJQuG0UksDyegJvrYLyggnd5aLtfzvt4DulU0-8CQRM9n9dehFr9HX9RAESUIgq2tAHq_ZPqmLIjoxLLnvrw0jFOc3pQGGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f00e5c331a.mp4?token=TL-DIE7DwU37Xih3dUzpB2mqM6lnouLDVFKoq8eeEozrycVTALNbbulqf1kwGH2ej4R6IwmEidTUZRO6rg2A39iZaHvXVsex5HLHLyorZRhqxt2yFo_f0VVoAefzqRBJlN4qQxCYi4gbApljuqhkmAP-ipgSc-U4lcij3lzuzyN399JMbZKQTWXQwQ35vxHY0YDVPRH5dAR0PJd__gwXXUjYfT_K-wWUUwhH0MyZNmirtmTOrQMyD8YgJQuG0UksDyegJvrYLyggnd5aLtfzvt4DulU0-8CQRM9n9dehFr9HX9RAESUIgq2tAHq_ZPqmLIjoxLLnvrw0jFOc3pQGGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28468" target="_blank">📅 16:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28467">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKbwCnXrxN28vidtM39iPI3A6aUoVwWm0TuUkRXkxXZk8KOt7w2LfFPpITZ27BKZ0BY9h50_IsWEQofwFAww109IybLQw6x47T3QrKVvCYXeuHq_c5Xv1jptSRhDcvCDt9whP68BTmkf7cEft6NVPtnOym_CfrLVGefu5FQwBXdLSRFvuJstlKEklIvVV34vZuHy8mOqlhXa8L0P0CtHyxQAk3AcCQaWLmoP8QzE0VsM-hb5lpJwqkxlHitSLICFdy0au2lTdbj586jxzqFDqbuBLokLkt_-yTbSLc62ym7c_fpd4aDeygwwl1wvxruGrWm1F79j2rTFmK7lw2i5kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قانون 90 به 10 در دربی بالاخره اجرا خواهد شد؟! بااعلام‌رسمی‌سخنگوی‌سازمان لیگ، طبق قانون باتوجه به میزبانی‌استقلال در دربی 107ام 90 درصد ظرفیت ورزشگاه در اختیار هواداران این باشگاهه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28467" target="_blank">📅 16:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28466">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njDBrIlcaMXdhiag_iERLiRkykm__lTgEIc_vY8EVZyXSBpSYsDBy2oJwbne-y9NqE77K4QSl_DSGHxdmW-Eq1mm2tJesliMrrDQSYH_iZeO5zorhQ4Rm0C8qNL3Dq-MgKJvfSi60CFt_9ya3BZEXuvfDNBhD6rV8v0QwkQwRnMNT7O7ldcssQiBIWJ6I9S7vR6O6nZ90Xv7AKk0oyesZRT_T5wwuDLh6U9P3cppSIMrSTKZEI1s0SneCRwEboLw-Z4s1pKCuvvbBi4c92QaQfyCr2dhT5Rkr5TeryMAL0IDZO2jF2JlYhQvAOeR7-bOByZKBDsUv419fB1Zm8HyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عارف‌غلامی مدافع‌میانی‌استقلال با قراردادی یه ساله به ارزش 8 میلیارد تومان به چادرملو پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28466" target="_blank">📅 14:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28465">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7KpSX8cDhXkSv910LBXxISHHVUbzK8pCUA4G2feKclRQifedwVHNzZZHLRlFVALPQvIOiF7g7AnFW6of6c9ApbWXFkUHV01L_fWWI9A29_R6LYxOjSKRtRff1L78fFMNRMHUC69CQpXWhdpUkkHuq0ZINqVH4z8zId5WfhvKmFj1l6uXqX9nVf3VJ3CCxyE3O9r5Cef9z9OtwYVVCUzNaptPQre2ExyLnszvoMe85DTp7LGlBEwcd7A86rZr0QY-VnL1jZ5Rikdl96GZ1WIMvTf4WXz_ajrz8cHs3Vz3BXxNAI2QLmj_nFNON5nNclQLiaK0-rA76_DhwxE4eKr-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
خبرنگارباشگاه‌الوصل:ازپیوستن‌مهدی طارمی به الوصل خوشحالم. او میتونه به خط حمله تیممون در این فصل کمک کنه. بزودی با او مصاحبه میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28465" target="_blank">📅 14:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28464">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmwqpMzc32aYVcxGYynLpFEwjDeGO7IpQHt_9xU2O9ybJmb90Tg4waGKqaFI1Umb5NNMJj4sUzkgtycYAIqgiDZPZ8w5zYbtw3W-EcZa1dYmYYVSImpGk4jAX-wqYoPy31WB5HQGIa4iD3o9apHzHuYJjWmnYPNqlrtExqUD3sKUaYCG6XuboXLM-HgUHWwaytvW_SmbrNZuEgUv1R4CmoU9tF3cnUPELVGnWIEe867QX-rAZ2JhFyCg4jqLGRsNSXbW2Y4jOe-tEjvBz3-wAKc6fXgRftbatKpeu_6G6saKLjjZ5RmUm5E-s3oOL1_OVWgZAkghEHP_lC28lhT8jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هایلایتی‌ازعملکردفوق‌العاده دومینیک لیواکویچ دروازه‌بان تیم ملی کرواسی و جدید تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28464" target="_blank">📅 13:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28463">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uudu4SkOte0DKMaBlXzVbkaz4QJ_Gj4ezw3BKq2ZpfdIJBTFaVGT-7SLFf11R-uiYP6EON8rVPmQkATgcvIu4EVoMWMUwaSbTPLx_Kdvegsq4fiUUicTVLHjbdWiJHm-qLa_t_FWDm4zesWMhyApIFmehRP3UlCHP3d5g5-kisouU0M9XQ8w6-Z6hgZgs0drDI-YhPWcJfOAnU0HREu1lEYf7ExSS-FAv7zfM5lW1M3sh9qtphTRSQhfakI_wDZYWqKojfAYl3AhFcj3G5rSJJMOUnZEzeEwe6qcUZpbWe0ACZNIRXClkfmcAaHK5WiWpjJB8MIrtIaH9hvCfkG5zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توورژن‌آمریکایی‌فصل‌جدید عشق ابدی یک دختر ایرانی رو دعوت کردن که همه پسرها عاشقش شدن؛ اینم رفت همشون رو به ترتیب بغل و بوس کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28463" target="_blank">📅 13:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28462">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=fmPYBmwVbGduoKaJvXhbqWZzl555gOUZRroWPGxp6u6b5PMWKI7Q2Z6bRRJMsd235dq3Hn6UkBycHdFvlElmHjiAlaeV7RybyUmKSSqb-6yvLsyJC7T810vAS-fbx_XyrgHJuScSj8v1myfhNyj1u2a-X9eUua5G1bFgWsYgLnSZkOl359hopD1Sd3jQJsknfmhWgqU0LLZyhzmB8hbm15xlCdN-qiN7EuVixTHuNsxwK96Ly6-KOZfIGHcHfg--F364mhu1Pxf4uuOty9mQ2AnvEOPVTyJrTojD-j6BJRaohVFP_Xt_0QEmoJkAMJUQYbtZcYl43e7cD1QCjOYzsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cf16d76a5.mp4?token=fmPYBmwVbGduoKaJvXhbqWZzl555gOUZRroWPGxp6u6b5PMWKI7Q2Z6bRRJMsd235dq3Hn6UkBycHdFvlElmHjiAlaeV7RybyUmKSSqb-6yvLsyJC7T810vAS-fbx_XyrgHJuScSj8v1myfhNyj1u2a-X9eUua5G1bFgWsYgLnSZkOl359hopD1Sd3jQJsknfmhWgqU0LLZyhzmB8hbm15xlCdN-qiN7EuVixTHuNsxwK96Ly6-KOZfIGHcHfg--F364mhu1Pxf4uuOty9mQ2AnvEOPVTyJrTojD-j6BJRaohVFP_Xt_0QEmoJkAMJUQYbtZcYl43e7cD1QCjOYzsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28462" target="_blank">📅 13:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28461">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZjad5D6lEMWFab6vsxZcvgcw2Z72fCwbWlWWgj8UUvN7CFsAgQO0rxbcyTKKV-yyyocjZUJEyiy852VI3QRJT8d1TkNpk-Pbgn01Q-WbZD_m47W9Wiy4eugLurvBcY25oh9G8ZdoclCaiR0QQIvil9ooUulJttL3q9cBU-Y8k-KOoCU5imERN-vsJrMuchQSsESnQUEzTJD1iwQmaz6bBstJlq8lsvSmWlHETyQXKAMi8T_7RtBEYV-s7e1PDbV-c7H4k4iVrHh7AVnQKTENunwuD6GbN804ZT4C-TZj_7hdcvdzajIBRRbnEtPpili4-skHA3YsAIqhIjRWh9EGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💵
🔵
درامد باشگاه منچسترسیتی در این پنجره با فروش ستاره‌های این تیم: بیش از ۴۰۰ میلیون یورو!
‼️
ساوینیو ۹۵میلیون‌یورو؛تیجانی ریندرز ۶۱ میلیون یورو؛ رودری ۶۰میلیون‌یورو؛ عمر مرموش: ۵۸ میلیون یورو؛نیکوگونزالس۵۵ میلیون‌یورو؛ جیمز ترفورد ۴۶.۷ میلیون یورو؛ آکانجی…</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28461" target="_blank">📅 13:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28459">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vw2fupefMi3hf1PsQT9nX5Qgu8iAs8uMJB0ZaeHeKTq8R1MlOJcsaI9rVtYEitGtcgZFUwNs5co_8Lv24eKb_j6XDpw_Km3C1jSqSedFFr1sCY8iQP91yiq3sQ-FTIdctpkkRw6KoJ9G7s6hyyNiKsbpZ0nhREcEFutk39Fw-VSykNcadDBOZ0CGKK83Rxts3kVCaNLIPv3qXQZ04DQdFWd7olge4aR-x7v2v__pTaof8IylGvTS5LdST7hSdUgeTJBs1CLyIeURvfK-PHWStAi2Z4J1GP2L0XqOAutmeHNXhr9SXc2sisFPU0s-Ky6ymxkebqQixOY2q9WE3nSw-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhDixb39V6f9fJdOKovU2mrwuVopWJzfWcHEw8ojPZK2SHEdHyehvJWKuCNAvKaqkuhPGiHkT-lAUVkj5gE0A4JRGvomJiJ4JL9hMO4L4nFIyYvwgP6SCKNiWXTvq6DhazNhRx30m5xnKVeQM-B-GkIkaEJwjMMxOekbv-lyHuq9CbWQoRbeH20s5r4niF1wFhISGncMcmptLhCrknQTFE5R2i3lv890nQtJ8nyDEMMzxCjeP8P2tV_nPXoLjWsyAHMG-X2suDCQyfj7zDbabU5CjitVl13OZ7TkBmhYyvxqgt1ZZ4tCuBpWqscP-_7f7waLFjlSTK6Gyk6aO4tjaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
از مربیان آکادمی لاماسیا؛
که حسابی به بازیکنان این آکادمی رسیدگی میکنند تا ستاره هایی بزرگ به تیم بزرگسالان تحویل بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28459" target="_blank">📅 12:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28458">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=Qj438S8tJJ47AQ2MjbrOpyMirPxzTvTPK6f_nsIfA2l0hFl2HuM71njlvNmIOGzRaYBDkrZu7qsZ7xXhbuDVx2wcQ6T_fSQRoaXYq77gqgpnwG4QCTlctyrapllzon8ineFDD5oObpT0Is4BaRLIpa-9z5JMg44X4rxy2-6F76qmgK9-Fcevp8jzVybwXop-V7K-egK1-3Nj2LL9rQ1ysvuCCELPcmb5hRUfsKanHEbYoVZWGN8CP01AZma9x6aenuh34nOXTn4P-xEdBAtdqimqAtxS5Mj4fjZgcxYYC7y9jc2VmmkHhCKlpei7whL6qXDsPRwhMXsHk53pL_CAjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b364f5abb.mp4?token=Qj438S8tJJ47AQ2MjbrOpyMirPxzTvTPK6f_nsIfA2l0hFl2HuM71njlvNmIOGzRaYBDkrZu7qsZ7xXhbuDVx2wcQ6T_fSQRoaXYq77gqgpnwG4QCTlctyrapllzon8ineFDD5oObpT0Is4BaRLIpa-9z5JMg44X4rxy2-6F76qmgK9-Fcevp8jzVybwXop-V7K-egK1-3Nj2LL9rQ1ysvuCCELPcmb5hRUfsKanHEbYoVZWGN8CP01AZma9x6aenuh34nOXTn4P-xEdBAtdqimqAtxS5Mj4fjZgcxYYC7y9jc2VmmkHhCKlpei7whL6qXDsPRwhMXsHk53pL_CAjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال:
باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28458" target="_blank">📅 12:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28457">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYoJsQgLvLnisGiD_BgFs3SJr5KGtcsNXUq7MkVAtLTDDsOFbA-S5xZC-t4I2V7YnutHL7aSMUVCzcvGRx7H7avq3tc1EIyUL-nH8bueaZWvcdVo1b5f-HAby0e9r8O7DIg8x59xgjbQ896b0sgmAaEiaZjW65l6VcWeZs1HlSWsS_U1FV4ANRv3QMvwvG3jBDUH_0ItapXzCeuh_bddNIKruCuSh5StteDqO7m66i7yTNWSB9VUnXw_DqBGDiuOyysHXkp3rMR-LvmYe-qMYnc6k7VwjDwnLSqTYreQzOE5nlxiGrAzATxjTauFo9FHAGiePSEpXjeb_CtaJEs_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
با اعلام خوزه فلیکس دیاز خبرنگار نزدیک به پرز؛
اوسکار ناسی مدافع میانی 21 ساله گرانادا با عقد قراردادی پنج ساله به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28457" target="_blank">📅 12:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28456">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmk9f3JZ-GU6MtfEqPpSn4pHFW24PkwRoDuMsuV2KLYqO5M4k_bkZUxs9BuD9IjhD5I5sqwbNIyZ3BiQ9CYEdFHHd5OYO8dN_RTBMfx0auE1es1ZT3VxKwFifthhTGUIhM3Xd30GQ5a8vmycj2cm0fYKEsYfKr8Bm80qsifhCZzH6cNJiUUJd2TkcD-ru3DLmUaxhR_Br7FIX_bVJPaWkKqzYXMK-Zxp1Xp4qiszcJdufUfr7ZSyCoxVPrBOB8B78p1EnUmREM8Uy7k8ctj4nkr8S0D6zdVf1ycXTv2TTsm9M5JfCc6MRE9i2MK_GDyOtSTdufL5g6CVjYYuWXq4uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعدادی‌از حرکات‌خفن‌و‌فوق‌العاده برای در آوردن سیکس پک‌های شکم درکناریک‌رژیم درست؛ تو‌ کانال دوم تمرینات‌بیشتری گذاشتیم اونجا هم جوین شید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28456" target="_blank">📅 11:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28455">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCFbMPkGtSuZkbTC97Neo9duSX2y_F_zEuwQQyt50j0d5bT0hweSfemSMWeXAj9aB3jHzhS_FvxRN9N8209cV9oaLH0rSQUA3uXC0ZpqU2T0hAprkg1UYGkCQ4R9xVCcsXNXjgrjzamlFk3UrEIEXpQSX7yEQdQ1GR8K7Gsy7TGNy3J19rmZqzK6wAmPQn89XSvRMgTMU8seVBXiPKvwXJXdzLwWDfKYuE0FBQ9LzxVakLJfo5iblLt4uRkhjQ0AeRnCQWy42D5vEb_kkikKUMdurOlO-dkXZK_k6i86v1UO0AShyUTfhTccSodufOeVcq3KwkIh7_hbcDp7dV3fog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمیدرضاگرشاسبی‌مدیرعامل تیم فولاد: باشگاه استقلال یوسف مزرعه رو میخواست و مذاکراتی هم بین دو باشگاه انجام‌شد اما کوتاهی باشگاه تهرانی در پرداخت رضایت‌نامه و تاکید آقای حمید مطهری برای ماندن مزرعه باعث شد که این انتقال انجام نشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28455" target="_blank">📅 11:38 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28454">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYSJdOZnDI4G_MDWz_fc4HgtycnsYCRr_-cqQnWx853owMGO-KL2MGXmrRZt8Fjs4csHMTZ5V0aFExNpyUTKPOU7czUwDyjVbI_f_Zv-rzRC_ic6orOpOcl4VqyTqQufOAmPs72ervGpFd1m1K95msvX9S6FECqu-gQIJxGOy96J_Ak8OXe2_xYBKY49F2ImeUknW68AQkF4R1SzcIx2WVtXCZt3HXkB2mVVkp8fHnIsedzOQfJf6nbWTJBQx1QmOZr2AjbDJR7cG-zhEkFAw2stbHa-PdR9ealZXpmHzghIegYXtghSWCjdNpMaReWVEIgbGyEoPfo3cuu4CourAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛انتقال‌ ماهان‌بهشتی ستاره 17 ساله ملوان به استقلال اوایل‌هفته‌آینده بعداز پرداخت رقم رضایت‌نامه‌توسط‌مدیریت استقلال نهایی خواهد شد. بعد از بهشتی آبی‌ها در تلاش هستند که انتقال فرهان جعفری رو نیز نهایی کنند. جعفری مدنظر پرسپولیس نیزبود که بدلیل باقی…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28454" target="_blank">📅 11:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28453">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9i861MMQTXCGXmqv7GhAkDWcQGsLTwr1gxFwwQJeevJccrJYwMr_O6l_nPFVkIyEDD4jqx2XYbR9KXBxzgCRBcoOu-Dj005r6At3Ue2TEjee_dlHn4bHm9jk30Ed46ZqgwPdCkxCwT_j4hwfu6LsKrv3p9CMh_CUpQayXu1Y3SzK7VYKZH-NtZV2vgbGnvcDhaMOJKFcepX24z39NelIjG97J0tcxvKPXOp85zsOqs5xAB9s8HmGTn1KLL-i-luYEvwXfLxPLYcSapdpugWYkicm1_DvN1tt_FDySY5gYYjAF2Q3LNB-805Wj2BMgBUv4yT0kxyJraDa54ca5OD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛‌سران‌منچسترسیتی‌بیخیال انزو فرناندز ستاره آرژانتینی چلسی نشده‌اند و مقصد دارند به هر شکلی که شده او رو به خدمت بگیرند. انزو در بازی اخیر چلسی از سوی هواداران بشدت هو شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28453" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28452">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJrrqk8cgJtrpumJB-TCIVAqWVYS7bd-omN8xv_VTrzRgsP0GBwQRp747uNRREGxxW0qLd55Uyl6iKzIj22U-98RgrCEaOO4osFpJFlBad3veTkmBzHGvzROFM82JTU5PtGPyCInTAqeC4dg-kY0JMzoYUiDk8eaOcRrYS0V87jTduA1ox1jDfuJqfwXFVz4F4Arh8pNC-4oYNGtUbCuMfmORs-t0dwe21ev7cr6uWc4MPeLaB3NmKNwnQqW_RRX5b2FNacJqH1H0ZM5miT3OyQRcWGPFmVa9Q1-KEM2mCW1BRN_WfNlcUVhTXitg3y4W8dHB2ErUHVtfLhXvafQNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی‌تارتار سرمربی‌پرسپولیس گفته ترکیب تیم‌من تشکیل‌شده از بازیکنان 22 23 ساله. براساس امار رسانه‌ها میانگین سنی تیم پرسپولیس در بازی امروز مقابل تراکتورِ نکونام 28.5 بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28452" target="_blank">📅 11:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28450">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJdWE9PT2qQdIp5FZlnVy47gOxCK-jXvI2O7SG1LJ7pS3g61xDJwSJH0_vkwL4G6D5VnRl3XX76wMr_9ikyj5J85Whf6ijavKSvCCsSLBJfCRQmGM6h1tN5vf1CKuVtzQP1K9kkZ8cfEfJygRGyL1CVhkIilPun3Z2_brIl32KF3gCom6gQSyLsOXlNQKJhZrsIjdQE01DmhO66ZTFTEipOPDaKT1G9NJ0SKZhcO1wjvSLfQVctMW5VlSi4FVtq637q_IanxnodVnBLb66gGFn2C7nQudFDxe3WS2M56-3X--eNq9lB2s5Yaw08VoICPpO9abWW-ONDi9rYcenlgtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نهایی‌دیدار روزگذشته تراکتور و پرسپولیس از نگاه‌نشریه‌متریکا؛ محمد نادری مدافع چپ تراکتور بهترین بازیکن این دیدار حساس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28450" target="_blank">📅 10:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28449">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=lei7Tg08P-xyo9eEnD5MSIEHavkEqzRv8aTs74lz8r_wtXTKSQDHheuDAa_mIjbV197tVvv80UA97KsQwRLhqeUUxQzZRT38upOcEfj8bC2ZQ9mJlrPYigJYkV-wEkPJYss28Pznnd9aTErNks1NylhbXLcLi5JZ78MR3d4nrUxIBkLRYkcSGTgUkcZr266pb8vxTaLr-tEH_mr0pbrS6DDBoSsHRWmqWR81WUQ1Mn8rhjFoolo4wkLLXyikfICwj8Gr955R5I7WJ8yDwuZIlpMkfXxu7kkja9PLh2C03T-E_vcMcMllKnLsal8917LBb6K81Idp_hS8PKTahc9mug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039b0e1735.mp4?token=lei7Tg08P-xyo9eEnD5MSIEHavkEqzRv8aTs74lz8r_wtXTKSQDHheuDAa_mIjbV197tVvv80UA97KsQwRLhqeUUxQzZRT38upOcEfj8bC2ZQ9mJlrPYigJYkV-wEkPJYss28Pznnd9aTErNks1NylhbXLcLi5JZ78MR3d4nrUxIBkLRYkcSGTgUkcZr266pb8vxTaLr-tEH_mr0pbrS6DDBoSsHRWmqWR81WUQ1Mn8rhjFoolo4wkLLXyikfICwj8Gr955R5I7WJ8yDwuZIlpMkfXxu7kkja9PLh2C03T-E_vcMcMllKnLsal8917LBb6K81Idp_hS8PKTahc9mug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
مجری‌شبکه پرشیانااسپورت:
جدا از شوخی سبک‌فوتبال استقلالِ سهراب‌بختیاری زاده یه شباهت هایی به‌سبک‌بازی منچسترسیتیِ پپ گواردیولا داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28449" target="_blank">📅 10:29 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28448">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3h4KiTdCv3B9VCxNlHnkZODX-iosCHX-wepMLKnuAgm0IskWfy73xYUHd4gIQ3zP2R1bvAluawYa5tDNjIibtApmwdN6WOr8K7YoKjtdk94D4eHflnorP7dAjJDzvDoDXxJoIMOf26GjtYne2ZSHTC18U3tYT8r_Zs2Ai7uHIQGvxb4lbEnkSUlOh0oZ1tMvCk4pE1DJM8OML3uOqhiebpeL2pU9egXNZoZy_YKsWEfNXWIL_e1WzXRlJi-4z3lZlz3VVTpSI8qWsmY-3FrTIynIgsadmE_LxoHq4TTQNYjcR43omZe6eqpPhcEdszF4tsm3ITkBd7EzBgApLfVvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
#تکمیلی؛طبق‌شنیده‌های‌رسانه پرشیانا؛ باشگاه سپاهان به‌نماینده محمد حسین صادقی وینگر جوان تیم پرسپولیس اعلام‌کرده درصورتی که بتواند رضایت‌نامه‌اش رو از باشگاه پرسمولیس دریافت کند حاضرند که قراردادی‌چهارساله با صادقی امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28448" target="_blank">📅 10:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28446">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T-tXNV5Xu8oukvD4KAiNTuVmHBNPTMueE6vV15EQy2PZ5jPO5Cp71hdr2GqmRrD828fRpHvylZiHVg7_vV4sV1YqbZLXWIYj7V6xXniHtDGC3_3nGmBNwuLvD-cZ9A1pqNhI4AEsZIfW_RZfIlHB8Zer3XUZ2bwtyhXI9wkORCuaQdkE2S02UG_q8YTiVyAf6QE7k3n5CNyBY9BEmm7dM5y8T683X9k7CeNoXFCFSUhU7-RLxy1SGSF4JrdyYgJ-KU2bdGm7OTTk4uGr16RsnHxqoSO7MmIIBP7k9jdxpl4caQZVPKC4EzTG9iOelKSNRF2RqeBzLXSv_Th1Bhln2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iU536i3rO5oz1uMz4VngBXYmq0shaF3RFONyd5zkshDg872a6Rs8yEAC_2zVLvAN0oIMKtt1zm4hSoHt9YhFus1jdO-8Xpv0y26empS85ypidOi_MRl15Sncv3rlFNifhmXt70Xl3XYR0lwnCi1NI2L54wx9TWm-6moYLdaVjMsF_75zUPecnxFbF2tm-6zU0BDvQBeaJwa9KOc_wmEd2JFqgXzm57nrKson-pPRkDQzETOaK2yOYeVby0NFY8LFFw7Qk7dqDs9fi8oXb7inNNIQyyNQyFwWke8hiB3oxOE6qfw1mtdYus6LHYvpPi40U8VUP4MWzIOz5P0m6wzU-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
برنامه‌وزمان‌دقیق برگزاری دیدارهای تراکتور و استقلال در لیگ‌ نخبگان‌ آسیا؛ این پست رو یه جایی سیو کنید و برای دوستانتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28446" target="_blank">📅 09:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28445">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrKwNTVGCbUsLLcy0EzacG4vOCLCd6Y5C7iA5XSOoit97DNRw-cqIh00dpSByij1WLWGplm_T8ijp9E6nxtnSxxsZrrZeU7fQvgspcqtXUH85updr7bf5vewAwmo-2E0vm-IImuPk8yu1TlokfvXSXkuPmXreOT2M6QEYCEK35ubb5_YcMpzMmbSvFDx9PH95tNn8ofTEVOoiaZdY25EKdkmaUjWAc8ZVkoXOxA3tgBB3Tsn2FOOw3oNyJI7Ebt1O_pt-2xl8AhsztUrAzGvqg9cc3SmdTfb8j54qFwOA2zSrEURjldtmhw5D0qS4EW0F4y1RZw_jlOA0VNwc68sbRbj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f23b0b1a8.mp4?token=SPwNHooRC_5Q_DuaLyg3tGS-GhkANPS2tl99UPVNvcR0EgMn7w7apq7mC56NgqtvyVo--2ZJF23VESmocB_C8R8pe6wRJISYyzCIYwPgHM8HRhLd10Hmn6pRmQSiGXDl7ePi7Xh1EJ6KReyTyXjxJkU_Mt0ni5Ko0dOokmSK1O8IFS2SLd53m0yfdTMsaWmfa_AdXr79prOKxZIL-4o3XLpi44h1YJr6ogBfMVp3MufY-E-KBjYZ2MYDYPedqMAqVBOgpDNZrQjy2vksDw6tq4YO7zYTf7OkJQ7sSvzHj8uugf203L6lH0XD7FrZj6Tj7X9uoJyvky0_0Mm77aFrKwNTVGCbUsLLcy0EzacG4vOCLCd6Y5C7iA5XSOoit97DNRw-cqIh00dpSByij1WLWGplm_T8ijp9E6nxtnSxxsZrrZeU7fQvgspcqtXUH85updr7bf5vewAwmo-2E0vm-IImuPk8yu1TlokfvXSXkuPmXreOT2M6QEYCEK35ubb5_YcMpzMmbSvFDx9PH95tNn8ofTEVOoiaZdY25EKdkmaUjWAc8ZVkoXOxA3tgBB3Tsn2FOOw3oNyJI7Ebt1O_pt-2xl8AhsztUrAzGvqg9cc3SmdTfb8j54qFwOA2zSrEURjldtmhw5D0qS4EW0F4y1RZw_jlOA0VNwc68sbRbj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
موقعیت صدرصدی که دیروز شهرآبادی در دقیقه 90+6 برابر تیم‌تراکتور خراب کرد اوستون اورونوف فصل‌گذشته دقیقا اون موقعیت رو تبدبل به گل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28445" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28444">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq9lMlJ2Bhu27dsG5phZVZ1Z0jjTuVd_7VUFSV_Zm-NvVLNp7hDnTee4bh8pdGtt50UXMmYeNd_rXrlbh99uZeIzCBWbzE9n95e3CrjbnUUylFPYQ_7qEv1dOQjlsWh2Bfmvt4Bo9jUNaRC6ZMccVdwQdo154O415FiP5EwazD_vLvZJU0eERIkLpN2d29D-4sICaRluph1Th-zz412J9FjICqKJgHbAHv4yOaNCFgSw00e-E9DsVDSHJAzrERK7bFQrmOb94tf60ENSn5pEcxnUy5yAuwM3pFJlaCBfKw3akZ5RPeC0EHKUFS4XncveswyEdcqMXJch-BxraX3iTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی:
کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28444" target="_blank">📅 09:18 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28443">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RipannZaAjtIbmjWbR1I6GTaU603g2j6DJfh22CVMK4ALcwFlbivD6vY3LY6fiGr0UzvLzHBP3F5x40NtaB9b4rz0Ka1q34NJNgX-eUvLTRJmaMQvazZy05WmQvyDyMJqXVm8uZ8Wn9OgzReo2vpcJzte9CV77OlgR6pv7sgMslIKoOCCnL3zfuV79SKo5HLe5_OJfm9UQqDL05rTRlLXaNxekNEI4vbzUawjxVRkr3ytdcmLsQXddRPPpOjOlzyKreP3h5IDnzzl26Q-a9mqQYR8kDLj8WeBrJvMWZTU6HpWvKqtTdnKNBYN6pI4of90d35ys6YIyd0TB9aJthbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/28443" target="_blank">📅 01:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28442">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=A3_W8PGQ5re2UG-ElQ7HvbriB4P4WTzsuwshkUAv2DJ51pb26n1f2BCruQCnHFOkkR5w0r-Ke9yGVHOdPlEgkDtDvlhwpXqG2UCtR8ugkrNm7jCW682cAd_KsjA-U9vo9Q2JJv3O0xJOzWriL4uXyTf4gcL0tPiCBQf-qmyc4U27U12Bg7VRi9HgjBJZX90PYlSZt6qMK2Sw1ScYuVtOd2D9-kmMu7mqK6vsuxLZkXjw0i7H4JxKnOZacvOgrw1aJBpo3G4HT8yfO4fVjajDFyD9z6DJ1cLxRPhJm3BhHjkyjnbtHhm_gCMbksTdHpjud_dJLfSS_bQjGEmZE5gmeBr1pvhx4zLDrTP5cAOSwmA-kekg1xQljxCOw46cQPtEN4olMHpV8nbeRDi0QHgf-TdFyeQUrn9r5EnfTcYIlV0RIMJsaUxI_vPp728ysStak-OpS0XU5JwQqGcP-wWgN0fRGHkEiKLn1rWzbpZ_eWeZ39RIC5OgR2hpof_wA8Hho0Xe0gIYyf3dIhRjZPpyUL4_eErzD_GJ8Ljpbjd6wh3jZVb4SywgrXXCN1GayGacY6udL0zqw222NIQerbasTsdaOfCDQizjvA5Z4AcvAaKl83EIPpzzMQxv_vG6ol1MXISta8_ouX6SkK_7MQ0x7Op0HkYuKmdkXIwzFG66eyM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1b5debf9.mp4?token=A3_W8PGQ5re2UG-ElQ7HvbriB4P4WTzsuwshkUAv2DJ51pb26n1f2BCruQCnHFOkkR5w0r-Ke9yGVHOdPlEgkDtDvlhwpXqG2UCtR8ugkrNm7jCW682cAd_KsjA-U9vo9Q2JJv3O0xJOzWriL4uXyTf4gcL0tPiCBQf-qmyc4U27U12Bg7VRi9HgjBJZX90PYlSZt6qMK2Sw1ScYuVtOd2D9-kmMu7mqK6vsuxLZkXjw0i7H4JxKnOZacvOgrw1aJBpo3G4HT8yfO4fVjajDFyD9z6DJ1cLxRPhJm3BhHjkyjnbtHhm_gCMbksTdHpjud_dJLfSS_bQjGEmZE5gmeBr1pvhx4zLDrTP5cAOSwmA-kekg1xQljxCOw46cQPtEN4olMHpV8nbeRDi0QHgf-TdFyeQUrn9r5EnfTcYIlV0RIMJsaUxI_vPp728ysStak-OpS0XU5JwQqGcP-wWgN0fRGHkEiKLn1rWzbpZ_eWeZ39RIC5OgR2hpof_wA8Hho0Xe0gIYyf3dIhRjZPpyUL4_eErzD_GJ8Ljpbjd6wh3jZVb4SywgrXXCN1GayGacY6udL0zqw222NIQerbasTsdaOfCDQizjvA5Z4AcvAaKl83EIPpzzMQxv_vG6ol1MXISta8_ouX6SkK_7MQ0x7Op0HkYuKmdkXIwzFG66eyM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛ پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28442" target="_blank">📅 01:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28440">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXIOjJT8cqmPSCGfE0pUeWYl2kMzZzH96lJxtYEh-19WDxiQQruMABHODsUtPaNflYtp4VYyLZIbtFFS14zxqnGFB532_lEFlSckVH9J-4pp97ZUW5SjetK6SkzdZtvYnFgnF17mUQhGkDnQO9d4z-qMTvZYr13cQVSqmcf8Mol6BV6MSTaqkLd_F48rYA-rsWZc2sDJO-NHM-JiABR-A0JzH8fpViDnAa7VdUlSCRSBpitiZ1iLt6khQQAuShJAUFvftfLrUcjsvIU-EPhKqRzLTx8JnDQMxmjQEU9elGQUPYTrNtkbckoRc6hLTdf1aDWC2w_J69ePEV1c1VHuWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
فرصت صدرنشینی یاران کریس رونالدو با جدال مقابل الاتفاق در هفته سوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28440" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28439">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpqHPbyJsmQCqoQAX8FzR9qb-Q-4c5s-AM2T_Wti_TDXP0x9OxaKeG7aFgCcJLFTo1BpD7gMGBaPkJkR1lQzSohatfTtbsyrmP8ByyZHU_zRRGHgJRZGBCW7ZIgPWlNhKUB_HPjqQRn9LvPxzCymGDxelvDBj9PGm6xE2qo5OUpOqKhfm8-LKfTZPDrp1t6e2T2cUtyvHp5zhS35xN3UipTou4JpfYzKJsYXnAjKl-qAn6_Z4Y94-cdRCxA-B6MOyx5xP-Xbuw7UxkWWb2KlR96k4cTLuRnxW2Z9CAmvtog4bqQVnGrRJjyOUKAs4xuR2UiBAWoTAx_Gl21qBjIOrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌‌دیروز؛
شکست پرسپولیس مقابل تراکتوروبرد ژابی‌دراولین‌تجربه‌مربیگری درپریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28439" target="_blank">📅 01:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28436">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=dMTTn5ga9bCdvWAeqLl-AFit50GMwpEFQEieAXBxgkfPZYaVB06id6YfPm6buQqF9SBnSMXRCDx4TfTTdKb3rKm_aOA-DXGhDm3xUv2W-R9oQv4twIERwrAl2wKEE8u0gfWNlFT3JR7rwKKy1Ka-rTMdYydM11X02vlIdZkHp35U0oORxcCsKiNGCdnlTb3-eG-ZgC64rZsP8j3RFnpq0Na261QJnO-62d6ikS9AT1mSl_8WI3szBWS8RGZP6zYAAwYmW281gg_gN4m7RKeGuU57_9PTQKaL05x0vq6yVCsVJ5atHvuFCeXzFLA3Exn6V4LG1Nj3TSpA75jGShhzwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5d9ec1535.mp4?token=dMTTn5ga9bCdvWAeqLl-AFit50GMwpEFQEieAXBxgkfPZYaVB06id6YfPm6buQqF9SBnSMXRCDx4TfTTdKb3rKm_aOA-DXGhDm3xUv2W-R9oQv4twIERwrAl2wKEE8u0gfWNlFT3JR7rwKKy1Ka-rTMdYydM11X02vlIdZkHp35U0oORxcCsKiNGCdnlTb3-eG-ZgC64rZsP8j3RFnpq0Na261QJnO-62d6ikS9AT1mSl_8WI3szBWS8RGZP6zYAAwYmW281gg_gN4m7RKeGuU57_9PTQKaL05x0vq6yVCsVJ5atHvuFCeXzFLA3Exn6V4LG1Nj3TSpA75jGShhzwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🇮🇷
رامین رضاییان در اولین بازی‌اش برای فولاد به این شکل پاس گل داد و فولاد به گل دوم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28436" target="_blank">📅 00:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28434">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cATBTAUI3sMtMVTIT0vBPjBkTTnB444eJB8DginZvg00fP_whz-yeDC3JpuAQcUiOqY6rbMFLHpe-3F4r_yXpUzM4KLEAFpxxVA-Kc_afna9a8gFNvOwuzrFZd3fyKlDkrmV0-XFgVYAUUTWZ_aV1VceYdPv3XEu63JXvPlhiqDNE1ASyOPs0eEJaU3VnrmAEqYt_gko_umv-NGNgGrQv2hvLi1ID0CUNkAJItFtzOoq8m24zwdEmoIANZdr5GXwSQDYWkSwO9pZud_aghWsBkjfF6CbzmRhOBzVS1skndOxrG5HF-qv-hG1F6xhSBGzvFr76XiOdOWqYg0vBG3EUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HY3RklaKzXOMUqKasPHwIbK2ZOc9t7ZiV3grXL7QFW6_1D6vHrhY_8YktQzdxLUYQ0GdK5IV6hKaxJzP39KE5ICWXVdTyZfeAEb2lBzC6pCDvl2Qp7ZDLFnVme8wjorZ0jySmphbAAxqPWPoAUTsxAfJjYnlDD5ullUmrmC6uh6uUaxHLch3IjGDe0SMFyWJAOvqaOqVmo75QKofiSo_Z_ATlItyfyridk-r1DB-nHE3BffzCCo0Tsa2csW5ecTbIomSiVOgAF1HSXkxqCpJK2b1iK_I8uu9owsV8l7A0ubBeflF10qplQw1FebmbYCSZ9cuqdg3lkZLXv6S7fb5cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه‌دو دیدار امشب؛
پیروزی پرگل گرگ‌ها در هفته اول سری‌آ و دشت سه امتیازی و شیرین آبی های لندن با هدایت ژابی آلونسو مقابل یاران آلوارو آربلوا در فولام در گام اول لیگ جزیزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28434" target="_blank">📅 00:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28433">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dvxao5Cj-6O_vd94OZMDidVGJ7Big5KNrMCRmjio1Eeumq9nw5FF4WTMlDlWQpS8OR__cTc1nsuG5XjdZtuZmFxNUP-4tci9kKUTWYAyDAVHoy0ovFKLB62_A0Y1e2Xjj74Ud4K0lXV9aX4-23LWOcq_q46YrJXMNF6D3txorNvhg4p4C5xdy_lbPwwoGlIFFpidUsBgs0Ntm055wunDgjr8QuSHPo7LsGxX7_PhpJgZ1KX-i2vMYBHo2148f91MFUqQUdvJ0UgiCHxF59fA-eTAMuy2runy7xQYTVzUokUJyfwqFWXx4DEYJlfteZP6cepKvSSRyxj5clY8fNNQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/28433" target="_blank">📅 00:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28432">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVcgAER0dr16JgS2oeShVwCudSHLuhvUe6JdSexnxH59hZjK83j2mzJjOw2skTQ2GU0p9fHMzEOpSSplrLqod7dq_kHQuMPFsQkwYt45V8BmmiQMFHmJ7Biz90QHKa2ge1YN3Ry1vwKj6mbtydXiOntVq1CAGU9GtnMAKpbHg-Tp29HKTxJSQbkckFgYFcOwFjPz_KMPZHSCkilmi_NZSn5dp0gVGtZL8-cpW70hbiNBZRSqiNUeGJ7041VyWPjFNHBwLffcrCyiRDkjdclheg1lo_ZK14lFPrhwPOrdJeCjquMUgPb4SHX71ygQ0xPX9Eh4G5SHQ0rrTQQd-ZBRqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مدیریت‌باشگاه‌پرسپولیس حمایت‌کامل خود را از مهدی‌تارتار سرمربی‌سرخ‌ها بعداز شگست مقابل تراکتور اعلام‌کرد؛ حدادی مدیرعامل تیم پرسپولیس اعلام کرد که کادرفنی تحت حمایت کامل اوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28432" target="_blank">📅 00:09 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28431">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVUkqS1OCkTY--2sNBaHt-jpP6gOR1ICJ3TuqEPS__ub8oeqfRZAOuW-U9MqCr_uzGLpxHcmYjeyXzh-90hXeTuDrceivR90KTLNer1WN1lrQYxNkNT0dRV5T9xp126c6asmGQat78w_CPesf7Yvl5xAQSVk2YMpIKC4_ZbIqA265r98pPKbMCec1KUACwtNrL_x-yjq4Hj6V0zCptgxzpdmwXfJDJZyZcjlg4APcgemNmqys7_xGhBGJhEDprTPZjyHARTLYGv3WL2jPqTLjoCGw3CpQzZvNtbndfJUz99ue5fY-RAQu0qvJCqnyF5GC9p4AGQ8UsyTwGsQiuh-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28431" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28430">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/206c65214b.mp4?token=OoaDhd54GesUnALItWsdvTeZ0xcjrpfpUE3yuiBH8hsTIu4yRBgLJ6t9SB3Et9hjmvIMShcZeZkMr2-t4Xr0ALhRPz5_eDHcX0HpMhTrdl1j-WbEwCxD6H2pyVULVRSVh_hp3AZRlue9UYX62wFpgeJMjOhea3LCop9BR9leTAUw9S2-d4lvDihCQdY3MPFmNQnVI9h0Ax8gLDxk3DS94BKCdGQ80nsf0DpapbL0P4uSPxnYBgUzqo6CndyvGkgnv67ia8DwHgZUhN-drPrrnjf3NX96AcdXzcS9V3gwIH122Fcdvv3ikN2wn4YP70IQONCTuPsmD6RcdzwveD7yuTEghxBamC_-T_h6pB8J1c3DxyzfRt67dacY2yD1rqHn3QryJMFLcQDVeZzm_AMhcl1TR27OP875iggFMxO3ydziZurlXSuIrH63d_wqs495bzHbnFgFaQQHCRhF1kIZYMBt4QoXGwSnaem8I7CH0AuAsllQX2Ms9IyBZnJnH643kKNM2QCj74qMhT0NAe4CH-XRvOSP2cJQUm2q5bByCvbA0jrktWJItLRFGa-Ti5iT7V7htzqGhs_wfjhvEBybPjuVjUzhYE7aKstBKC57lF5Tq3Q2013GG4vSdSJJzJ7qMD5Jac0SFiO73hxqkoMFxi5d7Rm2UE_GL_QML-VT38I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/206c65214b.mp4?token=OoaDhd54GesUnALItWsdvTeZ0xcjrpfpUE3yuiBH8hsTIu4yRBgLJ6t9SB3Et9hjmvIMShcZeZkMr2-t4Xr0ALhRPz5_eDHcX0HpMhTrdl1j-WbEwCxD6H2pyVULVRSVh_hp3AZRlue9UYX62wFpgeJMjOhea3LCop9BR9leTAUw9S2-d4lvDihCQdY3MPFmNQnVI9h0Ax8gLDxk3DS94BKCdGQ80nsf0DpapbL0P4uSPxnYBgUzqo6CndyvGkgnv67ia8DwHgZUhN-drPrrnjf3NX96AcdXzcS9V3gwIH122Fcdvv3ikN2wn4YP70IQONCTuPsmD6RcdzwveD7yuTEghxBamC_-T_h6pB8J1c3DxyzfRt67dacY2yD1rqHn3QryJMFLcQDVeZzm_AMhcl1TR27OP875iggFMxO3ydziZurlXSuIrH63d_wqs495bzHbnFgFaQQHCRhF1kIZYMBt4QoXGwSnaem8I7CH0AuAsllQX2Ms9IyBZnJnH643kKNM2QCj74qMhT0NAe4CH-XRvOSP2cJQUm2q5bByCvbA0jrktWJItLRFGa-Ti5iT7V7htzqGhs_wfjhvEBybPjuVjUzhYE7aKstBKC57lF5Tq3Q2013GG4vSdSJJzJ7qMD5Jac0SFiO73hxqkoMFxi5d7Rm2UE_GL_QML-VT38I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
#تکمیلی؛ سردار زاهدی معاون‌نظام وظیفه عمومی: علیرضا بیرانوند ازمهرماه سال 1405 سرباز خواهد بود، و باید ازیک‌مهرماه‌به خدمت سربازی بره؛ زیرا مهلت معافیت تحصیلی این بازیکن هم آخراشهه و بزودی به پایان میرسه./ حالا اگه یهو زدند معافیت تحصیلی بیرانوند دو ساله…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28430" target="_blank">📅 23:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28429">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9CUzLSmwRlEo_E2BsrVP22PcriTbknPVwS63YiDH2eJBJli1z52llZyVHd_WFNnM-ofrlMIX0uTHu0xrv3Z5KdAk-rt3qRFERTe54iktAeV0fuyp45Lm0_ouCHv1vEFjo7B9B1omRUm_sC7YlFZ8wi0YnwNLXJNAFdZ3cyfQbOJj1p-3H27NuEoIE4FUhkFleqEuj6XVEA98Itwell_uNzscdLPX28c3Go7xi1F5Cnc9mj2WmV6c8pjllMe4pSGzmmN2VhDOdlW_05g3ipU8GP-LeVnTljkVkTOEsywl5iSBVf-Z6YWaRvayj7Od5MEkkcx4WkL45wM3JH1B_PGjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28429" target="_blank">📅 23:26 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28428">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbf8bXBFPp098vBTDqnVexWUCxowbPP3G6uXbjHUpef0scN0bsrTc_lJ8JGCb_9AQ2O2n5eL29aeoClMzDzowTtH_lZbtfla-dYoI4f-XcVz1jbv6ntQYp7PwXCxOMJJNPN2khTuROlX9jIGr1Sjxk4YpWdPKnjBrb_A_SFFKzbpeBmv9kIV5eWe5Emhsjp29nLdqX7o9Mygbv2Q-Jp0Ki98jCqdgGgkRzxYEIDIbgOtO6DUuqff7MD_hWY2KnmT19th19b1u-F9_a0KORwAdd1Ou94AY3cWLIUt55Xjaa8qFl7Ccfr_oK7AnN-DqrZyrl_pVZ07dJqk6SWvna2k9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گابریل مارتینلی ستاره‌برزیلی‌آرسنال که همسرش گفته بود رویایش‌پیوستن‌گابریل به رئال مادریده حالا درآستانه‌عقدقرارداد 3 ساله با رقمی نجومی با الهلال قرار گرفته است و موافقت خود را برای پیوستن به الهلال نیز اعلام کرده و تنها توافق بین دو باشگاه بر سر رقم فروش…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28428" target="_blank">📅 23:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28427">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGOMXczx8-8H2SFdBvaZY9juU3j__Z28OCVyLnjnwQATJyW5FDAfuHRp7DdLQP8RluACSTgjaIMovu6tgFqk8YXRStiR1mGF6J2RhicxRcSAJDUA9kXn_8WU8e4iDiIhHkY5mKLYKn192nTXpE8W46x8NEycdmjiHEIYCIJgblJJ7CsQXfSD-9sy1QnsTom_Ma1pYvxjJ3Fi-MHmSbXSwO56X8LOMSolTBg-W5TzqbPko_xm84zA4UB8zvRW_9rfsFfXsj1xog64htxtmd_B7nKeA4U7aqqRm6ogw4a7kiGQbQO8cemqza3ubSzfNDRPsqReOG5abSCYVOourkWX4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28427" target="_blank">📅 22:40 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28425">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jxsscrs9ve490SOSBp1OCaQHSvZ3xMc59Sit9zPz6U_eWOE4HqZ_CwQSTEUOZO5Zg4ecgxCKdd-SK3FDMgei8bRmbCznz6JwKnXoc3BjQBRhp41jpIgdkZTzQnIMQrah6kYETRLzPHKnvs9DGYPrGVBMw49xg5Baauh4Bz6Q118wPQRO-bQsF1PAA9TuMuuToBxthSqK4Kua2Gfi8-fCFBuAgwmOq5xy2aYfTKCErhggoVPFOeUxOWFIVt9j-84RRDe0Kgd1hFiRJ46kvJlz_2pZHDnQ3LxkoIKpKsQQZpCcokQioByBCAUVKxynlurQIcCMNr2MwJ8xXWj46PaTcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsJa54g-mwo9ljAKyeazwP2bNDsLmbs4ocGQh0ac5Be50j5YSaTNxUE2LaP9Vz4nmPdXSkC2mXIxmf67ibmdZOzh-e4xCA7gINykmy1EMFlAKj9CSKdqbJ8GliojZyEMf2R41noRdVhAVUlnL_KUdhppJlQ0wxqCLU14UmuyYXaDMI5YFkSlM_wziU0uwReAz10GlED0dynqyK6vgKODhj35tWj6Jp0TBHKXh1hFnEtEsFVONgTnlIWRc--dOFb9TRKanjw0HY5TqnfrxIMfCwG671764NLSV2EiHYp5H3ZmbX9jSlX7NozEoYtqXlQxHPh3OnFcEOH93s9s0NpPjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌رده‌بندی و نتایج‌کامل دیدارهای هفته سوم رقابت‌های لیگ‌برتر؛ آبی‌ها درصدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28425" target="_blank">📅 22:37 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28424">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx0GU_KjP87W1gRIXUwu64ViHmdxNMz8ElSILTeyuh06wTf89Y_7prks_MnStIhdgoX-t1f9NcVcZqMPNa5tdr9tn4Vm2MchfEzT1BxtzC1vgK6xoOul4KYJcFJ4bFcThm8t4hdbYx2F4DBwoA1wIFVQbTmjIqUGbpAOFeBinQkduGCsqv1vfch2oK4OQTSDb-IluXwpzOrWuHLtZD33X6_4w8LaSYWILkoTn1hbl1AR_KPzs2kXur28Q1kdp7_VQrOlj5cJH6TBCwE5DyoPBUmmClXtDhvXWjzceqC6Y98gOSVKbgf6irThgROoDuYRhzKVOcJo6Yu7kXCCd-obtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اطلاعیه‌سازمان‌نظام‌وظیفه: بازیکنانی که مشمول خدمت سربازی هستند تنها میتونن در دو تیم لیگ‌برتری‌فجرسپاسی و ملوان بازی کنند و امکان گذروندم خدمت سربازی در تیم نظامی وجود نداره. علی رضا بیرانوند هم اگه معافیتش رو به هر شکلی تمدید نکنه تنها تا 4 شهریور…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28424" target="_blank">📅 22:07 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28423">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF1HfZn1QerLcXUDQN4b1PlvN8tx6Nqp1KLP1sFMXc_qN6GWaf-8SX9L_wjG40U8xvivotODnOa7og8xD3A9hFdW43IGAbbBEsd9xUor2bxYh6ihMsfY8la7hKUg3Nh01vroT-DqZOAWUcfUOSHhjVrDI424QPVKNYbharYMvAafRvZIp9O9mSeVMxxTIvIXoMrLa87wFDvo7LrIOVbFkMwEwfX9CzZIK9lMs9KWrKVKg88rqt7CMm4H8295fgNm_LQM1BgTqSGbs7joJZQib8ZKnxBy6wLfubVXFvWo_tQjgib-9l6YSq0HCMwct1LstAuMIVMuzU5wOaq6OhDLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لیگ‌برتر|پیروزی خانگی شاگردان جواد نکونام در یادگار تبریز و دشت سومین پیروزی پیاپی و ثبت اولین شکست فصل پرسپولیسِ تارتار!
🔴
تراکتور
1️⃣
-
0️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28423" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28422">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9gxmaR__9jrETN8uPPeSYSTg3V60n1p8Nx4qsNExSvObz1MR455bhMExgnj7R4XImqM3a0Z88TgbLTJjrqB-i3CbPhWN5Tg_o876TAK4-RaDiPdfcm13hJCc8GaqzdfKfQYsS9H73fb5jucmYs55yadIQ-YbK-6J9CUAspS_VYULK7AsgbeRBLMDyqYXAwQ4b7SFpSMfoGOmNoi2NCy1VBherfwHpb0Zn8J2XoU0UafsPKPWMZtWS2cQC6vSB5IQo_MH1rIFnCJCHg4R_IYmtcSsNzyEeOPu8WQGoVV617cQ6cs6KT5kgXnUmOOy7BO_w3a185B_7nQErdGShep5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگاره از تارتار پرسید و گفت چرا اورونوف و سرگیف بازی‌نکردند؟ تارتار برگشت‌گفت به دلایل فنی بوده و حتما یچیزی‌ میدونستم‌که بهشون بازی ندادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28422" target="_blank">📅 22:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28420">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9248dbd6b.mp4?token=W44Cikn7WEX7Fxh5gmtSsdbiBsPTbJ6YLKJ7qAnJONSkFqZqYmV9yfrkUWGTpC7egB2gXZGIkvRPJXO_Spawm1pPGv1ly7k5OC3R7C2_uG2QElQxeMg8Pd-eNriM2Su5m9q0R9_1jzVJN-k9nzpSd-Q1nZ-UO04lEGvh3QOfKN4zr6oNU2pNt-2ZrOsWRCMr4LJNdfVS7lPOLXvnM2NXCKQKV6iLdJPc90MdFzPUKlzb3aNyaaL69YNW53bA9CpvWsoRiDGcV8MivY4r8APyKsSJQCi1iuXTLmf1hdQyUYKn_j6YKAbIgswD_Dw8SW1fV-db2E5BMNMdxQTROZmusQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9248dbd6b.mp4?token=W44Cikn7WEX7Fxh5gmtSsdbiBsPTbJ6YLKJ7qAnJONSkFqZqYmV9yfrkUWGTpC7egB2gXZGIkvRPJXO_Spawm1pPGv1ly7k5OC3R7C2_uG2QElQxeMg8Pd-eNriM2Su5m9q0R9_1jzVJN-k9nzpSd-Q1nZ-UO04lEGvh3QOfKN4zr6oNU2pNt-2ZrOsWRCMr4LJNdfVS7lPOLXvnM2NXCKQKV6iLdJPc90MdFzPUKlzb3aNyaaL69YNW53bA9CpvWsoRiDGcV8MivY4r8APyKsSJQCi1iuXTLmf1hdQyUYKn_j6YKAbIgswD_Dw8SW1fV-db2E5BMNMdxQTROZmusQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🟢
گل‌های‌دیدارامشب‌خیبر خرم‌آباد - مس؛ بازی یک یک شد؛ مسعود محبی بایک‌ضربه سر دیدنی برای خیبر گلزنی کرد و نیک نفس هم با شوت دیدنی اش روی حرکت انفرادی‌اش گل مساوی رو به خیبر زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28420" target="_blank">📅 21:39 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28419">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb30f0066.mp4?token=sVR9Wut1YAJaGXtx6Qwu_XjoEn5to2v3rYtjAUY4EOMYhViwMHtbTl_GQpQ49DzE--1rvZB7f-5nznR4TBN0J99Rfi7qy6M5HE16QsGrKl3P5DeD1vVXWnj9Hzbzhs3Zu5G8uEIpBmSsDVi3BRrOtkLdFtVUyZ5vYincH79UFpeqGd1eLRkBIL7ebIsyBmQolmU8YuY0Umq894yJMlq_RptPtivK8qT3qWNqFR2zpogEaqFeSAyLU5RNglYLvrPeqePCNqeiFMvexcolKRZjhfM3DhDXYOiSCVVhu2cxRPoq0w6IUTB35qD5QxzyylRzr58mky2Aig6iPxvgE9xfzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb30f0066.mp4?token=sVR9Wut1YAJaGXtx6Qwu_XjoEn5to2v3rYtjAUY4EOMYhViwMHtbTl_GQpQ49DzE--1rvZB7f-5nznR4TBN0J99Rfi7qy6M5HE16QsGrKl3P5DeD1vVXWnj9Hzbzhs3Zu5G8uEIpBmSsDVi3BRrOtkLdFtVUyZ5vYincH79UFpeqGd1eLRkBIL7ebIsyBmQolmU8YuY0Umq894yJMlq_RptPtivK8qT3qWNqFR2zpogEaqFeSAyLU5RNglYLvrPeqePCNqeiFMvexcolKRZjhfM3DhDXYOiSCVVhu2cxRPoq0w6IUTB35qD5QxzyylRzr58mky2Aig6iPxvgE9xfzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهدی گودرزی ستاره جدید گل‌گهر: مذاکراتی با باشگاه استقلال داشتم اما به دلیل بسته بودن پنجره باشگاه استقلال نمیتونستم با این تیم قرارداد ببندم. آقا سید همیشه به من لطف دارند بله با من تماس گرفتند و درخواست کردن که به گل گهر بروم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28419" target="_blank">📅 21:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28418">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e283ffe059.mp4?token=iTYK7oEtWHUfm4Ujvix3UUk0dX9LAhYRCpCWAmKDL3BREEBf12WNqylwe9wBEBV7JQkqiw59HAasLfSIY2jR1vqKXXQkfeuCmK8qBsN2hnQdoDOORJenDYGRBc143MxSwLIAWVXr0eaNW2NIt3ynF9oKflmrBfdUI-nBlAHPQnG2Z18GMN6YhxNEXMbsznSUeZvkXuemsHM4MFo4UndoKPqaIrBxbcLwkLmDfxOMagFFgkuP012stLC5tAx5waT1slwUtW-pefh1cbpR3tlhX6OwOcZ7Jp89M9sibMGsQQgs3apAlVG_E8fccmjvRAK-QfL35yf5UiWbd2H9YQatug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e283ffe059.mp4?token=iTYK7oEtWHUfm4Ujvix3UUk0dX9LAhYRCpCWAmKDL3BREEBf12WNqylwe9wBEBV7JQkqiw59HAasLfSIY2jR1vqKXXQkfeuCmK8qBsN2hnQdoDOORJenDYGRBc143MxSwLIAWVXr0eaNW2NIt3ynF9oKflmrBfdUI-nBlAHPQnG2Z18GMN6YhxNEXMbsznSUeZvkXuemsHM4MFo4UndoKPqaIrBxbcLwkLmDfxOMagFFgkuP012stLC5tAx5waT1slwUtW-pefh1cbpR3tlhX6OwOcZ7Jp89M9sibMGsQQgs3apAlVG_E8fccmjvRAK-QfL35yf5UiWbd2H9YQatug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسینی فر مدافع ذوب آهن در بازی امشب مقابل مس شهر بابک به این شکل تماشایی دروازه خودی رو باز کرد؛ جدول آنلاین هم پست ریپلای شده ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28418" target="_blank">📅 21:24 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28417">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxKChosBnulUH5PMjxJrmnGMYgxsYel5UIdmt8CN-eOksUl8yH31OYqH6HzJXimUSgj-mHfTnPyio3dAz_UFkdahaEb-_NlXGrfaPMr51Q7rfr0mN-RzYV7O2SZbehBXMVHmg8IMnCy6N132iwgleBCmxs4lMejWHBeJGl16SOV7G3gAw9Qe5uIYynJr7u59IeL05r85_XXgXXs3aElPyEQngd33KuDrVt7ZCw8Oxvx494vUXigbzRsakigAoZbKQS33KHY7mTalvr3Tq1hS8_MNWV0jniQXWKSo_4DI-pk7UWpHnmloFyfWGwVELEibSpwzLXBs1m_ssDIAL4rGjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برخی‌ازرسانه‌های پرسپولیسی خواستار استعفای مهدی تارتار ازهدایت‌پرسپولیس شده‌اند و مقصر این شکست در حساس‌ترین بازی فصل رو او میدانند.
‼️
ترکیب‌پرسپولیس‌بعداز اومدن مهدی تارتار در این سه هفته هیچگاه لو نرفته که گویا به بعضیا برخورده و منتظر اولین شکست بودند…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28417" target="_blank">📅 21:08 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
