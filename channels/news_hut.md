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
<img src="https://cdn4.telesco.pe/file/IyB3zwg63yVXxj-TvHvl4uTXH648JNkwsWEjyWXL4h4iHNuhSh0qhnvbHwmcjly3aLcKHNp5dSm7s35HJ0W2HUnMz0Rn0l3oftAfWieCAPcZ_4az6EDHp5fJVTjEpAJiTZjR7lazRbuoHe9FvfQez7NbH8SzhhkLPYT6pWUKeHGZif7ZY141EQtjTkcB9F6JQFidq0AF7_ig5CPsExUp1i921XuthlOylNMlaNTTiTx2bbD_66qA0e8ZqzM_cKwa5M0HMHGpi8VDMNaijFLR4XN0uXOsaf3fPqnt9L6JND-mafSBJPZoFWKWReBQxXf_kYwpOcbaaTJ7ZRZs6_nxLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 167K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 17:40:19</div>
<hr>

<div class="tg-post" id="msg-68350">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd9bbf6c87.mp4?token=GpTdl6DSucgvKXxZdvbdNZ9ugwPyk6Rs2g1ZF6lC4_PvHVfNCgzJBY-alb196EW156G5SOHHe5Uc8b1Dlq6Ft7Sb3kXfVtjR951qLrNXGNYmVuJP6uEWB0_bGOp6bIo5ZamqmvN4HIcXpMJFcnnGJi1_I9h6HhxhaFT3L-WmVtgAcMM43kEyOz5xJdp_dls3pnrsed5AZPebP3Fi7kauUIQ9lCzuTz_Sau4I7c2jpRgs3IyOWGxZM-hozY_MtaEbGr0JK5vmHpbPBeM1HePlu-EJfnzznMyhNH5v4B2xniSPd0z5JPIgaxBbzUFyyhIvPeEom-hsggIDEM7vv57W6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم‌اکنون وضعیت پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/news_hut/68350" target="_blank">📅 17:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68348">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sHu-kqxgikpXkUo71iT_LhLcGkN0J7cDY6quTV1VBHam8KJk0SHLdHZ8F6h0ugKDqa_s73-QM3DEpwe8a1XbGeILNYA3SA0uagbT13Ce8UVZNozCuvaRG-2DQHMicflGTHGqb59g3xVVFRQidTLj2SalfC1hQLWTJ5NASEu3NURX2cWnhV6b39F_DG_YHGk4XZeuLVE31UTqJV4nyNOyxCq2qLKsmRjQBx2RjzmXfW7pGt70PA-mhNrdGxeq0szGIZ6wFWKXzrcejesdLiykBvpgCwIVQw8oXPN8hWY9If56LWvG3w2n8xQDHIzOG5aII_u_2PMl99cr32TR38LZkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6De5kUpyXRL1NqiYJJ1cdw1R3GsR52uj2aLSEHocYqOMVxqM2NGSwxN8LVuH-yvnTuexfrz5BC8BJQR0qIqG5D8Z0OKzWKqpsdbTEOiPyTpt0egsAzQZkBxpJdIOx8VnzpQqoBCQcQ7p9z8odHyTFg8jWmyPQjhcTcyeBP1z7Dv59Jxo2ocmazhWwS_AOREShrHhDX55NmSoyK4RVlQz50NM4P8ogI4r9Mfuiw9bVPkPlxzsaolbLgf1J5nHusd9qrz3LUkJqTsroji_4FlehxmRvPlfxVoV0tLxrKIXX11BC8kPic6RhOQzZHb03Lz0rxBahT12NP3huiAGuM7Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدون شرح.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/68348" target="_blank">📅 16:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68347">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeOhbH0igCJnnENwNcnp-RWLBwwNVLlGQL2l_8V5S7OC-G8X-wwYlks7T0GvscnQaTpueJZvGXX3iFJJnyGRSPO1dbh54LRoS1ttLDRi1V96Esxn-6DoplkT3AZ0U-hayGoGFCQOazGvC04UtOSXhIyzWq5iYT1S7GhwBL4RGT2SupYD5D8MxsUfemBmYke9qbpFXE-vvbrbjL22ndbEcTOv0DFqwlLXnbgd4qRRBgTUsX6OabdYdVhUffHm1Kj5AyUwu4PS3Wc1txn1gNtPmvtoLWqrDZHi-9BtXv7QHWZlo_25Vbz8aZ3xmeFSDSLKLqbKdIe2quavR8bFZajnAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سید مجید موسوی:
حملات موثر و هدفمند تا زمانی که صلح به سواحل جنوبی و تنگه هرمز برگرده ، ادامه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/68347" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68346">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2_AhHecTZ1NbIKLVSYm3DsEifTMZ_9TSU6kXO4fWXeMs3hD2_ArJEdaXy3ciQmNj7V_xzRcyn2FUO5V0g39cSHDBADV-Xai4_BRouYVE8U6yygCV9cTtAg987Hv9yf9ALYS5sJJE5L8Acaw3hsiF2geBJ0WGf0nonnKsuFDcT73kgHj6l8EMzzXd4IKPaTJPyvKF8O09x7HzzOp-FqykqyKjufanHl_T_SUCG7gnPluPs-vWjy-BvcaaxDYvh_SdSUEdadbxPDrq7VCS7LwyXEJAfSBvpyrsxZc3QHvoSewiDPYwWrZ1zITH82WAiw01Ejdk0Zc4o_FO6BKelrGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعد از قوی شدن احتمال حمله زمینی امریکا؛
بسیجی ها توی گوگل لغو عضویت در پویش جان فدا رو سرچ کردن و این جمله جزو بیشترین سرچی های یکی دو روز اخیر گوگل بوده
🤣
🤣
عرزشی فقط زورش به مردم بی دفاع خودش میرسه تا اسم امریکا اومد وسط همه از ترس ریدن به خودشون
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/68346" target="_blank">📅 15:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68345">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioxqVO2YppG9C8xOF16wAPWGeeIeVUjpgy4JKIhhW_0oG5I9As4S-VMBUIHlOpoN64_-75CAQVT4mEWKG0s7cha5LuQIJqrwCY5LxgAg9bOIjzSVyAlqbFQ0kH5VIxqotwyKX1eq-bZAGRvquGe4xihHZiKHTLgeEKUAWxv0WSEkYqR_qHW5_EYvm8NJpFlLv7G1A8IcvmHab66Ru2P4CHk_GS5Qa7NHAx-Ck-ti06QDEkiL_ANFU0oSnj9m3lgnpOQ4JuJKMajxiIS7Pvh1rs9Dy8lFUvbF_SK-Hq--SkMjccC3E9a8cli6etgP9owjMWvnZx1-vkHSM1R61lCmSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
همچنان آمریکا در حال انتقال تجهیزات و مهمات جنگی به خاورمیانه
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/68345" target="_blank">📅 15:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68344">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4edb5d45f8.mp4?token=vlHyO-eaPiZGLoGgbMDESPcp4sQRJ-Rv1kReuWerZb-klPhWOxvst6OWzwaaiJI_HMNiO6vMsG86yuwKhtxDWPr6s-mP3cZxpX98YTAFRzx8qlHzHX7RoDQFks_hOrNdHZ7N7_atLT8fnliiYi5UEfX2S6FSD1aRU9S9ndbYqNfbusTkR2L8d-wZKSiE3zfAWqw__Yp3U5zJcbGhXVAWr-3JsaCBbRK-ou8WpTO_FbPCqDEhqTmGwiWlZdPVzeJ-GmOxnTpqKrUirRRxewXmj5zziKAROrKvr3Ctvy87S9Y096cCSpVL-0XTMFCZfj61mRWTMBa6PBMjBHvVqMCfcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی، تحلیلگر ارشد اینترنشنال :
اگه حکومت تو 18 و 19 دی مردم رو با اسلحه قتل عام نمی‌کرد، مردم خواستار کمک بین‌المللی نمیشدن و الان بچه‌های میناب هم زنده بودن؛
الان هم اگه سپاه تو تنگه هرمز به کشتی‌ها حمله نمی‌کرد، سرباز‌های جنوب کشته نمیشدن.
جنگ طلبی سپاه داره کشور رو نابود میکنه وگرنه ما کشور ثروتمندی داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/68344" target="_blank">📅 14:36 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68343">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇮🇷
سپاه پاسداران:
در یک حمله غافلگیرانه به پایگاه آمریکا در العدید قطر یک سامانه راداری بردبلند و چندین فروند سوخت‌رسان آمریکا به طور کامل منهدم و به چندین فروند دیگر آسیب جدی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68343" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68342">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✅
تسویه فوری جوایز
💥
آپشن های متنوع پیشبینی
💥
کش‌ اوت تا دقیقه 90
🎡
یک فلک متفاوت، هیجانی فراتر از همیشه!
با هر چرخش، همیشه برنده‌ هستید!
🤑
یک‌ بت در صدر بیشترین درصد فریبت‌ ها
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68342" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68341">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHLLfoI3Z-JTjxWWm95I9LkWX-h0qaYZD9tzQbbZBcVUVaskEV20U7GAYAkr-mWh7bTu9gAgyfuxwwoO9Y457u08gXm5GL_w4T66QPwRdlhMAOZKWIss4cTCNk9fPTTukDujKarq3ssMwhlmo0f9_AILMwS8Bfk0R9Rpfc_BuWtgJNuyPexjfxXFHSSDTy3WdFIBGtzHMhpGb4C0WkZ1AJUEzdzG8ENIm3LwslmImhfTR-xjRVfHGeDcGINjPChJay6-oJEEkf_ZuGTvySLgyc2BnD5yUbjO77Z4mInGbr-zdlTyd8HSz91IQq3EuB4VTr87xTRVlbhUgGmDcKlaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🎁
جمعه و‌ دوشنبه‌ های فوتبالی با بانس 100% میکس ورزشی تا سقف 30 میلیون ریال
🔒
واریز و برداشت با سریع ترین و امن‌ ترین درگاه مستقیم
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/68341" target="_blank">📅 14:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68340">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6f934d59.mp4?token=Z0fHbR2FE3p6pPLuOIpv1yAeMVQmg5-SzZwn4ALuD7Dke05gBXXeOLAovPkt9ld4n0bJxhEL_sj6kU7DKR9L7YH_SRpLr7ARDTa_50uNA-N8L2UqhjRLaWY5MOV8mSMFBjpuVVydr-wHGFocekhbYsVdQW6AL6aDgzBF2gY5S7kiKcSW9ibRORlbUf1KrXUZgOlTCsKRyK9P0KWsVvkjAvbByAKpEkY8IuvQR12MFNdQlxJcRg3N7bDnDpjDC-LrSHXNR8DYsh8DLPXbfVRm3rY0trJd5bP_DSJ9v8Eu6teQSVIZJCvJnQSpdbTDzB-5eBD0XbBKH_WQvt7_dNtHKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی مطهرنیا در برنامه «با ضیا» به بررسی برخی سناریوهای احتمالی در تنش میان ایران و آمریکا پرداخت و از احتمال حمله زمینی و نیز مطرح بودن سناریوهای دیگر سخن گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68340" target="_blank">📅 13:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68339">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e12e57fa87.mp4?token=USRXdMQg6tabDCGyPwnuc_YtlXvfioIxG23_OFZ0UncEcMO0XHr-WdpIOkD2i_u425Sr7iubbsLeFrn9wkRVfQSyU_UhydW_b4iLk2m3h4yHTkBtaCBuuDEE5J-8VgrgMrZ003qv99pfzIyzN3MqqJwqCu8ygVGa-MWwt0g7kXrK2BW9D0G8oQgO1APTEkCWA-QkwjkKkK9gE6GYF8R6jR6kojrhkLU8911PPheExvy9S6Akt_pyeeBhPdfkMriNykuZMiu7ANCOEi33_2pRslyVP2Hci3Y9OA19zJBCbekb9Bg-pEdeKNOVQJ4T750fF7NPs61MMF_F3NM-eSfdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تسلیت به بلاگر های چابهاری!
برج کنترل دریایی کاملاً فروریخت دیگه نمی‌تونید باهاش ویو جمع کنید
🙁
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68339" target="_blank">📅 13:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68338">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kn5TQD-dCgfuSV2W5TNDbOMbV_ZL2oVcg5TLAL9GxBVNqKusEMM8tlv5ljEs270YSRmN8wFu8weocjHqQcd4vjAdlYbfUlrMUCtURXbpEYV-W_5_2noEdWlCKg_Ic8avQgtkpX1AcdjajTtDMz0VwNSEsOyKflIUlHg0h1akTd0c0FkG7_Z6k_EEBFWGZd5N12amNZ2URAj9Q7ds3WEQzeliHhqcZlb-ChHGk6T37gHYGTnnkxu_6Crbfdb7sHkDGnh62wbPa97O5PcB9QMPXkrc7FUUELicyPz9y4tY73MTfe0BFOD4BrJ_IghbYTsA0WYP_ecy2rT5drznNsxurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دقایقی پیش یک فروند نفتکش که قصد عبور از آبهای عمان را داشته است مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68338" target="_blank">📅 12:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68336">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MjBCDUoqa4p-VAonaxDpCcWNIhj6ZCBoSqi3dTcLotUhWONmE4uJorGwDCghwggRpPB1FP-GyIluJFsTbaeef-pHJYKgB1WZrSlKt5wpXoEfaMr9Mew8Bz7NGy-TUDa7O1awkgdO_e4P1rw1TWPPwErl7_Z3PkCfyR5srAxcIHfvFCVvlu0KSHVlwOW_w4Kp68oDmqHTDNIk4t-Szv5a0fy5vbfzlRZ6iO6nvKYKySagjN39XmBoh0-N6k7a1XPwUVMtXWniLsC3OA4TCE8hTGt9goFdOxpIVS2dqqyvkvIhoBh3kozFwyEwV372J5kvx1n8iViHxQkvyI7exP0l_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R41x1LdjwrSetQckUnmTPRnWBN7OTM3tpuAYG4OH7-qVVcclfilpUhKxeHRjweL6Taa_JlGJCT1-A7HUcKOffmAxa0cnnGA_1c01tMO100_X0A46sS7FtlFGV7BS9HER0BwxUU-5rkOYI-Jm1s8a84dp6uOz_x2r_XUPUstbjyRfqKMycJTkHVlAZS_1Le9r3JuOBSEuXKL5F3OWVAeOF1LNky-NR0a8vLWgt5mIGx9psbTvo3yrIaJ4AUBgApmE5Wc0EgjFuKSe3_WlDNZcyqynYgXhFcBedWhLe3umJ08NwHeophF3lYJv3jCLy7fsVdSnbtTm2XiUvq6Up-Vhsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
هگست وزیر جنگ آمریکا لحظه سقوط برج مراقبت دریایی چابهار را در صفحه توئیتر خود بازنشر کرد!
الان فقط یه خاطره از این برج مونده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68336" target="_blank">📅 12:30 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
⏺
پل گریوه؛ مسیر بندرعباس، خمیر، لار
⏺
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
⏺
دو پل مسیر کهورستان، لار
⏺
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
⏺
پل روستای مارو شهرستان خمیر
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPgzszBeCI3ocUP6ciKFrAVuB112sRQMNhaStdiG8shryZ_RW76qZt85u55sL_n9LHsb823HUipm0W8R4HxbE6rHLwPhlUSNL5zt5KSSQEM4n0q8zPTkM-YLFhjEBPbQKXhs3WmVRdbHppMKUZmgtbbKmzIvGJtyag6D5VUSeUpoP1G2SFr6kOqPCNxC8ItvahhoyslzXjogbrNMfPX5VB_3q7ZzW-QDs0zw59N1mVZpoq-T6S8ME_mW9hJ-rEvN5m6G8xfJ2bJSBD6JJvB0MMIeKJzBXNnKp8KbS6WDEM2F_ZLfv4kjOuv0pkwajtYpJQ63viHiwLIQ4cMYaE-3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1vY3k_RcNAjZU2JN1sbRlbkLoJwLevqalReK9JQ5pMmSgj4-ITUes5PPgc4TFgQdPTL9KUSR5LCOJ3kZL0mTL_gmBjEwv8VPVakgEAwiXHhAc0w_b-Xnx5XxKSzdlx8RObxiwgx8MGNuvMx2MtbBWuDYeCEvF0MSA4fhP3XbP4qglYCiysTY508KcEEM_b3E4KRmmWLGy0TGvRM3sIv2V6TdToyLJIN2Jm2lgp7_FrxGCzKUl_CYHUcMgAKF9XXYXIL49oNMfDy_emyRlybtDJ1j3fLbx2YOECFOyVZ0xRKGYAXjhDyMXILFQwDjzJTPY7bAU4Q3e00q4Na1_FJ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=OCQfHu6v1UjVsZlBGq9SAnDymjqLF9pnQEj_9sSnweUq0ODtNyGUW4fkGgHsREgy2wLrKiUUzBC1pWkN5EaV26Ame-9MCDyorSWbzu1dAnzgP96aLzRwXG7Iwp5adXJ028uc6I9zDHbCdO9zjhA_Hc44u0Y6azqVsR2aHNEmiobb8gZaE-Rq8bYumr0GvD1bRvPV39FAw6ASZJ4tFRVsWi89Du03_5zAPcofel64mIJ-xdg9NPcGYnmhcoSI7gvTJBQJeRMZ06xk_4lgTeF9a3VVacF0yFdB9aHWmDOHfcRbm9nJGB00DP_XNpkp2iB1TaG4Ya9DveEL64flYreWOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=OCQfHu6v1UjVsZlBGq9SAnDymjqLF9pnQEj_9sSnweUq0ODtNyGUW4fkGgHsREgy2wLrKiUUzBC1pWkN5EaV26Ame-9MCDyorSWbzu1dAnzgP96aLzRwXG7Iwp5adXJ028uc6I9zDHbCdO9zjhA_Hc44u0Y6azqVsR2aHNEmiobb8gZaE-Rq8bYumr0GvD1bRvPV39FAw6ASZJ4tFRVsWi89Du03_5zAPcofel64mIJ-xdg9NPcGYnmhcoSI7gvTJBQJeRMZ06xk_4lgTeF9a3VVacF0yFdB9aHWmDOHfcRbm9nJGB00DP_XNpkp2iB1TaG4Ya9DveEL64flYreWOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuMyvMH0SSB_MAKNRGXMROldacrxD1MsTAbb77lw9-2UH-Jz9myIWDtaNBRmFvbTDs7poi5vhngeUlQ_yetQ6TiGhX5Hi-h191Sv5qVutEzJiusieqVlUQ1USizLXGfpekeC1XBNr4THYQhDRljRzoZCOtcIrKtT3r_B9OGkGEKirCPm6YNfE6qdiABBCoboshgfZK8O22RCIGzq32Up7kpvtkQFlmvU30JlSsQ5bY9FCttZOpI9e5ELMmXMfGCYTzLp5mzgSIhzZcufrfaQIFmUpQ2TVLQL9ShmfupaDRMWLq3d3oqdVOGguI-tPsRFgpkmsq29eu564dno1mHfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=hwM-u1M_tgAx3N9kJfXmevyNUw-4eryXbdr3uBaUQRuA99w8jCuhD_dmo6Be7H37RBdBfv04WGXMRgARDgcCMsik70MRjJepbEskzS_okN_lcnj6UHQYHo7anAIZ7HDDVX4T6nN0cd_sIUEH5M4SxOqSgBDxeW6uL8dc5JNk8uMtN9Dqi2n2Ea7UJBs-gsWoByyarAreTL6WqYy2LmeqDAFtLhPQbNGhiHOZSCrc1F10s_OWOwMlTcHHetIYD2-WPj8tYjvUHEeoKTZprCW551Ht6PBVp7nHDbgZoVoYVMyAo9bmZFKWbdpFA8Js1ZRJRB0XJOVhDcgcuUbDrOqEyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=hwM-u1M_tgAx3N9kJfXmevyNUw-4eryXbdr3uBaUQRuA99w8jCuhD_dmo6Be7H37RBdBfv04WGXMRgARDgcCMsik70MRjJepbEskzS_okN_lcnj6UHQYHo7anAIZ7HDDVX4T6nN0cd_sIUEH5M4SxOqSgBDxeW6uL8dc5JNk8uMtN9Dqi2n2Ea7UJBs-gsWoByyarAreTL6WqYy2LmeqDAFtLhPQbNGhiHOZSCrc1F10s_OWOwMlTcHHetIYD2-WPj8tYjvUHEeoKTZprCW551Ht6PBVp7nHDbgZoVoYVMyAo9bmZFKWbdpFA8Js1ZRJRB0XJOVhDcgcuUbDrOqEyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=IhPoOaYUXpRgSRN8spWbhoWVHb0lLtcQixHeLGZwEld_9fFPa34dqc1f-2IJ4YowEBW_cOmFYPW2AZFRqAAmSnoKJ6Hphx4FXldKA3OEvRjeBznfWlsUf69wRf_6PjZSiKJqB2VznAoUAj1v9b6_NHab_JKPkwcWBRdLvuG7HNZVxcrJffjzdGFLzX_C1rW-1dM1gR6FPBOMImoBzvcL63Qt3nFF0onvDf7_mUpqDfHYEwceKwLqwbGT1u8bP8N-GVgQ5DIBBN0VcCf105tyRNslWzauayZIRGyPuFjpT1RdxuwUZv9zstuCFCtEe-PNhdyL_ZI7vLy6jlACcdji2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=IhPoOaYUXpRgSRN8spWbhoWVHb0lLtcQixHeLGZwEld_9fFPa34dqc1f-2IJ4YowEBW_cOmFYPW2AZFRqAAmSnoKJ6Hphx4FXldKA3OEvRjeBznfWlsUf69wRf_6PjZSiKJqB2VznAoUAj1v9b6_NHab_JKPkwcWBRdLvuG7HNZVxcrJffjzdGFLzX_C1rW-1dM1gR6FPBOMImoBzvcL63Qt3nFF0onvDf7_mUpqDfHYEwceKwLqwbGT1u8bP8N-GVgQ5DIBBN0VcCf105tyRNslWzauayZIRGyPuFjpT1RdxuwUZv9zstuCFCtEe-PNhdyL_ZI7vLy6jlACcdji2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SPm_UAYh2Gd1MRgikMhNpExMzyyghabpA8rKv8rKVj2M6BIAdiPeyb4AaPMwVhjBNVVFeiFmqEUMyHK3virBFfmNMFlknWGzmSu6Ufn7mRnX6HAV-m8d2kYUQuImEX0PDaWUs4HjEA3uFNuBei5Hq0eiDRBfBApxidBUpSHvKXpTB1-zLm-9k8APPb0pIpZMrIlZvdGE85bIGFmdG58bpa9kC025WrvIvJLuUqG70t2WdvlrGZCsZsEbw6W0jUWMapaBka3xQFyZsy7Da-dmJwP_jvKLxtCraVulb3WF7X8z4BgPYC7UjAv5bjA7D0EOgW1C5ZJG6i3qqaA_6zpiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=uQP21K6QEv9WOYQzTYnn9u7UNfAkSvVkqciY75G8NyhE7AILKan5n0q7pYusMPxc1rBVv50jD-FuAVOTDP8epiaHuAzDsVyQBTzQEQ4Go0y0QS51rGubH0FUWXLeZpRGVpoG2uc751eGY-ZZ3yJZdRyYP6TguHo9N1Pv38OhBCyH2hXHqb8SOEz0gxuGyYo6GHCdIUeWasn4g4sOz-75qaqAWhnBFGQOV_4yiixLa1IXNKxG0y5vSWQVJtWaAoNgOnPgg1VeCoy_zuZDtPT5xSTpoQ-xwS-0tA8ZS4G14n5qKdxU9AKTiUt_qjMcqVfhWA3wLi60A3Au8kBd-nFrKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=uQP21K6QEv9WOYQzTYnn9u7UNfAkSvVkqciY75G8NyhE7AILKan5n0q7pYusMPxc1rBVv50jD-FuAVOTDP8epiaHuAzDsVyQBTzQEQ4Go0y0QS51rGubH0FUWXLeZpRGVpoG2uc751eGY-ZZ3yJZdRyYP6TguHo9N1Pv38OhBCyH2hXHqb8SOEz0gxuGyYo6GHCdIUeWasn4g4sOz-75qaqAWhnBFGQOV_4yiixLa1IXNKxG0y5vSWQVJtWaAoNgOnPgg1VeCoy_zuZDtPT5xSTpoQ-xwS-0tA8ZS4G14n5qKdxU9AKTiUt_qjMcqVfhWA3wLi60A3Au8kBd-nFrKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IIZ41ok1TTFuZlBFg8ZFFo5ffX2cqFUFEA9AoA4NBkrGOU5FXWpQDf3q8RywtWDlKM4Uk3FyBWKKI0reLJ137o6DiAVGA7sSNQMLaINRnfUJvjuuat0c2T8bolM0ANjGGthFSwbsCKZlZzSAfAsMi4qL1ELIcuMZSeUKJM9q_W4jCG9c0R2kF-QYTgUSitiZBOv47A5fUcQi-oloH3LaGCCvbf0fxUhD1z5mxPoSI7yhDqWV1mAiXPMneG71uD3WUFrG4SoT3ekN4yMdWYBDXn74bMhMd7ANj5gW-_Pv27bldhu1Koxz22yrGTcw7_NCPi_KIhS8IdHKHdTjx3Gspw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=oXoi-dGGKMyxdTd68MVKbuK4n-m6LCAfp6VYfMA3dGTC3p1IqDh9194DuPCO2v2w0BfEO_-7NIHQalLTObCjW5mUYyhdvUGprYTZu_8n9HLrkGmCPR_Y5YG9dqrjIpwj_SL38rymG6JU8LjsYeo6YrZW5hcxWDCV52i6iMUrSCpl131kpyHw6zGWTt2yIbUsqdaWJVpOnoTq6mR0pdkOXStsU3HjoKzTR6xUKjnXB4h6dpdFinJBm3wVuHr4EJA9tO5PoU478cGx5bQuhGBPjzD0IS7U8xGipL1MjHyhB5lmqBqC7r5E4fp2XEbWInbJHaPVzdHIE7QPT28UAjoyvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=oXoi-dGGKMyxdTd68MVKbuK4n-m6LCAfp6VYfMA3dGTC3p1IqDh9194DuPCO2v2w0BfEO_-7NIHQalLTObCjW5mUYyhdvUGprYTZu_8n9HLrkGmCPR_Y5YG9dqrjIpwj_SL38rymG6JU8LjsYeo6YrZW5hcxWDCV52i6iMUrSCpl131kpyHw6zGWTt2yIbUsqdaWJVpOnoTq6mR0pdkOXStsU3HjoKzTR6xUKjnXB4h6dpdFinJBm3wVuHr4EJA9tO5PoU478cGx5bQuhGBPjzD0IS7U8xGipL1MjHyhB5lmqBqC7r5E4fp2XEbWInbJHaPVzdHIE7QPT28UAjoyvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=pkWXivNpBFMeJQRDtBpxdUdxoTyZcDcQCJeLiGhEBzZzQ-4g74FbQW4Lny9d3inZ35cYIwb0XsJXDUVSBCpn6obRP0urKHgW_3xeyHLg2DfoEg7BXRPnTpJ5ksZJIaTOJ19FIECwbmMWI6-kxeXe2L145kWk4VmxpR_2opI-Vpa5RYHcU1jg7ffoKCYr6oMSPh1cY-Q-fYHtGJvoLcy0rNQfbKm08rjZ6EWzIrtLWMTJ69h2yc2disfi2HC0jRSbFNg06y_38TVbDr6huNDraKAoKB1eEbju3kHyZBFrk-ATk7Sy_Dbu11CzvZBPffRYPbH56Jwt3V4qAVEEokawCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=pkWXivNpBFMeJQRDtBpxdUdxoTyZcDcQCJeLiGhEBzZzQ-4g74FbQW4Lny9d3inZ35cYIwb0XsJXDUVSBCpn6obRP0urKHgW_3xeyHLg2DfoEg7BXRPnTpJ5ksZJIaTOJ19FIECwbmMWI6-kxeXe2L145kWk4VmxpR_2opI-Vpa5RYHcU1jg7ffoKCYr6oMSPh1cY-Q-fYHtGJvoLcy0rNQfbKm08rjZ6EWzIrtLWMTJ69h2yc2disfi2HC0jRSbFNg06y_38TVbDr6huNDraKAoKB1eEbju3kHyZBFrk-ATk7Sy_Dbu11CzvZBPffRYPbH56Jwt3V4qAVEEokawCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات موشکی و پهبادی سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68316">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=guCMSUEJ0C-BW5s8JotRKeiMiod1OpQ0xhN-53ZlMryBdRMWH8r7dVAdrUVztCV2EvqBbqyGPh-3K3N5WZFkdwr6Aprivb15ZvNVm8aZgPHd_5M2eWnyHW4W0gO1rZXbII_YS9OGMpnGQ3nIfl5nEFzHw7c49V__v2bRrDdlWBP3UDG3RMyrbHSzPBR6b-TifOwtT2B_UvwBWAFPDEUkXUDXhTjaHWX5wgk_6nXy6AfA2VgYUmq_3wJMqlTrufM9dUh8uz-QcRwHuvMPVXpm1URAJ-dvLDW86kfor9OBKLrZwP00_k2V39z0m1Sn3ZlUWVCWURN2CxB0tZHcQPeopA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=guCMSUEJ0C-BW5s8JotRKeiMiod1OpQ0xhN-53ZlMryBdRMWH8r7dVAdrUVztCV2EvqBbqyGPh-3K3N5WZFkdwr6Aprivb15ZvNVm8aZgPHd_5M2eWnyHW4W0gO1rZXbII_YS9OGMpnGQ3nIfl5nEFzHw7c49V__v2bRrDdlWBP3UDG3RMyrbHSzPBR6b-TifOwtT2B_UvwBWAFPDEUkXUDXhTjaHWX5wgk_6nXy6AfA2VgYUmq_3wJMqlTrufM9dUh8uz-QcRwHuvMPVXpm1URAJ-dvLDW86kfor9OBKLrZwP00_k2V39z0m1Sn3ZlUWVCWURN2CxB0tZHcQPeopA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/68316" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68315">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68315" target="_blank">📅 01:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68314">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68314" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68313">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو وایرال شده از حمله وحشتناک آمریکا به بوشهر
شیشه های ماشین فیلمبردار درجا ترکید!
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68313" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68312">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d811948267.mp4?token=JAAn9TWQbQ71F6dnt5vyIwcUP8lmzck-hM7HPofbrJP0jiZV49wrZohZMu9cbsWvRP_dLA8_X5cF8qMMT7g9qXfqLDasEnzR5n1JbDyfXih6DtpbSH8wP5uFK8qVH1LAemnQj9h_sT1C8FM2vVaoSgS8MMbsqoGG0_5PmkUs9DtIhFPXQqSPqdqjRKUn7G39vDP5_41yutJUD7Q5TySI1ARSdFWkmxmqSFo-I4c53wOvvpW7CU43R2iO4jOAeSrbKGvmNv5VKXiGOXJdbtAnEy9SwQ1QcxwT68yPmeJh1KDoAUlC8H68lD-XKN-HqYmqltpNAAmVntjwB0w_EnieNZYozKaj6U5ZeUJaBH-Otab_XR2b6m84FFhRm1TGv1fkUVRq5kHQOjmFxLZOf9RuxwEH_-0fZSsm0CoFXn2aVjoxAjA5ZM8iMHgaymvQpFhz2OavSf7Dwfixz2Ya-qdvVZC6sTuBXTncPgyASNsJAyMOCUKelmToLCygMtnfaq333wJFnfp36ZijzeElFKgb74iYD_CCYQiuJSg0f9iDfjXPbr8NkpJr948k1GQIaFe_i_OpuGqFA0Lh7wza2o43GydH5geU7PIwIfE-BQ5Rc2Hs-H_o8W7c3mG_Ox5RpogH4vxnHrhnh_TwaQsVxkMkLZLD9klYc-pQ0z_2PrXil84" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d811948267.mp4?token=JAAn9TWQbQ71F6dnt5vyIwcUP8lmzck-hM7HPofbrJP0jiZV49wrZohZMu9cbsWvRP_dLA8_X5cF8qMMT7g9qXfqLDasEnzR5n1JbDyfXih6DtpbSH8wP5uFK8qVH1LAemnQj9h_sT1C8FM2vVaoSgS8MMbsqoGG0_5PmkUs9DtIhFPXQqSPqdqjRKUn7G39vDP5_41yutJUD7Q5TySI1ARSdFWkmxmqSFo-I4c53wOvvpW7CU43R2iO4jOAeSrbKGvmNv5VKXiGOXJdbtAnEy9SwQ1QcxwT68yPmeJh1KDoAUlC8H68lD-XKN-HqYmqltpNAAmVntjwB0w_EnieNZYozKaj6U5ZeUJaBH-Otab_XR2b6m84FFhRm1TGv1fkUVRq5kHQOjmFxLZOf9RuxwEH_-0fZSsm0CoFXn2aVjoxAjA5ZM8iMHgaymvQpFhz2OavSf7Dwfixz2Ya-qdvVZC6sTuBXTncPgyASNsJAyMOCUKelmToLCygMtnfaq333wJFnfp36ZijzeElFKgb74iYD_CCYQiuJSg0f9iDfjXPbr8NkpJr948k1GQIaFe_i_OpuGqFA0Lh7wza2o43GydH5geU7PIwIfE-BQ5Rc2Hs-H_o8W7c3mG_Ox5RpogH4vxnHrhnh_TwaQsVxkMkLZLD9klYc-pQ0z_2PrXil84" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده آمریکا، دقایقی پیش تصاویری از عملیاتی که دیروز بر روی یک نفتکش ایرانی انجام شد، منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68312" target="_blank">📅 01:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68311">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دیشب که داشتم با دوستای جنوبیم حرف می‌زدم، می‌گفتن حملات بیشتر داره به سمت پادگان و و قرارگاه های نیروی زمینی کشیده می‌شه، حتی دیشب مثل اینکه به پایگاه لشکر ۹۲ زرهی هم حملاتی شده...
امشب هم که خودمون با چشم دیدیم ته حمله به پل‌ها آغاز شده...
حالا سوال همه الان اینه که آیا قراره بهمون حمله زمینی شه؟!
اولاً اینکه ما در جایگاه تحلیلگر نیستیم که به این سوال، جواب دقیقی بدیم، ولی شواهد اولیه داره اینو تایید می‌کنه، اما وقتی کمی عمیق به مسئله نگاه می‌کنیم خیلی موضوع فرا تر از چند تا کلمه‌ست و عملا داریم از یه لشکر حداقل ۱۵۰ هزار نفری حرف می‌زنیم، حمله زمینی به خاک ایران، برای آمریکا بشدت پرریسک و پر از تلفات انسانی خواهد بود، ولی اینکه دارند شرایط رو برای تصرف جزایری مثل خارک فراهم می‌کنند
اون هم به قصد فشار بر جمهوری اسلامی،
یک موضوع دیگه و موضوعی محتمله.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68311" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68310">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861fef7828.mp4?token=GBRsCjgzw56rJPt1msUFjCIHi9fcSpPTwqrr2HFNHUsOteQRtykGsNkZ8xthyOHKrFy-u4haSjpm99QOIA8yBLGS-6Yc0CBv4Xo5gDz05rS5c2SJiauFQDQmFSaGIKQR1-CqEr_JHXHbXkYQZGLKz_txSvmBGUbOEACgLJ1AuYr7mYw1TR_iB5UEOWYnio2t35JDYhl_5N3lUXd5Y9S4KFoh8kLemiwC1YrRWOROqRGv16qjn7xn6vrYCbeeIemQcP7m0yfgCiI0dvFZBl0-A59m4tl6sWgEMl07OAyqqdPjdMTiQmURqod3n6UFqB-wxHA3o4OAuOMiwWTqYitjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861fef7828.mp4?token=GBRsCjgzw56rJPt1msUFjCIHi9fcSpPTwqrr2HFNHUsOteQRtykGsNkZ8xthyOHKrFy-u4haSjpm99QOIA8yBLGS-6Yc0CBv4Xo5gDz05rS5c2SJiauFQDQmFSaGIKQR1-CqEr_JHXHbXkYQZGLKz_txSvmBGUbOEACgLJ1AuYr7mYw1TR_iB5UEOWYnio2t35JDYhl_5N3lUXd5Y9S4KFoh8kLemiwC1YrRWOROqRGv16qjn7xn6vrYCbeeIemQcP7m0yfgCiI0dvFZBl0-A59m4tl6sWgEMl07OAyqqdPjdMTiQmURqod3n6UFqB-wxHA3o4OAuOMiwWTqYitjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
تفنگداران دریایی ایالات متحده از «یگان یازدهم اعزامی تفنگداران دریایی» در تاریخ ۱۶ ژوئیه، عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «وِن یائو» (Wen Yao) در دریای عمان اجرا کردند.
تا به امروز، نیروهای آمریکایی مسیر سه کشتی تجاری را که قصد عبور از سد محاصره را داشتند تغییر داده، یک کشتی را که از دستورات پیروی نکرده بود از کار انداخته و برای اطمینان از رعایت کامل محاصره دریایی جاری ایالات متحده علیه ایران، وارد یک کشتی دیگر شده‌اند.
تنگه هرمز و آب‌های پیرامونی آن همچنان آزاد و باز هستند؛ مگر برای کشتی‌هایی که قصد نقض محاصره آهنین آمریکا را دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68310" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68309">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68309" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68308">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTlQrVUeVcfmoS3h-Y8a1eUWHZ1KTDktc1uNG2GnKxsirJxphpx-0vfDj4rMlV96S4TK-MXpWnbzrTtt0WzkRZTZv8gXUVRaqkqWYy4juPUTyZRTlbwFBxZyJ3FL-gw-5Xfr30r5oXXKpdn7oTNKEUfKV9kdCBJNGsIPuLjkO_Qqa-ILY2wrGAQeY2cplxcghA1M9Hz31JYOgl5n9NSghTjsGW_DszaxOMGhXWsq0jsoAVZ7Mqy86V-siqvIssr20V4lcoF5pqugZ3R3GY6t8LQkqzj8LUPv1AaxYcq_H9H16O8oWExloR78dqsxViLG0QkBqugGMFxErP1UvkONmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68308" target="_blank">📅 00:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68307">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
دفتر فرماندار هرمزگان اعلام کرد که تا اطلاع بعدی، جاده‌های زیر مسدود خواهند بود:
جاده بندرعباس - خمير - لار به طور کامل مسدود است.
جاده کشار - کاهورستان نیز مسدود است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68307" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68306">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLk8m4fkzcsrMotLpS27VUKRZZXJ22QMPuA7Bv88kjAp2lUHfmaCQPL8aGbDl5hyAxUdVWdJGYN9CZmpkqHusf6c6rdFUF-7OmXeKhuCcbKtRRL1cBnxrZ8OO_-RY23cBblRNdws1GwpS74hTAvlzEGHjSzZ80fmXbpj2JmvVMIssruY4Qx_5H8wW-uicYeqAWvhAS1nAp-8ykAQhBzqbV8gtfT0Ce0F323C32zGBvWW-Nm_IfBD_7iiViahIXecyjpS8BH2CLUU7eGYx_wSrcWK1A7E90QDed6gkV-XWI2KKlxur7qr0uIrCPx6awLhXZQsUDhRI6t8MpCu6v-BDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رشیدی کوچی :
⏺
«حمله زمینی به ایران از سمت جنوب رو قطعی میدونم و به نظرم تنها دلیل تأخیرش، گرمای شدید هواست.
به نظرم تمرکز حملات آمریکا روی مناطق جنوبی هم در همین راستاست و ایران هم تا الان با هدف قرار دادن عقبه دشمن در کویت و بحرین، اجازه ایجاد مراکز پشتیبانی رو نداده.»
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68306" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68305">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_nUhBhDNm7Af99fklIhl2Q7c9jdUz1CyN1N9JMwXW7W2A3MAUbqpljr5I_p8r_wzzwzTB7jKCbF20Mx_9kv4bDIGEKunGCaVga7-i46iUSp59N-5KKJxvALBEofsybam8zZnE0BsnWR8ZAVnbF4UawoFBkahRJC0LNUk30f7QGZautNCVH4-0PO5D2b2-91P9VznG8eFHh4crCg0mghC1pnHYzoUiM8JNiQglexpdANtySBvTxWDYgTq9tlDHSwOL7fC3oOm4ftzNn07RI5vdFrG0BbIjS-tQoozTLEc8oIejMseiluchpOi-blDeeZ9NFxvcwVh-CqtVXhvuUCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68305" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68304">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4BOwML3D3WNRcH4xKWm3bnUC8evOdlAxgraFXvhyjoTmg_r2Cj9HXhfQysiaJgAguuxM44BMK_vZL1HVzqmVypkH1ubF3sk_CmhlqfQ5j2Sz3xVqHgS_6eIxfNCYX2EGQLJqYf0hh32PPpmsgzMTSQ1BIYoliYvAcH4yI5GA9vzkjSjIIbIrULZyMbviIbI5Qmzgrj-o1gJkR9eNiArfgjQtN8qk9Wf9MgzDF8Ug9scpe4qPYPuL1fTMKizdqWTUJj_dYwyb5Vhpg6KObgTjgjxlwYmOQz8S8wW4Lmv5BfAKm66j1OxUULEbb38qyntzVOuULreCAWTsTX-a1Qqmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت   @News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68304" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68303">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68303" target="_blank">📅 00:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68302">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=AKWHqdmfw46zUIxbO3PjLaEg2V5sk986r_R1MRz9HIidxfoDpzNP1t9kpOU4ZxwEMsQBcwYH4F9b1I7vLDzNpGFLBzkUyhp7ZOfIG-hrsmlT8WpdWIofM-1c1t7uiOnajo5S48ZBVJJC6sfDdYGP2cb0P2NDbgZG_GQ-csKRpYl8GzxVxHeg5ebZF83vAtHbQtned4yryRrbnQikJDk9iEhN62FoGFD9TTZG2Ojvo_4dbmaqIyIMadCSUiV1vWr0ZN2qt4VCQa_xu8CQlJVI97frJLoi53G4bosaxiTOOmlzn8H2KYxybKLB4bJIDxMQGs4iC8rtCgBsoLxOih70jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=AKWHqdmfw46zUIxbO3PjLaEg2V5sk986r_R1MRz9HIidxfoDpzNP1t9kpOU4ZxwEMsQBcwYH4F9b1I7vLDzNpGFLBzkUyhp7ZOfIG-hrsmlT8WpdWIofM-1c1t7uiOnajo5S48ZBVJJC6sfDdYGP2cb0P2NDbgZG_GQ-csKRpYl8GzxVxHeg5ebZF83vAtHbQtned4yryRrbnQikJDk9iEhN62FoGFD9TTZG2Ojvo_4dbmaqIyIMadCSUiV1vWr0ZN2qt4VCQa_xu8CQlJVI97frJLoi53G4bosaxiTOOmlzn8H2KYxybKLB4bJIDxMQGs4iC8rtCgBsoLxOih70jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو دیگر از پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68302" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68301">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
اونا به شهرستان بندرخمیر و بخش کهورستان حمله کردن و پل ارتباطی بندرعباس به شیراز که معروف به پل بندرعباس - کهورستان - لار هست رو هدف قرار دادن.برق مناطقی از کهورستان هم قطع شده
.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68301" target="_blank">📅 23:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68300">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=uurhZVPcThMpZYEIDHdgTT9kjrEGXJtdWOHoL2pPoI3ngYhXMCG0s-DAHh7TBvSBWBcBRhvu8LnZE7WMMgiJvLYcM-C--cAwIExD18IR7Fejq2XnMyGTkFwyM6jIynqZWU7oY0fc2PeyyUGQb-zDTCpjOymTxyoZhzBUWw1KHliCOhMlhlLpeYkycoAwmob6W1LpC1GQUrZTE85NtasAQCaLZHfjtxgUioBVkDtLN5Ax7lJzCKRQq3ED31TcKobuw4zZ6bSxy6twENV8vTKUBltlz3QFKAliIUZtTCGqKWyBA_QkTXt2kQo-PDcxRP_r8ab17sJtH4zeLJ79Psm4tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=uurhZVPcThMpZYEIDHdgTT9kjrEGXJtdWOHoL2pPoI3ngYhXMCG0s-DAHh7TBvSBWBcBRhvu8LnZE7WMMgiJvLYcM-C--cAwIExD18IR7Fejq2XnMyGTkFwyM6jIynqZWU7oY0fc2PeyyUGQb-zDTCpjOymTxyoZhzBUWw1KHliCOhMlhlLpeYkycoAwmob6W1LpC1GQUrZTE85NtasAQCaLZHfjtxgUioBVkDtLN5Ax7lJzCKRQq3ED31TcKobuw4zZ6bSxy6twENV8vTKUBltlz3QFKAliIUZtTCGqKWyBA_QkTXt2kQo-PDcxRP_r8ab17sJtH4zeLJ79Psm4tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
در کهورستان بندرعباس یک پل هدف گرفته شده.
موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68300" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68299">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68299" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68298">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=Q0i6d95N4jnYlacyI8wa8Hqy2eaYaboEBE39CAbR-1yCjTEKcvBUEmVFyq2AqYt82FCy4DCa4pV0uMel26ntG5NfGsz52MnVLXt9RdaagsURqaFuTcEYEva_1qgLCZ6M8bOFIEcnUZ7SolPpkvv0otmhVzLTvwfgznkz3dWjQbX5JnfCG2Zd3MDeIym-S3fH4nYe5V41x7GiBrgziUvXcApwF4lsUdcg3yk_dNeluZOjoO3OnCk10ItDYAof24tjtJjThuRXcEMrfS6g18C0XfCALY10Acz7LmMXU6sMQZyIIMq5sqAxmpUVYYQdRwGRue_MXPUZVorxs0dnl9kcZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=Q0i6d95N4jnYlacyI8wa8Hqy2eaYaboEBE39CAbR-1yCjTEKcvBUEmVFyq2AqYt82FCy4DCa4pV0uMel26ntG5NfGsz52MnVLXt9RdaagsURqaFuTcEYEva_1qgLCZ6M8bOFIEcnUZ7SolPpkvv0otmhVzLTvwfgznkz3dWjQbX5JnfCG2Zd3MDeIym-S3fH4nYe5V41x7GiBrgziUvXcApwF4lsUdcg3yk_dNeluZOjoO3OnCk10ItDYAof24tjtJjThuRXcEMrfS6g18C0XfCALY10Acz7LmMXU6sMQZyIIMq5sqAxmpUVYYQdRwGRue_MXPUZVorxs0dnl9kcZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملهٔ آمریکا به یک پل در بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68298" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68297">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
طبق گزارشات اولیه، یک پل در بندرعباس هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68297" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68296">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
به گزارش ممبرا ساختمان مخابرات بندرعباس هدف حمله قرار گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68296" target="_blank">📅 23:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68295">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
حمله به ایرانشهر سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68295" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68294">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlmKQl0rPFR9GUQN2SjW7LupPlN5LlGQxQrCNjT8o2KlmC2B_8ZjW15UMdFs1Mq5ITXCftBdaesQIT3KwheqQ3We2HGN43pkC3TJgiGEQgqHQb5hqjRE5y5MNzV1fHgtCVjlWTfOATpEcnfjKPMs21ey2BEbz57ugxKAEHiaTJ_yrR-yHWxLtLIP3Ubms7cGFLZYAwOtmF-FlBRhuCZ6JJMLKN2iab25rGfYJ0gPz-hd1e6LAikORqRCrP18koBFudhW--u-HzdqRwh-Eg7SrghTtGdEh58-Gw4nS2pOhi5oFFuebPcCkKmQwJWPvr_CZWP7WPyFh9GVokHMdXl2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68294" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68293">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5--QLBkrGRJ2gRSHAhWeaXUarn20Z32F0kCeus2RD_MxBeGOxnuFX-mWarplLGvklxtjWod97gfTXg1XjyMyi6Qra5XBjJF5HcmQhGtrMijLCDKqdXvjtKQcAeXiqyeA8U_QqIUF4fDd_5y5I6rSxtEQHlBg4ABgftdVWma4VyiKHxRBxGHiXv75kiMQDFM51alo_lW0utPdYvpFa0mEvkz0i53bYgL5XuL3Dqys59h_7RvjhBZqaLW_jxn_6PhhOClEjxv2z8lHMWTWHcAA-CwSpBM_rvEwPA1HmspFKuChiOet8MDwM8x467WUee8bbrp1h5DbGYnMQRVopEYHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت دفاع کویت:امروز جمهوری اسلامی چندین تاسیسات حیاتیمون رو هدف قرار داد.
از سپیده دم امروز، نیروهای مسلح 32 پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده‌اند؛
این پهپادها رهگیری و با آنها مقابله شده است
این تجاوز شنیع ایران چندین تأسیسات حیاتی در کشور را هدف قرار داد.
علاوه بر این، رهگیری اهداف متخاصم منجر به سقوط آوار در مناطق مسکونی مختلف شد که خسارات مادی به بار آورد، اما خوشبختانه تلفات انسانی نداشت.
نیروهای مسلح بر تعهد مداوم خود به انجام وظایف و تکالیف خود با کارایی و شایستگی، حفظ آمادگی و آمادگی مداوم برای تقویت امنیت ملی و حفظ ایمنی شهروندان و ساکنان تأکید می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68293" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68292">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
پنج انفجار مهیب در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68292" target="_blank">📅 23:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68291">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به قشم و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68291" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68290">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS-</strong></div>
<div class="tg-text">داداش ما الان تو کوچه ایم تو اهواز بچه کوچیکا ذوق صدا بمب رو دارن</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68290" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68289">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68289" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68288">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=dAIeau1Lx1adjFEfZju26t4fpX6DtgiJYAQbE3-R0rQOU-EqnGZpl5kKQtBnKOpi-hKXtIffzyB7X1TpEQj6tnE84y1K2kMzE2pSKeaxRHRHJzAj25MNfAg04mcnBO7g5s2IBbWx2-mADHLwopyRJurWioJnZVwUD79N-IbheZimLS9c58EV2rVC_nkuYM4_Sbh9KqdHNu8VZ5EAQAbSfhx3YhesL3kfDL4oqx7ijHfdPn1Ak2boi_t9vR5-FclkK3GzfGG-H2iemqGaEIn3koT2cVVF290v88_YLPkKKthjORKQLyOJ7ZLDQ0PjUCDyc20iHdgF-7BOV9cXNrBMyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=dAIeau1Lx1adjFEfZju26t4fpX6DtgiJYAQbE3-R0rQOU-EqnGZpl5kKQtBnKOpi-hKXtIffzyB7X1TpEQj6tnE84y1K2kMzE2pSKeaxRHRHJzAj25MNfAg04mcnBO7g5s2IBbWx2-mADHLwopyRJurWioJnZVwUD79N-IbheZimLS9c58EV2rVC_nkuYM4_Sbh9KqdHNu8VZ5EAQAbSfhx3YhesL3kfDL4oqx7ijHfdPn1Ak2boi_t9vR5-FclkK3GzfGG-H2iemqGaEIn3koT2cVVF290v88_YLPkKKthjORKQLyOJ7ZLDQ0PjUCDyc20iHdgF-7BOV9cXNrBMyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از کویت به خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68288" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68287">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68287" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68286">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68286" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68285">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=INUOpt8Am20QQfxSdToVr_RkKmhADg_MDccjRVHSwOgpYX08EWox-StwUcz-trZxETGWAIUbeooVAPqasWG3S2a9SCiXTN6s96mwGtqF_dqq2wKB0YCWmmFuD3zCoUOKTVp-gYX6MufrTirLL6wF0IBZCIjNH_HHZAdz4UKvy9252cuWephwsxGj60stvhbtkIV2J4JggZ358hUSO0ZH8vRaBfYTTc-NDq3O1iX0BV6iDAs6Yz4Wrj-vHg2f-CCK_dzxS5m7YDQ7gBW_AKFzo6Paem12fhsVB8EpSL5nEHUUctx9IYkPIo7b9sDGhzJmmProkiNsCHbEhBaTgHVY0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=INUOpt8Am20QQfxSdToVr_RkKmhADg_MDccjRVHSwOgpYX08EWox-StwUcz-trZxETGWAIUbeooVAPqasWG3S2a9SCiXTN6s96mwGtqF_dqq2wKB0YCWmmFuD3zCoUOKTVp-gYX6MufrTirLL6wF0IBZCIjNH_HHZAdz4UKvy9252cuWephwsxGj60stvhbtkIV2J4JggZ358hUSO0ZH8vRaBfYTTc-NDq3O1iX0BV6iDAs6Yz4Wrj-vHg2f-CCK_dzxS5m7YDQ7gBW_AKFzo6Paem12fhsVB8EpSL5nEHUUctx9IYkPIo7b9sDGhzJmmProkiNsCHbEhBaTgHVY0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68285" target="_blank">📅 22:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68284">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68284" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68283">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtTHbsO2M-8XIZKIx1OaUVqbuz0Swh8imATVjNvP1GEO9zi17lTvqMDHg5DhUJ6tatQPcd7IJYc52VSUAPaA5KrrsUBEC-dsIqxUWXeWSg2Oyvc9i0GStmGWcXHJefBz_8Bd24lGHo_32s9OcJ0hX_B07pA3HEtocSCtHaXH_6mTOdI1JRfDCb4fjj54R9PC8X_0Uyx-ovlGUDErarslVTKB3MqvzjcYP6L1-mD-VN0CNTYBgif0y9XdZH_a7fE62b0sJrWf661jTzMd9BJcUTpKpp1DkUXtW3upRpQd5gqGg55hsQs_FA3x2k9EeIG9ocm5S6jhnkJgwUmY4hl-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68283" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68282">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=Omt_x_hDQCaNwZiL9V9hCpD-TMfuwcgPRrcvL5p1JBV_vUXNWm-LqjSbRDWK_NlABF0AeiqcsgZz0W_0bPem1sBYjnsR6-BHPzgShbBy8TxrBx_W0l3w_LIieyJCnaSWIDzVbYf2oQDrHSjoLRBrUZGgG-6pbm8k5G0jYKv98sFCqv3r5F218PdI_JnHCoEqgWPeGbm5V0d-s4saE5Au9yV4-0i8tIJoAfDjHBA7Z552rv84C-Sw3rrGoZQgiXQxkOM4L9NEIFkGBeWvZfOvaTcHJfd7tJWCbDTMBagpZC5-t36n9-zeYkyARbpI3n_BzsTkIU8chNL9tg3kxIcO2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=Omt_x_hDQCaNwZiL9V9hCpD-TMfuwcgPRrcvL5p1JBV_vUXNWm-LqjSbRDWK_NlABF0AeiqcsgZz0W_0bPem1sBYjnsR6-BHPzgShbBy8TxrBx_W0l3w_LIieyJCnaSWIDzVbYf2oQDrHSjoLRBrUZGgG-6pbm8k5G0jYKv98sFCqv3r5F218PdI_JnHCoEqgWPeGbm5V0d-s4saE5Au9yV4-0i8tIJoAfDjHBA7Z552rv84C-Sw3rrGoZQgiXQxkOM4L9NEIFkGBeWvZfOvaTcHJfd7tJWCbDTMBagpZC5-t36n9-zeYkyARbpI3n_BzsTkIU8chNL9tg3kxIcO2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68282" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68281">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmvSYKfmy6JROd87zVKdun9RdPIfyFb7eiDwS8p411oSW46ZNkmAWJnl4wNUXPgtp0oEQ1ZTvq1sm_bAlQA3Zf8xT2m1I1rak5CFOLCfLGVlH5JehEiTCCthC34-yeVHGcewrnkiNbp0vLkRSyDtzbEaLW1mn5w9BszhL0oe0QCcbpJmj1-Kzjwf2S10MyCuKf1Hp9-hsnyua2jhEj2nb1yMqYIwCrzJb2kVQvVBIn7M-JjZQcW6eGYaW7BkcaOoN8dWExPLRt-ZZ9Q-jCV9N_GxgiKhG2nwZxb09ytqaq8VhGd1arEGtGqa-hxm8w2y9bHXg3R62hwOyAHYb8jX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۲ بعدازظهر به وقت شرقی، نیروهای آمریکایی برای پنجمین شب پیاپی موج جدیدی از حملات را علیه ایران آغاز کردند تا توانمندی‌های نظامی ایران را بیش از پیش تضعیف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68281" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68280">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68280" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68279">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68279" target="_blank">📅 22:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68278">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
پنج انفجار در بندرعباس گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68278" target="_blank">📅 21:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68277">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68277" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68276">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=Fu8yJaY_SqbuBhtVCQ5NjXQENeRHV3yZU3vdyzKrG3yqY9owHiuK6RYE-n0R3lp7oiR9_WGakje3FK4hTYYwC_GkrvCqbBvF1En8ukQmSYnuIyMc1P8zYlRlqkpvA7XL7pBLvSPLKAWBSLXTtXnwBOKjXYkSrFcfSyAxooP_rUmkKOWUC-GQ_elF9y-l0J_AaoWQLRMRNxa8Ay5vq1EKhtp14rxhGUsiFZ9Ctdrx3sNn8MWLfgWE1_EN4P5STlpieBNAdrVruUdKh_yF0CABrXobGiBeKP1LWIGkfg0SJK9F9S8ablT1lk4ftSoO6RTE8ekDAsENZr0aHNZ3RTbuBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=Fu8yJaY_SqbuBhtVCQ5NjXQENeRHV3yZU3vdyzKrG3yqY9owHiuK6RYE-n0R3lp7oiR9_WGakje3FK4hTYYwC_GkrvCqbBvF1En8ukQmSYnuIyMc1P8zYlRlqkpvA7XL7pBLvSPLKAWBSLXTtXnwBOKjXYkSrFcfSyAxooP_rUmkKOWUC-GQ_elF9y-l0J_AaoWQLRMRNxa8Ay5vq1EKhtp14rxhGUsiFZ9Ctdrx3sNn8MWLfgWE1_EN4P5STlpieBNAdrVruUdKh_yF0CABrXobGiBeKP1LWIGkfg0SJK9F9S8ablT1lk4ftSoO6RTE8ekDAsENZr0aHNZ3RTbuBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت سخنگوی سفید کاخ سفید:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتگو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68276" target="_blank">📅 21:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68275">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=nSQWgkI2MEk1eBG9lLzF_56mfp0FtgICDiWEV4wvYpfeX0dqsyWocIM3eYlmmytcP_RwSNn2Vm1KM0wHYYwxlleMnRhWmpCKroPS49DRJivnHSZg3-uvhzCC1aiptcKd12dVz7m3ZQ11CEyvsAePoeJWIcL27GtqVmnu1pk1nhOKRFkPL_g0wqCiiR3SF1JmNco2a4L75vwH3jDk8bIqcD_9nLMq67gHqkKEVz9VLRPWTNwaC9NfH3--iEdL17oMjOBWOP5aC2d7V3DZR4NPE7uLlONFnoKULpRHMXpLNED1SAuag0-jnltfuUCUQgU-853yEeaZETpWSe_P0n8dIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=nSQWgkI2MEk1eBG9lLzF_56mfp0FtgICDiWEV4wvYpfeX0dqsyWocIM3eYlmmytcP_RwSNn2Vm1KM0wHYYwxlleMnRhWmpCKroPS49DRJivnHSZg3-uvhzCC1aiptcKd12dVz7m3ZQ11CEyvsAePoeJWIcL27GtqVmnu1pk1nhOKRFkPL_g0wqCiiR3SF1JmNco2a4L75vwH3jDk8bIqcD_9nLMq67gHqkKEVz9VLRPWTNwaC9NfH3--iEdL17oMjOBWOP5aC2d7V3DZR4NPE7uLlONFnoKULpRHMXpLNED1SAuag0-jnltfuUCUQgU-853yEeaZETpWSe_P0n8dIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز ظهر تو خیابون ولیعصر تهران،یه اتوبوس تندرو بی‌آر‌تی بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت میکنه!
این اتوبوس میوفته تو مسیر سرپایینی و با ۶ موتور سیکلت و ۲ ماشین سواری برخورد میکنه که نهایتا ۶ نفر مصدوم میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68275" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68274">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BinrNetN1isewJbfBnKnTNfJFp9oNzVvuUD5WbqSm0gd6EaJMKR84hXLAkbHlnSzRrrm9IvTe4zwcJ7UWseBBJYFSyF97y-_lCLwJkjt4z3C8YzLg_ojy_UwQdEVF8ckRHxqNGTk6fW8EJfSuav8KfVxLPn57WkkJg96zJpwM-FoH69o15Bawrlapuur73_oYvBUXAFB5Xk_TpZwrXgz-WE7eXQfaFvwXladBL6RXdZWAISUXSSLeLlfZXWU3q-N-0q1yzvC21arbiW8Jr-Hp86gXt3PbX7LQkueWQUgJtklR8vO-JnTGgytdUFYG3r7GqGOAR0ETK8zhL62mxlTNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68274" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68273">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b-4w77ScWUv_mr259PEdgGJu0LGQ4wQy-F3Jq1AIiNtLgvep-JakQ7_HOAiHws_XcUIrTJMsDMHf7BeCsF-dPMqqouhqGBqhZb3dGw6GykzNqS7rrnofk4CnT4nvJWPSN_FGeUZs0jiLmnhZDJ66V1OgHoixtop5HouzLcoErF9_Ga0YPn8G4PMlrArqI3zRjTi-FPcHyQ0nuibkF_NPk2ysvQN0j1_Jvo9bhzV7R2Gb3xXECUEdhTy2ToBHfwUgw7QCwxh0V5aDF4ewqRL3BGvvq6o3oTq3tKaXnZSwv1IrSnHmZPNv_Aq0uD7gr71JJhGMEtlg9VRXfVDx_0YbpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏شاهزاده رضا پهلوی:
در حالی که جنگ‌افروزان جمهوری اسلامی در تهران و پناهگاه‌های امن خود پنهان شده‌اند، سربازان وظیفه و نیروهای جوان را در پادگان‌هایی بی‌دفاع رها کرده‌اند، بی‌آنکه حتی توان حفاظت از این نیروها را داشته باشند. این رژیم بار دیگر نشان داده است که میان جان فرزندان ایران و بقای خود، همواره بقای خود را انتخاب می‌کند.
جمهوری اسلامی این جنگ را بر ملت ایران تحمیل کرده است و مسئولیت جان همه قربانیان آن، از جمله‌ سربازان در پادگان بمپور، بر عهده همین حکومت است. آرزوی همه ما، صلح، امنیت و آرامش برای تمامی ایرانیان است، اما تا زمانی که این رژیم بر سر کار باشد، نه امنیتی پایدار ممکن است و نه صلحی واقعی.
این رژیم تبهکار بیش از آنکه دل‌نگران امنیت مردم ایران باشد، نگران حفظ حزب‌الله لبنان و دیگر نیروهای نیابتی خود در منطقه است. برای این رژیم، بقای بازوهای تروریستی‌اش از امنیت و جان مردم اهواز، زاهدان، بندرعباس، بوشهر، چابهار و سراسر ایران مهم‌تر است.
خطاب من به سربازان، افسران و همه نیروهای میهن‌دوست است. جان خود را برای بقای جمهوری اسلامی به خطر نیندازید. سوگند شما به ایران است، نه به رژیمی که در لحظه خطر، سرکردگانش می‌گریزند و شما را بی‌پناه رها می‌کنند.
من با خانواده‌های داغدار سربازان وظیفه که در حملات اخیر به مراکز نظامی جمهوری اسلامی جان باختند، عمیقأ هم‌دردی می‌‌کنم، و از خانواده‌های همه سربازان وظیفه می‌خواهم تا آنجا که در توان دارند، اجازه ندهند فرزندانشان در این شرایط خطرناک به خدمت سربازی اعزام شوند. هیچ پدر و مادری نباید فرزند خود را به پادگان‌هایی بفرستد که امروز به جای محل خدمت، به میدان مرگ تبدیل شده‌اند.
این جوانان، فرزندان این سرزمین هستند، نه سپر انسانی جمهوری اسلامی. آنها نباید بهای بقای حکومتی درمانده را با جان خود بپردازند.
هم‌چنین از مردم شریف ایرانشهر و زاهدان که برای اهدای خون و یاری رساندن به سربازان مجروح پادگان بمپور شتافتند، صمیمانه سپاسگزارم. این همبستگی ملی یادآور این حقیقت است که مردم ایران، حتی در سخت‌ترین روزها، فرزندان خود را تنها نمی‌گذارند.
ایران به فرزندانش زنده نیاز دارد، برای ساختن آینده‌ای آزاد، آباد و سربلند
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68273" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68272">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
فارس:
حوالی ساعت های ۱۹ و ۱۹:۲۰ نقاطی در  بندر عباس مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68272" target="_blank">📅 20:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68270">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=TxId-hNjOg9cK9LsVqb-I6L3RvxqJ4YIErAkPeiehxGMznQSwcx2KRAgbhyAa8FYKw3Cmce4ePiz0kPa1v1vPGCX30n7DqaWO1-psLqzL0J7NCWW5_oPCKaUdjvxXaBxM-1Dsf6a9akvb45AFeI-Fpy84mlPvyi_gd3xibOTZxR7uFUGuY6g3QsgvR1PpfwheM6Lmj37VB62qRIg6hRRWIEA_elP61P8yp6OyJJjxZeLyXWRQ6mXnVMS-qNNuT4J0CN3xpG05_9lRIdrRpWCu4k-hAZyyPScrrePrcQVnocFolYCJLXMRPZVeA5SajXaD9ivYTJN3025FBh4XitpkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=TxId-hNjOg9cK9LsVqb-I6L3RvxqJ4YIErAkPeiehxGMznQSwcx2KRAgbhyAa8FYKw3Cmce4ePiz0kPa1v1vPGCX30n7DqaWO1-psLqzL0J7NCWW5_oPCKaUdjvxXaBxM-1Dsf6a9akvb45AFeI-Fpy84mlPvyi_gd3xibOTZxR7uFUGuY6g3QsgvR1PpfwheM6Lmj37VB62qRIg6hRRWIEA_elP61P8yp6OyJJjxZeLyXWRQ6mXnVMS-qNNuT4J0CN3xpG05_9lRIdrRpWCu4k-hAZyyPScrrePrcQVnocFolYCJLXMRPZVeA5SajXaD9ivYTJN3025FBh4XitpkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در بهبهان استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68270" target="_blank">📅 19:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68269">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=AdIRGSjom3Yk-lir-vtrwxMJ-BfZs2uy7ZnkNzHX2vjIFUpnQ-zjBrQL-zspRE-77lz35e7vwxpwMfgREbx53kqTgWd_yv2aT5vz-Qu-WJKDWEQWOGOzFFMoCcC_9AFzxpmL6fxFcqcuMC6dV75se67R-qgFLkFP7UcZ1A06SsT4kmgxMmlVTsJhrBM78qoIbtWBdaMe_U-6qeQeKnSipRIItrfYfqE0Vx_Psu9VKuREquNIg5umgsFmXa9arIzJxakxd9ExZP9I2cIU3s4hddO6MVGLqbGfO9XfZjwYt-9ryWnjkXhJyt6kRDz7-lc6yfEz7rMLXLtfmkTSYmVMSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=AdIRGSjom3Yk-lir-vtrwxMJ-BfZs2uy7ZnkNzHX2vjIFUpnQ-zjBrQL-zspRE-77lz35e7vwxpwMfgREbx53kqTgWd_yv2aT5vz-Qu-WJKDWEQWOGOzFFMoCcC_9AFzxpmL6fxFcqcuMC6dV75se67R-qgFLkFP7UcZ1A06SsT4kmgxMmlVTsJhrBM78qoIbtWBdaMe_U-6qeQeKnSipRIItrfYfqE0Vx_Psu9VKuREquNIg5umgsFmXa9arIzJxakxd9ExZP9I2cIU3s4hddO6MVGLqbGfO9XfZjwYt-9ryWnjkXhJyt6kRDz7-lc6yfEz7rMLXLtfmkTSYmVMSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای عالی امنیت‌ ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم، نمیتونم ذهن خونی کنم
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68269" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68268">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqD0z91bX1GJxcPYq_Sn05Dy-qvtO1TOpVFILHflmnp7GMnCcwE6mELhuaQx1FuE_wbSJO6i2MlkUyvOgPRW5t_gwfjqd0_pwr4ldarPcxAD_trh53jYAlwnu-eF6iRkLY04u2mhg2PtycBvgKSv9nSQp983FkZnI76bCkxFnW7aJRxpvu_rqM6wxpblzVVxrIcv9YkuwYWxs2nIG_VTURXR01p4KlAvl8Gl-X5fE-GwBQMNusi7ztkk6VNm9u3C4BIYH67t8mlT9ZeKTbuFRshHDj_EvIUNuVuzpgFhKI90atd84Uxs8hTZ0_BiGZsuTl7tIGzQNX-PtYcEpa8jJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68268" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68267">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSo6NrbOLT61TyPwk3Azh-3rx-oxCtp4xEHoyyoufvrmrhPL4v6EcqKHAPRO6LTJssg4NnUQUJHi-7gX4xxNJ42Sdhw9pVIRlWA0srkBILf9kXXF8qPsyb2fTakF_7awlRfEsYFyHdLccIM6tEMB1zRZNAuoIb3C2SX2zFLJm-3bPlIBAn3WIRwBet2madkUXbNK2iZANuykA5w7QZyWxrUb87Gh9SqJU02OgomVJ4Yh7OmBXMvlTkJCEiSmYVrQSkbyppQ5hv_RzcdIZCBq_8SwPFQyhHCoVFohIdm4SN1Kj7VnU70EiVSdREfyIEUAKHaoVvN3YeeLb12oTCHYQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68267" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68266">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06389032d8.mp4?token=cdUn93uMH-Cpcd2WyNwP4qbsj8HuLIQqJYusOPOrJwgkwvjHhNjihikSGXZnPE4B9sIyE7YH6YFppORo5kFgpwVCmkY2U9NWsNTQ0Asu6qjzuJAZzP3eyc0q5asmfg5XJNMlj9M0ZdIKOByRUYH0uf6_U7FiNLMrNuEAj-SziCgBw3pTCkZCdCy08Z5TA6xov-5ONnUgPgqWtrJIFEO15b_sM1okPJe9jVv9W-Cz_CreA78BI9t96Za6SYH5vrdTgvtbVEQc5Qv4dc-Jkexlv-y9KyzNg1vJVYu6qk9K_BPeYnU_jO3SgaCJN-JQNG68pM2FU2bVjBW19VvXFhSFOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06389032d8.mp4?token=cdUn93uMH-Cpcd2WyNwP4qbsj8HuLIQqJYusOPOrJwgkwvjHhNjihikSGXZnPE4B9sIyE7YH6YFppORo5kFgpwVCmkY2U9NWsNTQ0Asu6qjzuJAZzP3eyc0q5asmfg5XJNMlj9M0ZdIKOByRUYH0uf6_U7FiNLMrNuEAj-SziCgBw3pTCkZCdCy08Z5TA6xov-5ONnUgPgqWtrJIFEO15b_sM1okPJe9jVv9W-Cz_CreA78BI9t96Za6SYH5vrdTgvtbVEQc5Qv4dc-Jkexlv-y9KyzNg1vJVYu6qk9K_BPeYnU_jO3SgaCJN-JQNG68pM2FU2bVjBW19VvXFhSFOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، درباره ایران:
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، این تصمیم با خودشان است.
اما ما قرار نیست ۱۵۰ هزار نیروی زمینی برای تغییر رژیم اعزام کنیم، مگر اینکه خودِ مردمِ حاضر در میدان بخواهند به چنین نتیجه‌ای برسند.
البته ما در هر صورت قصد اعزام نیرو نداریم، اما پیشنهادِ اعزام نیرو عملاً به این معناست که ارتش آمریکا باید این کار را برای مردم ایران انجام دهد.
ما دیگر دنبال چنین کارهایی نیستیم؛ واقعاً نیستیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68266" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68265">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4pxpi8X9oQZKfJXNtWyTdULTcmLH_dRp5LUbVPCxqGO56ahlVrhRNZgEiTOM780ger_pW9bzC8UJPETKwWre7Ipr_dq18SUspcSb4wThRtkj4Z1CSkPpb56OpcqGm216pP9q3TH7mEe6YiFo4LiN9UYZzUXSO5tPzbCoJqOOgLVp-eHfNEJBmdYT9f2DzGZniXLe8Q78MKR7SeUeKy3K0cvb0cJFEZiiHhuUiPfuWEvWNBQQgiLhdi6_vVMCFXkwKk0_htbHSHSGckRsimVfTpPLxaK811QexIKxw-AqXYWIM03A6FfXodTRnKoG32A7NOGWiawUphGZg2iC0EIqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لاشه پهپاد انتحاری آمریکایی FLM-136 LUCAS در نزدیکی بندرعباس
پهپاد LUCAS در واقع همتای آمریکایی پهپاد ایرانی «شاهد-۱۳۶» و یک پهپاد تهاجمی یک‌طرفه (انتحاری) و کم‌هزینه است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68265" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68263">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=e9NsZ4S0HIdga0Mlj5JapAui_xz5t2PMIlbPpG9WvOY1mCQikJ0gQP64JRtQU1B4v-CN_pgWvdm9l6zHoSREtneekDOYl05hdzJ2ii82U144I5RWwXtNHAqaDSZ9-ll56J2oGV7eC3AhtivC4IObaFgWcjfugokLSzgXjvOJMIFV_81o2lO0IgufVbWgHZ_jZycdU32TdOvHctlEH1nY4XKfSJmuEq3Mv1qVuVX-VpcLZ6mIkBiFYxUhmBpbnkjakMkX0PBNMUtdMY4VhUktPk6zr5XQdBTJGHqCxiEN-dz2v-NBiX6VFnDWn7UM7QNOlcmg9enpeC02TtjU4p5FfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=e9NsZ4S0HIdga0Mlj5JapAui_xz5t2PMIlbPpG9WvOY1mCQikJ0gQP64JRtQU1B4v-CN_pgWvdm9l6zHoSREtneekDOYl05hdzJ2ii82U144I5RWwXtNHAqaDSZ9-ll56J2oGV7eC3AhtivC4IObaFgWcjfugokLSzgXjvOJMIFV_81o2lO0IgufVbWgHZ_jZycdU32TdOvHctlEH1nY4XKfSJmuEq3Mv1qVuVX-VpcLZ6mIkBiFYxUhmBpbnkjakMkX0PBNMUtdMY4VhUktPk6zr5XQdBTJGHqCxiEN-dz2v-NBiX6VFnDWn7UM7QNOlcmg9enpeC02TtjU4p5FfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عموپورنگ هم اینطوری بصورت دردناک برای مادرش گریه کرد:
من دیگه مامان ندارم...
دیگه در باز کنم کی بگه چی اوردی برام؟
💔
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68263" target="_blank">📅 17:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68262">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=DQeaypYdvKEJ2dYFovLotmq3TZrdutSiOmc-vzyFu2hSW-YGlcpFJvhfUiw8uno0FxY-vBvlZWkInsGvxhlYYNupfGjXEmVRMWI-OdfpyMBK7m2g3yOkGfiyfhoSbrpuoDGbYxE716qoz_9Y5QEK7gY_juq3AqAwVEe-PeU4i-mieMZtkTAs3cantqF9FG3937nqT-QByuANGtHKiIuAJhgzthKhFVAIKrrSwe4svRwX8zd7frOC3FeAXb8ytLOAiuaBI_WqhDo3gPvV_OPmPNVc8HDs2xjlvMbEDdhCdrSJn1-HaJaDU5AXMjx5wH8Wb4pZ7ZlJk4LBvMrX-F2t_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=DQeaypYdvKEJ2dYFovLotmq3TZrdutSiOmc-vzyFu2hSW-YGlcpFJvhfUiw8uno0FxY-vBvlZWkInsGvxhlYYNupfGjXEmVRMWI-OdfpyMBK7m2g3yOkGfiyfhoSbrpuoDGbYxE716qoz_9Y5QEK7gY_juq3AqAwVEe-PeU4i-mieMZtkTAs3cantqF9FG3937nqT-QByuANGtHKiIuAJhgzthKhFVAIKrrSwe4svRwX8zd7frOC3FeAXb8ytLOAiuaBI_WqhDo3gPvV_OPmPNVc8HDs2xjlvMbEDdhCdrSJn1-HaJaDU5AXMjx5wH8Wb4pZ7ZlJk4LBvMrX-F2t_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام:
هواپیماهای جنگنده F-35A متعلق به نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط هواپیمای تانکر KC-135 هستند، در حالی که در حال انجام گشت‌های هوایی بر فراز خاورمیانه می‌باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68262" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68261">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AILe9Z6XpI8CcWgwGuZ3sAAFfhSTiFJ9TZbMmVhJWXInb_QBPj6Nod1Bx49g0soQtxSN9Mj4iNUeiE-teO-PQLPlhZ8oiXHKh8UGLJD6TT0k8J62le8WXSiAh_U8_D2fK6AF_6Z_od8oaiMFd178RrOeuGnYtMaGUVaDPh7zA-zHn1FcUXN-ROynUE3YFWO_eLv7WrVIVMN87FjM8d_LcCkynNGZTnBBWVb2wUsE5H8flVqFliaTzrR--ynVoVuFEAgxa0QAhQKDdaUD8pWEjuHsO1B5hJBOxNb1V9aTnsxSuUGp18N-RXWJOmDmZUokK0EIbQzp4htdEKEkgrfdUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سال ۱۲۸۷، محمدعلی شاه قاجار مجلس رو بخاطر مخالفتش با ایدئولوژیِ مشروطیت با کمکِ روس‌های حرومی، به توپ بست، و بعد از اون
دوره‌ی دیکتاتوری و استبداد سنگینی
تو ایران شکل گرفت و
آزادی‌خواهان کشته می‌شدند
یک‌سال بعد با اینکه ستارخان تو محاصره شدید بود ولی جبهه هایی شکل گرفت و شمالی‌ها از گیلان و بختیاری‌ها از جنوب به سمت تهران لشکر کشی کردند، و بعد از به‌هم پیوستنشون، سه روز درگیری خیابونی شکل گرفت و در نهایت، روز ۲۵ تیر ۱۲۸۸ محمدعلی شاه به سفارت روسیه فرار کرد و تهران فتح شد
خلاصه که مردم حتی بعد از
یک سرکوب و کشتار سنگین
باز هم ناامید نشدند
و پس از اتحاد اقوام ایرانی
، در
نهایت به خواسته‌شون رسیدند
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68261" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68260">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دیشب تو اوج حملات، ترامپ از جمهوری اسلامی بابت آزادکردن یک شهروند آمریکایی که تو سال ۲۰۲۴ بازداشت شده بود، تشکر کرد
خلاصه اگه امشب حمله‌ای نشد یا شدت حملات کم بود دلیلش رو بدونید
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68260" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68259">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMrBmvZTxQnoxy5EyqzLNYh7re8h1Z9kyHPYq3LhF-h4ImcUlhPCejMnCTVMKTcxagFbugpoZZHM_Aj9VGJsqj03VEJwnZTE7vSjXIbcZ8tLc-4wLHgzUBwMg_i4VYnkeXxmbYxew-3g2fmUg6uGFVJmQK8eUXdcKJitwhsGeGcESobXTV2y_ROESGM_QK4H0eUW_oz9c1BxqIJf9GVPQ0U0tDKgIjlYUFNRxDEkJxwmPnc6V78-DcY4sAq0_-1ImNIsOkpCQuhpVlsX58rqPShJPblj-txcAkYU9MPRzeyS10FSP6bUD6CRut1R-M1acLehcXftS8V0DusYoUfhgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوارنگاره جدید میدان ولیعصر تهران که نوشته «who is D nexT one»و هشتگ لیندسی گراهام هم زیرش قرار داره.
همچنین ‌حروفDT- اول نام دونالد ترامپ رو برجسته نوشتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68259" target="_blank">📅 15:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68258">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💢
مرد پاکستانی ، عاشق محمدرضاشاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68258" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68257">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Meuqtl3Et3UnyaaOEYrpF-TIZ742zQrEqZ1inPn_63o5Y1s5-dWPNOLKZQ2fkFGW-guTHj4FmA8dncC8zEgUL2ZqOurced5KkDkfv08r-15TEUeMWKYxtj9rbLpBFSiFjI3rPvco7T6fuPzQHKsEC0biXGqkUSUp4j5mCuZdlgENKQFag3qxgcYTPlDU4NUn3acdM_V2sJ65lHszfXsNp_fe2iWKFlmdSX7U_djvX7Ht4-aADyDU78FJ5MMMmeXc3N_YJcNJMGgHeECHN84HzPumEtHVnDDSq9eHjeKqMRhw3gE-6Tk8xyZrLY5_15fR8VCXjXaY6fUOpn7tqjvwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نتانیاهو سفر برنامه‌ریزی‌شده خود به ایالات متحده را به تعویق انداخت؛ این تصمیم پس از آن اتخاذ شد که مراسم خاکسپاری سناتور سابق، لیندزی گراهام، به زمانی دیگر در اواخر ماه جاری موکول گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68257" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68256">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=OsaiEuz4-bRa81axxWS2Bp3bfjUpNc_WAbmreUCCn1MaCI4DXuLDZ-A2sD7uURu9PpB9q9GmHY2O6lEnys5EUWRGdMjz_SEVSyju26hlL_g1javlvf3uPnh-s3NF16RmfOedtn1hRRNJNu8CnpWBCZvdntofZdOoCzdMgqUQHcQDsNSGEUuV68SwaDnJVIaNEMpBT82iwq298sncJhnXLATU5e7fmyzxC6PqAZjNbj3g6kOD9mat2xSk2N7CWD8OORDPdfNSVVydOSho30NZHxZsoLL-XhYe28YmK_1kA_V8zlhJGw4xEbxdYDWjlCzfGYb1M1E-oHWPv6Upowjy3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=OsaiEuz4-bRa81axxWS2Bp3bfjUpNc_WAbmreUCCn1MaCI4DXuLDZ-A2sD7uURu9PpB9q9GmHY2O6lEnys5EUWRGdMjz_SEVSyju26hlL_g1javlvf3uPnh-s3NF16RmfOedtn1hRRNJNu8CnpWBCZvdntofZdOoCzdMgqUQHcQDsNSGEUuV68SwaDnJVIaNEMpBT82iwq298sncJhnXLATU5e7fmyzxC6PqAZjNbj3g6kOD9mat2xSk2N7CWD8OORDPdfNSVVydOSho30NZHxZsoLL-XhYe28YmK_1kA_V8zlhJGw4xEbxdYDWjlCzfGYb1M1E-oHWPv6Upowjy3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش مجری‌ها وقتی یارو میگه تشییع خامنه‌ای ۴۰ میلیون نفر حضور داشتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68256" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68255">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyjEXXi2QQW7wqeNrFWQGLe3TQRNAEtrKcpBD4px6KaYCcpxEcOq33zIBMdIH6ThpWXEusmb3KLLbdUE6sRYktL0o2Mb_51SGlDGosUXB0qjPVgMOhWyEVdePI4xKVqw5WzsEIjA04aKvciuCcuj6m19DDkJPBa5KGW8QZrs2_gYCnoRehi1LaLzx047xLL_IgEmDmds4TAvgXbTzYUTtGhdMFLjuH871XoM2UNM29yBb-Fyvne9w3_sYMFVPSTITjynzdcb2-6GWT7NiGLOWcmjUUUZmgZlopxitsWGft3qjnzjpjx3x3tFoQSEN5LELirh21plUAv0fqjlUMw8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فینال جام جهانی 28 تیر (یکشنبه) ساعت ده و نیم شبه؛
- یازدهمی‌ها فرداش عربی نهایی دارن
- دوازدهمی‌ها هم دو روز بعدش عربی نهایی دارن
بهترین راه اینه که فینال رو با گزارش عربی نگاه کنید
دیگه عذاب وجدان نمی‌گیرید
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/68255" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68254">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJ8_gXDCv5UsX9dpHtItedfZE83peJpVkv7QaMjTzC8F8c0Aesq-XbCQ3yeujWwhF-Q7Q6CWZYGoXoo24MN2aASRDJHq3kI2hbKXHt5tR2wbITh1F1X6O4W6PkTb_0g4ZtBhWSJ-dDTRWsG3ZyJdpWSSs6oCzSwVAALJGhVbpeNJSxWqp3D8dV4NTfUPPjNg1A7lx2xmOHLhkBsQ88xwqjYMi3e2mk88XlQzZlS9_gNMtYnorpqLAnNeFj_WUO3-vAyofb21RbM7ee4VD3liknthNWJxqY3FlDJMwRaneTlsYEX17HA0YzQP44ttT1p-kwPcxeV9bjq9s4r_8FLlsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:  کارگاه قیرسازی حرم آتیش گرفته!  @News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68254" target="_blank">📅 13:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68253">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=Ib36uKP4cjN0PKfAbKef2bFAMe3FztbXKu9lBCSKsUMz-pLqYWbxmbXOc_3mbV2bq_W8sZtu4f32GRHjFyOq6rjhqD3EHxVzDpYaZvv2pwenLrVyunp44drGpGX_PUmTCHLAH1RehFECQrzpuZ1dlZ0d4m6l2sJqV4xIYv2Now70NcJHLcFurzUFBfJavF_u-twOak5jYNvvrC6aOghIcCXGtg9oZ3hBY8hAdMK7TF6_M0Y-QF7qKhGfQA3fBgLjJpyQkomppLdgzg-E7bk0ideeazcNTfhdZaU6FILeIcmrxtBG_CyMOc1T6F3laOHGHCodiCmf0-EM83DZgoqMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=Ib36uKP4cjN0PKfAbKef2bFAMe3FztbXKu9lBCSKsUMz-pLqYWbxmbXOc_3mbV2bq_W8sZtu4f32GRHjFyOq6rjhqD3EHxVzDpYaZvv2pwenLrVyunp44drGpGX_PUmTCHLAH1RehFECQrzpuZ1dlZ0d4m6l2sJqV4xIYv2Now70NcJHLcFurzUFBfJavF_u-twOak5jYNvvrC6aOghIcCXGtg9oZ3hBY8hAdMK7TF6_M0Y-QF7qKhGfQA3fBgLjJpyQkomppLdgzg-E7bk0ideeazcNTfhdZaU6FILeIcmrxtBG_CyMOc1T6F3laOHGHCodiCmf0-EM83DZgoqMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تسنیم:
کارگاه قیرسازی حرم آتیش گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68253" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68252">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA-YvVfxtDd9CSKw-htBT3_q7fKSQi11xMjMBL3K4ZWoWvmEbxfkS1QEnr8b-0kHKC6LcNnonTqhyXjlFRop8hiFAbzC7Vp5eRtKy-obcV-riYDeL4lurV78Qge2PontxNxnP1us_fUDRkLhCfLHXL-P1d_4_-uQweFzVrhOvlogzx-xDMiXfJOmxBlOmeuZJvU-t21B322yludWKCu68DFhF9LcGLMVWi8gLnen7GwCcgQH_P_wBk7ViwQ8duRCICdMSem2qwh8cVplde4WYwL3czkk996pWq1lvvASjTLIjY8uwfWSR5abr8joPhh-cx68_gi10KFtJx4jM12iIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتش‌سوزی در حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68252" target="_blank">📅 12:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68251">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314324694e.mp4?token=IXw2_8tDICv0pwVBVt-G69juGQz4OVqV1eyDb_WhgvCoU49rXOMwVQdkZx2VpDxqKfDXAzDFDejP4282LSPVqgMW6MKafgfvBd1FopPRlWnHdCDnLoa6PMJMwFoJoZsErpYSV-SN9BJU_HuByNDBn6ccXyifVTUnO9TkAC9bElFT9r6_nOkmjIwA-w0PylGfNxObNg3__ElzpC5PH3L67m1iCEyKqEUNqyI5llYLhV7PtMbZsoOFahPVyODODxGVUvaJCOufrrdY-kQ5gnjk7IxsAvcY80ORKZ-I6j12SiAzbqDphzWrqLWNmZjXneLaUCMNeRMM6TWRi0WSA5oGC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314324694e.mp4?token=IXw2_8tDICv0pwVBVt-G69juGQz4OVqV1eyDb_WhgvCoU49rXOMwVQdkZx2VpDxqKfDXAzDFDejP4282LSPVqgMW6MKafgfvBd1FopPRlWnHdCDnLoa6PMJMwFoJoZsErpYSV-SN9BJU_HuByNDBn6ccXyifVTUnO9TkAC9bElFT9r6_nOkmjIwA-w0PylGfNxObNg3__ElzpC5PH3L67m1iCEyKqEUNqyI5llYLhV7PtMbZsoOFahPVyODODxGVUvaJCOufrrdY-kQ5gnjk7IxsAvcY80ORKZ-I6j12SiAzbqDphzWrqLWNmZjXneLaUCMNeRMM6TWRi0WSA5oGC4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام تصاویری از حملات به ایران منتشر کرده است.
این تصاویر شامل برخاستن جنگنده‌های «اف/ای-۱۸ئی سوپر هورنت» نیروی دریایی ایالات متحده از ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس آبراهام لینکلن» و شلیک موشک‌های کروز «بی‌جی‌ام-۱۰۹ تاماهاوک» از ناوشکن‌های موشک‌انداز کلاس «آرلی برک» است.
اهداف مورد حمله شامل پرتابگرهای متحرک موشک (TEL)، سایت‌های پرتاب پهپاد، هواپیماهایی که پیش‌تر قطعاتشان جدا و از رده خارج شده بودند، و یک دکل مخابراتی بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68251" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68250">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tt_ZgadZ1OPy2BCw52W_RIpD1P_NpPTsNxSWATJ5P5CQWvyQ28UxBJGGTM9jSj59W-yeJyeD0-RkbX_MtgMut5L6irIC76h2nXiDHEfn3tUj3OLKpOZ8l3GRZQMTh1ROzxZNP2iinokigvaqNeBFrMmTMDwDMwod47bz-BPxPXseK_7pF1xd7qdmrI6jHwtbijf8uQKPag3cp6z874RWQbmif1CDvMwh-9iBmqGDLJwaQcGJbD5Kwy3_2sNGaV0d4T1P6ByC0ycHCHPV5q8cG2z1M9Iu3Wpz2Z7fMLypcsqFiqnExLesTipxUS5OWT3GLWORiAMn2gw8X9qAYy7SRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ:
ایران اجازه داده یک شهروند آمریکایی که در دسامبر ۲۰۲۴ و در دوران ریاست‌جمهوری جو بایدن بازداشت شده بود، از کشور خارج شود.
این زن اکنون در سلامت کامل و شرایطی مناسب خارج از ایران قرار دارد. آمریکا از این اقدام مبتنی بر حسن نیت ایران قدردانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68250" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68249">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=EgmMIteU3AqZ7tpIkpe8HjYUDSg38i4a-H-G9W_njTi03db52BZ8ql5mEy8UdTMJO5DEmV6ytrqHuZAz7maS0CgXgZRZRbz4O5H-899H0PRtlTcr7Hi9bN4w3IgQ6ZgNvIkDWFaMQObTy1Zm2Eghqx1k5AsIqmXt1lTH0rMcARWzPfQ9j3inH_8cW-scVGra1aMuLJb_ICna3Msw49sAu2-KW5pk18bVlwdXVba7Oyp93HsOgJNrwOWH03QcJRPh9v3Zceoek0qz1Kwtt3uGyhdf5zScyTqh5XNjVs9vyLp_BwHGyUPwsF54zSToo-nohVHjTU6KxUXDrULwAhxLwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=EgmMIteU3AqZ7tpIkpe8HjYUDSg38i4a-H-G9W_njTi03db52BZ8ql5mEy8UdTMJO5DEmV6ytrqHuZAz7maS0CgXgZRZRbz4O5H-899H0PRtlTcr7Hi9bN4w3IgQ6ZgNvIkDWFaMQObTy1Zm2Eghqx1k5AsIqmXt1lTH0rMcARWzPfQ9j3inH_8cW-scVGra1aMuLJb_ICna3Msw49sAu2-KW5pk18bVlwdXVba7Oyp93HsOgJNrwOWH03QcJRPh9v3Zceoek0qz1Kwtt3uGyhdf5zScyTqh5XNjVs9vyLp_BwHGyUPwsF54zSToo-nohVHjTU6KxUXDrULwAhxLwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پهباد شاهد در حال رفتن به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68249" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68248">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTk4Lk7zmkb7Fq-UGz674jkIYOxnpTQJuNd1obzwKw4Bi5Ra3Zo84aPi0dMjzpiyhMeY1UeBWak2DNByQhe_QAO3nvqn5PcpZNyh5jg5_L_3gfREHhzlG2aNUN2l9-udhtC7PEUTRmdwVc1lz-MTGjt1wmpphrxTuzseJYFdlyM225hNZfsKVgp6WpTZCFmFar6o7CfwwG0vjprxWXD7ztZxGFpyYUbAW6VOh4pGdGxG4ZJA8sKXaeXIXxSWq8aaUWRL1XSSR5iMSOzHM_h32dWS26gcTkr3KpZHafsUfzOIhspeabKIOcJund1EJWjJQdChEeCTd3ASEiWWMTUVws-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTk4Lk7zmkb7Fq-UGz674jkIYOxnpTQJuNd1obzwKw4Bi5Ra3Zo84aPi0dMjzpiyhMeY1UeBWak2DNByQhe_QAO3nvqn5PcpZNyh5jg5_L_3gfREHhzlG2aNUN2l9-udhtC7PEUTRmdwVc1lz-MTGjt1wmpphrxTuzseJYFdlyM225hNZfsKVgp6WpTZCFmFar6o7CfwwG0vjprxWXD7ztZxGFpyYUbAW6VOh4pGdGxG4ZJA8sKXaeXIXxSWq8aaUWRL1XSSR5iMSOzHM_h32dWS26gcTkr3KpZHafsUfzOIhspeabKIOcJund1EJWjJQdChEeCTd3ASEiWWMTUVws-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون طرفدار حکومت:
من الان شرایط ازدواج ندارم چون نه خونه دارم نه ماشین
بدیهی ترین چیز برای ازدواج اینه حداقل ماشین و خونه داشته باشی اما خب من ندارم و پدرمم پول نداره که بخره
دلیل وضعیت الان بخوام کوتاه توضیح بدم ؛ سخنان حضرت اقا یک طرف ، وضعیتی که مسئولین درست کردن یک طرف
الان ما باید تا30 سالگی بدوویم تا بتونیم یک زندگی متوسط درست کنیم
الان یک میلیارد طوریه ک ما شما با هفت الی هشت سال کار هم نمیتونی بهش برسی و انقدر هم پول کمیه که شما باهاش نمیتونی یک واحد اپارتمان بخری
با این اوضاع 50 شبه کف خیابونم و هیچ ربطی بهم ندارن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68248" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68247">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⏺
صحبت های روح‌الله زم درباره حلقه نارمک و جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68247" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68246">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgaqbtG-H0eoHu52xdEg-ZQwkDg5G2nKUcbBeQH1ld39LQ61Xh5qBY7NV92_hengsLid-AXlQMqdOaWvRJdHW3YECPO5XLrIsWdfNVUT5ZUvJOcLP8DId58nHDay4lx1dbToA1TvUplOtxZPIhUs3XqcQUO3TpZ0V9fgty9Fx3RposLjy2TWQjc17kQkk8Ff0rIQPa94ENXIp0yED2fgZjfiu8ywxTpBGS1-w_xrL7oOo9ZR8C1ZDlZKAmOZUGlczj60E5rAE4AlDY3oHIBGm6Qg8tcekeakS6w_GuhcOCMw0T49aetbqwGka-g2KG0I_G7GV9LNTSUhBaaW0eBT0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان به نقل از دو منبع آگاه:
دونالد ترامپ، رییس‌جمهوری آمریکا، در حال بررسی گزینه‌های گسترش عملیات نظامی علیه جمهوری اسلامی است. به گفته این منابع، در نشست سه‌شنبه اتاق وضعیت کاخ سفید، راه‌های تشدید فشار بر حکومت ایران برای کاهش کنترل آن بر تنگه هرمز بررسی شد.
بر اساس این گزارش، ترامپ احتمال عملیات برای تصرف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و حمله به تاسیسات زیرزمینی کوه «پیک‌اکس» که گفته می‌شود با برنامه هسته‌ای جمهوری اسلامی مرتبط است را بررسی می‌کند. با این حال، او گفته است ممکن است عملیات زمینی برای تصرف جزیره خارک را کشور دیگری انجام دهد.
سی‌ان‌ان همچنین گزارش داد جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگویی تاکید کرده است که جنگ تنها با ابزار نظامی به نتیجه نمی‌رسد و در کنار فشار نظامی، گفت‌وگو برای حل بحران نیز ضروری است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68246" target="_blank">📅 09:15 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
