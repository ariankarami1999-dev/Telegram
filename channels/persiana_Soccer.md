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
<img src="https://cdn4.telesco.pe/file/JrsEPndXhLSjgYLqJVYtMPs8BKmyyFw6I7YufMwrAmGr0ltk2v91X0R6QEfJP_UaeGn28zUvMlTG0FUF_mH5St4Y4_fYF5xAISMptj1K59NCaCBeUCYIObIal48mL2bcQGyHXLZ_1sJzera8WgmnXupcWYiHwXsoxntCvG2JyyeAIP4oURvC4rqelfBpsMBacRGGXHbuqFnpFfrbQPSEIKAFhtGdilZ8gAFX-EPz-jQUWrHzICM1lYnfobjsc-6_CW5WvkYHpqLqWU6o7R8VHwUJAIbNOtQUKPSjRdu67mw0tu53ahnVKrK2IO8_APifon-X93ujEtC7H1BBwdGFmw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 171K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 01:28:15</div>
<hr>

<div class="tg-post" id="msg-22976">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epXM9Z743yxwr9HqDlH8gMkJb1hQppwcLqE6Jua8b7aFsSP_0xa0S5walrqQhlIqpDweROqPeQHtkLubQxbEQuy7VughmlxLdA4njIZmJjzNG11L2B6TUSaEgJF4HbTiuAAOi-qSpJLvqcTLmaJBLZp34k7SN2b1Jzb9eWJBeSkFC7_LHmsoijR-ib5LTS7Ycp2vt9W7F1bPoPdPj0RezIDPEVGQNdaJ0zGpgvCwagQ220vj8Vj5cUVLLS6_XY-XOMi1i9nqAZz4xvhrfimFp0EvX6PFGLMwaZM7UggBoUYKVb_oEBTn9b1AjFpGkych48omXVBcPvQFjEeBT2CZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛پرسپولیسی‌های‌حاضر دراردوی تیم ملی از آریا یوسفی مدافع‌راست سپاهان خواسته‌ اند که برای فصل بعد راهی این تیم شود. یوسفی از پرسپولیس آفر قابل توجهی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/persiana_Soccer/22976" target="_blank">📅 01:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22974">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CH4NGGtslGiOpVbFM2qU7guRchiWiL2u8gdLXj3hW__n3xUjKL2f4KoCqOmDo3hGmvQnezxCUFuH7hfVPFs-_O0PNyRfaF6quXNhqYE0FuQXFVPw4xrlxOqkd53fOBM3rOvWOEz-rQTookPzU9Fk5s8YJxv2PTyrXsBVgGrQ1YrQ6NrT2xWcXipWzkjEv7X8GyeCIX7wkqjtUsxjyszuS3iei3pjW--Cx_dLfB1yNVeY7NJY1eSRucn_IQuE2CF94eJRMlYo5d3WfwfoxNhNzXvOU211ejzpoAb-ofxkrSydPn_HwKozMfZxrWSqomtiCvA5DuNJ2j7dxAvfs9-8gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
از دوئل تدارکاتی شاگردان کومان و کاناوارو تا آخرین بازی فرانسوی‌ها پیش‌ از سفر به کشور آمریکا و جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/22974" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q88iFgAdV9f5DsmgSTXajP90NwILN8UwZIKSpATBC85s4LSfJ4JqxoX4tDiLBs91rd_Ld_rci2vsw0pvPal8omDxqdfpZ6HUNlwIjm8OCidzyHH5dTvNQIxSJ0ELTQSlGotq38v9HFhXTkfDpkUZhuJR4-aZHy0N3Q8o1K6O63D22lEme_qxcN0ilvhna8FWLf9h-L-z0rCDTdG05240DIva-2cDfiBUDh_i4RnQeaLxuepzX4qC3lNOYHFzsveeIFrBh0tNDaHa2gNJBkqO69hVZuE9WRm3eVpb2KSFYLKIZ1vs9-hQj70uH50lVNpSnLR22hqvjWRuBcmqfWIV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از برد آرژانتینی‌ها در شب‌‌استراحت‌مسی‌تاتساوی درجدال نروژ و مراکش
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/persiana_Soccer/22973" target="_blank">📅 01:12 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22972">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tt2u4z1-X-5hY1Mo4E3orj8DoQRxsUWX6aYBDhH_QqA-tNm-h_mZCsQJXfzxOmqeVH8tEYXVg0FIjigdN3WggW1hsB6g5-qDk0ix1yhGA6-spaRz5xZQstgTIuXTLcVc8aFSxqdEK5V11HS8v_VhBcVDAMB7DTs6rryI5Dn_7AeyoJmm-3cr5l5haqgiA3m6CiuNRtyddZ1IpPvwApCkwQSO2Jpwu_gbQE60dEUJU51MuJjJDflBzbpvgbMeD2PWoNxNhTvcwAeI5fNryfvxB1wbHNHKB2zcOko4QZMzkTH5ORIvLPtYmnE-nx3nPHJsi9dXcBvPzC5Gx-uxcPB6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/persiana_Soccer/22972" target="_blank">📅 01:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22971">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=AcGdokDVD2PuhbhPzJ0dQX1057Z0a2HDZmeogSLYmw-gbnXdbFbbyHOSDSDKqcfhULXgGT3iHHyCmHon2qSBtw1EmCMH05UTzhG41QqC6sOOwyfYkPp7TL7ZACUbvL_Z6k26ySkpPAoDAblqLYirvql4g-P9ynpsFZt7BXv9e2_85acec4MgMIs0v8E47oWlrMPTtb6X7GVZIUrCFl5pXAFwLoVFu5UY_XF_Jue6lVfviJgN-B_Ac_0K_XENUoUdACt89KyR6TGd34unmdZNakGftxmsY4Zj8QoG40V5GTOPW3IFqSEC_MmQibkBr9E8OWSXYeBazT-gMUCaxr0lQqnQ0p3l-3Z5KhzYJDOzAc2j66jePH_c79EsjwzaACv7uwLa1OBLAIh3a2255pQRu2pYYowwDtvpuSoJauc8PXn_-GIjPzp7AKGlauN-6i3hHTH8t_G7bFqnAJQji-ri2JvlH2rGBdVlnGSctNfsgAWsmhq6B24oGPEm-eQhox3Ykp6jYHZ6Smm4g_Fpe_X4ccUlmjIHOAChLeQDiduPhQ2lO9K2ujuUXCs11XYhLc7pTMoPAdcKs6X4GCK-IO65AcSEoHper-a1FroPAR0_nw7v610_MKpKs7ioM3m3WjHWIqnmV2nTw5O0j7cNl2YnY3Vmnl7USAk8UF382yvKH1c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a6fa71d1.mp4?token=AcGdokDVD2PuhbhPzJ0dQX1057Z0a2HDZmeogSLYmw-gbnXdbFbbyHOSDSDKqcfhULXgGT3iHHyCmHon2qSBtw1EmCMH05UTzhG41QqC6sOOwyfYkPp7TL7ZACUbvL_Z6k26ySkpPAoDAblqLYirvql4g-P9ynpsFZt7BXv9e2_85acec4MgMIs0v8E47oWlrMPTtb6X7GVZIUrCFl5pXAFwLoVFu5UY_XF_Jue6lVfviJgN-B_Ac_0K_XENUoUdACt89KyR6TGd34unmdZNakGftxmsY4Zj8QoG40V5GTOPW3IFqSEC_MmQibkBr9E8OWSXYeBazT-gMUCaxr0lQqnQ0p3l-3Z5KhzYJDOzAc2j66jePH_c79EsjwzaACv7uwLa1OBLAIh3a2255pQRu2pYYowwDtvpuSoJauc8PXn_-GIjPzp7AKGlauN-6i3hHTH8t_G7bFqnAJQji-ri2JvlH2rGBdVlnGSctNfsgAWsmhq6B24oGPEm-eQhox3Ykp6jYHZ6Smm4g_Fpe_X4ccUlmjIHOAChLeQDiduPhQ2lO9K2ujuUXCs11XYhLc7pTMoPAdcKs6X4GCK-IO65AcSEoHper-a1FroPAR0_nw7v610_MKpKs7ioM3m3WjHWIqnmV2nTw5O0j7cNl2YnY3Vmnl7USAk8UF382yvKH1c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از کواراتسخلیا و کول پالمر تا میتوما و فرمین لوپز؛ 30 غایب بزرگ جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22971" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22970">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=jFW8rHNLU_UPoPrGVcNyGvangmKgEkxDvTnrCk48U3OKV_c47XvfESUmFstNTCSzBcyYR4_XjtYG5E6Ddl-ILkcOyPktw_C7H2fvAYhRtfVimbkqt8s-iYsoraQouG0uHy-cJcRV56QPJMCxa4kOtLO8kGpFbCsrZsJ4lN4Qb1QQywWQZ0PrXc95cs7xvyN7Bw2JkCMH0V9nB6BLV8Y8g4EUZsjwqIueFnf1Pe69BcIKPAPKu1NCBwesv8vn5QRz_KmYPy5uqixPJUkzJDAeESp6wOad8QtGfY76e4Km1IUb9ipiMrzP_kY47JwQftm8E1EDm1uN7sD23sC31M7O-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32598b0bc1.mp4?token=jFW8rHNLU_UPoPrGVcNyGvangmKgEkxDvTnrCk48U3OKV_c47XvfESUmFstNTCSzBcyYR4_XjtYG5E6Ddl-ILkcOyPktw_C7H2fvAYhRtfVimbkqt8s-iYsoraQouG0uHy-cJcRV56QPJMCxa4kOtLO8kGpFbCsrZsJ4lN4Qb1QQywWQZ0PrXc95cs7xvyN7Bw2JkCMH0V9nB6BLV8Y8g4EUZsjwqIueFnf1Pe69BcIKPAPKu1NCBwesv8vn5QRz_KmYPy5uqixPJUkzJDAeESp6wOad8QtGfY76e4Km1IUb9ipiMrzP_kY47JwQftm8E1EDm1uN7sD23sC31M7O-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ایکرکاسیاس گلراسبق رئال‌مادرید در مصاحبه با روماریو: «مسی خواب‌وخوراک‌رو ازم گرفته بود.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/22970" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22969">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0wRSkyturcpluakDmEZW8yTAnVpaJuyDlhtxk5XTjbHc4vYeFEXHuA2HVGvRKN56CUOPihu4wJYwzLnlCJ5VT_cA_f4jOn9tlgfNN0RbsDnx_Qn04LVgD0znJUXxv82uraJAq-nXHUkkWJD1GgIrewW3ptV5nz_v0inPtKPx2BGy6yYdcP7mUCbkqhMUloef4k270V6Zof6XRopF-ttENqZYTEHjhsJO60bie41ObtSbW6LZ4oGH8VuZ3GV5qVGkviKx00kBtZVTGLxj7P3CvT6w-siuRuXp5JF3Hr7YBFOwyQCd07s8JvfKwzbvsJC9giC4QZY7qtHZhdOS3qn_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
🚨
کد هدیه ثبت نام:
GG007
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
https://t.me/+aCbq7yy8QY80NzQ0</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/persiana_Soccer/22969" target="_blank">📅 01:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22968">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sOPCxBX5qafRvlvFvRzL7sPiJyo4N54A-2SJtIpx2x-zMF5xeJruX96HnWtiFf_U3sjSTULHLJHZMvNj-Rz-ZsH2ohM-jgBtiabNUm_G0JVOoGxSczOI59j3GANvN4ZmU20ExkKbYmF6p-Dx2Rne1TZxkZrmEKLgM7jn9NT_mdQZZSMHKvbyfmwIb23ARejynYHBqrA-3DIVZErhAa-axECzrwNhoL19gPfuWeZHKbLCx65rLV4_WDBsQyH8XOyJTzkqaLH-z_uRl9nCHeJTrV3luTSUNzf-mw47fvAoKZG1vb5SFWbs4vSUMGj179n2ncYrnZI7iAfGnqqeIuYNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای رسانه‌های روسیه‌ای: دو باشگاه ایرانی خواستار برای جذب کسری طاهری ستاره 20 ساله روبین کازان روسیه به این باشگاه نامه زده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22968" target="_blank">📅 00:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22967">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=jHIgSgrA6F9-3Zqi0TyFisSG5orbcWYz5kcsrihc7OzncSIYr9BFnBr8Me2eH-Te1b1_ggwzNioajX7bXzfFOM8kq-6FjYAqG0EtEMN96DAi6YMJznNPlE1k2SCMGB9umiJBmeD6hA5GMO2rT7umlwk9D4VZhg2FvuDJppn0yOzTs2w0W5QVgEtsUfPWI9yH_LfUe4k80_Musd1QVQvE4iDwzmCUz8I2oC_e3LE84bKFAvktDyzvbJu1p8HBktAMhXcs2IZPMZaSc2avaXHNZBzEv9PwmJYRG8OENPHB3K5fXTUBaZAFnAPwzxUD9FMiDXHpd1NZK_Lh-hIeyrsdeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca6abec005.mp4?token=jHIgSgrA6F9-3Zqi0TyFisSG5orbcWYz5kcsrihc7OzncSIYr9BFnBr8Me2eH-Te1b1_ggwzNioajX7bXzfFOM8kq-6FjYAqG0EtEMN96DAi6YMJznNPlE1k2SCMGB9umiJBmeD6hA5GMO2rT7umlwk9D4VZhg2FvuDJppn0yOzTs2w0W5QVgEtsUfPWI9yH_LfUe4k80_Musd1QVQvE4iDwzmCUz8I2oC_e3LE84bKFAvktDyzvbJu1p8HBktAMhXcs2IZPMZaSc2avaXHNZBzEv9PwmJYRG8OENPHB3K5fXTUBaZAFnAPwzxUD9FMiDXHpd1NZK_Lh-hIeyrsdeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🇵🇹
امسال مدعی ترین پرتغال رو پس از سال‌ ها در جام جهانی داریم اما جای یه نفر خیلی خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/22967" target="_blank">📅 00:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22966">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8bUwpG07T2EG2NMPiq7HUABoNlDxWfRdhRi8jCWPpBeflRg_IqxqpX9BomlQh7p2Ke-0VrO3mMKLBnMUo0PJDTq_eBPNBzEYwLluiPyB77P8nH_J-QVnlwf94q7wcqPLv2YX2XrlqbzQHu2penFyH4GC7VgTCka0817w7ICBEp9uBAMRAoBHaGpUWpcrUEzn8Qerfu_CaHlZPksJtGgcF8gQ15dovp3hH4vLxcBDmX8bQYastY9BaUGgwvZr92EyQY9zwUBRAGshiEBIgAhxk6rKE6LtghYrerS-PwGkldzFVqUN31oH4Wa1eIM4I1gNqkZKe7YwOcJ2WNUJ4I6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22966" target="_blank">📅 23:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22965">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGXoc-m_AoLPQ14aBAkM26QvQXEavkyGgs5MDQqRLUud-1tSwWo8hIjlEHOADpEVZsE9HBOvDjXLEI3NLdPkXxd4Qq1Kgiv88xZgmFzaP78xCoXy8wWMPwVEq998S8VYxH__2vZPGKcId0zUxHBTg8Dm0kGeCcNUIPDGebpYnsk-kiSV36rB5XBGxUlj5Kn_tR63bTUXX3P-Gs85aZYl5D3U97ObPzFimrqK5aC0hr2pj6DYn5pfNjxyUZXBfD_FLzBxERqymqCzFdO89VhiLjw_YdtL0ZRUtzefcxWT2XJEhDLIO-FNSAMapWpK52_nObuj5-xV-pFWM8Ikvwb7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوشش‌کامل‌اخبار جنگ در کانال مردمی مجله 21؛ نمیدونم چرا سرنوشت ماها اینجوریه. انگار نباید آب خوش از گلومون پایین بره. امیدواریم که حداقل نت‌ ها باز قطع نشه که هم اخبار داغ نقل و انتقالات تیما رو بزاریم و هم برای جام جهانی دور هم باشیم بازی هارو پوشش بدیم…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/22965" target="_blank">📅 23:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22964">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=HMuF_LGFPmdc4-5yj_We-HFtjYXzuz-eYOM4NKKhlN_bQFtVh2A74q4G3Gp0ewFDP4m60mqfe5gtHe9aJgc0dO6G2WE5HSPJXM1P9Iop4nvauDOWOjrH7--cuFszpyigzdC5xIN9Rq5Sy7LvoB_bvxgPV5TU5k71_M6NUhHdbrRANWEMZVFSq7jNFnR3EfpkVuyIKccEvfXwnnkKgboU2YAfy2A1j-lbMkgyAgDC9ZqblIcaog3rg1hCTPY8kiEtnpznZrLGuyVkH2A1YszcGY-KkQt-n8nG_dBghAYw-V5Ef_x-XRDcAihy4ilcsVnHrv3nddwxKTP1oD-QHJmB6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eaff3256e.mp4?token=HMuF_LGFPmdc4-5yj_We-HFtjYXzuz-eYOM4NKKhlN_bQFtVh2A74q4G3Gp0ewFDP4m60mqfe5gtHe9aJgc0dO6G2WE5HSPJXM1P9Iop4nvauDOWOjrH7--cuFszpyigzdC5xIN9Rq5Sy7LvoB_bvxgPV5TU5k71_M6NUhHdbrRANWEMZVFSq7jNFnR3EfpkVuyIKccEvfXwnnkKgboU2YAfy2A1j-lbMkgyAgDC9ZqblIcaog3rg1hCTPY8kiEtnpznZrLGuyVkH2A1YszcGY-KkQt-n8nG_dBghAYw-V5Ef_x-XRDcAihy4ilcsVnHrv3nddwxKTP1oD-QHJmB6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی: فلورنتینو پرز با 64 درصد آرا برنده نبرد با انریکه ریکلمه شد و باز هم به مدت چهار سال ریاست باشگاه رئال مادرید رو در دست گرفت.
‼️
رونمایی‌از ژوزه‌مورینیو،دنزل دامفریس، کوناته، گواردیول، ریکاردوکلافیوری،برناردو سیلوا و مایکل اولیسه؛ برنامه پرز در…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/22964" target="_blank">📅 23:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22963">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇱
🚨
شمال اسرائیل آژیر ها روشن شد دوباره  موشک ها از تبریز و کرمانشاه ارسال شد</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22963" target="_blank">📅 23:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22962">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxKUUOK0veXjaU-URZBCmCN2qsl-Kkqt25FbjtZE1hoB-GLVXSDpUgV1zfLTJeUpsCePXtUVxQLwgzo8MrYfdADaxlQdiQicY6AYakBTHuLVcnQF8Sk5BbzRZF3ZemhfswGnuubucQnG3A3FB84w2k3SHiYzc47PKgAue89TgGYU8isMGqgQUpT4ZiVugZ6wZSawgVFF8RKPR5rmrcZMgHUzHrYBH1z7J7nRgyydN1ZSCLm4RWjzQkxRP5DlWou9MTXJUhXku1lb9HVHrS2dlSycRfGEGXRw32w4-k3TGz5IOzso4HEf375nIg31Ls4IhgmKqtALOqkZj5fjMurirQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اتحادیه‌فوتبال دانمارک رسما اعلام کرد کریستین اریکسن هوشیاره و تحت شرایط خوبی قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/22962" target="_blank">📅 22:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22961">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmMPa18yyZ3Uq1itibpjHMiIt48VcFZbB9LYD0dvcAltfE1RWERzoqCmHRsbqV_90hxJBsSIJ6MUbI1rtEN2X6U9sa-DQLxctjv4PCF9KpsAFFoDtbta3ZrRCwKR_Sq2XSFD6siVF8X3uNAhdEVS11x9u9QgQa9W2S87EwN9b5CRDTGZmuIr46YvCr5oXyzajJoZX9_6i_5yxun7xZ1s2qqgm_0cuz3gIDvtMnCjOhCWQC16EdmI94mlTsxozTztXOBnfvDEHmoIifa-WDhANGSvbQKb38f6ok5-eer2Rw9sjtJH9O2oXgENRXOc8J6KNaZ4OKOZYM5c-9MWf8a1EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22961" target="_blank">📅 22:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22960">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW5xHiADNCzQQJZvMe8Ie2Ffbs12QZ2h3qkfxjgshjIFejvJrJCCag1QHqNWgG4iTm92T9QgHwc2XULigigZFQQwmSTvVpuviyIyvs98RSm3e3kT8cPiWFa6_kyNvX1efZ0SVBgqNm34UAE8xUEIrU0SXxnBryHEHpeVrbUflyo68I_XzqV_ClA3IhiKfucmQKKymajexekBXYekGQbf-YFcUWrJkHq41gESQQkf_5g1_V5N4OY2UmylrDPcpD4ouK5l6MSNm3FSqTZiQzpRMDnc8lTWhM-2uakNqqJdqme-J2HER0D4yvcdxLnCDxXuJFEc3KXNdwiYEFI9mufRQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری
؛ شنیده‌میشود محمد عباس زاده مهاجم سابق پرسپولیس، فولاد، نساجی و تراکتور به دلیل مشکل قلبی از دنیای فوتبال خداحافظی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22960" target="_blank">📅 22:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22959">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j32RGU7pAzFhewz1alEYdHiSJqRPqPZ-ihV6kSMrwWszcENa-P3xEfQHcj4i7opAHwwa0iefQmAG-r1IY3IjRUY4dMXsLA053OEUlR3ZeL69RctcZnSwJx0lCpAtQtxl_V8B32D1KWIK8MdAQ60hZn-pP32eyTQKYWlO06J1BRMsdilQO38l5Lcw0M6EwdQL0ncjS1n87HMyCo0Mzc27HaOorjes0Qj4vWQeIpsTo9cjWmmTLkz_PtvQlOQ6hPBkc5_weM2ZsLHOkFMrDs1F5QWARCdLvO9ZLuUrbMU9PswtXk_zU1SFiN2SBcU2j4GFCxG-yuWEZHcpFK6p7RI6TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22959" target="_blank">📅 22:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22958">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=pPPyzydwm8yWNg2uhDNL0xR9xgFgrqc8NEXNccridLAPP7AU9-9-OlfAJKwcYiO7whEnLxf1fFmcHIkb2g0L8DHTiZx5h9rD9IUZJCUBiD9eaDv48VT2U8-fydINkh3RwOXLYWyavTaLnM2ettwdvHPcK7gAnM1qWEdtjrtBLtsS08-9ln2Qe11mqEeJVlTjHZ73GbGkysEq962Z2IDPdcTjIk9BnutZNxe-XfRHZjRnlXW21JXj0nRYtRo6MDvB47qRllc0PsOuXFdUEUk67DD5QWttvzTcu794Eko0i6vLW_BpWdrA1NBatCyYu7t7tdk1OepF8XADiaARh2QCIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bffa01c1d.mp4?token=pPPyzydwm8yWNg2uhDNL0xR9xgFgrqc8NEXNccridLAPP7AU9-9-OlfAJKwcYiO7whEnLxf1fFmcHIkb2g0L8DHTiZx5h9rD9IUZJCUBiD9eaDv48VT2U8-fydINkh3RwOXLYWyavTaLnM2ettwdvHPcK7gAnM1qWEdtjrtBLtsS08-9ln2Qe11mqEeJVlTjHZ73GbGkysEq962Z2IDPdcTjIk9BnutZNxe-XfRHZjRnlXW21JXj0nRYtRo6MDvB47qRllc0PsOuXFdUEUk67DD5QWttvzTcu794Eko0i6vLW_BpWdrA1NBatCyYu7t7tdk1OepF8XADiaARh2QCIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22958" target="_blank">📅 22:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22957">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WCWZL-LZxPjDR8F6sWHB0JeT58_XTjZjOBQrmbhPjKelpYUdq-mr0vhHUUkosUoCGogfq3VGAHY7rkdvvTEyJAofo_ZeK4U6UqmwYCCjC1qvutakJNmBTsQeVj8v1Bt_cCvdu1Ztc0dy0K2sBuYlpvffDTd1tasE3WLPPpL46j01f6GXAsDyo86iW14Ce0j97ibpirJvbDIM7jMN-AVkNfOtRuhD69lVgxEHEO1ozG3ya3UojDtyoW0W01m10TQVN4otz9j5wHojT6kvCSDf3WgmjOMn_8y4IIAvmOVmETuN9Uibf_Xy7BMepvBp8mHIUo7PsTr3tn5VmZEcKHckVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ به‌احتمال فراوان آنتونیو آدان راهی لیگ امارات خواهدشد. او دو آفر از باشگاه‌ های اماراتی‌دریافت‌کرده.همانطور در روزهای‌قبل خبر دادیم جدایی آدان از استقلال قطعی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22957" target="_blank">📅 21:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22956">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=NY8MsVSBv8g6Ru7Gav_QV9SPmDBEdffJ-vi8PhyXFOnpselKd93vft99sDaKXgJPeyECOxWJcKmSXl-mq7hgm-d6I6tunxrnKKxTPW_FNs3AqfVizG2r6AHoZdKxMKFIU7NA9uUd1XaNBKC5FjxAqJhs3v4usdgkuAFIK7L0mqgOGOdYJQwnpdUyBCO_llL3szy7E8j2HGX1iB7Vi4k6MwYBfDKYiwmEb_qi9A7XwiK-l1FPO4hkiQql1C8SVNddZGJq_3PIA65sLj85qrLlhK16YaPOHjYiEMl0jQsamApqxO75DMhfwE_C6u8uhSZYoNj7QwdXE3Om6Sw5yxRv2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1b174faf.mp4?token=NY8MsVSBv8g6Ru7Gav_QV9SPmDBEdffJ-vi8PhyXFOnpselKd93vft99sDaKXgJPeyECOxWJcKmSXl-mq7hgm-d6I6tunxrnKKxTPW_FNs3AqfVizG2r6AHoZdKxMKFIU7NA9uUd1XaNBKC5FjxAqJhs3v4usdgkuAFIK7L0mqgOGOdYJQwnpdUyBCO_llL3szy7E8j2HGX1iB7Vi4k6MwYBfDKYiwmEb_qi9A7XwiK-l1FPO4hkiQql1C8SVNddZGJq_3PIA65sLj85qrLlhK16YaPOHjYiEMl0jQsamApqxO75DMhfwE_C6u8uhSZYoNj7QwdXE3Om6Sw5yxRv2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#فوری
؛ کاپیتان‌دانمارکی‌ها بازهم سکته کرد؟!
‼️
دردقیقه64بازی‌دوستانه‌امشب‌دانمارک-اوکراین؛ کریستین اریکسن کاپیتان دانمارکی ها همچون یورو 2020 دوباره بیهوش شد و بازی نیمع تموم به پایام رسید؛ امیدواریم اتفاق حادی رخ نداده باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/22956" target="_blank">📅 21:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22955">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-GJg8IJaaZDWavB2kObT3iojTopHIfQbBwry0Cx56pKoyqgegvK9t3URmq3UDvmnJ8af5ZvOSiAoOborqAFQuBre6beWjW6sfccDqbgkHorZjlJF8ZZ6cu__XmIGU13DKK0nWjUhydxFdfla1yp93-NemjtWX_vrFBemK16PLax78VAo7k47c1YcvjM6_boGCOhOUXkbe1Cagjg56SuSXBmMK_jEV1ky-a7SwVd3Uq6WZJLtxiKBxiAike6spiBecuASqGPPsIXpaj7HCqtc8ezBMcYdf6mNSX9AWbvnXXA4I3xRKSiElyOXnyUGoPZd6onghfZUHOCcrHukFgwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ کادناسر: بعیده که‌سرانPSG ویتینیا یا ژائو نوس رو با رقم 150 میلیون یورو بفروشند. برای هرکدوم از این دو نفر حداقل 200M€ میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22955" target="_blank">📅 21:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22953">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDxXFEBbpeVfGP--ZwyZ65s3CVyypGx2F0Rzp0cs-Tsa22Bk0vmoKdPQBMxvKDrIE4mrgKb8ypQGI9etiyh41coQmlUtYHO-O-yksHdVAQeGqA9xJyQ_HQfdGHv3d8jujlh1pS3VEO04ROfEAEYWK4Ywfyu0VAYIfofj6xq5z_KX9q35K2Z3p9dbfqbgORWxtN0_dznNaduEdX5tuBz0YPJMEcTdn0svjZXyaOIbqE-Kd3PQ9xEhuA165XKyAdZGF5wzg1jXVcuo1YFBy2GaBvem6U4dWQryOJmsp8itv14pXfISIiDoBeV8NWupT76GMAxE5fhgYnB6O7mHEdTNIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gNlIWDAMawI8c-F3q0sHw3y64e35YIDgTy4DrHzuYCiZKW27JNJ0PTwYzox12QCvUMgHzMbzmNSEDxe9yPZC16kIkrH3yaQ3f7l6ZZybr54Eh231B6z3IPtm-BXRrUl7MxgjwDLn4qui0Gzs8vLdGmbnUJ6yDX-K0GVhfTxdsdEMNfuJEy9n2iBaCtoQgvmfX27hjdpi5XmncCvMGDBgYdImbsgpiw-oPJ2rFdiif5jvJzTvPeeJcpr4co6RknNnrcjRSROKvU35RCy6KEkHeF4cc-oFzU8jgeDtrug4I2P_BNIY4gJk_ZAzvMw_dPaoU5e21qDcUN81KtuRiDmxCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22953" target="_blank">📅 21:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22952">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-aa02eBvqq28SPB36dYSmj8JZGpoNjsJYM7wLq-py0dUgm5sRHFjoSHBfW3ScrYziKJwSslblAyrfYvmK8-Wv8WZ6LQVhap8-5pnCkQBspBRxHgfxLviVf60TZgFU5lyZR5HBr9FCpNqmdYLPqYyWB_43poyQJlS1GxqAR8ok5XZqMah49D8h8POl4OmNwyiM0CFT3Xu7pHegH3G1A5kr5sJnvPBryOD5TehTiinusex6RMfsOO88gicBJMkSCcNxQ9KqRZY63cGS8YTml9IePaEKInEgMY1s3PCJvqGUtzeZ4py6m5JbTdrC_9v6OrcAcLYTuzThFw3Pe2FJFrAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
حواشی‌ دیدارآینده ایران
🆚
مصر در رقابت‌ های جام جهانی 2026 از نگاه هوش مصنوعی ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22952" target="_blank">📅 21:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22951">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=vjDBSYmEz7LiEP1hUlZhHJC0P4yfojf4dO9K_USq46sg6P0wNpVXVrVb4kB0w4c1MaEOXplQKK4XtS4VMQNCFIldZv8JV95jGVK4Qt5eLC8cIvjlutNraqlPUfUHm7Bf0HcCAYtPJ5okIsFIQg3EzgrN5Vm46drdeBriropnKhejPpULjnfNOyAZPMmM14o9u6DtyieitSXhu7GZ1ar6sBLwElsQfWj4TkRRIgO4-t3MErIjJ56RDJdhA0d0n2HS7dYTYLT4gL3fz_3UdbvNqh-uxgY4Ag9wie97K8H3Z9Vg3xGkhAilvG_feNl9CjuO3wSdWwE3LiT1whc6KXUWvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c25ae3aa7.mp4?token=vjDBSYmEz7LiEP1hUlZhHJC0P4yfojf4dO9K_USq46sg6P0wNpVXVrVb4kB0w4c1MaEOXplQKK4XtS4VMQNCFIldZv8JV95jGVK4Qt5eLC8cIvjlutNraqlPUfUHm7Bf0HcCAYtPJ5okIsFIQg3EzgrN5Vm46drdeBriropnKhejPpULjnfNOyAZPMmM14o9u6DtyieitSXhu7GZ1ar6sBLwElsQfWj4TkRRIgO4-t3MErIjJ56RDJdhA0d0n2HS7dYTYLT4gL3fz_3UdbvNqh-uxgY4Ag9wie97K8H3Z9Vg3xGkhAilvG_feNl9CjuO3wSdWwE3LiT1whc6KXUWvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تیکه‌های سنگین ابوطالب حسینی به تاج رئیس فدراسیون فوتبال درباره عدم صادر شدن ویزاش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/22951" target="_blank">📅 20:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22950">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_r2omQk9nt7Zps8EMMLifoiGAmIoUVnYyoVPuy8yJ6eW2V2XZTTIpHr-4TlbAryRqmZ4I2y_Aj4scHq7ZxYzoqVHgmjLOXi0DR39BCd2wxdF5MIaw8xiB_8dVCsmo6_hjiLLRcll-ppWp4KxEwsJ1k6x3LpReBuRFj0mY_vF89EZY2FGud6lBplKdElDum1gvTZfs3xhP7fd1_9UwHSTh1a_nT7QVfp66JBbtqLcsFYk1sQ50uJktfavONRHjqDrBbc95y4HL86qAzv22XwyntoGMopiy6BhauP4xBCvg1Q2UN3JUF4eNv7OGrfWpEZpwTaV7bCn_qb6_c47QcuEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/22950" target="_blank">📅 20:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22949">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNqMziCv3v7dKNR9Rlq0zLxoASKMR7wUPTzc6gUHFKiSiS-nTBB2dwvG-vKvy133OZQuYCpwX1F3z2c00bzo4D5Ee3PRx1FvQKoavQP-pf7PTZ-iI7xMyRfONVJa6ehAK-ojIqpdaNRnig4wAoY6XbaK2QIz3e9YPosaThF_cRrieggFVkfy_nWlCsQb_am5ho6q1hy0U54vc4XIcu3Rftf8JEoX_GvRW2dKSR5wSCVIghG8s7AiKQ7bcHxgJjvtG6q7dELy-j8voDl1P9fe2lglEiOycGyWkbglVZDLWQCqPozpdlgsP96YvQyvFnyWk2_Msk52ui0J4POInQanqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه کریس رونالدو در جام جهانی 2026 موفق به گلزنی شود؛ به مسن ترین بازیکن تاریخ این رقابت ها تبدیل خواهد شد که گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22949" target="_blank">📅 19:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22948">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL8PzbXjWNhxaG9ojosFD_dHAvwFc95VqFuR-oZllT061v-mgsUXLDXLRm_QU28guRfBdTrGsthqiRgO3DdHzmwOIZHRp1qOdgS_6AleOkhQBpNAIYOqsQkGAQuVZmjT3gn-Qis7qQUqqYbzCe5q9G6oONldHWTkQQ4zU2drl9AlsndaHNqYklqFUXbBqFbzJ0FZ1KXIzMVr32lFjXWEMvREPlR1odC9OgpVbBb8hOWBEY7Iq4Xk444C4CpMxqVRTWk_TeIf1YUwGfoRqln9qxjk0Apxnt0yLHSxAGKKMTJ90mT0gJwEuCUPz4nGPbOFIRc1pdh2_DXv9EdDK8XDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22948" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22947">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=bwDwM3hh54NsAIpwkleiHjar4hFF9hWJqHUL03-apWvExh29eDY6QacCO-kVaGq3xzHqY0Vh6kYVXYPfQZHPSVicNLCH_yailZUUDBpbeoJ7Ya0kcKDIMtE-mexvZHoyj0V0zIaEuUvcU0EopL3KAljXxdgsgi3ht64tpitBCftaBFgtXLpFl6d3VUFTamK4ymWfmSqS4KMiYTrZsXk4cnT6loyRvlfsOUj9Sftk4guYeGcmJKQjheH_kgVn6q4SQwI_T3_E6JUif9Qd-iSn4nX6JIbDMN1_w8NlIKJuWThGyNFsXHbGns0a9CLD3WtCF1mSPUS5z7-8ekqhb7KmYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c78767e61.mp4?token=bwDwM3hh54NsAIpwkleiHjar4hFF9hWJqHUL03-apWvExh29eDY6QacCO-kVaGq3xzHqY0Vh6kYVXYPfQZHPSVicNLCH_yailZUUDBpbeoJ7Ya0kcKDIMtE-mexvZHoyj0V0zIaEuUvcU0EopL3KAljXxdgsgi3ht64tpitBCftaBFgtXLpFl6d3VUFTamK4ymWfmSqS4KMiYTrZsXk4cnT6loyRvlfsOUj9Sftk4guYeGcmJKQjheH_kgVn6q4SQwI_T3_E6JUif9Qd-iSn4nX6JIbDMN1_w8NlIKJuWThGyNFsXHbGns0a9CLD3WtCF1mSPUS5z7-8ekqhb7KmYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
آقای‌ممفیس‌دپای‌هستن مهاجم هلندی اسبق بارسا منچستر و اتلتیکو که داخل و بیرون زمین می‌نوازد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22947" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22946">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGtZjUhjwVhprs9mLvXiZFuVL-SM6DtmiLv8EEVWfFrUsp0LjydGLuZ_bycBxoRHdPMTnjwOBuKS4Z3aJHxDcRlMqoVhz1lw5Pqc45oGo_FbhpoZ8fQ8SSXL3p-nDTVJh1yDeYFeideWwIsVjlQJ9D5j2aeZKtZICYrm-d0o6vGuOYt55OHZVGTkZk5DLDEV3SOq842L6n2w1OVvqbiiVtSSHaaykgUKzkAzCH7-a-VhK3f9wt4QkHMuvLuii5eLvYAPy1gtX1ipUYfzcyButATFsU1R2tNuyX4adUeUMOf-Gssu4nV1pa1QGF-W_RTfO8bTZrd2QjHjGk1VCCnTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
با ارز دیجیتال حسابت رو شارژ کن
🅰️
🅰️
🅰️
شارژ اضافی بگیر
✅
🎁
20% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
همراه با درگاه‌
#ریالی
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
16
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22946" target="_blank">📅 19:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22945">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EOHu94p3VnCpLZpn5bmKABCFemKL5zLYDr0VuO01t4fQfVT1wANAiDhCrrZoDlOoIJB3xrtsuJ8lgws7v69o-57AynhPDsgIkhLJ0hE-Qf7cil_D4QkxjdPlVF3XnB23BbpVRLM1R0RXLxLAlKOz00OECM8DaQjxoC1MSeDJmKunYIJr5y2MBORmIv8TMb4u0kG5VAX1tFvgtIjpDqxnYD0cn1SgjLWXNK1nZUrVqhO8im8Nvf0ym9cNmp1aqAoUDwEYz2eWXS7r8skxL6z0isEPuj_e7Oxg4dnQXUclaR3I2WIcoV8t91XC-uhxvyMRKvd4CWkSagkIQ4gmHyWlNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22945" target="_blank">📅 18:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22944">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZePzDdby3EhFWEOxF2K5f7TeI4XBeEFlN24sQW9iMawxPT2tchFxBMs4gik9YaNjNgED9XnOaBeTGQrrvaLyXTp9vyOhKUKN_fRlemHHI6CX9KDBfmv2y3fZlcJy1uRL29k-MHfe90UCnnwvjqb94HHpXwn8VFyHLyPn0MhwBFPwoKvpM2oZqvnTjQdTwQWAMyBFr6MzeRa5V8KyW7GD721dxk-NIhA5UYFkeNgAgtmeWaDfSjDttdffkPHlszGfYNGeEcVRHGb0De1lNq2oVBqsY2wQkdCeBPQoIWPNWwAw5Ocb_jIHANse7JHJOl1ZPxoL1kScx2xcBG-EYoijA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: منتظرحمله‌این هفته فلورنتینو پرز برای نهایی کردن قرار داد مایکل اولیسه از بایرن مونیخ باشید. پرز قصد داره به هر قیمتی که شده فوق‌ستاره‌فرانسوی باواریایی‌ها رو جذب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22944" target="_blank">📅 18:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22943">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHly0IILeiePF_qCHBD4SRbb9Rm3urhHobK0ors47cB9I8QQvBepAliO5wsyqpdUFzNFhltqt32zv1QIgBgV_yKtTpQQ1NwCgTJhOMnDyaqiXGu9X_TkqTpTflW5YhfVvnQzRVWhorzEnwfhMX4MgUnyJ2VLeZg6QX7dZMadjSiU2kR0lpm5zPJQRoRrcJ5ldkuxTOOYKm0lPEpw6KVmykMlI6l9ljLmolS-5l1SifyNnv95zp8KQOD9H9PPWnFgtXJL_eJvZgI2mMagS0bbeAFr79NL5pzjoTE0npFC3GiiciTRK2-VRLH8qeyvqefG25hTwehdCDKPQky0bp4aQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ انریکه ریکلمه از پس پرز برنیامد؛ فلورنتینو پرز بااختلاف‌آرای بعنوان رئیس‌باشگاه رئال مادرید به مدت چهار سال دیگر رسما انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22943" target="_blank">📅 18:07 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22942">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=JzCtCzm5pnRSCA6oXrS7_6RDq3VLltj0SHCrRMysAfzgseDfsBw2L2sW7nc2DpNE8Yyy5mhGDfuZpdMv2DmowMqDYrQQJ3fP_BkwWsI6Aiqv82YQ7Bs9AsS8M9n4f7TRKMr24M-RP46IpPpEvcctE3sCDnye_NEWsnAxdLS-iC6wOxIxVuGmxQ5k176YkOIuxr3hFVwOuUS9M6_E8Ght6o6eMwZBTQR5lQ8cbmTM_6VIb33VRvOINCqANe5e3WOKnM8txdrIRcQP0G8Uv3RcobHpaVHb17cGMTV_eEEt7pG4P0dvLD8T5pozMAJGhWOMduCYuRfETZmwjJnS-eMC1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ebed3078.mp4?token=JzCtCzm5pnRSCA6oXrS7_6RDq3VLltj0SHCrRMysAfzgseDfsBw2L2sW7nc2DpNE8Yyy5mhGDfuZpdMv2DmowMqDYrQQJ3fP_BkwWsI6Aiqv82YQ7Bs9AsS8M9n4f7TRKMr24M-RP46IpPpEvcctE3sCDnye_NEWsnAxdLS-iC6wOxIxVuGmxQ5k176YkOIuxr3hFVwOuUS9M6_E8Ght6o6eMwZBTQR5lQ8cbmTM_6VIb33VRvOINCqANe5e3WOKnM8txdrIRcQP0G8Uv3RcobHpaVHb17cGMTV_eEEt7pG4P0dvLD8T5pozMAJGhWOMduCYuRfETZmwjJnS-eMC1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی‌از مسابقه‌کاراته‌معلولین؛ این چه حرکتی بود تو زدی آخه؟ چرا از روی‌ویلچره انداختیش پایین؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/22942" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22941">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZv-sS8p5RLfqxKHAPLiqDbKtHFPpivdluL0Bs_3EhTpCNE9vbWp0i0GKftjJPLlwkYO4dw8jIlK-SBDdn7hLpd82VDllKwoz46U6U_n-QH_CMQteTplxC4VG4B4bynCBo6Vp0o7-HX_0yvngItcI1rpzxKlLFB2Ff8xT4Wesj6n5ou_7T9K9Hna9--Uxh0KoP4IfkiQrUpeK3JsI8kKDGODDfbDzo77JT9KDX-5r6M0b38zf8vFZdKAKoelJARoGj1QkrN9VZmliNHrncX5aCSG6He6zSCfYwErMMO-M5CavC1RCt0Eka0S9KNsCK1uYqIGEmWC7Yl9qZ7_WeNYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/22941" target="_blank">📅 17:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22940">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzkX9afF1JyUjP2XblqhnlzKxxp9MMvVj6JCXbqln0RJ-yAuOsgERa44Gmt5_3GOnVzu1Ibxh45nChvzLR_JkDFearF4A5QRlYCQIHYedNSl_IJ3THg1RCwQayo5JL9YeW0FjLdxI7RswAxB2bzY_GYJ_3riLmDUKjp6Xvf0KoHfRwe_CQOSO7sY2Mc11s1EUUN0IyeRac_DwHOt8kWdyxv28qArW1-9Uz2jFZBjVP5DnZlG5QEYfmn5DtYwyK6_4sFTlX7U8d0ZkcAm4YEJ09lF7UXdazMYN5-OHzs6r90L2-_NeZYmoBmsw8cc7IpLUcoBEexaz4TqoFhmnQRE7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ مدیریت باشگاه استقلال به دراگان اسکوچیچ پیشنهادداده‌که تنها دستیاری ایرانی‌اش در فصل آینده سهراب بختیاری‌زاده باشد که درصورتیکه جنگ پیش آمد و اسکوچیچ مجبور به ترک ایران شد بختیاری زاده سکان هدایت تیم رو بر عهده بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/22940" target="_blank">📅 17:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22939">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJpOnoB_70ioQ34EcOzw6XXvOhoGCoG_7ZOe4YmWioh4jMWADJV7jNdvMikhCNsxgXsaYMPayCiqrB7UiIIl4RVV01mPyVUHjAP7zi_lzPtopQPVqq7teAoiIXUw_totezaVqImcUKj-7ARgtTGE5sGfkWLCqpEtdyrU1Xi_qmy937ywJe9FB6CpQFjGk-_QUvlBkBMjSDcc8OvlTxDBd5YuJeQQadWEh3nKcJm5G9tSykuu6fW64N-e3xBLPt5tFQ3gMsOzc1TAulABdh578DNwNILlhab5n6BnSvXHIxa24-1PUzPOaXG6OSJAxEobRM5U_RHGQbEImacCjRjoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌ های رسانه پرشیانا؛ باشگاه پرسپولیس در تلاشه که مجوز فعالیت افشین پیروانی در لیگ برتر رو از نهادهای ذیربط بگیره و در فصل جدید رقابت‌ها به نیمکت سرخپوشان برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22939" target="_blank">📅 17:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22938">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdENyqfdSRvm9qHp58J-4VagcuRVxj-BwIMSEPtFeD-HxXtyMblva-cWFG_hcSNc4aWrR4x4o10Oy2xfQPAVOT0bAB08FYIXGHsVuBsCwl-EbPurxVFrLasFjnjkxjEiZ_DPx8GDBhB09LwRZ0keQ_wGrgeNl6N9tc5lKwUKj3b0vSfmy3CKl7Y1Bl0nKMh-bdheDdHF156jhoGfQKf1i5eqPWPTcn9hcq2HHJoZ221mml1NtqtP614TPWmVIX7H5AaJ_Ms86tp4hbX4mj0gtQ2FmUM0X4d8tiN6-T06L0P15bFjX7rHAg-9uWkQaQ3hZz8AdBqLw1VQekDH8tEfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22938" target="_blank">📅 17:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22937">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7buQpaLnH069WTdS3o1OPcm5mGVwoiAGfghO_qN5VQxcJUMIekf-gb1eunHBOhT9E49vJS3UiwuaWCyif5CmDLiaDCgGqWDNTn7iL6srnX1nPVMn238Zze9y98AwxcZJgxd20b4zEPPjqVT-CdP5zhRwUsnsqaQLm6RVBC9pnKAdhlgpu3QDxGkEMwKS0fZN7bIP46xCJerw_YIMX0avNlVmW_7rSYkE_CtB0EVHukOO_2xGwiNOKPvpYTwMCVacTTQWwfskQgIEuH-uk2NipmfFbbn1FWFJoWMaZq0jHBZHMhClOElvWT3jkYt3EclbluY2MjvUeRZ-34RgtXr9u9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca0d90aad.mp4?token=q_9e8d6dLF-tYBAGP9xMgFy8aIjdhF-yB-1cZEOgpFq_q6FOMzoC04Vh8FrIWEQlfwPoPhw2dw6J_koPVXmVhIOxv7HhPpU4e6SjMY8hylIW2umJrYEPvbFyoXOJ8PRtA0e71jbgW4E8rFfOyD-Lg9c6Fukmoj4e96X9sMlRyqcwW4ZxH8TUDEBN7QG11k7FrWeP0hLrQ3FZdjIDT-FhbfqgJhw6M45LcD2S3b5KX8uWZUH_ZKutq3xXsT44Kg61zpGfpfJegOLtznhxhk1IgDU3ypeDDK0m_MQ1W4kHmihH5-8TwKhKEkBGUVAiwn5q6eF1q6L6qpT1ELGYZ60a7buQpaLnH069WTdS3o1OPcm5mGVwoiAGfghO_qN5VQxcJUMIekf-gb1eunHBOhT9E49vJS3UiwuaWCyif5CmDLiaDCgGqWDNTn7iL6srnX1nPVMn238Zze9y98AwxcZJgxd20b4zEPPjqVT-CdP5zhRwUsnsqaQLm6RVBC9pnKAdhlgpu3QDxGkEMwKS0fZN7bIP46xCJerw_YIMX0avNlVmW_7rSYkE_CtB0EVHukOO_2xGwiNOKPvpYTwMCVacTTQWwfskQgIEuH-uk2NipmfFbbn1FWFJoWMaZq0jHBZHMhClOElvWT3jkYt3EclbluY2MjvUeRZ-34RgtXr9u9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اجرا چالش فوق العاده سخت ورزشکار روسی توسط یک ورزشکار ایرانی با رکورد زنی روسی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22937" target="_blank">📅 16:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22936">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlK-JJOibS8Tvuvu_-oI8O-K7KXS_kDE_8y68f87mIZFIZg4xtVMKbYiVS_K1cp4EXqsu96hfLFltzJACkKyQfdWFQK0MZwxTYfrdwvWYIG9P0PysaoIBu7ar-M2W6h9lBMvytWDXu2tqcMHNmCkUgq7eQ-CamX0lCp0fzesiVYI3stL6SFgdI28uQlkgHpw61WryBe_suGymVJsOHk8Bowdf_4oySNguSz22zCi6F-fAz1ASA8zuDmkC-Q608iSd8SLPiooFqld__kORN_jAOqFKCp4qsTdSlA_D4bD-zyDwi6w_91PmNJYtID_yd6nXrQo5SEru1G7bUfGnWmAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22936" target="_blank">📅 16:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22935">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lax9yhjKNL9vJ_rldEiGHvr5zW8Gq9qoZTiGGwjt0-BqE9KGiVEQIvh5wMpkvYPmjI77wipqWd5lCKHUh9fJsxhpEVfbV9uGgQWU24WmpqF0udAaHM7_NDRNZBQrNAWxXdzRHWWPDnXsycTjhJCMiskVQZ6vq2gwnSRVImDb1DX1GIWTfCWh4moLC7beDzlben6Y4hmakti5qd8yigLXiBKsILU_CHvHjI3oGkapZU-ISbsSDj_dfYUwCA9jE1pCApkwWTV_F3PDOqZMPKqAGzjaDavK3jeO7yjlYzxpHG9DbhiTLx6GDPuJ3k7IlFk8MBWhEtaRTvW1ymSGCaB54g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌انتقالات|گستون‌ایدول‌ خبرنگار آرژانتینی: با جرأت بگم که آلوارز درنهایت از اتلتیکومادرید جدا میشه. مقصد بعدی آلوارز صدرصدر بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22935" target="_blank">📅 16:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22934">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qClkkkWMtIv_eIaxS2xQxedLAAjV86XzqjnMoR6OKAGraSH3lWnKONnyhvKwyogX76v_O8RSH5sJXXlLp8yEIyAqIkmnWj9qY0pvn4GrjqYChe91frydvpsG-zGejuPL14cfx59vhCGs3zeHojdQ3Lu0KCSIEdrVOZsxDrkBh1rAoDxVNz2VcP_ZoG67rijfeOOD_dWVd522evY43DV2Id0jEICClBw1_Hc95tjkKSN4ZO1-TcGSNSYiOujhc-eMThPoQdeadXs0vBNlEfkigfxOW132q09umyJ5PHANzs604Y7q5QTTwfRqmQJqG6BbuNLoWbtCRXskx_OFG4ziXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
تا این لحظه فلورنتینو پرز در شمارش آرا از انریکه ریکلمه جلوتره و به احتمال زیاد امشب او بار دیگر بمدت 4 سال رئیس‌باشگاه رئال مادرید خواهد شد و از مورینیو،کوناته و دامفریس رونمایی خواهد کرد و سپس روز سه شنبه آفر 150 میلیون یورویی خود را برای جذب مایکل اولیسه…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22934" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22933">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=OgYb99Z25-qdsLRAcgGiXEqQJZQO3rYWPWImCHQJvI47MfTrPqyBeMviJ9vVeNbgQGo5jL40JJJX31znSyTOrMxwWWNOXWD3ejq1CfqFKYtEs22dOE_Z2dVg1LQiPyVnDLT3eIBl6sHoRzQarwBlvz0AysrCAAE0IBE867dfVXaL4JKXZHfO6D3qPynm76u1v4zVv4GInCKKA2qTsc9OsasXSBi00aObeI-MCNUf9dhhENw1LcBVEQNqUEvPJGw-r3IGMOQHhx_vsw0i59_iiRT3RDUkxen61vO2XYwBaRidpDk7rOndzlXHPiArvfOhrO5PQAHwAF6LP3sV6noyYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139c25f87f.mp4?token=OgYb99Z25-qdsLRAcgGiXEqQJZQO3rYWPWImCHQJvI47MfTrPqyBeMviJ9vVeNbgQGo5jL40JJJX31znSyTOrMxwWWNOXWD3ejq1CfqFKYtEs22dOE_Z2dVg1LQiPyVnDLT3eIBl6sHoRzQarwBlvz0AysrCAAE0IBE867dfVXaL4JKXZHfO6D3qPynm76u1v4zVv4GInCKKA2qTsc9OsasXSBi00aObeI-MCNUf9dhhENw1LcBVEQNqUEvPJGw-r3IGMOQHhx_vsw0i59_iiRT3RDUkxen61vO2XYwBaRidpDk7rOndzlXHPiArvfOhrO5PQAHwAF6LP3sV6noyYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آدریانا اولیوارس مدل مکزیکیم رو بدنش عکس تک تک بازیکنای جام‌جهانی رو چسبوند و از دخترای مکزیکی دیگم خواست این چالشو انجام بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22933" target="_blank">📅 15:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22932">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrPpdj9zXO3Pyiab7JzFgEsIWoPwxt-eEV6Kq6tjEcllRTosmk1WyHNkBRVhbLW1a6zms7FeFieQzelSc9Wg0sc37IY_ZPjNDRYRVhGkKsgRI73b1UdUPxHSFQ5Cirnc3kmWiNLs1Lki2IeTTtQhew9y4fM0_c3-jUOcuLQ73Sx0l48SDDZzoRmM2tdJ_JdbfoZfLtPezIOceQI4mMka9RoDiXI15kHcwW4ws-1lHSZqBYyTUYQ86aTjEzFEqqM95u3NjeKScG9PiOZLELquwZIoJoGzgKkq7zXNMPR-oX4tAZKqweFOPqHrvkNEztjh29w5aqvfGK4eIT9HHH14Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
انتخابات‌ریاست‌باشگاه رئال‌مادرید از دقایقی قبل شروع شده و تاپایان امشب هم مشخص خواهد شد ریاست کهکشانی‌ها به کی خواهد رسید. شانس فلورنتینو پرز بسیار بیشتر از انریکه خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22932" target="_blank">📅 15:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22931">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSS-q9Skojro3sKbzm8NpT5nNycVcR9O0RzhQ_sr3lxnYzxrc14IS8EjE5sfkgufyUu_y5d33eEv2y96ZtMCMHn07xiAh_OHybCsQsxMfhvLjnhfbMIDXHSabX7UW1Kl_2kM59WqSfQnxCRZSJa8fiTmfxxbZ37JX8EypAzijskIx6kJ9KszzcGnmJJWnI71CEtZG9C4YzShLI3tLDQMdIUiM6ZPYLX2S-j28v8VA3KaOzDe3Yr8kZTKZjnlwlabq5HhrKc2tO5zIFQ5fqTt91E0X-nHELYWBF17h7VH43ztlTPO2VhZwpT3n5IWThfEs9GY3vR-lscrQgqmJfh8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال خطاب به‌تیم‌های خارجی که خواهان به‌خدمت‌گرفتن امیر محمد رزاقی نیا هافبک 19 ساله این باشگاه هستند: 3 میلیون یورو پرداخت کنید رضایت نامه این بازیکن رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22931" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22930">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol7klxO_uAnxiExOO552r5GjzR2HrM9mXEHvFsvn-iSy5ExX4-wZqfsLfj7R7oExEdlhQeagYtNBXz9p3-v1e85_GJxj9GK0KtfdSKoHrsGnuo6ALQXp8VX45zA5Om31DFILqzvzeXBmORrcGSPAHCeoOHHblY-PRrYLkRFolOBGLvDwJDOJglMvS-eMCp3Tj4547x5l0-488nVzRs8Z8nim6_QezMChwtPF01Do3GZYOmtqLBkvMYPBGqBLX5390EmPnLWRbvH7bsf12m1B6V2PFusH1c4dWBLiSE8QNUWm6RmyuO29apfmDEwi52RgmZAZ33cIbtMhuTCK394oOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22930" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22929">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSc9jOAv12wZgcWTz6AvXsUn14EskD8b3XpMwp8KT00muR3Lf9_OUtRM3nWMzFEW6USfB8FtJcTug77tmVLbFMBGeEp5jXqttOwboa1fvl5-kssk0PvnBCKiV4fD60kzHYj5GXcT-DTYNohJCXi9yhyv02MN4aefcS7QpD8HnNMxLZH85oj0HzGTlKxMZ5qdjVlDJaHjAnpqdBbEiS4yeYwZk4SokNeKR_mcETAbkp74id0hndsOoLZ_c0-Q5qodobuVRtHgR7GDN-Ybp3raDBJHzFA6vgPH5dwERVjc7vZ2ax4O93ndQK7ElYD5ifK4tOHPSYlps2zMhaaJXvEHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22929" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22927">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fq1YDIVfOjXgt2_yDpN6M-hVNnKckgY2c4cViBNErqKiXb5aRM9AjPyaiGGHJU-ME-ADEQ7OYm2jpQy1OUCGc1j7MJWliiQjnj_1fhM3IcmEPItjgmvLoisopdWOSaTISVMjFwayNhNJC_zMkFk9DtvwQu7NfalD-Wu0d9x5nL_oHjhhTdGAe7peTw1KPDKShMBsQgPwmUz07zq8GfJk63bSLkzXgP0ziPGZ7m4pTEAWhzHkNibcI_mQJ7GP72I2dqNe8vfhdSfWtFSPgr-d9HHOTX4iDWhKuhwT15MPuk-eXvrEGlcsj2hD71i9fk53ErSnZ-p-1bDQOsrkg1XJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGpnqHYCr0dQ_DyiXnVBayshFJ4LuhoXSzR_Jmq5XbtBGnpuNZS7j1bxhDoNQTlHh8KlEqVDEzEmk5eDE88VHmutflqJemHm7Zitez9Yf5WlTFz23jy8UvM32QsqgzHIJcejE0xg_ZFym2zoA8Y9-zeT3_I4KlDCURbGRzU5_8niK2P_uPNcliZ1U9-0TVsJdVuoxVYzi-ndLem9TzXeagOO_5L6VHmX-q7lTWZivqqqJ9eVAN4U1T42QaydtBmaKPWqGWL42XHYROHukcXmf0UdqSGqguyRueCUUCL4LxCh0VpUhP9TYJVjmkmKXIiDo6PkCSRjosidSPTBMa2XOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
معرفی دو تیم بلژیک و مصر برای رقابت‌های جام جهانی؛ جفت تیم‌ها حریفان تیم قلعه نویین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22927" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22926">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm1MlYfGZm78tYiJuEX7BDOdtqFIJS2XaucfgMlKPIrSsG3rrlPR0-WhQ3O0VDbfCfyTpBNKwVif6Hpp-UUGcN312jc_0MPwTRk25ZmlDCgAnwzkVuOQ5g1O2jF_RCEijtM_TJrVPV8ghrmMeNDesZpNaePVSsScFd0IIKoq7JaQHkDf1uqTd6uRmc_CbrbcSJxCwwQ9VXcqTpss2Ha7mPC3M3TdZqpB1mLRTm4HM6d369EJl8ngnIngQ8iba9U0H-ttPzsXLml_RLobKyNv7UOq6qNDZLUPzGdNX9JEcXFHkxLMPdJq9Xlg6Z-6lhRwczy9NuCS75b1QHK_ElozAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رکورد بیشترین بازی ملی برای بازیکنان حاضر در رقابت های جام جهانی؛ کریس رونالدو در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22926" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22925">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2UIxIXnY3LxqiV-8lURqicaEeLPi8N9ANW_nWjIVVTNPbvw_eq9qtPqC0qUVxIV_tWbtNktqjo2T61kzkQF5-SMMGcL5nwBZZg-7j8GbepBzAw_ceRcE9HVT-Sy2UU09Mt6JP3ozZQdECsDKC6sl2aNu2SuAcjArd_uxse9zmMEvFUWHsXfWVRzLoVpD_YmtQ0oA15J_-SkFz28B3GjLs5v8YC74clf7KbYM1KNDmOKd9vAmKwri2lIYr1n-P7RaaleJbkjIPo2ZRrqihSQhUXfu6w2m6OLCT8vUYGS0UkfERjHUXVtm4zpSR6zLAfuS-YK9hopguvgaGaB1ZlJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی‌کنیم از این ویویو بسیار قدیمی امیر تتلو درباره استقلالی و پرسپولیسی‌بودنش در زمان‌های مختلف
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22925" target="_blank">📅 12:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22924">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LP184vS_SBkBwetYLa22cHSHMRwmoQoywXhT2MOIso9vcKm_b84QuL5aD_zBU9e96rK7uAENxRQOtPKwVTfc0U9JP9XSjYM4-JmvSF9Cdz_HzeCZ3aMMITkMgBHtkvw1cthRkwPzNjJYBHzM-tR1SNceBOrc972DA6O_T5GlKkUYMGcEDOwn72pKngsrlKW4mB8uhTmmnmJ58ze-uNKSYSo_KGMIaP-brKSeAKIypMNbRH9038eJxNA_87UmoH8jdYnEvU_q4gF8vnXaUBN9oJfEqSlfjrAZdr9iw4QiihIjVAsoCGwmYfxhOw8jJKjesc7GE4FhUmVRq7vIV-N35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ هفت سال پیش در چنین روزی؛
ادن هازاد باعقدقراردادی به‌ارزش بیش از 100 میلیون یورو از چلسی به رئال مادرید پیوست. او در طول 4 فصل حضور در‌این‌تیم 76 بازی انجام داد و تنها تونست که 7 گل بثمربرسونه مابقیش مصدوم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22924" target="_blank">📅 12:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22923">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a46a056081.mp4?token=c9h6T9DV6VAR7E-7UEQBKvqM_JZfMzm-n3170wGyIaCOnaVyjYU_24ep5nJ-6WQojDS8Cucdx9PE94w4AZFx2vSO7fA0xlh7qgO6JBy5XWqV0LDFhE_yqcFq7TERBzIXsg9qf9ivgknKeDJuj0w-HseqUZuJwqDdL5N0NzwDwgUcBHNV_jh1Jrnh5_3wdjzarId4-ha0e79C8nVtQR4i-ZHiW3H-_CpDkZQC5sqehafu6shLAwbo7xCrxSqAXaFUv25jjGmlNRD7jEvNbMwNiwBluc0WP3W5tq5ZAYXI4Wl5pYokfi7iqWdkDb2L_8yLHiOM9ytHY7HSIEYw5Y8N3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a46a056081.mp4?token=c9h6T9DV6VAR7E-7UEQBKvqM_JZfMzm-n3170wGyIaCOnaVyjYU_24ep5nJ-6WQojDS8Cucdx9PE94w4AZFx2vSO7fA0xlh7qgO6JBy5XWqV0LDFhE_yqcFq7TERBzIXsg9qf9ivgknKeDJuj0w-HseqUZuJwqDdL5N0NzwDwgUcBHNV_jh1Jrnh5_3wdjzarId4-ha0e79C8nVtQR4i-ZHiW3H-_CpDkZQC5sqehafu6shLAwbo7xCrxSqAXaFUv25jjGmlNRD7jEvNbMwNiwBluc0WP3W5tq5ZAYXI4Wl5pYokfi7iqWdkDb2L_8yLHiOM9ytHY7HSIEYw5Y8N3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
وضعیت‌‌آکادمی‌های‌ژاپن؛
قشنگ‌ مشخصه دارند برنامه میریزن که یه روزی قهرمان جام‌جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22923" target="_blank">📅 12:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22922">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1_Z2Po50S0BJm01zunxu5WndZzTUUxUY9kaEubnfi3_7dIGCbhf6X1lPo7V88SYk4x85N2dQ_ecbl_Q0F0EtQKFx4vwlg28xCwhnGKbXDAT8x1obNAr4plcvNQ0B0SCJ6XAVkiyFajcqonJGxc6BAa2_qEDRcT6rEN6-wkuHrDB4ChAAiRuBK-2S9kKGTrZMjiQAYcm9LDO5lR2DwKXWmBWiDEWPttDGOZE-QCXB7qySGTmWjUgVVErlqk6I2liuXaP6HuXETMyPYIeD5KJKIvIdKukX5TFKDFujinJwXgAWP5N9Jrhxq5MLAPA6dQnJvzOavCsY2A1moEJSvUynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حدادی مدیر عامل باشگاه پرسپولیس هفته آینده جلسه‌ای با مدیربرنامه مارکو باکیچ برگزار خواهد کرد تا تکلیف نهایی موندن یا رفتن این ستاره مونته‌نگرویی مشخص‌شه. باکیچ علاقمند به موندنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22922" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22921">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=HZUeY2WfdXrQj9Cq9YeOlSil1Bp3qUNFGtRT4AbinZaqOtFoIEwc_eSGBNBCAuJhDVqMk7yxpR7u46kPR8NykbqrhN9UDJ8alQhIF1XMnVsCfin3ZpGTm_IiRRhNvh-1zNTuCSfmcjN2MpYVWOGwJshfXPyIp_5pT4Z11TKlC6-LWRMfjo3oMYI9ZmcF6FENXfpVZw4UM3yeLWmBoC-hkG3nDNSeJFrjbAY1jZBNfLJxqwyES_9H-SuxD61cwgLgS3EwWpwnnEiGrrIq8iKPCAT7shQp8O8A7zW3NdnlYBmRWoarpOp_qfQWFTeyQvgc14oaFY3eZHKxOSpxIsyLbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2a01aafa.mp4?token=HZUeY2WfdXrQj9Cq9YeOlSil1Bp3qUNFGtRT4AbinZaqOtFoIEwc_eSGBNBCAuJhDVqMk7yxpR7u46kPR8NykbqrhN9UDJ8alQhIF1XMnVsCfin3ZpGTm_IiRRhNvh-1zNTuCSfmcjN2MpYVWOGwJshfXPyIp_5pT4Z11TKlC6-LWRMfjo3oMYI9ZmcF6FENXfpVZw4UM3yeLWmBoC-hkG3nDNSeJFrjbAY1jZBNfLJxqwyES_9H-SuxD61cwgLgS3EwWpwnnEiGrrIq8iKPCAT7shQp8O8A7zW3NdnlYBmRWoarpOp_qfQWFTeyQvgc14oaFY3eZHKxOSpxIsyLbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیبروین یجوری به تیبو کورتوا پاس میده که انگار هنوز از دستش‌بابت دزدیدن دوست‌دخترش فشاریه و میخواد کاری کنه در تیم ملی سوتی بده:)
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/22921" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22920">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22920" target="_blank">📅 11:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22919">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbZw0f7eQAHiqJhCDDV3-qs6BUGvAR6QKuyERdEU1Lw6FTuWOXpFvc8jqBnj7jJqzELoqLfBbik_Go_oiBtumOdT5VuOcJMCbnGcA3n6hELCuEoks9F0O2_q6kEn1IVNcLGQK3TkziB_-du-vYd7Ng49th3u2bUTa4H7f7l2esjmC4QN_2zb-P2SUW_3aP2afOejI4dDiz5VZULlEKxwi_xsZZp4olF4YtGjOvCN4_04a-9O0ZgdLygqXbnsEb5GwD39RSDESYfkg3cxm_Tj6gvQLaRbJmdren9EjAXmCdXLuHHk6gykmCpXZS2gD1nQsYwAiN3yKVU3IsxhMBdydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22919" target="_blank">📅 11:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22918">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brdXBp0h2AWrv5e-eZHWudlTBUckL4Ro3mYQ2aEQJaEwT_7KiVHGb0Vx0TpylSj18w5o0sOn8U38vIHOF62wV6f3LnNWzK_bdXnWnj-ZXJMX9R7_wIV8MDBwS-SIEsbcPxOZnzhqROAr6B27LaKrvlR_lR8WbrQmESLvdv6bPNetCBPL0MtQhp-AKrJfzwx2kzpcJIz80Nlk5x7KHqvgM0mrcfRnF2DpaVY6keS7kLg_CoAfB3gvIlOto7iWiXeAH7Qgqu6Z8rOruIhNrI3V6gHBidT5ADCFLWK1kLypAahZoREapRCvaZZIzXf9hXA8EUx4VlNZEZt-YEpLFnDlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/22918" target="_blank">📅 10:39 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22917">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=Bvt32GbhVffJt_jjxys0srs1IHb8DdHK4u2ugS68k1nliGMJBtUnTJNEigPBytNY2ureohW5R9_VX8MD9gxcBf_0VeGfAwm-PqfcuIDSdNTnE7pMg5xIn6S84MCYCYaD3k0E4mUb_QxK2vIghAzBTtb7RJ-id2Sm7_yt0pzQyOgSMajLPu7gpCQpZWJkrEJkossOti5n5KdE1YXbSzmjEVXTCjYpjbNTuHSoKMK7lFI21_OWJ_WFF55HixxzhI7mcfGGHbJ0WURapoIK2M4sr2UgK5kiolapAHdtda8cS_p-va9lUFjJf__sHdW4b8HentaQkJde6oOUbZLy1hy4Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d705d6a743.mp4?token=Bvt32GbhVffJt_jjxys0srs1IHb8DdHK4u2ugS68k1nliGMJBtUnTJNEigPBytNY2ureohW5R9_VX8MD9gxcBf_0VeGfAwm-PqfcuIDSdNTnE7pMg5xIn6S84MCYCYaD3k0E4mUb_QxK2vIghAzBTtb7RJ-id2Sm7_yt0pzQyOgSMajLPu7gpCQpZWJkrEJkossOti5n5KdE1YXbSzmjEVXTCjYpjbNTuHSoKMK7lFI21_OWJ_WFF55HixxzhI7mcfGGHbJ0WURapoIK2M4sr2UgK5kiolapAHdtda8cS_p-va9lUFjJf__sHdW4b8HentaQkJde6oOUbZLy1hy4Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایگزین تشویق ایسلندی رونمایی شد، تشویق وایکینگی هوادارای نروژ؛ تو جام‌جهانی اینکارو بکنن ارلینگ هالند جوگیر میشه به هر تیم 5 6 گل میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/22917" target="_blank">📅 09:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22916">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3BIcLjkKgm8JBbwO5--m_rsXGM-qUEFvlU2qv1jmkNDLsEFIyLKI9aVj_XjoS1FeBx5YuelV75quj0XTSubVoExdlyHrFYB7wFqfaRZrG8FyBOPUn-GC12HPduCwyWqpd1xI4jvu-NNXsCEOno6CkdvOdjfDGZswnuMtVad-oB0FaqC9OuyRs8vPa-1FiMtYoXjCl6nAkNXeDIPgjJk6reL13cw3Oml09nhUpq-nmeP_ik6zD2E_TbiuO5-CK4ySZkaP8rFyYN2EVUxrcmmjgysQYWn5XRoZ5helsIdvFsU7ABu8LMx59TjpsbVwb_xTZdumViPxlqqtxWVFokcpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه تاریخیی کاکا:
برام مهم نیست که بچه‌ هام بدونن یه زمانی بهترین بازیکن دنیا بودم؛ فقط می‌خوام منو به‌عنوان بهترین پدر دنیا بشناسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/22916" target="_blank">📅 09:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22914">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8tZamCQ5CL2U0S4UvN9e-TgiJfyU9Bf6H7hqTFgoYfywAbpI5rucVAS_soGx1JqQ2UHv2L3dtsfhlJzjGcalLEu5ruwuwKFHB5D7NwXIHzQ02L9-Se7gQnbgAUd6X2yIC83vz0rBVVfwr7UubntQcD9KyEeHiMNZuPF424TJ3Q5tzFtm0olfsVKFn1sMbOWBrRmMazEDVKRw_7pvtf4MvjDMZvfWKS4ykXAq65IVrvSp5isk5OEwte_kxZCIPYVRBvKbF08euFVXrKYSO4L0irSGEccTv8UBnMo2TpGUKruVgECe4JiEMJW5kNtCHeOE6HZzONH2YKdRm8Dd9_THg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارهای‌‌‌امروز؛
تقابل شاگردان کارلتو با مصری‌ها و جدال یاران مسی برابر هندوراس
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/22914" target="_blank">📅 01:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22913">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOg5oT4bMCDTtt8MoI3QDuC0JMH6PcxRbExKWagtktR0d2QFGIav3SPP2u0OsYHv0GS5MGvvtaDqr0IwfK9TMhVlBuCOKFuNm_jui_DD2f5h4H4G0776ZnvXEdwjKYdFaw1Ho0CiM2-TjcpZe8RyoVLiLin8ANOyAI86ScsG-cQPeuK6fRQXanCCCWX4OJeDtEac08ThF5iRcPdDDKn74tzAt0uPrhuCJJoVEciMb5lNt9NLeEyLBBX1if91cvSxRJmS_j5VpQY4vV46oT61uaBIPf2hutx-jIxYFuXBm0rTCzFEVv6TJa9a6kyvXuYBkbmCnJTtiA6rWrWinoT6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌روزگذشته؛
از بردپرگل بلژیکی‌ها مقابل تونس تا برتری تیم ملی پرتغال برابر شیلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/22913" target="_blank">📅 01:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22912">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAO69l8RDdsAv0AbXoKDVdf3UMxhFfM3MNt8g_DXjbO8xv2y2asx_lLb-7Mdnr_f2KHcMmS257uhdILT5ysdhuB2giAGA71fBdhf0ULexFwwxJZsfrTEDKIJod24fFRW438bU1KRp8_-8leBSmwsmxlHzKIMbiNjk8_VclO76t_CGq_TT-twveiiLOAypSZoQIgVP5I2Gw7Z8y2Ibja0i2DuYmQBMXEpawA3ZWKAFHG8oXhkIzvt0dzHLefQDoX2Gz7xOqULyKo2JUGmlJLifT-bdejjmAOgyqKYx6o_Rx3k_e93rLoxOPL6AmwTZWXmkby1sXVubz6t3Wg06icftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/22912" target="_blank">📅 00:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22911">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=XNAr4_2Gc8fpeSDZQPus88glOC68g5vg4r6OARk_9OyNcfaRqZSn5M-VDACqbwOEP2GhGQSj0B5VvoE2iUjIgz4GB8pIhVZPPGdTRWB838Zz6MOrPBDr5wgzmKjFEF5vHGNG_1gkON8xutOaVmnAylOmfZR49ycKUpj96ftalTqxbTc4hps9nWLTNPtaaQmCHpC9pMQjDI9oBM_b_3IJcO7yBN1zXXSNFLJoBGFN7BR8T6cvbacMAScMPoXHBZg8qpOHhtxyP8TsFG6Bs-Xp2HIr0dytlVAHmZ50VI6M0QMdWu1e_vvby3sgNocoCHhhZcjQ7SR_lmySnxicz2Ie6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc9d6ea65a.mp4?token=XNAr4_2Gc8fpeSDZQPus88glOC68g5vg4r6OARk_9OyNcfaRqZSn5M-VDACqbwOEP2GhGQSj0B5VvoE2iUjIgz4GB8pIhVZPPGdTRWB838Zz6MOrPBDr5wgzmKjFEF5vHGNG_1gkON8xutOaVmnAylOmfZR49ycKUpj96ftalTqxbTc4hps9nWLTNPtaaQmCHpC9pMQjDI9oBM_b_3IJcO7yBN1zXXSNFLJoBGFN7BR8T6cvbacMAScMPoXHBZg8qpOHhtxyP8TsFG6Bs-Xp2HIr0dytlVAHmZ50VI6M0QMdWu1e_vvby3sgNocoCHhhZcjQ7SR_lmySnxicz2Ie6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصدومیت شدید مهاجم صنعت نفت؛ ویدیویی که روزتونو میسازه؛ فقط کامنت‌ها رو بخونید
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/22911" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22910">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=Wx0TzJdfk-l1qu_7qisL2S1A15xD_qyRF4UzFMgGdCIXp7MtNFOT8-cPtqPUjG2Sv2x8sHPRKl1eTv0bDn8b2F8zY4m-GydJYJMnMH6ILsQZQgynWXJnNF3g774lBcAC4_0aOvhzb7-RCgstbtXcaa5KcR0Z-X5Wgd4PAP5868g-wDqnbeQSgBTk70wBierszxCTZ6AGvG190mdi9CvMQ5gPN75R_PjAuFLhHsSlWKRIv5xTBDVHgV_DGWMH4qYdbNMujs9T751PVCHdcauMcu4P8hqXsVy2n2XuNte3ZSIE7yZz51QVE8GEGzoPcApZ7yBTOifKO2StxtTx8hDD8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7334e55a73.mp4?token=Wx0TzJdfk-l1qu_7qisL2S1A15xD_qyRF4UzFMgGdCIXp7MtNFOT8-cPtqPUjG2Sv2x8sHPRKl1eTv0bDn8b2F8zY4m-GydJYJMnMH6ILsQZQgynWXJnNF3g774lBcAC4_0aOvhzb7-RCgstbtXcaa5KcR0Z-X5Wgd4PAP5868g-wDqnbeQSgBTk70wBierszxCTZ6AGvG190mdi9CvMQ5gPN75R_PjAuFLhHsSlWKRIv5xTBDVHgV_DGWMH4qYdbNMujs9T751PVCHdcauMcu4P8hqXsVy2n2XuNte3ZSIE7yZz51QVE8GEGzoPcApZ7yBTOifKO2StxtTx8hDD8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
امباپه27سالش‌شده؛هالند 25، اولیسه امسال وارد 25 سالگی میشه. اینم لیونل مسیه در 25 سالگی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22910" target="_blank">📅 00:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22907">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=nRR-dbg5gKx6-Ur7JdgYP5QnyhCP5VyBQEU1uCjCKma4bhv7gOkMcV53NsYJtyv3darGqycJ9Y2LUkMx5ERIjpIkoZB49l7L479_Y6VHjYPGp9TEFpnc2-pTXCn6xDHdD5tldEghu6VTfJd-FgSRSAYmrtoPeEjLfq3Y4xUeJRBIVq6GjhgCZoQ3ClMZ1n4nRMUmlHEdaJGgTdwVOuIOZ8MQbKFId4u551ip0sih26E2ngq_fQfQeU_51gs3P0D981x1QuF9_PSwe8p4wG4J5SkB5AAWeoXQHxHxjYEYQU5LelTFjO33COjOzSAUQeIChaxE-jOV-Uk_TVbdPPSZng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c2e44c05.mp4?token=nRR-dbg5gKx6-Ur7JdgYP5QnyhCP5VyBQEU1uCjCKma4bhv7gOkMcV53NsYJtyv3darGqycJ9Y2LUkMx5ERIjpIkoZB49l7L479_Y6VHjYPGp9TEFpnc2-pTXCn6xDHdD5tldEghu6VTfJd-FgSRSAYmrtoPeEjLfq3Y4xUeJRBIVq6GjhgCZoQ3ClMZ1n4nRMUmlHEdaJGgTdwVOuIOZ8MQbKFId4u551ip0sih26E2ngq_fQfQeU_51gs3P0D981x1QuF9_PSwe8p4wG4J5SkB5AAWeoXQHxHxjYEYQU5LelTFjO33COjOzSAUQeIChaxE-jOV-Uk_TVbdPPSZng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وقتی‌داماد مجلس خیلی فوتبالیه، کریس رونالدو فن هست و به‌هیچ‌وجه هم اضطراب اجتماعی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22907" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22906">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=YXxcP_Bh1rmZ2xpM6EMf2PYBoGhFpPRiagtTH7VUnPXSU4TJD4HzHWNO-TxOeaxYrlrRVGSJwosBh9XuqrVtL8CpNw_hmHRsk9DPpTgi-BdPXJxWOLsob-pZTidrqASzuwQl0QVz7onlHQ_Pp7mVvu_qTyejDzWEIQIfsDts5L419CKyzIZtY1mj0m18wd39XPpCcJ6m8GJwbHvWbjWW3CpUKbYJUZU94_3h1_5W0BkHj-LefmCHmxAMTe3oVihW02CPQzIa8emdLbV5oeq-uzKyvjrwG7gj1ZHJ81BcmCsJQ3XxeJ2ZQ9NTBPSo310Fd0zcyTi9lqxAInrXViekSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762477e8bc.mp4?token=YXxcP_Bh1rmZ2xpM6EMf2PYBoGhFpPRiagtTH7VUnPXSU4TJD4HzHWNO-TxOeaxYrlrRVGSJwosBh9XuqrVtL8CpNw_hmHRsk9DPpTgi-BdPXJxWOLsob-pZTidrqASzuwQl0QVz7onlHQ_Pp7mVvu_qTyejDzWEIQIfsDts5L419CKyzIZtY1mj0m18wd39XPpCcJ6m8GJwbHvWbjWW3CpUKbYJUZU94_3h1_5W0BkHj-LefmCHmxAMTe3oVihW02CPQzIa8emdLbV5oeq-uzKyvjrwG7gj1ZHJ81BcmCsJQ3XxeJ2ZQ9NTBPSo310Fd0zcyTi9lqxAInrXViekSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22906" target="_blank">📅 23:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22905">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0bFv_VuvlKgHiHpPRsezbJEeiUfNqAcLXD9_G2yJiM7JfDSwyBhNjnAgGizfZ1XBw-ndUADclMxL_DfgYeqlira7Apl1dp_1RFAxPIRp3iknTKxTe2JYjOEWQ1bT_Dz_J0xgcgFYDirLOQzv49vHMuGgvUbMup_P_6wGh0LIQ4jsGgi8YeWJezB8oWsuEnaelhUbANabVLNJQqjFZWx1-WgujibO6f50JC1Miipy-ET-CRwTk-ZCBzNho3q0BhoOtkJqdPdkDTaegXxDlqYAu2DpChPUb2245Ffd154vxzbIb_23ajBEpXrpKLYhuAfRQK4nsr_cygbNGxqdOifvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇪🇸
#تکمیلی؛خوزه‌فلیکس دیاز: مایکل اولیسه از طریق‌نماینده‌اش‌به‌مدیران بایرن مونیخ اعلام کرده که بعداز جام جهانی 2026 تمایلی به ماندن در آلیانز آرنا نداره و قصد داره راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22905" target="_blank">📅 23:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22904">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap7Ea2VZ0tWSDwi-E9aNPMJevRimMPir1pTXUeENF0JjnBRMGB4wbQ1d4jl5IvEkz4TCDpLxDm9BSYpPvxXecZYUw1DIF6WKhms1y-1owUqVpq9gjmDpEDKomjOcfXb6SA3bGgWeZlLKz5kRAGoOZYhWKMSALFU74fppok60OP_KfTZuSfc0VrdoFqJs_ik_NnNmZABNDOA8r0jwokKe7-Fq6eRObi-2zg8oGeRYB1OUozF7d-LafSsaFheZB0Y8ql0ybaZCAq6gpo4xJDjD60imn4qBMDn_2ljQZQyiii6ZHp6peJDmIUleOru_utdH-oiMj9yKF5gKX0XTkBpniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق گفته رسانه ها؛ یوتیوب بزودی طی روزهای آینده بطورکامل رفع فیلتر خواهد شد و همین الانشم روبعضی اپراتورها مثل مخابرات رفع فیلتر شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22904" target="_blank">📅 22:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22903">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEEwx7MqE78TEIBXt_-CL0L8dDBhge43EMVZWYGTJttaqmoyDLfZ2-IBQTEKCHu_MHCMIqipsfMdRfDxViDLmwCeKHsIUEzOE3GGwCBbtfiQwiBqTgeJR9Jp5HwLkmEKuhYipI_ZFgAjowu-Wd-i3CfvkwzCfUG-TBj3RXnR_3oN7f3gOQ4xpBmamRFgkfPeuO7JgtacNQgvYzJr9oqIR3G18pJSmpEht9dMNoFT4JiXTKfWgK15zRn5mRuzHofUspn2ZoOCs-EFa7osdHCPRBcGX6XPrs9MHyytOTFHJ7qWMcCW-9Ns4DeldEt0Oym2sSbGLIgBqfGG6WWUamj6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌اخباردریافتی‌رسانه پرشیانا
؛ ریکاردو آلوز ستاره پرتغالی سپاهان که با شروع فصل جدید چهار ماه از همراهی طلایی پوشان محروم خواهد بود به مدیران این باشگاه اعلام کرده درصورتی که محرومیت او لغو نشود یا به حالت تعلیقی در نیاید قید حضور در فوتبال ایران رو خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22903" target="_blank">📅 22:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22902">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELJEkiJq_5KuK52D6VjsuHAEsR9QrlUj3Pi-qZH0WLc9YbRI6g2CmbwzqrhKX6Bd-xPia_UrlZsLHst0ZQVqSwMbeLmRAmgz5U5t33iYGR7UYMfN_bDaXQZwVA7lbOOFZBy542_aSX6zwCupXAJxIalwdaiTmYjY4JHlQizeiLXN15XxXpXAW7eeEQKXRejt_fZtfBJKN-IbfM0kADHSF-qKNIp20GkLyVqfqv18qjiNDXRQfgWPJIb03eVDmRbVlZsbGYlHWZF6yuOirs3qfh9Kz6OJKQvLlNa2hkROzbPigrH2vlip9p6JnTXUpWTNDsl2ye5TaGUZt1IxUvVSrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پنج مکمل‌ ضروری و مهم برای رفقایی که بدنسازی کارمیکنند. هرچند با این شرایط اسفناک اقتصادی مملکت خریدشون شاید سخت باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22902" target="_blank">📅 21:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22900">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rryb6513gjA3gGqXN_fTLwiNpg8awxVOay0AoO1MZ4teHweyHhCtQVChuhCctzTa967XpSBgZrrfCswsUIAhrHxgX_jAOqn2jcNcquo3ChORrC3Y2_ED-JRJCUcR-F9Z67adUxaOBS9o5IA0dpRvaUkHdq13ArBH43XVbhbSdIvDxS7W24Z7BWRpfw2zPW3elMFm7EnebbyzOlOj0UT_9kMVqlISO1M4TKWJ7PCIxM3tXz-eLYyFCaCXwYw7xwGUCaFvncQWukUiX9ipe-FpuNfZ_rQmeTZG5Koebhk5iTWQAlzVKi0w2wqpfe6uANQKV6nwrfYPlJH1lEe_LZQkwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjWY7PJuPz6_sFKymJ5p7Ta04UNDsOs0RxewcRUT6i2NWgRI0SHgjH893oIAdHj_le0ZXTC64ix0iis_0zbeNG-FYu9Qj4IATlYgSR7ch7MO1uDf0r94wHUrM8d5IkSjV-DyJnHay5_Bz5th2GjKLf1I-lezZvT1uyM505mHHu6RRxlvleotVzPJEhgKdbdoVgwgbIs6zY7UFVtvGWAhJ1yDoaJDFZyIqNJF3RvN6A8YDYqVZRk9LITe-9sf3k9feX7DPpMSFgWGCfvnFHwdPKbYjZNJCb4J54QVnUx4ReOYlkHRGn5wUx3i5MmwrsqCuNgAAj19keVsc1aKgraI4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
بماند به یادگار
؛ یه ریاضی‌ دان آلمانی به نام Joachim Klement که قهرمان سه جام جهانی اخیر را با مدل خود درست پیش‌ بینی کرده، معتقده قهرمان جام جهانی ۲۰۲۶ هلنده.
مدل او که عواملی مانند تولید ناخالص داخلی، جمعیت، فرهنگ و رتبه‌بندی را در نظر می‌گیرد سناریوی نسبتا جالبی را پیش‌ بینی کرده: تیم ملی برزیل در مرحله یک‌شانزدهم نهایی توسط ژاپن حذف میشه، آرژانتین تنها نماینده آمریکای جنوبی در ¼ نهایی خواهد بود و در آن مرحله مقابل پرتغال‌میخوره و در نهایت‌ فینال بین هلند - پرتغال برگزار شده و تیم ملی هلند نیز قهرمان می‌شود. البته این فقط یک پیش‌بینی آماریه و تضمینی برای رخ دادن قطعی آن وجود ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22900" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22899">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkSMJRsIh5q146ViTpORSmgI8xvUJQDez9KamCf9XGRjwe3zSlwvvGGtd9l4Z7qC0T_hX5rPnDSJZaNKPnz5xYZ7KA-7iy6CuSjOMNfX_3mOwDTwtyL_Np_nNUKsqxuIDRwZimDwI7_tNpIEfQrh9L8n-q6H-JYIlxa_blUlD_dgNujtjSRBLXRQje6FdyHMspbshd6SS9i-u1BY07-tn9Ajp0J7O_bVhgcN36Q-eGZB_Z4ywPjig84WuCovL4A05Ae7DCS1caviCKhtrEvlWTBQny2OebYGYEUlJo9WEnb7aewe7yVj5qdKC24fkqqOCWKVNOYCOllGR0IsQPyLiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22899" target="_blank">📅 21:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22898">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HrwzjpyCWMPpfjL2nOv-arWGsidJMoQ7QtYqf2YhGSJgTHIHQ351pOcLKRruskVY2AxY9nDbHXVfdyQSC2emmTBY5_cUi73QwLP20E-IlyGz4cYU--8QjvlxvCQcXO2L0v7Q8WK-JEmPDNgghszTL5oxSwd5DbfvSKL9pgZ2vqKJCSuSWgdzr7yf2oD5VyfGvPKaq7Njchaiw_PUNakvSujDmDhezIvMYsaA8Yh6GZ1D-pi8KlydXwG3uMmayT4sJiRUxkdLGU72Fw10kAt3l1dsd4N96MrWCkwLIjqNe3kdrLnU6eiuFfU6wjjwXc1cDNjUvCSoWNWxN3ZqAe2v9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌استقلال با فروش جوئل کوجو به تیم نفتچی ازبکستان‌موافقت‌کرده و بزودی این انتقال‌ صورت میگیره و کوجو رسما از استقلال‌جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/22898" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22897">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f73008adba.mp4?token=GMQKwL7aiJ61bffee5nNGnoqeBNvKa-GhqeRjvwcczGp_v_OFLFOnZ_mhrvp8bEcNlcwJdA8qk8rLxkqpluV6jbIvVW8Em6VTFuQfLE6PaPQok-FfEOV0aRTBstoKqpDRR1g8xj_TFPJTxQxCDIRAItjpkts7Rz3vhDFbYSBBHTQb4VdTm28wxjJfF0nDjuU_XBvUI9q0t3TYNcetqP9uP-1Kq_r_gx2RhNy9p2cRn3pXMa0uiT_PejMI4VmQSjdVdY1IDL0N8YGvqy-m8aYg2tIK3mfPxwwCVin8ZHiZs25eB5fjcxs-1S8wLu-LfkflRJh2TVucy23nC6msxmdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f73008adba.mp4?token=GMQKwL7aiJ61bffee5nNGnoqeBNvKa-GhqeRjvwcczGp_v_OFLFOnZ_mhrvp8bEcNlcwJdA8qk8rLxkqpluV6jbIvVW8Em6VTFuQfLE6PaPQok-FfEOV0aRTBstoKqpDRR1g8xj_TFPJTxQxCDIRAItjpkts7Rz3vhDFbYSBBHTQb4VdTm28wxjJfF0nDjuU_XBvUI9q0t3TYNcetqP9uP-1Kq_r_gx2RhNy9p2cRn3pXMa0uiT_PejMI4VmQSjdVdY1IDL0N8YGvqy-m8aYg2tIK3mfPxwwCVin8ZHiZs25eB5fjcxs-1S8wLu-LfkflRJh2TVucy23nC6msxmdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبیکه‌مسی شخصیت‌منفی بود؛
آرژانتین ـ هلند؛ یک چهارم نهایی‌جام‌جهانی 2022. درگیری بین بازیکنا به حدی زیاد بود که به نیمکت دو تیم کشیده شده بود و این موضوع باعث‌شد مسی به قدری عصبی‌شه که یه نسخه از خودشو نشون بده که کسی تاحالا ندیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22897" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1hgoKjFSD959qRzkg_J6ALWdwwOyneXjGiL7KPLPRjZVDB2hp1p0_6ZJ9jUiiTjK6iVA9mfmmNSTz2hDc5A2J8nWJGW1RHksBiw6TNaKr5bcfyDD73IoOmEcEotEP6ARMCgCPvW0uac27Sxc8EAmZ4FIILY0Uok9XF6yOHN3kbDBTqzFzqOc-SKoQ4jOTEFoD5z3ouox87X-aWR58m0lSzUBQgyo0kJ1CKCrwGIzOqVrGgCEPcfBbsbrRt8jw-youNvEv83vVACvVdrcaL6p1Uz9qdQmD06E0o1mfLymTYktDxA7hlQFh2GD5CmeTD_QOvgOdsiLyV48SMHp-INNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22895" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=PO95HnehFhgA4vFGMwec9LTyNNanC0NegJgeTDMTWJvaUYmZ75gGiRsrOYJCtJoJqiBDmroZkG9kzsCYBuhsV6ctbDCO3PW1YHEC326MWM8IeKSNpL1oRBWyHCqBJDFQp_ULnRdoDaPZ_1DrOXy2eXBNuvylQdfg4ac38l1QqOwJfP5HHRUR4j0OB9yJG-nfI360B2UvTPd4VxgqIn1sO5S6qpsvqJn1NTjbLEG2M_3BmEinsvua1ScP4ccnKNxeXSmgDPb6Wnj_-RlSuTz8u_jWyOXkySbBrclU0XauhvG0t_DkCcps0ZJLWZ71-60vl8eu5XwgoYz7MJ4U9r6IKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc1ec4c74.mp4?token=PO95HnehFhgA4vFGMwec9LTyNNanC0NegJgeTDMTWJvaUYmZ75gGiRsrOYJCtJoJqiBDmroZkG9kzsCYBuhsV6ctbDCO3PW1YHEC326MWM8IeKSNpL1oRBWyHCqBJDFQp_ULnRdoDaPZ_1DrOXy2eXBNuvylQdfg4ac38l1QqOwJfP5HHRUR4j0OB9yJG-nfI360B2UvTPd4VxgqIn1sO5S6qpsvqJn1NTjbLEG2M_3BmEinsvua1ScP4ccnKNxeXSmgDPb6Wnj_-RlSuTz8u_jWyOXkySbBrclU0XauhvG0t_DkCcps0ZJLWZ71-60vl8eu5XwgoYz7MJ4U9r6IKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇨🇴
وقتی بازی‌های باشگاهی تموم شده و از بازی در کنار هری کین میرسی به بازی در کنار این:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22894" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4Veo7bYHoQy6Ltct_Tx3V_y2F1JHbICAQcqeoOO9lx9ELSlnQJyiIrudFEWAL41CQaLqshrjJkp6foNaWfeunclZhG4R02BTqSGAI0LJ_lr-8I617zcKzIE1gvCrF4JroetKa-kss_-GKbSTF5VAzE2jJBa5L_Ma3IIYpo0FAyzPTScOhpRp5VW87MWPZX-spVZwpPcU1HwQs0N0Hz_CV2NuhK0HNSNZfw3KLzj9i7B2LWCIS0uSkKRVl2wfoO8ceSZyIIFPC4VtNZ8XVOqauY8OwwH796qm_PBNBpY4SQPPOyd4VxIDjMAtezlfyCTqs-8VSy-rj7Sbyj5Dz3Eqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه فلیکس دیاز: با توجه به شناختی که ازفلورنتینو پرز دارم به‌احتمال 99.99 درصد مایکل اولیسه این‌تابستان‌باهرمبلغی‌که شده به رئال مادرید خواهد پیوست. پرز این قول رو به مورینیو داده که با هر قیمتی اولیسه رو به برنابئو خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22893" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrukWWkxQioXKJRxphuQPX0B0kwJQniYZDtVM8HvA-JwfaXZFNMowXMWxuoTyZJiMSN0GRMy511ezSddzIx4JdpvO9IIXD9eH7VbX0UdivtetIJqy-UTcmUgnsgtQRSezUCBTW3sAE8XImQ_F6tvZbYnHD4jXM7boNTYrx3sgjqwSA5hNRnpSvxFIjBCVnuQZeR3ViO6kJFbZ3JbJPHSilRHlGqpsDxC3pNhkZxjpCGhH9Jo-7JaZWJxaNnwthlscG068XIhTagB_hxaNRm91t8EUfZwgk8LxIu91H_bwV151isfTnro3BXSfE3FYF77y5vGMYmD62Kfo-dAoTxAhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22892" target="_blank">📅 19:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=aQNtd36uME4sfOYIiO2o39F2-hMAjTvOdxnXvoAksW3tjBOg6VTqUOB3xXAVzBD-V8H7dXQ9Hb4B8D3k2anhmOJrsoFX3V1Rd1BJP8Gop3_2Rb2tJ1w9FU0ORrB9UbtEFo8txwOXQK8hbTHjGDLyajZRHOshkZXPojOQSbt1bCqCAq6HI05lfXWOlPlAX9NxHuG4FrFXFob67Gha2pKaLrkokQYln49nmh-nVYRqaePAL7TrQQuqCfbR6dcgv0i9N_ax0LVb_20DKbTEk5WfR9qt_ZGsLZLj7QVxf1-uM4T1qOA5BEv4JoGMqL55RHkuk2i7hMkSzGO7RV2jpg181Tr3GT54vp0MgwZt8Gx5oBDcDqe7C4sdUQLlBWfR2-vpjeGahaJaO-5VAaVrMmQ2V5TvGVqzhSk6sfonZlMYue8siyOFQbF5tqREAeAgIRCCc5ni2uc54z4hYmTVkUCSKgFjBBgmWHtLE8FhNrDVcqgxnKIMAZr79_eUMT8xHO-F7CX7EBA4tRwrs21IOGXkNiMj5I-Z1R_Bcs9UQTTiwVXa7LmYmnw6DG6NRLLjkl-HcfwDXcdCYAu178M-f7d6ve5M2kG2WdJBZ6hEhMhpcUaJNNWRLs7e0BfBfNFfSfMZiMmMNmB2bSM8kyJGKoVit1eDarbeYCFK9P47J4CpuhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf50298d76.mp4?token=aQNtd36uME4sfOYIiO2o39F2-hMAjTvOdxnXvoAksW3tjBOg6VTqUOB3xXAVzBD-V8H7dXQ9Hb4B8D3k2anhmOJrsoFX3V1Rd1BJP8Gop3_2Rb2tJ1w9FU0ORrB9UbtEFo8txwOXQK8hbTHjGDLyajZRHOshkZXPojOQSbt1bCqCAq6HI05lfXWOlPlAX9NxHuG4FrFXFob67Gha2pKaLrkokQYln49nmh-nVYRqaePAL7TrQQuqCfbR6dcgv0i9N_ax0LVb_20DKbTEk5WfR9qt_ZGsLZLj7QVxf1-uM4T1qOA5BEv4JoGMqL55RHkuk2i7hMkSzGO7RV2jpg181Tr3GT54vp0MgwZt8Gx5oBDcDqe7C4sdUQLlBWfR2-vpjeGahaJaO-5VAaVrMmQ2V5TvGVqzhSk6sfonZlMYue8siyOFQbF5tqREAeAgIRCCc5ni2uc54z4hYmTVkUCSKgFjBBgmWHtLE8FhNrDVcqgxnKIMAZr79_eUMT8xHO-F7CX7EBA4tRwrs21IOGXkNiMj5I-Z1R_Bcs9UQTTiwVXa7LmYmnw6DG6NRLLjkl-HcfwDXcdCYAu178M-f7d6ve5M2kG2WdJBZ6hEhMhpcUaJNNWRLs7e0BfBfNFfSfMZiMmMNmB2bSM8kyJGKoVit1eDarbeYCFK9P47J4CpuhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شنیده‌های‌پرشیانا
؛ایجنت‌مطرح فوتبال ایران که ارتباط‌خوبی باستاره‌های‌خارجی‌داره؛ بار دیگر ارتباط خود را با خامس رودریگز ستاره 34 ساله سابق رئال مادرید و بایرن مونیخ برقرار کرده تا درصورت تمایل او رو برای فصل آینده به لیگ برتر ایران بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22891" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=qAgfnzmyuc9zx8wQxhlzSIpmfYp3SIrvOtiUaszkvWrAlxbA8NV2LFSYBYPwRTW-Pfe5oyvYuFwA04yK4uMWyz3zV6jjP5X0fITJghqqBl1tOhtc5BZyX8Ib1RD8E0MsB_L3KdJ_8c9Z-_MVdfgwMOkZEZc6BA4D3QqQbQ1jtGCfMXn9rZQBCTqMb9VJjMAHubT22gFOBDxslbIxE2DeRaRTJ7-_RiSKvbXFpVMM6nerUpVUOJvC4HTouSzaknvg03_uj0IzgcKeF19we68sgrC2XLsbzYlgNbPjKjaAihJnc9u7bwMuvVLpOhXnftyAsIBjss64PxIR5-aGOWfcnCZCctkNWBrb3G1wpMEaqdFrol5BiHPd4j2qotURqixh6NwdbRVkVxrZFLHKxg6SpaARsuH0cN8Ugwq2KUh9qSgTocy_j6x4HQYbLq36oW3dFE-4wfimghOkByL2Qxt7djjQlquOPqYxnZhaxYJv99DyyQYTTl0rcnpljpQO4K0c8RbboyBoOWOTrM8QBAoCRzSfWjr8H3BRrJQtkFY2g4sSka6IFf16oussYltht3uLWcHrE6AVT8fHMsbijYZP_fJBVaDZkORKjIlm_NqB8TmlQd9x01FaXNS1SewhlAmHZEpH5klpvO39an2sfOUKLSj56-XLnhd51jYGMbEfJ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fdcd2c12.mp4?token=qAgfnzmyuc9zx8wQxhlzSIpmfYp3SIrvOtiUaszkvWrAlxbA8NV2LFSYBYPwRTW-Pfe5oyvYuFwA04yK4uMWyz3zV6jjP5X0fITJghqqBl1tOhtc5BZyX8Ib1RD8E0MsB_L3KdJ_8c9Z-_MVdfgwMOkZEZc6BA4D3QqQbQ1jtGCfMXn9rZQBCTqMb9VJjMAHubT22gFOBDxslbIxE2DeRaRTJ7-_RiSKvbXFpVMM6nerUpVUOJvC4HTouSzaknvg03_uj0IzgcKeF19we68sgrC2XLsbzYlgNbPjKjaAihJnc9u7bwMuvVLpOhXnftyAsIBjss64PxIR5-aGOWfcnCZCctkNWBrb3G1wpMEaqdFrol5BiHPd4j2qotURqixh6NwdbRVkVxrZFLHKxg6SpaARsuH0cN8Ugwq2KUh9qSgTocy_j6x4HQYbLq36oW3dFE-4wfimghOkByL2Qxt7djjQlquOPqYxnZhaxYJv99DyyQYTTl0rcnpljpQO4K0c8RbboyBoOWOTrM8QBAoCRzSfWjr8H3BRrJQtkFY2g4sSka6IFf16oussYltht3uLWcHrE6AVT8fHMsbijYZP_fJBVaDZkORKjIlm_NqB8TmlQd9x01FaXNS1SewhlAmHZEpH5klpvO39an2sfOUKLSj56-XLnhd51jYGMbEfJ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 سوپرگل دیدنی‌از روی ضربات ایستگاهی؛
از بین این پنج تا کدومش رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/22890" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX5BGMDwfe0jN0FCt9uv8BSQB3kXgf-XPwbZcuDJ3fJs6DtGWvUNpuCIhKHEAqN3qGUNb1JQQYBgL_1sScVl5tSD0v_Ge3pVHAzpasUOUeRNk3tu-K926SMBaiBJgtIShXU7hsLE3iw2qikC5pBHeg2zccaH65zeflk6yl-d5gtxbwBb9pzsemfUENACuyg_ekMNHGrTDZiT8_jYfi92udlPpp44fTJa3Xh4BvpD_RLPo8ZY8E3uGv-3Vq0UfvM02ky1x96AsgOLrghaCt-CqziBWr3NOM02ZXSWckjjzNHC4Evei1X4yeRdM2Idm8oP6Ueq4u3_vUxgw9eGl2Mfjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در تازه ترین رده بندی فیفا و آخرین رنکینگ اعلامی قبل‌ازجام‌جهانی 2026؛ شاگردان قلعه نویی با یک پله صعود در رنکینگ فیفا در جایگاه دوم آسیا و بیستم جهان قرار گرفت. ژاپن بام آسیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22889" target="_blank">📅 18:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=tImBfuQ15B0BkJJTmWHgJmTokSlACxe-wupc1TPH1NwREpo92EpQGLPpZ7eupNaK9RjPG4zXcYoDbj7A_yBMX4vvncouqMqhDfjN8dCbzM5UqgxIJFfxA0G38Z6CrRBVAV9Buj0yiJcAKL035O5UlJog0e6-xGiayGNFmnIfRbH_ClWW0Nr7uA6_PNAKAAFGnlRceNccTKqQBWgyUDhAuSn4OqCl-s4KzF_5CfmyELOgc56LwHktfhcCDnjeLfRev_Yyq82OzorPovCPOM5IzW2doxaKCX4aT1e2qTzT9eLyKXmoBMglTMnaCC25Akz36-Li7ZNtpwYRfVUsR5EajZBM8Tn9lWowyUpNGPPXIOsivCiM3NvL3QYpLcSQLcgYMZC_WJ-oclBBhcRaGaMIdf9a3mGwZh_R1gHe8xBKOZuK-VzILYxOPYt6ZrYC3sJCilESf24bMGMKIXWVbzeY9JQ74662FNKxXGeMUrGFb5DvYAjdV2czaIXantpT4EuApdcGaxp6wQEZlYy5VX2IjhFXYE3ER9yczYuXTqzBzRiOO8HGYzPnhKC-_46szQTWSSzCQNeKX2u9YbmsqsmaYhq9VgvJGeMveKQDsxfBpQmtoQJVvR9DnlOCL4bcgTYPs_iNDU29AggYXrfbTqK55cf8tBcNrN4hljJVIceXUeY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb97f5a2f.mp4?token=tImBfuQ15B0BkJJTmWHgJmTokSlACxe-wupc1TPH1NwREpo92EpQGLPpZ7eupNaK9RjPG4zXcYoDbj7A_yBMX4vvncouqMqhDfjN8dCbzM5UqgxIJFfxA0G38Z6CrRBVAV9Buj0yiJcAKL035O5UlJog0e6-xGiayGNFmnIfRbH_ClWW0Nr7uA6_PNAKAAFGnlRceNccTKqQBWgyUDhAuSn4OqCl-s4KzF_5CfmyELOgc56LwHktfhcCDnjeLfRev_Yyq82OzorPovCPOM5IzW2doxaKCX4aT1e2qTzT9eLyKXmoBMglTMnaCC25Akz36-Li7ZNtpwYRfVUsR5EajZBM8Tn9lWowyUpNGPPXIOsivCiM3NvL3QYpLcSQLcgYMZC_WJ-oclBBhcRaGaMIdf9a3mGwZh_R1gHe8xBKOZuK-VzILYxOPYt6ZrYC3sJCilESf24bMGMKIXWVbzeY9JQ74662FNKxXGeMUrGFb5DvYAjdV2czaIXantpT4EuApdcGaxp6wQEZlYy5VX2IjhFXYE3ER9yczYuXTqzBzRiOO8HGYzPnhKC-_46szQTWSSzCQNeKX2u9YbmsqsmaYhq9VgvJGeMveKQDsxfBpQmtoQJVvR9DnlOCL4bcgTYPs_iNDU29AggYXrfbTqK55cf8tBcNrN4hljJVIceXUeY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
انریکه بال؛
سبک بازی فوق‌العاده و تماشایی تیم پاری سن ژرمن که ۲ ساله هیچ رقیبی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22888" target="_blank">📅 18:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGo7c0YldGo3PK_amNAeplCsFJE5wEjJHpUpxkuotsTsZihPHskhBLvreheXaCOilkNoBBLMowT2PqcQ6Wj3-juIdLoyIw2re9hNwz0NsYS9MPqFnX6EU9N8yJnYsvAyzGiBN02JbvcCfWJ4vf1F6vOYD_M8Ss2d400jybAU7Dw7omeDruR_qbfmWpWaNmfKSDI9p6kwZv-1D_-bCvjmOkTYjJtnT3irQc4pDcWtXkXDU6OAISZr2LJtDvnyl49hOHNFoCqXoSIwTUqKsfg0BFAsdmQMpBATTFqW3N0IxRZ6Bfl10fU6YXycaptsC5dnG2BWCn23ZcNlzZsLSD_FUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌ بندی لیگ برتر بعد از سه هیچ شدن بازی گل گهر - چادرملو بسودشاگردان مهدی تارتار؛ پرسپولیسِ اوسمار ویرا برتبه پنجم راه پیدا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22887" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22886">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=HbffHE8z7jRnNwGlNn9bZqOALzhTLn9-p5Ub_aLSB-S8evoJ1FF_Ryjz4hAqhSBtRvkeiBHQZSJDJ9HZdJtS2ODJUwfgl-A4nYQRiCa0Y9nlZ-s4uWHzYb4um14aKlkrfFnRltUftLcnp17J5NufdDmkL4AWWG0g678zpg-kj0j0Yf5AVA91WMRdEDk66Bp6FR3MntwRq6tpQZcdgV7e04I9N7NJ7ozBz5ZqVHJ7ztzSD-gNG23i0EOsqDfkX1LlSv6Tl_kd5SusYyWqHaHw8WklzwYWikqGhwEQ0Opqhaf9IKQ2k5fHnCQUum8PeG9WI5Ht9NJj6E1Wb-f7O5yyBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa86e852f.mp4?token=HbffHE8z7jRnNwGlNn9bZqOALzhTLn9-p5Ub_aLSB-S8evoJ1FF_Ryjz4hAqhSBtRvkeiBHQZSJDJ9HZdJtS2ODJUwfgl-A4nYQRiCa0Y9nlZ-s4uWHzYb4um14aKlkrfFnRltUftLcnp17J5NufdDmkL4AWWG0g678zpg-kj0j0Yf5AVA91WMRdEDk66Bp6FR3MntwRq6tpQZcdgV7e04I9N7NJ7ozBz5ZqVHJ7ztzSD-gNG23i0EOsqDfkX1LlSv6Tl_kd5SusYyWqHaHw8WklzwYWikqGhwEQ0Opqhaf9IKQ2k5fHnCQUum8PeG9WI5Ht9NJj6E1Wb-f7O5yyBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرد‌هاوقتی‌میبازن
🆚
وقتی‌میبرن؛ لبخند برای پنهان کردن درد و اشک برای رها شدن از سال‌ها جنگیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22886" target="_blank">📅 16:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22884">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vcd_PqSIDru49Y584ixz5G43iegS9JcprvRtTXItpNthdc6P2-fGoiYaAFZVzJ7wGQ1zEpYBd6TFYLsi-yR-m0YgNf8Mc0oqJKf5HeMS9Vmk8bcCa6CTqwXdhgyyZcVZFbUsZXSziIINl0VJt23b1JzAf3O4jsYCbRptj2zWvSEo2fkdTwuw0SVCsd2Up_rjJ69zn3PCc0JK_SIw2Q7ZAQTkPeue1r7viG_ab4cC4Kgw9vAX20uBDFvAqpYZ0sSBJaiB7xLoyHlFpkJk8cHOAfkFtV-R2NWw_XrmRP-TQttCL89Ha_ohqBQSf9QZgWWkiTjGE1jF27OLpIKe3WPoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u6Sazz2TKP_LgXsFfPBmeaQbE2srjBnoxx9OymotdqBJx5h90k_k0i_zKsWRdyZEZ42sKyIIhRk9dDxAlYQz5_J4ObiUpB001_HzuavS5Okz54VHXo22lOM7kTF3SCcsVAlxX87zqHjNXdCsL4vmO-EoXi9Kd9KOZDWeznmcEPrdBqYPYVcV7kPUL_AAnu-Vecd_oqJE9jJp68Zzk6sh3R-fYllTxT8V6TEzA-Q2cA9FgoBbPpw4T5MFmzmsFhgsVStPRrZaY9NASpUXY3xZB6m94TNwnhqA1oPLoEpfll0SfM6U0b9ctCSNRCzSMORlz_RcLNu4k1zyFi62gOswdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🟡
🔴
#نقل‌انتقالات
|شنیده‌ میشود آتوسا یوسفی خواهر آریا یوسفی ستاره‌بانوان سپاهان مدنظر تیم بانوان‌پرسپولیس قرارگرفته. آریا هم مدنظر تیم آقایون پرسپولیس قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/22884" target="_blank">📅 16:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22883">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZtI0Cfb1QwL5Lj3I6wsJYbBIRrZunpCF7ubV1UZ_MQOnV4GhC4oDzFatG6Z8d2_m1-j0gFClWhbZ94ltzOvw9OHbajoi-WVp_EzFI_awq44Y5pd9y1EEp-UlYZ9VmEgUV03mmlSmnk-UXUVWIMrXCeP5qkCaWnzs8EFyF9Siwdje1qY3_koC5EoNnL3c1QRG-bxNzg1amnX5hED38zxhDVMZG_bmr38Wx9Aapr6mZmx4e5l5ZoePq5rbiPVxycq_qjPQEGnSL5BxjLdwZja9y-ZmOYy5GcMMf74xqtcuIkOSUKknLhWh-DzFia6g_3oWBgVDl8Uu3nsKamD134eUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
#تکمیلی؛دولت‌آمریکا: به افرادی‌که حضورشون درجام جهانی ضروری‌بود ویزا دادیم. دلیلی نداره به تروریست های جمهوری اسلامی هم برای حضور در جام جهانی ویزا بدهیم. ما هرگز اجازه نخواهیم داد پای همچین افرادی به خاک آمریکا باز شود.
‼️
مهدی‌تاج:اصلا درخواست ویزا ندادم…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22883" target="_blank">📅 16:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtFI41GTqyvfTwDOT6Re6Ecr4MDldmJnSz8aXP8Dqk7Pnsxqb2sxF2iQRxOvobD1n9cVMxKUevjL-dG5-rewMM-FFYmHKFLXoAwTbxj8bif3fYV5C4jcSimasOvz-sEc_itp8dOoDHMKckE_K5ZyIPu-FR6-n27mxKnC74IVu2KO4QbP2BBJmnsM-K53djehZzc2r9e8KokGF3clRD75ylsvYmwAZGlULEwuczncEjnzs5zqM8_0KMVsgbmo3m3N2pcTrJX5HxXQY3SnUlDq5cw3osnibJzdr1WeegHddoopGEUpmm4FtbbEYj4DUsKaHkzGGvgSJ7UL6qwv7T_vFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ باشگاه روبین‌کازان‌روسیه به مدیر برنامه‌های کسری طاهری اعلام کرده هر باشگاهی که کسری طاهری رومیخواهد باید مبلغ یک میلیون دلار بعنوان رضایت‌ نامه به‌ باشگاه ما پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/22882" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyxIjgpwhvaYRMjjEQDH4SgP-2NqtdWiKnIOgcsEeR5LKCjMDBc7klAEUmlvWWoMW75wDgvuBw1saBl32aUiaTtfg5Z68WSFR4YmYbMeYXT0UwKfexPGm-FenFp7ocW-TbQQE405j3VMFuln_6xcOMyU-Kcygu9wuhw6rUp1u4LpR2CczQ7VxUdNRrqf21orjVQGsFxA3POZmQmbG5J4L94nk2b-rqQTD4r0DFXGhLq8BGZlDSpEuZBTW-mxJmEQeufvcl4Qc1KKIxDiDsL5rpxFseu-ChUYMC4812c5kAo5cbWz2QIJ65ZZVPambY4mCFohHDbn6u7S3mwgNDdS-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/22881" target="_blank">📅 14:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22879">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HijeGjNXjxi7ObRfz5lOBpJjPPLwFBEQK7uf4kXNx5iTgOWXYdlChWnib-lfcJ7kBkrbO3CXfo7nUqHm9nuLuyeZFRghwGmgUuVoqJWSiC0ZtdbNWeCGLdx8II_tcjAyMWyggggBgJ8cbq_6bnFgfd6OaePcOr-bLfGc8d_nlspxha3s-KoqRwOhaub-HC85o_-atOsA5nj_4A87EwKu27zsTD4wmnE8lZit7pv3TmKxaCmbUQ6TkABYIf5vrKOm9H1fyvMZuX8CGa4mRsRN8zMKQjsu8DJjB6otYhilDRz9miMTECDDXov-xpEML5GFGWhA5AcJWEUmTMVsLDTVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTtRS_0QaMpnr5LuUq3_LpHSW9pH2qn5ZHk1dFUul6YkIKhVyQFjSjxJEpOzDDxg_isFgLkcPxhbaTLaQ2rOOSsiC5Fr6bfUIPQRBBL7yGl_hH3KplaysKl1gjNdc1AdFGLGCF4eSo3doIDOnFDshZBjcbBGkFgaYOtLcub54AZt-V5ZWeaQHkZjchf_IqTSO7_k5Dsfo0roOAwf3dlIDl0yE_xvDL5l_nSPVpE2GmKXcouF9JD0IFR-T7y-88DkeYSOZukl9Xozx6S4LwH65DIJGDrJuKn1CIkhLaiAhuesmjchRRPrqkmin1txCkLcPrrQW3KYHpZPuJKJ_tp3WQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
خط حمله هشت تیم مدعی اصلی قهرمانی در رقبت‌های جام جهانی 2026 آمریکا
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22879" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22878">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rm_bQ5rJHumUVhzp0wolND_jkvNvJWd9l-k2A0X-rKhfc9OwQgOEzt-KcMv1MnHhWEeKJGnCIhnUjILQkZruB8p-yupkmNeu0Ebzn36f66wFDtBcoSo315wf3CSx7iojoikfo9nvnTRi4xMQ5_9yWStiMDkNEpo-nL1Jq0h-qsLClchmHbgu-vherymtvnWwbZ9XG_CaMIPUDRvg4DUnbCUc1KWjTEvq-X1PgCbj1vMdlEcPFT_pSMcxOaayi1GCE0wdku0lP4PedRqXHVwzzd2iAorueJMuUcyhmeWqy4MIDJTpwzJnzP4MBuFrY8gUox-8Kxwe0EPD6j3goamURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/22878" target="_blank">📅 14:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22876">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRwfHHkfowt8W8dmv_cla-jj9tTX3AKqJVIg6F_5Cm-72md5e64AtbJlDezhNHUNi5SQWJYresI8flwGXL9_MqbLXrbtux4ThfQItiVv5NGg8cZckp_PmWfM7yRZAb21nAzzsYoVVkntGakqBHpd0Uu45IrvlJKFS0YvVH81nWLC3Njg6Fh7xViC8fCgHG0u3k5m_-FMR9oBSQq7jzmTbl3eo5YFFsPs5j8zPY0CLgDlwBenpK5MghLKLlGcaApIDjbi1PUZE7HfjU923wnrwUtzUVpJsYiQFRgu1xuUkmWHOFIQ9-2ZZRV3AQCC5gKL0ZMbNzIaLBRTYSOhvqqcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال با مدیر برنامه‌های موسی جنپو برای فسخ توافقی‌ قرارداد این بازیکن‌به‌توافق کامل رسید‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/22876" target="_blank">📅 13:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22875">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=hsAjTFqbxMhdsgw3MVrzcgSpSNirEt00WWAoXFK3i2VuoA9YrO-xdNuQC0eToNdrA22zvaDdRvLt5yGauNnjqkoLN6QC9PcH9Hd9fLMpgiKBW1J5K2xSlPaivi5R3lVCyjrhl9LpX4FH1rDGxefhIpx07wnADcS1-UOYxYf0J8REa5djj3EL-CyLZan6utHfeNzVYrBW6bU00l6SVwnMR6azU5EZeR7-I2MunIL4Si-56TtV7xJUQBIXUJJL9FUyw5roYnFUCw4qrHX208okPt0bDP2rOR510SlWYN2hKWMOzN0sv5VqqnBIbsiUloGqjpdg9ibU0OlMhc_gUU-6hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=hsAjTFqbxMhdsgw3MVrzcgSpSNirEt00WWAoXFK3i2VuoA9YrO-xdNuQC0eToNdrA22zvaDdRvLt5yGauNnjqkoLN6QC9PcH9Hd9fLMpgiKBW1J5K2xSlPaivi5R3lVCyjrhl9LpX4FH1rDGxefhIpx07wnADcS1-UOYxYf0J8REa5djj3EL-CyLZan6utHfeNzVYrBW6bU00l6SVwnMR6azU5EZeR7-I2MunIL4Si-56TtV7xJUQBIXUJJL9FUyw5roYnFUCw4qrHX208okPt0bDP2rOR510SlWYN2hKWMOzN0sv5VqqnBIbsiUloGqjpdg9ibU0OlMhc_gUU-6hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/22875" target="_blank">📅 13:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22874">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kiYAsfKNsDVyJdbGGV4wC6_Xw0KQqqrJY-cVFqr-dQADh4Nt9h0lNDmlvtmzrtFOqdGTKG3D3P9UgeRPJzH_UAjcXkSEKMKa9QoCu0zUSAY-yxIfng_Md1F7IiT7fvZ7ohupcxnr0-SB-PObft9_nb3Obp5SLDOLs_LSJUg70QT-4e6ZGigcoGKh0mH42SUKEBPHJfN8VtoOqBXYcRVaNCUo4POiIVlz3s1sSXwvJCqTG7TSLfjbwugRtc1nj5cFUdUiKxgHCG4NBnVyutRq-LrHLGOe6vu_xmlcJpR9k0yuk5r9J4efHXUCvTbkJAmENhAfxZU_5O6Cjlzt3-lDmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نیویورک‌تایمز: ویزای‌موقت بازیکنان ایرانی برای حضور در آمریکا صادر شد. ایالات متحده رسما اعلام کرده که اجازه‌نمیدهد که بازیکنان ایران مدت طولانی در خاکش بمانند و تیم مجبوره پس از هر بازی سریعا دو ساعت بعدبازی‌آمریکاراترک‌کند و برگردن مکزیک.
‼️
همچنین‌گفته‌میشه…</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/22874" target="_blank">📅 12:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22873">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8AAm8dte3kkg-d8fjc0xQ2DTID0jeOVAK-94GY_xXJ8e8HX4y8Pvuhl2BNstYoNADlfZqPW4S-l2RMW0CJxTTDWl9USDlXScoEcM4bsgi1QAQ8hZopl2vux57xJvoAwzZdHSmY7709LdyTnuLS45jcrTTvRwJ5ZHWi_YTRMzezd3dHX7jb3-zC71zKg77tsk4m2_jk41vZ3FLWM9J1Ue48JJe3bHEXU71vY0_UCgaIZWIa64HOwRikdsPPrSpYDhgx6MtxMFcdcR6olGlZyxE0uUbTgh1u8T5K9HyXqU6R-XfnqCSErx3JcEv4yEBXmt9DAV0Uh1Fmf2KL0l5iE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
#تکمیلی؛باشگاه‌آلومینیوم‌اراک: در روزهای اخیر مذاکرات مثبتی با یکی از اعضای هیات مدیره باشگاه استقلال برای فروش محمد خلیفه و بهرام گودرزی دو ستاره جوان خود به آبی پوشان به توافق کامل رسیدیم و به احتمال فراوان این انتقال بزودی رسمی خواهد شد و پول خوبی به‌باشگاه…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22873" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22872">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPRUxS46iHo1RjJBVqxwr-oL5X_dB8gfG30voYREt0CSBnsuj1Jw62DYq_ud9YGsknsmwPjJTEvs_rExiehk55dslRdeKqdBbbzP9mdvGc0nzMkxhiW_2Zj5Ae_2UPCGWpB1l6OCbkU_rt_n6OuimjowJGmaGWUshYseNe3ebZTAtO4CqegmyUwgEWB5EibBUEbP5_lOWswZ-S2RYUjyFUtCIQU3NmEuSaBAn0xZ5-aDu7qZquLtfCxLv5TRi77NU8n1-y00b-djX55iSdyfJELK57DYvrz2qAawztP-c4Tb9Ru9XPl__RfCgsytkJI0nY47SM2qkhr_SJsy1--kvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل‌نفراتی که دولت آمریکا براشون ویزا صادر نکرده و گفته حق ورود به آمریکا رو ندارید.
‼️
مهدی‌تاج رئیس‌فدراسیون، مهدی محمدنبی مدیر تیم، هدایت‌ممبینی دبیرکل فدراسیون، محسن معتمد کیا مدیررسانه‌ای، مهدی‌خراطی مدیراجرایی، مسعود اردشیر افسر امنیتی، مهدی ملک…</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22872" target="_blank">📅 11:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22871">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEtIbRj3DNKa-N4pmrtkYum7CwxVyDde9tT_OT4ZBg-btBu8kG1_xBnlMFdEM6JInnb5QVgJ5hxiwo5-tiZWF5P3WBTEkb3o6P3WxP2HboaLH0Bir95PKQeKdI5-7cjJvUBLLjallmpzfYJs-5zlr4TIm-7C9jXiYDQmHmkpsy0zsRzJ_PnbJAaaZ94Ex_5yzt3KOooRIE0CHfjzVxwkZsIVhwVppZnQLaPSbZ_Ix2bCfpHTXDdbSYVIPEDrfbcW_4UusxVoWVOY46Niz3xFKfbtDP6ARBsIF27XZCuUeu-oMF9em2viG_md3eL0vcFbiXvT0y_-LcDyTI2Buto1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ تمام رسانه‌های معتبر خارجی از غیب احتمالی چندبازیکن تیم‌ملی ایران در رقابت‌های جام جهانی 2026 به دلیل عدم صادر کردن ویزا از سوی دولت آمریکا به دلیل خدمت در سپاه خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22871" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22870">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=HO9WCFz9vG4Lj5mVwPKzWO5rFJweKxOVjkBjU4qoUatHh-6G2woJ0mRJBDK4wY_sU7J6V2p8s6A3t1th55EBxSENHVR9tbQ9_eDAKKWcFFKrrkG8BgTTd-Grt9bpLLJ24LTkW43b9zP9xNlSxbXOJ9ab1cUNx52fAThpK9pveOc6hPx1pKoWbFEwkD5RBIOWAPN_1phFwxFjt33sBOGcNhwX-uOpnJ4hAtB1Nirr_xBZ1YdVjgSlMss_4KD5-g0aqh2g_uM8Gx5A38eH7UP_6TY6BQdGPZWWJg5CIogq07XVjD2H2kzs4rP4n23CvbvtZLo5AYSwE23XwcCim9yGUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35d2a48cbb.mp4?token=HO9WCFz9vG4Lj5mVwPKzWO5rFJweKxOVjkBjU4qoUatHh-6G2woJ0mRJBDK4wY_sU7J6V2p8s6A3t1th55EBxSENHVR9tbQ9_eDAKKWcFFKrrkG8BgTTd-Grt9bpLLJ24LTkW43b9zP9xNlSxbXOJ9ab1cUNx52fAThpK9pveOc6hPx1pKoWbFEwkD5RBIOWAPN_1phFwxFjt33sBOGcNhwX-uOpnJ4hAtB1Nirr_xBZ1YdVjgSlMss_4KD5-g0aqh2g_uM8Gx5A38eH7UP_6TY6BQdGPZWWJg5CIogq07XVjD2H2kzs4rP4n23CvbvtZLo5AYSwE23XwcCim9yGUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اجرا‌ها و موزیک‌ ویدیو‌های شکیرا برای جام‌های جهانی ازسال 2006 تا 2026؛ کدومشون بهتر بود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22870" target="_blank">📅 11:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22868">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMhgpF0dlg5xGqBxP9ILxbMeqT6hFFamyIk8XaXV2HbMhhQNXWCpzL5-Wm2p511TCghhq4aupj0mZHiv53eIV71CBLKG3k2zK8x6C8R0dVO0tB0Bk3bErak0234qI9EG6qUCW4iEHmmgyRE5rsUNemlIih_6X1cl0AZ_Oa6SjYvNJKX6WIo0lEDJunu3_fHfuzhUuiKlA_e3LGP_Ty3u2vkmWtFXylFNeGQLAiYd_VX48PMCSGek7Ge9j3DqWgRxWaLHQG6VYvnIKHRf78XgU_1lZ8TdUhGaZcjI3RaEEq7MCXFchkDjMp7OulcNmZTF-Ltz3fZNGPB1M6J_0X6WOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ظرف 72 ساعت آینده از لیست اولیه اوسمار ویرا برای‌فصل‌بعد پرسپولیس رونمایی خواهیم کرد. منتظر جوان گرایی و عوض شدن شاکله سرخپوشان باشید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/22868" target="_blank">📅 11:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22867">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFmrUnBwXZq6aODBNkVbPKMby9JVs_jGDu81NfxnF7DBmnHlWRwrTFoIRGBVbKKEX2YpzE_XW9wax06s0-pT3HPOrdjMjfsn806q1zZSlLKAkE0537BkKScFETSRwBdkfEAxMChISgwpHF3G_uM59oYvwZdRtnsrFD3kRqbFMt0syxRa5_IK1WIOK6bHs0vNMJ8mpVUF74usmpe3DyyTOF4yXCaYRafLUsk68c_VwYMLeA7ztZ2qszNB8DR_Oe355s_cz0EEj5opXg5lOfKUkod_kIV4fkdn_yI4pmjlLDycShMOvKrLTTgWs3MHb846g0dyHeP42IiM7S0lkr4DDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
#تکمیلی؛ محمد جواد حسین نژاد یکی از بمب‌های نقل‌وانتقالاتی تابستانی امسال فوتبال ایران خواهد بود. حسین نژاد به ایجنتش اعلام کرده قصد داره به لیگ برتر برگرده و راهی تیم محبوبش بشهه. بزودی جزئیات دقیق تری در این باره خواهیم گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22867" target="_blank">📅 11:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22866">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=KuprLdGTbVUg4eNrTSt3rlNTkBnANSJavxOnkrHyiXRPVaX3aI8YLsxM1H8NfbMMGXWLTi9iZqL_YoI_ISykee1_4TB6D2DcEwybwtZwmDR0D2xL1mRBAku1nhNTsaXPzPASGtUBym6Mc4XnrWUjLI8SI4Lob9dOhREpD42ykftQoi_U-sL7ZQ9tfKU_rLdRlicJuKC-bHp1Edti8A2EsRT7OGsgMkm5m5-HaiJ4BiJ1qQXsj743DLCuSkEDV7V_F-NEswced-47m_IB2EH0F5f1_sOYiA_kcrpWlIIQYafL5abT-EEHItA-7cbwIIaAcXB0Pcs2soysbzrCf9MjFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47f6fd1b53.mp4?token=KuprLdGTbVUg4eNrTSt3rlNTkBnANSJavxOnkrHyiXRPVaX3aI8YLsxM1H8NfbMMGXWLTi9iZqL_YoI_ISykee1_4TB6D2DcEwybwtZwmDR0D2xL1mRBAku1nhNTsaXPzPASGtUBym6Mc4XnrWUjLI8SI4Lob9dOhREpD42ykftQoi_U-sL7ZQ9tfKU_rLdRlicJuKC-bHp1Edti8A2EsRT7OGsgMkm5m5-HaiJ4BiJ1qQXsj743DLCuSkEDV7V_F-NEswced-47m_IB2EH0F5f1_sOYiA_kcrpWlIIQYafL5abT-EEHItA-7cbwIIaAcXB0Pcs2soysbzrCf9MjFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تعدادی از هواداران پرسپولیس مقابل فدراسیون فوتبال جمع‌شده‌اند و شعارمیدهند که پرسپولیس رو به جای گل گهر سیرجان به لیگ دو آسیا بفرستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22866" target="_blank">📅 11:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22865">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">▶️
هایلایتی‌کوتاه‌ازعملکردخیره‌کننده مایکل اولیسه دربازی این فصل بایرن مونیخ مقابل پاری‌سن ژرمن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22865" target="_blank">📅 10:48 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
