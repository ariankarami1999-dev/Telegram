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
<img src="https://cdn4.telesco.pe/file/gcL8uBIkVC5EW2UwA7Z2gXl78py9aeVF-OuunAhkpTkwyKUHdJ4cu3JdhOemP6nC9bwfg8BggkXiE5KB8WXZ3AtAfL4TnkyLeDdLddqVT3WwHI1juIjcmJFat0Vb8dc2L7_42lf2ArFPiMmfCFRI6B2jOYKnDgBF7pE968zcuLvjzr7EVc70dmf5WYJcSbs2UCrx_BYnK0lmiR_EfoCiXsF9qZLr8PwZ440bkhFIJZv9Y_hojEuY_LVTmO6G4galYStAYfWLTVRLL-9EKNMRbfT-GG71QOGp3zIpTWBt3gZU-klJiqEE7ONd17XkBXAjMMwfZL-dvTVVfPNDt4wt-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 191K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-05 17:41:59</div>
<hr>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQspzWRWoNuwZgBBzOtBNL8LX9wXXuxWASyUBou5QhGC1sz6_i99sCXHp92dZXlDChFEKo7aSLlXMd8eUixXc2AZ8aEDpRpnGVRKqF06KWDuLCf6cXSN0c7Wsyji5lGXJtt2X7yxDNacq0qEizqahqvpraS92NejsLlLyeJK8JBX1clkIroIz4kgBDjVZfAsnXTbZEf1Bl80qzfBdpwEpz04cqWv8W9n1x8ersVojL3yv4ZM02kVWgoLKRqjp9skPBKyYn6Kqq-8G2HS97XG0fU_nwDHjyGeUnuYYf7tLnlSOF3h4T7Cs_BXcF7-l-VBpBqgLuWG2FBlp7z90Tc9TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKyvVkJFwJaozxOOlArXXJRDQLuY8bVB96frqJ4UoBUW41tMk2Wu3SQ8I10fPDvcInVPwOo4gt8z2sjtqZZv_csKpYz7VZiO6sSY9v2S57HOBn01lB5Er8AMQ41dFad8eI7LiNzUUOVpDshpZNXh55FKwEmYQPKMCPsxM7k5LjSbA2RFCfpMK_baWoMk1qkf29_f7YaAdh0x59gSCqFoalM8f7mt1w0sXKvVd4CwzAgJglv0QeFWq9Cu5FdaF7tS6CelZX4ELBfyZawplMlKfSR4fjguLdPT0hu52fDYZqcS7BpIgquo4kRuVjhdHK_eJUBs3RZUSzW8RlJK1UmatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=hpRDSoEGXx-67v__ZjxdwQ8M3_svekB6dEYfKFEYzpCU2YuedNDev5DEbu9UPmzY4QCRCJzTbnH1ztaxd6zZb6KTIrH0zT1q1hZFlhIZo30TSNuhHsNdoXtvBGte1cLnpkCeFoLgz0IvAAPV3c91aa2UyhxA04C70-VPQoMQrv1KGpdTnS8zB6C9-I70YZyVTWYZl0bcbOFwgwPOjmorNlJKmVXr19yIo8UGGOqVlHP8dJ6Fuu7r4HQnL_V4bXixftWggAVuNWHEyQgJpxd5pirEmt6YJASmoieUUTAY_-gElvDE4PzOD68PKpoHqtHl8ov9CZpZDEQhINmU_4ONJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=hpRDSoEGXx-67v__ZjxdwQ8M3_svekB6dEYfKFEYzpCU2YuedNDev5DEbu9UPmzY4QCRCJzTbnH1ztaxd6zZb6KTIrH0zT1q1hZFlhIZo30TSNuhHsNdoXtvBGte1cLnpkCeFoLgz0IvAAPV3c91aa2UyhxA04C70-VPQoMQrv1KGpdTnS8zB6C9-I70YZyVTWYZl0bcbOFwgwPOjmorNlJKmVXr19yIo8UGGOqVlHP8dJ6Fuu7r4HQnL_V4bXixftWggAVuNWHEyQgJpxd5pirEmt6YJASmoieUUTAY_-gElvDE4PzOD68PKpoHqtHl8ov9CZpZDEQhINmU_4ONJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6_Tk9DEABSwSZfPFiqgeN4TQvqglwTRQDcy2hpTWPhuVPnNS5sJ7BS2gh0ZQRLU4hFyZ8DyqofF4JiJcsouJ67yoxxSZGijJjz5Dhj9veWHFdA10d1w6RRnTokvuQl1zl-GiCBDb3HAeLHqy-k__LCwN-BgbSbv6aH9BVVlG_HPHENLDexe9TDvNLSfkdnhHzcnkLFPC0xdlX5IWHMBlypJEMTLxY9OZ8b7VU7IPCiIqTmiIPZK2mCOWj4F8_pUREX_jHCnnEtGOVc2Gyzlh5-LkCYmBPiPiwRDpFy_1RUUTvkHrYO-zbMIcDlZAZB-AZvuXMg8x7F5-CmeOWy2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-Qq8-FDSPucly6toQUZgL_yVE0X_Y3kvoVN-1kXa9wnb6bsQXQhj70T5ouWAA8SZSXyrA-1eP1OqkxAdnKulCR6rkd1A2kO19BQCmjBSXjUTTiC8YfPNJoItuJspShRnPdGF5EOpelTmG0imfW0adcAGxd9c8NwqXF3dHKiRAzzBZ-J3Sg6Sfraj3krdujFusD3mYU96AMcacVRI-gIcAzPCA0zJeoNZi4QlpRlPlQvSBzQyLJT1JL0y59qaNWfoVNwbNyjQZtbRfGD-nTLl_Jfzdh1KnnmMEqeYaUPKmfuxRfZN0OMj51KvanqnpM2PfNFZu-uyThTYGZdCvkEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKXlD_yFVnXpDRemOMdZ6Ws9n5DCBMuI_rXPinjdb_b6doV-KfKR1sXf1Ck7qo8mp2faU32LL9Pz1zVlAn_KL9FzkDUFgxBOsSas2pIdCrX6q464BwDH484vNUt9_epXDTUkpU0xaPJPoxi_LQLCSWFondvomYutzwurrm-FwLOo6hV1Vo_xs7suSvIpta2W5i4pDkLAxQMg5IwFShg6dc5u9BYDyDoCixtCDNmf5t7gZHuQUZw7fbGiBNNeb0a37elbEmD48RCgZl4546NOsRwEeaH0uUw2l2MARYAMtZMNCtu9572Eg3jx3wCfrvRK8erTI3_W1Q0sHm7Jy6_SOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a80nVh57H5wBzUMzRCUhUA18sWvotGfLvIQHPc00fcB2kbM5dRl-0LexLla7hP1yIJ80IbxXURdY9CSpVDyUEtrhR4u_PTSk84iMwYVcvxKnBOA9f2j3xb6KpBOGG6Bkn54ygEa1V6yRP9gA_bA-s8T62MHhluDgpqCTgCJ0YrdArZLjEtYjQFt2wQmWkCN9zkx6kRxkhVjm3_6_OSYF0tMs3gTIkgK5qU1jeyOdfgRiaX0rQnDm0H3CvfNLKCH8owU4reFvCNWhNW90Y0Aw2AlLi9g-Sgp8x_GwAUmFK5DEodm2qsiGQBNQP8XfOeczJWC_-4XjpNcaQnq7nmZa1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H963Vu3NoDkrgnC7_mQl63LctZLuiTWtifOxILpasidQPZZwt9srxygykNOZLOLwx_lvJSVWz0xnY9b1LeJDN57id4bANUuy0rbtw_Pe7RqKSgeBcXSUSsPU67LNY6PTayr6_yCRv0ti2Qa7ta8e9toqzyRluxNpezXIMHO4fKm20pHmyTfYAF5rsnyeCV0hkFAZupoA3ygHlgjIhAOS7dyWigWl25gCVoDNtcEbwWvSEeTx9QcZcE-wmF41efY2Eg_Ah8u3xh1gTWiPr5OnAy9N-q4VQWF-hs_nPBNK6RCbi3e8tqJGXq9EoIvsnoqdcKDp3dfPw28o_KyqfCoFNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22314">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7AN6bsQdxJwysr9W0dJLBJrzttwop8O3J0KdHYG0LVsjHGcUscrY1R6tt3nzNEAlqfzxT_wKcqL0FfRONelw8lLNqlytcMCKtbaDaagdkbTKpx2QlhZhP8mS3xdg0Rx4uoGoPUkviEqm5xGJIYcpBX28Wl02myG6VsxnKTpafeiQ2jQU5W45Ly6fw2ERuD6BnK-dM70fsjbWUGlGOUQp3lgmz_oQaA9F77hv4dv7bMvO_KDPd5aNLDfrnfEYgkccLUISeH3DhyEuFbS8AkvWFRpsMSC7ZlBGKcFPCJb5SpAdudiTDVjGwG-bRbh61vTe3wtujo8pIrolQgW__8A4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛نماینده‌خولیان‌آلوارز: اگه باشگاه بارسا با اتلتیکو برسررقم آزادسازی خولیان آلوارز به توافق برسد این انتقال در تابستون پیش‌رو انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22314" target="_blank">📅 01:50 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22313">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbE4zznem_fH5RwVVGp-oPTx2YWjcYeKldYsSj8yFoY9fM65KuKA4s6Q7x3R_L6-gTcM_FeqBC3Hs2En42gNJsKfB3-Hi1X48GCyWuibjE76VEcTsh7ThvA5j9ZudyAeIJm1sdBvrGcT_uQn1D4cpMNJauUfwPfIqm8GkXj_2rAXnfhIGQhbii27TcAB5vV3MZkZlp92GfVu68d_AX-xG6v1QLiGR6Cq5G0c9cZJnf83gKwFD63cZ73mzh_HOysXFpRWDbwSpeLcz3XUprPWZbWc60mGmSCHyL4sk_v2jUmuj9pUkGj7cNrJRuqA0iBUgUKyjhX3WRImVXfGdsMfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ طبق گفته رسانه‌های نزدیک به حکومت؛ اینترنت بین الملل مردم ایران تا ساعات آینده وصل خواهد شد. انشالله این آخرین باری خواهد بود که اینترنت مردم عزیز ایران قطع خواهد شد.
❤️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22313" target="_blank">📅 01:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22312">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVpUPW2gU5JgWaMKnfqD7WxrvTNXJXAKYcRErzOKUNHAtOhDY-njvl8Afs3l5sAE5dzwH12VtFtcbZBSHQvEB1bXjhG0ce_nmsuHA-4_eNKCvjHTGEcVlzvXJwPAESfPfG7NNbc5Sqa28pqFaIVOfvP4031QvZZPowwQWIFcbKDkOcuYgy7YIUB-R_MW8qNioNu36xT9e6FO3Cocwh2-mwYu4Z6mz_Yuv8VbCs6gSQlsRkiF37DluKK0VBhnWuqj9kfK0zCSAU_VxuriXCnOfFUi_1RGh-1P7pDauG7imPWJ1FlBDL9SfMxsHA40pv6WyZur0BcYUNT3oLrdWj9soA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی ؛ خبرنگاران نزدیک به باشگاه النصر عربستان:احتمال‌داره کریس‌رونالدو سورپرایز بزرگ ژوزه‌مورینیو پرتغالی‌برای هواداران‌رئال‌مادرید باشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22312" target="_blank">📅 00:52 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22311">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGV1ORvAAIuBpo9aDOB6EY5VQEONoL4xUwZNDXs3IiGpz9AONnNVq2s7XZC4afQ-JUe24b5Kn9E8iV4ZH8TdExdef3lcHN3ZNT3tLeuVx65AflE9Y5mdmAVsRX8y0yYNzMDrLWRK7PxgmeYVGuhOWD6I45xTm6MIaX4O5fKj_JWljMmCZ8j3lV2sQndqZ5ZJDHmOkzMzLJE-ox5iuVV3P7TlgeOw70ujZwM14eH9QTaDnkU7q9VcHt_CdBtkGEu1y4vTuhfH2YfwgOhGforhqZuX0ihgR4-d4Wm3MUIxlS_HCF0IHjVfBstJ9AD-vmk5MMPa-xflISqtmFXinoIBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22311" target="_blank">📅 00:39 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22310">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KDkiZ40y68WNrm2qC4HLObzKOnpx5VJRQYG12zg_51ePGaxoQ6pguDY5PGT1ZJxVDRx44tFuckbbYnv6AomHaO7q08bVVw7kbo7wEDepPd4Ocqx-j5x9Kn8szswghQZzZXuE-mK82HheFE8GdnsBuMzey-EjE_6dixEJndPDxwFz9O1y-zC3q77o-MEsq2Hj7Apwh23gUVtBBLGz7HM_4ucFwsKTFzx6WFAFhMgccrhVcnPb8SzCmkICp4rfQYwqCT4XDFU03PvB-7uA6hIaRHe1xHGBASy2hKwWhWYsNeo7siS4MXIntumXWCyQoXGLoIgfV2waqGiS4u-eBCJT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22310" target="_blank">📅 23:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22309">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgaSg90UL9xNVM7BfLhlqUV2Hzqi9KRyukY49qeVhUjX_goq55Zt_WE2jAAg5j7uI4UbHqqwR9gjgJFG2crgzxUkHwWC2xr9BB1tSuf4Wp8BCZLL_PClDZ57rGev9hadn8SdcEQzsUkHJlqSQyIn9yklX2_38yj0ntVOOfbIauZpdyJ0bs45Ss4hprKNJZhcX-OFeFMHeS7l3fB6rFvMqDjKfKp-FN6PgNCuieT3Sdiy9MBP1gvskI6BiZHh2hepJhtN1J-JoWpLa3qtme_Hn4kYxCGR0n9VIPgLajCrcBsY5r0yECunPGeLp5mr9Y0ePsPX9JuZ7n65i0JaojTqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22309" target="_blank">📅 20:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22308">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVaayHzAqDFVtNyaLQTis1TN4YlpiLA5pvTPS83sJw-GhOdRkNaKVGxLQAoGTpru0Jlxj0TaSZpOOiPGrIDh73RzF8Mcm9xyga_sx2TGdYg8_hUgfy8mNys8UCX_sZs4t4v_PtkK8G35oNTzxEdpIYcFU0LTqLzGIadiaVYl61aT4QTI6RuLpf5AfE92P-61QiQC-qAA49MCq6WVt1sqDsEJngoOCyMBAvWW3JnYPvXzuNIss9BX5VvQwbAEkAio6K_9j0QxLIBVa4249952r2nnRH3Ie_d91MT0IxmPyV5YmdkLLglkONTl5wt4ErDNY2Ofwu0_-yJlpxqWqwN-Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...ایوان سانچز ستاره‌اسپانیایی سپاهان توافقی از جمع شاگردان محرم نوید کیا جدا شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22308" target="_blank">📅 17:32 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22306">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jb3XVmvW3D-m63EgD6KtT4G2DqS5cGH8Sezo1nt9cYcIANUKD4sl2jor8ZfZcO0baXETvlmA-lXCc63RsOn7k0ym__gtYhnYJEict7DtQgT5m89r5U4FXEk927nkDTsWk3LsTeWYxSJtHdPRIxR-yJ4iKqB9YgsFAHSMAx3P7pU3A0ftgTBILJbXFJz9fhSaqW1iLMse6eEoSL-KwfGE5v7wkpyUNth60f_6WhV3P5R6em5ZT3VaCdbTn3g6dTckYxoP_qlYy04yrVxU44J4oen1hDRH7e9XR9sdNumywJ1c160tdnoNWOQYhVPZaQxl4f5rH4_yNSypGLNKzLafNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vhxrU5QTG612atCm_ShCpV7MO3cVnJ-14moVokUjbdz_6F7I7vyQWTPA0zSXWIS7iESb-sCVwGpJCh1G0KGHZuvyg8om-FyPP3bcnpvDOCVupX-n3KOeAdbh38n5u_0kug9SJR3ZIqsz1Uwe55uHUseUiNSZWMSIEozM6503zFE5ff9ImVm6LmsQje_WatVz_nbdtx0nSEP_K1bbyt_TVheIPA0E7GHyM7ebg-ltztR5S-M2e979KlWIaIaml2zRKmZSHt9x1ibXEpGXsJXxvg_gP3gR8fjpRJ9JgSlSMw7aSamcMJzm0EZpPq7ZpQjIzxHFfNHbbWIXPrKCJgLpiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مائوریتسیو ساری سرمربی‌فصل‌قبل‌ لاتزیو راهی آتالانتا شد. جنارو گتوزو سرمربی‌ سابق تیم‌ ملی ایتالیا با عقد قراردادی سرمربی تیم لاتزیو شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22306" target="_blank">📅 17:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22305">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngUhi2lvlXvvX67VIfABfpe9qaN4QgYGjAi941NDO-cPOfiU567_-2FyYggnNrJfpty7hA3a1aIGto5s7vMICyDxZe4XCZlU-Fpx1WbbRJGnAUMYfrp94-P6RR5YwcIuomNbqqebNc4322FF8AgXuYM3u-ZqoGW5VpjSQshG0Iu1yGhg7CgAxBjeUvrNAG5p-0jIwBCJqTu0L_OKxBj6ZWseuPP5H6M8dZKHKOGeqz7Wkne13ZC-VN1a2aURf3FPWfoESRC44sEGrjlhJFU9b-0pVMRHSTioTZCbJ7Lz5WzkOeaQwJ4Vu2GTa-TwfBivIRFn_HpQVWLkYLA9CbIBrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سردار آزمون ستاره سابق تیم ملی شب گذشته بین دوستان نزدیک خود: تا زمانی حکومت جمهوری اسلامی پا برجاباشد نه‌ برای این تیم بمیدان خواهم رفت و نه پام رو تو اون کشور خواهم گذاشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22305" target="_blank">📅 17:07 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22304">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K65vnVO0lFjWgq9-DtFKMocXa5GM8gpMi-5fi5rAZFIX-0O51vC1xkC9nO6ru2rrFDbovmER5NmYp0v7cPLmKx7ZHQNXTglJOY-Uk6RmT38urfm3Mm27opU7J9EqMyi6Y4ttkulzt-M8iTvpBKV5zEwbX4yZu0E4UwtcmOyTaPpXYEObOnkRV0CG0XwbHIkWmyG427ZxQYE-wh1gP1LbRhIN5d4fqPtZp2RUnHJc92i6ZE2SLUTJzhOg6GmwaWKppSoxjMAoKu5Is6Ehy1hSKpLsP7EJdCEhyy1w3tabzbg5ReQEICoFePYTmaiyp1tYoDJWsphqzO8AvUKNLs8s9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... اوزجان بیزاتی مربی جدید استقلال و دستیار اول سهراب بختیاری‌زاده وارد ایران شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22304" target="_blank">📅 16:51 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22303">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fh4HbxO85NuvqK3O5X3-wdyLzhVx8H-zZPKqW1kMwTFz1RQ3oRs7F7mC_yCGaEHyXP3c388YSQxnKLAZNfpHAnJGrRJok0zHxwVbw9TIAKUbEiBgLorR8G06B2PFU1HK1z7lsdr7MsUhtUT1boQsppVCvrVJYTISSA02o9oygEAskh6m0bniOPkOaTRo_jDgaGa7tblNzNOjiTr3EFEnzlYsme4M6liGq8aRJzb6OdrX-EbKLjozxAhWDDIhi9n_W98QkT7QXwTdHJYX-OCnsY62jtOaTENlsXtlwg8p1MR4p0IlyvGhRLP3X9LpFTVulUXsjfQDnU5t2QG09py7QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22303" target="_blank">📅 16:12 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22302">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIOqgt9BlmbPL9TgcF0xamH5PtW2UnJj1ZNxKRF9K1KjLyuYTzsi_uhv-mEgICIpK6Sq8yTzBOVD50Ka90tgJx171dWwXMJ_-MmEoiNCCJWLFvbUVfPl41I_DZTnUXa53uqhbzXzO2FwmpQvOA3hEbLGen_fNpIL07WvzR3pW_XDlgadQVI1zQ0tg11B2SItxUiyZ1IDhvbdwF1s6KC-FKe1bpaRyZ6T2gatfQAoar3GgI3TfgiZYY2_LdCsJGc8pAUMnvui3_Xwjmq1Q25kYGtsHiZW4gQ-4kOrWPoUJ_rB6FmDA_z8-naYC3YQwCN_nODFzDNkFLXqMkdYFq0U1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22302" target="_blank">📅 15:15 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22301">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dklB2oNczgAsGFngyTYFEr-pLpyyRw-Lkz08uSw2IgR0YgEUd9X3BVYR45UUgMzIiUahbSfWodA-XmtPh7zxBMxUrMuSDWXDRSQOAVGhZP4tq_XrkYWljdFAVGPWIher6i4pmOcWFwmr5jqGZtMUa2asOdiHrNC3AfX6EwmaLkWszrTKvrfKUuEpScjPLAW_-NU6gOfe4CEfVBg6bd3qCLriOT1Yei-XNaJ0D1MRYIBGYCaBByAxIZCS7BKbMOy0dGT2AMzGCFAfy815X54N07fROFGD37xST-EgIj8WkYWgzMX5HoyqS73e22q9KMEcLWfG8nsUC4TfPXo_4MfYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22301" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22300">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtOdcDz5p5Zhcxe20CdURMR0iOPoOxJLveF1hL4-fiFcw10CLtgunPyvxwRGM1VUDSsMqm6sjC7MGijWPtdjTs1Cpt5zTqKM6ss964fPRlOE3vGChXQ3nLIU6WcEnfbM0uQ4GED7Sgz6cvGSI_bSkmwCLc1EUGHZWsXIEMruIILcLl4bACP-GPsTpuBiZgXTdPS4yqcf0gFNG6CiS8zp5NEENWaSGuI5LVBig79sVVKJR1Vibl3XBxFJmCa52VSE0M1RyuHYa3u55MB6Q72V33QTxA_RjY2oPiJ_RjIIPbYVAtmizOvpgiwqcwDjO6uAu9p3VzxdFoHs3GWs3Ng1pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22300" target="_blank">📅 14:48 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22299">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_4G5PAnvdFj43GIIR9cmvtVPF43TqUH0VOnzlfMhY3XmqEfcQoH7p1oCfvAmaS5RmVHAj98eTmpBjUpfsUxT_35LmQctZaTHQ985XUstV2wKBspbXurjFqi_vvNyqPAgm-pFyz_Nywq8e4m2pcw0ynygIW9zu4koEJcFUxHdIJLyZivHC0NueWl2LiWNCrfT6sKpLUzwZB5s92bAmrbUxyjYx146cBUzBI5CDkuM8GTrp0dZUBaDeBMqKxgvdJY4xZoc2qjyZNa2ya6huvZ7LOS8oSjapysZWUiWDcz2zbVcgthE95f_BUTZKMh8LGGuLvVh_qAtbb-nthLMvYcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام‌لیست‌نهایی‌تیم‌ملی‌فوتبال اسپانیا برای جام جهانی 2026؛ رئال مادرید بدون هیچ نماینده‌‌ای!!!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22299" target="_blank">📅 14:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22297">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4vixrqqiG_48vHc6JjDqjMM1F1CLXbDBoqSWaTZdnxI4o2U1UnZLjvOJV7oMb2Jr84i6r1ZAb_EwU2oTAZ1IudhxsASknr5g8Vu6FgJx32WSO02UbyL4XZKIUY3FXhWIIgkM2mLYmoP61p-vMU1vzM_N_Ou_X1gPAr4Jc5H-fMF1njxtOyifAz5nQU_UQOYAbh3jS-4O0qhyHfxeac4DVUoHF_U7g7vnUK1MEkuF-Hcm7N0pSvo8hoE2UFry82YpSj2olVUA5atIi6jF7PVzKueqeb4bxeqLpTzRnztO4ciZuHJD0dOM7iLTYLk49wdEJunumXacTsbTh2utOg56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌سری‌آ ایتالیا در پایان رقابت های این فصل؛ افعی‌ها با اقتدار قهرمان شد. آث میلان آلگری سهمیه UCL رو هم از دست داد. کومو با فابرگاس اسپانیایی راهی لیگ قهرمانان اروپا 2027 شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/22297" target="_blank">📅 14:35 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22295">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpvS2gppAg5faw-Jma0mWi19lFohERPvIN1emdqySLZyiisIdTxpBZbdB3jnmObISKJkqzqh1yvmJpC8EjKotvwVwGA3V8I227uicVObo1gdoL2YdlMt08beI4M-p3GdCciE9mHv2ikWyYJ7GJ0b7tE8EB2583gd3K-mfun6nqstFVQgnNxP5qPomdTP6ynwxIgHXhzBSLXe3TS0Vn7DaTxb2ZX7L6bCSjAQyM-oJwfU7p5KqBwL2EFzNUxQC8WUD9MaCYqvbRKCwbt7Rzb07Dp5oBaPRyXlbzAR8udGFN6kUseyYmPsenmWQm04NAiTamYMeg9Fb1QWSd9zDrTFOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رشیدی کوچی نماینده‌سابق‌مجلس نیز تایید کرد: اینترنت بین‌الملل‌مردم‌ایران این هفته به حالت قبل بر می‌گردد، یا ظرف 48 ساعت آینده یا تا پایان هفته!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22295" target="_blank">📅 13:06 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22294">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xn-j1ieCO0EmtCC2B-hSg0NFH6cd6_0RAnMWU0GHeiDAjW5G25UFs0fXVn-MwD04H9_PMkA3k64f-HMHApAMgWLJxRnqAY5uaULroeI17Pqx0uYr8QJR-U3wTuVb4CgWXy07RJFq2OZus9IHCCALbJ_EVTYKlCaaeD6PWdHwKR14StET4THeBbOL4I6Rvh2g1EMTQMyup27D5MJIC4dykbS5CkcoDkC7vhUqG-YQnto3O4wR0tv5wbC7nxgBWWU5tvN1yshUBa_PjXFByJ59CgsfHoG8gsQeToKN2CW-pvCpQySuRX5VqcZSWUOswLRi48PdRWLtukI08jcP6aDgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/persiana_Soccer/22294" target="_blank">📅 00:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22293">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVj5Ah7J6opTsR-fn1naOGTA3aCEqbvUMJAbVsjXV_7VTdF11INIeM8YQZuCcaPb9zq5HTtjdZqMCle39b1smoCfwygG5cwJv04-UBIhBB5FwSfQjg3x_zBlTjwu27swvjf4TtSYA_rt12hsRgWp_UJMIBU7HKGWvSYf5Gy-X3FwgqtWmzwHAfFszHtyddWUm_3ssEtnc1IQlaNjw4M4GkfQNVEHubtXJm_yaj8Lwj-04s-zc6zHlRKQCo4buGjm2hyO3nWlT72-SfMFNoOcGSgOcIwuYqgz0cX8l_IPNkZDGRKgM_JtFm8Or1UxzVTGuO69JPjRkcb8aTt5s0nBTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛ روسیه با اختلاف در صدر، ایران در رتبه هفدهم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/22293" target="_blank">📅 00:30 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22292">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gg47EJW9MD7S_tCfbIB4mGcKsd01zMGpKkkUKlnn2-lqYzLf6egTd_hzdVkw3lBxci8AMJApXaj1bdOEWyaFM6uBocV1T05lSgAe-aSJqyvrpT8RzcrW1DzQ5GZR75acw6-TtjcDESVlVTbN1le4B2fgsehwr6zQmzdZsCMcj4PRk3N6BwMgyRNM-gs-WtXDqwOnmFIc1r0zsoc9sgw2se6rYqsQ5pqHfmMsxWKaCCmEzz1QznNvvxvDPA7GUaRRgxTPRX2tvTozdoRl4RJGuMv9Sfx5JuC46S5peu4-RXJRb1tl7LecetRmy1sINw2R7vs6aVNT_ChyRZ1j1NaZoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/22292" target="_blank">📅 00:26 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22291">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJwc4NPYGhmdQjALeUWWAAvD7NdsCA5rPc31ce3T-62tIVkoNAGVl2sJ01xshInwVRsYAggKpo-cwNe4zCNgDZB6QksHsqsJPnuxEu6Fw50i63wkN3sznHPZhrM4AMgM-srPBqzU4CnWxJ9V7BCIUazqBUGi47-CyagdhSSYlNklG0V8PpLIoqqSDPiN7yAfcgLdqSwqfIMuMdUU0JhP3l0QSmOhL1OlZVcxXqIy_lovph4WE8clFJFj6wN_g5Gq43YlUldwUEKTvCJ_Bg_8i9PP4e6re-0VaRAHzIitXpUhSLmbhm7u5lE4Rcn8BvLH_jE4Dpnv1YX5_BTKSkPIJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/22291" target="_blank">📅 00:13 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22290">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogstD8REiD_UI-LAML5FFe5wvKGvJ4nz5HDbo52ihTqZgAV0pDK7hHgsDJeCil68h2ndlIwEfy5PHuplenWtMYyay4d4PktROTtkb5WELlfL_hMuytLF3Z3yZMYT0Z359sm4U_vK3wnTP-pj-tAMVgFYrXrurtDNNsOfI4Ftkpsh31rGdv9em4HBN0CW1HfhAReicycRYDI58sQTOk3oU0nz-PRT0oIS6w3QSZ0XLNDSMPlwQc7H7abG9LeQrwDNkNwVNNXNyhQZ-t_NwNxlaweuDrVFWXHlP5wAjtM1PEWVB7RQRwJJdQuYaP0U0euLw4qy5ysX4XdJQxQwOKAoTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|انزو فرناندز ستاره آرژانتینی باشگاه چلسی درپایان‌بازی امروز آبی‌ها با هواداران این تیم خداحافظی کرد و از جمع آبی ها جداشد. فرناندز از رئال مادرید و منچسترسیتی آفردریافت‌کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22290" target="_blank">📅 21:55 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22289">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkeF3-9kCvDFTZstC10KVWe6iIP7FTffFI9nO0PtMykm0mbWlzbEnHg40NV1STih0YrUFl7i-XZbvHAsQC3Vipj0oqTQF4tq7CR558FyUirmF49e2dO6ET9il0SOgZzO0nyIAgWFYGCMcArE-KNfYozcKqq37Fhczfvl6LpboiJUFqgtOfPdjzRGiV9AD1dnkZYCGnSx4_4Gz0lkjtwSXIiNiWIhrEZ9LKMmugXtixI3xeiOMUY8bZU1OFXcGp_TCQUakw282mI2mWxUab5uy4NBD4JPDAsroxccxezwwoJcNgmUGob2KYNJqTSDQN8VLvwSefuMlbXg0WzOsd-oFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
باتوجه‌به‌توافق‌‌مدیران استقلال با ایجنت آنتونیو آدان برای‌فسخ‌قراردادش‌درنیم فصل؛ برای پر شدن 60 درصد بازی‌کردن او و سوخته نشدن سهمیه خارجی‌آبی‌ها به‌احتمال زیاد او درون‌دروازه استقلال مقابل فولاد قرارخواهدگرفت.البته‌اگه بازی لغو نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22289" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22288">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VhEAZ40FuC9D6qXzmVScD2LRTuZFfr6T6ZNTcGtCo42e-a7mi37yPD7gOgncKloRI2Nz11JniVXPpJBYd8jHpar7DiX4Vvj1jqkCCea120lEounCAOrF6EoaSheQK_NDvCQUCuK2MaUYCAkgPOEtx8zK-JhbVE7Jre7jE-TLwkhJSflAqsL37mJozA-WHMKyEuaGOLCrOWXhuiPFhljis4Jevwnn-a2iQ2Yn2ENhGYkJVsvyvTFenly_sVbmoz1325oMVmQCFz_Wt3P3L0oZ-Ht01qyLrAGE9h8PhCtVhItHncNlXScNv6Nb6KWHGN3YUo5Le1yKG7s1C819WteilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22288" target="_blank">📅 21:52 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22286">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQrhvuit9mElXUmd-X32O-MmBP62TJCqGB7tRRlo9dfkRYSt0SoFq5w1kWDUNy7B7zw__1wvwFUtb64W-1RGRxbAQOBdoXX8QxOYHsLDlV6x5KwMaAcrkLQNVLanuRCtP94LMsCWyS0wf5ahZKRXpPRYsAm7Zhv5hR7-_IfnVw-7ACQzEnFp6aKeViqhXEa9fK7qXT0X84z2ThZ-hI1dSg-bF43PhshD22V2IY9dT2ccapLmhhmJmrIGIx4tSamvLZ-ZNUM4M42duF_0nCXF9YcgAvfqrGgn7wZYc6dQY-VSg_fWOzqH123fFvlqnac8iFn4vgBLdsQbAH6ATS0jlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22286" target="_blank">📅 21:10 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWq0pr90AmjyiVIAye39uOuoBrGsrGios6xAzlmwWyIrEqbgue_grelrhMEotQ06y7xfjseDHiKXfqsJddv9M9yurT_zUoqhV_5b-iiF0_mnS2WLPqH3xq01yVcdHTBN2QYnGfAAuhoIbL0IcvMIh-N5_ownzREK2KAF4Us0ooiRR_qiH-e_-OqlESZZyIG1Wmw-tNaUptYANXF5dKVBBSKG0e_Kl8u7HwO7HuKDbaAvTmbPYL0WHNYllCKFlEjS2-JMOskHmN2vFf0M1ORcv9RBAzAiJVNMAov-Jz-vizpGaR8sZ-oVd1cPF_oVi8OhQNnxNgnqKYEZqF4L-FCPyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efcvT9EvAjYScY8FMiyTUXX7vJY4Z-OKUBDyk8Pqlms1Ue7xWLpJzrpSh3faekZSqL4sQsAq8_vH0gaoLB5I331F8k3w4QBJXm7iBGhbYc30y9f6upieI7SvjytRmj_6HNoxUSGcd5abQajXBHCmoehEJIdGriGCVG7tuUBUnTJQl8TCl_4LWjqTNoBwNEzCrVgIRWqd0QjeyOif6p13qRJiH0ojHd8qOPMIiP7L-9RoCgwfhJ5_SCaF_vmjoeybUE0pv6cYme_vepiB-kbkgCcQJ5HOUWIgt7iTmY7I0n-hl27HGYcCRlKcUuGHcpgZgn1ibKEHnA3_QfFJcp87Cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22284" target="_blank">📅 21:07 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22282">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VzvmPHpj4Jgu-RbI3ZC-E3DGwTyqb3n5rOALCCJvN7343Zjkyc7XBZ07JbD_4yUF0o29sqzqMiVAR2e4c0NdCn8M7Yz8xKh5p22k9uedI8Ju_t9ATO22qfHLNI84EoVzMmmg6eQ6D8qAkZYSdqDjf4xk81wsHdjkP0Wj7E-ujje9NhjMThtzawNfr45hWgf2Jf02Asu-G9MnqIGy0hVauKEHJvvFsBzzhG61vNnRxp1pwoCtOCGMcHQ8v_qgVc3VG_DfTC0y3wvt9VjYb7xN5lrdAxY1E2XbIa39OSROgrtD59F2iTPQzSo877lfno9vh20968Cx5ExmOrQ8e-dMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKWCBnOI6IYqqtyxoUC8rfTiKzyZSkh1jS1cUkG2RvagL10EEuPq4bnRzJg2q7kp518t9yzKUjTHpa-7lXtqj_u6vT5Ne1Yf1tXOpYX9pL9R9LNoOlZSb85toidu427VevoaLXbUv6awLC5MsIafQs4t-dEomLXDjjLXTdhDFhFbEHTceKhdvybga-TyMMCpSTqC1ML28yUaeUVHhplZKAwTTZ57jAplCkwRKWIQNZNMFcW9oRzp3A6ENlsBqeyMSy9fe1KnG_pwbrVbmm1jH1GTA03Wq2ypVIaGpF5iKbty17m0X9c1-1u8TuRNruZdfTdVzf3stPStgrz7_8mBMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جدول نهایی لیگ جزیره انگلیس در پایان این فصل رقابت ها؛ آرسنال قهرمان‌شد. منچستریونایتد با کرک اوج گرفت و ازچهاردهم جدول به سوم جدول رسید و سهمیه UCL گرفت. تاتنهام از سقوط گریخت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22282" target="_blank">📅 20:47 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22281">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iV8JeMN8mtzo_MRjadz64Q3UVAKYQiN7uHisiHpP1F_p0Q8Umo2JpXiyjT9JWwtfc59SNVu3IJYwSQB5DKUTjchnk_0J_YZeizROIViEQSXrtavmFWpHNm61QFyQGsVsiBvnd2wYE1vJybVFGba5iL9Kh4lRL945yBxjobLESiwUmOsl1xvV5QUl-vLPzGvUkMQqQjtlI1XhsCr7b_mMiLOw1XRZ5Lz8ohIx-D-xHwbZtPL3MTlKnnskWVhmZvSEgHCICpoC4ZRaUdWGLn_Fl2ZZkPbagb0lbBedGH3oNHCncpIRfAXOGJQmes-F0YuV5MPcDY7WpsfnZPQDf58AWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌نهایی‌لالیگا درپایان رقابت‌های این فصل؛ خیرونا که همین‌چندفصل‌پیش‌سهمیه اروپایی گرفته بود به لالیگا دو سقوط‌کرد. بارسلونا هم‌که چند هفته پیش قهرمانی‌اش قطعی شده‌بود نتونست به رکورد تاریخی 100 امتیاز در یک فصل لالیگا برسه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22281" target="_blank">📅 20:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22280">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pf-CMpSMBqMzlT8X0SpMzXez2g0RXq6UrOJzjdu4c6wgz33sMloB5aYXHRssCaSeZqjIH9XTOBmAa_L7fbuJVsynGw16SykXr7bM3U7ymSlVy7Pz4c_hajvTdwXXlsCJf4z5mPhxBhu96b4Wl8lW_oFjG06t01scX5fR_qRACxpyeoDroxpD_aJ7Eo6093RXJ1yQ0FjcODi3ZBLE5UShkJzeK1U_X4WuETvP50wq0CFFFkKCNIsTHC60MzYt1YtAFtFbwU47tIBodVxthZQeSvD1r_ENIWRsSvlH9z7LYeS3SGYe-TlPwi6_ZcvobQNbxMguTx86KtquX832crhyCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ محمد امین حزباوی مدافع میانی 23 ساله باشگاه سپاهان قصد داره از این‌تیم جدا شه. حزباوی از باشگاه پرسپولیس آفر رسمی دریافت کرده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22280" target="_blank">📅 19:32 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22279">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0_0y0DYs4MvpAxOjV62DZkhxHjzoK_6U9Ih1ku_8dRVEpIXd8cULYMUi_ggPMIM_W_Orl5h7Vt6SNoAvzI2vlOCxUCiZCcrDMTQHGggvf0pSz3ElBwurupVlGdiQrt0AUfAS4zVH-ngKZFhVB4wXn7Lbg7j16XCDQ0yuwGqPq38EFJi3dZJ1To1Ly-SMQqQhMhRbiHEhSWWUJyDIZRp1IE5JI12Gx1dtSRt9fWIkGUKQWJKKwW-_OEm9x2G83YTqnGZRn5Ym8_ipliOBqN0OlH2UwH2kqruOLKTGdwneKSrnw0mKi-n0FyY7cP2NmDMTA_dsupbGWukhRFb16Xr1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیتنا پایگاه‌تخصصی اخبار اینترنت: به احتمال زیاد تا هفته آینده اینترنت بین الملل متصل خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22279" target="_blank">📅 16:38 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22278">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jib0r3nmG5KrPu34vp6WeXMx-eTbkvyh6mqyNvrvjcEXskSr8Z4xL9Yhd8CXT-6m42yrYPLSsvRVVf1IZ3wfzlUTGuNpAmF-LhXMDknpFADPNKu-QwOVnJoigAdgHCapcp8Xkp-TH4wi8bpggz_3hwnM1Uqtm8d78f6vT2BWH46RkokKne8EZpMtYCS6X0ip1g6Ye5ZcIn2eplzA54c5ATiRW6H3xhRz6xk_vysfPKOZ2GKAc6BYWFpWym7g7ZinoO8DUDJanD0eS9-9xvbf7y7arYnJWo-cnAIMsI0gTEyFbZPWDs4fz3EZqCAo3EYgOySEZSY5PGttWfk05VzOyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات
|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22278" target="_blank">📅 16:33 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22277">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lchyoPnpXnGz7sZx2khz5wycH46cWsRBJzUACt9apqkmA6AvIDNneDWwwb3aoNiU3n0fQln8MkVZ1hcIEnOzm5X5tC9WSS3apcEjeyaFbCoGl-igZ0LXr5Is2giH8-TRCV76Z6hQ4UwqGQ7yynTHG5zASolP-1LjEDOEDnmPyECrwp3OxFZe1qkd-r2-YFe3hVv523kkp9xnBFptFqAcPuLbyzNNlyu0et0HIQdJ2WOTMat7fh99bG1PVE235paPi_TM5u7bvzH7gD7d2J6eAoPr8FLZJFUcQkfEFnCw8V580-OTODnQxAHp8U8Z2sjfrskJOiZelowAbFNTF9noPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
هری کین بازیکنی فراتر از یک مهاجم؛ توپ‌گیری، حمل توپ و دریبل، پاس به موقع به هم‌تیمی و گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22277" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22276">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDwUy12IktqiT1UPP47dU4T4A8q7xbrrRI8nAlgwnh7qfaTm9xc2b12VfCZDj5a7WXeNF2dQaYrvesoSYs1kKb0KBWq9ahlD5j17VeDpi4AW1-6i2qV1VC_OjnALPe1Fqz9yVY6Eh_FbaHcja3PzSnUiDClgAMsekygutuly2kPZqVEQIG4X5JwnTUbUDKKl-J-Rn4N8Xm5PQYtiHqVyvaTAMdS7FTOf996dZhnj9ZrcGxJ4swhWFBmPUJUOmaL-PiPjk3hnJ4lDM92fWS0L4ol-AZkMhJ32TQY7UstzjLSsfNf5hHYrLnFFcjXp5BN905cqJmTPCJXdpx_Xps3LvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22276" target="_blank">📅 15:54 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22274">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb3zsLlwcas5wdAi3LxwIH3DkvhRtyaqzamJ37yid7ajx39IOBnL0prVFowt-YOeG7cyK1VQ0pKlOBrrf5ZWE-Veoy6niqcCdAtJszfVoNoEnyJ7GUWthBx_S107MO-aOz4x4z3zXuhFwv-u04eXQCMYMqfGh7iF9_M4X0pqRcakHyDeEH04pq_QkEPTM9GzKCvBd07nnYO2Cc9WglXLoCVJ036N_jWtOxolpGdVI_IlfTtebl6XnUw26TJlQOTMK2EifKD2EjVHRvFoXCXRwQHwdgGg-mOvGlnog9hlV3kfp9VS3ktRj6forpS3SrvYZbUoZxqJ5R5wC4-Z6FqDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌گفته‌‌روزنامه‌های‌ حکومتی: اینترنت بین الملل مردم ایران تااواسط خردادماه حدود 15 خرداد وصل میشه‌. حدود 2 هزار ساعته که اینترنت مردم قطعه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22274" target="_blank">📅 15:29 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22273">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQIyZVAAvr6G_ffOtr0bgseHvtZcaOwIse3CIuIsqlXIvb3vl3poPZmKd0OhzfaJRZqrvQ1NP_LzDVZQRQywUAoaCwTacKvtk5s23RIIRfJnCXzZcezWWq7juxmXGk8rQLxrXASAD1LTRsySgt9ygjq8XGPkmp2gSTOXZKfCJmFDD80zUqyZEY3dbSjGdU4TxIF6m8zdJjL99O8G5dKcLf1xcHr_VDlidGUQFxkNuLJEqmIc9Zj51g3QMhvQFafwiH5hEP4MyB6MhWii8jtWXElYIi9505JZjs8DOfiW34lCJEfWOoqCQ-peFccz0xaK9LTD2Q1gzdba3F2in3l7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ادعای سایت فوتی رنکینگ: سهمیه ایران در رقابت های لیگ نخبگان 2027/28 به سه رسید.
🔴
باشکست‌دیشب النصر در فینال لیگ قهرمانان ۲، حالا فوتبال‌ایران طبق ادعای شایت فوتی رنکینگ، برای دوفصل‌آینده‌بصورت قطعی صاحب سه سهمیه لیگ نخبگان و یک سهمیه سطح دوم خواهد بود. در…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22273" target="_blank">📅 15:01 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22272">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rOB_2RKZk1ceRxsRheXyEA4aBZQuuOoYxtV7HSM9iie0dHwAFHrfe1vque5fRnLyqBXkfLcLjZcTGZ___jXPzNMBvxZCfPapf87eXSmQKJ27lIZ1_fTN_MyisK9Tu3fTBCuPoeFVz9tktmoHvfZZ17W8wLjCFhxsc-0i9PiY8-5FrfLmvgq_m93tUc8SrVVSobWmqBP1fsQ4zacyOQBwrIIK1LiOFKGASnMW2Hvrwv6VAHRh18Owzcz8HMofB-PTtRvF6HJtn8DA8JfhtixS_LOSG2L4LPY2lfUXcO9hjhOiQsRCTktrCWLaldSdQ_fVItosRp-hHqs5z0iJ9KIjHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
درحالیکه وب سایت ویکی پدیا از تیم های حاضر در لیگ نخبگان درفصل آینده رونمایی کرده و در بالای جدول هم اعلام‌کرده این جدول غیر رسمیه اما برخی به اشتباه اعلام کرده اند که AFC اسامی باشگاه‌ها را منتشر کرده و برمبنای آن اعلام کرده اند که نمایندگان ایران از سوی فدراسیون استقلال و تراکتور هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22272" target="_blank">📅 14:57 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22271">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=AUk7rjai0mZkkm7W0XMvkVrp3tuPtTIMR440o5r6f97JVqMawv0cjYDjM65NDNP8hVPugiaGVXa0s3PCpfOt-Hk3fx9Ilgby-XV5-01Oxz-SdeGbLo_zSTn2FrlIvuIZ_JxMqL2LSMbHvqoDkMD2s83MEdFG8NQDnN0HDukuIee-nRK0Utfwa2TouI1CuvVBlciStWj0Le0_m54EtBbXaW_2KyEwFhJxpwW61OmMl-T8B9wwg1-92ajL9e3r-MAeExW6geSnFpP63yGvIXrcqEU_Obqwz0eve5E-4Tp61W9Uicj79Za9j07xjdd5t01tmLypAZxiKLu-q-p1YhNhN1ZnUUZ-pHB7fJUECNxkVOWGcQn7HAjdBSS3VBLFGdWOwvRQSh7otrrgvZ0ovbQhFklnzZYAjrekOaALV-Oat1zRwMwfRt72J6WBvqlkAZXefh_vwTlEiXzGeTxWo1agm5huctU-zRkLYffUnoReg-0BHaabvTOfH6sFlIuSKdp5o9RvUVAN80NJjaMjIVtVz79AG-CWXDI_elHMqpw9QbTo5TO--svC_pDuvb57-yVsWJqJ9w9M3xsGWRtFqSClm9SMmOIaqKJnTXfpITqpcDhRCVsBwv-fU0OEjl78ERaHeDpdIvjwEsBzoNA8-rrQ3hLHpistebEyB0SoADT9Lpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb874305eb.mp4?token=AUk7rjai0mZkkm7W0XMvkVrp3tuPtTIMR440o5r6f97JVqMawv0cjYDjM65NDNP8hVPugiaGVXa0s3PCpfOt-Hk3fx9Ilgby-XV5-01Oxz-SdeGbLo_zSTn2FrlIvuIZ_JxMqL2LSMbHvqoDkMD2s83MEdFG8NQDnN0HDukuIee-nRK0Utfwa2TouI1CuvVBlciStWj0Le0_m54EtBbXaW_2KyEwFhJxpwW61OmMl-T8B9wwg1-92ajL9e3r-MAeExW6geSnFpP63yGvIXrcqEU_Obqwz0eve5E-4Tp61W9Uicj79Za9j07xjdd5t01tmLypAZxiKLu-q-p1YhNhN1ZnUUZ-pHB7fJUECNxkVOWGcQn7HAjdBSS3VBLFGdWOwvRQSh7otrrgvZ0ovbQhFklnzZYAjrekOaALV-Oat1zRwMwfRt72J6WBvqlkAZXefh_vwTlEiXzGeTxWo1agm5huctU-zRkLYffUnoReg-0BHaabvTOfH6sFlIuSKdp5o9RvUVAN80NJjaMjIVtVz79AG-CWXDI_elHMqpw9QbTo5TO--svC_pDuvb57-yVsWJqJ9w9M3xsGWRtFqSClm9SMmOIaqKJnTXfpITqpcDhRCVsBwv-fU0OEjl78ERaHeDpdIvjwEsBzoNA8-rrQ3hLHpistebEyB0SoADT9Lpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22271" target="_blank">📅 12:23 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22270">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rd7-g2KyvljPxAFT-tzhZxZmRpkyzRS17AJR4Bt05nnLUKZUNbWRC6r8zsFeGT7qHb1q5ok3RrEzOLVUhv5db5X7mg50Cz5EvU-WQd-5bBmgAMeS4JQo72u_RI4wQmbTeWtAAlkjOnOQkyXbmbOQQD_b0RRPXpCwnP5Q4f26l7Md3_eSAxxIJgHBFa2Idj0KvAjVU00qIrYG9BizCTc3WKYHbkgm9Mu7eCYi3ra_iR9vsDX9OezTEYKkhj9MkKXyHPALrx_BDMY8dxJ7B5vgtnq7qHzxx6ivYPwbI9YEvAAyDBPq84VN88NshDnklaajBsnii0eXoKFHgWrCwc8-1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دنی کارواخال کاپیتان 34 ساله تیم رئال مادرید امشب آخرین بازی خود را برای کهکشانی‌ها انجام خواهد داد و رسما از این تیم جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22270" target="_blank">📅 12:13 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22269">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=AQADbMb4JHlv4A3ochxZgHFAhUur9fHFWPWcDEF3XEOfmQZ3tYwB1mM0r6x70s_EauFzILUc-2mxNcX4Onph6qaT2bdhV7gp0pZv3fKjI-cn-xKb1zbBf5JyzYSgttJ4OZJI5pbP6y5pbP5w2sU8p2HPirnPTwkC6_JpMGhqW8BdCgYqki6AO5QVfJjuThqLvC-r04u7NIYk04yAhHvBgD_IdB8rzEeGgmdJ_cO3uEd8aAXQCQj0bXB-BKK7bO2imeqmGW8KvqVJ8L_uKugd2LJOLD32IDbzCT7iyuV143v1KD6sidoNJeD02TtFp0H2xzUY6MLYFDyvY5Xicf1JXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=AQADbMb4JHlv4A3ochxZgHFAhUur9fHFWPWcDEF3XEOfmQZ3tYwB1mM0r6x70s_EauFzILUc-2mxNcX4Onph6qaT2bdhV7gp0pZv3fKjI-cn-xKb1zbBf5JyzYSgttJ4OZJI5pbP6y5pbP5w2sU8p2HPirnPTwkC6_JpMGhqW8BdCgYqki6AO5QVfJjuThqLvC-r04u7NIYk04yAhHvBgD_IdB8rzEeGgmdJ_cO3uEd8aAXQCQj0bXB-BKK7bO2imeqmGW8KvqVJ8L_uKugd2LJOLD32IDbzCT7iyuV143v1KD6sidoNJeD02TtFp0H2xzUY6MLYFDyvY5Xicf1JXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
روایت همسر ناصر حجازی از پادرمیانی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال بدلیل تاخیر در حضور در تمرین بخاطر تفریح با دوست‌دخترش
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22269" target="_blank">📅 11:19 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22268">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSTLzKAYsB3yuIbvvhzlnT2A7oyoefO5SnG5-N6h1EcYxdqo1jsJ7qU5qckWYLYoqYY7jLRYv23L2XC-rFsWiIu1JQD3ZrEnraUcNCydDjceazIvlMrD5sWMN_2ykjQGMKJJq01LH7QOIUapZAkO8UTKLTxv42zLjX5pKmV_tIZHgaMAW1UQ4jPgPauNdCCeJHvnkNfsrFMnBQMTYJMtb8msG6GbuNvamUeT9eqPdTgm4b2PHNkpnkm9BVi_FPNdhdw3TiDRM2ctTCWoW-CudhIa6P3v9q2nR4PQUuQqDuvxLRrkpnRsYC9IbMMN2NKL-If52kctcaMg0GJql6E76NdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7265d2cc05.mp4?token=PeeMqGk0hR9nyniq1t5o5EtLPKVcbAYtR33ZjujhTj30-5fH_qrPj2gxDqbAr0sC6XyShzmsTuVba1D-5rH0o89xQoyeYsSFlEbfmDoUt-pVjhv-IcbUs6sF_DwJ_FXx5zSyldRQ5oyEnTrHNcUn6bsikfP-snG7lgSuLBPmU3wgY7K7sb5kdGLN18WQZsQQT9kIFmV3RPe9xOStLe7pWizZOXO4FrDCAdj9Ye2Lw3N-pK8gQ23GWCZxqatPZd3nAl82UjpSjnZgWF6vbGIacR2t3_HnW4K3m-PDs5awUNZfPgKmgR6RwYmcXYKf7NO7UPcOkhwwv9SILzT1hiqQSTLzKAYsB3yuIbvvhzlnT2A7oyoefO5SnG5-N6h1EcYxdqo1jsJ7qU5qckWYLYoqYY7jLRYv23L2XC-rFsWiIu1JQD3ZrEnraUcNCydDjceazIvlMrD5sWMN_2ykjQGMKJJq01LH7QOIUapZAkO8UTKLTxv42zLjX5pKmV_tIZHgaMAW1UQ4jPgPauNdCCeJHvnkNfsrFMnBQMTYJMtb8msG6GbuNvamUeT9eqPdTgm4b2PHNkpnkm9BVi_FPNdhdw3TiDRM2ctTCWoW-CudhIa6P3v9q2nR4PQUuQqDuvxLRrkpnRsYC9IbMMN2NKL-If52kctcaMg0GJql6E76NdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از تکنیک‌ ناب‌ودیدنی نیمار جونیور فوق ستاره برزیلی‌تاریخ‌فوتبال در دوران حضور در PSG
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22268" target="_blank">📅 19:58 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22267">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyzHKFbqYzZJG0JGUn2UdzoF_yt7dgyw3nHuUIIZOuOrM0fhQYZXCr8pUgB8rw0pA3IHa7l9d2mqSZuvnw1pYSy2pEs23xthVQR4hASrYpRslwsog2vHhuiGqYYeeO7gA6hXiQTHJ8i6jvxTQ1d6zaNuT7nI9Y5eTITQiAIGXojq1gEgFkXgu7EogwXZEZjEBKA9xiyjoDv558aKz71QoJTkz6zaujjLmlgGIDSet79zpQcqmuq0X0s8REdxsPU3thIhJh7_oLZx03uAZwr5ivxYmchGAvEWPRO-QWl7sZNShWlPT19rkx4yn66X5bREZwEPgfyG8AMYXAaM2MO1Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعدادی خبر نقل‌وانتقالاتی‌دستمون رسیده. انشالله نت همه وصل شه همه رو خواهیم گذاشت. باشگاه‌ها نقل و انتقالات خود را از اواسط خرداد آغاز خواهند کرد. همانطور که پیش تر گفتیم لیگ امسال ادامه نخواهد داشت و تیم‌ها آماده‌فصل‌جدیدرقابت‌ها خواهند شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22267" target="_blank">📅 19:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22266">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcDI-7YHxua9hBxJSabo8fe2DCtArebRxZUD8XWjo0nUEgZN9xEJ0zc6U_1KdBKLy2aeS57s6RjjEGFxWU5t1hYb9T6Brqifk92joDdSALUZKuCEKUlXXRULqz0Ap2oujcBHVepkwRITn_67Y9ZdmkL6ZaPejVva-fbm0k6UD1s4Xq2iwcRTtYPE_xaXBOetNjQ6X8D4rtDLSBYRk8EMHI__SJfjR2pa4mw-ZMGtAPkGoCxIrAhgkrzN7eRvI6ISSL7EXYo1hjRtDoBwlq0_rBFJhnjdW2s8wPwmVt2RYVKH1C4hhOT2JoT7DsvzoPNYbg_N7bSIY-d4JUadEMSVww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو ستاره سپاهان مدنظر اوسمار ویرا سرمربی برزیلی پرسپولیس قرار گرفته و به مدیریت باشگاه اعلام کرده که به هرشکلی‌که شده این دو بازیکن رو در نقل‌وانتقالات تابستانی به خدمت بگیرند. انشالله اینترنت همه وصل بشه اخبار زیادی خواهیم داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22266" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22265">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YRrK3su-4F2TJ_5dj44n0pYeJz6fW2P_G_Dc7R7eJ5VdEu9U0X-ZL0R9A7z4QuonjJ8xABwMXOXCjCDjZJCiog_HZx56qFV_8pqRNF0LMjipb83n2v6WValWKpCMEHKTLVKUUYeXZeAGNaHLNOqmDgCB-MuTEr-Oy-keh81hqVeEQZbXvd7apxJ0E9mJS5o9zRUyelfbfsLhpwx6CfmC8Km0CXw3Mk0VON5dxVSJnp-35ytCf3AAngv8asZCCpMHv1G5leGYcW3anmyLeWIMvYL9vT-UfUJmU5k85ohn0jt4GUfOygY3d1X1U2TWgNqtQlbgsHrA5oYx8SmB8HXTjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رسمی: پایان راه آلابا در مادرید؛ با اعلام رئال مادرید، داوید آلابا، پس‌از پنج فصل، مادرید را ترک خواهد کرد و در تابستان، بازیکن آزاد خواهد بود.
‼️
داوید آلابای ۳۳ ساله، ۱۳۱ بار برای رئال به میدان رفت، ۵ گل و ۹ پاس‌گل ثبت کرد و ۲ بار فاتح لالیگا، لیگ قهرمانان…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22265" target="_blank">📅 19:29 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22263">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnJZ5elr_U4O8uyILZ3QW9e1jcMm5zv0v0F0gZ5pFcSH8d743Y2UP7KmZ1DlD5w0KFGK_5QrjeT7KCQzxsZehKI1WQFz0NI59nrMyeuykZZOJPRq2flaOUxeT_JXuJOyyjaX8nwl7pnI5URQwDmRnH5d6rHuJtF8QgqwKkF45leT2MYgms4KpdUdWhF3dexp-RRRGj3y69NaSqOqFIiItwjQ7Gh3JxQsXnrdQssrDQUfIrMWEvexVngcySc57F6nHaR5N7X9tk2s1RoW8uoH9k-80i1uFsQXHZPptw0FnYB1aG7ikMbbS6-x03Ke5t1G-VcS4aR_jweCbZSDdUkQPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22263" target="_blank">📅 19:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22262">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkGWEYmUaKRkK3IH7uLtgcrU76X8d-IbUQ9UfitXgrGGb_Q5RFhZ6CYP5XO-eCormPI6oCvncMvMg349qLXdmaOpdaW1z1pU8cAP32POhXh61Szw1CiiNKI5C0Pfpfbhe5fWUWQ9f7Vl4R-h962o4aFo2ll7GB6bE0tmw2V_y0DL9l7SAjEUSYsExTUssW-XRIMJ0O8IG4WsqwibPosDvARuyA4zWWIPAPxOvAFc2kbEegt2Gmtsv7c0fzuXK7A4PEZdTYk_0HPveUOr3ILZGDMogzRMHz3icFT5sfTbuN9JAoKem5Tvrm3VJ408jVQPI7fnQMUlQfmGDHobQbSc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22262" target="_blank">📅 18:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22261">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmpc84TKf6JwjlCepwCOf-INolC90z5PdsjdFW1aif6dIpbfNS2v_LOemwB14jDqJhlPiSopWzAa8-cGHl0i3scWumh4TwsZF-tTx1CcMCypWohy51Q6XQ9NSjaJi-xqhRCImzXX37AOgVQ8bEfzA8B1ntYa11GoQ6iWf9lNq3nfzj2IQmS8fwPTSabvTdwOf_nCghsChM1ubxM54RL4TcgfZxMaKDkw5UWL2v9rjVil5gU0nOsIfy3eLghsWfuqSXFSTW6apVYSsy7LksqORORm8EfR-PlqVgkIhmmvtnLEG9ab9leiCdvJKf6yf1y5VepW4TopN9KybYFcA2UCww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌کامل‌مرحله گروهی رقابت‌های جام جهانی 2026 در یک قاب ؛ جام جهانی 2026 از تاریخ 21 خرداد ماه تا 28 تیرباحضور 48 تیم به میزبانی سه کشور آمریکا، کانادا و مکزیک برگزار خواهد شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22261" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22260">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2S7fROwoG6zOls9kmh7rHeUj-BmFiam_7PCkNO5nryIFuUSyAv2itgPuC4ZauvKdaLHhv1Jk0vTMZSNSvfC7A5Q124I_jqf_EEk-CzlYFO4ZwHWFq1MXiPXEUTHTQpI0JOHIsU6VatQvuC7j1RW5n5HLPsSv7H0OkqvspNGFcCp3U-fCrBZIVIRjZb_Dn_qQ1HQYlfA-QEpM5VF2eg1XduHIK8nRK7n-qRHnIL_vHUZKJ-6K3fMxcDisFWl9TIhZwic8bTn7heZUo8ob3u_Do9TfkerLX-V7G94zY1wpLSYNyGRuxTxE1QvV3dIEinsD8OY9ioTkPOsICTDvzLvKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛
باشگاه تراکتور قصد داره درصورت جدایی علیرضا بیرانوند در نقل و انتقالات‌تابستونی با محمد خلیفه گلر جوان آلومینیوم اراک قراردادی‌چهار ساله امضاکنه و حتی صحبت‌های اولیه با ایجنت این بازیکن نیز انجام شده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22260" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22259">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpui2UaFdMNk2fkYT2oXzgbxRrWL_yZANX98Pj5qGhfXGdaCHQ2W58gR2CIz-Thuz6coM6veVGQlw-Cb5mQMgd0Cft1pFD40V6cPXBtK-CcyRUnEQUHKeIS-MWx6CCwr_moYWBIIqw0lY4fSJ2xWEJSf6EhFFipmB2QC0CbhMo-Bqx6ThXb9D_bGq8gDDeKnZpnGMp7a_oODLsFhyyB3raqkLE8RTXbPL7t9T4H9v40CKcOZD85kH1IpRHKlzMB3tGRXCJ4hzm9zGbv9YOtpT0_bltNeHPlJmW4Pc58HUoE53rC6njIZx1H0Ki5CPiG25wGXcyEhmdUKTBZS7E1SmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب منتخب فوق ستاره‌‌هایی که جام جهانی 2026 رو مفت و عین آب خوردن از دست دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22259" target="_blank">📅 15:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22258">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYmsfFAVeWZI7sAMx0XKWeJw2bSo4_x6sucvlL-6HNHXd-rYcr6K5rNutYRpS88uvJIXThOX4fiTA_UqjucSnvJVFAQMEAdc8mUZslkxxDvMAEtI3TsPo7yJrrthBiIH0netybSLQcESkK1YxPnKNb4pa9z0z3Lxuvmq1P0UYWW-EHZ59N_1ykR5UyE-X4DlBS_4c8YkzF3ZK6Blkf7U945x6Lh_GxEYfwVSbTZVcRJfJiENhvvsDsvx0fqKEn7z69_9SOBu6c_zoCJJ7m3u-qLX3ZaAcXmhg1m6FksjgNkAHW-kG5I35R5q3oiSKDt8P2TFeZCYu2jBe1PAW-l9hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برونو فرناندز ستاره تیم منچستر یونایتد به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ لیگ جزیره انتخاب شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22258" target="_blank">📅 13:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22257">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXafzWpRVK63CSNiTNqvX0OMpgH3DX8V90huJojTSe9m_T9Tp3n_Oz-pF5P18yqn3joi8sT6nrn4UqsL-mF5xahw4oBgSYOAXovVEr5Tozls_xlq83isFFgSe8PVJF9-LEw8tKN_ZDxv7pUUpOHJGwqS-DZLrDXgcQKQ3SuHlHAxM1JtnKqGBPY9lQvEf67KU3P4fh5TAMaUlqT7dKQEn0opUVBySNESMWAHZQybDwEMyz58s2OocekClIRjcE5xOv6vwOPDrp4U5d_GUZk24n6-e5qP1stnPKdZ4o8yO3IBR65_bLpzT-bKH3R49IqN6PGPy1kmLr40EfwawBKD_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22257" target="_blank">📅 13:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22256">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUGExLNNA5k4QJWS6x-68yIHyWCnCdFJNJMKB0YclvZe4Bcar7E-ILVho8WZJGD1HSeePSJ5Qg8jkxgYueEh2QUjWOIcXp0tE3oAPiSUBZHWkiarbcUSPyTQ2E4f9h-gkTModzE4Mynkw2h0v0xp5fN2ZCESMyn339zLAHUpsDZ8Ic4_-xGfUvNfSiyIl6gNlTs8VVsbCBYRFj1nGb8xF391Ogp503yrDum32itcYYpCtE7FNZp1XQY7ymgMqXMMyaJgh6mdtLUWPj3F0yJxozYQzXOpVxu3lWzmLJp7g4wxt222-jkE7JGKNvOOkCtR5bnEKTCrRTso_4Y5fuJ9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسعودپزشکیان‌رئیس‌جمهور: اینترنت بخش جدا نشدنی زندگی مردم شده. دستور دادم با نظر رهبری و در جهت رفاه مردم ایران بین المللی وصل شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22256" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22255">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1jtOe5WoA1WNfBrGkIFyR0bN1UIh3bLlDMdjkcenID6Ta80eUYcNWCV-lv18UKH4PN81XoqeYfSO7muTii3z_ZYaltEIn2-y0J_FY5oWFLmHBsd6IllQoBUY_vH7RMbE0p0qfLG-NKQkbMoVCJq8qoORhgrhsFwppGG_oBuboth3VGw86OoLKrnPIoLuizomSZyPxsqfiOZffC1kt42bOv6wOhyQhtmNmOYBJCjs0fIANUS3rDz-JvFuUNKvzMk2lNEFDpdDZWkJMhkD5BaLf57O3FKcYOv4ohfq55JU9DDJRzbZ3ZkO2EmJiO-ejMTdC1v4YFz8vzHqNz151eEgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بالاتر از رونالدو و سایر ستاره‌ها؛ ژائو فیلیکس ستاره پرتغالی النصر به عنوان بهترین بازیکن لیگ عربستان نیز انتخاب شد. ۳۳ مسابقه، ۲۰ گل و ۱۴ پاس گل  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22255" target="_blank">📅 13:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22253">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzT8S07yMQl6hgr712yPHdtYBY8cIo8XwSU2-rMFRgQauqQcjHLQQzlmfzm63_KPprMrNNaU7vFzzUkwFUxqsiqP8ltVBkD-t3gjuhr-cs6XMN-T8oQk7xNAZ14u30b-0PqBtLhR1dJKtizo9ROEfQnv_1irJYsHAiI5GUbw07BpnVV24KmOOLUgtYPM9eMUmXlyIvoRkI8fBLHSTvTkELWgw0kH8aLL7A48OU3inybs2_dQr80DFwOC0bdhv5LQNKfPvVtye8oo1dC6ExINHTCPSttHs94-AKjmqpW5LfIxaM1Zgu0pD_lggmIWjzlXKW7NCJaIOHVc1mMaYj77Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فکت؛ کریس‌رونالدو به‌اولین‌بازیکن تاریخ فوتبال تبدیل شد که در چهار لیگ مختلف قهرمان شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22253" target="_blank">📅 13:15 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22252">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTuti_QEG9_vF_MyXI-Mz0XfdoQqgvfUHzp68OUzSdGzoWKO0iIWHAcgpexyO4_rVUPyexCAfVcfu2xFLhOoHjm11bLDdX30GzOjX8y7u6VEVGaduyiTVnbKPdfIe4XOudGQOk85rv6s4WYV5cAQw_sNl7FLiAzwhzIcqcUTu4Lj7GSGL2HEW2c1FPG62h-I9i42zTSzsuPvCCJVe0MuGirCaLHjy7H-3UhyawA4WGfv2aHOrzykWQJjT2sAToPOxNC9nEMgOYcAm_9w-dQ5ahzzYCJaCfrdPFGUBB1m-1sX2oCV8QhpSNVGENIrqvhXqhZNmDtynnm00kMqbczzHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تیم منتخب فوق ستاره‌های توماس توخل برای جام جهانی به تیم‌ملی‌انگلیس دعوت نکرد؛ توخل در مقدماتی جام‌جهانی‌نتایج خیریه‌کننده ای با سه شیر ها گرفته بود اما درصورت عدم نتیجه گیری در جام جهانی قطعا مقصر اصلی این اتفاق خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/persiana_Soccer/22252" target="_blank">📅 00:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22251">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN_wQy6kvzZw-ervbVyOLbqCOUS3Q6wcPyZJzx8bFoHpF5RAan5QqhdPbbdLegIK0_vi1m-s6jM69HddrOgIgmpChfwIuSujc-vPTs0Oxlj9ZOgsJ2Oj6cx9QUOC5PatYaLKn5TmenT8YwtnVNV3F2CRSAI_8r5UPtFqUEf8sT-SYnlMgqAVyweYoXg_8z2TFfEGvLnnQH1FzKtaU-NkKhh3mgpy9isRW4fLFMhPtyqVYCtLnGpC4C6B_QiImpi3KR6cDeWu8_e7KGZYj3oyNuT_M9fLOv5D2B2t35WVnP4JaU4-faWjs5V-uW55ObXU_AQuktc41zVX2WRJM3RVNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22251" target="_blank">📅 00:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22250">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKacMyiOxOm15RGBE3S5XYs6-Jxoxk-54Ew21Y1n85KnsAsyzD4oMFiClsjDmGddTYVT2XVcPxMJjBSyitQt0IyOwf1nVMIRGzOlK5NTdijY3LOHkD40vUdyCLDIfe4up0R8M1RpCbWHMZdWY0DKJJS3gtdrcICv8hU8YtyZPEqgSbFib4wMMQo3AattUCbDNGjxc31JlUtnsmA26HoDnM13FS1bL7ZUfwwVm3WqyPdqt7qoY9WLmdpu2ugUDUK_EhSjHe4JmxbH4biNtgbGviYc6NY0LW9Wd2FV6aH2w_3c8-nW-vWLg-7LXMfaSaK2SrGnfeQCpuvaaa1DCHQU6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیران تمام باشگاه‌های لیگ برتری به غیر از باشگاه پرسپولیس تهران امروز صبح طی نامه‌ای رسمی به فدراسیون‌فوتبال اعلام کرده‌اند توان ادامه برگزاری مسابقات این فصل بعد از اتمام جام جهانی ندارند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22250" target="_blank">📅 21:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22249">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0MHMuu6yzol-q8g6cTX9Fd51Nfjpqtqx2mRPoj0Wa1yFkB50ZvZygveQhGupLqyOXExrYX9EdOC4PevOuKm5JI2cTHcDXmRcAJqNhfYvwno1tTRsBZ8OVWFYgqYDxrNj77e5MebX2R3o2IAroZ-V4KmY_GcuAtgCJizVZ1I2svsvJ7m07LNxQHBUzhzGFygm3aWDmQFLiuC2Po-8hGmsXdVUYwK_zeBN66Kj2nbPnXTnmy0WkB7gDJE09T6g4OU9blsbQlxOc0QSMYnv1EctOKbVMVToKi45Jaac_me-7yI1C5nrUY6XBpuV-zootj5W58qn5gvMPkYvKh61oKWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه اتلتیک: باشگاه رئال مادرید به داوید آلابا اعلام کرده که درپایان‌فصل‌قراردادش تمدید نمیشود و رسما در لیست مازاد کهکشانی ها قرار میگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22249" target="_blank">📅 21:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22248">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ7O1q2oUNn8bULVaMYTexLfXcXkEzQeuXE1skLU8pVuAGVQux56y9NuoHXFV7-W2XvT7cga18FmQu5fbqpo4LHuedq_XGWduD4pnCmOq-EO1kp2jmYDF0IWXFDp2QVhNH41rONzCPRwqHdqzF2xZx8P6dYy_O-1SKUyMFuh7LEcJw1PnEIyjJtMa-NyUhz7NWXr9bip5QOmYDwDzONenPTaixA3IOYpmgIF8KYBSwv0Kv_6zsCy7HECCt-spDkIvVoggRUkROv8nR6T8AM7nNtcc_5TZPW0TG_I3wSUlkcrfNZ-PfCTNYBNiqUBmBmEbu5gMyT7JeeHW_3KrbGA-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/22248" target="_blank">📅 20:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22247">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6R00W7Qycz_hg0NPzO2EPFZJLti0ZSrZCrKiwfFeZV_qH9CXi-bXd3sQYHd8Lxk2tqE3YzwGEC7vXfxWfPnLlNpypPEvWAD-FaI9NgkkleFegOxvKyKDK25L7wFtUmzgbL5LTqhaaeduE4gnidia8-kTnOPYGe8YVKkOTLrHID2K8ANiHWN75fsnpLNAUgKlb-kwNm8O_TqO5_nUcnaxmbC5j4vXIOKrMcCMVSr24mWyQe8B5f0mS3t7mIk0k3X2hzsj0V2FWVLpD6k1T_0JsG8yXyxX0sFMgQkC1BhjDvTNjmCLb_hhPvqz0b1UvVh9pBlnw8XmYTQrYaC2GGegA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22247" target="_blank">📅 20:18 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22246">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYwIDWFjAGNRyJuTnY7KJSBMm2J7ZtgXUaNVvMjvCzRtT_sKjmiAbsRIv1Fe6Y7HRsMChgcCfPXbNIOp2ZrOgIPxOoTfu5L5OzFtKwerzzCbI0TTYo77qHM9hlbrjl2VGh5PaAcVKPbmjNuXNYk1oQWKUy2U8R9EZuyZXJ6x59jnCZZs4gcWG7KUqcfO8J5_HLfWWZbFI566wsA2yUFOM7IYDwDMMTBok5HlC8Zc-t4d6ZJofl005SQ7XlADb9IIvpvvZ7gpZh4ltyc4KRgPBu_glJ6YZ1I5jupD0EXvOW48JONYaxQPJRev6cA-pwKfPkdTzNH8hPt9NQC8XdsLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ایوان سانچز وینگر اسپانیایی سپاهان بعد از دیدار آسیایی این‌تیم به‌احتمال‌فراوان از جمع طلایی پوشان زاینده رود جداخواهدشد. سانچز از شرایطش در ایران بعد از کشتار مردم بی گناه راضی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22246" target="_blank">📅 17:36 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22245">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=ixJosQA99-PYDL95KlQaSRl3aQ6nSdmAFEgZ89d7lO_n1ZLzXdQIElYnN6OIUH9UFsGpqcyQO15r8FyJD1M8ALgV-b5xFFeOKOhQZIOovqNVV69uwfYZSbHFFpY6dNGy1WAMHAusylYvDRHaxUAvZDRbyhYydS79IqDaAdKi0Tab4WhN7eJuY_1SoYtsaF6SWDuFfUosb_KksmkQjX0xPSHFYHYwLoPsRQ11WU0l-plqv_-n3o2L7-iEtZ6yQwl7YOZYjY0zTbt1DzvqgfdVFWm-AHka_LVJKCVuKCR0t9b22_dZ7gmvL1CzhNKHeSomwBxgs3KBWeogqgYrVWhr9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cdb0d3e03.mp4?token=ixJosQA99-PYDL95KlQaSRl3aQ6nSdmAFEgZ89d7lO_n1ZLzXdQIElYnN6OIUH9UFsGpqcyQO15r8FyJD1M8ALgV-b5xFFeOKOhQZIOovqNVV69uwfYZSbHFFpY6dNGy1WAMHAusylYvDRHaxUAvZDRbyhYydS79IqDaAdKi0Tab4WhN7eJuY_1SoYtsaF6SWDuFfUosb_KksmkQjX0xPSHFYHYwLoPsRQ11WU0l-plqv_-n3o2L7-iEtZ6yQwl7YOZYjY0zTbt1DzvqgfdVFWm-AHka_LVJKCVuKCR0t9b22_dZ7gmvL1CzhNKHeSomwBxgs3KBWeogqgYrVWhr9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیش‌بینی‌جذاب و جالب از فینال لیگ قهرمانان اروپا امسال؛سال‌رویایی و تاریخی آرسنال تکمیل میشود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22245" target="_blank">📅 16:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22244">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qc0H0EkCKnJvDVDMOXMlu9trBLM5GchwbgX3lUPRWVt77aarX9TWZ3u16bXr0KAAiCI7StyZpoHll1BViyJAsb0CULQheRkYfKS6TvMk6rC2kbgW6w-I8HvfP3IqWgGahQEO2LQ1rH3AE2wteFXS5bzRECPwp70X3uuM_B09bRGuUdHLWpMpRmSQRiK_eVk4AfN9L_olyyq542qymzMfVXwbke4hSsEEclYntKBsBD5g957rHpog2cGZZDBaqpDNtb1yEYpcEfm-Shm-rEiIxfkRWhFeYWwYBG-ZYKisJT5_QMmCsb4yxBZL0lOowXVO8121thGXL0nil0CU3VawGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شانس قهرمانی تمام تیم‌های ملی در رقابت های جام‌جهانی2026همه‌تیم‌هاباصدر؛
اسپانیا در صدر.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22244" target="_blank">📅 15:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22243">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pc2VdDYZZuWdy-8VT3lZe1RD6e0HhLlprEbCLFMvl9Lm8vHQhv_IopqlY4HJePIiaYuJzf_MLZ4yM4X390PMciUgh5imt2OmBWkCxovzWjlpnna_zUnnjYbTfDUbPw2Ia5C41ryNZQuW74b7OngErHcj7091mU6sCd-3Z81cUkaPcuSZoCN_mI00QzA6WryAJVZtTJqcuVsJcZqa7ccb35zkhwM-jVgORFizK7UkkQAjG7nmI2QhlXyyq2HJscUaM-DLF_HkDMHZdFazIDcWqiVHQwZ_G8koPxmuA68J_EHX6xfVyHect08CqHjRvZr5NwE5lKIsNvll-EqQiv8V0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ علی تاجرنیا صحبت هایی با وکیل علیرضا بیرانوند انجام داده تا درصورتیکه پنجره آبی‌ها در تابستان باز شود بیرو پس‌از کش و قوس های فراوان آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22243" target="_blank">📅 15:21 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22242">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6LGzWyUGmUsct1I8wx1qeoQ2x1eOO70Co7rLkxH7uUyYQ0Fa8IjU1P6hRk4Wjqo5Bvylq6YjEwp3-VXo-uRU3WymKH09n3_rSHfkFWYpcRAGp3rmoX78QGZLrcdUfiMU6qzkDgSTTf3TGDDXtkTGHHbyGY9490ltV0poSkOyCUT06k5viHC4xvYyS-sEnzpVnUE3PUNjbBMj2OSWP6DsoU6xLCFozo3T6STonmG_2_jXDnWMFZodnzh6imJR_Ru26L296Own5NtqP3EQvJMrZAiuwWxksgNgD4bnX5lLGBPOiNzHVUL2xZFO8IoAYR1Oq-jtHzPpI804PvYhdAC4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان تااین‌لحظه نتونسته مجوز حرفه‌‌ای خود را از AFC دریافت‌کند و ممکن است درصورتیکه مجوزحرفه‌ای‌این‌باشگاه صادرنشود یکی از دو باشگاه گل‌گهرسیرجان یا پرسپولیس تهران جایگرین این تیم در سطح دو رقابت‌های لیگ قهرمانان آسیا شوند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22242" target="_blank">📅 14:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22241">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEdnLZjvdoes3hN7VuIHE6xEeIVImSlU1YsKWaA1W3fNmXhMYUyJX9LdFmhYcyY7M6IFb5RxU1wldwMOaytgW5XTiAhhu3E7StC1MP6pYhux1nk5YQM0wF3toojTYHUdcjS2v0mNpUGGCUkF5X_aQsOF_HzfWdNOWWWu8HxGqEAqBTK7o-Fl3MEpGqMoHD2shqYBD7qiJe3M1nySFwo1SOoLpTVgGDf9CFr0ZUvyMB4sjKPtFImCmedVvBUsrRbiEjpE_i1HGTFsb1B7oJbdpRAocAuJSvf05RdT81LK8oE1cmkeD1TdIA3YZpvN2MQaR9oq-iizW02Lg9RtDsfs9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22241" target="_blank">📅 14:10 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22240">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiEkBw2ABGMIrc2z4f-1bE8xKg5VKZ1qyeIsad9IKmMyg_rszB1u6kk1izuoVFrHgHYK6UG8N55QMZTzJObYtTx9Sa6TNq6h3PQMb8sxnNgfQj0QFftY5cQjmZd_NS2TypI-1LJ6BaE_8t9E02ZSrIxoSx_YbYwGY_moIHXvuPl_0cwmQ3JtYZT3x87wGNSe3N7N_2uXAiHA51a8I2wH1DAEvdvE811TZRYPbtiLWV1TY_Dtk-EsdwUb2zKg6WWXKhQ78WH0HVH1ti9uXQeu8eTsq4OddHnC7dmxCRaKqMvz4Fka4RI-UpcbBngQdwvHEw8TxNqtTMxvVzaBrXB98A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی تا سال 2028 رسما به عنوان سرمربی دائم منچستریونایتد منصوب شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22240" target="_blank">📅 14:09 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22239">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEzT__AIxheK_4qmxw8iTMGsW4lsTS0qCYv4zzAH_iamV1rCWayJ-BhULjvGuWsNJngWD3G-xXIFSiBjeVfY9oWuXeG-RfjsaRHmD2wMw3PHKQgJZ-UG1uY7-IUyQL3pSUvT3KtJpTJWuFHnSN0JC57fZlEoV5Ss4Mvm4AI4SAXM3hv2JkYkGz45ITiN9xCdqQoR0b122fB2unPDjl8tYtCM4eKANLJ80AvK0STc6ELyCM_IyaghMcVtXuUjL6xaYSqFAcn4i_2DLxM0c-ebt6hny3BihNhodC-LZWn-gYswoZYpqZGKbQyPQTe9xeEBa1Cz5ZavkrJYZTrityvx5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
با‌ اعلام رسمی باشگاه منچسترسیتی، پپ‌ گواردیولا پس از ۱۰ سال درخشش در قامت سرمربی این‌تیم از جمع‌ سیتیزن‌ها جدا شد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22239" target="_blank">📅 14:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22238">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1Qek7waEp0CEHw9YyLBK279IGMH9U4BujUWWcqvs007cpfkF0I0rpgVOfEmUa7QhIIQ9skD0YCQE8N0TlPaU5jtbyn68H1orgawdwgZVFwuha9sv04uIB_MaK__rFbq7Rl_m-AQnDAxe0CD5V593T32j0m67MUpU6U9pUCZc-IfQ6TzPmjwlmKz3HHyKyGKAjKfJwUIUwiuuQPhFj_yDRXXdIWwVtWUeZFlIYg3-k02qOVCOJ1ccrvqfgJb-2aoFguHQSvvZ2GEHzo4wGJ_7xw7Y3GRIMnf6qIHzxmrpKyd3C7s_nigwgvbMf0xztO5NUDiYptWZpnVP0HQNYDZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نهایی تیم‌ملی انگلیس برای جام‌جهانی؛ نفرات سرشناسی مثل کول‌پالمر، آرنولد و فودن از فهرست‌نهایی توماس‌توخل خط خوردند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22238" target="_blank">📅 12:49 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22237">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEPo3nRqq5FHDQ1xsEVFfil5vpKZWacRyeVBKdHDgBF_fwrm9M0voqi3NrppMmjaFK3ZRH4eK7n5ID3rLGGVyD33VSMvVWLyvjCvF_ciHbDZjp-Gb8pccns1cJ-1vyfIP4yeIKs2ZxT6Qk59zKSu9sMJRHaJsPVBE70SRsYtpAkXvch4gRN3-223hjYSHwXdUnDVGXUwU5D9VBKhZ9aqNQOUwubTPzOQtf2fwDF794d_xExtKVg8TwVgwdc9EZfqAwHprGgnr7l0cvxSww9PZq8Hk2ITtH8NnuoMU2FX1eXtCuLLfxdlRDtfU6lGJz3Doz5Hg4EePIe6ttPE1oPjSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22237" target="_blank">📅 11:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22236">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/izvthcAE8wbWN5Yq-aBXOyTOwSfVyeQhPhnVGkjEZ1xEm2NjjPbjGJYXObjzxEP8O1K1JclZsJO6nE_C4HvmqU51_x7UN5_cJla9VHN8b4dG7JEhZUhTan2ZANM4vqi0tSAToTl1OZPYhCmNbcqb-QnvLtrShsMh4MIA8s--cod8kyh4Zs1kOMEl_2l87MR7CRKywbfPlriZvsbD1I-po6-F-A69IAczURx9BrE1L5RYM04Om53y8E_wHUqr7trHZ0mMVcJYhyj8_jZDnCFDQbeb1Z7U9cXuRFsMzN6arEw3Ng8pMEsM10Y_K3_X6RYYhxuvAPnyBBiODFOJLaCuOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22236" target="_blank">📅 10:58 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22235">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3TyBwnHIfaVXcqqCouyOtRXZ9SQ0bWLw0e2RNrLetA6tDai5OD4aRaIrWXP9rMCn9M8Kn6aKaCQuEiW1YATCn7NmDVgDW_clBR3P0hqMwbT7wLgHw0ZcjBNJnmbB_s49-xWOxZHEZ6UChemhZCP7fOKW_fgoWr8HI-hBTK2sP8gMWeRM5Ln9meo4IKulFZUvD67q7R1e8jAuC5_fEuUK-sIJgP_AfnrAKomnICscvJu3gjewdIpip7zty18G_PUvFOdk771r0mALdaRLM434wo3vB-5FuuRbjlgr-_A1dFUiHhLYXI5bxI-PxQMWuZ4PyXnxK6uJMHZtkjcyQirQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بعد از باشگاه استقلال؛ مجوز رسمی دو باشگاه تراکتور و پرسپولیس نیز صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22235" target="_blank">📅 10:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22233">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/buQEDlJdG5ojeXPr8fTVRVx4KgN_Q0rEWu46RfBSSPaFC1m5ukrYMdOhjisBtIFou6S9VBGjhETqjkJuWnytcPOva57NP1Ef4N8C8VPiwkjcfPepTz821sq-ZNypU1tnQI-oca4PFt143rCzKVeQhu-amsyaKAwApXWzqA38UyDW5q_LEn9ysQbU6SSylP279XxUFbsnNeAgUZlSSsotR0djK62MDejDH33AgAbJLmVGDti4Nauz8iaejj14D3lus1loTAqQMF0p3k2-G1pQ1xmlorx8-2yxzEv_9YbbI-OzoiU3fE-4gvMwjAPRCYnHx2RVXgbVm57A_FpqeqcYzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IwKktr9NJPzcaV-Q2iBG4U2F_j45LSbTVpTy4_5DqijBdBG5JkGqglrLKZe2wW7Qkdp7UNLMuSfWANtpV0plCDdBpiwVrhBUAuRItpRRMsH7Iv_VnV2BANvlmJT54hyCIJSJUyo997eCl7-iH4-USSYed01vqlFGhx-DPkSxluWUOCCG8MFAZFzJGyBdR8B7JkcNYoemQcR3ZUGnj6mXjekFzZXNfrpDS-1U4GtLHAP6vcOpqqIVV1y8Yt9Ax-iCrg8luYBlGyxo_rv2hYXJYB1A_88oHhL-pyWRbT6smP9dhKfqX_30YAVINz2QPmUZiEsuSnIms8lOlH-bnZb0XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/22233" target="_blank">📅 00:51 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22232">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">▶️
ویدیوکامل‌جشن قهرمانی النصر دررقابت های این فصل لیگ برتر با حضور کاپیتان کریستیانو رونالدو.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/persiana_Soccer/22232" target="_blank">📅 00:19 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22230">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RGQKFxc9reB00kAqxyFv1lpqa22pt1my-ZTeP5UBsZ5_go2yiT801-WU_kqxqKoyDGE4BgtmedZQmF0wNn5fKCOGOLm5G9piKwmeVix5a1bmnvzDiijE5J_LwGaAlgEhIS9i_QzmM1wlARdx7lFmAb1VZ7e6nsB196F25m0GcjU0r302hBlsY1joBqvKqxCD0bqx7QJgUgdlnoLRpSLvULXxkCAgn65F1vjepg3kTizXePMMTRx7n-u1POMQ7E6CYCWeyQatqgyx90Go2rfRVXd3CvRW4d0QH1x2YFDXqeOXi_ytAB1o_Xsrc7tTONsTSYJXy63mSuycU9QEjaq0IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2upYMavJJjnsXi8RR27-_a_augOQH68mwOuXN6V3Y-XvZwBO5vqWCwLbwhI8_5vCEFbM-edkLXoTIby6gq9s6wZlvK7j-cK6Tg0WkAxW7jC_EFX_7cE7iKjOy5GLTMj0v77ZfBUpnvPoI7XBlrth9Dqf4wWPEk5z-zx2ca03WcA3Z5lKPJzso56IAsFqIJuq4EAlNqIjx6HDQKrBr9c2Xxlu47oSfDk3b18C9nsOyCVj1yGxy8MT3chaCalI4Z0byj-MoeyBtW-bsJWinuRCVQi9aznKR2ufM6kSKzOjJytlf8xIKGWkRy9_x4u057uliXUXtVJtVHOW8utt9GVpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
هواداران پرسپولیس امشب پیش از دیدار با ملوان انزلی به این شکل ازدواج امیررضا رفیعی دروازه بان جوان این تیم رو تبریک گفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22230" target="_blank">📅 00:15 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22229">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj_cmxreb6sfJayrvKpjkjiKkKHMvEP6cDsHO8J0_ztewFRl0o1jUhCUFamfMb_W1smUgN1w9GkzZNIXO5rJzSSi_Qfzm7FwCDej1_CF7prIebtMpjzZMMNXK_LkxWfEc7akUIaadVysW-ZUQ4js7mEitqX7Db4PgDko7YtsPLmr8q4VoB4kSZlWp6X4lFX7RjHUz644iKup9xIip3PoU_mKKaNS24QwE2tV--OS0y89nHvn23svIGvlNsHiknbNZQf2cUwlsLyewn49V7V2lXMu75Pwlbm30dRJ30cOLaSLYyZsbAVHkLck2kMaKsQKAJbj9PNPHKUCJJuyJUe49g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22229" target="_blank">📅 00:08 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22228">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUAk2kq-piP0O1uJe69n6r7OyD65ikl-F0B-3Umv26T-XTJ2DlkfnceaBmHdyPbScoyUc1rsZMS_H1WZ_opAkY-Xrm5CMqyNt5fZIaNqx1EAHo6OFEnIh4iOs95rFowet_4RqlffCW2JGZjB4MDZUx6j2e2nyz_p4OglShifWlpqGsthaGSVxdkvt4OprGIRblHhDrjmOda947UIpUnww9DSQpj_FjMs1eBjXHxiGSulxrQ8t1EYncjc9ybOC_OuTRBN3ocNKqnVdmJyuShn-rvIi1TQCCgifcXo8_4MYhi-kfMcJHgH-tnKjBRqguo66YrKBkqeIPQBKUaaS-HB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
والتر ماتزاری سرمربی سابق اینتر و ناپولی که در دو بازه زمانی تا آستانه عقد قرارداد با دو باشگاه ایرانی پرسپولیس و استقلال پیش با عقدقراردادی دوساله رسما به باشگاه یونانی تسالونیکی پیوست‌.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22228" target="_blank">📅 00:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22226">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t89pcyNMiWobx3xDL2Z6ZEu445xQ8N0_rOrOWS5tD_O9kaY12nG-VTkUVPj8Bl-z2vDx7zlbKMaLz4qyzA4fm79jCWRzjRUDxVYINuNynKR-tassjKpJF5-ZUDsb1-afPjqZiCIMqJ7GFh44BD2cupuMSI8LHhv4Rsjf6TOJi5_pjSWOmnvnlFaof7ad8kaCQJ_rX4wPiF8VrIQO3lqp6MflG6FjqdglL9SWmC_FVljQv9MrJw4G2PwoHH1sNKu5g22MVsI7v9o3A97lNWGm9l_M3u7X97_03KzlLAIcjr2h0U8zR-pAAiKBk6GYL5tAR2n0jU7So0zLHpb9ZNtz2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ النصر عربستان بعد از هفت سال با کریس رونالدو قهرمان رقابت‌ های لیگ برتر عربستان شد. قهرمانی که با درخشش کریس رونالدو رقم خورد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22226" target="_blank">📅 23:51 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22225">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsDL9rQY_mWAJ4pMlVttinwalF6g7HdiZC0mtw0bovgym67kbfvPNNYOcPjatO8S7ylSAmJgD1v38YFxVpQLobJvfE77JpZ1xpu0LpuVmf5hSwQC9sgBbhirDoIqSwEDDMgGsUK_m9Kesa8yWzgzZtBf1dqk_T1IkqRL4J5dK35z3-vnbhFFBALx9H_axGbLsSb3mtx7ENyt9v0IW3MlxtvO-HSYl_GciiNsWTT3PaEhgn25QEZUWyv9TPnnPLy6FRqFg1lur7lmwjDaas-J3Np5j1B0Yl0gA3Cm2v7ILTD9Jxb8J2RJdGppK6NsYHRJ3TTlvNIdjtTdEle7NUbe1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خط و نشان CR7 برای رقبا برای جام جهانی؛ دبل دیدنی کریس رونالدو 41 ساله در بازی قهرمانی ارزشمند النصر در لیگ عربستان؛ این 973 امین گل تاریخ دوران حرفه‌ای فوق ستاره پرتغالی بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22225" target="_blank">📅 23:24 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22224">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d569523e34.mp4?token=Xw_GIo19HrQqSjHDxLgDHlfnWzjXXIUN1GeHaSxqizmEEkjiO_K9W-jD6UT0cyw1U09UFwEfGlJg99IvvVOnwl7nU3sLMdnnRMxTO4ph0xAk1b1uqU_zyhoJGweVJ0n93KzSaZLMkJaIWD3pSAIcSezqAW3S-cEhOKfI9lC3qrM7_lVmcAGPuoSyhhBSsbPo0FJZ6hKk_f-qs5iRDB582ae9DsFVQRnuj8-OPXVmy2Tj2boU67leRzBTyUggL4YA2C_dq2ipe_cn-zBoIMZxATglxaVXA-wMmk_nG7Pp0eNMwjH9xsH1oEEial4rAVChGMIL642UCvmqQbLOZI9u2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d569523e34.mp4?token=Xw_GIo19HrQqSjHDxLgDHlfnWzjXXIUN1GeHaSxqizmEEkjiO_K9W-jD6UT0cyw1U09UFwEfGlJg99IvvVOnwl7nU3sLMdnnRMxTO4ph0xAk1b1uqU_zyhoJGweVJ0n93KzSaZLMkJaIWD3pSAIcSezqAW3S-cEhOKfI9lC3qrM7_lVmcAGPuoSyhhBSsbPo0FJZ6hKk_f-qs5iRDB582ae9DsFVQRnuj8-OPXVmy2Tj2boU67leRzBTyUggL4YA2C_dq2ipe_cn-zBoIMZxATglxaVXA-wMmk_nG7Pp0eNMwjH9xsH1oEEial4rAVChGMIL642UCvmqQbLOZI9u2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرگل دیدنی کریس رونالدو در بازی امشب النصر مقابل ضمک؛ النصر با رونالدو به قهرمانی رسید.
🔥
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22224" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22223">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=GIuwBC-duYZn_4Ok02tFw3PUyX-XkaqKvwfvUYpfCMHrgWBvAUT3eXJQEYbJ6qvTb1zEl4GIO3kv-ArvDOPTN0Z48Jws69yRm8V57bczKXN3R4mzbdekqyvqAzjgrsNLnoZgv_g76I0bDlva5Iorv_U8hcNO1EhRV_MkgGMeIYlojFHYFOLYKwHYLMBjpuDvgDr3cJoVOtuJiGxO2nNOy28lX2YBVkmcXm8QdyiUvkwH0aFqZZWKRHlRqGmG5YS-2-aY9wjhLN-uAxX-jzhjeQbHtD1eyJ56aezZAbI4e0uPlAkmeFTUFbnteKZIJ8f2eYjnyTSIvgAwWiSjSYSADg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ff057fc.mp4?token=GIuwBC-duYZn_4Ok02tFw3PUyX-XkaqKvwfvUYpfCMHrgWBvAUT3eXJQEYbJ6qvTb1zEl4GIO3kv-ArvDOPTN0Z48Jws69yRm8V57bczKXN3R4mzbdekqyvqAzjgrsNLnoZgv_g76I0bDlva5Iorv_U8hcNO1EhRV_MkgGMeIYlojFHYFOLYKwHYLMBjpuDvgDr3cJoVOtuJiGxO2nNOy28lX2YBVkmcXm8QdyiUvkwH0aFqZZWKRHlRqGmG5YS-2-aY9wjhLN-uAxX-jzhjeQbHtD1eyJ56aezZAbI4e0uPlAkmeFTUFbnteKZIJ8f2eYjnyTSIvgAwWiSjSYSADg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درصورت پیروزی النصر در بازی امشب مقابل ضمک؛ این تیم با کریس رونالدو قهرمان لیگ خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/22223" target="_blank">📅 23:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22222">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcjZ__jvgnKMJjKTppQyPLpsfCOUjMQf2QIiDtniH_cVW5UBytgYea1fyf5HyAsjwT9SOM1Tp2r9OO4N5zbyhB92tthv-f2VuXwAIGkpdMY1G8TLyJwdZyNz_QenqZ3KwkB7l_2jYNvdM-pMt3EjRgbujD4WzCcGKDZhDuSW4dLzyi6Opm-p1FzrKr7Vb_vVN22zBKzc7kRGbkz6dC9c9T3Eh7lYX2jNFE4vSFv_e7pQXIly8xO6JxqmQW_-RWoqhFZ053tRfwr9BIjHJiOHIkUPdaEvBGAxriryUdN9K7CXvKF-Wa6wELJj_9WN5X03vBomE22Jcvk_9jyAG_cL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/22222" target="_blank">📅 20:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22220">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8cQYhvRZWAFWsBXDaZqXpFgqCBaaNaqnz6q2HUa-tZIIWy53TlBvEmpCuKImKRPs3UCnauUgJF2AbDL5F4RVhHIUqDbbrmocLs2UFYcGu_4P3YdQH54lrqKsI27lF0nDtA41x6MsaUgSQjUcXMmbey77k2qvqQ3FHFBh_V8T6a5NvyffQe_Qv8qpZd9hoJNv3nMXhwoq2jQB8wNyyvMORkWZuLnfwRAmnxCd7AfR7Bcp9x6YuHjc_rBXdLKYpDAlwnlZaEIWcGdiuCc_gsSEII4PTjtE1QKu-0aAK6f7UfG9wVzaXyEGt_34XlnJrOaVsHfmA6LhCZ3Kd-icQtnUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام فدراسیون فوتبال؛ باشگاه استقلال مجوز حرفه‌ای خود را از AFC گرفت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/22220" target="_blank">📅 19:58 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22219">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfIULezMrRB4TnF1C_A878Ffp_6UCA2jn7I1wV1TXw4w49ZVb6OOgHaIuN6_4FlxrPPRqgOzdIfSCmIv1jOR4padTW2m1cJjBU2uhNamOPuj-6WitXb2IoUU8fRv8-4j6uj_4mmr1kHRF1BXjLoYVA6eoXGpE4deqEZZE7ErNZVws0aBzST5ENiRGsetY1iKhq42CtX3Fd7tB7ZCyQyGM_3Kj6Iw6PCl6w5bUR5MPCYDvBQEm52IRSfmGOKN9cfmAF2HqXI5PGqFZZAzJvHzStOf-Ppcvq8nALE4nlvk_n2bas_WR96zdtNzOMV6QSDXoggtXwf516BJYPniTgxxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتاییدیه رسمی کنفدراسیون‌فوتبال آسیا؛ مجوز حرفه ای باشگاه استقلال برای حضور در فصل اینده رقابت‌های لیگ نخبگان آسیا 2027 رسما صادر شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/persiana_Soccer/22219" target="_blank">📅 16:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22218">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmYxiZkZbyGSQOgiU2XuOb_ZRod4ia8t3Ey7E0lJdCKaaZY1jOINGIem3QPUf9EFOoY9TnvqmPznClonFku-ygZVJ_Ll4wCa_O9J6BAD22Fioavc7urrPXhvdm7LWajRoJjLIBy-dtL-bU_Eed0ArlecnU8CoPeKDNh0Uq4Us0yOz6xrwW_bAHiBbwND_nLFrhZVkgYm1D5G3VQ6QA1D7RDh0jd6Yk2sirio03rKvxqXdBNIv4-xnPSC-0sSPsAiCdWNzgikQNHXO75s1bgCyu0CgDePTDHvUVJABUqCKH8wD3SwfQjK0kXphUW14tmq1okCm66gHVuqjGgZvm-ekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
صحبت‌های نیمار جونیور بعدِ دعوتش به‌تیم ملی برزیل برای‌جام‌جهانی؛ نیمار کاپیتان‌اول خواهد بود‌.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22218" target="_blank">📅 15:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22217">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUl_Ge29gualHwH0BG0nnvq0-IpHxVv1gSFIl_lckiH3trFZuRQW55vMxA0-YryHD90yneW31ZuOS8yREh2dMZRzHG4xX-6EWAjC42K8xrUwpJd2LmWfeVbWJsFa-KHjKR56F5CwaTh9ZOONmX3sUDo-HwQZPLvm_1KPF92fz9IZ8sifSSS-Xt8B7owJ8RXOMTNZVY2k_rgLX0wzlzFh9BBZFPg9LkhpB6bN7R8AxY6U_oL41E4nYcDDvfTJJDbJ6XfUwAo1M8ltDxoWOWoCGJmBv5Ia6CCUBjXOM73sAGiN799K2qCf1qG-kbJGMwa6L2rTPgXDapXYMIP7foUz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان 22 دوره اخیر رقابت های جام جهانی به مناسبت چند هفته تا شروع جام جهانی 2026  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22217" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22216">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmqE1U0l2dOYSQkfsl5-GnbA0bB1QBVfxX_mY8ZJDbFygQwCYCtgBBDxoiEJet05uScA36K9QQGMmE06HhhjVa7LbY_3I8vv01QUhn1frBRvgmFSzoWM9xODRb08MuYaBbK3qAhoQgnmcBv29tYDvcmiRame6HBL1cgL3Z16XAjF3MCw9FA54JRL_NLOOl1h38qbru7mrhAa7d_fMsdtxlJFuOTUJQ-1BnJJTcarhbcTOXoOPoEeerrC-fqWuTvJYFKrxeGnMEfCYodK9N5JDxsfgtfTOJhBJZY2WTmIm0XTNsdJnHagowOXJk9cYJEMHXDvueLK2HMQy9hq3vkx-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیشترین حضور درادوار جام‌های‌جهانی؛ تیم ملی برزیل با 23 بار حضور در جام جهانی رکورد داره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22216" target="_blank">📅 13:11 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22214">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nLoapr5JX6iWB4CCgJIy8gCjbUbVeWY1e_1TD8vW_9nj3QXWfjYM8CEvwPvl5MFNDG0KN2l-WVdkC00fQIpsmE6K-ADJMBKhSstHHceg8QFzjM9c_6yzsU7drQ8dnKFRHYwVdFOPeyzkZhgmfmt2hSrRPFNiNl2Uv5CAG8H9ARRWtpZwxxNF1zsMViNPaWp_RyvqRXF9USkYQwJfi-Rr97DRCBDLabzbnxKCDaDT8AsZsP2OMYlydKtsd5PwG8Hv9rXpgaKXu9Dlk6bRbXLVWmQ-gApiKeAEem_wbkQgFiv7-Px27rMRqfVs0NqEZ6bEoIJOs3PIYRzZbg1u18a19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fri_E6-qusu6RUKOX-8gp-_7U5GFCi69hxArF3FSj56-dUi0qt63OD0K_c-i3XgZxQONKdudletq0JyZTh9Vdqg9J7JWro_DCgR2Gi7GJHL4U2rdyj3xg11jRDmcorccXfrAkHut0OkZBhP-NCmBCRzhwYxnWn23B1tcngZ7YIHRWRK0uX2YI_xahjpyv_9t4f9xbJdfN3kU0mpB2LUAafs34A6I2gFUvnqeNGqy1jak4Vdian5S_8Hx7I71sBWAtZY5Ugsgw1I3bjWJKqf2UPeu4Ow6zBffWAbk22VEGmCdRHPkgHtwvIWy1uVZeBMroCoshepe5kDDd5wTwjDZJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🇧🇷
همسر مارتینلی ستاره‌برزیلی‌آرسنال: رویایم قهرمانی آرسنال در UCL امسال با گل مارتینلی‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22214" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22213">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKwA1x-hYX75fgfdrWgGykOvUiJJUP97p5kCh0VXYgIxh0xKhOeXz-Wx_u8M-XFYlS2u1ts5JGgmq2oQadQjpTkrKfm0cWcsqRjLDF2RxvJ3Fkzxk7K4H4qVImSezzJ1zxtDcW7NNIMsGKSkwGC0yIdl-Uo1jLhWgVPawSQdDsVr586z7yEf-B5YdqXj3vPzjLNEVW606T4vjG3lQj0Z8EH7b-WLECbRbfP2C6KKqQBQODNH6kV_7xSvWwrD6AkeyPF8zqmpI3uktw3j85Qhc3Iu9Kl7AG5pRr-mUb8uy57dgqdSXFRfWXLZKXqW23Wzz_caAGPRoxXxuqdExoGPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روزبه چشمی هافبک ملی پوش استقلال نیز در تمرین روزگذشته‌شاگردان‌قلعه‌نویی دچار مصدومیت شدید شده و ممکن‌است به دلیل پارگی رباط صلیبی رقابت های جام جهانی 2026 رو از دست بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22213" target="_blank">📅 13:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22211">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r207fID91s3fXU7XLe6r4T-pt1KXwoXtgjFzO4TVsHEleeNRQDuCiJ_fehcFNYjHzIPJq8qCLohIXiqM_Rp0oElMJeM4HIraORcIQA-hFOA_rBzDQZfFEet3Z17T1qudNbeHGisWWc6dbQIJcsYyaHw1dNkGovnWKG9e3c0XMutt4snLoXKj9rUL99eGvuLWAlSjob8ESbEGLXJYh_r3IHXYCSfwjKjT3hqWx-n2rSYYoRymqkF6se2zwCVZm7N-Cck0p3a56iFGGFNECdXWprwiCJ82tGUpBfMlaAvNx8isyEX7WTqhpbj87r0ZR_6IN9cgJBmfaBmg5rpU7traJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بزرگ‌ ترین کشور های جهان براساس مساحت؛
روسیه با اختلاف در صدر، ایران در رتبه هفدهم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22211" target="_blank">📅 12:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22210">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQHBZepLobUQXa3J6LK3HsPT8u8P4AKLsAgFhuFw9BUalIwUaEBylxfxR_Ijm3a9Nrb4dYIvSTLFh17pZ4aD2WuChOZAVGUBPvMwenLZqxBJCH1ubDDxSU_6ja3IPM-Hu08SR_Rl6r6B7mZTnDGnKUBpy9tZw985uB0A7JF-Ld7c8SGv4NtMktlmk3uriPE3qRkk0J0Yj8RBy_ozcpDten49D0QyBSpJgnppNHiqb-HbEhIqqK-1Q-Q9ec_gnxBJr3EJN7GitJjwGoT_nncbpdbrnzL4g0zRalseyFGpX5LBpiXIGKIDJdhi9coIfL1gZtagE5rPBcw503kWo067CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق شنیده‌های رسانه پرشیانا؛ باشگاه استقلال ازشب گذشته‌مذاکرات‌خود رابانماینده شخصی روزبه چشمی برای تمدید قرارداد کاپیتان اول آبی‌ پوشان پایتخت برای فصل آینده رقابت ها آغاز کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22210" target="_blank">📅 12:34 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22209">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgFUlWRAE4FhgB-puiB_Zw5CNbb3M6HkdJ7bw1WwLuuYBy-ZNyydmbB4gP7jOqbrc35MzqCklCbcJE-nJ7PGFGGjAPxPm-DNf3xJ7pUW7IL3R4s1piHQhCUhRM-oh_N1SRT6pBYRkhUu0APtmgfbHEj87tZ-ub4rNSZ24hT-JC7gvpdwYr-MW-4T5CECmcfS4G4aEiPRc_5Vj0QU7bjmFNNvXqPVZo43xkAzGK-y_LIL-ZPkV1stTJvG_U8Zwy28_4Qc26aW5glM6IUhHHUbCQAG0EJDjenVlAt8gIOQrmQchojQRjmN_uD9jaXocqzC-6za-fbrnp55V5bS2jtu_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اوستون اورونوف ستاره ازبکستانی پرسپولیس در پایان تمرینات روز گذشته تیم ملی کشور از ناحیه قدیمی‌کشاله‌ران دچار مصدومیت‌شده و ممکن است رقابت های جام جهانی 2026 رو از دست بدهد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22209" target="_blank">📅 12:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22208">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMzMxZD9xKG99zUACQm3he6ZN1nuKopQiBzrgZ1XDL9RoLMiL7fuDMdlYOBaohq3cQBEJ5iv4nT7U5vlNeGSWUc3wtRFU57olbDO9V2cCnzMUoAXlYnMC-UiMxrJZjPkUHHJP31S9JXbZXNJJiURSHDuyXVkwg2JhD2gFKmC5Cu7W7_NtVLp9NLU9ToaRIBxAwrMyZJt75WMgrm3VX701Lkku8JdrN0qJ1bfuEJTZMoH4Xf5ylfCjbd-_qZ1QNw_E8MpR8Uzj9mTcdkvur6ciQj_9lFMqrtVyjNTG1nV8R97iXmKKANIXxYEaextM3LIhcHHXdgg8uJ68vJIXFEUDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کلی کریس رونالدو زیر نظر ژوزه مورینیو به مناسبت بازگشت دوباره ژوزه به سانتیاگو برنابئو   @Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22208" target="_blank">📅 12:23 · 31 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
