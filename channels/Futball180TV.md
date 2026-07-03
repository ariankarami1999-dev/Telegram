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
<img src="https://cdn5.telesco.pe/file/hUEp8XfCtW9Z6zlJulYiyVgtsTiHF-ATVrStROt45Au4lncQBrxpxkxE7MvsHaoE6Zzypv5CecIUaIn9aYTa55D7qhKNd2Vngcow0IOj6Umwcwd4b-edKrosf-w1w425pidIkYSQV3Qdb7y4ZL2MrwEUyVKmuPjcVKW111328VUdbsaei5kQxiNrTjUSLn4JeCOXsUqvsKrI9lzosuOI6nBw6JBlGS3gM_Sz6SXo0_e2SKkn-e25XQe4MakN7q-C4pq7pVTW1eKe_F5Az6keGmkQ58VWRcVod2aEOO1fLVT-udjXUOk75JkbwNwi3UguNq6Que5AjQA_57XW3YpmiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 649K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 19:49:21</div>
<hr>

<div class="tg-post" id="msg-97896">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUvO39HpiYU5mZMKeYBPJ0_1gj2nGFhxAXjOZMZoTOuKY_HMqToKdPSbrn-MOHw2j1-ZysMHDeUcgcEDLIpIuRP1WAaQrHcB6cCnACMEIa4R7opQk4WSSfIUFSAm3j1vaa7aaPl0-Zd_YPemJEeAx6HA0raOq6Q3lno6MF1tbCtVLxPvpujPa1SwkcSEolToOlWtWm5hEXBZhyq7sc8aBBqkhU3m0s3gR6fdivsOrRyMh-xcDZ4h6XR8hdn67KDoE_UYMLGxBUifJ8JAPavNeOmCW5VVPetb4C4H8_S5lmjUgn7jwSB5831p5gSw_F1VaNWX3hqIEVNvcn6dyLn7WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با انتقال تونالی به تاتنهام، نیوکاسل که ۱۷۵ میلیون پوند حدوداً برای این سه بازیکن خرج کرده بود موفق شد حدود ۳۰۰ میلیون پوند بفروشتشون.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 314 · <a href="https://t.me/Futball180TV/97896" target="_blank">📅 19:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97895">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOYko7SWrRejLrBMVoAWllfyzisjbOoJOZmx5HpPSZyFLKpBkgtwQWYUyiMBtAtlT0PJeF2pJ0iTpYI_K6GrRl_RUBWrYYj8Bm50lJwKD4cTSLQSqCNLWweEUxhw_fyFvDQbnFKjsog0O1Pe2HKcoqU03XauBtYZWDymvyiiKoAf9HnHqAHt3SYtHRjOlFs17-q4uAw7fMRQPpLiRLqWHcWkomwSRvu1OrL9es2l-1g1QoiIzOPM1JBfddAKhGMhtDFxQEf86v0N0OHMILsMGSs74P4hiqkKulBoFofahB3H4zUud2RfnJFGHFZMLMDxvmcbJq_X2xV7oscva8_R6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇩🇪
فوری از بن‌جیکوبز:
یورگن کلوپ تمایلشو به مربیگری تیم ملی آلمان اعلام کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/97895" target="_blank">📅 19:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97894">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61eb94b3b4.mp4?token=bM3_AUZqb9oJLiVoHUT-7HqV9ggMZslf7MA8_PbXPb7b5bpJ24A83vom26u8mBi7540DmNMTz_YmRdaHpuVVaMYWCJIZlcCy3GfLoBiIIVSDg1zm3iXGEodPy8PV81sdchn2WWPH6yn6W0RImpVj-XEmPiskR46AraPCpmuaMyZTKFDzMvO9zrqegqIswh1Z9VSWxBqF6ms7jN9kckiGHgHZICaJgatw_Lf8OH1w1yxexSUjmIUHPO36NKHGsfdlSraMz6i1yHPE88rPc9kCqjLytDLOdaVi1NfyoVW0-24dhbN-k-l9SyVvvO8BDr5h-KH2ogDUNlsB3yYqgCQhfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61eb94b3b4.mp4?token=bM3_AUZqb9oJLiVoHUT-7HqV9ggMZslf7MA8_PbXPb7b5bpJ24A83vom26u8mBi7540DmNMTz_YmRdaHpuVVaMYWCJIZlcCy3GfLoBiIIVSDg1zm3iXGEodPy8PV81sdchn2WWPH6yn6W0RImpVj-XEmPiskR46AraPCpmuaMyZTKFDzMvO9zrqegqIswh1Z9VSWxBqF6ms7jN9kckiGHgHZICaJgatw_Lf8OH1w1yxexSUjmIUHPO36NKHGsfdlSraMz6i1yHPE88rPc9kCqjLytDLOdaVi1NfyoVW0-24dhbN-k-l9SyVvvO8BDr5h-KH2ogDUNlsB3yYqgCQhfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هالند تو ملیت های مختلف
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/Futball180TV/97894" target="_blank">📅 19:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97893">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecbf79b99b.mp4?token=q9Ar2rpY6cM6nIAEDrIzpizsNk87rw1o17D1sxb-bRvRHOZras82RrGn2SgCmglQXOYkLGyNLqF-MGLzIUJo8f7b0b2BfpPnUAW8HqqycxFTcljFAKwqQX45npBVaULMxMxbCYNVM3iQ0f2p69HSv4Nx0c_uY2UpTfdNn4u9VxNhUFcQAu6bUJPp4gxMj42QF-Zh5Ozy61ycsJMCLg-u3RUAN7GvME9TGJDWDOnQDKFCBQeC2rZ9krvQnK4-YJLLN3bECXuY8Xbur03ntdafjTxaN4NHC3pQLj8ADTHnVPtsvh-tpXFcJ3-r65Lnh9Vn2lChVsu2H6s96hb3N_jV1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecbf79b99b.mp4?token=q9Ar2rpY6cM6nIAEDrIzpizsNk87rw1o17D1sxb-bRvRHOZras82RrGn2SgCmglQXOYkLGyNLqF-MGLzIUJo8f7b0b2BfpPnUAW8HqqycxFTcljFAKwqQX45npBVaULMxMxbCYNVM3iQ0f2p69HSv4Nx0c_uY2UpTfdNn4u9VxNhUFcQAu6bUJPp4gxMj42QF-Zh5Ozy61ycsJMCLg-u3RUAN7GvME9TGJDWDOnQDKFCBQeC2rZ9krvQnK4-YJLLN3bECXuY8Xbur03ntdafjTxaN4NHC3pQLj8ADTHnVPtsvh-tpXFcJ3-r65Lnh9Vn2lChVsu2H6s96hb3N_jV1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازیای نصف شب جام‌جهانی هم دردسری شده
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/Futball180TV/97893" target="_blank">📅 19:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97892">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/l3Z-wRnttdCm4as1Pp0_t3v_lb76Qzg3YzPdA1mYa2g91Aeig8HIh4hEs6gpbK2J-YTIIxb9RtV6fbr46MebOZ861kg3UrJr8apN1xXhp3SF7KqoVK25T7Kr5GtaXtyEw4MnM2B84brno-rDmGD1Lw6KRZlmCHHwFc7KgOYkdmL6Hu81uSa8m_COnehjqLHLoFnDP9mcY_pUKWFXifTf7Rtvwc8qJb5q3zdmiuVDsXQorTDDlb-mGtpqupkr41ng8NJT5BjzP5qhrAHqt2YbIKiZ0OCQHBXNsIWDT9eJXYv2DrhWry5Rsg_w1vciPFkkFXlXSc2uBPtq4gxVnltTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/97892" target="_blank">📅 19:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97891">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">😏
😏
😏
انتظاری که مردم از بازی امشب آرژانتین و کیپ ورد دارن بعد پیش‌بینی جادوگر غنایی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/97891" target="_blank">📅 18:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97890">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5205517f12.mp4?token=aZT2OpatCPYTNas4h9fa5-vizrJv95NMo3t39LB6ozYvrqlmMWxp6c-cZCOkyFLOR3-AsjQ4ocY1K1HQ7g4rcceLLpgFsyxd0xwOH8jLjUWP0BamYenaLYjLKm63LNpA-mTtdisPreTISkGBPXEJfHBlTPfiV_WFVp7NKpy8RlZ76D4NoPFG0eQJmwE3wz2XPFk2RA5MD5q6A50mCTZiwlsPUUsOAvf9YhnLNjmjqIZSyX63Orv7w2rbTbOhukJ2e2dJJQAMEBvVPwM0RVenvZiiSqf8wu-lzev2LcABR6tIiS2oG4bZVMdxADCmmkdZoZ41xQwTuQtdEmDnsJRniw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5205517f12.mp4?token=aZT2OpatCPYTNas4h9fa5-vizrJv95NMo3t39LB6ozYvrqlmMWxp6c-cZCOkyFLOR3-AsjQ4ocY1K1HQ7g4rcceLLpgFsyxd0xwOH8jLjUWP0BamYenaLYjLKm63LNpA-mTtdisPreTISkGBPXEJfHBlTPfiV_WFVp7NKpy8RlZ76D4NoPFG0eQJmwE3wz2XPFk2RA5MD5q6A50mCTZiwlsPUUsOAvf9YhnLNjmjqIZSyX63Orv7w2rbTbOhukJ2e2dJJQAMEBvVPwM0RVenvZiiSqf8wu-lzev2LcABR6tIiS2oG4bZVMdxADCmmkdZoZ41xQwTuQtdEmDnsJRniw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
اتفاقات امشب بازی آرژانتین
🆚
کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/97890" target="_blank">📅 18:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97889">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwrAN8EhZbtjHFRD51mbtTw1z4RB4D-W4JmVqPvUtNgQzB9kT8lzkaD3MerS6h5IZlpWO77RzfBNvDvC-hXCU4CB3TYm9Ogg4Enug1O0J9KW5tT09zIbAn4KpUrYQd6OYhhqKrr9K1ks0R6-966oF3-DdbXSY8BQ5Td9cJdS7fm9jgtDypZweHoLSrfeQf2mhBCnoDzzZQV8lNclNrOC8v36m8hCs3ZzDWrb0vkokr5ahWRbzPfg1k0lYBDdEyhHO4YExtI_qn4gBBd7AD-CAPjyVrAMZbI1XnZL1sUWPHaVkOEGTc4moscMgBl8o9k4LIEylKfZZUKSw4AS6cphiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#رسمیییییی
؛ ناتان آکه مدافع هلندی تیم فوتبال منچسترسیتی به فنرباغچه ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97889" target="_blank">📅 18:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97888">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94c7d6c007.mp4?token=C7JHqVfrhNFCuXrtjdcayDYt6qh_EPXgPQteZIbYoPZgKuYVGbvFgcMdWtkKCLfvP8OcM3ultpS0eStVIbXuc_N0m2PqaWMpHyC_dd92cwfdQ2BNnQDLFowSjL-dGzMsUxgbN6--zLj_H7huIlj0-rekfqtXo7oUGE7S4YicXKHo-AfNYEbKblb44PbKaLgjPfAkZluSGO5iSOZNpFF4NiiMhhD5Zsie83Dc1xFTQgpz01hxcyMBYSnNm2t8w3KsBy_AuQ4GfF_-TXF0j8vNM_mueWuAg3K1My50ttgH3hLQXla27UxlARrKRfsGz-LVIDttUWTbYM1eyVoXWDgqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94c7d6c007.mp4?token=C7JHqVfrhNFCuXrtjdcayDYt6qh_EPXgPQteZIbYoPZgKuYVGbvFgcMdWtkKCLfvP8OcM3ultpS0eStVIbXuc_N0m2PqaWMpHyC_dd92cwfdQ2BNnQDLFowSjL-dGzMsUxgbN6--zLj_H7huIlj0-rekfqtXo7oUGE7S4YicXKHo-AfNYEbKblb44PbKaLgjPfAkZluSGO5iSOZNpFF4NiiMhhD5Zsie83Dc1xFTQgpz01hxcyMBYSnNm2t8w3KsBy_AuQ4GfF_-TXF0j8vNM_mueWuAg3K1My50ttgH3hLQXla27UxlARrKRfsGz-LVIDttUWTbYM1eyVoXWDgqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇹
پست صفحه رونالدو از جمعیت فوق‌العاده مردم کانادا بعد از بازی و برد مقابل کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/97888" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97887">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGkf5BHYXHVAsuF2YaoQDkklEy0A1z-1yVzcebWiOVXQZraxAMKOFDcs53_ZWe-MmHrqMGhPdRfl82AMx39hT-0Dr3q2QX5J7dyd21LSPKtZO8zDaLb5tetw29DWO4ECcXRgNz6Y4ONGdHocu7aDRPrRuu4wiqALT6J46F0mIpaAFQ-NzKh1SZaZywNjUtJs5vZdK4Q62Kl4Wzmi3BKeNEyanl-X4yrP-R27QKehrcsbyG3cie_TsOFlkuaHWNOl5vi9iSETV2lRVr4CK1r0H8F0aOjuJta4ZIUVB9BQCkArnJ1_1AC4zXaeLKUYkUqzh8Sjenp0_m-BHhpFzKHGeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
اسطوره مسی در اولین بازی حذفی از هر دوره از مسابقات جام جهانی:
🇲🇽
‏2006 | به عنوان بازیکن جایگزین در برابر مکزیک بازی کرد و هیچ تاثیری نداشت
❌
🇲🇽
‏2010 | به عنوان بازیکن اصلی در برابر مکزیک بازی کرد و یک گل ساخت
✅
🇨🇭
‏2014 | به عنوان بازیکن اصلی در برابر سوئیس بازی کرد و یک گل ساخت
✅
🇫🇷
‏2018 | به عنوان بازیکن اصلی در برابر فرانسه بازی کرد و دو گل ساخت
✅
🇦🇺
‏2022 | به عنوان بازیکن اصلی در برابر استرالیا بازی کرد و یک گل زد
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97887" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97885">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHHmJaFh_i6k-tkhlSi8Eojla8mc4oVGfynfT2Duth5B8E5zh8BJ-JT90k_pLOTbDO5BBPb6h9xA_6FESFswtXqyBw2IofPykDcd_1rUxjuSyRCLhar0b7JExi63aXkz4N2eZuN2UokwORbRhrq_vR4ey461rX163Wg54Uu0jq818_XC7ch3oT5_D6q6QSPnxjkSoFlM231VuD23k3wlRhS6a5MLda3YNbarzgGGpKZSoC9nmkFhrXF8-fWsp1Mt6J7vejnZhewq65BdLRAn_UoHSzdqnU8pd1aBtWBdxyaQF24RfXZ1SaiSXJ2kqj_QNlKp2Zt8_7pNJ2bgpK2aNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPy9EEB_3AQunj1TvUapQrFi9oN_sbOyJP0x9wosenA2Bm4fQGo_JVWHhJjdhov7J2qPbQpN6TZIXmffmwt160gSqj8HBLJKMeztAONtgQep09NXBwiFywN5brAW4F4UeE6beqdeaTNAh9hdnHa88TZB5zvKDlVflBrGsb1xPxs9W0T4CuJZ91dPXX2PF4weOK50uyxgQHwNpBoR0O3JzyhPl6j_rrSJ05AmtdtFqBCpFUjgK2jLcMmA1OposYR3KvzxTaxT5c2Zgo8D_BTpnQv8DvjbViInJESoXyHFGt0ExTbD0k2Ysu5pOklYFQor--ZdGD-Big7AekX50cfKxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
📊
🏆
#فکت
؛ تیم ملی کیپ ورد 22 موقعیت گلزنی ایجاد کرده است، که بیشتر از تیم ملی آرژانتین (19) در جام جهانی تا به امروز است.
🤯
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97885" target="_blank">📅 18:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97884">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WT60MVy0P_JuTcY1S7Ze6oym-0fEvLfZT2BgBSyoo0ptlr5A2iLLJ03LpIN8XyC_aPXUI57hk275smysBRRG9RY15wzfX7YcjhBASfiKmThWP5cMgW0tyaWgJEgo9CLnkn2jPjwAV91zRksonFZ_E-W1hynUbFg6xFkeDCYB-701XmGhNKZUWjAKK5th-chI6mkdcLcqrh7_jnbXcduq-SScObpraBlUMpvfkhHEn6rgeZyUrdKmd7ztB2lsEM4095kRCHvH-vMJJDjqNEmQzVEvpoeSYSSK2spkcOIkUgntdSg1gBsN7xaMvpUYFI3btlnqMC9Ep-nZ-IAH6eZXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
🇦🇷
🏆
اسطوره مسی در بازی‌های مراحل حذفی مسابقات جام جهانی:
‏• 12 مسابقه (11 مسابقه به عنوان بازیکن اصلی)
👕
‏• 5 گل
⚽️
‏• 6 پاس گل
🅰️
‏• 11 مشارکت (گل و پاس گل)
⚽️
🅰️
‏مسی، به همراه امباپه و پله، از جمله بازیکنانی است که بیشترین مشارکت در گلزنی را در تاریخ بازی‌های حذفی جام جهانی داشته‌اند.
🐐
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97884" target="_blank">📅 17:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97883">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d6124f5f.mp4?token=bYJ5dE6HYZQFZTq14j6RTnQ3oOUYTJ3dv8oEiT23Nm923rHyLSEpxcfN_L4oGAYWT8lQj7j_oWiXQYw3mBPdj_R9SnLGj-b18LlNkq15BBNwa0mXPGLIUxuwS2HYIw_y_us8G2dcTGGKCbZRFDRbjNGIg-SBl47GTAmMANJ6vWk4q5Wlk-pBUxQOOjBVzfySnQgj0W7PRrVje2QoHwZGRnu6hRxIMKo-mpOITTBRWJMdVm7ZZnFs41KC4mLft5hK2f83vMXcYODTx19pM_C0oiN8jUPW8cs1xLuC7mLoAgXt1wvtJeu8kydW7LF9vumMA_CaAgN8oKAwpa88PUgUVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d6124f5f.mp4?token=bYJ5dE6HYZQFZTq14j6RTnQ3oOUYTJ3dv8oEiT23Nm923rHyLSEpxcfN_L4oGAYWT8lQj7j_oWiXQYw3mBPdj_R9SnLGj-b18LlNkq15BBNwa0mXPGLIUxuwS2HYIw_y_us8G2dcTGGKCbZRFDRbjNGIg-SBl47GTAmMANJ6vWk4q5Wlk-pBUxQOOjBVzfySnQgj0W7PRrVje2QoHwZGRnu6hRxIMKo-mpOITTBRWJMdVm7ZZnFs41KC4mLft5hK2f83vMXcYODTx19pM_C0oiN8jUPW8cs1xLuC7mLoAgXt1wvtJeu8kydW7LF9vumMA_CaAgN8oKAwpa88PUgUVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بفرست برا اون رفیق فوتبالیت
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/97883" target="_blank">📅 17:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97882">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ1DOwVQ32FGpbtjsRY87XUBwNgX9bNCY8OqG6IwAF3vIfTJLf7HUR2ORyPFLuNah4L3WSUpG2dAmvodFnCzi0p4JztU5xw5-gizDScoOzpZabClX9m_J5GjQG0oXT16kpjLZpoMFLpsnv56glxJ97GrYNBPvvgEwpkkJbIkT2i5v7RJX3uaMlxcH-D7uTBs2KwgMoxUE2UlnC1y7sswECBqnJwF3efMKSJqRH-I2ZO0ls31m7_S5YwDyGO18UAG245wZjvEJ3ayjieR8xPVP9g4ggHkf76GNYrw8mQYw9VxY6KcEtT7Bt7CrSpqRF7vpPW0XOpkuuiWlGV3CXwWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
اسکای‌اسپورت: فدراسیون فوتبال آلمان درحال بررسی ارائه پیشنهاد به یورگن‌کلوپ برای جانشینی ناگلزمن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97882" target="_blank">📅 17:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97881">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtiNSnNPId3PXf7G9CVgcuZoKotImmKMB05LGV03hvDSq2ivaEFJNc6tYUSsPqoLUGC3D5OKvjKddfo86MZjG4RWmyEUx7P97zSrMm-HNihn4j8Z8iUOvNS5jFlvnJgN6LoR8Uvmv-jDjOWwB1iC-F5FvP7tgVRY3WfETfDukeU2SfhOl7AW3uAWzss-9n_nlDMhFoIvv2eTrQJxbZ6fZpv_S2W0wNjMN3OOPGyrh8ccPnJLLJluT-xnh4hQXsqTptdP_qgEIjxcpKnpPtOM9xE_iMQ_9I7RgWOgf2uYOqya7_G-UXA0s8C2vba5NsOitrruQZiZCLAYdUYpvj-giA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاقی که برای داوران در جام‌جهانی دوره‌های بعد قراره برخ بده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97881" target="_blank">📅 17:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97880">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/497eedaf5a.mp4?token=ZWgZo_vKF9HrRM55B_dsYx7I_E8QQ5yCoNiTve9bdNVGg7gjEk68lbylzF7hU0aZlyZ2ghKDwBG5IfDLhIYMQP-SxvywdnzawYAD-rW3IQOSVD1ujfSBrtgqkYb_pv6O3VR1UQTvtXGd45W58lQ5l6vL9AShV81wkb0N7UjDxGkTqe5jR81SvGGF_20e26etFgVPu9sTLV0DdI799o05VO6syaT-Q4sxcNJWiQhtbpJvHcZt2M4lHi3D8gKVffnN-a06pRtTPnskYJHaH9EpoRl9wZARWG-3fNgUc9KMBRYVwW-D0VXlFWpbELkZf27MQQsn1CeBhZdBuxWRD_kVlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/497eedaf5a.mp4?token=ZWgZo_vKF9HrRM55B_dsYx7I_E8QQ5yCoNiTve9bdNVGg7gjEk68lbylzF7hU0aZlyZ2ghKDwBG5IfDLhIYMQP-SxvywdnzawYAD-rW3IQOSVD1ujfSBrtgqkYb_pv6O3VR1UQTvtXGd45W58lQ5l6vL9AShV81wkb0N7UjDxGkTqe5jR81SvGGF_20e26etFgVPu9sTLV0DdI799o05VO6syaT-Q4sxcNJWiQhtbpJvHcZt2M4lHi3D8gKVffnN-a06pRtTPnskYJHaH9EpoRl9wZARWG-3fNgUc9KMBRYVwW-D0VXlFWpbELkZf27MQQsn1CeBhZdBuxWRD_kVlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
صحبت‌های بامزه سیاوش خیرابی راجب حضور در برزیل برای تماشای جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97880" target="_blank">📅 17:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97879">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlMn_M7XvP1dv6i3xQ_TxbisXuxYEuZBGB9b9GEE_nfaunsQQ_2g8onehSPtSuOkGPoPZskppu-XIaeP9HQL-fBgrvy3lxZXpdgTbR_HG849ItuwCbkjC9MQH91fOjz4dhi9OBy5bPN4wGIVfp5Cgr7wE_bmMCBH3HmdcnTg_Aasohk1JeAFEYixeRd0HEf389_g7ceWK3EgixU_yP3bVghdsu-HjNpDtIisQmX0WdUGX7DOnIQhkn9xE3ra7RhKWtLi4AGuVMjjjeRNdZPQdHNr12ZkRLn4SyUT1V-LqI9uKT4zq10zldMikI-lwbFwK3WPlgC19C4sq4mqbMYdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🚨
🚨
🏆
🇹🇳
#فوری
؛ فیفا پس انجام آزمایش از بازیکنان تیم تونس در‌ جام‌جهانی متوجه شده که ماده ممنوعه "کلنبوتیرول" در آزمایشات دیده شده اما این ماده بر اثر کیفیت پایین غذایی در مکزیک بوده نه مصرف مواد خاص! در نتیجه هیچ محرومیتی شامل فدراسیون فوتبال تونس و بازیکنان این کشور نخواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/97879" target="_blank">📅 16:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97878">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mx5Fc14wqqZ_KgFe25-mkJQth3Vhk2ee6f6SDrDQ0kZe9CQdXkA1GDHgwrv0h6Mz1owbGlLa2UCCZfiCOfFZUiSwJfZ3GdaXYUNmWASNOmRVY1kIuQ94w1b4v3IUF43gk-Byv2myTbfVGhzrAJ58e_wdrxAQ5FE88ARwwIvIVaikzOHcLkBuUWDeDZfVKSQx7fLcBaNMF-uMOILez6G-Q1K1Ja8SVwT0oX2Fi5jSEt3cq_gaHvm8ncWusqtC0Q4XSZVRs-ZqcuGP7J7_z60a7YKrBbX9ygGVLR8E5QTM3abMZbfMYgeKf58tcRXNQf0diS2VF70-yfHS618sXbEFYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
سپهر حیدری اعلام کرد از همسر پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/97878" target="_blank">📅 16:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97877">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYdwXXkR8ZbeJyzdx8pmZ0oKDVapEa3cxavl2W-uNncQyTvU6zLQs1TmdWJjNVTaqOVkdTHMPvSBLbpjLYF1AhcwdVPKZnkqpC48vEZTMsjQuQLdxTYGwVhWsUDyYEy-B41mu2VXDN2bSXSv8np99CjmR_UOefStFnblWLS8vEn0OgFDOssG9WAQ8ej5WmGdVO1BKa6ocFzi4AYsYYln3GiXlH6dDBP8MHTf9EnNoIsFIHkfBcn_8cVFENMGsaeHuXQdMYVlC-M3hsLGlBJfXLEG_VlqkySSTVfObvrOFDJRBPP8Oubnmw1fl5OLnxw80yvBk6q8qtLHgvOd_xaUvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارلمان انگلیس قصد داره به پاس درخشش و تقدیر از هری‌کین، لقب و نشان "سِر" رو به ستاره فوتبال کشورشون اعطا کنه
💥
سِر هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/97877" target="_blank">📅 16:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97876">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50819de74.mp4?token=IEK5oS1LJU_vk1Rm4fBe4D8BvlFC8A1A632zfx5Fx3Ih_MK4zEThQLTbFjuosSxqC5NmUebW5rUcDoXdeetDgVNk9AvshQweXknqee5EeiAlQeLZTieZ6c-eZ0SaXuehVi_5MkF8BoTcobLpppcipm3Zh4O9TI0ZIIsEvlPef5HhLUWR0Y5M5v9oh_AktbY26x_mceqBeulkeBhM_rCjTTxYj6uoMrEbPsUsME0949Gy1EjiaDUNLVZspoqpm5e0htLDzmtmbRarCiO8sBxIapAKZiP7X9xSXBn8kBVx50MbQD0ZK4e-pUsxR0ai6Vk1tWQS_lBmFNQiapUO8_pNtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50819de74.mp4?token=IEK5oS1LJU_vk1Rm4fBe4D8BvlFC8A1A632zfx5Fx3Ih_MK4zEThQLTbFjuosSxqC5NmUebW5rUcDoXdeetDgVNk9AvshQweXknqee5EeiAlQeLZTieZ6c-eZ0SaXuehVi_5MkF8BoTcobLpppcipm3Zh4O9TI0ZIIsEvlPef5HhLUWR0Y5M5v9oh_AktbY26x_mceqBeulkeBhM_rCjTTxYj6uoMrEbPsUsME0949Gy1EjiaDUNLVZspoqpm5e0htLDzmtmbRarCiO8sBxIapAKZiP7X9xSXBn8kBVx50MbQD0ZK4e-pUsxR0ai6Vk1tWQS_lBmFNQiapUO8_pNtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
خداداد عزیزی Core:⁩⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97876" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97875">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgJaeMWUYce7-Ua6o1gUEGHSJ1fUxFlNBoKuJEGb2Q3I7jGhLTkWVANrmjG9uLO-R65ZdGImcj-MFgnDUGLjv6MCigfSgcufzHl7WRsUnt5itzHkVRRNtclIyKXyPaaxLmCMqFBDRlnAmjI5m-fvTF857RCebX5Y3lUZWGESl2_l3F2CkQYA119rOERfYxKlRJE3De2j65yHoN6obmv3rC_v8V_fwYuz4At-pQtY_fhq9MMM0k7i1ewQQxMKhuFbob0FxEe8kCCEhsk-vm6FoxcVthMv2lHFW1045ExjmObvoAfWKFrHuDa2cw_a6bGPWsys0lNmhxWq83IpDqLtMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🚨
⚪️
فوری از ماریو کورتیگانا:
انزو فرناندز و رودری از لیست اهداف رئال مادرید کنار گذاشته شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/97875" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97874">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97874" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97874" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97873">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97873" target="_blank">📅 16:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97872">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b016be396.mp4?token=snil3OWwK8u3ZXneLCnGTG6z-qGBhaQ5wDnoaHWEUt1sJGwhZvuL5Ay-CXYsxjSnDeuqVFRP-_P9fm3Nhzi7Ic6GW48ylOdvus3BYqjN7k_LJz6iTkdgLti2SgZKJJt_UzXrndod9NStKk-htz3V2Ghqhb8jCFjs36n7wcs6L0fT1XoOjaiiXBjMV_YBnvnBNroZAvW1TLj0cI7SCy9AR-DjdTFOEfc8tj-gT-hIVlDKyhgsM3Mfru8eM2Bw3F92kLzXJ62Nf_bARg4gVhli3rUavMonLTIl4ACi7cuHEIrQFl10Qu_18mnuK43C8YiOfeRNUHa5g31LewtM8NqCtZemHL1FovJj7654Qcs3o-PkiL60C4ubWZyrPOi_pOeHbHOW-ngJfPXEcLsy91hWyWKTDUvfFTYnkgwbFm8BtdUD6TMhw-Xk6SZTL0wTvq9aK85CxRoUspW44lPQ7r7tPefLxh4XpAETaecPV2s9jM-uu8VcWQcOgCFUVOPDRRBfiVD8l42I2t0ua7nkAOpl_PB2FRc4ZVRLzFocIfFGAI_WVMq0FfpX64Ylc0YR4jGlgzWGbvFAX8pPlkzP6Ieh8joHMZ8nAK3kr6sv2nVwqliIIO1Iid2egnJqmiwKxySWqvNErSY3r1oHWydbrRHMpErO0JmgpiPpXAXjbiCxOVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b016be396.mp4?token=snil3OWwK8u3ZXneLCnGTG6z-qGBhaQ5wDnoaHWEUt1sJGwhZvuL5Ay-CXYsxjSnDeuqVFRP-_P9fm3Nhzi7Ic6GW48ylOdvus3BYqjN7k_LJz6iTkdgLti2SgZKJJt_UzXrndod9NStKk-htz3V2Ghqhb8jCFjs36n7wcs6L0fT1XoOjaiiXBjMV_YBnvnBNroZAvW1TLj0cI7SCy9AR-DjdTFOEfc8tj-gT-hIVlDKyhgsM3Mfru8eM2Bw3F92kLzXJ62Nf_bARg4gVhli3rUavMonLTIl4ACi7cuHEIrQFl10Qu_18mnuK43C8YiOfeRNUHa5g31LewtM8NqCtZemHL1FovJj7654Qcs3o-PkiL60C4ubWZyrPOi_pOeHbHOW-ngJfPXEcLsy91hWyWKTDUvfFTYnkgwbFm8BtdUD6TMhw-Xk6SZTL0wTvq9aK85CxRoUspW44lPQ7r7tPefLxh4XpAETaecPV2s9jM-uu8VcWQcOgCFUVOPDRRBfiVD8l42I2t0ua7nkAOpl_PB2FRc4ZVRLzFocIfFGAI_WVMq0FfpX64Ylc0YR4jGlgzWGbvFAX8pPlkzP6Ieh8joHMZ8nAK3kr6sv2nVwqliIIO1Iid2egnJqmiwKxySWqvNErSY3r1oHWydbrRHMpErO0JmgpiPpXAXjbiCxOVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
پشمامممم ریخت چجوری این جیمی‌جامپ بازی پرتغال بین اینهمه مامور از رو سکو پرید وسط زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/97872" target="_blank">📅 16:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97871">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374849cbee.mp4?token=TEPbvFNNGz2zV8-n3MtkZhpKyNelvAsc0DzI27RUFNWGAWW54VvoCMbQF3z2EKQnvmN97aUNVv3SFx_N4U3GSg7FDjbrkNC79_rgmtXSJHA40j9pzdSlyykb8KGPwYxWEWHhlftayxC6a1CtL__mBSB4YbjQXkO4NBwfhRsKM9eFFrtWEdkCegX249QWW27TfRBRcT3p7twp_JAGzd8uislYfgyVkSMrUIWWtuUqcwG1NCrv02n9hqRhXCXpalUuuJk1g842pOBLUfSyjUMC5I5tqD08Dfk28GcAo4QSB5zC-9nKcqWkuN_ZNYDBSAU3a0fpNB9vAoxl5JLCkCM65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374849cbee.mp4?token=TEPbvFNNGz2zV8-n3MtkZhpKyNelvAsc0DzI27RUFNWGAWW54VvoCMbQF3z2EKQnvmN97aUNVv3SFx_N4U3GSg7FDjbrkNC79_rgmtXSJHA40j9pzdSlyykb8KGPwYxWEWHhlftayxC6a1CtL__mBSB4YbjQXkO4NBwfhRsKM9eFFrtWEdkCegX249QWW27TfRBRcT3p7twp_JAGzd8uislYfgyVkSMrUIWWtuUqcwG1NCrv02n9hqRhXCXpalUuuJk1g842pOBLUfSyjUMC5I5tqD08Dfk28GcAo4QSB5zC-9nKcqWkuN_ZNYDBSAU3a0fpNB9vAoxl5JLCkCM65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
👀
چرا فوتبال شبیه به زندگیه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97871" target="_blank">📅 16:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97870">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b751ec19e0.mp4?token=YuTiObVSLY5fbi8gOjz_Az8ef05NejEh8noQq2iqfIqJAnm9gRv45Brn3fyE4Fo7yyif7jskn4sUqa_4aWva88asVccu3z1pOx6fpbcIwdHG1N0NY-hjv_TdsGprLnm7hr51MijDa3ltvHVgEsazWd9F8l3jvxGnPygf3ITRTGyYTRYVLS5hp3ussh3jOeyFjaBkyGfPdiPw76CS5hT0rj9yAZ6vxs4j9j4nx6t8F0--FHDVcuFqTIuNSG39ROzNbnb6y9iSUQKwoXphYVKmU7uLjjVojVerwfCWDRiuTu836vAK971gEdOCVgfNERzK32ZnaoGTdOHDBXoCZ2zO8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b751ec19e0.mp4?token=YuTiObVSLY5fbi8gOjz_Az8ef05NejEh8noQq2iqfIqJAnm9gRv45Brn3fyE4Fo7yyif7jskn4sUqa_4aWva88asVccu3z1pOx6fpbcIwdHG1N0NY-hjv_TdsGprLnm7hr51MijDa3ltvHVgEsazWd9F8l3jvxGnPygf3ITRTGyYTRYVLS5hp3ussh3jOeyFjaBkyGfPdiPw76CS5hT0rj9yAZ6vxs4j9j4nx6t8F0--FHDVcuFqTIuNSG39ROzNbnb6y9iSUQKwoXphYVKmU7uLjjVojVerwfCWDRiuTu836vAK971gEdOCVgfNERzK32ZnaoGTdOHDBXoCZ2zO8TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
وقتی رامین رضاییان، تصمیم گرفت بدون کم‌وکاست به تک‌تک آرزوهای پدر برای خودش جامه عمل بپوشاند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97870" target="_blank">📅 15:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97869">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e7bb3043.mp4?token=EoKOL2jxEjMOejmSJK91wqEsysZ0zIy7DQDwS_9m5e6uPavtTrGFWgMoBMXMgrBqG3DAUK_PRK6_mf7onXcfVoGHc47XlDeZKecKb4Hek7DfnDxZpTkcN3kkFaFaLDpzwfC4lk7H15kCOMnGPrJ4DfGuVc0COhkNGufriN5QfIqovFzNsSIndtcrCAX7bLGLY5wb9A83gUFbapY0vr2vQC8cALOq7jL3ILZ7ME2XTemd1o_kdk8F80TG7TaKHQ9kVMpI4Bl39r6MtBvlJsCjBFMjjKUimR8PbFkvkq4Gwdgl9qi6Ib4aZ91DE4hgp4Q1qvVy2noOVD5poNXq4RDOYngWpLrMEVUAi1odB06pqSUkXQjkG_8NGUG8lCtuDpXv6em73-LFelMxH-IN70hBOSDJpztLrg8-2hBTMW0JaoBpLdjWZl7UnRWr0662TnRIZZ4WFVh4NCafiY2IkAl5aA5u0Mp_7AdHod6rFzn2NIUb1tlnnZNopaMj5FY16DCxsX3F39UVMpkzYiWPri10ayyfLSGfGKe74H66vwGHeQJtTMfsbNCIZANjErVkgwjpMk8CaKaGCeVYxf2iPLTKF37sgpy9slHRRHKip6h3JcoRoZA8cQGIjGaQ8zik33P2cdurICm5u_D1oog-F2e7QDKD3w8DIKsCYP1GzO-HfQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e7bb3043.mp4?token=EoKOL2jxEjMOejmSJK91wqEsysZ0zIy7DQDwS_9m5e6uPavtTrGFWgMoBMXMgrBqG3DAUK_PRK6_mf7onXcfVoGHc47XlDeZKecKb4Hek7DfnDxZpTkcN3kkFaFaLDpzwfC4lk7H15kCOMnGPrJ4DfGuVc0COhkNGufriN5QfIqovFzNsSIndtcrCAX7bLGLY5wb9A83gUFbapY0vr2vQC8cALOq7jL3ILZ7ME2XTemd1o_kdk8F80TG7TaKHQ9kVMpI4Bl39r6MtBvlJsCjBFMjjKUimR8PbFkvkq4Gwdgl9qi6Ib4aZ91DE4hgp4Q1qvVy2noOVD5poNXq4RDOYngWpLrMEVUAi1odB06pqSUkXQjkG_8NGUG8lCtuDpXv6em73-LFelMxH-IN70hBOSDJpztLrg8-2hBTMW0JaoBpLdjWZl7UnRWr0662TnRIZZ4WFVh4NCafiY2IkAl5aA5u0Mp_7AdHod6rFzn2NIUb1tlnnZNopaMj5FY16DCxsX3F39UVMpkzYiWPri10ayyfLSGfGKe74H66vwGHeQJtTMfsbNCIZANjErVkgwjpMk8CaKaGCeVYxf2iPLTKF37sgpy9slHRRHKip6h3JcoRoZA8cQGIjGaQ8zik33P2cdurICm5u_D1oog-F2e7QDKD3w8DIKsCYP1GzO-HfQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
کنایه‌های تند عادل فردوسی‌پور به قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97869" target="_blank">📅 15:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97867">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqAO9fBa3Y9qJ0A93bOoI-Gcs0ghh8ERpklyjYD51lzrJAn7jLJFfx9KiBwkRrjl9a2A3bo2qrQt9T0T2YhMPDt9DIQOLRQkH7GYvqB82V7g8WgzjwVKhv814pJ7-VXmuhk2izXd-sfL5zA2RndH8wvrPP4SrfuR_6NhTFEDF_dZnWeb9V4t_--V7BwupjgUMHIqbdQJqzfsShh-uoec8_2_IkonvfaDlCFFg_sDopCHGkhQmJ4xGzv4c2oUGfAilz5HlrulAmgwK_I8amx-8gSXudD6MEQiQuh8K7FpM6Dykl4g5PdlLABG-k1wre3j3XZAfG1yJLsoJ7EXMyxbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3eb4669c8.mp4?token=r8yS2_tPopaxmjYiPmuPIVP6SJrCPBpKbNMiT9UuMjdMddTTill8JZhsv94ZL-6kNdZQ3SyrLTBWyHwxV3fr1wP0RqEKsRv-cgcxDp0bbOIN_PckOJUHl-TC5kkB-g0cmZ8E51Bk8bLz2_B9xypvGJ0FgkceZgZel36i2ZC4m1ZSBIZH5ltZdthkj4C73ZQG48q5Fa9Gnkwjl_x_VkPLFECCtKoMovqLvkUXVpotw4AH45z-Tmp1zmjpUhie02vDc3WvqR6bsG_he28u5gzqDPPjzR4-w6WcOobgrXAQiDJiUJ8pxdqGeTcXAJc_ONXQbGQL6g2Q4czLU9pTVQrcAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3eb4669c8.mp4?token=r8yS2_tPopaxmjYiPmuPIVP6SJrCPBpKbNMiT9UuMjdMddTTill8JZhsv94ZL-6kNdZQ3SyrLTBWyHwxV3fr1wP0RqEKsRv-cgcxDp0bbOIN_PckOJUHl-TC5kkB-g0cmZ8E51Bk8bLz2_B9xypvGJ0FgkceZgZel36i2ZC4m1ZSBIZH5ltZdthkj4C73ZQG48q5Fa9Gnkwjl_x_VkPLFECCtKoMovqLvkUXVpotw4AH45z-Tmp1zmjpUhie02vDc3WvqR6bsG_he28u5gzqDPPjzR4-w6WcOobgrXAQiDJiUJ8pxdqGeTcXAJc_ONXQbGQL6g2Q4czLU9pTVQrcAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هالند تو اینستاگرام این کلیپو لایک کرده و برای وینیسیوس کامنت گذاشته:
🇳🇴
هالند: وینی باید این صحنه رو بازسازی کنیم.
🇧🇷
وینیسیوس: خخخخخخخخخ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97867" target="_blank">📅 15:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97866">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx9yQFwiDusWGPMbVbfk9WmXSd7JkT9HXiWIs3aINDL1tatp5q4KhMfXkmCy0vpQZQl3LF4XFgDNStr7m54JoeAc2Fec9ykZc0JowU4TdvqbVOltXoxlegyehnbw6kOdaMcALys6RStrJqHaLLPg1z73RwyrG92gsJZaZxbzseg0Q-IJOoHGPco6swl-wujGrU8uTZgSo76Q5-enOVcBn7SdYtxXYT5Qml7ancDKafZRGZUBjInQ3ZQSKEAb1z15VulR7BVIwAmer3ortVmyXu16jv_WZEJDi6iJFA0-Qp7w2L-YOZIM8-MyOQZ1iP5m56JM--0jTeTVBNjEqijDOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کل افتخارات روبرتو مارتینز:
صعود به لیگ برتر انگلیس با سوانزی سیتی
قهرمانی جام حذفی انگلیس با ویگان اتلتیک
سرمربی اورتون با صفر جام
و کسب مقام سومی جام جهانی با بلژیکی که ولش میکردی اونسال خودش قهرمان میشد.
تاکتیک که نداره، ذهنیت برنده که نداره، تفکری ام نداره و الکی فقط تعویض میکنه.
نه سبک خاصی داره نه فوتبال قشنگی ارائه میده.
کرواسی با چندتا پیرمرد برات مشکل ساز شد
جلوی اسپانیا میخوای چیکار کنی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97866" target="_blank">📅 15:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97865">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خب دیگه بالاخره از بالا دستور رسید امیر قلعه‌نویی و مهدی تاج برکنار بشن
🤡
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/97865" target="_blank">📅 15:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97864">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d611a1c585.mp4?token=BKtOi9_GUfyjtTCdz6ftecwumcWEJ1LNqAFHwTwesaUoAF7eWVcvZNIlcmJXDQbNNOqOPJLe5yOd0lfQJN5Ti91PPrfvhU1ohz_KRX8TOlAOWEmaTwRlLy3ymARF4593Rbdm5kzIf6pgxyNXhY0FRvhBq3yeOnVhU8SK6ImacPO201cjN_EUxeY8aNyepJGel0nJdQzAnNhFTOLbhz6DptBK0RozTOZC_mZN448p_1yGlDbxWN6_z6eY2ZTRN_JAnqnoMp0IfoVkVASf535P97xVqef6oAjRmARRxXbjgn6KYJbcuppiz1Pqx2a5Rm_L5ZQF2O_DprIFxFuWS9mIlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d611a1c585.mp4?token=BKtOi9_GUfyjtTCdz6ftecwumcWEJ1LNqAFHwTwesaUoAF7eWVcvZNIlcmJXDQbNNOqOPJLe5yOd0lfQJN5Ti91PPrfvhU1ohz_KRX8TOlAOWEmaTwRlLy3ymARF4593Rbdm5kzIf6pgxyNXhY0FRvhBq3yeOnVhU8SK6ImacPO201cjN_EUxeY8aNyepJGel0nJdQzAnNhFTOLbhz6DptBK0RozTOZC_mZN448p_1yGlDbxWN6_z6eY2ZTRN_JAnqnoMp0IfoVkVASf535P97xVqef6oAjRmARRxXbjgn6KYJbcuppiz1Pqx2a5Rm_L5ZQF2O_DprIFxFuWS9mIlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇭🇹
🇧🇷
Ronaldinho vs Haiti.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97864" target="_blank">📅 14:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97863">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d42e2e0f70.mp4?token=Sc9idXlcdDhch7nx5pL7SSsCyX49H_BP0-jgtLf29V0CJsxeNxtjDIqCODtnLrTkWzQ_xxf8A_KGwPJLczd7SIfKDKBMWKTazfwOov9-t17HWazh0Y42fnp77Ib_aE1gtGZzrhio0A6yjTIV2ws8mlvYBKnbdoJQJHnZd1N6qET2rwmjbl-_Bz5vSKvuoXNTwjA795XLwupMVG-C0Z2f-EQiFwhWvLzksyosMRF86Rw9kMwMi22kaOvtDRcqQN6SnmR60IYJkVSLJZdhA_tS0GrH05eVRr2ZzWGC5cCpFC8lA3JXnEjRPBhSe4jT3nz586LCslg5_ZdAWBYSVX-YfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d42e2e0f70.mp4?token=Sc9idXlcdDhch7nx5pL7SSsCyX49H_BP0-jgtLf29V0CJsxeNxtjDIqCODtnLrTkWzQ_xxf8A_KGwPJLczd7SIfKDKBMWKTazfwOov9-t17HWazh0Y42fnp77Ib_aE1gtGZzrhio0A6yjTIV2ws8mlvYBKnbdoJQJHnZd1N6qET2rwmjbl-_Bz5vSKvuoXNTwjA795XLwupMVG-C0Z2f-EQiFwhWvLzksyosMRF86Rw9kMwMi22kaOvtDRcqQN6SnmR60IYJkVSLJZdhA_tS0GrH05eVRr2ZzWGC5cCpFC8lA3JXnEjRPBhSe4jT3nz586LCslg5_ZdAWBYSVX-YfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدل ارلینگ‌هالند رو داشته باشید. خیلی باحاله ناموسا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97863" target="_blank">📅 14:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97862">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f9d77bef.mp4?token=DKCUgI2vJa8utv08zdTzbmchKgnHGiQwJug9V4ZYlGfC5oEw51pHZiEZW_1QUeARs40KhUP0oBMevSI7tcwMutErGyiWO4h3P1ObxSCCjVfZ1Cy9nHUd1_Qz5lGP-_0DW7pQ_4VV99m0p6N4l9uNog3IV-IbAXngNR_oZcB58-l7AqnyuX4sv4G9mfdTDXDUl_Xg8qQxEAsuL0z0Yy70PhJnH4vsQ08viL9bT-aZx6BtE4SvN2ef7esYfzay1IlEqdXHB0bIE-psUwlFC2T7rxEq3zPJ9zIuo0de_bZj2O7lgFEs03iNs_IAJj5PvzLMVkeJ8bqXvGL0kAJqJWQhKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f9d77bef.mp4?token=DKCUgI2vJa8utv08zdTzbmchKgnHGiQwJug9V4ZYlGfC5oEw51pHZiEZW_1QUeARs40KhUP0oBMevSI7tcwMutErGyiWO4h3P1ObxSCCjVfZ1Cy9nHUd1_Qz5lGP-_0DW7pQ_4VV99m0p6N4l9uNog3IV-IbAXngNR_oZcB58-l7AqnyuX4sv4G9mfdTDXDUl_Xg8qQxEAsuL0z0Yy70PhJnH4vsQ08viL9bT-aZx6BtE4SvN2ef7esYfzay1IlEqdXHB0bIE-psUwlFC2T7rxEq3zPJ9zIuo0de_bZj2O7lgFEs03iNs_IAJj5PvzLMVkeJ8bqXvGL0kAJqJWQhKoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
به همین‌راحتی مدح و ستایش فیک برای امیر قلعه‌نویی و تیم‌منتخب ایران برملا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97862" target="_blank">📅 14:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97861">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ad396b4fa.mp4?token=jQz3UJi9zu-1_X7ofwIpqes3xWRTEB2AydQFab6HqetFXgl5G3O-PgDxh2_YMQI7Iq7jas2JjPzbovmnsAjrgI-m_2CJ5KXZD7nE6L_8fA29eohtv-wtFim6LyJ38TrgjPoAu09sZWTniX6REwf3chfXw-xMCLdvjgm1KfzZ1Xxx_xf9ZK1KALSRb78_Bw-y8EJKtMd1z1qnlC_cRsojTnDQZVjOIP35bpKJgKqK5-4c2Xxns5l_phYgph7lMn--l6ibqWTOoXNdn0rlXGIj0H3jqVoIKLK8f31nJKsSX2tfv2VaGR5MDihZAyNU0agwM0AclTq8RlQRgEbVISJJSDnlZ6EAL0vjbXlSIysxtkU0ksVDFN8vARA9G_doSfDaOvGDzGYQ_s7GUEIf6pigVpZ4y1k8qrbNdLg7xSaMFayAbWoRlWqLDdVuTWWewIGYgTTw6Y-R8VV-HOyFc22Z18h6NjdR7YEvObleCopFNpqiq39RzT2Zp7QVEjEF9DZNRoxGOl_1dXG09oxF9DjDaQDzhpC80AP6Az8mgiYBSjbxvdDxH2-Su8ZbVv1uqPd_0DvT97mPSk9QMAgJUSBUCYPZtbvcodifxxvzA-TGF15q4ixLJ5DlaMo_AefXlevIOR4mf1i_XcsuJD6AVF9ivNy2-P87VK-8YEPGA4biH7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ad396b4fa.mp4?token=jQz3UJi9zu-1_X7ofwIpqes3xWRTEB2AydQFab6HqetFXgl5G3O-PgDxh2_YMQI7Iq7jas2JjPzbovmnsAjrgI-m_2CJ5KXZD7nE6L_8fA29eohtv-wtFim6LyJ38TrgjPoAu09sZWTniX6REwf3chfXw-xMCLdvjgm1KfzZ1Xxx_xf9ZK1KALSRb78_Bw-y8EJKtMd1z1qnlC_cRsojTnDQZVjOIP35bpKJgKqK5-4c2Xxns5l_phYgph7lMn--l6ibqWTOoXNdn0rlXGIj0H3jqVoIKLK8f31nJKsSX2tfv2VaGR5MDihZAyNU0agwM0AclTq8RlQRgEbVISJJSDnlZ6EAL0vjbXlSIysxtkU0ksVDFN8vARA9G_doSfDaOvGDzGYQ_s7GUEIf6pigVpZ4y1k8qrbNdLg7xSaMFayAbWoRlWqLDdVuTWWewIGYgTTw6Y-R8VV-HOyFc22Z18h6NjdR7YEvObleCopFNpqiq39RzT2Zp7QVEjEF9DZNRoxGOl_1dXG09oxF9DjDaQDzhpC80AP6Az8mgiYBSjbxvdDxH2-Su8ZbVv1uqPd_0DvT97mPSk9QMAgJUSBUCYPZtbvcodifxxvzA-TGF15q4ixLJ5DlaMo_AefXlevIOR4mf1i_XcsuJD6AVF9ivNy2-P87VK-8YEPGA4biH7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😛
برخی از کنایه‌های افراد مختلف به میثاقی یا همان مجری معروف‌صندلی دزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97861" target="_blank">📅 13:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97860">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twcnBv7cKqrscpmMdJZqUje8HNEMyBiKQzw3zLttDQl9LBcYIG_8EOvV3mmLXPz4I-4L0llMy-0CMM8a2L1A4LtWULFrVKeucsOEXVGyOiuwqfqA9AqmKEfx-MCpicoWZ-DCU7iT2QsQKatRShfUoHLXiI2IzKwigWntBZcuSQ5RBrVQaR-C60QQUF_14eLGMiW4ZVXDcWPmSt7IbiG5PWzSMto0m1-ts9oJv2n60UdDpb5BrnCVEY8-9fDh9qERpZtHvsSAZqaOxVtgvcDnoX9Wh4jDZ-iv7x293l0f7XPt_mmAU_28K-TgDI3KPCqi4lT5kFECDcIgrpRXROqDng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
فدراسیون فوتبال آلمان رسما اعلام کرد یورگن کلوپ تمایل خود را برای هدایت تیم ملی آلمان ابراز کرده است و مذاکرات به زودی آغاز خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97860" target="_blank">📅 13:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97859">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQsjmisoM3oixiqJsADn7VKBswdlka7ctYuyIozTDB1pKdYoINxg4b7v2iWLTrxsXAYPd7jHbp5ynZKAP0o2_VF6MwxyzVrFQxeOHgPwf5rEClCBffUbmq7Nn5C3H5iFC3zLckOb0F0BjnWLBshULt6IvxpyDkC7rv7pd87zA2wykzk8Cvvv0pcq6rqqzKFmxJzJPUE_n7d996y2aFVy2cGUFcPi-_HrsTgsstpXaCn2eCCnG0tC7LxPcTlbyFlk0GEQoFjY8KsexhJOIfuP4HHPUUQ1TrZluVnwgOGstjmNv8nQer6h8a9XaaYIKVXFvgQXZW2uXBl7Tk888lJCTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رومانو:
ترشتگن قرضی به آژاکس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97859" target="_blank">📅 13:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97858">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df46960b2.mp4?token=ObQoQYLWUlrEy2uvSknc9D9iyqQjOLQvenPljlwYrVQfslyODCm8ctB2ZhWW0B0O-BXSd-ML92V17PGlL_-nxbB5jUm3l48he5uH31yWATeRyrEO8rvVO2cIinKNZChXQ35BVe-QLAlv_zf2wpQ6mNbZmLOuXWl7CSLUp3E_GuM8TJJCUCg5ZtW60Ueu8pOnmheaACAriaWgnDxjzED1e17KSXHbCN_8NkKTkZ0kKl-rb5wzlBQtwRqLGie7j_0lZv4j8JbYGTKKxsSto25GL7jK4kIBbobJukY2067sxo4-RsY2H3J0iYy3sDkvIYHUW8RuSpTrQ0YBIB575B7qtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df46960b2.mp4?token=ObQoQYLWUlrEy2uvSknc9D9iyqQjOLQvenPljlwYrVQfslyODCm8ctB2ZhWW0B0O-BXSd-ML92V17PGlL_-nxbB5jUm3l48he5uH31yWATeRyrEO8rvVO2cIinKNZChXQ35BVe-QLAlv_zf2wpQ6mNbZmLOuXWl7CSLUp3E_GuM8TJJCUCg5ZtW60Ueu8pOnmheaACAriaWgnDxjzED1e17KSXHbCN_8NkKTkZ0kKl-rb5wzlBQtwRqLGie7j_0lZv4j8JbYGTKKxsSto25GL7jK4kIBbobJukY2067sxo4-RsY2H3J0iYy3sDkvIYHUW8RuSpTrQ0YBIB575B7qtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره مشخص شد که چرا سالار عقیلی در رختکن نساجی ترانه «ای ایران» خواند
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97858" target="_blank">📅 13:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97857">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afX0mGWbijTEGPl8QUFLXlSVaW2DXaXUxpxfwPY9ujdxIPB-LjbE4dLnDLgWSAnjQl_A-F9nt745v3FfM7FlfEMn21FPhDbhECx0my3-Og8lTPa5RRX0lrdwEPi32YKWdpDtTLI7SHivn8BoTUh_VHsZClo_JWTIiuNUqh3t_Wh7qAI4c-tBwws7I7QzsA3M_RRwxou08lyNaQu7aBk35KkdhfrbGVBnQYXX56XDDtd8esfwRZyvp8jFK4IVgygbTDGZBdVTPQ3YxruFiueSXUDqTRwbAwgwvHu7YPHQTB9fIIbuSYFbHvGVGQ42GKonR9KyrjPFgVC_yJ_ut0SAkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
جرمی مونگا با ۱۰ میلیون پوند از لسترسیتی به منچسترسیتی پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97857" target="_blank">📅 13:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97856">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f201981e1.mp4?token=nKquPjkqHMt1_wi3BQitxdn5zS-UINl0oyToGIM1wmZDE_gWRZftVCytxjT1yvmrRcpc84U8osqeI3dEOWQqqRGg2_G24Qcfjpwf4LQfY-3LF7jisam_DyxWUvdLSsEujpzvGMACP8PooD8HU4Fpm9XqmvGubFMYtOq5p0Ij7nqwtCBz-_gL-_AeP1iyXNzhoZsw5t3Vxo9r9W54J_49AoEeB6HVlmLtDG6gdGMTNIDWS7UoXqwBeWi1AGrhqFo4LAPjerziw-TtutjaZ8aRLhGC4T9dcY2GmKi4SiyC2b5apDA0pJ85VqWpV-iE97hkXgLVVNxuOO0hpbJFrAC93g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f201981e1.mp4?token=nKquPjkqHMt1_wi3BQitxdn5zS-UINl0oyToGIM1wmZDE_gWRZftVCytxjT1yvmrRcpc84U8osqeI3dEOWQqqRGg2_G24Qcfjpwf4LQfY-3LF7jisam_DyxWUvdLSsEujpzvGMACP8PooD8HU4Fpm9XqmvGubFMYtOq5p0Ij7nqwtCBz-_gL-_AeP1iyXNzhoZsw5t3Vxo9r9W54J_49AoEeB6HVlmLtDG6gdGMTNIDWS7UoXqwBeWi1AGrhqFo4LAPjerziw-TtutjaZ8aRLhGC4T9dcY2GmKi4SiyC2b5apDA0pJ85VqWpV-iE97hkXgLVVNxuOO0hpbJFrAC93g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
تلفظ نام مسی اگر در کشور دیگر متولد میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97856" target="_blank">📅 13:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97855">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51882d6736.mp4?token=bjgY8MHZhoh-saptBbYQTddGzLIjjxOVBV6GOIM5BMCggMELW0M1VKmiSBTL4z6FGese0iqv2_rFwpOcOGg6m-nLPgfx9iJA_GLyEFM0IR_ViKq_rc86K5fR5k94brKGqOuQUAmlp0UuQGCkbg0cEgk80IGngyt7v4XlnXJbiXQuvb6XWSwduoztdMftFoPdgsZ8GUCsexIu8aLJLFYRVwWeth0TkXOwBxE4jM9SOvMa10cEPdS-DjpMHfpXT2YaXnnJJAZ1-clH2q0h9w4QC5cjU2ZEeUUCi-RshlXN0h13DvwI6ECPpZ0-0bqXi8lWH7M3iGBLGjh9B3qkFw8_ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51882d6736.mp4?token=bjgY8MHZhoh-saptBbYQTddGzLIjjxOVBV6GOIM5BMCggMELW0M1VKmiSBTL4z6FGese0iqv2_rFwpOcOGg6m-nLPgfx9iJA_GLyEFM0IR_ViKq_rc86K5fR5k94brKGqOuQUAmlp0UuQGCkbg0cEgk80IGngyt7v4XlnXJbiXQuvb6XWSwduoztdMftFoPdgsZ8GUCsexIu8aLJLFYRVwWeth0TkXOwBxE4jM9SOvMa10cEPdS-DjpMHfpXT2YaXnnJJAZ1-clH2q0h9w4QC5cjU2ZEeUUCi-RshlXN0h13DvwI6ECPpZ0-0bqXi8lWH7M3iGBLGjh9B3qkFw8_ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صعود پرتغال به ⅛ نهایی جام‌جهانی 2026.
🔥
🇵🇹
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97855" target="_blank">📅 12:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97854">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ImoaQIR8-XiVjGl9T2dxXVFG1qMtU7i-5teohj8VjNmHoiGaAc6fepp5S6Og06tSlrkDcVLssU3GOgip43b0-ovcNnoCA2tHnfS8PBY7cxzhe3r6ez0aqHI9IxTGsHwJV8Iy3ndzF-0IPzAEwlyyRW2ajGoRZ9KyjFy4LVwrZ9tmV20bhGFtmo0278RalgVagLbhAnxocrqdghG3Rim1u0rq0mzE0JuVZgHnE5v4ZCazOhuWy-jpCas9zTSKb0ydWdtnpP2XedE-VSAVodWcCGpuWIbjsq9ZeD1IJABS2bel5fJORpUn-SmgSSDDwJ4qJEFROyM2-ytNaJ1l5ysXFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باشگاه لیورپول اعلام کرد که یک بنای یادبود دائمی در کنار استادیوم آنفیلد برای بزرگداشت دیوگو ژوتا احداث خواهد کرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97854" target="_blank">📅 12:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97853">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCxJ8X8wiFIaI4rdFVA4GMeQ9iMebtwbjuhJ52sgTI_fSM11i2ufHVirDSnzgXp9YxNEr2bQyG21MV9GfsjVn0y9gYmX9JagGzJtZFV3crNrelX6l-w-MmGBOo33E8YaMl5hPK-3Ou3-INjt4HWc6xvla_JIOH7JeR7lPKMKvTyx0J3W1DeP0mNl5g3Ksd9hdf5Km20MHBaHdFFukdxbMr27Y_cNZmzX2FrdjKPt-4Q3FbVrGgB1DY3yuakG-_rz9xkITGlBaTrkuWacTr5lnLLYVPSPCZY7uoLAqfDovk2DDs_6iTtZEl-4Ghfa3ORvA9l6A3_BRxGHMdraZRSfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
👀
صرفاجهت‌اطلاع:
🇫🇷
فرانسه در سال 1998، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇫🇷
فرانسه در سال 2018، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇦🇷
آرژانتین در سال 2022، کرواسی را از مسابقات حذف کرد و قهرمان شد.
🇵🇹
پرتغال در سال 2026، کرواسی را از مسابقات حذف کرد.
🤔
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97853" target="_blank">📅 12:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97852">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO9Xu77HybpoAO4xZ2nnawbDY9P2nSKGzAFq6ERnwvjI14SmWIuPiaRPM5eHBm9qB0cr6ShEUUqTzEdbge3yEd61GzBt854S_vnJTlq5mtXYEvhGZjbbMtu-t1yVIiiKGDvomDW6sn_CxW0f7mB3Ak06YH7GxfopzwD1CgA0eCgUX4GaT32Kh2dpQNW7fpJQgYVP_e3PoAhkNeuHArvBzVOQDjI3LfKoebIrXj-QOO0eVQjdCDIAEBSXDcKGUvvyGF3LF5AMDgik6AzUJggo3o0XLiC1Hbw8Bt89qwAjPyJdQ1FAhXArQDEoiiOwyNnQJifezfmdtuN0_Jq4Z1gMrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
جادوگر غنایی بعد اینکه‌پیش‌بینی کرده بود کنگو و ساحل‌عاج حذف میشن، حالا گفته که امشب نسخه آرژانتین هم پیچیده و مسی باید با گریه از جام‌جهانی خداحافظی کنه!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/97852" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97851">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5nEYVqTRyOIlFwmkksm6qtcS11tIWPa72HIEed2yk2mK8PCiQv_RM0Ia3gFG_w5dSNJRAyoVK_H5OvitQGynM_tYqLAyXmcL0kpuK-PNA8bcNqKZs4UG0ZGCNEzU3_RfrRL6Ch9qvbGE3cChRepD2etX6GoKvtKWcs3csh29Yq6_6Dpm60iMGeGKXEVHgftYeOyeWz71EiCeOmpBSeTQJuXOYaH6nM699KbGi3EMJZR9Tpa-3iBpNYrooqVkBAQ7G8ggRDGkvv3LNB4P1IKGpS8F6EnzttFkFf3NCBkKOVXo3UrAUFVEjJIYizeaZAZPZcFkXOcO_oRcLU-WAhtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی طلات رو روی ۱۶,۹۰۰ فروختی و توی یک روز،
قیمت طلا
۵۰۰ تومن بالاتر رفته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97851" target="_blank">📅 11:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97850">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UyI72qIGbMZ9fvQ5V199o2Fd8BuWG05SBiA5ytQxjkGOByiLKr2lDvDhsecRfzzP_wS7mysTA62Qy8kwpNMM3F_X9YkRYdpZchExt1yzWVDKfxdIWmxWWxo20ltQpZZXfVk3eEi_6Adb5WupBneUyXQGbedCQtKsynzZ9P9dMgjnTJrjCPqCbbFgSy2LyXxTkZBs7I2sSDUM1ochCGXDiM1xuiYhCW3CH9FekeTcAn7nXwSeXAk52LQwX32zcGTdKODzfuSHMwBa4v3vjLDyisHwDnA6uMCELxEJhFh_aA6LmYfKmOM-iNDKF_URo1LmFxHBKbyt1f7VXgz1UDHYBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بازیکنانی که بیشترین بار جایزه بهترین بازیکن مسابقه را در جام جهانی کسب کرده‌اند:
🤩
لیونل مسی — 13 مسابقه.
🇵🇹
کریستیانو رونالدو — 9 مسابقه.
🇫🇷
کیلیان امباپه — 7 مسابقه.
🇳🇱
آرین روبن — 6 مسابقه.
🇭🇷
لوکا مودریچ — 5 مسابقه.
🇺🇾
لوئیس سوارز — 5 مسابقه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97850" target="_blank">📅 11:52 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97849">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFx-9rrRbO-GJWzSoL4nL0_VGuqgVPK2OSpSzHjwzsMXR3wfVOeJwmPCVAF062VAurVlnoVDbtYFGdt3yEeQ6XtiTvXwWz4p5qQYPX0dPemU5Hv_qal9xDil4JaQhevFHUHQt0hS29Q4B5ktLMSLwQ8JuotHa8L_F9iymnELThxrK11D4wyGpwilSrYWjZC9vaTh-6sLjv__K786G8emtGFJYUbR7gQLbv7s1tI5yqJ5JsjIMXeqB1P_Yx_ZhxVphL0G7WYQA_yflSA9BDBK4fpcNBTZpWT5eYWDvF7hyETzAcVVW5EcxZOn2kr0-nGhMBPkKQ72ruQ-0FKFq_sZmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇵🇹
برای اولین بار از سال 1966، پرتغال موفق شد بازی که عقب افتاده است را در مرحله حذفی جام جهانی (در برابر کرواسی) به پیروزی برسد.
لحظه تاریخی قبلی، یک اتفاق افسانه‌ای بود: پیروزی با نتیجه 5-3 مقابل کره شمالی در مرحله یک‌چهارم نهایی سال 1966، زمانی که اوزیبیو با برتری، نتیجه 0-3 را تغییر داد.
و پس از 60 سال، "بازگشت معجزه‌آسا" دوباره تکرار شد.
🔥
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97849" target="_blank">📅 11:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97847">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAUsOeTgNu5PjPtM9nctzoOO5BGOrr1WrfVK9j4LuPStNiOfvk4dwxvo5mKU8IaeGHy3V8FYpzUZqZG7AejfqJ5CEj5JKAo-iWcIrz5pCsvgzR2c0amcK5E8TgYDmc63V5uVpQRRMF48vDJZeW_SP-92h3rfzpYmyXlbbyK4NG7YClbugr6Exte0ruUmpczq2rfw-I1je4CeVKOM7DNf_eGrQJrRUiDvhdtddegKm_xuACz4-I9lrIffIbkHmOqN8U1Y7OGWRNfUr8WI6VFBCPZYHH9wXzrsgXbXyc1rgsZ1T9sf3lRZOkGGRAX8CfQ9paF2Juwf_JZxzRiE5_kLGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو : آلگری به ناپولی HERE WE GO
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97847" target="_blank">📅 11:38 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97846">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVV0Y0uqI2mN58Prf8uKkbShCsWMfCrKfALlEpTCSKrd4g9NuAcFx4_6ZJLwoCaW_xbMQ-RSq5NtNFjIVhGprbjUQ_rmK0Xzyb3R-Y_3JCHA6g89rD7nOQIqjYw6wFr1doTKHsZJm26ozDx_qmkQJYGhEoYRfyhFC1-6_CzTQXn4KvtPfZ-ta05UYSXZ-YlZzWqN4PqIPW1OjYo_LC_nfRgekecwwlWa_xI13qAnSsd7gUuOUeiDxqfyQDRk_UCsS4EXbXJ5gyyKsiIihVh8rXiz2fAqJ02jlYt0DUYEZWGNMav0OXNLQt7CiZmgNnbM5n5fESzIdZEgCfgLehyJ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
رئال مادرید علاقه خود به انزو فرناندز را تکذیب کرد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/97846" target="_blank">📅 11:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97845">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f386995eff.mp4?token=vL2gYrL0BfKLuJY0TC7fVswHUjZZRcDhq7uugBS771X9GDISHox9QIDKaFFrrzo4wvW7DsGqAZR5Rtmr8lF4JAMgDcfeMhDUYbNEd7_0Ir0I39qI3yaRSsgeUCs3rAzS7SjR0wlAkXw4DJB7GaAQ8R9d4Pm8HLFTEoYwqo6kBYdz9JznX3rJKej-O38LFcBA6ubqzb8cG3rkp3tuMHMifQNRpTBD8-CxCeS8JU_1tkJH2V-zSA0HQqhOgI13pLHpW6tmotoy3NOEeglEGhkBkyiCRr0QIuYCyOLAiL6aJZDifpztZ1tV1HfCRW2LWplKQ8fA9463Pp18WS9Qs4CWrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f386995eff.mp4?token=vL2gYrL0BfKLuJY0TC7fVswHUjZZRcDhq7uugBS771X9GDISHox9QIDKaFFrrzo4wvW7DsGqAZR5Rtmr8lF4JAMgDcfeMhDUYbNEd7_0Ir0I39qI3yaRSsgeUCs3rAzS7SjR0wlAkXw4DJB7GaAQ8R9d4Pm8HLFTEoYwqo6kBYdz9JznX3rJKej-O38LFcBA6ubqzb8cG3rkp3tuMHMifQNRpTBD8-CxCeS8JU_1tkJH2V-zSA0HQqhOgI13pLHpW6tmotoy3NOEeglEGhkBkyiCRr0QIuYCyOLAiL6aJZDifpztZ1tV1HfCRW2LWplKQ8fA9463Pp18WS9Qs4CWrYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😮‍💨
🏆
🇦🇹
ایستادگی برابر قسمت و سرنوشت
دوران فوتبال عجیب ساشا کالایجیچ، مهاجم اتریش مهاجمی که تا ۲۸ سالگی، ۳ مصدومیت ACL را از سر گذرانده
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97845" target="_blank">📅 11:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97844">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05870783f5.mp4?token=h10vjsk4twjCPTPES-FcgxppvRiLinXXPPI9V8UDYSdr-a2dY1qR9D3YG0fPMTq7q7DHcWbcX9ogXEUR9Mlgk9QnLFinAreKVK1lp6QeAQdLaZ93EKzPk7vJLrDxCZS_ZpVqjMzlxMN73xvozt-SQnMnEa6CFf3PvULHWzwPYTgu_2wsYFEsGEpWdt45D-RjTfDzQwPIMuJbKHodlfc4mUCxkja4S-dajdMG4NrQ0VPgLUUUkZMPt5eKQQJMfBBMuKMTtPANxk0wDiJz1pCGD82xDBSsQmCXFLzhKkgB7TrZsZ2D6EymM3CI6jmELfNLpUL-dGuYFyBLkQDtCG7OwKOVrp3o6y_pB4O6jK5FqX5g6ofxnr9a35sxEXnLi_NAESb8Jv49GKvC_zeCz_2luAJVPHf7Ywtj8A3dwqmz_r-MjUvRqn8nGwpr-Dfc2gIYW3gLhFi0Gu6LxMjrBWhVP-f3iA0On-f5tMKn8fzR5dE8jIAsyntSOLqw-BHVIXua5eTXjw_yRlTyUzz-aObBFvlssTFzare9cqbl6htGEV4Ece262nsbnT50fmudTTSJ1tF_n4SBb7NWhpI6IM4Z07qYCkpe_25AQQPNCb5SM7G-KepeAy8nm6zW6bvd3UOcBDrZdEXBvy9_H_DLJswPH8iAHGvFRkF9dRmVwKRZsAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05870783f5.mp4?token=h10vjsk4twjCPTPES-FcgxppvRiLinXXPPI9V8UDYSdr-a2dY1qR9D3YG0fPMTq7q7DHcWbcX9ogXEUR9Mlgk9QnLFinAreKVK1lp6QeAQdLaZ93EKzPk7vJLrDxCZS_ZpVqjMzlxMN73xvozt-SQnMnEa6CFf3PvULHWzwPYTgu_2wsYFEsGEpWdt45D-RjTfDzQwPIMuJbKHodlfc4mUCxkja4S-dajdMG4NrQ0VPgLUUUkZMPt5eKQQJMfBBMuKMTtPANxk0wDiJz1pCGD82xDBSsQmCXFLzhKkgB7TrZsZ2D6EymM3CI6jmELfNLpUL-dGuYFyBLkQDtCG7OwKOVrp3o6y_pB4O6jK5FqX5g6ofxnr9a35sxEXnLi_NAESb8Jv49GKvC_zeCz_2luAJVPHf7Ywtj8A3dwqmz_r-MjUvRqn8nGwpr-Dfc2gIYW3gLhFi0Gu6LxMjrBWhVP-f3iA0On-f5tMKn8fzR5dE8jIAsyntSOLqw-BHVIXua5eTXjw_yRlTyUzz-aObBFvlssTFzare9cqbl6htGEV4Ece262nsbnT50fmudTTSJ1tF_n4SBb7NWhpI6IM4Z07qYCkpe_25AQQPNCb5SM7G-KepeAy8nm6zW6bvd3UOcBDrZdEXBvy9_H_DLJswPH8iAHGvFRkF9dRmVwKRZsAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
ریکشن‌های اسپید در بازی کرواسی و پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97844" target="_blank">📅 11:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97843">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SomISN3GH-UG0uiNob9w8fHuOlw5OhddByx6CtryvPkWBUTYJ3D9JJIDla_Af09pop_nrUEOT7WBdPHIj6OwWVQaGtWLJMVIGl5cgyf_xJ_WLt82ih-gvoSgxis2NJo9DXEFDTbnNWJdyV3KDN6_yjf68h0a24FJ-GPH0OuK3-2UsAatc-At_ORo-4fMz5g90SomrttFsUiMr6txDceaS_iISeJx3AO4Znnw2UUO9a4NKFOVsmeUwu0GhLv1mR6obnT3lHHcxUCTZfBnTIb3ji3NSpKQT-iBExtufz1cZlxjLyKS0p2p5m6DAjwtgxl9j6wyCqqhTZg9GJSRPC030g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مارک کوکوریا اولین بازیکن اسپانیایی تاریخ است که در یک بازی حذفی جام جهانی دو پاس گل داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97843" target="_blank">📅 10:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97842">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307bbcfb1e.mp4?token=MNnx62oo_ZKfPjAHgmQNKi1CrioWIjfauLWEbAglok_BQVIcN7G99zRTH3uuStfvcIANqtBmpAwDqmwbefNjDIz4wMioV35iJPoOhLlCin1KNI9lcN76RbsoKowHYZ-qULcT_yam27vUe6C5Ixdx6xDhNfBhEanKGRf1l5S_NvWoANSFmVr5bEPx5ME1w-r1it37rJ5N2rKRpktosdevSTWLYREYhQsd4R4PIE3onA3dD6JH0Hlt0dbUkaRQMYm6sVFcFV86YoP5NYMR1iKfzHIX4YHWeL1FNOpUvJLecFEtaFcjgs8mIM16md2U8rpSR62_S52KxNixNvoM-yDFMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307bbcfb1e.mp4?token=MNnx62oo_ZKfPjAHgmQNKi1CrioWIjfauLWEbAglok_BQVIcN7G99zRTH3uuStfvcIANqtBmpAwDqmwbefNjDIz4wMioV35iJPoOhLlCin1KNI9lcN76RbsoKowHYZ-qULcT_yam27vUe6C5Ixdx6xDhNfBhEanKGRf1l5S_NvWoANSFmVr5bEPx5ME1w-r1it37rJ5N2rKRpktosdevSTWLYREYhQsd4R4PIE3onA3dD6JH0Hlt0dbUkaRQMYm6sVFcFV86YoP5NYMR1iKfzHIX4YHWeL1FNOpUvJLecFEtaFcjgs8mIM16md2U8rpSR62_S52KxNixNvoM-yDFMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
🇵🇹
شادی رونالدو در هتل اقامت‌شان پس از شکست دادن کرواسی و صعود به مرحله بعدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97842" target="_blank">📅 10:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97841">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0MKU8gu2rRhvQXcPQOk2nsdV6472YrCtX9lCvTKcqf_IzAs17HVqGTOb0r1jD9vLeiOfSdIsp9drqY_R5ernFx5ETQGDgE657y_pU2RorbPcPV9TPGxDe0n4hwvfmaDea-dn55OtzPWJCQb39tiqVRHQx7vrpfNDneDnonUCmutO5ST3f8o6dHfrlSYeBgoC3k9fsqFmdGG1by6gajYlvuWWKv_NGnM4Pdgahav9vwBUt_ForwPKJ0HdtDoFanV1JJ4ykRKvo4clpYCBIPfEY0yhxd4cD4YdMh9VFEu4xzu12Qy_lzjcSp08B4sZS3Arsxzmo9crrAqxh5VgAjReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فووووری؛ رومانو: ناگلزمان از هدایت تیم‌ملی آلمان استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97841" target="_blank">📅 10:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97840">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fc4fcb346.mp4?token=XiFQZ44J4gauuOc0NGG2ZUq4hznVlaOcNmOeQ8rBO9XDXIALYehm_Z72LMC68UQKBnG0-nQcp21rHCGNX_CwjrsgyvsE5OsZGgoOdxWTfPj9mC0hjGPXU_rzn1JPTURINy-8dqywLNvpEaQJAllyLNFRsuZr-lMfLtXmw_NqS-pBpV8-ANI_0pnTs8rHC6bVY3qvdEPq88BBNdrPlFUkZ4ZWgMqz5Wl5_43V4qantX9jt2aD339ueLsEYM_M0U6hAgA69uEf9zGilbwjxifiZtdhQTYUsdR1TAhYRJPY1gsPVrJEeCiteXla-BNwDOhMNj9VuOxgpYhc4KYAWiVSPmfBsfUfHjLge_Z7nC0LusykncJWXs4CUg0ices8cLpiXHf0SAi1ctAMiNxXFUi1lMCPj-xBjNxl5lmUAhfhHhwoluzzkh87L46xjRQ0xe6TcS7irkxQolPWqPd9zdqy2ewK20HG64aY1ADH73QzvZK_zktMYYbg534FGNxkemphZYCHy8i2tdKj1VOQASgsIr1xhXYnp7CKwtbriVOlBJI6w7nQcVEsFlu26ik6ilvMoA1_rlqMI8xlmxR3y-4ZjOBhSmD5nkPqMuXH9IPNO4PEwAtee6te-syGbi3l40-xTOPfRrILFPCNKPuIJcVTL5zss7X1HZ922SJw0ZAMtnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fc4fcb346.mp4?token=XiFQZ44J4gauuOc0NGG2ZUq4hznVlaOcNmOeQ8rBO9XDXIALYehm_Z72LMC68UQKBnG0-nQcp21rHCGNX_CwjrsgyvsE5OsZGgoOdxWTfPj9mC0hjGPXU_rzn1JPTURINy-8dqywLNvpEaQJAllyLNFRsuZr-lMfLtXmw_NqS-pBpV8-ANI_0pnTs8rHC6bVY3qvdEPq88BBNdrPlFUkZ4ZWgMqz5Wl5_43V4qantX9jt2aD339ueLsEYM_M0U6hAgA69uEf9zGilbwjxifiZtdhQTYUsdR1TAhYRJPY1gsPVrJEeCiteXla-BNwDOhMNj9VuOxgpYhc4KYAWiVSPmfBsfUfHjLge_Z7nC0LusykncJWXs4CUg0ices8cLpiXHf0SAi1ctAMiNxXFUi1lMCPj-xBjNxl5lmUAhfhHhwoluzzkh87L46xjRQ0xe6TcS7irkxQolPWqPd9zdqy2ewK20HG64aY1ADH73QzvZK_zktMYYbg534FGNxkemphZYCHy8i2tdKj1VOQASgsIr1xhXYnp7CKwtbriVOlBJI6w7nQcVEsFlu26ik6ilvMoA1_rlqMI8xlmxR3y-4ZjOBhSmD5nkPqMuXH9IPNO4PEwAtee6te-syGbi3l40-xTOPfRrILFPCNKPuIJcVTL5zss7X1HZ922SJw0ZAMtnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇪🇬
مدیر تیم‌ملی مصر تو هتل محل اقامت این تیم پیش از بازی امشب با استرالیا با یک مامور پلیس شدیدا درگیر شد که شانس آورد پلیس کوتاه اومد وگرنه حکم بازداشت صادر میشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97840" target="_blank">📅 10:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97839">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=WedXP10kt2eNYt_dx_qpSVMYXDKy0AbrPspQavfbkv4zlax-iEH2gLm9UERMV9Qxu0Jvfu1Ghw5F5LcRDXgOD1gK2gvP8_-S74D3t3kGesk2D7h-M2-Mu06Bez2Pt8EuBqjj6uKTfa3AF6lOC-nNUxKQuzlQ9qpM6TGt6tAkCchqtl69LedEiRO62tIWGJllk3lSWMaps8D0GXDNcc8ExPI5RcvELdFNvK44NBTUOgQ3OgUUj2f518Rj0p6X6E_FqrA7nMJtIesqc5F5Kd4dkJwUrjrHCnY8lrVAkaMw8dg9SZDNiIqChP3OE9kOVJyEeGPyL1csIBbXfngLhoP7hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=WedXP10kt2eNYt_dx_qpSVMYXDKy0AbrPspQavfbkv4zlax-iEH2gLm9UERMV9Qxu0Jvfu1Ghw5F5LcRDXgOD1gK2gvP8_-S74D3t3kGesk2D7h-M2-Mu06Bez2Pt8EuBqjj6uKTfa3AF6lOC-nNUxKQuzlQ9qpM6TGt6tAkCchqtl69LedEiRO62tIWGJllk3lSWMaps8D0GXDNcc8ExPI5RcvELdFNvK44NBTUOgQ3OgUUj2f518Rj0p6X6E_FqrA7nMJtIesqc5F5Kd4dkJwUrjrHCnY8lrVAkaMw8dg9SZDNiIqChP3OE9kOVJyEeGPyL1csIBbXfngLhoP7hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
بامداد امروز شوت رونالدو به جایی برخورد کرد که شبکه سه مجبور به سانسور شد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97839" target="_blank">📅 10:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97838">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98b01a092.mp4?token=GMfwloVlmvn-uZ0Y5eVvrU8Uu8OGT3HTCqgP_dvSZFu5XGnzNfgI43Ot0EFt4yFsJTKIqwQBqrUvQB16L_kFfjxQIgsNWTOIfC706xnqJb1gnaTwx4AGaKyvw4PlZxWb1UQOlDZC5YjzoAX0xvc-lL_Lfy-Ph86ksNw3O3_Z4OBNTuaFPI489ru3R-eQfkNH158HlyDsG8jVWlI_SUcRzoiERZme_46EWpSmqYYR15uGiWOa5z4bZTtcp7cxYXgl8O6gcVfwoqFBgAX2wjvVi6W7skEbLmDArrlB6yWI43V1XJcPWrpskTOeAZcipj_-8-TgBeQF3gNLok-eLQBc4Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98b01a092.mp4?token=GMfwloVlmvn-uZ0Y5eVvrU8Uu8OGT3HTCqgP_dvSZFu5XGnzNfgI43Ot0EFt4yFsJTKIqwQBqrUvQB16L_kFfjxQIgsNWTOIfC706xnqJb1gnaTwx4AGaKyvw4PlZxWb1UQOlDZC5YjzoAX0xvc-lL_Lfy-Ph86ksNw3O3_Z4OBNTuaFPI489ru3R-eQfkNH158HlyDsG8jVWlI_SUcRzoiERZme_46EWpSmqYYR15uGiWOa5z4bZTtcp7cxYXgl8O6gcVfwoqFBgAX2wjvVi6W7skEbLmDArrlB6yWI43V1XJcPWrpskTOeAZcipj_-8-TgBeQF3gNLok-eLQBc4Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇭🇷
🇵🇹
جیمی‌جامپ بازی دیشب پرتغال و کرواسی که با سرعت نور داشت سمت رونالدو میرفت ولی در نهایت پلیس به سرعت بازداشتش کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/97838" target="_blank">📅 09:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97837">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/949a0e76b7.mp4?token=o2FIGrWLu_Aigit0w0potQJLFsytxC1B-byplnGtf1bMLsCJWkBjPGmbN07HfRztjPouckp5XtsIBg98ncJZBKXTKN9p9daLw4A9XEucLf9LT2OP1KFv4U_p0AF1ZBpII9knxLvHht1nxojGeMwr6oRpHqp9ElpZOoLp-7RZNgK1sErZiZ65AXqYjN7N-gnzVaK6Ejr5skJqLLP_8STOAbPScXJPXGQI1ZG7jC_Pd7QjvlkIomrtIAgRwYkUwd4uAzxbPdsp5MlKNbN94cKEzUq4MIdxpqt8O5Y_1wQD66MfjUcX6Po8sNXDqHUcev06VcK26Not--UQk1Hw5p0f5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/949a0e76b7.mp4?token=o2FIGrWLu_Aigit0w0potQJLFsytxC1B-byplnGtf1bMLsCJWkBjPGmbN07HfRztjPouckp5XtsIBg98ncJZBKXTKN9p9daLw4A9XEucLf9LT2OP1KFv4U_p0AF1ZBpII9knxLvHht1nxojGeMwr6oRpHqp9ElpZOoLp-7RZNgK1sErZiZ65AXqYjN7N-gnzVaK6Ejr5skJqLLP_8STOAbPScXJPXGQI1ZG7jC_Pd7QjvlkIomrtIAgRwYkUwd4uAzxbPdsp5MlKNbN94cKEzUq4MIdxpqt8O5Y_1wQD66MfjUcX6Po8sNXDqHUcev06VcK26Not--UQk1Hw5p0f5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😔
🚨
🇸🇳
سکته‌هوادار سنگال بعد گل‌سوم مقابل بلژیک که در نهایت فوت شد و به دیار باقی رفت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/97837" target="_blank">📅 09:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97836">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇲🇦
تو اردوی مراکش یه شعبده‌باز آوردن جلو یاسین بونو که از لیوان آب مار می‌سازه و گلر مراکش میرینه به خودش
😆
😆
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/97836" target="_blank">📅 09:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97835">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🤣
داستان جام‌جهانی و پارتنر بالای سی‌سال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/97835" target="_blank">📅 09:03 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97834">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJl66wayZJb7bzy7T9XsbIGjwhzb8TrjDZFF5d7zOLLxDDWJBRT9HqHc1EGU6wJ5kQLcBNYmI7Jjbs6Wcs6GEWmvrO1TwGw4e8OgpNrmGWnGxq9O4PSpYwutOOdz3NH4fPTK6wu6ERHuudJiwRG9gFxOeKryi8DR0WGw6oUGTaOU2_rAOFPsDlmmVWKcRnqrhbJ2c0zKXFk4k6n1kc-gPHY6jFeo4Xkh5V-0JnVNq-_PYxO966-pbm6IVENHJe4S8pEcsrUL6xFJs5j5vWLZqK9zN2PM3bhECxsKOZjLtEVONnD9SnieYqhvTCB0FY9wOw-d3crcsgXZVAF-4ih91w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
#فووووری
؛ رومانو: ناگلزمان از هدایت تیم‌ملی آلمان استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/97834" target="_blank">📅 08:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97833">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🏆
مسابقه الجزایر و سوئیس، آخرین مسابقه‌ای است که ساعت 06:30 صبح در جام جهانی برگزار شد.
❌
❌
در دور بعدی مسابقات، فقط دو مسابقه در ساعت 03:30 صبح برگزار خواهند شد: مکزیک در برابر انگلیس و آمریکا در برابر بلژیک.
بقیه مسابقات در زمان‌های مناسب برای خاورمیانه برگزار می‌شوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/97833" target="_blank">📅 08:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97832">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfyuLFQPXfNYLdrMmzhGedrBUzHNNKXH_DXT-NfwbDesbb0knoxFEqi1JPU8p7s121kOA8U4IQy-b6mh8rDxyh796MPKowO21GS9eudL-UH6t3SW4DaqMwioHxbcIfKjUS1Peja6xdlA5Wwy4Q-P1p0GTNVsYHbYolmJCXfCgYlMA8W-YatPeVKiGpeY7A9oZweWAcueOAql0CMGqEq4mcWtHtpwO31Fj8ZAnNUzpb_f8QX1RxdQQN4UHgwMkFdqeLc4Wa66VoVgcgJHctn53k_IxWginXKTWAXcwyF1JA46Pf11NpHhlSz_UIGv-XydnRnUQlpQhsiNucUMFRwEGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇩🇿
با شکست مقابل سوئیس، ریاض محرز ستاره الجزایر از بازی‌های ملی خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/97832" target="_blank">📅 08:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97831">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZoUeH7cYRu4kiF1eY7LjCkSHQjr0WwmIgpuzDlu7iDlNU_r1Sj1WVeBwWiA0E-VgpHxzC2_npZt2P8hTs0CRsB3gqIDciJfCQss9-Vm8JPrXashHNe6gaPdb3dRt4rSISuXLcI8AQKoMmZePZQG81XKmNo7Z7hCLtdGt7HOfDHBnL_zoxQoGZbpC9zN9Y14_x9dXTPUoAjG0fhVRV5CWYIp9MtFDuizNnPuBR15FXjevR5QpCV21CACzMjf-yJ26MGFqNnabh5LVZUPcCQHsO5PLH9LMsfXL_XdBFm7Lveh_IIjKS70BFhfUjrWKB4oaF8rgCqp9gwuoK5bG7suBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
آخرین آپدیت نمودار مراحل حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/97831" target="_blank">📅 08:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97830">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecL1PYSXaA-_6-oHJDP_ryc1KFVTqOXy2P-fhU2Xe0eFt6Jv7DcEvJ6a0ueNt5xpSQ7AewkZ1FbT_GiY3g-U2IwZBAG4tV8jOFty4Sl1nFPpBu2CkoLnfIeZrbr07OeJPQGEjHJGLQYkGveduMDb_j69RmWEMrR1UL1tbJQXDUB4XTv0I5Y2UM2fzo9sPrm4ltIdnMSTCLX7rYm8YFXih-4ukTWGZ0C7n0Q7kYpiLxjuoy3pQ_vsiG9s66FM7zRj3tCjJnUGyM1hLEPQzgpznY9wT1DZuxvTP_8xIYLk6U1xbh4UHX8kz9DFRIOvU8_2wujkA_DIA1L7teYBE_q5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهاجم سوئیس چجوری اینو گل نکرد؟
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97830" target="_blank">📅 08:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97829">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">الجزایر این همه زور زد که گل بخوره به اسپانیا نخوره که اینجوری جلو سوئیس تگری بزنه؟</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97829" target="_blank">📅 07:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97828">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17d083e293.mp4?token=IppCpLIWpVWpJNRTQ9dENuY5eX76GI0pIcGcvRTbop7cQx03An8n4GNAhr0vm0IIAMvUYTdf-cwHU8N1dPP9Wf-yWamWDFBqp4QgYuu_mWk4UUqZe-b8YmU5fvGE7gI-SeskO40gpyt_6iex9JxFn4tY-lBfdse00Q9Eis7Nvwo6KGfeQgCp5UDGd0PwyKquZvpP-G6I8IoeARrfSf_kC9dLt7qpzehXRQ5LcdHpbld8wWt_NlXLD5LR1y9Y_8Yf1-FPiXbyrphHAQk_53tab9tI2xQkBX0NPm7KoJchnY1SXZ0g09J95czA-UI5Mv6geDPNndzsvkUbJp2xOSzAhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17d083e293.mp4?token=IppCpLIWpVWpJNRTQ9dENuY5eX76GI0pIcGcvRTbop7cQx03An8n4GNAhr0vm0IIAMvUYTdf-cwHU8N1dPP9Wf-yWamWDFBqp4QgYuu_mWk4UUqZe-b8YmU5fvGE7gI-SeskO40gpyt_6iex9JxFn4tY-lBfdse00Q9Eis7Nvwo6KGfeQgCp5UDGd0PwyKquZvpP-G6I8IoeARrfSf_kC9dLt7qpzehXRQ5LcdHpbld8wWt_NlXLD5LR1y9Y_8Yf1-FPiXbyrphHAQk_53tab9tI2xQkBX0NPm7KoJchnY1SXZ0g09J95czA-UI5Mv6geDPNndzsvkUbJp2xOSzAhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل دوم سوئیس به الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/97828" target="_blank">📅 07:43 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97827">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شروع نشده سوئیس زد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/97827" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97826">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گللللللل دوم سوئیس</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97826" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97825">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/97825" target="_blank">📅 07:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97824">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkUFz2IeDd0CL3ehOMuOao3f6eS1Cm-jei6xjGBb62nO1ZRrKuL7rIFmKxbBwfD4WnYfJK5aj7b263hd4XEr-0VecRgR0MPrfFcs-aNzLqeCfbR99g0rQ3IBfNdpvlZlTysOc0IEMaaRmDJc-XU9mVC0LTyoTbAfz-oVi2gYy2RuY86G-8LuPnyYTDocdgqF1v0s2xKGzgJLhHOZaPsELT3gTNKJI9XZnQpxrh3PilzWnIJHJ358ECKFb223Tj4Es877Xl5B-g0HiODymk2i44slOK97EqHXOzlRMQs1BFdnI0tlLkvZlOqUJL8jEhJQKThpXwcCDAIwIbnJHowm8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
یوهان مانزامبی هستن پدیده 20 ساله جدید جام جهانی:
⚽️
3 گل
👟
2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/97824" target="_blank">📅 07:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97823">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edce6034a5.mp4?token=C92D9UDwva6QI9_awNk3XxmJNcOJpX3pHstsKBWPVa5IPhIu7crclDnewg7Fogi6pSohi_RvT67g8T3Kb-9FxKRd6_peVqp8rZkmlO05OLFY7pegXVCpbMWSmmcb2bzOng5_PBaDWj1wq3zPlYzVm0NCy7Lly8Ho_nWSGhKraGDGvqTlyU9eJ9Via2Ogs3RIusMiOeB8iQo2cw8CMBCSnLXWwQ8vZSlyO84kmCNnH20x_CWm7UDDa7BV6VjH-pwjeRNS7Ap6lY056jJVlsN0JpwNUbexBoRSkh_njkWDmBh_kjXeqae4xQvvMcST3c4rt1h1k0b7mqYjmujLYRPARw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edce6034a5.mp4?token=C92D9UDwva6QI9_awNk3XxmJNcOJpX3pHstsKBWPVa5IPhIu7crclDnewg7Fogi6pSohi_RvT67g8T3Kb-9FxKRd6_peVqp8rZkmlO05OLFY7pegXVCpbMWSmmcb2bzOng5_PBaDWj1wq3zPlYzVm0NCy7Lly8Ho_nWSGhKraGDGvqTlyU9eJ9Via2Ogs3RIusMiOeB8iQo2cw8CMBCSnLXWwQ8vZSlyO84kmCNnH20x_CWm7UDDa7BV6VjH-pwjeRNS7Ap6lY056jJVlsN0JpwNUbexBoRSkh_njkWDmBh_kjXeqae4xQvvMcST3c4rt1h1k0b7mqYjmujLYRPARw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل امبولو به الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97823" target="_blank">📅 06:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97822">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امبولو</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97822" target="_blank">📅 06:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97820">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گللللللللللللللللللل سوئیس</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97820" target="_blank">📅 06:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97819">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بریم برا بازی الجزایر - سوئیس</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97819" target="_blank">📅 06:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97818">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa9c63f9f.mp4?token=okM_anH_7IGty3SZqyYOEUuecxZus5TUoCUiBtqs57-7LaGZ_bs_D-fJhNaXYu4RTOi_Maulemv96tR2oSXetaY4MGUDCcrsD2IBuj4VcmTHsH0_hzG12qZMZr02LTpo_ZladsiODZyUP0JjuF7Z-SJzhCOr9oVe8gxP3Z7_914atyBs4In7aUUaznUs-1pSU-Nu1QVXgjUroZ_KQ7U-0PcDUahhFJc6DLg6FX3pihfv1VxKnLel2_m2D-MD6kTTMKr4Htjbry1NDLvSCS0ZC9z7Asd1Nig7tYx_YucSvL1SH3Q2qp1FTf3I6LsmNX9FzfdrGn5ov6FMGdxDrnRzhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa9c63f9f.mp4?token=okM_anH_7IGty3SZqyYOEUuecxZus5TUoCUiBtqs57-7LaGZ_bs_D-fJhNaXYu4RTOi_Maulemv96tR2oSXetaY4MGUDCcrsD2IBuj4VcmTHsH0_hzG12qZMZr02LTpo_ZladsiODZyUP0JjuF7Z-SJzhCOr9oVe8gxP3Z7_914atyBs4In7aUUaznUs-1pSU-Nu1QVXgjUroZ_KQ7U-0PcDUahhFJc6DLg6FX3pihfv1VxKnLel2_m2D-MD6kTTMKr4Htjbry1NDLvSCS0ZC9z7Asd1Nig7tYx_YucSvL1SH3Q2qp1FTf3I6LsmNX9FzfdrGn5ov6FMGdxDrnRzhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زیدی ژائو نوس رو کاری ندارم ولی قطعا ترکیب استاد باقری و علی یاسینی یکی از دلایل صعود پرتغال به مرحله بعد بود
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97818" target="_blank">📅 06:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97817">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XCwvcpXRpNjWLKZfTsZTGpMB4RPLWC4lC93oh53aHs7b59WTXqPUFMgwgtE2R9W_km8VuzZ2LqH6O1gCV7_Rl9G6sVMOXoA-aZ0lDCp8EZjd9T0bNjmNF9yEufA7Ku1MxHarFqhzX4TNCvhjtHJoxgUNuNBlONwzDIjwxCW0To0X_ybOioL0WBMKGfM2PCmPw961nGYXljmqtbVCohliMe-jUDuwFr5poenVo11p__FuaZ4I3e2qQqvuvr6lNSWTbLksH4SuuY9ig-zDXVv4WUeL4wswbxJL2DIs8CVPXfUPzylwaHWGHmWFprJd-wNuUHPphEeJ91ZaI4bFcFkcGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"حواست باشه بعد بازی کامنتای اینستات رو ببندی"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97817" target="_blank">📅 06:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97814">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eHmAIuzQkDN2ktfN1nHI3AKfpvNO1y759g0Doq4klnI_KmOY0wSoOMklRXv066nMlcZyfAIrg4J0LlnWGPU91JEM0baqiVB17M0J6e4EZoC2Pmvlw0WgQT68rh5HuSX1V2AeBucq1RdoOq1PYUM-hP8aKm8GviIrlVR-DOF7SmEMevzo6oFc2MphPqoWqYYBNN2G7YWgnehgJTjYLOxDWuiceL0IJ3clHZ8wlWsU5hZfGwKIjq7vvTZwrRxgjUAjIiPe94uqDn6IuHHxYQo0JKQbRclwhv_Vwo2souZb0piZKCWXD5WwPeiqZxupTnbRslx_92ufYprD4v74fz8rUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qhl78kdDB-Eol7ulB-5jrSKmnqsA6V9mH_IUUkPpLpEPHZVcxN2uY4R06vnhWYaP2fRapLfH4ncmraECqesj0nG8Id-mf7z7aG45g4pYnh6BUgT6PjKgIcPGBsREeZNi6GvewYyvYk04k31VLKIsGaBXxLOoie2n7HcVsFUd6FFhz6vCaPKg2KfPvyTZOK4LGfIt-CdEhgyr1EtJbXzj7u17LeZb5tKfJq3noTfZLaY-_1Rv9E1hGKNVbyHoL1iw5SHrF_oGRHfCsD2k1x_XiDFRQouP8Cpup5mspFCrUug_XcygtWoQ3e8rzcpjJ8ha3mdQgfe9N1khBEDN79-_FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rynAcTz8mkRQzasPEgvlCsIqNiC1ElEil9z6dKRtgBm_36sEdxhIFoYsaGeaeFYdgOrvZqoFXO2cgbgtcuk4PfVOSRAgJPxITbUbMMuu-t3V0cy5nfKi-2ixSyQfMiE10wyws4FB9l02cVFxwbS9GFNFXXGluM58psosKFGwPKmTfU-OUukJq2uDC-DAkvc0yJXsSbHBNN54obMSh9EEpq42U0HiPqD1Fae_Zu8FTJKmvD8ZUInon5PkMVItsPXmvG0A4WsfMlKCoMXxPpG88SndQps68F8YfGDioEutew0toNJG1YC0yBI9uOEvIsuiH3_rhuJQQ65VS2gDeetS2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
از دلایل صعود پرتغال در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97814" target="_blank">📅 05:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97813">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9213P7oJ7uPN3wmJ8EQOgCN3jOzDZRHLhCX1ZiieuoSnCY1JZZBiLgniD_VSaDWBGNyvK7rlwaJvuOh0kUWTaY09RcFK7MdekUnuzW8-VvJfz743Fs_ZhRCmit0P0LxDbsT4wuwwKrXooVEOq7ADjbHIyjIrxFsY8rbfy8nJD-Us6Bd-as5MB40Y4JNEuIYLcej1LydTQ1qMpb0TMpzMA7psZAz2e_uGkx7tUp1P2u7z4dP3oPKNTZa3u-OPhcOy2baf89qCJg30ktM5gKQBgGT5_U9layk8s0jooTpMGJybA2lTBfawBNUDXFctpqHA9-bViSJbwiQXMDqbC269Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مارتینز کسمغز امشب هم با هزارتا مکافات و کسکشی تونست ببره ولی در نهایت این سبک بازی محکوم به شکست مقابل تیم‌های قدرتمند تر از جمله اسپانیا و فرانسه و حتی مراکش خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97813" target="_blank">📅 05:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97812">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/We8Qy4dLlXGteNQ3vk-n4slb5pkgayn3vKc1JAhg4Kf0VkeezGEbrITQg0pBKhiXvTMc8u4bKN5s_3i_25rkwGEzvvDM_1bLl3CIsmmegYqUROQebjhiR2YmhkVMJX86mF1Fut0QanaHqnncKSsPP8cPmwcxf7L4DC7arXd98muaM__cYIxhTY46qcDJp68PstI6-4Uj1RDrxoisxypaiWigPa_eveufhtsLM1-4AY7wkR6GJb4xobuPHbrtmhwtzOsL8oocG3pM1bbh_lwjnCCGx3OVgEt9AjlP_D17EYPST__eTe2HX3MgBaVc-qro_3w4tx-EtIScwgiOyeQgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
قیافه لیائو قبل از پاس گلش به راموس:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97812" target="_blank">📅 05:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97811">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNlE64RN3BWqo-E2LtjxZ317ofJdq74ud8eTMFlbaG3s0r8kPrbp2iPkqRwyYc5kLNiLkGi53m-E5-YTi8TSFVoPxXd0_WrNtT72CNl6t18vbVgIAq_yDH_OzmLQyW7fOkL4RQnJlXy2RhYxXSjGMAPz2PoBMJi2tRFHgAPMJoPXLf-HCXe92y5ATgyM3VQc9WzgwgLyIh4TQ9lE7MDco9nzrsElCqXhwUSjslLv14iw_M6wstEYbUdyzLm4hiwJi7EsDLhdAIN3fBtr-GUnJQ4bu89nJTgzS7wJYoJiqRb7CQiKqTNO-NXDWHHW9oKbykm9mFkO4tCjlVTu74mIFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد برونو فرناندز در مقابل کرواسی:
❌
0 گل
❌
0 پاس گل
❌
0 خلق موقعیت
❌
از دست دادن 2 فرصت مسلم گلزنی
❌
0 دریبل موفق
❌
10 بار از دست دادن توپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97811" target="_blank">📅 05:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97810">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szeHVtT3K-2IDJNiSn4I1ewsBNjoonW-0PPUp8KT7aGsowwX8XDT7kk2KV-lenv3gq3nNj_iDpsui-spGmL-IhCeLDWVYGVni_-YoHdsqauxmOSdhRBmV4P2hHuB4alAFpJnwNElZJU6GbubaSWbszoJhW1MS889UTCrxrTZEhDgsi-Hwk_zqoZ91A0VC-hQzEhwGpU_3t2kREByYDnmXbopE5I-vUajLtV07-NJjOyZ8HnJwnhnKELblMZisG8eG5xoC_q_hfmh-e566P0z-XYiMxDGMq-bOY0ZJ0Ob8f_Akre8XcMU7H9iJsUd83OPob7XZA6tDgbqVcZ5Zzi6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| کریستیانو رونالدو مسن‌ترین بازیکنی است که در مراحل حذفی جام جهانی گلزنی کرده است.
🔴
کریستیانو رونالدو: ۴۱ سال و ۱۴۷ روز
🔴
په‌په: ۳۹ سال و ۲۸۳ روز
🔴
روژه میلا: ۳۸ سال و ۳۴ روز
🔴
گونار گرن: ۳۷ سال و ۲۳۶ روز
🔴
ایوان پریشیچ: ۳۷ سال و ۱۵۰ روز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/97810" target="_blank">📅 05:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97809">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">از اون عکسا که دوس دارید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97809" target="_blank">📅 05:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97808">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njw-vevgHk95ycTAYy_YwjZjNVRt51HUWG6S663FxSh1QwqPTngGtb5H_33LeD7BJ64dJKYaw__qOHlSRNjFU4_90Msu6JYs0fAFp87N3P1n3FzITkUoNYVFzgEyT1f-jTdTRb51F0W1nPZ3F1x_P60wCIk0UUZjIn5EGQg-WDULCXpJqdi73aADD8V_yHxmZc9l_FhJSZwWasLNm-s1ezvCL7yNqzHSJI4ZFX35DJy5QdwTmz66VwQ40rV1pP-i8oD_kB7pKi_6IQsmely0nx8q3ALsEG-Y9Fum6J560gbiqiaf_7_HPHjQsZ5-o-s_p8IGhzqE1nXkZx2DJN848Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
خواهر رونالدو: رونالدو بعد جام جهانی از تیم ملی پرتغال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97808" target="_blank">📅 05:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97807">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e979b7d1cc.mp4?token=SkAQAwNAv4zPz2C_ePfDOtedWixR1xmzhhXciU7XSCr1XwS_PwUf9OR_Rw5YHBIOPYHD5EwHJ27ATxtKJdbO1vl4N135uT_jRgiVu8oxETZ41HZlW-kxRH--JY-AHcisIIvtDSf24R22wawk9ITQofgWv__DUZ6EkJagqsxW3Wcs66ITg6oO2FDdDj8L7oNjo6MGQViDA5H4AHM7y4HOCiv1qtumuZylBK9j9KjMsqX243tTULUtiehMhk_P3qh6iJSF6RCPDim_Tj4vsOVGsJXJwwQG4sfveHQGhdKhwGNNgVdsjd6g16e0wAcBopMte27ZxFh7DutvkawHapPNWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e979b7d1cc.mp4?token=SkAQAwNAv4zPz2C_ePfDOtedWixR1xmzhhXciU7XSCr1XwS_PwUf9OR_Rw5YHBIOPYHD5EwHJ27ATxtKJdbO1vl4N135uT_jRgiVu8oxETZ41HZlW-kxRH--JY-AHcisIIvtDSf24R22wawk9ITQofgWv__DUZ6EkJagqsxW3Wcs66ITg6oO2FDdDj8L7oNjo6MGQViDA5H4AHM7y4HOCiv1qtumuZylBK9j9KjMsqX243tTULUtiehMhk_P3qh6iJSF6RCPDim_Tj4vsOVGsJXJwwQG4sfveHQGhdKhwGNNgVdsjd6g16e0wAcBopMte27ZxFh7DutvkawHapPNWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همینجا که دریک رو صعود کرواسی بت زد دیگه آخر داستان مشخص بود:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97807" target="_blank">📅 05:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97806">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏
🚨
🎙️
اسطوره کریستیانو
🇵🇹
:
🇧🇷
‏همیشه احساس خاصی دارم وقتی درباره برزیل صحبت می‌کنم. ‏من خانواده‌ای در برزیل دارم و مردم برزیل را خیلی دوست دارم. ‏چون آن‌ها همیشه در طول سال‌های حرفه‌ام از من حمایت کرده‌اند. ‏می‌خواهم به همه آن‌ها بوسه بفرستم
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97806" target="_blank">📅 05:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97805">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
📊
🚨
🇵🇹
#فکت؛ گونزالو راموس به طور متوسط هر 47 دقیقه یک گل به ثمر می‌رساند. او 4 گل در 187 دقیقه بازی در جام جهانی به ثمر رسانده است و این بهترین آمار گلزنی تاریخ پرتغال در این مسابقات است.
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/97805" target="_blank">📅 05:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97804">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuFUVXYkM9Jw7hKpvf7o74Hr6SjJQdyhGn3_jJeMejzADl4FtBWb5yCwyzkUBy35p4ovYz_ZW9L6qTn5zrDFTQE3vDnmB30GTSSxdDNmiAxNfvfVsRuX3O3fJpHu7LdsVY_Ak-V-FvxZ82i1Nbiwzt8WbNinmDR-9eff9s_7uRYZarXs6-Wf__pRMylutac0wdwxkZHsPr3-LCG5Cw9i_b-v-gmyufbpjESq_3Z5RuaszCDMd9PenmMmGCYyHWGjkrFq_G6nCT9IeASxOAtbe2h8n1LvAbXsI8quhoo_39zjxNEg5FsScdGKQIc9i7e_csDqJLGQy2yFUCLKKlEgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇿
🇨🇭
ترکیب رسمی الجزایر و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97804" target="_blank">📅 05:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97803">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOT59RX5zmmWpMOIHnyGUPVT9E8Bd4u8o9wZ7uHBxBPBtmuoikN9WFvbE2Nl4V1-CDhQTRIVT6dmEjQ5BmfvGdEXQ0sOdjdKiNng9M804C4KOywRK3M0Js6zvW8chVY-pWqQFs-ZXrHdoyigztL5xXgnTeZtBbaW7BF5Bnd3ZJ4o88yggeiyyPvJTz6F94eRP1EUTTcRtDaHLb2sh_HeVTb5giMS0hvQXhGKWXMsSATT1-yXTfwn_oBdgsJ8cOvwxS1DVMtuZJHOOfTSAvglWKHTkJWahS_aOfAH6jWvyFBtnVoh7RxJAE9LEEBDS_yRMjS3wK6dObYPWSl0VqI27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🎙️
اسطوره کریستیانو
🇵🇹
:
🇧🇷
‏همیشه احساس خاصی دارم وقتی درباره برزیل صحبت می‌کنم. ‏من خانواده‌ای در برزیل دارم و مردم برزیل را خیلی دوست دارم. ‏چون آن‌ها همیشه در طول سال‌های حرفه‌ام از من حمایت کرده‌اند. ‏می‌خواهم به همه آن‌ها بوسه بفرستم
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97803" target="_blank">📅 05:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97802">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUpii_ymU5bB68nU-t6PWLQhXFNIY9cVtop5QIAVpBWWOjkU2J58KQ7_4l4Xmk3R9tJCM4PWYDq4fltwoQcLIN4Mds9xQBzBAdx4pHF2qr2LFDd9u5y15AuiiTfnKASV4-BPc_snjRIVueF7QhLb16bo-jUxkf-g5uhf-rtKFvxYHzItYtImw-pLg5UoXFC9mrqBk6mmBprzLGp25RJea3FOcJg5UAcqJqMIXFadFCXm6q-sOh9zL2W7KoSHxPFFhXjhubi4znNQ4cCu5WpOPn8EXawi7VzfuD6Z36XxNfdOcih7ffhBY5K0sL6j4Ar6-nZtOIEkdBvrO4-6UCSULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🚨
🇵🇹
#فکت
؛
گونزالو راموس به طور متوسط هر 47 دقیقه یک گل به ثمر می‌رساند. او 4 گل در 187 دقیقه بازی در جام جهانی به ثمر رسانده است و این بهترین آمار گلزنی تاریخ پرتغال در این مسابقات است.
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97802" target="_blank">📅 05:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97801">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vocJgdZ13j3dDHOBsmJXiYG8-AXT-o3Uqba8-P6luWMKQFYhEpfYRbEU5WxYpNqwmzaRXcT7BZwNOqDREApm1SkZAzjNT1L4W23W1Xbd02JJLXfUF3tFsVTasCgHmcQLufVXsFyIRQSVoHSuqiv3V5Tp0RvvQC2OZSSKrYWeUy_HMP7ify4ko5zuWRCE8SZi2FL7KBKov4IKCDQqPOePJae7VflUJrPtqwiMqt8DY2ngsnJuIqxELE9UZ8YmuWTt6UuKSskAqpQWIK75-MXAB6FTsSzhAMswAoUAGRFYMCCCd6D_z-c5K5HKEQIPU0wUoIZccfCoIPXFcXE4kcyIzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک های کریستیانو رونالدو بعد دیدن تصاویری از ژوتا
♟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/97801" target="_blank">📅 05:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97800">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👀
آخرین تقابل اسپانیا
🆚
پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/97800" target="_blank">📅 05:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XrM2saIQXK5tcMWSOfGqe8v7LN0wCD0BmdA-UNHRFIToW8Lu2z2OgIMPScXluIVlnAOAQTF-cBlVcDpAWfublvolEYWEP1134b-P3zA0KcQeZzUSoUdh-0qVQ8fiFcuG0CeEChMFCKZmHb3Q1QXs76YzksF6UW-1bpTn6WM9Pvhpk9cM4VvPZ82BnmDHCbM_2PUNfsQhJvWHgWrDQfNAGLofagr06QVHdxatWxxyW-76T5cGjH5ryPYpW781tdr7WZKkVbLif6JFSpnbhnwbSWJTL1l2wMlEbC4wH0yJYmo0_s-dhQwjCjaC3WoMyu99N-e3_01Vu2xVk3YZ4sQywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCtfieFcZRCbZHqGFmZQZFQR1A7batYkrKYk4nUIevXmORg32vrvqgrzufFBJMiK72B7mb_RdpEFIS995-tZlvih64o6a09XmZJbmo7FoV6H2Sl2pzXfQkCrPiRxAoTWQTSZ9-qwwl-NeEaIhj5vBe8vbYvVGDtJeFXBRmIqGSKunpFMz2guj7CQOxp5Jg2uxcgzsQLmHJgBCnOm0yCY40Ii6nDg533KB7uo4iWHCSW-rigeMyIodGRSVMP4TKVtydNopSNPGFQHNHvlusqjC3FyclG0yethaAVYNJRRmviK6toGXIu1eahWKxV7rqzzVEZbdcVg1yfaJ86OvJBsOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به افتخار دیگو ژوتا.
🇵🇹
🇵🇹
🇵🇹
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/97797" target="_blank">📅 05:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97795">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-5D6V3h3UE7xEs_zP8VO_QktV5UO8z-7mQ4mlVsC6ypCMlNXON1b2D4obgAr8g4Izj31dLF0iK-wcf-pXnN4OYWbdO1WKOST-1IlPZVAerc9gu-kJ8lZJ_pZR8iOFpvDJm4_zIl4CWEJresst-MG8Clu1qz05stmxtEScTkWmc4u4ljH1xi9ea4nN5cy-xu9qIyb9oRQBGl6MQ5tF4H6il6L8q_mCUGMMY055-Ivjyjxqsd9xq5emCj_Kn1XOI94MDRS8EC_wkXRWPfZ3oDYMAVPMC56pLMZlOkMEuslKK_LnCu_aNLB5ESLzMfRFcfSig3cg6c_fZaL5etGf6yEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از اون عکسا که دوس دارید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/97795" target="_blank">📅 05:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97793">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gG8ik2IhWSSqLwIT90UreSfKLV_4y3y9XEXN0BLpsnJOdx2SuTW4ZQ-UuMU6eX7pLOj3GoAcuMZFG6USBiYqVn7egTfce12AGjnEkxfTfwKQP4HCm7Gi0DSyS42Eh4XouhRbRAAhz0sUrcsbVBbs_0zKYebPgkCDJW0j7pQ_3A-kplOh5h4pT5PLLpTrCQsnOR-MqOsNWaLlVv4HKmdfp4zE3A-1xWHRVJuTThpK4ChJzJQkspWSpXqj_CFL4xZpVQeTdMuRa2KhZRCRo1Y6x_9yoHj-9rpLqfDqcQEMDQlAeNpIAtk_xdLio6s3bnLwL3rCnZye7mTLz_t7pZ_CuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Em528_eI6xasg3uCoERG6_I116G8t0S2_7I_fhhZes9FbRM_ilpwYBFmCfYJ1h0pfcyLoPp7oJT1opivmJ7vyH3kekD7AKbVBhpJtxwDAJmeLJ82ruTMdd1RFtOvl5-I5RFUj1Jq3ydXIVjsjdHxoFSqokNt93vTjcPNzweVluQ9MF4KLYqBsAZZy7hn8gba7TSIJKE9eBuuQOkdKiLxfeOcmyc6tCLn16fJSV0H_7zMNTJXTve-sqQ1eMn7BeyIvMCus2r3P3KumpNyhvJeYZn8Zb076nV6vbOGMtoMNetK-6q1DHH2gc-7LRGMdJA4PtAE6nbHp1qjUAv3rx3sCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تقابل دوباره و این بار در جام جهانی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/97793" target="_blank">📅 05:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97791">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FG-BcU2ZYUU-x-0bNKXqiSiT1TIhgLeYDjIkC8wczf2j_cChSBvITGwxjCjwct35zVRgWiSZit2dj6zQs9AacWCoS12mInUJTCSbugTcvznheql-a0M-8aO9DP40f75MpnJdSYemKHd9xhV27Sa9QrRJCJeGizcbZo4Y3-hBbPpyAHPLuPRP8D5uiJimsL8E02Xp5AOT7J5zHyhnbNoxpCH6AqDCquHadqH__jQs6fKHZfT50dO59E0DmaRF3abOsdbKs15qQj_gjXAeLoLNmLlNLS5RnekE5Rc2DuWYpwHGTAGdFAYIg2MJccpnlBVdq2E1le-X7YKbMQquuB0AjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
آخرین تقابل اسپانیا
🆚
پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/97791" target="_blank">📅 04:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97790">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O85wOlsAYExVCw9y5FxMcOZiF6xUvHYygTTf7ZIzbHEb7dWfiyMNO21D-cnW9C0xjsWxQLOD7T2LvhbnyOKGwQMHzsIgQudziKxQRDVNvpQ-kDXwyv2u4dls9g59eVCUTjZm0v1C6IMhjgwQinznlfmq_Fi2r2TpXTYMEga6Qws_r3gDSj0-0748gK4CG7dLocbFVVLZoyPw9DAfk6O46dD7WBq5pBUw72Ys04lzg0Sz5M5O_0_PrzO7XU3AFcZsZYxwaDPprvEblWkvdU73NNVV55FKZBCIgCnmAHnL9IC8zxZ6-_FizNhWOHuCvGuqo9ZEvY4xoUXR_Zt0WBubCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مارتینز کسمغز امشب هم با هزارتا مکافات و کسکشی تونست ببره ولی در نهایت این سبک بازی محکوم به شکست مقابل تیم‌های قدرتمند تر از جمله اسپانیا و فرانسه و حتی مراکش خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/97790" target="_blank">📅 04:51 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97789">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG528-AmgxyuyuSULkrHJ7CmkaTw9rFsE015A9_Ad5Wm4mIx3jJTP67s6eZe9nFDXvdIr22KKdMrc9BHuxNZtb3wRVdIuVFTK2CKY8Hzo-dW4HnQt1RGne1mo1dgbzim9puIzVKJftPSVyvTMzDacguWvTV639AWcfMaEuzjsERl_Iga_dennXdFwrc_YPJszBP4_7YBgXTC4YjnA0hpF0JD6m9mqftURJnPhlW4kD-hYTgHcAeplio512UtYSwn5AcZuzVFLr4B5l5TG3OGCR9RwXqmYM_NjHPc3kLJU1X-R5P_ffkU3CKuuwPWezMXprmETL1GTqvTq0l_M03LmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇵🇹
• کریستیانو، اسطوره فوتبال، اولین بازیکنی در تاریخ شد که در مجموع مسابقات جام جهانی و یورو، 25 گل یا بیشتر به ثمر رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/97789" target="_blank">📅 04:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97788">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIY_GCWoYwMvEfuTgHy3Ym4Bz7xvHsDTXPzc8JWr4NGvboK3j8_zJFAXH5CfdeELwjRJKIt52ajwDUIYn1He0lX9rXB2KzUd3_agUVYAUs-MpEczW7wjKAyXEzm6afsrDrrw7lnIdFVH1txtUqbXraoiWUM6lftE_f7qPF7vTpE-ddDpVTVVve16CvlmZBnmyYfoxfE1S5-6BGdp6REoDRbqK8BA-Aaq4Q8iD9yHf3zX9gt1pwlw0vmjgepzfd_hGKfLduC_jZ66J_a4wLWfI_ZYJ9T-oHrL_TWwaf7-KJhOf91gDnaFo7UR92u9SBYRqfpfdLnp7Zw5SgAuK5IUCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
🗓
دوشنبه 15 تیر ساعت 22:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97788" target="_blank">📅 04:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97787">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neegrTamZ1F65dRmLh3RIDoJCexQMr1LzoXx4UVsEmc6BuBki0ws4oLVQMz7MqE9riuntWIf6eT3rg3wqHUb_Ud0sF1qYygVFlbC_dEf78ID9n7s_zThB5ZA9lPXuARdc35uS_w4QKyPaeyzf6F1jtn2FDcYEwXF1iFjyawCh-UgrbzgELi9OwbAXQuEmxXdqfT0suMT8xBsCaLXHoDMKzzV7LsVonSTMnQGSkH_BiFTF9EH6owHHuGctHzDU8G0C5ZL6-2Bap3koQm4mxAcsAkQZqNLzlgdfHfRaNIUX2TuNaxhPbEYfY9WqzwCFK3Sol1KhVKq2mzp-8ZKUXk3XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ مهاجم جدید میلان نسخه مودریچ و دوران حضورش در جام‌جهانی را پیچید؛ فرشته نجات پرتغالی‌ها بازهم گونزالو راموس شد
🇵🇹
پرتغال
😀
😃
کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97787" target="_blank">📅 04:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97786">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auAbaHoxoJgvN9zcuICM30Jz4H3TjdtJnbWBgp5ALmKgnqBEGNSu9oyychrexmRdlO5BQtpkqmgD6IplGMPM9kK2DpYeq0XHGhp_GqxJHhQ-Nt2aOTQkH_rBzrvp_NEQMq_f6kNl_H5HJ2ZW6jxp828cVYs92oDJYmSdx20lMRYFuC6dvRjvakk_BQ1TMIbhBpiMLnTf5n-EPDhsmMYAipOaR9m4Kfj9pJK_NXNa5MIWofMZXdRRHsYXY-i4yXlKJRu-5VB7Kc-AtZnTsRtDwM_b0-1JvaTW-H8S1Qf-rvGprNaAPmWUOHCs6cpheRqwZ6Xm9mMNrSS7Jt_Kf5_ITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار مرحله حذفی جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97786" target="_blank">📅 04:44 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
