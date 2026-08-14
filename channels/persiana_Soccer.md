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
<img src="https://cdn4.telesco.pe/file/krTHVLfSwILa3A6ofqvxnbSmOUnlCApvw0E6_4NZE0nfSdNJwJ3MG9iRJhOXgYCGcwT9QMINZNpXe2q30qH9RZk10Qcehla29eejpochP9umZkX6MUk6gkUZVN_CbaUbWrJINHiUv0gh59ZLqm3E1fp2pZrbgV4BkczhGzNSVLBSVv7FRKP2SD5YhdqWHJCTKTIYTzZNe_c_Oem3c8wmKI-eTrTw59riaPa2uLGbBawbv8FUW_AX_G4kWy75otidv4XeDIZQVLdNQhxg-QFi0r4A3SHs9kO79Ex1gZJ1HeLTaORK0z8SP9gjz-I1P4WCFLQete5WEfsWv5-trPKsiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 638K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 17:39:13</div>
<hr>

<div class="tg-post" id="msg-27709">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iza0cJWDzS8xk2_R_Zm01QK8AwcOLNX2NTtn30JR3hqSQ8YNWDlg_sYSESOExQ1ytREkQnSw4hL8_RSSj9HlsTdYz89D44Ch825Wmng7xWF0Mji-Hq7khhm5Y7329-44KHOZK7FE5XSv4uKWxDtoK0HeleFmRn3M2ZgPGbwWe3tfxadwWl6N2ZMFM-ZiHTZ668izm5tG5gDwS_g3n3n4PWWpqq_ISYYIfcoFRApLwM9UP8pmsiIAO-4MKqvYQ3U4FLgTYOYsbvk7-Q1lVAYLgpI1rBQBDBrJG02qMJ93wWoMBRhHUSsOQbLAge1nDSoU0AVCGjXQiap_8GN1rx1Qvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
الگو برداری باشگاه تراکتور از دو باشگاه بایرن مونیخ و منچسترسیتی در طراح کیت جدید این تیم برای فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.99K · <a href="https://t.me/persiana_Soccer/27709" target="_blank">📅 17:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27708">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6acf648940.mp4?token=n6ZoAOistRsgVJTeOKPcnEdN6iIA7mW_Ih6SPdQjzVqYerEB0hj5zNNPhUr-ARR3jOBJvkFEvc8NFscpE9Rsi3MSe-Eiu5A6dY-o0zXIqFBshl-nFASKnQnQnc44pfSdLaEGmXSWvRVOkaUn8SWZG_dyF4E541bORjRdxtIPR26LrK4TUNbKw_2UKVK23o-UxsncDsE9-aRztqR0gMvcHuy903MPMNFP2LlBab1gpv3FOIXFDk_kftWVv0GBfK87mBhmWnlkrfDndhu1-Pu75KQUkTSMQd3YJ_LEyFnwVo3nkb6Plz3a4NRLd5vBQ2zav9wGcjaWAFzpvuj6Ny-RuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6acf648940.mp4?token=n6ZoAOistRsgVJTeOKPcnEdN6iIA7mW_Ih6SPdQjzVqYerEB0hj5zNNPhUr-ARR3jOBJvkFEvc8NFscpE9Rsi3MSe-Eiu5A6dY-o0zXIqFBshl-nFASKnQnQnc44pfSdLaEGmXSWvRVOkaUn8SWZG_dyF4E541bORjRdxtIPR26LrK4TUNbKw_2UKVK23o-UxsncDsE9-aRztqR0gMvcHuy903MPMNFP2LlBab1gpv3FOIXFDk_kftWVv0GBfK87mBhmWnlkrfDndhu1-Pu75KQUkTSMQd3YJ_LEyFnwVo3nkb6Plz3a4NRLd5vBQ2zav9wGcjaWAFzpvuj6Ny-RuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/27708" target="_blank">📅 17:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27706">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GYAeEoAZ1oy9GeptIt1VIC1u1kCYTgb4rYn5DNXwqrn5nA4qShcke5HZCrUBKTwC4bOCQF1Rcc9RunB7ld5Ybxs4CQAAAAqCGa17RY_3R-3qHcCE0hJS2WFwITD-4QgTZFhXUAXlobqo_wuSKulfRm1Jtw7uhy_SWTJWnbQlJN4LxupUrHGRXgZ_unwqaevt2ZWl_8D9PSzPQrVVy5QB3pvbA-pMT15A61cvXpTFSTzGZ8w5rveg5bKZG-3hxbCDRRt6UstZ7tgiDf6kjsEprzzGcIDSKGUkXLDP6cfK0w-rq3qxTbymmguVtG5pPnmN0OPMyiC6ciOSUU0CvBphEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3g1pvgLjCLi8T0gJhaun1StvGY-IfGBkdQVfkOWFTWOJLv5gYs3YJ3S7azBWqmtoQmMv0bEaWCM81RdvVnWatnYNohvJuutxAx2j4ERroRWtORJmAPN3zYfKNQJRUhF1Z2ouANxFC2WnSRUK46Iq94BLYU8kw_nwiaJKyJqnTK9O4NNCsAhjZq6wiMWB9nyyJSLa2WvMCeB2wsBNFo2TUHVuXfnTJICEHVzZgvhvGTgtK2MB5FxfJML03Ox2oLJhWVnk67eWS_uS5j0a3AodPtXwgPVzziKsro_gQTJgmx_k39r866ZXbFvhxglBmlzqFoWJ2NYEqK5rkfQZlwzUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
الگو برداری باشگاه تراکتور از دو باشگاه بایرن مونیخ و منچسترسیتی در طراح کیت جدید این تیم برای فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/persiana_Soccer/27706" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27705">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erDxQ5mpLUfynsK6AxUJoqRD7jjYi2lGx41do4DrUJZRWmz7AT0b_ntubWLvmv759rCniLerYfBvRpsgwazZKqzaqNZ_YFzIYA_Rf9mF_cJIYFpZgTNJMAxodMXsNmwqGdwRESzE0OIa8ezdbLt-gaxvZ7bVp8bCGhfAeYHSkUTL8QdEdgJrIYbTuIYmH5VGyx6ucHEwpkPzTb2itLzU1NkxC2UOflnvUkEm3oTTocCJmKFas8Xbe4rRxiXSk62pzUQDwuJYbWVzHanlRL_AWwIIOvKY4fsznDpTKMFWxgvZI77B2ge38-Z3Gy3FFQIakyu9vSu8kxVhNRj9SXfrQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل کارتال ظرف یک سال اخیر با این دو ترکیب کارکرده. جنگ ۱۲ روزه واسه اسماعیل کارتال خیلی خوب شد. فرارکردپشت‌سرشم نگاه نکرد. الان هم به جای کار با علیپور داره با لوکاکو کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/27705" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27704">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdmkrCd2yNRNIrexa0rB9zfRo4RlllfnOZHNUTlSz8FsJ9XKWNMexPoVuEPl9on7gYaosnKH3MuO3hxmnYH5dHbI9mQSuYJ-VNu2lqm_nO4beqDOp4A9HlVYU-WNctl4fm7rQ6aBNx46WXPHpGaXYbsoazcd6iutv8e1mP_jxG_-A1rCNlXmJskEjXPVWqPMHSdPBw8fGAGKex7qNefRBEBWUFt40AnPSSicSw4nl5wYOAgDOZSbhotsBOBCq3mubEaH7PsvsZQ9U-SwIA5yEXIv4G-Qu-R7MaOcv58YTqrnWyopXdePW_MBgynUtY2MSRzEkCx042UZx7XlxMHkjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هفته اول لیگ برتر ایران
🇮🇷
چادرملو
🆚
سپاهان
🇮🇷
🗓
جمعه ساعت ۲۰:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/27704" target="_blank">📅 16:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27702">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuzgNFPAeHxasJX4bG4mTpSnVJoNUtD-Lljb_DZeG-GBVnfxXphIhvvq48C8W6OwdDfJoJLI92oM15veCjDSonVZ8XkV3YA9qTdaWKTB-S9TabMAaJG4vtyE09-P2CKqq2XFUMRHG0D4Medz1G7IvScJV-tufEm--K8kguJk2z2CDY8Eddr5ryaZam3-DUsQOl130CPGURY-9uIX3mV7a2HWWFkOr-otIbWyWUsp6QkAAm26154RdnFybE6vfybjQkjCtKf1m7UwULGi2uxuzyJwt4BqnVYW5KBkChLHkzhXlXQTLI1IvJGJWiz-xh0N7Mp_ltiYfwQfewTQJyovtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kkITcL7a0BS8mBzM812y0o-nKVBJrvTd-miv1ZXTaAFbct5natS4iy61zQHql9iQnp46OJXxlu0Qi7zCiKQbNI6m2IK9OIfW2A-r01dwp8kNrCzQHR4-p_D2VcHEXRNNmvJxmLDdfg_BTck7siUYMo08DZlP6k-yZ4oyHN6mNe4Bs5EFhx1Sl3tLnqRSYYGQgSHE6J2E04WUXyOBIpLsQBLzjOnBaQIVi8ED4P-qOh1HfS-rYVDyrFX8zd1ahh97owaViqB3kiGYJLX9zB2cyvUzGHsQz4gmpEALNTDEz9MTt8ppVoDKsv7NTTbJ8bXy2PnYlAULC6lVpPoUgyK6UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
ویدیویی از مراسم ازدواج نادیا خمز دختر پاکو خمز؛ خودش‌خونسرده ولی پسره چه استرسی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/27702" target="_blank">📅 16:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27701">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umk9hbz_xeg8GZ134cjLecpdFSFbINSwk-M9rg8CmCM1cPvM419vz0TAOGsjbJomSjrby9GhCyOUaVyWR2_TxAAZ1wn3xMxoQKJ16U63gnbiUULrnyjmCshOBuDsQx6hFZdOiFk2HUil1uvDG8H4izsrMc3EJS_IfChvb-ZSKcSWXt6fibF6-Mzcyl_3NtbWKglT7B9klR37Mh6GpWrZm_32HHFxCoD7lj2MpiYBJLOwoXchhR2m2_Sua5mYv76ARd84a7LM6KxHOggRiZ1xrjB6U1kMzFs9SAeMU8XOTCSnxQvRX8cvcGTr2r3eUrHPR5LlF42AeyoKHB--nhl-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام باشگاه پرسپولیس کوروش اژدها کش پدیده 19 ساله فصل گذشته آلومینیوم با عقد قراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/27701" target="_blank">📅 16:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27700">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‼️
🇪🇸
🇩🇪
#تقویم؛سال2020 درچنین شبی؛ این نتیجه رخ داد و بایرن مونیخِ هانسی فلیک بانتیجه هشت بر دو بارسلونا رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/27700" target="_blank">📅 15:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27699">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kU1SdeK8MgBmjVHpWEgNqWwxXKUgCV02LlVf9B8B5BYOqtT-5EFhwOxXKAVGnhiaHcJ8PxxloeQkCgKeoQduRR_9Aqib9y234_ir254kwteeq73tDIV4FRNNx_m_hTDygv48Q8QlITN3WhYgRYLWPvHk3KXd7gWnL4n-G5tKt5HkCo10OOA9aLMN2ZHgemQZrgkRN3Mg3cvig1BYZ53sk0cb3s28tqAGPeX6dgPChJ9oeHrEuZ_zihRf9CS6p0GwnEqZMu84U60Os6xts0hCQRgvIrhoV4tG3mpgUiULauIiUuXedkfCkyhlAaBvtsHBPUdJHu4ieEz3GCVPSQHTdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/27699" target="_blank">📅 15:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27696">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWrBvLyXetIR8ex8ADHX7jfylzPMchPrjc5CERIE0O1DvR8ppzIzZYKIbOMwYB00W5igkphd1oQA5yXhfdnXlIfaW7o855fLdbuQArFKFNnanrQu5TRUUMgf9WtRnzT0tNbzABXS_q6jeo8iZ2twq6trrAhqWGPfOw7Cocet0AV7blKgxP8Ta_W88m0eTNFsmMiU5wiW3mLTDtCLeM1skQlr3MsFIuZ3R954kc30Vt8pSRRukWGiSK8yQwUTaU2uYy_HuCWMvHlRkaD_D8FARtSvojKPaXqJsGPsWqx9qPCxl27Fdttap8EhEgM5n-CQ5xcN9a2vY1jr7FwoRfGEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ به مناسبت شروع فصل جدید لیگ؛ تمامی قهرمانان رقابت‌های لیگ‌برتر از ابتدا تا کنون
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/27696" target="_blank">📅 15:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27695">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XlBsbyE3AIOd7lnlGsxvRXv0kVVLjdeFwfcZhJbZlUV16mKoIVORqBTQBU30kL6RIjYmZ1BVzstShm9m96qUitsuBQXh4SthqA8MJOakznR8WT_vB8Y1-q70KEBg8-DkmXg98pkeo9ko4wEEaKhs2vAk5fCkrv2sV9cWwI8yBW1T3TNchtdhbX_NytUgazf8rzANWB0ulbIe6rF0AKzLdZgMVFdsG-ZyeP0zIMW4bLiRDzHqWYyhKbNnX2IFgJigV-Zk-7Oh1uYboT-13mUzjiZlBGq4uCiqmWT6UTs_CFvYLQRRZgdtnJzyp86M9h_C5xte1oHZOkwPuPGuQSCoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ موندو گفته:
چیندو اوزور؛ بازیکن نیجریه‌ای که در بازی دوستانه از هوش رفت و پس از معاینه، پزشکان‌مرگ اون روتایید کردن و حتی باشگاه‌ بیانیه‌ای برای‌مرگش منتشر کرد، در سردخانه به‌هوش اومد و به بخش مراقبت‌های ویژه منتقل شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/27695" target="_blank">📅 14:12 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27694">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOGeDyYL3hP3aotdBGitSDgR7L6A_vLUGCJbyBk7yXGG5fX-S2vZk_UPrWZvLJPiS5tG22LZszOnQtTHGsrWNJnrwzBvXx5UIcYeoe3D0SS5OYc-G5LNWBAkmpTIirmDNvuEwGIPbF5AAeLOOxL1U5l0UgElOY7PLrw7WJS4O5aDPd1XzAC5pMwxRk8V2W-1drsG-LlWZ7Fm6qSvrPloDgZfbnu6kyBtYZy9PnSpi685fusXj7d-5D6c0i9tsTabqV_k2p8J8del9pYWl4XTY1DUted-4inEKamuZNGbl5p4zaEWZ5ThwkzC2nYL1A8JkW_U6_x6H8hWFYNTpbOCUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه‌پرسپولیس امروز ظهر به نماینده مهدی طارمی اعلام کرده درصورتیکه این بازیکن‌ تمایل به‌ حضور در لیگ برتر داشته باشد باشگاه پرسپولیس حاضر است بالا ترین رقم قرار داد رو به طارمی پیشنهاد بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/27694" target="_blank">📅 13:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27693">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3094b93ff.mp4?token=TmMks67dG0uqdnJ0IxDEA-y6-lHxb5IMcPMGcWFzDTnoeYtIBOeUhzzwjPugnUUcnq0GqI6lALG0oILjply4Dc89PcoiNEhjxn-J1N6RdotZ5dUmZBZ_8-2O0bC7v1o3xEcsU2SL3vbpoHX-IUdbRDqZ6K0BY_nuYWFcfNLeD1mI_QHHpkAtYHjo1scwdJNwXWgpQ-dKVsQerFYZADx4kqr0PUebexQQvZg8zwgMQgdTAm35hRSwCc4mpjjfCokAfQdogcTamVI7u5F-g_Mt8iQeTNbDScEFQC9IWtWhM_MEE3ULlVeMkS-yn3UxFmpfCf7Ut4LCNACwuIerVHEXZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3094b93ff.mp4?token=TmMks67dG0uqdnJ0IxDEA-y6-lHxb5IMcPMGcWFzDTnoeYtIBOeUhzzwjPugnUUcnq0GqI6lALG0oILjply4Dc89PcoiNEhjxn-J1N6RdotZ5dUmZBZ_8-2O0bC7v1o3xEcsU2SL3vbpoHX-IUdbRDqZ6K0BY_nuYWFcfNLeD1mI_QHHpkAtYHjo1scwdJNwXWgpQ-dKVsQerFYZADx4kqr0PUebexQQvZg8zwgMQgdTAm35hRSwCc4mpjjfCokAfQdogcTamVI7u5F-g_Mt8iQeTNbDScEFQC9IWtWhM_MEE3ULlVeMkS-yn3UxFmpfCf7Ut4LCNACwuIerVHEXZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌سائوپائولو داشته‌ازکشور واسه‌بازی دوستانه خارج میشده که تو اتوبوس تیم 86 کیلو ماری‌جوانا پیدا میکنن؛ حالا سه نفر از اعضای تیم و چندین نفر از کارمندای باشگاه مظنون شدن و در حال بررسین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/27693" target="_blank">📅 13:14 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27692">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: هانسی‌فلیک‌به‌سران‌بارسا گفته اگه شرایط جذب خوالیان آلوارز فراهم نشد با لوئیز سوارز مهاجم 28 ساله اسپورتینگ قرارداد ببندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/27692" target="_blank">📅 12:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27691">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWtqaMkv32S0hIWgRIabNtRvjtTbe4D9dcDzqHEhqC2UZdJgTp7d3dNePoshcBEBmB_cjqlJuGp-yk6YZjwkpASKvFt3ZhbeJ6WNaqFULHBORlJrso9fhMjhfAoLMO4_FfbvCGhJ0OAWz-inFsIYbWX5KzFKxQq9emEiJM0x1vDUxn-hXqlKBiQyP5aZBTryzUkGQJaYT3tqFUr3kDL35UW3amDHVV6CApMsZiKHnU3iVRvKf9a_Ls5l_iesdoixtu2r0G-sy-UGH8Mm8yzOnkpwUc0m8jMMF-KwhAryByUzKvwc2goKebFL46Y1bwjKHP8Cb98dWALkQia_g8fD1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇸
🤩
#تکمیلی؛ خولیان آلوارز امروز بار دیگر به مدیریت اتلتیکو گفته هییچ علاقه ای به ماندن در این تیم نداره و از آن‌هاخواهش‌کرده تا با انتقالش به بارسلونا موافقت‌کنند‌. سران بارسا بعد از رونمایی از رودری سراغ نهایی کردن انتقال آلورز خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/27691" target="_blank">📅 12:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27690">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FuBJQw0JtpLSGOCm6uySRGfeATiIwfUf-XC3ci6bJ8dWwXGBtj0QmBnSvF7-f7V6Sts-f2MTBJv9izNsCn6QjmoZiOQnATBeTLpvecYHNmrWkbucHHRFHOVeCaK00_zucZdfHKlE8hvT9QPEz-ziNZph0_H8eJDbaeyULKoC1e61-hbPgvvUoaYO0gV0Yk5xbhxsjyiTSA2Bfjno1wDqPf2zaFOmKs8SMoSv9GOAWbG_GtrLmMK3rgC2MMVUi9tfeKzCQFkdN2M3h-02OPh9FVFE4ud9efdQZN9MQqqD6wgvDjyLjKjj5fjVgACTfeRxkXJvJ61d25SZHvxB4dj-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/27690" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27689">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcLqPnXPFxvRfHQFsIZCF8O_mSmy_XECTeBAb70Ggo-LwFA9ScI0TMIAkRy7a77oyOgZnzE39Kf_yG9sFk-s6Amud03r3PrV-OOFM53ohkWnMxZBsQm8TlKpE0UrO-NxZKzbnIMbWD9lN1ErBVhOAHa4TEvXY2-GJoNDGxUfj2m--P9MtNBbSgV5JlT_LC0pAMYeiubhBhVpLNGPZtDMma5vdEhHubXFMl7msWV1MGHOJk05lU1SRFuc5tc7CUfmwubuX9KvCLinTkWoWpcvf0CM6SivqJYguD7dTfbyg4t7NVyxgRUhjTM7g39Fm5vonfvp4eR5OixHzex8A2B-lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🩵
تلگرام‌ِ‌عزیز۱۳ ساله‌شد؛
تعداد‌کاربران‌ایرانی چقدر است؟
۱۳ سال پیش در چنین روزی
«تلگرام»، شبکه اجتماعی‌محبوب‌ایرانیان‌متولد شد.  تلگرام بیش از ۴۹ میلیون کاربرایرانی دارد. ایرانی‌ها بیش از دو میلیون و هشتصد هزار کانال دارند که در طول سال بیش از ۹۰۰ میلیون پست منتشر می‌کنند. این تعداد پست در مجموع بیش از ۱۷۰ میلیارد نمایش به خود اختصاص میدهدکه‌نشانگر کاربردهای گسترده تلگرام در ایرانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/27689" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27688">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmeGIdA3UQXiiSFbhYyWGjM3ptILlzkQnysJevny2pltODNMwFhnDHeRXYbmmSvqTqoFWEw3XQ6udU6AcsxznIw3y6sAfbZ-dHUQvEZOrUnjm-OKkjnPpdgcg8qUaUJfje6OHpPevgrrfScEx4OzaeC87wapP6G_IRsm_R-wxZ2uxiyLpQBA2xnGcyLAwaEJPFjWsvWEgHh2TJhFMAQtrcMKoF4ha8Pu3xFoaWfNS76yUwhC6b6hUiG21f0IXFI7ACPw6LVmdMEmceoFrb5C41k02f_Dtr4SZqIGrScNbH-Q9UugGE01jnandF3KfC44cj5m-z1KY_cloD5uIyLBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شروع لیگ برتر ایران با بیمه ی
🤩
🤩
🤩
🤩
وینرو
🎲
⚽️
استقلال
⚽️
✖️
⚽️
مس شهربابک
⏰
فردا ساعت 19:30
🚨
ورزشگاه شهر قدس
🎲
باشارژ حساب کاربری و پیش بینی رقابت های لیگ برتر ایران درصورت پیش بینی اشتباه تا سقف 50 میلیون ریال فری‌بت از وینرو هدیه بگیرید.
🔥
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr23
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/27688" target="_blank">📅 12:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27687">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPVe17HymHhnEd8u-eylOve1Qj2smAQjw72qsmquIEaDPOWXNF8EH-O346i3EoSa89v3wESRNcLQkZNmFSvdVldEZCuOd88n1NDTE8H4gI7pWZM9h5UXYvQ3zxwMzV4Gc-rY-zQi8G4jxC5tDF03N_lEoOXBPpcMvzT7sU_uxK-V089Sm2JCmKZrYuhh0In9OV7vHvAs8aynvmBn-ZI8tf1iBMVv_2oIDg0IIC1Ua5uC98_9IHtuR2olPf6DqRCNX-Dr-jil1QmhWYN0qazCpKckFZpdZOBqVnxvumXEFwMEyYgbdZJb9_FKkpQYnpex757i1PWbqxB1QreAf05Z-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
صحبت های مهم فتاحی رئیس سازمان فوتبال باشگاه استقلال درباره پنجره و آسانی: پنجره استقلال روزچهار شهریور باز می شود و استقلال میتواند سه‌سهمیه فیفا خریداری کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/27687" target="_blank">📅 12:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27686">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD3xZ9GhzCfdSe4BRbD019VPkOpzIOk0Tb4FkXAKTZyK3ItxDu97xfb_6lgrNemEEPanmcBaWGHS_Z98T5TWG0ScIGat5BOXHEp2OT9kVlw6atAKhlLB3pqucqM_khQEC3lEmN9NCV0mtrXUZs3EBcIN1gup7E7JUIYyoXWJYmQahAk0uIy9UxKlHD6Ytvt70pZo3VYWge8L9poEupPibqCJ1_du2s_8ZOCYciMR_M3rmR1Pto7BMXX6GCjG26dVwN8m-Zv1Ed0GJUe3jzkz9JMcX_BXImj2EfUH4jFZ5C4lPSDbUOQ_dcTovE2d_iFMFK5R0A7hlWT6JqJb4jY_NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در عکس‌هایی که باشگاه پرسپولیس منتشر کرده علی شیخ الاسلامی آنالیزورسابق‌استقلال دیده میشه که به نظر میرسه به کادرفنی پرسپولیس اضافه شده. البته‌عجیبه‌که‌باشگاه پرسپولیس در مورد اضافه شدن او به کادرفنی اطلاع رسانی نکرده و مشخص نیست شیخ‌الاسلامی بعنوان آنالیزور…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/27686" target="_blank">📅 11:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27684">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cd0640fc.mp4?token=gNLw1tUAOh41Pf3X5AsgEMq-l92NyxduA2JrXGfPGr22526z6TAsHZEhoxXdn9pNJcsmb02SnihMiUXfu9WYTh8g20Pn7j5x3encN551-t_BBMSiCXNph4wNUhAdH-35EHTxZ0QdGAb-_hriEE1PQIz7POJF0oS4AqlgtoyGhQq1O6J-ZCqXM-a2QQ60H-92fQDwWhY1ffqfBAyxSwOmp9QzQeU7za8oj6z_4azuDWcHwbbupvvKFkdhBu6h5t2OCz2ise90AAXj4oaSVHxBcQKs_hrJYNu01roQMQNNdOkoP6yBUyJu7MAXiJbFTlTFVUmPR2i4z80b5RudlcbZzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cd0640fc.mp4?token=gNLw1tUAOh41Pf3X5AsgEMq-l92NyxduA2JrXGfPGr22526z6TAsHZEhoxXdn9pNJcsmb02SnihMiUXfu9WYTh8g20Pn7j5x3encN551-t_BBMSiCXNph4wNUhAdH-35EHTxZ0QdGAb-_hriEE1PQIz7POJF0oS4AqlgtoyGhQq1O6J-ZCqXM-a2QQ60H-92fQDwWhY1ffqfBAyxSwOmp9QzQeU7za8oj6z_4azuDWcHwbbupvvKFkdhBu6h5t2OCz2ise90AAXj4oaSVHxBcQKs_hrJYNu01roQMQNNdOkoP6yBUyJu7MAXiJbFTlTFVUmPR2i4z80b5RudlcbZzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#افشاگری؛ علی رغم تاییدیه فیفا مبنی بر اینکه یاسر آسانی هیییچ مشکلی برای همراهی استقلال در فصل جدید نداره و کارت بازی او نیز صادر شده اما علی خطیر مدیر عامل سابق آبی‌ها از مدیران تیم ها خواسته که در پایان هر مسابقه بابت استفاده کردن از یاسر آسانی شکایت کنند…</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/27684" target="_blank">📅 11:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27683">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/405e5ce55e.mp4?token=AarMwSVMN4IfD-Cvw7FnEMTdv6ggrM-NaJJKZ4NXe7Nz5-dUr9btCqMObPtL1E5pbfLzh03c2hBi0sD6WLa2CldNT4gLd8c44sooVnpvMvW-V_jNyddDmwoE5VgwFidAmaF0mT0Wr_LXiZQm7Poh9DOGeA2StdOg5KzPd-wa1Ygi9LKuH43mtrP4PTjrBdiZ96eiVK1Xrscfrhz33G4F33SJp03mQT7WuLfJSsBJH3k70G3Wf5KuSheuSbJN80ig9bex-9tiesHFdsWtUahvOPvNAf0U2Aj-k5sbdsu9VrImyP5Vxw6tVFxbG5lKL7qOkezjfMbKOtTd2mtZ1mNJLTRrKcNKrAJjqqKfrzCD5hdUWFpGfTR-ypFepWqvMsZz6slxXcd9EKr4_v6TYxWKkJbC_WjexpTkP4gfClqn1dhMuxqhIpu6mkpGS_XMhAiFYODJ0wULSB0gD5Z459lEXqFREHguvqvGIXAla604Yy_3VgNaG5NdqbVELeGD5BJQjv-3fCIfo3UUe3bsCq-9OC8mQDR4EgW7EzBBjhMg_wtyNh0hZDnbh1a77IAYUUCMp86N5zVCswMCwCUe_RSbWFib36oIVRP5qjTZo9m3pmzhqlTX5AXGSEi0hLilYx2SNkzCy6o8wzY1BZwzgp7F34pxdgEcLb-FfIeXZm6GSTI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/405e5ce55e.mp4?token=AarMwSVMN4IfD-Cvw7FnEMTdv6ggrM-NaJJKZ4NXe7Nz5-dUr9btCqMObPtL1E5pbfLzh03c2hBi0sD6WLa2CldNT4gLd8c44sooVnpvMvW-V_jNyddDmwoE5VgwFidAmaF0mT0Wr_LXiZQm7Poh9DOGeA2StdOg5KzPd-wa1Ygi9LKuH43mtrP4PTjrBdiZ96eiVK1Xrscfrhz33G4F33SJp03mQT7WuLfJSsBJH3k70G3Wf5KuSheuSbJN80ig9bex-9tiesHFdsWtUahvOPvNAf0U2Aj-k5sbdsu9VrImyP5Vxw6tVFxbG5lKL7qOkezjfMbKOtTd2mtZ1mNJLTRrKcNKrAJjqqKfrzCD5hdUWFpGfTR-ypFepWqvMsZz6slxXcd9EKr4_v6TYxWKkJbC_WjexpTkP4gfClqn1dhMuxqhIpu6mkpGS_XMhAiFYODJ0wULSB0gD5Z459lEXqFREHguvqvGIXAla604Yy_3VgNaG5NdqbVELeGD5BJQjv-3fCIfo3UUe3bsCq-9OC8mQDR4EgW7EzBBjhMg_wtyNh0hZDnbh1a77IAYUUCMp86N5zVCswMCwCUe_RSbWFib36oIVRP5qjTZo9m3pmzhqlTX5AXGSEi0hLilYx2SNkzCy6o8wzY1BZwzgp7F34pxdgEcLb-FfIeXZm6GSTI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ابوطالب‌حسینی درباره صحبت های عجیب‌گزارشگرافغانی حین گزارش بازی دوتیم ملی فوتسال امیدهای ایران
🆚
افغانستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/27683" target="_blank">📅 09:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27682">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa916cffe.mp4?token=end3D0GZougl-VaDxCVoQcCA6z1hvYZ9wrIQegeP6Vfx0UhSGt5Ahg1pJOMdznVlder3nuCNzs9oOt8b0c_bxmO73gA_56e0u56Bg1qA9YH8g6lyvQPzta7zAg6x0zKZYTbmt1j2u7YXkmT1aqC2W0Rbn5i9Uk56P4gpOZLFMBK3NRueHLYzSwy1r3J3J9CUIgyeW3A5ls8Gu9gKFEPTqtX7zX25tjoLK32yWMaUmuKbs02OoBMdxpNTlvVgAg8VLeKWUAcP-BaZZLzSXZ8IC7Sj3xAXbQu2Hl8J_5ga6p1CL4FJTkgO3iczG6G3zsjVsHHZVdrAIpL5tukftc5sAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa916cffe.mp4?token=end3D0GZougl-VaDxCVoQcCA6z1hvYZ9wrIQegeP6Vfx0UhSGt5Ahg1pJOMdznVlder3nuCNzs9oOt8b0c_bxmO73gA_56e0u56Bg1qA9YH8g6lyvQPzta7zAg6x0zKZYTbmt1j2u7YXkmT1aqC2W0Rbn5i9Uk56P4gpOZLFMBK3NRueHLYzSwy1r3J3J9CUIgyeW3A5ls8Gu9gKFEPTqtX7zX25tjoLK32yWMaUmuKbs02OoBMdxpNTlvVgAg8VLeKWUAcP-BaZZLzSXZ8IC7Sj3xAXbQu2Hl8J_5ga6p1CL4FJTkgO3iczG6G3zsjVsHHZVdrAIpL5tukftc5sAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویویویی‌جالب‌وتامل‌برانگیز درباره داشتن "ادب"
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/27682" target="_blank">📅 09:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27681">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc7f8a7f15.mp4?token=YKiRcoBcTX3v4GF2opWg2E3SwfYhHgCAdrMs5ZYCBMwBAtSDWKespLp9fNica-jR3ExJ4009rSAomdJOIqNEaieJMQYLd2FDgrHHAiz20xiiiJMgQt40bdyfpdF4JZ1DYCSIIQaW6jQg424ZsBNDVI8ZwaJaIzsSJPfDisIeq6667GZqBz2_bWDVC0Z9-sVkaNfXN2jzit7MzbDNnsB2X1XPQQp-HvBLO8Ku7wDEXQ4cxSMfrsHDriGVaoK6xL-K9qwyPvQwx0n5ZUKYXa7juiFw82kKMxMtkQzWEtc58obR9-f7_DNSS9AQaZ-jGZCSKej-p5HHzUlV1RUWYIbuyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc7f8a7f15.mp4?token=YKiRcoBcTX3v4GF2opWg2E3SwfYhHgCAdrMs5ZYCBMwBAtSDWKespLp9fNica-jR3ExJ4009rSAomdJOIqNEaieJMQYLd2FDgrHHAiz20xiiiJMgQt40bdyfpdF4JZ1DYCSIIQaW6jQg424ZsBNDVI8ZwaJaIzsSJPfDisIeq6667GZqBz2_bWDVC0Z9-sVkaNfXN2jzit7MzbDNnsB2X1XPQQp-HvBLO8Ku7wDEXQ4cxSMfrsHDriGVaoK6xL-K9qwyPvQwx0n5ZUKYXa7juiFw82kKMxMtkQzWEtc58obR9-f7_DNSS9AQaZ-jGZCSKej-p5HHzUlV1RUWYIbuyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27681" target="_blank">📅 09:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27680">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGS5nNYX9F8efzqb4utio77IB9bAPXp0ztwaDDBSljfIZoLUWg2tY_x1FZgxsUVkvt-rjhno2G2WZDCVf-GjIUlmUZNRsku1ALHveVmrS6QfnUn55OO5j35IsgP3WJRIErJo0Q752Jcz8dX6_-pW2Y1nSAaaXJuknAGjDHLXgZngCqNq6-rpH3mFonIRZ2O0hP_t97rOCrT7-eHku3xPr-sHIeNUxbW6TkScgqvaEqhGI9jzwncCTIiR-uMVztO1pqXTRp-sHupqX3Y5kKa9me5FjpIVVFG59eDenYkKpxMcsNqBlRekWzp8zTPn-Pc4UXdtFEBHV3hRX7Uwmiwn1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
سیدمحمدکریمی، محمد عسکری و آریا شفیع دوست سه ستاره سپاهان دیدارهفته سوم با استقلال رو به دلیل مصدومیت از دست دادند. این سه بازیکن فصل گذشته رقابت‌ها رباط صلیبی پاره کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/27680" target="_blank">📅 09:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27679">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea083066e.mp4?token=H-lw-0i4-LeY9TC23FjGrDvEb-AR0Bl9WSpnzc8ynAjQWsVGN8fV1nLmK_lBbqvpVKYpIuAtmZugom86U04OkmlF_RxULOYqdi5W-c9r8qnZ9UIyh5pnGsfLt9S-Yc-15CHruv9WyKi6xNpeg_YkTe0neKW8sSRvh3rHC-NnM6-7u4-E3zbcsqIrmdgiQ4rguZCAh2zIBL32rGhnIDShxLWq08JFAd498VOZ2hAVyl51Eyr0QvIhGdeDwkZNdvgZitwDstTKcSj-03R3UufSpa6H-z5kzpDFrSOZhrjqksMnEJcBNK9rkHhGAQ6ufYTFX-uQGz1zyvtPf-0i_cFRKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea083066e.mp4?token=H-lw-0i4-LeY9TC23FjGrDvEb-AR0Bl9WSpnzc8ynAjQWsVGN8fV1nLmK_lBbqvpVKYpIuAtmZugom86U04OkmlF_RxULOYqdi5W-c9r8qnZ9UIyh5pnGsfLt9S-Yc-15CHruv9WyKi6xNpeg_YkTe0neKW8sSRvh3rHC-NnM6-7u4-E3zbcsqIrmdgiQ4rguZCAh2zIBL32rGhnIDShxLWq08JFAd498VOZ2hAVyl51Eyr0QvIhGdeDwkZNdvgZitwDstTKcSj-03R3UufSpa6H-z5kzpDFrSOZhrjqksMnEJcBNK9rkHhGAQ6ufYTFX-uQGz1zyvtPf-0i_cFRKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌‌تند رضارشیدپور مجری‌سابق صداوسیما به‌‌طرح عجیب بنزین ۸۷ هزار تومنی:
هروقت درآمد روجهانی کردید بنزینم به نرخ جهانی حساب کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27679" target="_blank">📅 01:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27678">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boeMnTu2CmcsTUsWrzvZw9X8puSTpjxu0q1Wyqi5yPtA0VyAzrGxeIFQk_9mhvmh20Owa_GmrAhkJ3gouPTCPKiIbZF6yeAk0Ss-jKlcaICNY2mmLG_RtCVcRov0i9JDACRMZeDBO2z4xfLFygsao9CczHRg318L5P3a1Wa5Qgv2BcdegyjmkbC4sVtG4TldXDgcpi_EEx6PtNVwJ1hMWymJT3RJoJlTjeSMWcZOYg2tZ-2-vvhpcZqEzNO5v92qzM1fDb1XyAQWl72ZUDmTjTYH5BhF9hPlcqKNafKzos-_cYQWRD9AOlb9Zv5dbrdB2PL4QNStQqZtUseCT50Mtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌امروز؛
شروع لیگ بیست و ششم با مسابقات استقلال، تراکتور و سپاهان مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27678" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27677">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoH33n3uJSgjp_KPNg6F5BwMY0J5Vs22k3mMMNr4_HQ8uyewGfMWcrZKQjTuzdQLqw5esa6CvDzcisWY3B3T8Y80gtqdcd3yd_SpX2ydZL2vPINOOTyIOeghYTX5JyTzCRbjhGxcHto1v7OZocDakJb3raicqK-GJ6eZ5F3LwbFR_y5CbFGcLVXLAdUcwTd_cHdsjcKS0uBoKw5EWmlJWQuJna00VeiqCLXOGY7YM2q1SMmc-hGpVpPJWfoA75GscuJCDVFwMwWjCdwuYZiZRTd5KXmfAtlxAAJNg-wrCa2OrKG8G8bGPoaT5fjNt8UPrii_uknfQ1uAyy1hALrpVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
حذف‌زودهنگام اینترمیامی ازلیگ‌کاپ درحضور یک‌نیمه‌ای  اسطوره لیونل مسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27677" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27676">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H625TuxEfg_UCV-cN5WyvVM0uEvVqzgrFq2S8R_66LSM4qxhlJ9dP8F95hdmHTFQ8ipEzQlxKCCXz-z316DAkWSAsz8ugNIKa4pUYo6YVHwvEbqOsF6SNZGovvWbbks-DCdTjBUwBQd3niOTd_W7r8vJfkOGN3N1tgIRH7y7FUcMbirEmGC6VJMW_iNM7NOJ3kkj3gUQ97m7TEqHtDKzp73GpnALyv8XejKd2dPDhMIpYJLrtxpxE8LXXdrsZeYyi6PbWSIqKj4nAOtiPaoAMAt1DFR3YMpO3wxhSTlnheUtLgQk7OmY7I6sF--7iXmiCePjaNRUQVx6zq2kyiZGyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تمامی قهرمانان لیگ برتر خلیج فارس در فرمت جدید؛ هنوز تکلیف فصل گذشته مشخص نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27676" target="_blank">📅 01:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27673">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQOjHerl6sJkQNhXYCNZQDi6pPv9fEqny_IJQMZhf2BUlskSnmrbtoVaDB4LG8yCgTiUFpSAgWiDBJ2hEYM3pMmrneTpta9CKvzIAEFzWUL2ORffZipkINCRi0NPKqfajzUxEuUxrTqyAkY9QA33JtN5TJLLcDJKDNH8RKB_u3J9yS9wXl5qAW71q72JSrVBH1vYC6BJ6g_9kM0oHYGJoi5P7Y3k2Xj2W50t500XzXuPp37KUsfwzWnYOgupvxCaDDmhdWds3QGhrsvX70VPiw-q85U5WOUOuLupEPeTLQGQonjBPWYUpb8cBDDhfYxLmJ25qxQyJ_BJzWTfhsVWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fe1ugp_URsnAPZJvhEtJZXbpS2cl3oi3cOYih-q3QM1zqO8C511vPPRyOStuqq3Xlg8iNR4OkYVCsOGBUhygOoq9Ccydv2pt4-SPid8sxVSyg_yMOiwuVvj-yTcUfJapvne6KSJ9t6DUNmTzGDs5KGgeNFDTz8u89RCKFSfTxyJ2P-kLzW9Il7YoOe-7XiajYMaSFFjMFka86-ciGsurGSk1aCiWSzUcL80-wkCy6qtjbBHprPzjhtWHduTJGxDgfXbSq8OJ7he5Eg4EGZzPs2_2oKYQIV8TZmLPf5LRjG77FziFfR-wVXDU8nIo1qAmPnH9rF05Chmr7r2NzGANJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
🇪🇸
#تقویم؛ سال 2024 در چنین روزی؛ رئال مادرید تحت‌هدایت آنجلوتی برای ششمین بار در تاریخ خود قهرمان سوپرکاپ اروپا شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27673" target="_blank">📅 01:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27671">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/op-8QU6u_byo7HFWRN4IUAkpdFuQWR2qDaHdnBNKo0jqMMJ-hIywM6YkumJUbG0FxIfd0qIfvV-GgeCsh79GsKLjjVutt3pU_rzglJMYsRAsIzXgax9IfHhX8sGrofiP5dWuWWoiI9mTX8wgGQlMtuAJO6bkbkWA8YUDPkEw_b54WUf1sF8GlcTUpOyEUzFB9GjDhKXjmJt-MRosuJVijWPVRjibMUh5clsVPJyv6wXd0FMkB9ZXbJjLVbtJaSSiA-MCYZLiPJlN24I8arcQhYZ8MnrnjqEqhc35Xat9VBpTfB9VAi0gOa6_V6f0JzbQwj0OkUsUALQeyU-pvVne7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6583225e2.mp4?token=g3By_mQ4Kps_YdNTJo68OTaLz0ZJ2KWwYt9KzbNEbim8asMEgT5n8QsRhNyD94Fy6ibs4QgqBN_sHkAfWnQ_9RFR7jDWK11hKe7oPMOCezOkV-ldrgl9t8Qt2bCM2TWVFOhi3ySw533sQmH81bEn6C_54TMVMO5HgsiPl1AeqOdX9GYSuxRPRRO51TTeEWgzv6PHhxIbVVKTv-Ek2RXrDmttcG03QjmEjd_QWVfofDA4WygHuLUzg5b1WMEMOMB0nRpoOkxdmbvtlLwmJgsbrkGAqoJw9nNg6ZNIp24gvJqUsatwpfhf7vKuX0ueDuBrVOqKFCvmEjZUbxsJ1ni0sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6583225e2.mp4?token=g3By_mQ4Kps_YdNTJo68OTaLz0ZJ2KWwYt9KzbNEbim8asMEgT5n8QsRhNyD94Fy6ibs4QgqBN_sHkAfWnQ_9RFR7jDWK11hKe7oPMOCezOkV-ldrgl9t8Qt2bCM2TWVFOhi3ySw533sQmH81bEn6C_54TMVMO5HgsiPl1AeqOdX9GYSuxRPRRO51TTeEWgzv6PHhxIbVVKTv-Ek2RXrDmttcG03QjmEjd_QWVfofDA4WygHuLUzg5b1WMEMOMB0nRpoOkxdmbvtlLwmJgsbrkGAqoJw9nNg6ZNIp24gvJqUsatwpfhf7vKuX0ueDuBrVOqKFCvmEjZUbxsJ1ni0sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🇪🇸
#تقویم
؛ سال 2024 در چنین روزی؛
رئال مادرید تحت‌هدایت آنجلوتی برای ششمین بار در تاریخ خود قهرمان سوپرکاپ اروپا شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27671" target="_blank">📅 00:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27670">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnRl44Ye1Vcy_5EkBJCL4QM0FRDkY5UAb51hmpqxKXCzbspAkjwkd1xdj-DmSq55AXiLw09qIdyMUA9MJdWsww_SraN58YkLBZXZSeNujxCgdZkwCy0vEYyZYX_BafFkjEtt9wxO348KBqx5STsQ-z06q30PdlfuOhMNNoKrtd3FGPpSWST3XDs5fRZLyy9YoAi_NSNpgjDmcdTbHEUFkEE1-YRAJZIALgo29IzxuM2M9KOkRwmZD3ThKPSlsjLkrh8a6AtsvkGN8-X0evA-t_Axn-wdKKmi_o-rvdVVvNAHgvluIJVEVIlnO8PyksbdLS0pkjbGtQlyFBZCypX4yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛باشگاه ریوآوه پرتغال یکی‌از دوپیشنهاد اروپایی محمد محبی ستاره 27 ساله سابق‌باشگاه‌استقلال است اما رقم پیشنهادی این باشگاه 400 هزار دلار کمتر از رقم پیشنهادی تیم استقلال به این ستاره ملی پوش است. ایجنت محمد جواد حسین نژاد و محمد…</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27670" target="_blank">📅 00:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27669">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88b1013a4.mp4?token=IPu5QO3xD7ukBfXH0aA8y72UyKhe9OWsOzUP9YdXnsqQejMeyXSW2qhSV12FIe4jojKY0-imlpa_4rjLJ98hqZpEFf6FUklZD0mfL8GlcsqfUwj7qrd_VEaUhkxYmH6L9PpX6ybGki98U09wOUQsWXY_mN5TiQZIdZz0TOs2MPbh_k6atUEac54TRb3faft05OCMAq0QBI649MJUvABZtJZL3nCam00n4k9S0II1p76tGFaGQKyDyCW6YW5A-lXZgTp3qYK11a7eApUQa5XxMBqULydLwvXA57WudKHpoLCrm9xASn8UUETmGSEqNvjQGKlHHAdnE_pMEaSsKBuQiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88b1013a4.mp4?token=IPu5QO3xD7ukBfXH0aA8y72UyKhe9OWsOzUP9YdXnsqQejMeyXSW2qhSV12FIe4jojKY0-imlpa_4rjLJ98hqZpEFf6FUklZD0mfL8GlcsqfUwj7qrd_VEaUhkxYmH6L9PpX6ybGki98U09wOUQsWXY_mN5TiQZIdZz0TOs2MPbh_k6atUEac54TRb3faft05OCMAq0QBI649MJUvABZtJZL3nCam00n4k9S0II1p76tGFaGQKyDyCW6YW5A-lXZgTp3qYK11a7eApUQa5XxMBqULydLwvXA57WudKHpoLCrm9xASn8UUETmGSEqNvjQGKlHHAdnE_pMEaSsKBuQiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
استایل‌ومدل‌موی‌جدید رونالدو بعد از ازدواج رسمی‌اس باجورجینا دوس دختر 10 ساله‌اش؛ ویدیو ریپلای شده هم ببینید خیلی سم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27669" target="_blank">📅 00:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27668">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7E0k3IOPn5uasSgIAOTkIXU-cud2vKhrTWuWvDLfXwgRA9iKud0VBxzDEYrzYyrB75eUcHNOrOrg-vJ0MDAa0tHNwpbHUOYXPD5p7YdOQL3dejc9MLORhrY8T_PocGQyhADFuxVg_eY6dMgYxdSIUH7hhLJtfXj0hLC898pCStF7WMfYCBNu2mnRqCsOYVuz2N-M9XAz_4z8anzHPZC3JWgkfZnUqisWUY2BGvsUmvSTvog-268OpciFHY0UKGm9kHlRcYg6sAHtSet5jXDqe9__sXcVYznRBfZvTpf093JxL7emRLIkBmOHb5sIKK8Ap-CBk-vJf0uy3pNnKQtlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27668" target="_blank">📅 00:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27667">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CDfPv9T1DEnJ7LZUH_fhe2-fTY_DMqL4hgkPNQ6gr8UN7Jg0Sd1Rd6pnQQujaJ3JfdBk5pvn78wBHAxUgcBEY706KDGtFVdEBflp1-w5NWVK9iWnYIJGccdGE733uje27Y6iqAx1MPmB2npO4nsT6LziuSkkTLoS395beIRGkV5kaisSW1sjhaY7DNgtv3-4jLwJ2vbseCp8z9PS-j3lhXAYGbJCiIy-PQpSEYbu9eGjo5Mx4cfyN9Yqh0QkvXs6vSwuqRvoYgBwMHigrE6NRW_qPuNuSPehWIfgBkIXi-SElGc--AKv447D4MhiOxH88tJRkwXfzPMMRoSmxYl1eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ محمد قربانی صبح امروز از طریق نماینده‌رسمی‌خود به‌مدیریت‌باشگاه پرسپولیس اعلام کرده درصورتیکه تاروزشنبه پیش‌رو رضایت‌نامه‌ام رو از الوحده امارات بگیرید قیدتوافق‌شخصی با تراکتور رو میزنم با پرسپولیس قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27667" target="_blank">📅 23:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27666">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🔴
رونمایی رسمی باشگاه پرسپولیس از کیت جدید خود برای فصل جدید رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27666" target="_blank">📅 23:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27665">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/keXq9xARmGHdew6ssJt-3KPiyuAb-1jgdKCJ41SKwQlgA4ZpSN98ylad5EMqbQtKj5XD5gXXfwaOXNEHTcMYGP7CGPNnKGBiatkYxNSAreqSCD1UmgxDe1mUPgyBYgvKd4xSrkCzm-lFfGV8rIaLqRtqI5Rnjs2IG1q81lo1jlWC02LkpaYf_CX-3xFr0AIOcUfS_Ov7o1x6_cNCK4jxQJjZzRpsRvHQWWcYND40qEsJoQFv-HW-YjQvqErxwawKjNrWL4srjM6bDZtmLD8wFiBpKuXdO_Au9M9dH3iGmoYfqLre8hVKXHvO3QIR5f2zx5d2RQGjtCAMEoRTM1KKgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27665" target="_blank">📅 23:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27664">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUTNmP4uzyx4yz5WLz_VE6lTLv4F-BdBBwjHcpwTM-hv_RzlZv9qwo02hCQQah5XK7s3qm8l6zJE7vIoZF-ixcsABgLD3vnxiTAblShfJckM62MgHPCLltWoekoc8BdMvABWdJ6tw1Te4cl1KCW52Gd01zp2KPIIZw1h1VKZ_lmNyu9XFu2awxTMQFepsi4aK0preZmQXJTh55Aw_A0GyFWlKOTqsYQV-3q8fUwjRVlrdHu8T4u5pYMVCr7BIsS6-yDL7XD5Avjd1iCpqlZOjZv5jb-5o3RRaHVCPOZA4cG0ExzzIz05WBrbp2-ktQ2DcdOWCaex3WD2jBB4mrzOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ علاوه بر جذب دانیال ایری و جذب احتمالی محمد قربانی؛ باشگاه پرسپولیس یک بازیکن دیگر نیز جذب خواهد کرد و پرونده نقل و انتقالات تابستانی سرخ‌ها در این فصل بسته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27664" target="_blank">📅 22:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27663">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5zes3r8-TlX6nXhEv-0T-Nz9JUOySDyRKTiro80yS9UJdl9z3w2WhvDjV5jfFLjMNsUDA9ytkwdgQpvMk4TWTj74xcP2wzuFM52KECpn1wCVRxUt6BdrYifjShYKum5lhQmna552wtY7imZlQrrorejX-wuvwRPxLv67yZTnyJG4FB4GrqxJ21y-CnBGxtJ-DfGeoyFogxB8mQPJgTrdMosUN6Wk3d8CUXk-ALD3h2ldpXsDiBenSywCOHXrG3kvFVFa7TQCsyFpVx67rof_-Uto-0Iblv7UInTg81nZG5U-jsTQGJBWBGlN35Kxs_tSJkKevq6E-g6d1RLyVYkXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه‌سپاهان‌که روزگذشته با کسری طاهری قرارداد امضاکرد به‌خواست‌محرم نویدکیا بار دیگر از فیفا استعلام‌گرفت تا مشکلی برای این تیم در شروع فصل جدید پیش نیاد و با مثبت بودن استعلام فیفا از کسری طاهری رسما رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27663" target="_blank">📅 22:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27662">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b52oxodRmveKFgVC49Xgvk32x2RTIfDKghPA5MCoQB9iy7wz4sZK-JhG-yCqD3K2Y-mO1VdqOz7T5nG40B8qYyvz_uInk_spOlHmQt7CyxFX2ezQS5mPhWHFdUCSDOIvGPWtbkAErqK4ooy1NzwNwwKDlam0I5MxDCAKYpI-UeGlMnzKOlHYvp5fMVvE5pZg3dsOC_5LuwhgrOz8WKGUoywALx-4lygMYobQSOJByfGd7szX6mXmuG9dfyn6BaU6cVVBRcTFtmrXagwrB9edfRmQ_AiGkjbmR3eB0or-Z30zV_s2KSBvfUz_jGjR4jTAsURFcQhHbfyNcZjkd3ttNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌برمهران‌احمدی؛ روزبه‌چشمی و جلال الدین ماشاریپوف دوهافبک باتجربه تیم استقلال به احتمال زیاد دیدار با مس شهر بابک رو دست خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27662" target="_blank">📅 21:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27661">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A60wUiuRGYW1S8N_XQOvv3sQr27-eGihb4dNOr35mJHdmMl63dOA9jJfq0mdCjVnsma2fZyQbTrMHsytkGj7l1GyEBZYgpFmevkrlGeziwZR_rVdbsiJtgYpAwp8xmuO-6lBY9NIlokdwlCjGe7c3vEVAJXpHVN3RETdWX3_Zfi3uXvppHglYaOdyfXKtB1jtutyW7shHnqnzDdb9x6MeEH5RKhZoqnC5D2WQdYWQaSVnq6Z-4YIcbnP6ZrPJJnJKD7ldcwViCaWlsl6vRgcSiI_4DkNhJKIixssbUWbEXuFIkY8mXF15GzErmtMg1IDMEtR6vZGzR-q0z3Q_3sb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
#تکمیلی؛ فران تورس مهاجم 26 بارسلونا با عقد قراردادی چهار ساله به پاری سن ژرمن پیوست. هزینه این انتقال برای پاریسی‌ها 55 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27661" target="_blank">📅 21:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27660">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2QPsjuD4nHc5UCd0h_UqxTXNe3q058f2h9kea19dWDRWQgiFcnccmQMtyXJBZ4-cFVml6_YEEfklJXo9XUT9Yjp84n8PMeAiimLXWLPMbrNLWKMOO3K0GOmIaGVCfxhQy1zwk9x1M7p-XjLS_iGc5RgIDV1_BA6QZ0mW8Flk3YSVRKFyGELXobfnvvpX6Ni0FOK3d7zAhYx9XdcByEL1GIpJMEq0csLYVqoFLF2PJgxE9645Hz3b0syB5cWdNr6ULvWJbewOW-JHzlkxoxpDUIhtRqdgJQiyfpvE1ROuAPaOeN-N_aFxQHe7hGTGwfDMGzYEG9wxuVZO-TScy7TSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درانتقالی‌برگ‌ریزون کریس رونالدو به شمس آذر پیوست و برای ماه عسل جورجینا رو برده قزوین.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27660" target="_blank">📅 21:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27659">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAHPa7nztbqw8rfv-mShEMK-gIm0KNCoh2QRhn3cr5TjfZUlqnSHGwLURB81jJIpcuTu401lZPCLY7Oq4qXZT2wGWdELWdFVbAHL7mGod-2h58cbGkJILld860cpwcfGZsjP3F2pJxOrbB-EOspognstB7ZTHPTWOCyY75254biwtKfVUAe5WF86Uvtg4QCc-tNY8qwrGplhVo7Jyp_6LpwVnz81cYVOuVEqEpjOsFWIRkxAbk0VD1SKFH5yWdSv7mmTB4qeY8WM_8LFeqgUmU4Memh3o4_jAJdqSU04n1dzFk1vBJr59aIhv61GHG37zRSjqlJsYmSCsepx8jCJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی رسمی باشگاه استقلال تهران از کیت اول آبی پوشان پایتخت درفصل‌جدید رقابت‌های لیگ‌برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27659" target="_blank">📅 19:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27658">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9da1140dfb.mp4?token=u7istISCszOqVftUcD0Jhh0S7sS-fxHDObheQVWy3QIO9pmeh5CFcGeNuR_d4UoSplqseJt75N75fQ-Y9PkbwT6MCFZ7vgm4rSMk0J0WtsiPozOLeUdfGDL976bJoQmYJUWoDmAzWpYRCamyk7WKkrt5eHBJ5_8bZzcvnvGdWwJ2VW1WK-mWvyNrA2TB8R8sAfRXogQgNHmYUFyU04_2fZjOcDCuI_yXpGFowSVQCBTE9Vhoy830MnDb7MQ6zU0LP_l0MRK6cOW5-rt6-FC3xP1B6TWW3DTu6Y1MqJamVBtwULdzUyddANlLZ5zTnltq4wpmy2NPCds3WdoCQeCTlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9da1140dfb.mp4?token=u7istISCszOqVftUcD0Jhh0S7sS-fxHDObheQVWy3QIO9pmeh5CFcGeNuR_d4UoSplqseJt75N75fQ-Y9PkbwT6MCFZ7vgm4rSMk0J0WtsiPozOLeUdfGDL976bJoQmYJUWoDmAzWpYRCamyk7WKkrt5eHBJ5_8bZzcvnvGdWwJ2VW1WK-mWvyNrA2TB8R8sAfRXogQgNHmYUFyU04_2fZjOcDCuI_yXpGFowSVQCBTE9Vhoy830MnDb7MQ6zU0LP_l0MRK6cOW5-rt6-FC3xP1B6TWW3DTu6Y1MqJamVBtwULdzUyddANlLZ5zTnltq4wpmy2NPCds3WdoCQeCTlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎮
کل‌کل‌جالب‌مهیار حسن و مریم ماهور برسر بازی پلی‌‌استیشن؛دختریکهPES و FIFA بازه‌اگه‌زن زندگی نیست پس چیه؟! تو یه بازی هفت تا زده مهیار!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27658" target="_blank">📅 19:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27657">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cfa38cc4.mp4?token=UwWJ8EZ5cgQO8INg-qWal1JPizPghfMyY4arTj-PXbGM3JLT3LRynF4EXCSl_fkGCmInEOj9XA1Dp3m-x6jOxJgs4RHNwEk1UMndCQobcnedq9M_TEm2RMLlHO_kbg__yHTQfVuvsV0WwPsFSR0Fi61MLq0gnPeSWDvH0NcrPqW9w8hSWIlfHhn8_Vpb3hW2JM5DfvBaQyTujqjku42PCZMmFiSLh05owz0mUTVvfIUVASo2Mw5nU3lfDJsYZS-d7QJR8PgY0oh-DidV2sOcszdprO92MqHx42uLSuSmSWK6g9m7RPivBNW6Z7DPBLH_GtF89465Q4NcphFe6_q35yBYNAL4fba-S3G7a8UfAHRCvDMw9bQdpzAgihJuV6Ryl6wbMMIOqDfX5cTNiMbn2r-9WGlHn8EviVtJmdHNLMOlGHtvfxRoWN3i7_tHEVpkPI1B5t7vvSH1w6oCrdKIhlTMbHDmmCf93UKcIEMZ4KopSGCLRpUjHo0hlzyX7aqCHhJmlHf4pj9neC9rQ4jZ-fkbAi5jpg4uSlaiiAtOVna-g8nLbqW1AfKZTUXn4i6UgKlOMfZTNZeMy1_aOB8_6pxRSMryDI9fWdqhj5U5SfTbmwwlVxe50xF1YwOXhz_51fSrV8Q5AVUKL2yicVSBXfbUd-KskqBfjzzdQgPbr4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cfa38cc4.mp4?token=UwWJ8EZ5cgQO8INg-qWal1JPizPghfMyY4arTj-PXbGM3JLT3LRynF4EXCSl_fkGCmInEOj9XA1Dp3m-x6jOxJgs4RHNwEk1UMndCQobcnedq9M_TEm2RMLlHO_kbg__yHTQfVuvsV0WwPsFSR0Fi61MLq0gnPeSWDvH0NcrPqW9w8hSWIlfHhn8_Vpb3hW2JM5DfvBaQyTujqjku42PCZMmFiSLh05owz0mUTVvfIUVASo2Mw5nU3lfDJsYZS-d7QJR8PgY0oh-DidV2sOcszdprO92MqHx42uLSuSmSWK6g9m7RPivBNW6Z7DPBLH_GtF89465Q4NcphFe6_q35yBYNAL4fba-S3G7a8UfAHRCvDMw9bQdpzAgihJuV6Ryl6wbMMIOqDfX5cTNiMbn2r-9WGlHn8EviVtJmdHNLMOlGHtvfxRoWN3i7_tHEVpkPI1B5t7vvSH1w6oCrdKIhlTMbHDmmCf93UKcIEMZ4KopSGCLRpUjHo0hlzyX7aqCHhJmlHf4pj9neC9rQ4jZ-fkbAi5jpg4uSlaiiAtOVna-g8nLbqW1AfKZTUXn4i6UgKlOMfZTNZeMy1_aOB8_6pxRSMryDI9fWdqhj5U5SfTbmwwlVxe50xF1YwOXhz_51fSrV8Q5AVUKL2yicVSBXfbUd-KskqBfjzzdQgPbr4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تا ساعات آینده دو باشگاه استقلال و پرسپولیس از کیت های جدید خود رونمایی خواهند کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27657" target="_blank">📅 19:32 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27656">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiuKoeAeKX27_iuRKMYt3iPTAhuHwhE9kfwpcQTpLKLqtLQOfTg7Essg3vN7YmDg_TRDN16GqTd489RChFuVS25OwkE0WLP3q2SKD47Qd9QKmy_GV8wPu-XGfBaB7snDH3Qog-UZYmr2U2RS-ZbNgiOMYzw2Hax9DX9iowU_e5Aleyb7DfDy3zxgkaLzQ5Sp7bjMMUy1dUH-faKHuEIkjJrkXxQs8xeU31qyGl57MqangdLTp36Tr_zRvIUPO62bqKq-BRCN3yj1NpnFg5ZvO8k3gFB-JqzogWaCbTIuKEypM9MBSHDQTNwi92p1VzkyxCeus9hfdOo2rxJDLLvHfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
طبق‌اخبار دریافتی رسانه پرشیانا: محمد محبی از دوباشگاه اروپایی آفر رسمی دریافت کرده و اعلام کرده ظرف 72 ساعت‌آینده‌تکلیف باشگاه جدیدش رو مشخص خواهد کرد. حالا اگر با هیچ کدوم از این دو باشگاه‌به‌توافق نرسد احتمال‌اینکه با استقلال قرارداد امضا کند و قرضی راهی…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27656" target="_blank">📅 19:27 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27655">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vm2GcYA2M1yjlpEGSeYCDSy-uBgbcyoSeVYfz5yLwGTfmtRGUnIdyiI1S_DKBXTZHvsBwJrTW15bIwbVpxHxxNpCIaCUXsKgEWyVXSIF9xis27jifZE5xaZYSfu1erd377CTntTEcAb1giwyrtSxtX8-1vR_K2qNng7ElrAJzMpT6zBgrjDhJgLIl83IzjIGfTAo76YpnkWJoN6M2ncVWONEQh7reSeI2nCKycGAlhrc6P5QLYoaTJm-pyCaTJyxMwVVSnexLqFZzbnJA7xZu_qD6wep4HPG76al_bTBQJXFYEqKVdzFScDT_7KzpShauMDtI_I_2IXb4gJBN55IqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27655" target="_blank">📅 19:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27654">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjc98Obbh6ePppQ40-vIQaFzSM1M129TARZlF9UFBcyDEfldwKCnhjYYM9j8fsrUIDFH8xwloebXQ_TrKiDMyS0D0M1ih7yxBq9c1CeBWJeflYyRh6a5W9jRo2S3_-p5LUQzZCBbkj7TT0qQ0ul77ZHTANwedMu-vRWBORh_pmhf_md_T5W7RescK4YhxjBZVRvMSgSpsOaxR4-EjR-lmB9CZpcTkS03oZAfdgntKEXtfjvxj9E9w76VZpr-TqthjqoIx4KEFNua5Jj67GDtu1R6sw_ETVvnHAalMSTQBGCj1S1CewFQOrjPrjxIGFh3LmFCPDKngdyGxJ2UQNNvlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 ابزار خفن‌وجدید هوش مصنوعی که سرعت تولید محتوا برای اینستاگرام رو بسیار بیشتر میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27654" target="_blank">📅 19:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27652">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxG6dj3beASdCYE7rpXFF5ZE_ew6ZQ7FXQM9cR-Jc95zy5b_TskkBAGFH06eqYOu2Aq5a2HcPZCKuFYZ1Ub9is4FZYc0xQmSVUXV2LjEqwhtbIZfSXXuqpFqdMcNvhsPbVAnW1R7qDWVT-bd_60BSeHd-fxjMo-IrpTwYlooXlEZYS8eGhjwvoBdIuCT8D6QLGtXJnrULjysM-UbnCPehmL_twDY8DZ_2iTPVNr9fz3-JWu0BceF5GQa7PkapnWQpuvk4jTBmT4OrgBrQGBqNO0EoPgWpUfOAXd1pmSfVrWqmxVD6XenclriYml1WHnErzd95AcBHhErvjtAmHIzJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
سزار لوئیز مرلو:منچسترسیتی‌پیشنهادی 120 میلیون یورویی به چلسی برای جذب انزو فرناندز ارائه کرده! انزو مارسکا اصرار زیادی داره که این بازیکن رو به هر قیمتی به خدمت بگیره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27652" target="_blank">📅 18:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27651">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPrXwspJjOuSaBeuTA11bkU9hT6ZOJNE1qKJsZF8ke-alimKNexe7guloFERaJWwGeJFrR8QeV2wjM-FZBCktPAaq1LyOJ3AM_a5jpF5W754kbc5n2dzlZ9WkQOj1kAGKnA_XwXs3_ilYTtEU4mITv7Fu-SzXJAQ_PkA40qpElI6xfyh3i54OEpcB6SQMcILeZGUWMVKFStZ2EIWeCtXxdRq5J439I_RoUipyw5jaNqIjNiqM_7hJ0zjpGUaMaNA99r9quAhzfO7pVzg9elPZDJbbH39JHQQd2ORb5PiMtA0iVHvwTSK12EnENV0Lk7VmPmuJTQ158YvhdA4j6KKhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27651" target="_blank">📅 18:13 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27650">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKlSGiy2UnZOOUXISQvkJYC26YtBATr8CNCba1gFU5QfcSTUO8urgVnwn2BAAbACRE6EcU05GOVRahKi5h9Yyx8NDI0cE9JlBSom0gofQulKBFM9Fd9Hgbj8wWouTqEuk7iTrBKe95uox5_Fz3dYozyg8qRB5jaQkvxirqj94fvPfGRKqFNYR02WVfhWoJKx6CKMyL52gJHrS__3FLuy5gLjznC1UY60ojiFxlw5O_vkYVbHVJK71eKagAlkOtI-2rN5o3tZuj3QrG_AQ8pt9dvc3uwc0Dl9ARo4UAN5fal3uPhH4DjadazOOK_1pE2UO_9Vtf-RPqjc50QIukkQvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرکت یوسف جامه به‌عنوان اسپانسر فصل جدید باشگاه پرسپولیس انتخاب شد. طبق توافقات انجام شده قرار شده این شرکت در سه مرحله 550 میلیاردتومان‌به‌حساب باشگاه‌پرسپولیس واریز کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27650" target="_blank">📅 17:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27649">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbCn0QA1C64jEgibGKZskpAmI59gSJIbjxIgVKDyBxyW6m07hH3xjnME8gL_FiFQn0IkHO3K3it9RtBWJ-1Lp0hMbn2xv3WZb4-t5Kq5-9OYE6T4GLlKSq8S4eMyyASGLlszrHyudyK4YfY_pGwG_-hOCwB4gbl5sm3gaD26uCAUO0BEWfzvzWCw2lAydGNYgiyfiqPsaCaj0N82fx_Ao2R93mCgkbq1wiXQkfuyiMWmgvsI7qywPgQcd_byGTBy1f0s4ipccVhzwVh1H9-8ufJu9g3DXmJxYPdOJ7zbmFcHtUOMZxzGJS1Um9ay6mLLSc5UwDbor5Rm2YYboQTyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
دوست دختر هکتور فورت ستاره 19 ساله  باشگاه بارسلونا در ورزشگاه سانتیاگو برنابئو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27649" target="_blank">📅 17:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27648">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIvA8axNGsL2low-J3PWPbkLJt_xU3F5W8IjlAPpkNOs2eCXi175R6VOQRmfXzJVtpTp7yIKUhMfUJeMLr3LTP6BQ-QNBXBuxcLrcHClshycBz7Y8tKBsioMizHKQIexoXAAzrEc49ClHPF2fmJhZyymL79w2t5uSZ0U6q9rVQyvYGb99o_2uVBYG7syiACXhAVE9NFct5Z8KiVtjBEAmFogJFW9QMCLzSVU9-3M7l2bS-2FFtjtmUxIjWH3edXvcZV9tdpZ4h-Qx8FO1AiX6ZKM0BItRByPGvJWccV0e2rvt72rbWwgjF69jFNFRDrfRM2W8cRFUobAYxMrCqTuIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛ محمد قربانی صبح امروز از طریق نماینده‌رسمی‌خود به‌مدیریت‌باشگاه پرسپولیس اعلام کرده درصورتیکه تاروزشنبه پیش‌رو رضایت‌نامه‌ام رو از الوحده امارات بگیرید قیدتوافق‌شخصی با تراکتور رو میزنم با پرسپولیس قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27648" target="_blank">📅 17:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27647">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kED5ne8HS5FN9LOUySBCY2i7APzmlOmKZ3M07tpfk_FuFxTX_8ccd7cOz6k_0VTPO-_5W5Z9g6B97zhQbJCemniVPMLO05c8lZhs0fD8ATXIgnarZwYdpHhadDtYGc-RYO39IiROjQX3cAZiIC99ojQt-70F_asj9TGQxCo6aoziWCJ1kNhaXyYuoCZeSLWYmR06N_vFwR7JOC99OsgZm7Wmhu9lfYtYXMT3h5NAp0MpVrAOscKEKrIvah0XCrpExpJ0s2PHFmBIcOAfj2fdUXOZZnXI14sHbI3NzyJG3AOlHNhXav0EneLmdYFEY9pTqBipRQbg_9DCmIkcbxUu-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد پرافتخار کروات روی نیمکت امارات؛ زلاتکو دالیچ سرمربی‌سابق تیم ملی کرواسی با قراردادی سه ساله هدایت تیم ملی امارات را بر عهده گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27647" target="_blank">📅 16:37 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27646">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwGVFlqc3mzQgqZb-nswkl6z2vX8S7Jc1WoppfVsGc0opHHBQkRfN9ONhK4kwlTb5TNcw4jzMg06HkB7b0JN-kZjq0r6Zz9Kge8hGHeyxC_Rs6qgoz0ZHvi0APrJ4lVVXAKaaobUzDF25yaYlYhvg2lY81qV-HNoPCnQcw5z_5UY16a7cTDxBzpU7eNfhdxo96QZ0IQkFykcAa06rz5N_FoM51nXOw4Ais_CbJaICSVq5NJmCiXLhzBerULZ5qBqCVuGnXmFf0fRZggrqa4vGL6y2KLD5GfyyjA9JWraAJIVdkHCF-IIsNhQf6ZHPXUaXlZ4mCXqsyuNL9SySQLrag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال تاساعات‌آینده 25 هزار دلار به حساب جوئل کوجو واریز خواهد کرد و پرونده او نیز بسته خواهد شد. همچنین سهراب بختیاری‌زاده بخاطراینکه نازون به‌فیفا شکایت نکنه به‌مدیریت استقلال گفته مشکلی برای بازگشت نازون به جمع آبی‌ها…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27646" target="_blank">📅 16:23 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27645">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HX_YwE3yrrlqhcOD91USlV_sMG7QMDnnTtDihoF2sCSyblJXu-ImiIRVvkIXFm5H3uVW_AWUgB6YvDGfMTyaTHrwsV5stymR864NCIgcw3dCzadgMorkYDSa4_xAvwaX2LcEyEbmQcINCNj8vydheDf6-Pv0Kn1VBAdvvt-mw4JS5gMhBvZcz6kayPZX1DhS2xEyTyx3-sz-e9Y27YIZroKihBML5u02TtoJiucxEt74ZBIGjNPGBo7FKmRJaacil8ypkbNyITGHzlL4lySAe0XkMFS-oh_IHH6Amh17SpO2UGdVA2khocnZgptf5pUoVgdrGloyGcPD1IRwebITvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27645" target="_blank">📅 16:02 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27644">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilBuzA7wGlJYbPrK8OPNpVjDF4Y-v4miOPFSYj2E7V6P7bc7f3FOmrBM3SqiIntaokK_7T4UKce7eipAt67k2If9tzhx88VVECKiMwCWpWyVaf7Qgk1F8Rh9Fh_n2p3FcWo2DHsQPOlcfNXNbscVFp7gLmmo6bGE-doY6wqEAKBh3Oe9N8VeOt6NA0cDZelRsubVBh-V7DdV0crvCA8f5ALC92g8iWOnJUt54A5xhDAFTpKvRxqEl0c83pAJl0yxKc_zU2cZ7Pzjm5MaQL1fN4Y0vq-bJAE84UnXBadgbbDuJowidOo28GxS99UxkxYguIXHZsvZ3UHHD-tq2RaGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود رضا بابایی ملقب به "بچه" با لابی‌هایی که داشت نذاشت باشگاه‌های ذوب آهن، مس، پیکان و صنعت‌نفت با نکونام قرارداد ببندند اما نمیدونست که زنوزی و حجت کریمی به یه ورشون هم حسابش نمیکنند و تو جلسه یه ساعته با جواد نکونام بستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27644" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27643">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU3nGvaTwurm2bKK94BEKKShQTP9ednKVierLWNpc7lgAzwrkRwZzMQpR0AEEQXHM1eVrt0P9xGoZgA1fIVLaOAC14tElMICAnUSgra9WtS6uncVeMp6zn5ucjFSquMSJ2cXNdDBMbR4jok3l1Z3qOf-M1JMnXJeI9p2Ea6Cn1-6ji6aTjpoK-Jm1Ru6ZcEMskeP1eDEBRZHDMRY92o9yd2O2xns9aJz23pYuedzSazvRrqi-DYGygKSLZTTuUMdfUxAww9QVJsz8qTa6-vwxEuTFgu_VvwpOyTW7-SvnGSG3hbXLuwrUHqyookLF-QiGXarAbcWqWLKxT3o8r0GJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
تموم رسانه ها؛ خبر از رونمایی باشگاه بارسلونا از رودری ظرف 72 ساعت آینده میدهند.
‼️
تموم توافقات بین سه‌طرف انجام شده و انتشار خبر پیوستن رودری به بارسلونا باقی مونده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27643" target="_blank">📅 15:47 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27641">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttbZQzajTxn9ONxx4ZDO3YuDXtQx-rctxKBMBnSVOEBwlXH1RdryVglvAUlxARIzImMXGUEAGHvx4madpOyshJg-9DcFAYjCqeljM_WGr-Q3u-cuysVtStwTu-yzy5T1oSgDdzOz-A_V1JyAzPSS30NtSFZ-V_iQfxI2SBfLNoUqvGV8gfYPJzN57y1HJ_jfZX4cgiZUSivaQ684jn_heiv9wLgIeV8U2aZmiln30ykCnAw3e6yWSzkf9A6bNEy0m6QiTlDkFCdV7_zV3nF6eQOHjbR184FYY3mEExUFXkqImeoIEC26UgRwqu4gkACBRwOkEK0SGWVu-X7yKCm1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد وینیسیوس‌جونیور، عثمان‌دمبله، رافینیا دیاز و کواراتسخلیا در بهترین فصل فوتبالیشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27641" target="_blank">📅 15:22 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27640">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXqnXB1Xc4LK9Xlrld89_pxzE5Z1h-J4CGpdL13cMeldCVr5fFGlCAfz584X0SW2ckmdAl22g7T6_NuDQEi-Ol4d4P0t99b0rK0Z_VwmwV_Dm9ak8x1hem5OZkEoSLFb96tVLALAq6_g-o5vpozFxRHH62fntYPOp3in4dpQySdzkztmeg49Zy-l22o9qxCzcFdRAPPToHczdOcQjsAuM6OMa77lMgQ5e7tV7qYyb9q9JydjN6DVVpk7jP9CcMmseXbwQX13AdIk2C_1AoJktrEO62rYAK4wWZDUMLesu-5CHlLtg5bk3UWTwstjeRACr2nkapGUZ54zAGbcEh5S_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🔵
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ طبق اطلاعات به‌ دست آمده؛ باشگاه تراکتور در روزهای اخیر تلاش‌زیادی‌کرد تا محمد محبی ستاره تیم ملی ایران که بازیکن آزاد است رو به خدمت بگیره و از مدیربرنامه‌های‌او که رابطه اش با زنوزی خوب شده آفرمالی بسیار بالایی رو به او داد که…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27640" target="_blank">📅 14:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27639">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QC2LIvJxeB9dYElNnecPEz1CJC8fodLPMSoPBYPmgnkI2TfHGcj_2tFqOJb2YAME9B6emSNJ0wHkWs0DgN6qEpPb-6c_-gLulfn0TElEgzu4KdAM864BrozpUqm53L6hrFdchqF3kwMfzGy4WFnciACP_m7Uh13w0FlRH9DGHXnagRQeqhuyHZQxqlp5tgjH7j2d-F19IMDmy4jibQ_LNQFvH7zo8H0W6GHWSolr_x-wobsgzo-RaVPjbNmxGKy9XSRxd9vq0owo_9FoSw6uNoj2iQq-qTpGgPEFPR0ilA3-6DHIZ6YUyLMvkiAAw6aLze2zBJ1HscofA56Zy4eF8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ بعداز حرفای‌دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌بازی…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27639" target="_blank">📅 14:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27638">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nve_9u-phaLuo_iYz0XGQB83RbDktoT5VATXMtkPbUGDnyEAJe6xhlHcxRSSteoTQNcvkxE5KprcvbSyTJbOZdmBON3-LPymJ5Qu0TA1A7ykyTeEw86f82vlF2dSuIaSrJJYlkisvuz0M7z7GEXtkb8fn1t7grAr0dB8cYJIpN1IMceHPYOrp361-OAZPuPNMzHvAy_igkWxBCLmUBfhu7fE2jpyC3jXhXjz75uTG9VlRhnGfUi1DzWvSUwCzWdg9_Xli1oLfGDs6XCUmTsv7EKhTjLgqTwSJfgEIdBeh3BpKX84XrPzZjT_FUS1BEkwzMeh6vMao8-5POToVpxnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27638" target="_blank">📅 13:57 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27637">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1I6jWuCC0sqdxXsgXvxehIlibAOwrMzDgs5w29UtEXxRLKroacbChuQ66aGExdJeUG6xPHQi8xSaXzj5yyHO9xPMqLqwa9mGGU0gDoab9lTtEc5cJIcbH7lDxt1qfBWK9K_6xcRgG3l1frSSOzgsNSA4MjLjJ6rBF78e_LWevDHH_Jwpu6i6CcvjCDl4UZWc7H4BtPWbhKdBNrRbbSxm2pAlbbjk3zvRgGAL9S9XvFK4F_MeTFlBMWftkHe2kC-KdsSGYS0HeMo9lRaoGBqJoW3N6ztDM87ci7k06qHqRkJ4HH_-aUBTecMW3I6W3939-75T-FiUES2UPoHuedqow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ یوشکو گواردیول مدافع 24 ساله منچسترسیتی قراردادش‌روتاسال 2032 تمدید کرد. سیتیزن ها اعلام‌کرده‌‌اند که هر باشگاهی یوشکو رو میخواهد باید 80 میلیون یورو به ما پرداخت کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27637" target="_blank">📅 13:39 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27636">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e78NsNgIoBcotPbkaHyYen8lFWcjly_ziXFcbLkWmKwJanRamjKZvRcXES-qCLqzmBXzUEWNFfIlNsQHE3iEv7aby_ZAbhXtWrBl0efn5zzeY_hQuY61uios633TgHVTDELU7NJzPKO9wkZmePv6D73iYUvjDOZ4Kq3il2zcu0rxFjqq3QUmdR3cVemmqe5oYNKCDP__tGQUSKSE_fVi12LxByTMjerIYU6GngERBv10MceaLUoYUCWeIAgMHyY49npRTxDnXd7pOjqLSdWqbuUCtwr7O9j6gqDapI0_wz31C4Z2V6XP6Q-mSwG2e7zREiybF94FxMmPuNVYMOyVHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درحالی باشگاه استقلال تمام کارهای اداری مربوط‌به‌اومدن خواکین گیل به ایران رو انجام داده بود و حتی برای ایشون بلیط تهیه کرده بود شب گذشته‌ناگهان به باشگاه پیغام میده و میگه تا زمانیکه آرامش کامل درمنطقه‌شکل‌نگیره به ایران نمیاد. بدین ترتیب حضور…</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27636" target="_blank">📅 13:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27634">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428e46d461.mp4?token=WOLY5xBo6j6Lifld7stGZBNcDWU8UxzDRu1hN6TLyqEgvHxCwk9g4IQSwr9VYa2rwWv3oL0VgM0uaHgvosAolpVYzaGynx-J9fCD4Yyh7qBbCxzCzLBincHa6KxUJg5gN35o7wcmyzYrYxfgSlC5Opx84xMmqFQOym5Cv9JSX_rAboX4vV1V-HWNDJk3ODqJ21ZXub44k5pDPiX6QiKtRRg7PvwNUcf9ILOYw3uyt94dv6peCPO5P79or0VwYhu2fecpO6YwiBzGw4OaT29zFS7DqaF1U3A6D-hDJQxI1zMcVNxk6kRKPC5bOvEOSlBKllLLXRYsIM3tYDUZCklUuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428e46d461.mp4?token=WOLY5xBo6j6Lifld7stGZBNcDWU8UxzDRu1hN6TLyqEgvHxCwk9g4IQSwr9VYa2rwWv3oL0VgM0uaHgvosAolpVYzaGynx-J9fCD4Yyh7qBbCxzCzLBincHa6KxUJg5gN35o7wcmyzYrYxfgSlC5Opx84xMmqFQOym5Cv9JSX_rAboX4vV1V-HWNDJk3ODqJ21ZXub44k5pDPiX6QiKtRRg7PvwNUcf9ILOYw3uyt94dv6peCPO5P79or0VwYhu2fecpO6YwiBzGw4OaT29zFS7DqaF1U3A6D-hDJQxI1zMcVNxk6kRKPC5bOvEOSlBKllLLXRYsIM3tYDUZCklUuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27634" target="_blank">📅 13:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27633">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6EyeFRAWat9nNQ_As-J5YH6_bqKlylFTn5JqscR5R8qSA2iG26oHRWeyQdBTh0WxgN3NsNsWet7t4w-tNdhjqsKLy-XzIpIAn1MbAa9hS4hsOwzyQxUON30CG1OYBm9BSUvxE0dkY6wKKdO2rvY7mS8ZPf-DWrIWCp7q6DQL5favcdQKe5YNcxj7avI9Fy9JC6k31w5HyzedpMhP1ilpMjhGkBRU8OR1sESkKXc75Quv2lv9w_LWRb72Zi5cOM6ZsXpRE_d_E4_3_q9hN7Y_-nQqeDF9m8iuL1MUtH6n1kkLQJuNy4TcOxbkOnnl47Bw2DjgxtLIs3jLqiqhhNU-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رونمایی‌از کیت‌اول تراکتور در فصل جدید رقابت های لیگ برتر ایران به سبک باشگاه‌های اروپایی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27633" target="_blank">📅 12:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27632">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0ry3vbYErkwkVBMoyMEwM4STTVPVj6tlF5IPRI6pT137OYzMNsWOSBTBuqzhse8Lz1l0dO6tlczUvgWB5gpjh1mKaJeXMVomtlCz61V6qhED6W55T3iVEwlRpaVRb5rNI3ZjBFk-TJ6D80_2TIWnCzoChYty0J-sF2poyc6stnEjvn33CsIUkEbjPekzfN-ZQeeoo40xaPQ5PVr42GjzLgJMl6wxwvkAjXLKOoUsUdlpiynrJatbfa6GLRaQdrN9U6hXncEex79bYkvkdtWX71ibX8pl1DflYgr0ZqKMKdAYi9iyAYL38eYOckkLjWp0GQtfDQMpLIR-Y1HNf-JKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تا ساعات آینده دو باشگاه استقلال و پرسپولیس از کیت های جدید خود رونمایی خواهند کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/27632" target="_blank">📅 12:38 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27631">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVLE7msPjUEvt7eCQ0zqfUA7yPLWgiLuKbEmthqa2TGiyw1jhrkMa-bLWdtDp1VyhXeWQobbIn4fYqP4B4oi3399Fm2BwU3INyogsw5UlSjUVfrreGhWXqvAcX4dbO-SFxRyByOzh16X7gIP_-vPAub11W9Xhpb8XtD8JKmhT3pd4542ogvIWhd7N_p3yhd-63CVk6Kpz1QnAOUONy9sBPlPnCemND1sS7HRWAlaaPqgtxWXizpfxoBq2kIU_JfaaNBQOxMJKlIq437ihHR840zrCsK75ILGqp5rhHk_WxtiZ6zRN1h0intbK2_RuMdaclpDSdF4C9uT0udnLBeteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال در روزهای‌اخیرمذاکرات مثبتی و فشرده ای با مسعود محبی مدافع میانی22ساله خیبر خرم آباد انجام داده و قصد داره با او قراردادی بلند مدت امضا کنه و نیم فصل به جمع آبی پوشان پایتخت اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27631" target="_blank">📅 12:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27630">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgk3wPuSGF_XXakznDkMaR6nGSGzYN8f_RaGSMfC-DSdztDxSVOnOn-yjzYJUVBLT9f1tHruscqrewNaE7JjABl7hxjQsWDCl6_MHpHrKQFBuatedbincXZzOlukQp85L6px313-SibtoYHvQJdWoR8_0lXc1xc-5Vn2uEH22ozI1As2QXXY7fkbIhs7LVPcYgjQTnGdlNv83hT9Slei2yeaivxHqKgG9sA8KLOOV4pJasxfih_s6ZPqZVEr-hNvF5fu1rXzUfWemwq6Xz8Q7uIsP8x6HkrpoU8ETO-OS537V18rJbnIH1r4FsGLqb_43M-Sfqo89CqwOa5ArrcixA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27630" target="_blank">📅 11:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27629">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-48_SNX15KUXA6hGNqPD-UWQrM_WGikHXlq_sLORvMuozdWtaIpBzbEpb7rqwbHFUg_haEVMxcL8kKb2MvkeSOSa1idmWRuYaSwZ1c2FLQsQGQkdA9ZuKT2smdKcChcNOmaQol0Z3DoG8jeJQePajhdZ6dCDS3mgU_CZJzRH7SM-SQlRjua4uec4XWhf_89svLemVR2uhcKaRDv3JHoi9Hi6AMNpevN6l9NPpvxJ32plj48CYnb9YRyQhM1dE32NWb3Aweo2U5eoqVGJ8ftlfqYGCIniEYs54ddi4kAh5MG95qAQlegzJxZR_KIFomCCMsYJrFhEFikQixuI1cYNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27629" target="_blank">📅 11:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27628">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9P_1yVsed7QDPX7AFGaf83O1wnlb_VMizXkkRR32XdJ5hRSFDUVZnJQlpQ55-2bxSTsbLrcnjWpVsIPH6gwq4U-aANbWfnsAzqHjBnR6a_sDdg1Blig-TD1jv-ru2CEb1kJELs6VBWfk7DHb1JjRp6RpPJHLOT9_kUnuDbqSofpgxKYrB-AL7kMaGJ5-mo_3vZ1hi3cJw9DRUb_jqxpA4faldHqmuP0_wK2DaF7S9-sntKKoKvVJ6ZD3yw0Z_IRgC-o2AjDcWOTohKbfgTUzQRg0vwEbi984EICGb8UrqPiQmem3giaVzHEv9IYBRIqkF2QP8L7RQ3qSI7Ey8uWBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کوپا آمریکا هر چهار سال یکبار
شد
؛ با اعلام کونمبول، جام ملتهای آمریکای جنوبی به روال قبلی خود بازگشته و به جای هر 2 سال، هر 4 سال یکبار برگزار خواهد شد؛ دوره بعدی سال 2028
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27628" target="_blank">📅 11:43 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27626">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGE2c-QwLJK2tecajS5QOw6fmqp_BxzzUx5I3gnchrhx77UEpqTDV5v_lgf3zA_QycOc0Vc17Ot1csFGzDQjYzyBm9dxTBG6NoHrOjyf9JQgkegNqT4xv6WlW3guQ8DJuuXV4vznWnOAmrnKOnu7pA4rsaCjfxKvo8RPePFa1u41UqYggPqDUPb7JVlux5VqFSQkA-bNJNmSXY-0nRsP-9PIbWZX_Oo1x9-0lPwoCZBOsKhsHi_7Tms1hk9_qu_RoTEdu6xSRVFUEnaVSyzpGwk9QLSAFCuW_8T-MMbd5RzAaGbZTy8ApNvnTnKsvsuhcwBmpxi1iPiv0e1G6UK3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور در روزهای‌اخیر گفتیم؛ دنیل گرا در لیست مازاد مهدی تارتار قرار گرفته و مدیریت باشگاه پرسپولیس در تلاشه ظرف 48 ساعت آینده توافقی با پرداخت مبلغی با این بازیکن فسخ کنه. توجه داشته باشید اگه رضاییان تا قبل از فسخ گرا با تیمی نبندد احتمال بازگشت او به…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27626" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27625">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kD4Ge3KIhfNAUZtP0Gp1iqxegYVmtg0mFC-RA6AuQGRtfk-x9ERmNAvMoC3WkczWnEtzXuKM-h-swQuiW2vmBrDf-1OXHblxSdGQvbDCcCp0veyIcPUfHwolykgFrOVfMkV6O9FC8Y7zFZmCfUaPRXO0fMBIv8NtLzP9W97ya-eCPAKxvRaUpB7-yT3zcgqPCg0NaBt3t2xyofCB56ZIw6vUejswDWAndUEtSsYOuL3i_om489MEV8hSTAD_yk6gVaipv4W1Xj3Ur3awRWA_weYsa2rIcxos33BUz32KuvlZDzvEwwGBGK1k_x6ZJZfAKrXeiGDj5Kea_XHIwc0qtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خواکین گیل مربی اسپانیایی جدید تیم استقلال فرداظهر برای‌ عقدقرارداد و رونمایی باپیراهن آبی‌ها وارد تهران‌خواهدشد. خواکین‌اسپانیایی دستیار دوم بختیاری‌زاده و مربی تمرین‌دهنده آبی‌ها خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27625" target="_blank">📅 10:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27624">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
اخیرا دانشجویان رشته علوم ورزشی دانشگاه سنندج به مناسب فارغ التحصیلی این ویدیو زیبا رو ساختن و درپیج‌دانشگاه‌منتشر شد امابلافاصله چنان فشاری به مسئولین دانشگاه از سوی نهادهای امنیتی وارد شد که مجبور به حذف این ویدیو زیبا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27624" target="_blank">📅 10:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27623">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ae0dbca9.mp4?token=qi95m_Sf1cusm5upKr5WT6kMW0Cf7B6YgMqcD92BQJrImuCwLmMdYcuyHRLFAsCvEz9J96PaTw_E_hapiUklqD7EKm9S5-40D8_lKLOOOqf4KzddbstDQVJJ7qN5crO-aJNaZC7nquRBrL8wDak68aQu9ncm3TxBD1n7QeJg7ufTxqwLdq6CqXBBqM_jWgQfGI1MCh6unUtHdMGkqhfeRxljIjj1yVWPhuKUKSzIbOH5Ucn7k0Yo9gNXdCAOvjIcbjKPVRg-vwb4ayWGJQK8_jtkTgEwo_8YziPc0Nc9NmpqjIZ7JtUmrNgLh3TUrZ2wi9KT84SVlX_Vfj_-VaStcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ae0dbca9.mp4?token=qi95m_Sf1cusm5upKr5WT6kMW0Cf7B6YgMqcD92BQJrImuCwLmMdYcuyHRLFAsCvEz9J96PaTw_E_hapiUklqD7EKm9S5-40D8_lKLOOOqf4KzddbstDQVJJ7qN5crO-aJNaZC7nquRBrL8wDak68aQu9ncm3TxBD1n7QeJg7ufTxqwLdq6CqXBBqM_jWgQfGI1MCh6unUtHdMGkqhfeRxljIjj1yVWPhuKUKSzIbOH5Ucn7k0Yo9gNXdCAOvjIcbjKPVRg-vwb4ayWGJQK8_jtkTgEwo_8YziPc0Nc9NmpqjIZ7JtUmrNgLh3TUrZ2wi9KT84SVlX_Vfj_-VaStcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پیام لیونل مسی به مناسبت درگذشت پدرش: بابای عزیزم راستش باورم‌ نمیشه که دیگه پیشمون نیستی. درواقع من‌نمیخوام باور کنم که تو رو دیگه ندارم. لطفا از اون بالاها مراقب خودم و خانواده‌ام باش. مراقب نوه‌هات باش که راه پدرشون رو برند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27623" target="_blank">📅 10:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27622">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41aeeb5537.mp4?token=BP5uTHuZrzaAUXd-UGEfFZjvmt5gUg3qjTbvSy4lbaiy9PVZzI_ySJl0fCrNrCbK34v4q3H8dMR9Vb7lL2_bpBvvc05djpWb99i4lOM6SgsDzHzl1m2DARYvQr3sZ05RJ-LOGgRCogpVhhsGRebm4OKzE9Q_UM_0ejnFjduXBfOyiyWNQx5oUi2V_d0i1eWZX6Zn37ypxosLMNDkJdTh_6PxA9RfiINFqFXvfAUVxetgdYrBXOZwXJrK3SRT--70lWceDhkamkWOktMOrl3uAtTQ7jzVyWwYuS0BCROH9bQ6IXWQLM2xj4MShAqxn-03ZIepnYohyr8dEn167HXU7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41aeeb5537.mp4?token=BP5uTHuZrzaAUXd-UGEfFZjvmt5gUg3qjTbvSy4lbaiy9PVZzI_ySJl0fCrNrCbK34v4q3H8dMR9Vb7lL2_bpBvvc05djpWb99i4lOM6SgsDzHzl1m2DARYvQr3sZ05RJ-LOGgRCogpVhhsGRebm4OKzE9Q_UM_0ejnFjduXBfOyiyWNQx5oUi2V_d0i1eWZX6Zn37ypxosLMNDkJdTh_6PxA9RfiINFqFXvfAUVxetgdYrBXOZwXJrK3SRT--70lWceDhkamkWOktMOrl3uAtTQ7jzVyWwYuS0BCROH9bQ6IXWQLM2xj4MShAqxn-03ZIepnYohyr8dEn167HXU7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
#تقویم
؛ 9 سال پیش در چنین روزی؛
در سوپرجام‌اسپانیا، کریس رونالدو بعنوان یار تعویضی برای رئال‌مادرید به‌زمین اومد و این کل استثنایی رو به بارسا زد و زمینه ساز قهرمانی کهگشانی‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27622" target="_blank">📅 09:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27621">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAiyKprwuSDQ3Uu46ksdoLdu6pgTG3uRrcGzF9L4jvQyWXYg5SxA1eIVeZki2yogXyZw4WhtOGVska8QGxT6hdL1Vp09o-0JOOj8mR_ikM8G8iKO-L60cr8iumvM4Ntm1ewt2f0x2CELU8eCUKpvKPohGTeTFoDrp5jpCnTffyBcZfQsArfWYTNOj3AQ3irdbGUQjuc9SNMjr1US6JUGXEvjX58RkVlbn5j8pQt-l47BPq08BzCfEAT_581_VAZaO5NLpDqEziYiR9NWrJN1j_mkI5Ta9p8xUKRRfV0hgLkY2sHeobc9f1KANdrfjfuNJ8Os_CUCiOYOCVzv28j-8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیرو خبر شب گذشته پرشیانا؛ امروز صبح مدیریت‌ باشگاه‌استقلال 50 هزار دلار به آلمدین زیلیکیچ بوسنیایی روپرداخت کرد و پرونده‌او قبل از شکایت در فیفا بسته شد. مورد بعدیم طلب 25 هزار دلاری جوئل کوجو هست که‌طبق‌گفته مدیریت آبی‌ها فردا پرداخت‌میشه. باساپینتو،…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/27621" target="_blank">📅 02:08 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27619">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6NPxgbZBOWgjzm43qg63zms70D4XflF9rgYLyctHY5yCbAjtmmds0W3s6_s1vFTB3Eli6xpwkWbW6R2RRxmrdUmUsb68KUOkVwkns72CsN14D258LxGT7Kkmqfm4dPPFK5fD488doU1DfD0qcwyuUwO4iGOFmYdJRoVj58QrgJXqJgkQ6RiTb7O0ByPHTHZiEMRIZ3Ibk5FIc2yKw6omvOKjQNzPhfE5CviUB2Cym-dZxDFv9TQosuJv4wIu8gCE_3RrIu1fpcRKURFTP4_O-2bkYsqES6lRw_vnN5EfOTwETw8Ky7UUuH6vfJSPmN76h6zWzUbeFu34Ti4FSIgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛بانک‌شهر قراره روزشنبه‌بودجه200 میلیاردی دراختیار مدیریت تیم پرسپولیس قراربدهد تا اقدامات لازم رو برای جذب محمد قربانی ستاره الوحده انجام بدهند. اگر این بودجه تزریق شود قربانی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/persiana_Soccer/27619" target="_blank">📅 01:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27618">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFc1o6joDYPArxAauiJ5jrYi8Dh5ick1RXRi6aQXvBiYeVb11TzYPPwfZI4sskmxRSHo8z9osXcacBjbRAKYubPKhCH579PdvhqiGq7mm-Ri4C7eV5BSZ2nBLQd1DEzzJ7v4yuv6tfzYHrmgV7rbMBr4Zmd1gq-vcK1b87FPOZ1LgExDBSpuur9OKF5_XjlVINYW1L9fs3eHTOhwfPcXxLXtpwuRvbJy8BkeqFNEj5Gpmmcvk-7rLrsuFArxZmtp2yHmU6khWasO_05bFQqX6YFQ1dKock9lmXgiVpZJQbPdKOv_WkcG2WOpu6U1CoZ4D80AJFBonp5r8WcUudVsSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
هواداران‌پرسپولیس‌وتراکتور در زیر پست‌های این دو باشگاه اینستاگرام بشدت فشار اورده‌اند که محمد قربانی فوق ستاره 25 ساله الوحده رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/persiana_Soccer/27618" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27617">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpvD8k_mtZFEP5BhBuXJmOsSEpf-EKyKd2g31rsO7B_qM-Bzq2N2FWB0wZqmnIWINl3NCypxJaU1Fqg1mEYaB-WtT6CWX93wuTUvupk1Fgg1Wt8W_oCWVBY3oQMvKTSlKyFYhYNGyGdsmb6gBH1GNZfq7zJ2-LYMV-wvhUtqcVBRtiz8JfTpsf9rbmvgxapkrXeqaI-LNuRy6c2kuRC8kmf089jDXsL6MNpeLDUC0IipBTanswLWe9rrtjvcBmo0mQo2RA_poUq1BMTmoaATGOL6LJ20tmYEXt9bOHRYij7vVkpQgl2YkToVTJKW0B2ijSyEJOtk2ZY8cf763LPdtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌بازی‌های‌امروز؛
ازبازی‌اینترمیامی در غیاب مسی تا بازی برگشت پلی‌اف لیگ اروپا برای اللهیار
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/27617" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27616">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMo0d8g-kiSzJ_eVdTIodvBBhGnxLa9uW4hasl0y-DyG4_dacpLxxBGqhSOn5c_BC6LpFmfHFONQZQVQDZbpX_Pj9tki472JqIduIDYs1nlNgkcr9kikXEolgFqNVm3-WoxvUb79VQR7bCMOR-kWEfOOojU6JdcFNAdQFmJS5CnwPGEk-pruTGQfbDKHBLhdoqxhFEZrJ_sSPvDydsnGCqgy6zzzf7QjXfxahnBeqXNL3yDhdAG8XtVQmO2xmWFbA6SnbtdzFp8PSqSeZlMZ9DAAsnsYtvMaMBINnVDgUzr0EujOrrGVvA4l-kB79f_Nt_Tehs6Ija-TJ7W9zdI7Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
‌دومین‌قهرمانی پیاپی یاران انریکه در سوپرکاپ اروپا و برد رئال با پاس‌گل لونین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27616" target="_blank">📅 01:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27614">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULh-Plug_ZpeycyAJWarciSzIiou8lhrMf4sy3qZlKoM_v1Lpj-4ME3suzPtDBam6AcDE2xAKJsBkesddPSjzLAdFi28foxzUiqJvl29WmDrieD1A5oG4mCL3MSZyiPeLOV5D-D5-wuZs5OFKpCpxCgJDZxF5SQSpPX0_VZH3HgHk4N5F2ls75x5LnDa178r3vt30J7G28hSSattwfUEH--47FFNDoIlBRg1pE3d9pftDA561_oond1MrVE2v3Xbk5BnL9IKL_ZQylVKA0SNlSep3vvzEIgwwBW8_g8B1d5J4WZL8T6-fw3aU735vJw6K__iV5Ld9tDwO6Qxds6nNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماًآغازمیشود؛ طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87,200 تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27614" target="_blank">📅 00:58 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27613">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpkZ_X4JRD7uCx54M5kSm_yhSnT6PMMFj22TgQLVCDBP44nEYCzGlPLpo_BRiFxmP85GJU7I0ihtTr5rcj-ch93iba37x8iFH9AU0at4XkcgiywfANudf3zCpDe8KPT1CGPyPPNTeLLT1LrFTeJzmyxUimoIpmh8Q-0n5IlAUnYZH9srOiDsh8uA6MSqJxi8xUQdj0ERnP8QAeY8MQIIiEFMsHWxvgdRv0DFapWlqayL_E5Z57Svnl2wCFQC-ygKUWcWXz6W8nQBw3gvpxps9-DXICnajGBPiVPkhi9rstvPxktsH1WRm05fydIo9ArUpth10aghyQXiphdmIFxMjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شاگردان لوئیز انریکه امشب با برتری دو بر یک مقابل آستون ویلا قهرمان سوپرکاپ اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27613" target="_blank">📅 00:45 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27612">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5nnL7ZkhX_Tvu8cOoScrkBNwbF6cdtFltV8HYjDX4u7MLg4lXokPSkPbC62Tt1mo6DVWUSThq98h8iOIPMlN1w18JxLeNSd7fGOguWi4XOe16SpPASGr8Lu8mPIPrL8Oi6GxFpzZFftyaD_phXW1NNUN2Dp9JcZ8CyOFYmvj8pq-GC0YKcGxt5US5ytIGvY6K2cKI0nxMs7DiWxCHMSaWa3vL9YoPQnQ-D0udQgQQ1Cmb6sqUH42s9KHvAZmHet0LDx7PbTpvLF8dljLjVUxVDE7TirjIBev_0lPf2iiT47oG1zDRLYIeggNi7PvHNFhfdv5T7FHsrEV2E50ZUwnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌سوپرکاپ اروپا؛ شماتیک ترکیب پاری سن ژرمن برای دیدار مقابل آستون ویلا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/27612" target="_blank">📅 00:36 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27611">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jx75CSmZyU9boxEphmZhXAcqzI1vwZsbK_XHRy-4rXVmQihbef-_SkBOpq1qlFjAFI6LR_-lNHn8egVT-wMr1NkVg_xttstfmRu96gkF_m8AGLlzDCOC4l6OQGO2PoGBDuOqNekIPIGWXygnLQdAKAmpCxsnt5q_pM7aLLq9xMFJlzidNezfHpUYnUsYaks7M-Pzal8fMWTFMagRk0L3GiZVIjbfPEKH_yPX3RpAJcdLNuWzXEofp32yeMbvP4rBz3n1DcpinLUCGv5IFXil5fg2Vc8kk8VxM2qWsrZr2u65b26V9A12kPPIY4pnnYzjCc4FEg6TmE7CLy-V0LcUEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27611" target="_blank">📅 00:16 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27610">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgUgz8GJoRNJbcNwH2wpUekU3r1MeN2oghI0_wrvdhBBWw0mU51-W8mIOagCOTtDwQgq3Luo4Kx_Mpow8E8cYf0AZvGDFoTlnsyB7G-1M2fu5M5uuo6n_Ob2afQHv_jhaM_6CjqPDz4x0G_Tvjy8vNajUf9lOoD1_9FkicvklhZxUnqA7tQXiieX54j6ZYOXdOYI2kxyoju_UgQcjF5SRTEvrSzBBJYLqSQGSfGqf4tp0-3bVjnvgjXjSMW5Cv4tHNVRC0NtN4B256V_c2q4FsVTxiD_cpMEyq8yYXzIhtn86xwYJm232pFbKzwC9pBmSF6oxirbCbRsO-26Eu-rqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با اعلام باشگاه پرسپولیس؛ کارت بازی تموم بازیکنان این تیم از سوی سازمان لیگ صادر شدند و سرخ‌ها با تموم نفرات به مصاف شمس آذر میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27610" target="_blank">📅 00:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmbEcKLQWji5RVEv3ovMD-ybVauWrswttBzzXy-sGx0xVSdufWuMYsXj5LyllheV70K-2r0U9ZQatDlvdOAWUr1VUldrnkJKrNQk1j401D7bHdMXPur3IGl1It-ynAOOUEbZFPBn6mtye3l7hObY98tZkQUfI0YGrZjUAsKXIkdPeDZq_ud1BY82b71hEF7e1J08qA0QF6kTkB2FCzsSMUHyKtHL92-eE1eIkhHzIlnKmV5VI0pD9_ctQRawnBe1ufC5ylZszvkyYTWFP010r77KDpi_Ile2D9o0R5s2fVLDWOhUiY3cztDn6_o2-9JIyzx3k7dL4TMeadwYMkPl5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو اسطوره پرتغالی تاریخ:
🔴
اگه من جای امباپه بودم، می‌ رفتم و ویدئو های کریستیانو رونالدویِ مهاجم رو نگاه میکردم، میدیدم چیکارمیکنه و همون‌کارهارو انجام میدادم، کریس رو الگو قرارمیدادم و سعی میکردم چیزی مشابه به اون در پست مهاجم نوک ارائه بدم تا بی نقص باشم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/27609" target="_blank">📅 23:59 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEas_qwrapiq7JyH9XQOCMwLBDq6JbSmkdHNNh1rVkNNY0zSpgfa51vb0PrOLB8EbVyJg5SmPEXk1STNGuSaXLfA83hnrkWOZp_RW-Mb61j_TAkWVKrlQuq6VLgOoU4L6VUI84r9eH2bTpoSoNJN_MbJtqF6tArePQlc0QcwL2O1ce00ZrSHEvV2bNJ_3CoKlui0BWbxxKVg1S7N699oLxSU2ygHB4jEOYGO0qZzzjSS43UGfSizu0aFdwWTtP7SpydDWhtNNo5v_RRXa1CcXYUo_lPO07zvofOlhlt7VEHPEt51PdrpkpVB0GntLospNt61aQvgNngb6xgzjcU8DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه شروع فصل جدید؛ نگاهی بندازیم به باسابقه‌ترین‌مربیان‌تاریخ سرخابی‌های تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27608" target="_blank">📅 23:42 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27606">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgmD-zTqTcOPXLPF35-h4zYRbZWxbdta_Gp6BrOrfB6Hgon1Y0ESX6JcO1YasZposADMMoSMkcsnxAOlwD8SnT0pFriKeUdCDh7v8m46udWW-mnVPr0glsaGkmIOqj_WCj75TW_R6FJnMMUPeZeyRlQMTTKMvbTxFLxDe-GA4KNvbcAW3xVfvfi0OOZBm-hqiAwH-qh0CzmT5OFB4m8OQo6h-GTCWqWB2fSP6ak-W8PirbbQmd0z_8sXoTVS75dYPcrs-l4RQRnZYa9Japz2gdtGbzqR3HccK1VHNEMQQTwFva26A95aNYcMBhwKiAsQE3BpafGH1wVXRbkD2CV_HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Epp71Q4pqdcondHQe8lwS1J0bsvi8ZCAeyTqPFqnxqucIf9Euj7b6OKZ0IM3Dlv6-FLZD-njKwOOydQuQiY5RwrAu9iXVcYG_RRpC5gbZthOwLkyOxEUXCHFMlZDZSivyJqtWbNn3XUhhND2q5OBi1jCeeo5O8EZDHi1K7qFvgzqBbJ-BEXdoAlB0fX10CYctsrbe2T1th904X5MOK2NG3OOyeCQu_ovv_n2fdG3Tb_ZzYjltD58GMcl5M1131K5rC-tDpHrwjWxMX1a4fnXNitWim5eKCwYM5c7-C3tJGg5lhLJCU8ZlX1VFkP-qH1cXqSchFle1oJRWgKi4guaEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به بهانه شروع فصل جدید
؛ نگاهی بندازیم به باسابقه‌ترین‌مربیان‌تاریخ سرخابی‌های تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27606" target="_blank">📅 23:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27605">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfiJY1-NJW6WJoC6CibFAysFu82CAY3zte0ZCYFxd_9TZyjc7Ngm5FjYJOUhv3gW6HEtagAXIKUzQdf8ouiNhUfTIDaIlsizdnB98k95whCA_X4IvV4hnwmwOio6Ku-iBc6Zj-HQ0l2e_qWulYY_Ujii453GGPzynpnxakrfDNAtf5HhxmNGuot7sdh1aXkCmBNH5TeKOA1BQQSc1493LSMdaG-QJ-ISXB8feTw8tdy6DWgoZZtRnbY21gIDALXLevOBVBCrF2_FYK4dQfUay9SGpGXGjk1yvO2BkN6DmJhdq9zg7bB9PAUoHtEWDlSjmFfcGl-WMIX6jZqT89_2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
تنها دو روز تاشروع‌فصل‌جدید شکایت نویسی؛ برنامه هفته اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/27605" target="_blank">📅 23:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27604">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da5714c0bd.mp4?token=TmaknbGZUaRCJBb1yrfz3RXjAEULlKKVD6A_-YR7R5gJYcWNmYJylXPY9TY74FUayQfO8o0nYx448Kc56dHy1fpGQ3luMietiHXJIx43qpkYUjNQdI_hjK-xuPRvu3z_r0QO3vwd-F9_psZ4iWfOCaxqQTt4yiA2e2yfxLq3DdXusj_F2yKOvY9-nSgjxhKaMBN4uv0ve0QI7E6RLTj3G7lekBJtt6uM7PSxc3aOCUKxOszuinjlRq4RAZKFuahlpjZYCa_pNODYBzeW2wqqbOnyohxrYAiW0GhHohTOMcexhz-6cXN94K85SPR2zuamOScvmwpVRUNngq-zEAKQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da5714c0bd.mp4?token=TmaknbGZUaRCJBb1yrfz3RXjAEULlKKVD6A_-YR7R5gJYcWNmYJylXPY9TY74FUayQfO8o0nYx448Kc56dHy1fpGQ3luMietiHXJIx43qpkYUjNQdI_hjK-xuPRvu3z_r0QO3vwd-F9_psZ4iWfOCaxqQTt4yiA2e2yfxLq3DdXusj_F2yKOvY9-nSgjxhKaMBN4uv0ve0QI7E6RLTj3G7lekBJtt6uM7PSxc3aOCUKxOszuinjlRq4RAZKFuahlpjZYCa_pNODYBzeW2wqqbOnyohxrYAiW0GhHohTOMcexhz-6cXN94K85SPR2zuamOScvmwpVRUNngq-zEAKQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
دوشان ولاهوویچ مهاجم فصل‌گذشته یوونتوس باعقدقراردادی 3 ساله به‌باشگاه بشیکتاش پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27604" target="_blank">📅 23:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27603">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H8FkxGA-mwOxhz5Wtlg0t23fsSeHIMmAV7fgXxp4dtBHHhGYWppXquEPwGiFVTcy1e6YW3t_A6nfEO4Aq_0LEAlcvbxjUsRCeTfirO1B_n5nM36oo_c8y_ADMqc8KkI-gZBbYGh2KlYtbo9P7_Q35I7gJb4WI26lW15lHb338DilnlW4pQkMMVGL5bynQIBqU2bXY5Nh6pU9t2aRMqqxwy7x9Pijt0DtFqucsKgReyuSqNaMPOi73TjI3jpIG7gQYMyW2BAcZt9TulVa2Mdd9Qhw9q_NT47qP4HTMqjxQ8LmVXn3i6yCP7wOLXiL0FURhvSm632zGks_5zLYsUnyGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
ژاوی هرناندز سرمربی‌سابق بارسلونا با عقد قرار دادی تا پایان جام جهانی 2030 سرمربی هلند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27603" target="_blank">📅 22:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27602">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fb932d906.mp4?token=JhO2XCF0VW6MxO_B5Js8JRbz2lTW_Px3qKvvsGeOR4K17SkP7SWpHAVtQDuBbZqjS8Zw1XOS3OLUeIENaVKq1Rootvem5XogirAmq0Fn0ebwk9-vzmyBBn47devI0-B5MSTVHgERexCKhkTp0KpYofZOoA7TqCcqGWGt2EAa3rKHmvakKUiofPI37EBCSo6culy_QjfASRYfAwEnUrMz3gi_xazDz4q8Vap_DrOm6KwnDrHpV5yWdl-agHbQGjmYqmuoC7vvKlow2jW1sQw8DREuONZfJMqlGH4lzR-toocfl4Uh3xsrkj_y50TJbW3bpG3ih4bZWjsPLnbBWTjjFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fb932d906.mp4?token=JhO2XCF0VW6MxO_B5Js8JRbz2lTW_Px3qKvvsGeOR4K17SkP7SWpHAVtQDuBbZqjS8Zw1XOS3OLUeIENaVKq1Rootvem5XogirAmq0Fn0ebwk9-vzmyBBn47devI0-B5MSTVHgERexCKhkTp0KpYofZOoA7TqCcqGWGt2EAa3rKHmvakKUiofPI37EBCSo6culy_QjfASRYfAwEnUrMz3gi_xazDz4q8Vap_DrOm6KwnDrHpV5yWdl-agHbQGjmYqmuoC7vvKlow2jW1sQw8DREuONZfJMqlGH4lzR-toocfl4Uh3xsrkj_y50TJbW3bpG3ih4bZWjsPLnbBWTjjFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
معاون استانداری کرمان: از امشب طرح بنزین 87,200 تومنی رسماًآغازمیشود؛ طرحی با 4 نرخ:
🔴
نرخ اول: 60 لیتر با قیمت 1,500 تومان
🔴
نرخ دوم: 50 لیتر با قیمت 3,000 تومان
🔴
نرخ سوم: 40 لیتر با قیمت 5,000 تومان
🔴
نرخ چهارم: بنزین آزاد با قیمت 87,200 تومان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27602" target="_blank">📅 22:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27601">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Trwl4KKbXxIk9vUCCqPDUHonr1frkXFeNCASXc7Yg53FwYdWTavSiXk0lppeOIPSOovCQSW3MxTCd88Uzed-n7BEBYTtzkjyjTskylU0o7PsU9gmiqdiFaSgpuZNyG9jQfW2iX0F0fX3KypWnzuAenCZBzG55-jKlaPCiFNWnbg6UqYbLUCoHLELcp1c1oSwNfJCRG0T48hiGBTR7Eqz8lg4aqDfmNNFx-8O0xqbPmCBrOKicV03Pnj2WErlfwPTDVPhxRYx5MU9GcwN5e_QQi6lDWYIGyK0ZZg5_2Advkxx8WJ75TgXSVyMTlURYhx1aXQ6Of3RI_GtNSRX0mLHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
باشگاه‌الوحده‌امارات: دوباشگاه ایرانی برای جذب محمد قربانی مکاتباتی با ما داشته‌اند و بزودی تکلیف نهایی این بازیکن نیز مشخص خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27601" target="_blank">📅 21:46 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27600">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZgZILVECqzM0wokYJ7Cy8NbRDnm7ZbjNsNGa18mFeldjJKL3I6zNSXkmaYMMataOMwdG2jghmJiho5WFe_iZ77-pOxNEUuQ1cdsO91G8XPxrh99zd0L5F8dj5O_4CNUfpJoD013H9x3zLxMs33ua-aBP8pul9oUrYW9sW8TJS0YxdAO-3SXIhf2oD5EU2wIj5D9Vrvz_qkUOXWo9VzB0JuJLqLdfn6tbyTtrKQkME588DTxLiWM5DtEg65mLmOJw6uiA4BUUulHg_2Mi5urRk6jXCvfQzv1Nbm7LR-FWn2azUT1W2WGT6Iy-Ap7Hws1Emt6Kt1LQGqhmNkfBwl9aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فینال‌سوپرکاپ اروپا
؛ شماتیک ترکیب پاری سن ژرمن برای دیدار مقابل آستون ویلا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27600" target="_blank">📅 21:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27599">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWKhLnLcTmzzELW5vN9UwdaSOK6UlegGVm2yRUOfOJ6PUqHG4BIoftheiWHONvCfQ9Hcotfkueh0Vcuu6WLoI7po28rFOJhVtSZNnd7nqe6JXjn4lZoZ_0-JkgpNms4HEUQNA5nFIFjnV84M_TLOYRoRj1TTODUUtCLsw3tsJvUu13PMqxxAEXxs6vpQ4BbJPnEkMTTlnA6OCOeh2CAvZV3fEQYoVpMbQC-lTnDbTFtXN9ZWpqtIxukt79TEgq4p8MN43V7-Icr_dX_cSzxvORYFjA_vPHRGjbvEYEX4VbQ6zdbpUNy08Cz1pER2MiVDp2evXYpMW4jBvfZEj-Fpdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
حمایت‌قاطعانه‌عادل‌فردوسی‌پور از سعید کریمی کاپیتان ملوان درباره‌اتفاقات اخیر مراسم ازدواجش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27599" target="_blank">📅 21:07 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27598">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5cU6GLPmfJm8Tfd8dMbK3qA7r3jaHViGFfT6v6j_dhSCp_st-KRGkRWdm7qlk1D1bZEj0f9lDbyUxMfe4pZh1BbP-_n2YVx_K3mugyDP7csqnQ_-E6XatR21RvyV1SY_xrsG-6-uVHh25_W7ITSEgc_HKT6tYtH6Wi9pgGFLwSkjqhTtDt_5wVsgfJaDivmsgKg-STMsgtVO8hlQ2tTZ99cOxBanVAVckIts0fC59cSt7i-l3J3nwssF60y4sf8JNlBLZIHom5lhH6uqTwySIDQvburJriIK6Swr-3kZG3zf_l3uuS0AxQ3UG7HKEaXAcpDJjIDXr-RQFjHcg3zow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
#تکمیلی؛ طبق‌پیگیری‌ها؛ تا روز یکشنبه هفته آینده تکلیف‌نهایی‌باشگاه‌ جدید محمد قربانی مشخص میشود. قربانی بار ها اعلام کرده میخواد جایی باشه که‌فیکس بازی کنه. هرکدوم‌از دوتیم رضایت نامه‌اش رو پرداخت کنند میتونند با قربانی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/27598" target="_blank">📅 20:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27597">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNg9YSShZFgYEbJ4m_VxP5QRW942SaZNeQJZkq33DraEkwl3bon99ztkh6byb_YIHsIO_puOBVsjbJXUaOEUSQLQRPv3Xlvl2_y91wiTIl7C8KgalZGqL2UU8m2ORtGvGvEHTtdFKfurmPCg-ggeQ6aXBa6YmWBt8vfY1RwYnn-c7znLhweTOtbskcDKe_lFdy9d-x7KNvyrZPsc83EDI7iEugLHuzGnWJztkP8ADx_d-WeGdLxIRBwYXUNaOxgYkF3QsWQiNhS6oXarmYSBgeyFEgDTH5D9J8rSTxHjLoZQGqkrGRUbt9PWTrtRPZO9fhGyYzZeV6pENj8kbHrJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ تکلیف محمد جواد حسین نژاد و باشگاه‌جدیدش تا پایان این هفته مشخص میشود. طبق‌گفته ایجنت این بازیکن حسین نژاد حداقل تا پایان نیم فصل به ایران نخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27597" target="_blank">📅 20:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27596">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWfzo1a1UTV9IhI7yNkNF5lMs_YcTjxJJyGXaAQgkoZpyHJrzaQawuVPEd5AxJlmBJbPfSz429z6dIDCvReoyMzrDGWm3bdAzKcloR08Fg9uSqTDNQPKUregAT_YTR2k7yHPnXOvPYnJrjMQHvMzh0q-77j9podOMmtiKEmw7pAZJNl0jYv1Ynal9kZMLXk0xzaV8PN65AN05WpnulBYWNo-NLxcwXDSqwtoGQmBWjuXE-9mnPEbMyQBLmNy6WxoEi8jgN-kvuQQGEbSFYYynuBo5z-3zXSpI7PjVlMI0OGo_kqeuvmNRfijCICJ89Lr3d6ruNKb4J3zQcReTpUKfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی‌پرشیانا #فوری؛ کسری طاهری ستاره 19 ساله‌نساجی‌دقایقی‌قبل رسما قرارداد خود را با طلایی‌پوشان زاینده‌رود امضا کرد و به سپاهان پیوست. قرارداد 5 ساله مشروط امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27596" target="_blank">📅 20:12 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27595">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a80c00be8.mp4?token=FmymkN_SF0Rp7FozdltYmY0KGo1BTwTlgeqPcK5p7K9zg63oCQxH5754WCEfQGti38PKiTeqJv33KS0Zp7jcaaOtu_OSkVrMWyWqmi-Ksn96ZozRzwvzHA-Jz51qDEBT0PjGt_2GLTLLZzlIEcVCdnDT_pnL5wT0WxkTcO96A5y7dUNT5e8ZOB6x6Y-QvqShJL4PlCnwSBA_npIHnZS3ZXVWrH3dFgxzVpYnicd043LaSzRAXhp0ZEYGOMhZ1TTlMFX2I2m7ZXlSI9x8zNu4D33neVl9Uzs606bRe5987WIis1AlgZAGu5m-sCCMpvn_IRqS8jFg7ghQsatQJlLRrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a80c00be8.mp4?token=FmymkN_SF0Rp7FozdltYmY0KGo1BTwTlgeqPcK5p7K9zg63oCQxH5754WCEfQGti38PKiTeqJv33KS0Zp7jcaaOtu_OSkVrMWyWqmi-Ksn96ZozRzwvzHA-Jz51qDEBT0PjGt_2GLTLLZzlIEcVCdnDT_pnL5wT0WxkTcO96A5y7dUNT5e8ZOB6x6Y-QvqShJL4PlCnwSBA_npIHnZS3ZXVWrH3dFgxzVpYnicd043LaSzRAXhp0ZEYGOMhZ1TTlMFX2I2m7ZXlSI9x8zNu4D33neVl9Uzs606bRe5987WIis1AlgZAGu5m-sCCMpvn_IRqS8jFg7ghQsatQJlLRrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27595" target="_blank">📅 19:58 · 21 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
