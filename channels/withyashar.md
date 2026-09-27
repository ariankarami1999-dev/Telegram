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
<img src="https://cdn4.telesco.pe/file/Wzhl-aKSZpAi4BFsU16T3sS3utwzg_OMZ6DIeStStyFK4sTG-DDpqVzE_t8Ztx5Zl40Ui3iHbRBWwX4W5I5yQ81TvcMW-Jmxny4XwB6lWCuDa3IrYt-V0t3cZX_4B3G2AK8eEi1XeR2xF4QD7_kBk2eAr-moeP5KDStIKiqRb933ZqZSIPNrLUX4JnG0D3BLCPCpj78FKOUsRWgK-GjJ3c8uJ6xmLDXKEl-Uk4mZPmih-kY8d5wcKZbkdw0ugP-H-_1k1gbKX55cjpa3zeP-u8Wu7lhRkqiMWjMwylf6T0pA3atrfnWQvLB_7NX5aG-n10UEZR2TPwiY7xMjRn3oqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 467K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 16:40:44</div>
<hr>

<div class="tg-post" id="msg-24333">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ترامپ در ‌تروث : در حال حاضر، شمار افرادی که در ایالات متحده مشغول کار هستند، از هر زمان دیگری در تاریخ کشورمان بیشتر است!
@WarRoom</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/withyashar/24333" target="_blank">📅 16:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">امیر حاتمی، شهید زنده، فرمامده ارتش جمهوری اسلامی:
جنگ هنوز به پایان نرسیده است و ما باید برای وارد کردن ضربات قوی به دشمن آماده باشیم.
@WarRoom</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/24332" target="_blank">📅 15:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d096c16704.mp4?token=E_GLTAFBBq_RxfyJvFbTKQ8aJK6gXNz28vR59hc26IGED7ZZoRWk03qoXAeaU4paSJ-xmYbjOQKeJUmtxMVyKzipcuyF_NouLMUyziz2n7K9zLn2vEhLGV08A0muY9Jb731GcLE8NZOCgNLIhsoD1Rca5ILneSQhy87-QF1KDg3ZBTysQOkdJDBEbRFN0qnKjIjVx4fYJ_raeXa5uWyTbSmWrpvJR_uFRxzEVd88bqZSw7LZ4KXPzefMVxeIu-jDOymG8itwKykf6hEbS44iGDY-TRdq0229eUedVwJxAiKM98XQS61wEWjoE6rPN_ENPsZBBs5FqGgWjBmp9dLwS7R7NYh5aL4reAvT0ylYhFecWjnfqpuGi_KY-6Wu_c0M1hqiKq_fhYG_vtC5u_k27IpgfqLX1VMWjFditv7_minB0QFUpxatSmV6rysvmQRf0oIyZDU2B5OoXOnr7snea9EHnj8R1grS3wf8QejMie7rc5INg2v8K2zl-ttFzdn1JBoJq5ABFneItqYlyI7FRJfalQaHohb7Q9Gg7B5LUhnDA_dWzUt-QgX3gnDQ9Pk_db78e2TfG5GR1h4Vbtj0QKL8Hy3B4-efwoTCeUnOZKDlTNF8BAH2HpYJK0QpL92A7R3Z2b-r3kcuVQ49he81Pt_t6nlHDqekJeu7pIdvJbI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d096c16704.mp4?token=E_GLTAFBBq_RxfyJvFbTKQ8aJK6gXNz28vR59hc26IGED7ZZoRWk03qoXAeaU4paSJ-xmYbjOQKeJUmtxMVyKzipcuyF_NouLMUyziz2n7K9zLn2vEhLGV08A0muY9Jb731GcLE8NZOCgNLIhsoD1Rca5ILneSQhy87-QF1KDg3ZBTysQOkdJDBEbRFN0qnKjIjVx4fYJ_raeXa5uWyTbSmWrpvJR_uFRxzEVd88bqZSw7LZ4KXPzefMVxeIu-jDOymG8itwKykf6hEbS44iGDY-TRdq0229eUedVwJxAiKM98XQS61wEWjoE6rPN_ENPsZBBs5FqGgWjBmp9dLwS7R7NYh5aL4reAvT0ylYhFecWjnfqpuGi_KY-6Wu_c0M1hqiKq_fhYG_vtC5u_k27IpgfqLX1VMWjFditv7_minB0QFUpxatSmV6rysvmQRf0oIyZDU2B5OoXOnr7snea9EHnj8R1grS3wf8QejMie7rc5INg2v8K2zl-ttFzdn1JBoJq5ABFneItqYlyI7FRJfalQaHohb7Q9Gg7B5LUhnDA_dWzUt-QgX3gnDQ9Pk_db78e2TfG5GR1h4Vbtj0QKL8Hy3B4-efwoTCeUnOZKDlTNF8BAH2HpYJK0QpL92A7R3Z2b-r3kcuVQ49he81Pt_t6nlHDqekJeu7pIdvJbI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رویترز: در پی بازداشت چند نفر به ظن جرایم مرتبط با مواد منفجره در نزدیکی پایگاه RAF Fairford در بریتانیا، تدابیر امنیتی اطراف این پایگاه افزایش یافته است. چند ملک در منطقه ولفورد تخلیه و خودروها توسط تیم خنثی‌سازی بمب ارتش بررسی شده‌اند. گزارش‌هایی نیز از…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/withyashar/24331" target="_blank">📅 15:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24330">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/faaed5699e.mp4?token=Jz0pAcci77betc8KgjmZZNfl2KwiCknOAOVuCyYHREgly7HlbbjIaWzBAEYs15i81fny9qRrdQP1CqCHyL2TEkDZwIpbMK1bGMQzpGab1nKG0p784zBpdMWsJ7Uu14c5jFFdAM-ga6TQoCwEwqE4PXTuZFkDyMtk1gcWn8T3UIGOcQ3IEm9LB2liTSUyRoyTIw9XPQU8xbcYp1go9ByllOHtVZZ1-NxEf-FrXUgNKgVekcqxGhMDyGBq0mqB0vFLFwOrKwpJlAoEr17ztug4mXctS4t-dHGjCj1A-Vq9t98dTCsunlCuL0XdgG0pShKYG2xQtptdcrRYFZxsBOWaZhCGmgWpYuhS8M-J5tuYpWuk2q80oxwqxac20dVCJYDb_8jNpmKM5BQdgzngxmBibA1xH9tTINHHXrnOWUdHVwzC2CXaC9Lxkn1QC77NTcBKUokhVI-8ZasQ6gGRKSrsLaNDiZv_wT1Eoi92XQoqALax3dWWyuptZm5lVY6fI8WosZq5x_WqZwemnu-TEzPbubGyqBMEQ21yCSyZr4hUKYa1uMbrnxXWM1udlmsyw6BJvDytWWgpPC7SsYLmHUQqlrJxcx6_UxUscHDPiWI9Iqd3zoIgsqJqJ3aqw4fWEswOwhf1NYHcY0lLKqTk97figjA3yQpTkRmHQmh1Y7s6mKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/faaed5699e.mp4?token=Jz0pAcci77betc8KgjmZZNfl2KwiCknOAOVuCyYHREgly7HlbbjIaWzBAEYs15i81fny9qRrdQP1CqCHyL2TEkDZwIpbMK1bGMQzpGab1nKG0p784zBpdMWsJ7Uu14c5jFFdAM-ga6TQoCwEwqE4PXTuZFkDyMtk1gcWn8T3UIGOcQ3IEm9LB2liTSUyRoyTIw9XPQU8xbcYp1go9ByllOHtVZZ1-NxEf-FrXUgNKgVekcqxGhMDyGBq0mqB0vFLFwOrKwpJlAoEr17ztug4mXctS4t-dHGjCj1A-Vq9t98dTCsunlCuL0XdgG0pShKYG2xQtptdcrRYFZxsBOWaZhCGmgWpYuhS8M-J5tuYpWuk2q80oxwqxac20dVCJYDb_8jNpmKM5BQdgzngxmBibA1xH9tTINHHXrnOWUdHVwzC2CXaC9Lxkn1QC77NTcBKUokhVI-8ZasQ6gGRKSrsLaNDiZv_wT1Eoi92XQoqALax3dWWyuptZm5lVY6fI8WosZq5x_WqZwemnu-TEzPbubGyqBMEQ21yCSyZr4hUKYa1uMbrnxXWM1udlmsyw6BJvDytWWgpPC7SsYLmHUQqlrJxcx6_UxUscHDPiWI9Iqd3zoIgsqJqJ3aqw4fWEswOwhf1NYHcY0lLKqTk97figjA3yQpTkRmHQmh1Y7s6mKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : برای چندمین روز متوالی حرکت دسته جدید هواپیماهای سی۱۳۰ هرکولس به سمت منطقه و اینبار هم ۵ عدد
@WarRoom</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/withyashar/24330" target="_blank">📅 14:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24329">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سپاه: یک فروند زهپاد پیشرفتهٔ ارتش آمریکا را که به منظور جاسوسی در تنگهٔ هرمز فعالیت داشت، به دام انداختیم.
این زهپاد از نوع یکی از زیرسطحی های هوشمند و پیشرفته با نامRemus 600 «ریموس ۶۰۰» بوده که توسط رزمندگان نیروی دریایی سپاه به غنیمت گرفته شده و اکنون در اختیار متخصصان این نیرو، به منظور بازیابی اطلاعات آن، قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/withyashar/24329" target="_blank">📅 14:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24328">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سپاه : یه شهپاد زیردریایی خودران دیگه آمریکا رو گرفتیم
@WarRoom</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/withyashar/24328" target="_blank">📅 14:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24327">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGRsw9fpbkG4A6-3qs_ClUw7SAh-e7vW-uiDpprtboznagGh6cQ44hfovcIML4gBiIw3wEDkXrXagh5EZaMRUO5L1kVdlBJHYSHiUYlzMc6FxiRXT1giFwezGEerEg_vhyWaHMrl-9Rw1w_5Tfp9QFKKmviwFH5Vymfbw0H04mochfpkyr60OVhLXXZcQGhwsU0z83vC93SWrleCBlV5dhnrmkDJSlhrUO7qlEoG5kiF__txpBi-cy41Jdok5bzzlN7MlY9fG-2xQD6_JKPpGgMNj6bZ5ftfjs2qeiVfI2xyzJ5uZUDwXYT2rKsCeS1pmPD2jpa6k4-H7CevXLQFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : ناو آبراهام لینکلن به هاوایی رسید ، چقدر با RUDY11 خاطره داریم یادتونه ؟
@WarRoom</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/24327" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24326">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">مدیرعامل شرکت ملی نفت ایران:
بر اساس اطلاعات به‌دست‌آمده، اسرائیل و آمریکا برای ضربه زدن به تاسیسات نفتی برنامه‌ریزی کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/24326" target="_blank">📅 12:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24316">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNbg6bzwLTlmBF9veEK0nvTO9V4XsX3T34x7Yldcuo-b8pPGokRCd2C2lDhtM7YtXTZr5n5gh7ezaqiN9jEsRAHAw5562VACSxRmlZTBSxv0g9qqyKEIV5OAzEiL1dHiQAfZe5JlitM8zdK-MzJt4IZJQbkTVvT6MX-5e9rcyzeDxxq1cXzgev1Toyzag9yT4P7mk7029pHi-0x7X7KVLLmiguYRJid3hbSpton2UHluDXrtqrCXlNGn-uisdTn6rzIdQLO_234va_SDcDaeDSD1_EzF6F8y-s4jYoMsjnNwjUX2MwRY_raovZqm5ywilRPDkuil7mFD69g5mxbZfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpBHTca8zzzJ2vmdR3l-ejIO5qLGhDDymvqxKyFKts6IYtZTHE_EL77BMXf9u7GSk9pEstzVrW_TUf7oNVbu0SBAIer4uZuHyF9k-uaGrZgeELNu6CQDfrBsm2GgMvzyG4WRZx-s30GKin83MOL7PRpAr1t-dX9i-xRKjvWk5VeUPH7CWtnhc2gNSGTjjGCYaDsdZY-wX-X38K3tsT7NquGunGW3eq-XYTrL52xLTtM-Uh7uQ2QUPes_gwdP1vZRyASaiMQeQ8Ms2XzzKmV9dpCuoHVn9bXo7hkEHIPu4L1eR5IWCqVoppxJ5tF1syBV6QRpWlh8Vp7ykxGpD9GpaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wvwlon2k7_tmDNEXTivBbF4BEMYugqv3Stcz_mqU0MGbPWfV7W9SiGj9xK6--l1Xxmh0Xq9RK5FxIFXS8IOyl9k6qXY40XKlKwqo9C56YQcsbURgZZ1Mpx4Jn4ShD03oICKosAMeco8rVB_y88vb0O4r451ak2mDH7-VwKbDqTVSa1Eg9DC-ic1KgFMbxKNm1zN15O2vfTTB5mrq1w36fgQOtmdnXm0cTHAiXuW1CWxc5dB57TjeGawnyWUd3hpJxmbH0xhQV_knlLbOh_hRVlTj5F-1vEF9gxkRcD19jnR456mX3Nj8ITIllg5RkCxC8xjMe5p8ObPbPTC8BJkaZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pPIzshVPx4TTidR4PFxyJiHV1D7aCrpvaYbwMn3Ms2Vyslu1zxJPAaYq9YecItJL2EkO0i-k-948zKzJkMIodpCy-hqQePHxipG2uA_JzXns8_JoNu_DTWvb--NjmuDYT9kTzwAsVB9rGYc-kVn1jYGchQUbaj3lvLwQupnh73I0xNZVLYrY0a3FAo6lLS5DL1P7PYMIbWK83wXYlY98_i2soByX7hDB7uczY-Yzwk8cZosh9CNQnCSGMwch1qqQeoWhpMF2N-Jk1jVgbnrppMJh-dhZghxoTv-8Eznvt966Erfd2xSCRI2qIVC8_DHkv9jQbNhQdCUfGNu9CaIVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XP2Cta1tgOnkRPwP_DKWrkZtlUMEAe5kCPC1IeJ0f34b3ebHo6VXd9DrOxGgWjSMK-Y_85nmPYQ0AaUBoYRnzLkQgXAfKVG0g4QNnD9CSmAVIT7yGTbwYHebwDWFwdyORTgivRd6c_-DXk-oLbz5CZTrcRIVb4MDBMC8eFSxynICYCOEnnivk8HNLavJ4mt3dU8v8bKab7IizmnxRCVXYZ4RlPiQz7Fis8MpkmznHe8aC-vHje2YM2r2GzP004bNR2LRbSKanjTxZWPTeRMEsSm0nAC7cKKjLiMiHGMV4ygsWYGBwqN66qCjFDevYnaOh9MSZ1qZS7WiDYpm6DlnRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBLCMLAbKA2jarW8HLzFKbROdQX3qzV6hUPnkEyX2Q2pDy1xyRNbigV6ebINfp8ChVbKW0MUrPuSl1yeUPx3GLFv3vU136t869qR77nr_YnfVKGA-fHHZEFf1a47SAtjaIAUSYUvOiLQFYDwGT8UyKORrKFOeAWP_lLZeE4vmnmsa2mmo8bU_h-JFWLi4v8JED66m6ochdlnRCsIo4mN5tFZ6e6bwNd_6ywHUsBAbirxozwkDvbZHwb89cxe8HFj__gjhG_Keb1e5CNZJ1NNJM6os7TYLAsurMGOliiAo4U1GGw4LRH39mp__EFneLn01p0WlFm4mCMUYOcOu-4ukQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQG2AxRShTIx6qXxbutnPSUYh-0fxq56oCUWfBMcwk_eKMonAZvhySiAf9yW69-b6K5tZffReqgecvQcMJOAvtIHb6nWaUbZcf0h11nTjLZdVAu3fp9PhppLQ9Nf4373o0MbsdBMNalXuUaKK778cHCbqytka7evRZQfnqHBXSnjH3N0YatOgoromdFzKM58x8JTl1l1faYE9vGIQ3l34J5nMsvJr6BaiFJmHc4PHH_EHgBUzvW6bBDIRyfZVD1xD4M6-axDqY71ynj5IxI_e_AYxFAhbz7Nl_OXlQw6LoldZHG9Ii9-tR68mBpbI3HlAoCEdxy9pZOZHDz_kCGsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tIyVMi5eQ0Zs4RdWHzvQiey3qudJWMwXeJxkiuoTjJtwDOJ1gi4c4ExDYHCase7mggKHVUd6Hz3g3ddMjgE5dg2AVO3Rsv5sH1iQQk1MbtL5Ngz3-OQ12QIKga4C7yFB4FbuicWchBRVIENBOIAnX8HoLo7kUWF7PMtdaVclNGcohpd-SPG-D9gFBJKxa-V3_aztG9KwKQz_07csars8-A7UbTD-VUd-u3V8-KB7C6Ab-9rnnBONwANh1rf6uDg9Yx3TvGiz9u6VDTQbiw4PC9jJnUKXU5lLtDNwJtJ-_Psi2t3uJmxZRw7ntvbNNLWx4xNyHgt2Rb7kQUQ6yKRkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvGR6-yPyEWEoBtimFQBYKFxOcNcDuHn0asrZXEmdCDGSXIFASoxI6OviTjoVzG_vHf01tcrQZ10Xvre7DEPZvAXolXaeIbm1tv5CJntFWv2yv1EX1UH6UYuVU-WRX3CyFYvfoZMP2H6eorcImJADhEWU1xW-B3Bn-OZcgbuPA54wsEeN6huO3XY2M94OvNrjPG4JOY_4CeuRyf7LR11j3iiiJ38hAeTY4CDZpTNntuY_EcavAEjFCmcdvPd_LGq-Au9z9-WaFlEJdCIWWRjEZY2YNZB_9A1MZ5HKAJqbxEj9USE6pKsgMXejGpPovflMidqPw9XDbDiGYjB3bCgMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D9a-FkPzbQUkCwngaFGINELu-_MDzDif-GVHws8IdVwNJZWLZafflZGVm5ll1eOoNDCANx7lp12O4X6HZjsGFtNS1xmpTynBPQu2Lbvvq_IqCfOnZjT5kDfyPvzRGINTJ1UFbfp_K4_RnQqRhp60fp9apc9R2wX9pp7NfOYUic3_vIaibUO9TMlweupmgYUx4Zla1K66gIxZ_HQzEIW2IW6Yj3p1danYo7QJXD17DpGn1eXRMH_SPDk4lH1dkrMwRn8UxZduTNfmII6LZslReWNbC8Uk5IaBhziJxNkCaBCBXx2ZkJ3qcmlqJENeXzOWDobQqJPBSbzzgoiaSSu4nA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آوییشن‌ایست:
۱۰ فروند جنگنده
اف-۱۵ئی استرایک ایگل
نیروی هوایی آمریکا پس از بازگشت از خاورمیانه و مشارکت در
عملیات خشم هماسی علیه ایران
، در پایگاه هوایی
راف میلدنهال
در بریتانیا فرود آمدند. روی دماغه جنگنده‌ها نام و تصاویر شخصیت‌های بازی
مورتال کامبت
مانند اسکورپیون، ساب‌زیرو، لیو کانگ و شائو کان دیده می‌شود. همچنین روی این جنگنده‌ها مجموعاً
۴۵ نشان انهدام پهپادهای شاهد ایرانی
و نمادهایی از مهمات استفاده‌شده، از جمله
موشک‌های جی‌ای‌اس‌اس‌ام، بمب‌های GBU-39 و راکت‌های لیزری APKWS II
دیده می‌شود. این ۱۰ فروند، نخستین گروه از مجموع
۲۴ فروند اف-۱۵ئی
پایگاه سیمور جانسون هستند که از استقرار سال ۲۰۲۶ در خاورمیانه بازمی‌گردند.
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/24316" target="_blank">📅 12:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24315">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏در دومین سالگرد نفله شدن حسن نصرالله، مستندی از لحظات جستجو تا رسیدن به جسدش رو ببینید، ارتش اسرائیل اعلام کرده بود بر اثر خفگی مُرده و درست بوده، اسرائیل اشتباه نمیکنه ( با زیرنویس فارسی )
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/24315" target="_blank">📅 12:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24314">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یانشا, نخست‌وزیر اسلوونی: تغییر حکومت در ایران و انتقال مسالمت‌آمیز قدرت به مردم، برای توقف صدور تروریسم و ایجاد صلح و ثبات در منطقه ضروری است
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/24314" target="_blank">📅 12:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24313">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رویترز:
در پی بازداشت چند نفر به ظن جرایم مرتبط با
مواد منفجره
در نزدیکی پایگاه
RAF Fairford
در بریتانیا، تدابیر امنیتی اطراف این پایگاه افزایش یافته است. چند ملک در منطقه ولفورد تخلیه و خودروها توسط تیم خنثی‌سازی بمب ارتش بررسی شده‌اند. گزارش‌هایی نیز از قرار گرفتن پایگاه در بالاترین سطح حفاظت آمریکا،
FPCON Delta
، منتشر شده است؛ نیروی هوایی آمریکا از
افزایش هوشیاری نیروها
خبر داده است. پلیس می‌گوید حادثه مهار شده و تحقیقات ادامه دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/24313" target="_blank">📅 12:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24312">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75be4777e3.mp4?token=mWD01sebagnAPPxJhMm3ErmvJMHozxMvFYh8sc4nEtlgHphdKn20Ocv_2yEML3GX6lF4Y8s1MfGONz2hDLXcfINp77JNc-aG8yURAaOCXTtiz_RMMXySQclRkClGUO0HIsqjTP1APkQQZmSZV88ZI5FM7EEfkQaIbJkvG_n_GM0pJsB8S_PFpKf_KMP8IxRiki9b-PJyC8v3Y6bqGSm4oa_dkN4RdPOX2Jg6fu3H3iWE5SfAjUw678G56RrpgaPo0I1zwMa9ZipybkGDKwGWZ0tbUHKC3OQsDCqugz-VLEHzREc_I1Zh1kVeWjFJmEvSZ7YNGnKxJrkOhnBCSipLvVZNdioKQjZhmMbOLdZPUb65eSBPL05vdb73OwS7l-k-vkMNhdHXeeTQBXLlQC_Y7v5yMAlpWHXE5waVpsboZL1Hp-6xr_WLYZE9sUT4_Mw_ZZQ__GS2ZjNsdotL4Esdxz7Q30wwbUrBRSftFjcXpFNTj4R1ERvU4p6mXz8x3POO6JjbQYzLqORlM0c_Jw2AnAxZEkXqNGnIv5jCbjSj5TX9ee-_6HD8ekNzWgxOpiMVIixwfzNk3ersE0KlXjkvIofbmbResI-gLY8RiY5Nhk7ErrrgQ8i88WqBiZ7geUypGhweoVlT2W3W2VKkBqpc_e0xTNW3FN-vwE7SvsB078Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75be4777e3.mp4?token=mWD01sebagnAPPxJhMm3ErmvJMHozxMvFYh8sc4nEtlgHphdKn20Ocv_2yEML3GX6lF4Y8s1MfGONz2hDLXcfINp77JNc-aG8yURAaOCXTtiz_RMMXySQclRkClGUO0HIsqjTP1APkQQZmSZV88ZI5FM7EEfkQaIbJkvG_n_GM0pJsB8S_PFpKf_KMP8IxRiki9b-PJyC8v3Y6bqGSm4oa_dkN4RdPOX2Jg6fu3H3iWE5SfAjUw678G56RrpgaPo0I1zwMa9ZipybkGDKwGWZ0tbUHKC3OQsDCqugz-VLEHzREc_I1Zh1kVeWjFJmEvSZ7YNGnKxJrkOhnBCSipLvVZNdioKQjZhmMbOLdZPUb65eSBPL05vdb73OwS7l-k-vkMNhdHXeeTQBXLlQC_Y7v5yMAlpWHXE5waVpsboZL1Hp-6xr_WLYZE9sUT4_Mw_ZZQ__GS2ZjNsdotL4Esdxz7Q30wwbUrBRSftFjcXpFNTj4R1ERvU4p6mXz8x3POO6JjbQYzLqORlM0c_Jw2AnAxZEkXqNGnIv5jCbjSj5TX9ee-_6HD8ekNzWgxOpiMVIixwfzNk3ersE0KlXjkvIofbmbResI-gLY8RiY5Nhk7ErrrgQ8i88WqBiZ7geUypGhweoVlT2W3W2VKkBqpc_e0xTNW3FN-vwE7SvsB078Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسخره کردن پزشکیان در فاکس نیوز : آقای پژاکیان ، یه سوأل ساده هم نمیتونست جواب بده
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/24312" target="_blank">📅 11:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24311">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VE-PnIxKwVj-Nk6glSuMk5AbEFO5_NIqodfoiDY9VxWk3D6Kfhti8fA8VPnxN81WCMdLOk14ezwi7Etz5OrEZY3arBqFx5eDDiuDar8QDJjbYc5PwyttQtNI-BX37if5zpf5j1oDHUDpyXeepBrppzHgCTTiASj7rjvN9gT2SIAjtFtNt0ZbtwY2_eS9hC73fBc_dY_zOLmXIHHKcjczl8khz-jGyK8QJSNPT5sJLmuvdk1w0Nenn0YIUBCw-f4tLDT8D6pMqh9VQC9ERE_1K5VH26aL1JphezHKnmwme66yiZSn94Xhr8kRJZ4f8vXp_89u67qKV7VcsIAZ-0sE3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار نجات ترکه موتور یه پرستو نشسته قشنگ ارشادش کنه ، چیکار که نمیکنه این رژیم
سردار سرتیپ پاسدار
محمدحسین زیبایی‌نژاد
مشهور به
حسین نجات
(زاده ۱۳۳۴ در شیراز)، از فرماندهان ارشد و شناخته‌شده سپاه پاسداران انقلاب اسلامی است که هم‌اکنون به‌عنوان
جانشین فرمانده قرارگاه ثارالله
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/24311" target="_blank">📅 11:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24310">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: تمام بانک‌های تجاری بزرگ در امارات متحده عربی و ترکیه انجام تراکنش‌های مالی با ایران را متوقف کرده‌اند. بسنت گفت فشارهای اقتصادی واشنگتن برای منزوی کردن ایران در حال نتیجه دادن است و آمریکا برای اجرای این سیاست با بیش از…</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/24310" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24309">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoCoIlbXWggPXG7iqguCo6dR638d0Vcx2IUyHsu_jYaS2C1X2b1NBkocak4kkNvuLLNH31_kJRBVULiZHU1VkBxv87R4_03GdboyGOIuYZDO86-wzf5NLkTkPeI3uG24uwdTAVPXR-7TWh7CMDeXCSFTVDs1CuD2O5QJSFEuqiqQfzgy2AwLm-UUjpXguQ5F8kDgxTTIzHCxh2k1eDTYPSzCZ_W1iVkvkTBNchnZZMenXSRMZD6djyIlCBbeRLGn1BGgYQDVqWlaILnDeu0hE4df4J_keclTUM5g54FZ7fdYvWfzLzVGwvpF7pVq6SdwsjQP8HCae4qwlsunqYKtvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی : من جام خوبه نمیام ، مرسی اه
@WarRoom</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/24309" target="_blank">📅 11:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24308">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcKi86nMcED3shsn-EPbc1eEIjfA3r3KEC4Sh0tIoWJedIFMG6twyic1pz5hAeeoUMczKQckwyE2WmMH9aZd9rONg7C4Kt5OUK2CwgRabq9IIo4XubO7zx2PKNgE6PkXKAk2YFFYGl8-fbhlUA4AENVPyq7y-M9lE39RFO5zBtUon2AzVz5_WoiOhPXtp3T_aeFG-vOnxKgw4yHRwRm4C4rRrySFpMf3yLqoLYLI9g1FO68Xwy4DqMYmkkU5Mn1pIMphup36-NYj_z2z0SnE5AwFWWlBd0G3lQgWcbA3RQOlaZbq7fzZOCQ5r0TNZOxyA9NLE5kD8bWM8WdMqRLj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه های رژیم : سرهنگ دوم
مجید بهرامی
، رئیس پلیس آگاهی شهرستان ایجرود در استان زنجان، روز پنجشنبه ۲ مهر هنگام انجام مأموریت برای مقابله با
قاچاق کالا و ارز
جان خود را از دست داد. بر اساس گزارش پلیس، در جریان عملیات، خودروی قاچاقچیان با خودروی مأموران برخورد کرد و سرهنگ بهرامی بر اثر این حادثه کشته شد، این یک ترور سیاسی نبوده و
عاملان این حادثه کمتر از ۲۴ ساعت بعد توسط نیروهای امنیتی و انتظامی شناسایی و دستگیر شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 92.2K · <a href="https://t.me/withyashar/24308" target="_blank">📅 11:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
تمام بانک‌های تجاری بزرگ در
امارات متحده عربی و ترکیه
انجام تراکنش‌های مالی با ایران را متوقف کرده‌اند. بسنت گفت فشارهای اقتصادی واشنگتن برای منزوی کردن ایران در حال نتیجه دادن است و آمریکا برای اجرای این سیاست با بیش از
۵۰ کشور
وارد رایزنی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/24307" target="_blank">📅 10:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HyjoNdHZK5N142iNk1Fxp3LSmT7lkkUDQu_FaLnm3uNGznvjpqFp38CoiJDUp5LvoUHAhfsyT-j7U7bHFRNzPjxvECW_ZpRRYufydw27uShNJkRwqHm26sH83g4J9oAPtHEKKHcDxEk8iT3_Um674GV3HcN9B-PQRisf7St1K_X8yBiDJkd6nYpMdR1bA-WTA7ZtDbua7zjSI0UzdvdijZlFaUqHiBDrZdRthDDbm24EGfzdaRbOmFadIhJmfbC2bUI8ji_n8NTW5CJge4HZZ1-qpPReKtBT8orItu8V8f0w74_GDEd7twEfjLl-mBf8xw2_E7TyKbjDQxlK7USWTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ۳۰ دقیقه اخیر ۳ انفجار بسیار‌ سنگین خارگ
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/24306" target="_blank">📅 10:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تام کاتن، سناتور جمهوری خواه:
یک درگیری جدید با ایران در پیش است
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/24305" target="_blank">📅 10:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgZChXC8Ydja59fHWhw6WywmCEex9Il_oiwNAbVcVBNEDRAhnbfGJEI5eUCV9ZK0oDe7yvfFPpqZfy134RYq7D-KyWAm1Y8fCsSL6S_ndR3GK0jiQcHfhChah8eDi7_wsfequjVv3ldf4-gZq3hluV9-E18Q0AK8ms9h77ZP2O9SmfrnXdF73uHUbOn4yOG9SuCwuzv18hSwXP6YnckiFWIK0OC9o7aAtc2o3wA1i4L-po3aAOUyJso1kSrnbqyJFaY9SHEbFW6VlLOWb6JdSKhResl96k-7pbfCDX_3q3v6N2D_dwx5ZPUC7ssceuYNLWUv_NR-qx6Ww-kG_Lo1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس:
چین دو پاندا غول‌پیکر به نام‌های
«پینگ‌پینگ» (Ping Ping)
و
«فو شوانگ» (Fu Shuang)
را پس از دیدار شی جین‌پینگ و دونالد ترامپ به آمریکا فرستاده است. این دو پاندا بامداد یکشنبه ۲۷ سپتامبر از فرودگاه چنگدو با یک پرواز چارتر عازم
باغ‌وحش آتلانتا
شدند و قرار است حدود
۱۰ سال
در آمریکا بمانند. این اقدام بخشی از چیزی است که چین از آن به‌عنوان
«دیپلماسی پاندا»
استفاده می‌کند؛ یعنی اعزام یا امانت‌دادن پانداها به کشورهای دیگر به‌عنوان نمادی از روابط دوستانه و همکاری دیپلماتیک
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/24304" target="_blank">📅 10:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فاکس‌نیوز:
سخنگوی سپاه، سرتیپ حسین محبی، اعلام کرده ایران تا زمانی که
هفت شرط تهران
برآورده نشود، به عملیات علیه آمریکا ادامه خواهد داد. از جمله شروط ایران، رفع محاصره دریایی بنادر و آزادسازی بخشی از دارایی‌های مسدودشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/24303" target="_blank">📅 09:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24302">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رویترز:
عباس عراقچی اعلام کرد ایران در مذاکرات جدید درباره
برنامه هسته‌ای خود امتیازی نخواهد داد
و حقوق تهران از جمله غنی‌سازی اورانیوم و نگهداری اورانیوم غنی‌شده، قابل مذاکره نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/24302" target="_blank">📅 09:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24301">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اتاق جنگ با یاشار:
برای بررسی روایت انتقال مجتبی خامنه‌ای، ابتدا باید به سه بیمارستانی نگاه کنیم که
در ۲۸ فوریه و شب اول مارس واقعاً آسیب دیدند: گاندی، مطهری و خاتم‌الانبیا.
۱-
بیمارستان گاندی در شب اول مارس، در جریان حمله به ساختمان‌های صداوسیما در نزدیکی آن، به‌شدت آسیب دید و بخش‌هایی از بیمارستان تخلیه شد؛ تصاویر و بررسی‌های مستقل محل اصابت و خسارت را مستند کرده‌اند.
۲-
بیمارستان مطهری نیز در همان موج حملات آسیب دید؛ این بیمارستان در کنار مقر پلیس تهران قرار دارد و تصاویر قبل و بعد از حمله، خسارت قابل‌توجه در اطراف و داخل بیمارستان را نشان می‌دهد.
۳-
بیمارستان خاتم‌الانبیا نیز در گزارش‌های همان روز به‌عنوان یکی از مراکز درمانی آسیب‌دیده ثبت شده است؛ گزارش هلال‌احمر ایران از حمله به محدوده اطراف خاتم‌الانبیا و مطهری خبر داده و بررسی CNN نیز خسارت به خاتم را مستند کرده است. بنابراین اگر روایت انتقال او به چند بیمارستان درست باشد، هنوز این احتمال وجود دارد که یکی از مراکز درمانی مورد استفاده او
یک مرکز نظامی یا حفاظت‌شده وابسته به سپاه، در مجاورت این بیمارستان ها
بوده باشد؛ اما این ارتباط هنوز اثبات نشده است. همچنین بیمارستان سینا در گزارش‌های مربوط به مسیر درمان او مطرح شده، ولی طبق همان روایت،
پس از حمله اولیه
محل انتقال او بوده و نباید آن را با بیمارستان‌های آسیب‌دیده در حملات ۲۸ فوریه و شب اول مارس یکی دانست.
در نتیجه، سه بیمارستان آسیب‌دیده را می‌شناسیم، اما فعلاً هیچ مدرک مستقلی نداریم که یکی یا همه آن‌ها همان بیمارستانهایی باشد که مجتبی در آن بستری شده و سپس زیر آوار مانده.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24301" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24300">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">در جنگ ۴۰ روز قرارگاه سپاه در محدوده چهارراه آبسردار با اینکه کاملا در منطقه مسکونی بود با این دقت شخم زده شد
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24300" target="_blank">📅 09:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24299">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏افشاگری محسن حیدری آل کثیر عضو خبرگان رهبری در مصاحبه با تلویزیون قطری العربی تایید کرد که مجتبی خامنه‌ای همراه پدرش بود و زخمی شد و پس از زخمی شدن پی در پی به سه بیمارستان در تهران منتقل شد که هر سه هدف قرار گرفته شد و در بیمارستان سوم از زیر آورها او را…</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24299" target="_blank">📅 02:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اتاق جنگ با یاشار: پیامی که در برخی کانال‌ها درباره «تحریم جدید ایران توسط گوگل» منتشر شده، نادرست و گمراه‌کننده است. این پیام عمدتاً به ارور Too many accounts created مربوط می‌شود؛ یعنی وقتی در یک دستگاه یا از یک مسیر اتصال، تعداد زیادی حساب جیمیل ساخته شود،…</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/24298" target="_blank">📅 01:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24297">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرنگار اسرائیل
ی
: حملات امشب سپاه پاسداران به کشتی‌ها در تنگه هرمز گسترده و کم‌سابقه بوده است.
گزارش‌های دریایی از افزایش حملات و کاهش شدید تردد کشتی‌های تجاری در تنگه هرمز خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/24297" target="_blank">📅 01:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24296">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اتاق جنگ با یاشار:
پیامی که در برخی کانال‌ها درباره «تحریم جدید ایران توسط گوگل» منتشر شده،
نادرست و گمراه‌کننده است
. این پیام عمدتاً به ارور
Too many accounts created
مربوط می‌شود؛ یعنی وقتی در یک دستگاه یا از یک مسیر اتصال، تعداد زیادی حساب جیمیل ساخته شود، گوگل برای جلوگیری از ساخت انبوه حساب‌ها ممکن است از کاربر بخواهد
شماره تلفن خود را برای تأیید وارد کند
. این موضوع می‌تواند با
استفاده مکرر از VPN یا IPهای مشترک VPN
هم مرتبط باشد؛ به‌خصوص اگر از همان IP تعداد زیادی حساب ساخته یا وریفای شده باشد.
پیش‌شماره ایران (+98) نیز در حال حاضر برای وریفای حساب گوگل قابل استفاده است.
بنابراین این پیام به معنی تحریم یا مسدودشدن جدید دسترسی کاربران ایرانی به گوگل نیست؛ ضمن اینکه محدودیت‌های گوگل علیه ایران موضوع جدیدی نیست و سال‌هاست وجود دارد.
اقدام جداگانه امروز گوگل علیه حدود ۶۰ حساب مرتبط با صداوسیما
نیز به دلیل فعالیت‌هایی که گوگل آنها را مرتبط با
فیشینگ سیاسی و پنهان‌کردن هویت
عنوان کرده، انجام شده و ارتباطی با مسدودشدن عمومی کاربران ایرانی ندارد.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/24296" target="_blank">📅 01:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24295">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ : این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.  گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها…</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24295" target="_blank">📅 00:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24294">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ :
این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.
گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها را بکشید، اگر در هر نقطه‌ای از زمین آمریکایی‌ها را تهدید کنید،
ما بدون عذرخواهی و بدون تردید به سراغتان خواهیم آمد و شما را خواهیم کشت.
ما این جنگ را آغاز نکردیم، اما تحت ریاست‌جمهوری ترامپ،
آن را به پایان خواهیم رساند.
جنگ آنها علیه آمریکایی‌ها، به انتقام ما تبدیل شده است.
ترامپ :
ای مردم سربلند ایران، ساعت آزادی شما فرا رسیده است.
زیرا ما آماده‌ایم دولت شما را به دست بگیریم.
این حکومت متعلق به شما خواهد بود که آن را به دست بگیرید
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/24294" target="_blank">📅 00:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24293">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خبرگزاری محلی هرمزگان:
هم اکنون فعالیت‌های نظامی در امتداد سواحل جنوبی هرمزگان، به همراه تعداد و شدت انفجارهای امشب،
در چندین ماه گذشته،
بی‌سابقه است.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/24293" target="_blank">📅 00:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24292">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اتاق جنگ با یاشار ، وضعیت قرمز : ۹ سوخترسان در خلیج فارس و یک دسته سوخترسان با مالکیت نامشخص به سمت منطقه ! (دسته دوم ممکنه برای جنگ یمن باشن) ولی موقعبت الان کاملا جنگیه ! @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24292" target="_blank">📅 00:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24291">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دیدبان اتاق جنگ : پدافند شهید رودکی قشم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24291" target="_blank">📅 00:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24290">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بابک زنجانی:جلوی استارلینک رو میگیریم، تکنولوژی در برابر تکنولوژیتون داریم
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24290" target="_blank">📅 00:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24289">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/inE6iC8bceSqVVYOZ0a4tp669Vd0ee9wz2WBHRGDKBEaVwFpY87QStHPkbpbYJh6GM7rdA_NyarHnMzUdi3T1eqfRH6lRaRpHcYpzWdnjxu0xCNP6In2FJCJ6yQH2vlYJDe-gcOfZBIod48XelgAeoRpQjW01wCQDUupmaIpIEJd7WT6FiAL5xk1vYdzJVSg8VKG8dYx_P9w7VGN1cvyo2yKOKq8N-WJ86RNo2rEelpALXU3-nKK5KQf32O3UFDEH1R8r0Rt2t_b5DWKM6htZSfWWlv-f0DjAeeVV8PMU4RAReCbvhhQqJfyAADXjjnVl03cmS7w42Fu7x4RHa6GVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیویورک پست: دادستانی ایران پس از انتشار ویدیویی از اجرای نمایش «تهران پاریس تهران»، علیه گروه تئاتر پرونده کیفری تشکیل داد. ماجرا مربوط به صحنه‌ای است که در آن فاطمه مسعودی‌فر، بازیگر زن نمایش، سرش را به سینه مهرداد صدیقیان تکیه می‌دهد و او دستش را روی سر این بازیگر می‌گذارد. مقام‌های قضایی این رفتار را نقض «هنجارهای اجتماعی» دانسته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24289" target="_blank">📅 00:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سیریک زمین سنگین لرزید دیدبان اتاق جنگ میگه ممکنه زده باشن حتی
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24288" target="_blank">📅 00:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">وزیر خارجه کانادا : ایران تهدید اصلی است و نباید به سلاح هسته‌ای دست یابد. هرگونه حمله ایران به کشتیرانی در تنگه هرمز را محکوم می‌کنیم
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24287" target="_blank">📅 00:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سخنگوی نیروهای مسلح ایران:
موشک‌ها و پهپادهای ایرانی پیشرفته‌تر و قدرتمندتر شده‌اند. این بار، ما یک غافلگیری برای دشمن داریم و در برابر هرگونه تجاوز احتمالی، از فناوری‌های نظامی جدید استفاده خواهیم کرد.
هر کشتی‌ای که از تنگه هرمز خارج از مسیری که ایران تعیین می‌کند، عبور کند، امنیت نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24286" target="_blank">📅 00:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">۳ پرتاب از سیریک  @WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24285" target="_blank">📅 00:13 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">۳ پرتاب از سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24284" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">موج پیغام های  شما از گزارش عجیب ایران اینرنشنال توسط مجری افغان این شبکه مرضیه حسینی که مجاهدین خلق رو مردم ایران میدونه و پرچم جعلی اونها رو پرچم شیرو خورشید عنوان میکنه ! و پروموتشون میکنه ! @WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24283" target="_blank">📅 23:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24282" target="_blank">📅 23:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24281">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‏افشاگری محسن حیدری آل کثیر عضو خبرگان رهبری در مصاحبه با تلویزیون قطری العربی تایید کرد که
مجتبی خامنه‌ای همراه پدرش بود و زخمی شد و پس از زخمی شدن پی در پی به سه بیمارستان در تهران منتقل شد که هر سه هدف قرار گرفته شد و در بیمارستان سوم از زیر آورها او را بیرون کشیدند.
‏محسن حیدری آل کثیر نماینده منتصب این دوره مجلس خبرگان از خوزستان است که در گذشته مسئول بخش عربی سپاه تروریستی پاسداران در خوزستان بوده است.
‏افشای این اطلاعات در حالی که پزشکیان در مصاحبه اخیرش در آمریکا مدعی سلامت کامل مجتبی خامنه‌ای شده بسیار قابل توجه است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/24281" target="_blank">📅 23:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24280">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ
:امروز روز بزرگی برای کارگران صنعت خودروسازی آمریکا و خریداران خودرو است! من به تازگی استانداردهای جدید بهره‌وری سوخت را تصویب کرده‌ام که دستورالعمل احمقانه مربوط به خودروهای برقی که توسط جو بایدن و پیټ بوتجج مطرح شده بود، را لغو می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24280" target="_blank">📅 23:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24279">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24279" target="_blank">📅 23:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24278">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromK2</strong></div>
<div class="tg-text">اونهمه سوخت رسان تو یه خط نمیتونه چتر باز باشن
یا پوششی برای ب۲ ها
اف ۲۲ها</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24278" target="_blank">📅 23:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24277">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">صدای‌انفجار تنگه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24277" target="_blank">📅 22:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24276">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پزشکیان: اجازه نمی‌دهیم تنگه هرمز برای جابه‌جایی سلاح‌های آمریکا باز باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24276" target="_blank">📅 22:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24275">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">صدای‌انفجار تنگه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24275" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24274">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH0V-6L-B_w74KNrcV0zxmcB42SmDcG6CeN2vD--tJUzWSOIws8B5kxnfx3dsdmLe4QLlNlzegKB5n4cIUDgr1iIZq3O6w8xvd4jNvKuN5KbKHsJ3dXnCkzg4K2vCnv2FjaOPNOVVU_8dZJu50QMVAPVjiTVJETecU_xV6gf0gLmJnqRbS1e3uXgzDj0ewxG4mL130LzX3EGlhvCMU_mEHLlkt9EB5EMaseg-p-QNulyF1gnA0C5xpD3QCUxFKoB5OatmX2QDBUjsShpx6wsE4PgKKDph6hf_FL5D5kdLqqDIqKJg7bYdbXJloHP8_50SO2JPTO7rymuSd_7DN4smg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث
: ایران نمی‌تونه سلاح هسته‌ای داشته باشه
@WarRoom
یاشار : پست باحروف بزرگ در چت و نوشته اینترنتی به معنی با صدای بلند و پرخاشگرانه گفتن اون جمله است</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24274" target="_blank">📅 22:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24273">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UA7U9Ho9lfGDeGoEsY_i85UE0Ik-xvZoMNfRJiFLNUsMSi1lQkC4dnCJQljPRUN10-h8XO7d--cmgDL923CM4BHowkBAMky7CBGgzb8H7C-CX1_5jIhh7x6Zc3Rpo69a4oUIZPZliPt836j6PA0VnjJm6zUXGafXr9uyCxkmITVKZrh8jyqdWAxw0QpEYuP-rwO1QgB1tHAjAgozQhITZ_IXVOQZ5BasIhjDXW80nC9cmM1c0uNxMJ-8Bq_Nream6uLGUcJcGKSToQnRxR_DOVZn9JsXGd7rCgEVBq8QPmq7fQjxqELm8RRLP7qmJkOBWZHFzjb0qCvbFN6_yyGyKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار ، وضعیت قرمز : ۹ سوخترسان در خلیج فارس و یک دسته سوخترسان با مالکیت نامشخص به سمت منطقه ! (دسته دوم ممکنه برای جنگ یمن باشن) ولی موقعبت الان کاملا جنگیه !
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24273" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24272">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پزشکیان لشش رو آورد
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24272" target="_blank">📅 22:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24271">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جنرال جک کین به فاکس نیوز:؛عملیات نظامی علیه ایران اجتناب ناپذیر است. با شکست مذاکرات جاری میان ایران و آمریکا، مسیری که در پیش داریم شامل ادامه محاصره دریایی و هوایی و عملیات های نظامی گسترده از سوی اسرائیل و آمریکا علیه ایران است @WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24271" target="_blank">📅 22:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24270">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها می‌خواهند تنگه هرمز را فوراً باز کنند. می‌دانید چرا؟ چون دارند از پا درمی‌آیند؛ می‌دانید چرا؟ چون هیچ پولی وارد کشورشان نمی‌شود. آن‌ها پولشان را از تنگه هرمز به دست می‌آورند، بنابراین خودشان خودشان را فریب دادند. آن‌ها گفتند: «بیایید…</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24270" target="_blank">📅 21:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24269">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">جنرال جک کین به فاکس نیوز:؛عملیات نظامی علیه ایران اجتناب ناپذیر است.
با شکست مذاکرات جاری میان ایران و آمریکا، مسیری که در پیش داریم شامل ادامه محاصره دریایی و هوایی و عملیات های نظامی گسترده از سوی اسرائیل و آمریکا علیه ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/24269" target="_blank">📅 21:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24268">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کانالi24  news: یک منبع امنیتی گفت که پس از رد پیشنهاد ایران از سوی رئیس‌جمهور ترامپ برای بازگشایی تنگه هرمز، ستاد مشترک ارتش آمریکا ارزیابی‌های خود درباره مسیر اقدام بعدی را از سر گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/24268" target="_blank">📅 21:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24266">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lievUKLHNDX2Y9WRL5T-bTpTdM7DnEXdN1mZK-Mtv5l775dPX1vviHTa9rCAZJkBnxIxOjl9PtDYzETHOeJHbFWbKsAQE3WOd37xe8ZX8KCVtgwqTJhKqmV-xsdyW1rBoFZQ8P_leqownDW_UGIc6q7taHM9rEiBgCp3ZJEnLdXGHhXIiG6WDd02BtZ4vCcZgTdlQEkwIDCaANixfiAvr6UzJdB0MHq6kriqL27PmJV4am3IgHTs8YBCz-By7Z0j3BW9FuGz7oap-CcLdNUGOBFEbc_zxRF0ZbbMSaRXA5jpRmhLQdjC2yfCdVntLJSghVEBQMYQU-Fw1brKG7Vk3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oiWE_cHowT7VVvkOR-8Q7B_-6-uzonpCbiwAukVKfY5AOJINMVKRO8unrvNs3zmJp2LjCj7VOid7bn2eQrte4JRIBN4WFtSJrgFcL_MXJBfF9TUE4alBNkZiQeo2lqku4Hom1i-V2IInkHDxQQdNVOZct1kzgAlV-9fsIB1RzqmqSfEGK9q1DmxFJrpjiD94ecB-r6IOhu8xL-6Vcqn5F6JXAxBZJhO9sTvaCOfndHRnTQUVGN4Zyn8-inXA4RKl9m11hT5Ae6T31kRvOwUDQUmjPoWyZy0pBU7ag8GqdbyA7BiwJVkhT3_0QLMHG2BG0Ar-CUftGhFvOGTzQl4SGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مخزن سوخت یک جنگنده آمریکایی در ارتفاعات ایران پیدا شد: تصاویر منتشرشده از یک مخزن سوخت خارجی پیدا‌شده در ارتفاعات ایران، با توجه به صدا و جنس فلزی برای یک F-15E Strike Eagle است. چون F/A-18/EA-18G از فایبرگلاس استفاده می‌کنند ولی ساختار اصلی این مخزن از آلیاژهای…</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24266" target="_blank">📅 21:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24265">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مایک پمپئو: رهبران ایران بی‌شرم‌ترین دروغگویان روی زمین هستند. ظاهراً آیت‌الله در سلامت کامل است و آن‌ها می‌گویند که به‌دنبال سلاح هسته‌ای نیستند. شگفت‌آور است که کسی تصور کند می‌توان در مذاکرات یا در هر موضوع دیگری به آن‌ها اعتماد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24265" target="_blank">📅 21:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24264">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">العربیه: ترامپ به تیم مذاکره‌کننده خود اعلام کرده است که تیم مذاکره‌کننده ایران تصمیم گیرنده نیستند و با آنها نمیتوان به توافقی رسید
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24264" target="_blank">📅 20:54 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">اتاق جنگ با یاشار : شورای ملی ایرانیان آمریکا، معروف به نایاک (NIAC Action)، که از مهره‌های نفوذی جمهوری اسلامی در آمریکا محسوب می‌شود، از دونالد ترامپ در دادگاه فدرال شکایت کرده است. نایاک خواستار غیرقانونی اعلام شدن عملیات نظامی آمریکا علیه ایران به دلیل نبود مجوز کنگره شده است. در این پرونده نام نیما دیلمقانی، آلن بند(زنش ایرانیه عرزشیه) و پروین اسماعیلی‌زاده نیز به‌عنوان اعضای نایاک مطرح شده و جمال عبدی از چهره‌های اصلی سازمان در پیگیری پرونده است.
@WarRoom
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24263" target="_blank">📅 20:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24262">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1oXiD4gkG0Kxez60c1ZQ5tGfxIAf81KzP_dgR123VnA0l-Sxa8WoU11B5tf5oiHqvfJ_S7Rg3n7SRHw1t-4lgSoO9LZj6CtBIH9y9vXblh1-nCCOQuv8M1mfkCRZ3Q2uZ4mwJ4gVkfgcdva-DOkzuzka57Pe9gVCOqHN-XdG8z9xI9q3M35Hjzv9Sx1CwMiY8US1t7yHokuM_J8yEVuZPf376nQYtUKQllT5nGOYkMd-WRSLp2aYI_LbaoCebsU8a3Vypsv_DSDsZLhfN4T1bl3zBD8b-fC0sypW1pd8Cs8GCbgp_pL5713qfvdpP-pYUVZ1kKjFLoAjimmp9JrKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانمی که چند سال پیش به عنوان بزرگترین دزد و جیب‌بر خیابون انقلاب تهران شناخته میشد، آزاد شده و به تازگی در رزمایش جانفدا شرکت کرده
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24262" target="_blank">📅 20:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24261">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ژنرال جک کین: شی می‌خواهد ایران جنگ را طولانی کند و نفوذ آمریکا را تضعیف سازد.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24261" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24260">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سی‌بی‌اس به نقل از یک منبع: انتظار می‌رود دور جدید مذاکرات آمریکا و ایران هفته آینده برگزار شود.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24260" target="_blank">📅 19:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24259">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گزارشهای بسیار از اختلال گسترده در سیستم بانکی و دستگاه های کارتخوان
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24259" target="_blank">📅 19:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24258">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ارتش اسرائیل: امروز صبح، انبار تجهیزات نظامی حزب‌الله را در منطقه سجده، در جنوب لبنان، مورد حمله قرار دادیم.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24258" target="_blank">📅 19:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24257">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وال‌استریت ژورنال: آمریکا برای تشدید تحریم‌ها علیه جمهوری اسلامی با بیش از ۵۰ کشور تماس گرفته است و به آن‌ها پیام داده: «در قبال ایران یا با ما هستید یا علیه ما.»
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/24257" target="_blank">📅 18:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24256">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏اکسیوس: واشینگتن خواستار امتیاز هسته‌ای از تهران است
در حالی که ایران می‌خواهد هرگونه مذاکرات را بر موضوع تنگه هرمز و محاصره دریایی آمریکا متمرکز کند، دولت ترامپ خواستار آن است که ایرانی‌ها با امتیازدهی در موضوع هسته‌ای موافقت کنند.
مذاکره‌کنندگان آمریکایی در جریان مذاکرات روز سه‌شنبه به ایرانی‌ها اعلام کردند که ایران کنترل تنگه هرمز را در اختیار ندارد و بنابراین نمی‌تواند درباره آن مطالبه‌ای مطرح کند
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24256" target="_blank">📅 18:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24255">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ef4ff4bd.mp4?token=ROzcWmdhjug97asEfjWZoZ9BIs-13ODOYsETblyx2-LD_z4_VrV12OC8ikFjIWDqeCV-y-N6iQHOzLeZTIvr7nfDPvT4-8PBt1oQlsA8UfB_ine1WlP_kGo38pdIJ1tn1j8j1Qk6489yLvKTk9zuwBiBlFkU4k3_dyRR3GHYXldjT81h3R4ubg1zh1McsTWq8BtTXpNf--oKUjJ2E2ExK4YZJHAJMTvIP7z8Ccl7O7A9xEhnlBEDThcHx5eaZ_RxrzfrM3QECgcEWKIVCC_WKyCm6Nk6BEWBdaqauUPBIqoCvwn8zXvko1aLrC-V3NzG3acyVilFx_wGc9dgu-KvtpIUBsI50iLvr5LHvLnXzH_SmtAOxiNd3FhtUbnml3hQZ8_3BJN1j9_DGjYoiIr9_YadrYMbOG2RN-acT7EopdjM4H226HbqM4qeX__jyfZsci8U-2NJ0fKdhaURAz4Ui2mw0QGJQ-fdNXiI5XF_-r1ZDVMdzp8WW54yYdr3fFXe1JF2CK4srqEfGRH8VblJ9xl5i5OaAQNmH8VzSpXQr55laTz0AE7hQjnlrnfXTZuVJDsflvnZ4oqbRbl8T0meRIubKMxWlBEM180wJctxsq5roM9pWSuAqrr77POXjgu-iiBhiaNREaS8TEJtbfeq2GT-j-IVIyYTd4vuIdtK0ZY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ef4ff4bd.mp4?token=ROzcWmdhjug97asEfjWZoZ9BIs-13ODOYsETblyx2-LD_z4_VrV12OC8ikFjIWDqeCV-y-N6iQHOzLeZTIvr7nfDPvT4-8PBt1oQlsA8UfB_ine1WlP_kGo38pdIJ1tn1j8j1Qk6489yLvKTk9zuwBiBlFkU4k3_dyRR3GHYXldjT81h3R4ubg1zh1McsTWq8BtTXpNf--oKUjJ2E2ExK4YZJHAJMTvIP7z8Ccl7O7A9xEhnlBEDThcHx5eaZ_RxrzfrM3QECgcEWKIVCC_WKyCm6Nk6BEWBdaqauUPBIqoCvwn8zXvko1aLrC-V3NzG3acyVilFx_wGc9dgu-KvtpIUBsI50iLvr5LHvLnXzH_SmtAOxiNd3FhtUbnml3hQZ8_3BJN1j9_DGjYoiIr9_YadrYMbOG2RN-acT7EopdjM4H226HbqM4qeX__jyfZsci8U-2NJ0fKdhaURAz4Ui2mw0QGJQ-fdNXiI5XF_-r1ZDVMdzp8WW54yYdr3fFXe1JF2CK4srqEfGRH8VblJ9xl5i5OaAQNmH8VzSpXQr55laTz0AE7hQjnlrnfXTZuVJDsflvnZ4oqbRbl8T0meRIubKMxWlBEM180wJctxsq5roM9pWSuAqrr77POXjgu-iiBhiaNREaS8TEJtbfeq2GT-j-IVIyYTd4vuIdtK0ZY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها می‌خواهند تنگه هرمز را فوراً باز کنند. می‌دانید چرا؟ چون دارند از پا درمی‌آیند؛ می‌دانید چرا؟ چون هیچ پولی وارد کشورشان نمی‌شود. آن‌ها پولشان را از تنگه هرمز به دست می‌آورند، بنابراین خودشان خودشان را فریب دادند.
آن‌ها گفتند: «بیایید تنگه را ببندیم و برای جهان مشکل ایجاد کنیم.» بعد من وارد شدم و بزرگ‌ترین محاصره تاریخ نظامی را برقرار کردیم؛ یک دیوار فولادین!
حدس بزنید چه اتفاقی افتاده؟ حالا دیگر هیچ پولی ندارند، چون خودشان خواستند تنگه را ببندند. من هم گفتم: «بسیار خب، ما هم آن را به روی خودتان می‌بندیم، اما بقیه می‌توانند از آن استفاده کنند.»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24255" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24254">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67823a94b1.mp4?token=uol9zs6ZtHkPWHqU0CHzFLrjeWtOFcM6vfr7hPF1GwfTBeOLafDoJwR6uzKic-GU9umuTDUYM28rgfDxblQkTLRrlCrED55kVmzer9EA0dJZ-fJPseJ7deZ2aagXx1JYsh6PMg_KkRdqRNHGcn-lV-nTQ3A9m5XUWLuJYB_u2cEfdzmOlR0QObCsNYHbIvCpdrYqn96NbIakaJOqV_NNYQdVNpurzaru1DIE-UHZazCOXjkJwirvtRP_nfdnsLLzIAOIzj7moiVZoZs0JZAlfvbdU6D0l9HK49nA8t3h9TkAnoiPyU4Ql9OW-Yth7VsZ-j_53zJMUNl8O8b-keVUz39WhMfv_dYJMLfFBAGobxeRsk5maPWXDw8R5OIjgl6tRrT5XlY3dg_-TCzkPIGq0bnxrXy41DMSKs894GqitQKwnmnvU5zQHld7A6ifuO9eID7BH3hu803x34B5MXmrd3dA3Mf4ViqkXNfxEc-_JP47AFXT8MDY-WEuwRNx6j4ncB8LpFX-IT5t0VNUumMNZITY9PGUtDcRmrwKNiChRh5k2QkJM9mkwpBuZPhkRITsK_n1H3lNh7zRU904V7CchEbtvMYOtGjhpYHKHOwSc1yNLmW2xNqkLSy3Vu9xK6K5cXkwy4Hkn3HelgVxlvzbgWr_fcw683pbeZHGgQvun-8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67823a94b1.mp4?token=uol9zs6ZtHkPWHqU0CHzFLrjeWtOFcM6vfr7hPF1GwfTBeOLafDoJwR6uzKic-GU9umuTDUYM28rgfDxblQkTLRrlCrED55kVmzer9EA0dJZ-fJPseJ7deZ2aagXx1JYsh6PMg_KkRdqRNHGcn-lV-nTQ3A9m5XUWLuJYB_u2cEfdzmOlR0QObCsNYHbIvCpdrYqn96NbIakaJOqV_NNYQdVNpurzaru1DIE-UHZazCOXjkJwirvtRP_nfdnsLLzIAOIzj7moiVZoZs0JZAlfvbdU6D0l9HK49nA8t3h9TkAnoiPyU4Ql9OW-Yth7VsZ-j_53zJMUNl8O8b-keVUz39WhMfv_dYJMLfFBAGobxeRsk5maPWXDw8R5OIjgl6tRrT5XlY3dg_-TCzkPIGq0bnxrXy41DMSKs894GqitQKwnmnvU5zQHld7A6ifuO9eID7BH3hu803x34B5MXmrd3dA3Mf4ViqkXNfxEc-_JP47AFXT8MDY-WEuwRNx6j4ncB8LpFX-IT5t0VNUumMNZITY9PGUtDcRmrwKNiChRh5k2QkJM9mkwpBuZPhkRITsK_n1H3lNh7zRU904V7CchEbtvMYOtGjhpYHKHOwSc1yNLmW2xNqkLSy3Vu9xK6K5cXkwy4Hkn3HelgVxlvzbgWr_fcw683pbeZHGgQvun-8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: من توافق پیشنهادی آن‌ها را رد می‌کنم. آن‌ها می‌خواهند فوراً تنگه هرمز را باز کنند، چون به‌شدت در حال شکست خوردن هستند. می‌دانید، این را نه در رسانه‌های جعلی می‌خوانید و نه می‌بینید، اما ما با قدرت در حال پیروزی هستیم. کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز خارج می‌شود و دیشب ۲۹ کشتی از آن عبور کردند. آن‌ها می‌خواهند به توافق برسند و به‌نظر من این خوب است؛ من هم اهل توافق هستم، اما چنین توافقی قابل قبول نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24254" target="_blank">📅 17:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24253">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639d93cd0b.mp4?token=btN2Igf6rByV2jgWhcHRThbDJEqL4Vl78jJWLyFYrd24s5vxGSBSFL4xUzMc2gXgt_Bx65O04xfp9aPKh_3p3_qTeOb3bF-aPvNrgaB4lXMPq2toRUJfkBb1lk0e5U6fh-CTr9HX1pocO1x-D9tYvJIQrUMbpgmm0DY0kNZAraJ1gyxvt0zJDhP4lPZ3pTXDGiiOFuIrBUhbZqISQ8V5WOKFEUoOSnePPNa4Y1TVDTdWj6-KHrI1SGLaIhYI58FCbLdbfGlBblD5FQ3zv6Aj19K9DJx9qdtBFoAmgwCDLxMHQWfB-hN_ulDCzj8px-BNOi_856RP76hj3d7r6ONBqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639d93cd0b.mp4?token=btN2Igf6rByV2jgWhcHRThbDJEqL4Vl78jJWLyFYrd24s5vxGSBSFL4xUzMc2gXgt_Bx65O04xfp9aPKh_3p3_qTeOb3bF-aPvNrgaB4lXMPq2toRUJfkBb1lk0e5U6fh-CTr9HX1pocO1x-D9tYvJIQrUMbpgmm0DY0kNZAraJ1gyxvt0zJDhP4lPZ3pTXDGiiOFuIrBUhbZqISQ8V5WOKFEUoOSnePPNa4Y1TVDTdWj6-KHrI1SGLaIhYI58FCbLdbfGlBblD5FQ3zv6Aj19K9DJx9qdtBFoAmgwCDLxMHQWfB-hN_ulDCzj8px-BNOi_856RP76hj3d7r6ONBqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: آن‌ها پیشنهادی ارائه کردند، اما من آن را رد کردم.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24253" target="_blank">📅 17:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24252">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ترامپ: ایران خودش را در یک بن‌بست قرار داده است با بستن تنگه هرمز، و ما بزرگترین محاصره‌ای را در تاریخ نظامی بر ضد آن اعمال کرده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24252" target="_blank">📅 17:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24251">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ترامپ: ایران متحمل خسارت می‌شود، زیرا به پول دسترسی ندارد و منبع درآمدش از تنگه هرمز تامین می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24251" target="_blank">📅 17:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24250">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ترامپ: حجم عظیمی از نفت از طریق تنگه هرمز عبور می‌کند و شب گذشته 29 کشتی از آن عبور کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24250" target="_blank">📅 17:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24249">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: ایران خواهان یک توافق است و من هم به توافق‌ها علاقه‌مندم، اما این پیشنهاد قابل قبول نیست.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24249" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24248">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ: ما به یک پیروزی بزرگ دست خواهیم یافت و کنترل کامل را بر تنگه هرمز به دست می‌گیریم.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24248" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: من توافقی را که ایران از طریق آن خواسته است تجارت را فوراً از سر بگیرد، رد می‌کنم، زیرا این کشور متحمل خسارات زیادی شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24247" target="_blank">📅 17:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی: تهران ادعای پاسخ نظامی به محدودیت‌های هوایی اخیر را رد کرد و از مذاکرات جدی با کشورهای ذی‌نفع برای رفع محدودیت‌ها خبر داد؛ در عین حال، هشدار داد در صورت لزوم، گزینه‌های متقابل غیرنظامی علیه برخی فرودگاه‌ها را اجرا خواهد کرد، هرچند امیدوار است موضوع به این مرحله نرسد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24246" target="_blank">📅 16:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJLmB_e0LpL1V6_z180QNe2Ec1DPfrerfdW-W8erGbVmjbYBb0GdCUH5OKVpxRDBvRl0NTBFIQjmH_zXuDfFYza664yEMnXF4pytyycOmUevORU32pbqS7liU9z-dL4AklFVceyYQgIWgt0YkpLz-saKAUvpC_wrgZpH4GIaoFGGvUtPsYlqeBPa1mVXSwf3iF0PoWKOtW_kHOcVfrL3HNcX2gkcYKXrJhnxirJ9HoCI4ithg5pcP8KxumJxerXtvH0E2xSWO8U0HF7M_fEW_kJtUTOuo76GouXsvhMnEG_5CUaoxs3UlYW-rCznndpmLS7FQlJjrgN268IjMpmXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گارد ملی آمریکا اعلام کرده که در ۲۲ و ۲۳ سپتامبر، هواپیماهای C-130H3 هرکولس از گردان ۱۶۶ ترابری هوایی دلاور برای پشتیبانی از عملیات سنتکام در خاورمیانه اعزام شده‌اند و حدود ۱۰۰ نفر از نیروها نیز همراه آنها مستقر شده‌اند. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24245" target="_blank">📅 16:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">عراق: خروج ائتلاف بین‌المللی (مبارزه با داعش) به رهبری آمریکا از این کشور در آستانه تکمیل است.
رئیس سلول رسانه‌ای امنیتی عراق اعلام کرد ائتلاف تمام پایگاه‌ها و مقرهای خود در مناطق فدرال عراق
(از جمله پایگاه عین‌الاسد)
را تخلیه و به مقامات عراقی تحویل داده و خروج نیروهای باقی‌مانده از
اقلیم کردستان و پایگاه اربیل
نیز در حال انجام است. مهلت نهایی پایان مأموریت ائتلاف در عراق
برابر با ۸ مهر ۱۴۰۵
تعیین شده است. این به معنای قطع همکاری آمریکا و عراق نیست و پس از آن، روابط امنیتی دو کشور در قالب
همکاری دوجانبه
ادامه خواهد داشت.
@WarRolm</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24244" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تایمز آو اسرائیل:
ائتلاف سعودی اعلام کرد دو پهپاد حوثی‌ها را که به سمت ریاض شلیک شده بودند رهگیری کرده است؛ این حمله در پی افزایش حملات حوثی‌ها و همزمان با مذاکرات امنیتی عربستان، ترکیه و پاکستان رخ داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24243" target="_blank">📅 15:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7t85bBK4nU73_prRa_dy12sCkYAVZRuuH_SksJXGVJ2IPPnGglX_hXGkFJ6qsCwEWroJ_q0tHupN4ciim8RW73pijYrYUcvaTGhqiRQq8RlcpBeh3Revo3gAfRHRcxrC304wM-6omX_V6v_Dj63JznTdeJkz2c3_4ZA07quEWTGU3oON3C0I7UBuDXE0u-dRIrLPFU8ef_cW94X3pOiQsZjalVKpoEqHOr4xl_x22Si8cXbsbuiK420X_nLZLlvHpICrkizJFGz6fLgN4YhOzZDdvAcFOiH74X2uYOEGlXoa_OZKwBhIpI3U6fukIEO_53ScwMUFGMgmJUVbbUBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسوشیتدپرس:
دونالد ترامپ در
واکنش
ی
تمسخرآمیز
به رژیم ایران تصویری از نقشه تنگه هرمز در شبکه اجتماعی خود منتشر کرده که روی آن نام
«تنگه ترامپ»
درج شده است؛ این اقدام پس از پیشنهاد ایران برای بازگشایی تنگه ظرف هفت روز انجام شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/24242" target="_blank">📅 15:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نیروی هوایی عربستان سعودی در حملاتی در شهرستان حیفان، جنوب استان تعز، پروژه تصفیه آب منطقه الأکبوش و شبکه ارتباطات این منطقه را هدف قرار داد.
این حملات در منطقه
الأکبوش ـ الأحکوم
انجام شده؛ منطقه‌ای که طی روزهای اخیر شاهد درگیری‌های شدید میان نیروهای یمنی و حوثی‌ها بوده است
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24241" target="_blank">📅 14:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24240">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پزشکیان در مصاحبه با سی‌بی‌اس: ما چند زندانی آمریکایی را آزاد کردیم، اما آمریکا به تعهد خود عمل نکرد.
پزشکیان گفت: «ما کاری را که آمریکا از ما خواسته بود انجام دادیم و چند نفر از زندانیانی را که درخواست کرده بودند آزاد کردیم. قرار بود پول‌های ما آزاد شود؛ این پول از کره جنوبی آمده بود و قطر قرار بود آن را به ما منتقل کند. ما به تعهد خود عمل کردیم، اما آمریکا به تعهدش عمل نکرد.» پزشکیان افزود: «آمریکا چیزی را که می‌خواهد می‌گیرد و بعد به تعهداتش عمل نمی‌کند.»
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24240" target="_blank">📅 14:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بلومبرگ: پایگاه نظامی دائمی آمریکا در لهستان، موسوم به «فورت ترامپ»، ممکن است تا ۴.۴ میلیارد دلار هزینه داشته باشد.
رئیس‌جمهور لهستان، کارول ناوروتسکی، گفته امیدوار است این پایگاه پیش از پایان دوره ریاست‌جمهوری ترامپ در سال ۲۰۲۹ تکمیل و افتتاح شود. مذاکرات درباره
مسائل مالی و اداری و انتخاب محل و زیرساخت پایگاه
همچنان ادامه دارد. بر اساس گزارش بلومبرگ، این پایگاه می‌تواند محل استقرار حدود
۵ هزار نیروی آمریکایی
باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24239" target="_blank">📅 14:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه، اعلام کرد که در سال ۲۰۲۷ به دلیل محدودیت‌های قانونیِ دوره تصدی، از سمت خود کناره‌گیری خواهد کرد، اما احتمال بازگشت دوباره به ریاست‌جمهوری در آینده را رد نکرد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24238" target="_blank">📅 14:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فرمول کلاهبرداران
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24237" target="_blank">📅 14:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یاشار جان درود اینترنشنال الان باید آنفالو بشه یا زوده؟</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/24236" target="_blank">📅 14:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMojtaba Bahrami</strong></div>
<div class="tg-text">یاشار جان درود
اینترنشنال الان باید آنفالو بشه یا زوده؟</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24235" target="_blank">📅 14:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24234">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗦𝗔𝗝𝗔𝗗™</strong></div>
<div class="tg-text">حاجی پس ما برقمون قطو وصل میشه بخاطر این لاشیا بود
🤣</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24234" target="_blank">📅 13:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef185bab33.mp4?token=lTL6XYIydXod9x17OqV1YI_ydpl4KLe5dDmnIKTqPw8BGeo-p_GcZSpQDIX6p_5AHAtrwxH4eQeYKegT3RPprHX06MNFuPyE93IK5iwRgcnq_VUt-eWDqW6pRkvLW8n60hRYIEpB8P-6EvKsITehHYR2zMj9y78SeEHYzEtVIkn41R2EvvexRSXcyvNLaihktHYk0uMqViMp9U1hvbtQ6yT3ZGJ4LKeXeORioBMiPN_aNWR0sdwNL0nA2GA-iMo3tKkzi5abefvdlZOotCWxZduXR4FMbdf2tNAi7DpxWY6DBCCwQ_NM1HKlfSfzU5ClfeKmNWctuktLQMVjFCcfxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef185bab33.mp4?token=lTL6XYIydXod9x17OqV1YI_ydpl4KLe5dDmnIKTqPw8BGeo-p_GcZSpQDIX6p_5AHAtrwxH4eQeYKegT3RPprHX06MNFuPyE93IK5iwRgcnq_VUt-eWDqW6pRkvLW8n60hRYIEpB8P-6EvKsITehHYR2zMj9y78SeEHYzEtVIkn41R2EvvexRSXcyvNLaihktHYk0uMqViMp9U1hvbtQ6yT3ZGJ4LKeXeORioBMiPN_aNWR0sdwNL0nA2GA-iMo3tKkzi5abefvdlZOotCWxZduXR4FMbdf2tNAi7DpxWY6DBCCwQ_NM1HKlfSfzU5ClfeKmNWctuktLQMVjFCcfxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">IRAN: NO PLACE FOR AMATEURS
ایران جای آماتورها نیست
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24233" target="_blank">📅 13:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگر بیماری قلبی دارید زیرزبانی دم دستتان باشد.
@WarRoom
😂</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24232" target="_blank">📅 13:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رؤسای جمهور آمریکا و چین توافق کردند که ایران باید به تعهد خود مبنی بر عدم توسعه سلاح‌های هسته‌ای پایبند باشد و نباید برای گذرگاه‌های آبی بین‌المللی عوارضی وضع کند.
همچنین واشینگتن و پکن بر سر کاهش تعرفه‌ها به ارزش 30 میلیارد دلار توافق کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24231" target="_blank">📅 13:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گزارش شنیده شدن صدای انفجار در خارگ @WarRoom
🚨</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24230" target="_blank">📅 13:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پزشکیان: در حال حاضر قطر و پاکستان پیام‌های ما را به واشنگتن منتقل می‌کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24229" target="_blank">📅 13:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گزارش شنیده شدن صدای انفجار در خارگ
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24228" target="_blank">📅 13:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ee584150.mp4?token=lARhucAQA91gKUuXFrNMOqUic0xoS6KLWtf5cwK5l1UPj3Hpe7n-aWDNmijoXuikx_V3HEMEQaku1-s9dwcuZ2UFDNTd2eGZt3Ac1lSMmMnaixlgReMX3Hus18CW3fJric8bPpXfR7uJL0256vq9VAIoLxLoJYxlWd9Bjg1oikubX_XxxvCwJZGl3YtGjRfVXEVWRG6d3LEPE642BuFfJBcyf9RUZ2kztUnkiVXpIxWUavLATCz19qXBiXlb5GZi8JN1hLa27Z8QY2ai29XLlsYAKu0dKiymR4AYkyY2eMU7m8k5uLrBmvJGZE0mQKKp1xKQZ1mhEu-aH1E4LmT3rItint-O-wJcuZ-aqoldhUJsT32gP33pPNAhpfc7reEwSli0VFscdPtfoNniY7dwrM4REh3Rzs6iDn83_Ju3un957SIjHgwALwUD2QXGcevT8Js4wJmaej3ghdlAcXMG_GKm7gAXBIZqS612R42Pv5JM7KVOIkLgpHHYDfy4xZBF6LM8fWbo2cNBhWz5Za7OCWGieHGh2W79ZygBy8XiLiC7czhfzZqNryX-JTclM5NOe34jy612xTqurA7MlZC66Ie7sKlcIsEt-Vy-l_tKxoMZ8WUC_XXAR8OPONGexY2c2EPL8cYWgKiduJ9rL6elrIlLMwtek2jmuXOilAhhUQs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ee584150.mp4?token=lARhucAQA91gKUuXFrNMOqUic0xoS6KLWtf5cwK5l1UPj3Hpe7n-aWDNmijoXuikx_V3HEMEQaku1-s9dwcuZ2UFDNTd2eGZt3Ac1lSMmMnaixlgReMX3Hus18CW3fJric8bPpXfR7uJL0256vq9VAIoLxLoJYxlWd9Bjg1oikubX_XxxvCwJZGl3YtGjRfVXEVWRG6d3LEPE642BuFfJBcyf9RUZ2kztUnkiVXpIxWUavLATCz19qXBiXlb5GZi8JN1hLa27Z8QY2ai29XLlsYAKu0dKiymR4AYkyY2eMU7m8k5uLrBmvJGZE0mQKKp1xKQZ1mhEu-aH1E4LmT3rItint-O-wJcuZ-aqoldhUJsT32gP33pPNAhpfc7reEwSli0VFscdPtfoNniY7dwrM4REh3Rzs6iDn83_Ju3un957SIjHgwALwUD2QXGcevT8Js4wJmaej3ghdlAcXMG_GKm7gAXBIZqS612R42Pv5JM7KVOIkLgpHHYDfy4xZBF6LM8fWbo2cNBhWz5Za7OCWGieHGh2W79ZygBy8XiLiC7czhfzZqNryX-JTclM5NOe34jy612xTqurA7MlZC66Ie7sKlcIsEt-Vy-l_tKxoMZ8WUC_XXAR8OPONGexY2c2EPL8cYWgKiduJ9rL6elrIlLMwtek2jmuXOilAhhUQs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مخزن سوخت یک جنگنده آمریکایی در ارتفاعات ایران پیدا شد: تصاویر منتشرشده از یک مخزن سوخت خارجی پیدا‌شده در ارتفاعات ایران، با توجه به صدا و جنس فلزی برای یک F-15E Strike Eagle است. چون F/A-18/EA-18G از
فایبرگلاس
استفاده می‌کنند ولی ساختار اصلی این مخزن از آلیاژهای آلومینیوم هوافضایی ساخته می‌شود و در بخش‌هایی از آن نیز فولاد، تیتانیوم و مواد پلیمری به‌کار می‌رود. این مخازن از نوع Drop Tank هستند و خلبان می‌تواند در شرایط عملیاتی، پس از مصرف سوخت یا برای کاهش وزن و مقاومت آیرودینامیکی، آنها را عمداً از هواپیما رها کند (Jettison)
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24227" target="_blank">📅 13:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1482c7d1a.mp4?token=PYe01uf3gIhL0RrU54hZddZXoJyvLhKSMlZLTMLXM8sRSNNKCOuTdPxuOOPqrNTKvODPfZKaEtcrcAVBLuwhUq6AKUiZBFciGmMkfRZjUFCAE7dzyzYe-GnDbU96pzfBcHFjiLrzldJhz1BhjpLhkurFFaXIwxVD6hgLjAXpNhqDEQF_B5flYstZ52Pk8bQLM5vatPTVvQJZlVIr6NqfZ94nDxkqbaLFlnQ9TuSbSRH6ZRlCyZrqdcReqJS13q1HcCVe-9aZxKq_kZMjrVDJy-uOFg3jMXWuxaBxRSqTobr1gJKEVJW2n5oshQ85Nax2vEchXZun_-dOAFdvjec8Loi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1482c7d1a.mp4?token=PYe01uf3gIhL0RrU54hZddZXoJyvLhKSMlZLTMLXM8sRSNNKCOuTdPxuOOPqrNTKvODPfZKaEtcrcAVBLuwhUq6AKUiZBFciGmMkfRZjUFCAE7dzyzYe-GnDbU96pzfBcHFjiLrzldJhz1BhjpLhkurFFaXIwxVD6hgLjAXpNhqDEQF_B5flYstZ52Pk8bQLM5vatPTVvQJZlVIr6NqfZ94nDxkqbaLFlnQ9TuSbSRH6ZRlCyZrqdcReqJS13q1HcCVe-9aZxKq_kZMjrVDJy-uOFg3jMXWuxaBxRSqTobr1gJKEVJW2n5oshQ85Nax2vEchXZun_-dOAFdvjec8Loi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش یک معتاد خمار از لانچر
@WarRoom</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/24226" target="_blank">📅 12:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24225">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYaPqF574q0yeI0wEwxe3ZCAPwxI0aY9fzheUIZZ0UZ6YZBpywD_EnesMjgldok5n9h655T31JmN8Lxy-3b813b4eMe6F9GohCmuwpdJbfx0JFKkXmZUHKFrO07SlpbWEDYB8yXgnaLvXfMlAhC2eloqbBpgUzOO0HbTa4ZXXBXPl2bkMnnO0gevoaly8Za2Uv4Sj-uZBIE12qmf29XgEZZCMWQ9U8o6EDWQG2ceBfTRSYEBbMk4SD4KZXZY_kUiDTzsnDCLfdfhsPqEO687t7GwmWnSvn8QI1P82_JCZxir6BHWWDKi-SHcd09ujPepEYkMFdH5XfNbCErwPn3CXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زرشکیان دو ساعت و نیم پیش نیویورک را ترک کرد و هم اکنون حدودأ در مرکز اقیانوس آتلانتیک شمالی است. بسیار جای مناسبی است تا کوسه‌ها او را بخورند.
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24225" target="_blank">📅 12:11 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a6f13b5b5.mp4?token=qM8DJlhtumRzh6rW30MoudbnKkZyUUNTDkq1Z7Ga3eUbFOtg5FybnaxjFFKKK64Nfu-D__ZbvziRbFxbaha20oMdTVK8WR5WJJfQnHQL_jIc7jBtz9JFOe8RyoqlWAvHu4vB7hRmLz-BQsvhwTJF_ZOw9F9re9z9oAMlUbMzr-nv-7PnSH79AtybliPxZkijxFXc6HjoNESDQ9A6p7QCtYI0MjuGsQjPctYLX4iwPnX8yR0Us22_UBBadCoEFK499dGWwobuKHyynoYlGygQZVWf-O9d4k1u5ELjLSrrmjo88Ii8LPbOR_49m01WKNt9Tfvx_B3bgWfAG60H8CFZF6X2kioRLNmzhrLLrSti6IpNb_bwoBbF1M8DlouQSfBNSN0evNpr9zv5NTjNY34MvQrmNAD5q4I1KwsR_SMwelmeFF-TWvZeIjY7MG7RjltCr9DWOQUTXCJC6kGv73PpUoxqJ_f84CIRugglz5sRqkTzakOXjFwY1VkgUZIW1MwITdlC5Xky8mp2Dvlz3IV7vOqLlwVW6W-ExiYwUThfyTnX7Oejvbf9o0hkuOqvj_a-hSx29IoCeJUnlD8B2yCZ7KRdrZkG0zNKfRi4B--_ob6OzioXHpV_KwjLQLpLM0ybkmLoaQFrD-cHxnHKQA96gxAEqmpZNr1leLhEjeRUkCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a6f13b5b5.mp4?token=qM8DJlhtumRzh6rW30MoudbnKkZyUUNTDkq1Z7Ga3eUbFOtg5FybnaxjFFKKK64Nfu-D__ZbvziRbFxbaha20oMdTVK8WR5WJJfQnHQL_jIc7jBtz9JFOe8RyoqlWAvHu4vB7hRmLz-BQsvhwTJF_ZOw9F9re9z9oAMlUbMzr-nv-7PnSH79AtybliPxZkijxFXc6HjoNESDQ9A6p7QCtYI0MjuGsQjPctYLX4iwPnX8yR0Us22_UBBadCoEFK499dGWwobuKHyynoYlGygQZVWf-O9d4k1u5ELjLSrrmjo88Ii8LPbOR_49m01WKNt9Tfvx_B3bgWfAG60H8CFZF6X2kioRLNmzhrLLrSti6IpNb_bwoBbF1M8DlouQSfBNSN0evNpr9zv5NTjNY34MvQrmNAD5q4I1KwsR_SMwelmeFF-TWvZeIjY7MG7RjltCr9DWOQUTXCJC6kGv73PpUoxqJ_f84CIRugglz5sRqkTzakOXjFwY1VkgUZIW1MwITdlC5Xky8mp2Dvlz3IV7vOqLlwVW6W-ExiYwUThfyTnX7Oejvbf9o0hkuOqvj_a-hSx29IoCeJUnlD8B2yCZ7KRdrZkG0zNKfRi4B--_ob6OzioXHpV_KwjLQLpLM0ybkmLoaQFrD-cHxnHKQA96gxAEqmpZNr1leLhEjeRUkCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان در مصاحبه با شبکهCBS: هر بار که تفاهم هم کردیم باز حمله کردند و کشتنمان،  آمریکا به تفاهم عمل نمی‌کند، مذاکره کردن چه مشکلی را حل می‌کند؟
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24224" target="_blank">📅 11:54 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
