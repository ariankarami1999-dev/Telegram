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
<img src="https://cdn4.telesco.pe/file/fqXI3Xj7SOQHnyhjSsW8rji3UjtoEk-wYlTSRQFMgSxRn_89B3UbHcMhDlQ5SOWR7Y2O446awa-LFPrazbBddvbuWPggNReTDCA-YUIM-Wp7PIB9avLc7mGs5QBCG47UtHrByTm2OdJliTu5FOH3zvjgJKM3ity7GRwOo4OF3sBM4jtD30G5am3IRk6kSXUFmpwPVAwkLBC-TCJn553PFPrE1RUbVimNn1nJU-yBrrv4IxX34O4h_7EmvmGWhG0qUVH_nYLtdqrTqQ-Y0fclfj8AkquO-7BMe9G5e5HYsKrWoEGtL42BviWfxf0WyggkxF2OXNr_RjKEyDqa6ZgGZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 469K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 20:59:37</div>
<hr>

<div class="tg-post" id="msg-30205">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8btCncxKCNox4f0KI-PrgY25AdwLNYSsDv65-13AesDAvlkrbb9RFpwyvNIMIzQg9kMCrq-UW-E1o-TrDmZzKiARMVAzA8lL5Jr-iy29lD0xbPz-iMgkATiW6pRTkM7uXAtLYkvA6xIjDUymdUS40T_Ho1cCZ9nJ7ulcS2jDjGeVK7LKVYuWS26SlmXoM27-Q33_tIEFHSGTgO2Jr8gZXqwHZDhmE9xNgIKTh-FKFlENpGBRW_70eFBb-YIx0sVZhHMXipYEWFlTA_FsUbdCsdfPVajZtj_YUga-hJ4t-BwJUAjCy9armCgbb-CkW9fvqQuBbmy-NZvsOMWV-0f1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s-w7hhQDVdhBLZHm7UGae26nYi5nZySGv6vsl1uxoEYWFI9F7zTmHlp2mw3V0z2rUN5gToFNrP3eM0RGuvema8WlcpaXEXwMQX2tj-DS1EIV2D_xfLuvBwFuCVZ4Mk77nCilAeWW6HHQZEWezsHry32Yg7H0JH8gBaIutjq0kFd9iRSmIK46PwXymenweMEWWzuLTG3NsWM7qRKUp-CY_cYJPKN5w1RWVJXOGof2Svp5iK3kid6g5g7f_KSzXzXPDU3U_McDh4aOeE2WLg1x4IynFV3PFSKHcU0ab35q7YHOBQEfXy0wRdgnZm55BXI1FOx0WOOTncxv2yAFSSipqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج بازیکن برتر لالیگا و لیگ جزیره در فصل جدید تا پایان این‌ هفته از نگاه سوفا اسکور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/persiana_Soccer/30205" target="_blank">📅 20:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30204">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtO2v2p7Uebg_UYOnR8UabkAAX3YUD8S7mlV9lV0EtA5fKn7QHARBhiIw3BkfBXOS-ZPP2I0zQ0gsfYoP8WHd7LYKzQw1kXkYEa0gkDykDT3hznOcZs5razZKX0Vx2S9mfaTPk2kM3NRWy08sTZQ3lvx_7yJ158PqtQnWme3L5AA4baU4DL4aDX59XJo7UD6--WvQVLXor4S64wxMPgC2sCFBb_M0VXI51JS7pUoZ8k8ZJTVVHeyY8CGksThd3myPXkhELqgUJZvcbsR-3pUGu9-PXqJe-OwufCxJdQOMrQdQN9KGY5DxZ1TOyIYksBqEg_gpCQFFIZ8XYT_7dW9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گفته میشود عربستان‌ سعودی و چند کشور خاور میانه‌ در آستانه‌ شروع رقابت‌های جام ملت های آسیا بافشار به فیفا به دنبال تعلیق فوتبال ایران هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/30204" target="_blank">📅 20:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30203">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=XpPkrCmXgVUjWoI9G_HAczDP1MCul7j5L-qI09RBNYifYzWtrLhT96PiEJUI4YFwh7AOaAToVjuc1fm4bvrHa__vlnNJ0DOHb2cCQolW5j_4mgPoikjhugBrkxdrRwEaEoTPMipnGDGUBYg6-Q07atmHciQYrro4iDtPeJ6ImAZMvhx2BR3dbHAirKAxYLKU1gSRhFDWN3FYO3AdIpekCB2Bi7MWyvlGFAdEpht67iHvxAZVSHo-xQl_aJYhehWYtkgAvsgCnkjz2RVEZlPbcQmmcNLUESOktna7U6he1RtfZGLnJQ3XZ5tkujb0HwnWlb0zvrmax5yBO4YZrYucKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ada5d0f44.mp4?token=XpPkrCmXgVUjWoI9G_HAczDP1MCul7j5L-qI09RBNYifYzWtrLhT96PiEJUI4YFwh7AOaAToVjuc1fm4bvrHa__vlnNJ0DOHb2cCQolW5j_4mgPoikjhugBrkxdrRwEaEoTPMipnGDGUBYg6-Q07atmHciQYrro4iDtPeJ6ImAZMvhx2BR3dbHAirKAxYLKU1gSRhFDWN3FYO3AdIpekCB2Bi7MWyvlGFAdEpht67iHvxAZVSHo-xQl_aJYhehWYtkgAvsgCnkjz2RVEZlPbcQmmcNLUESOktna7U6he1RtfZGLnJQ3XZ5tkujb0HwnWlb0zvrmax5yBO4YZrYucKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/30203" target="_blank">📅 20:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30202">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=O6AB8P9o_CFFnr7fjV7U6A9N1hUDSbz2PxHPSv1AQc8znA_W1Fe698ikmr_GZYAGXUe3OA7pTMgYbLXzaf90GN72KeSKr8tJ8YJwFyQss3qb-LLCs3SK19Fypw7wXo25X2R13EY5Hh8KksJgV1_ziBNRb4AbGiVCytSkZHmtV_LxwU4mvzG8MapIGm46tORnPEobF8gvZHuOJ69e2ayw5DBUpjlzJBEiENYdrvIhJ01cY5J0QvhxVxvo5t0iNRevLGlGmrpXAaHK53uKKAS-Ic6RooSztg9aJgrh00E-NBJ1F-nCspyVZtfTdC9E_Np_4W54XdM3clLU0CPS9A2kyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f47656d4.mp4?token=O6AB8P9o_CFFnr7fjV7U6A9N1hUDSbz2PxHPSv1AQc8znA_W1Fe698ikmr_GZYAGXUe3OA7pTMgYbLXzaf90GN72KeSKr8tJ8YJwFyQss3qb-LLCs3SK19Fypw7wXo25X2R13EY5Hh8KksJgV1_ziBNRb4AbGiVCytSkZHmtV_LxwU4mvzG8MapIGm46tORnPEobF8gvZHuOJ69e2ayw5DBUpjlzJBEiENYdrvIhJ01cY5J0QvhxVxvo5t0iNRevLGlGmrpXAaHK53uKKAS-Ic6RooSztg9aJgrh00E-NBJ1F-nCspyVZtfTdC9E_Np_4W54XdM3clLU0CPS9A2kyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
فوق‌ستاره‌ای که بعد از خداحافظی از فوتبال نه تیم ملی کشورش روز خوش دید نه باشگاه‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/30202" target="_blank">📅 19:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30200">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uYbtS3UldyLddT29fJo01lge9y101HQOp2yicoBQrGqsEgFKYROi-nMuw1IobfXj40GFuNsHkc3_VdhYUg5knqYtyCw-NEh93HHPAY8JOvm7fdxLDcmVyy3OeALGcf98pTUoxYHSjjdHMlFkBGvSy-U4y-HQ1zJe00g1kkbNV2zlfzRuuIvaoprCR4M-fM_KhhEL7F5-MXATvvLiakOumwtfYtmCW-RUGMrQ7VWqj4cPQizSx9GnyOHNLmeIKcLVKQi0gIPhmI1dX7QfSKarETaYSv1kSHW1hiap6Hk34DoA8dSib6SkZgEsQnqM_yw-EzrR92nZZ4apY4W9svd9qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcRZ01_-A_mWhOe6BeKD8ZH1D2u82vXhTTXBmSfy4yHBB0tHBzuz-CkOdrj9cAWWAQ2HvzYogT_KXw22SdyoEVsARU08soFhKtSNlSlUYhYzbSd6zFC0S5NCS764gNxUoZwf6DNJbI-7LS7qmrASCXgFfcXjyn6sXyyl0K934GdArgK7H8xvQpU4LATd4Wn_qkmicg8tDQiCSfsPsrJLA_8dm-REMugrxZk1XdXxlSjiGNfiZ6mIc31XQ9ExueyIS1INILKHnYWGFBNgztzR9csWD-HXzkJi770-qnwY5gEBQgORBTzSDend1sY6TUQ4iBVxMMd6I7z_vVrWDaKmgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
تعداد خیلی‌زیادی‌از هواداران منچستریونایتد از مدیریت و کادر فنی شیاطین سرخ خواسته اند که در نیم فصل کریس رونالدو رو به این تیم برگردونند. قرارداد 2.5 ساله با CR7 و خدافظی از دنیای فوتبال باپیراهن‌ منچستر یونایتد رویای هواداران این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/30200" target="_blank">📅 19:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30199">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xtj-WChOLkjpSQVfGMxhf8-kyq7R_7FTSoY-xtNVdcKjtpoQLtaIntuX_JyUga2kd_Ou1HHReLDJIAT2yjI9YEkTjsCjly8r-wkVSpp6wIIAYNYr1e2eeYyvMDKeR3OhJ45vLabB7OpO0z0I8FYoU3XhCXruyAwEHNGpxce-n-DgBUmaPg9twMbbbKCIC8c7hopYpwUGnf6nAix_gmKIGn9PX4i4hz3pmmZl5QCOdNVuuycYNtnsok5DA_TxRvYce_LTcaO9g2GTivLTSHzYayMAQ0Da_DeC_o170hFn4Dwkras2bf1QyQJlo8SDzN7MMZArqN4RAhfMG16kF8zJkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قهرمانان10سال‌اخیر تمام لیگ معتبر اروپا؛ پاری سن ژرمن و بایرن رکورد قهرمانی در لیگ‌هاشون‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/30199" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30198">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP4tzjEqchkSgHeCY4GxKtTiVyn5s4s7b7Y5wTiOkC7Q_mbZ3d3wVwGyGzIcNIM7TWWy58O-oFe3dsMWECMfO_4LUmbmfB9lOdKIEtHJ4H6yPKmJD6cx_3xtSi3tur3D2fccUMiugaoHWGaq_4H9e2t02QqKwgrR6l-3LQOANd_-e0hFrUaAAyuJJqFDJp3eU-dBDPD071UICU5umzmofNNXTz-qrUY4sU0A_qzY9R1GmU-cNEZv20ptw7WIgtl53p8pbfheST4_2WsHjq0krjqv2_5JIfu1CQkMSpRJzKyaSaYuvLGmPKbQ8HD8ehXR8_kbAHe_pzF3zfBFjtqJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه عملکرد رافینیا و وینیسیوس جونیور در این فصل رقابت‌ ها؛ جالبه بدونید وینی سالانه 24 میلیون یورو دستمزد میگیره درحالی رافینیا در بارسا سالی 16 میلیون یورو حقوق میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/30198" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30197">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loZszLfcRxgcq8-rWrHFsGkGBAt69RpwqVv2ezvUcLn9CFoYrWtO0LXHCryJP47HSZMy9Tj27hEGG3yncmMCtV3aPR1Xiho-CSQp_Xc4wX3z6ar5N45h6JXxGS3XNn_bV6dAPOWouH1oWrlX7apCWw0b68WKyIOGdaYyEn12v792Kuu3q5tb3IyUixT7f0lM-wDK1VPHllPHjlpw11XXSQoN6yfPE2pqf_UueJiF1F8V4JUR7OBul3wPsBENFwzSUjzJKPmR54Xg1BJmWl2VhOEHCsDMELJQVnd_rMHm2f4GnSN0CHHdZEdKkIPz9q4ux8lNxgE_QBMJkvXLZxhEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینیYekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
‼️
طوفان یک بت ویژه درگاه های کریپتو (ارز های دیجیتال )
💰
🤩
🤩
🤩
فری‌بت ورزشی ویژه واریز از تمامی درگاه های کریپتو
🚀
برای تمامی واریزهای انجام‌شده از طریق
🤩
Fulgur Pay
🤩
کریپتوباکس
🤩
UWALET TRx
🤩
UWALET USDT
🤩
می‌توانید معادل
🤩
🤩
🤩
مبلغ واریزی خود را به‌صورت فری‌بت ورزشی دریافت کنید
.
💥
🤩
🤩
🤩
🤩
هدیه ورزشی ویژه اولین واریز
💥
🤩
🤩
🤩
فریبت رایگان ویژه واریز از طریق درگاه ریالی
💥
🤩
🤩
🤩
فریبت ورزشی برای واریزی‌های ووچر
💬
بلافاصله پس از شارژ حساب کاربری از پشتیبانی زنده درخواست نمایید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g30
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/30197" target="_blank">📅 19:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30196">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IfuxeXR4jiQ87qvpmTcGWqrkanOtkigqKrA5MRs2Z_neZS-NTlCaXtBsd48bPfYb_rCbWMVZB-vQUjBorachcZvDLuUFOhiHOzYFnGbsU788sZj5qwvBQ1tLJozWy3-_p9MqD-1wQFob4bfsPdjinznUQs0Otie11gMzBb8X4KBHEcO6Ekw_IuYfntnNIkP3m4wdCLjI97EKGDoZrHCouknKq7LqbeInUapFz6nb12bbVqiWl67wVC5PKV4TnVaLH0-bNvFgkRE6_TLort_eQsG_92_I-tXUvHLX_GTrxKcoxRIP-oiZM1qHrg6-ZwVRMEwstGEMYE1iXgppMl6ydBnizAA0Lp0hGyR9ssBMYCzCWlk-zGPuomPOn8ZoYLj7f1ySd2PcJ0YSPKClfrlgA8BjLdYXIY9Ur9wD0g-4ozuJlqS1CXrCUFsA9un96ZKN6bpqX5AtKugkgURDar7_wiauRMFHi-LzHLhdXrUj-kMSXoC88NYkAYyTyddBtJDi5vuhvHXylfUviMqQjWr8ZRkFBnSH1jgfPGTQn5spFoEtIGvCjHN2dJrkTLZEkmb1qtOn30WYCV6Xas06f9v-372DdgoXn4gr9bPw21c2l9awMdcio_gpauu6Su-jJBIYgm_QIGAoQR148T0HQ5O2RmKwtcrgOPAx9pHBUE4qugA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21bbbf6ac4.mp4?token=IfuxeXR4jiQ87qvpmTcGWqrkanOtkigqKrA5MRs2Z_neZS-NTlCaXtBsd48bPfYb_rCbWMVZB-vQUjBorachcZvDLuUFOhiHOzYFnGbsU788sZj5qwvBQ1tLJozWy3-_p9MqD-1wQFob4bfsPdjinznUQs0Otie11gMzBb8X4KBHEcO6Ekw_IuYfntnNIkP3m4wdCLjI97EKGDoZrHCouknKq7LqbeInUapFz6nb12bbVqiWl67wVC5PKV4TnVaLH0-bNvFgkRE6_TLort_eQsG_92_I-tXUvHLX_GTrxKcoxRIP-oiZM1qHrg6-ZwVRMEwstGEMYE1iXgppMl6ydBnizAA0Lp0hGyR9ssBMYCzCWlk-zGPuomPOn8ZoYLj7f1ySd2PcJ0YSPKClfrlgA8BjLdYXIY9Ur9wD0g-4ozuJlqS1CXrCUFsA9un96ZKN6bpqX5AtKugkgURDar7_wiauRMFHi-LzHLhdXrUj-kMSXoC88NYkAYyTyddBtJDi5vuhvHXylfUviMqQjWr8ZRkFBnSH1jgfPGTQn5spFoEtIGvCjHN2dJrkTLZEkmb1qtOn30WYCV6Xas06f9v-372DdgoXn4gr9bPw21c2l9awMdcio_gpauu6Su-jJBIYgm_QIGAoQR148T0HQ5O2RmKwtcrgOPAx9pHBUE4qugA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی از انالیز دقیق عملکرد خیره کننده بارسا هانسی فلیک در این فصل از رقابت های لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/30196" target="_blank">📅 18:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30194">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwFQDyfHsqO_ncFA0QaJ9d1v4caNwR0ZkNabLV5bYFq7YEeqTLSpmqw15uG1hZOMLGxF7y9YlEoY2AWIXyikLiguzFbCJy3-Fh3M00emzUP3TgyfZahN3jJXKWW4_b8vcJy9NSasXi8K4WiUmduReleXDEzHNZzPdLyPX-xxQv_0NABHSBg-ghN72yO90yCwQTOqevfdlApFyY8MBx_U-A4WfKpcD025I2Oz3mu3p4ZfCgD_DwBoLE2iNa4wMbugTcASAdw9vtpED5u4ORV4ot0xamBwvHwDqxrThC0aNNO9ktxY_yCurUKaKxR1uWNRbnfgNeW9A1pyw6h5U8r4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L_9ZbLJYlGJXiYl_JIjrC6qlIBAO3rY2jHLQHjgfS3INZzos6YLQaQoIImqBHPt-JJIVGikAITZ6Bmm682a4aTi8xD6jsr6tqejv6M_eodjwK3rrseExI5uXmTwnOvMVwGMLntEHaRTXR-7LnEISuzIW7iQc9muhfdgWvRKKL2cVgREqWsDfbNrIYegwtSp7B04nknDGvNkKmKGNAwTA-1Ldzn5HO3k0V6n2HrKb504jNPL7dUy9DGSUHUx-lIxJFD8CHVfU3DBM88OLAhe3R8VtZ3bL1r_F1JLvyJmBXOVMWnlbTPz35oZ_r3vsTI5zQjf_1ZU0FDczmC_6qWZSaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/30194" target="_blank">📅 18:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30193">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSidsRWzD_HDsiqzSUsUHcBOvQBLKm4eC3tdlDHrwj2uFXDvBsMQKgA4ARFL4njlYd7WaGiuCgGYqxSbB40vn5IDYiCYp5EJ33GS1VVruWuiCKi9BDVKSw7uPJrJewct5voWKeZt4DcOG1oAjx-necjO_E6QbWHEDfRIry7SG5dqd9n8NcIeEf8nLhG3na7RTpCEWH6TWe7cXkpdyMcAQGFWl8NDwRJZUQT9T1tg4122jnMkyufcIC7KDjmH5RHuD3R1qs2oqs69LZlkx5kv-OpSZqUJufI2JsganAEcPCuob4LUudxxHvwWCu37ejSk8g6L4WF166IcZJL_-n1rIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/30193" target="_blank">📅 17:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30192">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9jwnouI5mnW1Tn2VFZlWwt-Lr93cITN5RGdqFwFTmN212cYnI1yzE6IkKmIwRvDQh3lCVFOJC68b4b0_S8ayub4WJfhQexz-MoD9mm4C9-28vERVLQlXNFOEAJYqSInzDd7s5Wkbshb1EBVmdLg0D9ZD5DULVNmrpzwUiyQvHT2EdFTiDFLNXFuzp9JtzfCdHVK7DIR05LTDAoOlfhUHKoE930qD5Q7V_BQgifq241THzL3UTgP70gb0bijgcJKU1VU4Kb2q9-gT5EJbu_B8u7-z60r7hM5WDLJOIUeXCkYl2PaIXGh_Y_-6c5jTFSvkGGvH5VE9YLyAAdF7ONuMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خبرنگار:
بارسلونا این‌فصل خیلی خوب بازی میکنه‌نگران‌نیستین؟! ژوزه مورینیو: از نظر تاریخی و فرهنگی رئال مادرید با هیچ تیمی قابل قیاس نیست از مقایسه های مزخرفتون دست بردارید. بعد مسابقه الکلاسیکو از زدن این حرفتون پیشمون خواهید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/30192" target="_blank">📅 17:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30191">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=rJ4-i8MES27FLA64UxDF5YFDhEZItpGZGMjvs3HMK5CVB0Vl6VI1Jp1gQQEXANMDkw-N7S7L3uMlKyfUbGykEfVEQJfMnFnPLnqsr4053f2pwqTAV6Tu8_ZyiXBM4eGbw97aGixdvi2-R2ls24HyHAR4A0zuns3x5N577GgpTU5UZzTZTOD1axmNd0D5B_jPhXm77c6nS3DswIHclSdUhBctc1RRfc5nhF7R6ddFlVXunhf8gzR4UJQaOJ-aLqc-8UXJ7R3tMZNvIXBVdcrK-WHeG9TItpPACqm7PzTLAx1RgSGbx5aff02jKolHKO0FfiHGw_6IdXyAlJcpYt7Utw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa95e86e27.mp4?token=rJ4-i8MES27FLA64UxDF5YFDhEZItpGZGMjvs3HMK5CVB0Vl6VI1Jp1gQQEXANMDkw-N7S7L3uMlKyfUbGykEfVEQJfMnFnPLnqsr4053f2pwqTAV6Tu8_ZyiXBM4eGbw97aGixdvi2-R2ls24HyHAR4A0zuns3x5N577GgpTU5UZzTZTOD1axmNd0D5B_jPhXm77c6nS3DswIHclSdUhBctc1RRfc5nhF7R6ddFlVXunhf8gzR4UJQaOJ-aLqc-8UXJ7R3tMZNvIXBVdcrK-WHeG9TItpPACqm7PzTLAx1RgSGbx5aff02jKolHKO0FfiHGw_6IdXyAlJcpYt7Utw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صدرنشینان لیگ برتر تا پایان هفته ششم رقابت های لیگ برتر؛ هر هفته کدوم تیم صدر نشین بود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/30191" target="_blank">📅 17:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30190">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRtmJXyg-J0kL3i2lLPYf_sBfftWvn2XB7fUWJaCjYYNaLf74lsn0R-BRN2fy04H4xWOpuM9AozA_nk0QGE_AG1L_q4vF97y2rj4QsZM2XboTvU_ySFVNV_vXs3YhWQaCrS67K2X7H62-9zoxyfrsRktkqCMB1YZl3Rgh3TxybqeFBi1WK4HKvDu6Pp3zSSiiPrmqM2Ammy3Gd-PKAcw6SoOujk8wPbTHZuvZ2Sy5-rg5N6NNhrMTtUKLWc1F-Itp743hzZvKVLy_gmWO8TgXnIRt3_GJUpu_F3KKZbMrWm3gOSBGGnrrco2utQ4QI_i43PDwPqLAWS3wR9tnFzo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سلیمانی وکیل علیرضا بیرانوند امروز صبح بعد از کلی رایزنی باعث شد که سربازی‌ این گلر تا اوایل آذرماه به تعویق‌بیفته. او به بیرو قول داده که تا آذر ماهی راهی برای معافیت کامل او پیدا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/30190" target="_blank">📅 16:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30188">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=LF7W_EQ-mYfvudicwYwERCIfUKGUHQe7Ah5_TcmBPO4qC0S5zzwKboQV1WxDbPQ9TeXvERrxz9jPEAnAGpl0o9r3ySgJjsuGu62zwZvI8m_kcgydN_yImoX2rjLffmZMkhRd3HjZI5nxrX21Z7sL083aJxDmPqBo7Pji0aP1IPYX90G5QKQbw24PwlVxjUu91nPLPonWcwmBlnnMVZPZOSGg-dT1tMtxabA38BpaqE2t5OPtQFm0QlnCQbUH897ujKx_u_bK-4w8oWKqfXL43qNfEHluWDNWjiswf_IuAeFavFE_BmZVbSLmMluXvG2WG2GwKclIdDK19uGfHHSkBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e07dd6207.mp4?token=LF7W_EQ-mYfvudicwYwERCIfUKGUHQe7Ah5_TcmBPO4qC0S5zzwKboQV1WxDbPQ9TeXvERrxz9jPEAnAGpl0o9r3ySgJjsuGu62zwZvI8m_kcgydN_yImoX2rjLffmZMkhRd3HjZI5nxrX21Z7sL083aJxDmPqBo7Pji0aP1IPYX90G5QKQbw24PwlVxjUu91nPLPonWcwmBlnnMVZPZOSGg-dT1tMtxabA38BpaqE2t5OPtQFm0QlnCQbUH897ujKx_u_bK-4w8oWKqfXL43qNfEHluWDNWjiswf_IuAeFavFE_BmZVbSLmMluXvG2WG2GwKclIdDK19uGfHHSkBIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برسی‌لیست‌بازیکنان‌دعوت‌شده به اردوی تیم ملی برای دیدار دوستانه با ازبکستان و روسیه.
‼️
اللهیار صیادمنش،مهدی‌قایدی، سامان قدوس و علیرضا جهانبخش در این فیفادی غایب اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/30188" target="_blank">📅 16:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30187">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4MvFYwPizY575iFaJyV8-gDFKby8SmFLgmh4SKao82xu_Bui6tD_OWlWRrHDZea70PI506c9Vj81rS6nvD7gnyJqriyfIofdUpoxtxtHh-4L_zQBMtrmJZEKorh6TGUlGygbRg1lTfsIqHPn6RT1_Ijwasr9_y1xNWvr3Hd0ZOuQySZF1j1wdKxJunQbBcHFBKnOr4_IWRgffWXWMUIsk3RQM6GtM2IMLcQrxCzSPue_IXXUy555lNPSGucocJuPFqmN-gbgN5oz1fdaM-9Fs0FFD6_wLZ_EH1VIyV2u5dgaDzYNozus2I8SdEdVy967foL34ql2DI5EZJ54ZG_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانیت‌ژاکا ستاره‌ساندرلند تحت‌یک‌پیگرد قانونی قرار گرفته زیرا گفته میشود کارت واکسن کرونای او جعلی‌بوده و بازیکن‌حاضر به زدن‌واکسن نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30187" target="_blank">📅 15:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30185">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfKMC3d_94C12Z8im3bseEh02OTeGhI6tMGSJzDs12rJm0ES4O5I6r2KLv30Whzcc7yru2KnJOVyXGLE_2Ca5WLMU2roCcAIx74fQwLzGeqG-2f5mlXXqXD1p2nwf7XNFqbZcCLmna8t5INKpEeukrnryCfz45XdWXNPTGKHFyTOBo6p0nL5vH3MqI-MTkHn9G5jOaxGDYOqGyHsWCUVZGoMHld1Br23JGtVeVKL9elB-8fweqbGXyZ_7xonq5YNODJFzbys_F3qLQvvn4EPJM1sYrfgCJUwUuGdn95nMnJ6Y8nTb7SjQK3uMGBRATkK4IP9e2nlAxOUyngXiun1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZUlfQNNhdhCbNoiDqcVC0b5MFMXG2XSOfc3RFOxSsgmhGsIcvj-DAdjsCy4HeMhDTr7wQDGMSSeac1uj0Skf2ANVXl2QmL4V0gLc_EucBlB2xT9CZg8WT2a3BwfK-dP8gIllknst9c0M0iUvGx1CzMft59WfN5UEYZvqAMjxw6_Cnroa4VlkHOXxVFb8513Q3AMqnvsy4Z3hK3lLuHwVgmI1Iru-vJ3Akx2lmOl662zig0KQ7EnjfNB3APhwjt0yGPaiS7RCxNJJvTxvwY4k6nSTRQrDK8iBArnBxIycMfqss9vKTgU9qpB6XAjAIVg3mNwjN7AmGYUSLYVqL6Skw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30185" target="_blank">📅 15:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30184">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O8_WZr3WskXAV8ZhCbDrc8jQgkdaOjEJaURJOHafvK7KYDiv0PA7YirTjDaw1U_dCJ7vOKEN6a7fzpk0vVZxl1QFkkEVYsGjF2gG_rRmlTgNTnBMmJ86woZ6w7N426etn3a0p1ZyQAskkPimViBm5CM2U5ynUwt2-9ABrhR7e15Tjw-CNZpWX8swtK5e4BV8aNI079ZSVjWpjckWqgo0Wzw_-B24nql_oHlblQCnuEFk5uoR1ZtYFlHNYxi-E9Wg1VgiOkkZNuKx5Mih6trfCAzB7Kt9xRWfjKECmyHqgwUtu4tneCvft8IjZe996QSUrHMMUSDqr7E3EQ8bv-uczQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/30184" target="_blank">📅 14:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30183">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bVeZGgusF-PBdZaTYkSEP2EnrtKwQUgUqSQ_8fBGZwFSVhyicXcoOchDiKunlS-gh2EMzorE6wU_UVw61u3zKL4IxQk7-yjmUT1tVyUfe7p6tP-6O8nDHZs9MwCUfT5bnRNa8FiNVemKG24p7nxRNpl-2q33Dyo_LHBv8lbk_QnyCX3d5v3EfYRRWW0Rx96ZN5x2RLtwyzbEBBqVhWwM14k7vaRWrENWXksHBgrSbcNbji0Q8dsUthn85hpYmk1T2QA93tanjkGtBykiMLDvNMZhynq4R5KdrQVJ89E8gU3XPzEx4QWvZmiZrQg1gLK_6Kp5uNwjHa3NFKF83hEUGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیانا؛ سردار رسما به تیم ملی برگشت؛  فهرست هشت لژیونر دعوت شده: علی نعمتی، محمدمحبی، سعید عزت‌اللهی، محمد قربانی، طارمی، سردارآزمون، دنیس اکرت و شهاب زاهدی 8 بازیکنین که برای دو دیدار دوستانه برابر ازبکستان و روسیه به اردوی تیم ملی ایران…</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30183" target="_blank">📅 14:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30182">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVmC5RDc0LiVQyYX49cbxsPfRxIhac1UoGhfZ1svOkn-MaiZE2lRBL9epIEzLr8EITcXOQ2C-uV7SLomEq8x-dIP2FJmhgz7XUVb9GyKoxF_jXaP1OC9Zarw-IE2WqfZ8j7OMcrHM4fAGts_6cj0GHqWxRC38giwixzMNKs6WE-aiMi6o20nlflDBKAG45TCj8Az6DT_B9jRsPQ4xslBodrSguYDnq1tJunCSRfnWw9Y1kzr-aC751yYWCh4UIoy_pd0bfGQ1_zxoaBTWfN0K5TkglE1RSADUonKAcULfkPUI9T7VCbvmGV99jls_N6goOiG8DuZ0H_lSwiRbeqftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد عمری دیدار باذوب‌آهن رو ازدست داد؛ با اعلام پزشکان باشگاه پرسپولیس؛ رباط داخلی محمد عمری ستاره25ساله‌سرخ‌ها دچار کشیدگی شده و به احتمال فراوان حدود 4 الی 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30182" target="_blank">📅 14:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30181">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
آرزویی‌که محقق خواهد شد؟ درحالیکه خبرنگار فنرباغچه چندروزپیش‌ گفته‌بود آرزویش اینه رونالدو به این تیم بیاد حالا رسانه‌های عربستانی مدعی شده اند؛ رونالدو در نقل و انتقالات زمستانه به فنرباغچه خواهد پیوست و شاگرد کارتال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30181" target="_blank">📅 13:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30180">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4ME-oMSII2MxiVVWMtUa1lGsFAANbH9ptZZrRn8O9m7tojFyoDtmwisMkw1AHvUodRJLW93srg_ebTWcpWU2GHRVwlkazeKEa624BOFj4FrcU0ab5Bg4ikohFlVju5CZzjCQI5Wq2Ifbw5LtitZymnOfjyUGatscJxSi7ILxFNtp3I09OVLLz_1BdiaWPWSrsOFwPpANSfZGpvKcKpGtmpsrTwhYJ7W-O_dqg9Fw_LnT2PYtG4EKehvdFVMW8Oo85phzcl_3OQyPPQa3ToJUGZ3pVpdEAN-LU7BLdYlF7__gjo2qkpziNln0qXaBiyW9iDM4T6suRN4zG1eeRDymA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
برگام‌این‌چه‌درخواست‌هایی بوده که بیرو داده!
‼️
علیرضا بیرانوند درخواست معافیت پزشکی داده و دو درخواست از کمیسون پزشکی داشته که اولیش این‌بوده‌گفته‌چون تتو زدم مشکل اعصاب و روان دارم دوم اینکه گفته در سال‌های گذشته رباط دستم بار ها پاره شد و با این دو دلیل…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30180" target="_blank">📅 13:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30179">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9om5WKuR9cjaFvliULWxu-ackRGUMBEu3fzRMNJv3jUgBCrebKGVzpX7oC0-NjxSOXJi2ZmfIMKBort62udDU-h9RtE1Wg95Kf6ZV3SeSVH5i8q4kETjBb8i6_3LM44F-epu09ITYj3zRYsSrfQ2X_3xrmrepe6s28Opm1nYnTCLccJgCgVk5EEp4NIjyXRBFlXhFE_v4IEbLxITC4BlKOdjLM6ZwcTKwZ8Vi1La6MlxFNTGb5aitHU5yd96fd3V_CpizkTWmFK4nVCdRzh7MPouCx2kFcRdKnJ_R2CTV5jxOCycXc-5H_NLZFOR9VOmpqq0OUMf707RZBxQInA5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/30179" target="_blank">📅 12:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30178">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSwRud_S5v4puuIlo7fxvf3ZE7FbWjWel9rBJ0VX08rR-4CQQgla5CJFTXuOcVujzv2h4Eu1whZATIAndnUcWwfCJWPLUwbPQCVmIibuSj7QCiR1YDP-feaG6bhPGb013Wz4tP3Nr1rXkMJLMPHko_EFp5UQz4iRDvyc11718oeFU59Ho-ZfdgYYJKh9nRnZ3XQD4eHDaITfJW012-l5Lt0jRyYD4semkewrvedsSREeMeNVokrTVxmNzlfW00M_2RKFDryUX65whdgbkf0IyCkQSIfwc3svj0JrSUjlW-S5_m6GguXwKllanRJQDXylwhd3cefoN4PUPmExIGTStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه بان تراکتور در جدیدترین درخواست خود از سازمان نظام وظیفه خواسته کهه یک ماه سربازی‌اش به تعویق بندازند چون مریضه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/30178" target="_blank">📅 12:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30177">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qighfA2dSW9FiiwDN1N0xdyXR_U5hXSjpktW67k8Qg4WRdsWumcCAZIQld2NlRN48RbSL42y3G9N6jXh5FA9HQVl0pKv5-2LpBf5o8y08evB0vjzrGugj0uVUlJqah4DDrLPLA0rTnJHMJoAgM0sQ0AYepfnrNPne07zGVt2iOurQGJ_JUsAoazNUyPLbbzDEkELgUqF3Q7QRdiu8zlits0jcb-MnqpmrcnPunLkkj-6mCRn70CQrZbJV0wVNENhHCd-x4tHoy6NObU69fTOOd0F4wV_apXq84XelohCWxDDroV2dvaO9QxjBTDyLNUk1yLpRltRvUjUp3W4RWHwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
نمایی‌واضح‌تر از خطای‌شدیدی که باعث شد فده والورده حدود یک‌ماه دور از میادین باشه. تموم کارشناسان گفتن اینجا اتلتیکو مادرید باید دهه نفره میشد اما داورمسابقه بازیکن‌حریف رو اخراج نکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30177" target="_blank">📅 12:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30176">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b904658a51.mp4?token=O-YgSnUG6ScUQLuHmmTzyKB0ebk68MaHY6cIh8aB_FDIU1H0qq2-zDD3Iz1qnoN1Bp-VKkrGnNNwSoRUg2qKzZPQOgnBqnydI7IZGD8stQHS5QT8zg2A69QxSruyL2Ze4X-xIzN_4oFNj0KoL-PdDhHaNCBz4jfghEMMStKebU2sR49ETaJFWhdqYLA8xLuFuI0ns3khHruAvBHazZEdalVy3E0w1SgWKUSnPjyrz1IQuat_Tz30HpW1m0lzRfQv1ExusjSY7GQpj_P2JpZUbQUjJt0b47Tik9XiYh8T5Flt9eHTnjbTnqn8-oObs5WFC55sngg74jJJhyJc3e73Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b904658a51.mp4?token=O-YgSnUG6ScUQLuHmmTzyKB0ebk68MaHY6cIh8aB_FDIU1H0qq2-zDD3Iz1qnoN1Bp-VKkrGnNNwSoRUg2qKzZPQOgnBqnydI7IZGD8stQHS5QT8zg2A69QxSruyL2Ze4X-xIzN_4oFNj0KoL-PdDhHaNCBz4jfghEMMStKebU2sR49ETaJFWhdqYLA8xLuFuI0ns3khHruAvBHazZEdalVy3E0w1SgWKUSnPjyrz1IQuat_Tz30HpW1m0lzRfQv1ExusjSY7GQpj_P2JpZUbQUjJt0b47Tik9XiYh8T5Flt9eHTnjbTnqn8-oObs5WFC55sngg74jJJhyJc3e73Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه‌های‌محمدسیانکی‌گزارشگر بازیای فوتبال به شاگردان در مستطیل سبز که منجر به گلزنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30176" target="_blank">📅 12:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30174">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=cyH4Wnf8ZTrLDk7pHGo4vgCHsMF9ZwPFEaA9-vYvPjfvyJHiOqk6MX-l3SH82EoYe22un1_A20dWFYnOZ53Z2_VR1f1E9eTlgrTj1W1HZKoCeu02i9cVgUknMtvkyI761OFML0QjuMJZlg2Zup59yISffSwM8Zo9QNz7olHMyPheaSmkxlnsmbUHhHlki6nhuV_Q-QJOpw8Dl1SNm-2T8KPWUxd8behfCl-fQY6l_3m6E0ySHpP-PoMECd-Rbp1mKrb3twl4N2cJDgJvThknbFTSrVPHo_tL9HBIpVOSm1hTidASq03FhA48k-gNt2bAyMvRu-ANGRGdNrwOmYXj2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42e997aab4.mp4?token=cyH4Wnf8ZTrLDk7pHGo4vgCHsMF9ZwPFEaA9-vYvPjfvyJHiOqk6MX-l3SH82EoYe22un1_A20dWFYnOZ53Z2_VR1f1E9eTlgrTj1W1HZKoCeu02i9cVgUknMtvkyI761OFML0QjuMJZlg2Zup59yISffSwM8Zo9QNz7olHMyPheaSmkxlnsmbUHhHlki6nhuV_Q-QJOpw8Dl1SNm-2T8KPWUxd8behfCl-fQY6l_3m6E0ySHpP-PoMECd-Rbp1mKrb3twl4N2cJDgJvThknbFTSrVPHo_tL9HBIpVOSm1hTidASq03FhA48k-gNt2bAyMvRu-ANGRGdNrwOmYXj2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کل‌کل‌کردن دوستاره‌انگلیسی و آرژانتینی در بازی امشب رئال مادرید
🆚
اتلتیکو مادرید: جود بیلینگهام: تو لیگ قهرمانان اروپا داری رو من تکل میزنی؟ کوتی رومرو: تو جام جهانی داری با من حرف میزنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30174" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30173">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/driLqOkT1g6RSqdPZOO7njs-RsbNrmEZ8q8ETRTF0NPr6_HhnAKOQ6riNSeJc-wNnZ8KYA8cVU72ZM5YnC8yaALufQA2c4iKj7OqWTpjmSJ1__ZUZqXP6XQztHFvWD_xG5g__7sphZ5CANPgEcAZpOzm1D074ZmbeaI-_zjSW0tbznpexvezQONTkvrNf7VnMPxfzRACNXQH0P0Wb-JtCaxpkouC1zVD2irpLFrKrOCWbnkI5pr-KaSluR5XnNgjlt2w117EOXbX1QIdBMAF1nu0V58XTS687Qa1Fs-40I2vbMjYm7DvLr7kBNsFZDVUt9bjxHzuMgvnSfaPmNJaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینیYekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🫰
لذت بازی های کازینو با 100% هدیه خوش‌آمدگویی تا سقف 100 میلیون ریال
🎮
بیش از 5000 هزار بازی کازینو زنده و اسلات
💲
🤩
🤩
🤩
فریبت ویژه واریز با درگاه های کریپتو
⭐️
🤩
🤩
🤩
فریبت ورزشی برای واریزی‌های ووچر
💱
🤩
🤩
🤩
کشبک اسلات ماشین و کازینو زنده بدون سقف
🛎
گردونه شانس یک بت با هدایای نفیس
🪀
هر روز تا 180 فری اسپین (چرخش رایگان) در یک بت
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r30
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30173" target="_blank">📅 11:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30172">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWneZox1XSVjfzs2o-9oEqdomOGgQPxF7LBsPnxxUbJ9GhYZ_C-fLzDqwvFIf4z5cVl4UAN8HNboZk0fclWuiSevUSwA5S9kIBKbsAsLxOure3xtVkQg9R9dEEgeVLmZeT3pSxVrtknqE_YSC2zz-gbyC6XuyzNNpdJ-7QMwHrBE9ZQW_wMG3GRF-JlsB-jSIoWSZJNskHcAqWAvUeHZA8pS4ii71ioo5BrTaJOmEn54ZGd-TR6Nj64Mj-85T1aLoHgdqAyg3aRRi0cNeQs_luN5gRpKEFd_uKZjCQ_1OJqc5Cv6xhn5sCAGmGMdGK_KLbOhiOl5m_tY0k_qvtRjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
دو مسابقه استقلال-شمس‌آذر و تراکتور - فجر سپاسی شیراز در هفته یازدهم رقابت های لیگ برتر به دلیل بازی های آسیایی این دو تیم لغو خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30172" target="_blank">📅 11:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30171">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpV-59mAU-tBR7DXe_fDD5gPxUnpnKHv-xNV4Ona5l0BCtyUm7QxhVRG8uoaNhC2g6dO6V6VOm_7heIiB0uaVsiiGl-cw6r-4D90eH07mIDwem2Y3svG86_d90QgOIM6VAYxOvS6vgEjq8b9_Qh1CxzNgLoRWxU7Rn0Oxwlfncoufwb7KVfvcbarQM_IuDWhxnzv9GW527oKqWMvPkOZyuVLa6HWJy3pwDUwGhQBghNmvGJrnhndUWDylvAV06TZgjS6s9T9tpiMil0P_FKqATqePqMbTYHUmKI4QzkoZzyoQY51CY9MeoRPnSBvOPyWjVEqi0NG8jS50gw0Q0iTSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت نهایی سه نوع آیفون 18 پرو، پرومکس و دائو اعلام شد؛ آیفون تاشو یک میلیاردتومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30171" target="_blank">📅 10:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30169">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyXduN1jZ1gv5DO_XnC6Asbg-WCiR4FHlwBJ7ReuaxgCrRbPsRvx4cb5NIrwY-23tzUq9m2FUfAQ-3hrDSsQE4hQCuHrKfz8oQZlHQAQOq9pf41IrxzvYYowDr4Ok3crJfqPwgultPKD6Bv7LU8MkPtoDgcC1P4Hm_1dszbAsQndpgeidaR-83mT0FYWyB5m_JvpJcsWtet22HlINsx0CbeolaEsqZsZnh8v8fvXf7bFcVZ9ifA3IaEziM178uDER0nCK10ic9_BZWwhe8_HVi_MZgvWlpt3sgZX_PLKqtbkMQcb1yFIgpCkgg1jMRCe2OP0yh4xSupsluyzz_wkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gX0KYTBAecoKfhUX3LqgThF8vfjjMM6D5MGqk81DDLSG6ty0GtK3F2VmhoR1FnmnYSWeC_9D5SxKphSPPhcfbQ5X5YiHmyfbtAaCPlGsLre1f7RXeXZ6iHD19L25uS_SKGJS72Q_r-vYsKUX4OdXHBTe1gnpoDNYD31yoQ6UxlPqXlzE_4tl6IR5xCuLcLPxGlUwRNKRUv4Y0D9S8vqnWMPUN0AAOyA6IcvS_MyyAArSgNxmr7A_h-R_nWtMoz6LT0TCjpderurZK7pQoAViWGDbmngA3da8LQHx1kAcEIzIk2ApjcovXvFuyktxNCNGgdfGyg0INZIdJBKEf0m9-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/30169" target="_blank">📅 10:31 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30168">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rUB6Do67XHhluEMILsyxCWDBvv49GgL9butaw_7X0lLxht4An8XMo1UnZGADNdprJqIHdft4xq0Dr1fXU3edml7pbkBdDRPGY8Ln98KWPy4X20QNrmNGBrtDNgAjLv1YO_pESXFajPoq1NkMhJwSxboYquNheH5LyH_qGsvmX472RPSMR_P0SVRpVQ4ZrgJWCxBxTTpVGmTYUK-HMo1O5oMIbdgUtZ5tkqau84ASugk0huNrPaqOGaENuhh_DrvKFkAKe_OiHVIef0lwzsmX6__-A9yrW_kJvCUJjm2WP42Is6nSLB80F8Gsq-mRzG87GW33yZ4MXDno8KIs5kWVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اولی هوینس رئیس باشگاه بایرن‌مونیخ: فروش اولیسه به تیم‌رئال‌مادرید؟ ازخنده روده‌بر شدم! حتی امپراتور ژاپنم‌ بیاد پیش ما اولیسه رو بهش نمیدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30168" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30167">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015580725f.mp4?token=lybBHyypqLbCocQHliiD3o7rxpI3o7n9y8ScbHaT2Dpx7kzOSWRS1bK2VjjP0MXOQ55Jgbz4SwCoTtt2Z2Kzl7s7JhlKlUWKFl-u9x1v0xfENmAwbHcYVSWxnGwInrweNM9z0y6FZMexE4TC1u36Ntm26B1ydecmMA0FVTkVl9rZwsSmE1KSNgqaOH8TrE0QnIphrydnQjqJvGJH9AnAKZ8WsYJlR9CrODVj1C-RJJP57T-CnSmmS_brofdjOzsXJod_p25S78MkDrs4veD7-Mfc1qEBb5QWEakUL6qAgZs6lszP3LVld1JyEixxRSCbccGbQLRfrC5o7dZOPawVFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015580725f.mp4?token=lybBHyypqLbCocQHliiD3o7rxpI3o7n9y8ScbHaT2Dpx7kzOSWRS1bK2VjjP0MXOQ55Jgbz4SwCoTtt2Z2Kzl7s7JhlKlUWKFl-u9x1v0xfENmAwbHcYVSWxnGwInrweNM9z0y6FZMexE4TC1u36Ntm26B1ydecmMA0FVTkVl9rZwsSmE1KSNgqaOH8TrE0QnIphrydnQjqJvGJH9AnAKZ8WsYJlR9CrODVj1C-RJJP57T-CnSmmS_brofdjOzsXJod_p25S78MkDrs4veD7-Mfc1qEBb5QWEakUL6qAgZs6lszP3LVld1JyEixxRSCbccGbQLRfrC5o7dZOPawVFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
👤
گلزنی تماشایی لیونل مسی در بازی بامداد امروز اینتر میامی در لیگ MLS؛ این 930 امین گل لئو مسی در کل دوران حرفه‌ایش در فوتبال بود‌.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30167" target="_blank">📅 09:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30166">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKKn3pUPsl0-hhSPrPlrzI7KEtnOx4fvfpNTvMk8ZwAx2loA3W8UaTj967mXQHABd7uEePul5-TGAOlAGCc2mxTqZCKwCuKTKMCNA8PItV02XSGKQ8NbOP1s3V1IBLvmCKrEcZfVlElDbqdnJawq7g_AORt-u_Ylt1fsEXdQWd_wmPw0JgjE7KXrNZU3gOYrnalXU_CY9caUAIihxi9rWR4N9PxYjzYKbIGu0YGL26o48tj04ZKlmMvFd-qv0hpyhM_hDV7Xwg3U1_WbvMcDU36D1gxf7dgqteM43vtCd79zc0VeBQZ2lAdZj8C17tnak_XYZD1sL9eGKSNz52TJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30166" target="_blank">📅 09:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30165">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=frJke0iuHeTWRpElCRVCEbXeVGtcg_2MELjU24ijq3ULGl8wgmToz1dwZZ_Dy7olbvTFrl-MXE5ddsOXmaj3ajc4vfbBg1-wslwJ5GJUeYTgFaawCEZ1_3-ynN40zwWFHAjfuWTvKLBWMrHOjCYCpZbuhP1XBEJoMSZjP_jR1NIESCX3XgXZRAuTKPnP4iwTjXOQ39r6vPo-Ku8JEhteZY2Jsn80_xyAdfHTqcXN7cNBnj9aKHGyssggNG5ePOT1QwLY6mk4KOKduTRu43m8DuOGLgPF76HRNAWWi5Ow37pBh7iyDeQ-O6R9NVFTHeIAeMSLpRkckL8Nz7G7ht9MgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8af73188.mp4?token=frJke0iuHeTWRpElCRVCEbXeVGtcg_2MELjU24ijq3ULGl8wgmToz1dwZZ_Dy7olbvTFrl-MXE5ddsOXmaj3ajc4vfbBg1-wslwJ5GJUeYTgFaawCEZ1_3-ynN40zwWFHAjfuWTvKLBWMrHOjCYCpZbuhP1XBEJoMSZjP_jR1NIESCX3XgXZRAuTKPnP4iwTjXOQ39r6vPo-Ku8JEhteZY2Jsn80_xyAdfHTqcXN7cNBnj9aKHGyssggNG5ePOT1QwLY6mk4KOKduTRu43m8DuOGLgPF76HRNAWWi5Ow37pBh7iyDeQ-O6R9NVFTHeIAeMSLpRkckL8Nz7G7ht9MgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه جذاب از عملکرد کریس رونالدو و لیونل مسی که ابر ستاره تاریخ در فوتبال اروپا رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30165" target="_blank">📅 09:13 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30164">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myOFWkPatEO0owTs86TFqAXXP_2mowcgX7nRmtQaWPjQiaNdXuHnQsQqeN5kjPPwnwHCbWzUcglqsububCTR7tpRaIYd512KUkHWPv5SRAN2hVMEOTwSauyN2LjlDRUND2JY2uCsCCvi-vXnclpCwDz25KTXwGDCiyyhliMUX5Sf7VwT9aLc05wLLBLF30yiR8nmte34DesEXa0aXWpj-yyYdf0VTd7CLJhir9HUH4AlJA1Aq4IjAZ8mklfgEfhKLMyo59PRGZjE4R6kZfALlTVuKnuF3CInLT0zjkLAEAi791euRlXBP_QxZy_j8MZzSiLF51jLokjQy1BpVVO-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/30164" target="_blank">📅 00:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30163">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHdLKZeXJPxv3AqifaifBuXCtvgqf4aC67f_g7YFR4VnAaOGCMBd9udCcS4t2bSRzbQj6WH3y5vqwuhdDe39FQyVoSzLZBANBXg1JweuGwUBZPwPCeHGgCAGz5agvzkdXR-Xu3BlmH5OAxoxqYx7vCtxKdAJRzDclqR5XLdJGIPJjsoj0kR2v-k1xFTKt5hFdyfmSobYQ68ODBJElxLuKnT1k8m8TkazctwCwfEbvuWM4Fg1Hc13WaXIGAriiPHYshdLQqNhwtpLnYGZPKt4yud1JXoF1bXeH6w3T3owA_SX9t164oRaHPlxDt-w4mYnO-EnmjHrSc4GtZ6jVcw-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
الریاضیه‌عربستان:جدایی‌کریستیانو رونالدو از النصر در ژانویه قطعی شده. رونالدو قصد داره به فوتبال اروپا و لیگ جزیره برگرده مگر اینکه باشگاه الهلال پیشنهادی نجومی و سنگین به CR7 بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30163" target="_blank">📅 00:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30161">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVnXDskv8rCVbzvRYCBO8ylQAw3Jjw0D_Eiy96fkVWKD5QGg6GV3chxg9hOTuFzesaWjwC3R44Ztn4LStvcSe6q0gOAKP4tDwCiN9U1nbEKa5imKy_2y0m48bqJSoNY7IvFLAUZv2XGUFvgANHoX_1X62yvOfvo40-u3240yw94h_FPIIusTpmc7Sg9RR-8WD4VnAUf7hHeAhANzrmn6uVW8dLVVXj9bphbjLt1_V-6j_raGxDKCJjwHCXqS2xVC81jyRhVvBwqZPAbPGloLwgHWXKAjW5EWmf55KjGAM8zZ3gKBisDOxT4aNMW4zbIRa8d0ShAx_pBaWayKMgP4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ جدال خانگی لیونل مسی و یارانش باسن‌دیگو پیش‌از آغازفیفادی و بازی‌های ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30161" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30160">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klrT00UwZlJ1W-vGe-Lp8MbdKV-PD1qZaaXN-1KEZY-UBlDr5CrMeVzFn_ZiKjISWH441e-iVWEoPHLItb5o_dQuJTt6hcZF3-EaYzlQY7mJTYoT5whwQ-iY2GT_LYn0shvM-aV7JADl1GzS9Orn0LSwqW_5E-KusWVZBKbSaKRe5WYimD1zpgYCZ8pP1zSfCnY0kyp6E1-zfngWYdS1L3_ccXfOWcY0wzsMrlFqlhA_oL7ApfsPbl_942A-mmeYLSBDeWCXj6PkWJ_Lwae9I8TM6E17L9a4v1vpbSHiYDj9JW1zO942cG9GrIYABA0otIfwU-4Op10uFXFbazZhqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌بزرگ‌ال‌چولو در دربی مادرید و برد اقتصادی لیورپولی‌ها با تک‌گل ایساک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30160" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30158">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30158" target="_blank">📅 00:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30157">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba92349391.mp4?token=U6Zz3xZdjI3RK267m8CbyR_28SytkeVwg-itaPZYt_ovzs-2mfecJ1xoEycpyVeN9U4JRHzzgf02AeQdU2AGawo0c_UF_y3EwOptWgVJqa9RyhiiMzexX-XU3vIFG7KjEv4_Uv_rH_hwFcUilUiihUQ9loD-uUpzkrJdG_V20jUHrhGOPsxlgPp1-gDZV9eHaWs8lxYt20IFeq3BDfVSj41Fg7FvQ01U9awli9NQvVo5jvaMj2e8qYo_ZQ4CA5iNL9zKYx7GaxxS9FpXQDhuPerDu1PvOgVPQyLZGMXbylJKwFIx6IthzA5vTNrHR-AI4YLFHCFNB3wtd1OjCwwVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba92349391.mp4?token=U6Zz3xZdjI3RK267m8CbyR_28SytkeVwg-itaPZYt_ovzs-2mfecJ1xoEycpyVeN9U4JRHzzgf02AeQdU2AGawo0c_UF_y3EwOptWgVJqa9RyhiiMzexX-XU3vIFG7KjEv4_Uv_rH_hwFcUilUiihUQ9loD-uUpzkrJdG_V20jUHrhGOPsxlgPp1-gDZV9eHaWs8lxYt20IFeq3BDfVSj41Fg7FvQ01U9awli9NQvVo5jvaMj2e8qYo_ZQ4CA5iNL9zKYx7GaxxS9FpXQDhuPerDu1PvOgVPQyLZGMXbylJKwFIx6IthzA5vTNrHR-AI4YLFHCFNB3wtd1OjCwwVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30157" target="_blank">📅 00:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30156">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldyeARofFV2V1TesWmOqq_mGyxXJF4NytbsPxFqZNTX8Y3YNORMw8WRwHVGqj2xIbtCc8ws3bJajK3CWUaEaYT7iR0U8-7Op7r-URvEOStLFFnBIaRwTlNzJJvxTaIbBYh2i0TOq6CMD4kOlKa1_j8Z_Ks32HmjOTCjQ4WamP57TQl9RHXRtZ2e4kxMqKj-Wku7pG8gZnA4vUiZHlw3rhJKWwRmdafvAmdS5HXYP93lPaUsUvgj8WaSxa-bOwYMLLMKsb_3c_gdElzC4YZnSfus6ykeeUBhIRWWwG1n69gayLOGfKFKIAk3-MWVOi20OedDMFVlnUSVhplFOZyUL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇦🇷
کریستین رومرو با سران اتلتیکو مادرید برای عقد قراردادی چهار ساله با این باشگاه به توافق کامل رسید. رومرو در دوهفته‌گذشته پیشنهادات دو باشگاه آرسنال و بارسلونا رو رد کرده و گفته بود به سیمئونه قول داده بعد از جام‌جهانی‌راهی اتلتیکومادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30156" target="_blank">📅 23:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30154">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bj00u9Sj0ZHcz5i4MJ3K9ibKlev9YqlLSE1O2yLGjzodC546zMhzC7NInWFyxOHBccvTKfJIIlMB6G83r76CQLJrakfr2E4HasAbL12AjdvLVvkNZXlsfp-gGk-EHJ1rzWTkHfdLoCi5aApmggVRXHVG0QTkl7MT55_06QGdo9HAvXpIO3OwzSXjlUhMCNRLLA3N6bh_M_9GyCPjeYOIvKdJLyG2IAHSl28trNva18Vt2rCHWN4d-x2ao15c6ARviXhdcDch14fUOPyJb28x_-StuENmYUMNS6kr_UkV2pW7oMO0RCraGs3xwMtpsLZcy40pb7r6emptiAuF71Qftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HCR4GCEsCTOrsymGJZR0Bt6Kwjsm_SA7BMGHUP77P09JYFKH9-__OTjL1HwknBdYVM3kF6VBPUzw2laPKfuH9_LWkPnGmojYWVPKaiX4eFpFZNd-_6kwv475FK1ps_aUXx8crnPp6bXlvoZUSifwHuu2nvZK7kmi740if7oBl1IbgY6ydhxsw05KIo2kp2Gx_Yyq6YNC0hBf_YSgJvQ5lsdIw22yMoIzjLBokcf_LZtvQaoH_wXi5bmIrVRq3ZTu64dK7dHukhOI2O3yEN1UV99G_v-H61v4J_JUConG_HKBwJMazeSxMKHMKszwWj4h17iytLhGYpg1w8jTMWt5TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد رافینیا و یامال درفصل جاری همراه با عملکرد کلی رافینیا در بارسا؛ بازیکنیکه بعد از ژاوی داشتن میفروختنس فلیک احیاش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30154" target="_blank">📅 23:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30153">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cm-FsOGTfW1_-NwCbyrnSgSy774Q3UWlniDI0lWa2qaEuE_ozvda-FwAwyX2fwu0FomPENdhV__Mp50Nh4U2axtRBUhQRWp_UTrtwBR-k63oikqOM8u65KdGksbv0t0Fv7tj14WVwBq6IzMqdq078lspXqfa5A5vBQ_SJe8CqQAff3xRXryePTaPFG4U9ncHE8pL84mT71vu2mg0NXFcDrz97lDL6jrx0B2XOQNMHRWkmV7xMCpw4itXRqBxly4qYzucEEV27eGsmHQtVjRcRGesLeD-quC50TKhAIGjizSi1-wm12RG8zSFCrYeX8DGDc5B9lKi2yKsTWm7U-R4Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
مصاحبه‌‌شدیدالحن خوزه مورینیو علیه داور بازی امروز مقابل اتلتیکو مادرید که از نگاه سرمربی پرتغالی رئال‌مادریدعامل‌اصلی شکست تیمش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30153" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30152">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNMGO0IQYpy9Vrz6XCs7oX3QWexJJ1CCNCHy0PLFKnbyn0c80_9S87VIN_50aoX8IrAh9QjvNNYvn16VE9u_k8guKq3MqA_IwgdJz3Kq9cDtQW8oi3srlsuyuTDCVYFJ4Ao2Kls-Bw8eLlhYk2k6WSDyd9j7qewgkGkWVzUUnvqzqk5M8QxWbEjz5twH3XooQwFaRq52XNgN-hRFo3yFPY0ug_qbvsGVpe1Gxu--i5x9q354B2nhgo5_uQQPX3wHjuhoSvrdLjTj5fPLLzTXvhhLVRL9KRg3y8i1kVpSuUlPev2ghajUYdNEI3kI3BEurdml2TIiS7nyLPmSiOy6KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه آغاز فصل جدید رقابتهای لیگ نخبگان آسیا
؛ نگاهی‌بندازیم‌به‌تموم‌قهرمانان و نایب قهرمانان باشگاه های ایرانی در رقابتهای لیگ قهرمانان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30152" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30151">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30151" target="_blank">📅 22:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30150">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTybsO44c4pkXn4tqdyGdRyzxUsX5hY5F4uhZPy7NoQZ6k3Xw01K0YjhcgBYF7OtlfZ-ouEkPI9ilM89ktyiboVuuu9GT0xaLc5zv7KU_wAR1sDDCsNEFL9AlfL-7ByF2YnxTm-nNO9ji95sLY4XELyWryhaDWnbTiJFfIukz17FDmbIFz4jp_LTmvWrd2HmQIo79Kzuqqyk5kSGM8UOyusqI-4id5_iq7_aRbZxF_wqFMSb2lNriv2sEtO90y3TlDjb9jqrAVv4fKtgPsSZnA2VqcYp-Np_fhxtR-r7685s0K6x75nVEO_zGrju9D8CaYcdrgAWICCsxJLeAei2HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار رسمی باشگاه فنرباغچه: بزرگ‌ ترین آرزویم این‌است که کریس رونالدو قبل از خداحافظی از دنیای فوتبال یک فصل برای فنرباغچه بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30150" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30149">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYGAUn8tcpZOka2ClpPS3TVwN0XAo-Vp_kyPBwHeZcDpAIkIxFVGrF_QMn_l5hUzQvhvgayFn3_FAsS8eQpR3-i_wmfbAQhcgGLfcqC0EGl4KKiqNKtIYsKDTZPdec5P8Up5_OwFAgIoO67IlVkK2PcPGC_hwg5P2z2INfLLtW6URve7t_OZG0el-t29sSWI1XLkMn9XbzATQjnk7qKje24lmde_Vl0Y-n7voxMobHqSTaEqguTjoLca6jkInpC7dEU9I-x8_cMTEUnMAT0oX4Qt6qp8xf0CtSM7a2w2yu90AEOxe4mcL3_MdKfZTd4vh3PXkRSmLGi9_KJl60WB9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فده وارده کاپیتان‌رئال‌مادرید به دلیل مصدومیت 3 هفته دور از میادین خواهدبود و احتمال داره دیدار الکلاسیکو که سه آبان برگزار میشه از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30149" target="_blank">📅 21:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30147">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⚽️
⚪️
شبکه رسمی رئال مادرید به شدت از عملکرد داوری دیدار امشب با اتلتیکو مادرید شاکیه و گفته سران‌باشگاه دارن برسی میکنن که لیگ کنار بکشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30147" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30146">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKaHiivYW_8d64cJx0wLzn4cCD_NXX4Waz1LqS07p3LEmt4RR5LztR6jNLncnV6uCcveI6fcsEZyqJ6LeMWBB3VS__fURBev34O1HIlFE-SV_gMqL_xublcG1AJoBcmHyo_dqp59K7w3yd3EFphGU1fA2OQPAh0hQmZJmSVtXS0BgPO8lN3rbHEo4nbfSqmf0S_cw8S1LPEA9AH9WSywESDKI0sDH28DzXMmKpIGj_q-hhcbFedN092PsNs4wtYpO_aslmfUThlCIjEeXHRSUkZBrpsUBJ14lL1C-_bi1y8ypn3cbzxdwb-G5llQj-ix1wZTRaw_Z8lw_e-bTOMpEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30146" target="_blank">📅 21:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30145">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfGut7F_BiVlvdcpPQGa9pVer2mqaNG0EDK_qylNvypSIivp6RL5WK_VxhLZNWIRX5KfvHaI5YOiIxVF3DtmrD1NnoE1YvomhQBltJootpan6szOfsVSkaV707wt-OWs54PCEe1txu41g-K6AHygQa93Dfa7AHsBMlr-3rDEOxVMpbQBRA23XENpitdFIhXpNAMEAWfR45an31e59Qnz4kKJYT-PFzC3lKhE4LPQyKRqbdVryphfXCbDyMC5luKynnQDEvi-RUFMJ5Hf3nc3vC57o4NrVVsZaaOVvLHJLvg2pzvN5AeLSKYDDioZiD-ETOaczl7wZh52pYfGY6kBl8NM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfGut7F_BiVlvdcpPQGa9pVer2mqaNG0EDK_qylNvypSIivp6RL5WK_VxhLZNWIRX5KfvHaI5YOiIxVF3DtmrD1NnoE1YvomhQBltJootpan6szOfsVSkaV707wt-OWs54PCEe1txu41g-K6AHygQa93Dfa7AHsBMlr-3rDEOxVMpbQBRA23XENpitdFIhXpNAMEAWfR45an31e59Qnz4kKJYT-PFzC3lKhE4LPQyKRqbdVryphfXCbDyMC5luKynnQDEvi-RUFMJ5Hf3nc3vC57o4NrVVsZaaOVvLHJLvg2pzvN5AeLSKYDDioZiD-ETOaczl7wZh52pYfGY6kBl8NM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛ ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30145" target="_blank">📅 20:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30144">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=JYZJ3b6qfwhiEHjgKHYY-msDAeCO-Ll5HTZrY61j_vcUNbaTCSrK3kyF4UWpd05ORS6biSdwuiyTK6LwiEV3PjelycyQGFKRvjHdE1yWg1cPbG9pGy2784uLCwmDB0DYmPz_pActwywtQ4cGtiuB9WE2xREQOdPZraciHsLSrFHx8lKdMdlyi5HB0o68cWFly1OnUMZT-sbwKTj95STyTZvoO7mrw6QWAy6MednKG5VNsgvKQh3VSUY5MVfi0oSU-GpSlWJP-X43t88XSm5hvXK7vBft3y3klrv1wrJWeh-W2ANfwhPOKV3gR3KbNhBXnbbBYAd__t63J_pcm_zijg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=JYZJ3b6qfwhiEHjgKHYY-msDAeCO-Ll5HTZrY61j_vcUNbaTCSrK3kyF4UWpd05ORS6biSdwuiyTK6LwiEV3PjelycyQGFKRvjHdE1yWg1cPbG9pGy2784uLCwmDB0DYmPz_pActwywtQ4cGtiuB9WE2xREQOdPZraciHsLSrFHx8lKdMdlyi5HB0o68cWFly1OnUMZT-sbwKTj95STyTZvoO7mrw6QWAy6MednKG5VNsgvKQh3VSUY5MVfi0oSU-GpSlWJP-X43t88XSm5hvXK7vBft3y3klrv1wrJWeh-W2ANfwhPOKV3gR3KbNhBXnbbBYAd__t63J_pcm_zijg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛
ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30144" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30143">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=ZQTL3waiAjbQPBHEpny7I7bG1muE4YyHkEaHFcfrCArBmW_WkJ-wg3334F34su016YUejiBGFlwEZ7Vis3rLaZ7MWetzjEKnjRq__S3Vbe-cnZqfqgsh-3ggGWAXohyG3hZqPDTCe3hwlW8bpPKOw1M72_V45wLJyyREsF1L9sYgsC3j2nxdJfTJe04hMgy6NQkm2fL84HAzIH12mIMU5Z-1TVaJdS0wZVR2Q9Gc-wweENXE_UNGIURCxeRru9U3s9qo9injWM8dDV-MHSSmyTqD54t-n-Irzqc52Lzzqn84bouprRAqEXCo2K_bb3P2ic29-ETpO_mRoRoSh42uTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=ZQTL3waiAjbQPBHEpny7I7bG1muE4YyHkEaHFcfrCArBmW_WkJ-wg3334F34su016YUejiBGFlwEZ7Vis3rLaZ7MWetzjEKnjRq__S3Vbe-cnZqfqgsh-3ggGWAXohyG3hZqPDTCe3hwlW8bpPKOw1M72_V45wLJyyREsF1L9sYgsC3j2nxdJfTJe04hMgy6NQkm2fL84HAzIH12mIMU5Z-1TVaJdS0wZVR2Q9Gc-wweENXE_UNGIURCxeRru9U3s9qo9injWM8dDV-MHSSmyTqD54t-n-Irzqc52Lzzqn84bouprRAqEXCo2K_bb3P2ic29-ETpO_mRoRoSh42uTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30143" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30142">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUfXWlQdrSQdQbiv-IVGvaCy3NoitSZ6xESHD-AEb848U1tMDyqH3H0A-9AP-FhOvtVyqLkTUG_XJ26c1u8ISIHHGYpgC-73hA0LQM17K-rSlO8peN1HxjS1mkodhrx1ue36wCO3Td6ie2hQpyieynx-HGbRb7tjrojwkBiQ7k_GEEjapDMltUebk20BUSWNMnFvyGJjA6q-m0IcUvAAW-CZLkz1msnI4q9FM-sY58jhfVFspVXuAfxxiCx0p2tIbvJ0dETRthe_bx_QZchgNgUMTT4w-kLlF-TNouqIXxwIecUrevwN4xMXuaaU3FG2e6xQU6iXqQD7HdnPZ6nmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30142" target="_blank">📅 19:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30141">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2JENmuvrvZcN7-umOlb19Swfl3Al491-ACdNAhjJH-HPIlAvHnUr2eFy3egBhKp0dA0ZPwgXZb6wY1ifpKMK_kEMYaAwOdvw8DDrvhhSbt9uTIciKJgAHqUz7rfOHGD05VHg_OookkK3uCDA07qK70vKA5ZaWzDfNoZfoeX7-sR-AlAG1bjvXjJCThZsSMtz9HlE0KXls-fR1GWjhYjKgtg4olr6hqUfstRvwWWe8JPCQsDlAns_pit3By8fYMP-q-gN8_j0POEMeAut4WmifUQPK3bbK0Bz8b-p-WjZo9So0oe8dvO955IlEg3IJTG5XRbqtF-BY5o6w4_m4482g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک ترکیب دوتیم رئال مادرید
🆚
اتلتیکو؛ ساعت 17:45 از پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30141" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30140">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exp3pjmCBHR_dfQcv43hWvRyb8Fku9-t8zRtp-wwEogshvdpWTKBGMbOgcpWmpiSOgQCJ6nwCrG1zpKnu2C18igtDovPN9IbqMiGv4-rjdqj3mdzlOIducwFGKNDt4ysoWUOh7be6_T5oEElKnVza7yM7E9zG-VbJG7s2xSlz_qmcvwCVkOw9cpqph5okv6xqbWeNAIXAv2xz1uCbSH2wC_vZQJIGYLTFeg5uLdPfXJB5bzs-Uvg3bu4XAbJO_ssdSYZSv2yQ5vezMdrtVZBwvp6w9wjRSmsyOFg0eV1_Si_MACDsELARXr1BF4mjXpGUc0otiiEXT6fHmatBgTHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30140" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30139">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=iFVTHo34rI6OTR2cTBnfHmRptsNY4s-ZrGYeIL9eMnOmkj1II0uYai2FOFrq_c7ttYxerLApD5-kobj_80R8L0TvlCR3ea-dcmQUBMG2d2HSOY9fcrtb80x3nK27m4LIj5ePWLpE61xp6cLn88fLnlpynnMTEzpLcHSA67ygGOCkMrdNx5WllT0lzTGUPyug0Vc2XoBHCmWZRMxhVGJ3PiztiH0EUHjTVFwLQQy1IPUWW0qyqS3v1_OPS7z1dOhJUCMlYdMssqThPjZ5WLUi1XXVmvfD1c8G_zdgUQVHhdSCSd1BIZG2vaxgZVE4ZhK-7wSTGxrgsIg9tHMYkGiKBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=iFVTHo34rI6OTR2cTBnfHmRptsNY4s-ZrGYeIL9eMnOmkj1II0uYai2FOFrq_c7ttYxerLApD5-kobj_80R8L0TvlCR3ea-dcmQUBMG2d2HSOY9fcrtb80x3nK27m4LIj5ePWLpE61xp6cLn88fLnlpynnMTEzpLcHSA67ygGOCkMrdNx5WllT0lzTGUPyug0Vc2XoBHCmWZRMxhVGJ3PiztiH0EUHjTVFwLQQy1IPUWW0qyqS3v1_OPS7z1dOhJUCMlYdMssqThPjZ5WLUi1XXVmvfD1c8G_zdgUQVHhdSCSd1BIZG2vaxgZVE4ZhK-7wSTGxrgsIg9tHMYkGiKBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطرات سمی امیرحسین قیاسی از مصاحبه با علیرضابیرانوند و جواد خیابانی؛ بدترین مصاحبه کل عمرم رو با علیرضا بیرانوند گلر تیم ملی داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30139" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30137">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPVItmhnuo01OIn44FKS6lRfPDAbunDWZSoVtBNUQ1uMrxiInriIjrliuj0zw-RnHpUp_P8i5Ywvt2VhYz5ULDjc-6ADSvCrLO3dEc-1eJEBaiVD7VHEyB1L2HVhxvPOgX5pJOSblDBllm0bhFNhxNHKqdAdTo7j0uauWztcfcP6NI9wN3IIHQQrPnUP_COatWGBd46Xe8IzARpmiczr6ORmX87vFoVoM2nDOBWfLL3PUl_IvyfrbS8ROd522NOtIMq3UfV6zILkYkzGTDjaaX1F-GxylxDybaSaKFzGcC3F1JcK1GhPaCpqkSMsn-mKeeYoz12HHe1IFjyo7qpl0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30137" target="_blank">📅 19:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30136">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMmqRxP0YP-tkITUwd5U2Z0_w6yjcBTZouhK0G1xRCvByyTkBsQh1jsAu0_DOFmEOEE-RpI9cNIByaufPzoUsE4yaczRj1U2UcbFCClVal4bRbupUfacfHSJgZZKwNvAEWdarBuihj78epRIm2swpOJ67goShQa71-sAaGRBnziG0LgYNWAlhsWDygv3y8rmaE5G6sHAfyB-EZe2lTilbHRV1UGbcluJKKEu9qQbN8mp0BadUG9o_xkTneDdtJgYqbeYL2J7tZbBM_t1EpzKNczkqP292FrOIYdisrVK5nB6ULE2lyI3xoa4gGterhJ_B9NPTNoE26Rti3y2ybtVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30136" target="_blank">📅 19:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30134">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=l7Gr0PK_KfD_Qz_-jBQ4ft_YZj07S1ZoYzk7ybGWWTk5lrNyRR3cg2xmWm3leYq5SqOpcYkh-pqtRHWWtv-tDK14vU8IkgpomUZZn8ibylAhBofRcuLBXBRhE_k_iZbLE_O6IvK_yeehE4O7HvThZO1OH8bfcGgmjdSae4zSxfY0V2AaKIp7v9lM4BaxcmlN33-N8CyKzYD44wW_bo50bs9m4J_yAWSBEjRoR4dEZYjdGaYFhMJL_mq40sHzfkekbqQENV2QakskS9oWNe8Tn43LZNL7WdbS32cIXaEJQ0Bd9yg-U5k7pKo5hpoR51jNmkO7V5BQH7IYWY_1KkvS7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=l7Gr0PK_KfD_Qz_-jBQ4ft_YZj07S1ZoYzk7ybGWWTk5lrNyRR3cg2xmWm3leYq5SqOpcYkh-pqtRHWWtv-tDK14vU8IkgpomUZZn8ibylAhBofRcuLBXBRhE_k_iZbLE_O6IvK_yeehE4O7HvThZO1OH8bfcGgmjdSae4zSxfY0V2AaKIp7v9lM4BaxcmlN33-N8CyKzYD44wW_bo50bs9m4J_yAWSBEjRoR4dEZYjdGaYFhMJL_mq40sHzfkekbqQENV2QakskS9oWNe8Tn43LZNL7WdbS32cIXaEJQ0Bd9yg-U5k7pKo5hpoR51jNmkO7V5BQH7IYWY_1KkvS7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌جزیره؛
پیروزی خفیف لک لک‌ ها در دیداری خارج از خانه و آتش بازی تماشایی سیتیزن ها در اتحاد با درخشش انزو فرناندز. گل‌های این دو مسابقه رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30134" target="_blank">📅 18:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30133">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hi1FEr9ZvXMoEqJdaVJXINwUcGXv7quMhPc2D99inPVNN1HqCX_MMJy6sMkBnxzwqXdQ4ELAkCg2w2L_1fjsRJw9olWd-uFYBzAbXyKiOb7f6X29-9RA9SE9Rag7j-PFPY30hP-MIwxUop8BeslrMX22T5hymfH_FrThGaOqA8th9GRO_o9fd4fzmt07VTWECOwsuwieMqaV5-Q0Zb4zhkYOPPhjbQbw2CmNzAtnEwCYCEo9uUJ6-05N0vj9gozb3jnkEBI_y1N3BmO1TW5AegDQ7JLuIi9uraOsqDEZp-U5JuLKYvIh8bZ3KfLQj1llFxyAjgodAGrfHMKiZZZkCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رفتاریکه‌مایکل‌اولیسه بااونیکی خبرنگاره داشت این بنده خدا هم ترسید اولیسه اومد تو میسکدزون ازش پرسید گفت اجازه میدی که بغلت کنم؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30133" target="_blank">📅 18:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30132">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfayVIgrENflsCvstQ_KH5Q1bV1cVHroUUNf3LP-kGLyGXUEzd9LQP6XP2ZjL1MyznPh3I4S19O5VhExpzCacpoWiZryobNYH75dmqT6y9GWAMosvdA3U_zAUf__Np76QKa9huys67r93jHC8UFp7rqZ8M8IXu7eR8MY1FCNoJeFgDMGlONLqW0tGS1y_9RWB0ZkQTDGsjJgxDlflurM2_rw1J_IYXsa0K1aDCjmHqfBqTivK62vQw778CbxRq623CSs_n6_Nt1T3GnJeqhiYwKuG9h94dP4Nw7iKplV66cviAzTXoMYR2P5PoqomNN4shBJdBsFu3oqj6RltczuAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پارتنر لامین‌یامال:همه‌شواهدنشان میدهد که یامال شایسته‌ترین‌بازیکن‌برای گرفتن توپ طلا 2026 هست. اگه عدالت برقرار باشد یامال برنده توپ طلا خواهد شد او اسپانیا رو قهرمان جام جهانی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30132" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=SDPS1W993SRaZhR-H0G3yD0EwjNsnJ_zJ67ccXcLD7QEIlKX8Dy0XGV3ipHW2Hz39sJ50QUDVv0CYr5EX0ycg0eoGG0LX7woSvTz2CEMqasaJrLNU8eSHtXgOqCmOtaD97OahwDdjqiSkpYfaPLpbpIRC5ebCeHrmxLq8BIMHPCx8284AgvL3_19DCrzz7Pe6p2s1A3iQr6LuYBW8fQ9TtExgn17ZtniZzUc2yH5xWmtvVPzDdJDxrZnMYrnwHfWB5v9Ar2FDWShDjyt2zXbI4m9BxVIuaZUtPkhls9hdenQ_AAJ_7qE8a2sEKoTTK8nj8C9_fS7_PoKdT_bG67i6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=SDPS1W993SRaZhR-H0G3yD0EwjNsnJ_zJ67ccXcLD7QEIlKX8Dy0XGV3ipHW2Hz39sJ50QUDVv0CYr5EX0ycg0eoGG0LX7woSvTz2CEMqasaJrLNU8eSHtXgOqCmOtaD97OahwDdjqiSkpYfaPLpbpIRC5ebCeHrmxLq8BIMHPCx8284AgvL3_19DCrzz7Pe6p2s1A3iQr6LuYBW8fQ9TtExgn17ZtniZzUc2yH5xWmtvVPzDdJDxrZnMYrnwHfWB5v9Ar2FDWShDjyt2zXbI4m9BxVIuaZUtPkhls9hdenQ_AAJ_7qE8a2sEKoTTK8nj8C9_fS7_PoKdT_bG67i6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ از مصاحبه‌ تاریخی‌وفوق‌العاده گزارش گر صداوسیما با یه‌کشاورز؛ خیلی خوبه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30130" target="_blank">📅 17:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30129">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=fRj6F9Zcb9zquN4LgLWwVaSOnXZFmPcjoyei327J84IbaDattxOhxYMaBIQ1S0yeTk4cjUKsOJzk8IoUjFckRhr_9lDFMXchvlWtog7EB9nOkn-tPGmPAdKSw3JPFf0cHLmBvbqRInfOgRKwfyYhFibtFc42LQh1tXS0RwxxhHEiTZC4TsJwEZyarauuSpuV72mP2oS4ZsnI5Hdo1GHsNlqvpzlWjbLbjyBpIiGP1k1LAJMm_D1EbOeqN2jV_dGUHDEe7wmpbUQLCuNKoi3ihATXJq0MxdBv69VdY5amLT0QerJRQPy7QM9o7IdNWnyBqWNfis76oCSBnTf9v2jQCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=fRj6F9Zcb9zquN4LgLWwVaSOnXZFmPcjoyei327J84IbaDattxOhxYMaBIQ1S0yeTk4cjUKsOJzk8IoUjFckRhr_9lDFMXchvlWtog7EB9nOkn-tPGmPAdKSw3JPFf0cHLmBvbqRInfOgRKwfyYhFibtFc42LQh1tXS0RwxxhHEiTZC4TsJwEZyarauuSpuV72mP2oS4ZsnI5Hdo1GHsNlqvpzlWjbLbjyBpIiGP1k1LAJMm_D1EbOeqN2jV_dGUHDEe7wmpbUQLCuNKoi3ihATXJq0MxdBv69VdY5amLT0QerJRQPy7QM9o7IdNWnyBqWNfis76oCSBnTf9v2jQCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه مهم مهدوی‌کیا اسطوره فوتبال ایران به والدین درباره زبان‌انگلیسی؛ حسرتی که مسیم دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30129" target="_blank">📅 16:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30127">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vPq78ZGsuKKl6vad31DA_08bjAyiuZSIAca57EAv6g-cCq8WUo5G42VOp37qTNkmaLHNI0iB8nfgMZOksx6dhsAjcLyFeJT-yvezLe2QtNyZGks305I-DV6xJtk5u684NCY5luT3yD1jRByUCrKVI3FU7yTvQyCH88tpNXEDJVvgK5UNJLWBdyktEzOvq8V819BY5dOrc1oVyDVpPTHdfUEAmzFaUlNf5avCDiY3EemBFo__oDU_JsHOIHqzyd-GuoEAc3pVx80NR03bAaDm_dxqJmHJE4-HXkPO2O8iLu8nA34wqOlQPn9HBWnXOz96SZvbSG1w2edsQQoogTt_mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CIQuqWNrAX-pj794LntkwAK7g7CtyGxggkmba9bqaUIairMKK_FlcdLMzlVJhZK4i011FyrQtt19d8NaqQ_ju5zHnr5Goom9mc324QrsH9n4rODH6DyN2i4cLuHeSibHnjJRv6VhrpympjAo_3h-nIcxFZkUn90LBl8tI3NwXqFu-Eqxa255qU56J6HdO4FFQnxRjnhVWXUu6noSsqc7iR0AYTfnIytRLBnPCw1fqz4HJWgK50UpBiJQFat2PVt5WGOrpearhHQywfEBv4b-okJAal0WvYKxxtz0jqb6E20bihH9sOL0d_zy6GTbmSY6tUrlhxWF9zV5tmFzy7w_RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30127" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30126">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdSYk7Ia-eZTAfcz37cgkmH7QeE3I9kiBUpvOLI8GbJF4CoFNhW-28aqgFeiv_P3DyxLaDbgp9cifYMmX8AfhynUnsgw7E5O3H5MdPIDDMcWOEDGuI3WtcuR7R8UTx77lhkS64vQJ2iVI2proreSa6eXjU3hOyuxLwZx_4wS0SJcKoFnnslNJs3vuUC5BU8QYY_icQdG7MPIswviHGZEgn2t_V3uy9wsfcSjcNwdebGfBOB3rp6hd9BCNaJwvkN4Ugxrl6h51iafrkoe21RStSa8Bb6Cf2z2Y-PidzBUxVBTgSijoxKuryom5BR0d5DJFjLAcLlfr-DmyZh9-hI4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30126" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30125">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZ-HK4QhXaT5ZXCedonUm2FRzrnFurzCaU719TFltPkQNoPZ-Bd7iNiA6Os2v_YT74pHdLRfoGwqcpczxyZmDwYISVDsd-epfOlgai19L_KiIroim9EC-dABuTd0S-qNPSiVlt6uHp-bvWQuDTkKfQ6SqMqaF8vIZ1Rgk9qkBkI38Fr23OL-Kun7plbkCzhZ0W9Bmipyu7004iMMS0Gju36cpgrddM6Lhu2Le1vgXDHHpO3e7lKCNFG08vOL95Lu2Kd9aYCGj6_lv9ZvJeIs07Pdv7KlX35ooeOZvTvbcx5LJRW06A52dTeo98bnp5dyVwX4o3Yvcf1N_iWVxAVLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛
کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30125" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30124">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0-t6JLtt37tPkyZxuOWdYkCrsBs-4pOnJXg9wGXo851UvfFEm4LU1loS3QavHFWBo4hCfkU7F45_uNBxQLbSMX5Cj7MpQ2yP7kamcohDzG315eSl_shjRomFVv0N_oexQ4D39yc8ybH-RpUiddrpE2nYdNr0_wFNJnu_ClDpPRDg9fvXoyLwBOvI7SfEOM4sY99x9vIb2RAFDZOoFOQtYgJooMVo6sZnQRXj4ZCYiD_9j1vuohWRL_u5RamU5JakHmfbY93vm8rBmKxylLsjaWB9wl1ZaP-ph6fD-5WdtC-8h7HVyw2kHVRf87CitiCec0cSyIuLYlU696FI8ecwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30124" target="_blank">📅 15:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30123">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSJ7gx9iZZWVfEvzolkjEahuqmyIVu-H62NnswysA5KA8T9qRmZByVb6asj_ln_ydex0dXdohiZ-R062GRrpO5aHhqDRAefpH4FvJBecyYpXqOtCeUZFdDqg-ESux992vl0q_EFZ8c0xYcPk3xG2ABKXhH0rirjwTFGSfMrEPP_Tz1X2FSAAaVNh4opMYUZIaYjnDPiSHmeH9fjEcwCpW3uFK2gsE1DDBR76LRtTZcFm0TsTxe8zt56MJB0FWZvuOnC1gTDx84WZ5tqM2hF8zoPHRCOBmdJ88TMIC8h3dE9qx2CusHU2TrtV4oqD7eVDZeRmehA2DxZTdj07kJQF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مقایسه عملکرد رابرت لواندوفسکی و هری کین در 150 مسابقه اول با پیراهن باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30123" target="_blank">📅 14:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30122">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09969a195.mp4?token=qRSiMgePD1ImCoJPsj2yW9ITtP8LGX21p8xFqXR-2kY_cO1CafVYldvz-YVz0bu9pI6vqZq1-VPoSy40zwLQPgWQJKpgfL6DBIIz3rylREYpxSgguQ-8MOmEiCryYsgl3c-GccBlxo55EYpUVRJQQ7yr2PF658pF9lyEBdJt4UrS9Uh7Ce8jvAKyfr04TtNRkRYB512SME9ABtoXN3WrYrXHW_08bTmfAeexalFIPHFcyGPqypatn-XZ0xaLPOm9pG9gzYparAbj01_owk1rKZAcbqI858ggIBkITDejkkqYe5OeMX_wjukXa8yqlppdkv28Svzam4OgVuyaFGg-5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09969a195.mp4?token=qRSiMgePD1ImCoJPsj2yW9ITtP8LGX21p8xFqXR-2kY_cO1CafVYldvz-YVz0bu9pI6vqZq1-VPoSy40zwLQPgWQJKpgfL6DBIIz3rylREYpxSgguQ-8MOmEiCryYsgl3c-GccBlxo55EYpUVRJQQ7yr2PF658pF9lyEBdJt4UrS9Uh7Ce8jvAKyfr04TtNRkRYB512SME9ABtoXN3WrYrXHW_08bTmfAeexalFIPHFcyGPqypatn-XZ0xaLPOm9pG9gzYparAbj01_owk1rKZAcbqI858ggIBkITDejkkqYe5OeMX_wjukXa8yqlppdkv28Svzam4OgVuyaFGg-5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ و شنیدنی این نابغه هفت ساله اهل شهر تبریز: در آینده میخوام پروفسور بشوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30122" target="_blank">📅 14:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30121">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnujSkZVOzPi-pJo98nOKS4amJKlDZ5YklgR8-MUUyXMSnRVgFcodCI9qvVqGL-i9uFD9IzpoCw21db0yC-G5bwEQiLZAL_SR5W1CtdzNjr4IfGdMOOG-dBiR7Z23MC2Yk-P1_IOUsI8VKzP0h6oOg-qJlsp52p_kCLTS37vFdn4FMzTd99tNdU8zpg82oM-deY13wk1jb9CTKJwe5ah4mM9twgezClBGNobT7X7_oh5CUR7ItxzffdTt8UbQl_LWgQOOPd3FIriwMJcjscJ7fBDQdT8VMVu9U4guzJ7FbHA2kIet1p-oEOaywM_PtoYHAACCQAGp6FmxI30qqEnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق اخبار پرشیانا؛ به احتمال زیاد سعید دقیقی سرمربی‌جدید نساجی میشه‌. فرهاد مجیدی که مجوز فعالیتش درلیگ صادرشده دیشب ضمن تشکر از مالک نساجی به آفر این باشگاه پاسخ منفی داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30121" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30120">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLOcf2twdWKyKAdcVvUvkLHlN-Wwrj67Leh0rC9bTj9FZH3S-2OmVL6G98KbpEsYSpcH7DScrLRtAk1Aaiow43Ov_QGlENaoV5b3JZCauULCzRs5FB7-YWkESqtabPRF05P0J2P6mm3OQX6EyTxDMugcZwdJ-xuRazXNCsQrUGsBPJIXESGg1N_hR2h8GdKdLrktB6jL_DvBy_1aPpq0SLeFVXypu1G2Oxvm8X5Zm6McP2wc_s04FdRVpkoxW8OGsKQG2209Al2BgzN1AS1gXgxPhHLpY_E-FqiW2cnKBAEytRSeBpYerWDaU7ThrClmX2ukQQtAoy5HTEzosSS7pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها:
رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس رو گذاشته بود. تعداد فالور های اون فن پیجش هم خیلی زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30120" target="_blank">📅 13:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30119">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=jD0Chm4QAM_ERpzU_Gb1abIobfKmDAbmnpYBUVicJhSN5zu72cAtKNCTBGwa4EXMXUOa9tiJfmHBEQ6h4d2LSiJ3FAgd4uTjxLzcVYlIyJQaw6nJsUL99AYI8Mp4NBd_7CTHzQnwhKtWjHe74sD2u4WpFQnDcbG5sOPhKMlaAIsVPhrGqPRMAXCo7t26ki_r3FdY2yBq3JvBj05YMV1e9oD1MQu8dDoZ79raB3gvdvxgeB9x7-HKF2NEwLCAfHENytZXf5oA8gIzatYyE0QSNui8YT5pcVgbHa_EahAbA7hDeEs_q40RjKbuW7VkWnNtzTzHbp3VWDJYBMaiXca2KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=jD0Chm4QAM_ERpzU_Gb1abIobfKmDAbmnpYBUVicJhSN5zu72cAtKNCTBGwa4EXMXUOa9tiJfmHBEQ6h4d2LSiJ3FAgd4uTjxLzcVYlIyJQaw6nJsUL99AYI8Mp4NBd_7CTHzQnwhKtWjHe74sD2u4WpFQnDcbG5sOPhKMlaAIsVPhrGqPRMAXCo7t26ki_r3FdY2yBq3JvBj05YMV1e9oD1MQu8dDoZ79raB3gvdvxgeB9x7-HKF2NEwLCAfHENytZXf5oA8gIzatYyE0QSNui8YT5pcVgbHa_EahAbA7hDeEs_q40RjKbuW7VkWnNtzTzHbp3VWDJYBMaiXca2KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#تقویم
؛ 20 سال‌پیش درچنین روزی؛
ژابی آلونسو ستاره اسپانیایی لیورپول این سوپر گل فوق العاده تماشایی رو درلیگ‌برتر انگلیس به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30119" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30118">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXEjQ6O5TYEi3_Ix_DVC2YjJvp0o2fi-AA69TFS4rrYyN087nqm6jd-fPCO0p-wK90V-LGCdNCxwgm9chDlFBX-TmMYuDfdoN-fwhCmcRjix_x4prETfmrgvzf3sBbyuZ-OjlD3oi_6j72dbNzIcnRx6FFyVJV6fTwwnIdl09544auAtfNKAQ63CllNFPocK3r0suNSC_LyYsONAyvNPj5Fejltw3y0jUUeq_8KXxQgPqUeK1yQN0qiTZwXWU69QBL5tXIiwZuriYKQu30_j3A-JzHSReI3Hedr8srM1O7hw9rcScvi6uZj_IVm13VlRUdpLTMZF3HG3nu9sn8fKcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30118" target="_blank">📅 13:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30117">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGANOeHe4PSsfda56JDZL86awaYqMLWC1TfQKVBhSHgJOly0jgoEW483S4gjxrUbJJpyNZvknNBU0kDE58VrNtgPLWImHSYIj8TuSdwb5wEc4uU93yYB3-FRmFg2M69yn9Ei2Id_zxaEsJdLnm71DlBkPdyreiUsm8uCQCJ4v3Lq0Zom8dCFbZ3sUBLrK85AeVLbizA-ttSP8dA0Lr8pICwnBN1SnaPOR4-75InzVeNnJJImmXsDOOsWkuXqlfJ4qPmCHxBVBa2hTB_XV2M22Wvjif5urclsZ2MggqCS-Z-wJ6pgum3cOerWfsKTp34qc_iSgWz-c5vRSGWfYFsunw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم رئال مادرید و اتلتیکو در تمام رقابت‌ها به مناسبت بازی حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30117" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujm2AyrLO1hurvxBurhwakYMOIYVLTwC4VVsu-dBJMJYus2O-tPw9QAaWWhngMUc4DxTIZQi0AXzsW-e5wVpP_4WtgvZIq3XXYxkwYwImnBLh5Ip1ww3CdgT_4QoA8ReJCAlhanQBkxDUbmB6usVs7C_roqJDPmYsZSyghbKorlmEPvKB12JCT3WjA97-15jqFtSXb-X9nTa3p7YhKzGLkkRd_FVaPalFgzY1lkLqLOR9d4Y_HEiYmb8QQLg98EHGAhNeoHuD4hAbk_kBRMvURNvSeqL56BF1MpbQgdCx9VZqHlgRuVBa2NZtPy3j3b1N3P2KpBZ2eJw_a76FnljvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عباس کهریزی وینگر20ساله آلومینیوم یکی دیگر از ستاره‌های‌جوان لیگ برتره که مدیربرنامه هاش درتلاش که در نیم فصل او رو به یکی از دو تیم استقلال یا پرسپولیس ببره. شانس سرخ‌ها برای‌جذب این‌ستاره 20 ساله کرمانشاهی در حال حاضر بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30116" target="_blank">📅 12:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_M54AXSGWUWOKuDSDqwOqZ_OM6B-qGFYRa_wRNlWhIXG_xMX07Exj3EnTE3jxCYeIKDx6rCz7IyzZmqq-fDeOTrwfJ0kgCE6HxV3AzI-lSLadzq7U5Z81wOGU5JlpgZUHrDynCSCm7zEVh8hLKxRQJJywBW8cov3qwDvbYBlhjr6Ip62R6wF7MBh5jprlrxSU4auw7tQQF_zBu9-4KW3UqDEDOyUkJROdwB_pCSdO5cLsZGehCtxRL2xUBBsi0ul1DH_Rx-JmbWKvrMPX-rnePJ7-pwAhwHeMRY8tSTgHuhfCMSJREsDF3h-EnJc3j3IjPpf7kiUXrSBBh6CqCrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇿
لیست‌تیم‌ملی‌ازبکستان برای بازی دوستانه با ایران بدون حضور ستارگان استقلال و پرسپولیس! این‌مسابقه‌دوستانه روز دوم مهر ماه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30115" target="_blank">📅 12:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30114">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30114" target="_blank">📅 12:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30113">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOvHuHEVZ9aDV2aMNjZ3sZhWk7SyME-VJza9QMSJT1YwxDpgKzzTusG9pVFU7vId2yWAYzKOXlSYrVkn1ixzd0BS_EurX-fNG2keKU3s_GsTy1Noofxx8FhgK5q6dCASYgg5h0B-5j7NVbI-WKVLQw3DSR7XkkBL6ecnyKzzD1IoQhQVtZY1-pW_tNs1VEsIlJAozMdKBa10Q8xPsMCrm2qcdPPxMrvh4wNFlsB4Do1ltuPY_lIWl8TkP1DRsxOZpPNyzSZoIApRI30HDRVxOchDVALC1qgZ6fwvn4cWG50eHibLO_wg70s7Pp7DP_S6PFkuS3MUASaNvgjqL-5NGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال اواسط هفته آینده بامدیریت‌تیم فجرسپاسی جلسه‌ای مهم برگزار خواهدکرد و با پرداخت 50 میلیارد تومان رضایت‌نامه یادگار رستمی وینگر 22 ساله این تیم رو خواهد گرفت و رستمی آذر به جمع آبی ها میپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30113" target="_blank">📅 11:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30112">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0_iat5x-V0-ZsmNnW3ap-icfhW-e-X_TDSbYIG7IID7Kf1K-6vRHNCZw8Dfmyuwui9ZutllzWnA7z9B0cc3p3FI8ydrBdu8M6DlJnxN3bLv6FBDORkPK3iCSw0sjsrM3kauZBjwSbdjQ75PWmjzoi716kY4x6jls2z55blh47-OWuXaONY-w9583_98nRvgi6V-e4YcZJ9mZaD_S6175GQpVPXQZb1dw2aHFFtjbVXenbJqZFC0Y5UAFkMABztFkriFy1pbtv-FcMTl44Q-j0OZMgfiotZOgg2fKYSaGme8UN9olGF_sawyNGwMXQvB_-b0WHcaLUycCL6FnAS7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز تنها در یکقدمی رسیدن به رکورد رونالدینیو درجمع‌آبی‌اناری‌ها؛ از رونالدینیو تا رافینیا؛ ۲۰ سال بعد یک برزیلی دیگر در بارسلونا می‌درخشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30112" target="_blank">📅 11:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30111">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdMUWKe640eopUeG4NQ0pQmlp8rfzvJka_7drqjSoRZDsy8DFEAa5jgi96cZNZLciLsg_HcB0DsFBiNquQ4uTGVgtm067VA-fSwrvvwwVL5NRLC6Q4oZR_SXKUAqmc5QIIZmIuPW9dVzKy204jIqg7DbwNcsWdv89lr4D2R4AlI8QUO0P3U5V8vpK99EN03D6WcwYwSXi_VJ8c7N9Kw-i04ACl0sdMKQbt4iVZ6a8NTJSUMcK-O63zmpgu7acTc_VJ3kNmlahTGobHQRZvgqY46-E2Im2HaMyU3RzF3QfwdFGm7eW3yu6b91aOA8phPrxink6s259jclofC4Lh3ykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌آپدیت‌شده‌سرمربیان‌لیگ؛ مجتبی حسینی اولین سرمربی جداشده درفصل جدید لیگ؛ سرمربی بعدی نساجی‌به‌احتمال‌زیاد سعید دقیقی خواهد بود. فرهاد مجیدی آفر مالک نساجی رو رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30111" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30110">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJ0A_jR_iupIGFHmLoqvEii1ZerZvgUINPbBepPjMM897rm9isbZplW9bhYLNUb-JVax9y21X0nvak4NocagNneNV-SKEEynqUVOXQu8oG3ZwAeuxd4LFhyQWM75hUtF2CqMw_aFVLl7z0-zRIH8kykJbxbn_tYvozPPgq0fnpyeBfs0zl6qIcaEw9vHbC7oC0Dbu5RbKvOWwwmYhDynTB33-LoP0G3TMqV5zkRJxJtS4K2JigrFtLhTmmkhC6KQxi4snmy55JCrbpdFW5xXtKJNTMjSnkCdXR7SFqvH51tp-ignr1yO3_IcUDPSYF-tq0nMsRHeeaHvXj2ZdSIZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تیم منتخب هفته اول لیگ نخبگان آسیا در غیاب ایرانی‌ها با وجود درخشش ستاره‌های استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30110" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30109">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgZTPcOuXXOJslBim0xeLN1f73trLmdOmEDl0ukmOW9WJt8-vB_nnJEnsTjVUJbgXY2yEEpX6JmhMxE0Ijv611Ndb8OT4IwE2tk_7cloE4zObFYAAbx39dUvGhPZkq4klRfzcEhF1HwONZT3gGMnSnCTl77dtT5WRuNuZM1oYLIPxTjlOHyC17WqIkB-GK9bWNgDpR8tAeHtz-yo2n8sXg5E20I5fM2XXcehqYOKDSKXrxPBCjyX2HSd05yPkLefX9-XxcFBdOX57AjsdH6pDnTSaCsmx25i1YPT22T7pPiLcITQ3Y1yuo7JhAjUJwknXGkseDq1IwVZJAne36RUGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
⚽️
لیگ فرانسه
⏰
شروع بازی ساعت22:15
⚽️
مارسی
⚽️
🆚
🗼
پارسن ژرمن
⚽️
💯
اولین واریز، اولین برد بزرگ
شروعی هیجان‌انگیز با
🤩
🤩
🤩
🤩
هدیه خوش‌ آمدگویی ورزشی تا سقف 250 میلیون ریال
🖥
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با روش های ارزی و دلاری
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
با هر واریزی
🤩
🤩
🤩
هدیه ورزشی شرط‌بندی میکس دریافت کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/30109" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30108">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30108" target="_blank">📅 10:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30107">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjouKFbAz8fZdDx957NvAnZkNmkyHqIXWTdxX9TiSFTmn-IGK846Shvjmb3V3hBkx2IeNeJZZbg9mwj3O7LrS88yRXutHeuVPfMo_1rOeXx-DSlP19pr-hRJet3BZh_wkNn8aUayuSg_KxfJU4xrJKbed3hSzSWU_ZK0eX_BUaVpzwUq8DuEuqmoXZ1MY0_OazFNDVKjHpFD2C8WqBCcpsY2cUSnTHJ8D5W24_eqtJ1QaecD7LKnR3wYbAxn5X474jhytcQnGB_nI94_3_XoZoyTyvNP5ki2hGmgyLdc9y4Ej8frIZ_KFnrCs0GGgk3dUYUeI3K1T4UGp7Kjrp5DtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شرکت EA پیش‌بینی جدید خود را برای جام جهانی منتشر کرده و بر این باوره که اسپانیا جام را به خانه میبرد‌. این شرکتم تاکنون دقت 100% داشته‌. ببینیم کدومشون درست درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30107" target="_blank">📅 10:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30106">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDDHKfKRKpX_LDPHf_JSl472Ng46XYDGiQWINtf1VepPezJwdIUfTjQW0i-tnlc3b11xns15hXYrG8XRhtdzLShitzWkVO2BN9zR8kdzRZaoqyu1W9wXkH-OK3LDb6DW5jcLSfh5Tj4JYGXJ455cIPEQCXsOb1lJ-WCxuZAIjHfVwRP1mdrjsEtaki3MwsZf4fQ5ucMCxPgmI4IojtRAfytLnx-7zw_xlBw7a53xIejbX6Br6uy9BKckazFMQEK-YSqcJ4t27BeZj613MUC1O928a-mXmlMRt77z9TyXSgUUYnNBnp9iR4Gjf0gc7ZpFllgPEocv9VHbqNX3T3XEmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت فولبک‌راست‌بارساکه‌دیروز به لوانته گل زد شروعی خیره کننده در این فصل را ثبت کرده. هزینه صفر و خودکفایی از سوی لاماسیا عاملی‌ست که شرایط اقتصادی بارسا را در سه سال اخیر بهبود داده است.  قرارداد بازیکن تا ۲۰۲۸؛ دستمزد بازیکن، هفتگی ۶ هزار یورو؛…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30106" target="_blank">📅 10:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30105">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MktPPRgykmF1emJAdU9A8gEZPv-S2IC1lO1b0pevCxK3InV5HNc02rX_KQCA8Ssr4rPuE_fnLfJ60FK68wDDwPwUO9HIdCMUTIfho0c6TplkpMLiN6bzl3DKtQsnNEVkKiScatp51vRt035BhxsK1LVsKXYLRkC0bF3HRqr5fQ7By91hX4DVn6rhwWH1CVW_te6onE7fDSBZTbwSeLxprs1saCQzMvuyoMc6wV0juplNrtdx2vh9MQGQ_FRqp9IVvBeCheVQ3hNz-4TZ6G1dz3gOP-OoJTbS2giwShMkUmzifeOXLVqdDQlIA3iRkz9VJpEU9UbjrWfyOVNwuHGWuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد مهدی زارع مدافع میانی تیم پرسپولیس که‌هشت روزپیش پاش هشت بخیه خورد از اواخرهفته‌آینده به تمرینات سرخپوشان باز خواهد گشت و مشکلی برای همراهی تیم تارتار در بازی روز جمعه 17 مهر ماه با صنعت نفت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30105" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30104">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJyGGqil1Zw0Q8_03LwfvQuP30nDYr0zc1zs90lhFA2G4KWTfBarPDVzESds_2wJ7CXq5zTlZrhmRfRgpWc252GjYjN03IufGu7JGLTLyg455Top2gXSoPnPrgY6UUYDMzsdQWP78Snk2ynoEPRS1Kb04G0dVwGkhtB_aF4-0A9dTp_K_r5Pc72WQsytU6WXgVqguczhCDHUM0HCmAb4vowKwZEhCRz2EN2PDOyedmHIyK7xGbFaR9HcamUDOOCYfJ71wd1rBXp4fNDD-_vUN_L8Qdem6W2GO6eZHl-3GZoagPyAJSRPPRB1k11UibYPrd6YuCx7sHj92yamRtKiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30104" target="_blank">📅 01:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30102">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ep5gqEpQ2cWSlKIrDIr0-RWFuh_dIL8eyx3rqiwv3-o5NgHLF7tPEWW80czDZ8OS57nEdxRPVYIw1xUqPy65hud9vPpSIriaiJkm_rY9FuEaAeEYGFiHVH1r9dZRSYrsIi8CGmCCi-Cp6I9VnL_Cu__wd0tVrMrUhYr9aJx2KqT5T6_F-CRWpKOlf4qBXg3rBezqDoLeEY-N62x0mUBxWBxPBV5t4Pyz2HBk64G2dcy00uRQn2qLYwS-pheyhhK8H6bFmz-bMwGKUcxq-8NLnCn3b180JWa8lGwnxK2L2LbrEmRpKzfBLydWIQCtAUnR95Rq_fB5wXvFc827UOMy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/30102" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30101">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtIPM2seAfUmN1ukYDRWhg1UTJFxtNEYU2n2DfMAI4Zg9KlO6RY5IIhE16SZumOieEN-hDyE6bZzs_WWSShBLlWW3IHKqkFWioJo7LZvb3H_YE-G6YMmRUUgmOcQMnXJiN3PF-IkiAn0lGnEhwa-CxGnNqvSqoJAQ_wjy68LIwEIi1s7UIU8VIPhnY_8qlth95SSFuxXS53tV7EaKW2VE9hqar8NM55InrIueKjwE7y-BIg8qGFZPERNMM-sIHRCiT2BWbd3FJN5RhDu0sf908OBIHGY70bkZcY5hg9N6n6K0e-BYdSZEwNbXc_w-aev_NmMle4-liacKskGHAlIbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد بارسایی‌ها با هتریک رافینیا تا تساوی در دوئل آماده‌ترین تیم‌های سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30101" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mu42R1RGixgvLDTEqTmZHE522QiCZOP_Sf6dEJwNRty47X5Q8On55bwynO4Jzm--SuAoSPE1zljeTYRQ7975srd2_RGa3FDCfJqel7AsikuIWM_ebLEm6ASq6BUSvdoTLES60Cr7OagkZDY84eEL_a8KfztSLiWMcR5zw59tKGrGx_7goBcJQbLxA8fzATuLJjjg5SMmxriMevIz7u3brzii6nCXpUz5nmZp3MzLAzg1FMCZXa9iFlq5SBepyX4NAlvHBN5INzeRdgkwAjX672Qf3EQ12t-B3zXyewrqaUoWRAOXDDIQGpPYY0rOU939nQ88h5NXGFSl8FQxR0DTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSrGyfl15mtx4WnLWRGYieu6hmtTnAZdNns4kCGP6HRtdY0ETFJqbRHXLurlxpmwPBL2o4mL3vIHeQIgG6uqRwC0uCdN3Bdr1E8BVdPhDVllSqVtvW1YK_NVtaf5bKxOiXqS3LLBepq_DOv7gDh5KtqyHs8q6bIDR748ZrmZO5OpFEo8BQPx7IAYccXBYJ1AiW9pfMy2y3pFJNpPo1ixYI3RVv8WLTVgEe7ITNE0KN-4NclqZaASm4csDAKuWUliGuvraEz-8Kv_khz1vXZabfOSqC96MtsieXhvs17Ar1fIDlFeifa0mdAzhNN1VMa5rrpBMQAhOlv1ySNHj-fZUw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30099" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQgOdubpEeCxPjTX0DCYpH1V46VpimgeUIOqCJnING7eZmIpk-86vy9ng4CT8S3W82bB0LyuBletD1NpZFqkNXtDo5NBEp_iEd0JEhGj5xMilnjoxKivKNaFNHRCTvDlIWf2jISQ9mY3YiV5Jz8B23o1Rnp-wyGXQsLrGwMxhEPEApXt7d5uHh8e6gROaCFeBLtOLbX7IyBB_pTclK4Ce9Mpi1ZT4BjT6IguG-fTsGaDo-iykk16tHGUGNfTJQdCjtYaGIsqDF1NEE9Kdv8XRKABB0No7S9PceLvQrSLRQH7ThVqEhcLU2f6utqJh0GhFZEuLaa6sBCRAqugbrBbSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30098" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30096">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9QvygrTt0LgdLeyaORBPcK6oM26gBUQmFUwbsJxByZJOjMGT2XTCROenksG1voTuOUf0I6nlVDCRXn7VEgLeN4_ie7wDNFy6v60i8XSY1xDV1qhqIBtJtA2w9YVdihAXxOdlBD-mdEcuNtx4XpTe6045zpIjo60DMta0WPIr2-mCrnt8HITC2sfU0HsFq0anrAL_CpmJriSSCFpGlEpPxjMaqIdY-zRaYsyLntdL0zjXx_LFmP3pV0qnKlUvy15h6HtQGyzhp1z2ZlUKJKKN4xeIatGmmdR47ACLKw0zxNWaoZGiixAIGR9KkjHAp9qe8wZwIVRnX7RjklCNN5M_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30096" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30095">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRYXpbSOomGACdKqbSSP_SHpeKg8PybgEiAGgmzeb-9x94iIelr4OVv3AAN9QF66MzSG9h9SQJwZzUEbYkyNRm-ivdxQEiH6RQqzvqRSmRv9536RIn5JeyykYXTqkJG2yDwqAKV1XECdSN9SH_FT-qZxWXmziduuyCD8VA1vw9GTcCbL9W2gZfQX7bkNInh_yM0jumLPsD35TKQtB7xeKp53VroeC2c-P11rABpt6759UzAOV6hnTr1gOFTIQ9jiKakyZ2Fwsvdv20BPpA5dbN_RD1dk_FPfW0RtZT4zYc9dgxZJJX6LEmUVkmsZVo1TPdit3mopDqzk73bnOuXCNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده خدایی تو سایت پلی مارکت ۶۴ هزار دلار بی زبون روی پیروزنشدن بارسلونا مقابل سویا شرط بسته. اگه‌این‌اتفاق بیوفته ۳۰۲ هزار دلار برنده میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30095" target="_blank">📅 00:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30093">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzVqm5sq3CEx6LNtXfl2BoY45HAhuEXEwkip1xSMVDpUI9sqKMcLYOXU0NOd6MVq6ma2FWanTf0m64ovu3kPj8UHxcpqDwVIfqlU625mbJI4n0GQRsA4SK8HhoKhIm_JHACLhnHj28Mk0t5cgk5UGNqRINfkAiYWfz17hciKfOtPg6vBycp_1m6Ub0xDEbgQlpUdVahoWs0J5TiA3RD2wo5KZy6fvdm89HWFVwsKFlu3JgRV7fRF7uBNPrQE9ahAn9NVu4anEN-ALPKBxYcbc6vUKIrtxYORmktne08o1p_YjQMXmgjophQ4dXeYu-VcJibtnImm3r3LGKnK5nu6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30093" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30092">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuNqq5f6oRoNk9FNhXjgr45RTUGeEpP0JoN8u_RCk7C5X-hKuLwB3udgq1bBnI1x9xPvTf5CchTC0SShwECVQiXHKhpsf7-pBqntuO6DqORHRdB7LbW71tevDp9rxHPl85s-K3QzU3SG5-_5qsvbbjDT8yFbD0WS9c48s0dcjuTlR7eKi-KTm8i_yxUkb_vP-hKqCDuxcIH8wRMeQvkr2HwJfAVEz2goVaDY7DaDQpwIIpltadz5Cz3XuSUh8BM0drrBHU12X0rWJw0v5fmgClwc1ddKoTUnLwWqKtqhfX5KA9DXOyId39S5ZQpgmatRs0Ko5djIPnLgiB-JRpdiig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یگانه اکبری و آیتک سلامت دو خرید جدید باشگاه استقلال برای تیم والیبال آبی‌ها هستند.  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30092" target="_blank">📅 23:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30091">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qS_Iwcdp3urWqEl9HK-uOkBc5yj9fpgko87f_VPS8ewGHIxxYcsMLBXUVvmMVdwtLKPyc9N_g0vYiSFeCqEbrqkaHNfldHGv-U_RzkQsZvDNWllPP-A2YR8hfEpsYAG5SUJbW4BkzLEtRD74X0tIpG9ekDe_-z1r1EQyJdWLpxbV8pEqagb2bgXVJzPi2yiw1Wy5uDJQYU3YJwK8hAMDx8xjHwRvJI9eNPGXZoiLqdn2f02J6m1ce_EtvHubHmLtmlkD7EtlSaArW_WhWhXStTCMYT7sGmlh7WdRyNfMyd4Z8XFBA8NZrmHfXV6QicjwZjZ_ujO6sCDmXLQm-sVgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه مسابقه فوق العاده حساس در انتظار فوتبال دوستان همراه بامراسم داغ و جذاب فرانس فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30091" target="_blank">📅 23:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30090">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇹🇷
🇪🇬
درشب پیروزی پر گل تیم تزابزون اسپور در سوپرلیگ‌ترکیه؛ محمد صلاح ستاره 34 ساله مصری این باشگاه باثبت یک‌گل و یک پاس گل و نمره فوق العاده 8.7 ازسایت فوتموب‌بهترین‌بازیکن‌زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30090" target="_blank">📅 23:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30089">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa_s-W-dGF_GOYa-CJg3XKLeq2tumvNDVhzb_27M6H0GUGiDS4Hop1Lt6WUlLjUUkWb4kUKm-_59Dn0J55X1pvfx811zroonxZCMD1AVJLeMp9srffxZB0IOZoj08hkrLHbYHMi4nsAAYqvNWButihmwDl0nd95cxzkY2SYWGYH_7RZcAtnYZ1cixff3BNTnFPlIlAoeXtoaf1z7ZT1Le2poZp6aschEVGWuJLhjpi_xBv84WaPPBqROAJm3HZwgevbh1_q_NSEVaOB8YnyfA2fBsWifgN6aO2yYbJ-nRnse1k4B_V1qE_vczEKLrt6X5Bqkz4pr2ZgKp5UEWiB93A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مجتبی حسینی باعملکرد دوبرد، دو مساوی و سه‌باخت‌از هدایت تیم نساجی استعفا داد و بین محمد ربیعی و سعید دقیقی یکی‌بعنوان سرمربی جدید این باشگاه قائمشهری انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30089" target="_blank">📅 23:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30088">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z50wIlCFTOKH7E3bs4rmY4XBf1t52ngL0S_qN56UCJKoaEwm3O5xFRfXMlB__u85EV5TRGtc2rPT--KyuXrFQ09nZkvc34T6MFR-BHRLu2PTSWSkCyCj3xN6VCYmFQxs-Rd3cBGDs_ovzmbpuAPO9m8MegnEBT4eYQWP5iThQfOauRAPVMrx2nLAYek95gjMAQZRenXajS4ltR9BBMe13Udl08JOMwlSXUDfkKe3WEzfj8a1hKUqW4FjlYt76GNNAhRycTR0r8-UH3KlzxXJyRni-hRQ5KxqYi2uyno8YyYA6QRT0lzZY7B6hsiFz7Z7pRzdRYd5Ntpf7nm6Or-XIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم‌بوندسلیگا؛بایرن‌مونیخ‌با درخشش اولیسه آتش‌بازی به راه‌انداخت و با هفت گل یونیون برلین درهم‌کوبید. هری‌کین‌به رکوردتاریخی 100 گل زده تنها در 98 مسابقه با پیراهن این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30088" target="_blank">📅 22:49 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
