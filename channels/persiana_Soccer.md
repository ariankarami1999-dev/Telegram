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
<img src="https://cdn4.telesco.pe/file/ByJo-9dl89Khdp4gk2KH5hMFuiT452PcrZi90zHfIs75IwHbZB6rYJgkT6DzNhuVUQoDv832gkclwpTzaX_cysIlIBR8AIPACTNcGXlJybR-IsGuR3Xe3ti0whTYux6uUjSzM_lIfb5wacgCk1lC7CbfBBSBG1aIXU4iPCbFZg9mwI3QifZAYkNM20cAViU1OOjuFS_VXvdHPPtJ0leyyzOWpPPBNcDr3DCxXfqRpYqcgJPFWZBhRBgnVBgF3RyNVTuOt9jCPuheSRZJeM3isMkzZeklhwwGCjVg5NVQfu2iuTiS-3XFjc08PfKdr-V7Cpv8labVVcMU1yaJz1p-Xg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 245K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 15:50:01</div>
<hr>

<div class="tg-post" id="msg-23439">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOBrNbH-sTkwz6UDrgr7cBaJWiAs1gF-o20xt_Y9I9ha9uo0KFC03iDQFwmiUwgPGjwzpu7eE-qnGQOl8rrflw8ONYm55oRl9QrEFoees-xVA0QMh76NlMBmVr8aCZnHm397Ht8QypZiusfwXwVbuEVA26o76HPOHgrKDqgqMVGSmCgCxAtIuG1CCCFyeiB1-d6qsDXgO3O4IaF2OGrpLkSUwMhMev6TRZsiYrZvNCgTvqIXp4JOyHM3lK0y7Cxk6LSPFJvv4HthBayv6SWvLfAuxqD3up_C_99ocjr0jtNkyF-ld0zLRFohnKJDEGqqoeTM44XWnk1CPYpZ2iiloQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/persiana_Soccer/23439" target="_blank">📅 15:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23438">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AuxwslTgB-n7HFkFnf90Gf-Isc4LPl45EppHHcMlYO5H80l0XDve0kysmem_pw0eubyXUT3CWuEScx9H0_s3SgzRCWIl3G-NdPZ4sy2NrtwPtbaHZDIpdZDyShaOPhTqG8C_su61MbxsPXXVPHQRsXT9z90fkSwQbpWg04ILF0burALy6z9f8BM7yGLKRAnqY080cxvREV5xzWVqIsrEAcALaT3plvmzwiejqPH6gibrUaHkYIC3iyC5EL_LYGNxDOtycaDXnk4wRQlJbyN_rk1gum_3_PWXcNQAo9SNHpUZ4-sW01qlp31UKg5v-P73FqUCYLthPiCxxx2aXjJ4rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر برخی‌ازبازیکنان‌تیم‌ملی‌برزیل؛ جالبه بدونید کارولین لیما با نیمار جورنیور و ادر میلیتائو هم بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/23438" target="_blank">📅 15:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23437">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">▶️
قسمت‌‌‌سوم‌ویژه‌برنامه‌‌فان‌ جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید. شیت و محمد نصرتی مهمونای این قسمت بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/23437" target="_blank">📅 14:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23436">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=c20C6Jxr-RSf0TLnzEI0rN3nX2vTHfbdnaYM47gHo4xLq-D5ERUdj_Z5ftLjNUnnfctSStzklYAAccaLjOvJiOK0Ck_BYDOmloYmv-mvyImMwJwmusEdyEzTNLgzQP4xjFpWvpHTEJtI3UDiVgfDbBzCjtQJRxMWngnlaBD62M7UEHhAOrWyCIP6MwYxc8eh95riKCKDp9GqOj8fgRy5MZsAt1RS8X6PCKIX1nzISAnPZbHhm9VpgNIuICEPBYy8quYXIuJQI4VUgNzUsWSKq22SHO7XJaNqzglpuo88wAGCTNj9v6Ekn1W_Yh1KyTyX8Whu0yMSEDs6Pd2U7VRwmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf1fd42fe.mp4?token=c20C6Jxr-RSf0TLnzEI0rN3nX2vTHfbdnaYM47gHo4xLq-D5ERUdj_Z5ftLjNUnnfctSStzklYAAccaLjOvJiOK0Ck_BYDOmloYmv-mvyImMwJwmusEdyEzTNLgzQP4xjFpWvpHTEJtI3UDiVgfDbBzCjtQJRxMWngnlaBD62M7UEHhAOrWyCIP6MwYxc8eh95riKCKDp9GqOj8fgRy5MZsAt1RS8X6PCKIX1nzISAnPZbHhm9VpgNIuICEPBYy8quYXIuJQI4VUgNzUsWSKq22SHO7XJaNqzglpuo88wAGCTNj9v6Ekn1W_Yh1KyTyX8Whu0yMSEDs6Pd2U7VRwmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
وکیل تتلو گفته‌تتلو واسه‌ماه‌محرم درخواست مرخصی کرده که بیاد داخل هیئت‌ها نوحه بخونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/23436" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23435">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=Gde4QN2ciQhgqruk2pDDu6xCIV3QjiIqzjaU52qb-wgdvea0vutjaTYzBkPX4V9TZoaKcaIEUC91ZwfBtycQEHuCew1ziNUA2gIgOy-3zRsCWu0Fy8VT8YkUBZlzZV5QpVIN5wD-a0qiIEFhIOh-GqRL1EK92bbeyW-UrnsaYAWYceAsqlTsSSkHJlFnjxeG5BPOChCn7bpmZWfaFHbq9aFCnWm8gfMIRng6zdAnb1QpKmrsIC8w01yC0rY34VClsR3blkxYK2xaSUJ1z9cULQs-RForVxJRuPZByo-LMAn2OpoL6rwDA_psWTZ_Y_3Up9NMrps76y6MHg6rCqalqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fddab3a3a.mp4?token=Gde4QN2ciQhgqruk2pDDu6xCIV3QjiIqzjaU52qb-wgdvea0vutjaTYzBkPX4V9TZoaKcaIEUC91ZwfBtycQEHuCew1ziNUA2gIgOy-3zRsCWu0Fy8VT8YkUBZlzZV5QpVIN5wD-a0qiIEFhIOh-GqRL1EK92bbeyW-UrnsaYAWYceAsqlTsSSkHJlFnjxeG5BPOChCn7bpmZWfaFHbq9aFCnWm8gfMIRng6zdAnb1QpKmrsIC8w01yC0rY34VClsR3blkxYK2xaSUJ1z9cULQs-RForVxJRuPZByo-LMAn2OpoL6rwDA_psWTZ_Y_3Up9NMrps76y6MHg6rCqalqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/23435" target="_blank">📅 14:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23434">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNS7skMYVSCUtIDYjhvBMVHJoKESltv0XKr-gP42OzUNNlSeJg1y-1z1_S1nreCGJDrv4-D0VxarCpqAPFY5tiawI4amVhvep0XXAvx17xWkTGFRq_3aipbHDaV_aKlXi2Bey64I6fW9xcUZqGcmt5b12jyJ_3vn2OPcNrSv134LT5Y5B2x5AGH9VjX-Kh3z3lR7M1WFCHKin9Vh5mjzkPNLKAGYeZwehSnKKCmxwMLoCPp5DFqBZCTS0kcBGM1ZoScH9VPWvEW83ZiYVxBVaWHh8zVhZq14jYCWoswqg87cd_KWx_Ym0rwmBLRDUUX6AgMkZs_Y9FTclIH3r_LH1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
با اعلام فابریزیو رومانو؛ سران باشگاه آث میلان مذاکرات‌رسمی‌خود را با روبن‌آموریم سرمربی پرتغالی سابق منچستریونایتد آغاز کرده تا درصورت توافق نهایی بااین‌سرمربی جوان قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/23434" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23433">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=IcbMK3ogAUvHkVPV8SMrk6h8CQC9F2CLOe0FVRLgEiY6Yb8MGJ5qp10qUQ_fDOnP5yapOASKMjJGdAIPRXZL0U0grF5kCVpqoMdHyiLDMwlT8O071vsLTXoAhiF3DEe4paiLcXfvhRbKqXHKEO230WHRO9chlDChjTZaBkIikuBvR2fVx5B69FtMq1tZ_cpuNcipnEu34ajH6TRGbADQFmjw__oaUqCz9y2YDkcq0_GemjY2OgsZDfxgzZUdIlnLzFNYsxnOqZZ-Fj24qOIRHnm_X6b-wCwwNPEG_8Ox5G4JcM-UTGUW5lqVB2hj3A5cMCLRsdRQFKMBzwNObitbqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3586ff8630.mp4?token=IcbMK3ogAUvHkVPV8SMrk6h8CQC9F2CLOe0FVRLgEiY6Yb8MGJ5qp10qUQ_fDOnP5yapOASKMjJGdAIPRXZL0U0grF5kCVpqoMdHyiLDMwlT8O071vsLTXoAhiF3DEe4paiLcXfvhRbKqXHKEO230WHRO9chlDChjTZaBkIikuBvR2fVx5B69FtMq1tZ_cpuNcipnEu34ajH6TRGbADQFmjw__oaUqCz9y2YDkcq0_GemjY2OgsZDfxgzZUdIlnLzFNYsxnOqZZ-Fj24qOIRHnm_X6b-wCwwNPEG_8Ox5G4JcM-UTGUW5lqVB2hj3A5cMCLRsdRQFKMBzwNObitbqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
کریستیانو رونالدو ستاره 41 ساله پرتغالی گفته: این‌پاها میلیون‌هادلار و بیش از ۹۰۰ گل ارزش دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/23433" target="_blank">📅 13:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23432">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=iMz2r2UbAJymHHwCo7i2h-rCGPFNYbPPpL6Lb3plPAE21WfLIStXJmDpburF4nEP6E2VmLewWulXgrQrvFPyhTcSFAAweOcFSvsAat-QMlksItU7mRQl6xeppl09bCRlOXzqcaxpcNdpZbYSBcBgDec_R_OXWmE7E6yVE3lhVOQ6UBdd8p_tLt7awtMN3kB2fbvjRuh3hwRl07VWJrFhvlhfyKs7cg2gnrvtKBGiDgrp8iqXiJVU4owGkbS1f5zxt84h97RclknZU3TO5RXFJAjpGZnff-MLSWsPLezxoi01EbFFTiFDqGYefvQ41xWFdM0F-F-Hbrz3DgpfR9CNCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=iMz2r2UbAJymHHwCo7i2h-rCGPFNYbPPpL6Lb3plPAE21WfLIStXJmDpburF4nEP6E2VmLewWulXgrQrvFPyhTcSFAAweOcFSvsAat-QMlksItU7mRQl6xeppl09bCRlOXzqcaxpcNdpZbYSBcBgDec_R_OXWmE7E6yVE3lhVOQ6UBdd8p_tLt7awtMN3kB2fbvjRuh3hwRl07VWJrFhvlhfyKs7cg2gnrvtKBGiDgrp8iqXiJVU4owGkbS1f5zxt84h97RclknZU3TO5RXFJAjpGZnff-MLSWsPLezxoi01EbFFTiFDqGYefvQ41xWFdM0F-F-Hbrz3DgpfR9CNCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شهردار شهر سیاتل اعلام کرد که ورود پرچم‌های شیر و خورشید ایران برای بازی تیم ملی برابر مصر مجاز است و از ممنوعیت‌فیفا پیروی نخواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/23432" target="_blank">📅 13:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23431">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXyzXSFLLh9SfcpT6OnEsKWLoMf4KNaZgs8EWmNFfyXSD5xlcQ1I3RMliTyBD_AWGmDO-a6hyERp-aT7i4_KErBqhKiC1FqrA45iji_SGI7Mnu8EMV_IjJWl_Deb7vxRR4r9QVj_yUjJY5xCjKfpnKchNaTqfHJu4Odn7tR5Nx_V2A-GJTAA91J2ZakGG4ukT-bePyHBhgep5RpjbCf-wzxBHGUDN2Hom2LMvqXOfBColtUBPfb4LTR6HhwP4m8ulap9xR5zT4chLsmdWkvNlM44FrddReGMvbzF246vEwYwAO4yMDnftrT2jwjeROg97pEuCURYIZI7_Ut1lfDpJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
حرکت‌ جالب‌ و زیبای فیفا برای جام جهانی؛
تیم‌هاییکه‌سابقه قهرمانی در جام جهانی دارن، لوگوی طلایی روی لباسشون‌دارن و تیم‌هایی‌که هنوز قهرمان نشدن با لوگوی ساده وارد زمین مسابقه میشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/23431" target="_blank">📅 13:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23430">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKWcPK6UeeUUeAWm6WIVzVArEJsJMI6pbEfrYIjj02fv5s1qyWaiEftTF_0sGjckB0xAWvTcIjetk_GC2l7kJkk6JmM9gN1WSdyY_3Bx1rhZw-Lrdo73NBIOsHWbopLo6Vo9ca5XPWUTUoKb-8jPgLNbOP-v8ZGfzTuhqgYy7ekdXPGXpzt2bYAOOdXdBbiobHt0vd0S5YWFonQi4YWCS_mPNk7dvs70eCsmMxI9qieIRrLNe71bsOpVD-BaUi8Z2rrt6Q2lnSmnXE1sQh7q-xPVNUxK2Y3NIEt3nbLlOBg0s9Ru2tTrGyLFQvWkIYwQEsMPvLmNR4yfA72zhIDd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛طبق‌ اخباردریافتی‌رسانه پرشیانا؛ بعد از مطرح شدن نام جواد نکونام بعنوان سرمربی جدید گل گهر سیرجان؛ مهدی تارتار از مدیریت این باشگاه دلخور شده و به دنبال جدایی از این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/23430" target="_blank">📅 12:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23429">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=Spyl_BaHjAvsf8bpPeSQxBFS9JWL0Sx9OFzwDFMJnW3RfBFfCMqsK46tiwtexnT4EALhSwDVI8u9gg3DeMup6jOMO925Ipt4wxmNLPqMxKfKBBlN1WC-kQVSMFRDKVyFjnbkducDQpk1Ks3DpLWW6mmjBEjRghXM6iYBjR5T9oLUOPBl6tpB0g8YEkr5RWpoNeNKce_kLtXTqpk5NIgYh-iMu1gR_QoBCPLySQ2o6O6_h6q5Up184xyEM4rFJ__05IFphb_vaNkP0JljzQuaYoZinb6da8FbT3fEhzF7zOHUEveL7CoS_Rxxd3zixCcJcExtxCq7a4wb-XyXViKTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df3302a4f5.mp4?token=Spyl_BaHjAvsf8bpPeSQxBFS9JWL0Sx9OFzwDFMJnW3RfBFfCMqsK46tiwtexnT4EALhSwDVI8u9gg3DeMup6jOMO925Ipt4wxmNLPqMxKfKBBlN1WC-kQVSMFRDKVyFjnbkducDQpk1Ks3DpLWW6mmjBEjRghXM6iYBjR5T9oLUOPBl6tpB0g8YEkr5RWpoNeNKce_kLtXTqpk5NIgYh-iMu1gR_QoBCPLySQ2o6O6_h6q5Up184xyEM4rFJ__05IFphb_vaNkP0JljzQuaYoZinb6da8FbT3fEhzF7zOHUEveL7CoS_Rxxd3zixCcJcExtxCq7a4wb-XyXViKTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های‌ابوطالب‌و‌قیاسی؛یک رولکس که قلعه نوعی بهش وصل‌شده؛ عروس‌دامادها میتونن با پول این شجاع خلیل زاده رو یک فصل داشته باشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23429" target="_blank">📅 12:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23428">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nT3peM-1W2hi5-1aSCF9h11YHou68S3b3KS-DoguSwS3HPaMIyEfw7D10Kh8PJ3jZZJxCaF6KHgC0D8hCvTEP8JHhXPBERxj4j5r_qHWGFkX4JmjD9YVSJLb1LOzHLAGyuxzvACy_hb6dFswBdjvftpYjDhO4ZkcUELkcg5u2xdXL1CFX9RkfxpDsS6aFm5Qxrmo4okMhMdyBITEERvcAnlvLJvMEjF1jzQvbN-YdmLSrYmwzsjyWJSLkH1zh7XgFnbYJlO_gtvL9QvXlWONZYxyMGGRhYUmf2XN2XO8TVse2T97GKYlivD2IpV7u-zUgG4BAzh1EEWCEW4D7JX3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23428" target="_blank">📅 12:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23427">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOlLB_FdfY_0biRmEOkhJ6BCoJwwExxARYfbFaQoxh0CrmXbDT8LUlH5a3RLtuiZGXVmzBe3wgZzGJWZHu1mg5AzaoO9YbLvaBxglA-xEkjNPfqo866-DwI9vQqXJH5CsOn5-BzQ3UXhLfN8ALypPln2RVJHgW7ARJEBtasW8IHVWgR6Yl4wrKPSgdDjqvyFME8yqh57pldnpVbdG411Xk2FUeDtGk0fazusAZFXuTNstW-jpS_3EZZDg0nvi1FXhlL5So9HxZu8JfidjzoK2PWw8ULVD7hsnlxuSXqI3QYJwa3Wkq-IiQP0801eMevz4zkEtF9mDYbwcTb0mSZW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇺
سرمربی‌تیم‌ملی‌استرالیا در حالی تو ترکیب تیمش مقابل‌ترکیه ۶ بازیکن با ۲۳ سال سن یا کمتر به زمین فرستاده‌که‌سرمربی‌ایران در لیست ۲۶ نفره‌اش فقط به ۲ بازیکن از این رنج سنی اعتماد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23427" target="_blank">📅 11:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23426">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kxhj2zFewoguUOKO8M84xkUs9dbGerF6ITkEWS7nJtE_CLLSV8_PMSZOXM39eOJQuL2OG9rTc1uzkmUUL_FHaWVyaW--_HwWPBatfZQhCSMgUyfgpD5mjx5qEs9S5GBgvy0TO05kPvgFuieQryiY3Iyu53U1DqOduiklTKlNVV5CUGirzxQr5zhdpl2QiqIyC2ZqeEYc9IBU4gByXj4hDnk1Kc4bwICbrw5QTbWIGpVNHoLnJ6f6pCR57tMVwZqbvtyx_AXSjlEo_1izpF7NmYZbYcUE3lj6kJhgh8bM0ViSTNRP3fH-iA5bY7PPMxpsaw4xOpoRbGndGl3fRiL0Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/23426" target="_blank">📅 11:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23425">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQG5aD6ByznKVPbRULvJVm0De31aazr7jn-mpOqi5kdIDpt0shR05Jxz6txf40kGxMTQxsbouU7xS9c8wKsCUMYOP97QGT1ZIT67R7HnoHpxqQgCO9MkapYZRern51WRf6u07Eao6mvRamNdY7ixH4Y0BYKuGhROuDfKBQd45c9ET1A6A46yZQaOG-O-c6LlfiZssqrMRJqBIOmoUgCSft4CN-UjCEdS0igODQiSkLbxWbCIlPmYIWcoiFXTeotuW_eFTwEBsnNihOOO-c-D9nhTRyLds1L0dYMk624GaFBYDZ5gWKYue_PdEXdNtlwc4aq5R7DByvuhV3KnBSRhHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
⚫️
#تکمیلی؛ روبرتو مانچینی طلب 15 میلیون یورویی‌اش از السد قطر روبخشید و رسما قراردادش رو با این باشگاه فسخ کرد تا ایتالیا رو در یورو آینده به جایگاه‌اصلی‌اش برسونه. مانچینی در یورو 2020 ایتالیا به قهرمانی تاریخی این رقابت ها رسونده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23425" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23424">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QidJ5Ts0KNnMDIca2CkVUSLehtQ1RhiobW3km-8cJ8CItQ4X7n-Gt3wn5OGOgRlYHPNg6V0OHmXi8QXwYvAbtfSU5jq_zMaK2BgsdyBPeSI6rovNsQFgP471-UOKgIEqIGWFvBXxLwOcWSiBMFh29CNR3cO2zkrdpPiEbZSEJZQ2BkQovRFm4bqs7KMdij7JN-nH96gursUZVcFOk191_apRM_9QFU-UVvFWakho5Sq_fjeQPI-ZFm9CX80J-xrlemu91M87Yn1OtluVyvRfAub1jSygHQ0FGdbaHun_DLKC3_6prG6WyJ4YIZZ7CO8KXzj-_TuIgmU5LClSzbxnPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23424" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23423">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lgKJqTdNC4tyrdyhv-qahCM44pXIi3jpGuvqJCbxhAsSGeGagDkQL28qHkDLndoqDDnWW8fpsXweET3PaNqRbe_YkCCBx8VzFvyDvKLRN6_gb97ky-KANkOZKNFtIpDvLUcx2E3fgoSFugJT-WU6MBMrtAUMTOgZW_loKMX1jQaS6r9n1mriw8b2RiShJk4cWmdZboLmZdfzJETqY-46N-7-xcHrfopull3aNuDW_MR9fJT-4NeYrfYKsFs6BcUNRhflXNWr9Bjd1ZsWuMnLZ9wVwNAL1HMZOimddHOTeldA6-65wYdl2cDeDJ2nTsv8QJfezw9Oq8He0-iaxjIHuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MelBet | جایی برای پیش‌بینی‌های هوشمندانه
درجام‌جهانی 2026 هوشمندانه قدم بردارید و روی پلتفرمی با اعتبار جهانی پیش‌بینی کنید!
🔥
امکان شارژ کارت به کارت و هات ووچر
اسپانسر رسمی جام جهانی
پشتیبانی از زبان فارسی و کامل‌ترین برنامه موبایل
قرعه‌کشی و آفرهای ویژه جام جهانی
✅
حرفه‌ای،مطمئن و درکلاس جهانی پیشبینی کنید!
📌
برای ورود به سایت فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌ Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23423" target="_blank">📅 11:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23422">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWW-JB09P-7yAESSHmL0vID6Pc_On4Lfywlju6z8yboScAAn_LxdHvr9yD-8lRpYuSAtgnIBb_kq1C-qOINgXKs_Q4OjV5SH40wn2jgH2BOiGowq9MKMfGEPLIjayJ631RkJAyXXvHviMGulYlpADIE5UCUDBKhqcxTZc12_boTEbNA9blqrf0h5OdUBLQT7G0YRp6imki5OGOTJAkl4cl_rYz3uu-fQs_3IR9o6gBGsr3Txnt3v6_N57EI75gXTpWR-cWtlishwWtAxlavqKU6QUT9-eQFvAbonIWKPOx1deR43TxdvSaTYAFys8EMNzBhrIBRtQi861ZE8FkLRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
طبق شنید‌های موثق رسانه پرشیانا از نزدیکان کسری طاهری؛ روز سه شنبه کسری طاهری بایکی‌از دو تیم استقلال‌ و پرسپولیس قراردادش رو امضا خواهد کرد اما فعلا رسمی منتشر نخواهد شد. همون روز سه شنبه ببنده درجا همینجا میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23422" target="_blank">📅 11:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23421">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJo_F4ZvivJCBfoVYPHhq9SC3ks0nd5GEtQKj5UT7JN_5uGhh8YZypHjV4BMMPyP_nIkZgSi7Y9mR2GSyssOqjycr8Xq2SXUrrgvDLQnRaMnFYqZihaz0HhpHnmcl9029GSIm2yRkNM18AZRkMywQEkWzhUp5GxdsaHZtHVq2jN1ljwfxCpUwQh-GkRZopOoAx4YYLLc1IMH4bY4nySDu1P8Sr0mOURbvK1SrMoACVwTjIin4ROJjYo649KDthlzp9I6zmZYgT4IllpmddNpGtx089tigiaHe4oLW0xnZhr0plSrSseglune8xpgEysLISy8_5Ncl0Fqi8InxsetCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول گروه C و D رقابت های جام جهانی در پایان هفته نخست؛ استرالیا قاطع و دو هیچ ترکیه رو شکست داد. اسکاتلند هائیتی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/23421" target="_blank">📅 10:50 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23419">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/je47p3uSx0Spdm9Vr4OnUc9AW_XH3jGENSjNjvmP6zCz1E-y38cOJ3uMh3HaheCsdbkKVXrib-bW4qw9Ppvsw257HQlL2tVt0kvDfGVFXFITi87J04tQMl4EL8eAASAkANXwiGXzo8LGhMn3gYr8Cg5ND9XEXj3oy6w6jh03ThhZSHnvoEAMp0mOBZjjuU9WAZ8Ym8QV3NKHRjPFakmQ4bLTWnt6lT4dj7ACZ43Y7Ma3M0KeRRJ-kx5HBdUJ6jWxYHS175XRZ6HBWXrdZYo5iQE45An14TsZtKGzdr9n30kNScDzbig5I2kPZStY9rn0g-p5nd7CRzbbe0-QK7Znug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Np_g05i5rO05ZUSnIW9_CBQdPhkmsQhkxOaO-th8Yums3TyJNYscw3bk3EESg6Fu9npa9339TAonpo8v26BDRHsDZOL5Ccy6w14wpM_XzmGMfSNDu0QcKKcxW56kavsUj34jGq9UHunBf-8rDxPVzdFyHlZmywF_PDfDUT4DiV8j0BFUQbot-GzePCBAE91ofxQzZL3ig4lLFJvDEDs1hDk1JKUwUSNazXmDmD9wPmsENtwAJspIm1kgOhPj405ZEehMrEMFszFFlkpautbSf56_hjv2QxoAUICfsJyPFhJhlCZP668QvMZilk_QeY1yv9_zaTnvlFnh2hW1ocmaNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
اشرف حکیمی کاپیتان مراکش: اعتراف میکنم که در نیمه‌اول روی اون‌صحنه باید اخراج میشدم که شانس بامن‌یاربود و داور ندید. لیاقت‌پیروزی در این بازی رو داشتیم. هیچ موقعیتی به حریف ندادیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/23419" target="_blank">📅 10:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23417">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSUh-_ql-If-4KjbjqH_kiWUWFdfofjAbXVfvMUMnuqXNRRGaHgWYsd7tpsc0zk1HRvCFokdg6Fxp2KrdK2_-G8y8Rjyp-iOIBK0cLejzaopKZ_3G3ffhgMhe-AkBrMlUHEAAaCfWOotut047DuIIbsEBOCkS98kfvBgAMb3VxDx5itwE2_h7cUGUoAYpRUzk0OjTXFWpthEfDHellvTPxRNz2LZUqastHkJ5SaMU5QhrZQf4HqRt_T8I2sVK27q0xQZBrJpV7J3BPbBaX-WM_PfGDtyVAihZ086CHnzHH6roHYYyJkWW4ZdMGUBrrDvdAkX-LbLKW1-VrsJEwMygw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=AzzjSC-PcHJEt_hRyxcY45YB5Mog0SwahDFePmpu2mdCWTeHhfFDXbi2ypEwJQ7_h8hXSJmiMYX5BoaJRF-gFTgtyI5ZzHmxd021231EFq1IZvGFxliGDgd22_sy9KoVUYoF3hfREOUGVMiM95C1dWmUUVVITv71oaJ00_K_7rT2bhlMMmbwzWdLNhRZJkdIM-GIooB9dY82sawA5Jn3UrgP5CIv66A6y3j1l9GohKV9zxow2Gaf9iiT18T5wQOmdZUbIAGuiuPrRhECYV9yzNefX7bPmISRLIOhDUI8L1YO06vkB_qjZCW88vYY7Hst7fj5gcS4p-g5p3xkdaSDlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc2df20eed.mp4?token=AzzjSC-PcHJEt_hRyxcY45YB5Mog0SwahDFePmpu2mdCWTeHhfFDXbi2ypEwJQ7_h8hXSJmiMYX5BoaJRF-gFTgtyI5ZzHmxd021231EFq1IZvGFxliGDgd22_sy9KoVUYoF3hfREOUGVMiM95C1dWmUUVVITv71oaJ00_K_7rT2bhlMMmbwzWdLNhRZJkdIM-GIooB9dY82sawA5Jn3UrgP5CIv66A6y3j1l9GohKV9zxow2Gaf9iiT18T5wQOmdZUbIAGuiuPrRhECYV9yzNefX7bPmISRLIOhDUI8L1YO06vkB_qjZCW88vYY7Hst7fj5gcS4p-g5p3xkdaSDlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
برونا بیانکاردی پارتنر فعلی نیمار جونیور و کارولین لیما اکس میلیتائو در ورزشگاه بازی دیشب برزیل
🆚
مراکش درهفته‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23417" target="_blank">📅 10:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23416">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eb4mnne2MDT6UvMKT59BenLoWPaWozRWtxJRwzLQI33aJBNxLGl9i_eZJIECFpZjUDA1As-Tfxzu977p7SrGihs7CdhklMZHXfHQZBQhpm0l3eVJFq-y4EigsUajZiE4bOg-rGAqlldHjMlgvJO4ZeUe1wq7mLAzqTMuneX3fALPJReq4kUlg76M-siDCg6eyjmDWW5WLKhwTZzAojbEKJehBzwza6BfZn-_3eNL5f307NO86PgEo18BJ4OSo5IWf1lRrkHBdsx0mVFEpa2vByNYcnx55HaMPv4vb0Vt8rsb1WSbGop2JSFTxgZF3qeUMTgEfiH-Nn32as1da4HuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
ازکهکشان‌اومد زمین بی‌بال پرواز؛ مثل شهاب از اسمون اومد با یه راز؛ خرید اونو قصه‌مون شد آغاز، امیر10؛ ابر قهرمان جدید ایران و جهان
😍
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/23416" target="_blank">📅 09:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23415">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=KPibLAMiQFN5Q5WVmyccHrPzywTokm76DN0qUdz2-J2ffhivMaYFW17gI9pp2caMb22zrnvM3YUx8igC8HiY1HrriA3ViKryTL2XnzgrMREwJCJ4yZkYmtQMPMkiq4RnHNqs_KJhQ8fb7w89ymhyvXm4N2gvmFTpIv3ju6TK6OYAA8-yYI_2VqlvPywlJbaqlW_GTkpndp_0530205gAwD7Uxod2mOSRF251cLlqG6TCOaVI3rCYeISMAPMuzryZyatk3FGnYVZH7pqSjcNOCCqk2f_bLXkC3N6E_dgBDoR3y8PNd36UET7g2fUS3s_bX0Lkxz0D86l3r7phaxQ75A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/260d53aa6f.mp4?token=KPibLAMiQFN5Q5WVmyccHrPzywTokm76DN0qUdz2-J2ffhivMaYFW17gI9pp2caMb22zrnvM3YUx8igC8HiY1HrriA3ViKryTL2XnzgrMREwJCJ4yZkYmtQMPMkiq4RnHNqs_KJhQ8fb7w89ymhyvXm4N2gvmFTpIv3ju6TK6OYAA8-yYI_2VqlvPywlJbaqlW_GTkpndp_0530205gAwD7Uxod2mOSRF251cLlqG6TCOaVI3rCYeISMAPMuzryZyatk3FGnYVZH7pqSjcNOCCqk2f_bLXkC3N6E_dgBDoR3y8PNd36UET7g2fUS3s_bX0Lkxz0D86l3r7phaxQ75A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نگاه عجیب ویکتوریا همسر دیوید بکهام به تام کروز و حرکت عجیب‌ ترشون؛ درسته ما فرهنگمون خیلی متفاوته ولی‌همچین‌چیزایی دیگه مورد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/23415" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23414">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxyyPlQhTTpB7p1iMeDoZN1IO3N-kUU67Kbdbnzp88DxDW8Km6iS4nqDkOaYJL5dw6rsXPRL0qN5UZTk2x_sLpxX2nbO55-fz7OzHy320OoyQgXaLJVG1wTuQDOjqc1WwXj5r-tva0idFAwi6uLNBPgjF0MOK2IbC2p12x3-vad_0okGSbPDl_J2IK7ZrI2jdxTuazyR5MhAubMtd7aeNmHmETsoO0T_gokw_CZHFRUL8_Hewj8pM9hjRWKgTfEX9rzESZkN058KLnhrNWkxmvjcC572kIChABgbZgkGwkG8yrdtwZSmDUZzUpxJiX1f6koQrvLdMmjlG6F02urk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
درحاشیه‌تمرینات‌دیروز؛ بازیکن‌کره‌جنوبی داشت وسط تمرین یواشکی از گوشیش استفاده می‌کرد که یه‌نفر از کادرفنی این‌تیم اومد گوشیشو ازش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23414" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23413">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da531b194d.mp4?token=a2UJ7uCFxgU6F6ouE_NnwLDCwW3StWul6boDBeShMwYpwlU7bNhNduRQVM8RpAuJEJfRWY0YCYPopifph8h6Ke8Bv_DOHyoF19pChv6VeyPsenR_EvIwFJSuw_HyaoS760spMNl-NCZA8zgxzwgOOcaiUmKgvcKz70X6BNMaLs9PzvDHDcx0is0vJFQ2cpfc8VpcTffgtbzJ-nNmbunVbTHaNx0YRPSDvbUp_g-ogjDO7Vchct5947IfNutw8q_FVK4n0Mrlmb_yMR6IlbV1BPq6ieokrLuVMACQvX9-k6YNH5gfoBS0i4OQU1Yk5q16Kpe1YeY0QWelJPupDSqoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da531b194d.mp4?token=a2UJ7uCFxgU6F6ouE_NnwLDCwW3StWul6boDBeShMwYpwlU7bNhNduRQVM8RpAuJEJfRWY0YCYPopifph8h6Ke8Bv_DOHyoF19pChv6VeyPsenR_EvIwFJSuw_HyaoS760spMNl-NCZA8zgxzwgOOcaiUmKgvcKz70X6BNMaLs9PzvDHDcx0is0vJFQ2cpfc8VpcTffgtbzJ-nNmbunVbTHaNx0YRPSDvbUp_g-ogjDO7Vchct5947IfNutw8q_FVK4n0Mrlmb_yMR6IlbV1BPq6ieokrLuVMACQvX9-k6YNH5gfoBS0i4OQU1Yk5q16Kpe1YeY0QWelJPupDSqoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23413" target="_blank">📅 04:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23412">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCS7yh9mGJu26UlEa8XBTzFOZuyRMBuX18-tF4hT1DYtF3haCUqcJWaaKaWzq9yxCVkPq3Z_PwNHyAXr88VaB0ZMIiinzpK2hWDojUyP0UtQGJJHPX_M6hEpQGytNgdI-pChgrCG6sYmaYyit0qzIFaRJpqn0XYhNTcfCWaeCl_8C9_uebJ9KOL8cSy1Hqgd2dKtr28HymbZE1G7T0uCsRw55TO6G6Q7QN-CdGprtyZgsYUvklU3fSZ2PFp1d0u5blaBnV75n8KvYgjuAo_8VxJPn6RgNfsLqvoMgQ7cmekiHRHsnlj8FPLPwIvwFbaqJvRSm-KQkfR5LQEIeG1nOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23412" target="_blank">📅 03:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23411">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">▶️
گل‌های دیدار امشب دو تیم ملی برزیل - مراکش در هفته اول رقابت‌های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23411" target="_blank">📅 03:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23410">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی|توقف‌شاگردان کارلتو مقابل مراکشی‌ها درگام نخست؛ یاران حکیمی نشون دادند خیلی حرف‌ها برای گفتن در این جام جهانی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23410" target="_blank">📅 03:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23409">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlEJExQPY8SEEAkLVeCZg1xHU0VfVw5DiyP4UO7CLY88izxMmi9n4s4gF3e1tB_gDQyF90Ho-sugYgUD_IM76cnM5xd8P203PdtslasP1xX-OX9hTB1p_qd3Zgu-LbIFly07BoHFryCvJeZ7ru1IwMUvAZIYRS-m7tNYK5Sv0jlxWwFcQ2_biiZbpFjqpgpIBjR_LiqKMdsCsRGt_o7SMhupcBbJIDbFn5KrJPezONZGwGxCdyW9tewOYY-2WGCmqT7v2FIFLQ1wovOreTZQWDusfyWKzS2yZveilJ4dCfWARpeotzUwv05wCkIV7EVEJsdKCE7cFuOyGg3j4i5ZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23409" target="_blank">📅 03:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23408">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858efb6719.mp4?token=jDvKGaUDDRAMyT-i3bB0qiIFl48Pbofv2zDSD7ImuR420dH66qiVTIBPKljRuH039pp-_LJo7MOmzi4KAwffTcBzOpHy8v-x1XO_rtb7m4QVRLv8nnXZth4n6VVrDcWF05oqHu8xNvXQLuoJwZFjQx918nZ1ryx8nKsryyv9S3gsqUSythpTcdMFEXpBtHi-Axq6M6YjncYI9bujLNY0CbRHyMMFLm0mp83FgOwMW47viN9E3lfAGXDnm4SPQaQfEXxqjcKwgNykFQ6Es9Gvxs0Q7CzTEtb-rp4k-ExBBxF9xpAIku2gr54CngkQRCbYsO3vOIAykl5IJMWiZSsspA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858efb6719.mp4?token=jDvKGaUDDRAMyT-i3bB0qiIFl48Pbofv2zDSD7ImuR420dH66qiVTIBPKljRuH039pp-_LJo7MOmzi4KAwffTcBzOpHy8v-x1XO_rtb7m4QVRLv8nnXZth4n6VVrDcWF05oqHu8xNvXQLuoJwZFjQx918nZ1ryx8nKsryyv9S3gsqUSythpTcdMFEXpBtHi-Axq6M6YjncYI9bujLNY0CbRHyMMFLm0mp83FgOwMW47viN9E3lfAGXDnm4SPQaQfEXxqjcKwgNykFQ6Es9Gvxs0Q7CzTEtb-rp4k-ExBBxF9xpAIku2gr54CngkQRCbYsO3vOIAykl5IJMWiZSsspA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23408" target="_blank">📅 01:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23406">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAN7-mz-ZHNUhWPvizZBEJeYf1ieLq-atVzOfX4RHp2rPwTmIDSPPmbxSxDF3xlR9T68IcX79LEBXd2bOIOal8dYBLebitYUbEJHdxz_Vas89tgpd0Ck38OJTA6kjL2O51BrI6X6RSOnn-fe5G3IWRF10cRh3CmQKyDCRxKQFAaZMBBzcsVgcXlyeEAsUu7XzN1_ALojBTwNYQz73LCmNdVkYuFQ0wPQJxz1iKJmu-aH3LulgCYWxr3yPJPfpDAzhyjIi-YHkDYXUjmXwygSmRc0ZIsrzkiXtJ9_BMvXp__Z9I-gtfqt9n4rKH-lcXrTLmJeeDy-MPPG4qWcv58hOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
شروع تقابل‌های جذاب جام‌جهانی با دوئل تماشایی برزیل
🆚
مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23406" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23405">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLfWNDOYzWu7ijCi6TyT2MIuNoGt5CkRMUVEfX_N0BfmOf4UiGnMk1WGwQ7vXy8uhmGtuVUD4aZQ3-OaA1OwcacrRaoIdwwy8VpGD2dXFue4mb4s_6QPgEZbFFvAqJ8AhgSagtWZORZz2Zr53hkfXZmcVX8PO_RJS_ye2-KSvp5jtNCgZsz86UaJgR-1GGA-Ub6IQ7yQ1qoHIqJQ1jsfd6YSrS5eIWuTP-pXfKysRuUC9vl12keVRGXL0OBOLrVBZvsMTrznW3PLw-MMznWZjvgARATnbLZoguQKfjpzcisTxdFprctISDQdir7JKyWdOcbKpivnn220jqY9XzaB9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
از برد آمریکا با درخشش بالوگان تا اولین امتیاز قطری‌ها در تاریخ جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23405" target="_blank">📅 01:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23401">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-IDtR9uvLoeKJmJl8ME1k22-uatKM_kI5aNHCnzR9OexYkDwgUIAbr5eNdhNP84faB2AkSHaitwm46J6IalWN9z8ajaISNYChPqjGdbJenNUY5h7QW5wqlp__VTyuBlUKWVaj6WBT10KDBP4toxLzSNUgw4UD_zj3WL9IYRCTqt0JiLfPVtY24UNv9HW4vGVwiUp8U-ph5NgECicYhTT01RZqWq8TdEUOACXd-LQJvOQ5yxoRzg51fLGfGr60aRSu7cHipkBLqDpBmZNwi6bosZ0qRqBfVH6mwCFS04Bes-6-YcOi4LIIClRXol8KOmjkmkoS8WovfkdGeXjtd9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسانه اسپورت ترکیه: کادر فنی کایسری اسپور نام پنج بازیکن رو در لیست مازاد و فروش کایسری اسپور قرارداده‌اند که نام سیدمجید حسینی مدافع 29 ساله این باشگاه نیز در این لیست دیده میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23401" target="_blank">📅 01:22 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23400">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=W81eI3_ZThzgqDvlQRbfSrmsK1zTtk11weSwIxxQudwn2O0DgZorzn1XcM7tdO7phZJ_Bzfkdhlgaf8tJwdD7ulpqU0A218bK10CkJOD9UwalCiZADEwg8MiRmC6C4MQLZlkU_xhSDlrhB_NJ9EhkQVLQRQU3K3Sro_Sx-F6X5-KctHDeS9cyXLQwxeo44S1UoYyPmf8KbNoV42g4g6pN6Ku32beBPgNAS8hIbFF4Pl0M352c0vPzh_E-uAJtLXSuHxiCwtYYurjb4Fplww1ov3wbKr3YHbUFNUIx9izmb47WiDgFma1bb_BrB2nnnS3r5i5JP7mhN59zcHlGBm4eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db8eea25.mp4?token=W81eI3_ZThzgqDvlQRbfSrmsK1zTtk11weSwIxxQudwn2O0DgZorzn1XcM7tdO7phZJ_Bzfkdhlgaf8tJwdD7ulpqU0A218bK10CkJOD9UwalCiZADEwg8MiRmC6C4MQLZlkU_xhSDlrhB_NJ9EhkQVLQRQU3K3Sro_Sx-F6X5-KctHDeS9cyXLQwxeo44S1UoYyPmf8KbNoV42g4g6pN6Ku32beBPgNAS8hIbFF4Pl0M352c0vPzh_E-uAJtLXSuHxiCwtYYurjb4Fplww1ov3wbKr3YHbUFNUIx9izmb47WiDgFma1bb_BrB2nnnS3r5i5JP7mhN59zcHlGBm4eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های شیت‌رضایی مدافع‌سابق پرسپولیس در گفتگو با ابوطالب درباره حرکت منشوری‌اش در بازی پرسپولیس - داماش گیلان: نقره داغ شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23400" target="_blank">📅 01:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23399">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✅
رتبه‌بندی‌کشورهایی که دارای زیبا ترین زنان دنیا هستن؛ ترکیه با اختلاف در صدر جدول قرار گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23399" target="_blank">📅 01:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23398">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evfKd2dGfBMrmzK0ZXmLFFF6Wg5dVOvwbo4emuteJjdYb9y5EfBCOpq_9npxHZpPcDmmx17Q7R3Tp_PzDvaQtWnYxBVGEvdGcVcWL6ikqoANCNdS9XY6no7nJYRjR_d6C0Ts6YhWxit9B8GXWttlqtd1biXNmcjKnkgiQiPx3CLxJ8DtAnEGxxQN5pw2SUw4H4GG0c529LK8d4vmc9ZP3spTB9Qvx2rP0ZGKJqnmjcMigkxr0m06AYIDo08PfjnmGC2U49WnKcNNA69SegdVGImODzdR4gmoHD4faCils8xIttkJVW9SSUGtRPWwQMpsjrLDHbaVfb_hmPkq3VwvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌رسانه‌پرشیانا از زبان کسری طاهری مهاجم‌روبین‌کازان:مدیربرنامه‌هام با دو باشگاه استقلال و پرسپولیس جلساتی برگزار کرده‌اند. بزودی تکلیف نهایی ام برای فصل بعد  مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23398" target="_blank">📅 00:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23397">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=o-aAS8yLefRS0TTuoeqC6H1UCof5wO5Xr4fZMxIlzGzJK9xlIH1JLcjdzQuFs7_6jjnbAB6vHEnDbbHbOKFzKX724jyoZj5QC_Ad-34WmWxYaLAK6C6RP5x4CTf2ZWppcInvpf84wCsPVQutUen21K9knSiYbfTdCVwDllo_ScbS6Ow-oz1S7vUtSf2C9GNVQsrgboEwFSsYHZJnltbahqc0AJEHIZ7kwF1QYJSZz_fSwL7tMKf5UuIYUL7VxCz1VkA5M-bpMRRqUK0PKpqmeVhNkRvN9NBuZptAoPTMZw-JzcPNF-UaneBJxesloPAvl-3Org8FBtR5d6DZXm5u3Ch2r4C0QoSNzFzqGYwHXjcFETzsK_3ZwbGe4fmx8v-_uhmw5wQsvbfuTE5yTn4dxxLN1IG9oG9aS75HD-uh0bTx4dljMM3Il7ovMyzrFy9ow3Iql_9MPADX0p903wGTv7o_3Y5GvttKKJrYue6_rScdYbJoc_JN0FW3Y6_Zr4nPCZqvCLOMar6Vazu90ugD8DsYjOti38qA3EKLjJ-VFAGYmRrYXXtn6Mvz4PGPDNAMIzV1F3q4IavEZPm8BzRRasjnkJEDZSEBCXw783UMc3im1ntl4rAP2lUTFroUgsQ9ZIjioI_BGAfgpxhV9v7yEtGrfSD0AmD2XVBF_D2qNPc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c16a032b2.mp4?token=o-aAS8yLefRS0TTuoeqC6H1UCof5wO5Xr4fZMxIlzGzJK9xlIH1JLcjdzQuFs7_6jjnbAB6vHEnDbbHbOKFzKX724jyoZj5QC_Ad-34WmWxYaLAK6C6RP5x4CTf2ZWppcInvpf84wCsPVQutUen21K9knSiYbfTdCVwDllo_ScbS6Ow-oz1S7vUtSf2C9GNVQsrgboEwFSsYHZJnltbahqc0AJEHIZ7kwF1QYJSZz_fSwL7tMKf5UuIYUL7VxCz1VkA5M-bpMRRqUK0PKpqmeVhNkRvN9NBuZptAoPTMZw-JzcPNF-UaneBJxesloPAvl-3Org8FBtR5d6DZXm5u3Ch2r4C0QoSNzFzqGYwHXjcFETzsK_3ZwbGe4fmx8v-_uhmw5wQsvbfuTE5yTn4dxxLN1IG9oG9aS75HD-uh0bTx4dljMM3Il7ovMyzrFy9ow3Iql_9MPADX0p903wGTv7o_3Y5GvttKKJrYue6_rScdYbJoc_JN0FW3Y6_Zr4nPCZqvCLOMar6Vazu90ugD8DsYjOti38qA3EKLjJ-VFAGYmRrYXXtn6Mvz4PGPDNAMIzV1F3q4IavEZPm8BzRRasjnkJEDZSEBCXw783UMc3im1ntl4rAP2lUTFroUgsQ9ZIjioI_BGAfgpxhV9v7yEtGrfSD0AmD2XVBF_D2qNPc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی؛دشت‌یک‌امتیازی و ارزشمند نماینده آسیا مقابل تیم پرقدرت سوئیس در واپسین دقایق بازی؛ لوپتگی نماینده اروپا رو متوقف کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/23397" target="_blank">📅 00:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23396">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=tikkuf5VS0yMkKhlFI2fcRQldXIERGJxf529k0mv00Eui4YVLRpkfEQCrvRWmsgDzdvLXv1iLzYdRi1IrL2SauXqh9FE6dNV1_MM4sYDaEUPuMtzCu0oPY_1i9N9QyMN63Vdmmwf9ymPpBevAp5jNNvv3Ew2vQpUgTLNE4kST3vqoDugSW1rHoRIcKXMHZZtLhgGK-yTNujwRDaofw-Wt5q7sOgT1QCOKkOX9nskdGkBG3iU9hEVSZIizyXEBoQZPKt6hFGDV4eAxRL6T9O3m2K-nt8HjDwnaz3fGb0xLNdxB9KDg5Nd1iC274InTIrE8-zNt6jD7SQYudXi3MMxVbMCUQOg2x0ICZK_8ug55Z71V3w9dVMAgjRy-s3loEBy0QW3R-GuJi4APPuR6-2Ar543Vq5tAytWSF1b8gV-IFo1LQxkYSfAxGk5qsf4ZLNruXv2_fvz0HTy5LsMDaqt8IKvGHAG6j70-dQ746bQeIb9x8cFVUhVxhHeqwAoAZ6FOdzNlx20N34gWfj4HFCsbik5hKGlL0RBiNBAWrCk2iI8Wo_6AtjZT8HsLGt5nQHruaXLVROYI1xsGIdRVOQd0p-9_0lrBsus93FuKiiiJQCUJffl28c0L24nhStb-Mz3WXJolXoM9m1KSO4dqSBpyXcTcAdOYPRjzDOI2Cf_Aao" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ba749a0b.mp4?token=tikkuf5VS0yMkKhlFI2fcRQldXIERGJxf529k0mv00Eui4YVLRpkfEQCrvRWmsgDzdvLXv1iLzYdRi1IrL2SauXqh9FE6dNV1_MM4sYDaEUPuMtzCu0oPY_1i9N9QyMN63Vdmmwf9ymPpBevAp5jNNvv3Ew2vQpUgTLNE4kST3vqoDugSW1rHoRIcKXMHZZtLhgGK-yTNujwRDaofw-Wt5q7sOgT1QCOKkOX9nskdGkBG3iU9hEVSZIizyXEBoQZPKt6hFGDV4eAxRL6T9O3m2K-nt8HjDwnaz3fGb0xLNdxB9KDg5Nd1iC274InTIrE8-zNt6jD7SQYudXi3MMxVbMCUQOg2x0ICZK_8ug55Z71V3w9dVMAgjRy-s3loEBy0QW3R-GuJi4APPuR6-2Ar543Vq5tAytWSF1b8gV-IFo1LQxkYSfAxGk5qsf4ZLNruXv2_fvz0HTy5LsMDaqt8IKvGHAG6j70-dQ746bQeIb9x8cFVUhVxhHeqwAoAZ6FOdzNlx20N34gWfj4HFCsbik5hKGlL0RBiNBAWrCk2iI8Wo_6AtjZT8HsLGt5nQHruaXLVROYI1xsGIdRVOQd0p-9_0lrBsus93FuKiiiJQCUJffl28c0L24nhStb-Mz3WXJolXoM9m1KSO4dqSBpyXcTcAdOYPRjzDOI2Cf_Aao" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23396" target="_blank">📅 00:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23395">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF1x7gzpO4kemMvKDlpxpcNmP35E1UKJBoJmZCNM0oLSk6woB1URRW4l-p4UQ7GxaRQHvx_UrQu5Xh_1c-bMfTU3rzB2gCm37nWDCHTFhijM5HlBowPmVTey4SL12etWopVPkuSDuki3Nc2xY_bI1q6fUxulgt_Vrc34IWIXs65J-8G8EAw1mL_LgFU7vvJC5og2lmOd5tc93xhjg3kV2mOYS4SazHRKNndXw0fPg6IRoc2KN-mTK8EfO6yRANsTB5T1jSHDDCys2osPnPSd6jU1Bmls0-T9bH-qWC0wOGqtwJTUrdgiEb3fzWKORNCNEut8uuG8A1gmCsJhqoqWoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23395" target="_blank">📅 00:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23394">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpPzHsXvglIOsLO2a9WdVX-_MeRRr-i5ZaAZn-dU-jHKQP1T15mgbCSyPjP6SZy56KT4PrSMcxnp7OtBp-E_79KWci3ThM5Dy8NZZeaHmN0_hsXAU9I_0AeGQSE-dQK4JEmR-QgPcgl1rEbYP6XFLMpXgH3Qyy5FWh315GPqTVeKtuZ1_cbJo5d4p9vol2_AgIy4DW6SRsgSkKo4wDsQzZd-ug6p--GBlNWS7E6XnUX6oYlRbR6ewd6VKPO3ALl7puOi5nz4y0P8y0LYG90jW8LnzC09wGOhvNrShLf65QlxzNNzMuLlUIcRsqtqUdF9KfV6l1SgmOHNujmNJZiTrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خداداد عزیزی ساعتی‌قبل با حضور در دفتر مدیرعامل بانک‌شهر مالک باشگاه پرسپولیس قرارداد یک ساله خود را با سرخپوشان امضا کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23394" target="_blank">📅 00:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23392">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHq40FHuC-KuWeCKlO9t_oZ6bLoEpJVmNCM74Z5nAxToLh776RVQEmpiFupUcrugO2ppL7TQ9RCcQL3L1dIzaE7O2AMa3-NnC31vAlHI7pDxJNmKKZF8m3w755B4obyp3eAGWShIlSeRD4cqZadzVgobBj0V6ammy2Qs5LAxYgOwQ0hdEjAlV_lMkPizyiypz1F_HKOSN0iNjOCjLYE1UmTC_RWLdZv5_7xf9EbegvA4lrpvd6x5OSlF_KACWIEUUNVaHXiWQdUQe4wjRSMKn-eO9D8QhUiioqIG1CdfUg93mVp3caYI1RsUFuQn3y7yKEM1vRIGY5s5h_Ist6l8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CznaUJcx_ezXDLf_PhgDBJCZkyP_MmvYtFwR2HQDHBRX3zZ2n7lIlyvdEkqYYGncLCTwXn21bamEsn3-GaHtvkTun6Dl0L15QLjgkoCzgV8zGmIIFK2AgtKGi6ML9_4Kxsc-n9oCftE83UWldG60UL2jnxcFOsHechL-9QbU08cbfwalFM2AYzX-rHRToytw4hziAXVe38CvkE7Agek2Cb0C1bhFZZB2gwNDEM8Ia_S-RgeCGQSoJlqzTBB-o-jUqjWc5hP3Dt2DJOKU-LHDsm-V-yd1GWx7H9BA6TOLCFQyELMc7bHsWA1GDchYoXizrQYJlmhq0AQKMkKqqzwUtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌جام‌جهانی
؛ شماتیک ترکیب دوتیم ملی برزیل مراکش؛ ساعت 01:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23392" target="_blank">📅 00:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=MLZ2HlfH25Dt6Hwm7orAk4LY9udqEof767JWQk3at3GJoK1c_4l_JQjYt86PfWsz5pVUimIPTUpDewIkarnqyVVvhcF4q8_cw8WaN_xCHcST00rjKlarWJm-RaEVtgMxcv4z7tRTcYc2apZgcZxEV9drblVpzTL_Yqim-8JAOLE6MMJeaRexM3_7WkKvXuwlQIylz4TUdJ8oL24jL0-1Vcryk18toCvubap-DAsSuer4yqPnAMfITAjBWW31-iPHWKM_9WWDkIFX3bss6_LV_0RaUeckiy-NvHpACKyFFzHHJZTyRXcR3a6YXHsALHp7buZuks5rBKhpVGhMAzmTkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=MLZ2HlfH25Dt6Hwm7orAk4LY9udqEof767JWQk3at3GJoK1c_4l_JQjYt86PfWsz5pVUimIPTUpDewIkarnqyVVvhcF4q8_cw8WaN_xCHcST00rjKlarWJm-RaEVtgMxcv4z7tRTcYc2apZgcZxEV9drblVpzTL_Yqim-8JAOLE6MMJeaRexM3_7WkKvXuwlQIylz4TUdJ8oL24jL0-1Vcryk18toCvubap-DAsSuer4yqPnAMfITAjBWW31-iPHWKM_9WWDkIFX3bss6_LV_0RaUeckiy-NvHpACKyFFzHHJZTyRXcR3a6YXHsALHp7buZuks5rBKhpVGhMAzmTkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQXAHiSMy5ACoVgiClwYn0KRDxBQZ0ADeYO0vYPUgXsfkq4bpzn1x5Udlq1tsFcjdEMSfgpf-jxnj7r9JIDu31FdtP3I6LiwEYrAXCXAETWQoGv01oVXFpv1JTJiJvj3tWV1KlrOVIIeJmGCcTwGJiUZ48RfaiUmZzf-9zOUvxqDD2LPzkb4yU8ABZ7gheaSOADl9JQa_w-O6aSJvbkOl2_pShML2NJ6mqx08OUrUSV0pd8RUVD1A87uZ8MvK7nWx4w35TKFTzSWrc-C7RhMAeVLLkzA1NHGQ5dvGj2kMtQEliUb2rd0w0VaO8-ln0Ah2kmaAZbH9Sae4FvFYXOTyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6-jqyeJMvIGJnhR44y8bhKucIhWv8So1NLSDpKx10bzckiZj8eg4gqOtgUbONWjMEl1Mja2wjXXyUxC8l0Tjbo72asfKUQqXIBw_12MozXIWMVWfIrl3dUUXQh8XfRW9s_LZL0rw691aU2YXJcMKsRCOFwAsGXqMBoqGPWE9sNTf3l2A-mJszu6GvAulFnWuM7h__g5xLuX2QbwMd6uUkccMhzVITQeghViLgxaW8fHBBiLyAw7YShw2LAP6HI43JIff8mxfl-6o-mnwllIxvJ6ZcJF3lbXH54UrGd77GbWGa7mH6BSiW0FYjpn9T59AX-lG8CsZn0iFm0f_yMAGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VG-wRqTYuzrjnDoSPZKmNKqETERiBOgoiT1YABmewcmvPJuD8l1MWTBFme97ijZuA56B5bucszJ7lypR0dpk49uRo-uTZkzjqiUtD5QxHpRide-FU0fTg-jPixr283xVtJ_-P1XsUMfpclR7xCd0UWc1GiMe3s24iuLbzi7vdLjdskPAzJFpUNllUwQlf20SHwILQ1oOKZCcNyWIDulyWkHAOkJ_GyKtgPGBipGvYZMR_25NmqlA6sXi8_XtkhlddYHGsXwKuusC5sPS5vuYdmq77ginzFY2iUzD2mQ2CoKiYZEfcq7kPduGr3kPjxdTtKfS4lW6LVP-lOPBkVhjXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=fksPpWXHWhelRf6axyRljOQZdRxOE9eZaQnIpNuuKmQSgVu4pzIM4c44FZq_b2DDKDFVkRbbINlVkJFbl2w5FmCRO1W6Aeafjd9Jx-flwLtEL3xt7ONrDa0I3ds-I0n4HJdx_1w0iWTnNUUbswA8cXgcYSAtprpy6mFGgE48HScgbKf5L7NfY1_5EvfCnNx-xUPR25g55qalXJ0GE6q39sfF5A6yQU-oige-TFnMw7q12ADfmNQcBTaTaV5bIHmXHKpUY_Kctjhvp-NThFi8vPmadYc0P-KyA8_6_lUUXsquLCaFL9rd0KrT0mqG7PIAiEZtk6ufjS-_xY9NL6MdWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=fksPpWXHWhelRf6axyRljOQZdRxOE9eZaQnIpNuuKmQSgVu4pzIM4c44FZq_b2DDKDFVkRbbINlVkJFbl2w5FmCRO1W6Aeafjd9Jx-flwLtEL3xt7ONrDa0I3ds-I0n4HJdx_1w0iWTnNUUbswA8cXgcYSAtprpy6mFGgE48HScgbKf5L7NfY1_5EvfCnNx-xUPR25g55qalXJ0GE6q39sfF5A6yQU-oige-TFnMw7q12ADfmNQcBTaTaV5bIHmXHKpUY_Kctjhvp-NThFi8vPmadYc0P-KyA8_6_lUUXsquLCaFL9rd0KrT0mqG7PIAiEZtk6ufjS-_xY9NL6MdWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1AZMkqnve90A4b-VPWAOdsJ_fbEQ4xmQiHSWo6dzVYGMnijvyPoT1ekLRAM2hB7RwH6llUEqqotiDpN8xPPBQwGHkPLBDOBeOrE8W1uMEftcQodkazwNantCoHrHKCBnrGawNoQkcBgZdkzA40cwcxW6bPiFJ_AaH36xrgDlBZY0bYz-O4BMQXp6Q0h8FQM2oB38AewtOvg1QQ2AvGb8rDEdoOYPBBSyduPtCQUZf3JHHDVVHsnnfzQCShkfo4F3ZUhK3gQg6MT2SLL6q4TP6K3KNLkSiRLjEDPnV56_TlIFsa8lWNGlgqa7oBHPgzHjSgIBwEREOQN23V0GYo9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=o3VBxoDvUvTwSlbUfuQQwGJWGs8wbse2ErwBuLnpAf6S4tZxdtcCf8Icfy1VLCVIM3jAXlouwgYFGmN_CvU6bvUCYx3Z3jpBVlHcb_wZxhL6Grx48NfB46_j_UfCuxa0zjC8YEosZoUez7nGT1mWO0ePK-6jkAHlJjX7Xsy7lw95nmd_iAHnqqLA3iY1i_q7dA1N4akihEP97cSGFZ7P1jT1-WNMS_TG1LW0evt5n1_WnTajStZOc3DigAYlaenxPNnYctEEMwT8RgQDZHrMC92Gw1uAEREBu_MIPrqjeCPvkfY1cr0ri2K_q8g1XshEFsJyK160-PXE3hIJz7BmJ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=o3VBxoDvUvTwSlbUfuQQwGJWGs8wbse2ErwBuLnpAf6S4tZxdtcCf8Icfy1VLCVIM3jAXlouwgYFGmN_CvU6bvUCYx3Z3jpBVlHcb_wZxhL6Grx48NfB46_j_UfCuxa0zjC8YEosZoUez7nGT1mWO0ePK-6jkAHlJjX7Xsy7lw95nmd_iAHnqqLA3iY1i_q7dA1N4akihEP97cSGFZ7P1jT1-WNMS_TG1LW0evt5n1_WnTajStZOc3DigAYlaenxPNnYctEEMwT8RgQDZHrMC92Gw1uAEREBu_MIPrqjeCPvkfY1cr0ri2K_q8g1XshEFsJyK160-PXE3hIJz7BmJ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMTbxG5aQIE14ZZx5R15TnDl7BxN4qujm6w13Lo_45jWNNd4cnMY9K404ba8mFm-JWewaWrNm-s7zkSw4D0RKaLQBNDXJGJoxi8gAQIRpM5RkfICyLCDUoSifWmXvjRvD8iGJb6S7jvGZ9Y5J2YgF1uPv9q8LQJY0oihpMs6OLinY3upKPwqXHP-jPzatUSJgtdkmOyzBL9OiSOP7m-hSZ0AJ2l4Fm6FZkiC_gn2ThlDy-Q_aaEindyw6cr8Y7oYK13IrFMVMw0AnyV1VAEAzujQkbEowap6e01LnwPVjNWdi4O-nSubMyQa2-tCO2zP7cBNyGVeDd18X8CspUT-5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7NLNXb_hPRqrH3K1GskQtIS3Y88QiOQJh7mcRQkrI8-Vo_HztvHZqC7-F4L2OyA4T2W0kPPIIGA_QHe0wwwxwV0g9tTfnEmsVGev2TiGAII5oZD8Z4ZCGo7tpAVRuAkFHbkVtFLvXkSZBWDQ3bgIAx3RbXCEiHoc_qrpgg59aYt_J0SSk_m_cUH6SWK83nLV-n1RR7LhLYLX8H3LoP2y6OWVzl08K_YET25pmLszXuKd1qEbxkFF4D7cl6IHf8Rc0Ijjx7hVZZTvGy6D0PChdctQc6RELBqIjIfYoS5fHFKsALMjxBLxe6zf6FGrOW9dZuqd3XKP798WETKGa2OaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBKA4U2RUXJQMME4RoqluZW1ZxwhzEu-0xXjZBew37zp4SOT7sdpT94kAnOU5KBycJ-Md_9CvselBwJyXodkspY9vesLBGWoOqg81uwredZKwTknY6B6K4kwg6Kv-aoRX3QFKbD3sO70oSHw9vpw2sOdieesPPkl3ktzu6GK3i91GweEob-ZSTOCIUnfSLeIfRdgbHtiOQ-C3mZcWCmMwg477hl7t9VCuA-lPZv-uLfr1KKtam5t9fVgSUbEWjTidVt_M1NTH9_8f-P0ZXXwZl43AnIQohfvOWNEn-ELo6JI5pfWryagVfLb_75zV6kAISyhid7g4DUh1B7Lk_4GMFuI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=TMcgKlYZjxqe0vHmhVyQfAgs4Jsb7is0YVKb1UAZUmy5YlgiCQBYmdz8qYcbjxwd7p-udcaHypxJqm1RJjl6_YZLRIt6Q0b-9mXJCOWDZuOIL3rw0Y9Em2v2WM93N3wBeh3Pjgn89J76KBlycxzhv_QNBwCWOGpterdWYliReBnZFsptz54RZ7k4-7diPh_XOvrJRIb1nR1QdPRzKWV4Bcwy4r3gcegfhy7iuV5BzH6S_NeqPexR9uBU-IUD89SjOgDH75tEKMjfWDz_zeUEKIo3UHmT_iUPUjbnNm6dKoNbgcFMU61MA_r0bhmHQKBygpqPxXHW7S6sXxCQtvZfBKA4U2RUXJQMME4RoqluZW1ZxwhzEu-0xXjZBew37zp4SOT7sdpT94kAnOU5KBycJ-Md_9CvselBwJyXodkspY9vesLBGWoOqg81uwredZKwTknY6B6K4kwg6Kv-aoRX3QFKbD3sO70oSHw9vpw2sOdieesPPkl3ktzu6GK3i91GweEob-ZSTOCIUnfSLeIfRdgbHtiOQ-C3mZcWCmMwg477hl7t9VCuA-lPZv-uLfr1KKtam5t9fVgSUbEWjTidVt_M1NTH9_8f-P0ZXXwZl43AnIQohfvOWNEn-ELo6JI5pfWryagVfLb_75zV6kAISyhid7g4DUh1B7Lk_4GMFuI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJWsz8EWsIFAlu9UZDNcKe-xAc5CUtenKwYcXlbWp2cyOtu10PC9hG7rbpDkmIsQuMxI9Wmxoxix3kpkdyG0kCtAhv6tK2MUHIKHvb9AN3pmSDtb3xM4nFoOrz54jtiWdRwUj9Ufq6Upw-OW6-pHcUkq0uQocGmBU4wRECJ1Uqgr16KxsTQhCjdf12YRn0HbGKlqFuzzVmAZ_v0p1PliFNULh6ISm8RKLn7akCf5Wdbqpc-iobcr9fvzB0N1FD7hjgzRYR5dg-Yo2l5DqwGdTbst6n_TCep2trWaL66pmbyhqwWRa-rC4TzGrjHst1bfLoVI3ksiknpyt-e4wlbZ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWxmof0wr-thXJGMDEYMvbuW4UYLPtibz2MojzX719NOFN8-w6zZL_mQcxIcmR_PUVpkxAy1rFoz3qXQsa_X252rGtwHAToL1i1uINaSjkZODdpDwI7Mix7WPN53WQJdu6V5h2LY1M9u6lvPZylLlWoHQSN0IqIkHDkb0dci98Qmg3_D0u42eay3JT9uu4luNrPPQwccuqtnfhLDqLKuWIRomhSY6GsEJdSvnOot3QjILKHKkfKFNb2wbLP0mPw5icT-_JHZbHBTFuEX3aVGhCmsK8aigfnv8ARa7bxN3RqVNg5HWyLXvfTHOOws_iFFBTCQyyyHM9lUhKg4d7ljFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=PhW7uE37lPwq0HmD2v1WRiaYipVo3KEEYKAGRPNYbQVsBlrqFWEkDzSTWsSX8vygOlZB7MbKCPqHYliG8aRHxspEr4xnvYZCbTI-6bZ5uDK2ub8bHoo59RCgVvHDIi0vzS_2kWToRLonxT-8majE9cGg7DXEUN0G2QVcw4j4_DHYjp1O-go8N5XmYWtlT5xIo-ymxgDj0aA1ODlR80brCCNirh5ebBIVoBjsgaZv7wkgY6WO9Ysy1xybEs4DSErAasETPsJi4IdofQdXYes3aoO9rqGr8ACz7DnDQthCCjKi2QiCHsUAysPSJAGHh1q_v_4P-VzeEga68ZK3-S3QoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=PhW7uE37lPwq0HmD2v1WRiaYipVo3KEEYKAGRPNYbQVsBlrqFWEkDzSTWsSX8vygOlZB7MbKCPqHYliG8aRHxspEr4xnvYZCbTI-6bZ5uDK2ub8bHoo59RCgVvHDIi0vzS_2kWToRLonxT-8majE9cGg7DXEUN0G2QVcw4j4_DHYjp1O-go8N5XmYWtlT5xIo-ymxgDj0aA1ODlR80brCCNirh5ebBIVoBjsgaZv7wkgY6WO9Ysy1xybEs4DSErAasETPsJi4IdofQdXYes3aoO9rqGr8ACz7DnDQthCCjKi2QiCHsUAysPSJAGHh1q_v_4P-VzeEga68ZK3-S3QoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=ATKBWc3r8qlEoNI8yCDmLQLd2KbuHOKhjI6Q1R1H6XMO7rd6qewxqM9i_GHYy3On2KVAicR1SvCUp7qoz2ZnRdSk7nxLlw2IqxNue5fOILca6EKajtzKbfcDNd3TsutEym8ssK0gtHCSyzA790hQRk4PQRC5RuUxEs_1n7tDdUAmPtnqavz3vYI3yXGnEmOcX4QXMnQsHcRLJc5ZeKOUYO0hVw-UeBlpGTlZqrbCeBZ-ak76Mu1FjDtu2KWJCTtJopQyhzKVl3Wr4mC3t_AjccarrE4vd4RcBAZ4upLr4OSIAb1Tbsld-QeRJ12g7x2mRb-lMlmkDsBwFGqb7QRGyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=ATKBWc3r8qlEoNI8yCDmLQLd2KbuHOKhjI6Q1R1H6XMO7rd6qewxqM9i_GHYy3On2KVAicR1SvCUp7qoz2ZnRdSk7nxLlw2IqxNue5fOILca6EKajtzKbfcDNd3TsutEym8ssK0gtHCSyzA790hQRk4PQRC5RuUxEs_1n7tDdUAmPtnqavz3vYI3yXGnEmOcX4QXMnQsHcRLJc5ZeKOUYO0hVw-UeBlpGTlZqrbCeBZ-ak76Mu1FjDtu2KWJCTtJopQyhzKVl3Wr4mC3t_AjccarrE4vd4RcBAZ4upLr4OSIAb1Tbsld-QeRJ12g7x2mRb-lMlmkDsBwFGqb7QRGyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
هوادار تیم قطر آماده دیدار حساس امشب این تیم مقابل سوییس درهفته‌اول جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=Nfyq6tE5lSKIsMmLKKlP4pJsRl9PIwOi4bP0wHj4XeTbHH0HTT7u0Kie9THpMM18yRGtJIJjyK0dpKfSC1pcF5rAr3HxaADiyh4gomE3WOr_0oHSHyEsIDStmJOS0Q0lZ67GZg3VRlpkP755LMTBv6fRKMI2HatX10LAU-ChdeQms4Dy32uC2xZn_JGjIrJqMjoLrx1WqvH5Tus_GeV32TxfZ3hcrl4aTTRueszqCiDF-EqD9lW6DVzYaf-mKPpb0YCIV0dKGTl3PFcYbYEi1wgSOkW9MNERQP64b3azV0FMImg0w4_mJxa496Myh5sXOCErGbUevhJfBVoEi1uW1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=Nfyq6tE5lSKIsMmLKKlP4pJsRl9PIwOi4bP0wHj4XeTbHH0HTT7u0Kie9THpMM18yRGtJIJjyK0dpKfSC1pcF5rAr3HxaADiyh4gomE3WOr_0oHSHyEsIDStmJOS0Q0lZ67GZg3VRlpkP755LMTBv6fRKMI2HatX10LAU-ChdeQms4Dy32uC2xZn_JGjIrJqMjoLrx1WqvH5Tus_GeV32TxfZ3hcrl4aTTRueszqCiDF-EqD9lW6DVzYaf-mKPpb0YCIV0dKGTl3PFcYbYEi1wgSOkW9MNERQP64b3azV0FMImg0w4_mJxa496Myh5sXOCErGbUevhJfBVoEi1uW1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهمونای قسمت اول برنامه های جام جهانی
🔴
امیرحسین قیاسی: رامبد جوان
🔴
سایت ورزش سه: خیابانی و خداداد
🔴
عادل‌فردوسی‌پور: نکونام و کاوه رضایی و دیبالا
🔴
ابوطالب‌حسینی: علی‌پروین مادرقحبه برو دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=D4yIDKoAxfknMFVz3VYD0ewrDAg4WoPrkJddRs7WWmdPFjVygO-y-Qrs2PX0uVFCT5lTB9zbd81Y5QYfvli6ZeEIXqULB6dVOsPg6bKJZ4asjNRhLDoOeIaM6gALv-SKXC-1gov-aLx5ljTbmDTVsWf_l28-U6OIo2sv0Blh3onUoJHjDIjxEIRRJ9ZxbbnQu8N7pSJgtN9jaUFwBLcvub51BPqw_gXqYj6GuGYINd0Vkp4mwCaxvSsTBA-ma66nl1qyszkUl_uRyvuK3RzYxMHq3hOfqrSQCsE6eyo-mLaMGKi5NCe_uz7rnWY5e6T7l-zcf1NNZA88jPDpW_TIVDmS3W6SmFB7t1MvlDikhTpdCI_NoeM36XFZogirCza5J_A3PIi2ipCsR8HhXHjldcdubtAhNWD1bdBaGhoX0-bvVfWhNxcQRGCwOQ-yj7tQFMcXgqagNbnOfcWmXvx_2xHPOns1-42rEPYptKzGieljrxqaH0X-Yzkb8ah6fHwzCNQC-8b8Wpkgx3dyEdd40ZRs_2ylUUUl3RSE00h-x8gafsXemnWNV8e_TbY9StdLoa0F3dynX3HFKfyBuKofRESVcvzByvUBOsZWc20WInKku26jPIoXNWZpsKLdeJKCW1F8sFp5H8OWPlp2XVGI_COBwv-JO7uqCgG3Jofbyts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=D4yIDKoAxfknMFVz3VYD0ewrDAg4WoPrkJddRs7WWmdPFjVygO-y-Qrs2PX0uVFCT5lTB9zbd81Y5QYfvli6ZeEIXqULB6dVOsPg6bKJZ4asjNRhLDoOeIaM6gALv-SKXC-1gov-aLx5ljTbmDTVsWf_l28-U6OIo2sv0Blh3onUoJHjDIjxEIRRJ9ZxbbnQu8N7pSJgtN9jaUFwBLcvub51BPqw_gXqYj6GuGYINd0Vkp4mwCaxvSsTBA-ma66nl1qyszkUl_uRyvuK3RzYxMHq3hOfqrSQCsE6eyo-mLaMGKi5NCe_uz7rnWY5e6T7l-zcf1NNZA88jPDpW_TIVDmS3W6SmFB7t1MvlDikhTpdCI_NoeM36XFZogirCza5J_A3PIi2ipCsR8HhXHjldcdubtAhNWD1bdBaGhoX0-bvVfWhNxcQRGCwOQ-yj7tQFMcXgqagNbnOfcWmXvx_2xHPOns1-42rEPYptKzGieljrxqaH0X-Yzkb8ah6fHwzCNQC-8b8Wpkgx3dyEdd40ZRs_2ylUUUl3RSE00h-x8gafsXemnWNV8e_TbY9StdLoa0F3dynX3HFKfyBuKofRESVcvzByvUBOsZWc20WInKku26jPIoXNWZpsKLdeJKCW1F8sFp5H8OWPlp2XVGI_COBwv-JO7uqCgG3Jofbyts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WfNnZnziii-fsi34IeQ45Y_QjqfokES_vkM5LxtYPJUko0SGPiKRlTcvKDutL-h84CxaKPduKuokBdGOShc1oH3OOWpdu2aTKCRlAwGk1MDaiyoqXOL3Gwc0UdQipl8xbnvaluGRr9r88ropH3DyKRA-dn29zN_hSR9tV5UHCcdj0wCLOWOY8pgpyes-RFkD7XGpMQnI8IwkUvqKe8Jmy-qZiLEhii4QDmzEJ0veo6d5iQjSq7n3oqpYovzpHYHuk5ztVPbwPfizaGmC1OqHri1-P_T9W1vyrLthSfkFjA39IgHGBKtLiPaWCvh22z3Y6-b3FnZwdMbVX5bcXIGJ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXDK8EdbKxNY-MH_vuUbHfWtiqQGyAZiwVL2DAJ0tDkp-Q2qujRdIAOZsP2S1uFC0O2dYYL3Pi1Ieg9HJ6_hHt__sP89Z-xAVvjMScBy9tUgxvZJt0GaIBNN9u3Jwjf7E9JbIabQNTQc80qu3OYKLKmN9dT-3EK3jHkhNqxFwML09LLCqg3sjCG-48gEtXJdwtVDPIkgeqCVyt2c5nnJA9TXhOmH67qsfFdx94IycZg727keCdFkmcGAQJRrzopPoV6fcc9BS07UByHF1JN_cMlRqDY3y5L6wvfynoKrVznEKda_oPAcd_ARMjbVh7E15UshuSynPlqX4H9CLxa0PA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oim08Yl5vNxxj_3A0_2CegAJAyn31lJo8c5GtQdlDU-eP2gCjjfs_2_UgkcQbtDkc27P_JP4JwWDIBAUxjW2knMkD3EOq2-pqn0VidfV6AhDnN7RXICKYE6G8Yf0nZri5K4m5mJMp7lOYYYcBJLlGtMC4ytTbQhSRMH1DvHRHmsi9TQSrsA9TL9U6a7JerLc-ufcswK_yqhhkW-VZeHyPH5Y11lm4tekuJhHyfDwJRUkjlOTaK4gAD9vQrW0Z18Wy3uAAgI73_OGRBVFFv_h3crcKHRU6EkIGkAsouticL-nhXo4rvm1GFksAylsJLid2Ig5dkFbPxw_QhSw_Ld0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23370" target="_blank">📅 19:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tziPta3prjETXIn1h37A3mnk6Z-QlxirWX777FX6PaGBEPusZob5uSjjDICUfMwJiTQ8I56YfBtygRMg_SMxq2sBAX8kKVZm3AZ8SCvLjSCDUdGA7t4QtZoJvY_KvcQoVhoWyAgaE6JEoo1l8mxa24f-rYWy5JMlziPcAPGqJBwbMUY1wCOghZPD3bnEmy6S1Cn9HNzJlepk3M2-uBNM7ZGgsscha1-ioYvfJ4XtKhDE8DJR5h3gJ_FWSa5_E-vWFmrMeKH1sOipDHLIF2FRWCPxIoP6ePpNEFWqGY8Qb058QRB4s0dRitJNPBH0ggM8o5YQodSWDY21wlUHEWnzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23369" target="_blank">📅 18:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWpNLc0WriksLCX77T4CJbcAWMvgFlDzNYfBatAgBzmusDmAXTBP0OTN70bJAqLXZCyuUJuOV-UTV_INMDHixY7lMdbYxIvGv2lNnHwhdO5ocgEDK88N2LHDydcd1noLGV2e3GTKjiHZbto-FMgkkNBDAjltUaYqHuhkDvt8Gy7jn_YD7iyIIDixcj8fXZuiNUR8rpM4-GXxMKE1WVfouaM2YtKCFilNiPzphaQiXNoi9-X-2H8ueYL5gIl6j1yY4O3kLmsZIyvy-CEUTSkUCvAx-VkBU5qxdXZNyF8-P6vHNbj_Lb9fB9tLmp4nTcPGMslIV0a0SwiMFDiCYNdXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/INIx_jrU4qzZCdPLEjGisAPv96UfB8Q3qDCw0qtEwqo1Lj3Mu-Vi8I6nGC4oBr6gRvyK0Ix76jJ1MFhiv26FwtxMnPZZvioWpiZIg0xFES1Nw4ktibJnagII1eR5EDtfxq1pJTw0uLFebVWZW1E4M3UAxP5oJ7vzmCeaRhiiIMXBmWYigaipa28pgfY4iPLWyc2Rr6blkinrIzicOV2a42CpRStTmAtZ_IlmGkNw2NMikPcAJsuZy1aW7BzZx-Qrn73lvqRHdluPj4CLyZxrAZ0ncFwyLSRi8DU80VqTYwZIuCZ9FIs_KZyKvn2Qk1raT0BoET8pOnnHngxHFzaOKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23367" target="_blank">📅 18:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLodwzao_R8WHD21tBLDlXAM4eyhPMb54TUEhL9o0uZ-8IeoiKazgNkIaIi7URNBokexwgqea9cmqQN0xsPggG7ddfmhsCrlqiQel2iAwWr3wgoEh4nklFBO5_tXMf9BjxI_hRSJJCBvFYchEmhUI3aqzyMAPHK_E5ImJ5mBaAGulzo85diHZiNqurqYexwwJIbDAgUsvwCQgLk6UvnS0ENO-uG8nkwIT6CxfkSOFl_QiIKjUEd2euDxiJvdUexqfp3CXGFrJfthCCu53pmNCura6Gl3DmfLQLQLbcSJM9exzhcdIO9Tq3vsKfdiSOXdGcmc0WDCeudBnbSwXrGb4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23366" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=FduMzMztLcnOBEwUJvR6vpRoUPijrZqbin-TySdQGActmLTuXv48TX28svPBo_3XVXdkgY9vqEuXu_uv4GubFrylugP8wE5IsGLB90o-RUm_3F6XHvrslUqhRand4ecND_Y2iiOe8He78kZUu8Y2rWkDpj6194_VfG7aqSmZkVPwE74hwzwYLVuMhHo0sVaPU9aVUEbexElkZ-MrB_kJ5MeaPP4XkG4S_xWsGUYjal__uc5eetfC54-SYg1NkvK0TSDPgyf97r7JMF-3zhxb_DuKBTpXAU3GNuSScneSlu1eobovhIbkcM4G-GUY56RpY449fLn-s1z3ByFGS_xzfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=FduMzMztLcnOBEwUJvR6vpRoUPijrZqbin-TySdQGActmLTuXv48TX28svPBo_3XVXdkgY9vqEuXu_uv4GubFrylugP8wE5IsGLB90o-RUm_3F6XHvrslUqhRand4ecND_Y2iiOe8He78kZUu8Y2rWkDpj6194_VfG7aqSmZkVPwE74hwzwYLVuMhHo0sVaPU9aVUEbexElkZ-MrB_kJ5MeaPP4XkG4S_xWsGUYjal__uc5eetfC54-SYg1NkvK0TSDPgyf97r7JMF-3zhxb_DuKBTpXAU3GNuSScneSlu1eobovhIbkcM4G-GUY56RpY449fLn-s1z3ByFGS_xzfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23365" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnWd86O6A2TKtYwaK9FLnw6cxzWOMK0gsDM6K0Ovpr8jIsPm7TY1pS8rsTEuK3VyMJhfByYVA4ZGtBU4XD66DAC4UeoDHyiVNT7UlG2J1tdRv2Xod5KWzSVo1Gsh3RBkkI8XxV9RudUjsGkorT7ABkLBMMPL8bSrTJv56l_H6YINZbAG9LJGmw3I1guMDSDfZOFWdRcAzZ0mGNSEmc61tQHORw1MLOVzQ4Q_Gh9y9YTnJSalH8qeXPR68M6JHCHcHrurvbBdh9PWU-sdTGVoapvU8IcSVrL2I5HKJiHSBsIRpqWZUKvuAz4nm5-J_9AQSyezv2diBHzF5WFDDAIfLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/23364" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sihHzNUjhGY_9hMYiEpCNJ1CQdHaagVEdNb73FpcqWpEDo2Mlc-l9tyPQSU3zQYznX2LylErIb95QbE2h_fl-IQKX29rUm2qcixSkNW4pqwp8lBeMouWTQNo5IP76x9-XyWCEm_4WhY6DBkUuk7Lwq0wKZWXwN6xCFpXnsCXWYfFsgYV_u6rIyLPgTlDP0n8PX2AC87giGSkQnO6enjm0Z6MeiMlFeD6RYKklqc7SSOuQWyQ9AUeV1ovv9dy4WYt5WtsYADIkXIXgrGnGMpgnloBykCFAQ8nSJ16ri2X_ZGgocWzcFMn0B2zGD6ZRyOXt5SgMRpSfCXRK0rzbl-slw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MGTsT5XRjkKVuM4_NCIqrth_KnzxCFXmX1d1YNQSACaaX2kULBhmXI15XO994aMgf7tJ1rz6wiohAePpEZakjnMo8-SJvTjwmv1wszKOGVYpH7RBV8cqr4B1QWKaNA8pxVIMNf17IHgSDZ0H8wYGsIJDhLwuz0n-y5Iv8W_l-OLhTmNcqqQqI65TiulmXWYkm8mUHdkMeDN9Jcqax-xoDl1vS-k_jwYeeUG-0mTI-_jhwD8XQyIJAd4knrIwajGi_WEZQGUHlnnXhuTC_Olx762hTLK-Vu4wR4UaOZsU4edlUcRzYKyTcAkvqNwKFLo5csXACMSdOQtvL0Y7QpErzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23361" target="_blank">📅 17:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f75Aw3-pJAmjUI-31KGiUaODHj9rcHmFqWIjiuN7Aya-4n9nqULBuFv-P88iWN5oPKTE32To977xhv59hEjEhTm77HVX27-cWPb8Lan0XCgR4iZyykf5mOWzSNBSP5UjTcim5qbPGbo2MQ7dx6Mciy8uV0oItXel2t7ytvdIokrBuNhr7auayJOldwREDnq3Ux5cnuG5PzyzBbdi1BZDjbOiwDEXfpRqaP14rP03uNVM5qJoGk1ydJaPkc0koPp6eMTCq4E4eClVcRmP3TWUDP4_XITje9OXTKFUK-MY8w5pjEs6QxVhaYQqzIrWa6Yt6nyY7T1a5bh3zSMadhnrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23360" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mFKbjyIoA6MhyS6_urzLyVe2P-6UXThqqXstgk2eTEgCeVdRtRMehI8jVbzFS9kbbOE8Xtji9duhFj5VHLs7gY85rktiEGXTv_d1KQJk_HtBbjKw8Mp3mH3ah42r4d-v5qMAdYjFSEgzNhHrAZLKEKc5-OP8-TlyGY6E6NoQS6P-TcuTAIQv9mzb5aARB85K4-5bIepYQ7DOiRDW9wLl-XMmgqG2Y4llieI08s55dNXuN1wd6IiOO1QTwt9RSlEtSHTOZiBTOf_oM7EG6c2ZHJXZrHn7a1d3PFErvXEjYU6dIQV16E0zB_MuzkcuUOWLPa6vLnkHFeFYym-JggF-hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNUgpJtLVa8Y37eWc9MN_uY4l_07CEKY-czWth5YVKkI2sqcOgx4ODrTdHGMi_NNkb_aUP3DIQ8R6L-l8tivcnACnguYwp-uFIr0a3Ol9QogLLog0rSORU7QZ8pWOxWuwfFTdMJ-uH5FTCf-Yok8LbfEdvJjsq_LaJFsmI9Pn5mxmcoCyVr_RwlrCm4vTXtqArM5pV4atOuXVF9-u8vGxgrzTAsHZcF8DQlflLqRr1FW-lws55JlAo2RNmG-N6rhY59mKQQQOa7pzTWzdRpLQqK_VuEDO4VUEXC2Dyy4rT_e9k4tk6X1psoQ9Sqc5ypKho_a0VTRvv7YAT4qxu4hWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دوست دختر پسر 15 ساله کریس رونالدو: من رابطه‌ ام با کریستیانو جونیور عالی است و شایعاتی که منتشر شده کذب محض است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23358" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgodsHPVNADsVAZTVGbaITdR1PaiSHfkY9iskQwtb5a_h3rDADdJJTjfegy9m0ZKDHRWQptKRWhMflN6vp0D-KoUrCLf_6HWCab-NJdfDiCwc3XEivXtnICybrnC-68Rr54tA8jzeg9TnSBianA3RTRYL8OobylSj3crKgoIsvhCFrjmWZN_BVlshWkqrZkIy8b4n5ZqtSIGltk00C-CUoDPWNLXm4U0sQ1jpRNcsX8_qlDY8NyOSxAbjd8KnIbZYeK3a9qply_WH954dPLs598Trq2wjgRX1C0BL9nCfxkasT45qnhKzYAFJJhMfW1LxI8hUwYhIOAWyWPkGF1D9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23357" target="_blank">📅 15:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23356">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDCHYxmbXuXTFUYXdzEl8btc9jec9DpQgkmpHkvtzkoKowr2lDwa-FQpb16RJMSjk76ybOFSS72zWHpjzEz_JfffEpn7ExMqh9O6GfL2ewWepxowmNg2WuHUYKvw3KUeyaK6eXaDZ_P6-0jHkyEdiZTqXJLiw_TNyCY-q31PMSxyUZxmhfNTAybM0xCB8k6OSQI_SiwZl0fAXToRfmOsyTYlwStXzWRjfD8sQKuXt6JcbuHpWRjxdNSOcppBd_nDCyPBTfQBSQHZU6wqGKKZdK5WoDR5naJWm-zmuHSXgC6CPkSXjmfhkLKqLCgWRqVpwO-FaAxIzFZKue35Z-TG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23356" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOt6EhmnMUFYKP7deZvWG4Ay5r-GSSg-eyZ4ElxQ4Z6uiTfdmdRh_FJm2papmEw1n_bd8Zyaxy39rGwwBGL4yKiwONTBpGc_j74zLU_yZe5Vv2Jwh1NOfqU36UoufyB2QJ7rUI0WBlkutDMkSvR6MPlNrmPKun-7nAMY9E7b2LXk8KlRJpWsLRXCX6YxIBTO0nR_No3fXVmaWPQ4HnoJ78Jkn4R_Q48QB8yma9Gc3JyiHh52IcFCrxY_pK51SeKa7a1fCJtVo-gMTXXqi7lcU1SrqKdDit7M1ESH5pX4DlMznnYlXo6AXqvntWY9og5ob-Z2EhrgHdjduUnTFL3IkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23355" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SA9vba64TnTs43acVEPD3vr1etRe55evT-L9yWk4bIYJgDz0HhtXNB69oP_Sw9KYQUqYOE0vQq1khqVxthDIljFSr65vXhaCuvTjmHV2fciHXfqpPUVxKPHtj40ueEV8FnvSlqqPwe_WVOXPcs17fMIadsm3uba99hJlOTG4hBNHvutZ5-NScz4JdBh_htur6b1vOBDcIBSBj6u8uY6-TRov9OW6dJe6o2D7P7uGxeteu41ey1uOFJcLH0EKHnbi3bg2eJQesoK0zX0bEcfrCd4FmDEkMcghUFXnTfDCsAsV8BxGj3vxt-2EST_5myN1hD6xmG_DxZBMAzhFb9KeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vt_FS4J1fACbHJwmHK3FsrHk4su5ItiIrDIa_8Qtzjc6rT750FBmjlL3zSA1u-Yu1FQih7e9tnKa5M9f_OYPBV240FRYq3ldsm2ga2tewB69mGdMkxcqPL-amgpyCPMMwA07meF25P-PWESvwviQuPxAPXpqO8mc4ZbTkVJv4gJoJoBKgQFAVYryLXfLCF7WICDpUE4UzulaWk-VDjDK91x3KOcTGg8veUjHV-Fmu4bcHItNGp6uTAupt0JtFJtkx17C46TQhY2p5flgy8U1h9WUx_fuibga9x0VGsk0Jt9Tnd7A-LbN6kEzwUoykL41wUqdvKDOS7ax7pL6Jgo73g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نگاهی به کارنامه کریستیانو رونالدو و لیونل مسی در ادوار مختلف رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23353" target="_blank">📅 15:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAK8pt1c8jooRMsIJRI1RIu3WB6n21yslCQuRHfmynhLXQHjVrWdy_snDrKuHvixPnOVf_oMWKC6OHxGK4DOd8NAl84StUFHp5coP_cc3B5uGQQaSDzrqfNLBSza7k17wkB5Frhatyk31iPKu32J7-V5XmAtmebYjYuUbq4yqtWcQufLuYsVcmI2tSjWoY-hkbt2MhqQN-MOYPdohcTnDSN0FY4SfEoxI5BQvEbNc3BwYNEOsvr9pXUGksuewNeJLlSldY2_-9PcMC8Mfe0HDtQgPQ6LGI1SAaY2r-vK360wXbhdM3BwOJhfFGRF2Hjt2QBeD4nmnZpScAi8CTVYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ‌ملت‌های‌والیبال؛ جلسه‌‌مهم پیاتزا با بازیکنان جواب داد؛ اولین پیروزی سروقامتان مقتدرانه بود.
🏐
ایران
3️⃣
-
0️⃣
آرژانتین
🇮🇷
25|25|25
🇦🇷
23|19|23  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23352" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23350">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IS2LeHe05ss9xOSaLG0MoybOOTtgkr7NlWz44Jr_mnD9sCk_9Edx3jM_cqMpVwqPe2jLvx-0iud58hJ3_SEy3f9f-SYaGRrBCfeok1QY0jaR05C3ttweMe5DgpiHAfiqNzU_6gQFq4zJVjZ4f3PByHg78IskYCpzU0VTZOV_iJ_E1eEvLrwOMXFWcXCO716vUWh4dVwlw-jZUcrYxTaav5AZng-GntSDcjC2RPqmWFbeENnaZFUC0YfVhNZfmShHvSBLDO_0PgYmHOtGODCYzg4ISbWGtrNOMcW59Ayi53gSV61o1rjD-d3i9z34B7POWuX7WDzq3pmMeMw_vh45Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ieja9F_DNSf8cuNX3YN9COWlyOd7XzllsXC9n93oa8LVQDQbfRmyaHxkCOcirDlWfNNHAv9vQJ_69tMfNpNMoVlfE8q3W29IDm9NzCo2aMne2xbyFeqe1PmMVr7ccBaj3Ba133GX_86Bs4Yg74gENvGKMqjMSq_MRbdNsPDlwdocK30sJ-gAHz81BdBOuP1qNqkvrB9Deeorr1IKUtaWR__hXX0m9DKZL1Jtj5qhPEIoknxUWQzP84nAKLHrEFWS1okF0M5bWRPgeudsBrP-5fbE3O1drfa6Jzscw8eRibNZ2JI1KUrl-3hTJmXTyTQse_0v8gp4KlrAxtWBEh92gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
گزارشگر اختصاصی بازی‌های تیم ملی مصر در رقابت های‌جام‌جهانی 2026 ایشون هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23350" target="_blank">📅 14:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23349">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jv7vXq9tx9emx0dxQyxae7Joqx5TGav6RRPKRbPgZ9CQ-nWZICRWq6KtnJeTEysD2LUnU8kPBsaJ0I4r-CsmeiGhKrZYe2nN30OxUQtGca_lragcUDN-h30u66E30SAX3PT727wahlJFYcXbFu6JQgdMESYmw7WWAiXVCTWnBVnzUIQyDJCskdO4HZQqSNJKQieuAbPwxuRZ6aNE5-KT_XVaEeqGQvvEaal2grfVUT_IVl23DYLUv2vXMBpymnksuB5J5-WR1VNKfIxFH8Fe4iQXtogPuMBCiTrdLQzXA2ngbmbUzwbwlFph5S80SmBcue1fvEn5TocQIAgfi4RJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23349" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23348">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=uQaHqD8K5rFuc3UCEbwdeQrzJyrIP9AGCiPDT3pwMgMNqykAwroc2n6F53xGRShqdbvfIAh2Ft3QaSplh9sZfCDqKSWKE1LD6qp7F6r0aF9GOT2HBYxMzSsnXbgaJ53AV-8pkmLAIc80CSiY-l7t1nXITryBM-lU6miniqI9HblImxwH6FQaUDejmNvWUynZFfL4EIbYdYOwAZH6nY6FEY967is9DaiJKMUDS-c8ykIa0nwE52juVzRLdRDBMYJINob9z_IuX_Bey5GZ8BzCmXzW837p_QW1sdsqAA2_DlVJ6H7nMXPm1rb8TJIrUnIezmWs513xTaJ9lvU2FR9VRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=uQaHqD8K5rFuc3UCEbwdeQrzJyrIP9AGCiPDT3pwMgMNqykAwroc2n6F53xGRShqdbvfIAh2Ft3QaSplh9sZfCDqKSWKE1LD6qp7F6r0aF9GOT2HBYxMzSsnXbgaJ53AV-8pkmLAIc80CSiY-l7t1nXITryBM-lU6miniqI9HblImxwH6FQaUDejmNvWUynZFfL4EIbYdYOwAZH6nY6FEY967is9DaiJKMUDS-c8ykIa0nwE52juVzRLdRDBMYJINob9z_IuX_Bey5GZ8BzCmXzW837p_QW1sdsqAA2_DlVJ6H7nMXPm1rb8TJIrUnIezmWs513xTaJ9lvU2FR9VRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
اسپید یوتیوبر معروف در حاشیه بازی بامداد امروز آمریکا میگه‌ رونالدووپرتغال قهرمان‌جام جهانی میشن؛ زلاتان هم این‌مدلی بدون هیچ‌حرفی بلافاصله میکروفون رو از دستش‌میگیره‌ومیگه برو بیرون بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23348" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23347">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGCsEI0RF-7PYiO2AEumGrR0nnrJ9NQ36cKebCNnNVOUivNzFEoG6FPjeWwuZf-ZjhyCMlshyNNQ7VYPYB4qvdxea2wWUhn3tbg5NRyZnSLQhRrrszN8liHfv_e68rzjhaQBvAf5vHah_yG9de_t-a2xMw-wb8KYpKnA9aEDA8_po3cyPkpUBzqaRWEj-aul0f9bMMY5TYVxj3ABV4wvhITLQldPQrSYYLrfRkAJhVQCngvqnZiM2Q4sc6q3htLGBaa6L6kYmbA6MxiVQvcFJECNexqun0QGb8CAgChcbj2Rh7ql1CWun-Ku4RhV3NIMRdRV7D0ITt6i8gfbfYA03Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23347" target="_blank">📅 13:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23345">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HlFVopo23wI6eof8kcww9SNDnuBZ4_tTTxChBTsKUdqYPl5jDxa7hU-wsh5_oa4ssqBTZt4sxxlO5-3buvDmEEX26bU2rwRNFcSYwYOudh6hpGQJbIp5eLupyVyAyV5VhiyMRHEBb98CwxsFmUv1PZzkXBxFFOxrrEWGjFaMK7XDa70OiBqGaZ3Cnopjj41y3lQx6_yVFS3X_jwD4dd0scBBGV-xzo2VHvMELDr3HMjjWt727bHdWGNZKd3EXx1eoVHg9cYPRXAWarxCz14JI8PHnOh1J6UyW0et5ULyNF91e3T2iv5kTWd_6YnUdamD5e9aRWpxYuTfEGQ2fWY3jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/doBLCoX5YTXlCVw0uEWlJ5R4yCfAoO345Nv8BSKzyIRGtSIn03ZgPt5bFndpaoM4vxnrLZUEXSGqEvPOkBJMgpAFgWaAeHMdNTu-sMRLVnbPT0hycNNxiVgkvQh8irSxSpxdgjkAWvsyBeI79mg6mqqjwlG0gc-TNIJw7FnusbZ1IDYLNa3jSsYmurtkBcmZZhWyoGkJzGwZr3YHUhHDGDXge7O8gXzN8tqp_zaqR0Mtn5omdGO3DTBRXNdlD6pafkJ9ln9HEqqUoMjAxPRDPEKQO1JARsWtD67vUZNzgTne0qIvXhJqtvIi4z0zRn_16muzQZ7hCx6gaUevj7igjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرنگار معروف باشگاه شاختار: بازی دیشب بارسا و پاری‌سن ژرمن فوق العاده بود. انریکه یکی از بهترین سرمربیان حال حاضر دنیاست. همچنان معتقدم که باشگاه‌رئال‌مادرید قهرمان این فصل لیگ قهرمانان اروپا خواهد شد...!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23345" target="_blank">📅 13:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23343">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT5tBsPVvTeMXCOHtEHDGwHnST_M8rUUxgZjHdk67Y67ndZpReny0-K2py9donfaDXcB0veir9rYy0L-g3X6qhTYq6Q0vANu3BLHEmtjSXYyMo6TlkJVGU0F3vNVnvZvIGmdjO315FtXVVGf4TyGiU5N-bafXQfr1GDbNsU2H0gT8mORKLNFs6JY2KwqpPI7cm1nbCcrT921oH0LeLwyA7AxA_RG-7l9ZtziBLQuXV1yAHxYPNf91Tzpmjd6I4K6OQgtvNvUYxxSMbdzJmC_tpC0QgUdbueI_7Nkz_7rvKfe2Uw4uN9nDsGR8gq5SD5IiJ2Ziag9fzP2Jv4JQVi-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23343" target="_blank">📅 12:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23342">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLMCQnIyUCg8JMX8R3gB7Ej7oRm0uT6oWE-bKhF8M5Imy9gy5PwumzukJca0Pzoqy3Ksmpbv2dM1kZO3GDfGw4iICNTPt5yRkXjbqdkY_mL0EIQoTOhOvE9AMLeHCQb8WNtkNgmTDn99_pCgErfoquQSCrtYQ0tHzi9MhNan_0EOeWHAyhX1YTMFlEb18TrJ3fA4mW8fqw6Hh_bB-unm5fJoVboEEO8CUR9hIxl7M_dw3C9Lrw0QAny9w_bLvslZEUm5l8W5h3lE3y0czmpvhaBC0aeV3vcz58cNkJGHGEuMDZifuUcj6ZMIGVG3XZw0mpfYORC-pGplHN0OKImx_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیف‌وتجهیزات تمرینی تیم ملی انگلیس در حین انتقال از فلوریدا به کانزاس سیتی دزدیده شد. بنظر میرسه که هری کین یکی از قربانیان این اتفاقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23342" target="_blank">📅 12:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23341">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7MwbzxZtih0tls9HuyntcWu8vQKatBcKu34vQE-iHJcc8MsL9evX6UY86O39m2Be-GjuJdmxZ0sLoVAtK_9Yd4IFhYJvpoox6lmBYyZsPNctsc6_vFyWtY4zgNy4R7dA9zY1ljlmaqp02iuFlG3336YSJ9QY5UmjlHU7EY_8h_4iqXJDtUOOvfxbUqfWEsu-tiy0OIMDR2ntkEYLveAOUNYDaM_DXeSpWqcZ2ni-Nu_dDThKbElc9CT4QfBJF0TumH3sVdiP4F4uLocNzf5DDy6CIt1Ha2qq_X-mZhmhoXj7bPogy8kShy0z-FAAOV6J-VcucvOMGVQ2aMydrZomw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23341" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23340">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ug5o-cpPC1kyM8Us8aWpMD2KSv3i8MeXO9s6aO_PsE7JvOLEiOoPAp4N0-yzmb9nrGczcx9N397nR-JETIymedlTR4pEoUszPps8vH810Skj8l5EIEFCZSiKjFuFTK1TuQ_2-pdrAS8410zMnuIgvciwlIE6AdWx58ZD67J49KVthV_weRzYwmbv24hZKIYACbyfT4IxzByBMhuKqqZY6osIVKZhuFKLhkWN3QJ0dWx4zU-1mMENO-DQ26VPbaq03SADF1zwJUpbKLTLIM3kcXcQ20jw8bL4ck4Ou4YM2VChKSnkhlMP19pmwId52M3hzB3GBUP7uU04kkEpItmVKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23340" target="_blank">📅 11:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23339">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-aM7h08wnkBiq8TGaIx23ReKUczPt8KUrRhurBMKDHYP9J5qysZsb7e6FqcSH93lNKWC-1C2yu2u3pLLtdYL7PXQfPEGylDluMws8bStt88l2yxqyztbPxz_LKbv-KoxmBX8y35-FAS53fYCefk6pwhRwGvBeCnE41FAvnIay_JdL5xzzL6pRvHXiuVpMlxkFKAfwIqREVtKv0KSQhFo3oMicJpY2Bp_A2r2uJQFisuCQvikyIeJVF4HHidXiLey8mbdeBHyh9IlO7JWzNhi1YzFtoQJkUVeXS175SRNQxBfTklxyYuL9E-Z-aTOIV703Ymky8ei6IGxYi6P-vJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 صفحه برتر در اینستاگرام با بیشترین تعداد فالور؛ کریس رونالدو بعد از اینستا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23339" target="_blank">📅 11:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23338">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGmjwARB9zR7j2e9SwYtsqH2JyO_MEBxkcCb6c1Adz1BapqgwhFMXn0MEy3bS-mi8GQ_Oh90aWUSN1VtUCkv0E8IVvBh3FW22fB39Rqsa9jUm9phfDgZOyRTCNXc48bL0XlNFsw8VLjUBCNWSYQSK5Tm6TE70SV9HIej_Xr7i9fEWB7ZzZqm8AOfl4liVcVdx_JxMBx1Ye4Cy8nHPmaVIel0ixpUTlGkvwddOqvL3rJfPNGxe4aFyeEPRVQQgIbOs8eW6VztWMotznvtbSthXNAjJxnrmmgZvxsS9vAeKPLEJreejwxkHwQIiJtQ8PgJPlDrig696X3ZDNPlGY9ahA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23338" target="_blank">📅 10:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUnnCmYfXCs1ioc8C3dLqq00eyuSzOLgayqGKrgqQLuWl-EEgo0RMFYKu2WyX9fF1K-c3oAwDiIvz4JMfRvg8eODQQpAv8zgtCuOa3Bp_aTSkgJgLce0YghoWULdYhXjMheuj12HyPO8dhkG1dc6SkJgam49WLsameKQGajK3Pk1vYVIr9XFz6zY5BFWxflhNFGR4YXddroltM97ES1RzKJci0-2ZQnn4c1TS_jxwSqyj2JJE6lcUo7fPur_rrwHlCm0hrEChmt227wfX6qdeNqg-Vk-eCKnDXlTKeFSygaNoWV6ZUBlMtGKyGQf8tLQedhR3tDavqQwjE9UcDbbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23337" target="_blank">📅 10:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23335">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29987e4127.mp4?token=qsjsadff01T91H1MD3JkP9D3EvGw3-pHC2DIGZyNGzNi7oo70ytk29eaGnvCrJolI079ssFOdAD0Ft2W1T1ByX0NPhlDsQuQlkODx5qRn0VStn0lWkIL0RusJE321SiXg62SmTUkwza8FyGVpKfBNGwNPhKUHWHoHKZMfyT4TujJic45Co4Bi5WiKcHew8Fh6NuPG9t56-y7W1Q-KbkwtNqNQbflkiEToG5nxC9BLnH2Cj_uHCkhYFsqypSB4eWcu-kDw3THfMroMjeiXVWqW5QBX6zfAkPK_wlQFbYh0gBCcjP-pB03qnVqOinqXNkQrFMkIHOF7oOTQJ3VEZMz6rS8K0abxsPYUybI5Ujj0emLSmSvth-Z2NJU7M5dwIV1NQDOZwFHkPdTUoP2_VYCb95PbCqZJR10bw_Ht519JZ-5U-i2yd5fgFeSeU5T4mId-iNysROBi6uluOio_bwInP7-wxlgWwSLoKtbGnPLw-90h4KKShCYn3F3UiAJEuJ9IhVq4yFyu2t7HV-NVs-AvLg8Ge7gwqZQii2AV1MZ-QKUyRkqsF5tF6Kvk9ufXLsStqxowmjN5kmGs8GnZMzbF9Ub2jY_JAAO8EDkGyME9adZVg3FhF53CGgKjQGVDVUE9fycIY-SUlUiX6cZY1ptEFDFrxtIIXm0kWFaGWglA8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29987e4127.mp4?token=qsjsadff01T91H1MD3JkP9D3EvGw3-pHC2DIGZyNGzNi7oo70ytk29eaGnvCrJolI079ssFOdAD0Ft2W1T1ByX0NPhlDsQuQlkODx5qRn0VStn0lWkIL0RusJE321SiXg62SmTUkwza8FyGVpKfBNGwNPhKUHWHoHKZMfyT4TujJic45Co4Bi5WiKcHew8Fh6NuPG9t56-y7W1Q-KbkwtNqNQbflkiEToG5nxC9BLnH2Cj_uHCkhYFsqypSB4eWcu-kDw3THfMroMjeiXVWqW5QBX6zfAkPK_wlQFbYh0gBCcjP-pB03qnVqOinqXNkQrFMkIHOF7oOTQJ3VEZMz6rS8K0abxsPYUybI5Ujj0emLSmSvth-Z2NJU7M5dwIV1NQDOZwFHkPdTUoP2_VYCb95PbCqZJR10bw_Ht519JZ-5U-i2yd5fgFeSeU5T4mId-iNysROBi6uluOio_bwInP7-wxlgWwSLoKtbGnPLw-90h4KKShCYn3F3UiAJEuJ9IhVq4yFyu2t7HV-NVs-AvLg8Ge7gwqZQii2AV1MZ-QKUyRkqsF5tF6Kvk9ufXLsStqxowmjN5kmGs8GnZMzbF9Ub2jY_JAAO8EDkGyME9adZVg3FhF53CGgKjQGVDVUE9fycIY-SUlUiX6cZY1ptEFDFrxtIIXm0kWFaGWglA8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چالش جذاب هوادار ایرانی با کیت های تیم های حاضر در رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23335" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23334">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c684a93218.mp4?token=HqdBirJ6Tsyo21KnXo1adLfnHRhE3BHhC1XXXnO2u4oNfgVzT-AEhG67ZPVYH08f4LKULskOH9F9GxHHfo9z1fIiG6bspmpwIUAPbH6VyEp_Oqaa3TkQOZ-WKAtQgah-JgSmzcPnnpjtQFnyGmYx6k9NkK9-7x3tDpad0zEXIEiiXrzxxRH7U-xwiSBgM16RIWP5oYXSYau_UHqIC5m9a08yCSXeTh_WGjX3-P_fN3TKG2mhyucHpmHXCEY4MlQbJa-cGFzijbqR2uD6thgoe3uhr3PovvSSPuxfIzrJKpHjwduFblTIqC-s8AQCp_UvYWHOD9tU-PLAtrGFqKQJ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c684a93218.mp4?token=HqdBirJ6Tsyo21KnXo1adLfnHRhE3BHhC1XXXnO2u4oNfgVzT-AEhG67ZPVYH08f4LKULskOH9F9GxHHfo9z1fIiG6bspmpwIUAPbH6VyEp_Oqaa3TkQOZ-WKAtQgah-JgSmzcPnnpjtQFnyGmYx6k9NkK9-7x3tDpad0zEXIEiiXrzxxRH7U-xwiSBgM16RIWP5oYXSYau_UHqIC5m9a08yCSXeTh_WGjX3-P_fN3TKG2mhyucHpmHXCEY4MlQbJa-cGFzijbqR2uD6thgoe3uhr3PovvSSPuxfIzrJKpHjwduFblTIqC-s8AQCp_UvYWHOD9tU-PLAtrGFqKQJ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
بازیکنان‌بایرن‌مونیخ چندسالشون بود وقتی نویر اولین بازی‌شو انجام داد؛ منتظر کارل بمونید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23334" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23332">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sF8aSy_v4waDkwE1gH1r2lM__WjE0DH6EVxk2e50JAZNxFKAx4tk7AfAoAD4-XKqw8AUy5ActgOpBJmiF7Oqx3pDA-Ua6cm0Hun5c9MtlNZbZ-aLoLwqD11Np0JGt7wplEWoMMfIRtOw5s7GCsAtRBogwHKH-Gdh5I6IsvF7XRA_U8S8RlAR2Z5bmdXs1I_yOZOcU_5KELYLtV8G5E4qLPvzMNOG6Rfoey1vteG8rCWtyEt65dhk0uMhFZ3x7Wj7P3A-5JjeqiF9XU_N0GOUE2f6M3NRICHWow2RySUzPRUQagTgqHtmZViRY4QtqpDLPl-hHGOpYS15R9-s9tw7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23332" target="_blank">📅 10:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23331">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|آتش بازی یاران پوچتینو در گام نخست‌ رقابت‌ها مقابل پاراگوئه
🇺🇸
آمریکا
4️⃣
-
1️⃣
پاراگوئه
🇵🇾
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23331" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23330">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9xne26RDnwO_cTShSUMp-6DKncxCf5Nuy_klMzvmk-0yh06WzJwqKSCmpjSgswm9nnD-z9OnQnLXgJa8LDngshEI4ZgCAlV5ShSgL56z1lsSMC8PZvGHROuIijBLM3yFViPqaAlzKVto60OgunJ8JtngIfRsMVDSMpiFU-NsK4hJ9pC1uYpq78K05Pbqa3Y-USL6rGIVtRo_UnDysngMYGQTRW1K12TDTgLwZdPb-jyLcH7856yp2egiPyRXDdYpSyHDBy_tkbAYgR8_auiGFXcEWwehUgJE8Q-tkmNYyuvHA57mkiMutiIS-NDyZpgmOP3jCu9VAxkc_NgqEhPxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23330" target="_blank">📅 09:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23329">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=uvOZWvUKWueTuJnM5W3fCGwJYXw_2Eox-VsFNB3ejoshPOCRcc8WJCEnwxQyt6OhR7pfJmvaHHEnWJPhA4D_7YOqOVfVaAa3FI9kDabspKotSRrtAppOFJfyaAdDScICf0L_VEJ4HCm59mPR_0kWnDm9Z4i4gYtePyH8VqZ3Rna3V5SK7wKByLlh4kvL-76ZFVXEIKB8AStSMkapOW5Qyz0ZucgzAyOrzlmsNPC2bxrmiurjQqiw_cNmENVzGLwlrnhsTwxUJG-DzSYIZ-RJGNJx3LlAEdtqIacsblVQjzNO4k6o3o0A2wCiwNF_lelY2dHfHlfAN3G7p3nHn6BCXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=uvOZWvUKWueTuJnM5W3fCGwJYXw_2Eox-VsFNB3ejoshPOCRcc8WJCEnwxQyt6OhR7pfJmvaHHEnWJPhA4D_7YOqOVfVaAa3FI9kDabspKotSRrtAppOFJfyaAdDScICf0L_VEJ4HCm59mPR_0kWnDm9Z4i4gYtePyH8VqZ3Rna3V5SK7wKByLlh4kvL-76ZFVXEIKB8AStSMkapOW5Qyz0ZucgzAyOrzlmsNPC2bxrmiurjQqiw_cNmENVzGLwlrnhsTwxUJG-DzSYIZ-RJGNJx3LlAEdtqIacsblVQjzNO4k6o3o0A2wCiwNF_lelY2dHfHlfAN3G7p3nHn6BCXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تیکه‌سنگین عادل‌فردوسی‌پور به امیر قلعه نویی بابت ساعت دستش در مراسم پیش از شروع جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23329" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23328">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=GApDNgB2avNFcDtPRQr8mcnUu5ZziuMUQiXRGQs1JYJ1lk77R_jU7oQrzbJ2Z5Hl3UwQihVFnd5E7x0Bs0Rnkd1wiFKHHki12ytP2f1YWbufgMYUYhAcpxcqpd8VFgMFCHHTb1F8n1hQoHPAaghbyEq7IG4lkNFAXAP7OfXiSEy6UUuqWOtlkZr35hkCiQE6FtgXA-qBxlOBZF5tfaKXdDQJFGcgqn6OJXWR4JiQEHJ46VjU4wWP3ecq7w8pHRZfLYfOdDFrduMBnlf_DtePOVkiIrRGCez9Eh7dZ2hGr8Bosk0wvzpWz-6NhZLNITa7hbojBM_4FpML0m7uYFTBe3iViuO3pYPtMfcy8OaUycWmRWMpIxmwlK5QcMbCHCXEri95WpSGdJDIrTWy2oZ0R4EpAWy7uXG_nlikid45ha3ejyKGw50IGfR1xsUdPETZz9fmGDbSmYdJWS0VVTy2z0AQQUEOlf1MLZL28LPQOttNamQOKWdx1cUm4A1HZ6Ok-d8ajpbz14yP02FhQ76Sc_1EkWe2hSFfIsCVUUo_IAQlHHLtOEgziiCw6wWcJ-SHKiBbIkTmkCWMb_X1NvyjdrCFHpj_Gb5NJQqvGXf-GdAPEYg0dDC_kkbBU_wjXW1rTn3ATC206ZpUOazUlb_KARoC7ktTJcUaVMVODqZ2F_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=GApDNgB2avNFcDtPRQr8mcnUu5ZziuMUQiXRGQs1JYJ1lk77R_jU7oQrzbJ2Z5Hl3UwQihVFnd5E7x0Bs0Rnkd1wiFKHHki12ytP2f1YWbufgMYUYhAcpxcqpd8VFgMFCHHTb1F8n1hQoHPAaghbyEq7IG4lkNFAXAP7OfXiSEy6UUuqWOtlkZr35hkCiQE6FtgXA-qBxlOBZF5tfaKXdDQJFGcgqn6OJXWR4JiQEHJ46VjU4wWP3ecq7w8pHRZfLYfOdDFrduMBnlf_DtePOVkiIrRGCez9Eh7dZ2hGr8Bosk0wvzpWz-6NhZLNITa7hbojBM_4FpML0m7uYFTBe3iViuO3pYPtMfcy8OaUycWmRWMpIxmwlK5QcMbCHCXEri95WpSGdJDIrTWy2oZ0R4EpAWy7uXG_nlikid45ha3ejyKGw50IGfR1xsUdPETZz9fmGDbSmYdJWS0VVTy2z0AQQUEOlf1MLZL28LPQOttNamQOKWdx1cUm4A1HZ6Ok-d8ajpbz14yP02FhQ76Sc_1EkWe2hSFfIsCVUUo_IAQlHHLtOEgziiCw6wWcJ-SHKiBbIkTmkCWMb_X1NvyjdrCFHpj_Gb5NJQqvGXf-GdAPEYg0dDC_kkbBU_wjXW1rTn3ATC206ZpUOazUlb_KARoC7ktTJcUaVMVODqZ2F_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
طرفداران‌کشور‌های‌مختلف حاضر در جام‌جهانی؛ از سری جذابیت‌های بزرگترین رقابت فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23328" target="_blank">📅 09:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23327">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">⚽️
ویدیویی‌بسیارجذاب‌ومختصر و مفید از مراسم افتتاحیه رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23327" target="_blank">📅 09:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23326">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rK5XIgo69wc5i69DBItrWZ2OXfk6xfdbuoG9q0w6acx6zXM2ihGsMmKU2XcZFbuq59Y_eFchwDgIqity5nvIk0AU3Lg4aVEv6wW3XxeOqVoHvk2tBaV3eXuqEx-bLkzjjg5houbeakpAgcH_aO2LKPldixmYjf5ByupIxBLNmX540QCe2wjtYsXx5s7FSxwN1FUdbjvEIZE-BL_05T1tIVTCkaTUwFUEnBhLLfbMDvZrgr_E49ExzhSXTFPWtR2lwgJ5aL0lMJ60l63qTClvQ_UzufeiqjtGcxPvCdpP3wjFEje6E8VbkyCBv-_fKjvJ4H1BIN6hNtN21YbAPHbwNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حال بازیکنان تیم‌ملی والیبال تو بازی امشب اصلا خوب نبود. این صحنه دو ببینید. باهم تعارف میکنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23326" target="_blank">📅 04:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23323">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wtb0bd_HRfq9AUGEqAbRX4mqlZMFQSOo3OK_HTkBiAQRo3ZvstOsKN6Q_6Oekmt14NfVVYB8XCs2-HN6tC68IQvJ5yetUrSVFBq6g7X4ce6t-6-I3YOqHZgtGu_vxJVSIVzMvLDIlbZjXYFdSq2Xf00akFhdqj8GR1DdHWmMSESouwHvGAJOOql8y3WRSqmQvdbI_Yth4NrJ5Si8evzoIgWokjezZKm7Wh4z2LW2oASL-GxvhEpMxDm4mOqnxaDvL70mSUVsQuBk6t8y8Q3F5AjXIEYbJco75pHF22BhXds5M_f1hsUgSO3LOJeYA0ZfYdCTPzt-C_PohRUaIqBx0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJCqlyjhAYbn9s-f3coDEQUh-WN5GFCGp0Sy_agpMNYrdcz7l-37KaqB3zZCwFPtkv6vixnDRsB-6M-pBCr7Z2eBzW86RiTZF22aPZ0pZ9QrvzHlTs_N7UJVkvULoWjqXwPY7xwXkU60W5CWoi0Y9xX-bpS5EGrbxQvEo6d46qPnlv3CF9kYlQdIxz4LQFK_xouDtl-wK_ylaTB4JR0-VpNlXBv2UTbfA3FH_n8EAaMM2GpeXw7L6N9vWKRMpWbOnPhfVEchuVPIiA6hDs1IAdqd55tUOMdQv5dCKGSrbA0lR3nxTE6Mt3qHBGJMTLZvVSfXRdSkr14D7Nwg_ycvag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
امنتیت بالای شهر تیخوانا؛
در ساعات قبل رو به روی محل کمپ‌تمرینی شاگردان امیر قلعه نویی یه جسد توی صندوق عقب یه ماشین پیدا شده که در حال تجزیه بوده. این ماشین هم توی پارکینگ محل اقامت شاگردان قلعه نویی بوده که دقیقا رو به روی کمپ تیم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23323" target="_blank">📅 03:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23322">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wzjet0O4yQ7_4TjJO8oCdohpDCXtMjjonvq4J0vpwX1SzzaG9YoUmtgMfGF5qJY3dSLn-f2tGISrm_pEvQhLkoCtsULHYY1BWeUh2J9v3Pn-PmRYO4uwkeYvyh2oirnAoYYeLAlscKDtB_Fze_5_u5WBql6rl39TLci2ukDQLTD3ucgAyHHul_csA74shxKdK_H-I32VC2JNQrko1sN9t77bFDMn8F9vtrg80YfyllGXOTxrmt3U3zHvHcMNrdq6VkKmT8L4iYNTVl_dDQ2Hh5LTZ5MYw2uAkI3SB4G4L2gGIbzMsysvJ4ZmywFmXpY1UY_ZuxdY0U3jPv5vurF-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌کادرپزشکی‌برزیل؛ مصدومیت نیمار جونیور رو به بهبود است و این بازیکن از هفته اول جام جهانی دراختیار کادرفنی سلسائو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/23322" target="_blank">📅 01:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23321">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjyOXdawX5ykH2obXfvjHPMd8QOHGxbjjYYAM4uTla0_ZUcH4R-U96nCTcR20dHlhTHHWnEMVmkZJO_O4ap1dMFo48QOm92pUM7JooZnTuZ0dqXCZ9Lf5YrQ5dA0Uj-JiDHQTd3Qkvia4EGBc3YalyI6y7gCSshhRRa7v9JfYSfqZTWFfLjgN1PAiaSjbxDiiat4b3mvQkIvw_PQe0vTNJzGWjolmn16TDDR4ke3yJNuRGNOluw7V3iwgfbJk6oD1IcbRLj5K_f0SielXLdKi-WaoKuK9AKZoSuKuQv8SDY5lL7D7lpkwDjD6boviP456PJdsm7qEGpYOZNjiwWg8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|نشریه‌موندو:دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23321" target="_blank">📅 01:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23320">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">▶️
قسمت‌‌ دوم‌ برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23320" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23318">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F374fxiFLXCXFMb1ZnF83YTNYDmkIkQbSxuQtKFD0OB7rZ-SchRdNhRKbjgEy5HMMPPB0KS3eYrk8zZMagPSUYQaIBMLe9pK9QuMNAnyR7bHIUDfVluOCNA4CRsmmpYPeqVA3_6fDk9Cj9qSoSRafIFVNKkc1fOtY7JKTfILxAIuYZ3hyzjDp2_duqZ3wE0tQiqFkEGaNIjBEWrmNyRrR9BUAGpFMLeT5EmdNDtPIA3LEI6aANPDdoa1OTv3aKpfa3jnXt5x9LMic334lIirWdnUmAgyn0QDZKkt7lGxDXbzfC4WM-kQHU47M3nLVibsoaEVigMYd_6x7l5gDTWZpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23318" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23317">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxH_qa-sZpYkdGCTU7nY-E-7S4cQB-zE5_s6sx23AtuXRv0fYh2Uy-A1ln5NVFOkFfIK1zj7uWvafltUWnKt4Sks3xObYSXCQGGemKGL35BqPBDP35OFJhnyMwjcuzxfxXyFYQJH4TTbOXC_xzme7eRnJNqMBZgFczYjAfsqjw1_Q85CoAPfCtl6jRW1w0ONOrAKrf3_9tBQvIaLsesIPOj4A_tUT93CI6EAZwJj_FguivuiY01tv_Rwp9YZipNBQMMmnfhrXgJp_Mn5v7o2Xx9IsPeHeQ_6BqNxCrz9aIIqUrWffFqpinSwh-gCNJKG_FrKWC9mrl8_nhGbNT1cNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری بزرگ کره‌ای‌ها مقابل چک و توقف کانادایِ میزبان در مصاف برابر بوسنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23317" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ulk08cmNQQTxAlOLzwCDelCxgf1bBKQfVmA1yBFUshYZoqxqG56UhEzgKSO74xa6gUBajBkVvNqq-nhWVDCn8hPe5k7Weuv5R-t5MbFLIYhUwCOumfCrN7AWKjmSOEkYsLiOox3B_Ox7rLc74ijanfAGsze0mjGkCbqUre2jNG-jHogodmnpEiHISXI7l-feqJhGFiQGHzg3JT5NePB0guWtksnJCelhDctRxtd599162YeR_r8je0ZSQdYX9LFojv-n4nj7MZkatxaIQP3iWlWUAdnY52jdqmnXirWJ2qtq4S8ETPoi7aGT7SMajuIaxvWDGhTLnygKoNj_gIaRjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BfXP40OiqXgQYvoopEfY88OcdWPIiZ2QbD03IioQMyIbqow1Rbe2cjQwHxh8MM6yrYXYfDjZ8sQzJzAWiLE_CU5yz4BCSiBmmTw7llZcOszzMrBJXpHqZFcsU7eN4DGXV9Pd3s6R8vd67PtKysDjDMdIeWalaidRKNWMDnXwJcjWI_RbTFdK0YYsPvR-e8V-HBxT5zoYqftNkjYMbmo2a3sUPgNGvFJmNyCsGb6Eog1r3XLNRQU-MUP7cGtKtbp_0SnNEvFJ_ck2W6ZDNgdJMaZSsSohlAERb9RoUsl0Urd4LvApGDM5-N64crhOHWCumb0gm5WgE9TVISO0aWQ2EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
شات‌های‌جدید نادیا خمز دختر پاکو سرمربی سابق تراکتور؛ ایشونم بعداز اینکه اینترنت مردم ایران کامل وصل شد پست هاش رو شروع کرد به انتشار. حدود 70 درصد فالوهاش ایرانین که اون سه ماه نت نبود اونم پست نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23315" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
