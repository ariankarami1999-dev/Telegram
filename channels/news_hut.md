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
<img src="https://cdn4.telesco.pe/file/qCCw2ivLNQjEr2x69QSA-70FuMpS3IWDsO2q-oZjq67nf154DKoyK7cjPbI8AmVeQWjuyNqhnDok5rdA6bCrqwnyP-nO4OLxwbDXh9NxkhVTuVq06u_PFi0SN8u03NF2K5QnDYRaBQiwNZzKqJFObwK7K9hzN4F2d2c-VIrmNPsbEgzqlBsEMNCFzVvWFN7_PRj1wWg6gMImj0L0ZZvZdMOwQbpCnowFDrUxaYAF63NPXPtANj_pX_JgailNTX5tXzNH4msWv8v9APW3fv_IDK8h1oUCzg3UM89UZLWSxL1qjg4MyGRqFart62Qw_rUit15ssfcsGCxAmtJMR7BhZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 127K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 14:41:23</div>
<hr>

<div class="tg-post" id="msg-69886">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=n03_xE3asT670BsnXZghShswKCySLZsIh2pyLJ_IZPZ4mZ2TAwGrXJINGMc4RnIWdTZMoSHRUN_2NiY38XxaRr-gUGpfIOhByA-a6PSeaU7sZFoFVC9BtCs7GMoBgeM0pX38VfXoqADvnODNusIx2Xl2yw8bw2NfBUYDqlP-mbe6rfTCTkbAz3GU84eSr-VAxsQdgKt81y84s3IRWUQbQs-TO_HwdjAJEhaJbdIRxHuCZGphvhk3ejtQjWGOi9IcLoZNrL5cNPrZmfFJ4n4cmwLQdTuBhVXqeSjenOS0hN8eYY-JSuM8O05cVJpJ1kfNNzqf0GwEvS4pFTnQmRcYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e61a50ec6.mp4?token=n03_xE3asT670BsnXZghShswKCySLZsIh2pyLJ_IZPZ4mZ2TAwGrXJINGMc4RnIWdTZMoSHRUN_2NiY38XxaRr-gUGpfIOhByA-a6PSeaU7sZFoFVC9BtCs7GMoBgeM0pX38VfXoqADvnODNusIx2Xl2yw8bw2NfBUYDqlP-mbe6rfTCTkbAz3GU84eSr-VAxsQdgKt81y84s3IRWUQbQs-TO_HwdjAJEhaJbdIRxHuCZGphvhk3ejtQjWGOi9IcLoZNrL5cNPrZmfFJ4n4cmwLQdTuBhVXqeSjenOS0hN8eYY-JSuM8O05cVJpJ1kfNNzqf0GwEvS4pFTnQmRcYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان زیبای زندگی کسی که هممون باهاش خاطره داریم...
@News_Hut</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/news_hut/69886" target="_blank">📅 14:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69885">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
🔴
ما سه راهبرد داریم:
ادامه دادن به همین روال فعلی؛ یعنی صرفاً پیش رفتن و نظاره کردنِ وضعیت وخیم آن‌ها، چرا که تورمشان به ۳۰۰ درصد رسیده است. ارزش پول ملی‌شان تقریباً از بین رفته است. آن‌ها حقوق سربازانشان را نمی‌پردازند و سربازانشان در حال ترک خدمت هستند. بنابراین باید همین روند را ادامه داد، چون این وضعیت پایدار نیست.
وارد کردن ضربات بسیار سنگین به آن‌ها، یا... در واقع راهبرد سوم، شکست دادن آن‌ها از طریق اقتصادی است. اما ما به هر حال داریم همین کار را می‌کنیم؛ این [راهبرد] تا حدی بخشی از همان راهبرد اول محسوب می‌شود.
از نظر اقتصادی، وضعیت آن‌ها آشفته و نابسامان است. آن‌ها نمی‌توانند وام بگیرند. ما کنترل منابع مالی‌شان را در دست داریم؛ همان دارایی‌هایی که در اختیار داشتند و رقم بسیار بزرگی هم بود. آن‌ها سرمایه زیادی داشتند و ما اکنون کنترل کامل آن را در اختیار داریم.
من بانکدار آن‌ها هستم. من بانکدار آن‌ها هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/news_hut/69885" target="_blank">📅 13:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69884">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=h_0Py_gcslcw5U9kGT_jUm43hMSIBWEGMDSNyXe6hyQ5uiqAx_A6WhPYShOY7eAbTbSkvbTCpd1EUlRBanQWiuG7hgDByv7wVo3OKAIZb_t1_IkDA_OxyBf48M0__HPasnyFQrS1wr3-5e8wBI_jmDHqfGW_X-N067ES8HmARbqQP1gOstXAgph8-pWXMlb8OGfGHeBEzPAlmKoaG9ty2smC1z2yqE1kFxPVIL1-1EEcBoofpXHcEHh0FnmXDsbfC3dh_n5hmW6JfHYRJS72heuW8qgaO63mA36OeFUU4_YURM_8Q_vwaQMC9fCtQvVKrgDKLvt1xjqssIDDWjUe4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d56160d7.mp4?token=h_0Py_gcslcw5U9kGT_jUm43hMSIBWEGMDSNyXe6hyQ5uiqAx_A6WhPYShOY7eAbTbSkvbTCpd1EUlRBanQWiuG7hgDByv7wVo3OKAIZb_t1_IkDA_OxyBf48M0__HPasnyFQrS1wr3-5e8wBI_jmDHqfGW_X-N067ES8HmARbqQP1gOstXAgph8-pWXMlb8OGfGHeBEzPAlmKoaG9ty2smC1z2yqE1kFxPVIL1-1EEcBoofpXHcEHh0FnmXDsbfC3dh_n5hmW6JfHYRJS72heuW8qgaO63mA36OeFUU4_YURM_8Q_vwaQMC9fCtQvVKrgDKLvt1xjqssIDDWjUe4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سینا حجازی، خواننده:
اگه زنِ هات میخواین، زن گوشت‌خوار بگیرین، زنایی که گیاه خوارن، سردن!
@News_Hut</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/news_hut/69884" target="_blank">📅 13:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69883">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbTS8WBs5qKhTj6UpCLJj008xm8WI7bwPPnFmR-NEJEzIhhcFH2Kg_UFC35DoOjEyytYl2FQwV2hh0bVUBzod55TapzYYIicQD0SOBaHeGiUVLu2VzXkveZBzz6bzFAEYbne3zZyiXPTyqmnoUmabruH_4AUd8nUml2wm0-XVJjGnUKIep0jzcXJeGSmzt_rfNZT8nwAK_bJOTSZg2zkaMVoaQqy6zCP2XW9mPj71VVazeiPG9eyyHLAB1I5Ay0JX8IL8rHcEzhD-PmFQBAZtNHjfaN10JsaJPWcFfgGsT1mYW5tHP8jaXEL3BXhy3n2ojoE6oINRmodl4zzch-kpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا:
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع حادثه‌ای میان یک نفتکش و نیروهای نظامی در دریای عمان خبر می‌دهد.
هویت نفتکش و نیروهای نظامی درگیر در این حادثه هنوز اعلام نشده است.
در حال حاضر جزئیات بیشتری در دسترس نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/news_hut/69883" target="_blank">📅 12:59 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69882">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=QDmc7BEKxzZFjGS-X5YRclZjIeQmXpJW07WH4dqEbAg9bg20ORRIVxQ377F_MYBH2LlcdmD6zaHlYLvh6HAFJoJJUas6w_oIP7XobMRaEJ_pZ_ijkMTu5mnmJUkVJuSUjSeuWkPnDzJ2P8d98AM_o5YgRr-AhM8ASziP7bfQJAoRxFdEe26BSc3LkLycuyGUA2C7NziozW4I8cOPSgk3a_rqZ8KdM0lUdU_t9Xi0Wv7KLcezMp0-UZxa7shXCnNhLWoGg1NCEzEDF_3gRQ0wxbBuWWgrDHysmXtDtz6brtgOOHfCwaTKySDuA3a49g5q39_HENw48M1fdI_ZR9Vz8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b61a921e39.mp4?token=QDmc7BEKxzZFjGS-X5YRclZjIeQmXpJW07WH4dqEbAg9bg20ORRIVxQ377F_MYBH2LlcdmD6zaHlYLvh6HAFJoJJUas6w_oIP7XobMRaEJ_pZ_ijkMTu5mnmJUkVJuSUjSeuWkPnDzJ2P8d98AM_o5YgRr-AhM8ASziP7bfQJAoRxFdEe26BSc3LkLycuyGUA2C7NziozW4I8cOPSgk3a_rqZ8KdM0lUdU_t9Xi0Wv7KLcezMp0-UZxa7shXCnNhLWoGg1NCEzEDF_3gRQ0wxbBuWWgrDHysmXtDtz6brtgOOHfCwaTKySDuA3a49g5q39_HENw48M1fdI_ZR9Vz8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تازگیا به نوع مدیتیشن تو تهران مُد شده که کلمات رو به صورت نفس‌نفس زدن میگن تا انرژی بد ازشون تخلیه بشه
😳
هزینه هر دوره بالای ۴۰ میلیون!!!!!!
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/69882" target="_blank">📅 12:31 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69881">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=mWnf5cZEcjEeGDq8z9C5OUtsbhgryxre5E95SQN4wlO43Mlvi3n4daDVV0uNm7zt8jCNqBnwCSoTdWbgaorSwNbzHPCOnruPkT58DMuEJjl7vHyOeUbdNl2u4PrUCdGLGNbNXmyAaV4fMHmDQdExNsBIyubUZ09dhoo9dB1xakQhG75Sie9JeHidX2tE9LVvqh9y8-O9BuYuyR7EzX5BlYOwK6BkyLDNNrKcsHGt5TewcC6YmpVSXVONNvq7cssvVkYuc2jSDILkZlf5vcXDJwnImUVq_6azcMXhHx2IY8rb0_pHy8Vb_7uq8nGd9NwFCd7Nyimf663XybTV8oYPSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ae8f31fa.mp4?token=mWnf5cZEcjEeGDq8z9C5OUtsbhgryxre5E95SQN4wlO43Mlvi3n4daDVV0uNm7zt8jCNqBnwCSoTdWbgaorSwNbzHPCOnruPkT58DMuEJjl7vHyOeUbdNl2u4PrUCdGLGNbNXmyAaV4fMHmDQdExNsBIyubUZ09dhoo9dB1xakQhG75Sie9JeHidX2tE9LVvqh9y8-O9BuYuyR7EzX5BlYOwK6BkyLDNNrKcsHGt5TewcC6YmpVSXVONNvq7cssvVkYuc2jSDILkZlf5vcXDJwnImUVq_6azcMXhHx2IY8rb0_pHy8Vb_7uq8nGd9NwFCd7Nyimf663XybTV8oYPSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
استایل ثروتمندترین ورزشکار دنیا
🆚
استایل پسرایرانی با ماهی ۱۵تومن حقوق
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/69881" target="_blank">📅 12:01 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69880">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=setARej3TUu-2HFoVM9bQr96Y3nCyQgNPKBEeNv4fPUfBRCvV_FkcvkcjowkcbTQbpUzNxPYqE_V2zsdQraGh62bCYxMUvWgpW1Piy5MXtTAlpA6JHPd7VReNSXGgDW4eIyDRxKlqXzDUDvulePQJBZlnHLbMO_iU2QFNY_IOfUFThDyfLfdZ2i__n43wi0txuey5w8iMdrzUNPDw7uHg_F1emq2GeGrg6H7umVOIfIMg9piGX1aCRVXBxPR0MsGRo0vuTbt7am0BgKQ71BXeBKIZKL-xgqKFUEYMZ5As-OEcEwPjSRJu8UC91Pvx4T0_M2eNmKj2zZ1pgSt6R3PPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf27d27808.mp4?token=setARej3TUu-2HFoVM9bQr96Y3nCyQgNPKBEeNv4fPUfBRCvV_FkcvkcjowkcbTQbpUzNxPYqE_V2zsdQraGh62bCYxMUvWgpW1Piy5MXtTAlpA6JHPd7VReNSXGgDW4eIyDRxKlqXzDUDvulePQJBZlnHLbMO_iU2QFNY_IOfUFThDyfLfdZ2i__n43wi0txuey5w8iMdrzUNPDw7uHg_F1emq2GeGrg6H7umVOIfIMg9piGX1aCRVXBxPR0MsGRo0vuTbt7am0BgKQ71BXeBKIZKL-xgqKFUEYMZ5As-OEcEwPjSRJu8UC91Pvx4T0_M2eNmKj2zZ1pgSt6R3PPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:درباره گرانی ها هم توضیح بدید؟!
🇮🇷
مهاجرانی سخنگوی دولت:
قبلا توضیح دادیم، گرانی های موجود دلیلش فشار اقتصادیه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/69880" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69879">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=dRI5baYmi4hbWk_YlgNVc73JlbamEyfzRmRDtsrzUjRpJc60nkccZaPiwjKD-m04Ab2cY5_cP2FuMdvzJYkSiDgAR7Omstg6_oHQJfOD_iHvX_Qj3Bkhg_GMxfHcqndWbHqKcSlnE5XdHtyXNhKPv33jxL1qSlwoWsDhKVA0O_ENivcSG17WfoH2e-3fQj2GxTZpSf1XyD_FOX6qs4MjFg_XIi-T-3jRoCwMo8fafiim7WdLhQJhR86oAT65PkjTLlSR0ubvKhjjRuIwqrz1PUtTqUpyIxFqHxZcVsDLDK534gq11MQrQMbgF-G9ivM87YEPeq7EKDR_ZnwhmLY14A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c1ee7cbbf.mp4?token=dRI5baYmi4hbWk_YlgNVc73JlbamEyfzRmRDtsrzUjRpJc60nkccZaPiwjKD-m04Ab2cY5_cP2FuMdvzJYkSiDgAR7Omstg6_oHQJfOD_iHvX_Qj3Bkhg_GMxfHcqndWbHqKcSlnE5XdHtyXNhKPv33jxL1qSlwoWsDhKVA0O_ENivcSG17WfoH2e-3fQj2GxTZpSf1XyD_FOX6qs4MjFg_XIi-T-3jRoCwMo8fafiim7WdLhQJhR86oAT65PkjTLlSR0ubvKhjjRuIwqrz1PUtTqUpyIxFqHxZcVsDLDK534gq11MQrQMbgF-G9ivM87YEPeq7EKDR_ZnwhmLY14A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دکتر مشاور خانواده :
یه مرده اومد بهم گفت زنم عاشق دوستم شده و منم بهش گفتم که تو حق داری باهاش رابطه داشته باشی!
گفت منم با خانمِ اون آقا چندبار رابطه داشتم ولی چون اون خانم خودش پارتنر داشت، زیاد خوشم نیومد و کات کردم...
ولی خب موقع سکسِ اون آقا با زنم، من اونجا هستم و تماشا میکنم!
الانم از اینکه خانمم از اون آقا باردار شده خیلی ناراحتم چون آمادگی داشتن بچه رو ندارم.
ولی خب بازم میخوام شناسنامه اون بچه رو به اسم خودم بگیرم...
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/69879" target="_blank">📅 11:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69878">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/69878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/news_hut/69878" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69877">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCL5pMj5gRmRht7322033OL9hKO1-HB7_FUuWqlTAWmsQ9wo80tVVXnDMc0MyyuUcA0SvzjMXm2r1cIp6xuB5J8-l5Q5Dp23hps7N45DuVpog46vMIo3Itt1RO1D_Umsj8-RB5Y1bbWMO6TljXTMEQde-J5DIjCfu6gNJEFAMZBXtPW3GJnNhk59jaFvYj_6wGLX__41F1xWRNdltU0NE5yvtRg-HvKRylxvUWqMRZqocM4zuGOAVrbcGWt-GAhmCyASxBOuqKllp7IcSZOS6IbK5wu-8aGiGUpPKOygequn9i5rbKvcyv8ZJ5pXNnIjexfilMnu0atC_yOtWKILJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
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
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️
برای دانلود اپلکیشن کلیک کنید
👉
r20
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/news_hut/69877" target="_blank">📅 11:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69876">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2435556002.mp4?token=OXOMoXO1vJJO7ejo-cqj_PjKbGLU_3bDO4iQ75dw6E3iQWiQbQL88QAPQyfYB1Xd7EQ9bH1k9FxTR1XsT8WoxK3xg_I0JVHgLD52QgcALMIbuzHma_Lh7edOVWpOwb0ECOi3ojKzQHEUq7o9qJvqu3HqukQH5xYNJFJR5_NbBH2HnEjumSuTyQOQdJk7Rx40GU53YTbku-AumITJ-vIBvrBJFQwgEZSanCbOm_79Mqp5ABSO0nliMZQTP6NQzaDgBRbtJ_zfQzOUKYqIr3lsNDm2TyqlDmxNoY92-f3cQM50LVNrC_6jjCaBD-tLPPDWMAYGyDI4JST0Favk9ZDU8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2435556002.mp4?token=OXOMoXO1vJJO7ejo-cqj_PjKbGLU_3bDO4iQ75dw6E3iQWiQbQL88QAPQyfYB1Xd7EQ9bH1k9FxTR1XsT8WoxK3xg_I0JVHgLD52QgcALMIbuzHma_Lh7edOVWpOwb0ECOi3ojKzQHEUq7o9qJvqu3HqukQH5xYNJFJR5_NbBH2HnEjumSuTyQOQdJk7Rx40GU53YTbku-AumITJ-vIBvrBJFQwgEZSanCbOm_79Mqp5ABSO0nliMZQTP6NQzaDgBRbtJ_zfQzOUKYqIr3lsNDm2TyqlDmxNoY92-f3cQM50LVNrC_6jjCaBD-tLPPDWMAYGyDI4JST0Favk9ZDU8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری و بلاگر طرفدار حکومت:
یعنی چندنفر باهم مشکل داشتن و همدیگه رو به طور کامل میشناختن
این پروژه‌ها از این به بعد قراره زیاد باشه واسه اینکه میدون‌ها و نیروی انتظامی رو ضعیف کنن
قاتل‌ها تو کمتر از 24 ساعت دستگیر شدن و کشور الان تو بالاترین سطح امنیته مخصوصا تو تهران.
متأسفانه قراره خون ریزی های از قبل برنامه ریزی شده شاهد باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/69876" target="_blank">📅 11:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69875">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=W2OTrEuQ7qZdEVN9TdvbAaXeALXZYSN9KbHt5DUEk0s66AQIBsCJ4bhwMIKZ2FJB0qMG355dfVdEz3Nbpduwq7za472m458w6hDnFfJvHGNBDtDQT0iwTVB-8oDhPkz3EVixO09hz-_-HRXYP4A9CU1Gf-YwhjuN7uPziFwfqPgE7YIyAAwBiMvaBL55bwgFdJLODKwNoZnJvtZPfRsR-3RV_lwogSNOMWAVeRtriscHRldLhq6_7agTGFZIvSxW3eD40TmdkqpZzIT2MJ4tuVgJnONdlY_1h3A2kp8xZZCovgFQggnV3HkT1SnE4kyZCqHVF7h8900D3Qdorzb4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022aef02ab.mp4?token=W2OTrEuQ7qZdEVN9TdvbAaXeALXZYSN9KbHt5DUEk0s66AQIBsCJ4bhwMIKZ2FJB0qMG355dfVdEz3Nbpduwq7za472m458w6hDnFfJvHGNBDtDQT0iwTVB-8oDhPkz3EVixO09hz-_-HRXYP4A9CU1Gf-YwhjuN7uPziFwfqPgE7YIyAAwBiMvaBL55bwgFdJLODKwNoZnJvtZPfRsR-3RV_lwogSNOMWAVeRtriscHRldLhq6_7agTGFZIvSxW3eD40TmdkqpZzIT2MJ4tuVgJnONdlY_1h3A2kp8xZZCovgFQggnV3HkT1SnE4kyZCqHVF7h8900D3Qdorzb4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇺🇸
واشنگتن پست:پس از تهدید ترور از سوی ایران، ترامپ مخفیانه هنگام ترک اجلاس ناتو در آنکارا با هواپیمای دیگری جایگزین شد.
او با هواپیمای جدید ۷۴۷-۸ اهدایی قطر (اولین سفر بین‌المللی ریاست جمهوری‌اش) به ترکیه رسیده بود.
برای عزیمت، او علناً و جلوی دوربین سوار هواپیمای قدیمی ایر فورس وان شد و گفت که می‌خواهد «به یاد گذشته» با آن پرواز کند.
اما دقایقی پس از سوار شدن، او و چند دستیارش از طریق یک کامیون پذیرایی فرودگاهی که کانتینر آن به صورت هیدرولیکی به دری در کنار و دور از دسترس رسانه‌ها بالا رفته بود، به یک هواپیمای کوچک‌تر C-32A (757 اصلاح‌شده) منتقل شدند که از دید پنهان بود.
سپس هواپیمای قدیمی ۷۴۷ به عنوان طعمه پرواز کرد و همچنان از تابلوی تماس ایر فورس وان استفاده می‌کرد.
روزنامه‌نگاران و برخی از کارکنان کاخ سفید که در هواپیما بودند، اصلاً نمی‌دانستند که ترامپ با آنها نیست.
به آنها گفته شده بود که پرده‌های پنجره را بسته نگه دارند، که امری غیرمعمول است.
هر دو هواپیما با فاصله چند دقیقه در فرودگاه سلطنتی میلدنهال در بریتانیا فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/69875" target="_blank">📅 10:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69874">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ما ۳ استراتژی برای برخورد با ایران داریم
رصد نقاط ضعف این کشور.
وارد کردن ضربات سنگین.
اعمال فشار اقتصادی.
🔴
اکنون ایران در وضعیت آشوب اقتصادی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/69874" target="_blank">📅 10:13 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69870">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=kwbcItVEe6WsZZzF5O5trVUT6LMDUkhU7_NeVqBKK65b4WedGCnpK62KLxUuSUGdXyFU3mE0x4ALQUP6kDnp7HVEaetn3GPH7W61yvgEYs3LpCCfSbAzlYIomHojfyUald0hrc5AgVPg1kNCWyeo7ItpR11_RHEqOaLaR2wLyH3Bu69hqL6kuJsUn0gsWA2lYsZRj8TN9PzkrPp3W0VPBq4yEttPOZxV_CN4tbNLlQcJUlZ4mk9ThwPgv0Hu-XKZ2UqJLh3dS7PxWY3YA8BNTcEBFR-z9jmXmzD0UIfrEXxGHKuoNfnXvjLyVnwkBxZg8PP2h68E2LYlupZk-B7anQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b616d440e1.mp4?token=kwbcItVEe6WsZZzF5O5trVUT6LMDUkhU7_NeVqBKK65b4WedGCnpK62KLxUuSUGdXyFU3mE0x4ALQUP6kDnp7HVEaetn3GPH7W61yvgEYs3LpCCfSbAzlYIomHojfyUald0hrc5AgVPg1kNCWyeo7ItpR11_RHEqOaLaR2wLyH3Bu69hqL6kuJsUn0gsWA2lYsZRj8TN9PzkrPp3W0VPBq4yEttPOZxV_CN4tbNLlQcJUlZ4mk9ThwPgv0Hu-XKZ2UqJLh3dS7PxWY3YA8BNTcEBFR-z9jmXmzD0UIfrEXxGHKuoNfnXvjLyVnwkBxZg8PP2h68E2LYlupZk-B7anQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
دیروز تو کلمبیا، یه زلزله 7.4 ریشتری اومد و اینجوری به ساختمون ها خسارت وارد کرد؛
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/69870" target="_blank">📅 09:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69869">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=TymmZWuBzPtgtTEOfW1dBG2gD_CvidBJW-1wIKWZjT-D-hYWrlK9EtS_aTeYhUxcJCVzhdYd-btQA_f8PsOudPI4GferGxyDSm5KCAQ3j6gk8bMxDi-AhkLA9w8AQjUM5CSw4Lcwek081NepOHbVhwKgdjFhMCbJRXjLFaE4w8agGoINMrp56U_BdhztbQddBSLfLgRiw_Ng9_zbDvdUYwMEPFGXoi2wjt5DyaKtT4jaIiXCzyHpF8OvNtW58nJMLoKj4VFOT1h_21ScsFueV3pCj5UH51aTIKS0dT36uJhhGyHxxYIh7HqrjMJx6p0k0IF_p9rCIEBIWJqoFsFOzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c07c5ff9.mp4?token=TymmZWuBzPtgtTEOfW1dBG2gD_CvidBJW-1wIKWZjT-D-hYWrlK9EtS_aTeYhUxcJCVzhdYd-btQA_f8PsOudPI4GferGxyDSm5KCAQ3j6gk8bMxDi-AhkLA9w8AQjUM5CSw4Lcwek081NepOHbVhwKgdjFhMCbJRXjLFaE4w8agGoINMrp56U_BdhztbQddBSLfLgRiw_Ng9_zbDvdUYwMEPFGXoi2wjt5DyaKtT4jaIiXCzyHpF8OvNtW58nJMLoKj4VFOT1h_21ScsFueV3pCj5UH51aTIKS0dT36uJhhGyHxxYIh7HqrjMJx6p0k0IF_p9rCIEBIWJqoFsFOzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خرازی:
مجتبی خامنه‌ای اگه تو این سه سال از دفتر رهبری طرد نمی‌شد، می‌کشتنش
خود علی خامنه‌ای هم همین‌طوری بود، تو دفتر خمینی هیچ جایی نداشت
از احمد خمینی بگیر تا کروبی و... همه میخواستن مرگ علی خامنه‌ای رو ببینن.
ابراهیم رئیسی هم قصد داشت رهبر بشه که شهیدش کردن
اصلا بحث همینه مجتبی اگه زیاد پیش پدرش دیده می‌شد خودی ها میکشتنش
تو بحث رئیسی هم یکی از اعضای دفتر اومد خونمون گفتش ک دارودسته اینا میخاد رئیسی رهبر بشه ولی شهادت جلوشو میگیره
خیلی حرفا هست ولی خب مطمئن نیستم بشه گفت یا نه
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69869" target="_blank">📅 09:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69868">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❌
🇺🇸
✈️
پشتیبانی سنگین آپاچی‌ها از نیروهای ویژه آمریکا در افغانستان
⏺
تصاویر نادر و حدود ۱۵ دقیقه‌ای از عملیات دو فروند AH-64 Apache در افغانستان؛
آپاچی‌ها گروهی بیش از ۲۰ نفره از نیروهای طالبان را که در حال آماده‌شدن برای کمین یک گشت نیروهای ویژه آمریکا بودند، شناسایی و درگیر می‌کنند.
در این درگیری، آپاچی‌ها ابتدا با توپ ۳۰ میلی‌متری M230 مواضع طالبان را زیر آتش می‌گیرند و سپس برای درگیری با اهداف مشخص‌تر از موشک‌های AGM-114 Hellfire استفاده می‌کنند.
تصاویر این ویدئو با سامانه تصویربرداری حرارتی FLIR نصب‌شده روی آپاچی ثبت شده؛ به همین دلیل صحنه‌ها به‌صورت تصویر حرارتی دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/69868" target="_blank">📅 09:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69867">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
a19
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/69867" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69866">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYUI2pJ4mSEIyM84cxFfSXNmZaKxrrykAy0wpMPDhBYxz4HDLdoqs5BhRdDdtpcuiNjiWYnlIkm3EJ9sKm32xgv4TJFwcoSoO3s6Ud-ohLi1OEGRN2z4RhjZ-jgdeu8D7rZFTwz8oTPdZsnOLbPGBCQehkLnAEmKP1PGMLGW5PAEZTopYMxNoEwZS4xahUkvt3V8Yp2WwGkhEcLwBtZtIFKcsu6Rt1onmkvz7ABjs7QQzWNDEeXYDBSpRNfEzck9HIQ8ekl1pFVV3WQzQgBDNLqGwvwNQt9ZSllZVjoE5oZW_eYvAC28jeYcFcyk8ebAlSKxnxPaUEwaL_OPjAZOSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
a19
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/69866" target="_blank">📅 01:58 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69865">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=O6PrhSFKJXpIxBPO7WbkNnmsq6F2JVI6CXEptV1ttkXggMaqwLy8zJp95g7kQMwEzispqcdrwYqj-1WkZjLkEnP8Uh2TN7lSu96_4IlnkjBUEl9shWUHGGAaaWlwE4e1D6EnrXrfF5UutGAwQcCYU6tFgT7x-aSF2diYkA_QxPDwtV-rxErfReTV51J1TQq-PTRJZ3f_EkJGY6Jo4O7Mwi07hw-n9cwup4krNvJRVnrcGwrWJSsiIXM551uEt53SdPjYCiPH1bA93VJcJt4kjacQ_7avhE5GOYkGTX1C5KD4ktNhrHvtVog-ZOQJ1HbeJhBorJpz71FXVsR6sFtjdLNjcGI-hjCUe6qdmwls9xBKImNPgC7rC-xutfviDfYyKLiSusTe4suc7JY9-s1F3ByTH0SndSe5RY6WNe3uHtuWRwWc6Gsc2cXVxcqQtVVPwxjg2v29B6_O_6gk3jvN6pvUmdKqXMbEiKy2vDdsz3QIr_tbTcEC5_oqb2_0Kb52ZNLflyWCEej2uKIlDNi_P4rcNNc9RE_Ow6vfhaI5I-OgPZ0ImuwxOWzj0S6Qe0BNxw6A_PKcnA8CaJ267lV4-8Rc2n2kWKOFxfl64UwFetaUUUJh8WabdUr_FooZwyckVpfg4VYyW95b2V7jYJOxDEvfqhcL8NwtoZqg5IF07n0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/6ad4ea0af6.mp4?token=O6PrhSFKJXpIxBPO7WbkNnmsq6F2JVI6CXEptV1ttkXggMaqwLy8zJp95g7kQMwEzispqcdrwYqj-1WkZjLkEnP8Uh2TN7lSu96_4IlnkjBUEl9shWUHGGAaaWlwE4e1D6EnrXrfF5UutGAwQcCYU6tFgT7x-aSF2diYkA_QxPDwtV-rxErfReTV51J1TQq-PTRJZ3f_EkJGY6Jo4O7Mwi07hw-n9cwup4krNvJRVnrcGwrWJSsiIXM551uEt53SdPjYCiPH1bA93VJcJt4kjacQ_7avhE5GOYkGTX1C5KD4ktNhrHvtVog-ZOQJ1HbeJhBorJpz71FXVsR6sFtjdLNjcGI-hjCUe6qdmwls9xBKImNPgC7rC-xutfviDfYyKLiSusTe4suc7JY9-s1F3ByTH0SndSe5RY6WNe3uHtuWRwWc6Gsc2cXVxcqQtVVPwxjg2v29B6_O_6gk3jvN6pvUmdKqXMbEiKy2vDdsz3QIr_tbTcEC5_oqb2_0Kb52ZNLflyWCEej2uKIlDNi_P4rcNNc9RE_Ow6vfhaI5I-OgPZ0ImuwxOWzj0S6Qe0BNxw6A_PKcnA8CaJ267lV4-8Rc2n2kWKOFxfl64UwFetaUUUJh8WabdUr_FooZwyckVpfg4VYyW95b2V7jYJOxDEvfqhcL8NwtoZqg5IF07n0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
لحظه سقوط یک جنگنده میگ-۲۹ اوکراینی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69865" target="_blank">📅 01:32 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69863">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=jkOvZs-u6hU3SxYJQNPbzwFY_RJ4r12vXtFoMUFsg13eicYElQSjOsLk_k0Gc2_jUitTooI0CCbqF7DyzVeU-Oki6LgHtdFQ5HmF8ufShErvJS9OZUYysXjKCmuDRXHnZAuEANxOG1mcoDbR0_V5xuuoK6Th423BWjKA7q-jOm3QzxB1C9PagoVHfbC7NP4qwv6p42rVd-mnWUhPpeE3Xl1h37xr9rnthRyJNj8dKMbijMMac5fXvITOWLAtUA_H-F_q95-uVzDHtME2XiflOBFyYidO90XkS5ZMgzq0JAeZTIOAWInQz9v10vJIltlbTzOeilmDLoBrlF113nAgpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcca7b928e.mp4?token=jkOvZs-u6hU3SxYJQNPbzwFY_RJ4r12vXtFoMUFsg13eicYElQSjOsLk_k0Gc2_jUitTooI0CCbqF7DyzVeU-Oki6LgHtdFQ5HmF8ufShErvJS9OZUYysXjKCmuDRXHnZAuEANxOG1mcoDbR0_V5xuuoK6Th423BWjKA7q-jOm3QzxB1C9PagoVHfbC7NP4qwv6p42rVd-mnWUhPpeE3Xl1h37xr9rnthRyJNj8dKMbijMMac5fXvITOWLAtUA_H-F_q95-uVzDHtME2XiflOBFyYidO90XkS5ZMgzq0JAeZTIOAWInQz9v10vJIltlbTzOeilmDLoBrlF113nAgpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
املاکی رو ببینید؛طرف یه ساعته داره جلوش گوه میخوره بعد این کصخل یجور لم داده رو صندلی که انگار تو تخت بغل ملانیاست
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69863" target="_blank">📅 01:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69862">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=b34SIecnCfHFOZWSKejpzpxNg0OXxWEbQvcKcK4Hn0hbi5L0SzGk8jVOqx_JGoxYJeGZQREfe99utHBFJc8E8SHLpuWUD5-1b5hFg3Qc2o-P2nFZEZk8UJbtpxA5jiYm_xKq0wRQeOgCk7J9P1qz-2m14TdzjiD0QejqQilel5de7Lmb4O6zsckwgoC7HescuAnHKz1ysWFV9JVTigG4oFs9EyYSUMBulQP9kqHwlaKbA-1JywPHSlFcmz2a0gp5LL8IqkT1BPObu1zsjMbj-abfGwgh1gCjohbR1Qd_vqNz3TpfO4XGT4lJu1HlsT3GYb2YyqjdTgA6DGsEl36CJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d1e744df.mp4?token=b34SIecnCfHFOZWSKejpzpxNg0OXxWEbQvcKcK4Hn0hbi5L0SzGk8jVOqx_JGoxYJeGZQREfe99utHBFJc8E8SHLpuWUD5-1b5hFg3Qc2o-P2nFZEZk8UJbtpxA5jiYm_xKq0wRQeOgCk7J9P1qz-2m14TdzjiD0QejqQilel5de7Lmb4O6zsckwgoC7HescuAnHKz1ysWFV9JVTigG4oFs9EyYSUMBulQP9kqHwlaKbA-1JywPHSlFcmz2a0gp5LL8IqkT1BPObu1zsjMbj-abfGwgh1gCjohbR1Qd_vqNz3TpfO4XGT4lJu1HlsT3GYb2YyqjdTgA6DGsEl36CJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: گفتید این آخرین فرصت ایران هست چیشد؟؟
🇺🇸
ترامپ: به زودی متوجه خواهید شد
ما توانایی افزایش تنش رو داریم
خسارات های جنگ رو از طریق منابعی از ایران جبران خواهیم کرد
خسارتی رو اگه قرار بشه کسی جبران بکنه این ایران هستش
هیچ اتفاق بدی قرار نیس بیوفته
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69862" target="_blank">📅 00:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69861">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=mGN4rgbKKvwWfUgr9jG-aBEcW8fkdsgcQMf2ss5IHQa0aQ9buUVWrHfZTahKJLx3fJcPpGuasIB5suPuYRpr_IUzf9P4qAu5qOp6S3rxOgP8h9nKSh7KwEH5QQyW4JkP2ezekV5hApVTr-w9PBJtFoJ03pMwVgNb3fNuf-tsZfzQtP2CXCT-NyBu-O101sTQWTo43y_JnAXFBQ8ZB26EAWUt84YBahojZzj6Tk-pMKd9YKUDmvBWue_ziECnKdhfRxxudOsshxu6urTUR5RUxtfaptbTGvp2RtfqnGIgRQcM68TN_YMm22iYndVqQBSLGdWnoeYRwNYvLSEuqNR8Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10abc62a6.mp4?token=mGN4rgbKKvwWfUgr9jG-aBEcW8fkdsgcQMf2ss5IHQa0aQ9buUVWrHfZTahKJLx3fJcPpGuasIB5suPuYRpr_IUzf9P4qAu5qOp6S3rxOgP8h9nKSh7KwEH5QQyW4JkP2ezekV5hApVTr-w9PBJtFoJ03pMwVgNb3fNuf-tsZfzQtP2CXCT-NyBu-O101sTQWTo43y_JnAXFBQ8ZB26EAWUt84YBahojZzj6Tk-pMKd9YKUDmvBWue_ziECnKdhfRxxudOsshxu6urTUR5RUxtfaptbTGvp2RtfqnGIgRQcM68TN_YMm22iYndVqQBSLGdWnoeYRwNYvLSEuqNR8Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
پس تنگه هرمز کِی باز میشه؟
🇺🇸
ترامپ : بازه!
ما صددرصد کنترل تنگه رو در اختیار داریم.
همون طور که احتمالاً شنيديد، كل تنگه رو مین روبی کردیم. البته شاید هم نشنیده باشید.
اونا میتونن دردسر درست کنن، ولی ورشکسته‌ان؛ پولی ندارن، ایران کاملاً ورشکسته‌ست. حتى حقوق سربازهاشون رو هم نمیدن، نرخ تورمشون 309 درصده.
ایرانی ها صدها هزار نفر رو کشتن، حالا دارن تاوانش رو پس میدن.
اگه قرار باشه خسارتی پرداخت بشه به نظرم ایران باید اون خسارتها رو پرداخت کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69861" target="_blank">📅 23:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69860">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
گزارشگر: شما گفتید که این آخرین فرصت ایران بود. حالا چه؟
🇺🇸
ترامپ: شما متوجه خواهید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69860" target="_blank">📅 23:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69859">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=W4iw4kISa7IIZ07wHeRuOsb6oe8xEz8-AY1pDM2m95gfHYzlRmNaH47Ekq9XTZCkVTh-XvDYFnY0c1cpBh-SuD2-RTeOz2lJ7eSp3ZE4EBoWg_Ln3HLHqB13Y7qvQYid8eM6plvxrbA2qGCEOfWNBeMXkGnrkuAE4oQjEo8Tv5laYH8zKcdSKB5I9aBxptAWiclx9-lHcUYKhum-0j5a3OMhgbPILkEfU64A29DHg14hAg6tO7dvTTetdB1IKU0X6OoyRYz-ZiLflbFV1RytAYV7Z0og60g6UF9htYijU29RCvL3WLSzVUXSSVKBv8BEsHsS3fqti573YIqSB74siA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8eb808fce.mp4?token=W4iw4kISa7IIZ07wHeRuOsb6oe8xEz8-AY1pDM2m95gfHYzlRmNaH47Ekq9XTZCkVTh-XvDYFnY0c1cpBh-SuD2-RTeOz2lJ7eSp3ZE4EBoWg_Ln3HLHqB13Y7qvQYid8eM6plvxrbA2qGCEOfWNBeMXkGnrkuAE4oQjEo8Tv5laYH8zKcdSKB5I9aBxptAWiclx9-lHcUYKhum-0j5a3OMhgbPILkEfU64A29DHg14hAg6tO7dvTTetdB1IKU0X6OoyRYz-ZiLflbFV1RytAYV7Z0og60g6UF9htYijU29RCvL3WLSzVUXSSVKBv8BEsHsS3fqti573YIqSB74siA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
🇮🇷
عظمایی فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی:
«اگر اسرائیل، ایالات متحده، یا هر یک از همدستان آن‌ها حتی جرأت کنند نگاهی خصمانه به جزایر خلیج فارس داشته باشند، با کمک خداوند متعال؛
چشم‌هایشان را کور خواهیم کرد و خلیج فارس را گورستان آن‌ها خواهیم ساخت.
»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69859" target="_blank">📅 22:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69858">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=HPoKsg0JxTu7q7OH01DwmoKBd8h_MdUNbTbFn0xy0H9kjhbqto7_YxEYvG6nns6lxd6OlhEic6B4gYP__JIoGHCtP7aNLoo1SNo9M543Ml_JDsc8CIzRpIvjsjHOdFEpOsijL8wtWG4aKo5oDsl0mrD_r0XEkyHKTDzWM7OrlSTqY5vvLigbIBqBFX4Af3Mv4Ik2JUDEXYltX9SFnalIWC5Znk6Vsoa9UIq-3yMHIvfT08YPEpxWFTzk8Cm1qDrxhYx4D6wKXCx-XmcR8oV3cSlvMh_EzVoabk9CxQgKL7n_yJCBN3W0aNWshE2oQbnNYPIsVjfl6LsuxLXIZEFr5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c15a39d1d6.mp4?token=HPoKsg0JxTu7q7OH01DwmoKBd8h_MdUNbTbFn0xy0H9kjhbqto7_YxEYvG6nns6lxd6OlhEic6B4gYP__JIoGHCtP7aNLoo1SNo9M543Ml_JDsc8CIzRpIvjsjHOdFEpOsijL8wtWG4aKo5oDsl0mrD_r0XEkyHKTDzWM7OrlSTqY5vvLigbIBqBFX4Af3Mv4Ik2JUDEXYltX9SFnalIWC5Znk6Vsoa9UIq-3yMHIvfT08YPEpxWFTzk8Cm1qDrxhYx4D6wKXCx-XmcR8oV3cSlvMh_EzVoabk9CxQgKL7n_yJCBN3W0aNWshE2oQbnNYPIsVjfl6LsuxLXIZEFr5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه مختلط تو قیطریه تهران همراه با استخر جکوزی سالن  ماساژ سالن بیلیارد سالن بولینگ و...
😟
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69858" target="_blank">📅 22:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69857">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGK9KsCn-BfdCUhqmf0qluLV1nWj0ogpIQRWaOhfq6R47uPBdo3l8QXeNF1fpZSDNZY8pEuxoJRfXERIzelSBm_yuqGKBtagDh6ylKDvqlHYncjg3gOW4wvADun3FvQHGpM-JWRVuQXAKdHYOIyxbP3tdAozQ-fTQkXTrVNwxKE4xaKjzRji0Eg3w0XJYljDYqUZBtyA13wmq7FhkSEvdj5nIbNLHTk0vs7y4OJRJeYtTmu4uH8R8BAITyYfzXNc6_nozzp7650HayCFhxmWWuRZL-JiYcu_sURaiyuBvIFPMypUNwIS2qvrOuhLpLuBJnGVHyP-zZ6yj4kdLUdgKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:   می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69857" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69856">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79470446aa.mp4?token=Gh1D3Awa34H_3Sh9QspAP4-ayqgXbk00ZwwUE2JlBRUMoQYtJhxeQaujaYO0tmK-kHUpK9at7UkbTOplFnpxonCm2grViA5QD6DnZ2ZjfdPyVEF6__RKaCg9jLHTp7QOJcrRMzOtEyTuzBelCJjOdRnoQHoDrpo5HzcxnhPoDBfW0m99zwMlKzf2pGk6IBhupMdehPTSowJPE5s7ySNXJOpHQ3e-ehzW-GKA3PkOetKIEXTfZzhvJBH40-jyqUPX3-jSx8eFiE01tvhGrpm1Yn7GKPsRPyW0gcG5pzRZYCf59ALUt0HnrZ-IAFdACFqIuccpfJvYttrEPp_CsJOW3WjNPSgiUKMOkBzAcv_YbOeP93xG_8zZUYGxYWCLHTBv6Tm_8F-HKBcjcHTtZ06wpdWUSqOTzlrEMcsf1OJUWK4WpqwnS0nNDxoWFMMINaphi3ZD5sbPvVRrLzRWYzp9XRlP92ILVtHWftGFBoZAbfJH0uuTICqgQmrO1Asnz34xoK9dFoYWzer0tIfaKdNZEZFTUywZbJShg4PvkswV1FRcawunILMJvc4WdMeWqGgeRmDjWJ28SLHU-nQBe1haDg0ooldnhO1QV8kIEpK4HAgcNrYO6ccZGfXb084RClA8r4gc0ekEkWcMPsg80wrzwleQJTjEsB1GJ7dU6hROskw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79470446aa.mp4?token=Gh1D3Awa34H_3Sh9QspAP4-ayqgXbk00ZwwUE2JlBRUMoQYtJhxeQaujaYO0tmK-kHUpK9at7UkbTOplFnpxonCm2grViA5QD6DnZ2ZjfdPyVEF6__RKaCg9jLHTp7QOJcrRMzOtEyTuzBelCJjOdRnoQHoDrpo5HzcxnhPoDBfW0m99zwMlKzf2pGk6IBhupMdehPTSowJPE5s7ySNXJOpHQ3e-ehzW-GKA3PkOetKIEXTfZzhvJBH40-jyqUPX3-jSx8eFiE01tvhGrpm1Yn7GKPsRPyW0gcG5pzRZYCf59ALUt0HnrZ-IAFdACFqIuccpfJvYttrEPp_CsJOW3WjNPSgiUKMOkBzAcv_YbOeP93xG_8zZUYGxYWCLHTBv6Tm_8F-HKBcjcHTtZ06wpdWUSqOTzlrEMcsf1OJUWK4WpqwnS0nNDxoWFMMINaphi3ZD5sbPvVRrLzRWYzp9XRlP92ILVtHWftGFBoZAbfJH0uuTICqgQmrO1Asnz34xoK9dFoYWzer0tIfaKdNZEZFTUywZbJShg4PvkswV1FRcawunILMJvc4WdMeWqGgeRmDjWJ28SLHU-nQBe1haDg0ooldnhO1QV8kIEpK4HAgcNrYO6ccZGfXb084RClA8r4gc0ekEkWcMPsg80wrzwleQJTjEsB1GJ7dU6hROskw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله تند مجری صداوسیما به علی دایی:
وقتی جرائت نداری جیگر نداری به دختر اونور آبت چیزی بگی پس اینجا هم خفه شو لال شو
یه گروهی گول میخورن میریزن کف خیابون بعد از این دایی و خاله ها زیاده هشتگ نه به اعدام میزنن
یکی از این آقایون مشهور دخترش مورد دزدی قرار گرفته بود کم مونده بود دزد رو بکشن بعد همینا هشتگ نه به اعدام میزنن
بعد این وحشیا این بیشرفا جوان مردم رو به شهادت میرسونن یه عده یاد حقوق بشر میوفتن
اعدام نفرت نمیاره شماها نفرت انگیزید شماها ترحم انگیزید
ولی یه پلیس یه گلوله شلیک بکنه داد میزنن عای دیکتاتوریه عای خاک خون کشیدن
شماهایی که لال هستید همیشه لال بمونید حتی اون ور آب
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69856" target="_blank">📅 20:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69855">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCryMxwQ7tObpVshmg39x4z9f_b1cC0oX_V7vZB5iEF1ZWcDnDG9IWCGs_agJHVd6ojkd4D9KMcjpuqYEogtvkiWM_QsvexZyPWge0hfd8GSEXtZuwoTHQiwuEKdDqxrBSAximumQdNMy1gaKPwwni2rbdp_kNjg5efEg8CguOjFvOs9Cl8LV0-VZR_k18HAYLAjf9vJd6IHAJuWaIpr8BFtscjL2nwlZO8vd7kl1UBVFkqUwv6eHpOW7x18U9QmvvXQgpBITtZ89tgcKQHxefcPtv-jG-Xtoz05X9qp4LcjpLL02_p3dwX-wzzE5K47zHZxE6HC9JAaCiCTwmz8AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ درباره ایران:
می‌بینم که نمایندگان جمهوری اسلامی ایران خواستار غرامت بابت خسارات وارده به خود در جریان درگیری نظامی پنج ماه اخیر هستند (درگیری‌ای که آغاز شد چون آن‌ها نباید به سلاح هسته‌ای دست یابند)؛آن هم در حالی که این موضوع هرگز در هیچ‌یک از مذاکرات یا دیدارهای ما مطرح نشده بود!
اما این ایده جالبی است، چرا که من نیز اکنون متقابلاً از ایران درخواست غرامت می‌کنم؛ غرامت بابت تمام کسانی که آن‌ها با بمب‌های کنار جاده‌ای و در درگیری‌های متعدد — که به آن شهرت دارند و در ابتدا تحت هدایت ژنرال سلیمانی انجام می‌شد — به قتل رسانده یا به‌شدت مجروح کرده‌اند؛
از جمله خانواده‌های کشته‌شدگان حادثه ناو «یو‌اس‌اس کول» (USS Cole) و هزاران نفر دیگر که در میدان نبرد جان باخته‌اند. به‌علاوه، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران طی ۵۰ سال گذشته به قتل رسانده نیز غرامت پرداخت شود، چه رسد به آن ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
من به نمایندگان خود دستور داده‌ام که این موضوع را قاطعانه در تمامی مذاکرات آتی بگنجانند.
از توجه شما به این مسئله سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69855" target="_blank">📅 20:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69854">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OK_eBfezN-S2CSFTnQqIh1KjMQsiaJVIsSKclEc82Lci7wshmeNK4ooxbBhPIYIw4UohNWbRnCmoAnvrLyY9G5dJZwrYKskCZBJgFlkJnIraX2f3qS61P-sQks6evCHZEpqtrgSNISeOBK77DzuG0-v4bxCP36zo4vSEElxKHJr0Vw50AxyXf8OlOgGDrD_KnK7Itm-qzsQObE9TK3VJLjqA2gFw6Pxc_uAYWJwtOktfuHISvUoKoEyElCKywj4Os0-VGbfb6nd9lh9u1uHxZaoUcdkZm0iNBa9Xt8A4bekZePWJi7p1o9RsVHYrlelrQqhwhURSkSQ8ifvh-D46NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
مرندی:
‏ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه - احتمالاً در کنار نیروهای اسرائیلی - علیه مردم ایران هستند. جمهوری اسلامی با پاسخی سریع و کوبنده آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69854" target="_blank">📅 19:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69853">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🔴
🇮🇷
لیست فرماندهان جدیدی که مجتبی خامنه‌ای انتخاب کرد:
سرلشکر  علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح
امیر کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح
سرلشکر احمد وحیدی به عنوان فرمانده سپاه
سرلشکر مصطفی ایزدی به عنوان جانشین فرمانده کل سپاه
حجت الاسلام طائب به عنوان رئیس سازمان بسیج مستضعفین
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69853" target="_blank">📅 19:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69852">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=It_13FwSqKyrHTo8uYbUc-TJVtr1yp2lFI4OLUGFvLTpKktNLQ9G5e0CDwHEQAIegBaffYF1dYmzEHFuGna8LmrtM5m-k19JvfUxup1p8GTR7q6UuvJNpJYEdOjQa25SQxlK7yQpckWEMbhhME06GAi6yOKXbLeVC12VDSN38XymjkQuOEQjohJYEKupcYyL0RDlNb41HRWprohyRMA3l62ApE2ipHTQrG12NgrTn0FQVEZRG6m6jOisGa2I6BvDw3CEqCk97VAjZwbz25rHzhrXCwRbgyVvPrHCZSmPsg_rl4-lj9keUZcP72cc8hoptqYVXu6SV6iSaP-pi8kvSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f1723f2a3.mp4?token=It_13FwSqKyrHTo8uYbUc-TJVtr1yp2lFI4OLUGFvLTpKktNLQ9G5e0CDwHEQAIegBaffYF1dYmzEHFuGna8LmrtM5m-k19JvfUxup1p8GTR7q6UuvJNpJYEdOjQa25SQxlK7yQpckWEMbhhME06GAi6yOKXbLeVC12VDSN38XymjkQuOEQjohJYEKupcYyL0RDlNb41HRWprohyRMA3l62ApE2ipHTQrG12NgrTn0FQVEZRG6m6jOisGa2I6BvDw3CEqCk97VAjZwbz25rHzhrXCwRbgyVvPrHCZSmPsg_rl4-lj9keUZcP72cc8hoptqYVXu6SV6iSaP-pi8kvSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇫
طالبان به طور رسمی برده داری جنسی زنان رو قانونی اعلام کرد تا محدودیتی از این لحاظ نداشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69852" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69851">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🙄
همه بت باز های حرفه ای دنبال
🔞
شکار این بونوس ها هستن
✅
لیگ های معتبر اروپایی شروع شده بهترین فرصت برای جبران ضرر های جام جهانی
💯</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69851" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69850">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma1jFYgjMZ1v0HZhCD6qEZuezlQQ6i5IODLTZ4mV9hiJMfEsB_APTkXC4smrS65DXFAQrmfFl4Qae6HqITi6vFn1UPlsU2yZn5Z8DPg3McaJMNbKw159ZSqYeU95ijmny-keViwMTCcs5P-vuZTJ2XwvBEnpjzcG87rrNXVDx9yhJIbOen0pmd9WZk9x7RcjPLJf_NMpvx_yp2l8hsN-XN-D9EzDzoOupIPnoRT8UiSgcz-ggErKea8G-E0b3pY7EgFzoKsuUGEW4jOCVIqtp4qKPQW8uWJqhnQOYFDQNV3ASs94LA32Xgzo1wDL1NCrnQdtZLBW6pWSAqSYZpLy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤔
شروع رسمی لیگ های اروپا
❄️
🆕
بهترین فرصت برای جبران ضرر های جام جهانی با جشنواره رویایی مرداد  ماه
⚠️
هر افزایش شارژ مساوی
2️⃣
1️⃣
🔣
شارژ بیشتر بدون محدودیت
☄️
به همراه
🤩
🤩
🔤
کش بک باخت همه روزه:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g19
@betinjabet</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69850" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69849">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
⭕️
مجتبی خامنه‌ای تا ساعاتی‌دیگر اسامی فرماندهان جدید نظامی را پس از بیش از ۵ ماه رسما اعلام‌ خواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69849" target="_blank">📅 18:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69848">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=F_9-gcadp_eQt6pOLIl1twy5kQPGlokLvXlr5N_OIRum7ktMW7MvQUsVCJ8tk5u9VvTVtDB_-IJUu7yVXfIop-ZSUnisxW1iLV4nsyTcY8JNpSwxC3FWhnLltZ_G5AdGZY6qr_9HLWsYeu9bA9Y4XnK790a7jpHWoGRaQziLtMlWErmBKZMrzMljIlmTpAgRyoe0a2KE2RCpXD_ueFOKG5louD7vtuY57jdC-lTosxSESdoUxmGtyBz519Mr5I1Vj2Ll0rrc_uO73JnCnEec3zPwIiv-BtWcTvNpDJJXhVzoRjjR1S6NixOrgdry0jquifx_zKQYmgTYe-1hHU30gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a2288e087.mp4?token=F_9-gcadp_eQt6pOLIl1twy5kQPGlokLvXlr5N_OIRum7ktMW7MvQUsVCJ8tk5u9VvTVtDB_-IJUu7yVXfIop-ZSUnisxW1iLV4nsyTcY8JNpSwxC3FWhnLltZ_G5AdGZY6qr_9HLWsYeu9bA9Y4XnK790a7jpHWoGRaQziLtMlWErmBKZMrzMljIlmTpAgRyoe0a2KE2RCpXD_ueFOKG5louD7vtuY57jdC-lTosxSESdoUxmGtyBz519Mr5I1Vj2Ll0rrc_uO73JnCnEec3zPwIiv-BtWcTvNpDJJXhVzoRjjR1S6NixOrgdry0jquifx_zKQYmgTYe-1hHU30gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان درباره مجری و کارشناس‌های برنامه به وقت ایران:
این همه علم رو از کجا آوردید؟
چندتا جوون نشستن رو صندلی و درباره اقتصاد، سیاست، جامعه شناسی، کشاورزی و... نظر میدن.
از چهارتا جا یسری اطلاعات ناقص می‌گیرن و بعد درباره‌اش حرف میزنن و نسخه می‌پیچن و جامعه رو منحرف میکنن.
من 18سال تو دانشگاه درس خوندم و استاد تمامم، الان فقط اجازه دارم درباره یه گوشه قلب که تخصصمه نظر بدم نه کلِ قلب، اونوقت اینا...
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69848" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69847">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=FAHAj_pAzQuphV85Y2JI4nH6GISaPC0ndzcZbWMJyKVDPCmmD2UOpfpjqG45AOvIRD7GYMlaVCSxYAHcMVYmCXvkEAwL50Gb7uMrJORbiBdC0RjKxjLLc52KLzKaml5JIPv40YS9-rfMB-WZbSwElpfOqknucYDBOeEfxxwBHNr5PuncJYaq3rpNRcL1eZ7nV9m8IjY9HLiWJ1Kof70k3-IOir4ZYJQUBYPchBfwLYr9ERbE-SHDZp2WL4QmUik8jynsbkAf3iSl2LE0xzgnTtfHmD47uSrusB3pJkoTuryyirQqi-pQl9nx7YphJYzUEktMqr4nk8V9Frpiiwfr1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7c4253089.mp4?token=FAHAj_pAzQuphV85Y2JI4nH6GISaPC0ndzcZbWMJyKVDPCmmD2UOpfpjqG45AOvIRD7GYMlaVCSxYAHcMVYmCXvkEAwL50Gb7uMrJORbiBdC0RjKxjLLc52KLzKaml5JIPv40YS9-rfMB-WZbSwElpfOqknucYDBOeEfxxwBHNr5PuncJYaq3rpNRcL1eZ7nV9m8IjY9HLiWJ1Kof70k3-IOir4ZYJQUBYPchBfwLYr9ERbE-SHDZp2WL4QmUik8jynsbkAf3iSl2LE0xzgnTtfHmD47uSrusB3pJkoTuryyirQqi-pQl9nx7YphJYzUEktMqr4nk8V9Frpiiwfr1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی (1392):
اگه آمریکا به ما حمله کنه ما همون هفته اول هزارتا آمریکایی رو اسیر‌ میکنیم و بعد در ازای آزادی هرکدوم چند میلیارد دلار از آمریکا پول میگیریم و اینطوری مشکلات اقتصادیمون هم حل میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69847" target="_blank">📅 17:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69846">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=EOQziuA5jLhDe3I5A0FlQkMPPtNKOw74xOI4xHOwewnIgdDdnUScOmPsSK3Zwp76pImSjCU1CKOAeVK6LefHcR-XqYec-5LA7Hv0jwrSgw_nMq2c1Ak7FzQkFKQcQY8y49W-8aySsejUVEa5qOx18_IeIhtpv4u6wZA82a8XI-qAwdg5-snnNbweqUzPyvLwMym23G29HiD3zgE5svZ2Hmf6d2DqfXyOUzTzdOr-0vhV4sZ1PU9dNbbzptvHX46U78fWbz6Mk5s8f_Oi10M0yCAoCFwPqmFvqgQqOmybazBupeA6NzWgltaa6k_s1QsfX3CFmgYxEet3HaP4c_Bg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77b47958b9.mp4?token=EOQziuA5jLhDe3I5A0FlQkMPPtNKOw74xOI4xHOwewnIgdDdnUScOmPsSK3Zwp76pImSjCU1CKOAeVK6LefHcR-XqYec-5LA7Hv0jwrSgw_nMq2c1Ak7FzQkFKQcQY8y49W-8aySsejUVEa5qOx18_IeIhtpv4u6wZA82a8XI-qAwdg5-snnNbweqUzPyvLwMym23G29HiD3zgE5svZ2Hmf6d2DqfXyOUzTzdOr-0vhV4sZ1PU9dNbbzptvHX46U78fWbz6Mk5s8f_Oi10M0yCAoCFwPqmFvqgQqOmybazBupeA6NzWgltaa6k_s1QsfX3CFmgYxEet3HaP4c_Bg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی سمه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69846" target="_blank">📅 16:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69845">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=kke_YsYQ3hmJpx_EUfyBazUDNqUsQWtC7A1MVlZxTTfGgCLZMxf008GCf7SSJCperflz4uFWEa3RIpraxFt8lNEqCCu4cAuZVoW6d_ZwbnQ9hAQa5tK8rMncBYex3vX62XXzpLClVujBkIq1gNSKM1BxaNEtMydYCcptVue6gWj8rkZ7rvBpcqEKq6wCTQK7SfEE9cyHDcTjdEdqiK5xZSqlLEqNScAkYwSN6iqE7ED8dQVLhyLXlhtBSVrsbBSvet9Gv7W4ge7mutVcWwuygDyG7uW-oLJKopHWVQ4QDx8T_EenTviTyJJGbVr0x2AL-vD2rzatBhJDxx5VPimJJj35FEJ9NSNocPyqCohsIS9z3JYhPPDZ9zkfMDdy7MjgQxn3Ag_IeIqfpF6-Pqr1rmVtmiMnM3brn__mAp0WIxmmAc4tiE0h6eoZ6GbKAVmqwOXFQWHo7_q_yNsBZPTO4pojvb9x0RlZGrSFyEekjt7rtcdnncTtDsUDE6wquwqfuGff2KcJDp5yPcWG3cqOMrkpXAXibQVNWUaOWUDXdBZxR4NHBds4ZJFORPj2CpXJX6gzr16VqFQjcVOvjnRDmPkRSWZqD7mLSiz2qQcs6IqCxaJIH62p0iZj1hS-JhxD6VKyWyokKKsO5Wr_oWZuPcO_VU3PlaB2shCfo277-Oc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=kke_YsYQ3hmJpx_EUfyBazUDNqUsQWtC7A1MVlZxTTfGgCLZMxf008GCf7SSJCperflz4uFWEa3RIpraxFt8lNEqCCu4cAuZVoW6d_ZwbnQ9hAQa5tK8rMncBYex3vX62XXzpLClVujBkIq1gNSKM1BxaNEtMydYCcptVue6gWj8rkZ7rvBpcqEKq6wCTQK7SfEE9cyHDcTjdEdqiK5xZSqlLEqNScAkYwSN6iqE7ED8dQVLhyLXlhtBSVrsbBSvet9Gv7W4ge7mutVcWwuygDyG7uW-oLJKopHWVQ4QDx8T_EenTviTyJJGbVr0x2AL-vD2rzatBhJDxx5VPimJJj35FEJ9NSNocPyqCohsIS9z3JYhPPDZ9zkfMDdy7MjgQxn3Ag_IeIqfpF6-Pqr1rmVtmiMnM3brn__mAp0WIxmmAc4tiE0h6eoZ6GbKAVmqwOXFQWHo7_q_yNsBZPTO4pojvb9x0RlZGrSFyEekjt7rtcdnncTtDsUDE6wquwqfuGff2KcJDp5yPcWG3cqOMrkpXAXibQVNWUaOWUDXdBZxR4NHBds4ZJFORPj2CpXJX6gzr16VqFQjcVOvjnRDmPkRSWZqD7mLSiz2qQcs6IqCxaJIH62p0iZj1hS-JhxD6VKyWyokKKsO5Wr_oWZuPcO_VU3PlaB2shCfo277-Oc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
تنگه هرمز از زمان حضرت آدم تا ۹ اسفند برای همه باز بود
ادعای ساخت سلاح هسته‌ای ایران توسط نتانیاهو دروغی بیش نیست
به ترامپ بگم که ایرانیان شطرنج بازان حرفه‌ای در طول تاریخ بودن( ترامپ جنگ ایران رو به شطرنج تشبیه کرده بود)
هیچگونه مذاکره مستقیم با آمریکا نداریم
باز شدن تنگه هرمز منوط به لغو محاصره دریایی هستش
نگرانی بابت پیمان دفاعی مکه نداریم چون همسایگان ما هستن
بحث کنوانسیون دریای خزر به مجلس ختم شد و تصمیم نهایی با اونا هستش
درباره عمان نزدیک به یک تفاهم هستیم و به زودی نهایی میشه
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69845" target="_blank">📅 16:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69844">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=KnUvsHsx1j4p52TOcjZ7WE6W81c1u7suQHaimkSisk3Z5Rj_gX2nFJ_2tJd5oM5-80-Ez5ub9iIfGMoY2iAye6-8g572LYjENnknsLx7ElVTSt-ZrmNroyebr6Tx0UzHOcN0h_LpjZx_VhustaDb8lu80dDE2tJnZTs2FW24fJRYYpjYqYdDk94jD1WH7FeodScMKP9BfO2SgEXIV_SxzPUW08gEbzjdQKme40B1PDdJGQKEabJn3JvlIm6uIJsGZ-6PPFWKl23IAGFWWOI7zRId8Ykn8cZyaapmxU4BXBsvKE-0uZEaEkBeLo8D52r3Kt7pm_ug201dFWZky_waozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c431777b9a.mp4?token=KnUvsHsx1j4p52TOcjZ7WE6W81c1u7suQHaimkSisk3Z5Rj_gX2nFJ_2tJd5oM5-80-Ez5ub9iIfGMoY2iAye6-8g572LYjENnknsLx7ElVTSt-ZrmNroyebr6Tx0UzHOcN0h_LpjZx_VhustaDb8lu80dDE2tJnZTs2FW24fJRYYpjYqYdDk94jD1WH7FeodScMKP9BfO2SgEXIV_SxzPUW08gEbzjdQKme40B1PDdJGQKEabJn3JvlIm6uIJsGZ-6PPFWKl23IAGFWWOI7zRId8Ykn8cZyaapmxU4BXBsvKE-0uZEaEkBeLo8D52r3Kt7pm_ug201dFWZky_waozzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
پزشکیان:
با رهبر هفت ساعت دیدار داشتم و درباره مسائل مهم کشور باهم گفتگو کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69844" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69841">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoXM7uAIPKWnnJV7kjQW8hMca-z-AlgJpAVNmtxWuxM9MtADB0on14rIA6Ak0JjnG4z2rVGRzXH52x8iIi5jYOdsrJuArJMfpLhgCmH9u341txSEsp2gwmcFO9IxJwRcpnXPTtm7LZlxbRfso45z8MYbyir7pVrEJGAJH8z6BTDz_usamzjqG6d9e0uBTX762AfxAR4B7SxHFKQQEmTImkoFE68ZxW2TWK9Dszxvwo6vL4Zw7PZeZNJvQzuyNoFKthhDwnOJ9O8SAxGIl2IYp8bJ8eqMIokx4y7tGBKzMLlrVpWZXjEwYu0A0XHkaDBBZffhCCxFp0UZNyAhV1uJmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hkp4VEIBKoteS2SnEHcbYBSSejS3XPo2YWFEgHopIuHC0epyDgxmfAlFU4bqIKWMudW7SI3De3i9dUfhRzrV_qqf1CO5X4nz7h13PvOH0Cu5ih4kK3WCwkSpF8LBgKwCxRg4QshHwyxGMszfB0VR7CjLRD4sP3OXCNPFbLM9hJvF6qSY_FPh0DamO9HuHZTasp4LZxq4Nl2qZbdk-Hkq_d1V5k0wGnNG-5JmYWV49rMLcgGvOzC5YqLNrm-PPd4p-8Fw6RRAAWLmV-Aed1qKisvaLSmK1H0wSLU52Kcqk96cxbe_wu2Mq8uC28UhT4fg9NGHtUrpvZr-y4CXo-yN_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92217bf769.mp4?token=bY_I45_3kvcW3Y_bjHyf13eeChim9xpxokGOAip9-7TMPY77o7aBMMqLH6DeMhIq_YDkbzOSXqT2lCgKFMyTQVOr7XSQGFwM_3OCD7Hxkfi8e_n5U52kezWJXOsdri5IaCVQtx0AbsyQj2y49XKTSJ1_H3J5yLRcCZMD7OpVxeP59YXSF7DE0kG01yxYDwrbi-12MP22IIH81Iq_rl98sDE8rzVq9ramAPyhRsNeuO01j8UYWf0Jhe8o8VZ1U5yPtxqcglnPlq1M3bi3wG3RLU5e0CuoaXrvrDlA46DrVfANZ7MXMhyeEothJNvoJZ11W6Vg6I2Kfi5Vd615tqLjBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92217bf769.mp4?token=bY_I45_3kvcW3Y_bjHyf13eeChim9xpxokGOAip9-7TMPY77o7aBMMqLH6DeMhIq_YDkbzOSXqT2lCgKFMyTQVOr7XSQGFwM_3OCD7Hxkfi8e_n5U52kezWJXOsdri5IaCVQtx0AbsyQj2y49XKTSJ1_H3J5yLRcCZMD7OpVxeP59YXSF7DE0kG01yxYDwrbi-12MP22IIH81Iq_rl98sDE8rzVq9ramAPyhRsNeuO01j8UYWf0Jhe8o8VZ1U5yPtxqcglnPlq1M3bi3wG3RLU5e0CuoaXrvrDlA46DrVfANZ7MXMhyeEothJNvoJZ11W6Vg6I2Kfi5Vd615tqLjBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
دیروز عراقچی برای مهمانان خارجی تو ساختمون وزارت خارجه بساط تعزیه راه انداخت
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69841" target="_blank">📅 15:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69840">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=tr7my-_XCeqCDW6GFM9Z5s6ImAa6UJ3p8eMwGK8y6B6ckP5QzpJl-P--5UuuHPHt4KRZCx0DUKVMZzwjxmMKGbwDaHmEhs6JsyUWR_UvRP4Xa1EKZ9JcaDmwGa0B3d7qMhb3jq7Aj-Uv8eCyDAuCJfGCODXQAaAM0M4-42eZLk00rGknR_EbcWli6pG_sHCpq3-G119EEIZEpkkZVtaIpFpURQSe42-QEtVr10Hm7OitkrQsGGntWvI0Be2NjV3MWEMgfPigHWStKYoAY7uDV9-bIuyvw__cDwBf-zXSBTmLGs2RWCXwLd8551hInTsIAVJlbRfufxjmQS2fs8radw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7709b161ed.mp4?token=tr7my-_XCeqCDW6GFM9Z5s6ImAa6UJ3p8eMwGK8y6B6ckP5QzpJl-P--5UuuHPHt4KRZCx0DUKVMZzwjxmMKGbwDaHmEhs6JsyUWR_UvRP4Xa1EKZ9JcaDmwGa0B3d7qMhb3jq7Aj-Uv8eCyDAuCJfGCODXQAaAM0M4-42eZLk00rGknR_EbcWli6pG_sHCpq3-G119EEIZEpkkZVtaIpFpURQSe42-QEtVr10Hm7OitkrQsGGntWvI0Be2NjV3MWEMgfPigHWStKYoAY7uDV9-bIuyvw__cDwBf-zXSBTmLGs2RWCXwLd8551hInTsIAVJlbRfufxjmQS2fs8radw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وایرال شده از قیمت یک پک آرایشی که ناقابل سه میلیارد
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69840" target="_blank">📅 14:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69839">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr7lFUWdxmQmfiUh0dyFkwE9scOU7dxW6LF62Jz-oqazQb88ib1l9Y5a7s9ot6v6cDjbB3C3FStDYUmnoaP_Nyi1RxGZGWC_JoiEgJtqJTCByz8EINqHNP5y_Bfbw1VEoagTdkgx3ppFmSCx7VF7VSG_BPC2FQaRivtRGckZHlgGOUZHgd-MMhsehNjdMSdHdD7jzFmrv58b4vmcFzhUlZA-glf7OGrqtu3uw6rw7HQVfza2fl4HeM-mw-hPaT9MVCe_gdxFREWAoqs09y6n9vqhJOKFmXonzFJaPZTifczkJn4Hy0MiNZam3ivevOqgWvgRHfRdyb3EdN3M7WCgIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
یک مقام ارشد آمریکایی به من گفت که کاخ سفید از اظهارات نتانیاهو درباره طرح غزه «ناراحت نیست» و آن را بخشی از فضای انتخاباتی اسرائیل می‌داند.
این مقام آمریکایی گفت: «ما نیازهای سیاسی "بی‌بی" را درک می‌کنیم. تا زمانی که او به انجام آنچه ما می‌خواهیم ادامه دهد - به‌ویژه در خصوص مهار حملات به غزه - مشکلی با این موضوع نداریم.»
به گفته یک مقام آمریکایی، نتانیاهو هفته گذشته در تماسی تلفنی با جرد کوشنر، فرستاده رئیس‌جمهور ترامپ، وعده داد که علی‌رغم تردیدهایش، به این طرح ۱۵ ماده‌ای فرصت دهد و حملات به غزه را محدود کند تا روند خلع‌سلاح این منطقه بتواند آغاز شود.
از آن زمان تاکنون، اسرائیل حملاتی علیه غزه انجام نداده و ارتش اسرائیل (IDF) به‌تدریج در حال عقب‌نشینی به سمت «خط زرد» است. هم‌زمان، آمریکا و میانجی‌گران خواستار آن هستند که حماس روند خلع‌سلاح را آغاز کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69839" target="_blank">📅 14:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69837">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=UVzA_RetuCpGnPXxpzt3JfRzrbtxf8orQasopgzKaGqKMFQdcjlq5WabIXCTn5FNq-IO-lrHoJ9K_hEDLj7ntctHj4kUVUEZleHGcPXm8--VN1Zy7C2iJe-aoEnojEIb7eyrXhYdzxmUQ69lPlEc9JshqjGahQ_ymoED9hNs_Xlj5ZSwAPwouKzlcOTikCZts4cheses0hxrOWyBqu8rGqVMXSkZ-HkrtyamgCjDpEzshgUzI7PYaOLh9k2itYxiTQ9gVBmISPM0SxruDNe9jj5tELBB_iNFzxBHdQJ-6EudZ34O0IeYcMUfSUTGiwSEu2VHbJQm66RQztJCxFvd8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d242d991d.mp4?token=UVzA_RetuCpGnPXxpzt3JfRzrbtxf8orQasopgzKaGqKMFQdcjlq5WabIXCTn5FNq-IO-lrHoJ9K_hEDLj7ntctHj4kUVUEZleHGcPXm8--VN1Zy7C2iJe-aoEnojEIb7eyrXhYdzxmUQ69lPlEc9JshqjGahQ_ymoED9hNs_Xlj5ZSwAPwouKzlcOTikCZts4cheses0hxrOWyBqu8rGqVMXSkZ-HkrtyamgCjDpEzshgUzI7PYaOLh9k2itYxiTQ9gVBmISPM0SxruDNe9jj5tELBB_iNFzxBHdQJ-6EudZ34O0IeYcMUfSUTGiwSEu2VHbJQm66RQztJCxFvd8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فوران یک آتشفشان قدرتمند در جنوب غربی کلمبیا
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69837" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69836">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=sfAuPYAHEdVG8E6nR9ccyTNrFnKXBBUJB-rjwP7oZibScrdWr24shy1c81_978FW4ivpLtFbT9Hdu20asFVgRN9xdprdedwf8jhnlCjaoEis5vhbtjnAltrirJsto30c57EJPXN6bBS6_L-qaa86KUFOb0OAYVzlVEt3rTK2xYR78JNMa4dySpBDyl_Fda95HaNApCzZpv7YUJ5Rp3iIybUznA8na-bio1cP37JEi3zs8IfjTuEsO-e-_x8On_vdYBramprIZD-ad7uBvdi1s2Qn1R6S8ErEmiJIXOfBa5sddG2E-ZWdMMT6Q8XSQCUrg3BnFEBBe0iceZFTtSe-Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81027c9c4b.mp4?token=sfAuPYAHEdVG8E6nR9ccyTNrFnKXBBUJB-rjwP7oZibScrdWr24shy1c81_978FW4ivpLtFbT9Hdu20asFVgRN9xdprdedwf8jhnlCjaoEis5vhbtjnAltrirJsto30c57EJPXN6bBS6_L-qaa86KUFOb0OAYVzlVEt3rTK2xYR78JNMa4dySpBDyl_Fda95HaNApCzZpv7YUJ5Rp3iIybUznA8na-bio1cP37JEi3zs8IfjTuEsO-e-_x8On_vdYBramprIZD-ad7uBvdi1s2Qn1R6S8ErEmiJIXOfBa5sddG2E-ZWdMMT6Q8XSQCUrg3BnFEBBe0iceZFTtSe-Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشتیبانی سنگین و فوق العاده از نیروهای زمینی آمریکا در جنگ افغانستان ( طالبان ) توسط بالگرد آپاچی ۶۴ با توپ ۳۰ میلی متری M230 Chain Gun
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69836" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69835">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=mH6wzoQLqyO3H2yZqeDY7IEySk-dEf5eow7Xm04Ha2ev7ENjmuMB20FRa06HDBeZGedZ0yGbrLmPZwqs8WdHO3K4xJddT8UqLWLMJYieAOEQ9O_ojZLZsK3a0l1r4PQIz4TsJMcITpLe1M8DHwcLg7oPKenSlB7a7nEDEw_D8Lbkrd8EFbHabmes-kJIdXV44mCvZH7FBlpUapbwlYqthSRDvXavh36-jNRu3-4SvbJnIKlNFW05LDNnYOBFQBjIVV0lwdCi6cg4aXWDIRDLjE4I7mUGwg1CdfZwbZ_XPz2aoG5t3KIZQ-ajKAZW8bE14-VI-xdrHUip8FYgk-IfRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea33d827b.mp4?token=mH6wzoQLqyO3H2yZqeDY7IEySk-dEf5eow7Xm04Ha2ev7ENjmuMB20FRa06HDBeZGedZ0yGbrLmPZwqs8WdHO3K4xJddT8UqLWLMJYieAOEQ9O_ojZLZsK3a0l1r4PQIz4TsJMcITpLe1M8DHwcLg7oPKenSlB7a7nEDEw_D8Lbkrd8EFbHabmes-kJIdXV44mCvZH7FBlpUapbwlYqthSRDvXavh36-jNRu3-4SvbJnIKlNFW05LDNnYOBFQBjIVV0lwdCi6cg4aXWDIRDLjE4I7mUGwg1CdfZwbZ_XPz2aoG5t3KIZQ-ajKAZW8bE14-VI-xdrHUip8FYgk-IfRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پرستار از اتفاق عجیب شب زفاف یه زوج میگه:
ساعت ۴ صبح یه خانم با خون‌ریزی شدید به اورژانس منتقل شد و اول فکر کردیم
سقط جنین
اتفاق افتاده، اما بعد مشخص شد مربوط به
شب زفاف
بوده.
خون‌ریزی اون‌قدر شدید بوده که مجبور شدن بیمار رو
جراحی
کنن.
⏺
پرستار توصیه کرده زوج‌ها برای اولین رابطه عجله نکنن و با آرامش و احتیاط پیش برن تا به این روز نیافتن
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69835" target="_blank">📅 11:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69834">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=OcguwEt13kKmmO8C_jcXEHSAzW0BpGfSSS9PB-E6wx4s0ZkKa2Qoh8i5F9Hn1A0zW5SdEKbsUptXjEW0BdARFfok4dKVQfs1nR6tz-1cm3nUc4Xw6tbTrvz-XsF50A3nU_bZMwXcZ-61JDxU1xNJmU8Q26u5nSaeLSvMnKOk_gihzLC_UGV57o5VFz8Z1SeYtyLsFyHZxGcvbpw2ReaGOqqLMlSkKywq_UZNBvmzT_RtSjkQ1pG3AcNa82rDEWTkjf0B09WH7SksTVbLA9guWfK7bFvLIw-0CHIEheDMlnrlG1CZX6z4dL2OM0AsFllTVC7dtNqvVUCGE_YE0sILQl3RGfXDFkxgF3kCFJL3ACNxEV5_k6VVah8Us0VfWG5wFfB7ZrA--usNpVLvFoHd7f3XSlV0wpoWNuEuXLwev1LFj_6dO-dBoHySK8uLzTPqQcNszd9WWA0wEMQ2Kgrfl47pHb1J4PIAxqiFEWJlEqJqdumpb7pEWlfSyRwfPWiwREAUuf8gwoRNei4c8IcVu3z2tt9yCXJzGFIN1L4OH5iWbJ7D4uoYeVl-JUVuDjxPgJP11QDomklv2P8pBG9n93OhtfB9AwSTpFd0ZZoHvEqvm6TBpoPvZMvzz5B9Oi-VfkmA5GYyW7qUMB6aHdIu8IVlc2-N6-5jNIG5sDH37Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53aa49426e.mp4?token=OcguwEt13kKmmO8C_jcXEHSAzW0BpGfSSS9PB-E6wx4s0ZkKa2Qoh8i5F9Hn1A0zW5SdEKbsUptXjEW0BdARFfok4dKVQfs1nR6tz-1cm3nUc4Xw6tbTrvz-XsF50A3nU_bZMwXcZ-61JDxU1xNJmU8Q26u5nSaeLSvMnKOk_gihzLC_UGV57o5VFz8Z1SeYtyLsFyHZxGcvbpw2ReaGOqqLMlSkKywq_UZNBvmzT_RtSjkQ1pG3AcNa82rDEWTkjf0B09WH7SksTVbLA9guWfK7bFvLIw-0CHIEheDMlnrlG1CZX6z4dL2OM0AsFllTVC7dtNqvVUCGE_YE0sILQl3RGfXDFkxgF3kCFJL3ACNxEV5_k6VVah8Us0VfWG5wFfB7ZrA--usNpVLvFoHd7f3XSlV0wpoWNuEuXLwev1LFj_6dO-dBoHySK8uLzTPqQcNszd9WWA0wEMQ2Kgrfl47pHb1J4PIAxqiFEWJlEqJqdumpb7pEWlfSyRwfPWiwREAUuf8gwoRNei4c8IcVu3z2tt9yCXJzGFIN1L4OH5iWbJ7D4uoYeVl-JUVuDjxPgJP11QDomklv2P8pBG9n93OhtfB9AwSTpFd0ZZoHvEqvm6TBpoPvZMvzz5B9Oi-VfkmA5GYyW7qUMB6aHdIu8IVlc2-N6-5jNIG5sDH37Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون هم اینطوری انتقام قتل حمیدرضا رجب‌زاده رو گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69834" target="_blank">📅 11:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69833">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=ZFgCIOMaGnm3KDxDV6_XGwoacr9NE8bWuy1Ip1gESExySg0t_neOuuvfQ6Ie4qFfiiF7DJDNH24eZeT4rDaW8wkueNtf0B8rEDIent5-QxzZBf835_Cusl8gpDGZRtUWYoleT3PmCpX4VdgRn3Yfw0zx_biUmF64c6jc6V-B3LmQoKWZycU5ZT9HzQv6CVeXb0BORES2PK2V2Lqt15dh-XFjZst2bbY4oDnfrBCnLQkwUDfDx4RXIv_OUvqb8vNgUVbBbAc5glEpPJOPqryFbp7_v_EN1NXeODVGlYVI4jOb6jdIXz7ZNdtvFZeSQeYEfzxgXh59rCyOEIFq91vpqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=ZFgCIOMaGnm3KDxDV6_XGwoacr9NE8bWuy1Ip1gESExySg0t_neOuuvfQ6Ie4qFfiiF7DJDNH24eZeT4rDaW8wkueNtf0B8rEDIent5-QxzZBf835_Cusl8gpDGZRtUWYoleT3PmCpX4VdgRn3Yfw0zx_biUmF64c6jc6V-B3LmQoKWZycU5ZT9HzQv6CVeXb0BORES2PK2V2Lqt15dh-XFjZst2bbY4oDnfrBCnLQkwUDfDx4RXIv_OUvqb8vNgUVbBbAc5glEpPJOPqryFbp7_v_EN1NXeODVGlYVI4jOb6jdIXz7ZNdtvFZeSQeYEfzxgXh59rCyOEIFq91vpqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک، از بزرگترین خواننده‌های دنیا؛
با 140 میلیون فالور و ثروت 250 میلیون دلاری [50 هزار میلیاردی]
وقتی ممه‌های بزرگ یه دخترو دید، نتونست تحمل کنه و براش هاپ هاپ کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69833" target="_blank">📅 11:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69831">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=DB3GjLmPbdOXh_JA9qOdn0J8sHClsvjI6ty9ULCfKQkrEJcTZocfKwzdtPSqAqGzzkcCD5QNcD64cDLgpaT3kQjZhrqteaKeXVxbNPrsMhSEkZeh-pDbu1QoBBGnGU4jeqsQUUUkmTyoQ55mLQso1Jx00k9wS1wS8t4t72xjj2jPmrx_1lfZNfp5U_mbJCLteWM8lBEic_LwpnqmZW1WTnpm-cfAEQErJX3fH23a-ikO7RdwNnIwP7fBv9PnQhtYjswlGHY7ZLIjndpy83ZBkZEPTf7gQk9p182mzzcpvG3GkfA0IIVMeZPb77hdFhb3ktt8oXvEZRxty6VLsVh0L3P681CAA13awCJcbKdQLhQwjDd3sdOTtny4XyQVRB2fBYzfOu52_FHlg4DQO1bIfqF72BuuzMsza0bPVgObg8kPIrk3gJExi2tpyiYmc-Il-wJoJg1EbySRPdS7l84kycdnILt0YVqEUKlk2Q_q9ozcqJQR7Xkod9U8B7B266M_qA-NW6MV-nt2ytztUgbRM_FYS64WJL7lLlfhNaNxd5A8eFAaiV0jaYd6o6qKOk3ohS3NcOAGXI9fzFVLzMkeUjO3FwnisdPQRa0g7KsPSs0TGBWOmHPMj_GCePdcbP0zwi2ulLysglZ9LtHCUyB6wUd8sWKgJ6VLZEkkUtTDAoc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6d3c25ee1.mp4?token=DB3GjLmPbdOXh_JA9qOdn0J8sHClsvjI6ty9ULCfKQkrEJcTZocfKwzdtPSqAqGzzkcCD5QNcD64cDLgpaT3kQjZhrqteaKeXVxbNPrsMhSEkZeh-pDbu1QoBBGnGU4jeqsQUUUkmTyoQ55mLQso1Jx00k9wS1wS8t4t72xjj2jPmrx_1lfZNfp5U_mbJCLteWM8lBEic_LwpnqmZW1WTnpm-cfAEQErJX3fH23a-ikO7RdwNnIwP7fBv9PnQhtYjswlGHY7ZLIjndpy83ZBkZEPTf7gQk9p182mzzcpvG3GkfA0IIVMeZPb77hdFhb3ktt8oXvEZRxty6VLsVh0L3P681CAA13awCJcbKdQLhQwjDd3sdOTtny4XyQVRB2fBYzfOu52_FHlg4DQO1bIfqF72BuuzMsza0bPVgObg8kPIrk3gJExi2tpyiYmc-Il-wJoJg1EbySRPdS7l84kycdnILt0YVqEUKlk2Q_q9ozcqJQR7Xkod9U8B7B266M_qA-NW6MV-nt2ytztUgbRM_FYS64WJL7lLlfhNaNxd5A8eFAaiV0jaYd6o6qKOk3ohS3NcOAGXI9fzFVLzMkeUjO3FwnisdPQRa0g7KsPSs0TGBWOmHPMj_GCePdcbP0zwi2ulLysglZ9LtHCUyB6wUd8sWKgJ6VLZEkkUtTDAoc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به مجموعه‌ای از اهداف در سراسر روسیه و سرزمین‌های اشغالی حمله کردند.
پهپادها مرکز خرید گالاکتیکا در ماکی‌یوکا، که قبلاً مرکز منطقه‌ای بود و در سال ۲۰۱۴ توسط نیروهای روسی تصرف شده بود، را به آتش کشیدند.
آنها همچنین پالایشگاه نفت در نیژنکامسک، تاتارستان را هدف قرار دادند، در حالی که روسیه ادعا کرد ۱۵ پهپاد در نزدیکی مسکو سرنگون شده و عملیات فرودگاه را مختل کرده است.
طبق گزارش‌ها، حملات پهپادی باعث قطع گسترده برق در ملیتوپول، بردیانسک و دونتسک شده است، در حالی که انفجارها و آتش‌سوزی‌هایی در سواستوپول و کرچ گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69831" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69830">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69830" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/69830" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69829">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=MTm6354RzwmQC8VwFKt176sTR8DimDN2DVI9FGL0N9-sANUIaNWmTACN4GvAv8qfMFedlS9vAV8Ilo4nbNh9POQp8ePc_xxGiwLF4PGvMS1KtOnA5j3dBylY_lf9D5BqLnsGHAbw1Toyg3hKuOBcqtAVWHaMcZLOumt8srqTIa-l8WMoPp2yx4qVxT9LYsMLTsbxNrLMYarth6M7dx_HjyCErIP34JnG9AVGKQ6Tmuq9q6QkXIUTpp365FnjyCOoTf7R37PH0BQLmkl4lXZvy9Os_bQzom4kKxW5_nTTVHmk0i8TWm1QRN2RXtwsX6Laz5WB7sJ107RaMz29GzuVlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=MTm6354RzwmQC8VwFKt176sTR8DimDN2DVI9FGL0N9-sANUIaNWmTACN4GvAv8qfMFedlS9vAV8Ilo4nbNh9POQp8ePc_xxGiwLF4PGvMS1KtOnA5j3dBylY_lf9D5BqLnsGHAbw1Toyg3hKuOBcqtAVWHaMcZLOumt8srqTIa-l8WMoPp2yx4qVxT9LYsMLTsbxNrLMYarth6M7dx_HjyCErIP34JnG9AVGKQ6Tmuq9q6QkXIUTpp365FnjyCOoTf7R37PH0BQLmkl4lXZvy9Os_bQzom4kKxW5_nTTVHmk0i8TWm1QRN2RXtwsX6Laz5WB7sJ107RaMz29GzuVlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r19
@betinjabet</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69829" target="_blank">📅 10:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69827">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5oWd1V6NyDk3cVA26rVJeO0X8mNZDdjeQY2FD266D3J8RpGK2wN5j97YT5aTaNBZIz0A97rfxNW5UHrnhSljVwaewDN9_aOiDbZhYmhOTdu7nsUWli6wpVyhgmjOJXGbArNiBpVBpilvzuF4SyWHPdk9g6t_TJF0d8JSAsO5iwASAZPGiBj9FMNuP3kOuH6XfUjD-vQTxY_LMiUsgTTCezfZeEOX2J03dqDmeWo0g5HOZP1EE3ubnEUSrMVQ0FaNb87YFXoqJtrHmCXF2BDXVCNrPWBr_0jrJTAdN06nKGImYP4t8SRSLV8_qhaITosVQOPJBAdRD5OMCADM28flA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
شرکت آمریکایی BlackSea از پرتاب یک پهپاد FPV از روی قایق بدون‌سرنشین GARC خود رونمایی کرد
؛
این شرکت اعلام کرده است که با استفاده از تجربیات به‌دست‌آمده از جنگ، استفاده از پهپادهای FPV هدایت‌شونده با فیبر نوری را پیشنهاد می‌کند.
محفظه‌های پرتاب این سامانه قادر به حمل پهپادهای FPV در اندازه‌های ۵، ۷ و ۱۰ اینچی هستند؛ پهپادهایی که از نمونه‌های FPV مورد استفاده فعلی روسیه و اوکراین کوچک‌ترند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69827" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69826">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=s4RMBDOvOSyu35ugA7mLDTv7vJI3oPB15A2MYeD_RoF-xkXeyOYfgtZKk2AoWFjWN7oN2MKGlrUpkmFUjwfqj1GttQue0XZmnplyQnQ3fkLx_v-C_FWbRS6aSOy3r5IhjZVSVjZD3A_mDTTZNvxXkPSm2sDU76sLcebxpj7PRy4tBWkPge8uby6edhsOOuBGdwqC6bCU7EhpnWwY168hkDe5AbT8KcP7sOSvyOxaWOh1z5LFEpiYlOlCify6bXLRMyVLgmpvbbpM_7GR6x_x0kGz_ydIgP0lhZHo14ZZExcW9wk8ApRj3ZTnxNpX4bRc-KR3oICK5l7tgrubDFR13w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c36a2172.mp4?token=s4RMBDOvOSyu35ugA7mLDTv7vJI3oPB15A2MYeD_RoF-xkXeyOYfgtZKk2AoWFjWN7oN2MKGlrUpkmFUjwfqj1GttQue0XZmnplyQnQ3fkLx_v-C_FWbRS6aSOy3r5IhjZVSVjZD3A_mDTTZNvxXkPSm2sDU76sLcebxpj7PRy4tBWkPge8uby6edhsOOuBGdwqC6bCU7EhpnWwY168hkDe5AbT8KcP7sOSvyOxaWOh1z5LFEpiYlOlCify6bXLRMyVLgmpvbbpM_7GR6x_x0kGz_ydIgP0lhZHo14ZZExcW9wk8ApRj3ZTnxNpX4bRc-KR3oICK5l7tgrubDFR13w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جهانگیر، سخنگوی قوه قضائیه:
آخوند خرازی، بابت صحبتاش تحت تعقیب قرار گرفته و به دادگاه ویژه روحانیت احضار شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69826" target="_blank">📅 10:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69825">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🟡
📰
مراد ویسی تحلیلگر ارشد اینترنشنال: «جنگ بزرگ در خاورمیانه، برای سرنگونی جمهوری اسلامی است.»
⏺
پرسش این نیست که کدام زودتر می‌رسد؛ پاسخ روشن است:
جمهوری اسلامی سرنگون شود، مردم ایران به یک حکومت عادی می‌رسند.
جمهوری اسلامی سرنگون شود، نیابتی‌ها خشک می‌شوند.
صدام رفت، یک کانون تهدید در خلیج فارس از بین رفت — کانون دوم هنوز باقی است.
خلیج فارس می‌شود منطقه‌ی صلح، ثبات و توسعه؛ چون امارات، قطر و عربستان دنبال توسعه‌اند و ما هم دنبال جبران خرابی‌های جمهوری اسلامی.
ثبات منطقه از تهران آغاز می‌شود، نه از میز مذاکره.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69825" target="_blank">📅 09:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69824">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=a1hyUyf54eGkDMBCdGRUXMA45TGfkZfrqdYffV4250KRGzdyAaBok_-NedsxVX_jQWdSifNDx4KrWoecVn9mMmjXr4xL6wBFOsR1Ke8kfIU2WLAAX4kN3eHjdqR8r_XsIQu8hRvfQH-Awf7a7LlwydtWfyaRpAQQBGV9x1BYzyb0kjpgXBAU11YEW9SBXfMb-jAprtXZLMq2kpGcTdFI7cDBIYMd8Bn81-C071WViR0QeFyPJiIZ-Nr4gQnLWJx0O9N49t0qJNIvmumgNk94yKDtA2dcwM7kjzUG4ygROFmb6HDmbgeCRS1mlsfn3FRHK7mxJUpft_WHKLFSaZ5bbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bdd241cc6.mp4?token=a1hyUyf54eGkDMBCdGRUXMA45TGfkZfrqdYffV4250KRGzdyAaBok_-NedsxVX_jQWdSifNDx4KrWoecVn9mMmjXr4xL6wBFOsR1Ke8kfIU2WLAAX4kN3eHjdqR8r_XsIQu8hRvfQH-Awf7a7LlwydtWfyaRpAQQBGV9x1BYzyb0kjpgXBAU11YEW9SBXfMb-jAprtXZLMq2kpGcTdFI7cDBIYMd8Bn81-C071WViR0QeFyPJiIZ-Nr4gQnLWJx0O9N49t0qJNIvmumgNk94yKDtA2dcwM7kjzUG4ygROFmb6HDmbgeCRS1mlsfn3FRHK7mxJUpft_WHKLFSaZ5bbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از نفس‌گیرترین ویدیو های منتشر شده از جنگ؛لحظه بمباران شریعتی تهران!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69824" target="_blank">📅 09:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69823">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69823" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#بازی_پولساز
⚠️
🔥
بلک کارت جدید ترین بازی معروف جهانی هست که فقط کافیه یکمی باهوش باشی تا حریفات رو شکست بدی
👌🏼</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69823" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69822">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=cR4e7KTWwjro2dDv6hPyw-FXuq4cTiXFvbXRZecZvtu6ft2kgHYh3anRAJjJKn0SuZGMfFOsj9Nii19KLun1f2E_Y4S4aVMbJwk48MNPavw4_Hp3CWwuDKMroBato0MNWQ4daooYRRUsPOA0jw4T2CVJONcfh5dmbGdQPpT2KKfaIZyCIxChyBUanvYsdV7mhFui7UulFpOwKd4Czyv8JgP3XN7hFAS94BWR2BWZVM81JpOt9cyOo9AnDVjwgMwxacjJqOseT6_iaT5umUE-jbH2gKHX1_2as9f6asNCRfOulTNTXLZ-XRRvH4uAaW_Om6Qy_TVmLfmuHm5ffNhLZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c003ee1.mp4?token=cR4e7KTWwjro2dDv6hPyw-FXuq4cTiXFvbXRZecZvtu6ft2kgHYh3anRAJjJKn0SuZGMfFOsj9Nii19KLun1f2E_Y4S4aVMbJwk48MNPavw4_Hp3CWwuDKMroBato0MNWQ4daooYRRUsPOA0jw4T2CVJONcfh5dmbGdQPpT2KKfaIZyCIxChyBUanvYsdV7mhFui7UulFpOwKd4Czyv8JgP3XN7hFAS94BWR2BWZVM81JpOt9cyOo9AnDVjwgMwxacjJqOseT6_iaT5umUE-jbH2gKHX1_2as9f6asNCRfOulTNTXLZ-XRRvH4uAaW_Om6Qy_TVmLfmuHm5ffNhLZ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😯
اگر هوشت بالاست
🗼
:
❌
👍
این ‌ویدیو‌ آموزشی رو‌ ببین و با ‌استفاده از هوش بالایی که داری پول در بیار.
🟢
بازی خیلی حرفه ای و‌
#پولساز
رو‌ از این ویدیو یاد بگیر
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a18
@betinjabet</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69822" target="_blank">📅 02:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69821">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:  اگه ایران از این به بعد به هر کشتی‌ ای توی تنگه هرمز شلیک کنه، فرقی هم نداره با موشک، پهپاد، راکت یا هر سلاح دیگه‌ای باشه، آمریکا در جوابش یه پل یا نیروگاه برق ایران رو میزنه حتی اگه نزدیک تهران یا داخل خود تهران باشه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69821" target="_blank">📅 01:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69819">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxh1r64Gl8VE853AnoD4qe-uAuLZj5ItbLsNL5eqlSxKF4kSWKLI5YoJUthX0F7GjeKBTjFAT6e1ZuKnfu1PGj8KN8-eYCiPUyHjedz-mZ9u1R_OfpA_FMruFK3GlOpzf3mqF1WyyGJm_k0kAwaytQogvZ3RU5EX6i-sPAQm5BwnW38duHzffKi6Ah30GKnozrvkbPkhvIbuHeOSSiIX1yCLcFmu-C52xBrsLnqSHY0nsbLuDE7snLf2zp5Lb0IHX9YEknTPNEwvzShxsMAH4FT6azStOV5P05iPk02nz1bSCs7OKRtiy28Xc7eTTQUzhjzAJ7DFXoR4Q-6va0dzdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=t8tVLY1KjFo3sADnsEputp2bKf4p_SPNI1QOO2pcHinjBnzyzmzDzuM7mXCrtIzyHs8dTqoOR4SgSlFGgiv9BipTlJxLXtWBd5bXjziZ4SS1nSSFi0AnojA81z92TTXxIjUScm6_2QWGl0ZEa9paOjeLen1jOUi2Ol_7ywBPZSHOqgmthPW6xceK-eTKEUQIdL75yNNtwSmK1E9VKB7ic5kTvqgv321B0Jh7StGZq33iF5obWd8Ajw0RWNGcySQFpyoVkmd1sNB76op5Gs0CMsGZYyA3s1O4UfmNTy8dxQmrnevxkE1_VYJkrQIuwl0PCRhccUsuCVIbmxukAX4hhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94eb35c039.mp4?token=t8tVLY1KjFo3sADnsEputp2bKf4p_SPNI1QOO2pcHinjBnzyzmzDzuM7mXCrtIzyHs8dTqoOR4SgSlFGgiv9BipTlJxLXtWBd5bXjziZ4SS1nSSFi0AnojA81z92TTXxIjUScm6_2QWGl0ZEa9paOjeLen1jOUi2Ol_7ywBPZSHOqgmthPW6xceK-eTKEUQIdL75yNNtwSmK1E9VKB7ic5kTvqgv321B0Jh7StGZq33iF5obWd8Ajw0RWNGcySQFpyoVkmd1sNB76op5Gs0CMsGZYyA3s1O4UfmNTy8dxQmrnevxkE1_VYJkrQIuwl0PCRhccUsuCVIbmxukAX4hhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇨🇳
🇸🇦
یک پهباد ساخت چین متعلق به نیروی هوایی عربستان سعودی در آسمان جنوب کشور سرنگون شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69819" target="_blank">📅 01:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69818">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDU1VrPsJyb4kPqRKSFafk0RADFk6cPIAv-GTgZ4KibGmk9JKEgHM2kCpaBbNniCQckyG3Adg_pjASDOObo_hCsbMcSJVzcF5L1D5NtkrzgyQ9b5BA0VQ76y9VOCNKxZPgR6aqu9xxQjfg03sUD6LvzRCJNBVJfLydxFZJ1n7I22w83o568ImMayt_hb91_JxXdsQlkc_CW2oBJSqXMANC-m7Mxz1mTPEBOT00VcvUwmqzxrXtpFqGSc_nRPFdAd45T8RpPWGzkRbtpLf8j-HR7j4Pi2_Ym0-X-VgLU6VvQCYoS1JLH-DzK3-ribsFaONiZ8FLivlLIngegUYUDgFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
51سال رفتار نامناسب!
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69818" target="_blank">📅 00:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69817">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=XWK0iZNFUWikZYe6WRn-XJrqbNifR1bNISVP_p2PYX3ud3UvFyM4poJfARPznylHS6SuIt8ZkezeBBSGtabMsX2SI3hD_tDou8frzFIAxFBvnj42gtZ9Wgm1taupQLoALtOlBqTV_QDX3SfAztoUnF1K2XntXrn78MTEjr-OMMms2I0DOFTQgSHsR7YQJEAb4JgRioKFmCip-VmX8yiMO7cAHhPU8xDHiLs33UwEnx67vdeLFqzDh2Qg33fWWPdam7kxz-yYYJDnAqTAya-EM-NTzXIgWx8gXzAMsY8TwGFfRuK6vHGqjgCcL6dSU2Hy6BBVMk9pw15McGy0akmBLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dbf391292.mp4?token=XWK0iZNFUWikZYe6WRn-XJrqbNifR1bNISVP_p2PYX3ud3UvFyM4poJfARPznylHS6SuIt8ZkezeBBSGtabMsX2SI3hD_tDou8frzFIAxFBvnj42gtZ9Wgm1taupQLoALtOlBqTV_QDX3SfAztoUnF1K2XntXrn78MTEjr-OMMms2I0DOFTQgSHsR7YQJEAb4JgRioKFmCip-VmX8yiMO7cAHhPU8xDHiLs33UwEnx67vdeLFqzDh2Qg33fWWPdam7kxz-yYYJDnAqTAya-EM-NTzXIgWx8gXzAMsY8TwGFfRuK6vHGqjgCcL6dSU2Hy6BBVMk9pw15McGy0akmBLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
آتش‌سوزی یک کشتی در پی حمله سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69817" target="_blank">📅 00:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69816">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🇮🇷
سپاه‌پاسدارن یک کشتی را در تنگه هرمز هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69816" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69815">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=eG8PTZ3Z2v5qA_1_ot8BoW0Z6I7ziwpa8YJMzRSJ9bX6qPI5vNCko-19gWAKrbJDp0cTIv1AuU8-GVoZ_nqtCoK1t0s39bxVSs18Pa2Apc43pHb4Uz2jA_XkFOdfj0HVqM1upB6rNSfbOqKXZq6dfxDaXrM5YpoRcWKvd4FwLC1WozD8kXFILD9Jjq1xRcw6rwbSJXo2JyYoGPCJORBoG4gLZJZjZohoeDApzivbZZKSSYXWxLNDSGQnMvoQk9hW1SLgu4HmPp1EpW-WTKfrijNQZku68nOnYOYU0_vW4rqKt50F5XxCGklqsuK1FPjqZp94AlrmD4DswJsEcNZRRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec1565ac0.mp4?token=eG8PTZ3Z2v5qA_1_ot8BoW0Z6I7ziwpa8YJMzRSJ9bX6qPI5vNCko-19gWAKrbJDp0cTIv1AuU8-GVoZ_nqtCoK1t0s39bxVSs18Pa2Apc43pHb4Uz2jA_XkFOdfj0HVqM1upB6rNSfbOqKXZq6dfxDaXrM5YpoRcWKvd4FwLC1WozD8kXFILD9Jjq1xRcw6rwbSJXo2JyYoGPCJORBoG4gLZJZjZohoeDApzivbZZKSSYXWxLNDSGQnMvoQk9hW1SLgu4HmPp1EpW-WTKfrijNQZku68nOnYOYU0_vW4rqKt50F5XxCGklqsuK1FPjqZp94AlrmD4DswJsEcNZRRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یه پسرِ جوون تو تجمعات شبانه:
به ابالفضل راضی‌ام جنگ زمینی‌ بشه، یه تنه 500 نفرشون رو حریفم!
ایشالا روزی بشه مکه و فلسطین رو آزاد کنیم.
ایشالا روزی برسه آمریکا رو نابود کنیم و تو کاخ سفید نماز بخونیم.
نیاز به بسیجی‌ها نیست همین بچه‌لات‌ها اسرائیل رو میگیرین داداش...
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69815" target="_blank">📅 23:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69814">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b396273688.mp4?token=Cn04ZwsRM2fKTNddEzvE-C0sUmfGO2QWm7DR0LifFf-IYXhqrIhePi5VZibI9l_QZ7dRANDjbPmdHrxcXVvaL1afBwtWtzC0b9dVIr3FQDtdo2h2G5TMNJ9_KYJf-vE9Sb2M2pQQcJZERxz9prooc9V18n18KFgAgzLZIyydjntOHVftm-GZzeFabYvdhQIpxnrih0DsF_l51hCj4n6PJAID-r0f316gqDl9tNBoMuF8dymD1iVCJCJf5gDhcIS6ZDmDtGEQ0QxyN3-aG-zFlkOBv0wZ9damfEe7er6QDh6mSsSwjU1LCEk5ECRX4qs1B6KoeI0JgDI-6OKoX7tmuzD4KZQrQDBmJnsfkv2kFT99LyRSyM-FO1zZEE7QgwijEZeQca1nHo8k3h8WqmZ5VNMKF_ci29GNVlM7R7IdcKL_Yq5ydh0fo3VqCdeHD9tdgWIBUzyk5dkPScl3tY6miRh_EHU37h3sMhjRQ2xw8LCV5S4dLIdTLvrOilDxfyulWEDyTW1GGJnG0JVKIMhDLFS3EtiyRjh_x8DzDlF44pW1t_jkFtWsfCFMgwBdE1fHFL3FM2dNjwdaLR1eEzWJTAncVb631xDC5LFfTbiu6L5Sf-Fx6Jg9aVznmw_ZB1YKGt0jtebVK8JWypePmO5sNE4Xq-4ryHeIYOAwytLzRqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b396273688.mp4?token=Cn04ZwsRM2fKTNddEzvE-C0sUmfGO2QWm7DR0LifFf-IYXhqrIhePi5VZibI9l_QZ7dRANDjbPmdHrxcXVvaL1afBwtWtzC0b9dVIr3FQDtdo2h2G5TMNJ9_KYJf-vE9Sb2M2pQQcJZERxz9prooc9V18n18KFgAgzLZIyydjntOHVftm-GZzeFabYvdhQIpxnrih0DsF_l51hCj4n6PJAID-r0f316gqDl9tNBoMuF8dymD1iVCJCJf5gDhcIS6ZDmDtGEQ0QxyN3-aG-zFlkOBv0wZ9damfEe7er6QDh6mSsSwjU1LCEk5ECRX4qs1B6KoeI0JgDI-6OKoX7tmuzD4KZQrQDBmJnsfkv2kFT99LyRSyM-FO1zZEE7QgwijEZeQca1nHo8k3h8WqmZ5VNMKF_ci29GNVlM7R7IdcKL_Yq5ydh0fo3VqCdeHD9tdgWIBUzyk5dkPScl3tY6miRh_EHU37h3sMhjRQ2xw8LCV5S4dLIdTLvrOilDxfyulWEDyTW1GGJnG0JVKIMhDLFS3EtiyRjh_x8DzDlF44pW1t_jkFtWsfCFMgwBdE1fHFL3FM2dNjwdaLR1eEzWJTAncVb631xDC5LFfTbiu6L5Sf-Fx6Jg9aVznmw_ZB1YKGt0jtebVK8JWypePmO5sNE4Xq-4ryHeIYOAwytLzRqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خرازی:
این کلیپ ها جعلی و هوش مصنوعی است؛
من این حرف‌ها را نزدم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69814" target="_blank">📅 23:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69812">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=jHeis5sv0QlAUUb1xJAvrmUE3m4ZHTqTISZ9Pu41vaOEh2xPGzr5kdDJGBDZQko0CtaTL1KHMcjV0wBQnctN5rrdmFVUb-wg_2e-mCXEwesa4F9UYUlcA2tQMbGNmLeyC5IRTAc5k9H4PlgjVBp78in9xFuzPOKDQ86OoCgcblAMyZhHJZDJtOzOF9XX85JKK32NFgUFxj7yvgvwePpMFbnwQCUbL-WDuAXgN1eZHbPkXtj8upg0GkjU78MURkcb31i5cxASqENAv33_db7Vu4MohawbQerWFFfe-cKggCn4kQ7UhGZpl-CUgohgWlITwDGiK7funEb5EqhfvEfWzg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1fdc25902c.mp4?token=jHeis5sv0QlAUUb1xJAvrmUE3m4ZHTqTISZ9Pu41vaOEh2xPGzr5kdDJGBDZQko0CtaTL1KHMcjV0wBQnctN5rrdmFVUb-wg_2e-mCXEwesa4F9UYUlcA2tQMbGNmLeyC5IRTAc5k9H4PlgjVBp78in9xFuzPOKDQ86OoCgcblAMyZhHJZDJtOzOF9XX85JKK32NFgUFxj7yvgvwePpMFbnwQCUbL-WDuAXgN1eZHbPkXtj8upg0GkjU78MURkcb31i5cxASqENAv33_db7Vu4MohawbQerWFFfe-cKggCn4kQ7UhGZpl-CUgohgWlITwDGiK7funEb5EqhfvEfWzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه ماجرای عجیب و تلخ که زندگی یه ورزشکار رو زیر و رو کرده
این بنده‌خدا یه ورزشکار ۱۳۰ کیلویی بوده، پرس سینه می‌زده و از بهترین راننده‌های جرثقیل هم بوده؛ ولی یه ماجرای مهریه کل زندگیشو زیر و رو کرده...
همسرش مهریه رو می‌ذاره اجرا و حکم جلبش صادر میشه. وقتی مأمور برای دستگیریش میاد، فرار می‌کنه و مأمور هم به کمرش شلیک می‌کنه؛ گلوله باعث میشه قطع نخاع بشه.
حالا با وثیقه آزاده، ولی هنوز داستان تموم نشده؛ همسرش گفته فقط یه هفته وقت داری، وگرنه دوباره باید بری زندان!
از یه آدم سالم و ورزشکار، رسیده به این وضعیت...
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69812" target="_blank">📅 22:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69811">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇺🇸
وقوع یک حادثه امنیتی در نزدیکی باشگاه گلف ترامپ در شهر بیدمینستر، ایالت نیوجرسی؛
فرماندهی دفاع هوافضای آمریکای شمالی (NORAD) دو فروند پهپاد را که حریم هوایی محدودشده بر فراز بد‌مینستر، نیوجرسی (Bedminster, NJ) در نزدیکی باشگاه گلف ترامپ را نقض کرده بودند، رهگیری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69811" target="_blank">📅 22:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69810">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy-XcwW9n1TF1jLzIl0MtFQlAeHbOceIom9MGX7sWPi_MhonXj5aN3jU-T2wC6aktRYq2SYOvJ-jHi5-FiwnXqSxOsN8cV8rW5Ysvh4VVHG4b_f4AUktxaWIG4E0rAz0gWXJA9Nqd8xQ9fy83ru1xOpjH7GoClXIJ8lD3PJbVDgJ19A6kfgkeNDNNq3mspEaTLwBFlbVL1f4tsiKuMjBZ5mq57uQMMOPTNR9f1TaLle-L5mft-vR4RPOiD5gVYdS7Qqx2gfAVQTmHu1OxQIBq0An_GDczoAzL2FMy7V2bcxAvG0u7YYDFUAAfyeyvCtg1vJ8CAHO7nyQHsuAHDRBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
با حکم مسعود پزشکیان محسن رضایی رسما دبیرکل شورای عالی امنیت ملی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69810" target="_blank">📅 21:58 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69809">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❌
یه فلسطینی به زور بچه شو میفرسته جلو سربازای اسرائیلی، بهشون میگه شلیک کنید بهش!
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69809" target="_blank">📅 21:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69808">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNH7yk9ZuL2t7-Z8nIoHkmTnN3XxWfqQyvvORg8t4mK_PLiXC4n2T6G8Cf_mUudGj56oJ7ijlvP-qK4_zrgJsBPoy64SZFSbakTBhI7z406Gca8k5sakL9Flbxh2AeWXwMkX1u-8Dow5UHL-Xew5QmyJzds2zZ9yF3qplWgAtrhgw_gob0UJMkiEW-eQ-39OgZbi5aizjQRPUXJA529Pz0b2bVxXx2tj1tmE-Jikc3_ORm31KwD61w9T47EjbKKxn5Nw083NHvm-JYnvFRYG6in2xcfqvBTEeNHzuRxdtoOVKwwbQrPQibCug6Jo2yZQXNQ5m3l2RHOD6c2U9ZjJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
اکسیوس به نقل از ترامپ:
ایالات متحده در رابطه با ایران «بی‌سروصدا» عمل می‌کند، که نشان می‌دهد واشنگتن فعلاً از اقدام نظامی عمده جدید خودداری می‌کند و در عین حال اجازه می‌دهد فشار اقتصادی افزایش یابد.
ترامپ با این استدلال که ایران از نظر اقتصادی «در وضعیت بسیار بدی» است و در حالی که محاصره دریایی ایالات متحده فشار را تشدید می‌کند، برای پرداخت حقوق سربازان خود با مشکل مواجه است، گفت: «این [مشکل] حل خواهد شد. همیشه حل می‌شود. مثل یک بازی شطرنج است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69808" target="_blank">📅 20:49 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69807">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🙂
لحظه کمیاب واژگونی کوه یخ غول‌پیکر در سواحل گرینلند؛
ویدئوی ثبت‌شده در ۲۵ ژوئیه ۲۰۲۶لحظه واژگونی یک کوه یخ عظیم در سواحل گرینلند رو نشون می‌ده.
با تغییر مرکز ثقل بر اثر آب شدن یا جدا شدن تیکه‌های یخ، این توده‌های عظیم برای رسیدن به تعادل جدید می‌چرخن.
در این فرآیند، بخش‌های آبی‌رنگ و شفافی که میلیون‌ها سال زیر آب فشرده شده بودن، برای لحظاتی در معرض دید قرار می‌گیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69807" target="_blank">📅 20:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69806">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=LUZ8zRdtKK8Iwrew63oJTfR5QQs0s5qO4Tf2Hf6m_p_S_NFFCMxEnUloG2glqKLFoSIrBWU3HfiIT7ZlhDP830H4K4elkOVn-fYEOHA5vnCvoVBE5FvHuo9M7W4bJcRB6tjrGgOJeFz87EKxtqKBQ2aevrOtAjuKQIKAUqa7JVm0ucOQS1DnyB0Rv1uSwTUM8-piw_k4fymcMPvHyu5Ih7AvX_Am2KRD8hmCZB4nGB9EHqeZvfxUd6Odyw0X2u6KknEQRG-ZRDhl_N-JapbN-gmaxU881xCbrlXTUhvXyiCeD5Hs6OhARVE0znPRg77EtCAXH0BlbRUM2KGbWKS3Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=LUZ8zRdtKK8Iwrew63oJTfR5QQs0s5qO4Tf2Hf6m_p_S_NFFCMxEnUloG2glqKLFoSIrBWU3HfiIT7ZlhDP830H4K4elkOVn-fYEOHA5vnCvoVBE5FvHuo9M7W4bJcRB6tjrGgOJeFz87EKxtqKBQ2aevrOtAjuKQIKAUqa7JVm0ucOQS1DnyB0Rv1uSwTUM8-piw_k4fymcMPvHyu5Ih7AvX_Am2KRD8hmCZB4nGB9EHqeZvfxUd6Odyw0X2u6KknEQRG-ZRDhl_N-JapbN-gmaxU881xCbrlXTUhvXyiCeD5Hs6OhARVE0znPRg77EtCAXH0BlbRUM2KGbWKS3Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
طرفدار حکومت در واکنش به کشته شدن حمیدرضا رجب‌زاده:
شما زدین مبارک شما ما زدیم مبارک خودمون
خدا سرشاهده جرائت دارید بریزید خیابون
یجوری تیکه تیکه تون بکنیم یجوری ریش ریش بکنیم شما رو تاریخ تو خودش ندیده
به جان امام شهید قسم به جان رهبر مجتبی قسم شما رو با کارتک از وسط خیابون جمع خواهند کرد
جنازه شماها رو میدیم سگ ها بخورن
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69806" target="_blank">📅 19:56 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69803">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t4WX589PZBrF3rjhKefpsE9RHtqGESHTFqD4EdeHvclJ-B3DIx5WEaqHauFXlXKgpJfUQrmsn4WOXThk9qUpt6o-nI7pwbz_s9X1Y3kSxWS7VPnLdIZG8nwllr0HxfR0yHhltzKqgKcPF_g6mIhHK1hpS-jvQ7G9SPtYON2a6jj8aE_m-auocj0yqTHgvCWfOAlo8lfbrwcUY1AyUtReFsQI_RFNHNFpx2QOfj-6LCSY_OP4M70I36jOwL-Awr9N1zxujP7tTH1aDtzOUTdvzDr2gMAXciJLg_wVK52cV9WFZsSt6_Q7xm13pvK6RmZIXOFzFzH0fCVB8rL_ZJkrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ROj62qA_0OdyNr0NCUVm4qQMRx_EBzJRVncZJrgxYae2vp3FSYsQc9G3fD3R788etqOLCVCqYq_2ixskzjFsAtDx3Zx4AZQewc4oTCYS1uq0drhKDl1vDLjrqMrPLwyKLD1kw-SM2Xq3iQCDyKvEvhKyw666rb-6VeHQ2nHIaeb0fmcQ0EAbXhoo9T_KtpnlVkdWhcQol2zotSSqHvXcIdMXbzPL6kwuGS-pbv44LOR0CEmf-FqvqWeFeO3dtbVGyoVmBhmE_ALuXUjBZDVbl3zbOypnf35jhqaEmYjEDH1OmMfixMGDZDxUeRsayH5llDPay2gmPMIEOKv-6cYbPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rsOeS6ROrYmLCWuiW4On05TAHx4EKjstqOf74kSJtUBEYNd_V4T8UMxWix-_A8CrTwawhLDmp9kqVXrlTMH8-eIzH4WM-jYpQKdP0MaBCXgunLRzTLngEJP-XBjA5VhXbM17QgIbXO-MhpwOFsGz8Img8qzm-OzJYT0761f3lvVGfECaxOtzOWHOV3gDTeLf0WjtbyPP5Ju63Y1UK1QfrX8C6JTya81b5KZNST0QKOerrYYjrojiVqNwIlujYzYysTUbEkPNHwirRIxDborAlhMQeEQdf5ILiESFHnBCwZPy5Flody8XeiYq90H2jsfnv7HHN4VVASFg6aZPt2a8ZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ریورز یکی از مشهورترین فمنیست ها که زن رو برترین موجود میدونست و خودشم علنا لز اعلام کرده بود با یه پسر خوشگل و پولدار رفت قاطی مرغا
☺️
☺️
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69803" target="_blank">📅 19:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69802">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=I0qFnJCxCieClAYRYnvgIo5unCJNffSI8V27IUXpaS1eZTe0bSRLTgucKN6n8byl22KR9sZWZ2ZYnD0BefRW2GnE6ui9lbpkGIDzLFxrmdHLrldrhvO9YSVWCbEIIaBWe3iaR9T0SImRbkossWR4wfJoRTZaFY4vYX-bCG7J7A--5bjkWl8Yey8ATivi_Ezsg4YxYP4fj9MSAmDtKzgchKfVi8ziarltptwmLBSYU8ClYqZNwurDdukYA9YkkoPUeiu7HRPlvsJPkMb1PmTFKBNUOBsmhqIFXPy1_OBr3ZZ8ajw1UGB3xgmls8fRjPZ4Y4qsxdqqic7u7iPon7pv2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0cbb95dc3.mp4?token=I0qFnJCxCieClAYRYnvgIo5unCJNffSI8V27IUXpaS1eZTe0bSRLTgucKN6n8byl22KR9sZWZ2ZYnD0BefRW2GnE6ui9lbpkGIDzLFxrmdHLrldrhvO9YSVWCbEIIaBWe3iaR9T0SImRbkossWR4wfJoRTZaFY4vYX-bCG7J7A--5bjkWl8Yey8ATivi_Ezsg4YxYP4fj9MSAmDtKzgchKfVi8ziarltptwmLBSYU8ClYqZNwurDdukYA9YkkoPUeiu7HRPlvsJPkMb1PmTFKBNUOBsmhqIFXPy1_OBr3ZZ8ajw1UGB3xgmls8fRjPZ4Y4qsxdqqic7u7iPon7pv2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚀
یک فروند پهپاد بدون سرنشین جنگی (UCAV) نیروی هوایی ایالات متحده از نوع MQ-9A Reaper که از فرودگاه چابلی برخاسته بود، در نزدیکی گورستان چابلی در جیبوتی سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69802" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69801">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم g18 لینک چنل https://t.me/+_btGj-rRAxs3NGVk https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69801" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69800">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PY_dbzVBF907WIgKucCiszqHVMnQprLbsaVCZgKATC6hGP-YZvjiPVsWMIdRFdZ_B74-riZmrHWEMCNhjA9GEiu_Mg7bNit-yTd9cNzR6QYT_ML2BaIHkkwHNiRKOblnnH8TVzQikVYCQi7p9Re26jBWLzYBNiQJFHvW0sDV3TBwwL9do2w2waCxHpv9n1rEbQCc5XyJSnt7guaGE8qOtGz5qkuqIC1Jqr25NB2kxK0y38baAFVprbHLTCtJJUmWf22a4VZgSC3QJMS-PM-4LlW5bKbrWiFCTbSjq6eclvkK4n_YHHEgwv2iw7bsJ75qNl4I_KjiZWHVB_Bcan11fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پول درآوردن از بت دقیقا جاییه که فرق استراتژی داشتن و ادعا داشتن رو مشخص میکنه
👌
15 بازی 15 برد
✅
من به پول شما نیاز ندارم و چیزیم به شما نمیخوام بفروشم
g18
لینک چنل
https://t.me/+_btGj-rRAxs3NGVk
https://t.me/+_btGj-rRAxs3NGVk</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/69800" target="_blank">📅 19:11 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69799">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411943761d.mp4?token=TGZz0WSe2_tvG-Ikr262rpMT7y2jpxWIyW2TjNGMZuWFPiJ06prySUHAS67usx5PPpU5u96rry90Tf6GA_IhDODLw58TufeYLFFEmgj-GkqoRtVCky4Qfny1fqW0xuQwYOsxA30yKPr4-PhrvIz7WDgTWdUvm3AWojxd54dR1EFDlSuudMNm6pjdvoDssLctNbHvoEok_XrskKfy-JCf09qST_muDRnECjWIBBjMLPMFBp5EAVGKrS_jh5WlRl0Nv_A2KD51CeNXbbw1PhZ49zEjgAGyDR1hEqaoELWh2QTrnWc001BzxovYQCavj7-5eL4Gd3LeLEc1jww4c6jovQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411943761d.mp4?token=TGZz0WSe2_tvG-Ikr262rpMT7y2jpxWIyW2TjNGMZuWFPiJ06prySUHAS67usx5PPpU5u96rry90Tf6GA_IhDODLw58TufeYLFFEmgj-GkqoRtVCky4Qfny1fqW0xuQwYOsxA30yKPr4-PhrvIz7WDgTWdUvm3AWojxd54dR1EFDlSuudMNm6pjdvoDssLctNbHvoEok_XrskKfy-JCf09qST_muDRnECjWIBBjMLPMFBp5EAVGKrS_jh5WlRl0Nv_A2KD51CeNXbbw1PhZ49zEjgAGyDR1hEqaoELWh2QTrnWc001BzxovYQCavj7-5eL4Gd3LeLEc1jww4c6jovQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
آقای پزشکیان بچه‌ها یه شوخی باهاتون کردن راجب درختی که میخواستید بکارید توی پاکستان، برامون بگید قضیه چی بود؟!
🇮🇷
مسعود:
من فیلم بلد نیستم بازی کنم.
اینکه الکی یه خاکی بریزی و بگی من درخت کاشتم پس تو نکاشتی.
ما نایب رئیس بودیم توی تبریز باید ده تا درخت میکاشتیم همشو خودمون کاشتیم.
ما کشاورزی میکردیم، همین الان اگه برم مزرعه خودمون بیل رو میگیرم کار میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69799" target="_blank">📅 18:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69798">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=UrWVGVKODCc83z_hRB0xQH4N5XmDTAFBaA_c_Tb5uxQXV5ZVIiILbHNacKOeA1w_q-1XDNaGpR2UBImeDZDQiVSHt058zRRuKPN7mnCJwS-eZC7cpTz_jUIqyv7GRj-8HjjTBbSGU1GioN3_ivVofwfkR8PPIGm_dNdojkYGh3MbyurSZ2WujolTESFvI6zOSWCYRQwzGWHlHBWJDAfl0gsBCbh8v9q_CTPuOnK6AxAQ6hQG7_TiEQdlqU0IBqlVgKwVPyrJO6BFuZ208cuo9_d5gO16Qeunvb-8ETTdHJP5zcC3JRIZAJtnrHdG3e8zYjQrS_1vp1rAqYqZW56zjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb6125750.mp4?token=UrWVGVKODCc83z_hRB0xQH4N5XmDTAFBaA_c_Tb5uxQXV5ZVIiILbHNacKOeA1w_q-1XDNaGpR2UBImeDZDQiVSHt058zRRuKPN7mnCJwS-eZC7cpTz_jUIqyv7GRj-8HjjTBbSGU1GioN3_ivVofwfkR8PPIGm_dNdojkYGh3MbyurSZ2WujolTESFvI6zOSWCYRQwzGWHlHBWJDAfl0gsBCbh8v9q_CTPuOnK6AxAQ6hQG7_TiEQdlqU0IBqlVgKwVPyrJO6BFuZ208cuo9_d5gO16Qeunvb-8ETTdHJP5zcC3JRIZAJtnrHdG3e8zYjQrS_1vp1rAqYqZW56zjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخشی از مستند«پسرملا» روایتی از چند سال آخر زندگی روح‌الله زم:
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69798" target="_blank">📅 18:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69797">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.  او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69797" target="_blank">📅 17:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69796">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGlqSkr1jN-ffQBTeDPWWv48-zftLE48BThkU21BCXgtq2JAGJ0H7wYpBc2BkxHqbsdRuflpUbYT9geXmHNE8O-6590kjPaQDerMWBc4L4cZQLmc12Cd24pvX2HCkNYmSfZcP9If4_L2LM4ngBAuiSxsqMQvndsM7FwDVmIudnSO8Thd0yc0xyRn3gZWV6uyaRAK1iyqYplekdmq_kjziDYbbu7IgWc2mTanZ0s7CMuly6JoCkTX6DFZ-4TLuU0yRG3hgoykiqUqLvs61l_2MY3I40OLhAuSx5nGyZEv1MqMVMzL058NgIdmTU5qFg_sbkswZJWFsrqlM9CxjmfI6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
📰
وال‌استریت ژورنال: دونالد ترامپ، رئیس‌جمهور آمریکا، از چند هفته قبل برای اعلام پیروزی در جنگ با ایران آماده‌سازی‌هایی انجام داده است.
او به مشاوران ارشد خود گفته است که در صورت بازگشایی کامل تنگه هرمز توسط تهران، می‌تواند این درگیری را بدون دستیابی به توافق هسته‌ای به پایان برساند.
ترامپ معتقد است که ایران احتمالاً در طول دوره ریاست‌جمهوری او، برنامه هسته‌ای خود را از سر نخواهد گرفت، به ویژه پس از اینکه آمریکا سال گذشته سه مرکز هسته‌ای بزرگ را بمباران کرد. مقامات آمریکایی می‌گویند که اگر واشنگتن بتواند فعالیت‌های هسته‌ای تهران را کنترل کند و ترافیک تجاری از طریق تنگه هرمز از سر گرفته شود، ترامپ احتمالاً تمایل بیشتری به تمدید آتش‌بس فعلی به طور نامحدود و رفع محاصره بنادر ایران خواهد داشت.
مقامات آمریکایی اعلام کرده‌اند که ترامپ همچنان مایل است تا در این بن‌بست دیپلماتیک جدید صبر کند، به ویژه زمانی که قیمت بنزین نسبتاً ثابت و در حدود 4.02 دلار به ازای هر گالن باقی مانده است، در حالی که سال گذشته این قیمت 3.16 دلار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69796" target="_blank">📅 17:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69795">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=PEcUbhNLXy12mW-C8OkswUDD7BPMtzrEwJc1GFNJjvnAjcOkdTXjZJdk7z_YKBad0bhYZoLbneBVfja47XaiJz2VfDMVK-zVjvYxe_aj-XbJqKffVmKCvhFilBJlSAQMdLjNzLsGAcpaPe7wx89z-1K8qegWrfxW9IzlNkSE6GvrSsG5nWdOKzLlJXsADXZhhLd-5uF2K5R2JhQvNBxnfQDqqUQ6rDt5VhIhZR6JyucBvvOpw_D5-wyg3Dsna3CfImjAietaVSfAubgDeH-sZGTJCuBuGAAfyGd1ECYxOHV6n2rCQlmqf95BY4yqzRgHI540kPAZkFeLYL7ksReUgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b5af888.mp4?token=PEcUbhNLXy12mW-C8OkswUDD7BPMtzrEwJc1GFNJjvnAjcOkdTXjZJdk7z_YKBad0bhYZoLbneBVfja47XaiJz2VfDMVK-zVjvYxe_aj-XbJqKffVmKCvhFilBJlSAQMdLjNzLsGAcpaPe7wx89z-1K8qegWrfxW9IzlNkSE6GvrSsG5nWdOKzLlJXsADXZhhLd-5uF2K5R2JhQvNBxnfQDqqUQ6rDt5VhIhZR6JyucBvvOpw_D5-wyg3Dsna3CfImjAietaVSfAubgDeH-sZGTJCuBuGAAfyGd1ECYxOHV6n2rCQlmqf95BY4yqzRgHI540kPAZkFeLYL7ksReUgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تصاویری از یک پهپاد تهاجمی اوکراینی که به طور موفقیت‌آمیزی سه بار متوالی، موشک‌های پدافند هوایی زمین به هوا از سیستم "پانتسیر" روسی را در دریای سیاه جاخالی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69795" target="_blank">📅 17:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69794">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">⏺
معاون برق و انرژی وزارت نیرو:
خاموشی‌ها در مناطق عادی ۲ ساعت یا کمتر است و مناطق گرمسیر به دلیل شرایط خاص، از تخفیفات ویژه برخوردار هستند.
همچنین برنامه داریم تا یک تا دو هفته آینده، محدودیت‌های برق را به حداقل برسانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69794" target="_blank">📅 16:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69793">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJLy7UEm48U_rOHd9P2UEj9VH9zkzGOE5Og-ZSlUKPES4qwW_EOItm4_jswQ16ujGpm8nRB1EFGLiYYQ42-ypM_P8W53F2H83BZEtGbsFsATuSO795flL6YK5VLfiEijspOXhSkavY7UIHVB-yMAcrM1G9qLvHngVMkuOqnsZdcmse1HfFIQsgkq6b-hIb4yzIqUg8cYF7uPEy38oojYlaptamgmfW3kGrHimj8nK4-wseuvzKm55kJd1FjigywzC7R-b7znYC6yO0gBMCQrmE1L3A1k3DPQkQjgp1V7pGjeD_vEcMRIwzkcDQF5JZE-lwv21GFOepMm-JWbw4EwXd3r8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3f5dd815.mp4?token=HJMQKtL9aPe-S0PWDnU2AIfHNMaGbr8IJ7krIx1zt1l64_uT9Grx-1xAwq4nGgy3WeaVDxUSfCGmQHyU9oXfRTcqi775KadQsbd4HC_lLPjYiutXiJuKi9Yud2ZTq77t5E6f7lSttVW5_-628CvOew09Rro_ETy_sR1xqZYsgj9CR2GHKXP8z1nV6RpRBdA5l-SftU8DZ1j5eI50ngWMgGG2xt3wTGfvK_pcdD3mJrj-DcHcWc-VKSax0BgIf9ngLsjvG65Uy6LKtA-txaxf4-lQhSOhKQqJ6FSm_X-sFAhmCj9mm6nAKSjtjl-bVx3xhDSfOMcUtfLn6ub5xGbJLy7UEm48U_rOHd9P2UEj9VH9zkzGOE5Og-ZSlUKPES4qwW_EOItm4_jswQ16ujGpm8nRB1EFGLiYYQ42-ypM_P8W53F2H83BZEtGbsFsATuSO795flL6YK5VLfiEijspOXhSkavY7UIHVB-yMAcrM1G9qLvHngVMkuOqnsZdcmse1HfFIQsgkq6b-hIb4yzIqUg8cYF7uPEy38oojYlaptamgmfW3kGrHimj8nK4-wseuvzKm55kJd1FjigywzC7R-b7znYC6yO0gBMCQrmE1L3A1k3DPQkQjgp1V7pGjeD_vEcMRIwzkcDQF5JZE-lwv21GFOepMm-JWbw4EwXd3r8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
به یک نکته جالب توجه کردید که ایران به همه منطقه حتی فرای منطقه حمله کرد جز اسرائیل؟
تا الان به ما حمله نکرده ممکنه تو آینده بکنه ولی میدونه جوابش چقد سنگین و دردناک میشه.
شایعاتی هست که اسرائیل عقب نشینی کرده و ضعیف شده.
این شایعات از کسایی به ما روانه میشن که میگفتن اصلا نباید عملیاتی توی لبنان و ایران بکنید.
لازم باشد بخاطر منافع ملی به بزرگ ترین دوستانمان نیز نه خواهیم گفت.
منفعت اسرائیل رو پایبند به هیچ توافقی نخواهیم کرد و ما مستقل هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69793" target="_blank">📅 16:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69792">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=nSzauzT4zHnYLJmdDv1_IVFveT_b-9FL995Aicet8BvUNMQlqB9ZOzKvjhfWwtQYIv31E4aTgy2FX1yzbveHYYMhxdmNQfxZQsg0pox5Cint9uDl2KQsGyhiMwuGfj8_IZYSDMBqvZMrrJ7gxMdYZVfhvzK8dY5HN-vqdjTBNf3FaDwRWKuN_tOjXXGnw9cCamRWvFQzWhDbs4fZCM-dbSXrCE-8j3nlsn0rwmTCAdzTnh-SDzkD5_mNsCEGZllWXh40BjXSfQ12Ki1PCy85kmQ959QiSQ1AjoNrc0sDxq0fa3k2tZSXIaVhIP2AQcfJA_seUQK770nD0GoTpuiKBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef1f7ed1d6.mp4?token=nSzauzT4zHnYLJmdDv1_IVFveT_b-9FL995Aicet8BvUNMQlqB9ZOzKvjhfWwtQYIv31E4aTgy2FX1yzbveHYYMhxdmNQfxZQsg0pox5Cint9uDl2KQsGyhiMwuGfj8_IZYSDMBqvZMrrJ7gxMdYZVfhvzK8dY5HN-vqdjTBNf3FaDwRWKuN_tOjXXGnw9cCamRWvFQzWhDbs4fZCM-dbSXrCE-8j3nlsn0rwmTCAdzTnh-SDzkD5_mNsCEGZllWXh40BjXSfQ12Ki1PCy85kmQ959QiSQ1AjoNrc0sDxq0fa3k2tZSXIaVhIP2AQcfJA_seUQK770nD0GoTpuiKBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت آمادگی جانفداها:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69792" target="_blank">📅 16:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69791">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=dgN7v15DshiD8AR88pbQytVV36jf0Fy1XWWS6Br0wY62v_mrgLQbdNX6l5qxr5cqZ5DrdYrmZju5amHChjpM4fiMgtWt9swvs3_vIEL2TAQHuO65d3igddOEOtBxX9bw_silZPrt3-oKA-W1VMk61wl6AMR8vRb3qtXLCN2VufErN83IQ5UnxJLFKdNSmH_VIkiOav9fI1Jlm4GQiGAvukxHVS6-cOdyfHNwrCyAjMxSn8hQE-IHTbuovmtZRSvgpJ3hsxwf3gJqCtVc-6gl6ap9Ej2LRax9FEwvDpE8GoRZ6HTrkpzXCZXgF67QksdDDtY81pUWceUTaiSWA4KkKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26df8fab5.mp4?token=dgN7v15DshiD8AR88pbQytVV36jf0Fy1XWWS6Br0wY62v_mrgLQbdNX6l5qxr5cqZ5DrdYrmZju5amHChjpM4fiMgtWt9swvs3_vIEL2TAQHuO65d3igddOEOtBxX9bw_silZPrt3-oKA-W1VMk61wl6AMR8vRb3qtXLCN2VufErN83IQ5UnxJLFKdNSmH_VIkiOav9fI1Jlm4GQiGAvukxHVS6-cOdyfHNwrCyAjMxSn8hQE-IHTbuovmtZRSvgpJ3hsxwf3gJqCtVc-6gl6ap9Ej2LRax9FEwvDpE8GoRZ6HTrkpzXCZXgF67QksdDDtY81pUWceUTaiSWA4KkKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ژئوپولیتیک:
ایران سامانه‌های پدافند هوایی ساخت داخل خود را به عنوان جایگزینی کم‌هزینه‌تر برای سامانه‌های گران‌قیمت خارجی معرفی می‌کند.
طرفداران این سامانه‌ها مدعی‌اند که آن‌ها موفق به رهگیری هواپیماهای پیشرفته شده‌اند و استدلال می‌کنند که فناوری بومی می‌تواند بدون تحمیل هزینه‌های سنگینِ تجهیزات وارداتی، دفاعی کارآمد فراهم آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69791" target="_blank">📅 15:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69788">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pFfWiX1UfdUOCJzbE0geG6tSUQ579atdR1kwPMNNO-8avoBI-MwS6KUKu-KGb5__jUqPiEZAqF9UYV04y830qOQRF0s-EVjq3ZM6TcQTqj-fWZX0Rx7h1jFbxVfqaRnY6JrJDQgyBzoENmlRkqZ-X_L7digtcEhy4248Lu8SSr-ZPxVMzblpfT8pF5wxGff0Bcj5RoS8QZK2po5nHVZJk4kVX-xT54uxfSrEX63rGFlO8ljLRprXFoJ5X1BSlGz2XTMa_AZZHlnmAL284oxs3d3agcYb7k6Ph3AfJbtTGq-7hQoKBbK4DcFkpwWUyXpd_nsQNhJSZUmqNq5RTjKSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPABaZniwyBVT1r4QzLtbrlb9iG6yNVFuvscJ5mugwnIAURuQXhgGnF49zpUMjCTw5AXU9y7oAofAwQqVIIGIVEkyhI659zmGfYK5vA-f7P5rrjyIbEBQAQu_go3hYjpNrUaKVbkl_nTiXwMziNZhiHaxx47f364adAWgJXYPbckX0M1k37H8GHvJ22T2caRefSDJ-0-vS6GT_CYxC3Njep5EUUNC1KoP2A7kRwFMZqsyLAYhg8-5DBJsH0xcx3d4tkO-wLg4sXiPqnEnmuS_6Yd-hNKmh9X59GOiUA9Wtbvm9Wf6CsPS5wlAqy7NvRPXKvFj6s7QJIQId9yNOYzJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vm65-ccCLUi3ZIN0n0XoovKktkwXu9F_5pJJLMUPfGU_R5JaHqBtz4Z-QznV6n63iUbM8rwL-ICCKr4KgfDifaOSwaN45hvkQoqtPerh4kafM-bHNKTi1Tpe2sDhHPP1zIV8E9ii5Ior7wtN0OI0YZv7iTXHwubCcQMA_wdRjwfYIpzld17BdcXXSSpHvINE97ayaryryumelnm0IaPUOmgsmGbasR4KIv21VXmsyG3SkI326HDraRyke9cYklblsNbVJRw-0pE09IGFDtXbiGYV86DiaDKlgmnnINZlzZnFo-yjDKa-NBEiD3kVDJS2e3zoEft_P5DTDeBIT4C8Bg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🔞
ابعاد جدید ماجرای قتل حمیدرضا رجب‌زاده توسط یک بلاگر دختر:
حمیدرضا رجب‌زاده، یه مداح جوون، بعد از خروج از خونه ناپدید می‌شه. پلیس در تحقیقات به یه بلاگر زن می‌رسه که قبلاً با حمیدرضا در ارتباط بوده و اون روز هم ازش برای یه ملاقات حضوری دعوت کرده بود؛ حمیدرضا به این دختره بارها بخاطر حجابش تذکر می‌داده و بهش می‌گفته بحث سیاسی نکنه
طبق اعتراف متهم‌ها، این زن با کمک پنج مرد، حمیدرضا رو به یه محل خلوت کشونده، بیهوشش کرده و بعد اون رو با ضربات چاقو به قتل رسوندن و قلبشو از سینش دراوردن و رو صورتش مایع منی ریختن، بعد هم جسد رو به اطراف پرند بردن و آتیش زدن و از صحنه قتل فیلم گرفتن؛ با اینکه چند نفرو گرفتن ولی متهم اصلی هنوز فراریه!
🔞
ویدیویی که قاتل منتشر کرد
⚠️
⚠️
حاوی صحنه های وحشتناک
⚠️
‼️
اعترافات بلاگر دختر:
من با مقتول در فضای مجازی آشنا شدم  او مرتب به من تذکر حجاب می داد و می خواست درباره مسائل سیاسی حرفی نزنم و زندگی مناسبی داشته باشم من این موضوع را با دوست پسرم درمیان گذاشتم که او پیشنهاد داد مداح جوان را با بهانه ای به محله خلوتی  بکشانم تا او با دوستانش دست به قتل بزنند او گفت که گروه های منافقین بابت قتل بسیجی ها پول پرداخت می کنند بخاطر همین بعد از اینکه مقتول کشته شد فیلمش را گرفت تا به آنها بفروشد
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69788" target="_blank">📅 15:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69787">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va2volccrWCv2kHqSnZUZGEuRxSaEWe51VIhjPO0beUTOP7aIIk-cafBcBrbw19OAj0z0-PUoSwtCDoTnQ0kdIv9c5SeCsQYDKyqikCZZA7r9BWQOZQB0J0EzfIsPZGb138szwITikakCOYyC-3uef6wcsC4sOL8aVnrnIN0zzt_rGfptAPkVM_I4pALOU4t-LMG0LFwKOtYKyadNxVY79lYsEfzIp2KFsRhVv3xzutPyd6aA25HO2QjjONGMEjRFFseGRBw3fNNCHDJAHo9FkfWPUf86jKQ_gzGta5Bm09EviNaAxhkCuCxUpzEOJTRzaH9EO-EsyTRz1vr1BqC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
فرماندهی مرکزی ایالات متحده:
ملوانان آمریکایی در حال تعمیر و نگهداری هواپیماهای F/A-18E Super Hornet در عرشه پرواز ناو هواپیمابر USS Abraham Lincoln (CVN 72) هستند تا اطمینان حاصل کنند که تجهیزات گروه ضربت ناو هواپیمابر برای اجرای محاصره ایالات متحده علیه ایران آماده ماموریت هستند.
تا 8 آگوست، CENTCOM 53 کشتی تجاری را تغییر مسیر داد، 2 کشتی را از کار انداخت و 2 کشتی دیگر را نیز توقیف کرد.
🔴
ارتش ایالات متحده همچنین به بیش از 30 کشتی اجازه عبور از محاصره برای کمک‌های بشردوستانه را داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69787" target="_blank">📅 14:59 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69786">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
ادعای فارس:رئیس‌جمهور با رهبر معظم انقلاب دربارهٔ مسائل اقتصادی و نظامی کشور دیدار و گفت‌وگو کرد.
پزشکیان همزمان با شروع سومین سال ریاست‌جمهوری با حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای دیدار و گفت‌وگو کرد.
در این دیدار به‌تفصیل دربارهٔ مسائل و مشکلات کشور به‌ویژه تأمین نیازهای معیشتی مردم، شرایط موجود جنگ تحمیلی سوم و آیندهٔ پیش‌رو، تحولات حوزهٔ نظامی، راهکارهای ناظر به تأمین منابع و مدیریت مصارف «ریالی، ارزی و انرژی» و همچنین تعامل اقتصادی با طرف‌های خارجی تبادل نظر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69786" target="_blank">📅 14:23 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69785">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
صحبتای این خانم در مورد کافه رفتن و پیدا کردن پسرای پولدار، خیلی وایرال و جنجالی شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69785" target="_blank">📅 14:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69784">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=U1l1NXNitfvjzM6sPuFqoPC2KWaYGdCAlVHddeLePXcFEIcEcBbF2e7B-cCR_XaXiFuODwKNcpX68FbNz2eu229yNCBwCsCZXnGi9rXqVGXSg-0BjMkIi-NGlBqeziAaEC2PEO31ph5Dp0e60etNk04TegIjmYDXnPrHdefWTsOy82JD3USiDwrjJa26zQROUxvy4ILz81vaiDuNbUhccjPnY7RrF5Umj0-QN9xXL33K_XYdCiuXrGUI6ixYhvl81FTLnwhqkzN4fBAPi44kKgWHwvl07gkC1hcIIwlR0vEbTD2V7cDTSo71azMtUjIOYfW5p0fPoAcVHrDBc-YBSm8-mKZYKhS9mvYrsqrzkqGiMHeUXtHjaVpY0s4e4Zn1bf1xT2ZRihNbpvf529h_eCY_lMXno-vDObss64uvgEXzG_UnJybUUEPR4AhQGSZEVsakJCGHPsTsha2Re2KxA5Ptdv7Uu3SD4V4Z_hyzMy7car15ncZZg61LAqozX0bOluOF2nE2Ojrh0WjAUNFcIy9S1GjPhr6qRpWHX1huTVz8xIOq5j1WIRumwTbygFascy1c_vELSiPIBJ0uP_e9xZV3XOEvD-HhZ7D20PruRANmBviLNtbHdRAnbXmRkFRq-xJBR1tXO1uNM49JURH4K_EzlrGptyZ_ktz7SFFCx1U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab9ff0322.mp4?token=U1l1NXNitfvjzM6sPuFqoPC2KWaYGdCAlVHddeLePXcFEIcEcBbF2e7B-cCR_XaXiFuODwKNcpX68FbNz2eu229yNCBwCsCZXnGi9rXqVGXSg-0BjMkIi-NGlBqeziAaEC2PEO31ph5Dp0e60etNk04TegIjmYDXnPrHdefWTsOy82JD3USiDwrjJa26zQROUxvy4ILz81vaiDuNbUhccjPnY7RrF5Umj0-QN9xXL33K_XYdCiuXrGUI6ixYhvl81FTLnwhqkzN4fBAPi44kKgWHwvl07gkC1hcIIwlR0vEbTD2V7cDTSo71azMtUjIOYfW5p0fPoAcVHrDBc-YBSm8-mKZYKhS9mvYrsqrzkqGiMHeUXtHjaVpY0s4e4Zn1bf1xT2ZRihNbpvf529h_eCY_lMXno-vDObss64uvgEXzG_UnJybUUEPR4AhQGSZEVsakJCGHPsTsha2Re2KxA5Ptdv7Uu3SD4V4Z_hyzMy7car15ncZZg61LAqozX0bOluOF2nE2Ojrh0WjAUNFcIy9S1GjPhr6qRpWHX1huTVz8xIOq5j1WIRumwTbygFascy1c_vELSiPIBJ0uP_e9xZV3XOEvD-HhZ7D20PruRANmBviLNtbHdRAnbXmRkFRq-xJBR1tXO1uNM49JURH4K_EzlrGptyZ_ktz7SFFCx1U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
عباس عراقچی:
اکنون هیچ مذاکره ای با آمریکا نداریم و نخواهیم داشت
شروع مذاکرات بدون پایبندی آمریکا به شروط تفاهم‌نامه غیرممکنه
ملت ما تسلیم اراده یک عده خاص نمیشه
بدون تحقق حق ملت ایران کوتاه نخواهیم آمد
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69784" target="_blank">📅 13:15 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69783">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34556823e0.mp4?token=fT0B7YGmbam_-7JkxSzlbdJiOnzV7GhX5ACZpjZ7631iby4eAl5A7JTl-3K-8MK8WqYypq6KGzi904WkgW_YNrx8aGv6-1Si1R7XBREVzavTQj6u0PtO7Dz1mD3Iquqruv5LO8EJ4fT7HyfiAvoDdf5nTEKTnq6zS5tJbWobeTLKVNaxqK809Xt0pufjo6AbGRFilGe2gBM1L6hULoBaMIOyliiHSQswuNTyi41sUtKbJyqIweldzn2Ndf-7s1nPHhxS9gDMK1RFtpJPWJJdQdDvbERusjSDUejH3bIq7YknHZ9seGDDQF-BN8rDn-qUNjEZs8Y5DROefhN7mptkHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34556823e0.mp4?token=fT0B7YGmbam_-7JkxSzlbdJiOnzV7GhX5ACZpjZ7631iby4eAl5A7JTl-3K-8MK8WqYypq6KGzi904WkgW_YNrx8aGv6-1Si1R7XBREVzavTQj6u0PtO7Dz1mD3Iquqruv5LO8EJ4fT7HyfiAvoDdf5nTEKTnq6zS5tJbWobeTLKVNaxqK809Xt0pufjo6AbGRFilGe2gBM1L6hULoBaMIOyliiHSQswuNTyi41sUtKbJyqIweldzn2Ndf-7s1nPHhxS9gDMK1RFtpJPWJJdQdDvbERusjSDUejH3bIq7YknHZ9seGDDQF-BN8rDn-qUNjEZs8Y5DROefhN7mptkHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا متوجه بشید با قیمت الانِ یک نوشابه، تو سال ۹۵ می‌شد چه چیزایی خرید...
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69783" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69779">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJBcDZ1Q55qj-HlFIIbkWEW0wQts32UkQiZ0o2zuR1sC9J-p3oYrwZKHOQEP84GQxoroSq13unFM0bLGoI6sCkQoKOijvnRUY6-p1EVgvEi5cZoFZLWsvOJvVGTHgbZz4qWQQPiwUvodQN56xpOgRQnOgWZDj6aL6LF9RgIdCbYrRtoeWiijnnH3HtCop6Q0Web_7lHQjLkcMzY0QmWQMsOxDnTPFpFjHJHaGP6J8DzuusBIJUqtxwUOWtWOtFb-aSZ5_o0ECzllZmkbZBr3P2eAWlOWinpjmxbVAZXL_KgVE63ERfQkWjpgRuf3sq89SXJRxA3u4l4KI_5rwLSzMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=TXB8x3w1N3MVZN8Jn2NhELp98npyQudQlNO4oBTVx3IwRzh_uxrJRmFy7RpsF7Z48C2uZyFz4vJGMXHkW5KyAaDi9hqqwnfUR0ygAL3gqsUd5XtjoRx1Or5-QXJgbGaU7LkhCQU4tPGivwfWNYDpsU6f1w-OjTifpSnJpSMgFlPLRZJRAda8Jic2sO-ZsrfbSeDAIn6ylSaHnDR64Hae6g4b57P6GhhakrX3sPC1lSYt8nY_j0gK1MZcgqS4DaSeZVqBzK0RyPKd2nvwRFKC7knfvR8EkwegoqCRRmZuWIumekrpUmNjpbNPKimfNzuEKABXGyCgn5yo5GLyTVBmsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e5f1aeb56.mp4?token=TXB8x3w1N3MVZN8Jn2NhELp98npyQudQlNO4oBTVx3IwRzh_uxrJRmFy7RpsF7Z48C2uZyFz4vJGMXHkW5KyAaDi9hqqwnfUR0ygAL3gqsUd5XtjoRx1Or5-QXJgbGaU7LkhCQU4tPGivwfWNYDpsU6f1w-OjTifpSnJpSMgFlPLRZJRAda8Jic2sO-ZsrfbSeDAIn6ylSaHnDR64Hae6g4b57P6GhhakrX3sPC1lSYt8nY_j0gK1MZcgqS4DaSeZVqBzK0RyPKd2nvwRFKC7knfvR8EkwegoqCRRmZuWIumekrpUmNjpbNPKimfNzuEKABXGyCgn5yo5GLyTVBmsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله پهپادی اوکراین به بلگورود
نیروهای اوکراینی شب گذشته حمله گسترده‌ای پهپادی به شهر بلگورود روسیه انجام دادند که در پی آن چندین ساختمان مسکونی هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69779" target="_blank">📅 12:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69778">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69778" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
r18
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69778" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69777">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N33x72PvhTEWZVK69ez0p9P-HDgf4t2EBz6xUJ7kjjf_ygVVHYIK6di5MbtLrMiV1-fXagCZcyaP8X6lzLJPKKi7RkHGQZJvcIGrMqd_1hf5HuqIASxb-FS_VBXArwIQ8Fr71LeFIJq1KKkjTP4M6odd57f0PUZG_ZfYnKpQjMPperCcXdu-M8Zif2HPTlzG7BQ5FH1olhezS0GkEhHQNQNn4k3z0TnWhbPD_MuvjJZjCMpwQQL9ipQhtE3Te-z-dN3HyD3GT9Ec-avYS0Tusnk_EbzG0c1aoaae39DZ14oGFhs3J2uqj-gVuSi_ta3REd6r7sEJh6iXs9BfrnGOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r18
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/69777" target="_blank">📅 12:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69775">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=L-7eLGjmLPK0iNA8brl-rOXBpCL8pguEv2R38kvjXsytmnQ8YR-tXPpIp1b8hQFgMXWBARsKgMZnSuzJ0bq7MM_iWGJQ_9XQa4h3LAwMilK6Vchl-pWWdqdlZC0-VANaUk9K-hQO0TM8PCZj_o6L6_mh74GV-FO31o98IZkTwKwsQW57WQZs9bDNPbDd5b1S4BndR2XxH6AxujRc-jCc30ZG7g2WJv_WfJ-wvEyYArku4T_RNdSPEsBlV3Essx5z-ughhKVSQD2o_C2xX2C8gwkAQTToxZZd4xBiEnIDJZSI4PcHRPPlXzGRFE2lP6CD558mXdb1pQxWKma5_Mss6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c93de8243.mp4?token=L-7eLGjmLPK0iNA8brl-rOXBpCL8pguEv2R38kvjXsytmnQ8YR-tXPpIp1b8hQFgMXWBARsKgMZnSuzJ0bq7MM_iWGJQ_9XQa4h3LAwMilK6Vchl-pWWdqdlZC0-VANaUk9K-hQO0TM8PCZj_o6L6_mh74GV-FO31o98IZkTwKwsQW57WQZs9bDNPbDd5b1S4BndR2XxH6AxujRc-jCc30ZG7g2WJv_WfJ-wvEyYArku4T_RNdSPEsBlV3Essx5z-ughhKVSQD2o_C2xX2C8gwkAQTToxZZd4xBiEnIDJZSI4PcHRPPlXzGRFE2lP6CD558mXdb1pQxWKma5_Mss6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⚡️
تصاویر جالب از لحظه برخورد رعد و برق به ساختمان مرکز تجارت جهانی «اسپیرز» در نیویورک؛
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69775" target="_blank">📅 12:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69774">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=KboZ14IJmDU9JhRDZc3wnhmjxzK1a2WEOGOqMgQiqqRWI8ns-ytO5tIPJKUk84UPPLsggQA5sxh-hxv9jeLz-N4GBQTmAACt5ZjoK0968I4BUv6c5jiz9AIcEzbVUcd6w3wN0q6_2bpmwiZhQjt-hauD_lIxFXSqawQXEvZ5s4KWfYov1MLPEmk5rU95Pt5u06n89ON55bQ_pwI195raVci_iB5xSSTWi4kofvI_aFZiFjTRMttH6EO5DJZsUjvdC4lNntsjk1CTTlUNZazSSQLUGdQbfBX8OKH0ByKyU_TLxbOilN7CoiMTouOPJc0cz7--SEkxVkeciSQ2U1qbJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b13fec044.mp4?token=KboZ14IJmDU9JhRDZc3wnhmjxzK1a2WEOGOqMgQiqqRWI8ns-ytO5tIPJKUk84UPPLsggQA5sxh-hxv9jeLz-N4GBQTmAACt5ZjoK0968I4BUv6c5jiz9AIcEzbVUcd6w3wN0q6_2bpmwiZhQjt-hauD_lIxFXSqawQXEvZ5s4KWfYov1MLPEmk5rU95Pt5u06n89ON55bQ_pwI195raVci_iB5xSSTWi4kofvI_aFZiFjTRMttH6EO5DJZsUjvdC4lNntsjk1CTTlUNZazSSQLUGdQbfBX8OKH0ByKyU_TLxbOilN7CoiMTouOPJc0cz7--SEkxVkeciSQ2U1qbJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
گوشه‌ای از سخنان وایرال شده خرازی، برادرزن مسعود خامنه‌ای:
جمهوری اسلامی یه موشکی به اسم «رستاخیز» داره که میتونه یه دور کامل دور زمین بچرخه و به راحتی خاک آمریکا رو بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69774" target="_blank">📅 11:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69773">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0189fef147.mp4?token=qy2Q8O2MQ8zMD3rET7DsFch6MfGG54wTQhuCkB2Mpo8Hlse6h50qK9J2JGYjj_1Hq4sZixwBMNVQv84xPM7BJ4G2b8DO3AngcDjo2-4QKab8czDYxXs48eUGvKwNORv1yKEOQpGnbsvznNCRN2RKx83kLpITnSfTlCkqk0gWneroKqG2a8VTMLbpixQzvK3m8lhDcxtyYz5o6YrjNMh1lk0Wbdazyn7UgA0oBepAyryze4bi1z9YuHrGUB2vGwmLLIrbkQvjzibH8Ps_2-Xd-smkRAM2PiyePD9xtdr5URKbX7dHrqWIoD3nQKs7RQe-mJzzjiLYOJ39rmnOhyvrG2jupFZPWzsJq0oUTlXiUt1Qi29UzZosfOGnl7rCIiBPcpDYLLELAuZzKueiQUrqkbRwsHBgD9CkYZnyV8JgTpPCD4Rtwbf-RMb71riuCu1w3zJ5jVr-oezpfLreAlIH2KBqc1E4A211H53HZVihN5zQ3l1i6TY2vuQrKajhIrxgIUahig5XcpWXukPVeoZrxEVKjWZTUa7sEVwMEvp_DQDqJxmqAAwQGC389ILRJQ8P1hy4x3VCh3XQ4TSiJ9jiIy-C578Cg9Piw8DXDyBAxVRud6NyDuYjUinKGnb5FrSo4iCvEXyyZZv6_n_69xQPyJyHI4W2scCG_VwRkuXUVhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0189fef147.mp4?token=qy2Q8O2MQ8zMD3rET7DsFch6MfGG54wTQhuCkB2Mpo8Hlse6h50qK9J2JGYjj_1Hq4sZixwBMNVQv84xPM7BJ4G2b8DO3AngcDjo2-4QKab8czDYxXs48eUGvKwNORv1yKEOQpGnbsvznNCRN2RKx83kLpITnSfTlCkqk0gWneroKqG2a8VTMLbpixQzvK3m8lhDcxtyYz5o6YrjNMh1lk0Wbdazyn7UgA0oBepAyryze4bi1z9YuHrGUB2vGwmLLIrbkQvjzibH8Ps_2-Xd-smkRAM2PiyePD9xtdr5URKbX7dHrqWIoD3nQKs7RQe-mJzzjiLYOJ39rmnOhyvrG2jupFZPWzsJq0oUTlXiUt1Qi29UzZosfOGnl7rCIiBPcpDYLLELAuZzKueiQUrqkbRwsHBgD9CkYZnyV8JgTpPCD4Rtwbf-RMb71riuCu1w3zJ5jVr-oezpfLreAlIH2KBqc1E4A211H53HZVihN5zQ3l1i6TY2vuQrKajhIrxgIUahig5XcpWXukPVeoZrxEVKjWZTUa7sEVwMEvp_DQDqJxmqAAwQGC389ILRJQ8P1hy4x3VCh3XQ4TSiJ9jiIy-C578Cg9Piw8DXDyBAxVRud6NyDuYjUinKGnb5FrSo4iCvEXyyZZv6_n_69xQPyJyHI4W2scCG_VwRkuXUVhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابای این دختره چون دخترش توی امتحان گواهینامه قبول شده براش BMW 225 خریده ناقابل ۱۲ میلیارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69773" target="_blank">📅 11:04 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69772">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/973161bf95.mp4?token=N4fOvLI1gPwjsHi4CjCLBAMaka9OhJXeDwbBpEsa4DZh1c1JQjSMWp3EDaNecVG8vBiARuSb9M_jc4JnYvoQVAyTj0CkneiyrtPcD8cXrhgtHBHYd3aU3RX4RomgyvSIFTIg6_U9TAMNAIdxBCWTC5IS-DJcJgkg9_O28GVYbMvWkDaSgIPcmLwK6PsvY5-8TFv7OZx15AJdcDcQ9Ciib6DQUyOl4ZPktd4PfcMoUaZcclatMp5NVBGCdkNAVTVq-33LGjvNAyl9y4FnX7PSWAcf_F79BFRINukiFCDVlQ4DPJwz_5iFRM7AuCsgRTg7kgZnA9Ob39TNfStu8OiMag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/973161bf95.mp4?token=N4fOvLI1gPwjsHi4CjCLBAMaka9OhJXeDwbBpEsa4DZh1c1JQjSMWp3EDaNecVG8vBiARuSb9M_jc4JnYvoQVAyTj0CkneiyrtPcD8cXrhgtHBHYd3aU3RX4RomgyvSIFTIg6_U9TAMNAIdxBCWTC5IS-DJcJgkg9_O28GVYbMvWkDaSgIPcmLwK6PsvY5-8TFv7OZx15AJdcDcQ9Ciib6DQUyOl4ZPktd4PfcMoUaZcclatMp5NVBGCdkNAVTVq-33LGjvNAyl9y4FnX7PSWAcf_F79BFRINukiFCDVlQ4DPJwz_5iFRM7AuCsgRTg7kgZnA9Ob39TNfStu8OiMag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
علی مطهری، نایب‌رئیس پیشین مجلس شورای اسلامی:
از همان ابتدا، هدف ما ساخت بمب‌های هسته‌ای بود و باید تا پایان ادامه می‌دادیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69772" target="_blank">📅 10:32 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69768">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=VnlAdhX1fsqFDPM6EusgeczBWF1AVtl8QOtDKjHdpI0Od5rCLvJgiQdxFMxaDTt-mCEKYsuTUNeCGFBsZx2IOskP-OqqMRaO0SnUdBbx0wza4cf9-KGDEgzQdi8KT1uvvQmIJHlEnYztJi6dUXaLgWEg6i8ZAJSiFbTNYi09qtiYW9kxnBmEHOweCJUUTb1_4FB0tYsSSiwdjcNgGMF9gzQQQULGBGFK8PIafeVdfsAwKIVHBPIStuEkfWy88CH4z9RG6H7yTUhTth-Z2jwDKDzETAZFvoJnbYsEtJiNTbiPdZIIlPYbSqqQVW-dAcx-w5yMqqITcScCsRENVR0y0A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=VnlAdhX1fsqFDPM6EusgeczBWF1AVtl8QOtDKjHdpI0Od5rCLvJgiQdxFMxaDTt-mCEKYsuTUNeCGFBsZx2IOskP-OqqMRaO0SnUdBbx0wza4cf9-KGDEgzQdi8KT1uvvQmIJHlEnYztJi6dUXaLgWEg6i8ZAJSiFbTNYi09qtiYW9kxnBmEHOweCJUUTb1_4FB0tYsSSiwdjcNgGMF9gzQQQULGBGFK8PIafeVdfsAwKIVHBPIStuEkfWy88CH4z9RG6H7yTUhTth-Z2jwDKDzETAZFvoJnbYsEtJiNTbiPdZIIlPYbSqqQVW-dAcx-w5yMqqITcScCsRENVR0y0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ایشون به اسم آرش، خودشو اولین:
همجنس‌بازه، شیعه، پادشاهی خواه، دو رگه تُرک و لر معرفی کرده که پشمای همه ریخته
😐
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69768" target="_blank">📅 10:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69767">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=hgb-rvTSqx5e28xUMGdQSbYmshb_M3IRK5kAGz7uWzBKjRoFm9Cz1KSR-AdLcbNkwGJlSUiL2zjhdTW0meNrJG1z7a3gqwnRbeDwJOwQlmTCrNq9pIcgjAKqozHY0xSH9DLDdv0vWgwgQoYPeMmJKS7QEybSZOXR2OLDpeVyJUtD7CeELS2oa9YZYOHHp-xFrsD7_2nsdET9Rx3JiL8WaOcJ2x_Bd7DmGaoGnKT9dWVdn-b6B90RQsnr1CTCVn50Y1QOvY4XemkUqQtaa9IwTiFmWPxmy_iLoq3P4YfzvGrCdQ_eAyNqYg0-se_2xEyfnLF6YplywEqfCacR070jTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c02b892b.mp4?token=hgb-rvTSqx5e28xUMGdQSbYmshb_M3IRK5kAGz7uWzBKjRoFm9Cz1KSR-AdLcbNkwGJlSUiL2zjhdTW0meNrJG1z7a3gqwnRbeDwJOwQlmTCrNq9pIcgjAKqozHY0xSH9DLDdv0vWgwgQoYPeMmJKS7QEybSZOXR2OLDpeVyJUtD7CeELS2oa9YZYOHHp-xFrsD7_2nsdET9Rx3JiL8WaOcJ2x_Bd7DmGaoGnKT9dWVdn-b6B90RQsnr1CTCVn50Y1QOvY4XemkUqQtaa9IwTiFmWPxmy_iLoq3P4YfzvGrCdQ_eAyNqYg0-se_2xEyfnLF6YplywEqfCacR070jTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه طرفدار حکومت درباره حجاب:
آقای پزشکیان واقعا مرسی که گفتی نمیتونم قانون حجاب رو رعایت بکنم
مجلسی که ناظر هستی توام دمت گرم که اصلا فکری برا حجاب نمیکنی
پزشکیان داره میگه ععععععع مگه هنوزم گشت ارشاد هست؟؟
بحث دیگه حجاب نیست بحث پوششه پوشش و اصالت ما داره از بین میره
تو خود اروپا هم قانونی برا پوشش هست نه اینکه لخت بریزن خیابون
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69767" target="_blank">📅 09:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69766">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=aDcrxpucNhkX19_mESX5w8zZO3B00KOSRhYab_XTrPCsr6UPh2Wt_7qIx6fc0txqTj_kdq6AFagrCCmQflWW7elEYtf3FFVKK-qY4wtlmv4naQkWAFE8acmRRBl6PUmGqd3QlArRbeiKWb4I3GGd30RWndDAks09VJkEzmUE2Ro6izWsf6qe3e7Vw_dqlym4twYpTXbjFYdRpgjWpy0MScJKGKirRE-2BKNiCsadgo7k15JrRuS7X6JNzMA8JogrV_7HwKD7JXw2bdqx0_BlF6_AoCdH2p4Vws_XwKjUrzWfmYn8k_SJb3w-IHW5qFpJj7aR20ziwjHb53CuluynNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed36a1671.mp4?token=aDcrxpucNhkX19_mESX5w8zZO3B00KOSRhYab_XTrPCsr6UPh2Wt_7qIx6fc0txqTj_kdq6AFagrCCmQflWW7elEYtf3FFVKK-qY4wtlmv4naQkWAFE8acmRRBl6PUmGqd3QlArRbeiKWb4I3GGd30RWndDAks09VJkEzmUE2Ro6izWsf6qe3e7Vw_dqlym4twYpTXbjFYdRpgjWpy0MScJKGKirRE-2BKNiCsadgo7k15JrRuS7X6JNzMA8JogrV_7HwKD7JXw2bdqx0_BlF6_AoCdH2p4Vws_XwKjUrzWfmYn8k_SJb3w-IHW5qFpJj7aR20ziwjHb53CuluynNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو وایرال شده از فردی که در زمان رفراندوم سال 57 حضور داشته
:
وقتی من روز رفراندوم رفتم بیرون و دیدم گفتن ۲۰ میلیون نفر رای دادن زنگ زدن آدما بهم گفتن بیا ببین چخبره.
اونجا رئیس حوزه آخوند بود و این بیجک های صدتایی رو میدادن دست مردم میگفتن بنداز صندوق بگو مرگ بر شاه.
جمعیت ایران اون زمان ۳۷ میلیون و ۲۰۰ هزار نفر بود.
کل کسانی که بالای ۱۶ سال بودنو و میتونستن رای بدن ۱۸ میلیون و ۷۳۲ هزار نفر بود.
آمار رو با خنده اعلام کردن ۳۰ میلیون نفر رای دادن.
توی وزارت کشور گفتن که اینطور نمیشه پس گفتن ۲۲ میلیون و ۴۰۰ هزار نفر رای دادن و ۲۰ میلیون و ۴۰۰ هزار نفر به جمهوری اسلامی بله گفتن.
اینو حساب کنید دیگه از کل ۱۸ میلیون نفر واجد شرایط مخالف بود مریض بود زندانی بود و.... از اینجا بود که من راهمو از اینا جدا کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69766" target="_blank">📅 08:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69765">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/news_hut/69765" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69765" target="_blank">📅 01:46 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
