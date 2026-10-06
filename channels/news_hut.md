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
<img src="https://cdn4.telesco.pe/file/eGFEi3ORE3IVwqZ1fwZJWmaoi4ShnvAX42LasSw0K2gRsGpszqN1w4FMKLdOnNqhyTCABI_-2av5u46eCNddOpwz2y3hyHeKhGNRGXqufOwLUg8PtuE0jTVQQdEfL0AwDnCP468DmG6TRkSeWs2-EGwCw_5YnetNMqLMNhogOG5GTjHjd49eGu85fVwljVuupWiOYoYG7yq3cR4rrm-HTayYb4R0SYgm_M6ZtpGJSP30yHTW73r6c6LKE7hpsCEQH3AGm1m1SJsaZnzT9QlUtL2ye-dg0ZxtITU6TX72EArnK59Tjlh7T85z7VCtPobfF81i71ZmulAQ80Ro01MbtQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 17:18:01</div>
<hr>

<div class="tg-post" id="msg-72833">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=aamscDhwd7r166cAwdI_A0bsel1gqbH018rmLibAdyLoOVjfQKuSUEzQQU9JAqYu83grZBW3FGaYv1cZKwSJFYU4LqNwfLgOvCdAV542_goLb1RnnKMusK6Vg4VtpqzHetpcl7Qb_z19fD_EN0YuGXmKlem2zYEL4tkNicC3K-_io_IHL-32HotK3Ocl0Zj9Z0je0tGuHo2GtujU7FurdwZh7jmRBExZsqr7iq--1IZRWAXLCVJEANGfvYUUojI_scwK2-HRwjhf1bcd4sdvAc6DVZfFeyCSpYWMvr1fCkw4PVl_Ib6eaxnD6HpOarNb8jwXkYKcqLtoWeiEdNBVZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab24bbc88d.mp4?token=aamscDhwd7r166cAwdI_A0bsel1gqbH018rmLibAdyLoOVjfQKuSUEzQQU9JAqYu83grZBW3FGaYv1cZKwSJFYU4LqNwfLgOvCdAV542_goLb1RnnKMusK6Vg4VtpqzHetpcl7Qb_z19fD_EN0YuGXmKlem2zYEL4tkNicC3K-_io_IHL-32HotK3Ocl0Zj9Z0je0tGuHo2GtujU7FurdwZh7jmRBExZsqr7iq--1IZRWAXLCVJEANGfvYUUojI_scwK2-HRwjhf1bcd4sdvAc6DVZfFeyCSpYWMvr1fCkw4PVl_Ib6eaxnD6HpOarNb8jwXkYKcqLtoWeiEdNBVZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن بیژن مرتضوی : مردم ایران در دنیای واقعی خیلی خوشحال و شاد هستن ، واکنش ها تو فضای مجازی دروغ هس و حقیقت نداره
@News_Hut</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/news_hut/72833" target="_blank">📅 17:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72832">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=fAE1aXUiLMJ7lb7_7E5BBmct_cRisGst1sHBrA-ImHcj1IUGkdPCkqqx-h4noBaiR00dxghg39BfXLEYSrLnBzWH7HGZoBGFfSgXfaph40NPyx-Cud8_zP8Kf66ygAbyHbQ9SIIw2YzdaUgKBTMRzIMdIoGBfsAUAeQy5tModqLBuwAEO3Hz9wXPfMkXGwltFDzUiF76ArILZ62uqZAURsZTrLx1zxVUSMDHT9zPOGYPyF5fSMYRD33yasnJEf-37CgApXxYQm2w1mbzpjhF9BiIuyxPYxrlC2G6fOETEBd9L4fSVdHDAnJXCzNmI-mwT3CuI9vbR9x1YaKwnqAbnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be4d4d973.mp4?token=fAE1aXUiLMJ7lb7_7E5BBmct_cRisGst1sHBrA-ImHcj1IUGkdPCkqqx-h4noBaiR00dxghg39BfXLEYSrLnBzWH7HGZoBGFfSgXfaph40NPyx-Cud8_zP8Kf66ygAbyHbQ9SIIw2YzdaUgKBTMRzIMdIoGBfsAUAeQy5tModqLBuwAEO3Hz9wXPfMkXGwltFDzUiF76ArILZ62uqZAURsZTrLx1zxVUSMDHT9zPOGYPyF5fSMYRD33yasnJEf-37CgApXxYQm2w1mbzpjhF9BiIuyxPYxrlC2G6fOETEBd9L4fSVdHDAnJXCzNmI-mwT3CuI9vbR9x1YaKwnqAbnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خوش چشم بازم تحلیل کرد و گفت جنگ در پیشه!
@News_Hut</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/news_hut/72832" target="_blank">📅 16:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72831">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=gZEphx0wKm5eUfxPRoTRATcgRTbLZZBUDxX5Py6rzbFp83jR3MZSt-1uGgg3AtepOLOnsF4XL5U1NVN-mb1FAO6WVD_UFlEWAhimzXRqDjJadYUwoza3Qef274qvU2imkqFS3Q5jT_cuYEo3yX9bAmQJQ5F-aQMK94-ky7cWoTtsZc-V1hkLyW1DhaA0hO5ln_YFzr-3TZ_v4jQ3SrVrzaAI-HglcWoxRBurjuaiFuRRSSGnH3k-nybMe7tBQHfkQQ7S9nMBzR6lmauIy72Og2aFD32Eka03xpyUbW3Zogv_4xyh9uQtVL3mQcohL5gzUKc4mxRWVNd_-Q0DXGqnEg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cd2b481530.mp4?token=gZEphx0wKm5eUfxPRoTRATcgRTbLZZBUDxX5Py6rzbFp83jR3MZSt-1uGgg3AtepOLOnsF4XL5U1NVN-mb1FAO6WVD_UFlEWAhimzXRqDjJadYUwoza3Qef274qvU2imkqFS3Q5jT_cuYEo3yX9bAmQJQ5F-aQMK94-ky7cWoTtsZc-V1hkLyW1DhaA0hO5ln_YFzr-3TZ_v4jQ3SrVrzaAI-HglcWoxRBurjuaiFuRRSSGnH3k-nybMe7tBQHfkQQ7S9nMBzR6lmauIy72Og2aFD32Eka03xpyUbW3Zogv_4xyh9uQtVL3mQcohL5gzUKc4mxRWVNd_-Q0DXGqnEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدنی وزیر دلقک اقتصاد: درمورد قیمت ارز از همتی سوال بپرسید.
خبرنگار: همتی هم گفت از شما سوال بپرسیم.
مدنی دلقک: نه دروغ میگه از خودش بپرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/news_hut/72831" target="_blank">📅 16:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72830">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=t0lhJ3DdJMv08yPBD8qNiDqxi_23Gze6IYq1lu7g4IqqM9nLNqfiQRMuGjY-kxL8bmE91TuuQeB021fucSBJzX-YXZGhnDaRWPROLQiKVwxX_affWE1bxv4OFjutVXTQS9hqei2kh5j-QhocaXLbER3xukyFAldeNcesKwwvW2MmHGSuN4PKKIldn-ez_kOv1-wABPqiyKgNTndY7aqJIPLly-oskxMVgDCkTMbsywW_OcqpsYEgwtFttzsLDfE6u5vHJW_zYqyDM8L97zCltL1sEaZdYMd2AuQ3hpOGVusp9iD4nX8MVp61xSAoIJX6SKJDW1B9e7cadzJQxs0gQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cac062b9b9.mp4?token=t0lhJ3DdJMv08yPBD8qNiDqxi_23Gze6IYq1lu7g4IqqM9nLNqfiQRMuGjY-kxL8bmE91TuuQeB021fucSBJzX-YXZGhnDaRWPROLQiKVwxX_affWE1bxv4OFjutVXTQS9hqei2kh5j-QhocaXLbER3xukyFAldeNcesKwwvW2MmHGSuN4PKKIldn-ez_kOv1-wABPqiyKgNTndY7aqJIPLly-oskxMVgDCkTMbsywW_OcqpsYEgwtFttzsLDfE6u5vHJW_zYqyDM8L97zCltL1sEaZdYMd2AuQ3hpOGVusp9iD4nX8MVp61xSAoIJX6SKJDW1B9e7cadzJQxs0gQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
اسرائیل توی ۱۴ ماه گذشته اسم ۱۴ تا خیابون و بزرگراه توی تهران رو عوض کرده! اونی که عملاً داره اسم خیابون‌های تهران رو تغییر می‌ده، اسرائیله؛ اسرائیل همین‌جوری مقام‌ها و فرمانده‌های سپاه رو می‌زنه، بعد شورای شهر میاد اسم همون‌ها رو می‌ذاره روی خیابون‌ها!
دفعه قبل هم بعد از جنگ ۱۲روزه، اسم چند تا خیابون و بزرگراه رو گذاشتن به اسم حاجی‌زاده، سلامی، باقری، رشید و شادمانی؛ یعنی اسرائیل اینا رو می‌کشه، شورای شهر هم جلسه می‌ذاره که خب حالا اسم کدوم خیابون رو بذاریم به اسمشون!
در واقع اونی که داره اسم خیابونای تهران رو عوض می‌کنه، نتانیاهو و موساد و نیروی هوایی اسرائیله؛ شورای شهر فقط می‌مونه و تابلو رو عوض می‌کنه!
با این حساب، اگه همین روند ادامه پیدا کنه، باید منتظر باشیم هر بار اسرائیل یه مقام دیگه رو هدف قرار می‌ده، تهران هم یه خیابون دیگه به اسمش دربیاره!
یعنی خلاصه تقسیم کار اینه: یکی می‌زنه، یکی تابلو می‌زنه:)
@News_Hut</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/news_hut/72830" target="_blank">📅 15:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72829">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KL393hn6QS1HbnfjKMUhA0G_VPaZe7nHSvBiJDhgbthiMTHyaAWmorqalJX6wqwBvjflRPcQdp5QENuOtGH7wOQucVq8W32Q7eIAcYQQqShgDlhDjyoBfUo_ou4T_Bnz7IZ9ahUognHuykYYLpnPTTBIzqnJRdmru2cDJlqtqJ1CCSAu-5WWU78mVMAxwDzNSSsFf4dic4AXehzbYQ1nRB7fevrn7gaIPUMqwF6aVM0ROX1TXfCAzbJ5ATrlkaU4fraTuJvljEBW7VI6Hhl41VhZHZ6wJsKoxSS4-hMFmUKUIKsOYqa8ysgPI5scDnGpX4MUrj3LacgNI5ccZm2aWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه از تاثیر سهمیه! توی کنکور امسال یه نفر رتبه‌اش ۸۱ هزار شده بوده،
که با سهمیه ۲۵ درصد، رتبه‌اش ۲۸۳ شده!
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/72829" target="_blank">📅 15:01 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72828">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=ekjSgKDrDLyn03Gr9ZQXefnP2BvAPRQCdDdREMUoHJPEhk4Erh89Eol3OMTAF3JzkuiHtue1glN-ztzMXJYRPh7vf23njDMdrjlmckCsdJYsjCfozETdcyjOQZdUjyDP2SeSN7WrHB0lg6nVQwEW4J8mhRdAjJzWCjWbzYigBFHiGiPuLstVCt2cfKrX7uYkRlOWsVQUZNmCdbNW2EovsQR0_he5OWk7zPO_p8itkz69EBJtzWSphRSFSkRzQYQ61O6qlPPk049QQwrFbA-POVbXTp85Gu5hWJcM-j1Q_fD5DPlVum0jMVBnrcxLK2B8c3HOalp9GQ3ku3iQ0fv0AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2512f994a.mp4?token=ekjSgKDrDLyn03Gr9ZQXefnP2BvAPRQCdDdREMUoHJPEhk4Erh89Eol3OMTAF3JzkuiHtue1glN-ztzMXJYRPh7vf23njDMdrjlmckCsdJYsjCfozETdcyjOQZdUjyDP2SeSN7WrHB0lg6nVQwEW4J8mhRdAjJzWCjWbzYigBFHiGiPuLstVCt2cfKrX7uYkRlOWsVQUZNmCdbNW2EovsQR0_he5OWk7zPO_p8itkz69EBJtzWSphRSFSkRzQYQ61O6qlPPk049QQwrFbA-POVbXTp85Gu5hWJcM-j1Q_fD5DPlVum0jMVBnrcxLK2B8c3HOalp9GQ3ku3iQ0fv0AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشور چین واقعا عجیبه، روی یه شهرک یه شهرک دیگه هم ساخته شده. شبیه فیلم inception شده.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/72828" target="_blank">📅 14:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72825">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pkx5WzJKSJz0vjYc-qarBhxdKLHhlyolOzYzO6z_3y2P2zT-VyUWRikOKRYkhulrvq_IBHALEjb_HVSbwis3IRYw1FX-imXkWJCT9f6-00E_Twa0Ye0vThszfFKYc9RPjIKqfvV9Eygm1DJpE6OpybQCeaCoUivDDdOXwYVX1CE3cTz6Bj8hnL-i5GNvv-Cmoc6Br8cgWzEtPmIPQJZVyiealJTREAKeJcZc60wTN9l8ktk2-MJ753-v8L2dlDdwW1x32irXyZtkTADbpTGwV0EryFTM2lhI8JfLpb_prPqc4QkLaQQtgZdNF7BySt-0TPWtPtlLOaW35oDvFcE6Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOAcZdAzUciwkpoe2N5YAjo7XQTZErn_5QS0WtvxXn0fTSrhkcjpSfQHrzYx6hgFEj5t-RPMu5rtuqoQIhmEG7dXttXjB5spQ0lviTK0SWB0oGoCpt1VaSKPbUS4H9qB4H28BXuDThSj8nsx-bW-WNDeqBLafQGLu5dmN0fd_7Sj5Ohpx_-Mlxv-f6wfiFrH4LVKDAh8sHU6gbsZvyt1CHzPP5pc8HJKoXZisuaRoSaQCODDm_Z1fgUfgxzc0GgGW-1xQFtfXbzIagimSSq1khGavrluKRTqy1d7qYFiSviFNsE8Zcuwb38pjsb8SSerzMC4exo2AtSkob3i3JjPOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=UPYhWaCzx5NZMUkUEpKcnPDbfxTHdU7nRvG_nzZ5pU7fQJlWwu29MpWjLDdHZjxhZFzJKyeNUj9S1Xllw7CyLljpB-2aFnLUqfigok_2m5xtXB6qlangWPTFbpEIGCJhnJrt17LlSNVWeTT-fYX-5_k-fRBtjZBg7hMZQkQyKJzJczo3IaRaJd7k4nJuPiOcMyutzUoXLGFC5eb1PVtYBdBtsMUwPGaa9V6qWVqBUlBiQRC4nXizrPuUfZeQp43_XXtWSDdnLcz7GfQrEBWxIbUCleyc9-p5KHP_Bj6t05VCZDhXpZZEbe4pNfQlZsaNxB-F8fYnyjCbt2JwrGj8wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e31c23155.mp4?token=UPYhWaCzx5NZMUkUEpKcnPDbfxTHdU7nRvG_nzZ5pU7fQJlWwu29MpWjLDdHZjxhZFzJKyeNUj9S1Xllw7CyLljpB-2aFnLUqfigok_2m5xtXB6qlangWPTFbpEIGCJhnJrt17LlSNVWeTT-fYX-5_k-fRBtjZBg7hMZQkQyKJzJczo3IaRaJd7k4nJuPiOcMyutzUoXLGFC5eb1PVtYBdBtsMUwPGaa9V6qWVqBUlBiQRC4nXizrPuUfZeQp43_XXtWSDdnLcz7GfQrEBWxIbUCleyc9-p5KHP_Bj6t05VCZDhXpZZEbe4pNfQlZsaNxB-F8fYnyjCbt2JwrGj8wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم یکی از همون ناوهای آمریکاییه(USS Delbert D. Black (DDG 119)) که سپاه تو بیانیه‌ها گفته بود موشک بالستیک خورده و «خسارت قابل‌توجهی» بهش وارد شده. ولی خب، به نظر من برای ناویی که موشک بالستیک خورده و خسارت قابل‌توجه دیده، زیادی سرحال و سالمه!
الانم برای استراحت چند روزه خدمه، وارد پوکت تایلند شده و بعد از تمیزکاری جلبک ها مثل روز اولش می‌شه!
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/72825" target="_blank">📅 13:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72824">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=OvAhr7R5Y8fIY9dVDOTyyQ5Eq54JaN3bKHC0Nnc-DgNQ5xh1D0mJNQvh7WFQ5DCdWk7riR8_BEb60uVwms40c_qmVnjkg8HfwVdbwqRCywEy7-bJcWjmCRd-CsdeVtD5mR11mHnDqJ6wZbiHW3Jb0iMoS87EK5p6m1l0MEuVzh2TBaoDyjC7EdYk9ndGgfABn72FRy5T3bbYebeOez1ZfQMqr22JlLixkG6k2-NONCEAxX2e4tLzEOjBIw_xT17wFdXLG4vMoMoRnSNMdTr4IO5f36M3drX6YqMifHDzl5sTGPLIjJQzF7uUE3FmbBqMPjrc5pdrUfRHnl8spCEhXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdf3b5b159.mp4?token=OvAhr7R5Y8fIY9dVDOTyyQ5Eq54JaN3bKHC0Nnc-DgNQ5xh1D0mJNQvh7WFQ5DCdWk7riR8_BEb60uVwms40c_qmVnjkg8HfwVdbwqRCywEy7-bJcWjmCRd-CsdeVtD5mR11mHnDqJ6wZbiHW3Jb0iMoS87EK5p6m1l0MEuVzh2TBaoDyjC7EdYk9ndGgfABn72FRy5T3bbYebeOez1ZfQMqr22JlLixkG6k2-NONCEAxX2e4tLzEOjBIw_xT17wFdXLG4vMoMoRnSNMdTr4IO5f36M3drX6YqMifHDzl5sTGPLIjJQzF7uUE3FmbBqMPjrc5pdrUfRHnl8spCEhXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه خانم طرفدار حکومت:به پسر نوجوانم گفتم اصلاً نگران نباش!
خواستی سیگار بکشی، بگو خودم برات می‌خرم؛
خواستی قلیون امتحان کنی، با بابات می‌بریمت سفره‌خونه؛
فیلم مثبت۱۸(پورن) هم خواستی ببینی، بیا با هم ببینیم! این‌طوری دیگه خیالم راحته که همه‌چی کاملاً تحت کنترله!»
@News_Hut
😐</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72824" target="_blank">📅 12:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72823">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=fc1ev3fgcI-e8CQwAF6XswIK9bD_UQ-Qz8timcjXDdkwPzD50Doiu8-dCeubxmWuvP301Lr2q2m2vPj9d8_pK6kY230m1RDvyQ8GsajvyyAW8QnhXxSWlK15UlF4tTEAQNNAsN-cKohjbDZhk7ipfi6x_Cu3LqF4BpyVIFRu1Df0vZBtM468CbN4mvtI3_154m72KghXCIuePEiLIDOgqEYtLAHCz83CfmAPrxzSyB7IUBaq7RKs1SeYd4rQBxINjOI4QKKp2-F8fXjAdyAz9wrbzg8KX80ZIR81B5F2AC1fL-no1Ogm_Rcp6CXw-y7DpDErqXY4s6lEHirj8S04QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e258d805f.mp4?token=fc1ev3fgcI-e8CQwAF6XswIK9bD_UQ-Qz8timcjXDdkwPzD50Doiu8-dCeubxmWuvP301Lr2q2m2vPj9d8_pK6kY230m1RDvyQ8GsajvyyAW8QnhXxSWlK15UlF4tTEAQNNAsN-cKohjbDZhk7ipfi6x_Cu3LqF4BpyVIFRu1Df0vZBtM468CbN4mvtI3_154m72KghXCIuePEiLIDOgqEYtLAHCz83CfmAPrxzSyB7IUBaq7RKs1SeYd4rQBxINjOI4QKKp2-F8fXjAdyAz9wrbzg8KX80ZIR81B5F2AC1fL-no1Ogm_Rcp6CXw-y7DpDErqXY4s6lEHirj8S04QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سال 2023 یه میم به نام Opium Bird خیلی وایرال شد که یه موجود بزرگ و پرنده‌مانند تو کوه‌های برفی رو نشون می‌داد و سازنده‌اش گفته بود که سال 2027 (۲ ماه و ۲۶ روز دیگه) می‌فهمید یعنی چی؛
حالا شباهت Opium Bird و طاعون
👺
و همچنین لوکیشن برفی اون میم و آب و هوای روسیه، دوباره همه رو داره به این فکر فرو می‌بره که نکنه داریم وارد یه سیزن جدید می‌شیم...
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72823" target="_blank">📅 11:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72822">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=CHJsJiGX8K4JHQP8V8HUg5yzBY1o0oiaDYNJJfm10OdjWyNRCu6eKLyD39IVdlCx7NP0IjMfm_1T1QN5tEH4Hhh5TSasAutlY7g_crL8f3klVarSJ1Z-7KNUEVVVaRUYYyPEFMm0A1nz8ZUN6GPMrF380UJpITG9sDNDoM-lTNgjGSRW18CLs3_A9dsrOQiZMxbemK7UTa4Z6JVH2khD9Vl1jsQKU7o2WjmySVxTKuZZEYxeM_qnJ9PCscOrZ914-fgE6aYNZp3-G4peekFbqgrbATdNQX2t9JdbfxJDxc4CiRE7ZdeTblDwlTbbCpvAiNO0rC3kzlBB2-099TuJPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dc05a4717.mp4?token=CHJsJiGX8K4JHQP8V8HUg5yzBY1o0oiaDYNJJfm10OdjWyNRCu6eKLyD39IVdlCx7NP0IjMfm_1T1QN5tEH4Hhh5TSasAutlY7g_crL8f3klVarSJ1Z-7KNUEVVVaRUYYyPEFMm0A1nz8ZUN6GPMrF380UJpITG9sDNDoM-lTNgjGSRW18CLs3_A9dsrOQiZMxbemK7UTa4Z6JVH2khD9Vl1jsQKU7o2WjmySVxTKuZZEYxeM_qnJ9PCscOrZ914-fgE6aYNZp3-G4peekFbqgrbATdNQX2t9JdbfxJDxc4CiRE7ZdeTblDwlTbbCpvAiNO0rC3kzlBB2-099TuJPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«همه دارن می‌گن من GOAT ـم، یعنی بهترینِ تاریخ.
من می‌گم: «پس واشنگتن و لینکلن چی؟» اونا هم می‌گن: «شما از اونا هم بهتری، آقا!»»
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/72822" target="_blank">📅 11:28 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72821">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=TKmGHGkpkd4jKyD612hPQwKYIRbtUKen3bFA2rHZlyv9HXk07DSQX0bRt-Xmv3vtDe7ZtDahU2F3dsOKGL6AwOBA2vkj0xzNy1biaweu9AHhHWNjlAWZ2acqFG6JVPezmHh9IPN206awj79DDWl6UaCR9wvP0dbY7ZwMcpHVha7E1PCwIohHCFn9DdBdHLOpy3iiJguL0vekXFUnK88TB47bHwvrjCtNBASBFTHIMvnKTHzDshB3AJvnVwKQJmGL_pshoNniU05Xza7EYuMSMWDhPmXeWVWXAtlmRn0lolOUrLkw6GQAczAlyQVt21YZcoinQh0RakNLtwvhRJxARQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/affe4d122e.mp4?token=TKmGHGkpkd4jKyD612hPQwKYIRbtUKen3bFA2rHZlyv9HXk07DSQX0bRt-Xmv3vtDe7ZtDahU2F3dsOKGL6AwOBA2vkj0xzNy1biaweu9AHhHWNjlAWZ2acqFG6JVPezmHh9IPN206awj79DDWl6UaCR9wvP0dbY7ZwMcpHVha7E1PCwIohHCFn9DdBdHLOpy3iiJguL0vekXFUnK88TB47bHwvrjCtNBASBFTHIMvnKTHzDshB3AJvnVwKQJmGL_pshoNniU05Xza7EYuMSMWDhPmXeWVWXAtlmRn0lolOUrLkw6GQAczAlyQVt21YZcoinQh0RakNLtwvhRJxARQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«این جنگ خیلی زود تموم می‌شه و قیمت‌ها هم قراره حسابی بیاد پایین. شاید حتی خودتون بگید: «خواهش می‌کنم آقا، این‌قدر سریع ارزون نشه!»
😂
خودتون ببینید تو یه مدت کوتاه قراره چه اتفاقی بیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72821" target="_blank">📅 11:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72820">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=ro-30RsLBNDOsoxnAfvwT1naYQV041Io4VQ3sBu3FgVGT0pvNUbXkbSNcaOEE9aWsY9oxGB8PIlRihru2KW7A0lN35nnKGFuyPBeC0b4XOBxK97NHhW7a9dliprW78x4YPWtHfYWLITHmHo1nrIk6t-lfsy7303aBwz5IUPxcU8zF9juX8GrCdgczDvV_3_kbNBXa2vW9pwV7FemvL1-_pLEBcFxXcXXPKOwMRTtWpEIlz-zfV87Om590x7gKgm4veEtJKNkEzHL0IhYKF9l7ncIS58xiDawTKcYAIu3Z8-W_VH9sEtborrZIjgr3YCqC73lDPEzWno2fVSRxcJvDqfjvHOGCIbEmlLSJqJ6FngC3umqej52RggCRBm1Mk87tbvE3__WfXu-2jYR7LAqQq7tWyL7ZOn2Q6Lw9RcYWP-VZDPJkmHyaQdKpcExBrRhuCfd4nNahYPyLvpml4CMEO50mCclhHazLZ2oJzWAAT2qJgwXn7ptRc9pcX2SIzOTdijNq6gWbTrHoQ3VuO45EpYXape3rbHVCT02J86mURBgbpC7cnPBXTumpgp2T-d1qc7qdEM4MP6D05VlUi-nAkzXuVQO0Na1MSHmZfcHGZAu4BrRmBdOJUjp8m5DQgOcRn3GyAiKZqxV1WO7PbFxhOn4tVicZa2PMqgAMRvC3j8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e9f8cbdc.mp4?token=ro-30RsLBNDOsoxnAfvwT1naYQV041Io4VQ3sBu3FgVGT0pvNUbXkbSNcaOEE9aWsY9oxGB8PIlRihru2KW7A0lN35nnKGFuyPBeC0b4XOBxK97NHhW7a9dliprW78x4YPWtHfYWLITHmHo1nrIk6t-lfsy7303aBwz5IUPxcU8zF9juX8GrCdgczDvV_3_kbNBXa2vW9pwV7FemvL1-_pLEBcFxXcXXPKOwMRTtWpEIlz-zfV87Om590x7gKgm4veEtJKNkEzHL0IhYKF9l7ncIS58xiDawTKcYAIu3Z8-W_VH9sEtborrZIjgr3YCqC73lDPEzWno2fVSRxcJvDqfjvHOGCIbEmlLSJqJ6FngC3umqej52RggCRBm1Mk87tbvE3__WfXu-2jYR7LAqQq7tWyL7ZOn2Q6Lw9RcYWP-VZDPJkmHyaQdKpcExBrRhuCfd4nNahYPyLvpml4CMEO50mCclhHazLZ2oJzWAAT2qJgwXn7ptRc9pcX2SIzOTdijNq6gWbTrHoQ3VuO45EpYXape3rbHVCT02J86mURBgbpC7cnPBXTumpgp2T-d1qc7qdEM4MP6D05VlUi-nAkzXuVQO0Na1MSHmZfcHGZAu4BrRmBdOJUjp8m5DQgOcRn3GyAiKZqxV1WO7PbFxhOn4tVicZa2PMqgAMRvC3j8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«یادتون باشه، این جنگ یه چیز مصنوعیه؛ یه مقدار هزینه‌ها بالا رفته، ولی خب برای اینکه دنیا امن بمونه، قیمت زیادی نیست.
اگه اونا بتونن یه شهر رو بزنن، بذار لس‌آنجلس یا سن‌دیگو رو بزنن؛ این در برابر حفظ امنیت دنیا، قیمت خیلی کوچیکیه.
در واقع، این ماجرا تقریباً دیگه تموم شده.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/72820" target="_blank">📅 11:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72819">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=S90urj0aa9LNeU3oU4ns0On_Nl3PgTyBUnqn8BkQ0tQy5s5CXNJC2fa3mhDNhyXZ54wtOd9WnQ-bIb36hdZNT8krqkpLkA96olvO_puw4Zq8v7XqS2hpQSAEXuIgj_07CPKEHxyplV4cWp5gt9XAhdPXK-An0iBDxDaiGaFdY7f2Q6Eu6jnGbpDmeObvI2p7E9vpnEHaQM8PQEYKpZqTB0uC6By0tlbulkQGNmid6Yy9IfImks-A7zBHNsaL2qI_IFL2E0cQyz3DMqPfQNhJSSdhDHi2MqgQEnoZzW6tHuJJ9ovL2RczO1GRKtTOosy9Dg2NmHheDaRt9LEsQkPWGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb2e238707.mp4?token=S90urj0aa9LNeU3oU4ns0On_Nl3PgTyBUnqn8BkQ0tQy5s5CXNJC2fa3mhDNhyXZ54wtOd9WnQ-bIb36hdZNT8krqkpLkA96olvO_puw4Zq8v7XqS2hpQSAEXuIgj_07CPKEHxyplV4cWp5gt9XAhdPXK-An0iBDxDaiGaFdY7f2Q6Eu6jnGbpDmeObvI2p7E9vpnEHaQM8PQEYKpZqTB0uC6By0tlbulkQGNmid6Yy9IfImks-A7zBHNsaL2qI_IFL2E0cQyz3DMqPfQNhJSSdhDHi2MqgQEnoZzW6tHuJJ9ovL2RczO1GRKtTOosy9Dg2NmHheDaRt9LEsQkPWGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: جنگی که علیه ایران راه انداختیم برای «
نجات دنیا
»ست!
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/72819" target="_blank">📅 11:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72818">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225b755540.mp4?token=J4x-jg742NJGGRivlBXaV9OApQZHEwiegOad7dSGqi9QlfmOXSbUk-0Zl0P1pcYzHgKflUaGovrQq1t6qmNnjKi_I1-7qzkzutyKBf_x9AP1HW--XtK-sj8mh0zWAN_VxmaOuKSd9eCu28JXh72hY2TKkF5uVc3dMxtuzxtgap5OmJ_XJUpaZHMtMyeivyhTimnkfHJGeA51wN_Rcv_hRpkjXg0qElJdamy2vJcWkRop7YLNJY9F-D7KQJ_Fr5G1ETaVs-KNPu0kKKrtTh3_lm-wgShvrQKts21HPGhWcos8fyL2CbXjmdeLpxGayWyG5Z0TTNOrWR0gDQa_V1iKcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225b755540.mp4?token=J4x-jg742NJGGRivlBXaV9OApQZHEwiegOad7dSGqi9QlfmOXSbUk-0Zl0P1pcYzHgKflUaGovrQq1t6qmNnjKi_I1-7qzkzutyKBf_x9AP1HW--XtK-sj8mh0zWAN_VxmaOuKSd9eCu28JXh72hY2TKkF5uVc3dMxtuzxtgap5OmJ_XJUpaZHMtMyeivyhTimnkfHJGeA51wN_Rcv_hRpkjXg0qElJdamy2vJcWkRop7YLNJY9F-D7KQJ_Fr5G1ETaVs-KNPu0kKKrtTh3_lm-wgShvrQKts21HPGhWcos8fyL2CbXjmdeLpxGayWyG5Z0TTNOrWR0gDQa_V1iKcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«راستی، داریم حسابی ایران رو می‌کوبیم، اینو که می‌دونید دیگه؟!
در هر صورت، این داستان خیلی زود جمع می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/72818" target="_blank">📅 11:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72817">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72817" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/72817" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72816">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgPQ9IAjBTfhVb8704ASmr49dOOjVjqvQB1eQucmeW5K5meKlh3rXjHrQiozj5q92bMMivBXXEagSbKyYyUfOsaKw0VjfRZB5TnGrFtTRzRQzZZ7K0P-BqvavGIcXFgPF-8XXHmxj6k8r9mtXmwksfh4rUmh2L05LT16U4qD1g0SJ4Hq_-px9MR1mD5MIzPwDjTbh6vt0CApt9k53Cmlq4y7HRayhjgHoGokuz9kWdkOtbU6jAWbdTnOVwMl_7X4SQg_6LpK1LnlJQXZMbGlw1K7ojkhlfBCpXlGGEzvEioYkM5jQrq-HTKxeRHrRinL6LmeG9frB4OP7-1EGnhs_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
اسپانیا
🆚
کرواسی
چک
🆚
انگلیس
اسلوونی
🆚
اسکاتلند
مقدونیه شمالی
🆚
سوئیس
ازبکستان
🆚
کره‌ جنوبی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72816" target="_blank">📅 11:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72815">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=LxUrr2pxBBO1au_JVnjAs3wjSFsOJShefFyeAlCDpXfXfX0pI63K2oh648NA84f0OjLnzeZGHYZzHP1uvl9LLNnhfmMy1NPbHfHHOrCPN3gA0Sp3XxAcC7oeOkkA6PYeEsxOikGIbGQl7K-a6L4CqESpMSIH6z5iCKBu-JKMmRm-9pmr5r41uSwrrumAX7eDqm6yA7xlSrlEFVCMJm6eNmldXmCu1TgwRXVQC_VDxXKVPjEISlPqA7KiNLIhNt4ugrlxeAvKJm1A8PVIZjSL8uZ0JKHXfxJPK1kdvvGOy0jQizsowp2uikZ7b-jfc48u017hlDyVcM6Kv9xKVmYQ_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c201257b1.mp4?token=LxUrr2pxBBO1au_JVnjAs3wjSFsOJShefFyeAlCDpXfXfX0pI63K2oh648NA84f0OjLnzeZGHYZzHP1uvl9LLNnhfmMy1NPbHfHHOrCPN3gA0Sp3XxAcC7oeOkkA6PYeEsxOikGIbGQl7K-a6L4CqESpMSIH6z5iCKBu-JKMmRm-9pmr5r41uSwrrumAX7eDqm6yA7xlSrlEFVCMJm6eNmldXmCu1TgwRXVQC_VDxXKVPjEISlPqA7KiNLIhNt4ugrlxeAvKJm1A8PVIZjSL8uZ0JKHXfxJPK1kdvvGOy0jQizsowp2uikZ7b-jfc48u017hlDyVcM6Kv9xKVmYQ_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش چشم: اگر آمریکا بمب اتم بزند، ما هم پدر بمب‌ها را به آمریکا می‌زنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/72815" target="_blank">📅 11:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72814">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=DlADapmechRVj9qVZrTEdIzFkGKV-pvi5bVumlZut2Kbcq5zHTDAf5ENOMX-19SgVYbyccEbMICDFh7FxwLIOtbpU4Nndda9M4PAHOPEhUGsTKQ_KmPHPA3yucnYyWLpU77_YkiskfVfu5xJe2Q27ZUVJzEMlRQxaBns47LgD64K1CnD4WBygD-9NmpDUANFd8Bvz_rgwuGMrDhd-jvR4SLp6jU3n4Ymm1QsV5HIf0CIOcusCgKEDG74NdzVVll3ueZdABsrvfUGbOlM_kY7-F6aI901hyMjUVuZ3tBaJcAKJbxRe5hmtZ1ornybt0W2J8_0Z2plGKLdQJbJd8EsZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/796b47b54e.mp4?token=DlADapmechRVj9qVZrTEdIzFkGKV-pvi5bVumlZut2Kbcq5zHTDAf5ENOMX-19SgVYbyccEbMICDFh7FxwLIOtbpU4Nndda9M4PAHOPEhUGsTKQ_KmPHPA3yucnYyWLpU77_YkiskfVfu5xJe2Q27ZUVJzEMlRQxaBns47LgD64K1CnD4WBygD-9NmpDUANFd8Bvz_rgwuGMrDhd-jvR4SLp6jU3n4Ymm1QsV5HIf0CIOcusCgKEDG74NdzVVll3ueZdABsrvfUGbOlM_kY7-F6aI901hyMjUVuZ3tBaJcAKJbxRe5hmtZ1ornybt0W2J8_0Z2plGKLdQJbJd8EsZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران هر روز ترسناک‌تر میشه، یه پدر برای اینکه پسر 3 ساله‌اش رو تنبیه کنه، یه بسته مداد رنگی 24 تایی رو فرو کرده توی باسنش!
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72814" target="_blank">📅 10:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72813">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=v88VspXX6Ex4T7pfG8po8Q1lMF-SM0OifVy31keKc8ppEKLbmBjTAgoII945sqrDDMnRCrVR-LcFx5_ChRUUZ52LDQlsrO4iTENfsCXmvE0khfD2u-rJSHoXv0PL1HOcFw0RrDd74ZvzhXx22wOfBLxdE5oPAwt6OvuyhVYzt57fBXEf4NW1qHFVN91uZsLIXXdRBoInlKPFYZEtsyAWtPrLFASceZPeTYd5zUwGoDsliOFh8b_L0PDtGY5wGlf2VP_duHNzB1jeBPPKxSMVQIb925VCCxySBVf9UDmzHbjpiqWuTuYeAcL9_Y8XbUU1G0k6GlBqP-U6-0Sh4PoLxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0246c863e9.mp4?token=v88VspXX6Ex4T7pfG8po8Q1lMF-SM0OifVy31keKc8ppEKLbmBjTAgoII945sqrDDMnRCrVR-LcFx5_ChRUUZ52LDQlsrO4iTENfsCXmvE0khfD2u-rJSHoXv0PL1HOcFw0RrDd74ZvzhXx22wOfBLxdE5oPAwt6OvuyhVYzt57fBXEf4NW1qHFVN91uZsLIXXdRBoInlKPFYZEtsyAWtPrLFASceZPeTYd5zUwGoDsliOFh8b_L0PDtGY5wGlf2VP_duHNzB1jeBPPKxSMVQIb925VCCxySBVf9UDmzHbjpiqWuTuYeAcL9_Y8XbUU1G0k6GlBqP-U6-0Sh4PoLxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو تا از لوکس ترین مدارس بالا شهر تهران که شهریه شون یک میلیارد تومنه!
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/72813" target="_blank">📅 10:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72812">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOBFr751XTFzVfQtraUnjd3ALowmMz_qsHHW9QhgCvZ0EaZMHe_N8z3SAnrvvvUj8pGeytuEMJR6X5DO8Wawj7PHRDkYs1coCX0v7JPgXXjdewZtWWxZnPXLz3sj7q2mwqdOL_5R-c_ipNEWdTudqBSdQaelCTZ7Lf0Y3sDOOD_YgoKKid2pB3v4qssHLHIVOcgusxclrKp5gFWFtsqF2Ep1Aue9yOOoWV5BTfxM3KPyFnFGpiJElicz8IBTcXC3GtXhyioXfp_9u1fnLZ_iXAv0ey7WDT1_BDAN_wOy4lXkiPEyu20sFXXXMU2fGaiyfVGQN9aZAWzON7iozC7yVYCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c2a17b7a.mp4?token=chbMkY507FWQsZUGCorupsIfv8KYDQusyQxPdsP57XtBHp2i7u4nKmkg9ldyhWyV3UN1uLZuOBAbJZfcoXAF0mnG2fcw4LzTbAeeQD9WUIGLq2kRfXeqfOWcfYA7Wpz3Z0x-6YrHXQ4UgDGU7ptwrZNGhnxtTEwlffOjQZboM-oqblRIBYi0paPJYqZhGPEQVMrJyuV2rqZsnwU72y3MutzwwuAh1qwY1jJSJ2yiL-zZwXfMjCYWfqgO1etuH5PrThb9fN1sbHsaBiTs5e0qirfBAOrDvg0j9egEUkxXUvZtFCv0GXoW1pWQkcuX5aHzTzRx7c37B9ODbIsqZzXJOBFr751XTFzVfQtraUnjd3ALowmMz_qsHHW9QhgCvZ0EaZMHe_N8z3SAnrvvvUj8pGeytuEMJR6X5DO8Wawj7PHRDkYs1coCX0v7JPgXXjdewZtWWxZnPXLz3sj7q2mwqdOL_5R-c_ipNEWdTudqBSdQaelCTZ7Lf0Y3sDOOD_YgoKKid2pB3v4qssHLHIVOcgusxclrKp5gFWFtsqF2Ep1Aue9yOOoWV5BTfxM3KPyFnFGpiJElicz8IBTcXC3GtXhyioXfp_9u1fnLZ_iXAv0ey7WDT1_BDAN_wOy4lXkiPEyu20sFXXXMU2fGaiyfVGQN9aZAWzON7iozC7yVYCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: خبر داری دلار شده ۲۷٠ تومن؟
یه خانم تو تجمعات: اره ولی ما بخاطر وطنمون اومدیم، اگه ما نبودیم دلار حتی گرون ترم میشد
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72812" target="_blank">📅 09:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72811">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=qelGHxQo3PPa7r9jAvgoUl_SL-01MLTPkdc5yaootmFoqjf2nsTVHnxPqV1c0axghpCs8Az5EqbrwrPjS2_NR2D74NKyihVUUWsFqZ6wUzj0f9qDBJ9bmvGd37eXZRK690Yj4CNGAOX1kp6uGb8waMXSUXHp5lBbOf6M6vr_Gi8kQGp4-nHIE1ih0k7YSueMi8Kxn4uKSBewLPVsUJbPTjDOPaAczTGKDU_gLB2RBhs5r0YsY2DX6IPOTNtouIlV-t1wrJBYEqVLZoZOFBVVMd0HfPkMkNbJnnh8L59Hlx5HIdCXM0sExwueKAdKU_PrCs-o5qfzA0EIe7bNbrvwpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4d885120.mp4?token=qelGHxQo3PPa7r9jAvgoUl_SL-01MLTPkdc5yaootmFoqjf2nsTVHnxPqV1c0axghpCs8Az5EqbrwrPjS2_NR2D74NKyihVUUWsFqZ6wUzj0f9qDBJ9bmvGd37eXZRK690Yj4CNGAOX1kp6uGb8waMXSUXHp5lBbOf6M6vr_Gi8kQGp4-nHIE1ih0k7YSueMi8Kxn4uKSBewLPVsUJbPTjDOPaAczTGKDU_gLB2RBhs5r0YsY2DX6IPOTNtouIlV-t1wrJBYEqVLZoZOFBVVMd0HfPkMkNbJnnh8L59Hlx5HIdCXM0sExwueKAdKU_PrCs-o5qfzA0EIe7bNbrvwpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آجرلو عضو تیم مذاکره‌کننده:
بابا بالاخره یه جایی باید قبول کنیم یه‌سری از این تحلیل‌ها اشتباه از آب دراومده!
هرکی نظر متفاوتی داشت رو «خائن» و «وا داده» خطاب نکنید؛ وقتی می‌گفتید ادامه جنگ این‌طور میشه، اسنپ‌بک هیچ اثر اقتصادی نداره، نفت میره روی ۱۵۰ دلار یا با شکست ترامپ در انتخابات کنگره همه‌چیز تغییر می‌کنه، باید امروز جواب همون تحلیل‌ها رو بدید.
اینکه بگیم «ترامپ انتخابات کنگره رو ببازه، دموکرات‌ها جلوشو می‌گیرن» هم خیلی ساده‌انگارانه‌ست.
بین انتخابات تا شروع کنگره جدید چند ماه فاصله هست و رئیس‌جمهور آمریکا هم قدرت زیادی داره و می‌تونه سیاست‌هاشو دنبال کنه.
خلاصه اینکه تحلیل غلط، تحلیل غلطه؛ فرقی هم نمی‌کنه از طرف چه کسی گفته شده باشه. به‌جای توجیه و فحش دادن به بقیه، بهتره بعضی‌ها یک‌بار هم بابت پیش‌بینی‌های اشتباهشون پاسخگو باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72811" target="_blank">📅 09:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72810">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72810" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72810" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72809">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRFjE7Jl_QS6PCs-weqTPhgP1wzeA-DoLeOfv25e3k-fMyUpHUowOxnadgfk95OFHs2ygzAQk5RDyEHuXF7Esgmbgf4wOoKXkfva30ARzgDW6JEL_fCGu0YOUPynYiYLLjut3Yrcd54w8fRQKTShBkMsog75BFgxTjy7RanTuvk6drcr4EuPQDMA09RqoLFKDgPICApghBnxqcJV8N1kF9P7te8zxifxmtU1VyCWM910mGRsUYEpDx8eEyPYNoNQqnhatJkQqETJwYi0nlKIpOcbUM0ZGBrhtFTN-FPSGLGNjweQ4Mz1CAobpy6s0h1urMEkjdkCesf_y-nzZTK5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72809" target="_blank">📅 01:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72808">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=K9JL8MNgjqE9keW0mqrmaYk2RuVw5UXm_5Svv2hzBGrRnhRgyQZVl3D7SdmHObftIWKOF6ERt9E4gsw9pakG5lc8cfLXo5lkCw-SaHHZjv21NgECtiG7HXgUBURuZP3aUv6GoOg1XXvOk7TWSkfF0txbK0Lr0UdY5MYbUlSPWCYtP5hfFz3M53wF1-Iq_Q0OiQGM4-RvgIDJvHNglwe48m-D0aOtp9JIMyXtTUeb2beV-yQ7jxvclE_Rwu75Hujvg4sgKMhXhI4wcRFBDDZ7V-o3-ZmL-ep71IOlkFb5B4kCoRjashWXPRYmmJwDSois06dXx6jwAcZblmlh5GoKpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d28d251d.mp4?token=K9JL8MNgjqE9keW0mqrmaYk2RuVw5UXm_5Svv2hzBGrRnhRgyQZVl3D7SdmHObftIWKOF6ERt9E4gsw9pakG5lc8cfLXo5lkCw-SaHHZjv21NgECtiG7HXgUBURuZP3aUv6GoOg1XXvOk7TWSkfF0txbK0Lr0UdY5MYbUlSPWCYtP5hfFz3M53wF1-Iq_Q0OiQGM4-RvgIDJvHNglwe48m-D0aOtp9JIMyXtTUeb2beV-yQ7jxvclE_Rwu75Hujvg4sgKMhXhI4wcRFBDDZ7V-o3-ZmL-ep71IOlkFb5B4kCoRjashWXPRYmmJwDSois06dXx6jwAcZblmlh5GoKpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین ویدئوها از شهر طاعون زده شلخوف در روسیه:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72808" target="_blank">📅 01:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72807">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=A3sgIoAOXSzSVSvOeha2pZncrZ-O5Z7G9mVAoaJgxg2BqgCxRoWhSdEbyaji-0_TqslxZqwESqrPVu7YuGv0Vj5dGKYfQfsj8vJPvgfc1JOIab8aXbBHlvb5pXIRdviBTgNtugWyX_Vi5xik-iKMJIcIGWYgDYGSb9Y-wfmgY1hD1dCRcfERnGaniMD4Qy_mEm6iP8OZc9I1yuTpduBPt35k0jrD1rwzhbnDxhirQ9Tv7913WjY1jpXdNLW2l--KdWF43trP6sIbDio3WHZSgoVa_r80EBpPb4PJ0ckNkpI8FLF8-msjpWc9sPA8Ar6RdwUSzCoZKoFOxMNQzyhGUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a90e5ff82.mp4?token=A3sgIoAOXSzSVSvOeha2pZncrZ-O5Z7G9mVAoaJgxg2BqgCxRoWhSdEbyaji-0_TqslxZqwESqrPVu7YuGv0Vj5dGKYfQfsj8vJPvgfc1JOIab8aXbBHlvb5pXIRdviBTgNtugWyX_Vi5xik-iKMJIcIGWYgDYGSb9Y-wfmgY1hD1dCRcfERnGaniMD4Qy_mEm6iP8OZc9I1yuTpduBPt35k0jrD1rwzhbnDxhirQ9Tv7913WjY1jpXdNLW2l--KdWF43trP6sIbDio3WHZSgoVa_r80EBpPb4PJ0ckNkpI8FLF8-msjpWc9sPA8Ar6RdwUSzCoZKoFOxMNQzyhGUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو پشم ریزونی که ارتش یمن منتشر کرده که دارن با ماشین، حوثی‌هایی رو که در کنار ساحل گرفتار شدن و در حال مقاومتن رو زیر میگیرن و له میکنن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72807" target="_blank">📅 01:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72806">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46e493def7.mp4?token=Lvv5GF_vGh5ktvTfZbq0Fx_0da_DWqytASs77a8VcjxWDB99xEtpu7Ul2buuxiaMi6ivAIJanz_J_k07Bu47Kg1Ym8512_AGD7T0TDrpcSWHWLujf2fjNQnVS0y5tVGa0QKMMYAIT2gSLAaBlQQS8vzNdpyO7UD4HkinVBzxfi5MJ6FpzG3JD4H4pDogz3q8bkp557E0PqW0daMhQ9NPhCKQlqd2t6wf9cx-KCdHdJPIqJwrfdTKeXNFkSmN_8iVDhGGpq9_Guujtvpi_ZqodC7qtRC5tQ7BAdHaqfJ401jasfp_ekEvre8J-E0W5ltTrGMRrsXbRAjTkTI8MfQRIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46e493def7.mp4?token=Lvv5GF_vGh5ktvTfZbq0Fx_0da_DWqytASs77a8VcjxWDB99xEtpu7Ul2buuxiaMi6ivAIJanz_J_k07Bu47Kg1Ym8512_AGD7T0TDrpcSWHWLujf2fjNQnVS0y5tVGa0QKMMYAIT2gSLAaBlQQS8vzNdpyO7UD4HkinVBzxfi5MJ6FpzG3JD4H4pDogz3q8bkp557E0PqW0daMhQ9NPhCKQlqd2t6wf9cx-KCdHdJPIqJwrfdTKeXNFkSmN_8iVDhGGpq9_Guujtvpi_ZqodC7qtRC5tQ7BAdHaqfJ401jasfp_ekEvre8J-E0W5ltTrGMRrsXbRAjTkTI8MfQRIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان سخنرانی حسین رحیمی، رییس پلیس امنیت اقتصادی، درباره افزایش قیمت دلار، برق محل برگزاری سخنرانی قطع شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72806" target="_blank">📅 01:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72805">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSrF00TadBAYI23d7Mp_YDl7QldTIqbiTbsXh2uZbhBWDCvXdiHzBosbwFGMRsG_stTzY6773lCLEUc9SZFfQKyRZGrDC298Mk-I270PYuX9x9_2VqNS6JermsnJqMbuj33hfXimkApgsMLgLUhDYTVPgV_adfW-xL1JvCFyd9D48T5lotomXPreM_wA-o2tdaef3XWwAfwUliwMpUnqm3m7fHCP76uqYpKtR64i7MEg8wI8JfUnUSIuaPayPUUjydrgzJVwWy8rZ4nHFZVrY5joqRp8TLtp8xWKlW2CSYlWzwxjT6cqJ0WqoZXW7y2Mjak9CAHveGH_dEU7YiM76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکات بسنت درباره ایران:
«عملیات طرد اقتصادی» نتیجه داده؛ ارزش ریال به پایین‌ترین سطح تاریخی رسیده، ایران ماه گذشته هیچ نفت خامی برای بارگیری روی نفتکش‌ها نداشته و حتی یکی از مقام‌های ارشد امنیتی ایران هم گفته کشور در یکی از سخت‌ترین دوره‌های تاریخش قرار گرفته.
حکومت ایران در حالی مردم خودش را تحت فشار و رنج قرار می‌دهد که منابعش را صرف حمایت از تروریسم می‌کند و عملیات طرد اقتصادی تا زمانی که جمهوری اسلامی از تأمین مالی تروریسم و ساخت سلاح هسته‌ای دست نکشد، متوقف نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72805" target="_blank">📅 00:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72804">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=KoWvoIEm3wTyxStgxkEBS1J21Yw7JrLgBZIxa9D_Ue1nM_9cA1iid5SKaGxfbyvItxZQbh2zck-6LGCDZfGK6mOieiaJASpqD0nFgqiPCsitJPBDgmTQX0FgO0L4BRjHtaD2-crMHAoqANOmhRCXuCIaro-PLE0BM_LaPYbPv66jVUYt7K5mUm3qapp9yUP_AcQpNZms9UiBYvd8WwlYIOigAIHgh4MfbsyPHAE7WxzszOLAEyRAdTM5sPs7OdCelCRfkvaUq_yYC0-jzreLp7xRTS3O0aqNDWRQ4ctVFc7IbC_XVTNzIPzoUYVqUlfh_L_jFvOSwa-v419lheIJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b15ea218.mp4?token=KoWvoIEm3wTyxStgxkEBS1J21Yw7JrLgBZIxa9D_Ue1nM_9cA1iid5SKaGxfbyvItxZQbh2zck-6LGCDZfGK6mOieiaJASpqD0nFgqiPCsitJPBDgmTQX0FgO0L4BRjHtaD2-crMHAoqANOmhRCXuCIaro-PLE0BM_LaPYbPv66jVUYt7K5mUm3qapp9yUP_AcQpNZms9UiBYvd8WwlYIOigAIHgh4MfbsyPHAE7WxzszOLAEyRAdTM5sPs7OdCelCRfkvaUq_yYC0-jzreLp7xRTS3O0aqNDWRQ4ctVFc7IbC_XVTNzIPzoUYVqUlfh_L_jFvOSwa-v419lheIJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ:من فکر میکنم ایران مسئول حمله به هواپیمای «فلای دبی»است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72804" target="_blank">📅 23:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72803">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ:
ما مقادیر بی‌سابقه‌ای نفت از تنگه هرمز خارج می‌کنیم. یکی از مشکلاتی که داریم این است که پالایشگاه‌های روسیه به‌شدت هدف حمله قرار می‌گیرند.
این یک مشکل است، اما اوضاع به‌خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72803" target="_blank">📅 23:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72802">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سؤال: آیا نگران شیوع طاعون در روسیه هستید؟
ترامپ: این بیماری‌ای است که قبلاً قادر به مهار آن بودیم؛ اما به نحوی، آن میکروب‌ها قوی‌تر و هوشمندتر شده‌اند. آن‌ها مثل یک ارتش هستند. ما به روسیه کمک خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72802" target="_blank">📅 23:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72801">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=HfhJWEkVc66VoCp9lRUBkGOdhwx3LXCZMG3kYf50XiPMhe9xtKVsQQ3INgcFYy8h2AFQyz5GGWdZuezPD3ghcr5qSLuTXrZQIx80LCnWgCyeVOwfrIRKd86wTBQgszBzunYChSFIcBr96qbnq1GmFk6_kpH8g6-bIVL1A6HPfu_1DuezjlDzRX3ON2C-026fmlqDq4oynWK7k190yVXjJBMGstA5c66pnr3QP-ORtxzp2mt-FOl1alklyt5IwGjYpyZ2g0syqLSdC3DdWwgsUFZTXH3I5AafD3vlf1k6YMeA5BWsFK8ELR37sGLWF9sGKnFvZ9Bzw8C8m-rq5T40kGuITsYJJUjWu-r7BHLwfQhYeBSy4GtiIfp3lAs0zBBw79EkA5Qc0gBIj5KnohyAXLZIlCcli_UeA0msXoXoDTexTruGQpoJIMbHpOW6bRg0TbpU_EhhI78zrFdOhvtis-TGXEvkaG4Y0vnSkVswyOfCRm5QZbXILumh2lucNP8tR7ArPSnyXMHvCpVkWllmEpfG9IRO82Uzf7f5buV2wU9-IVNAi4D8E-4Ifv9_BxGT8isdJlK_xr3sSmiy-IuVLHrDDNiS6WWBzTJL0obfpJJJE66sn2yQjzDOvYhmIGOqlVGNVM4P84AwCL1wrYXlsK93FWBe86-NXVjwlYDM8oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c9bba814.mp4?token=HfhJWEkVc66VoCp9lRUBkGOdhwx3LXCZMG3kYf50XiPMhe9xtKVsQQ3INgcFYy8h2AFQyz5GGWdZuezPD3ghcr5qSLuTXrZQIx80LCnWgCyeVOwfrIRKd86wTBQgszBzunYChSFIcBr96qbnq1GmFk6_kpH8g6-bIVL1A6HPfu_1DuezjlDzRX3ON2C-026fmlqDq4oynWK7k190yVXjJBMGstA5c66pnr3QP-ORtxzp2mt-FOl1alklyt5IwGjYpyZ2g0syqLSdC3DdWwgsUFZTXH3I5AafD3vlf1k6YMeA5BWsFK8ELR37sGLWF9sGKnFvZ9Bzw8C8m-rq5T40kGuITsYJJUjWu-r7BHLwfQhYeBSy4GtiIfp3lAs0zBBw79EkA5Qc0gBIj5KnohyAXLZIlCcli_UeA0msXoXoDTexTruGQpoJIMbHpOW6bRg0TbpU_EhhI78zrFdOhvtis-TGXEvkaG4Y0vnSkVswyOfCRm5QZbXILumh2lucNP8tR7ArPSnyXMHvCpVkWllmEpfG9IRO82Uzf7f5buV2wU9-IVNAi4D8E-4Ifv9_BxGT8isdJlK_xr3sSmiy-IuVLHrDDNiS6WWBzTJL0obfpJJJE66sn2yQjzDOvYhmIGOqlVGNVM4P84AwCL1wrYXlsK93FWBe86-NXVjwlYDM8oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آن چه تهدیدی بود که باعث شد آن هواپیماها را از بریتانیا خارج کنید؟
ترامپ: احتمال وجود تهدیدی را می‌دادیم؛ خب چرا باید آن‌ها را آنجا نگه می‌داشتم؟ با تهدیدی مواجه بودیم. ما کسانی را که آن تهدید را مطرح کردند، می‌شناسیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72801" target="_blank">📅 23:36 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72800">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=Da3P48FtVI3R-F05OA2gm4QL2_x83HBDlx8_Dlg1Gx5jWajiHgl-ETmP7Tgzq1kZkwK0xFpG4-YSyn4-bG5cz_ggGhoowZEnV3GRAtjbalVp9x6E60qo_aD6MuiSfqiuj8RzOmIxYe3cjFNYOWAkEiSqLr12vgeT01X2SU7LKDMoEgOCIxqjgxDhwdXlqRQMLK0MP0-EONi4egX-7TM8u2gVlsD0AGA5oufnl4jH7Rw3ahnvJqyO7UIMNH6sgAIIDLmUQaHzd_dsi4hlmp85vzqvs7tin4j5cmo07gKSVUP2TrOBND4mWL6PTEme04xOAtHplywaTJwbu5vXFZERow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8f6705b0f.mp4?token=Da3P48FtVI3R-F05OA2gm4QL2_x83HBDlx8_Dlg1Gx5jWajiHgl-ETmP7Tgzq1kZkwK0xFpG4-YSyn4-bG5cz_ggGhoowZEnV3GRAtjbalVp9x6E60qo_aD6MuiSfqiuj8RzOmIxYe3cjFNYOWAkEiSqLr12vgeT01X2SU7LKDMoEgOCIxqjgxDhwdXlqRQMLK0MP0-EONi4egX-7TM8u2gVlsD0AGA5oufnl4jH7Rw3ahnvJqyO7UIMNH6sgAIIDLmUQaHzd_dsi4hlmp85vzqvs7tin4j5cmo07gKSVUP2TrOBND4mWL6PTEme04xOAtHplywaTJwbu5vXFZERow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا فکر می‌کنید این خطر وجود دارد که ایران پهپادهای رزمی وارد بریتانیا کرده باشد؟
ترامپ: نمی‌توانم چنین چیزی به شما بگویم. اگر دست به چنین کاری زده باشند، بهای سنگینی خواهند پرداخت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72800" target="_blank">📅 23:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72799">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=tsfGZsyTJtdc2dDdliv-hjMr_o1CJfZQRPEoriYfZz8_-2tfTEBvwvkxUYVWPM7cR1zAq2nZJfwjyTSW_bpfDzxIGhXFC3tbJ1mlep8XTnZpuCS_LerQD8gODubC38-ICkHZ7fKfUFvPFh0tI3jz_P1GYhvEttUlmkkvqxMA45Fgh2lADGdXL0MG4RXM87FhhkPP8xtUwugvHm_cVnX-X7JqWFVtwAD9_vulegxLvaWhSutLlnQfRl_1L3S5huMPsIgdVTrOqJMTONF5unzXAxPKQgOz_8nLJIFgbJCrWzqYGLV2Xkh0knZKpo41yjlfZ89SMjl05FrwgH8J0pJFNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a5b0254b5.mp4?token=tsfGZsyTJtdc2dDdliv-hjMr_o1CJfZQRPEoriYfZz8_-2tfTEBvwvkxUYVWPM7cR1zAq2nZJfwjyTSW_bpfDzxIGhXFC3tbJ1mlep8XTnZpuCS_LerQD8gODubC38-ICkHZ7fKfUFvPFh0tI3jz_P1GYhvEttUlmkkvqxMA45Fgh2lADGdXL0MG4RXM87FhhkPP8xtUwugvHm_cVnX-X7JqWFVtwAD9_vulegxLvaWhSutLlnQfRl_1L3S5huMPsIgdVTrOqJMTONF5unzXAxPKQgOz_8nLJIFgbJCrWzqYGLV2Xkh0knZKpo41yjlfZ89SMjl05FrwgH8J0pJFNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:نظر شما درباره ضدحمله عربستان و یمن علیه حوثی‌ها چیست؟
ترامپ: همه چیز به خوبی پیش خواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72799" target="_blank">📅 23:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72798">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=WUJBZLS1qki8jkOCs5hBLflFeEIJipz0fx5AQJL7NqFyBdEoFpBok5ffi6iuWlrcRwpU1SL8v_orqF1jcU6m755S6pxok6kMAXR8ezud7noRilSP-81mLzYYfzvzKORkL4FRZm20BgFQHyJYeqCPEacQVLlF2vKarlTNgKk3zQlAOF85Xk81Z6p9BDppHxyYIO4kvc4GAGLbskKXB-bwlH3vCxolI1Hf0oiy43-t5aHPagbd2oBeceeYFCW-NZoAu_4d99fQl-Uh-HpMO2XC-5ti2d8H6PhHxb6O8ENaCRlVSlur7U94aGkdj_VyT386txj9SE45-xGnzLPry8xka1x-H-f0R-KqRWsoxkzDdd_UVyi3_LKW7nRKkF0cFCW7BlcrVH4kptd-srOUgzxkgm3L-YeHl2bGED1f9NJ9vrxe1_TI4vo9jscPXXJdwG1X2ekR3KHpvrfkBnjwLJGHyBT-FncoeXSHOc5ro5knZDy4-WROUeyhhqrU8-7x-HldfxJ02Gn6p2EMOKXbBqJghiGQu-ellEKQ12ECbDTXiMpH-R1Neqx1BTkDbbAlxgz5iSuDPBL2uI6pM1UZCqZ-vuJKtl-RfiW-wc1rqWj4XLe99IfYCeyT9VYdoKdBGJ0cSsohDT1sKQGoMbQuMBSr0aUoWD0Jh4Au1sM8YVCpFjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8db85c22.mp4?token=WUJBZLS1qki8jkOCs5hBLflFeEIJipz0fx5AQJL7NqFyBdEoFpBok5ffi6iuWlrcRwpU1SL8v_orqF1jcU6m755S6pxok6kMAXR8ezud7noRilSP-81mLzYYfzvzKORkL4FRZm20BgFQHyJYeqCPEacQVLlF2vKarlTNgKk3zQlAOF85Xk81Z6p9BDppHxyYIO4kvc4GAGLbskKXB-bwlH3vCxolI1Hf0oiy43-t5aHPagbd2oBeceeYFCW-NZoAu_4d99fQl-Uh-HpMO2XC-5ti2d8H6PhHxb6O8ENaCRlVSlur7U94aGkdj_VyT386txj9SE45-xGnzLPry8xka1x-H-f0R-KqRWsoxkzDdd_UVyi3_LKW7nRKkF0cFCW7BlcrVH4kptd-srOUgzxkgm3L-YeHl2bGED1f9NJ9vrxe1_TI4vo9jscPXXJdwG1X2ekR3KHpvrfkBnjwLJGHyBT-FncoeXSHOc5ro5knZDy4-WROUeyhhqrU8-7x-HldfxJ02Gn6p2EMOKXbBqJghiGQu-ellEKQ12ECbDTXiMpH-R1Neqx1BTkDbbAlxgz5iSuDPBL2uI6pM1UZCqZ-vuJKtl-RfiW-wc1rqWj4XLe99IfYCeyT9VYdoKdBGJ0cSsohDT1sKQGoMbQuMBSr0aUoWD0Jh4Au1sM8YVCpFjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال: آیا تهدید خاصی وجود داشت که باعث شد آن بمب‌افکن‌ها را از بریتانیا فراخوانید؟
ترامپ: بله، فکر می‌کنم بتوان چنین گفت. پرواز آن‌ها تصادفی نبود؛ تهدیدهایی در کار بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72798" target="_blank">📅 23:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72797">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449cc78904.mp4?token=ZdJZMlt-JijejDO7NkvGd_TxMfcB4zIUDvXY-M_tb3eyAlydoN8bVtPGvtPKqZpHPqFuK_bA3-kreh8-nkd4eV7F8ugqTWhWRPXCeo6SP9KXthE8tlyedSbh2iLCs1g79Rt4GIbSO3vCZP4hV0DTKuFgLZbe_5xC7uecy_1-qJdICt2GuHnFneITAn2sVScn8Rh7UFGifQ6gPpskG2b-MGW58V-s6QMpJC0u4oim_kMnf7WuXj_oeH3Rb7GyrFaHqwKdJ9ari471O0aR8cyzL3qY3Ie7dnKcfPMTOZdb49gAX4D66S0l-zE2YXAEq5dkNZkG50RAQDyAeQB9otvPHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449cc78904.mp4?token=ZdJZMlt-JijejDO7NkvGd_TxMfcB4zIUDvXY-M_tb3eyAlydoN8bVtPGvtPKqZpHPqFuK_bA3-kreh8-nkd4eV7F8ugqTWhWRPXCeo6SP9KXthE8tlyedSbh2iLCs1g79Rt4GIbSO3vCZP4hV0DTKuFgLZbe_5xC7uecy_1-qJdICt2GuHnFneITAn2sVScn8Rh7UFGifQ6gPpskG2b-MGW58V-s6QMpJC0u4oim_kMnf7WuXj_oeH3Rb7GyrFaHqwKdJ9ari471O0aR8cyzL3qY3Ie7dnKcfPMTOZdb49gAX4D66S0l-zE2YXAEq5dkNZkG50RAQDyAeQB9otvPHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در میدان آزادی (میان اقبال) سنندج از این کوماندو‌ها رونمایی کردن برای مردم! امیدوارم این فیلم رو هیچ وقت ترامپ نبینه چون بعدش قراره دیگه شبا آرامش نداشته باشه
😂
یه ساختمون چند طبقه رو ۱ دقیقه طول کشید تا برسن پایینش! از پله‌ها میومدن زودتر می‌رسیدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72797" target="_blank">📅 23:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72796">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=mJIwXrEYD3-0sVQpRYGKjar0TCQJYlyvjrHPX780SNp4HPmkzJBG5hynZUVZEc51ULFKN-O9oD87afKOnYMh6SO-39bK2OgE_3Y32OuLEWDZPeEhrSI5U-2TSgNbMuxShNG9dnk-EltM1e2mKUdfgB1og-UeBYwSU0dtriwqGphfLGT2PjDZSo1tPUwV9ibEXq3pSIaydAl9dRIXDnis5MyM60odsxiBVYxQdVtufIZ1TSWmx0GMdMJRm33qwSzjbANYQjDKnLjWjKU3KLofIZgTI8bSChtYTu39X81foFONyIHIhB6CXfqNdk2hKLJAeAQL1DioPtLl9P5vwioAbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1edaa900.mp4?token=mJIwXrEYD3-0sVQpRYGKjar0TCQJYlyvjrHPX780SNp4HPmkzJBG5hynZUVZEc51ULFKN-O9oD87afKOnYMh6SO-39bK2OgE_3Y32OuLEWDZPeEhrSI5U-2TSgNbMuxShNG9dnk-EltM1e2mKUdfgB1og-UeBYwSU0dtriwqGphfLGT2PjDZSo1tPUwV9ibEXq3pSIaydAl9dRIXDnis5MyM60odsxiBVYxQdVtufIZ1TSWmx0GMdMJRm33qwSzjbANYQjDKnLjWjKU3KLofIZgTI8bSChtYTu39X81foFONyIHIhB6CXfqNdk2hKLJAeAQL1DioPtLl9P5vwioAbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شامگاه شنبه ۱۱مهر۱۴۰۵؛لحظه برخورد صاعقه با برج میلاد:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72796" target="_blank">📅 22:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72795">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=OawNHaA_nl7LNWXI6Kg-VjTLH-D3jPEd4YfM03WWD4iAeGVHx6Arck7onCb-GH3k_d-GT4hMEnpC1Bgjn8elg5RJhsMMylZkLuYBZdUBis9RVJiDg5a13rIAxfDqr8zRC3_KvdeKdnfx_6A9MmqT527Kmf8P9uaUwu1xi0cphWkH-_zuPaeGt1KbozPYaMfFxAT2x65am1INQDT6lDjfP-Yodyh8f8Qy4U0gFS-o9tfcKnmaH1w0_UBFvzYZyjedAyHQ_OWFeteOhVKZv8w7zedNPl65bMiSVnO6F2a0CQDzyYMe0gr7qFBnH7T42Tk_YQ8znnSJwNRweJWv1Iq3ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d10955ac.mp4?token=OawNHaA_nl7LNWXI6Kg-VjTLH-D3jPEd4YfM03WWD4iAeGVHx6Arck7onCb-GH3k_d-GT4hMEnpC1Bgjn8elg5RJhsMMylZkLuYBZdUBis9RVJiDg5a13rIAxfDqr8zRC3_KvdeKdnfx_6A9MmqT527Kmf8P9uaUwu1xi0cphWkH-_zuPaeGt1KbozPYaMfFxAT2x65am1INQDT6lDjfP-Yodyh8f8Qy4U0gFS-o9tfcKnmaH1w0_UBFvzYZyjedAyHQ_OWFeteOhVKZv8w7zedNPl65bMiSVnO6F2a0CQDzyYMe0gr7qFBnH7T42Tk_YQ8znnSJwNRweJWv1Iq3ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: اخراج ما از آمریکا مثل اخراج تیم برنده از المپیکه!
پس خبر درست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72795" target="_blank">📅 21:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72794">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=ea1EXzfjD2BBCAqUAwE8QlwYxIDj56Ak7rJEVEJFuE34qd99C_ATztoSz_B77CmY7EVy2DNb7dFV8yetSAlqTDz2YrP-NLD95PFhrFr84z7-2TI-B88Lxdl9hM59MT7On8cz-7cUk-mswpE2teZhvA07VwWMq_S5bep5XIFQVPdFbzAR77bpzOCL20dCmPlQe6p8dalquRcyerJ6RVsZp034031AV5_Gjx0HUhePyMhBFwUBDc4sOSO3ug7L-z9Y47M19w4NBgc5NI8iFcGik-ZGG81oInc2Yabi7IFyfeBVnmD-g72DliIJcBJ3yZYRcHEdevUzXG4OwffSrISa7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d035f07a6e.mp4?token=ea1EXzfjD2BBCAqUAwE8QlwYxIDj56Ak7rJEVEJFuE34qd99C_ATztoSz_B77CmY7EVy2DNb7dFV8yetSAlqTDz2YrP-NLD95PFhrFr84z7-2TI-B88Lxdl9hM59MT7On8cz-7cUk-mswpE2teZhvA07VwWMq_S5bep5XIFQVPdFbzAR77bpzOCL20dCmPlQe6p8dalquRcyerJ6RVsZp034031AV5_Gjx0HUhePyMhBFwUBDc4sOSO3ug7L-z9Y47M19w4NBgc5NI8iFcGik-ZGG81oInc2Yabi7IFyfeBVnmD-g72DliIJcBJ3yZYRcHEdevUzXG4OwffSrISa7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آقای آتش‌نشان در مورد ساخت پلاک مشخصات برای دانش آموزان:
امروز رفتم یه دبیرستان دخترانه برای کنترل مسائل امنیتی بین حرفامون با مسئولین مدرسه متوجه شدم که دارن برای دانش آموزان پلاک مشخصات فردی درست میکنن مثل همونایی که زمان جنگ استفاده میشد؛
از این پلاک‌ها که زمان جنگ سربازها مینداختن دور گردنشون که اگه بر اثر بمب و موشک چهره‌شون دیگه قابل شناسایی نبود، از رو پلاک شخص رو تشخیص بدن..
وقتی پرسیدم برای چیه؟ گفتن نمیدونیم فقط از بالا دستور گرفتیم و مشخصات فردی دانش آموز رو دادیم تا براشون درست کنن!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72794" target="_blank">📅 20:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72793">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unmr_ge4zKI1yBvHZlfOGpJZGMVjsqke3FFqv_9uJZ8aUiI5SoxjexZzFO1uVset4HeLCIPp6Ybw6CI8zRKJ5sNuf8vSxBWwwAFzylxWxFu56skFqp4behyjaAJoV-Vi3K5q-ZC80vPI-y1HgQls0Ruj-7hJIKYf5rcGYIf5Uirp26JKoDWmkDqpEirIyM2iUmbjKEqV26Rwoq2_JCAmN6Xq74n7pgjDe6cJ3a_IIsi3BiZTkwSG7aRXTRgaw-qPQDVk3WBzdtlzizgV13qGgROrygo-BIRfONQsZwBFefhLR8toE4QXNxJd6_bAkgERkoMehwh_TJl4vKtf62ZDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
آنچه باعث افزایش قیمت بنزین می‌شود دیگر تنگه هرمز نیست — چرا که اکنون حجم بی‌سابقه‌ای از نفت (بشکه) تقریباً به‌صورت روزانه(از تنگه هرمز)عرضه می‌شود
.
بلکه مسئله «پالایشگاه‌ها»ست؛ جایی که پالایشگاه‌های روسیه توسط اوکراین منفجر می‌شوند و پالایشگاه‌های ما در ایالت‌های آبی (دموکرات‌نشین) مانند کالیفرنیا، توسط «دموکرات‌های احمق» تعطیل می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72793" target="_blank">📅 20:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72792">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902f67b684.mp4?token=IY-gzoeNoPTnCkyZ5Yh_dnSPCRFHbjhBEmTx8MoXpPDM5dAFL369C-_XLzNe64U0Egos2JmmxZlAIBSsB15wN7rdKYPPb8i1qt84tRbUk9S5dS5nRA0JPrFyVcm6RGHbEI1lll6Z2f2L2V6EuSf1hRJfqD-bzYxjzxYDYVOLvfNJ4cvcgnbA10XGrnXW47G1WSTguRpa4OibS0Ps6x3Eza0MpxqMS7NxQDjTtLmT9dyNaoGooPYqEwE_vKUAgTh5b5aKbUtD8lY_GQ8KzVB7Mtv2Yrl8yK5kdPfAmn1qEu9zAjX4kTq2WP01bXZUlU2U09gxeqrOJdqmSAD7lU9tng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902f67b684.mp4?token=IY-gzoeNoPTnCkyZ5Yh_dnSPCRFHbjhBEmTx8MoXpPDM5dAFL369C-_XLzNe64U0Egos2JmmxZlAIBSsB15wN7rdKYPPb8i1qt84tRbUk9S5dS5nRA0JPrFyVcm6RGHbEI1lll6Z2f2L2V6EuSf1hRJfqD-bzYxjzxYDYVOLvfNJ4cvcgnbA10XGrnXW47G1WSTguRpa4OibS0Ps6x3Eza0MpxqMS7NxQDjTtLmT9dyNaoGooPYqEwE_vKUAgTh5b5aKbUtD8lY_GQ8KzVB7Mtv2Yrl8yK5kdPfAmn1qEu9zAjX4kTq2WP01bXZUlU2U09gxeqrOJdqmSAD7lU9tng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا توانایی خودشو توی بسکتبال هم نشون داد و تقریبا همه توپاشو سه امتیازی وارد سبد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72792" target="_blank">📅 20:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72791">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=oTvz4yU5uncrhz-KCNuK9yULPTCjBdp7tOmcSvM78QQBgeOQcasr_q4_cUQSiHasKXVz1Ayq3BFg5dKDwdgYeQKgtbyMNGdP1awUHEI3uG4NMwsnDV7j5wqHsn1dLjPumThb-6_R4Wh6_VicHUQfY4T7nUyW7zAEPclrJM9-vSwYErCA3Dd6JBQj8rpz0pcEkFqUscGKUTyGlp0xG98T3LNCPgmYX2Q-xGUF0VPaHOEmN_Gk1vd19S_Ecg8ZERIKQ2NvVTGq19d4XXWkQGWGSJLDXONtCUcaxR84UmOXqChP5Scfp9lGcUhU9v3kIJtIeXfM_Y1zxL-uhagNN9GO7ax7Rt8ro0nJnf1ANv7xmKtoUdJePV77O4wJz72cDu-H9d7JAHRR3nnx1YAD5mi64kPXkoZfiH_a8xw68rsQmuMYbxDK3U-e07RWbn3TKer2rpHMMLkMQLQWrbSxeZPrEz6zhZCGwwanHHxNhHSqESG5HnLMSwVCysRa02xOj1I1uP2tQrllHab5rvG2sRntrZrACc1Y9sjJgHqGDY2IHd8eNdG5RzDj0UGs_03yrZTsGduvYYjMEPnWdQeaEgxzsLyCxn7GcvfUZ_eQsmBP9mqTZpHKnqXP_D_MVGPvgZ1gLICEnOuMIof_7NdFRInZN6U1sWjiid1SHmCp7iTWnYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0b5a00bb1.mp4?token=oTvz4yU5uncrhz-KCNuK9yULPTCjBdp7tOmcSvM78QQBgeOQcasr_q4_cUQSiHasKXVz1Ayq3BFg5dKDwdgYeQKgtbyMNGdP1awUHEI3uG4NMwsnDV7j5wqHsn1dLjPumThb-6_R4Wh6_VicHUQfY4T7nUyW7zAEPclrJM9-vSwYErCA3Dd6JBQj8rpz0pcEkFqUscGKUTyGlp0xG98T3LNCPgmYX2Q-xGUF0VPaHOEmN_Gk1vd19S_Ecg8ZERIKQ2NvVTGq19d4XXWkQGWGSJLDXONtCUcaxR84UmOXqChP5Scfp9lGcUhU9v3kIJtIeXfM_Y1zxL-uhagNN9GO7ax7Rt8ro0nJnf1ANv7xmKtoUdJePV77O4wJz72cDu-H9d7JAHRR3nnx1YAD5mi64kPXkoZfiH_a8xw68rsQmuMYbxDK3U-e07RWbn3TKer2rpHMMLkMQLQWrbSxeZPrEz6zhZCGwwanHHxNhHSqESG5HnLMSwVCysRa02xOj1I1uP2tQrllHab5rvG2sRntrZrACc1Y9sjJgHqGDY2IHd8eNdG5RzDj0UGs_03yrZTsGduvYYjMEPnWdQeaEgxzsLyCxn7GcvfUZ_eQsmBP9mqTZpHKnqXP_D_MVGPvgZ1gLICEnOuMIof_7NdFRInZN6U1sWjiid1SHmCp7iTWnYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس، معاون رئیس‌جمهور، درباره خروج هر ۱۲ فروند بمب‌افکن «بی-۱» (B-1) از پایگاه نیروی هوایی سلطنتی «فیرفورد» (RAF Fairford):
آنچه در آنجا شاهد بودید، اقدام وزیر دفاع برای محافظت از نیروهای ما بر مبنای احتیاطی مضاعف بود.
ما با اطمینان نسبی معتقدیم که ایرانی‌ها در پی انجام همان کاری هستند که حکومت ایران طی ۴۹ سال گذشته انجام داده است؛ یعنی ارتکاب اقدامات تروریستی علیه ایالات متحده و همچنین علیه بسیاری از افراد دیگر.
ما نهایت احتیاط را به خرج می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72791" target="_blank">📅 19:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72790">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp2uhAptJMu1SO1UaLd08SaRKrhsHuKVop4Bb9fzOtBP9a9rZVGig5BYIfooFUImGuu9rdF4b12-meNY2notDBirzFVWTZ_kZQ4ClI39hJUP-JbgZx1wLQHC4cNIx-FIcxsF77XkDeU7d-uzIrKNuw3G_u7bHQ3IvJoPe1tWfe6ZxjIaGrKAWmAwOdXyoV_E6WW7lKJm6cpiUoYvDSBqUG1lrNH3qQuV9bputthUh6If5mNDU3zTIoPdKPsk-CcznAqaeHWC4Lv72_FsNTSoVw88624uMNIPbWaOUFXfTyqfJ82bHmovW1oIcAcPqU9Cg-zhUd2sCXNRs8LKAYLTCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
ناو هواپیمابر آمریکایی «جورج اچ. دابلیو. بوش» به همراه حدود ۴۸۰۰ نفر از کارکنان خود، پس از شش ماه پشتیبانی از عملیات‌های ایالات متحده در خاورمیانه، برای یک دوره استراحت وارد پوکتِ تایلند شد.
پوکت نخستین بندری است که این ناو از زمان ترک ایالات متحده در ماه مارس در آن پهلو می‌گیرد؛ قرار است کارکنان آن از ۴ تا ۹ اکتبر برای گشت‌وگذار، فعالیت‌های فرهنگی و برگزاری یک مسابقه فوتبال میان آمریکا و تایلند، در خشکی حضور یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72790" target="_blank">📅 19:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72789">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=c_5ip3zfXfj_x9HQEL4PeKcBlKMRWeVoRwwwJUrp_n71_8zB65cFvDStdQkGb9VS6UFs5noy3yIXrQj6Aws2Sr-8KfKuwyK5twEmXSF0KF3doHyypimDCYK9M42D9J7nQKE6WPXbh_lELZ155IR9yD9c7aGZ7JTJ3-ifqARwhuAdeD4JoVts0RY_IXxKVo5DsFo2ES17haCNR8nakCSlkUz7WocJ-8Er0vedbc5wr4JO4OvAqfIbKVGbhedI4Nq9b3Swv4hflJ9uSXZ5A74Gzo59vaQauDfZhTQi05k2zzqyBaWpNiDt9bbk9oAmOsWP-ZxPUQ_ZF5xCmJn8FTct5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3aadbf79.mp4?token=c_5ip3zfXfj_x9HQEL4PeKcBlKMRWeVoRwwwJUrp_n71_8zB65cFvDStdQkGb9VS6UFs5noy3yIXrQj6Aws2Sr-8KfKuwyK5twEmXSF0KF3doHyypimDCYK9M42D9J7nQKE6WPXbh_lELZ155IR9yD9c7aGZ7JTJ3-ifqARwhuAdeD4JoVts0RY_IXxKVo5DsFo2ES17haCNR8nakCSlkUz7WocJ-8Er0vedbc5wr4JO4OvAqfIbKVGbhedI4Nq9b3Swv4hflJ9uSXZ5A74Gzo59vaQauDfZhTQi05k2zzqyBaWpNiDt9bbk9oAmOsWP-ZxPUQ_ZF5xCmJn8FTct5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)  تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72789" target="_blank">📅 18:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72788">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حوثی‌ها به معنای واقعی کلمه به سعودیا دارن تجاوز می‌کنند، یعنی شما کاکولدزاده تر از ترکیه‌ای‌ها، پاکستانی‌ها و عربا نمی‌بینید، بعد حالا فکر کنید این سه تا پیمان دفاعی هم دارن =)
تازه از خواب بیدار شدن گفتن عه بهمون حمله کردن بزار یه گوهی بخوریم وگرنه شرفمون از دست می‌ره (کنترل شهر مهم تعز همچنان به دست حوثی‌هاست)
#hjAly‌</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72788" target="_blank">📅 18:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72787">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حوثی ها دو موشک را به سمت منطقه ای که تحت کنترل نیروهای دولتی یمن بود شلیک کردند.
در همین حال خبرنگار شبکه العربیه در حال آماده‌سازی برای پخش زنده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72787" target="_blank">📅 18:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72786">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2wojpeKa6V_Sd9VsEz5io7m1-6EtNxq_tTcOo2gLiS9E79XDNqQxZ0jvWwhoHrAye6eJSBAIzy6IiiW0SDXvA24RuVEOotBXZp92wvOCUwCIoefbkUpqju8jlLGUZg1A-2CjP_9ekWjsbcwQV_3qp9A-hrdIo_J_jMiuu4WM9Fy9yevibUFy1HNLc5vH54QaGEadRWpHYSztxCBK2AgClTU-8sCymMvj8AEvq7qPazUP7e7cXfF9oT0iPFGaSaRj4baHCtJcB_x9pqyLlhOSNFE5RcTeuDMoftDJPQWW_7AeMh04sO9d8c5MyPJ4KLUrDwrHFo9zTQYb0UWzP4dfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛
مشاوران ارشد امنیت ملی ترامپ نشستی محرمانه و چندساعته را در «کمپ دیوید» برگزار کردند تا درباره احتمال جنگ با ایران و درگیری میان عربستان سعودی و حوثی‌ها در یمن گفتگو کنند.
ریاست این نشست بر عهده معاون رئیس‌جمهور، ونس، بود و مارکو روبیو، پیت هگسث، استیو ویتکاف، جان رتکلیف (رئیس سیا)، ژنرال دن کین و اسکات بسنت (وزیر خزانه‌داری) نیز در آن حضور داشتند.
یک مقام آمریکایی اظهار داشت که در این جلسه درباره مسائل عمده خاورمیانه «تصمیم‌گیری شد یا دست‌کم بحث‌های عمیقی صورت گرفت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72786" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72785">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72785" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72785" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72784">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgMQEx7G3ZB4t1HbfnXcG-ypL2diCGWOV-it8Mr2FfN7W625oAY5d0XSq6J1dCswBSrezf8huAEC7JB2OHIjo3-4OAICtFcWsaq-Q8TDldgEBXFLFm7yLDvJ5hg2QvGY-yvZSMqEubGGXu1OyK3V7fkZNF4fRefBJnYdG0Ylahyn_rLmrFNApk59Nu35lvvUvdXnOdPp_0dinPBxwnC5nNitm0tbn2OXxiwCi6ylE3NXhz0ZD9BC9VJ-hBQ3zuUBxjISZnKr6x-5kG0mfw55jR3nn9F8kITPQ28iy4nWKzxeUZSOgd00SBWBN3Hb5c5cP74sHuqPG5wqLhbtsEjdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز بلژیک
🆚
فرانسه را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بلژیک: ۳ برد، ۲ شکست و ۱۰ گل زده
فرانسه: ۲ برد، ۱ تساوی، ۲ شکست و ۷ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72784" target="_blank">📅 18:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72782">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=SxW_HuvtRPxREfgwNDzbNwfCr87SpKVno8AwBC7L5lLAqqC3kPTDgAg5FkXTJaGuG-IkWtqVVhaqJ0uDhVFJzGi-3Jm-4RO4atZzeogu-oU32Szr2E1fa1geC3iW9GHZstOu1l3p6oDqEn513CFAsBg5c890FSoe_kmYmsrlXYky0F-InsqlW58yOxFj_M0wo5q6PWJXBFFlitUGlQrHlDSIcT65k5XKx2Nes71_WUp4LbHZlL3odaxJbNaJWbig2cf1SK3bc5PO0cmXd8P2BBhBrwojbXQSmR0d2xFdb6Zde43FU7BMMYQAmEb3tqlVFVL1Wt9EqdyHKA-cwjepzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e7b8e8d5c.mp4?token=SxW_HuvtRPxREfgwNDzbNwfCr87SpKVno8AwBC7L5lLAqqC3kPTDgAg5FkXTJaGuG-IkWtqVVhaqJ0uDhVFJzGi-3Jm-4RO4atZzeogu-oU32Szr2E1fa1geC3iW9GHZstOu1l3p6oDqEn513CFAsBg5c890FSoe_kmYmsrlXYky0F-InsqlW58yOxFj_M0wo5q6PWJXBFFlitUGlQrHlDSIcT65k5XKx2Nes71_WUp4LbHZlL3odaxJbNaJWbig2cf1SK3bc5PO0cmXd8P2BBhBrwojbXQSmR0d2xFdb6Zde43FU7BMMYQAmEb3tqlVFVL1Wt9EqdyHKA-cwjepzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های جنجالی کوچک‌زاده مجلس :
کدام کارمند و مردم عادی پول دارد ۲/۵ میلیارد تومان بدهد ده هزار دلار بخرد، این پول زیر متکای امثال همتی و دزد‌ها و اطرافیانش میرود.
آقای قالیباف، چرا مملکت اینطوری شده که راننده رفسنجانی هر کاری می‌خواهد در این کشور می‌کند؟
طرح جدید بانک مرکزی؛
هر ایرانیِ بالای 18 سال می‌تونه تا 10 هزاردلار (۲ میلیارد و ۷۰۰ میلیون تومن) از بانک بخره!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72782" target="_blank">📅 17:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72781">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=VL_WkK8jjAGqWinQml6_1lvZC9mpug9YCH0-2Sm349Zj-6HZTHLroFTg3wrguGMzKL9cd_QZ5ubpKttOJDQiyB0-EP4UNerjcSaIOWKeFNxib1yK_oDjNoPayIvLP85V5wKw6uaxv7BkvsGSzW_OZMOMhnkQHLGbI4yB54KUcUpMh6SO9eD92Ig3bpXLdKWPoqEvwm-1dS8BKOFsFemEMx-X4jX3x6RZWz3z6JUIjNEm9wI5r29w3_5m3qEw2ZxG460WTLDm5b58Eay-a16ATyizeyRgnVbc74fSIO0Oe2v8ju3_6rddLuktWhl5kkM9WJt9f2fX9bTwZfAYu0iX1wgo5sw96gRIqy8niDQuI_DW21Yum947bWIlZRsgkUXAX194gOI8dt8wHi_1K-AoLmjBjE8JVaWzWbrJOY0f2BzApm5tSLDJbQRAMl0gvti3S1N_7diONMeHUWYM3OHwHGujySYlV9DWoRvkQzwj0X9J7upHXioCeip4GmdCYvX3AZHiKo-TRQ_kNNsDCkT9n5bwY6K0AJ2kkrcRyS1sc7Nupn1gsLAhVPhTBHg8qow8BxR86McldPXxe3OcKEQd5DknaAenn-LZW5vNlkMvCfFj2QOVE9AfM0BQ3nJS_H_kajv0AdrTuYj6SZPGKHIUVzaSRJkjnvnqnyFZX83gLi8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f1c650a97.mp4?token=VL_WkK8jjAGqWinQml6_1lvZC9mpug9YCH0-2Sm349Zj-6HZTHLroFTg3wrguGMzKL9cd_QZ5ubpKttOJDQiyB0-EP4UNerjcSaIOWKeFNxib1yK_oDjNoPayIvLP85V5wKw6uaxv7BkvsGSzW_OZMOMhnkQHLGbI4yB54KUcUpMh6SO9eD92Ig3bpXLdKWPoqEvwm-1dS8BKOFsFemEMx-X4jX3x6RZWz3z6JUIjNEm9wI5r29w3_5m3qEw2ZxG460WTLDm5b58Eay-a16ATyizeyRgnVbc74fSIO0Oe2v8ju3_6rddLuktWhl5kkM9WJt9f2fX9bTwZfAYu0iX1wgo5sw96gRIqy8niDQuI_DW21Yum947bWIlZRsgkUXAX194gOI8dt8wHi_1K-AoLmjBjE8JVaWzWbrJOY0f2BzApm5tSLDJbQRAMl0gvti3S1N_7diONMeHUWYM3OHwHGujySYlV9DWoRvkQzwj0X9J7upHXioCeip4GmdCYvX3AZHiKo-TRQ_kNNsDCkT9n5bwY6K0AJ2kkrcRyS1sc7Nupn1gsLAhVPhTBHg8qow8BxR86McldPXxe3OcKEQd5DknaAenn-LZW5vNlkMvCfFj2QOVE9AfM0BQ3nJS_H_kajv0AdrTuYj6SZPGKHIUVzaSRJkjnvnqnyFZX83gLi8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: چرا بمب‌افکن‌های آمریکایی پایگاه «آر.ای.اف. فیرفورد» (RAF Fairford) را ترک کردند؟
روبیو:
مشاهده چرخش نیروها و جابه‌جایی تجهیزات، امر غیرمعمولی نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72781" target="_blank">📅 17:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72780">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=T8-oWSUnORaUzxdU96x_pwm5e-QIZ89VJ49hrk-tRbQFmF-kCWzBW7BNKXh2E2imz_SsHgYhf69iZfRc_TVO2XqtifACtIszthVCO76wUITCiPWqRcvaPIiMTOSmu720zBuYUHq2fhgK8dMtTwtHWdc4ZT8evGnXUXrjNqU_rLuEZI8ygEiEgckVHlMtHCj_BOnVBs3W4d8p9BCIGrSbxiKS4ZSzLXi-4XT6KZOINT2cOKyp8KzOSj24hGsFMUTyNmxk4UdTOXMfMzk8WqTjrDNBstLY2HPTXeFg5ZBXh6GLP71ETrgi-slvL4ZTO-48jVLt-Zoj8tEhVucv1oK_xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cde1d0199.mp4?token=T8-oWSUnORaUzxdU96x_pwm5e-QIZ89VJ49hrk-tRbQFmF-kCWzBW7BNKXh2E2imz_SsHgYhf69iZfRc_TVO2XqtifACtIszthVCO76wUITCiPWqRcvaPIiMTOSmu720zBuYUHq2fhgK8dMtTwtHWdc4ZT8evGnXUXrjNqU_rLuEZI8ygEiEgckVHlMtHCj_BOnVBs3W4d8p9BCIGrSbxiKS4ZSzLXi-4XT6KZOINT2cOKyp8KzOSj24hGsFMUTyNmxk4UdTOXMfMzk8WqTjrDNBstLY2HPTXeFg5ZBXh6GLP71ETrgi-slvL4ZTO-48jVLt-Zoj8tEhVucv1oK_xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آترینا فرحمند رتبه یک کنکور تجربی ۴۰۴، پارسال همین موقع:
دخترا خیلی خفن‌تر از پسران، من مطمئنم رتبه یک کنکور تجربی سال بعدم دختره.
نتیجه:
توی کنکور تجربی امسال از ۱۰ نفر برتر، ۹ تاشون پسرن و رتبه یک هم پسر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72780" target="_blank">📅 17:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72779">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=GCkOAPTYdd6_irFfyAWuT8aM183kFgBfDkrr25pm51dQEo-0yHMS2HlW2L10YQzaMgWiOdtH5MLXkq1rmIfxVFov4TLxQHn6o3l696wszoIE7bFzSww0oTS_fnUiJiKOmvQi_kDvHRVs7jSuBKrWdOeOv_bm7snmSHSweleNZHZ_NXkyI6eyfcUeizEa4xhc1FiocHhwgBsCncd9ZeOSYQ_Quc6nLuNQLAFGDIhR690qbLOqmJyfOpy3s1ZO0NCMPkhByp0wK5bfgRfNdFBtfFVUucfvXmLUTYeDLNKFFf9phDQfVXja-JkidmecWKwW3K_f1YhmBcE9Tn8xs4lPibtHckN_206rrfUHFwaaL6s0mk27LKeEIz6Q7fDCNSICZ6609yuV9GoxuookTGzt8uOHYFBDcpjDPh0Cx58_GWUUVo1geDuYhil04i3lm-cPfT6xmqp2UyDd2ccx3kSiOsSk663gnSWroySkNnYbWZj7nrdD7G8bQ0yqe1p9DvL14JXNolkBT1-YB0v4GuX5cI07_rh-zpUSQp6py1FpspEIRf0o0-NXrrRW2abrW7aCTXZLlUJVMBz6r6GXZcTOuvsh6BZqYUD9wq4qoK0F9a9k06Jz5wVgKsT-RbVcGqiayHAjHGVQ3dc6OCtm37NfyIiGWWGqyHitm7S8Y9Wsfr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a05bc751.mp4?token=GCkOAPTYdd6_irFfyAWuT8aM183kFgBfDkrr25pm51dQEo-0yHMS2HlW2L10YQzaMgWiOdtH5MLXkq1rmIfxVFov4TLxQHn6o3l696wszoIE7bFzSww0oTS_fnUiJiKOmvQi_kDvHRVs7jSuBKrWdOeOv_bm7snmSHSweleNZHZ_NXkyI6eyfcUeizEa4xhc1FiocHhwgBsCncd9ZeOSYQ_Quc6nLuNQLAFGDIhR690qbLOqmJyfOpy3s1ZO0NCMPkhByp0wK5bfgRfNdFBtfFVUucfvXmLUTYeDLNKFFf9phDQfVXja-JkidmecWKwW3K_f1YhmBcE9Tn8xs4lPibtHckN_206rrfUHFwaaL6s0mk27LKeEIz6Q7fDCNSICZ6609yuV9GoxuookTGzt8uOHYFBDcpjDPh0Cx58_GWUUVo1geDuYhil04i3lm-cPfT6xmqp2UyDd2ccx3kSiOsSk663gnSWroySkNnYbWZj7nrdD7G8bQ0yqe1p9DvL14JXNolkBT1-YB0v4GuX5cI07_rh-zpUSQp6py1FpspEIRf0o0-NXrrRW2abrW7aCTXZLlUJVMBz6r6GXZcTOuvsh6BZqYUD9wq4qoK0F9a9k06Jz5wVgKsT-RbVcGqiayHAjHGVQ3dc6OCtm37NfyIiGWWGqyHitm7S8Y9Wsfr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا می‌توانید آخرین وضعیت مورد مشکوک به طاعون در روسیه را به ما بگویید؟
مارکو روبیو: ما به‌دقت وضعیت را زیر نظر داریم. فکر نمی‌کنم این مسئله جای نگرانی داشته باشد، اما نیازمند توجه و تمرکز است و ما نیز همین کار را انجام می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72779" target="_blank">📅 16:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72778">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a15378585.mp4?token=ai7YXEMlXCbUY0NT4xI6LK0snIm_FgOJdEZ8qmTL_eVpTbsXOH0NgZ9G6xSTcbIgDTz7YyKAtAd30GF5QhCjyj8gxjkukddOrns2npm8tZlDkQATDZFdCsHMOf2wWIt9Ovj55GCE7XpfHBckIEgQJgZDDDT5OjUw51p5tZWC8Kz51npqabp9CYghimkicvKWHtyAELuLIGpzaR5f8EaMnbz6-Orh-cDOUIAfj1RtpUhgopbc6YA195Q36Bq-7yJqKV2AIgFRjbNU0C3U_q_2810CnDWJmyguYOmHq-cKAz_OI0U1T1cPRvZ52FuTG1HXGQxTtj1bpuqg_W8LOcSAnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a15378585.mp4?token=ai7YXEMlXCbUY0NT4xI6LK0snIm_FgOJdEZ8qmTL_eVpTbsXOH0NgZ9G6xSTcbIgDTz7YyKAtAd30GF5QhCjyj8gxjkukddOrns2npm8tZlDkQATDZFdCsHMOf2wWIt9Ovj55GCE7XpfHBckIEgQJgZDDDT5OjUw51p5tZWC8Kz51npqabp9CYghimkicvKWHtyAELuLIGpzaR5f8EaMnbz6-Orh-cDOUIAfj1RtpUhgopbc6YA195Q36Bq-7yJqKV2AIgFRjbNU0C3U_q_2810CnDWJmyguYOmHq-cKAz_OI0U1T1cPRvZ52FuTG1HXGQxTtj1bpuqg_W8LOcSAnoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره یمن:
به‌نظر من، سعودی‌ها و نیروهای یمنی به‌وضوح مخالف آن هستند که حوثی‌ها کنترل آن منطقه نزدیک به تنگه را در دست داشته باشند.
این منطقه در پی تهاجم حوثی‌ها به تصرف آن‌ها درآمده بود و اقدام کنونی، واکنشی متقابل به آن است. ما انتظار چنین اتفاقی را داشتیم و همین هم رخ داد.
سعودی‌ها هدف حملات حوثی‌ها قرار گرفته و متوجه تهدید ناشی از آن هستند؛ از این رو، حق دارند که از خود دفاع کنند.
نیروهای یمنی تلاش خواهند کرد تا مناطقی را که از آنجا بیرون رانده شده بودند، بازپس گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72778" target="_blank">📅 16:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72774">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=aiG71NWbdrV5-z7GUKn5XP0ZZQaTTtL9KAWQinVuDoxynEz615SFqfUpdfXi-jNrlKLajZiuvRD6hj2F6Q9t4WmoowkDNXfWKN-b2EunypGU_ihhFI75BjhXT6MfO6oBpjtFYKJIkwE1nfn7XMotaXd7x6XuvFMjZ4INsHB9ccyHbg_MTUc01WLfDfH14vtqUy1RemE4-l18kjK2Zb-E0R9sOvxhgJt8o1UKNbblPWZVGUZxcPFp4B0JAvWUp9nr6IsoqNIwCfsVB78-Rci8XrpVf-Dc8A6LJBCggg-bxACn7SyW240zLr3WPq_Qm635U9_31EPXt46eByL4xFcVKyWI1bXw1x8NwYMB7FYiY1DVdcjZc0GCVafwNhjPd4LSLQBVzqe3mtjVOJoysXkwW-fs5jW62rGjXmyQ6yzl7ABM07QTTwhkLZUUqc49IFHx8BvQrkOmCGVPOFHOjKDZjVZjQ7HljJmi5T_1fm4NoAnzhvz5gxfOSaSXvLtUqa0mVCCR6b3-zuCjTb3Km3pAP0TDIEjDVO5prdAs98mcPMfgPXjzIwG_Px3usSZQGYGToUL-yql-gOyNGIzHPxEL-p7oHhvehLlklt073dBh_SYWGdHjIwjY6s06MXi77ukbRV0rpiHKXfvjd7te-9PhSlq5Sxg5x_8aCyo2xSGfgIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd09dcabf.mp4?token=aiG71NWbdrV5-z7GUKn5XP0ZZQaTTtL9KAWQinVuDoxynEz615SFqfUpdfXi-jNrlKLajZiuvRD6hj2F6Q9t4WmoowkDNXfWKN-b2EunypGU_ihhFI75BjhXT6MfO6oBpjtFYKJIkwE1nfn7XMotaXd7x6XuvFMjZ4INsHB9ccyHbg_MTUc01WLfDfH14vtqUy1RemE4-l18kjK2Zb-E0R9sOvxhgJt8o1UKNbblPWZVGUZxcPFp4B0JAvWUp9nr6IsoqNIwCfsVB78-Rci8XrpVf-Dc8A6LJBCggg-bxACn7SyW240zLr3WPq_Qm635U9_31EPXt46eByL4xFcVKyWI1bXw1x8NwYMB7FYiY1DVdcjZc0GCVafwNhjPd4LSLQBVzqe3mtjVOJoysXkwW-fs5jW62rGjXmyQ6yzl7ABM07QTTwhkLZUUqc49IFHx8BvQrkOmCGVPOFHOjKDZjVZjQ7HljJmi5T_1fm4NoAnzhvz5gxfOSaSXvLtUqa0mVCCR6b3-zuCjTb3Km3pAP0TDIEjDVO5prdAs98mcPMfgPXjzIwG_Px3usSZQGYGToUL-yql-gOyNGIzHPxEL-p7oHhvehLlklt073dBh_SYWGdHjIwjY6s06MXi77ukbRV0rpiHKXfvjd7te-9PhSlq5Sxg5x_8aCyo2xSGfgIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دولت ائتلاف مردمی یمن می‌گوید نیروهایش باب المندب و فرودگاه ذباب را طی یک ضدحمله با پشتیبانی هوایی سنگین عربستان سعودی از حوثی‌ها (انصارالله) بازپس گرفته‌اند.
سرهنگ ماجد النزیلی، سخنگوی ارتش، گفت که تیپ‌های غول‌های جنوبی و نیروهای سپر ملی، این مناطق را به عنوان بخشی از عملیات «فجر یمن» ایمن کرده‌اند.
نیروهای تحت حمایت عربستان سعودی در حال پیشروی به سمت مخا هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72774" target="_blank">📅 16:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72773">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=KKBJ_y7SgjGsZUrTxfo15s_wbbPg8R8VonvbfgWlxuwaB8z_F5x6AqofivsExk6D1N6CzBlq8UyQNsVWKlx0-KK2TSWlCtyq28NEoEl3d_nvN08NWBarghUcloLv4_XEDC1xVFVdtrVo47pAK-BoAzExLeq7p9M5t5HZ0WSAVxYehOC_1xpojcqv1Kla_fKwYX2IqdEZugmJ3bR8-tU4eIAOilETGh-x8MAhB6dPW_PSVdzJ9lXyxAGKbqYdY6QC0WLJW2n9wRjw4EGYWKtdXNpY6SCI7-XEicMDs9FqkY_oREY97v6sBT420dKOk05sVBfnDZbI__gus2uQyuT9Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ab7e166d.mp4?token=KKBJ_y7SgjGsZUrTxfo15s_wbbPg8R8VonvbfgWlxuwaB8z_F5x6AqofivsExk6D1N6CzBlq8UyQNsVWKlx0-KK2TSWlCtyq28NEoEl3d_nvN08NWBarghUcloLv4_XEDC1xVFVdtrVo47pAK-BoAzExLeq7p9M5t5HZ0WSAVxYehOC_1xpojcqv1Kla_fKwYX2IqdEZugmJ3bR8-tU4eIAOilETGh-x8MAhB6dPW_PSVdzJ9lXyxAGKbqYdY6QC0WLJW2n9wRjw4EGYWKtdXNpY6SCI7-XEicMDs9FqkY_oREY97v6sBT420dKOk05sVBfnDZbI__gus2uQyuT9Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات خلبان هواپیمایی زاگرس در خصوص نبود رادار و تاخیر پرواز
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72773" target="_blank">📅 16:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72772">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=ZiE8V29Z90R2v4DIwwM1DFguXiET6rG8O2DvTmiEwGJONx1GIuQz7dB0A_s2ZdFOhUngaEdFLUzzm9p1RmJkrD50CmUgq43HhyqFGbDFSWuavjTaHjXn6WccbJqnZ1ygEuyMimOwvu3tS-Lxna69eNA4cQbyV07qWFXZzqGdulmcp0ATWRIhCjUJLoPtysC7sxUOxwJLvQqsAzCy1E96M8Ai4j7TTfxz3YTykrkIr978BF4NUEErpD8k6tDXP2SQX7QVxTKVhVDhzll7aWWECSiTW7-Gd24trQxlVt_lWbUjRLOgp0e3WSV7AxI6iXjZOOKrwsmpaWMylr6rObhz0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ea9911386.mp4?token=ZiE8V29Z90R2v4DIwwM1DFguXiET6rG8O2DvTmiEwGJONx1GIuQz7dB0A_s2ZdFOhUngaEdFLUzzm9p1RmJkrD50CmUgq43HhyqFGbDFSWuavjTaHjXn6WccbJqnZ1ygEuyMimOwvu3tS-Lxna69eNA4cQbyV07qWFXZzqGdulmcp0ATWRIhCjUJLoPtysC7sxUOxwJLvQqsAzCy1E96M8Ai4j7TTfxz3YTykrkIr978BF4NUEErpD8k6tDXP2SQX7QVxTKVhVDhzll7aWWECSiTW7-Gd24trQxlVt_lWbUjRLOgp0e3WSV7AxI6iXjZOOKrwsmpaWMylr6rObhz0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی پویش جانفدا: در میان ثبت‌نام‌کنندگان افرادی هستن که اقامت آمریکا دارن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72772" target="_blank">📅 15:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72771">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=Ou5TEGWvMxC7BP9BzzcA1HD33KCVD2ABOrrZRwNKyFJ7V4v1Q4nRtZ5FfLyXCFjwXJZ98_eshiAksuWexNj-oSBerYyVi2h3JL-L9OMc49Gy2mgvMI0Vi9bLwXL9BBYuVFqogG0JUulOB_MkjVBZKKxVqybhHGcdVDTqBDFSEEoSY3UHl2NZW8puYMAgEtznvxgS4IEhnbOZDkFdWZ_zKcQYHIob_hlW-WSmM3vIvICRhwFR6Kawj1enOY2bkQs5Q1tvTi_mQVrLp0D0D9SJpi7aQTxyijjbwhh6ItOZbH6_DMVDeFmQVBEmyuU0ChEHXpcBRfozPImkG1iuopTFjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bbcade1f.mp4?token=Ou5TEGWvMxC7BP9BzzcA1HD33KCVD2ABOrrZRwNKyFJ7V4v1Q4nRtZ5FfLyXCFjwXJZ98_eshiAksuWexNj-oSBerYyVi2h3JL-L9OMc49Gy2mgvMI0Vi9bLwXL9BBYuVFqogG0JUulOB_MkjVBZKKxVqybhHGcdVDTqBDFSEEoSY3UHl2NZW8puYMAgEtznvxgS4IEhnbOZDkFdWZ_zKcQYHIob_hlW-WSmM3vIvICRhwFR6Kawj1enOY2bkQs5Q1tvTi_mQVrLp0D0D9SJpi7aQTxyijjbwhh6ItOZbH6_DMVDeFmQVBEmyuU0ChEHXpcBRfozPImkG1iuopTFjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاظمی وزیر آموزش و پرورش:
ما در آموزش و پرورش تمام هم و غم خودمون رو به کار خواهیم گرفت تا اقامه نماز کنیم در تمام مدارس کشور بدون استثنا.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72771" target="_blank">📅 15:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72770">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPe2GfMkFtDbVlbrFrX3kWHFP88inDROfJCXu4jtZlihjfJU4bcWlVFOqtbBX5dZlU-zG4V90kEWqK2i8onFtz69Aolqfvr2iQrqkQknn16HvoAAEztyTHLXG572S3rYymFAYx0xm3XJ1QGMBevbIre8DiOSRQJKmzq-PKa_SA8dNGgUs2IcI0noeSG0-v-T1eFsaUSmxeWHKknSUtQJDThW7AgQIWkuRxzcAvIQkGy2uzBxdK6qjGfLDzHj74MDZ-W3wmmqYtBNJe5Y9cKHCB4v_C1ej5OcPHSSi902Ok9S7_-eoNkZ0g86rjudV2Wr5gxfolOPYfUOhcjghOJmTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک نفتکش در فاصله ۱۱ مایل دریایی شمال «خصب» در عمان، از سوی سپاه پاسداران مورد خطاب قرار گرفت و به آن هشدار داده شد که در صورت عدم تغییر مسیر و بازگشت، هدف قرار خواهد گرفت.
نفتکش مذکور از این دستور پیروی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72770" target="_blank">📅 14:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72769">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aD0vcqmOTWg2ghDynyebIbJBSl0IyA90igBIMaQTcIItCznc_npdYFMjKgIXpR-sZkiU12SUgZJlXVGPbQaAsi-29ufvmIX_D7XGMtWO1BU26erJI8p__AGvDsfAlKdlcwQHhrUnlAIgXRrBkZubhFKg8yhhCWldSsEc_xk6JR6plQiB-qq_8E_Cr2qSxPwdPyo1KPWbywoHIXDh_l_pF0EgoD4PvoSqe_1znRuuPOl9GJtGsS_bYy1mffaHWZv-plba_VQQJaIu88bsY9VBy2vwFIzQxfVEs4JnOwDdD-Fd7QeBak0lSLqH3g9cFiWx7wrF4OaJwUBj5c2GaKUyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار در روسیه؛ قرنطینه نزدیک به ۲۰۰ نفر پس از مرگ کارمند مؤسسه ضدطاعون؛
در پی مرگ یک کارمند ۲۸ ساله مؤسسه تحقیقات ضدطاعون در منطقه ایرکوتسک، حدود ۱۹۷ نفر از افراد در تماس با او تحت مراقبت قرار گرفته‌اند و برخی مراکز درمانی نیز محدودیت‌های قرنطینه‌ای اعمال کرده‌اند.
با وجود انتشار گزارش هایی درباره نشت طاعون از آزمایشگاه، مقام‌های روسیه تاکنون ابتلا به طاعون یا وقوع حادثه آزمایشگاهی را تأیید نکرده‌اند و علت مرگ را ذات‌الریه با علت نامشخص اعلام کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72769" target="_blank">📅 13:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72768">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یکی از طرفداران پروپاقرص رونالدو:)))
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72768" target="_blank">📅 13:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72767">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مسلمانان در انگلیس با برگزاری تجمعی خواستار حکومت اسلامی در این کشور شدند.
جمهوری اسلامی بریتانیا!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72767" target="_blank">📅 13:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72766">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=V1eL0NZYGibZlLVbsvuQnhOyaokZVVrofhcnId2xBn3XqVUcWD8zYf-MK687ft9o9_1bcUC3tPBK5e_aBeSfOqE6iqcyVRDUgrMhoQwcxIcVgffXkMnsg1CTO4AfohhP2Dquhvl6ZIxlExn7UjTXJJeYLDJYRqqHIhZ-ryiZHbIgNqYgFbeRj-N3ERCRkOy2QNE8sJj7HKxaIy_sTvDCxhnFrT04r2UoLKVNuWDp80XLCdzEkdtiaUgl4RsGBHrTUbAcWRngwbgyiv3nbHEn8dLKdN5cNSSCFQ_JjV5pgBKJEX-QlJUIiMAZ4FrO9fQptP8RDVECSeQptQJxM_eLb3otysJsx3EIW7oISubSI2wOow-czsxaxMvlRtOBBpCQlcVxUUomchrIgsus75Gsul61t4eIAvs7JRMov_nQq_rfJfGLfRU00jLGE9YgEDFon5idpmEyZ6FvtVqKqeUCBpZtHTIy7URJKFaJNaEGB5hhnq_80AD5fCS0QCN5KlL302_vHb8i6NeIw7DJ8O4q40t1xOpY8eZgvqLkfhjm7elMW2SQcELha8fpJjiIMQ5bXfYQKzgPyWPIBiKrBC10sQBTN4grX4WytXJwpVtIP-tDlQ5jxU2FvaSdWJ5NwhODChBQ9nsuhzZNJWjRJYoRwvDS0wl0tab98HJHKqlXQGI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcebd0dcd.mp4?token=V1eL0NZYGibZlLVbsvuQnhOyaokZVVrofhcnId2xBn3XqVUcWD8zYf-MK687ft9o9_1bcUC3tPBK5e_aBeSfOqE6iqcyVRDUgrMhoQwcxIcVgffXkMnsg1CTO4AfohhP2Dquhvl6ZIxlExn7UjTXJJeYLDJYRqqHIhZ-ryiZHbIgNqYgFbeRj-N3ERCRkOy2QNE8sJj7HKxaIy_sTvDCxhnFrT04r2UoLKVNuWDp80XLCdzEkdtiaUgl4RsGBHrTUbAcWRngwbgyiv3nbHEn8dLKdN5cNSSCFQ_JjV5pgBKJEX-QlJUIiMAZ4FrO9fQptP8RDVECSeQptQJxM_eLb3otysJsx3EIW7oISubSI2wOow-czsxaxMvlRtOBBpCQlcVxUUomchrIgsus75Gsul61t4eIAvs7JRMov_nQq_rfJfGLfRU00jLGE9YgEDFon5idpmEyZ6FvtVqKqeUCBpZtHTIy7URJKFaJNaEGB5hhnq_80AD5fCS0QCN5KlL302_vHb8i6NeIw7DJ8O4q40t1xOpY8eZgvqLkfhjm7elMW2SQcELha8fpJjiIMQ5bXfYQKzgPyWPIBiKrBC10sQBTN4grX4WytXJwpVtIP-tDlQ5jxU2FvaSdWJ5NwhODChBQ9nsuhzZNJWjRJYoRwvDS0wl0tab98HJHKqlXQGI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای دولتی یمن مورد حمایت عربستان سعودی اعلام کردند که کنترل تنگه باب‌المندب را به دست گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72766" target="_blank">📅 12:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72765">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XP4T01zn4iHPTAcjvaWkF2E64Av1_011Tg21llUh4aiGvLOPhKCkB1xkLcvGHJLKWULUr-nyKtkOMPFa8AdSulHiiyz5dtz7yUkcP6i91FtEcrwMiZcnP1hBJevirkZTRrrsJV4ASmRGCoRuuUtcQ8d8dH6K-yUESUU8WBRKetZqcadltXuIGqS5AzcCDs9TniQf8X-lsWq39TRoYS7NwdmJK9p6Nfyl2ZhAs6_quQKguJIFjm84MXQdHojWQIG3SgI70-7CXDYhw8DtWccHZuH8FqIl2eI0UzmzLWPsAoEdckI-bBqpvIaMIEjUYyNaJ12z2Y-CeRsBk0aGiVc4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علیرضا سپاهی به انفرادی منتقل شد؛ نگرانی از اجرای قریب‌الوقوع حکم اعدام</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72765" target="_blank">📅 11:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72761">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=L_EhaL-1iamwb2PoGgFGmyJGbGcddgjfE0wTbM7S0EXOxsnR3UPuRb6As5Jci8cut9_pyMhiW5h3PvaFgZxnx4_WNC-Xrc4zJmKzYEPP5yL1t0-Bx5byCGDnkhOibmnwC56fUzXeIGCYRSNoPaCDCQlPI-L-e2JscE7yPwFq0uGEAf4u1C7bzApfRj6AMlH1A8paj76jRCHs6fNXJlys-R07WV39kDjplopM_Oya4sln3jv8S6vw1boCB7PbsV8xvwWqUpMSvtAreBvM4YAcwfRF02ZnQ3JOF_N4HM2fMIug4zRlrev7bME0Zh1zj62SBHh99WBAhItFBLCUF4QvCg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e88e1de928.mp4?token=L_EhaL-1iamwb2PoGgFGmyJGbGcddgjfE0wTbM7S0EXOxsnR3UPuRb6As5Jci8cut9_pyMhiW5h3PvaFgZxnx4_WNC-Xrc4zJmKzYEPP5yL1t0-Bx5byCGDnkhOibmnwC56fUzXeIGCYRSNoPaCDCQlPI-L-e2JscE7yPwFq0uGEAf4u1C7bzApfRj6AMlH1A8paj76jRCHs6fNXJlys-R07WV39kDjplopM_Oya4sln3jv8S6vw1boCB7PbsV8xvwWqUpMSvtAreBvM4YAcwfRF02ZnQ3JOF_N4HM2fMIug4zRlrev7bME0Zh1zj62SBHh99WBAhItFBLCUF4QvCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت خیابان های فرانسه پس از اعتراضات گسترده دانش‌آموزان و دانشجویان به دلیل کمبود معلم و وضعیت بد مدارس
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72761" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72760">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72760" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72760" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72759">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oom_tX93Gce37Vj_SRJ6Nli6L2kLem0ObmvkM3KjFumC6Mog7yjdN-MSi6wtYfZarisXFntQNid1uqPZqXo-jbflgPUbNMHUKJX6b8Xw3VH7LZubmn-BKJcQuOynl9aAumvuOFZQzezBxQELDizBwH9Ebe5oEhHH1NlVRgihCS6jyDE51_CLtcQRvy73fwhcZBn0g4J8kqn3Qvw69trMTwIVLlEHrg3xgCgWuG8DQtSKkr7mxCmY9lxkwZ8-ABCfppmUrThxX-Q9EYpzmE9qcZyp2mb3lC5OoQ9M95Qu-PECTXobSYFI5rM5FymIYzXiWFzJ2MoO6mg_Lw_72O8kPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
فرانسه
ترکیه
🆚
ایتالیا
لهستان
🆚
بوسنی
سوئد
🆚
رومانی
نیوزیلند
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
http://T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72759" target="_blank">📅 11:31 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72758">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=mUOf_G3lFn3-imZrUzqDijG-0fryY0b5UCUhl_-wkOeyWsOlf8U_kB9rp4uqADcdgbYuRK3gpmCOdNmg0_YGfYC2RII4k7viBT2J2RM2NmokwKc0RBHgcr8NQVo9UU22lb18gYAaiQHMKi9SgzM5iHF8dSD0Wbh3fj3ANMMQS5mWENpeBV6zCy-nGfFSUWz5Djuy1s4QMJmhPuFzcP-Wl57Rww1WRWYZ2_FClNJ0IQnpOJRMrYJWRQY34J4O0TqHcl7C_05eFzwOlVllyiutqLbx64HJoiYRuumJnbMMRNTdI8Bhk6yrpwUvq_sHaIkIPtX4qxG8dfLDLtMapnaOVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=mUOf_G3lFn3-imZrUzqDijG-0fryY0b5UCUhl_-wkOeyWsOlf8U_kB9rp4uqADcdgbYuRK3gpmCOdNmg0_YGfYC2RII4k7viBT2J2RM2NmokwKc0RBHgcr8NQVo9UU22lb18gYAaiQHMKi9SgzM5iHF8dSD0Wbh3fj3ANMMQS5mWENpeBV6zCy-nGfFSUWz5Djuy1s4QMJmhPuFzcP-Wl57Rww1WRWYZ2_FClNJ0IQnpOJRMrYJWRQY34J4O0TqHcl7C_05eFzwOlVllyiutqLbx64HJoiYRuumJnbMMRNTdI8Bhk6yrpwUvq_sHaIkIPtX4qxG8dfLDLtMapnaOVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
جنگی که توی راهه، آخرین جنگ ترامپ با جمهوری اسلامی خواهد بود!
اما به قدری این جنگ شدید و گسترده‌اس، که جنگ ۱۲ و ۴۰ روزه، پیشش یه شوخیه!
شدت بمبارون‌ها خیلی شدیدتر خواهد بود، کشورای بیشتری درگیر میشن و این نبرد آخره!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72758" target="_blank">📅 11:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72757">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=j1t0nkV_jLL4q9VJm14O0iVzAXl5WNUc2gI2EoWDv05fX7soOvh4oDVcKfyOnVH91P2ZOfoV6MZKqnKHdTqLTDxn9YZpB-zGIpfh6v935RZkvKsvM5_C40RXHs291pPK_JRBF6nUmfBEiFD-9Po6h7nuw_Rja8n4IFMEsr8R3Ad2aatMljtRzPscJSRaXi3JXWDI1uE1PSijX0ASuEbEol2AgtjKSEBwy82BVB-CG94Uy4YVbIFAwoyU0pjcVHmnnwkMkZWLvg1G1KfGFPMRdU6sP4qOva5D97cqkukWV_JADf3rMcjOw0ARD97u8DmKgLQyNbNTA5VmGpTnF38mUA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf7a6e5830.mp4?token=j1t0nkV_jLL4q9VJm14O0iVzAXl5WNUc2gI2EoWDv05fX7soOvh4oDVcKfyOnVH91P2ZOfoV6MZKqnKHdTqLTDxn9YZpB-zGIpfh6v935RZkvKsvM5_C40RXHs291pPK_JRBF6nUmfBEiFD-9Po6h7nuw_Rja8n4IFMEsr8R3Ad2aatMljtRzPscJSRaXi3JXWDI1uE1PSijX0ASuEbEol2AgtjKSEBwy82BVB-CG94Uy4YVbIFAwoyU0pjcVHmnnwkMkZWLvg1G1KfGFPMRdU6sP4qOva5D97cqkukWV_JADf3rMcjOw0ARD97u8DmKgLQyNbNTA5VmGpTnF38mUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره یه دختر تن فروش: یه دفعه یه سید بهم گفت بیا رابطه داشته باشیم، فقط تو زود بیا چون ممکنه خانمم بیاد خونه.
رفتیم تو اتاق و شروع کرد صیغه خوندن، هر چی قرآن، آیت الکرسی، تابلو و کتاب دعا بود برعکس کرد و گفت زشته، گناه داره.
یه دفعه وسط عملیات زنش اومد، گفت سید زودباش درو باز کن خیس شدم زیر بارون، سیدم بهم گفت تو فقط چادر بنداز سرت شروع کن نماز خوندن.
خانمش اومد به سید گفت این کیه؟ برگشت گفت این خانم مسافر بود، اومد گفت نمازم داره قضا میشه، میتونم خونه شما بخونم؟ منم آوردمش نماز بخونه.
آخرشم خانمش بهم چایی داد و کلی پذیرایی کرد و رفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72757" target="_blank">📅 10:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72756">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=jn0BaYCucDV-dkVpjz0C-EqioOlb_-cZAWaENIX4BHcXSltYlew3mP_wxjcOCuIpG9WO48F0ki09xHm2jhF-WkaRuZkdXxZvTBsJYR1c76tRTdeFBDxu9liWgB2rNDQyCouuEgQi031Xy4XDi9IFwK3cXTQiphNwgAgjb81OI_HPwpnFE7zJz3uJTLEUtXz2oQt7dWHFnqf5Wilk2vLV-VvmcBWoOBpvYC7B4lpt-2zQ4ZsnTFQi7tA0fvniARxA76aO-vi_pBXuEaMnfdL_V6H-qD7tVVQMH17hN6hvIEkXwSF_-zA2DWGSvSWkTVZDfFUibK0NBi3t7THl32nxpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de6e0dfa99.mp4?token=jn0BaYCucDV-dkVpjz0C-EqioOlb_-cZAWaENIX4BHcXSltYlew3mP_wxjcOCuIpG9WO48F0ki09xHm2jhF-WkaRuZkdXxZvTBsJYR1c76tRTdeFBDxu9liWgB2rNDQyCouuEgQi031Xy4XDi9IFwK3cXTQiphNwgAgjb81OI_HPwpnFE7zJz3uJTLEUtXz2oQt7dWHFnqf5Wilk2vLV-VvmcBWoOBpvYC7B4lpt-2zQ4ZsnTFQi7tA0fvniARxA76aO-vi_pBXuEaMnfdL_V6H-qD7tVVQMH17hN6hvIEkXwSF_-zA2DWGSvSWkTVZDfFUibK0NBi3t7THl32nxpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه عراقی :
به حضرت عباس اگه بگن بین پسرات و جمهوری اسلامی یکیو حذف کن میگم بچه هامو حذف کنید تا فدای جمهوری اسلامی بشن
ایران از بچه هامم ارزش بیشتری داره
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72756" target="_blank">📅 10:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72755">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=uukx3tMon8Fpeu0MoKfR8qCmF2k3gFDU2-UCEFO1CcmNUg4rR-mgQsg1HS3qJAZKOkSHu5KciV-2_m1ZUdbzef1C7o3ml7c32AImUGqVtU-bgIEkvX2EK5tHmLZsIj8MKLBKDJ7aafF16IhGNF3RohOqkHZCI2hYeqaYVEWEJjVaRITn4pVPQprU1vXX8WjtNYt5tKRKMIiPlalhQx1kmeYHIWNdFsQoAa1FhOh6TQDxSWODAHGhQgi1NyuWIh5i-GMj70HmTTj8muMwRzgh3UxTocYXfYEfu4kfPDitNP_-Z3QXPcs3EQzkAB9fE9UeecAPAa9bPzcngfKRLlaSMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaee08d663.mp4?token=uukx3tMon8Fpeu0MoKfR8qCmF2k3gFDU2-UCEFO1CcmNUg4rR-mgQsg1HS3qJAZKOkSHu5KciV-2_m1ZUdbzef1C7o3ml7c32AImUGqVtU-bgIEkvX2EK5tHmLZsIj8MKLBKDJ7aafF16IhGNF3RohOqkHZCI2hYeqaYVEWEJjVaRITn4pVPQprU1vXX8WjtNYt5tKRKMIiPlalhQx1kmeYHIWNdFsQoAa1FhOh6TQDxSWODAHGhQgi1NyuWIh5i-GMj70HmTTj8muMwRzgh3UxTocYXfYEfu4kfPDitNP_-Z3QXPcs3EQzkAB9fE9UeecAPAa9bPzcngfKRLlaSMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار :
از آقا مجتبی (خامنه‌ای) چخبر؟
حداد عادل پدر زنِ مجتبی خامنه‌ای :
سلام میرسونن...انشاالله خوبن...همیشه...خوبن الحمدالله
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72755" target="_blank">📅 09:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72754">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32e173a359.mp4?token=JxluhMZLxVMHeI5rjSmfIkHXqv1Iah_cla1E6YIkzzWIDfTnO2yoamCW7Snm4YxJhxHWU17Q4pQmWSW80y4wJtdIeoViGn9RV0FpVs2mu2ROyUyBMUqBuZxyqD8EhCvhaXAs_7gMCxiGo0l3bJY4xPFkUB26VqVEbq_DGcvsvk0GUKfwI0PcjqHgw6gRawSvm0rgkbu2u-06-emixlAHuURc4K-CCVnudDHbzPdBekCwycEw634nriqkldneJqvQarz9riwqx9dhrAzjV8dZPrJOeXT9gJOLMyC7bpNQoBi_wgVrXyMXZDBEp1UI6Hw4JqlLR76gKjDbCjin2GJArQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32e173a359.mp4?token=JxluhMZLxVMHeI5rjSmfIkHXqv1Iah_cla1E6YIkzzWIDfTnO2yoamCW7Snm4YxJhxHWU17Q4pQmWSW80y4wJtdIeoViGn9RV0FpVs2mu2ROyUyBMUqBuZxyqD8EhCvhaXAs_7gMCxiGo0l3bJY4xPFkUB26VqVEbq_DGcvsvk0GUKfwI0PcjqHgw6gRawSvm0rgkbu2u-06-emixlAHuURc4K-CCVnudDHbzPdBekCwycEw634nriqkldneJqvQarz9riwqx9dhrAzjV8dZPrJOeXT9gJOLMyC7bpNQoBi_wgVrXyMXZDBEp1UI6Hw4JqlLR76gKjDbCjin2GJArQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حاشیه ختم خواهر عباس عراقچی، وزیر اقتصاد از پاسخگویی درباره وضعیت فروپاشی اقتصادی و کاهش ارزش ریال فرار کرد و خبرنگاران را به همتی، رئیس بانک مرکزی، حواله داد و همتی هم بدون پاسخگویی فرار کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72754" target="_blank">📅 09:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72753">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72753" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72753" target="_blank">📅 01:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72752">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/haUuauKXyK6gexh7oiyHdB-1SFVSFaU1Upkm_Sxsy_yxI1KKMZe3KLaQY-lR32coN6Dsjo1n_e_dhMDlfL6VbKKopjHpAbqDRASuqAivlTpOZHzTmwM-G1mnVEXM9aKmcF20-x7s3rYXCuJpwH1JIuhcRfNp_KuBqqrMz-jMzCdTkKJkyGrCQZFM3pyWCYEYcEt-_k9fiQJYx8nGw28QODY1UzJo6HO9fdjCiMOT_l8Yd6OSDKPCwbj1ytMqjChx8NrmWdho_EbtFV_whuplpEiUF2s5aGU7HjiuFjKN8jhjo8GDOsq-7G29EGc-g_NkJ04D_YECXvFS-fEcEhJ7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72752" target="_blank">📅 01:41 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72751">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/krLsCi-Q0LDE5VS_QCITtyR2_9FECH9f02pdd31GhELGHgPNYJPdEvzCkSvSQxJtoWSCvwSAc-2lIg8CeNN56UhqTiR-d-YKSZTa97TLaON9-MeoD0ajRSYoKU-UZB6RbuSld8S4ZvHbm0L8ykATR7R-RpE7ShqdnrerzfQfi3aiJ8ac7xYU5G2fKb7zDfTvh3bQi-WVlZndrS3vbU6qq2ve2e2VLYZ72BU3lfTG8kUubzOsa_M2Rpp4I9-gYnvwn_KMZcDPmCevrQNyl3fWz2kHW06gpuOqoabJHnPgG64vxaJoNs2HJ-Aao24gNGCqPrrgU0OJBDEqMBFm434QgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال‌استریت ژورنال به نقل از مقامات آمریکایی گزارش داد که بمب‌افکن‌های راهبردی «بی-۱بی لنسر» (B-1B Lancer) در حال خروج از پایگاه نیروی هوایی سلطنتی بریتانیا در «فِیرفورد» (RAF Fairford) هستند؛ این اقدام به دلیل نگرانی‌های امنیتی و در پی دریافت اطلاعاتی مبنی بر وجود طرحی از سوی ایران برای حمله به این بمب‌افکن‌ها در پایگاه مذکور و کشتن کارکنان آن صورت می‌گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72751" target="_blank">📅 01:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72749">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bRIBZ6IgPh3OWawCDkazLNMqPZ9NQHh4CUF5tlCrBpn2E6WaZZExjXklgSAKuqbRI8rDX508CSTx-RqPlNzB-uKWG7TUYUmONQfcoE0Ux_4_qI6NZnEIy71_s7E7vYiDG_sp86arF2JFGER6nIalPPcD62G6apAIydekmjSKghEinlTAi8Guwrls-yV0Qz5FSABN02u6Rx0ReXqMb3pxKxbZKFixyq2iOQk2x62sC6iqsOLfoEHrlk_ppjBPYSG8hIVy0XHPrtAGo7mvW61dp_OGOtpn24sj0LGzhGfahUvOpoQ2Fux4AabQjMNw3o_vzyZMyEsyoJW8bkMzV_wgqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5cef955dd4.mp4?token=tIEWbBomnU5MxvPsU2RkgD8nWQ0-ihQveiWGBFOUu6mh4AvFxHqPHwmeJTQIGljQALdP9dn1-QnGjTm6GbJfoGxOKm5dBK_uFGYE1L63DrBO_3gLyXe7GXOW66rqmoMw1PwNEmpLm9LXj45M2p6dsfQVFgiqFBwAPhiCXlhTFC3a_XBKqnCN9zE7ZTKm9lhVz81-0hw3StILMnm2j0xjCXG9fq0V7m9PX0q6O6FlvsFZ_rfim2ij51T3GO0pTNodKzxF1MxRE9psjjp2FSIPHLLsScL0_SQNuJ4NBbnOtTZEw1q9hcRouG2M-HQD0d57l1uYCzOac-YP391pVpIkXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5cef955dd4.mp4?token=tIEWbBomnU5MxvPsU2RkgD8nWQ0-ihQveiWGBFOUu6mh4AvFxHqPHwmeJTQIGljQALdP9dn1-QnGjTm6GbJfoGxOKm5dBK_uFGYE1L63DrBO_3gLyXe7GXOW66rqmoMw1PwNEmpLm9LXj45M2p6dsfQVFgiqFBwAPhiCXlhTFC3a_XBKqnCN9zE7ZTKm9lhVz81-0hw3StILMnm2j0xjCXG9fq0V7m9PX0q6O6FlvsFZ_rfim2ij51T3GO0pTNodKzxF1MxRE9psjjp2FSIPHLLsScL0_SQNuJ4NBbnOtTZEw1q9hcRouG2M-HQD0d57l1uYCzOac-YP391pVpIkXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا سپاهی به انفرادی منتقل شد؛ نگرانی از اجرای قریب‌الوقوع حکم اعدام
علیرضا سپاهی، از معترضان بازداشت‌شده در جریان اعتراضات دی‌ماه ۱۴۰۴(پرونده میدان علیخانی اصفهان)، به سلول انفرادی زندان دستگرد اصفهان منتقل شده و خانواده او برای آخرین ملاقات فراخوانده شده‌اند.
وکیل علیرضا سپاهی نیز انتقال موکلش به انفرادی و اطلاع خانواده برای آخرین ملاقات را تأیید کرده است.
بر اساس گزارش ها دختری که عاشق علیرضا بوده گفته آرزو دارم باهاش ازدواج کنم و امشب در زندان خطبه عقدشون تلفنی خونده شده
💔
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72749" target="_blank">📅 01:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72748">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvXmU7kbNWFmCncXC3IpcsftLGFRDQr4ZffCSeyWX3CMUTtN-WOgCPb0mYVOTnb1MmxdffoQpSOm1BGkpCo6dl0WjjbQ0HXzEh0wVEFjRmGWsivqN-Pzx0BAFryQVX3DLJ4IA60WOUveudsfOfCPj-wI9Bis5yHL4fF4QfSFieanXbDHzoSTs20riBDA-jyk1BBNT3VIU0k6I6TvA6nIcalL75A0sTVgVK-RpjI8SOqNCnmpRKuEdWIHOF5e8ALy6jiFAao1SsQ2cI-2fe4ppYNm1uvamC1_hpIQxis8RMZJRKH3Kweaj3W59rZpI2fSn8MBhAjlA-1z-2We1-U1Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید صفحه یوتیوب امیر تتلو:
امروز دادستان و رئیس کل دادگستری صحبت‌های خوبی با تتلو داشتن و اگه گزارش خوبی هم رد کنن، امیرتتلو فردا آزاد میشه و به استقبالش میریم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72748" target="_blank">📅 00:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72747">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">۱۰فروند از ۱۲ بمب‌افکن راهبردی B-1B Lancer نیروی هوایی ایالات متحده که در پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) انگلستان مستقر بودند، در حال ترک این پایگاه و بازگشت به خاک اصلی آمریکا هستند. انتظار می‌رود دو فروند باقی‌مانده نیز امروز این پایگاه را ترک…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72747" target="_blank">📅 00:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72746">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=XtQrXPlyU7W1E0_1iNsGFUsmA-_ooXWE8YOIvXtSoB6LY7vFjIIl2wdAOePDk2-sdkzeEPR-GpmNmcf_ZzII5o_BVn6oiBox6Q0NhenfmusQX8DGuFzdjkNdyZj-ul5UlxwF90TY0wvWsaOEtycPxkkULXEtVD_NOPovV3E_QUcc9DWJ5S9Ih4qifBdrtvEY-lzSqRTd4ocojfPnhMdkT6MYN1xhRFPIJnhpI5o-Rv3ymsAf0ZPX4DLrlOuXGpdHxgn1HdCuqmma9yGA2p_bUCkkF4qQJTfEN41b19xfJIrw4E-kOj4diWgpwM7pW5k6vEaix5NUzb4-yLJ-mhlgxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec28377bbb.mp4?token=XtQrXPlyU7W1E0_1iNsGFUsmA-_ooXWE8YOIvXtSoB6LY7vFjIIl2wdAOePDk2-sdkzeEPR-GpmNmcf_ZzII5o_BVn6oiBox6Q0NhenfmusQX8DGuFzdjkNdyZj-ul5UlxwF90TY0wvWsaOEtycPxkkULXEtVD_NOPovV3E_QUcc9DWJ5S9Ih4qifBdrtvEY-lzSqRTd4ocojfPnhMdkT6MYN1xhRFPIJnhpI5o-Rv3ymsAf0ZPX4DLrlOuXGpdHxgn1HdCuqmma9yGA2p_bUCkkF4qQJTfEN41b19xfJIrw4E-kOj4diWgpwM7pW5k6vEaix5NUzb4-yLJ-mhlgxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای عجیب در تجمعات شبانه: حسن روحانی در یک سفر استانی دستور داد برای دستشویی‌اش کولر نصب کنند!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72746" target="_blank">📅 23:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72745">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673e09822.mp4?token=tVJSXRLpBdBnhj-5n51q32Tf-srx1rpIRESXNEWnizuAaqtJXWS4WovT4vLeKNpPD8jh0tYR9hYomJWFgMUyJDcjz5C6LxIY6S5cYlbE8OAi-r2WuB36LMlhr7f3B7Yk71S63KWN3SHdxPl4HSuPsETeup9reB7A330vGx72C8ser5Vv3Ikkx64p775TVc0GngBE4KO5c0hutAgIS1AyuBwMlPr4Iesiwg2Kta2JCtATswtLVyBtgj66kftI95hBgccW9_ifhbDZ7bdyylIrnoFtHdyqlJsPmolmnCNOO1bfYtC_xOOaPD3uXLwfpo5MXa1kPCA-yB0HXYZrYn03Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673e09822.mp4?token=tVJSXRLpBdBnhj-5n51q32Tf-srx1rpIRESXNEWnizuAaqtJXWS4WovT4vLeKNpPD8jh0tYR9hYomJWFgMUyJDcjz5C6LxIY6S5cYlbE8OAi-r2WuB36LMlhr7f3B7Yk71S63KWN3SHdxPl4HSuPsETeup9reB7A330vGx72C8ser5Vv3Ikkx64p775TVc0GngBE4KO5c0hutAgIS1AyuBwMlPr4Iesiwg2Kta2JCtATswtLVyBtgj66kftI95hBgccW9_ifhbDZ7bdyylIrnoFtHdyqlJsPmolmnCNOO1bfYtC_xOOaPD3uXLwfpo5MXa1kPCA-yB0HXYZrYn03Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سیل اخیرِ گرگان، یه
موش
برای اینکه جونشو نجات بده، این شکلی داشت تلاش می‌کرد...!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72745" target="_blank">📅 23:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72744">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=lXovmqREe6ec_zDLDHdyalrCsqm4C5iLXpko_QemUyxPOMtHw8payUUnMc55HtJcrvWAhnzRBOtTwKNfFpthk9BTjkAtEP6zGloNpb0BthYYPqdC-mdRqgG5av8aia3k7GUZ5R0OMmDOEU3vINXDSwjjZmVwTJnapacifI6rg_xgQJ3bJY8Ho4vtpifdmXtvm5VVaV2tkr5-0s-_TaKUUf_0BA5MlEyJ9wIIBqOQkN_RT2ftE1UBc9K_-7VfEay2i1ZsN8TGu81OABcujgL9MY0pmv0ZfcjJvZXhA07b8jSX5gl7x77q8k1_dDB_oeka6nZLtKQFgqFAB6s1DeQhen7axMDQKXQHfAi6Ep9brAMmrNHOEhq0jZa64HChvtEaAi_yLEig4BQOvf0sdy3SsKYe8O7cLeLsO9fOLnKaETIS9YdXrbsN4j35tFcLDmAZ2k3WLTo8yVzXKP4micrkzEtbeLY6StZzuHRkdTj7_kDgyOiiXzG8ny3vku7ZJbbkzqNb7QonQ6S3j7QQfq5goBkZD5yPDbBaLKX91wY74uFVMwJvK14Kl-GBvqKRJa5OyBUweobrYOPU3j8ZWHGcAPylzEugmp8cQ2noIbYcnSIVAqUSyDLoXQfXlwTvNZZLBGworrX5_4kbNDmMp-wmsdk5_7QHlUrkcijyBh3CgD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bffb33370b.mp4?token=lXovmqREe6ec_zDLDHdyalrCsqm4C5iLXpko_QemUyxPOMtHw8payUUnMc55HtJcrvWAhnzRBOtTwKNfFpthk9BTjkAtEP6zGloNpb0BthYYPqdC-mdRqgG5av8aia3k7GUZ5R0OMmDOEU3vINXDSwjjZmVwTJnapacifI6rg_xgQJ3bJY8Ho4vtpifdmXtvm5VVaV2tkr5-0s-_TaKUUf_0BA5MlEyJ9wIIBqOQkN_RT2ftE1UBc9K_-7VfEay2i1ZsN8TGu81OABcujgL9MY0pmv0ZfcjJvZXhA07b8jSX5gl7x77q8k1_dDB_oeka6nZLtKQFgqFAB6s1DeQhen7axMDQKXQHfAi6Ep9brAMmrNHOEhq0jZa64HChvtEaAi_yLEig4BQOvf0sdy3SsKYe8O7cLeLsO9fOLnKaETIS9YdXrbsN4j35tFcLDmAZ2k3WLTo8yVzXKP4micrkzEtbeLY6StZzuHRkdTj7_kDgyOiiXzG8ny3vku7ZJbbkzqNb7QonQ6S3j7QQfq5goBkZD5yPDbBaLKX91wY74uFVMwJvK14Kl-GBvqKRJa5OyBUweobrYOPU3j8ZWHGcAPylzEugmp8cQ2noIbYcnSIVAqUSyDLoXQfXlwTvNZZLBGworrX5_4kbNDmMp-wmsdk5_7QHlUrkcijyBh3CgD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک جانفدایان در اصفهان، سازماندهی اراذل و اوباش با قمه و شمشیر و چاقو!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72744" target="_blank">📅 22:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72743">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7gHDr7h0R9EnontMQLZAYJHEY_J4p_vgbamDT3oDS6OQ_yCoZE5NH2Pymx4h0-iVDWQmPhd6QtCx7tNpo1u3ehlzL_ecdnQ3v0PCzh7HdOC_ZSlxUawDfPyP8vCaH3EX4gzp8Y3OXcf4GGrgjpP5lSkROR1fapnh02igKZcMeQ5KQJRYHTQNT1CC4oaYsv5mQFJCpo6-xolE78K1zlewVbJo1MWumaabw993GWyzR019kQl5HdKcoq6sMxJVejU957MkX1m_3-JG7gsfCmybqjSiyA8U_0RLmzd8psc3cVDJk5gTYXjm-lOKR7aoBe4_72XPGU_4SP2hkkNdsJYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تصویری از خود به همراه پنگوئن‌ها در گرینلند منتشر کرد.
پنگوئن‌ها در گرینلند زندگی نمی‌کنند
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72743" target="_blank">📅 21:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72742">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم   @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72742" target="_blank">📅 21:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72741">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شنیده شدن صدای انفجار در جزیره قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/72741" target="_blank">📅 21:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72740">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=gBP9zs1xWDI4p8uwiN7KWgkeYNSCSw5agreBNXS6CuJotR84A9DSEKMiydZJ0-Kb22IEIT_ccFHVs4eM2wG_ifSYzjruXekmpE41I1VdTMIveS8ZCGCZPMrc7yfU_mH0YH1Fm7tXQVm4fFqL-GOLB2wFyy3MmA7wThO4d02f_IUACwthmGqfYiU_R3hsO4oJWw32wUKJQM-5jII6mepzOr2M_XmwxeFLtDaj1Zhbjept0YcDg7Y1FxCsQ_s5WDSeISUdlaCuYk20xT5w2j_SSXVeZNdTgsQovkf19TssxwKtRHxVQFGG5y4geeDblBI1TiwilXjkvcIUmPShadrKrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d25df363a1.mp4?token=gBP9zs1xWDI4p8uwiN7KWgkeYNSCSw5agreBNXS6CuJotR84A9DSEKMiydZJ0-Kb22IEIT_ccFHVs4eM2wG_ifSYzjruXekmpE41I1VdTMIveS8ZCGCZPMrc7yfU_mH0YH1Fm7tXQVm4fFqL-GOLB2wFyy3MmA7wThO4d02f_IUACwthmGqfYiU_R3hsO4oJWw32wUKJQM-5jII6mepzOr2M_XmwxeFLtDaj1Zhbjept0YcDg7Y1FxCsQ_s5WDSeISUdlaCuYk20xT5w2j_SSXVeZNdTgsQovkf19TssxwKtRHxVQFGG5y4geeDblBI1TiwilXjkvcIUmPShadrKrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۰فروند از ۱۲ بمب‌افکن راهبردی B-1B Lancer نیروی هوایی ایالات متحده که در پایگاه «آر.ای.اف فیرفورد» (RAF Fairford) انگلستان مستقر بودند، در حال ترک این پایگاه و بازگشت به خاک اصلی آمریکا هستند. انتظار می‌رود دو فروند باقی‌مانده نیز امروز این پایگاه را ترک کنند؛ بدین ترتیب، دیگر هیچ بمب‌افکن راهبردی‌ای در «آر.ای.اف فیرفورد» حضور نخواهد داشت.
پنیک نکنید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/72740" target="_blank">📅 20:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72739">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yr3L_lOGgMg7frH9zhy2xwr1Q75zhwPLdythTyUkn4zdDCqBODJJDKcKHhk3dHvryGHZYCBFMsWbMJ4MI17nJsMyeb_Ig1boyY3WL_nn-eOLADweLam1cuqqoNrp0Eu9eKWrfNOyGY0KAEWQZLRcOG05BpoksWNBDcKYP_FgksYNL3hcbp9THmG56QBYVIJZcc5JyndNy4w8R6Od_kgzm1VyxaAbF9iS823v0b6LzvgSpnqhN0379L3LZsQ93zOjk6rehpeeuyQaNs294QFBu4KVdhPBWbEekQyePKRtIoNs59OSh0CPJ3hikcRGZOO3xDZpSrbiokEBG1irOKxG6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛محسن پاک‌نژاد، وزیر نفت جمهوری اسلامی، استعفا داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72739" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72736">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=R8U1eGBMf6wfybXDzI4ivDzhZylXbvT_WIw9DpmKToFOUXAScmrdf9WvgsrvYF0zBADaEBL9c9On7HwPjDgeVxyVFl9_ZwT5tPWXBx-HO7gSg935Z6jL1c9gDLD_7yYuge_dlFmxG21je17cPC9ItSdjLcjODxjboPhh9bS_lHUMfDq2O1A0xQk1Efv3r-yS8oNWVLn0j6MKyVf9ORDuPvOF3Xldvv0x_Et2l1BfDiueOw8yNr3o6eblKxbOFX8cG38IXsThMlYQTd7_7hh3Q-axBVnkH010C9_700CxphSmVU7RsXJpqDS4LOprAl3GmT0XLqWJURr0rSgXjL7UJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1dad032a8.mp4?token=R8U1eGBMf6wfybXDzI4ivDzhZylXbvT_WIw9DpmKToFOUXAScmrdf9WvgsrvYF0zBADaEBL9c9On7HwPjDgeVxyVFl9_ZwT5tPWXBx-HO7gSg935Z6jL1c9gDLD_7yYuge_dlFmxG21je17cPC9ItSdjLcjODxjboPhh9bS_lHUMfDq2O1A0xQk1Efv3r-yS8oNWVLn0j6MKyVf9ORDuPvOF3Xldvv0x_Et2l1BfDiueOw8yNr3o6eblKxbOFX8cG38IXsThMlYQTd7_7hh3Q-axBVnkH010C9_700CxphSmVU7RsXJpqDS4LOprAl3GmT0XLqWJURr0rSgXjL7UJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رتبه یک کنکور تجربی همین‌جوری داره بین موسسه‌های کنکوری دست به دست میشه و تو همشون میگه که من از بچگی اینجا بودم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72736" target="_blank">📅 20:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72735">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/112f06092b.mp4?token=aLSq3-monHuHXEztNh02HYJiOBQF4kXe_zEhwH_DGCB9Rx7b1rLKEapE1omAhuCTDC0zQe9N2ILg5klWwtnC-3bQfw3SlmIMTMrV0cBK1V9XTmz4_mjWnIh9mM9Ratc2c2GR5dGHLLAnfJ-eIKXVvnWfYmnzpp6tbzz8zkkg191vg_Th0LRLQjzMpXjLW1HgYNIlkoui9ygSHgWKq_7ev7YtwUIZ53lu8Z31QTkjpPMPNmI7kZCv5bkXb3_s70N8EQGwnbo18mWxttLG2Kkf6gBjrU9GlHt52R1S1qzEfulZFsTh-TznTQJMxLqSkeHQqOQlsmLFkzpWtYf-4eOK8wuhqxFIPm_R_dMDs3Io-4N3DTmHg5vYtgMASC5AzNrGc0YMYb8J9X9NuAPxNeR6CBrZXKysjiuFm366UAEXMvcUonzz_Q2btAriwhd5UPwh3H5Io0UfihXy3OdOryAuRVhoWzfvyizHnT7jC8WonIxh8M4Eieo_nKtxnbJ8u8xih-QXhjWvW4JIcbjSqPIQtleXqjah1NDIrJVl-IfArodClFxbDimHUtFGUoDYQpNQP2LvY5NyCqVABIHff8DwGiqQoGoxrkrAwSyqoFMndizkLxUWMe-Esod7OyU5xFj22PQ2OJJZ3SwuBfCzBaohCsGgw5cvyskl6Es_yIojFfI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/112f06092b.mp4?token=aLSq3-monHuHXEztNh02HYJiOBQF4kXe_zEhwH_DGCB9Rx7b1rLKEapE1omAhuCTDC0zQe9N2ILg5klWwtnC-3bQfw3SlmIMTMrV0cBK1V9XTmz4_mjWnIh9mM9Ratc2c2GR5dGHLLAnfJ-eIKXVvnWfYmnzpp6tbzz8zkkg191vg_Th0LRLQjzMpXjLW1HgYNIlkoui9ygSHgWKq_7ev7YtwUIZ53lu8Z31QTkjpPMPNmI7kZCv5bkXb3_s70N8EQGwnbo18mWxttLG2Kkf6gBjrU9GlHt52R1S1qzEfulZFsTh-TznTQJMxLqSkeHQqOQlsmLFkzpWtYf-4eOK8wuhqxFIPm_R_dMDs3Io-4N3DTmHg5vYtgMASC5AzNrGc0YMYb8J9X9NuAPxNeR6CBrZXKysjiuFm366UAEXMvcUonzz_Q2btAriwhd5UPwh3H5Io0UfihXy3OdOryAuRVhoWzfvyizHnT7jC8WonIxh8M4Eieo_nKtxnbJ8u8xih-QXhjWvW4JIcbjSqPIQtleXqjah1NDIrJVl-IfArodClFxbDimHUtFGUoDYQpNQP2LvY5NyCqVABIHff8DwGiqQoGoxrkrAwSyqoFMndizkLxUWMe-Esod7OyU5xFj22PQ2OJJZ3SwuBfCzBaohCsGgw5cvyskl6Es_yIojFfI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه محمدرضا پهلوی:
"همیشه تلاش میشود ایرانِ دوران من با بهترین دموکراسی‌های جهان مقایسه شود، ایرادی هم به آن ندارم.
اما درباره اینها (ج.ا) که چنین قتل‌عام میکنند همه می‌گویند بگذارید درک‌شان کنیم، بالاخره اسلام وضع ویژه‌ای دارد، در حالیکه آنچه اینها (ج.ا) می‌کنند، در تناقض با اسلام است.
حتی در لیبرال‌ترین محافل، دوران من با بی‌نقص‌ترین دموکراسی‌ها قیاس می‌شود اما به اینها که می‌رسد می‌گویند بگذارید درک‌شان کنیم، اجازه دهید با آنها دیالوگ برقرار کنیم.
این چیزی است که برای من قابل درک نیست."
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72735" target="_blank">📅 19:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72734">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=dzaEd6sJjHwxL2igRshzCIrA-QRBK2TSSUvJ0I34XLvc-c088hSj-s9GkpMJomjx75hj2kRqGJb_tPmsYjCXyh3lzt6cc8MPJ1nS3nPHhktHCusxmcu86bJocOJsQtnbEoDcjLaAOxRV4GV7WwYJ7WBrwdHaD1IUPKs0UsTMfuC8UYQ7h7VS43oVR58xQA5ELc8g29vevHqxHiWm_p8mcJEg-TiCDcAZas513TZgylQJkJJXxzk5mE1obAnwx4ZCulGnfHkKXtgNN1264bKz9_1hlGMEcH7xrQW2pecXAyiChiyb40cWJAoEL_ehEQgpD2aBNKW_j51Z-DhjuSLD_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe642fca6.mp4?token=dzaEd6sJjHwxL2igRshzCIrA-QRBK2TSSUvJ0I34XLvc-c088hSj-s9GkpMJomjx75hj2kRqGJb_tPmsYjCXyh3lzt6cc8MPJ1nS3nPHhktHCusxmcu86bJocOJsQtnbEoDcjLaAOxRV4GV7WwYJ7WBrwdHaD1IUPKs0UsTMfuC8UYQ7h7VS43oVR58xQA5ELc8g29vevHqxHiWm_p8mcJEg-TiCDcAZas513TZgylQJkJJXxzk5mE1obAnwx4ZCulGnfHkKXtgNN1264bKz9_1hlGMEcH7xrQW2pecXAyiChiyb40cWJAoEL_ehEQgpD2aBNKW_j51Z-DhjuSLD_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های عربستان سعودی مقر نیروهای خودی را بعد از اینکه به تصرف حوثی ها درآمد، در تعز یمن بمباران کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72734" target="_blank">📅 18:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72733">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioOVFR4oIh2Z6FDi2MALAjxvOzwhNyCMkYu0DL5tRG7hqO7jcJczOd0lvK_WO2RKTi7AuoTMOTdVK1h8EtUV9X022-39gTAkhymTRKmFszPR4A9WPeKwgeakJ7xr6t8bJTVtOO0EJDM2wUtswN-sDwqzdvuWX24r9MVZRqOq6lsjEDVpdKcrfv60N94pvyYmU0waQo3bEi8sfd0Mo6Z338luETVj4KLaou9aF7LqAm1locUZYB3N2VV1l3mBbxbZM1XpBitrBjt1U19d0nbChGpW0lywn9HLcc4F9tbjn-Fu3zesu-T2a8cv7INJkVmI6AWOfY640qygnSZmlHhLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده با ارائه کمک‌های اطلاعاتی و پشتیبانی در تعیین اهداف، از عملیات تهاجمی تحت حمایت عربستان علیه حوثی‌ها پشتیبانی می‌کند، اما به‌طور مستقیم در نبرد مشارکت ندارد.
شاهزاده خالد بن سلمان، وزیر دفاع عربستان، از پیت هگسث، وزیر دفاع آمریکا، درخواست انجام حملات هوایی کرد؛ اما مقامات آمریکایی اعلام کردند که واشنگتن فعلاً قصد انجام «اقدام نظامی مستقیم» (عملیات کینتیک) را ندارد.
گزارش‌ها حاکی از آن است که فرماندهی مرکزی ایالات متحده (سنتکام) با انجام این حملات مخالف بوده و یمن را عاملی می‌داند که تمرکز آمریکا بر ایران را منحرف می‌کند.
@News_Hut
| Axios</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72733" target="_blank">📅 18:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72732">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=secMRSqYyO-_WZslxVglED7yy52TcPTYQssC4bbyQ_pYOpYSSEnDKyRNkGpU9ZCJvAi_M78kM0nhXeNlifHLrv3mvGVKE8CULF5z4E8n2Q1JEwXkPAtjSnJaarybL44AqLzCYkAcdGWq4kPDV9dMP4H4EzebunvTN4XUb28gWq7cp5kVpHbacL1TPQJmDySdZ_9G4geEQaMdGuFQXkVhMsDUavWv4uLWklg_bvDtW_bFSnVTRje3tjYn7KciS5I-K61JmcvQ4kYjImZOgj1pJh3DffUxLIWbhYM-_VA0HTRsChj30r_-blh-SjBoRKwhHBxTNvAdM5Gs3S8_AKG4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9ee58a69b.mp4?token=secMRSqYyO-_WZslxVglED7yy52TcPTYQssC4bbyQ_pYOpYSSEnDKyRNkGpU9ZCJvAi_M78kM0nhXeNlifHLrv3mvGVKE8CULF5z4E8n2Q1JEwXkPAtjSnJaarybL44AqLzCYkAcdGWq4kPDV9dMP4H4EzebunvTN4XUb28gWq7cp5kVpHbacL1TPQJmDySdZ_9G4geEQaMdGuFQXkVhMsDUavWv4uLWklg_bvDtW_bFSnVTRje3tjYn7KciS5I-K61JmcvQ4kYjImZOgj1pJh3DffUxLIWbhYM-_VA0HTRsChj30r_-blh-SjBoRKwhHBxTNvAdM5Gs3S8_AKG4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش:
در جریان این جنگ به این نتیجه رسیدیم که قطعاً باید برد موشک‌های خود را به ۱۰۰۰ کیلومتر افزایش دهیم، زیرا دشمن در حال حاضر در فاصله‌ای دورتر از سواحل ما مستقر است.
اکنون در این مسیر گام برداشته‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72732" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72731">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72731" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72731" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72730">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFPkiklkQNX-AJMjTPbDEsWSQgnzU2Ki8J49c_vBE9ubu6J8622LLB9Yj8AKgY8Lf4gl8juqE0aiGE0zzk6qnxxfif24BkNoQzkBVLB-gOwIlugj7afx1Hz0tZ-3GTLelmgDQxm9R3VH1FqtMfLv5Dox9xrj17Jk3XIn9jkHtCvz5HUchzIyl8fCgMvRcXIIGUaTB8hmbXnOXvNRHmXon2XUF9HMNN16YMNi_ZS3CRlwDP1gfT0SrJuY2e3enroTRBwXJ63WxI4U4Ic1OC6cDkfpAOGiH1my7yOaDy-i0PO-xmmpQUFcrPYAThnRj3QOhkDRPzBj8VviU_sph6ZHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز نروژ
🆚
پرتغال را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
نروژ: ۲ برد، ۳ شکست و ۸ گل زده
پرتغال: ۴ برد، ۱ شکست و ۹ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72730" target="_blank">📅 18:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72727">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0lowcLc7laFp4ZpNLVQyb9rJw1_Bn4YO24TW2CtErGz99YELNEjkbz-YcFGNWLJgXZI7U0ynHMMWw_PonBJ1m4TjQzd8T6NYTODQT95yXYca17bIrKJIvlJRNpI2BStg1e81Nt8mIE3REMaJ3U-uX0JtP0arzCLMitwTE8m52JC3cGgwBO_G-CHX42BTbMdpDIw0Czs8OJ6AHzfKXniuPpIfGcSTuiIMVfpmyK6NjAaAQrGfL4eWKDcnyy6I42cEv7Ka_XOG4l0vSP76ur9qjeAnQ4SkzTViExXhf17I17Osh3fUcoCVyxSxTSQol5pK84D9DG840lAgRGqE2pZgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0214da517f.mp4?token=BgVmSMOZKWt5G5sdhSLSmZ5ZUVWuKpktsl0ipXo_nGz7_OE0vu7c4n1bI6L7ybCZ-1QxCj2k3smkdaGgUInnCKDLQpoICvqJW8e0k57noX1MHBleCgP4Dz-rkiYTETlpnmTzXjhLbvJ6mnmWcBkYlxYfm9eALniBEEu-MDQe2_pHU3rm1Gq6f9CafDNAvdXiHFo_om7vKsHp6brM5t-UMjYPH61rWqCO99t7KXDMA9nry4FSTkXCqx3ri4M3fX-D9QzHnUZGOyWMlz9QAuNYdd2DZ-pXIk-neI9REPzlX-FVRvZmOsW8baEmxCprT3Gg5RX351A-7ohq8yxDxN-Oog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0214da517f.mp4?token=BgVmSMOZKWt5G5sdhSLSmZ5ZUVWuKpktsl0ipXo_nGz7_OE0vu7c4n1bI6L7ybCZ-1QxCj2k3smkdaGgUInnCKDLQpoICvqJW8e0k57noX1MHBleCgP4Dz-rkiYTETlpnmTzXjhLbvJ6mnmWcBkYlxYfm9eALniBEEu-MDQe2_pHU3rm1Gq6f9CafDNAvdXiHFo_om7vKsHp6brM5t-UMjYPH61rWqCO99t7KXDMA9nry4FSTkXCqx3ri4M3fX-D9QzHnUZGOyWMlz9QAuNYdd2DZ-pXIk-neI9REPzlX-FVRvZmOsW8baEmxCprT3Gg5RX351A-7ohq8yxDxN-Oog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به نظر می‌رسد نیروهای انصارالله موفق شده‌اند کنترل منطقه «البرقانی» در شمال «الصفیه» و در محور جنوبی تعز را به دست بگیرند.
در ویدئویی که منتشر شده، نیروهای حوثی هنگام ورود به خانه «سلطان البرکانی»، رئیس پارلمان شورای رهبری ریاست‌جمهوری یمن (PLC)، و تصرف آن دیده می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72727" target="_blank">📅 17:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72726">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=M6gHFSNjivSSTt0BpYuWHkhNdfHdolKCaZc_v6MfdP--WAOeyghxTkQDI5H1FnXw-pc8yxGc0RIQ3LbUgnnB6RfMhImYmTcFhVBDHhIsbY_4TyvnEbyuUyPdCWGW6xZEBzKI92pfwMWcdM2TVTE4kIrITICuY3BDwgthp0oY99y3MMfh_yx7V8BUQbluRCNqpRDqVORI4FUtVX-IMZEFZjtwVDUgPZeRK_XuK0Q6bjNd-rKVjEyczcIYIryTrxpYluYC62PykF_R2lhUq4zrJYShe1ENqC9Pl5VvK_9ku9oTM_109fBsEuXVeBLTjPOEGj4-WWGhCQBSIF0bQ_xWPW3EAHcymPFCGc7MhfU-uHnvISdqqqyqShyykItqgu1IgAxSPjBlRTm8J0KFPboyjjpUXSctvl5UgFoTJHA3tJjNV_Jc9bYqI_Xjnk26TZelKm7TLBxKIAWRZqNZAHiu9gDvyMLU54-pmwTQYJ2mrBcD4w0YVOJPjyYuoM5xiNx7LN2FwZ9vFYdVO1wLsUiJ5-6DjvbbZge_cXRcDHpkMDmBpm4il0Gln1t8kec8I30FfBkT0ZZz1atgySh2fhxunA09P8mhVrvfoxIoy_WTdxkpZwxkq2XLXrXZSF1AnAVCeoydlov6_uQWvymnLivogVbFAEeO8n4sH9dSzXoP4b4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=M6gHFSNjivSSTt0BpYuWHkhNdfHdolKCaZc_v6MfdP--WAOeyghxTkQDI5H1FnXw-pc8yxGc0RIQ3LbUgnnB6RfMhImYmTcFhVBDHhIsbY_4TyvnEbyuUyPdCWGW6xZEBzKI92pfwMWcdM2TVTE4kIrITICuY3BDwgthp0oY99y3MMfh_yx7V8BUQbluRCNqpRDqVORI4FUtVX-IMZEFZjtwVDUgPZeRK_XuK0Q6bjNd-rKVjEyczcIYIryTrxpYluYC62PykF_R2lhUq4zrJYShe1ENqC9Pl5VvK_9ku9oTM_109fBsEuXVeBLTjPOEGj4-WWGhCQBSIF0bQ_xWPW3EAHcymPFCGc7MhfU-uHnvISdqqqyqShyykItqgu1IgAxSPjBlRTm8J0KFPboyjjpUXSctvl5UgFoTJHA3tJjNV_Jc9bYqI_Xjnk26TZelKm7TLBxKIAWRZqNZAHiu9gDvyMLU54-pmwTQYJ2mrBcD4w0YVOJPjyYuoM5xiNx7LN2FwZ9vFYdVO1wLsUiJ5-6DjvbbZge_cXRcDHpkMDmBpm4il0Gln1t8kec8I30FfBkT0ZZz1atgySh2fhxunA09P8mhVrvfoxIoy_WTdxkpZwxkq2XLXrXZSF1AnAVCeoydlov6_uQWvymnLivogVbFAEeO8n4sH9dSzXoP4b4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛رشاد العلیمی، رئیس «شورای رهبری ریاست‌جمهوری» (PLC) یمن که مورد حمایت عربستان سعودی است، از آغاز عملیات نظامی تمام‌عیار در تمامی جبهه‌ها برای بازپس‌گیری مناطق تحت کنترل حوثی‌ها (انصارالله) و احیای حاکمیت این شورا در سراسر کشور خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72726" target="_blank">📅 17:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72725">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=oBw1wJt2jA79jUDWlU54_vz9zqcD-Ai2PdgILSbTj_6q45A9ngAHopC9HUe5L7c9JNzmi8mrfGwRssaTEImo-5LZiggAwss6RaXrzyeKNjOvUWHfgKl4UwZbkWu0pRCJPtDLOtA4yJGNWlf3aLsO51Xaj1uK4yhn8abdY_u85Ht-z_yarOpT4CHf30fj35wzSkpFUVaAraZe_wjDkbCXQTwjWaNTl8zvemXgaVYF0De8Z7uhxRzUtKgg7gc0wZCvjeHWOMx9zsuk_9jMExVHN6UACjGj5v5KtVobAe7xraA2VQnl7-FfVlmD4MqiZ8wAfIT0kaVjfN5Dm3_XwlREwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05733ed2f5.mp4?token=oBw1wJt2jA79jUDWlU54_vz9zqcD-Ai2PdgILSbTj_6q45A9ngAHopC9HUe5L7c9JNzmi8mrfGwRssaTEImo-5LZiggAwss6RaXrzyeKNjOvUWHfgKl4UwZbkWu0pRCJPtDLOtA4yJGNWlf3aLsO51Xaj1uK4yhn8abdY_u85Ht-z_yarOpT4CHf30fj35wzSkpFUVaAraZe_wjDkbCXQTwjWaNTl8zvemXgaVYF0De8Z7uhxRzUtKgg7gc0wZCvjeHWOMx9zsuk_9jMExVHN6UACjGj5v5KtVobAe7xraA2VQnl7-FfVlmD4MqiZ8wAfIT0kaVjfN5Dm3_XwlREwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پای رپر ها هم به تجمعات شبانه باز شده:
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72725" target="_blank">📅 17:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72724">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=G_W7vfZaaOKoUdrMUtGS-74z8XsumFozvGzSsq5j3fTRPaQkpcW3ItI6ilyPyf4_LeQ8EQD-aO8g9wXbYLAF8a9iATJsjUf6zGt1yS7Mpf2dmWw6RbUSZrHYx9JXTisM-nYn-HcVinJbOIAfJbOUOUFT0zyok8BLJB_NJAC1arsuZw6NBCKKbjPwFBplYRcmwcuyl_zUlYEQlYCqqLLn-9iBWjM7xjWtCBNxwOY7BltmQmLxCVKtsUN9AhLJpSGuNk-FuPp1X_CkgSCOapxooC67BCJLPV2rx8j6mnMkqHejvLI_nexdLPJQYZHpaqmfidOJdJQE59Z2bvpuxy1KiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f15ab8539d.mp4?token=G_W7vfZaaOKoUdrMUtGS-74z8XsumFozvGzSsq5j3fTRPaQkpcW3ItI6ilyPyf4_LeQ8EQD-aO8g9wXbYLAF8a9iATJsjUf6zGt1yS7Mpf2dmWw6RbUSZrHYx9JXTisM-nYn-HcVinJbOIAfJbOUOUFT0zyok8BLJB_NJAC1arsuZw6NBCKKbjPwFBplYRcmwcuyl_zUlYEQlYCqqLLn-9iBWjM7xjWtCBNxwOY7BltmQmLxCVKtsUN9AhLJpSGuNk-FuPp1X_CkgSCOapxooC67BCJLPV2rx8j6mnMkqHejvLI_nexdLPJQYZHpaqmfidOJdJQE59Z2bvpuxy1KiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زنه داشت از حس و حالِ ناراحت پسرش تو روز اول مهر فیلم می‌گرفت که یهو یه مرده اومد و این شاهکار رو گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72724" target="_blank">📅 16:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72723">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=sI4gF1Y3TQkoefHzZYoLuyLR99IR7vpNMi12g7rEtE7MP_6biSlbKSBp0l6YvzOFRRnZn62C-P49dIh6cleiEsJBus0H6id3_MmCYHvayeY3sNI17k_sI9UsVvAI_soY19M-Iem1tIyGJosUY-qiBNQU_o30i1BVIuXyXURn2NJ826ES7HAm6xXZ34thdyiCvcS1s61-qgngopNJSWN0agH2DAWA9bFVIFeWjWnl4byrK4ytxcFleu7NVRU4lFlSvYCbYV27XKTJ7HQ24u9GCs7N0QKi_jeg-VsBlwJ6VzqpGvkZ3b8HB1H9ZXG3-g-zGEzgwCUDPBCTbD4NalUkWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5caffe71ff.mp4?token=sI4gF1Y3TQkoefHzZYoLuyLR99IR7vpNMi12g7rEtE7MP_6biSlbKSBp0l6YvzOFRRnZn62C-P49dIh6cleiEsJBus0H6id3_MmCYHvayeY3sNI17k_sI9UsVvAI_soY19M-Iem1tIyGJosUY-qiBNQU_o30i1BVIuXyXURn2NJ826ES7HAm6xXZ34thdyiCvcS1s61-qgngopNJSWN0agH2DAWA9bFVIFeWjWnl4byrK4ytxcFleu7NVRU4lFlSvYCbYV27XKTJ7HQ24u9GCs7N0QKi_jeg-VsBlwJ6VzqpGvkZ3b8HB1H9ZXG3-g-zGEzgwCUDPBCTbD4NalUkWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو مکزیک  یه گزارشگر داشت از وضعیت خرابیِ کنار جاده گزارش تهیه میکرد که همون لحظه یه ماشین لیز میخوره و تصمیم میگیره گزارشگر و فیلمبردار رو با دیوار یکی کنه :
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72723" target="_blank">📅 15:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72722">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=bmmjvrQWRkst5VbVpd72nwUpbqSWLwU8DUtexHFnArHGIfmCTkMEAxdyWwwThuhhZqHEohum-Wdq1Q5kdBQCMk6fqdcx8K7v6FkIt4PaYs_qK4GY0HvzEp6X0oAuREjQ6sibN94SXC0sNRB37nTYUirZlOtluETi1nIENS-DJgSkB9erZKArECTtQM8blazscyreM81PW5nWhMqzQid0LOOTREuLpeVW4kt2_FIX-sfsFb3_yzrNylolxhDhT6h5v4kbexnopTIUiaWbs1imIbsr4wlc9h3SkacUbZtpQoxyyJUxGioBGLoBRxhtLU8kiXOxH7pbjgaSXTzImbWCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf8cf90e0c.mp4?token=bmmjvrQWRkst5VbVpd72nwUpbqSWLwU8DUtexHFnArHGIfmCTkMEAxdyWwwThuhhZqHEohum-Wdq1Q5kdBQCMk6fqdcx8K7v6FkIt4PaYs_qK4GY0HvzEp6X0oAuREjQ6sibN94SXC0sNRB37nTYUirZlOtluETi1nIENS-DJgSkB9erZKArECTtQM8blazscyreM81PW5nWhMqzQid0LOOTREuLpeVW4kt2_FIX-sfsFb3_yzrNylolxhDhT6h5v4kbexnopTIUiaWbs1imIbsr4wlc9h3SkacUbZtpQoxyyJUxGioBGLoBRxhtLU8kiXOxH7pbjgaSXTzImbWCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فریادهای مهدی کوچک‌زاده نماینده مجلس بر سر همتی رئیس بانک مرکزی؛
کوچک‌زاده:
مملکت را دارند به آمریکا میفروشند.
«به خدا اگر از جهنم به خاطر کوتاهی‌هایی که در حق شما مردم کردم نمی‌ترسیدم، امروز خودم را جلوی بانک مرکزی آتش می‌زدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72722" target="_blank">📅 15:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72721">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d26538e463.mp4?token=gA3xVN2ZlIJcJk6IpTGVeiVcIEZtEfLktIiqpHJuUfKspkrbrnqU4KS_B2pGrhde3_FoxLA53VEvR0jDcp-e2s1NpTePjLnFdw7XOpuKudPP0MwM-XO_m4N8uE7bpEVaKUjQiKlXgVKVo1Sfiv7o1urHk_eNB3v_Uo0CfcDb_5gI0CJCoS92wpDid9zCaATR_Bbcj0N0kaDBapf_VXB4ZxwQp46FK2hYD_XZJPSraZbA6siLxV2X_E8wJzi06vkX6zaLGkaeP-SHhmFz0Lqbsqvm3mpzet1ASmG2c3o3l8oWs0MGb-R6S9RGhfjklpwjjRhKCGX9NQTQxyZooVL-zmzlyVyY9yq3Zhusi4vli33-NRjrJeT3xvhflL-ZDu5bhPC6rPyRZpS5qA7t0_PmvvZz2Nr5LK5pLBs9JxKfpkPrZNe9RPZZ4eEet2ISuXA6ecPDIzQC8AyAPlE6aQhysorEWaXMTDkuZMv1FlS2Uo-uQ1BoiWmDKOEcqZp1F3u69GO1sxn_vJbNopZb5ieoobH4pypHz17z0lvyZ9jve3k_8DmX0hYzIEMOoF23JGl30NEBA_g9__Yc26WlsNzWk57H85GZKoZdzBG43xmVNcRMZMKpFO7WtvK91qPmLLs_EmTaaQUZuwlPnws35hzjJekM0vT0KypmlFEGJqlzMlI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d26538e463.mp4?token=gA3xVN2ZlIJcJk6IpTGVeiVcIEZtEfLktIiqpHJuUfKspkrbrnqU4KS_B2pGrhde3_FoxLA53VEvR0jDcp-e2s1NpTePjLnFdw7XOpuKudPP0MwM-XO_m4N8uE7bpEVaKUjQiKlXgVKVo1Sfiv7o1urHk_eNB3v_Uo0CfcDb_5gI0CJCoS92wpDid9zCaATR_Bbcj0N0kaDBapf_VXB4ZxwQp46FK2hYD_XZJPSraZbA6siLxV2X_E8wJzi06vkX6zaLGkaeP-SHhmFz0Lqbsqvm3mpzet1ASmG2c3o3l8oWs0MGb-R6S9RGhfjklpwjjRhKCGX9NQTQxyZooVL-zmzlyVyY9yq3Zhusi4vli33-NRjrJeT3xvhflL-ZDu5bhPC6rPyRZpS5qA7t0_PmvvZz2Nr5LK5pLBs9JxKfpkPrZNe9RPZZ4eEet2ISuXA6ecPDIzQC8AyAPlE6aQhysorEWaXMTDkuZMv1FlS2Uo-uQ1BoiWmDKOEcqZp1F3u69GO1sxn_vJbNopZb5ieoobH4pypHz17z0lvyZ9jve3k_8DmX0hYzIEMOoF23JGl30NEBA_g9__Yc26WlsNzWk57H85GZKoZdzBG43xmVNcRMZMKpFO7WtvK91qPmLLs_EmTaaQUZuwlPnws35hzjJekM0vT0KypmlFEGJqlzMlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
من با کیم جونگ‌اون، رهبر کره شمالی، رابطه بسیار خوبی دارم.
وقتی طرف مقابل ۱۱۲ موشک هسته‌ای در اختیار دارد، خوب است که با هم کنار بیاییم.
اما تفاوت اینجاست: ایران هرگز موشک هسته‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72721" target="_blank">📅 14:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72720">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=uaPOasrpM0yVZnZEZ9SgCqAiWVQ57a7zCwCYax6wXdFS4F7qdDD0OTB58_LFK4nzNNOfbjRewQzmzB4vTXuMfcGrsxPOEsDdePG-ubNdK2tAIuerJlG6kSnNcSIcfGg7A9KNmTSFCu35-55jdxfRNXPHaEKlrtWDZw3nCNg-eM0_r6K1IDFsIPgvTej92lugjFkg8lfuRTSnOO3fptZGToPi3No90Q9vkVXbzv_5JOl82gFtQyUWK-sLgomJmbaqhbn2zsI0tLvjnxafa8BMYu5mqNvZL0giMx2tXwNVAVfjMYb6nSZ0p8-pcmWb3o0ysFwPpx45uH9BE-jwtb2q_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe93c3478.mp4?token=uaPOasrpM0yVZnZEZ9SgCqAiWVQ57a7zCwCYax6wXdFS4F7qdDD0OTB58_LFK4nzNNOfbjRewQzmzB4vTXuMfcGrsxPOEsDdePG-ubNdK2tAIuerJlG6kSnNcSIcfGg7A9KNmTSFCu35-55jdxfRNXPHaEKlrtWDZw3nCNg-eM0_r6K1IDFsIPgvTej92lugjFkg8lfuRTSnOO3fptZGToPi3No90Q9vkVXbzv_5JOl82gFtQyUWK-sLgomJmbaqhbn2zsI0tLvjnxafa8BMYu5mqNvZL0giMx2tXwNVAVfjMYb6nSZ0p8-pcmWb3o0ysFwPpx45uH9BE-jwtb2q_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی :
بحث‌ها پیرامون خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) در محافل سیاسی ایران بسیار جدی است و وزارت امور خارجه به تصمیم مراجع ذی‌صلاح پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72720" target="_blank">📅 14:43 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
