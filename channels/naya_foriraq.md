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
<img src="https://cdn4.telesco.pe/file/R4iz227nIC58QkdJbhGGjs66IoEyc0b7yd6mUI1FktF10AQfueS6EX-IW3MOuvYdFqITqH38hEWGUVDXx869JV3TKyXxWn4qB2mLEOO6B0um-pCFj0sojrDyRNmZo19OSUPQAOXxMp4Z1njWXQU32afHyj6J74B_edeHfFioAPcgu6YBear02B6pce3pDtMPKC96B2374ZJS3a2hf75EGjh2p-sMUaxUDx2LZ1pEer3aj539F9ASpIKp4kwVnQyBamM3kSMQJe-LqP_ZNf4S1WPdMLcStD4P9-Yy4OF8OM0tmfwJvw_e2RYl0aDON73VMYPNg2vW_mGsCEJOWzb5PA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 260K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 04:29:35</div>
<hr>

<div class="tg-post" id="msg-82611">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
🇺🇸
مسؤول أمريكي:
الضربات الأمريكية ضد إيران لم تنته بعد.</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/naya_foriraq/82611" target="_blank">📅 04:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82610">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجار في مدينة ماهشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/naya_foriraq/82610" target="_blank">📅 04:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82609">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔻
مصدر إيراني:
عودة الهدوء إلى محافظة خوزستان في جنوب إيران بعد عدة هجمات أمريكية طالت عدد من المدن.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/82609" target="_blank">📅 03:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82608">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔻
مصدر إيراني لنايا:
الأنباء التي تتحدث عن انقطاع التيار الكهربائي في جميع أنحاء الأهواز غير صحيحة وكاذبة.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/82608" target="_blank">📅 02:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82607">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0639135974.mp4?token=CVvVRRe0yiQbw9uJsJ7aownVUoSmgcsjlab7hlIyFnL_uf_qN0KgEI4-zI7IBKaJuvAS3TrOubkSY4h2Tg-Y80gUAG1zZJ_0kr7m8QxszsfqvpRzO_yGwJ8A9mSE_FDdVGUUgjlpq-RhLRB4LVz0vXvmBtkFZNWHZPLDB0Vup5m9qpGITByNv0a64Y52TViqZ7bdH3UMvJcrcYGXjqaqabmPmVJmjcNIH8DSXaDy_gtNpee1TNt0Apmet22t7LEbYFWFQS0V6raZSPitqF2uGvcgJtPBQGlJypUspPyC64_NcwpHmZJiHPAucKCXl2eEsESUa2AgpSHFtEQjkVBY_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0639135974.mp4?token=CVvVRRe0yiQbw9uJsJ7aownVUoSmgcsjlab7hlIyFnL_uf_qN0KgEI4-zI7IBKaJuvAS3TrOubkSY4h2Tg-Y80gUAG1zZJ_0kr7m8QxszsfqvpRzO_yGwJ8A9mSE_FDdVGUUgjlpq-RhLRB4LVz0vXvmBtkFZNWHZPLDB0Vup5m9qpGITByNv0a64Y52TViqZ7bdH3UMvJcrcYGXjqaqabmPmVJmjcNIH8DSXaDy_gtNpee1TNt0Apmet22t7LEbYFWFQS0V6raZSPitqF2uGvcgJtPBQGlJypUspPyC64_NcwpHmZJiHPAucKCXl2eEsESUa2AgpSHFtEQjkVBY_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة تنفيذ العدوان على مدينة الأهواز الإيرانية</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/82607" target="_blank">📅 02:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82606">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عدوان على مدينة انديمشك بمحافظة خوزستان الإيرانية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/82606" target="_blank">📅 02:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82603">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70b929cfea.mp4?token=LoL_kdYrDTN_MWK9OTVCDcgFCc6awbNwWjKOJKH0HgNn_BrNFHqViraqV1kbNMpmKzgu20QR9rVfrtWn4FaiXJimnJKwp9S2P4EYVgl5FL7x7ofQr2lETXeubMV9XrU5hYMQBTtQfsYzXjWqDTFMj29e0dXIqFlMWJWxKyQ3W3dxMuMVFHE-8exjeAO4008i1S7pl1tHlyKwY3-gQP7is60dhmZ4wyNggdDbZ5R3PsDx8RUSDjMuhZ1XWK7C03CHGyG4WwNdb_kiA5Wwj_cbf56bI0VSJIgPJF75VQYXazdmMUGebfBjUR05MwQEMR0Vmk9AwqmaPrbUx-tPOYH2yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70b929cfea.mp4?token=LoL_kdYrDTN_MWK9OTVCDcgFCc6awbNwWjKOJKH0HgNn_BrNFHqViraqV1kbNMpmKzgu20QR9rVfrtWn4FaiXJimnJKwp9S2P4EYVgl5FL7x7ofQr2lETXeubMV9XrU5hYMQBTtQfsYzXjWqDTFMj29e0dXIqFlMWJWxKyQ3W3dxMuMVFHE-8exjeAO4008i1S7pl1tHlyKwY3-gQP7is60dhmZ4wyNggdDbZ5R3PsDx8RUSDjMuhZ1XWK7C03CHGyG4WwNdb_kiA5Wwj_cbf56bI0VSJIgPJF75VQYXazdmMUGebfBjUR05MwQEMR0Vmk9AwqmaPrbUx-tPOYH2yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رصد إطلاق صواريخ من الأراضي الكويتية نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/82603" target="_blank">📅 02:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82602">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارات في مدينة اميدية ضمن محافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/82602" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82601">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb3b90797.mp4?token=uzRif_xFYrTq0YLP4JKF4p48N93upAIeDuAY4RlGXDQ2qzwcqwQSYpqIEYXdvS5ydZIgXzcRxz5EdREX2rKEGPTxyGK8KuQMY7kl4-csLzIPdT3TgZS6xnukYutBen11IArwhzzBbcIYkJ2KGLzpCUdQ5tGyQPTf8WX0x3iixAjPYJ69s2xINQdyIG6tqQK2GM_ZvjmAwocS9CBBOYuz-r7B_QWfur3_vim3pPGwPWGAWbm36l0EnldLrxxZEvXQOmCAYv58WWOGudPKDFiUKvy7QgEBjrpeC7Y2bGZdCeSJeD7XJjw4O7ZBreB3MltG3sZ4XzCeyP1NVQPX69YqZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb3b90797.mp4?token=uzRif_xFYrTq0YLP4JKF4p48N93upAIeDuAY4RlGXDQ2qzwcqwQSYpqIEYXdvS5ydZIgXzcRxz5EdREX2rKEGPTxyGK8KuQMY7kl4-csLzIPdT3TgZS6xnukYutBen11IArwhzzBbcIYkJ2KGLzpCUdQ5tGyQPTf8WX0x3iixAjPYJ69s2xINQdyIG6tqQK2GM_ZvjmAwocS9CBBOYuz-r7B_QWfur3_vim3pPGwPWGAWbm36l0EnldLrxxZEvXQOmCAYv58WWOGudPKDFiUKvy7QgEBjrpeC7Y2bGZdCeSJeD7XJjw4O7ZBreB3MltG3sZ4XzCeyP1NVQPX69YqZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية الإيرانية في مناطق جنوب غربي البلاد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/82601" target="_blank">📅 02:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82600">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجارات في بهبهان ودزفول بمحافظة خوزستان الإيرانية</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/82600" target="_blank">📅 02:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82599">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دوي انفجارات جديدة في جزيرة قشم جنوبي إيران</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/82599" target="_blank">📅 01:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82598">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انفجارات في بهبهان ودزفول بمحافظة خوزستان الإيرانية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/82598" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82597">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a9f5eacac.mp4?token=HNf_UL2fysB79CV2Ryw-FhOnw16cvzHuCnGSnJhyZmUp6-wn9jRDXyUFL5b0HCf2UuACovVI9q2O7mMVr9yGb4NRmaq_vVkLGsy6-BkKMpi7Hya_w7pgpQ7QS2BzY43zvZzJ4KSp5Hs-w_zx-yONhBfEIgw8Kgt8VunU61euY9S045REGJaGiBiyhD1oCBkIVKkYyHkuQoTVIBieHpENJtfxdZPiSUbjCxsHGcIUbIi5fOSub9Rvs8ovZfKLhWX9E4GJfxd-Z12lfy2I9h0ZL4W7wYINYh4_e4DO2244aXqu46z-80OBKAS2FNecH4zRZWKbqIv27PIQgr10fKcCaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a9f5eacac.mp4?token=HNf_UL2fysB79CV2Ryw-FhOnw16cvzHuCnGSnJhyZmUp6-wn9jRDXyUFL5b0HCf2UuACovVI9q2O7mMVr9yGb4NRmaq_vVkLGsy6-BkKMpi7Hya_w7pgpQ7QS2BzY43zvZzJ4KSp5Hs-w_zx-yONhBfEIgw8Kgt8VunU61euY9S045REGJaGiBiyhD1oCBkIVKkYyHkuQoTVIBieHpENJtfxdZPiSUbjCxsHGcIUbIi5fOSub9Rvs8ovZfKLhWX9E4GJfxd-Z12lfy2I9h0ZL4W7wYINYh4_e4DO2244aXqu46z-80OBKAS2FNecH4zRZWKbqIv27PIQgr10fKcCaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل الدفاعات الجوية في مدينة ماهشهر</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82597" target="_blank">📅 01:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82596">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجار في مدينة ماهشهر جنوبي إيران</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/82596" target="_blank">📅 01:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82595">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=JoQzg47215oJR6jBuQIbWxKucWeQzeSewh0xo7KyZ4odcfHlSCRSmum8NN5dXFlLxtvfIWOjMsADAGnKcoD0ePgNzrg4lD48kTrx4ok0nloo19Qw0ClhCMXN8SUzzH9gDzwYJDLJWN75lLcABgdJIy1o1SAkVVBw3IE6a-_Ws0Kv0cdgVVXLnGhFZ6SGSPjUf4JE52fmy2zBx0sWOLjSk0tqF1ZGA9E19Iw_Wy2iFfym0ss0Yaz_ccPiesAQKx8ICwp2qPIRuzoWEbwWO2WJnNbIBcoBQ-gS6WR5gjEYpBWggEHac9uhbCujQ_Ka-djvL15hw2uSw7egcovLsgPyow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/234339e6d8.mp4?token=JoQzg47215oJR6jBuQIbWxKucWeQzeSewh0xo7KyZ4odcfHlSCRSmum8NN5dXFlLxtvfIWOjMsADAGnKcoD0ePgNzrg4lD48kTrx4ok0nloo19Qw0ClhCMXN8SUzzH9gDzwYJDLJWN75lLcABgdJIy1o1SAkVVBw3IE6a-_Ws0Kv0cdgVVXLnGhFZ6SGSPjUf4JE52fmy2zBx0sWOLjSk0tqF1ZGA9E19Iw_Wy2iFfym0ss0Yaz_ccPiesAQKx8ICwp2qPIRuzoWEbwWO2WJnNbIBcoBQ-gS6WR5gjEYpBWggEHac9uhbCujQ_Ka-djvL15hw2uSw7egcovLsgPyow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انباء عن دوي انفجار في مدينة الأهواز ضمن محافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82595" target="_blank">📅 01:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82594">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انباء عن دوي انفجار في مدينة الأهواز ضمن محافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/82594" target="_blank">📅 01:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82593">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات في محيط مدينة خنداب بمحافظة مركزي الإيرانية</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/82593" target="_blank">📅 01:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82592">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjdnfoF5dwrKZh8uxrMxxWP1yIJW8ninrzFMhqzxyqyldNKbdkoYM1a8YKleI-Ic5xplSlAY-C1pm7ZaT2SwRt7wpNBtaT2XIugOc6PV_gMJKRNJAFs1li7AynYvQRUw9bE6qHgS0Yx389URjNNPp7Yhm4D63KbsCXqUVp8gbSaCEIMxCG1jzvFXMhH8JRR4Evm_pTLtPvijQQSw4GmMyiS4waQqxfMBbXz_5YNTpKRRT8nuHT4BM9rNyNsQIYQBecGb2tRZ07JSqIbPaYxpIT12645xUlKwP7EGvhQVjXFCPHrAQ_yXRo4ZyOB8Ocym-RTgz7SQVsOGW7l8i_dEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد إطلاق صواريخ من الأراضي الكويتية نحو الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/82592" target="_blank">📅 01:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82591">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">انباء عن دوي انفجار في مدينة الأهواز ضمن محافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/82591" target="_blank">📅 01:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82590">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انباء عن دوي انفجار في مدينة الأهواز ضمن محافظة خوزستان جنوبي إيران.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/82590" target="_blank">📅 01:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82589">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجارات في جابهار جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/82589" target="_blank">📅 01:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82587">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyJmJj5nQTTy5wRUa04fqyzG0nOVfAraUiX_SzKP8_KFNJt2h1JRAcFDLFFMAng5JmBJE2EIuPZSxVQuLpYps1r3WAnXgDF1hFSAAPtvmpEgYYzOL2wBkI91-rrRZN64U4aQ6dilYUn2xOMXw9IpFw-ytunCnN5Q7bGtI-5F3-ohK5s8QATTT5bBDTscaWHFsey5CFC-UZnXVLD7yu7ldjaZddBaPkLUyaMBNLubFseFk22aALUeG_W7US5mlXi0eAEeG-geR9UdKvvVPeBh3XW7nLIqEdDDwGgN5ez5uk019uRHgoGe_fLY-zbQELcEgxYnrlnmlwl_wxoRUm0kug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=MPIT-xjA9fIDz2ugLuHwusBrV17zwlQT_sAAqhCxxktNmmyhR-ZP4ZCpIhQ9OS3dbXOsSB04CvZiMzzWSmJh1GTZGLacdcNVW2eeJAhtr_PSjHrVgIOJunek3FN1zYLE5sZuCPqqczfD4WzEw0NuF9V9sqzerGXi7H3CIPdiLAvHoOzMSIMVtEtHTugVsqPg4x3UphksYGCdTf-wyeYeBV2lk7G0Wz1kRkkRWoih8e_ZMJ7hNtFvl6QgqJ2vVCvxEHbu85egs02JezT2lOB7yhPjvphnCYd48XqJxHIWNJZQOxd0IyZrUkG1Qmri-78cm82cm2T-Edm-0jP-BIZE9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5306540b7f.mp4?token=MPIT-xjA9fIDz2ugLuHwusBrV17zwlQT_sAAqhCxxktNmmyhR-ZP4ZCpIhQ9OS3dbXOsSB04CvZiMzzWSmJh1GTZGLacdcNVW2eeJAhtr_PSjHrVgIOJunek3FN1zYLE5sZuCPqqczfD4WzEw0NuF9V9sqzerGXi7H3CIPdiLAvHoOzMSIMVtEtHTugVsqPg4x3UphksYGCdTf-wyeYeBV2lk7G0Wz1kRkkRWoih8e_ZMJ7hNtFvl6QgqJ2vVCvxEHbu85egs02JezT2lOB7yhPjvphnCYd48XqJxHIWNJZQOxd0IyZrUkG1Qmri-78cm82cm2T-Edm-0jP-BIZE9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سيريك وجاسك وکنگان وبندرعباس</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/82587" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82585">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF2GwE9LixRjslG-fTqqmE0bzG7WaTdVhh3b2Yfh06SeXXWNqFmju1KSmZN9PvDTctOwBPnBvt4uHWZOfXM6x9-oPBURtSi_nLMDV7mQd_bwASXQrnsze-nKOZ95W2JrFkZzJk2QANpQyHwyEdvYIrLVFb0-64PJS_zUh3bfPldmTXLSBdSZFxzzabCOakdN_hcQVfGZY7b3VCRpK-1Dc69kMJoJLOVRmI9mn4vwfBHB2XIsG6tDv-5WEy8aTRPSQSHJdVQwTuT0hBawJgfUuWFJLpx4rQRG5vXmnio3kIOok4XuA3IAQz9ubydw2iQ1Fpu4SWd59l-F9zthx0KF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ طائرات التزود بالوقود الأمريكية تنشط الآن بشكل مكثف فوق الخليج الفارسي.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/82585" target="_blank">📅 01:07 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82584">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1d9hjQcgrI3pzoFaIpkykw_dqxFV103BOSy0-BdHBlbZu6NUjqnMPhX6ASWaQBYl6TSJ8pxQcOaayKj3hZazcjCU6XM8Pwo5R1QYgMMuoUEdt2cllS4NKOv_7FMkrD6zLD5X4TnRfuDJMPx2UFqBv4ArlhrRRM9JcDeOurTJbFVCTxo_TlwfyCnMxguVPZnfZT4CH4tMU_orhZaCX7d4UJhwLuPb72vEXIOUwNVDgwQrq5Wv1RDvfPs1N47CAxf2hGiiJUiGpgB-40P97tAyKWEm8CjD1gziH3OlRHABw5_2Ek-qf7lNJ4nZzN9RoNusTh8hHmi8aGzU8nY6EgMYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
المواقع التي سمع دوي انفجارات بها في جنوب إيران إثر العدوان الامريكي والاشتباكات الجوية.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/82584" target="_blank">📅 01:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82583">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🌟
ما تسمى بالقيادة المركزية الأمريكية: ‏
في تمام الساعة الخامسة مساءً بتوقيت شرق الولايات المتحدة اليوم، بدأت قوات القيادة المركزية الأمريكية شنّ المزيد من الضربات ضد إيران لمواصلة تقويض قدرتها على مهاجمة البحارة المدنيين والسفن التجارية التي تعبر مضيق هرمز بحرية. وقد وجّه القائد الأعلى للقوات المسلحة هذه الضربات لمحاسبة القوات الإيرانية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/82583" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82582">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة قشم</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/82582" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82581">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سماع دوي انفجارات في جزيرة قشم</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82581" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82580">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05e93d3a70.mp4?token=l-qc6NpfBZF4qRQqlyGhARYNICMgQg_n9ye01Yr52bXH4LtlB9HC_PAq2WDZW6m2Y8XfYKPB9doU2AhGYM_YgmP9QL_8dxVJWeve0n22w7clUdKerjxRZSR8IKfR77igr-V4XCuQSNc4B22VkERB9yojFyrcOSXHGw1hk0u5Ly2eWgdMwLHfA2i-TFnR6kVb6xE7MnYChJ3EMS2ir5AIAnVW4Vq7eapHsO8zlIRzrWhR1UhtWyeBAOpLmXZ3VhkX_jDFG4q-urVOje8_mzP1MXX76ViTNV-jPb8rY6BmWK1cDI0eTnLaursGM_e7gteFO_WB6qpS0oha-yR52oY5-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05e93d3a70.mp4?token=l-qc6NpfBZF4qRQqlyGhARYNICMgQg_n9ye01Yr52bXH4LtlB9HC_PAq2WDZW6m2Y8XfYKPB9doU2AhGYM_YgmP9QL_8dxVJWeve0n22w7clUdKerjxRZSR8IKfR77igr-V4XCuQSNc4B22VkERB9yojFyrcOSXHGw1hk0u5Ly2eWgdMwLHfA2i-TFnR6kVb6xE7MnYChJ3EMS2ir5AIAnVW4Vq7eapHsO8zlIRzrWhR1UhtWyeBAOpLmXZ3VhkX_jDFG4q-urVOje8_mzP1MXX76ViTNV-jPb8rY6BmWK1cDI0eTnLaursGM_e7gteFO_WB6qpS0oha-yR52oY5-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انباء متداولة عن سماع دوي انفجار في محافظة ديالى</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/82580" target="_blank">📅 23:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82578">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00811a2e17.mp4?token=G8LevjGEymrLbCS-d3dUhWisYyrj8j4MMFD06UCmgzNL--d3ojY7nJGnKSITbiUJw9NcjXstzQc8hZ1GZRCTsI9LX9ZNY8CjtRxHsVfCHme9xGSRB3LKyq5wasHM6EYW_UjUNgQzMpueckVohm3LQ_luGBg3q38lP6U_zvAQI4KpAOjlC2xLgdPNgWSSlP4eivOGZAQSQ0epsM3nTOrCxRGmWOhod6C8UFjZuuYa4IdQzo8eR-Ej1AIXoFrmpkWIyAkzyoN6ZunhIYRWtNIlt6Mm23lDGB1ADjlDZ2h4Pz_hmp6OMY2oZ7QdZbR2wC2RHp-r1s2Wlditufzi7wSU4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00811a2e17.mp4?token=G8LevjGEymrLbCS-d3dUhWisYyrj8j4MMFD06UCmgzNL--d3ojY7nJGnKSITbiUJw9NcjXstzQc8hZ1GZRCTsI9LX9ZNY8CjtRxHsVfCHme9xGSRB3LKyq5wasHM6EYW_UjUNgQzMpueckVohm3LQ_luGBg3q38lP6U_zvAQI4KpAOjlC2xLgdPNgWSSlP4eivOGZAQSQ0epsM3nTOrCxRGmWOhod6C8UFjZuuYa4IdQzo8eR-Ej1AIXoFrmpkWIyAkzyoN6ZunhIYRWtNIlt6Mm23lDGB1ADjlDZ2h4Pz_hmp6OMY2oZ7QdZbR2wC2RHp-r1s2Wlditufzi7wSU4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
مشاهد متداولة لسفن روسية تحمل النفط تعرضتا لهجوم من طائرات مسيرة أوكرانية في بحر آزوف.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/82578" target="_blank">📅 23:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82577">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
ما تسمى بالقيادة المركزية الأمريكية: ‏يتم تزويد طائرة مقاتلة من طراز إف-35 إيه الشبحية التابعة لسلاح الجو الأمريكي بالوقود فوق الشرق الأوسط. القوات الأمريكية متواجدة باستمرار وجاهزة عند الحاجة.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/82577" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82576">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex1ujWY-ZerM9F1AC1alMGK51KR9QrFL7O6lpZNsvAB9d-wRToi8ycOHk4w8lOyUsOzhrw3ZqpTuQ6DBp5Utd-R19RCCM_rFT2ycQRcvxyx5eAwl_RqxhdQH5ATFpZYF8CgAKZL0uVhc3WFhiTHlznqqqujVeAquaIzsnfEf5P5iKgP24vJ3wUq-R63bXul9Pz0YBOXzLoIYOyl-owjXaEG7K2fXoqJrhGIac9IjN_FSMUMm8AR5inPY_Ji5upwu_yPwp9z3Fv2KdxDVzqL5BO-b6aG021nufQpGiKCeetG65rwCOHitmEbk0sjgBQ2_FGD6A547j2w84RRqi-Di7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائرة إنذار مبكر أمريكية أقلعت من قاعدة الأمير سلطان الجوية جنوب الرياض في السعودية وقامت بمهام مراقبة مطولة فوق مياه الخليج الفارسي قبل عودتها.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/82576" target="_blank">📅 23:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82575">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
مراسل نايا في إقليم كردستان: مشاهدة أجسام مضيئة في سماء محافظة أربيل شمال العراق.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/82575" target="_blank">📅 23:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82574">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
اسماعيل بقائي: ‏ينبغي عليك حث الدول المعنية على التوقف فوراً عن السماح للولايات المتحدة باستخدام أراضيها كمنصات انطلاق للعدوان على إيران.
▫️
‏ليس من المسؤولية إطلاقاً إلقاء اللوم على إيران لدفاعها عن سيادتها مع عدم محاسبة المعتدين على انتهاكهم الصارخ للقانون</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/82574" target="_blank">📅 23:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82573">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">AUDIO-2026-03-17-02-59-01</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/82573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">وما اعرفه عن العراقيين وعن فصائل المقاومة العراقية</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/82573" target="_blank">📅 22:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82572">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTlyi9c5E8zdcR0HA-Wl4tO5zKbxeNmdt0XVrLNv_0Y-M0P2SIcbQPNa7mR8q5QcqKUzlKgwNQkDc9uJhJ35lS7FpEO4tt4dNtGlxHNzBjfx2t7vdMZs1JQUqiUvJWVaE_fbO3gFtfxHKqpDH7veOeU2ka4K2KjmmcxSmH46uf98Tlzsow68JVCMiaVYWP6KNS20pI5GBiZDTWruGRW_MPzqMO4HPSjqTGELIdBLJnyseA_gq9BYpCnj-NZscTN0ZUHFf2dfiblwKUIrMEUFBvBUU-_Z61T5lmafVgh9GpZ2HeGYbGpKzgp-gSBNm-k8IjDTdh0ROd_p-krMoC2EgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
(وَمَن يَتَوَلَّهُم مِّنكُمْ فَإِنَّهُ مِنْهُمْ ۗ إِنَّ اللَّهَ لَا يَهْدِي الْقَوْمَ الظَّالِمِينَ)
​في الوقت الذي تواصل فيه آلة الحرب الصهيونية الأمريكية ارتكاب المجازر الوحشية وسفك دماء آلاف المؤمنين والأبرياء في العراق وإيران ولبنان واليمن وفلسطين، يخرج وفدٌ حكوميٌّ عراقي إلى واشنطن للقاء الإدارة الأمريكية. وإذ نعلن في المقاومة الإسلامية رفضنا المبدئي لهذه الزيارة التي تتزامن مع غليان قلوب المؤمنين والأحرار في العالم حزناً وكمداً إزاء استمرار تلك الجرائم البشعة، فإننا نؤكد الآتي:
​١- إننا نتعامل مع المواقف بحسبها؛ فدعمنا للحكومة في ملاحقة الفاسدين لا يعني منحها تفويضاً مفتوحاً في سائر سياساتها، ولا يبرر تمرير مشاريع ترهن مستقبل الأجيال لشركات ترتبط، بصورة مباشرة أو غير مباشرة، بمصالح الاحتلال، وقد ثبت أن عدداً منها يمتلك شراكات أصيلة مع العدو الصهيوني، وهو أمر يتنافى مع مقتضيات الكرامة الوطنية ويخالف الوفاء لتضحيات الشهداء.
​٢- نجدد التأكيد على أن استمرار وجود القوات الأمريكية على أرض العراق يمثل احتلالاً، وأن من أولويات الحكومة العمل، بمختلف السبل، على إنهائه وفق الجدول الزمني المُعلن.
​٣- نعارض التبادل التجاري وإبرام العقود مع أي دولة تكمن العداء لشعبنا المقاوم أو تعمل على مصادرة القرار السياسي وهتك السيادة، ونرفض في الوقت ذاته أي احتكار أو هيمنة اقتصادية على مقدرات العراق، ونحذر من استبدال الاحتلال العسكري باحتلال اقتصادي أشد خطراً، بعد كل ما بذله شعبنا من دماء وتضحيات في سبيل تحرير الأرض وصون القرار الوطني.
​٤- إن تحرير الاقتصاد العراقي من الهيمنة الأمريكية، التي تفرض سيطرتها على مقدرات العراق وأمواله، فتقيدها تارةً أو تفرج عن النزر اليسير منها تارةً أخرى، يُعد من صدارة المسؤوليات الوطنية لأي حكومة عراقية.
​٥- إن لا يتحول مراد القبول الدولي إلى التنازل أو الانبطاح لدول الاستكبار ويوصف فيما بعد أنه نجاح حكومي.
​٦- إن التطبيع مع الكيان الصهيوني خيانة عظمى، سواء جاء تحت مظلة الاتفاقيات الإبراهيمية أو بأي مسمى آخر.
​٧- إن تمثيل العراق في أي لقاء أو محفل دولي يجب أن يستحضر عظمة هذا الشعب، وتضحياته، وبطولات أبنائه، من دون ضعف أو رضوخ أو قبول بالذل، فنحن أبناء مدرسة «هيهات منا الذلة».
​٨- يجب عرض أي معاهدة أو اتفاقية يعتزم أي وفد حكومي إبرامها على مجلس النواب العراقي لاستحصال مصادقته، بعيداً عن الالتفاف القانوني بتغيير المسميات، كإطلاق وصف «مذكرة تفاهم» أو «إطار تعاون»، بقصد الإفلات من خضوعها للرقابة البرلمانية.
​٩- نحذر أي شركة احتكارية تسعى إلى استغلال ثروات العراق أو الاعتداء على حقوق شعبه، ونؤكد أن خيار الدفاع عن الوطن ومصالحه المشروعة سيبقى قائماً، وأن شعبنا يدرك أن قوة الموقف الوطني أسمى من كل عقود الإذعان، وأن سيادة العراق ليست سلعةً للتفاوض، وأن إرادة الأحرار لا تشترى ولا ترهن، وأن حقوق الشعب لا تصان إلا بالمواقف الثابتة والعزائم الراسخة.
المقاومة الإسلامية في العراق</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/82572" target="_blank">📅 22:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82571">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88ad999a7.mp4?token=OWxqF-ItuTfZPeR7DhDK53tnf5_DV0wzLlL-Q-ndcB10zDvXr4tsNePfDnpvEFsM0vp5T4PGwsh7RRuVIBkCFjalyr_uQkLPfTc6V6k5tBGDXAn1fbmG7WQ9zmG9-9ODL_ES6-s_SOxbqvz342W-tU_YaOvEA8pcUYYJphvGvozfDaM4-WyR_NuetypcsUMFuomEu7nPT91P9KO50PIIofCOnSThbah6B_XzD8d0l1ysouWO2DRQaZH306yaHEXdirCks5lxVGU6mBRQG7Zqba8xGubBXApkadpai3SxSzPhnE-GdC1XDyV8mVLarZiQepPgX1vzhyFo9zSVNpiEqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88ad999a7.mp4?token=OWxqF-ItuTfZPeR7DhDK53tnf5_DV0wzLlL-Q-ndcB10zDvXr4tsNePfDnpvEFsM0vp5T4PGwsh7RRuVIBkCFjalyr_uQkLPfTc6V6k5tBGDXAn1fbmG7WQ9zmG9-9ODL_ES6-s_SOxbqvz342W-tU_YaOvEA8pcUYYJphvGvozfDaM4-WyR_NuetypcsUMFuomEu7nPT91P9KO50PIIofCOnSThbah6B_XzD8d0l1ysouWO2DRQaZH306yaHEXdirCks5lxVGU6mBRQG7Zqba8xGubBXApkadpai3SxSzPhnE-GdC1XDyV8mVLarZiQepPgX1vzhyFo9zSVNpiEqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
البحرين:
في ختام مراسم وداع الإمام الشهيد علي الخامنئي(رضوان الله عليه) حشود من المعزين في قرية السنابس ترفع نعشا رمزيا للسيد الشهيد.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82571" target="_blank">📅 22:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82570">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHZxPzW2NkTHoMw3NV1MvgoeCV6Iu_uGD_l-vhPLTN-2Sxia5lbNiqdwv5SSr8Su5e2zjyU-HhhEBVW9Qtebmieeq-bl6n5rVP2fCL3NB7Jnvm0-rsWc_x74o-IQYyn7_w3Nn4mfJk42vUFdXIfJzL9LneIKgB31Jem19ArYpT9hnFS5IAZVtzVySff_5RefTcxDySyLtrWuhqTPyv2W3UFJrswOxyGuD5Fn4v0-5Gwef7o8GcFu4tF44GTGGxFBv0vR9-yORgQt7oFeb-RIm_jBJCDkcpZhpv5o6AKp2M5Zntiql04eVP5UREmR4As6y3DjHqy2wXFhARAL4lwKpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
Nato bases in west Asia be careful this night, have a nice night baby with love from IRGC</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/82570" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82569">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDLxvFaVXA-EZX0BhrTR-trmPnLKZJgrtPOSWeysWxeQpTZZ8zo2iejOsC-FabuR6grSa0ftbUD0qCreIumruZ91q2A4dEMi-n_aYbheF3_nOkojWFGMgqXLkiHjhvTq1l_mdTt0knqmmJ_n-LpF1WtvU_ZsuhMz7W_gcuHd7L6t8yi7hSr163DHGcRyi8tzSKC5ZGhsv1dEIZrpre3v8EgYvfqI3pbVY_GYtWrEdLZlTK2T5TYG-i_2SwxoVfX6hZL29uBad1jrwEcEGyusuEgSNXQsfuhDet8eEk1kL26OCtkcz3QCDzFdIt33euD3r0zLObuacAO-uulM6haKyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
تحذير عاجل  إلى جميع المواطنين والمقيمين في الكويت والبحرين والإمارات العربية المتحدة: نظرًا إلى ارتهان حكّامكم، واستخدام بعض المناطق السكنية في الدول المذكورة لإطلاق صواريخ أرض–أرض باتجاه إيران، ندعوكم إلى توخّي أقصى درجات الحذر.  وفي حال رصد أي منظومات…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/82569" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82568">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShGWPbk3E_QrPTY7F9_emUJ_UxV2Z3KxkLi7tAdfZIMtEPM7IpCVn9RHAjhN22VaFS63KdBWbb77A79pM5WpKdNNsFg-wekTvnQO2dlI8BiNi4gDKA0qZmKkYKIaBGwBnQtZGpfuf8AWaTsUPVhohX7VJ_Bya8TjvwPHgCOiudPfCpU2koDMD-gRplcqz11rvuCbH_9eZRzvw941T7A-HfBR2dhowA3j6nM51XFKGAZbpSIRP8e26Zjl4vfdLD1cQE5X8gL-KV_y_OoD1HXyiflKNAflx5rq2Q2wYP4_ryxnXpojDeqRF0Jvh4o4a9Rh_XfBfHoP6SlUiUxd--BbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
إلى المواطنين والمقيمين في الإمارات والبحرين، والكويت:  سيصدر إنذار عاجل قريبًا، ترقّبوا.  يتبع</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/82568" target="_blank">📅 22:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82566">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">طيرهن مالته عمارة
Our friends it's Iraqi Poetry mean we will fly our birds soon</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/82566" target="_blank">📅 21:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82565">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
قسم بالله
🔻
قسم بخدا
🔻
We swear by Allah
🔻
مونتاج نايا:
#شاركها</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/82565" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82564">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">⚠️
إلى المواطنين والمقيمين في الإمارات والبحرين، والكويت:  سيصدر إنذار عاجل قريبًا، ترقّبوا.  يتبع</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/82564" target="_blank">📅 21:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82563">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">رسالة هامة لشعوب بلدان خليج فارس  يتبع</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/82563" target="_blank">📅 21:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82562">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">رسالة هامة لشعوب بلدان خليج فارس
يتبع</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/82562" target="_blank">📅 21:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82561">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDDWMDEeeR-Xeic3D-YsWce5PZH09jt4NOEapfBauNbh1lsYde9MWQ3wZy3f6yBnETaKv4ecG0LQmWsECjQRIwP3LCpjKlLST31PebBNGIxxcJQWhnuTwDnRgc1hGNO0TMUGU6CkQ-bVXNdSm92OFFyNzF8NJYm4821bU86UQdZy8Xm3CKtMay1d3d8xQ17rz0lD9ZMZqZgbzzLddA8-6Ii3NuUOn74rIz-Gui13DiWO_vDOH9CsPkM2W_1pQZ840mGhtKn1NjkYmteiNe7sr_6t2ZHrAHZGOOJfnkfaesGvRQd0tt7JP-WF_gzkxXH7YI2GmM8Dknb6SYSdVGKRwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/82561" target="_blank">📅 21:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82560">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/naya_foriraq/82560" target="_blank">📅 21:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82559">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">⚠️
إلى المواطنين والمقيمين في الإمارات والبحرين، والكويت:
سيصدر إنذار عاجل قريبًا، ترقّبوا.
يتبع</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/82559" target="_blank">📅 21:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82558">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
مصدر ايراني ينفي هجوم على محطة بوشهر النووية.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/82558" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82557">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇶
سماع دوي انفجار في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/82557" target="_blank">📅 21:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82556">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5019ff156.mp4?token=Uk3mXk8Om0Xjh95hs2RQmJk_x_y9N1zQW5E7_DRNnoZW98pgimYQeg5lWyCc0Mkf-MYgshKU_idJwCgzrgPqcrvH-mBpdCf6otXInY4yEqoFtXb1M-cueaiMNMSeC35-pbJKDGAdK58NAOtrxZnkMHu-3pIEWsHYg6DwzWTYt3lfxi-fJHvziSNWraFEChu5skD2LXW4QAsH7ptxxfnIwphjHOASblyvXE9z1Xy8013YgM6_HAXMgPPMXOiEJTaISkb079ph-f45TTtXC1lpHMq_TsHk29CulYo7nC33ARAo49e6s94pjdISVJ08gYc0C04gSDvw9-0vQzlGBbbOOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5019ff156.mp4?token=Uk3mXk8Om0Xjh95hs2RQmJk_x_y9N1zQW5E7_DRNnoZW98pgimYQeg5lWyCc0Mkf-MYgshKU_idJwCgzrgPqcrvH-mBpdCf6otXInY4yEqoFtXb1M-cueaiMNMSeC35-pbJKDGAdK58NAOtrxZnkMHu-3pIEWsHYg6DwzWTYt3lfxi-fJHvziSNWraFEChu5skD2LXW4QAsH7ptxxfnIwphjHOASblyvXE9z1Xy8013YgM6_HAXMgPPMXOiEJTaISkb079ph-f45TTtXC1lpHMq_TsHk29CulYo7nC33ARAo49e6s94pjdISVJ08gYc0C04gSDvw9-0vQzlGBbbOOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليق طيران حربي كثيف مجهول فوق سماء الأردن</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/82556" target="_blank">📅 21:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82555">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
سماع دوي انفجار في محافظة السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/82555" target="_blank">📅 21:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82554">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔻
‏
اعلام العبري:
الجيش الإسرائيلي في حالة تأهب دفاعية استعدادا لعدة سيناريوهات.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/82554" target="_blank">📅 20:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82553">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فشل جديد للمنظومات الدفاعية الأمريكية في اعتراض الهجوم على الكويت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/82553" target="_blank">📅 20:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82551">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚩
SUDDEN ILLNESS  Lindsey Graham is Dead! Iran Lego is ready :) Who's next?  #KT
🆔
@explosivemedia</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/82551" target="_blank">📅 19:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82550">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/82550" target="_blank">📅 19:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82549">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔻
مصادر أمنية لنايا..   الجيش الأمريكي نقل إصابات خطرة  لمستشفى قاعدة رامشتاين في أوربا نتيجة الضربة الإيرانية الأخيرة.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/82549" target="_blank">📅 19:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82548">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/82548" target="_blank">📅 19:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82547">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سماع دوي انفجارات في قشم وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/82547" target="_blank">📅 19:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82546">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
مصادر أمنية لنايا.
.
الجيش الأمريكي نقل إصابات خطرة  لمستشفى قاعدة رامشتاين في أوربا نتيجة الضربة الإيرانية الأخيرة.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/82546" target="_blank">📅 19:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82545">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">الحرس الثوري يستهدف بوارج وسفن أمريكية مخالفة بمنطقة الكيلو ٢٠ بمضيق هرمز الإيراني</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/82545" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82544">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سماع دوي انفجارات في قشم وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/82544" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82543">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سماع دوي انفجارات في قشم وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/82543" target="_blank">📅 19:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82542">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سماع دوي انفجارات في قشم وبندرعباس جنوبي إيران</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/naya_foriraq/82542" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82541">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a466ec6027.mp4?token=pG8V17aZEgkCELXVUB8Lny0qKe8C11noU8iUJoz_dkCDIVV3VlnFNU38F4KLGhAPp1WtRjCDW2VSnhFXZEdzkVihfqsZryDwd0PJyMaXXDgUB8JuWgl5RpKZf7WS0u9-a8-aTxdBqb8_b4CfMTCYR6CduAK3U9yVBmz8cYKIWw0GiVzYVxIP6Ro1rEya6FKVXQU254lujufsS6zewR2pB4WfM4AAhTmawNv4_0auFdYWAmqFGj-EEGie4eNeA1KuTcEPsHJkr-jlSEVVeDmk0yM0lkCaD-P2E1btYRUQB32Xw0TgZ9XzMl7tMcARYU3fd03kjAge-yaKHTiGq1iM9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a466ec6027.mp4?token=pG8V17aZEgkCELXVUB8Lny0qKe8C11noU8iUJoz_dkCDIVV3VlnFNU38F4KLGhAPp1WtRjCDW2VSnhFXZEdzkVihfqsZryDwd0PJyMaXXDgUB8JuWgl5RpKZf7WS0u9-a8-aTxdBqb8_b4CfMTCYR6CduAK3U9yVBmz8cYKIWw0GiVzYVxIP6Ro1rEya6FKVXQU254lujufsS6zewR2pB4WfM4AAhTmawNv4_0auFdYWAmqFGj-EEGie4eNeA1KuTcEPsHJkr-jlSEVVeDmk0yM0lkCaD-P2E1btYRUQB32Xw0TgZ9XzMl7tMcARYU3fd03kjAge-yaKHTiGq1iM9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🔳
اليوم العب بيهم جولة..
من أمام القنصلية الكويتية في البصرة، المتظاهرين الغاضبين على إستشهاد الصياد العراقي يبعثون رسالة تهديد إلى دويلة الكويت.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/82541" target="_blank">📅 19:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82539">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9320cd179f.mp4?token=U5JF3Rqw0vkTA85p5exkK2D0Cz3V2op6vVdNVRW55560bAW8njNxRc6xmrv6Ze2Pjo93ExVgGuhCeC8bKL1kFJ8uh50N750Lp8b_kQQQRIL1JOrxNIUDe379q7tWiFI0oAIzazeUxm7VzWr9Njc_3itP9G1SJrvqZAUcJDlgauEiPA1M3ve4qC6nefpK4s2pCzNOp1CR4gT6jeLACWtnsj0J1qT7y7Nm48aEmliZxWJWh9v2D6Q1E84X6fQCgvPwRYMFlpPcHv9TSXyTn3StIyOcAjxwBSqndfG2RHhP_4mL51o1Vyou66K0YoAffPiGNBfSxHuphwv4l39W9XWSAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9320cd179f.mp4?token=U5JF3Rqw0vkTA85p5exkK2D0Cz3V2op6vVdNVRW55560bAW8njNxRc6xmrv6Ze2Pjo93ExVgGuhCeC8bKL1kFJ8uh50N750Lp8b_kQQQRIL1JOrxNIUDe379q7tWiFI0oAIzazeUxm7VzWr9Njc_3itP9G1SJrvqZAUcJDlgauEiPA1M3ve4qC6nefpK4s2pCzNOp1CR4gT6jeLACWtnsj0J1qT7y7Nm48aEmliZxWJWh9v2D6Q1E84X6fQCgvPwRYMFlpPcHv9TSXyTn3StIyOcAjxwBSqndfG2RHhP_4mL51o1Vyou66K0YoAffPiGNBfSxHuphwv4l39W9XWSAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد إستشهاد مواطن عراقي على يد القوات الكويتية..
مظاهرة احتاجية لأبناء محافظة البصرة أمام القنصلية الكويتية.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/82539" target="_blank">📅 18:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82538">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2KRJZ8eXY9TkE7aDdTHgwqQuiko2uX2oXq1D2Ero1sy7uhCsSBAZRuvej6qkT0_6E3BIxpepj687aZVcDteaQcSHDZRszoGua67QmLE7IHBDhzrJMsPb2-vwa7lVvoapRVHnxCUpS2gAEWC-g6bRAALPz89f3x3c_tHqkYdjc7pSCzsGb4E5N-UY84a30TUL_VUkYyJjuwZzg7_v1miOtkk2dFNvxRmQkjJbFkw0TIdFiNANGyMtW48BFhwdD08ljQeT7HxuchFSG6NUxCEJorfLGE3fQDqXuEBiNasE9wmB7GqWCSQTXTLbdV-wcwFs0D6XrKI-UlCIYBW23TosA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف مواقع إطلاق صواريخ ATCAM</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/82538" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82537">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43920ef29.mp4?token=bItAynIkWEYRJoqstBFa_mh1kFZKggyvHnfdGw8K3YvwjICZ7F5EvRxEr1icvQyGG3y23UG6JsG_AHfq7R8IXQa1_KHq3SufvRMuyZgvz3HZQclVNUqvcrkoQUqTEIdZLyFVp09dxCXKalPw0WQ_403dcZWV0XrFsvexo3_WrXUQYYuu9ycnk3RjjHiRRaxC5MMsUOy1plzO2N0vOJ1YAo3sFMDrRxdi6UHG7fyy5s1aGMMvyTqdknENBR4Wbmkf5BodaMY4dPgV6_Vcy-pg3kFODzbDboVcTNbdeq4bDFCTuadyy5pogE0E-XGmapOjSiAaK9NzDrGdj64y_Sf_pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43920ef29.mp4?token=bItAynIkWEYRJoqstBFa_mh1kFZKggyvHnfdGw8K3YvwjICZ7F5EvRxEr1icvQyGG3y23UG6JsG_AHfq7R8IXQa1_KHq3SufvRMuyZgvz3HZQclVNUqvcrkoQUqTEIdZLyFVp09dxCXKalPw0WQ_403dcZWV0XrFsvexo3_WrXUQYYuu9ycnk3RjjHiRRaxC5MMsUOy1plzO2N0vOJ1YAo3sFMDrRxdi6UHG7fyy5s1aGMMvyTqdknENBR4Wbmkf5BodaMY4dPgV6_Vcy-pg3kFODzbDboVcTNbdeq4bDFCTuadyy5pogE0E-XGmapOjSiAaK9NzDrGdj64y_Sf_pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82537" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82536">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/82536" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82535">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/82535" target="_blank">📅 18:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82534">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">استهداف مواقع إطلاق صواريخ ATCAM</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/82534" target="_blank">📅 18:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82533">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/82533" target="_blank">📅 18:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82532">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82532" target="_blank">📅 18:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82531">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇱🇧
بيان صادر عن حزب الله تعزية بوفاة أمير دولة قطر السابق:
يتقدم حزب الله بأحر التعازي إلى دولة قطر وأميرها الشيخ تميم بن حمد آل ثاني وحكومتها وشعبها، بوفاة الأمير الشيخ حمد بن خليفة آل ثاني، سائلين المولى عز وجل أن يتغمده بواسع رحمته، وأن يلهم ذويه الصبر والسلوان.
ويستذكر حزب الله الدور البارز الذي اضطلع به الفقيد الراحل في دعم لبنان  والوقوف إلى جانب شعبه في معظم المحطات العصيبة التي مرّ فيها، لا سيما وقوف دولة قطر بقيادته إلى جانب المقاومة خلال العدوان الصهيوني على لبنان عام 2006، ومساهمتها الخيرة والمشهودة في إعادة إعمار القرى والمنازل التي دمرها العدوان. كما نستذكر الزيارة  الفريدة للأمير الراحل للضاحية الجنوبية لبيروت ومدينة بنت جبيل في ذلك الوقت كتأكيد على وفائه ومحبته للشعب اللبناني.
كما يثمن حزب الله مواقف الراحل الداعمة للقضايا العربية والإسلامية، وفي مقدمتها القضية الفلسطينية وحق الشعب الفلسطيني في مقاومة الاحتلال لاستعادة حقوقه وأرضه ومقدساته.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/82531" target="_blank">📅 18:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82530">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f44f93dc1f.mp4?token=SAQ0BlkqoNaQMjb5fO4oYSqx2JM0t5AFwo2xejLBKKJZ15k9Fq1kn8sDdBoqm0wjNllCIVV4G1VkJGoIJuEDJxpLq0lek9jVLqTgr1VNuFL3xAjCOuPDD-RgxZvzL8w7eRzsfLMBH16iQc_rG9MN15B6OxNdAl8Up049Na-u3PlH5jkhUxFW4Ix98uDOowhvB4cPRzuJeU0wCeZzHZ2Hu_gfln-GJetJYfK7QSc1khu4_GqZphCmc3CbmyQsf_ybClzmFidcY6dgH90Qt7biLIW7sglUVKO2L2LBB5OEDF5jD0AzwGVOrGUt5LnJotxUzgprq8xYHGzn7pgaFE3fcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f44f93dc1f.mp4?token=SAQ0BlkqoNaQMjb5fO4oYSqx2JM0t5AFwo2xejLBKKJZ15k9Fq1kn8sDdBoqm0wjNllCIVV4G1VkJGoIJuEDJxpLq0lek9jVLqTgr1VNuFL3xAjCOuPDD-RgxZvzL8w7eRzsfLMBH16iQc_rG9MN15B6OxNdAl8Up049Na-u3PlH5jkhUxFW4Ix98uDOowhvB4cPRzuJeU0wCeZzHZ2Hu_gfln-GJetJYfK7QSc1khu4_GqZphCmc3CbmyQsf_ybClzmFidcY6dgH90Qt7biLIW7sglUVKO2L2LBB5OEDF5jD0AzwGVOrGUt5LnJotxUzgprq8xYHGzn7pgaFE3fcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الاقمار الصناعية..
تدمير حظيرة طائرات مسبرة في قاعدة الأمير الحسن الجوية الاردنية ولا يزال الدخان ظاهرًا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/82530" target="_blank">📅 18:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82528">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromExplosive Media</strong></div>
<div class="tg-text">🚩
SUDDEN ILLNESS
Lindsey Graham is Dead!
Iran Lego is ready :) Who's next?
#KT
🆔
@explosivemedia</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/82528" target="_blank">📅 17:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82527">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🌟
‏ترامب: مضيق هرمز لا يزال مفتوحاً.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/82527" target="_blank">📅 17:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82526">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7929df771.mp4?token=eG-jHoVDezZI1IiWMoYEdRZ1juZHDjarMVvJbJjhD7-C6_2CzlGyuYbpKEfblaLYi9A9xhnxAkX2qnXIQ5Nfdohs-2_O7GyFdWWDAIeHP3RMu_F1_Dbyd01f8hJ2eY6ZHzFRZ_cwtd2QS42FqMkHVKgZabP2SHa517RWAKcu8EjVsXgd_JlEfaRA1bTxR-nkRwBlV3UardeeMZtwAhEEYUSrH1fo7uW5EQXXk5d7xfiG5VjVSQduayBzqzeDo1BNpOJI_V6y3AbxqC1CpbUMSIsK-6jLGg8vfs5eWIMIaBNGMbIYRImBQU7ruaH8x3XnOLPGpxZH8yh-DePSXhEvZ6mYI1-Ea5UlLZXGerGooJ_XJYk6XmTzfAGuF1rhpdBdCVi-WcT83m8FgfNQwP77StoH5rn8AuQHHqHREa4zj97W4hj2LnDL6mPVZm0dul5udtH2Y_i0AQ5TG3ByU9lpdnSLyU8J7T6ewhkZB7PTjfvOTbEsDB6pnz-HZzZmJQXFyT9Bao_65z3_laoinr-Sv87rIdAvERjNBHQU03sR60wwp6bM5HVJGERERh6BniOhU2NpJZFGKmV0vh7Wa3YJy4TIkNq2-NURG8jr1QPe1fN1cZ5Ra1y4POYAkPNnzRL8rlr6ocheBPgCpFY5vT5C28YRVjYwfuZ2G1m-8ZBdh7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7929df771.mp4?token=eG-jHoVDezZI1IiWMoYEdRZ1juZHDjarMVvJbJjhD7-C6_2CzlGyuYbpKEfblaLYi9A9xhnxAkX2qnXIQ5Nfdohs-2_O7GyFdWWDAIeHP3RMu_F1_Dbyd01f8hJ2eY6ZHzFRZ_cwtd2QS42FqMkHVKgZabP2SHa517RWAKcu8EjVsXgd_JlEfaRA1bTxR-nkRwBlV3UardeeMZtwAhEEYUSrH1fo7uW5EQXXk5d7xfiG5VjVSQduayBzqzeDo1BNpOJI_V6y3AbxqC1CpbUMSIsK-6jLGg8vfs5eWIMIaBNGMbIYRImBQU7ruaH8x3XnOLPGpxZH8yh-DePSXhEvZ6mYI1-Ea5UlLZXGerGooJ_XJYk6XmTzfAGuF1rhpdBdCVi-WcT83m8FgfNQwP77StoH5rn8AuQHHqHREa4zj97W4hj2LnDL6mPVZm0dul5udtH2Y_i0AQ5TG3ByU9lpdnSLyU8J7T6ewhkZB7PTjfvOTbEsDB6pnz-HZzZmJQXFyT9Bao_65z3_laoinr-Sv87rIdAvERjNBHQU03sR60wwp6bM5HVJGERERh6BniOhU2NpJZFGKmV0vh7Wa3YJy4TIkNq2-NURG8jr1QPe1fN1cZ5Ra1y4POYAkPNnzRL8rlr6ocheBPgCpFY5vT5C28YRVjYwfuZ2G1m-8ZBdh7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إن نفّذت أمريكا تهديدها، وخاضت معنا مواجهةً من بوابة الخليج، فماذا ستفعلون؟
كان جوابهم واضحًا جدًّا؛ جوابًا يخرج من قلوبٍ بلغت الطمأنينة بذكر الله:
«سيكون الخليج مقبرةً لهم.»
فالشيطان لا يفعل سوى التهديد، ولا يجرؤ إلا حين نخاف منه.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/82526" target="_blank">📅 17:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82525">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">#ترفيهي
🇺🇸
القيادة المركزية الامريكية:
إيران لا تسيطر على مضيق هرمز. فهو لا يزال ممرًا مائيًا دوليًا. والقوات الأمريكية متمركزة ومستعدة للحفاظ على هذا الوضع.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/82525" target="_blank">📅 16:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82524">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🌟
‏
ترامب:
مضيق هرمز لا يزال مفتوحاً.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/82524" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82523">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pORMcEP-sTPaay_Os5zwijthinDABEKOVV8qnaUSPTii2DVRC6EFQ3Vrzj_hVrw72QL3T1-OBUckGAMMohxAE6N78UA_YtilqIw4cacr5DIK69_LYIwendns2oWLxYatUpq2FfJey4lNskWO5iIhtYjoxYovxWD4TYjXVoxJiX1J9ccvz5u5J93YSLoXx-qH_dLWoH0aKjj5e0wxCw2zbOgKU0uHseD-5hHBxlRwpXtxoB15KFKt0cNnsmJz0bL11vrXTEFXgVYG9yhV750n0PfVne1Hgd3RwFVODiqHVy7sgeI59cF3TYk1UvFktdZfZqHLyyIK2BOUkChWghzuMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة الاعلام والاتصالات العراقية تقرر منع ظهور زينب جواد لمدة 90 يوم في جميع وسائل الاعلام</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/82523" target="_blank">📅 15:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82522">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دويلة الكويت:
نتعامل مع بقايا الشظايا والمتفجرات في منطقة صبحان وذلك من الساعة 3 مساءاً حتى الساعة 4 من مساء اليوم. أي أصوات انفجارات قد تُسمع خلال هذه الفترة ناتجة عن عملية التخلص من الشظايا والمتفجرات.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/82522" target="_blank">📅 15:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82521">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">الخارجية العمانية تستدعي السفير الايراني لتسليمه مذكرة احتجاج بعد تعرض مواقع بمسندم والوسطى لاستهدافات بمسيرات</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/82521" target="_blank">📅 15:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82520">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
سي إن إن عن بيانات تتبع:
حركة الملاحة عبر مضيق هرمز تراجعت بشكل ملحوظ بعد إعلان إيران إغلاق المضيق.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/82520" target="_blank">📅 15:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82519">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IowVatH3Sq2T3vdJUu0_ZKDQLPKaKcTDWgQmv7FBxAbOrLAH3fr9GrIYAxi0fXX9lUm3D6xTE3tJKvrlDNui-SU94J6KRar56T4hRUu0LvnUQYC-OIAygiJ8ivq3vd4U4ks7wDJENZvH2v7Aabxe74JT6SJ83w7IPmFsZ_a9RWYRpWTpSAhuJc5_FLC75LPMwHcqhyoblOXkGiYQQxKA_MJ4PueQXKQC3G9bXPlWudaQCbzk8o6S94XoAM9Fq5Y00x9jQOIJRN2dmQRZpFtfUEDRLxbuZfeSvlbXRyRnf7LlyqsLgXT5d8MZXYjfDExtfxrqcYTh5l2SLvtymUCKzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
الدفاعات الجوية الايرانية تدمر صاروخ كروز تابع للجيش الامريكي في منطقة "دره" الواقعة بالقرب من مدينة خرم آباد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/82519" target="_blank">📅 14:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82518">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏الأمن البحري العماني: استجبنا لنداء استغاثة من سفينة تجارية ترفع علم قبرص قبالة مسندم</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/82518" target="_blank">📅 14:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82517">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">حدث امني قبالة السواحل العمانية</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/82517" target="_blank">📅 14:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82516">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حدث امني قبالة السواحل العمانية</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/82516" target="_blank">📅 14:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82515">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">المتحدث باسم الحكومة العراقية حيدر العبودي: الحكومة ستعالج نقص الكابينة الوزارية عبر الوفد الذي سيذهب الى الولايات المتحدة
لشوكت يبقى هذا التدخل الايراني</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/82515" target="_blank">📅 13:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82514">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNDPaNVrCOHR1CBFgVXzA08kMFhJkMT4T8MTdabBEsVUmAg-WTOxF9yHXTMB0DMopuJF7YHpyfLWw2B9f2M7-l-XcpEJglsbKM2pS-YPs1ZGKhr-QM4HBFIhI-1OpWv27qNZP0_qcurtI_KpkBjAJYl4EYhp0kOTFSIYw8qgIiabEkKHvYMQrR1ykuD1REKdUcqQEN2d_li3st_mZoUpo67XC6TOOYB0IWPc0dHgZrLIVt5FYE2HWRtdQM3o9xfLCxAUyzadYOMmpFAfRrogLif87aGgVfB6ZZZma5jW85WF7Fa3TF0iO3qMqtJ62LQLSR7MMAiOYgASsyYd_97xYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزير النقل العراقي وهب سلمان الحسني يصدر
قرار بسحب يد مدير عام الخطوط الجوية العراقية (مناف عبد المنعم) وتكليف (مصطفى طالب يوسف) بتمشية اعمال الشركة.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/82514" target="_blank">📅 13:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82513">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
محكمة
جنايات محافظة نينوى:
الإعدام بحق إرهابي حوّل ورشته لمخزن متفجرات ونفذ اغتيالات في الموصل. الإرهابي اشترك مع مجموعته في استهداف القوات الأمنية والأرتال العسكرية ونفذ عمليات اغتيال طالت عدداً من الضباط والمنتسبين وقام بتفجير سيارة مفخخة في منطقة حي التأميم بالجانب الأيسر، أسفر عن استشهاد أربعة مواطنين وإصابة آخرين عام 2021 وشارك في الهجوم على مدينة الموصل، واقتحام سجن بادوش وإطلاق سراح السجناء، وقتل عدد كبير من النزلاء</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/82513" target="_blank">📅 13:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82512">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">في خبر غير مهم
🇮🇶
وزارة الخارجية العراقية تعرب عن قلقها إزاء استمرار التوترات التي تمس أمن الملاحة البحرية بالمنطقة وتؤكد ضرورة احترام سيادة الدول وعدم التعرض لأمنها.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/82512" target="_blank">📅 13:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82511">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇬🇧
‏هيئة بحرية بريطانية: التهديد الأمني في هرمز شديد للغاية</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/82511" target="_blank">📅 11:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82510">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خميس الخنجر يعزي برحيل امير قطر
والحزن يعم مجمع روكسوس وسط بغداد و أجزاء من حي الاميرات و قناة UTV تفكر بنشر مقاطع لطمية الوداع الوداع عذب قلبي الوداع</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/82510" target="_blank">📅 11:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82509">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔻
تمديد حالة الطوارئ في جميع أنحاء الكيان المحتل بموافقة الحكومة عبر الهاتف حتى 28 يوليو.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/82509" target="_blank">📅 11:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82508">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ترامب: رحل السيناتور ليندسي غراهام، أحد أعظم الشخصيات والسيناتورات الذين عرفتهم في حياتي! كان دائمًا يعمل، وكان وطنيًا أمريكيًا حقيقيًا. سنفتقد ليندسي كثيرًا! سيتم الإعلان عن التفاصيل والترتيبات لاحقًا. يا له من خبر محزن!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/82508" target="_blank">📅 11:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82507">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5bAaRI9-FA2H1203497E3kG8hf9IlNkKR3fH53xCYFFQi3Kqt6YPJg2y_HP2b4gF-9ATQVN7_TIFWwIk-FtM49XPcJLq1TOWdHeERb-0eH0xt2S8U78W_gBOOhTJuX-E3TC88cEmR6YOi0GSHkA5NL0UjG49cJszGBok8cigEo-RF0aAWwVUmC41ZYRE27rf8HXqeFTuB-_K3xs-kCihEsMH3jem53APFgV7YmXlEubv7GeY_z21IArCa4jE81Vl2SsrsD1HJ9juXpPK42WtX1-KBmMFR_eutMPWubH54kSvdHIFJSK4w17ZNObxgGyoriDgOsvdYoaTvqRxj_Suw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب: رحل السيناتور ليندسي غراهام، أحد أعظم الشخصيات والسيناتورات الذين عرفتهم في حياتي! كان دائمًا يعمل، وكان وطنيًا أمريكيًا حقيقيًا. سنفتقد ليندسي كثيرًا! سيتم الإعلان عن التفاصيل والترتيبات لاحقًا. يا له من خبر محزن!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/82507" target="_blank">📅 10:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82506">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز البحرين من جديد</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/82506" target="_blank">📅 10:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82505">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a42f3b66c.mp4?token=OaE4O2wIHefe-VbXChIUezFrwFSoLZQzwhMcR8xoInUmqcKHYF7MPzMoerFLItjHb06K23_tnV41zRfJ-Ts_W5J02QNOw83mT3BNBcoj3Y6-HAZAvM1DUMpCVshhWV4o4cIOPUYhBxONDcj9Z_Z8ukVn4ZaEi4cj6pFG9ey0_RArmOI1d3OwT1TWKmO10nm3z8wqWQlobIH8tDNlVzgD9YADZRITX6IzDgxmX8zGYN82oZh9eWteJl3NgeVaZO1V7EbgXCfI0m8Lfe0dw7lONOb5ZeMIs26cXiYlVwoNcY5T0HfpD_4dEibTMBGB0e4AnQC4NHnMaMMhwzBrlrZTaJe-IVnZ4kj8KEyrY2T8znceC3MYFBPClDNOQe-1qQ13aFP9TY_O7FUtDL9NL5_fUGPYpl3FZjraZLKmsmL7QuJBQoZi5Qu1c_9HNjPRPXexM2Nb6xUtiOA-TiXba7P65oBrSEgHa5ZFWn1PONTcS44Qy4CDmo8NnMZDZPp2EPKa2kypsGdZvhn5edk5oY6sO7f1U2rCxLDXDQfkvY8hsJ7umw7sQ0bMnD_sTpvj81vVr8MMkRVrWNd-NEt03tj42uJeqfyRa_oCBonuRFLVy4v_3ztZlW4q3Ee4fuQMYyW92O7OCBbZiJbQqVjXTSb5nCel_-H5yg0N4f41S3AaGiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a42f3b66c.mp4?token=OaE4O2wIHefe-VbXChIUezFrwFSoLZQzwhMcR8xoInUmqcKHYF7MPzMoerFLItjHb06K23_tnV41zRfJ-Ts_W5J02QNOw83mT3BNBcoj3Y6-HAZAvM1DUMpCVshhWV4o4cIOPUYhBxONDcj9Z_Z8ukVn4ZaEi4cj6pFG9ey0_RArmOI1d3OwT1TWKmO10nm3z8wqWQlobIH8tDNlVzgD9YADZRITX6IzDgxmX8zGYN82oZh9eWteJl3NgeVaZO1V7EbgXCfI0m8Lfe0dw7lONOb5ZeMIs26cXiYlVwoNcY5T0HfpD_4dEibTMBGB0e4AnQC4NHnMaMMhwzBrlrZTaJe-IVnZ4kj8KEyrY2T8znceC3MYFBPClDNOQe-1qQ13aFP9TY_O7FUtDL9NL5_fUGPYpl3FZjraZLKmsmL7QuJBQoZi5Qu1c_9HNjPRPXexM2Nb6xUtiOA-TiXba7P65oBrSEgHa5ZFWn1PONTcS44Qy4CDmo8NnMZDZPp2EPKa2kypsGdZvhn5edk5oY6sO7f1U2rCxLDXDQfkvY8hsJ7umw7sQ0bMnD_sTpvj81vVr8MMkRVrWNd-NEt03tj42uJeqfyRa_oCBonuRFLVy4v_3ztZlW4q3Ee4fuQMYyW92O7OCBbZiJbQqVjXTSb5nCel_-H5yg0N4f41S3AaGiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صور لمهاجمات اليوم التي نفذتها القوة الجوية الفضائية التابعة لحرس الثورة الإيرانية، ردًا على العدوان الذي ارتكبته القوات الأمريكية الإرهابية في هذه الهجمات، تم استخدام صواريخ باليستية ذات الوقود الصلب والسائل، بالإضافة إلى صواريخ "قدر"، و"عماد"، و"خيبر شكن"، و"فاتح 110"، و"ذوالفقار". حيث دمّرنا مستودع طائرات MQ-9 الأمريكية المسيّرة في الأردن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/82505" target="_blank">📅 10:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82504">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
سكان المنطقة الوسطى في الكيان الصهيوني تلقوا تحذيراً من إطلاق صواريخ والسلطات تحقق مما إذا كان خطأ فني.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/82504" target="_blank">📅 10:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-82503">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔻
سكان المنطقة الوسطى في الكيان الصهيوني تلقوا تحذيراً من إطلاق صواريخ والسلطات تحقق مما إذا كان خطأ فني.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/82503" target="_blank">📅 10:28 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
