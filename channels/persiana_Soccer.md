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
<img src="https://cdn4.telesco.pe/file/dPqY9QQV9S6tjg_RMDBo9DPYTJrlqg3NYmoPyCE5hS9oQVslh8vk8g3_5JUa_N9b3D7FtlyQyQfQJQWsx1vpNPXGwRy-9C62-5VQMhplOaH53wgLj238jH7In7t1FjIuc8Sdjj_gMGGt-NNTjfCiLI6p6t9aLyjFjiaWGnv04jTAWUDHrKnyZtJ_qnwihftul86ReJ-xejRCCj_6yH1MaJBN8NIg4DRX4OvDoQHTTKPGdunrIcPHNzpKIqZo9v-B5v0q2oyvxwoNb8SCtOcbHP_u3ViRShh6VNqvq3qm4T-zVe5pgXXXKajEt9rZwiVfu7xLp13gyXfMp9wx18a6Cw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 195K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 19:08:14</div>
<hr>

<div class="tg-post" id="msg-23193">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5yqJXy61M12wDh1HbFW9i__RdqfFbHWfAc7YvLn41b4lWlauwI5-Cq20badQ2o4QhH9Z6joHsux1w04GYHPy2eJdYUYnSyeQYr-KcW4E8bA0V4pyTCTuRbEVx2m-Ow6BF6WQkrNYfR-55_5MKGrX3kaTjuKpnl1IVWkWHLBHiLiIJPx4SPsaUVkRWKm_TRsWsWI9BPvYuaQE4DW1SF3FXwyhGK55QGV-J0qL4mGCb7nsbdnSSqe7-k56sPqSEDU5cKpTZ_zwDx-H9eOYN4YWcXmdpdFAXTvsn8TJbhUfSY9VV7S3p1taTtk0hqsIWCaEpdspxpa0FXrGMPc2kIaSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/persiana_Soccer/23193" target="_blank">📅 18:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23192">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=CPs3jJEQK2HOaouuGjhgLyfqf9tjeKJTVo7trX6AJu_qzzupGXtGS2f_C_69ax4wOW1IeXF9oEn0AOVp6zHxxgsTTYGG0n3RFak8G84Vv2dcmILyKhGIOwvSmGtAKl4vvcuJTX4kbezaIyytt8AV4uqvfFaH-y4mfQYnKQy_8ur-4cKnwd6OCfw17z3eYCZQls7y24K9Y8QkOmgXjwOtd9d5vs2ueOmFw4QSd1vyOeOvVTfVMdpwyV4FnS9HOq_-FAaqTzF7m0zjwBDFL6ysqirN_lLryl7dEGMQWd9seAp5OJBkBsKbRVsvKm9w3Z8m-y4v_XPMgjXmC8ccKCe70mOOvQ32pGwKa8_CcJdJTlHlGIUBaxOOFQ_yRu6kPGyjrpbssA4D_kLtTSWASP_y6XAQFo55arDYyAjp_yhZ7amcay76_DxNJ8WXLgMdGeWtSCfAMhnVDDBIAUKy0QIdyWOG1CnZ1tHZnoGB226UKNqHykYU0TE9eTT4S_yFH86h4KwPJxf36YymM5n7fBGSDv-J8S9mvMBGFSk8LI3ENUYYx062ClrQuqeUUuz8aqsCqEjUlsnzTEWHjqQTkTI8Z9-s9wlJ0JdInWponoIC-8Gxg7y0mNDSUDI9jxmHZw4V9rmuzHHOJbYikjLKqUdSFRaMHVMmR0j4PgxMIAavWDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88bf35c2a3.mp4?token=CPs3jJEQK2HOaouuGjhgLyfqf9tjeKJTVo7trX6AJu_qzzupGXtGS2f_C_69ax4wOW1IeXF9oEn0AOVp6zHxxgsTTYGG0n3RFak8G84Vv2dcmILyKhGIOwvSmGtAKl4vvcuJTX4kbezaIyytt8AV4uqvfFaH-y4mfQYnKQy_8ur-4cKnwd6OCfw17z3eYCZQls7y24K9Y8QkOmgXjwOtd9d5vs2ueOmFw4QSd1vyOeOvVTfVMdpwyV4FnS9HOq_-FAaqTzF7m0zjwBDFL6ysqirN_lLryl7dEGMQWd9seAp5OJBkBsKbRVsvKm9w3Z8m-y4v_XPMgjXmC8ccKCe70mOOvQ32pGwKa8_CcJdJTlHlGIUBaxOOFQ_yRu6kPGyjrpbssA4D_kLtTSWASP_y6XAQFo55arDYyAjp_yhZ7amcay76_DxNJ8WXLgMdGeWtSCfAMhnVDDBIAUKy0QIdyWOG1CnZ1tHZnoGB226UKNqHykYU0TE9eTT4S_yFH86h4KwPJxf36YymM5n7fBGSDv-J8S9mvMBGFSk8LI3ENUYYx062ClrQuqeUUuz8aqsCqEjUlsnzTEWHjqQTkTI8Z9-s9wlJ0JdInWponoIC-8Gxg7y0mNDSUDI9jxmHZw4V9rmuzHHOJbYikjLKqUdSFRaMHVMmR0j4PgxMIAavWDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/23192" target="_blank">📅 18:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23191">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTySVwZfIey8ZUE2OBeeEYPqkoN6deazvKEYUw7KtOtSwzzi4H4exUhFzcQlCQHRLj3Od96XvQwksiemzQ8DcE9E5i1TR1KIaL67vJRdKOSP3--1onEATf6ah70zaIJAjgX7Mg3EU3TvXkPhy5hElVLkoyp40gY6RKynbXxAr6fXZ_wj2j1ISTGE8nn8WbDbyD0NLTY9j0q34a4oHhSkaVvsGvOmAWMr6d422hXXnSx1o8mpu33leglElilDL98N1tQp3nw87gA9WldChfIemRcfCvue2107DtrenWABCNFzkgJ9cxsZxLTSPuanRISU9WuLj8q6G9eYxAye4TW09A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/23191" target="_blank">📅 17:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23190">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmPdpmVSfK_8ABu3-lohN76r8kV9x9cee0C3bvYozlANdBeHyuUHaQHwznGrjnsc9SAmgZ13599uXTGAkQ7Sox0lf0C0QdZIZUk6SuZ40HJNL6ggADW0ED4B80oLZhBaBHQMNboCQ6XWT5V6sxdc5VI_wSU0pGMJ0L7JW__73eBP3xSBv11av0kt5Xek-KFgQuGt2SMHd4pJ1fjcegvIhR77t_OU1L4gZ6AkHQ8fDFx9KEmqKOmMHTcm9oW-ARdRoozsYTKXEh7POuX6TOPlbN_tNsVCgdafdm1DZwuPmNI2iNzu2uaxtI9TeQ8ZfN4DoF-MM_ENNjE3QLjrWWDayw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/23190" target="_blank">📅 17:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23189">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_3M2vUg0hvtybZ3WEumhcJCWOem_haVxPOFthAhvxS2lwJj6tt5M5WdcpUlfpD7GSJloTvo1bc259fyhWefFcgHS2HE3woipHFMdOqKE_xeD2l8JdQ0Oq7bFEEWwDtDWI7QeSeFm7zA36faS2JLmXzu4QuOy0ipO2lXWsmdAIJsmhSmOPFje6ofo9SZP-ZWhDHu3Ue1J4LUUhcGskq2ZRu0tkDQOaKfJ8Pw9finQHsDKx2P1JNi-BGfSGk3gGRGkx1F-9zWOLRxwmaV6YTkJGBoQ_-Mw0-3I3HywtsazZ8Jwx5OgQZARURwcJeHRdwRVaZBcJV3rzL47Kq6yIGIIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیستی‌از اموال‌برخی از افراد معروف کشورمون که درماه‌های اخیر توسط قوه قضائیه مصادره شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23189" target="_blank">📅 17:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23188">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uV0fHxocDBSCnLpUQRRCB5vDs4bJn5bAMyeJ1jMKg-d8Q2PoYPOeGYKUT4P0e511ubsL61AMLFe2dwXZOtcrn4gvAp9PosKTuKTl9NsanxHZQZQy3BpkzHXt3FpVW1hT2UusLjR_mKwaZSc4b2Kjee3vaaPMh1v40XJlghpymfH00CZ6mUge6R5Rgl5737gkkqr7sBNq6jjGWA1q95dcm4MANp8Uiu_aRMuXR18jHfKBBTYhLj8CyA1ZeX39I4HaRtWnJZ_mWIrQXvrGHC7v7zIH2tA_UE5zKxtqC1VLBjaVf73mXl44nUACvrmnC4L2r8SFwz3voejkpf_uIDcsHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/23188" target="_blank">📅 16:53 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23187">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyZt8ReuktX6a6bcwS0Jl4LARjtb1NHweMx9aCqDccHiInlnqYsmC2JK7GltSHQcxm66xQAJ5JjFd0hX2SyhWsJWnDrgJFMWei9i93LbAe6LJDjpa0r1Lhquayv47BpJi5BlBc85YmK1XgIt7eEZFzqZiTSJyt2YgUgQPejv4uzMU-a9k6YrXqcjZPFD3KPtylA7SA7Gt4P1wpfe18BtNqwRU1PnkO8qGwiS11MbmC9OAo7zXG4_iv6mgP1kMJ8lMpVaERMH1nskAHcnRoZ0Z98iW61YQlJcjg5PEL_UjGcgH8nP8dR7C4NGruLkCtT1DWaLefVy_s3Q-xibSsGcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/23187" target="_blank">📅 16:44 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23186">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG4o0UwptNahOBlCDLu9EFQyd4OSEMcWx7QS1dCo7H5elusQUeKlMwkhJwjK-oOAjHEj4Yzz1MZTD38iKF0W14-0lV7tcw8dXPPf29fAms52gte6geD4uU7wBa5IRP0S1cMjL4ynju4J8RLT_fnxI8FgVhUK_4RqbN1gboBWz_4cxyqeqncxo5gaeigl-LEM2uTWaNR23bOFzvqQjjeI9wVJDIsppBH2vpGawrr6pxrY06FvLDObYKfaSCfvpcFakwaTc2EOXqA3CTRHbUZ_em4CJNM02-lIDROjvd4b42esXq4zIIw-b88aRbCTW8FHWLCjQUYaA0MRFNKdM3edUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل‌مرحله‌گروهی رقابت‌های جام جهانی 2026 در یک نگاه؛ این پست رو که کامل و جامعه هست ذخیره کن و برای دوستات هم بفرس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/23186" target="_blank">📅 16:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23183">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlypvmNt-BkeO_E0B69m4uviI7FmVvoePTcNXzNuEPYj5-hbUvZ6x9y2BBPcJen21Diz-o8b8RD3IIr6KgjORVx1OAD_DrqJjs5ogfLTHg7oVS8UwMfzYV_LF5rzyPRVgETLUG-YEs9C3fHMXXE9_oIyQkFRCWQvWrT0t5fza1RZ-nITUNyImyvRkqg0MJwMbp_K0MqkJlKn9XdekpfQDFjk4pwK9_GSUu4YBkGN8yS6pHklfyhW9qWOIdHCyt44RzA6ezmxokLPhgcGRYyg-BPsPp7JysCPyjwih9ZI5rGu7YbFkffvb0G2mpky5SM1JZoAEOXv4ZeatVZ8akJlww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=MdUsYZJIaQ85iX2zp8FQZQj9pgzpmesQlGm-gT7Fx3V5wRLKKnbiJywxnOLah0ufpD4WGpbv75LRWgALGJzqTcs0uW_oMmw6NHZ5ZjUg5wiVG_knrlMi8pQNBl9CYoy7qkWNnn9557NBCV-AvD558uZMpAZI4uso96Ef3uJImv4FWE7cii3nzUyaGdxOvloiWElDY8xkahd_NLO2E0ivyEVD_tFvb97s-QKBwQRW0R-BLuSSigHJPEDn9y0LSUbfX7ULqAoiP0hDNGs9QE0ZHpakQU1UICD8riu1WlDz_LMhMzFlHlFesrOf96iTh9-R4LFt0UN6qE4dT4bdlC00Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f875912f.mp4?token=MdUsYZJIaQ85iX2zp8FQZQj9pgzpmesQlGm-gT7Fx3V5wRLKKnbiJywxnOLah0ufpD4WGpbv75LRWgALGJzqTcs0uW_oMmw6NHZ5ZjUg5wiVG_knrlMi8pQNBl9CYoy7qkWNnn9557NBCV-AvD558uZMpAZI4uso96Ef3uJImv4FWE7cii3nzUyaGdxOvloiWElDY8xkahd_NLO2E0ivyEVD_tFvb97s-QKBwQRW0R-BLuSSigHJPEDn9y0LSUbfX7ULqAoiP0hDNGs9QE0ZHpakQU1UICD8riu1WlDz_LMhMzFlHlFesrOf96iTh9-R4LFt0UN6qE4dT4bdlC00Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/23183" target="_blank">📅 16:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23182">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs2x9_rq81HYLTc3dmG05ec880sHJhbp9tlNo_vMEYhq59OGkyLRKZD2is1zXnU08Sya94AsQYhjIH4-wZeCrVlQnl21TaFYXerlDwZmx0JNBp_oR56LccgkDKV9oOf5tjaRlAnm9z86Xsob016K64bO1wssYeYfk2u-UHqEcpgMw-AbeXGIOdhtt2x6Una6-PLee7apJaexapoUFPGDsxZmlbi7I8mkbZGLBlr8gMFSD7_q7tvor4zJBWndRTFFc9ysru_PzBfBAW0QykPRGqLO0e-6MqGK0vgcT1rF2X5U3GsUZ-AoBmlozJF87jpy6k9OKQ4D5ve_6e-hzYByng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
رتبه بندی تیم‌های ملی حاضر در رقابت‌های جام جهانی 2026؛ یاران لیونل مسی در رتبه اول جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/23182" target="_blank">📅 15:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23181">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojwjhhf95pr4VCUDv2hJyBbLmTLUsLzF_f_uroUhZMlpvsYAvBHtfkYNFLXjmcNqt_g95fGFHoSx3q2fXkR_1zJmnOKMSq29Ks2Pc_IPQ5JWAcixgVLkPd7OW13C8C6KSJLoLcl6cKVq6mJRVBmKuGWCaAWOYx9VDfqB4bkbztsVZSD50KakAKqcffMhg9LoA6uDWv4sXb74SVQHRRssfe_xJidE8_6rCM6-HRA9I-ACrP9qaI09wGE-PbEC8S5xL9rXyDh6nxR8B3JgZyxB-EeTvJGhnRyrSBRdp77tTtAOJFnB_UpvFzPbRyQpHxq0c4HFphGwKWuk09WCMBPAxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول به نماینده‌ اش گفته باتوجه به اینکه از دوباشگاه رئال مادرید و بارسلونا پیشنهاد داره‌برنامه‌ای برای‌تمدید قراردادش باسیتیرن‌ها نداره. قرارداد فعلی گواردیول با باشگاه منچستر سیتی تا تابستان 2028 اعتبار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/23181" target="_blank">📅 15:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23180">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=FQwOOAllXYB05rcOZaNAQZXjLAAnEq3dX2Xx6ezISxyOcjqXzfx8RhzsMEEh6o7m2E7sLEkWW8j3Cn3eEkgSUoWY5mlTZcyySpjwzhYakWCem2Sde_0UVm0MBnADsWrm25xzkY8oGzAor3Z3SfK47BKLAqZBjac4q0ExWn_QnK8nKdnVJZ0zQoDQKRX-0ikHDYUjamsgmNFQqekiNwSHcTHuDKZP8lZF9OUKMb_HRsQcIMPqurJ2siCLM5iiVTJjqB6D5hisuO-fBP8abr4VkJku_4lLM3T1c3qN63_ZKwWDR6MNOrHvF1VVgudfh2hlLreMbJAXqHb_vBetcFccxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e075d0a791.mp4?token=FQwOOAllXYB05rcOZaNAQZXjLAAnEq3dX2Xx6ezISxyOcjqXzfx8RhzsMEEh6o7m2E7sLEkWW8j3Cn3eEkgSUoWY5mlTZcyySpjwzhYakWCem2Sde_0UVm0MBnADsWrm25xzkY8oGzAor3Z3SfK47BKLAqZBjac4q0ExWn_QnK8nKdnVJZ0zQoDQKRX-0ikHDYUjamsgmNFQqekiNwSHcTHuDKZP8lZF9OUKMb_HRsQcIMPqurJ2siCLM5iiVTJjqB6D5hisuO-fBP8abr4VkJku_4lLM3T1c3qN63_ZKwWDR6MNOrHvF1VVgudfh2hlLreMbJAXqHb_vBetcFccxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
جوادخیابانی:
سردارجان تو الان تیم ملی نیستی ولی هستی، بعضیا وقتی نیستن نیستن؛ بعضیا وقتی هستن نیستن؛ بعضیا وقتی نیستن هستند.
👤
سردارآزمون:
آقاجواد حقیقتش اصالتا ترکمنمی هستم فهمیدن اینجور مسائل یه مقدار برام سخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/23180" target="_blank">📅 15:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23179">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=fz-Eh-ww_O45P4TN6X8VwMJTgeEBAB5zODoiPH2vFezrNONOUbXfwUbiz9vzORIvjDNfmSjWVkauBLTPwnGav2dWO29ZWXHHiVNd4BL0yJOBFP7Qm22-o8DnBNAaeb1tTb-hSdKqBzX5Kz2o9ehuqBKMgXdyMN-VtlENdTatV6gc1sg1pGysLtVXLUl-a5SbfVh-xRJDdsG6M3CIL4rr6oafc51d-TYgEJzIoIcF6KLtm59L7x2HkfkPB93_eXp8SWAI8MebwXiaSJOtbL_d5WdwwoaVdFlwt3HPtiPitLXGUJBoW-c1Zrmu6ROYbp5EJHxJMLFnOWNTNe2jrK7vgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca2e774e3.mp4?token=fz-Eh-ww_O45P4TN6X8VwMJTgeEBAB5zODoiPH2vFezrNONOUbXfwUbiz9vzORIvjDNfmSjWVkauBLTPwnGav2dWO29ZWXHHiVNd4BL0yJOBFP7Qm22-o8DnBNAaeb1tTb-hSdKqBzX5Kz2o9ehuqBKMgXdyMN-VtlENdTatV6gc1sg1pGysLtVXLUl-a5SbfVh-xRJDdsG6M3CIL4rr6oafc51d-TYgEJzIoIcF6KLtm59L7x2HkfkPB93_eXp8SWAI8MebwXiaSJOtbL_d5WdwwoaVdFlwt3HPtiPitLXGUJBoW-c1Zrmu6ROYbp5EJHxJMLFnOWNTNe2jrK7vgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
#تقویم
؛
خیلی‌جالب‌شد؛
دقیقا 16 سال پیش در چنین روزی؛ آفریقای‌جنوبی‌میزبان جام جهانی 2010 دربازی افتتاحیه به مصاف مکزیک رفت که با این گل دیدنی اون‌بازی رو برد.حالا بعداز 16 سال امشب این دوتیم دوباره افتتاحیه جام جهانی رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/23179" target="_blank">📅 14:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23178">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqfiTeUz1FAvCwDJC86RfUC08lO9eG6H12aAI7hff0AALPXb2ICuz4yoxlVZ42xV-_9WXDbpjTm7tmZhWYtEVrn9_vREUv8b3v94Tu9TygSDeq_YkCSU3Iu_UwmjTiMwgJQMyq75Tk8xv_C_aTfKx3W5FQ2-Ha1WlffObU0rWVK0NRfQVsBPDzhIXfS11cQaWzbQTw2qCBxlDbpZBd6CsFIxB4hsj6cSyIWU3Z73hFl6fwteUgj6CIk62seM8i04h_R8zVDGOrIf-JfOmF8bWWi-Ii9Tbcf-LypZcRHuYU_9M6I5BLQQi2FPf51ulzLyA2f5MHZl7fjPXhBaa71ZDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23178" target="_blank">📅 14:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23177">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcQke7jTHwkRkNrkuefXrQsX5twN2zEld2vUHWMKz86pEXd50ZBCQMKKAU0GWATexojGCTWa7wCHr2U_QSguImSUpNvT9hRTUWTl5cnVh2MKkwJj2MN5sBZdkyJLpCrujQ9GnV9jfrL1MHjUqHQ-OB5OfxpwKifsJgGawDy8eShiGySJmX70DnLSFOj_ipWG0yxVm4VP_Ax8pOnXt_OTCDh_MR8NjAFpMTb33oCeoWQhk44oW7mo39WF1dR2xU51Z0w6CvEqTYPb6ZVMOICL53WOeiX5rWgwerIuVYaKbtf8JBwZ6-6xFbQ5jIY9ZF7vz7_-Ew817ZmMisGD9m_uZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های پرشیانا از باشگاه استقلال؛ علی تاجرنیا برای تمدید قرارداد محمدحسین اسلامی بمدت 3فصل‌دیگر با ایجنت او به توافق کامل رسیده و این بازیکن 25 ساله به زودی با حضور در باشگاه استقلال قراردادش رو رسما تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/23177" target="_blank">📅 14:26 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23176">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=f9uEN4CJ-3FzBaCAQOHHOOg9LbWUuy_v5oTRt-ytL2ID8kEQVtfdT32oZ8oxKvdEnNWVhqI2M8U_vh1UQ7RzQOP6FpBznJ7g2ysAhHI537WRRFeE-Nu4RRcdxWSG44CLTPQ_xL6_sAmaolUec_z-9SacNHTPNGAUbu9fCyV9MOqwjHIH0pP-qrbBgrApWu-nOF5AWf6s-cmQGDzO2XPFYtzR3R9S6lA4LgG_K3_mTpkvb2c-DWLRRQx-g087E9OBI7xjHmDRNKa5YK-8I9IB-qqPeSwIF9GNG44tOfVxg90sFRghBB27K3cpDV1bI4odBAvhbZnm-WlO0qa7Ud26RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18448ed5c3.mp4?token=f9uEN4CJ-3FzBaCAQOHHOOg9LbWUuy_v5oTRt-ytL2ID8kEQVtfdT32oZ8oxKvdEnNWVhqI2M8U_vh1UQ7RzQOP6FpBznJ7g2ysAhHI537WRRFeE-Nu4RRcdxWSG44CLTPQ_xL6_sAmaolUec_z-9SacNHTPNGAUbu9fCyV9MOqwjHIH0pP-qrbBgrApWu-nOF5AWf6s-cmQGDzO2XPFYtzR3R9S6lA4LgG_K3_mTpkvb2c-DWLRRQx-g087E9OBI7xjHmDRNKa5YK-8I9IB-qqPeSwIF9GNG44tOfVxg90sFRghBB27K3cpDV1bI4odBAvhbZnm-WlO0qa7Ud26RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
5 تااز بهترین‌پاس‌‌گل‌های دیدنی در تاریخ رقابت های باشگاهی؛ کدومشون رو بیشتر دوس داشتی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/23176" target="_blank">📅 13:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23175">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XE3g_lzEGF1Sh2bcB-3XYxEgYUAJrSXrpIltYGHoT5YPJ6i9ptHR6PzMMFvHHnmpQW8mWdBFlfsfcstWPfDTVoJFlFMjnsy-W7xzJ2ecu2JXcvbLaLpI5TykrwdalhLpGg_yJCAFLgtRIsPUliSVb63AxPdRmZURhVSUpB_myVCdEPAbE2iNiH4VWlmi8TvPa8_izrIcyXNQqY-6vlDZ1IGeT-ra3PazV2DzlkMkJsnLTp3Dz_xe9UMig-MVX1BPBRqB-_qxpq_R7uSgTpPJt78iat1nd7nM5usT-Gu_if2QbzGviYn5_Il9kg2sgYqaZMR2G_d_dopgm05GG7ayvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
🔴
#اختصاصی_پرشیانا #فوری؛برای اولین بار اعلام میکنیم که اگه شرایط کشور برای فصل بعد مساعد شود نظمی گریپشی فوق‌ستاره‌البانبایی روبین کازان به لیگ‌برتر خواهد امد. هر سه باشگاه استقلال، پرسپولیس و تراکتور بدنبال‌جذب این بازیکن هستند. باایجنت ایرانی نزدیک به…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/23175" target="_blank">📅 12:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23174">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jkb0JncBgrNahzIu09Ydxfqr78F_mBspsdHEt4Z1zwLv2l0CFS5pSrVhqy3R8dN24P9eT7G_zHreqgGbElQWD1WoEHQTDATk4jEKhiMh0US5fvTMPXOS8NiGTOtI1b9Q3hyVPsgR__R6zUo66HSrXasEI3AyuKMHEHXYymvoOw3DmQdwH6p6fNhzFFJiy1L_VrzbodyM2O3JesYBVwpVgPgTIgLK3X1VA-LQTgnNcSeGDqEqfljgMBAM-SwsOGCqy4Y2DXpR5ePKtbLXXZ8XdtOoVRsJ6-zNz1MQqID0iHr0bMaYNoW_K1xTYUvMxjVFPxQHiaDwM4KSHZcIRf-kbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23174" target="_blank">📅 12:37 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23173">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfZI7yAFfA5h3QvUgemAfcWC2zho4OgqD7dycJWNelk2idJksz-kYAih9jroxSiosXAtXVOr10mVoJlooI6JmSbUzCi7jQ8B10cuA-gyhVPNDAUfTMJXqVNizJ80UITQfSdS1rR_2WOC1_gn9iq-iTY6xw7zcmB89iQlP9AcV9C9iRkBm43Y1wwpWsvAezaSV9RjnYue0kNdNRAh8cLcM9BY_1XhoMl_rvi8jxCMq6ii2Cea_n17FmCquLrKU6lS6fDQrHDXxIncgLcf8q00pdiSD3JsXN7ms8g89hZ0-7Hu3Z3EuQYReOv70hrcsuF1JOwI_74cHC6f5mLyXoFIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد فوق العاده شش ستاره فوتبال اروپا در فصلی که گذشت؛ جای ستاره‌گرجی در WC خالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23173" target="_blank">📅 12:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23172">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=sBrc5MQVxPk1nYcq4bPqsfTJFRfZCpPIjZA-io52tdnXOFdO9RjRFmw79csWjtVlZHQOacf75qy_eLo5eyMadGkS2L9QG7scvyIliSgMuB2aQffq4zHuTBuKDJ_2tkDPBRAZuIucJhgK2fUy8MTPRbetWRB5PFlR1oz2aqIM6GbjzLNOFRbvw8tdgypF2q6dj7D4Emb-zcMcTezFqlnKSpVK-k13tLQ81e6-IXANZhAszDPZqmxZI2UxB9SHKGAIc9YukPaVf8zuZN7pjzjeioUX9PP-Mwg53IqOC5ER10Pd7PuCBZcIOpPz0F7ZoG2V3uSwpPLUfgIuycHXfad5xIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e4d302a86.mp4?token=sBrc5MQVxPk1nYcq4bPqsfTJFRfZCpPIjZA-io52tdnXOFdO9RjRFmw79csWjtVlZHQOacf75qy_eLo5eyMadGkS2L9QG7scvyIliSgMuB2aQffq4zHuTBuKDJ_2tkDPBRAZuIucJhgK2fUy8MTPRbetWRB5PFlR1oz2aqIM6GbjzLNOFRbvw8tdgypF2q6dj7D4Emb-zcMcTezFqlnKSpVK-k13tLQ81e6-IXANZhAszDPZqmxZI2UxB9SHKGAIc9YukPaVf8zuZN7pjzjeioUX9PP-Mwg53IqOC5ER10Pd7PuCBZcIOpPz0F7ZoG2V3uSwpPLUfgIuycHXfad5xIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ نوستالژی‌وخاطره‌انگیز از اوج هماهنگی فوق العاده لیونل مسی و اندرس اینیستا در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/23172" target="_blank">📅 11:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23171">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-UIvMKrpR4C7K0pjz3DbhMiA1YadBFANHfzQYIYgVkxPAd03dHydFrP9UuRPRoCr6xj8pita8cGr4jPBtpwRrUwxZlu68M6tpROQtHz42tkMH51G8ctoia4tXIrItdj_MG08Ky-mTtB3mY_4P4VR9fNos31YPRhcBVgH4VbOUXcry627KM1eTQJSxKb8RrxMWU7IyXA8DIRHPYqC6OxrpJv7M8SLlvXzN2jcNFTIjjW-SIpmIp4-gx-KIbjZWcwf4nSoso7uYpX12MvU_dIcRsAbx5piLtJRWlteHp3Mi_QFjHdcrAHGLBncOMCJRVQlc12MpBKUOVjM-I7uTSpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23171" target="_blank">📅 11:29 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23169">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwZZgTN8KtLfZvNfwpYfh709f9-0XtxDf0S1s5Ma2yxwi9y2AoKjSi2XUZDyv0upAC0wXjNSFQfKqo_3uaLAD29JfAybyn_PnFYj0OwicrBZ1WQQv2w2jnKuprL6VZCGqhUx9XG5-xbjaiE_HDSKUnve7VstgxnzxJeP91p2m7DMKAeRPgkHXcOkMB9Vt6rHlK7j9g9TW094R76yMDlCFhGXHx8VJugXAqVogMVvMUj0tqpE95V4lFp_TyvQEivMf1CtWwUZibbQSW3Q6sC30Z7zkYf0WdP5kbN74xdHM_R2e4aqo6G3mHKGleuGmWMIB3bIYeyxBA4KnsnSujbAcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZCCXE7u7K6ey3-SpetuBxfkLCp0DhM62NlYIs1LH3Tj2RPddRTqtkg2MieygBc_P4Nbmn7SxR-z64WF0qcv8Ah01dAqO6gI-ozZVfxZq8YkKejfVxo0M_wBG1t6spOV1nTmjLKxEiHJw_XZq8sX-fgUgFLTNbOXJmdo7gkplsCwoEh_BmHj4MtdlXboXJWWAp1JqdKIFadGOZwfHp4oPtZW14iW70Rnq95peqIFF-JHQhQMmai24IW_UBOkwwi4L5OesAfaPRiWrsHgmXX-ue4-_oPAnD55aUCDXf1X5hoMzq2vUPb_bT5h4IWYs68uekHYZd0SM5bdgPbU5lRe8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های‌رایگان‌که‌قراره‌ رقابت‌های جام جهانی رو از امشب با کیفیت‌ بالا، با گزارش فارسی و جلو تر از صداوسیما پخش کنند.
📹
شبکه گرند اسپورت هم جدیدا برای جام جهانی افتتاح شده اون هم میتونید فرکانسش رو دستی رو رسیورتون سرچ کنید بالا بیارید.
‼️
خودمونم‌ازامشب‌لینک تموم بازی‌هارو سعی میکنیم پیدا کنیم بزاریم. اپ آپارات اسپرت هم که چندروزپیش تو کانال گذاشتیم دانلود کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23169" target="_blank">📅 11:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23168">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RURlI03MOKNnZNhB2MJVYRxVNMi4JIB75csk2mGUgnG74ECVP_fvoHoTvf734nLuiYnbbdUHuc8V5oN_bPj2vIAWiTyUhR6sxGGEGC7v2HLAgfz8CTervxFMV02rRcSEAAHupdpZwiLqiQs4lE7MvyPXLcbu13ijEvkArFbo0W4oSqDy7Nksz7jHz-bnr2m2uNxu9F4lLvXL3rbYAoi4_LAuoccIj5gRoMJqhXuFZmip65UFnDo_9cTE9bN_KMmqgqzjR0jlmDFUQzBh_ESsuv3ERYa9q6Iiesm6ICIQ3oDgHCoHwDtd1O2IuqnUacvvTI39thpskVEM2A5UUvXjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛شهریار مغانلو مهاجم‌ملی‌پوش‌باشگاه اتحاد کلبا نیز از دو باشگاه تراکتور تبریز و پرسپولیس آفر هایی دریافت‌کرده و درپایان رقابت های جام جهانی پاسخ نهایی خود را به پیشنهادات خود خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23168" target="_blank">📅 10:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23167">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=VgCc_GXdzj-IjF7kLJx_RTced0-7kztpp6iUuvOZaco4xNjB0E99Z0zu9cld2O3z8yqNZHbaYKjcAc1KXdmpaJLG1VoCQJnu8iz0A4-uucX-jmdPFVXeq10XwryhvqXrYi7TfsSZ7UTpboBpr9i-r7kqdJwl_PF9_0zAfn3YmLbTp5DfsZBprDCAbh_Ll0czkqXtRt-iZuaT-GzJ0L5R6alax_IvSgZM57uUMx559tnoVGs7HRKfFtpcHMlmQpolV-_3d7z1uPstU85LVkhC0P6oYBpgOmCq5ALJZlotv2zRH2gajxSttoHOYiMS2C0WJrW250Es8LN3WcD0aPd-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=VgCc_GXdzj-IjF7kLJx_RTced0-7kztpp6iUuvOZaco4xNjB0E99Z0zu9cld2O3z8yqNZHbaYKjcAc1KXdmpaJLG1VoCQJnu8iz0A4-uucX-jmdPFVXeq10XwryhvqXrYi7TfsSZ7UTpboBpr9i-r7kqdJwl_PF9_0zAfn3YmLbTp5DfsZBprDCAbh_Ll0czkqXtRt-iZuaT-GzJ0L5R6alax_IvSgZM57uUMx559tnoVGs7HRKfFtpcHMlmQpolV-_3d7z1uPstU85LVkhC0P6oYBpgOmCq5ALJZlotv2zRH2gajxSttoHOYiMS2C0WJrW250Es8LN3WcD0aPd-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23167" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23166">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg7KRifC6pKOfT5SqgfVs4Oj5OBELfCklFchqgUazSz4apDzQtnaq24Yp_hW9qqH6SvaFGBjdTH3KEOTal1EHN3yD6QSgfn4Kq-0V6lt5plNB-0TT9Uatzq_2kXoOCug1PvWmXmxl3V_RUmQy2xMIk96ADeQYooHV7LhtOAd1I2Mw2BysES_BH-LPVyFWxDgVm_mp_EGRQ4U__fhw3upEXfZlHEpyWPbDH0a0PZQnaHXfvy1y_FYApwZdbDwOBUBZZPhJJu9TWD1XLG5njzHFO-2VHkfPCZXTbapADwqMeJzxl0_dYeuMPcFr3Nup9hqZqAVqqPKbFsnLm6bKnKO8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23166" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23165">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZC2ZbqT1vmTf8w9HwhD-AawxgY8c1lx87fQq7AIslxUopWR6K47r0hnLqfwS8MjnqN75EuHKjwTPuUzxjhy3zarAdrquTSjcl3VP-XH5znSw0Wbvav--zbH8WiX9zcYHmCL7Ab30r9CBTXumVDYiuZTbgLvLyOIC9prHoMlAn5A7Nt2O6YMc4nh7f-QUq0SN98ShDc9UJyq-U4bXE85Hth0wBUHfPheMC_sDGOv1_hFtnC0objT6Lwrz31AI3pFGTYKrmMf4BYp12buA4g5PY_RGjH0YZ4Y4GuqoZyVDkRxhOnJ12eTXN3jJqiSuQ_MbcCcctWZIFNlqivUAyv0bwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا er21
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23165" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23164">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKBlsF4PLIkHYZ7IDE-2miSNOgq_fMu1-zeUeVIE8X4H35EogbU4ZhxXUxnqq3SOfeJWTv1u04roFZ7STpcYWYzXh-gkxpQiLImdtg7zOfnQ-FTkp8umjHNS4Co4xfIv-k8aX9Ff5HWCqfWmM_FaF4B7hETGNKAte6UTpBB5GL8HKpl0WovV3eeEwQRz_DMD3efk7yXOObcaMI8hm6zwzNUzrklB1M4fCAS3N9S-KawarihOpw63gT2uHEVhx6T75UtuaTSVzxcJjKj1g44jO0QNjFVOJvvtwG9pLvUPKfVRAd6u2e_uflpUYHwykin-MxyXxzjKTrayFzsqJMI4L220" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKBlsF4PLIkHYZ7IDE-2miSNOgq_fMu1-zeUeVIE8X4H35EogbU4ZhxXUxnqq3SOfeJWTv1u04roFZ7STpcYWYzXh-gkxpQiLImdtg7zOfnQ-FTkp8umjHNS4Co4xfIv-k8aX9Ff5HWCqfWmM_FaF4B7hETGNKAte6UTpBB5GL8HKpl0WovV3eeEwQRz_DMD3efk7yXOObcaMI8hm6zwzNUzrklB1M4fCAS3N9S-KawarihOpw63gT2uHEVhx6T75UtuaTSVzxcJjKj1g44jO0QNjFVOJvvtwG9pLvUPKfVRAd6u2e_uflpUYHwykin-MxyXxzjKTrayFzsqJMI4L220" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجموعه‌ای از بهترین آهنگ‌های ادوار جام‌ جهانی از سال 1998 تا 2022؛ کدومشو دوست داشتید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/23164" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23163">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJEiBj2yF-RejoDEih52D4SFwnjPdAFEx7qbXMmuPQaqU1uFSYS3BVC7JH2TwcrfzlMSU1dUVAY8ui2BfI6MgBEJoMbygkWtxqn4hc0rW0336IAbMv2AEwsgOsHIt8VKguyky4Q-EFxbsRadlq267j0VLUS6G-m2FeJkWpNrGqQfOIGh1xyWeoRbl1XTAcDnZHSOv6RPsIhK-QY9CxKj2D4YpWeZ7XCXlFBDJPNhcV5-YgOxi5cMfg4bq1-Dhzbbdho6x0dT48g20IUgilCLR9RRzIlXOzcPo3imEWjmHDGxeS82S-lUD2IPtA_gutOsJyG8_DBGg7WDFfvJHt5mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/23163" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23162">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX_FykYT2c7ggN673H-mXYpF_Kq1kfWnA_9FmAkViWAJbhRP1r-ienkA3HZIyJtcYzqJhsq-_7KjMVRhQla2myLSDGwpDOASIAiNy7xDwi6OrKVhd91-qdUh2dnVGHvIAmp_s65PWYe19JJRXNmFU5FXFY3W6LFfBjz-9R-vHQVJVgeQHQFoS7m58xSfqXjS8xBCDyyGfefHw-TjoXnvWRw-3qAvJNnki3k_lRE3KysK0i9kbWV3iAoAMb5qAPe8B003VJlOLoAjGcTaGyqyoDb7bin1NCAPw-8oLYjKX5Se_3CZ6X0kqABmTy2GunjqX-_f1viodksDALEJXv2l6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23162" target="_blank">📅 09:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23161">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=Vz6OkOWUUxACzanHGV4my6x8sBiagyu_yE3aJg6_dH1LkjAAK_u0oyXR40py3bqN_Kwvif3r2hZSu9Vh3BSrcxLWGgPTYVJOgJ1MxQgpkEm4LpwOObRzgmaE3z8fP-w-xoQbUWzQRrIMgmSD5NWqvP7aHzhkr7YrvH8Q_kDKrWw5oU5vvt5upUSt-1SIktHg6eRqsk6lEouvDltMj2AMkaS4eD84cw5J4PQrlnYw84-Tt39WYMl_diHHT-1wYTWsV5SLv126WaNHmNdkPXLqpAzeAG4c4P61OxMhaK7mg1FcbsErqtklZpwiG_4oANpBDDiY_gSYvaz4NRyjyNhVoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=Vz6OkOWUUxACzanHGV4my6x8sBiagyu_yE3aJg6_dH1LkjAAK_u0oyXR40py3bqN_Kwvif3r2hZSu9Vh3BSrcxLWGgPTYVJOgJ1MxQgpkEm4LpwOObRzgmaE3z8fP-w-xoQbUWzQRrIMgmSD5NWqvP7aHzhkr7YrvH8Q_kDKrWw5oU5vvt5upUSt-1SIktHg6eRqsk6lEouvDltMj2AMkaS4eD84cw5J4PQrlnYw84-Tt39WYMl_diHHT-1wYTWsV5SLv126WaNHmNdkPXLqpAzeAG4c4P61OxMhaK7mg1FcbsErqtklZpwiG_4oANpBDDiY_gSYvaz4NRyjyNhVoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇺🇾
جالبه بدونید
؛ مینا بونینو، مجری سرشناس آرژانتینی، تنهااز‌طریق‌چت‌اینستاگرام با فده والورده ستاره رئال مادرید در ارتباط بود و قصد صمیمی‌ تر شدن نداشت؛ اما شنیدن یک پیام صوتی از فده همه‌ چیز را تغییر داد و او در جا عاشق لحن والورده شد.
‼️
درادامه مینا دراقدامی‌جنون‌آمیز و ریسکی شغل موفقش درتلویزیون را رهاکرد و بایک بلیط یک‌طرفه راهی مادریدشد تابرای‌اولین بار او را از نزدیک ببیند؛ تصمیمی بزرگ که‌سرآغاز یکی از وفادارترین و پایدار ترین زوج‌های حال حاضر دنیای فوتبال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/23161" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23160">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=YUbZOh0jal96NnGK-Nlhw9aMQSzF_oo-EMXrJg0AhzxuaG0swUSzWDiZ638Qc1Qj9Zu0p-4x3I1zuqEIWE10DE6LYUswDfub_D6BvKNYrlzEXwIL9f9QBW0dKtS2V7Tno6X30agXbwz-5TogyPhYmE1zLBUFq57TuVxyEblcOqkbMuqN-fg_nBFLqQYZOJhTfI5HDFKJORFmHAgoJwDBSPL-HV0N0kbJqIzHUK6LXoeNa85jvW51NfRMvDlIP2h_lBXQayuSVPahfBIENsK1w5AAJechOKJq4ohCT0hsqK3FT6xm7dnOBT_coT1AKzDQ58p2dOWBc4BZlUpMx08I3IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=YUbZOh0jal96NnGK-Nlhw9aMQSzF_oo-EMXrJg0AhzxuaG0swUSzWDiZ638Qc1Qj9Zu0p-4x3I1zuqEIWE10DE6LYUswDfub_D6BvKNYrlzEXwIL9f9QBW0dKtS2V7Tno6X30agXbwz-5TogyPhYmE1zLBUFq57TuVxyEblcOqkbMuqN-fg_nBFLqQYZOJhTfI5HDFKJORFmHAgoJwDBSPL-HV0N0kbJqIzHUK6LXoeNa85jvW51NfRMvDlIP2h_lBXQayuSVPahfBIENsK1w5AAJechOKJq4ohCT0hsqK3FT6xm7dnOBT_coT1AKzDQ58p2dOWBc4BZlUpMx08I3IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاگردان‌جوان‌روبرتوپیاتزا درحالیکه ست اول رو مقابل تیم پرقدرت‌برزیل فوق العاده شروع کردند اما درنهایت 25 بر 21 این ست رو واگذار کردند. پیاتزا درتیم امسال پوست اندازی بسیار زیادی انجام داده و بازیکنان جوان زیادی رو به تیمش اورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23160" target="_blank">📅 07:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23159">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=sm0g59WllkWzE11bXfF1sT-mkJi4zr4Lg6M2ZWTW2qJKgVnxd1YsqWqxZHA8TmkXYvURFV01rhwDMQPQJg9fkM-0XIEoM15LHQ3UlVSIqK9k1J4767j63MxSIZIUU2i4c5WbY2sD0NrwQ3-JuRSafmpXmyHn-pV5hmbOFss6_jO1DOX-MzTs2kodRLp7OnzveHhW_ZZUJ_Di1n8wf5QHzDRdmF7VK5O7YCuaxd-8SmkBKeRn0KkQGF0gERG37iH17ZfH_0U7yS7VXoaRdcaEnVG2n-f998MfCrvuZTYm_4pW0D2xjDa03UwPPoytA3MSty_5QlIyPxrcCZii_WAasQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=sm0g59WllkWzE11bXfF1sT-mkJi4zr4Lg6M2ZWTW2qJKgVnxd1YsqWqxZHA8TmkXYvURFV01rhwDMQPQJg9fkM-0XIEoM15LHQ3UlVSIqK9k1J4767j63MxSIZIUU2i4c5WbY2sD0NrwQ3-JuRSafmpXmyHn-pV5hmbOFss6_jO1DOX-MzTs2kodRLp7OnzveHhW_ZZUJ_Di1n8wf5QHzDRdmF7VK5O7YCuaxd-8SmkBKeRn0KkQGF0gERG37iH17ZfH_0U7yS7VXoaRdcaEnVG2n-f998MfCrvuZTYm_4pW0D2xjDa03UwPPoytA3MSty_5QlIyPxrcCZii_WAasQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏐
برنامه کامل مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23159" target="_blank">📅 03:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23157">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZw3_tvecXPkLd8XR_vdx32s_6_4yuFjwVwdRfWqpo18veG_N1e9zUCJ7fIzvudvWQNP28TyNbq1eULe02lSeLJBH4KOk6SVqyt5h0-aTS4ccrn61iAVqEsb_UQp77XSADJHvwMC3H4d27fO10SBM0PzlIWiLLe7k_eK5rPonVgQ1Da8CoJen2Aqyuiq5Nt16Pk-_GX3Kej4Qwyde_XiLPMZ7x3gV5bWjfrt4E2oxlytA2w0ogAb_DwkabBWaQ7aiqXpMTNZcmWq0zYogaP4gI_KxKZK6rZSVLBreTJGSmxmBbZ1ch2UuGyEw631JhjAbv2-NKZ8j2mJ6AJ0MAlPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23157" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23156">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgu-0i0HwcHnShBGk8o0SgOSl-kzkdDDhQkhVErQqObqVPPQiqvqs9ROzX7IzTUPxPbJVEi9rwEVeHqlaaUS5UEMtpYMj4G0zL9n9JT0SCCHNIP4zHeSf4RvskpscCczACYdoLn-UQTDtNWeCpgEKsDDcs5PvrrDYEodEZAu0r2HGn_HI_NTs1PAl8CYCcIkSUcQ8EI1z6goQ3wXw-kZ9qkOSwPdMeX6AOfkHtgwCaRHE3rmmUyOhMCy8dwD6JKiKumxjHB2t3CBpJyWTfL9rcruB8HF5jraoN8uMIiEfhj3mydMq6RYxsRVDVi94NxK6uhsuVjP_mqoRL0eeZgYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
برتری‌آرژانتین‌وپرتغال برابر ایسلند و نیجریه‌پیش‌ازشروع‌جام‌؛ انگلیس هم تاپایان نیمه اول با تک گل رایس از کاستاریکا پیش افتاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23156" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23155">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baVbN_CmjexC5WkOxI_g_Y-yE-Z-GjgFLRUM8kxe2__hU2UL5CtfCUJowLTHBNRG4ksGM3I2El6JWb6WvaXkipb1dGk__vLaupkrLzQoaa3j0qskF2UN4t7zg5fHJeUV2YweXiHgJA_UJB_-q8wlCLovAqrmZJpKem4XVI3ATgMINEHCwuJZrP7Jx4jEEk-LGZkIDYh9GCFQoKBZ73ftQhABXOE8SXDQF7pXahDRzYHHDRzL_qCUCl2FSzHgsjlPI50CQJ09ihQG0ipTr1wWoNZMduUUh2TgD1g6NWPU1X904So7XcdvVbyIv1PZ9Quj6jsjZYbgNJ4Mdcobe_F7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
— سنتکام آغاز حملات علیه ایران را که از ۲۰ دقیقه پیش آغاز شده است، اعلام کرد.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23155" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23154">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">▶️
هایلایتی‌ جدید و کامل از عملکرد نظمی‌ گریپشی فوق ستاره تیم‌ملی آلبانی که مدنظر سه باشگاه بزرگ پرسپولیس، استقلال و تراکتور قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23154" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23153">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsR-AhcVLU-ehwJFjlxZQzEqf-7uOuHwUI7d9QoO7YVm94nKtU57ZK4daul197-_rwxBJ2f_EWDWuln6RAYUEL0dCuOu5WOF4LPxsx4ZF7C7n_01K3Ka8cVVyOEMITj_SY0UqobeIuswZ3FlK5u2D4FaX3geRtQy7btbKL1C6TpnD9eFc4eOpG4m15uH_7Nv2khu58zs65PtIIntGrng7bQCYfNR946XyIjTMa4XKe69z3zwbvmxGpMeAlrPCz3urNMCkNN_L01nX9D47VR0qGVKympJQmLuDdegnxqAx9aQ_2RaYYySX16AaYb1YZ3zN14a5opMbpCUJ8Kg1JObzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23153" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23152">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=oQmwoe7mgXsFIeSG8B5DdbdPeGzGqkoI19PkZ6hrUb3laHppyNQUzTe1_oISsXV9b1oj-o7TF28G-Grefe8bNci-OIyTP7jQPxMIPyb3G5yegCqwyIy-oUXc5CFcc-xx63BotfbNEBloiCrRfhGfAtoD8LGrEKw1fOaI_GvNbhaaKvJHnzSpKZtNUk5sCfCpfTcg15BBx6qthlIHj-vmxqxD3ANxM-RgY4UbA2n1OL0izb836anqRaSH7bYrgMfzHKyj6v5sUUpk8g4XsnnCE3t6nCWgZ9MG4YXoGQ-GTiVFOvYbJzI6zHZacvut0eG_in6KeqUILsQtSA0sXj9mfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=oQmwoe7mgXsFIeSG8B5DdbdPeGzGqkoI19PkZ6hrUb3laHppyNQUzTe1_oISsXV9b1oj-o7TF28G-Grefe8bNci-OIyTP7jQPxMIPyb3G5yegCqwyIy-oUXc5CFcc-xx63BotfbNEBloiCrRfhGfAtoD8LGrEKw1fOaI_GvNbhaaKvJHnzSpKZtNUk5sCfCpfTcg15BBx6qthlIHj-vmxqxD3ANxM-RgY4UbA2n1OL0izb836anqRaSH7bYrgMfzHKyj6v5sUUpk8g4XsnnCE3t6nCWgZ9MG4YXoGQ-GTiVFOvYbJzI6zHZacvut0eG_in6KeqUILsQtSA0sXj9mfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23152" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvKhm9O4E0Tb0OyK2R2F7sD8XXuGYNauklt8ZSiCuaFgcMVPPb55qm1fkq4l6X2SM8MLKQOc4nGieluK437Er2fWhLl6e0-qJEwTzBV8YQt1C842J-wWBcfhFjhGSUSk7ki14487nsYdcu8BmE8nJXs3VJyRlYXP_9eDviwTHc0ut-4cKKhVUeiQZVBophLgfPI1tr4x6zwOCo6lxF06Vhps7BMi4yj3L-sY6b66ZNSwn-AeBONWUX4uCD9nVNznx8AlgZgtiVkmBt7Rbzfgy8Madf3yH-WxqPf6Y6kJdUdIhg7fRgI3UXcdT_wNXXLoQjN2ghYE2Ms1YkA9cvs76Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23150" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23148">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxsxLPmbpPWlPAL-xJPVwqSnzhcc2FWfUX2iywuUcTLPCCtkwZpoRoE62QJi9dVe9KpmfUPgvAON4--Zv1gcV5HHG-FlLOxBBxFocqwib5bji0d1tPHWSFT-9hr8uJotZK_vZCDstlvMZTfjkO1R4mB2mpEetpzCI6dac8WWfWTCDHL-QUFvrxqJJi0CsHsUVwaSGwlOABoEuNuj5PQX1ljqOoFsJNWnqRfswsel7eqdgxYhMkYuIgxTIro6jDAnA4IKuoykCjyyW7hloiVN-NgDfYow0c8Z5N_OpHH2GfKvTBWIUTUHOS1RPovBZZU4I7VxjH_hhasD70vWdX3nPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23148" target="_blank">📅 00:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=sFLLw64QUPHSIbw-i1bf45TRmK13afcXOQorNmDXtEzcdQSxEOQthYDkVlErPMCbbEDhELHHO5HAtYixZx8C3aDcm5VxBasHt99A6eOKn55JYlqk1fK2Q-uv0_NKCVi9IaN30jhZ8JWg8hM0NSLpfqTd-qLghSUnh_HcxSB2awnCDCD8Jo42ZpMGmSCcXgoMbJWlPNmBBcZyGp4MO0BsuSIRfBC3jy7sTWY3HUc-xsAGg6a-ApYU8F251DFlJs6xol8aS_JYNBI_5KihWyeFpxb3DggbKGr7WTvBN-mRV6Ruc1RvuXauvtX50NL4nPLFBs6A5VGM8vU1GfgnJjmGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=sFLLw64QUPHSIbw-i1bf45TRmK13afcXOQorNmDXtEzcdQSxEOQthYDkVlErPMCbbEDhELHHO5HAtYixZx8C3aDcm5VxBasHt99A6eOKn55JYlqk1fK2Q-uv0_NKCVi9IaN30jhZ8JWg8hM0NSLpfqTd-qLghSUnh_HcxSB2awnCDCD8Jo42ZpMGmSCcXgoMbJWlPNmBBcZyGp4MO0BsuSIRfBC3jy7sTWY3HUc-xsAGg6a-ApYU8F251DFlJs6xol8aS_JYNBI_5KihWyeFpxb3DggbKGr7WTvBN-mRV6Ruc1RvuXauvtX50NL4nPLFBs6A5VGM8vU1GfgnJjmGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
از پیت‌هگست وزیرجنگ‌آمریکا:
سنتکام امشب درگیره چون پرزیدنت ترامپ گفت ما امشب ایران را بسختی خواهیم زد و این کار را می‌کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23147" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23146">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDGNjWOmDlIlRLpFG4bYaBtWODNtajbhPY8Dy3Ul9Os9NboJbRs4u09c4BoiSuo8gaUeTX2kPEpGEvUs5Zb27FM_IxxI0J_70PjIQQZ1x6ARqTNdZ5t7-NQhIWRce6NCoBszhHroOdcNymNxcJ370MQWhJvjdyoYWdYwMOo5GhpccQMKk6o9-Fydo4LFqwQ46l0ZGj7qG-ROY42E6sUaC2vqxfozfw0xpAcKitU_3apIBUgcnqak7qaqzPNmT4Vd3ttShMZbAho7ifthiMjVgXOkq7A15DfErWt9Yj2nhZQZ5EslH--g_z1hGwI3JIJl2hoRNlzVVENKi07iJp7NRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23146" target="_blank">📅 00:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23145">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldtR-rxZWtS9859FizStglFHqf2MTKVXP_kJQDcuKq-TlcFJjjRXBYpJfbp-Dl9AhoCcZjOXhDZn8P4B0ujcYuOfNCjnbLoGyTJxTCGLi8eWnEhMz_opVKKMzO60xkhaGNy38LKkl41tKlTownOpKvT5FPVDNp30_WTbjKAj-rfJsIdf919XrNVN5lL27Eh6jYZke6BPHsvHFk_KpPWW66ct7P-2dEh0GuuF35TxTZxyfUlTsdujaoriguIXgdjNXbIHTexJD1olbijyPShEpmTSm_QjWB2SHkyliL8S_CSJQ9WhByWjpRX0OadjwQcUbml7ISXT_DECuAtyzuL8_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23145" target="_blank">📅 23:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23144">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2m0g4Gq0ImfnwjMwZcKV0Da4-hpVi11N4zfP9K7usGSajt5YYreX1TWMmE9pHH2MDm9ZYdo-w9IvPktuUg6O0HM8bDu_XdPM2Elu8px0gv-tgQ2s9DTcZaGEyVIQmi3i4Lmp3j9On71JG318g0r9VSyazxR5g5cZfSbipysy63VIvSSoz7n4L--iQQG6RbzKzicVquTO4xL851k5ySZcGFHrIh_yD2wkZZ00cAluxjgV9oT6KHr094uO9MzmkQ0IAPYrvugcrIdjvf1ZdNttUJzljXrehcEr9AW0XmkGe0r06V9hrginPeaGGTsYRsnaHthN_TgYom6VY5uIFGHuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23144" target="_blank">📅 23:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23143">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGchA7XeebKydXuo0O6lbJpKguc6aruXDcN5LcDBhJQLFj8OUhg3z2uLXihAaj1X9k6sCw0fjtSIx9fRiGvMPg4oYxcG3tG-rBEH-3CI_l6pkb1Ms5K0fL2psxEpCeCMTu4zOPeKJf8EgXDAdu4OC2lMXy9QigStLQpA2SX5n6ClNiQGUi7J-2mEET-dd9AON4rgJq-7DwE0bEeRTRbV3GV_cyaBsWJHxXsXDAcGyDDlLCnbaY10Ev-cXlsfi0iIUfQ_3MXoYOE8ekZgpXbU8n6hbyRwXPJffwTcuztlioAOLxIECNidcm3M-DKF9Ca0kmqZjjQlP0w3q1MLhLPsLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23143" target="_blank">📅 23:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23142">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4aYyAa8E-mSBEpfXiwrG4pdMwE-9E6jFYPJ1LLoPXvmb9kE9vRJsxM6FQc3d-szYZuF4o_LD4nRGB5iBl7P5ehCx2Y3hjJ800Ej1PN5VbGTia_ULA9Rf-YLhN9xadIspkJ05HjA1McKF8bR94HkvL8s3t1e7Z6oZymV3pRadqQ6fmEhp0_HZyurg3ZE7wxGMedzbXStxwuUVJKJqDcchSptXRCf-LJmDZXNcVLFmgaYwaMcDxMFf9emCh8m1IUYvhGmfSU6WaEsB4QO3FuWJL_G9jgzlMAhbV-mwjURNkOYTwfe4sBlTjzOX-zAihdTv32_YYgEzWkQi0l4-uw9Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23142" target="_blank">📅 23:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23141">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p3TtLnU9c1xQGA6vTYgsQMIL4vPL-YS9SQ3LLjKbABDlKXWFK8031KUHAwifmO7MraTO5mdxRtB2HD4SJscezBlsKuHN-_eYdxXilTP5yPfsqEjakLbJUTInz1f4UFPMeJWgkVlIVeIXZDwvfKPjR6ifCGMaMMtt9KObAe4pCAiq01G5A-0HlsQVgpWAccj78mOOTZM45BJ3qj4svtN0nGVaed_paDi--lNrqwe3dEoJkya5JofpgBrMIc5e0VBk9DmQIqWM_NUls1m8txXvPlmspeowxVd0gV6jyI7Baiv-cIE38FaHqYrmWsu-qdagXEfxMwlEATB4I-Ag8DYHdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ متاسفانه اموال و حساب‌های بانکی و خط موبایل وریا غفوری توقیف و مصادره گردید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23141" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=uE3FOn04ctCKNe2G_-LAkFAXtjHiwu6-hBgeWx6aygyQaUX9NcAd3KvMCcMnY09nqcyXDJa3R7KTn4T-x0VtUHernejOVYFirFX_ycgfmbwlsEgO9KeoFrVN_WpFuMZNwxzE4ESl5WIk3Sf0gSP4sK5iYKEJY9u6KMCZ1XViMSwMi0qBqUSJ9q06CKJG1PLkbgdQpO74pzhj1Gp-qMdFSj9jmv3oc6dAYnBi5x3Q55E6Xib3qE8LoIxHZ_uUmdgZzSqPMuBvjbAeBVFkfIgQkv3s9ijPILgyno6ATWUpe4X-JCiaNlXmHXZWrRklHSc3T5i7XSxQ3NC84To8JmbDxRS1DOBNpUArKoax7KoT8F2H9tJsJ082Ld48DozVhzkqd662Tz0XWKW1EDbwIcbs7h3g9caNd1vcvEdUBgeykvp_Nztb71iGisy9kPzMES3GvD7RuhxFM3OhO51tgS1b_PqYQXco19zmV4J1rxb4gqO9XkEXBjUq3jPL1E1n8OdAxJf7fehIHnuhLXuIzeR992BFD_lhiHkGD29cbtZYM5AvoHffNija1MwCa96C-nlJ3d60EUhzFuiD2_M1lzco923SeOwfdSvZNi9Hel_Gy-Z_uhfMlla1wAOpVMhQ-KrdhBChmbOHJDI9k2ljJ4LRJOLN8STlsAwZqsFgxjbmCAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=uE3FOn04ctCKNe2G_-LAkFAXtjHiwu6-hBgeWx6aygyQaUX9NcAd3KvMCcMnY09nqcyXDJa3R7KTn4T-x0VtUHernejOVYFirFX_ycgfmbwlsEgO9KeoFrVN_WpFuMZNwxzE4ESl5WIk3Sf0gSP4sK5iYKEJY9u6KMCZ1XViMSwMi0qBqUSJ9q06CKJG1PLkbgdQpO74pzhj1Gp-qMdFSj9jmv3oc6dAYnBi5x3Q55E6Xib3qE8LoIxHZ_uUmdgZzSqPMuBvjbAeBVFkfIgQkv3s9ijPILgyno6ATWUpe4X-JCiaNlXmHXZWrRklHSc3T5i7XSxQ3NC84To8JmbDxRS1DOBNpUArKoax7KoT8F2H9tJsJ082Ld48DozVhzkqd662Tz0XWKW1EDbwIcbs7h3g9caNd1vcvEdUBgeykvp_Nztb71iGisy9kPzMES3GvD7RuhxFM3OhO51tgS1b_PqYQXco19zmV4J1rxb4gqO9XkEXBjUq3jPL1E1n8OdAxJf7fehIHnuhLXuIzeR992BFD_lhiHkGD29cbtZYM5AvoHffNija1MwCa96C-nlJ3d60EUhzFuiD2_M1lzco923SeOwfdSvZNi9Hel_Gy-Z_uhfMlla1wAOpVMhQ-KrdhBChmbOHJDI9k2ljJ4LRJOLN8STlsAwZqsFgxjbmCAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23140" target="_blank">📅 22:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba85793af.mp4?token=fXGkrod9BFD_ZX1E3v6YOP6fZAe-neUm1JKiC1W3dUWMEgphyCcm4zU09d-c7d8uf4rSC-sg53EYHJ55w-Kgr7B5FbWGEjpbyNpClpXtPV-U38zDklmjQ79gfLef6S22G8NW-eyBDT6gCxw6MUI-u_A29YRRPpL0_qoUSnx8-EjA3ek73itxo-WQ8nkhJ8N41wq2QrwXekj0wDgyrSLtE4ISTxazkmtIwRnuknsHH-76cfsqju7FpSgJwGbXDV6L7q5nEOLFokqnN5mpHDn8g2R-EuyASfak02g1UzzESaZAw0R8Pgvcf5PfEotPHUOsFjjeU5jojpHU_3pTbvGUvmpQmXdkM3MxJ4MC8oK5G4MpuHGxsS4Uz8SrVA1hszgnZYZRV766VHNT15RPhdrC15iC2GjAApZ6uHV34V7PdFl9Bvq_BjyAvy-p5YdOksk-V15K5C3qX9_iuoSNauri0dhxlfumpy4_PxkoeAHhKkttgwluFevjH73H3F-3Ilo9QHGgIcVAFbIqbHJe-nE-McO0GVxELhM2A1BqhuIIm_I4HWG_w_WfqmM9jCtMtJsF33yWl_wlSpgJSezW4mB5mxo-71LmoY5ar1bzMR3wXoXfdawv9QO36EeGtPRGt1kwBnuhbQY56CXAqdPLEFdUBM2sVk8vqkOcCRYiks_psz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba85793af.mp4?token=fXGkrod9BFD_ZX1E3v6YOP6fZAe-neUm1JKiC1W3dUWMEgphyCcm4zU09d-c7d8uf4rSC-sg53EYHJ55w-Kgr7B5FbWGEjpbyNpClpXtPV-U38zDklmjQ79gfLef6S22G8NW-eyBDT6gCxw6MUI-u_A29YRRPpL0_qoUSnx8-EjA3ek73itxo-WQ8nkhJ8N41wq2QrwXekj0wDgyrSLtE4ISTxazkmtIwRnuknsHH-76cfsqju7FpSgJwGbXDV6L7q5nEOLFokqnN5mpHDn8g2R-EuyASfak02g1UzzESaZAw0R8Pgvcf5PfEotPHUOsFjjeU5jojpHU_3pTbvGUvmpQmXdkM3MxJ4MC8oK5G4MpuHGxsS4Uz8SrVA1hszgnZYZRV766VHNT15RPhdrC15iC2GjAApZ6uHV34V7PdFl9Bvq_BjyAvy-p5YdOksk-V15K5C3qX9_iuoSNauri0dhxlfumpy4_PxkoeAHhKkttgwluFevjH73H3F-3Ilo9QHGgIcVAFbIqbHJe-nE-McO0GVxELhM2A1BqhuIIm_I4HWG_w_WfqmM9jCtMtJsF33yWl_wlSpgJSezW4mB5mxo-71LmoY5ar1bzMR3wXoXfdawv9QO36EeGtPRGt1kwBnuhbQY56CXAqdPLEFdUBM2sVk8vqkOcCRYiks_psz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23139" target="_blank">📅 22:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqwldO_6mwZX9G_-OntL497KIgJGSbwjRtRs_CxTUkLCdHS6lfWlRIcnjlZsEOYfdz_b0HWYThp9SV0kvozwxJNEEf80cnNDg2RZ-mbGxLJb6RZINFrpnuHwwz6Iw0Xk4y2V3QOx5bMhnaHvlt0HZVsNe79LXCRF0YCjqiS_edLhdsECqNhCI441PDpaEWE0F6S22Z4Nadml6ShF7w2wArYx4nmvWub7nj9tb8WvCxgbodbbWQeXy7b2iot7Bv9ECQu3D-s0vKgaHetbsgxx46tchczHe1nsbZ_TFmkHfwx3DEKeT3bTog4roy-S-yYnfVEYLlAG3AQYu9qmXQwCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ دیگر مجری ویژه مسابقات جام جهانی شبکه TRT SPOR؛ از هرجانگاه‌میکنید بکنید فقط از صداوسیما باحضوراون‌دومجری عنتر نبینید. از شبکه های خارجی‌ببینید از هر نظر واقعا فوق العاده هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23138" target="_blank">📅 22:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23137">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KGKFeLmsL1Aia5kTr6MOumjD9saLfpHZc_rxbqKTWEZh_J_mAbyq9eOYM9E06c9en_5kIsD_-__mZRChfne0xu-L8749z2aGBKQ5w30UyaDbTRbG0FGUbizduiY7b4jsRyuQbYw5i6IEzsrPQpjs9EcJDM-Uji6qX9mzsD1Ui-soGnan3rLwlAd4lNQ9oxWTb_ORLgwr3XW6tI3G7WkV-oAu-2ZQKQNLwaZmzhmJNQ4RSZZLLW3Ag1p7PEcGU9Bs6rz_6r9ai3SIj_l7lrkgxnyK2EJDBPH4Z0a-JOKR3mENYwxTNwD1q-j38vE3EEt6RTT9Stw83EicbwmGAGJ6IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23137" target="_blank">📅 21:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23136">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwoFUn9cThOSSO2p1sH7xKEPE6yn9qD2qum_4cDSwfvoGDIEdz85Q7N5k_v41Nj9ftyMEZUJodQ6PBKZjXh3tjTKvauitw5dZtc13TKB5SjihaILQ8vu7gbCkJRm9f31Jy3ilV4DBE3REPeW2cqnuJ4zsOKaIpQtsTEEwvpZSQ8s56ae4UGAiqN9NDcjsRFY05B9WWhDN93fyS1ofoam4iiC7xk4umKJp8LnH0WBJHdW61kXOY7XEpXVLNbew11LSqUBIidktIpwVdPnadq4EcL9pHyDNWzhuiz4Kn5hNu0Ebb9WT8DOFbpi5pKccKS_B-4EdWb8d5rjgsp_LsiepQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌اشتباه درطراحی نیست؛
پرچم لهستان روی پیراهن هائیتی؛درسال ۱۸۰۲ ناپلئون سربازان لهستانی رابرای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه‌ استقلال این کشور جنگیدند. پس‌از استقلال هائیتی در ۱۸۰۴ ژان ژاک‌دسالین به لهستانی‌ها تابعیت اعطا کرد. اکنون و بیش‌از ۲۰۰ سال بعد هائیتی با قرار دادن پرچم‌لهستان‌روی‌پیراهنش در جام جهانی ۲۰۲۶، یاد این دوستی تاریخی را زنده نگه می‌دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23136" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23135">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G69f66-BWWBAKqu139C7Z-0h9HSDFPmahsFsJ2sIXJm8Q2OEhUYfDbMNzNCPEvF_wUCprP8I2DC6SDtYPsRJias4Qf3mNq3ensXwB0I6Q5PD57xpH4DI9T1-N_S5P_lHr87EqUvY8R_gRrRGywzjykMpJXp4kaLxokX97Sq8RpSInzr6ZojhnCf9j-2r06mE4lmy6NDzCBbmTtbkC2Pr-OhWo6WTWOX8sKJq7hhr65vnnYqOW4AkNUQ4fACbKrIF7QeWX6qbCLgB4vS0OGlz8RymdDaGgah_Uvh_GF70IrpPn7gL-hh7E6BszwKXPOnyh9I8N7vNzkpOiRxakBSK2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23135" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23134">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYRGdk2Dg3a63up9buQSsvr9rFe0ZtkQOg7UTiayxMM1zeS62nb_hIjW4mPVZfn4W791ZZwXP3HBawCV8XZy33FQMgDbMrDNb307hj0oJ6Lxtp24w78jhwLqzIWFq7jSaod8KUyB9iRszBh3ykZwwjJbp5KUvPM-NqN4PSuFjkt4zvOjD70un-CPVpSxLeiRxAUp2C_8PCDYEp90-a1jbxOEF7I4RZD02M2olYKctb-03iq-SHZUu92rWMAfCdNq7qXzoimHK7ciwiHZFon2l6w4NgZ_rp3Y-N09RlHAUAPVieDy3xv_sbxGND4CuSYXKTk5olEbq7uQiSb05MWfDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23134" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23133">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfQ_tYwMViVhLEnJcaFpzWPkAocNPuNNcmifDR-E2ejeqNMQarjLolA84Esp3Hf97MPIpWkMgdwF5eSgb1BpLN3UbXaxnKaexHSL_KoLrUKUpMB0lhN-DQvgn9XlCeEiJK5IIeVqfRqnCYez_JTsxOZILqaybM4HisR6c24j77ZVngdoBVGO3M_jEYhWly8yU0jKHhRTHF8TPmqoHVtS8t_hG84guRpo6JnzvR_WKFGlHOKdsly2Rj6e5A9DrVLpY6duYztjeztzQ6GQ-IfvterBvK4BzSpcLwwjJZRxDITDlwtwSvnTyawrIrCB9EpkzgaT9AhcxVj8m48_tzUB8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23133" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23131">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G7O3Oflfn6mjNFgxNaJBLtF4u0LJPiCUUf0TnteTscPjkOQYvKBPSsNn8ewGDDyASgrvAF_4eCiI3SpTmbbA_MOP4zXH-Eh5sUPyjJVmd7_ssukBzkWXtVya0qBpN0U6VqmTqQdAtCrPppitqFvOIvTgomkCBSy9VWpIFW3lOrJB6SGB90gcSALnxbUwn6cPDsJ-HAHaY6O1zGX4sS-DG_oPD3p2Tw9g0LMsckrkLM0IZoz7-8-9-KWzbHdk8VUhlcggTU_LBIdLdFZrQgWLBTxQSp6iQ4FnXVqsDdDXUuJQRBMwc3u3O9FteC0wp1OcDCEHubfAO6706UkV5b-QUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ECzsjbGpRO3yCeIzaTqDaj7ODmEbBa4CGeU5XExuoEitdtB6xxx8v-UDqPDNW4XG9RuNK324L7LQP72HWXa3PZze0P4M1c-EOFAMwyI8rIu4o4X4-gb38hVh89l5jgudjo-54EFhyQOl0FrHTcAi0kXViOz_YvqDRXQUSaPpY05Mjr7g8R0y_ys2xELAptidYGDJWU9LAR9lwPOhGOpX_iinmvx30o7MKiEaz__c8srgBM1iEp_CgP8lSo_Ix_SkCHint4ngQEieuLPF9RTPCsAFRB-qMy64Gl4Q0LTGws9d-bZH5wiO0pogdjoau1_QN-cjbexYyyDjObkAYg35PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرخوش: تولد و بقای پنج توله یوزپلنگ در پناهگاه میاندشت‌. ‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت خراسان شمالی، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23131" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23130">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=FxDaY3j3IjRJpbUalrxZd1CgUOs2A1z3EXkkys8ve9JF-jJR4sRuaPouss3QUsyixq_8sNa6Y3cQHEMl7Mhu_E0bsYDgmAMaK_21XBeJYwQFiLh7wQyNY5Ht9qFwBHmYUGwcl6ZjhWPOe2gCztdZuxELOGJ_b9NYQNm_nqMNw0WKBxbrfa5tMYobNqtMpR67NK8recWjR-jKCvTT-0GPomRNMLTQRjTnItFhNAZSUvBdFZqL1dXJSq6R1v8tS1tXoGsYRvuiTE4PK8OjdQ2EJTJSPOae5lx6t0udFr93qAMplPFBXPAR7Ec6XXnhdB9fdEa5n8ZeSMRp23MFUiJAlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=FxDaY3j3IjRJpbUalrxZd1CgUOs2A1z3EXkkys8ve9JF-jJR4sRuaPouss3QUsyixq_8sNa6Y3cQHEMl7Mhu_E0bsYDgmAMaK_21XBeJYwQFiLh7wQyNY5Ht9qFwBHmYUGwcl6ZjhWPOe2gCztdZuxELOGJ_b9NYQNm_nqMNw0WKBxbrfa5tMYobNqtMpR67NK8recWjR-jKCvTT-0GPomRNMLTQRjTnItFhNAZSUvBdFZqL1dXJSq6R1v8tS1tXoGsYRvuiTE4PK8OjdQ2EJTJSPOae5lx6t0udFr93qAMplPFBXPAR7Ec6XXnhdB9fdEa5n8ZeSMRp23MFUiJAlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇷
حس و حالی که از آهنگ‌های تیم قلعه‌نویی و بازیکنان منتبخش و تیم ملی آرژانتین میگیرم:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23130" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23128">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTvTIy0ksvJ-QUTV7AqbKEvZ8JzUzU-t9By73GRRHe4fYC6Eibz3UjrXxEt0dl2mGdHVRVq1jaMjKKQ_o-pj1O-hADMylz7YDIzC2kjyVkFkDR7aSaAzzepB41FpWKuhYtDLgbdY8NSG2NKQriufcnJvMhg8ToYud2eTPvJCOwI-NAiu1BneQrhNraK0_CO83uOGdG_DzuFyppLQvEQXl5zT2tMuKpE-QarqvOXU5IxHEmKyyU02EMCSC5pg68EuA_FbDa96jxlF_p1LtKgFQKfCWro7OgtPr6iz7-A4WDuEmLZieeoXj6z1wsv-zpJ6g9kWIgjtCt7G6QVQ6y4HHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23128" target="_blank">📅 19:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23127">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EF2pp3NSuzHyAVr26unOt8rHUxFBHbQOXo7V0YJu2AcX2WZQOULWfphGsgZttZ9wcYWDIdQWRAjCGvhXePCn-jFv8Tny3KfY5d9m8nFN4SRFWSo7HmdGVvRJrepvy984W_D6BlIJmVCDGmMiDPEolVG8R9q1Rjl95Doj6uWZqPTGfqjQJWG8ODaYedJVHBnaQgpejaLaTvffRS6F2kXdd7wrbICbZLneYqeuVUVsynBYEtk5278_T9d4iCl9Vhcooc3nKQR4dm1d1EvewlGx1B64jHJSqtlIUoj-1phfLXzPaHdh_lCnTxE7pd1Sb8_meEvANTQ_UmXPggMbfqMFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23127" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23126">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTsyIXDA8do_Xhw7r351BvFwBcG4W2tCJ8evy5fzkjCEpGdR45RTSQfIgF2J-fkHCnkCL7W1NAV9HgyyE-d-7H3ex5TOMJdGmlxF88HDPFlTMJqqcx09tn-crAd6LLWQKuGWOoLTWzCdn1UXECVCOFepu1_hbfMghie4Q0p5aAHkboDdB0U_rzMz5EYCgtk-XhkQ7qcu-I-SjJhTJRb-eiIyPvF4-cXwusyOtUHNlpjD7mPinmrqipd9jjLnQe3DfTDO-9Qy82dI5yjyihlg3Yh3iI256ARAwLoVgyDKG-RyQnACfdn6VzJUoAtOrV3BB-bAzfoHEUVwkktkzkoW4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23126" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23124">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/urust2tsyO7JM7XdP9Y2ctvbtfwh1steDJ4-4qCUDefTN7e6B1Pc4BB7cYkv7eDcV3X9g9MAoS_JEilQaWT9ryXLMm0JDIU0QakjtI4Rkuw0IBqQX-6sWbPfo1U-jXpSp5zUC2Jk6HbLNNiXFfum3J-YcwVaPUtIEfWa5jbhX18-kgQ-jc5p6T3vNcqCZcgECF-vOuJwYK8dWHYhAHaM-Gun6eorjjG4eEE0DeOMg06UVsEPSS7utvkvDB0LABIP0-dJdH8YA48zdKKIDqMZp_ZbJ3rfAwYMs_-1EJuaCPQZzLCzTyYNTBlz47xdYlUY-bTKb_xX3G2wjjz9cqaZwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rAjU-bF2JocRwscCLi8lgKOREUAKG9lylCHRBVGkvsRFQfbWrmAxx2uNMmtGfqvQu3gXCGoJe606OfwNm5BEeK8EJssHIdnLEAttamQEHAVFNiSRatkyopGPIKOugE4AhlaEpRyIwNHGnOwctrVSUj5WDP3iRR2G4UY25ELyPrJWgfdBjrSHV5F5dYO9tV63-Mj1amOEBqJt3K_rPdxFMnTv1iF3rLq3aBM_ymiblmPtyVeR3thsuxgfVR1WF0fjlW1RWUGS2TYduPecR7hJezg9lH6t1AvJsUOqyIGTudzjSyz_hLLG-E8EcMxuWbHcOadUfAjj4X0QUBmdvORstQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23124" target="_blank">📅 16:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23123">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ja2eKu2jBnHcM-TObWM8OgqfmY5JihdrYe-pbrnBS421vWyEpm7MDzMLVSmSX9Ysh557o4Jpp2Dn8j3nRv64L5TS1MhYCWqFPlzsiTpBDoHPJh85E0gFFF2Ba5V29SckL64BkY2Y_R7sSQyjhnBUujPy4K4pOf8neTeaBiqKSKPVx4bQkyVhGWgI8lBhldvQRSNbuKyAIC2ngcXosYtMgUYvFXzXpLS2pyRb0RS1GyLbHA4cUvpdxQRD-Rju4lt8LrE7f_a_g9fbdy7Xei5qh0tHiF230N0GPnhOPSgqiX-5mpF4nuQTvp0Oo6oC8UT-0C2qAW07ctSLJzjiLlH-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23123" target="_blank">📅 16:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23122">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میراث‌ترسناک‌ضدحمله‌های منچستر که بعد از یه توپ‌گیری آغاز میشه بامربیگری کریک پس از سال‌ها که توسط سر الکس فرگوسن اجرا میشد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23122" target="_blank">📅 16:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23120">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DHA550m1xILcPNF6X-LTnom2aiRYHgq_gXLYPmfx2WGCx5M-pKKSlQtGe5f98YsYx8OXuKSK8YkOJrOCSDF3rf-GDmOyagTn5ZCxND6jVMNQDfXBS1g7OSlbSgkeX-1FAN2b79OUSzOGFTpiZGMLwAB1NQNQYtGn11c5qvkHtUbuSJV_ouF9TaaT1zJGIrx9ww9GrSti9Xtj2gokv7b2ZohmnfYtaq0zewhulGdBw3LExfMWKfZ0KwOqdqBwpSK59s2XPtAqYhi3YyuzI2dKku-ZcTW2IK_u84KpvkKD781DWm_1F6BE_y7IaLg72eXhr6mQU4SXNP0pDmkf3z5DpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eAxgiaS802fsOEOxifZd1dhY17YXYns75WqFDz6YvH46b82D1mI7a90YXVQicPqA4X8ua1M5X3w6_NLYc94lNtezzTwaNnBm1roUt7oLeEJiHQU5YO_wB3nBsLrEmLAx_2NHCUgAPWDMkM-jhdUSauVJLd0tGk2QuxG_-sGOKP_mnohtkOIGzX9MPSmZKEww7F8GQcHprF_uLNAmNb6hAHZnU1gXdfzh-eqzy-CukBF3Yv6xe4rUKYZNlOR4VnFEvLZpl_to-2FVU4xvjR9TckoheYMwVMZf5C3nbzIYWPXvkXufN53fW-tri3S0-vFKRJwiIrqmMCrlabOvICWNyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23120" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23119">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXViAiPvDeqmnpnPB8ofwQ-myzXoHJNGxj41dfNNLL_cL4HkUQhi4BL7RwDqsjmSyctUJFK3a_Om0k1yUtc_BQlmcBjTdfCr7Xy_68nDknjzKwLKXG12VSLnyFz1pQExFKbn5B4byvjXjsFgaxoHKmswQmRVJBwO6i5A8Pnr_QnD9D_lw_67FBsee9YVR3qL94RYyJhvMzzTRppt7prkflFcuqjaSdU9NGKASsVFWfKVnvJ4kv_rU-fWu3864tLzRNmWmJGstQkge9Cf6GagMGjSerdjs37Q5d5K0czYbF3lidkRBwj-qob-5nqT4V_ZlN4JvFdSXM3IrJ_COoFPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23119" target="_blank">📅 15:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23118">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ifMWO-z0uT9YKdva-uj7F13_uto-fzoTIgXv_BULYYnoMWQmEioVSnySk9p_p-iuZd9FhfRJBGrR0atychrLmWGx3TjjJJbkOu1DZiNqLHH87ZtxqwXQthmTwNVbO13D48CQXBHSx1JVjM-oWX3q-1ZVIIfArV33cVwre0j643dvU53kpvZ-lLL6v5CaVyYF8cQp10yRDG1s3z6W8q3OfmxnbgFJVunncEmrsw0npjLHdReWStPQq-pHJravPaHdKqxm0t9vD-PFpE79pc9essCDAENACKOpNcZejB-bN9sksirdHBUxE0XTv40EPCWUNF4KOBaBVSEWnptcbhjlkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
شهربرلین‌آلمان تازگی‌ها یه مکان برای شنا زده که خانوم‌ها در اون مکان حق پوشیدن سوتین ندارند! همونطوری که مردا سینه هاشون پیداست خانوما هم مجبورند بدون سوتین وارد اونجا بشن و شنا کنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23118" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23117">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFUKu4fhvmBFy9mXrtLFuzPwB6yLpRm45sCMDLH1TvQoRCzF7TMAjTNnG3G161dqLBBYl84zaNpgufFOmxO0bDMqVr17lM60n4u1IKDPVJDxnLMiyKsGLwwTe3RLOsioSvJC2vhqMpEhXBe41Cdw00qMxruKmInt53QfRUxF6t5MJe1UBGNIndjqje1OCpB-hpyC84zumwLDck8-cjVj2Xk_OvQ_h5rsiVnIPeGqUW8bcaQJMzu5Is45qnsz2sAJQnn5VeelnrpOwy2Qi30rCe_YKwWGszQEvruYyBDuNU-BIoOViMv0G8HUkW1IrAX5U6wm2drRpykMoTE9BI3rCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23117" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23116">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kyz3duvgJCXBtcEKV7uCcE07V_92Ag5-ifnYnG1RPOuFWpaOVDaMyfXtEeXM2U3TOd-vBFymxgldcY4P1Ta1bL2BNPSR4kIdlcsV5avKGr0adSZHrazBuCQfLkLLTSTFurALZGE1CMGXFos0xeDN4jpnPnQk1CC98mmV0NGo3EW47Wt9hAQQ8GH8a0isp1-vl6_xNloqWtjy26yd94k5T7QTtqez5G3tCutQ27XTB2bkmI8MnR7OJ0b4AWnS07nZht_ocm6NSLL9Ybl3QH5AyL4t14iDuO31EJFWUab8UL3CMSznUpG5_4dR_FwLQpmvV68YtMKAFT38e5-7afLg6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23116" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEXXXmdCBajlrttHWc8f_kg8TpyDFuQs0yf10FcxdN1n1HUqnsnei969jnd5jDlCdqXTfYocApp2eCnmaOvFWdqbiWH3lTNdEInVrVOjbTkbIPqa8OFhe__yBN-k-pzB8xYNE141lcjH5P7h8V8Jyll9PGv8m6fXJUsT_4DR2O5wAInQ7ftZebnym30RTQKfpXkhDDKApURdc7nTXAjwTUTVNls5BBsHkohTgI47fe0CgY5aJyu6L35x88V_LT2J2zNrKCcwWC5F9ok_kpkniZRXLe0do2mGpI7FahUrbdGsAdKpLJUMDesMal2UbbLLgtwSveIu5YOnhKYCeqO2-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23115" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUlv2NkSlVEZHkuTqYP548LcDSm6DPiTk0p7AJhCjpxZlVWeDNiuaiQgMzuzQIPiKMT2GXpR4SrEwIHUChcK-zUCkuNRacQr0q3eirZYzz9M81g5cnMXMbzolCc54PfI47zUGfR6EHsuLzTKfl64GC5HVx-W90xcsnLuk6pqxhp77aVEQnVuLYCVz7PFWpTmNZm1c2Pur0_kmczXLY_csaaszA15STKGao8X8duulq832usW9dBRXpAVvIENq9BQ3UgF1g2aNEFDRcXXifEMMc-0EBC2WcfMGwB0Mc3JcSBUwIw1JyNgt3o-OE_HKM_nuniqSqV1b7QAwRQhqGZRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23114" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=dTsgWDIWy8F89h26BdXe0URK3D8CtYH9y4sFzFaYO2VUCN-hTvFbuuRK9gj9Kg6rVwGu7KkyUkFvyIjemcdHuBF5loWrRzUywooV5712lfdYElapssr4FMFTqdED0ZJZlzXCemvoxBdtQI1ZzRNIGW3v1S29_0_N80Ncoa0nnVc4pCvswNCfY7PcIANbEY0bPPYRMrNtDh0Y22Oj0nED8HVoF62D7P1Ds5i62nNN81zsTpcx7Q6RmZp9tPVP97WqNxjaODrlbTgfzw37rY0mBK8sr6UvHfCj6R5BHleu6sDaZzg1PJDg46-X5ymeFvvNeUnvE2i3WlSXyo4P8GL98IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=dTsgWDIWy8F89h26BdXe0URK3D8CtYH9y4sFzFaYO2VUCN-hTvFbuuRK9gj9Kg6rVwGu7KkyUkFvyIjemcdHuBF5loWrRzUywooV5712lfdYElapssr4FMFTqdED0ZJZlzXCemvoxBdtQI1ZzRNIGW3v1S29_0_N80Ncoa0nnVc4pCvswNCfY7PcIANbEY0bPPYRMrNtDh0Y22Oj0nED8HVoF62D7P1Ds5i62nNN81zsTpcx7Q6RmZp9tPVP97WqNxjaODrlbTgfzw37rY0mBK8sr6UvHfCj6R5BHleu6sDaZzg1PJDg46-X5ymeFvvNeUnvE2i3WlSXyo4P8GL98IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اسپید یوتیوبر معروف رفته‌سرتمرین تیم برزیل؛ بهش میگن شوت بزن اگ گلش نکردی باید شنا بری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23113" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/poIaznpa6JwGoV-CDI8t0ESv0OK5cbJOtwNorfx8TWhOgF82XeprFynbLAORK0bFDAzBVeIx0ZRukYebnCW_IHAJfCSfvlJgsGx1lmhwwre2BvvncgxH4r9GSthX-2cCzB1Y2dPzEz_jau7RqthmGmgZ-ce-9_Pl4fKRm1xY6MXLfPYsDuPNDF3UjLnm9jWc8_a8ynLesGHoLG4o2hrryTs3EtOnrPmqyBckjgoI_axaoqZ8ZEC5tHfTAGJMqFxnDs0I2FefKeqAxNBFKDe8RJIlYpwNr_nJXxsQAalj0HXRK93n0FbqBvefFzkxWVO7860lwqlzeoGB7eCslhpWtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23112" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSwgFliQq549u1lBQb1zWtxrtf57HCkQZcZ9PEhpgRtGV8AzbazB9oZqAo-P1Dui2RnkPrYRlyicsi9KOJ609q8kWxAPIuRuwX3c5WpZ1C5CyTinKsPxyeiwI5BTJYZGhorSC1UMFHkeE5LTg7u3jcKCoNv2oX8ZBGJ5XMKgWR3rgT_vBH17CLzbmWvUgUh9LwEzP4QEhp6rgOOA-RBbIw3SCFt8TadPwFplnDoVndt7Zx_ZXea-alVaTX5JnRK7zLmEuRNP87T3BbgMLZT5TzSgY2jwgvZ8q2zkjqsr-HODrI-yV72Od2Glb532sBNyrj8WpWIchOUjW18rk9vMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23111" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=RWoHk_htVF09Ndy4i-0X6ddfFORWh6IuYVY9_GNYc0ne0HmfyPMm0WQzjj8OiQB8fdshj84SZ1GKjK7ytYfhDj5iauGj5YMaLe_jtbOjpdmPbZAUtW4KHYtGquoBzRf08FkIweom3Wn7M4I31htKN8BBFWEo0lOiFgLmy6C6H86RfRF347sGi2fJTAcyzLYAHTje8tPLAuGF-OKbQoPOlrwVJvOlGbwtR_6pyAYQZvP7Iedhrptul9NtwC8Zb6FsP_d_Dz7x6JZdQ6oWfLEJtgWW7DmKjCzUeXmhQXZP9KmqOjT-OyANl3AOLbKc71mA2AiLRjTAehZwB_hYvqiaxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=RWoHk_htVF09Ndy4i-0X6ddfFORWh6IuYVY9_GNYc0ne0HmfyPMm0WQzjj8OiQB8fdshj84SZ1GKjK7ytYfhDj5iauGj5YMaLe_jtbOjpdmPbZAUtW4KHYtGquoBzRf08FkIweom3Wn7M4I31htKN8BBFWEo0lOiFgLmy6C6H86RfRF347sGi2fJTAcyzLYAHTje8tPLAuGF-OKbQoPOlrwVJvOlGbwtR_6pyAYQZvP7Iedhrptul9NtwC8Zb6FsP_d_Dz7x6JZdQ6oWfLEJtgWW7DmKjCzUeXmhQXZP9KmqOjT-OyANl3AOLbKc71mA2AiLRjTAehZwB_hYvqiaxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌قلعه‌نویی‌وقتی میبینه باید مقابل دوکو،دیبروین،صلاح و مرموش کلین‌شیت کنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23110" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6fx_4T3s_7B3yv45Lbsqx94NZ1BZnTQafzO4N6-L355p7fu3Oi1Hdrl98XWaQyKz3PM31bAidv3ZUwcou623AEDd705R1MPAM69sSBBem3-sB7Kw7wT1WCdULJqMHzlxwrHYQ8AxSPWj3YYa2s7u66qaHsB6bw6EXmDukK9FvcVCRUcq_Hu9FxSBWprRq7RdNvSxyYE5S2qZGZhtM3-lakBD-GVY-SXZoSlMZ2ZW42ZzUfQP1bNmxAGHv6IbNRja-FQDnQegz1_U3hywoNXcq6d0TBWasjxb7HdJ1WLXpyCPQJ9gdwSO-c9poltez4dN_0T4DYkpbPE6WcZ5T0xwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
دیمارتزیو: باشگاه رئال‌مادریدمذاکرات خود رابا باشگاه آرسنال برای‌جذب ریکاردو کالافیوری آغاز کرده. کالافیوری خودش برای عقد قرار دادی 5 ساله با کهکشانی ها با پرز به توافق نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23109" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23106">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYgwisOeZlaoC09AIGhrh83uTtEmdVYQRV8lgIoBeF_CvR_94cEMyZOwwyPBEW463RFippy-XdZNHxX-iQqWqmqt5HbqR_vKWZB1lEZ6axO_UKoXeRY4GHVsrbhm8XruE80VaIwYxO8WSo5Dh8QLbRurcO_4NE_Pzmkl--KQGFylk7TJZWl1QnBInlLjohzAiDYO4SFTvIRw5_iotkWyhz3tlVclC0l8PbZDdDHSIrQvf9V0gTKQOEARgEP6HCNnF8zx75E7C79bMhZG5WnhWJOiyZP_v-ZWUvuu-nvXIyBCFcPXlCmSPbeYw32OAivctqoCvk6RWwgWGVRUhj9mRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23106" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23105">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RN4fh3u0G307zPsHcPA-EukOIfDnvTIRQy1WWWyQMYwVXoZ7WNB53p__dREwXPdMRZftSp5ZIxUtTkk1o_rHKdSwJiAwtxjTBnRbCeN_J-GKRrzVHKddVviFEJFlcsjms-H14fea028kbSkRybsjjrqDY9FWt1j9MTeRz6i1rlAb_UH4yPjn306opjs1mx61TpXK_eDZeGY1NTx-Psw9qWDCHkQiKg4ZWExQrH7rTW8X_iJaACN2dH79_IF6OEP-KB-l1V3_hfImndrWYWS8gK9MpxB3PnT0XZ-sDzpzV75OqyLbNT7VonwcanG4hRWgib3Jg31dmHy3b-PSc23CGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23105" target="_blank">📅 12:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23103">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhVkmEjxuYnUQdcirrfXNCp9YEAbmtsKNjGC35MLdZQ41wPsuqRQqg2QPkJLitoHayTrNH36wawbfwTOhNRQKd7OjtRr-mMD6oSkYIr5Lz8tMh4-ncJncY2enfT3rzAAv315SWGZcFpAhof863EQVyZ3G6HvUYDjuyhDXih7GEuEXVsZn_NSV5bYWpPxpFIxufYow-RgRhjlCByWSXWOOSplilz-y-n6h_lbjT-LTJUkPYhPz961wErGH_Tp-uOBhzjB92rHs_ut8nFyXvoRvj2qaYyQXuaKxeDc6cZlDDqT-QGO7DFgCxTAZS2QJtskx1UIb0w2RgqsnxIBpHDs6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/om5FjeOajgidyUthxIjLaeaC187N1oKNffGyxJk8WPP3BbMepy6beGI9W6K3gENM-mceWRZ_PGwqj5UVPyIW8-tUS_3oPkP_PiriW_4pd1o0pWBWupMIvfPBulGBST1DYWZf1K2Wivxkh6KYL23uAWsurVJL9j0eDNeMwtHLbsefr7RUFZXvcVReYvJBj-leu5zZFw3p-I8_lvYaZEGcMNeYefywFzzp9HCXu-saEBNL35zYFw6l1h6CKBx2XlhAuYA0PSsi-97FZUwbACb0qeGAM_Wov7cTFkNbJ_BqV5OKbmjgtL9qtp1P0oX37t1wYHQ3lk_Y2qRVWROjfLBRzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23103" target="_blank">📅 11:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23102">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqNbVrz6QJzGPi-ofEI2wIfy0_Uaaw721vp7pA2puWPVP1JvFUDdqGt-Pvq6kd3In77v1FS9WTG9iq8cYBwCyeND7FH2CwATSfz5u-A4ukaKWLOY5Ma-T9A4FRA24dBjlhT-Rs12BMlOIrDTBpScvY_orzz-Bxh65yxarU1pBdnUaltr5jQMthE9cOgfLOVMCKmEpGAzkndz_ZJ7ZacnKPMZ7De1Diz1L96AJQaF0Bfm0PnrWaEnPeXbOMbWJ8Nvr6mHal_gWWDEoDv6FPSFZkxGKJY1uMrsvclSOEbtVZuvbvkDasGg69LPMVY1RDb4J4kOANGzquBG-UKV9pt7MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آب پاک ناصر الخلیفی مالک تیم پاری سن ژرمن روی‌دست‌مشتریان‌ویتینیا و ژائو نوس: این‌دو ستاره رو به هیچ باشگاهی با هیچ رقمی نخواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/23102" target="_blank">📅 10:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23101">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXVTQCeWOAa8qbJjGkUaO_dvRNAsSXOyZOjKysQTWL4z9h1WG77cberHH5DvUQuVii-lCPbz92ykT6_gLEAezvtvvzPBsyoV5Ra5cSi9xEJtgdTd5n1S9uEb0FPHxxfq8kVjQvpC3DF7VSKxDUVySo2HAy6o2DWpDwLq1lrXuDb4sgB1DL0bc4wm6UTLsJvqz-xPFXgfkDIw8Md1LTjmlc5E-x386-SNsklTmi3DgKlnjjyr3RuwKKloiv-ksVb0Z4jYcpk-Koe6-XJlQJzMzgor97B8FvvfkeuGJDliHHgNjEX_A895UxECpTfOn9-HSsgF4-Hny_7hRiFtoH_ZcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل گرا مدافع‌تیم‌پرسپولیس با دریافت چهارمین کارت زرد خود، دیدار مقابل ذوب‌آهن را از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23101" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23100">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=QZuo_gbKwwKm-2XdgDqbNN6uoix6cTvM8isqa8FlqWKXmiKtZJaDSWRDrfPIzudBDVywNk-LYGmOGK5GKJ_aEDjGP8e92xOk2DJoiGTTxmmIXGlzX5QddJRAW1mopBvEvq8X3rfjOzpkLiz-lzuIR8ZIVm1DaxFsmjR05vqlAUCJI0FaolvXjc8S2dJSYmBkdHHGcVdzoEAt1oaHzWtH4L9lNc253-Uvqm1OtD18cjE47_cZ_41c0324BaZWqiU0R3CHePjpu7DBdu9wKiNyVFxwrUUVsZ3NHbSB0TPJG2bqa8VsTdgz73J4UE41p7PBivw-36tiyO3u23RZUdr_Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=QZuo_gbKwwKm-2XdgDqbNN6uoix6cTvM8isqa8FlqWKXmiKtZJaDSWRDrfPIzudBDVywNk-LYGmOGK5GKJ_aEDjGP8e92xOk2DJoiGTTxmmIXGlzX5QddJRAW1mopBvEvq8X3rfjOzpkLiz-lzuIR8ZIVm1DaxFsmjR05vqlAUCJI0FaolvXjc8S2dJSYmBkdHHGcVdzoEAt1oaHzWtH4L9lNc253-Uvqm1OtD18cjE47_cZ_41c0324BaZWqiU0R3CHePjpu7DBdu9wKiNyVFxwrUUVsZ3NHbSB0TPJG2bqa8VsTdgz73J4UE41p7PBivw-36tiyO3u23RZUdr_Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
درجام‌جهانی 2018، آلمان، مدافع عنوان قهرمانی داشت درآستانه حذف قرارمیگرفت و در حالی که 10 نفره بودن کروس دردقیقه 95 این شاهکارو خلق کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23100" target="_blank">📅 10:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23099">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇧🇷
👤
به‌مناسبت‌بازگشت نیمار به تیم ملی برزیل؛
ویدیویی ببینید از شاهکار‌های دیدنی او در سلسائو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23099" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23098">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPg9j4Aa6iLLG1hQR3otqK16Vmbi1u3hKhKsGyzHuXgAz51a5lRPYwey95NtMQWLM6UOzRO4bNRc4X-prg_CsfE-rOq7McrlGf53UEGkU5TQFDSY5fkU6kvHxsCz5AhFb0zEG7-ljzTGAv5PQyRHhQr4ofAy-xL_NYa7LcuguQhqcVePRpUs5B4r-t-P9st8GdP0cit3XNHwJI9-u0JsTQbSEr1roiaMilMcCPYHZmHLHqrFiPVM6CHv7j8O_EvZ3eDvREflQoX2JMgAOY-hquYASqS9e6RenY-2NhtRKC_287BmowDZMPs84SvD8Nf0YDjBuYnhRT6qTI-PBfaWiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی جوایز تیم‌ های ملی در رقابت‌‌ های جام جهانی 2026؛ قهرمان 50 میلیون دلار میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23098" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23097">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R59EXtS2FioYxhv_aMt3moTbhkL9TzxgdLqphrrsbyMSBEA30OkZT3G_XFXjarWt7LuwV_qLZYnBLN9mum5hCbsijUIxPaHeraLL8EHjDcbO6upYCI0mbDfO56oE7Z_lgZQcgJFvgNCDWEsek25QRqv7GYmwws7WB9y8Go8Y7NOdgXwQ22qoa7lD8O3ev6v7DhETz5v3IbQd3kCGLE6J-oNrh3H0ngfMr3vi_mUYmuPPkLRF7ag9MfupveYEYs27h6cOKb1EgA6qx7forFbKAz7hYv-XysR3Y0AlJJp6ugm04VZfz58bZSa8cbYXh-2kImNZzEzEEJLa_2aQyql6AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان:
بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23097" target="_blank">📅 09:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23096">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=YrPmmcFY24FetWY4D3I5YaKCAKJSqu0bNcaZuCYC64f2ZPLy-N-LfTdFeaJGWT7SXTSGCrroXcgo4gvKV97li7PGN85JwovWhacnxL78-YvIEtNvxmo-JoPfUm6EoYlHAu3Sohi4nH6-5zeq56OmJ2jJ2892iWvwzV27bNTPCQt0ZFH6EkpqqTUHoWtOV8xelAF-PPZcd_zUMgLNiyxlFzHEVuriewcGgP0GZhCJSZ_2qFHPdqJE436opkFpzdMzSGHEpCNXW4fz89-bu8hd8YwXSn15-4kuliINKCtaVGxR9TODB4qkHetFWXzbi7maldkOQfabLiFcN-wmO_pfuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=YrPmmcFY24FetWY4D3I5YaKCAKJSqu0bNcaZuCYC64f2ZPLy-N-LfTdFeaJGWT7SXTSGCrroXcgo4gvKV97li7PGN85JwovWhacnxL78-YvIEtNvxmo-JoPfUm6EoYlHAu3Sohi4nH6-5zeq56OmJ2jJ2892iWvwzV27bNTPCQt0ZFH6EkpqqTUHoWtOV8xelAF-PPZcd_zUMgLNiyxlFzHEVuriewcGgP0GZhCJSZ_2qFHPdqJE436opkFpzdMzSGHEpCNXW4fz89-bu8hd8YwXSn15-4kuliINKCtaVGxR9TODB4qkHetFWXzbi7maldkOQfabLiFcN-wmO_pfuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23096" target="_blank">📅 09:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=nN4dCUf6Xousx_rdJ7m2z72ySuznNxBLC4kd_LEsssHtD8CYhKZ0pIK2Wryz5OgGYPoY6Wmo6l_h12SUvK9g3sjkjSMvunrS2S5u3ow-y4h0Jb6-KO_eZIpLPXnKe52O0SRl9yENXqxIL159O5opp4e9oUSxvjZEGnFvq7mUevxwah1eJx3KoU1DSNo4LuUbYLHvyYZqaFG-hu0qD8EftYDHB6wILGwLQHSLHd06MPEDXL-msNq8bJ0jTFeq29lYhMFvEidBXCR2ACHs9JkxXc2n9q_ziD56hrJ7Jh8lATf1qnSVoBX8XN5Oe6XeTN_aF93QVLYjsSeYC52F2-u_FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=nN4dCUf6Xousx_rdJ7m2z72ySuznNxBLC4kd_LEsssHtD8CYhKZ0pIK2Wryz5OgGYPoY6Wmo6l_h12SUvK9g3sjkjSMvunrS2S5u3ow-y4h0Jb6-KO_eZIpLPXnKe52O0SRl9yENXqxIL159O5opp4e9oUSxvjZEGnFvq7mUevxwah1eJx3KoU1DSNo4LuUbYLHvyYZqaFG-hu0qD8EftYDHB6wILGwLQHSLHd06MPEDXL-msNq8bJ0jTFeq29lYhMFvEidBXCR2ACHs9JkxXc2n9q_ziD56hrJ7Jh8lATf1qnSVoBX8XN5Oe6XeTN_aF93QVLYjsSeYC52F2-u_FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحنه‌ هایی دیگر از موزیک ویدئو شیدا مقصود لو همسر ایرانی خوزه مورایس برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23095" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4vBPinp-62NNPy97L5eUgHCBY7EMpr3GI1_APCepspBN07iH-JmpwT0nszM0azUZVqp91qMX9mm3Tt_oGUzJyN5fQVov1AsQ4QG2aVKRXm3r1rZPpd0r9mAb7Nc6eEosmthBn28xNjy_YznJJ2-T6O853jSTcVC8gh7KeDtMJDyL2cwdh1R8hjQEli3YVOMKXFEms0WpJrXZd3-HSM8BDbkFxsn_zV01OL3H2tcgUCn2vdIVaZwk4LrXvalXjVse80wxIlQqqt3in-Z5mEkB1H-1-nLYyYieBieRwdSmwYrseTUaTH8MOS4JffU7UoVg8V_hBBco35Z-DWhWn0lNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtJ34b-9f18NyiFhzPaD_3jimy8s1FgEg6i2AVnqzFUAwWZmMG7OcrXMmvtuCp4CoBWwvJtCBp6SIXkuJTZLjSpdY24Vjx2tSJgdlrZoxS4t5FMPxhdMRjhdunc6umFJCF5j5LCczG3ZnlHEZCyuU73SL0hV3dKxpnry9q0YmcPCOKT76Pc42z7L-c41aDSpCPVnaTNI_4LFjaje6pnggj04rXgxJmua4qbI1GgoQ_Gcvgr-LOQDdQrVIlPLqtfuevPr-8x_WB5JsEP12qxOFbBBZYUd7wPxzUf7GgBuQ71y57ncWfczfmn9QxBHdjOW4QtCp0lLigBUKDENlzHyOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه تک دیدار دوستانه مهم روز گذشته + برنامه مهم ترین دیدار های دوستانه امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23092" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=hpxCoWDnRH1OV-7j3xdmMYfFYUM9r20mhG-fzfxoYo5LEs0nhGAAWvAVWdd0tvZFmropDRVZ9--UjyZohcsARsZAorpQj8h17uGhmjqqb-QetMQVoX7qqiprwWk8KxBABRS24rlgAPsqoERdTeZZZqL3z0OGBnZzYvG5GqXZQmNpyLdOhHMsuFNpqKNT3TTD_61Kv7P2bwTDPYW9fJbCqbkdkQhq3ihmXo6-CvO_h7gnCupTWKzeei7dCey9sA14ZvwmTnDfvlfKgZBWIqyg_tXnDgsAkNG2OXPDV55TU0yCeI9nN2tYcPLOHAHeJujjbp4GnNI4oafFO-_LO1gVeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=hpxCoWDnRH1OV-7j3xdmMYfFYUM9r20mhG-fzfxoYo5LEs0nhGAAWvAVWdd0tvZFmropDRVZ9--UjyZohcsARsZAorpQj8h17uGhmjqqb-QetMQVoX7qqiprwWk8KxBABRS24rlgAPsqoERdTeZZZqL3z0OGBnZzYvG5GqXZQmNpyLdOhHMsuFNpqKNT3TTD_61Kv7P2bwTDPYW9fJbCqbkdkQhq3ihmXo6-CvO_h7gnCupTWKzeei7dCey9sA14ZvwmTnDfvlfKgZBWIqyg_tXnDgsAkNG2OXPDV55TU0yCeI9nN2tYcPLOHAHeJujjbp4GnNI4oafFO-_LO1gVeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23091" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzWjmcdT2fCG8sUj2PGxqAJMXXRb0DtAnCNuxPkTcbufKqaRRj8F7_btjMlQvMhxmTIki5M7bYQffuzGd1zHWUD59eYcHjpzK5n1ft6FiWsB85b-_awvnvBcefnIXIXqXbHbvIYBkZJGD3zBUQ3cXa7XDfsTNe3lQP6OJ9PdqwjOjXUZKGlM3VPBMBK_5NCgOXP93MfW71_LboB6hPzu2xtxfVqfWe4iygY3Cr2TS_1GuE2N9bsu8LBHSz2QaZiaHDYGoeJVtiQDtb7klnostr_ccXmXzTWBFoIGQVlquG1ZNVOyWqoWhCsgSeKHFGQ6akMf2CyUd0OPGIpsonLlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQvCea6nQXqxqeTOAGDlWhsQop_4gS6dcgAKuNRjeFTcrORABluUbx5HD4--3XDvSyzUUV387QJX7HhHdUfT_qzKwfTHNXu7So9zmICyUA6NlohI63CokJIv-ds_a-VuRgYFzT5FjnaHDcFuLj29TfjAzG0mr_kXqGKOx4eoTfxkwDdSkP24LuTy_489s5jVaQjEfnBvyjgL2rQTIUvDohHufgxKgdBnWcSHsM7_2hb1NXH6BxQNeJE5ZI_-NzTEXzNMbn348GKHDhnpuWr6fhuBdkdI6s39OA81K17fv2L0Aj5twJC7BL0hCsxYuf6xDvNUW7AAiu_LO4u1C8aBfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌باشگاه‌های‌برتر لیگ قهرمانان آسیا بر اساس آخرین امتیازات کسب شده در 10 سال اخیر + پر افتخار ترین‌ تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23089" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHBInT3exWh1Y7GmRdvifzn1urHPLpguRSIe0RrPbwhc7k4ARgkMX3sBdMBJ__J_uMIjxIfOrxrpOdnv3O8I_ywxHBAMvZ0cTNsLyD_2ylkKJ8XMBAQmZFRH9NkJPuDHE7_3xK814y2YOrzEZ8cMcKS3RJADpeOBkhVyq63o3l7dDtaJLVPMZPu1nHKc8udRJcW3ZNHAkTJYjpEnc0IjhWpgxPSxDhs0kaBAFKOlbYMmBFF68fPGXkDM5fZ7ELWtQp-T0VLfJkUJt_Xm95i0of7L7QT9B57VlOH2c90OJ1XabOI2OT9kXyVcDX4H_I7oIqZIdNH5Phv1aHjhqilnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23088" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5366993444.mp4?token=MWEOl7Tcx2jcHsquJtXiQpV7fSYkbPBoh3M6v--mdSAWRYVmilGlQfcI4t0aEeE6AOwioXt3pEZ-BgwL8BcB5D70XrVgJgwTw_TL99tpygzNt407BJjZZkKxj1-B3BmywFg1-__eKkZ3CaPBzWZvGn8gkT4_x--evFKZvbgFIupkDTH0RMTtxuKuU1KBNbfNTBpdseO2OprTl2bO2n94uA41S9XErum4KKOOIfgRbTAtizsN72Mfxwoi1WbZ3IyfDpSp4O5MgyhhCmL86iNcs9760gLZpWMUtjDkP-OE3jB5-aSCvUKF8wbV6VyyXFiFQvwsbSMc0Ga_loOpvRiZSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5366993444.mp4?token=MWEOl7Tcx2jcHsquJtXiQpV7fSYkbPBoh3M6v--mdSAWRYVmilGlQfcI4t0aEeE6AOwioXt3pEZ-BgwL8BcB5D70XrVgJgwTw_TL99tpygzNt407BJjZZkKxj1-B3BmywFg1-__eKkZ3CaPBzWZvGn8gkT4_x--evFKZvbgFIupkDTH0RMTtxuKuU1KBNbfNTBpdseO2OprTl2bO2n94uA41S9XErum4KKOOIfgRbTAtizsN72Mfxwoi1WbZ3IyfDpSp4O5MgyhhCmL86iNcs9760gLZpWMUtjDkP-OE3jB5-aSCvUKF8wbV6VyyXFiFQvwsbSMc0Ga_loOpvRiZSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
جام‌جهانی‌داره شروع میشه اما همچنان با بزرگ‌ ترین غایب رقابت‌ ها؛ تیم‌ ایتالیا با شکست در مرحله پلی‌‌آف مقدماتی جام‌جهانی ۲۰۲۶، برای سومین دوره متوالی حذف شد و در این تورنمنت حضور نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23087" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJToww9LMO_WwrZ49NO9cTOxTbZTNouTyuiDuWVYBwGxLjBs8rSh6bB84Rh6E_ZKXFuYaVZhKbp5YyKYzLZ0_wnvQWAePfjHJghxggbpcZme53DgS1VHNvSmdrOLrsLEoiJJ2b9NRzxyo7BZVtLWx4v8Wybnwa_4iWyoWA5ptcUgqh5GR6suA4pohBLqTFRGjyQYHfmxwjjL8ypApOgQcqPqw0-Rj-vC7sQjNaAIJMPoCXP6nYJlicfLfsQtl1RqXpzUZpj37Lk_Qbq9HcCU0HHlikPbFdMzhK6MaubePhsYeDIRJ4DAVZ_vLJowxTRgYqupSRR2XmB8AXKjBrRM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصطفی پوردهقان، نماینده مجلس: بعد از رفع فیلتر شدن واتساپ و یوتیوب؛ ما سراغ سایر پلتفرم های فضای مجازی خواهیم رفت. رفع فیلتر شدن اینستاگرام و تلگرام نیز جز برنامه های مجلسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23085" target="_blank">📅 00:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k34vF0hwaikkx_ApE9lUI_sPEVhGVLf38iUpVXsb248Qq6XUMhnjcLHLQjtRhH15YtbCCrG3StX-mP5rKriCW9U53edMuJ_DM9T0owPDYFNOU7SjR6894d_QPof6hhVTSIXvSP1Kmv0Sgy4WBi-6pDBOSwnDFuh0_4QbNB107gNWpvcPl9Ce0FUaPD7IeVkRFb5EMxk-4PcX5Bfc9cXFbIJ2LiHh0JsX-xSdSZvx-H2Z0Oz2icHkygjtMl06W6i89zLW28hxWyBcM7tgg9Iueau11qPoij7BH-szrEqIe7KCc7a5UHD14S3mq8YdaqG9TYNy_WNlgitG_FRPMl70HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
🤩
#تکمیلی؛ نشریه کوپه: پرونده پیوستن خولیان الوارز به رئال‌مادرید بعداز رد شدن آفر 150 میلیون‌یورویی کهکشانی‌ها توسط اتلتیکو بسته شد. حالا بارسا مصمم‌تر از همیشه به دنبال جذب آلوارزه. الوارز بارها به مدیران باشگاه اتلتیکو مادرید اعلام کرده علاقه‌ای به ماندن…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23084" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5c9332hCIiCj_crmbcOBws_z7Vwl6eaXEOnlJ6kSmGmBqIBuv2VOAaQvhOyDYlVEJ8N0rlmL1CS5AQEU2MKaabPFOkxoAyARAjcOY4BkCX6840UPM-kvrXGTfU0i2KNRp1Uor9PppzKByD6n4paHaxZGy9306Z-q9uw7Mae7JaMxWx8ir6hFoWU_GkVf-4pLH9R54ODOrokozKkqOG1WkJAb3G2b9rH4tG-u-5CfyCnauvwuG3kVmc6Ga7yfDeF9HyIhI0Pt5XLsyD0hGYdlyQ3AyhGSfdBZ8I9Il-5BTbtZk1Knsxmly50dQwon8sDlffm7yXMidXihvAlBMpM1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwaDG03iqmCKrojDbl5G6XRuaojRk-iGhj9OiKwyw4Dy4KwhTvjHhP_pIIOhuQJKFjBKu9Fxqq7u7cgS7rOqYS-UqOgcrQYZtUHWiOQWrlMiVa_wpO2cvclJhEbFMYZ2SJFwWBOYpyF6Ertj-m4C6Tf2EdXOyxo_xbVyg7saU1dzi6QhBN5SrBIYtroHCW39WZtY6Pg-9CS0w_Er6Uxymf4eiMU9Te0uLNE3MdLQuU4awiEYFRoy2U78CMw-PhJUXBjSloRwjGpO7IoUckRwTcNgwLM6whajVLTus9eujidpS0SmvEHbvH8SR5mPnvKKgJMaoiu8bEFTIfV6HOJYmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9c7e2ggoqnacsr-O4kKCA61CSvUuLB7EM1JWpTtk5fnypBBEtGoSE6S1tTYUWQpb3RJ8ECPFmZBJ8tbNXy-8QDboXdJfRXq_Fk_7qMRf9YFGp5Eiq5hX7wW87C_GNcnutEDRQBrGQO8XYixFKIqLYMbwFxv1V7DpoEko2yBNnL0VXuYCAM_UcDYdIxIg2DkIFTedj4H_wr7yhfL_RkFy-xKsHFugNeRECBvlYPynLnR0Rna-o1Wm5GFVIReYMK7jUFLqBwmyU3zVlg3N9AoQErVYOzCslrLpU-Xhj_NEdS27qD8i5vmD8F6IwIwgFQ2WAFFxwe21bz73DJJncc_6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCCtWJZwjwpIzoY6IDGvDi0kd0fgBeF8I0MBqkDWLIBNtyNO5GNmtohCurEzC--_pn5DdylTN30ui-cq4vjP-2SXF7lzLshKGhhYn1svnIzn3FW8WYyLD1l0ZZJb2OctL7h_YiRxGDgfYpS8YSLwIleE8JrHDRUdnuzPwivdKdM9GSkFXjT94fQEk26vXp2mTf5OESWI-p7Yw9VM2uHNtl9NAxCYH3hLdmMVD7cwZ0UMqyYiH5fT0v4pEfoo2M20emzDR78aO-RsRwRNOIScl0k6LfuXGQ9pL_4retTs08E2FAib1Ocz601W4npwudfaVtsdQwnPe-_cj8DZhlYg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vubBCxaSDSfx4SLKw0iHbPC9buQkpav9n5bpGTaMtGBk1P5zt_7KNibTpGthwxTGKz_eB9_fuz2k1_0JlNVtcvfnlckJ0Fo5lk0tIf1AE5hruBXIvtzGUtukGnZYWNFvoqsl4Ie50-p0KgHSHonUcN_aeOz19UvV0V7MeAk-Na35evJMqNSdgogLB5AwS8hyYfmu-wnVjD8w0bJXL6AwwaR1Klu4IbWfehmlzDs1VZaIcZ_vw6EyQ-cp_wYd1UwS1UTVqvnbkjmUB5B9CdcSinY_IXh31fDK1eIiKxcFJHODrtxlc_y0mX9tgVAUXcItuxyjkXwO5Ki0fojcc40JAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
نادیا خمز دختر پاکو خمز اسپانیایی: علی رغم‌علاقه‌ام به تیم‌ملی‌اسپانیا؛ اما بخاطر اینکه کریس رونالدو رو به شدت دوست دارم امیدوارم پرتغال قهرمان جام جهانی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K0P4imVBk-Drh1dmZrxTjDAkPJYMwAfUfW1sHA7IaRlpEhlXLxeRmgQ7MQQxhg4MzeO7CAJ2UaaOy3ws9lORJzP38kNNEws7Zl8wbRmw5w1ZadY9akcIR_pmoA4U1YfzbNF77ThGQp1VuPpcRmpAzIsSbpcoV7LHxxvmOBjN9RwMHIFmDaA8miZP1ckIJ_Lb5R8Z4cT5_Iw-rvzAQlrqhtkGNHAXnb4vxAWSAm7XK0rCjvIHPNBuzKSgKcmmMAFWIhlttd_fVXPWysz0U2O4yVy8hn-is6rIRHwzl3R_4OUKWGe3hvMI-fxPLyGwhAbkts5YiYLoeQ0qFBuS74t2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsKlOuKbcg2kCIxc0bwZBinS5qy92mFixg0-GFqcFM5yYqCFJeq879bBaPn2kEywtakGXukF2wmiLBue4gJ2FS4iXqdp78yPQL-inLyFFT-HjQQ5ExRzWRCXTCO3UrLN70fpFJIMxpovMkJbqRn9KOtncSvwf5ybg0-HrYxBv99WgmiIs7n20Q-mbH0-GxH22DXPHRY4OohYAzUjREIaDDq_suQnWvl4kirNkIULwBYN--0PV6EE3x7rY9EG-s9uR5RG3DjphHafg7JI-efZ6lc6Ca1ImdiS28Pg2he0Cv30z54goVr-D88raPbqhwvpXqoB93Quigj2TBJ_kA4QWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtViY7a4ZO5WTn_rQni4DOyvMVaw5vJ9PUpHqbjQvW7vcCpdBGo-doH3ZE3wh5O5Qq6tjap1UZ4evdZpDxWDMoB2DRz5Zk2KmpSfNGwQ8Rk7zY6p864E0DYq5X-9L8r2pbGvs8oeuCuZ6cyCScoP5Je7LutjxgwQsaJVyQ-PoAGrxkupTJ3IvMmcZKrR6mvZbg-gOtrs_QbaWjy4NAsii-mhC-_EuOln4AD5uNjULuwU6s4EZnv3vL6CPrJSq9GQbm-pviDY7zy1rkrzXN0HxlzkBzPYxYFWITmRa_Ud0ov4fWwnA7CyAP786CtAfLXBLFr3elaV9naUs2B1vrU0bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
