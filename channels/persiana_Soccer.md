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
<img src="https://cdn4.telesco.pe/file/Qeii4NzLuQgA_6lBU6I2ZtyLJ2l7QmCL4u86M7YoAzZmMw1veTiWwZ-YJKVcn4ji18kfdCALWBJpat8UZudBHejaNXtfcxcBHvIfPvYMeziRMd0sDEsV324rh7dA0UZHd1xzxfC-1wOvvHipJ_t0GawT46IwhbB4r_8j5DR4mwGbx-saIYaHWWxL_IeaNKd-qjGr4ea0HsJ-roIKKbg3btKQVoNfhbueDMV8__cUtfPZ_c5BJMmL5WngYUwVBvhVyk-gaoHa6fWpStJspbQEukYXS2SIHWZv1NG4exLWnRwbt3dlRhM9Rp3h84oaM8fKOvZk36mVwCmBF9dpyBvmEA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 618K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 21:36:25</div>
<hr>

<div class="tg-post" id="msg-28758">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8ljpQmG0PmcjJg1EWUUFdTEyhBsz-tJ7Irwy1veeNWcwyOgQb_wgqc3pNRmhgYwH6uyLHnu8kGU7pFvjN9X-oMhWHgTJtkt0MPyjUgT1FaP4_4Z_JEqEc-VQS0JQ0r4nr0znnRG4uAiLhfjcPB7aI6wKbSAzRDXnubOZGCzugydzHZeCViVJgYFvK1iQ9bpjc6SPRkHya2kS0QCvsj5nxcQYoFs-Bnaa2CL_rEuxLWe4B3wxMAhNbNOh1ZI6MnGPO-a6ZnRp3xIN4QSGHBH4hqFcmJaREwQVM-hTWXB5ASDn0GjIAKAPeikyAIulOyB97DyibaSJCKbXB9IMnY_zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باموافقت‌سرمربی پرسپولیس؛ پوریا شهرآبادی، دانیال ایری و پوریا لطیفی‌فر، سه بازیکن جوان تیم پرسپولیس، به اردوی تیم ملی امید اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/28758" target="_blank">📅 21:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28757">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=edVgMp_8Yc4niLfSasGHl9utvgs7fu-kOnSWwq5nVOgzwZNAbH03Ok7WR6XgGJy-8Modt2ksaqCFm_lFZID1nQ-VUqVhUKr3kHzE9m_BD6FQHFqSM5igHIdOigQw6minKBzVIKazeoK6dpsWW0RvzxQNL7x4I8S_dp4tN7uR-7kt4PrHgXsdvISsP2bLbjLulCBRCmYdhMX3DJ2iJlneN_M49CE5hUNiVJBC6xFHmoH7dmr2u2XnyVO9hf9uO3QE6PsXiKcNEOZiHQxysi-PnHYfI4Fc5eG6AwTHJVBzYvyQ6OV8JZzo6tbVvfkF1dL8LYHfzKKaKk9qGZh9SXj1nYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3f6e0903.mp4?token=edVgMp_8Yc4niLfSasGHl9utvgs7fu-kOnSWwq5nVOgzwZNAbH03Ok7WR6XgGJy-8Modt2ksaqCFm_lFZID1nQ-VUqVhUKr3kHzE9m_BD6FQHFqSM5igHIdOigQw6minKBzVIKazeoK6dpsWW0RvzxQNL7x4I8S_dp4tN7uR-7kt4PrHgXsdvISsP2bLbjLulCBRCmYdhMX3DJ2iJlneN_M49CE5hUNiVJBC6xFHmoH7dmr2u2XnyVO9hf9uO3QE6PsXiKcNEOZiHQxysi-PnHYfI4Fc5eG6AwTHJVBzYvyQ6OV8JZzo6tbVvfkF1dL8LYHfzKKaKk9qGZh9SXj1nYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛ من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/28757" target="_blank">📅 21:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28756">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKHipfXmbp8sZ-1dtpZUnYYFuH9oX8gpoX2R3DSyQH8ao0Gknkidi4PsOVoqdPr-Zho0EUoI4y8JyZA6_WK19pH5AniolvnMg2mpb_Bkn2uM2Nj5858nvRdSMt3gf5YKF25bQey_x6PWE8Vu6uiKzNxDmdEAIXq7Eu2mzA0ffX7sHz9rTroDHgRWoCnoEzjZnvaKhRpWpZToYfaT003Y-uoNcSVL_cRtEiMHYxMGYZx8pUtGW-zPyMo8mq39kLbr_QCI6EXjUZwAA_T_RzUHbDirf8BLmw8Gac-BEpS0cWAKcv9XK3WNbkFJ7ovML0AvMQ1igMfDedffMFAvjWcTIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
درهفته‌دوم‌لیگ‌جزیره؛
من یونایتد در اولترافورد با درخشش خیره کننده برونو فرناندز ستاره پرتغالی شیاطین سرخ پنج بر دو از سد ایپسویچ گذشت. فرناندز سه گل و یک پاس گل به ثبت رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/persiana_Soccer/28756" target="_blank">📅 20:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28755">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=XUzLDy4fQje7XrwN7jCbnBnLq2WoihiIM-GA_9Vn4-MdZDZyLkdxYPB259D30KrdSxSp-Zrb2pVWNh51b4li5UKj0PiZz_CVxjF_WtpDV4HU3GaVJTvzDuWYm0Vv_LodVFSMXVDwO1W4LU9_rwmkvUICIh_6h6pAXXn-srxkEQHscMejCAqZ4razByce_D7AZ8fvpYJ0HhpV7O-LKhw4ln-S1H30ypikvd8WLO3shcB7iPoHgEPXXBQ6Jxbx_10XdaBzDEbY4vYpXsHsVaysk6zbmEke2SJLygepPWKq2n-4fgqyLX1c5VoVO9oHo8vlk4HvWYnCuzo9cyKCWQygOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cd133737.mp4?token=XUzLDy4fQje7XrwN7jCbnBnLq2WoihiIM-GA_9Vn4-MdZDZyLkdxYPB259D30KrdSxSp-Zrb2pVWNh51b4li5UKj0PiZz_CVxjF_WtpDV4HU3GaVJTvzDuWYm0Vv_LodVFSMXVDwO1W4LU9_rwmkvUICIh_6h6pAXXn-srxkEQHscMejCAqZ4razByce_D7AZ8fvpYJ0HhpV7O-LKhw4ln-S1H30ypikvd8WLO3shcB7iPoHgEPXXBQ6Jxbx_10XdaBzDEbY4vYpXsHsVaysk6zbmEke2SJLygepPWKq2n-4fgqyLX1c5VoVO9oHo8vlk4HvWYnCuzo9cyKCWQygOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته سوم لالیگا؛ سومین پیروزی ارزشمند و پر گل شاگردان مورینیو درفصل‌جدید با درخشش جود بلینگهام و امباپه.
🇪🇸
رئال مادرید
4️⃣
-
0️⃣
مالاگا
🇪🇸
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/persiana_Soccer/28755" target="_blank">📅 20:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28754">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm1b06vymIBDN_uPzNEu_z1AAzJqzS2ifRfu8XCzi1RfAQNQWLB_qpjiMIMeeCpXZIaO86Igne5UjGM8zmY8rwl6sht0PTLABJam2KGCMaNFDaxa9qgUOCzAAE05GRE2UgFeSy5RMsQqdr3sGRGLtEgBBrujxsn857U0lGB1kIs9oDZk09yycmVIGqT1mh-9etXzj8YO-dOwmYCudopLKOx24N3U5Ykeu7hjaEDf0HIC2m0DqRlpS5BIki-jPstgqbSc6Wl9rquisy01jMMtso4MzZm5AeeIbHlIWFVOgCBh1vbZywpWfNFFXeSzHdNzefbN_JWb1xFBEKmhI4Evpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ دوست دختر جود بلینگهام ستاره رئالی‌ها تو ورزشگاه برنابئوعه و قراره بعد بازی دست جود روبگیره اون روآماده مسابقه بعدی کنه. جالبه از وقتی بلینگهام باایشون وارد رابطه شده جود عملکرد درخشانی درجام‌جهانی و باشگاه رئال مادرید داشته. امشب هم مقابل…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/28754" target="_blank">📅 20:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28753">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1KW66FJC7GvgJKA9id_dmfAlMsefdiV3_aR18sFeNAqwpYit1wuY0AdzrJNJZE5CsEROqjog_HUlR15u-wBhbmvwc1oVudHCm-Z7Bw0hfMG9smVv3BYAR7b5dKwEFxvi0KnGXv8_m8x0Yrtu6-bIp31O_MwbfVjB_nex-RFi6Vz4aVhtxs1aBxAcwBClt7shRaTaW2uxwguAKA2rRFF3uTNQmrTqGzlNyHwY1Ke0KGwhMjq1QYCrNBiEtmbcy6DFTTC3XCmnxsbtstq4ZWvhvinl83OoRZnvB5Ca8gO3R8F9JF7kREKJoNOGluluSORWTYAm0E4Ubg3IMLFmQDGfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/28753" target="_blank">📅 20:27 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28752">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6tlxeHm4tn_xbButMZAEb-LPQbqYL1jfCQKuAxUq8T5RZh2rZxvEf_9vm1kNAaHNkQ-7hDZYbYTTA6kfCLNGwrFaLCFpKlyWPMVHq2u9DKWU8eStg9C9WL6L5sAoFVO_YdswFQsW0oViG92evCqgEZVKCuS_D4CIk8BJcCEDXleyuOShYRp52LgLIklmFgzxQ-5uEzSlUKhzZ1wAwGzuYscimSrLGIlBemElVka9iFVIlCELpe0GsAlcN7NU6_9M10DBcvZBOfkgK0FMVtKVS1Y2PYaMCCVf4_yalLWI6ZkluHYp9V6AffDf1rTMnfwogmZvECbEEstpqawrWkcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/28752" target="_blank">📅 20:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28751">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8u1pLifQBI64VYVNeRm4pqVvsybv5XxFJEwErghky8va60oHwcryHkUqluBQK7TL0JOdIpclNReyxyDeZVPYmD1Gb1qHxdnWxEk4HKED8aQpJG33_Bw9DEDd8esl3ChZy915IHTSyFZbkYQq9vEdlaVOcoq-0dRVhrKLbIWEJQ_S0UA9Gl4LlFOaa9C4x5KYbqdIRzHkYAWN2Vya3elYndpKlTcGRpzF1IYlhD-e035TX598r9mOvAZ1-RAiMhgr0ohzz2FAemCe-hqmJn-1Kso90jNPzIdR_OdBYOBNwoyY9ah5O70zKcBHLhuQcnuQpPFnM9yC95BuqpoOzaT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/persiana_Soccer/28751" target="_blank">📅 19:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28750">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=vJFe824170nJmZHHN7VSq7m7dRggJTV6MdhL72F_2l8wlxpWgBedpItOR6k1jF76NMwh4VZMwYiNtLIxPBv8p1m2Oh0TJ_nvdDAbZuhsLYZCW1PFrqZhZbTMhCoQJb9YaXBRwozO9zIXp61WvGmTJROEKRRvN7mmnYG1rYosD3ql-XUj6x1E4JCsXxS1XEbb8G23fTwo3bEUJl3whncDqscl9TYQoiBmNY-gMeNP1QF2lV3ZWk1x9FaOCO5tktB7yHYEvQ8gmEMjhl2h_jM0_IpC0tjhjSQdqh672OEWOvqFQQQgqORZ8uKye5WqpX8qTnapk6hD_3MvLC-mcC4eVTqKTGEHUeNDnQyxoc3CFWaHzcjPypiRFYMSzPECJlyXTYlHCT3npLOU31nE8dLNeGxTIlc_kPPhmNCJX4S7JKgGRK-f57ffz7o_t8kAK4cUf43ZOgVhwPovKZw-lwXp-pdToE32UPzVYYAQNJ01-ePzZ0ruLwNlbFEFnQe_vDhmhZN_2vHlVakwZbgEhNQUuOjy3TKa3zDHyK0-FwLyxEDWs4Qyg59yoP5DWxPAT0G94QnWqksMcJrKGEZtSsGp0vfseasUOLzHYgQdrdx2MZmEBGAMj7UF4mC4KcsPVsKa7MOSs6bDUPN94SgQUy9iyiyA-0t6BH5I5ew0I2XZWFc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3859b36e.mp4?token=vJFe824170nJmZHHN7VSq7m7dRggJTV6MdhL72F_2l8wlxpWgBedpItOR6k1jF76NMwh4VZMwYiNtLIxPBv8p1m2Oh0TJ_nvdDAbZuhsLYZCW1PFrqZhZbTMhCoQJb9YaXBRwozO9zIXp61WvGmTJROEKRRvN7mmnYG1rYosD3ql-XUj6x1E4JCsXxS1XEbb8G23fTwo3bEUJl3whncDqscl9TYQoiBmNY-gMeNP1QF2lV3ZWk1x9FaOCO5tktB7yHYEvQ8gmEMjhl2h_jM0_IpC0tjhjSQdqh672OEWOvqFQQQgqORZ8uKye5WqpX8qTnapk6hD_3MvLC-mcC4eVTqKTGEHUeNDnQyxoc3CFWaHzcjPypiRFYMSzPECJlyXTYlHCT3npLOU31nE8dLNeGxTIlc_kPPhmNCJX4S7JKgGRK-f57ffz7o_t8kAK4cUf43ZOgVhwPovKZw-lwXp-pdToE32UPzVYYAQNJ01-ePzZ0ruLwNlbFEFnQe_vDhmhZN_2vHlVakwZbgEhNQUuOjy3TKa3zDHyK0-FwLyxEDWs4Qyg59yoP5DWxPAT0G94QnWqksMcJrKGEZtSsGp0vfseasUOLzHYgQdrdx2MZmEBGAMj7UF4mC4KcsPVsKa7MOSs6bDUPN94SgQUy9iyiyA-0t6BH5I5ew0I2XZWFc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛ برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/28750" target="_blank">📅 19:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28749">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXtrz9r2AGmQU_oic1FMlaLY-2wnKL9KyqJ9m-9jnrjx_XZdkZomarm7gW12WNGcaJyFAJyPi21sZXBlejNeMvBkmqjgzUCpFeKCLkU2ucPfkIG_sERgDmGFVUOxMMQcb87h3dePYcjv7kSIhIiGr97C33JDVC2MswwAKa6cInUVXDbwtmqkEUcm17wI-s-r_q7cJyN-42YwEbWiAfWiQ6jf_FGWG6aEIIwJxHZkCDutL9ohDRh5YsI9beRCm_-Vs2vbxXpX0_MtjvWpU0SP7QlweIyqqWt_sld8wwgq6Mbx3n-TpShYRyFmhr3Hzo6N4ijWlnLlHi9kLekHQf4GXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب هفته سوم رقابت‌ های لیگ برتر بر اساس نمرات گرفته شده بازیکنان از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/28749" target="_blank">📅 19:13 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28748">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFnt9OPRF1Cec18Nr-Ewq3CbemLOZqelsblybvh1x56hkl4b0CrKVgXIjc24OT4rHbHYWdvsyUMh8O9fLH7ZUr9Iv6ffXac_-cfVrDBC5ZJGg4p3U3_SfyONyazIc210qNcs_pXm0nmxmHq0FpeEEBFfJZ2aybzzxuITqf1k49JV5Izl84DH436E2oFtrwsZtXg1k__GGTFDYstULvoN9xh4LvB_XwQ9i9NqoCpyoljkflLKVeilXrHLa7kRVM-EfKi5B3506XO8Skk1ogdEKkC4nIrPvMxEliS_yNZsTTWN9v1n8_NAZcdhsHeUnqdkwu-pvlSJZWUTnrKDJedkMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
رسانه‌های عربستانی: کریم بنزما در لیست فروش الهلال قرار گرفته است و کادرفنی این تیم به مدیریت باشگاه خبر داده ستاره فرانسوی 38 ساله سابق رئال مادرید رو برای فصل جدید نمیخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/28748" target="_blank">📅 18:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28747">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GeAYs4uY8JGobQVcMEGcFdUE4FKmD2fnXJdReN-USDp246QIHGJP239IYHQegVh_NevvKR4YHBUp7KUaLWxvJrBhwdycjqBnXhfLkt-j0mIklOb2w3trQ3hPZ971XI0L6bdHV1V6rNK8k_w9hyngq6b4dPW8anGV938c2doEySSyGGyrqqLcej7usafv1Z7AT_9JsKgvdFr6RFJksNkdbhEac8A9Mi4aKvxt2wC57zzLNFZaUDC-jQVDgcqS4M6tAghmGMPYzi-HF85QI_47aJcmvk-ykASd_TycA4IS9fbb_UQp84CQKLuGCzqKlmXNg_r14lq4P34Q5tPSrK-nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌جزیره؛
برد ارزشمند شاگردان ژابی آلونسو در استمفوردبریچ در دیداری پرگل و تماشایی مقابل برایتون؛ چلسی بامالکیت‌توپ 25 درصدی این مسابقه خانگی رو از برایتون برد و رفت‌صدر جدول.
🔵
چلسی
4️⃣
-
3️⃣
برایتون
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/28747" target="_blank">📅 18:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28746">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=EKaes7_lg3zhCdLevNN67dKGkG91OIwzDJ-foLfmEjdBjOXouskk09OEA299wLoSmGvNFG-hfuOBcia1tmQuiEDb7nigIVA0FXXgFBR-dBsyGLP21L2S9k7jSS5-VLgIzOsLyZ_oEyEDavz-fpTVYtgilCH-4itj8xrl90dW4rUqgsPGOLOleqw_tRyz8RjZEqH4HfqbcagdYG13HODxJZeukBqeYBSAGrTMbMGPFMMeP_NrhB6t2f3avbQKItFsAfiGctPjopZpnOJD9f-Ji5ciHsbpYcyv26SlpEU_zRoZOcj2QDm-_90LOJA6_sQ2NoP_M4J-d_RSMEfhz6uEAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ad7e62a7d.mp4?token=EKaes7_lg3zhCdLevNN67dKGkG91OIwzDJ-foLfmEjdBjOXouskk09OEA299wLoSmGvNFG-hfuOBcia1tmQuiEDb7nigIVA0FXXgFBR-dBsyGLP21L2S9k7jSS5-VLgIzOsLyZ_oEyEDavz-fpTVYtgilCH-4itj8xrl90dW4rUqgsPGOLOleqw_tRyz8RjZEqH4HfqbcagdYG13HODxJZeukBqeYBSAGrTMbMGPFMMeP_NrhB6t2f3avbQKItFsAfiGctPjopZpnOJD9f-Ji5ciHsbpYcyv26SlpEU_zRoZOcj2QDm-_90LOJA6_sQ2NoP_M4J-d_RSMEfhz6uEAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
#تکمیلی؛بعداز اینکه‌خبر از مذاکرات تراکتور با عزیز گانیف ستاره تیم ملی ازبکستان دادیم. حمید مریخ ایجنت‌یاسرآسانی و جلال‌الدین‌ماشاریپوف در تلاشند که این بازیکن رو از تراکتور هایجک کنند.
‼️
باتوجه به‌باز بودن پنجره نقل و انتقالاتی تراکتور فعلا شانس‌تی‌تی‌ها…</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/28746" target="_blank">📅 18:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28745">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4JMvh6EQKfwQmKuv0i0EZqbx7VuQiM2EeuS8xalbWjTPBbTYh8gVRVBdbFel27jxwMJUPSoMKG6CbJz7x3YBmqdX6Y5RsB_ClI3wCbizxRjJmTmguYf0uXwTTOHa0z8HUGAbtEmn3vboejW9PU96c351xGRb4pYGrCoeIyZaef3Xw6_C9Lj9XVxpF8zzYvDmLBWzKwh5wQG2bqaKsFa5EjrR0U7bIhinzvcNfmIskratXphUu379ftgg1pzNPWX1iYnhORzmYyA3K9gEDRZdDKmRfPthAj2P0Ps3xwQ3Z3NSJELaAYjUfHReseRkMp-waT3BXEmut16eJTZRr8uQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باگلزنی دربازی امشب با ملوان؛ علیپور با گلزنی در بازی ملوان به رکورد تاریخی علی پروین رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/28745" target="_blank">📅 18:16 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28744">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKUjyAQGtlgj2aS5fuqwDSvq2VbF_PSprt0x4MTVcRsSzDsdqMkpl15Tk9UA0AyFXWuU4-xOY148CSEfqmosmV3d5Pf3KrVXmTi-kGRcaxhea_yUB8NDNPNcKRlq53TVIMqKM_EE1hvA2yaheoI9xlCWQZz4OrT77rOJ-QDNX_jrqSggTtO1ihQEhoIsjwbyMIwhsDhoQd-8N-4ft7RfHK9y55XQZh-RRKd6A2hvL7jZOs_V-ptIq1sKfxfEbfxT4bnus6WeU9U_6ZmaVycrMYleJj6cDcbMvyCGGMTOTQPlDsRZ6jQzaaFaWPp37EP_v8UNTTmNgOFsBuFuOnRO6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه‌تراکتوربدرخواست نکونام با عزیز گانیف هافبک دفاعی ملی پوش سابق البطائح امارات وارد مذاکره شده تا درصورت توافق نهایی با او قرار داد امضا کرد‌. گانیف در حال حاضر بازیکن آزاد بشمار می‌اید و مشکلی برای پیوستن به تراکتور ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/28744" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28743">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s91bSX1tFbzamGh5sxnCb4-jriA3W3DS55WMOJw2TZiqcssEQDHYo-kGmzA53YoGLs4Uuo-mdwE9DXHR_m-3v3JvRyz3cR5qoxfSocz1A47b_RwvZRdKPCpLuchRc9P769DpblrUZJ2Qyr2LSYeWrrYkqWTF6pY1B68R6aZ58XES_uZXSWbULkE6nh66wB-7Vs3F7ZiL-Kqy42TKQtj-1YzuUeFROhnfoS12VCtHN3z8FQXDShLWbIgCFJ4zo5q0DaP-u-f-7uMPxExlPASqxSHBfQ8Vp2Fr5soqmTKwhMhyneSIGtDwfwdISDoVID_0BN63R99IHhgUpOv_XN9HOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/28743" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28742">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwPOdPYMNw0pFMbMMNbbHjzO2n5tahKM_2ycteGvZ3dsSfVDvhtP5oeRBxVD3eMWwznbrovGO6JqPJl9boe9S6_X6xgVsa2youiVbZD_aImCVooaUzmCZgAV0zmmQJ9P2eCa7BFKfXVTSj499n5ayGSPSQgswLX1_DwKEjxZV9Hiy2MJNXk81rCm4qen0yakZ2EHzyilsFecJ59GIwfMftsBC9tu3pWE39u1u9kZyKFonbs2AKKMfA8SGhKj8zpG_28VRLQWz-HivvCFXIQ50-Hwtol-jHAM1rBJvt4A-h2k1NhA9iTMmF1Pa_ByLg6_o0tR5So0cGKZ4X2P9QVMww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/28742" target="_blank">📅 18:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28741">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob4kxLlWUjOKqYVcWvr9b90CPla6Ohdp__wPiclAVZDckxYKxSkP_NqLy0xqOh8Wf2TH9Qpf8Eqm4hm2vPC9SlNrgwFZSFut1I4DmnyxSE-7GJ7e00YMU1hZDSZbtoyYUuzHLEDDOshgVX5iRuG-U0rxxfrnoPwzUEicfewvgQkGpRH1XGmd1T5AgEtagy6gKMOYMrRCKJ1PdQ1cVZf2D2jbqxefvpTownqQfBDnFcQ1LrvJIwLFon1TJnZ1vRicrk-PlkExWBY7y5hM1Kq0LtfFloMgBMIqM-U7yCRKr6xc8id9lUtU0r6F7MtAoN8YWiLj7N6BIa7Bl33dcuwzmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سوم‌لالیگا
؛شماتیک‌ترکیب رئال مادرید برای دیدار حساس‌مقابل مالاگا؛ ساعت 18:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/28741" target="_blank">📅 17:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28740">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9Hswb_cs0CVj2XJq-v_Qjif5FI25kNKj5PnSqhwFCd2Tco2h_FFdJOk-ABW3DWX8eLwTUYgtic7aNEWUROU9uxoI4FzOpKyzffatrWiNGA3qqamYIRqcSZxz5hYNUgzGhtUIPsVSFfGrHp1kSmlBpjCzOwFWs5xPL1Ns5xX4ygbYPA22mPuqmqNJWu3HEv1lqRhdVuxTjvYAObNbdAtnn6KJpRKmp3SaJ1DkFtmc4Nxs6sMqAvyiyNL7beIfQWtAO64DGt7zlGfYc4oBSgAe6a-CQqVHK84ylGX_qEBxU0tXljsBt0hAKi7_HOKnYpLwhmOOSRWOIcCBuIzuO_DNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
#فکت؛ اگه حبیب‌فرعباسی درمسابقه این هفته مقابل پرسپولیس موفق به‌ثبت‌کلین‌شیت شود رکورد وحید طالبلو رو خواهد شکوند و به اولین دروازه بان تاریخ باشگاه استقلال تبدیل میشه که در پنج بازی ابتدایی فصل موفق به ثبت کلین شیت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/28740" target="_blank">📅 17:35 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28739">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGkPBIcmRpQmQ2S8VlJs7UumaMA8m5mmz_MI0YDZl1DICSTRGwBb6RemJcnwReeGbiCQS82Sq-e0hq-nZHCbA__U6w1MOBKOoq8mMbL9euW17WH_L7ISbR4X1z0tjjp4P2kV0PR0uX2tNjDGIB42p0z62aWO5j_-WXN90Em4ghMM1lGnXCutYBrCXwBMELbhKjqBDHnwtB1xLyWIEFEoKE0g9PsxLcr0bpPbWI5TRixglAQ-V83g7Vgp_b5pMhnU-aYAdqQyc9X-5CUBD738Ws24TfIdegePFQbx9cYWYrP1xTf3mcq0VXNjtBqUY07Y6-yTYCM8jdZqdriavZxcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکردحبیب‌فرعباسی‌دروازه 28 ساله استقلال دراین فصل: 4 مسابقه، 4 کلین شیت، 0 گل خورده، 14 سیو در 4 مسابقه، نمره 7.7 از سایت متریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/28739" target="_blank">📅 17:12 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28738">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTi0AxeliMdmRBQyZwCsuLEhYiHCTjxQ4RXGBVF98Iic_1nKkYUCchPxG05Tax2uk_a8bWx3qOUSFLMOSzSPLexCMFXOU-6qhV5T4yEPfsUQe99Wm2MbbiccCtA__qbM6Sl2rEMXRIUFBKGCMp8Omr3hBs3JlDaiTaFm72XQ4pft2mWXEeqeb_zaW8qxF8OYppwM-A-atT7CMuToOSP3C_xhAK8bpXhL8eOaN5e5iCwEU986YB4pktgB8G0GpNomfKu4ingHTuj2JP624p8k8JFq8L-qmWyFSrgxLftsgbXfbQYemZyHo1zXkxRq6JXGcZBhfAp8Vp5icyRjL8RWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/28738" target="_blank">📅 16:56 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28737">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FduZJIrKNGm7YO_w_RFXDWE4Pf8mpsaiQUCoSKQlNmQ5a3XskAIl_OWCIG9xWab7KzrieLcVtsvKl6fbUPxJokhQf8rSrbCTZr03yAs0NTh7vGoVD3C5fhC-0fozjVrLpw3qQo45F3nQGs9t6twFiuH57vGn3nVYbiRlqCjGfNZ-P_mgPTy2Oyr6iy1YAs8qsj5MJUU2qLPnlYRgXSBRlsZyBgZfpdhWO-jwMkS1W2yoM5dTP4uvIG0CGn5oBnGLBVluiIdyVWyh3CHo0exGMXw7aTk9QNUE9ik362wq8doI7vN0_8-5EAGJ4TpJN8LYY0D8Xi6Bsh7T6aejRZ-jYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#فوری؛ با اعلام فابریزیو رومانو؛ گابریل ژسوس مهاجم 29 ساله آرسنال با عقد قراردادی به بارسا پیوست. آرسنال موافقت خود را اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/28737" target="_blank">📅 16:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28736">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG7QOVvVFjpf5SecQsDXPuO78rYPAsg9r_cBz38UlDzGQscs5-lowAHgV3oH3VFm2LWupKv0duL212Vd6kg0F5y5zEypYk9UYGE04M1jUWiCBSSSLmMZvVuGS1gMiuiskE7frNgRf1k5J1zSdB9waAtIgKDbIE60VKJFPMSoBxo_fnpjm_adTxQNt6Un6EiZzKRDuf_86SsCODsTJ7XwqpjT7y5Ac02YyQYHnYnsGLLc4UUURrjhYTs8ANcPasG5NzJuDMfn3z36i0PsIxev8aHAaq5IQ6DiOph7Zlec_or-gfUsSvldtQ1RhqxHvbheN7aglYl5U9IqxJr8LMeM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی: بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/28736" target="_blank">📅 16:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28735">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMlEWNOa_oLXKceQEb4LF00qHjF3_Aq3LX2qnZJiP_zY_S6eJM1M1yZ2xiicJgxNDGs-_qmWsiMRIbtvyVr_eW-iIWxUC3fCD9m4BTxHFhA6gLw8_j_PrVWkYDLY679EHVmYgbB6RHX9sJaz1cFEtOY-LQAeJUworLDqo1ul84fQI3E_3Ka8J5ixTy5g2QczSaUKKDu5LQU4QGHiewajWIyV5KC8nTie4Wuzf5HYbUDyqqAOuFpblQ8CCpa1Tki6P_b7q9jZncxsLfRTRZGsbyIa9eBRt2sHQ66dprHqAsJzxr7alo_EQZGH-q-oQCfykeZ1sm_sDjjfp8WlaWoW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
فرناندو پولو خبرنگار اسپانیایی:
بارسلونا مذاکرات خودرا با گابریل ژسوس مهاجم برزیلی تیم آرسنال آغاز کرده و میخواد درصورتیکه آلوارز جذب نشه گابریل ژسوس توپچی‌ها رو در واپسین ساعات نقل‌وانتقالات جذب کنه و شماره 9 آبی اناری‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/28735" target="_blank">📅 15:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28734">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6lJgw8hdSFYszg_Lp2iJG2twJV6ugXrtrYqvXvPA_OTDssk7ijH2uB1gQkb3i75atdR20diDpfhZGjyVCaN24G9f9AjAE7FLLyV5QtYuearo8qBvqEcGnfFYzbur4WLWgEbmTqtBmO-w4gTmrpFgTHkpdftEwFu5UWv6oI7UNG6v36gxGD7BKhO0qZ4gB9stF5mZ6y0vy4eMYWG4sdD_U4DD0QpPZpYu802I_x_VR4mUec-wDr066VZkH29lx66cjl3RgNUkNt801_ABdg1nzO1UyIQQVl-cyWEEuJl4f4b4TrQkfYrp_VvIm_hPjkbCU_ABDhDpCqLLyWlYfxP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی پرسپولیس در استانه دیدار با تراکتور: به جز تایم فیفادی به هیییچ عنوان بازیکنی به تیم ملی بزرگسالان و تیم امید نمیدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/28734" target="_blank">📅 15:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28732">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UFXiB_JfoSIZ1VhdHpx6m8ccPBZTft0Tq2jh_pZELOfeLXAFT5k567KPktvsean9EMZixxpE3HGw1cJjVLRRj9QdDxPRo2estOCXg2xTtMoNooDMuzdt3-F3wzvPyAKecgPlBcsEVrmfeq7d3XJPypr6mAL1BoyYtYyl3RLl9Lo5dNEGbM232ZpVMjpTnP6Tddl7CPxCr4rfBSF9nLyFkBVJfAe_z2H7x0tK0VNkJNqwIT7V5h2FZSOCKzkzbOQ5kR131EX9a-k-qfIOR1fHIfBsZQbzaiMOnSJLr0UvO3CpWzDCMTJ-_uuzx_xTLLYEmj2OO-chlh5KK2_DdNzidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdoBImd-nq9M1WNMgG0Tdy0m9fM5CIfC-Fp2hDfGcTgC9XPychqLQEflIaB9t2Eemurbd56kRSoH0BmdCjuL9-gzUSoGUsg0eTvloHiz2t_ibb0Hmo95kcMSE2Bd5Rz2QvI52VJr7wggWpQpxK5jVk_XQ5DiWU-iugLL_kukaASovUjjoiGf7mHJOMqU8P0yb-0GUkHLmVPuP3PStSOX-_mV8gHrvy0iTYHHfcDLUc9h2LqR4OlboZZxfEBGf196nGfBmJZR1wEdy9n5bLgnjyCkgYvd4b9TPtJcquU3YNMd0-KecvMgWJJyzk--ndRbhnvKuvfbKlsqItmTDUDzKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚪️
بانوان هوادار حامی باشگاه ملوان انزلی که در تمام بازی ها برای حمایت به استادیوم میان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/28732" target="_blank">📅 14:50 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28731">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgACXTdURjUHk_NFoXk2QJ6E0Wmfj5A4rmpYFofZkpr4PYG4bSf10FLC7QSUUk6O9Gv_a3u4NSDZyRHxwdzRFqbduSgPhIgTWb5TJimlcMZotLvJ_rTLlCWSXojWMTX3De3C6kLJv9VXuskud9xanTCc333CcMJl1rHxWJKCkSs_f1vWlW2Xh6Peb_BOxxIrrLBe-uzcDLh7FNwN5stwe0KiC40b8N1YX8xOMHa3pHyEV2aCLx3b_1vsA-__kRXTfcugaCUVDPbpc87x-FIqHp8ry09TtabPY93t1iXH-QBRK6Xhbk3DIGAhf-23pimEJmqU80ZA2lwSsPShX3CNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌انواع‌کنسول PS5 درایران؛
PS5 PRO که بهمن ماه 40 میلیون بود شده 251 میلیون تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28731" target="_blank">📅 14:29 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28730">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWo9ZVzSoSTxmv84y87O6aCVpflz0E3VhmQcNoi8tj3pHLy5XnOXiP_I65NyMu5yzgjXUJJRZZOEGegJNeJAA88vLpk05dJmrdtv9CPp3lIqONJNIqgnSTbqPdHsmNGqj_A_27kLjIO6NYw4bAA8lHz4ssLLQwsUOKAnTbsR-_YzQlq1OEmKIX3kxMexZnBvg1fedMaVTRct1uU6OPMK7qQEUdDlPtYovkJFfU-6iBUot9l2TmZeRrU_b0TmNRomn-pjeR4ey5i61hIUeevaI1IUNRcc35nDxtkWMffeIVv4zMbMQEzNmex5BrpSVfUrFg6YEH0IwJkCG2GiCJeQ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
مریم یکتایی دروازه‌بان‌شماره‌یک‌تیم‌ملی بانوان و گلر سابق باشگاه بشیکتاش با عقد قراردادی به مدت سه‌فصل رسما به تیم بانوان استقلال تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28730" target="_blank">📅 14:11 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28729">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgbbL7Ky8eNSn9WqZ9m-zTeSuSLMlEpbWcV_lps2tqSTVopKCuDkYBbMdNqTGNOMh-zMmt7dJyVVCpQMWWJtKp11Nr1rg5zLDeGTppnIvpebl0bXJQKD70wpdrMpDgj4_vYw3e1etIByDKo9PaEid_QXmQq_0VgiSTIoFvldeJeoYz4-BQij8cw5dfBE5PyhcIiBPcMSsmmgnXq-p0q8AZdaQx00RvV_r1YZlb7kNROyM8srJE3UA6t1RFDmlSHT4zS1OyWwg8kGlpQCT-fKLdq7cwPyBN57N3uu9CtLAjsmFJTiw76Uq4XLMyyECx38DXgSjwdGpils8SL9sjlbUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از همسر عثمان‌دمبله درخصوص پوشش که هرجا میره ماسک میزنه‌پرسیدن برگشته گفته این یه عقیده مذهبیه و دوست‌‌ندارم‌‌چهره زیبایم رو جز عثمان کس دیگه‌ای ببینه. حتی کنار فامیلامون هم ماسک میزنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/28729" target="_blank">📅 13:52 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28728">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520eadae82.mp4?token=RTYkvIXflAU0ejpJWuiVgKqa0if7HUjr4sZEOYIYvLZ_3V-gmYJ-qCF4Ag0iAsiJLxJ_ei-kBK6dL88VmCVyqSyCexd5lsvZhm8_ZOX3IaXLmgDcwclv1z6wV63TLEoUOzSWfGvAkp6LO7TWmExq-nf7EdS8a-vmvWZjHnxjVmVyaDX2xUBonDBTnABgJBzUvv1GTxN8toJXm-xK9CgPgEzqhgGD1-C55GKEotMpLcNdzgzLltFJIRWtGViKHbqzPGDD_IbEfh9gcy9dfkEmRXbtG3O1x_SE8WrqMndXScm2Uto0bT2aJthrXvohG0fJhGlqn5lCVBKI6UrqpolNXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520eadae82.mp4?token=RTYkvIXflAU0ejpJWuiVgKqa0if7HUjr4sZEOYIYvLZ_3V-gmYJ-qCF4Ag0iAsiJLxJ_ei-kBK6dL88VmCVyqSyCexd5lsvZhm8_ZOX3IaXLmgDcwclv1z6wV63TLEoUOzSWfGvAkp6LO7TWmExq-nf7EdS8a-vmvWZjHnxjVmVyaDX2xUBonDBTnABgJBzUvv1GTxN8toJXm-xK9CgPgEzqhgGD1-C55GKEotMpLcNdzgzLltFJIRWtGViKHbqzPGDD_IbEfh9gcy9dfkEmRXbtG3O1x_SE8WrqMndXScm2Uto0bT2aJthrXvohG0fJhGlqn5lCVBKI6UrqpolNXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعودپزشکیان‌درحضورجبلی‌رئیس صداوسیما:
دیگر تلویزیون نگاه نمیکنم وقتی من این نگاه را پیدا می‌کنم. ببین مردم چه نگاهی پیدا می‌کنند. هروقت تلویزیون رو میبینم اعصابم خورد می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28728" target="_blank">📅 13:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28726">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCeuw6WNCvS6xfOVjAvy6rGNgAgcoOmLsZsF9nAfm-xhqSGu6gNM6D567nGBOiqvhDTo8G1HfDHAOKj7RfsLWcNWyh3qxWsM1LDhe744Sa8EgwjEQrhsAM_yeud_iINV-qHxzpdZ27TLgcD48o5j0XNVuxNEi60fYYkgxnjVWWm0tDFjgadTF2yUmNASjABxbXv0HDR4RP5wqcvrcbjnsy0Bk75brihFut1rtlI9GIYmiV1FPl-oiSRk9npOJ7PgpAdZEnYLOl96WpbffLLunj67Qfum9F-7vIf_IflI1gRxzuWN9kMqwc4lrfaNCbBrN8a1XC7Jv6YKKdNSkENPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
جوسکوهای ورزشگاه فولاد آرنا دربخش بانوان؛ هواداران بانوی فولاد بعد از سال‌ها بالاخره از فصل گذشته مجوز حضور در استادیوم‌ها رو گرفتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28726" target="_blank">📅 13:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28725">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">📊
تمام گل‌های هفته چهارم رقابت‌های لیگ برتر جام خلیج فارس؛ سیزده‌گل‌زده در 9 مسابقه هفته چهارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28725" target="_blank">📅 12:45 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28724">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yco4Bbe56wlgqUVMXcJJNimddwFUTjCTNTFKsg8j-GeZZctE7vTrnu-aFdXMTSb3N9sgDg9MoY9oy-jgM3YtXqrT3qgCM2xTxsqzaQ6ymc1DS48GG3QagQfp_0AixA4SufcsWGRENp7sU3yBu36MO6xZ-218uZWYqpXATtzkZ4DSfijwkYeiPo4Yaf0l18RCFio6NbJuV57P23xHEYMSZOJ1bU4FhVrFndRNdsI9YVLgn2hgUFf-y3I6sifz0ZS-iJGlRYRucXddRkFpVP_TdJe4e5CfVDVDbpxYIcjk8ynkVyXaeQ-FAv8XHsrhXVRIVCEXKkl-xZRpwpMdB6uB7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
درفاصله سه روز تا شهرآورد؛
کوپال ناظمی اصلی‌ ترین‌ گزینه قضاوت تقابل حساس و مهم یازده شهریور ماه استقلال
🆚
پرسپولیس است و اگراتفاق خاصی‌رخ‌ندهد ناظمی این دیدار روسوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28724" target="_blank">📅 12:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28723">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=Tn-t3JNhAPR8M9HwVo_a_ZQbYzOi04Tk7_oMvhKZO8SH8iXo4zXsiVBvH_0mTZ9_vRReJYeO7-97Oha7Tp-LaCxCqfuZFYlHgcUaFHJevMVhk3K5-3Ow6zxg_KmGsWSGU_duNHYh-2mcQPkzT6goNX4CYZPtNqfAnytIpaPjPAkiWbMIHqMtXvNWOVkFjFW-awOWWqfJOqWMfWL42AaD9nRyrNa_Mn3q7Don1Gez5XkBI_NK-N15GH-1YQaVW_11exghHREeRsFU2D8Q8kRqk6lUziFOIWTmLN32j2CbDxlv8s4dZaTqj-z1Naa8Ds-l8u1mGQrflrjXzpipS5kY4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc627927f.mp4?token=Tn-t3JNhAPR8M9HwVo_a_ZQbYzOi04Tk7_oMvhKZO8SH8iXo4zXsiVBvH_0mTZ9_vRReJYeO7-97Oha7Tp-LaCxCqfuZFYlHgcUaFHJevMVhk3K5-3Ow6zxg_KmGsWSGU_duNHYh-2mcQPkzT6goNX4CYZPtNqfAnytIpaPjPAkiWbMIHqMtXvNWOVkFjFW-awOWWqfJOqWMfWL42AaD9nRyrNa_Mn3q7Don1Gez5XkBI_NK-N15GH-1YQaVW_11exghHREeRsFU2D8Q8kRqk6lUziFOIWTmLN32j2CbDxlv8s4dZaTqj-z1Naa8Ds-l8u1mGQrflrjXzpipS5kY4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28723" target="_blank">📅 12:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28722">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqijZWdUvvyrzLPaJtusJu0Vs97lg2jxbCrs14LU8ZqJe6Q1vzN2fU-kdvsc8Ol0-Y-nMGgnveeoXGwiF68MQcAIQlD9TjaSioNJU9YDttjqnTWwDOMLGMYtNO3yNk0Txcnk-MYMjIJFD4No_tkdQZJmqxiyDbcqqA3vYkX9gay8EyxPdLgLPFNLmb_TPjNSd9ribELQWtKz6VR56W5AKIbk9EKt6rdrAfQOCAqfU0wFH5TIUrolddILOywzZELhq8vW9fJJagQ_LBKVNtoLc8wZMrs8yUB3DCXvqe-b1ulB14NCNCysmkYSbmGuzmL_Ct2BkId1OCoYTb6W5yjlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
ویدیویی زیبا از پوکر تماشایی لیونل مسی فوق ستاره آرژانتینی اینترمیامی در سن 39 سالگی.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/28722" target="_blank">📅 11:51 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28721">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFDUezmpVWoihhV5OiO4MDvKnS72PyqepGFE9Qlylgz4i9amw5DhwNNLQOFeE50CRXZDtn3h2z_85xBjmgAbI3gvP3yUwDAsUE1AceJf9fRnlTBuKbM4KDJmLT0_kbWC89N0FK2LzX-IeI40d38MKfd8rwKlhC_SsZBZhQBkgc9Tjnu8aPBIOnnbPHgnNCP-1iS2kKWepNFhdN0U9MpYR4wD-eH4QUWnJ6oUYFsyWEX7Ss1Amel4ORKfteTqDdJxvr3Qv-vPA0wNx8nq1ir8QLYQtNFByVvNZfurWjoG4ytv5078sHyUZx_gmWIFNM_uIY6gXGKfXB8hky6UkVkzUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعداز جذب دنی ولبک و جردن هندرسون؛ چلسی به درخواست ژابی آلونسو امیلیانو مارتینز دروازه بان 33 ساله آرژانتینی تیم آستون ویلا رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28721" target="_blank">📅 11:38 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28720">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuXUW19fsMZhTCJfMUr273D1PWe-ypibC8UBbmLT4D5YR7ot8lCJwAk_8pRmPdQSXJ3ScvgiiY4eQdG-PxLUf0OVak74G3Hm_2dezFa0KHk-GvyWXeTSzm4PdCnSAOKlI6dZCVESVPx85TZgd7hpSgWsews_wRVNScMV3cm6m30oPIbeNSVL0TeevWhkezXRBQ7W4B0isQDqBrzbuSssp2udExi1EMvCCZ-2cs8nx7epoSFDX5YOqs_wNxfN62nx_rYY1G9XcPrsT3O9MWAc9AS91dclX8mwqf4Lf9Y-lD6QYep_OGNW0TUIFGoLHnJxv8Xf0mr14UWVQYOKLYK98w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
منیر الحدادی ستاره سابق استقلال: هیچوقت دوست نداشتم از تیم استقلال جدا بشم اما شرایط طوریکه مامیخواستیم پیش نرفت.‌ از تمام مدیریت باشگاه و هواداران که این مدت به من و خانواده ام لطف داشتن تشکرم میکنم. امیدوارم در اینده نزدیک باردیگر به جمع شما برگردم. تا…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/28720" target="_blank">📅 11:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28719">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gf9l4GDihPQLov8HWsMspsA8PKGTDaLcyfNNr_zgH3xeL89zic5ITOJrTTv0Cf6_8cmOAlcBg7ru7HEq7zmjH_YI8LOpiVjWrR-cgYSFi9yASsFBeBJIiexVEqujSztDYO1vSpRUf5vf3BJ-xH2X_pqdEHbe5nzpaR0H9w4sAvs76XIch7W_JW9L5XGcVj_T1UsF2kNlJVIge0IVX2WnT8W00lkZGk0ohnLtLudCK2cRE2cnaPZggwui7-Fug2d0NZDW7S2HF2-Qu6adDlw7TD8ZwIrrk4r6wxpegUel1JroeLL8hzRhw9JWw6RPcy6IZPamUnyRdelXxbwSvmEsQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/28719" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28718">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4635dd1d8.mp4?token=L2pS4Bxc6CyV0JR8TdH1L_wz-PI2-omPb2kfbSi6YTgXmmHKQuY898u3u1XZFv3MjopbRvJFNFHOedDkfO73Mk-6GaO6xf74_PSOqBHEfwDi43QAanSEim7U6Pr0zbp-ak_R4NPD7qgMlESu1OqeoccFeLKlo-eRI5hF_WDFhs6ZW3aS_czievNsm2DIXXk3v8-tObTDv5Fr2xy7FWs6nmlmwIXIaJXgX9298HpwqkzVWRUjgO-qy4AFW4XrSZXvPUPaWbgJ_44N7jvsCyPzvZMHzqaGxNySvnp-UdSU6eiiP2sFq_BVtxgvSJ9Z-06tJVjdyjyQrZYnDF8lNsCPPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4635dd1d8.mp4?token=L2pS4Bxc6CyV0JR8TdH1L_wz-PI2-omPb2kfbSi6YTgXmmHKQuY898u3u1XZFv3MjopbRvJFNFHOedDkfO73Mk-6GaO6xf74_PSOqBHEfwDi43QAanSEim7U6Pr0zbp-ak_R4NPD7qgMlESu1OqeoccFeLKlo-eRI5hF_WDFhs6ZW3aS_czievNsm2DIXXk3v8-tObTDv5Fr2xy7FWs6nmlmwIXIaJXgX9298HpwqkzVWRUjgO-qy4AFW4XrSZXvPUPaWbgJ_44N7jvsCyPzvZMHzqaGxNySvnp-UdSU6eiiP2sFq_BVtxgvSJ9Z-06tJVjdyjyQrZYnDF8lNsCPPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
جوسکوهای ورزشگاه فولاد آرنا دربخش بانوان؛ هواداران بانوی فولاد بعد از سال‌ها بالاخره از فصل گذشته مجوز حضور در استادیوم‌ها رو گرفتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28718" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28717">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOhrA7lHL27Jjb2V2Wsd9nxt2Z0hYBAZRPZYCGx4tYBAew0j2mo76Yheg4UPfiYdhOsirWR10j3HGuVCaTtMMx77mXTOBllu0-q2XK1swJwiX7ZlFpDVhiXXL7XsI1nQnGG4InRL3Ghep1at2j8RTRkn7JWmxyU-SkpGzwN94Fjl0CU_QbbjdAzr9GGtz_yB5-b-13bzX9Dxm7yNFzq2gkwbO_E00RRzdqZRwpQXbY44wWqUUQpUtMRXGHn_uCzLmFqkbkByybh-jr9QWIWTdUMUrttWO2gg9NQ3AV1IuMMZwAEUhl89VxwJ2ujZEqNXcihL1PJkQcVQ4UxeV33RAg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/28717" target="_blank">📅 11:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28716">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alur9_zxePdlVigvg28sPz4Y8uGHtyCIOR69TzQfV9ctMEBGnfxv0bixXyDKNl1gpYps0FedSlPVpxnt3TudAD-IHA9YDdQtIH9twh_7TOd7ZI1T-E-iRqqk40H5D4shSpJXq_1uO0mBaIFr4Cq_T1VymDg3rdj4_-JymmAagLWPSdz0AnIwn4QingwsKQnkmtolYN7fUwF7k8KGbZgeqKg_tb6suN3qZ7r1i-BXTKCyE-l9-CYyhfJBaQeOJIA3E-d5a-j-2klCrDHcpH5eAn0s0kLIDam_neGoyIsa4auP48QAF9atxHKtkXeF96BLmzQT7J75gt2urkvyqJffzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شایدبعضیا یادشون‌نیاد ولی کریستال پالاس یه بازیکن داشت به نام کریستین بنتکه تو اولین بازیش مقابل لیورپول دو گل زد . بعد دوباره در جام حذفی مقابلشون بازی کرد و دوگل بهشون زد، دوماه بعد تو لیگ مقابل‌لیورپول بازی‌کرد و بازم دوگل زد‌. لیورپول ازش خوششون اومد و خریدنش یک فصل بازی کرد عملکرد خوبی نداشت فروختنش به پالاس به محض اینکه برابر لیورپول بازی‌کردمجدد دو گل بهشون زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28716" target="_blank">📅 10:59 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28715">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d907216599.mp4?token=gFZVsduydg36ycfGMzu_w98orTCM1MULopoWb4Isto1vjfafzwuFLjLtHZN0sPv5saaGnDcK92vhxYA4NDCoIpV2g5CnqFppOu0EKJJu7qbPfhJmacXi0ip9S-NiAB5BFrBBv3ocrxP6IXoU34nCk05che9b0j7Hl2dbSl8GZQar8YDZNrBboWkX6Umx-xkzRgx3oj-lQKSXPFTgShBFB-h5HWXEwxeqlxN3hiwoXhOHj9rpdUpcKZGAAfb-x5D0Bbahljc_ifCRFocf3buolwcOi-XortWVngZhxiLkaOS58TDBBdpi2LSF5fWuTVYeFVrrx0ssi80z3Io-_qBqhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d907216599.mp4?token=gFZVsduydg36ycfGMzu_w98orTCM1MULopoWb4Isto1vjfafzwuFLjLtHZN0sPv5saaGnDcK92vhxYA4NDCoIpV2g5CnqFppOu0EKJJu7qbPfhJmacXi0ip9S-NiAB5BFrBBv3ocrxP6IXoU34nCk05che9b0j7Hl2dbSl8GZQar8YDZNrBboWkX6Umx-xkzRgx3oj-lQKSXPFTgShBFB-h5HWXEwxeqlxN3hiwoXhOHj9rpdUpcKZGAAfb-x5D0Bbahljc_ifCRFocf3buolwcOi-XortWVngZhxiLkaOS58TDBBdpi2LSF5fWuTVYeFVrrx0ssi80z3Io-_qBqhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
عملکرد گلزنی لیونل مسی، رابرت لواندوفسکی و کریستیانو رونالدو در پنج لیگ معتبر اروپایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28715" target="_blank">📅 10:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28714">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbpRh5I5iLPmAQ8ZMJAwlJqIzwlogDaWt7717z6Z-OhLOHg8uUwZZb02QF-Ybv-VaWL-TTP1q89rCkgZ7Q422kFz_1iojv3rhKgv0ySMuaJKIRRO1ZkXwJDO3tDXy-HfPtPsYMID40evft7E71MMEKDExlvbNhcXtBfcnXQJcCHkxzTZ_kQZQQV8A2EfSVJ1Cm4pkbS7bkU0iFVmV7Y5elAj5m7my8qjD8zLKcQeodW89pAxFR1Ulf0oGFJhLHELvikaO3qBixOfl7_htJhEGNvqN8tgZ1AeVVA-KoAT-8mRh-Eewsbrz_eUw4e-tgXbrkKa-7bhXARpVjm3lOEhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/28714" target="_blank">📅 08:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28713">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
درشب‌پیروزی 7 بر 1 اینترمیامی مقابل مونترال؛ لیونل مسی‌فوق‌ستاره‌آرژانتینی این تیم موفق به ثبت پوکر شد و نمره درخشان 10 از سوفااسکور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28713" target="_blank">📅 08:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28712">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2cRV305mZf7eyU_emKIBX9hZy4vmk7fnq9WNX0KDgyhSTi2BSOmJkWSnGHLcFC31rRenShR6oPLq3LHrZXfkZGo7XehsApuPCmogPbeMWjOzz9sVDS8egwWSS1LajzOMKwD3o18D2hJysU0XZQ0lRUYKUO53NOzblLJ8d4rZQX2hfoZK1xsvixyySCbaBfK661Xy6I4Rz6c2aUt8RrDo5x5YQTtkCwokaCOFdXiPizn-rtI9dhOLEMUaM0_CRKZxsK4z1NdekNcmvCBz2UURcTfhKni_RaloaH4VQNbo5AZiCgUbRRUeCTL58NFV7ygJsv7vYW90OLfDdla5KDBsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛اسپورت: دو تیم اینترمیلان و بارسا در حال مذاکره هستند تا برسر معاوضه فدریکو دیمارکو و الخاندرو بالده در روزهای پایانی نقل و انتقالات به توافق نهایی برسند و این جابجایی انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/28712" target="_blank">📅 01:46 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28710">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrBjQIytxlJKcjCDRavjWw8lAFVocIHIBXKPzzvtdoaCLL_sPpfR22Ltvb73Yp2qjhbLOej_rLkEROEy5OdCrT-cVs3vEOMVtF54KsVaBupqKSU6fi_e9_b_NicNg6UvDvbkxh41sRabI5DYOFdz-AipdrnxL4uGOA1tXZYpRLiqCpsiYlB2rSNE0BLAUu28Xbr2ueWTUA4fbx9i4NDCMhirWpRKyGf1h_BI_-8wXZMYZ4ptdt2lYkMaHtVCc6-X2FJtLyF26ORZfuxsl6GQL7e3vHsjKoo5h24hU5VIOK2__ChXxq_82f2jI9bz-4VwP4p12uQVTg5A14E36vUwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ نبرد رئالی ها با تیم سابق ایسکو و مصاف شاگردان کریک برابر ایپسویچ‌تاون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/28710" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28709">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRHlpOYzknjQaRvt_AdHsMvGIMmUhp0rOYll3KKccWq1Thups0_N9ifM4S6zi_p-4Kfn9QSZ5-IvOdJKmZ_0_I6Du6CSg1D6WMn3KmAlfYdYeWaY6AmquSOL1o_spvgzu-HoW1fcaWD6a40sNTXxT8m7Bp9BqD_qnBciQnif18cC_Ny20U3A--dE-tSSmFN-rtE0CPxrtGqMBvdI7H_C60y14rdwKs7L5BBaZalD1Z2-OOto2M0Rgr5MVfL7CnWsOYJ3RITvRPCXyKNklV7So3Z7r29VxABzorpgMiJDN592E_NyxxRdB8a6rYolPjLnGsHoMGYF1r9xa25Gp6ZObg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌دیروز؛
برتری قاطع پرسپولیس و استارت فاجعه‌بار شاگردان دی‌زربی در پریمیرلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28709" target="_blank">📅 01:34 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28707">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eDXWawoXdjSMfl5OBwcBNjAOVtOw3gpgB_20JgMZBeKow07LDrGV6KQ4D0FCbmFdn9z89U-uCBlBk8uTsPIHl4tFVwqhC10B23-AJ9siY_e3y15F1WFXZQaHVrHhqIS2bxmMhwLKD4-si7Rh7FZA37nLOWCtq4-tP1AsKah2UrPSS9DJBuMox9sMllNoWRg7wCeAK8zLYcdiQyLuE5vJa_jdozF_t8KKmx3zlBzcrOOPQG09VtlTTDGORL-6bV7cKynl_CVj6Yv6WP9CV_UIPPr-Pr71TPkgt6QH0D9-uvapzLuJXUFd742Y5Y5XzU9l02VcshD1M0SGGMbHocDFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍁
پاییزِ زیبا، پاییز خوش آب و هوا، پاییزِ دلپذیر و جذاب‌از رگ‌گردن‌به‌شما نزدیک تره. این گرمای لعنتی بره که برنگرده. با قطعی برق دهنمون سرویس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28707" target="_blank">📅 00:58 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28705">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH5UR9rKrqB_caJhAzlwos0g7VyEczF2o_Nnn0MY8wszvIzFGvvWEkrH2DR1dladJxCbRhmjQPnCZ2st_RtJKazE0XuZpc8E_JSji8gs-34RgVDbpVmiISxDHI97tSgzyuiPfHLM0h8-os44Vb1MXHXFzy5djIL_IDUGydmo6VHvtJN-dS34EodrngbwIJj1hl7DqDNkz-xrCxGmXF7gGUC8teE91pdJ5kNIzhgCKKz9pa5xRh17givs2GZDJTPr2B6fxxFKsOKyZygr3R3neOKmsNvSEKZH3OkCaM65XNABMZUIxspMb-SjdkG7BF3tlbM1B-Ym3YDjckFj9rp2Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنهایی‌دیداردوتیم‌پرسپولیس
🆚
ملوان از نگاه متریکا؛ ثبت‌امیدگل خارق العاه 4.02 و انتخاب علی علیپور بعنوان بهترین بازیکن این مسابقه یک طرفه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/28705" target="_blank">📅 00:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28704">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmsO2VgP-o8Xn0BjxHJxI9-36AwEu089Ee8igWqeWc3vmMPADqCtjzPHor7xsgjTGEC5bBEamij2A2F_xs1rs9dzXLjeCf-wt7PsGETD4zXJ1Zs8lnnVLb5EW22DjwrlGAhXN0Hp58wP4JvkuhZQpm77yZT_Dw8a--PKPW6Sp9iGd9zniWCOU-XcvoFFZqdqqkhb7JzaisSZIXnKotaho_8qSqQEEKRkr3XU_lId1SmbXyVvuAQccK-SDlpngZx3BqE38q4v5b0wDG-7kdRS3Syhpdo58txFiHCrlDYH70kPN-abkMqdVhoQxLzcYAIeWYch2f9ZLRqdf-noQAIxbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزنامه«Novi list»کرواسی‌گزارش‌داد که محمد محبی برای‌انجام‌کارهای‌نهایی‌لازم در راستای پیوستن به‌تیم فوتبال رییکا وارد شهر رییکای کرواسی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/28704" target="_blank">📅 00:24 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28703">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO3ObuKWD_2bONDj0ci8TgSuXyn5Gvhk9-aVeHXJWiYcTNoyGMRJ_FtQ_5VXKRDl133ShlxVCHKBGjrSgTvEyLlvBpxtKIjbmbS_XHQIslhP5Q-DKT70NcKbP1kcH37MtNTtQoL1oHN8cFB6aaMK7kpHfhdrq9gdBzgbLxKidUqy3_eJu6LknpDVmr2IrYdVzqpjK5-SkXXwKi_QWDtAWvVVFUj6TBcFOOf4MbIqmtw49ddw1JRNgy5PiI0GKa7JyqENrwgi7po2wW4FfpYMylrUntIwalZWFL7-6HkCbk3k_NDRpfnqSE97UIqIIZjNmfpNuoTqOUtCiKaacNIVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 79.7K · <a href="https://t.me/persiana_Soccer/28703" target="_blank">📅 00:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28702">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqMIZEfCje4c-dt7dK42Npsp3tyuubhyRKBNUX58ywYlgLouWmz3-emcNoteUms_Sxr8IMHgWkmIGdNGrXHW6lBA_VbfTLbInsiEbJrEsDVXNypbb7pjzpoiuDW5qRbIMtcOQWDc_3php3hq2QImaEOo5Kod-K2NL737v77Jzd69XMohrm7cqW9cPiTc_LV6UtT2pyxJukOuA0i8uIwn6i_HNJhAnmyYsys_6gHKu046DxB5IBt6Dz0Di1hlO7st42d95rHVFiLYBrcDSTrYRO7AyQLfblpUjhhHwnBK0B7igLGOZYRXBSav4rmV1qI3tRQRlkfd_eWkRxffJQdJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/persiana_Soccer/28702" target="_blank">📅 23:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28701">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9R6THR696tA68cVkjH45nEL3ZTxxO74hiHSulGfcpt58BmfHCUphfKuGP1yMQHrQPzlUWMdczhcgSjTGhov6lCbFrYMcUcUah9QLPdXoLuJENobqVRdVXeBm8WyEv9x60ezucaBRK-24v9t3L3bKNRIhN2vatraLd8NDL6TC3Ntm3ZSNnbr4sQaSwOxsR0VLDmxhv2WvFWLDxrrJqYzrj1EELHDZMLxixtBDDY8I85WQhe5m9QbmNjJOpV6iKhrragUA-xali0oZjW-Y5IXvHsOUFpTpALKMxl8jio0HEr1c2cJKtUkFYpBqb-ILWeSuR8J7Og6WXMT0mfdJKJf6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام جرارد رومرو؛ الخاندرو بالده مدافع چپ اسپانیایی بارسلونا تصمیم نهایی خود را برای جدایی از بارسا گرفته و بزودی از این تیم جدا میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 84.4K · <a href="https://t.me/persiana_Soccer/28701" target="_blank">📅 23:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28700">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8UixOI7XN5vY2fXzXbtDrr4pPWDgUm9w1mnvwVx4dsxuVKzAIqtxfwOXyJZDE1ePpU0RXy2y3YlQt54PCsevFXXJN-83mc2WR2_KbHrtWGQrPlZSKp4sR1sBmY4Zjojf6CcfUG8HRAKKviCfrHVorxjnBgp-NXUKZdxTANXfl_m5QD_sOR-JuJOWlcD5ZQmliwS6OY_TXiI5fPhUosyQmjy2RaSNiGCQuJSS3DozgFvZy6ytncIaXLfdgA_hVADRdXj_N2WDRVbqv-yVJVEOFz_mwLtH0mbWDnSUgV9Sc0qGhRwwYESydTUJGgDDtWw6swTYCY3lCuVTFdaGJNzzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/persiana_Soccer/28700" target="_blank">📅 23:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28698">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQFDb5H_8Q3ELu1Z85rBMMgZbt0sozm8QtkMANESp4go9ZPDwxrSngS0BHn5ZIr9FD36rcrMWVR7-IWrIfrB0jKNbjopCWiL4NDU3N_YNMPvQzOydg9LnU8C2UebrBx8Ofkxjt71pjC6xJo9aimzyLqJDB4tiVqFH0ZNNjutt_VT62nib0_5gej5Rf-hWi9eLvK5ip43yxV2x-FaC9xcSvty-b0ASg-ZykNH-R0Kr4h0-w1uBhCQjtvto6zh6BbZjDPOI08Grft7fg9EEstdu2I1jEhQCljLyfP3tOPb2bzutwB6xENatlE9GaxxFKM_syW2lshBN9N7jVsyDCSSlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری؛دیویداورنشتاین: کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/28698" target="_blank">📅 23:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28697">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=C5sm9xucwcOJHGzzB3u7PrRtu-lEEZmApLJZrw_SoOnI0fXanbcjO1igz0goXaH4V4i75GmCG_h0nq0Z9LPXfFwmqo1SuDEs1RduDVPBnv2Ra0vrY1SYAZtyCON5RSx8dju1vwckx9nrRl65107r5A88avm-SdJh15eOYp2zy0RJq2SPyLY25ZaZPLwY6fJjQcK3lt5UzPhJ__ZEBRu9lL7R9jQ0_NgK65LtcCooiJ3PdeIWedpSMnN0sbhWjHH6LujRqyCfPwUgMz2Pl7wL7XWR20Brg_y63uvQ8U242HNa-uCjiN7VShpaFzx7yhM4uQTPGAIwf-IKssBR8gZFSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f3cfd1b0.mp4?token=C5sm9xucwcOJHGzzB3u7PrRtu-lEEZmApLJZrw_SoOnI0fXanbcjO1igz0goXaH4V4i75GmCG_h0nq0Z9LPXfFwmqo1SuDEs1RduDVPBnv2Ra0vrY1SYAZtyCON5RSx8dju1vwckx9nrRl65107r5A88avm-SdJh15eOYp2zy0RJq2SPyLY25ZaZPLwY6fJjQcK3lt5UzPhJ__ZEBRu9lL7R9jQ0_NgK65LtcCooiJ3PdeIWedpSMnN0sbhWjHH6LujRqyCfPwUgMz2Pl7wL7XWR20Brg_y63uvQ8U242HNa-uCjiN7VShpaFzx7yhM4uQTPGAIwf-IKssBR8gZFSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28697" target="_blank">📅 23:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28696">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ff1-lxkguZjJly9v0-PtpCK05OB6vWUKUJMa8HDIMDBm5d3tTPpaGWS52fGs3qJC1tj7YGZPVcSJ26-zngBcKhKDlHnWJ2zKbAYjs8l-4FC4zk6LjTw6DTJsEOcN6M1mWw4gqWn57m2_xxj-GxlBv6zihi49Yv-O8Kx4WeY2jP0R71vI4hWAm9p6Z4d_DX3UE7dXkIjzx37OnYlxPOYLvjYDkVXVCgRlAlA-kfrpAtIQmznsoP33q7sF9ZJayvocKYdUowt3Ru6BubBxKay0PXuCsQosX8t4Uv5av2Wdw5GZmGzo4o7LOk3Ps4s3J1U6VAAHs_QnZkObk51T6gMaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇱
#فوری
؛دیویداورنشتاین:
کودی گاکپو ستاره هلندی لیورپول تصمیم نهایی خود را برای پیوستن به منچسترسیتی‌گرفته و این‌انتقال بزودی انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28696" target="_blank">📅 22:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28695">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DihI8mdtByZOg2GafqqFh3dnnsoE6CWCGsrgNb5Ej1YHOQYLN8bAFNMdybmCByh8CM0jGLXh7owZiT-Hj_sX6gcKmUSbiC5DbX7cExTKGeSZrvaReycVlFHuODQTXlsxjVUzxnBABLR-Ed_0aNLbwanSwjSoF0w-QvnZUX0btoLW1hs4yZsaU8ODTIxmxK6OgjGnSYvnbNyDlA-Tkdr2CKiU5-Yw6sMkoBVNmSyuRVw22x5ZTwbkvpl-7o-ByulEsr9LVZE_bMcwLQMJWOXyzR8_h1PhFe7huOvCw-9oBkhndLLyP_yZLVHELsTRZufU5eVnYQmndi3E-htBl_A-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های محبی قصدداره بعد از بردن حسین‌نژاد به‌پرتغال، محمدمحبی هم به پرتغال ببره و نیم فصل با رقم سنگینی به ایران برگردونه. فعلاسر انتقال حسین نژاد به ریو آوه 250 هزار دلار به‌جیب زده قطعا سر انتقال‌محبی‌هم 300 به جیب میزنه بعد نیم فصل‌ 1…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28695" target="_blank">📅 22:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28694">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=ecOlRep7oFnoLWAO9_Oofqc0pthdypLmc6LsHZX8---K2S_ukCzOEyES-jvbv5Sa2OJs80ESNeuIqdpfA4H27vxEoHxZn4fjSfT65dCCjs2XOeHZfp9ZSNQ3uEsIJM1T24B3am-OQvtkyvzRMegarzQkGzJLFpWIOpsGv0FA-of6YSiuRfCODlB4tNlnILzVGviDTzOtfC9f8RTw4JvwG55fbulbQGnvTJEsIKr97heyNP7OxXbLlnwn2M5n_LFNJd67cenMURO5FqxtbN_gnaS1hsj9rKc58YBcZW0vdBIrjqn2MW7H-k18zd_Tlf7-Hlkc4wgPZ6d3S5Qefy2J_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b98c0d9b2.mp4?token=ecOlRep7oFnoLWAO9_Oofqc0pthdypLmc6LsHZX8---K2S_ukCzOEyES-jvbv5Sa2OJs80ESNeuIqdpfA4H27vxEoHxZn4fjSfT65dCCjs2XOeHZfp9ZSNQ3uEsIJM1T24B3am-OQvtkyvzRMegarzQkGzJLFpWIOpsGv0FA-of6YSiuRfCODlB4tNlnILzVGviDTzOtfC9f8RTw4JvwG55fbulbQGnvTJEsIKr97heyNP7OxXbLlnwn2M5n_LFNJd67cenMURO5FqxtbN_gnaS1hsj9rKc58YBcZW0vdBIrjqn2MW7H-k18zd_Tlf7-Hlkc4wgPZ6d3S5Qefy2J_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس‌جالب‌ازسریال قدیمی فصل دوم ساختن ایران و رفاقت باحال امین حیایی و محسن کیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28694" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28693">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e895367e.mp4?token=LdzN_FYax1jOJ4dzYUKRrqCp-CACZolsJXKfaNXnnIYygHPpnNuy_rhEA_GxnGZ5XTl7YeJCoj4svLgcYNXWIHwaxU95ZcHKjAn2eVqGoUe7u5Uj4xwjiqFqDI7pNm0_M9AwpzVA896bH4J-FTIFhj7oOtzvfRXGlzyBicEP9CAsYjgnsQu1xtkiG7GCWqBlUfWTFvq6UcJxm0lQWlNaEP32l_FEaG0unp48SQ1sfDQom80vj2sNiQEsb4mYm0vT_bWt0umKG0dqcJmcK6td0D1Uc_V5-MciCdRC-sp_pjIXWMGYKfbTrhUgFnNrZG2SLON6M9_RSiW1A_At6TzEZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e895367e.mp4?token=LdzN_FYax1jOJ4dzYUKRrqCp-CACZolsJXKfaNXnnIYygHPpnNuy_rhEA_GxnGZ5XTl7YeJCoj4svLgcYNXWIHwaxU95ZcHKjAn2eVqGoUe7u5Uj4xwjiqFqDI7pNm0_M9AwpzVA896bH4J-FTIFhj7oOtzvfRXGlzyBicEP9CAsYjgnsQu1xtkiG7GCWqBlUfWTFvq6UcJxm0lQWlNaEP32l_FEaG0unp48SQ1sfDQom80vj2sNiQEsb4mYm0vT_bWt0umKG0dqcJmcK6td0D1Uc_V5-MciCdRC-sp_pjIXWMGYKfbTrhUgFnNrZG2SLON6M9_RSiW1A_At6TzEZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تاریخ سازی دختران ایران برای اولین با قرار گرفتن در بین چهار تیم برتر آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/28693" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28692">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jleoTIlP4pwe_2eiRJQ09Io2NsIWvNJLqXJYfveHCPUjXTP-cq1UIwhC9cNFDf5cNAVYrnPBcNZSffJikg7KdVge4V47NqeLnphq7RuOPrNpKxo8nSovMQFOFIdL8zhJp9bhf2YwHO8wzgTvF95AdERT61y1tz9-jchbRqmSuvTEXcOelPrkOf45pxaep2YvzdFvHrJVFnBvetPGhLBvPHrXZLWtTConiSW7bs75y0xmjWK-KUTmQukYUan6T2zKfW0CCH22enO0xqMnv2iNxu37uzF1z-N4fjg4tUnkjf5T4Qy2CvU17EDdwJb20tEZ27_cJcaPxUaQF3PBw9kSVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌دونستی‌امکان پرداخت قسطی می‌تونه تصمیم خرید رو برای مشتری راحت‌تر کنه؟
با درگاه‌امن اسنپ‌پی،
حتی بدون داشتن سایت
هم می‌تونی پرداخت ۴ قسطه رو به فروشگاهت اضافه کنی. این‌جوری علاوه بر اعتمادسازی، خرید رو برای مشتری‌هات ساده‌تر می‌کنی و فروش و درآمدت بالاتر میره. برای اطلاعات بیشتر و شروع همکاری با اسنپ‌پی، روی لینک زیر بزن
👇🏻
https://l.snpy.ir/hw5zl
https://l.snpy.ir/hw5zl
https://l.snpy.ir/hw5zl</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28692" target="_blank">📅 22:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28691">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=o6n3EX_3einOuGaASVBbJZdxdvYw5LF36Ab3nqj65EY5JL61R-p1xbL1_eJAx61y99y3eUqnDzcmvQLZTY7xx1VHUZFD4agrSPQX6WR80RsyzY90vpFf82cZoPejKppaPTNQANrk47worAsClBdadCtXLJVsax9uxot499RcVMN6SS_1SrVP9ywV4EYHpnZhZ-Yv3PB83un9l69NiFeeiEbxK5Ilha6Ku7OwWLEz9QUIvV0cw3MatKeSpOxsToHgR-E2KsUSoQ2P7nv3tYds5sRIdUBhvT75cB8cpXB9j_7PJC_Ppn-heixsp92zXL6Nc_o4nJheXZN5dysF7zgGyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d295e52c.mp4?token=o6n3EX_3einOuGaASVBbJZdxdvYw5LF36Ab3nqj65EY5JL61R-p1xbL1_eJAx61y99y3eUqnDzcmvQLZTY7xx1VHUZFD4agrSPQX6WR80RsyzY90vpFf82cZoPejKppaPTNQANrk47worAsClBdadCtXLJVsax9uxot499RcVMN6SS_1SrVP9ywV4EYHpnZhZ-Yv3PB83un9l69NiFeeiEbxK5Ilha6Ku7OwWLEz9QUIvV0cw3MatKeSpOxsToHgR-E2KsUSoQ2P7nv3tYds5sRIdUBhvT75cB8cpXB9j_7PJC_Ppn-heixsp92zXL6Nc_o4nJheXZN5dysF7zgGyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
👤
مازیار زارع سرمربی‌جوان‌تیم‌ملوان با تریلی از روی برنامه فوتبال برتر ممد میثاقی رد شد و گفت تا دوربین خودتون رو از سالن بیرون نبرید، مصاحبه نمی‌کنم. دوست ندارم تصویر من رو پخش کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28691" target="_blank">📅 22:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28690">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B15dBO1vkoGCchD5tp7LEKzxYphjXuKCN9FjmJulBc82mU0rRKcXGtR4vtn4UAfaCTMPWCBjzVpe5qZ-6PmnrHp_1oDseR5jRjaB8-CVjhG7yhhDxH_oXPQ7TpBOAa1SQueyxrJFbBpUtNUCAmo8wmFieagvjhdH4kINDkXwxh6RSaKYMoBVKopo6bY-Y7Tu3J7orUbsNDFWTpiQDfMRBFXpsli0GIpPY_ulvK6QWs6st09NwltZjkMKoNNgHZnUT2WXVxw0PO4IrS02V0UfCUe0d5QHLRv8bxjHwLroQ_KgQm9VStT4eOuR6GEnHCKP6NkxDNK4rHW0OAU6dfey0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28690" target="_blank">📅 21:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28689">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geWALu3hg5wvPblSftGUhYdDVQE8tS6luR8fDcfglPCJuFr8QGcVQ5xjPMtdWaOT-X0Z1uhRXppolMen3ifGWMr17HkJUSFmkWyv4-8TgcK3jnGP0wxVIGCjGJmVVEBFs3TZoL3KnSrbh8X69CmSS0GKXKYfczgYz_xOkCiv3wPlB2R5B9ppGzDNeGDJkdTcACJIR7Y6ksc54f4MqBQkS7FDJlB9WHMEEe5G32GCtXKbSvjKmZAWmVVmJB3mUOV4_qfhuCGpkEpqQ6lXO9n34HX8rLOaW_jaJIu0e7bvPMWrTzi0Z5VCqtn6lCNc3Q6hiHY6Xnb3bBOMaIUlz3T0Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌ونتایج‌کامل‌‌بازی‌های هفته چهارم لیگ برتر؛ تراکتور با جواد نکونام همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28689" target="_blank">📅 21:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28687">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_rIQW_cK0I9EWv-spWCY5tMgexxo7wSl1tVbO0w1y_45kOfJ2H94alRMhRzgyPQMkreWJTc3QmuSKoB27LeEB9KL2m_C3GYdUeuKViJw_RjJCcN1HQW-TTVezh0hQlOa5cqfPJ72t7R1VYJAzx0ophVUpSVOa3_mD4T7U-ZIQUgP8M8WpzVNWVoLMwkveCQyXWZoaR8WRu5VmZhJsWvH3I4F0tuHTounkEKBItArR2Wh8zjfg0G4MyZg7afeY1fCkzsT9cWRFE5rMAcPKO55kIY95p3gYSTyyStpivqP2ZE4KOXJjHsPraDJQOwNueudhB8ljIvh2D6mXEdECHotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DGZxfLPWkkOaa56H_0ZiQ2kmnZly85vxlX2hbeujkGH_mwCPRX2nWn-mLSp3TaJtkH8883EqZNyMCKXDGyDpMTivCffdX_LlTc_ep4JhrIYTaSocIZIoWKPXhYXFvFJSFo1hiMZK3M-afcFwwzOZcY5ft2ejXwLjc7FURLUauB63mgDGaOO19MIOFHMsG-WiQS3u2ZkQDra9S-sTcdWD_KolKYa_X4pQ9ebkBM_E96MHxtSXgHqyEWjaJqsuW-iQzeC-PjWc5S9aetxQqg-Qo8-LWSIgTqDpCD-zmgLNUIx2ZqZ673HEKB0sh4BMW43eZtgWJM5O9Cr0AEBAT1Me7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28687" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28686">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ia4Oi-WVWhqDYlcOA_GMN6F6quc9DXZPb49SeRW9sx89ecM00GLHsdVLn2HS1aaXnZSX1xVNV7D-tkkx013128XAeZpP9VW6rJpI_RusRiMK1c0aR_w5FHx7ng_HhMuo4g2IAToCGTwcCqCsJBvFOOEBLZCPfJEqUiI0BZy0x_yCwzhx8b28bSiJE6r6_DxgTF-Wg5N37t0CQiMlODeju9-zYAuOm0GqxHYaOpkx0DzJ-zkNj7CP3nB1jPZ8lT6RF96HyYz9Vy8Dzlx9tV5OqK4LuWfxkKJ0_GQDeglnl2ih-RdMEZcMAMpLwHN03seeMczDCXHNQ6AfA7bTpouHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شاگردان مهدی تارتار با یک پیروزی پرگل و قاطع به استقبال دربی رفتند؛ تارتار بالاخره به ستاره ازبکستانی سرخ ها بازی داد.
🔴
پرسپولیس
3️⃣
-
0️⃣
ملوان انزلی
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28686" target="_blank">📅 21:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28685">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bwbFP2PomLKD5c5vhCypDKT84KADlroCTWuO3UNHbtInk0G01-Zir2EMM2B7750awRBx03sjL8XBoFKhIz5VLLMZJHYLptW6h7ImHuvr6R3dYFgxuoJBJlOBTTPUK1pYmGd8bmJO-sXnif93Ne1iQnqUIo-QkfRoK7XMI3telFJjSMJnBcI5n00UZgqZCsXoDZUburGqf17I7l_oK2on9PsLGg8efwSuE15VahNglPG094R539B_fU6cb1jm1B4VuOb7kos6DXIprcrYYHEEF05JMFjIudU5DolL3KYPfDLn2_M7BmPeNCI94Ev1yXfX-wk6O0XVLcPIPpcqfHbfqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آتش‌بازی‌سرخ‌ها روسوتی‌های عجیب انزالی‌چی‌ها؛ گل سوم پرسپولیس به ملوان توسط علی علیپور '56
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/28685" target="_blank">📅 21:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28684">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=gv8qTpkTHofP_g9hWuyfPRBh3wawUJoPDKAK0aIrHXxvlM-fKGuto2ik2_3GnH1Dtho53gdrYR5XsSPzzfDAf4L-hTf9lrI3me3oncT-rgq8NLrOCdx60RtcgTXil6jl3p-_ntzybXfZPPMCZKxobmGz2BgYu4ixnTcp1DpH8bYztCEkk2TP1PTaI4WjqPPwPs15Uwbpm6FsdxthbdRDUrxCSuebcNJ0P_4KrL91fhMj8d9n4I-4-Jp8m3ucJRTaISETDpNCk8VEIyyAo9YShbe-zN1VUDYurtrOud_mfXUTgakGGTsg-XKtxdpPmD8D4hcdbtkpvV4ce5D5IE3aKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0430b06fb1.mp4?token=gv8qTpkTHofP_g9hWuyfPRBh3wawUJoPDKAK0aIrHXxvlM-fKGuto2ik2_3GnH1Dtho53gdrYR5XsSPzzfDAf4L-hTf9lrI3me3oncT-rgq8NLrOCdx60RtcgTXil6jl3p-_ntzybXfZPPMCZKxobmGz2BgYu4ixnTcp1DpH8bYztCEkk2TP1PTaI4WjqPPwPs15Uwbpm6FsdxthbdRDUrxCSuebcNJ0P_4KrL91fhMj8d9n4I-4-Jp8m3ucJRTaISETDpNCk8VEIyyAo9YShbe-zN1VUDYurtrOud_mfXUTgakGGTsg-XKtxdpPmD8D4hcdbtkpvV4ce5D5IE3aKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28684" target="_blank">📅 21:02 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28683">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=Usz1QFOZWS3iC1bJ0Xn2F0bkv0M7simOFrLINc9RkCEqN68qQtq1QkRndA8CNoCrykUMVSeMRPAdiW9d-FBgPv91xnXhh56ZyxY39MJIhFEf5AJT6RvAySxd-pXxuh5NfjdePc33s6Y_6UqmJjNRy3MVEKKqz3dRocCxm14NTQ6Jnz2HSCvRlF32W8rhoMKOB_6Sq2CH37aaDHCB_MztJVfOXU6n8BqvBweB0njwc5eynS45GAo58INKIOMbs5hPTlNf5aw9_H-Jmd2tFTHC50-phLi7xo9yqWBKJQL4XchelL5cgFORW9ILXMGqkcUZFH6VHa6bm0Hv3tyo51DqKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ebe211786.mp4?token=Usz1QFOZWS3iC1bJ0Xn2F0bkv0M7simOFrLINc9RkCEqN68qQtq1QkRndA8CNoCrykUMVSeMRPAdiW9d-FBgPv91xnXhh56ZyxY39MJIhFEf5AJT6RvAySxd-pXxuh5NfjdePc33s6Y_6UqmJjNRy3MVEKKqz3dRocCxm14NTQ6Jnz2HSCvRlF32W8rhoMKOB_6Sq2CH37aaDHCB_MztJVfOXU6n8BqvBweB0njwc5eynS45GAo58INKIOMbs5hPTlNf5aw9_H-Jmd2tFTHC50-phLi7xo9yqWBKJQL4XchelL5cgFORW9ILXMGqkcUZFH6VHa6bm0Hv3tyo51DqKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28683" target="_blank">📅 20:38 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28682">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=tk8rWtXX6QigK4TIQu2E7cgLxSVRb8v50MmHNUApNezgfoCnC57KGpoEFZfIcQ7Y0Two26AuiLnnnfkewtcEv6iIYj14Zph1fiwwWENEcLMuC_NmTfPcLjKuK8lOWWh0UipbCiNRcFj1rPtj6Ln01zLe5f-_Vm9pTj6u1C07zyp7BzPnNCbhjQsG5Ae_5CWBdBW76hZBQRMq4zLTGB65ejCN4fzsFuIxn6YbWCtMBZNdBVfEwlAzPhhQwwzX2UMhEYBQxlDucgmJ-mcTFSKaT2IkQD81mF_r-yyJg3lyM6UZ8KxckouUIz-vGJlhQcsVTVB7nBG9du6kBwAs9v2oEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b26514a40.mp4?token=tk8rWtXX6QigK4TIQu2E7cgLxSVRb8v50MmHNUApNezgfoCnC57KGpoEFZfIcQ7Y0Two26AuiLnnnfkewtcEv6iIYj14Zph1fiwwWENEcLMuC_NmTfPcLjKuK8lOWWh0UipbCiNRcFj1rPtj6Ln01zLe5f-_Vm9pTj6u1C07zyp7BzPnNCbhjQsG5Ae_5CWBdBW76hZBQRMq4zLTGB65ejCN4fzsFuIxn6YbWCtMBZNdBVfEwlAzPhhQwwzX2UMhEYBQxlDucgmJ-mcTFSKaT2IkQD81mF_r-yyJg3lyM6UZ8KxckouUIz-vGJlhQcsVTVB7nBG9du6kBwAs9v2oEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریس رونالدو کاپیتان النصر پس از برد دیشب النصر، پسر سامو کاستا را هم در شادی اش شریک کرد؛ قاب زیبایی که حسابی‌مورد توجه‌قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28682" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28681">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onkKalRmSsF6ehwWpIMwHhwkS6ogtBdgyXqnu9IaWAU86dWGbeVY38VmfQtF1oqV-Cd3Vnhs4AQ-I7t5MGvuHyJOPGOJ0rWkofaBqtEd6R_v7C3qT5s3oDnb8Lihncd1nZZveBX8-NTXNyau5xh0s0NSM5gJSKfsCVpT6xWmgDK3O8sx_mx5tzHWa9LzBagARNK5CZ_WZ1OeMJfa-yaJqT2ta5ED5hWlkl9b6I1Z9CmMV1krPXUtDPXBUSNgMUIgpY8bGEHL-uzyHoXgjSAbBQd_UgAbQjh8Sqvl-ty_LltT_Ip5irBZj7RfAgy__KEiKmuDGb7Xg1J9C9pH39Rj4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/28681" target="_blank">📅 20:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28679">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2OPY4vvrvFHtvEc_kFec1iyb1RMt94okoNSy7Ahy8LUF8Apou4mcJgy_hFmuSsPkuUzmegoA29lgspD7s4qPG54ZN7ClcNY3r3UicpIRKDXf0Hz9au6UItduzUEpcWJiLyOAdPeC9B1Tn6M3tr53KThF6YsASjSvNZAhhb2gTt1sq93KW2I01ll05pQwXwnx90B2u2f66EMYBdYcpfSrtb_dlbLla1FRcDI2K1860Lt_OkfRZG1k4dQVwa050PTjUBszVz52xxtNqH4A8AQeEYSL5NU1EEGvVeBedVpSh0Ka5S3pT9aBK6XR3bpk3KyySpg_CxJJSDhTSvQ4Q2E6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گل اول و دوم پرسپولیس به ملوان با گل بخودی مدافع حریف و تیوی بیفوما در نیمه اول مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28679" target="_blank">📅 20:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28678">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/28678" target="_blank">📅 20:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28677">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSnrNah3-ZPS7R8BswtG_CPHPt7mx15TT_lWSiYTbP7WpyWU1ncDm2ilbIqUV1OG_lXI2YCag64emSACaep2ypyCy3WZwLF_uRrhqrXhjg1gmwlj3bn2vnh3coz9adQRLZtTWPLTwOkovPe7NKuSISEAbKeZ_731UEHaM764kdxDmg0ZsnMOB-CSQNDCeDf9vQjyNNGOzjotQSbfntwdqGFxWkFdXCRM47aT3Gp5PFtSz7-cjGOnxE5v8HwssFp0-4LR-Mz8cUuQqecn5RTQz90QfJQZPVxcKLEPoPeF7SjwbPkfirZhsa1I9yIRANfmfHhBpdDKrIAXFTAzwFJ7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر
؛ شماتیک ترکیب پرسپولیس برای دیدار مقابل ملوان؛ ساعت 19:15 از شبکه سه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28677" target="_blank">📅 18:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28676">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=HWfZu5yqSDsKpJRNDf9JreZAi2PPPGJDrZ2akA3pOW_NR1yuy1PUN4iIGSMWkEQdgYNAbpEUkjf6AEDzDFHEO3sPEkzB_EVNMu1MvI1AL3XHirJz3oGNKUgQHSr34Xafzh0JlW0zJLsNh2FszEn-bqeGtzGPdVqzNKCVbYCw2Bfinsl_L3qABHfGdESD1--VhPZ9n2H1JZYZGrCxqZaI51gvGop2MkCndcr_AvIxaTu8yu5PzgVEmCv7VYzgVTqxR78tHxdIx_BRVO8ir87h1PebSK1atVHsqipBJLtUwUYL5q6TvetBfzV0SThl-r43rNTQqFF61HvOPHxtyNa7vrJCYErVF4GkF5yluC0wB863Qlf2-QIMcIW3znc6TB65MdBIqqEzz2sY93rsP3ULsy0w_OWqsQkJzbTcG3fFOwcBRmkrJMLUAVLLsq9BIMJ_1HKAwGoCigQjIXEO832rQkbb6P8jj1pezBdHqEp8-lMfHI_rfq4CDvvngkl-C5IdjbFtrKxVQ79tbfZ71M4EDjpACsevvL_CdNYswbMwNKgQVoOCo_seJ4vxxFsTfwGlLxDeObxm41rEiJAdkIed-ryo_WuVKNXhhwy8foaMVTq94Xpjr5wGL-TO8B67P2SJkooKF3zsm21wR-cW94umzj-pHBlFQDtyd_zF-xGWUxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9cce8d93c.mp4?token=HWfZu5yqSDsKpJRNDf9JreZAi2PPPGJDrZ2akA3pOW_NR1yuy1PUN4iIGSMWkEQdgYNAbpEUkjf6AEDzDFHEO3sPEkzB_EVNMu1MvI1AL3XHirJz3oGNKUgQHSr34Xafzh0JlW0zJLsNh2FszEn-bqeGtzGPdVqzNKCVbYCw2Bfinsl_L3qABHfGdESD1--VhPZ9n2H1JZYZGrCxqZaI51gvGop2MkCndcr_AvIxaTu8yu5PzgVEmCv7VYzgVTqxR78tHxdIx_BRVO8ir87h1PebSK1atVHsqipBJLtUwUYL5q6TvetBfzV0SThl-r43rNTQqFF61HvOPHxtyNa7vrJCYErVF4GkF5yluC0wB863Qlf2-QIMcIW3znc6TB65MdBIqqEzz2sY93rsP3ULsy0w_OWqsQkJzbTcG3fFOwcBRmkrJMLUAVLLsq9BIMJ_1HKAwGoCigQjIXEO832rQkbb6P8jj1pezBdHqEp8-lMfHI_rfq4CDvvngkl-C5IdjbFtrKxVQ79tbfZ71M4EDjpACsevvL_CdNYswbMwNKgQVoOCo_seJ4vxxFsTfwGlLxDeObxm41rEiJAdkIed-ryo_WuVKNXhhwy8foaMVTq94Xpjr5wGL-TO8B67P2SJkooKF3zsm21wR-cW94umzj-pHBlFQDtyd_zF-xGWUxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجای‌مانده‌از دیدار روز گذشته فولاد و استقلال؛ دوئل علیرضاکوشکی و رامین رضاییان درکنار زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28676" target="_blank">📅 18:08 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28675">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWzpRjPaOjliuVuRA894PIMOgO2K1DEpgH6csMZF4ZFcT-BM3OS4RQAcOdLh9fYEwkAzU4_AXaDMYor-zXPbrNqbLH1BKpG--KvfplxKx8Fo8m9XZ1QZi3R-Pfrnz8-DdZFqHQ8TLuLYhJNevQsgZs1sCxD8z2qoRLMM_RnTwfFRGJ61POkrClxwt2ai1HXBUztztkow3zZCGINV57bZd8nfz7b4rgg9COfYG3rh_yCZYZy-Y__if8jY2e5W0uvXOwB93TQX3Ye6ze7cV_O6aDj9B5IJZJH9QJDjwPZOkPxM4_GlFYSCCb52JuTD0p4iMQS5n-9Od6tEYFh_cE7gWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
دوخبرنگارمعروف و محبوب شبکه DAZN ایتالیا برای پوشش رقابت‌های فصل جدید سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28675" target="_blank">📅 17:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28674">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=basTmapy3eYES0xT9LEoq5-qcCv7_SRL9tkngBMxijtjcOGHgS6bfqmcwKmlunW4gNIH5Tqa4Ao7fgmmdte7yyTygIgUIXnLCDVlVSuGR82VxXNGLc6y77uT6vrc6vYmIGvnODyIHqdO8n_khpcsFxtvOP8JPA8HVEDphMyIJMxjN_xyV0HlsWQVKa1R7sCzC1v8wnDfRsb8QsNp61nrHxfDCUH1PHMt5TfWkB-52F6py83qAxIjsBBj8Ocax527Hqods97sZ-uIHrLd9NlQGmysbnbERQ4Of8T2LlnsOfUm6OAK2CyP_Y6g32zdJfMtbqojbZeHqGf21StfgH1rgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b03755e8.mp4?token=basTmapy3eYES0xT9LEoq5-qcCv7_SRL9tkngBMxijtjcOGHgS6bfqmcwKmlunW4gNIH5Tqa4Ao7fgmmdte7yyTygIgUIXnLCDVlVSuGR82VxXNGLc6y77uT6vrc6vYmIGvnODyIHqdO8n_khpcsFxtvOP8JPA8HVEDphMyIJMxjN_xyV0HlsWQVKa1R7sCzC1v8wnDfRsb8QsNp61nrHxfDCUH1PHMt5TfWkB-52F6py83qAxIjsBBj8Ocax527Hqods97sZ-uIHrLd9NlQGmysbnbERQ4Of8T2LlnsOfUm6OAK2CyP_Y6g32zdJfMtbqojbZeHqGf21StfgH1rgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
صحبت‌‌های‌خوزه‌مورینیو سرمربی جدید تیم رئال مادرید درخصوص جایزه ارزشمند توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28674" target="_blank">📅 17:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28673">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WsUpYMU8U0bNmqycoolTcynPwmwcsfs1wRTSA3GNXOb1NuziEd0TDP0QOvg4arJwmv6sBnu4lKZXdzAezIeezrSrkOOJw0C_FTr8JoPStHOku9TKJgIzdahiLww-zLH5SQFb1dvwxSI4rT_tzfS5yAP_JMC_nh8Ccv4U-AchVk-P9douT-5rGSSQSj1XhA1nUYIyEugOQstPe32q3QP0aEqZLvcTZYwYUaeIhyoH7p-6hzuOskK17fnshIZ1MWME_cDxfXs9FcoTyaSIxQ9qQ1TsX721MByt7C9saTznGW79coTOg6MQfGxnt1okII6YO2815WSKmVPb9ESxQl8oIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به احتمال فراوان تیم پرسپولیس در بازی مهم امشب مقابل  ملوان با این ترکیب به میدان خواهد رفت،ستاره ازبک دور از ترکیب فیکس سرخ ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28673" target="_blank">📅 16:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28672">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=gUXzxjaLBYeBbHl44wrGlSiMP1eCMlVIsIBx6yKEJ_R91nbzqZvHMymzfcfjvN1gD4eiO_99zMLjNLpmTZHGWxG57MUBZJCWyPgZlmpW-DTBLHPRoqRpT4ScYRkaM6qGWS1EkMea9WeUTyDn3x6yIhulrLM6pBfBZlfZ1zB1kLW_xjuv-FqsRb8gq5uYTXibnQcHorAdDV1f4VzKwJP0d4ZmSX7002U_4-jDWhH2OhPvkWfF6NnERCcBNWqJp9nBkU8zCulYWD39zaFLRZOTZ2HmnX7uO_3JXN6D5FdUhxOwK0zWaNS1VwguMzsGJlVi4aQ-z2nhg3PGq8IXKlb7ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873c1f0eb1.mp4?token=gUXzxjaLBYeBbHl44wrGlSiMP1eCMlVIsIBx6yKEJ_R91nbzqZvHMymzfcfjvN1gD4eiO_99zMLjNLpmTZHGWxG57MUBZJCWyPgZlmpW-DTBLHPRoqRpT4ScYRkaM6qGWS1EkMea9WeUTyDn3x6yIhulrLM6pBfBZlfZ1zB1kLW_xjuv-FqsRb8gq5uYTXibnQcHorAdDV1f4VzKwJP0d4ZmSX7002U_4-jDWhH2OhPvkWfF6NnERCcBNWqJp9nBkU8zCulYWD39zaFLRZOTZ2HmnX7uO_3JXN6D5FdUhxOwK0zWaNS1VwguMzsGJlVi4aQ-z2nhg3PGq8IXKlb7ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇵🇹
باشگاه گالاتاسرای با پیشنهادی 50 میلیون یورویی درآستانه به‌خدمت‌گرفتن رافائل لیائو ستاره پرتغالی‌آث‌میلانه. لیائو ازمنچستریونایتد و الهلال نیز آفر مالی بالایی دریافت کرده بود اما به طرز عجیبی تصمیم گرفت راهی سوپرلیگ ترکیه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28672" target="_blank">📅 16:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28671">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvNz01W4f9kEEkm_S8oeF9WJ6hSojYf-4E6rSbd5U05mmxNGvTwnFezzAg36A8NXbiy_p5oFDfRMauTK9_CLsl4WSJU8OjvvuIgPHE21EIp4psf6F_K3ArnkTq7UzPA3CBI_0vSySwbixY09lhrvJr7j6fMZPkCJPbyNpcrTvnhVzLyWQA7mq3OGy4VnZyP-hqUmLF9P2SSn4D2kD5mG9pB8StTstBXN4RSoMvJVdKvbJiz2rR-dUo2F9ucC_pbIOm0PGeoaRkOGMWRcSapa29SmCQI6t1Vy8PH2OHICv53Qiy5eQO2XpMcqDkoUMNQLB_j-QryNAjlESJZij3dd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28671" target="_blank">📅 15:20 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28670">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e418389c.mp4?token=oBVEsgiIiblZyNR_GDY612VfpXxqB-dxeQCRBj9RIemYq8EJ5qUVS6JJBAzItHkVWNUk5qhPNrhjTBSzgxks5OIQI6whywBsVprMoc3FvRq7evPV0g1Jg_n1ouwdKONDn2J8bkqOjEoVaVz6Zmnu-vP_I3sE9BDAxofVc5NpNXm7yDCIxS3OmWypZ_CUvCsaRliI2smSDUsBcFEvSiobjp9At1rM4j4Em2-al0HdVoEUsF50wqTDpXJ6-zYx7MK5266POebfxF9oD9tr_T3u-HKQS1FLO_8uR3g0Drf6n9TxduTH7xsCSNJ8KIOc3vGLhK2gmoWJkWfTcAWcktO5JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e418389c.mp4?token=oBVEsgiIiblZyNR_GDY612VfpXxqB-dxeQCRBj9RIemYq8EJ5qUVS6JJBAzItHkVWNUk5qhPNrhjTBSzgxks5OIQI6whywBsVprMoc3FvRq7evPV0g1Jg_n1ouwdKONDn2J8bkqOjEoVaVz6Zmnu-vP_I3sE9BDAxofVc5NpNXm7yDCIxS3OmWypZ_CUvCsaRliI2smSDUsBcFEvSiobjp9At1rM4j4Em2-al0HdVoEUsF50wqTDpXJ6-zYx7MK5266POebfxF9oD9tr_T3u-HKQS1FLO_8uR3g0Drf6n9TxduTH7xsCSNJ8KIOc3vGLhK2gmoWJkWfTcAWcktO5JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالدو بعداینکه‌دیشب‌گل978دوران حرفه ایش رو زد یادش رفت خوشحالی گل معروفش رو انجام بده که مانه میاد یادش میندازه اونم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28670" target="_blank">📅 14:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28668">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dai1gRzB4jhOaIOV0RR_DqDnr4kDRntNlnk0Pwkhhn7lANcSmLdMnN2xZTa_0I26hE9hlXACny6UM36SlWJJBCTw5VWXqvDHKjq_gdGr0m9os1q6jVCHHMZTGny1jhIKFiGc7kcPlqcm5642lq4cc6X5kEu8Sg9xVI11qjR9Mu-YiMflR9NMmAJAaDNiiygORRQhr964KwI0OtEVTbMcC95nYNiJUutTj2YJZWuDxOIcLtIiewErHTtAbC4z-TpboBgdg3XDSkkJpXakyKEVe4q5Jd0Gy1TvXKT4_xTGKCLDf59L7JyprtsOE1mtJNfe8s3dOwfN96xzgIL8-xWl8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q0TMByrTtLEKTne81UBUOZ9L7qRcz-B1jeu5YRcgPqOKa8MdYJ1lDWIb8I123RNqR1poUcnSrMlLe2TL8ZA8KqTvfPmC3mL44Dpb-FPDgCwzj8ASjAbbAMP5KUg1zdm-aQeriiIrA6AMP7XbKr0ersFhQpTNB-PTMIL_3q1Leyhm5cNHrjLzm7Ik933vXAEpUyQpeHKRGnHc00BtA7-LA-WsalNxEGDC7wEzWEwwzD6R76YL6c3kRzQvl5TKFxirIst7iiWyyRALguEPVCjYw3LIduxv48oBVAOqO6_8lAUgpBr8dchoUTyhkEtiBj17YZyrWnMQt0ifskzek4h1bQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار نهایی دیدار دیشب دو تیم فولاد و استقلال درهفته چهارم لیگ برتر؛ بازی در حالی بدون گل به پایان رسید که آبی ها امید گل 1.4 ثبت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28668" target="_blank">📅 14:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28667">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UeIyiLt9RgbAEiwZLnL4ziD6REpt3FVHn7d-KJCuZ7zZKUDCt7YP6igMbbNdAdMjIsi1QRRN1HChxClbWqD_3SX0yC-aE1tfFEEJK9cifxyFJl2Nrcct0hZimB6e8Q-brGUw25ckl3DAaIHK29k5uBb3zMqJMcNB0eM2ReK8XJRkWtMl-sazl73B3XxL32lJvMGCaJmYeQW6EdDAessw3KSUXMs-chrsgyG6blsKxlTrNh4cjsHZtKalJ7VTePOs1pN8bFqpGfKmAVUKwrK1xzzoJNAif6ZsYdnQ_YAoo1bx4XioPf4qvU-ca0siGwtQNAhq6eSU6HpWW1A9gDd52A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28667" target="_blank">📅 13:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28666">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=Rs2S2w8-cuN0Qao642a_xHuh095u_QtM67pb6KhXCZl0PPG-hTq_oUbmUCMvibIWOSAOP3f2ZrlEe2H4JrM_kKSNgzorNAoAKcFsZCd_IvTsdyP_m0FkR5geW4jo_cXv8wD93uOXq0AP1Tr6G7tFHkSu36Ad-IgwoPfFu6eyAyRtKkSL_V85WAFq3s8aALTjUu_VlVr3y_YRWdyjjaU3_VPPxx_sIpN3uTkrzDQRnzfa0o_JPSpif1Dsnloyv53RXnNDve112lDyu-O0yhqcRbd1GQK3i-Zx8rTftYAWhkZ0JIcSkFiYdEv4DUVTTK35ofnODdY_ZTD9yxj9WQPcWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d08aa642e2.mp4?token=Rs2S2w8-cuN0Qao642a_xHuh095u_QtM67pb6KhXCZl0PPG-hTq_oUbmUCMvibIWOSAOP3f2ZrlEe2H4JrM_kKSNgzorNAoAKcFsZCd_IvTsdyP_m0FkR5geW4jo_cXv8wD93uOXq0AP1Tr6G7tFHkSu36Ad-IgwoPfFu6eyAyRtKkSL_V85WAFq3s8aALTjUu_VlVr3y_YRWdyjjaU3_VPPxx_sIpN3uTkrzDQRnzfa0o_JPSpif1Dsnloyv53RXnNDve112lDyu-O0yhqcRbd1GQK3i-Zx8rTftYAWhkZ0JIcSkFiYdEv4DUVTTK35ofnODdY_ZTD9yxj9WQPcWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28666" target="_blank">📅 13:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28665">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQz8YPh4C62Jj3-WC1qRtE0nw5sZindpDoSx_mQvnSL8TnZjhcoU-CIKly6v93rRcVJqW583hT9du4Dsk-vyT3wVKQDZa0I9UfAx5Kco5r1ggIGybI9uYD9PBi-LgCzupojm4TgsFjjTwh-UB-eqicamrUjRIdqLhfeebtcoPWUmHKv1D7G0q8Rkm2SL6hWT_JPIF82zq77uSRoRnOofdSl_PJvvRf974dzZOhiPLmRc-JwpuNDbkYgyazGhnBoA4FWRKbXLgcpWH6yEFUlefwjMzqVrkAq5Px1FuGfGmWQJVfoRvwjByKwXUmIkeqsO9ou5km2E4yBCt4avyZhezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28665" target="_blank">📅 13:12 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28664">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🟡
👤
تیم سپاهان در هفته چهارم لیگ برتر؛ با دبل دیدنی کسری طاهری 2 بر 0 از سد گل گلر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28664" target="_blank">📅 12:53 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28663">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKNat6be9ugzGrW42VcwBKfj6whv2GSnpBuWuC2F469fjDyP2BvaZViH2WclMAb9emH0vhqy_E5Ahsm_2e8liwNcZ82st0yiLx_oGm5PDM0kHF-xj0yeLs4ExMpMuLOtl92N22OcqLHFPv_M92A6vYsiqRh7INbP6Ws0ZjdahvTouCzoDaMgukp1B14M3Mx_pSkdxcmShRN70rHMIWjdxLfjOcy1fslEQu28sgJf6V-doRtLU1XZ1FZUSNkqbDGgDKkkLvh-jZ2bdNzb0qheyPvPnlRSmmLWx96nSFcpSYWiteBIuAygKY2JJlMEwKpB3flakcY02IaDJQ0PEYdaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پوسترباشگاه‌لیگ‌دویی لگانس‌اسپانیا برای آلوارو مورتا مهاجم جدید این‌باشگاه؛ مورتا سابق درخشانی در تیم های رئال مادرید و یوونتوس در کارنامه داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28663" target="_blank">📅 12:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28662">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDhMNGjARNHKuoDcnto-qc9Nko9SxyXwR4HyHrSAuj3NKdK-0ez65Xu_cyN03S8uI9Auxy8ytLBBOJr5MvfZJGTuSXDnt-TfjzeWSE8naPhF_r1g3bPr8RA4DtrBMVSw8KzUYMdRCDi_b0KveJhItO2b6Fz0P0Rdbdg9--a0pl5v4a68C_NwZfii76KZoUIpmZh1j9l8Znkw2cOgwjXs9IIRSnouarNrkU3ZATtwbTV5glfgg0suTwO24E-o011xIhEP4kvh2xMgyzRA7DYpcfXQjLxrBlJkrIGIMpW0X4u1toYyqYD91Mj_lEJjR0IxPijhA8u3yepNp1aYOCBFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ شماره 9 الوصل به مهدی طارمی مهاجم جدیداین‌تیم رسید؛ طبق اخبار دریافتی رسانه پرشیانا مدیریت‌پرسپولیس بعد از اینکه متوجه شدند که طارمی دراروپا نمیمونه قصد داشتن برای جذب او مذاکره کنند که مهدی تارتار اعلام کرده بود که سن او بالاست و فعلا نیازی به…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28662" target="_blank">📅 12:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28661">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpVIZIoE41NBwleiCMuaYz4OY_DBifu0w3pcUMNxXAC7SJHEUAqrl-X4P1P-Rzv-d7jeHA7hdTa4XVBeioURXZnS-LTiYamxElnf_MylwQJiYX5S3NPjAVIM1D4pGGK7NfK3b5DQtIfnqfQjxu3GeRgaAb16oQBw1uJ4xBN8L5UHcB2gqwCM5R0zI-lNyLh0cYev5nNm-E61HW1t8Cmc4dq6DDPPLNjMrzwIBhjtY8TP2wZohFBbdB6cm6fz0NnNKHAKR5aHk9Q_5Y1Mez9fYBKuSQ8GFMtlXVFmsOzWnciBSLHgzjQo4DxTHp32-nc9o7Xx2sFaCVzwinkvD0WlGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
کادرپزشکی‌باشگاه پرسپولیس و استقلال در تلاش هستند که ابوالفضل جلالی و مهران احمدی به مسابقه شهرآوردپایتخت برسونند. 48 ساعت قبل از بازی مشخص خواهد شد به‌بازی‌رسیده‌اند یا که خیر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28661" target="_blank">📅 11:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28660">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2LYg2t6f-wnQjGojHtS2oaz3y8vfur8uKhLn-WMmKsNMIqrhdp_vlCjKzrk008pUyuZ2El2DVweJzK5E5J80jXhtyJSV6jJndOrGja-BznkHZSb47t6ehN1Xw7eOFSqchBjKFePiSbQSRuQjGsetqWbnL2uUxky2nec-UZOgw3zO5vyc7y_D82Nu1AwU0cjOKeUYpy-wPpgp3oJqkm2DMbovIwg9mrMFp01FIr9aGm3UwnLG1PkUdpiYOMfpcsConXTd6VqtTpAcvzwRXDjefzXgeHnnlHzQVPSujf77j1vjB9xqRIOHiL2J2By0ogkuQL0PlfBQpYb_UmVhF8fbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهریه دانشگاه آزاد رسما اعلام شد
؛ پزشکی و داروسازی سالانه 137.5 میلیون تومان ناقابل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28660" target="_blank">📅 11:27 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28658">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HWo_PXdAA5YTOiWHOylezcR8ploMXwg2CVQYrfxNgfXz6CoA6PPFiwQetZJEMMH7JTPTV8ySb-XC6d_vvXzApLRjOyvdaXxxl3YLxSJM7K5bJ05_wedDRN9uLKEpWIseQv_bqEF52wzkLYaLqiQPYYOZAryfDyfRazVz3Fg7_KbCYdD-hXK3vbbOmuJy_QyAl7sgmL61Y7EC1G0ZFzDNcgb5fRCowl0-cPPotfPzAoH4teDVvA6EnxX4MH25gRkA5yNSz4htABjtuE_NqmGG61VI2HzUavgT0NQCPeTorhIWmbjsTB8ubWT_f3J1H3MfY42zxkD0PygoeSopAjV4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_fZ83Q6ihhnP1-qC2ypN_muQy9XeTZ4sScQN5KSOoJ5Qm54TvV1_10r0iRlTNEzw3iUbNqr3uJ0CfdhXjqaMs97NBmWgzLtJr6fYGftTUl9zMe7v6OSYO02oqTv1-SrfJTTuENc06DV64E4WEkIeQBvOPR2yDS3NmWO0TbfNG6buK1cYX6Ry7U0ajuozWEgUqiGVbVYdjJGYJPgEF3QrvvFkCqku0LUrKgLUV4EPqr2ksy17BRtryOq9BnlboYI4iYqGovB--sKlcSFGaG-crZQh_DPIp2ClvpSoXJ13vopq7XIi_SUpFNkeY72zuKqwg2BpQmWHesWRRW3l_Z2Tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
دوست دختر بلینگهام ستاره انگلیسی رئال مادرید و یکی از دلایل اوج گرفتن این ستاره در بازی‌های اخیر در مسابقات ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28658" target="_blank">📅 11:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28657">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUyfIaybdmGJjOx-eIPcGt6Dip9e8bo4JTY30sxK92RdhH5ADI_OgMSZmQwRzUMEoQJw-Jk3EI8BfyC6yJjEZ5g3tzap6_duXBR9RXsQFB0SSF-VdFDhnAcUxW30imdZyjGy6CRKuU4X-o7uvURrj0xwh7kGqxLHJkuYY0uulLJQvVWTDVfRBhXil0BiBJLrI9sfGy8-QdI_I9H5fJuIQ5_WzKk0uecCsHlHp0PGh_4a6nz57ZOSexidKiW-npvS6rWbPnXPW3h9lo7lTvAl8FJm_jWyCcG00z_LrOURa3nCpklo-fLVUjM7divcP7v-RHe9YjC5JNWxwhCQ03vcNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه گل گهر بابت استفاده باشگاه سپاهان از کسری‌طاهری خریدجدید‌طلایی پوشان شکایت کرد. باشگاه سپاهان هم میگه ما از فیفا استعلام داریم و فیفا گفته که کسری هیچ مشکلی برای بازی نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28657" target="_blank">📅 10:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28656">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=JaNJ_YzkwI994dEoH3lc_iQLETIp3D9WhtUXcp5hPQ0hoA11S_mE-HLCXlmeoU8MgqX2M2rgLtcg_JzRkdAj9cMwxwQT-3SxhXrhEjt2W0wBHtJ--mDOlVjVZvWInHyEdq2VYMl2mebT3P9rzITlgaypScG9yD6Bt9W4zHH0hp_lTr8H24Q81jCkXDn60H5ygQA04SDGX2_jxl4jEfwMB2RXhSeRdbS7Xj9d_QGJih9MCWmKhgyHy-OWYFbCfCR03wTgcGabP0Pk2GQRwQfnGsSkTAM7zsDC4K3BD3VtzHbv5WErjJ2ACTi6yxcE-r_VbsvegRBVzTGbcpdNyOa_1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa9fc8311f.mp4?token=JaNJ_YzkwI994dEoH3lc_iQLETIp3D9WhtUXcp5hPQ0hoA11S_mE-HLCXlmeoU8MgqX2M2rgLtcg_JzRkdAj9cMwxwQT-3SxhXrhEjt2W0wBHtJ--mDOlVjVZvWInHyEdq2VYMl2mebT3P9rzITlgaypScG9yD6Bt9W4zHH0hp_lTr8H24Q81jCkXDn60H5ygQA04SDGX2_jxl4jEfwMB2RXhSeRdbS7Xj9d_QGJih9MCWmKhgyHy-OWYFbCfCR03wTgcGabP0Pk2GQRwQfnGsSkTAM7zsDC4K3BD3VtzHbv5WErjJ2ACTi6yxcE-r_VbsvegRBVzTGbcpdNyOa_1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوپرسیوهای‌دیدنی‌حامدلک‌دربازی‌با استقلال؛
تقدیر رامین‌رضاییان از حامدلک در رختکن بعد بازی بااستقلال: حامد نمیبود این‌بازی رو 3-0 میباختیم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/28656" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28655">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=ppGEOsCuf4SR0G00eNnMoF6y4xfXPqOHrv70cq_HSeRWx2eKls0hwmU0lTYiJTYJn_yfP-WhQerC1LMuhOLmx1QB8n6jmao4KOAvV1wIGn4Zcfwej99IGu3oFuF3KaMkLpfMxe5EiBEMJW-hgx4ziioizhAQkLfH47M9QgI1Oor5slGy14RfCMgzB9axJthKNyyaB88WfWdcL7L9tiBkk05pfKFMpVZUfHCotugIToU0UW25GHqQzrMgepTMCbT7InEa-q33XaUTLh1vzlJgH43LPZvH3GiyzCRAf_dDcLp9esi88z6GR5ue40joPwzPEGPz52kKG56fbPPSQGtp9bRe-Bi4EMtXfCIqw-G4f3qd6t6ON8zySWdxQLTub-sK2tVrTSlaZ-fgUmmcfH1x6jWTzB2WUyhCwL7_i9TnT6LX9PkHykFoFZdvJvXbvpp_U4jEvfpum_E-SqLyaIxkJKEqk0BzG_ED6aQg-Vk20_CsHtI_HHnSUiSGtWEwOf35loBVMDmPhnwoIFPYe48Uo_wXLMocglP-YPR0szeMmcBFkYmNrUe9gp2Pyy08QXw82W2osqt6SRAgYpqjyYndD97RneGG0spax060pEQVpOJJkzOEqwcDkDVQEBFKmXQPY-0sgcgzMiYtY9QGPbNfzDjAZvo67PXjxuO9hINnkr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de192f8f44.mp4?token=ppGEOsCuf4SR0G00eNnMoF6y4xfXPqOHrv70cq_HSeRWx2eKls0hwmU0lTYiJTYJn_yfP-WhQerC1LMuhOLmx1QB8n6jmao4KOAvV1wIGn4Zcfwej99IGu3oFuF3KaMkLpfMxe5EiBEMJW-hgx4ziioizhAQkLfH47M9QgI1Oor5slGy14RfCMgzB9axJthKNyyaB88WfWdcL7L9tiBkk05pfKFMpVZUfHCotugIToU0UW25GHqQzrMgepTMCbT7InEa-q33XaUTLh1vzlJgH43LPZvH3GiyzCRAf_dDcLp9esi88z6GR5ue40joPwzPEGPz52kKG56fbPPSQGtp9bRe-Bi4EMtXfCIqw-G4f3qd6t6ON8zySWdxQLTub-sK2tVrTSlaZ-fgUmmcfH1x6jWTzB2WUyhCwL7_i9TnT6LX9PkHykFoFZdvJvXbvpp_U4jEvfpum_E-SqLyaIxkJKEqk0BzG_ED6aQg-Vk20_CsHtI_HHnSUiSGtWEwOf35loBVMDmPhnwoIFPYe48Uo_wXLMocglP-YPR0szeMmcBFkYmNrUe9gp2Pyy08QXw82W2osqt6SRAgYpqjyYndD97RneGG0spax060pEQVpOJJkzOEqwcDkDVQEBFKmXQPY-0sgcgzMiYtY9QGPbNfzDjAZvo67PXjxuO9hINnkr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس‌رونالدو با۱۰۴گل در ۱۱۰ بازی به بهترین گلزن تاریخ‌النصردرلیگ‌حرفه‌ای عربستان تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28655" target="_blank">📅 10:40 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28653">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=hb_RawkGSZXlGEUyeMAcPhC0tkwR64_wtFZqxHeyQYgO80HcSrcO3roz-Oe8Yq6NWb_88ggT2f0F5qTMKySqPWmh4YMxnzfu6Cz1EXvY50VxkO_HyrB0363hfv-n09iwI8ho2xMEcPTWGUe0cPXbpyGQU15OLmg_rF-C_ERBZDPuIxiRbgrsBQe27hCTCinGpmQcGQ94BK535xcIh3mCol0f0VpYUARXgrzBVyA5_a9wTaHxfCy49VgJwGoTdwKH18DTokwLCEk0MDSTEZrNAX1i969BLHpPonPu2GXy_EdS2WN2qYX2Qk4wIVDV4MeUhY_B2I7Ov-i6z39BZT0EBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41bc6c0a53.mp4?token=hb_RawkGSZXlGEUyeMAcPhC0tkwR64_wtFZqxHeyQYgO80HcSrcO3roz-Oe8Yq6NWb_88ggT2f0F5qTMKySqPWmh4YMxnzfu6Cz1EXvY50VxkO_HyrB0363hfv-n09iwI8ho2xMEcPTWGUe0cPXbpyGQU15OLmg_rF-C_ERBZDPuIxiRbgrsBQe27hCTCinGpmQcGQ94BK535xcIh3mCol0f0VpYUARXgrzBVyA5_a9wTaHxfCy49VgJwGoTdwKH18DTokwLCEk0MDSTEZrNAX1i969BLHpPonPu2GXy_EdS2WN2qYX2Qk4wIVDV4MeUhY_B2I7Ov-i6z39BZT0EBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇵🇹
سوپرگل تماشایی روبن توس ستاره پرتغالی الهلال در بازی این هفته این تیم در لیگ عربستان؛ نوس این گل رو تقدیم دیگو زوتا فقید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28653" target="_blank">📅 10:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28652">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmKewrkJcIGSyqqWrGMqCaeCRBRdi-r_cFPuAZRYGyk-xIxQ0guDhkfzHtAha-RXwPbYNgfsmNNRF8ejo413f7jWW-z2vurvkn_S3kM7fUd-BtIOhfoM63h3yCm2LL7v_msMMoQfjDXjqhchQgqW1imSlzUNxAQVf2indHY_4B4NcnowDSWU51s_0bR1W2ovGWWzYv7HpM7eunFikgjJf0e8xm-tGRCo7vqvNbqJ7FckvGTlDoOuartt7izk_V5fz_D7Sd4ioQezIPLFaEbFCYzEiElWG0_tm7gwe5Q-EKuc_MhNGXh9Wp-v0H7Q1QcyJwPogYQB0uf9X4PBzc4r4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌چهارم‌لیگ‌برتر؛ دشت یک امتیازی شاگردان سهراب بختیاری‌زاده در گرمای شدید اهواز؛ آبی‌ها بی تلفات به استقبال شهرآورد پایتخت رفتند.
🟠
فولاد خوزستان
0️⃣
-
0️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28652" target="_blank">📅 09:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28651">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=JrXjqDyhfaJf3RIYxQN73TwCVtrHqtaNvfVjsEDKE30jL_eIgM3oGS8J9Kj7x8pTyGmdwkJD7tqm_-B_hw_Hi9-LsJbBRdQuLrcPPTBiP0KnWQoXUFTY39eeZK_LSot0odzmjYSNBMbWmJJgW51T_BmUBVp0ik-XKaiqr1xcZE1ISkBVRiQSs1SYOpACf8_3LZjDBpzUbzxgbbHDiUuvNW4jlA4zb1meSEW3X8E0W6XFz_BIY2vRtkXCYAXw1T20ZseeG55GENpXHHsOIx4AfqXpouwS2nbsjclIvrm5zLhhAieojb4RIVLipV7VW4ANHu99YjTdfIKGJQFSsHWPAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7ef945d2.mp4?token=JrXjqDyhfaJf3RIYxQN73TwCVtrHqtaNvfVjsEDKE30jL_eIgM3oGS8J9Kj7x8pTyGmdwkJD7tqm_-B_hw_Hi9-LsJbBRdQuLrcPPTBiP0KnWQoXUFTY39eeZK_LSot0odzmjYSNBMbWmJJgW51T_BmUBVp0ik-XKaiqr1xcZE1ISkBVRiQSs1SYOpACf8_3LZjDBpzUbzxgbbHDiUuvNW4jlA4zb1meSEW3X8E0W6XFz_BIY2vRtkXCYAXw1T20ZseeG55GENpXHHsOIx4AfqXpouwS2nbsjclIvrm5zLhhAieojb4RIVLipV7VW4ANHu99YjTdfIKGJQFSsHWPAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده الولید بن‌طلال‌مالک تیم الهلال در حال دوچرخه‌سواری‌درریاض‌درکنارجوانان‌عربستانی. او با بیش از ۱۹۰ میلیون یورو سه خرید بزرگ برای الهلال انجام داد. سامرویل؛ ۶۴ میلیون یورو؛ واتکینز؛ ۵۸ میلیون یورو؛ مارتینلی؛ ۶۰/۶۵ میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28651" target="_blank">📅 09:45 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28650">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY18GxEC0XKys027adIMfQ5bWZC-O43cGJdzxi4JbVAtnjSFWiQHKbLgc09ROWwiTJy36Ri-g9_e2deCFNyuuTlcVPJmtPNafyOEpVoKnP8ur1EBLTa3ICPgKTp4WtTZd6CmTg9zHp4A86vda0cheR4Jdhk8jYxxdZD2dAnbuMTWdkCgrJQ4K0lFgKL98QPvMeB94_KW5SKskFAZ_Ug0YhRh6IGaYb46xt1BAkmJ9XUpa1IUwbwBt4rrrrCG07geZ6hCQAViKXVH9-tBzsvRv2AaiSf8EOKnFM3c40xeTNWyPU2UDPTERy_yNgY-8gX8aD5iY2eciZfSi7R3AvOIxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تارتار گفته به اورونوف بازی ندادم چون دیر به تمرینات اضافه شده درحالی‌ایری و محبی هم دیر به تمرینات اضافه شدن اما فیکس بازی کردند. واقعیت اینه تارتار هیییچ اعتقادی به اورونوف نداره و داره کاری میکنه اورونوف خودش فرار کنه بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28650" target="_blank">📅 09:30 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28649">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=Bs_Sc5F9eYljOr0xN18jGoeEFWxQRTqtiVbi-9YDMBCHaqP-2V3gcIUIu9T7LdfYkdu0kGgLBEwX3cZyl2x3CAnPWvNncEyhC3SyQFsiY6xHtMFZohkBZOSxnJw5Gu-MAjEuR2sj3cXX9nuOCn6zJrFI5lKunS-Q61Ja6xN0s4TKB03FuGFPl_JfD6NEWlropDU4IMcw6C303HJ9L7yGaTY0BRBb7zFZiXE00RJRd6vXTXh3mNt-oJ9NuI0uPH7ppSN28yuSjiWmePcdNe8wWpmw14stR8JpLwynfv7r7ehr1HUZiF5dlZ-M4rP-xwnKzfGzo004W3oBEb6WNpk4xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6abfbbf23d.mp4?token=Bs_Sc5F9eYljOr0xN18jGoeEFWxQRTqtiVbi-9YDMBCHaqP-2V3gcIUIu9T7LdfYkdu0kGgLBEwX3cZyl2x3CAnPWvNncEyhC3SyQFsiY6xHtMFZohkBZOSxnJw5Gu-MAjEuR2sj3cXX9nuOCn6zJrFI5lKunS-Q61Ja6xN0s4TKB03FuGFPl_JfD6NEWlropDU4IMcw6C303HJ9L7yGaTY0BRBb7zFZiXE00RJRd6vXTXh3mNt-oJ9NuI0uPH7ppSN28yuSjiWmePcdNe8wWpmw14stR8JpLwynfv7r7ehr1HUZiF5dlZ-M4rP-xwnKzfGzo004W3oBEb6WNpk4xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بجامانده از دیدار شب‌گذشته فولاد
🆚
استقلال؛ برخورد سرد رامین با یاسر آسانی و صالح حردانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28649" target="_blank">📅 09:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28648">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9d5kpn98WwJ7uUeePDMrldY1t5vYBeGkbC-ZizVx5GymG6v4p5T318vxXzx7JKw1D2OK9ng3tvtjjm1fzreVT7HH-1_hr1IJXBgSkUp6Lt7zXWG3nZHfN-NPB8x-o3pYcuVjUv4KEjrgyJlMPXvu-rJqm8T2B8wT8isNJrrXTMOXwZeiNujJQCYe3bsULQ6Zewll73kpqOa43hre2QTEHiCkGuu6gifynL3s1vFD-02SyrZ5U-c8FMBPycrYz_o6tq5keaQWfB2v8Wkocj0gxZM4OHVcdp8zNmQYiACVMc_gwCr8V5Frxmc7gY0U43-q8bjXpMWgA5iijngm9XA4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شماتیک ترکیب احتمالی پرسپولیس برای دیدار امروز مقابل ملوان انزلی در هفته چهارم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28648" target="_blank">📅 01:45 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
