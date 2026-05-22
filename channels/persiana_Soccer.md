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
<img src="https://cdn4.telesco.pe/file/iHZPG5sPno5UTzTIzyfbUkDA4CvB7eTIXAWUQBEuy_4yEmCK0E76BzJEs9GEi4reO8e0DL7z79awUBObbBJhmqyJpwlUNEv4FdwAQVP1thMNPgNIRzvrMoyBD885duh58vTTrQ9bpj2PImrUfsP8y7WxiwKSUOwMhOczUSlz1INwUBPdC3Z-vvjEsnvjB-ajimLSYyCuHjiNR4Nz0AnN3oexb3qFtrGfhaptYvsDomVAfc1M4Ezm9Ln_EAsq0s6_lIt2PO7x92GtUJgA0kf5yKf2wyHOls_yBJVwRfaoYwq7FbM-0abprQJhXshwu13wLNlc-X8rX7nk4Pde4jHFAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 199K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 06:04:48</div>
<hr>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA6KKRUXJsVzi1aexljtT9b1dyuuES9fI31Wo_RewXu-HJ-5MQpLOupKZZRaaw_8ZEvcfRzpgkPNIGrbw5yMKg98mndSLP2WTcKBwYgXbfUoL7qeaG2_eXf5VaMQ4_d-Z8fo9HH7iU6PyzZNF1u9M-qtlYjkwzriLKCVhb3I4RNTGreMOeRixL8_SsQUyxqr6GkjEKaGCfaOnsfukpAirF6JrjlKIo7-HZ4Z8P7bRaMQCs4V4qJeoRhj2xKlk6uf6GA_qSDnVW7Ufn5FttpvAxfqM6OitjF_msmU8BNp-fMHrS0yEOyhnmiXV9m5Gt9ZVsN5KIX844hHB0pepobqtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqicYASW9B9T3Ua0z-s9Q3VVLnasml1uorRuw7W5nJ0QuiCLQTQC8K8aRF12PYIr-cXIM_l8kq1TIcGrQ53b-QJK5NnVPBrBW1QWF6z511HEqnOpVm_SJ8eABnameckWqNk88Z96LAnHKFXWoRLhVO4JUNDiR2rURqGCVbbNRJAOe2mznxJp1vaz93x_NrLNUqj3LEBKrn2m4Q3M_J5zZ8HyHaSOZPfrL5Iu_L7EUNXa2TlNIM7FSq_CiSWnBkPV3IJJ8rmnZ-gxNlg6o6LLwKzEgKnmhWFLuJeYiQFJ1JuNPYs1ppYLRdLJUN87dF9AklKbDhgv_Wkh5K0JD4YhXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jRrckIYxNaYfaa4JXCJDqIXmYIshKnxbSpRaRcY2SqN227CUrQFHogFEVG14CAj9dTpe0Ua_QdnZeYXqwy8-F6-wS5WDD2FTT-wK8TDgN0WuhpoI--JwM68O04KEEmBZjNtMN1QDuigskpnXeiz0vCfSE9yPnapbVjXqSNbG7oTMQZrI6sA3rqupW_B1wiiqOiGSZTsO8PJjs4WAZMwpi5LsTUvbS0kMuj46ee5w5cET-xYE7UwSGlqrO0wH3VjYZJd-9DgvQ0DMUF9IJ0RwqjVUYXX6nP8hy5pBZo8M04XLCmvLowvsF8YcsJRP3NjX0EPaDaBufzVB9nNebO7ZLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZIZK7PMtCq1XDO3-vpzC3d9WMQjWa3m9UXCRA4Md47dVr7ZfSear9DrVXIoH2m-Me0MSNvfSOAL1JdsifWUxPz1B15g3uO9rKh7Kd9lnd589MRveCbcXHLyDxtbZBNdUujkLbmvgRJtFXlOk-RVdQdHRjj4_OHETkGkWJQtTD_jlQap5LUZbd7WByueGx42WO8l7Rngbds1EWISKdMT-bR_7SlbfV6PzICEkoUtjewUQXMquZTHkhvf1Wyloe7WzxnZxmrDN1XiaItmGwEJR80AeMEh_bzw_zr9oclqFqucxybj8uUehsqXjM1d1hYcXBft4PDYbYlGaMQgZb9HLAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg4IOQy0Kd1_9mlj_lfwQpqnrprn0od0z3bqfhZZWs4kB--kCw-bUZSPI0YILtLI01Rz4_Io5d_wqSPBvYay6BBvCRA1QuLBNuGmzE8VMBsBQaajK9DiVxIq7xUCZGM10LIP7FFAi-dry2U8i3oro-MFSmR76tU95tzdrMb3IBgMsxipgcBaHvG8yrEfeVdM6tY4p0PFEO1amSmRe3frBU9WXvC1AeCo_AgqgqbYI4eYcbOgUMmtcmmPerzEP9Hvsg6uFkOxwtxhvQv99wGX7t0l1ihrQjSJ8LLMqagaEg3KgX4Fbj_DAPtX1C4P_7ISAl7n-_zB38zrEdZxGY6zKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlnjSF0k2tsgKbT2I5qzdoW64vdbAmAIH9yCV_xV9iy-WPTtXEzCiuw179FBsRladpF2dYF5r2BPxW_pJ-iEWYJiq__Mre-YWmst-HXqsL0HXpfaXr8g4nGgpVjO8ETwhAu1s5kRpNJmdBk9DTck876_8dzM8iN7OoR6BaQ8VvdyvhMu_BDHFtQ1pZXsSm_yi6M0OPfmfPE-b8gQ3CQ-Df932tDHzCc00DqTPfygLkp28e9HNsalU6BYYHkTRprXou37c4M19iJn6edZ4lUouHZRzgaMF9gSnWLGocjGBfT8IVa8ocdDGONaTOT6PINT6x7cpNIuww0glrfpBTWrvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22227">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/persiana_Soccer/22227" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYXb2qaeHjZCkfZCX6ux_uYGsr5IAM_GzoR4Ydxoncwy7zBGg_qaPKkaU1qKWUBw8qWh9uXBdmeTQyxWb1g64g6zYzzxHKlZbg6jNTfMGTriGyuNuRX8poscqIFISc8UjJXfiH7Yn-D_5mNgXMm5TywAF8X_MeIuEUqzVulGqYwWfNHfYmHziQL6hKlds7HwYa-2My0NBHgxTOoeir3woaUbN7mDFx7WHNltQ8vlEAXSRVcoA_DpZoUhq5Sed5yjWWKd95TC5Mf7p2k14SHH6aRR8sKl1-tjuws0X_3w_0MVH8qjFDALntB4OrRChl_Lv0MVt7sN9Tvdtybzg6cfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfQ3fHrwdAwA7ID9ojM92JvHzuhT4bAVFOXpkKmJls4NombMD2vXcKEQ-GxKiSMdBovAj3HzertCMsWSpzrdt4v27_QIlLIPrfKXXE67ej8ZnBcreENOGDaebEYlbFfJbcikIIo8Xr3VNUSQQGryv4dNu3nxtcYXHpktT6DkWKjbWuZWSxAb8KHu1WXJJJO-KgMUbiW_FVXP9FSjGaFYrCVh2boSdjpLgdiqxY4wczNAfxlOtgf2nbfdNidgRDW9HIk8lp0TwNU7uR0H_2eqRlzCUhrgYaK-doOdezuQzAjh5vEvddqEJJoqa5BV3EGMCGG_VDsRG9Aonoc_uete9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=U3JNWoDuDTTayX8AZkq4YboJGAA1cnWQRMNc6j-maTc6W3HDK5WQxtpal-V_SzJbGMAfCDb6PZ_Kcu5hpaMqLHrqZg25WpFFhRHW7QLK4xswmJe0CkenH42nA6jjOAkF0KJqtNBkrozkFU1_uT_TbFDIuMBgc0F_8kd_UFy7YbLL__VSV94gYIhCbBbrwG-VIguLStdtE3IKn_SrEayqLQjA6yYDcuUaX5S3_ekZe_Il2TA6IM0I4pX5yjFhbET45ExZq0XIlu0pK8e4etTwb-6-cGuxvGAg6X5DxBFkHNSaMuIuuY2PTyOigdXO48t4fUSMxjaYhmslSMtKf-0NjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=U3JNWoDuDTTayX8AZkq4YboJGAA1cnWQRMNc6j-maTc6W3HDK5WQxtpal-V_SzJbGMAfCDb6PZ_Kcu5hpaMqLHrqZg25WpFFhRHW7QLK4xswmJe0CkenH42nA6jjOAkF0KJqtNBkrozkFU1_uT_TbFDIuMBgc0F_8kd_UFy7YbLL__VSV94gYIhCbBbrwG-VIguLStdtE3IKn_SrEayqLQjA6yYDcuUaX5S3_ekZe_Il2TA6IM0I4pX5yjFhbET45ExZq0XIlu0pK8e4etTwb-6-cGuxvGAg6X5DxBFkHNSaMuIuuY2PTyOigdXO48t4fUSMxjaYhmslSMtKf-0NjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK4yGsyvptFLNMWGOl4v9acUO6qHC-hpSPttlwkQV2kTNVejJ-RveOkEWWjxp0PPnIupEnyRoZEkWDU7qZvPUnCNVee0BD8CzjKeVbybwF4GahjqyxesuitIzJ1tuZqgcjtYB2EJVk6jxjxD9h_aeAtGouJ8JKtQ6UvPS6fD1SLbRrhnVsW8xxGRypKtvWq3TF_N_Wq0bIekeE8yEzCSsjx4zrDs_asB4CIkZpsCveBPuW3l8zOXpq-WjtMi3dzlbuzs_3Lqi-wpD-elMWGkE5cmSxErD22IzMX_jyszM7epnppfcMtrdotxl3zxqw0vRGcFux9GllPKNeVvgYNBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22221">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/persiana_Soccer/22221" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtlVm1QYfhNa3KWryIxcrc9NmTACIHB4-IO1Se7TnR3CuJQZRyvim9uHtWmEwlTOBYWdhkukBAkQCTr2vdJbDaiTS9Vzrlqww551k2zhXlbeqlJoswjkOdxDSUUV5ZAQMJ5NNsSDVIjXIl4JgjjVI5h0wVr86nVK6HBjbWdF2aXapGvyXjWUO-FA2MvL3Qm7Luj6qAYKmTWh-Tj1O8awszQYMciPJVn74szDD3f3keT_Ar7TS4IcqenGJpN93U1DoNPaytpFNBSULh_qK4SLC8fD53sMdqPjbCfBJT3vgryngv7IFu7Wt54xcxkc2Bpr21LHuBRhGq45sWfICjY4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAFXt7iXfpxDy8d6CJ2EWwkApA4AwmAbyQGRlK1t7FQD5kghlvyDYUJME1ll7L_FG-pG-XgH01yot29yQzRp1tKLdpJxtY3ayfVSkjKoGP0dp0U8T3Jr0E20jC470d7Pq3QqbDrQzODr_xLaZ1UJTNtcYE3TUvpRYE783G6i86sQn0lHZAqwHy1tO9rnCayRJKd3Ng9KsADIbBX0c31yGlKAHe2nXe_eQhnaVzpIdUVHvBio5Xd-1SUcdGjpMjv6UzDVj7SHi6EbO9tCWEVADy23Vy8o0eymxu5xTmIvbfRaUdUwWrf9gtc8NLSOd0vavEhxROJjiUevbxN0oLR-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCju_4Z-xMDrb6p7rlB4pTsN2mnw03A7r99xYGWbtBC-Q5LBK2H2YjR_ieooKqbd4w2BM4dj8sSu-Y_Urhr4ErBX_9cGc4GsQ0NgxNajvSr6gSlgouGpcfjxX6Qtt9YarD_PGtQCwuSGZhUxiGOvjejmM4ZZ_gfJkZz0_toEDl7OpSoZNKDzz9id9ldjhIEGPoa0ZwSYEo71g6OprphoVUPaSw0p7X_SBUOQ9JmhXvmBu4LRjpHCNJh2kQJ3xwsuQvct47HrRhTzRyj8OgY_CeqYwwZnqxDVuI4T9c5R66RKYr-0N7D02nKre-I1toYn8RFnFZT4xnCZIX9vJkB-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER9Bjgd1jzDYxTgXpIihhIE4C9yXPruvLVTdz8KtKL7QT4cVyiTTdIP1rtdGDNrFvBUabB3VC_o7njE1h0KnizWxG0L5yg_dcYC3L03PCVjVVUHV4p2qhG9lvrgJMWik8VzfEplnHXZsGUJDk3GT9IvaT02rTp2_SkXrN44rB-332oCRHCDJRPO75zITxoBY7fe0rNSOxAp1XPO9WohMFSp33_i2_-96hzkp7ypFCgXDblroZiMwzIeJpfjDntNiv6M86Z1sP7gL-zQlqJDbp7HYXgVyJwA8gVokyxYhubEFE-ouqZnZrrNrv1dG9fdg6iRPnlEITFFSp-vb0viRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozTikkFV7fX1PtQFMlrHHloUhsxki46kQfvBu8-B7rT7B0W_IC5gQlxAWPwwQ8TY5tFZmYEY8cmZq5JDXoj4nZrvOdFlyAEdjVT0gc2Z6v4z-YW91pfGhELvcOtZeNFh3IqMmQg4z7bRGARagU4-IHxRrY784rnda5o5nPJvhwyuLtl3olPL7TiGy4xLuPvUciPnUVDcbcULlDo5i4TNSDStjy6a0gvgWcaNEH_YP_1iJQBitRCywXAEPwEb2GyNkuc5asx9ji4-LVzI34BTkZjPBnw_sPZWSSe6fvVis3rLznw3qgjaX5FyHXwfTsr8vRTeiOD6qGYdnHBxWEYDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6J1Wbytal29L_FmGPKtA1th7RJ8g1vI8LQQI805zQI5oQNVsAlINsC_d20YmiS0nI1TYR4tqVRK1-V3eg7e2lIQ_ce1B7lCm0JPHmtlp1ypvA3QBFnAmSHiwelCImc-Fo8VL8ItYsJscKCIHhz1RncU6VpbNM719uD-xbSWtsjI8PwcVVFPp6BhgX29Nb3UgGSmr839OhhbP_iLfpNThMO17d2G6cZK7ey6teNfZq6jjq7wpeE9E_ymTfuRCXkMZqzKObfyio1Mq7EX8ldtr9UNDrXjRuvhkwNi417FWEyG10OPHx7Ti09xmQCDIPv7O-ksdLKy3i_Vbc3i2mh2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kuvaL50hQz029fHOw8BvuWiGKprXQoMLEQ_XrW_e8rl5GsmSt7Oemkt9xtjD-CLQ9MyYD8LB5DiQShhDroQjxf-ZnHmM2HZ5i1sVeNmkaDtsPawSEC7syxg9orI0Segb0l4Tpi4DuWEdVOdXU4dp00PGWtddcpA6tDQ_O0g8-CSMTG8WuiZMKgWKuO8dSmweuZrKHtDj0iU_NfFLgzN6VPiXrknNCSlVbwgfQHPyp_Z7M8ieFo-0z1f-n5uYtdgg2Brj4NmXvoLUQIxwj4xvzpiWQ3WGNIZvsnn9IzvHy3meWFhHzSRsXgnV9K3Qtcuy8aOpXql6SzdL57VizU-rwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCqDZM4DEwTYx8a0-cWs7sjAK4sS5VlkH5iKf2yi2SlNs6jPL8Yqv2RdkIDRK0oDuK2KB5ly1MSmxgTzBqW27_uczXdNk8YshbigiCK1Zp8iH1NXQLQUdzpU6hxztxFGukhjLyYNoh6778O-hfZYEaa8bnVYTudeuUdZvC_cgZNyMdHjuebPa8-P14PNINTKpvm475jycq-9txSlh1kNDsJLDS_ayD9pHP2OQZZDUkA8kHI0ABFcMxV-Uq-M1h6WwTbnPLK7seZ2zBrKunaomlxVFQFZxRNjbvX9W40jsU_zCxOE2hsj4XlwOpeabBBmNywrhqzI12nnJ74Dl2oe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI2z0mPME2ZbfVurKhKRnHgHUooRG7WMb2ns58h1K1Emz-rXh4xMFhA-BigB2M8MV-gQzpW8cB6vnxYod_3WwpS15yQPx-a1UX0_SCC-81yZLWqJXjCTl9O9Hj8EEKooy7yyGZGNhxkGmtUiKEwwkqXQFg-K5nmwq8ugNKFVi1m7RK8_xsTCVuxy7GnFlM8crDhmNosGsYPDGKk12RUVYLgJn_Q-rvC0IvcDdC0Ue2ZRugsRSXGxzi7Q7uZqRHTYG2qDinqCmF2KHeI3pBVeS9qnChWUZYjRU4aIdER3rJRmWoASQQhmEvKSqGeg0E6ER700Pt4Prb9tlbBGj6ouCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV3eH9UUzVXV-HUdcTjS5sXIeL_YUYVEQoX-X2L3ThiE5boJMjrRXawI9gfQXN6aLUbFEPJnUl_kN3SE05nbuKyyytjobN_PPwElLKL6fuC08NnLIVjHqd3UV9c9r0nG22Q-ri_QJYCkvCNFmko3xxBjjMlOuzZwzPU-AOgGJ-xYvlKxat4Qq5tN6M8s34zRetFobo7xeLI7fewwwiE0BwaTt6lo6fUvZ9m1PKNiHzvsiyXALLFTNHO_UMnwmcH08qyjBDhdh53aPgI1CqwaYt4f5vxjRLBA8DzwWKkM1bM-kc4dru_8GmCo4dgXFwoPKlob6xqpdfOX5X-mpR5d1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npoG7uOZG7v58IlszpjLNRkLURrtp-LZnG1s6AspE2Qtg3ho3jFBGlMjLKtploeJeroBAKKezRx5JuNRxt9mmrewF8FaEp7klwXFrz4jrdGfD3rESliOvnKYJ1aQ28Gq3_qwGTxnABSEfEdqvJ9mnAbr_e81RAomsK3kjubhXFBh8wl0NOYbq966VB96VV32R9jGkgDvYnCyHxUbcrd68uI-lBjwEQpekRgTSDsY6_bAnqGwJSi8WXzQerJFv6yaeKgS5V03FoZbecKPGzits_3HPyb3HskKK6chNtt7GihAzj1DxPJWf4Yesj67G0xO1jnBfNUjglP4znxE78lJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGKmx7HPVr7p5QEaN7kQFylGGgiMIeN9ZoHVXAdb09ch029sDwqRlhnmkTlJ3Xkzg_5tREKOGJVujWBp-aa126NMghnwfhqZX32xqavMHm1bJ-5y30iQOVVSTZrvUGYldzAR7npGL0dMfgr4DhUgKqnSEPP-2IUASc6Zit817DReSInZ-BJO_lbTCCZB-nwXZgBbY6g8C1SuoQp9seNIxixERrzONKA4lL0ZXC2j1xYixbmZWB5U5Y4XCyW01mzl1RxXwHzojADsqu96WTos8hwfZFimHF1bOiVOuaVixeHhc1wX-Y4kEEDF_RZswyDh4eCVSoQZY7y9vlrH2_zHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-JauixGHvpFMKFXECPThDbat3wj1w1UtUbU1CyS6GbaiCrLgcVXxww1QGjDCDoR9pyEFDVjdz6dlgFobxuFmrCSg8-qR4WEZl-PYRrfEMH8y6heKoAVl9H6RySmrD7uJJ-MSz_eXG-Csu0UKDwGrhNojOv6STvgHVl3bgTicvzKqkBC3sXQCO17JNCR8uLE7rVCLYro7KRmE4kKI2SO_S2n9y_1IVdu9j5jZ0YDd7E8kXYAheDLviKIG3tg0mprcFCiiG4dxWpylF8oYm4jduKGdm3cVjOhtS7LB4qRlQsw_SBoC6o5B1f5aXsKBdZGyQ9I-KdKsiFFY9_uMicMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDlUk6rvoW0CXQkGz8tiNI3_P0m_gJCLTtiB60EL7m1D8T_dx5l37CBNkkp7gHYkutgsWzu9F5jt-AvVKKegMjsbuIlQ0Z3NerXpAkZ024qki78TePMlrKkVKcjmk2XH69qQHDdxlDFDQnNQAPfi0aLGaQ6VYsBshq7TCEG4xaQ1rdBkjy31QAgX6fWsGGAeltUa7hVzRrVb8U7xiRemBd-ZeBu4xkiFC0MnMFevkme5BSLt_MiJbXtS1wJ3bJSjSKNcbSQ889sJ8J8Zk64UklumFFlClE6qwDE-QEvy8jbuNUQjHNVvGY5Tuw9UD7YBZlVFc5IHKC_AdGZLMlbyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z63AfyWH5le5oOFLmr-lLdSr1D0rW1DN2ZI-g3RVephJsXeG4HWhdTpxOKPjft2XvQYa80KEHh5vdlHWkCElItiDCZH4wTxo2preHsbT6mYOPEN-6GlDPMwGgJm9J0xkBCoIIxfe7oHNl_yhQ4azkSdTvRnGdHBmwk6PHow-F0e-7HqGo8WxGr0ssg7huuLeewDeON5Itw9zZXpu5EfeqhNOjJUf66yDkHsjD8-wFNc3tNMixLv6qQLZtnSnSCptdwo-Uga5Y6EqLtBkmOAU9DItFWjpvlxbYTG82B8Q_aqbJXEtoh99Co7d7669j6K0i6IM5BOenBcO_wOlUvYLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFF5hkH7lruPcje2_QC-3YMNQUJsiLirri3bIGTJrL_tFbxMTxFwrUB9edSdmAy-_Gf39WtwFlBt4S9ae9ceG7FJhuH02bgsGboz0ECElIme2iYE-JD5OPC6mxxFB1qXxms2JOfzTvPvaa-wmRtY1Gj7V3g__KmtdXaeeR9Lx66KGsIRhX2--5niYba_5ig2-g7qBNvzSgOcCy1ieBBAERr67Bble2d0J7cFJI4JvAiNSLG7H2V-DP2mr7MWtJJcFgzgbE8UM2DWAEQ8dzuLbsmEpg0fvVavzrVJJkHXGDwijQQYcmepwtneQRA813YN_UKQafymOXftdE9HLp0Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22203">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RomZzbYopIi5vaZT2BMMj2RKA9ZQFeUfRzQK4ONaf-iK2Te3CuX379XIQhXGbF-FUjMr2MprKZ_Tm_AkOOue-oqsgZdqjFrjxbRa-UNYDRnmpDKIoLwpOJF71pjxiLESlUL7V7KPgboYf5LYiUlhJ-DzcV3SDW3e5Hbf21qHIuaXkC-IxYDqURv2d8y-nkVJ2k6lgpmvyM2vqgX9Yhogonrfkx8nY4H3S4eJRr-xh5_IoYcSGK81QLN0ZZ4Hu8tVZW6HbUm4vhETUqdlwVANelAos4LDRzI46lOhci_CFt6I3XFZMZxqQEOYa1TNhEV6n81Tz8f9HLCvS4W8wW3oeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22203" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22202">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnEd2h8VNRtD2eBmORetpxkfPKTZAORBfqyuvPvqpeU0bz8ZAfUWZ_aA0Y24AzJ0p0DzrLaqO07FF2OPixn6MEDj2wTZ-8xTAsL38xq1hgvJ-jzUSJ4LS_VPKcX6PhxGvlsP7LKWnnObpyqTSB699w6i_A2nHWCaYAI_V02_nP-P3rRe-d2DGhaII2E29p-jHmniUeRPXvCYQo1YyEnkhbYsCywUkNiGvLmnKRvSNlcbOx5XPS41ayhKKO3euyCeAyesOojDuKTM-hKDpCB7glaZ8VAMwZ5FP2c9uv8Td5ofHxs5wmqdF1gWXzwp7V6ZkoPEFyvJig8xJqSSaqWOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22202" target="_blank">📅 20:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22200">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NSYpu9KBPOVxRwSVRY49CX98Uwi8vYLyY4CaYm7d5PN5JJRS2yJrU-C5nYeO3B8S40nh8C4mozojTmc_oy1Wi0D6_M7oG3Jo5x4csNi5cvxnPanskR_Pc05AhuYoQq-ezn8luTHZ-vBoG-He-vwqQe0PchNZI0GhFBZts_7FdZoWKqCGRbas7tUOgLoSChG2xV5Y9sRA2vH21JNFtDQy1jyX1JgORb4ngye3PcCOMZ0l1oNxQYWlnccIgDKTJSobKvEwUCblPspPZqLchEr45UNdIm0cKksbAOQHKUzMymQ1WgPUagjX-5SjGsjAPxNFm1OR1dY68njB5ciBk6eewQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0CCFXfTepsOWaOO9cGSRa9vT4pJcCd12ZRQsziTysnlXyqICl9OAJKQ6LFRb77gSQLYFoPM6VyXG0UUHMm1ZIZv31aIwaRPQAmqk7XfEtOzwJk4fdXa8SCBctRBruSAA9ImhoNbhIgjTG4WKhF0XilxMcdl_loi6rH9sn1HuR9QD-k1eiV1mpx-yFR9Ydp6uoqzJYwH2LyXwFhs5FuYHVuzse6zkmeDcREaEFYPi6lnjsL-CaYfWXD6R0Mg7xXjRE6whXtJMvzQ0JRIlbu8nq1eenLk6z_LHRpcodrkWFSSZ0m-lmKmTJ8HON-sD1G15yi-oMVIU_CvoHhU8awqBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22200" target="_blank">📅 16:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22199">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22199" target="_blank">📅 16:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22198">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIoosCMt7IUIw7TCaJmTnpHNBZkwC0x_Ipn9k4gUXA70ZoG_ddmUi4M-ghIHTU1BL0x9yZa5XVzQlWLoku_K55UKnbox1SA0qicc67qYCB99iyeIqXXeN1n8ar6lnRfk4dF4xI2zmA6hypRb7ETdLOC_YjMMxr9okXpvu-hujUO_3PAcmjiuWrXy6KRk1-wnWP0ZpRqiA4xK6bU6qAC1DZ-B8I8Det7s83pWQ53RnA-KBSgQz3zHNazgI5dNlDPNVfVHCGfzeqZ3OcDo29mXU_peLvYwhd-4C7glNdWukOGLlQ-OCDWs1uv-vMyNTiOvWTxvHx_5PYyuRIG4pC2WCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22195">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKcT6nZf-TyLB5YlbZymDxVnoZDLETVBlsBMjxx-wTrzA05aQZQVcI6UyxgqxZd0xUWBryCnnsI-jYePAjHDA_anv-Gwr3JlM1tV-GBf7VvYTbP1TdccPxnNq9N3P-qCdF5yIlUqhtKXsBa-_T4Ufx7Kq0O_K9ANREcR3shZD2I6_epy8i0YiT-4WCfHQVe5mODxxB_iNUsMKcuxSQadBEXZVfn8mYkK2dmafnV9_pCtimcocpKnlnLOYeDZ0ogCnvrN_L3voHxoE-vnidZQce0EPYtkb0zmItLtifKlETtVqJPQ1Xcll6CJPtb7VKOOvai7YsnwIM_j-aR1Y9C0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک‌ترکیب‌احتمالی و پرستاره تیم ملی برزیل در رقابت های پیش رو جام جهانی 2026 آمریکا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22195" target="_blank">📅 11:40 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22194">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUmG4gLFVh1IDAFSe-b_oxCwxOsjhMstwxnBGkFfZEX7D-00Ksb7nrFwqPdWUa9NDIjNFApb_KRliZ8bxI0I8yiw-tNLDBXhCKG2Uzk0ZqbmrLjG_iN5XFd4XhbTFJDuHXCFd68WN9JdiKW-eXhbJVP9xhEfv5AuwJkFC8xLW1qtuo_GCFxG4DKsc3NC2to2usJg5thmuqrzpaxiddrW7isGf49l604ETxARJk9bvZr7pl6DoAgxZHessgERa-q6BEzItleQoHI5rpOK1AZabsTFNoi39SObmQCa0nMEjc-xIvHj8H1jCj7agyTkKrRvJKW8VR42J7Kw7-jgbCTJhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22193">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0qEDm_FW1Ysn3j1INYn2t97p6IaX8awnFbmMLdy4go_nMUNKhw9teZWpR7TsHGT1Quvb_lPpPYQDer4bOaBiuF2uFuHjgIH5kTM_znkGeSXEFksH7B2eUjMfeerUmOSh8_TTWwBOHH9kI-Q1vARh8TOMZpzKnKscRIzFb_hdohXzZ5-saQkbi_HjYBfrKPEqWu5jkfco5vxbizMD5sJ_ldT4-hg1uLdpzEJN2-leWKi28MM9uUDmCVUvLDVnxRRIgBEttjnwVuCnZ8NZyR3eeOrtrMXPr4jbY7dlJMeel--cDgKep0W2F2R5ox1c1Nh9uoT7K6Ff_rIcXwUirXAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکوردفوق‌العادهCR7: حضور در6امین جام جهانی؛ لیست پر ستاره تیم ملی پرتغال برای جام جهانی.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22193" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22191">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYi52irwYAWxNTOzq3Ajug297t-UFpDU4hLj9yn0G4En4tur0OMsP0pwPSBwunWK0RJRWDoBPFu9Md4lf0Nnv5nVT41QyCwYHgJMp1TkP_-hyO__BpXz23LY86RNKJiBwQvdMQNNCU4nOelbO64wVP1lJxUSDLQ6p9DTGKPvNVPzaPY8krxPjW6qhhrhXkjf6_QVf_MC1E7cdi89mXRLu7RSKhPnUy2vqfNtVbryIozvZNR3t9lyVdVpskugA-NgPeUahJHeh918AZy9kWJcUeMua0jMmO2Zimm6B9a0dF7duWtKK8_tAfEk_nBBKttymzLMfpcEsG147e2p0Bu6uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zo2U381k8RacnMdCf7Snq67dDgliSeoIVooMQlXHH9mwXRRvlwjZqvriHy8wpA-hKaTdfpdJ5pvP5saKy2BdIyYAV-qwDpquC9c6OkXK27yMMnEjqAqf2jvEf1nXesfQpd4qFmfCWDsGSjYFwNGTiFbdNCb2e4V1lUFf-QTvWKHyxW1yVZGARk7v0GF-9MUNlXZJ5RGTICrVL30MnTMlUJb7i3UT9OlirESLQ2fFHrYOCznQ9Y1iJQIBBMSr3YYiw8Ad2RRzxSinzJMeRQPYLckO3Z---kLk-gRJKiimMc1m-fMWALTAXIJ87AR3stYCKk6yHFmzTJupn1XIS5t3hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jizQDWzSpBcgKElqakls17qP6qylBDKmVLWbbgIIVRDPDXIiGotmccC3t8qiBLq9Jo13Vxkc02JZZk4-NE-m7IP3RoIcdkacfhw7EacmE5zsxxHls6N7kBkhozwQz4TA236SehMSHuZOQaFJx5EApfqF8P_7d5GMDnV7JVKGdIt0LL-eMPKQx_dFfWDZpf-389b1O7MY_8nsI33dY_qOzfMq2F-MCcLm3yW2hIfQeVAccHZKom6kc276golVb9QMHLPYC3hj5xA3sRZQMpsE0fRVUEWIqSNahXLwqRKxfoW0ldA-N94FtJdAjiFC2iQt1UUgjHQMxQuVyHXoMWBXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند
.
با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22190" target="_blank">📅 00:28 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22189">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
متفاوت نه اما همچنان‌چشم‌نواز؛ رونمایی از کیت فصل بعد اینترمیلان: لباسی در قامت فاتح اسکودتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b77lzPy9EGcTN2-DzunSmvV7PPWDZI73jTz6MGkCnKdIidLwfPbJ1EGHbAdTbqiZy4cUygfprTuByc6c6gMwQUui_ZzyySji9NPJxYgcs4Ct663agkI-9lnWcIHNp5f-AoIcTdJwKuSCKwFWtO5AsYcpWZzHs4aCJ_SifJe5MzhtSQK_WnkdkHB9GVg2G0AjbbIch09tNV3zKTyiQurDXqt4zm6IVzGD5Pieresvpnyrv-Vqw7ibxoZvnn8F18TZZKqb-LhrLnIodq3BpBon2VlCeal_OxLpdufdvRr6ONG7OPHJ1pFRyZ5NCe4YpjahVzMhGXoYF0NXj4SFFb3P7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Li6dff3BgzddMW9Y86q_LZB82M7fpSA4X5lRxz4k2ODT3M6hpZ7nE0v5Km3aN3GV_4gg7E9V-ch1vhdU90j484IRNcxpL3YTNaExSLpw4hb8-nwWy-dnFV-3LGFWWrpQ4lWObyol4HjL4FdLCRHRuRPIAJlldUKGzRZxPaxh9Siupkb0n1qJ_Ssok1Y-rbW4OcEb8yHEBxAHWS917brnD_I7CeidZNVVbdYHaxsq44-UoyZnmYU7_qSt_KX6GjaJBPGE6wI_aHChNZMGAXSog7diC49VujK8ziee-jY6eX70iDm0RVDL-NwRcQ2EYtZWMh5crHXrsa0ayE2EjhjAHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYXmff0XVQvhuBHGXHPpNjilFfg2qwK2i67dcWOJJFq6T638thOI7xIydlK3zsK7zcsH5BRf1n8rfBdvxCRCqN8S9pSPwvrB09I2bqwZVdV_LITwI_DMoLeUtH0e7BgK1uH35eCbmfsfssA_H2YuW5WYJvXgRGNhkWAjVNSdRRpY1hAuMP2bKFWtzY8vs3PxlhZljxzISbA4-qEvI4weybEdlTFwRHxZZFSLPpVTl02TucAm2VhWYST5HIaRzCd4nkERH8iBwoigdtPZaLgk2wM_iJhvzSjYG52rfa3ZwpbKeH4ZLNC6FsWnnVCvavgckw9qUviTXDFDxRPeHnM39w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22184">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUZWv68miQ1Gha2R7W-LddF2aXPHTzvR4Q9R5N7ZkAJKaBMcsPwTUtJf9pjcd1WXWQgwgFz_0V0qv6I8QhY2fcifX4tO44fBsIpeHhZsg-FIM0_xRDx1UHxpDFOlYkT7_0DVoFMIKQi0x_MzGNtTygRsLkdOSpwc6hSHFfhirUvF0lsSzvmxj_Ibn5czAkvEsgPsB7QxNYhBfWjR4L7LlsF4CUn1PBX-1z-O5rlvnHWHJfceXDSAbUoFEB9PdrjzAef2yQgytDYmX0SKegAP5qEHJhikvpu4tN2l296n_QLuQ00MPmdP5bd_xOc-17tkS3sUwa1NqU12HiWERj5hHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیرعامل‌باشگاه‌پرسپولیس؛ اوسمار ویرا قطعا فصل اینده در این تیم خواهد ماند و لیست نقل و انتقالاتی خود را بزودی تحویل باشگاه خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22184" target="_blank">📅 12:42 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22183">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621338636.mp4?token=b3fZTgBH9EkwD3600otKVUCq2vs2wXXTFYX_UUvpJdMnVBtZ0wxESb0WTLgUeHzWVDoXLwZL9oRuzDiH7yM6bhmC_OaDP-mXH5mZjCBhPk-zePvpOeMQnZle1NILnRFOSVg0HXZ3XX0EPjPF56uhJuuv5h5y721Lvo_hvAFawraF7KI2hgN0loIQOnEbuxTTX_tfPJnOtIwHY9Dc8h5u5iT8qVx_iinLtW8hOYmWfuHQkjAEFw_hXVvY9kCb3AiXs2uOicYjVfuLkB58VEmMMYHhuX3d3bKr3ZHNP2IqI8paDQwoAZ5sFT3T0sQGZyJmPcmf1ZiIrC0D12agw92nzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621338636.mp4?token=b3fZTgBH9EkwD3600otKVUCq2vs2wXXTFYX_UUvpJdMnVBtZ0wxESb0WTLgUeHzWVDoXLwZL9oRuzDiH7yM6bhmC_OaDP-mXH5mZjCBhPk-zePvpOeMQnZle1NILnRFOSVg0HXZ3XX0EPjPF56uhJuuv5h5y721Lvo_hvAFawraF7KI2hgN0loIQOnEbuxTTX_tfPJnOtIwHY9Dc8h5u5iT8qVx_iinLtW8hOYmWfuHQkjAEFw_hXVvY9kCb3AiXs2uOicYjVfuLkB58VEmMMYHhuX3d3bKr3ZHNP2IqI8paDQwoAZ5sFT3T0sQGZyJmPcmf1ZiIrC0D12agw92nzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
کارلتو به وعده‌اش عمل کرد؛ نیمار مسافر جام جهانی2026آمریکاشد؛ لیست‌نهایی بازیکنان دعوت شده به تیم ملی برزیل برای رقابت های خرداد ماه‌  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nm5HcU5G-nw-CNrw0ZXqKcN-ZGkWI4Us3mX4aKAtDxgaVJBC1vVmB0nXSCK4jXEvt4vM8L3cw_03Kfybef13ZqUaokB_zvx9OlYzZcPHG7aSomEu9XcjtL8MLEfKcRg_WR3UNL6p8MTcbl_J18zy8yE_n9v-YncalnVNNC-vTn3SDE0BKFYkZTL2I4GtxNYKOBHvROS9-4Zwnf_QT-_Vlyjiyurn37LVqKE0oJF9-oY3zvqcnbCHIa9vZXICkPmTWLxlAQOXMi7_uAnc9nI1zkj_tFZS-Gpr2oyaa7UCKXB13R_uBydN8KzXbBZJv6MgLLrGi4mOx4t-GaN22_eVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4N8v4XmPL75fU1L5wqOi7Wj3l8XR9Ra_Y_o9h2f7elu2zODtg1MMyFe0397mFZl07e1P01csivxk5UbZJNl4GVRjG8lMo8g1NSELCqnNpA0WQew770pXX1GtKMM2gVAjS9uXTTZDbopdKdWie8UsoyXx_4n0J3tTXZWCHxwbqdfCBpyJDGbA7PCmkt1J1ksQRonbPQYsoTVO9mmtg60kxDeqhS-yBXTLhNByHQ5iOnRbKlv3FR65ZzIUvqu6TKvXEIoR8sZslxk64TLlJp-CKXvhI1Aec17plS4InoVp19gS-qTDHAJxvDcrr5OrghYb0Zn3nvo6uo6pra3sdumaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22180">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYEUrqx1ASCfywUVxnoJPXEjdQVJMLdcVQP8WQzqEZrMWe3m7TnIFcyFiiZTIj1fd84_gPtzJ91ZwvItClnTOqBLPPXiW2Me53yRBAMVmd6AHd3D-CWEQpkXuoZvRv-QvOxFlxcu0B_lJxDYnEdaJUZnPSz0ZQRZJlcXg0bENuHaID-9AV-zkL1CZYs6AY1yoIVMJb6j5Im4DOsEVAcwjxRYYbf2fOxE_AaYOj4zKmxz_GlRwmBAUsG5NosqJvep2lwNW4uchrRPQc2BAP-gZR7Rpguzdr4ODYdT0WoGsE2Wr1CgKC4wyqLwH0qdON7d-u7ejyiSxtEZTJZqvhKw4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رسمی‌سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان اصفهان خواهند بود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22180" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22179">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAp4aO_P1RZwCbEI4kBZls-MeW5lNPKZcuBQXXIoXFjJxzYrimEh7HNv6tulyeAcYDnHZedWVVt5k92eGU82AQPBo6hDQsgYRjL6ozGn_a5UgFY7VofC3Fqk2zWXuFm86i6Rk-ggFPKKBr7wgjTtioMUN_SRjuDP1dcJmmKKpuwH64JjwK2Hk3qtoIoT04w12ypbB9AjGbtLhNf554rfg6YXuAbrZ1Iw53MccGlnosm_Z4lpLknXF1hGlLjXdBzmiLjtFvuEHwk-PCc0EaoDVVF9tYROxSaF27uRZalBNwu3tspZ4BWVjCM0WCZAUVvJEJzO764OYEGRx4lAP9f7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه جذاب افتخارات پپ گواردیولا و ژوزه مورینیو همراه با هزینه های هنگفت این دو سرمربی محبوب در پنجره های نقل و انتقالاتی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22179" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22178">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3lji7RqdNV6moS0AbU900vosuHBxIlF2vcZHnGvh7Rq1trDAValxWViwJ_Z19k1NeY48lpbY-OkqJR4u6kYQhbAwRB84emLx_STdr8F84Dpb6O-NfM1n6sPBijbcMcMsTDQIqsAqVeXmCvASPwUuKDAITNmWtqwlwCJq_YuM9K4Jr49u-U8LrkpsGVDC7RJoCtvu8_wt07eCZpQplweGh1jWDXydfJY0gtO5gJ0osLQOABq1VVDb0Q9tR_xFKzBjuE0iF1-oQmqxAhd7DpSalvc33-RmEa71yPDhBBe2tcO755o5b2QLkkLayoZFRUOzNZJbEz92wOFjwpt1djVew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورودی کانال VIP بتمونو رایگان کردم
؛
خواستم یحالی بهتون بدم هر کی جوین شه تا ابد میمونه
💯
https://t.me/+--L2Hz5HpiY1YWZk
💎
#تبلیغ‌نیست
💎
👀
کانال وی ای پی رایگان برای همه
👀</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22178" target="_blank">📅 00:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22175">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/raBtH6o0QapfLoqUQryV3H6lY4vKz63QaTK10PCB-QfBJ4siE3YgyEoI0VkUZ5o16yR2I_L69hQrUg5lUDF8tIBpacJyKyy04diCr5787J4l5Uk_YU7KYI7OVpXv9Mwrvvj3DJm_aAgOs5TDXWnzQW16rqnFG0CgsphpVT_eTzKpgwEbtK7TK3E27Hr035P8PAkXgomh8Gqpg86AtOehvA-L3Fxt4EpwhrFZ07gRgPPQI9tag1cMJg8shP-vmlmUWnvLBGEaq7aO6C-vmlTkj2v8Q8a54eP5FoRRv-uiwosT-BgflgPCWSgFotnai04ftIaOwFcTVU3eijTy3px2aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wlpd-HFmKb7hNTdqaU1Gel7cx4Ryjy-wgrNQyfSSj3sHt_DlxcQytMUQKOJ1_Zlw1PWA5Rz6Y9dkedRYkFoi2bmGr_7wHKsQaFGZa0zb4l3hUkUJo6Matxv1xipU6rfoCQ3u-vzaHewEsbe9tJ-lrje3mKSW8xMoNlvQVuf-ip2h4048GANHQRFjNnVI8KLAC2R4az9103mIsHOkkyK_X0WinN14703jTCiK_tLI_UjKN3f485SgI3OxfSGJ9EcunmBh_KKVHQoXrYTfBiuFiYr_6-bRhtWDpRv9chuxVCAYu2Fsam7LzRxfkq08-QqM9LJjq4JB-CGb_vrfEbfbLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aee8c0vz2tCkyAHNZbRP_N9JB5F_d86HpuMYTtRjfG6xIVb5aGsZXtP5G9haXW0yPFthBXN0x0_uC9nLg1Yq-zImje1Dha2nHrHVoQBZ8B2swbHN1Vkc6tnZeqwNZP4YapZIhkqezyOT2jWqe_pq8p_cLnqsPVOC149rRGpJd0bRjfOjj5_p4VjeQ_tupIhSMtM7ik-SpisQCsqrwaTAJZZfOaxsmXikjarXMOcqn9r-AawxZvglhCrLJEOHT-k2PUueImEaz0zVj86VFegHe4Ua9DRzHUhO7mlIyUpTngXyfehvjGgpCU6JKuW6djpWekifvCyVlD0kDKlh2wVhwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_NF5JYoZA8BAryovJ4nko8zikiQplcxzgDPZ0N3HmV02ozhkTzhiPDo53aeP2XC-JJzANDKLHT5O65nINBk_z2hYYg7F8bbJ4jGVHNGk3OgErFAqw2oYs_F5_gwVpQ8Tw99oe1SIGAv1Wq5s7eHvzIK7EgoUaotFDG5MPwn9EapZ_E55XPWCSggO8VhAvGUqNsH4wxv2n_qgjH2LthQqiS82Q1zg7e2inJQNu4KyOCR7AdZpCeCvEenmAZ1IZ--htA8mbZUZR5CWH7i9EAqGjW7zep_D1wCY1NAdSZXga9EeXZtVBER-CDDdoGv7WxqtWdr6wSsB2rrdmXDAXfTuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22171">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVu-eW8nopc5OpxE95ug62iNyGvFZM6xek9IhFmIW7iPo8Iq0ewsNSOJXbfg_W43rGvB90srilub2esUDl2kuWJq_pOWUK59G94kPaEqfY80xVKmPrHRCtojoF4NwcQsOOZCwwE_5CZlETtU3Y2iPZ6Yjs5s2884C_8ncluVjSA3095Ulp5IZife7rViP2Oq1VnooNrMIFhn2euom43B2O3yeznEjkAiK_oDKXFgarm9V1XhRz_fZJ1-r14HjGiS5j8FL9KYMQTEIvncQknObGAhNIMUJZouJlFMNsuNDQ1Xc3VL8swrNDkQzXruDBE609uQwiAWzfLmTbxX8TE4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#تکمیلی؛ سردار آزمون به نزدیکان خود اعلام کرده خودش‌هیچ‌علاقه‌ای به حضور در تیم جمهوری اسلامی نداشته و برنامه ریزی شده پست دیدار با حاکم دوبی رو در صفحه اش استوری کرده.
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22171" target="_blank">📅 10:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22170">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=VnmnLszsWi5VK2tY9oxy1QWYfn1c7LUJpFJFVoZ6pc4q4XjWwOkKIlTYiLbWNapbdI2JUqCNB__RpAQtUJC9WDYFsgtcpadZv0kTXVVqGHfqX704YK-SX-rjQABpG0pd7MSWNeiwb-703-0u3Rz4EDMRyG6TOlHe2axfrrlpTOvqRfSxA_C1T6j7l1DjQZnJBioITQpQfCbkPLlV30ZJlKDai-a0WH8tIKsu8Ht4InK5gb0sG3JtqerPErIa74RfT7sPPFy_MWiRY91KsvUIGF8fwztX87BrU63noku5TpbpAzsxTVuTYvbjYdxLNK_DLrU4J9MckjKHtaahAjTCUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=VnmnLszsWi5VK2tY9oxy1QWYfn1c7LUJpFJFVoZ6pc4q4XjWwOkKIlTYiLbWNapbdI2JUqCNB__RpAQtUJC9WDYFsgtcpadZv0kTXVVqGHfqX704YK-SX-rjQABpG0pd7MSWNeiwb-703-0u3Rz4EDMRyG6TOlHe2axfrrlpTOvqRfSxA_C1T6j7l1DjQZnJBioITQpQfCbkPLlV30ZJlKDai-a0WH8tIKsu8Ht4InK5gb0sG3JtqerPErIa74RfT7sPPFy_MWiRY91KsvUIGF8fwztX87BrU63noku5TpbpAzsxTVuTYvbjYdxLNK_DLrU4J9MckjKHtaahAjTCUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#تقویم
؛ 13سال‌قبل‌درچنین‌روزی
؛ دیوید بکام آخرین بازی دوران حرفه‌ای خود را با پیراهن پاری‌سن‌ژرمن انجام داد و از مستطیل سبز خداحافظی کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22170" target="_blank">📅 10:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22169">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=c8oTPGOyujoe96hu6JEVEztQJ_v5WiE__G9GQbJ5VA5uwve9NeO0BqdvOw8WIeYMVOxd5Nv65F5EaWUAzzVY_EARLoJIjEpT9NIHruiwyaosbOPHUaB4e27LO7L-bqcc6penUuSfi0I0GsALFnjqnyyriHaKwywsy1eFYKoHiPRygloNmIV6WPmjGGAHV1fVKasq86t84VDFxyl3kuNgzIjyrD-PN69LD8SGBOAONkqQ0megpJcAcxmSNQU4tfsP9xUm_Iuru8t2wi1e-n8AxnG0IrsUUTLfHdKVDpIs-pfIWNctLcrpSspqXJnw_kGRd1JWMjLvTM77EH54I-KH6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=c8oTPGOyujoe96hu6JEVEztQJ_v5WiE__G9GQbJ5VA5uwve9NeO0BqdvOw8WIeYMVOxd5Nv65F5EaWUAzzVY_EARLoJIjEpT9NIHruiwyaosbOPHUaB4e27LO7L-bqcc6penUuSfi0I0GsALFnjqnyyriHaKwywsy1eFYKoHiPRygloNmIV6WPmjGGAHV1fVKasq86t84VDFxyl3kuNgzIjyrD-PN69LD8SGBOAONkqQ0megpJcAcxmSNQU4tfsP9xUm_Iuru8t2wi1e-n8AxnG0IrsUUTLfHdKVDpIs-pfIWNctLcrpSspqXJnw_kGRd1JWMjLvTM77EH54I-KH6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hji_5TtbTZadEZvJZsST2FxiT4oLNgObwYG1lRswvRSBBfXnOEPdcSgWpLNO9I-7hZKtGHhtmJPn4m8HA5na0Ak-bg1fnUrxlBUdt0df72CEFMi_Vj4DEc1GRXpPnLLbRRbTQmr_RxSZxfZA2XHHhdKqcUwNld4gpHuF_COQqnGxAvaPInF1TJdlAlHmiv5Es5OgKtKeQ-iCRdMKwcv2yv5uTkmX5eKF0AbaPlgPhcZfugjt3UbK8feHE1cgYNy2I3vCtMPSqhOIgPrQ6VIQOwzqj_ze8yeLveTHCcezzrINzUCZktd-qfYPcH2-DNE0SKXVVeQGsMuEEZSDtBZZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oaW5lHQl2G0arKhpTbS76CRh6hyP9iLyT6ba2Y1JIi-5CmxZtmaDveZ7bCBprQT3lQhdbQn-UZID-00jl0Tv7hjhK6YKRn31uVqn-UebsGCHXgjd6UAgrXVpdRUX_DO3BFAuihwStfroQl3V4VSgcKSWrkxA-E5C96PNxNC9pzCLq3d58kh5ujQnSOFVi5RkaXZSg9AH2Rc-IcM-4dmDy4t76prtBZT7BLKWnmcgZyG2ueXv5hViJQ_fzCcc4uSoyA1v2_PSdlhwRzRMysCBKC7SPDXh-fOuMd3AcEy026VZT95EWBwZDdlpHz-TpbnKFjZvW2Ytl2IpcsWZtSU24g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_SmNTST10OZwwE7vw6eFXFCKZVzNEHSe8uMG2jQxy6u9Yl_Bp3Ykt3GdVtSJKG1PUMpMqcVI2rh7mQ69CV6m5vtgPcleuNQLPbam994WFm0u5gITUGYY-vlmyYHOiiNwtGNV7J9yJmJ6qTNFGZCP1r-fCtBYg_vqQ_x5Q1qCj3nZyzbCtnkqkY--t5pwgO6vSYo77Lfw_Gk0g5E_XDq0dPieo1qq6DvpG9NPaDGPXRionHE4kyvhcgIqw_0CziISn3a7FgLb0rSurh43KqTGpVuFwsaEfreFNoJ8XP77nY2U4ZckNOGGCUkGkGiAuI2AK4mO68sQaiJjYyB_-4Krw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در جدول نهایی رنکینگ منطقه غرب، عربستان در رتبه اول ایستاده، امارات‌دوم شد و ایران‌بالاتر ازقطر رتبه سوم غرب‌آسیا راحفظ‌کرد.براساس‌سهمیه‌بندی نهایی فصل ۲۰۲۷–۲۰۲۸، ایران صاحب سه سهمیه مستقیم در لیگ نخبگان آسیا و یک سهمیه مستقیم در سطح دوم لیگ قهرمانان آسیا خواهد شد. این در حالی‌ست که‌ طبق اعلام کنفدراسیون‌آسیا سهمیه‌ایران در فصل آینده ۲ سهمیه مستقیم درلیگ نخبگان و یک سهمیه درلیگ‌قهرمانان ۲ عه. باید دید با این تغییر امتیازی، وضعیت سهمیه‌های ایران به چه شکل خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22165" target="_blank">📅 20:06 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyT3gKDMjCTtwV9sgw6035Qzj1AxOlrgQAmaldooow8LVpEf5AiwbUTYOJLd-WgoV_beKz54XTYgAQmo4W_37KxC1K01Vm9c6NUBMFAdi9_dryZ0zlJQ4vN52MKo0WoX3XKb7xl9VG6O-L0p1V_Z3BrJxXpNovOTy0CV9XxPvTRnTEtnaqKtZoDkyeJyo4cNY7tiv0aj4Spy9bVupCSEMdxSg6ErT3CsLi_UrCc3dMlEfhkYfuK1rhPyO52ujjB0WE8JsiEkL_rNCxuAmbWcSRPgQeIEZCQskcXWJOYjrX2JY183MHFdYFUO6uvimPCuZfAesvrghCHIfbWmd-E4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C11iE7erj1DDnNgbJDjShej_degPfnbWiceBUwu8DfUz0bH8EPrfYm4IEs2cLeAQ46e8AlUwHFEYGod-yZJApD3yoP_GtuFM_Y9Z2z5WZA3B7wI7t7aFnb6Esf2Xc_HbSrFBYnwb2_HKoCPuAvcmkxsXWJG7AubdTJ-9CvI9ti9_9iGbqwMttGC-pyG2mBoKh-hGx1SL1dXE07Y82X06QkSg2-JNfMjGtZDhrMIJYuFEUOMYk_1TwVJ9wy5hkLMWk2poT_l6cmKyHCFAlMPBZGFChs9JUun3iNic-cKzqiuMzBq2Z-3oTiSac35yLnUUgTVPOVw_FWA2eSSVZgVItQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BG0Yog1Mhnq032YgIrArCIG2pE6RPgka94ZShcgI2MnCvXHZpLJ50O5BBDKm9TTCozVd-gEDln3VtL1pfCCSgWcWuda2vr8oRsVm6829byb1kYWevTiDnapGiMU5VoxJ_hzD8nWXfQZcJdhO_zbkjkUJ__5o83Q2kg6At4oD817Wz6KWYORJnFBn-HPwPDAH3nK_lpC1d-hh9_OP6dZcHwA3NQkTfaLQC3dFXCQnXttgZoJTy--5JWejifWR66psLz07iaitv_udXEBxCCTM13qDJpDEo1v8NHmTkiAZGFmPgHosvgXcbldZUeG7nQJvyBYA9nkpYSITGEB1ZWSssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD7qUZl_yby6Blb5y86BsTilbNx-00xYEp0xn1_hGo1kWhuCch2hEoKH7QnuQiZVsUj96LxXKTR_cfIYTFO5TD0acblmubvol-5LURywiW6fASuWSIkV225q1F-QrFo0D3gLFIkdL3jq00fk0_MmhL3skFqyoggUau_7M52pkcPgl99UmfhK5VOS_nHm0uX3xCEEn12Ely3zVfNWbdQwmaaGaEWBEPicmABNb-6rhiucL6jOod27cmEqQYlGaHtj_nbnjCSCWKvi1I8dY3ABbzBdoO7QdhWThVJoTZp6JgntjSLW_bw8VnJ6zSLCHXDZouK-CPWRiXVfS9Aoz78_tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbqZyTYyMTtqKdngIuCvciRuHCnuzJFEoAgPqxhw6rrwsTqnAqU8mJGuen2r9-zH0DN588MT9qYrLyv-vryRiD3b54jmooOmecjXP26amkbFluqmbMbybFITAXUyj2G8aG40mrafmZhPuB6StELL4MqLPZ8hUogWcyteWAw8gXNCEsjRSd_U063DUtD3VT-3N6r79ThoibbcJGiihbsOoV6NwA0qGV8lCn-rHKQXfZ4tMni1h5Tz3HkhXiGn5-QSUxdrATuPE7GHYtD_rt2WqgjwuzYPhfW7lHbmSVUoMX7O7qIyEqxTNnhMsJAMqAsk8GjyF85cCKrH5UWDbbu_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSPV-bNNRmrbGV0FnxHDHpE9GR5p6Hx9bNHbzmkSLeop4En3VnX0svMXwOHBYkR-_jq4WCBVlIVqsaoS9VADxaG8eb9Dx9IZBLUMBG04FbJt5-vTCP6sM6qzzr_KLI0jM0tc0-Uw19Jbp9yIZxBmHZZJneODl-o52iG_ZUdDvU5AD8BfhRI7vliwXnm1QVNoP-E9JPrY29Z2uCoYeaUne2HXkYxtVkdvTgbZM-OYbygMz0efcIitv1C5hIXfxSqg8WhqGhDOUP2Vkmph7KYnwlpU_JsnB9nr2Thlxh5S7MSG5boUWTOf5QtMDI_TOq_4k2zby10CDS2dtANgCv4x_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdU6O3NT33mGYeu5O4aO8wWxnoT8TI9v7uGUW1XXbYLLK1hm6EXkmtjt_U-iyvQ_o8OvtPvt8KHSW8O33F3WCbWccrpBAvRuQ-UcRG0ks-6jDca6Z56OAtctIc621kGwPKLwk44pcRugjpdwzmkDFnQz7zz8RoRa2kZTPsdqcprCmri0GduKk3ia-BNfpooLNh1IrKXEq27ridBo9lD7Ki6vp2Y3W_PFlADWXTK5Ch141cT-SLhjCSPI62ivmBJi2xRrftACGOBAqiAXB71fggod4gex4LVv_Zyc3LSnAjy-dmYFvHUpqaO4JGtlOSEWJ6mqMKiIaGYf3pwPDtFhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvZnQQ38sYOXWzZYxX06PZcEm60cPZYX6zexsc9gUbX_RreLqU1xggKjbM0iX77XKh9Wgz2T9xITJPfnBsOX5pobLG8VUVMUUgPNyFrvy_Qa_cSseM4CGhXMbzMFSPDwwqkVAC0P9rWv7wW8ukssCf6spIYoTN4jmW0FIN4_19DkljJevNMt320QYhJd44chxbm-MwfscucFSo2C3xFgSRi2jvsjjnho-kSznRwq2p_bif7qBXYEp_5kqKZbbW_kXBHK1GBLfDkWphpALD1TBtdbzPkA7t6RlZJtYQtVM2a2Pto4_NXihnqpRZrHbhvt3s3RLoSeHYAscG58Zj-_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNaw0fIdM8AoIHngUSy940smN6z6SsldmETYQLKUaZOhQCWFGUdMGfYMWFM0WFbNCZgmqthzQXfgRSJiahy4KPohBm5m9IFrVfX7OS_6IWYIghdiYAjP49WtTUH2mgIsc73B4ihfDnmCiEF8knCzY8gEVb9nlXibRJ-G68EIN3f4AI-m829iCJMQtnvbghbKn6tncmpO8b_G1M-EjcXJVoyI0TKbwnpS-Iqiu404CxuCcPPB-5c5l4QQijK-2KRsuqBDX2fk5Yl9eH5dXTn6THEMT4a7D7kYJkP6mH72JmjQwEdzyhuVWlSwF4GNjuCIP0V4eODWbulU8e2_-IpKhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c79N60sCyx0ke5hmZ_kdHtuE4IEpFZ82l6fD4rvnYS7D98HTfCG46YdQ24NjeVFIBoLUKJqvt1wHE1hVR9IRgGLUe4HLsjkuAkUaELnPY8WorjLdkbjynfO7MYy9rLf6wE5tD5YoXzdq5UeIIMX-SuetENTU7QqlAKT8f6ZX3vHzg4i-LuMTUt_aiw_QgN1PNwZOkbv_wwabYlxcvphcm-hUD8QLOIOTCOpTO8HcHQZboS90XXvXyX5et2y0PzpVaYiOja056_S59O1Bxdh5qDvgU94oZTThYDlL-fzY3of3TaCj9UgAwzFKmYYiaVLfDkwZX_71UuMHLF1MeA9oLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWRXXtW06e4Id5IGzA70Wadn63AXoBWbyV0U-um6eU9HuRtNUkRncjPl75pBhh2kBIdTEmmJqmpP_QhAQ-FM0UrpXDQBCO131ttr-7Ab9RxdEOGb06OGSiPlMxG1SRjKE_T5x-SNTnP7Ybtdm-gwUNbgT2C7rqx5KzyAKAwDg5lcjEpj4nXxxWE_VaPb02jWFIK9eQT_iZaOjOidxDDnzpqeCB9Ts96oTn07VwL6m99W9pkS3X7nyPztAfgBj4EGgx8K6EZNrHOhSczDxzGUK5hyD_LIiteonzCaDCKFAKRmpzBrQP-dLTSI_7O6w30wgllQLmwzz4e5_njFZsxlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROPGGJO3bMGmz6VfWDZUyB-zQCfMsIYkRV24aYl56VY2ugO7dws-u711PhJz9y38yn6C3ePPKfTHZbvqaQchTENNPDa3zRg7LhtF-DZDesYmqo9AoZ8IMaEp1NV_cyQyiLX5FzJrxJSuf6QxNXqrzTQZ_M2xiylGHTEwosyyAKe5HlXywJQTSmPPTzeWGbBpfLKTsB2NKJ_u2BU2gioILMyUKtBphFsma6ksSYzC7UMDeAHMxwpQcpo2IEDsnY7cfa2JOdGMSH4zaNiknEZ56oB7KVqVJ4ntkhV-jbPLd-9OpziqE2N56roRSp40qnBXVjpiu55Nw4YwcYwG_-hgRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fel9W67eAp-jrmKTvmOAMpkTFifp8vyJ3__GE6hGr3qTT_5vS03bWdpIXo5OaqEhncisMS6spBWKR6__N9Q9MknSRy2EADM8cftgmbAJ69U7FeBUtTHWK1o304zY5s9ZkDCVubD0d0L4ht8yqfYTKMkXyHfpfabk2ZYkh5QAicwJh1MtgB6t_xZ_gdy57oa6eXDagEJQp81p5x2CDJe0NGcgTDq2e80N6sE1GB4bKbQAj1_7dEhgeEvG1PM8StIi12Sv0blym6p6IjfjR_O8m9FPtRvA-9lKKZ-17ptoW6UBxiil9Pzy-HqAUlDPNtC1JccM22YY0Nzc-wIrBDpENA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHL2qxJkh-XqrTNgdUavIt78VSj4TKeu49me-Gsrf-8o60okFW02bPXiv02WUbVwpvrJpvuC9qZ2Meq33KG5dMCnMOyuijWILr_yMI3LhNW9gSUBdREXb1T0YnJL8Jyir8cjAB8lrnndCN4WI_Pe2a-0CDMauGxoVp5o5VRxx3hrLG0kEN8Zq49X9_w_TuHTS2oLY0XVWGqs6UYGLlqVJ_7ndMolTxrCxt-B22Esycadtna_J8GR9LZr-OA96if3E-G4ExSVK6VlxTS0sagVfPIrRiluRgJlhWinlt491A9jhQ194hQGfJpFf_0SmZS6vPhhadW0AGkOu3hY9jtAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLjtDs5Aosv9LGeiwOTy4RhJCCShzH10Q7NEZDqTPlIN9wRDqAplXMgR4b4F32cbwPkD5t7cqprXoEDPzdNXn0dnU9Tidm0xaCna-8_HwwTezDQjBgTd0-uG2zw5IxnWNpFVeJ9zBfWZZQiwOBkQY7TG0fLotoCPRWN2KaCmZdHjqbbSHgmo_vYvRorVw2bE2PWVp_Xj_6GoGR1kqaJnLG741t8ZGe6k7aUpKkUFvRPyX19_BE3irYWEBRqctJp__z-AJkYtsMKW0F2imFXXUvujpJ1OEbna_EEUpreiBXAY5LlT2y3j_BpkKH2Vv-g7oZkqnpZ7tSCtmJSFmWGeoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEHk8i85j3jRIjlkawUNPFy4GGgine27cYb9_3O0OAF-TJTKl8ohyJAr8yw_1yxAwfVivLAzq5nIMiY95_8zfoZ1ZNRFshrjqoC5hCRO_7h2SDFZO5bHHHWx-I4v-kHT1u1v9ZIOErh2bVLPyq5E8PrUMZqTsaVDHgUZrTZsQnuHxFCqUvbefb4C3IChwW_nnu8qTlfeLRO3KvGZPoQVtH798lbNhjZhQLuKspXGip240KlYkgJHgjK7MqQwkmfugVGOy4cCFUUSNKB5biwFVJZrF7ErFum5y-z26r5n7KA-jqiQ75wUJYQlmaLUnXDMzFjfDIUdbD77EidJRWK5cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_ZAQeGk8ztEAS__FZ74z_e2l38inVu-0sPvy-QkuR-lK22NHiQENOZeEMhVx5b8OexlotiJy7Ya7kCOfd-jAWdfEN0Gdotcu2sncdY_3pqetwYO9fYelJB2UJiOUmBthaWL5KoDubB68NVQ9v4wHzxgzYWj0MpBPdW_UFdk0xUNd--s660RAcMYWffz_FdM8-4XU5zWd1spSaiDqeNqSX-fzW3LXr_JX6owQTk3XXiY8lEjShW_yGvVbkcScjpv3P_OWGOwcFWrm5WP7gJ0wgm1wT504yaiqK7e6h29n9cJ7GuTWHi5SEuZxsj7JOOjOQCewFMLDRjjPOBos9T7ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛اوسمار ویرا سرمربی برزیلی باشگاه پرسپولیس بزودی لیست ورودی و خروجی مدنظرش رو به مدیران باشگاه پرسپولیس تهران خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22145" target="_blank">📅 00:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsw2HUU3U6hv2RtosazGrlzP57JZt88hRM0TyFRwL_L1TKaQcyeQsAQuu85BKrkXG3bDnLqRIvRRQxJY8f9aFbhsw9GTWUe5drZGwmJH4hDtekZJ-9rytAws6DuwOxx6plC_i451ovBg-Nub-7-P71K6ZqydHOrouzD4AyMBV2OeKIAoImKt4lGH0NNOQQTZrvqZnn9IiqnS9E8DkdJ2ZSDzJgb872gCQAnPcXJ6nPBHMnsFBp3Tv6lcjaNStLCyM7Aww4ZJvykIDlBjiyTPlP2QYJoaOGEFe3n8eBpbnDKk020wZftn0ecmznACsZuvHW0JQK-wxgnwyur5nVOhLw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDv9qHPGeg6f2Ec1UxDrU1Rss2AP5Jq62F4Ti4OD7RCnfu0isb0X6czzJ901InM7pJLbbyRCjIp0lID9V_BzPb-Sbc1lYEQFz1H2Zf5qF8vByGGJUc9v2kfN94xQCLHsraZhbLcPBlEiYLbTmZbLYEqfLLYZAuX84X6Zzr-ELfgelzLoma9M9HYPxjlESggaj8oOe65eIj4e7t8W2F1fRVEoTs56j7Qmcgc5xhvvTK9nR-qp5s_m2E6I1sQCkGREmJ7SuqY_O_Cf-fRBms4E0-R4zXCPfj5xR0_IKbCuWNUykFJtUggTv0tYg5uxARFZUuz-ndc1a6eDo85jYoz1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNMWgs_ntAugeSVA79yOVKJdJ3WMpTsHiAVO47RoUZ_jOJgGSE6XRvS_xoZqqhQmiO7cHQRIlYJ8_mYf40blhrQMP8yjJzvLKeX35qL0As4N3ffCQ4XDRr9N06lOlLunOWc_4xpdYeYd7ZhIVtJrdELzplfkiFZgEr91WP1FOCiHyJsaMAW_pbiHgH4txGNBrSoI4iOf5Qb7VDJzHKGHwWsV0JpdAmJN_03I8ob0IhFdbWNuC6u-XALm5fXyETJll6FDiSOxJ689_6qK38jqJATw68-0ugE94-aR51tlOQpBVDj1mNvWvIRhSqCsXIOZ8aqagWklsroHvItUd_zvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gNSR_7HnRadyihSw3tDWInEjR95Y2DRXzkoPFxlIfDKzMVWM6TVBuqXvpyGeIWXdcVrWrxO-lMPsThf725dtJZpMPgxq8PmsCSbtXQywMMV85d8vzo61oBSKDX4YgP4cDeF3wIWqyz_-dziZDxfB18Yn14unhItBKeUeyfsc_cGbuf4-6pO2FOSnZuM0HbLK38BjLkVJUENYRSM56x9X-aWCdQlfsxClsHwIJL3yxK1waLjDov5eapcg6_XdSAgIJ8PbvcIXU0bMPpbihX-EQ8WkgWFFYOTpPeDJ_lGBGwwXQEvo5xD2m_99hvYr2HV37a5ZmomJozzQEABr6SfVZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLRdWX35MB8YQ941f3fkKhWCcVYPqkkdkPl4VBL29smJEx8iDTyt5YDBmd5SsWCXd3s7mh1HVZeHeELeuEhjxycGmnttdrTya3-_GgHrA1KHHVf2xq2aP1hzkxz0BHe2au6-IBXtfSIcUDnVHPB-sv3wWFH_MopmfUwTxIb6sjq9Q3eE1Kwl2uB9HGLAG_8czayVIqbmi3Cv_iMRPqK1MEbQssQ-dbUAHKTPA5FwB-TuAguGcz8f141s3nnhJfc4k4kANs9TxQbpD2OedwMQaQ0V5Wr4ap6xRhAeFSzl9L3MRWlmrS9BFG5PyGRiP3_ritEAC0oK-i59T3v-NIBnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSywRPGPHNr3pMfiztAV6NcVr_RphibuXvVWTJ37G0O6uJ4f87MygCnLj6ANdYqq4tW7DiQwUMBDBt4GagSqRVParZnDQUZ5Hv4Ynn5HTlC9-mJAPcwOGR4_BKHNBJR_rw3faG8UHzXGfqKcx9s4o-Z2bVuInaXWEQYmpzF6CfKB3JBULc7MbxVoiKhcwc3fgE_jJG92yga2onsT5s9HbJgmtmbO2ZB_jeFtwUtGCWjWYR0bq0D_1VWU0UQuM9TRANaGb_EBvn7GQeGe8rUo_9KgCbPtwCAr8Kg2MBHM28yLH_wO_APNjh2GqbbT_uDdE3Ux_6RoiWW3kQzgAwQFJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mr1WEvSvxSL4jBs-Zt2RGV4f3pu7LEjUmXRAFRj9aVNSF3zOLFcw1tdhDiruUQKKqeNl7DnnuScFAWWglZEZ7UHItDqJuBRASJ_COLDMAei8_qHGm9KucH3_mtBAoH_HaDPSx0kofnT0yVRBN1vyw6KBblEq_RRUTzlf695PbPV2_auBt4ZpCXVr0dxAvHFgepNZcQUdzcQPsTaZcuTXbMlG1DH6GT4q_bM0-KpBltHBZiMGVKl59e-LAlvQXCX0h8LkPTKSTp78m5N1IKYXR3_norioXotui2YpSgvVVQPEvfhMv3dhJjGzcDsrZHJ3rq7UsJKMEFALLDjS-xTpBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phKNrD9l6p6PZzKNBhWxyCmCp7UHxRUfR7i0Z2isIy4fw8Lh95i1j0jueU46augfXZCmK68TiLnGUUCq4vAlgaUmBdYuJVJBA1vjZMJ4hjHMsgLq1yToYxq05h7anqXa_pyCMe1dbzfmZvHf3BUB4Nhvptdih5pfuiedAcL1lxG5k46LdTlUstNLNkdansSOPdQwbuMuYydxuQWWQWg61dwjcqOUHfFUonUnonK8DGTgJEKYdWAi2hJLFxhs8hNtllEcJLEfx9EX5U5um9Eo4m2L28qPh8IScfUOGEhuX4Cj8xWJPZhwsCbTT_Z7x0-VgVzu5UyIn0V9RgyitXwUMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=DTB_c0b9bmB9txICXt0p7thK2F6eJo_2t69g0GEuMxhTewdYDMi1Tg9aLQmy6CfbSo0aqWeH-q_Ux8rYas07Cnbc7mmotu7kJ-YtdzVvHtYyeJ9MDICLJ_aQjQ5Gxmz7mQBOw40M6jmMJ58le4N2GDcKIxInp0LIt2HvkFtctZZmCEgLgDE1-YIswxBkvMNKxq8GBvH2dUkjR4qhbWQCHCAffnWYdeoR3efnjzKOVRNGJipZOhZAlK1Ugi0OszAMG3-WQteBDDpfwrsqfHVqZZ9r-8vE76AxSlrYVkAMlxC3p4yImmkfz8B98e_mJxUH8IY24sfb5LYkKof4UWuKRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=DTB_c0b9bmB9txICXt0p7thK2F6eJo_2t69g0GEuMxhTewdYDMi1Tg9aLQmy6CfbSo0aqWeH-q_Ux8rYas07Cnbc7mmotu7kJ-YtdzVvHtYyeJ9MDICLJ_aQjQ5Gxmz7mQBOw40M6jmMJ58le4N2GDcKIxInp0LIt2HvkFtctZZmCEgLgDE1-YIswxBkvMNKxq8GBvH2dUkjR4qhbWQCHCAffnWYdeoR3efnjzKOVRNGJipZOhZAlK1Ugi0OszAMG3-WQteBDDpfwrsqfHVqZZ9r-8vE76AxSlrYVkAMlxC3p4yImmkfz8B98e_mJxUH8IY24sfb5LYkKof4UWuKRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0pPcwrc4Hwf29LvY0lCMy-z-3hIjvEl9aARLJbNZrk9ZrZDNZvvJiGvV-g2v8Jw7vbCgH8ZV4nxVsnwqXWByWDcr7EDYI0sJ0B2Tu0P5TjPn9W3_cqTxDew6VfZsBxiKAkuGfExDJF2zko_DmRlwSZUuesCHv-kkdOEO76IqSVQcaJwPMjZHofXNTzhye3wFYn70cBsFuA2jkQhNvIxv8A_XPF6fJQF8qc9aa-GadlzkHtiLaRbNy-Mxw0mJ23YI3sYwRGk2bb1LckFEpFvXoEO8emh83bL_KXY04k4GySaWIw6hJ-zaN5Z3M8ulK5wfNelnnBC6-TXxzPlqvb-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcXMiw1ruRv-0zpQvf-xnrArYDzYvbrz2BPULa648DZLhwrfmR0UlWwb4lC54cZqSM3cVket2UDF_RNXfNgr_X3MUWE2To4HcTjjms37lXsPaa-C1qg6zBrPT4OqDbtWCwPtU6_WB8qYHVOZlxmJhHUYgimoV9GItLgc-JBT7W7rJc5L5RVkdGFRjXYkVnEXSlRBkTPLuuhoM5v_RiFIkklzdLxu3t8yoNCxSeoyk3nU2zXzDVUJaU-MrqHZnlnRu1mOGfacEg4rz_-qAzzTb-o8eV58X4UHgSrSE4cap6BNbZ692gNZy3D1dahY4IX-jCUChB-SfDfgJ9lakIcpUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1x6qxnwDgQNvHhTv05jVK8FpNmEpsx7zbkNse_SjqN8kinVBf6GuvUlfS0_XaitcdpfQyzLy8GomY51wM7pfy2K4_Wk7s_nUQYfpvkAtgYWoiinzKdv9TaZUAPYJYHxZcZdsA17HJ8NwOGwxWVmuReebZBt1vDKE4CC9V3ZKamleAZht3jcmmfSZRTmd8plPiD1seQ7zskJVJ5HTeoWb2-Ic0hhLAuWUaTcfvM_pipNbHEolHRKUmulffOKcaL__CfXVVjQsj4dMTrIy269854xQ--buyT8nm_ZsjPPx1-mturVd2z0nFrA8ItNe3FFWh2shOr2kKrvqZYG7CiheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHeBml289VES4nvXvvgzY-pGy7MnHwWSJa48xfLLEVvUCbt8YIBOLhe2Q6SjmmmXfSzgnHcfDhxjyry3Q2KKAPhiTxfsful4Ve8H-VyJExjpocxWIgFqtOclM0t_167S20U_y1jr5URQzTckovOd9JXuwe4tAuSNPK4r7-WAvUWKBdXpv-XEosFwsRsbnKD_conFyAaWbqXkMeTRZbNKrFJByJzTm0L0HFkuQa6iAnfEmvqtP8okeLjewx6_rvbVkhCd3tkzSbHbk9-HYaZwon__T38voTC4KUtnGqgVhp7YNijNtQrx7x8xpdyTvk5F_WszYs10DhNTA3NosJjh3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmBSJwnFkysgt55j0Dc0FCyjckKaQ6doWTQ8OazFdNlVu0fUaSzB8Ntk5J41xFMCdvy5rxkb0iz3fEFQy0ruDeNZueV_8x1Njy6TVM3LPK7nqOM7JFW7raovbTa7G6s4VUSVsQ1FlEmC3r55YyrrL-IgN0gnAJFFfokNBPvLMFysxZ0XYH-exzrataywIy1ht06AO_mNyNOZzPlV7Qu_GeZTuyDExKUqxPjt14aC89XhJf9DhYCcrvO98_-apNU-TEkPKqcURhzPco6Lw6aaNtQvnqcE9REr610TogHGfcaTRJTCZug-XRt4DblS5FbuS0zwV9_NFRf_RxUJfC3JDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEyHEIH319z8_2b_HyRq64mQ39LNtDGhUkg5eaD3E9tek6li9mdEg42HmvmtdmzUdXpBWzAodW9tqf46uOZqq60AzbPIZr5sgX_EylzXhMdDEfzRwt0KHNP7hR37-koBK-U3Kf9iABQ4yphfrXQ0Isi6IjCzQRdL-J0XM86FsC2nuLOuIm43ZmFKVzWS4-heYrXuIs3X4kTJR_omXzk_ZmRBh5DKFy3PSrdx-jHWCaxBtvkdydWeYtNqjV9L1AcEXqyj6mMhHj1jiBDQKJm-T94S-gBUYAhdcOv2v24X5baoz1bVK2lu6LAkPGiQUD4gaT0I7cPt11ZQAih11TRc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1Iwc6K3QrxQ3chxWF5PmGzdznWQqIGoZsYirRo4C-TV_AAA1rNaamolDDdS4bnsHJQGkAzzOZebno2zjfek9Ek9_xWYqoAwg0HkVFt8_rkpbAK-IWe4AVuSWEsIW-968H-Rdpo4Xd-2Lv0y3QzTgqHPztoLy9xeokXzIanN6r2bxvOdvyJjryYp0yuUGNyNdSkPgzdKF4hB4uztFv9A__KJE4zBbD2BJu3RFTrk45HsSKsBpKXKCnCw7tKMZsUSR2IH3vw_p2Nn6lzcYHzWXy7vLjr2yTfRFECox9vQberGFOhJqlVHQgzNJTN65JIcXrW7BOVGBG5N8wezOJfvlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmKWV5NvWfP1gjHHH2A321DLPC8tCvox1L718WR3bNlyOycste_4Zb-fOPJErUQO6xXWJRIbDGHF8wQTxTm2Cqs8bkKMTl60kyCSBfMaiiBom8o5flnTqJxxVPtlAeYLJa1d5NfGLbXDBLcWbke8d7mbXgZm3vLq5etQrGI1v_8a5QLZo2laROl30ZUwOOifwFq7tSEXqNMrwTxvycqUVes0jH5NvlKjbikKa1Du5ofutK_bhmWFMCZJ3M9naJmPTTww-bfqz_hTzCnjhrALc-ZDaBIjElf7xlZlWylgkqrabW02UtTXtxExKYHRjFhudtq_8VFPeNTMCGZSe8NZww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=Ym6hj5oLL0PVcZzr68Q31yXHn0YrYwNymVxBKZCpHlbvxAUz8ZkfkW1m8MJuG_xCL6L6KO4pij7SpKBxk96ifaNm4JePKzWgYx8nvefC-XTHwcVCBpKk-_eWWX_L7A4voSJXuPoiwScgdpuFXaU_0cpbgyvtXQeN-eYXHW6xdS-sw11kcOyqFZYpRY6HCj12s5vZixyw__H4h5ktpsYYAaWbYzrHaX29ZO2jzNUo-kOV8b0ByqUXC75g-v3Kw2mR4ykVa8N5iPF6iciYnnBzbbJQ8Q7rAK2hG2KqDXs-7PP1YpNn7H57ZE6BO3bL43AXbI_80Og-LYqpYokzWTaHgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=Ym6hj5oLL0PVcZzr68Q31yXHn0YrYwNymVxBKZCpHlbvxAUz8ZkfkW1m8MJuG_xCL6L6KO4pij7SpKBxk96ifaNm4JePKzWgYx8nvefC-XTHwcVCBpKk-_eWWX_L7A4voSJXuPoiwScgdpuFXaU_0cpbgyvtXQeN-eYXHW6xdS-sw11kcOyqFZYpRY6HCj12s5vZixyw__H4h5ktpsYYAaWbYzrHaX29ZO2jzNUo-kOV8b0ByqUXC75g-v3Kw2mR4ykVa8N5iPF6iciYnnBzbbJQ8Q7rAK2hG2KqDXs-7PP1YpNn7H57ZE6BO3bL43AXbI_80Og-LYqpYokzWTaHgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuQFx3UhjED7rPeFmmX2Rih94ilKi2V8cD5lc55F-F93hIqOpLsmpN0nNVs-pdCviJtnfliI-kXQkGm_--DlVq2RzLOVsq1GyoZl2DCVxWrZSTju34v2M8jliYJvoSP7Y-KM5AZYyyQn2YQPM8H1WudD4n5f05cr4v5-ogZIJ0RugTDBGG2daOb6uIdTdSyFOb9b2D2yFS99uTbHZMKn4nT5WBsfQSIZ3lFn62Zq3rVBNFAPgjEhDC9aObDMZhgXBRuJEiGPTbg_6LMrgzIQl1dqa7qjOmt7r3Bqpc7wP9aJwoapUTWOyqjLcUb4CM7z2T3Lp5ralu3RaSW-hYn_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJavGhuZbJVqRx6kwmZ7eQqwH_RMTuU7U6lYnVvt_4I-p0z_C_Yb1fUR9oEP8lIN5exkhuFqFepndGgFSEAX7iVlJIiZ2AGgZpnEK9-NDZyxFrF0lc3WH0_goOznOUUAuwp7wy24TzKAr2UhHdlZNVRzGFSl573-_jXr7LE9AqHyCBj-_DdkQT31D3kI9wrUKuQ-AFUzUPiFARQsxErPDhrcWog-FDf1J2lWG6Wf8yv50KmocbBFwKgpGFatxG537W5J8I6hgpkKAvv2G5EhbCV67_0U9Td9B-3zlruG7kHuCGzcML08zmErrv7HEkl91AM7xYym--Yvr6s-gCbA7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=YT8V0ShNerF4C55J_wSSmsOW5q7tiYlNm-kYDSWlOJIw2TgmSPzgiv2IMTVwikXZCJqsh90WAslV7CyAhiVKcKyAL-tFB8m4WJxdEcva-02zdZXMupHR-6D45vC9Je8vN2O_nm6JT4UEVMy1OgJ-M9IJvHPBXM1Hd9-_nPcNaEYhNQNiq5ToUxmsNFKUP94mQx2sp9mXP5GuBQVGDnME1qKUvFZ2D-Wxy_EYN17sdR5i2ryyIeLKPCD1Z_9sbziTxwMt6sQA_45pfUQTYg7Bpql4Ug5DWDaMk22QqSR_myoMIqGz61LvQtxrhdis__yJjuCSbeyAlZYmPkFiqRsTCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=YT8V0ShNerF4C55J_wSSmsOW5q7tiYlNm-kYDSWlOJIw2TgmSPzgiv2IMTVwikXZCJqsh90WAslV7CyAhiVKcKyAL-tFB8m4WJxdEcva-02zdZXMupHR-6D45vC9Je8vN2O_nm6JT4UEVMy1OgJ-M9IJvHPBXM1Hd9-_nPcNaEYhNQNiq5ToUxmsNFKUP94mQx2sp9mXP5GuBQVGDnME1qKUvFZ2D-Wxy_EYN17sdR5i2ryyIeLKPCD1Z_9sbziTxwMt6sQA_45pfUQTYg7Bpql4Ug5DWDaMk22QqSR_myoMIqGz61LvQtxrhdis__yJjuCSbeyAlZYmPkFiqRsTCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gdaajn0TafZyB0ONW9SzztKOtRQs75Xc35I8dN691srOeduJclLdNI6XgWFSz-BQIQfqrIQRo3X9h03_9bqGCXW9E7sdnlXE3MUT9gzrjr2-LeRf-5AQ5BQqKuej2-lYwfMcixGCvs69wqbwK_CG20yWHSWRJVat4KWtVUJIVL8lclqcblRZHSgzBsC77Qsu4rKWpEckdP8erSOMdzcgHSn72QugQy8mA-KjJSK4fmBl-Ii-BJXaeXPFa_Z777qNURzkTpJ62jI3Yz26AgwqQqpLZJ_aYq52VhPZQ3dXHrc5sxQXqfCcd0NiN4hjJzIZj_2BpkJ9RJiTo0kOP80yww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/RaYwT8I4JBCvYK6bIIZARajPDu_UV_07cM_rJ_iSju_f2jwPnfVAPWYgme7V6TV0AuDoxXP5PNGRwwNPE3PO9FoMonc263PL3wp1NVMcn4SRqJfzKoTEtRJVehrZEkRo_MjQjlV6JffoPSx1WgydarVFZu5fwPlTXm2NaB6_ssLnTTl785ZAvIol1ypxirdVEa-r05GASLosJJUCcXQkvhVCGcznC9ChqfRGQdtik1utFEZziz-BMRvgvUglu_FSSZltzbbKXGPSH2m0JM54WsBdB03xIUV1kcZn9SiYmyD-G0RsbuLf6BpaRZHAqpwTh7QfVhYvm0tvBVnnoAbOgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
