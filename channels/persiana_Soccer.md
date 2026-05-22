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
<img src="https://cdn4.telesco.pe/file/jGZBntk1z7E9aoCPAGexeVORjF1OgpiRDnmi9an5NVlvj_2YTlnKEfG2-puF8Nnmmb1ISvj_aer-nWmNIj4k0HgFdGJ5qet8kuzSSJrLAEscalST4fAPoj78qbivSdnPxIeS67weF9XmDDdNlupnrafQDd_O9MsIKrkmuPHbIrHDlVzYi9JQxY7ukWc-NL3CzQJpoWA9NZvcviGxhgtNHhWc3BEGYYW_20su04k9ENODig_S7FWj-6eFqi91sS03xwF3Q6ayY1guSARyrqhPN5x9k8gdLC-hSJ4aN6HuJtLC5v9NKAVDnX8RWVzXDbn7bex14gpML7rIbRYS06mDNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 199K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 13:48:30</div>
<hr>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-EpLWKuf0SXX5Q9g639JYCYs2WMVjLbHIzS4jIrFdhVGsG4UieZ_CQS1qrSpVzUJXByneCTRTp5rEZwMVT8bcL9_XmUheYC_ztvkeLUzG4CLMuMM9lIDRm4kFhru2-v2gO5RTgxNk-cF-GnXZimYky_6VwoqFeD5U66vSAyhHYrjkWRRA7in11fL_UgyVY-FD8c0rO7dTTPhg0KWo19BpSbhKghc-XeQ8M1O5NXFQNh58MncBuziN2QC9_wYUtNpP1LaKnxl1j3gVZWMPFWc9MhQyltPorTbHuQH_GLIgVdpN2DR1mspXcjac_F-YgQiX9JrKd7EQUSj7E-fet76w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6iTacoSV1zuwQsabZSp7cWK4BrheeDLmto6NSLyl_eitLDy9FxG7jxjTFTyGaMsCR6pqfB7TTvnIcTfGBx-YGyJWndoawxmyS-K2OYy6qd1i4S36cUz3csGhgxQhfq1ikPQKmeKlTObejnpHxSEtad-uw0BP02q5Y6CGpFIWuLAlftJ_Rf0PD5Y8rElctU5mkhO5nGURL5F9G2cbg2yprOtPADC7mRioXoTFKRPfNCkrD9F7ayF9WYojeZ4dxf8IcOFOWJNkrRO-_ZK4fuvC-yfQQWrIPapqQp7o20TwjJi1_tXkLdlMHHd6ygd8oKxUW_UJU_W3MLbkkZuz6FY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpdEk8RIsUUp4mbJJ8n2NVWRUvFWBO5HVxl2oL5c99cKxjtDuQNfupxZkMjBunVulf8t76P7GGTLl10fBhmskln8jqURMQdd2BY2w0tn7CSHlSmSUP7mH9xPMfnaAo5bhda1WoKXeoc2QT4ya7mijQLlMnDyqX50yyyj9KogdLAt-Dy6RmgyaCahEXrBvy8fI8XIT2jE_Az9yUXTotxPn4gzJiDIvhrO_x92Nf3IX06PjaYRLSXyjxB6KX594tmgW1HuixbIedO_qejaqs2i37utBRnkJ3GmcqTQbSdQvmsAdd2ShIJ6QF3tJKUqRmg55pTL6Gb4171OyCQYiATbrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De8xmqfelYtdE7kAU27yM3upHLGRuIAVu59wPDEBEnjINldTeK1oMdOKl3pkTMToDZSm8OT2rjl1RLFRLmk9n_wcHL8OsECbcaQqcn4BOMKN68OK1kjHb4KCH2ZvFl64aGfx4_UUIpo4-ScdBhUYowIf5DCJvm3C3LAnze9vkStEmbvglIS-vWQwFR27usI05W3BAxiJ8OZDte4jFRcKw3_5FkdI7pto5zUkwMT0DgH3Q5Trt2LGKskP8JyKxp7x_xuFnrNSGEyHhyPhFigNRHnzptFkvpGSLqd86EygEKgW_D_gVrwmaCmvc6YRndFTZLWYDSjJD6yODHty3Y5dZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA6KKRUXJsVzi1aexljtT9b1dyuuES9fI31Wo_RewXu-HJ-5MQpLOupKZZRaaw_8ZEvcfRzpgkPNIGrbw5yMKg98mndSLP2WTcKBwYgXbfUoL7qeaG2_eXf5VaMQ4_d-Z8fo9HH7iU6PyzZNF1u9M-qtlYjkwzriLKCVhb3I4RNTGreMOeRixL8_SsQUyxqr6GkjEKaGCfaOnsfukpAirF6JrjlKIo7-HZ4Z8P7bRaMQCs4V4qJeoRhj2xKlk6uf6GA_qSDnVW7Ufn5FttpvAxfqM6OitjF_msmU8BNp-fMHrS0yEOyhnmiXV9m5Gt9ZVsN5KIX844hHB0pepobqtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqicYASW9B9T3Ua0z-s9Q3VVLnasml1uorRuw7W5nJ0QuiCLQTQC8K8aRF12PYIr-cXIM_l8kq1TIcGrQ53b-QJK5NnVPBrBW1QWF6z511HEqnOpVm_SJ8eABnameckWqNk88Z96LAnHKFXWoRLhVO4JUNDiR2rURqGCVbbNRJAOe2mznxJp1vaz93x_NrLNUqj3LEBKrn2m4Q3M_J5zZ8HyHaSOZPfrL5Iu_L7EUNXa2TlNIM7FSq_CiSWnBkPV3IJJ8rmnZ-gxNlg6o6LLwKzEgKnmhWFLuJeYiQFJ1JuNPYs1ppYLRdLJUN87dF9AklKbDhgv_Wkh5K0JD4YhXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRrckIYxNaYfaa4JXCJDqIXmYIshKnxbSpRaRcY2SqN227CUrQFHogFEVG14CAj9dTpe0Ua_QdnZeYXqwy8-F6-wS5WDD2FTT-wK8TDgN0WuhpoI--JwM68O04KEEmBZjNtMN1QDuigskpnXeiz0vCfSE9yPnapbVjXqSNbG7oTMQZrI6sA3rqupW_B1wiiqOiGSZTsO8PJjs4WAZMwpi5LsTUvbS0kMuj46ee5w5cET-xYE7UwSGlqrO0wH3VjYZJd-9DgvQ0DMUF9IJ0RwqjVUYXX6nP8hy5pBZo8M04XLCmvLowvsF8YcsJRP3NjX0EPaDaBufzVB9nNebO7ZLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIZK7PMtCq1XDO3-vpzC3d9WMQjWa3m9UXCRA4Md47dVr7ZfSear9DrVXIoH2m-Me0MSNvfSOAL1JdsifWUxPz1B15g3uO9rKh7Kd9lnd589MRveCbcXHLyDxtbZBNdUujkLbmvgRJtFXlOk-RVdQdHRjj4_OHETkGkWJQtTD_jlQap5LUZbd7WByueGx42WO8l7Rngbds1EWISKdMT-bR_7SlbfV6PzICEkoUtjewUQXMquZTHkhvf1Wyloe7WzxnZxmrDN1XiaItmGwEJR80AeMEh_bzw_zr9oclqFqucxybj8uUehsqXjM1d1hYcXBft4PDYbYlGaMQgZb9HLAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg4IOQy0Kd1_9mlj_lfwQpqnrprn0od0z3bqfhZZWs4kB--kCw-bUZSPI0YILtLI01Rz4_Io5d_wqSPBvYay6BBvCRA1QuLBNuGmzE8VMBsBQaajK9DiVxIq7xUCZGM10LIP7FFAi-dry2U8i3oro-MFSmR76tU95tzdrMb3IBgMsxipgcBaHvG8yrEfeVdM6tY4p0PFEO1amSmRe3frBU9WXvC1AeCo_AgqgqbYI4eYcbOgUMmtcmmPerzEP9Hvsg6uFkOxwtxhvQv99wGX7t0l1ihrQjSJ8LLMqagaEg3KgX4Fbj_DAPtX1C4P_7ISAl7n-_zB38zrEdZxGY6zKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlnjSF0k2tsgKbT2I5qzdoW64vdbAmAIH9yCV_xV9iy-WPTtXEzCiuw179FBsRladpF2dYF5r2BPxW_pJ-iEWYJiq__Mre-YWmst-HXqsL0HXpfaXr8g4nGgpVjO8ETwhAu1s5kRpNJmdBk9DTck876_8dzM8iN7OoR6BaQ8VvdyvhMu_BDHFtQ1pZXsSm_yi6M0OPfmfPE-b8gQ3CQ-Df932tDHzCc00DqTPfygLkp28e9HNsalU6BYYHkTRprXou37c4M19iJn6edZ4lUouHZRzgaMF9gSnWLGocjGBfT8IVa8ocdDGONaTOT6PINT6x7cpNIuww0glrfpBTWrvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22227">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JimHe9JIaMYKOTnZvCI8MfEeoXoMtoiIRcDfkX8N1_Y0xKXlxOOX0F-_SQPKM72njRkWXN45E9puydiWHp-SsaKbPPMvYQq2wivRDk40Zgi0qM7OwE0dNKZPcgNyDWy0gZ9gTcPllhZ2t_y-VTNixw_iFSH4Y4jZt4xtzeKTVY0pTdsUC0bmVVEjXDlR6ggXfDqJaEU1xHe8-7XxFwNFg8AzIzfIU1wf7aLQMNLYhVjrjru07oM54WC6SdDrLl_y1WLjax6ci95y0j701NUh3nxNWadI3GObLk1mAuCMmZZSElg_EyPMw1rbxdUYoCwrjhbRdKbE1n8U-FIaZj5oWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چنل ما برای اوناییه که فوتبالو نفس میکشن
📹
خبرای لحظه‌ای تحلیل، حاشیه، نقل‌وانتقالات
🟨
مهم‌ترین اتفاقای ورزشی پوشش داده می‌شه
🥅
یه منبع‌کامل و قابل‌اعتماد دقیقا همین‌جاست
▫️
https://t.me/+XdSZ8OmU62QwYTU0</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/persiana_Soccer/22227" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYXb2qaeHjZCkfZCX6ux_uYGsr5IAM_GzoR4Ydxoncwy7zBGg_qaPKkaU1qKWUBw8qWh9uXBdmeTQyxWb1g64g6zYzzxHKlZbg6jNTfMGTriGyuNuRX8poscqIFISc8UjJXfiH7Yn-D_5mNgXMm5TywAF8X_MeIuEUqzVulGqYwWfNHfYmHziQL6hKlds7HwYa-2My0NBHgxTOoeir3woaUbN7mDFx7WHNltQ8vlEAXSRVcoA_DpZoUhq5Sed5yjWWKd95TC5Mf7p2k14SHH6aRR8sKl1-tjuws0X_3w_0MVH8qjFDALntB4OrRChl_Lv0MVt7sN9Tvdtybzg6cfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfQ3fHrwdAwA7ID9ojM92JvHzuhT4bAVFOXpkKmJls4NombMD2vXcKEQ-GxKiSMdBovAj3HzertCMsWSpzrdt4v27_QIlLIPrfKXXE67ej8ZnBcreENOGDaebEYlbFfJbcikIIo8Xr3VNUSQQGryv4dNu3nxtcYXHpktT6DkWKjbWuZWSxAb8KHu1WXJJJO-KgMUbiW_FVXP9FSjGaFYrCVh2boSdjpLgdiqxY4wczNAfxlOtgf2nbfdNidgRDW9HIk8lp0TwNU7uR0H_2eqRlzCUhrgYaK-doOdezuQzAjh5vEvddqEJJoqa5BV3EGMCGG_VDsRG9Aonoc_uete9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=fxq8cCUzCXEN8KqEuwAikAckESdhuwLLcwfOmA2_-JYPvR0bLOO8HxFSTUGZdwvXW4LPT6m-ervpBsEgR9gT27LJJiyu45H_AOX_y7ONRHX__NOPnYfRXmryE_I72d38wA6e4dG1UuJkzvtivUCUEL-nlyEnSWwp8UwfZseUXDlHGUTEAq2gY05TbJqRWoMzvcGGeNdVnXGkcURbpCbp5N8nkK0TiSaE49XL8fMNF0oDIPAWr_mKj8Kno2vs5IhTrW5KFsC6aZivPIr-2-_JwXFQF7eUhrr3ufOW1lY-kaY8HBTevP0hI2b7vejnb3zNDnc6IYWNLH_BDDtL6ejbqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=fxq8cCUzCXEN8KqEuwAikAckESdhuwLLcwfOmA2_-JYPvR0bLOO8HxFSTUGZdwvXW4LPT6m-ervpBsEgR9gT27LJJiyu45H_AOX_y7ONRHX__NOPnYfRXmryE_I72d38wA6e4dG1UuJkzvtivUCUEL-nlyEnSWwp8UwfZseUXDlHGUTEAq2gY05TbJqRWoMzvcGGeNdVnXGkcURbpCbp5N8nkK0TiSaE49XL8fMNF0oDIPAWr_mKj8Kno2vs5IhTrW5KFsC6aZivPIr-2-_JwXFQF7eUhrr3ufOW1lY-kaY8HBTevP0hI2b7vejnb3zNDnc6IYWNLH_BDDtL6ejbqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=U3JNWoDuDTTayX8AZkq4YboJGAA1cnWQRMNc6j-maTc6W3HDK5WQxtpal-V_SzJbGMAfCDb6PZ_Kcu5hpaMqLHrqZg25WpFFhRHW7QLK4xswmJe0CkenH42nA6jjOAkF0KJqtNBkrozkFU1_uT_TbFDIuMBgc0F_8kd_UFy7YbLL__VSV94gYIhCbBbrwG-VIguLStdtE3IKn_SrEayqLQjA6yYDcuUaX5S3_ekZe_Il2TA6IM0I4pX5yjFhbET45ExZq0XIlu0pK8e4etTwb-6-cGuxvGAg6X5DxBFkHNSaMuIuuY2PTyOigdXO48t4fUSMxjaYhmslSMtKf-0NjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=U3JNWoDuDTTayX8AZkq4YboJGAA1cnWQRMNc6j-maTc6W3HDK5WQxtpal-V_SzJbGMAfCDb6PZ_Kcu5hpaMqLHrqZg25WpFFhRHW7QLK4xswmJe0CkenH42nA6jjOAkF0KJqtNBkrozkFU1_uT_TbFDIuMBgc0F_8kd_UFy7YbLL__VSV94gYIhCbBbrwG-VIguLStdtE3IKn_SrEayqLQjA6yYDcuUaX5S3_ekZe_Il2TA6IM0I4pX5yjFhbET45ExZq0XIlu0pK8e4etTwb-6-cGuxvGAg6X5DxBFkHNSaMuIuuY2PTyOigdXO48t4fUSMxjaYhmslSMtKf-0NjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK4yGsyvptFLNMWGOl4v9acUO6qHC-hpSPttlwkQV2kTNVejJ-RveOkEWWjxp0PPnIupEnyRoZEkWDU7qZvPUnCNVee0BD8CzjKeVbybwF4GahjqyxesuitIzJ1tuZqgcjtYB2EJVk6jxjxD9h_aeAtGouJ8JKtQ6UvPS6fD1SLbRrhnVsW8xxGRypKtvWq3TF_N_Wq0bIekeE8yEzCSsjx4zrDs_asB4CIkZpsCveBPuW3l8zOXpq-WjtMi3dzlbuzs_3Lqi-wpD-elMWGkE5cmSxErD22IzMX_jyszM7epnppfcMtrdotxl3zxqw0vRGcFux9GllPKNeVvgYNBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22221">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
آفر مجموعه سوآن وی پی ان: ( علیرضا )
⭕️
مخاطبینی که 10 گیگ کانفیگ از ما تهیه کنند گیگی 185 هزار تومان براشون حساب خواهد شد.
⭕️
و مخاطبینی که 20 گیگ تهیه کنند، گیگی 177 تومن براشون حساب خواهد شد.
جهت خرید به آیدی زیر پیام بدین
👇
(
@alireza_mosve
. )
⚡️
𝑪𝒉𝒂𝒏𝒏𝒆𝒍
➡️
@vpnswan</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22221" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtlVm1QYfhNa3KWryIxcrc9NmTACIHB4-IO1Se7TnR3CuJQZRyvim9uHtWmEwlTOBYWdhkukBAkQCTr2vdJbDaiTS9Vzrlqww551k2zhXlbeqlJoswjkOdxDSUUV5ZAQMJ5NNsSDVIjXIl4JgjjVI5h0wVr86nVK6HBjbWdF2aXapGvyXjWUO-FA2MvL3Qm7Luj6qAYKmTWh-Tj1O8awszQYMciPJVn74szDD3f3keT_Ar7TS4IcqenGJpN93U1DoNPaytpFNBSULh_qK4SLC8fD53sMdqPjbCfBJT3vgryngv7IFu7Wt54xcxkc2Bpr21LHuBRhGq45sWfICjY4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAFXt7iXfpxDy8d6CJ2EWwkApA4AwmAbyQGRlK1t7FQD5kghlvyDYUJME1ll7L_FG-pG-XgH01yot29yQzRp1tKLdpJxtY3ayfVSkjKoGP0dp0U8T3Jr0E20jC470d7Pq3QqbDrQzODr_xLaZ1UJTNtcYE3TUvpRYE783G6i86sQn0lHZAqwHy1tO9rnCayRJKd3Ng9KsADIbBX0c31yGlKAHe2nXe_eQhnaVzpIdUVHvBio5Xd-1SUcdGjpMjv6UzDVj7SHi6EbO9tCWEVADy23Vy8o0eymxu5xTmIvbfRaUdUwWrf9gtc8NLSOd0vavEhxROJjiUevbxN0oLR-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCju_4Z-xMDrb6p7rlB4pTsN2mnw03A7r99xYGWbtBC-Q5LBK2H2YjR_ieooKqbd4w2BM4dj8sSu-Y_Urhr4ErBX_9cGc4GsQ0NgxNajvSr6gSlgouGpcfjxX6Qtt9YarD_PGtQCwuSGZhUxiGOvjejmM4ZZ_gfJkZz0_toEDl7OpSoZNKDzz9id9ldjhIEGPoa0ZwSYEo71g6OprphoVUPaSw0p7X_SBUOQ9JmhXvmBu4LRjpHCNJh2kQJ3xwsuQvct47HrRhTzRyj8OgY_CeqYwwZnqxDVuI4T9c5R66RKYr-0N7D02nKre-I1toYn8RFnFZT4xnCZIX9vJkB-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER9Bjgd1jzDYxTgXpIihhIE4C9yXPruvLVTdz8KtKL7QT4cVyiTTdIP1rtdGDNrFvBUabB3VC_o7njE1h0KnizWxG0L5yg_dcYC3L03PCVjVVUHV4p2qhG9lvrgJMWik8VzfEplnHXZsGUJDk3GT9IvaT02rTp2_SkXrN44rB-332oCRHCDJRPO75zITxoBY7fe0rNSOxAp1XPO9WohMFSp33_i2_-96hzkp7ypFCgXDblroZiMwzIeJpfjDntNiv6M86Z1sP7gL-zQlqJDbp7HYXgVyJwA8gVokyxYhubEFE-ouqZnZrrNrv1dG9fdg6iRPnlEITFFSp-vb0viRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3vMFgAmKsYAIsaeFYMFh1KRISsW_xVaVk_IwcEPB770zusdv1tXQY-pXtfHxsNXZL57yXAOOXtWMsJ8tisoGrOFWyHgsTUD3b35v29KOo3Z9acUNSil8qI1u1fGWazwOiXeVeFajER7nC6ezfbvuKr2uwzevqQ8Za0gPsWN6MdH1pPFrHm_r3W6HZJtnUhnSYPfH4FIhp3FuWNOW0cgw3mR0i28TEKEBrWQsefiB0hX9SZ3MXgW-UdnG0Esd_TCecy7vLEkoL84-zfWhOzxYFNsznq91B7_YELmWi0kbDXoO8Dy9kgs_EAMR0D8u4G9jtH11Bey9OeuuU94gn5UgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nEnTV2O0z4KZ5MulsXJQ-nXCN_52z1MuErezVn5uMmk1K7vVdD3jb-M3s8e-D0AJ7U-OGxBoFnasqRxITwYcgCNCeN_Cg32isNSGa9SMFPDOixLXUeeVlIxkyH55CXsr2sjGFZLk_Tvtcu5MUNhhyvVTef_SFxBUReHPlSHaFbaqbPngucE3qx-ywrmG5FJU4n0fUp8I9HtIk_PptKoxJi1RFmhqmKX1LTIDAPRd2mIdzaILb8mw10r6n9YAKXMzbeR0jP27fV4Zr_HKTGicpRbZU9A-zmaiov2tbRHeiJv84xYxQAVPhB4nyIvBDJTrU1ikpwm71xA5yfoBGTQP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TEb2SoDRVWaWCOX0J5SRnBgG2_QW6AUWX1bVJYg12829DwgZlu-VtTV4bGKHZYxMqXTD7jdhszgq613-6PonLolCKQ-S2jO0yLiZ_KC9pqNBrNor9JO_0Vb6N6ML63i0y_nWk8o7nn2RWy3r9rvdZh7WQfOAOp3mFaX5bKktKT4JSMQ0iItAlvzpOci1uyuYK6xMl1Iga2ByeOGQC5XF8SkPx21RCv96xOQCvBF2i_wHrfngpPjnbzySQ6pRo-tunBEss1Fwa9zE1RSbznSaLHkhMKySRNWnTL8GbRynO8h1e0pNNVjO5PDRWpJlMNZSfz4sIqxkfx8SqjZO_OIvXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBX0LEFz7weFXZSgLiOjC16E2Flq2UuLo1sKhgO7TIp82j7lC7Ca1CjBwfTjNT55ncYxRZiTDjLADT1Mpeoh5YBT8thwNP3-pUMsNPuEm5lpKcwot3s00IqJMzjMQsl6dZzpCn61Tpwb_a2662jzJjIHTr1Zcr4AqPlcUXoCCnjoCwrzvTvdmoW9YljzCWw3beS8KqKh_bYUvljJEveoMsktE8cNKNz4IOipF-ZQpOG1OSlO28Hbj7vrsZBmm1BOVP6465zvab9DLdPJsgT7IkDuEibjLKfshQLiyAvDubfGg-C7utRA8qfkxV859YEvtkHnSCGUhZkY7-OBv6O4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOU1qMbPZDydHn9kB6BVyRWOHEJ1ao-urnb4NcKsKSy2S0qt3aIwI09tE9_B8yWGarbuipu8_fvpH--YMLZBNnH1TpQMbEr85G5E0C2X7CI5IBHPaDUS4XpIZrIEpCrikxaRiKB8MLEJvbNFC8jGZo8gvatdC5j8ROKLqEPhBnKssnrAWBDX5QxOh6Kflc4Nir5QzhBQV78uA_Q6q4Fyy7P4HeqaKNJk2hrna12ub9ty69IaLljda-TuymEwwo1X38IzgB32J6_q5cINA4dXH7AonZTP-tcD8vy2TCi2MoWFHdODe7ccPMljIOEnAN2oYg15q-PDsJaj0ikbfqnPsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1hMJKNeV93V2Ao4XfzZ12PbvxjTnnmOYm6gA94gg-Ll6R8VYBvAkOGv_Uf9koqHrIIoSXamOWv63NEc_J6EtFQVH78CgxfFRgOK3ZeEHqofVHyQ6rhamJl0g1qW6qUX8C92rjGZ14T4FNkGEnsLq5D66B2djknxR8dx0ZLy9np4YrZ7djwudstxRbhKQxUlSCCmWwh3o7fRbzITvxn1tAPupF82idUoDWHHcDrFjULnPJYyXK0pLeTGI9DOgG0kT8vbkZ44lWxdcEjz2pfPiHft7FsyiWtTw4ChvOMWBKsORJ7iw7JjevUH6GnOw5ZDC-aGlHqf3tl0LZHu1Ei0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lClAbhLtfVDqJb81WP6LFp2cipbVGbRz-whM4ZrZ_zosjstN62rXfeYpWyaWhGsAo9y--b-IVRgPgJ7Uhmw7ItnqKZp3CIuo0hRbYsAdVmfU-T-X5gzN9XxoevoWlzME9FSHsHr5RScnuK_icLENb_m3YaU_rwrRTu4PBBUcxhnJzMBlPZFYGKtfpKxHHqtr9Fv12bmL_dPGdvwbklkWs34svJVqMzn95nxRVtTuBzQWZ94O-sAJNVblZcfhyz9TzWvRvhc0qC95xM1-BJexTX9pssltqpTK4aiT5WhEyqQgZyC3iwNN-lU8LInAnyRgIorWht46MZK8ro1orsGNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX1E48H6q6NUk4Fd3n8avhiT04RpLCKMU43YIdKEM-ycQHTZVUB9U5ssmK6_0ZR4rPDcr3gq0mg8i6yeN_iL9VEih66QAIMzHUgkvyWOOdKODUHtSd3MGos_UEIGcdzAIDC2T2fifONDFAg0H3BI1xAEdCT0qde_5yxyx9NSqlyfUIMEG8X5KtNPq9Hk-TA7i7gnSI49lgJIImXcsdnHVbzZu8AB4nR9Mm4kV9D3EvjFExZET1sGRqS-JeJaOpe8IDiRqk9ccWJG5SbqDAT7cN58RKEGP3IsF3DcOr4mo0UdoMfNvO_OtJiqnftjwv2XPHBHwT03eBlebVfSBnUq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-JauixGHvpFMKFXECPThDbat3wj1w1UtUbU1CyS6GbaiCrLgcVXxww1QGjDCDoR9pyEFDVjdz6dlgFobxuFmrCSg8-qR4WEZl-PYRrfEMH8y6heKoAVl9H6RySmrD7uJJ-MSz_eXG-Csu0UKDwGrhNojOv6STvgHVl3bgTicvzKqkBC3sXQCO17JNCR8uLE7rVCLYro7KRmE4kKI2SO_S2n9y_1IVdu9j5jZ0YDd7E8kXYAheDLviKIG3tg0mprcFCiiG4dxWpylF8oYm4jduKGdm3cVjOhtS7LB4qRlQsw_SBoC6o5B1f5aXsKBdZGyQ9I-KdKsiFFY9_uMicMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDlUk6rvoW0CXQkGz8tiNI3_P0m_gJCLTtiB60EL7m1D8T_dx5l37CBNkkp7gHYkutgsWzu9F5jt-AvVKKegMjsbuIlQ0Z3NerXpAkZ024qki78TePMlrKkVKcjmk2XH69qQHDdxlDFDQnNQAPfi0aLGaQ6VYsBshq7TCEG4xaQ1rdBkjy31QAgX6fWsGGAeltUa7hVzRrVb8U7xiRemBd-ZeBu4xkiFC0MnMFevkme5BSLt_MiJbXtS1wJ3bJSjSKNcbSQ889sJ8J8Zk64UklumFFlClE6qwDE-QEvy8jbuNUQjHNVvGY5Tuw9UD7YBZlVFc5IHKC_AdGZLMlbyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z63AfyWH5le5oOFLmr-lLdSr1D0rW1DN2ZI-g3RVephJsXeG4HWhdTpxOKPjft2XvQYa80KEHh5vdlHWkCElItiDCZH4wTxo2preHsbT6mYOPEN-6GlDPMwGgJm9J0xkBCoIIxfe7oHNl_yhQ4azkSdTvRnGdHBmwk6PHow-F0e-7HqGo8WxGr0ssg7huuLeewDeON5Itw9zZXpu5EfeqhNOjJUf66yDkHsjD8-wFNc3tNMixLv6qQLZtnSnSCptdwo-Uga5Y6EqLtBkmOAU9DItFWjpvlxbYTG82B8Q_aqbJXEtoh99Co7d7669j6K0i6IM5BOenBcO_wOlUvYLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFF5hkH7lruPcje2_QC-3YMNQUJsiLirri3bIGTJrL_tFbxMTxFwrUB9edSdmAy-_Gf39WtwFlBt4S9ae9ceG7FJhuH02bgsGboz0ECElIme2iYE-JD5OPC6mxxFB1qXxms2JOfzTvPvaa-wmRtY1Gj7V3g__KmtdXaeeR9Lx66KGsIRhX2--5niYba_5ig2-g7qBNvzSgOcCy1ieBBAERr67Bble2d0J7cFJI4JvAiNSLG7H2V-DP2mr7MWtJJcFgzgbE8UM2DWAEQ8dzuLbsmEpg0fvVavzrVJJkHXGDwijQQYcmepwtneQRA813YN_UKQafymOXftdE9HLp0Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnEd2h8VNRtD2eBmORetpxkfPKTZAORBfqyuvPvqpeU0bz8ZAfUWZ_aA0Y24AzJ0p0DzrLaqO07FF2OPixn6MEDj2wTZ-8xTAsL38xq1hgvJ-jzUSJ4LS_VPKcX6PhxGvlsP7LKWnnObpyqTSB699w6i_A2nHWCaYAI_V02_nP-P3rRe-d2DGhaII2E29p-jHmniUeRPXvCYQo1YyEnkhbYsCywUkNiGvLmnKRvSNlcbOx5XPS41ayhKKO3euyCeAyesOojDuKTM-hKDpCB7glaZ8VAMwZ5FP2c9uv8Td5ofHxs5wmqdF1gWXzwp7V6ZkoPEFyvJig8xJqSSaqWOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSYpu9KBPOVxRwSVRY49CX98Uwi8vYLyY4CaYm7d5PN5JJRS2yJrU-C5nYeO3B8S40nh8C4mozojTmc_oy1Wi0D6_M7oG3Jo5x4csNi5cvxnPanskR_Pc05AhuYoQq-ezn8luTHZ-vBoG-He-vwqQe0PchNZI0GhFBZts_7FdZoWKqCGRbas7tUOgLoSChG2xV5Y9sRA2vH21JNFtDQy1jyX1JgORb4ngye3PcCOMZ0l1oNxQYWlnccIgDKTJSobKvEwUCblPspPZqLchEr45UNdIm0cKksbAOQHKUzMymQ1WgPUagjX-5SjGsjAPxNFm1OR1dY68njB5ciBk6eewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0CCFXfTepsOWaOO9cGSRa9vT4pJcCd12ZRQsziTysnlXyqICl9OAJKQ6LFRb77gSQLYFoPM6VyXG0UUHMm1ZIZv31aIwaRPQAmqk7XfEtOzwJk4fdXa8SCBctRBruSAA9ImhoNbhIgjTG4WKhF0XilxMcdl_loi6rH9sn1HuR9QD-k1eiV1mpx-yFR9Ydp6uoqzJYwH2LyXwFhs5FuYHVuzse6zkmeDcREaEFYPi6lnjsL-CaYfWXD6R0Mg7xXjRE6whXtJMvzQ0JRIlbu8nq1eenLk6z_LHRpcodrkWFSSZ0m-lmKmTJ8HON-sD1G15yi-oMVIU_CvoHhU8awqBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=l_CHE2c2WryAnDXcN-tVyizuGYda5e3PWCYH7hr1WPB2foDDKGejwoQw9jL5UsmznUvDuL82hq1HBdsBl0-se1M7ydJW45bCssqH7cz5A5N5QGCeU1zxEpSS04IKqRNuUPjsABJ-jLDwjXRzkXtnpY-pIBAFAkQZNQxdLO9e0lDq_-L3YcNfRX9ZAI9PTw7Y6SKkO2LLDDzr74RQZugnXOMzTRWpAwnfPhP9XGX-X1inznCH1aVsPdALZyBL58ClaOODjG2BX5IV51QXouMu3tMb06H4KSHISB45XDGYfzH1_W5P_frNiPRiNxSu29NRjRZ_G-HM8JenT_vl1BkXVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dc475c66e.mp4?token=l_CHE2c2WryAnDXcN-tVyizuGYda5e3PWCYH7hr1WPB2foDDKGejwoQw9jL5UsmznUvDuL82hq1HBdsBl0-se1M7ydJW45bCssqH7cz5A5N5QGCeU1zxEpSS04IKqRNuUPjsABJ-jLDwjXRzkXtnpY-pIBAFAkQZNQxdLO9e0lDq_-L3YcNfRX9ZAI9PTw7Y6SKkO2LLDDzr74RQZugnXOMzTRWpAwnfPhP9XGX-X1inznCH1aVsPdALZyBL58ClaOODjG2BX5IV51QXouMu3tMb06H4KSHISB45XDGYfzH1_W5P_frNiPRiNxSu29NRjRZ_G-HM8JenT_vl1BkXVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIoosCMt7IUIw7TCaJmTnpHNBZkwC0x_Ipn9k4gUXA70ZoG_ddmUi4M-ghIHTU1BL0x9yZa5XVzQlWLoku_K55UKnbox1SA0qicc67qYCB99iyeIqXXeN1n8ar6lnRfk4dF4xI2zmA6hypRb7ETdLOC_YjMMxr9okXpvu-hujUO_3PAcmjiuWrXy6KRk1-wnWP0ZpRqiA4xK6bU6qAC1DZ-B8I8Det7s83pWQ53RnA-KBSgQz3zHNazgI5dNlDPNVfVHCGfzeqZ3OcDo29mXU_peLvYwhd-4C7glNdWukOGLlQ-OCDWs1uv-vMyNTiOvWTxvHx_5PYyuRIG4pC2WCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ch5shD9Za_FV4l6EkAYk2qK0RWNDf37bhropCj1lEdwAWM4l0B2rKB2-KLTFi93IukmQwWOskTDZs5xiSLkpDB2TZxpxFrPpp5sEUvv4AD7r8rAH7gRHQS-EqWnDIopb1BnJjLlZQO1x7SquJWPQKhYZrWcdu8sd1cI4wambcq0Sus9IUdBc6Yp2PR5AgCBVAxKTL1G4OEaoW-xm4_kMILIba40SxmIx6rGkLUJ5e1A1VFagoqQFbMj9gc98WDLg8KV_OZOkpjdCOLsNjmbm2IlIJ8WWPc5zAk4DqyzF4VTQ8JUvF3smeA9IIssSb5tO2CSG5w9dSVp0g_GXc8C55w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6PdaAIF7lxHagwRosA0l1jmsZmMp8eVkVc_wIY_ldylUpo40UH8YsjxTXn89Ky-yrzD7RzHwiRj50JQMP93dwhXRTrShgf-ymN-0Kf8_vvYk-ocaHWPKyc7Yr9aacqrOxGyi7cW0DbqCNOrBgNTFYZHZwI7nP_zu1XAX--CuiGzmxmvjBzSdfowOT_5OFn-cqO5y8PIkscqEF8O9902hiZ2LW__ZlEknq7yI4w1BiMbte-zyp2dk_8bYhQCy58_y1DKcVVxjQqqPogFBBVFVlEm5Ah2gSUtRxvFV3cmykCxMKiLmY3n2a2QCkmEFJkDEe8dxeAOruLxcI8gBYNKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHeKaseJAO6B0p33GshPAufWe7ZAHRDU8CGBTG6U_51XPRAAui1MMTskKbM89PZAoN-ekxCdDJ1RSWyJTyxuPPNbYb7CFjKo9JUwnVTijwTL73R5GtuP1rhjpSBnJm7TE5IJN1OH84THY2baUUbgzP9z4XCxCT_XHPiDqTczyZDEMxNpofq8L_h3Tt6am6bBg7t0YHhPLTjPeYzfWKqOj-L2AD3ItmgmtCDx2BCKOmsEjEGv75xWQ2vKDxJpwibja8FwOI-_iY4CW7Fo_2apJjI7LjfeyR2TyhQCAHzfVAPFkxZQtHt32rtme5AU8jv8PumFRXJ_tcVq5SUHu1Eqpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkWBwOgfWwtAbULTvYkKDjDUn3O0_M7mPKLOeNk7Cxm-91tUIcROWOZUc-cRad5B_AfOpzVLwf94mALSk3202e6CuCUzEpQ9O9CHFjWFQXBGILCUIwo0aDU85kZMHzGaRkPWk5UGdsg9gYvTOvQ-UD5mTxP00pen_SLdmHQwUrJvWF6c7lADvDZHMOgbmHtm2imdAw6KNYgWfqv6HjsX2XKfHZDBFkTHr2LiGrWYK7MBF-PYSjeA0hldYWRrlRuPlH7BjmXFHy5fvkRQ9jUo0nv4T2neULwn9820_dxAnBXzQyP1eGPJcda0SkH-BuxZed8guipBCCItphvf8aephA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIkjU26llov1KLx5CsWtRxNfWQl3PqN4Xk3kDFQgC67T1sPExoJBYm7-3BSRD1uSZ7n-XaUJhwxXzNz-sUfPY9tmQrRpd9lLz_fJuaoU30OFfDIpiMA295-Ea96XKSsi4BBHHhslZfeHGOFqheqJJVb72xzIKGGiyIpZQigxbbzd-7pl9iSukbDdJJ3CbhAIKCctVYx_ouAVzgk32yrIlfd2cB7BqeHZ07fBqa0XSSYfse_YFXe_538W01NaaTb0qnbWv_0emQk1QfUdqVdI0oaVrOU4Q63Szfm3ks17Bv5SMDfJMGUIKBAxfPFnpXufyHNfb_HwEfxyDRe_1UsIFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBqEhMI_TOzWaRa24S291hDk4KVmgtXirVkg29B6PjMi5ReHi3dCyLj9-S2R5LOT45J1CdVBv_ouYNHmD48q-oG9Qr5EZrBJMSep42a4xOedZoVCNazQUUs-qlVmK8o4cMjMC2lVYiYqKuhKqpegF4_Icb9IJyS4YBZBxB6LBLRs840JrfaNUiM5wPFBj-5dOckFM56s7p7AxspE_Qz9eGMvkBzQKTpVCqUUNsGgcc7oPHwi8xXgbgvNRLRtlYlJCaTfdu67ikwRRPQoagcB32IHcjianxeoZjVp3V0r62qyPIZd1JYV3FmyjEdFeA7cXHF7xpSmLQBleHPLhxeMYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0SfMDKVaU2kRehecxgCCzL58eAtU2a6jjU0IFOTUlQ_mYeuvoNQ08PAsPonIwfjBkexe1iKASvCBb4iVefC7IkBJeIE9I3tA-3Iv0M4rgP1t2zBfWOo8f7XT4XRuWvY25M1MYXXrWP2SlYjFmUEBzcIWDUd2ExTDCmgnJcor26azowjPUdnM3BS2ZN7vKTYAkL9Kxez-P2Il7-l3u_4xrFCLA1Seywz0oVGhzazLyip6KnHbfLcEWby7NvSyqVLxzlSEYZnVOV6JxjUiwGVx4qVkt19JQPLqUzILQhs20v0rEQjpyOMzgOtA3PT4Q0117I3e4gWGyVdEHBmXj5aCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSKYcYhK5kuVzTGtNOF6Hq8N7YnUwMsoHHqTPl9nnAN8krf1GNnS1UvSkhS-IgGwBFojTtQSfJi16flA1bSiNA5WfuvPjZ9haI6y-rKHfn3iDRj9_pCax-bSLv_llXM9ikp7QMhI4OFQKcjxukpWDwn0fecpdRPSHdkgEYjUvwfmVjlPlzGWDxIUuwAH53MsqSDD8_C8LqZWeuvecUDPXAbQZcunMeK1lcB1PCqP63M8-P6xYnvdjtWX9eGaHzvQj_3IuzvmYnlFOckr9qgdkj3TDPelBdS7Z4zN1Z-jv5zcuXUtPyhLl5okIUaPP2z0OYXvyjpGe27gfAHBGcx4iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDNSgD1UEpRTrS5zYdYBumST8uaRS9AH6jOx0Q8l6L8NEyHOAs9tPHzSzOHQaN6Wt5OnE-AambStkvUu-NLgT1_LQ8FmrEWB8EnKhWJGxU4N6pKdxTTGr6yKDGAP6mwgYxRYV1EExujK-CZMbtzDDUqWb4vaFpJQ8Yenrv_Hjrv7lofHsQRhY41AwFZFMfV6BAHIPyWtpEIocXoUcMsF-nfJAn2MFN6aZVjXWQ2svK1nmXtQdEPZV7aTxLG83kfAD9eow7mTg0c4WxDJDfZ2H_IgXkkuWMktPpeKo-jjwSCUSQhSJq2ep4jFzd_lBQNm86nJweJrzw1PHndBOs8D3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDRvc9pa8UaCgZogdlciZC6MANiuH2iMzKRLlyBtUa0fpzPjb82viOS1RvgP5Vb5_ba4drGyGgRey5AzgBQ8TnJh-3r2jQm6ofbvYrYqoqO9coDhrfewfX8w2h-G7caH-kZsuDsY5M5Q-Y6J13EdKx52JYVCwwG05pHLv6Y7GCHzePj59u2Pe6vE8nedtyFTd2DeFoR9VklKrtog6mEDfsdSHzb7TvR56svqZd4-oy0L8jM9vdfN8XICnNLxRPqQCkOV983LvdkkojPMSKLxnmi2C0K1w5ECWXj5DwqffxEhnHhTovp9TF57KbMKJngmwt5lqfXFm4yq7D0sv1Y2vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=jev2u0GvmBPteV9Q4xrobdu1PUMisgBNj9mQobNhuFFslCSxTTcCuNBs2OSl3PYQxZAtyptqjErubWLiR1TyAPOK_Lo7YRSLXn0Q5k5zb0B6PTV5lLnt385VeKvGdqtnpUw56iftvDVWzt02vY-UX9jYLm6xuZGnWl6PE3jBeUMWtwJjirhKjq08R0aG1NvwwoYBdTYRkDY8pJcjA03svkqZrlinPFfsoDCEDjiNv509jAjcZ40BEM_9Z4RC08U2SNKnIdTbbkY9eKsjIqAGx4popI6_L2G6aBtzK507C_PbNWMrH_5ISxflZ4VDBhEgaC-jC_ZxXeTi7J8A2IlcqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=jev2u0GvmBPteV9Q4xrobdu1PUMisgBNj9mQobNhuFFslCSxTTcCuNBs2OSl3PYQxZAtyptqjErubWLiR1TyAPOK_Lo7YRSLXn0Q5k5zb0B6PTV5lLnt385VeKvGdqtnpUw56iftvDVWzt02vY-UX9jYLm6xuZGnWl6PE3jBeUMWtwJjirhKjq08R0aG1NvwwoYBdTYRkDY8pJcjA03svkqZrlinPFfsoDCEDjiNv509jAjcZ40BEM_9Z4RC08U2SNKnIdTbbkY9eKsjIqAGx4popI6_L2G6aBtzK507C_PbNWMrH_5ISxflZ4VDBhEgaC-jC_ZxXeTi7J8A2IlcqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkXbpVEdX2PH-1K3hrHhu0FMsNs118oaFsdQuIscIxx3I5JLrtgeeHLjoFCMnIqQe5Z2Bc1JUbuJe9Gn8KbZYJcDSy4Vn4Vb5XOcLOe67te82WJxazPQA2R4qPPFhqO-Qcygs5536joJt1e56MWjIV_fqv-Ck5BmXWF3JdbPtZhv-8LIHWRJmA1-Thze9qYr8jOtWDkhn52Taj5URBLppu_Tik0FWdE7cAE2QJAP81-h4tSFoO8BlajZO7AmUxsAlJ3UwkuxlXqSbYGmTxvd_PhKqL5sUOIbXMmf2s-pHVeLnOfW0CFjk8y6e4tAiab5yjOmlsoX4JyO_27K6ku3nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFYJSFwlRJZJd5URoR7ktG5ViHDTvY74WEKcmVaP5cBBYSbCqVKnRVaKezyJoZy5ZEA7iwu_fjER0znyGG92eM3Dnv9-xETNQTrtl3ib0e8XZ_cwU9FgX-ly_a6lTaXIhSie7snFUPZ5EEnCar9BykEuwxVeDkEKQdAzvVSYoILfp2mGpU7darF44uw6WgicNDcaIXfgZVcLvbWkWWZZaEe_qWAmnGk1wuXYYXs04yiQC71D-dgccLaDW6NyiFP2Kulss7O0DyRlQjJ5QGJa0QI6hLgefXNG2CopaW-jIogfL2uloH28oFvNTHpxuQ-jkrqJCacXVIQuVlqcEyoGvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLuuYzUdig4m22RWiOpM-HrWb3vpLAs4k1k5fQx34FSmfWj9TizIXbAPc9ZJ6ei8D7jLvu-G9f0yAVfgqcu1MWfAR_Jq0g6dmaBgjZqaYACTseQFtQOk-aaOciki3Wh2QZ4K__LJefqrC2UsALxut17f-hlBcJOls_Bo07QMn8NS5n1ZKARa5G9YGMwmpOK0n2uCjCuOLHsXA1sTQvw79uYMrRPQfbEF5lQNr_n_veRNqFy20mcZyFXs2v4-28pO0USUNmaDd6bD5jjS8WGYABYX9tRrBT3Q6UJVr5_RzQbNL_Gbw6Soj4h0OIA0GVabozLoSOwKnBdxsepK5q_Eig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmHF1FJPyeCSASMeqGVSA9EBelRH-KdxFPCPe1zBewPT3PHcemC5saGSri9f9jgOYmnOZpKUyu0E7B5n7RZT2Runmxqz0e-q0_ACD3XYCLlzM6uDINl0QtTLgDrSRtfZ09FCrELCIkmQfEyQd8TNXi-z65NQi38-5sMCMOdNUB81oj16glxFFmPuRixiJ7rc_iC0SVHt8WWpJHXd8CA_kBblRX8nmuJYggtNnARtkXdRP9xdoQE5LnKfywqLYeWstbu4ADCF_F41fPQS_yBJhn7sMkKCk6IYlXGJbgkI4SAsOHMpLErrDh6Md8BlhagNuHUUu48LZTefXkM7tMgfSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qc_Pn5bhpXVD89umSrZinrCTXC1rF-6v7PuQIzap-uoHqpiH7BckmqFMJBzb7hScTzWW7KbEkd5pv1SonLZ59ppGIBtkFtuBjhq4DV6J7SVWw24aqUyN4sPlqB89j_Z-Ll9Olo5RA_BzhfGhQh5-q-lwyiX8KhX5WFYQdsKtc-YAkC8-LKbvOSOVKURhMWZ-LxnO2cGoMXhaesl0cMW155RslujrTIlKpcICzMAzR02TfCsVVKnPjBIi2RwWSXkOLv1bcwDmHFMpYmIVyoOUYAU7_60NoyvtGHBvNSDfmwv-sBzwFk015DMFcenfqOuF-YBnM0Myz1fYHIkIpV63AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgzVqhi8_YY647ZLtxrbU0OMmzqTgsQZfSzAyxDsjSYmgS_YvIXlRiZw8I3b2Ccoyu2kjh2kSd0W8zuYAeurQWZJL_M2lEmLtsbOPTt_8djsyPdN27pkZNREXg6Vo_hAbvbZy821pdAUO8WuO5JC5sfGTbPd1p5WKx5m5W4fQhxSxhNkL_nysy7wG5eL1zuIb2CUzAX7bNXsMLmfsdH40CpZb1ZJia76f4vG6RsDRUTP2hVHHf6rf-uK-k1DsLH7FqP48d1aQZtTvRoL7WCLXRpwDLEcKoEsbG2ghX7N-pwq2crbGbm6vtxBc4wBUIc4jY_P9E5Aox3Fh_sZ9jbadw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAw8g23VGkeDGwsdIh4FOf33tpkAm9fiqNZPlrt9mRYMwVkxtCljw-j9yWRPIIIpdUp_QtmQlvGGaS7mE8b57S6Ob5bx1dg4dGklljiZkFPYoozHrRSNUPcVXOatFryeN2ngqbX0c8RDqGZsJLIbJE9GV1buAOBm5OyKaeJ_MInTvkbAn0UEv7VUtjzULKre6zO9qq9bCZdPzK_eKXUxQbyD51NhhLIZh3hDMySb7ujRnnnlVMh4YU4cC66Qs6zlhMkD6IMRUnlIFv85eNn12smii3xpzECXp-ZEYnqD_B_0vE0B-gznkCaBduRzyEmENnQb23_o7nkyaD70jTj_Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyusNEj-4PuBuKTH6X93aEBGpopGv0pqJUhr10bd0zQypBP6r37yK_Ty0xPQvYAOcmsItrt-s3oLiGwaX3MKk7KELX5WYdKS3k9FiltDbQ3G0dhqUo8VtdQrb4lJnMIe8xfsP85bb3eDWFkl1QL-gwVYPHBPa3uujdfPcod6UVq_XAk5w8mXMc1hKXU718F8WGQ4wfjZoSzgBX4FF-sWyrbMm2Uu9IWM9BBt5pKSx_xuZBuqJbIEQFm3dp7EBUXsfCkoEm40Gn-WDAMkr4aglwkpHbMcHKckEWqBrQY-I9dW1ttOmiBgkhERhCHgyh4kDuvBtZThYev3Wk2XWGpM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ky2yiuc-MDwfJAfxzw8_pxaLdP_mXWfaWBVg7MV5Cyb86NfSJuDjw_CTVY-lftGCYc-6kvHCPqFxyv0X-azQvBHnOiIGRI3ONdXlHLw6vdI8WwpoUmkYl74k3MIK2n2n86sS01ZeGEBGL8uo15_GdwpQgIYnE8pKTwPy2P9dRtcmiyq25649EYvrjATxHRo90og1RUrb3dF0HWIbdtVZnYNABGWeqJxwQQbqYGHFZQndCk1EfKwnA3HA2YRjaARujZyLk6lOvFGkfdAD9WQbyIBm6xzMlrOaKppzehIPUKxgjSo3CKNkx6i_c_55ZD7lfJ6yhu2janGNZzbXn2wNcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=lyIvNAk9-LDYLlPx6vpVXMs-poJ90jNCyJvnq6brWnC3sg_obTBif72JPdaqSZZ0YsjeP1nhyXSH28VIQ2oydFy9KPVeICzW840Vn4mj5F_YEU-3lNzqCg8luVjUuO9QUX_a6pxLIS-jXBOBj2x90xNgyh3WObxv58Q5NYpp-vQ-NphtdX0ltcZp_-mTGYfa1gG684WwWzspCHYKEiGHVnyD4b2uIugDov_8X8OUVX84vGHjPO9wfVPxsqroxR6LMwx2Kj_RUuRpScfr3OB2Jx7llfeUcEoOW-_OGU4DhRiSewOeozhXLi0xuUGLAL5y2c9vUYgSSotoIYPJT-cl0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=lyIvNAk9-LDYLlPx6vpVXMs-poJ90jNCyJvnq6brWnC3sg_obTBif72JPdaqSZZ0YsjeP1nhyXSH28VIQ2oydFy9KPVeICzW840Vn4mj5F_YEU-3lNzqCg8luVjUuO9QUX_a6pxLIS-jXBOBj2x90xNgyh3WObxv58Q5NYpp-vQ-NphtdX0ltcZp_-mTGYfa1gG684WwWzspCHYKEiGHVnyD4b2uIugDov_8X8OUVX84vGHjPO9wfVPxsqroxR6LMwx2Kj_RUuRpScfr3OB2Jx7llfeUcEoOW-_OGU4DhRiSewOeozhXLi0xuUGLAL5y2c9vUYgSSotoIYPJT-cl0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=KsBt0p2VT0v2U1WYbrCXYOI2YweRWPRJHBGB0kfSwaYYzqGmMWWVb1MUwIqv3jecCvZJwBLAQLS1_75ve6i82-2Jo4vtfVzw_0_X6vpjm1F48OfBo3V7lFtSDQSNnFdGFxw5W_s3Mue4SXO7tqjJF_gSQmf5_8nAcV6zbPu7kEFaNJdlGimzNaaYmsim2iDZZ0_XMD1w2SWxPM7VQxzLo33cKEAWrDyDEMvC5P7eRN4kygNUq6RzpiTILBzvfdOYB8z6G4kRfQxBbh3MNpUWPCIhSlQ2IyFgNG_orSkAEFnjMHA44bXi7Db-Qp1lYdDP0Rjgna0Hy3PICIshpKKT-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=KsBt0p2VT0v2U1WYbrCXYOI2YweRWPRJHBGB0kfSwaYYzqGmMWWVb1MUwIqv3jecCvZJwBLAQLS1_75ve6i82-2Jo4vtfVzw_0_X6vpjm1F48OfBo3V7lFtSDQSNnFdGFxw5W_s3Mue4SXO7tqjJF_gSQmf5_8nAcV6zbPu7kEFaNJdlGimzNaaYmsim2iDZZ0_XMD1w2SWxPM7VQxzLo33cKEAWrDyDEMvC5P7eRN4kygNUq6RzpiTILBzvfdOYB8z6G4kRfQxBbh3MNpUWPCIhSlQ2IyFgNG_orSkAEFnjMHA44bXi7Db-Qp1lYdDP0Rjgna0Hy3PICIshpKKT-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ok2EbJE41hG0x1V6hLHZI1ndlGqjqIzAn6HbBncP3wM4CC4RrA7j6yXgaILthoDIxg6YNB5iXlgvmEbCCVyuRKs6IK9z6rp2B-fcZxoGFw6NjwESVeQH6wMTvgx6s9AO-Ukv2b038sHlsamQDZdgwvTxzv4PQj8xtHJ3EGnH3yIZw-443HIAXVY9cX_C04BhX6sY9401KnV_LgpQnp143KQWXcfz5eSBBLiIptdo12WYC4mslkjDmHcrbPvzeZCNQtxGc05JTNfK_FPuhby-FVNSKW7VZA_RghWTLkTgucU7D7X6ZgUQDd4QFHJ_2cjdbP5drwZOSmSlphPXCeYQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy0fFl2vsVJJxVg9yiTpYv2IV_8A5a2QlEn1IcOIwf84Tzzs7DGgafH3P4TplmC7aBHSNPQubrc-1Ytg6d_7ot4bDK5zIymmXZcI72E6qN22_sFbKccQYobJTGsSq63QCazsA5KfFQmxSQKVzdz74DzUgWSf1go51NfcbLbZQqAaoos_TOCRfiWMnauqSFUmyr9Y5soP5-_VZpJuT_Ny9od-3JciE9s49Jp4PZF_Wj_HkEsDEerk3D9n7Wb0-1a9pUtkspcrGLKyUy2hYDfuKqNQfzOY_76p2awWMLFhyt-GmkAEO9Ej8C_sqRMb4miAINdvjJaW4bu2esFzrxPA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN0HrEC1ozUKEjLJEBX62DhYmmB-q-_qu9jtBr3A6TTV3ZNWPgW-o9Kf_hKH8C_5sxASb27b4Nvrj1-OJnyQwju3ziZ5VEb3pEjXQu6kHooAjoC7o2hrN8NJT0lglvrqUHjnk1FKfYNl2gkTY2jZXDIEtO3oE2-nZDTUUxrMafIGZNbzDhMZmOASPt6hUfYmRvmpF3w4FRIUIikrztOD1WaLNyzEip73v_poiuBFn623g5Mp0WK_b8YDAvUn6ZcuyhEqKPOYST_TKamhavkJaI0M-6DZXLcrYZkkPCrqYYC524siuCFCXC7JEKTTVuenmdRfkhUcDrqi2wejJWRqeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtlZGXphTxYcG8yMH6pVaXOEfaSjVzIveBH5JWJdsWO2ekmxjS45idRehH2M0HUWbt5jMhVY2xwhlgbLKZKyKfjGMgVDYGn3vEkLrAH2AxAS_FTzlpNxq5Bm7JmuFw1_QSeXk6gWoIAI1u7mtJezT7Pq4pXwXECTScZHbuKIzN2l73lX8AFtvgz6zev7xlv1MRm2Enru7uSu-k5V8Y4Vcvt8vFXfnrwx_O0ZNi4HOghFA76K3woHdPFp_cV1uo5ZfjjP-CvIHp7REUqC-KTWTGxhzBhE5HTFh49foAPdMLfiNAW83nWRoR143J_5VqAI66rpKWbNev5F1KnUuVkwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFrA_YHW4FgycvoHZ2vcvrJUdjy1CjK0CuuxoUzcpvkzbZo405Vgsg1H6kCDcp3lq8_KdrxnSfJ7ccFvDKl0hppRHz6jVAsl9sE7FN1yJ8G3hKmfX5VziZoaQhvdXJ9hi6oq463vHUXn3oM-nNdFYrFmu3zcrRNW3Eys45I9wyQaaU6qkm2M46E1DRRDuIv0rhVyejum3rOFU92pOP9DldrD44gkRaCF5fGuuqbUg9cWvWRUmfri8MzyV2KLtVYyJGWIikWQqMTTh_jk-yc55rUdXuqxWeVl9axKJ-1CpiAoF_sZuMvRW5rfTfshfvOKJ6SW4oZ_w8iq5LL3XU-L0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl7_ntIG4xINcj_nMWq0Z386hJOwFhzMqfpHjCtQ9mm8qEBjOIeiYqSXbCpOa-G3tq32MKargl8mrBB9lAGPiMZfzrVkUQuxP0nf5jCiBEuvZEqxmNDk4GR2N0xBZ5IT_k-Jm89RGiGlYALvsscc9T3quZOsSAz01QQXE3yGv6OFJSoQlomexDF9BINEuYjRglTr-bktLwWKswqNNvM8BTMIIsbezqjrUTrr4V4APuiLdgu7_oWHqnA-YYPtY6WYzMpGki-Ay4kNN8Sp2oVqXgTK62Yd-ALoPjkfX-qdNp3ySnngh2-WZ4fpDmCWc8gHtRJI1q0ZAIJVbe0Y27_vJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxLaFEreRd6GXLwevkOxcsq_RoILTyb5IkTNTBkpJirjXDE4ZiHZZYFvgX-Nbwmhwtv7wZAaANds4IzPZRnssPpDAC195I0rU8q9fuGf2PL6JAMGe5l8FC8oFJ_K7q06Tpf2SLGc-Lz5WH0VoRuqJVLWoEDx1SLYYXyiV-mPBh4y1YIKeyTGPgGqfXYmqBIVG5JHC2l0KsqAdKjZ--vs2tR4EyTJm2RCmpNOcQLjslm-BwjvQ5VPwe1XRC2zmYaEwpx5niOPP0D_ur54stTt8LPORXrP6Llqxc-bRG4p87P5JGuQdCYmyTyrD7gJfP3OSticuQoCm5kAc56KBsCOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUD69ak5b3xqSZPRThiSeweRphyB3kI6gLrfgEmGmrSs5XAZCIab0-W4JgTTwON9u2zoPtcFUAqkbiO3tkI38APUvDrXEuVaWKs6Xmywn8EMrlfSyOjghCS5NGF-Mgs-gRYaQrx189Y8H4lcslBV7P_WqxeqveSsE87n0au1Exbb9QXZcnOegxsokKrnaX8TGPOO7RgrTpU7MHzApPtUYlLbvhtzx_xLRTIZViTglMe4-OLj8uDLtx49Rat-IwUagGdm7-2SX7eZmC8-b2zB1Hh_5IkFA7UM0Qh778Rx7kSQRZ20ozBbLv3nH9-PrxHRbd0M0fp7Svq2-5RiVue01A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg3OKE11J1micqnXCUJqom5D4SD9ajUA3Ea57o21Ogf-M3p2b7zpLl4EfcclN57JgMLbksE5OPC35dPpDT3-FqGPRVqi7sGsAchE19wlj2igy5RPVxnPqwnEFWd3ebEW08zae7xVRXW2ov-PNetwy2Qtt5IWFdmNdT_JA8MDHraobaJqxiaJDEArnmUqdAo1EQG-SNjErDGo20WRM3Oh2CGj9TD4sHXe-zFsy74DJVFX-91PUMksHbl9DQ5Kcp2zorvQEED-VwTlrPtvpzIdYkqPS46uMyftQgV2aj8hvjP8X0iBFV13bRIxm04ydfEoni__LhqVjcIVIqir0bhXDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2MiljuYIsIf5pOJIDfiZ1fpBS34rdMaS55hEtZQhKZ3fxBUQNmFZ0xUdKX-_x74LYa9LaYy4lS1J0W7ApNt01N8FIO3Pq8pkF_K9fWbil2rddH8JiOtSZ4cyn7gFiaILXz0GcslBc5xGvmPsMsYyaMrtbu040nC3rtFJ6kTuxK87mfhLef7XBxZ1InjC8xsNuR7vyXFVRBK-jAl5Uub3sKOXB5f8q7GvxS7k-ef-nLUA9ToMRl51cmCkxvf5KPyZpwfypHzQuWiq8NueNvPclpiNfsv9EY4pSn8BwzNHRI5Yu3pwp55Uwgt4ovjPjoUZGi5ZS1hkFEm-LDIrnmiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uPIEu4LT-zqWX62DEw_mufhMNI2m73jrWVPoyutpfPW4JYZTsBozNlXBuHDs3ThP2NDE1UCqMOVrz5HeFoIFyc-vjdTFDoW5GeLkm_Og7RCY2tN8W1RjH866wWbnhMSBamqa7jhNdG8pKOhg_3bYV2EJmYmdlVZEHXiESR-U9bQY4a-CkxPTJVwNuGwMi-ehyyJkSpMH5YXIX_RS8di7y2m1bjDLYzzb07KK0BblABtu7g0NYAox10DleRZ7VsAtcGFmp2QbWhO4Uzznmsr8MPrx9vunU0MWMwxvPQhYrQHvRRJqjjvC4yVEmhWWyJ7LYLNI10GnwGfOs3STk7HkJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHMIUVOTDlXK83PkNFsSAv0ffSkeAOCN9dvaoS5Wj-Wy_1DQ2eQaANTe_1a-sAsEhiE4CfSvMghbDMJ2EaIorIursvYdhd2-KFiCMehHgWSqzHM5L1RYFqgLt2q93rwWb9grkKppJtgoauYMz9KXYv3hTCLuPjMgr0zJq1ANqnflIASdrhJmoVRfnGpiQfVrp5uF3yEKOMTnBaDFktN_5j8HTVVlBxhoZHTX2vm8cPtzLXt68DUTaRzIcwtLh6FC0HMpIChNzRWtEqFubYapXy2xxEN2V6aF7ZetjwGUyrnYzlcR6Yv-w-H3g54RlVDm1-Onb9xCcycadrnPd6gnlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoiIgHloznFWMbR5mv4srt3vKU5vPMt2cHPsvz5OId0Rr8uTYKOz82r6KsbK1LfHqT-QffjJcP0t6c9XnjqICoLAND41upNiGfJ55A928lChZFAtO49FrUYGeW5j0j8XiaWE9s-QMxJ2RACQQSM2F2sjHJIp_BT9y5OVvWIDSdK3HrNlVIu_ViFw_PJEzN7zFpbjsM4sr90sfZ7nxTQkv5r0u9KZyjcs5O532st-xYpSA-YtPtvz4M6Xh44TQuRw58sMBYP-03cubtxWCdyULaNvsF93QgaBxf7rkwo97Zj-SNvrtJeEDZNULD00gNC-BWgqw9mDlumKkpfCv7t-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJym5-N_Sv2Ul3oyFoV-O6XSudvJljw8l96pRAU5adGhcmqv1HaP1SYn-kILebtsMTyG5h6-ek3fgPHX9kJUtSslMcunHbsHYMfKBpKq3eIRhQ9G2xexnsms7OgWzsRsu_d_JkpiW4Su6NfdgxuESAb1G5gCjlzfxT1-WQiabf4lZMKD4zHaTx-q6vqEaDkt9kSj_vDqsyyrlKjlQ3lMzMRkD4EkE19iacQlNE5l2n_8nt0AH1ul1YLs-ZKXd8gFYhrp5MDawSowtJ56N1b0O5qlad30K0Wd0J4t0p0phE8kMJ1PwfFoG7e61NosFLCI7rbdqAqxei4aySTs1A3b2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5rxwMBOS7ip4JGl77YPgbT0WUmKaddZ2iUE8wlzLkyuop1AQnMALmsBipEgrq5Huifx_Qtlx9zgU3DDPcv7KqVIBKcJ8_CiHfxJaie2VRGMhOn-x1w0oIOfp9-BqFM78IykgGZK9eBGsqQRvE_X5NAT3TrKBWJOM7TvEpOJ63Hu-y8CGUd71tC7evZgsNxp4MRQcMqA-yS78TnduNnYXvdVVTtTulDrOnbKXYeQMpa9pX6RGPxgcaRQHZ0ajRN00cGXU3I7Ec20sqHdsDBg4MXshWYr18_JPJhmXIbXtEq0X-1NdLZNe2ZTExwWBjMPhd2HJr4s_9Dv5WnCgO50Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MoWjoaIlLXTlZ1x_zou2b2VZhLdIa5w0ns8njqKznwq-GAjDwUfbmkjSRr7gOivd46bIXFN-K89W6YNP6gQakZJY4iheMDbdEv9O992202U8k4bquCNIYPLVOX1eW4rqBkBhcp7m2Fa5n0aqk96al8ZQrbFAxKZEpmgjNZZ6cFFISWrscpLm5dINEfsI9TsouE0pE877rPTNOvqGIZpRhr30BmUqp3ZKRkO-vlNlnzXlF7UO2RMONnaXxys-bxyvrmmtBhgCS_UrYCeJ7ZjMP1BonmJa9-ALXhsOGifG-jjmKbS390-w6oHyE6opzWE8_E2T_ZK7fXmtNq8hQH-W9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXjlwPa0DvVuqjwtMHyRVWy1IUU2zydHKgBX0jBZVResqhUDbsW30L0GyGAvEU4F9ACjy3cEbUuc-N6oy1jlKU2En7avA_toyUn21uT05UojP03DcvzSV8fe41CIcJjDux78LtQffncyB1sL9oRcvtc5h4Q_S9aif6F5MTTSrj9SbG6GVxz5LAUw1Ap-d2JaETghbD0G2XWNQujNIUWa1PpC8uip8kqfbI8YNfoWw3R8HfPKitpl_ZsBUXcvutBXH5nODcj0BTzLY0aNBUlUiWnyI3qkq3uSP7AP0b262UMkZkOvCS-ne85QXWEHE_Z2MP1FwV60CfkFap_aA6Ee4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MylFE_MDz-hVEOT3Vi38qd_qsWOQ4gXMROJ3hTdzfeY3XVE9wLaTjUcB2oK6cMJyilNv9grqUqP6gz1plI9UX-jWfY5myKyUbPkNAtgS-kAucWLasjy0RboBE92WTgoMYBi9bTq11dk7xaWGP7THoEU46ZZn87Mf0ESw7fINT88MSb_-DmqFZwRzKQ8ewaga4m0tLYZMnlNrapmp2z0tatX3qhnwyS9aF6u-bd5GOA7cA9xezvYUNlLQtryKrWWJSxyPDFq_ksvgkH7XFRz4Rj7fsshnr-vADR0g_Hk5S6e1odHL9G1EN9jQcDVbMD-5qy06KHNCXks3Fn9ipnDTtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_kN7f36LlRnFMGDH2X0K68brmJckbHteAvmgr9WWGhknO4KvgnLi1TEJF5SUM7Nnswfz0stAAys5hNBacHShMdtevqXvpzpsSDbgHXyvvA_ByNkJPzHD4VZgpBwlL2lWPt5Sixy6TSoPZDg8xvgIbOS0wtFXU1m6vA_6LhYAIsR4Sr5NaMzyblP0QM-I8isz63Y3pZ6OSsQryRdY-pHkq09UN48xli8P2xNLo9_icDqPyGMEsK2id6Z_ARxQ1JGffBsArasMdliGCucZ_LoTMQKd7nEQgdM5YkbiWHxXP0x36q2b7UW_Z74-IRz3oRhgJq4BPSUcntyuz3XFraJMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sB63FOs2aKSbEdLu7yAsZJFfih_rnEvKEAxA6QiOjE6U1GA7KespVHRpz0D3tA9PmA-X_KF-ovbl3RR_g6GegBbxpa4FRTswv_9ZhAiy1Y9657XePjwJpOsGxT-OKIGDu4W9d9f9BfRu7VEDI-HufWgv4yquDjaN95dptDohxsY5cS3tkbSJ1AEBqfV87Ixrn_QQXqWj3_eUh-Z43_WlvnOEWW-uYtIazBS_NLbQsYSsh2EdDb3gFPRR_rkbDvZ6Vu4SPCX-1iN6yDKnDkB0ELDiMZ_9h99jeAM5MUgR8NZuT2af9sGmRh7h02qlRLh9fdO9Gs6V5txNQrWZ4sHgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRJuodotk_tSgl7ieJn2swtetm-f2LnmRn3jXGLJVVNoBpLfm5MXvPTapzFAGzC-GIB0nZsuTlr7_zE7YyOrr9h4dkc6jUMT9zwTFUg2IqFdPbHbfvytQZy42ijUgPcNrOvmojt0LCvU83foief9m-Yr1BPr1aWxwLlcsDOGhyEOcbF3raHELMVHaS6wjvJvd7gAkY0xyq24QlUGJ8lbuKyq1W_bDC5MUXVj7NUVUFXF6QZd-a6Cyug1fReKlEAgOrSMN9KXmjOlqhtbRNp3aI0vCwimjfh07WNZnYuowyj6ytwbTyaMUFXNww8ONsck0KLJmyVXLwO7bEn_aa6Yvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مانوئل نویر، گلر ۴۰ سالۀ تیم بایرن‌ مونیخ قرار دادش را برای یک فصل دیگر با این تیم تمدید کرد.
📊
آمار:
✅
۵۹۷ بازی برای بایرن
✅
۱۳ قهرمانی بوندس‌لیگا
✅
۵ قهرمانی جام حذفی
✅
دو قهرمانی لیگ قهرمانان
✅
دو قهرمانی جام جهانی باشگاه‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWui2_vzAcCynzJvmpW-oGq10FZBuY7usT_ZBTeea6oRdH4_JF4AX1xriHGj2hj1PiZwYMbZ4BOSriEwgaRATK2WOzOhCI4tV6dXuUvlf8UL4Vn3AzBpJzgrVcK5wvbcELFVVSiho9ltxauhjxFgWPHWpIVa3KYs5LlE_iWAI4oYQnBqU4lxm9VpVmjMxa6h7_yecYIMtnJWniD3owOohjE6PurcaNHLYhuEfne2rU2fBG_Rz3kxprgfGW_eeo5MCPe1Wbq-Wfl_9W7U2mQbm9TpBcNbvM5N-SUlJEixMQKO726XWptJwwc1tJM1k7RA4C7yzDMlI06GNi7pxi_n_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qt9zgcXBQP0t1giTgvQo-Ewh6zg2tsboZjfd16TcnM2WKu13mAI76IBKuEABUFFCf-EIU_yaOhIIsAk1DwZsYKoS3w_uy51DihpzPYzd4fUCwqTwNEOIChEsikRxqQfzeiRo5Oyk29fPNA0MAvmghifYsf3qclQpuPirNuAAk6qraTl3WT8cdMdiBi5GIQtsiCkp60jf0wBNFCI0v5t0Pd_Cr25hGWexVH1wXxvHdGT6tQeEFGF44A9TqddO9R2QXLP7aA77yzK_5cxNueJV52KqzeLjDE10ukA3gfxHCfksWhoIYazGaTqUYMtRJKQHM8RuZalfx1sefIE7l207zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0HhHMaoet5qQmhDUINFsg283ZjYov5eZ3-7CabwII_PXwAvDjgiR0RzYgv9Tn7_dbyga-EFcZHtyeXJYVHXSuhxCOxvXQcX6pjEjIiCGPKstoxTnoG4Hf0ZdISs-0ItTIvSHPCpKSxEU6nsXOsXRW8DWroNCn7x3E9gOJnvoenPiqu-N28FV0S8G4uXKxKDtOyf3CqULlZXqwfUjzwdsM1VEcZ4DdzUmcANyVMF7tPEfUew8s4OnH3EAg8xGM2UgcNBAkapk1qx-z4PodGn2S5NdaPyUS33pmYr5NyGedg6TLKyXvy94QZuYjt5rHuOcsOB_o3Ghb05z9DRYNj15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btXk9i9tkotGSIHD3YxGvRcHEhSIYOvrbCerNmqu_dzFApE-1hz9arDiWMMMmRBjUHeh26MgZzM1krjjRJMlLCI5QKoqW7D0NaJxiCzR6Yzf1LFQGdc8sIrH8nE6anzuyjUM1n9WfUaYC4Gu_j0KqxxAMoBLC4B1P_g2B6w2RylgANFMigEh9sUzU4oI6CXGso3Uc3lF5lRwb9fv7oeTsk49IyI-_mOTioCC6WWMEOy5JtXGjQxzolE3TEIDK1LynjLxrwtiMG0igLERi3GTEs9dRJ34QU3Fotb7b97RVV0gLIbnDELTKhDyCZmvyg8JHx-YfRxF_Cbv29Fi11jN8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTgjkAK9h3XVY1grv0Bw6P-twGtyxMwdAZ3aEWUx781YMx8T5eyC_FWqoWn8fbf6Lxs7gOyhOFK0ohQq7MCCrvKCZsJKpw9CgOP29_8QgFrM2u4hLDvL4PBXHS9mZVGgA2GrzHBHZKXERw-AFGeC93r4CIkE9gMjkj2XCt9-S1dF9LOnAkSa3aPyzOdKTQOV1tBdlkL3-1vxJcir-rJSI5XWAMHgSdV72X6QAM7UsZcldxCoGMpT9AXvEJvU1r7W91ql2Pq5LEgPKv1MbZqH2lgcX9TEOJeMzCl3j20oFANInUSZWvMzCeAt1kDto6f0w7-5n0KNTR3fALiQXKwjfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcITpqulrB0LAN_o9eWRLsFqfu9J4nlmeXyTcoBx93zl7LHlBj9LdVcaH4IHO3CVw6MdoKzq5ZC_4bAV6xxu2wtuTqZWgWw4HZdsfbCKR2cNqGpG1n96y5nen-bf9Rj9Gn1HywQl7rn66nt0Jqc-2PXlF9GUCaXJASC8lLwJ5HOGANordLAHyn_CvtNQFBBgFJbBOHyta2rynDi4_PN7tS_AFu1scf4P3Ewu8gau1uqcJlkAFGxvD_nmZAcw2KsJE7yJdUaw3ph0-tFKeYkkJdoxV_aPH7Y3rFM-xv33xYDChULDAlK3_r17EJcVUaHAtO91NDJ-GKri_QpJJRDFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cm9wBMdin71vrDo6J5VIBiDcUCxTPPM-DEDHiL3DIcFHOOkOZuDVIX6UG6PRM0Z4BXW0sGTM_tNwFPs5SnCg13abdNbUXW0l85xVrXXF4muWJmzpDI71qKrsP5aVXxlWAtBybZrxOKD7sNuY8YkBR-_joCHDDgclftXG2MTaNRIxAqK69VKj1zzJPiVEzdsOatjbgysVLnfMHL2p2-15sRej6lG1-U85ZFfkL0CF1llz5aoVKFRbWEEGBB3-rWMvdOs9ecIKXNAQYHUgbasYHnRFjVAqNMKx2KQv9jF2-w74pG6roAfxqso8fFqR7FD3AA3RauTVnzJMvbafH-w4fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=aHJsbxLSY0MIUcxY62Wt6jPGF6abzAcIuFTKU2S2Srq4F_46wJ8IrkJnyDkEyw1q9AOXXkyPxaMbMa4kv9m6_g5ILWDuIQh5fd18sWvcFTSjz-xd44MScA0Kt15yPqqn6NcpKEwvjakui6W1qzU1nuOamSkaQzlYFBMlFgRb1PIbEWm1VOJega-ld7hSFoVdtM0UMHpWZFjzk93OvaQAbl470dzqD9GTCpiToNH_k7Jk1YWIygMELgehHtXBl8agA0QwZ5H418WhnxjS_DCuZGSdBxBRmJr4w7Tq72ymbdD961gTKYS3hsxLyeu6dQvyOJRpZ8Z_ud0e634Nma3w4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=aHJsbxLSY0MIUcxY62Wt6jPGF6abzAcIuFTKU2S2Srq4F_46wJ8IrkJnyDkEyw1q9AOXXkyPxaMbMa4kv9m6_g5ILWDuIQh5fd18sWvcFTSjz-xd44MScA0Kt15yPqqn6NcpKEwvjakui6W1qzU1nuOamSkaQzlYFBMlFgRb1PIbEWm1VOJega-ld7hSFoVdtM0UMHpWZFjzk93OvaQAbl470dzqD9GTCpiToNH_k7Jk1YWIygMELgehHtXBl8agA0QwZ5H418WhnxjS_DCuZGSdBxBRmJr4w7Tq72ymbdD961gTKYS3hsxLyeu6dQvyOJRpZ8Z_ud0e634Nma3w4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1ma3v9Z43CBlo-uN3slKz5bVVLmBUEvJIAoPyGdI3oh0qLB_1MSbAtHTSQ-C0rJIXSklF1gPIvJS5_xZDM9M3TNstpqcrn98qa5VDdAMgYNyuqNrVb1XlGOvcVEBSrEXYbwRiLu73bCuqvwgLvwNwPWA_c4glROR9WFV1l0oVXiioN-fNwvf4H-OJL1DHZSg6Hzv9KdYaEJAFN0WPSLvDtKghhLQs6WkTUQUu3ANEqzvH7LLaywPylEHK6yK9DJtBKE2MJesckauqzPPvr7CnBSgdwjSgzzaDvltR_FS3C4F6zZ3BVlCEU_VGcwVT7uDuiDQWgjdIGo_8pJ38UFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwVsvxmBn8WvGfh6CgjScDggqF1qFW-QEaCGcprbj4-_CUNZVvKNkuhLqStqdki41YND6GARKjJ2_L4d0fhjdWQG67eJXmPn83LT5Vh0Svpj2-oRDfkKAEN3swijN7Q4gMoTCUWGrIvLF_JhtHDvT9L3ce0F_a7-QpNMFouMGuJ_9jigQCFsk7EuLRLfe-0C8MP68uXl3dQS6en2-ubGxhs_br7nhgHpOI-5Kq2a1Or7mdWu66yeWEkc1FwA8EyjuOCkp5nQYOGMzsu1yly2P_9PJljuYBWY328GF4_BZ7TtSF5uKQhMRqFSDlvOAVwgwDqjAcbUZgAVYukGZxJjPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mj27nL81A2ngPU1V3_gdwGc9FnLh8oJ1Mcn9SxWGrCnyo06GPNVz6AyXrAWKFyeUEBlBokUPSoQiPJ9uZkKoJB-odOXE_IaW-ungykzeb_HxXC7zWff9fr2tRAcxnPFhyC-dRScXBEfaA0scat_gQqjHWivs1Crykj_zgZywh0Zf16FZ1-ehSKw6tHQu9OM7jKE5DalnsgA7BlNB-O46xVS31x8s-kuHflhZUf7yT1Ns70R_wUvyPpptNaltT-ic0Fqtp_RAxO_tVGuZm0PhfoBiihG66z48wHa_VaAG1Z42YXjEPuBQpeA_vhOviXUMECejIHLKeRoBTM97YYErgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnMj3FVv2uvZMY9h9evZYuT6vXDh8t5UDezrtJud9gHrdo_W8mF86Ur2G14PwWbqSYELnyQEGmMZ6U2cQNiPF_bHY49YlFJBJ4b0Oir2RgkQALQxEzljkrKMOSWP0nsVb-l1S9NgeBxN6DK2uZ43MUGDXj7c_ygu6pXIVjDQYE3pk5zDZGcdFwiXW1WGvi3uYDt-pmOFyTqFdHiSmUlCSnrmUzM2ShGJjYk2r7lUSSL4SSs-ROxH5IUzv4vybIN2IIzmcH6McBXJQKSrmqBQY8X9FlewGl6d-gJ4yx4er04cImsHWsOOyRILyzS1rof6oqcqaawD571E3tA7zPbKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW8qi6_k-aghDDk9ZcyYrSvSc_0iuN9CN1RzdzHwgURWw0DapAhAXcI_2Y32HnCW4YcQPQTp-KbpDSpdn_p6ImW2IMClfqYzDHvxc8WTIL_2v9fwH58V9a_hNsp6BupFSqGwyL-bt8VkrM8sEX5r5llC0GKt4FCw8cerZ9pu3kk4ptdxuQKGGor3qVXEcIA39wrFovwrvBlaInPMBrY8HTxsUoi67p4fE2dBdz9WJX5tRxP8a6LEoo-dmhAE7bygoIGXPRKhuKquMRCDRIbRNLYfZLOKj87j1HniDslUaXGNs7E48L0vhF3dY5H90ndhgdAehcDR0x2nUzvdfKcbEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2Z_OVKLiKqUUxNoPMyMhzJF8MSIJWc1c-y-stvZ5xbOVjclmfynm9LrzV-OzlazIW-ip11voIJvm4ibvHScAIZVZIZxJ4UyHrES8rG7e4hdkcaXt5eDpqEl-V1Hx_2gDZUza-URCj6plHTwa7fi2u1UCTUn70Fg_-efmZyCiFU2S88aVP7APg_Hv7SeAsyXDUZrjBMFb3DAoSUijj039JZ90bl6654FbKlc7ay-qxYrxxlJ9zt8dktycjJSlFDxxN2ya3nUvV6gzj2d39-43YFhuSXikFC2A3zDYDI52sLxwV_0lkTJhhoigiab3-_S3I5woxm0N0L_fIEwatCSOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CspvQWz1fsQY_HzTo7yYmKLyoZiAq0Fg6WzLj5LOpNdbxWRjUUsUQJbhUVvi4BsZfWPH8KUAgvM3o_gIAHhr8urkqqL8T8T9K2P86d7p7S1t6Ij64ey23yx1dx3waBpS-W5CMmjrJ_u0AvmJuMt8H7wtsVgWTxB2-D5l8Jlz3ZVgOuB8zwfm2-8osb2hdOV6HBysKlwi7q12G-dOdahPz-KWgVSuHuzVUKMBc9xzbcGFeSKnVO7mu73GshE4kHH03qa4w6CwNMrSO4hibh7B5o05ZXqQbf_mDsZa_Ya-LFLvLlqcLPRrJ1KLcMkYigI01C8fU_PRgNUa7et3-JfU-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v83rzAHTq9_IngfRFm0iPk5BZUWDRaTv6XjlS6GD4zPRxq513mvZJGVQ3uHtuSKVRFYo-Xm7meUjyE1gfiNWYNMFfpSJvJ-IsbvY_Xf0NlMH6I287jAXB_xdWF6jEqEHANVlQomPuP-aZtC5bY5ALV0_JI4dtNrqffxrOkIp-SlehmHG5iLNH6vSux5JQMznmsrF6xsnOIPbPOhimSBWAlq0ZvTE-UAZ-PECyRM4S5sukRNIIum88SL5w0ou98zlJpnGWJ_cv9S-6G5qbt2ZhhSZBaBVQ4R_udCAPRujPY8eaRp0F5PfuS0Y-Lr6pAob2H-BwVIeO9WVLWryajPJBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=WfOiVsngd95MvJJjyJhNMUERSVE_k4Kpc65Om_uz1-aHnCu0hikMBIIXOrGzHrNWd0Ihe9nWQSlQ9DHvmv5qJ_wFm_eABfvvKG5CpQFVl6kRoYAjiAgUtEjGs1_bo3k5B71szLspgs6D3BmJmBlDzpnUkwKW4g10VqTCSC1W1m9cYvvz6xzWnWA2lw9U3Gd6sTLd98qu363eXW9U2MKnK1vpqnkriqsQcifCFYpPhmjmnK0ZpRmdwpcgX9A0VPZDCwUPGw4_EDBYNAdy9G-BsC5HtVtJpZAngNY4_luVy4L5aWURuZBizedKJesRRlvyU3c3wwdCgd5xlq3loQOUrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=WfOiVsngd95MvJJjyJhNMUERSVE_k4Kpc65Om_uz1-aHnCu0hikMBIIXOrGzHrNWd0Ihe9nWQSlQ9DHvmv5qJ_wFm_eABfvvKG5CpQFVl6kRoYAjiAgUtEjGs1_bo3k5B71szLspgs6D3BmJmBlDzpnUkwKW4g10VqTCSC1W1m9cYvvz6xzWnWA2lw9U3Gd6sTLd98qu363eXW9U2MKnK1vpqnkriqsQcifCFYpPhmjmnK0ZpRmdwpcgX9A0VPZDCwUPGw4_EDBYNAdy9G-BsC5HtVtJpZAngNY4_luVy4L5aWURuZBizedKJesRRlvyU3c3wwdCgd5xlq3loQOUrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzDXSyuhjjyzF_ZgxkS71gZZdV4KtBFHK2Nj0ZdSXXgXhJMSkttRcZaOW24E_Xvb_Xfp-5m-tCx4y_k2oJU8s2cGMI7heXXTnOwvPI7Q-n1MD8PLGeGK2Csk-lJKxz_wbkTBVImU8rG-xb9HP7qSvx0hWiI-eMK-wOg3IdfWWPJUc9OGLNRbVeY4l105mzpQpNDHdVJ-bWUcaxvlDifc_MnaTpOa_5gOCrmeOM-HJttFc8fQlCrLrrTkmmDuhKK3mgVS2UU3d-uPuAI4sH7kLtwfKVcy_HA5u35sk9IQ4xXeFpOUL60bnVK_5xd79ViTJgs8dXNtVcjVyXd-8qkibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUj8m_P25gKorZuyMKH9eTyKAydhCb1XSGCK2lTeW3Sjnj7_J1EM6gOa95i5GY-YYg51KKXI1AuCXsia3BuccB2FuqAmKLD8PSPCmT9BT8VLiOqioLfQMu8l6jkSd_9rT7B4QVingUBqXY7hnr2OgPVjN1Qi4Rh6ZsWeMOfOAvzc43ihDtw1muKw94cKweossRDK909dwsUaTkDaO4bBsI1xscepgGM-JV95Dg2QO_hllfPyGN7W6KEC7_L6mtXPeHTKE9AuwkezLKp8cJteD2DDeCiNAaJXyt3fgL7dBIBNJCR9N57BhsyQKHznc2KwIawFaeDnFhYli85CxYHE8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=eq6UGT1gZM8hMPR6zGpdu-_eoNIt2Xiu4kj8SvrHFFvqlTL7lqeZhksfpEkwKSf75xtUyzpIB4vrmIhCmMZaJLfY9VssKRB4m-DHguYPDyonNsTqiBUsnokfU5T3dbAK2ZTshWavxyxe0QD4LKTmDXIfwzMiFPUYziQN5oOXlhIKnA1b-VFqzZ1N4HtBgJA4VCZBwrtzvEL0l67wcex7ZXSou7Ozcziov6SlWszT8t8zcK2kVdqvQLgrRVhHQ6IZlvpK3zHMXbQRdcYjHPZvP-dWvtDURto84BdzUdyC5OKnmpVLIM07F6pj9JTrqAZdE4bdXjSS86oXVGoE5OFevw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=eq6UGT1gZM8hMPR6zGpdu-_eoNIt2Xiu4kj8SvrHFFvqlTL7lqeZhksfpEkwKSf75xtUyzpIB4vrmIhCmMZaJLfY9VssKRB4m-DHguYPDyonNsTqiBUsnokfU5T3dbAK2ZTshWavxyxe0QD4LKTmDXIfwzMiFPUYziQN5oOXlhIKnA1b-VFqzZ1N4HtBgJA4VCZBwrtzvEL0l67wcex7ZXSou7Ozcziov6SlWszT8t8zcK2kVdqvQLgrRVhHQ6IZlvpK3zHMXbQRdcYjHPZvP-dWvtDURto84BdzUdyC5OKnmpVLIM07F6pj9JTrqAZdE4bdXjSS86oXVGoE5OFevw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
