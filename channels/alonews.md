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
<img src="https://cdn4.telesco.pe/file/t_lD_O9vtDOjG8xFisZ-Zi4gbfTCblaJ6Fi9AnO-jDVbp41P-ahX7ZFCsWHxa6SPcq5eFQ0FIuoMfQ_9okzyTw0KdM6NLJvLNExhWVmVR-wFeEg1bqiQoy8FlkQTFFnvDTJZs5tcJeGY8VRQ3w2g06yJ0N52qeukL4eUXIZhTD6XoawNCGJKfxPPt6cY3ipeGSn_2QOCVeXUbTSWWVv9TmfD7l5MueIsGGt2AFoGHN0M_c2Pf4s8kBVU9aXRGVqBMlEp0u7jrycyDhrkDP74WtsSSbZAD3Y2_PFnub2SneWrvF3Eu1XgURznkpVByGaP8RCnF6D6tgDVW_AivWz5QA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 976K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-18 23:33:16</div>
<hr>

<div class="tg-post" id="msg-126396">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoTMg4BoX2bNb4r-X97hEKaKvF2uG6nBhcG3YGWzFteoOQsPNi9_dD7apgdE8Ii26FFDSauwhoBYhEF-54axgEG_MWaPE_VJPclobBiKN04yVuJqYms9jvBbcccXf_11dIBp40pzyO_Uoz25X3SbiSaQZZkP5IY73v5RnA2XgLnYcCMlofs-fIs0xvAP94AaebAs-OQu1nFJAYyfM4q9Zx4UJNNBOj6WCdLYiKu2Ij94h05o4msrXE0huGuvJP3ppPdLHK1GgM-0BZI4eMFFoIjg8GzFpCAU9hcLvuUEirzbRZWwl6efBVYwtLqAU_q0Ywza_HmQYHGxwRQIstxPDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک مقام آمریکایی به Axios گفت:
بیبی برای زنده ماندن سیاسی در اسرائیل نیاز دارد که جنگ ادامه یابد، و ترامپ برای زنده ماندن سیاسی در آمریکا نیاز دارد که جنگ پایان یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/alonews/126396" target="_blank">📅 23:32 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126395">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWzbGLF26hctoR4u-CF5un3Fr-3EcfeXcn9ZQy2D7aIMqurwtncKje_jZnVkj4HvYvpgaYK7U8P-AtNrSG0qveD26K_0bgmZGI2XMA3W_cMO1BB7BnaXXLItJGFepLMxu0K9wwnua2XuKJW0q8_omwyST0tmwz7t2sHVEusV3Hvm7iwe8BmHvu8ZczwF4uwVJI4iVSM8NOz0ggqcamOzSCcJ8l0yn8bHWZ-8ZQFHyP0znRoWmvNUwCQ5ltmNSDrkUtS1HV7fCWE2e_-pDhEj4LPEAwb7OmFiTWahnJD4KcoAdSqyTdnKghWmHltb3nwfOpIZ_oVi_MLDGbyn20chgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/alonews/126395" target="_blank">📅 23:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126394">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f522c1055.mp4?token=UZkqMdBm9RVRJPyY0ldrt76ftCOoBRNKeYtf3S7wULzdC64UBjw_Z9_MxsnrgxL8-Kb7_qTHfZd8Mk0_pxWPEXWny0Wpyy9CXbqIosXsKCrfbrEcLWTKTaKHaMHUb3GEyNJOeBf5_z5EQfVccuOyX_D3OdddiD5xy2-Rf6yRgvo20SdBUN2fBxFQRtYxyCnw-P9SKkngopseyP0ZX--s6pykxN1G5sjZRsSL_hTaXPAGvltX62l9O6iPPzavx-5yEajvBBjS0q34sHtH0IxIcXSjGRThZLMLVr-LHaoadogNhewXFNgxn3uS6VFcFt9idjxU5p6cA8bxWp-cB4_fLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f522c1055.mp4?token=UZkqMdBm9RVRJPyY0ldrt76ftCOoBRNKeYtf3S7wULzdC64UBjw_Z9_MxsnrgxL8-Kb7_qTHfZd8Mk0_pxWPEXWny0Wpyy9CXbqIosXsKCrfbrEcLWTKTaKHaMHUb3GEyNJOeBf5_z5EQfVccuOyX_D3OdddiD5xy2-Rf6yRgvo20SdBUN2fBxFQRtYxyCnw-P9SKkngopseyP0ZX--s6pykxN1G5sjZRsSL_hTaXPAGvltX62l9O6iPPzavx-5yEajvBBjS0q34sHtH0IxIcXSjGRThZLMLVr-LHaoadogNhewXFNgxn3uS6VFcFt9idjxU5p6cA8bxWp-cB4_fLDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پدافند هوایی آمریکا یه موشک بالستیک از ایران به سمت پایگاه آمریکایی تو شمال عراق رو رهگیری کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/alonews/126394" target="_blank">📅 23:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126392">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amURavho6UAIQfoT2QqcJKUzXnfTQ8vbUmk6DdXg13kCwpWSkA8CwlvDBHlbLv2eUUOuiHDX8_ycOUD_P34IHFUYZeG4LmK1QVQYmWYVQNteAPshKdzFTK9VzVWZbP2hCKRaHNIkxwHMTqSzgRnrvqZ3i-EtHwul8yoPzVZA-96JYZ4AHOru-Ft9Hv4oxDzBACSxSQe2HFjQECpvTPBRleSXmED1uGMegCK-u1qH0lj7UGzbnchI8ZpTdQwQPFzVJBGQ23WRbMxFr2Re-cm5GKbM9RnSG5YhXvYICwjOrltFgmXqpYFG0IzqKQBXYz-NA569-7QK1H9Yd3XfdyUzfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/934b102cbf.mp4?token=Oig95vlZGjHmddA-mphlymE5i-F2n-wGj7-JKoY6gnMaIuqc83q-DJ5c4LSQ4qVNcD4vgXmpuHAE_U6gcxNAXGJgnYKca6HAxFX0GIg3kGFNk8UA-yLW7qgmbxPuN8OqIkaS2F4fm8GvXMgA-MED0ImHTTE6MoQ-GisFuDgoOhNDCPynPYAZjkY34KPt7q05S0px2tiUfkmhBIvVI2lvDx50kCtx-Ggcs2UMU-cWVmMECv-n9cbbxUEi_HEQo7xqpVFGt7SF3mCjdoVBey3yam9ojp2T2l_47nKgvwRno7sWHJu_kGyy1Kh2xLyHVHwgFegy9rjOxxyT4fG5iEYY1osDq6an4dsOEz0XTIhjsPzJWFkeT4ZWydtHJPSxNyUbz0-BMAV56Qcr3FcXEu_LRy6naO-JP_wxxWmG40P-etyBpbFob5474LuOk1SftOLbj5sHzBle6OB5mfB5QqcjztwZm05QEg5RCEipjzhBOakXEkIwPWm5HV1uaHsiAJldrf6W8hN4xyM3X6Th5yaWnKbDOp6stVmrdOL0-oVUjrtFcdPhjIeIQiFquRqAuETqsZjQb-3fTfSFsP9-Oph2CYts3i0a2tsKEjygVDNIQ1ZAK9GqdDsZJS2bFd42HKlLIUzZhlwYhSQSXZe4bNzm4LwRh-JFWsMj01CDuadkCWY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/934b102cbf.mp4?token=Oig95vlZGjHmddA-mphlymE5i-F2n-wGj7-JKoY6gnMaIuqc83q-DJ5c4LSQ4qVNcD4vgXmpuHAE_U6gcxNAXGJgnYKca6HAxFX0GIg3kGFNk8UA-yLW7qgmbxPuN8OqIkaS2F4fm8GvXMgA-MED0ImHTTE6MoQ-GisFuDgoOhNDCPynPYAZjkY34KPt7q05S0px2tiUfkmhBIvVI2lvDx50kCtx-Ggcs2UMU-cWVmMECv-n9cbbxUEi_HEQo7xqpVFGt7SF3mCjdoVBey3yam9ojp2T2l_47nKgvwRno7sWHJu_kGyy1Kh2xLyHVHwgFegy9rjOxxyT4fG5iEYY1osDq6an4dsOEz0XTIhjsPzJWFkeT4ZWydtHJPSxNyUbz0-BMAV56Qcr3FcXEu_LRy6naO-JP_wxxWmG40P-etyBpbFob5474LuOk1SftOLbj5sHzBle6OB5mfB5QqcjztwZm05QEg5RCEipjzhBOakXEkIwPWm5HV1uaHsiAJldrf6W8hN4xyM3X6Th5yaWnKbDOp6stVmrdOL0-oVUjrtFcdPhjIeIQiFquRqAuETqsZjQb-3fTfSFsP9-Oph2CYts3i0a2tsKEjygVDNIQ1ZAK9GqdDsZJS2bFd42HKlLIUzZhlwYhSQSXZe4bNzm4LwRh-JFWsMj01CDuadkCWY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انبار مهمات عظیم امروز صبح نزدیک بلوفسکویه در منطقه بلگورود روسیه منفجر شد.
🔴
گزارش شده که این انفجار ناشی از هیچ حمله‌ای نبوده است، اگرچه هنوز مشخص نیست چرا این اتفاق افتاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/alonews/126392" target="_blank">📅 23:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126391">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
آکسیوس: ترامپ صراحتاً به نتانیاهو گفته که از پاسخ به ایران حمایت نمی‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/alonews/126391" target="_blank">📅 23:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126390">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
آکسیوس به نقل از منبع اسرائیلی: ارتش اسرائیل پیش از حمله به بیروت، سنتکام را مطلع کرده بود، اما کاخ سفید را در جریان نگذاشته بودند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/126390" target="_blank">📅 23:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126389">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
کارشناس صداوسیما: مردم ایران الان یکصدا میگن جان ما و لبنانی‌ها یکیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/126389" target="_blank">📅 23:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126388">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی:
آتش بس باید در سراسر لبنان اعمال شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/126388" target="_blank">📅 23:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126387">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HViu4Jk1GEk-k_m0mDM-K5yckmPZEmKs4ABA1KHQyKlMgDY7EtKom15H4mxwkr-DJ5gGDf2jPImPghOWfb-u-yXkKpzgwAxwtlNHQTempgO3mzrQhDFi0y0JlQbhjMnkvTD2OkNPQjL5mBjYoHadyu7q1u6_1TWcCUwc1JSm4aguHvnb3Z6pqZB-C7L4jI0Vg3H1DQc6nxG_t9OPrjH5WbOezACKsSlllPoN2Mfg25QcjlxTsZwV-3wb37SgAURYJv4S3maWpNyUg27KXa82Ye01YFHNStiM-egsiGhHiTkV_Va0r0gdHWiklYaTVUhNIMxAuW0ocLtvobd13gKntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روبیکا به کانال خاله دنیا جهانبخت تیک آبی داد و رسما تاییدش کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/126387" target="_blank">📅 23:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126386">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🤩
⚽️
کامنت شاهزاده زیر پست فیفا :  آخرین رقص
🔥
😉
The Last dance
🇧🇷
@AloSport</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/126386" target="_blank">📅 23:06 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126385">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
رسایی: این عنو(اینترنت) قطع کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/126385" target="_blank">📅 23:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126383">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/128f9bb157.mp4?token=XPVVW9WPx-MsBeXDrremhEeQSO18wbCFF60-P1WrVnHiwWJz9X-I_giLI3XdxfCudlrTrPvK5tsFWhxQJ0fz4Atf3aOkO0hHGr7SzznH9hiWF6KJfxng4jWm0R9czQ3DXZMfM9W1nnuzAnZYeApvzyd-ZGRlsDMLpIMJezp40dRbuU9DzSuwMMnvVyULkRslmZ2KQUz_oVlqRVUQkYSFPklqbFBQsDuOchqtSX6UFbi-ewg6tbEQBrYez-cI_RUZHWT1ovhkXwWNyTaDCy5PXBn8oQOnKrGftLTK-ZsQjkIplbGx3XNi5qBvoKMQ0Gj8tENtf79c3I0SehDr8Af6EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/128f9bb157.mp4?token=XPVVW9WPx-MsBeXDrremhEeQSO18wbCFF60-P1WrVnHiwWJz9X-I_giLI3XdxfCudlrTrPvK5tsFWhxQJ0fz4Atf3aOkO0hHGr7SzznH9hiWF6KJfxng4jWm0R9czQ3DXZMfM9W1nnuzAnZYeApvzyd-ZGRlsDMLpIMJezp40dRbuU9DzSuwMMnvVyULkRslmZ2KQUz_oVlqRVUQkYSFPklqbFBQsDuOchqtSX6UFbi-ewg6tbEQBrYez-cI_RUZHWT1ovhkXwWNyTaDCy5PXBn8oQOnKrGftLTK-ZsQjkIplbGx3XNi5qBvoKMQ0Gj8tENtf79c3I0SehDr8Af6EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محیا دهقانی، بازیگری که برا نقش رل میزنه: نصف جوونای ایرانی بیکارن ولی دائم در حال خوش گذرونین و خوب زندگی میکنن. خارج کجا اینطوریه؟ اگه برین اونجا باید صبح تا شب کار کنین فقط
.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/126383" target="_blank">📅 22:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126382">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
اتحادیه اروپا روز دوشنبه تحریم‌هایی را علیه دو شهروند ایرانی و یک واحد از سپاه  اعمال کرد.
🔴
این تحریم‌ها فرماندهی استانی نیروی دریایی سپاه در هرمزگان، همچنین محمد اکبرزاده، معاون سیاسی نیروی دریایی سپاه، و حمید حسینی، نماینده اتحادیه صادرکنندگان نفت، گاز و محصولات پتروشیمی ایران را هدف قرار داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/126382" target="_blank">📅 22:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126381">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: آزادی اموال بلوکه شده، مادامی که ایران به تعهدات خود پایبند نشود، رخ نخواهد داد
🔴
محاصره دریایی اعمال شده علیه ایران تا دست‌یابی به توافق پابرجا خواهد ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/126381" target="_blank">📅 22:51 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126380">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f477f009.mp4?token=v6QjdrLjrqGLWy6xXFYY-h9_weeHeyiorIfIpcQrtGCIpxKfQgLrYVFeF6kxqgvz8WZeu1iit-QW4KD576CX0lS8eirPaJgebr5txGmizYLqOZFfWCWfS_BlShr4NdVEBcf9VFhUWDdXb9whIlPFxv_4vJWzzuNIiqXXOKZO2X5smGzb3Gg_4Dx8SLp6eTrILOZt8kdAn9vfsvPd9Eb6zLKUq-DrDPtU4kJTMjHy2bjuqiVWUNAoK1gEMvwxLQSPaphZXPz5e8urOjRgxAuPw3eoA-lDnRUsG4drChaLKiDIG6Es2e2eRC9jlNh7TZE45c0VHtsMxKiUJJwDY9bUmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f477f009.mp4?token=v6QjdrLjrqGLWy6xXFYY-h9_weeHeyiorIfIpcQrtGCIpxKfQgLrYVFeF6kxqgvz8WZeu1iit-QW4KD576CX0lS8eirPaJgebr5txGmizYLqOZFfWCWfS_BlShr4NdVEBcf9VFhUWDdXb9whIlPFxv_4vJWzzuNIiqXXOKZO2X5smGzb3Gg_4Dx8SLp6eTrILOZt8kdAn9vfsvPd9Eb6zLKUq-DrDPtU4kJTMjHy2bjuqiVWUNAoK1gEMvwxLQSPaphZXPz5e8urOjRgxAuPw3eoA-lDnRUsG4drChaLKiDIG6Es2e2eRC9jlNh7TZE45c0VHtsMxKiUJJwDY9bUmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از حمله موشکی به مخفیگاه‌های جدایی‌طلبان در کردستان عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/126380" target="_blank">📅 22:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126379">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8efb5da491.mp4?token=hOyl0vcy6oeD0vJvCealEuT_VfhBWGmWlZZ0wlWCRyUvFaq0oBrlfskG_FzHHjsJlVk1A5GLNac0PhyBTBdIaD2JbloqjS6ZipXstUt--XXZiEbT2WNhu--du0gP8LVD7jhmO68NTv-wYGgMOCAbDh0SjLT-CCx8uqsAl_OT8MYzj-UtL68N2u1xGtD1AD5JDjF0TnEfqvg6MSIV1Tw3Y_ghaXF6JFmZsfE1RAn9mzwF5-WybA-_T-TaRAH28haG7JwRMub2iwBR6zbwPzcIYz_buAZTJhLja7im_KkfREoSTy1kJ8LLwUWiBeMpSznkAXJipL8dmzbXU9nr2PQLJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8efb5da491.mp4?token=hOyl0vcy6oeD0vJvCealEuT_VfhBWGmWlZZ0wlWCRyUvFaq0oBrlfskG_FzHHjsJlVk1A5GLNac0PhyBTBdIaD2JbloqjS6ZipXstUt--XXZiEbT2WNhu--du0gP8LVD7jhmO68NTv-wYGgMOCAbDh0SjLT-CCx8uqsAl_OT8MYzj-UtL68N2u1xGtD1AD5JDjF0TnEfqvg6MSIV1Tw3Y_ghaXF6JFmZsfE1RAn9mzwF5-WybA-_T-TaRAH28haG7JwRMub2iwBR6zbwPzcIYz_buAZTJhLja7im_KkfREoSTy1kJ8LLwUWiBeMpSznkAXJipL8dmzbXU9nr2PQLJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لبنان، صور
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/126379" target="_blank">📅 22:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126378">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
شنیده شدن انفجار در اربیل عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/126378" target="_blank">📅 22:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126376">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgUWChU9O6szOJDZnE764f7mFS-jGYB8ERxLZUYW-ZOEMn2TjzMPCTSeBIzjD9_Ds0E721n1NumjoLBTwcqF-rtCEo4c50Xyf6HMgQzgJ4dRHXSf0hLZEfXWMM2D_50PkvgDpUheXnstawQkFq6OziZ7-CZbyPVwxK0ZwxiIJGhJzgsWRVWlPha4OQn2wAxaLDKmHmnq7YOKEZmN2OGwvFoZBwr2j4WhLFGOgyXuAKJs55-BYAu2pPT8map0NbsDMKg-wEJfavYXhpheLJw4M3aQJIRjY4Gni4RFgGKtjD-JFjMAAKH_54CAZy3X_9FkG-u10Y1femL6XexK0mchEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sdj_gA8eYnYt5LHVsSAfF0cFVJHgHEj-UI8XhDKS2qBCAFUPFiuNErrsoRNW9qYxjuMnFC-9LPWYYq8rHOiS90zwIZfJA5ry38lV5Xb3N9T0t7M5UhWC4E4de2Vyp_hg9IBAPMbBZRh3rQVQttBua3L91yWeBJJOaxifEzfwPCkY4Zrv3IZnXfDSvUCe1k-KHa-84Rlt1l0mDi03Ua6Els6rYfFMYU3cvuV9pJJHFd3XP8QWDya7btFthAMjEkothocdthms7BQG6o9N4XovjaqjiXVuCDAX7c_60C0UWznmFlp_TvHm65rXhI8mh6ygu9TLmsFaYEVJoT2mwXtGAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای Sentinel-2 نشان می‌دهد که به نظر می‌رسد یک موشک ایرانی به انباری در پایگاه هوایی رامات داوید در شمال اسرائیل اصابت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/126376" target="_blank">📅 22:40 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126375">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_CcVwqbRWVMly10ELO6hWCqR44f-9eAPgwzuxtcI0bjJ2CRA8bWjsEY7sZ0p-Imi-BNvkbcULhqMNAqOojRYd-hjl4ah-MMvMCLiPw1qaET-qbwhIRi-1NWKpEGBLhIoaFdNv8uiHCUaQoyEpi-0gLxvFE6CvKvI50glF8Pl43FEtiHE-oIahAmbM7-Z0d1w-BQ1yEgi9q6IpYRLpRMEuyNtSrYn5wWMkEneI85g1O3nMqjV5E28R56uWqVFYLASNhjhQxD_-j1jz05gPU3X8Fp5jIu0XjD6LCFds5Vzi9hyMU1oFLBrKjJgOsrNgxCDQb1oYmEmfZmazXUyyIu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خاویر بالاس ستون نویس بلومبرگ: سقوط آزاد ذخایر استراتژیک نفت آمریکا؛ در آستانه پایین‌ترین سطح ۴۰ سال گذشته
🔴
گزارش‌ها حاکی از آن است که با آزادسازی ۷.۹ میلیون بشکه دیگر از ذخایر استراتژیک نفت ایالات متحده (SPR)، حجم این ذخایر تا پنجم ژوئن به ۳۴۹.۲ میلیون بشکه افت کرده است.
🔴
این روند نزولی نشان می‌دهد که ذخایر استراتژیک آمریکا با سرعت به سمت رکورد ۳۴۶ میلیون بشکه در حرکت است؛ رقمی که پایین‌ترین سطح ثبت‌شده برای این ذخایر در ۴۰ سال اخیر (در دوران دولت بایدن) محسوب می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/126375" target="_blank">📅 22:31 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126374">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / نبویان، نماینده مجلس: ایران پیشنهاد واگذاری تنگه هرمز را داده
🔴
بر اساس پیش‌نویس تفاهم ایران باید ظرف ۳۰ روز ترتیباتی اتخاد کند تا رفت و آمد کشتی‌ها به حالت قبل جنگ برگردد.
🔴
وضعیت اخذ عوارض مشخص نیست.
🔴
وظیفه مین‌روبی هم به ایران سپرده شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126374" target="_blank">📅 22:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24a75b678.mp4?token=myw4VNjousiXCDKnqQDJoGMyVNw11J5cL-oV3INDx-M3JuLgkFnOSyzcDVla4NNw4AsOvn-_1wXuP2MjbZ9sjPQ4_KKa7gKiS1pqagh2vCeUAvoCxqswmWPYyTJa1ZXP6M8dNEJLuUjlCr8TtocZ07YEroK2Nw-BeS3lb-yhSwazi7LoyYOOSRGM71NY3eyrWVq8KB4GSCDyFwYiZWemvjADYMUM9WFb1NpjT_Vj2nr1LlSzrBKLfrYPDsJ22vRUKSWx9-oOvpZS19k9Po66QJKtkYcsBimgTJ-1z3g2xt4rbzka1Q-J6QOWpTF-vz1Y7FUj1hhTpFAQPifaF4agBbFd-_-964w4Wg__we9c0iWEYlAh7gjQWGB1KX1Wop3jZG2P2MZVdgpvcJLoAz1hVe0oc7tVOLsRVSs8f23YMKiLu1Jl2bBcPEIctb7rhgR2iQUWOx-aXVbPTB2EqyT7THa9kpTAdQtWhSVR-3dOt4cJ31E0gDpGqWr1oeu7Hti_tu0X8HqgfC5PdQCLZMkCrvQCqpTxiUZ_p9GDiB46MxzzucKTT-8AZI4R2XzjRCpcqqs-tY2h0N9egw9sa1ZMNtfA6shzC8NJr4enAuK425xSNfiMQk6mS4cL6gnvXm7d3UGRSsmhKBnmdlWq-Ekdg3nshhAY_TElNFauckdV1KY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24a75b678.mp4?token=myw4VNjousiXCDKnqQDJoGMyVNw11J5cL-oV3INDx-M3JuLgkFnOSyzcDVla4NNw4AsOvn-_1wXuP2MjbZ9sjPQ4_KKa7gKiS1pqagh2vCeUAvoCxqswmWPYyTJa1ZXP6M8dNEJLuUjlCr8TtocZ07YEroK2Nw-BeS3lb-yhSwazi7LoyYOOSRGM71NY3eyrWVq8KB4GSCDyFwYiZWemvjADYMUM9WFb1NpjT_Vj2nr1LlSzrBKLfrYPDsJ22vRUKSWx9-oOvpZS19k9Po66QJKtkYcsBimgTJ-1z3g2xt4rbzka1Q-J6QOWpTF-vz1Y7FUj1hhTpFAQPifaF4agBbFd-_-964w4Wg__we9c0iWEYlAh7gjQWGB1KX1Wop3jZG2P2MZVdgpvcJLoAz1hVe0oc7tVOLsRVSs8f23YMKiLu1Jl2bBcPEIctb7rhgR2iQUWOx-aXVbPTB2EqyT7THa9kpTAdQtWhSVR-3dOt4cJ31E0gDpGqWr1oeu7Hti_tu0X8HqgfC5PdQCLZMkCrvQCqpTxiUZ_p9GDiB46MxzzucKTT-8AZI4R2XzjRCpcqqs-tY2h0N9egw9sa1ZMNtfA6shzC8NJr4enAuK425xSNfiMQk6mS4cL6gnvXm7d3UGRSsmhKBnmdlWq-Ekdg3nshhAY_TElNFauckdV1KY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: خیلی عجیب است که افرادی در کشور از مذاکره دفاع می‌کنند در حالی که رئیس هیئت مذاکره‌کننده ایران می‌گوید دشمن به مذاکره اعتقاد ندارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/126373" target="_blank">📅 22:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
میشل عون به سی‌ان‌ان: ما به دنبال رابطه خوب با ایران هستیم، اما نباید در امور ما دخالت کند و کشور ما را به خاطر منافع خود نابود کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/126372" target="_blank">📅 22:17 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126371">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
روسیه: پیش‌نویس قطعنامه آمریکا علیه ایران شرم‌آور است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/126371" target="_blank">📅 22:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126370">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07861131cf.mp4?token=omSd1DbNQMklSdukIVm2rEMNe4kKrZ_38NhYjG_0dUPY4I-UkbNv_EsghqFuCmVKU2HYdUw3PGAIJ-aImStcYF9-9N5kIFnTngM3Q1WWUbkiO5uuxzIUpzfZMWgbZ2685ePIr2E5GXqPwAgSab5is1GzQ3FT1wkUHFpSO0434f-fPkMpBj4__YsoWjzTnmVEuhh1aJx1nsmf1ke3EXdDez4f7l0DKxO7EMouX_sJMxfxGteYQ16ZKfvyPJ04vBwJl0REME8bsvDRCg9cAEwcHTyVC1xmpMeVdtVTBb3QPyuuhay8qfXdoO0o0R0ugUEImIlxmFlDam0fbSs6GELLlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07861131cf.mp4?token=omSd1DbNQMklSdukIVm2rEMNe4kKrZ_38NhYjG_0dUPY4I-UkbNv_EsghqFuCmVKU2HYdUw3PGAIJ-aImStcYF9-9N5kIFnTngM3Q1WWUbkiO5uuxzIUpzfZMWgbZ2685ePIr2E5GXqPwAgSab5is1GzQ3FT1wkUHFpSO0434f-fPkMpBj4__YsoWjzTnmVEuhh1aJx1nsmf1ke3EXdDez4f7l0DKxO7EMouX_sJMxfxGteYQ16ZKfvyPJ04vBwJl0REME8bsvDRCg9cAEwcHTyVC1xmpMeVdtVTBb3QPyuuhay8qfXdoO0o0R0ugUEImIlxmFlDam0fbSs6GELLlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنوب لبنان پس از حملات اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126370" target="_blank">📅 22:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126369">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTrAFkPZFIb_xI4x2rtQ4iVxQ6GCrK7jg5fAAjYZJi5zBQ6H8LKnHUECeudiM-3IoBRqH4yDdPJ3d-y0GMiA-UhrTikIvotA35vuF7c9FzLFmDvT7obXReVJHxVmk-qUyVDojg4WA79yL4-B19_Hkf8CETBDj4K3_S98yuXAQ2JCkLuphWlj6myS8qZL6Bd9GboU01bFMeHmLOfR1EIG-yM-7QDLmMjOvWiKhbco1dV6FKu_lYwnMR9nKTVuuT_DOS451x6CqY_2dUHC3JiaNZUdcVI-RXKgWbY7xOdHINNolLgVcQleMeMM9nG-diNY4i7sW2QI8NWD-z1k-5PpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عارف: دشمن ناچار به التماس مجدد برای آتش‌بس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126369" target="_blank">📅 22:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126368">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e489176d06.mp4?token=N--DJHUs_XiKRXU7Rs5gR5avC3KlyfMkFbwOmWW0pyCtxmAmzGYHppnIw36KyF_d8TuZrb3wXve1-FPV2OSlC30akXAQDiEG4_kaRyi20tzI1U6tAGfg9AwK4IQ3Kg6EFgQoITJtwDMf3PYz5RpliDayA5QOFPC9rHYAKWG_QB7Hfw2Bf231lv7MKrzLdqzpV53Ov8xbhQeTcKAAIDGAq0gshk9ORsjnXLg7-MftwsNP82nalsLKiAiPyI5Gj2WNZAYaGKlIqirriQCgnO50m0Cm1WM2OJc2L4CTzedOs6uVtkCH3HFGjML74AFUAR4DuhWJcxeW0LCxJhjXUFxbrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e489176d06.mp4?token=N--DJHUs_XiKRXU7Rs5gR5avC3KlyfMkFbwOmWW0pyCtxmAmzGYHppnIw36KyF_d8TuZrb3wXve1-FPV2OSlC30akXAQDiEG4_kaRyi20tzI1U6tAGfg9AwK4IQ3Kg6EFgQoITJtwDMf3PYz5RpliDayA5QOFPC9rHYAKWG_QB7Hfw2Bf231lv7MKrzLdqzpV53Ov8xbhQeTcKAAIDGAq0gshk9ORsjnXLg7-MftwsNP82nalsLKiAiPyI5Gj2WNZAYaGKlIqirriQCgnO50m0Cm1WM2OJc2L4CTzedOs6uVtkCH3HFGjML74AFUAR4DuhWJcxeW0LCxJhjXUFxbrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصویر آخرالزمانی از زلزله ۷/۸ ریشتری‌ فیلیپین؛ این ۳ ساختمان متصل به هم از یکدیگر جدا شدند و آب استخر به پایین می‌ریزد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/126368" target="_blank">📅 21:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126367">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
استان یزد فردا تعطیل شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126367" target="_blank">📅 21:55 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126366">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ef830c9ba.mp4?token=v8XMBMyuObD7Ds1Ux_fBPZAJIrd_XfpYHzFOVnQvKklF7NP7-ogjqvhiCp7e8xvCdXuuQUocUxHtwLWgqe_9w_pZdXFxFpEcG1MRRycvuGcmC0RuCXyETOE9LvtKcxqihqpo3n7WL0DgAQmAKHCilnBiqBGPnxDy4FH94KuZ2vK9uPMkPC7oqJOplQKA336VhJY8uboKptgpsg4C6wlcb5Z6Ax4inFJS7BMBbG0miUlh03NjSrBgRBZec5yR-tjq0ezOoRIh6LjK8n0RZdhW7ioXZKTxYa_0dR_6KAOPzm9rkUf-t3uLqj5xdBvDvCTpLfyzOVk8giaPWMgbnNIX8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ef830c9ba.mp4?token=v8XMBMyuObD7Ds1Ux_fBPZAJIrd_XfpYHzFOVnQvKklF7NP7-ogjqvhiCp7e8xvCdXuuQUocUxHtwLWgqe_9w_pZdXFxFpEcG1MRRycvuGcmC0RuCXyETOE9LvtKcxqihqpo3n7WL0DgAQmAKHCilnBiqBGPnxDy4FH94KuZ2vK9uPMkPC7oqJOplQKA336VhJY8uboKptgpsg4C6wlcb5Z6Ax4inFJS7BMBbG0miUlh03NjSrBgRBZec5yR-tjq0ezOoRIh6LjK8n0RZdhW7ioXZKTxYa_0dR_6KAOPzm9rkUf-t3uLqj5xdBvDvCTpLfyzOVk8giaPWMgbnNIX8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه حمله اسرائیل به مناطق جنوبی لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126366" target="_blank">📅 21:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126365">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
رئیس سازمان انرژی اتمی: واحدهای دوم و سوم نیروگاه بوشهر با سرمایه‌گذاری ۱۰ میلیارد دلاری در حال ساخت است/ دستیابی به ۲۰ هزار مگاوات برق هسته‌ای در دستور کار قرار گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126365" target="_blank">📅 21:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126364">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
وزیر امور خارجه فرانسه به الحدث:
بستن تنگه هرمز هزینه بسیار زیادی بر اقتصاد جهانی تحمیل می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/126364" target="_blank">📅 21:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126363">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
سفارت ایران در بیروت اعلام کرده است که «لبنان قلب ایران است»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126363" target="_blank">📅 21:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126362">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
در پی تداوم تنش‌ها، شرکت هواپیمایی «ایر فرانس» نیز به جمع شرکت‌هایی پیوست که پروازهای خود به مقصد اسرائیل را به حالت تعلیق درآورده‌اند.
🔴
شرکت «ایر فرانس» تمامی پروازهای خود به مقصد اسرائیل را تا ۲۱ ژوئن ۲۰۲۶ لغو کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126362" target="_blank">📅 21:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126361">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
قالیباف: هدف ما پایان جنگ و ایجاد امنیت پایدار است و نه عادی سازی روابط با آمریکا و اعتمادی هم به طرف مقابل نداریم. البته روش ما احساسی عملیات کردن یا صرفا اعلام حقوق ملت ایران یا محکوم کردن جنایات دشمن نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126361" target="_blank">📅 21:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126360">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
قالیباف: دست نیروهای مسلح برای اقدام همواره باز بوده و بر اساس تدبیر و برنامه ریزی درست و تصمیم تصویب شده عمل می کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126360" target="_blank">📅 21:09 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126359">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
قالیباف: قرار نیست یا جنگ کنیم و یا مذاکره بلکه قرار است به وقت خود جنگ کنیم و به وقت خود مذاکره کنیم و اینگونه است که می توانیم دشمن را شکست دهیم و این که می گوییم مذاکره ادامه مبارزه است عینیت پیدا کند.
🔴
لازم است روی یک برداشت غلط خط بطلان بکشم، برخلاف تصور برخی که فکر می کنند بین مسئولان هماهنگی نیست، هماهنگی کامل برای رسیدن به اهداف میان مسئولان وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126359" target="_blank">📅 21:08 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126358">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
قالیباف: ماجرای لبنان نشان می دهد میدان دیپلماسی کنار میدان نظامی می تواند اسرائیل و دشمنان را کنار بزند.
🔴
نه دیپلماسی مانع عملیات نظامی است و نه عملیات نظامی مانع دیپلماسی است.
یک بار با تهدید به حمله و قطع مذاکره جلوی حمله اسرائیل به بیروت را می گیریم و بار دیگر با حمله نشان می دهیم ترسی از قطع مذاکرات نداریم و نتیجه این می شود که آنها مجبور می شوند عقب نشینی کنند و ما حق خود را تثبیت می کنیم.
🔴
تصور کنید اگر ما در میدان نظامی پیروز نشده بودیم یا در میدان دیپلماسی جلو نرفته بودیم و یا میدان های نظامی و دیپلماسی با یکدیگر به درستی پاسکاری نکرده و پشتیبانِ هم نبودند و با هم هماهنگی نداشتند، آن وقت دست ما برای حمایت از لبنان و مقابله با محاصره دریایی بسته بود.
🔴
موضوع فقط لبنان نیست بلکه موضوع رسیدن به حق مردم و ایجاد امنیت باثبات برای کشور است و باید هر ۴ میدان در کنار هم و هماهنگ با یکدیگر این اهداف را تأمین کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/126358" target="_blank">📅 21:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126357">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28cb167517.mp4?token=t2PGJkQGs57SdS3rTMA7f83nJ_c8aVoP67eyhqjwh4tWP42eNkv4GT9mt_HSFYcBTA4iiS0Ey_BKAPvD5jjKkjsftBXfJWe5OgHkv5-tgetbobpzMuRK78dYGwJPeOmqt8kpcFN3_fYfnDRv12K2kueKne3XYscFOcLK0JOn3EAd4QIi_bQtiZliL4Am7WVKhYSpfP-h-j_ZeP1tH9kyvOLN5GfOS64rdGZiMOvyDQxWEVr-TQlb3K5siEzE2FDL4EQUZUPDsb0K1bHCGpSnRgz3nujNgXFHIM_ecnkiP-fT9ntF92-P5uIP9rU-tXZdFjCzwoyZr9Mcx6BMBNnY1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28cb167517.mp4?token=t2PGJkQGs57SdS3rTMA7f83nJ_c8aVoP67eyhqjwh4tWP42eNkv4GT9mt_HSFYcBTA4iiS0Ey_BKAPvD5jjKkjsftBXfJWe5OgHkv5-tgetbobpzMuRK78dYGwJPeOmqt8kpcFN3_fYfnDRv12K2kueKne3XYscFOcLK0JOn3EAd4QIi_bQtiZliL4Am7WVKhYSpfP-h-j_ZeP1tH9kyvOLN5GfOS64rdGZiMOvyDQxWEVr-TQlb3K5siEzE2FDL4EQUZUPDsb0K1bHCGpSnRgz3nujNgXFHIM_ecnkiP-fT9ntF92-P5uIP9rU-tXZdFjCzwoyZr9Mcx6BMBNnY1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیرو های نظامی ایران خطاب به ترامپ:
عمو ترامپ با توئیت که نمیشه جنگ کرد، این ارتش و ناو و جنگنده‌هاتو بفرست خسته شدیم دیگه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126357" target="_blank">📅 21:05 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126356">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
کانال ۱۳ تلویزیون اسرائیل به نقل از یک منبع: نتانیاهو به وزرا اطلاع داده است که انتظار می‌رود اسرائیل به چندین دور از تشدید تنش با ایران بازگردد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126356" target="_blank">📅 21:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126355">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
عراقچی: همسایگان ما در اولویت ما هستند
🔴
صمیمانه‌ترین تبریکات خود را به جناب آقای نیکول پاشینیان، نخست وزیر ارمنستان، بابت پیروزی حزبشان در انتخابات ابراز می‌داریم.
🔴
خوشحالیم که فرصت خوبی برای استمرار همکاری های سازنده در راستای تقویت روند پویای حاکم بر روابط ایران و ارمنستان فراهم شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126355" target="_blank">📅 21:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126354">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
قالیباف: صحبت های رئیس جمهور آمریکا درباره یادداشت تفاهم، مخالف بخش های توافق شده بود که نشان داد آنها نه دنبال آتش بس هستند و نه دنبال گفت وگو و باید برای دفاع از حقوق ملت ایران پاسخ قاطع می دادیم که به لطف الهی نیروهای مسلح ما با اقتدار به وظیفه خود عمل کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126354" target="_blank">📅 21:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126353">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
قالیباف: آنچه باعث تنش های اخیر شد این بود که آمریکایی ها هم با محاصره دریایی علیه ملت ایران و هم با نقض توافقی که درباره آتش بس لبنان شده بود، آتش بس را نقض فاحش کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/alonews/126353" target="_blank">📅 21:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126352">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دونالد ترامپ مدعی شد که پنج کشور منطقه که در میانجی‌گری میان آمریکا و ایران نقش دارند، از او خواسته‌اند تا بر بنیامین نتانیاهو، نخست‌وزیر اسرائیل فشار آورد تا حملات را متوقف کرده و به سمت توافق حرکت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126352" target="_blank">📅 20:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126351">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی به کانال ۱۴ گفت که: بازگشت به درگیری شدید با رژیم ایران «فقط مسئله‌ای در کوتاه‌مدت است، احتمالاً در روزهای آینده».
🔴
وضعیت هشدار بالا تا اطلاع ثانوی، هم از نظر دفاعی و هم تهاجمی، حفظ می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126351" target="_blank">📅 20:57 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126350">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ: فکر میکنم ایران مایل به امضای توافق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126350" target="_blank">📅 20:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126349">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
حداقل ۳۲ نفر کشته شدند و بیش از ۱۰۰ نفر زخمی شدند در نتیجه زلزله قدرتمند با بزرگای ۷.۸ ریشتری که در سواحل مینداناو در جنوب فیلیپین رخ داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126349" target="_blank">📅 20:54 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126348">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ترامپ به کانال ۱۲ اسرائیل: به نتانیاهو گفتم اگر جنگی تمام‌عیار علیه ایران آغاز کند، او را تنها خواهم گذاشت
🔴
من دیشب از نتانیاهو خواستم که به حملات ایران پاسخ ندهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126348" target="_blank">📅 20:43 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126347">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ : اسرائیلی‌ها وقتی جنگنده‌هاشون تو مسیر ایران بودن، به ما خبر دادن
🔴
من هم سریع وارد عمل شدم و تلاش کردم ابعاد حمله محدودتر بشه
🔴
همچنین پنج کشور منطقه با من تماس گرفتن و خواستن روی نتانیاهو فشار بیارم که حمله نکنه
🔴
من هم با نتانیاهو صحبت کردم و اون در نهایت موافقت کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126347" target="_blank">📅 20:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126346">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
برخی کاربران مدعی شده‌اند که دارایی‌شان در چند صرافی رمزارز خارجی، به بهانه تحریم و بدون هشدار قبلی مسدود شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126346" target="_blank">📅 20:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126345">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
سخنگوی سیاسی جنبش حماس مدعی شد ایران به این جنبش اطلاع داده که در حال انجام تلاش‌ های فشرده برای گنجاندن غزه در چارچوب یک آتش‌ بس منطقه‌ ای میان ایران و ایالات متحده است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126345" target="_blank">📅 20:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126344">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNotOb40_KGfOJSNRZxB8FMaRVLstjC1FcjVDnDdbaCQYYY4kGXfC3RrhfOgtbzb3x7f2LN7YpLijS-z2LhGgKU2zpp5k_RFK3Q7KulZn_Fe84ZgRe-97v-auh7EE7SU2ZyGtwnwIrSgX7eAT5Ro-HKAySqDmvSJDngbI7IQ9xedlcUmH5liv2cUqD0KOfaarbETBVkZMdkM5OPDRTOo-V9nZkecf0cMM0HrPHpp21D3348hJD0IyYVvGD04SqjU42tYOHl6ZTTcEF7pk9P0cg2Xn0QdOraWJGPecqIoN9JGRWr7rJX0QhVDYZN6-aiRWiTJgkvBf5ZZgmjj-XQcXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت‌های عجیب هارد اکسترنال!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126344" target="_blank">📅 20:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126343">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd75eece7.mp4?token=Uut2GjXT0KngE5_7Lfeq7OoX3P6OUomPiK-HNxfvz_z8kA_9tB1eyXfZxspQiBRluD8__tV18ZAeyitNOL1bZ0IOrTch8v9bMnniqa2_1FERh1l5MO6pNKAJ7Be9f3Vp2LcCv8n1Psa9SEgist7wwTUu3UtHrqiaAnWaKvntpubuIPPCWkdg7jkA1CON7B0i24M_jhFbgHEpqWqiZ9jHPEYexGeQ8M0z1aqxvgQA5UtQuE_TTlCsxAo9aNJ-17MjB8yqVd8MqizBiHa6fTxpIho_BHvvkObG5_yQJRcfeOjKckdj63XDmCAMo39h9Kp97L1-21rj1_tIFzAUVOV8yYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd75eece7.mp4?token=Uut2GjXT0KngE5_7Lfeq7OoX3P6OUomPiK-HNxfvz_z8kA_9tB1eyXfZxspQiBRluD8__tV18ZAeyitNOL1bZ0IOrTch8v9bMnniqa2_1FERh1l5MO6pNKAJ7Be9f3Vp2LcCv8n1Psa9SEgist7wwTUu3UtHrqiaAnWaKvntpubuIPPCWkdg7jkA1CON7B0i24M_jhFbgHEpqWqiZ9jHPEYexGeQ8M0z1aqxvgQA5UtQuE_TTlCsxAo9aNJ-17MjB8yqVd8MqizBiHa6fTxpIho_BHvvkObG5_yQJRcfeOjKckdj63XDmCAMo39h9Kp97L1-21rj1_tIFzAUVOV8yYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات هوایی اسرائیل چند لحظه پیش ارتفاعات ملکخ در جنوب لبنان را هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/126343" target="_blank">📅 20:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126342">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
روسیه از شهروندان خود خواست به اسرائیل سفر نکنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126342" target="_blank">📅 20:27 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126340">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4242e53622.mp4?token=V8tLXHQsIEw5q2mGdVeGj9-OyIqtYn5Ut8PGbZU6Od_qwK-urbYeNJZStTblX2RW4QBSEwUIcEfeIPh3NWTdmWL_jITvS9GfvjPfw23b6HO6eoJFa1VNTH_mtJ-U0v79WB3TURQJehgcvMME7-VGn6zcsdhlMWdnYw1tUWmt2VQGJ29iebplDXnZ26LiT99iC-MspccME3Y2Vxlkl33cdt-w6LsuVB2kLRDjSoWzbSlVhWjgDqCtB0ctm6x82hDHqmZ0QYhpwiC4dlQCESineEWQwgDyggiD1hmxQKkI-kMWlxSYN4lkoleAnwu6gOYyCgr8GGBQhu7dqXS3xKXD-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4242e53622.mp4?token=V8tLXHQsIEw5q2mGdVeGj9-OyIqtYn5Ut8PGbZU6Od_qwK-urbYeNJZStTblX2RW4QBSEwUIcEfeIPh3NWTdmWL_jITvS9GfvjPfw23b6HO6eoJFa1VNTH_mtJ-U0v79WB3TURQJehgcvMME7-VGn6zcsdhlMWdnYw1tUWmt2VQGJ29iebplDXnZ26LiT99iC-MspccME3Y2Vxlkl33cdt-w6LsuVB2kLRDjSoWzbSlVhWjgDqCtB0ctm6x82hDHqmZ0QYhpwiC4dlQCESineEWQwgDyggiD1hmxQKkI-kMWlxSYN4lkoleAnwu6gOYyCgr8GGBQhu7dqXS3xKXD-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیستم پدافندی اوکراین پهپاد انتحاری روسیه رو مهندم میکنه، حین سقوط مستقیم میره میخوره تو یه ایستگاه اتوبوس
🔴
دو کشته و ۱۲ زخمی گزارش شده!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126340" target="_blank">📅 20:23 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126339">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9417287cba.mp4?token=TCbR-_c40GUQAyt6Oq0Yf88t_z3aOcZNaP6Dn8vBd1YhjxmJUbGsAfPNbws0WDBknqQAH_hAUJE5L1IvQGHNTR92kWRNHjGKm2CgcrKCamokknWedArtLRafIer2KTB8gkV3K63Wvj715biTaKwPlUZzEV9gjogCDkelzLj-heAPKuddWGPjsInK3Ark0VUG0hsvWkpgGKNKQzFY-pdHL9xNHIm7M3Fj2b7fqyOX2jgpqk1I_Zy8zJkX4K1_JjfJTrRHTnumJ-KIx-rJPb2YL9VlEtRYBRfjxYDP98yXoq-Pd-bkRcEkXfxN2ybMpchxrpcFUMf38iCjfDzEPiBIBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9417287cba.mp4?token=TCbR-_c40GUQAyt6Oq0Yf88t_z3aOcZNaP6Dn8vBd1YhjxmJUbGsAfPNbws0WDBknqQAH_hAUJE5L1IvQGHNTR92kWRNHjGKm2CgcrKCamokknWedArtLRafIer2KTB8gkV3K63Wvj715biTaKwPlUZzEV9gjogCDkelzLj-heAPKuddWGPjsInK3Ark0VUG0hsvWkpgGKNKQzFY-pdHL9xNHIm7M3Fj2b7fqyOX2jgpqk1I_Zy8zJkX4K1_JjfJTrRHTnumJ-KIx-rJPb2YL9VlEtRYBRfjxYDP98yXoq-Pd-bkRcEkXfxN2ybMpchxrpcFUMf38iCjfDzEPiBIBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حزب الله تصاویری را منتشر کرد که نشان می دهد جنگنده های آنها یک تانک مرکاوا را در مجاورت قلعه بوفورت در جنوب لبنان در 4 ژوئن با استفاده از یک موشک هدایت شونده هدف قرار می دهند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/126339" target="_blank">📅 20:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126338">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزارت خارجه ایالات متحده فروش احتمالی ۱.۹۸ میلیارد دلار سلاح به کویت برای سیستم‌های ضد پهپاد و تجهیزات مرتبط را تایید کرده است.
🔴
این بسته شامل پلتفرم‌های ضد پهپاد رودرانر و آنویل، جعبه‌های پرتاب، سیستم‌های فرماندهی و کنترل لاتیس، برج‌های نگهبانی برد بلند و دریایی، سیستم‌های جنگ الکترونیک پالسار، مراکز عملیات تاکتیکی، به همراه خدمات پشتیبانی و آموزش مرتبط است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126338" target="_blank">📅 20:16 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126337">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وال استریت ژورنال به نقل از یک مقام آمریکایی: نیروهای آمریکایی به رهگیری موشک‌های شلیک شده توسط ایران به اسرائیل کمک کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126337" target="_blank">📅 20:13 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126336">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گروسی در پاسخ به سوالی درباره ۱۷ حمله به تاسیسات اتمی ایران: من در این باره چیزی برای گفتن ندارم.
🔴
نماینده ایران حق دارد اعتراض کند اما من با آن‌ها موافق نیستم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126336" target="_blank">📅 20:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126335">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
آی۲۴ نیوز عبری: هدف حمله اسرائیل به پتروشیمی کارون در ماهشهر، مختل کردن عملیات و توقف تولید این مجموعه بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/126335" target="_blank">📅 20:07 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126334">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
سنتکام: یک نفتکش مرتبط با ایران را متوقف کردیم
🔴
فرماندهی مرکزی ایالات متحده:
نیروهای آمریکایی در ۸ ژوئن یک نفتکش خالی را در خلیج عمان، پس از آنکه این کشتی با تلاش برای حرکت به سمت یک بندر ایرانی، محاصره مداوم علیه ایران را نقض کرد، از کار انداختند.
🔴
فرماندهی مرکزی ایالات متحده (CENTCOM) کشتی M/T Marivex با پرچم پالائو را هنگام عبور از آب‌های بین‌المللی در خلیج عمان به سمت ایران از کار انداخت.
🔴
یک فروند جنگنده F/A-18 Super Hornet از ناو هواپیمابر USS Abraham Lincoln (CVN 72) پس از آنکه خدمه از دستورالعمل‌های نیروهای آمریکایی پیروی نکردند، یک مهمات دقیق به سمت فضای مهندسی و هدایت کشتی شلیک کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/126334" target="_blank">📅 20:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126333">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رادیو اسرائیل: ارتش اسرائیل در ساعات اخیر در حال آماده‌سازی موج بزرگی از حملات هوایی علیه ایران بود، با ده‌ها جنگنده نیروی هوایی که قرار بود به اهدافی در سراسر کشور حمله کنند
🔴
با این حال، این عملیات گسترده در نهایت انجام نشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126333" target="_blank">📅 19:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126332">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc8KtAkfwC2P4CieC_8vGJCcfuoob-2r3pGGePO58zEIEJPuDijh9-5T7Qi00N_L1VtbcSeL8Qx1ZIOd5iKf3m_2OwVsObJBS4KJhPqMR3i34wRHulAVZyuqnea9uztYlD67jJCr7znf_fx4r25UYzL7fYtKw_-VnRO9kanyVQ0EEbTtvc2SRsr8DPDXyiUqKuerVXptCz0UP6qUH3_VMrWULSGngBTBznQVJgmFwikDZJY_BSSRQO9G27MM1OE5UovGenk_lv4DbLzJROky8S6_ZkWNc38L-NGxwHwvAxsfknOk5e7KHkk-tNZH2nN4MEBJoLzagfn8ModpUO9jtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوک این از جنگ هم بدتر بود
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/126332" target="_blank">📅 19:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126331">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bone7TV1nFZaviRGwRmRVrtNzezSXMh2IZfyCqkohYFgtqdKlDfOaJUgEMc4tNFvx5enzl8lNFD4BHOeXBCWVzrbFJEgTt4OuIF_6lkim6TBxolEkNQi73cIdxsSX2J7e1PMoTDDKJws8qC7X3DuYsyHlGftXTlHbqWhEQ_HVhX9XRxf_3TAVvmQdIbkcaa0aQ36t40Zux5zw-Oa5-Z7d7YXjbXQYd2yyMqQy8McqIuLJK0qnyknz9oP-vOCQzC_Hc_eVNkAqeJ5pf-dDiAmwaVwfp_UZM8cdUyr5xJwOJz9_YStYcqPlox6VU0pbpLYaFvtgnrykA3uN-YKh4VeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫
🏆
به دنیای هیجان‌انگیز فوتبال خوش اومدی!
⭐️
اینجا قراره باهم لحظه‌به‌لحظه‌ی جام جهانی رو زندگی کنیم؛
از بازی‌های حساس و نتایج داغ گرفته تا حاشیه‌ها، کری‌خونی‌ها و اتفاقاتی که همه درباره‌ش حرف میزنن!
🔥
🔥
✅
پوشش کامل مسابقات
💀
ترول تیم‌ها و بازیکن‌ها
🎥
ویدیوها و لحظه‌های فان فوتبالی
📊
آمار، ترکیب‌ها و اخبار فوری
🌍
حواشی جذاب از سراسر جام جهانی
📢
اینجا فقط یک کانال خبری نیست؛
یک جمع فوتبالیه برای کسایی که فوتبال رو با هیجان، شوخی و احساس واقعی دنبال میکنن
📛
💟
🆘
🔞
آماده باش چون قراره جام جهانی رو متفاوت تجربه کنیم!
⚡
@Vaarzesh_Plus
⚡
@Vaarzesh_Plus</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/126331" target="_blank">📅 19:56 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126330">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4446250ba8.mp4?token=LQ8HFVBE93Rn8kogGuF6g5rvfehhf8gu6tbh6TiuvaU9w0aZR5_RcE-97XxxhaR6XtEG_qJqi0MknPDXyohGsN3vL_Wh9xzu6wvBCbsaRZwxBjEeTSb-4WCgMpm9rMYCLHaRXH3KZ2L0TVhg6WcCufJLZDm5gy4z3314boyhvbInDudv2gZC7GCoNJ_Ot7i3HoHwAms8QekI4A4zejD6Zfg3BP-tUGMxUL0mwpb-aEfzf74li5sZArEG6pnRu8kwOAb9qt7UELAV6_ebnDsGw6H6wa1p0816v-CZf4UID79n07z_TIhYPSBt16RLB1J3VnRG9Jd0iCgTJP1NBxQ1CIeG47YZ7z2hHhF9HN14UsSKchct1wuw-CMzCI-hcOeNlmyCAFsYX4l6eIxIc24r89SDQmFPKaxmaC8KO07S-B9SA9f6ZyAGP683C5NxU8rfafI1Tw1bah4JSKPQ5QMFpsD1MhsvcDBss8wkEwvWKMJ6rBbFjDcpPFwCyH_qLbEY4lWlGy0qDdMvrL_-6fQZ-blLYkXyl41QzzbaAe3X4HfvbKN5SfmrJHjnEnvEPBf519TBmOFcU6WICCMpwQDLPiRXVJZ5S0iSSIiRAi6cQi489ZwGycF13J2zqvqYKAQKKsHo-ukap70VQ86q_2zcLsGqPP_7F4HpNjAvK2UZFnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4446250ba8.mp4?token=LQ8HFVBE93Rn8kogGuF6g5rvfehhf8gu6tbh6TiuvaU9w0aZR5_RcE-97XxxhaR6XtEG_qJqi0MknPDXyohGsN3vL_Wh9xzu6wvBCbsaRZwxBjEeTSb-4WCgMpm9rMYCLHaRXH3KZ2L0TVhg6WcCufJLZDm5gy4z3314boyhvbInDudv2gZC7GCoNJ_Ot7i3HoHwAms8QekI4A4zejD6Zfg3BP-tUGMxUL0mwpb-aEfzf74li5sZArEG6pnRu8kwOAb9qt7UELAV6_ebnDsGw6H6wa1p0816v-CZf4UID79n07z_TIhYPSBt16RLB1J3VnRG9Jd0iCgTJP1NBxQ1CIeG47YZ7z2hHhF9HN14UsSKchct1wuw-CMzCI-hcOeNlmyCAFsYX4l6eIxIc24r89SDQmFPKaxmaC8KO07S-B9SA9f6ZyAGP683C5NxU8rfafI1Tw1bah4JSKPQ5QMFpsD1MhsvcDBss8wkEwvWKMJ6rBbFjDcpPFwCyH_qLbEY4lWlGy0qDdMvrL_-6fQZ-blLYkXyl41QzzbaAe3X4HfvbKN5SfmrJHjnEnvEPBf519TBmOFcU6WICCMpwQDLPiRXVJZ5S0iSSIiRAi6cQi489ZwGycF13J2zqvqYKAQKKsHo-ukap70VQ86q_2zcLsGqPP_7F4HpNjAvK2UZFnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اردوغان با دلسی رودریگز، رئیس‌جمهور موقت ونزوئلا، در استانبول دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/126330" target="_blank">📅 19:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126329">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
تایمز اسرائیل: اسراییل اکنون در تلاش است تا جنوب لبنان را از توافق آتش‌بس حذف کند و با تهدید موشکی علیه بیروت، حزب‌الله را به توقف حملات به شمال اسرائیل وادار سازد، معادله‌ای که با مخالفت قاطع حزب‌الله لبنان مواجه شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126329" target="_blank">📅 19:45 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126328">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزارت دفاع عربستان سعودی اعلام کرد که یک موشک بالستیک که صبح زود از یمن شلیک شد، دچار نقص فنی شد، از مسیر برنامه‌ریزی شده منحرف گردید و در نهایت در منطقه‌ای غیرمسکونی نزدیک مرز عربستان و یمن سقوط کرد.
🔴
این موشک توسط حوثی‌ها (انصارالله) شلیک شده بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126328" target="_blank">📅 19:39 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126327">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
آی۲۴ نیوز عبری: هدف حمله اسرائیل به پتروشیمی کارون در ماهشهر، مختل کردن عملیات و توقف تولید این مجموعه بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126327" target="_blank">📅 19:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126326">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
دستور بازگشت فضای هوایی کشور به شرایط عادی داده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126326" target="_blank">📅 19:35 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126325">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
خضریان، عضو کمیسیون امنیت ملی مجلس: حملات موشکی ما تا برقراری آتش‌بس در لبنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126325" target="_blank">📅 19:33 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126324">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTaE04E5eE0d5p7yj3taT_h0m9Fkmyq3QyjUI6Mh-UFEePEtUSPVX-LjNKEUeFS4TgNqBi1frBq_oNqXzZL8QExe58F_Ou5kXtG9pBl_tx9alxKHIHnlp0WFOa5uP-0tPsIplcEpfIe0pTuhU9g7ubNyjzzGKP17pQgnn5i_n_ZfOnaQfMjLyGlZ8c1qHBnlH5TugjLiCflNhmbW4KamAJdDsIVcwZ0e8i2MFmHcQj0epuzfFcKuqkQO5ry36V1Uh1to3FHlPGAN0u4pekt1RrAtx9jwBIf2pag-jX_RnoT77oazaqc0gwpkXkbSF7yrmMDjJ4r2T4Mp1xQWEsHHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترور هدفمند در صور، جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/126324" target="_blank">📅 19:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126323">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نتانیاهو: اکنون در جبههٔ ایران آتش‌بس برقرار شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/126323" target="_blank">📅 19:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126322">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvqCphaaxITCesqNFS1xJ6YgzXU63O5gH21d2fMGnVwCsWWf2RM6lNvYd9JrUjV8bYLhqqhYR5SbxRJCoLA038w4GGw9Opa1P6d5siSfpPh4ui7Wb8kRXVrcOTfDTVBOj9yXKCnNPv4c-Sc6J1lr9bR-BfRMi-95O90z6RQ4vLCWQPyp3-UiT1NVMrQODRhrCa3WCV-XKuhvbtVGd-GyWDoREfsJnXlhtYDo79BMV3ufv3A4TpHstvK5iK9EDtNiDO0p2QL8i3JI-JkgLjnTWkXWxHsbY-Ed00ltcBPzuimjVNpKc-6xjv0JXmKDJezZB6QsZykCGlDZziu6hSM3kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / ارتش اسرائیل به ساکنان منطقه زوقاق المفدحی تو شهر صور هشدار داده تخلیه کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/126322" target="_blank">📅 19:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126321">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
نتانیاهو:همانطور که به دوست خود، رئیس‌جمهور ترامپ می‌گویم: ما اسرائیل را با عزم و هوشمندی دفاع خواهیم کرد و با هم امنیت را به شمال اسرائیل بازخواهیم گرداند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/126321" target="_blank">📅 19:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126320">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل: وضعیت حومه جنوبی بیروت همانند وضعیت شهرک‌های شمال اسرائیل است.
🔴
هر حمله‌ای به شهرک‌های شمال اسرائیل با حمله به حومه جنوبی پاسخ داده خواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126320" target="_blank">📅 19:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126319">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
نتانیاهو: فعلاً از حمله به ایران خودداری می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126319" target="_blank">📅 19:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126318">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e1620903.mp4?token=Q6ubyK8aK0Hc5fNld8Sutv0nAmEm-NjHGTrJMZPKvjdcg-R2kDjcVu0I9dsAKh_v9VgMO7i0lJhscUAi5mZjuuEHAnH1UGn5ldDiz7wVmmoQPAxrvxKeObgxj-I0jj7FgFlBckUxFHZ3WVb1TZpR_fzQnQ8lt9d8YsTgmveuLa-aLkRb6HgAnnhsJdfaBN-Xg_D0O-9l9haPRlBJUll2zadD1rDCS364vLTgid3USSEzJ6R8yKg6Rx6wAgao5NtF2RDjf74T3i9a_F5nI7povdbGt8GoP9WYGKFr4W9ZRIK6DsV5SFDwEHyTui5rzLu5NBryApy6J9fifB1a3NHcpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e1620903.mp4?token=Q6ubyK8aK0Hc5fNld8Sutv0nAmEm-NjHGTrJMZPKvjdcg-R2kDjcVu0I9dsAKh_v9VgMO7i0lJhscUAi5mZjuuEHAnH1UGn5ldDiz7wVmmoQPAxrvxKeObgxj-I0jj7FgFlBckUxFHZ3WVb1TZpR_fzQnQ8lt9d8YsTgmveuLa-aLkRb6HgAnnhsJdfaBN-Xg_D0O-9l9haPRlBJUll2zadD1rDCS364vLTgid3USSEzJ6R8yKg6Rx6wAgao5NtF2RDjf74T3i9a_F5nI7povdbGt8GoP9WYGKFr4W9ZRIK6DsV5SFDwEHyTui5rzLu5NBryApy6J9fifB1a3NHcpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: اگر ایران اشتباه کند و حملات خود را علیه ما از سر بگیرد، ما با قدرت پاسخ خواهیم داد، زیرا اسرائیل حق دفاع از خود را دارد و ما از این حق دفاع خواهیم کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126318" target="_blank">📅 19:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126317">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02f10c40e.mp4?token=MC8KYhc180Nx-SvyjGETCVcfnxdDdnaGx70u8011h8kn-Ez5uMu2Dy46Omzl0wNikHQsZsYaiXVQgPOXDNqpEme36LzRqfFxcBThAfBJ-MAw8NFAAdYemVz19oYsR3riFeD4nu01aGkOrof0jRHmHNwRgDW_bob5gyoRWJ5NZFV-VzNDY-Yj4e2MimvTH28pIjBB45FhpPffAcJgMSqq15WkJT3tAXHPu34RAfiTWbaNKAtItOTJ-z4UAQrHTmIITTxD1y1c6ySzVt6Q-8BslpCoJWVMBpMZliHoanZ_i3MUmEjZrnm9c9G6wdOrtMfuA2rWuhopdTvXA25ZwD4ZMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02f10c40e.mp4?token=MC8KYhc180Nx-SvyjGETCVcfnxdDdnaGx70u8011h8kn-Ez5uMu2Dy46Omzl0wNikHQsZsYaiXVQgPOXDNqpEme36LzRqfFxcBThAfBJ-MAw8NFAAdYemVz19oYsR3riFeD4nu01aGkOrof0jRHmHNwRgDW_bob5gyoRWJ5NZFV-VzNDY-Yj4e2MimvTH28pIjBB45FhpPffAcJgMSqq15WkJT3tAXHPu34RAfiTWbaNKAtItOTJ-z4UAQrHTmIITTxD1y1c6ySzVt6Q-8BslpCoJWVMBpMZliHoanZ_i3MUmEjZrnm9c9G6wdOrtMfuA2rWuhopdTvXA25ZwD4ZMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ایران و حزب‌الله از همیشه ضعیف‌ترند و ما از همیشه قوی‌تر.
🔴
کارزار ما علیه آنها هنوز تمام نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126317" target="_blank">📅 19:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126316">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f62b9b32b4.mp4?token=pVPaV_2rtMAsYuf-h67OLI6ipp009Wafk-XKpzsedcGAHvY5kAfd5wLa4Mx9YHjfP9BdWGUxvB3hRzu8jwNlTYAN1E4Zuj0BT4qn2l6tImGixxrDa5JOCEIo3hrj3RSGr2SRvC4WBmBHpc9ujIsoUdLWSvsBecEFBmxgkRtnWXcAWn-Dj1ZTgA8N513LsdQy93dMNPmHaR8rX6Slk2Ikyg34Aio3Ii16e1srXBhkZbiljF5wrCDsBlnwhrojrYiNLzNmkskeEBfT2BDbExMyluSYVrft09jJ3XZoEEfP_6GFP_53s7Xaz29J2q6NSSLHWvUDeOhLE75P0HVoM3XRTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f62b9b32b4.mp4?token=pVPaV_2rtMAsYuf-h67OLI6ipp009Wafk-XKpzsedcGAHvY5kAfd5wLa4Mx9YHjfP9BdWGUxvB3hRzu8jwNlTYAN1E4Zuj0BT4qn2l6tImGixxrDa5JOCEIo3hrj3RSGr2SRvC4WBmBHpc9ujIsoUdLWSvsBecEFBmxgkRtnWXcAWn-Dj1ZTgA8N513LsdQy93dMNPmHaR8rX6Slk2Ikyg34Aio3Ii16e1srXBhkZbiljF5wrCDsBlnwhrojrYiNLzNmkskeEBfT2BDbExMyluSYVrft09jJ3XZoEEfP_6GFP_53s7Xaz29J2q6NSSLHWvUDeOhLE75P0HVoM3XRTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: حزب‌الله قصد داشت با هزاران تروریست به جلیله حمله کند و همزمان با آن، قصد داشت شهرهای اسرائیل را با ۱۵۰ هزار موشک و راکت نابود کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/126316" target="_blank">📅 19:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126315">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f2c8a0c70.mp4?token=W8sAIIRR4ZADY-1cbFMUd8MKerhCKqOvsMFuElGnyC9cO3OI4XrE1evLToMpz8kih-YR_bK-q7L1PMWGSsspuYQLHLVuFjMpIDkQbzxNE-eO6glPPPvuVPg5Jr7Psuqbn7yX1SRClHs6gGJ5e435PXN40Az1tdITsiL8g0K3uwpNOYwKY6jZ2RsYuTH2r8OqctuHETyGL55nKA-Pbs51xlk_4yyhzZ9FCklUUdAKT49-9o10QoT7KKsC47N9oAm6G8JKj5TL4ISY4EmPevzB-faVEJY4PvAu3eQubI4e28V9yClEv3pzOK48Ny__MuDmqLiUhd9isBjn566yR9pMPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f2c8a0c70.mp4?token=W8sAIIRR4ZADY-1cbFMUd8MKerhCKqOvsMFuElGnyC9cO3OI4XrE1evLToMpz8kih-YR_bK-q7L1PMWGSsspuYQLHLVuFjMpIDkQbzxNE-eO6glPPPvuVPg5Jr7Psuqbn7yX1SRClHs6gGJ5e435PXN40Az1tdITsiL8g0K3uwpNOYwKY6jZ2RsYuTH2r8OqctuHETyGL55nKA-Pbs51xlk_4yyhzZ9FCklUUdAKT49-9o10QoT7KKsC47N9oAm6G8JKj5TL4ISY4EmPevzB-faVEJY4PvAu3eQubI4e28V9yClEv3pzOK48Ny__MuDmqLiUhd9isBjn566yR9pMPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از عد‌دویر، جنوب لبنان، پس از حمله هوایی اسرائیل.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/126315" target="_blank">📅 18:50 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126314">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6eJqoM3IZ2_8VfJ_dReFciPG5aHDthcURfMBzhy1FiGbC2tlzBfuBfi84VHfZzDfSSaed7pUMSFGo343NvOa72IBUXtKni4iVaPLRLeLOwlfRUTfXXfkUfKGMjYdQejMRvzH85fFhreISxunODRO72uydydNQoN7JLxdJAjFm689TD4Pyybi1WL03HEA3l_URWa6gmD26nQ4Ism4Y2EGXR2xI1HFRnEL0UzT9VUAV0O7vkUt9noRADjIAS4yns1_YYf-tF4-rTLp8qHp8a4MEsK8SidXrFgqxQGV9u-pH-DePsjPsgrnk1F2tt6V6cHk_epzWofTGnigF15dTYivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات شدید جبهه پایداری به قالیباف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/126314" target="_blank">📅 18:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126313">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
گروسی: هفته گذشته بازرسی معمول از نیروگاه بوشهر انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/126313" target="_blank">📅 18:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126312">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e941f5858.mp4?token=ol67n--4Z5kwSW_aPQGoTtjq4pBk1_hTbGcZ1puqZF6zo_cVgjO330t3iUV1XcO-rYXLklAu00RuyD1AWCXNnCWyfIqYWR0c6Hs74TcertfFv6pcxQ0WGaDr3X7tjFvy8jW8nXAjn2Ik2xVbKrwdT7uwIw9vjh1KzHRNCiOUTFBRf5FP6fbxTA3VrO8JRy0qN7PKE96SF2qmZ4RmTVVvQLiM4Rllhspz-uzeJ0mQBmx_FlBYk6XFUOUPEhVGe-MuXHsmLa6HzlwxPG9wXtjTUXMdLy62lBEKKAfCvXwwDqFRCH9taPPdkpPMm2SD6t6RzT55Wt59XtFSIoNeC6h5HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e941f5858.mp4?token=ol67n--4Z5kwSW_aPQGoTtjq4pBk1_hTbGcZ1puqZF6zo_cVgjO330t3iUV1XcO-rYXLklAu00RuyD1AWCXNnCWyfIqYWR0c6Hs74TcertfFv6pcxQ0WGaDr3X7tjFvy8jW8nXAjn2Ik2xVbKrwdT7uwIw9vjh1KzHRNCiOUTFBRf5FP6fbxTA3VrO8JRy0qN7PKE96SF2qmZ4RmTVVvQLiM4Rllhspz-uzeJ0mQBmx_FlBYk6XFUOUPEhVGe-MuXHsmLa6HzlwxPG9wXtjTUXMdLy62lBEKKAfCvXwwDqFRCH9taPPdkpPMm2SD6t6RzT55Wt59XtFSIoNeC6h5HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادامه حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/126312" target="_blank">📅 18:47 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126311">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
وزیر خارجه اسپانیا: هیچ راه‌حل نظامی‌ای برای تنش‌ها در غرب آسیا وجود ندارد
🔴
توسل دوباره به خشونت، رنج بیشتری را به همراه خواهد داشت
🔴
کاهش فوری تنش ضروری است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126311" target="_blank">📅 18:34 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126310">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a021092ea6.mp4?token=sCwOjkLiO3VOZm2xaYrgOYmZy3xwzV27_7f7dTdm5QG0-ldyPZiP0cQ1L-1te5DM0H-ZFwLROMxoQItEwEnKjw5ev05pEfONaopkzWqFS0FQixMFxwl26mhttLtgo06UM6Xn9HSJ03GrKrKwSykPtvEv6f9h0oJJXoL2sslLXufEXoCtBH-Vwq62r4IoodGGnzfFxRNFI8Hr6DjVCnsRVRbNnNvM9hlHrerNZYjjJfsemu4IPWaiUKPA0hyHq19sdHybDTFaAkr0lPEhTn4FUrRgci22k2UBICdBLxHfP9NnconHgwlogfVRl-f92jqKw_s9Wn6PApG7lALklk8nbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a021092ea6.mp4?token=sCwOjkLiO3VOZm2xaYrgOYmZy3xwzV27_7f7dTdm5QG0-ldyPZiP0cQ1L-1te5DM0H-ZFwLROMxoQItEwEnKjw5ev05pEfONaopkzWqFS0FQixMFxwl26mhttLtgo06UM6Xn9HSJ03GrKrKwSykPtvEv6f9h0oJJXoL2sslLXufEXoCtBH-Vwq62r4IoodGGnzfFxRNFI8Hr6DjVCnsRVRbNnNvM9hlHrerNZYjjJfsemu4IPWaiUKPA0hyHq19sdHybDTFaAkr0lPEhTn4FUrRgci22k2UBICdBLxHfP9NnconHgwlogfVRl-f92jqKw_s9Wn6PApG7lALklk8nbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوخت رسان‌های آمریکا تو فردوگاه بن گوریون اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/126310" target="_blank">📅 18:28 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126309">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
نتانیاهو ساعت ۱۸:۱۵ به وقت اسرائیل قراره یه بیانیه بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126309" target="_blank">📅 18:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126308">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlO1IhHb71IJFVqoxkx0rgU1JBvK8lf54w4CHHqOepPH6iSuD8LuQV-X661A1ncRp-Vn8BgzxfUUP27qGZ75Vl6jliFvpBH8Pkwp6xTKUIXsapCT3mGzb23TxujeB-_eUVgcUSOM-zpYfrZBLS6roHjkjI_zjWQG2t50ybaxiKpTqWyx0DVNHpA8lWlHTrYauIb1drfaICWLlbAjIzRFJIZ35oXu4fWFG08QWqQWCJ6vuaZkHeO7hMRgXkpsFRzHm9QqR0N7mkhkLYSqbVx09q3jgf4rPKNPcpLuj2X-1wVSfA4gdAvk-Siv83S8DO8lKLrZQcVIGL_J6Emgv6ktIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر دفاع اسرائیل کاتز: اسرائیل به طور قاطع تهدیدات ایران را رد می‌کند.
🔴
هر تلاش ایرانی برای پیوند دادن لبنان و ایران و حمله به اسرائیل با نیروی عظیمی مواجه خواهد شد، همانطور که دیروز اتفاق افتاد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/126308" target="_blank">📅 18:21 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126307">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-UTL3kDYNJX8UF4tBleItVL_e5e99EejftGMfjuNv3uzasbxJpBfSl0CGaFrevgLZQpCD7Vtc1K90MBoRMz2a8Vu1nxpJ-Gr2OQX-OfJHJsvK_rby39TecFyXiwf6wx7OprSXbrIr5o0Il8Yygsr_oNgh1Wa9Ti8A84uO29vwRDal8qOa1lPydqehsjZ6b79FeBHxau2EoBWv7zeQ9tmJc5y8GalrZBync6pRsoWm-hLyqoyMwaFy6OKQjNwqYRrTx9POQnaPYqvFD1y7XRbbT-Vm25DVUz53JkHvvmjDlzW-D9Xb-mMLThMyUzuCUroqahmLlVP3bYE7XSwlrcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف: معادلهٔ آتش‌‌بس روی کاغذ و نقض مکرر آن در میدان را برهم زدیم
🔴
تا زمانی که ارادهٔ واقعی برای اعتمادسازی نداشته باشید، پاسخ ایران همین خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126307" target="_blank">📅 18:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126306">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
فیلد مارشال ، محسن رضایی: ایران از غنی‌سازی کوتاه نمیاد و در موضوع آزاد کردن پول‌های بلوکه‌شده جدیه
🔴
اگه مذاکره نتیجه نده، محاصره دریایی رو تحمل نمیکنیم و اقدام نظامی انجام میدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/126306" target="_blank">📅 18:18 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126305">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=e0_KDaE_8LlV0OWu8nj4lXYAzyV9W0eXAtj0Zeg_EmVqCnEt0w7dVgl5szErVVYr-F48ga22wbobZSyzOlo3WOPJksSZf5OepdgqTq2w1JSSgznlZ9AoYI63pf8xx3PFOb4w5G2J91KZI4eAuIb1uYWZFMqmAIxlDclhYC1Hw8fLJSmCB54ck69HmR_GYnI5obY3J1PkmKRlquGfxuKQjRpYadChARdrhfSVNQZEPPGT5eaiCyGdFXQFkR1JF4WD4UaZc4uZq8ibgPYKaVlU_P1qGwrceCwei_EObZ2o-2uP3167o-szVk0n8idKgQHaRVxGu6RB1Qcmpq9yq7Yhfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=e0_KDaE_8LlV0OWu8nj4lXYAzyV9W0eXAtj0Zeg_EmVqCnEt0w7dVgl5szErVVYr-F48ga22wbobZSyzOlo3WOPJksSZf5OepdgqTq2w1JSSgznlZ9AoYI63pf8xx3PFOb4w5G2J91KZI4eAuIb1uYWZFMqmAIxlDclhYC1Hw8fLJSmCB54ck69HmR_GYnI5obY3J1PkmKRlquGfxuKQjRpYadChARdrhfSVNQZEPPGT5eaiCyGdFXQFkR1JF4WD4UaZc4uZq8ibgPYKaVlU_P1qGwrceCwei_EObZ2o-2uP3167o-szVk0n8idKgQHaRVxGu6RB1Qcmpq9yq7Yhfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در حال هدف قرار دادن یحمر الشقیف در جنوب لبنان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/126305" target="_blank">📅 18:15 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126304">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
خبرنگار الجزیره: آنچه ایران به دنبال آن است، تحمیل یک توافق آتش‌بس جامع در لبنان، در هر توافقی با واشنگتن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/126304" target="_blank">📅 18:11 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126303">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HR1Qy_dJxotpzTYYnsadNcZ2hDqMuLfGgU96RSkKYfFPPwtxD0GYopC_cwJM6wH_WBzBiB5H06gSbQGmpJCZ4EA8yo9OpAdVdCbAE6aT3wM_1BO5Z3l1DdXICMSAY40FhplggalfKJ11be7C6lFrH_zlDCvLFYs2pv8W_BBfwmo1QG0Qg6wgB7JsJ8AyRLBe76GyTS8zT9F2hf_xx3yTEV1E9-oH_Jkhs41XYKm_6sKEleVlxWB1YzEi2fOt5ImAa7654jHQHgykz4cvpTFxoqUKYkcuITErLq-fRLbZfYFJU-CUJKP3NpBvd5H25R-NU8u9ioe__ODIV_GxSf2D1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیر شورای عالی امنیت ملی: اگر ائتلاف شیطانی خطا کند، منطقه برایش جهنم خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/126303" target="_blank">📅 18:04 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126300">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IcHMEZ56NG8yyMTFeB-eQhxqFMl3Hp6BoDtUpz39k-qlOkw1KLNLsqusaJ-JawcpSHvJi1O5eJ460bUjG0-9c7yHCMu53UIylTq4OsucwAjtzAKMWw4W5vyRfYfabbsL0Git6TZtxpv-6fpXoPWASO5mLv_Cb58d1L5Nzd7MFpTWs64Zne8CNQBUHwn8Eyw3IPe0ttamUWaJKJv9kRiO_Q5cUshM3CmJU7c7xtJ2M2GGYe4FIuYNEW1pUFjFdx8CEHCGJToFqU8cCAuMTPVQh4or1j70VzKXMcx134E3ZpeU8lXbrZpQPvR1d2Dh75KNrAHIBBJMoB4KxWaEGH7xsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEsXf-c7OpFXWgduoXVsKA-i8Ee1Ux_T6uA98hLj7CLqUrLEEXmhlcd8sH-uEm8fduSuz3emmp4B0tsnkYKtzZpw1Oz2cY7or-DFTf9XYZcyZiZauJw8MXlEl-AsXvNkh1ortB6doOcOEMGMP-wph7dtSRETLwUCY35hjbDQdgFdJc1epxv8i1Lahn9W0QzX9y1-dHX_OkcHmCMVMQKciHt8A6JWWuW0L0kupxxwJKRGkoEVSP23tnY6ty0BTvjN8BjEp6uSgWdDrT441oL-Tjrlni2T1ieZ3ywaAopdUik3vPVzHCJWEPKGzqRqJi9nopc9DjCQw_NBL7S9-9wh8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d52e06eb0.mp4?token=IHgZdK7H9NyNXtsu4IvhQ7PaV4NpdJHFsExKJ-9JhWeVsC8YBEQ0MBwJFQf8VgE8sCS8JqAAkEb638KViXhsN9FO3_d5geOhsfntWtZ_93asYQUHhucWwl3_nwesU1O_DG5FSU41EWdzljsuzlYyUVE23o8IHYmPFHRWM3_P4SIpdxsQ2ZrgvQsxGgPQHpV8jrFtrhYOESu7JytIYkuByrIkGSu70wzUuAZQ2kF-xtitbV3h6CTj7-xgLW8Md7zt_T-pMeowLkORnJan68zo9sDMmEH3dpngQPFkmdIf7JxgtxCxKforBXjFzLdq04yhmBwe2-bswr04inbmcoBevA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d52e06eb0.mp4?token=IHgZdK7H9NyNXtsu4IvhQ7PaV4NpdJHFsExKJ-9JhWeVsC8YBEQ0MBwJFQf8VgE8sCS8JqAAkEb638KViXhsN9FO3_d5geOhsfntWtZ_93asYQUHhucWwl3_nwesU1O_DG5FSU41EWdzljsuzlYyUVE23o8IHYmPFHRWM3_P4SIpdxsQ2ZrgvQsxGgPQHpV8jrFtrhYOESu7JytIYkuByrIkGSu70wzUuAZQ2kF-xtitbV3h6CTj7-xgLW8Md7zt_T-pMeowLkORnJan68zo9sDMmEH3dpngQPFkmdIf7JxgtxCxKforBXjFzLdq04yhmBwe2-bswr04inbmcoBevA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله پهپادی اسرائیلی خودرویی را در نزدیکی مرکز صلیب سرخ لبنان در ورودی جنوبی صور، جنوب لبنان هدف قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/126300" target="_blank">📅 18:01 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126299">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
شهباز شریف: هدف نهایی صلح نزدیک است/همه طرف‌ها خویشتنداری کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/126299" target="_blank">📅 17:48 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126298">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل گزارش داد که ترامپ و نتانیاهو دقایقی پیش تلفنی صحبت کردند و حملات به ایران و جنوب لبنان بزودی به صورت کامل قطع خواهد شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/126298" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126296">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXt_ozcNmB0-NTLxI6UIoXLl3aawzPlTjuquCVD2Y7tUeS1txIOM9RRY-EkQpq-3fxdamiHsrMFsegUsFd1IrGTtRWjReulvrIgnduGOmFEysaCU0P3uVxJgWDazECQetgCT-F_OOP9YYhNSCtAo4m8WNGa5dR-NPmvjErRwHKzcCdiVQu5L9wNgMGar0cYhKLJhHKZEzlCsRJ1rJrzQ-ubtw79RvhRoea0Efgkb12g2TsO-u6vc9lcA2S03ahOvlhLq2GlC96BxhElarFfcIwEaGFxJKPO9T_jEp2_GFBqilOLdIKyNhMHD1TyU7W-pnF4GmW9WGlzmgIHf7tW0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=eyCwHwsn87PRyp0SkA6G153FqVttVXLUpTvJpiFoCPtTd5g9Li-1Kt9aII1AE4C_VpfryGCj5NjX6_IGu3K0coQ2z6HYj6UsXJ6v9ilESLhMt4vvMQXb7-Wf5V4knKdpK8W27DipPlsm3gJpzTuOpUVDK6up3PzUuOL4kDNbCoolMOsjgiEIzxIEAWVKPwkSZ6hgNJcho9ybgwWpxqPK_BwpWcjAQ_3yRnm9RkJUSZncflri5U8_HuCbHYuBbs1dnJPr95osYArab21YymHIUz9J4bzfLHqiH4nIQZyDUjybAKsRCwhIWIzdYzZR9yLxroLpZe_kLXvrKqddLCMrxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb17efda63.mp4?token=eyCwHwsn87PRyp0SkA6G153FqVttVXLUpTvJpiFoCPtTd5g9Li-1Kt9aII1AE4C_VpfryGCj5NjX6_IGu3K0coQ2z6HYj6UsXJ6v9ilESLhMt4vvMQXb7-Wf5V4knKdpK8W27DipPlsm3gJpzTuOpUVDK6up3PzUuOL4kDNbCoolMOsjgiEIzxIEAWVKPwkSZ6hgNJcho9ybgwWpxqPK_BwpWcjAQ_3yRnm9RkJUSZncflri5U8_HuCbHYuBbs1dnJPr95osYArab21YymHIUz9J4bzfLHqiH4nIQZyDUjybAKsRCwhIWIzdYzZR9yLxroLpZe_kLXvrKqddLCMrxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای اسرائیلی در حال هدف قرار دادن یحمر الشقیف در جنوب لبنان هستند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/126296" target="_blank">📅 17:37 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126295">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وزارت دفاع عربستان سعودی: آنچه درباره هدف قرار گرفتن پایگاه الأمير سلطان در الخرج منتشر شده است، «صحیح نیست»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/126295" target="_blank">📅 17:29 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126294">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
فوری/ایران اطلاع داده است که در صورت ادامه حمله اسرائیل به جنوب لبنان، حملات موشکی خود به اسرائیل را آغاز خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/126294" target="_blank">📅 17:26 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126293">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سی‌ان‌ان به نقل از یک مقام آمریکایی: ادعای اسرائیل مبنی بر اینکه آمریکا موشک‌های بالستیک ایرانی شلیک‌شده به سمت اسرائیل را رهگیری کرده، صحت ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/126293" target="_blank">📅 17:25 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126292">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
روزنامه هاآرتص به نقل از یک منبع اسرائیلی نوشت: نتانیاهو عصر امروز در جلسه کابینه امنیتی در مورد تشدید تنش با ایران تصمیم خواهد گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/126292" target="_blank">📅 17:24 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126291">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b75c4ec36b.mp4?token=aBLSsyEHwmFxkiYXBOhS_1hfdNBsWPHEce4QW6huqw4QA2Nd-lnlcwRsfIIU0hJhLtC-o04zdgh24CHtJpaRYS4nxVnPZA5WufsePpqWBkWL1iujIhsTYWrrkcW5wH_jth5se-58NdZwt2cDXy75hY2Gbvy7WUPC33LdaSgqZI2TKjZSnqqMl3BJxV-TXx0Ir9NQxusFd2UwisgkKhg0QKTX5j35HpsegwO7RVX1CHiqV28Njol78Ja408eZ9QLMlT_zY8t4qgTA1fGdsl7ZWhcxsKVA-kvftp-UrA2hL9zuagBQkCcvEswiN_7fAF8BrK3d4_c2J6gTaN1topQ0Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b75c4ec36b.mp4?token=aBLSsyEHwmFxkiYXBOhS_1hfdNBsWPHEce4QW6huqw4QA2Nd-lnlcwRsfIIU0hJhLtC-o04zdgh24CHtJpaRYS4nxVnPZA5WufsePpqWBkWL1iujIhsTYWrrkcW5wH_jth5se-58NdZwt2cDXy75hY2Gbvy7WUPC33LdaSgqZI2TKjZSnqqMl3BJxV-TXx0Ir9NQxusFd2UwisgkKhg0QKTX5j35HpsegwO7RVX1CHiqV28Njol78Ja408eZ9QLMlT_zY8t4qgTA1fGdsl7ZWhcxsKVA-kvftp-UrA2hL9zuagBQkCcvEswiN_7fAF8BrK3d4_c2J6gTaN1topQ0Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کالاس از اتحادیه اروپا درباره مفهوم ارتش اروپایی: چرا من از ارتش اضافی حمایت نمی‌کنم: هر کشور عضو یک ارتش دارد.
🔴
اگر این ارتش را به ناتو اختصاص دهید، دیگر نمی‌توانید از آن در جای دیگری استفاده کنید — همچنین نمی‌توانید ارتش دیگری ایجاد کنید، فقط یک ارتش موازی.
🔴
خیلی مهم است که ساختارهایی ایجاد نکنیم که ممکن است باعث سردرگمی شوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/126291" target="_blank">📅 17:20 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-126290">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c5fd0563f.mp4?token=KtG9r-0jlAkVCQLWX84LJd2MnSTiR3dw4WKfnh7uyo77FvZ67JBzdWFWzTBeIa9XZUNzloHjbk5bYhqtJSe7LtXQAhB7C9dfL_mfdJwdVDMgyEoqJxj-N4hNJdGw527RlC6HDh_Ww3Um7YmZc91uduNkpJeFs515_iF2o85uzBmYh_Li25j58sh8JCZQ3dB0DsmxVEFeHkdh_g-Yq-CEnOPKR_FkLKsazNOxVlE6MFG2C0C0UnicvKDLAJRw7iGTXX_TOAe8AeyFGUa6qZHr6LfLIdnqX1asN97U8xMJ1jX7tnO_haj39QL-GZdXMj5OLiqLX6tp61mJLuTYGYX54w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c5fd0563f.mp4?token=KtG9r-0jlAkVCQLWX84LJd2MnSTiR3dw4WKfnh7uyo77FvZ67JBzdWFWzTBeIa9XZUNzloHjbk5bYhqtJSe7LtXQAhB7C9dfL_mfdJwdVDMgyEoqJxj-N4hNJdGw527RlC6HDh_Ww3Um7YmZc91uduNkpJeFs515_iF2o85uzBmYh_Li25j58sh8JCZQ3dB0DsmxVEFeHkdh_g-Yq-CEnOPKR_FkLKsazNOxVlE6MFG2C0C0UnicvKDLAJRw7iGTXX_TOAe8AeyFGUa6qZHr6LfLIdnqX1asN97U8xMJ1jX7tnO_haj39QL-GZdXMj5OLiqLX6tp61mJLuTYGYX54w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپاد شاهد-۱۳۶ مواضع گروه‌های کرد مخالف ایران در شمال عراق را هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/126290" target="_blank">📅 17:16 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
