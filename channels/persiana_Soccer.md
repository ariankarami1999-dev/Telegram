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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-01 10:11:43</div>
<hr>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA6KKRUXJsVzi1aexljtT9b1dyuuES9fI31Wo_RewXu-HJ-5MQpLOupKZZRaaw_8ZEvcfRzpgkPNIGrbw5yMKg98mndSLP2WTcKBwYgXbfUoL7qeaG2_eXf5VaMQ4_d-Z8fo9HH7iU6PyzZNF1u9M-qtlYjkwzriLKCVhb3I4RNTGreMOeRixL8_SsQUyxqr6GkjEKaGCfaOnsfukpAirF6JrjlKIo7-HZ4Z8P7bRaMQCs4V4qJeoRhj2xKlk6uf6GA_qSDnVW7Ufn5FttpvAxfqM6OitjF_msmU8BNp-fMHrS0yEOyhnmiXV9m5Gt9ZVsN5KIX844hHB0pepobqtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqicYASW9B9T3Ua0z-s9Q3VVLnasml1uorRuw7W5nJ0QuiCLQTQC8K8aRF12PYIr-cXIM_l8kq1TIcGrQ53b-QJK5NnVPBrBW1QWF6z511HEqnOpVm_SJ8eABnameckWqNk88Z96LAnHKFXWoRLhVO4JUNDiR2rURqGCVbbNRJAOe2mznxJp1vaz93x_NrLNUqj3LEBKrn2m4Q3M_J5zZ8HyHaSOZPfrL5Iu_L7EUNXa2TlNIM7FSq_CiSWnBkPV3IJJ8rmnZ-gxNlg6o6LLwKzEgKnmhWFLuJeYiQFJ1JuNPYs1ppYLRdLJUN87dF9AklKbDhgv_Wkh5K0JD4YhXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg4IOQy0Kd1_9mlj_lfwQpqnrprn0od0z3bqfhZZWs4kB--kCw-bUZSPI0YILtLI01Rz4_Io5d_wqSPBvYay6BBvCRA1QuLBNuGmzE8VMBsBQaajK9DiVxIq7xUCZGM10LIP7FFAi-dry2U8i3oro-MFSmR76tU95tzdrMb3IBgMsxipgcBaHvG8yrEfeVdM6tY4p0PFEO1amSmRe3frBU9WXvC1AeCo_AgqgqbYI4eYcbOgUMmtcmmPerzEP9Hvsg6uFkOxwtxhvQv99wGX7t0l1ihrQjSJ8LLMqagaEg3KgX4Fbj_DAPtX1C4P_7ISAl7n-_zB38zrEdZxGY6zKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlnjSF0k2tsgKbT2I5qzdoW64vdbAmAIH9yCV_xV9iy-WPTtXEzCiuw179FBsRladpF2dYF5r2BPxW_pJ-iEWYJiq__Mre-YWmst-HXqsL0HXpfaXr8g4nGgpVjO8ETwhAu1s5kRpNJmdBk9DTck876_8dzM8iN7OoR6BaQ8VvdyvhMu_BDHFtQ1pZXsSm_yi6M0OPfmfPE-b8gQ3CQ-Df932tDHzCc00DqTPfygLkp28e9HNsalU6BYYHkTRprXou37c4M19iJn6edZ4lUouHZRzgaMF9gSnWLGocjGBfT8IVa8ocdDGONaTOT6PINT6x7cpNIuww0glrfpBTWrvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
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
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/persiana_Soccer/22227" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYXb2qaeHjZCkfZCX6ux_uYGsr5IAM_GzoR4Ydxoncwy7zBGg_qaPKkaU1qKWUBw8qWh9uXBdmeTQyxWb1g64g6zYzzxHKlZbg6jNTfMGTriGyuNuRX8poscqIFISc8UjJXfiH7Yn-D_5mNgXMm5TywAF8X_MeIuEUqzVulGqYwWfNHfYmHziQL6hKlds7HwYa-2My0NBHgxTOoeir3woaUbN7mDFx7WHNltQ8vlEAXSRVcoA_DpZoUhq5Sed5yjWWKd95TC5Mf7p2k14SHH6aRR8sKl1-tjuws0X_3w_0MVH8qjFDALntB4OrRChl_Lv0MVt7sN9Tvdtybzg6cfwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfQ3fHrwdAwA7ID9ojM92JvHzuhT4bAVFOXpkKmJls4NombMD2vXcKEQ-GxKiSMdBovAj3HzertCMsWSpzrdt4v27_QIlLIPrfKXXE67ej8ZnBcreENOGDaebEYlbFfJbcikIIo8Xr3VNUSQQGryv4dNu3nxtcYXHpktT6DkWKjbWuZWSxAb8KHu1WXJJJO-KgMUbiW_FVXP9FSjGaFYrCVh2boSdjpLgdiqxY4wczNAfxlOtgf2nbfdNidgRDW9HIk8lp0TwNU7uR0H_2eqRlzCUhrgYaK-doOdezuQzAjh5vEvddqEJJoqa5BV3EGMCGG_VDsRG9Aonoc_uete9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK4yGsyvptFLNMWGOl4v9acUO6qHC-hpSPttlwkQV2kTNVejJ-RveOkEWWjxp0PPnIupEnyRoZEkWDU7qZvPUnCNVee0BD8CzjKeVbybwF4GahjqyxesuitIzJ1tuZqgcjtYB2EJVk6jxjxD9h_aeAtGouJ8JKtQ6UvPS6fD1SLbRrhnVsW8xxGRypKtvWq3TF_N_Wq0bIekeE8yEzCSsjx4zrDs_asB4CIkZpsCveBPuW3l8zOXpq-WjtMi3dzlbuzs_3Lqi-wpD-elMWGkE5cmSxErD22IzMX_jyszM7epnppfcMtrdotxl3zxqw0vRGcFux9GllPKNeVvgYNBWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/persiana_Soccer/22221" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FtlVm1QYfhNa3KWryIxcrc9NmTACIHB4-IO1Se7TnR3CuJQZRyvim9uHtWmEwlTOBYWdhkukBAkQCTr2vdJbDaiTS9Vzrlqww551k2zhXlbeqlJoswjkOdxDSUUV5ZAQMJ5NNsSDVIjXIl4JgjjVI5h0wVr86nVK6HBjbWdF2aXapGvyXjWUO-FA2MvL3Qm7Luj6qAYKmTWh-Tj1O8awszQYMciPJVn74szDD3f3keT_Ar7TS4IcqenGJpN93U1DoNPaytpFNBSULh_qK4SLC8fD53sMdqPjbCfBJT3vgryngv7IFu7Wt54xcxkc2Bpr21LHuBRhGq45sWfICjY4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAFXt7iXfpxDy8d6CJ2EWwkApA4AwmAbyQGRlK1t7FQD5kghlvyDYUJME1ll7L_FG-pG-XgH01yot29yQzRp1tKLdpJxtY3ayfVSkjKoGP0dp0U8T3Jr0E20jC470d7Pq3QqbDrQzODr_xLaZ1UJTNtcYE3TUvpRYE783G6i86sQn0lHZAqwHy1tO9rnCayRJKd3Ng9KsADIbBX0c31yGlKAHe2nXe_eQhnaVzpIdUVHvBio5Xd-1SUcdGjpMjv6UzDVj7SHi6EbO9tCWEVADy23Vy8o0eymxu5xTmIvbfRaUdUwWrf9gtc8NLSOd0vavEhxROJjiUevbxN0oLR-7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCju_4Z-xMDrb6p7rlB4pTsN2mnw03A7r99xYGWbtBC-Q5LBK2H2YjR_ieooKqbd4w2BM4dj8sSu-Y_Urhr4ErBX_9cGc4GsQ0NgxNajvSr6gSlgouGpcfjxX6Qtt9YarD_PGtQCwuSGZhUxiGOvjejmM4ZZ_gfJkZz0_toEDl7OpSoZNKDzz9id9ldjhIEGPoa0ZwSYEo71g6OprphoVUPaSw0p7X_SBUOQ9JmhXvmBu4LRjpHCNJh2kQJ3xwsuQvct47HrRhTzRyj8OgY_CeqYwwZnqxDVuI4T9c5R66RKYr-0N7D02nKre-I1toYn8RFnFZT4xnCZIX9vJkB-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER9Bjgd1jzDYxTgXpIihhIE4C9yXPruvLVTdz8KtKL7QT4cVyiTTdIP1rtdGDNrFvBUabB3VC_o7njE1h0KnizWxG0L5yg_dcYC3L03PCVjVVUHV4p2qhG9lvrgJMWik8VzfEplnHXZsGUJDk3GT9IvaT02rTp2_SkXrN44rB-332oCRHCDJRPO75zITxoBY7fe0rNSOxAp1XPO9WohMFSp33_i2_-96hzkp7ypFCgXDblroZiMwzIeJpfjDntNiv6M86Z1sP7gL-zQlqJDbp7HYXgVyJwA8gVokyxYhubEFE-ouqZnZrrNrv1dG9fdg6iRPnlEITFFSp-vb0viRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozTikkFV7fX1PtQFMlrHHloUhsxki46kQfvBu8-B7rT7B0W_IC5gQlxAWPwwQ8TY5tFZmYEY8cmZq5JDXoj4nZrvOdFlyAEdjVT0gc2Z6v4z-YW91pfGhELvcOtZeNFh3IqMmQg4z7bRGARagU4-IHxRrY784rnda5o5nPJvhwyuLtl3olPL7TiGy4xLuPvUciPnUVDcbcULlDo5i4TNSDStjy6a0gvgWcaNEH_YP_1iJQBitRCywXAEPwEb2GyNkuc5asx9ji4-LVzI34BTkZjPBnw_sPZWSSe6fvVis3rLznw3qgjaX5FyHXwfTsr8vRTeiOD6qGYdnHBxWEYDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCqDZM4DEwTYx8a0-cWs7sjAK4sS5VlkH5iKf2yi2SlNs6jPL8Yqv2RdkIDRK0oDuK2KB5ly1MSmxgTzBqW27_uczXdNk8YshbigiCK1Zp8iH1NXQLQUdzpU6hxztxFGukhjLyYNoh6778O-hfZYEaa8bnVYTudeuUdZvC_cgZNyMdHjuebPa8-P14PNINTKpvm475jycq-9txSlh1kNDsJLDS_ayD9pHP2OQZZDUkA8kHI0ABFcMxV-Uq-M1h6WwTbnPLK7seZ2zBrKunaomlxVFQFZxRNjbvX9W40jsU_zCxOE2hsj4XlwOpeabBBmNywrhqzI12nnJ74Dl2oe7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI2z0mPME2ZbfVurKhKRnHgHUooRG7WMb2ns58h1K1Emz-rXh4xMFhA-BigB2M8MV-gQzpW8cB6vnxYod_3WwpS15yQPx-a1UX0_SCC-81yZLWqJXjCTl9O9Hj8EEKooy7yyGZGNhxkGmtUiKEwwkqXQFg-K5nmwq8ugNKFVi1m7RK8_xsTCVuxy7GnFlM8crDhmNosGsYPDGKk12RUVYLgJn_Q-rvC0IvcDdC0Ue2ZRugsRSXGxzi7Q7uZqRHTYG2qDinqCmF2KHeI3pBVeS9qnChWUZYjRU4aIdER3rJRmWoASQQhmEvKSqGeg0E6ER700Pt4Prb9tlbBGj6ouCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV3eH9UUzVXV-HUdcTjS5sXIeL_YUYVEQoX-X2L3ThiE5boJMjrRXawI9gfQXN6aLUbFEPJnUl_kN3SE05nbuKyyytjobN_PPwElLKL6fuC08NnLIVjHqd3UV9c9r0nG22Q-ri_QJYCkvCNFmko3xxBjjMlOuzZwzPU-AOgGJ-xYvlKxat4Qq5tN6M8s34zRetFobo7xeLI7fewwwiE0BwaTt6lo6fUvZ9m1PKNiHzvsiyXALLFTNHO_UMnwmcH08qyjBDhdh53aPgI1CqwaYt4f5vxjRLBA8DzwWKkM1bM-kc4dru_8GmCo4dgXFwoPKlob6xqpdfOX5X-mpR5d1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npoG7uOZG7v58IlszpjLNRkLURrtp-LZnG1s6AspE2Qtg3ho3jFBGlMjLKtploeJeroBAKKezRx5JuNRxt9mmrewF8FaEp7klwXFrz4jrdGfD3rESliOvnKYJ1aQ28Gq3_qwGTxnABSEfEdqvJ9mnAbr_e81RAomsK3kjubhXFBh8wl0NOYbq966VB96VV32R9jGkgDvYnCyHxUbcrd68uI-lBjwEQpekRgTSDsY6_bAnqGwJSi8WXzQerJFv6yaeKgS5V03FoZbecKPGzits_3HPyb3HskKK6chNtt7GihAzj1DxPJWf4Yesj67G0xO1jnBfNUjglP4znxE78lJoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGKmx7HPVr7p5QEaN7kQFylGGgiMIeN9ZoHVXAdb09ch029sDwqRlhnmkTlJ3Xkzg_5tREKOGJVujWBp-aa126NMghnwfhqZX32xqavMHm1bJ-5y30iQOVVSTZrvUGYldzAR7npGL0dMfgr4DhUgKqnSEPP-2IUASc6Zit817DReSInZ-BJO_lbTCCZB-nwXZgBbY6g8C1SuoQp9seNIxixERrzONKA4lL0ZXC2j1xYixbmZWB5U5Y4XCyW01mzl1RxXwHzojADsqu96WTos8hwfZFimHF1bOiVOuaVixeHhc1wX-Y4kEEDF_RZswyDh4eCVSoQZY7y9vlrH2_zHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22207">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-JauixGHvpFMKFXECPThDbat3wj1w1UtUbU1CyS6GbaiCrLgcVXxww1QGjDCDoR9pyEFDVjdz6dlgFobxuFmrCSg8-qR4WEZl-PYRrfEMH8y6heKoAVl9H6RySmrD7uJJ-MSz_eXG-Csu0UKDwGrhNojOv6STvgHVl3bgTicvzKqkBC3sXQCO17JNCR8uLE7rVCLYro7KRmE4kKI2SO_S2n9y_1IVdu9j5jZ0YDd7E8kXYAheDLviKIG3tg0mprcFCiiG4dxWpylF8oYm4jduKGdm3cVjOhtS7LB4qRlQsw_SBoC6o5B1f5aXsKBdZGyQ9I-KdKsiFFY9_uMicMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22207" target="_blank">📅 00:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDlUk6rvoW0CXQkGz8tiNI3_P0m_gJCLTtiB60EL7m1D8T_dx5l37CBNkkp7gHYkutgsWzu9F5jt-AvVKKegMjsbuIlQ0Z3NerXpAkZ024qki78TePMlrKkVKcjmk2XH69qQHDdxlDFDQnNQAPfi0aLGaQ6VYsBshq7TCEG4xaQ1rdBkjy31QAgX6fWsGGAeltUa7hVzRrVb8U7xiRemBd-ZeBu4xkiFC0MnMFevkme5BSLt_MiJbXtS1wJ3bJSjSKNcbSQ889sJ8J8Zk64UklumFFlClE6qwDE-QEvy8jbuNUQjHNVvGY5Tuw9UD7YBZlVFc5IHKC_AdGZLMlbyfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22206" target="_blank">📅 23:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z63AfyWH5le5oOFLmr-lLdSr1D0rW1DN2ZI-g3RVephJsXeG4HWhdTpxOKPjft2XvQYa80KEHh5vdlHWkCElItiDCZH4wTxo2preHsbT6mYOPEN-6GlDPMwGgJm9J0xkBCoIIxfe7oHNl_yhQ4azkSdTvRnGdHBmwk6PHow-F0e-7HqGo8WxGr0ssg7huuLeewDeON5Itw9zZXpu5EfeqhNOjJUf66yDkHsjD8-wFNc3tNMixLv6qQLZtnSnSCptdwo-Uga5Y6EqLtBkmOAU9DItFWjpvlxbYTG82B8Q_aqbJXEtoh99Co7d7669j6K0i6IM5BOenBcO_wOlUvYLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخبار دریافتی‌رسانه پرشیانا؛
دوباشگاه سپاهان و تراکتور بشدت‌دنبال عقدقراردادی دو ساله با سردار دورسون مهاجم‌سابق‌پرسپولیس هستند و صحبتهای اولیه با ایجنت او نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22205" target="_blank">📅 23:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFF5hkH7lruPcje2_QC-3YMNQUJsiLirri3bIGTJrL_tFbxMTxFwrUB9edSdmAy-_Gf39WtwFlBt4S9ae9ceG7FJhuH02bgsGboz0ECElIme2iYE-JD5OPC6mxxFB1qXxms2JOfzTvPvaa-wmRtY1Gj7V3g__KmtdXaeeR9Lx66KGsIRhX2--5niYba_5ig2-g7qBNvzSgOcCy1ieBBAERr67Bble2d0J7cFJI4JvAiNSLG7H2V-DP2mr7MWtJJcFgzgbE8UM2DWAEQ8dzuLbsmEpg0fvVavzrVJJkHXGDwijQQYcmepwtneQRA813YN_UKQafymOXftdE9HLp0Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22204" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22203" target="_blank">📅 23:05 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22198" target="_blank">📅 15:53 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22197">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">▶️
واکنش‌جالب‌نیمارجونیور و همسرش بعداز اعلام رسمی دعوت‌ او به تیم ملی برزیل توسط کارلتو
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22197" target="_blank">📅 15:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22196">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">▶️
مهار پنالتی سیدمهدی‌رحمتی گلر سابق استقلال توسط پسرش در تمرینات تیم اماراتی در دوبی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22196" target="_blank">📅 15:43 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22194" target="_blank">📅 11:10 · 30 Ordibehesht 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTsewhTkIuJyxWA0DkPYG6Ya-0KYs901sFPayx0DgPpHG154oXRSr5pLssipo-oxybyrd8USDYIyK20SBD3u3sz7p2o6OMuO0kJEP88J6ntCZ8PYYplxj5bOjCq8XJmEX2ODTsK-CHeCW9uoYp_7w-DQ9o2QbEPZ6XJf9o2Ch2SP-s8nA89bGKYkq9ojYLmZHUdgKaWGYCerMglvEv3Z7y3LzSRGBRedpWosrqGXeQoWfp9S0aCaI4NO0fRNTlOUBh6HZ_4f9zwH4s-pRO1zboKtuEcRqwT3QSoarFVh4Oq2w-VvM69k9o7jtm-wu4B3kEC8UgitnOCqz-F1h7ZYpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zo2U381k8RacnMdCf7Snq67dDgliSeoIVooMQlXHH9mwXRRvlwjZqvriHy8wpA-hKaTdfpdJ5pvP5saKy2BdIyYAV-qwDpquC9c6OkXK27yMMnEjqAqf2jvEf1nXesfQpd4qFmfCWDsGSjYFwNGTiFbdNCb2e4V1lUFf-QTvWKHyxW1yVZGARk7v0GF-9MUNlXZJ5RGTICrVL30MnTMlUJb7i3UT9OlirESLQ2fFHrYOCznQ9Y1iJQIBBMSr3YYiw8Ad2RRzxSinzJMeRQPYLckO3Z---kLk-gRJKiimMc1m-fMWALTAXIJ87AR3stYCKk6yHFmzTJupn1XIS5t3hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسمی: پس‌از ۲۲ سال‌توپچی‌های‌لندن دوباره فاتح لیگ جزیره شدند.  با توقف سیتیزن‌ها، شاگردان آرتتا یک‌هفته مانده به پایان لیگ جزیره بر بام فوتبال انگلیس ایستادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22191" target="_blank">📅 00:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22190">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soKvzhBNIgra8XQtrhsj0juC-4imZV6r0ENK75KOTO7V2-MfIveXqWjzH0EggzyJsD2jueBfBr-Cxw2vQrnO1jEz14ag-WP5Y9O5MI8yg4iEtkDPxYJYHFoz5HY0DaF3v4ZhdtPILRTiEcRYutSaTSNf1Qf8C4jOsGcCx6qY3j_KYdH4bN7QZCDJjun-lppWIVixzqGsZMXx1u6gnm-vL1akiyAsG07TbLXKVJL3Qn6rzTqs8Hbjc3kA6VytCADN6ErCdtKTz7vaZIoG_VNKooIGZpdOJqL-8VQRReqSN7TFxAdKx652kH8G8IGO37H41BNqmdHzX67DknAOIHPZZw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22189" target="_blank">📅 16:41 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22188">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCR3Mw0bG7Rr5ANDmCAXKOjFHAApUsZxPHykB0vy74HH1RDqWdqFPTOuLZfp9fOy5T3znvE5fA5zMNkbTbOJhQR5o8sPMaGzVvEvz3HC-pFOB6c-kuG2bfBlOXIT-RRkUKSWP9JjsdDn83mgGP4JwbForRktsToUH8bdUfKZvPHBgirQf8mhQh8VqMq-jjQLRRuicbawMrO5AAOtLO6v6KJEJ9UF6KbTKTsiYN8TQ42fPm01J_wdi-AO_YPMsFDy3PAdI9Cok5NIM-yZT9ClCGtxV1E5X03dizTkqlx6AZb07_HnMORseACcZmpRRTbk0QI0Nk82OI-SArb0CoEkVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22188" target="_blank">📅 16:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22186">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naU3ltq_bs7PRqU0yRkat1I_EalCnmPqdcFw51JmVreFnQ6SRtBOF7hbLjvLXdOp0WCjg8FoW94orktwABjghLmHf79sc4BMxOSIC8fSuh9iUB6orsIo8yfLBH-MhCdHhhWTCXb9jN1cmNoVCwjcC_qFiEuXPZeek9IFtSaBbnh9dy-uxkGE7L6QT1LIJF6CsUkFUgdandWicKIxIhN5YJUJFdS9cKwXqJ3FosG8RYRJiD7_E_c__ZHyHP9cGJ7LNHey_yVp5IsLHSV5-XXAx3rujWCsaCIHz2db7cvZxBblErg41kEYNGMqEJ3WgKKz3sIsXDgbrHtfcGBwJ3E55w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا
؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22186" target="_blank">📅 16:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22185">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAzwZ2NUM3iNwOt4pBO7YRCdJk5t-Z1mP6nSmc5ctF83eJyaKGS-U1EBtpf4pFJMrrL6KxBeSNn7iYpkELMNu-H0x09qqRAe8t3q1KCmlxnseGf64ot-knVhGFv0-zeo-NGlXZq2UBmSlsl4VXpjgsor8OxYk_xUOTzM7V6HpA5UA8wf3YFAgeJOWv55hkjROSqr6GRgblRhdgpOFVOWYJ1MNNAoyOS89luSSr7spaj9giDvqWwp-QdLHNN3KDJQx5mHL-8SQZ1cVVrFsM6AbF92FKYCZA9nXNhTrogptTk6jCctFVL8Yoe8wYSmLG-gOZKMLbzn7UOkGGYQC4TVGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22185" target="_blank">📅 12:56 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22183" target="_blank">📅 11:20 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22182">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8AGGs_XaNblIc1NN7Wt24EL-DM7L8-lltEyv_I8UKQG2IXk6cUhm9OjQUta3Ezb9gl2jANEgAy1dhbqQtRhI4Ux1fxHUhE4PCr9jlOGo61TIKtLp2dL-_f96qX4YfT15kd35kLz8W8zwKNyT92YtjnUBHG0i54mv6yWDkWpay7-efOonHmFTVhEC-281HEn6QDe3cLBGDkN4ocsph4b1o9j3CKxfi4k_0fFdY9Z92IuUPFraBa02tic4dV2XmOoBNDurhYEzzN-AFvPb0T5UlfxoeRmsClbFv8UcYodW_MOGQgM1LNL3foXIWy0DpLcJ7i01lO3ega_sJrRTdI_aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ پپ گواردیولا سرمربی سیتیزن‌ها در پایان فصل ازمنچسترسیتی جدا خواهدشد و انزو مارسکا دستیار سابق او در من سیتی جانشینش خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22182" target="_blank">📅 10:59 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22181">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4N8v4XmPL75fU1L5wqOi7Wj3l8XR9Ra_Y_o9h2f7elu2zODtg1MMyFe0397mFZl07e1P01csivxk5UbZJNl4GVRjG8lMo8g1NSELCqnNpA0WQew770pXX1GtKMM2gVAjS9uXTTZDbopdKdWie8UsoyXx_4n0J3tTXZWCHxwbqdfCBpyJDGbA7PCmkt1J1ksQRonbPQYsoTVO9mmtg60kxDeqhS-yBXTLhNByHQ5iOnRbKlv3FR65ZzIUvqu6TKvXEIoR8sZslxk64TLlJp-CKXvhI1Aec17plS4InoVp19gS-qTDHAJxvDcrr5OrghYb0Zn3nvo6uo6pra3sdumaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریهESPN: کارلوآنجلوتی به نیمار اعلام کرده که او کاپیتان اول برزیل در جام جهانی خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22181" target="_blank">📅 00:41 · 29 Ordibehesht 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qkiiYfm42TKkJr4JU_H1788y2AAiskS_v9EHC-CO2eiwJxp3BTKebmUjmUoK4KLqCnt1c2SJQG2R6ShKHuxsx2dZLFmf2pDdx-iRI6kvmhH5IkGCCeDqzTMu-cDTr4jXXzNn0LLk-HeDJ7Cnv1_rgJ9aruT4DCSD47m-iMidXQkVoae1YI2nV2reIHwTDQrTlPiwAmdmZijJaCUmlahWximG4XwS4-Dexn0OuLtBFeMFb8P3w8Etz87aaNrHBWwG7jdsmJ33Ol19YRL1wp7l1ootAGWaj5SabzQ-UCj0vPXSK4yGOcMmE4lBWrgZ3J7WmUJl9gEuli7JfTRd8tqSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3Wa2g6hQJLr4I_G4eGHBL8HTVnmqIm3HknIVx4sXvnQAESmatXz3d7wRsKI88PU9cl22w9P5sQKb6-Cu8-Gh88-yAVzMejqptLucI5buB8da4Aq0Yz_tMOmPGkcS172Cfjbkl85cZnqFLSpSvIEBS6noxsRHxOWWkfHrT4x6U5D0AtNuUWjMio7AQThLznt4Js2OePnE2mOqcNsAcpcTXCF1w4egI9fe4Dpk-Uhb7HXR76S6pbLxHAfp2Kde5YPlXivPysrg2PbXx9cT7JC0CVDpHFtVmXVGEKd3tcDr496gcOrnlCpAc5kE8oP1hC11I1mIqHEBVG5jVXDtgtbCw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
مهدی قایدی ستاره 27 ساله ایرانی سابق باشگاه استقلال در کنار پسرش میلان قایدی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22175" target="_blank">📅 20:58 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22174">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYX1fXfKBCwY96LHvo-KFdQSRzF_byqadzzQVcbmaIYnrdaUZK6jkvVNAX_PmDcLtDJ-quh8uyhKaVRoTa2JrByQGFsvoDY5J0Z9sQhyvUrak9SlqYJAwordc-9h2LsKX7qUx3NvMmRJKZrbEne9yXsxbhqX4mloAtuqz3RHVR7mnc13aIC-awKYGqkNWcMiCtXiKe0N7A52M_k26AhmpVUCkUwPEYj35qmE1zpHPF1Fx8uaz1p7eJ26hz1bcshJLtETfWwAKZ0FPY7sUbRW1d2GjWhaLIFOztZnbkxRkh31MkMpfa3KLGYwDP5GZiALspkOvWeaXKf_7-2lzw8PIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22174" target="_blank">📅 20:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22173">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOImxbam2m0SUcFKfBrKuCt-xQKwm3omc0tpf0CLgO80bb8FhSxWLJkFtncPWRrA86xHojnlDck4AThIoTQF4xT8G_PrJ7botIN_SNEzECTLGCoVlR83yA6Jcq54ZBA1WU3sL4ilMQOHE6gIJ0sDv6HHTePEj5BPIyXYLKRUECxcz664bOKkzlpTEki77RPhBWu5v06rQICTbNSc5jobfCAVJIQnidLPiyZXjsnlxJBzJqWoQkJeNKL8i-btjC0ndDuQ6aorKnPoKG7Y8pvR9J3tORt1M6zCmy3xRvk1JlxCo7q3NCQq70Nn5nZXclEybMQrK7SAJV6MRcY8x5bK6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
فابریزیو رومانو: باشگاه رئال مادرید بزودی به شکل رسمی از ژوزه مورینیو رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22173" target="_blank">📅 20:15 · 28 Ordibehesht 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/841076b140.mp4?token=tehfC2FNP81CUuN90woLyXNL88isRA5KzCN4_tXUshGa_P6fZqY-x_DI8jq5UaZSNjdQ8DJdNbgyFc1gnt7AFVEoXlo3pn5JImVaXizJjXtCL9V8vypF_KBGioYgJ3794HoDHEm8mPYJNrJaR-SqKbI4NgS7YHYGnqZoVa33h9EeQ6oTwfzcBmusAFl2-vMPFU5lItwZ8jGn29STq4cQmaxs7zFXxocLwiQLu8Yqa6Qrcv8aVx1ud_OS86vc33x7Pikw3BymE1A1dG_KmsbJ3rWoBG2Iq71i3x23RoGuYlDjFo12Nu50MgZkQQTzMupnUBjzx6J_AWRG5GVOxgGHug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841076b140.mp4?token=tehfC2FNP81CUuN90woLyXNL88isRA5KzCN4_tXUshGa_P6fZqY-x_DI8jq5UaZSNjdQ8DJdNbgyFc1gnt7AFVEoXlo3pn5JImVaXizJjXtCL9V8vypF_KBGioYgJ3794HoDHEm8mPYJNrJaR-SqKbI4NgS7YHYGnqZoVa33h9EeQ6oTwfzcBmusAFl2-vMPFU5lItwZ8jGn29STq4cQmaxs7zFXxocLwiQLu8Yqa6Qrcv8aVx1ud_OS86vc33x7Pikw3BymE1A1dG_KmsbJ3rWoBG2Iq71i3x23RoGuYlDjFo12Nu50MgZkQQTzMupnUBjzx6J_AWRG5GVOxgGHug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=aoFy9CHqsGs2yzz2gV7ivs-rCYvE8VynlcoGS-jg5jKEUojr1aKzoqEkOoHlKOssRW-3swHFuh1Ik5EWiJYnPVdsvLaYm6jSBhSUJmimaALASjGeDtH81gCeAzyPDtwROUFGqxzVCOPDknmLi71kvI9nwk0-bSiufq_qXn8OhIGzYPBWhg8iffVv-NSDkTR9pfzr_FKf3sdahilDqMuhjnYWxbEkJ9Yr923xzCM3p17RH6f9aWXCu7WDs0Vtwdj7cmPZseaSjpt7R4kimqKzahXCnLCbJON40qj7BzCMtb1xD9WrWzu1O10MagFlcAxU--XF6PSCmP_vedU7-0HCLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757af8f5d.mp4?token=aoFy9CHqsGs2yzz2gV7ivs-rCYvE8VynlcoGS-jg5jKEUojr1aKzoqEkOoHlKOssRW-3swHFuh1Ik5EWiJYnPVdsvLaYm6jSBhSUJmimaALASjGeDtH81gCeAzyPDtwROUFGqxzVCOPDknmLi71kvI9nwk0-bSiufq_qXn8OhIGzYPBWhg8iffVv-NSDkTR9pfzr_FKf3sdahilDqMuhjnYWxbEkJ9Yr923xzCM3p17RH6f9aWXCu7WDs0Vtwdj7cmPZseaSjpt7R4kimqKzahXCnLCbJON40qj7BzCMtb1xD9WrWzu1O10MagFlcAxU--XF6PSCmP_vedU7-0HCLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
لئو مسی آرژانتینی در صدر بازیکنان با بیشترین تعداد بازی درادوار رقابت‌های جام جهانی در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22169" target="_blank">📅 08:31 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22168">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLfPTcblzqDqxSXxnx_Lp92d_kQzvGDjzgaMmv6G-1IRgXOScabdJj5kU19HdZPm-v_A96SOsho9ZW_TPLqHerDi5JBrdf2oQKKC7V8kdiwkYB3FRAGkr6Yu5f7llLh4hvHY0xtMsKnSreMjyn7V1FvTyTfz4nalwm87guGGJMZNiO9Yxmx9U2A-eotgYo3M5p0Bv7TI_1z4b9wMlseZJY8mIfhUnkASOewSv5ndfSeZnuJT1R2wxULZy5eJ2XfoHVxElTVpJaoSbURCcMtW3iKjROy224Mwzmihu3jNpERd3z_gJQUit2Zek6y4NT_RRlQfMwESa1mY0NhsD5IWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#لژیونرها؛شکست‌ تیم مجیدی و شاهکار منتظری درقطر؛ البطائح تحت‌هدایت فرهاد مجیدی در دیداری خانگی برابربنی‌یاس با یک‌گل شکست‌خورد. شاگردان پژمان منتظری درالشحانیه‌برابرالاهلی‌قطر که سپاهان را از آسیا حذف کرده بود، به برتری ۲ بر یک رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/22168" target="_blank">📅 00:37 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22167">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn2KlC5LyF4__qlu5Z8rV6Nkr57SP9XWPEUnV5bdgG3oX40z76-QFC7sL7s9JW-TGtuxC4APOBKo_pS1GzZsAZ7CWaQP8-P0cL6Uxa4UwsZ841FCn-eRhmY0k0lXgqscxX1oa8BjrtFTEIFPswC67gB2B1LbPqeZJEoGNMotFa6UL9pbAm64ya8oLeSQyVw3JndL-_VLy-L_5xz4Qj6lotXfIqdC3AXAiRBtAnKYzx4_fYn8cUngtmx5-w425F3ffWFSu-g4hVClq-WkP78vl8T2n2a9J24iARq-QnV3RoV3vdbXC7pjViyKb91VeZ5-vZ9st7haIRAZ8WMhaB1O8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22167" target="_blank">📅 00:24 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdexpUWuQbo2b7fPBGEPE9EI3uMzZSy3VCa2wOyDqr0sqTpH8UMQHN-g1aSMzNizS7I7V-yZKEf40FrCMoA6_f2hh1n8RjlWyKhy5OlM-RGMzJHEkNKvNhKnt5wAg0tjyfiMbK_PGfEncUjC1JoYdSbjVfu5b0EJfqRVzXsD3Sre0SovUTqhgbj8-LtxlUCsrDzMb7QV1Vw2U_lTuRR9-eKK7BrZB1YB2JbB1TL_s8Mis9PB9XiMFHLtLzNOacO24vOKqG3PBehOZNzjszAgGTgpC6Gz_aXHpSqNcY_HWgYupSU2JEhIBgIZYLxL6dTDfsPzOGI6jPIbNM3HWmYpyw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1wCoILd01V2_uCWp9OexKdHIro-6m6wLdAvwPvWFo-zLKhzd6ukr600VrOQREF9OIQW2qoDiXWf-Olu9NCOKjW8seIM9X5hRkxjQ9u647IANBsNLI0LbXMgc-wRSs-khDPxN5fwq_3RerB_CefXgzmGGK0UUGA9wYqRSzxvlh7r63gKnYwLbDoqdrgaMUXwnkRjAt0tdix4_Cnz2BWBB--xcVoSkiW5NK_6rf51Zb-xKxEUjx6FmPrFR8rBr5ck2bvgIIUt622MVkAOdSZ_WPTI53FV5kKY8yqzdMVe2BRXhfBMvxkWvWoEGZ7Uz1rYXNfB5E6AivODOluU9N1VPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22164" target="_blank">📅 18:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22163">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sn5NukeUkoW1IlWuLTA5j9TbxTcFWDNl5GLKY4Uox2OqAvLuERmiiOFdCfgTN7hg4qKChAH4TC78oC23GhYt8abW-arZbvKBb4qaFhaXela-1ON6FV-nRfnzRZlT1KwSWTjRU7ek8EKqxuGiiRIpz1BEr_b-rWTdRKBa5leBdeWNLFxq9DXSMEzLraow6rZ1pFgIol2InbKIotsuFVQqB_2Uozw8h83TcBX03e0zshM3VcxZaMeTzo0wm-7174aV2wswH2j0yHtM4XNqfp0kWzMLHu14kTVbwGJhNFpbnLY3l22WkViIlAeajMqfRsK9CvgefrLPKLdMf1PfSzFVOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
متئوس‌کونیا و کاسمیرو دو ستاره منچستر یونایتد و خانواده‌هاشون درتعطیلات کریسمس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22163" target="_blank">📅 18:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22162">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuolOMk4oJlS0grLF8c9oUvDygw211OI_e30GL95T9emu6C75AxacMxY88l0YGrQg23WOZ-n8sYEW7ukoa8qaOfQQtwXKgwfUpnyxFqQ5p42py8rbvXqgAE3gel7EU_BEOtW4cpR2xcjeBuVZbZjQtOxenQTq78OaEcJwZOmqHJRSzH15C3ziyjrN94Hf1Fqjl9Tsz18iJbw6dqUmYFsIl4spdaPV9Y1T5Em1U-DRKBGJNhEiTfBsnG8asL1UocgAfsFJD40zs05SAnZc1H2xAQ9E_ok74AsMsYehjw3EgNbJOaZ_2O1MYaC1-alBmbEtPGFFNTfs29I7RJvHlhlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست نهایی تیم‌ جمهوری اسلامی برای رقابت های جام‌ جهانی 2026 به‌ تفکیک تیم‌ های باشگاهی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22162" target="_blank">📅 18:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22160">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2u2XOCEJoTGhdXGXzI4rq2Ej3T84la8EorprHKfc9yzJNmsDF0JYhQQgtiPtKz9A3hqk_SUzSG3JWnRoT_Vsh9AaIipifdeBPhWFeWZt9JLLW2c6sebIiUWbZZBRW_3J5F0AJnY6YUtJSK11qa5XyOm9ilIRgd22qzZ5h6DzSWSxxIrjDtVlXHInbllwJ-ARrPVGqwn0rxqTdlTifjSjDY8I2Jj_iUcF3v4QeIKcalRiHhWtjKInStpqfaurrosP5Qy5p0rYXrZnapFYU3FI2xl6wLedzQWFgMMrByzBspx6pKW3WNaKVQ9kjKg-f_ovF4_4RZjAvIJjGFB-7KWew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22160" target="_blank">📅 13:43 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22159">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7qocCRsNxFiM5wkc8wl3k2QN_v7brciGybNNwyVSxhac0ur0Cji00jyIvfJY1mWJGBLqJFshgfF0CBrT4TyGJ9EZcXwe_7EdvbNcUMfVEX-VLALgAy9N134UJxfsyAQeS2Eo2vmFQuH6j57WhffVhIDY19ejz88PvVwgeoLirzccO0NLCwwmY8VVi-3_2LxWd1pchoNXUuRjCOmV0m0g2cfbAU86cHiV7txg9eExf6kmONxpMrlFys0QOCiehJPE77j4yj5e05keUy6Fsr-HG2jBP8i0te4cHZOJ4JCbGlhRY5208j_iXEYnc2NmW4y72MkTMj948i1FQ6hJGmDzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22159" target="_blank">📅 11:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22158">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPWpx9kRrLQU-EJgEb4lF0JZ0g8mxB565-HXPhqywPDvwZqU2bDFFK6vlZCAydeMthUGxIMSs8qBASvryKHIMvbo3WgvNrntr0KWQb9TP2Uxzr1DA_TUTk7WPIMiTrUjKuPWWCUc5cXP0wIYMymQFTpd5VLeeEaENf1PYXOZNaIQ46ic70uTxVksMxMrTnkwGZ-oflrHffvrGPzcyJ5yJDpd-lkmaEd0_Z2M_JxWJU22MHOBG5GR8g4A6eI8vt2V78xffw1flr-u8dxE2t9yZPFrh-ZLsr3lw9j9eyuB9UTte2MLlrQ8BQuTOOXBbh2iLehxecfdf83UAD2xWJEr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
گامبا اوزاکای ژاپن ساعاتی قبل در فینال سطح دوم لیگ قهرمانان آسیا با یک گل النصر رو در خاک عربستان شکست داد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22158" target="_blank">📅 00:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22157">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abyYYg7MOFRKJuriRKTLgdHz-RWLhr0wDzNTAfS2x4SY2iWfAWB0r9gTq0lX7an0w6MTBW8ia1ijV9hhKKkD92Q2d0MxZSc2YFywAVdKLMoaa7zSXDKLUSx0bRlao8XTBAu3b6aNIEX4ZDK8qT1fq4Aaxf0oFmZMX0tqcj-458Cn_4CQoD8aisoX_tZb1kp37Ex4HmbTn48UeTAr9QHT7_oMyi6MOAm5CI6EkfAW98udyHWt3I7EsuIhT1Pz27AT_lIZZbZzCWbg9jR67QLEjtzusGBtKNwO8h1VHv6rIawPwq3wGn8fglBexBjEYeP7x40w50qcaWx1QfdzT3CX5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22157" target="_blank">📅 00:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22156">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTbk2FyW0TlJAHCz_rcJUR4bzEDoAqwqs_GI6ZsGuLykNfQZaTYHUileIaZMVbFJzutmfUxVwlmZ1iECR8bL5jYnzzKtJ1a6lCd1mguwu7KZxqP9Tq_j7tiihlg0CZJNLmLUov0ra2KJ3BLAkpujUR4lPZtYaJJbJdCmEeYqE6cjP0QDGIOFDhDJjQncbX-nyUthPSZFqmjidMnngbNCi1lYH1nLfS366-T8wqzRlkOS4escajVIDP5DofzxBWvr2Ig9fZXaz-JUQ0g4w3GkOiMpwqvEtWwcSyLEtSNnXLo_E_v52_HnW6w0-eS1PvTbl0o0qtfpyem_9pb7OjF9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی: باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22156" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22154">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiT-JokbM70W2wcVQYeFbLhtXQ6U1coHpgtBRuHxvc39MnGBa0zyN3AvG1uDHvxMAIMWXMJl6Af_qM33piZOf5w-jZXjy3w8XDmv8EqW0mAwYkFi5aAkoBn8xShr59kVj_Fcm3MO19EzZzzIjtzQgO0CKlBlgpHktEjCDhBnBSqWSC2VKvG46mQSXgrPkv7uoOkukbxvYT3zCcU0N5sGV2cZ3poHuYeq5hTya16mStwOYpwXZpzNThOfxl5bLeIXWiAIr1d3m0_m7_w7t4Hu01LGlL_gWgTWdvG9DRNfHhx-UCn2ykDzCnT4umzk9A7KRZkEAodo2faYrpUFcTCwHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
تیم منچسترسیتی با تک گل سمینو چلسی رو در فینال جام‌حذفی انگلیس برد و قهرمان رقابت‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22154" target="_blank">📅 20:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22153">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Npx1bTDWjIblZTWQfMm-eRaLul6WdLFAJdn3-BDBqnff-XaSWPxE4_9WHMu9G7HQp_oTNlTmSbMn4vtcd0o25sAsdp-Bsfwst2r-FxNNp5IvBHMo3haUQUzpPTCC5KBdv4HWfSmg_Se5XftXdKJVZZcE3Xx9pCTrfJ_-tMQFs_SQlzq-e96i7BUbq43DiYC_yzqC2IOwKXKBzoWypqE0vsXX5t7TIN_7QueHhcHzIzOgqmsRKSXzea-0yGI0GBYNhzjRXUYZFTsAKs-mEKu44eku31SpbuQI4_aR8iLwmoOamrQEHCvHKwQ1WxlDijAdG81IJ4yfcG7UgqevdkZneQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاکا اسطوره‌فوتبال‌برزیل: اگه‌اتفاق‌خاصی برای نیمار جونیور پیش‌نیاید اوقطعا درجام جهانی 2026 بعنوان کاپیتان اول کشور ما به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22153" target="_blank">📅 18:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22152">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQ2DhXkukL5ina7FlOdGZKEn7rxs9gLFDMDxn2TZmyxoAnlUpWenM7ww5C8ionGLQ5DAUa5AR8G1gJZrxkDTXbHCaSj5vPVu7LPGR8F2YfymgE4aBCuIBj8fsvuexia5UexdIG656FNntS6uitGActWsn8bKxGfU5_z6R6xjitDju0aQR5g8EX3ILVB3nWsAKZnPq6mS6jTHE0WfbtYYrYoVB1kzuf9-Nom1_lAp8uS1z-PTXMvhCNvrbzkRoKJ0U3NhgcMUqPpakNAz-59I9a2c28EohTVXUP41S9nrlYGtGoTib4bRC0YW7-HQ6S9EErHagkvChGkP253NkNRXLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آخرین آپدیت از عملکرد کامل کریس رونالدو و لیونل مسی دو ابر ستاره تاریخ در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22152" target="_blank">📅 16:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22151">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5oDsaPMTODPXryPDeeK95h5_5S0Qa2ujZmzVazi16WKw77WEyThm5vOPP0p30Mt6uZp1Lk5Qm612ytL4z1s9IwLv_EQUBFzr7D03hTpkucJ2SEIG8Q94GJk8QbeAeqi0J4cJ5yB8I3B_rZCcctoyuo6HCvCdmemiupgscdax0ugF3vHMLTJ7hwtNSWdWXwXUhYP32WNNH6a8YBZ2FLwAYgRc3e9CWhDm1G3-sqN4Me9PKTW6g8QwOllPHcz-xhZ_RWShhxwurszezu7ozaH9YiUd2osuFjq_SkH3atyFCZmX2L1zJ_xjMLe5Q3LFkDFWgWh5YRdVvZdT3pWaMSy9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رویای‌فوتبال‌دوستان:خداحافظی کریس رونالدو و لیونل مسی باپیراهن‌دوتیم رئال مادرید و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22151" target="_blank">📅 15:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22149">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGVq7r3vVR33OZLvsa9L09g0x7JhtSX9Tk1KqP7L3tQZI0rR9leJmfSWrFw6Ahr99eyrNvI-Zt5tu81jnNs1zmdG8RF7NlpfB4Ne4zUUPQ3HMXolz2IlaUogIaEkANXApjOp3PYaFQxirqDehQzonSLs-HjYW3qCi3ByKlH29XQgPV9Rv20xmW4hY6vQSN_i7rMrdHjhBttlSM3uhj408wENTS42zGrML9RHTliqLiw-lA4Pe--OaUbnhmIKoNBDkdsaPZXesQx6Jv-Vp0FTfCb9HoTBLfwXUWo5Wfa3jNfwVFaKYXIEuoJ7NeizJBG21MVI-WMGV_OTyoLMIilZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رابرت لواندوفسکی ستاره لهستانی تیم بارسلونا اعلام کرد که بزودی از جمع آبی اناری‌ها جدا خواهد شد و فصل اینده در این باشگاه نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22149" target="_blank">📅 15:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22148">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AL3zduejzcjXU1_Hd8xfeKlv7cxFJwY9cfSkAvbH0LHnOS4lbRv-0kUHoDWclx0T_jFMADYmq8Z4HAIp9l5WMLOMyp070i2tcYx-Yr7rT6hKLI9XFoiEjyjW2DWS4zpQu2C6wsw4RdNFuII0nav8lYeBsTgYRZYu3dFIiMHNg8AVQF2PbCgV34bYKDYc0ZojCWYveXxom-mUc5lEAUiuoBCm9XKbHrHD8zIGbbGvMj0QB6uv7G4oTylPkPE43JD41A0ALfMHhYQ-Md42FCyTornPml5LhK-YYpvtib_BIRm16NfSOE_Y03PRHB7KnTeCVap3Fo2fhD4aQBG0vNbBcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22148" target="_blank">📅 15:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22147">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqdGXTCChN2izNmx645qdEo_fq5LXWc6FfxrgvcfOpmhS8zHOCpzVrIhP_u5njV1SZy23e4jQSvvkYf5t7BsXgdPtfaxUdiCSSsBCkjJqm2G_AMrNnIHTRSu5vCpJcb7MfqZ1GwtJf9f61QFKKU5Jmx3bFusjMAEiU-1gu3eHPa4YWnb_Jp2jiSWyLbwdR0M1iPPGCfdi-aWfnsv3E_HkpHJUBVicWihjl_XYWmQrtpFwXqAnQ8vtFbC5Mw7w7jONuMjBF2UiVIZ2Kz1uaJB2wO2GB6eocFYWDp7XzsnXPmWJn1geXsUQD_NuXwmiLeYHhIGJsDH85BKkrz1fAnZxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22147" target="_blank">📅 12:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22146">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tny-7DjSoijI1-iAjnKI_G-SASFuOVJfkpoMyEtnzaZCDOO1Fkya0LcYGCMrdvccxH-HLj_K4tRSWbCOdFFS1NmHAmAzK7-IXk29YgFMenB3Mk1IVwHphw5LBnbf0ltQmD6lr4T8fSTQL47ojJ0qiKvdMRbQL1cQ4H9PNGEipRaofj3D3KpCTceR9gGLEN5whMf-lE-CHJCpfgOcjVRGrq43eiWL5yrgLop4CxLM5pLOACBsNqeZZ3JaBbGTEUihbaDo9z_I0lOQ_zgpzuGoTuVKuJc-SfKfyFlAedDMPUtyc4aEueyF9NgEcRJhfcgKJmaciLTF0mEXoHi7ub6Euw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/22146" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22145">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HA9JHDYSO431QUkdVYYVQHJg5mqf3LnBw-sMoiUlgxJMkuSvy7xmeXjiNc0mQwaMPqitGhucKqosP6GL9htsI10bX_CSo85gI1vW3RuhbuQP6QDE2LpVrpSnghradSuffLtu-IlyNqdiajqdZZBQfYPKlU4gUWeTyM0BRsqF9q3UkC0aKX0uVLreijjVB746VilNajsSEFZeAowxcXOwpP-_XMS5gytzIOIAY6hAw8i06Uefp5f0jw24iZM7hLWn5vuu8_yt9hVwr6fLyoFKvLNlBJOgibTnh5fiaxucyN1elkpGlL_A_ChNz1rYvYjRJttqQrwRbg3jrw3r5aVcbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4yBCvYfB3SLOef0JJehFNZJlCkz7TwZtXGX5WYzJVl51Xq0MqB0JcMrKoS2W66oUdWbppnHmsBDWxZU7e9Sf78wm8oixyOtm-0JNLnlAehMy-kR_3zB3LBLbdaNA39_qj-rV2vO_FFWBV83Src4ThMhpZW1w8IunvMpX9JvwSti7A-aW_ZDIU1c7qsO_MtADLx-jqEk_RWd8ljICAzF-Zw8YnYry5GB71tE6VYIweZsoad1Ce3-AYc8onQqzImldtU0HvAQW7dnxUF0ulO8lVuJKqDqh2sc7S-7xMM7rvO8bRtFf8m6ktgfdA8ui-9qWfPYvvQzo5Qx-HRM0pLh0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBdLm12VxZTYRGGbez3wJPkbY8DnY168s9rPHXOIEJARcUMtiMqjpMkuVIQ3YTgL9XaMcenHqaczhpwLnImvk38271xPassP5HogUqHrApkrGb0jqcHtS0bcfoRECAuQC159TubreMATtanApqg2BKPatut3TrAgu5p_TZiAMK-d0nRJJgZk5Ao4d484cEP0j8rUDMGLYXGu5j2ino06BJ1AVShf4NnkOK16UryufWwLp5PCUYzcYgKRnfp3y6sCDrCJNLgYYHFP9H3Y5dcCSv4H2uN5fySKYoHYkH_hxSKTlJXoBl77OzN2IDX4Os4_CQqHUTBw0128zGWAfZ8Nmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMW9QLUQdrK6vOoQq4fE_t1qMMdJsWYJf8oQf0EOgE4vepxl_6xxeVQyBAz5XDwE5b8sg3XsPq7PgQV3olTIMCAf0JcxXd6tDsOzXwhs5uZrHTz5IUqfeiMa2pl9BrpuWCpNfoCzT1v_e1S0txUXZFLcn8TdmfUgNX-s2mXJkSmhiAs_kaH_nCF5mqvpvaYHng9SpQXuMVraZZlfybqgVu7p-u2ViF2rwbUYzyLzS1MZ11N3H39qwXpzCWNvqqRzTuALBDVjv3zkkoLXKOMgLPd03n8Lr-XC0XQOL5VSdM8gTaRHtNLnzYpF3ezLqJZ1S5Ztl3XUntt-a6mNPsWwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw4XYfsb_E0NwprZCuDzo9GFUr40Pw18tjlUCxtB4ZGUQuVRLqigPHPNdMUtQaRhBQORpLJcBqM9-TLHqFTEeh5QAu4aP7OclhBiQutwPiIvx3fHrAzLUGQP2j0k9y-v3-lvwHyTTiOi-PJOgx_ttRSvqlk9PiCOpxa8BwQuRzWN3ECUb0uQvrYxE5u32yh4Y0BSiyBZVfa3I41WHiTNrqAdItHvQfzUEJtaZDi4lLFms8IRNK35wKbzW4m-l9R1sPxSwsy1nOnJPvAnYgo_mGB8I0qp0q9Tm2yzDNi9mRE9sqLYLLuTFw4OYJut2zwm-QLuCc3cZU71bt6GL11lGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOAjGYxWJ6P2BKbgXUhAwvm5urjkow9Qov9RfmD9ylWJefhyPnCo80ABg58vXJ1KRdQ6LIaEr--F1y8JpqggfNoykGiH1Q9exyjMYQE65OAnKeZJs_Q6ZznlbuP5OQq5e9rv6ock-4YiJhCOtcPpbGreTH1NNDP4-sEVNw7mGzc8mgPBuSLGC-nwi5QlQSiZnKDOpXSm4iFcVLK17Ff89U0VwfqX-__HH9PUStzIOuPuRQMBr63iXxdSkM5leFFyzPhFLA6ZRUPG1-MF5GoGaQRm57mOAWbQp800WQKwIYG0ChHFKflf2xLDVj8hS7FkskyTdIIPDOWGPMGRt5FQRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3NO1wMfH8yWGEJWuYXluviBUmeU5E1iZRvzsrJr7Xj2jSpMV8XratFrI_lxQg47sPqgYbgCz6QsthDh2WebN9vbpT-z9KKtsGvU4jqwwhTZizUjgixSQ1SOS0I8BwAC3GuLteduAXSVDWXU4ClViusqgYZpR3J3d5mAzlig8jm_QYzzs_SLRm8Wmm8fEKfH0LEJMnQk8bh3a7bxIgCDK6DTrDAs8OcE2sPST8rgS4Fp8QpAQ3TeIiP8xT-C2Fs8gW5WsQwrXBloJfgReWtz4ZaTbbgpxJh22abn9kWvF224nHzC9nb2hC7Aj_moQI5l6W8id6m8zmPgj8EsTPPUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBhi3KVkI5h72pAyGwHx-2CDCf6rLwrCxylzAI9paXPu7ep6_wKFKbzCgy8mT52cD8RQHWjvIRNlqviHOzcs5yFdfhGvZhVpY89_tjijfCAkbCVLMWtI2Wnx_Hgv3dbZIzbugqTOt7glPQrJkf4IBdH5T5xyDguSrIXAcI9FrNS5ndcA-vXgKA_TMMeK99wHVxzH6rUAoe-8eJnBoLjOa3JzVk_6rkOIhXiAPs6ROwjdRSDeugUNaZMrIHnh-k9lRKKl-2FLK1PZivp_vxAYz-YnVGodhuPWQ5iGAoihk2xm2v-Xmg0nyjbgf6hZYagKcpQ70yFrIOEvA2EhKMm59Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=XbqMKoUvgEl3pwpVTHs1Cy2zEaYRz8dCxSBP_6XbKpBZ04YuIcbboba4XnqLii4YyDm8nM1Cixa7N5v-dlSbR7kld3Rddqw3vkyhsXqbaSqTHB_j8SPwO5l21xf9fSThJfYdKvCfcdLWlkMNvODznkgILXudNQU4C3nf7FTsXKR1Ngl7knKxR3lTrf0vjeNDUo0OO__p-F3qVYk2V8u3EjJttWOO7hrANR8A4KmcKLIiEVG366kNhY462TkRk2-vk0E62OPtZcfytyjiTyj8c4DH-RMCeSTDouyjAoegVrau9xikT6c1qAJB-41hFgN5REcKIFrH5O-1tpAxIMbsQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=XbqMKoUvgEl3pwpVTHs1Cy2zEaYRz8dCxSBP_6XbKpBZ04YuIcbboba4XnqLii4YyDm8nM1Cixa7N5v-dlSbR7kld3Rddqw3vkyhsXqbaSqTHB_j8SPwO5l21xf9fSThJfYdKvCfcdLWlkMNvODznkgILXudNQU4C3nf7FTsXKR1Ngl7knKxR3lTrf0vjeNDUo0OO__p-F3qVYk2V8u3EjJttWOO7hrANR8A4KmcKLIiEVG366kNhY462TkRk2-vk0E62OPtZcfytyjiTyj8c4DH-RMCeSTDouyjAoegVrau9xikT6c1qAJB-41hFgN5REcKIFrH5O-1tpAxIMbsQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXvT1XKG2OfthrJpFvNWISdBQ2Q3zXwv2wz8uFyMcv7tcBhwvl92kHzbZaFfoPot94tvkXpU7xjh5GO7gU9bQyZkBYSmOch8pNWagoRYEnb7vKYDdIAk23wnu4wlsqkj7Bo6VbFOHecVN2ReHi8iHsiVO1m3mTx74_LcdOgr6oLLpk6EiZtttaakDJcXUSfv-cDZMmFNibyIpjcrgKsqE2ukLMK3GKpC59xeNM3b_tLY1kL3ktA5zuhUhFHYAhfs5R-vK9J1GgfDggcin5qITGEOLaWC43mOQIcNUQpKQfqtUFMm8cZk2h6j47bQs5HSRmCfaU3MtKV8L-MiCPTMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vF_V9fJ-LPDx5eivkaUIvTDsnqm1lAR-4-yCjSF7Rruj6X6JH_-y91Ge8cx14jyKhtKSy8aRWcfn4Wj7NTv93abQX5QKoFvWHH30vbJydk521c8IikY39sCPeRaWgp1w8lsV0LCsK1s9H8xmBHHJ4NbJ1W3NYUAykNhV7gAo5WNDlJ_ID-UiBK8AyidKikCv8284NHRKAhkidVtk08vt-zT60K9NuaY6pmsh8xvldETTJnPW11ztA6jkfXOunQ3hiypkigsgFfNayowUB7wyzSVJe2pWSD8feg1Pirmth6y5BcSjxZmKX0uKgRwwO2qdCYirpM9F82mRq5CafnrpRA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F6jeRGMJYBYECw99S0E4MwDFw8TBIA61xb8_m3QzuMiQXwbre1dD0qofRdTaNDjDrjsBMr3NlneDX9OcnlK4IW3IDsRYkQpmWoMKvHb35WX5AQwov4cX5Yif2Pry_b3YQ6vfU-s-q44nPDdgydx_kufoZb45inYJ3uFqT9FBDGNy2_4cDtbW89MJoTPWbh6wL4VXcxDNkInX7aVN3eqESlPcBcYHcLrGRuOZMNTNq7_AIEzMYAtwf-i5UYOMrPaz33DFKKxL3STTXTuu6biKsM3iDnNsf7bLmJRisndCZM6EDjs7N6FcL4euJH0-rHPdltzLBBPzYVHQeYVT6qtHtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGbDT-_MHgSvHw5h2mytO5RzuwF54wSwob_MzervnzgRtWuYXK7Z0_JE1XORMJ_I_FinZxlEizVKZa3tlmQsj8No6ct3MvowFyCX2EMAmmbKV1Ofidza9Tqt5OXd2Z6zUXzhp0dFs-79f7FV9mEeq0PpU_tQD2a1X2GUeeiEtqNequIbo8lXvS2hlKjnIvLjQ4bhMKRLPS3CyIjxu4NGwK5QBZG84PYjsrljPn-1TBTN1iV3qmb2lNFvZKqpCRo0BwaG_Pjmch8VHTxh5n_W2nUvbrfcrRnfAukseE5Uocks-yv13ZRoyy2M5IYC5fTJUDMybvx3vH6-wzEhVRtOQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WlQeAMSMqziSqvyeW4JoWGHtcD06dzdBmrpt74Pw5iIxqE_QAakqdjqDM2Ln9Uqgmiv52sNFVDSxDlytTM8gdxIjc-OZ5_Qqr26-HapxHEefnZy1OZHA93MqDsuaTuR5QwTrc5NrKEIaxmeUNciIxgVObwtvDWMaU1ZPinLDtrUmuWhAiQ4UYhQxvFcQyZypekQ-al4xI-RCVtpuoZTETdX1tAXdvEEf1cZrd9aBAtEmKZoDJqFVlRN0sAT8MRhiqm0xIIBMf6czK__ofB8fVOFnr0FIO4pedOWspjeO91iqPRm2X5BtYxQp5G2uN686VKKwgwOyZJR60F5Ty9Ewkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGlFMxdVQ38I4ttU1R1V26n4Z6-OspVFFD1xa1kI9gOn7Q_ZYaiF0sb4CJs08NThuoMcKUmRhhhLHTHjSqghqh97aHpjtlgdlCfjj1h-36ohnLtq1Oono9ZrpKThcU4A0qoYy0a6JqvRETCiAxZImlrsLMQeVXuxsj8PUe7ZSAradUD2xZ8py99V0QYyx20qft7Tza__N4rebhCgCOTg1OSzddnXIvz1GH1C2QVmxaFWY4RJdX6_S0KAAJqr6hdLco8uxly0Jo22iYXT6PU_oEwwGDaGzvltygWtu4zjEgcbrDFkTrJb9-f1wfu2Bw4Jd_lAdIQ3ygtFvNxGqBMjsw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=oVIl7yxuyCElTLNQ4X38o17JDbhVZZBNkinjbjoRV955zrrb0QMkQ4-O26Y0Fges91apNQNm_dYViv9w2E45UFE8yJ9D1d_TaeHx9eP7XEX-7zzxkrOQq3PDky1VhPyXCpT-ViEBVbuND41wyEDwqhyOSyJHTa_MRgwqilyS9KBPgv6aIJzqetcLkud-N3POUrhjA2UlvP9Wie4JF9pp4f6fzxrXlDIzgskQ96U2zHIFLgqGeAUzuC5zowpNBKPkofyhbdjtr-1cqaWjP-2Jd1wuuWFMW3ySxSbDSWkXuLUDQyjqprW3S1wMKr1aQ54LGBCJxvNdxA_zzhqPuKLxDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=oVIl7yxuyCElTLNQ4X38o17JDbhVZZBNkinjbjoRV955zrrb0QMkQ4-O26Y0Fges91apNQNm_dYViv9w2E45UFE8yJ9D1d_TaeHx9eP7XEX-7zzxkrOQq3PDky1VhPyXCpT-ViEBVbuND41wyEDwqhyOSyJHTa_MRgwqilyS9KBPgv6aIJzqetcLkud-N3POUrhjA2UlvP9Wie4JF9pp4f6fzxrXlDIzgskQ96U2zHIFLgqGeAUzuC5zowpNBKPkofyhbdjtr-1cqaWjP-2Jd1wuuWFMW3ySxSbDSWkXuLUDQyjqprW3S1wMKr1aQ54LGBCJxvNdxA_zzhqPuKLxDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fokGlP51q31kuLZQM1tYmesLZDO6F5OEPBOhGICgf0C4w8EcCYVQFxU_gc5wsmC75VC9eoBM4Pa4Y82iXO9Px-ZS_WRVkELhZTjI3n9KWUQFb4yEbiACiXP12IRJ4akdG3CD3o6N1uxeKvQjI7MZwX-XIVsFTRx60tgxnWuos3Qmp6-ZzU241RUp2SWF9mYqIHeBIv2XnheWJ8smuitWwj2FNJtn2X3HzBRSNZAYOB5UgE3k0YGUUaIJD52zy7vgml_oG9OFNxOm_vLI6AuJuVebCA3UCQvy21bfAZ4KuO3_kJ2nNfQbqXqQXnD1DP1_cGHk56t2ZNN8xTrJRcSuUg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiKu_TZxuktctekl9WFpLd46Kck8McopGvi_bhTqP72kdhz1t-GU1NYmU4P0pjBnw-hWlbMcL3jcMimMiXZMFqs_WtMTuGW7o1ok_nBIxUA_vvdgFOCcWUiV12sv6eFo1SaaOR_4WG62AkvYZzCNELYZqNuIprJZYINNQmXfnHWixCxzkVCKwnKv8OE2VK7lObElImx5eishSN1wEqZlzwaMRH6Xz4vSe51VKNcE0rYvfX31KPjiN6n54AiHa9qaF6Q0qHmzskkLCwhiJPo4fGEnDMtwJAkk0QFHfApDN7h1eCGpK-U25f5NoAXDIXERPuafpAy06s11gdS4G1hquw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=D1GpG8VEun6tsyeSNzqmZrglFkiBzfnikYKF-9-NJk023kHskciag_0pHDJaz22NYBkuIFiiocSH4P_HXxqi_MoL7bvc4ozSo0JsbyVA-lZEgmhZWzUWCsmY2rfMnA7CrrNkAnknK2CBICUZrKx9WxQRR8SpFOJMe0vAm-KzuozUTMnaVGe2Cf7oi9Rc9YwFFYnLVsx-OxEbIYGcop0Wn4ZV-BqMRI03n4erZtLhCwg3eyjeNvw1-I2vaig71liNbnyy-DBJO1nHN3XIFJuk05BrQ9Du70gfzwCQwYhNgzbZMphI1Ljsq8PtFj6JlxbMws62gZAPFqY1Nv2Mrh0pZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=D1GpG8VEun6tsyeSNzqmZrglFkiBzfnikYKF-9-NJk023kHskciag_0pHDJaz22NYBkuIFiiocSH4P_HXxqi_MoL7bvc4ozSo0JsbyVA-lZEgmhZWzUWCsmY2rfMnA7CrrNkAnknK2CBICUZrKx9WxQRR8SpFOJMe0vAm-KzuozUTMnaVGe2Cf7oi9Rc9YwFFYnLVsx-OxEbIYGcop0Wn4ZV-BqMRI03n4erZtLhCwg3eyjeNvw1-I2vaig71liNbnyy-DBJO1nHN3XIFJuk05BrQ9Du70gfzwCQwYhNgzbZMphI1Ljsq8PtFj6JlxbMws62gZAPFqY1Nv2Mrh0pZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo376uOr-T3OwhY6U9HD0C_Sr8YDbywcy9QkUz3UORNep7W-CN3R9Gl_KwQfY1y9ckFbGkKSiIINLMTsKtMdSfUc-nNPuB7f3yriO5MKhlS28cRavM4L3HpjVl6o8_Zn0u-b44J5IP0auhVdpYybRdWgYDwVqJw02HMyL-T9tskXSrdo2vNdYEtfQIZ-oMwXZCQf4U_8EcAcB-y9pznTv3aU9SQ4mdrAiRJpw09Q6aLZ_MQ2fnbTmyk_dPJ6s9eqEPBdfv9Qs2Ay_E8qtam4aw5-tYwPdzRb61HW8z8LXZgSrl28zC5HdMOHQgZBUKBUoQJzW-xZ7cZxrCD00D3zRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/XpI3J6R61JoiIgCazlh8Qrx4Z0JGMdkfuVOTT5GLbhZvHnFGdkdrUkeRt24G65z6RFbdg4qGWfabW97oHlY-0xwpkKzLPMCnMC0bghN7XA_7386jWUHCt6PeYQyt9JrolRVWgPZmuvsygg58SO1mxsdVkj9AAXv37THYxTpOCblsEpI0VBX6Gc8VjitP4f2_TaA5qszwKV4MED_qmNAjE6ZXFdYguaNLK9ecfbnu3U4Feyzv0LCZMeicElDTNm4rw6vXtDetoSo82X39qc79jZGKh0kq-edX_CvF1fGOjWIWRU3WgCCuFpVUbBq404fi9jQsJm8_TJmVfLDlHAVyJQ.jpg" alt="photo" loading="lazy"/></div>
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
