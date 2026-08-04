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
<img src="https://cdn4.telesco.pe/file/Gu6Hu8AZdNVofx05Txp8WwpBA64Cn9EFg5tLfgP0N0c3ax_GJB-AMqRCTP9z2dE6zHFZ2G967S6hC68ebaLE0Je1AeToMZQunVlXYCpRuEFBNjHxRX1nY_hMyQ3BxpXiOGGoCc16z6kkEBMSFQU0_cfhmN4yb4Udr8xcZkv-Sgu9Qpa-kDN_nXL64CggiqXamFIHkYdWYOzAsE9U4gZ8ppgquGCSsg-VKLoa3UsWaiaM6FM3SZfdKXw-mtDAEA52LODWnwthZxiqho1EjUTeupJxXlqdEXnhE-U2ZeVFxVttKSG8zPvCPLuEwNvGcsiY_b1TM-_8FLURzgyTSH0y6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 135K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 12:47:33</div>
<hr>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=BqD7fjJVbxIXL1yDcnjNomvl7o0DzHi6j6meAoXmhWq6gZt0EDoWCFzb6rlTYq0waqs4TORqrCeysBYpnIU5Z56-gjCaZpvBg83zEFmpkgwMW-GMWJ7ZMa0OWzgS0B7BSj_Q7HOxq5l60FzpLuPH8lz0lQE5jA181NZWq7O9gT_JAarvN6udfGeQBiANWtd6gFmW8ZiJVoh0H1xK9OfotMyqYpCV-xYmHSm00qIMHHsVycBVbG77wm_IzRicmg_4iib5P3URohs7i_6mvPZyXrG9DfRh7Rswk1NfkkwCO9CQx4QXvM5rInFcsZ2E2DbmtC93UIFvw23fBZ5bqpYfkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=BqD7fjJVbxIXL1yDcnjNomvl7o0DzHi6j6meAoXmhWq6gZt0EDoWCFzb6rlTYq0waqs4TORqrCeysBYpnIU5Z56-gjCaZpvBg83zEFmpkgwMW-GMWJ7ZMa0OWzgS0B7BSj_Q7HOxq5l60FzpLuPH8lz0lQE5jA181NZWq7O9gT_JAarvN6udfGeQBiANWtd6gFmW8ZiJVoh0H1xK9OfotMyqYpCV-xYmHSm00qIMHHsVycBVbG77wm_IzRicmg_4iib5P3URohs7i_6mvPZyXrG9DfRh7Rswk1NfkkwCO9CQx4QXvM5rInFcsZ2E2DbmtC93UIFvw23fBZ5bqpYfkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=WRo13lpnP820ozHwxQhZorBz7P9RH3bM3OqdbrEYqWbO3twr3mLfv4ju4uYImchCsYTgqUfWklmlAzybkp2boDdMQlGrIfcWuqvbgQH3oHvngr5oIOzNhPZrb8amQc986DKtcEdKiGAlPQVs62guw8wfMuRUShkwO63faKYgyv4Hu1Kd4ngbqcgqg8zx1bUF65GngDi2EZ8clWR0al4xSNhrXHbSZbaryRRuXC1d94fVEfQcI3r92WMAL_cWYAG37ebL97h7tij_KXLaoo75BcW9oRZpysn770ONdF_dEDnZiSLWSpnrbU5PIisjr1zpChncC18zpnwQ_CEXhl9SxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=WRo13lpnP820ozHwxQhZorBz7P9RH3bM3OqdbrEYqWbO3twr3mLfv4ju4uYImchCsYTgqUfWklmlAzybkp2boDdMQlGrIfcWuqvbgQH3oHvngr5oIOzNhPZrb8amQc986DKtcEdKiGAlPQVs62guw8wfMuRUShkwO63faKYgyv4Hu1Kd4ngbqcgqg8zx1bUF65GngDi2EZ8clWR0al4xSNhrXHbSZbaryRRuXC1d94fVEfQcI3r92WMAL_cWYAG37ebL97h7tij_KXLaoo75BcW9oRZpysn770ONdF_dEDnZiSLWSpnrbU5PIisjr1zpChncC18zpnwQ_CEXhl9SxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69507">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">⏸
مستند از شب های تهران قدیم که در دهه ۵۰  تهیه شده:
@News_Hut</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/news_hut/69507" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69506">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuworvOLOqMd0dFQeiQk5DYDSa8C6VWrsAm3_AF6q-h5pQdLdvg3lGQgkO0K2KK191jwY0wDnpZDrU_pRJJ_HbsxRkcDWXvsWLPbhOT_3ndJz1Or2_SE6UtDrmfq1objqc9jQ97s4Ny6aQLkcmT0HIJ2WXH43PGMz9NsReGL9D8ia_GNtWPq5jIqbVz0S0BfKvb5b95tnS8Pd1173trSRi5ZC4FNnula_OfZtN21weT9URI1ap52_8YCnczo1RFttk7P_BweYlJo7qbkmwW5k0h_pINxMglP5WNHC-jsh6hrnaJd2wPu6ns0532H1aOQu8ImRZftP5jKCR0d2dy583Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ccf6718b8f.mp4?token=aryaA_A1iekXv4Ke9s9auFe7Q5efjnOnHRujUrxM5NKXufZHFKZACqXpl7xWLU7idYAp3PiAlfOlADHURsH58STmLfyeP2-7x9B0EeFe2hj-ZNM32PCE5Gm23f9LrZ-m9_KJrBg8KHjTQBTW73F6Xr9zcb190QH_2tn7JRgsbktmVwXNGG618jVnr72D9UME9b-4UJZ-TXFmjiJSeKf5qdOdCx6w5gtjuvnYTzigYzSJKJHf4GiRYS_5yqtaot2tyK4eeidmXji04LQTJ4g3UWYEbRtKbprQlASMFLB_FtGwoO9AuprcZIqwQn790WYNjDVUAQ3huINWiLsYs8xXuworvOLOqMd0dFQeiQk5DYDSa8C6VWrsAm3_AF6q-h5pQdLdvg3lGQgkO0K2KK191jwY0wDnpZDrU_pRJJ_HbsxRkcDWXvsWLPbhOT_3ndJz1Or2_SE6UtDrmfq1objqc9jQ97s4Ny6aQLkcmT0HIJ2WXH43PGMz9NsReGL9D8ia_GNtWPq5jIqbVz0S0BfKvb5b95tnS8Pd1173trSRi5ZC4FNnula_OfZtN21weT9URI1ap52_8YCnczo1RFttk7P_BweYlJo7qbkmwW5k0h_pINxMglP5WNHC-jsh6hrnaJd2wPu6ns0532H1aOQu8ImRZftP5jKCR0d2dy583Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بخش‌هایی از گفتگوی ترامپ با خبرنگاران درباره ایران به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/69506" target="_blank">📅 10:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69505">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=Hx812geP1WCzjwPutU1MmSZ23AUHYJEy0elJAGSzvt_lpsaebeOTnQJqUDfHfHu0Af6k24CN85kuHpvp151gn6cMdvPwmiPpbvZJFCG4IqJQ3DaewDS1_WN-3JziZrKmerO6JrJ-Eoa5flTxYwjtHeNgCITvT4QkfT2qQWcy2ghfqv4pue_icOUug3OsRaem5PUia0CKz_TdmmprVzicjOl0Y2mV8nYtpmxVUDR8TR2KLuv3KfSEnQRiE44UC574VrD6WJV__yayN_m9-64jXgr-tASlhs_rFRFBZ8CLc2GKBgmJSfzCKvIseOS3iPChdywLZzFAxntua5GXw_pHN4m27ofYwXxqQFz56CJu6woAXV5nBc7AIpkMURPRBdeD2SfiKT1YWXLQ1OiPhHAwJaQv66UWFP_YkX68RjOBQ0fTcdS1FggPUD-IN5D__9LRXBS0ki6wGcOrAqysu-GN-yGHEjXpObhhR35X8jGHRYz8cXDzg3h8-xd5fQ98y69o-JedEX0mdDU7gep4yPuQRl8oXxe7bJlUto92LL9R2-DcyCfJ6pyuRWHrGly0wd0J_1nuDX7_6sGLRjUcNJSj3ldM_D6hWgAWt3DeO1a67tnfqhN2iVowU9QDFxJUXE5G9-J5HL_s6wJ3nnxOZaw6VClYAVi8KBAuzCcLzgHQm0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca6498e72.mp4?token=Hx812geP1WCzjwPutU1MmSZ23AUHYJEy0elJAGSzvt_lpsaebeOTnQJqUDfHfHu0Af6k24CN85kuHpvp151gn6cMdvPwmiPpbvZJFCG4IqJQ3DaewDS1_WN-3JziZrKmerO6JrJ-Eoa5flTxYwjtHeNgCITvT4QkfT2qQWcy2ghfqv4pue_icOUug3OsRaem5PUia0CKz_TdmmprVzicjOl0Y2mV8nYtpmxVUDR8TR2KLuv3KfSEnQRiE44UC574VrD6WJV__yayN_m9-64jXgr-tASlhs_rFRFBZ8CLc2GKBgmJSfzCKvIseOS3iPChdywLZzFAxntua5GXw_pHN4m27ofYwXxqQFz56CJu6woAXV5nBc7AIpkMURPRBdeD2SfiKT1YWXLQ1OiPhHAwJaQv66UWFP_YkX68RjOBQ0fTcdS1FggPUD-IN5D__9LRXBS0ki6wGcOrAqysu-GN-yGHEjXpObhhR35X8jGHRYz8cXDzg3h8-xd5fQ98y69o-JedEX0mdDU7gep4yPuQRl8oXxe7bJlUto92LL9R2-DcyCfJ6pyuRWHrGly0wd0J_1nuDX7_6sGLRjUcNJSj3ldM_D6hWgAWt3DeO1a67tnfqhN2iVowU9QDFxJUXE5G9-J5HL_s6wJ3nnxOZaw6VClYAVi8KBAuzCcLzgHQm0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
مستند جزیره خارک(1345):
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69505" target="_blank">📅 10:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69504">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=mgML7miN9GNGXssr5dO03DuEiwnMQGaX5n6Vg-kK1s92qnCWMNls-8cgA8vDpzUACiEl5292vQpxuWTe9oBCEgjfzpzz5FYXSNsXY-h9h-NhXDv2ITX359FE3RazesaVRTuBjcPD4WAmOivChJnt_E4sEiyKrLS6GF97teTUPL7_7uAK7NchvpsgZYgRXxNOUgWKaYN-zneoHTSqvV4l_n01vDvSIhyag4vngC4CZ6bcwFoP1irDUt4fFdDTHaNKWudkNeMnwLKMb4OrnHG910eYRlKzO0g4K6Bz4qATfAgulaTHciU9_NBESvcP90HAlLPlLH8HKkDw0fuW0v92aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb81b5812.mp4?token=mgML7miN9GNGXssr5dO03DuEiwnMQGaX5n6Vg-kK1s92qnCWMNls-8cgA8vDpzUACiEl5292vQpxuWTe9oBCEgjfzpzz5FYXSNsXY-h9h-NhXDv2ITX359FE3RazesaVRTuBjcPD4WAmOivChJnt_E4sEiyKrLS6GF97teTUPL7_7uAK7NchvpsgZYgRXxNOUgWKaYN-zneoHTSqvV4l_n01vDvSIhyag4vngC4CZ6bcwFoP1irDUt4fFdDTHaNKWudkNeMnwLKMb4OrnHG910eYRlKzO0g4K6Bz4qATfAgulaTHciU9_NBESvcP90HAlLPlLH8HKkDw0fuW0v92aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭕️
محمد باقر خرازی:
اگه پزشکیان یک بار دیگه استعفا بده، مجتبی خامنه‌ای موافقت می‌کنه
.
مسعود پزشکیان تا حالا نزدیک به 28 بار یا استعفا داده یا تهدید به استعفا کرده!
قراره ذوالقدر رو از دبیرکلی شورای عالی امنیت ملی دربیاره و محسن رضایی رو جاش بذاره.
مجتبی به عراقچی هم گفته دیگه به هیچ عنوان حق دخالت تو مذاکرات رو نداری.
همه اینا همیشه تهدید به استعفا میکردن ولی از وقتی مجتبی خامنه‌ای تهدید کرده، دیگه فیتیله‌ها رو پایین کشیدن.
ماشالله مجتبی خامنه‌ای خیلی سفت و بی‌تعارفه ، پدرش یکم تعارف داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/69504" target="_blank">📅 09:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69503">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhHt44KzSIpdvltLOfn0tp1otk3DRgYapxP2BiO4Z77mymxYd_5mxL4lkxRhOEeSLpwzAVbG0IFfVsOzzRBmOwlNUMwM7YlO6w0rjb2q2Vcs2qywg73IWv5St-IK7mqG_Pb4qY6yH9U1fCrqFmSxGlXaoroARCCYcuk8eiy_H96jdpYaY0WUzlHL6ujLX5F5z_Gf-fOV8VnkBRMogzr23V_mV228PKwf1bHp7Pn5EMQfbtDwOS6Ihh-vX8JnV-4E1a2tj77RwCcdjZchvn-bfZXrkbY6fndjpb-RFn0pdqdxO4HXCbniNuAeQR_Iq_9WTyTVG2TkPKboExmZMwAhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
یک کشتی باری در فاصله ۲۰ مایل دریایی شمال شرقی «الخصب» عمان، از طریق کانال ۱۶ VHF پیام اضطراری مخابره کرده و مدعی شده است که مورد اصابت یک پرتابه قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69503" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69502">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
🚨
رسانه های حکومت از حمله به یک پایگاه آمریکایی در شمال کویت خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69502" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69501">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db881c0183.mp4?token=n0IUl9Ite1h7pCzmgQFWcLgHL-7p3rfAcec5v8GBOXj37aarwOWgITBw_YMEO_viCb3MYc3bdH3-wE-CAtnucBz0zd8cas56dJpUKKDXFzSEY912dQbrriHSZjO939IVFaQ9Z7nB6ypq4lIIz6jyj9eVznt_uzQd8h_ODhvUHgoIELco9Ree_4waF1hHnOToeMkxueEACfK3JVwIZgcaYAdwgs8ji-heyL7jeaMY3fJMh27mRKoay2KnMPHAm146jZf321BTHSh2c7Vdpr4TltVtk7URIu1wfhyCOgunEnUzWW93BpNglKUlCgp5ROtOs72rKL1IgA5f9jVXi0MrvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db881c0183.mp4?token=n0IUl9Ite1h7pCzmgQFWcLgHL-7p3rfAcec5v8GBOXj37aarwOWgITBw_YMEO_viCb3MYc3bdH3-wE-CAtnucBz0zd8cas56dJpUKKDXFzSEY912dQbrriHSZjO939IVFaQ9Z7nB6ypq4lIIz6jyj9eVznt_uzQd8h_ODhvUHgoIELco9Ree_4waF1hHnOToeMkxueEACfK3JVwIZgcaYAdwgs8ji-heyL7jeaMY3fJMh27mRKoay2KnMPHAm146jZf321BTHSh2c7Vdpr4TltVtk7URIu1wfhyCOgunEnUzWW93BpNglKUlCgp5ROtOs72rKL1IgA5f9jVXi0MrvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69501" target="_blank">📅 02:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69500">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
منابع عربی:
شنیده شدن صدای انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69500" target="_blank">📅 02:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69496">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r17Kqm6vYEHx43R6WXon7Vm3p5QAm5osoyeD0O6WTEkn9I2X3g9ZSrk1lnzRuro4BHXr3uY_HizA4Tie8wva9UdruT5t0Wl7fSPefbR-lcELIpkEohhvjaKjw4xs1dEMslilRdmVt5hhDvRbh0wldYS1SRAmOmnT81hCYQY4B7ToP77_44x-IAMLfaPBn2wezz5ZZiyFhTOao0HDqVRRVWYIO6IxIYEKIh4NcCBmA9xI-xx8yc_EQ-1CK5NTQngw2WJUKpuhkuLZiMg8E7p6Hh7djgKhaNMTFJycAmKuvWML9MX0wOWCvAdH_2BVE1H0fiXEbciaWxb9weLITSYJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=o46V5AxinO90jERJ6Yn2-BH4xAcobf3auSWPW44v8KXZmON59tCZl_VJsSB96yf_n-DgB88moHvd3mU8VoDKXnVZ_14CMrCEzwdZnmpqlE3hvVBqVxUP5nls8ThqWPfTffHCeeVujK14L7Bwt914eMgmdCK-7sOHwafom8bvPcEgmv-6bfbiHm2lKvgyZp7v5QmicQF72mzLIQQfEaZ5yJJir6OcoVilaNKSnM48CyH_tyAqPujucxgtKhZhcX1257HCV1L5NU_P0NWBhOqPNEnMA72PyTkCdRF_x25jOH29fbPsKCx-jdrwYRzJcft55Z1obsWpk6EKVTWfkC2_mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967a0aa4e1.mp4?token=o46V5AxinO90jERJ6Yn2-BH4xAcobf3auSWPW44v8KXZmON59tCZl_VJsSB96yf_n-DgB88moHvd3mU8VoDKXnVZ_14CMrCEzwdZnmpqlE3hvVBqVxUP5nls8ThqWPfTffHCeeVujK14L7Bwt914eMgmdCK-7sOHwafom8bvPcEgmv-6bfbiHm2lKvgyZp7v5QmicQF72mzLIQQfEaZ5yJJir6OcoVilaNKSnM48CyH_tyAqPujucxgtKhZhcX1257HCV1L5NU_P0NWBhOqPNEnMA72PyTkCdRF_x25jOH29fbPsKCx-jdrwYRzJcft55Z1obsWpk6EKVTWfkC2_mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقای سیاه‌پوستی که تو تصویر می‌بینید، رکورد ویوهای تیک‌تاک رو جابه‌جا کرده
👀
حالا کارش چیه؟ میره به شهرها و کشورهای مختلف و دخترها، زن‌ها و دوست‌دخترهای مردم رو بلند می‌کنه و باهاشون مثل دمبل وزنه می‌زنه!
جالب‌تر اینکه تو بعضی جاها، دخترا حتی صف می‌کشن تا نوبتشون بشه که ایشون بلندشون کنه
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69496" target="_blank">📅 01:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69495">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b93335655.mp4?token=LkZvQR5t7z7LC23GN5cnTio_DUJGnYQ99C_duoIxHN_3l1t-FHf_t3a7BYwpjIbyYTw7GHCZx4CyyXFdoSwuL9qJ_b_I-6pux9tduAAuwpjAtHkZYbFDv4JVztPqAw2Vg0fQJNWKs9qpRpJ-fKB1vRLVAsoj4d9P-Aqh_VoJYRins2vVThGrtJ-lTck5kiXENWGWGtcedbWVTmZrjWORGN9bh6K5v-DioBwQXtD0qdzgPvS2W3WIo12JSQktp0EErBq9OC9O1WWmNzzZmnRkoJW6DwLTI1r6A-IPlWr8g_2GZP_ZK3LEvP3uDcK8iOT3pPpCec_2ir_PqpOQIqTOIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b93335655.mp4?token=LkZvQR5t7z7LC23GN5cnTio_DUJGnYQ99C_duoIxHN_3l1t-FHf_t3a7BYwpjIbyYTw7GHCZx4CyyXFdoSwuL9qJ_b_I-6pux9tduAAuwpjAtHkZYbFDv4JVztPqAw2Vg0fQJNWKs9qpRpJ-fKB1vRLVAsoj4d9P-Aqh_VoJYRins2vVThGrtJ-lTck5kiXENWGWGtcedbWVTmZrjWORGN9bh6K5v-DioBwQXtD0qdzgPvS2W3WIo12JSQktp0EErBq9OC9O1WWmNzzZmnRkoJW6DwLTI1r6A-IPlWr8g_2GZP_ZK3LEvP3uDcK8iOT3pPpCec_2ir_PqpOQIqTOIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دست فرمون پشم ریزون اوپراتور اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69495" target="_blank">📅 00:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69494">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLlEXUYjiMoybAJ9kVcPM6ERHkPR9NyX0jxRoabFJX_ZCWBHFu7IaecVtcaFsEfVRZz_4J3WFgk61YQAe4d2Y5c0iQnYfC3ucRywzGWVo2Tp7u552Wb29vB59Enl8nC6gJU7bEF-EgBfnly5cj4tn0VGN_uNV7Y9fKZ9RzFfsPB4RteBI4MpPaK21-ZGspzcEjdBBBpSWsY4KnirWM82odDrNN7q-YgsZJlVTCVchEp34j27zrWuk7dLaX6Wiw4Jr0FOLZFYRjDhz91CSgkwEwVwcoiID7YpS4J0A_DFIP1vMkhfUt4xjk-fVNYMn_uCc3EpQmqWUipkreS4xdyf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرندی:
ایران هیچ‌گونه قصدی برای مذاکره با رژیم ترامپ ندارد. هرگونه اقدام تجاوزکارانه با پاسخی کوبنده و قاطع از سوی جمهوری اسلامی مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69494" target="_blank">📅 00:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69493">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=HZA_c7SGuEYO4wRSjuAhq7Z79tAr5eMQvvTWaa87K_ks5nGttQICHfdSt9kvPwLc_K3Ss9hwRIvdu6yLyc9LFFQscza6OB4i-Ue_1m97xcEld9OOC7pfSDFanDywOSHvOqJAfDUrgcJD1_4WEljxhDII06bgiC2li9SxMtJhlSp5xDVPSjOF_qAvZfDYvOT7JAtCm_8uebkx-C5kCfWEYNx4jY6ieHRCBE_V3tYENRWEhcCphgcR-fUgaCYs9sxmnLYGocYc1gkVwD3anfPuxXN9CIzC0dr3gEpXUJz4wwPq90spvFSVnBtmlX42lioKDfFAz-9AIAf_eHOj12-Bcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffffb49aab.mp4?token=HZA_c7SGuEYO4wRSjuAhq7Z79tAr5eMQvvTWaa87K_ks5nGttQICHfdSt9kvPwLc_K3Ss9hwRIvdu6yLyc9LFFQscza6OB4i-Ue_1m97xcEld9OOC7pfSDFanDywOSHvOqJAfDUrgcJD1_4WEljxhDII06bgiC2li9SxMtJhlSp5xDVPSjOF_qAvZfDYvOT7JAtCm_8uebkx-C5kCfWEYNx4jY6ieHRCBE_V3tYENRWEhcCphgcR-fUgaCYs9sxmnLYGocYc1gkVwD3anfPuxXN9CIzC0dr3gEpXUJz4wwPq90spvFSVnBtmlX42lioKDfFAz-9AIAf_eHOj12-Bcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی:
آماده بودیم به ۳ نقطه از اوکراین حمله بکنیم ولی عذر خواهی کردن کنسل شد
پل های منتهی به هرمزگان رو آمریکا میزد که حمله زمینی بکنه ولی خب طرح هاشون ناپخته بود
تو ۱۷ روز با حملات شدید موشکی پهپادی ترامپ رو مجبور به شکست کردیم
آتش بسی وجود نداره داریم حملات معقولی انجام میدیم
تفاهم‌نامه با موافقت رهبری امضا شد
کویت رو ویران کردیم و فرماندهی سنتکام از قطر به اسرائیل منتقل شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69493" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69492">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571743cf02.mp4?token=N2yNQpps9ySjqZmE_HEwIgryzMxSOOqr1sg96oxzkh32FASImaRAhjjy6Z_zk-PchvgEoLii4E1WlWqGj_bRd48eKxigQ64mE0KhhoPlm2jvhpICrseQkEOtdALkpQ7SHoDmceetRjUokcqGQHvjolL5YOTq_DPyEzTMmBtaXvLjhA29b1o-xMjH_ujz6b401gNIuTy015oFtzuvu1iVW8gXL2dW-cFiAf6ZwKjCxfpVQLPvA77OlKIHP-imbPdJf-iHCN-iNxM57VLtQ0B7wHq1db8e3JGIFRgBJFvaH4nvsbKGg26e_78W-ks0KuxzpGdPIg_t4wNQlKNpxXsLXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571743cf02.mp4?token=N2yNQpps9ySjqZmE_HEwIgryzMxSOOqr1sg96oxzkh32FASImaRAhjjy6Z_zk-PchvgEoLii4E1WlWqGj_bRd48eKxigQ64mE0KhhoPlm2jvhpICrseQkEOtdALkpQ7SHoDmceetRjUokcqGQHvjolL5YOTq_DPyEzTMmBtaXvLjhA29b1o-xMjH_ujz6b401gNIuTy015oFtzuvu1iVW8gXL2dW-cFiAf6ZwKjCxfpVQLPvA77OlKIHP-imbPdJf-iHCN-iNxM57VLtQ0B7wHq1db8e3JGIFRgBJFvaH4nvsbKGg26e_78W-ks0KuxzpGdPIg_t4wNQlKNpxXsLXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی وایرال شده از موکب خدمه ام‌البنین که به زائرا آیفون ۱۷ و آیپد و گوشواره طلا میدن!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69492" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69491">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدنیاکالا- کفش ویتنام و اروپا در بانه</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGCq-z4RZJ5MDFQ6SyZkhj4ZfD2xfLTpCrDKFAr7vt6Vy_3BWzkY0MWMXD_A_lZbseFVMz9PmTAWYkqNR9LJUV63_aWV7R8b49lMhMBf4ISbdEyAVwOjoJIj0uHe2OHivSdPCC_YMuD4_YVIq_NdBPjzoXCNLldHtc9k-iZ4fxIlCoA1KNykoU4AccObMV-oVJHQDiM9vnSwBOhuGUNXEnExXDQvRFPdL1kKsmL5idelbgF61eQmxCaMv7f9BFmDamNjQbbWmhk3yg2UNRD2Vv7z_LmQgZuUBLrZyj6Ma26gl8eztLDSX9B7eWJ7iCCTdnDyGGSobsBEdv1sleKe7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کتونی
ویتنامی و اروپا
رو از شهر مرزی
بانــه قسطی
💳
بدون ضـامن
بخر
👇
👩‍💻
https://t.me/doniakalacom
کانال تلگرام مجموعـــه بزرگ دنیاکالا
📱
https://tlgrm.in/doniakala
بزرگترین
واردکننده
🚚
کتونی در ایران با
سـ۳ـه شعبه فعال
💊
کاملاٰ
طبــی
ضـد زانودرد
🦵
کمردرد
🩻
اینستــاگرام
مجموعـــه دنیاکالا
📱
instagram.com/doniakala
✅
ضمانت
کیفیت
💸
قیمت
مناسب</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69491" target="_blank">📅 00:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69488">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cyIWpY1DmszBbyEVx_0kq1V7lcoNrnzq76IS0BS-m-NF16LImliu562zDm6cCfFbPkH6LjXUva4A2IbstpvbqtHWn-PGPgJ0hzRh3xG7-wdXgtGHXwlmbbnw8oBPzM7u2v5MX8nJHMNq-_l66S2n8VxvNcC7EFhy-ByoYL4vMYQqIXKzO26NsmkjuacGQctcTMHOJw0y_ugY27eQGcdeeu59IzSL9xu60kwrh46Z0Q4tr2TdmrcKxpEN2Oi6UMnGWeAn-cwW6ThQFT9_oSJoy0zpnvi9LPnABtuoblPNjoSU_UnTd6gy5egYHqKfh_rgXv_X2MSGskZoeFxMtwPADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/au5n3w2ZZ3Yb1ce-03ox6JhGoC_D7ItBNqmU2GkMDg7WZJvVBoAkxoTFQd_DHbFo3UmDD1Tny-XG1itezhkld5qJkG_uEXxvweGtQGxAkkmTQEPwL1w2xxFUC3WKrFinW-Ddp-P057oqgU43PcCXy99QYZ86V-0eRZnrLK70UYPlozPq-6JRIPYPbbP2PRWzxhnkHpp_TWJXRcUUwkrKvGPRRb1nBCpu18bf0vrzsbAfS-6A8JCiThFQWIPpBRbkyR7wjijSzBriAkUV7QwneKV_jryzqBfmFerNjkfqvaGrGQXIsCGQtCjkzEVTo22JZZ4CBDG-staVepdNXbobyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yu7oRBKaNHkYJzktiFPwTKAoeyAPuQXtIpzFp9S7Akm6sYZ0c8DIzUsiWSJMg7iCvBOdFr_Iw7rKcx8sJl-C-tmnus4KDCIRzXkJA99_6TBdBohwznquEk6C-ULEoh367mOrB0Sq6atFa_tlhv3b7KqaVfwvEpSvzIDRV8HtzylHWTaJPLQ_ZMqn8rmBx6JcvLPn5qZ-zzMePIVcM6ahbS7dM_84KNxnySSeGK8rep5JjxmYzaD5t0zTdd1r3SBoMfdf093qcOyEqVqg5qsb8EPq9BMgyexSu4EqnV-M8jXgXkxacHetkxDFPHfsfJan-vYZZUZqfFPOYdRDmIPC2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کامنت های دردناک مردم زیر قیمت PS5 تو سایت دیجی‌کالا
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69488" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69487">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=RdNM2Yzh0O_bNTTmL2jW62npKDinnht5Z7r0qyOquFadJJd2GIKUulWh2s9lIMOQmMu-1n9tWFjQUogywjGYdNFDi-YzsAl6BR7Rrp6jhhtU68rRW9yAP7VwxnIfHsFWBZXHmfazJ9-z8xu8O7Ml8B8_KL7GUAV3_6jEwqZyQctUoTfkHOUksjTz50eu5wb3hbOrpRlJ6iuirmJXA0fmT8GcfT13N7OwVMA6wHbASIA0019ItRq_-lobVMuXzuIeiAm3rtFJZnNhiEXi3mEh9Nh1geLRQMRXGnBK207z23QBDtGvletqkK4zqdzZXMotTbP3ew9aRkGIARnOhTjrcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ea32ba7fc.mp4?token=RdNM2Yzh0O_bNTTmL2jW62npKDinnht5Z7r0qyOquFadJJd2GIKUulWh2s9lIMOQmMu-1n9tWFjQUogywjGYdNFDi-YzsAl6BR7Rrp6jhhtU68rRW9yAP7VwxnIfHsFWBZXHmfazJ9-z8xu8O7Ml8B8_KL7GUAV3_6jEwqZyQctUoTfkHOUksjTz50eu5wb3hbOrpRlJ6iuirmJXA0fmT8GcfT13N7OwVMA6wHbASIA0019ItRq_-lobVMuXzuIeiAm3rtFJZnNhiEXi3mEh9Nh1geLRQMRXGnBK207z23QBDtGvletqkK4zqdzZXMotTbP3ew9aRkGIARnOhTjrcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
✈️
یک جنگنده F-16 نیروی هوایی اوکراین، یک پهپاد انتحاری روسی (Geran-2) را با شلیک توپ ۲۰ میلی‌متری ولکان (M61 Vulcan) در آسمان اوکراین سرنگون کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69487" target="_blank">📅 23:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69486">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22887d7155.mp4?token=lIY2eqMmTONkam5jBrKlkghOKFOXAHnVFZuu_okh4ULbe3L2kQpXMGXj3CHwo1t7vUHLcQWrKzRH-QdA0EDh-9Xp7E5nEexoc1RizesIui1MmgvlXC2PdYoY9Aoy6qJrcnr4ptJ51drVL_1H6Fn5AIhyuhHbbKa02Qxtcp3Mx8Tvbv0UAdUFE2UWiYRIJlbtuPLaG-oUCm9dhUo6oSVdlZoe0fjgYt3rc3YP2dK1P6dvsDrIZCd-8EipfyRodOYQRqAaXFoLadC-UPVjDCAszSwPuxFitdpGjE2g-p2_WcS0FgXhFcR7KbRbKez_PBvrzQRNmfONq6aa8j-Lo-ppPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22887d7155.mp4?token=lIY2eqMmTONkam5jBrKlkghOKFOXAHnVFZuu_okh4ULbe3L2kQpXMGXj3CHwo1t7vUHLcQWrKzRH-QdA0EDh-9Xp7E5nEexoc1RizesIui1MmgvlXC2PdYoY9Aoy6qJrcnr4ptJ51drVL_1H6Fn5AIhyuhHbbKa02Qxtcp3Mx8Tvbv0UAdUFE2UWiYRIJlbtuPLaG-oUCm9dhUo6oSVdlZoe0fjgYt3rc3YP2dK1P6dvsDrIZCd-8EipfyRodOYQRqAaXFoLadC-UPVjDCAszSwPuxFitdpGjE2g-p2_WcS0FgXhFcR7KbRbKez_PBvrzQRNmfONq6aa8j-Lo-ppPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانم که میبینید ۱۲۶ سالشه و اهل کشور برزیلِ؛ در زمان پایان جنگ جهانی دوم تقریبا میانسال بود
این بدبخت نمرد تا جنگ جهانی سوم رو هم ببینه و دبل کنه
😃
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69486" target="_blank">📅 22:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69485">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
آن‌ها با من تماس گرفتند و گفتند: «لطفاً حمله نکنید. ما توافق خواهیم کرد.»
این حقیقت محض است و همه آن را می‌دانند. چه کسی تماس نمی‌گرفت؟
کسانی که اطلاعات را به بیرون درز دادند کمک کردند، چون شدت حمله را فاش کردند و ایران هم از آن آگاه شد.
آن‌ها می‌دانستند چه چیزی در راه است.
قرار بود دیشب [حمله] انجام شود و مدت زیادی هم ادامه یابد، و [در نهایت] چیزی باقی نمی‌ماند.
اگر فرصتی داشته باشم که به افراد زیادی اجازه زنده ماندن بدهم، می‌خواهم آن فرصت را فراهم کنم.
بنابراین، هیچ محدودیت زمانی‌ای ندارم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69485" target="_blank">📅 22:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69484">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20068f370b.mp4?token=dedXlAbfbokbgbQ1z29JtTL2qu8RUzvubtBf2ur8D6-FiHrmZ9bkc-nbdZ0extWg2Ix4wT545jJRGrFq-k2IR5cEoTfyzAFB9YsSTF4pOtKvHdKPndU0yrGKeHxoc9zWqHBnmixaYHmoiSDs9TOSRYYBYi8KpxD0Z9X076kMA5br5uM5X28VkR8ScG_t17MFzNYVfvDl0aebNZOJBnxgk9L6W_iPEQReUW2kCLJzolj0v480ycrLNxzVoQhO3Lc2gEiqdorm1147tOic7dhyr9pmWYo1RC9yp5AMQwKeNoCQfb73NW2kJWR3wAJRaOfojpl-urWrX8rb6v5mS9O82w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20068f370b.mp4?token=dedXlAbfbokbgbQ1z29JtTL2qu8RUzvubtBf2ur8D6-FiHrmZ9bkc-nbdZ0extWg2Ix4wT545jJRGrFq-k2IR5cEoTfyzAFB9YsSTF4pOtKvHdKPndU0yrGKeHxoc9zWqHBnmixaYHmoiSDs9TOSRYYBYi8KpxD0Z9X076kMA5br5uM5X28VkR8ScG_t17MFzNYVfvDl0aebNZOJBnxgk9L6W_iPEQReUW2kCLJzolj0v480ycrLNxzVoQhO3Lc2gEiqdorm1147tOic7dhyr9pmWYo1RC9yp5AMQwKeNoCQfb73NW2kJWR3wAJRaOfojpl-urWrX8rb6v5mS9O82w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ در مورد ایران:
می‌خواهم قبل از نابودی کامل، آخرین فرصت را به ایران بدهم.
امیدوارم سر عقل بیایند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69484" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69483">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T04fi0C-Z9g_XG2naOyFIL_CF4mfPah6wHMKI6MbopEkMXR26oVOqfpT-3EZXpVx7bR4uTthSWMo0VkFrpyVYm_SC9e1pvF1N5m17cprSBGDkoFuo_4XHAWbstfvnnAQ5-DiSuw5HPYyWCAf8xpBvdqClO8eSjB3NhLJIDV144FiXGDK3KWh4z-KslVJe_MLVU6w3-Du7pKdauWq3jqPE1cwSYi8zA5ulLI5BmIWHYnnZd9Xdz1yf0KO7r9rCspjZTpzTLnpcdIQ27YeQ3-xIspEYhymBnAe7c7TLOnW1k0xX5tZPSOja1Bk5u4Dlavojm2y20g3WtJbEjmwq4VaOUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec7ad13cc1.mp4?token=RbvjJ3yxH4s9G2yOPXqmXSfOHSVh0-wqbgDKaCZfQ0vmp3AWMhPbp2qtvFzrLPB_YAPLetQz2_x5ZfIhot9kkm-TYgtwDv5fRKYG9oNlTWzIhVhNxPPhi1VL6V_1uUc-Jz472GjyC1cciHbtJPFWL9zhSVK9A4IEmF0mvrvAb0CiSJRVWrnY8qCJTBaoEIixWOAVV-4AreoslvhjrjecCm_65X9go_eQ0fNmz4nnVS6nBfT_95Lpi1V1v51iYgl43Bbax7MMItcsNbeYYhMOw5SlDFXyuTvHCO4aSfwcI9PCJc1YQXX2vQm3vUAksQL8TewFkcHrzqY_8paI4wn3T04fi0C-Z9g_XG2naOyFIL_CF4mfPah6wHMKI6MbopEkMXR26oVOqfpT-3EZXpVx7bR4uTthSWMo0VkFrpyVYm_SC9e1pvF1N5m17cprSBGDkoFuo_4XHAWbstfvnnAQ5-DiSuw5HPYyWCAf8xpBvdqClO8eSjB3NhLJIDV144FiXGDK3KWh4z-KslVJe_MLVU6w3-Du7pKdauWq3jqPE1cwSYi8zA5ulLI5BmIWHYnnZd9Xdz1yf0KO7r9rCspjZTpzTLnpcdIQ27YeQ3-xIspEYhymBnAe7c7TLOnW1k0xX5tZPSOja1Bk5u4Dlavojm2y20g3WtJbEjmwq4VaOUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا ایران حاضر است به وضعیت آزادی کامل کشتیرانی در تنگه هرمز بازگردد؟
🇺🇸
ترامپ:
اجازه نمی‌دهم آن‌ها [بابت عبور] هزینه دریافت کنند. اگر قرار باشد کسی هزینه‌ای دریافت کند، ما خواهیم بود. ما کنترل کامل را در اختیار داریم.
ما سازوکاری در نیروی دریایی داریم که نوعی محاصره محسوب می‌شود؛ آن‌ها به آن «دیوار فولادی ایالات متحده» می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69483" target="_blank">📅 21:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69482">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=fMIAFZAThql2ztNR9RXy46HQaIjczrPrjCSBroacK6uNZAW7uFW9QtJI2NRZalxKzCvoXJfzxWfTqVhDfBoAgxEE19O_PqwYyKrjeMOvk2pPMZsBT3mPbLjfEhYmHugjE9UF3CoM6Gzn5iDU503N7gGLzwYaB0fbrsAsvoQiBLkqt97m0VUYPihgpKpOMZEzVpsnjknbXr0XwI6NtgyqJt2NPlQvps82ykaXeMmtlibqbe9Vf7pxqJzoPhLkfCy3LqZbZvWX-5AIhfByaZ8SzGxeNbItLKLifSojFxHvDmq-k001LiAjyp-LdweXOOY9-L2_P4Lq3wd8Bm2achJX_URAQnWxxYi8Ck687EGo4-sm2B6o30YcZpehM5vOgL7zoqc9beBrntP_YyoUPymFxZavA_Wj7TbNAyWRCWsurLzcF7x_xAtgFjHlTLd9Y5xrd48UVwpAveN1Q4SLeLUgXTnzWvzhD5zY0L7FKv72-LzBsdlYapCcH7uFXQJDSpHsM7jE_NCRS2f_fJRvzYNhdBpN9atvAccYoMSDk-bWOeb4cbG0OWK8eG0ieq1fx761WO4_ubGWaSX4oUzubIFluglHZ1Zap2mE-78IHh-hb1S_crlM-EL50gkQ2S6Jv_a0-n3A7kUjKfjSonri6pF_9Ti2WBnp1yjqvq8YagXnyEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fd9c3c056.mp4?token=fMIAFZAThql2ztNR9RXy46HQaIjczrPrjCSBroacK6uNZAW7uFW9QtJI2NRZalxKzCvoXJfzxWfTqVhDfBoAgxEE19O_PqwYyKrjeMOvk2pPMZsBT3mPbLjfEhYmHugjE9UF3CoM6Gzn5iDU503N7gGLzwYaB0fbrsAsvoQiBLkqt97m0VUYPihgpKpOMZEzVpsnjknbXr0XwI6NtgyqJt2NPlQvps82ykaXeMmtlibqbe9Vf7pxqJzoPhLkfCy3LqZbZvWX-5AIhfByaZ8SzGxeNbItLKLifSojFxHvDmq-k001LiAjyp-LdweXOOY9-L2_P4Lq3wd8Bm2achJX_URAQnWxxYi8Ck687EGo4-sm2B6o30YcZpehM5vOgL7zoqc9beBrntP_YyoUPymFxZavA_Wj7TbNAyWRCWsurLzcF7x_xAtgFjHlTLd9Y5xrd48UVwpAveN1Q4SLeLUgXTnzWvzhD5zY0L7FKv72-LzBsdlYapCcH7uFXQJDSpHsM7jE_NCRS2f_fJRvzYNhdBpN9atvAccYoMSDk-bWOeb4cbG0OWK8eG0ieq1fx761WO4_ubGWaSX4oUzubIFluglHZ1Zap2mE-78IHh-hb1S_crlM-EL50gkQ2S6Jv_a0-n3A7kUjKfjSonri6pF_9Ti2WBnp1yjqvq8YagXnyEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره مذاکرات با ایران:
امروز یا فردا متوجه خواهید شد که وضعیت مذاکرات در چه مرحله‌ای است.
مذاکرات به هر طریقی که باشد، به‌سرعت پیش خواهد رفت؛ موضوع پیچیده‌ای نیست.
ما درباره بازگشایی تنگه [هرمز] در روز آینده صحبت می‌کنیم؛ بازگشایی کامل آن.
سپس درباره توانمندی هسته‌ای ایران گفتگو خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69482" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69481">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=Ph0m0ATegkkRnT9FJD3Ywaj59ZDurLYXrbaXTxhQwOvrKxx6TkPpYrP5P3GzIVhP8RRs3xFdqfU3zSplPKQIqGmgk5mSbu-yC_zj4UlQnEJMKxBaUKh-sP_hlYieNJKy7qXRMNU3fcNxscus-RkkEarTIIYnDpuUgFMzZYhAiFubuXpKQzHGjkBeFW5v60BahsTZzEG1LK15rFxBU3Uf5OhlagF-vJxSGsdIu9ubbOl6OujDrsKI4w6IlvkqOtMcap3PSxXRj1LxiHkbO7Vz-3QGP-rexzsMNCynJRFnO17siPi87GnbUfUiDcf1-xJtOVTFgHOxIrJFlfJ5v14WrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f121f698a.mp4?token=Ph0m0ATegkkRnT9FJD3Ywaj59ZDurLYXrbaXTxhQwOvrKxx6TkPpYrP5P3GzIVhP8RRs3xFdqfU3zSplPKQIqGmgk5mSbu-yC_zj4UlQnEJMKxBaUKh-sP_hlYieNJKy7qXRMNU3fcNxscus-RkkEarTIIYnDpuUgFMzZYhAiFubuXpKQzHGjkBeFW5v60BahsTZzEG1LK15rFxBU3Uf5OhlagF-vJxSGsdIu9ubbOl6OujDrsKI4w6IlvkqOtMcap3PSxXRj1LxiHkbO7Vz-3QGP-rexzsMNCynJRFnO17siPi87GnbUfUiDcf1-xJtOVTFgHOxIrJFlfJ5v14WrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک سند خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69481" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69480">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=FOGlCSFEcwZEuq7a2hJ_JDO-uuVB0Ydo5PGDYBPQLSg2mKn4YyGW1yjQ6b-I7vszRcNFSLxZTOZEf6dERo-U9B6VOaVm4jJNHi1_kmkZMuiZV70Pb85bXFtL5tCGsTsEXRpAz_Uv-QX21GQFMTVJ4Ea-cIQbzIYBzbRMJtwhT8H-FxQz4Vgr-SsZ7a9oRoq82QG6A8VDFMDISSHgyweQKL8cCcGb4dOdmzigwK1RWI4GQTmTiQelOZ9dt1GH8jeVKFiDyiBlc28z26fzxsDG8q_ruDfsYjNePxG1PCH6jAAv_onQTG4Qo1aaK15MWY1ydcn1LH5zlnywNikRGDdWTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85a0d41a8.mp4?token=FOGlCSFEcwZEuq7a2hJ_JDO-uuVB0Ydo5PGDYBPQLSg2mKn4YyGW1yjQ6b-I7vszRcNFSLxZTOZEf6dERo-U9B6VOaVm4jJNHi1_kmkZMuiZV70Pb85bXFtL5tCGsTsEXRpAz_Uv-QX21GQFMTVJ4Ea-cIQbzIYBzbRMJtwhT8H-FxQz4Vgr-SsZ7a9oRoq82QG6A8VDFMDISSHgyweQKL8cCcGb4dOdmzigwK1RWI4GQTmTiQelOZ9dt1GH8jeVKFiDyiBlc28z26fzxsDG8q_ruDfsYjNePxG1PCH6jAAv_onQTG4Qo1aaK15MWY1ydcn1LH5zlnywNikRGDdWTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
قرار بود دیروز ضربه بسیار سختی به آن‌ها وارد کنیم؛ بسیار بسیار سخت.
سخت‌تر از هر حمله‌ای از زمان جنگ جهانی دوم. این اقدام بسیار بزرگی محسوب می‌شد و ما کاملاً آماده اجرای آن بودیم.
در حال حاضر، به درخواست ایران و با حمایت عربستان سعودی، امارات متحده عربی، قطر و بسیاری دیگر، مشغول گفتگو هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69480" target="_blank">📅 21:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69479">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=t4cmV1BvEsCPolzSlyeSgTwClQ3YIuuSBw00N62NtQS6h9ryuloVfnrb-obsoMcCMRLfCsNlsPkLHuRfSTu9MdEtbs-f2x-w1neZ9KB1d-LyMqJ0i02WGWmzlbHDlDW0_DgAE10L17BwVijmpe7dZ80VlHyAO2ZsJsGBxgrhtb7zkFni4JIfuTb-iFPV0nr_J_E5L-HNoX3JJLK29D6OWh6aLxl8vBQSzDzy7W2hoH_4pbU4j7d4CInlAZdEGgRPEHJYOFJnVgRh62M4nOMN6sEP958mhuiBUzbcVQ6PQVGUtY76qjbYl4I8Cn0x3oJFK4Ri43JrbyA_1LFUbLzeL1XGcjI2APirJIlppYqdPbtR1BgmeZMpYsgfRtr-qXYmm4TzV8Ld1FHxhrPnBiEPt_LC-_-xJmd6J3S-F9zwnBdC_URLEAxwPBcafJJMZoskoUYq6uFaLrDnpW1Gg26LH7t-SNdyS6fELZePhCR-TDt2ralcpBEuQxyryoNUCCtHfpqXIXIufBnDLvvq3z4ommeUrLcQPD4RB3qm9MYaDu5V8tgYQeEOlaALHKtgnukQT0dmAgeuCbvr9nYyb8quqT5qj8yazUjFbWIS9hT1ISDAoPvNPBoofyQlSlJyYibBkh3Kckce5pyFs8gi6mynLByxG8vkYsgtBGbB66-UwbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2e110a924.mp4?token=t4cmV1BvEsCPolzSlyeSgTwClQ3YIuuSBw00N62NtQS6h9ryuloVfnrb-obsoMcCMRLfCsNlsPkLHuRfSTu9MdEtbs-f2x-w1neZ9KB1d-LyMqJ0i02WGWmzlbHDlDW0_DgAE10L17BwVijmpe7dZ80VlHyAO2ZsJsGBxgrhtb7zkFni4JIfuTb-iFPV0nr_J_E5L-HNoX3JJLK29D6OWh6aLxl8vBQSzDzy7W2hoH_4pbU4j7d4CInlAZdEGgRPEHJYOFJnVgRh62M4nOMN6sEP958mhuiBUzbcVQ6PQVGUtY76qjbYl4I8Cn0x3oJFK4Ri43JrbyA_1LFUbLzeL1XGcjI2APirJIlppYqdPbtR1BgmeZMpYsgfRtr-qXYmm4TzV8Ld1FHxhrPnBiEPt_LC-_-xJmd6J3S-F9zwnBdC_URLEAxwPBcafJJMZoskoUYq6uFaLrDnpW1Gg26LH7t-SNdyS6fELZePhCR-TDt2ralcpBEuQxyryoNUCCtHfpqXIXIufBnDLvvq3z4ommeUrLcQPD4RB3qm9MYaDu5V8tgYQeEOlaALHKtgnukQT0dmAgeuCbvr9nYyb8quqT5qj8yazUjFbWIS9hT1ISDAoPvNPBoofyQlSlJyYibBkh3Kckce5pyFs8gi6mynLByxG8vkYsgtBGbB66-UwbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: مذاکرات با ایران حالا دیگه متوقف شده.
🇺🇸
املاکی: نه، همین الان هم مذاکرات در جریانه. واقعاً اتفاق عجیبیه.
این بار دیگه اصلِ مذاکره رو انکار نمی‌کنن.
فقط نمی‌دونم چرا، هر وقت دارن مذاکره می‌کنن، دوست ندارن بگن که دارن مذاکره می‌کنن.
با ونزوئلا یه درگیری داشتیم که خیلی خوب جمع شد.
الان هم با ایران درگیر یه پرونده هستیم و اون هم داره خیلی، خیلی خوب پیش میره.
شما هم دارید فوق‌العاده کارتون رو انجام می‌دید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69479" target="_blank">📅 21:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69478">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=r7EFgpEmtqjFQ3lV_B2lmKH8iBu_dkJBPme2cGpJnSx8M5OMX_klH-nxMJU-Ib5pjjI5ooavoW2g9QGJuultYkITJlocnKbh4PoRPmuJYUecN7O3WBt1KrUQqGlwW_d6f7pnDB6ls5LeqOtzi4SOZ4fUJphqCnVgitPgMRwSCaDr4tHLVaf77pnu3P2f6HwFdJsNTNxrCsX-zkE5rJ0blA-2QvvtFrbXg7a77j3eBmJomFMXEvisOorBPhgyrj2IgaPhKdwXmjk3BJU0-hp6eopqLkZdEyqtctbpaWoIckfWuj-uuFTP6BYDJC_EzOJOEcNcrE8dQrlTwy4X10Qx1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a7f23c0a5.mp4?token=r7EFgpEmtqjFQ3lV_B2lmKH8iBu_dkJBPme2cGpJnSx8M5OMX_klH-nxMJU-Ib5pjjI5ooavoW2g9QGJuultYkITJlocnKbh4PoRPmuJYUecN7O3WBt1KrUQqGlwW_d6f7pnDB6ls5LeqOtzi4SOZ4fUJphqCnVgitPgMRwSCaDr4tHLVaf77pnu3P2f6HwFdJsNTNxrCsX-zkE5rJ0blA-2QvvtFrbXg7a77j3eBmJomFMXEvisOorBPhgyrj2IgaPhKdwXmjk3BJU0-hp6eopqLkZdEyqtctbpaWoIckfWuj-uuFTP6BYDJC_EzOJOEcNcrE8dQrlTwy4X10Qx1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
ما با ونزوئلا اختلافاتی داشتیم که به خوبی حل و فصل شد.
ما با ایران نیز اختلافاتی داریم، و این موضوع نیز به خوبی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69478" target="_blank">📅 21:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69477">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=BaTZJB87cKnDgb6MQBPioVq2QmFA7TmVeeo1jYK-xVP8aKFeGA-_sQb2ff8kxEI4BgJn50A1i1jcb441ZHbXRGp9dGuHYt7mOfGyuF--OZJRvvmkhl7XRJyYcsKlfu9nSJmXbcRYoUva1iWKW_nvtnnCh28GBhLyccysvr4YlspgvqIIQMSkoriUM8aDtSfB7IjTaGD4BwPvKWXwJ8cCDHf0b3HRh7sDsZHiHgtdZdmFj1gPp89bhcJg5YW7zL8QP5QOCsvizF2Ry9yvTycoCbjWFWQrZ0szv3dckDoEpmkcnDekPWYs_YZB_2XpmNfyXgHGl4lWrtT13gOaYMpCrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34a1d1b391.mp4?token=BaTZJB87cKnDgb6MQBPioVq2QmFA7TmVeeo1jYK-xVP8aKFeGA-_sQb2ff8kxEI4BgJn50A1i1jcb441ZHbXRGp9dGuHYt7mOfGyuF--OZJRvvmkhl7XRJyYcsKlfu9nSJmXbcRYoUva1iWKW_nvtnnCh28GBhLyccysvr4YlspgvqIIQMSkoriUM8aDtSfB7IjTaGD4BwPvKWXwJ8cCDHf0b3HRh7sDsZHiHgtdZdmFj1gPp89bhcJg5YW7zL8QP5QOCsvizF2Ry9yvTycoCbjWFWQrZ0szv3dckDoEpmkcnDekPWYs_YZB_2XpmNfyXgHGl4lWrtT13gOaYMpCrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
فرماندهی مرکزی آمریکا (سنتکام) فایل صوتی مکالمه ناو آبی‌خاکی USS Comstock (LSD-45) با یک شناور ناشناس را منتشر کرده است. در این مکالمه که از طریق کانال ۱۶ رادیویی دریایی VHF (فرکانس بین‌المللی تماس و اضطرار) انجام شده، به شناور دستور داده می‌شود مسیر خود را تغییر دهد و هشدار داده می‌شود که در صورت عدم تبعیت، با استفاده از زور وادار به اجرای دستور خواهد شد.
ناو USS Comstock به‌عنوان بخشی از گروه آماده آبی‌خاکی USS Boxer (ARG) و همراه با یگان یازدهم اعزامی تفنگداران دریایی آمریکا (11th MEU) در منطقه مسئولیت سنتکام مستقر است و توانمندی اجرای عملیات آبی‌خاکی و واکنش سریع به بحران‌ها را در اختیار نیروهای آمریکایی قرار می‌دهد.
بر اساس آخرین اعلام سنتکام، نیروهای آمریکایی تاکنون ۴۴ کشتی تجاری را که به‌صورت داوطلبانه از دستورات محاصره تبعیت کرده‌اند، به مسیر تعیین‌شده هدایت کرده‌اند، دو شناور را برای اطمینان از رعایت دستورات بازرسی کرده‌اند و دو شناور متخلف را که با وجود هشدارهای مکرر از اجرای دستورات خودداری کردند، از کار انداخته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69477" target="_blank">📅 21:13 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69476">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oguBRXV6FS619BavvSJ8P3VT9cFJvnli1s8QgoGR7Tk1JWsyRHi7iaVFn2D3JK8ZfchYMUMBLgckaAaPFsVMpQwDGiTJjDymLVJkpz-DqBJD5ec7nSfzv6EY2zNTfApCW0YqVNk88TEqTQBGUH589aZ5XlXmOHqE915tNGM_9cmvZZINF88U4B_iqS34nfA2Y3VsGfqkQUCyVweSU4Blke7lVCch7s3OxOI6v_efysh1oHBsaXo_nETr5CNwemCuzIKudEfbtrMBj0E6KGVcQwkfmJifMKzoflOY3Vr6aPymh6XzLY-hHJs5z3yCOxLSHihVwO3_seil2wZ5Kvp5PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مارک لوین:
من از اسرائیل حمایت می‌کنم.
من از اوکراین حمایت می‌کنم.
من از تایوان حمایت می‌کنم.
من از مردم ایران حمایت می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69476" target="_blank">📅 20:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69475">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebsK6Fo6QmpuaXUmycwYB3ax_590M-EsSjPAzWyWHO6qDjKNO2TsC0srUZSdJ-L17JptfVYt2mHMMaOYaAWkr4_RH_vwzIMCW0JlDBfqLcZQ7akhAPysiPAyZ8csXYFJR7Uv8cNdWtD4A6gLmEBMwilOTMDpNHWcHTjEjSFlRAl-diviESTzoRvTUVxgy-ZmPl77RiwPqvo8t0UM9ZF4um70xOLQtshcmF0C6vCbGUbuCK3LYVchEuT1nTwJatoTq6W29wv2QSYVdYA_2A_MTowtzdM08i_UhTBlX3G4b67FBnT387qAwMAlvTdEo4FzQFQNy7yF9hL1NAIm4X_QBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ : رهبری ایران واقعاً یه جورایی دو‌رو و ریاکاره که باورنکردنیه؛
خودشون می‌خوان مذاکره کنن، بعضی‌ها حتی میگن التماس می‌کنن، مذاکرات شروع می‌شه، جلسه بعدی هم قراره به‌زودی باشه، بعد علناً و با افتخار میگن که هیچ مذاکره‌ای در کار نیست، هیچ صحبتی نمیشه و فقط با «عمان» کار دارن!
بعدش هم همون چرت‌وپرت همیشگی‌شون رو تحویل می‌دن که می‌گن تنگه هرمز رو با قدرت خودمون اداره می‌کنیم، در حالی که از قبل کاملاً تحت کنترل نیروی دریایی آمریکاست و همون «محاصره» یا همون‌طور که بعضی‌ها می‌گن «دیوار فولادی ایالات متحده»!
هیچی به ایران نمی‌رسه مگر اینکه ما بخوایم، و هیچی هم نخواهد رسید مگر اینکه یه توافقی بشه یا اینکه کامل تسلیم بشن.
فرقی نمی‌کنه ایران بخواد قبول کنه یا نه، واقعیت اینه که ما داریم درباره‌ی راه‌حل مشکلی حرف می‌زنیم که خودشون دهه‌هاست ایجاد کردن، خیلی ساده‌ست:
ایران هیچ‌وقت سلاح هسته‌ای نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69475" target="_blank">📅 20:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69472">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4129d878df.mp4?token=hA6wNbI57NIY3sOiWUDWyhICJVMlEVB1b9_0lM1etRkNKHk2zlDZjQt-rAhdwjDKIboRzigVFpztCfe1wL1WpvpzkTiMcg5V0pRau-FmFo34ajMRkcQPSSi5Nb9t1e4saGLJxyVfxcwc8gq221NbFRatvnaL8WmNrPMGEVu-gplfkzjsfsNvN8DaUyWrWzoEWV-vThrslFe990h_GWjJojxW6JtfaQsd-4Do_zJ34pwU23g7kMbkTtXChQaf3F-QNRfOmJRlfCwOZaS-WD1LZ-e36yPQpE8U_9Xd33zncSEzYv-NGumLbKJ8zPBjsIuim3xWybQww81niEMCkQAnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4129d878df.mp4?token=hA6wNbI57NIY3sOiWUDWyhICJVMlEVB1b9_0lM1etRkNKHk2zlDZjQt-rAhdwjDKIboRzigVFpztCfe1wL1WpvpzkTiMcg5V0pRau-FmFo34ajMRkcQPSSi5Nb9t1e4saGLJxyVfxcwc8gq221NbFRatvnaL8WmNrPMGEVu-gplfkzjsfsNvN8DaUyWrWzoEWV-vThrslFe990h_GWjJojxW6JtfaQsd-4Do_zJ34pwU23g7kMbkTtXChQaf3F-QNRfOmJRlfCwOZaS-WD1LZ-e36yPQpE8U_9Xd33zncSEzYv-NGumLbKJ8zPBjsIuim3xWybQww81niEMCkQAnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇶
درگیری عرزشی ها و پلیس عراق در کربلا:
توی عراق یه روحانی به اسم صادق شیرازی، مخالف جمهوری اسلامی و خامنه‌ای هست، اون معتقده که فقط باید گفت لبیک یاحسین، نه لبیک یا خامنه‌ای.
حالا عرزشی‌ها دیشب افسار پاره کردن و هجوم بردن سمت موکب این روحانی و شعار مرگ بر آمریکا و لبیک یا خامنه‌ای سر میدادن.
عرزشی‌ها شروع کردن به کتک زدن مردم عراق تا اینکه پلیس وارد شد و با شوکر و باتوم عرزشی‌هارو کتک میزد.
طی این درگیری بیش از ۱۰۰ نفر به بیمارستان منتقل شدن و عراقی‌ها میگن دیگه نباید ایرانی‌هارو راه بدیم، غذای مفت میخورن و مارو کتک میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69472" target="_blank">📅 19:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69471">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=nkgMgChftkYryBhblIfyUjsQl5Y0bazNUyZ4ay-DXKspKxazLo4c5l1UdQBEE0lc3hnOxXjMmZFvwA8y95XuqDUdKyha55dnwbWDiX2g-mlofSWqO-pIseXUEmRsoRWjOKU1PjggLk4NOozAo-Y9W_zii4b7AsTLNhkv1iJCct_0a25CTk1xuQxgcpvLZCetFolD5H8VU3RcYcc1sxbLUef0xRn8i4m-SKS83kKH61CxbnzOVxB72o9SaSJGt-Fe8nJLHMOBWlOQe-8tb8PBTs-QGUAVV7RLPRVaOWomirZo9Fcc6AFWG7Prs0GmTySXHUNJdUciwxJhllkfvLFTi2BDA1OTSbjUYA6rnqKltORtfweGaImxyMgvRt7PRmk-8ICCTG5cwgudDI_v8yudL9Ye8D7QtH0cC1IX5BFNUeHjgeEezq3HLSwzhUqHNjU7YOFfeeYM7enF6nQfuVM4OevqP8mw6uZdf2-kG1Rl_-A4jICuJB0FR12hheD9d4Mc8JaRUkwcm_vVv2bd1VCoolMwThs71BXPmXlTPUCYyeLFqNDnNkBqBB-PYoGv-ltvUWrWef9gYAknlalt1iYVECKIkd8_uiWZOFayb4zvLugIk11O4x9J3y6ckQRfARgG87U7-6JgLyOA5IAEzUXS3e9e9MPcjE-JU0y_BXhhIgk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e330dd8504.mp4?token=nkgMgChftkYryBhblIfyUjsQl5Y0bazNUyZ4ay-DXKspKxazLo4c5l1UdQBEE0lc3hnOxXjMmZFvwA8y95XuqDUdKyha55dnwbWDiX2g-mlofSWqO-pIseXUEmRsoRWjOKU1PjggLk4NOozAo-Y9W_zii4b7AsTLNhkv1iJCct_0a25CTk1xuQxgcpvLZCetFolD5H8VU3RcYcc1sxbLUef0xRn8i4m-SKS83kKH61CxbnzOVxB72o9SaSJGt-Fe8nJLHMOBWlOQe-8tb8PBTs-QGUAVV7RLPRVaOWomirZo9Fcc6AFWG7Prs0GmTySXHUNJdUciwxJhllkfvLFTi2BDA1OTSbjUYA6rnqKltORtfweGaImxyMgvRt7PRmk-8ICCTG5cwgudDI_v8yudL9Ye8D7QtH0cC1IX5BFNUeHjgeEezq3HLSwzhUqHNjU7YOFfeeYM7enF6nQfuVM4OevqP8mw6uZdf2-kG1Rl_-A4jICuJB0FR12hheD9d4Mc8JaRUkwcm_vVv2bd1VCoolMwThs71BXPmXlTPUCYyeLFqNDnNkBqBB-PYoGv-ltvUWrWef9gYAknlalt1iYVECKIkd8_uiWZOFayb4zvLugIk11O4x9J3y6ckQRfARgG87U7-6JgLyOA5IAEzUXS3e9e9MPcjE-JU0y_BXhhIgk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
عملیات آزادی عراق؛
در ۱۷ مارس ۲۰۰۳، جورج بوش بزرگ رئیس جمهور آمریکا در یک سخنرانی تلویزیونی به صدام حسین و پسرانش (عدی و قصی) ۴۸ ساعت فرصت داد تا عراق را ترک کنند.
او هشدار داد که در غیر این صورت، حمله نظامی در زمان انتخابی آمریکا آغاز خواهد شد؛
پس از پایان اولتیماتوم، بوش در اتاق وضعیت کاخ سفید  او در آنجا دستور رسمی حمله را امضا کرد.
بیش از ۱۰۰۰ بمب که بعضی آنها ۱ تن وزن داشتند و ۵۰۰ موشک کروز تاماهاوک را به سمت مواضع ارتش صدام شلیک کردند، بین ۱۵۰۰ الی ۱۷۰۰ سورتی در ۲۱ مارس انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69471" target="_blank">📅 19:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69470">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=BmA3nJQN7mFXD-7a8rc2_mRBtCJlUid1z1gU14xf82G7dxbJUw0YiQnDqzBHc6mDfLrNRDSq50kt3LBMxt7MY6mOEmMm-U_xeI8U_I-Mhrs3S9NI2PzIRY1OoDLY4CZLRnCN3G65TbMwWsBLSpIJ3dECcLPDNbKy4PKgAbWD_wJqNnUrgHPujKmg2N4CcKNiU81-ROFXjDeoCOArl4DCc8mod2CC8YGHAOsZqMD8SC5ZzveB3c9mLAFOuQQJNTKfsXEKDMj4RUHORUEMRYwnkHW0GLcjT1eZkdhm-nyLn7o_P3nhHD4-G01LTweMm36r6TnhxwOC-CiSMYWWLAilcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00b8733ee9.mp4?token=BmA3nJQN7mFXD-7a8rc2_mRBtCJlUid1z1gU14xf82G7dxbJUw0YiQnDqzBHc6mDfLrNRDSq50kt3LBMxt7MY6mOEmMm-U_xeI8U_I-Mhrs3S9NI2PzIRY1OoDLY4CZLRnCN3G65TbMwWsBLSpIJ3dECcLPDNbKy4PKgAbWD_wJqNnUrgHPujKmg2N4CcKNiU81-ROFXjDeoCOArl4DCc8mod2CC8YGHAOsZqMD8SC5ZzveB3c9mLAFOuQQJNTKfsXEKDMj4RUHORUEMRYwnkHW0GLcjT1eZkdhm-nyLn7o_P3nhHD4-G01LTweMm36r6TnhxwOC-CiSMYWWLAilcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
اکثریت قاطع ایرانیان، اسرائیل را تحسین می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69470" target="_blank">📅 18:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69469">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=MAVmGpWapRqkcAeXFk0PJMcnmQphyqun1VR4bOTEd_UaFW_EgpXtRBcUxKJdHqpCMKIA1YvEZc6AvoVRdvHO0zHxGtoZDITqzvw36dJZJwQwxd7XxwauCShN5yzgbUEl7jjmxszP6aPvRlIyrrg4HtzmuRT5FJmzVQeu015C4Y8mUFfMwQpbFQIZpWGhuSxpKd4ul0N316SHf6uPK-GASuQdWFgoO-xc5jDaqKGdo_-FpOIAZawdFowGYAqsUhp1TQJlvwxmZS0fQY-yl5l9FpTGJe1kq9iy1SgtRA-CJspxHbeFfhZue3s-QSRzHHByeEYRQUSI14qinguIU8NnBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59529a1dcd.mp4?token=MAVmGpWapRqkcAeXFk0PJMcnmQphyqun1VR4bOTEd_UaFW_EgpXtRBcUxKJdHqpCMKIA1YvEZc6AvoVRdvHO0zHxGtoZDITqzvw36dJZJwQwxd7XxwauCShN5yzgbUEl7jjmxszP6aPvRlIyrrg4HtzmuRT5FJmzVQeu015C4Y8mUFfMwQpbFQIZpWGhuSxpKd4ul0N316SHf6uPK-GASuQdWFgoO-xc5jDaqKGdo_-FpOIAZawdFowGYAqsUhp1TQJlvwxmZS0fQY-yl5l9FpTGJe1kq9iy1SgtRA-CJspxHbeFfhZue3s-QSRzHHByeEYRQUSI14qinguIU8NnBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
خاورمیانه دیگر آن خاورمیانه سابق نیست. ایران هم دیگر آن ایران سابق نیست. ضربات سنگینی به آن‌ها وارد شده است.
آن‌ها همچنان توانمندی‌هایی دارند، اما به یک ماه گذشته نگاه کنید؛ آن‌ها به سمت ما شلیکی نکرده‌اند.
چرا شلیک نکرده‌اند؟ چون می‌دانند ما می‌توانیم چنان ضربه سنگینی به آن‌ها بزنیم که بازدارنده باشد. اگر به ما حمله کنند، متحمل ضربه‌ای بسیار سخت خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69469" target="_blank">📅 18:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69468">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=taw5MPHXKFMHpGNL6lHRb_WLFRegE-5GuSmATvqWmZ1QOfyaB2WTR1SJm0QMlIsGU1fjy00zYXFaYQ1WxprWGdPNEo5ba0LybI_x97pL74nFfk8whqf3ocY2WK9zJhYBEvAGix_e1hQSpFSkYC6Y_d1bHta1ChYp4pSCecd9tpl9WSyyrQHxaZ7ci2npmBNXMwDIdJtplbKxQ2G4ijoqIF701UUY9Jb4sjzgvvPYQh4ZjYK9om3Mz9-KgFU16Zov-Gy2KmB_Ap_zNFLGmecrgb-Bi3blUO2RfwbCcLPixsfNLtJyAAoUsDLjLu3mPRZwf4LCKHYsiHmG7r9wCDagnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1d96a133e.mp4?token=taw5MPHXKFMHpGNL6lHRb_WLFRegE-5GuSmATvqWmZ1QOfyaB2WTR1SJm0QMlIsGU1fjy00zYXFaYQ1WxprWGdPNEo5ba0LybI_x97pL74nFfk8whqf3ocY2WK9zJhYBEvAGix_e1hQSpFSkYC6Y_d1bHta1ChYp4pSCecd9tpl9WSyyrQHxaZ7ci2npmBNXMwDIdJtplbKxQ2G4ijoqIF701UUY9Jb4sjzgvvPYQh4ZjYK9om3Mz9-KgFU16Zov-Gy2KmB_Ap_zNFLGmecrgb-Bi3blUO2RfwbCcLPixsfNLtJyAAoUsDLjLu3mPRZwf4LCKHYsiHmG7r9wCDagnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
دیروز روسای دانشگاه تو جلسه‌ گله کردن که چرا حقوق اعضای هیئت علمی دانشگاه رو با تاخیر دادین؟
پزشکیان هم تو جلسه کلش خراب شد گفت:
نامه نمیخواد، اون گوشیو بده من بینم...
📞
«سلام؛ حقوق هیئت علمی دانشگاه‌ها رو ۱۰ روزه ندادین. خداوکیلی این درسته؟... بده دیگه... دستت درد نکنه، خداحافظ.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69468" target="_blank">📅 18:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69467">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04343db3da.mp4?token=fpd0YViaD0r26dMOaAuxTjyy9JxjWQpiMInIRAyE-DwDIde3loID_2NCrS12FdGldxD5SFQTdWnR0P6swY7xN1IqB_rXHzz9SyR2bHs_b2bAsoftsSPVjQvAFCwR_5sXStaqiULHqcR3CgdPgX_ovHd5iBxFJ9HSQCzc2qSkZcrIXDw8WEMMjlwwah8zAoFEFyQLfzagRKKj4ac3D6oMChXxkUz4-LCve0clW_Jh0ca-744qHNspAm6u1BiiyRgoIBbC9RD2o5QEY2rDiqjvuIoL43ZPx_sRroY5gUjcMrm7e_gn8BYuU3nk-nKPbXf-DhUJDY7simNi_2-g2s8XOkdp5WNtAmf29MRg8ZxeyEnX8g07iNH60U0_7tPMvO0FWyfPjrHOHIdsJVL3Ebgxn6gzuDysAAHlaFcLSwFqouyW2BMzwTzJNOoXcHYxvi-3VeOi1uHEjzmeLUqepB0XN1pEwFqIcFdxoiT3vaM1IbvcuOdQAXIfTOpEwgGooRM7Zbxbb3v3QKND1mE-20BDlYqy98lzhHWdzzwTpJfKaZM8m6As9JGmICMPtBj9t04H4PDrMy4RnMmoKn_liDkhq7OhgW8sSyWA2wFC2ahPF888kwluAljgXYT_dDvRO_SQ1ljrGbzgf0VovBHQJnrKGudGqDQDVG8bpKl2CL4eTQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04343db3da.mp4?token=fpd0YViaD0r26dMOaAuxTjyy9JxjWQpiMInIRAyE-DwDIde3loID_2NCrS12FdGldxD5SFQTdWnR0P6swY7xN1IqB_rXHzz9SyR2bHs_b2bAsoftsSPVjQvAFCwR_5sXStaqiULHqcR3CgdPgX_ovHd5iBxFJ9HSQCzc2qSkZcrIXDw8WEMMjlwwah8zAoFEFyQLfzagRKKj4ac3D6oMChXxkUz4-LCve0clW_Jh0ca-744qHNspAm6u1BiiyRgoIBbC9RD2o5QEY2rDiqjvuIoL43ZPx_sRroY5gUjcMrm7e_gn8BYuU3nk-nKPbXf-DhUJDY7simNi_2-g2s8XOkdp5WNtAmf29MRg8ZxeyEnX8g07iNH60U0_7tPMvO0FWyfPjrHOHIdsJVL3Ebgxn6gzuDysAAHlaFcLSwFqouyW2BMzwTzJNOoXcHYxvi-3VeOi1uHEjzmeLUqepB0XN1pEwFqIcFdxoiT3vaM1IbvcuOdQAXIfTOpEwgGooRM7Zbxbb3v3QKND1mE-20BDlYqy98lzhHWdzzwTpJfKaZM8m6As9JGmICMPtBj9t04H4PDrMy4RnMmoKn_liDkhq7OhgW8sSyWA2wFC2ahPF888kwluAljgXYT_dDvRO_SQ1ljrGbzgf0VovBHQJnrKGudGqDQDVG8bpKl2CL4eTQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو ای از یک طرفدار حکومت که میخاد ترامپ رو بکشه:
میرم خون رهبرمو از ترامپ بگیرم یه دهنی ازش سرویس بکنم از یادش نره
از لحاظ دفاعی یا هجومی همه جوره دهن ترامپ رو میارم پایین
حرکت های رزمی‌شو ببینید فقط
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69467" target="_blank">📅 17:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69466">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eflmt57R2RJKZ6BZnM0Pk00yThr0BplDIB_lXlNDrqybnc_qaJOXnsZNalZt1o-X-tQ7kB9WHo1UcUcdqqzMIxzx9Lf529IeAqSit6j7x4MV5OS_0eFObfMT6-iErrsyi2_kqme6pSUPbvAR1KQSWDXphmuOmdmxeaJ65-ufbmgubfeeMQry4lIskG-hVH3gI_ated4om6pxN2xgaUmfSFCGqfMYtKL-PnYlmqVDB0cl6b2cmm0gf_zMAqe4J3q4IIP2L8xjBa8x8cs6ugVPxZOkZOJs8HEbDArofwsfzLDTzDIlddujUmlGBtOE_ZU62CPamL4KZbjxBx6Liy17Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری
؛المیادین به نقل از یک منبع ایرانی:
ایران در پاسخ به آخرین پیشنهاد آمریکا، با بازگشایی تنگه هرمز تا پیش از پایان کامل جنگ مخالفت کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69466" target="_blank">📅 16:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69465">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSkZXb1lWth2O1E9aMPOzExPIchr6aNkga0XVNAbUR0uLrZ58mrcUpUfMDxS8AHTIEBNIDybHq2Bz1usg0VFIZs1amKYUht7Sk7ngrlmZ2amyQ_n43Bqnu_-E2ScDsDohNQZGzzrO1JQzyq8vBusfnR14yGGeTuM28Es-AvK2QRxPGymvSF03vmKRe3x_gflSkosGegRo7c-gbIYkGcYDELczEt3PYElecp4z5bZXQ5sef_CbX6r2rw-0c_1v8uT3AmRFT7MQHdcIXY5TyvUitAf43LReQkVmKcLrPa4LWehyaU70eGsEj6UKUPr5svX7Tqpb9LTXy5CKNOUIG7npg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست میانگین IQ کشورهای مختلف تو سال 2026 هم منتشر شد
🧠
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69465" target="_blank">📅 16:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69464">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863fff3357.mp4?token=cH6DCdnCndeg8uPBT8RVKKJW8IrjT7RaKymMnxTo_YZyi30JhnBG4lijvGZptWuCxBz-QI-I97VnjtOkfz-v0WdxzUnugR75Wrsq_Flgv66KIJH_nx5vzqMQFWZP0RoFNAMjv5VJPNrd7W6Tf6bNVqQ2CE3vSekglodfZ_MPfPxZZiuQAMVdqa5WgdhKwFV1X6nF93tLIl0eX_SRj3NsSPnhhhwoTLFcrFThXXGd30BDjemy1bHgusPiMCyznWnlqq5rJXRs5gk1xipX83K9uax-9e5WJOxv90VyFxxLmkhrPiQCgoDdzozlrbCwOrXI6qPy9jeFtw14oT3mu8w3Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863fff3357.mp4?token=cH6DCdnCndeg8uPBT8RVKKJW8IrjT7RaKymMnxTo_YZyi30JhnBG4lijvGZptWuCxBz-QI-I97VnjtOkfz-v0WdxzUnugR75Wrsq_Flgv66KIJH_nx5vzqMQFWZP0RoFNAMjv5VJPNrd7W6Tf6bNVqQ2CE3vSekglodfZ_MPfPxZZiuQAMVdqa5WgdhKwFV1X6nF93tLIl0eX_SRj3NsSPnhhhwoTLFcrFThXXGd30BDjemy1bHgusPiMCyznWnlqq5rJXRs5gk1xipX83K9uax-9e5WJOxv90VyFxxLmkhrPiQCgoDdzozlrbCwOrXI6qPy9jeFtw14oT3mu8w3Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مشهد یه دوره‌ی آموزشی گذاشتن برای افراد بالای 60 سال که توش مبانی اولیه‌ی استفاده از موبایل رو یاد میدن؛
موضوعات آموزش:
آشنایی مقدماتی با برنامه‌ی بله
آشنایی مقدماتی با اینستاگرام
وصل کردن فیلترشکن
ارسال لوکیشن
تماس تصویری
ویرایش متن تو واتساپ و بله
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69464" target="_blank">📅 15:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69463">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cda203069a.mp4?token=irJsMtZVqsCOqFWFP6-nKJnF-ktJ9uZQbvKiEvTagOfg6-M2ekaEpb8dHCIO0F8SAuxj_duwQ1M8A55vlpNUzdIkCkT-_YBVSX_0-Fd4ElpY84X1x_1EhwnhYhqBwqTjWww-KHljY48Yey2l9Vkl2cs0d4N9VQBUuHjf8WfE120qyp2iSTJFWlBQrs8q0qFPNOuavx0jONRaqTO886cj7-no157PGr3mD1jJ_RZU4oOdLRQDQ-xX8kV_f6Hnp4QnlGYNTxxSHUSRlHuq9Rbta2hyhlK_cwQT6kRVPVMOS-PZza0ldf3o340x-Qhl8QoWa3ON9JryswO_COEZoelw5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cda203069a.mp4?token=irJsMtZVqsCOqFWFP6-nKJnF-ktJ9uZQbvKiEvTagOfg6-M2ekaEpb8dHCIO0F8SAuxj_duwQ1M8A55vlpNUzdIkCkT-_YBVSX_0-Fd4ElpY84X1x_1EhwnhYhqBwqTjWww-KHljY48Yey2l9Vkl2cs0d4N9VQBUuHjf8WfE120qyp2iSTJFWlBQrs8q0qFPNOuavx0jONRaqTO886cj7-no157PGr3mD1jJ_RZU4oOdLRQDQ-xX8kV_f6Hnp4QnlGYNTxxSHUSRlHuq9Rbta2hyhlK_cwQT6kRVPVMOS-PZza0ldf3o340x-Qhl8QoWa3ON9JryswO_COEZoelw5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
میزان شانس بقای جمهوری اسلامی از زبان مراد ویسی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69463" target="_blank">📅 15:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69462">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b293a286.mp4?token=FTYPIcWExc5oGf8bU9ItGNgSFpyR_trB-ZPoDGP-Eq3JGkiS-9ttqIXmkaBas4p87J_mafYJAwG-AJ0yXEtu9Nlmp4LeJDtfiP-GGOGDIyaue8XOIeRfp4fWrEWn0TAB1Linv8o4AIp4zWGSuJ2xEIRPGghkqP8V6hvkTMbh_w1YSmOkQdHqqBDfzApUguBKRZUbCEm1CvAL_Ukni2aYjXSrI14gML8XgEuiRpwwlWI2bY8I5HNm-ji0y5JEvCu6BHhXp7-uX1s8oxNE6mQwHykh_6H_UX82LpdRQT6OckyhcAE5Djbd09gfB7z2ek4JAdRY3eO4JUnnSMAKbachow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b293a286.mp4?token=FTYPIcWExc5oGf8bU9ItGNgSFpyR_trB-ZPoDGP-Eq3JGkiS-9ttqIXmkaBas4p87J_mafYJAwG-AJ0yXEtu9Nlmp4LeJDtfiP-GGOGDIyaue8XOIeRfp4fWrEWn0TAB1Linv8o4AIp4zWGSuJ2xEIRPGghkqP8V6hvkTMbh_w1YSmOkQdHqqBDfzApUguBKRZUbCEm1CvAL_Ukni2aYjXSrI14gML8XgEuiRpwwlWI2bY8I5HNm-ji0y5JEvCu6BHhXp7-uX1s8oxNE6mQwHykh_6H_UX82LpdRQT6OckyhcAE5Djbd09gfB7z2ek4JAdRY3eO4JUnnSMAKbachow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اعترافات عبدالباری عطوان (تحلیلگر سرشناس جهان عرب) رو شنیدید؟ کسی که همیشه به مواضع خاصش معروف بوده، حالا لب به اعتراف باز کرده و از کابوس کشورهای عربی پرده برداشته!
عطوان در تحلیل اخیرش (مارس 2026 )به صراحت میگه:
اگر پسر شاه (شاهزاده رضا پهلوی) به ایران برگرده، با توجه به اتحاد استراتژیکی که با اسرائیل خواهد داشت ،ایران به چنان قدرتی تبدیل میشه که تمام کشورهای عربی منطقه باید جلوی عظمتش زانو بزنند و عملاً به نوکرهای ایران تبدیل میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69462" target="_blank">📅 14:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69461">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=Eq5w8xUZTEhMCoFG-gRxSu9irqUjIJ2MudMmamQVQcbcyCWTnZIt_M58Afj3fmtwA-qtEN7W2wKA6CWoRPtqZ-dzw57ZUUZwL4amHXVrA_AvKsS7RGFow0hdbPsRX_hx07L4ZWzLUG47xmNYTnoaLlhWv0qh6E5Zzw5txGjZupvJiXxqKuu8JRFI7WvdZgv3L151lOX9YPrScFxOjJLA1ZzosdcED5aBdBXGfsKGkwCDfpcUkpa5aSM8HlsCzOY6_O3Nz0LT3f4ccWCK-R0V2dzq4XMzoI7D7OJOLhrQFdRgKN5dKowQ4WBJMgznZOn511dVmv89TWOTVLbaw1U7zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0c3fd91e0.mp4?token=Eq5w8xUZTEhMCoFG-gRxSu9irqUjIJ2MudMmamQVQcbcyCWTnZIt_M58Afj3fmtwA-qtEN7W2wKA6CWoRPtqZ-dzw57ZUUZwL4amHXVrA_AvKsS7RGFow0hdbPsRX_hx07L4ZWzLUG47xmNYTnoaLlhWv0qh6E5Zzw5txGjZupvJiXxqKuu8JRFI7WvdZgv3L151lOX9YPrScFxOjJLA1ZzosdcED5aBdBXGfsKGkwCDfpcUkpa5aSM8HlsCzOY6_O3Nz0LT3f4ccWCK-R0V2dzq4XMzoI7D7OJOLhrQFdRgKN5dKowQ4WBJMgznZOn511dVmv89TWOTVLbaw1U7zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
عراقچی داره میره اربعین و ماهم توی تهرانیم.
دوشنبه مذاکره ای نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69461" target="_blank">📅 13:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69460">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
از فرصت تفاهم‌نامه و لحظه‌به‌لحظه آتش‌بس نهایت بهره‌برداری انجام شد
در این مدت، واردات تجهیزات جدید، تعمیر و بازسازی سامانه‌های آسیب‌دیده و همچنین تولید سامانه‌های جدید در دستور کار قرار گرفت.
پهپاد‌های جدیدی که اخیراً از آنها استفاده کردیم نیز حاصل بهره‌گیری از فرصت ایجادشده در دوره آتش‌بس بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69460" target="_blank">📅 13:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69459">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08375903ec.mp4?token=iZCZSnqTYgp9USPxB2W8uC6yP7Aon0EMGihw4jqbfz2wsFxiianLJSh7DlzdM91El8SMqysiS1kfdkcVoKWGD0nGmRgrF2dhmeB8InEtQGn19l7RrftIif9ra8DaDeoNoGNiACGyeIQ6uhT62ubpitXX7LbKKku_cUNg1cvyHj7OCvhn2-tbzuA_8JTbhvmUHZny4R9Q9sORB0IRhMNzoYxTIRyldpJ_uxQhsqG2vGDp3wA6XTzu_6oQNNaaA4q5D3MeTUzaPhPkaD0DS7760mhmmUcEkZO4QXuOzM08YV_etoZLzUQ3zsrmw1zWdR3KwQElGRybh7VhGCLNY9d_Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08375903ec.mp4?token=iZCZSnqTYgp9USPxB2W8uC6yP7Aon0EMGihw4jqbfz2wsFxiianLJSh7DlzdM91El8SMqysiS1kfdkcVoKWGD0nGmRgrF2dhmeB8InEtQGn19l7RrftIif9ra8DaDeoNoGNiACGyeIQ6uhT62ubpitXX7LbKKku_cUNg1cvyHj7OCvhn2-tbzuA_8JTbhvmUHZny4R9Q9sORB0IRhMNzoYxTIRyldpJ_uxQhsqG2vGDp3wA6XTzu_6oQNNaaA4q5D3MeTUzaPhPkaD0DS7760mhmmUcEkZO4QXuOzM08YV_etoZLzUQ3zsrmw1zWdR3KwQElGRybh7VhGCLNY9d_Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نیروی تفنگداران دریایی آمریکا ویدیویی از تمرین‌های تیراندازی نیروهای خود منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69459" target="_blank">📅 12:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69458">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm5ICu9gp6u-03k0PX9wkPC_s8cjdnhFh03oTX2kdsSediB_i5o5MncGRBs1xbqxV-PhSnyxJBsv7yFh4nC50V683OsFwD8EmXlk5t1eSwjgSN7bjJhD3POQaqJ0fwHaFe42JPxrAwRRmdc9ZbvPoFaWTu9jGYXNrb0UNZ4KY_uvPO4-Jeg7MgrUO19F61IHHBR--EuDaq58E0iG65_vpH3lhUspSMO4L6XxKq_fdW_SJ3suremwR3tG8Dt0poRHhkRaAomyAJNs8cbF_-366ORKqClrhJ4XGDVVuwEMl3TBHR-4dE6wG9yw0RfP8eTCu4bwxylVX0qcn6B3aQIwdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی، سخنگوی وزارت خارجه:
ما در حال حاضر هیچ‌گونه مذاکره‌ای با ایالات متحده نداریم و مذاکرات با عمان بر دستیابی به توافقی پیرامون عبور ایمن کشتی‌ها از تنگه هرمز متمرکز است.
هدف، تعیین مسیری موقت است که ایمنی کشتیرانی در تنگه هرمز را تضمین کند.
تا زمانی که محاصره دریایی و اقدامات ایالات متحده ادامه داشته باشد، هیچ تحول قابل‌توجهی در وضعیت تنگه هرمز رخ نخواهد داد.
🇮🇷
اسماعیل بقایی، در واکنش به ادعای جلوگیری عربستان سعودی از حمله آمریکا به ایران:
اینکه همه کشورهای منطقه اذعان دارند که از تحولات و شرایط آتی منطقه متأثر  شد، امری مثبت است.
جنگ ایالات متحده علیه ایران، جنگی علیه کل منطقه است.
طی پنج ماه گذشته شاهد بوده‌ایم که حضور ایالات متحده در منطقه، موجب افزایش ناامنی و بی‌ثباتی شده است.
طبیعی است که کشورها برای جلوگیری از تشدید ناامنی تلاش کنند، اما تجربه نشان داده است که هیچ‌چیز جز قدرت و توان بازدارندگی ایران، مانع دشمن نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69458" target="_blank">📅 12:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69457">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=QEFCAyL4Q4JkJDevvFzUpn3RbVcKwiNC6t6KhR9tBEBOtfQSkM3KaesV8TdcpyvrttokzHkG1Af2aZraZZcFAYgjFlyWMV3A3Y1X8lklMuvAeNC4SYEyX4USVAFxOHarREx_V_8gru2rOouUadpCP1J1FKuZlQh3C9zAWWJ2sMBM4Zkm4F4EeXXNORvmAru6tgFrRsKFgoDxjkyx-8UHt_DWztBvQIUOwLX0NZcrfKyvTUfoyZzqEHxT5EUoCEq35mOkChmOmryvEopfazST0OzLC5mRvQNyFJn85PvekdVP4YoTiPGnlEAhhu9jSjOqMa9k3PiFoNPPyeVVrroumg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5b3706c487.mp4?token=QEFCAyL4Q4JkJDevvFzUpn3RbVcKwiNC6t6KhR9tBEBOtfQSkM3KaesV8TdcpyvrttokzHkG1Af2aZraZZcFAYgjFlyWMV3A3Y1X8lklMuvAeNC4SYEyX4USVAFxOHarREx_V_8gru2rOouUadpCP1J1FKuZlQh3C9zAWWJ2sMBM4Zkm4F4EeXXNORvmAru6tgFrRsKFgoDxjkyx-8UHt_DWztBvQIUOwLX0NZcrfKyvTUfoyZzqEHxT5EUoCEq35mOkChmOmryvEopfazST0OzLC5mRvQNyFJn85PvekdVP4YoTiPGnlEAhhu9jSjOqMa9k3PiFoNPPyeVVrroumg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله پهپادی روز گذشته به مرکز لجستیکی عظیم شرکت وایلدبریز (Wildberries) در نزدیکی سامارا.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69457" target="_blank">📅 11:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69455">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKlXhMuHZFFGkfx2T73D7rMCETCez_Y17_rHPUoUPiVJY6FjI3OksOiK6BOee5ARuSS1EmxH_fdsc65ai6tO0tMcUHe5gwjDFtN_W7yGd0_KBUo9wp5cq0Vyf_ikMWFroCXBbVFcyjKC96f-tpAnsgIhsK_nfaqk_87F0Xe_EM1HChwRXpG7RGGoR6Ec22GDPchNRBOudkEtE57nBkEQGPTJm4vEb-fRXzatKWPI3EGFCsocws3lvkdB9WyqfXF7mxjlm_ft3bLIMCn1n8rYUvPNEBXRb182khAvXeSWkc0xJYV7zNUD_NRRJRxqTD7QkL6MFIeBMiORYwT9EM6tVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=U1FFEAwFpc0M0wImMDqevFqzrmKUgy4pf9LbBWNL7vCWh0KyaZEzgSlT8jlBffZ_jbuJU2X85V-FYPJa5d9qVa-nufHISqJLVQAHKRAHf2_Zy1mDpLzEQF9W3RKc3e4P2F427V2E0Xu5mkY0-eXnCPGncMbyuhR1_H1tA9QD4ZZFBaKJLBAT6tdsHBCKsMbB5vCAREaVm0zbC79KMibpaenAhkXQwoiNMhR7fRGmMWCl7k5JdYZIKOci3myOlA7J8mPf4MyQSee4-JwH_5_QxAvo-AQoUHysRGglL50GeL1MHIWbealP-S6cqAa97lXyc4iBQXTG2yy_12xwp_9suw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ab83ad5.mp4?token=U1FFEAwFpc0M0wImMDqevFqzrmKUgy4pf9LbBWNL7vCWh0KyaZEzgSlT8jlBffZ_jbuJU2X85V-FYPJa5d9qVa-nufHISqJLVQAHKRAHf2_Zy1mDpLzEQF9W3RKc3e4P2F427V2E0Xu5mkY0-eXnCPGncMbyuhR1_H1tA9QD4ZZFBaKJLBAT6tdsHBCKsMbB5vCAREaVm0zbC79KMibpaenAhkXQwoiNMhR7fRGmMWCl7k5JdYZIKOci3myOlA7J8mPf4MyQSee4-JwH_5_QxAvo-AQoUHysRGglL50GeL1MHIWbealP-S6cqAa97lXyc4iBQXTG2yy_12xwp_9suw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده مردم در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69455" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69454">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=PrXLErx1jBcZz1yscg-dUyHO1824Ydfi0vsMuaouwNkn_DGpFEzEvVIvdt6KLuRwBttw1TzK97GuJZcyoKgW0dY3sJMZzzuDOWqnApMfqpeumxFv1z22A5VaeIYviBVVjmRah-DTapv-f7-gj-lyHQj_JKGoOaCFsntz_8HR1r7npI9gT8Ac3jRzB6JVTzSHHmIFCMu5Ep-vnp9Vm-75pekyJU8i_8HiOLFQcxo-OPtwHUluwICvpH1QrfeKfyBkOOpgnKBEP0eAkfZB95_EuFAGFRfj6FyvPFPyq40s8n8dPCMqvHI_jVxpUCtR9EeAL74wRsKMJZAFN7meqXvzvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63f06a84a2.mp4?token=PrXLErx1jBcZz1yscg-dUyHO1824Ydfi0vsMuaouwNkn_DGpFEzEvVIvdt6KLuRwBttw1TzK97GuJZcyoKgW0dY3sJMZzzuDOWqnApMfqpeumxFv1z22A5VaeIYviBVVjmRah-DTapv-f7-gj-lyHQj_JKGoOaCFsntz_8HR1r7npI9gT8Ac3jRzB6JVTzSHHmIFCMu5Ep-vnp9Vm-75pekyJU8i_8HiOLFQcxo-OPtwHUluwICvpH1QrfeKfyBkOOpgnKBEP0eAkfZB95_EuFAGFRfj6FyvPFPyq40s8n8dPCMqvHI_jVxpUCtR9EeAL74wRsKMJZAFN7meqXvzvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای ازجواد موگویی که توی برنامش داره خیلی شیک و مجلسی جای همه فرمانده‌ها و مسئولان رو لو میده:
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69454" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69453">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVKpKXFe8-alp21_RMz6KZqqoXNq4itXdOSJgQ4HgY7EQhxmDMF8VtubXUb_mXzBHalc5Uau38Zg1aURnu2mUrGdMmWJSW_xVUzfSHT7pa5oogOUJBiQyUyLa21-uJkFRYdORxludbVZKxHIJbRUdJ3JBQD_0QGlEaELwGmrHGbPN8VJqETOYlAlwsZ7SasTg65ZGniTUmHpkOv0m1CY6NXy4BN3RBHDBbU9CnLkZP30C6cW_m6Jzs_LNzJT3f36zaRuh-n7EVpYk82XkGKwTZc4yn9PSld2Du4TfWjIHQ0Ox4A3pkMV4qHULAHOZ0XRRokwXnpxMem_3HzNrcMuI-0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b06d3aa4b2.mp4?token=gkL6GzPf-jqLQpCs7fKNRQCi06Rp2DdUhF-eAieN52a9Mrqor8I9XvQzMnoTUc_mhdHZiIFML6NCOXU4z80oFHK1C4z9VmPf_cQxnfbYNBQKN4np9HX4BLNVdGUhokSWj1WRJCG68Ys-42HDavLcvjQ4uqE6__9LLVqUblLjaC-U75g8AI8E9tr_Oz7ODNDP0w7algQnb31hKSkHO4_cXmIgpHO1Qavmlj-4URjA9ruED8LbRCMOtPUt1Z_LnxdEmccZkXe6O6z6K_7YlyhlCM7fQepiNPvkTpJxUxB2YrIDhNgYSjcIT_jc9tcVJ8zrQAMJPMuhRURThlnshLkYVKpKXFe8-alp21_RMz6KZqqoXNq4itXdOSJgQ4HgY7EQhxmDMF8VtubXUb_mXzBHalc5Uau38Zg1aURnu2mUrGdMmWJSW_xVUzfSHT7pa5oogOUJBiQyUyLa21-uJkFRYdORxludbVZKxHIJbRUdJ3JBQD_0QGlEaELwGmrHGbPN8VJqETOYlAlwsZ7SasTg65ZGniTUmHpkOv0m1CY6NXy4BN3RBHDBbU9CnLkZP30C6cW_m6Jzs_LNzJT3f36zaRuh-n7EVpYk82XkGKwTZc4yn9PSld2Du4TfWjIHQ0Ox4A3pkMV4qHULAHOZ0XRRokwXnpxMem_3HzNrcMuI-0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مارک لوین:
تداوم توقیف دارایی‌های متعلق به ایران
ادامه محاصره دریایی برای قطع درآمدهای نفتی و گازی ایران
هدف‌گیری مستمر فرماندهان نظامی
حمله به کارخانه‌های تولید موشک‌های بالستیک و پهپادها در سراسر ایران
هدف قرار دادن ساختمان‌های دولتی و تأسیسات متعلق به سپاه و ارتش
حمله به بانک‌ها و مراکز مالی
دست‌کم تا ۳۰ روز و شاید بیشتر، هیچ آتش‌بسی در کار نباشد.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69453" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69452">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/998caf4317.mp4?token=c4vMWLOZ6lLqg28wpQGbo3I5yuBqtF5NwmKOtjkBABYYjcyGQKhkqImwLAk5rcLaDVMh45tMc5ldww8Vwx8kg1-iixB4pSKiDw3lB95Gjzg-Qn1kCsaI0ruuum9JQn9vWOMvvkTManVrwZnlFnXS6Hyre4akRh0N4WYhAw_xY39dP_56eyNZq4SOyFO4hb22vQhVS2AFRrhAP011iIaXvh-DcQk74pEqRbm_cwhC74aGhsSKYiKrBTIWTlYGzAucvXAaxj9FCJGM6JXqNoUguYzF0--_VgiIJrpDIlftrAFSHfRAqlkvFWyo5vPRc68EKnVq-HY4p81AvbEK1C1-0wW0Mod0HXlXRWxI0QOUY-Yco4rCgV9yPmlhZewT46VFpWsFypybIZTrd6o5YYYQAVeQxg1OvN4UWl94G_NCF1f5Hw_HnwQgArBGln5PYgVJ8ZXuhzT-UicR_08iAA4oSwCInOqn9lVgIrHu7IIeS7wZYVgqgIQo_GGepsrChOPFuZWaAyNb_JM5rGuj2AFyNIlKVZfTx86b717Qufgc_rMapLBUxYR8f3lpAvhMiG7LolmjuMnLUM327hfqCKuya4Nzb9FeJAvsSX91ej9TWPTMhtrZOf1NkFUToPvknD-r0f8DPurlGpOFHOUhQF2C6I4UveBTfrqWob-KjEuQAtI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/998caf4317.mp4?token=c4vMWLOZ6lLqg28wpQGbo3I5yuBqtF5NwmKOtjkBABYYjcyGQKhkqImwLAk5rcLaDVMh45tMc5ldww8Vwx8kg1-iixB4pSKiDw3lB95Gjzg-Qn1kCsaI0ruuum9JQn9vWOMvvkTManVrwZnlFnXS6Hyre4akRh0N4WYhAw_xY39dP_56eyNZq4SOyFO4hb22vQhVS2AFRrhAP011iIaXvh-DcQk74pEqRbm_cwhC74aGhsSKYiKrBTIWTlYGzAucvXAaxj9FCJGM6JXqNoUguYzF0--_VgiIJrpDIlftrAFSHfRAqlkvFWyo5vPRc68EKnVq-HY4p81AvbEK1C1-0wW0Mod0HXlXRWxI0QOUY-Yco4rCgV9yPmlhZewT46VFpWsFypybIZTrd6o5YYYQAVeQxg1OvN4UWl94G_NCF1f5Hw_HnwQgArBGln5PYgVJ8ZXuhzT-UicR_08iAA4oSwCInOqn9lVgIrHu7IIeS7wZYVgqgIQo_GGepsrChOPFuZWaAyNb_JM5rGuj2AFyNIlKVZfTx86b717Qufgc_rMapLBUxYR8f3lpAvhMiG7LolmjuMnLUM327hfqCKuya4Nzb9FeJAvsSX91ej9TWPTMhtrZOf1NkFUToPvknD-r0f8DPurlGpOFHOUhQF2C6I4UveBTfrqWob-KjEuQAtI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇱
🇺🇸
ویدیویی جدید از لحظه بمباران خیابان فردوسی در زمان جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69452" target="_blank">📅 09:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69451">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7I5wmhcWhS18ECjZVrW-qS6FxP_Dw7kOBsz9kxibM42eUk7ByR0ktkzzPgog99EEaKoQZ0GNHI5MnBO6jIBXjjXiaPo2MpiSsyGrAO77nU4gYiqGcPaH_B9kccfnWluAAppPPc3AKNoGj-9Z13PUhez0r2MSPUiXRFJ32A8JA-369IXE66txrheGiDiwQ49VDHso0WtO8GltoUM7bTKCoY50h0bcMXG934VFjSTtxgMfkOd1L1yN1KX_eqny_2cjICSNxaPHkc6pYs5yq0I8IHhw-l04i_7JRN1kIZAId-zncxdMN8xQS6M2iWwXyZ4XH14gIUf4bTQs8OpJtO38g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
هگست وزیر جنگ آمریکا:
واقعیت.
وزارت جنگ آماده‌ی حمله بود - و همچنان آماده است - در سطحی که از جنگ جهانی دوم دیده نشده است.
قفل و بارگذاری شده(آماده اقدام).
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69451" target="_blank">📅 03:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69450">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tMR2Bbr5PTuoU9id2FZkFbI9RCkQGn3Uno0PHjo4wms3zDLHodthD1ooGJwkZ6QizP53UVTim0W2oPrKvoqi1HC4q1o_KPjZBIRmPMFJM8Hwd8wu-GAKVn3kVt_KphEgplOuJyStXbuWHn7hIaGk3hUVQljOAwlB8bjMcIRQ0rcbPtIFkBAdIEEUXJgp6bod9D7b4bLOQ1dtfh5IbK4fPNQEe6GcmMCca7nH9u9oSSQT8z-1gVb-wpa2rT4hd9ChKC2_Cc1l5sOflDqUw_uLVPrefvPxsnMTuxfwPdry54US6n8Lbh8XpQ61cajfjHe3rPx3X_KHpOYS42YgkFB8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پست جدید کاخ سفید:
به ترامپ اعتماد کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69450" target="_blank">📅 01:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69449">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxPWQneGFl-9DImjb1uL2Qgg-OnWuloQBsxL5AVoixMLiP8LXAgtboZZT6YyxkYqM8wX2fyb8Wx29ZQqpvMG__mmME5lIOuM9YoANyjJP0IWbo6YvUSKU_o39GlKxN4lCcmyy4EF_Z3az7Sz715SBUDetQoA35672xbmOKGTice59Rr_qcC1m4hF6XYC_L4DH9qxUrkb0CQ2C28GLcyMR1Hp_NlthJ7g90rrDlACNG-lCZNI_7qhZsGrnunr1rdGW-WU63r3RcJYcLYKBbGDlXY5__fF4eDhLlYfqQEijl6DrE4dY5uhqlzsnvXdjew1aTs6zM4nqKJRGtDhw4nsrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):
گزارشی مبنی بر وقوع یک حادثه در فاصله ۲۰ مایل دریایی شمال‌شرقی خصبِ عمان دریافت شده است. مقامات در حال بررسی موضوع هستند و به شناورهای حاضر در منطقه توصیه شده است که احتیاط کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69449" target="_blank">📅 01:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69448">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
وسط حرفای ترامپ یه کشتی تو تنگه هرمز هدف قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69448" target="_blank">📅 01:47 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69447">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=l7NL4NNOpJ7r4-SPonGPNg2hzwbBYrEcC6MrYAlNHvmBPpHXJ6I9EXPLV7rzGTefgjxgJazr1vPuSr-BmLyQDeUA2rH2ZkcNgpHx5yJH3RcCTOk3ldsjJD-xE6ZpcBjfKFA-bK7kHJWxPpjHfzvi8sO0_VI4DGbhxjkgt6NEhUroM2Y732wJHlyp9H6pfpBBo2HsAzUlhv5GZIXWn4YTEF2qNxP_XBSqKEMzXwohpWpx9PBSPCx2kh9tTW8nijsfeq4KJKJHFfVef7goy3uUJT80T-XXL70BzVZFbOwCeg6eci9z3fn_3tBF3mAmR4ibMZ4Nhgh9SvmaBpXCu12Rhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac4e8fdd53.mp4?token=l7NL4NNOpJ7r4-SPonGPNg2hzwbBYrEcC6MrYAlNHvmBPpHXJ6I9EXPLV7rzGTefgjxgJazr1vPuSr-BmLyQDeUA2rH2ZkcNgpHx5yJH3RcCTOk3ldsjJD-xE6ZpcBjfKFA-bK7kHJWxPpjHfzvi8sO0_VI4DGbhxjkgt6NEhUroM2Y732wJHlyp9H6pfpBBo2HsAzUlhv5GZIXWn4YTEF2qNxP_XBSqKEMzXwohpWpx9PBSPCx2kh9tTW8nijsfeq4KJKJHFfVef7goy3uUJT80T-XXL70BzVZFbOwCeg6eci9z3fn_3tBF3mAmR4ibMZ4Nhgh9SvmaBpXCu12Rhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
نمی‌دانید این حملات به کجا ختم می‌شود.
منظورم این است که آیا همسایگان ایران با هجوم سیل‌وار جمعیت به کشورهایشان مواجه خواهند شد؟
یک فاجعه. اتفاقات بد بسیاری ممکن است رخ دهد.
ترجیح می‌دهم توافق کنم. به دنبال کشتن آدم‌ها نیستم.
آدم‌ها می‌میرند؛ خیلی‌ها می‌میرند. ما چنین چیزی نمی‌خواهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69447" target="_blank">📅 01:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69446">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=ro80RfUedYXhrmJim_k6_LRO16cDxPDo0h2deFJQNb2BPGjJREcHgW91lvHXYJehJLhTaGcbwSN52A6VxjCOTglQBk4SuDuHiSBiNL4Uo7rStxXLwip2ePuxPKH_Ozdf8CREMbuVn7Rq1IdEQiJP4A0Nbpf7YUcOAE-d3ZZ4yYZeYICpKh2ndfFNHqWuf6CJz_SasGRc9ChCNSKpDnKYgHQeSYYww4C01YiWn81jhVcGBlIEvsGwDRNeIukVZDaY6D7LA41AIOeSIjOXLgV9vpCDG2NcNphAHENgFTo6_wxVD0SIs0ClDexrKWjsIhoho0lmaMvkfFlFmMSM6z85dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/320bfbc7f8.mp4?token=ro80RfUedYXhrmJim_k6_LRO16cDxPDo0h2deFJQNb2BPGjJREcHgW91lvHXYJehJLhTaGcbwSN52A6VxjCOTglQBk4SuDuHiSBiNL4Uo7rStxXLwip2ePuxPKH_Ozdf8CREMbuVn7Rq1IdEQiJP4A0Nbpf7YUcOAE-d3ZZ4yYZeYICpKh2ndfFNHqWuf6CJz_SasGRc9ChCNSKpDnKYgHQeSYYww4C01YiWn81jhVcGBlIEvsGwDRNeIukVZDaY6D7LA41AIOeSIjOXLgV9vpCDG2NcNphAHENgFTo6_wxVD0SIs0ClDexrKWjsIhoho0lmaMvkfFlFmMSM6z85dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در مورد ایران:
ما حمله‌ای داشتیم که می‌توانست بزرگترین حمله از زمان جنگ جهانی دوم باشد.
این حمله برای آنها فاجعه‌بار می‌بود و آنها نمی‌خواستند ما این کار را انجام دهیم.
صادقانه بگویم، عربستان سعودی هم این را نمی‌خواست.
آنها فکر می‌کردند که توافق قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69446" target="_blank">📅 01:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69445">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=dBrlgvWb4Vhj6vUvMizOrE9dU6OLoxahNZ3ED9gnHtgY28pd9JbFIFBUh7cNhyBEv8IRXVTgKAU4H7cs-xdNVsTaQkaIBhK9sNh3ot4T9HxsHmiQZzacZayL9S0ybHV3lpK63UZ6LklOzqj9g3WyQ-Isn7pt9LAx-DtmoCSwMjOeBHLlh3GarfQSrc-3cIv6738K3tdfDysuXAwCIDTcIseCvRVRQe_yiOBltVRtdk7ztXjPxnt4ImqD0cDxuwJz229fs7ga-YrrVGpzDNQc7akUmpDZlQZI2QREZ6VwCNy4rQraC8noBACY6piP-nxk11XqTPtG6gNkZ4-JXgcRIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4635f3df1.mp4?token=dBrlgvWb4Vhj6vUvMizOrE9dU6OLoxahNZ3ED9gnHtgY28pd9JbFIFBUh7cNhyBEv8IRXVTgKAU4H7cs-xdNVsTaQkaIBhK9sNh3ot4T9HxsHmiQZzacZayL9S0ybHV3lpK63UZ6LklOzqj9g3WyQ-Isn7pt9LAx-DtmoCSwMjOeBHLlh3GarfQSrc-3cIv6738K3tdfDysuXAwCIDTcIseCvRVRQe_yiOBltVRtdk7ztXjPxnt4ImqD0cDxuwJz229fs7ga-YrrVGpzDNQc7akUmpDZlQZI2QREZ6VwCNy4rQraC8noBACY6piP-nxk11XqTPtG6gNkZ4-JXgcRIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار بود حمله‌ای گسترده باشد.
آنها از ما خواستند که این کار را نکنیم. گفتند: "لطفاً این کار را نکنید."
همسایه‌هایشان هم همین را گفتند.
ما فقط می‌خواهیم ببینیم که آیا می‌توانیم به توافق برسیم یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69445" target="_blank">📅 01:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69444">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=ZKDFPI4ppEI72d2oNG70iXe4hHZnI34bhCjUbq9NY8YMB_GoaBKAIZHYSVQCNoB_u1Ekfzmfd09m-Im5djQAnBn1WKlMaFZABNYPLzixF0KOluDpCOMT9eDwku65U8VnPpuCobR3bKC696CxQpHLgedIvP0DT9wyAA41SuxFoQMLRZu6Q6SEGa1mrnkZQQRJ_rNCg1E8gQm2t_8X2tQg5wuWP8CSISA5IDkeLtWEd18wuKmDVaJIs3uxoWVgMqtZTTXFgcYTFcrosPtYPJJgEyil_JAVUK7qixZLY2h5jjrmU40ouWH329oEhKxOO5gAa6ZOW41ULXO9-zeZFi1mMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4ad85e5d7.mp4?token=ZKDFPI4ppEI72d2oNG70iXe4hHZnI34bhCjUbq9NY8YMB_GoaBKAIZHYSVQCNoB_u1Ekfzmfd09m-Im5djQAnBn1WKlMaFZABNYPLzixF0KOluDpCOMT9eDwku65U8VnPpuCobR3bKC696CxQpHLgedIvP0DT9wyAA41SuxFoQMLRZu6Q6SEGa1mrnkZQQRJ_rNCg1E8gQm2t_8X2tQg5wuWP8CSISA5IDkeLtWEd18wuKmDVaJIs3uxoWVgMqtZTTXFgcYTFcrosPtYPJJgEyil_JAVUK7qixZLY2h5jjrmU40ouWH329oEhKxOO5gAa6ZOW41ULXO9-zeZFi1mMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره بمباران ایران:
گروهی از افراد هستند که خیلی دوست دارند من این کار را انجام دهم—صرفاً انجامش دهم—و گروه دیگری هم هستند که نمی‌خواهند من این کار را بکنم.
🎙
خبرنگار: آیا ایران برای دستیابی به توافق ضرب‌الاجلی دارد؟
🇺🇸
ترامپ:
خواهیم دید. من به دنبال کشتن مردم نیستم.
از ولیعهد عربستان سعودی پرسیدم: «ترجیح می‌دهید ما چه کار کنیم؟»
او گفت: «ما توافق را به حمله ترجیح می‌دهیم.»
🎙
خبرنگار: گزارشی وجود دارد که می‌گوید شما در حال خارج کردن نیروهای آمریکایی از کویت و بحرین هستید.
⏺
🇺🇸
ترامپ:
نمیخواهم در این باره اظهار نظر کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69444" target="_blank">📅 01:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69443">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=iWzoWSq20LbuELDzHmPSZ-_W4j7PZneGSXmJR2sSYLAgOTdNHgryCgy_j-xmcdHdKGTfpbtIODkRqBhVJRM9dgU7PCq0hUKCypRLCepZewQDmZ-2MmVmpcMeayYIbQuKyG7UaJh6ZHTKohT8OCkKz1xlKY5IIS4SmZtmPlvwlv-yfaknHsVgqp5k7fwAlTVdeTqc_14zMqPcOUfNcLB_4cMZrIMQ86GoaDphfyS3hZmFH93ILBvXQVKLIQ4eIGaC5YaMMo5gKoGY_QdE_gXnsFVBN_jmGqjAlxJ8nW_WuP_yzFldphRYyrs0kHRZ5pFIGcy6OcyrZjKQYcHsQDnXaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098cb6b6b9.mp4?token=iWzoWSq20LbuELDzHmPSZ-_W4j7PZneGSXmJR2sSYLAgOTdNHgryCgy_j-xmcdHdKGTfpbtIODkRqBhVJRM9dgU7PCq0hUKCypRLCepZewQDmZ-2MmVmpcMeayYIbQuKyG7UaJh6ZHTKohT8OCkKz1xlKY5IIS4SmZtmPlvwlv-yfaknHsVgqp5k7fwAlTVdeTqc_14zMqPcOUfNcLB_4cMZrIMQ86GoaDphfyS3hZmFH93ILBvXQVKLIQ4eIGaC5YaMMo5gKoGY_QdE_gXnsFVBN_jmGqjAlxJ8nW_WuP_yzFldphRYyrs0kHRZ5pFIGcy6OcyrZjKQYcHsQDnXaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار: در مورد ایران، حالا چه پیش می‌آید؟
🇺🇸
املاکی:
ما در حال گفتگو با آن‌ها هستیم. این گفتگوها از بعدازظهر فردا آغاز می‌شود. این کار جان‌های بسیاری را نجات خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69443" target="_blank">📅 01:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69442">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=vbyedp9JIoeli7seiOgPCj-BBZKE-RnqEp4mi-dZrDSPCCM3T5Xxm9xYLgXacOHlMzM0p3hHPtPAoQa1i3WppyuPYrETEdJb6uVLcG8Ie9zhSsAMJrIWfh-1G_VHr0-IN5HjKYjvSMpQ2_8KZCNzJ_0xce_f60rc220FKQbUUVV5PJu40VKL_pnkahqb0DxeWITclGMVFeLDqFG-UjPWo3cue_keVmqUxQ8p6UmzQB5_UzMOAwL8hJ_x4wSYbnvQEumLM8RY9lPE67pYTVoxKS4d2ystZmvFrxhpKxlULAplAWP8sAmAf8p-EmVXmf7M24He_mnY7IHvswpa3vJm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992fe6ee4d.mp4?token=vbyedp9JIoeli7seiOgPCj-BBZKE-RnqEp4mi-dZrDSPCCM3T5Xxm9xYLgXacOHlMzM0p3hHPtPAoQa1i3WppyuPYrETEdJb6uVLcG8Ie9zhSsAMJrIWfh-1G_VHr0-IN5HjKYjvSMpQ2_8KZCNzJ_0xce_f60rc220FKQbUUVV5PJu40VKL_pnkahqb0DxeWITclGMVFeLDqFG-UjPWo3cue_keVmqUxQ8p6UmzQB5_UzMOAwL8hJ_x4wSYbnvQEumLM8RY9lPE67pYTVoxKS4d2ystZmvFrxhpKxlULAplAWP8sAmAf8p-EmVXmf7M24He_mnY7IHvswpa3vJm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ در مورد ایران:
عربستان سعودی، امارات متحده عربی، قطر و ایران از من خواستند که حملات را متوقف کنم.
حمله بزرگی می‌شد.
وقتی متحدان خواستند که آن را لغو کنیم، باید گفت: "خب، ببینیم چه می‌شود."
متحدان فکر می‌کنند که توافقی حاصل شده است. توافقی در مورد هرمز وجود دارد و توافقی در مورد هسته‌ای خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69442" target="_blank">📅 01:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69441">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=EhZicbPxKciMO9JPMzYp-Dj-sjG4PjBnnATRUPJrEwWjOIyOhiFF819iR_-ochQGw1K2NXuMQ9IGtIvGdcVkwHLsj5cMe_sEAsQPulCNQ1KpF4OgcfdI-BjDmijYwsSY0F29wl-O7roDZjTwfkXslTLoatwtTzWn6BgR8aM9z8bmEfl4k5mm8_WAxRnGgLFIsRZ4-8fi_klbzdvdk3hzyNYmXkfnodSVvvVtnvwDdHoMaMbxY3jAg-baDQZ6LBzhVDHFfhYzj1UP8Zj0-sz_U0YUiiCl7HPFqve-cR8PX_quJnz_rwQKjJWWBUSFNbaqbW-WoKPNVUTZ9TOtyKnWrg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/661dbe4eff.mp4?token=EhZicbPxKciMO9JPMzYp-Dj-sjG4PjBnnATRUPJrEwWjOIyOhiFF819iR_-ochQGw1K2NXuMQ9IGtIvGdcVkwHLsj5cMe_sEAsQPulCNQ1KpF4OgcfdI-BjDmijYwsSY0F29wl-O7roDZjTwfkXslTLoatwtTzWn6BgR8aM9z8bmEfl4k5mm8_WAxRnGgLFIsRZ4-8fi_klbzdvdk3hzyNYmXkfnodSVvvVtnvwDdHoMaMbxY3jAg-baDQZ6LBzhVDHFfhYzj1UP8Zj0-sz_U0YUiiCl7HPFqve-cR8PX_quJnz_rwQKjJWWBUSFNbaqbW-WoKPNVUTZ9TOtyKnWrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی وقتی می بینه دلار شده 190 هزار تومن و آب و برقم هر روز قطع میشه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69441" target="_blank">📅 00:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69440">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93362f281c.mp4?token=GRe2YKTzKF-OUaBNSh9b1aQ6lyrb9yILC3MoK8i4mTpwGxiQ1qcVQNmfnnIx02wfTbXsmFgC7WztDJ31Z1wPBthFqpQqlKhsrFiwQGFBa1zYowYGZp8AL4Xg2VftsVrX9huDAlKOAcbI6N42K7bENojj36526NNiyvznk5OGjIhIGlyVUAduRe36SLMOctezSaMpXLXJ0WghtSxJkITSUTdLHYfJBe3oSp1GXzJugLa6D3XRNFPDL8ZYW6e5IXHK_-DPp33dAgBwTHOmmdx6MiHYV71pL3biMrcW8k5u8eWqo0iw1qztCxklvhRS2VnY_6h8CkyE6Z2yXn96aNxEwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93362f281c.mp4?token=GRe2YKTzKF-OUaBNSh9b1aQ6lyrb9yILC3MoK8i4mTpwGxiQ1qcVQNmfnnIx02wfTbXsmFgC7WztDJ31Z1wPBthFqpQqlKhsrFiwQGFBa1zYowYGZp8AL4Xg2VftsVrX9huDAlKOAcbI6N42K7bENojj36526NNiyvznk5OGjIhIGlyVUAduRe36SLMOctezSaMpXLXJ0WghtSxJkITSUTdLHYfJBe3oSp1GXzJugLa6D3XRNFPDL8ZYW6e5IXHK_-DPp33dAgBwTHOmmdx6MiHYV71pL3biMrcW8k5u8eWqo0iw1qztCxklvhRS2VnY_6h8CkyE6Z2yXn96aNxEwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث سوشال:
شوت برنده در مسابقات قهرمانی باشگاه بدمنستر! از تمام کسانی که شرکت کردند، بسیار سپاسگزارم.
من با امتیاز 70 برنده شدم و از این بابت بسیار مفتخرم، زیرا برخلاف سایر شرکت‌کنندگان، زمان بسیار کمی برای تمرین دارم، زیرا تمرکزم روی مسائل دیگری است.
این را "استعداد" می‌گویند و من آن را دارم، در حالی که آنها ندارند!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69440" target="_blank">📅 23:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69439">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgRVsBarcHL0guKpVjeN9aOfF-btpHdpmV0TNrPtuVwksUyzmzMEutF0mHOjUE458cPc6IcRXJuXo7ebXKeh3wtWSqbTyrHgA_a86pWzCXyti9w-bHXKNi2nM4kh_TwEulcmTtKuxNt-yGG2uYB3bixUlAQjVXrp_G9HZd1dWiu45gSB3FtzaXTv2cUvSIiCWLf4KJShtuJCHzTkC69cAE753GjjZ_u0x9TToFbbPwcxiT9pG43S1ghOOqPRIShVa1bTm62HcajiGBmWnkVU-NUm9ClKF88jMmuQSZrpGz4ykA-lHFyITf1483Sw9FgOWATTpmYln_kkKr_zOC-cGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پزشکیان:
تفاهم نامه که امضا شد حاصل خرد جمعی اعضای شعام بود
این تفاهم نامه ثقل روابط خارجی ما توی آینده هستش و باید دشمن رو وادار کنیم بهش پایبند باشه
امنیت کشور و منطقه و هم‌پیمانان با این تفاهم نامه ارتقا پیدا میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69439" target="_blank">📅 23:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69438">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">⏺
شکار و هدف قرار دادن ۶۷ سرباز روس توسط مولتی روتورهای اوکراینی در اطراف پوکروفسک
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69438" target="_blank">📅 23:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69437">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=l76TVrjHy4ytfue_ErM1yl5glOI5DX_7sA-_-0CCoT7UtNllPKfM6CzX8jgyB8XzE7UuMV7er4gdhmGQ5fH7_pAkgnwZFr6wX1A6wofBda7KvcMj24DuTIFsOBt14FB-jLzxWqa9w_q9ZF9UaaLf8cUWY1sd8OZyRele8iPoirh4W33V89QqkcNPnsR_S0h_wsaZ0NihHef-0SHKb5pZZsis3vo0wiAaGhgkKUY3S8q9Ofvq3GRaIJ1MMU7xDERtK9Zoo0nl37BGHBm1eazA8lPo-6uY5cM5EIFfjH0KEp0mg5CyPSmAJcSiA4zRie8gGziVOzrun9iJxtlEQnqrJYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f93e085c7.mp4?token=l76TVrjHy4ytfue_ErM1yl5glOI5DX_7sA-_-0CCoT7UtNllPKfM6CzX8jgyB8XzE7UuMV7er4gdhmGQ5fH7_pAkgnwZFr6wX1A6wofBda7KvcMj24DuTIFsOBt14FB-jLzxWqa9w_q9ZF9UaaLf8cUWY1sd8OZyRele8iPoirh4W33V89QqkcNPnsR_S0h_wsaZ0NihHef-0SHKb5pZZsis3vo0wiAaGhgkKUY3S8q9Ofvq3GRaIJ1MMU7xDERtK9Zoo0nl37BGHBm1eazA8lPo-6uY5cM5EIFfjH0KEp0mg5CyPSmAJcSiA4zRie8gGziVOzrun9iJxtlEQnqrJYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
‼️
روح الله قرهی رئیس حوزه علمیه:
«وقتی ماهواره به فضا می‌فرستیم، می‌توانیم سرش را کج کنیم و خود آمریکا را بزنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69437" target="_blank">📅 22:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69436">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPlH3IyQwqH0iGqgCqy7vd5CRiNXik2tare1aNodKpRfS7BE4g-ukTqV40BxPeHsb4iWsedAjjAVrsfdFxe1_QfufUHfZgNY385WXzvUoLw3qleoalr3sx7dDbL4qy3i1PMZwuD0OtxktyzAgtWxoSRoxQxxXiB0Jh8OsEVtb9g0ZNQKW5A6guTsZHeN_HMpNTralgOmPdBBXUYSS_DaU5h8_QBYJt-iNk2dfIptl8brZTGj8R98xREQvMlJfx1sKH-NUL3hPT-F8d2uPZuMSxqpMGgvwEov6AAcgQMmDmBDuuLqHEEIhWdzwi7Y4KKIn3uvW4310GC33YLmavTkcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کان‌نیوز به نقل از یک منبع امنیتی:
رفتار دونالد ترامپ — که منجر به لغو حمله گسترده به ایران شد — به توانمندی عملیاتی آسیب می‌زند و آن را تضعیف می‌کند.
این مقام امنیتی گفت: «این دومین بار در طول یک هفته است که ایالات متحده اسرائیل را در جریان حمله‌ای برنامه‌ریزی‌شده قرار می‌دهد که می‌توانست خاورمیانه را تکان دهد، اما آن حمله در آخرین لحظه و بدون هیچ توضیحی لغو شد.»
یک منبع اسرائیلی نیز افزود: «با وجود رفتار رئیس‌جمهور ترامپ، آماده‌سازی و تدوین جدی برنامه‌های آتی دشوار است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69436" target="_blank">📅 21:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69433">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/lfS01anL5dRH6bRhYTxh52wGC_fS_zMV9fwdBZ_KdlitD_SaCYjV7SPnV4mQZueGYh-J-7KyDPrsR8iL3rW_ATu70Vcj8H4_58zlkwmdGb4KE3oXgf9pkPPqQYS-34vs00I6QyncIIDElQm56X-UOCdXuUm05c965RfZ1SlACjH4l76cNpZbOOJeGecBP9EhbCYafHB3UObwzq86ouWXgRO_RZE9tlywSa8IPMgXoP0YUGwjDqt1ECbmFMySJKS708UUu1BK6jxZbe2V8iTaFOmLqREVcsU7G8nmK-FAfwlJJX02Pd_tx9Qq7i06Icm90Eqd0uS7kJZrEiSYRoktaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=IUJKi0ByyNp6dfGil8DCSy6-6ccMKpOt6GumQYsTsBkZvTOfo8W05ZH73DzRQLfyMAE_Mq9pTTUtVIKMzBpiq-2ARw0fvyjUCZFddc_VmpCjvBJuoiDQgyNuXcYaRGwQbm6qmJGsseSuzE8PT0pjOmCLRztyErdiYPjxDuL1zCuxFS3kyrwG-mS5ZGHJ5Jd3baiGKzWJpKwr0Xzw2vnzmRCwnLud47I-JiaYVFBxLIfBBQ6E9lAw1CDwJFlrWkx8nMNjpBrLa0wtj8Tq-u1mp_4694HHCitETJG42w7LmSpGSAJV-XEUH_UhxvswMR677NpFvzfohtM_vK3M-ltw1A" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/98190fb3e2.mp4?token=IUJKi0ByyNp6dfGil8DCSy6-6ccMKpOt6GumQYsTsBkZvTOfo8W05ZH73DzRQLfyMAE_Mq9pTTUtVIKMzBpiq-2ARw0fvyjUCZFddc_VmpCjvBJuoiDQgyNuXcYaRGwQbm6qmJGsseSuzE8PT0pjOmCLRztyErdiYPjxDuL1zCuxFS3kyrwG-mS5ZGHJ5Jd3baiGKzWJpKwr0Xzw2vnzmRCwnLud47I-JiaYVFBxLIfBBQ6E9lAw1CDwJFlrWkx8nMNjpBrLa0wtj8Tq-u1mp_4694HHCitETJG42w7LmSpGSAJV-XEUH_UhxvswMR677NpFvzfohtM_vK3M-ltw1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انبار شرکت Wildberries در منطقه سمارا دچار آتش‌سوزی شد، این اتفاق پس از حمله اوکراین رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69433" target="_blank">📅 21:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69432">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5208110eae.mp4?token=jeAzgU3d61ub26a0p0M5pUrl2nav5-J0WPAs4ZGseRi-YR7WdWi1CJAYj9uVbgE75mk30wax-1KZbBLq0JrsQcJry_uG-8JuR5aKNReUVvCrYfMmsDucBdyufCd4tDEXG-qOIjODw5hJhT1ReKc6WZe8gJhTNtEt5sUHANZu1saxHOlog1a92xhX0makzFrkfCRZ8I3E-EoaTNxaZK1gJWUOWGJ8F1MJCCU9jQxz9pJefCGHLgWMit0gDZxdLElXGAPpFtDuH40_cefflZuKKhNxvNCG_fmn1fLn3VRQ2wxTR2S_2Cu-7U0RVrOl7bHayAZc-jPJjeR3MKxCPOuVKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5208110eae.mp4?token=jeAzgU3d61ub26a0p0M5pUrl2nav5-J0WPAs4ZGseRi-YR7WdWi1CJAYj9uVbgE75mk30wax-1KZbBLq0JrsQcJry_uG-8JuR5aKNReUVvCrYfMmsDucBdyufCd4tDEXG-qOIjODw5hJhT1ReKc6WZe8gJhTNtEt5sUHANZu1saxHOlog1a92xhX0makzFrkfCRZ8I3E-EoaTNxaZK1gJWUOWGJ8F1MJCCU9jQxz9pJefCGHLgWMit0gDZxdLElXGAPpFtDuH40_cefflZuKKhNxvNCG_fmn1fLn3VRQ2wxTR2S_2Cu-7U0RVrOl7bHayAZc-jPJjeR3MKxCPOuVKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی امور خارجه، اسماعیل بقایی:
مدیریت آینده تنگه هرمز توسط ایران و با مشورت عمان انجام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69432" target="_blank">📅 20:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69431">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04acf28261.mp4?token=LdZtJ2y4nfU0KYKPO95C-WzNwKaGWGwAkA8ZfHGmN685Lsp61B2sSUwAgaR_PVwraBiUB-G705xxOGasCGlWUvOW7dYN8qNgJuGrMZ7mGs_2AbPzGHsiBmdM5PhfkqN9QTZ2WxKUbAFdhTq19e_RE9QlVjZnNX8olFxML-N6FJ9e7-SsG3Cayq3jgZvzDu6j8XjxhUgxfpjGzAudVzdrAnRQTzcxVXUshMARVsk5c8FMIfNGj_zivcDM-40xhQkg1uEcxqOgcLAODr5Ur9lceWIbH20yx_LawGzktIpfWZKgJP6HUpz7mk5VE6uUVH6tUV9yprx-WruPQYO4FPTzbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04acf28261.mp4?token=LdZtJ2y4nfU0KYKPO95C-WzNwKaGWGwAkA8ZfHGmN685Lsp61B2sSUwAgaR_PVwraBiUB-G705xxOGasCGlWUvOW7dYN8qNgJuGrMZ7mGs_2AbPzGHsiBmdM5PhfkqN9QTZ2WxKUbAFdhTq19e_RE9QlVjZnNX8olFxML-N6FJ9e7-SsG3Cayq3jgZvzDu6j8XjxhUgxfpjGzAudVzdrAnRQTzcxVXUshMARVsk5c8FMIfNGj_zivcDM-40xhQkg1uEcxqOgcLAODr5Ur9lceWIbH20yx_LawGzktIpfWZKgJP6HUpz7mk5VE6uUVH6tUV9yprx-WruPQYO4FPTzbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
سخنگوی وزارت خارجه اسماعیل بقایی:
توافق ایران و عمان بر سر مسیر جدید هیچ ارتباطی با بازگشایی تنگه هرمز یا حفظ بسته بودن آن ندارد.
مسیر جنوبی از طریق تنگه هرمز با ناامن کردن منطقه و آسیب رساندن به منافع ملی ایران همراه بوده است و تهران آن را نمی‌پذیرد.
مسیر مورد توافق نه مسیر شمالی و نه مسیر جنوبی فعلی خواهد بود. در عوض، مسیر جدیدی خواهد بود که هر دو طرف متقابلاً بر سر آن توافق دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69431" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69430">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=cGT52IHc1lQwGvQS4qWTTfVUaui1kf8BuALhrL5altbeDDGMcpXLpQBDkPmtViaPXfRvyO7ltXpFbZ5AG0Ii9jLbar7XVyEDe5ucmYSTRtrVMExSVvwq-wVZu3f9OoMgiRgvr6wzqoEHLH6OTH0eH3tCdqhaPou7K_yZs6VbDcH1IPNtZbJ3y8ZhQVOT5qEswvbWXnCwP4x7PKTG8XtKPh2TJ53_2EtPj5fUA1HVv9C-zsNzYX38MThKk69AckN5yZAtq-yQ5aFAnDQSZQ4M9tUf_IeF8D9VR3eajMrairYgUoxL8EbPsh3jA23MGEEBZAOQ0bUXhOBRFzdJwpVXeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8dec97ea.mp4?token=cGT52IHc1lQwGvQS4qWTTfVUaui1kf8BuALhrL5altbeDDGMcpXLpQBDkPmtViaPXfRvyO7ltXpFbZ5AG0Ii9jLbar7XVyEDe5ucmYSTRtrVMExSVvwq-wVZu3f9OoMgiRgvr6wzqoEHLH6OTH0eH3tCdqhaPou7K_yZs6VbDcH1IPNtZbJ3y8ZhQVOT5qEswvbWXnCwP4x7PKTG8XtKPh2TJ53_2EtPj5fUA1HVv9C-zsNzYX38MThKk69AckN5yZAtq-yQ5aFAnDQSZQ4M9tUf_IeF8D9VR3eajMrairYgUoxL8EbPsh3jA23MGEEBZAOQ0bUXhOBRFzdJwpVXeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کارشناس صداسیما:
مسعود رجوی (رئیس سابق مجاهدین خلق) فرد باسواد و کتاب‌خونده‌ای بود و قطعا خیلی باهوش‌تر از رضا پهلوی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69430" target="_blank">📅 20:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69429">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=r1uWiQVIb8Mybv-uzD9bZeYRKurBMWpAe3ntC4Emn7ew20p2XHSBFvgu73Szdt4o0TtfOb32MW67TkcWh2JpYKGS4bxNd5dVjKVzyEXLthm9VKtpjbnRllucwrlK8GwfNxHRFGYOYDtO7tm6qiJztfaqrNYMmoe8lhLa7NUUWBD5CAynZRqlgbmk7PFGo5PHQQ2Pz0bOp07u_x0mI_Y_mzSQDzEWkI_vWA0yUDhVN7ooLPvNRf8xFyoHc5aIvdImC6Bn7ETxMYQE9NossF5IEJKl10etBE1tB9tcnIMqg8VJ4PSwAlo2cU83eIfc4YAJh3B6X49fEYd65_m71HIHMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d5ffc4c3.mp4?token=r1uWiQVIb8Mybv-uzD9bZeYRKurBMWpAe3ntC4Emn7ew20p2XHSBFvgu73Szdt4o0TtfOb32MW67TkcWh2JpYKGS4bxNd5dVjKVzyEXLthm9VKtpjbnRllucwrlK8GwfNxHRFGYOYDtO7tm6qiJztfaqrNYMmoe8lhLa7NUUWBD5CAynZRqlgbmk7PFGo5PHQQ2Pz0bOp07u_x0mI_Y_mzSQDzEWkI_vWA0yUDhVN7ooLPvNRf8xFyoHc5aIvdImC6Bn7ETxMYQE9NossF5IEJKl10etBE1tB9tcnIMqg8VJ4PSwAlo2cU83eIfc4YAJh3B6X49fEYd65_m71HIHMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
من یه مشکلی برام پیش اومد که گفتم نمی‌تونم در جلسه شورای دفاع در نهم اسفندماه شرکت کنم و غلامرضا رضاییان، رییس سازمان اطلاعات فراجا به جای من در جلسه شرکت کرد و کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69429" target="_blank">📅 19:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69426">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=uy4gQvIms_SCPjHbysATOr6dk_n2JRM5pj9AP-7jTSiYUGAKGNXIB499kRarpPY3lbSXeUW-nvoHH2s3IJijio2CPDsb0GQ3BFMWIjVVD_lMuW31-rn-wYr4jhJG7lQNXyLmeyn2mW54railZQPKfm2ScaTY6qTIcGcyX66SWKEdqIDOUFPrnABsWno--vTsC0m37NVlWyHVq42GssHJOr5e7idbxW2hyNka9kXUCcCpqyghMddKmxggJQHaaZKoFzN9hDZxAJdI_S-QdPlFY1b9XalEXB7hkBGiK1hCDD3G8puD10dPPZo9SBO0LG8VbFkOyaRAAYJthshkNoF9uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7637f967.mp4?token=uy4gQvIms_SCPjHbysATOr6dk_n2JRM5pj9AP-7jTSiYUGAKGNXIB499kRarpPY3lbSXeUW-nvoHH2s3IJijio2CPDsb0GQ3BFMWIjVVD_lMuW31-rn-wYr4jhJG7lQNXyLmeyn2mW54railZQPKfm2ScaTY6qTIcGcyX66SWKEdqIDOUFPrnABsWno--vTsC0m37NVlWyHVq42GssHJOr5e7idbxW2hyNka9kXUCcCpqyghMddKmxggJQHaaZKoFzN9hDZxAJdI_S-QdPlFY1b9XalEXB7hkBGiK1hCDD3G8puD10dPPZo9SBO0LG8VbFkOyaRAAYJthshkNoF9uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💋
🇮🇷
این جنده‌اینستاگرامی که خیلی ماجراش وایرال شده، یک‌شبه تصمیم گرفت بره تو آغوش حکومت و تبلیغ اربعین بکنه، چند ساعت بعدشم ازش یه ویدیو های
🔞
عجیب منتشر شد
🔗
⚠️
مشاهده تصاویر و ویدیو ها
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69426" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69425">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=AMoyatBaTyjrSFEUYQd9lTM8i8SggKC8DIjBNNDDltP-pxZQkhiSEcpFzyU6PLxUpMIgZp0iFCNc7g_vm00GBGfdpvhhKHI-XbMUkivWcUgbpkxUweaoQyXCiVYXcGOusEm0SRslBZoZXLT4BE1QQa2pxBA4jKoOG2ruxQN2DUnDYRzTM7k9ouZhFZ2BdWOM4Fey6uwSuHgdJ6vfHEH4jeulzibp3HjsGcQMbGkihYCcr0LXEC9DGMB1Tq8pLALh-vSnLcIx2g3poRunYEQDA4N3-DaWjrzePbU-f3Fl6exZ0dtq1sauf-QE-y3fpNXbshMqLsItrYrdC8Noae437Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae764e4921.mp4?token=AMoyatBaTyjrSFEUYQd9lTM8i8SggKC8DIjBNNDDltP-pxZQkhiSEcpFzyU6PLxUpMIgZp0iFCNc7g_vm00GBGfdpvhhKHI-XbMUkivWcUgbpkxUweaoQyXCiVYXcGOusEm0SRslBZoZXLT4BE1QQa2pxBA4jKoOG2ruxQN2DUnDYRzTM7k9ouZhFZ2BdWOM4Fey6uwSuHgdJ6vfHEH4jeulzibp3HjsGcQMbGkihYCcr0LXEC9DGMB1Tq8pLALh-vSnLcIx2g3poRunYEQDA4N3-DaWjrzePbU-f3Fl6exZ0dtq1sauf-QE-y3fpNXbshMqLsItrYrdC8Noae437Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند پناهیان به پزشکیان و قالیباف:
همه پیامبران را مسخره کردند؛ از تمسخر نترسید و با عظمت صحبت کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69425" target="_blank">📅 18:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69424">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🇮🇷
بیانیه سپاه پاسداران :
انتقام خون رهبر شهید و اسماعیل هنیه اجتناب ناپذیره
پاسخ این جنایت بشدت سخت و قاطع و سخت گیرانه خواهد بود
توطئه خلع سلاح حماس به نتیجه نخواهد رسید و از همین الان شکست خورده بدانید
دنیا بداند اراده ضد صهیونیستی ادامه دار خواهد بود و پیروزی نهایی فلسطین خیلی نزدیک است
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69424" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69423">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=prkz392MDdyzxNtOzh6Ntf6uXcMyttTK8P1Jxz8jB8VRTkejnPBq2BgUUWufKHCi86_WAOI7HQRLVzsCdMcZugUpDPJHckA1hK3BGbBfkHAAELvnqoxR71qygzxMfG9QUbhiqNY05DSDi9h1bjJCLmgfyuOM6I0HiUIe45hUGJs9DV7IW4W0wDrE4hfQ8i7kL6hLzSm9h7Y8Z0_gM7KBVMovTNB0_8KU0M-vbCXiWxdqw45kZedkP8WmNNgZyKyzCWMhNqzYovxnMdP9DZGBMp5OsQi0zJO6kl86TbGqj4ZeL5z30xz0QM_IpG8CLjjKvRX3UgSLFHdngRzaaEjbGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc039adc5b.mp4?token=prkz392MDdyzxNtOzh6Ntf6uXcMyttTK8P1Jxz8jB8VRTkejnPBq2BgUUWufKHCi86_WAOI7HQRLVzsCdMcZugUpDPJHckA1hK3BGbBfkHAAELvnqoxR71qygzxMfG9QUbhiqNY05DSDi9h1bjJCLmgfyuOM6I0HiUIe45hUGJs9DV7IW4W0wDrE4hfQ8i7kL6hLzSm9h7Y8Z0_gM7KBVMovTNB0_8KU0M-vbCXiWxdqw45kZedkP8WmNNgZyKyzCWMhNqzYovxnMdP9DZGBMp5OsQi0zJO6kl86TbGqj4ZeL5z30xz0QM_IpG8CLjjKvRX3UgSLFHdngRzaaEjbGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو هلیکوپتر آتش‌نشانی در حین مبارزه با آتش‌سوزی جنگلی در نزدیکی پساتا، یونان، در هوا با هم برخورد کرده و سقوط کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69423" target="_blank">📅 17:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69422">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=nT6V2m_3IYqUiZU4fq6WpfpZQlqAHJ_NMF97NDWX2NDk_eF3BCs4PUBukjklXNTfF7OVq_c6qYGhiDVGZlhsSA1DC_IrabIBXJntJJJBwRDIKKMr8xeiwwXZq91cgtxEUKCrxi4YS-4k7AQQPXIkkd23VVi2NgXmdPGB-2WomwhhZ3qXHZV6UtmAbERYxPkQx7QV-d_lGFUEiowAxUs7HtVhJGdSVPrPl1aCwgCm4PkGJv-7vah_gbjWMan0d50BwG_xpBwhU1NKREDb5t5ELfuGP6hlUHJyXPUyo0xn6lG64xdtzeuI0pjmvaTxBtpAL5BGPnfs3DVN5iweUuYr0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bef1baf0f6.mp4?token=nT6V2m_3IYqUiZU4fq6WpfpZQlqAHJ_NMF97NDWX2NDk_eF3BCs4PUBukjklXNTfF7OVq_c6qYGhiDVGZlhsSA1DC_IrabIBXJntJJJBwRDIKKMr8xeiwwXZq91cgtxEUKCrxi4YS-4k7AQQPXIkkd23VVi2NgXmdPGB-2WomwhhZ3qXHZV6UtmAbERYxPkQx7QV-d_lGFUEiowAxUs7HtVhJGdSVPrPl1aCwgCm4PkGJv-7vah_gbjWMan0d50BwG_xpBwhU1NKREDb5t5ELfuGP6hlUHJyXPUyo0xn6lG64xdtzeuI0pjmvaTxBtpAL5BGPnfs3DVN5iweUuYr0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی اینو ببینید توی پخش‌زنده صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69422" target="_blank">📅 17:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69421">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCNxpAwXLcB_XBGKJ7dfHcIPb3pZzk1DA1t3HE6685mL6EtTItRwEs6Ih58beQqhabHeG8yqmpkrW8o6p6Wv5P407LnRRjPHclHB9vglNyNkSCFXHjhpAfNifTRDIjlw5lEp9fpvJXQTMbYuhMe7qLnMzoQALUwP5_D4vTdcjY-CUkciRqCDp3rJYDqKcsVXOHpA5qjqIp27PM31nkDoMFUOSy0ZaVDz14bUGw-oIOEDMmDLEBIPYXhvj6n6dXyyGcRocRz3oXtYxUSwGKwC9QPMqqZceGv0Zxsng784ghhu9GuqqU4ggiT8f3E-qNO7EvFCH8QuOAfWoWLHv0U2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
نیویورک پست:به گفته منابع آگاه، در حالی که رهبران اعتراضات در تلاش برای دستیابی به سلاح هستند، انقلاب ایران ممکن است «هر لحظه» رخ دهد.
چهره‌های مخالف حکومت در تهران به نشریه «پست» گفتند که خیابان‌های ایران به دلیل اعدام‌های در ملأعام، فروپاشی اقتصادی و جنگی که بیش از پنج ماه است ادامه دارد، به مرز انفجار رسیده‌اند.
یکی از رهبران اعتراضات با اشاره به سرکوب بی‌رحمانه ماه ژانویه توسط رژیم — که به گفته رئیس‌جمهور ترامپ منجر به کشته شدن ۵۲ هزار نفر شد — گفت: «انقلاب ممکن است هر لحظه رخ دهد؛ مردم خواهان انتقام هستند.»
یک روزنامه‌نگار مستقلِ فعال در جریان‌های زیرزمینی ایران گفت که تدارکات برای خیزش بعدی هم‌اکنون در حال انجام است و فعالانی از تمامی اقشار جامعه مصمم‌اند تا ضربه‌ای نهایی و تعیین‌کننده به رژیم وارد کنند.
این روزنامه‌نگار گفت: «ما در حال بررسی اعتراضات ماه ژانویه و تشخیص این نکته هستیم که چه تاکتیک‌هایی مؤثر بوده‌اند و کدام‌یک نه؛ همچنین نقشه‌ها را تحلیل می‌کنیم تا امن‌ترین و خطرناک‌ترین مناطق برای تجمع را شناسایی کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69421" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69420">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V3zrBFfxMNXpYM7-BgsT-JOUuiIaFsicrnPFVzA20B2gYUkFe7coV-yFlLE8biRvboPbV7TD6N13FEXaJ5WkbTjEXMkgBXwShlTzdg5ixeWsZJCyJkam5ufDIpVhtv1MVrVrqcOXrLcb2wachF43vLhSxqr_SOPGUqEKklHO70cYfWLnbMOMnDZ1l4qwZuHgMlMbFsiXVzByRT_PmjHlZvEkszTv-JLmabqsUXVVBOhtYhqB4xr5JzOuAXj5YgJk4q5ZwobAEROFmeRZvya38URbREeO0JPcEGyMqj5RNOEUIkrvA0K7QFD5HejZ0ZbZxwXfysHyJSJVD5ofhTae4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
صفحه فارسی وزارت خارجه اسرائیل:
هفته خوبی از اسرائیل برای شما آرزومندیم!
💦
اسرائیل داغ‌تر از همیشه به نظر می‌رسد... و ما فقط در مورد آب و هوا صحبت نمی‌کنیم
😉
🇮🇱
☀️
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69420" target="_blank">📅 16:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69419">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=tdL14oH4S9jMgNg7hx9B5534Qs0O3Qg3ieMrr_lm5LBh3k8Q9BtA8APl93JNMKV3JYTfFalHbBdBLx-01HR0iBAqIfL9Fu3kMdIXWWhKcSlRvIxvgQwCjoIwagRVJqwY35Ph3Aly9Z-xreTZ5sn2XpVSEn7RYsqt9ZcLrU-eVg-49_UEYfYz-UXMKRR97U7yda1PSZDj5eY6J0v53M_7OIlaWnL4Cao-pdabss8Ge0nD3ZDBF7LgExSVLcjmtAh2LaZJATzjkAyVBOeUy-X9sywgK9OA9vdtWVLluaj2HW1J7tpv8MyheP21FvdT50GjzhTRRLoalNPBmrbWitC3ww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6e5661f181.mp4?token=tdL14oH4S9jMgNg7hx9B5534Qs0O3Qg3ieMrr_lm5LBh3k8Q9BtA8APl93JNMKV3JYTfFalHbBdBLx-01HR0iBAqIfL9Fu3kMdIXWWhKcSlRvIxvgQwCjoIwagRVJqwY35Ph3Aly9Z-xreTZ5sn2XpVSEn7RYsqt9ZcLrU-eVg-49_UEYfYz-UXMKRR97U7yda1PSZDj5eY6J0v53M_7OIlaWnL4Cao-pdabss8Ge0nD3ZDBF7LgExSVLcjmtAh2LaZJATzjkAyVBOeUy-X9sywgK9OA9vdtWVLluaj2HW1J7tpv8MyheP21FvdT50GjzhTRRLoalNPBmrbWitC3ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از نیروهای سرکوبگر: تا تهش پای حکومت وایسادیم، بازم بیاین بیرون بهتون رحم نمی کنیم!
چون داریم دستور خدا رو انجام میدیم، شما اصلا کسی نیستین جلوی جمهوری اسلامی وایسین.
کل دنیا هم جمع بشن نمیتونن کاری کنن، پاینده جمهوری اسلامی!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69419" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69418">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f215b551.mp4?token=hs4ij3rds_ip4XHS6IdP7TcOeicxOQJr8jdVtbzd1-TufGZSdR0RPs5XBzds3s6nBmFvcliQShqhy95O9DP1JB2Drg1jL84naDtGL_wwDd2J_n08-jKjIeVpppuPrDYL6YA9ccEceHupdlB2F7VUZFF20WKEWNYdMiNsSii4xIrM6kP6W1n9AZMRHDzYON0jLPh7czT6V-iuCx60iHgAU76ZjHI4rOkc51f9nFIKjJoJstsPI1DP4mBgcTDaJogw1BvkmPg0WfKIQ60zzNMbOIkGfM0TIkfMDSSbLYs9UVFWzqCLAMUf9TJ0vy0pCXVNuSK3QYvoR7TmHelaN6p7nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f215b551.mp4?token=hs4ij3rds_ip4XHS6IdP7TcOeicxOQJr8jdVtbzd1-TufGZSdR0RPs5XBzds3s6nBmFvcliQShqhy95O9DP1JB2Drg1jL84naDtGL_wwDd2J_n08-jKjIeVpppuPrDYL6YA9ccEceHupdlB2F7VUZFF20WKEWNYdMiNsSii4xIrM6kP6W1n9AZMRHDzYON0jLPh7czT6V-iuCx60iHgAU76ZjHI4rOkc51f9nFIKjJoJstsPI1DP4mBgcTDaJogw1BvkmPg0WfKIQ60zzNMbOIkGfM0TIkfMDSSbLYs9UVFWzqCLAMUf9TJ0vy0pCXVNuSK3QYvoR7TmHelaN6p7nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدئو با اختلاف زیاد عجیب‌ترین و دارک ترین چیزیه که تا آخر هفته می‌تونید ببینید؛
هربار یکی از این خانواده رو دنبال کنید تا متوجه عمقِ نفهمیدن بشید...
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69418" target="_blank">📅 15:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69417">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/90d8743494.mp4?token=PbvPhjyazDlZ58WVeGTzwyF4TZXo9preiAw8FPezxjnrXfQ0J3UkgVbOr3vXuVplV9zFAU4REdsMvu1e4jpL-YLUjPyyVyi4RQhhpEjhEg13sQwiFPvVqnbwofAR00geJ9aI84NiRlwY_gclOdwOj4oAq1Wpr7NLZO4zbFJZrBJt4vOo6KkaaX5GxOHGMtrHB5tncsRhh3nWg_finlwDUwF5Jk9GhvpNrdTFtCoD7wgcc4cLNSN8MfdVX7kkof1za1Hm4DDgYZj3GchFymJ5yQngfclvFnjZFoEATo_g7mXVZ6lhMftQhB0f6sdyimyC6bPs9AvBRibiy5cIynYdWw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/90d8743494.mp4?token=PbvPhjyazDlZ58WVeGTzwyF4TZXo9preiAw8FPezxjnrXfQ0J3UkgVbOr3vXuVplV9zFAU4REdsMvu1e4jpL-YLUjPyyVyi4RQhhpEjhEg13sQwiFPvVqnbwofAR00geJ9aI84NiRlwY_gclOdwOj4oAq1Wpr7NLZO4zbFJZrBJt4vOo6KkaaX5GxOHGMtrHB5tncsRhh3nWg_finlwDUwF5Jk9GhvpNrdTFtCoD7wgcc4cLNSN8MfdVX7kkof1za1Hm4DDgYZj3GchFymJ5yQngfclvFnjZFoEATo_g7mXVZ6lhMftQhB0f6sdyimyC6bPs9AvBRibiy5cIynYdWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
بر اساس تصاویر ماهواره‌ای، پایگاه هوایی شیخ عیسی در بحرین که مورد استفاده نیروهای آمریکایی است، اخیراً تخلیه شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69417" target="_blank">📅 15:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69416">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=V248Ptx5YL9XDFEhRI4Tjp2L00YKqEWnFv-_WEbdzyTYQXh7fX544BSSW1VVDmRmzABDNVpfUe6umu81kHY13UkAb2YrlWRCp8Nq858nGgxolbUd1Hhs67bGEOASyn6N6CrrfBZWM9-LEd_DJBCqHgrhGabtCZOVebux2R_GK0FNw5hHcBr0WsVmD673HpofxVLFvMF4pCk9D6imHSiiy3som5SrWt_T2VxdS57EVrvhkoCV_6AKTp0As6Y1Za_NyMpNps8aUgcRcTjcuCdKbCoRBliPnOpfWkSuOKm5ekL-SJTFHIVpUspBH1kbr3M5sKNY4Q3io8zGk7bpNQhTPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba4d1f7356.mp4?token=V248Ptx5YL9XDFEhRI4Tjp2L00YKqEWnFv-_WEbdzyTYQXh7fX544BSSW1VVDmRmzABDNVpfUe6umu81kHY13UkAb2YrlWRCp8Nq858nGgxolbUd1Hhs67bGEOASyn6N6CrrfBZWM9-LEd_DJBCqHgrhGabtCZOVebux2R_GK0FNw5hHcBr0WsVmD673HpofxVLFvMF4pCk9D6imHSiiy3som5SrWt_T2VxdS57EVrvhkoCV_6AKTp0As6Y1Za_NyMpNps8aUgcRcTjcuCdKbCoRBliPnOpfWkSuOKm5ekL-SJTFHIVpUspBH1kbr3M5sKNY4Q3io8zGk7bpNQhTPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر مارو خندوندی حاج اقا دارم پاره میشم
👅
👅
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69416" target="_blank">📅 14:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69415">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇮🇱
بنسالل اسموتریچ، وزیر دارایی اسرائیل:
رژیم ایران در جریان جنگ سقوط نخواهد کرد.
مردم ایران در شرایطی که هواپیماهای اسرائیلی و آمریکایی بر فراز آسمانشان در پرواز بودند، به خیابان‌ها نمی‌آمدند؛ چرا که نمی‌خواستند در نظر دیگران، همدست دشمن به نظر برسند.
تأکید اصلی باید بر این موارد باشد: اقتصاد، اقتصاد، اقتصاد و باز هم اقتصاد. این همان عاملی است که در نهایت موجب سقوط رژیم خواهد شد.
به گمان من، رژیم ممکن است به نقطه‌ای برسد که شهروندان عادی احساس کنند دیگر چیزی برای از دست دادن ندارند.
وقتی چنین وضعیتی پیش بیاید، ترس دیگر مانعی نخواهد بود؛ آنگاه مردم به خیابان‌ها می‌آیند، قیام می‌کنند و رژیم را سرنگون می‌سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69415" target="_blank">📅 13:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69414">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
خبرگزاری فارس، وابسته به سپاه:
گزارش‌های حاکی از موافقت ایران با بازگشایی تنگه هرمز نادرست است و هیچ تغییری در سیاست تهران ایجاد نشده.
منابع نظامی گفته‌اند این آبراه راهبردی همچنان بسته است و عبور از آن نیازمند مجوز صریح و هماهنگی با نیروی دریایی سپاه پاسداران است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69414" target="_blank">📅 12:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69413">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835653bd72.mp4?token=dwjGDu_yiVJGUgWmfz2ZbnARoaXwGyST3tNd1bRlGqLcCgWyfSyGGZvGaU210w36BNjft6ppa96UwMKyQugGgFhxlx2oEqOHOnBhHURRgSr4F8Fbfk0ax8F3U6PfhyZ87bJ4VVUsLZ3ZP0LSyeZmBdeE7hA4qkrd2N21lfRuumtXWAURE4HxeCGjJrMzUX60eNxsIGuAAkeo49SjYYUI_jlcQlHzcwLMragaoUXvEjLOcvcB_7EgMJADxuJfz6oHBeCU3_JGqYphDZFgNrlUEsFQ3tgnO2gVpFmrG6HozroqZ8tMInQfZ03RwDMi4Oy2ko84svdVj4pzeYS4hhocmqe4xXdntx0fuGghiCJtEuulA0wys4xTNDgrULdEcEe0MbmFgOcg8rqXLvfTERTvz1tCkGYEUY373XYwMK_4SrEMgAVt-SkYnlJBqJP5Biti9dpEvT43AOpJpTzuEJt7GQ8GAHYlhaaf4A6lh502vHU8xBs1kacupwu-LEfVC85jKkrW_cRe57YgnZY9HMigDPO-bWuPQWqmbWW3Sk77oV-iVHxxibhUPp0HnSesF9DRLPg_IgH6w7YgqOUwkAU4UOQh2t7uFe3lzY5r_vC-RnKM9PQqie06QM8XpJQYLRvLw6qd4kXuTRE_XCNNZsb4Mg02vMHV_q6HzozLSpAU8YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835653bd72.mp4?token=dwjGDu_yiVJGUgWmfz2ZbnARoaXwGyST3tNd1bRlGqLcCgWyfSyGGZvGaU210w36BNjft6ppa96UwMKyQugGgFhxlx2oEqOHOnBhHURRgSr4F8Fbfk0ax8F3U6PfhyZ87bJ4VVUsLZ3ZP0LSyeZmBdeE7hA4qkrd2N21lfRuumtXWAURE4HxeCGjJrMzUX60eNxsIGuAAkeo49SjYYUI_jlcQlHzcwLMragaoUXvEjLOcvcB_7EgMJADxuJfz6oHBeCU3_JGqYphDZFgNrlUEsFQ3tgnO2gVpFmrG6HozroqZ8tMInQfZ03RwDMi4Oy2ko84svdVj4pzeYS4hhocmqe4xXdntx0fuGghiCJtEuulA0wys4xTNDgrULdEcEe0MbmFgOcg8rqXLvfTERTvz1tCkGYEUY373XYwMK_4SrEMgAVt-SkYnlJBqJP5Biti9dpEvT43AOpJpTzuEJt7GQ8GAHYlhaaf4A6lh502vHU8xBs1kacupwu-LEfVC85jKkrW_cRe57YgnZY9HMigDPO-bWuPQWqmbWW3Sk77oV-iVHxxibhUPp0HnSesF9DRLPg_IgH6w7YgqOUwkAU4UOQh2t7uFe3lzY5r_vC-RnKM9PQqie06QM8XpJQYLRvLw6qd4kXuTRE_XCNNZsb4Mg02vMHV_q6HzozLSpAU8YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گزارش روزنامه همشهری از دلایل عدم انتشار صدای مجتبی خامنه‌ای :
از طریق صدا میتونن پیدا بکنن چون هر فضای بسته امضای صوتی منحصر به فردی داره و از بازتاب صدا از طریق فرش و دیوار میتونن مکان رو تشخیص بدن و ارتفاع اتاق و فاصله گوینده رو از محل بازتاب رو پیدا بکنن
همچنین از طریق تحلیل شبکه برق میتونن ردیابی بکنن چون همهمه ضعیف الکترومغناطیسی در پس زمینه صدا ضبط میشه و سرویس های اطلاعاتی میتونن از طریق شبکه های اتصال برقی مکان رو ردیابی بکنن
هر میکروفون و دستگاه ضبط اثر متفاوت داره و مختص خود دستگاهه مثل اثر انگشت خود شخص لذا از طریق ردیابی دستگاه میتونن مکان رو پیدا بکنن
صدای پس زمینه مثل خنک کننده ها یا ژنراتور ها و حتی توی مکان باز صدای ترافیک ها و صدای محیط و نوع حشرات و پرندگان میتونن محل جغرافیایی رو لو بدن
😳
😳
ویس ابعاد فیزیکی نای دهان و مجرای صوتی رو نشون میده و حتی فیلتر هم باشه با دستگاه هایی میشه ردیابی کرد و تشخیص داد طرف زنده باشه محل حضورش کجاست
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/69413" target="_blank">📅 12:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69412">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇺🇸
ویدیو ای که صفحه رسمی وزارت جنگ آمریکا به تازگی منتشر کرده
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69412" target="_blank">📅 11:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69411">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=DGYNxIRNfAlYXEhzYTOTezo6kDW1008TLmPJ_8ee1EnQH9d1ntUOqHBxa4IF7ApNomcw3aVOCi3_3OcoYIHMgry9NePE-0iJjSnzuM1wgVDSZ-p2vAbfOVmTYLywDgQ9x1A4ZVOpnwGGskkC62C1rbzWvzASTekFeQ_kPE25aToLMerSL-URUGs8GtVfsWqBx9Cb_BH0DILMWNOytXm5KJQzH9AB3XFYlea5B563XwfxjFZyC-EHi5BJ5yOwHIE1f50sXaUwNQoflcL_HFOx8ylIDE-MJvmaWKYUSelbFr3mAGDtdLv5a72jsShF23XPaUduKUaYfB_EEY0CmO3dUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb1d460275.mp4?token=DGYNxIRNfAlYXEhzYTOTezo6kDW1008TLmPJ_8ee1EnQH9d1ntUOqHBxa4IF7ApNomcw3aVOCi3_3OcoYIHMgry9NePE-0iJjSnzuM1wgVDSZ-p2vAbfOVmTYLywDgQ9x1A4ZVOpnwGGskkC62C1rbzWvzASTekFeQ_kPE25aToLMerSL-URUGs8GtVfsWqBx9Cb_BH0DILMWNOytXm5KJQzH9AB3XFYlea5B563XwfxjFZyC-EHi5BJ5yOwHIE1f50sXaUwNQoflcL_HFOx8ylIDE-MJvmaWKYUSelbFr3mAGDtdLv5a72jsShF23XPaUduKUaYfB_EEY0CmO3dUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش پزشکیان به تاخیر ۱۰ روزه در  پرداخت حقوق اعضای هیئت علمی دانشگاه‌ها:
این واقعاً قابل قبول نیست، کاری کنید که اساتید بیش از این ناراضی نشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69411" target="_blank">📅 11:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69410">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇮🇱
کانال۱۲ اسرائیل:
عراقچی، وزیر امور خارجه ایران، شبانه با یک مصالحه میان قطر و آمریکا برای بازگشایی تنگه هرمز موافقت کرد؛ اقدامی که باعث شد دونالد ترامپ، رئیس‌جمهور آمریکا، حملات تلافی‌جویانه برنامه‌ریزی‌شده را لغو کند.
بر اساس این طرح، کشتی‌های عازم خلیج فارس از طریق آب‌های سرزمینی ایران وارد و از مسیر آب‌های عمان خارج خواهند شد؛ هرچند عمان خواستار تأیید رسمی این موضوع شده است که سپاه پاسداران از این توافق حمایت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69410" target="_blank">📅 11:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69409">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66dc919056.mp4?token=muxHKprKTfD58C-PoDEh9kOJtmRpyqxyevL5wT5YVfq-rcef__T7jw3AtLT_mu-5NwJ6OrtFeLZ6kqlqL8WUBMy5oPxny6Drke1rfYCbeBePAV8f0WVIzwFA5P2XLSYsLGhRNWwS6WK_l1eitGc-9MOzw2yOBLTR2Ay3y8CYYyzCZirMLt3cPAdNjhqZV34Kw1t6HYj-D4bV7AfTBhaR51J3KZTTjOltc6ZExfhfpETD0OaUJyp0EbLGNC8UA_BOWkerfkDRlhWAFpT0b-gOwccugYK68e88yj0Kpvt6v-TzyI9-6kT867---IWMraQywOYR_nBsUuN-Rdl8aw5K4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66dc919056.mp4?token=muxHKprKTfD58C-PoDEh9kOJtmRpyqxyevL5wT5YVfq-rcef__T7jw3AtLT_mu-5NwJ6OrtFeLZ6kqlqL8WUBMy5oPxny6Drke1rfYCbeBePAV8f0WVIzwFA5P2XLSYsLGhRNWwS6WK_l1eitGc-9MOzw2yOBLTR2Ay3y8CYYyzCZirMLt3cPAdNjhqZV34Kw1t6HYj-D4bV7AfTBhaR51J3KZTTjOltc6ZExfhfpETD0OaUJyp0EbLGNC8UA_BOWkerfkDRlhWAFpT0b-gOwccugYK68e88yj0Kpvt6v-TzyI9-6kT867---IWMraQywOYR_nBsUuN-Rdl8aw5K4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
با این حال، تغییر رژیم هرگز هدف اصلی نبوده است؛ هدف، خلع سلاح هسته‌ای بوده است. آیا می‌توان یکی را بدون دیگری داشت؟
🇺🇸
مارکو روبیو:
هرکاری که توی خاورمیانه و جهان انجام دادیم کسی مانع ما نشده و موفقیت بدست آوردیم
رژیم باید تغییر بکنه شما شاید تغییر رژیم نداشته باشید ولی باید اینا تغییر بکنه
اونا میخان
انقلابشون رو به کل دنیا صادر بکنن و باید این تغییر پیدا بکنه
ایران تابحال با رئیس جمهوری مثل ترامپ که مرد عمل هست رو به رو نشده
اونا هنوزم موشک و پهپاد دارن میتونن صدمه بزنن ولی خب سپری ندارن پشتش قایم بشن
از روی قدرت باهاشون مذاکره میکنیم نه ضعف
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/69409" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69408">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=DBg8kOOK1Qr2zFZO5xXIl8mA8I8RyPFoMDUKyHoPZhNTRz9G-eBcMGY3faPlVSKIdjcLA5jIsqw-dX_xlMvLHKUCHXRdZgF_4PkxUT_Cj8IQoUJK-4aW-IKjS9UTAKXpAwS1TUdcNbtg9DKwarrDP3d8REe15nLOOa_5gnZN_ZT1WEFTEwEMu_xNgRgS82rYsf1awll3js4ERQaRNLUOEnKc5wtve4GpIbMpZTp-1bl2p2LUEoGIn42zIU2HCHp-TQi6HMY3SyOoY78dFEMbG_wE77JngYVfw7EbEJBdAmtrLDRFlEbaBW-TqbZSKhJSuBSq3CdIu6r4VmUuSpwGXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb72a3070d.mp4?token=DBg8kOOK1Qr2zFZO5xXIl8mA8I8RyPFoMDUKyHoPZhNTRz9G-eBcMGY3faPlVSKIdjcLA5jIsqw-dX_xlMvLHKUCHXRdZgF_4PkxUT_Cj8IQoUJK-4aW-IKjS9UTAKXpAwS1TUdcNbtg9DKwarrDP3d8REe15nLOOa_5gnZN_ZT1WEFTEwEMu_xNgRgS82rYsf1awll3js4ERQaRNLUOEnKc5wtve4GpIbMpZTp-1bl2p2LUEoGIn42zIU2HCHp-TQi6HMY3SyOoY78dFEMbG_wE77JngYVfw7EbEJBdAmtrLDRFlEbaBW-TqbZSKhJSuBSq3CdIu6r4VmUuSpwGXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مرادویسی، تحلیلگر ارشد اینترنشنال:هدف‌های احتمالی آمریکا تو جنگ جدید میتونه شامل این موارد بشه:
1. مراکز نظامی سپاه تو جنوب کشور
2. شهرهای موشکی و پهپادی تو عمق خاک ایران
3. تاسیسات هسته‌ای "کوه کلنگ"
4. مراکز نظامی سراسر کشور
5. سامانه‌های پدافندی و راداری
6. پایگاه‌های هوایی ارتش
7. مراکز و نهادهای حکومتی
8. ساختارهای سرکوب (سپاه، بسیج و نیروی انتظامی)
9. مقامات و فرماندهان ارشد باقی‌مونده
10. مکان‌های نمادین مثل صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/69408" target="_blank">📅 09:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69407">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=sHDu8EZbOpIVhjJ5j0CDGQa7H29oaGyKVlZZLowaiX6JY9Rxwf3dn0PeHMsL4ZhijG1k4DYJev_zT_aY_AX2GNJK0QcqWTvlJoEntXjG7THXxe7SHHi4wDumCGeai6vC9GeXRjJNTYpYQqSZBhokLSF-6aV-JAEZ4DCwMG3q0wN3u-ITbyNEwRYqi63uOCJ_NAgN4NQ3Cy7FBJ0UG46AwPjhtunlfLBSZ27h84gTMe25PLwvUb8EJhYF2ackKbPEFJJtieB16UWZEU0xG4z1jwCghcPwbFEqzrdrh41GtDy3Xz4luQ_3ZJ81oHLSw-bzjCB0b3xrSr_GDqt1JK8Pvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbd0e326f.mp4?token=sHDu8EZbOpIVhjJ5j0CDGQa7H29oaGyKVlZZLowaiX6JY9Rxwf3dn0PeHMsL4ZhijG1k4DYJev_zT_aY_AX2GNJK0QcqWTvlJoEntXjG7THXxe7SHHi4wDumCGeai6vC9GeXRjJNTYpYQqSZBhokLSF-6aV-JAEZ4DCwMG3q0wN3u-ITbyNEwRYqi63uOCJ_NAgN4NQ3Cy7FBJ0UG46AwPjhtunlfLBSZ27h84gTMe25PLwvUb8EJhYF2ackKbPEFJJtieB16UWZEU0xG4z1jwCghcPwbFEqzrdrh41GtDy3Xz4luQ_3ZJ81oHLSw-bzjCB0b3xrSr_GDqt1JK8Pvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
حاکم بحرین:
حضرت محمد (ص) پس از قرن ها تاریکی در ایران به آن عمق روحی، انسانی و معرفتی بخشید، بخاطر تشکر از این کار حداقل دیگه به بحرین حمله نکنید.
@News_Hut</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/news_hut/69407" target="_blank">📅 09:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69406">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uws_PEl_b6KF-k3BAA8YkgoxAP1f7HL62IREjubul4maCccuOYS-bgOWqjvVgsB94tlezb3qCldaELJx3EEKLgjwiMbEHhuZnbep6xZ3oy3gZf1yvuW2dmC9kB1qSwiGxYCTtxXJlagbCyRbbn0tBV3h1ipJzp9a84TWbeM1qRhCUDqEKUA--xaEKqybpYxeW3HbnGqH9aqxZcEWlyFYbXcZFgG3JcCl7kMofj2ocoQWITtxY_wUri1J0fHUva3Ikztg7-27yrCGgwEzqjZvZk8OMBgB7v__DV1Iy1milvmbfOcsX-YNQeS1seBNl5FVGZSQLIMgcHWRsqnu3XIrMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: حمله رو کنسل کردم
!
ایالات متحده آمریکا آماده و مجهز به سلاح است تا علیه جمهوری اسلامی ایران، در سطوحی از ترور نظامی، قدرت و صلابت که از زمان جنگ جهانی دوم دیده نشده است، اقدام کند. با وجود این، ایران و سایر کشورهای خاورمیانه از ما خواسته‌اند که هرگونه حمله‌ای را در چارچوب توافق‌نامه‌ای که مورد توافق قرار گرفته است، متوقف کنیم. این شامل بازگشایی فوری، کامل و تمام‌عیار تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران می‌شود. بر اساس این درخواست، من برای منافع آینده جهان و همچنین بقای یک ایران موفق و مرفه، موافقت کرده‌ام که حمله را لغو کنم، مشروط بر اینکه بتوانم به سرعت به توافق‌نامه‌ای دست یابم. کشور اسرائیل در این تعهد به من می‌پیوندد. همه دست به کار شوید و آن را انجام دهید. از توجه شما به این موضوع متشکرم! رئیس جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/news_hut/69406" target="_blank">📅 06:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69405">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exll3jdY0-Z0zSmpkLVFV4aPQ45NPLxAe8D-o3MlCPIEj1PdV9r9t7LVup9rbjOajNIeXp0zqWdoOFU3XJaA-ItNOmAQAr0BOUpewDviD9sY8A-yzPoX13Io9hqFK_JtUHAEng3bOpPMvQNPpp7TT3jTzsK3JusO7Pr-dwkGIHb0Euadru_Z_970bkzQgtC4fN6T6ULiTKdLRZtod-dxaMt4FDZUcRFiBNyXNBge3WxCGzpn7s8wocNrmxHSaUg4bHTPJUt2NSKO91A69ojhsHQph1oxm791nJawO5GWvKIBeyARhI8eVQgTFzapq-qC7kTznwU6ALB1-esjSrymug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این خبر فیکه و ترامپ چیزی نگفته.
#hjAly‌</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/69405" target="_blank">📅 02:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69404">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=thz5lpNEoxYgJuXJjZKr_PL8WNDx6onEXZ45Z2rGWeQkgyHu64saNy8bsbQQFTc2OorqY8aYTmqV1io5G1bcXvk-m4bwQ7uvPxkrCqIg-M2l4ok8Ed4SsKceVid2rmQLJPZYtnecG0a8_Gz45KMj6EvxESZUEkkiyrx1SUmam5jcrGfXf1KHpza86RMOPvhP5ePj7AAvM_ASzQoQgEhL288kivlJpOoATo_0oikmIZo5CxkluhV7LY5LhvZ2NUZpHetRMZrJcg4fGJ4T90HGxPekuKKUrCGd-GxZPZvDaaMhDAAEfjs5IniMiuAGHcJ7wWOGgGEp2VwCZVD1MZlyBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6db9d071b.mp4?token=thz5lpNEoxYgJuXJjZKr_PL8WNDx6onEXZ45Z2rGWeQkgyHu64saNy8bsbQQFTc2OorqY8aYTmqV1io5G1bcXvk-m4bwQ7uvPxkrCqIg-M2l4ok8Ed4SsKceVid2rmQLJPZYtnecG0a8_Gz45KMj6EvxESZUEkkiyrx1SUmam5jcrGfXf1KHpza86RMOPvhP5ePj7AAvM_ASzQoQgEhL288kivlJpOoATo_0oikmIZo5CxkluhV7LY5LhvZ2NUZpHetRMZrJcg4fGJ4T90HGxPekuKKUrCGd-GxZPZvDaaMhDAAEfjs5IniMiuAGHcJ7wWOGgGEp2VwCZVD1MZlyBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان سلیمانیه
@News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/69404" target="_blank">📅 02:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69403">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=DzX0xnMFlaN_S0TGmEB8s1-45YaF1UuqTaswq5UahpKxAGnk_1Bba92YYzrUeh0XISlbU6wRqFY_LtfbexnkqxfWH8CWJOBSxF41HYp44iWjz2X9V4l3PGFURf-6TeWpIhRRXX7uyh9FcCB_AMOgRdviLtbIQITRlQC-s1LgSZ3_Kg4ldBdeRkMQ6gwZjfTfS_ScSraP7HGpe21vAC10sxTr_u1iccCYxqjL0Y-ggFTzs9D-kJcskCj8Q4VB7REGkFZt8LmERWsqR83_vzsxd6fBhZvmVmtrV9r3gIfgpcUlW06BeTIXUUf-w276EIigGGebezDrmdzp5CkpRrPDgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5cdd81f13.mp4?token=DzX0xnMFlaN_S0TGmEB8s1-45YaF1UuqTaswq5UahpKxAGnk_1Bba92YYzrUeh0XISlbU6wRqFY_LtfbexnkqxfWH8CWJOBSxF41HYp44iWjz2X9V4l3PGFURf-6TeWpIhRRXX7uyh9FcCB_AMOgRdviLtbIQITRlQC-s1LgSZ3_Kg4ldBdeRkMQ6gwZjfTfS_ScSraP7HGpe21vAC10sxTr_u1iccCYxqjL0Y-ggFTzs9D-kJcskCj8Q4VB7REGkFZt8LmERWsqR83_vzsxd6fBhZvmVmtrV9r3gIfgpcUlW06BeTIXUUf-w276EIigGGebezDrmdzp5CkpRrPDgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات سپاه به‌ سلیمانیه عراق
@News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/69403" target="_blank">📅 02:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69399">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9KTMHF_58yMBuZpxaKq33-2YCmdogFbw9XaeaQl8mqbrZm53vu1G98k5qM652fqSkZrhEYDDXyTb5VzIeNv9Qu9qZxrdlb0bUu6zoUYbCp9RtdT3jtoW-nAi8g_2wY71p4An1LFmwV5sarPFcoe1N0bN5Amm5N0iS0A3ZRxVleF6Kgk3LCeY_K9f89u4bD3JW6v44gS0iwahwTqjjfhPtjjQyTwy_gdEPKjPIhGQFR7ZD4zGJhhAdC2GDoo5UH4jj3vnleprNk5vxFH4j24St4VfyUngelbczDoXPRxW0_rZAHcgohg3LZHUXxeqaGh-YIe_E9eQt8Prb_kq9GOrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXOjYDCmXh7TV4jJgcCDAZNWoyEahvndXLv8ZuMiVxMftl-JfHgN_sT1DAv7ICRPP9vUMf7oZEjHYLTYwxarko9_u3NgTLXTE0VyAabuXi6OqJMCfHotfxyC3WQQ-nI9MK8Hkq_y3lL4oER5wCx-gLK_i3krWEH87YCmpFW3fUF5EXlNWccUtyeLv5Xq_7VktbijGYPPYnbxHehsyUqFsTsANbsIn-NXKioUynFpaci-iUY0Iog3e5lpQnwVV6Vn4CnGfX28swJUwRNPhOF_rc2sGhR-zab5_C8yNEuSSBIh3GI3-8gvNA_qLAjrrcK5Y-vj_1ScbBzruyqgRo1tdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=sp5EFYPDWP8IhldHtgP_Fpth0hQkYiSwx05iasj-R91N6MNHZj0TWvGBPsKeHFKDCTfIS7FaBnI9bD_k1QTgRaDzQNu8Ig4-6oXMvVoJl5_eRUPZveTkCXqy6PhTqw3Mi7JIpJkZlHkRjaPJwDl8Ur6GY2Im5FXgqk70SkPvkUnKKogH-xUa7QOUzCIXM9NZGf6iI6D0ZZ1I1ZvPvc5y2ku0pkA0rYOjPKys9qdNLDgwB9P-tAFKA0v8CRKRSY3u-bH-raAqlzUSH2fHqr3rM7f4W533xLW4KHBe-nL_JGSYimEruvpaXnPm-OujHhsT9jz0kI-bW4x-8ew0pLAizg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ea496ad43.mp4?token=sp5EFYPDWP8IhldHtgP_Fpth0hQkYiSwx05iasj-R91N6MNHZj0TWvGBPsKeHFKDCTfIS7FaBnI9bD_k1QTgRaDzQNu8Ig4-6oXMvVoJl5_eRUPZveTkCXqy6PhTqw3Mi7JIpJkZlHkRjaPJwDl8Ur6GY2Im5FXgqk70SkPvkUnKKogH-xUa7QOUzCIXM9NZGf6iI6D0ZZ1I1ZvPvc5y2ku0pkA0rYOjPKys9qdNLDgwB9P-tAFKA0v8CRKRSY3u-bH-raAqlzUSH2fHqr3rM7f4W533xLW4KHBe-nL_JGSYimEruvpaXnPm-OujHhsT9jz0kI-bW4x-8ew0pLAizg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇷🇺
ساعاتی پیش یه انفجار تو یه رستوران تو مرکز مسکو رخ داد؛
جایی که به گفته منابع روسی، مراسم عروسی خصوصی با حضور چند نفر از فرماندهان ارشد نظامی در حال برگزاری بود.
کانال‌های تلگرامی روسیه می‌گن "الکساندر چایکو"، فرمانده نیروی هوافضای روسیه هم بین مهمون‌ها بوده.
گزارش‌های اولیه حاکی از کشته شدن دست‌کم 3 نفر و زخمی شدن بیش از 20 نفره!
@News_Hut</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/news_hut/69399" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69398">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⏺
المیادین:
بر اساس اطلاعات بدست آمده، گروه‌های کرد حاضر در خاک عراق در حال آمادگی و برنامه‌ریزی برای اجرای عملیات علیه جمهوری اسلامی ایران هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/69398" target="_blank">📅 01:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69397">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.  @News_Hut</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/news_hut/69397" target="_blank">📅 01:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69396">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=cl76tv9GyVcSGOO4dmbjsIXi2msPJefqBMzf4b463pD7tRdWlX4TzNuYy9413lv-ZlWp60lBbkVQx61-qR82J1o0biZ-i38RigtNcR1N1N4sXQxfu4xnpyHZN-ypEIJuWpKlyPM8lVZMiRObu29vmrrXVfS9vRBDd1UJ-7ClfW9EaBNmFxgdnP9j4TnULe0jLTY_xVIOmrHcchJQRmZE1BCqnCF4841vAVltLyhOz42ma65NBIvwvDPVAbIptGdy1lRPl0q9etb8G5WcyPsG1bCWCTE1K8CnZMJ4ctrdd9kcR8oZs-kNAybfu7FjCxuL7AXFLrTOX1Y_RI5Gs0IYgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff498baa1d.mp4?token=cl76tv9GyVcSGOO4dmbjsIXi2msPJefqBMzf4b463pD7tRdWlX4TzNuYy9413lv-ZlWp60lBbkVQx61-qR82J1o0biZ-i38RigtNcR1N1N4sXQxfu4xnpyHZN-ypEIJuWpKlyPM8lVZMiRObu29vmrrXVfS9vRBDd1UJ-7ClfW9EaBNmFxgdnP9j4TnULe0jLTY_xVIOmrHcchJQRmZE1BCqnCF4841vAVltLyhOz42ma65NBIvwvDPVAbIptGdy1lRPl0q9etb8G5WcyPsG1bCWCTE1K8CnZMJ4ctrdd9kcR8oZs-kNAybfu7FjCxuL7AXFLrTOX1Y_RI5Gs0IYgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پمپ بنزین‌های مملکت بخاطر حملات احتمالی، دوباره شلوغ شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/news_hut/69396" target="_blank">📅 01:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69395">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdtO9HYx0vnvp_wEYWSmNNBPwF58K3YKt2yHNmD25nU7s5xK6O_rO3P4nQBoly0JaE3yL7ID4s5mrbxt5ilpbQU_lhUdGVQVxO7_mhPyOWgw77RNn3usOTh6lDzSrdQyd8A_p7aBW-gc9s_aLMjKLu2RHdf9zdwDPm6RIC9eIBbXhKESPm-cZcC7NW_UWa0jPyEi-tAtKUGTViNumE1ha6SC68NOzhXBiei70K5EgRpCoCdDnTZW82t6eJdHvkBQO0hJPS1QPcq_5UeVfBLdituIl3twwr-1De8JyBykqigtJam2rL3zY7YINert5ShVF1rt2XtxTyv6zXIEKdFoxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
توییت اتاق جنگ اسرائیل و اون ساعت شنی معروفش
@News_Hut</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/news_hut/69395" target="_blank">📅 00:32 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
