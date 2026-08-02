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
<img src="https://cdn4.telesco.pe/file/dxjWttm1eoD7zvH2Mb2Uw7FZ-8PkdNfpiViSv_GRNxSYrbP3suAn01wluDKPcu7rJ0hGvSwteZGH1xjXW1Kfm-2QI4q00AN9vUC-MItuVyXFhda0DE59wXlQwG1IHHMy3NDWdfwRFfBacrr6mxrQCGcy8jcjxURnFqZBdRlQ9EZcrl57kYXveMEkGne0mSAmR-Z0EnryxOGI8ti4GBLUK1CeUv-kuwnPQIznEU3WqLjsnh3BU_LR5EG9x1oKN0yIm6fma-vSDmfDR__fSOfFIg3BqCKTsju9tuk39dnvcKqdKNNWLCBdIJy6wWfqSY4LYtHRhzR7KUl8OR-tbUOUdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 621K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 16:02:47</div>
<hr>

<div class="tg-post" id="msg-27002">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlmPw9jeHSLC-WcaYBm19hmevwkjdXY8qkGX_Y3i9o-HL6vPXBBHHVxGi7sLHXuzUK9vzK8qQbbXGdHiXbZoK4Y9aZYy3gfk-RdycjzUgMjzRpnqZUGuO-UZa9IiBQ0MBPnT6fwgoDqrq2X64KpQmMMhUZ8rBzjagxHuunBMcUMMLDJ8YJd8tTDBZApJcukDOsWCZ1GyM3DzW1t_NlixHZgPgZY0rz6oUpADsxOiXs-jHbMIGHtDldO4UTvsygWLTzdG9_59pOTM8Kxn-Cm7Hdghr0f0blAaw6m4KTcasp1Mde2OeIDQJQ6QCefdzUpFXuutr0lM0lIaOaINoyxmgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💰
گران‌قیمت‌ترین بازیکنان در فوتبال زنان
🥇
آلیسیا روسو - آرسنال ۱,۸۰۰,۰۰۰ یورو
🥈
خدیجه شاو - سیتی ۱,۳۰۰,۰۰۰ یورو
🥉
الکسیا پوتیاس - لندن سیتی ۱,۱۵۰,۰۰۰ یورو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/27002" target="_blank">📅 15:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27001">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTDNcPC55xa3RzZtmDxAyxZgOf9hX_Srpv_JVKpiLg-WGp-FJSN7IFVDTr8ZWt-16mVrOFjlIZvEZpMhTmGtOCw6OP85sGbx9w2HTiZ0C3JHXf2ajapcdTMgHjUzATglpGUNpFFrgi8z3XAykGKralLsDpIEz91CRW95ADdQZW5evVI8zhUE65uDKOQeKMftiNo-pvl9ZupXgjnMNv0AjmhF2t1Nj-ubx0ugeT2o5Vwg2yNK7avePlzO3C9UxbkA8bXy8JA7XQ7RzexnzLCYCwzhEIKvkqsh2nnx5stNbwQD9kQzzfrJtUN62MQJ1lHQXGPI-mm5wskp9m10k7jt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/27001" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27000">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp9nLHpIPhYJxCh5Bj9mvGk6ELrofafm1cq-vbbGTE01k3i5B1fGidTN2pc9vxqqEQmvhS28r-lDodMgso8xHGP3cFgQPM5PrJgvNKTZeJuim4QsKen14u0gZn3GV4CehRNSlXyrP40mqRxvZAul9i0WMmpq_XutU8kPjs84_4WcWKgQe9kSWlXbM7DMrI9wCZAOEIdCeJEZelxr9tt_9ItbiGm29ptSbZda12iFLG0R1qB4_UduA8OTHsEga-xVp8N4J7TIVoyCfVgi5W24uO0X4JNy7dz-huDTKaRKBuUaYeC-gCJbV8NRawgO3Yn5ZqMubLy7TgaJzxCd1h2TzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/27000" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26998">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPywgJl4AXlkBKlO9vCsKscbGDP1Xj-SQlZuyhnjSmtx8r1pdfkdUyn6tTWrLhn839BR495fT9b_-PqLrO1yN9WDnFpqp0ZrSd3tbWSViE6dvqus327bj_nBsMlmya2kUOdZQQ7R3U_IkyYyJT0zUprmrtxMzFvhPZF8AfoJoxcZ1_Ccj4COujImkbGwzqF_4Lm_5WtetSQhneexraSaArlquEpifp56BTTfIoUHpKyLUnKQ1ucqxY2B8zJNLnEYupTW5hX33qfjddcBUeKh47zHAhAAD6zW6HS64CJKA7vsy08_H-FpBzQLaCmNASpbjWywnCl6j6Xg2_IRBopppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCaFHizyCYbDyB7059VA0AS6eoxVTVb2fHJfM4CXVLg6_eE9rfHMg7YKa9WGGOGeZgMxDm6CzcDHGIQmz5fz5Ltse-HY6hPxbTQA8kIEEflBfXuaPppOO6asrJmjYZU2EuXv6ne3OYeAW4eyiyQUWyuM97V5W87Ec9T3iGayGaLhTFti7ir7ZrDStCYrbQBzu2xtLWYM9hBw4GooxFmUlcaQXUIfbZN70_DDAsNZ7C8umoLt60fV9mri0InWWGb9ZAoMbAlmylIrfUGx1nL7gJdMXFt6FHFyZ40am4DJS6GeEVAW5rcyJmuQsCELKUv0CmXWPPMR7teCuEHPvxU-hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
کریس رونالدو و جورجینا میخوان‌؛ مراسم عروسی خود را بعد از مسابقات جام جهانی در جزایر مادیرا در شمال اقیانوس اطلس بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/26998" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26997">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDjI2zW1drL50oMAt12zluMJsnpT61iV3j8KLAwZ6RhiAChPCldC_AABKU0c9dYxTCwJ3JuBVPpEfS2UlvRaQZELsVrZ5cyq7Fmvh_UC0-tcYaALitj3kUFNTBdajP5yNH7jr7C6SqC1SYncokVGkK6ShEDKgrsenPRb5ZKN0Gq-sKHAi6rzodu2D93Yo4Qxc_F8bFW3R8rTHFIH_aNUj-USbxYSFFDLqA-S47xfwJpgZPIiQjRW2bu19khnHJ-IPZmIzoKzxSiyh0_LtN0RhnbUhEpJch37Nc7LpICJ43ll92vVIJNx61EyJq2a3r-n7K3h7i1_DiaBD63uhsjp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اینم از توضیحات کوکوریا: خیلیا بخاطر مدل موهام منو مسخره میکنن اما دلیل بلند بودن موهام پسرمه که اوتیسم داره، این تنها راهیه که میتونه باباشو از بین بازیکنای دیگه تشخیص بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/26997" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26996">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP8RKHHMHs4iwx5G59ANnqYE6lbIwos2f5mLf9C12i_-Ni4dZBMr7UPIlpPkNlBFKUaCwUiPVwc1a_j-An67RqjZt5un8u-NMgVMEYKxsPcflCwLB8fc2ELOIAD1QlxfYOB84m7Z2FhCU0qNRqhNU3lclfJ-0wWbtEPEow0midPIwGvRVfbUQZ-y15uWltRkrjebE0Dnww99OqNiij_G4pz9Y6Kgpu5Gcv6-R0vMYMHZNtojH2yLpPNrLd2BIiOv3XsoeyvyoQP9meV00QOCFFjC13Egf6eqVu5pWZHxkYVlntBLFGpWRgpHGc4oXAxDwpgqPh3mfkB1duaVzmLq_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس‌نیشیموتو بازیکن تیم‌ملی‌والیبال ژاپن که باعث خنده خود او شد؛ یه لحظه تعادلش رو از دست داد. بازی فینال هم ساعت 15:00 شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/26996" target="_blank">📅 13:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26995">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=VCwxrZtqkn_aCeGzsFDVMOiQkMpWWItU7KUGLuOfxK6UV68CA_fii18rqfDeBTgwFC-_OO2zHyKF7sTopwLuF-ZCkDa4qVhTbpVEfy2iruzo3zYgjZqjcCuctveyNc1KTBsV40IosFSomrqU8bxCHbfB9_fEuKuencp9fcpetvaEidSSUhMrq3Ggui_gMAANKSuHZOy4Ssqaw50nk6-kZGT7S-aYNysoGfXci5pEB01wHG_pO-3aome_DrMjkGmcmzaFfVNfj2UyXKLCYsw2647uB59_0U5CZrTgG-0nDJMYq3hyyFOsOiMWiZVVUcO_RFyq-Y7ehQuwnUm2oCaVkRf8NeJWUMxQlYJTNqr9idb0nrIA6vqePMksljdPP_dGjkLXLDcz4QWmrUarVQ2wYS9keNo0QeTG260sizeHTDYhxBJat9UG8qx0sExHrwWkDfNH0Mx77AyWJAGTggs7e6EUcX3pN5OX9KGdCa6LCw6mfVjseICqgQrI0j8EnIs6uDH9hPxLpiI-hGHR2XNcmjyVuYdgQQ5_yGF205U1HpGRhuS_4tlvBabWnq_WWzdibp-eTny-XKI5Sm7mRIVtxGmDkRvVmSGrA-hDnbR_EgWi3GODg_12zEwNOpzWXCU8aYJ8lZb3goXwRH7szxZdSFAmX9Ol3-T-da5sXm_lmCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=VCwxrZtqkn_aCeGzsFDVMOiQkMpWWItU7KUGLuOfxK6UV68CA_fii18rqfDeBTgwFC-_OO2zHyKF7sTopwLuF-ZCkDa4qVhTbpVEfy2iruzo3zYgjZqjcCuctveyNc1KTBsV40IosFSomrqU8bxCHbfB9_fEuKuencp9fcpetvaEidSSUhMrq3Ggui_gMAANKSuHZOy4Ssqaw50nk6-kZGT7S-aYNysoGfXci5pEB01wHG_pO-3aome_DrMjkGmcmzaFfVNfj2UyXKLCYsw2647uB59_0U5CZrTgG-0nDJMYq3hyyFOsOiMWiZVVUcO_RFyq-Y7ehQuwnUm2oCaVkRf8NeJWUMxQlYJTNqr9idb0nrIA6vqePMksljdPP_dGjkLXLDcz4QWmrUarVQ2wYS9keNo0QeTG260sizeHTDYhxBJat9UG8qx0sExHrwWkDfNH0Mx77AyWJAGTggs7e6EUcX3pN5OX9KGdCa6LCw6mfVjseICqgQrI0j8EnIs6uDH9hPxLpiI-hGHR2XNcmjyVuYdgQQ5_yGF205U1HpGRhuS_4tlvBabWnq_WWzdibp-eTny-XKI5Sm7mRIVtxGmDkRvVmSGrA-hDnbR_EgWi3GODg_12zEwNOpzWXCU8aYJ8lZb3goXwRH7szxZdSFAmX9Ol3-T-da5sXm_lmCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
۱۲ سال پیش در چنین روزی
؛ منچستر یونایتد و رئال‌مادرید درمیشیگان به مصاف‌هم رفتند که ۱۰۹,۳۱۸ تماشاگرشاهد این بازی بودند. این‌بازی هم چنان رکورددار بیشترین تماشاگر در طول تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26995" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26994">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=LQiuCHNvb2RBVqioEPOVBcKtprV5SGkgdKEGTiEaPK6nfbyxeDT6OZ3jipIp0GktgUCQH9FA9vfjOp3CW8WX8gJ83c_viAThj7OcKjwMz88Y-qq_sJaKKcPQrP5MhmJqfkKqBqTqgnvLma71LM9O6ugm_lvYE1ozHo6HSFUIYRrPi2ke896bv2dFadTzi-UUCrOg8tEBNQMkqSyHGVgJLm5STvTsGUWWrJrKO1Ld6jwKNLfw2mQLApiTlt_u9DPPRo78vFHQfq_BCZWsSzrlEaiePWabcq6D-gJGu1a8U8LkTxLjUELhiZEpmawdnGYb9PFeX-MBCiKPmpvCufTC0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=LQiuCHNvb2RBVqioEPOVBcKtprV5SGkgdKEGTiEaPK6nfbyxeDT6OZ3jipIp0GktgUCQH9FA9vfjOp3CW8WX8gJ83c_viAThj7OcKjwMz88Y-qq_sJaKKcPQrP5MhmJqfkKqBqTqgnvLma71LM9O6ugm_lvYE1ozHo6HSFUIYRrPi2ke896bv2dFadTzi-UUCrOg8tEBNQMkqSyHGVgJLm5STvTsGUWWrJrKO1Ld6jwKNLfw2mQLApiTlt_u9DPPRo78vFHQfq_BCZWsSzrlEaiePWabcq6D-gJGu1a8U8LkTxLjUELhiZEpmawdnGYb9PFeX-MBCiKPmpvCufTC0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
رسانه‌های‌ مراکشی: منیر الحدادی تاکنون دو آفر باشگاه‌های مراکشی، دو آفر باشگاه‌ های برزیلی و یک آفر باشگاه‌ های قطری رو به‌ دلیل پایین بودن رقم قرار دادش رد کرده است. بالاترین دستمزد رو باشگاه استقلال ایران به او میداد که فعلا راضی به بازگشت به ایران به…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/26994" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26993">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XezlMsPINut5WgkCLkPQ21uOOBdiQancF1TGyrCR0n2-HC2opYEFlW1aK7WunI7nPBVM3seBcOej1D-OzH3d9CLrI6MQdCMy5Rw0kM6hzhQPP-v1sYl16c1iiCZHAfoybDfOMoOH3CTiZz4V8iwVy4Yrq4ys-dy3llsakbWCoMSUGcmXbww52Mur5TMYzIZtUSrKNdCES2mXiPpl5A2wXaS_Gtare5jtwrBvmjuh6UFr6LXkH08uBRFGJeYBpmUqvLnzEH-azIjn5MgyO4jy2XBFZ23WT2SGDKS3mXSUQER9hnbAhtb9oMvSKgYmGrYieW7B8MY6yIBfJZ-aP98EUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دوران اسپانسرهای شرط‌بندی روی سینه پیراهن‌ های لیگ برتر انگلیس به پایان رسید. از فصل جدید، تیم‌های لیگ‌برتردیگر اجازه ندارند لوگوی شرکت‌های شرط‌ بندی را روی جلوی پیراهن مسابقه درج کنند. این‌قانون‌فقط شامل اسپانسرهای روی سینه است و سایر همکاری‌های تجاری همچنان مجاز خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/26993" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26992">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSUfSfYiRhSKt_6xThMTXAKEsSGuUfqmztwD6lMK6gGzjE-LD9NxMgNVLgjPLkr0f2uu4cLSx8LUI3cgkSW_xoklyN1RScL92s6oXluGb4DQv77sRiGvKHwAUGDSSTJV-6yzCuvZ0u6x2ViETDsa_Q7I5cAaayrrDLk71GX4Pi-8YkXMMSsjdtmpKd3RBe6TYks_Frs_ttltjKyh8MJx6SN9iWvx1S3uOOY7tN1VQqrhs_ac7DVUR1v1pA2wj0AUTnG_27S7sgPGgK1w7Pzyez_Ck_GiFWDoa3kSYJt1zIeediNWaKEGiCN2KCreDFSVdRULEi_qOnyfk08ZFpUKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
#تکمیلی؛بااعلام‌رسانه‌های اسپانیایی؛ فران تورس بزودی قراردادش رو با بارسا فسخ خواهد کرد و با عقد قراردادی چهار ساله راهی PSG میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/26992" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26991">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKuZwRjc89gCgwm_HK47ecVqg498Z-9UeUWrCckfhJ0QV8gnCnSnGG8MhN4911ievxw9z--ziu-GRvzlJtZoITQBju4KMUhcfRxcZ3NJT7qDH4kN7E5zst6Aw51JOwdMiu05oDOPir7ASIVByWiV7-jGamwO_TgUz_PH8F2Hj4usQcbcpxrwhJQ7KdcNBX7AtiFXBdincZ3TD03Zh_f_0VxwnUc-UEm3My0cv0ZoLsnYrYtuOIwV_wrnaD3pbjE38Q2GgayO83yp0M4Avg3hmHCblAyoS-T5BEIyObgVeemG35v4BXs5Jz_ECnSxdhl7jUS0DmsqSzbgRvnzkivxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/26991" target="_blank">📅 12:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26990">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdofmu1Tnu4tS1-2gStyKLk78GlRF7zTILJRg-_2vEbzYcnhbuZJTdyV20zRSNaRUUIxGMXxGa9ZWH9hudVBISDdlmIxGuEPtqMFZorPMlAC_0qgfNQm-Xhdy26GxZA7RUn6IivjHhTPLFSGTGa6MvRk_f9Kol4YOWX5lu-S_T3v0XKMiRzsjbpvNlo4on1SQZzoNA6D3hQJcDaKM3iB8IgH9MMYWxZ7GvIVq8G5y7iRA1xZydCSn4iddOw8igWAJPJXEUkYAr1vGrQGsXOo5CLiqOumzBSm6vLBzxTacrLt6MTJLAU-8W3npR_ZGIuZftxpMSlKRD_8FtG9Fu3t2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیج بارسا اومده صحنه سجده حمزه عبدالکریم بعد گلش‌رو استوری کرده و دقیقا تو همون استوری تبلیغات یه‌برند مشروبات الکلی رو هم انجام داده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26990" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26989">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58235729a.mp4?token=n_oHd7JeKOKIwaf1_KzhWHubmVePKkYBuKSDmlHRt2o3D8_rZvMLj28BOratuSdWTiuct_Bq-SKdIK5IE7aqFZXwTG7mJfDAFQdiRLuTjiuttt0yBrjPsXL76ZqTxLBeCKe4LpUqsT9qDaZrUxcHsRH5NWmRGIbKZcqXbdOXqutGMEfuelHY1uSGFw2szAcIvdlYcOZInIuG_K8WcghbwSdnp32g8JvySup9ZfOGPWj2W_WgQTZmWHIA0EKAyXDlOQv_Xc__Hk9CbnInrTM_ZASjzlt1O4rMlkgoNXz8375iMZjD8xfLQ_AEQEjO2slvLu0_yk7mLY9bFFYTUDEHDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58235729a.mp4?token=n_oHd7JeKOKIwaf1_KzhWHubmVePKkYBuKSDmlHRt2o3D8_rZvMLj28BOratuSdWTiuct_Bq-SKdIK5IE7aqFZXwTG7mJfDAFQdiRLuTjiuttt0yBrjPsXL76ZqTxLBeCKe4LpUqsT9qDaZrUxcHsRH5NWmRGIbKZcqXbdOXqutGMEfuelHY1uSGFw2szAcIvdlYcOZInIuG_K8WcghbwSdnp32g8JvySup9ZfOGPWj2W_WgQTZmWHIA0EKAyXDlOQv_Xc__Hk9CbnInrTM_ZASjzlt1O4rMlkgoNXz8375iMZjD8xfLQ_AEQEjO2slvLu0_yk7mLY9bFFYTUDEHDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/26989" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26988">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMNbAUW_Gll_jRUG0chSxwYwIQUOiIPdp6LTEdTl-qv-QIdx8IKA0dxGOMi_Ng9pDQCzoxOiOQ-ZW8_L4L9wk3KkY2hsuCp21tAPUG2Tupa1xg61wJKd9a9_S7Y3Nwpjn7xT-Pbg3hera-eevse2xq8mJ9KnOJpqBQHB3SkutOGqyDpCq8Je0C5pn5sMqImDXt1Q5xJNO8xxKkKVnZhkUGQxo8JAbD4sre2wSFXmY0mvj5x3C1wsxxEEVniLvEUuCZ34yI4lGTn-2f40NwpHgBCvkZhFvuD-13cqmDcPWra4jOlSFipVhZYrpA4QX-XLwLFfi28m1bx4kP7b9B78Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/26988" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26987">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436452afaf.mp4?token=ZiCbsiJcPUBqMhzAJeazdiv9mw9a9R6N2wTSHap2XxhmZwXiRjxRRQhIWKTepfxcfcPX6StAvxMgoN1eNkbuA5eG6NjDVJ1jeKFexj_ba3zDRwzbrK1I70ybXO0zGuPNXFB0QO_6lctjzZ85IJft8IUOqPHAZQvj4_SljjYSEta9DK8pfPSQMrIMATCgRv7rakU20LhV76-7yEG1_z-nyKfOckkop65-dPdowhgcbYy6pPgEZUzS1dSZ39xkg7s7B-96FGN6tSz_lD99DxT2_rvTMeF20Jjj463BDZrSsykp-68Q0ILugQHFmmMIiDg0EE3ERmbm1b2NqCO8oxqang" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436452afaf.mp4?token=ZiCbsiJcPUBqMhzAJeazdiv9mw9a9R6N2wTSHap2XxhmZwXiRjxRRQhIWKTepfxcfcPX6StAvxMgoN1eNkbuA5eG6NjDVJ1jeKFexj_ba3zDRwzbrK1I70ybXO0zGuPNXFB0QO_6lctjzZ85IJft8IUOqPHAZQvj4_SljjYSEta9DK8pfPSQMrIMATCgRv7rakU20LhV76-7yEG1_z-nyKfOckkop65-dPdowhgcbYy6pPgEZUzS1dSZ39xkg7s7B-96FGN6tSz_lD99DxT2_rvTMeF20Jjj463BDZrSsykp-68Q0ILugQHFmmMIiDg0EE3ERmbm1b2NqCO8oxqang" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه بازی فینال و رده بندی لیگ ملتای والیبال؛ فردا ساعت 15:00 مسابقه فینال برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/26987" target="_blank">📅 11:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26986">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9LbR0P1OExvy4EXKKPWFnimUZMt4s4yb4o4A0R37Zu47ExWkWHVbcIr38YtED-01uZTaWQGABzoNaZ-9tkPY8Ti3YswuXV_smz1Zc_l4VsLpsdMzqLclJxGnffK9H5RrjwYEZxouw9Dk96bOtOmYR5dBJaV4xr-agUcugovPrd2_3F5fU27667a9mbK-cac6-QCvBEgHmZAWafekQdPBx4yjymQWgZ1-J6AnVQ5NcUEwIU68itFfQwxETY-L0KBUS5LRBDIUZe-iAfacl34751dJUAc-oZSnX1xAflwrijtaVRhMhwN2trSGog6Q7NUeemLqsIdSZMXvSbLgBT_Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوری از دیوید اورنشتاین: وینیسیوس در حال تصمیم‌گیری برای خروج‌رایگان در ۲۰۲۷ یا پیوستن به آرسنال درهمین‌تابستان است. آرسنال تمام منابع مالی رافراهم کرده و بازیکن به این ایده علاقه نشان داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/26986" target="_blank">📅 11:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26985">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZ3EfO6TyY8da0zjuFEnH1cQsG8pJZEpqulFHLW1NoN7-FZqNKQ2i6lKBRmHDTnrJsAEm0XiknX-VelLbA4ykcQztEW4qmBUyJsK9re1b5DtJbWVpCMH9dFZ0_tLF8iEkNiHTp3BkcMuqWWtH6t7r_bynz6t0N5KXHEJ-Frge9NejajcC9vKeFypivdFHBqh44zKxF6ttCCh04o11iCDE_BoNJITEl6eFnmV-TtoSIb10v2J89IglOpsYHdwYOe2NHlvaQJ9Onc6IbIiRvir0V_9E2ThAhxWqMLIHq-lp31IHAICt_4GAPbVssXzfp39LZcxC0OhmI2YFk4yoSIYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/26985" target="_blank">📅 11:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26984">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12920f454e.mp4?token=ixsfrHmPJUIELMc6tnmi_G4mYurmZLFu_mv6nUyYP5-xjA3zn0SaZIcYHs5IOjuTPLv9_pq2ctKtRorp2I2u3flUIOyeALsIjNyzbE2-WBeDr377MTtxi3e2mV9XwarVEB2oAu3D-Uayuyut5Bhm7ME5h7LKP9PtxNfCzumkA3ubpEmIYJ9hApO5y5jAbhjRiI7v1iWU3c6F8qXvJ9GXZWYoM1sLKHRWCqkCriJSQ6pqnLkc3SQ1_0nWYfTpWiNcuxHMUz9O0RbT2q_yFm8i-0yg_3B4nBXwosbrPv1h9lVOlV1ydwY-SmT0ZRAf84mcKjjVoX9ACVutrlp1r-RsZGgm1iSLoMEn3wkvOC0FzynozBu1hJNCVO4rEyCOiVymB-Az8jn5EP0-qOn72LN1Wi_n0YTeu46UBFgTyFQNtY-MeI-tyb35ePN3IR6Th97xchyrHfmoVWFgnGwdrolJ0M4gj-v0tTS_7Jjjae3dGw1e5viy6aalzF9dlqpzFAiBP4A1fDCFDLyFow01zgmHqD-SxQFj-GAZtcq8RaO9GaqXKoA5tlZQ0vcZZcvG4ljRZFAltlsLtfEFqbEeUsP-HJ74OOH31UeFJbKjjAty5i4SFKVNlQsxPwfAWHSIX957BLVT1Ybx_HrClsfYniaPDy5aKcmvpjlMD1QJE7TlWgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12920f454e.mp4?token=ixsfrHmPJUIELMc6tnmi_G4mYurmZLFu_mv6nUyYP5-xjA3zn0SaZIcYHs5IOjuTPLv9_pq2ctKtRorp2I2u3flUIOyeALsIjNyzbE2-WBeDr377MTtxi3e2mV9XwarVEB2oAu3D-Uayuyut5Bhm7ME5h7LKP9PtxNfCzumkA3ubpEmIYJ9hApO5y5jAbhjRiI7v1iWU3c6F8qXvJ9GXZWYoM1sLKHRWCqkCriJSQ6pqnLkc3SQ1_0nWYfTpWiNcuxHMUz9O0RbT2q_yFm8i-0yg_3B4nBXwosbrPv1h9lVOlV1ydwY-SmT0ZRAf84mcKjjVoX9ACVutrlp1r-RsZGgm1iSLoMEn3wkvOC0FzynozBu1hJNCVO4rEyCOiVymB-Az8jn5EP0-qOn72LN1Wi_n0YTeu46UBFgTyFQNtY-MeI-tyb35ePN3IR6Th97xchyrHfmoVWFgnGwdrolJ0M4gj-v0tTS_7Jjjae3dGw1e5viy6aalzF9dlqpzFAiBP4A1fDCFDLyFow01zgmHqD-SxQFj-GAZtcq8RaO9GaqXKoA5tlZQ0vcZZcvG4ljRZFAltlsLtfEFqbEeUsP-HJ74OOH31UeFJbKjjAty5i4SFKVNlQsxPwfAWHSIX957BLVT1Ybx_HrClsfYniaPDy5aKcmvpjlMD1QJE7TlWgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/26984" target="_blank">📅 11:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26983">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=Zggm6QbOIBHgocokerjK_4B9vAUIHHi5Hj0TIFGZAmm0f74hTs6v39gjmJTSLXU_TICC1yQksvSAGk5sdTas0sQZZRmGaSu-bzS8rKAvLUSFa8eCCGJ5dXg98K0klGD54nwX8_9hgf3PlkQInTSoUdeFwgUeOFIhF9kBD1_nGqRbNd0NcnVzGRI7QN27h37k2lsTuOPYQceqT9iE-5DrGpt6lMBHDapmAVEvpoSWW2LJQdRC2tIr1ZRi5QA-L6ZNT0qsJqHNY-7CApvWfxftWTpH2P3G-8I7veJxI6B3hePv2BWTwOHAxpAihoPsRTxtI8DYdto_BqGxJIJAVeHgnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=Zggm6QbOIBHgocokerjK_4B9vAUIHHi5Hj0TIFGZAmm0f74hTs6v39gjmJTSLXU_TICC1yQksvSAGk5sdTas0sQZZRmGaSu-bzS8rKAvLUSFa8eCCGJ5dXg98K0klGD54nwX8_9hgf3PlkQInTSoUdeFwgUeOFIhF9kBD1_nGqRbNd0NcnVzGRI7QN27h37k2lsTuOPYQceqT9iE-5DrGpt6lMBHDapmAVEvpoSWW2LJQdRC2tIr1ZRi5QA-L6ZNT0qsJqHNY-7CApvWfxftWTpH2P3G-8I7veJxI6B3hePv2BWTwOHAxpAihoPsRTxtI8DYdto_BqGxJIJAVeHgnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاسمیرو بعد از پیوستن به اینترمیامی: اومدم به لیونل مسی کمک کنم که جام‌های بیشتری رو برنده بشه؛ برادر در بازی اولش برای این تیم امریکایی:  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/26983" target="_blank">📅 10:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26982">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKwYJQIGnJl12oqfnvmYxjYhkIp0SWTgwZPWbcka3LKHaP6m4S4xrs5kY9O4K-cTEHS91NijXifCZp4Bh73QLQODd9e3AvaVMiHwVGA3BR0w-EbkAhxTm6120WL926bcfLw0GVEsn7dwXtLnwxrwfkf-cXsH8EXNZ5jKRHFydb01zG7YlQIMLAlEmh_Qg4cl7iLiMvsKtVS7LG-bNu6uc0Eq1n6qI8Qv-wWDA47BkeYT68lOEEr4Ez_p2mXqyA-RcibLaknkV5Cw6_WYwZBsC0_e18qBtm8nEyKKm4a_wrXK-Lp-k13iigQCQp55O-emRoXa37hXdgkdoNbWPkQ_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شایدباورتون‌نشه ولی‌این‌دراز فقط ۱۸ سالشه!
‼️
«جونگکوچ ماچ» بسکتبالیست اهل استرالیا با ۲۲۹ سانتی‌‌متر قد، درحال حاضر بلند قد ترین جوان دنیاست و عکس‌هاش‌این‌روزها حسابی‌وایرال شده. حالا بخش جالب ماجرا اینجاست که پزشکان گفتن ممکنه از اینی که هست بلندتر هم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/26982" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26981">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=Chd79kauRmMx4CoYAaIAHBAyaCe1xDGbGV3-dN5ykq3r9BM-SqKUmmverFcjKtJB7OYb7fNRD6MpvGfpDvrwc9ZaNWZHt9ewNZb32xtjAwSJwEZh8-WY8BcSlcaDzdcjcsJhypVlXU6_iRFDgJS2lPN-LbdFWyUStvSumxfw_DbHv-YZYjl8r7D12gV58XXmKeaSkOS7adFV82Lm9_M4Q2gzN-gDZ0hsY5b3cSyQRMVsZalzULwgLQcKpjOJ53sQCKNFKmTDBNCiCjzt9j8BSWbPYDHWkl4CfP3TVWlYv5tHdpKDR_BVeUEOJrow0tyoNtHk9Zss4Z4W7M60um07Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=Chd79kauRmMx4CoYAaIAHBAyaCe1xDGbGV3-dN5ykq3r9BM-SqKUmmverFcjKtJB7OYb7fNRD6MpvGfpDvrwc9ZaNWZHt9ewNZb32xtjAwSJwEZh8-WY8BcSlcaDzdcjcsJhypVlXU6_iRFDgJS2lPN-LbdFWyUStvSumxfw_DbHv-YZYjl8r7D12gV58XXmKeaSkOS7adFV82Lm9_M4Q2gzN-gDZ0hsY5b3cSyQRMVsZalzULwgLQcKpjOJ53sQCKNFKmTDBNCiCjzt9j8BSWbPYDHWkl4CfP3TVWlYv5tHdpKDR_BVeUEOJrow0tyoNtHk9Zss4Z4W7M60um07Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
محمد نوری کاپیتان سابق پرسپولیس ملقب به جمله معروف و تاریخی "هرگز نرسییییدن بهتر از دیر رسیدن است" با عقد قراردادی یک ساله بعنوان سرمربی جدید صنعت نفت آبادان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26981" target="_blank">📅 10:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26980">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qr-MlHcZoHURs3YRxyH4_q7qfCtR5azhDFAM392zFo5bsweCCpEK3-B5NgOLdB5Peyk15S-8U2DfB2N9E1ltsAy4quVF3YjRfjUfY3rWq0looXYva2CowNOGi4iAzHDrBmf8NRP6VPcIVZcEtjoHgxAtDDWoszu7aNaAVs_sr7vfQyUZdclwRkkTNo3lBYvjHbLOpB55PTmcOZmFZ54xBNwOpkEbFepjax_quzybS7m5gvHGReAAVmXFb-iHkEGXWMZbrdGyMFk10YHzPGi3FFoqlL0hin0tXUOOUubmzesloUiT2d5rzVYw7OKPCw4DL_OELA-B3siMpfmDj7E_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رکوردداران بیشترین‌تعدادبازی درجام حذفی:
🔴
محمد نوری: ۶ تیم با ۴۷ بازی
🔵
محمود فکری: ۳ تیم با ۴۵ بازی
🔵
مهدی رحمتی:  ۶ تیم با ۴۱ بازی
🔴
مرتضی فنونی‌زاده: ۲ تیم با ۳۹ بازی
⚪️
پژمان نوری: ۵ تیم با ۳۹ بازی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/26980" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26979">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m920qkEA6wA7S9p5_sdJUIaTmqp-myCGep4aLlxfb5qlYed1crPlR3Pg60t-RJNS9DBU-SOonbE_YldJScAOhPY7-PTJGNBhbN9cwTedj6th8bHBLLXt4MXxEJBk4tEv6dbCdxtCwS9Y5ZUMqvveYkGYdHzTg3D_aikish_xcyxePSIPJfJvJ76NIlbdO7x3xaThFMNCGmyoFP8hEjhWZvuCr9EUHcFfDMy4VoyBGv05m9IN8WQBRYhAgWNNHKNE0qYgy-4gOitXLGI_N_V-AuxhzuE9VDbwRwTeCsdZzM2kbspoEY3FyYEbiPZIKJpjQWKEh7EZxZhew8Z1gvWQRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تمام‌برنامه‌های‌هوش‌مصنوعی مناسب برای تولید محتوا در اینستاگرام؛ یه جایی ذخیرش کن به کارت میاد. برای دوستانتون هم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26979" target="_blank">📅 02:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26978">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E10L5c_OqYjhgnAi8s3j3LrbbWWEmkCb-2M6oOMxUCVy8o-O13PYXtj4aAr43-2C7CnUTbNFKSarfXz2Rn1Cg7EE0nii8EzSX64Y7QqH3EjZiZv_iPiEvh-NiSFerWK7euWhQpAlWS4iPbGC1WoIkB9rXWEta9jAREoXCnxG624A4A8qtGIlM38DwwPJnmQyCGjANq0RgFz5keoX355i2BGVuhY60Zenyc050bVJEgBdHxvu5jm3ICRDN8HYONoTT7fdBROo3ED9DleWtr3CWLwUR-jm13x5Ff7RuwzthzUeHNy7pY75vHcAFFaaTF5qrucnz89BfbE6QK0kIkWZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دپورتیوو مونیسیپال پرو که به خاطر بدهی های سنگین در آستانه ورشکستگی بوده و به لیگ آماتورکشور پرو فرستاده‌شده‌بود در یک حرکت خلاقانه کیت خودش رو به ۱۰۰۰ قسمت تقسیم کرد و هر قطعه بین ۲۵ تا ۱۵۰ دلار برای گرفتن اسپانسرینگ به حراج گذاشت. جالبه بدونید تمام شرکت‌ها محلی و حتی هوادارصاحب‌کسب و کار به طور خودجوش اسپانسرشده و باشگاه‌رو ازورشکستگی نجات دادند وقراره این باشگاه به لیگ برتر پرو برگردانده شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26978" target="_blank">📅 02:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26976">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFlTkjgBGKXEdefTvvxj8o8dF6sXwJaS-7re12pPoKvsQhd4eVHMVcZssphQLUMYQgenq4c7TDb4cIt0YHiwW7SqDxxVMIFxBK-HAq6a_m-I1tfR5VfEGRKqQpCbTP6tuiLxmzgLLgCHuL3IKoJgHjhKvTCVLI-wyj1N6yg0MrYf63B6qxoTG__07V_fMlS9D8GVmmpDVu7fWZzQuiDik4cMaNHK0-XxH2CVxK2ivfdPJXe8otDepRb7bhLX0A74Qg6v57bh59vt2zQ6gJo9mL0fdXhVEt3AUuUkhc6vf4510GBXRkTAbb2NfujTEb3TzfZYWz1EIMQAlba1WdY8yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
بازی‌ میامی‌ برای بازگشت به صدر و دوئل‌لیورپول‌ولیدز در اردوی پیش‌ فصل!
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26976" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26975">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/namfBsEFqdZxMC9ANAziQL6ZzDOb2TqQXMf-vlBHT0nj-ZtyjnVKDzOzup5gTZhn8Bkhu9h7BYj8gGn3V_W48W49SiYSbFDxTV-UB03M8abn_XvuCxv6HIIEXtofQ7G4dNbqFbarjKSsYerR3J2_HMJRgT8HVJ_yzBto3seoqJJkRkfFhtK4T3ngmsGfMupnb4zIIiZNDIc1nEFY7I1whfhD3O8lRpimFj2mNC2oBHRciFVausj9mTH3wOOu3-PMj4bZcPRxhCPE9hl63Swoy9d9fXT0gBaynQC0USKiGuLwQi18gLrGWCMTTtvQa7WlibOK2XUywshMUaCjtIpNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برتری لخ‌پوزنان با سوپر گل صیادمنش تا توقف رئالی‌ها برابر یاران دخیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26975" target="_blank">📅 01:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26974">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QX1Ji_nYSX5FYFf5QvrKid0WdMFQxeUpmWnAiytD5hmJkZdNiP7GcC8BXX5P0xtjWxFQFKbExrF5b7NQCLf65REvDYtxFZCa_TdazQkYvB8b-iib-oSXCpIfYU3Zqxz25KQW7BoZi7BwlUaYMvW7JKPeb7A0KSM81uzdQnSftzqqilZPZxweTsbLG-WmMJvGiYg0d-9iBCa2TRIpAskkPhsu8T5A5tOgFtBP0Qw41nsQK24aU-VKUd5s6UnyeVtyEWw1gi6033qyhhbQ1m3Yw9LNUEz0K2bIbSaw68WLGZyd9DK3CTlT65eavrhmwkJSYTjhBBJQ9vKgWWTmFT93Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26974" target="_blank">📅 01:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26973">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOTA8Bu5H8UMT4uRv5sc6w8OGxBVV8NmNc3q0fhJNzk1YSPXPGxxu4fZH5fkfHKNBY1zX8D1WLPtKvPw9wLf2IMEcdyq_jupw8FtowyVXCk5vlfJAQcNhnZicthVatFf1uzY6i2-BaBBCBAm2ql_ZlcyTVGjL7wWc9j2vuqK7jhM4TJaJcm_74FoP193970Plf8FANTyWIFbS77a8GleLvXiSX9BBEQqLJgzPibK6Ikj1MGBAplxLbUOWrc3BQkqqv2MtzrzlWwHLnWF4dSpupNZf3ytF7jJi8wg2T8zav0BxPaz80X_6GqjgDyZfi7Ui6pkXAXHDRPocbHtzCrkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون مهاجم سابق استقلال: دوست داشتم درتیم‌استقلال بمانم امامدیریت هیچ علاقه‌‌‌ای نشون نداده. بارها گفتم برام بلیط بگیرید تا بیام اما باشگاه هیچ پاسخی به درخواست‌های من نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26973" target="_blank">📅 00:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26972">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXsQf-QfEwUw355lSPgnSTnVp3RZm7Kr1bv_2YSmu9E9slAOM2vBRUsamTmtN1NmYv6ykk6wKrFC6wjuJT8hDRrYHIB8wt1moa7MCnMtjVegxzjtd93qIZfoZG3W95Ho0pBufOlhWYmHPawePQvbSkoVc8j0nh0eJTxvJMW63elMYEAjGvVi9UiOb88lmeX6yggLQEld6OmrbhUE_zqM_8ojm0qAlBw9I1hEnhWP7kDdUHHDD48I4G5gWfqMC2tItSc8ThuyZfboSbHcp7F8bUo00qbseNCmv2axQNt_hKd3626LdI2ekM5Dn8NrOuNIqkYG2b6UviYZ3Rjy7vhhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26972" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26970">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhIbpPE6PLIdehsWdq7IhO_QCSp7sb1-YglLczv0wPxhzmRCBgzZE5n-l0i0kpMUknqiCn723I3_8fQ4stmYXYqDPx6TDA48nQ5evYZHAMUc1odnk4i4i0pBC5NFxZwAl9TGLbcvt14MQGta0QGGOUGXmife0qUnQwovGTd63mhC_WV546gJzjrOxLiAHQ16cZ_5xzQxGJsGRyjwvntH_UuCjHfoHEqhbDOXE29gBXY6PRk0qo2UWAtV7HpvA67wGeUN-uaagOOWMbtKlAF7vPNKb0LKpLsDQnkya7mqQlj4R1ChS_fLp5jMaUaZhxV_A5GzMlMWJZxIUb3RVQ7o7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HW8JcJop0fdjUhP7O2ZCEYeBFpNiGK4TM10YmO0tJgbrIkiPEikJZHXjYMeVzmm1xJj6oa_nomR-UgmJrMkzeAlNGQNoZYU0SyqSAIrdXwmxUp13qFNgqzh5tkI5KrhKUzVK-uD1FDdrlKubJa7Qxmndsfa-2fxXl_nt0sORhS-ZujlRFGk3SJUYhG8_FnqibCrdjDL0PukKxnToElHwNtAGKVg0jS99tqjLlSGc_rex6qHixgooXdynTruPxcgBvvWHiOjiaW2C1gUtiy3b-N3vFFTuYxkiIl0E9psEH8Qh2Z6n34H3vOBSl1iDR2ON7V6ynW94vkKZY8DhR2-21w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دریابنگر دخترخانم 20 ساله محسن بنگر: از بین بازیکنان ایرانی سبک بازی محمد جواد حسین نژاد رو بیشتر از بقیه بازیکنان حال حاضر میپسندم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26970" target="_blank">📅 23:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26969">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGkj0yp-MGBx2IaJGP7PmCZo_G-RgMhArGXjuj6mgNNNbG1KHIUBj4nYHROQ7iBW95kGXiMQDN6e4T1ca6mzofyWZ7B7F3n_iVr5vBoZyaBF1VZ0CMvLn9o9Sl4B6xKULw4kC8f6FC4sKA-OibgwmFPEIAtkyEBXpZKnR1IHfGXB5aleUJh9mPO2dm1RBeBrkpdv0msuB9t6UI8WZyZjFO1QrMHrM7188Oby_lHaZaXYp3ATEHMUYiK1GJsPXmd7SczIstBuIebr-Kl02iNK6qhNwvF15PB7c3scBhNt-85xFGKCDhepVfuCNwDxEmRL2dpEcq9qtwNiHvuEedGN7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26969" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26968">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJcGmFTgXeKGsArk0bLpQypS4TrFGYuiEt-dcAUkE_V5fHyfAXtQAXmIU3eyH5NhR4nfMGccWbEGi6iJTszlAma8G8YqmDoUKwNCXTL1CrKRw2Xtt7Os06wzGl0qp8TQA8ixEnBYcYkh6_1_iLUL9kcUu0K8fDbl-jptA1zYzEhthy619GQDSfLfCPF3OkpQIWefQClfyIFQiA7jMa9SfrEftM7x8jSjQyBmRHh8EqLaCpenbQ4SeQfVFYxft0orNx8Fm5h0wLEka4Q4ytOvKs0hSe9rcFhdcSXXPZGBmBiDZqayPu_xPbk5pPeC_ZHTNl04Pb6LRoJqhU08BhhBhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های ما از باشگاه پرسپولیس؛ علیرضا اشرف مدیررسانه‌ای سابق‌پرسپولیس‌بار دیگر به کادرمدیریتی‌سرخپوشان پایتخت بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26968" target="_blank">📅 23:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26967">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL4M4pDR0qeyngTH3G2rl5nXsujun4Qd2RrygoLb0CJJdSQ2q2i9MLpNx9M6WuchLfAM9fKE9TBMO3FC8Ot2AvWNX5HdTSMMCUknRnT2-izRVbllxRNULbLU1fgoWlQ9RkibDIY_yeoXjPeN7xyrkCSWwbNBnEmOTvaqkBYgI0If9FmftMVVuLZzzAo4W-qmq6MgEaI5aWAAVmxCWvkR8orRprbjS2mCToWlfPnRGNj6ouhgRSaEHc_80Yr1saH6vHLjDNMihwgwm2C7mBKbMCiOoc-xxYNAMbedfxCVxJg5Xep_oWDqe_f23ZCVit1-O7nFCi1l6mwbZe_9ID3s9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26967" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26966">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBoivn64JUdRZr2isyCIh7za7kdAZ6TnMFM9amcc7-dPW-OCLxcN-mWL6wIBlZVieoiC_W-KDuAq3wOXDw8-ZJa68yj4f7p3w4CgNdS61olk4cjja4Ol2n_OlyGdJKCXua2Tig3pvineSrnfHnz0MTIrKyoFo_b-2o1OvalXM-8OD-_Ae-WoZe0aMIfvEhJ-E5ONYmVJIVKj6kF3JrmqC10dv7XcJOC1A3Bc9G4_jwm0VOqwqY7GQ-dtbT7Xn_nRAQ1h9UyStGanJc_66QhttY5LMUsutMp56f0BOm33Ad7JA4KSzzUSVhlbR_DIPb3ttyNMybi_s53EvkLPCh4Trw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف‌شایعات‌مطرح‌شده؛ باشگاه استقلال تابه امروز هیچ مذاکره‌ ای با آنتونیو آدان دروازه‌ بان سابق خود نداشته و برنامه ای برای جذب او تا نیم فصل در صورت بسته ماندن پنجره آبی‌‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26966" target="_blank">📅 22:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26965">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW70BsjGJ7O1MFImFenjokgD-7Vf9ZTo9JitdhXIprOj6Y1TRr_mJAFCcNKoziSDK-PKr2LD13SgVplbMajXAMtbaxLVKWV_DXotIS6RB-LlPfcjlOKwnTEINf3OtDiOmOJHL1-Xy3s_zOfsDHhChFlUGhVKGXgtnA08Nwt_C0RSt7rA6CjQ10d3GeaMt4o8o60d8JYfG4kXq0Z184U2scOYytgQTw1qLgn7v757ToED7-KgEQJkN044vB9KYT8If0yh4itrsKoMVqyIHicd0eJ3dwahOinpIgWhDzOCvcbPifxMLhw87SiXcGOg2pLquc5cWNlqx2m-lACC4CQs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید شد...زهرا خواجوی دروازه‌بان تیم ملی بانوان ایران و سابق باشگاه گل گهر با عقد قرارداد تا پایان فصل به‌تیم‌بانوان پرسپولیس پیوست. همچنین زهرا قنبری مهاجم تیم ملی نیز سرخپوش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26965" target="_blank">📅 21:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26964">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIPqeXDYxBrS0iA2D4u_ZCig_AUO3ewbJI4TP-g-bfd7oB4sWoZxSfjJmxugwaYTuUaiQ5jcT0dB3061yjm0rd-8ReyvZl_eyOH4L3NQvazyQvdVxit60BmLZySaiNToa2JFR_cxM2qFhifuTQ54dSd51IoFWmnDADLGpTsN7-FqAL-Q0A_NAQLIOdTgnA_2ZC_ZqRtmOazeZz4ZujNHgh1AnxlCLHCO9E_sXMH78PoEmz906nRh-Z8Eo_0o8RJDMEpyj281GYJpOMr5SXGerOeeG5e7eonhkltY4to7VI5SAD5pl9EGS8aCHcq3d8ftoNfcutqCx_IkPsftIR1uVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدید
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26964" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26963">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLjGodyE8R1ZiMlBFrsE2Cgq0WtucCb9tGmxlOQsdZR4k3IKSxDsJsGONaHqRZjh3oPxiUecDaPiRiIOyewc0S54240tU1YKCEjfEkD-3F1yDABy76sFu0bo12KfE_GhK1PVyEI8_CeumSHwofUV4CP5gJ94jwfqZAf5s8xahp1WcCC3YY_9fUkz5opJP7C1qTBzf8dYHgwmunuKM6NdjVWuLX-dlpHq6qsbb7Hm5Rm2ntxkYaNa8CLpD02TeL_yFzkvOezJ54Ean-H1-UFouNKTh4-CMd4GvsN1zBE-ZZ8JzcS6dVkDy7lRnM6HuAa8884cpRWf3-x5cwJmcbKlYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26963" target="_blank">📅 21:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26962">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbgVO-znr2-E0VqSA4KErGpsdA1hoTm5fmhZLVrJyDGRFiryDkuAvRgSrmVZOkF1AOLlURhacxWzvRTtzZfWIVLFc0vvqPtHpxxllK0doYIgA96BaxY3pUX3oJDmiaB5yyefbFxy0ZpJe3ERMkhM-rofLDDbGHbq7bdFib6YXNbrMI3lGPN4alIbawA2aKRlbbIDtLfU9jY5vt3MFeABq5e4dEukcviDJ-e2KSf5V-i6CptmyTZi1b65yeOWmvvV2bLpID3tDta-J29Y2UbQ8ep5iZ1f66hk9D6-fV0F6E_VF7Tvr8voY3P6FyrcW0Jaiv7cTxdAFy2Sh3iewYUk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26962" target="_blank">📅 21:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26961">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipQ5ITNIWNnV_Uj4I87G2SFjoNbIB41kffpZM8qXPaHxNF6OJF9o0Tgvc2NTvDkjxPxmqCkLup9z5v4zZj35gzy1AuGhAWnh1QQfmvKLHcIOwVLyutmzmwC0rCr9blDK78k0qtgTG00rPACxh8xiD3dxKKre6A3jctprVeOgz6TPztwME-B28K421HeUbLW8Ysl4yFch-2pFLAPGpdvyapebhpzoTd3a_BoeNS63iLvY43OQ4Rgh_iKnrLnw3UQVj3WSRV_C2MJZWE1X91EQbLE8mTjiP7_MKTTUVKoXD4oEOSC0PPIppmvNzlBI6O2xS42CEYl8d483CiI_NR8DiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌ های رسانه پرشیانا؛ مدیریت باشگاه پرسپولیس امروز مذاکرات رسمی خود را با عثمان اندونگ مدافع میانی 26 ساله اخمت گروژنی آغازخواهدکرد. اندونگ سنگالی علاقمند به بازگشت به‌ایران و پیوستن به باشگاه پرسپولیس است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26961" target="_blank">📅 20:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26960">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOq_1iGhKLHvT5lFEWP3kNvZvlnkMyU99h2e_xui_rJTUYYGWWR_xA_Bre1MJMYdF9Uwzyxj0W4j7Q51yMQGqdLq8UCJqNFARkhKBjtH3DgmAQMapkPhBWL8v2lpwtn1L9Gq9P_PQ_cQXj7PpuVBzkOxTXgGAbqr_GSUXwdtv8KHOrPvckD-7MfvMpPX7jfiweHQXmx_Dh5tB0hECeIRAdoaFQ4sBmKyBnBi9Uhir0_00-t-ZRx7xGitHfOsPDCvqzYxVn_6wXhDGuBOaAUiKf4x8n_r-HYZXl16u4ESf4v1q1P45n3ytqt-D65MWIxvIwGNzu4HEITAKLm2QkAJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26960" target="_blank">📅 20:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26958">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=GLiFGNdzi-ogH9TrFru1o-zv6lBUQaEF1x8QZg5of9iZ611YAp7aDJqBL8ndwg4PYzgzDrQbSkM6FdtkIbPLWabQXEmz921bmzaCgJWGWc6bxRYq05udMv5IrF9d6eiJs7gXTcNlYk5XOgGQcBqpiMoA8TBwYgLJ1nEkyfMnBMdgwSxI3ufTj3fa_W2t0nSC4iR-0xnUH3_b8rKV69wlzU0nGFpvr59dFFkbx1njp334Jw_sGRvLOXM4-nC9D-lJqiCOVf_UmPBS-anPWPJTUkpzUjI9HyczPkxvNKZb0WaK_EDYRjQY0hZy1vOXe7MOdYRqqMcwux_FW2rtNGEKwn9aXXv2mD5UDmd-DxWh1AyEnsAirbLvvwUi18vhL0ilAQw0eELpeyTDF_92wxO-ZuqiLEiwTg7CMLeqQraOIe62_kTClxVwzboAaSCyiq4qznGvHtf_zcaSbI8JKpw8OEa1AbhUg-3BhlH2YH95HWiIPFvCwXfs0-9o9Mp45G8lVr8QAhwctSHEED_dAMoiZgXJT_-f7hJvIT4gRAo-JmvqBiCZsUafOpUB76E-YNoEb-i4ODNgs_wIZmCoP5hG6cmaV53acL943LutbYtIaJ85yXYkhIW6gdK-c-Mx5zytodbToMSad3kNQetbu3iHEKDQVlWjhjIJYxatwQnQtbY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb2a69728.mp4?token=GLiFGNdzi-ogH9TrFru1o-zv6lBUQaEF1x8QZg5of9iZ611YAp7aDJqBL8ndwg4PYzgzDrQbSkM6FdtkIbPLWabQXEmz921bmzaCgJWGWc6bxRYq05udMv5IrF9d6eiJs7gXTcNlYk5XOgGQcBqpiMoA8TBwYgLJ1nEkyfMnBMdgwSxI3ufTj3fa_W2t0nSC4iR-0xnUH3_b8rKV69wlzU0nGFpvr59dFFkbx1njp334Jw_sGRvLOXM4-nC9D-lJqiCOVf_UmPBS-anPWPJTUkpzUjI9HyczPkxvNKZb0WaK_EDYRjQY0hZy1vOXe7MOdYRqqMcwux_FW2rtNGEKwn9aXXv2mD5UDmd-DxWh1AyEnsAirbLvvwUi18vhL0ilAQw0eELpeyTDF_92wxO-ZuqiLEiwTg7CMLeqQraOIe62_kTClxVwzboAaSCyiq4qznGvHtf_zcaSbI8JKpw8OEa1AbhUg-3BhlH2YH95HWiIPFvCwXfs0-9o9Mp45G8lVr8QAhwctSHEED_dAMoiZgXJT_-f7hJvIT4gRAo-JmvqBiCZsUafOpUB76E-YNoEb-i4ODNgs_wIZmCoP5hG6cmaV53acL943LutbYtIaJ85yXYkhIW6gdK-c-Mx5zytodbToMSad3kNQetbu3iHEKDQVlWjhjIJYxatwQnQtbY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
پوستر رسمی باشگاه لخ پوزنان لهستان برای اللهیار صیادمنش مهاجم جدید و 24 ساله این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/26958" target="_blank">📅 20:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26957">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgs0Qd9-VzrxFrs6FHPjPRzIRw5QpJPhRTqhwNlQosvoVI0L_dg9fZ6MZ1YstnKOtWcBCuT2KDIH_PQyCqfy1k1rNbt_gh8xzDepKGIFoRo4RPJrvgEploq5TAkiJwmFoF3ZHviGALHLEJ9oqoS31kN6oZYmXNO65vDHv7Qyf4WxP-3SF1BMHrGjBfrdqCxJY2WarirIvap_O9n2KQRodJ6NI-PySy5YE-W4zLSm-WDN8AgEiaT4M_DP2SV3cftG3-H2CwXJ92Vl3oJnGJ56vJV-RpFvCzybRpEiBxmFBq_cbQYKoIYWCXCViFAXPiBHM4ztthCInZEKZyuLChAHzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26957" target="_blank">📅 20:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26955">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfDErY7x4m8eplMUlbzvYbhkuHilawZnr1pGjNkeXpGu0BG_tfPIObaewToDkbNSKIu4m2meL1WUBIlqEKdSxZbAA9kVPqVU1iAclnIsHv9rUF-rrzN8H6WJYfcbH22vJy-U3akdSkmwN3Xr1jp_P_3ik1LSNUa6Kggbwvqt5yhGh1Y9BVwDL72TMUGupN-2JFkMgwoZaLgC2b1VD8bi0CwaQxNYxVfkku2TtrkeOH4rZZEhLkcZfsoyaX4Z162tv8dPXtH_pJ2SOicsdeQBhjlT-DN-lZ9drmSOzR39Jh0k9ZWFq3cSVJR5x3BftuHO6j5LS-wxisYmUIyqy06eNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NCnLKJ6dzrNWYcaYIG5q2nYcUiOS46An4ktx-25VYySRf4SlsEZr4yn95uHgnF-GH9k0bXHzFS4l6YCzj9Vx51ogxBVGQws-C-5AAyMB7dS-jTEAH8xKA3W8-HqtJWOo5aguIpreMaCPteAHWWusN0JlVCG_9hayqcBkhygX5HzgY9XZqwINLOBTE_sCoS-T9Hk0HFxTqRBt5sxkgts6_8jPjPQVz8TkqPWlTuLpnZK3hweRHTH_WxJ3xK05Dqs8VCFUsOiHnvdrrYypV3IdVHniCQWfsczFKL0QHfQJhUCA-Tzg2ef-XN3rsQ1zDA_nPDTLVA0uLPu3l5H_RrTC2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📍
برسی تموم اپراتور های اینترنت در ایران. این‌‌ پست‌رو ذخیره‌کن و برای دوستات بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26955" target="_blank">📅 19:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26954">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-dEmR23PYm_wC-hGhFGDTVa3ovmMQKrLTznYxRCjETZL4lauEMyT8W6aePt9yT-TzyzNw6cZYBVaVp4Xs6c6NqHYChjR3es_EdMiuK3wAVstL2rDRJTiUGzPqUUGKh0fJWt_57vmoepiBGqTAjpDrEAA1V0hHYlhmSsBEt1Khn2rh8GqtHD97v8WgGpGMsQDa-UALKnOa30HnWHe7D-KfRoarYFAT_MzR3E6R6qP5Z1ZnnQ9O7bcscuf_adCu_NmXNRw5ARYyxkqK4OmfHqW4lxlePW4XFGloTymMYPSiKEYsPJL7s5M8LWQ-HVquAB43VyfC4NXOKM06PjfI4PFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26954" target="_blank">📅 19:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26953">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMD5MdQ7XIuCJrBrlLFagx76psu_i9F7Rap1Z7uRGfyQYyFlfe5MA-ByjX1XjXN5aB12XmAig_sErkNspN9Q59c0UOcHjmzt3ack-96pMYGbuGLhX_IHx7oxSe4kGuUkCMAaJXPm2WMEHaSlp5ZmtxUtTTqtNDH2ogQgSO14VaqoL_2b-XoCgvIT-gg_sA7AsMBv61pvktarRgPTY3R_P-OarJqdrXP99pfz7VCakAnJY0nAP8OJY2FMARPSteaLemcdXPExunSczTUP85GEVTamAifbX8aWIEPE2dpcV7TJh6fYWwe7EKzbJtcgh3safbNLzU08zYuKNEpjBlo4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مهران احمدی هافبک تهاجمی تیم استقلال به دلیل مصدومیت دیدار هفته اول با مس شهر بابک رو از دست داد. باتوجه به این رقابت های این فصل بسیار فشرده‌تر از فصل قبل برگزار میشه‌. اگه‌دوره‌بدنسازی‌خوب انجام‌نشده‌باشه دهن بازیکنان لیگ‌برتری سرویسه‌. هرسه روز…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26953" target="_blank">📅 18:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26952">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf02af4598.mp4?token=M-CX7UuEGKZIkDbWi0-ciAZ0cEJwCkOhr5ME2Hv5NgAOasA7Y6Ru6vkLj5-OhAl6T9QgWT_TpJET8IhXKOuxN2ZaNpyLdHwNGMHwnSEIFE3KxgY0ejJ16TMv0sJ6G5Imnjv4NQVQjq8MNzfQxiQirzUeZxfzeysJyAxUCskYAM228lYQ1ksY6HkuBBNtPIQUFsgZhZ7As0KyZxHU1Z-acqXN0YSbJxhxCsJxI4ew1GXZms20VBt3VajK44KN3SLoGu7FGyqjgZ0EvMEIBBbX6j1htmc_HE1RCN_XnoIKzoi6GdZpL4NRVKnZNNRmemsdCOAAYYyvvyzxii95uotKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌ ملی‌والیبال‌ آمریکا در نیمه نهایی لیگ ملت‌ ها بابرتری‌سخت و نفسگیر سه بر دو مقابل ژاپن به فینال رقابت‌ها راه پیدا کرد؛ ژاپن بالاخره باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26952" target="_blank">📅 18:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26951">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbUwnAscmcO_b8ea0OXyH0-xnoQK-llRi4FmK8yoPeeA0oZdplN2UcBSgqFGEBmgBj1HMuG7irczTukl95DKUoYSIqJORBZe82sQWUYoKjFqgP3rBpzqO_fUREpY04Cm4h_nfpRFUr6tV9KywLqdQvklcNFJLi8lLi-fa6V-srCnBlHpjj-A5gQNckzS4ceyeh_5Qz5VHiLCKkskQEozceeA4071INcHL4KCWAoAB6zpf3OeX5xAw4csOdALbzuYkIde-qbN_tbNgvLSigJ_dAXxPzYvaTPu70Fl3Z4o91QswZNANTC-0o691rqt3P8yOKzWLcLy-ApGKFKXbp7HeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/26951" target="_blank">📅 17:58 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26950">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab908f0eb.mp4?token=ASTE1FasX188jkZiuyTs-F0FK0BsO_cVFKCQQIB2JUIt_tQfVUTPu3Gt47d7Zb3549furKNZtGxGY60m51wBVdhZMb45vWW2In5pVY539PLV8PiSKxyeHSfM7ViCbxwLM4aAmYjfyJd0bULmZHqDwqGd-c0n48ICABV5XpcJKiEfRGxz_zpT5K49NjFIeQlBqp3r0goPyuxPHfg1bfxa-S6MClOcOG-WfV2LOuY7Pt0vIo4zUTW1OLox4LjJzozUJKbq4rbMqZK7rZHC_FVCEhXiii1DNa3NKaFviq5-_ycqvD7DxJspg1BGEhV5htD4HCpBC9v1_-8Ax765pVlMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی بدنی خیره کننده احمدرضا عابدزاده گلر سابق تیم ملی و سرخابی‌ها در سن 60 سالگی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26950" target="_blank">📅 17:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26949">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVNPF5ylIfHw6rRcCHblYkuAx1f4tdqALGOwWz-Pv8SmhtVYmHrggrtcwbx6ag1zMuxZFoYVIL3mvHjH5X9IUDKRNqrqwxrq_GZX_jMeyZUYvfQzmATi2X0F4FtToT09G4D5oDzyKehXww3uV5ogHFU2q77wD_gHMACMXveVaNkAZMKNVFbkdDC_lf6GTghalY2qdVSD_ZWjfJnnHgE1VaNEnelZPD1ggXC324BxqiilGr7dGz_aS_pv4shgdxEZQLAHlmfDyB5hiUpfy6Jc-LBz-3ezjuV3XjostusFuISOYqS-whsTfL9mSysDzopvqaUigoZLCBrpvxVQkFajBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26949" target="_blank">📅 17:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26948">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQNhnn6_P5sCQli5uZytMLWxgVap_1t5pt9xfVrUR2OqV3LhONyrXtZT0WvnaJDEqVLb3EVcAvJ3f2WUd2flwP156YvYyGEDj2x8Wmp41dL_CDscDPx6uP3Cfl2a9lg9xD5487lbNfTyl2fxkja0YEbKKo2neOAhpuQ2f_jyfqRpouQJfIJplZwFApVTnQNeICwM3pVit02yFYtKVqB9N4WysFYI_2-Ew5WnzUF05FA_1EL79toJfGJTkFqFQqnKNVvS1wl9Pq9vbtbgwWGqhG4ZWwe_dll3JOOux86l0dIkk6n37aIlpZtPkPrakRjxvogks4dNzWRJnefRPGgvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26948" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26947">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3XPZChWv2TYjxTnrvlhhZuuRH4m1HTX_CuZw12ZFwobKCO41195qaQDpYSiMFPYt0g2fHwQP-QRvTrZlXfy9kVU7wSajBvMRTqTr-HYGdYY_B8AzITX0JsuQ-EvOYYjy5bYSedcPSe0pr5csG8WOjT8NnxskyIoMkBwN4IRZfbFFW16jzHji-fOQXRTEIh6FU8AtTc9rTH7b1d9lZEwGLyL_AGz0tghN0zxSwAyTXgDL-XqW8cLaZtAqOW2kdu1Xh7r5R3UEkezwCoPdmoejbD1Uc9h_U2n-_3dL7L705pM_NZI6g8nK58CcSzaE4vr4kIcJaaI7Cc_ZiMbBrEN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛ اسپورت: PSG این هفته از فران تورس خریدجدیدخود رونمایی خواهد کرد. تورس به لاپورتا اعلام کرده هیچ علاقه‌ای برای موندن در بارسا نداره و میخواد شاگرد پدر زنش در تیم PSG بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26947" target="_blank">📅 16:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26946">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HytOmBI9-yN24uC31VcJrrFrGH0GQp9D206okleJ2jW8lffkB45ODCMMezOf7bDpRxTbKracbp1yv5oA_NqdyDFQ-GptZDkBGI_AFYbBYSxa2KoS0rC3PWYQUSxlFiB5eGzRq0skqGqm_ThPK0w8GEBB6lXhpGoGO8oTV5ai-yYgk-inhQTD_aVdozwmd-6X8nVP221mEiderNRjDYYrtdTmnjCaldgSUEJS4ifE7dhPqHW3d0PCWiXv4q_Y-iISowIX8-kReKUzCeDBfveXUQiofPiwvIE_r953ri_xz2C0B4A8kBGbDPFiamjh3VUuwI-OdKKUauXkYuKOEyi8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26946" target="_blank">📅 16:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26945">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psKLfoo-FtJwAFrVbovmE_eS_f4JPIMA9LVgQCN9jZwmXUqNobGLoVoKdZN8n-R78P3DOf4S_q1zhGFBVv0-ol95jfYQJFgyA8WOht41QvjGUNsVePhreC9W9GmAseLBC7WRQpRdoVWuwexPBep3ifsXQ6g2A2G69Gv3nbZRFLJiIsWgBIiBbdghVpY7j_3dOzG0xsd0WEAPvZwwiEiCh5h2s0OcZfgy9VZ7tfx-M1PuXj3ggJosimiZuG4gengJT0ZzG2HGEIrzRZquA4zDTchRjbDRU6ahM19M311-yHV_uraldjtWY_G0r5dEbed7tzFHL0G2khIALX3y6IHLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26945" target="_blank">📅 16:10 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26944">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbOy9XekCqVvGD09sGewjyDCIH0EyrYKL-eFT5XReix3K_yMF20Z4omdg7XIKdvhZcAHpXtQPnzc72sGfWbwPHrFj2oZefHcdAA9eQ2MUecLEWlIVy7XdIyC3ENAxC6L1A3eoHPmNO_YzZbOkF_u_3pMD5mxCSLCX_vG--jgMwzDxnclzzbvJpBKdWOYlR4DXHgDBdkPbKT7wgn3c73vWdo7Uqp0c4bC67AAOOvaOpY8pmbAAYjOm8iSzN9pbGGE1fTp4Cvr6HlNCFMSIn9dDYna9cCikyBo-qfAMGVdCvJxV3JdBnyrfYxWjVm3BhtqDTsv2SFxzXYkvb8bykZIdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های‌رسانه پرشیانا؛ فردا جلسه‌ای مهم بین‌مدیران‌دوباشگاه خیبر خرم آباد و استقلال بر سرانتقال‌مهدی‌گودرزی و مسعود محبی برگزار خواهد شد. مدیریت استقلال به این بازیکن اعلام کرده که با ماقرارداد ببندید و تا نیم فصل در تیم خیبر بمونید. قراره فردا تکلیف…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26944" target="_blank">📅 15:53 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26942">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PP_VjxFH-k3uX-jfWk4LZdk4NbWK-IH0A_TuJDeu-oo4GQnIWXMAFFPiDfsIgvsQohoAilrHfIaReBZBvVs0TiSFCULzfQfAMfCwAUIYhSDAx5fpXlPCLlFWXb32EqX0I6TIIkGgogewQoRTKhVgkUo97Ny8y1Ac068pQna34_c0TPU-7ugob7ImE-dB7pAClCSAJYCF1DXCjr2dLe_oDGGP4LlFgPP9t0BX4kOynr5F60ciBfdtpUyPVaqDIaoQECxnmo2LJi98AQ-uYO69QM066A2biVppYBYSCvGA5_QSg1-zlF-L3R3fAp2PwRr1vSX1hI2AH_ZaOjyr37mkpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=n3taVqO2JbtbIq6xYPPLyfUQxbI6fkb3ZOD2uqN13tAT3_-AsrtGkgWF3xb9mOt8IZyEfu23dPq5auh9EqQuk8qkPcnLHgbmCbc5dAhmT8PoqknXUhJefINYyrHcPkLBWN2bFv_-zAjWBGZ5YgmQwc2XySB6vzuzJN5dnQKtwlvZ-1KjW3dGX2jZ2Zu-Ug9m8EQNyFlolCQYWUIAjdNsKOgk8TFJdadB7Ksa6G_gKOPJDl9C2IU7aT78NSAP0bBm2QVBbDGnNhgpogylzDEV1l6JGoqphzvYzR5m_tHrjHdjz5Nuex77jBBREJVo8waKlpysg2LEst70-M1ffyPPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c22a2b9700.mp4?token=n3taVqO2JbtbIq6xYPPLyfUQxbI6fkb3ZOD2uqN13tAT3_-AsrtGkgWF3xb9mOt8IZyEfu23dPq5auh9EqQuk8qkPcnLHgbmCbc5dAhmT8PoqknXUhJefINYyrHcPkLBWN2bFv_-zAjWBGZ5YgmQwc2XySB6vzuzJN5dnQKtwlvZ-1KjW3dGX2jZ2Zu-Ug9m8EQNyFlolCQYWUIAjdNsKOgk8TFJdadB7Ksa6G_gKOPJDl9C2IU7aT78NSAP0bBm2QVBbDGnNhgpogylzDEV1l6JGoqphzvYzR5m_tHrjHdjz5Nuex77jBBREJVo8waKlpysg2LEst70-M1ffyPPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/26942" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26941">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=KG_TxOt1kOLDux8-YOEdXhsHAnk9RMo1VPp5oDw7e734AKHgcLngNWZQ1-Y75Gq2WLqdvzTkuvYiCofDqUvMQDUxwIaO7HcGc4XQvfR0SBHYYc6t2SlRWYbRh0IrqUiUszJzKHPQvzwJEOu0MH23GEXAOKyOneIHseBPkepyp09CdJ_PNCR3jZpN_D7zyeugfFIvxEplwU0JKPQsYc09BynQ69WMQhY_8qR7pNwRlz3VIG9WsdKH5qNVy-4VumdB0vstVWEDxBOUwSwoRpUTSypfjR5n_IA8ECHTnZRzEadb_FxFPO8nitH5Kgf1fN7DXt4qP_0RxeRgG4WHVrDllA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1f8c0281.mp4?token=KG_TxOt1kOLDux8-YOEdXhsHAnk9RMo1VPp5oDw7e734AKHgcLngNWZQ1-Y75Gq2WLqdvzTkuvYiCofDqUvMQDUxwIaO7HcGc4XQvfR0SBHYYc6t2SlRWYbRh0IrqUiUszJzKHPQvzwJEOu0MH23GEXAOKyOneIHseBPkepyp09CdJ_PNCR3jZpN_D7zyeugfFIvxEplwU0JKPQsYc09BynQ69WMQhY_8qR7pNwRlz3VIG9WsdKH5qNVy-4VumdB0vstVWEDxBOUwSwoRpUTSypfjR5n_IA8ECHTnZRzEadb_FxFPO8nitH5Kgf1fN7DXt4qP_0RxeRgG4WHVrDllA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن…</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/26941" target="_blank">📅 15:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26939">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXPZ1j09tvXpqUgrWc_GdafF8Duamglon-7XAL8TCKg3G8yhvblgyE4Dp_DvXOgazfyntqFZ_8bFXljVRjx8lJYBqBN8X5Q9j5B-qqlV8Hf-i3Bd43yyxPQMx9zxKDno-3SKfFvyLQAq_pjfAKEIfGKACI_7IN3yDh3-rXilXlx8toiU5VH_vGrFv6OC1s-8boaUxmepoG1-RULNm41K2dPnJwL1crlBMNFN4-aS08xXDZTBs4IEfdXzzAtuB0LhyNXr5g2yyp1TVyBMa5ygJ4FOCQDhF05oA-LRopwLMEydFaaf72AgKHvAik9InU7D-xi8_JxNUcJcDjeyfSTTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwwII6BjA1UmeMz01qpH0ipkcpQ2uC5HvCQorSaXd9_8mUny2FwmwP_6E2Uu99J4_BltwzluOY-xrqiu6lgNG5Z0eeY3pijoEtzRjq771riS6lWreQ13S3BbQUJJC4aRk_vi-o9D3R5FtagN_c5A1ZXIfMx9Ug_bXjDABXHVcQ1160haqzYFuSn409kDJl9JZE7odISHkT6z7AOezfoVy3D3Pyh-n0ZT2rE92flvjFLsvJsrmHJuUUjx_WcSdVy2zZ6_M3b6_wQjb_ZKcVKW96WaCtt6e9olUoaW4pM63RUuftz62gTBcz3fmx13R5pgmo6gXjAiKDaeThjt7shoFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/26939" target="_blank">📅 14:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26938">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH5ZpyI3Rxmj1JdFmlyhBRh_iHfdy3kF-6ZulAw0rgY04WLNce6lS6i__YT2SWkX-QsO6PBSzyHCEjDn-xKxQOyGbxx2_L82qNguCx0ldXtdx0_HUTtFAihuEdURSuFePxj-T_G14Rbw7XDdbPOkxEOU5ZR1teYh5iD2wSv4jl1P1IIsmp3wkNAwkawEbbFfA1rl1zSrq0MdfvCAa3xdv1WDsyf0kiRofrWHjN_2QzmD408z0zcT7ZMx6xsiDGgk8dGC-ktMoyAoIGK995IVoKPjeqN7OW2SEIMvC3YnDQp-FCQin6wUNbJmKCZN3Ivaym-k2avj8bFqiOHwWQsVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
پست معنادار و تامل‌برانگیز رسانه رسمی باشگاه خیبر خرم آباد با استفاده از اعداد تاریخی 18 و 19
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/persiana_Soccer/26938" target="_blank">📅 14:39 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26937">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=d3sDBmfsWtxttFJEO2yy0bObZG92BLRYsCQDsPhyDjQMDhj_Bysdmmt7HGfbOGt72PvbfGRCSlthJTK8XRQDohfkbwRv7LAasU3-dxJqei2UCEFKbLJSxXRRe_61SrDAQSwAf85jtCp8gkPd8VQN7AWWp8tcv9DJxpVz062flV9xUd7pQczizfvhHuoFIQrYHzEJm2BozUefjyDnalNS6OI5IPJJU5YsGCgw_c1BYRptY8BTJc1OQT5BRXQovBWwNUYUiTHVBIQKoTq-fFRcxs5f_BJlI7MHTCoQt0g9CRTMZ0_xBgvb7Co2MCPd_TG1JtDWYubnineUYdiCBk2maw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cdcb5398e.mp4?token=d3sDBmfsWtxttFJEO2yy0bObZG92BLRYsCQDsPhyDjQMDhj_Bysdmmt7HGfbOGt72PvbfGRCSlthJTK8XRQDohfkbwRv7LAasU3-dxJqei2UCEFKbLJSxXRRe_61SrDAQSwAf85jtCp8gkPd8VQN7AWWp8tcv9DJxpVz062flV9xUd7pQczizfvhHuoFIQrYHzEJm2BozUefjyDnalNS6OI5IPJJU5YsGCgw_c1BYRptY8BTJc1OQT5BRXQovBWwNUYUiTHVBIQKoTq-fFRcxs5f_BJlI7MHTCoQt0g9CRTMZ0_xBgvb7Co2MCPd_TG1JtDWYubnineUYdiCBk2maw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خیلیامیپرسن‌دارایی محمدرضا زنوزی چقدره که هرچی خرج میکنه تموم نمیشه. این ویدیو رو ببینید متوجه میشید. امکان کز خوردن پشماتونم هست.
‼️
طبق‌گفته‌خطیبی؛ زنوزی قبل از تراکتور خواسته بود استقلال رو بخره که سلطانی‌فر بهش نداده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/persiana_Soccer/26937" target="_blank">📅 14:08 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26936">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_ZAB3vVV-W4-4IhDQ96wULVlPeymLo7apxa7gJgEGFeEP18t106pLfImfZsj0w8nV5GqZBI8Rz8UzlrsZLjqAYZBQ58AqX_zTJnZcUenUxDFiMJ-XEK1dkBQ5gIbIjKtA8Sn-8rG7pGFrL7lv4pCrR1xMDsI2RkUQdeHhWME3zrY2tAUjcMDRVoZWiNWx4SMD1YOdCe4wdL9w3rhJNTmQOkDDIJTEjDTuqCMcCUvNCRmZ6qsDC48DMyOU7mElnBnmLFOASlDl_YK86Az1_3bjGgtMxQW2OI3T-bj0Ntk6a2xrrTSfht1gperiDL7rueixt9pFtFFcYgEVtf7_uydg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/persiana_Soccer/26936" target="_blank">📅 13:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26935">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I99P38gZQp_GRltBHnRhN-YRtDGuipWyvsBfdhSlFX39mE61iqSX5p0E7S2wjpgVMvc9cYrJ42ObYGoH9yVlNucOJ9oR-z5-NJGoePrussOON7xHKXnUZaApzysk_oQSghB-cXSTCc7Bw7NNeqQzf4ZFwrj1iunRDCkndTZuqSSj_OgizsRsGkaLW2QKGUSgmO-Y7WkNLM1B1YkOdTY1HYJmhqXvLAt2dcmHagii53wYrPzwW921r_fCxDplKjbHezP4V5UeVoapwFrQuablRH9RWiDBvVynWUiXT7E9dINZ5a05rFaaAHv9ebImopSY7hxEN_zErEekOLAZMESkgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/persiana_Soccer/26935" target="_blank">📅 13:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26934">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iICgFz0TdPNh9C09jDbXgL1VTMX_N718F39qqKmh8kmTvq6XV67WyOCkvxylz4cMfohgSQN_Q1OSaOZ46ockWMlDd2Xb3LYBjgQgGwb13_CsqlkHufymixxUJcoZSZGqjhQs3ImiDXMwIwvQr1r8DOsiU6alB1qHZhH6G9L8YErfwsolmFAF7DGdDrg259lV0ZualBrrAUmir5FSyq9prM8ERoHk_IiZ57Ds5r8tDh5fWQ4nzU1TarmjN8U4baTKzsmp6M3G-eo4NnS7j4wpvfv0QU0sMgBAWX9FK5wKn_pieitGY5Mx6HD7xJnjbbAULg51z6nVtk3M_UHEffSDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 84.1K · <a href="https://t.me/persiana_Soccer/26934" target="_blank">📅 13:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26933">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYnpr1lYWCG4Y1dWdHUmlQTDgd9YIrsICJRtbnquVQKu-ihVtvdmsWssA0y7m_uxlox1Zg9VSwrk5ma49FkKuuCs5crk6mjNMAjaIyJrJ-4tOCJQvtfomJKRch3hcKRY4DR74dxlwALDNwF5yQ9xcyI4R6kV4WeViQ-Q6YAofETVTuQLTEL9DmE9nwQMttOYBmjdoBAF36WBqIaCYJ4r3JSkUUMiqaUU55RXlNAnbzWx1P51dOpHTZnD2mlsgxCEjzfuXC0S0zJI-pRY7HEUkpd4qOduG2Udpd5AKdwmYDfyZBrJSgEN43LIh_Lq1glkRvBewDgUkz32aYaCRbDbvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی‌پرشیانا #فوری؛ تلاش پرسپولیس برای سرخپوش‌کردن‌فوق‌ستاره‌ایرانی ماخاچ قلعه‌.
🔴
طبق اخبار دریافتی پرشیانا؛ مدیریت پرسپولیس ساعتی‌قبل‌باارسال‌ایمیلی‌رسمی به باشگاه‌ماخاچ قلعه آمادگی خود را برای پرداخت رضایت نامه دو میلیون یورویی محمد جواد حسین نژاد…</div>
<div class="tg-footer">👁️ 89.7K · <a href="https://t.me/persiana_Soccer/26933" target="_blank">📅 13:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26932">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKLQ6T6Ks1SiDuV0tHtDAyLvwmT52ikdhjo0DzogBawjOj_ELr_RJUWCWA7rBcGQzoz_JyFq5G2viJfLwylShOjg83jF4rqn-_D0TADZR6NQ-WQ1DbCNnIdqg7E12KnHwsWKChOHGNEAcr-MQLANaTkMv5wtJL1E2dJYVF8fdKJ3a87Jt7pmITU6h5SJviO3udPTS8rEplgkMrWBx0ikT34_38axlhbO1h7vv5MCQzxeY9_2_jDPQhdw5j1X7ctFEYZx2ge6XIbIpRUqW38A2JzIcZCGYiEljfotfGLgDDtD4P3OLz7smZ-DJ3evkEvuWEOd-33LMc6SzlveH-mROg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ محمد جواد حسین نژاد ستاره 22 ساله تیم ماخاچ قلعه روسیه پیشنهاد تراکتور رو در رورهای اخیر رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/persiana_Soccer/26932" target="_blank">📅 12:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26931">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyeINraodMue3J20P1OXtN3Mzib2NbqKE4xSnlAIljGQsp9kfgW0Cpjsrj5DSlAXivIbxTjsei5CNarzvOoGppPvn92oKx4u2jRfMPkFWH8pI7zRFIltrB6xDC-GruplzVue589NgUNLxbQzv_IOiLJ_40UCpNAiWPqblRwXSbiFNhhYYehJIBJYU2eAJc5y-axAyRQkeLxJ_EziQrm5IynXsNCIMCneFtmGDfXekoIcY9XjXIQ2z7nHSTsfsWXH9pvaO-DssLW1iuf2Kz9k4vK0rZStnnsU3tocMuoa0StdAxdql43noyfEfyl9ICzT_IcKWzppD7QFzyD0TqfVaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
نشریهESPN:فلورنتینو پرز قصدداره درآمد باشگاه رئال مادرید در این پنجره رو به 400 میلیون یورو برسونه. تا حالا 200 میلیون یورو بابت فروش بازیکنان‌آکادمی درآمد داشته و به‌سران آرسنال گفته اگه‌وینیسیوس‌جونیور رو میخوایدباید 200 میلیون یورو هزینه کنید. اگه توپچی…</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/persiana_Soccer/26931" target="_blank">📅 12:44 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26929">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHWm2QeYt3_r3XdbbPksilWkmhgMlxSXyDZxjsmuhEa6wab7Tid-FAkrLvECLqV17WBbPNpj-FaJueMxiH670Sk7jycrkAHkZuj0ORC5QrOlkMH73fwRdckuapirhxt6CqiXvjZOGHLorZeOO6y9aYMYXdgn0_12-n_dChy_U-l0VgKdOjOny9EhxBCY09adyGEPVY1qvIKHwS-PEsE8XGRx-rhpmrcrn2r2TfS_HS_rfFgdrNVTuivcWCbMKcI2-4ErFwVMBeo0i_1AWBW5BCgf9tZxHm9m3e-51pkyHVBa24RzXcLTr8C4pczZPtntfhrPQIRIMvbI_KSxYvEw4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v2M2ozFEwnqHEv3M_OEPBxdAy2CQu-qi3qfV0x23nByFv5dfM7LojTosTJXYbL89R4FidwuZ5tPxu8yVTrCBRetSNzGOAMVc4Sj-v_0N8KSJDY-rhcRW-g52Qcc9xYG7v3B_EIbPy2nSVrH3x48xIIi3UJtTNtWGN6faCi1oZbpcEJ547gToBiriY96FZwrBWbKigtrSqCHkPtju-yzyZtOFwngzdCAzdzQJWuhuA4uTV6fI4OK5lWroGNbFX-hTjyj1nz4H3mLor7o3gZX0FuCTWuZvdSmwrhq9rma0FFT3xsZdyX7vD4tMh714xr7i7SAEcB5qVG6rLjb5u4crmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لیست کامل ورودی‌وخروجی‌های دو تیم رئال مادرید و بارسلونا دراین پنجره تا به امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/persiana_Soccer/26929" target="_blank">📅 12:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26928">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gH6jnhKPApvu2sjE2gt5TsoXT8qxYs8OquIzUus-QLmGfuS0IhuR6UoX0aE7AvZXm1seCuOe_j1XepdNnSNPSoUldHiPPIadZXvyGdU1jGvmhtKJPCJ58V58tKwBtz80c8W445z77wqJYGHAILZJ6SlotM_BtfuESniVbE7alpu5kvnR-ze_UW1VUUB6k5NMwlJ4yymxmTWCrEZeHacxUtjxkkUQN17zPK9Fp6FrFihAXqdtx26JtLkyr3RQaco7eOQTzbiUs7_a0swOcSvSeRL-13NR0yyPhp2e8umo9YDWFdneIYoSR5uGCgucNhkOUFKZRzOi44kI-IjOyTtclw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/persiana_Soccer/26928" target="_blank">📅 11:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26927">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">📹
هایلایتی از عملکرد خیره کننده فابیو آبرئو مهاجم 33 ساله انگولایی مدنطر استقلال در سال 2025.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/26927" target="_blank">📅 11:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26926">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8drIPh9esJXvgnCYAxyolizsZxnWGJOIpEwzDSH30isja3XVEsd0yKOem9qa1A0PXd-IpoJ6ILnsRrzTOuIuI0B-Ac8KLPcqozbkcwO1vO-Yfn9E52qPAiJvXZwrPKNQoqbhvAzCOhzVYRTwLfOdyptJ31bRZxMpJ-GYKgbdfgvO3l_H11KQqTHlh2NShQs2utbGpcxtk5P5bmMz2KsdAXYFh49T1h7OoNJRIqv_N_TUYah8YbMFbnDJp0wHoCHe50hkqsbJJsl8k5v-hToNmb4zbCoUAoh5nG6lCBFf-ttSSj9nl5qCDptAJhhbWK8bbgK13C4aUqh5JDkkPcbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
زندگی رو لامین یامال 19 ساله میکنه که تو این‌سن جام جهانی برده، تو تیم بارسلونا بازی میکنه، حقوق بالا داره و صبح تا شب با دوست دخترشه نه جوون بدبخت ایرانی که از بعد هجده سالگی باید به فکر سربازی و کار و قسط و کوفت و زهرمار باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26926" target="_blank">📅 11:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26925">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1R6jkYBV9K-2LB2orWmee4FhVhxfUrsyvjz2q71pa0n4Y40piToXzEDr4UfEEQLg62jj7De0P3ry_qbaqLFeh82Ej2ebkCY9IAnGPqrrg4kpS-LxFBcyBsfSuhMtOJjNG7jbI2s-qB8jP63Pj6GX0x3EJSV1hyWHairyr6lnmJ_P4ulcp-ouYU9t_sNuv_DayJSobnDRi7FOlfwj2O3an8rnCdikuF43u1iNkmQLZwtA02_lEbNxrwdASNYDV3Ta9S6AkDna7-X0FgYIWoKExiKVAEBqhOUnMdWosXkBW8ogq9JnR9M0Pg0o_wPG9LfuF9b5JYrJ2BrGoKySqAimg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛
با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26925" target="_blank">📅 11:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26924">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEvWIc3lWZkVj49QDVIn1MxBHbtamWfaRWsFQdOrm4Pt86HKhkaOOkCgb_Llf5LLqDWpsN9ohJcI1hvialhFoaU7xELB2RLB3NOspS1MccV6OW1pjqAamjcPaI7EG8wBEmia2eBS9F_Ec4R7tsv9oQhb8ISl8dRmZCNN7rcrO1RCSfMwAshR1sC0yG3XDKZtGl8klud8_cr1XcTJVGrDeuy26fdvI26mihQiTaZyEMpAHCkwS4USHmOS0eXKskv05HgGsxOcSgoyuWisR3zNVksNEmpfSZ2I-Yom9UUvr5ZVrqy_q5KEQE_OyoET2ILJ2NDLLc41N7y-bIVKNRiKqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/persiana_Soccer/26924" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26923">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB664CHc2wFTFEBnFh2Yr1fh6_LC8bybLQAixnKEIH42KWVqOgUhp_cMKnBT4s9gC-pj2tBTgpq-MkdVDzpJOYj7w3qvGcjjkDS4_2P1pOSPo5hbtzYZnUixzp6jhf-DUgzJfBtYp4sQ2nhVT_tCBR1vsiM8AeQH7wxUgJjzL1feK7ciWIIu32jdZvQCkfkqBHJDflCnlrLAiTXl59BodRCieTxbSNdoBq_sXM2t9WVjGOWT0tcgkvWDxjgShFhubQ7HYS4GKuuLGaSYS5AE5VT7Rwr9FN_eic-hiLDf1WF2JgFOeLC0B-mTzFm-h0sucaT_ul8bIq2g7bHpNJw87idU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99893fb77f.mp4?token=P0j4PAXLECrNwg1spxznVecbK4h-eAaVPevB-9iti-atFAUP7dehXMd1W9kDWmMB0Yos5FE-lbKFmdV879CFAcCAW11Qiji-BJCa5EB-MA_Xq6mm0cdm8FVOdLCKfM13y_JRV1rhOTGxjFdwCz2WDJikyHhONxodyvZasHJdRKPy5_jxJFb3hou3HM7vACel34juJpzrmVRqxKV8MMp_OG9fGCQQ5Gd4RLSWonJfcls4XRHoWMVyV86lnqfaEsSjIqVPhgCAt049u2ICb9d5AzQ6HwF3Z82rENTu5_Lz69_FKjs3n_3zgqIToWbHH9fsSGoC2GNKaJxeWm9h8OhRB664CHc2wFTFEBnFh2Yr1fh6_LC8bybLQAixnKEIH42KWVqOgUhp_cMKnBT4s9gC-pj2tBTgpq-MkdVDzpJOYj7w3qvGcjjkDS4_2P1pOSPo5hbtzYZnUixzp6jhf-DUgzJfBtYp4sQ2nhVT_tCBR1vsiM8AeQH7wxUgJjzL1feK7ciWIIu32jdZvQCkfkqBHJDflCnlrLAiTXl59BodRCieTxbSNdoBq_sXM2t9WVjGOWT0tcgkvWDxjgShFhubQ7HYS4GKuuLGaSYS5AE5VT7Rwr9FN_eic-hiLDf1WF2JgFOeLC0B-mTzFm-h0sucaT_ul8bIq2g7bHpNJw87idU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
چند تا از شوت های روبرتو کارلوس رو ببینید، زمانی که فوتبال از کسب و کار و پول دور بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26923" target="_blank">📅 10:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26921">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jw7luqL2UTnLPH_KxmWiq9b6FZSZ6o6BvaG-pc4uUHgSpFn3Sb2o3JTiVX-_6odNk1Sq8V_tkI96s0GUhMD6HA_fVV5X5mn6gx-CWG-3-DTUUIhOn64mX0L2aIaLeCLRxZIChjbGNRYF9GI1cbjqnAtGCyb2nl8kSMoS74Zq88mIv2Hs4ZIaUVj_f2asmQSbwLuY05J4RQdmgQQ-qzZOvJgiayOQcLsBWv_rJmPK9MrWzWq1hNmYwTESy6FeWbNJ5D7KaSlq1t--jnyxz8Fy_E7zwqiMSYzjoeabNM4sZJG4P5Rq7PO9_HB7L9FZFzLPF1KLVm1r4luY5VXqVlBfVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
ماتیس یایسله سرمربی 38 ساله الاهلی‌که فصل گذشته این‌تیم به‌دومین قهرمانی آسیایی خود رساند باعقد قراردادی چهار ساله به تیم نیوکاسل پیوست.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26921" target="_blank">📅 10:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26920">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfQzEsc1SqkYJnTMZ-_beMwCulNkmUY8zq2ntkoxNAMC7pOYueTzqjQ1-rqG1e7QbqKWSEBVi34jzksUakNbwie7rmbioTJq6UCQJuAoUiynwT23tKihliIgOABe06Dsf5YaooIx0esA6_bPYQAGxtuBVb6XUDP5YIVJDe_gLZNBUs4G2wOGtEhE4xf-StJm5e6_H6T1PMuSe9THZbIZw45SiQzGVZJAjZLFnNq7i4Z1-6A4QIjexSBwuzh1QoNmbkGP4HlKWokU3gN0iAkMkKEP6KPtT0MN0HOf1mWP3d8XFw69slAyAgg9K0kg4fqD_eCPrtvkDuT6MyELRNeEwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/26920" target="_blank">📅 09:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26918">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7Lcs9IH5C5eZ0X7WlQYKAYMES7be5lhUulqfTJw6mq6LgBx6U0979J9Oziz_68chXEQBdVIe41BhIVJcJYaveXHzobMhDPHGD5ln8fvd1y3QWGBMBghTM482-8DgrS1-QZIE8zhO8xTMsmt2AaVlVMVg9Vwb9eX6qm2hfSDwz0Nd6SwV2Hz1DBpFv0CFoemZE9KYo-jN1Ff3oPuwrB-K-o4XFwfLy-aguP4Ci7xfb3_Vh99Wv6TXZ1PHCgQlMJ0NO24Tg610bHsimdZUS2g_UsrueZLhsMzXOKd0rCGu0aIqn7tX8Ba9rLVlRlmGlaadUG_i7eonTo6Eem-rShK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
رسانه‌های‌یونانی: تصمیم‌باشگاه المپیاکوس برای فروش مهدی طارمی قطعیه. سران المپیاکوس برای فروش مهاجم 34 ساله خود رقمی بین 1 الی 1.5 میلیون یورو تقاضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/persiana_Soccer/26918" target="_blank">📅 09:24 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26917">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DR8TSjb9yMOcDIsGyWOi5LYlD-7g-wZYbzzsvOOc3wgUJKhPtVX6dfce_0RyCOU4IXGp6pY2pJyrt0odzUXbI52izzjX7Cq4Xoc00rei6RJBflQAsD5WLRP-SMiWmTSRa5V9uu7LSiBmQFFZFH4PbQdtgp1Xk7MbhX7Qo9nBJfRbF9TTmEhQcR9b6Je4ShH968AHS69S0_3alnEVJs1qaBI5-uWR7NXvGUAY5WnpH9yxnGbrtdN5mD2pmjklekB8nak5a9-ubQrivSNBXHXqtQF46W5DjpuSBJvDzs41Hn6H4aWshLoJ6sXOJZRJ84sKfIefPui4BIin5N_qIPBs0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شامیل گازیزوف مدیرعامل‌باشگاه دینامو ماخاچ‌ قلعه در گفت‌وگو با RB Sport: سه پیشنهاد خارجی برای حسین نژاد به‌دست ما رسیده اما ارقام پیشنهاد شده کمتر از رقم مدنظر باشگاه ماست. سیاست تیم ماخاچ قلعه فروش این‌ستاره‌جوان با بالاترین رقمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26917" target="_blank">📅 01:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26915">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-zb7f1vnEPKTSGJiMvADcuyYnR55AD_suxT4skfhb8zDhs4AZvMpMHcZmEIHKQ3jPOYDxL5gjn6ox2Cz0aoBNdERodJyx2h9ljQ17aE292is6fHo-XkRVi9gr1I64G6_JUv8cT9Jk5wThuHcd4iCjrWOpRSQKBKoz9J3Zhe7a26EQjitEr-Nak8mZpnvtY2g38sxODmEK8kEjdbhy3Aw1kwq7K0WSargA3ivWGnyzzkMGpUC8tohlEsfr1M2eRMb2jchC0nmYB3FzKb8tnx_nyPt2DGd5L1951eJNErmPs6FyYZBW9g3zKm6i8LQ1YFXvpvllGkLFIvz51cRb5LhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
از مصاف شاگردان ژابی با تاتنهام در استرالیا تا بازی رئال مادرید برابر فیورنتینا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26915" target="_blank">📅 01:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26914">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiH-PNyx5ciuDRFiFwvasXH4eqKg2eSQjd9jEQEkTw_R4tn4yqUN-2AFYfy4-xdFLCz76x3y5KtlrnmpD3lHCb1ANtSkUj7pSiKBbEZIf5cW4tRiaZZp-UGuaM1qtQrETZqrwHgaECa2h36N00zh410vptNeqc57QHJ50SQYoRLzIzxOFKgXj4SyC3UaGgmN50Pkh5u7LZW20e9-sLPhVfm5-1zdN9U3RYnlL6beVZ8Xga6HHpizCP1cHv4kAVPtdBE6QlBxolW9PdROCLXFSJjvvPLGVuhfOi0W9eKIyYAcLY06nyulYiso9yxcDZwgzMKHEk_XqfxtVn4ID_jEiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
بردشاگردان اسپالتی مقابل تیم فرانسوی و شکست کاتالان‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26914" target="_blank">📅 01:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26913">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_OVwKgbxwvX2KJj5xqjhPbIl2m8vaZkVMwxAxVwRBuQ6_D3rwTNpRSqARsCnPSqYAWE1k4CVsBsVEWOaVoHIYLttzIbyycqVhtFP8XVFfrO_2bDsVhOLDzYEECiZe7dvBihYTjoAF65qGqppjUVp1guWwwdYAUH3UjPlKspudGYFgP64qCLM1UgaYUvhNDocYloX3G4PohXEPdokPn8grsMaq72sf-A6v_ad8GCe4hi4w2-_eOkhPj7weVLWvhcIqiS4xnsbJbzlTtX44tsIOFzTPlCljIGSjgcIctke3GjV6dEc9qzTJwTqxEWyxoeN0hWOoK3tvdKN5VoY4QHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشه آمریکا و اسرائیل در حال برنامه‌ریزی برای اجرای یکی از شدیدترین حملات هوایی تاکنون علیه زیر ساخت‌ های بخش انرژی ایران هستند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26913" target="_blank">📅 01:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26912">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ9qsafMYnJzUqAOjXdk_TVKOUomQnPf_I8x50cYYRkS9RIvX4PneNRnMlUerD1Ba8yq26tXHZIFM0x4dn-BUADvcW4Aa8Yx9zUA1nhWq1iBYo51aXnYsC4IbwLJdj8-VtCRFRjd75BSb0w0XKNTaLu4btRP0Kj5NPVH_wrwlmpM7h2Iq0Tv9bN-msiSZq2hy5a_DKL74e6x_7mb8DlXiT_xaEfv0IB0Tk_WaAcNcYN1XR4wBETHEEYZNuDnr2WQvnOmQo9RRMnni1URuQTrwYOw-cBlZ10GbT0hu7AXPlNIcXzyPlpbLLMScEj7jesS_Q2UFJdO_aRepD9xfonAQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
رسانه‌های مراکشی: منیر الحدادی ستاره سابق بارسلونا پیشنهاد باشگاه الاتحاد طنجه مراکش رو به دلیل پایین‌ بودن رقم‌‌قرارداد رد کرد. باشگاه استقلال به‌منیر گفته‌برگرد سالی 1.5 میلیون دلار بهت میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/26912" target="_blank">📅 00:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26911">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gn7lxBYCV4_0Yqk4hM0kW1OpBi7guz5ysgCiL2KIYLZD63nxMq8ZGBnqEzZEdV1H1LIsn0PTZnUNR6FW7mpS1EZS9sRmFGrbVkawURgbY81h1iJVXt7IVL4egFgK-67DDFqMsLEutRFyYoe95kg_iHltRhF2SjKSVLUHAe0MjKBxowwvQCHz-RePOMztDkCHhdXCs6gnYzCu5KPO80yP2kFP9eJNQ-9Pc5_lZGYKvijaTTSOc0lVFHPTWkJnFDnV2veHUTHAf0jfYY25ai96n1m7_xjiOYbt-j8PGXfNsEjnr4AVZmqZHSiTu8KsYBNsAstUW4Y39HLNGxcTF-9pIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛رئال‌مادرید بابت‌فروش‌بازیکنان آکادمیش درشش‌فصل‌اخیر 440 میلیون‌یورو درآمد داشته. تو همین پنجره هم 196 میلیون یورو درآمد داشته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26911" target="_blank">📅 00:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26910">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M_ALBE0bKE3d_JNzwsPyro5jrr5us8lYdZMKXCk-btWXy-tr3EPJtntokPdOPmoh0_1r9dkhM_rcBD-Em3DrPWHJb29CfETaRt2EG-D17DnwlFjLXk_mv6xTuCbdtCJCmuRoEfCGIGTn2kznifAN8mkL6EcObJwJJuTYuG65XMFrdAruA_lvT1P1mae_N8Z4uNTBZJzwzLbq-FjsaW2YoveLbTy8uqY31IpJj-mJ7mLz2-Mljb3eraZMHw3i194hSxr3Ll8xhBP2EyQhsYCvbdXVqcRAfn_Uqh-p3CsvxBk_bQ6RCOPIHOGGvB8RWZzd3eaSW-9pb4ctxHydPEXz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه فلیکس دیاز: با درخشش در این دوره جام جهانی؛ فلورنتینو پرز تصمیمش برای جذب انزو فرناندز ستاره خط‌هافبک تیم آرژانتین قطعی شده و قصد داره انزو و اولیسه رو باهم جذب کنه. انزو به سران چلسی گفته نمیخواد در این تیم بمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26910" target="_blank">📅 00:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26909">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhirjVo9HZ9PlBf77wxj1PV324-s4dOKC72vVCJYdHFtFrgB9_UlgMbbCjb08SVIrVAEvBtdIjaGggujzaXyYIzPh2fH9IVCdcdRP-kl2dQAQT8JxFSBJ6FbL-l9iyQ3jaomFKdgXDHROaP1vRS0n9gVijxVDnjVhz8PP-UbW7lk3L9mHYIjTrtsUNtl1NX_3olPxwbTKSGHMR-5VthsPORLWoE4BMdMzuxGoOrbuReXnor-ygX9he9Yw9AJe7a4VT-cVYal3gBEKyxq4LPSUImjK3ph3bR5KQ__SXFBam4l47EvNq-ePWjp28wjOngPLyx6dBEztSXXsQ6m_489kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26909" target="_blank">📅 23:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26908">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0s1tkeCDAbK-m2UnwkwVzlKGraclPm2xmy4XQ_AWF4eLP_U_YIXCvk0MFt5L1tyEymkDXiNXrqwb0khXrW2697V9QBCIXzK_dex0t4xEhmTgvPXmBjNeNkwqXVHgmJEIpLoxURi9Y52w9KMcEot0q2jHzk79CxFW0aFi6OnjLwBsdUu44rtCBLw65lax0g8E0suzPqRuFsHhQniS5ovHPUqwzDdJigRf9TOKyDv1NGyemjbSE3Y0AJm2vznErOO666otUjUukfINTLcanHMjcRz-QQn5-5d8toZ0BtWWoPMiCeTmjphDtrKPPpg_ZjGYoHmlc_4l5PszH5Izocdpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26908" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26907">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jybFY5JPnlZuPf9InuqFUUpVTByBCuYejGVrcajTAI_czOt42b-GT5k3GCY3z_K5_M60ASyGDkofMLafeOo6o2jLWBztqNIeIx8Wsn2mMFrQ2RjpyfurKOCgcL6-BhLz65M_mnTPZsQQnrKD87RMUGdXLKJ5N9RHrcSFnj05k2MvPaAZvkkSfk0fzI3rhJWOwojCIPH-cLdXh_Leye5-Ve9w2BnShVQ7oh5mYMWCnO8mihCnsZjBNBjU7M19Y_nF2OIT6ym1VToNWD1qgX_DVb891SYTSx-HzNWqpIwQC3LRmmHLPRPyWGMFpaRlzeMautXbekI-dvJMIv3XS7u5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26907" target="_blank">📅 23:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26906">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇪🇸
خب گویا سرخیو راموس اسطوره رئال مادرید هم‌تحت‌تاثیراستوری‌های‌رامین‌رضاییان قرار گرفته و دویدن تو خیابان‌های شهر مادرید رو شروع کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26906" target="_blank">📅 22:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26904">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKEbL_YUr4G_yvh-ZQKCreax7110b3IWfPN84lZJXm64s7AQeZc5_lGOFYYvzdxLsFteEj5aBzPdPoaiWgpcwqB_GZMizstmX8Kn8IkrSi_IqAvNoS2f5mE0aeu3HK6VvcsvCv15tqi4z1KiOLgzvOMP_vzp3DemZpUkiMnqL8uYoDAVfXlIlldkIjPxIRk2HYzwaMXMCODIl9kTFaSEdTdl1_TKEZcYLWb50gAU-U_CJElw1wGM3TWE-H17PCSQJ5iNCoqmww_-gqzO6ShwNEUILT4cD_j9KRYER7vMiqRSx-Iu2GTMXCdYn8bp2V4_2ACG-0KjqCVzH91QUHzT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#اختصاصی‌پرشیانا #فوری؛ آقای‌گل سوپرلیگ چین مدنظر آبی‌ها؛ آبرئو بالاخره آبی‌پوش‌میشود؟
🔵
پیگیری‌های رسانه پرشیانا ساکر نشان میدهد که باشگاه استقلال از روز های اخیر مذاکرات خود را با ایجنت فابیو آبرئو ستاره انگولایی‌بیجینگ‌گوان چین آغاز کرده و قصد داره با…</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26904" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26903">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDDpxCshJ_bYAeNcWzK0bOfBPVGMixDD_H3lLoV9nTwIvFu6aFBfDY3xBgeHFgLPRSq6iciho5xUeqlL-f8FnuCr7gnG8HiHXvyRH2l5GqhX9BFqM7Pp3fW8D2I93gdrusfwgbXBUkB6LUTBFMKAFCRwFktXhztVvstILG2rhWc2e1Mt393Yz1-yWItKh41Z7gng8PMv52-LL427VoSVhejxwoBkSf6ZmH3Hu0BvGiERz5Q149A3I_Dwy_h3q01Roj8eUPBZn-DtfMwRfUal8mhu6S4GnZcUVuxmY2UPHp-WUwoYqlGE1s90M4zE9cX8ijVaPdncO-aSCvO95q14SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شش‌خرید قطعی تیم رئال مادرید در نقل و اتتقالات تابستونی؛ به این لیست رودری و الساندرو باستونی هم اضافه کنید که در نهایی شدن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26903" target="_blank">📅 22:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26901">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrEN9oR8TgvOnMt7ZCMJCNWuocOcLw_8N0PFsPVjb9R2C0q2sR5w-PmPXOchbJ9h_qPgfgFb2yP4_RNDBqxwaC6XAHMRisvCc-YR2gn1XXFCcg2XgSWxZ0_Kqt5Kmm50rT2DamT3vRDzHHaMmAfVql9SbRjBVhH1ix5DtdZ_46vTklZWoOoBWm95TFL2iGTE8P2zHlhD-pkOwrZLqtWReV9M5PkZq4JS75p6vp8MB6EBZoFo-h3Rni-WRbWPYz0MSdDV4CnZK6MdrfFi9oodb8k8NMd6Vaakz-G2eijXuX3MjlxWOjkSpYz5o_cKCb0kiuMYf49qYUCBDAAnpySyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
جسی بیسیوو وینگر 18 ساله کلوب‌بروژ با عقد قراردادی 5 ساله‌رسما بارسلونا پیوست. آبی اناری‌ها برای این انتقال 8.5 میلیون یورو هزینه کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26901" target="_blank">📅 22:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26900">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx92ud4x7bEXRVEHp14S4xHOx702f0ItAVK6DSEMZmcP-jR-paU6rjbpUpKP6ofrAs0d9jE9DEV7kb4HCNrDxbQ62n4cN-dqMT37Qcu7eoYWgvaPdm8aE9bVUHLTWZsdLlflWHw3bMbEZT0CVpqSj_jxqFUcmHUvPoPOeP1Ruo75Z83GYZdIx3xRv82WxobyTDIb9CN3RTfBrTnZ04JooyD0Rzmafoy07wyVeXPiwNZwq1v3rvltC7XX7sLq38TAku_ZbYVqV1-pVJi0i1xbZVvWl30EYQo7_slywEINAT6XgMzCfVzqUfWV38yXzCJ8oxF7eGJ274TiJZjITLYWgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفامیشود با بازیکنی که 6 ماه از قراردادش‌باقی‌مانده‌مذاکره‌کرد و حتی قرار داد بست مثل‌ همون‌‌قضیه یاسر آسانی با این تفاوت که در حال‌ حاضر پنجره استقلال‌ بسته و مدیریت آبی‌ها میتونه الان‌ باهاش‌ قرارداد ببنده و تا نیم‌فصل در همون تیم فعلیش بمونه و زمستون به عنوان بازیکن آزاد جذب بشه و نیازی هم به پرداخت رضایت نامه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/26900" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26899">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaGmCL9y9MlwdxXPbHw_uclbkfo2kSB5TGjDFbj_HPjs-dlm5zxOdJZOiHhl92X0_AG4d3LsVFqIp_XxPJOhquNU0SwPKsMST9O_A_7fUj_Rw1wC2f72jWSpRtUS8419hPuT__OMXeUVQtskPahF6kX_BYCvbRzBKGpkVh6dVjytfPGSxtPJpdHrqmAjXPgBVBi-XQmi4mXg7Lnle6q0OaBE-W4uNydFjdGaRVPCWVTbffqBbWUS68TSzmdx-Bb26LQ4XMInp5l3efF1YiFZvGyd-lONzyiturnXPpdnTtsGuTAtUxk0lMGI9K1xGEbDSJWhMJa-ejaG8cYVmIYBVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
براساس‌اطلاعات‌ترانسفرمارکت؛ تنها 6 ماه از قرار داد فابیو آبرئو مهاجم‌ آنگولایی بیجینگ گوان چین باقی‌مانده و طبق قانون فیفا میتوان با این بازیکن مذاکره و قرارداد بست. در فصلی که گذشت بااختلاف‌آقای‌گل سوپرلیگ چین شد هر باشگاهی بتونه بگیرتش ضرر نکرده است.…</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/26899" target="_blank">📅 21:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26898">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA3pdmFLMXLepZ2-scwZ9b1TanzH6m8OxEBSAFef11kB2TEq8Ggv7Q-MLPRNtT6ShkVh-7jnlVXmItUvEYlxqVOzNWozUYTnXf4pTgvc8S_WMBvcRND1grAr1StkTLrZozxY1K0TO0mDtDotNMWaqT1tvG-ICl-GRi4tTPhknJiCIF8LQvdRkH1u9WSxQ6iCNS0ZmDum7bDztjMLZZaHlZCa1_XnmkDnSe4yKCMWjeoKEILlOKERtW6Oy99nDjcTgVY8YWyIyo1zUGZQSEJxF0T2s6ynEjE3dNRfokgOU04VMgaI_zLipYJOWVtkypF3uKbbNtB-psctRkLa0_wpfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
در فاصله دو هفته تا شروع لیگ برتر؛ مهران احمدی هافبک‌تهاجمی‌استقلال دربازی دوستانه امروز آبی‌ها مقابل فولاد از ناحیه کشاله ران مصدوم شد و ممکن است دو الی چهار هفته دور از میادین باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/persiana_Soccer/26898" target="_blank">📅 20:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26897">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO1u1GkCpPRWo2b26gDKF3NCCshcO94oJ-BFwNZ_uuqyZX5oQrkR8mkxVqm6iSWjOeNWx9w1YeCeoeR76BJijnEsUopZlOhWi8zvGGE3NGKBiJnPTUJz5YJbpkPhg3OJRmpPQi0lC0POvBUuUF2RAqQz_yP8qk0b6S7TCcUXMnzfg4K3tFw5HPLCsWRN-1eS6OK23bAUAT_5r4g40VOQVR8BdS9vkffkQSOq86cxFcsO2NJZfwx-DXbxuzq7JDPctu11aQDmpdAFOxFublRhw6G-QTF9-tygq3sT1mAFUZrEQOvkvCk1dmHfIFw3WxpaZrEkGqEYKgPdTorR5ino7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
افزایش 12 سانتی متری قد لامین یامال ستاره جوان تیم ملی اسپانیا و باشگاه بارسلونا در 3 سال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26897" target="_blank">📅 20:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26896">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92aea27557.mp4?token=nTVW3xSamjJ0olcOp5GxPTQja03mzwdCETJ6tvdYbs7PegoX5yFrocbmJ4YKF77EoUNuHoIL7-iVyNZlJSz3hEeRjjWtXwgaMWn6jgle9giVa3H8O2pJsA4VTIwD3YVTu8uxzcb-T5m2o5PVuFfhyZ70IZ3RFqr68IkMplMzDm3Y35lkD5zfsFO6cVunhoACbFrioNkoH6C8yhR4f-hNblxVfwSr2tiZNNMB3AJbEHOj5xuw6G4NhuAfCgAs7oAS6d2euIvqZtNqTHdsapn71j4cNdH77rmAK6SrRmniS2iPzsEmMkoVdv7RcKM1fDnAy84azubBQR_mq06Qq69k6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92aea27557.mp4?token=nTVW3xSamjJ0olcOp5GxPTQja03mzwdCETJ6tvdYbs7PegoX5yFrocbmJ4YKF77EoUNuHoIL7-iVyNZlJSz3hEeRjjWtXwgaMWn6jgle9giVa3H8O2pJsA4VTIwD3YVTu8uxzcb-T5m2o5PVuFfhyZ70IZ3RFqr68IkMplMzDm3Y35lkD5zfsFO6cVunhoACbFrioNkoH6C8yhR4f-hNblxVfwSr2tiZNNMB3AJbEHOj5xuw6G4NhuAfCgAs7oAS6d2euIvqZtNqTHdsapn71j4cNdH77rmAK6SrRmniS2iPzsEmMkoVdv7RcKM1fDnAy84azubBQR_mq06Qq69k6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از عروسی نادیا خمز دختر خانم پاکو خمز سرمربی اسپانیایی سابق تراکتور به پارتنرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26896" target="_blank">📅 20:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26895">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtvtH6ZzMV-bs3QxO9-gbCcT6v3UgH5dZMJ_ijhpCDQi2rSzYSyvjQLUEs7tJHbNre3RKS1x-W05XeFB9DS4UNYsiwlQxjWd8wSp_77Ca_sna0uM9AbyJUINlPV9Hs3uGuX-ryyV64xaDna_NCwQSwDTSuEfDR9VHdYrf5ARxR6XotJQuhObGjRccKDS7lhwQZrWOpvGO8PameUfN7wwVoFHEuB3LctloWkSd7c6U8-ufTSjKddLBCNL5ANeDaCkw8A6vn4iA-V_xBynLEl8KIjHY7x2QOfem28YlqG6mTuEc9HDlm-Q27lk7kI6PHRUbNgvvuCZIvMAdsAuZySjKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26895" target="_blank">📅 20:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26894">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-1u3KAXlm_4Z-HNSXI71zCth71edR8LjP3Jl7sgWwkUBIOWoCMZpfcWfw0E2CIflKVKkWDEY6OTuEgcyf9kcdIpHMUdpaiyVrkXnZGHa_XzPRmy2p4CWHPGWDbC9w6ETCHlgJ9_ZM853vGD_l7XL-jALID3DgJ4TT6Mw-sSXKYZ4eI7wHzYd-QjA6tMN27mMbP-4X83XABxsY-Wlslxqo6Ar2Rd3wjRFBrKMyA656k58LmG8yxj2DcnfchcUP3eCyMNdL-NMxJCUu6uNLpPqlv7mJyrpQRwQ31NIQV3pVCsRAW_yDtI8ojrMht--ro0qzLn0FkD3cCZ_iHd5uSMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شمارش‌معکوس‌تاآغاز5+1لیگ‌های‌معتر اروپایی درفصل جدید؛ تنها چهارده روز تا پریمیرلیگ ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26894" target="_blank">📅 20:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26893">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLvE2DXQ7KvBcMSo1MvntyEq7y2DYeJ39vlrz3zPJcBCBnow5pjgp04bOWEaxWAhgsbJt2PKH1GtlZ2_gFT1-HN2IbFBRCBa5KiNdo9KK9rXdXjAcoIasT5zFVJabh2_S7mdvcxe8LVXb-XjX3a2MY8Y1UbNfjBIvIkWu8ys27srjdJTNJSXSgJ3nZv5HOhmddCpk7V8IjowqU6SBdqOCgCMy_unPahsaVy-emf2s31uxTfOGnNHtqhZNWCe96xf1rf2LeA9um6-uNHHHc5CHB8u5ZOQTvSAZizK7pISelBh2doAw9JkqezBaDivsoNKsLoTOMxiedaBwBvn18hs6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکرد اشرف‌حکیمی،ژائو کانسلو، ریس جیمز و آرنولد 4 مدافع‌راست‌برتر حال حاضر فوتبال جهان؛ رئال مادرید حکیمی رو مفت از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26893" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26892">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsXAVGXn0n1VMVyvYaUUdKjP9sqrAfVG7WLGbr-FjC2RR-9GqAtQYJrrf7jKCQvhwimLpJzi-uPttNbxPUUIQSkC4nM7ipmqb5-LdiRVQwYzhv-puj78TYW-aHSnbc8XVKqb4srnfoMBtAc_GU6lFFzwJb-gThuJkdlk5zAt00C0AAHeES6ds9wC6EiSrBc0ac-Zphb6CXDZlk-Dv_ng7dhHtWxysH3P7CkcXJSVLNx_CFDwuzzA9Z3HuWl1K8WhGW-P7p6MheNQBqwxqicnlusU8vBJ4Qy9qliNLnMGLK0bop9nHJtxVC7Hl3Tv8OPdRZC80t9fiHlA7dFsFm5o1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌مدیربرنامه آنتونیو آدان؛ این دروازه بان اسپانیایی از تیم استقلال جدا شد و درصورت بسته بودن پنجره نیز قرار نیست قراردادش تمدید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26892" target="_blank">📅 19:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26891">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgTNY3TN4UnLEekNI7ioV473V5ACcqePVq2leiMHot4fOTY3sPXaUiQyna3el4xjd5w4lqX7lFJfIeJ58r8MeDH1ttjS0y7b9C73O-ZkWNOqGkPZwnNqvbZ0Qg4H5J4HIE-tWQg_ZIx89p7h0PXn4ds26uukB20lRMlwZVLvT4CDl0DUBtYYp6uhCljRm7j3jITP7udNeBbUsxGIy35DztbiI1PIrKCNpDI4fkOF5m14yfJhkLqqiLVCLYt2pJXzxcoDSe3FIiXJi2XBgtD9PoKrvxVRjpv6aXBaC4alMW-9xty76pZiiesXTNK8zkiKVH_Z70XoIWd8f0sZ8qSjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
برونو گیمارش‌ هافبک‌تهاجمی‌برزیلی نیوکاسل باعقدقراردادی چهار ساله به باشگاه آرسنال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26891" target="_blank">📅 19:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26889">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KU64HQ_iaXy8PPBm_SY5anUUKTVwAiO-h3j1_AnZRzPMgPEI6KVytUKZbIe_mbTrcqDDPjJKf6BaUp76Y1WE3LCeluEYS9wZfFQOtZfhsQ0ZQYutuE6oeuIqHiBwBBbxhqW2IMbWKWIVDhXSI3Agbhi1DzFk5WYoToUfrDOf4kRuEDnlOHV_ZBZ_NXq7bMk20p9PXh3EF-H0FAnnpxdhRAFMfTCw3zOxwTS7llp65oqSPsqDwe_rJhLOtYZmtGtiN3SGfltPpH2PMmki3QO46W24u2Sm2rMJQlVMU8OOcTiVDOPlD0cieiqDFWJEn3nbM3KigbYrwdPYkD1Prv8a3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
همسرایرانی‌خوزه"ممد"مورایس هستند سرمربی پرتغالی سابق باشگاه سپاهان اصفهان.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26889" target="_blank">📅 19:03 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
