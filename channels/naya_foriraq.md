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
<img src="https://cdn4.telesco.pe/file/Ur25_Q7cGH1fH98uesEHtWqvITwn_ZSFBmx4flXlOVQKI2XknxuF1lt2pByp4xL15ZQgxy8nyXxxmZnEk7qDBnK4BCzHKSQanFBubfzZKtem_PTrq9weTvuehU2DDVZIVQ2dQqxZy-TtTZSkRLBVaR0qJp5BDx---nnu7T04MNzhSABhtD-0voz_K2tsL-LFk1UG6PtVdgM864P66QOvtCSi2-f9_Gc9RQTG5BEIvG0g_G03VzFS4bIgPqviVwhGnjueBPAtBrlJs75D3LlASRVVQKx5sk495F9V7z0i6e8FiAwLYlfVc7tGQDwOS9UxFEobRy9K1FK-B1p1JtNFAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 07:33:24</div>
<hr>

<div class="tg-post" id="msg-80163">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">اصوات انفجارات تهز الكويت الان</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/naya_foriraq/80163" target="_blank">📅 07:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80162">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c81df6c5.mp4?token=LIS8vEIKaIwknKG4qfnVewZAIAIZ4RsFFpJlSq243nguB6B55N9KUajRkYEgtBsZIvpYdpWsrtEhb2DaS-uhQSZ7mLPuvc2UJ8S_kgW1lB0fMcimaii875LNrmKDJ-77EnqPHC2zGrQpuotFbZJA0f_j1LoirPuHdHbi7iTP7xtCFseSHXHVn3GlOqkbAqLQ_QIpvo8oNdWaGKRgsOUXncc1W56uKjFG8xdBZLYGZTXciNfLti6czqu2R_GYA9QtxHH0wMiwQTKicsHXQR8Avri1pIWF5tMwhmWBk0XQWUn8ygH1N-siQ0dD78S7xgBx0JXSJrXtAT44soC3jUjzVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c81df6c5.mp4?token=LIS8vEIKaIwknKG4qfnVewZAIAIZ4RsFFpJlSq243nguB6B55N9KUajRkYEgtBsZIvpYdpWsrtEhb2DaS-uhQSZ7mLPuvc2UJ8S_kgW1lB0fMcimaii875LNrmKDJ-77EnqPHC2zGrQpuotFbZJA0f_j1LoirPuHdHbi7iTP7xtCFseSHXHVn3GlOqkbAqLQ_QIpvo8oNdWaGKRgsOUXncc1W56uKjFG8xdBZLYGZTXciNfLti6czqu2R_GYA9QtxHH0wMiwQTKicsHXQR8Avri1pIWF5tMwhmWBk0XQWUn8ygH1N-siQ0dD78S7xgBx0JXSJrXtAT44soC3jUjzVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز البحرين الان</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/naya_foriraq/80162" target="_blank">📅 07:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80161">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انفجارات تهز البحرين الان</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/naya_foriraq/80161" target="_blank">📅 07:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80160">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">استمرار خدمات الانترنيت في العراق على الرغم من تلويح وزارة الاتصالات بقطع خدمة الإنترنت من المصدر مؤقتاً خلال أوقات الإمتحانات الوزارية من الساعة 6:00 صباحاً إلى 7:30 صباحاً،</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/80160" target="_blank">📅 06:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80159">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58da81163d.mp4?token=uF4aZEw8lHOK8EXRwAYa1oMVeYA9oOtZDAQCMf0NBw1KGvSggdGpsTDzE6cDetXJQXkm_yKTxxz7mz3sKn5bA0sLARk-x-dQb0bieuiTc2p6QSGk20FrHdwTbMP1gHrqW6Xl-y-Hr63kTLkbnUbfhPAo0rHWLeXLs-LVb0cfLZQQJpeKoZ4da413roL-BuYF9-ZJlGoxQ7jQqFO72QRHHBSof_AoIVQux400Kok_gdPjauz5GFLA-n5Gm21uP0Xg2y7pfggJl2T8f21CFWUjPpuYvjVe9AUJmrpj0TZTUCptVHmGpzP1psfDGQ-gxcXugNGzKoEa9dKRhqUzxHs9tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58da81163d.mp4?token=uF4aZEw8lHOK8EXRwAYa1oMVeYA9oOtZDAQCMf0NBw1KGvSggdGpsTDzE6cDetXJQXkm_yKTxxz7mz3sKn5bA0sLARk-x-dQb0bieuiTc2p6QSGk20FrHdwTbMP1gHrqW6Xl-y-Hr63kTLkbnUbfhPAo0rHWLeXLs-LVb0cfLZQQJpeKoZ4da413roL-BuYF9-ZJlGoxQ7jQqFO72QRHHBSof_AoIVQux400Kok_gdPjauz5GFLA-n5Gm21uP0Xg2y7pfggJl2T8f21CFWUjPpuYvjVe9AUJmrpj0TZTUCptVHmGpzP1psfDGQ-gxcXugNGzKoEa9dKRhqUzxHs9tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تحركات القوات الأمنية في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80159" target="_blank">📅 06:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80158">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5o9Xgm02o2GAL5NWLYM4MMpxoR5XtubIAlyIxbSqa0OcHd1sWeBGjPfW_w0bwqvQZr-ghLJ5hpKgmPJrdf4hl-J-OHpr7uuYd8uYzXxV5-pH10XPnnqQ0KqYUaFTFVCKnjnjV_2usgY0aEyhD_-Ogl98cQ6R0C1SVAgIEDuJs0EO6UFbFtzzOXg-x8gauokog-45YygJn7AEJo1vbjgkJvGCTw18GknFA3xKm83JfB6QyeK20-xV_F8mFO7Am3K6EzHFKCB9iSz1TS0jLzr4kS5uRPa6zh3igLyZJM1O-88DdKfzqG_Js0qxSgcKRZ-TTsP5GQo5xQi2iiH5FJZRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلل حركة السير بالمنطقة الخضراء</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/80158" target="_blank">📅 06:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80157">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">العملية الامنية لا تزال مستمرة حتى اللحظة .. مع انتشار لأفواج مكافحة الارهاب والفرقة الخاصة وارتفاع عدد المعتقلين إلى ٨ أشخاص بأوامر قضائية</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80157" target="_blank">📅 06:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80156">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00df836d16.mp4?token=bvZ2-TrUScQVaQ6W7UxeKDkuIR332tSiSZsrdTIbJ88Q2hwwwMTn7lAbzURutpLARk8fm4ckBw6UWYB1H_YDxw-AXA0_2rVbjxNGkJ3p5l6lQ7oy9S79cHGVNvPiCddXSwQOf3SNwZBWVphWjiz6erT0UtTR1ZJ4T--m0rKS-rDzoBuizFNNFdhsSSYnWSJglTr66VehT4MmgVZAsfFGPC25OvCPPIPgSSO9-spj188X9eeu7EZVrIpnc9x1P8Ioge74n8yDL3slzPs5EUPiOm--QqcZIE-vr3tGpH2-NSWYhYW-PvNANfGWlNyjisgmCrXpYmM0dFPNxJ-2sWnOKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00df836d16.mp4?token=bvZ2-TrUScQVaQ6W7UxeKDkuIR332tSiSZsrdTIbJ88Q2hwwwMTn7lAbzURutpLARk8fm4ckBw6UWYB1H_YDxw-AXA0_2rVbjxNGkJ3p5l6lQ7oy9S79cHGVNvPiCddXSwQOf3SNwZBWVphWjiz6erT0UtTR1ZJ4T--m0rKS-rDzoBuizFNNFdhsSSYnWSJglTr66VehT4MmgVZAsfFGPC25OvCPPIPgSSO9-spj188X9eeu7EZVrIpnc9x1P8Ioge74n8yDL3slzPs5EUPiOm--QqcZIE-vr3tGpH2-NSWYhYW-PvNANfGWlNyjisgmCrXpYmM0dFPNxJ-2sWnOKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعادة افتتاح بوابات المنطقة الخضراء وسط العاصمة بغداد</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80156" target="_blank">📅 06:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80155">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/994fd7d7a3.mp4?token=uSaRj8NfBX4VvhbQ2thx135v3H06xlK0bUTScRfa-ys_N85QqtpoGmoUiqpm8KemPfXEl3MMJwJqoIa4hr5KdiHU1fpg23wX3VZBambldsNbVOyuMbVK8QNN5sbBHZJpcQ7zJy_2FlwAO6q3Gievo4OdNFHudIzO3vV3MpGHCxqQNT9ECQ5tcKVx-jGCSDUH6GAJjQQe48AzaUReOYlgHSjYvOblIGlbDKVslXbI1XRGysBTWtcgun2eh5nyMY5-jtg6tUT__JYU2HUwub9n1DcovluZ5YNhBSwlBfIr0VvosP2LwVKO1evlMrlrJvp_HjrgqHYQ6XwlPX_Rf3Y0SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/994fd7d7a3.mp4?token=uSaRj8NfBX4VvhbQ2thx135v3H06xlK0bUTScRfa-ys_N85QqtpoGmoUiqpm8KemPfXEl3MMJwJqoIa4hr5KdiHU1fpg23wX3VZBambldsNbVOyuMbVK8QNN5sbBHZJpcQ7zJy_2FlwAO6q3Gievo4OdNFHudIzO3vV3MpGHCxqQNT9ECQ5tcKVx-jGCSDUH6GAJjQQe48AzaUReOYlgHSjYvOblIGlbDKVslXbI1XRGysBTWtcgun2eh5nyMY5-jtg6tUT__JYU2HUwub9n1DcovluZ5YNhBSwlBfIr0VvosP2LwVKO1evlMrlrJvp_HjrgqHYQ6XwlPX_Rf3Y0SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجهة المنفذة للواجبات فجر اليوم " جهاز مكافحة الارهاب ، الفرقة الخاصة ، الفرقة المدرعة التاسعة جيش عراقي " ؛ بيان حكومي مرتقب عن العملية العسكرية</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80155" target="_blank">📅 06:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80154">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عودة الهدوء للمنطقة الخضراء وسط بغداد مع انتشار امني لجهاز مكافحة الارهاب بالمداخل والمخارج</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/80154" target="_blank">📅 06:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80153">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">عودة الهدوء للمنطقة الخضراء وسط بغداد مع انتشار امني لجهاز مكافحة الارهاب بالمداخل والمخارج</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80153" target="_blank">📅 05:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80152">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عودة الهدوء للمنطقة الخضراء وسط بغداد مع انتشار امني لجهاز مكافحة الارهاب بالمداخل والمخارج</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80152" target="_blank">📅 05:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80150">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سرقة سيارة نوع جكسارة تعود لضابط برتبة عقيد في وزارة الداخلية العراقية .</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80150" target="_blank">📅 05:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80149">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سيطرات مفاجئة وتدقيق على الأسماء في اغلب شوارع العاصمة بغداد .</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/80149" target="_blank">📅 05:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80148">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">قوات أمنية إضافية تنتشر في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/80148" target="_blank">📅 04:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80147">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇮🇷
توثيق للحظة إطلاق الصواريخ الإيرانية نحو قاعدة علي السالم الأمريكية في الكويت.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80147" target="_blank">📅 04:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80146">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b80a9e9cb.mp4?token=KJGP4The6HjAtdprw-r6mPDLODWSYOnZve9EPEGJ0omR39kgergvmZAPCnvRTCSpBPyhGflDgFYSxLmnCpKzynwELpyaftWxRAcuvJzbiWUyftFnBwcRJmZ8jHOqI3f3EJQ3p1xdkI4DDqrTmnURtIBrrwWoZ7iUMqAobbjrhNM_qMBEiyFOcYLRfv7OsrndkKwbhfFLC5az1gWUN7UOjy9tfXCWpByD14l9Ap-Bi8j4relnCm0IGIUqSYs5yLuLGY3eS8sWutUn1KsyrvSy4uK7UynY_6pNu4H7itQhzFzG9O9zaxFH6-tbKYbC2ips52ZZ5rbUheQtyfVb7xL5tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b80a9e9cb.mp4?token=KJGP4The6HjAtdprw-r6mPDLODWSYOnZve9EPEGJ0omR39kgergvmZAPCnvRTCSpBPyhGflDgFYSxLmnCpKzynwELpyaftWxRAcuvJzbiWUyftFnBwcRJmZ8jHOqI3f3EJQ3p1xdkI4DDqrTmnURtIBrrwWoZ7iUMqAobbjrhNM_qMBEiyFOcYLRfv7OsrndkKwbhfFLC5az1gWUN7UOjy9tfXCWpByD14l9Ap-Bi8j4relnCm0IGIUqSYs5yLuLGY3eS8sWutUn1KsyrvSy4uK7UynY_6pNu4H7itQhzFzG9O9zaxFH6-tbKYbC2ips52ZZ5rbUheQtyfVb7xL5tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إغلاق تام لبوابات المنطقة الخضراء وانتشار دبابات أبرامز بالتزامن مع حملة اعتقالات طالت عدد من السياسين بتهم قضائية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/80146" target="_blank">📅 04:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80145">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/911e440568.mp4?token=UTT6lTpWhV7VBjcqbegUPSLl71IncC-_rJBThX1O-UGk6uD63KW2SxlOrSkIgyyrtuid6zS-dgZ0Cw1fEBFID2KOZ9R9-AflJH_cZGpsW7QoXMz3X6_LsLUm8WomLzvMX3DguvEAu7Ivy4Z1MHXNuMqYZQFhQlUw7WjJIa3XSjlr-JwWA_CN9LemVi2oSHEHJq1krBiPWMUxkTv5HM9TRd1OZwWo0tBGcTd83Zu9q7IGYFm8Bd61EvvL7dEy3X-3qBdh9bxsicUG5SdgzycGcVkkjU8f-17fzO2GBfQ60fbcK8ZBkloVJXu4W4lLQBtWZzT0FQ6_LoPezwLyBWvQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/911e440568.mp4?token=UTT6lTpWhV7VBjcqbegUPSLl71IncC-_rJBThX1O-UGk6uD63KW2SxlOrSkIgyyrtuid6zS-dgZ0Cw1fEBFID2KOZ9R9-AflJH_cZGpsW7QoXMz3X6_LsLUm8WomLzvMX3DguvEAu7Ivy4Z1MHXNuMqYZQFhQlUw7WjJIa3XSjlr-JwWA_CN9LemVi2oSHEHJq1krBiPWMUxkTv5HM9TRd1OZwWo0tBGcTd83Zu9q7IGYFm8Bd61EvvL7dEy3X-3qBdh9bxsicUG5SdgzycGcVkkjU8f-17fzO2GBfQ60fbcK8ZBkloVJXu4W4lLQBtWZzT0FQ6_LoPezwLyBWvQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر خاص لنايا: اعتقال ٣ قيادات سياسية مهمة في المنطقة الخضراء بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/80145" target="_blank">📅 04:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80144">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/80144" target="_blank">📅 04:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80143">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a37338d56.mp4?token=RGEFxit2UZw_Bd6M3NVwq2Ikzs8OqeSt3nGDLLciCQ5I6oBWGlh5wY6S1c_TlzZAb_M9vHagZlrUOFHdZyR9TVC4vKy1cEGXK9ASzjP-zOFJ5F2adj99FzzpTekR9qPSTv_KWGwCwlduiJB6Ji9xpTod4Tj2h_uhhYzdU5c-eZGyTBKlkynrNQAC5ZCytD5UXgPyFsNrF_6WCTVVoamD6WHi_gtHQ4mjqBMTFKB0fjP9fVnXDLCpELsZNmlweXdwAEwX2u870tYXNmYCDRl65oQjYM2dF0AaRrTJOr-ZSiUMpIg7Hq7S1oRYTqnaogfb963xf6MDV6bKqqi-0Ja_Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a37338d56.mp4?token=RGEFxit2UZw_Bd6M3NVwq2Ikzs8OqeSt3nGDLLciCQ5I6oBWGlh5wY6S1c_TlzZAb_M9vHagZlrUOFHdZyR9TVC4vKy1cEGXK9ASzjP-zOFJ5F2adj99FzzpTekR9qPSTv_KWGwCwlduiJB6Ji9xpTod4Tj2h_uhhYzdU5c-eZGyTBKlkynrNQAC5ZCytD5UXgPyFsNrF_6WCTVVoamD6WHi_gtHQ4mjqBMTFKB0fjP9fVnXDLCpELsZNmlweXdwAEwX2u870tYXNmYCDRl65oQjYM2dF0AaRrTJOr-ZSiUMpIg7Hq7S1oRYTqnaogfb963xf6MDV6bKqqi-0Ja_Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تم استهداف قاعدة علي السالم في الكويت</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80143" target="_blank">📅 04:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80142">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
مصدر خاص لنايا: اعتقال ٣ قيادات سياسية مهمة في المنطقة الخضراء بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/80142" target="_blank">📅 04:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80141">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔻
مصدر خاص لنايا: اعتقال ٣ قيادات سياسية مهمة في المنطقة الخضراء بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80141" target="_blank">📅 04:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80140">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">توثيق أخر يظهر كثافة الإنتشار الأمني في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/80140" target="_blank">📅 04:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80139">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgecF8CdQqkhGeKojyMazcBEuMTkHPwSfXHWS53ER6E3FiVbL2dNE-gDLdaYLLcdsOP2xTnUIQXqllDay23r8T9drXslVFj1RxlBSWdKs_S2K0ExZ1vZQ4XztIiDTHQbVIui6VCxxJyrk5bjnbciHlpVUplReuRNS6n5Q1sP3UmpVUNb___uOHGLw_tcnLDO5b00xVL4Qg08b9QYkfxSWRWTSkJMTP685WBlI2VBd7zqpD4s6U1m7nB6Qu2I_GkqJUBQ1mYmUpQA-rj1i0c2KgMYsfWuTwTfLXg7vs1ji9kY3QMHmUOM--ZXKpaDOF2CUcY2GTkTnx4mK5sa46TezQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العلاقات العامة للحرس الثوري الإسلامي: أيها الشعب الكريم لجمهورية إيران الإسلامية؛  خلال عملية صاروخية وطائرات مسيرة مشتركة بين الساعة الثانية والثالثة فجر اليوم الأحد 28 يوليو، أطلق أبناؤكم البواسل في القوات البحرية والجوية للحرس الثوري صواريخ باليستية وطائرات…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/80139" target="_blank">📅 04:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80138">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99f860d0e2.mp4?token=ndpJZAUZMFf9VmKG4-us9JFd8lvStGllwdYHz_BqrcDzlYkxn4Aho_0fJqxiuDVCHqOF3DVS6YRADVGPCv2DBzoYoPrgM9dfvZwpxCr1rkxhDBUpoWK4lw6mpP8L7ieqdEzQ65a698y99N-IwMq6AtRX-rf7QJ25mAc340YVjh6oUio6CJfxLEACscXpTs9mZkr46Mp3kaj3OfQwuDCyATLp8qPyqZ4zXACb7SELXdlDy9bH5TjKMdbU2_xXJCr0fQhPLudf3JOFPT201pMvWTIjgbQadKn3bNI3Sxfqijcma6mLTd2A36lNg-OCvnIWCG1sTjz6Mik_8abYnOZuYAMsCGp3AroLxCLjr-JMhilONQPxV_hsy8bTjWoYJeVjy5HhC8wffHRXIy6cGmEqGmws4lndmSufeSCp9-OZIqbJYN_RM6ivI5uqj-Nb0Zzb-XMSdRrngE775g7PCj38T-A1dCw5HpZqikL9LaVILFU4sr6ZVo4v7fbRa_OA9I9ZP408nOi3QRopEyisTMa5UlIduXxWoBMaQ1XSRfR_1PNPOMzgkcZyBRWsLpSvHnOyqBGAb64h2QaUcnmILBJ74rBKcwRohRQoMm1F_W-ULHrKq9rzoOgOLjDwxCMj3y0X0ROQwf8o4euQqxQOX_YJYct6XGD-JzNalH9hsntikLs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99f860d0e2.mp4?token=ndpJZAUZMFf9VmKG4-us9JFd8lvStGllwdYHz_BqrcDzlYkxn4Aho_0fJqxiuDVCHqOF3DVS6YRADVGPCv2DBzoYoPrgM9dfvZwpxCr1rkxhDBUpoWK4lw6mpP8L7ieqdEzQ65a698y99N-IwMq6AtRX-rf7QJ25mAc340YVjh6oUio6CJfxLEACscXpTs9mZkr46Mp3kaj3OfQwuDCyATLp8qPyqZ4zXACb7SELXdlDy9bH5TjKMdbU2_xXJCr0fQhPLudf3JOFPT201pMvWTIjgbQadKn3bNI3Sxfqijcma6mLTd2A36lNg-OCvnIWCG1sTjz6Mik_8abYnOZuYAMsCGp3AroLxCLjr-JMhilONQPxV_hsy8bTjWoYJeVjy5HhC8wffHRXIy6cGmEqGmws4lndmSufeSCp9-OZIqbJYN_RM6ivI5uqj-Nb0Zzb-XMSdRrngE775g7PCj38T-A1dCw5HpZqikL9LaVILFU4sr6ZVo4v7fbRa_OA9I9ZP408nOi3QRopEyisTMa5UlIduXxWoBMaQ1XSRfR_1PNPOMzgkcZyBRWsLpSvHnOyqBGAb64h2QaUcnmILBJ74rBKcwRohRQoMm1F_W-ULHrKq9rzoOgOLjDwxCMj3y0X0ROQwf8o4euQqxQOX_YJYct6XGD-JzNalH9hsntikLs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قوات أمنية إضافية تنتشر في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/80138" target="_blank">📅 04:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80137">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/366e2bae2f.mp4?token=usS1gle-kk6ZSMPKCA2bYMTf52_pbrdxWgWHLyz-TVPpnodvu-ua0cfgiOuGx9tJ2mjKrOh9qvPKJRcnRTlPUv21CERBir581HppUOA2CnrVNPYTp9SRbEl9v66rGskFWcuPkQu7-R_sfG4tecyEEdvjeghynHSpb87AQkK7e8DbGP-Yi3fRYPWyFRmj1JjNLVm_CcFuxsfvT4IqnrOp_lPhiyPkgmjduYdx8PKoplMCIhuA8-snaLiedEOTm5cWNTUkiAau4KBrJu3UUhqsLJ5CXxIsr1nhEtGiRvG49B6U1Y3fi_igI8b09r7-li12F7UKlZm6A9A39dWRsI9RT4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/366e2bae2f.mp4?token=usS1gle-kk6ZSMPKCA2bYMTf52_pbrdxWgWHLyz-TVPpnodvu-ua0cfgiOuGx9tJ2mjKrOh9qvPKJRcnRTlPUv21CERBir581HppUOA2CnrVNPYTp9SRbEl9v66rGskFWcuPkQu7-R_sfG4tecyEEdvjeghynHSpb87AQkK7e8DbGP-Yi3fRYPWyFRmj1JjNLVm_CcFuxsfvT4IqnrOp_lPhiyPkgmjduYdx8PKoplMCIhuA8-snaLiedEOTm5cWNTUkiAau4KBrJu3UUhqsLJ5CXxIsr1nhEtGiRvG49B6U1Y3fi_igI8b09r7-li12F7UKlZm6A9A39dWRsI9RT4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أعلنت القيادة المركزية الأمريكية (CENTCOM) تنفيذ ضربات جديدة استهدفت مواقع عسكرية إيرانية، رداً على هجوم بطائرة مسيّرة استهدف ناقلة نفط قرب مضيق هرمز. وأكدت أن الضربات شملت أنظمة مراقبة واتصالات ودفاعات جوية ومخازن للمسيّرات، مشيرةً إلى استمرار حركة الملاحة…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/80137" target="_blank">📅 04:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80136">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الحرس الثوري الإيراني يتبنى الهجوم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80136" target="_blank">📅 04:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80135">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الحرس الثوري الإيراني يتبنى الهجوم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80135" target="_blank">📅 04:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80134">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تم استهداف قاعدة علي السالم في الكويت</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/80134" target="_blank">📅 03:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80133">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تم استهداف قاعدة علي السالم في الكويت</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/80133" target="_blank">📅 03:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80131">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EE3MRRNiFl4RrwZDJdLmISftWL0FEJTGl8tmytlml2JW1VfGXoTTOkj8-d5GpoKAooDpqWl-LXsfDNduUcZdUKO33_1tCDVafz6UkwLayeJ0ccL5qMsCFjKEIL8wByDjx95alZJDKaif4KXx4SANj-9DhNiIFsSfWFizWeyJOXtAVw3yIp2wdKhNVeXd_iNBR_ozMDzWCtSEX0huhh-6TysiHd2G_9Er5-RDR_5uJiVbHvwPDh5_gexKUbMEZ-peJIU-UVoTR1BMtEv-ak07eTxvzqdPx0uu64kqlq46WJ6SFj6Q0AqcZWF2zuirhPj0CBKnc22SlqrBNTGLnCRwQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iRhl0gGp55xbplU_S7usqPWbHXFXDWbsVNG20OvdorTJY6sVgbGw7znDJhuejXPUkHKSNx6LSwRvdwra2cCT0SjKWk727zpC8gdGiElo_JHoesBYweLJFELEt6dgq6mx-3ihcc7lRAJLTbc9ktI-KHDeVp29uZHuwdAxwdk5qGehUOCM4P5s1i2pQmPP28zHuznDFSR5WTeb6H6uGf5yhLYFRFoDbO8SrueP3y22XXx_yQYPdhxEgAZ5Ob8zVW6dvCQgJgJwDat7lIED4VIfhdY-KpIx4x-8M18ERbKayhMlnbCtKL0NROec-27O3Sew2q2AGVt-obCjdYJpfciI7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صافرات الإنذار تدوي بإستمرار في الكويت عقب هجوم صاروخي وبالطائرات المسيرة</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/80131" target="_blank">📅 03:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80130">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">موجة صاروخية جديدة تنطلق نحو القواعد الأمريكية</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/80130" target="_blank">📅 03:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80129">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/80129" target="_blank">📅 03:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80128">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80128" target="_blank">📅 03:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80127">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71aa5ae7b8.mp4?token=a6_PhDMupf-Ae1VNZCCGBLkysqsDQtMND2g6_bSPU8inFG6hlCO_uhNnJmOjN0Sx-s7Els_y8NepGVRn5CfNg2zHYXfKA-gR3NExODM6GJwBY9In1TrzCUDZRhy51n1W3T2vQJdujFe-CuS5YxxwY3OLbnkVWLYBNNLJzcFUAvykiScngsCS0hy5mKdXgt9VEAKE0cbUVJfmM4d6QZmelSdlc_I99e7gPHsQnlnVye4-JHaU0-IbKsWH8pNP4th0Xq-0aSK93gYK0DvFqYkr_sTPc6_wWDy0SBQCv8irhCYL7aWD0Yu6m2RyISfK3Y37HeWvJbU2p7YxIlOpSz9-Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71aa5ae7b8.mp4?token=a6_PhDMupf-Ae1VNZCCGBLkysqsDQtMND2g6_bSPU8inFG6hlCO_uhNnJmOjN0Sx-s7Els_y8NepGVRn5CfNg2zHYXfKA-gR3NExODM6GJwBY9In1TrzCUDZRhy51n1W3T2vQJdujFe-CuS5YxxwY3OLbnkVWLYBNNLJzcFUAvykiScngsCS0hy5mKdXgt9VEAKE0cbUVJfmM4d6QZmelSdlc_I99e7gPHsQnlnVye4-JHaU0-IbKsWH8pNP4th0Xq-0aSK93gYK0DvFqYkr_sTPc6_wWDy0SBQCv8irhCYL7aWD0Yu6m2RyISfK3Y37HeWvJbU2p7YxIlOpSz9-Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/80127" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80126">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f975085a0.mp4?token=F6pjvsXkvq4cYF_KXJua0USjPlgoe-kQIEQAcJJJ9byzvMRcwok1hcjaEzLJWVz1UXu-__bm_0UpDMgDpaxoMJIvGChq660fVps7cPLPm39GTao5DPI6OHphLRO_arTtEueZCyWMuxPpqsVSxMXCsnbUQK_V01tY6PzXe2P4Yrb0ocrLXNUdglD0w7srYcgtzFFvn8x5RDYFzCYp9JBTgP_8gJQLu9dFNrTTpyiXGUyHp26OiOPankMgjIPl5Vl5ZhAnX-oSA3NTB_Ezg8s7ZYOQ976O-Xa0OERV1HoMm5u82H6OQcud_WyMGMmzk4vjkDIM2WInk_Hpt4nYVrx9ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f975085a0.mp4?token=F6pjvsXkvq4cYF_KXJua0USjPlgoe-kQIEQAcJJJ9byzvMRcwok1hcjaEzLJWVz1UXu-__bm_0UpDMgDpaxoMJIvGChq660fVps7cPLPm39GTao5DPI6OHphLRO_arTtEueZCyWMuxPpqsVSxMXCsnbUQK_V01tY6PzXe2P4Yrb0ocrLXNUdglD0w7srYcgtzFFvn8x5RDYFzCYp9JBTgP_8gJQLu9dFNrTTpyiXGUyHp26OiOPankMgjIPl5Vl5ZhAnX-oSA3NTB_Ezg8s7ZYOQ976O-Xa0OERV1HoMm5u82H6OQcud_WyMGMmzk4vjkDIM2WInk_Hpt4nYVrx9ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبابات ومدرعات تجوب شوارع العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80126" target="_blank">📅 03:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80125">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">منظومة الباتريوت الأمريكية تحاول الإعتراض</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80125" target="_blank">📅 03:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80124">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/80124" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80123">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الصواريخ الإيرانية تدك الكويت</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80123" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80122">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صواريخ تنطلق من إيران</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80122" target="_blank">📅 03:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80121">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ada82ae90.mp4?token=gRT1oh3Lagd8p3vI-mC46Lb_ajElt9vqUVz7ByECtYyMB2N1dQ1_gwdOpyVvCTNQPsVCs87-e_lc-fSvLYp8M-LrArx6lhHNkP9QVUXHzgEeD_M5gE2H6KR-ltESqGcj3ChpW-B590Vh01se5oH35T-f1kB-wS_KyKnr79gBLFcdCctEvm7NZ5AaU9VR7EnqIJxtYjGU3XL4Zczsif4ijgS9D0GHI7bIiAjTXdKZjUUhV2ZomQkQPQ8_yPS5JInqqE7SeNzXSWfcoMoc1TbYczZaBoCDb4C_cjwEFgjoh6-UEyLYhw1iQa-y8Lw0he1843U4YnoowfKyHxZmCLSWeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ada82ae90.mp4?token=gRT1oh3Lagd8p3vI-mC46Lb_ajElt9vqUVz7ByECtYyMB2N1dQ1_gwdOpyVvCTNQPsVCs87-e_lc-fSvLYp8M-LrArx6lhHNkP9QVUXHzgEeD_M5gE2H6KR-ltESqGcj3ChpW-B590Vh01se5oH35T-f1kB-wS_KyKnr79gBLFcdCctEvm7NZ5AaU9VR7EnqIJxtYjGU3XL4Zczsif4ijgS9D0GHI7bIiAjTXdKZjUUhV2ZomQkQPQ8_yPS5JInqqE7SeNzXSWfcoMoc1TbYczZaBoCDb4C_cjwEFgjoh6-UEyLYhw1iQa-y8Lw0he1843U4YnoowfKyHxZmCLSWeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبابات ومدرعات تجوب شوارع العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80121" target="_blank">📅 03:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80120">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">صواريخ تنطلق من إيران</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80120" target="_blank">📅 03:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80119">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجارات وصافرات الإنذار تدوي في البحرين</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/80119" target="_blank">📅 03:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80116">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rdgoJEZ-_1kWk5tRz1ejEHVNKz2lImlFhuUrdmvLANIsPxxgzKBj3Y4CTN5pCTXvZ-KRp7GpETkTyBpTx00Ba9ekUP-mewUHLl0QZugVnlH-gy6AMNQ1Oys46oUPMOHxb2fvQjF99zEr81FLhW1c291WRXpf5svqE45F-CCYqWqC5Nc--HdfV08-qGKbWi9i5VycwkvVoTZzKYDmJGqNHaxZ10uaP0LVnpH7psyBJHd3hqQcBQ8i7HAB4I-yGSDu-sbm9CEHwLPLhi5iSSO5FW5kQAA46WSDSAzTObcRBX1tD0De_7TcRkSG6hcRh4e_Qc8X9W6wmbMjcrqLy57vfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d3784e6c.mp4?token=WJxhOn03zwiHqEDaA-FadjTjiA8PTxp_qC0TuXiIo4Pj2b8NIS-u74J7iLICaw8GpSCxNmTOW4eVhzhHuRyeqRE6EUcsUyeL3Wpt3NtYRP0hMXKHK_mtN9D8a178V9BIGQ3SH1aFK7WsbT5nX_xpCHxDUGlMkW80TguKWuhGcClfz7YHZ7BHxHDoVPMWQk9itA0d3qaZz6p3EfS-i-9WuahaqNiS7xc5TJzgyCBMAD-Jjht_Tk1p-d8rOqNPNKIuVdLhJvH-S4eaaIpY4PwnU8C_6V0OEUR12fWIJogsd44Qm9sIeaCSU9tP3-m1xU311ytMiUlcDUzIcfO2WObjPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d3784e6c.mp4?token=WJxhOn03zwiHqEDaA-FadjTjiA8PTxp_qC0TuXiIo4Pj2b8NIS-u74J7iLICaw8GpSCxNmTOW4eVhzhHuRyeqRE6EUcsUyeL3Wpt3NtYRP0hMXKHK_mtN9D8a178V9BIGQ3SH1aFK7WsbT5nX_xpCHxDUGlMkW80TguKWuhGcClfz7YHZ7BHxHDoVPMWQk9itA0d3qaZz6p3EfS-i-9WuahaqNiS7xc5TJzgyCBMAD-Jjht_Tk1p-d8rOqNPNKIuVdLhJvH-S4eaaIpY4PwnU8C_6V0OEUR12fWIJogsd44Qm9sIeaCSU9tP3-m1xU311ytMiUlcDUzIcfO2WObjPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من الإنتشار الواسع للقوات الأمنية في العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80116" target="_blank">📅 03:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a323ca8867.mp4?token=kHgTciw6h3kwFzotYsTfjJQvCnjd4CeYblSNi32JgU8JiXZQrJZnBLHeeqn_tq1i_a7vHqLvAsZncTTw-zyte2horT4iYfeUwCOvq4xj6t2XvwwcyBKE09Rr3xAshV0OK33FLZoDsVruYOQ4gs24mt5e8fsKUp0Gg-60Onux6BSQxlW0NK4j0ocfMnLMNzfbuv2HoMWgRU2sVV_YLxh1JL0-AGRJfBR6liQbXRD2rlOPpGf4c4hjjVCb-Z-PhYbJP3s7PZckRV5iVS5ldPhDCVFuiE4NxqMloL_mR10Ymdow4a8r9hRpDszPG56GlBXLY9VnPqNqVyhOVYJGD7ao6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a323ca8867.mp4?token=kHgTciw6h3kwFzotYsTfjJQvCnjd4CeYblSNi32JgU8JiXZQrJZnBLHeeqn_tq1i_a7vHqLvAsZncTTw-zyte2horT4iYfeUwCOvq4xj6t2XvwwcyBKE09Rr3xAshV0OK33FLZoDsVruYOQ4gs24mt5e8fsKUp0Gg-60Onux6BSQxlW0NK4j0ocfMnLMNzfbuv2HoMWgRU2sVV_YLxh1JL0-AGRJfBR6liQbXRD2rlOPpGf4c4hjjVCb-Z-PhYbJP3s7PZckRV5iVS5ldPhDCVFuiE4NxqMloL_mR10Ymdow4a8r9hRpDszPG56GlBXLY9VnPqNqVyhOVYJGD7ao6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر امني لنايا: إن غلق المنطقة الخضراء في العاصمة بغداد يأتي لغرض تنفيذ ممارسة أمنية، ولا يرتبط بأي طارئ أو حدث استثنائي.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80114" target="_blank">📅 03:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات وصافرات الإنذار تدوي في البحرين</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80113" target="_blank">📅 03:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80111">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔻
قسم بالله
🔻
قسم بخدا
🔻
We swear by Allah
🔻
مونتاج نايا:
#شاركها</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/80111" target="_blank">📅 03:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80110">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔻
مصدر امني لنايا:
إن غلق المنطقة الخضراء في العاصمة بغداد يأتي لغرض تنفيذ ممارسة أمنية، ولا يرتبط بأي طارئ أو حدث استثنائي.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80110" target="_blank">📅 02:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80109">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/egIMNQWpVswlepa9IWUNBWixAki5ZnBEgjAWu9GPXxzk9Gdh9HxLllKESxPw23gJceu4sInEa1FblYdCOwf9JFKMabtEo0RNPaten54VDGF8ADVi-cQY_VZt9Qvlg6lPjMUa9DtYPmDyV98Fep313sIdR1ftcwbVEaLvvQsNwmFB-1efAwiTP-_WEW8ir3M5GSReDRi1NDwIGoIBoIk5LILlryLIxqXZ9xIN7BQw-Wn9Y9sEBIH8FJFJDamtFZp0YjBIr4gTVumIKukZd4C0jIBWYkDBT_DWPV_7HSO5pH291cJZXkgAt0drpkomsP9ZEob3hGAIEOj4uAxOx8qZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
ترامب
:
«شنت طائرات الولايات المتحدة غارات على مواقع تخزين الصواريخ والطائرات المسيّرة الإيرانية، ومواقع الرادار الساحلية، لانتهاكها اتفاق وقف إطلاق النار، مرة أخرى! من المحتمل جدًا ألا يتعلموا أبدًا! قد يأتي وقت نعجز فيه عن التحلي بالمنطق، وسنُجبر على إكمال المهمة التي بدأناها بنجاح عسكريًا. إذا حدث ذلك، فلن تبقى جمهورية إيران الإسلامية موجودة! الرئيس دونالد ترامب»</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80109" target="_blank">📅 02:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80108">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1-Wc7bNYz29MU7UXuR8Mfmq2Ikl53Ai9RCfsXaUm8QtVY0H_uxHowaTE_AO-QXDYmAxpVg1Zj6NRdclpL8p-hn5qBbjQm6bW1IrGF9vGxOafSy7_GwWslQ57XhilGavv7w9Ahma1jebIJ2EH283e59g_6gCXuLBMFR2Uu9J5XwlnNGJXJ9NZQFEWEXhDL52YFlKzEsJ2AXN6Jsz4r0qdQc9wgxSwQEbh8Hz3-QX-MRnjzbeBkt0TsKsPp4TIoB7gt06uwzVjFaMKHPpfWrj35LR_FEaXR8woycAUPE0OZSC_3f-w5uVgsxPXgFmBjVBaRmRNmVZ7ikI139Lq65IOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
‏نشاط مكثف لسلاح الجو الأمريكي في الشرق الأوسط حالياً.
‏يوجد حاليًا حوالي 13 ناقلة وقود تحلق فوق عدة دول في المنطقة، وخاصة فوق الخليج الفارسي.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80108" target="_blank">📅 02:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80107">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔻
مسؤول أمريكي: أن الضربات الأمريكية على إيران "اكتملت".</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80107" target="_blank">📅 02:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80106">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
دوي انفجارات في ميناء لنگه وميناء كنگ جنوبي إيران</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/80106" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80105">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔻
مسؤول اميركي: ردت إيران الليلة الماضية بشن هجمات على القوات الأمريكية في البحرين. وأسقطت القوات الأمريكية والبحرينية تسع طائرات إيرانية مسيّرة هجومية أحادية الاتجاه، دون وقوع أضرار أو إصابات.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/80105" target="_blank">📅 01:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80104">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔻
مسؤول اميركي: الجيش الأمريكي ينفذ جولة جديدة من الغارات الجوية على إيران الآن، رداً على قيام الحرس الثوري الإيراني باستهداف سفينة في مضيق هرمز في وقت سابق من اليوم. الضربة الأمريكية الحالية أكبر من التي وقعت الليلة الماضية.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/80104" target="_blank">📅 01:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80103">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
مجددا سماع دوي إنفجارات في سيريك جنوبي إيران</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80103" target="_blank">📅 01:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80102">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/80102" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80101" target="_blank">📅 01:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80100" target="_blank">📅 01:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewlbXsMlP6IwUlr_4xH72hP1mM4Bc_ZhJMTX7zZhjc7D4XWnRol8f00cyU_66c9_cAJCNfqjXf9ZNg5yT6AIYilLZheZU_O81lcyQ84oXlbkkPGZ72jih5xf7XzzO0y01GqZV53A3WvAMpXGlwLNo0mrtk8yjvWZsxJ4ixgFL-QD3Dyj9ih2cTZ8SPKZhgSedLu_KU-QFIhUTm04ugqTTGf2d_x8USjfD997VMjmVYhsg35zRGrTvxoH_GMtKfrprU3CP9qCiOwZLexa_eFVLv1eVUG5y3Y7CXrq0P1O5aDFYew491vjNXyTinTOt1e5PKxcjxIju2gL9MLPcRtplw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اختارت الولايات المتحدة ناقلة نفط للتحقق مما إذا كان ممرها الملاحي في المياه العمانية لا يزال "آمناً".  كبش فداء
😂</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80099" target="_blank">📅 01:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔻
غارات تستهدف برج اتصالات في قرية طاهروي بمحافظة سيريك.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80098" target="_blank">📅 01:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80097" target="_blank">📅 01:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دوي انفجارات في سيريك.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80096" target="_blank">📅 00:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80095">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇯🇵
زلزال بقوة 5.6 ريختر يضرب اليابان وأصدر علماء الزلازل تحذيراً من تسونامي.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/80095" target="_blank">📅 00:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80094">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjrhFZWHvAyvGIBzN-O_VZ6--rNchViLYXVI4pq2XjYMwgQj3KAwonaIUzQQ_byYpe4UqhaWu9XTNQCYbn2Gx8f4Yj2hSeTWHAdRaIyjX9n479AdBp6p1vC99V8pfUgrJPH2c7wNjdu2-hwwpgHNMicJcLFqrmc24tGhEx9duWTsaysS5UAhAqChjjCKh2mr9s6c_9eGlpvZpld23HONB5FzAYPK63-6RnmAQOIGdAKu3RCEvXlnx77LpaTR8A85aQLiiFOqSDjMQRpv5cf2TGS1dDZp1dotLLOfi6Z0RZvpLHzjsaNvTzD9CR2j4fhowPtSSi--3C19_CNpogNy6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عُثر على جثة أحد عناصر قوات البيشمركة التابعة لحزب حرية كردستان (PKK) ويُدعى سوران محمد زاده داخل أحد الفنادق في مدينة أربيل.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/80094" target="_blank">📅 23:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80093">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQl0Ec32BeV1aAB2vCJdcGmjkqGFIt1PrizfwC07B161zz-JOO14Crn9lU0_LGt8NxKwMphmKqGgwWcj9Q7bOGNBVmgAuKj2VQbSYViga1Ev9cibf15AcQbeZK3ykybJ-zpXKLzM4oLlciIMHj4n-bKoFUpjMsnsr-LYZtInckBunvzDwZcmBAPY6_CzPuJE7hMGz8WekUTMY4dhqY9o9NtlonfYfLDBDFsOJ9tZjt4K4Wb-LrhyVBVBPHgcBwRuN518Sy4lZuJC9aEQ-w6rPWxc4dCv9JRULuSGPJ0SrM4qaMJnt3qBQGO63rfa2nh2AzR56w_ABceEkZEtyC-nrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اختارت الولايات المتحدة ناقلة نفط للتحقق مما إذا كان ممرها الملاحي في المياه العمانية لا يزال "آمناً".
كبش فداء
😂</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/80093" target="_blank">📅 23:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
‏زلزال بقوة 5.6 يضرب سواحل أراغوا في فنزويلا</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/80092" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80091">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تحت عنوان: "قوموا لله"
🔻
تعلن الفعاليات الشعبية والوطنية العراقية إطلاق الوسم الخاص بتشييع السيد القائد الشهيد علي الخامنئي على مختلف منصات التواصل الاجتماعي وذلك بالتزامن مع قرب وصول جثمان الشهيد في دعوةٍ واسعة للمشاركة في التفاعل وإحياء هذه المناسبة عبر الفضاء الإلكتروني.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80091" target="_blank">📅 22:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80090">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtgE_wX3mHh2VJAUDKLvz2mggDzhssABmRmSTdBmk2MJ8bOfz_UA4ZNqgOBJDYHc2S1jPkb-YeSkrm0BfkY_dnL9AUoGX7m9-NM6Zcy0U_h3QbKdh_2Ab7pIPNBV-PdtG44-EuELpnAsY0H0nh-dAcXbZeahtfOwjY3TW2KuFYvpbC3JVbnmFQxQg97GiO9F3gb2U3bNu-5nxWisZqGI11LVgtQ_qxKtyX3xDJ_bIOYkH3PVkO8Vc9I2oix_VA1qkWOn83SsMHa-3HEtFxzpQZR4Y3tV7qb0ttyj1hI2J2gi7I3gYaxl52Hr9Gead2mCoYyJrb0KYRONtF1ly6TH-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب ينشر:
حمل العالم ثكيل
😆</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/80090" target="_blank">📅 22:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80089">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
🇮🇶
‏
الخارجية الإيرانية:
عراقجي يتوجه إلى العراق غدا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80089" target="_blank">📅 22:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80088">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇫🇷
‏الإسعاف الفرنسي: 109 حالات وفاة في مدينة باريس لوحدها خلال 24 ساعة الماضية بسبب موجة الحر.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/80088" target="_blank">📅 21:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80087">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🌟
‏نتنياهو:  أشكر حكومة لبنان على ما أظهرته من شجاعة.  توصلنا لإطار تفاهمات يؤهلنا لإنهاء الصراع مع لبنان.   الاتفاق مع لبنان ضربة لإيران ومحورها.  إسرائيل ولبنان اتفقا على منطقتين أمنيتين لتجربة العمل على نزع سلاح حزب الله.   لن نترك المنطقة الأمنية في لبنان…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/80087" target="_blank">📅 21:39 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80086">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2dbc6b86e.mp4?token=B0I5dfn3uNBbNqHNZgXJyzTNqRJeTB7zpoN6Xae3CrVKb5RA9wyIO6JhT8y0CMBJ8wWb5cc21-0lOfwfj3pT4IT37IyIP2CG0f2oBtKLYny1gIs1v-CV9ugJ9wiqY0Lum8BO_fWO2z2scI4nd4gBXiqfwd5VAuo9BpvQng_RKcVluXL8u5_OaUl3fBBx_n0L8JeUgCanJTdvU9_91JZLy1O021Vy2kXnhGT7wzXyDoqHwNG7AFZp1Cfybdy8foX7R-gNSseeB0J68QmAbHmpZl-3Raripksnwd95On5IhCNY4AkqYk7E3F1RWsq7D1mf5GV3w5fHNoEtDSfithvbUA2iigB8L2qBl4RmraWS4lGFWhN82AMfUQMe5-feu0Eiq1grLZAxBseqvfHQx_Lr63VUjmHcb9q3X2WcSJFz3ypKRekonPR6enXHspNbURVvmIifpW7oMWIjXh_0tJtrN3pSVfzbHoZkSQJA-tYyU2F1fomXrgYABm8ZpjQ1KPwLWZqNkxlq-Np9Rb06hfzSTFIiBeQTImVg0yQH7FbnkP5LcSlImRwN7Q8ZGdPkERGNqzv4G-W3UMWy-LeTxMw3MDZTmYlMWfDPh3Y2JtKi_nfWqyAznrpmvBrBK7puaAxCM-s2dsse9ts9MOG3kuk5K8WN7QJDtAXhZlLFTNfZJeI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2dbc6b86e.mp4?token=B0I5dfn3uNBbNqHNZgXJyzTNqRJeTB7zpoN6Xae3CrVKb5RA9wyIO6JhT8y0CMBJ8wWb5cc21-0lOfwfj3pT4IT37IyIP2CG0f2oBtKLYny1gIs1v-CV9ugJ9wiqY0Lum8BO_fWO2z2scI4nd4gBXiqfwd5VAuo9BpvQng_RKcVluXL8u5_OaUl3fBBx_n0L8JeUgCanJTdvU9_91JZLy1O021Vy2kXnhGT7wzXyDoqHwNG7AFZp1Cfybdy8foX7R-gNSseeB0J68QmAbHmpZl-3Raripksnwd95On5IhCNY4AkqYk7E3F1RWsq7D1mf5GV3w5fHNoEtDSfithvbUA2iigB8L2qBl4RmraWS4lGFWhN82AMfUQMe5-feu0Eiq1grLZAxBseqvfHQx_Lr63VUjmHcb9q3X2WcSJFz3ypKRekonPR6enXHspNbURVvmIifpW7oMWIjXh_0tJtrN3pSVfzbHoZkSQJA-tYyU2F1fomXrgYABm8ZpjQ1KPwLWZqNkxlq-Np9Rb06hfzSTFIiBeQTImVg0yQH7FbnkP5LcSlImRwN7Q8ZGdPkERGNqzv4G-W3UMWy-LeTxMw3MDZTmYlMWfDPh3Y2JtKi_nfWqyAznrpmvBrBK7puaAxCM-s2dsse9ts9MOG3kuk5K8WN7QJDtAXhZlLFTNfZJeI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏نتنياهو:  أشكر حكومة لبنان على ما أظهرته من شجاعة.  توصلنا لإطار تفاهمات يؤهلنا لإنهاء الصراع مع لبنان.   الاتفاق مع لبنان ضربة لإيران ومحورها.  إسرائيل ولبنان اتفقا على منطقتين أمنيتين لتجربة العمل على نزع سلاح حزب الله.   لن نترك المنطقة الأمنية في لبنان…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/80086" target="_blank">📅 21:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80085">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f6b672cd7.mp4?token=Q_8Fx7kmyQTapSqYPY5hbg1aBrgimVS_yCL6HjOh-UKuq6Yk5pz_IUngUGjnKi6rJOtAIcJ4Swz2Tg252Sl5lGmo24G56-pN8ZgQXFsPJ6kr9jH8wFPTJ3-Q25sW35SOKt2u3x7Jr8DgtPj7cDIpqCqyBeKaXWNLltTVL1orKeW6NCThhIqmYu8_IcZDoK8q34ORVqHKhsm-wkGA918szeY3a3y83dvp2khn_BAVhNaO5f5eFbjrHBIfj-oexIobD76pbYpJbNyCkIZZtSwVG5cJU50uYQ60B_9Vz6MGiUauUczUdSsKoaZReLCcbV7qDdFr0HJBrbHxFYvZdXGSHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f6b672cd7.mp4?token=Q_8Fx7kmyQTapSqYPY5hbg1aBrgimVS_yCL6HjOh-UKuq6Yk5pz_IUngUGjnKi6rJOtAIcJ4Swz2Tg252Sl5lGmo24G56-pN8ZgQXFsPJ6kr9jH8wFPTJ3-Q25sW35SOKt2u3x7Jr8DgtPj7cDIpqCqyBeKaXWNLltTVL1orKeW6NCThhIqmYu8_IcZDoK8q34ORVqHKhsm-wkGA918szeY3a3y83dvp2khn_BAVhNaO5f5eFbjrHBIfj-oexIobD76pbYpJbNyCkIZZtSwVG5cJU50uYQ60B_9Vz6MGiUauUczUdSsKoaZReLCcbV7qDdFr0HJBrbHxFYvZdXGSHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
‏
نتنياهو:
أشكر حكومة لبنان على ما أظهرته من شجاعة.
توصلنا لإطار تفاهمات يؤهلنا لإنهاء الصراع مع لبنان.
الاتفاق مع لبنان ضربة لإيران ومحورها.
إسرائيل ولبنان اتفقا على منطقتين أمنيتين لتجربة العمل على نزع سلاح حزب الله.
لن نترك المنطقة الأمنية في لبنان إلا بعد التأكد من نزع السلاح.
‏ندمر البنية التحتية العسكرية في المنطقة الأمنية بلبنان ولم ننته بعد.
الولايات المتحدة ولبنان وافقا على بقائنا في المنطقة الأمنية بجنوب لبنان.
شددت لقواتنا على حرية الحركة لصد أي تهديد في لبنان.
عارضت بشدة أي محاولة لفرض انسحاب علينا والآن الولايات المتحدة ولبنان يقولان لإيران إن هذا ليس شأنها.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80085" target="_blank">📅 21:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80084">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌟
المكتب السياسي لحركة "أمل" اللبنانية: نؤكد موقفنا الرافض للمفاوضات المباشرة والاتفاق جاء غير متوازن ويكرس في معظم بنوده وقائع لمصلحة العدو على حساب المصلحة الوطنية وينطوي على مخاطر سياسية وسيادية ولا يمكن القبول به.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80084" target="_blank">📅 21:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80083">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-wO13-LSKfNufwcgJ-C9CkN4Hd_hVgrI2vHODKA5QCHTd_PYFBtO3oH07XcnhLVu7yW8hjpNCohgKWZSht-5x2F3erPiwxQKnZQZVJr3bOUIpE2TU0dRdnnTk0NrT9tLEs02HggEUKTTfp-0OcURW_acbJf7bkmXLv64a6BedsVUp6nIl--cRxiCH7fjJZTchK7wJLFej0QqCmqnG1YRss8C09lzg3JHfvd_aNrk5htPH4lY0WJK-Tkx-VXg3he1Gn233fmIdcVy8zeNk2p86GukK8gmEYU8C1vARTZ6Kj8QQHOE99j4g0zQzsTJAf3s6yNpYPXYr0u9BOb1-81pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
السيد مقتدى الصدر:
إلى هنا ولاينبغي السكوت عن الأداء المخجل للمنتخب العراقي في كأس العالم.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/80083" target="_blank">📅 20:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80082">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🌟
الإمارات تنعى جندي قتل بظروف غامضة.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80082" target="_blank">📅 19:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80081">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🌟
وزير الحرب الإسرائيلي:
إذا حاولت إيران الهجوم لمنع تنفيذ الاتفاق مع لبنان، سنتصرف بقوة كبيرة.
‏لن ننسحب من لبنان بما في ذلك مرتفعات الشقيف.
‏سنحافظ على حرية عمل قواتنا في جنوب لبنان.
‏الاتفاق مع لبنان يرسم لأول مرة واقعا جديدا أكثر أمنا لحدودنا الشمالية.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/80081" target="_blank">📅 19:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80080">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇱🇧
بيان سماحة الأمين العام لحزب الله الشيخ نعيم قاسم حول اتفاقية العار الإطار بين النظام اللبناني وكيان العدو الصهيوني:  1- أين أمانة السلطة اللبنانية ومسؤوليتها تجاه شعبها وحماية سيادة لبنان، والتي لم يعطها الوصي الأميركي وقف إطلاق النار، وعندما جاءها من محادثات…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80080" target="_blank">📅 19:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80079">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">تشييع الولي
#قوموا_لله
#باید_برخاست
@
in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/80079" target="_blank">📅 19:11 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80078">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn13aZGrJWj_KW5oj4aDwvvQoJuo1y0RIFsZpUfm390Lcvx1MXmjvwbHMRzjS0eEeiiJ8Ww77EdRQQ8_MxzM2B9voxEd9QfvV6n7GJhfDV3LKoEUk_WqQk6tGfKbhflw_bV4COhKCDB8hVzqn8YGlHAg3o0dYvYkMAoiovSZdm5SgxDKz6_O5bRcqUweYngp6KAmR5_bn8P9egxYHU73E9NPyZjr7iSUmW1ddsuoHb__UOeUT7HPKBETqP49RdaZ2-247vVzqcILghO-m052e7R5hLw4X62P_8_i0MRSyO2wZ8EBUJw_lrYFRcHv_Td7x9LAjLdoHpCK7nEK4XPubw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
غارات للعدو الصهيوني على النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/80078" target="_blank">📅 19:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80077">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c051e16298.mp4?token=Qaz8AEIUAyctp6fv4lceiKmGTXI6gfavnkDsEPR38LUOjK0RqGv9IjhM18CdrT4rkB88N0qkGcXNvZvWZ9xjHUT36B9_7Bxqeu75kUgNWZzipO92GJ3rA1Sact7ECp8W7tVhmUVU2IO8OESYGvfGX9Nqfn_DxWlabVmeOv3DsIHBrvIT-2xq5TcriN_wqozeImUnIvjYOBLVG5uceIjIcy_f_BknAoDwwlAN6jKC0EFafZEsY0jdZ4ZXtQrIo3Te14fAzWz-z9tPkph4swE5lmOk85EL0e8_lCuHDPcVUm0uFAp2XducXFYsG-JIvrQzgrM6UBoeWTy0pHz-_Dx_0i38DGmGZvV6OCN8dagLYYtiZFWLNznjPFtD45yZhfSTTEr8PLkxpnlevkdklH5Xx2q9lYcFgRpoINcjS2YzvLQZzU1KOkHw5ST-mXeRUEths0NeD7ZJ8Yi7I4RxEVMdxCHDsjVkztO85I2gSn7pjRscNBDAWgEUFNytnw9Mv4fr6HqgExr92QaqWp7Na7IniDX2fHixVsUmDpIsuCVnGTwjbaeQLG0umuasTkN1f287SWbIuSmqwIwCfgGlAZB3yYPqRO9b_4QB1QJ33e2Q-hbq18uY4QnBOmwlTCpkZTAfv7qGyab1k39M-nNGpAHKrL7UcDXdh7dhywJQDsh5Km8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c051e16298.mp4?token=Qaz8AEIUAyctp6fv4lceiKmGTXI6gfavnkDsEPR38LUOjK0RqGv9IjhM18CdrT4rkB88N0qkGcXNvZvWZ9xjHUT36B9_7Bxqeu75kUgNWZzipO92GJ3rA1Sact7ECp8W7tVhmUVU2IO8OESYGvfGX9Nqfn_DxWlabVmeOv3DsIHBrvIT-2xq5TcriN_wqozeImUnIvjYOBLVG5uceIjIcy_f_BknAoDwwlAN6jKC0EFafZEsY0jdZ4ZXtQrIo3Te14fAzWz-z9tPkph4swE5lmOk85EL0e8_lCuHDPcVUm0uFAp2XducXFYsG-JIvrQzgrM6UBoeWTy0pHz-_Dx_0i38DGmGZvV6OCN8dagLYYtiZFWLNznjPFtD45yZhfSTTEr8PLkxpnlevkdklH5Xx2q9lYcFgRpoINcjS2YzvLQZzU1KOkHw5ST-mXeRUEths0NeD7ZJ8Yi7I4RxEVMdxCHDsjVkztO85I2gSn7pjRscNBDAWgEUFNytnw9Mv4fr6HqgExr92QaqWp7Na7IniDX2fHixVsUmDpIsuCVnGTwjbaeQLG0umuasTkN1f287SWbIuSmqwIwCfgGlAZB3yYPqRO9b_4QB1QJ33e2Q-hbq18uY4QnBOmwlTCpkZTAfv7qGyab1k39M-nNGpAHKrL7UcDXdh7dhywJQDsh5Km8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
توثيق جديد يظهر لحظة دك موقع في البحرين بالصواريخ البالستية الإيرانية وفشل منظومة الباتريوت الدفاعية الأمريكية خلال أيام حرب رمضان.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/80077" target="_blank">📅 18:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80076">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCsOoysboZN9rvufzxfvWDtQQ3u-K-mL39ToIRksLhpgUtQuhgqMPkIzTujTrYZXyoLnEoKbgxp8Wso0egyYMZU3cZK2gSYvB94xb8bw6ktkq4c72d1i_73iQ590JJb69dG4-FwQTUMImjirlYMHg8Brq1qwPm3CB4iLv-BcmUlaZl1YytuA2UrFbPoomxAmoO7s_oTbYI12w1JpMsV7ybNpodfh312dcd-EcpbrkKaNsA6DQUeIujN8dAlD9fKvKjmQI49EWFzR6_x4x45vhmRqhcEbSvxh8ykPVdwfK0IzpDrfKwOmAavA1sRE8XpHZ3VbeIoHwHo2Nf9rMPXLew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
غارات للعدو الصهيوني على النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80076" target="_blank">📅 18:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80075">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b3f81696c.mp4?token=hzNpviGv4S2r378vFS2BpnTmIKhdslNJ-vOXW_4Z1jq4ku0AWewmCTwuw7tqGkDfmctPQvJCSwxpKrZMI4HOO03ewPRMGmNys9RGFsKsC1sFC2B6fQxwdOpgXToxqAXyGXn508HcUto5C33QksP6w0laDMjbY5TjAirXEuFQxWgzi7GmbMmAOHFrkHttDBn2dLikR6iff6WgMxjN_IlXm3GFa0SUhdDj9Qx8WBMeb8eK1TT2tX4rDs56OC0YFxT4QeSEQaJ6BeTPXDUjng70F24ubNJ7E4szTgSueuorh-KneiQrVg17hRKI5kJYkr0D0j61IfL1F27B9gpBDjAQWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b3f81696c.mp4?token=hzNpviGv4S2r378vFS2BpnTmIKhdslNJ-vOXW_4Z1jq4ku0AWewmCTwuw7tqGkDfmctPQvJCSwxpKrZMI4HOO03ewPRMGmNys9RGFsKsC1sFC2B6fQxwdOpgXToxqAXyGXn508HcUto5C33QksP6w0laDMjbY5TjAirXEuFQxWgzi7GmbMmAOHFrkHttDBn2dLikR6iff6WgMxjN_IlXm3GFa0SUhdDj9Qx8WBMeb8eK1TT2tX4rDs56OC0YFxT4QeSEQaJ6BeTPXDUjng70F24ubNJ7E4szTgSueuorh-KneiQrVg17hRKI5kJYkr0D0j61IfL1F27B9gpBDjAQWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع حريق وإرتفاع أعمدة الدخان في سفينة تجارية بالقرب من جزيرة قشم الإيرانية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80075" target="_blank">📅 18:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80074">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وول ستريت جورنال عن مسؤول أمريكي: مسيرة إيرانية أصابت ناقلة نفط كانت تحمل مليوني برميل من الخام قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/80074" target="_blank">📅 18:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80073">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">وول ستريت جورنال عن مسؤول أمريكي:
مسيرة إيرانية أصابت ناقلة نفط كانت تحمل مليوني برميل من الخام قرب مضيق هرمز</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/80073" target="_blank">📅 18:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80072">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">#قوموا_لله
إنتاجات نايا - أهالي خرنابات
جديد اضغط هنا</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/80072" target="_blank">📅 18:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80071">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‏زلزال بقوة 6.5 درجات يضرب أفغانستان</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/80071" target="_blank">📅 17:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80070">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇫🇷
‏
الإسعاف الفرنسي:
109 حالات وفاة في مدينة باريس لوحدها خلال 24 ساعة الماضية بسبب موجة الحر.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/80070" target="_blank">📅 16:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80069">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/80069" target="_blank">📅 16:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80068">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/80068" target="_blank">📅 16:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80067">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/80067" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80066">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80066" target="_blank">📅 16:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80065">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80065" target="_blank">📅 16:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80062">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الاردن تهنئ النظام اللبناني بالاتفاق مع الكيان الصهيوني
التم المتعوس على خايب الرجا</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/80062" target="_blank">📅 16:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80061">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇱🇧
بيان للشيخ نعيم قاسم بعد قليل حول إتفافية العار التي وقعها النظام اللبناني مع الكيان الصهيوني.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/80061" target="_blank">📅 16:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80060">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">في خبر غير مهم
رئيس البرلمان العراقي هيبت الحلبوسي:
نرفض الاعتداءات الإيرانية التي تنتهك سيادة الدول العربية والإسلامية وتهدِّد أمنها واستقرارها</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/80060" target="_blank">📅 16:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80059">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وسائل
اعلام:
‏ستعقد جولة المحادثات بين الولايات المتحدة وإيران في شهر يوليو في الدوحة.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80059" target="_blank">📅 15:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80057">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C1bzkPYGbLogmvG03v3ARyFYBCThGSbLPN3XY3LJxNsC0LlMMD-JonVhXA8SXedfoQFdps_Er0f26aKHj40Pv5RXLSfUU4nkFyneVW5YGQZ2bVwAnQ4tJCvQfl9mRcV6PAhbeWFLyS7sMcWaoSNf9yXzQz8dNmu5KRwvBmMxEE6XpPcenpb_c4DPhORRVbxkqmrfQCpCuC6oQruSMIA8NyOAouYTeJosx4hozLsR5B8jlT4V4LT0pjO10t4kPe-I5CmOTmfcEgbdDosk_iWsJh3MXKqKJnkl0qNDaWLj1u_qXfrmdjeUs-HlUi_eNxaqnw6KhoznDyBO2O9MYXXiMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط طائرة مسيرة مجهولة في النهروان جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80057" target="_blank">📅 15:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80056">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c12540e77.mp4?token=u3kkQDGiTNqWz7Gr_xOYfrowfgEC_6bvTt0hrrzYsl2--KwFnXei3mUeaPVgez5YdEvFL_E9sYGrTu1DkkYO1LqZDGMo46pU_vl966Ihs3aCksMY83CBD5AIkZiKDeyTpfS4JGLPtNamgQhqV3qNpvhZR7QRxzavfchWOytK9dEd0bxnXAXohYcALTgO3gYab7iWclg3biawqKT8oUUIx8gH0kOqspDr66skqCCiNnEaziZK-ihwKEa_eMHxKCVdonFABfeGgD3I5CX2ZtBOcXOWhPRUod69mwSB2APCKRHI9y4ASJGXM3bh4ba9AQ1CkQ92QRQpiZJl-cYwCnC-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c12540e77.mp4?token=u3kkQDGiTNqWz7Gr_xOYfrowfgEC_6bvTt0hrrzYsl2--KwFnXei3mUeaPVgez5YdEvFL_E9sYGrTu1DkkYO1LqZDGMo46pU_vl966Ihs3aCksMY83CBD5AIkZiKDeyTpfS4JGLPtNamgQhqV3qNpvhZR7QRxzavfchWOytK9dEd0bxnXAXohYcALTgO3gYab7iWclg3biawqKT8oUUIx8gH0kOqspDr66skqCCiNnEaziZK-ihwKEa_eMHxKCVdonFABfeGgD3I5CX2ZtBOcXOWhPRUod69mwSB2APCKRHI9y4ASJGXM3bh4ba9AQ1CkQ92QRQpiZJl-cYwCnC-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات صهيونية ترمي بالونات عليها منشورات باللغة العبرية على الحدود العراقية</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80056" target="_blank">📅 15:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80054">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4jaKsRQcSrZ1_0SSzJhwUVWsT6FHOoBuvmQzatHKUls_7bDDmiQHOG2vI8VtXwnpZqyi8ZIVRkpyLGt7s2s_E5pjGD_SP4AVuPM2gbAmQZt-wGcgGOXZ8OnXbBT_mzXU3DdhpcMtFM2vRqfvzWrUkD55LMnJpXTf8Ins55Q5IOnLwAasNn6HqpqJDqjPtyQxf1bPxE4a1iYhMzQcobL4b7w4_kvTycCJNjCoPD1b4mfyjMygRV9YBfueCRlzz6hDJZBXKcjBboQRg9cSd7Y3NPE6KrY5tKQTfdDT2Y102UkoJCQUiH684DV3_M5ra7tXqi9ymioNI7TTuMgS-4YbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A2sS_au2UjK92kqLCb830jROqkcB8hqFekdsapiuQATafIAEkBJNb8usyaRzE2qsJurKztHkLBjhDo55jBZHqnKT1tG2tDnDWMHx_7ykNKSRXKue0sdjqq6b1tFNAoxtluWnMn9YhLUff0fYATAojPBmLbHSKToTcAQMNnOtHLR5C-LxDe_BNwzc9E2BOg9SrP09Mr1psAO90o-ZrTjIGG6CV81D-7f6zHEdEW4uS5vqyZ91NR1OXUlpaU9wXSPwyq0R_aANDxEnBvh2ZnZRX-cYd3XR9XmajxX0xurMtyTm5x5iV6WCRP-YZROYrUMOAeJ95ZL-ouVSXSOAFizvcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طائرات صهيونية ترمي بالونات عليها منشورات باللغة العبرية على الحدود العراقية</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/80054" target="_blank">📅 15:14 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
