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
<img src="https://cdn4.telesco.pe/file/odtcdlrOfbkelo_Vj87Q4oy_rman3GbbIdsQfEU1oSJPRjPR4lZDCqJE-nT00AyG5R1m27JjYntj7KD4hzUFxOHYUY-e4ndGfWS1smBdevnyEth941pom78-X17nLHCC_QILDblKxkQ1fD-ivgwVH3hS6h17F01-tBrZfGlo0TPQGmHOf3SBTPUmmalzoT9NGUyrxRy0rrmpLxy0GuAj3YTzbAElF9hpRLZyhfLUcojdqoHCS29ABCxg_i8yL_IE-mivZoqgXE4QW3shrVX0qbSgMq21uTtgKIrBY3jKGh_gJcWxgrZe_As4VcuI_5OCJYHkS-0_K2LcF3qjGkuDng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 18:08:14</div>
<hr>

<div class="tg-post" id="msg-443451">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خروج یک هواپیما از باند فرودگاه مهرآباد
🔹
سازمان هواپیمایی: پرواز شماره ۴۱۶۹ مسیر شیراز به تهران، صبح امروز هنگام فرود در فرودگاه مهرآباد پس از آسیب‌دیدگی یکی از چرخ‌های فرود و کاهش سرعت، از باند خارج و در حاشیۀ آن متوقف شد. تمامی مسافران و خدمۀ پرواز در سلامت کامل هستند.
@Farsna</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farsna/443451" target="_blank">📅 18:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443450">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c507c128c8.mp4?token=Prd2shcjz7bVONeRKU6KJJpApCoXz0pYMYIqV8B4w949lKfKFbAvbOJog8fI9SdeCuRZy3aTl_OMd4hjcmRoQUpw87TIj63bs2y7vCAp1AQjuuhvUp6GVwJHPmepjfoO6BONdr7RjWBk8o39q84dvGO0ErjxudzqgJha84FoPai01249tHD_rp1FacitmnYAhplh4LRAQpQgi7L7xJNmasTvDB--q36IGT2B9I99pKsmG6_NWLoOnbsJT4EikbEMGI-b4FfUtZuXwp4eupRWabLVcn9gF5M6XX9hMRlBZyaFKjs6UkbqWO0LC1w2aPb6xwtfJVLyON7Ldb10esnRvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c507c128c8.mp4?token=Prd2shcjz7bVONeRKU6KJJpApCoXz0pYMYIqV8B4w949lKfKFbAvbOJog8fI9SdeCuRZy3aTl_OMd4hjcmRoQUpw87TIj63bs2y7vCAp1AQjuuhvUp6GVwJHPmepjfoO6BONdr7RjWBk8o39q84dvGO0ErjxudzqgJha84FoPai01249tHD_rp1FacitmnYAhplh4LRAQpQgi7L7xJNmasTvDB--q36IGT2B9I99pKsmG6_NWLoOnbsJT4EikbEMGI-b4FfUtZuXwp4eupRWabLVcn9gF5M6XX9hMRlBZyaFKjs6UkbqWO0LC1w2aPb6xwtfJVLyON7Ldb10esnRvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ظهوریان، عضو کمیسیون اقتصادی مجلس: مقامات ایرانی، چین را کمتر از غرب تحویل می‌گیرند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/443450" target="_blank">📅 17:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443444">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال عکس فارس | FARS IMAGES</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gTujQLQHs6ResGqVVeueJaPgYWgBDGoq7zaQCczAZDxU_TU9bGLq62s6R_Lbg1yEJsEZE4I5_5jQI46yoYZk4lmHvHeKHbscvPFZ8ZNVfQnDQNOfgk1il0bpi7Qy5-sb11bNCp1vh0EXCBeZ2qu4bDJlwPkDiKXhcV9Jpw2WhVh5OFxOT8iFXRNSPrLhRpdzIk_b17GNLs2MfkdMTw8CJwzrCwzOcZiopAp8oQlroi6nfJjjY4FT6r2TyyAECcbNYjEy4P59kFg1UzC-jP9LkeBxnNjnKrRN5pFCHLYCQfTQ7b-3-wmbQzrFyDlQqD2wXu86fM-6X4pC8GET8fVHnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vwyn-TEPW2MdDTYJdkadfLgI6avXPWycpklRwxI_XnUPVD0nWWqVwm3TOy8Gmik8Co3Zf8sEwZNzvli4Cvt1uHbFJYrJyTRoGTHFeW09CweMKO9YfdKydoGpVbKLzv5xQ13oYpwPE3YudfX32vCaB6IokGESnLSRCOkCp7T1bErZcsK-pRKccqTxB0D9-dm9-gXuOIvBeDJB-l_IWNhM4pEI0zhowDJMADced_fef28X2ZiguFSwjs0o--PmcipWq3cruxmuVnr8pxP99QRNkBtIz5yXI-2rRDlEnWXHYpf6LJUUSoAseSeXvJQLcO9miQFC4Vmv7z0s6ZTEo8uZUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zrs4wrSaImfY770QCemYV1yYaBuEtYiWcFI1-wy82Y3sfp1RIv8IsM3306sq5w9wmm_Vfwfi2qoBO5YmvTc9vtYMCDvrpqtcE2EJ7yqIk7XpP54vh131CUBbWdPlDu_iqj-m92DVggOQTJ6R_Dn1Q85yAi68FjBz366zE4xqIoA4Q5xU4FGqx9Gfxy2mT5BIBynQ7vkT9kI9OOzELSeSW9NMu3UXHWZfxx3JWrCBbtvcq1xFExaKUYacpwl7Dd_mzhbPVOW6PNMZf-TYfgr_HqUMpiCLHYpvODd_iQt4JIt4ObEEcYgZHsQC1kn2HZzu4rHqWirkFdpuMGsuH6E3KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JK8pMZCQTmeQpDN-FdjRExK0uSCragbmxuR8ed4ysNfo4hpYRs4wyYh5N6ezQaFqJhNso0GVb6fgMjlmKYNpScHT26W-7N9y7aTR2IITvHnhRw9Thu97XnCZoC1k9nX7SRYhx18YPoPsX9fQRinCUavdlt720E0G3RJzdzyxHivtSFQoB6HDl2aBrTLpbLxLqh_h4U9_pMIod9xdsga7O2_RheL2T2dHOsAved1Lmt12OZvnuuxNrFDzqq2z7JbflhMjm3X4zis4_pV9_Qc-Jk4_bee50XV6-TLwv_h4w-UX7oZ-tlPJ3AjrqKStYST14Vyteh24-hhDmVCJf87KFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uh4WqgIsVJlz8emZKF2Sbm8drVOPX61_2NuhCvey7MT9SogfdWG1PGK2YaIhyI7swIQzUXWJipPXtNE7Id4eoV_874pTo_X136YMRAgbkkVApi8TVmqQ8-R2ngR-_0k0d8BYfILB7tm7taWQ_qdTq5KTRiEjHmufsyU__dEStJNkdQpRjyc1bUy9dy0gH0__bDlmi6TblIxOsu3o0udS9CbnURm1WXyFpGyKHXPJyiS0WA4TpTpWgmsb339KzlWkjbKZxUDrg3VeObCNAVL8mfU0wKQM2ZLQDx9Fov05LvkidLctqb-cpdhtL9AWrpUS4gcgkBNfxHmbTjZycbaAtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UzPzOLEqMywrz-9n4TAx2pvZ1e62j6DJh3QCLqzHWET3N24iPRYqXf0uOZ-KLmG28TvGD5qludZVv0PVL6n0Cb_VYTchQLPImlpCqvohbPEzBik0odsRMPL-Q1SGD7dXhZEC8_59rZkAEfcaK0NiHxk0USSnufRXUuKRL08YFI7xMO5ZcM9BXysGIJTzhiBvLA5hwgSNYeu2H1aAd9YVRDOqCPEFDcSDeBAfC33BYzj08-qhyVYey4WXqG_XyvFHk_cMD2LvFS78Kgs6FdwdUHdOpG5T1tSeEHgHtMG6iMPadALo5yfYnh7fTg6JAH7ygBbgwYlFJ91MnTYTxgvLDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📸
دیدار وزیر کشور پاکستان با سید عباس عراقچی
عکس:
زینب حمزه لویی
@farsimages</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farsna/443444" target="_blank">📅 17:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443443">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mtp3caGJtQf7Yvw-7DcEQdOLkkhi9a-rri8AjcGDpnsK4LSenGNPqNWrgLP_QDk-_gFvV_DiQp4PDBiEVdiPltb8UBYp1CP9IWY66ZGimvW8VE3Yb1i6e71IYc1lqCvzQYQaaA4hHkMlg3OJsVlFCea_K-Uftll21RigSdP8BG8PAXgcHfR0W6wF8_zG40Je0StyflcuxjSFP7USwB7_bNL7-JwEa3kQ_3Stmag3csVLFJzk7WgD0GAJuwmMMBekNllzV5vjDovAdIfrfMPnIarDbVYkKi2kKV7KZL1FZ-qtOqZ72Z4TPDCSHeBGUmz4fkj8YJ3D-niaK9hZt4E6Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استارلینک پس از پذیرش قوانین عراق، مجوز فعالیت گرفت
🔹
دولت عراق پس از ماه‌ها کشمکش، مجوز رسمی فعالیت اینترنت ماهواره‌ای استارلینک را صادر کرد و راه ورود این سرویس به بازار این کشور را هموار ساخت.
🔹
شرکت اسپیس ایکس برای کسب این مجوز، تن به قوانین و مقررات عراق داده و پذیرفته است که فعالیت خود را در چارچوب حاکمیت اطلاعاتی و تکنولوژیک این کشور پیش ببرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/farsna/443443" target="_blank">📅 17:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443442">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhWj4_h8v6FS5Y9VqOngJq2ln_jBObhz5hvUc5d6ovi0EAYEjp5tDg7Mp1J-wsl3mfgfUjmfBOgvVO6xBVX64J81RvpfrvVyaqKVHhasUap3H8ZfHuS6PotWL6UCi525zsbceaXl-0u_osRdMX7MFoAV86l7FUrhSLY8EvqLaceo4DOcuGhTBWdYUYKBJiYgPJ5oEtFfviIwojw0157XCgv6PAIo85xcQGudww8p-lMeGS1XkUU_LIKS8jSxjApka6EmPxi22DIMkwgcvKnZWalRHu4mK1zR05H1c9RYdyIFmRoFc7gYe4MQhnKpoEGM7ZhtUFabQpEiB3CHspJRZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمار شهدای لبنان از ۴۰۰۰ نفر عبور کرد
🔹
وزارت بهداشت لبنان خبر داد در جریان حملات رژیم صهیونیستی تا به امروز، ۴ هزار و ۵۷ نفر شهید و ۱۲ هزار و ۱۲۱ نفر هم زخمی شدند.
🔸
این نهاد لبنانی می‌گوید در حملات روز گذشته اسرائیل به جنوب این کشور، ۸۳ نفر شهید و ۱۴۱ نفر نیز زخمی شدند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/farsna/443442" target="_blank">📅 17:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443441">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‌
🔴
یک منبع نظامی در نیروی دریایی سپاه: تنگۀ هرمز از دقایقی قبل به‌طور کامل بسته شد. @Farsna</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/443441" target="_blank">📅 17:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443440">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔴
تنگۀ هرمز بسته شد
🔹
قرارگاه خاتم‌الانبیا: نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم…</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/443440" target="_blank">📅 17:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443438">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: اگر بخشی از تعهدات طرف مقابل اجرا نشود کلیت تفاهم دچار مشکل می‌شود
🔹
طرف مقابل باید هرچه سریع‌تر تدابیر لازم را به کار بگیرد وگرنه کلیت تفاهم دچار مشکل خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/farsna/443438" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443437">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه:  آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
🔹
ما به تعهداتمان پایبند بودیم و طرف مقابل موظف است رژیم صهیونیستی را به توقف حمله به لبنان وادار کند. @Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/443437" target="_blank">📅 17:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443436">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: در سوئیس قرار است دربارۀ اجرای تعهدات طرف مقابل مطالبه‌گری داشته باشیم و مشخص شود آن‌ها چطور می‌خواهند به تعهداتشان عمل کنند. @Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/443436" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443435">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‌
🔴
سخنگوی وزارت خارجه: هیئت ایرانی برای پیگیری و مطالبۀ اجرای تعهدات طرف مقابل به سوئیس سفر خواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/443435" target="_blank">📅 16:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443434">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
تنگۀ هرمز بسته شد
🔹
قرارگاه خاتم‌الانبیا: نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم…</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/443434" target="_blank">📅 16:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443433">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
تنگۀ هرمز بسته شد
🔹
قرارگاه خاتم‌الانبیا: نظر به بدعهدی‌ و پیمان‌شکنی آشکار آمریکا نسبت به عدم اجرای بند اول تفاهم‌نامه پایان جنگ، و در واکنش به نقض بی‌وقفه و مستمر آتش‌بس توسط رژیم صهیونیستی در جنوب لبنان و کشتار بی‌رحمانه و آوارگی صدها هزار نفر از مردم مظلوم این سرزمین و همچنین با توجه به عدم عقب‌نشینی نیروهای اشغالگر صهیونی از اراضی جنوب لبنان، اعلام می‌کنیم که تنگۀ هرمز به روی تردد شناورها بسته خواهد شد.
🔹
اين گام اول پاسخ به عهدشکنی دشمن است و در صورت ادامه تجاوز گام‌های بعدی برای پایبندکردن دشمن به اجرای تعهدات برنامه ریزی و اقدام خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/443433" target="_blank">📅 16:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443432">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/751d1e0b88.mp4?token=A030S116dKDyRIrYBYbA1QXPfHyt3PORz4CeIU2ZMP4L7qoYTrc7Me_FPi-buQ-FxC7uBQXi6DA8By4SVCtivCWrx3J7uhOBeUi4B1V8GNO16sRGwY90uOl5KILUqyg1cbimnEKFO5ZySZwqOuO68G3qBlVSBb3BEyIVmLh1o-7gLCvZi2K2G_5B1JPwRv-nKtXFu24QGK9P5xS3-iDxG25C4K8UUQ5MU4Oxsox37utU98Itss7O8-pgNz7qhZmZBUYtBMj16NjfTGaywS25y1Ao-3X5TdYReiI8Sjfo2ZfrRGSIqqy95VR3mdN7lSr9YTvsfqJHXvPRYSr36_r5iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/751d1e0b88.mp4?token=A030S116dKDyRIrYBYbA1QXPfHyt3PORz4CeIU2ZMP4L7qoYTrc7Me_FPi-buQ-FxC7uBQXi6DA8By4SVCtivCWrx3J7uhOBeUi4B1V8GNO16sRGwY90uOl5KILUqyg1cbimnEKFO5ZySZwqOuO68G3qBlVSBb3BEyIVmLh1o-7gLCvZi2K2G_5B1JPwRv-nKtXFu24QGK9P5xS3-iDxG25C4K8UUQ5MU4Oxsox37utU98Itss7O8-pgNz7qhZmZBUYtBMj16NjfTGaywS25y1Ao-3X5TdYReiI8Sjfo2ZfrRGSIqqy95VR3mdN7lSr9YTvsfqJHXvPRYSr36_r5iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقدام زیبای نوجوانان تهرانی‌ برای کودکان میناب
🔹
پیراهن تیم ملی، یک پیام جهانی:
🔸
«کودکان هدف نیستند.»
@Farsnart</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/443432" target="_blank">📅 16:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443431">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cu4Yz1HY7CbiwFK2pZMYrGLGfd4rY4aHo9bLgdojkydTQl7Bs33C_cAEiZCkvHiW-Arfsim017P2ERR7OTpmnw8N6sZxC1PRiHjiW2gVIT0uMhN9o_Y00F0XqR6I-7Awh0-3MhIfEBte5QHFrdcyCh3rvq6ZG52qsF76glfQMSAuylyUsA-yhToadY3I8raspPsaZ7XksNDgGAvdD9nWZJ69qHW0muH-2xHhHW4tFU4LyvO28wp9735By4s8nCGWsIrBCcnwrOkvoVUI7LjYVN2Q6Xh_jS81fWKLxAmOOjsEV9mwUcH9cRoxvuNo3Y7nzpAS5lnCwUfGB3MoAv7n1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان وارد مشهد شد
🔹
وزیر کشور پاکستان که به‌منظور دیدار با مقامات ایران به کشورمان سفر کرده است، دقایقی پیش در مشهد به زمین نشست؛ تشرف به حرم مطهر رضوی از برنامه‌های نقوی است. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/443431" target="_blank">📅 16:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443430">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d80b7c7a4e.mp4?token=gS9OVyWzhUC2ASza9QRNbUNn6Jnb9jbixBPRQPdqwiL0EhGBW_mC9WCJgUZ9jVVx5yaEIuFEdx_KLRH9SUYhxBeujWjMsCTMG5KnC7_oBt9yq_FzorvTHLfRZHSXc2hNuY5nXmlyBNG1UOSlYXrFc4Nf8Z1ZUVIqFO3oj76P_sLjMPnEUkBIlCxXToPMVpPB6gMVVrSmKs5YQEFKkr97D8Ft2Sadp2BK9dB30xCCo8OVeVQDqyppnw-KRtcfTdLe60uaUZnH-O6YwTCCsmEgr_iDUZloxhDa6QB7sCq6BSEAid9yjS6PY0NcxjEBdolatRUjUB7pMerKr2b_Z6BNuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d80b7c7a4e.mp4?token=gS9OVyWzhUC2ASza9QRNbUNn6Jnb9jbixBPRQPdqwiL0EhGBW_mC9WCJgUZ9jVVx5yaEIuFEdx_KLRH9SUYhxBeujWjMsCTMG5KnC7_oBt9yq_FzorvTHLfRZHSXc2hNuY5nXmlyBNG1UOSlYXrFc4Nf8Z1ZUVIqFO3oj76P_sLjMPnEUkBIlCxXToPMVpPB6gMVVrSmKs5YQEFKkr97D8Ft2Sadp2BK9dB30xCCo8OVeVQDqyppnw-KRtcfTdLe60uaUZnH-O6YwTCCsmEgr_iDUZloxhDa6QB7sCq6BSEAid9yjS6PY0NcxjEBdolatRUjUB7pMerKr2b_Z6BNuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قاب هولناک جنایت میناب، برندۀ جایزۀ بهترین عکس سال جهان شد
🔹
مرتضی آخوندی عکاس ایرانی موفق شد در رقابتی بین‌المللی و در میان صدها اثر از عکاسان سراسر جهان، مقام نخست بخش «عکاسی خبری» مسابقه Golden Shot Photography Awards 2026 را از آن خود کند؛ آن هم با عکسی…</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/farsna/443430" target="_blank">📅 16:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443429">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f98ac79ff6.mp4?token=psVPG2iN_FCKVH6LEWZTz55BkMx3r-BxyoVxDhrWaNqsj9kGxbFegTvHHliDefW2mpW_fUWZaigm0phtlzxh4N09iv7dWyRVsr3S9_TQnwUs02P1rAcqOzetFNtC10Tl7ps8vKtdou-DZdI3S71vTTF4Er4jLnq-Dw7Hp9uBen4rH3jK0YeVO8iB9HIU3EOP9nzIevGRE7RNU5ZHrFOnHQgoP5fGSsiZtacTT0w7BFlYVxCfUK3CWf-nM-2jRdeaArogXEBhw9sZdIqfXYucKOH_cSccRiT5KWUGQ-IvP_OCJeuM8pfOS_JXD3d6czPIHuFojvg3f6a7KDwBNmxyFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f98ac79ff6.mp4?token=psVPG2iN_FCKVH6LEWZTz55BkMx3r-BxyoVxDhrWaNqsj9kGxbFegTvHHliDefW2mpW_fUWZaigm0phtlzxh4N09iv7dWyRVsr3S9_TQnwUs02P1rAcqOzetFNtC10Tl7ps8vKtdou-DZdI3S71vTTF4Er4jLnq-Dw7Hp9uBen4rH3jK0YeVO8iB9HIU3EOP9nzIevGRE7RNU5ZHrFOnHQgoP5fGSsiZtacTT0w7BFlYVxCfUK3CWf-nM-2jRdeaArogXEBhw9sZdIqfXYucKOH_cSccRiT5KWUGQ-IvP_OCJeuM8pfOS_JXD3d6czPIHuFojvg3f6a7KDwBNmxyFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شور عزاداری مردم یزد در حسینیهٔ معلی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/443429" target="_blank">📅 16:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443428">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9757274c43.mp4?token=RRbpd5ZX08VILRiGr6nMWkkFatWCEu_aaquqdJHnqj9AxW5Z402skJQ6i6_YC108olKYIPQazQgUm2xkqiMja_SGgas6b4YqvAjnOv_FiXVqy2Odu2qxm778ZYZLg730ROC1la_qtRQDNcRJGK8X6KYjlo0yC8W5_Qxac-PSYV78tT9O6WJoqQJyCO020tDEU_coibTnAOIH0px3hljcy8WZEKNB90vXrksDQ2uhpSrkD0_-WHSm1JePpL6kEkusvJkzbGrBQEd-Sr6JZ2Hh7KXc5ISyusnlxPgb8RaYWX9XeECezupcZIhwHkrggu2JWxmbMmSzD3bOWD43ADbP4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9757274c43.mp4?token=RRbpd5ZX08VILRiGr6nMWkkFatWCEu_aaquqdJHnqj9AxW5Z402skJQ6i6_YC108olKYIPQazQgUm2xkqiMja_SGgas6b4YqvAjnOv_FiXVqy2Odu2qxm778ZYZLg730ROC1la_qtRQDNcRJGK8X6KYjlo0yC8W5_Qxac-PSYV78tT9O6WJoqQJyCO020tDEU_coibTnAOIH0px3hljcy8WZEKNB90vXrksDQ2uhpSrkD0_-WHSm1JePpL6kEkusvJkzbGrBQEd-Sr6JZ2Hh7KXc5ISyusnlxPgb8RaYWX9XeECezupcZIhwHkrggu2JWxmbMmSzD3bOWD43ADbP4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست نیروهای شرکت برق از مردم ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/443428" target="_blank">📅 16:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443427">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/189907ab09.mp4?token=jfFIBtGaG96OD6doZP2yX7os4EjeK6fB6o8Lhwn2nsE_r_gA6DeanXH__HoKZVuZKJOZtbKHIOdXinR5si6sfO_Lo0dm4PDpIIiUzKcgLCfm8gMSMgF-VgPfsTxOGbXEb11nnQzVwlxI9JdESHZoO0ssVDUMdI282xNc-he_ncc-9xQT_VHmjqQzzoyUJ91s14rw-RCuYrBFqyGZbsZJK5b_tuSaYiB-v3Fgr8FMb5r5gENCuIsqwXtuoE4_tLrgQZxZ4Xahqbdk2nmso8mFHYTrLB7WlE0mSkiOADLPdiP9Db_Cnq7gH1NyIXs1yKOzj9c_jTcuPTNzdy7STmuqZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/189907ab09.mp4?token=jfFIBtGaG96OD6doZP2yX7os4EjeK6fB6o8Lhwn2nsE_r_gA6DeanXH__HoKZVuZKJOZtbKHIOdXinR5si6sfO_Lo0dm4PDpIIiUzKcgLCfm8gMSMgF-VgPfsTxOGbXEb11nnQzVwlxI9JdESHZoO0ssVDUMdI282xNc-he_ncc-9xQT_VHmjqQzzoyUJ91s14rw-RCuYrBFqyGZbsZJK5b_tuSaYiB-v3Fgr8FMb5r5gENCuIsqwXtuoE4_tLrgQZxZ4Xahqbdk2nmso8mFHYTrLB7WlE0mSkiOADLPdiP9Db_Cnq7gH1NyIXs1yKOzj9c_jTcuPTNzdy7STmuqZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فوکویاما: توافق با ایران چیزی جز عقب‌نشینی کامل آمریکا نیست
🔹
دانشمند برجسته علوم سیاسی فرانسیس فوکویاما، توافق با ایران را «عقب‌نشینی کامل» آمریکا توصیف و تاکید کرده که اسرائیل و آمریکا با امضای تفاهم‌نامه با ایران، مشکلی را حل کردند که خودشان آن مشکل را با شروع جنگ ایجاد کرده بودند.
🔹
فوکویاما معتقد است که دونالد ترامپ تمام اهدافی که دولت ترامپ طی سه ماه برای توجیه این جنگ مطرح کرده بود، به مذاکرات آتی موکول کرده است و هیچ یک از اهداف دیگر آمریکا برای جنگ علیه ایران از جمله «تغییر رژیم» یا «تسلیم بی‌قیدوشرط» محقق نشده است.
🔹
این کارشناس تاکید کرده که بسیار بعید است که ایران طی دو ماه آینده در موضوعات مورد مذاکره انعطاف نشان دهد؛ زیرا «دقیقاً همین مسائل با هویت بنیادین و بقای نظام سیاسی آن گره خورده‌اند.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/farsna/443427" target="_blank">📅 15:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443426">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03f13d2ca8.mp4?token=ZNKwRIdI1XaADT37Em7lC_MVHGbzFtPXm2A6OwKzBGSVq3uwvXf3AgZSZQTnMmpZBte5OamJuThf71K-_jI0gBAxBOrvz_0SZ-cudVtJX6stWyP5WytT9OBeEzpxNAqDa5f4te5uVAU_Nt4wqZPX29oxtkxDIrEgx4RF_nshEsBPfqxfKiO7_NCnyHqNn8m0NOdqqE_YhOZU-t8_OfxByRncua9O-TJUH-8e7FhI16TPWMxH_ga6g1zegEwP8H3GzKA18Pu28eaR_Lv0NhzNsm1ipzS0ha9HuvUlJQY4v44Umz2Pp3QGzO4qZ8YmDMINrHEaAviioj6A0loYjOB-Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03f13d2ca8.mp4?token=ZNKwRIdI1XaADT37Em7lC_MVHGbzFtPXm2A6OwKzBGSVq3uwvXf3AgZSZQTnMmpZBte5OamJuThf71K-_jI0gBAxBOrvz_0SZ-cudVtJX6stWyP5WytT9OBeEzpxNAqDa5f4te5uVAU_Nt4wqZPX29oxtkxDIrEgx4RF_nshEsBPfqxfKiO7_NCnyHqNn8m0NOdqqE_YhOZU-t8_OfxByRncua9O-TJUH-8e7FhI16TPWMxH_ga6g1zegEwP8H3GzKA18Pu28eaR_Lv0NhzNsm1ipzS0ha9HuvUlJQY4v44Umz2Pp3QGzO4qZ8YmDMINrHEaAviioj6A0loYjOB-Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حسین پاک، خبرنگار حوزۀ مقاومت: اسرائیل یک عملیات نظامی بزرگ را برای تصرف شهر نبطیه آغاز کرده است
🔹
اسرائیل با تفاهم اشغال‌گری را رها نمی‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/443426" target="_blank">📅 15:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443425">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlCguniBhQi_AI6Fal3mTyuBmvLs9xNeInXzO3STvhxItFoWMC2AHj2oYSe-JdYp36BMxH750ISXktxLYSb0NMqQ9CnAHZyW3FRwhzh7mwqudHKaSYgc-IiXFEI8oA17yfdcymBHDfSUPDm8cqxrLkx_VON3rpbiMVAjAjO-2wQAIG83LsP97-SVtb6M4EQyYY5byEzTOf1d530p3xpR9h8xIIf8o2rRN0lO0TFv2O8sMQADTh4E6wEu9MH30byhAQqfFE1i5oaH7XtwAQie23FMKVrRc50s9aXoOZlb9utGMxmbNjMZuvisxa0D3KYXDu_COtRzfW66L-_SJTMDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یارانۀ ۴۰۰ هزار تومانی دهک‌های ۱ تا ۳ به حساب سرپرستان خانوار واریز شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/443425" target="_blank">📅 15:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443424">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwIzZjLtloXDT4yXCDL13RFVPOf81IhMYeo60qXLI6h8mjtKZKCeCBg5p8uhe0JKaRrOgG64Ljzwl1_rx5dd-8I6qpPERqG0H6hxa-x__plqM6YYteg9dQQ5skQrZsI6DCA6jTiFA27Foa_MSx5S8HFEaIPnFj8KRiQdlPidxfzlJxLsWuq1fc-yK0wYYk7JfbsPPVPvmnM4SPm-Own3OpXAXWzrBuvwXC6lzYufwxeSiUCGZNHkPFhA8u4VPZcl_q4Q8cJsgmkorEYUOcgkZFs_14ESa5W74g6ogC7PU7Xt4ZF_VU1Edohn8DmGBJjqtE2qDsMZSeesjAlPjXR9kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برتری شبکه سه در تجربه تماشای فوتبال در ایران
🔸
در این نظرسنجی بیش از ۳۶ هزار نفر شرکت کردند که سهم روبیکا ۴۴٪، سهم بله حدود ۳۱٪ و تلگرام ۲۵٪ بوده است.
🔸
بیش از ۷۱٪ شرکت‌کنندگان مسابقات جام جهانی را از طریق شبکه سه صداوسیما پیگیری می‌کنند.
🔸
شبکه سه صداوسیما همچنان نقش غالب در پخش و جذب مخاطب برای رویدادهای بزرگ ورزشی دارد و جایگاه پررنگی را در تجربه جمعی تماشای جام جهانی حفظ کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/443424" target="_blank">📅 15:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443423">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXqzOmpzABtQ-geN0p2Z0XQa9x6a1sU7ZaGCCmCdCVxfgxfTkvQN4Q2IavfrTcqGFNpMlDUgxbWem0ujOu0UKyqS_KjL0TfaXcRdW0D2C_iDsdvCscX53XXPe02WRhyshpEkIR1-1CSXFVRAtsE0OkDRkKpdR2QX7tWHQKoPu0M99sFc3q4JCJtrWiSjHtivM9W-2tfu-1yR8j_G79jgrbay4EPKQChjJbsLeCUFSFKZSBEK74L3jUqpqw6a_0xd6D5qHrvafWf5RT016p6K6ulDsshhIbXnZWP1USErRyk-8mI-ikv-Qea0DZY0bK4hjyprmv2B3JqzqAiA3Z8frw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#اینفوگرافی
🙏
خدمات کلیدی بانک تجارت فعال شد
✅
تداوم خدمت‌رسانی بانک تجارت؛ بازگشت تدریجی خدمات کلیدی بانکی
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/443423" target="_blank">📅 15:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443422">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/443422" target="_blank">📅 15:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443421">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd3o8_Or0nGZ3y8MidiSvaiwMYt80pKoZ_plXx8PVqM7dQGPSS67d5P914TESfxC59ZduKYfhazMbvs0CxH_S6sU84Nq-buDZ194NT3i8YJiPQ1HdzXzDM22TV5svXklW7BHCOriahAWLqOBh9p8q723n-OcJzYYfQgOnOhkPizy6nlDNgDzuJQddQq4UxomBL9g-YJ-I2xVMRWnp97N3VosKMTAL-4BkYEvLgN0fgtmMd7Xx596P0QCmwNtJcbyd339rq-YAPDEJYtO4W1Z_sXbiKoBrI4kdpvQ3Bhxkg7ID7Eu7PQwWX4CTdQZOP0bqXnmLshOZTqzmHOlcVCOdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترخیص فوری مواد اولیهٔ داروی دیابت و ۵۰ هزار قوطی شیرخشک
🔹
دادستان تهران: یک محمولهٔ ۲۶ تنی مواد اولیهٔ تولید داروی بیماران دیابتی به‌ارزش ۷۳۷ هزار یورو ترخیص فوری شد؛ دستور رفع موانع ترخیص ۵۰ هزار قوطی شیرخشک وارداتی نیز صادر شده است.
عکس: مهدی قربانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/farsna/443421" target="_blank">📅 15:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443420">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa76fba735.mp4?token=XUJ0T032Ad-LagCszufTh9jjp0rVxdzTAtXk83rPeeiph5xRjPPKWmg35g0hpVBQjPbfZXRDe90_NtbBk_ZM5uT8PYKZn6JeQQEWCQX4inSWvC61Y8S88-P8a7i9iHs0z-kvmhRu5JcieIMybPery_xo5DbSkCbn4EwXoa755vV8BMUPeFcOq2HJZiC5qn0WaUpz7QL6QYI2wtGhQjRkUZDW7MOF4dVmNI_ZSlJEVyiEcFugeMGECUzLcd-LQ4OWcTmz31XainYAEGqJUhOOL7MFtDYC8rhb8XBKipenMTprKbkx5BW5tfotIRamzO1f4wmhd9Tb-nXCs2D7xpwBm4A9wiBSDXWJ6P_DCHBNoKmYZTQu_vMVXGvIKLSmdWoMciQB82QNk2StNprOuLou5ypsOnBF1P5XZEuEFAHZdxpRnrl9hbfAVLn1xi6StrsfHM_X6N0kLW5SYIXkMyVC1GjBC8RfTcN06PYc7IyIS5i4UAezU6KQhP5vUG5fRhGdcAVJHfOl_jZ9er0JFjOqLKyMg6M0IriTie8x9DKBfVWDUWQw4HndNusBr-b9-RgvHqzv2-QT1tYult_fl-kY-J3Pd0KSE57sEBY4mTMg0TNXKVows_4k3FVgg0PqsWh8bY4iB6Lc7mHYXxOUAMINLxG_THrUxXWvg4o0g-9PofQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa76fba735.mp4?token=XUJ0T032Ad-LagCszufTh9jjp0rVxdzTAtXk83rPeeiph5xRjPPKWmg35g0hpVBQjPbfZXRDe90_NtbBk_ZM5uT8PYKZn6JeQQEWCQX4inSWvC61Y8S88-P8a7i9iHs0z-kvmhRu5JcieIMybPery_xo5DbSkCbn4EwXoa755vV8BMUPeFcOq2HJZiC5qn0WaUpz7QL6QYI2wtGhQjRkUZDW7MOF4dVmNI_ZSlJEVyiEcFugeMGECUzLcd-LQ4OWcTmz31XainYAEGqJUhOOL7MFtDYC8rhb8XBKipenMTprKbkx5BW5tfotIRamzO1f4wmhd9Tb-nXCs2D7xpwBm4A9wiBSDXWJ6P_DCHBNoKmYZTQu_vMVXGvIKLSmdWoMciQB82QNk2StNprOuLou5ypsOnBF1P5XZEuEFAHZdxpRnrl9hbfAVLn1xi6StrsfHM_X6N0kLW5SYIXkMyVC1GjBC8RfTcN06PYc7IyIS5i4UAezU6KQhP5vUG5fRhGdcAVJHfOl_jZ9er0JFjOqLKyMg6M0IriTie8x9DKBfVWDUWQw4HndNusBr-b9-RgvHqzv2-QT1tYult_fl-kY-J3Pd0KSE57sEBY4mTMg0TNXKVows_4k3FVgg0PqsWh8bY4iB6Lc7mHYXxOUAMINLxG_THrUxXWvg4o0g-9PofQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای خیابان‌های کربلا در هفتۀ گذشته
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/farsna/443420" target="_blank">📅 15:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443419">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📷
آماده‌سازی محل تدفین شهدای دانش‌آموز جنایت ترامپ در میناب  @Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/443419" target="_blank">📅 15:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443413">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KT59DKqweMlhOrZ-8CGkxqyPU7L1BjX9Kkr7NST4C3q7EY_N9h8ag-EdlhRWfgaEUyXZR0jfh6aBkez-gdFFHu1w4_hpWC0850XlrwnTY2dyZMk1URL-koP_w7v_L4h6fhH7IwY2WoPK4mVx_goKElF7yZoJhG1rtu3AVXEx937POSJAAjsEOj-7HMb7VgwTRTSq7kuOrG6WyqfCgA0soMf8FZ6I39GCWzIgrtwiWMawZfEvhZBZGK7qwiCVCEovCMQhlStOguUDgcC9pxGfZnDITWivHC2tWW_NsCXcgNTHc3PWHuhJIVJTHg0FN1puhVEN4D1dGHd621Xjly7PpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pY0ftORaq2nrA_pWYiVxkGmhKIeuWjmGa-zFfwh9sRhNyRaUz_pFqtKRIG5RYtqmnikd64Qjps0uj966J5jtUe2ob9l2OwGmeP-epBjYwv1uxNnVLctoPyq-76pD9ia5fO7V_1GdnvNjol7UNyvqjs-kr4mDEqqptq_-vnr1HxqSaVLZef8q3a3XwdVhwFoF1mAeYGdlxdhwQMGcKWs2ITAv1OJYAKU2BBS4D-_1nL11VgiIRic9SsoTPvs7ju6XG2CDgU4ZFN88wDqI7ci3FNGRQ_nr1bsskURA6o6yQDVFvRckLEm5kviWu8kbC8AXs4Ko1KwMeMGWDGyTBNnaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u1ksBy5dRbYBiiZESUBWhb3NoNJw1a93yZ72Zx8Nse-ob8A5t2MMGrYGN8ofxlov1Vf5KMCn37qNEd9VzEDHueUAwu8MTlwSdOroGq-qVa3_sSbb7fdnv-IESjE6xD28dt0-6cUiASUAWejPqVV1MKr6z7qV2mL4r-9T9TV0UpOOxTE6DROL5aL9t9I-U0bNE4pLiHwBxr0pG6c-pOdw8AkC3s2NmOp1Dx12Kf1xiJ7VmbnjcQW6kSxcPyA4wgydSa0Og3D8OF69qUMSu2jAkAoI_0dqo3NRLx6fwh8zHd-SFhes_M1pFxyrhGLxnDjrRq4lFZEtHH-Q9fFtoaNhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoXMgXqrcam_3w4RNl6ZoYxMnMBaRl_o8OmIgojxVYl5TVHiyMBfnJ7WW6fcysobXRllP-H4wVeCYFb4ZxbTXBn5B5m1f2RpUd7JfrQ1xGxy0EuenhtNvHTm4yMO9OIwtD23E7ZNDlykSgmOIJQfRuvyrnIujEP3iJoY8gwIzNBL9_BmiaVvqcM-PWB6CKBtOf0MzxzJvr8mHOina7atwYuNlmwY1RMcTQWP71GztemoLFvXMDSWgFIJFfFpn3mqKNqTwZwkT2WcN_EzdeFk2a0UoM724JTjEw4MWZVVRI9Zfp6RIoEIQyAE-9kq8yQpB94ckEtrrgQowwGUUgs4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eq8e9y1XJAVunEpq29NQghD2V2QOL50zylEBR6DFC8QcNLEkRX_Rsd7fkg3CVar3LCBa0cyUoOKPl0qmR6KtFnUj_HWxkRjBEg6dbqRmmxIYkRuDxs0exDHVCibytmmLT4tAm5acfYSWrKxEbf57r2DcIAp-ri03rRHqgVDNScfz3NXB-C_UJUl3Fiu_e79HY57S-Kt8VrivizAQwIn9eyhm9TsUfHFztqQCC2JeUyVmEfqCb6KJeo1r1lxy1Ck7VZNovsp591g0XhrAaW9SDXqFQc6wwlKVjUR5NDyPAwO2pVEbEPhybHFp_RAiYPLWUxVvODANFDQVwKAJ2HTM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgPJEVkR4_3-EgSSS6OwqM9u27byG6I096oCwtssN5ReVa97MLMZnWY-HuHzBxei_iqqBLbRApKntrWaRTwPscESDtFSaojqBBoDUwIUJKDrEki24k8VIeQOYbCHpqGB6x5EjsXNLi3TtN6ippyOs-d28bN7e0yhO9JHccE5j7zAp5As5rUB6nfEfTgboZfFQD2MLGbkMtwUltZW-Gc9DS6WBMtfCJSyc3fiRtbEJv72QRoQHz2XIaS3mNqi-SHsTrMUQKVrV-3H00kbF2TmqVe0mrbf-Kh5cyLhdhUn0BVgn1qYhdSgYCkUHrXSDtzAhJeT8-j-Kc9fim7uXfBF9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جنب‌وجوش فلامینگوهای مهاجر در دریاچهٔ مهارلو
عکس: عرفان سامان‌فر
@Farsna</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/443413" target="_blank">📅 15:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443412">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzKbplZMVKjvm6E39-79T9Wfs2C226SDACLYOuocJb3h5wPXGbPtXPPcW_2iv2JwMU89n8X61cgEbEdqaNujL9v7eMi4A1EhEHzC3XhEOGoT964mWTE8Uv2CQEaHmX_A57HMpBXYpoiD4-Mgk6l5qIY1j8QOZWquyB4wU--lVd7aWNjrx6o23uqrx9Zs_RGzIEk0AM6qruKKD0wT2k3GOGigx7RZfgfzGbsqxLZVz_aNmvjLWsulEh0cX0_Ly0VC9bkpUdOe9ahdcMbDPWUgJrgmSsl0TCgxCa0NT13xTDRQq2dmcMoekUtocHAVWh2d5ZYNexZPQsZviMVN3xDgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بیانیه اتاق عملیات مقاومت اسلامی درباره تحولات اخیر و نقض آتش‌بس
🔹
اتاق عملیات مقاومت اسلامی حزب‌الله در اطلاعیه‌ای گفت: دشمن اسرائیلی بار دیگر با تکیه بر ادعاهای دروغین تلاش می‌کند نقض آتش‌بس را که خود هرگز به آن پایبند نبوده توجیه کند؛ در حالیکه از شب گذشته تاکنون حملات علیه لبنان ادامه دارد.
🔹
مقاومت اسلامی تأکید کرد که از شامگاه جمعه به آتش‌بس پایبند بوده، حتی پس از آنکه دشمن از همان لحظات نخست آن را نقض کرد، اما با توجه به سابقه همیشگی دشمن در پیمان‌شکنی و حیله و فریب، دست خود را بر ماشه نگه داشته است.
🔹
به گفته حزب‌الله، ارتش اسرائیل در شب گذشته اقدام به تلاش برای نفوذ به سمت ارتفاع «علی الطاهر» کرد؛ منطقه‌ای که با وجود تلاش‌های مکرر همجنان از اشغال آن ناتوان مانده است.
🔹
طبق این اطلاعیه، امروز هنگامی که نظامیان تیپ کماندویی ارتش اسرائیل به کمین رزمندگان مقاومت رسیدند،  با انواع سلاح‌های سبک و سنگین مورد هدف قرار گرفتند؛ به طوریکه مقاومت توانست تلفات گسترده‌ای را روی دست دشمن بگذارد.
🔹
حزب‌الله تأکید کرد: مقاومت اسلامی اعلام می‌کند که همزمان با پایبندی به آتش‌بس، در برابر هرگونه تلاش دشمن برای توسعه اشغالگری در خاک لبنان، هیچ‌گونه تسامحی نخواهد داشت و رزمندگان مقاومت در کمین‌های خود در آمادگی کامل به سر می‌برند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/443412" target="_blank">📅 14:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443411">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lG4EymdEQrumHbKRLd18-J7w5bUSPyAWuFIM6krI5wi0R8eEi-PVmlnJz6ZG5jHOIa4GVbU2BhEH_HuLoNJbt4CET6hLJswutlW7SDASt4xj4wNHpjmq-TG3HoVBZ5tshiRJL0ADIEHDXmD17MEORbeeabwqdmP7HMM3SvMlwgGMEqzyJB5dYWhuOIjAtd0tyBliLSYSBiEFkzSobevi6QgbFCQg-FgwxeiPil_VIqDUw4r-jR7Z8Ll9pK9bo-l-NuFfsecUdHWpVsoEJsHHBIHMWX-5L4Jg_jdUWzjGF8DtonlW_6jw1YXOVPVV7NdgLaWuieYYUWwfHZOx52cTiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارز زیارتی اربعین برای هر زائر ۲۰۰ هزار دینار اعلام شد
🔹
براساس دستورالعمل ابلاغی بانک مرکزی در رابطه با تأمین و فروش ارز زیارتی اربعین حسینی‌(ع) در سال ۱۴۰۵، برای هر متقاضی بالای ۵ سال ۲۰۰ هزار دینار عراق در نظر گرفته شده است.
🔹
فروش ارز اربعین توسط تمام بانک‌ها و موسسات اعتباری و صرافی‌های دارای مجوز معتبر انجام عملیات ارزی از تاریخ ۲۰ تیر تا ۱۲ مرداد انجام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/farsna/443411" target="_blank">📅 14:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443405">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FoqApBTUosN18_hWk2jGLrHrb_7NoSh4Qd9lBnsMk9fJWDOtDTtzPI2rHQpcsLjJPUfTXaDyGqH8XFllP4wW93ks3PfUua-84UwwP37tyMjE6unW8b1EnSBoguz6Kzz_9uQl4QvFfXWqG6CYp5XR_cQeqAXsbwEYZVL1wePBHEmFUZy20jGF3phDk0Zex_UHpyzJbV9OXeWIj1oAsUaC__8xQkA4wJW_Vt2Vj7hC-qj8Io2ojf8mhgtRwgCNHuOxsATUxI2yklhA6p_2qNMHymGv5_CmbbS1MzxvyeAApG9U8ghGT6B6zKG4q9GrjSNrv-0HMFJDZccsXS_1MXvRog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvvAYsjN9Ps_rAXjnN4n2gHimc6BlY1AWthb6KPTUjZCyUYtvmakCuFwHkj0k6GUlX2WNJnRT2LRmu_YoIVzB0EvGXr1wDNun-EJhRUlEayV65Z_ub96R9iXjnf8LlEFjDEowXoW7mB8Q3wphO9WQha6CBIFr6VQlI8urW--mGna7f-GglDGe4DQ40M3LjjpyZ4cXW0rTEgxuuaeQiy8gMDp34lGv5F-JpjSMAl8lTTjv_LDxWir_OqIy93iEj0Ah5foxtp3X2HBnPSygleGZ0t28_K3e37eWYiwS8LV71m9C9af15ToWpilpn1hZ7ELJRz0zTJUDaVD4mbj-iAXXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vsOLH7k4rP8qDaSJBZ7RWyDROUZDF5JhFWIeeuwxyvYLIebw5JiSw2Nr534gYmNj8q_dSAhSYjv0SOWdmw5VRfYasVy2HDLrl71Rm_engg5wAIA_4aAwasC6Is4EnzfNlyW7dPMITTxsHZe0EnQS6DItP3gzZNcCEqwArnqlxOptGQ_66WZfaqkiZW5l1YUiibCZb0yoWFDS5k0kpbja7Sm80AlNuaASLTbzZEfwUGiK5kaUeZqiTGi1Od8cMmEs9GA1urIts-bHY7fBogqaTdIFIvUpw0DE9eEszjzqqYhAdjg1nWO9kuXe0im6Feqx-N7h3Tzy-DasbZbmyGKt4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIzw84ghd9VKIrCeUVq2mVlsUDNDSGZazsWU1WHyivu43xfOaKEpMrZzG8HzDr5RvzFRoWh8OTbftY6niFm1WgurhP3Tht7FrXs-0ZljyZRqsjY2vpU03iqjAC6oWHxJR1pHcKQunKZ2Lhvz4oTLUHeK6LGWpa8p6oesw1cWDRCFJz18REWgkPzbtUqIsF0Ozq65VB7E7cCqfXIx6pVP4C87XTRkaYvwMbpiKejYRbv0ouJFucbveKNzTE5WG3AUx1gxO-ILJkN525w09483FC4YCUIlzb1TgqOTRHojtT-DUN7toDqqdpzDDsasRkEi3wXDJW30pDttTEdarxGlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Npm1A-NNHZO0jzzXc_jTHcDKLrR8J3w8yKC_TtU0P0fDcmZqguaTl5I6fXQiNCDWci9NQsAWM5CBrNrH889x9NQT7Ry7uG2he_R3jz3R7D-PyCWViUnRy7rg5_sCP78ggSFSRRdzMyX1YZ2JenJlVsuAHWUUClttC43WX6iUji9AN7b-1Mzcu1-P81QqhtWijydCnD2HdERPUYYp0VSMLkTa8jFP_H5DASfmtSDNLb2N3Or7sscDB5-Qnq_lWzNfYS0d23aRKr-rTYSkqiE9S4AIri4FKizTfJl14qU9I3b3d_F0auvSE2ODGPmlgMDnlJAy91p7dTEdURNLR6RU5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OjHDpsi_rTZ4x9k0e2LFA2kU6hUIFRKKPbRASU4nLwytVuLEwZt9j5DIZCLnVOArnjCfU-R0-agoatWk851UwMh8c_pHnc9Ta3RwMLmVCF4sGqEB3MpUOGoqVr8ARB-RecsCdKtAnx02i0tUOXXLmLlFZvWMgxZDhhQuWepI2hhas5sJk8q3GRCYOdITvTm691Ah2vv3XcHajYkb4AL49KZd7PKCUepA63RxeGEhJ7d-awAaCe7ie3PUoa1LrXZizqUq1MEXuZnB9cyRCZPe51gW8EeOpO4ALH519CIg1zqulQcQ1EvvkNW-h_sIk2xm7nMBLIIgvKkdiO7mNe49cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور عوامل برنامهٔ تلویزیونی کاپیتان در خبرگزاری فارس
عکس:
‌محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/443405" target="_blank">📅 14:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443404">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86958ea936.mp4?token=mbrLzJl8A4t2xwQ5emmQk_3FkVoi7yoE_J5k39Kn0GYtBDeCWjqgq9vHvgvDvR28DuRY26w-cQyq9hRUuloQysZ2_vMBDuPyQSiFhkOczJ-VfxlyTsVZXXwezOKb-b4lvj3b3NIGsKyk-fN1y6u512TxF6uTqNjhXX5aMRn2rCnjtt3yL98adIsO0DLv3NwI2WDAqOXSljT9ZxBn-xxG3trqkUje3DzEIS38ABrhThw76WvdikvY6wFEBzh_38Byb2hpN0-ey_ykf67BV9iWT2ZzhBpKtKnsNG_sSwm-91s1Wh--d40tnVqaxIsxFtyXJ3EqfCl1EWEESPlLm1ot9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86958ea936.mp4?token=mbrLzJl8A4t2xwQ5emmQk_3FkVoi7yoE_J5k39Kn0GYtBDeCWjqgq9vHvgvDvR28DuRY26w-cQyq9hRUuloQysZ2_vMBDuPyQSiFhkOczJ-VfxlyTsVZXXwezOKb-b4lvj3b3NIGsKyk-fN1y6u512TxF6uTqNjhXX5aMRn2rCnjtt3yL98adIsO0DLv3NwI2WDAqOXSljT9ZxBn-xxG3trqkUje3DzEIS38ABrhThw76WvdikvY6wFEBzh_38Byb2hpN0-ey_ykf67BV9iWT2ZzhBpKtKnsNG_sSwm-91s1Wh--d40tnVqaxIsxFtyXJ3EqfCl1EWEESPlLm1ot9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خداحافظی با صورت‌حساب کاغذی
🔹
وزیر اقتصاد: با توجه به آمادگی زیرساخت‌ها، همۀ فعالان اقتصادی باید از اول تیر صورت‌حساب الکترونیکی صادر کنند و دیگر صورتح‌ساب کاغذی اعتباری ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/443404" target="_blank">📅 14:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443403">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1ee46777c.mp4?token=eDjPvAQfRM2Iv-2Kf7qaFtBA4Cf28h8N0zQLvNnABm4MfX-LHkMNl4gs9oKpyzmjj6InEm8ZdpcRlQf4xJE8o-__BHmOZE4kM8jDNvj-x_lFeRft2JSVd6Oaor7iw8fNiX6LzpD7OpnoZ6jNAsxFcOxKaPGDBBhAkPHl76HbgVNQ4OoXTgfrxn8JegrjH9NRTq482jhzHnH_kgK_CLIHDMib16ud203Q75pdch1CGdtgjuVMScMR8eqf3VPY6L24RcKW0cl6tcfXZb7m1TIZswyjjt9lEvOM7sl1QwYhmslr_0ovq4Qrcju75jv-iff0iB_NzRPElwIEIOWl_1Ah8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1ee46777c.mp4?token=eDjPvAQfRM2Iv-2Kf7qaFtBA4Cf28h8N0zQLvNnABm4MfX-LHkMNl4gs9oKpyzmjj6InEm8ZdpcRlQf4xJE8o-__BHmOZE4kM8jDNvj-x_lFeRft2JSVd6Oaor7iw8fNiX6LzpD7OpnoZ6jNAsxFcOxKaPGDBBhAkPHl76HbgVNQ4OoXTgfrxn8JegrjH9NRTq482jhzHnH_kgK_CLIHDMib16ud203Q75pdch1CGdtgjuVMScMR8eqf3VPY6L24RcKW0cl6tcfXZb7m1TIZswyjjt9lEvOM7sl1QwYhmslr_0ovq4Qrcju75jv-iff0iB_NzRPElwIEIOWl_1Ah8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جنایت در شهرک قناریت در جنوب لبنان
🔹
منابع لبنانی از حملات شدید و پیوسته به شهرک قناریت در جنوب این کشور خبر دادند که تا این لحظه به شهادت دست‌کم ۷ نفر و مجروح‌شدن ۱۷ تن دیگر منجر شده است. @Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/443403" target="_blank">📅 14:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443402">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d49524548.mp4?token=Wq9MkHAXePYGN2YcA98Z2FwFehgKpWmsHgbhr5XiF0POXOXsJU2nAOy99L_vl1BccNkgqlJtcl5xnBCm7dyboULgcAosn0UzejCUlYnBgllYehSYBR72rXjoub_Uy-l9RWhTap0alx302asjwIzDpKvDdI7ZFzc7VPsVe6awBFoRNY0S8YPNEW6GE4VXLkCcJNzqSjmuuaZB0gADDeXCzbyAz_s5d-cbpe9oaVTneTQEEEdYo3vVAJeF-qbX-Hvag_INhI9LHiuEoT-NvS651pfNnB5l8K33d0eqGhtshNMP427zvwHI4oNAVCEYm5wuQR_8lRA3HYeO5-N7c1JsdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d49524548.mp4?token=Wq9MkHAXePYGN2YcA98Z2FwFehgKpWmsHgbhr5XiF0POXOXsJU2nAOy99L_vl1BccNkgqlJtcl5xnBCm7dyboULgcAosn0UzejCUlYnBgllYehSYBR72rXjoub_Uy-l9RWhTap0alx302asjwIzDpKvDdI7ZFzc7VPsVe6awBFoRNY0S8YPNEW6GE4VXLkCcJNzqSjmuuaZB0gADDeXCzbyAz_s5d-cbpe9oaVTneTQEEEdYo3vVAJeF-qbX-Hvag_INhI9LHiuEoT-NvS651pfNnB5l8K33d0eqGhtshNMP427zvwHI4oNAVCEYm5wuQR_8lRA3HYeO5-N7c1JsdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نیروی دریایی سپاه: اگر شناورها مسیر دریایی جنوب جزیرۀ لارک را رعایت نکنند، مسئولیت هر اتفاقی با خودشان است
🔹
از برخورد احتمالی با مین تا تصادف‌های دریایی و حتی هدف قرار گرفتن.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/443402" target="_blank">📅 14:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443399">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34d70cf233.mp4?token=d3qIMktKJA7mZOjpzGplh48nGxoIzA-WVDx82FQzccmubgtNp_Ti5MlP0TQRt2742Tin-wHcVw__iWr4RomrO11HLmrjULltdrAllGvBaF-Irfh7cz4NfDp_i7Sbae3ZV1LysucqU4zOSTuIcQqaSy5qtqS0fsD6V0ugCJ9x_TOzdl-8_hT3KdvExOip8zb7WPdLDU5zOKHrZ7Bmkoq8ThprobnL8B6HwSXnm5wkPqhj1AuJjvITGlulDg8LuLoVPrZ6bNj2f3ViF_7QlINvs_FRypFZHd14RZREdcLt77r3nY4VFGmepb0-N9gepkktOBwY7LAgI7HXIZW2dcqBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34d70cf233.mp4?token=d3qIMktKJA7mZOjpzGplh48nGxoIzA-WVDx82FQzccmubgtNp_Ti5MlP0TQRt2742Tin-wHcVw__iWr4RomrO11HLmrjULltdrAllGvBaF-Irfh7cz4NfDp_i7Sbae3ZV1LysucqU4zOSTuIcQqaSy5qtqS0fsD6V0ugCJ9x_TOzdl-8_hT3KdvExOip8zb7WPdLDU5zOKHrZ7Bmkoq8ThprobnL8B6HwSXnm5wkPqhj1AuJjvITGlulDg8LuLoVPrZ6bNj2f3ViF_7QlINvs_FRypFZHd14RZREdcLt77r3nY4VFGmepb0-N9gepkktOBwY7LAgI7HXIZW2dcqBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قاب‌هایی از بمباران‌های وحشیانه در جنوب لبنان از صبح امروز  @Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/443399" target="_blank">📅 14:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443396">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vUxS7Wr1Am4FbtfuGlqHwLkU0Vxq8cR1hZZtqBi3h4S6lKgibk6-JmMRGfqvMO8Wk6f7twjZChEo4Tz6CEaRj-dn8vjkNDpjeivHs-csN0dzYAkanh2Y8c05H4xOOGU_oqO7cydyN92PWvz6mtwq8JWdX1ez47kxNZymXWKGBaTaovagtyonaPIDHQIsAov5B4LGU9L9BSJsSG7qs7D9ezIptvcHXbW88x2WHDcRTiUFE90-e-whZ70wesber4Rgf9kkw9MGU8VCRskKNeb9lvrW_vLNTRLdo64zBmuKDOB9jg_XWQpOJgRczkajDpJAzJxbiHjLauNky_vAocWh3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CWHKwVs3W6blTtIOrphvTyWzlyvk9iqctjtx6MqwHRFVTCz5QYs9QTuQ-JjdrxFIQsOTsy_5b98NzgFJiIsquvIK9wqj0jhINdvHBYpMRH0D8VjirR-QUhszDJNrwFdFNgPYt3mEkkHB3smtffABb5XmK2mR4iwXsFP9NbUpoLq2z-6Z5lPyipjvuVi7MN6Ya_ifIy2nLBDMbRr8oLcU-v8S6nkuT9p6-U7mA2XxM46_aC99MtIxB7cRkreurRNoWRLpdxHcLburLleogAS-Ek7uttJ_3RMANyK1ArPEEbqODaciI9jKsEsi7q9vXkzPICcAllgbry1XOB6y1iK-1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بلوار علوم و فنون به نام سردار شهید امیرعلی حاجی‌زاده</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/443396" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443395">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKs1Krbp50502Bzaoh5dqJzfROHda0G0ht2r11sqBbgSzqcA-iqzC_vixscroZemSvzSVSHnFffJxj6fQVvD_HWDkYae4XaifR_p4eA8oK-EWurSkUcGIfsOgpy1bWYNvhPIzYVQbsP5f0pvQR2hdaVEruYXCQVGAL4vVrkpGvMREv6YMk5qKgM_gCG1bKlzi7sjvzCegm1GOGgR52v3Ua6UvgFnmZ5fSA3zXYaQta3RFqIklJc-UYcuBp68S1THwwCTJ60w-qd9BJfKqPYX0VruAWKyFt4z_pmsGbC21bw1-Edf_0PCyfQyj39k7oNDOeI8XMF3dEjTK16M3i6Hbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سگ هار آمریکا
🔹
کاریکاتور کمال شرف، کاریکاتوریست یمنی، در واکنش به حملات رژیم صهیونیستی به لبنان
@Farsna</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/443395" target="_blank">📅 13:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443394">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4h3F521GeScM19G-bguUVQbLRvUYYGZRsiwA5qkLLCW9ojhYzjhQbpZHNgnsTQ6RjN6oBbNpNv9t7TNWrIFIpAcjFzMq8TYxma7gK3YF5SdDqMYYQbyc0Ny48u4IdMoBg9w9JMw22jB8QpwfrWQpFy0MrEqIel-IAzKZlNlhsRMfZpjLugRNXcwM1tEVNCA_2h64Q3_TJOZEhb9k5_1nqlfM_FBuMTsPa-2ICHqsWQXJdOtS3b9KhyB-iJo9gouLcl-sdoRwczVQmoo8jEAzCoZ7znZ-ZJp-Le8VC7A87RomUaQJdhEMpoRMQEauZ4prMZbcJJgZKOn1BeQEgQeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⬇️
همزمان با پرداخت یارانه اقشار کم‌درآمد انجام شد
✅
واریز پیش از موعد حقوق بازنشستگان کشوری توسط بانک صادرات ایران
🔹
بانک صادرات ایران همزمان با رفع حداکثری محدودیت‌ها در استفاده از برخی سامانه‌های بانکی، رفع نگرانی‌های مالی اقشار مختلف جامعه را در اولویت قرار داد و در گام نخست، نسبت به واریز بدون تاخیر حقوق بازنشستگان و پرداخت یارانه خانوارهای کم‌درآمد اقدام کرد.
🔹
به گزارش روابط‌عمومی بانک صادرات ایران، طی روزهای اخیر و همزمان با بروز برخی اختلال‌ها در شبکه بانکی، اقدامات تخصصی جهت بازگشت فوری خدمات به وضعیت عادی انجام شد و عمده سامانه‌ها در کوتاه‌ترین زمان ممکن در دسترس عموم قرار گرفت.
🔹
از جمله مهم‌ترین اولویت‌های بانک صادرات ایران همزمان با برطرف‌کردن محدودیت‌ها، رفع نگرانی‌‌های مالی اقشار بازنشسته و همچنین دهک‌های کم‌درآمد جامعه بود به نحوی که با وجود اختلال فنی، حقوق بازنشستگان کشوری بدون تاخیر و‌ پیش از موعد پرداخت و یارانه خانوار‌های واجد شرایط نیز واریز شد.
🔹
قربان اسکندری، سرپرست بانک صادرات ایران پیش از این در مراسم امضای تفاهم‌نامه با صندوق بازنشستگی کشوری، بازنشستگان محترم را ارزشمندترین نعمت برای جامعه توصیف و بر رفع دغدغه‌های معیشتی آنها با هدف ارتقای رفاه اجتماعی تاکید کرده بود.
🌐
برای مطالعه متن کامل خبر، لطفا کلیک فرمایید
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/443394" target="_blank">📅 13:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443393">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnPJoasMIt_UyXwlxtMiJ0y428ESxYPIah9l7MYxZamny5DNU5ZGW88PpsC_EH4LrQ_k5mGNlrrZXwAzqgoADzuYZtM4kLrsRpMktc7dVF3oGvo29z8EN6_4dQiNBwAGjCTEkl22Su5kAYeNZLX8qu-S2H8XFPFjkzCA1KOCGIdmIt_jUg686SVx3izBj15RId1TMp5uhWquPFoAk9UP0dtTIJYK9uAn8YtWJIcOQwjRSF_84DmPrySOa0sAUeHUoSEEbFJZWGQU0MT_PkcNdmEeAzvg32DyHsasG34JW_47mt1ja9fgwxWGLqEKj_a3_fe53UbV_L0pWbnQ-QZ0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/443393" target="_blank">📅 13:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443392">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/443392" target="_blank">📅 13:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443391">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuAVnYVfAp9tdOS_WNzrCKhfgW8JqxpwsPLKbzpcm2_y0lDhG7bG2np_07EkBTipSukbck5RP8LAO-s2wuH2QTUGajIqRa-rNGzwgnPUZDFy9PSvYJYVtIoKbMOPj5Rn4MT-BiW1QMjWIDkmF1iMZ3fGQ0G0t1cLoatPT4HZRSx9gMM07QOl87I6odlxHdVh9EBVDCEeweQDzIFwyMPyrsodtsQVU1Z7u_Af5amNNS8jKtzsRKcVuZpXXJYPKBXwQLaVZVWLPGj8CoTKD9oRk6q7ySDT4pEa9aRuCd8WGoH2gg19veokxnuu2YT2jTFhmnpRTCxIFUeeiBPFj0wlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجم آب دریاچهٔ ارومیه ۱۸ برابر شد
🔹
مدیرکل حفاظت محیط‌زیست آذربایجان‌غربی: در آبان سال گذشته، ۲۴۰ میلیون مترمکعب حجم دریاچه و وسعت آن ۴۵۶ کیلومتر مربع بود که مقایسهٔ این آمار با شرایط فعلی، بیانگر افزایش ۱۸ برابری حجم آب و بهبود محسوس وضعیت دریاچه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/443391" target="_blank">📅 13:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443390">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8bda46a9.mp4?token=k9XANros9rtuDNenZr1u1fQHFrZw4Uj7LIRJYnunq9M5zER3eK537DzOtfREQskWuyVbsRkBEgX-s1PVzXVcmmu0S3Ahm-0-xz2sMwxE6v7DLDlTNi6VS-ftnw2WWpSwqKxTAzFt1RB5SBmR2KFzern_PAN3wkJ0GAWpOPPV6cFuJwZTul9khlbfxew_5l0_Qe9cKBseS9fbIIowN7kzER0qzfkOJAkw643J4DvCuY2Ng2D0S8foZ3Ra-EV0ec8qq61vcY7EgRA1Sy4fUnKIicCeFjz4Y2rAKOj1v7BFMDr_JR6rPDhTkDz2eB1pRii8EOWB9A4So2M0mYkLh-97xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8bda46a9.mp4?token=k9XANros9rtuDNenZr1u1fQHFrZw4Uj7LIRJYnunq9M5zER3eK537DzOtfREQskWuyVbsRkBEgX-s1PVzXVcmmu0S3Ahm-0-xz2sMwxE6v7DLDlTNi6VS-ftnw2WWpSwqKxTAzFt1RB5SBmR2KFzern_PAN3wkJ0GAWpOPPV6cFuJwZTul9khlbfxew_5l0_Qe9cKBseS9fbIIowN7kzER0qzfkOJAkw643J4DvCuY2Ng2D0S8foZ3Ra-EV0ec8qq61vcY7EgRA1Sy4fUnKIicCeFjz4Y2rAKOj1v7BFMDr_JR6rPDhTkDz2eB1pRii8EOWB9A4So2M0mYkLh-97xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازداشت ۳ لیدر میدانی و ۱۴ مزدور شبکهٔ خرابکاری دشمن در ایلام
🔹
وزارت اطلاعات: ۳ لیدر به نام‌های «مراد-ع»، «مهدی-ک» و «رضا-ف» از اراذل و اوباش سابقه‌دار شهرهای ایلام، ملکشاهی و سرابله که در کودتای دی‌ماه ۱۴۰۴ با تخریب و آتش‌زدن اموال و اماکن عمومی و تیراندازی، تصویربرداری و نمادسازی امنیت را از مردم گرفته بودند توسط سربازان گمنام امام زمان(عج) بازداشت شدند.
🔹
از لیدرهای بازداشت‌شده ۳ قالب TNT، یک کلاشنیکف و شمار زیادی سلاح سرد کشف و ضبط شد‌.
@Farsna</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/farsna/443390" target="_blank">📅 13:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443389">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18ae351495.mp4?token=Pc3lCsc4Ge6ZUFnesnBTZRChIXAfV7KB4GgIEpoSdwF2Ilu0sOCuvLq1JRuiBbcI_gfyYovZDOZD-3KzpJW8ac6KiAvfTnAwofV6MmkHlSdR1pJIXLkWaok3sDDmDvz5jh2uXT3gcOYfoz-vHLxVoeE0woOJ34BHjKFkQ5_S3ZK6gKyDFyV31xgwUOsRXsN7aE7iCypo0EORpYu5eCcfPu1i_lI58a1I5gG0W2RTgoe3Ah_RWEzXRLMBNxj0rcnC2epGE6gON9Gv-VlITrfDf9YUo295xYPdnfe_cULYQ8SsSakW0UA0fBIJM8dVeJi7_8o6ztF0U9FbkysF75n8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18ae351495.mp4?token=Pc3lCsc4Ge6ZUFnesnBTZRChIXAfV7KB4GgIEpoSdwF2Ilu0sOCuvLq1JRuiBbcI_gfyYovZDOZD-3KzpJW8ac6KiAvfTnAwofV6MmkHlSdR1pJIXLkWaok3sDDmDvz5jh2uXT3gcOYfoz-vHLxVoeE0woOJ34BHjKFkQ5_S3ZK6gKyDFyV31xgwUOsRXsN7aE7iCypo0EORpYu5eCcfPu1i_lI58a1I5gG0W2RTgoe3Ah_RWEzXRLMBNxj0rcnC2epGE6gON9Gv-VlITrfDf9YUo295xYPdnfe_cULYQ8SsSakW0UA0fBIJM8dVeJi7_8o6ztF0U9FbkysF75n8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲ توله یوز هلیا پس از مدتی ناپدیدبودن امروز رخ‌نمایی کردند  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/443389" target="_blank">📅 12:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443388">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWL15VcPl-8p-MsQFy5heSwbkni_4yH2j1u1q3kCTJtNd3ilTkBZuYRFy7b9hyhNpMRPfqXnYP62WKC8NzK6iJPmr-ancuRkxDWusCNJnkBHUA3Dqu64C_2wPFzUy9tH4ITYR6HG3UwUyra-Ng7jXZqr8TZsRyTmIxF--zULh-vJgaQE8j3pa5xMCTVHsde3_Yo0PqBShKAx8niAWQ6fY2V5gafrIa9FX-02PkohEqFnJszQMLQyHh4ia0Pu9FZID-L5cpVnrTS_U95yrL-OVr4j1_QaVnsB1A4eiVEwOvvcD1uuhJ9BpNEcHwaIPlHa8L_xCxFtDGkjqkNJs4fPlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل جدید دریاچۀ ارومیه آغاز شد
🔹
دریاچۀ ارومیه که امسال با افزایش ورودی آب پس از ماه‌ها خشکی، بستر از دست‌رفته خود را پس گرفته بود، اکنون فصل تبخیر آن آغاز شده است.
🔹
عیسی‌پور، مدیر دفتر برنامه‌ریزی و تلفیق ستاد ملی احیای دریاچۀ ارومیه، به فارس گفت که آخرین…</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/443388" target="_blank">📅 12:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443387">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">لیگ برتر ۱۸ تیمی شد
🔹
در جلسۀ امروز هیئت‌رئیسۀ فدراسیون فوتبال تصمیم گرفته شد با نیمه‌تمام اعلام‌کردن لیگ برتر و عدم معرفی قهرمان این فصل، سال آینده مسابقات به‌صورت ۱۸ تیمی برگزار شود.
🔹
دو تیم نخست لیگ دسته اول به‌صورت مستقیم راهی لیگ برتر خواهند شد و تیم سوم این مسابقات نیز از طریق دیدار پلی‌آف برای کسب سهمیه صعود تلاش خواهد کرد.
🔹
طبق این مصوبه قعرنشین فعلی لیگ برتر یعنی مس رفسنجان باید در بازی پلی‌آف بقا به مصاف تیم سوم لیگ یک برود.
🔹
نقل‌وانتقالات تابستانی لیگ از ۳۱ خرداد آغاز می شود و تا ۴ شهریور ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/443387" target="_blank">📅 12:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443386">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRs4UqFYOw1tsdeIAhF8aHXFqYl352jNPOmJ0Rc0y_nxzzp-tSN7oXN3_YUcYIXarSlyvVrhiliGAirsnRsy-z9076keRTmTNc1HbNjzwwvV1dvcOteuPeH96HDBsAlZoxyKFX0toAL7mIHIQxz-AZYZ3bUWNUKI68W62PJ08lTUp0Fmxc1NvAuU-VIkH21ZaPQv3pYht_7LKlgnv9HeO1Pm8fvfgdrE_HQB_d9ANHTVVYyOxyVFOhsiD_4v1H-dTHbVZG0487R1BgnpFpszwYixYbg_igG0RYq2NGyA1siDUtmu_Vkk56qgIjH0kyMW8F2USih-ZW1DcOp8En1Auw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با رشد ۹ هزار واحدی به ۵ میلیون و ۱۶۰ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/443386" target="_blank">📅 12:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443385">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cyAIdypnnRXXdCRnLv-VdBN69s_tm-yKhyWF5POYBXbDZiw4Qlw6JA1LLFhZRhAZrDeBCdhGySGE3oWmaUIEZzGHD0MmN3Y-GynBelXvkZIYGVTWHTRhDVGE_AOCvhtf8XP-YVyMgLP31EuJfEF5tBMA7D0_wvnI1oPuw4w5r2CQZyYNGfCsQiS6qYxcfemYSd8NDL2J5w90PQ9Qb7Xb4X7oGvG003l_ZV-c3hit79dOmPzstabpR3QkzP6k6IxURzJGmGZPj_SP_vdgWbw_hcgTkfJMdYl4Yb6xBEIwdEFmzPbccALqEROokMB2-hBM3I5tJM3DtGlirnFBo0BnZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر کشور پاکستان برای گفت‌وگو در مورد مذاکرات ایران و آمریکا برای چندمین بار در هفته‌های گذشته راهی تهران شد.  @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443385" target="_blank">📅 12:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443384">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch4PsPE8HBUheRqdkSKMOl0QnbT_zq-MygUsil5Zvdh0vA96rdxu8vA1ynm6hfA8Tmkun0yKmIpI7dTwkgERpjwT1uLaWL2f3mk5jMYEjKnE4M83bqKk-U4H3-wGUzfb_FYLoryfK_-8O1iDG-vkopgR4fWmwcVYSC3PuH5bYxSeN82T4_1jXeh3plLatQwtzHIFZvtRwMJcuP-VS8ytrUzkbjaiJDn8vF8jB09CRU4PsFPUTBLC3iLc8OJZzd2PBsJDbv4gmDsR9TxFCWDhecWPbT4yf8UaHpA0uniypii-ZTW_-8EhI6RYN3LQYyRfPezM4bpYLuQeMXEszzDteA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: بنده علی‌الاصول دربارهٔ تفاهم‌نامۀ رئیس‌جمهور ایران و آمریکا نظر دیگری داشتم
🔹
بنده علی‌الاصول [دربارهٔ تفاهم‌نامه] نظر دیگری داشتم ولی از باب تعهّدی که رئیس‌جمهور محترم به‌عنوان رئیس شورای عالی امنیّت ملّی از طرف خود و سایر اعضا در پاسداشت…</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/farsna/443384" target="_blank">📅 12:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443382">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kynJdSzi6CI8Kv3BWgAlVAb4rR-0cc92CXx0bDy19Rpuykpzrqh5FmzZMZuAxBkdX9il60IBa-BIYieYOMASVCoz6_sDtV4JztgPJhKvAEvT8V-I1BGUbMcN0E4J_npDjGqgyhFxCciLjPcUBn-JFMTVLXPbDl-YZAAavTuQbtsBkVTZ-n7uMLeLKlCCO5R2fAq8zxFPf0xikQUFcn-6lHKxJNnFJNXRkaBIy1zKv84vaqpX4h_zpnn9rVBE9-Q8VnlUZKS9Vb-J3PTlAKxskQVUerqX0nG38wrx6ypmBPO_xS_z1MsoWMh6cjDC-MoL9sshrr9-aRFixPxqgtJ7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anq_0joBi53N231kH_ukqTKal6qJBs2MEhyOJ3z3vFZsxo2aE4HpoOKBGzWS_KAJjxaC3D5VTzNTZcBb2ZDTHvFgBT2Dwv9M0wtBUxaYHx2KNERCo1y9OUhxLJl8yEK_-_-mE-Upn-akcAHqoSHz1a5NLI_cB4bqYkdEBbx6_MtIYY579MaaIp3pVHkIBWIGxUeY1DSifHvnCk25noaC_VV_vblmKi_wAUQA_AKJuHk6IxWsScVbA2ymlacp5BaHulXRDvrR2dWaSOLwu9XeFaPnOD3aA6_eL80y4SDFmNCam1mc8ZuMumTfKE9fmWbcWDogv7Mnt3eyZaTUehnKCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاربران خارجی:‌ تنگه هرمز همچنان برگ‌ برنده ایران است
🔹
رئیس جمهور ایالات متحده،‌ دونالد ترامپ ادعا می کند که جنگ، ایران را تضعیف کرده است؛ موضوعی که بسیاری از کاربران در ایکس با آن مخالفت کردند.
🔹
کاربران شبکه های اجتماعی بر قدرت مردمی ایران و تسلط این کشور بر تنگه هرمز به عنوان دو عنصر مهم در پیروزی ایران در برابر آمریکا تاکید می کنند.
🔹
برخی از کاربران آمریکایی با اشاره بر مقاومت مردمی و نظامی ایرانی ها در جنگ با آمریکا تاکید کردند جنگ ترامپ نتوانست کنترل ایرانی ها بر تنگه هرمز را به چالش بکشد و بندهای تفاهم نامه نشان دهنده شکست بزرگ آمریکا در برابر ایران است.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/443382" target="_blank">📅 12:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443380">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWecX2YqgN5YGLaGckJXvD-VauEi9KDM9JO3RJnCjlF9RESjR4yLQqUPCZY0MkKIcFB6mIdC3-EYuvcm44DfFtFcMKpuezRaqBOPBgR5CO0KV8mqHrRydvvn9Jdqc_FLjyL5cf8g0AiMxPcUmF48a3jKOvQEzJmwCefD37l6haIUSqg8J42Ebn8sa63lprLHR7B_fdtk4DVvDtSmD74n227RzUr7jk0RTNJTLCrG_FDCZLWw_gPShVATNMHix2nb0f2iGzWB04jMgqoCcpVU6SYsG8X0-9o3-HZDkYe8ezLoTQaWrspLE1RosJxb0tySbohphiKahgzRkKpNEii5Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
در نشست همکاری پایدار اقتصادی ایران و چین مطرح شد
🔰
سه پیشنهاد مدیرعامل مس ایران برای توسعه همکاری‌های راهبردی با چین
🔻
مدیرعامل شرکت ملی صنایع مس ایران در نشست هم‌اندیشی فعالان اقتصادی با رئیس مجلس، با تأکید بر ضرورت ارتقای همکاری‌های ایران و چین از سطح تجارت به سرمایه‌گذاری مشترک و انتقال فناوری، سه پیشنهاد راهبردی برای توسعه همکاری‌های دو کشور در صنعت مس ارائه کرد.
🔹
نشست «همکاری پایدار اقتصادی ایران و چین» امروز چهارشنبه ۲۷خردادماه با حضور دکتر محمدباقر قالیباف، رئیس مجلس شورای اسلامی و نماینده ویژه در امور چین، سیدمحمد اتابک، وزیر صنعت، معدن و تجارت و جمعی از فعالان اقتصادی برگزار شد.
🔹
در این نشست، دکتر مصطفی فیض، مدیرعامل شرکت ملی صنایع مس ایران، با اشاره به جایگاه چین به‌عنوان بزرگ‌ترین مصرف‌کننده مس جهان و نقش این کشور در توسعه صنایع پیشرفته، بر ظرفیت‌های گسترده همکاری میان دو کشور در زنجیره ارزش مس تأکید کرد.
◀️
ادامه خبر در پایگاه خبری مس‌پرس:
https://mespress.ir/x6R9
@mespress_ir</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/443380" target="_blank">📅 11:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443379">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHKEOzfXW0ah6URqX_dXLRV0SMQTaeRSIi9kzaPK3Ziaj5uCFsYE95oNlbr9Q-81-rU_WRcLKawOjGCqZAGE5PPtQKtr93ulNkQH9NEQ3hxYQeW1E3bBswogwfs9JUTuzbXPcTvnofr4ahaQCBJrnqOfr4OqN7SMTZCWC7fcyZUenePuq80XMv_gyLbd4jPWl2I6OZC-7grEUH4OpETX7XkGxjjBONZ1K7ecL5jSXNlVafGmlON41SgumFsw2El3UcByMsfoR2pHvq_GdKtJ4VMrc0EBeD7UtkmfMS4I8g7gyuCPyBHtcqiaogjEd1ZUrS5DtmK2t8knwor11hqjDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
نمایشگاه پوشاک ایرانی-اسلامی در مشهد
◾️
به مناسبت ماه محرم سدن پوش با همکاری بانوان آلا برگزار می‌کند
📆
تاریخ ۱۹ خرداد تا ۹ تیر
(در روزهای چهارشنبه و پنجشنبه ۳ و ۴ تیرماه به دلیل ایام تاسوعا و عاشورا نمایشگاه تعطیل می‌باشد)
🕙
ساعت:
۱۰ صبح الی ۲۰ شب
📍
آدرس
: مشهد کوهسنگی ۲۸ پلاک ۲۲
◾️
پوشاک زنانه مناسب ماه محرم و اربعین
◾️
پوشاک کودک و نوجوان
◾️
پوشاک مردانه
◾️
محصولات سبک زندگی سالم
📣
تمام سود حاصل از فروش صرف امور فرهنگی و مهدوی می‌شود.
✅
ایران‌تن | رویدادهای پوشاک سدن‌پوش
🆔
@irantan_roydad</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/443379" target="_blank">📅 11:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443378">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/443378" target="_blank">📅 11:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443377">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انهدام کنترل‌شدهٔ مهمات در بندرعباس
🔹
نفیسی، معاون استاندار هرمزگان: در راستای پاک‌سازی و ایمن‌سازی مناطق شهری از پرتابه‌های عمل‌نکردهٔ دشمن، عملیات انفجار کنترل‌شده امروز در مناطقی از بندرعباس انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/443377" target="_blank">📅 11:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443376">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مصوبۀ دولت، رقابت برای ساختمان بهشت را داغ‌تر کرد
🔹
درحالی‌که زمان برگزاری انتخابات شوراها ۲ ماه پس از پایان قطعی جنگ تعیین شده، دولت با اصلاح آیین‌نامۀ انتخاب شهرداران، دایرۀ گزینه‌های شهرداری تهران را افزایش داد.
🔹
با ابلاغ معاون اول رئیس‌جمهور، در اصلاحیۀ جدید، مدیران ارشد دارای مدرک تحصیلی در رشته‌های مهندسی برق، مهندسی مکانیک و پزشکی هم می‌توانند شهردار شوند.
🔸
در مصوبۀ قبلی و با توجه به غیبت این ۳ رشته تحصیلی، افرادی همچون مسعود پزشکیان (رئیس جمهور)، محمدرضا عارف (معاون اول رئیس‌جمهور) و علیرضا زاکانی (شهرداری فعلی تهران) نمی‌توانستند به‌عنوان شهردار تهران فعالیت کنند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/443376" target="_blank">📅 11:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443373">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tg4T0wbBen20x7HRqnUzvi9-wilAnngL68JA5gIdB_FaOL9XSMO4IYpzWoYCCj19M_16kNH9SbLsiuTdjgBsBYsHYjbCHWeanp2CpJhemURFghcgXFfOiv0dR-XdUs2Zge8JggLlSjBOjNzT9bFCabg91A5eTUx7NtaQrlMa7slgB1KyBA8Gb9DqMsyeLDCXe0LoAxJvaJWKrsg0Gt_Nz3jii5-8XenjBAGjBG8VNVtI6ArFhm-IU9A_6K2oU-3qu87IIflpqInGrTKLwX9txF6aFZNKJRAO27nzsuBUN0SfO5Yuhp92GY8EAJN9gjcZhWB59fmbam7gg165-OaNuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OcrmJyHDNZ14-sE_9TIES6bwIsGcpB1axo95XM3fk02sAiRy18FY9fBSl7pyjkLE2TYXyVvZ2QdjKVhYrftu94JMiEbp2HblUPFqOeDHaZPyV_SBsfCvu9odoWnVfgQ-AQchCKX-zBIyWTb9BfYsMqjCLUmf52b4O-GRNWTPZIvdTkPF3QTxrircTmROGCloSPpNtlblDVmVsgbn1Rzmepw-IF4Mc79LXmJL7GYIYZm18LtVl9Zj1x3QUFkxSKxYlSkLUz4NS9V8_VucUqOV1BXR7Y29nYHWJnQeSPuenZJB4B1xDFEQ-fPh2bYZjjnimH7VZZpg0sI1lo2Qd8EWCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dngral8lRnURsP35IsgHkinSqPYGMUxteVjQtimSIAGZ8ny8RLD8nDy-YOX4eAl77olyG3OBj-b8lnrzqws0Xs-BkUrhjbgcNkewbqXujJzvT8ef_Ul3fVH2XrtWIoijreqsoQixOUAXYeoHzgZnSoQiF9zWHPsDBbYxYRJUlKInlN_lB7caUSlpZyK2xDLqxK9ZZE8w-nkUleoezZqGBOk54XLQFuqZeyAEPNGES5k5ZaAUs3CjMdwcQCIhiAymL82wvynvcQyxkdiHRV_EHC4tyDSrOIwhp9C5YTlQ61X5V9bdQp7Q4rbjGKH5FTYnOLOZWcDsXflYMJtcmvwKWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرمانده قرارگاه خاتم‌الانبیا: شهید پاکپور مرد میدان، معمار تحولات عملیاتی و الگوی مدیریت جهادی بود
🔹
سرلشکر خلبان علی عبداللهی در دیدار با خانواده شهید پاکپور، فرمانده فقید کل سپاه: این شهید در بنیان‌گذاری یگان‌های زرهی سپاه، تحول‌آفرینی در نیروی زمینی سپاه، ایجاد امنیت پایدار در شمال‌غرب و جنوب‌شرق نقش بی‌نظیری داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/443373" target="_blank">📅 11:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443372">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OioQASMh_M1KKCbjupngSkR2IUFNLcPsOJxXfJ3CVaPd7GHCLAhV6dgtqVsJ2t7I7XcgnUnOMkGTknBoDpeqGmnWcplWPrEHETncHSkiSz34FJyzQpPMry3-9jSxWrO6wXqm7I_RZJ_h56Sp9ZPaTjfVOvdXV8YUi6XEhMQKaKxtVIse9_y42lzvV5H3Ik51y4p0ISayBMragO7RH00ygM4xw1DOv28GASM4gn4kO2vVQP4b69VD4MGD1Tmg2Bze84MsK9fpTLrXW1QnllH3aZmDUeMQwQtx6-7OSpmrjT0JR-VMmWLRab2BbGYolakTQ6wx8hvlrrF4omh0qATd-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری ۲ مدیر اختلاسگر در سیستان‌وبلوچستان
🔹
دادستان عمومی زاهدان: ۲ مدیر متخلف به‌اتهام اختلاس و رشوه دستگیر شده و از یکی از متهمان ۵۰۰ میلیارد تومان طلا و وجه نقد توقیف شده است؛ به‌محض قطعیت دادنامه، رای صادرشده منتشر خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/443372" target="_blank">📅 11:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443371">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تأیید حکم اخراج لیدر ناآرامی‌های دانشگاه شریف توسط شورای انضباطی
🔹
شورای انضباطی تجدیدنظر دانشگاه صنعتی شریف حکم اخراج رضا دالمن را تأیید کرد. وی در جریان ناآرامی‌های دی‌ماه به نقش‌آفرینی در تجمعات غیرقانونی و ایجاد التهاب در فضای دانشگاه متهم شده است.
🔹
براساس…</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/443371" target="_blank">📅 11:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443370">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT8ATh_Ky_MqZOqFp6XP4pOYa0yBE0Zr2dXPVCKjTK1PFDQqcPh8mi1axz_3kTGWMTooZ7JMsR3j-3FgHdLjcI6PLfcDMQIeeDUrTN08DOM24hoJPA-u3PAipy1OYd0JVNw7p6_nlAd6LPjyORoEid3jfnAqwKpZR_2OXXH4ftc3pR3GYplGfBVFkgMrt4GkN9M2nyicLUMPl6okNEWQBnsMwNxPe5mkHfqf2GUpkDs_aPjs76HcFx3YeMDJ1SgwakDpUIHR0bPc-eeNOd6wLvkFwTUgOwjLwva8DYgtkiVS5886sY7OA1ZJ1s9f8DhoAaGN3zanbYkcS3TdWTWzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قاب هولناک جنایت میناب، برندۀ جایزۀ بهترین عکس سال جهان شد
🔹
مرتضی آخوندی عکاس ایرانی موفق شد در رقابتی بین‌المللی و در میان صدها اثر از عکاسان سراسر جهان، مقام نخست بخش «عکاسی خبری» مسابقه Golden Shot Photography Awards 2026 را از آن خود کند؛ آن هم با عکسی از مراسم تشییع و تدفین شهدای دانش‌آموز میناب.
🔹
این موفقیت با ثبت و ارائۀ تصویری هوایی از مراسم تشییع و خاکسپاری ۱۶۸ دانش‌آموز شهید میناب رقم خورد؛ عکسی که توجه داوران و مخاطبان جهانی را به خود جلب کرد و بازتاب گسترده‌ای در محافل رسانه‌ای و هنری جهان داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/443370" target="_blank">📅 11:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443369">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54bea1b4a2.mp4?token=Ud3Z7oFD-ff_y8PQsyftCGLPqlj8JhsbqcZYisRhohAC5nxV3E7qSfB28gvwR2aRhFqjv11xwVc0GF4N29C8ji6jQUcrUottzDIKN-y18ESy9B2tNYYuqxltvCNHgwzU_vGo2Ce_ot21IrctzxSt7_zmdGLST_eO2sHLX_qm_PfhKwusaHTIYAk10tBzAj0UyfNNXO7gBwTC3fyKE3iHsFQc6gXU8r5E8uSYPp12Qo8wB88mhfWwoHyvfC6n3Bp38pa72JrTYfSCCwcC-5g_Pb2zqy9t3N9BgezlFalNcZOiNlBwDMCqrwnO2UVckA6krTaSCzXFfrSI152pZsYHHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54bea1b4a2.mp4?token=Ud3Z7oFD-ff_y8PQsyftCGLPqlj8JhsbqcZYisRhohAC5nxV3E7qSfB28gvwR2aRhFqjv11xwVc0GF4N29C8ji6jQUcrUottzDIKN-y18ESy9B2tNYYuqxltvCNHgwzU_vGo2Ce_ot21IrctzxSt7_zmdGLST_eO2sHLX_qm_PfhKwusaHTIYAk10tBzAj0UyfNNXO7gBwTC3fyKE3iHsFQc6gXU8r5E8uSYPp12Qo8wB88mhfWwoHyvfC6n3Bp38pa72JrTYfSCCwcC-5g_Pb2zqy9t3N9BgezlFalNcZOiNlBwDMCqrwnO2UVckA6krTaSCzXFfrSI152pZsYHHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت کشور: همزمانی انتخابات شورا با مجلس ممکن نیست
🔹
قاعدتا چون مجلس ناظر انتخابات شوراهاست، باید مجلس مستقر باشد تا بتواند بر انتخابات نظارت کند. به‌لحاظ حقوقی، همزمانی انتخابات شورا با مجلس ممکن نیست.
🔹
انتخابات مجلس اواخر سال ۱۴۰۶ و انتخابات ریاست جمهوری اوایل سال ۱۴۰۷ برگزار می‌شود.
🔹
تلاش می‌کنیم تا سازوکارهای قانونی آن را فراهم کنیم و موانع قانونی را برطرف کنیم تا امکان تجمیع انتخابات مجلس با ریاست جمهوری وجود داشته باشد.
🔹
البته این موانع قانونی باید رفع شوند، اما بنا داریم انتخابات شوراها را در همین سال برگزار کنیم تا تداخلی با انتخابات مجلس نداشته باشد.
@Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/443369" target="_blank">📅 11:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443368">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">وزیر کشور پاکستان برای گفت‌وگو در مورد مذاکرات ایران و آمریکا برای چندمین بار در هفته‌های گذشته راهی تهران شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/443368" target="_blank">📅 10:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443364">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDV6zvk1nSjuqRi7kOgwRIgtZ4Jc8aJfmWR0mI5Lnjdfhr1PLHwaNndsAyScNMV2gdBWgRNhbfnPB8KI9xSkED7gs4fnjlzW-8-i1bgCkYDicmIzYE_uJon4ITuQGw5UbSuaY9RmwMQ9FazyHYBktXf3iABQUu0BkDP0nn_5yk19oD2Oe-DUZwZ6EfqmOASWTHey6a_q79QwUcsXhL8Q37z9XJg_tZdDynfodOC-0xpo2iXPZMJYePgv9GpXNiHw1rBKe7K8ISrKmXnSLfP6dPPLtqHMPdKnSzl3acIPJrGwzPmiDWXFcfWT5wKSja7e0_qzuB86OZ8i8IlFKDEhtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MddVEKD3C_ICoAJx0qk_-L5Dbm2vzxzCLjJh60F9z5GL5Me4FcMysijMsaN_ahtSLdlVejIg23KUH8tzHfAvjpyycE_3dEoSd5nE_bQRZbJRrcEW0F7wdkFrogySRrk_CqsWq4PasDSkXoIFjk-9_6-lzm56Fa81PLxsHz5X43Nr7EmicETmAbAOQmVx-Bu-8dlH5Fv-f1UESndc3hJu6gKpAmec_jFYrvcpSLMJuJi3sI3T1HAZWS9TC-TnpumPZygB6LMSPDGF1hmXIYPjlnYEglPWwfzwcAXZonHXd4TZRo53Ot6rnue6hsgUR-0XL_dLi61bYwyRMl9X_drmcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T2cDim3w5NwHsDPe2FodfUZRmxD9X70sdAHZvK3nadftOcxbb1hhPuJMsaQUcEBDz6g5g7ktR9-dFksTGiviXCXoEdxADM31mUxcEcrucU3nwxdY4sMwTk5lmRvxf9aVzu_FQNnVSAFTsxFm9mYuhNAYBR3Ru2FDHj_1p_5CAJMj-qPOrcufZ7mqR2uLqiITttkdkaGtkU4tJmhrN7ppPEkf9TYnVfKaUWNWIjNHTEHqMEzebivvzaSmQ5887MFnKirH_N5YuHXbUsVGsyHSyR_PQRCPsgEwAoOX4g9H26JSBLPtNqiWccNhXcfEVHG-Rm09wikgsGesGGqmzqiv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ap5Am2JiQlk3B-qCRtJSnYnAXBbNQCDY-UON9-S-W34lEwxa9lAJ_uypbf2XEoHJMgJEJ1oELhspHDhnneVbDYIsEEx8qOMjnVgL8Jlpac0c63eY2TeR8STjw_NPWLncWaz8o4QCfStlubHmQW-egC6Ah95P2Q3XunnxX0kC24gS3pJXPlhygO3YtJHUIEQi5w3DgI4InG8U11gdIhd3upgHey32nCCSoH7uVa5sJM466Hpol98JdQW7rRE1shLqLaYKnF1TJinvOSPNHHczP53xMoa-sSMFTW9p76GDtwa6e5rOAzxEldor34KwxTolbjT_n_dm3DFm_QbnS5Sa7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: حل مسائل مردم مهم‌ترین راهبرد پیشگیری از آسیب‌های اجتماعی است
🔹
در نشست هماهنگی ظرفیت‌های مردمی و مدیریت شهری در الگوی حکمرانی محله محور، سازوکارهای هم‌افزایی میان مدیریت شهری، نهادهای مردمی و شبکه‌های اجتماعی محلی به‌منظور شناسایی دقیق مسائل و نیازهای محلات، احصای ظرفیت‌های موجود، اولویت‌بندی چالش‌ها و طراحی راهکارهای اجرایی برای رفع مشکلات مورد بررسی قرار گرفت.
🔹
رئیس‌جمهور: پس از استقرار و موفقیت این مدل در تهران و برخی مناطق آزمایشی، نتایج و تجربیات آن در نشست‌های استانداران، فرمانداران و سایر مدیران اجرایی کشور ارائه و زمینۀ تعمیم آن به سراسر کشور فراهم خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443364" target="_blank">📅 10:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443363">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده در در محدودهٔ صف، بهارستان و اطراف آن تا ساعت ۱۴ امروز، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/443363" target="_blank">📅 10:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443361">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa5c80958.mp4?token=A3qn0aFG5pE7tRktP6eZp1Emo7abkpniN-FQYMYkHfoaQ63BQYqQ900m8ypKDQr0Hb7aXMBCV4ap_0VJnr-vw30AdphotkR07GEkgND4QrQcIKnzxkmRqs1AI6NLrlSlsxyB11tR215nIKQ8B4pE0Wnfi_LeTugxBCS8O3ibVp3FRHeIGpuieUvKuq_a7pT0gd4EaNBO-fmAVYUFg5KkfcfzFFqgxoG4tbpiKKy04SvjjHiHDSojCLzXKJ7ZHIHVLdSVbv2wPFvlVx-rBuYlbDSRu_eFi9w71JNuKlIQ7OsxsCshAsA39VmOuG1mLuoH7I-dtzQIHfqp_fWop3Mhtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa5c80958.mp4?token=A3qn0aFG5pE7tRktP6eZp1Emo7abkpniN-FQYMYkHfoaQ63BQYqQ900m8ypKDQr0Hb7aXMBCV4ap_0VJnr-vw30AdphotkR07GEkgND4QrQcIKnzxkmRqs1AI6NLrlSlsxyB11tR215nIKQ8B4pE0Wnfi_LeTugxBCS8O3ibVp3FRHeIGpuieUvKuq_a7pT0gd4EaNBO-fmAVYUFg5KkfcfzFFqgxoG4tbpiKKy04SvjjHiHDSojCLzXKJ7ZHIHVLdSVbv2wPFvlVx-rBuYlbDSRu_eFi9w71JNuKlIQ7OsxsCshAsA39VmOuG1mLuoH7I-dtzQIHfqp_fWop3Mhtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
قاب‌هایی از بمباران‌های وحشیانه در جنوب لبنان از صبح امروز  @Farsna</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/443361" target="_blank">📅 10:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443360">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTO9Ul6wva9LgRnDKKnGAXQHArcUogaWkDkAcwjaB_M8iPvCSpuv9slBijLKufncVN3lR8GZtrA_We0Ct0AWpbktTxo1Alh62Ay-AtR0KnM0NUcCQIhwgcDUlhuVYCyRBrprGeVOUo7mbW0G8taAabizUR4_gfnXBrTKYWlMlX8rHJ0OlK05GRSf73EvyFCks86Sb5BJxCBAg5CNB2Z-zVoyui8rLqQEj9SBFFs1CiSxeOmFLMSgag3yOiOAabGDz8jNeuvhLPclqzOsKNHIY5LrzXaHQ1p48DFjmwgMQEsBxPtewY94VmGKs6car3JP1ozDtCV13b9AVSiYHsOtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصاویری از بمباران‌های وحشیانه و پیاپی رژیم صهیونیستی در جنوب لبنان از صبح امروز  @Farsna</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/443360" target="_blank">📅 10:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443359">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVZcp1CsQoWvkXmWjfWxW_9wIVZSU5GbYqd59JkA29XDWS-Lzgck6m5NX4xia_2fgHHvRdMyTaRNn9vjT4wwQgvpzUdXBAqVqJqR1gdClmobcnaMnY3t4fC7ciweF6d92cvl2EJw9b94htZQ8Ssyqr2FjCXKbtDpQuMhVUu4PQKj9iarmZP0I3XrqpaglLm5hwFantDwKFoYAq2NcanxLpcOkECkSfoQKxRZhGkfcKOW8L5KJSPaH8ON-LZV4CtE4SdPUHjzd5NSKHPt_AFunH6dfcoDqCUMJLd7ZipeFgqIjnDSiRFaUE5BiC3r9-2uwlf3xtGbK2ygrZz-ldxkRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر صمت مهمان جلسۀ وبیناری مجلس با محوریت خودرو
🔹
سلیمی، عضو هیئت‌رئیسۀ مجلس: وزیر صمت فردا مهمان جلسۀ وبیناری صحن علنی مجلس خواهد بود.
🔹
محور اصلی گفت‌وگو پیرامون مسائل حوزه تولید خودرو، ارتقای کیفیت محصولات داخلی و نحوه حمایت از کارخانه‌هایی است که در این بخش متحمل آسیب شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/443359" target="_blank">📅 10:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443356">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SDRsKWLylwSokEDAze0hrwnvH268KYpOn3pzijTENpACm2pWZtyPXF2x4lbsLvfBvhA68awgwvM9XlUzGGD8uieNMXc2sKj9CQIq4o9m3cV8tTksDABAn7yqQrVVzln2uzpqTNz09fYrda91hbTm_zTIcVrbLAtVlQKo8cfpsmnPV2Wrnie-XKaOJcnOQpMmRq8OMTf5FsZNSt-_F8sYLH1U90Is58OopYCbvM2tVoIUY48BfxgXo2OIo7pF9HzUAWuThFnxXmwwmRLppRwpzNuHeFbnQZDJDnq4Dg5zJTXf8LX12vUP0xqrJCm6UojRbst4RdNBvK3_MFI4h4er-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mRlBbmnYD4VdB5CPHTq0Adaexv7uWxaKQUNdT-SOoiKzrZoTbqWwW3LnW1kq8wDk7a8dogNiIWEnhvfx9LQTOAvRCyRNpydZiMl_SPgXQSLCD55KTIy4st-LFD-GkozVl9NyFqtRW8IScH0pdEIRarEH7FYlW8cZ2UvU-y1fDQmk83dreqv1WuRltvDrWs8eLFwWlXHGI7AuczchrSGqYSrjl_qTvpocP2eFspY-UzqgvjxeXkNnxq6owZ_7jCJaruqo9ngzFIo7yAzGknLCX3jDradHYiNI25CwBjZ4E-jk5X5LK72ZwA1GEaa27H6geiDRR9tulljjJQBiiAszfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZjNqAg9GImBTqrdZ-GX1JPZ_xVZkxQDoar_-NmH8e8kQo5VtIAShOY_l0A5oTw_8ItrBSx8UFAbJXtgjKKM9_0bHx0S-owS9on7-rd5fR0rzWHaGWaXF84d5Z4P7eCeQJmAqJFPJ19nOIcWJSTJsU-pCQhFH9v6OgpJpNwuFmHWcpgTAkmWpivP0qMn9GIDvEyOgfhqglgmhokEndOtR3LvxovlmGTr3O1JCFGXO8tBqIoC1tzY1VSgJ5HvXDWiNuWlElZwwtHuXR50XuVfjmAfg-4dGEDp9sJEC9QrE4pBid5gvx7Rcv2FNOBz_-RCXatmwZnT5plSYJ_AQD92uQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خاتمه فوری و دائمی عملیات‌های نظامی را در تمامی جبهه‌ها، از جمله در لبنان</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443356" target="_blank">📅 09:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443355">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJObbCqeSFgNWp2rmvs9DqT2bitBlPJlEi6yjTM6fwNKhF2Sn3AYU7DjaidcipIA-RPongAQwHO-B-88cweEEX-rSSOnAiDaFeet6Nz-AUcbeWx7FsPVxFWkesplIqr7MEPWn4s4qk2nu9Ep8r6KPpkhS1mFzBCObto3Sqhq8lKVZJ8c2dOPV72WK859PQsV9zaCnJGy5e6X_B82iUo1my-P4BFnX0kAlXZMitLbsgxnbOjlhNckyVukVKM3Fi00UoW5uXFPGCubsvcgCxLDr0t_olsyOxo-wQf9Z5PD4MIhFuGS4LZb635aVzOTLE6TVgm3v4ZaQJDPxE8lpx4mVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
الجزیره از ۴ حملهٔ هوایی رژیم صهیونیستی به شهر النبطیه و شهرک النبطیه الفوقه در جنوب لبنان خبر داد.
🔹
المیادین هم از حملهٔ هوایی اسرائیل به شهرستان صور خبر داد.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443355" target="_blank">📅 09:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443354">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BovpOjxoj2sgWQCmxSZ5mZs8lqGyc-2d7mKNI8JrnQLPv8gsb1h7CNaa-X5JBxZaC9GPJrVnGg-cLK2jXEsO16UbW37lZV9BdAtW71K8DZOODVnIRwzwVgtbedqBGIifxhgH_dx8youM5fyw0VX1cB-HKTU4Avodx1aC8GsdRpDQT5H62m_GeNh6mURmcXkffpDpOx1c4aYjIJRGb2h21JHUsn-FIw9bqKTxPYRirCB0BtzUIkYJcWpzNaL8Uw_zIrMiXTLlFLDWmwOp2mS99gE426M9dUSXvsqDvsXiWepF9pyju3VFS71FgWAt995iIuqRMSR6sCu3jb0IJww78w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور اینفانتینو در رختکن ایران و تمجید از عملکرد بازیکنان
🔹
قلعه‌نویی: به‌خاطر شرایطی که برای ما درست کردند، ما مظلوم‌ترین تیم جام جهانی هستیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443354" target="_blank">📅 09:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443353">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad273a0bf.mp4?token=szaNjj_FnED6LnZSdhbabD3SItuC1ZKbZshB4foT3ob8SYuFd-xP9Hh_mURQHP6t8pRxHiMa11UYRV1AQ0wC_7rEx4RoKVX4I-Yqd8MOWWSe_0Ie0iZD0HixFxzQShI6EppNgA5rWokd3GRBiCDZzrm1bJ7Swv3cgPiD05QebIXbPOqNt48C0lGe94gmHcKQndu9c_WvovbX_mwSvv2kamzu9_MjNxfBSN6ZXu9Jk8PH1RCVoWq9cLF7uH_0NIVcMtROL4MU_LlTKVxuffcNrt7aHDJYtdbwrpLg-Ty7yIm39Sk5ymGpqbpcHn7DqISfGV29BPrvHT5Xk9pZ4Cd5bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad273a0bf.mp4?token=szaNjj_FnED6LnZSdhbabD3SItuC1ZKbZshB4foT3ob8SYuFd-xP9Hh_mURQHP6t8pRxHiMa11UYRV1AQ0wC_7rEx4RoKVX4I-Yqd8MOWWSe_0Ie0iZD0HixFxzQShI6EppNgA5rWokd3GRBiCDZzrm1bJ7Swv3cgPiD05QebIXbPOqNt48C0lGe94gmHcKQndu9c_WvovbX_mwSvv2kamzu9_MjNxfBSN6ZXu9Jk8PH1RCVoWq9cLF7uH_0NIVcMtROL4MU_LlTKVxuffcNrt7aHDJYtdbwrpLg-Ty7yIm39Sk5ymGpqbpcHn7DqISfGV29BPrvHT5Xk9pZ4Cd5bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آزادراه شهید شوشتری چطور شرق تهران را از ترافیک نجات می‌دهد؟
🔹
رئیس کمیته عمران شورای شهر تهران: آزادراه شهید شوشتری که به بزرگراه شهید یاسینی منتهی می‌شود، می‌تواند حدود ۳۰ درصد از ترافیک بزرگراه بسیج و بخشی از بار ترافیکی شرق تهران را کاهش دهد.
🔹
پس‌از…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443353" target="_blank">📅 09:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443352">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f8e3c743.mp4?token=J0QHPteLCG44xpT3QmdfOHFY-_MDTZEO4AdQMYDMV_Msn94SWaOlMPw4YYok-oNO07EuQLzfDVunG645tkkaIxvwP3tfzNPnNbTkJPrgA7hGfUqfAkDOHOZ-xaTg3eS2dJl6mF-9J0Wba_1JKuHh5Z06hi5eCfBr3L0VTrgtNoSxc79IqpXzIinIb8VSfkkYN21gtHGqEqPnBrTW5gsMUWGvyeoP2hVDaw4UoBxlF1-0Fv454hbk3zoclXDLk6E6AfxaaNXPRBVx7wq6OpgpSXUBRQ9_msd-rfcZ8WXUgntu3_tTkOPuzCg16ZGtuIZkvvbJ8xgg72Hj3e3H69PNPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f8e3c743.mp4?token=J0QHPteLCG44xpT3QmdfOHFY-_MDTZEO4AdQMYDMV_Msn94SWaOlMPw4YYok-oNO07EuQLzfDVunG645tkkaIxvwP3tfzNPnNbTkJPrgA7hGfUqfAkDOHOZ-xaTg3eS2dJl6mF-9J0Wba_1JKuHh5Z06hi5eCfBr3L0VTrgtNoSxc79IqpXzIinIb8VSfkkYN21gtHGqEqPnBrTW5gsMUWGvyeoP2hVDaw4UoBxlF1-0Fv454hbk3zoclXDLk6E6AfxaaNXPRBVx7wq6OpgpSXUBRQ9_msd-rfcZ8WXUgntu3_tTkOPuzCg16ZGtuIZkvvbJ8xgg72Hj3e3H69PNPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روز گل‌های زودهنگام؛ پاراگوئه در دقیقۀ یک به گل رسید
⚽️
پاراگوئه ۱ - ۰ ترکیه @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/443352" target="_blank">📅 08:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443351">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqxaShaEA1ALKm3fAyZ6qKvArwNYTuqS2b8w0NUph-BgTauZDOMT2nODBEfbg0c07TvheMVjEC9wLu8Z2fGLQsdtIB9Uf7eTooc0XwNzA9zWMn6DHnO9a_YPXSlAOuh44LRf2qU6Gn60pkuj4iZM2cu0p9wu9xZF8u3hZy_Ml1TSmPYHHOQK-wfjqG1-2b9Beu0rfIQyfzlM38EH6nZa4fULVIPpiOUimB4CBj_iUyQi7IWMAcesColLC4c3tJ-d7gprhyuVXXML6U_w1cOAxA0FIy7oSqosH0MMkXD99AITEyu59fF_eFbIKfwB8vKGzGtP2vq0hrp509u02mQdHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سارقان مسلح تانکرهای سوخت دستگیر شدند
🔹
دادستانی سیستان‌وبلوچستان از دستگیری ۴ عامل سرقت مسلحانه از تانکرهای سوخت در این استان خبر داد‌.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443351" target="_blank">📅 08:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443350">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJQkXV1JHPWOZ7eAeIy6aY31C1pgddM8AYJZ95IzeSRjvRx8NUvOE2KwCIm_nW8-UeoEaBeZr-lLiA2Oj3RXAboC8boh-poungLJox4UXs0fb-Aqd82-uSeVp1E05Tz1amYmq9kpAG1YQxm355Oskbq9hoTCZR-2IEzciM2QN13OFxxhAJtGmxSEAACqh-l-VrkAQBMsfnlc-A1evYGObci4clDQ20uHCyfYg06orGfEt9uw_ndDVu0KV_hIWoyEqK6fKawygNDtUsAijWvP4oZnMjZpF7yvlY7y1UCvcjUYt8vIYomPKHagEj0V-Rk1nI6GyBYJi0McBTUHwyVWhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روستایی‌ها تولیدکنندۀ برق شدند
🔹
با تسهیلات بسیج سازندگی، سال گذشته ۱۸ هزار و ۵۰۰ پنل خورشیدی در مناطق روستایی نصب شد تا هم برق خانوار و بخشی از شبکۀ کشور تأمین شود، هم از محل فروش برق تولیدی، درآمدی برای خانوارها ایجاد گردد.
🔹
بازپرداخت این تسهیلات ۵ ساله و از محل فروش برق تولیدی تأمین می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/443350" target="_blank">📅 07:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443349">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEu6rIpnbEY02NYsYycdsvUq1s_kKSxZ1llDw1C66Ss87H95MaifP_MEyd3VP2gVst43hHnjO_1EBFwZ-_i3d3N6x7k-EErRE4FxL2fUcCPWZR49MlHlOjnQdxCpAx4hJSs8Bxfmy-mPCysY_YEu84bz1muMw-2P7BrglqCKqthWgP9LGV2-gbVuTwaza2V85CLZzvh_Gg3iCM2XZ-6DcwkCESeghr3-4DAnGDDijW_ZryygbWd7QziWk1tATszlKt1d_j0_j5cs5DaYTl4XWxqTTFJ4NyPVXlX7rJkWIptvTSP_0CRsZDvxhfNlem8oN5GfrHTGmg2xhdy7m8VyOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتایج آزمون سمپاد کی اعلام می‌شود؟
🔹
به گفتۀ مسئولان برگزار کننده، نتایج آزمون ورودی مدارس سمپاد اوایل مردادماه اعلام می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/443349" target="_blank">📅 07:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443348">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9f07b3fe1.mp4?token=MB66qQgN74kKzAgzTRynl2tbZ6sUgtj5jvh5rdeePEqKGvvrr7vb--9M9Sppdql2BVrusSJ8X4wlUKEHyAqN4lsPOxCJaS3zw5iYms0Hn24YxfBYRwwFRtlySK1e3qHhuZSCK-ghJq1rYy0HdYi52Usy8Hb9C8oXYglnHfTEpcy86rCGfkFlo-blN9g3kzPvvLQ-tOMtYAKwEuwjwzsAAe9ur6ZpiWoqvrSeCPz7BWzB-B7-vRDnwvJdNxRkcW2gx00JBRwNnQM4-2ewmGGzyZHIbH1Pv9m0MqG_MVtQJIiBzXqlxxxtZ8nGIT-A7uTS076k5aOUjJVlUKuK5sGBUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9f07b3fe1.mp4?token=MB66qQgN74kKzAgzTRynl2tbZ6sUgtj5jvh5rdeePEqKGvvrr7vb--9M9Sppdql2BVrusSJ8X4wlUKEHyAqN4lsPOxCJaS3zw5iYms0Hn24YxfBYRwwFRtlySK1e3qHhuZSCK-ghJq1rYy0HdYi52Usy8Hb9C8oXYglnHfTEpcy86rCGfkFlo-blN9g3kzPvvLQ-tOMtYAKwEuwjwzsAAe9ur6ZpiWoqvrSeCPz7BWzB-B7-vRDnwvJdNxRkcW2gx00JBRwNnQM4-2ewmGGzyZHIbH1Pv9m0MqG_MVtQJIiBzXqlxxxtZ8nGIT-A7uTS076k5aOUjJVlUKuK5sGBUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قانون وینیسیوس قربانی گرفت؛ پاراگوئه قربانی قانون جدید فیفا
⚽️
میگل آلمیرون، بازیکن پاراگوئه به‌دلیل مخفی‌کردن دهان خود هنگام صحبت با حریف، از زمین مسابقه اخراج شد. داور پس از بازبینی با VAR این تصمیم را گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443348" target="_blank">📅 07:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443347">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پیش‌بینی بارش باران در استان‌های ساحلی خزر، و آسمان صاف برای سایر مناطق کشور
🔹
هواشناسی: در پنج روز آینده در ارتفاعات استان‌های ساحلی خزر بارش پراکنده پیش‌بینی می‌شود. در سایر نقاط کشور در طی این مدت پدیدۀ بارشی نخواهیم داشت.
🔹
همچنین در پنج روز آینده در شمال‌شرق و شرق کشور و دامنه‌های جنوبی البرز شرقی، در برخی ساعات وزش‌باد شدید و گاهی گردوخاک پیش‌بینی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/443347" target="_blank">📅 07:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443346">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljLvDZ6m1xTel2HlkPUMHfKSEkvGIWH4t-JR4Wb5i8_eCdqC-MSs6YE12mLAwa5m_ij2U-K2cUIN3pyUEolLoq8N_cqp9MsLpnCD7aUzPefQjMkK72BYf3IfhIb2uzPgmxjKwpY_3Aoqhum-cq_AXyL0FYP59IXxkE_leeEK4V0VSb7MaP9MzS8C9d9vypHT02QXjUeNYKMNhDJqtGrATJNmn_CtMOhP8TdC6Rn85fbzVr7HrtxkWNjCrMWgf5iw4inVn9vC1yEX-211LIAb8cQ73fhNU40gl84KHM4PvzvfIJtDyEgZeTMa5SPWvaOI3nyS9tru-M8ZdP-wmrSpOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لشکری که هر روز بزرگ‌تر می‌شد
🔹
چهارمین روز محرم فرا رسید. ۲ روز از ورود کاروان امام حسین(ع) به کربلا می‌گذشت و حالا نشانه‌های یک محاصرهٔ بزرگ آشکارتر از همیشه بود.
🔹
در اردوگاه کوفه، عمر بن سعد مشغول سازمان‌دهی نیروهای تازه‌وارد بود. از کوفه پیوسته گروه‌های…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/443346" target="_blank">📅 07:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443345">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71790d2667.mp4?token=ujiuYHZgRLq-BC6PLLjWPgS1qCSNOVG4ebRq3_8DtvP6a7_cQOVCLMFpndgkA_DfHWFyIKW89ssEym3pbfOSa-t-5NO7x693yWgL48KExuyu1sn5-qM7fIjfSoQijhsmhxf75N318BzamwU6gBWO5I9cgmT8gEDZS9OsqqpdiWOhIRErIzEFUdlpwBXFoADEVr1bUFvyE-B8WorgxH6XNTVjq3Y7_68IbNCEt8r5SbLvq3-qqoc4CSic8eVL4scNoDMVWKOEb29NnKFMy4TDnbtt5veOwB_94DQTFUAteIBvvqKupn2_n2eBE1kbRUqefmLolCn4_7FdqaMnLLhtsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71790d2667.mp4?token=ujiuYHZgRLq-BC6PLLjWPgS1qCSNOVG4ebRq3_8DtvP6a7_cQOVCLMFpndgkA_DfHWFyIKW89ssEym3pbfOSa-t-5NO7x693yWgL48KExuyu1sn5-qM7fIjfSoQijhsmhxf75N318BzamwU6gBWO5I9cgmT8gEDZS9OsqqpdiWOhIRErIzEFUdlpwBXFoADEVr1bUFvyE-B8WorgxH6XNTVjq3Y7_68IbNCEt8r5SbLvq3-qqoc4CSic8eVL4scNoDMVWKOEb29NnKFMy4TDnbtt5veOwB_94DQTFUAteIBvvqKupn2_n2eBE1kbRUqefmLolCn4_7FdqaMnLLhtsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روز گل‌های زودهنگام؛ پاراگوئه در دقیقۀ یک به گل رسید
⚽️
پاراگوئه ۱ - ۰ ترکیه
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443345" target="_blank">📅 06:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443344">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-_bRxWfF98pQHJK1lP3W0vbx3hu2bDcZCOTLrSdElGFHAOc8kpYboiuZ4lICK7oYgrWyH1i0hZwBMRjczL8LpxyoLEVUoUssmUr8hL-PQYFPhnFiT8y_JVcKqbQbl8Y4SkLR-kQ1sbCBSGjVbIS6uHLwDBJIQ5oN8WWooLZ9VhrXTr9xstVbv9f6rojB4zOMz9bT-pY5LILvBMY4oF7PyRiKjXkL9ZuoO_lhNQ11V9MWCWCTbjg5S_NRdOtLHkl52T8KAALgh3MreFHha52StK1-jr8aVDo6ZFbuaHVROOtHfsmCUfngqN4qzJrJmOth1Db0g_QfuscMj_Hx0eR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای تازه نفس در راه حفاظت از جنگل‌های شمال
🔹
فرماندۀ یگان حفاظت منابع طبیعی مازندران-ساری، از صدور مجوز جذب نیروهای بومی متخصص و کارآمد به‌منظور تقویت بدنۀ حفاظتی جنگل‌های هیرکانی خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/443344" target="_blank">📅 06:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443343">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hkg4ZikELVxmsSMjH8G0dzLQR9cirLayI634kEBSpFElLXgJBGo3_xJ4kaeIg3yZxWG9uczuVZXSLbib9ro6YEUyeFeWdUs_1CDjSWZHudnY6oPuHP28ieCsglStaietLow1VjjQ5i5OECCf8N9UtG2i9nnXjNzifoP48DMrLM19s4lFQ_uq0X4c05a8YSIhhnrq35zMjPvAe6AceGPnMLez3500tyIgqa5M0QahMnBMqbELlqDYN38-yJ_aCVDuQ8p-B3LfcLHWK6mCUbR6rjP3MOBZRV4jHGjPzYiT2BB709XDXY7aOOFpw9eEB0NpH2_ZJEwV1a8pyMYS8KOveg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برزیل‌ و مراکش در صدر
❌
هائیتی اولین حذف‌شدۀ جام‌جهانی ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/443343" target="_blank">📅 06:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443342">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1y6a7DdGyBxrl_LaLEWtZ7cP1yFZwM78gUDXE4ncjIOjNz3dNvyEPTw5mClIlzAAmYes4hTkMXRjquxjQ_nJJ0JeUbCGKBJlTXF6X6kLeuQYyNGiI14DVOfb2fQ_4fxkPhy_0Ygx28HYjjOSIMgHmvd9BuefBpb32YNDot8rdRUfL0aAnXgYeKzk0A6b7qZy3M_SV2IZQgINyCdH3V1sake22j_Tnn_Un9tIelhhQvw8SgCwmeu16bq48hUPAhdST7v6o3a6huu7JvGUbLaSP_rqVkPt9PtpU-G1D40ua_Md_ahqgShxukMuXUKaeyQEXX6QMz8YbeVnB2B84sILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برزیل، ۳ بر صفر هائیتی را شکست داد
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/443342" target="_blank">📅 06:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443341">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34c6faf471.mp4?token=YXbjz6n0bWa0nojHii7yiYlQsIWK64SyyqDB0RaJp0NFy3TBlHBn1s3z4vW3lelOl1ONy6djO8KJYj6JfPHjf73HD1RZ4JAgXDQSVgrQcsrPOEnWq-5wnCYvdUz4OgzdHHMHHis2XKbHN6TtBSFV3Rx6c8hd8Df5Oopgx-01pyNMhbnRG6q81403aU1UNiXOU3VY-G2V1Jf322HahWEPxd3dU8FvbNXPvTGUrz2ysufGWk2F7ILVQkYYw79BRdhRrA9AD0dnE94a8W3U4CGaTHU35NS6W6N2plNX13YIHcvnSr3oiPuIad5Gx8Xz72xRgrh0B-lUzTymDfk2N7SJOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34c6faf471.mp4?token=YXbjz6n0bWa0nojHii7yiYlQsIWK64SyyqDB0RaJp0NFy3TBlHBn1s3z4vW3lelOl1ONy6djO8KJYj6JfPHjf73HD1RZ4JAgXDQSVgrQcsrPOEnWq-5wnCYvdUz4OgzdHHMHHis2XKbHN6TtBSFV3Rx6c8hd8Df5Oopgx-01pyNMhbnRG6q81403aU1UNiXOU3VY-G2V1Jf322HahWEPxd3dU8FvbNXPvTGUrz2ysufGWk2F7ILVQkYYw79BRdhRrA9AD0dnE94a8W3U4CGaTHU35NS6W6N2plNX13YIHcvnSr3oiPuIad5Gx8Xz72xRgrh0B-lUzTymDfk2N7SJOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در دقیقۀ ۷۸ بازی، گل چهارم برزیل به هائیتی آفساید اعلام شد
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/443341" target="_blank">📅 05:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443340">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfUMTYz7zkY26QuUfkbeq0Pp7GAp5hkNJfv5kwwF8aDk22cJD_rlN1nH-nLTQ-ipFZC0WCTzsWajxE4s6MVFFV83NoFLSGFOBg-xLKtMcBHqukqXXsRyXhTAV4gteqrI6x0Ii5kruApA3XXF5VdjmQBpnB4B2m2gnuh6_qJkOxT_uJUrMVBjJndJRQFnvaEkkFeyx_682bfAtK-Wg-DBfc-9bYF2Pwqp64PHnZizcnTuuBoWRrRA4HWsYu2EZc2FsiQmVKl3OMWvJ2uFtcPKXIA8WJgBSYUFTbOpuzHkqFygSZ-92EEZZGP01S30YSN9L_AIm2mZwjq-EJHKR2d6wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکثیر یوز آسیایی در محیط محصور؛ آیا راه را اشتباه رفتیم؟
🔹
از آغاز پروژۀ تکثیر یوزپلنگ در اسارت یا همان جدا کردن یوزها از طبیعت و انتقالشان به محوطه‌هایی محصور حدود ۱۰ سال می‌گذرد، اما در تمام این مدت تنها سه توله یوز در سال ۱۴۰۱ متولد شدند که در نهایت هر سه تلف شدند.
🔹
معاون سازمان حفاظت محیط زیست، دربارۀ علت این ناکامی می‌گوید که در آن زمان تجربه و آمادگی کافی برای مدیریت چنین فرایندی وجود نداشت. از سوی دیگر، روند زایمان نیز به‌طور کامل و مطلوب پیش نرفت و مجموعه‌ای از عوامل، از جمله کمبود امکانات و تجهیزات و برخی مشکلات دیگر، باعث شد نتیجۀ مورد انتظار حاصل نشود.
🔹
این اظهارات در حالی مطرح می‌شود که طرح تکثیر یوزپلنگ ایرانی در اسارت با هدف نجات یکی از نادرترین گونه‌های حیات‌وحش کشور، در سال ۱۳۹۴ و با انتقال «کوشکی» و «دلبر» به پارک پردیسان آغاز شد، اما به اهداف اولیۀ خود دست نیافت.
🔗
ادامۀ این گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/443340" target="_blank">📅 05:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443339">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‌ ادامۀ حملات رژیم صهیونیستی به جنوب لبنان
🔹
المیادین: رژیم صهیونیستی شهرک‌های کفرجوز و نبطیه الفوقا را نیز هدف قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/443339" target="_blank">📅 04:54 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443337">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FXnNKOsHShSnmcqKXeXcE1N3J8LY0O3peq41SuiRFOin80-2_tup5cDX72dsbyn2jttPKO-GTcHxo-6-9P0zLWhnN9e0naKtrP7Icr7ot6lTWq_ra_hQMXKxwWVHJxhznL0L8j0sfrbJ2lVdpe6_tO8jwKTVaCpw5Rupfg8Zt9V6qUIIeHENCDuYVY3N4mgMaglcI_-5yRNEORRRuTskHm7n1vdGqZ_nXQ3UD8tCaoZ_avYgouGVq_fMgmSbazJAsjKgKC78r1y2UVDGgZ_YWYlwA5fVPaYqWwsPFWYizNhL4qmOLgEGtGxs95Y7pl3Z_kldoXy79Qa1Dtawbbqrmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XqAoINhwZGoG5KA9yfkVhzlyactXHcc1pgZlNqUJMiKGkVuwasmUx3iX1VmLHQz2v7fb9b5CGaCvrRlfC7h7AI4aeOYmeurtR-QheF0U-LvrK45pcnoVE5qw8wX73tUgf43oCt89wa7enayaxjaf94R8u_bzVyzDh8LPIzuW8u3C2IW3KFBRFJ6iwM-n9dPfBTWDS5wF_qF8eds65Tsh-u8Jj_qcrBfPruHvJyh51EdEtrY1r4XV5qBn3kkTzSWJKuMscane5QClZwooemzIYDDhNwxwOP-e_HPY_LqvxHpoA3GEKTYqRhKtmARBDNtSyxEfmmDPG-NysdvDPJ-JsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این سنگ قبر، جان‌ده‌ها نفر و عمر سازنده‌اش را گرفت
🔹
ناصرالدین‌شاه قاجار نه‌تنها در دوران سلطنت خود برای مردم دردسرهای فراوانی به همراه داشت، بلکه پس از مرگ نیز ماجرایی پرحاشیه از خود برجای گذاشت.
🔹
سنگ قبر ناصرالدین‌شاه، از شاهکارهای حجاری دورۀ قاجار، به دست استاد حسین حجارباشی یزدی ساخته شد که چهار سال از عمرش را صرف تراش مرمر آن کرد.
🔹
انتقال این سنگ عظیم از یزد به تهران در نبود امکانات حمل‌ونقل مدرن بسیار دشوار بود و به‌صورت مرحله‌به‌مرحله با کمک مردم روستاها انجام شد.
🔹
در هر آبادی از مردم خواسته می‌شد با چوب، طناب و الوار سنگ را میلی‌متر به میلی‌متر جلو ببرند. گفته شده در این مسیر ۳۰ تا ۵۰ نفر جان باخته‌اند.
🔹
اما با وجود این همه سختی، مظفرالدین‌شاه تنها ۱۰۰ تومان به هنرمند سازندۀ پرداخت کرد؛ رقمی که تناسبی باارزش اثر و سختی کار نداشت و بنابر روایت‌ها، این بی‌مهری موجب بیماری و مرگ او شد.
🔸
قبر ناصرالدین‌شاه در حرم حضرت عبدالعظیم حسنی قرار دارد و سنگ قبر او نیز در گوشه‌ای از کاخ گلستان که با نام «خلوت کریم‌خانی» شناخته می‌شود، به نمایش گذاشته شده است.
🔗
گزارش کامل را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/443337" target="_blank">📅 04:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443335">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXwbWrkfbv2ikGtKxE0arVoPafPD4A9vDkYjabnIvfqi68RVvckvbQ5xYpLq1oA7fm_-6c1ReRjwq7klUkkWIxL3IbfNUVIljvdj1VLDjWbzl8ICvIbXh2kOfJQpYVpKhEOs2Zoi4sXsbJurIWTSFGtYsKnp5twvObu4xylYc2exZitcJ7qaDgb4Dcc9-ICD4lkSFG8Ud9KBopkWMDu2rYuVRfJpou-vynOG4SA-DxDFZ0TRuqP_3xNiGhAzdGRTEAUA7VM6K7OObYPKcroDQZb71wMoA93WOVRcQ1g4Zn-Ileg38Fyil1Y8172qe7PsOrC83u4GdUOzavX47Whv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدافع پرسپولیس در لیست خروج
🔹
حسین ابرقویی که فصل گذشته از خیبر خرم‌آباد به پرسپولیس پیوست، در نخستین سال حضورش در جمع سرخ‌پوشان نتوانست عملکردی در حد انتظار کادر فنی ارائه دهد.
🔹
بر همین اساس، به‌احتمال زیاد این مدافع فصل آینده جایی در ترکیب پرسپولیس نخواهد داشت و باید فوتبالش را در تیم دیگری دنبال کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/443335" target="_blank">📅 03:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443334">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5599fb0ca.mp4?token=X_HCeKTZ1LJnUWOvIza9iwl_wZcSl5pxo5-ebZejX8z6LZw_Q1Nx8l8IDQs2HP6NdZI106iLyX0Nmu0lReqVw96Gnnqf-H0zhQcLLmHeBw6v4Auosn4qidj6wiqaFQc4cCkIdmGqcilDEOryEHXSvHpn9Y7t_vfRfr7QwbpFteXdUefGus7Q0kaegcZg0gNZC-ALP7OEjWGPzCBy2TjayLxdoBL7OIVTwL3t10aafXrq1S6mlbOgtmQrf45kfdJ0nFRsSaur1QVwAnf925ExHaIDhpB8sHLFj-gtTRUt1TJZnpMpSEhG3kHeTYT4MMuBKhLGz74R0HtKZm8rZxRiDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5599fb0ca.mp4?token=X_HCeKTZ1LJnUWOvIza9iwl_wZcSl5pxo5-ebZejX8z6LZw_Q1Nx8l8IDQs2HP6NdZI106iLyX0Nmu0lReqVw96Gnnqf-H0zhQcLLmHeBw6v4Auosn4qidj6wiqaFQc4cCkIdmGqcilDEOryEHXSvHpn9Y7t_vfRfr7QwbpFteXdUefGus7Q0kaegcZg0gNZC-ALP7OEjWGPzCBy2TjayLxdoBL7OIVTwL3t10aafXrq1S6mlbOgtmQrf45kfdJ0nFRsSaur1QVwAnf925ExHaIDhpB8sHLFj-gtTRUt1TJZnpMpSEhG3kHeTYT4MMuBKhLGz74R0HtKZm8rZxRiDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آیت‌الله مجتهدی: به‌دنبال روضه بگردید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/443334" target="_blank">📅 02:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443333">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
رژیم صهیونیستی شهرک «کفررمان» در جنوب لبنان را هدف حملۀ توپخانه‌ای قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/443333" target="_blank">📅 02:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443332">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
رژیم صهیونیستی شهرک «کفررمان» در جنوب لبنان را هدف حملۀ توپخانه‌ای قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443332" target="_blank">📅 02:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443331">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7rI5jpJEoLc_1OvB7SdP_InoEBFkDSgFaGARFN4SqLdWKKkbAQafqpuYlVKiqJOhc50-U5U5KZoTiSIgX4_28K3s82IsYx5jGtF_znZxOrt9mqhzl9IZrfgM1pCDwOXXqZvbL9pnYpHoXEnSF97j0RQWXl_M7_aN2Jt5U-_imxVeRw-ub_nEhqdrfSc79vJ71vYBIhOzE_v5bS0BUygKxxG6sF460bcU20MxkjbkaDpu9qiUsR_QpCQgg9x194h2ZsAdLRKHkVofVy-e6baW1JOKGAXp5d6zITm0DGXEU2wLKsoAEWxT3BeJUyIWHZpz83wy-XsTjeseh878V46Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقاومت مسلحانۀ ماینردار بزرگ دربرابر پلیس
🔹
سفیدمو، مجری نظارت بر استخراج رمزدارایی توانیر: در جریان شناسایی و جمع‌آوری یک مزرعۀ ماینر در یکی از شهرک‌های صنعتی کشور، عوامل حاضر اقدام به درگیری فیزیکی و تیراندازی به سمت مأموران کردند.
🔹
در این عملیات، نزدیک به ۶۰۰ دستگاه ماینر غیرمجاز کشف و توقیف شد؛ اما پس از بررسی بار مصرفی شهرک صنعتی مشخص شد این کشفیات تنها نیمی از واقعیت موجود بوده و بخش قابل توجهی از دستگاه‌ها پیش از شناسایی خاموش، و همچنان از دسترس بازرسی‌ها دور مانده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/443331" target="_blank">📅 02:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443330">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab12f1bdf.mp4?token=bSDmhZWVli-2yyKv3h9c7ROCiPJDk5iCaPVyU9sVqp5gIKDOp08VngsIziXcvg9yXtvlQ8DdJm4Mh2wbJfjuRhW6GMeva9eFd92WdhsPrkmrPL-2f36DiFO0Pm9yiJEYvUp33Ex4z11ftOJfSXnv6bjhhFgrLZ8P3-v2EhkBrrEWWh6cqDSTpEI0ylxMJv9XHb-fOsn06QwYgixr-b9lza-pIfjKe9fbMz5vwpFQlhFaL5xLa0njSQP0aXJKcJZzYni6dPScOKLeaCO5ocs0T52qg_OyngfIM2kdUsi8sIbsrc84ryBmgBFZ2r8mfN8j9oakxdTe_YBQ4IrYaAbYSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab12f1bdf.mp4?token=bSDmhZWVli-2yyKv3h9c7ROCiPJDk5iCaPVyU9sVqp5gIKDOp08VngsIziXcvg9yXtvlQ8DdJm4Mh2wbJfjuRhW6GMeva9eFd92WdhsPrkmrPL-2f36DiFO0Pm9yiJEYvUp33Ex4z11ftOJfSXnv6bjhhFgrLZ8P3-v2EhkBrrEWWh6cqDSTpEI0ylxMJv9XHb-fOsn06QwYgixr-b9lza-pIfjKe9fbMz5vwpFQlhFaL5xLa0njSQP0aXJKcJZzYni6dPScOKLeaCO5ocs0T52qg_OyngfIM2kdUsi8sIbsrc84ryBmgBFZ2r8mfN8j9oakxdTe_YBQ4IrYaAbYSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شروع طوفانی مراکش؛ گل اول در دقیقۀ ۲
⚽️
مراکش ۱ - ۰ اسکاتلند
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/443330" target="_blank">📅 01:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443329">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca518b96fd.mp4?token=CE6MPA0BGhhsmc1sazSd_Ayxc9LAo-G4gh0oH3I8oxk26bff-xZLeXtPP3n7-3vBOQPkbVRPshRqOLu8EVTtkGQLw42W3eHQVeXqltxXUIUs_exZ_DyyLAmqMx9a8mJZMmPZIBr5zCEGFO9X6bgM9U9GGzdUeIvC1MkHeXqFx4iM5DKbxURFpeqb4UceGZ8kIQI7lfWrvfgfg2hdHGmSrlLZw5DfKKAoJLwDbz3FK9lEn68N334eiekD718NIuL_wEQLp_lYM6jgi3NCwZTmSkNNyYXJIEI86zlWxKoNq5jRJMPG6kqq1gYxXnpG6z-lAWV27fIn_swvxvCe1-tO_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca518b96fd.mp4?token=CE6MPA0BGhhsmc1sazSd_Ayxc9LAo-G4gh0oH3I8oxk26bff-xZLeXtPP3n7-3vBOQPkbVRPshRqOLu8EVTtkGQLw42W3eHQVeXqltxXUIUs_exZ_DyyLAmqMx9a8mJZMmPZIBr5zCEGFO9X6bgM9U9GGzdUeIvC1MkHeXqFx4iM5DKbxURFpeqb4UceGZ8kIQI7lfWrvfgfg2hdHGmSrlLZw5DfKKAoJLwDbz3FK9lEn68N334eiekD718NIuL_wEQLp_lYM6jgi3NCwZTmSkNNyYXJIEI86zlWxKoNq5jRJMPG6kqq1gYxXnpG6z-lAWV27fIn_swvxvCe1-tO_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«علی‌الاصول» مسیر حسین و شمر جداست
که شمر بندۀ شیطان، حسین عبد خداست
🔸
مداحی مهدی رسولی در شب پنجم محرم
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/443329" target="_blank">📅 01:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443328">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPWr2WQgQh0J4_aCbkuRASSsfRG3Lg_czhElI47U2KySYppMefrobbWwk3Cf7O7xFomwiEHzcUV4aAXvE_zwkFn5_lJR5KSNDCMu4OZ8iJQUOwoyV6dIDVolp6CacM91z9DaiwD69MkW_BbeePSIaRVB8gLxyJPrndn3wJaYUC8qjD2B-dQD1d9JthO0uCmTSK3DMd9OeDcIPLqef1XqlEUCBso8LEsjQACQJqNZTKshrSNUSOBOoXVyH5B6uVkrYCL6e32stEMXEAuObrY1q8tkbhWMYmFZ1MeIfzGL-f7HzG4b60ALLTpLJEnW_FrY-H4Comd9IZ5k-yXYFgegXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدشانسی مهاجم استقلال برای بازی برزیل
🔹
داکنز نازون، مهاجم استقلال برترین گلزن ملی هائیتی، همچنان در شرایط نامشخصی برای حضور در دیدار کشورش برابر برزیل دارد و احتمال غیبت او در این مسابقه بسیار بالاست.
🔹
نازون از زمان دیدار مقابل اسکاتلند در هیچ‌یک از چهار جلسۀ تمرینی گروهی هائیتی شرکت نکرده و وضعیت او تغییری نسبت به روزهای گذشته نداشته است. بنابراین کادر فنی این تیم امید چندانی به حضور او در مصاف با برزیل در جام‌جهانی ندارد.
🔹
غیبت احتمالی نازون می‌تواند ضربۀ بزرگی به هائیتی وارد کند؛ بازیکنی که نه‌تنها مهاجم اصلی تیم به‌شمار می‌رود، بلکه یکی از مهره‌های تأثیرگذار و رهبران این تیم نیز محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/443328" target="_blank">📅 01:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rqwYXG_wliGvgQcyrYrY7NsacHYppb528hNOWwnmhzSeMsZAcpKn4R-5l7oZRkop2ECUjIdVK9C5B9UChm9TGc1rqeS7PH-hGBvGK_rDm4d6bkipzaIk59FX9nu7TOzgepY2x3V3HsDrNkbH_t9mvGJi6HAa63tLvoPYKLdDsiJZnBgu2s55SJj7z4j13YF5Ar9YTMvKfhILUuenIKHeIqamNfLCcvjJb4_VlAy2nzr1xGUEE5iR79BRTl9eeAGoRGp203tldpFVAKrO36vV8mHvjgoEqIzxkeKQ1X22zAE9lzg-fD6HUufb0AHWG3rAltshMNsO-5WH025thk8odQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8w_DZnpd3MiJWnVRPJiF4ifRfk7Qdzi-Vwkq4V8wfBkQdCFdAFu-WFVG2czIZmcx-f0t4zpL9nUAREpVvt-iKP48C597JSMIoF0eU1ouqb0ATdF-IXtkLzIIuAS5YzH16UqqOm2wAYB6WHnYzHq_bJu7eO0xtgll-umwWJE45sdxTxDHjI-p2grYVScedn5TW8vrHBTDUVsj4Ks3dbkzEoMmRdzIP5hsIST1p8aFeXfOfh3mRKMtXDWrk2tkkUaR6xDdmmszj4mnzmyNmUt2DpmZ7qc68r1PRJ49Q5g4c4RnFZLVHCjLHtefbeOKOF4BKNCKngi63tzPw6w0i9FxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BlUQzk7jh9_nL_g4Q0LaLVtmUzCGyKA4htIz9ZXhlwKDVpnXadpMkM5pGwhhXXhSxurgWw_aUlxrhOE7jzxCFBRyEKgBHj6sSEH-0MLJt56QGW-4f7dvugSEb-6djrd71wdzW3wOXFqztHbbUaVpwHufOEf5_iMXNtPYWsxkFiEVD8onuwIoKjijNPPPh3wPkktXgSJz5mT4Ylq0e27iBiL-uAx4GU_Igvgw_bo47oE47jGl6hKO--D06kQew4grw2AJLcDfmEtcwyD9Z_c7NssOAXCIIDdc-OfPx18g5I3bixxt9HEqf_uY4YHUcZAki-3YwcH9tGsqOKa_CRJthg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T7246T4eHpkrkQJEKs9tr_QwBRp5vdfgj_HRiMw-wfi-8CwOKUy7TnmvG_jXq37rG_0vUeBl_HsRE_X_ZHfxPSQeYowIOh-teRoP-xOy13-txKGtf_HeeUAsxnqHCLKSFEIbw2QBp_33mgyYYkNDHEWaFa4q6ZlKD6FBf82Kioy8woS29BV8_oG04HkBeM_BhFKAM931pu9Bg20C3RyCSJisIqciLxQSb-a9x7m0jlQV_WpKkmmIGzvlADxbsq_8UFDRyf0JQ9dIRMiqcYDLrKKOPJ81EVUas0LcmpYJQHFgGN2XtkoQrNOAb52y4MgdVyeMrxKKXVulGvi5XWRv2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zbloe16hbGC0Ag_GRCXXDX40fcdPlMxlF2p4_LAZ3mp5ufSk0s9nKTG17Zx6GR8ai2SS56pltlKlVwm95p5IhWSuZY64SJN_nvEiYQ8txj7Q8_zJksqx-GMeHvZtwLBJwZuVu0Awc9GFjeYkUaNBdFIjTSm_6qaqZqN4fw1YMW1tRzNXaLgrXaGCx3GOIzg3-dKKn4Twq_DySD8KTGamKX5jrLcFrQmCBMjXbs8QcIzKVjX8L0oIWZIFsbT4d-mcF8ct80E-NNlpVFeGwBIjw52H3UQ1_LuKGA-m30eI0ptcB7AEQUN3hm8mTvOJ_volcgtrFazmJGwir6_p-3Brbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmQ4LvXLrMYxNHpJ-JlXYzZD4z-5cTosIwaLuEJIa9Yi-ue1nj0w-FuMng3qZc5fSM5Vg77uvD4HicB01XociN7TIJrhRaRxf69T1l3IlA3vz8RoeIHI9h81QtE0Q16-OOZxs2DhF7IJDv_je4cPTZfpzea2vgbXfLVvF5uKtS6nkrgzfqWa6imJApqFcfaVhLEQaDC0opdDg-hCVjP3JCgcSLc6kLxfNqiArJZomcv7_tPW7PUJvrNn7Lw1Ly_ftVHFjE5RO96ZB3Xw-Tw-xCjAi1FvHcP_QsEUaOU5S24DKnf-mt0qMQhtLvHyDj6hP71kwJV5UwyNVH3-zQH3ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | شنبه ۳۰ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/443322" target="_blank">📅 01:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443312">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OwgB6ZfyBhg7W58xlYQdCiwGt_pT5nsiuVz6-4Ibe97ABFXtzjuc8HVYiLeubxPuPUygTsVrkzP4fTOIufhZkkfBFjN_Z5nfln9piL-1ugn9uUcFs8yadbL3Dl-G4hl4OXWuuVjQ4_9Gq18WcVkqPsr9GPcxtgA41OphHAMPkI_Tk_sLiie9rjQHfrbYMcRxOOIuAY6VQVJPpRVYdBzbpBUKbEf07BkOL8NzU5BKnZ6XyqvxplVbyBupEVStPfaQ9__1xcJsmYAqnIHX7_5dCqRpMRa2CyWZJTkcADC8w8i-DLiHAQvHI4gyoF723qZLb9eNWwU4LKiGTI4m84j0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qIXJvMWX_U4I1AHpANipyJ4nG9HhFzrK35OxAcq5cL6pyC3vXskgsOwcDOAF28ry3ouSglWH8W1l4JSWWPZSfgJ2EQQqxZzfX3ewlhpB7cg_lbeS51FT4MDwsQ3fM7u7GTIuWa3tslhijrnhHnS-FQBA8uSv_-qLKnJ3PdTrT6nBHK0ZDZEINj6U4MTywvANtyBuTHnve9Pi4jX9OQIu7GV2xyFvYV9Brcjez15bQPUyvuQ3hgJxNGsN7N3TrqkcLjR6yXd-pqDGG7LgClsUMaet71VOQ0J-6rp0_KbTqU0m3ifABUTL6z-g7HdCMx0S72l8FxDe7KVPk6-n0Yu2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ra6QSjXU5T5h9bjzj7qwrqzSAGlkSmSZFD2gmZbUUBfzO3V6vmFgchDVIIDtFGWKwFKo-fQlQ6ZbWMe7i3GqrrBnEqaXmDhN4C4v4yudct54yG4PgSsLhIoSB2y37ReasUdVd0inULQMdojiKZkAaTC2xjNKCBjsxSNteQuuQ3_6vzxGjPkn7xwP83cGHIkbcf7FTPqiDkeYkoiX32oZoS3eIiph9pH14oW7huuf9MYmhMMJh4OpNe-QcqKIyNIqw2fpf6iTGe5AyRvxKJQP72gBRcfse5piNPBLy4Q6Uy-KnreEMmoi8wokG4ROpMulYZ58LfS6kX3agvarQErEQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WotG6vA_R5wDzSH2eqSh7tEyPesNT1rhtCfXXB1P5pZxJVAznrPw5wKvWYOr8liHCAxtypvPLaY03WQxUzn6KccE22UQ6kbitBp545vnXaxE6-rMvqCIfjaohR-4bfLFa57bhRWYfznj3K_SfzmPuAfLtUS8oE5YsyHr1r81Eu-iX16CvTwNHu-AC3iwvxSpnfNhOT22Y_zezsW4v3u9Ea1kuqhO_1vMbYFrKdZM_NEoX1tmLk0RBV4HDNrwG7rctOZ85RFpXw8uaIyban18bMUSHCf9BdD9Zl1AnJkdtgaRVShm2t_gm0w0UZBDITvcY6NrG0b6YRZNTSB-TvqXng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjiTDimk2oSF19hzb16kbDhFxcurm_1mzpficQRNlCPqYTdJXtp_dsz0rj-leYLAPpe8pTWn_JG1FjTHi1jq9GymzcvM6Bff1nKzaIySQ_aXKBmVPdUr_TQpDgmTgXP-XrvZ7d8lZ4GSUxGa7gf4G1uD2vvjwsgFhWpk_J2gR1EKAVsVHV6H7cRgyZFpWIHKm6oLiZ459bRmvPXp2mLtudfsH1IFbsGgVlsvXuBLMLt52e9FDUyJRQTMsOWXob9OiHvSLkjjR575qZ3vxtCmb3oSIiI02mYxUDe9GK0Ejy_k0yfwfVfOyIgwzDUdGmf2_YEiRPXhers2k6Hwzmar1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6nWKj_7YIU8C-aU9t4idX4nGZHTfbbfoDyrzSMSbDBtjPaM99VvSHBnUw0lDa1L3_JY_YJGwnBtqcWtTtAcGD6Om_f7iOqPzsWQg7s33Ltd69swUANrxKs9bVvyfTPFF1-OrbcNTtsTTSFi1VhBVb3JV73smtauu-ILUx9DLFIRJyG24xybRBbkzxa_kNdn4aLbfh1tvoMUf5Ch0J4fClCYmUfxX9z3xD6EjlecCHX4Jxeeq8YOnNZ7meboQFIIP-yBtdKUfeTOYlGWINpmr07iRU6RXcKUsYwZr7fB-tycS4bY3SIoJX334_0sWkHVIOKiEl8xqWAz1qIBMsiTWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/REDiDoRI-QmmHrYlxTnOQSen0c3yAVpPwc0KQzlaV_PmzXz1TG0DBoKeZ1IO6uoBkWDH8nJ93M5N8IQE2--SQw6K6GCvRJEinIhigi6yp43Wtjjbo4jHn7xsm6gtsvbL6kbcnq1VkFYgXgga6QirX_YM2RifUlNQER06PLIo3iYG4sZkVhj6yNs9TdkckXVOPXAf4yxrN-nyPtNaSVizZmXX6qF54KfvzImMWvRoniOlcSb9V6xP9aZ_6KByy63y8HQvlyN0CgQlx-71HtFRghUslHfh5RFZJd7GfrVr6GhEJs5ApMWaKDF4fHoj39C4v0Tpbe_y6frOPvsGzWTyvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKcOM9ltkZqfzU0aCigFkUfa1lzZsNJWW3VnoWF-TFNAeTAl9zoDLoMnczSFbV8kkaTfD3hWuAIS109h0tf3Ugi-hbUS_mMw53oB9dSoNaUhBNr9mXiQjffZlezHcJj9hgLBXObneCKBoaLFQi2W1I7Ug1HJ7UMGKBKJKdO0Ok8qwT4Ewqp--KTftge7waWjtT4mFF0Cojbwakb9GGdjyxw11IoPeh4oyJzsVIx28qspKDMZ5uo_hElen9VpiRkM6DGmcGIHazK56E1bTPvadqqq01pwUvCeWAJsLyUwB4rdGPqyjiKkGzDVnbY3kC9D4CJAN9kODcitYC8hIl67Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDQ3NphGGu6uZfodrKEpWFyCVLCPEE23PT6d7OFTHLsaW49aVKyvLh9StHF-rcUHWxHIMWXfotI68bFU0x5DDhP3aDFmg_FVL20YQKDYUFgjtv53Ls3hvuzB4Z1AjCcpOYKe6QAjE3v1BR3N4UGazXWaQALaNTbaTeY9xdsefMaI3oSaKTYl66wgW1e2F52k3SbmLd8cra46O72DBOYbVQe1ew-hMVT5fZJ1snYo-vUjbFEdH2mCk6njqqINgzxV7gNOE0S5BXPHt-efIWPLPda7PzwW3sGJqpFrWecUOXvWU-zZuyTWwou9VsFr30zZxgQQ_FEje6fGbr-PkOO9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s82PlS0Cd3w-rr5Gc5nYeCPRGFeyfV3x77RghL6gNZYcn64cLhTmckSij0Glaax-x3VlSgur9iFjrAANiq-N8mrDy61QDtUOyx_JC07gj1kHK3aqk0lqRH2Wu0I3cFsVyHKPUthXujtrP8tANcfP4A9G5QzD7M5AnetbGC0Yf_YPCYFJ-QGZP9zhSA_bmh0F_J3NKSDFLqW86n4757OWOskjpwKjWn2suXmlaOHnmfVOBPAu3sa2iHFgsd6rj0wqTGZPLhgkECcm1ZCqwi-Xmpt3JehgLKew1SeSKQBNr3f6jcXj25knBF2qGJeveqMTOSRpf0CUlrfVLOWG_d-wNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443312" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443311">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee81c2b3.mp4?token=tEOx-cgAM7N4NAETs4KM_aWKCWFvMdoAgi4WcbhQxh1nhtgWo_-PUVHt-Bjr1Su0Ike1kEso1KQrVyvSM5G6pyzZkfD8Q0ZqmZ9nmA79sjbJO0RhRbiW17HYPCkMT2Y3uHkIanVVvYo8hxHNGjHQrBMJEv71my25I4NWi-uZOhZIABiUXP-ygEdhGD0jRfgV-unFHtMrRkNzNcBZI-wZUDFPqtavEXWzucj2j2BMXU_t-Z7qI5ADxRphcudf_3jhq7-WKKa1fqe3LDEkQfK_DVEsL9GxODLhBIYyIImQ2UyhWPB6WZKyh5ix2a_jo5m3fqkG1SaErXHA7g-07repgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee81c2b3.mp4?token=tEOx-cgAM7N4NAETs4KM_aWKCWFvMdoAgi4WcbhQxh1nhtgWo_-PUVHt-Bjr1Su0Ike1kEso1KQrVyvSM5G6pyzZkfD8Q0ZqmZ9nmA79sjbJO0RhRbiW17HYPCkMT2Y3uHkIanVVvYo8hxHNGjHQrBMJEv71my25I4NWi-uZOhZIABiUXP-ygEdhGD0jRfgV-unFHtMrRkNzNcBZI-wZUDFPqtavEXWzucj2j2BMXU_t-Z7qI5ADxRphcudf_3jhq7-WKKa1fqe3LDEkQfK_DVEsL9GxODLhBIYyIImQ2UyhWPB6WZKyh5ix2a_jo5m3fqkG1SaErXHA7g-07repgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
توپخانۀ اسرائیل با بمباران شدید جنوب لبنان، آسمان در بحبوحۀ «آتش‌بس» روشن کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/443311" target="_blank">📅 00:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443310">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
رسانه‌های عبری از هلاکت سرهنگ دوم «دور بن سمحون»، فرمانده گردان ۵۲، در حادثه امنیتی که روز گذشته در جنوب لبنان رخ داد، خبر دادند.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/443310" target="_blank">📅 00:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443309">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWvCJ_Ac9i3nJ48EtdbRvsdDHxVx5FMp-4k19xBCxDRchchuZu6jYBLCHFqc6vJimygPoZFSTLhSNj5eKJ6odVhulS5rqs7WDRocPtGMuDGonQuUb9BJg7afWFG67CmgVudqC4_Bdm0D45gGTID_i05RMRupzW1RKYuyr0r9uQwf1RWTcH7QO2O3rcZ9VZtf7RDWJP1BtjPIcoCGjpzoeqW-L_ieJIsFUTB9R01BPW5M_AxHodzCL4WGlvLqj_3Ct3vszydX6bjWMbXV5zu3vJ2779cwbj-RTfVvjkaZHlm1Jz_grVP_S_GtC0csG2MbT21_oAXE8NpD6xZCLCscbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فعلاً گل‌به‌خودی آقای گل است!
🔸
جدول گل‌زنان جام‌جهانی ۲۰۲۶
@Sportfars</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/443309" target="_blank">📅 00:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443308">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۵</div>
</div>
<a href="https://t.me/farsna/443308" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۴ – کتاب آه</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/443308" target="_blank">📅 00:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443307">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmDpUlMInzCtfotMJsexwH6FBrTbwY_1GmVmW1ODHWmhyANMghYO94UDTr3BQwU2O6GyRsWInOMiXdMVJilWxEb36wSHmC5br8gY4gLjc81zMiZDmX7P-q2zEOQBhadNxWjZ8alk7asiwdpY52DuJVpe2D7LtNJi2QwSV4qGCFFCKcZb71FnZ-kkjg_G5dWXz73x8M3RItwQjJnLLN9X4UwRXMvMpJU5-WtxTWp0RFwvZMRx5Xu8A4FwWJ3ry3j1nPmDH9tVTOF5CmkIVerLCVXpCMnjQOlKKJLsFPEuiSn0xOtEunjO8rnwAsT-XtUseazuKHwNvgnJqCKrtgjdLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: اظهارات وزیر خارجۀ فرانسه دربارۀ مردم ایران، اوج نفاق و ریاکاری است
🔹
سخنگوی وزارت خارجه در واکنش به اظهارات وزیر خارجۀ فرانسه نوشت: آقای وزیر، ظاهرا ریاکاری و نفاق تا به امروز از ویژگی‌های بارز فرهنگ سیاسی فرانسه باقی‌مانده است.
🔹
همان رذیلتی که مولیر در نمایشنامۀ «تارتوف یا ریاکار» در سال ۱۶۶۴ به‌درستی درباره‌اش گفت: «ریاکاری به مد روز تبدیل شده است.»
🔹
شما در زمانی که شهرهای ایران با قساوت بمباران می‌شدند و ایرانیان بی‌گناه در میناب، تهران، لامرد، اصفهان و جاهای دیگر به طرز وحشیانه‌ای قتل عام می‌شدند، سکوت کردید و در واقع با متجاوزان همدستی نمودید؛ و امروز در راستای مصالح سیاسی رژیمتان، به ناگاه وجدانتان به‌صورت گزینشی بیدار شده و شما با وقاحت در مورد حقوق بشر ایرانیان موعظه می‌کنید! عجب نفاق و ریاکاری!
🔸
وزیر خارجۀ فرانسه روز گذشته در اظهاراتی عنوان کرد کشورش تا زمانی که مذاکرات هسته‌ای ایران به انتظارات خود نرسد و به موضوع موشک‌های بالستیک و نیروهای نیابتی ایران نپردازد، با لغو تحریم‌های شورای امنیت سازمان ملل علیه ایران مخالفت خواهد کرد. این دیپلمات ارشد فرانسوی همچنین در اظهاراتی به مداخله در امور داخلی ایران پرداخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/443307" target="_blank">📅 00:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-443306">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEzoG3fhihryBvQFy7azo-Z-L4OK9IODclBvs3Pb0J5jI4MFonXSHkndiSI_gi1UeN-QrmRufJCTc81Qvu1LV_madiwjpUVTP4ASo3y4-VCqYuYBK9fy2rPNMAYQADYM717YRN3grUJuI-txd2cIkOEq3eM5JPhyqxXCScRBV2KApjjiwZuoLb-2eYKmesZ8CpeHSk7b6NsC-Mtx0VGt3yNcx6oHaY_tLWelWggL5ZkGHDI4Aggnq9Ie_eIz02PSYdJUkJAB6tp6v9K-RCSC5ffp9cf87MExGMKQdBG4VeXIaQag51tFja32m9hh0ULAEhOEdNZykLYEtThArGpp-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان فضایی: مهم‌ترین پروژه‌هایی که در آیندهٔ نزدیک برنامهٔ پرتابش را داریم، ماهوارهٔ «پارس ۲» است.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/443306" target="_blank">📅 00:17 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
