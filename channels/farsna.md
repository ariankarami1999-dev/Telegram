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
<img src="https://cdn4.telesco.pe/file/jWzjyXyU8AIkvGy5S8l6PfrHmHeK6jb2awPJr0bo0rgfbQ-R5Y-yH5Qh7ypRG07UDBYvRmb3gUuTRXLx7FzE4Rk_JiHodGhG8_yeIlx0yT_xOx_QyRZIfqrC41TC4tdFTB6f1CpvaOewuYjyBjf-Lnnj1j75HAHEwnGnK94BeKl0WBZQtyVu2a0quHRkEtuq1J2x1BmfhkuKJLJ3Qc1e7YpdUjyUTCJ1o8WWUG289gw-nPZikcnG-I9Gjju_EoJorehY39c8y6svTBv1-yFC7_X5MWBIfhEMkedfiBPOiP28K433V0OQL_P-cCrBgkpXPaNlV4bHbNCn5h3rg3uKIQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 12:47:33</div>
<hr>

<div class="tg-post" id="msg-454408">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7138496cbc.mp4?token=hi079440PeHSyA35GYwMfj80yromD0lfLSJPpDRpE40GuQ4wwgVy8XOb0DJzsd5xJGrUZjnwTEGXqUGsD-YUJFtk3wjXfTxM_2j-m9Y-dwG47tc9WUpzx8xI_QeO4mAeoOcyFJpB4BqrO14kovep1YWkzpkxc8gMY7UnK9sr1AWkOvBX0hnLnNIAyQvpG6bfYtd2uhAb0f0FcO4UsgvmePyaESSIuXFX5mRoMPai0EVoyxTII2ZW0RBuq2zgNonefX3w6grxthluPTvOp4urfYSO2IpRcY_vPDPDn3MOtcJcZLsgj0_xNx3mmC4ul02wMiygz4--5McmOttnoYmRHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7138496cbc.mp4?token=hi079440PeHSyA35GYwMfj80yromD0lfLSJPpDRpE40GuQ4wwgVy8XOb0DJzsd5xJGrUZjnwTEGXqUGsD-YUJFtk3wjXfTxM_2j-m9Y-dwG47tc9WUpzx8xI_QeO4mAeoOcyFJpB4BqrO14kovep1YWkzpkxc8gMY7UnK9sr1AWkOvBX0hnLnNIAyQvpG6bfYtd2uhAb0f0FcO4UsgvmePyaESSIuXFX5mRoMPai0EVoyxTII2ZW0RBuq2zgNonefX3w6grxthluPTvOp4urfYSO2IpRcY_vPDPDn3MOtcJcZLsgj0_xNx3mmC4ul02wMiygz4--5McmOttnoYmRHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت جاماندگان اربعین به شهرری رسید  @Farsna - Link</div>
<div class="tg-footer">👁️ 673 · <a href="https://t.me/farsna/454408" target="_blank">📅 12:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454407">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78cca7f412.mp4?token=AUcLcNJcMWFyxAzT8SmZdbpot8PZsoEhnLdHKblu2iMyvfaTakxMK18wanLc_USs8y7rj1j5wVccTquYXJFEfYLhVOF8RUhjbPFoboeele0ys9d8884kflB0tr-jrs31dnqlZB50sDfF3hpVFGy5Q_fWyzcHbsqC-mt6UGRwD9Wkbau-7wUZLCHRrsm3KCydwQBahk8kdp4UeJDZaSFJAFgBfOdDaRaMrbjHyteoQpl6To2aydKvpNWYolGQSQVW8_HG-jp8ayd_cijYcMDJCWldimfpJX8DCzFNMOHbpSiLURVg285W3foRZg8l6E4EtEVGNH9hjBkap-zP2ornbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78cca7f412.mp4?token=AUcLcNJcMWFyxAzT8SmZdbpot8PZsoEhnLdHKblu2iMyvfaTakxMK18wanLc_USs8y7rj1j5wVccTquYXJFEfYLhVOF8RUhjbPFoboeele0ys9d8884kflB0tr-jrs31dnqlZB50sDfF3hpVFGy5Q_fWyzcHbsqC-mt6UGRwD9Wkbau-7wUZLCHRrsm3KCydwQBahk8kdp4UeJDZaSFJAFgBfOdDaRaMrbjHyteoQpl6To2aydKvpNWYolGQSQVW8_HG-jp8ayd_cijYcMDJCWldimfpJX8DCzFNMOHbpSiLURVg285W3foRZg8l6E4EtEVGNH9hjBkap-zP2ornbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تایم‌لپس موج بازگشت زائران در مرز مهران  @Farsna - Link</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/farsna/454407" target="_blank">📅 12:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454406">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🎥
پیاده‌روی مردم پیشوا، ورامین و قرچک به‌سوی حرم حضرت عبدالعظیم حسنی(ع)  @Farsna - Link</div>
<div class="tg-footer">👁️ 1.69K · <a href="https://t.me/farsna/454406" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454405">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itOERk-YBY-dDBm28ZUvneWt3x5iqqYVOlpnQeCBLc8nPUqDZiBubLzv8C0XQF68vsCzJA6bpZp3UIRrO-Nz_m9Ca9L6hAafLW6-4SEdlzrlFLWfaaAjkI2TK7LmheaxeUgFjX8bVzVjvgcZKOFL09sxXHk0Aa-bUtZVahJg8-wpfPL1t_6cWnPQ0cuUDtUEdVMYf1FdGy6tc9vGFB7NMRz1I2tZLgnPVuw8UNjixA1XLO1d2cw0oD0G4Ugh1ov4xf7AVRNhpQEOvvR3lE1s_f9REuz8T4h5JFfDVpnqMhYltpohHhK0zOL1TLr9mJb9m7UWQsRT5G7BnnFD_p8PRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل در چهار روز ۱۲۵ بار حریم هوایی لبنان را نقض کرد
🔹
نیروی حافظ صلح سازمان ملل در لبنان (یونیفیل): ارتش اسرائیل طی چهار روز، دست‌کم ۱۲۵ مورد نقض حریم هوایی لبنان را ثبت کرده است.
🔹
مجموع مدت پرواز هواگردهای اسرائیلی بر فراز لبنان در این بازه زمانی بیش از ۴۱۸ ساعت بوده و پهپادهای شناسایی و مسلح نیز در نزدیکی یا بر فراز مواضع نیروهای حافظ صلح سازمان ملل در هر دو بخش عملیاتی مشاهده شده‌اند.
🔹
این اقدامات با وجود آتش‌بس مشروطی که در ماه آوریل با میانجیگری آمریکا میان لبنان و اسرائیل برقرار شد، همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/454405" target="_blank">📅 12:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454404">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9274f1a744.mp4?token=GcV3HIP-_E_0Iw2S2TGmK7j51Hv8nv8A1M9tenoNLvcpeCA8xrSaH7Wd7w36m5P0sXNV5OniFad148C8vmTi_kxbfn_t2yLgT5c8xNtOO4e2a6pLwr1M2YSxIb_NSbu_qc14R-6OUcBJ6I0Q8ePWEzdUv_djwnNLh7pGNZRsXK7RLAkk0B2UwEh3UGcaMmmDmKpmAj6QMKeTTkz3ZabFIvQuMRBqb5A2rRQjyhq1JGQxjZiZ7lfW4Wudx-3dtoHB50er2De7QG5qFMKp73uK1sxWb1KaJK_bKKPBGTWCUhP87BGvuDTIM1a5dDzumatmOOjUdHV737Suedev-0TYeQDrnq8cpKErZiieHxnnURel4idW6RixE0wBZCFm2fQHjp2QrLmaD4XyXUN40QGRfQgdXbQPQq_KVt3dAWcSg5NbUDdWe_6jJOVEKU6cveNvaBl_naqRlDqPfLFd5XYI959m-fNfg12rx6PWipXhPtFRAeuO4eNqJxShguZ__aWCNM9joio91GzglAjogNq_ohBgYdcTZ-D9nryYBbciPvQBgzaMF-TVsJDlKSQk1O9MjNI6LVpi6wkVCw96jOSeknfRHvzcoC-2eTb6BsPlX_I7SlSnwv5ipszWFwfoeD0bU480qyED1chobMRwLMf1CR7leVvXSTxgyXJjfLSnA5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9274f1a744.mp4?token=GcV3HIP-_E_0Iw2S2TGmK7j51Hv8nv8A1M9tenoNLvcpeCA8xrSaH7Wd7w36m5P0sXNV5OniFad148C8vmTi_kxbfn_t2yLgT5c8xNtOO4e2a6pLwr1M2YSxIb_NSbu_qc14R-6OUcBJ6I0Q8ePWEzdUv_djwnNLh7pGNZRsXK7RLAkk0B2UwEh3UGcaMmmDmKpmAj6QMKeTTkz3ZabFIvQuMRBqb5A2rRQjyhq1JGQxjZiZ7lfW4Wudx-3dtoHB50er2De7QG5qFMKp73uK1sxWb1KaJK_bKKPBGTWCUhP87BGvuDTIM1a5dDzumatmOOjUdHV737Suedev-0TYeQDrnq8cpKErZiieHxnnURel4idW6RixE0wBZCFm2fQHjp2QrLmaD4XyXUN40QGRfQgdXbQPQq_KVt3dAWcSg5NbUDdWe_6jJOVEKU6cveNvaBl_naqRlDqPfLFd5XYI959m-fNfg12rx6PWipXhPtFRAeuO4eNqJxShguZ__aWCNM9joio91GzglAjogNq_ohBgYdcTZ-D9nryYBbciPvQBgzaMF-TVsJDlKSQk1O9MjNI6LVpi6wkVCw96jOSeknfRHvzcoC-2eTb6BsPlX_I7SlSnwv5ipszWFwfoeD0bU480qyED1chobMRwLMf1CR7leVvXSTxgyXJjfLSnA5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مخبر: همانطور که پای رهبر شهیدمان ایستادیم، پای رهبر جدیدمان هم خواهیم ایستاد
🔹
امروز به نیابت از حضرت آقا در پیاده‌روی جاماندگان اربعین حاضر شدم و به رهبر شهیدمان می‌گویم همانطور که با تمام وجود پای اهداف شما ایستادیم پای رهبر جدیدمان هم خواهیم ایستاد.
@Farsna</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/454404" target="_blank">📅 12:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454403">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/499a783e28.mp4?token=TbTSuEj-exAYmZN_FdUPc5guNzeaYYjGdlOL54iJqEXtvVe4pq_jDzd2Dgd_RosNNGHN-5DbEus-WQi-_r_73rOtJeC4Rm20MP8iH_GhjXaTVAojDpNC0WFv5fmq_wIXMSCCc5XxXVThWKmcc5hQ3-JUUgxu1PHUaHjlAZiuHue-v0w9AcrH85PvyNP13wl1ltuD_4VTW4SX_PKfe5CjIKAQ-fx1ixWx5uJHPOIPndh-8bm8cfbt83CvyktaFNrZwQAP7zba31XSWY33yeYLKOsbu5fLLW8DFoEuwgBl7Nl3XbJq822bI9_OQ9kKEkIcngzs63HIQaNlOC9lyz-Zeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/499a783e28.mp4?token=TbTSuEj-exAYmZN_FdUPc5guNzeaYYjGdlOL54iJqEXtvVe4pq_jDzd2Dgd_RosNNGHN-5DbEus-WQi-_r_73rOtJeC4Rm20MP8iH_GhjXaTVAojDpNC0WFv5fmq_wIXMSCCc5XxXVThWKmcc5hQ3-JUUgxu1PHUaHjlAZiuHue-v0w9AcrH85PvyNP13wl1ltuD_4VTW4SX_PKfe5CjIKAQ-fx1ixWx5uJHPOIPndh-8bm8cfbt83CvyktaFNrZwQAP7zba31XSWY33yeYLKOsbu5fLLW8DFoEuwgBl7Nl3XbJq822bI9_OQ9kKEkIcngzs63HIQaNlOC9lyz-Zeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله پهپادی اوکراین به کشتی ترکیه‌ای
🔹
به گزارش رسانه‌های ترکیه یک کشتی باری این کشور در حمله‌ای که ظاهراً با پهپادهای اوکراینی انجام شده، در نزدیکی بندر نووروسیسک روسیه در دریای سیاه هدف قرار گرفت و دچار آتش‌سوزی شد.
🔹
بر اساس اعلام اداره کل امور دریایی ترکیه، ۲۲ خدمه سرنشین کشتی بودند که ۱۳ نفر آن‌ها شهروند ترکیه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/farsna/454403" target="_blank">📅 12:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454402">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0267901a.mp4?token=jMJ5ZEhA7fmmpVWwrHLJuz8pLUJq7z8HlhtQn0522rdGYZjTadnmK1M0wpBAIDcSTfrK6vRLJaLfk9zty7yQ7hIu5e2DFZ5nmL_kPTiVeUxUBDR7x-796EllVpIX4F8YeVorUbWGo_g4MPH0mz2Ql43N9ZxB7fhEnAqMHrt3UHvzaZOwLozUyMhGiGa1bkyqhDjxGJxMrTsXGFeLYF-Gs6rulyja96IBCVW_by0Ug0A3ccE6jp4mAlFZJUNnvVV0V8cU7A9MHvtqHVuULQHnVG8lxix-itSq09C0f8FgclQBjGRrp9OQehYGbGBsc0820G3MHfwTV8IT04CGWjsiPZVsCk0sy9Tk2Xolpfa7pscZfXovGcw5d4IcQjGnhVUsXYmsMqE3vgJ69wtZ21fB2y4ywEF6d8lImgXIN9VWbRI-gYheQ7aktOd2cGkYGSFnh6e9YXeQ4NKCJ5jYgZvB-j3GyyuMyjwfSuAyOqifZ_FHumnHxOj7FVrNzZk9PWkrIxCXhSFBRzgoAxr753sVRI8S5sUpUze82JGoKIgKYWumD66lByanWxPDATvYxEPAHiel8Aqwzf0xGi0v2Dv415_EexCfWz4jJVTtSkW-Ep3b5pG5xBM5zHJp4zfFZhGg53swgUBhktH26u1tMEydeUlxZ2YUOpLcUQ1KbMm0I7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0267901a.mp4?token=jMJ5ZEhA7fmmpVWwrHLJuz8pLUJq7z8HlhtQn0522rdGYZjTadnmK1M0wpBAIDcSTfrK6vRLJaLfk9zty7yQ7hIu5e2DFZ5nmL_kPTiVeUxUBDR7x-796EllVpIX4F8YeVorUbWGo_g4MPH0mz2Ql43N9ZxB7fhEnAqMHrt3UHvzaZOwLozUyMhGiGa1bkyqhDjxGJxMrTsXGFeLYF-Gs6rulyja96IBCVW_by0Ug0A3ccE6jp4mAlFZJUNnvVV0V8cU7A9MHvtqHVuULQHnVG8lxix-itSq09C0f8FgclQBjGRrp9OQehYGbGBsc0820G3MHfwTV8IT04CGWjsiPZVsCk0sy9Tk2Xolpfa7pscZfXovGcw5d4IcQjGnhVUsXYmsMqE3vgJ69wtZ21fB2y4ywEF6d8lImgXIN9VWbRI-gYheQ7aktOd2cGkYGSFnh6e9YXeQ4NKCJ5jYgZvB-j3GyyuMyjwfSuAyOqifZ_FHumnHxOj7FVrNzZk9PWkrIxCXhSFBRzgoAxr753sVRI8S5sUpUze82JGoKIgKYWumD66lByanWxPDATvYxEPAHiel8Aqwzf0xGi0v2Dv415_EexCfWz4jJVTtSkW-Ep3b5pG5xBM5zHJp4zfFZhGg53swgUBhktH26u1tMEydeUlxZ2YUOpLcUQ1KbMm0I7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تبریز امروز علم خون‌خواهی را به دوش کشید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/farsna/454402" target="_blank">📅 12:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454401">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67eb5295f.mp4?token=H-fIF0nMyQLsHO9Q6FuWVhW0aaxdJeDNLljbs3ALfobvYeZqZh-oR_opFNF3mk8Z664kF-HspIFrEUZNxAo4dEK70dAMCRiNP6IrBHeOwp8E-KcNM2u5QZhlYjYp2Qjr1KaQPw8j0KcxCJdhy9uBNF0Hu6tvxawoG0cVCOnVCINEXIjzQErZekgqyFyP0yPcQ8fEhd_XDu-lsHlvkvj9GHYHj_z1vSf8iLgMWkSv7lm5fJgTD34Z2lP4AcXPdW9A80NM5yKfUaHm99RAmgaEOcNfcQnwXhCUG71W1LtFIZZOxFKlDzGDhi1JC7gCr7n8FHt5v_ZTLQTUUrVacsIxHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67eb5295f.mp4?token=H-fIF0nMyQLsHO9Q6FuWVhW0aaxdJeDNLljbs3ALfobvYeZqZh-oR_opFNF3mk8Z664kF-HspIFrEUZNxAo4dEK70dAMCRiNP6IrBHeOwp8E-KcNM2u5QZhlYjYp2Qjr1KaQPw8j0KcxCJdhy9uBNF0Hu6tvxawoG0cVCOnVCINEXIjzQErZekgqyFyP0yPcQ8fEhd_XDu-lsHlvkvj9GHYHj_z1vSf8iLgMWkSv7lm5fJgTD34Z2lP4AcXPdW9A80NM5yKfUaHm99RAmgaEOcNfcQnwXhCUG71W1LtFIZZOxFKlDzGDhi1JC7gCr7n8FHt5v_ZTLQTUUrVacsIxHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: استعفا نخواهم داد و خواهم ایستاد
🔹
من استعفا بدهم، رسما اعلام می کنم؛ استعفا نخواهم داد و خواهم ایستاد؛ می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر.
🔹
ما با نیروهای نظامی کاملا هماهنگ هستیم؛ همه مردم که این سختی‌ها را تحمل می‌کنند برای ایران است.
@Farsna</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/farsna/454401" target="_blank">📅 12:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454400">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fb431df3.mp4?token=R3sRlHPQRUjbuHJ7SFnkKfy5mFqSInjFdposwUUnioIXECOTAVyRKMfzm-_OysKfb-QTmaBraZYCwuPyDXXLu19E15aFpLES_EjUJ0H_VvWuCHymTDRKhh-wVoKjlXgdmiZCWgSBgUZZooyl1jI2EBRtPhQRq6nyjrwi3F5-lsEcM3iYjupCe5JSEZ1oFY9cFcH2FwEmL4vsu9SulmWbK3qjJyHNxwcZ0sa8w_03dbYm3CqJJ0LBNjmXJZ1wIAOkGxh7K3kqFW1DLPruv9XiRtZr8_dmjgcy4VvuvDgcH1RD-S4lqY5J24f9J30U_Usc5-NEe2OIn3Lll7Qb6k2244l2G2FgULJrzPN28c2hY8A2QoFAIqEl4O1C9abTDtlKgasQAHLxR-2N-e2U61-UUdngPbcuXFIYeWg1vP-fpLg75BhJUTLH6k4XjEMVfRz5Smw4dEC-zlMziLLPlQfT6amWfTZlJAYduB7Mquwg1mEh84yw9sA0eEb7MMoWfE95j2-C11EqqB1puJpheV-tTX1ZaDIow1vE2kLUr00RJItmKWtwCEPUOP36EEXknDQzqbXbvNFgx14SSjAlO_Nhy2IIkrrp0ahZABvJZJqri1Y7ZFm9ky7VIN5vAPii7cmCRxRpFgfywn0mR1ZUkFG_jCpbKU13XrI_vQaTxDQiIMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fb431df3.mp4?token=R3sRlHPQRUjbuHJ7SFnkKfy5mFqSInjFdposwUUnioIXECOTAVyRKMfzm-_OysKfb-QTmaBraZYCwuPyDXXLu19E15aFpLES_EjUJ0H_VvWuCHymTDRKhh-wVoKjlXgdmiZCWgSBgUZZooyl1jI2EBRtPhQRq6nyjrwi3F5-lsEcM3iYjupCe5JSEZ1oFY9cFcH2FwEmL4vsu9SulmWbK3qjJyHNxwcZ0sa8w_03dbYm3CqJJ0LBNjmXJZ1wIAOkGxh7K3kqFW1DLPruv9XiRtZr8_dmjgcy4VvuvDgcH1RD-S4lqY5J24f9J30U_Usc5-NEe2OIn3Lll7Qb6k2244l2G2FgULJrzPN28c2hY8A2QoFAIqEl4O1C9abTDtlKgasQAHLxR-2N-e2U61-UUdngPbcuXFIYeWg1vP-fpLg75BhJUTLH6k4XjEMVfRz5Smw4dEC-zlMziLLPlQfT6amWfTZlJAYduB7Mquwg1mEh84yw9sA0eEb7MMoWfE95j2-C11EqqB1puJpheV-tTX1ZaDIow1vE2kLUr00RJItmKWtwCEPUOP36EEXknDQzqbXbvNFgx14SSjAlO_Nhy2IIkrrp0ahZABvJZJqri1Y7ZFm9ky7VIN5vAPii7cmCRxRpFgfywn0mR1ZUkFG_jCpbKU13XrI_vQaTxDQiIMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اربعین شد ببین که جا ماندیم، او به مولا رسید و ما ماندیم
◾️
روضه‌خوانی میثم مطیعی در مراسم عزاداری اربعین در جوار محل شهادت رهبر انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/farsna/454400" target="_blank">📅 11:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454393">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQgzrkVQ50mL4DCsuK5nAn4YWfYjdneNsF-u-L6xcoIdgVtHS9upQsUJceEqXD7YTLAygJMWxFVTa5Ylzg2AsQK_Vhjs1VVq7gDtj5gcQn7ifZN3zx8Hw87mCprFklKbkTpARRxGKlq98XpcP6wShYJftDBQeiYfI53RwcrHGut5T2nUD7QY27qhVQmF4j8QHqDcmgpltEJA9LFvi3ZDHZanqr7kwu5_hFJIGKK1h8Fft6ycjyt4xi32iAtGY8O8lUefBnvCXzm0jD0ckozP_u7-DRwp5ihx31Q369-WuznZnBeSEYzh11qkKOik8Ufpn7EUtqVfAPIsY-8l09Hz8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OnPOJiam1UrJtNsaRa4V9QLBoa6qu4kd4TdAjnpK9KE9h9F8tnHJfdrYdDZJbIvXWRrAZFkTmWYmIyaM5NP2co2jilQK3iFV3j1_HjUa9e97dnZQpA1AO9yKEmpUX2Cutgn1HPTJ6D9cv2vCdG2GgSdSyfv_EVwN1iZwepguL57oD-biQN8jVrjtO1Sus-suLs2z6s9Y-u6Xa3EDeTGHFXEr7kT_Bx263D5Fsx5e3zBE0JwLX5lQD422CWtIVv56AClJNLoPSHE7nvfgC7RSNr68Glkxsx4Kd3VyeIPUNXoZTUgCdqwoYfNCc0_KJLN3sFy_e2wRnxF7ONJben6LgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfV_T6nALURZcazjbm1DyZgrK3xGnufgagoWL80tgdQRnJJDZwgrxEjKNy4wW8Vg83YofB1AMbi8CLY1elz_V2fmoN2dFIr8pCLw0O5IEF86U3HG9HKIzJkLt_KX_sDOYjWwdBrwrpY-S62xM04umTZzEDHH0MrldcHxI5lpLsWUHxdOX1i2pSy3fxrxpKba2xPFR5krnw30ulkWcefHLsjfHV25hsE9dP1uBJqaJ4DzrPp6sIW3mND8xB5A8-BKZFEArvG1ODKX9TSQUqol6zToRL1LuviIvZsnT7lHri3NOKGAnsZKzGqNtDDHX4i9hd2Rkq4MkSU1V_uauVJ3TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHmXs3v_lNyM8QkUjr3BzzBlrzdeoM4W7vHIWAhjns-qHs9sO6EjS_4Rx2sXoPpoQN-U5-D2uxcbBjzVo0sL6XqNHObomcgPSW5YA_qf5RCf6RotU1kjBjv2Ijrg3ENVduWvEJ2eUKqyYAj2wK08SPXitrdKynlcAa8ul1mMp1ibXHj9JvrlJyNm_V4LfGBzmHktIgc6GVzTDFnhwC5RvVTgXea9pHeo50nOid9q7qc-_twU367SBwSuEPixYOLCrLuAH-fk0Fxg9s7RZ6L7Bzxk6W40ceLKsBi_Y7brtNCzzLoL0rK2FB3ekyIRaasqOumeEoUiLBYMZlkp371t_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFvpfJJyf1NOZvL6M6Mb_MtebAIE-ltq5NxG616waZAVgv3Dg9i_j4hrJ4dYDoTKXXWPeWIkALDOjg1-Hk7YQD9K9mwvoM2AQFf1LAN_HxY_HF-B6hZhl1p9qHs5xcTuuIMDQThbOh505DVdm-THKObELnY2fvXNU2cDdKdKxMEYJEx3Y4YfDrgCIwIxwpYBexim24hdmosvBWYhQrZ2F64tDk9asNRRWXxgaIwBN6VTddSQ8H8Qs7cI2s2ZnUAObBKj8oIfVxN2KGzIcoGBWyYvm7Ry93JDJZZVluCIWTXpPIEWmyDAlqEc8mRY2GWbuB-eJaUapbIYb9KPhBvm5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HuM3O-iirfwR8zZUviV97X6wK-y6bXG-LbseWCJp10BUII1yraIOvrZ11XW8X604zaMeAC9WKI78hwyHIWyKa9swOfQvdTm0HelYbTHdvr4YMCOh8VVbPTZ-CyBg_MFszI3J7QomhBvYdWZ2K3upbI6v2avvE4hgIOATjb3TRA44E0NfBNJnC9hAIt3qwl7IzW-Oy_rUgvu99gMlVIJV6kAbExdpEEgq4Mq0PqFnTFqMQ6Q--LFp_YMo1TM4srrGqwD9aUBddT8TlHi4O3h8VmsBIhJBeEeNz0d5h7E6ZIQh2a7UOs3NPpV1YapCC5TxqhsK_OwB5aiuo7gbT5D4VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tYZn96c2HHBL8OZCQhsXVxZczmv3Odr0a7h8eQbBqFarZ78JyJgRunxWOfCQnvyOIVVan93P4GOBYCt_r5lGSHgNnH_aI6PKELCdv8PVdbYwGT9GtQBZZJtsApUQyh6CuVI47yJ-4e458FXE_wd1YrS2Ix2gegtxEqTmcRY3L5RKtLS-VQxOP6wOn8KHMGaMbPmxerQnjTktWcUULFUvEUFD2V-ksNJTDFZvZWV31ZGm6Qihyzhxz8OzWh73TQA_6sLMk61ue_MQAT8h6vmtOHeHHetSKM1l_XFpc5e17fSRJaRv_0R8VJZob0nl65pAobV1C_mhXFEb0rBA-j1D3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عزاداری شب اربعین در کربلا
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/farsna/454393" target="_blank">📅 11:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454392">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c6dd698b.mp4?token=FUzq1920sD7LO_uopVfagK05EvjvzAiQOHxg5kquN6ZMuAHjC-eSPnQF8YGeReWAmB_aph6-gamYDoqJnRLvK6TiRdpBqCKEuk-xzCTeGHuvJ67PHsmoWD5pn4moGDk_ZYyfJJo3qDGx3rPn0zq2jKttgnApqxkV91eO_hvDuXlbntQwjI5c7e3mVr4sRrnePTjw5mnDsRsUwsJ2e6-Cd4HDTyZhcjS7TLNl_XWbSBysHTFpYQMbFCdKiNmOL533byZCNr60jyGa-sfVS6buzQBWXNQJ3zozmG0RM5K85YeEmrYIpeq5lphBLf08tqx03X19Qe44WU94xUhoy5ztxTaVUW1OfSTosBcw0qb9qY9V36fW2mSg_0h2O5OetCits6crrg7AskHszRKtwCjIQq2ee8ugnlCYc93eMEVQf3_uVaNFjeejmUZ2sFTULzAkTWQEAitDkxzzeKbSykqWkUUSyIFKukJmILO-K2jZMPuh8w9q8AczFqsYl4Jd8JDcaiDCMD-fVQLWGt2bhnDqfNRTm327iEbMLNHxpgrKohhxA5AZFYgrwU6u-s5WO5a1ZvfdBXmawcLYb8Ogrqmk7_ltDBYPKQWCjzl1Ymunjl1VAYd7Nf7cuqHLLSOEu0rYx1KNbiTzkO1XzuhUAh0qfYVK05-i3ydAdk_doHG2mog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c6dd698b.mp4?token=FUzq1920sD7LO_uopVfagK05EvjvzAiQOHxg5kquN6ZMuAHjC-eSPnQF8YGeReWAmB_aph6-gamYDoqJnRLvK6TiRdpBqCKEuk-xzCTeGHuvJ67PHsmoWD5pn4moGDk_ZYyfJJo3qDGx3rPn0zq2jKttgnApqxkV91eO_hvDuXlbntQwjI5c7e3mVr4sRrnePTjw5mnDsRsUwsJ2e6-Cd4HDTyZhcjS7TLNl_XWbSBysHTFpYQMbFCdKiNmOL533byZCNr60jyGa-sfVS6buzQBWXNQJ3zozmG0RM5K85YeEmrYIpeq5lphBLf08tqx03X19Qe44WU94xUhoy5ztxTaVUW1OfSTosBcw0qb9qY9V36fW2mSg_0h2O5OetCits6crrg7AskHszRKtwCjIQq2ee8ugnlCYc93eMEVQf3_uVaNFjeejmUZ2sFTULzAkTWQEAitDkxzzeKbSykqWkUUSyIFKukJmILO-K2jZMPuh8w9q8AczFqsYl4Jd8JDcaiDCMD-fVQLWGt2bhnDqfNRTm327iEbMLNHxpgrKohhxA5AZFYgrwU6u-s5WO5a1ZvfdBXmawcLYb8Ogrqmk7_ltDBYPKQWCjzl1Ymunjl1VAYd7Nf7cuqHLLSOEu0rYx1KNbiTzkO1XzuhUAh0qfYVK05-i3ydAdk_doHG2mog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امروز حال‌وهوای بروجرد کربلایی بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/454392" target="_blank">📅 11:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454391">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e301c8ca9c.mp4?token=lRE-KmpBOtoJ0PNeywrqgHq3SyWy2asFMy_cFvC49FTwRgMQ9oHmSRRf1cqq69Xrk8g1TmQeMMG0oT0E21Ag0z2eQ5AJxgyBN_Zhw23XYJOvMkrOkXFKgWo0wbl-8f1OLWveuyxk44EJPw_VWCtgoMYK3R-nh2twqzu3qIREruLp9qeLugIfW2zPDE4tuuybgXtVsWbNhxObA2oY1_WgI8epHK-RXHpfOE_Z1y_5zi_SNs6FJhZXxRpISeInxwWhgF-zUK7COi3rFw0tgFj98fkhRrBP0jlarfG_zQ2mQj2utnIajWkkWqqyX7ALTakQeoguHvqUe_tiqvctKjFnaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e301c8ca9c.mp4?token=lRE-KmpBOtoJ0PNeywrqgHq3SyWy2asFMy_cFvC49FTwRgMQ9oHmSRRf1cqq69Xrk8g1TmQeMMG0oT0E21Ag0z2eQ5AJxgyBN_Zhw23XYJOvMkrOkXFKgWo0wbl-8f1OLWveuyxk44EJPw_VWCtgoMYK3R-nh2twqzu3qIREruLp9qeLugIfW2zPDE4tuuybgXtVsWbNhxObA2oY1_WgI8epHK-RXHpfOE_Z1y_5zi_SNs6FJhZXxRpISeInxwWhgF-zUK7COi3rFw0tgFj98fkhRrBP0jlarfG_zQ2mQj2utnIajWkkWqqyX7ALTakQeoguHvqUe_tiqvctKjFnaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویری از زلزلۀ ونزوئلا با بیش از ۶ هزار کشته
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/454391" target="_blank">📅 11:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454390">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/730ba09e37.mp4?token=QZ8ZsdWcVfnwHxDzMktI_D8Y0BnB3UPPnm1CbyOSAeEOcnnUktzsrnhSWLcfZl9CSvkHB9daW1l1bf0S5JGF_XrFU5_jQfGZFJAnKdX48FEU-_OLEybKIU4A-X0eUu8gGt2Od6Upx2G0pivVDOf1ouv0fK6tbefEMXl3SlJ_T74WDiq0Pu7GUDqU_tPj9-xTJKP3OEdX7RfEeMQCVP8JX8fHD8SKxnqLsvoG5UL7QhrqhSbEFd8dCrMqJDCpTNQjoL0jw3PBCLvvsuTRvKuUBMy1bxXGdCCbuEwXLSuFqtp2sI14l9Cwh7XPdEL1yYDO737Ivt_BB2Ma3oKN0dppiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/730ba09e37.mp4?token=QZ8ZsdWcVfnwHxDzMktI_D8Y0BnB3UPPnm1CbyOSAeEOcnnUktzsrnhSWLcfZl9CSvkHB9daW1l1bf0S5JGF_XrFU5_jQfGZFJAnKdX48FEU-_OLEybKIU4A-X0eUu8gGt2Od6Upx2G0pivVDOf1ouv0fK6tbefEMXl3SlJ_T74WDiq0Pu7GUDqU_tPj9-xTJKP3OEdX7RfEeMQCVP8JX8fHD8SKxnqLsvoG5UL7QhrqhSbEFd8dCrMqJDCpTNQjoL0jw3PBCLvvsuTRvKuUBMy1bxXGdCCbuEwXLSuFqtp2sI14l9Cwh7XPdEL1yYDO737Ivt_BB2Ma3oKN0dppiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشاهده ۴ پلنگ در ارتفاعات میناب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/454390" target="_blank">📅 11:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454389">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzPRtX9imfl3JzZiwD2oOYUCr6zELnGDRE4lrsUoScgXYQPrR4XHCKY6-J1NCfV7tO-bnmtM7ymbl7UPOSiUXuwVLq5T6qnWG9u4kf_7HYpOlM1DniXYqBeFIRtAX9Png0vgrBaG56AZphW3Effb2uWac09l3dgHWRP9-IW9Xq3_-c6pOCTbN70OflFcG77x1RtdU49TM36Pbf5T3BeCILiRCWOkrzar6KW4d1-vYk6nEbvMleiwUTXlXCyZmPZKbraxnHjmbysUbjWlO2sFfIIcswNnpTVg2gwVk7YhZ_8aa0XHM-C6u-TbTG21g-eVBv5zesbR4lxf1FgLZ5acjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرعت باد زابل به ۱۱۵ کیلومتر بر ساعت رسید
🔹
هواشناسی سیستان‌وبلوچستان: صبح امروز سرعت وزش باد در زابل به ۱۱۵ کیلومتر بر ساعت رسید و دید افقی در این شهرستان به ۹۰۰ متر کاهش یافت.
🔹
تا پایان هفته، به‌ویژه امروز و فردا، وزش باد شدید، خیزش گردوخاک و در برخی ساعات طوفان گردوخاک در منطقه پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/454389" target="_blank">📅 11:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454388">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e32388821.mp4?token=k3B8jlKN4thhi1Bo3gG7liaRxTntNc3-PQZJRfsZR-3YwYqxmImxOmyg71RZ0P0N-sPM8ukS79n5E2cAYdVXiUN5THkI5q8N5yUwbF_wHeaEG_KkMpGBr0UECVgxvaQxMMKxzagV02mQbfXK7enLm5rF25IwrBiKMrlii2menJahLFHZUnhxHG6FMsGGx7bF21NR1R0lm4oVreN1brn6kcNMhapszbRfsa5xbwFucrZMfcHHF0afNm6tGSehy4yecRNq3mgYQtmI-xNOjjVlgH9flopwBbqUEC9OC6NU__frUryAUCOOkdLZJJpFlnPwpVofC3Gffhwp9R4QPZNpoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e32388821.mp4?token=k3B8jlKN4thhi1Bo3gG7liaRxTntNc3-PQZJRfsZR-3YwYqxmImxOmyg71RZ0P0N-sPM8ukS79n5E2cAYdVXiUN5THkI5q8N5yUwbF_wHeaEG_KkMpGBr0UECVgxvaQxMMKxzagV02mQbfXK7enLm5rF25IwrBiKMrlii2menJahLFHZUnhxHG6FMsGGx7bF21NR1R0lm4oVreN1brn6kcNMhapszbRfsa5xbwFucrZMfcHHF0afNm6tGSehy4yecRNq3mgYQtmI-xNOjjVlgH9flopwBbqUEC9OC6NU__frUryAUCOOkdLZJJpFlnPwpVofC3Gffhwp9R4QPZNpoIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عزاداری جاماندگان اربعین در سنندج
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/454388" target="_blank">📅 11:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454387">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">‌  دبیرکل حزب‌الله: ما به لبنان واحد، متحد و غیرقابل تقسیم اعتقاد داریم و حمله به جنوب، حمله به کل لبنان است
🔹
لبنان نمی‌تواند در حالی که جنوب آن درد می‌کشد و رنج می‌برد، به ثبات برسد. ثبات در لبنان، مبتنی بر ثبات در جنوب و تمام سرزمین‌ها است. @Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/454387" target="_blank">📅 11:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454386">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت اربعین</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/farsna/454386" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
باهم زیارت سیدالشهدا در روز اربعین بخوانیم
@Farsna</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/454386" target="_blank">📅 11:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454384">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن زیارت اربعین.pdf</div>
  <div class="tg-doc-extra">2 MB</div>
</div>
<a href="https://t.me/farsna/454384" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📎
متن کامل زیارت‌نامه سیدالشهدا(ع) در روز اربعین
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/454384" target="_blank">📅 11:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454380">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4sE3Pl1mQ31p8Z9EsKYWCw2kCGrk9k5OG1KcYjrvxi_EnmJuMLpD4LiqgRZq8q39qxuTOKFL-ojj0IkkchWimRUBX6KR-SHIQ8DyM2Ioh1ZkOJXnMBYR1FvWWKxKw1fNDv5dov6xg67o1uwdKEllNkCI5WO-Vqg5HafNP4zO-cgQ5ZHFChsMgsU2gGs-ZnEdQIzF793boFDio_yM0AAFGrHUTmruvNW7FykJLvHPH1ZK08p6_qKP3xEP5_pUYXRPwhlV3HskbIbY26-8vfRXs7kecGSV1c8-SlqNqj38hD8C5sSEzPrUp_e1Qys73efFa6oimNwbud0Mzz_gzxGTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O07LxqEuOK4Qt2GGEianarFftbTxD6C5WWDNd44mBqvxJd5t_PQbuGChBE-luPGhFG5bGZNctQzTt9aLkujbaocwXEyxU5nbk1mb2BDs8EDpsTnGL64H6uiUS2ZSQkA7GoJIuBBbzyoU_cmmL60i8BF8PE8JF5Mt_jjcNc-ioOAxsnvb4A6fQh3N9ZxNZSwBg4MbQji61z9Hf9j7SFPG2HbyKMLAIU-TUut_HZDhRihs6ZA8qRpWGUO9INU2sXiSddCABpUmklfU_jJxji-LtJbyIfSruLJzpybjjGRGC_Km0BYRjzmcssmYlP9tMYqHoZHbdUet54gYqy5hmVR7Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QcVY-oB-_gAjv3ITUbWpz2LwxhkrzwQAF3HYeYVVLzGiZGxYVm22crTDDnqaxzME51sWpmDPQ2YbPRK7jA_W7F20Am0XNsV57bo3mH8aYONn2zbPbH0aZxpFAXYtZvrQaiN3dgwz1-zKq1M4224x6zYUsqoBXMPSYaqcR0toVQHnQX5O9NbO3cE8MlW_GTTPKW7esOsiKkILkjSKntgIqyL0gY_kiVdlA3CBvVe13VdgyZa1ZWTAO8QF9ljid-ONBJhrbKbBhlkjVc5id9uSV1J9YfhJw_SilptjGHqSyFN8D_F10-n3h9p_w07--drW5AqnIKc94eEv1ESms8qBxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vn3K6OgGRx0FupnjSf9Causryz_WEjgB5rWvqS3HVHLJ53QoTbxaE0aYIbgqL6zjgjB-S8EEqVAJZuBuGXpOic-W9UelMS-Ab3vu1dhFzS6o9ZL3jT-y3_axwyRcxnw9TmEoO5srgpZ1eXxAmjPyPiGD_Z_IymArD0Az7q-ZKxzCLpxdu8MdCcRGyuFjmXLxjYFvjE84TDRUVCShbF8zPK6SPmdtbi5v-f0kf-KKjWR42N51iFAQIx9wCVoDvsbRLuD3ea-e0Z7OxRQ5HRM5GmxHWcVnNw1JL8OETPcV8Vz8DCW83FaoqwV6VqG2FuPsg6zy_DwdKVIZuX-UbrTZxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ngNxccuBnC4aVv0pqALg_uNRjLAFtowCrfWX7VQ79q8tRofnKdmajb0q08kQiTyeZldVC00N5lnokvo_jvAOJQhq9p1b4gt-W6UtUzmTuldBW3VytYXuDJ-E8sapgvWHf-C0bewqiKnfuS814Y2z4a-fEOkWUGJKJxb6kiOp0AGUCteXjYgrNjZsKboA7l3N2UfHRARGRwjcr2w8st2XSKUplRjeKG2D29ApVbVBPc7N4HmHyHhFFVbufzUtt-PNw2EYYow48t90PWZe5h4hV10cX1U7zD5EgXQIakN8H3TKvyT6_oeI6TJWEJ6X4ZfRHZPwEU_kokAQ0W5X1_mApg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مرز خسروی در روز اربعین
عکاس:
بهروز احمدی
@Farsna</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/farsna/454380" target="_blank">📅 11:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454379">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">‌  دبیرکل حزب‌الله: رهبری آیت‌الله سیدمجتبی خامنه‌ای موجب پیروزی‌های بیشتری خواهد شد
🔹
ایران توانسته استوار بماند و ثابت کند که یک کشور قدرتمند است. شهادت امام خامنه‌ای، شهادتی پر از عزت بود و به انقلاب ایران استمرار بخشید؛ این شهادت، به جای آنکه باعث تضعیف…</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/farsna/454379" target="_blank">📅 11:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454378">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‌  دبیرکل حزب‌الله: مذاکرات مستقیم تنها شرمندگی، تحقیر، ناامیدی و تسلیم‌های پی‌در‌پی برای لبنان به‌بار آورده است
🔹
اسرائیل گرچه در عرصه سیاست دستاوردهایی داشته اما تا زمانی که مقاومت، مردم و افراد شریف در مقابلش ایستاده باشند، به نتایج میدانی دست نخواهد یافت.…</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/farsna/454378" target="_blank">📅 11:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454377">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc83e39827.mp4?token=gKzZ6ND0-AaD-oBSPcl3tSynqzLUDVT7n3OUZqND_yCl3yYia4ETu0OIqooxMDg5ubI6lIxA5fGISxF4xk9zgF8n3gDrWRF6CkKI2bTlSlVIW4fh1zYdRjcnkpUvH6dO_EUxCbca0yrp0h5Nu21kN198MWVGxrhN9tsqxo3F2YQhwnall1voRv7wQDZrTdT48BOsQAQGdJiFPvcrE8aejM8ee7wI0WbLbiCG7B-CGSHj-gkot8YF1KEq7J7NEfaioiRPI101VDUJ_UMEfvzCw_LlJGMbSbenrAkQrfGXCQBX_FXEOTm5MaCxgeVecO9onX2v88GFwxJIk5I8u2E85A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc83e39827.mp4?token=gKzZ6ND0-AaD-oBSPcl3tSynqzLUDVT7n3OUZqND_yCl3yYia4ETu0OIqooxMDg5ubI6lIxA5fGISxF4xk9zgF8n3gDrWRF6CkKI2bTlSlVIW4fh1zYdRjcnkpUvH6dO_EUxCbca0yrp0h5Nu21kN198MWVGxrhN9tsqxo3F2YQhwnall1voRv7wQDZrTdT48BOsQAQGdJiFPvcrE8aejM8ee7wI0WbLbiCG7B-CGSHj-gkot8YF1KEq7J7NEfaioiRPI101VDUJ_UMEfvzCw_LlJGMbSbenrAkQrfGXCQBX_FXEOTm5MaCxgeVecO9onX2v88GFwxJIk5I8u2E85A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشهدالرضا، کربلای جاماندگان و ملجأ دل‌های بی‌قرار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/454377" target="_blank">📅 11:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454376">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دبیرکل حزب‌الله: سلاح و مسیر جهاد حسینی را ترک نخواهیم کرد
🔹
شیخ نعیم قاسم: امام حسین (ع) خطی است به سوی ظهور امام مهدی (عج) و امروز به وضوح اعلام می‌کنیم که ما با امام حسین (ع) هستیم و او را رها نخواهیم کرد و به حمل سلاح و جهاد ادامه خواهیم داد، و شما را…</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/454376" target="_blank">📅 10:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454375">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3c302a35.mp4?token=KhGSJsP-WOD0CWXFcUBnKU0UvG1Lj4K45j9ODPGhJv_517UDb9Wq_zwzbXVRo5p04zPDfXj0OQdhoDAVSVOwPIwOE6os1PwSMiQ4kHmHgctW0F9BhVd4mxNIrNAFkvQ-k-0fEkLhPMndOnw0hx41FXWsAe1wrajuVVBPFEMlj6R5yrurDdpoDNBL6NWWrrx21N134LyGGDH0tF19FZwky-QruwE47KmeVsykpOXFKjCbiJsUIBtSGGFRi4dkuvP3t2ENcdeAtwGM_RtFKlk3HyBMZBl8sYfZYhhFDdyQPhuBaf0RoQINWVrQnyKsr4nCRVmZboJgQFM0jxvcLLEs5lKfprk5xVocFzdQ03p2TZqQFZ9FPUAAIDOCYspv56uQ6vEVmshIlJDYQ-2Qs3ge-Zvb2EJBdSKyYMnZUl2WnPwD6M1O-dfrvc3GiRkYjqx_Uq7XmbKclukLuL-4Aj648xk29ZABhSDD1LgWl1topjtx0YdHoxZfMtscG1qnMECxKXO-P_s0a0T1Uv0g8sz8N0ULsydTafwfdiHKfiSdk1-sYsK1a7suW7rRWnqp_9zfK9YY12enntMHxEzlC3AdY0rYMuquw7IT0hWRR6R1hB8Qi6s88Nwv1cxQ_kvmjlmtYSPtYlVwnWjqCBCOTNqW3YXXsPZhuiOSOFn_J2IpYTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3c302a35.mp4?token=KhGSJsP-WOD0CWXFcUBnKU0UvG1Lj4K45j9ODPGhJv_517UDb9Wq_zwzbXVRo5p04zPDfXj0OQdhoDAVSVOwPIwOE6os1PwSMiQ4kHmHgctW0F9BhVd4mxNIrNAFkvQ-k-0fEkLhPMndOnw0hx41FXWsAe1wrajuVVBPFEMlj6R5yrurDdpoDNBL6NWWrrx21N134LyGGDH0tF19FZwky-QruwE47KmeVsykpOXFKjCbiJsUIBtSGGFRi4dkuvP3t2ENcdeAtwGM_RtFKlk3HyBMZBl8sYfZYhhFDdyQPhuBaf0RoQINWVrQnyKsr4nCRVmZboJgQFM0jxvcLLEs5lKfprk5xVocFzdQ03p2TZqQFZ9FPUAAIDOCYspv56uQ6vEVmshIlJDYQ-2Qs3ge-Zvb2EJBdSKyYMnZUl2WnPwD6M1O-dfrvc3GiRkYjqx_Uq7XmbKclukLuL-4Aj648xk29ZABhSDD1LgWl1topjtx0YdHoxZfMtscG1qnMECxKXO-P_s0a0T1Uv0g8sz8N0ULsydTafwfdiHKfiSdk1-sYsK1a7suW7rRWnqp_9zfK9YY12enntMHxEzlC3AdY0rYMuquw7IT0hWRR6R1hB8Qi6s88Nwv1cxQ_kvmjlmtYSPtYlVwnWjqCBCOTNqW3YXXsPZhuiOSOFn_J2IpYTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرما هم حریف دلتنگی جاماندگان اربعین در تهران نشد  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/454375" target="_blank">📅 10:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454374">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87cafbf9ca.mp4?token=Cqa5hHDOIhoMoh5XtEO6IjsXB328L4U3DumcS4wCyTlpNaXO7Dm_pHCE7TKNZWii0kecwW33WKIYNqx6bTImzBij79V6NBHW4yFAjhtGi1tHH3ew1rieP8JH2nsLRiYeJo3FO9ECe0uwawEDLNqTtdqPyGNORx3OnHPKNdHdyHInVG_9ziJT4J08bYO1U0tvgHhlXnbzw2qrJ1E-P8h5E5O3sag9Vr5gXmbyGLXR872DoWGvveq3Si_7rRpFX9ICRrY8c1PwtZycM12mou_Jw2_lOoCuxeLwSUr2zfIThKORVq1cBQBFD2yMzRw8E4yaVhfmcQM-vmO_bBTAYUpGIKm0rrOd8I-y95lK4h2Dbz10Q_vnIcP51gTi5i9TE4x9Z_Hjn5hdorSXf04IjYlo4HxwuBXRAEZeFbhu3hfBK9fpCe0GMA58J-2MdknjI7WEZ-dirSSVzf9TTaAECODnCfBygYjusxjliv6Z7C29TCI9ovc4K-BSnU4UBncX8jUXLRi1usV6J7tQReqo3zLEx3tBbirDvaQO3J5qHH1cmZ2fRQSQd2nzb9QrFnxdO8zH36aKGu0hagYg5okZr1RIirARa98r25JJbY0qL8Qv4S_gPH6XamgTydPXlhEZ7J6FWl8eUvcIAFlQUBsRSR8BELuM0pHJ8k-4Phm2Dhi2O_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87cafbf9ca.mp4?token=Cqa5hHDOIhoMoh5XtEO6IjsXB328L4U3DumcS4wCyTlpNaXO7Dm_pHCE7TKNZWii0kecwW33WKIYNqx6bTImzBij79V6NBHW4yFAjhtGi1tHH3ew1rieP8JH2nsLRiYeJo3FO9ECe0uwawEDLNqTtdqPyGNORx3OnHPKNdHdyHInVG_9ziJT4J08bYO1U0tvgHhlXnbzw2qrJ1E-P8h5E5O3sag9Vr5gXmbyGLXR872DoWGvveq3Si_7rRpFX9ICRrY8c1PwtZycM12mou_Jw2_lOoCuxeLwSUr2zfIThKORVq1cBQBFD2yMzRw8E4yaVhfmcQM-vmO_bBTAYUpGIKm0rrOd8I-y95lK4h2Dbz10Q_vnIcP51gTi5i9TE4x9Z_Hjn5hdorSXf04IjYlo4HxwuBXRAEZeFbhu3hfBK9fpCe0GMA58J-2MdknjI7WEZ-dirSSVzf9TTaAECODnCfBygYjusxjliv6Z7C29TCI9ovc4K-BSnU4UBncX8jUXLRi1usV6J7tQReqo3zLEx3tBbirDvaQO3J5qHH1cmZ2fRQSQd2nzb9QrFnxdO8zH36aKGu0hagYg5okZr1RIirARa98r25JJbY0qL8Qv4S_gPH6XamgTydPXlhEZ7J6FWl8eUvcIAFlQUBsRSR8BELuM0pHJ8k-4Phm2Dhi2O_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور اربعینی‌ها در سمنان
@Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/454374" target="_blank">📅 10:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454373">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0AW00r5jce07Uc5CY4lwh9PuPnbjUWoottb-ZTZZ3azjvV7maR10mXHnucMP1MguhewrLWv-aMhoQbc8Y74IVwgoRec-vxvKEqZ4NI7hIeqtWtQ9YQsww2pwQkwYgFD-IAZwxnVxXLYSJ4HZbRGFf9B0hEnB7tp4jg45sfdJmFkS6fWNDaDk94nDT51wsTgzqy9p3rYUm0F_4_yz37HMaqvH6ypx-o0bzMoqZ45ZiJuhgCuE10nXedyCbih_ytj-Mk77yi21rFI81zp8yXx0QjAZICv4Dxq1X59efHxowuWVk9eoaE336ouqd7R1ZFI_RwYAXvOYVjZgrLVwwYX_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله: سلاح و مسیر جهاد حسینی را ترک نخواهیم کرد
🔹
شیخ نعیم قاسم: امام حسین (ع) خطی است به سوی ظهور امام مهدی (عج) و امروز به وضوح اعلام می‌کنیم که ما با امام حسین (ع) هستیم و او را رها نخواهیم کرد و به حمل سلاح و جهاد ادامه خواهیم داد، و شما را ترک نخواهیم کرد، ای حسین.
@Farsna</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/454373" target="_blank">📅 10:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454372">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92da06cf35.mp4?token=lRqbCE40B7kh8tcIAoaCjEQodEB4gjDhFV_5yxwvDE0KDSHy6daLkAnDlWS3n6TEWUFxQ0bEGE_qAlkecTA-56Cw_28g2B0frI-CKllUZKSGqEs89_qw8_92XCOT7tlCPB1nJUPVmNWGf227BdqPc8jw6YJXy9MNednDHJxh4aEHoaeVt5AbquiM902sJPxT9kML1KX7FRF_XqimxVSLNUiBowZzDYyE_x3XkiAAFphrfq6HhCLX407RGm5dSukxWw4Vd33qSAq4RW54NG-VvW11vr5xJG8Op45VxBocBTJ2F7uqVjQtEs14VFLLP1GZ8QEs0S-U0X9pKzTz5OuaGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92da06cf35.mp4?token=lRqbCE40B7kh8tcIAoaCjEQodEB4gjDhFV_5yxwvDE0KDSHy6daLkAnDlWS3n6TEWUFxQ0bEGE_qAlkecTA-56Cw_28g2B0frI-CKllUZKSGqEs89_qw8_92XCOT7tlCPB1nJUPVmNWGf227BdqPc8jw6YJXy9MNednDHJxh4aEHoaeVt5AbquiM902sJPxT9kML1KX7FRF_XqimxVSLNUiBowZzDYyE_x3XkiAAFphrfq6HhCLX407RGm5dSukxWw4Vd33qSAq4RW54NG-VvW11vr5xJG8Op45VxBocBTJ2F7uqVjQtEs14VFLLP1GZ8QEs0S-U0X9pKzTz5OuaGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت تصویری موکب عراقی از امتداد عاشورا در دل تاریخ
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farsna/454372" target="_blank">📅 10:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454371">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/410cf61146.mp4?token=K9EpHj5Azr97vJ9u9pJ8f9dedj0sPa6BKfnSl65fgzoDWGTKKs93QCQzDxV5dPmFUDGzEvj2pUabySCFWc-kJR8sUbJpat9oOYHoOEikd8QiTtonP_OTL8gXvf-HNSgADcE5fbI0114RcK3xaq1SxcK4IPjfr6uKXh1QMBxOm85ok3-ga8KOlbV_mRHaRc-UPKnz32opaT2Eyv3tnCuXlL6L7CE9ZRjcdQX4BYXXSLkv4yMCBXrLwnMgjGRnPyHGgWEwRfWqu_-p3JQw4UvaNHTEWAxU0LavYdPfOFRA8-7LsAhl1OhwNp3jEFMZDuFVN02eTxz3sogQFpe8KRovSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/410cf61146.mp4?token=K9EpHj5Azr97vJ9u9pJ8f9dedj0sPa6BKfnSl65fgzoDWGTKKs93QCQzDxV5dPmFUDGzEvj2pUabySCFWc-kJR8sUbJpat9oOYHoOEikd8QiTtonP_OTL8gXvf-HNSgADcE5fbI0114RcK3xaq1SxcK4IPjfr6uKXh1QMBxOm85ok3-ga8KOlbV_mRHaRc-UPKnz32opaT2Eyv3tnCuXlL6L7CE9ZRjcdQX4BYXXSLkv4yMCBXrLwnMgjGRnPyHGgWEwRfWqu_-p3JQw4UvaNHTEWAxU0LavYdPfOFRA8-7LsAhl1OhwNp3jEFMZDuFVN02eTxz3sogQFpe8KRovSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این چشمۀ عاشقی از کربلا جاری است
🔸
پیاده‌روی جاماندگان اربعین در بخش بیکاه شهرستان رودان در استان هرمزگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/454371" target="_blank">📅 10:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454370">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/054c5bbfdb.mp4?token=Xe3FP12Kt6RsvZyOkPbiMaw_wJJip1FONGNQXbnohNVpydPt9vTHCzaMCb2ocXhXclvyOExX4wClpu00VlvFIn43Rl8H3o8HilG7VE5GvV_E7Wxhcw7lkRw3LY8E5qenAqyayGFi5Xd5sf0Uo6v1vSQNgsRkGL0XuNj97hbjCwH27jYYjLTYhaMZ1c0DhuRzKWeB_50Fc_qpMhLWIkSHzmmQON5zjwsLBa8EvtcRpjK-ql9OH2Ss-DAKI5oyT_n5MKlzx2A958Zt1sGYUIYJhGQKbkZ54RPGu0AN2RLG0NFfeDQHKicYzWPb_NQa-YXo9mJ2uVLsPg-YGRmIjRowOrl2J5dLOjysU0b3vRpCha9zkD9ME8GYetXRzNardSCVyx30aGt89Kd_a45Q8tRBnmL4qjDGgHi8XPURlia-Z6_0O07GjalE8mqxq7ZUrtIKOnf7XaE4Kb3ZPZxaAyAqDSmrp1HIkgazynMGLAfyemAploud0ev9tUw6Lr4qR3QPT-aVjN6tHNnRGV3A9nz1Ye-VGntniEItsz_naDXqaQmyNw9g9JNoiYoMbHKPi_AeGqofhyrvk3tdjX-XnD5a6qQJvCqx5p-ntkQXqBR4uYNbJmEPwQqmKvcpqz2IlsgmPkMAiGZ4bjspsuma7EpZ9gfadj_C_CVUe6hThTbQmxk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/054c5bbfdb.mp4?token=Xe3FP12Kt6RsvZyOkPbiMaw_wJJip1FONGNQXbnohNVpydPt9vTHCzaMCb2ocXhXclvyOExX4wClpu00VlvFIn43Rl8H3o8HilG7VE5GvV_E7Wxhcw7lkRw3LY8E5qenAqyayGFi5Xd5sf0Uo6v1vSQNgsRkGL0XuNj97hbjCwH27jYYjLTYhaMZ1c0DhuRzKWeB_50Fc_qpMhLWIkSHzmmQON5zjwsLBa8EvtcRpjK-ql9OH2Ss-DAKI5oyT_n5MKlzx2A958Zt1sGYUIYJhGQKbkZ54RPGu0AN2RLG0NFfeDQHKicYzWPb_NQa-YXo9mJ2uVLsPg-YGRmIjRowOrl2J5dLOjysU0b3vRpCha9zkD9ME8GYetXRzNardSCVyx30aGt89Kd_a45Q8tRBnmL4qjDGgHi8XPURlia-Z6_0O07GjalE8mqxq7ZUrtIKOnf7XaE4Kb3ZPZxaAyAqDSmrp1HIkgazynMGLAfyemAploud0ev9tUw6Lr4qR3QPT-aVjN6tHNnRGV3A9nz1Ye-VGntniEItsz_naDXqaQmyNw9g9JNoiYoMbHKPi_AeGqofhyrvk3tdjX-XnD5a6qQJvCqx5p-ntkQXqBR4uYNbJmEPwQqmKvcpqz2IlsgmPkMAiGZ4bjspsuma7EpZ9gfadj_C_CVUe6hThTbQmxk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم سرخ خونخواهی بر دوش جاماندگان اربعین شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/farsna/454370" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454369">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997924bb9c.mp4?token=FeKFCxcumLyVQWXprVTVCkcpMxSDwz9qSgb3p_TvQLTQNMo-Y_P7F5VKRNy9qBv21PbALdmXIr0lE0TDHpKydhY1k06qmkbu23UCKaXPRMVSZWqw5GG1grTrbtZLnu2_AbO9u73ZjRhWTXlwIVibWUWhZaS9c0LUf33IqMf3SWQJaCSyo-dW-Lhzm9ywOEkcNWsX3tLEuvitd8SKsmVy0FT9XNdWhmJ5BMX3N8vOswV6eop0bQB_nFLk0nutwqMzrRODGTjFdGjQRgP8In5AG7AyU61ZY1jSEYZVbJTEJxgi5wZYmTlMJZpTJMVt3C5LdvEsFoqwWWf7LzqzludIkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997924bb9c.mp4?token=FeKFCxcumLyVQWXprVTVCkcpMxSDwz9qSgb3p_TvQLTQNMo-Y_P7F5VKRNy9qBv21PbALdmXIr0lE0TDHpKydhY1k06qmkbu23UCKaXPRMVSZWqw5GG1grTrbtZLnu2_AbO9u73ZjRhWTXlwIVibWUWhZaS9c0LUf33IqMf3SWQJaCSyo-dW-Lhzm9ywOEkcNWsX3tLEuvitd8SKsmVy0FT9XNdWhmJ5BMX3N8vOswV6eop0bQB_nFLk0nutwqMzrRODGTjFdGjQRgP8In5AG7AyU61ZY1jSEYZVbJTEJxgi5wZYmTlMJZpTJMVt3C5LdvEsFoqwWWf7LzqzludIkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور پرشور مردم تهران در پیاده‌روی جاماندگان اربعین  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/454369" target="_blank">📅 10:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454368">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TR4E30Lyv1cu148hDlDT68SPzoahv9mju1HE6zp2RODMayedjJ8SmsEO1aKsCb8Xh1dAHf5LNSB0mSTNkp6jUg2x1JQ1pmsQPg6yaxEgOsR71xamwTXtnGCLbGJ7-2gC-y-TZ4d9-szYQMSOAam64a3qIbpNuM32mitqGqki-AtP3tAAi_tIm4zj3wiCbhI7U-zQ5BjpyuwhRWVxYdjOy7Nef1fZNzuJ80IkJys3_50cpI0eau6b0iZWTf78IBy9UA1kkrgGVR5XVqHdGujVIleIVkfvlEFZeHltuHPaHfUDk8wYkAUjoKcci4PCK60QcwqwR2QYZ4tKnrq0dlW1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وحشت ۱۰۰ میلیونی مدیرعامل آرامکو از بسته ماندن هرمز
🔹
مدیرعامل شرکت ملی نفت عربستان (آرامکو): در صورت ادامه انسداد تنگۀ هرمز بازار جهانی هر هفته ۱۰۰ میلیون بشکه نفت را از دست خواهد داد.
🔹
با تداوم این روند، پرکردن مجدد ذخایر جهانی حداقل ۱۸ ماه به طول خواهد انجامید.
🔸
بر اساس گزارش رویترز در دو ماه گذشته به دلیل محاصرۀ این گذرگاه استراتژیک حدود یک میلیارد بشکه نفت از چرخه عرضه جهانی خارج شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/454368" target="_blank">📅 10:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454367">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d618a647.mp4?token=g0sNb34GgRHZumo2ZHuQKVvw318UUIHVjG-YWJ5kH_GeN_FA-CHm3_T40dBUwbXhPTWmMQdEu9HYM4Whpxw5HsUfNfW-5Z1Ms0svZXZURqUJiK9oLaFakJTPeFGkWC0_lwrxOKnjlp2JrdzAaazQshu5qGbwDMSzD00xD9Korr5OP-Wmt2b4fXXLXadOYiyr-Uxi3tTrIcjRaDp6qakT_S4Vfc-1UBKdGDl6b5P6gFqMUOq4oyI__j1U-FZGHy3hDCYcCooDhkTY144Tq9OB9CKtX1sq2WNG86KGZH6tl0LlhanMpFUO94RAOmo0ztzDI-TkC9-rItU1gIWthjzQYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d618a647.mp4?token=g0sNb34GgRHZumo2ZHuQKVvw318UUIHVjG-YWJ5kH_GeN_FA-CHm3_T40dBUwbXhPTWmMQdEu9HYM4Whpxw5HsUfNfW-5Z1Ms0svZXZURqUJiK9oLaFakJTPeFGkWC0_lwrxOKnjlp2JrdzAaazQshu5qGbwDMSzD00xD9Korr5OP-Wmt2b4fXXLXadOYiyr-Uxi3tTrIcjRaDp6qakT_S4Vfc-1UBKdGDl6b5P6gFqMUOq4oyI__j1U-FZGHy3hDCYcCooDhkTY144Tq9OB9CKtX1sq2WNG86KGZH6tl0LlhanMpFUO94RAOmo0ztzDI-TkC9-rItU1gIWthjzQYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور حسینی جاماندگان اربعین در بجنورد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/454367" target="_blank">📅 10:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454360">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZNS_ZOWi2xuOXhatEVhoBW-TfaKolLDk_L-j3qW73m8qsKUDQSev_79Y_K7sf1eJAzqdo4SShOTUjSHZsjbNvAuOLYXpUxvQvWgLYEoxSXTI2zUKSm0xp4GHMOAAw1iCQCj_plIWmQ1eDCM3_PPkA3qro63JKJITgdSQe_VWRWISVJvsv8UZq_wEVky1IYq478wxI7T7h-IT3t73rq1iTF1Y7mdBaYfXApZavbJmkIju6Jdjwq1wfu-UNNnakOhOGNk2FOWkKYN3tuSXEK08S3qvePcGZLYWiaDeyelpqRBC-gCgUGjWle2zunObp9sayD5WpkKxdn1lekHPYlf-Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fes3vv4MK3yXVlu9rV3MlZ0ItThadJf9jeb9Jw5ijT9wnzxZlRXIiLcxB2sh6AHIz-xgXOc544EcrLgRwG9Ya7mdzbAZGJELG74UIiUumWcClxhkFp04mvhHsahla89Gc2lD7f_-7LxYBYWhEmxJyJy8jk7PABrWpOpk_4Xr7zd0uTmKhhszW_-8KBwN_knBaS_8BSH0S6fx_abHp-LWp1M3Z3pdhIJBxWyhgxqSGtNPSC79cO9m4PYxNTVm8ggyN7OCPkm2R74DvQVvH6U3R4IjlqdEkl46QplJJjm-yhAcW9uZOZtTF1jwMf08I8nFfmm1m6_vZPh7l4cYUVZcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzAEdSmORVBR_3U_lnCpESgwAvj9bivk30ShLN88bdD77I03NWHInJ0YTPydg3MnoJgZZpG8o0AmcSycigFSCGhpOike10EphiHzL2iqDXI2UTANv6_vTVSUQ3_l2Ml2hmetTrUpxaaLAoGI4DkWxFZiTHIiyzUgqi6eeGCdvtVC2ueiuEIzh-3TeSrqkGUgfXZPqBJi-P2hE-3pmUcNczrJX7H1IxtwE-MjJD5x4DS6Rj6BOHI05OnIuMteFZN99GH6HrV9K-WtR0XFAtdylyooT4d6w1A9AT1ciharl7_rEIt9XZ26Q7uUOa5BvtHCQRJIIM8ea8Hb90XQehgrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HU8xFN72Y9QdATAut0EC6ObvA-mIC5A9b3PYqH-IzBTrYtTwZFy-SQGB0bG9V7AZ-rBWdyg-maS9r2nCA0M4aHc1QKjBF2FkfjljO7TVigvhlp4BXbaekV5zjzYMcM45zE3w1nd54h6loUQ8ZWtvizdH-5arXn98tzLPy1d1pa4udNQUZG9U-T8hi9BsM0mNwWOwbFUVeWaLSOm8MXu7_nE6LeSiJ1i5tRbnB4nIcKuXsZwW0-nLWpfi4ZSMG8FuWRKatKXUP-Z8QCfGEe2mbhdUfxDLOtGx0wfcRwynSvOPN6G3TQfct9j0hwOiJ8dmXMYd3fMViFG6mTsrw-nQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VaVmiSMGzKciUSN_I3-sKBk5e4476l4N7XtIVQAGpz6IzhK9p1C_A-R8uJq_9YNTGNt_daAZ_5QBnBjtBc5pPoiUuChNlcComwACjhUCUXSMvSUL1kAxiRci211vYRe63GkvTEVxiew3vvdHQVCubjJrS2f2l3J_-pt37BZ5eFJGsORfhb2e2LhDrDCJkTjZykwgJ5aR8yoTPF8vkYujrd_R-ZL-ksu_ljQu8mHQRmGFiQm9x3V_ZjflTZl8z5ZmzuhRbYLG59rjkLQS353lvEogy2WbaY7dJmxt0PK3jQ-32CNe-8vxIr-OWOx9X-EolCUHUuobOk34TAibwh5KMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6DTKvIfapYNfzFodGw7t16PrzRLExDaPnNz4ShB4jYZ0ouSOSjHk2Mg6tbnjxDKJoZ5IZMEI56YWyinsPNS6zLzZ6SrBLvp_DHPOp76tJLHsUXCoBG3dctCmHKLobUTwj2dPMSuUkcRLXCX6cPiDoOhfwMctp7SIAFsfulbf-1JaLitmZPMP0zabhWCRNw8A5BI8M_uA1uKj---aSre0uyEVNrcvuEtLx44f26wL1f8bGdUvDINEjAnh2lB_8K7t9geuRz3OHLvmnJPiUyG3UY7uvwXVaAi2U_6GnB05sxQxjZl34hYyFxooJ0H8iNtT216X1PMWnhAruVeHioiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7-kLuZhqj4lXDi-If9HCaofO8yH75i4lAe-DCsstGw-jMHPSv91OMCc2qLg711Rph8Sw9GlImXpdk5XQAb_avjEB0pTTWYkphZm3Tv1dCin0Y9kQAooeUVSnf1NgQbyxVnjOVHZUvHPWR8cVFrsAk-A28ikI5L_IfYMRTSsPy_jiE1LmdsqgHJfTK_sJQUb5IQuTyEbMgz4kSqwgdDK8xC8Pp6y1kZQMhtL0NdLBt2u5D2Ef-TK9CWee2s20XIhsvs0A_61vvaMAPnq095m-xN1Qe_PsvM7q2m1nQJ6wljHOcbOgn10CrIiMlJXDRYQYQVOMbXFGNbTKRuelWojjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زیارت اربعین در بین‌الحرمین
عکاس :
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/454360" target="_blank">📅 10:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454359">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16082d6cec.mp4?token=XlS-6VBkrVgeR52FmZJRHdqdYW8ceHnAA9bdeWLRghs4q2KMoHdX4udN-ntp2rtrKUTTR5SbwQFoWN9QSrnLhg74jikvYUsj2smeIDxvfZhhqVySKZ0NvMoJLH4hiefn1KNMaj--Jl18J-38XMwEsvyqWYkty4j6nFSDt6hWOinNMofQ-YDJWhWmLPu-xcGTaNl4Z09XhB_KxH1PePWRbBRTgERsi6OlcQKZmtOc9kx8RKqgGbK946N6NcHlFARxGsl___AE18-9vMOGCPFkS0Y5nhqR7gyKpNz1oUS7al-ShetWVJPb7HSavqcQD955LR1Ib3_EQX9TZ_zK5zu4Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16082d6cec.mp4?token=XlS-6VBkrVgeR52FmZJRHdqdYW8ceHnAA9bdeWLRghs4q2KMoHdX4udN-ntp2rtrKUTTR5SbwQFoWN9QSrnLhg74jikvYUsj2smeIDxvfZhhqVySKZ0NvMoJLH4hiefn1KNMaj--Jl18J-38XMwEsvyqWYkty4j6nFSDt6hWOinNMofQ-YDJWhWmLPu-xcGTaNl4Z09XhB_KxH1PePWRbBRTgERsi6OlcQKZmtOc9kx8RKqgGbK946N6NcHlFARxGsl___AE18-9vMOGCPFkS0Y5nhqR7gyKpNz1oUS7al-ShetWVJPb7HSavqcQD955LR1Ib3_EQX9TZ_zK5zu4Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیاده‌روی سیل خروشان جاماندگان اربعین حسینی در اصفهان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/454359" target="_blank">📅 10:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454358">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🎥
قرائت زیارت اربعین در حضور رهبر شهید انقلاب در حسینیه امام خمینی(ره)
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/454358" target="_blank">📅 09:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454357">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be4818c90.mp4?token=pwgMfFIgFUIUfWYAYvmldO-6xRCJ8mQRLSjXDUNEgwWfTJ0kNC2oNehgSZqhZkf21n-H0BtsVVhEm2iqAgNEuR6zw6d8XEBEu5ED5uVvBME2QubFIELjkTif4ZsThhTFx_CQ-L0OBnBROneXWFFITXn9CqS7wFSnYyiLrifPDbZAsYM7WujfrVw6P0O0lpzw5Tq-JJ6GJT4SV2182MzvsNJi7_2wAX9mTtMOi5i4AD7vCUSc1jcHkQva8HDCJYCaRsD3fERlN3ffvkOLlzXcsC-Y3pn2xgEM1Tbw1wRUn5R9Is7ELPUfI6STOQldFgeDMIjaN6-Dt8gDdHPvKD5dagDQCmejj7FUlhuuYICyHuCCnKjA1MQhaoaZn1OrnrXOsbt_6L2Y7xTQRPXx_5nxbwIqqzq9tu-IS-dOjK-_wUS_0oDX8bZW1klKYd8wQ2E70CKyATrHpGAUlz7EIKwPu9Cyozb40Kh-mM7RUfLJXnza81E02Rrs6pPpacnCzn8KWeJcvm3HwjLPu9kOGJaWbxsnriI7_Ve5LyN-uUYqter1IrNZrM1-FxB7iudRAW8aTXJQPno_B7Efmg6C_9SpW572BHmxn4YZyreNK_THRK1DRXzQGp2C7fAIyuDMkZ79ZhR5uk7oic1fbhvIvL5ky0rjpr9bN_xTtRFbLJp6gw0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be4818c90.mp4?token=pwgMfFIgFUIUfWYAYvmldO-6xRCJ8mQRLSjXDUNEgwWfTJ0kNC2oNehgSZqhZkf21n-H0BtsVVhEm2iqAgNEuR6zw6d8XEBEu5ED5uVvBME2QubFIELjkTif4ZsThhTFx_CQ-L0OBnBROneXWFFITXn9CqS7wFSnYyiLrifPDbZAsYM7WujfrVw6P0O0lpzw5Tq-JJ6GJT4SV2182MzvsNJi7_2wAX9mTtMOi5i4AD7vCUSc1jcHkQva8HDCJYCaRsD3fERlN3ffvkOLlzXcsC-Y3pn2xgEM1Tbw1wRUn5R9Is7ELPUfI6STOQldFgeDMIjaN6-Dt8gDdHPvKD5dagDQCmejj7FUlhuuYICyHuCCnKjA1MQhaoaZn1OrnrXOsbt_6L2Y7xTQRPXx_5nxbwIqqzq9tu-IS-dOjK-_wUS_0oDX8bZW1klKYd8wQ2E70CKyATrHpGAUlz7EIKwPu9Cyozb40Kh-mM7RUfLJXnza81E02Rrs6pPpacnCzn8KWeJcvm3HwjLPu9kOGJaWbxsnriI7_Ve5LyN-uUYqter1IrNZrM1-FxB7iudRAW8aTXJQPno_B7Efmg6C_9SpW572BHmxn4YZyreNK_THRK1DRXzQGp2C7fAIyuDMkZ79ZhR5uk7oic1fbhvIvL5ky0rjpr9bN_xTtRFbLJp6gw0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهپیمایی جاماندگان اربعین حسینی شهر نور مازندران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/farsna/454357" target="_blank">📅 09:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454356">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cec78c0c6.mp4?token=IEJy5ssxfg0KJi4t33YuQLocKyQtc9isd4upXrQndwPkewWRgawMdjBmWTfYGmoBAu4cOZ3w00OKtk_HaTWeHwtWtN3M_BjGnAiGqpG-iw7OQh_TVjd1UyrLHYOa5_ynANm28GxiDZz5P9v1aORrB7_SdFtH89k9etc_rdRieeqUIjqFDvma5n0AIalHzkYVY-gMtyjGvK7TpFxKGuA6JhxiuwawGPjwzQGSdJSk5K9reZO2PU4UOv7PYxV-dAaQuMa4zEw7GVgozRD5Pi6C3FoVzD-kF8aUGwS1kSUCC6JrXSoVXOgymb2EXgj6vAu2VGFMvDcIoG-gSpA5f29MOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cec78c0c6.mp4?token=IEJy5ssxfg0KJi4t33YuQLocKyQtc9isd4upXrQndwPkewWRgawMdjBmWTfYGmoBAu4cOZ3w00OKtk_HaTWeHwtWtN3M_BjGnAiGqpG-iw7OQh_TVjd1UyrLHYOa5_ynANm28GxiDZz5P9v1aORrB7_SdFtH89k9etc_rdRieeqUIjqFDvma5n0AIalHzkYVY-gMtyjGvK7TpFxKGuA6JhxiuwawGPjwzQGSdJSk5K9reZO2PU4UOv7PYxV-dAaQuMa4zEw7GVgozRD5Pi6C3FoVzD-kF8aUGwS1kSUCC6JrXSoVXOgymb2EXgj6vAu2VGFMvDcIoG-gSpA5f29MOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امسال پرچم‌های سرخ حرف دل جاماندگان اربعین را می‌زنند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/454356" target="_blank">📅 09:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454355">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09cd20623d.mp4?token=tq--5gajcTpxCBW_ohgKrQYXJ-XgMESP_wGmlm7l3ZJKJgpgtjg-vYCnNWb5TAvVhGSO5PVvmUPiFV5mt-DeXlP4o9lo0GKpSheqM-nTSohrrZ1ErMVZ9ImabY1xcDV2xYk1a41Rm8ZFfk8UjoOngMtodR2UFmjwxwyrh3uMVvrk8slzG-bIl8YkAjl23TSqQ3QLg9vNxhQs7pHoR45oRCoIdNgwhbPS7IO484lUVBEaoMS71H1q5ldYahhOY_6UPcBI1anmrMLWxIhNtLNgQS6FL4j_QEfixB6rt5X83VWEeSw79mtmV5jR0qazv6l3yQWMjwF5Umvj3iral1peoa0YyZTRbJULpie_TKeWesKf5AknT0RhzFfmBne2jXCovebyNgXywlz5pAVXfCbAE15-pjg3AbIctKjTh8l_xWw9v17-tExS9_DIrh1oi6rXNdJF_r1GTJJiCWWURb6Pcvzpp9JF5F0CKlhxuGgucsg0U914Q3wWqswXVtrU8mf9DPRH9NDSlzQpnqh0AytgId7UHwVPoUMmtER4VfNOucpAl3WbkMiygUoA5w-gQwOxnudmpFXWE5GAV0UK7jSJgboyoEALTBgG4Ox-wnnjWB1BEoW8RHh1kCu0ReVcFZ2KpY60vOi-1NKnCbxuM9qn3R0oFwYsmTROa8aGcV4dUKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09cd20623d.mp4?token=tq--5gajcTpxCBW_ohgKrQYXJ-XgMESP_wGmlm7l3ZJKJgpgtjg-vYCnNWb5TAvVhGSO5PVvmUPiFV5mt-DeXlP4o9lo0GKpSheqM-nTSohrrZ1ErMVZ9ImabY1xcDV2xYk1a41Rm8ZFfk8UjoOngMtodR2UFmjwxwyrh3uMVvrk8slzG-bIl8YkAjl23TSqQ3QLg9vNxhQs7pHoR45oRCoIdNgwhbPS7IO484lUVBEaoMS71H1q5ldYahhOY_6UPcBI1anmrMLWxIhNtLNgQS6FL4j_QEfixB6rt5X83VWEeSw79mtmV5jR0qazv6l3yQWMjwF5Umvj3iral1peoa0YyZTRbJULpie_TKeWesKf5AknT0RhzFfmBne2jXCovebyNgXywlz5pAVXfCbAE15-pjg3AbIctKjTh8l_xWw9v17-tExS9_DIrh1oi6rXNdJF_r1GTJJiCWWURb6Pcvzpp9JF5F0CKlhxuGgucsg0U914Q3wWqswXVtrU8mf9DPRH9NDSlzQpnqh0AytgId7UHwVPoUMmtER4VfNOucpAl3WbkMiygUoA5w-gQwOxnudmpFXWE5GAV0UK7jSJgboyoEALTBgG4Ox-wnnjWB1BEoW8RHh1kCu0ReVcFZ2KpY60vOi-1NKnCbxuM9qn3R0oFwYsmTROa8aGcV4dUKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیاده‌روی دلدادگان اربعین در مراغه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/454355" target="_blank">📅 09:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454354">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ادعای نیویورک‌تایمز دربارۀ جزئیات مذاکرۀ ایران و عمان در تنگۀ هرمز
🔹
نیویورک‌تایمز ادعاهای جدیدی دربارۀ مذاکرات در حال انجام میان ایران و عمان پیرامون تنگه هرمز را مطرح کرده است.
🔹
طبق این گزارش کشتی‌هایی که به سمت خلیج‌فارس می‌روند از مسیری تحت کنترل ایران و نزدیک ساحل آن و کشتی‌هایی که از خلیج‌فارس خارج می‌شوند، از کانالی در نزدیکی عمان عبور خواهند کرد.
🔹
این رسانۀ آمریکایی مدعی‌ست این توافقی شامل «هزینه خدمات» برای پوشش اثرات زیست‌محیطی کشتیرانی و همچنین امنیت کشتی‌های باری و نفتکش‌ها خواهد بود.
🔹
بر اساس نوشته نیویورک‌تایمز اگر این شروط لازم‌الاجرا شود ممکن است هزینه آن گزاف باشد؛ زیرا به منزله تأیید کنترل تهران بر آنچه که قبل از جنگ یک آبراه بین‌المللی آزاد بود، است.
🔸
پیش‌تر عراقچی به هیئت دولت گزارش داده بود که مذاکرات با عمان برسر تنگۀ هرمز به مراحل پایانی خود نزدیک می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/454354" target="_blank">📅 09:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454353">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337121d388.mp4?token=RgFZEa9oCZ6rOB8cfquOBrAz0vVy6LkyniyF9_e2EL23x5kYMolHbOPjdLQI2m-LW77Mol4Fg7nec48dxflYUed6GLLEqvC79ikaG8gtTETGlSpdXIt87aRDsuYFOVPhoJUH_P1pELBPHtoPol8Exsds8bAf-oUnnuOBFpUE6TXPHjYNCR_JkitVHGVoRmJXOQIHReZcue66E9ilQIDJyVekV6rqcl80GlaVnYHdo5vaRttJ-a-ag2cN0QQK8NkK5f26QIoIWZzGfaGDaz28H8gx3I_2mKBw5J8C6w3Lh5UXk8IU8-NP5UyXPdXj5TMQXLFUI-Z937JswcUQ6DwvfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337121d388.mp4?token=RgFZEa9oCZ6rOB8cfquOBrAz0vVy6LkyniyF9_e2EL23x5kYMolHbOPjdLQI2m-LW77Mol4Fg7nec48dxflYUed6GLLEqvC79ikaG8gtTETGlSpdXIt87aRDsuYFOVPhoJUH_P1pELBPHtoPol8Exsds8bAf-oUnnuOBFpUE6TXPHjYNCR_JkitVHGVoRmJXOQIHReZcue66E9ilQIDJyVekV6rqcl80GlaVnYHdo5vaRttJ-a-ag2cN0QQK8NkK5f26QIoIWZzGfaGDaz28H8gx3I_2mKBw5J8C6w3Lh5UXk8IU8-NP5UyXPdXj5TMQXLFUI-Z937JswcUQ6DwvfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پیاده‌روی مردم پیشوا، ورامین و قرچک به‌سوی حرم حضرت عبدالعظیم حسنی(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/454353" target="_blank">📅 09:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454352">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80315544f8.mp4?token=fpE-KmPEd-dnBmFLepAELxStpYLI0lDfMRKEiyr5lMEaBlAiYqbRv4FuV6xMSXn9dbm9DqRkgLZwrEEsHxqSUlUO5HU_cW4kq2fGauoJmHUF6ftB1lHoeda3IiSbk2A4o2evPy4upbSY55U_JXHF7vlX_m3uZnZYJ3DFuP-73cfN0MkMlfRnIm6cANrj94l-kwK_9tIzsBJr9IuwRDsJ7EMz7ZaDZNXWnhepbbfRDqMByLWSnqnEjYlNlPImqWM8pwaUaPUT6EWCrRexJztxsgxBmXAGI5NG5O9agsqJ29bD3Unph13nqkWvjUxFzbFoDo_xzgvKtE0iMAG1ktBUjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80315544f8.mp4?token=fpE-KmPEd-dnBmFLepAELxStpYLI0lDfMRKEiyr5lMEaBlAiYqbRv4FuV6xMSXn9dbm9DqRkgLZwrEEsHxqSUlUO5HU_cW4kq2fGauoJmHUF6ftB1lHoeda3IiSbk2A4o2evPy4upbSY55U_JXHF7vlX_m3uZnZYJ3DFuP-73cfN0MkMlfRnIm6cANrj94l-kwK_9tIzsBJr9IuwRDsJ7EMz7ZaDZNXWnhepbbfRDqMByLWSnqnEjYlNlPImqWM8pwaUaPUT6EWCrRexJztxsgxBmXAGI5NG5O9agsqJ29bD3Unph13nqkWvjUxFzbFoDo_xzgvKtE0iMAG1ktBUjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاشقان کربلا در تهران پیاده راهی حرم عبدالعظیم حسنی(ع) شدند  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/454352" target="_blank">📅 09:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454351">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/294102c63c.mp4?token=IlzXl1fyq879rgS1M-NDq7tzYqh_BADRiLv3XbcksUO1Yq2Inq4-5J2Ano9Zm5KokzM5xK3xcbyhIhig2RbTXmgNHh4QwG8Mx-eCmsmDMkAKRcGHvKOiMBAjCHibo2GyyrfneHn7liVCu0ZUFnN1gaYKXIagyK2vu7q003D2xQqGgLYV-5jV5nUp_F8slP0MRMAxUIH6cdxcbZbVDOnStt0NhKnBzFB8D3er_rquFFLCqUz13PRahHsEReW2FdWKjIFgK89Pxe0CkenIOVFP96EkUEgWcuICOvQg7ly1opIBUAC7L0jwyOU5Z_Dy9SJQMAD4gL-FEuLT5U7wAp_SZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/294102c63c.mp4?token=IlzXl1fyq879rgS1M-NDq7tzYqh_BADRiLv3XbcksUO1Yq2Inq4-5J2Ano9Zm5KokzM5xK3xcbyhIhig2RbTXmgNHh4QwG8Mx-eCmsmDMkAKRcGHvKOiMBAjCHibo2GyyrfneHn7liVCu0ZUFnN1gaYKXIagyK2vu7q003D2xQqGgLYV-5jV5nUp_F8slP0MRMAxUIH6cdxcbZbVDOnStt0NhKnBzFB8D3er_rquFFLCqUz13PRahHsEReW2FdWKjIFgK89Pxe0CkenIOVFP96EkUEgWcuICOvQg7ly1opIBUAC7L0jwyOU5Z_Dy9SJQMAD4gL-FEuLT5U7wAp_SZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
راهپیمایی ۱۴ کیلومتری جاماندگان اربعین در شهر الوند استان قزوین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/454351" target="_blank">📅 08:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454350">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl14Z1cMiZE_jCtYEuEof4bj0bPcSCrAdFJkK35n8jaU7dFV_737qoYDmfZ0zFpgwTHDi-lezj_nPb_j7R2WisWq7wy-_gGvg1cv2KGm23SVXwasWlbL_0-yAQDY1MZ0ZTX5Emu2krVQXLSqFNCinHsUXJ9frKh_ulAMkIVO_-VwI7m_NJLZ91pgF6FcSJLllAR6BUmw29SBl8htDhj6Spm1fvD2pZc2XNLPXB5gGb1uNUXjO030ahVkPw52H_b8AxvBGy4x2SBxHeyLScrQmrO7aTermmumXCTtLDR9fIOTofIP--4osqMHnzcywFjUTyJgYYjVswExOpLqj61Ivg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کره شمالی: محور تقابل آمریکا در آسیا را مهار می‌کنیم
🔹
خبرگزاری مرکزی کره شمالی (KCNA) در بیانیه‌ای تند، اقدامات تقابلی آمریکا، ژاپن و کره جنوبی در شبه‌جزیره کره و فراسوی آن را به شدت محکوم کرد و هشدار داد که این اقدامات «از نقطه بحرانی عبور کرده» و صلح و امنیت منطقه را تهدید می‌کند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/454350" target="_blank">📅 08:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454349">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e88135373.mp4?token=CcsKNkeH24loIjvvmH1jPTlh-M7rbbqs9CSLu1xrlrPQF3-1ubzVWIF3DjCva51hvuyziQH3ER-KBNPkny7xk4hp2O8xReWLpMme4oLp6lM1E7M8Qr4LiOyeYhvAVzVnFAqwKiK8zZBBYenmmPHvwEQ8UC377Sc2LpzGO2LPuKtleb8vOyo_fo-CkjrrXZL05T3fHBkbK2XPvhMWubge3p4yZX-yAaT5hTIijhosPPLjg0vIJQwMBLCVA74DV9oZM6aIV1SSpY3mf5MSL8ZsLMsm4lhkjCwulT186Qi0rpsFruVTmaHLEn7GPOvSZ345gVW0dGSXo2YcAviNChcvWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e88135373.mp4?token=CcsKNkeH24loIjvvmH1jPTlh-M7rbbqs9CSLu1xrlrPQF3-1ubzVWIF3DjCva51hvuyziQH3ER-KBNPkny7xk4hp2O8xReWLpMme4oLp6lM1E7M8Qr4LiOyeYhvAVzVnFAqwKiK8zZBBYenmmPHvwEQ8UC377Sc2LpzGO2LPuKtleb8vOyo_fo-CkjrrXZL05T3fHBkbK2XPvhMWubge3p4yZX-yAaT5hTIijhosPPLjg0vIJQwMBLCVA74DV9oZM6aIV1SSpY3mf5MSL8ZsLMsm4lhkjCwulT186Qi0rpsFruVTmaHLEn7GPOvSZ345gVW0dGSXo2YcAviNChcvWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قدم‌هایی که در مسیر مشایه دشمن‌شکن شدند
@Farsna</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/454349" target="_blank">📅 08:48 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454348">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb50e3a465.mp4?token=n-aGKuV2bOW3RIcOpQHOjz-JzluiR5ylcSSPZV44j6SVVhzakRwOcu-ckaWZj8JVBPM1r3QtbesiVwQesuhTBUsO47X57MY4Xy3RY_xBtOvMRxB7gn3_9enSTDw8AlSdEsie-_hUCO3WPMEeXjbec73tQcNIVg2aOwKnX0Zchtz7j9CvrtMTRA-hBhO0NFe34JA4jUNiE2SeRtJ6wN_w7B-oAwrGZ7CMP1mQpJHaSKqEpRTBwDHW6z3hyZju0I8CGeuMeNOHQ4MGRSKeuXm-XXz7aNl3qzCOEEe2UTve-MZRnXcpB15yTFSq6LYAZboGPAsVd5lhLV5SkD7zdtLeYUKvwPvx8848tlSpJD5GycfoTEDNYbmjlg0ow2SaF20Db-k0Ss6PfaecXGqTvgc0wsXdpgQAdRv4Yp08maj99vs-pSdxi9p4ZR9Lpl-UN78MRY6rZQLZpKF4ORwh2CpFMZ_5bxXhFtphpDvGoaDDZyLyupdi8pzYcK_NFdzM7CVrQIN6F1y9W9qOwreSMwmU0cupbwm048nRvteHBHeUK5zCu9kQ1Exoscq9pjtpfiMLz1DsQL6co-km2rYm5TsTPlcdYgeXKjPSJ6E_1affkqrbUbmrvHLl97fFYTtIcQ7CnFeD36Gu3oH7sElaCrqdgPz3ByKhHvK8RT7X62uqgXs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb50e3a465.mp4?token=n-aGKuV2bOW3RIcOpQHOjz-JzluiR5ylcSSPZV44j6SVVhzakRwOcu-ckaWZj8JVBPM1r3QtbesiVwQesuhTBUsO47X57MY4Xy3RY_xBtOvMRxB7gn3_9enSTDw8AlSdEsie-_hUCO3WPMEeXjbec73tQcNIVg2aOwKnX0Zchtz7j9CvrtMTRA-hBhO0NFe34JA4jUNiE2SeRtJ6wN_w7B-oAwrGZ7CMP1mQpJHaSKqEpRTBwDHW6z3hyZju0I8CGeuMeNOHQ4MGRSKeuXm-XXz7aNl3qzCOEEe2UTve-MZRnXcpB15yTFSq6LYAZboGPAsVd5lhLV5SkD7zdtLeYUKvwPvx8848tlSpJD5GycfoTEDNYbmjlg0ow2SaF20Db-k0Ss6PfaecXGqTvgc0wsXdpgQAdRv4Yp08maj99vs-pSdxi9p4ZR9Lpl-UN78MRY6rZQLZpKF4ORwh2CpFMZ_5bxXhFtphpDvGoaDDZyLyupdi8pzYcK_NFdzM7CVrQIN6F1y9W9qOwreSMwmU0cupbwm048nRvteHBHeUK5zCu9kQ1Exoscq9pjtpfiMLz1DsQL6co-km2rYm5TsTPlcdYgeXKjPSJ6E_1affkqrbUbmrvHLl97fFYTtIcQ7CnFeD36Gu3oH7sElaCrqdgPz3ByKhHvK8RT7X62uqgXs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هیچ‌کس صدای «لبیک یا حسین» این زائران را نشنید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/454348" target="_blank">📅 08:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454347">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d613e41b.mp4?token=S3VLr5aWAiIzwZvlNc2s__gI50Hls7HffYhid0AHEs2whP5O7kMwTOlk800AZFfQnkhod6EYtJOASFNF9Bok1eIfyfIlBQqcsgfCoC3cZScax7X8zvuO4J0GdiPbHQZW4Rc1GdtItPc4hPX6_4lZDLyY_CX3TdkRTzHuv8--DRgs6I-bRk-ixKCZ8-I3VfaP5aKr8SSWIoQMkSbhJAzWetFY3-3LwLdP8jv19g9l66xIAkBSjdpXhjAsU5Ffhjf1KHYKpMc8w1AL0f7n7f4qCfHhTY3PjUBSKeuQqoCqzCRl_tITuD8aHdBhpnKW2tJu7I4ixzzxQE8Sf3e140G4t4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d613e41b.mp4?token=S3VLr5aWAiIzwZvlNc2s__gI50Hls7HffYhid0AHEs2whP5O7kMwTOlk800AZFfQnkhod6EYtJOASFNF9Bok1eIfyfIlBQqcsgfCoC3cZScax7X8zvuO4J0GdiPbHQZW4Rc1GdtItPc4hPX6_4lZDLyY_CX3TdkRTzHuv8--DRgs6I-bRk-ixKCZ8-I3VfaP5aKr8SSWIoQMkSbhJAzWetFY3-3LwLdP8jv19g9l66xIAkBSjdpXhjAsU5Ffhjf1KHYKpMc8w1AL0f7n7f4qCfHhTY3PjUBSKeuQqoCqzCRl_tITuD8aHdBhpnKW2tJu7I4ixzzxQE8Sf3e140G4t4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز پیاده‌روی جاماندگان اربعین در شیراز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/454347" target="_blank">📅 08:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454346">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f99bd1bffe.mp4?token=RThb7FsNL1enSoe99-vhE_5lyHC6PnMEy1kMQjo5F5EHdReLFu1zDuR1P6Bz6MrOMoHtiQlIJUBuKf27EUewV7153ZR9GXnz_7bvm4vnJO0sjVYN6bghGopvyCt34wMmr2YML5WwKztLTH2HAIg2XrK4USAyC5vZH73KR59z61Zh1TsNBdkS1x_GLUPWlAavm5rJTdEU7fD5A_615skv9pUBh9_ro_VfpHYG01eMqY24LPZAUeBP1_QIlBrPbaocJpqyhow6zlndcmMVF4bMahfMiNiI7BKhY8nouAO-Ym93gSEjV2aSTEjuTZZ1QX86oDs9b004QiG8L0-TA5Q4FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f99bd1bffe.mp4?token=RThb7FsNL1enSoe99-vhE_5lyHC6PnMEy1kMQjo5F5EHdReLFu1zDuR1P6Bz6MrOMoHtiQlIJUBuKf27EUewV7153ZR9GXnz_7bvm4vnJO0sjVYN6bghGopvyCt34wMmr2YML5WwKztLTH2HAIg2XrK4USAyC5vZH73KR59z61Zh1TsNBdkS1x_GLUPWlAavm5rJTdEU7fD5A_615skv9pUBh9_ro_VfpHYG01eMqY24LPZAUeBP1_QIlBrPbaocJpqyhow6zlndcmMVF4bMahfMiNiI7BKhY8nouAO-Ym93gSEjV2aSTEjuTZZ1QX86oDs9b004QiG8L0-TA5Q4FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم جاماندگان اربعین تهران
🔸
اجتماع بزرگ «خون‌خواهی آقای شهید ایران» در میدان امام حسین(ع)  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/454346" target="_blank">📅 08:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454345">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d23e42144.mp4?token=KtMDRMTMj4pTLSwqOJOAoXGnZLnUU6MNAouzUh4kUJZOkH7ytCyyWZAaLyS7KnYPR034vjMx5IxgmMct5G_ul8DeFhGPmvIS1KTOKyz0jyXOvzcBN1EaoFRHIp_YEfEqetPPvCDgpCg93LMxwNyyO0HqmMNqgWSgMes6weT9cCeIDOpTZTS-uFStDyd3b80tY2WqCSwJwAQkuv44eesCg-XB1bKG3n1ZfVeNUkgXUr7x6ZDdIx4iZu3x5nQU0z4XfZnLsmyzYQGUT5chclmZ0EpWeu8aXhXbamvCr5NeuYDKQRzIbgNGETv21B2yyxuHnRdH0ScNC4gxywhl2cimSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d23e42144.mp4?token=KtMDRMTMj4pTLSwqOJOAoXGnZLnUU6MNAouzUh4kUJZOkH7ytCyyWZAaLyS7KnYPR034vjMx5IxgmMct5G_ul8DeFhGPmvIS1KTOKyz0jyXOvzcBN1EaoFRHIp_YEfEqetPPvCDgpCg93LMxwNyyO0HqmMNqgWSgMes6weT9cCeIDOpTZTS-uFStDyd3b80tY2WqCSwJwAQkuv44eesCg-XB1bKG3n1ZfVeNUkgXUr7x6ZDdIx4iZu3x5nQU0z4XfZnLsmyzYQGUT5chclmZ0EpWeu8aXhXbamvCr5NeuYDKQRzIbgNGETv21B2yyxuHnRdH0ScNC4gxywhl2cimSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل زائران اربعین در کربلای معلی
@Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/454345" target="_blank">📅 08:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454338">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2OlVe1179nmDuiDMp7wKuhSpEJuQv8USQJXWpbyyWma00peiy_o559dQR4Yyb8pVVX1nxg7kbE-nDEi8TfpAh1z-Q-z9M4_yA3OSZTuzVm1YGp_wkxHd4nl9IU8ARETlGW4l_0EvyQMiXeS8zanNEzVNtYb0sWlEcJGMJQi1lcoWQWKZUSzdbypYP2i1R6V7qCYzial_2841Fay79QoxpmferznKAkEeT6dLZJUOQGCAIqIpR65ScBmG6oiF7k3k3S5163PSOknqGsddYv1HyRu1Vb3lA2SELOMSf40pWv1PA036YmmuEfB80RHGLiv7AUgvYH5H2k7GJLHkccddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UZ8XA5yG4y0q9y54dvnarq1E3K6uPvGrSO_NQmYlqnk5hj_bYO1JoWTdWFSnieiK6cdWS0n_JG9FZHFmQm-032LMWf4Al_AjTHQB2KX7x5NJmc80kSWG_HetIyy2SrwoB43xeV9V4y9WyoLamFJpCtcXOd7rtth1uru0ZlUFmS8k-8ukz3WEVjeDNpa-_VM06l4iwnwAwWDrqZL9rmALZ6M3tun7ROV6EkP3gJMPMne9SgwojgKsDrdetb3R0gboXQvvP1DUdDobk817XM0oDHwlUKP0-nmJVwMZaJt3Rij91ITWupUo0mc-R8esz18mjF6KmWIdtroV50U-wEAdWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKxqcJtSXcr3uUdVdCEXJeneAh1QVmjzHMOhcmQ47Owi521t7cg9dt6C6ifQ9XEAyGYLDYd-CTgg98XhRfxP2c4T1zQiIGAosF10zQSkT6yfPGumSMJu9IUCvrl47TFQVp9U4Nk0CaAZNUhn5VmIGzzE6vB3wEsZLjaXopgOSEwltKlLXqMCyAnIL5INHyFej803k1DGixijgJC75dRF4IUAbqY0aptOrRNlaLaxSZooDyylo3ZZLik17ksIpcTwp2KaGjyIg65u0_MhN4A-LBVuPFPQqQQQxAKpWfCpyS5QykluapLVOd7vZCUTNuIKVaNmq0wihyEn8zfBK6Fl5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpqmKRM12seUf3_IeAuqbLRxuEERSP8YDYQ575IFhywXO4KY9gCPU6CE9vEu-pLOHy3qVP-phlD2GbPY9J-MtyQTKqJge7fjoZIyiTc2UWPekoV8HhoGqP7G6Bkwf9kkFdgOJwxPV13YE_4iHi5wc5PNkYujrZKdH8QeHkBYqsM3VzRof0AI1n9nB_QrYmdVeEc9icLeDLhEjphU5asnCYZbhTu1q2iyi2ejswxGttU4UFy92h5KCpEPET5LMqVUq0e8G53ZNbqEQd6ZalgmUlZGAJBeCIDHO9l7MtpkEkS5MunSTfhLGp16Xcy6XeqTJhGkv8Is2-nShrEzgzlbmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d2XCJbjbVXwTLyte8xEeepM03-MUlD0WvOR17EEITeDKwBW4ASEn2a-0BoixA-zqOujqonMpAuuoZ588XMA1ObvxhNULcaz-VCCPf1l-TuxoI9Tg_EDBRaztA4vxx2c9YAXRDZybsDc4EDlAZ_B7fsHNksxeHLR2FZaCVdq17ZLtNVDvQVJvsNH_v34LB82uc6HKiYoXzywNJfWgFzqflE0BLe81x4AHxoLJq1gtn39VBy_bDJpoRHU7qcJPTVptChXoyqV2ny2OH4fOxEz8jtzlEcNN47WGUYQFCOEjLCUgbk6PESihP8qnFwY40cCQYE2vOOIQR1l0DiIey7uCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcKXUkPSZMZ5rikO-yjVq3HIaOO3E8QRBkMspdUheWfd-juxfy1Dj8iXQvVIEGvOlPkRywOn5HxQ-dTDFG9pQ1Zd2lu9Lwlwa8t1VsoTn5Vay-UcIEIEZPifxmIMf2s-xs2bvZir6rWKYICDfKuQi25qlIb2-bH0Sv2wPFbR--8V3bVv4QVkZSesL4oEcgYkcAq-qQb83ACGAYI6subqu9iUIwHv8lpFAYCJZbodPnky4vhta5NNC7gXJnx3WihsPgcFtK4u7KgngIxFf4crMl1N5HC6WeHLAc8s9ErUsPD5cVnhDyf0sIHOFzEXMlti2bSBiHNcyo4ah6Nk6-6FVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYz_ewDnuOhPx8bXYMhaumoiFvAjwVcVrYyFQlngqeQNSMU7aoZchNakdQ8chQ_ZxRumrZeFVZx0iZnlNdVU8u0EIqsCMxQCyPSj1ugMkA8ltGWb6TzeNDtzY-STsprxlb55sVqzMEOJyXGVhYA1ERQWnnnWKVTocOE87fYuF_6xoB2OreEG_mdHmH7UsiWv_V2QltdzjXOEDn3WYMAqq7dvlR0y1TQwtw88pACTTy3uuYZbhTLSs2mv9lQcadF9H8wkLqnSiWGRfh8feVtQy39p33vDYMAaFo3qY23WBtjQIVdSKMbQvxr4y1dcroPXHHAUpXIe4KuqysxEWP43xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
روایت دلدادگی در آغوش فرات
عکس:
حمید واحدی
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/454338" target="_blank">📅 08:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454337">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7b212acf9.mp4?token=WlWkgdskR4OgyF_mHWIs7-vgNcg5wO9YRhxCxyWTKWDuJSPHfyUN0DV3-e1PRgVpCwj_zSKU6b_zvyGPzyfwXiFDQVOCUMDDaUghSbo6sIP6rBhXYemNJ53G3kiCTNa_jlvNcaGJhWboqAAIZ-0eOn2jStQUi3aGzEvLRJlGA2pBrg2BY9KzZ8Mb_rPxDHyw1oeUgw0AzA6q9bRe8JpVoxkfG_LwUeEPfhbAuwil9YgBjh9S9kKGxUDgChKD2Qg0zh4LtnVAHWy4F4CUFOPJh9SwvIFX5vA2hDYNKrpxARx5DjbvVwC3JLHIxBhPPx7HClWOEYhRA5HZ4gWGyteOIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7b212acf9.mp4?token=WlWkgdskR4OgyF_mHWIs7-vgNcg5wO9YRhxCxyWTKWDuJSPHfyUN0DV3-e1PRgVpCwj_zSKU6b_zvyGPzyfwXiFDQVOCUMDDaUghSbo6sIP6rBhXYemNJ53G3kiCTNa_jlvNcaGJhWboqAAIZ-0eOn2jStQUi3aGzEvLRJlGA2pBrg2BY9KzZ8Mb_rPxDHyw1oeUgw0AzA6q9bRe8JpVoxkfG_LwUeEPfhbAuwil9YgBjh9S9kKGxUDgChKD2Qg0zh4LtnVAHWy4F4CUFOPJh9SwvIFX5vA2hDYNKrpxARx5DjbvVwC3JLHIxBhPPx7HClWOEYhRA5HZ4gWGyteOIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز مراسم جاماندگان اربعین تهران
🔸
اجتماع بزرگ «خون‌خواهی آقای شهید ایران» در میدان امام حسین(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/farsna/454337" target="_blank">📅 08:14 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454335">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d7de51822.mp4?token=CuB5EJJ3hae1g66mA3aqzUGwqvUb8SZ_Sp84Z8aAVytvvFzyIpIbSYeIgcKoVHfmADepPxtPosgjiVGOInxwfCOLNDNG6uvhA4EjVFpibuaMkV_FH7CGqdXWcm3joe7SnBFD0iRpB2tC38QLvYONc2fTnwD_jZodIOYGlCGIB64P7YHZfrg458XwHCVI-bUMNE75PmBrm67j6e_GQWXxKfyizG04JayaEIvig5aqtn3jnE1Q3cvMpGxpdSf7nWQr-60_aOD7KvcgwZ-VcicN8X4xpc3kGjxytOM6uVSbO9OR_tywJNiivYIghnM6G7QRlAx3HAntEs7MVALEoqBwWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d7de51822.mp4?token=CuB5EJJ3hae1g66mA3aqzUGwqvUb8SZ_Sp84Z8aAVytvvFzyIpIbSYeIgcKoVHfmADepPxtPosgjiVGOInxwfCOLNDNG6uvhA4EjVFpibuaMkV_FH7CGqdXWcm3joe7SnBFD0iRpB2tC38QLvYONc2fTnwD_jZodIOYGlCGIB64P7YHZfrg458XwHCVI-bUMNE75PmBrm67j6e_GQWXxKfyizG04JayaEIvig5aqtn3jnE1Q3cvMpGxpdSf7nWQr-60_aOD7KvcgwZ-VcicN8X4xpc3kGjxytOM6uVSbO9OR_tywJNiivYIghnM6G7QRlAx3HAntEs7MVALEoqBwWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئات دانشجویی در اربعین حسینی راهی مقتل رهبر شهید شدند
🔹
کاروان هیئات دانشجویی طبق سنت هرساله از مسجد دانشگاه تهران حرکت خود را آغاز کرد و در قالب دسته‌های عزاداری راهی مقتل رهبر شهید شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/454335" target="_blank">📅 08:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454334">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omuH8jzF2ojhj40J_IqDJy1iLmDhO-3A-De7MaBhR0GOCh5mzNC60QSezHnPERrIBvwusgM2-F9YhTq75MUtUX1c3t6bBFxZ1RyyHIfo0No7lbUGyNMngBxPSF--j-Hs3fuC13ES-DrubBn_K4GlInunSNr-202JLFUz-8RN-4ljtEPKZ-kYZNF4ofCRXV6YHtwiacUFXV2lCEwNMTaoGNmdihnyrxHdbUAXpvePh1lst_6XZyA3MllzyIEkFkr2Jp3-KVrz2LR9Zc29kPTj4xjwmfcjJAOpYErGvB-2Oqlbn3ASaJrMfRNj6cTjGuwKp7qLnxxNePjW19KT0JR8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس فیفا به کاخ سفید پناه برد
🔹
درحالی‌که یوفا، AFC و کونکاکاف با تمام قوا طرح استعفای اجباری اینفانتینو را دنبال می‌کنند، بن جیکوب خبرنگار CBS از پناه‌بردن رئیس فیفا به مقامات ارشد کاخ سفید برای رهایی از این فشار خبر داد.
🔹
اینفانتینو برای خروج از این بحران…</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/454334" target="_blank">📅 08:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454333">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بازی تکراری تحریم؛ این‌بار ساختار دفاعی روسیه در تیررس واشنگتن
🔹
بر اساس اعلامیۀ وزارت خارجۀ آمریکا، ایالات متحده، با استناد به قانون منع گسترش سلاح‌های کشتار جمعی علیه ایران، کرۀ شمالی و سوریه، نیروی زمینی روسیه و چندین ساختار وزارت دفاع این کشور را تحریم کرد.
🔹
فهرست [نهادهای تحریم‌شده] شامل مرکز لجستیک ۱۰۶۱، نیروی زمینی، ادارۀ اصلی موشکی و توپخانه، ادارۀ تحقیقات پیشرفته بین‌بخشی و پروژه‌های ویژه می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/farsna/454333" target="_blank">📅 07:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454332">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فاجعۀ امنیتی در لندن؛ اطلاعات ۱۱۴ هزار افسر پلیس لو رفت
🔹
روزنامۀ تایمز: در پی یک حمله سایبری گسترده، نام کامل و اطلاعات تماس بیش از ۱۱۴ هزار نفر از کارکنان نهادهای امنیتی و پلیس انگلیس در بازار سیاه دیجیتال منتشر شده است.
🔹
این فاجعه، افسرانی را که سالها به تعقیب مجرمان مشغول بوده‌اند، مستقیماً در معرض تهدید همان افرادی قرار داده که خود پیگیرشان هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/454332" target="_blank">📅 06:37 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2Ghjk6TQ6NQmpe6Tq6l03QP9E72VEFib5cevBnswJhQqFPeFC8Na_6HMujrTVkiVD-0gchvq4Lis4LvIxmODr4l65tlFmlGSdzFz23qrQYwjxpvN075to5cRvvLCZbJeFlHa2eXOPVaVM1ke8gtbtUT07_esBw3Daw2a9jFSpVGBmmRS4KNSXC81guNdZK06FaqvEJuQHonha9-NzSJYTeKouvlReW8rKD0NIvROavohYT4Fr8gRkIzgpBdvfvYbsIG5eOdapu5WL5LF2mmmYhRW3abRnKUr3OEfYL7XruMz0I5AR1AQvLJM1UcHbMij8OoZlU7M8r3_JwLmdq_UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گرانترین زمستان اروپا در راه است
🔹
با بسته ماندن تنگۀ هرمز قیمت گاز اروپا به ۷۰۰ دلار رسید. کارشناسان میگویند این قاره با گرانترین زمستان تاریخ خود مواجه خواهد شد.
🔹
شرکت گازپروم روسیه با انتشار بیانیه‌ای هشدار داد که کمبود گاز طبیعی در تأسیسات ذخیره‌سازی زیرزمینی اروپا، خطر جدی برای تأمین انرژی در فصل سرما ایجاد کرده است.
🔹
این هشدار در حالی مطرح می‌شود که سطح ذخایر گاز در مخازن اروپا در روز اول اوت به پایین‌ترین میزان ثبت‌شده از سال ۲۰۱۱ یعنی ۵۷٫۱۱ درصد رسیده است و پیش‌بینی می‌شود که این رقم تا اول اکتبر به زیر ۷۵ درصد سقوط کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454331" target="_blank">📅 05:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454328">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DtM5nrXxrknJLTTG4xASwbbCQeCmJD7xCiODGcJ_1hTacjSwUAxHylADIycOkTeWyP40pR9i4kW0lzPE2xioqUnvIQs2zewCT35NbGCEJkUXLtcVfPb5ex3jv3P2V-DJU0ZAGjuFyMla7eXyNgnIYmByCHAfllBJPdfxfGIRJUMdUB7CReUXaTEZHe6SbIYGg2JjNey9nGzWuxdPObCSzstsNrgbSz_rNxtkv4CpkfWZvYBDymH4rvfZBfkwr6cEUM5Y_i5B3hg8JKJHd29vocxZbS6_IGlkDgHH4UPocLOJnZwDg82QO2LEiNMyqOI9kkmRoLeQtS-DBo70boZxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCVU6ccJsy4tzGT16C1ATuVeC57tEBngHWZ24p-b9eCeu86F-8ZjWmD8hJ0u0IDrw3g32rNcvyPb-RNztsckO6D2vPdO7iLCUHF_bZf41oZUIApOIvlva4jC9fr9eqZRJLQ5BpnXzpqda9OsKqJtnXoyQfBzbd-UJpAgti-KoWNxNHaLPEW6_BZKUeWM8tzHFLkKn7kmisXecUHl9bDNRGbUYKPZKClJ8HyXNEaH36SwqsdQaCWtqHo7HMpAtBIvEzncO7IMuxR4OqeEsJ9EPuXj1Zz_y8gGfvm8FwU37AZqWzLi8qPkClYHwno9FT80YEuZF65IoE3eQb7ofQv4UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd196e81d.mp4?token=rnv-Fh6xET7ZCz0P9iFem5VhVC_9j7LGFRYWXHGxvyKJBOkFs61Tiy46lyA9s9c3uuSoJeNZrdNIxRm3DpagxVlenYPDBrND4fNDrlQmTw_7hcgOZkEL02wKCGQ95kZ53TmWipSYnkMTTt6OwF6lpFW_hyWCL4KgVnCHVw69PPSXMoScEKj6LlWHiOg27t9FxG_5xmhexKLr8Xm5KS0KVKwOzvU6LkbrJ3xT3uf1f2nvPNxARu9iUWB6pJFJHwMRYQu75Bb4uSejkizTnoI5__cqkt8WW57-HkWpc9WSjh-Ju_aeOg2IgTkoaAHbBH06CEnWgl9Ra8z4tNgOLwSsvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd196e81d.mp4?token=rnv-Fh6xET7ZCz0P9iFem5VhVC_9j7LGFRYWXHGxvyKJBOkFs61Tiy46lyA9s9c3uuSoJeNZrdNIxRm3DpagxVlenYPDBrND4fNDrlQmTw_7hcgOZkEL02wKCGQ95kZ53TmWipSYnkMTTt6OwF6lpFW_hyWCL4KgVnCHVw69PPSXMoScEKj6LlWHiOg27t9FxG_5xmhexKLr8Xm5KS0KVKwOzvU6LkbrJ3xT3uf1f2nvPNxARu9iUWB6pJFJHwMRYQu75Bb4uSejkizTnoI5__cqkt8WW57-HkWpc9WSjh-Ju_aeOg2IgTkoaAHbBH06CEnWgl9Ra8z4tNgOLwSsvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان سفیدپوش بنی‌عامر به کربلای معلی رسید
🔸
عزاداران موکب چندهزار نفری بنی‌عامر هرساله در ایام اربعین از بصره پیاده به کربلا می‌روند و با عزاداری ویژه خود در بین‌الحرمین شناخته شده‌اند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/454328" target="_blank">📅 05:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454327">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59dd190025.mp4?token=VjMx-DmpxWm-0exDwlCl0LmaiuqljwemkOdveC2Pt4cRaJndVbupTcPOM_hX1Nv2PumU7zQwo4r8ZU2rjy6c6ERkEKgQ_5p7Czl4sJvMXicOzOWo1XSSCPVjM2RAS7YlJjnvMwRh_6a80-MAjMg9kjNWiv2Mg8BHSiidlpSYtRPm4Gxd58dsBYtyBckz7ws8pu825veJ3X0lNdN2sMjixMyFkHavz039nfWwVh-enUdMATG0nKeNJ-Eq2S684hbzqkFexEHylQx2in-Shoi-i_I5i2dHVZ6wy0SYIwh8ZoRKPmsKRuIkW9Bqf1dFTY_m7ItCxR6wpGtGx5c0BogFQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59dd190025.mp4?token=VjMx-DmpxWm-0exDwlCl0LmaiuqljwemkOdveC2Pt4cRaJndVbupTcPOM_hX1Nv2PumU7zQwo4r8ZU2rjy6c6ERkEKgQ_5p7Czl4sJvMXicOzOWo1XSSCPVjM2RAS7YlJjnvMwRh_6a80-MAjMg9kjNWiv2Mg8BHSiidlpSYtRPm4Gxd58dsBYtyBckz7ws8pu825veJ3X0lNdN2sMjixMyFkHavz039nfWwVh-enUdMATG0nKeNJ-Eq2S684hbzqkFexEHylQx2in-Shoi-i_I5i2dHVZ6wy0SYIwh8ZoRKPmsKRuIkW9Bqf1dFTY_m7ItCxR6wpGtGx5c0BogFQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادعای ماسک از بازگرداندن بینایی تا «دید فراانسانی»
🔹
ایلان ماسک اعلام کرده است که نورالینک قصد دارد نخستین تراشۀ مخصوص بازگرداندن بینایی را طی ۶ تا ۱۲ ماه آینده روی انسان آزمایش کند. به گفته او، این تراشه می‌تواند حتی به افرادی که از بدو تولد نابینا بوده‌اند کمک کند، زیرا به جای ترمیم چشم یا عصب بینایی، اطلاعات تصویری را مستقیماً به بخش بینایی مغز ارسال می‌کند.
🔹
گرچه کارشناسان می‌گویند بازگرداندن بینایی به همه افرادی که از بدو تولد نابینا بوده‌اند، به این سادگی نیست.
🔹
ماسک همچنین از ایدۀ «بینایی فراانسانی» صحبت کرده است؛ یعنی توانایی دیدن نور مادون‌قرمز، فرابنفش یا اطلاعاتی که چشم انسان به‌طور طبیعی قادر به مشاهده آن نیست.
🔹
از نظر تئوری، حسگرهای ویژه می‌توانند چنین اطلاعاتی را ثبت کرده و به سیگنال‌هایی تبدیل کنند که مغز آن‌ها را یاد بگیرد تفسیر کند، اما تاکنون هیچ مدرک بالینی معتبری وجود ندارد که نشان دهد انسان می‌تواند با استفاده از تراشه‌های مغزی به چنین توانایی‌هایی دست پیدا کند.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454327" target="_blank">📅 04:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454326">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk44ANAwxYjyjbZhed9l_4rgxV9lxDA8IZ68KfuHIawtFwdf5IKcVfqR8cxRSNYG0T__g5umfGKF1q3ODzDyBcJRRctbqIWVKhYXaYLUbjjbe1RT3pEQ6nYpInOiUdBRRS1WJGwZtz7LTkJkpmeIdwHQR7L1TzaB6xyrgPtXbir6uZ-ehZbmBLSsx_XY0XzOz626wZYRRrb9JB8RX8YxXyYhVL2uAJuYdXrTJ3NyXjHXlgF3B2_Qz-G31FsKz542_C2GN7ecpCJZJDIGYheOFRHqyt2U3bl_joHw-zoKb5WpO1kyxRrjcsi2tlj60K3R2WZoDr6Cx3rKqBMPDXqidg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای پشت پردۀ التماس ترامپ به شرکت‌های نفتی
🔹
در حالی که ترامپ یک روز از سودآوری جنگ با ایران و فروش بیشتر نفت سخن می‌گفت، اکنون به شرکت‌های نفتی التماس کرده قیمت سوخت مصرف‌کنندگان را کاهش دهند.
🔹
رئیس‌جمهور آمریکا فشار خود بر شرکت‌های نفتی را تشدید کرده و از آنها خواسته تا قیمت سوخت برای مصرف‌کنندگان آمریکایی را فوراً کاهش دهند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454326" target="_blank">📅 03:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454325">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1839906b.mp4?token=LUOnTiPze_caXw22G5Iepg9vjH5zRY5EbVxJ8Q_Ld_l8lCY4maAk-fr3OEXoSZ6NwSXsQSA_GugP2LBH3o7fK4Hv1tdSKK21jt9K-cKk86SwGJbdX9aH6RJ3N-3DOlrOJv_nw7Teyu_zY-TCNG47Q0hUeuY2Anf6vWvILPHDqbtwL4YHHkLvE7VyhTfGa8T2k3QsIIMvlLXkidYBqKkZxWHh3_7Gwe6cOmUAbtHQotTO6twkVHUzov2h2Tsv8FxPPrO_afsG1S20V-vTXQb4YiBkJ3tE8x1bvqA-d8h8JUUTfqF6LuPvGwK4c4z1GiAAnkocJFw3UXC2gyZZBznv2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1839906b.mp4?token=LUOnTiPze_caXw22G5Iepg9vjH5zRY5EbVxJ8Q_Ld_l8lCY4maAk-fr3OEXoSZ6NwSXsQSA_GugP2LBH3o7fK4Hv1tdSKK21jt9K-cKk86SwGJbdX9aH6RJ3N-3DOlrOJv_nw7Teyu_zY-TCNG47Q0hUeuY2Anf6vWvILPHDqbtwL4YHHkLvE7VyhTfGa8T2k3QsIIMvlLXkidYBqKkZxWHh3_7Gwe6cOmUAbtHQotTO6twkVHUzov2h2Tsv8FxPPrO_afsG1S20V-vTXQb4YiBkJ3tE8x1bvqA-d8h8JUUTfqF6LuPvGwK4c4z1GiAAnkocJFw3UXC2gyZZBznv2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای زائران مزار رهبر شهید انقلاب در حرم مطهر رضوی در شب اربعین حسینی
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454325" target="_blank">📅 03:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454324">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-qwMlXwPs6SggoY9m0Zp1FdAs2EGb20cz8uHIcLEHp-YdG4alEO-__oCxGTIj3lk708u1vD-ru0d02boFhE0rW8N9YtDcuRivhTb_NCuLZfgckr9HcD8DciGG4vYmKWGor1N_WJlXvsdaUHhegCgZKz5bGOL0NLRSlF3q5h5JaITLU9-JJujzAfe_HVvsGLDrUs8dlWBBvc_2iWY01xQGCJ1n0zDQYSmjxCVEjNadh1mNNP_K2xGptOt3ODc5utxR5-NK5iyON2PAp4Ug5wCzb3HpTVU3ssfYzic8VEFa74ITE29I8XN5dZ-sjNa67IIn8bCBG_fw8rUuSYzCg8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوزویک قدرت ایران در تنگۀ هرمز را هسته‌ای‌تر از بمب خواند
🔹
نشریۀ نیوزویک در تحلیلی به نقل از یک مقام ارشد سابق نیروی دریایی آمریکا نوشته است که «قدرت ایران در تحمیل هزینه به اقتصاد جهانی، از برخی جهات، سلاحی قوی‌تر از بمب اتم است».
🔹
به نوشته نیوزویک، کارزار ایران برای اعمال فشار بر تردد بر تنگۀ هرمز، تأثیرات ویرانگری بر تجارت جهانی انرژی گذاشته و این تأثیرات در نقاط مختلف جهان از جمله ایالات متحده احساس شده است.
🔹
به اعتقاد این تحلیل، تسلط و اهرم فشار ایران بر این آبراه حیاتی، می‌تواند در نهایت سلاحی کارآمدتر از جنگ‌افزارهای اتمی باشد که آمریکا در سال ۱۹۴۵ وارد میدان نبرد کرد.
عکس: حسن قائدی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454324" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454315">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fCivr1U2LJyhVDsMYmppCzcuAZmH6q6YC26kmK79fVLha_X27gfU33A_c8UHSN42YZCsLNy-zbRfmLx2F6G-TLfRDNc2SbDhrE_7wnHr2lphHzPmjsys76Q0-jqngk1talOgcLE18kBYvNh-YRf8M9rpnjwdyZ-oy8LhfvylMRP9d2ipbJ-jrMDb6TufCrs8Vc1C2EyBVBm7bS1tO7THH1JdXeyQLVotYz7EmWPFYb6YTk4pnEad8Lzg93T8MEPTPJqJcIFfNxS6E4FP5-LAJuceyrf5Bu4VP8LNkSiKU4eVdcuvj-Ba6pSb10nqALmOFDSKon1vhoQpKVn-rZbfnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anKWIoNXN0ayGY0_itzABWUUsHhR563DrqOfgwgZJ0mdSiBFZ5zt7wbYuOLPstf3EPaSkY-1owEMcPA8bZRsqcMP8IXsaxlBfmLaZyacfuBf4RMQi0e_bR0N4dQJLtPJDyEKx1PidAwsEKRXahcPDIJMPfk2kTEqRrdZe04uzJp9X_euVmoIEKi-E6uGACD5MWzZfLyalV3Ygy_Hw3zgNdYh0taVMfmKbb5zF17MANVsrTH731ZK-OsVKVYI0h6fi-1oMQzumRKYhNlmxG4_r0eVykxBsaBSIBKwUQIoH3nh5smE92jn0utItUci4P85wf9SoI5zGMwa-UTVgWaMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/exVa3VDxsoo6JDd5-1p_7GE6E9kkjB9y0mF0-DHvhefSMXG6ObnmFnc4vFVLu8cun6Da-lsr_VkLZWiWYpMc9OXaaw6v3K7RzyUBHO9eWxKJhpc2P_BTswIrxuhRWJ1HQ3hWpUG1vY_QGZzO5WBLt-2zR4_yFhHi3CGHN_qUowDVQIbD8hDAViK3BelcfKPaMfZBwmps_goNmcfKPYb7mgXluFFNS_tp54Xzqhj5gNcZJ5Hzmr02HZ0o3nk6m0LE3TUVB-5OYRsaAnNq1htu8ua-DzjFmPgv7rX6R2TGs05E5L5G1mZxpNnb0FnyXexkfyMsUt923cYSni1nimj2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XodA2A1SXVTLTh32VAh8-xupnbiBtOOMOowme1V7nTem7Rh31SGrEoYIsO-oJKATcfSs3DRy6SIlsbQXvOVFxY_07Z5QpJ56Fux3d0urBHXuieoLFt94BWHFFyQc-EL7k3i1XyuYnvRnb4VFTmVUOgDJXKPQLBNhkLZ_fwD9mZzBhvjcZBkI3o3OSKZ1yqOVeUAEVb3TBH8CD1MqSb8PsTpw5QVKejS3JfBDtlYLijkXSJAIvuSEoLF18HDpKt6ph_O3q8jcQmqh_0a9eCexSN3y4LPWRWA8PtAYNS0v_pYYDgAlM2poOjNrvQuGxYWclwhzeyvpBbgxtuPy2KDiEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYYvx79K6F4-_BWhpl_exKV4oTWe44y4vNbf8QrsBDJ9rfQfNIc0Kdlz6PLR8gfRJPbPdW6mbd9V-eM1BKKbBTbtoB2IigFmLNNcJ08rFR5hIm70IwoS0SP-htZGJvUurzuCum2nupBjX348kCxdQsBuSjCt45ZrgzicwbU2tOW_NTsJcb5bQgP5oLdlxKsGyZ9s7bbI7LxtzEcpi02X4Hpz7ujMR3C5HpKlhfG0_eu7ktsh7ydOUF6AvLeaeA_eLVQXZlPXlt779L7qF5ndPxmAb3Lap-UPkbFmRXpodOaOGUc-kzXsYQkDJf3XABfFuMnQRa0gxrSO18l_pHWUgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gK5B9JUfZdVwhqqpYA_X-0hmbLYyQbfjz6IysQCP6cmgmYpKsbctFKhO5zDiCFKDofSADVG3oMGtmZyO0BqyrGzK75MThz5DQZb7fyo6Ds3Bq756o62NVDXgyHekVkrXx6Lkea5OnUR01P4CfyNstTIZDs9gq1jX-JNiw1MW0i23bT4HsUXwNETONNbyy_YAhx6Mw_mZlrzJHE-K-NBP6W-gLq2MqsnAHchkP98UJkvdj__XxuovMjheIKexxfuClQak8_4XQUATyTLP7nLf94j8pADWWxP00n1obs978K1HTniKFVjdGskqffyKSb_-aE4MXfz_7orWJhNxtDpHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkyGdjaEIpfj_pS6rr8mgrHVRlEC-wbCtUjpYzUYt6lsgV_0UEtBk4iQIv9dAvk1JR2aKLEx4ZtbM0af0O_Ykfk1x-cwMBL3SHvjol_8DuR52Wz2epoMWDc6MCxYkU1jiQvfGxaJpVK9FSJzpogJoqdAY9LZAGZsb-Fwfz0rVD7cJi6uy5CDN1xDtPfQf1Po1iG5QNbADXlrMYd-LfuxMAPlliT0J_AiiBeYWrw0AywAHfZMbeeIV6LEuZCquSZTe3iHfaEDkvX3xfi8KJq7CwPDPfabcMTS2E9Bb9B8jjOKW71iOuycorEF3j2eP3x3CXHlEZxG_hZAsU0PSSP0Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C6l7xGr_De8TQr4XXcAcx_MK2noahZDEvvBJKDR1TaNxKBS746HXrL4NE7O7C9D7fxsReVj7FO51qOSQGmJz7TEn-3xA2oey4qSIjcAZAJzDshBYwhw2WnZhuXr5sXJ9r3W__Nq35GrEwKHTZWkbMR4ugZwV1CnYnTE5ueQaW5NGQ9DbRlYfGksnv3QisJ6a_CRxSC9bxgGePRE5dc9nU1EXYu50MexF7RFBMy-Hhy5e9gSeAdCrtccedNtecqgIHYeMpFNKe2393YMA1gha-sKfuNW5NoRU74IiEyofpBJF7PBGaE_YuX6hru9tKtDCD-RRUlSWeC4IA6KtET792A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXa9zsVUp8dVGDHeCt3sadVObOuU6vryRT0r8kOuoFpV_Lr8p9mGcEJs9Kmu9iJbQK9oF7h0zjUFLB23AZX84ZZG4CCDZUozT88KojiJpGnsFkPvHKp123cApB__lXpCTjT5awWY2ssvAG710F-LhvjETKubJwK1gblfnAuappWplBj-F4U_7HQ2Bijif5deDAXEeZ6iRZRD6NIuI3Y7Ra5zDa_xUzW5FkzvVr1ptnInBrc7IQmw6e_ET0zF7Knjukf4spxat2UNbfT3yGoX19_3LZtvfcW5BlYp8Ru4Io6hV4ahufvtGpNlHcTiOSRyi4EqfW_JUw7Ggp0g5UF-RQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حال‌وهوای بین‌الحرمین در شب اربعین حسینی
عکس:
حسین شاه بداغی
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454315" target="_blank">📅 02:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454314">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
رسانه‌های عربی از آتش‌سوزی گسترده در مرکز کویت گزارش می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454314" target="_blank">📅 02:25 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454312">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efa8d399fa.mp4?token=cUpI0dw3VApVxdPo647RURMR1o2kjV9-VwqjiKeOzJC0KecbRMJQGXo2DJVFRr6JOfMac_m5zoVSPA-XUggDXYnFrQKJC7D9HMZdIG8wcdWMmqeyUUULvbZmV0nLXyYCb7kN8VAZOZqjeDrQZb2jGdKjNZ4SPbw9SgOZ132bWLJuvYnphw-R5Pxvs5NFcO2addyZKSBFPchq91I5I4vMGOa6RKODsX4wqQ_q6P80cc0uyWT-NMqN6RyEwyaqJLQ4PPMYE2OQpHM_N1n5iQHavAIdQPJYl0IwyhpxqNug92B2k7u3AeHa27X8oITMYomMT2hVa-tKUgxv6mNBaWUvLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efa8d399fa.mp4?token=cUpI0dw3VApVxdPo647RURMR1o2kjV9-VwqjiKeOzJC0KecbRMJQGXo2DJVFRr6JOfMac_m5zoVSPA-XUggDXYnFrQKJC7D9HMZdIG8wcdWMmqeyUUULvbZmV0nLXyYCb7kN8VAZOZqjeDrQZb2jGdKjNZ4SPbw9SgOZ132bWLJuvYnphw-R5Pxvs5NFcO2addyZKSBFPchq91I5I4vMGOa6RKODsX4wqQ_q6P80cc0uyWT-NMqN6RyEwyaqJLQ4PPMYE2OQpHM_N1n5iQHavAIdQPJYl0IwyhpxqNug92B2k7u3AeHa27X8oITMYomMT2hVa-tKUgxv6mNBaWUvLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
منابع عربی از وقوع چندین انفجار شدید در کویت خبر می‌دهند.
🔹
گفته می‌شود صدای این انفجارها در جنوب عراق نیز شنیده شده است.  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/454312" target="_blank">📅 02:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454311">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
منابع عربی از وقوع چندین انفجار شدید در کویت خبر می‌دهند.
🔹
گفته می‌شود صدای این انفجارها در جنوب عراق نیز شنیده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454311" target="_blank">📅 02:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454310">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuGFja_To8RN5P-03x-wjGmJnbJftnS5aXEY40xacDrHbarQq029edhQj1l-ULm8xFQmnfmI3EB4T10NbTWUXWu2FRxK0en2wGkAwCQ4lXFgveVGPtvyS88NubuqkZn2tkSOXsvJCKZlQhvTAM5xn5hpVTiGmN05JrG1b7TceRmVANmV3Hfe7WlxI76MdEBIY6E5_PoeGjVa-BJgHQyXYxwvY2VPbDKeBxp9GLZmTwIL_5yhVtXa18A9QC_P75cfrwlaOjDDaUYtCahAtpy3024O4W6lnToKO102ioOxhGUznBO-3F5oK9Da2LEc2M3ocamwyXHnPvRvO8PQEnjaow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
زمین‌لرزه‌ای به بزرگی ۴.۱ ریشتر، ساعت ۱:۴۵ بامداد حوالی فارغان در استان هرمزگان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/454310" target="_blank">📅 02:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454309">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a992f7e7.mp4?token=UM8lKBup_PVC7p173VvwT6CXQmQNEjhHWChOMYE4qB3jAidgt4yvBfbcPEcE4Vp7qgwuOdlCjW5rYiQH0yHN4lq_Wm4fxiklnbGqDWYbUH5qJ3rm76aJInYgq-6hA_JuXCldoS03oDJbPLVg8rDTh8bf8_soucCNQ4_tVCwA9xbjFCFDKGpght_Ez65d_8L1JFVzB77wilkesphtx0E88dop76t56icUHXQU3w9gXMCZIZT2k6qyHXK074yj5oOxWsL76Ldpw6lPF6I9m9i8adnfyNBUXeCJUAkjvMV1tal2htCGAPBIL0RdkstBLa3uqathosbtqwVXsmg7xg6hXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a992f7e7.mp4?token=UM8lKBup_PVC7p173VvwT6CXQmQNEjhHWChOMYE4qB3jAidgt4yvBfbcPEcE4Vp7qgwuOdlCjW5rYiQH0yHN4lq_Wm4fxiklnbGqDWYbUH5qJ3rm76aJInYgq-6hA_JuXCldoS03oDJbPLVg8rDTh8bf8_soucCNQ4_tVCwA9xbjFCFDKGpght_Ez65d_8L1JFVzB77wilkesphtx0E88dop76t56icUHXQU3w9gXMCZIZT2k6qyHXK074yj5oOxWsL76Ldpw6lPF6I9m9i8adnfyNBUXeCJUAkjvMV1tal2htCGAPBIL0RdkstBLa3uqathosbtqwVXsmg7xg6hXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبور شمار قربانیان زلزلۀ ونزوئلا از ۶ هزار نفر
🔹
رئیس پارلمان ونزوئلا اعلام کرد تعداد جان‌باختگان زلزلۀ اخیر در این کشور به ۶ هزار و ۱۲۵ نفر افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454309" target="_blank">📅 02:04 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454308">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pm327kTRTs9q51UzeXQohDOLlE8_VbwbD7rSK9DZA1fhud07EXFQc9bz2P5gVGdqIqVCFDCiWDUBaubo4bhmujcl-WA3aVgLFn-GDHeW76gD0ps-_WgRgHoX4QZfE9Gbb2JocznLh29u9GnVDc7Oxp64QERJfR982vIHTYoN_DOeSFc4IZW2XjNESPgTV2ovAelLOZxduWpAAWvKdty6Vg9XsEa4GjMzqlSbySifz4u_Sh95QQzqz-wyNP6h4ORpFQlCsCshZnW4V2je70NYgT1APEWkoc9HtKpAYjOybICoFs0AgKtI9v59OuZs-4Ie5em72LecB7My5k8jTZDFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد بین‌الملل: کنوانسیون دریای خزر در خدمت منافع آمریکا، اروپا و اسرائیل است
🔹
احمد کاظمی استاد حقوق بین‌الملل، تصویب کنوانسیون رژیم حقوقی دریای کاسپین را یک امتیاز مستقیم راهبردی برای رژیم صهیونیستی دانست و گفت این کنوانسیون علاوه بر تأمین منافع راهبردی آمریکا، اروپا و ناتو، یک تهدید امنیتی برای ایران محسوب می‌شود.
🔹
وی بهره‌مندی رژیم صهیونیستی از تصویب کنوانسیون، حضور غیرمستقیم آمریکا و اسرائیل در دریای کاسپین، احداث خطوط لولۀ انرژی به سود غرب و به زیان ایران و چندین موارد دیگر را مهم‌ترین دلایل مخالفت خود اعلام کرد.
🔗
اما چرا تصویب این لایحه از جنبه‌های حقوقی، ژئوپلیتیکی، ژئواکونومیکی، امنیتی و نظامی، پیامدهای متعددی برای ایران به همراه خواهد داشت؟
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454308" target="_blank">📅 01:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454307">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89fbaafe73.mp4?token=JQ8RV9svyfr7LWdQkDp6CN8jWSx-VcyCwA72QvhTrN89XUFy4MpRE49YEK0K_hMOx7t_B4Dq1202lQEWR0zOOTKIeHmYNiMXw1SKnZL72w2C8BimmGLTE1It8l4odEL4_hnc8cdF5ok_YAdS5WNIFi1FTSurbSEnUwQTXFO5_doN3ZbjJg2CPNYf13m1H4JnTFHMEe8w2PTKONXw6Jf6oQGqkInnobkcXBzLnYv7zs_hfxLT6jQEIMmomY7QGZEnQcX4tfN6CSClrGfORgNsHSOOqq8G5Xg5UmsyarTrCLWZtqCDCTAQDA7u34MzaPOQ1Jp2XTHzbm75Fop_rtAeoxFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89fbaafe73.mp4?token=JQ8RV9svyfr7LWdQkDp6CN8jWSx-VcyCwA72QvhTrN89XUFy4MpRE49YEK0K_hMOx7t_B4Dq1202lQEWR0zOOTKIeHmYNiMXw1SKnZL72w2C8BimmGLTE1It8l4odEL4_hnc8cdF5ok_YAdS5WNIFi1FTSurbSEnUwQTXFO5_doN3ZbjJg2CPNYf13m1H4JnTFHMEe8w2PTKONXw6Jf6oQGqkInnobkcXBzLnYv7zs_hfxLT6jQEIMmomY7QGZEnQcX4tfN6CSClrGfORgNsHSOOqq8G5Xg5UmsyarTrCLWZtqCDCTAQDA7u34MzaPOQ1Jp2XTHzbm75Fop_rtAeoxFPBD23tTpfxlIToBYhwS7eF9c0NpkwDArvx_nbwNJkG_12uDJXVvzwSKVrGCVt3gH2ta_0kJeOTZRem2VnRFeS5Nip-EfQgInulFRnQXu9pyz8sp68LwI7DQM8ShpciuRme9L22Pojk6YNMHNzD4-inLcKuCTN6F7RXEcPtoNukWgncIdd_MDlJFQr84eIpvgqz4x_8WhVyvdQ7bkW57QizTR7eFB17a00blyyU5es81W4zBnNkBtoCBmSNqSBNeaepy29aZONf7R1shUaRKuo1OYVUYyzHEiPZbef3WmSkP9HIWELUyqIk4EBzwUrmrnhBgemxCf3q2mEQiLlOrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رضا صادقی برای پیاده‌های اربعین خواند
◾️
همزمان با فرارسیدن اربعین حسینی، نماهنگ «پیاده‌ها» با صدای رضا صادقی، منتشر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/454307" target="_blank">📅 01:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454306">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZnBX0d9FepiNsD8WjAeT8yHw312fK9Ie1RvN-Wzfjl6AWiBB8D2QIBlX9p1V0aib-W8dJBhATpoxxFhwHnzBeIUJw5FWrqxNWePjjYTB2IsN8bLEDOyzdK5rgJmNefznhn60FOsCPiIHxGAdu5kWW7X6gp1CPNsMF5E_Vvw6fhcKeOqG--vAZLey_7Rka1jeEB9WalGDlWPoSOvnBLpvGOvXaThQcd0CrE-2vD_g8mf4-yLU60wagYlFziHmbHSXWE1MsRO8uGpUWXhQRBXfW8TSZMx_-qLPX8YWNsi3lPhwQXeepQo9BHkIG_9VK7gUxVyVFErZI8AtKUc8Y7eFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش حماس به زیاده‌خواهی نمایندۀ ترامپ در شورای صلح
🔸
ملادنوف رئیس شورای به اصطلاح صلح آمریکایی در دیدار با نتانیاهو مدعی شده بود که تا وقتی حماس به‌صورت کامل خلع سلاح نشود، نظامیان اشغالگر از نوار غزه خارج نمی‌شوند.
🔹
حماس نیز در واکنش به گزافه‌گویی وی اعلام کرد: گروه‌های مقاومت به تعهدات توافق شده متعهد هستند، اما رژیم صهیونیستی به هیچ‌کدام از تعهداتش پایبند نبوده است.
🔹
ما منتظر پاسخی روشن و رسمی از ملادنوف و میانجی‌ها درمورد توافقات هستیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454306" target="_blank">📅 01:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454305">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03465f95c0.mp4?token=fK8co7N3wQ2WOwU1gokrbRsIoIyNxC5n9lOnFRlqQLulVNFteEjUtElmXHCLvLUkt9ba2-TbaoM88jbdUg4XgOcC_plXSVwyTecf-hIGjbb1i8Cay8Xv_DV1lwNCd1EDvBawsULJTgvd63sPELWH6-38Z-auCeYpmCEqL4fZkBLRO8tG5thB16XgXHaQ9AnYKkSUQZ_rXqIAyBIxlkue-x730QYL6ilw8C1cfOLUHd1OjolqTiGZTf_FtCyY7K4Tb7mRouzVqtKYnrxQC7lMGWv-kpmFAeCEYZ52Rh4Lbp_P-pkUN7ScfNrI2FPI3ZSHSwknJUBYhYX3cGS1527MsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03465f95c0.mp4?token=fK8co7N3wQ2WOwU1gokrbRsIoIyNxC5n9lOnFRlqQLulVNFteEjUtElmXHCLvLUkt9ba2-TbaoM88jbdUg4XgOcC_plXSVwyTecf-hIGjbb1i8Cay8Xv_DV1lwNCd1EDvBawsULJTgvd63sPELWH6-38Z-auCeYpmCEqL4fZkBLRO8tG5thB16XgXHaQ9AnYKkSUQZ_rXqIAyBIxlkue-x730QYL6ilw8C1cfOLUHd1OjolqTiGZTf_FtCyY7K4Tb7mRouzVqtKYnrxQC7lMGWv-kpmFAeCEYZ52Rh4Lbp_P-pkUN7ScfNrI2FPI3ZSHSwknJUBYhYX3cGS1527MsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع اربعینی مردم رشت در میدانِ خیابان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/454305" target="_blank">📅 00:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">بازداشت معترضان به جنگ علیه ایران در مقابل کنگرۀ آمریکا
🔹
تعدادی از روحانیون مسیحی و فعالان حقوق بشر، در جریان اعتراض به جنگ علیه ایران و ابراز نگرانی دربارۀ حقوق رأی‌دهندگان در مقابل کنگرۀ آمریکا بازداشت شدند.
🔸
نظرسنجی‌ها نشان می‌دهد که اکثر مردم آمریکا مخالف تجاوز نظامی علیه ایران هستند. آمریکایی‌ها معتقدند که جنگ علیه ایران ارزش هزینه‌هایش را نداشته و خواستار پایان فوری درگیری‌ها هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/454304" target="_blank">📅 00:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454303">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تأکید کشورهای میانجی بر فشار به اسرائیل برای اجرای توافق غزه
🔹
کشورهای میانجی توافق آتش‌بس در نوار غزه (قطر، مصر، ترکیه)، بیانیۀ مشترکی دربارۀ نقض‌های مستمر اسرائیل در غزه صادر کردند.
🔹
در این بیانیه نقض‌های مستمر اسرائیل در نوار غزه، به ویژه هدف قرار دادن تأسیسات و مراکز بهداشتی و درمانی و شهادت تعدادی از زنان و کودکان محکوم شد.
🔹
این کشورها با اشاره به اینکه این اقدامات نقض آشکار قوانین بین‌المللی و حقوق بین‌الملل بشردوستانه محسوب می‌شود، بر لزوم پایبندی اسرائیل به تمامی تعهدات خود بر اساس قوانین بین‌المللی و اجرای کامل الزامات مندرج در توافق آتش‌بس تأکید کردند.
🔹
در این بیانیه تأکید شد، ادامۀ این نقض‌ها به معنای شکست توافق بوده و تلاش‌های صورت گرفته برای اجرای مرحلۀ دوم آن را تضعیف می‌کند و مشکلات غیرنظامیان در نوار غزه را افزایش می‌دهد.
🔹
میانجی‌ها بار دیگر خواستار تضمین کامل حمایت از غیرنظامیان و دسترسی بدون مانع کمک‌های بشردوستانه و تجهیزات پزشکی به تمامی نقاط نوار غزه شدند.
🔸
میانجی‌ها همچنین از جامعۀ جهانی خواستند فشارهای لازم را بر اسرائیل وارد آورد تا به تعهدات خود بر اساس قوانین بین‌المللی و توافق آتش‌بس عمل کند.
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454303" target="_blank">📅 00:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454302">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/349825ca84.mp4?token=rZYslTCfNJtqSpZ5j23Zg7dk_WFO1Mc1pN3u7dc1VJ60dyY-SCUfAMLlC9THXFg-7HsIJ1S8qg9NpP5FXW8IM2UWmRO41bIbczejM_NuZQp5QbPJiTi-j9tWNFuRe680mqgMt9BbjcvVyy5AMzg0qNJWto6mft8YUTXO23SfJmGcqt-6obvrIUixXy9MjGQvPKby9psouijGBEx2R-u1s0Cl7OOT1ni5QmJSJ6Uedvz0dgrByYxkgtHfs4Wyi_QbjmPG1UXIG2vqXZfb84kcYHaYoFqxcShRVyvOoo6Zmbqb-kt1H7-4mF8VrLTfcRMqZ4UuRu3wsE8urkAf4LLpJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/349825ca84.mp4?token=rZYslTCfNJtqSpZ5j23Zg7dk_WFO1Mc1pN3u7dc1VJ60dyY-SCUfAMLlC9THXFg-7HsIJ1S8qg9NpP5FXW8IM2UWmRO41bIbczejM_NuZQp5QbPJiTi-j9tWNFuRe680mqgMt9BbjcvVyy5AMzg0qNJWto6mft8YUTXO23SfJmGcqt-6obvrIUixXy9MjGQvPKby9psouijGBEx2R-u1s0Cl7OOT1ni5QmJSJ6Uedvz0dgrByYxkgtHfs4Wyi_QbjmPG1UXIG2vqXZfb84kcYHaYoFqxcShRVyvOoo6Zmbqb-kt1H7-4mF8VrLTfcRMqZ4UuRu3wsE8urkAf4LLpJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تایم‌لپس موج بازگشت زائران در مرز مهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454302" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454301">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70140da514.mp4?token=UHFXkKnfmsv0ZbkYpniA-7YMiaUeUYbmZ9vb37qMA4KEjXB0BpVkXV08hS9HBJvk_bv42nRgJYyjrXDHxHxXRhoj0w51zOM_EW6O-6FGPOtIu9gGUncO0ObU9DJLCyZPiAON9muFM5vg4LKjO8iCtazAfBuUUXDKH5KBnpj-RA89ZWMPFZ_WVAon0R3eZjc2yIrnnxxWiFVqpnmqr29Jy2YX5XxYBIvq7hEtRgQrCVGL5S0Stl2Z-2LvG91Qd9c6uYuNxBoGEQmbJQ7EohYf1qpp3mxVn2GV0FxzWSFrI9pehAGLZ9qqUyUZXWWtI3BsmZj8CWo8eMVG_GIg7W2PnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70140da514.mp4?token=UHFXkKnfmsv0ZbkYpniA-7YMiaUeUYbmZ9vb37qMA4KEjXB0BpVkXV08hS9HBJvk_bv42nRgJYyjrXDHxHxXRhoj0w51zOM_EW6O-6FGPOtIu9gGUncO0ObU9DJLCyZPiAON9muFM5vg4LKjO8iCtazAfBuUUXDKH5KBnpj-RA89ZWMPFZ_WVAon0R3eZjc2yIrnnxxWiFVqpnmqr29Jy2YX5XxYBIvq7hEtRgQrCVGL5S0Stl2Z-2LvG91Qd9c6uYuNxBoGEQmbJQ7EohYf1qpp3mxVn2GV0FxzWSFrI9pehAGLZ9qqUyUZXWWtI3BsmZj8CWo8eMVG_GIg7W2PnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از قرائت زیارت اربعین در حضور رهبر شهید انقلاب در حسینیه امام خمینی در سال ۱۳۹۹
@ّFarsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/454301" target="_blank">📅 23:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454300">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e029fa1916.mp4?token=sHYn-WTwtAH3PAAkmWD3LuMqHHmnBrDoDsOAC43zlDRGcWfLeoCs7OijqsUnhudantLlg_0Qtbx88Vcb1-IDkaGQLfmp3Fm1BQoUh5VjrENF2RBEzeO48rl09fCqND5xVWiSlkuWdxZ4Hx0DU0ceEkVjFe-kkDXm9AaW2rF3n0BWxU_LBGmhA92U5D7oZ3DDggkbbAlryHDh6pAdXfKEEbvjnYndCJunfjhqXIeXEVub9rctsoPnvd2dWzbzCOyI3wTfpDBIXp-WKnLEChIuHO-PUj6ylQ6tfa0-aMq6TkCof85Xb3QrCkgNzqBYDRkRIoffQPJIKuPJZANvMJndug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e029fa1916.mp4?token=sHYn-WTwtAH3PAAkmWD3LuMqHHmnBrDoDsOAC43zlDRGcWfLeoCs7OijqsUnhudantLlg_0Qtbx88Vcb1-IDkaGQLfmp3Fm1BQoUh5VjrENF2RBEzeO48rl09fCqND5xVWiSlkuWdxZ4Hx0DU0ceEkVjFe-kkDXm9AaW2rF3n0BWxU_LBGmhA92U5D7oZ3DDggkbbAlryHDh6pAdXfKEEbvjnYndCJunfjhqXIeXEVub9rctsoPnvd2dWzbzCOyI3wTfpDBIXp-WKnLEChIuHO-PUj6ylQ6tfa0-aMq6TkCof85Xb3QrCkgNzqBYDRkRIoffQPJIKuPJZANvMJndug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کرمانی‌ها شب اربعین هم در خیابان‌ها میدان‌داری کردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/454300" target="_blank">📅 23:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454299">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f36b90c1.mp4?token=NQ7kNlBrx8yKCYR9-ihBHYnZKS7QoLF58b7qlLd7vomfGj-XlxTUFXwPxQWxfr-fo3e1IFH16bF4zATcqaR1-8xDLyyxPgvFfvdUEeVuleL59adQzBgsmB862Jwu1a7YWHkuOBQSGS9L8LF4Rl8bl2pa623DVkaOG2xhoN13deK9lpHkXR737BxmltkqaMcUVI_4kZfYE8NMjpMO9bkncibOEDs9DoarJSzciHAiJtVMog1zk1TTwRFbxxKaNx2LrCKFO0MW9RRy-3wereorrtRwZYw707I2NKKIK-TOgn0GdMzLn9Ds2sfWn5_RGwzqCuC2-sT0efit9NoUw0n6Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f36b90c1.mp4?token=NQ7kNlBrx8yKCYR9-ihBHYnZKS7QoLF58b7qlLd7vomfGj-XlxTUFXwPxQWxfr-fo3e1IFH16bF4zATcqaR1-8xDLyyxPgvFfvdUEeVuleL59adQzBgsmB862Jwu1a7YWHkuOBQSGS9L8LF4Rl8bl2pa623DVkaOG2xhoN13deK9lpHkXR737BxmltkqaMcUVI_4kZfYE8NMjpMO9bkncibOEDs9DoarJSzciHAiJtVMog1zk1TTwRFbxxKaNx2LrCKFO0MW9RRy-3wereorrtRwZYw707I2NKKIK-TOgn0GdMzLn9Ds2sfWn5_RGwzqCuC2-sT0efit9NoUw0n6Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفارش امام رضاست، برا تو آه می‌کشم
🔹
نوحه‌خوانی شب اربعین در حرم مطهر امام رضا(ع).
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454299" target="_blank">📅 23:42 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454298">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a7dc3048.mp4?token=UsaUEyk6gOLfJ_AWXbImnTLK_iDURwTn86pAnX60KFCYjvzckVXrbKBntj_H3ey-EHOQAgOhHE5xpwVOKpBaFqKQEk1cau-420o5aJMmVA-KOs9jqdgFFzqjhnZkUlT6iGCUswNZiTcOz95k_BnrakvTIhnHbQV6EBPALSEkkyONcyXvYnJNKXmUmfhDBI6WNz35u40xri35L8-5bLmRrOCwzdwNrH-S1tFVKu-dzfzGqJ-MJe9R_4r6GwrmiX1BPqQxkYMhEECJPaH7eFHz5wBcNHwlMA38p9S8UJ7UhRvOd6nYq3cA9ShAynXsunYNqOa3QJWgeAnZWaiMY5iR_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a7dc3048.mp4?token=UsaUEyk6gOLfJ_AWXbImnTLK_iDURwTn86pAnX60KFCYjvzckVXrbKBntj_H3ey-EHOQAgOhHE5xpwVOKpBaFqKQEk1cau-420o5aJMmVA-KOs9jqdgFFzqjhnZkUlT6iGCUswNZiTcOz95k_BnrakvTIhnHbQV6EBPALSEkkyONcyXvYnJNKXmUmfhDBI6WNz35u40xri35L8-5bLmRrOCwzdwNrH-S1tFVKu-dzfzGqJ-MJe9R_4r6GwrmiX1BPqQxkYMhEECJPaH7eFHz5wBcNHwlMA38p9S8UJ7UhRvOd6nYq3cA9ShAynXsunYNqOa3QJWgeAnZWaiMY5iR_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روضه‌خوانی حاج منصور ارضی در کربلای معلی
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/454298" target="_blank">📅 23:31 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454297">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی گروه فولاد مبارکه</strong></div>
<div class="tg-text">در مجمع عمومی سالیانه صورت گرفت؛
🎥
تشویق سهامداران فولاد مبارکه؛ اعلام رضایت از عملکرد مثبت در سال پرچالش۱۴۰۴ و روند بازسازی ها
▫️
در مجمع روز گذشته فولاد مبارکه اگر چه سود بیش از ۱۰۰ همتی حاصل شده بود اما سهامداران با اولویت دادن به بازسازی ها تصمیم گرفتند برخلاف رویه سال های اخیر سود کمتری توزیع شود.
▫️
همدلی، همراهی و تشویق های ممتد سهامداران پرشمار در حین ارائه گزارش عملکرد سال گذشته توسط سعید زرندی مدیرعامل گروه فولاد مبارکه از جمله نکات قابل توجه مجمع سالیانه این بنگاه بزرگ اقتصادی و صنعتی کشورمان بود که پشتوانه معنوی خوبی برای مجموعه ای است که سالهاست ستون فولاد را زیر سقف بازار سهام قرار داده است.
#گزارش_ویدیویی
#رضایت_سهامداران
#مجمع_عمومی_عادی_سالیانه
سایت
|
ایتا
|
بله
|
آپارات
|
ویراستی
|</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454297" target="_blank">📅 23:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454296">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxRLUeHEn-DrEDIjI0ccXcfZjGWDgtPSb3LkCmoiy2tY-cfw1hEcGHEd_nDVpajTQ6l0t16NsD6F8-o-E3RsuPOGYtlf-xT9pwtiuFVuDmpffYwzDbr_P41eHycFmdNfApaSHTGjXlqiYnO3G3axNFRF7bSBHGXAkSUckrCWLcBEtSEsXTopjZUDuNuv94PUGWFxV9Ua8Xpt6CXzVjgbYsEUvEUVawhCT-ZdEmkZOhitpbBEVpF5_1a2LleN0UrYiBsFjtJSaR9argatR0F2C4Rc3yjzeZ23FhYQonlvO2S-EtsUBLlzoFIfB34JK1Yt1J4kvEIS1OCdwFSbG3e4uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش بلیط اربعین در مستربلیط از ۵۴ هزار مورد گذشت
داده‌های مستربلیط نشان می‌دهد بازار سفرهای اربعین پیش از آغاز موج اصلی اعزام زائران رونق گرفته است؛ به‌طوری که تاکنون ۵۴ هزار و ۲۰۲ بلیط به فروش رسیده و اتوبوس همچنان بیشترین سهم را از سفرهای اربعین به خود اختصاص داده است.
جزئیات خبر</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454296" target="_blank">📅 23:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454294">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/987517445f.mp4?token=cMvme8KvRWpev74iLBGsK4rWK-ezuYOXtyCWWC_wbee90ZEyGB1kP4dgWY4X7rDA6EEk2DvtNboti_IrABGORCNFsC_fWpmWVFXcr5ZD9U6QVDdLCJgNsK-1lb1bd91CAvKzSTmUQUjBCFivtMKXH3H826MC8lfDsG7vOJf_XI4RIJnfj4SVn9JcfbpliEXLqt0NBBInB6lxjXnw4AU4tYtj0kS9iR3Om9LO81w6Fz7KAYLAA8C5aIx8r2Wbq1qD1UpyYIj5glRRph6c3KP_-Uv6pw8b9vjxOB7YHR5o9kNWJLK5zQcPS6yofNrGpn7UGKHzqYGisXNs1BUbNkte0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/987517445f.mp4?token=cMvme8KvRWpev74iLBGsK4rWK-ezuYOXtyCWWC_wbee90ZEyGB1kP4dgWY4X7rDA6EEk2DvtNboti_IrABGORCNFsC_fWpmWVFXcr5ZD9U6QVDdLCJgNsK-1lb1bd91CAvKzSTmUQUjBCFivtMKXH3H826MC8lfDsG7vOJf_XI4RIJnfj4SVn9JcfbpliEXLqt0NBBInB6lxjXnw4AU4tYtj0kS9iR3Om9LO81w6Fz7KAYLAA8C5aIx8r2Wbq1qD1UpyYIj5glRRph6c3KP_-Uv6pw8b9vjxOB7YHR5o9kNWJLK5zQcPS6yofNrGpn7UGKHzqYGisXNs1BUbNkte0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جان مرشایمر: ایران برندۀ جنگ شده اما ترامپ از پذیرش این واقعیت سر باز می‌زند و در وضعیت فاجعه‌باری گرفتار شده؛ او هیچ راهبرد نظامی معقولی ندارد و فاقد هرگونه دکترین پیروزی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454294" target="_blank">📅 23:23 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454289">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aCor690PTxCqfKZBN04H9tPCfEzasAR8vupUzfViOhe7-ekcyLjwLGBwAsBMm-Gf7YWfoq2u3svBJ8ukc1gG7XXhLIMX2jOEkSgXw_QPTkWR0v0_PEH_yXUYhAe8Qi5yejXSMc-kx9NFVzlyCtBTZUcQVabaOglHkt08qapiEqqXGlK-1I5vhJG0G7bcEpdZOylPx2-yS7Tje0dARu-7b6cT1dZJuXrFYPRQtgmoI5-hIPjm0XdVQphC-u0w4eliq3iH2RuYlBCp3pmX8_HKNwPZiYU2UENE7aUiBN99IVN2Ns4f101l63X15I9nHrBmproB66GyRY_WWwPG8UDSGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spyt3wofUUJtJiJSZFXoBx4BJjXz0E9EMnAm6g_Ditt_RJstD2upMgqdSiErRU3rp2ZEHfvL3I10lWXLEFteW3If32Dh1VM0PUtiVN3V6iSOpjGK--CvqSvhte9AlTCWaLonXx0KltEta6wXR807YA1InfD6ZIethCPvTVbHA4phy7_7FuVLlnlQ15Afr4aMpjw9nMIF1G4qIHpkK9NIBWwb0D1jUM8PnvguXFnO9ZG7hIPC8dL4SHSShvh4YpTl_SrjCsoSDB9ogNw0E24L19nn2Riztm9Mp-ixYyDnpsByE3seHKOYOwBBpJyJa1pGThd1Jbvt4w_jKeJj0oA_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SvI7kgAwbN3wTNfQBqKS5Wlb5UicISaJFx2zMX96pCYwTyCWEwTqGWqyDzCR02pxB7vG5v4iwxdG3T_lGROKJaogYRqaMY2hHq206M_dvD3J4gLZbn5LrwQsR-9mj060SpEe5mvBSlG7igPRfw1ba-aNn3SOpYodIVC4xR9W6Zlg0r_xrvuLf_e0eBDWFJaHtLHBm92D4vQ0Lyg71bTCMKlhevv7QTDVfwxRp7hwEnxqlP-5ARuGPjYaiccOtf4-3S6F2lWk0tJrZMqTotpJY0yK63yf4UITqUbAnBoDUSL6xEOoSUzuLEyYGs-BhjqsxNmmwb3V3xWl6IRtKKNcGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UmkVDX8YYp26ik8Pe8FvURDTPUKPJudDI7q-ebX94qcPdZ9pquYyzg84-yJFZG4tkSHtCQcEIGfZwvI5k-CBsrA63VzdIm6dtAJZ2J7qb1jRPG0cqCR13HUm0Sp2iEp1JDc9EPw04QNrOeMQT_xLq_X_ZCh-vCIMfjG8uJHgSEG_Ard7R6kl6oAk_-s_zEPK1il-0zav426kVsAR3zJ_TxKTEMT_apHUwjmroTkVNUYo7YMeZV3qfnE3C6SG7H5D-rD3jKmTI6-YwyTQyBBOL4AKXm2zR1hZEOyuCRSyvH8tH-yxZRR3iVcZ7cj_yGbDeR32clrtaT3e_7Q8buGjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsF4D5sxs2m31m9KnBIUP-Is9s06H6Ip6N2fUrSSX7eaaTAGvucZUCvSDSVz7RQLJTzFoTJ98vMYI4Jg39NBZoU_aJVdeDBoVyTG7VkS94lYi-vhOwccoyjNR0s5PPJjbgOL9X9kKOrCpaibyiB0AamP5swYkzRkvQUtB7Cbj_VvSgBlwr9KgG0sQdVq4uQceYSVkFRBPu3rvIzrOjyEoZSz3riGFZei8o8uVtocpe7q-c4QUvq9O6XHNfdc_nGpevc77S3d_nfjMf7TYeMfu6VWc3kiMSyyfJFLaTcVasBhiY237kVJ3TIkbvTlrNa896QXSbAhWqzH9D79w2zfLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اهالی خراسان‌شمالی در موکب خود به زائرین خدمت می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454289" target="_blank">📅 23:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454288">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/768146331d.mp4?token=DC_o-X60DuHXq99aBKLmGMuhTN6wB4oap6lDMsB7qbIqsplAJ45_L9Nv-t9VAqvPXTKmfCuJnCMG4Zy4i1KfGqvc5_Q6SBI4VC6EBJBfSz0IIpaiQTKqzzmA6J0ARVaZxkkwkz0OcX1TvavQZpqYo1-TOzoEiCsx8VCyXNsikWL0N0VkbEBlnHW18s4N3y5XAFukVR5wcC10NLt4VCqPT477sOT-mKVD0gCeKBod0eLgI5W7Zxdy5MozhW0x1hxZgdVFJS1TykA1Nm0cnJ9E4sic96E32og49T-RHAOzg4Eo31ADiINNVzue6UbPVseJRohw_lDoUMe3KJhQUj8hnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/768146331d.mp4?token=DC_o-X60DuHXq99aBKLmGMuhTN6wB4oap6lDMsB7qbIqsplAJ45_L9Nv-t9VAqvPXTKmfCuJnCMG4Zy4i1KfGqvc5_Q6SBI4VC6EBJBfSz0IIpaiQTKqzzmA6J0ARVaZxkkwkz0OcX1TvavQZpqYo1-TOzoEiCsx8VCyXNsikWL0N0VkbEBlnHW18s4N3y5XAFukVR5wcC10NLt4VCqPT477sOT-mKVD0gCeKBod0eLgI5W7Zxdy5MozhW0x1hxZgdVFJS1TykA1Nm0cnJ9E4sic96E32og49T-RHAOzg4Eo31ADiINNVzue6UbPVseJRohw_lDoUMe3KJhQUj8hnDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشق اربعینی گنابادی‌ها در میدان دفاع از میهن
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/454288" target="_blank">📅 23:12 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454287">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6233b98d41.mp4?token=V_ewCbjNBVRtUeJdAiTF8n6c3p_n_KPQSpgkwXa7DGvL8ONcP0JJsIRjtzzUxbfQPOhx4rtkUSQTSzbes1sw_eZIy7VCjuRSjmMxhhvRT7BxEa7P8QJ_mhrMwHDYo5MzETpF9VK2LeQ296sF7xlGGRsGxNCVIYfiRlch65w6vri-fudFsQb4KVPl973-Yq7UTI5U-YnkYXnAaOXvZfzcsu5EAp-k2Rd9t8J33i6fvwDPmyX3Azs_gMlPezwH_SgabwWq_xqUStuDYsVDO2ZT8-dA1CVWkbPlPdxQNUeZ1D6CWYbapr7b-R_ij3wVM1ohj6mNV8S8rns-O8dNQuMXFTL-WrFhLbgEDf3uRhEmJogattmHaDZq0NRnclvZWSwDhrMlTfR_JzQ-t6mGucqPACB7RfysTb0mZt9Vtc6EmHnrJke7_xWuJPww0OQbhFJa9Cqqq0TVbfaIt5ivci3UeA6LTtOR-n6ctFp5Bv3iMWwhhmaMCb2euy-o9zsjlNs4NVVUFxmpnfpvKfjFZHZzQhH-0XKHlDxUGHh2nGwEliWMNO1-fhKr1EZXekWuRymOxWDGUx6hoQZ60nmJ3s3ZA24pRKPGOzuHy35GbZimb9fLq3v6r6MiQzm06g7381rz-BO74d6LXarlgAuLlH6L2eYKqIlmTay0Z51lS0JT_JM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6233b98d41.mp4?token=V_ewCbjNBVRtUeJdAiTF8n6c3p_n_KPQSpgkwXa7DGvL8ONcP0JJsIRjtzzUxbfQPOhx4rtkUSQTSzbes1sw_eZIy7VCjuRSjmMxhhvRT7BxEa7P8QJ_mhrMwHDYo5MzETpF9VK2LeQ296sF7xlGGRsGxNCVIYfiRlch65w6vri-fudFsQb4KVPl973-Yq7UTI5U-YnkYXnAaOXvZfzcsu5EAp-k2Rd9t8J33i6fvwDPmyX3Azs_gMlPezwH_SgabwWq_xqUStuDYsVDO2ZT8-dA1CVWkbPlPdxQNUeZ1D6CWYbapr7b-R_ij3wVM1ohj6mNV8S8rns-O8dNQuMXFTL-WrFhLbgEDf3uRhEmJogattmHaDZq0NRnclvZWSwDhrMlTfR_JzQ-t6mGucqPACB7RfysTb0mZt9Vtc6EmHnrJke7_xWuJPww0OQbhFJa9Cqqq0TVbfaIt5ivci3UeA6LTtOR-n6ctFp5Bv3iMWwhhmaMCb2euy-o9zsjlNs4NVVUFxmpnfpvKfjFZHZzQhH-0XKHlDxUGHh2nGwEliWMNO1-fhKr1EZXekWuRymOxWDGUx6hoQZ60nmJ3s3ZA24pRKPGOzuHy35GbZimb9fLq3v6r6MiQzm06g7381rz-BO74d6LXarlgAuLlH6L2eYKqIlmTay0Z51lS0JT_JM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع جاماندگان اربعین جزیرۀ هرمز در شب ۱۵۶ ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/454287" target="_blank">📅 23:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454286">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27205720f3.mp4?token=jSpeXg_92UDVeGHIIfXeI8I67x8Q7xP1X8gRW68tYvoUytWclqwwW5R8i3tsVnjfzuAn_9FZE83fpRzSz-QX4k9LSQQbcsIxJFA4vkR3uK5h5IRSXRTGTwn52rnPA3M3MJDG3HEsbtwn8zQTA-L5n7TaLKC0sGzSDbbxeDIrO15NRowXmMnID2HJ-nXwSPCqOugUCfsiOyIl4sOJMp6OHaRjytbuQ6TEYZTDwl0vdU3MWO1TYYYYDZTTktzDxVJZ5_2U5ZB3ksb6QjBY_b8ZNETaesPaETvDqHw3Y7l5Ded_8xpivz-Wy9BU0AUk8szuqOxhw2mK2HD5iP39xuFOCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27205720f3.mp4?token=jSpeXg_92UDVeGHIIfXeI8I67x8Q7xP1X8gRW68tYvoUytWclqwwW5R8i3tsVnjfzuAn_9FZE83fpRzSz-QX4k9LSQQbcsIxJFA4vkR3uK5h5IRSXRTGTwn52rnPA3M3MJDG3HEsbtwn8zQTA-L5n7TaLKC0sGzSDbbxeDIrO15NRowXmMnID2HJ-nXwSPCqOugUCfsiOyIl4sOJMp6OHaRjytbuQ6TEYZTDwl0vdU3MWO1TYYYYDZTTktzDxVJZ5_2U5ZB3ksb6QjBY_b8ZNETaesPaETvDqHw3Y7l5Ded_8xpivz-Wy9BU0AUk8szuqOxhw2mK2HD5iP39xuFOCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اجتماع حماسی مردم گرگان در شب اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454286" target="_blank">📅 23:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454285">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950dbc2faf.mp4?token=lAagJPakXjnWFMI8_TuVOn-bRFFZ4bz3CGu-7TVVK8QwUgcc1JF0hgK_KW35ErkpnLbXYPHteUgOoa3RMVQqPIaWgPU3J1BCccLjeX5mV1o2hEnoKjMI7UUwfNnM9sysDq-30pJ0xp3sy7bM1vC3wufKUVx86cDHHbBb3P1kvWQsI4r6mWix9TvM2rcVV_yLxaM8nC-_NUFbCOoJgJKmUp6TZ9Sc0UDiDvdaOYNpIQnrko5_7MweHuWr3pIWy2VbB7o3HJR_6ZLE3--b28rE8CvQv8dcH9iUt5gb2C1ndZM8JZaE20_WpbJ9sXFtbzS5WyjoqX_c71nfp6nYLQtswA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950dbc2faf.mp4?token=lAagJPakXjnWFMI8_TuVOn-bRFFZ4bz3CGu-7TVVK8QwUgcc1JF0hgK_KW35ErkpnLbXYPHteUgOoa3RMVQqPIaWgPU3J1BCccLjeX5mV1o2hEnoKjMI7UUwfNnM9sysDq-30pJ0xp3sy7bM1vC3wufKUVx86cDHHbBb3P1kvWQsI4r6mWix9TvM2rcVV_yLxaM8nC-_NUFbCOoJgJKmUp6TZ9Sc0UDiDvdaOYNpIQnrko5_7MweHuWr3pIWy2VbB7o3HJR_6ZLE3--b28rE8CvQv8dcH9iUt5gb2C1ndZM8JZaE20_WpbJ9sXFtbzS5WyjoqX_c71nfp6nYLQtswA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی وارد نجف شد  @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/454285" target="_blank">📅 22:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454284">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec765ed50c.mp4?token=JaQRfo1pLlEZUXyN1FmGrrAoF0XG0DhXrfgH7NbnWNCpeGYKpFExrG68IPiBF0H1XvKiacZJCRx7Gi5CF3yutgf4y9mI8rkyT9LcnklnOl1Wn6B6WQfBhKxYFbsjN-3U219ks2-RgBQRLDyLCdbVE-aKvi8V5YZR6fC3o5VDilE32YlAAovICinzJqkfyjSL4Z-Nrs_XC2IS8Hg22db56VGJJqHc5p5AoeAPt0_YpQPRtx23-yK3N8m5VrfTtqN4buoEQ-V_JH37827V60uAvCqw1O_sor7ezN9mDHF1Y64dOcPFDRuxCAW3zvAdIXtTJMjjK9nba4JBdqk59yDKSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec765ed50c.mp4?token=JaQRfo1pLlEZUXyN1FmGrrAoF0XG0DhXrfgH7NbnWNCpeGYKpFExrG68IPiBF0H1XvKiacZJCRx7Gi5CF3yutgf4y9mI8rkyT9LcnklnOl1Wn6B6WQfBhKxYFbsjN-3U219ks2-RgBQRLDyLCdbVE-aKvi8V5YZR6fC3o5VDilE32YlAAovICinzJqkfyjSL4Z-Nrs_XC2IS8Hg22db56VGJJqHc5p5AoeAPt0_YpQPRtx23-yK3N8m5VrfTtqN4buoEQ-V_JH37827V60uAvCqw1O_sor7ezN9mDHF1Y64dOcPFDRuxCAW3zvAdIXtTJMjjK9nba4JBdqk59yDKSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: دست‌وپازدن ترامپ ممکن است جرقۀ آغاز جنگ جهانی سوم را بزند
🔹
خلیج فارس و تنگۀ هرمز چاشنی بسیار خطرناکی برای جنگ جهانی سوم است. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454284" target="_blank">📅 22:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454283">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6307a090.mp4?token=p1xwxrg07STUp_TFz4vJgA7-ypHk2Otpfss8BiKZ5T-dQqX-7EUfnUJWq5gWGpN0fvxnTDsn7dXzhzV88iC9F6dMN00mCZrlT9k_3G0R9B19wssxYFtAw9O-uYvO41aJp3wA_vPXXWNQnwKGgwkHeFaNPerxOW3Ng8clViVpf2py7DpmPvk57LOcPF2eyfobF5aSGsTzzdijdl3LAg9LRgUtBQtQ8yX-qH4MUKBk8pmQ6sgKJJcEX7iZtqUVAT1tVLJDohzcJ65cxAYoSCw3r8j4zF9udBa5jxOygA-LvqFj6C8ERHoq4yHME6jqhQwx5GmcNCjYwf5-3FBxXoCfnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6307a090.mp4?token=p1xwxrg07STUp_TFz4vJgA7-ypHk2Otpfss8BiKZ5T-dQqX-7EUfnUJWq5gWGpN0fvxnTDsn7dXzhzV88iC9F6dMN00mCZrlT9k_3G0R9B19wssxYFtAw9O-uYvO41aJp3wA_vPXXWNQnwKGgwkHeFaNPerxOW3Ng8clViVpf2py7DpmPvk57LOcPF2eyfobF5aSGsTzzdijdl3LAg9LRgUtBQtQ8yX-qH4MUKBk8pmQ6sgKJJcEX7iZtqUVAT1tVLJDohzcJ65cxAYoSCw3r8j4zF9udBa5jxOygA-LvqFj6C8ERHoq4yHME6jqhQwx5GmcNCjYwf5-3FBxXoCfnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: به‌هیچ‌وجه اجازۀ بازشدن کریدور دوم را در تنگۀ هرمز نمی‌دهیم
🔹
اگر ناو و نیروی نظامی هم به تنگۀ هرمز بیاورند آن‌ها را هدف قرار می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/454283" target="_blank">📅 22:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454282">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b215ef3f7.mp4?token=chS0uC5WkKdKy6X6hLy_LJsfMdU2w3nuOMwsOQAl592flYHyMRhU4dTo0ge5RwKFJXk-OK7j6KtDeouHkrajtKOuaHB3YdAwpxDdOHji0B4NwzV-BE03AjXZNETONokMgTM_JGKpxllvLaMbT0SK5hbO66lxf0oyUeHjG-DfrSTKd5lIV5Kz_5c4VHZvb9sKsiRajIjPes-NIRV9swxgULohEx28V1r-dk2_F71tQJUMHnalKrLvAqUY_qv5Gj3OFJLVzl093FAAE2EO4gN_vwkkVdifBbBZIsmofXuc_O6rEmolxBsj1x1kZAa7PL8Ito8iYzzbgkl_rASiDHRLLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b215ef3f7.mp4?token=chS0uC5WkKdKy6X6hLy_LJsfMdU2w3nuOMwsOQAl592flYHyMRhU4dTo0ge5RwKFJXk-OK7j6KtDeouHkrajtKOuaHB3YdAwpxDdOHji0B4NwzV-BE03AjXZNETONokMgTM_JGKpxllvLaMbT0SK5hbO66lxf0oyUeHjG-DfrSTKd5lIV5Kz_5c4VHZvb9sKsiRajIjPes-NIRV9swxgULohEx28V1r-dk2_F71tQJUMHnalKrLvAqUY_qv5Gj3OFJLVzl093FAAE2EO4gN_vwkkVdifBbBZIsmofXuc_O6rEmolxBsj1x1kZAa7PL8Ito8iYzzbgkl_rASiDHRLLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: بعد از این‌که آمریکا حملات را متوقف کرد ۲ روز دیگر به حملات خودمان ادامه دادیم تا حساب کار دستشان بیاید  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/454282" target="_blank">📅 22:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454281">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e260f8ebc.mp4?token=Bvxo8mNPdbJWu3W11no_vZYPcIr5BE0L2zCkXA-y5igzJl6CY9g_igRqGkWLveuhoDNljnAHtlOQKdzTkxkoUcM_0O7lvdltAnNjOK-La06vPTTixphfENJseIFAm-aiTfZwLvQK5OIwCVlm2OleyLUGbL9tW80ubV00I5czIVpTxBU3Ay3aNL3qn2rJCmdN55bq80OYCI-8dkCZBOFAX77XQPo__iBU91EdJxZvIX35NEPwZyJxKF5WdsTalkPp5hvftJqpSokLFHYKde_ivzj4wY40GydH2X6jTPuWbSjs3v7X691PxMfzulS2iLi5W4fqKHMIuOe6jz7J-KbOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e260f8ebc.mp4?token=Bvxo8mNPdbJWu3W11no_vZYPcIr5BE0L2zCkXA-y5igzJl6CY9g_igRqGkWLveuhoDNljnAHtlOQKdzTkxkoUcM_0O7lvdltAnNjOK-La06vPTTixphfENJseIFAm-aiTfZwLvQK5OIwCVlm2OleyLUGbL9tW80ubV00I5czIVpTxBU3Ay3aNL3qn2rJCmdN55bq80OYCI-8dkCZBOFAX77XQPo__iBU91EdJxZvIX35NEPwZyJxKF5WdsTalkPp5hvftJqpSokLFHYKde_ivzj4wY40GydH2X6jTPuWbSjs3v7X691PxMfzulS2iLi5W4fqKHMIuOe6jz7J-KbOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: با حملات ایران فرماندهی سنتکام در خاورمیانه ابتدا از قطر به اردن رفت و بعد از حملات دقیق ما به اردن، به سرزمین‌های اشغالی منتقل شد
🔹
حملات ما کاری کرد که مواضع آمریکا در کویت به خرابه تبدیل شد و در اربیل بسیاری از نیروهای آمریکایی تخلیه شدند.…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/454281" target="_blank">📅 22:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454280">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c317899793.mp4?token=mEUYqE5Ha8A2Xv6WGiFPqy9spvMswRMXCO38yaN2W3em0IGE9h_eCITdKy1fRRqYLcJAEUTeUbhTcKN_6edlCeGgmAdCPTB5dAzLO45c-webrlyWYdujwuZHJF8cbJd6HEG_NvlERi_me6w45UqZs0HCWgtqX1MipZ9SekbwVFRsArHfEEW0PqlqUyABCuk1qtM0u3CJMzT6j6WNxAKGUCkGgpLAI4r2eAg9upWFCHtCOoN0MMCkm5JptdRdOyork-3eiL3lm-bCy05TTH3zP46yGwKdxQsjMosCNdxwOeJ5fy5OvMagVtD2VnwAJyjyZaO1hrbzL22Irrxa1CAoTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c317899793.mp4?token=mEUYqE5Ha8A2Xv6WGiFPqy9spvMswRMXCO38yaN2W3em0IGE9h_eCITdKy1fRRqYLcJAEUTeUbhTcKN_6edlCeGgmAdCPTB5dAzLO45c-webrlyWYdujwuZHJF8cbJd6HEG_NvlERi_me6w45UqZs0HCWgtqX1MipZ9SekbwVFRsArHfEEW0PqlqUyABCuk1qtM0u3CJMzT6j6WNxAKGUCkGgpLAI4r2eAg9upWFCHtCOoN0MMCkm5JptdRdOyork-3eiL3lm-bCy05TTH3zP46yGwKdxQsjMosCNdxwOeJ5fy5OvMagVtD2VnwAJyjyZaO1hrbzL22Irrxa1CAoTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: با حملات ایران فرماندهی سنتکام در خاورمیانه ابتدا از قطر به اردن رفت و بعد از حملات دقیق ما به اردن، به سرزمین‌های اشغالی منتقل شد
🔹
حملات ما کاری کرد که مواضع آمریکا در کویت به خرابه تبدیل شد و در اربیل بسیاری از نیروهای آمریکایی تخلیه شدند.…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/454280" target="_blank">📅 22:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454279">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88dd872897.mp4?token=eWSiX_zz3FV9oHsGtG99syD4Vqs1H0rHTf-3ZNWOpuvezYmD9ia9WXFkdL3rL9oI4jZPYo86S7_sPuPwlJBDC2aSHGF4tLfVOfJEqY9OnjRyvl--ng6GIkGXSIfU5d57TjZ1C9bR2-JcIhfLXRLAO9AyA93-Tuy_wN6oVF_Tqal7xt5FHGPpp_UuJnZ1DRvVPGOl3EQLE_aqlWY-ECcO5_zdMJIjZisaEkGTBxAnXt-th34Uc8e-C65-j90Phg37w0W0k1_tAaoKgagmOW8PH8uJd_jDEaveg4iqS4GKHnV3kZrTQNLr1LQrsDyZ9MHO_QTgrIHdWW9jvfB1A9NIvWKxcT5T9mD5DZjzeg1x_R7XF0H0kCjnlbnbmrcvqZ7gUn5M__zaaNzBDJge-vFaXGcofHUY-eK44Bc9i0JF4MT1Y0ogUasa4ALfzygTo6nR5NcaTMf0oYyk-tHbT2Gn5I0FW4Oa91nAhTFonh5kv8x9flkKPWg4KrDjjVPUXCZa921n4heWT5btNM3m1S2e3qpINnD4yfiVGfWWDzDc7U5pULk8phL9B5s5XFrq3IwcXQyy7PD3fp03WjJRBRBsPapHMEUtNLwvA9eT4eh4jLufkp0KGoeADcrHymvBhtSRP9p94TQXystNk1rme65lCQD7u4EItG0W0L6OYi3M69o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88dd872897.mp4?token=eWSiX_zz3FV9oHsGtG99syD4Vqs1H0rHTf-3ZNWOpuvezYmD9ia9WXFkdL3rL9oI4jZPYo86S7_sPuPwlJBDC2aSHGF4tLfVOfJEqY9OnjRyvl--ng6GIkGXSIfU5d57TjZ1C9bR2-JcIhfLXRLAO9AyA93-Tuy_wN6oVF_Tqal7xt5FHGPpp_UuJnZ1DRvVPGOl3EQLE_aqlWY-ECcO5_zdMJIjZisaEkGTBxAnXt-th34Uc8e-C65-j90Phg37w0W0k1_tAaoKgagmOW8PH8uJd_jDEaveg4iqS4GKHnV3kZrTQNLr1LQrsDyZ9MHO_QTgrIHdWW9jvfB1A9NIvWKxcT5T9mD5DZjzeg1x_R7XF0H0kCjnlbnbmrcvqZ7gUn5M__zaaNzBDJge-vFaXGcofHUY-eK44Bc9i0JF4MT1Y0ogUasa4ALfzygTo6nR5NcaTMf0oYyk-tHbT2Gn5I0FW4Oa91nAhTFonh5kv8x9flkKPWg4KrDjjVPUXCZa921n4heWT5btNM3m1S2e3qpINnD4yfiVGfWWDzDc7U5pULk8phL9B5s5XFrq3IwcXQyy7PD3fp03WjJRBRBsPapHMEUtNLwvA9eT4eh4jLufkp0KGoeADcrHymvBhtSRP9p94TQXystNk1rme65lCQD7u4EItG0W0L6OYi3M69o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: آماده بودیم به ۳ منطقه از اوکراین حمله کنیم اما بعد از اینکه گفتند اشتباهی حمله کردیم، پاسخ را متوقف کردیم تا ادعای آن‌ها را بررسی کنیم
🔹
آن‌ها  در هر صورت باید مابه‌ازای حمله‌شان را بپردازند.  @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/454279" target="_blank">📅 22:30 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454278">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039faea8ea.mp4?token=QHeNhL0hj80vUNUrOZ2z1VRY1TL9P1--JVP9NQOE6_dZsJttSzrsWJCXiEuLTKD2M3-51A_VraPoWxfyIle4WWj0MhznmAGQ1WVBf4OY2VcID0dt4T10CbJ7vT8OGtTMcy__g2SUuzuYLKt-MLG66QQI3mFMWSdVXtkpoOBBryFwJ7Ts1ks5PtFccQB4gWiSNXut0SH0JqNy95yBK1wK0-e7q3g8AVYUnZ0F-WU6qhewXwqOjRf8xwkDdSG7SzrHi7ktlJ_RoCT_oS-uBk60x6T3mB675X9Tvuq_4Mh0TxhsAkm3cQXr2l1gHqC_RsfOMpFuP6S-7aynh3qyO-17Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039faea8ea.mp4?token=QHeNhL0hj80vUNUrOZ2z1VRY1TL9P1--JVP9NQOE6_dZsJttSzrsWJCXiEuLTKD2M3-51A_VraPoWxfyIle4WWj0MhznmAGQ1WVBf4OY2VcID0dt4T10CbJ7vT8OGtTMcy__g2SUuzuYLKt-MLG66QQI3mFMWSdVXtkpoOBBryFwJ7Ts1ks5PtFccQB4gWiSNXut0SH0JqNy95yBK1wK0-e7q3g8AVYUnZ0F-WU6qhewXwqOjRf8xwkDdSG7SzrHi7ktlJ_RoCT_oS-uBk60x6T3mB675X9Tvuq_4Mh0TxhsAkm3cQXr2l1gHqC_RsfOMpFuP6S-7aynh3qyO-17Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: آمریکا پل‌های منتهی به هرمزگان را زد تا یک اقدام زمینی علیه ما انجام دهد
🔹
طرح ناپختۀ فرمانده‌های ارتش آمریکا باعث شد حملۀ زمینی و هوایی متوقف شود. @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/454278" target="_blank">📅 22:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454277">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c98a052b1.mp4?token=FK5hzKvl_42jK7DGz2E_ZBo7ZPcz0X01KZxM9DeAt0gGFpEbKkLvoHRAALbaZrojYjTH6pwwIV4PTmol8w7KdxLAt0SkjxI6OMkmwg6YmBrv10yjwNlZUciniAALg8PCP6D6QflvQ5K_EwDKuXdDn-k47o0tDwYj_ms-F9BhLhACcM8bFo34C5SYGU-RkxL9SUndyGjr-WZvNHLOfZvCRlqAKYRGQD6gzV-hlguQg-opeGhzz1wo07nRkKT7Og619epCpz4IvlsKYzbls61F1od9CRnuT4tzg_W2IBlWtCoRWrnHz8S7AiIQueuUCPRqm1vEGd-ogcPUC94ofuLnzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c98a052b1.mp4?token=FK5hzKvl_42jK7DGz2E_ZBo7ZPcz0X01KZxM9DeAt0gGFpEbKkLvoHRAALbaZrojYjTH6pwwIV4PTmol8w7KdxLAt0SkjxI6OMkmwg6YmBrv10yjwNlZUciniAALg8PCP6D6QflvQ5K_EwDKuXdDn-k47o0tDwYj_ms-F9BhLhACcM8bFo34C5SYGU-RkxL9SUndyGjr-WZvNHLOfZvCRlqAKYRGQD6gzV-hlguQg-opeGhzz1wo07nRkKT7Og619epCpz4IvlsKYzbls61F1od9CRnuT4tzg_W2IBlWtCoRWrnHz8S7AiIQueuUCPRqm1vEGd-ogcPUC94ofuLnzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: آمریکا پل‌های منتهی به هرمزگان را زد تا یک اقدام زمینی علیه ما انجام دهد
🔹
طرح ناپختۀ فرمانده‌های ارتش آمریکا باعث شد حملۀ زمینی و هوایی متوقف شود.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/454277" target="_blank">📅 22:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454276">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28a5e6e348.mp4?token=gL-9wcyqSQQdvkAAjJptLRgOr5jj-zGEkBI-bK_zaoxzczOZgm9LcLF3OYtF5qZKts4ouEOgd79B6EICJFn1B16b6PV07_PSbGFzPS-TUoWPvx9Z0l_6VUYSHGTFvexbdKWGA5D9A7tpdCgUe-o8gVFOL7OcPQGVP15VSMJW28XaQRPCgE8L9jRA408RVhOhYygZ-Ox0LfJktF89Ir-Rr36CovKEoED1H-j2JXgvaW5mIA1vUMIxp2eVTQhjzPKinNy3DKu95duqCREnPnhu-sS_qgIFYI6I15PhodOo12Cx3b06fyKr8O_cV25yacEq24n88vvvCxyn46op119c7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28a5e6e348.mp4?token=gL-9wcyqSQQdvkAAjJptLRgOr5jj-zGEkBI-bK_zaoxzczOZgm9LcLF3OYtF5qZKts4ouEOgd79B6EICJFn1B16b6PV07_PSbGFzPS-TUoWPvx9Z0l_6VUYSHGTFvexbdKWGA5D9A7tpdCgUe-o8gVFOL7OcPQGVP15VSMJW28XaQRPCgE8L9jRA408RVhOhYygZ-Ox0LfJktF89Ir-Rr36CovKEoED1H-j2JXgvaW5mIA1vUMIxp2eVTQhjzPKinNy3DKu95duqCREnPnhu-sS_qgIFYI6I15PhodOo12Cx3b06fyKr8O_cV25yacEq24n88vvvCxyn46op119c7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگهٔ هرمز در کنترل آمریکاست</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/454276" target="_blank">📅 22:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454275">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bac9fbb15.mp4?token=Nq992CdRndTXDDB3Q9pDvSZrKrzj-NCSQk6Hy4llqbL_A5uwuG6Dev1Ccw_FOboevqhvh6BKDnrYsyf2XpyhyMLQLiNfAek9IbtitGUXUyKtFUP06wfszum7pIpXJuR7J9b0x9myiR9eaK6VFOW446WC_VgDY6yOfMf2fZd9S-8QtbM2oUI325WDya6xnoQmkwTiomBJCJCfg0_aJ8XvBWIgT3-ykcfSYzAbrM-ZMR2UExIdVXktvXb01t7zr732usJQJUjV-7my1RCmNfClxjmjJoLuyw1bQnSo--rRYaHvHlPIjCwYxmYks9TfzRgeoZ121yH83p0UiXgkSHY5gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bac9fbb15.mp4?token=Nq992CdRndTXDDB3Q9pDvSZrKrzj-NCSQk6Hy4llqbL_A5uwuG6Dev1Ccw_FOboevqhvh6BKDnrYsyf2XpyhyMLQLiNfAek9IbtitGUXUyKtFUP06wfszum7pIpXJuR7J9b0x9myiR9eaK6VFOW446WC_VgDY6yOfMf2fZd9S-8QtbM2oUI325WDya6xnoQmkwTiomBJCJCfg0_aJ8XvBWIgT3-ykcfSYzAbrM-ZMR2UExIdVXktvXb01t7zr732usJQJUjV-7my1RCmNfClxjmjJoLuyw1bQnSo--rRYaHvHlPIjCwYxmYks9TfzRgeoZ121yH83p0UiXgkSHY5gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطره‌بازی بغض‌آلود عراقی‌ها از روز تشییع امام شهید در کشورشان
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/454275" target="_blank">📅 21:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454270">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jIwNFIOaK0KqDhtbyCqcHBNnY0UHMX4W1h91K2QFXljyOVWGXbsoUjaGEeAbD00cxahU5oczWhKIpXn-IBI_Nq003WXY6fnza7zZW4rF5tuydVwmQ6tj2doz9-cb94kjs2fN1DbTpIB1z822PSudcPtYTt9iUDnxHZsIWL4O9fTzrPKJ73n6vGe7UGG_aXiwIu7ODBTKYw0QjUvTLNwx9RuygubGprh_xjrb8dvb2hnJzp9Vf_p8PYjinAIU8azzRT9iXdICgb443ZZb2QLJ4LwAipsH9IwGT5FTvqN67MHmfZFaFt5xCRguBxpw1lv1D0gwn1aDcq3LQfQhRkWN8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y5KfGUVanxEGPss-YYg8cB_OTARHj64rCekFeAQoFpxHex82OJD9iLq-cpsY7hreC_j_xsMRps9gjZHBkE7SlzQXP6WV4_DakwjZiQexRLQK0VYD7Pd7_8Z7uIj5kzn6XGhLZE8L7FmnumMGBx6OLkMXRnRFS4dxgmXDYjs0FzWaJCbabqQvAgrJOcYRLCzPltXsmN95Iudsb5MVvtwBdJdIpzHo_8AZy8fj22lLYmxvV-0lqxYbkWcChAs4KS2_pagKbJo28rs5pV6atvRf2mXh2ydLy5x-QF9LQo0GhoKevFiakWXwudak3tO9CE07SZIQtDFEV7_hAAyr2FFKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAEjlUFAh9XGX0BgtrtVYTuNJpg3ZLUBpd8UpZa31mu1xEg4LwnqcJQCFSOzOHPkwBt6BkyJos5SjZOGtAMX-sCVXIBm12uN_zVscoo080BKiyBxOyovvqurAeTygOWCID95VKIAMr6Om-DsOganfMMxywivbCWyZiLSwB9snJKvFYEKSx1BCqKTTXO35CGeafYR9VmE2-r9N2v1Dgis2VRW5WFVJ0FOtS1WKaueHdWTVNjUcG_Z1gan2cqRTJdbiUUyJB78ceUygnRWO9XuIxqcnkv-wMW9Qq1U1RRXA2pYIx0kazcFD9cmr2T8GiXbKT2YCTkl2NXRJIvVdQrc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H0L24nstr2fXXi_XO1R_QIyiKXJU8VZc9HstVgrtyEZkPxmuuRpqDOm1FW5EEzARfLq9I4cXx5W64QbOZpoE7-zpmE0ly-cy7oE8wJ0OhqIaXaqmV8bcj8cv-qAw3CQ30qSXd9pnQ0sSd3FO82T0JmivS6leN0lBO0Ve9V69S0SRRtjXMNADd79NU6xlGwle64k2hf8uBvgwnntPt649uGJFToXcTsoxcsbZZIiqonPXwlbc7Yq0JMZJWZvw8ioo53aeDJZk1z7-Ue9mfUUSs1MCJBqocfF9LrGDiQS5nsnxIjUnSfYKPUEw2MpU4UzpCO7fBczmNQb1CKo2G57aOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LsC154MMlx3Qj7sdjFMt6K68bKliZsAe6FDMyW8399ex5xXfgWgKFZ92w4zjPjtBeYxqeT-qrQmSPgOKX6f5W8BFPme9-FfDNmygPVsom2RU-o7sH8fLzCyP2h0phF1FDCqgiQyLuagb4tPGhQu33pS9cfilw_Qe7FESuz3-CvhGc7zYZ13MKNZCjFMT1wclgjGal9IKSXVTjacrTSMvmrPoUkv3C3NUARUXNvYx0WCtZebOWoYTg0xSvXPK2IdpycrPduojhQCKWtW1jH-NvSc5ZRnSGb4lAPaa0UnvoBY4-eC_x-LBpzdDFjiOF8RxmebkJXvxuDsXAA56lYwRng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
زائران اربعین در حرم حضرت عباس(ع)
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/454270" target="_blank">📅 21:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454269">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPAmvO3jMkDipn2z_JY-QXQmnjx5BUWUKUX8h8lkOrIs0m_A1zM3wfkOdfJ8nTxgSlrH6x17YHtEqXb6E1siYccAoAeiWJkwOBw25TvSqFVeXNTE3It0SoZjuqLcy7LW8W6ffDJPBLMulKsPENas5VWqnhzKsbjhg3BqFuZS9NrS8S5D-7FqqPex5bbXKZt6Jz2PTbr2pnQveTiS4ffc6I6OJNJIeH8ZGkcQCPG_Xy_lsHVNHpZUoSxXj4ajlSySOkMKpJIlScKkSKrF1uKdMI2H2iFJHiy3C0_Z7skWeI2eUyGOyYtnSE-eaxf1-z3STQIgi8_bLUDvv9_iN9ry_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
واکنش ایرانسل به ابهام درباره مصرف اینترنت: دقیقاً به اندازه مصرف ترافیک بین‌الملل از حجم بسته کسر می‌شود
1️⃣
بر اساس مصوبه‌ رگولاتوری، هنگام استفاده از ترافیک بین‌الملل، به ازای مصرف یک گیگابایت، دقیقاً یک گیگابایت از بسته اینترنت کسر می‌شود.
2️⃣
ترافیک داخلی با ۶۳درصد تخفیف محاسبه می‌شود؛ به‌طوری که با یک بسته یک گیگابایتی می‌توان حدود ۲.۷ گیگابایت محتوای داخلی مشاهده کرد.
3️⃣
ترافیک پیام‌رسان‌های داخلی با ۷۵.۲درصد تخفیف محاسبه می‌شوند و با بسته یک گیگابایتی، استفاده از حدود ۴.۰۳ گیگابایت ترافیک امکان‌پذیر است.
👈
جزئیات بیشتر و متن کامل اطلاعیه
@irancellnews1</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/454269" target="_blank">📅 21:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454268">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🎥
گزارش ویدئویی از مراسم امضای تفاهم نامه همکاری بیمه دی و گروه اسنپ
#کانال
اطلاع رسانی شرکت بیمه‌دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/454268" target="_blank">📅 21:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454267">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/454267" target="_blank">📅 21:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-454266">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06725d913.mp4?token=RvVSIrcFTo4tMb1E-dOlDHwC3QWYoSfwbEogD4IMWh1f31FnYXk7BO0MxqeqxExloUxGe4O76C7UBPJXC390qqv3RPayrjW9jCX3uY2CZYd0QUYZsKtx_3oK0SamHPzJX0rw2zGAnCXq9W_kkzIbDiXCkcWTlAHO_C2VBUeJqto7bVBM9zaupug1_XGrzuxa8MJBJbIsGv3-mqTJKIGRH4y3Zj1al7JnpRuqgyLZuIexeC4eIu5R2ET7iYVx7b6-hqRnNypd1I7A_zt_aa6ZVxzyGF1-C36QE6F-vAOEupJimHyHBWWjOG3UW1kcMX3INs3HFpRpRfsSt4nB5Kmk8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06725d913.mp4?token=RvVSIrcFTo4tMb1E-dOlDHwC3QWYoSfwbEogD4IMWh1f31FnYXk7BO0MxqeqxExloUxGe4O76C7UBPJXC390qqv3RPayrjW9jCX3uY2CZYd0QUYZsKtx_3oK0SamHPzJX0rw2zGAnCXq9W_kkzIbDiXCkcWTlAHO_C2VBUeJqto7bVBM9zaupug1_XGrzuxa8MJBJbIsGv3-mqTJKIGRH4y3Zj1al7JnpRuqgyLZuIexeC4eIu5R2ET7iYVx7b6-hqRnNypd1I7A_zt_aa6ZVxzyGF1-C36QE6F-vAOEupJimHyHBWWjOG3UW1kcMX3INs3HFpRpRfsSt4nB5Kmk8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: اجازه نمی‌دهم ایرانی‌ها در تنگهٔ هرمز عوارض بگیرند؛ اگر قرار باشد کسی عوارض بگیرد، آن آمریکا خواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/454266" target="_blank">📅 21:51 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
