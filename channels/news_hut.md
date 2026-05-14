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
<img src="https://cdn4.telesco.pe/file/W7OXpp_XK8V_zTcTsVV9tessjLYI-OuuypJ4_5czJEQZCyjFf7MR0s4ukZFJthJ-j3D0HUvhN0DX-m0oPs1ameYkSN0DF1yZtTzAgZKzrZEa7sXk3Ge6QoJywCkLqH6ZH-SyDLO8yKIuThSHV5doLe1gjJpMT-kSWzHN0vspa1_qrgCnhUkxxptlDqsWJ225pTTASatr14Cwwh05y9jWgi_DDogruNx67VLtNp1y6iFNxl_aEFvJT5wBXadkcLPWRRkm1NE93k6xT8efzojwbKJYjNqoNjOe4JY-DM6-cg_BFNe2a7Ugi91hXq1S_qMcY_uOV9RnIlZKxYFvQffMbg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 146K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 01:33:15</div>
<hr>

<div class="tg-post" id="msg-64912">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVPHReCSyIWk9Z7ACn6d0L0_UR4ptMHq1lx348bNwybq-PFY8GERbcSqewBLqQliwl97F4dHBi_kQkyxO4wWRCzunScdvA1gULVpdXvT4nAOG5T8lDseH3SuLTUmKj73jM9xcpHofipXsKRoWIwP8fsO1XulP4hsbM9KZtGTSoBt693PV04wHp9bB27UaM_n13QrljBQq12nSGCIfi57rUV5ApTSfTkkBOOvwh8hzoP9pHTml3Y-sbZu5Pe9r5ZqJbJIofHhMj02qwzs8iR-ZCzya32Z16CgonnCcJ_HWB5HXF0_DWXOPdURAlKMScgPSA_2wycG9gMUr9Rqxzx3xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسایی؛ نماینده‌ی مجلس:
دولت قصد داره میزان سهمیه ماهانه بنزین ۱۵۰۰ تومنی و ۳۰۰۰ تومنی رو کاهش بده و قیمت بنزین ۵۰۰۰ تومنی رو هم به ۲۰۰۰۰ تومن برسونه.
@News_Hut</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/news_hut/64912" target="_blank">📅 19:59 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/64911" target="_blank">📅 13:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64910">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNteQoq6g6rfefkr5xXhhIMNPPgddpBMHjun_fTPe0dnJdj0GZXe_jqZ7D13-AZAnHW628FtV8i7qfB6WkHQzTv-jYwPE3d0xTl0wEK3h_RfqeVFPgpq9HO5YB3N5olI7Z7oepcg_9CC8ijFNiv-1OZ0hS5i4MTA_L16JvTz-KIzX3HG4uUjaX5ks4_ajSxXWZwOp3KEIlqgA48yWakEF0l5Y5HNNBO5Zxz3cgh4dmjN79zvtxJ1PCKCK3yamQmW3E94mgbboAiBiV1m-oAJMfSjO_Af0m0tzgrxFd7ZZjz9fksnaPn8Gm9eUm_rowMgIZ3Tzqns3Qqmzu0CWxpcwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/64910" target="_blank">📅 02:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64909">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">خسته‌ایم و کم‌رمق
😂
#hjAly</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/64909" target="_blank">📅 02:33 · 24 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64908" target="_blank">📅 23:04 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64904" target="_blank">📅 10:14 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64902">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b7TDhxZfCVTGxLUUz4d3zVS1qn5W2lQOJZa5oaevOr5wHjcmxzm6QRltEe7qbgfcGp7CTcttcgzTqYNBA01PWLgL1x_8Zx7rHstHiYyux6agChqdCQUkQcy3ZU51jkrluMFDJYTemWZBoO7JJFrvwtznB9XbC_vywG5wk6gOdjPKFsVjWfAZugmY2EchNpBJU7omwokCELaQRjvdedYIh6Tl2LDn_pqd6oA4aSGszOFeP5eKPUYAHLXllLovD5IQu9GXsqXf46upk1iUgfj2PXmV9MZPD8oLbInwSqSO2wQQPDiXhhkFJmWqjP2EZXz_JkPHT0lwXoUaxXiUoQ-yXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k_QBeserCzHPfpyIeVAw-T77UXwNNfpa8LbZcpYUeQwUNpuc-h_4KpVU4wDxvldVZZe9J60h0TveV11K7uQmWpO24aaQ9eUwdH3sr5uMcdUlJX53TBQm7zOO8Nstha09xEK2lPKnIyO8ucKQdNBy-agbSXwDpAC_rl3REb8edji49XT1EpNFX6jKALtr_wNO3NFH2NdGveOPnK-bcDdg0bvZj9UfvAz2vTP5iRJL0l4B3kDqkFED_RlNa-0gQYmvEI0lUkYkkxfbyTTPGSwQz4NttOhyOsEDkiuANjxJbzAi618HNlGFBDesaS9Etme55P50342gFwMAPUiER10hRQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با اعلام خبرگزاری قوه اعدامیه با اذان صبح امروز حکم اعدام «احسان افراشته» به اتهام جاسوسی اجرا شد!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64902" target="_blank">📅 09:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64901">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
📰
خبرگزاری NBCNEWS: پنتاگون در حال بررسی تغییر نام جنگ ایران به «sledgehammer» به معنی«چکش سنگین» در صورت شکست آتش‌بس است.  یک مقام کاخ سفید به شبکه خبری ان‌بی‌سی گفت هرگونه عملیات نظامی جدید علیه ایران تحت نام و عملیات جدیدی رخ خواهد داد. بحث‌ها در مورد جایگزینی…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/64901" target="_blank">📅 09:05 · 23 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64899" target="_blank">📅 04:09 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64898">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ihBlVhBVkw-RGItMFrbVx2Cw6e2uXTKJO0YUyRKyS3TfoajhQ6ifZ7qpfqWe-B4Ex1s8xb3eBYEJW0Vng6XNcq0p7STwcwoCLgwYHhxm-iP6ktw1O0EvW_clqp_SJODj2NAB2YiajmBSdJzcj7BrBeC6z4WVOBLpg6pJ-ET7_4zsDgI7AMmf8rpMHBV1IkcVJd8bh4kIEOKGpdqA5OUbJCe3lRAQ1t8TB9N-50l33na3G68e9w7fFrmVR_6kJmp7SpWZitIP3LXm3i71qBDwCXrN1Ib9auIm_o7BsK1rTnkifI3wQp3wU8keNwcL8oYKL_6rFYtvSiyKJi50LfY_LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64898" target="_blank">📅 03:03 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64897">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">باز تهران یه چص‌زلزله اومد، منتظر باشید طهلیلگرا ربطش بدن به آزمایش هسته‌ای
🤯
#hjAly</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64897" target="_blank">📅 00:21 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64896">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kEUIUqGhVmSKtgZkvRJaxBhzoTrZgbCqkMj7xrGDiAOQQkCptEnUbmz6Ppjr0AbzO7f_rxhd0-gI2rnBhePegdEIGElSMHgTNCDfzwxgt3XNzWp9q5-8EqcAMjEh6HfGGyaxwzsLnEIU5kBXpAm194SnCO3LBCteyEMl2zhAJdm2XSnV-PwSclNUtkfa_mjNihn0w8pcgt9jweUB5oKfI2QW3hFzfh0JlVD_crDtvtF4tSWMQ_YeY051r19vHGFXhCLzriTcsqa7xXzJGw_jBPywDBQ2QqdMMT6MQxoFOOOWk3CAmgYLfpWF7gGL7U8SBo65JST7X4HM4nrLrO0Mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ قراره یه اکیپ کلفت از رئیس شرکت‌های بزرگ امریکایی رو با خودش به چین ببره  رئیس شرکت بلک راک رئیس شرکت گلدمن رئیس شرکت مسترکارت رئیس شرکت سیسکو رئیس شرکت متا رئیس شرکت ویزا رئیس شرکت اپل رئیس شرکت تسلا (ایلان ماسک)  @News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/64896" target="_blank">📅 20:28 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64895" target="_blank">📅 19:13 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64893">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bE08i1kp2lOelcU4SXPjN4uco1ScimhwZSPoQJdTa6gYz4GW1RetuxlaQ8TkKpozSAsSrgbBCUDcmmNqlbnpr0NBHen3K8V2m1xx6UUbEhRxBkozL3wONuRs-H0Yyzd4C45nQ2WjfIbF0XJqIyUbKogOHZvU-Mpu_2RiHjrzmyoHxLmW0P_FzUp_k-1B4YrpyAeqY4AwSf3r4MWYouUpTyDmyFYaRBkU5-UD4vrHE-7yal6ZseTxzMCioiA4rSApfF3MTimhusVWv-iXbQtfSG9HDvBS-92q8TRsF2bzmNUblqPOF2CvSt9yDaxazbqTzrm-PI4jyMnlOGFkPkg-nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KY47M2weuFwLaKJVJiYzmtPWVRpWcCnBz0xzIKBsRg6PR7cSXOx08Q2IECTkIVrXc8hJgQttZf43eu9XPJ1NRR1CLSgf9el-wEQShuY3qimAd6PvsCGMEM3588Fche3ypz9FkSs4ueGrytN0Y1SDJcOTEllBNKhSTBqXUEveM9J3osTTwDrFFUgfbDuQlHGjOAzXsrkh45prR5qAPIlmAJvdQq14iyTStORtf6py6FcozP5p677li82xxgpDGjreCPl0qMI_RSkHGviiWUsFJq8pZrQBlLPPfUM1FBpc1f8ncLpSQ7htG3vt7bO8679xBIAx1NO-NnkMMDA6iQAKwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...  جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن #hjAly</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64893" target="_blank">📅 17:50 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64892">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPF-1Bly__OLercWiTXTHdX8kCDhBFZU07Mqz_ksWXkktUMM-ua7C40zuMRMwdSutM4UevfbFKXpGmmJZDPDbgmT_7Kgj19ulCykXdjM_nrlKb3NULE4RIAqJzrENPi-1OBb7Fzu8Rg-4jSczgpgJIYV3DmSqMnb9zhgSgrDQFDrn2xGsp5_QU9cEHLz58-ivn8iQxu1m6wAfx5y2HB5t-3LpU46QhTcPo0iGVUYVAFH8BaCEEttF2emeDu4mnRNrvyUCit0BNwpk_Q4n8zn7KKBW-m8cLNYuLdIza9As0G07EZwiOC-9ZMDkYivOYRdEBVQLm8gKUVXUHM6tIBXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من هیچ جانوری رو ندیده بودم که آرزوی مرگ یک نوزاد رو بکنه...
جمهوری اسلامی حکومت بی‌ناموسا و حرومزاده‌هاست، اگه حتی جایی یک درصد با اینا همنظر بودی، به انسان بودنت شک کن
#hjAly</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64892" target="_blank">📅 14:04 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/64891" target="_blank">📅 09:38 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64890" target="_blank">📅 09:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64889">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
📰
خبرگزاری والا اسرائیل: هفته پیش ایالات متحده نزدیک بود حملات به ایران را از سر بگیرد؛  اما پس از آنکه مشاوران نزدیک ترامپ به او توصیه کردند که قبل از تشدید نظامی، یک تلاش نهایی برای مذاکرات را مجاز کند، تصمیم به تعویق افتاد. ﻿ @HutNewsPlus</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64889" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64888">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kc2LpyLaguGV-1CJ4Ce2QItIdYQ98UqbP8LoJUYfd-5T-IufyYe_iA6Wg3cIyyr7UlQQYymsaRlajcxaTKzlaKHYj7Nm-3VQkHtQrTdMH5gJwUJni80QkTqWbmchfBqtjfG9BSCgKtWNzgDRQ2l_5QZiEsHBXhsR3xN6wC6mGCjrBo5HXukq1rRNHy_hr6cU09nq684KWDN13LQOdYaoHlxn5C9-Hcnsc9od92duJ6LY6ZR675x3SK84PFY-AE851ug-F46UTR_O3PpQMxkQCJXWojKAfcpmNHUZ3Wu_4xvq4OuliXlrXgUlKHAV2BGhr2KRTKJ46SljybmgcV02OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ: من بسیار مشتاق سفرم به چین هستم، کشوری شگفت‌انگیز، با رهبری، رئیس‌جمهور شی، که مورد احترام همه است. اتفاقات بزرگی برای هر دو کشور خواهد افتاد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64888" target="_blank">📅 03:38 · 22 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64887" target="_blank">📅 01:07 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64886">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.  @News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/64886" target="_blank">📅 22:52 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/news_hut/64885" target="_blank">📅 22:21 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64884" target="_blank">📅 20:56 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64883">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری؛ ترامپ: آتش‌بس داره می‌میره، بهش اکسیژن وصل کردیم تا زنده بمونه، یک درصد ممکنه زنده بمونه!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64883" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/64882" target="_blank">📅 19:16 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64881">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
ترامپ: کُرد ها سلاح‌ها رو برداشتند، مردم ایران بی‌سلاح هستند
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/64881" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64880">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا گفتن بیاین اورانیوم رو بیرون بیارید چون ما نمی‌تونیم، فقط شما و چین می‌تونید!
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64880" target="_blank">📅 19:11 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64879">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تا مرز رسیدن به تفکر اوباما</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/64879" target="_blank">📅 19:10 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64878">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">حالا ترامپ با یک نیروی معجزه‌آسای تاریخی بنام #محاصره‌_دریایی به دنبال حداکثرِحداکثرِحداکثرهاست!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/64878" target="_blank">📅 19:09 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64877">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
ترامپ: آخرش رهبرای تندرو ایران رو تسلیم می‌کنیم  @News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64877" target="_blank">📅 18:49 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64876">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم  @News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/64876" target="_blank">📅 18:48 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64875">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
ترامپ: ایرانیا بهمون گفتن بیاین اورانیوم های مدفون شده رو خودتون بردارین، چون ما فناوریش استخراجش رو نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/64875" target="_blank">📅 18:47 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64874">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyaux03V2KBczp2QcLYK1KOHWzyrmD8dobkLGhsvhrqdrhdbfxz9QA08gXUE7E2VoQ7BtFbCFUu3EYTbjkD11B0vuUxehlKw_-PZUzs7A4d0SdOByff5zgwllwo5uYMo6NQC7VZvOEQE0m4y7DnukVAkTsfy5a_GGhjThRpT5gup7GxikSoFaJ697g0bP_kClsLujGUaSuTspUgcUHwzUyyqUZ1vU-BIbHYVRw36PXj8n-fQqc8Y4NmyEfT-kKO-jtH-9h-cNl_ydS8PRXZGvXvFzGkYmlscceAbgkVWu5hKmNnh9AT8NEI6pEx6g3oW8au1RpMlTBaY_HNMg2EBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی بعد از اذان صبح امروز، عرفان شکورزاده، نخبه‌ی هوافضای کشور را اعدام کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64874" target="_blank">📅 11:03 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64872" target="_blank">📅 09:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64871">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2_uR-dDW5yBDs0NWevSdFIsREkEs1jTtPwnvIZ--mMIIDhUd8kkrOaNofXJst0TwAdkbS_um1uRNj-lmW0MVEpG5VW4pg5xKe4ZaXsbdxJvK9Xt3U-mDvSQQhPW-QmJyQZ2XaYb6sE-3ZQXfkvADa-mpP446XGGxNSDKeih6ZDE7s0Z35cnOmCLLiDcnQfvf_BFgEeFztrGD3gKy6QNfJOH2gVCXon9lC3miAM1hLdV6W6Fh4qCMG-uIF27rDmAz_5NQP-ICijK5kbk3GdSe2PFrc21xyH8QWgqfFoehPgRYuWkXiRuzI2A2YgpFpu58B1HxmE6Z8UhCY_7fL-fRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇳
🇺🇸
سخنگوی وزارت خارجه چین: ترامپ از چارشنبه ۱۳می تا جمعه ۱۵می (۲۳ تا ۲۵ اردیبهشت) میاد چین.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/64871" target="_blank">📅 08:04 · 21 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64869" target="_blank">📅 05:53 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64868">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یک ماه و سه روز از ورودمون به چرخه‌ی سیرک‌وارِ مذاکراتی گذشت، و این چرخه مطمئنا تا روز دیدار ترامپ و شی ادامه داره [اولین رویداد مشخص شده در تصویر]، و بعد از این دیدار بهترین زمان برای آمریکا جهت آغاز مجدد درگیری ها به حساب میاد   #hjAly</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/64868" target="_blank">📅 02:38 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64867">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IE3Bjym9jvpl-frNAix6uUBiFVmbK-hPQ7OMUQYXtdUyKjQB3VCfHGEj3XmgewfJ9ywEsGzlvg8DDJXFZ1Go3nROM-gU8n8IaMJDOMAG354hgwAmxdzQXqoelxCIuqu9l1Dp69wrdcWSVXdCNeGtud_saDV1q1a9IGKOXz_CPUCBWCAnR-cPKCo72Kqg77-J-dy1nkI_jG7RnphMfXptzqKjIehiNyoBLSUJ5Dw4TToOhj71Ftb2vkUStgdITXC-yf51OlcpTLJ12CGS0-eoOuHUJ_5Uf0Jq2dwxuGfEj57SqaGKYxL4VysW22hAiSfaAUR34UTSQP5aCxza1UqC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظر می‌رسه تکلیف خیلی از مسائلِ کشور در دیدار آخر هفته بین ترامپ و شی مشخص می‌شه  البته که در همین حالِ‌حاضر، احتمال از سرگیری جنگ خیلی از بیشتر از موفقیتِ مذاکراته، آمریکا بعد از خارج کردن اورانیوم های ونزوئلا، هدفش دقیقا انجام همین فرایند در ایرانه و با…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64867" target="_blank">📅 02:18 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64866">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UQxpguVL2fhD2WCwd9yfPzRuxUNIHKaRnwUKyAtDvgmvYI8PmTzsARPUJxOEVPr9arwEFLyZeApInsD3-r1pPtlZWxGnVAaYM4mx1LZ93dJh_l6yog8Yi8c-G86Zju61iyIGoNLk5MnfKIHEh7CIStASZlplaacYypWbIr6lZS7gI0oWQznoZrv6EtidZLcQakaj7aCSnmvFsjVLnkuTGI04dmaVszP7I8wULucHa4nivcI30okEjUPIte8o6jn1D5AtQA4q4p3w91mZJ9quHkIahDH9QOWAZ7Jallv_Ny-tVaPWFaID2tSU_oUqvQxSMdYN4WCWTt9VQ62H00ooEA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/news_hut/64866" target="_blank">📅 02:12 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64865">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYtyVkb3JZZRgZ2R-ShZLxBeYrmQrYSA6Of40TD1Ovq1f2oBPzqPQfZIta33t31Bf5W4KrNEkoT8-Y0rdRUTpZS4xx1F-QrDwwAWPh8XT4ELC_-ghFFvc4q_miAoDTDVukyiQJD3N131sOKT5-vUxseIthdvLnHmSg73UJYBxhADa-2ym2z2fp6GToXNyE1DJFbpYNRDWfVyzjB-ulI_9Wxuy_fHxxeenvhY6KrAXzebjuW7xy5yBBLlr5Zc2fXZ0E7mf0G5_AdZ8S712p_rWg2vBT44tkty-2OKt1twB9-2JC0-wpM5vaiBUzxs8Ny0XbBqyZaPwk5c4TP6zNS1pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به دو رویداد مهم نزدیک می‌شیم  ۱.اولین‌دیدار ترامپ در دوره‌ی جدید ریاست جمهوری خود با رئیس جمهور چین ۲‌.آغاز جام جهانی ۲۰۲۶  می‌شه گفت عملیات آزادی که ترامپ استارتش رو زد بخاطر دیدارش با رئیس جمهور چینه و می‌خواد حداقل وضعیت تنگه رو از این آشفتگی در…</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/64865" target="_blank">📅 02:08 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64864">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇺🇸
؛ ترامپ: از پاسخ ایران راضی نیستم   @News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/64864" target="_blank">📅 23:57 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64863">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">خبرگزاری فارس: مولوی عبدالحمید همکارِ نتانیاهو و ترامپه!
@News_hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/64863" target="_blank">📅 23:54 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64862">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhGmQdgtOBBfFplMPyofDsC8GeteoLq5pMZRzYhY9B5uYWGT4Ge2cBHCgSZKSE7esZA7ILOesHyS4xIyC3KPQpiBtX5S-FQE5To1QOjDt27ytLb1ZFO-W1mf52KVbcgVR41ENcQxRzBI01hKVck1KNkTniZ5JHkr0FzNnmOuWXoGpaN32xjcM7eTBq6Q5lEJmGOsdQW_heOaSyV0f4-QpMefgrpjA7G1xi2TVHlKFJaICVRqJ2yuBRFAh55Ko7YjjqkBDMX3MKKd2TByK90G7cZRue3l52hnpPl7ihRNtNTlgebOcpX1qcbfpJ6i9MsvdoEKk0y_1yjRqmvZXKKiPg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/64861" target="_blank">📅 22:35 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64859" target="_blank">📅 21:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64858">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxtKlVnAYbraE2RIk-BUNH2OwMAFTz3ItwsSPJ32qvPk5zFE-veKxvLK365va4etblg4T0wj2sf6iGDlP0_5KcWRNlwGIOQWX_8iPsJxt6bMu56G-3HhBCQIAnI99yMXMZGojXxPnLXXuan0CKOW_ixAhEq8AQH4IJ5riQiREIOwCh0sYmubzytpFjfr_DuNfXyLWS1QvFgRErZTectp1YXQxwtlC8R-r-GJYOtc6eOBQF1-Y7EOA-yF12LGbQrWWDxk2J-_7wj5uu2Iv3wn2mXjozIIiv3gYy_Tu70-KYimYynpeeUv37jitmhV0QQ9TLWBfh-aLgsuPX0zY4ENZA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/64856" target="_blank">📅 20:35 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64855">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAriya</strong></div>
<div class="tg-text">احتمال حقیقت پیدا کردن پست آخرت از تو رابطه رفتن من بیشتره</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64855" target="_blank">📅 20:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64854">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFbkr3RpvVGfuALRnhF7OyzrPvbe2jWbWwB8gVHbpg0gdnEhxTBsd8yEI07o3kqvsVS-qv-ETiztqWCeeTT0IZcnffSbFySsY7aacvqissXANUl_MD_JZI76MyNmnN2KJ1WurWpnfgBz8CBRIektsfPnAYjEQm6BLW_QStu3ct4LhIAKVx7RMsJ-02sZs3AFRNzkmwSzm2QZ5QBkCcHmwbYeau9y32eQRmnt2wwfNg0iPXDXeMUA3OzrPoJZMYITxci28CNoUjtFfXat-yAZPudhoKJNGSMMebNrgclHYmDThqx1kBdoRq4hoxYnitEfhjdOrkUrJSJoIWrgWqxQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا سیدمجتبی
🔥
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/64854" target="_blank">📅 19:53 · 20 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XqBuWKsgV0eIVYpI4bRfqUQqdTBp-x_Sl5P-SlSrLLY10gCVgKrcKlcQRBGu0-JrY1SmNu7xWUAhWoYm2FUZ1ylqr1VpFmaTWU2tuVxY5UBVAXqKCkwzxQPClsZ7_1i2Bb5myObqLa6NkGeIYgFSjMvXh2-HeQrAhJ6dTa0xFjCj3isQuJzKpOZpZ92lSljcIpDctCnAJ6wDdZhHIU73GlnfDUfBY-u2vVe-wG3fhR_rXXlWOHmh3HOp9EVeGRSdEb1cYYhWM20-0BfS8iBFLJ0kWcr-_Dhyaw52d9YWE0zFLC4amHtItaLyMFhRlEVeA238r7Gf4sf5pI2fo3LCoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
خبرگزاری جمهوری اسلامی، ایرنا: ایران پاسخ پیشنهاد متنی امریکا رو به واسطه پاکستانی ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64852" target="_blank">📅 16:23 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81439301a6.mp4?token=AVa6XDnOGWF1zGqBCR-itnualKu1WhgdPqSQ1Ur2keWA0cqaee5FMg5g2SKDABk8B7JsrqL5-afPzjpAap79dUP-AUedypyBCQvPjBgM3uh8D0P4YNiftegbkFEzDWueN_9lAtpAy_APrYKTbp1hf-HKS1y0IYWOydqolLbcYjKY0m-Ku8m7q-cpGD03Tj5h8YWEz0z5IFj3r-oMdBB8oZKqMUr8w4lt-HfJIxHjXF1se21SW8KpTA4ElJb-J-zcV55zz94ix5O5QSqoHN4vOC50EmNbf7cR-slj3sEeT6-3emueF12foBGgqpW-Yzz6m_lflKi_dEqbS0ydXBu6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81439301a6.mp4?token=AVa6XDnOGWF1zGqBCR-itnualKu1WhgdPqSQ1Ur2keWA0cqaee5FMg5g2SKDABk8B7JsrqL5-afPzjpAap79dUP-AUedypyBCQvPjBgM3uh8D0P4YNiftegbkFEzDWueN_9lAtpAy_APrYKTbp1hf-HKS1y0IYWOydqolLbcYjKY0m-Ku8m7q-cpGD03Tj5h8YWEz0z5IFj3r-oMdBB8oZKqMUr8w4lt-HfJIxHjXF1se21SW8KpTA4ElJb-J-zcV55zz94ix5O5QSqoHN4vOC50EmNbf7cR-slj3sEeT6-3emueF12foBGgqpW-Yzz6m_lflKi_dEqbS0ydXBu6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در همین حین که ما تو ایران هی داریم به عقب برمی‌گردیم، برقمون بیشتر قطع میشه و اینترنت نداریم؛ بعد از ۱۵ سال تو سوریه دوباره «ویزا» و «مسترکارد» برگشت و مردم‌ش دوباره دارن به بدیهی ترین حقوق شهروندیشون میرسن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/64851" target="_blank">📅 16:19 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64850">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=Q2YEn5A6qtnsd1kMmWJEZuzNLvp5LHsxV9XtCfd8JJzJMAOOIaxBXY9LCNfsBRAiVxyNXKS9A1pfppf1LhDuY-m7cZb7kyyV_lbIPUhmsDJ4r7lzo6ck4O2MJs4i-a0Zg9-YOc4ZZPhrV7JszsttvJ821Oz9mH1ZVUw4M5C7-gTwvdoOp2JkXZ-AGvij5MFu8kzIqGxlf09VKnb9S4H9xFWFUyYDsiMRpgsFsHKQdUvNnTX_6fk4BPi_XnlwQg7HX5thqM-81jW3ISO8kStSsl_OBiSDFLaZm71XJf3uP2ZhG9IzPvKvfDo5Jw-pVB_0HWDc0EJm0p-jBGWrnvZy_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01d351c3a4.mp4?token=Q2YEn5A6qtnsd1kMmWJEZuzNLvp5LHsxV9XtCfd8JJzJMAOOIaxBXY9LCNfsBRAiVxyNXKS9A1pfppf1LhDuY-m7cZb7kyyV_lbIPUhmsDJ4r7lzo6ck4O2MJs4i-a0Zg9-YOc4ZZPhrV7JszsttvJ821Oz9mH1ZVUw4M5C7-gTwvdoOp2JkXZ-AGvij5MFu8kzIqGxlf09VKnb9S4H9xFWFUyYDsiMRpgsFsHKQdUvNnTX_6fk4BPi_XnlwQg7HX5thqM-81jW3ISO8kStSsl_OBiSDFLaZm71XJf3uP2ZhG9IzPvKvfDo5Jw-pVB_0HWDc0EJm0p-jBGWrnvZy_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز 10می روز جهانی مادره
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/64850" target="_blank">📅 12:44 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64847">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HngV81jbWRx60CgQouwl6eu4z6ABnf8_WpNEV78ooRvRjOV5aBzsNY_A4QAeK1OEt161AAhFiTZzRg8zqMGvjAYdzZ5dasO-pfw69t4a3ZQJpYuVnkBjfJENFkV8cLBxQ4iJe_PzyCntF_yESiKLmcSKLn2OTX5z8R8buN7mnRNpmPn9pPrldCt_q2NdnIFqj8GV6S5kjXo1gTKXETBqijG1YcHa3mFbvzRkKcVKKUm7bd1C3Cub5cGzj8Y_QP1s_S2ANlAtF94I5ruT0ugmlLe7KrwpvmyHwIUVtC172KLPgyIxWHog893udaeBTFswpL-txVS07VVcbTD9F_OPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OBolY45Pmrg-svtqmZ9ClS-lE-TAGDD4gpgu3UtQBu2Q6ehc2NnekCNWXrpmowgGemEnRlJkj8x79yEY2OqGnllc4EKMCVvTNlyCGUrN2UVDoFrIBLOAyBJzeFUDlq5XhTnD6XEqGyvRmkXFihV94MFcoVwVTOYlJp4lRFXhGZP84L4qbAX8P9c6QBebTWfXvmOkYCNVXfS6d8tfPEgmOwmluJw79ZJc9MKkmWO5rPvAuSYaj-AFGoBusDkeW3KIx6tAdeNSTY8HFNuIOCyFEw81c4fA163rVv4BlnsC88RTOsPpJn8tAM2Hw70YDo19Jnp6zMcuPbWgfAw5c-O0lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoEaG8Z96UYRLugwSj1T2jXDSn6UkaG-kgFoae0-uTYywmkeLmaTq5eR3I4W4Qm0djaGnAk_S_OqrD4VfXcrESNWlaTdyTAJFsJPkQJ0hV2-WZJ2yJ_vvC2SrQl3DrC5Mn3PPxSzlTtHie4Iok-5jHXV0VFlxOxcoqSJP8oGVNGR525M2DDJwsooyvfAcbK_puOWy4ZeSfRomm15D9BbJgB1qmudy45qwSZZ-wMpXIxTRYab2BDZXLGD6vqX1W_E4Zd_8j4Lgb2VeUtuMok6JtQWsDCo_DOzrzEh8Z5Wu1aOcsud0lRe8_WbobE6Tstw_4cry_7F3VHZC3TlXrAypQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/64845" target="_blank">📅 09:22 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64844">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9B7y7lW5yPZ6YNjRiwvhQnWPViM1oJplxplarFZLhHuszJCDWl6TcFbaceVtGqNehoq46E9RaU_7aaYMIcyClKNFSB2SJ09jDrGMLtRjAagfYjzlRpioraJJ_cy7eFdxu5D5k7QF-Bkbg694JlIWZ-tus8i7FC9SuzzXarLgpgPEq9DsgmBbEODz0dB0fTUQbBcG-ENwWfAF5UdlBmj_CLkhGYO78nzC_nuTBF5wjNhLJ0PBAzNuvUVEGkaAktNZYdkUM7pZGDXX2AJJYw6TdAenNrai4sGGI8glmmr71GaS4N4vLOkWNbs5rppDYxHm4sKOYW4ylRRfTofK3H8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه: از این به بعد اگه امریکا به نفتکش‌های ما حمله کنه در عوض ما به یکی از پایگاه‌ها یا کشتی‌های امریکا تو منطقه تهاجم سنگنین می‌کنیم
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/64844" target="_blank">📅 08:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64842">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">یه ماه از تبدیل بمباران زیرساخت های ایران به آتش‌بس دو هفته‌‌ای گذشت
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/64842" target="_blank">📅 02:34 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64841">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=Ui3O_EbcTpShJrxTzipOb4CMdNk82dYnEE98tKvgdCabmUMxSWe3rPBl9tnaZ_6HgWjjNAhHQK71FJGqUkJhJr8CIVxZKeSA3-REfMI8A96HufpgqcIhYcPpornoA3CY7-1gV4zwsHfFfSZtiDFxVcIipTecZvhqWlG3vIDzJb0qE28SEndnIU2iFVjGtvqUQcc-a4joBgWnZCvutN8L_Gbj8qbdbKFGsoQoxwtg1mgkWRjJsetXA2pOfJFo9Zs-RmRELxSLDAM2-tlGFcU_L9SE9GqsyoLSE_EFVrBdtFL1ZxHR_HI-MO-38lo0e0VV9ZxkbhiEIAxtvrNu8o44AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d4ece00c.mp4?token=Ui3O_EbcTpShJrxTzipOb4CMdNk82dYnEE98tKvgdCabmUMxSWe3rPBl9tnaZ_6HgWjjNAhHQK71FJGqUkJhJr8CIVxZKeSA3-REfMI8A96HufpgqcIhYcPpornoA3CY7-1gV4zwsHfFfSZtiDFxVcIipTecZvhqWlG3vIDzJb0qE28SEndnIU2iFVjGtvqUQcc-a4joBgWnZCvutN8L_Gbj8qbdbKFGsoQoxwtg1mgkWRjJsetXA2pOfJFo9Zs-RmRELxSLDAM2-tlGFcU_L9SE9GqsyoLSE_EFVrBdtFL1ZxHR_HI-MO-38lo0e0VV9ZxkbhiEIAxtvrNu8o44AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT12caANtITfHbX0YG0PGXr0zSAXUr4fHKKMK0dNbW_edqMVkx5KcNqcTv9YONNMSyDKWJuaqfp9xcPSCQUB6dn9uAkUazJT4jF1NbCdqLOkMwxiRtHhyGvxYVqWER1hCKe5rC0e4bQFENAdOF7DFheM7ZI7eCrDoUhutHmXE79bZWkHFc5YMwpBnJGaX7Ew-Ou0xlMwnAHOaG3J1xmp2iFfa2aREgaXO8_D5PBcZULCZ5ai6QH0d-25eOWcFrHyRRYXE7bsIbITs2jsQIUw3uD6pNT-RtWcnYl_GlFOnzRD-8fsZWBRGUf-4MFc5CA4X2RagEa_bxq9qYDJpmj_3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#مهم
؛ این لکه نفتی اطراف خارک نشان می‌دهد جمهوری اسلامی به‌ناچار نفت استخراج شده را در حجم بالا، به دریا می‌ریزد!!!
اقدامی فاجعه بار برای اکوسیستم خلیج فارس
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/64837" target="_blank">📅 09:13 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64836">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016b41db02.mp4?token=tWTdZPha9C1ZOyLsBK_LcVt6r3eVA4oxlqVCPCbCCAhaO2XPCxCx3jdUYwveted-fQJciIp0tDkrdfBjlUMJFOPSIjUWpo8YVdnQvvsPn2Suvqx5UMhWX6eASxZ5NGZLJppsMnsA8oYKM1at3t7JqREyof7llBL6rDCnZmb5SDFCYivAU7CsgC0V8W_FRzVIW7Jg6gi5uc3mxnaiB92Q7zCBq7TkPTGPofAZDHW1flsmwQw22nGgHSA3lCwJr0O-scJlCcApP8I98X3-2yLFmLUfnj9hqQfUsaKmCIKUFyu09zCSe72ep4KnapGBhRJaDdy7BghErJ_zwOVhWTKvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016b41db02.mp4?token=tWTdZPha9C1ZOyLsBK_LcVt6r3eVA4oxlqVCPCbCCAhaO2XPCxCx3jdUYwveted-fQJciIp0tDkrdfBjlUMJFOPSIjUWpo8YVdnQvvsPn2Suvqx5UMhWX6eASxZ5NGZLJppsMnsA8oYKM1at3t7JqREyof7llBL6rDCnZmb5SDFCYivAU7CsgC0V8W_FRzVIW7Jg6gi5uc3mxnaiB92Q7zCBq7TkPTGPofAZDHW1flsmwQw22nGgHSA3lCwJr0O-scJlCcApP8I98X3-2yLFmLUfnj9hqQfUsaKmCIKUFyu09zCSe72ep4KnapGBhRJaDdy7BghErJ_zwOVhWTKvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: آقای رئیس‌جمهور تقریباْ ۱۰ هفته از اصابت یک موشک به یک مدرسه در میناب می‌گذرد. چه کسی آن موشک را شلیک کرد؟
🇺🇸
ترامپ: این موضوع الان تحت بررسی است و ما به محض اینکه گزارش را دریافت کنیم آن را در اختیار شما قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/64836" target="_blank">📅 09:09 · 19 Ordibehesht 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BoQN-W7_6X53rY8f66-BpSW84IS5xeAsINxelbrY5Wl68Inucpyt8SI3RcqaSQNw4i0cxXNqE5kJofGAyrOk0mottYsoK_UQ_-UPBNZ7fF3onBssuyDFE9OpwOF28uUN9821aC44JplsxrUU0uwBoNM_5-_IJ8OIxzFmC-94yqmRmDG6BAe5WiyzZjxS8eIBRmMm9n2Eiu1KDy5jp0pv6AcfgaobLagPNRAuvFWoFKazRCKmRzWx8Y_-4sT2DdHJQLvy5E243mdL6bohD8aIcF8xOUtjrEP7m8hCP3s6yozyrEg4cNS5TaLmPEgxzXf9d6FWbAy5-3iIBjhymAniAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X0RsrRO8rMRMLaL1dBKoIktGLzQpTTtAdJ6vPaMv1Du17SJ98yaschrxcKR0VgqGh5hxENU1drfJNp4qzCLexbUG-nhIAQrd0cA7FF_R1iAJJFgz5UrlyPKo8yINcI5L_ZZHXwL5Apvls6JXmpDjrWqSLvBzZ9sVjVTI9q1qWPJ86x_vXdlbKWDEXDrsAA9z1ug8ewNNclOqTP8xhSonJ14lppQV2AFEpqD8ImoJDcqnwFaPqdRmbdRSA78gRQKeaANwZMXME5OBBHBYzz5e5P8KRRZEOOTFYTAD3bmkOzqrTNA9sZprQqHyjUGwccFLCz3ckoA-P_iLAAwIK-dIew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرستوی های صادراتی طرفدار حکومت کنار برج ایفل:
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/64831" target="_blank">📅 00:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64828">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EHZwIbuZnCwFcScUFKX-1dP0xt9MjQT-H7UDWMQlpqt67nNeVamR0km0hPKBpRQy6DQ8CKf5yv9G-m_e_wvi4JSg3EsJAb29i7i_ESVe5_VdXJ0-bEg0812jaNXByZrb0KnC2u5I8gihnzD76WSjIWxgAqcL_pJ2gQHVkQe29cJwGn-ncO0RiIbZqOHiIzC0YQNsEI6QY0XXfd15heVIZ8tzEzaqfEV_1Kl-0rRvQw4xmtqXxwFuzSOsJZ7DGFh9VqVBHzgXJ1fp99NkOVZGDGy6eqYoc_NDByvIjgZBQbOBM8H1ADyXZmilno4O8Rx5v0kIXXvHUhuh3w7K4yDiPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ivxv-Nqkhy5-MwEEZPH8kwMacr_p_epwejy3N4Ti41dDgWodgokS6rQ7JkKmGyKszNHNCDiurIZnd22I4wRaC86cuuUPeDuollEdDEp_ZqQfbVsJr-Y8f8kQXeJYVLAMBVVlRUmOfP4hblgOazImMIxCAYeViBty0FaRPMsJmIZRD9ElZ4SlIQ_0x_q777hL_XJlJyg_JS7wTnpLP_ueJtmDlBmRBn7sulOQC5FQA4EGTO5TAyccaTgsnay8P9-_SN8wR0hfGeaGHCD5tzTfoJlVRLKF8gE0Nnw4A_KZ1D2uK7ZaGBHOT3b24RN-CBIeWoCljD9B_8MroYOIg5mLeQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=OKJX_KzbMGINo9I3UMOuRYwPcDTTPEBB92OhKFqNtgWEj24ullbBCgdBM5qqulmU32E_w6PzOeDwu52doRcx1gaZvuize2AWrVFPwyEUziiVD5h9Njah5D59Dkg0pro10lrkipGoITJPqOKVI6M0jWicahlb-V4KjGl_iCHGJKjX5KeBeRVdNF_WJecQCTSgQfaDRuu4inJHReKnGlk9lvg2w9slT6ooxyyf_fixzICCVO2jCk5cTRDdFTRazchVVnaRhEk1m_qELco-co0xgLKeBZ36v40Hl6PuAn_AgcUcRNOV8aJKw60tEA3glY6C314_N1mFT0ioV4mAWF7Cjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a27dcdec82.mp4?token=OKJX_KzbMGINo9I3UMOuRYwPcDTTPEBB92OhKFqNtgWEj24ullbBCgdBM5qqulmU32E_w6PzOeDwu52doRcx1gaZvuize2AWrVFPwyEUziiVD5h9Njah5D59Dkg0pro10lrkipGoITJPqOKVI6M0jWicahlb-V4KjGl_iCHGJKjX5KeBeRVdNF_WJecQCTSgQfaDRuu4inJHReKnGlk9lvg2w9slT6ooxyyf_fixzICCVO2jCk5cTRDdFTRazchVVnaRhEk1m_qELco-co0xgLKeBZ36v40Hl6PuAn_AgcUcRNOV8aJKw60tEA3glY6C314_N1mFT0ioV4mAWF7Cjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SnuKEbKPwwofFs6gOnPqoL16Kg5s1-7qtzMjtcYnjP8k6_RYq9JG-H8-ePAtIS8vO0GzcH1kSiOg0JvP633CWvG7A4A3ocxRpRba7Y7FXw47cjx84oLvv-17qmHQPOZuwAja7KOgEGrOvyVRxJPEYmMsl_Ajm_AbY0s68V6N12EwrGjYVv2oZ5uZLTays0NxOn2r8HWU0Tu1vTMXBPMzXdqcFmq3Ayns4mf65vcEdWmICBqeFFattY3Kn7ZWtp5V3aKru3NVyh0Ooen1pcybpPxJsglXNfTxU4vH0bu99ThrLWqSQXagHKhyyd6XHu3kYtxXAAorWYwyygMI8ljayQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHJ2czKkwqBrTxcjMbTPx5QgfBrMQdWHqHJUas2o-8QOZQA-3J8URJjp4ccUIBhIgeI2RR6uPT0E_VeY3zVZf5DHhmdPGs3zyJTlgcKJ4dem9bniI_FOZgpTyxjFKQnIY7Rou0Gb4ELZN_kPdDEF2Dl8wjhsg15Uz6gWRaJQgrgVsumBtj2COINYoSnIbjLgg3s8zOmF2DmIPfpTZh8VRazaVqSbXPuTX3ACvR_k-hJUOycCSaqNlzFy1DElgd0mTCid5h0oKo21QYiuGjz0NwA7DShPz65hyPDCvuaxLi-cZH_WMZQVzTkpYGIbnNcL-m5x2ALS-QqHIIwXvq5Mlg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=gW2fuXGhQJ9f54MDL9BaWZIHyu6vLnm_1MlVJH5gqQK-cQOj1POTM_w9us_CW7uOnDPnWebMfCsergXlYv75_qcU0-LJ0NZmAyjxKOjXiPsly615tEh4E6FsRdvS1zdIOAU_rR7UTiuM4jJ5dxMQ5fQOXjEP5bSejl1O9pGESa_CiIGJVXh6KkpCxiZwmTG7qZQBEozhA4ClLNBZnMUcBLbr3OkgtfI9XQuM_i2FZx1y6ywlGstV9xpfIkNHO1k7Hfp1bdD3AIwAqxRx76-alLLHTReFJEmq2bs8bZgce7qqOhmu2Lz1Mg7BY2GoneC1eZ_77ve1skYpN5fc9j5wHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc869dea56.mp4?token=gW2fuXGhQJ9f54MDL9BaWZIHyu6vLnm_1MlVJH5gqQK-cQOj1POTM_w9us_CW7uOnDPnWebMfCsergXlYv75_qcU0-LJ0NZmAyjxKOjXiPsly615tEh4E6FsRdvS1zdIOAU_rR7UTiuM4jJ5dxMQ5fQOXjEP5bSejl1O9pGESa_CiIGJVXh6KkpCxiZwmTG7qZQBEozhA4ClLNBZnMUcBLbr3OkgtfI9XQuM_i2FZx1y6ywlGstV9xpfIkNHO1k7Hfp1bdD3AIwAqxRx76-alLLHTReFJEmq2bs8bZgce7qqOhmu2Lz1Mg7BY2GoneC1eZ_77ve1skYpN5fc9j5wHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیو سنتکام از حمله نیرو دریایی آمریکا به دو نفتکش ایرانی M/T SEA STAR III و M/T Sevda که سعی داشتند از محاصره عبور کنند؛ این دو نفتکش پس ازحمله متوقف شدند.
این دو نفتکش تلاش می‌کردند در یک بندر ایرانی در خلیج عمان پهلو بگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/64822" target="_blank">📅 21:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-64821">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
📰
فاکس نیوز به نقل از یک مسئول آمریکایی: ارتش آمریکا امروز به نفتکش‌های ایرانی که قصد شکستن محاصره را داشتند، حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/64821" target="_blank">📅 16:50 · 18 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poAuTYFm-L1ejmkhW4J84wr39bkm1ZViJbQo2hXvdaQLRi4a5Begc1y3BCoiwtmccj6FLg1jSXwBMsce52WxItFon6n7yUHUiHll1toc6JPBXaIUNFMCym2IvP63z9fA1Ci4kkc3hLebfl3myU6SaSUl7eSL22u-fuNfiL85-M81zsue9J3fr3Tryk4dA0V54MKoavJwTRgKxyWpu6wPgGx7mH1T7jVJGvaVJ1ts5VbDAsL4tJ-8efSDm00LaSeQ55Ujoc0mLVKxJYer2SymSrtjDRbzP3YGfGR9Z9VGsTL1NinAS8KaVrbC2iVWeM6DVmd1luBKRONJKtiOhWJf2w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=k773KudWvHDnSp91-_zSzvi-5152kMi7JiIerwfGiTE3eeFdgs4ufJMDGGFhHefRtLMZqmsurECsqc8hMQ5aKfyHvSjtOiZ3VJQlxJ03eRdiuIyGhya-jRIY_gPvXvaf-2FVCkam0TnetzXIvpRRhgKiRbCuBhfG9V3Dn-PcZwb3LDPfHFAnOOgx3-YYtkkKYdZi33Tph3KJgB2AdkxOOlHT-GJ1pL8e1fXygzrG1jhbLOEldGhoqKF0lT8_X-6ygO6uGJHtHHO0_Ba2Qw1nuwWi_0j_bxU5RMmG9AtjgsjVDFubDQlDL79Xh8g7dW9rohqwjetNAUG0zDMyaT0SiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1280dc2aab.mp4?token=k773KudWvHDnSp91-_zSzvi-5152kMi7JiIerwfGiTE3eeFdgs4ufJMDGGFhHefRtLMZqmsurECsqc8hMQ5aKfyHvSjtOiZ3VJQlxJ03eRdiuIyGhya-jRIY_gPvXvaf-2FVCkam0TnetzXIvpRRhgKiRbCuBhfG9V3Dn-PcZwb3LDPfHFAnOOgx3-YYtkkKYdZi33Tph3KJgB2AdkxOOlHT-GJ1pL8e1fXygzrG1jhbLOEldGhoqKF0lT8_X-6ygO6uGJHtHHO0_Ba2Qw1nuwWi_0j_bxU5RMmG9AtjgsjVDFubDQlDL79Xh8g7dW9rohqwjetNAUG0zDMyaT0SiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/64813" target="_blank">📅 04:53 · 18 Ordibehesht 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i5Zg4PQbSMn3kyyCjU5Ne-8jTrYa_u6bkFxwVu_k2X6gMOpvxnsrROwiGIenGlu5hEnz5KkApkEeBLDSduUeRfYqFX3wmXSS12NXpK4ksgRfsK8t23T164JWJLlKO3ToBrY-VTVYuKcq9cLBgIX-G9dWCX1V0LOtkHfGtB6idv2FsgzKYawF3sY7v6ZOxaLlohVV8UMz5KN7Nawi19uRSEPr-FaHyIA4aAU6EkubsZafQU4jKlwehdwU9HOhM12btHs4Q_x6DjkLTaIknwPLa34uGJRVVUluc_URSgExGBRGFoOwpo8Qv5m2X-bcprbMeOl6iG1zrE11RXme8kNBTQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JGc7jUyTPnJJldQn0VQRkxLfMVIKhsTb1H6y1JK7tgSWXNKg1GSxXbvmQsUiHnIgaKeQ0G6BlUYi5Bx-Yb_5ZqSGOxe6yc4_Z7AvSm_HRozWGqH1rz06xBT6wFastVbY7Gygq9J9QRrDYBg5sdjU38jr_G1A7hEwUHU2R0w09bbH6U7UU6JO0DDW_RK7qxyCZ71e__yp0tWIQ1_U1pHjJ6SuoH0FYCpYak9ia_4_i6M_ly9SVWl0JhJ-XgwZGzwvIhmT1beEa6GQ8N1a0SM7WA0qRw4tJWGTgn4p93nXoA_13V1UxdtP1Tpidibe3vcP3xie0ei1NUipNnVf6Xlmgg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMgvAgv53p8VnoJeRcJin8WEDVLsXWviUVU_1jMlxMJvGpm4EDd5BtcsfO1aWiX7PcYwTnfq8gnRu-uo5L8qZFLECwY9wPrR7GNPleTlNvXMIjIMPCjCIy6sWgMkh0MB-w1rMgMNTQbsHRMMy_j0B9S-EB9HGWDw5HpSehNmnKzQ3isY0y0ZAALomG3iLcI-tY2RSA9ce8lHLxxDlSAOsKNVbOsoRNFpB7Sc5bj-Nvb7WqnjsehkvtXF6qGxTZVaW4iR56sGXtKVP66JYyR-z3zOy2jvNakmwKSmSEvAEwXVx9xW9De-oxSoIa1A3UH14fpuMaQnOajSR7biY6AdJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hc7VLs7GQ5Pm3lS0IWRY8sQ87LOFrPEzYdJOrckBKJnmIxNNPZ_FlTHy9_1CHGofTEoq3bZ-cP7rYd6hvJ1OX8GK-y0oAVBEfGA3X3JsHmq1CDd4flkDeFNzPVRV8kGsjQDwyPruFfeIcXx77_Er0rg4tMqNn1TjKzhZoGmUEDUWgjqyfo0Y1MtB3yk0oX6RPV-4pqXCQpUvfb5SVMlKLlTdYE-cMYUEHLham92_QONtYW2d7Idokr24NtOmpUB45P00zIJLpXvNnnON4Hr5UpSCp1EcosdzIgaGNPDfBnjy4yhfTJWGdd6bk16kWUAeX0akmwBHLMLi1k9WLhVUrw.jpg" alt="photo" loading="lazy"/></div>
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
