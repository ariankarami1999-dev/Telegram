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
<img src="https://cdn4.telesco.pe/file/e4d0a7S_EFaC5jLDH0-MTzdTrAtGVAiRPTjyNCSDwHhi7uRWj4u08z2NO77aPIH80Id3wEgiRr0fMBf-gTY0ixllEBKP8BvbGAkIbIOmyB-haHvZ0DSZw0xJ0QaRIyKIAf96nMAtFr-jMvrIbWx_r2uj_Y3Rf2WPImf2lxrgt9u1bowIxDPbUgPZ67aZB3_NXIYr18P9A0tZG7lVUoAC4O5yQB250gFyeeSToBFtd5C6J3H9QosbX2kBD0gLTDUNeZeb9obZ9wm3c1eqQSRFqLuDPHAPDRkJJ-4RuMMyzBmRfj5OdTSRk2x0-DOnrN89hQEsx1-j91xBGVl2UGt2gg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 146K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-24 21:13:13</div>
<hr>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVPHReCSyIWk9Z7ACn6d0L0_UR4ptMHq1lx348bNwybq-PFY8GERbcSqewBLqQliwl97F4dHBi_kQkyxO4wWRCzunScdvA1gULVpdXvT4nAOG5T8lDseH3SuLTUmKj73jM9xcpHofipXsKRoWIwP8fsO1XulP4hsbM9KZtGTSoBt693PV04wHp9bB27UaM_n13QrljBQq12nSGCIfi57rUV5ApTSfTkkBOOvwh8hzoP9pHTml3Y-sbZu5Pe9r5ZqJbJIofHhMj02qwzs8iR-ZCzya32Z16CgonnCcJ_HWB5HXF0_DWXOPdURAlKMScgPSA_2wycG9gMUr9Rqxzx3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64911">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=Y0ogNeh2k_Gy-Tltm6UldP-4HXHUkSj1WSumuEgb1s4W_M0UVLyB225XqhOptBAavcxHNwQHWyxT75KCpv-J3Dqmvl8GCIMQvSTrmUnjkYeoDvJnth8g8Ze8BgZ8QtPKxgNLhvB-YcM9nJsw0jPIoLy-5wbdE1TFyZKDEnysPHG7MwVGzsY12kydI1ccpy9u593ZgqsCVgS5Uv_gj-El-OPzM1TNsdnK6IHqsEy0AWBulYplzxCiWUMwL_c2qHlPEMiIOqxSv_HvT9o2Hw1bLTfAkiRPDa3RXXXewBII0aXs2UOMFnfOuNddGRh_cQ6aVU9FZJ-VupaPD5lGY0TSoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09aa0f1cc3.mp4?token=Y0ogNeh2k_Gy-Tltm6UldP-4HXHUkSj1WSumuEgb1s4W_M0UVLyB225XqhOptBAavcxHNwQHWyxT75KCpv-J3Dqmvl8GCIMQvSTrmUnjkYeoDvJnth8g8Ze8BgZ8QtPKxgNLhvB-YcM9nJsw0jPIoLy-5wbdE1TFyZKDEnysPHG7MwVGzsY12kydI1ccpy9u593ZgqsCVgS5Uv_gj-El-OPzM1TNsdnK6IHqsEy0AWBulYplzxCiWUMwL_c2qHlPEMiIOqxSv_HvT9o2Hw1bLTfAkiRPDa3RXXXewBII0aXs2UOMFnfOuNddGRh_cQ6aVU9FZJ-VupaPD5lGY0TSoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ی دست دادن ترامپ و شی
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNteQoq6g6rfefkr5xXhhIMNPPgddpBMHjun_fTPe0dnJdj0GZXe_jqZ7D13-AZAnHW628FtV8i7qfB6WkHQzTv-jYwPE3d0xTl0wEK3h_RfqeVFPgpq9HO5YB3N5olI7Z7oepcg_9CC8ijFNiv-1OZ0hS5i4MTA_L16JvTz-KIzX3HG4uUjaX5ks4_ajSxXWZwOp3KEIlqgA48yWakEF0l5Y5HNNBO5Zxz3cgh4dmjN79zvtxJ1PCKCK3yamQmW3E94mgbboAiBiV1m-oAJMfSjO_Af0m0tzgrxFd7ZZjz9fksnaPn8Gm9eUm_rowMgIZ3Tzqns3Qqmzu0CWxpcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64908">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇺🇸
#مهم
؛ برای اولین بار،  اینجا در کنگره امریکا، سه نفر از جمهوری خواهان از صف حامیان جنگ ایران خارج شدند و به قطع نامه پایان جنگ با ایران رای موافق دادند.
با اینحال این قطع نامه رای نیاورد و تنها با اختلاف “یک رای” رد شد.
در‌صورت تصویب این قطع نامه ترامپ به عنوان فرمانده کل قوا حق قانونی حملات مجدد به ایران را نخواهد داشت.
اگرچه در نهایت ترامپ حق وتوی این قطع نامه را خواهد داشت
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64904">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eA0Zf1wOjBaTIjn1Oj1utaEQ1ncikN8H5mJK7iTgMCekzG1EWS1N7Oe6141susOCGAvRIUuV24994ujSrPVp1vpPr5-PirooHq1VWv4wpZydj3cypsDUXnopIgVaiHpgExg9vpOG17Xjmb_PKZOYzT-NeQhJDMZp0nqnszsf5pJduZcabpKaCGzSJr1ahVl_YqN8WsW-6h7L5iTtZR6ITPCpYZHJx3rfzhXn2lhOCYzduEBO4aFpINt-xteY4Z5Mhmq4ytrb0MsqQsRmLGmF-sLlGkS9TAyr2gbr8LqfqwIITbAMqJFLHagc16ZY1bZiHCWQjlRmr7omkCrazEsdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyoY8hQ_2mns8lNvQX9C8mcF2uUzirnRulS5ruT2awCHmmFZOPlYG3VZrk5jaVdEw42kka012Eypi0i6f1DV82NuxfjVbQtgSw1TnwMf-2uF_GpiOK7mU-Di3n0NGSzKyKO8joHlzaN5mxUiRvtfh8os27jX_-ygXF6bK54hfbRmKozvi7am1NokHG-UpxS_Vr0TjfNusAPcSMH2QeRmSfXa2XSHXM_fKbLEsnOtj5KuZHtFKbcASE_W1tqf5ekj82RWyyaGE0HiKABr5qVeiZcgdo_OF9BTc-L-03XJDQr1H1kMwo2q6usn_Bj8nasLpMJMy4eKQkw3bPbLNBr1JQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=hmoOeOk98jq-K0CEK4K1AS31lX2Df0gyS-wvn4vcu0AqV7CPFSsjailqYORcOOT7-FDA-ybjaND2-49ncDx95_7Vx517VU9alAry7FGP2k4SZveMVyuq-FYuWN1DNXmZqpBAt_4X7XkPZW-TiJguAuXVPnJ0AEEd6V2QKwYucpO9B6o88ddTQ_DxlAFMJ5IsitbAdyaeMrNC107XBvYJoNDRSX4S8PqqhGN3zczeMINvwEwO4LO0-aCWFKukd7evNLnSZS2WLKKahnyqtBTNiHr6wyPai1e6hb_LYoAVJSUCVMOTrRr0CMtmIY-09wubqQyQrJSYCbb2c1v2DlodFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8253c8a3d.mp4?token=hmoOeOk98jq-K0CEK4K1AS31lX2Df0gyS-wvn4vcu0AqV7CPFSsjailqYORcOOT7-FDA-ybjaND2-49ncDx95_7Vx517VU9alAry7FGP2k4SZveMVyuq-FYuWN1DNXmZqpBAt_4X7XkPZW-TiJguAuXVPnJ0AEEd6V2QKwYucpO9B6o88ddTQ_DxlAFMJ5IsitbAdyaeMrNC107XBvYJoNDRSX4S8PqqhGN3zczeMINvwEwO4LO0-aCWFKukd7evNLnSZS2WLKKahnyqtBTNiHr6wyPai1e6hb_LYoAVJSUCVMOTrRr0CMtmIY-09wubqQyQrJSYCbb2c1v2DlodFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مردم تو خیابو‌نا و پارک‌های اطراف پردیس بعد از زلزله و پس‌لرزه‌های دیشب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b7TDhxZfCVTGxLUUz4d3zVS1qn5W2lQOJZa5oaevOr5wHjcmxzm6QRltEe7qbgfcGp7CTcttcgzTqYNBA01PWLgL1x_8Zx7rHstHiYyux6agChqdCQUkQcy3ZU51jkrluMFDJYTemWZBoO7JJFrvwtznB9XbC_vywG5wk6gOdjPKFsVjWfAZugmY2EchNpBJU7omwokCELaQRjvdedYIh6Tl2LDn_pqd6oA4aSGszOFeP5eKPUYAHLXllLovD5IQu9GXsqXf46upk1iUgfj2PXmV9MZPD8oLbInwSqSO2wQQPDiXhhkFJmWqjP2EZXz_JkPHT0lwXoUaxXiUoQ-yXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k_QBeserCzHPfpyIeVAw-T77UXwNNfpa8LbZcpYUeQwUNpuc-h_4KpVU4wDxvldVZZe9J60h0TveV11K7uQmWpO24aaQ9eUwdH3sr5uMcdUlJX53TBQm7zOO8Nstha09xEK2lPKnIyO8ucKQdNBy-agbSXwDpAC_rl3REb8edji49XT1EpNFX6jKALtr_wNO3NFH2NdGveOPnK-bcDdg0bvZj9UfvAz2vTP5iRJL0l4B3kDqkFED_RlNa-0gQYmvEI0lUkYkkxfbyTTPGSwQz4NttOhyOsEDkiuANjxJbzAi618HNlGFBDesaS9Etme55P50342gFwMAPUiER10hRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64899">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cys-1xMXjAzA8-LKmdrw0xT8g9YPiIgyCan3YrSjcFR4OPqZH9SvoSGheMZum8jkrDpEq0K-afwnCwQoVDrrpZ7FepoAOAaJprPmQ-AE_c2in1YQPHvb9FVASV1PF1vaqCv_74si-dd4iAEfWsXSGPUVDEDOL7nmOc4_jGgufSMF4xPpYlRDMijiE6C9LpbsNjt8wjhtDWPbkoUKauxYa4GbShGuQ5J4REGb9xlzYGkmp977ob2EHv_xMP0mcmVN0Ebjf220lqFkcBj1w1J_MQT1jGzRA5iS8vLmeopXAQ6wG_wyEIMy4oAnTlfk_8WmVYzJ8Mng6h2VbSf1qse6Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PXRZR_uSrRknIF-rvSPB3TCAoGJDLurWTzUjxU_P3klO2EGW4Oef2GZHpkALyOYbsugvi3lyJiHrMzamMAtpVFIJKydMLUyod89Xh09zMvS_XtFtO1qkHuYVoMhKjTx2zVaJlmxpDQTr_GFEqKPqVn_xnzWzU78SYz5jKN5FjhZ1BcTWQdcS1tof3ro7eoe4ZgQmYYRY8TO99fznaJzdjsYkjUh7G4S7Ir1IVSE6D4Oj2Jbb3QbL4Lyfo21yeVxC_NUyiKkBeNnINjah48FFzfK57bHaCAddQj1YPZLy-E4oGK3GHp3-z5LlPOuFEFHJYK64wt2CRhwuMgzXRnacMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مارکوروبیو داخل «ایر فورس وان» دقیقا لباسی رو پوشیده که مادورو پوشیده بود
هنوز نرسیده ترول رو شروع کردن :)
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ihBlVhBVkw-RGItMFrbVx2Cw6e2uXTKJO0YUyRKyS3TfoajhQ6ifZ7qpfqWe-B4Ex1s8xb3eBYEJW0Vng6XNcq0p7STwcwoCLgwYHhxm-iP6ktw1O0EvW_clqp_SJODj2NAB2YiajmBSdJzcj7BrBeC6z4WVOBLpg6pJ-ET7_4zsDgI7AMmf8rpMHBV1IkcVJd8bh4kIEOKGpdqA5OUbJCe3lRAQ1t8TB9N-50l33na3G68e9w7fFrmVR_6kJmp7SpWZitIP3LXm3i71qBDwCXrN1Ib9auIm_o7BsK1rTnkifI3wQp3wU8keNwcL8oYKL_6rFYtvSiyKJi50LfY_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kEUIUqGhVmSKtgZkvRJaxBhzoTrZgbCqkMj7xrGDiAOQQkCptEnUbmz6Ppjr0AbzO7f_rxhd0-gI2rnBhePegdEIGElSMHgTNCDfzwxgt3XNzWp9q5-8EqcAMjEh6HfGGyaxwzsLnEIU5kBXpAm194SnCO3LBCteyEMl2zhAJdm2XSnV-PwSclNUtkfa_mjNihn0w8pcgt9jweUB5oKfI2QW3hFzfh0JlVD_crDtvtF4tSWMQ_YeY051r19vHGFXhCLzriTcsqa7xXzJGw_jBPywDBQ2QqdMMT6MQxoFOOOWk3CAmgYLfpWF7gGL7U8SBo65JST7X4HM4nrLrO0Mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64895">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=D-CeSTJF3PeLj3RN1bs7pny3zTpa_xK97RJCUgegzs8hkZ-ulslNvxUzitY5L5eyYq6PIvv2ofORTyz3nEJGCur_eGhAwW38WgGnVhjPlZjqLjTUjg18QFBXdBJVRf9-nvuUZNmj7LOKutYJj33zTpkHrVft5-VEIf1huhnlQrb9lTqiupWTSnF2Zd6d2dP7mptkUq3IGJt_s6MQAcgplxX4iTrJnHfpljSvQMe837X6_eBVcsYmk4ImeMRGoVoc5_y46SO2xgItrDvyfTSJa54pe1IYiPTio0x8PNB8r5efJf0sc_zk17M30OqziD-sEJq3LEp1MCfm0E13H5AKWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83afc3e388.mp4?token=D-CeSTJF3PeLj3RN1bs7pny3zTpa_xK97RJCUgegzs8hkZ-ulslNvxUzitY5L5eyYq6PIvv2ofORTyz3nEJGCur_eGhAwW38WgGnVhjPlZjqLjTUjg18QFBXdBJVRf9-nvuUZNmj7LOKutYJj33zTpkHrVft5-VEIf1huhnlQrb9lTqiupWTSnF2Zd6d2dP7mptkUq3IGJt_s6MQAcgplxX4iTrJnHfpljSvQMe837X6_eBVcsYmk4ImeMRGoVoc5_y46SO2xgItrDvyfTSJa54pe1IYiPTio0x8PNB8r5efJf0sc_zk17M30OqziD-sEJq3LEp1MCfm0E13H5AKWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پیت هگست درباره ایران:
ما در صورت لزوم  برنامه ای برای تشدید درگیری داریم. ما برنامه ای داریم که در صورت لزوم به عقب برگردیم.
مطمئناً در این شرایط، با توجه به سنگینی مأموریتی که پرزیدنت ترامپ برای اطمینان از اینکه ایران هرگز بمب هسته‌ای نخواهد داشت، گام بعدی رو فاش نمی‌کنیم.
ما داریم یه ارتش رو دوباره می‌سازیم که مردم آمریکا بهش افتخار کنن
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bE08i1kp2lOelcU4SXPjN4uco1ScimhwZSPoQJdTa6gYz4GW1RetuxlaQ8TkKpozSAsSrgbBCUDcmmNqlbnpr0NBHen3K8V2m1xx6UUbEhRxBkozL3wONuRs-H0Yyzd4C45nQ2WjfIbF0XJqIyUbKogOHZvU-Mpu_2RiHjrzmyoHxLmW0P_FzUp_k-1B4YrpyAeqY4AwSf3r4MWYouUpTyDmyFYaRBkU5-UD4vrHE-7yal6ZseTxzMCioiA4rSApfF3MTimhusVWv-iXbQtfSG9HDvBS-92q8TRsF2bzmNUblqPOF2CvSt9yDaxazbqTzrm-PI4jyMnlOGFkPkg-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KY47M2weuFwLaKJVJiYzmtPWVRpWcCnBz0xzIKBsRg6PR7cSXOx08Q2IECTkIVrXc8hJgQttZf43eu9XPJ1NRR1CLSgf9el-wEQShuY3qimAd6PvsCGMEM3588Fche3ypz9FkSs4ueGrytN0Y1SDJcOTEllBNKhSTBqXUEveM9J3osTTwDrFFUgfbDuQlHGjOAzXsrkh45prR5qAPIlmAJvdQq14iyTStORtf6py6FcozP5p677li82xxgpDGjreCPl0qMI_RSkHGviiWUsFJq8pZrQBlLPPfUM1FBpc1f8ncLpSQ7htG3vt7bO8679xBIAx1NO-NnkMMDA6iQAKwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPF-1Bly__OLercWiTXTHdX8kCDhBFZU07Mqz_ksWXkktUMM-ua7C40zuMRMwdSutM4UevfbFKXpGmmJZDPDbgmT_7Kgj19ulCykXdjM_nrlKb3NULE4RIAqJzrENPi-1OBb7Fzu8Rg-4jSczgpgJIYV3DmSqMnb9zhgSgrDQFDrn2xGsp5_QU9cEHLz58-ivn8iQxu1m6wAfx5y2HB5t-3LpU46QhTcPo0iGVUYVAFH8BaCEEttF2emeDu4mnRNrvyUCit0BNwpk_Q4n8zn7KKBW-m8cLNYuLdIza9As0G07EZwiOC-9ZMDkYivOYRdEBVQLm8gKUVXUHM6tIBXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64891">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=beWxp35BhIOFHI9whXub0RVQxDSqpztZKlCT-JkeRobIEEz4Tnr2BdAngV1bwAUHJ9vGF2HbqcEnTN4t0jQYbMTlcJtkgkx0irEGOe4LPerTKWa_Y2t46IWOqzEATt6vec7Qm3dkzsbXllrpiQpjR8dSLBbyQcN-shMRXZm_TIMiIONo2_eM62zEJDa9_zKyK0Vk52uqMiALewikbkn9u2m2eBpCXrqGSYwme26QdxnuYbrs4NKq47c33Bv9T-isWZQ5pPaClo2e9lJpWc4Kjm83jJe4xgGsaQIqZBswpelwgv6A01_dGWavsU-5e1sm6hYAJBbo4ayHjxYj7ewk5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbb21e178c.mp4?token=beWxp35BhIOFHI9whXub0RVQxDSqpztZKlCT-JkeRobIEEz4Tnr2BdAngV1bwAUHJ9vGF2HbqcEnTN4t0jQYbMTlcJtkgkx0irEGOe4LPerTKWa_Y2t46IWOqzEATt6vec7Qm3dkzsbXllrpiQpjR8dSLBbyQcN-shMRXZm_TIMiIONo2_eM62zEJDa9_zKyK0Vk52uqMiALewikbkn9u2m2eBpCXrqGSYwme26QdxnuYbrs4NKq47c33Bv9T-isWZQ5pPaClo2e9lJpWc4Kjm83jJe4xgGsaQIqZBswpelwgv6A01_dGWavsU-5e1sm6hYAJBbo4ayHjxYj7ewk5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ملانیا بهم  گفته باید رفتارت رو درست کنی تو دیگه رئیس جمهوری پس از کلمات رکیک و فوش استفاده نکن. من هم همین کار رو می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64890">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=K7nz3-jmK_TE81xfFpDTMW9uNkEkKi_Caoz2l4F72cHGdb7r6RqGVg0rOP90LY2dZ5EFDh7svSJ0W4Jp_vS7ExEINcgNKm-d3xuJrXOmC7gAyJqpRKw3RDXr_u4DOjG9xx-B9f515-k-sdyzTvaWNcAcD4gUaUl4qoN3KiYwEdk161GrlpqUlIVxMfbWhNvNvA-u1yshTSlIOqIK84aCKISOdfxLEYfTMISKobypnfxYOiMGzucWw0N6pmAlHYUBi0JNMWKCVXocsaWgnZ7QVWFcA3e4Hv324rfAaAdwNeHcwCE2cpRERJJvS727yXO0CHlTMUnx3wF2eSB4yAGqrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba55a8b78a.mp4?token=K7nz3-jmK_TE81xfFpDTMW9uNkEkKi_Caoz2l4F72cHGdb7r6RqGVg0rOP90LY2dZ5EFDh7svSJ0W4Jp_vS7ExEINcgNKm-d3xuJrXOmC7gAyJqpRKw3RDXr_u4DOjG9xx-B9f515-k-sdyzTvaWNcAcD4gUaUl4qoN3KiYwEdk161GrlpqUlIVxMfbWhNvNvA-u1yshTSlIOqIK84aCKISOdfxLEYfTMISKobypnfxYOiMGzucWw0N6pmAlHYUBi0JNMWKCVXocsaWgnZ7QVWFcA3e4Hv324rfAaAdwNeHcwCE2cpRERJJvS727yXO0CHlTMUnx3wF2eSB4yAGqrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ درباره نماینده حزب جمهوری خواهان تو انتخابات ریاست جمهوری آینده امریکا:
کیا جی‌دی ونس رو دوست دارن؟ کیا مارکو روبیو رو؟
به نظر ترکیب خوبی میان، من معتقدم که این یه تیم رویاییه. فکر می‌کنم کاندیدای ریاست جمهوری و کاندیدای معاونت ریاست جمهوری آینده باشند
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kc2LpyLaguGV-1CJ4Ce2QItIdYQ98UqbP8LoJUYfd-5T-IufyYe_iA6Wg3cIyyr7UlQQYymsaRlajcxaTKzlaKHYj7Nm-3VQkHtQrTdMH5gJwUJni80QkTqWbmchfBqtjfG9BSCgKtWNzgDRQ2l_5QZiEsHBXhsR3xN6wC6mGCjrBo5HXukq1rRNHy_hr6cU09nq684KWDN13LQOdYaoHlxn5C9-Hcnsc9od92duJ6LY6ZR675x3SK84PFY-AE851ug-F46UTR_O3PpQMxkQCJXWojKAfcpmNHUZ3Wu_4xvq4OuliXlrXgUlKHAV2BGhr2KRTKJ46SljybmgcV02OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64887">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرَک | کوتاه فوری</strong></div>
<div class="tg-text">پلن های اقتصادی موجود شد
🔥
10 گیگ => 1,700,000ت
20 گیگ => 3,100,000ت
40 گیگ => ‌5,600,000ت
درسته که این پلن اسمش اقتصادیه، اما کاملا جوابگوی تلگرام و اینستا و یوتیوب هست.
سرویس ها محدودیت زمانی و کاربری ندارند و بدون ضریب هستند.
خرید:
@SorenaVpnRobot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64887" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64885">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/eMURqIP4_Kf7faUXQDQ-yGRH0EfjQULWWhNmqhh0_5An3urBkWoYwuIeKHSoyxAc3yBiR0kLg56BSIXiCC_fBMzuRtscUa3JXv7mawRpWRGuovIhuEDBPoGsH4S7mVAPq1UK6_GIrs7p4WxkPIRkRLPj_msl5_hmyNJ5UArFloDdfxFF8YYgeouYZuClHhrZ3hzcpLg7DhpP_BuA2ahsMTwcAtllk8RPP6Vry9C-VVogYW1pn2ho_yiosfjaeCt3Qqt7fNuLNbhvLZPPezgjAWcynrlGHtLZfe4d-SPqcFch9Drv66yH1rOUOjPq5gDoJHslfN9h_dbA2avR_KFwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64884">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
📰
آکسیوس: ترامپ به انجام عملیات نظامی فکر میکند اما ازسرگیری حملات آمریکا به ایران پیش از سفر ترامپ به چین بعید به‌نظر می‌رسد
+باراک جان
اینو که ما خیلی‌وقت پیش گفتیم
😎
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64882">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyaux03V2KBczp2QcLYK1KOHWzyrmD8dobkLGhsvhrqdrhdbfxz9QA08gXUE7E2VoQ7BtFbCFUu3EYTbjkD11B0vuUxehlKw_-PZUzs7A4d0SdOByff5zgwllwo5uYMo6NQC7VZvOEQE0m4y7DnukVAkTsfy5a_GGhjThRpT5gup7GxikSoFaJ697g0bP_kClsLujGUaSuTspUgcUHwzUyyqUZ1vU-BIbHYVRw36PXj8n-fQqc8Y4NmyEfT-kKO-jtH-9h-cNl_ydS8PRXZGvXvFzGkYmlscceAbgkVWu5hKmNnh9AT8NEI6pEx6g3oW8au1RpMlTBaY_HNMg2EBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64873">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzxDZmBq499c5o2L9SzQa6hoDl0YVZQLa91qtOn01FB-PRuSKkbpesWbek6B5C7IKPhEh7BTaoVzLwJCiFipWHQjq1nzf2Nf_GFGkxIWmFqQyZDJzijt-BL-gsGNMgQB4Dz6fdafpsSFkrudK6Gzoo7E8rRVTzTqGjc2NNTLkoRmTDoS43u5wQBjsCrmaaOOSfUrt1suFwd3e4LdrxAFtVGaMuPjNOvVBc1pqlXjl7UzMzPrThRP3s0On8901un2HGpUWKiGYtDelnVI_Pk5H_ttvUS7BiLf8pYjdGdea4uS0w7e4R0NMel0oik_Pvya0s43PutRWkfYNdq3b6pdnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
لیندسی گراهام:
من از تلاش‌های جدی دونالد ترامپ برای پیدا کردن یک راه‌حل دیپلماتیک جهت تغییر رفتار رژیم ایران قدردانی می‌کنم.
ولی با توجه به حمله‌های مداوم آنها به کشتی‌رانی بین‌المللی، حمله‌های ادامه‌دار به متحدان آمریکا در خاورمیانه و حالا هم این پاسخ کاملا غیرقابل‌قبول به پیشنهاد دیپلماتیک آمریکا، به‌نظر من وقتشه مسیر عوض بشه.
در این زمان “پروژه ازادی پلاس” خیلی ایده خوبی به‌نظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64873" target="_blank">📅 09:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64872">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
📰
المیادین: منابع المیادین جزئیات پاسخ ایران به پیشنهاد آمریکا را فاش کردند:  لغو تحریم‌های آمریکا علیه ایران آزادسازی دارایی‌های مسدود شده ایران آزادی صادرات نفت و لغومحدودیت‌ هایOFAC مدیریت تنگه هرمز توسط ایران  گنجاندن بندی مربوط به آتش‌بس در لبنان با تاکید…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2_uR-dDW5yBDs0NWevSdFIsREkEs1jTtPwnvIZ--mMIIDhUd8kkrOaNofXJst0TwAdkbS_um1uRNj-lmW0MVEpG5VW4pg5xKe4ZaXsbdxJvK9Xt3U-mDvSQQhPW-QmJyQZ2XaYb6sE-3ZQXfkvADa-mpP446XGGxNSDKeih6ZDE7s0Z35cnOmCLLiDcnQfvf_BFgEeFztrGD3gKy6QNfJOH2gVCXon9lC3miAM1hLdV6W6Fh4qCMG-uIF27rDmAz_5NQP-ICijK5kbk3GdSe2PFrc21xyH8QWgqfFoehPgRYuWkXiRuzI2A2YgpFpu58B1HxmE6Z8UhCY_7fL-fRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64870">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=D7q7zTUfxRHVzXzU3GKq-ddOvmu845DIrol8HVYHEHSS0vpUFMymApOoGfHZRxnr1EbDBQWdSceRWARfCkg3dEvQ7VJ458YoVcK1CVvoXvMTDmsSxjbiCAOZC8Lp2jhDxBfn-z42GHKVEsCyrkR7GVKF4B_yMRJmAmx3d1uOwe-F_z9aAPA1eKZthheegC2X9rpV1SECBt_yWWECJny5naRlR8eUsIepj34sA5oSPhptZ06x38N0M4vEcBhPNkfdBBqzHP8GXVQjFfECvmWD3VqDXqiexb9UAj7eZBawTnWxLyobHL61PHySwyL1bAe6F63V6h5tdwmvSmZm9Mi1TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ca5d9dd02.mp4?token=D7q7zTUfxRHVzXzU3GKq-ddOvmu845DIrol8HVYHEHSS0vpUFMymApOoGfHZRxnr1EbDBQWdSceRWARfCkg3dEvQ7VJ458YoVcK1CVvoXvMTDmsSxjbiCAOZC8Lp2jhDxBfn-z42GHKVEsCyrkR7GVKF4B_yMRJmAmx3d1uOwe-F_z9aAPA1eKZthheegC2X9rpV1SECBt_yWWECJny5naRlR8eUsIepj34sA5oSPhptZ06x38N0M4vEcBhPNkfdBBqzHP8GXVQjFfECvmWD3VqDXqiexb9UAj7eZBawTnWxLyobHL61PHySwyL1bAe6F63V6h5tdwmvSmZm9Mi1TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو درباره احتمال سقوط رژیم جمهوری اسلامی:
فکر می‌کنم که نمی‌توان پیش‌بینی کرد که چه زمانی این اتفاق می‌افتد. آیا ممکن است؟ بله. آیا تضمین شده است؟ خیر.
شبیه ورشکستگی است — به تدریج پیش می‌رود و سپس سقوط می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64870" target="_blank">📅 05:55 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64869">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=t7iwZJ6KSX2mLJAUu7rMTOpfiJTPl00zHH8Td2rHpzLBtsrXuZWQBRIXL07FKvjhBVTt8c5s5It8925UoiKgwRJA-qk3fokbf99WuhVQMdgS9XXiUWOGWQZuqcMLFDobi26YnaPo4MYArmAfcNxdLiRi4yf6dzgqU-R5M02qBYvNvubvDLHUGlYWN2wpdQA8oVU00-FR7oP4J_68oQ7DwmHeSdxrcTajzUZ-tC7DEnSfi2PGO22vWQVAg179fylDRDhZBj6hmDs7i853uRo1sSuEvsK5LxEI8CSeuK23CZSPexMbApqnqoG3XPAsNDCZIYAjDlCdGkjg5nP4TZDyDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34c8a4b81.mp4?token=t7iwZJ6KSX2mLJAUu7rMTOpfiJTPl00zHH8Td2rHpzLBtsrXuZWQBRIXL07FKvjhBVTt8c5s5It8925UoiKgwRJA-qk3fokbf99WuhVQMdgS9XXiUWOGWQZuqcMLFDobi26YnaPo4MYArmAfcNxdLiRi4yf6dzgqU-R5M02qBYvNvubvDLHUGlYWN2wpdQA8oVU00-FR7oP4J_68oQ7DwmHeSdxrcTajzUZ-tC7DEnSfi2PGO22vWQVAg179fylDRDhZBj6hmDs7i853uRo1sSuEvsK5LxEI8CSeuK23CZSPexMbApqnqoG3XPAsNDCZIYAjDlCdGkjg5nP4TZDyDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
نتانیاهو:
در ایران، به نام من خیابان نام‌گذاری کرده‌اند. می‌دانید؟ البته بعد از رئیس‌جمهور ترامپ هم همین‌طور، چون او رهبری این نبرد را بر عهده دارد.
اما یک چیزی هست  من فارسی بلد نیستم ولی آن‌ها به من می‌گویند “بی‌بی جون”، یعنی بی‌بیِ عزیز.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IE3Bjym9jvpl-frNAix6uUBiFVmbK-hPQ7OMUQYXtdUyKjQB3VCfHGEj3XmgewfJ9ywEsGzlvg8DDJXFZ1Go3nROM-gU8n8IaMJDOMAG354hgwAmxdzQXqoelxCIuqu9l1Dp69wrdcWSVXdCNeGtud_saDV1q1a9IGKOXz_CPUCBWCAnR-cPKCo72Kqg77-J-dy1nkI_jG7RnphMfXptzqKjIehiNyoBLSUJ5Dw4TToOhj71Ftb2vkUStgdITXC-yf51OlcpTLJ12CGS0-eoOuHUJ_5Uf0Jq2dwxuGfEj57SqaGKYxL4VysW22hAiSfaAUR34UTSQP5aCxza1UqC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rbzFemye1kiy9Q0c9IN4gXnMj9AcmHtpo1ZoFIeGLHOD0Xyh5eaaqqBcB4MxUJUSH_hnG_iKA7ZspEThkqKQ07ZzeXqoMyTgW34Kenzl0b7X8RVoI_o0P3vDSEI4M4QQGmYlUudAZQtrQ-AgGfZGYmYRqIbm0Kg2t7uBEAEl-GaJEkKVIfuSZb2MoX0sOW4LtOgcYWvow4Hm1IrDR_JaFK3IFLiLijVaLH9Dxo7qL3ycqzgLXItw85CUP7Uzde0m4sveFFozWKN0b7TCY0ShCGroAWwcFFKyrESXgfWgmWsgQ0CLu5_s5DB8WbTT_fVuT7a6Lh71-lVLPcek85aMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYtyVkb3JZZRgZ2R-ShZLxBeYrmQrYSA6Of40TD1Ovq1f2oBPzqPQfZIta33t31Bf5W4KrNEkoT8-Y0rdRUTpZS4xx1F-QrDwwAWPh8XT4ELC_-ghFFvc4q_miAoDTDVukyiQJD3N131sOKT5-vUxseIthdvLnHmSg73UJYBxhADa-2ym2z2fp6GToXNyE1DJFbpYNRDWfVyzjB-ulI_9Wxuy_fHxxeenvhY6KrAXzebjuW7xy5yBBLlr5Zc2fXZ0E7mf0G5_AdZ8S712p_rWg2vBT44tkty-2OKt1twB9-2JC0-wpM5vaiBUzxs8Ny0XbBqyZaPwk5c4TP6zNS1pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRa5NVWalaLvwA5hfxlPNkHhOlPhzWAZPPoOjkEM71M4UGYnZ4TMkMbz7oDm2qvbW4Y3PspBWW-R52gMhclqjHxYpGZfMXd56pEMc-NSHmvPh5-5R_O5fqFJ5FiVh5AZxZjE8pDFx1LYZsHpvQp2caeDJbSX4hGeoP667_z0eMV4nYgcoTSRwx_WWGL0w2hTM4iW4bMjrQOFZt36IC9_STezW1lfwBmNxlgmjMXAsRZXKlgxOMFnFpt0al5LwxVUul0pWzRnLb9-JYs5Ac1pvoft7ApYNtGAH3ZSUcBctQjRHGU6JNbB2oRvSy9vE0AMlCBJM8TbpdKEYmNMWd5aZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64862" target="_blank">📅 23:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64861">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بعد مدت‌ها دارم ال‌کلاسیکو می‌بینم این چه کصشریه کاپیتان دو تیم وینسیسوس و پدری شدن یه زمانی کاسیاس و پویول بودن ابهتی داشت بازوبند
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64860">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=E1n5_lRSF4O2rl2awE63QzF5nOCCeqn_by5yzYlXoEwvvGU6Us5QTukl68uMUOnq95UOCTt_MhYoSWwcXluoSufVP7j4US7J4QSyvvAef7IlGbvBIrhHahEEwbOUGL2jXMsEFPOjl2t4E28AzkrPxEAGTZYeS8beJ3oqn75d3GyuHXrm_mg54NNBTjIIdk3XFW6xMkuTlAAmS0tJOfL1USjc1TADY7ahzU-GIp0QSoqU-7rjuKYj4VmnBfpwg54N7-KREVIQyB_uw_vx73DjL-8HUXM1n8kg6zox9tBtuMNCW6cBDYjReChJytcuZtj74BMcVKDmUMA6yQnnRWkYaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d27dd7e9a1.mp4?token=E1n5_lRSF4O2rl2awE63QzF5nOCCeqn_by5yzYlXoEwvvGU6Us5QTukl68uMUOnq95UOCTt_MhYoSWwcXluoSufVP7j4US7J4QSyvvAef7IlGbvBIrhHahEEwbOUGL2jXMsEFPOjl2t4E28AzkrPxEAGTZYeS8beJ3oqn75d3GyuHXrm_mg54NNBTjIIdk3XFW6xMkuTlAAmS0tJOfL1USjc1TADY7ahzU-GIp0QSoqU-7rjuKYj4VmnBfpwg54N7-KREVIQyB_uw_vx73DjL-8HUXM1n8kg6zox9tBtuMNCW6cBDYjReChJytcuZtj74BMcVKDmUMA6yQnnRWkYaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: اونا دیگه نمی‌خندن
.
مجتبی و فرماندهای سپاه:
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64860" target="_blank">📅 22:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64859">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید. او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONAgvTBhu1OENczD3RD5ZUqFFBeeAppdT-rEoltxwag9GXWP3xSY9nHiVbN_qDBrRHwc_WrJMXnEzErJHANN8Y5BV6bW4kzGMsY1chMDX_yzlp2nBRQ5h6OodIDAppgqc5gN96dFBKFtdpMS9ERI5Yoq02UoJWvWfy3IMCy4sk2GZUHtgG2GTPCi8QWuafjyjkpvgz89qaeoVxFJ1YDWeGU8qflepXk0BpWN6SSnE_wHLeDzMDhb3gqVyohPzIM0rUCfl-GTBhDIbt3ZPKBWY7jJ6KzBgpffVz-BQrTJJmrrJav2N1xOJ-3FoW11ETN0xWeAEKT_PfK_2FPVfaUjnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ایران به مدت ۴۷ سال با ایالات متحده و بقیه جهان بازی کرده است (تأخیر، تأخیر، تأخیر!)، و سپس بالاخره وقتی باراک حسین اوباما رئیس‌جمهور شد، به «گنج» رسید.
او نه تنها با آنها خوب بود، بلکه عالی بود، در واقع به طرف آنها رفت، اسرائیل و همه متحدان دیگر را رها کرد و به ایران یک فرصت جدید و بسیار قدرتمند زندگی داد.
صدها میلیارد دلار و ۱.۷ میلیارد دلار پول نقد سبز به تهران منتقل شد و روی یک سینی نقره‌ای به آنها داده شد. هر بانکی در واشنگتن دی سی، ویرجینیا و مریلند خالی شد — اینقدر پول زیاد بود که وقتی رسید، اوباش ایرانی نمی‌دانستند با آن چه کنند.
آنها هرگز چنین پولی ندیده بودند و دیگر هم نخواهند دید. پول‌ها در چمدان‌ها و کیف‌ها از هواپیما خارج شدند و ایرانی‌ها نمی‌توانستند خوش‌شانسی خود را باور کنند.
آنها بالاخره بزرگ‌ترین ساده‌لوح را پیدا کردند، به شکل یک رئیس‌جمهور ضعیف و احمق آمریکایی. او به عنوان «رهبر» ما فاجعه بود، اما نه به بدی جو بایدن خواب‌آلود!
برای ۴۷ سال ایرانی‌ها ما را «آزمایش» کرده‌اند، ما را منتظر نگه داشته‌اند، مردم ما را با بمب‌های کنار جاده‌ای کشته‌اند، اعتراضات را سرکوب کرده‌اند و اخیراً ۴۲ هزار معترض بی‌گناه و بی‌سلاح را از بین برده‌اند و به کشور ما که حالا دوباره بزرگ شده است، می‌خندند. آنها دیگر نخواهند خندید!
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64858" target="_blank">📅 21:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64857">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=QZNmjGOjH_lCdGRDfxRGdkklPHPoh8TRW3NluDXdkH505h9XrAc1jyq4Q_DQqad1jshkoY7GjYaiChNnR9Lq_ZRk_9FZgi3t9VpEbgb92ML9O1Ij3Njt5mb38ZnlT2graNw1wDc2aLvUix12Cd33H4v2oViYhMlKP4Fi_fJNbDa2tX9mhAF6C-u_1qJzr4DPM0qqOfr55NQCRGbKKsuqLVvB_5w4cLiuetgwizRvOpQdqVOLglZ3HWgHfN_UgW1F1uUEuzl-jBXehpXKz9SZXi42eLLMSFJhqzy7XTmmdX_q5vA5SfJHa0w5ApVYVkqSoteyZppSNr3f0izHDKlpkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e4c1402.mp4?token=QZNmjGOjH_lCdGRDfxRGdkklPHPoh8TRW3NluDXdkH505h9XrAc1jyq4Q_DQqad1jshkoY7GjYaiChNnR9Lq_ZRk_9FZgi3t9VpEbgb92ML9O1Ij3Njt5mb38ZnlT2graNw1wDc2aLvUix12Cd33H4v2oViYhMlKP4Fi_fJNbDa2tX9mhAF6C-u_1qJzr4DPM0qqOfr55NQCRGbKKsuqLVvB_5w4cLiuetgwizRvOpQdqVOLglZ3HWgHfN_UgW1F1uUEuzl-jBXehpXKz9SZXi42eLLMSFJhqzy7XTmmdX_q5vA5SfJHa0w5ApVYVkqSoteyZppSNr3f0izHDKlpkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری: چگونه تصور می‌کنید اورانیوم بسیار غنی‌شده از ایران خارج شود؟
🇮🇱
نتانیاهو: شما وارد می‌شوید و آن را خارج می‌کنید. رئیس‌جمهور ترامپ به من گفته است، «می‌خواهم وارد آنجا شوم.»
من جدول زمانی برای آن نمی‌دهم، اما می‌گویم این یک مأموریت فوق‌العاده مهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/64857" target="_blank">📅 21:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64856">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=ILr0ZF0nsh7EZdqO3SGoeNTKWqoi3a-8Cv6OoBy7oZ8DXoDit_oH_M9KKBBj40eUO_wEeik9nO6O2WYp6QuMJUP8xs5A3haesSQrZ1PJdpCFUp3wtTjBVYYRTVsb8R0lDzkW8SqAjrTezmtjENAAKewgAuIxaZim6WzFVDzTJCULQwIlpGcXBv37b6YiVyAKCpVeKpJw_SmsduJT8lMw38jEIA0yo3OIvclWw7HWrDilWmLc5xRQ_eU0ecGaU3dFlYVelC_gSdiuOsQdcZ1Xnv206JGnoPVTqmYIbHxpqfhO6d15FizuD6eczr9X1-8ghr6OYKGpE3qbPK-blczR2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf0dbe0a2.mp4?token=ILr0ZF0nsh7EZdqO3SGoeNTKWqoi3a-8Cv6OoBy7oZ8DXoDit_oH_M9KKBBj40eUO_wEeik9nO6O2WYp6QuMJUP8xs5A3haesSQrZ1PJdpCFUp3wtTjBVYYRTVsb8R0lDzkW8SqAjrTezmtjENAAKewgAuIxaZim6WzFVDzTJCULQwIlpGcXBv37b6YiVyAKCpVeKpJw_SmsduJT8lMw38jEIA0yo3OIvclWw7HWrDilWmLc5xRQ_eU0ecGaU3dFlYVelC_gSdiuOsQdcZ1Xnv206JGnoPVTqmYIbHxpqfhO6d15FizuD6eczr9X1-8ghr6OYKGpE3qbPK-blczR2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: جنگ با ایران هنوز تموم نشده، چون هنوز یه مقدار اورانیوم غنی‌شده تو ایران مونده که باید از ایران خارج بشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvOwLg9EGTQxp-hmd2n0Vxp5tmAF2F5ByYGY1sM_puHirASuIOr5jlym42lqs2KLAQRaX0EjmaA1byFS4mj7rAJwNFeMRdLfcUaqXyk988KOyThsfLts504tEx2KfKaEY5KoV2PNYtKj1lR2Pnbv1Bvj4VpAUFFsJ4gtOlTp-TgyqBJPDpWVupKnDGjs4nQKMaRY0FEKsFAKwYnx-T-0pDUuO2G1JzzA2RZBU6u1X5y_MBm3MCr1jWhW1KpvrbbSN-uvF-ZRpOq0esVvos-1Lw4lF7LiNsieGARh8sDA8VJgq_8U8h5vhgTvdF0Sj45qy8AmvKnzLqioq3cP40nkeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64853">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این وسط کره‌شمالی(آینده بقای جمهوری اسلامی) قانونی رو وضع کرد که اگر رهبر این کشور ینی کیم‌جونگ اون ترور بشه به اون کشور حمله کننده بمب اتمی بزنن
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64853" target="_blank">📅 16:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64852">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qx4KQ4HKaLOMHVqLlU4TYo1bf04XTPQyiR8MhdNjFgZHzu3IZ5dMEkbJSVUvgXinEpna232r7iuaQHs_g7JXj9eLo8ExGbsxMmOF3-lpKwtVFSEz4LGJQlu4txRwYug2kWFPVsUSSUAOpRzKbcUAUc_sg8SlY06zQAxXTFQKq9VUNdWl3PcKpH0fktZQN_byc747xNYJjJoeJGDwJcsoqaN9NsDZZZEFPYcyiN2QiL6P3O__-T2sdCUeklZyCyOEHewD7Wl9IY3IB2YgseOdaDOoBEtCwXxWf8H9Jstfpr4k014s0o4irhEjNAGHeKPA6y8EBMzyuvJCYuBWpIvW0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=Nn8IZ13XI8PSedAXA5JSggfDL5PNJPEOIXyy5JXO5IBmo8tS8z6eSCbbTthB9snU5f6SSHnMbZknNnuwnIfaap8OoIVFqlniZwr1XhW9SK1BBZv0wz5OcNji2cw8k6PbugGJqcjr00E8AeoM69Rn5nm0g4CntDNm6ORjSdL-LBk_34AmXUAV-JR1BAamrvjof1UzbEVG6qrcdFQ90Fq9pnzlTDIIZIg62la1dSjZLunNGqhM81R6cOsguGcBBqH8daOXwNejAQM_3fQ7CxkpeS_EKTlYGUSl5BDGsJilRZofZiW4CqcBF62Av0ivzsornX7z0Cethv9VmJl8gvKoMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=Nn8IZ13XI8PSedAXA5JSggfDL5PNJPEOIXyy5JXO5IBmo8tS8z6eSCbbTthB9snU5f6SSHnMbZknNnuwnIfaap8OoIVFqlniZwr1XhW9SK1BBZv0wz5OcNji2cw8k6PbugGJqcjr00E8AeoM69Rn5nm0g4CntDNm6ORjSdL-LBk_34AmXUAV-JR1BAamrvjof1UzbEVG6qrcdFQ90Fq9pnzlTDIIZIg62la1dSjZLunNGqhM81R6cOsguGcBBqH8daOXwNejAQM_3fQ7CxkpeS_EKTlYGUSl5BDGsJilRZofZiW4CqcBF62Av0ivzsornX7z0Cethv9VmJl8gvKoMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=S7tIRAOunPGtloocSW2wFDa7WA01nSkjYYB7voEc0JoVb0uAAxDVYry3WA0S7V7ymJCw7GMwaUvRFanSapgDXDxo99Dc20eh3qyQJ-w99fEwCsy2eCT3iUT0tKO5IUZ9X66p0kZgtEV3c_V6Q018Vkucee7NChYKOhqFmZa5RcCauZkNyQHarj2PRT36SOUhUFiaanuL5zkMoOMUVZQa4oNmy6XV9PO8p-J4WtfG3Udl0yljTeEg7k0RGpV6yNMVIuOYWe75pklKSKCf28YizQ_HoEJucdGx7U2cRLad3j0LyhRHolD9Tloq0V79wd832LWY8eMAMqnKvXPWsvaOSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=S7tIRAOunPGtloocSW2wFDa7WA01nSkjYYB7voEc0JoVb0uAAxDVYry3WA0S7V7ymJCw7GMwaUvRFanSapgDXDxo99Dc20eh3qyQJ-w99fEwCsy2eCT3iUT0tKO5IUZ9X66p0kZgtEV3c_V6Q018Vkucee7NChYKOhqFmZa5RcCauZkNyQHarj2PRT36SOUhUFiaanuL5zkMoOMUVZQa4oNmy6XV9PO8p-J4WtfG3Udl0yljTeEg7k0RGpV6yNMVIuOYWe75pklKSKCf28YizQ_HoEJucdGx7U2cRLad3j0LyhRHolD9Tloq0V79wd832LWY8eMAMqnKvXPWsvaOSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A60cYHP-JZDG2RmRUsmiLTwsKS9EFnDwUu52iSb7_PpULeZPtZyurbdAhUcw0SZlCClKTl8kaCGhPCMn-onde-gPE706c0jfweUlIk8bqerefVWYRbH4srhyCOKkbY8FPm8gfjpDJqCaZVUvc_eBzrfzRAxpgMqy1Y5MZu6zN1KU8Q46MkBR8rNnz42xLeDl0gRv56ZsF3RGFIS0xdX0AtK3wPvpw0mxIegsd-pleefDhsUqDqQ2o0EilL3789fXAIeJCb9OT5k21OUm2JO8s6idScz_MXt4nQyUMC3xbfao6xHzKU5bGdLGy0bVMr57ipwO4EKdlXYufjWxzqf95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rp5sNnzWXEtDZlgsFLaC_vp-rym6-iNvhZKNR-4xVSwxsngzquH00ezHcJvyjmkCbOOfD4CfH4OlOUIbZJXC0h6WNn90lTP1lv8vqCCmIVON57hRaXubVqy2SeHMUEmGMkuVaZ0KqKlrOIInDbxcF20oU3Dsf-VRKeBt5rXNcfPnEn81Zfm312xMPpv0lwK17bmzGHkXwYWCotsDhJEthHB9JeG2z7SDuqtVUOL7wV9wWae36-NAEBMgiOoLHCAM-O0kirwn-L1C9mGdmKRuOzZi34KQKpR3oMquzWKiywLWFTVgy80e6gnLjKlOcGfxwShWl8sp0588p3pHSF49aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IS9qRAvH8NMu1vaGfK_nLwUbfmbBiMll3hQfEsoVYRWg4B8LnVduEr9KfA5eFG7ZK2HRrrR19gTxa9lpPxxSFlAd8clXyNYynAFXQC84QuRrA2Ck15r_P3hO8fm8gDmA-3fkLW7ke4NWfiwCyWU-M8FrKI-sHuDQKR4ZYWn6q9zMHq3Smb80d7shgd-_p07Xzj_EGgSMGcF29IoNKy2V_lK_VVJlGtHKFRZpr80BVh1jKZem3SG6kX_0dqL18-NFAgDxVHUO4lg3ideBKfo2R117w4fXm4kZTEutcVKd13lUU9zFeY4gcSf0sP9caUdeMsyKYfOPnISiiSr7SBZLyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست های دیشب ترامپِ بیکار تو تر‌وث‌سوشال
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64847" target="_blank">📅 09:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64846">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❤️
تلگرام از هوش‌مصنوعی و دستیار جدیدش با نام «@mira» رو نمایی کرد  امکانات رایگانش شامل چت متنی نامحدود، تبدیل ویس به متن، تبدیل متن به صدا، جستجو داخل اینترنت، تحلیل تصاویر، ساخت ریمایندر، لینک سوال ناشناس و حتی مدیریت والت شبکه TON روی تست‌نته. بخش پولی…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64846" target="_blank">📅 09:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64845">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
📰
وال استریت ژورنال: اسرائیل یک پایگاه مخفی در عراق ساخته بود که برای نیروهای ویژه، تیم‌های جست‌و‌جو و نجات به کار می‌رفت.  اسرائیل با اطلاع آمریکا، یک پایگاه نظامی مخفی در بیابان غربی عراق پیش از جنگ با ایران تأسیس کرد. این پایگاه توسط نیروهای ویژه اسرائیل…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXDE7eOwn86qoPNzcHi44CRi1TuaJi3QOasU74XF0hk48p1W6lD00i8smaEBkBMiAl7q4r5fRnaN-nnh7FB-z3MKtw_eDLW_cKESDwLU8UzzS18G3WuYjsH91PxsHNWoFxKK9KhH7H3YLnMhvXGIFblJ2Drfca9TdzNJdjd_B50I1BrCkJ7oySwtEGPPT9OoYrhsTCPsa167oEHDV90-rK5SMhLN9SN7uTo8mHoNwZx3HxRgUhrKnDKyaOFaQ4_AiSIB8FfASYEGQF_d05tA42zIYq_L_r3QRDvWhKPss_dJjVIcCNHhzy6d90t_iRgCA0hSMgsSoUMXZDDxRdxb4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64842">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه ماه از تبدیل بمباران زیرساخت های ایران به آتش‌بس دو هفته‌‌ای گذشت
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64842" target="_blank">📅 02:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64841">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=mS3kYuE0SFJF4LpxUXFvaaOXD2BUnaQtZa63LbWrJmLlf7sXwLy_9DDXrqI2CcEE16qvZWGKvo7jzdV5H1PWcNKf4Qxbokm94I2Hh0uPKGMRrwAjW2443cfZOUkPfaZvzBRUMowZ2WlKyA-9w6SmS8dkpiclsqqHLYUSsNmSDrZzO4TrR7XsyO_sWy-n0YmGg1ilYV9oxRMJZRN8jDGzoVs6e_2jq99kAEzdwbSk7KZ0F7wzT46kJEPKz2XtIlt_XCvvQ-t-47jwgzIqR1aw4iCjTghO0CF_nsJCgnkADh5fb86p1aJQOuAZnxjnQmEC0EqIYQa3xKEOwa7Q03h-9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=mS3kYuE0SFJF4LpxUXFvaaOXD2BUnaQtZa63LbWrJmLlf7sXwLy_9DDXrqI2CcEE16qvZWGKvo7jzdV5H1PWcNKf4Qxbokm94I2Hh0uPKGMRrwAjW2443cfZOUkPfaZvzBRUMowZ2WlKyA-9w6SmS8dkpiclsqqHLYUSsNmSDrZzO4TrR7XsyO_sWy-n0YmGg1ilYV9oxRMJZRN8jDGzoVs6e_2jq99kAEzdwbSk7KZ0F7wzT46kJEPKz2XtIlt_XCvvQ-t-47jwgzIqR1aw4iCjTghO0CF_nsJCgnkADh5fb86p1aJQOuAZnxjnQmEC0EqIYQa3xKEOwa7Q03h-9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس کمیسیون آموزش مجلس: برای آسیب دیدگان جنگ سهمیه کنکور در نظر گرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/64841" target="_blank">📅 02:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64840">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
مارکو روبیو وزیر امور خارجه آمریکا: ایران به توافق جواب رد داده است
👎
خبر بالا فیکه و روبیو چنین چیزی نگفته
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/64840" target="_blank">📅 00:30 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64839">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کشور عراق، تلگرام رو رفع فیلتر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64839" target="_blank">📅 17:21 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64838">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">‏ترامپ: ۹ جنگ را به پایان بردم و در زیر دهمی زائیدم
@News_Hut
#Fun</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64838" target="_blank">📅 16:56 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64837">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJD37oKu4NT3koSnpNKhNsFOgeKQxHOwMQqladBpejtRV25-CLdwVfKKhsWL-UM81WRiTxiLylLR9NTZr287gBC4rNMSeXJlmjj2Nx4EQAB8OPoPUvuO_qhDso2lF77t0DuQMWt3yY9zFk4ktSPKBbbJVKeX-axxLlnNTwH27KJHaUOvgpWg0TpkeyKHtG7uvPArnynFRCvrjlkKt2lBUNaVDxSgBrFBfNSYbuOA3mRpIfNS3tsaXRYY9QRC8NJIsLJn4cuJThveYI4PhJz9lJBUL4VNe_F6V_Ju8s4UBcW8KndJab_WPEJnLdOb9PVnohYM7goBs_8gGD4NxGoxTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#مهم
؛ این لکه نفتی اطراف خارک نشان می‌دهد جمهوری اسلامی به‌ناچار نفت استخراج شده را در حجم بالا، به دریا می‌ریزد!!!
اقدامی فاجعه بار برای اکوسیستم خلیج فارس
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/64837" target="_blank">📅 09:13 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64836">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b41db02.mp4?token=Y3XpJJVJlAS7zBboNQOZKC1aRrNTtNvVdFbtrkEJoDUX1uphvrRaPS76UGsKW4tmm9bXI7ErIUj634gMdQPrWHuR5C0uybnGVAs69Gj4ePOBSbF1UR9S0U48KbuW-ZULxHE0g-am7YujN2I6WCc_gYH8_dqRP5x0TDyN_1d8zQyV9sEYlx6LCUCa8dAlkqb63AIyqSF9klEq-tODv51cgWf1HkOTtx1Bw-Jj3673nN34QrnDnEcQQwaFQB8kJSEnZbNOI0hAuNsXJ5Cczo8tiibFBTm6W6tm1RbPHDKVahXDXqREBd9cUOBViocmxuHyCTWHyXVJO5kgkygc1jZMFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b41db02.mp4?token=Y3XpJJVJlAS7zBboNQOZKC1aRrNTtNvVdFbtrkEJoDUX1uphvrRaPS76UGsKW4tmm9bXI7ErIUj634gMdQPrWHuR5C0uybnGVAs69Gj4ePOBSbF1UR9S0U48KbuW-ZULxHE0g-am7YujN2I6WCc_gYH8_dqRP5x0TDyN_1d8zQyV9sEYlx6LCUCa8dAlkqb63AIyqSF9klEq-tODv51cgWf1HkOTtx1Bw-Jj3673nN34QrnDnEcQQwaFQB8kJSEnZbNOI0hAuNsXJ5Cczo8tiibFBTm6W6tm1RbPHDKVahXDXqREBd9cUOBViocmxuHyCTWHyXVJO5kgkygc1jZMFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آقای رئیس‌جمهور تقریباْ ۱۰ هفته از اصابت یک موشک به یک مدرسه در میناب می‌گذرد. چه کسی آن موشک را شلیک کرد؟
🇺🇸
ترامپ: این موضوع الان تحت بررسی است و ما به محض اینکه گزارش را دریافت کنیم آن را در اختیار شما قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64836" target="_blank">📅 09:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64835">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇺🇸
ترامپ: می‌خوام کل ماجرارو تموم کنم
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64835" target="_blank">📅 03:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64834">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
ترامپ: خواهیم دید چه می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/64834" target="_blank">📅 03:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64833">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مارکو روبیو: متأسفانه، تندروهایی که دیدگاهی آخرالزمانی نسبت به آینده دارند، در ایران قدرت نهایی را در دست دارند.  @News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/64833" target="_blank">📅 00:45 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64831">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HMpXzNViU94JYZd8iMvf9Y2-QKCRagxHe0fO0GQNqSxx2Pdl4cegtUUvrJXgh9OP7YgLkmJgqACsk4Qv3tFNHaj1aYO-TBv_Tp0jvxbOpesLcKO7dTz99thrQRqkEemrISTmjV6wdd0WCViyJmQiiFj_Ei0x6Jnk3LAEwMbbgfVjvLCnygeQyLbg9o2ib2AaXpCM7oHWk1ErvWOnYlcQG02qQfD1bNsViIsvC8e77ngK1kh4mmgrGv87Xy_amNhD47i2ISvqefH2Z8oaCCNasuP0JlOZxQ0KjTD21KqVtADLDbBLbAGfmvNJbyrOD1JvsZNT7CH_Fo_oQYT3veBHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K8Q4F-BI6BsrhF8Im2wGALEWocPluHx1EZ5HeuOazXlzIC5Rp5LMeC51Ar9xZUrQ8E2Wzjmm6XbYF70hE_5wj_BLJXTelvooytwBNQwQdrXHdMtWE8H2SzwBTpBex4EOZ5far1f-YOaY9ra8PNCJ1yomAunGVVozOpDUYmIiKGHr0Of4cXWVHYd04NSIbkbfLCp7O8z8qG0lOMFO0zKqfPWFBeD5-RY4S64EAjOrW6_Ist4tOX-zndGo_075FlQmhLTTPHFKPC7HeQl5yWu0pr_r33Qi2NlZc74A7wZCScueFz2-fpdwmJ69krLluTRbHlUGieb0y0eDflmvlSzb2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرستوی های صادراتی طرفدار حکومت کنار برج ایفل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64831" target="_blank">📅 00:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64828">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vXfjDYCDFrPNrWXG_YLjxgkfU8z9xmqI0s2fSYk-tKoPv-OF_wu2o3I0hiqGTGq6rs_1lNm6MWm3Z_oq9eb9iZHx8z8r227ze6E_0h6r7_4gG2zkC3JOPX3GVIpIPmhFvOmIbWuP9MN94Y9AKsxlrySi3x1nvkgPOVyZ7yAUyQVGzCYC9aOjCLKcnErp3YpHJGIPR7nlsVYfmOjWysP2EXPtAts8MaM3gPQlLEwE8TWHSUPAqDDGRLzPIJAfqXwQaG8cWfVt6jhE7lzvC1EupZER9KkrhYQVfuMdY-cVBb2oSSXiLj4TCr61SxM5aCQMrwdX5ZZa-lEX8MHszKQt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRGdnLiY1RJOnyKfjl1i_JHX-AIoBOwWDL-1DqiEzg01tdSXeIOAx2g5Eln-bwE8F1XPlotphQAhbUxY6dgGtjeni6IQ44Bu4uWz5G-TP91SocFsjxx4m0sLpar8Lp3xShuInCArx1IozeQvNGLWFEEKdGOBkJFzLr9FGNgLzp0GGetiXbXetN4_RccIYgeTOknrw5UnpGOly2A3BO1KBg7VdQvNqG3s0q5InSIkdTibDwYCz_qlTI-2C9QsWlqFQ0p3pfVmZbIkqsZ-fsn_R4ZHQRx08jpdBlMWKSba5nn5ER_IgXBJw0WqLZxGAVWsN_BUZOIwmqg8SDooLi6c1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فشار جنگ کم شه
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64828" target="_blank">📅 00:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64827">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=aNFmVUUJoI14piIIVR9YZVSnFkCo1GDLkolokp9VTN4eTaGcMCymzlsVnCuHC9Q1q-0BCPrCt7-4k8rTbcRlnw8WC1-A5TKTvjB4kca755vLIwVwqDlRp9DAo9Z989p-utdOyV0062r07pWLHu9Uhmq9vDs2vqUL1utREKpfamN64drNie8oIiYVujWE8q1MCQNmoOJ04faESNnYdWdSxcpUfEYYRhgPt8JkKVwsg37m9Th4_n3Oqq6VpTAjC5EEvd9KwcJ0wMV0a_5ZKmJvOzhuj__nA8xH2NM55ULOb8HlbwoKjLB5mUZAvmRU6icpYddRGPzX-g35OEZ23Rd7Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=aNFmVUUJoI14piIIVR9YZVSnFkCo1GDLkolokp9VTN4eTaGcMCymzlsVnCuHC9Q1q-0BCPrCt7-4k8rTbcRlnw8WC1-A5TKTvjB4kca755vLIwVwqDlRp9DAo9Z989p-utdOyV0062r07pWLHu9Uhmq9vDs2vqUL1utREKpfamN64drNie8oIiYVujWE8q1MCQNmoOJ04faESNnYdWdSxcpUfEYYRhgPt8JkKVwsg37m9Th4_n3Oqq6VpTAjC5EEvd9KwcJ0wMV0a_5ZKmJvOzhuj__nA8xH2NM55ULOb8HlbwoKjLB5mUZAvmRU6icpYddRGPzX-g35OEZ23Rd7Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مظاهر حسینی مسئول دفتر علی خامنه ایی درباره مجتبی خامنه‌ای:
خونه اقا مجتبی رو زدن ولی ایشون تو راه پله ها داشت میرفت طبقه بالا و فقط موج انفجار بهشون خورد و افتاد زمین.
فقط کشکک پاش و کمرش آسیب دیده که کمرش که خوب شده و یه خراشم پشت گوشش برداشته ولی الان خوب شده
مردم صبر کنید دشمن الان میخاد یه فیلم و عکس ازش بیرون بیاد که کارو تموم کنه به وقتش عاقا خودش میاد باهاتون حرف میزنه
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64827" target="_blank">📅 23:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64826">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNkGbLSLA8pA3pK0ZcgpKRGIGfOHqzRMm7ytjpZjA0Oozo1s-JY-uRrk41INM8AfCIVZVSx_236-KiltEpAqbqCF_1pi91IEti-GRXAcI1VmILkra1-cR2ysD4u_qOaSIYIAM2GbN0KJm2Yxb9o1GZd34n9hmW--B4gHzG5HE9y0-TabNCiwzudwHnTxOhwpEkJavaO0P82frsWYfmXBWG0eEVZnthpcKGMN0oG3lwWnJZ_MFeDONYKoQixCb8PB-YbJO9EWVfP5shTTK0w5hLrx7dqfcJAqub5-PqatJ7rqjHhFjV3yU6RMft8yPBHh-ICruvsaE3Gqo3QJ_G36Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ ۳ روز آتش‌بس بین روسیه و اوکراین اعلام کرد:
خوشحالم اعلام کنم که آتش‌بس سه روزه‌ای (۹، ۱۰ و ۱۱ مه) در جنگ بین روسیه و اوکراین برقرار خواهد شد. جشن در روسیه به مناسبت روز پیروزی است اما به همین ترتیب در اوکراین نیز، زیرا آن‌ها نیز بخش بزرگی از جنگ جهانی دوم بودند.
این آتش‌بس شامل تعلیق تمام فعالیت‌های نظامی و همچنین تبادل ۱۰۰۰ زندانی از هر کشور خواهد بود. این درخواست مستقیماً توسط من مطرح شده و از موافقت رئیس‌جمهور ولادیمیر پوتین و رئیس‌جمهور ولودیمیر زلنسکی بسیار قدردانی می‌کنم.
امیدوارم این آغاز پایان جنگی بسیار طولانی، مرگبار و سخت باشد. مذاکرات برای پایان دادن به این درگیری بزرگ، بزرگ‌ترین از زمان جنگ جهانی دوم، ادامه دارد و هر روز به هم نزدیک‌تر می‌شویم. از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64826" target="_blank">📅 23:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64825">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnjNNUZDWQvubP6JgyYbCzPEavm-1pI-E6E63dUBhS_FvY6RpPp_YdCB7La2SYQ16A8757xX5V26kb0RjksOeg5lP9RVDmdQEuVAww497eqgBB-AIq1CYGkM4GZ-UMWEqfp6yCTEmQ7TdcoxbOW6WNTeXnwLjvDgTeDMNtZrCimD4Gk3EV-qqf4paCg_OkndqZWNslBGhzBYqTHMLjiJUVVNyHIr-RhusEvauSrgEiFE34tjSAUs_i-UnajFreXG7R95_YY3tKkKGo0xa3N-mh8PUuGHFAnwaqQv7w7FcRtotdcImKkd4oOvpRXxNnjkp_UlIhiCcwhA63jP2O7Feg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ:
در مورد وعده من به شما، وزارت جنگ اولین دسته از پرونده‌های یوفو/یوآی پی را برای بررسی و مطالعه عمومی منتشر کرده است. در تلاش برای شفافیت کامل و حداکثری، افتخار داشتم که به دولت خود دستور دهم تا پرونده‌های دولتی مربوط به موجودات فضایی و حیات فرازمینی، پدیده‌های هوایی شناسایی‌نشده و اشیاء پروازی شناسایی‌نشده را شناسایی و ارائه دهد.
در حالی که دولت‌های قبلی در این موضوع و با این اسناد و ویدیوها شفاف نبوده‌اند، مردم می‌توانند خودشان تصمیم بگیرند که «دقیقاً چه خبر است؟» لذت ببرید و از آن لذت ببرید!
war.gov/UFO
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64825" target="_blank">📅 22:24 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64824">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
چندین تصویر افشا شده دولتی از اسناد بیگانه‌های فرازمینی، پدیده‌های هوایی ناشناس (UAP) و اشیاء پرنده‌ی ناشناس (UFO):</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64824" target="_blank">📅 22:19 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64822">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=LDXbZ_OvO9zSlbmEhQRHle2eM_Yrao0ESrkV0Qi9Sa9z24Uu1VOn6Ap3EyFYHAO3Yy8xdYxDCGw7Fhj7CBo-1JE_72m5qgPU7mKoPbbgqmODkmW3Ev_WQF5aE61wGG8hpIBuaTPBhrxqdK6-i1ACZ7fuxszRHJlb61bolhwRaYQ1xZmju0Sp8fwzWvnWGdz2GveWpaDMwfT8-Hkn3PkwnNKUU10WFsWwW7JQFXLhGWR9rOb6heGYN7Z08OBP2N1QXEjt7KHo-BBpUEUtL52X_6pUxwxNhlHNM5PJphfOhH9N2n0XLZ8J-eHzE4gQeYKAg-R_JkRf-n8bpbWO_wQQSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=LDXbZ_OvO9zSlbmEhQRHle2eM_Yrao0ESrkV0Qi9Sa9z24Uu1VOn6Ap3EyFYHAO3Yy8xdYxDCGw7Fhj7CBo-1JE_72m5qgPU7mKoPbbgqmODkmW3Ev_WQF5aE61wGG8hpIBuaTPBhrxqdK6-i1ACZ7fuxszRHJlb61bolhwRaYQ1xZmju0Sp8fwzWvnWGdz2GveWpaDMwfT8-Hkn3PkwnNKUU10WFsWwW7JQFXLhGWR9rOb6heGYN7Z08OBP2N1QXEjt7KHo-BBpUEUtL52X_6pUxwxNhlHNM5PJphfOhH9N2n0XLZ8J-eHzE4gQeYKAg-R_JkRf-n8bpbWO_wQQSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیو سنتکام از حمله نیرو دریایی آمریکا به دو نفتکش ایرانی M/T SEA STAR III و M/T Sevda که سعی داشتند از محاصره عبور کنند؛ این دو نفتکش پس ازحمله متوقف شدند.
این دو نفتکش تلاش می‌کردند در یک بندر ایرانی در خلیج عمان پهلو بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64822" target="_blank">📅 21:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64821">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
📰
فاکس نیوز به نقل از یک مسئول آمریکایی: ارتش آمریکا امروز به نفتکش‌های ایرانی که قصد شکستن محاصره را داشتند، حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64821" target="_blank">📅 16:50 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64820">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو: امروز پاسخ ایران را دریافت می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64820" target="_blank">📅 15:43 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64819">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcMB5Mp2Kb4_mHrXaTRObeFlG6s9NKs5zC44PLjIqcF-ITNqLLNikrK4yiTEgBmM6rzBRmev4_MTnpVwR36Q53HjZo4n3AmE9ACu8Yt_TMTKQ9skcv9B8ty3X3apyRsYUHSr8QHkjcl472q4mNwf7O8Ltzn81-j2z66gb09cRCm9-SmwRzsbiOLZGRQhuZ5tFochWnNe_2kd70wbDctZMx7uZxZzwMeWGpULoZrIB6VISeR5IFIqbLRbqVnl5NkomxjQCEh7UYs4xPH0Ot2XGBUQ7-_jcfq_DzAKpg-kSPLfr3uucix5KXaJSzbUmaqa34XzAaNwx8X8CXU1DbrT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات که نه، حتی اسرائیلو هم بزنن ترامپِ کاکولدزاده وارد جنگ نمی‌شه، چون سفر و دیدارش با اون کیری‌خانِ چینی براش مهم‌تره #hjAly‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64819" target="_blank">📅 15:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64818">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
وزارت دفاع امارات: مجددا ۲ موشک و ۳ پهپاد به سمت خاک ما شلیک شده  @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64818" target="_blank">📅 14:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64817">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
وزارت دفاع امارات: مجددا ۲ موشک و ۳ پهپاد به سمت خاک ما شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64817" target="_blank">📅 14:58 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64816">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">باورکردنی نیست آخوند ۷۰ روزه که مردم ایران رو از داشتن اینترنت محروم کرده، چقد شما حرومزاده‌این که دارین رکورد می‌زنید
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64816" target="_blank">📅 14:57 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64815">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=FmcR3nlZg12cPqg4QGrmL5j_Rwj4nRCdaFKxmRebman4b1DW4MctG5uOZ52vufZnYRnuTCsLt5V68RBofyRbhf6hm-N1XkoA-ccRSv-HSyLnLje7hiZdnYx7wuCiQXwlx46sMGztNtVRogEtqpqXRCYHcgMW1G8f55McFZbXSg7P2yTcrQmp879X2vdUzkViWL5MvemeV7KxIFiQ7D8wHMsWiC8pXumsz00QdQhA8fWp6WtO5_WZrGjnq92q6ZFi5HUyeVINxhZQO7KzA_7U5r_frHqC8T7PtRNDuj1MqKpStnre_V11TyqTxBmi3G7xjS8c89e6YL-wX5IYKj3XDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=FmcR3nlZg12cPqg4QGrmL5j_Rwj4nRCdaFKxmRebman4b1DW4MctG5uOZ52vufZnYRnuTCsLt5V68RBofyRbhf6hm-N1XkoA-ccRSv-HSyLnLje7hiZdnYx7wuCiQXwlx46sMGztNtVRogEtqpqXRCYHcgMW1G8f55McFZbXSg7P2yTcrQmp879X2vdUzkViWL5MvemeV7KxIFiQ7D8wHMsWiC8pXumsz00QdQhA8fWp6WtO5_WZrGjnq92q6ZFi5HUyeVINxhZQO7KzA_7U5r_frHqC8T7PtRNDuj1MqKpStnre_V11TyqTxBmi3G7xjS8c89e6YL-wX5IYKj3XDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دلیل اینکه عملیات “پروژه آزادی” را متوقف کردم این بود که رهبری بسیار خوب پاکستان و رهبرانش و فرمانده فیلد مارشال و نخست‌وزیر در این موضوع خیلی عالی عمل کردند.
آن‌ها از ما خواستند که در زمان مذاکرات این کار را انجام ندهیم.
اما اگر لازم باشد، دوباره به آن برمی‌گردیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/64815" target="_blank">📅 09:14 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64814">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64814" target="_blank">📅 05:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64813">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇺🇸
ترامپ: ممکنه هرلحظه توافق بشه، ممکنه هم نشه  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64813" target="_blank">📅 04:53 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64812">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇺🇸
ترامپ: ممکنه هرلحظه توافق بشه، ممکنه هم نشه
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64812" target="_blank">📅 04:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64811">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">چالم کنید جاکشا.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64811" target="_blank">📅 03:03 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64810">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D__uNGKQbX-yNXzbw0O-4ZvBcA26c10Up-wPGRW97q2uu8jaW9yaE-MQtOy227tPNH60mRfveGB_eOSzpwK6_3ylPXJ669GUMvWFsdR9DO-q5IMBWxEohl4q6cSQKDTZ_OJwxL8Ir5cWO57kYO_XJ3GL-JwQcJg5rBqcifYBQvHJmRdyyG0iYpdVERYlz2Z9RM5VLJQqjPOH29KnPrNvrzI6VyF0eRbKjskaUlR7W0RjqzgZ74LBdyU-lhKLQOQQiNnvvzsxlMZpPvsbQeJuZCz3M_VClvv5a6wY2kqhlVwviGfKihJPzzs7TmUvjtAt-aitDR_3hMlhy2OvKk64UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
سه ناوشکن جهانی آمریکایی با موفقیت کامل از تنگه هرمز عبور کردند، در حالی که زیر آتش دشمن بودند. هیچ آسیبی به این سه ناوشکن وارد نشد، اما آسیب بزرگی به مهاجمان ایرانی زده شد.
آن‌ها کاملاً منهدم شدند، همراه با تعداد زیادی قایق کوچک که برای جایگزینی نیروی دریایی کاملاً از پای درآمده ایران استفاده می‌شوند. این قایق‌ها سریع و مؤثر به قعر دریا فرستاده شدند.
موشک‌هایی به سمت ناوشکن‌های ما شلیک شد که به‌راحتی سرنگون گشتند. همچنین پهپادهایی آمدند که در هوا سوختند. آن‌ها بسیار زیبا به سمت اقیانوس سقوط کردند، درست مانند پروانه‌ای که به سمت قبرش فرومی‌رود!
یک کشور عادی اجازه می‌داد این ناوشکن‌ها عبور کنند، اما ایران یک کشور عادی نیست. آن‌ها توسط دیوانگان رهبری می‌شوند، و اگر فرصت استفاده از سلاح هسته‌ای را داشته باشند، بدون تردید این کار را می‌کنند — اما هرگز آن فرصت را نخواهند یافت و همان‌طور که امروز دوباره آن‌ها را از پا درآوردیم، در آینده خیلی سخت‌تر و خیلی شدیدتر آن‌ها را از پا درخواهیم آورد، اگر قرارداد خود را سریع امضا نکنند! سه ناوشکن ما، با خدمه فوق‌العاده خود، اکنون به محاصره دریایی ما خواهند پیوست، که واقعاً یک «دیوار فولادی» است.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/64810" target="_blank">📅 02:28 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64809">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/p1KgTTThi03nH5VmDUcYpxDcc7EChibwijjoGZwqd-igAUyx1i2pAxfQjI1LIXXdw_MmJnoN6jZpoQKdbXXEF0TV2fzw3Ke9rnWalXl7mw5k99GRS-DIfiwjBpUUj0UMoUQ4jxSXSiWKobl3AL1OWMlbmNuAbUFvslGYybC9wsV37QxGpeYzX0tBKS5qkx9icCxyDZ2DaxhhiwXv5Y_X34h6xjDJCY1wmwUsmHctRJzj7q8TwzI2qw-sa8jo9SuaDZmKBgn2mJ8zRJGdNoD8mJmOuYxm9gIWRvP-GSwk417ZPG9RQ5rOH8xT9QY-QpJgAXgaHbVgK3oc9YxYjfWYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی خلاصه: چند تا ناوی که تو عملیات آزادسازی از تنگه رد شده بودن؛ خواستن برگردن سمت موقعیت قبلیشون که سپاه بهشون شلیک کرده، بلافاصله نیرو های آمریکایی تاسیسات محلِ شلیک رو بمباران کرده و ناو ها هم بدون مشکل رد شدن و قضیه تموم شده!  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64809" target="_blank">📅 01:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64808">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64808" target="_blank">📅 01:45 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64807">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🇺🇸
#فوری؛ سنتکام:  نیروهای آمریکایی حملات بی‌دلیل ایران را رهگیری کردند و با حملات دفاع از خود به آن پاسخ دادند، زیرا ناوشکن‌های موشک‌انداز نیروی دریایی ایالات متحده در 7 مه از تنگه هرمز به خلیج عمان عبور کردند. نیروهای ایرانی چندین موشک، پهپاد و قایق کوچک…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64807" target="_blank">📅 01:44 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64806">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64806" target="_blank">📅 01:39 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64805">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0SayAeDDqlBHcLun_fs0w9CryGx7jNBUXgogKC0m13BUtW7O6PqKHE5N_tMlLhHi94fNK12AsWCyQgPKXD_QLWp0ra0gL4kk_K-esPT4MkRJKM-VKu8ne1DDi_G6hlFkzuJfgJD9BN3z7ugyribBYKzRUw60yis8fi9VRFjWH3VxNcMLGY1fVibwgsZkck8y3r6nOz7SJJpyz9N8oMW37NP8XuswNNr-vmgcCflhwZbZqtWDin5Un08_3DA18Jsvk_bG_IZ7y8YQzD-PJOq74z4kTGtVj9iwPWm3fqnyt3-JnbZYfIua3YGw-QOkU_mU91BXn6maXUGTR1gzCxExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیماهای جنگنده زیادی مدتی پیش از بریتانیا خارج شدند
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64805" target="_blank">📅 01:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64803">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKVN SUPPORT</strong></div>
<div class="tg-text">🔴
ما هرکسیو تضمین نمیکنیم اما تیم کاویانی واقعا کارشون خوبه و دارن کل فیلترشکن ادمینای مارو ساپورت میکنن
❗️
پشتیبانی 24 ساعته
📱
OpenVPN (Starlink)
💵
5 گیگ: 2.300
💵
10 گیگ: 4.300
🔐
V2ray
💵
5 گیگ: 1.600
💵
10 گیگ: 2.800
برای خرید بهشون پیام بدین
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64803" target="_blank">📅 01:27 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64802">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VLv2iE4yJS7X0NsbM2bZAlJGuQpU2EiDjO4id-8v4oVPgaofo82jDaybmJQDfpp-GOmZlpWCCs42hMkwvX6fzO_D6CT9s_welqHeAkYs5NlJKLfBbc3IlFPjIP2ikl3GA7Q5sUFWq55_7IiZzv4nK8NjLbnsXOgdcZGd6GJ8zKkahtwlpwIKwxRHNaxxTiJdWMhjD2DNl7yDz76ctfbtR567bVSwMpzBwWwB4QTBBnHeWWqYYCQsMDVsNjGXBSW4YtP-Gkds1dHK8A9qALNgQ9I1dRAd2Daq4jiorgVImqAi1oeS6XIKXrjMR_RjzC2E1G3QznKRfVupwA_fNXLWPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
#فوری
؛ سنتکام:
نیروهای آمریکایی حملات بی‌دلیل ایران را رهگیری کردند و با حملات دفاع از خود به آن پاسخ دادند، زیرا ناوشکن‌های موشک‌انداز نیروی دریایی ایالات متحده در 7 مه از تنگه هرمز به خلیج عمان عبور کردند.
نیروهای ایرانی چندین موشک، پهپاد و قایق کوچک را در حالی که ناوهای USS Truxtun (DDG 103)، USS Rafael Peralta (DDG 115) و USS Mason (DDG 87) از گذرگاه دریایی بین‌المللی عبور می‌کردند، شلیک کردند. هیچ یک از دارایی‌های ایالات متحده مورد اصابت قرار نگرفت.
فرماندهی مرکزی ایالات متحده (CENTCOM) تهدیدات ورودی را از بین برد و تأسیسات نظامی ایران را که مسئول حمله به نیروهای آمریکایی بودند، از جمله سایت‌های پرتاب موشک و پهپاد؛ مکان‌های فرماندهی و کنترل؛ و گره‌های اطلاعاتی، نظارتی و شناسایی، هدف قرار داد.
سنتکام به دنبال تشدید تنش نیست، اما همچنان در موقعیت خود مستقر و آماده محافظت از نیروهای آمریکایی است
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64802" target="_blank">📅 01:13 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64801">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🇮🇱
#فوری؛ کانال ۱۴ اسرائیل: ایران اعلام کرد آتش‌بس نقض شده است!  @HutNewsPlus</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64801" target="_blank">📅 01:06 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64800">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حوصلمون سر رفته، کاش وحیدی چن تا بالستیک سمت برج خلیفه هوا کنه
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/64800" target="_blank">📅 00:57 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64799">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">به همون اندازه‌ای که پوتین تو جنگ ۱۲ روزه نقش ایفا کرد، الان چین نقش موثر رو داره  وضعیت طوری شده که اگه وحیدی به ملانیا هم تجاوز کنه ترامپ میاد میگه نه عادیه این چیزا پیش میاد #hjAly‌</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64799" target="_blank">📅 00:52 · 18 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
