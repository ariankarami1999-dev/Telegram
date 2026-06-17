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
<img src="https://cdn4.telesco.pe/file/t_JGijPVxfoAic9UHVfeniCbkNjhuumzMhPmE6MZlNq-oMSvyaDOmQ2J12JlMXbCCRGlt4kvg2zVExm-5S5IHuS9bECXYXnP9wYT4cGFMsLpfj36KYMOCiPtontSKq8pmHc78wImwtFMY-JzzfW10gCB4NOm4SUmIEB95Zl9hWiUfU0SX9dJJwo6ehn8iAeN3FJU9zyTJWn05wq57Zb21VJpLFGF87pbS5DglFKgFestckVkC1KfcCkhyoSCNzKvD_a6NOz4eFgWQtvb6mfLIlJPWNiIOMx5L9BHBvRPRjdQDnSnTNWx2qEHnOliQZC2HPSS4x-0hs1l4ewDT9e2wQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 968K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 13:42:08</div>
<hr>

<div class="tg-post" id="msg-128638">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYgBnV7F14G5QMr1BpQ2VmyhNqqZdRIu4UxrZbwZELbAWYN-FXuVkC-f_4AOfTARQhKKZLgvI7Hmq-fml22D18XTC86sDAcAFT9t_LIZGGUeRWFZoQPScKRrd0mhdVj5xanXPix-9b_WU9VIpwspJ-NRMaE4wKypxTj6HoZ94CS7MrbHQphz4jI86S1ePn_J3KzTA7DklrCwKXysAhTLAo_BdQdrBW3OZ7eP9pxXeeyg9R0MgPqHXXOthriOWsJH51s4LNC4oaEnYdElrEEzx97UzDMqktC6hk2Vum6fh6GrvXSYjx7MJzJovIVjtFkhRxBnevBzaQJnNAiEOMjzkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / حملهِ پهپادی حزب‌الله به اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/128638" target="_blank">📅 13:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128637">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/368ad2dab1.mp4?token=WYrNcefkX1z3Izys2OaDwZ6a5dLdaZMR-1Cgm4xGyNzE8sSjKZrjHrQt69YaHbxL-G1_8aT6gW8uMfep2VCpuDDS7zQlnDc-VFpG7v05ndD9Hr7i-bKO5p-Hgu7RQXQW4-eXe2s1evrbKcu9uy2b5jVw4YeC-5sjJbrVFG5FfaG-YsAib7YZOYIhOOVjuBQJViZp_cYs07QWMTgVs60UiK_unhCzgDLBQwAGD6ay91vzca646vxmYl7HDJSfYTJwFnQzYst18dq9O8VeVwJBB4Y7fOiPkBDn9TKDZOn-PaoQEXIjSQZsxxUujONIvx-nQKXmMWsloHE2wWwHjzWGFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/368ad2dab1.mp4?token=WYrNcefkX1z3Izys2OaDwZ6a5dLdaZMR-1Cgm4xGyNzE8sSjKZrjHrQt69YaHbxL-G1_8aT6gW8uMfep2VCpuDDS7zQlnDc-VFpG7v05ndD9Hr7i-bKO5p-Hgu7RQXQW4-eXe2s1evrbKcu9uy2b5jVw4YeC-5sjJbrVFG5FfaG-YsAib7YZOYIhOOVjuBQJViZp_cYs07QWMTgVs60UiK_unhCzgDLBQwAGD6ay91vzca646vxmYl7HDJSfYTJwFnQzYst18dq9O8VeVwJBB4Y7fOiPkBDn9TKDZOn-PaoQEXIjSQZsxxUujONIvx-nQKXmMWsloHE2wWwHjzWGFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب نجم‌الدین شریعتی وسط ویژه برنامه شبکه 3 برای ماه محرم، یهو زد زیر گریه و گفت ؛ من امشب دلم واسه آقا (علی خامنه‌ای) تنگ شده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/128637" target="_blank">📅 13:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128636">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b91d542c6.mp4?token=KaHKW_ER7eCv0eRePAY3hHtFOtXfx7eEreB34LYyoyXUgYLdCnE5A8umlRlYqCMg_K2BZHULqOx7uB-G4knDpzOqU1snkHB4G5llleJs9D2DKPuCjgk5pk5p1XpOQo5RAnJkOmGtZ16rbtnM0zT0hnPOGmSK0H_vUk6ySgxJgfBWfyIHQCLIeGXZPJPDafjfW-pHM78Lo2-ozlf49s1Rw7v77XsDmjS3GJWKDj2fruMLUTAd2STRLg-yPGnRnPOXz3m6gIumdZxHSlP-wHEmIAihYVpRf3Q01JYM_tCm_xa8ttgV2jxBg34HzJR7GP8uywBr4gdGckCUWMWKPBz7dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b91d542c6.mp4?token=KaHKW_ER7eCv0eRePAY3hHtFOtXfx7eEreB34LYyoyXUgYLdCnE5A8umlRlYqCMg_K2BZHULqOx7uB-G4knDpzOqU1snkHB4G5llleJs9D2DKPuCjgk5pk5p1XpOQo5RAnJkOmGtZ16rbtnM0zT0hnPOGmSK0H_vUk6ySgxJgfBWfyIHQCLIeGXZPJPDafjfW-pHM78Lo2-ozlf49s1Rw7v77XsDmjS3GJWKDj2fruMLUTAd2STRLg-yPGnRnPOXz3m6gIumdZxHSlP-wHEmIAihYVpRf3Q01JYM_tCm_xa8ttgV2jxBg34HzJR7GP8uywBr4gdGckCUWMWKPBz7dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارنی، نخست‌وزیر کانادا : من جزو معدود افرادی هستم که متن تفاهم‌نامه آمریکا و ایران رو دیدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/128636" target="_blank">📅 13:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128635">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1c1bf45ae.mp4?token=Fs3dT_MIeEHvYScB6Dfhz98jy3qzrDnJb7iuPrdj90CQzxMqqnpbeczGdAj-WNA8pntlV9FDqzdguQ0YGtk3J4bs5eEEL4CaByhIvh2sIqoF5L5_uWem-BYtZcoufSp14W0ss2-wOf534tQxC0NSka9HQ0g16wWK0rPOuGnBZK6Morat3_QIvkvBPmkxDpcDsjUSCHxLf75gRDYR0HSk3SKjqvDYDiKQ2SRXWoTnTfUBG6vVrHfm6ETzT8dd7aLYuu2wOTwh23SQ2YMytdLxjHmsEELgjNoCALEBzEGv1PPjIEst3HGukedL09xBLvVsFPpJDxaJvA-yN2pZ9b4YAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1c1bf45ae.mp4?token=Fs3dT_MIeEHvYScB6Dfhz98jy3qzrDnJb7iuPrdj90CQzxMqqnpbeczGdAj-WNA8pntlV9FDqzdguQ0YGtk3J4bs5eEEL4CaByhIvh2sIqoF5L5_uWem-BYtZcoufSp14W0ss2-wOf534tQxC0NSka9HQ0g16wWK0rPOuGnBZK6Morat3_QIvkvBPmkxDpcDsjUSCHxLf75gRDYR0HSk3SKjqvDYDiKQ2SRXWoTnTfUBG6vVrHfm6ETzT8dd7aLYuu2wOTwh23SQ2YMytdLxjHmsEELgjNoCALEBzEGv1PPjIEst3HGukedL09xBLvVsFPpJDxaJvA-yN2pZ9b4YAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تلاش بالگرد کاموف52 روسی برای رهگیری پهپاد انتحاری اوکراینی بر فراز مسکو طی حمله صبح امروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/128635" target="_blank">📅 13:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128634">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
مارک روته دبیرکل ناتو: از توافق حاصل شده توسط رئیس جمهور ترامپ با ایران استقبال می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/128634" target="_blank">📅 13:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128633">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
یک مقام آمریکایی به بلومبرگ گفت:
«ایران از مزایای توافق بهره‌مند نخواهد شد مگر اینکه به تعهدات خود عمل کند.
🔴
تعهدات ایران شامل نداشتن سلاح‌های هسته‌ای، خنثی‌سازی مواد غنی‌شده و تضمین آزادی ناوبری در تنگه هرمز است»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/128633" target="_blank">📅 12:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128632">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
صدای شنیده شده در سیریک مربوط به خنثی سازی مهمات جنگی بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/128632" target="_blank">📅 12:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128631">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خبرگزاری تسنیم : متن تفاهم‌نامه بعد از امضای روز جمعه منتشر میشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/128631" target="_blank">📅 12:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1x_K4j7ZRGbTl5shxBstv-2qlMZ1ALE8mOn-BuIY2IY7USf_YKPpMTRgbyyWqIgR3uNzDtY39btsVFvwuv0VFTOn9JbtVL08YjPWh6IWAirF-dT-nryivb85rPuMsNbwb_XRERTIPsuIP59gJCkrMQpME5z2Dh7lNr3_2fCAmHcjR1-rvIEpaqfLvqeLjyC2CwTngu6w7tpQOrNLDd6RU0SfAmkn1F9PHFYXYzAIup_FzlRoLCxat8BNDXK3ja79tpozrMQw1x8lNRCwvXzoI4cqweLUkBBaDTGdKzHwPxrWFt_BP6ihL0dgcD_SurSLcz4jE9NRBcBmR4WNOJ72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با کاهش قیمت دلار ، مدیرعامل ایران خودرو درخواست افزایش قیمت خودر ها رو ارائه داد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/128630" target="_blank">📅 12:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128629">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYkhqY_Ppi_Ee07nw2FPrJIyzIgj1Jb5FQW4h1llSqUOAjRLawM2i-GW8PNjYbYVMQ9coSUnxwA264YVcmDs-pV1ntJA4AA9j5OeLj_AJyLITN_6IhAIS0bOpDSR0WqkTxJWv4FpHsEG_ZOIonU4PnbYlgc1GzlnND8tyDH8VGWNkXviRGAAo6BxSujzaLVM-pBM9qiHmCs-Z72466CInEobJnMRxgb6uPZlMCIPf4c9WkyPn0knltzVtsyv7EzXbMjsI8RX98kthEtRmwbMZJuqNDBkm2_aiIeaeBXVJPblFP8FSKoDiVaqhakmyzngU0bpLjt5G3fODo77gHMkyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاخص کل بورس در پایان معاملات امروز با رشد ۵۱ هزار واحدی به ۵ میلیون و ۱۵۱ هزار واحد رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128629" target="_blank">📅 12:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128628">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
یه زوج پزشک ایرانی ۳۱۳ عمل جراحی رایگان رو به عنوان مهریه ازدواج خود ثبت کردن، یعنی بخوان طلاق بگیرن طرف باید چندسال رایگان کار کنه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128628" target="_blank">📅 12:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128627">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عضو کمیسیون اقتصادی مجلس: ۱۳۰ میلیارد دلار ارز صادراتی به کشور برنگشته،
ارزهای برنگشته چند برابر دارایی‌های بلوکه‌شده ایران است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/128627" target="_blank">📅 12:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128626">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
بلومبرگ به نقل از یک منبع آگاه اعلام کرد: واشنگتن شروع به توزیع محتوای تفاهم با ایران به کشورهای متحد در اجلاس گروه ۷ در فرانسه کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/128626" target="_blank">📅 12:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128625">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزارت خارجه: عراقچی در تماسی با لاوروف درباره یادداشت تفاهم با واشنگتن گفت‌وگو کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/128625" target="_blank">📅 12:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128624">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
بلومبرگ به نقل از یک منبع آگاه: وزارت خزانه‌داری آمریکا بلافاصله پس از امضای توافق، معافیت‌هایی برای نفت و پتروشیمی ایران صادر خواهد کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/128624" target="_blank">📅 12:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128623">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
هاآرتص: به ارتش اسرائیل دستور داده شده که از حملات گسترده در لبنان خودداری و بر حفاظت از نیرو‌های خود تمرکز کند.
🔴
ممکن است ارتش ناچار شود به «خط زرد» در جنوب لبنان عقب‌نشینی کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128623" target="_blank">📅 12:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128622">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
بلومبرگ: تعدادی از کشتی‌های مرتبط با ایران، همزمان با آماده شدن تهران برای امضای توافق، موقعیت‌های خود را جهت فروش نفت تغییر داده‌اند
🔴
دو کشتی حمل فله، یک کشتی حمل گاز طبیعی مایع و یک کشتی کانتینری، در حال حرکت به سمت خارج از تنگه هرمز یا خلیج عمان مشاهده شده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128622" target="_blank">📅 12:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128621">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
در بریتانیا به‌زودی استفاده از ۱۰ شبکه اجتماعی معروف برای نوجوانان زیر ۱۶ سال ممنوع خواهد شد: تیک‌تاک، یوتیوب، اسنپ‌چت، اینستاگرام، ایکس، ردیت، فیسبوک، توئیچ، کیک و تردز
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128621" target="_blank">📅 12:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128620">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
در بریتانیا به‌زودی استفاده از ۱۰ شبکه اجتماعی معروف برای نوجوانان زیر ۱۶ سال ممنوع خواهد شد: تیک‌تاک، یوتیوب، اسنپ‌چت، اینستاگرام، ایکس، ردیت، فیسبوک، توئیچ، کیک و تردز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/128620" target="_blank">📅 11:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128619">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
کارشناس صدا و سیما: جمهوری اسلامی قوی ترین حکومت تاریخ ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/alonews/128619" target="_blank">📅 11:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128618">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
غضنفری، نماینده مجلس : اسرائیل بعد امضای توافق، دوباره حملهِ میکنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/128618" target="_blank">📅 11:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128617">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ترامپ :  تحریم‌های روسیه که تا حدودی به دلیل جنگ ایران و با هدف کاهش قیمت نفت لغو شده بود، می‌تواند بار دیگر اعمال شود
🔴
دونالد ترامپ رئیس‌جمهوری آمریکا در نشست گروه هفت از احتمال بازگرداندن تحریم‌های نفتی علیه روسیه پس از دوبار معافیت خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128617" target="_blank">📅 11:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128616">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نخست‌وزیر کانادا: توافق ایران و آمریکا قاعده بازی را تغییر داده
🔴
نخست وزیر کانادا در گفت و گو با شبکه خبری سی ان ان با اعلام اینکه نسخه ای از توافق ایران و آمریکا را دیده، گفت که این سند قاعده بازی را تغییر داده و "ورق را بر می گرداند. "
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128616" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128615">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
دلار در بازار آزاد تهران، 154 هزار و 500 تومان معامله شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128615" target="_blank">📅 11:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128614">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
یوهان واده‌فول وزیر امور خارجه آلمان اعلام کرد کشورش در صورت شکل‌گیری عملیات مین‌روبی در تنگه هرمز آمادگی مشارکت دارد، اما این اقدام تنها با موافقت هم‌زمان ایالات متحده و ایران، وجود چارچوب حقوقی بین‌المللی و تایید نهادهای اروپایی و پارلمان آلمان امکان‌پذیر خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/128614" target="_blank">📅 11:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128613">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
طبق اعلام وزیر خارجه پاکستان محمد اسحاق‌دار، با کمک این کشور ۳۰ تبعه ایرانی، شامل خدمه یک کشتی توقیف شده توسط آمریکا به ایران برگشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/128613" target="_blank">📅 11:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128612">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
خبرگزاری فرانسه: یک گزارش حقوقی دولت آمریکا نشان می‌دهد ارتش این کشور از ابزار هوش مصنوعی گروک متعلق به شرکت اسپیس ایکس تحت مالکیت ایلان ماسک، میلیاردر حوزه فناوری در جنگ غیرقانونی علیه ایران استفاده کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/128612" target="_blank">📅 11:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128611">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzbrLHCdoNwtoNfOyNnPtyIrLrnXIlNEN-ISIa3a_e5jUzRWnz4yXsowWJOItVkZe2cWaNyisSDQiID8gX4AEoxjlIxxnQXKPum19g4VD6IaTePa-5-W60XtwYNvO9Vubiq8jdb_CIpbMsQBpium34giIPuWbiFOP_Xlg-uRGUE3Bd9S60ZwqV04y0ADziwgZYsSkL2ztkVqevujPR-BhOd_fCPsvPULraUAXtCTqcWG6FKJoxit6Ie_sz3BztsB9U24CLBL5joJsdGh9-kaUqv1fKaCEFwL_Vgkw2lwKtWcW-7atsqh7_AqsQlCwdLAO4YUwDLI6-Zg3AudgiDbdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت مارکو روبیو پس از اعلام خبر توافق تو این چند روز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128611" target="_blank">📅 11:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128610">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/844516bd22.mp4?token=bMyX5vXRiAAnbGIusieuSXokfFpo154MwlHB2u8KDRcrx146iPZGBluSEvSjTL9kY_6MgbLzCjFK37z1f-_cXMZBllDEYwPe6-wXszswq6XAgbRxf0W6clEcV7qINNNqhIy-llvrbuIw3fYl60LGQZ8A1xMU-IiW6A9wUYknj9aY0XFghC4yozERiYMSz5euS7f0yDR-wSvh9wn9qSY3WzyJh1v2WzYN3d04SioArLKG6W5kvtWEWKjQDi1Xrb8mAFTzUfo4ITrKWohk24rn7av54PZFva2wfqlLTPVhJ9xA_LwgNzrNbqAfNgd5fcjZkWQ7piUUmxA4B8gh7J7LzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/844516bd22.mp4?token=bMyX5vXRiAAnbGIusieuSXokfFpo154MwlHB2u8KDRcrx146iPZGBluSEvSjTL9kY_6MgbLzCjFK37z1f-_cXMZBllDEYwPe6-wXszswq6XAgbRxf0W6clEcV7qINNNqhIy-llvrbuIw3fYl60LGQZ8A1xMU-IiW6A9wUYknj9aY0XFghC4yozERiYMSz5euS7f0yDR-wSvh9wn9qSY3WzyJh1v2WzYN3d04SioArLKG6W5kvtWEWKjQDi1Xrb8mAFTzUfo4ITrKWohk24rn7av54PZFva2wfqlLTPVhJ9xA_LwgNzrNbqAfNgd5fcjZkWQ7piUUmxA4B8gh7J7LzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادامه حملات ارتش اسرائیل به نبطیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128610" target="_blank">📅 11:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128609">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2nhClYVhQAizrgH7hvRquo6skugGQ9rrWVSCkU2X1YG7jrPJo82I2xhVQteJfEa9KL9F7HyNMSqqwD6afM14vs97Xm1Gl_eoBjQmeQ7s0Q9qlFAB6ZfLcLrkPc_E2c8gdg9TJTO1MKDvWa_o-x2Aeo_qg0Xx6QVEWbcP82_44MR_RKv9mxgQm9nAUSECeL63EFbtRTrCUc3mlpgg_xPvfwLmmwz6EQoX3Fy7c-xIVlDpuX-btnIq4tcg7NBqNI3Vt3EdO-ehScaTWrRQINOX769oVlX3igqoEJeE3Sq3WvU8DLM0sO0XnXgJl8neZH7587r7WFIyszEpVyAj5xNSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت برنت با ادامه روند کاهشی خود امروز ۷۸ دلار معامله شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/128609" target="_blank">📅 11:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128608">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVDKUglvlOxSwRc-RiBVmhLevCYrpiVos5abkJATo-mroBFmTjcwEhWp00g_1OwZN3_gC53lMewn-_3miOlQADCEFu7r4Qe11mU6F0VZFamIYyvs0lxRER84k-2xT8gMZ-BR27gEFXqbvGAVg8ldkRNzXDSYLzxHYPjf4OpB2TtSRD87aAwzM3_jhTRIKDC4Mmi6j4yUqw-0AG1dhv91Do9Xm2ySq4xpOaDz5CZUa3uLFcueB2yP3XtS7IvYP1sbOv63vWWtrRR8g8M21TnffGPa_zK4c10Tbk7lFYepB10jVUbzOcde1AE6sJ-BO8EIj8DWM8Hfm3tFm_nXrwNo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ای بی سی: رضا پهلوی ۱۰مرتبه درخواست دیدار با ترامپ را داشته که تمام درخواست‌ها رد شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128608" target="_blank">📅 10:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128607">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b03e93ff7.mp4?token=crh1u9-jBjqsF1u_0_LAg6mJUmYp1VwrUwhsg6KWxZ13loezPFGX1fap1OOXoc9yA02BRnXc6LTiWLuPrAwqfEqma8uLUrHswrhG16gnLK8akLyQBMUWCCRKEqzReG1UWsl_VblJZud4Z8oxqfT6H_bDBLDmBS6WVQLu83PQ6bfGemoI6KvMHYDjJ4GIy-BEmar5CFqx8xy2d-SDoN2DkX03wjrYe4bHcxOmjKfyCSABClI-idEgOPMwkwEZjdRRcTAdDxbEakpHkyHI4rKYwPR5oGu7M3YlWwgI25KBSY6rUuLKGh0KGXJOlce0dS0VB7uNKaJ4W3anxeN1KoHcsL0waJyp86C6q9kLXay1D7__lX5OZYe3nBg1W-E4yU2MmaaWmah1ctb1Gt65syOYBK4Ftmg0YuFct0t2FqwJvN6unOJuepmrBdJ1YSx-D9Bb2uT6bjSF_0a9GSjPCzD5m88bsdjaoyyIzQoUyQ_beQ6ZS60wyUGbeB0XFJpbYJ-Scr86wNPaB-xKaiD9bWoBKKUXsYzbwzg7_xtvlgP6bFBN0dic_wPtmj7s1SyHeXZw5LN3dr6ho1CMOtU_yOkmZc3Atte2MzTxn95lOCtAWYRTSpqyRg8kh3voGkmt39TBjN0Ld__DepwQF4HB3KoXd7q1ZLcT3y0rmWnyyGeaDys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b03e93ff7.mp4?token=crh1u9-jBjqsF1u_0_LAg6mJUmYp1VwrUwhsg6KWxZ13loezPFGX1fap1OOXoc9yA02BRnXc6LTiWLuPrAwqfEqma8uLUrHswrhG16gnLK8akLyQBMUWCCRKEqzReG1UWsl_VblJZud4Z8oxqfT6H_bDBLDmBS6WVQLu83PQ6bfGemoI6KvMHYDjJ4GIy-BEmar5CFqx8xy2d-SDoN2DkX03wjrYe4bHcxOmjKfyCSABClI-idEgOPMwkwEZjdRRcTAdDxbEakpHkyHI4rKYwPR5oGu7M3YlWwgI25KBSY6rUuLKGh0KGXJOlce0dS0VB7uNKaJ4W3anxeN1KoHcsL0waJyp86C6q9kLXay1D7__lX5OZYe3nBg1W-E4yU2MmaaWmah1ctb1Gt65syOYBK4Ftmg0YuFct0t2FqwJvN6unOJuepmrBdJ1YSx-D9Bb2uT6bjSF_0a9GSjPCzD5m88bsdjaoyyIzQoUyQ_beQ6ZS60wyUGbeB0XFJpbYJ-Scr86wNPaB-xKaiD9bWoBKKUXsYzbwzg7_xtvlgP6bFBN0dic_wPtmj7s1SyHeXZw5LN3dr6ho1CMOtU_yOkmZc3Atte2MzTxn95lOCtAWYRTSpqyRg8kh3voGkmt39TBjN0Ld__DepwQF4HB3KoXd7q1ZLcT3y0rmWnyyGeaDys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل، بزالل اسموتریچ:
در غزه، ما همچنان به پیشروی خود ادامه می‌دهیم. امروز کمی جلوتر رفتیم. ما در حال حاضر به 70 درصد نزدیک می‌شویم.
🔴
ما تقریباً 70 درصد نوار غزه را کنترل می‌کنیم.
🔴
غزه ویران شده است.
🔴
بدون غیرنظامی شدن، هیچ بازسازی‌ای وجود نخواهد داشت.
🔴
ما اکنون در حال آماده‌سازی چندین طرح هستیم زیرا باید حماس را نابود کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128607" target="_blank">📅 10:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128606">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
انهدام مهمات عمل‌نکرده در تبریز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/128606" target="_blank">📅 10:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128605">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
بلومبرگ: آمریکا آماده است در توافق صلح، منافع مالی گسترده‌ای به ایران ارائه کند؛ مانند حق فروش فوری نفت، دسترسی به صندوق توسعه‌ ۳۰۰ میلیارد دلاری و دارایی‌های مسدود شده خود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/128605" target="_blank">📅 10:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128604">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وزیر خارجه چین: توافق فعلی بین ایران و آمریکا آغاز راه است، نه نقطه پایان
🔴
وانگ یی در گفت‌و‌گو با همتای پاکستانی خود: توافق فعلی، آغاز راه است، نه نقطه پایان؛ از این رو، تداوم صلح در خاورمیانه و منطقه خلیج فارس همچنان به تداوم تلاش‌های همه طرف‌ها نیاز دارد.
🔴
چین نیز به روش خود به میانجیگری بین ایران و آمریکا پرداخته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128604" target="_blank">📅 10:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128603">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1b58f4916.mp4?token=kJ0np1SDLDwKxnYSEHpmt--0KdjU86nRYn3tTjAcmtXuQ2qrsPoGL-GbBAulM4CgN0lIgnTo2dMV1h8hyrQ6wmR9iKKm2Q71qpzSF6g1x3DOzuwWJiSzHe40kxnZ2JSTaqfcVMqbXyJ6FWX7lFD1F7CnV36dlvKh20ETOvqLR5OWMl5mK8SY3UnOxmGh5HkUeS2KJCE32G1yxEXTlU3pxgK9CQFLDgnCAHjyUxfGbocyoKrYoUJJVGO_LNz0VxF6pNvdTKMRqQvyeRh9kXidkt2beddaucGPwt--fbMp7vpNAbzkfcGEWlnADj1rz0i10BLELP5fHseLThwp9MWGag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1b58f4916.mp4?token=kJ0np1SDLDwKxnYSEHpmt--0KdjU86nRYn3tTjAcmtXuQ2qrsPoGL-GbBAulM4CgN0lIgnTo2dMV1h8hyrQ6wmR9iKKm2Q71qpzSF6g1x3DOzuwWJiSzHe40kxnZ2JSTaqfcVMqbXyJ6FWX7lFD1F7CnV36dlvKh20ETOvqLR5OWMl5mK8SY3UnOxmGh5HkUeS2KJCE32G1yxEXTlU3pxgK9CQFLDgnCAHjyUxfGbocyoKrYoUJJVGO_LNz0VxF6pNvdTKMRqQvyeRh9kXidkt2beddaucGPwt--fbMp7vpNAbzkfcGEWlnADj1rz0i10BLELP5fHseLThwp9MWGag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک پنس، معاون سابق ترامپ: «به نظر من بهتر است به نیروهای مسلح ایالات متحده اجازه دهیم کار را تمام کنند، تنگه را باز کنند و قابلیت‌های تهاجمی ایرانیان را از بین ببریم و به مردم ایران فرصتی واقعی برای آزادی بدهیم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128603" target="_blank">📅 10:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe43e0026a.mp4?token=q2eL1caH6gyzFQcVkhcnul2M9TyddQ6yBIOydl0ADlY_aebFytl-z78U9UHHxWb7rLxzHyrEIFn4Y8qpOJXwQ-byK4XJ50xTCDOIcgcsTCRqNMVM1czgA1n-CWC9Rfjq1ts6aqiYx40tOmF1gH51DuMwjfhbyT-aDzdGuX7671V3om99v-5rGqYEXAerYwNu6PBIvMWGDhe3ArCT3_dxMf-HtEW49NCh4WQYmAgRywrUm5-vbm6qzYNHa3biHDR0Gz5yZK7X02wC6l6RPQo3gXce4IHl2r_SNsaxXHsiwgssJHAlm_JqJ8Nn573q-rmL0eDN_ygI1n6_2n9723LP2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe43e0026a.mp4?token=q2eL1caH6gyzFQcVkhcnul2M9TyddQ6yBIOydl0ADlY_aebFytl-z78U9UHHxWb7rLxzHyrEIFn4Y8qpOJXwQ-byK4XJ50xTCDOIcgcsTCRqNMVM1czgA1n-CWC9Rfjq1ts6aqiYx40tOmF1gH51DuMwjfhbyT-aDzdGuX7671V3om99v-5rGqYEXAerYwNu6PBIvMWGDhe3ArCT3_dxMf-HtEW49NCh4WQYmAgRywrUm5-vbm6qzYNHa3biHDR0Gz5yZK7X02wC6l6RPQo3gXce4IHl2r_SNsaxXHsiwgssJHAlm_JqJ8Nn573q-rmL0eDN_ygI1n6_2n9723LP2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سرقت خودپرداز بانک با لیفتراک در بریتانیا
🔴
سارقان با یک لیفتراک تلسکوپی شبانه به شعبه بانک در کمبریج‌شایر رفتند و دستگاه خودپرداز را از دیوار کندند. پلیس اعلام کرد لیفتراک هم سرقتی بوده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/128602" target="_blank">📅 10:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ونس:  اگر ایران همان راهی را که عربستان سعودی رفت طی کند، ایالات متحده کمک خواهد کرد که کشوری موفق باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/128601" target="_blank">📅 10:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
وزیر دارایی اسرائیل:توافق با ایران بد است
🔴
ترامپ از منافع کشور خودش محافظت می‌کند و ما از منافع خودمان
🔴
باید بدانیم که چگونه این بحران را مدیریت کنیم و در عین حال، بر مواضع خود بایستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/128600" target="_blank">📅 10:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f45fe35652.mp4?token=IhRO0g0tdRzt7w3C1c966wEtvn0Sc_hM-fUP9HvxLVYgKiJwMbnM8VDe_suFaxTDrSV6mQQ-KxnGozx_qYl2EnuRjyEm5L2PGoLTU0FhdTKq17-eBO70iyrlVDjHpzquTgz9FN4k9QDXDuC_n4eGmT6x2iH1gmX8by0hCh-nWF-dKCaASB0KF1tbhqkJhMgARS1g7mWIafci73r0XgMz2EBrAxR9Xhx9XtIr5Jyy0wxc4iOs7ifu8PfXc7vgFJ_EKO00jfABA7zgYlozzMxCsvw6IKhBxOcpBQqrliRAny0YsS_GM00GTX2crhpAffgoHxzBgtVyj8nyxMmKNYjd8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f45fe35652.mp4?token=IhRO0g0tdRzt7w3C1c966wEtvn0Sc_hM-fUP9HvxLVYgKiJwMbnM8VDe_suFaxTDrSV6mQQ-KxnGozx_qYl2EnuRjyEm5L2PGoLTU0FhdTKq17-eBO70iyrlVDjHpzquTgz9FN4k9QDXDuC_n4eGmT6x2iH1gmX8by0hCh-nWF-dKCaASB0KF1tbhqkJhMgARS1g7mWIafci73r0XgMz2EBrAxR9Xhx9XtIr5Jyy0wxc4iOs7ifu8PfXc7vgFJ_EKO00jfABA7zgYlozzMxCsvw6IKhBxOcpBQqrliRAny0YsS_GM00GTX2crhpAffgoHxzBgtVyj8nyxMmKNYjd8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وضعیت جوریه که حتی رهبر جمهوری خواهان سنا هم مثل من و شما از مفاد تفاهم نامه خبر نداره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128599" target="_blank">📅 09:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47bcf91b13.mp4?token=Y7TRuq8OACU3pjkoUErMLHJCHnPgA3pPIKDglhyCAc0fdiITUJaOdqBV5mtSueEqggHVYEZszxjTW3NaApbuuGR8kgv7QXRw2prjpnHrEPfE7dFHVpeCpkuu3_vk-WMlIKVEiJg3PvTuaw65xDHF-_ud34f6-SgG8BaaSKxJtUSvzVrjMMW9loHgNdZmgxay7kOKR3J2528l85TtkmJ4TU3VBLwXAiA7YrShFUaZuecgyxY3-_jpr2UAdNe5eEEUVQaZ1Od5W3jA_00pgP2sfs-y2-PY5MifA1W7ANNkpIQ3Vzqz6lZ5-dvqmTgfUUEJK3oeu_YxZBpRHyjpf2cBgFLozLDNQoaE5VmCk2mK-TuwVCMNqIj4W5VBIcaYFqlKpzMdc2Bm3spllsPaMnZWbhuoxjuShlHpce6Yf27arG1z5D6fMMS7iW7uuHOwXQPmR7WJqmUDCkV2kmIRllX5j3RAY1bkuky4lTgcJ4g3GNELKR1OgzDdtJZPuo11nJkFiIOZLSTxVp1ZMO7srGonyzavUDF0GWkFtMdXtwrOnL0ZKA7NRO10y0vZtOJRGHyksEWD6gW_9eW4EzljyHDVIP9ircqPysZTOBQFCs48XjpafQBWvBufI8-Gvnm7_FHRExZukatu9dd0EI-WgffQfLDsnDBpD2A0bsOtZ2Xzm2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47bcf91b13.mp4?token=Y7TRuq8OACU3pjkoUErMLHJCHnPgA3pPIKDglhyCAc0fdiITUJaOdqBV5mtSueEqggHVYEZszxjTW3NaApbuuGR8kgv7QXRw2prjpnHrEPfE7dFHVpeCpkuu3_vk-WMlIKVEiJg3PvTuaw65xDHF-_ud34f6-SgG8BaaSKxJtUSvzVrjMMW9loHgNdZmgxay7kOKR3J2528l85TtkmJ4TU3VBLwXAiA7YrShFUaZuecgyxY3-_jpr2UAdNe5eEEUVQaZ1Od5W3jA_00pgP2sfs-y2-PY5MifA1W7ANNkpIQ3Vzqz6lZ5-dvqmTgfUUEJK3oeu_YxZBpRHyjpf2cBgFLozLDNQoaE5VmCk2mK-TuwVCMNqIj4W5VBIcaYFqlKpzMdc2Bm3spllsPaMnZWbhuoxjuShlHpce6Yf27arG1z5D6fMMS7iW7uuHOwXQPmR7WJqmUDCkV2kmIRllX5j3RAY1bkuky4lTgcJ4g3GNELKR1OgzDdtJZPuo11nJkFiIOZLSTxVp1ZMO7srGonyzavUDF0GWkFtMdXtwrOnL0ZKA7NRO10y0vZtOJRGHyksEWD6gW_9eW4EzljyHDVIP9ircqPysZTOBQFCs48XjpafQBWvBufI8-Gvnm7_FHRExZukatu9dd0EI-WgffQfLDsnDBpD2A0bsOtZ2Xzm2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس درباره ایران: دلیل اینکه متن تفاهم‌نامه را منتشر نکرده‌ایم این است که برخی از میانجی‌های ما؛ پاکستانی‌ها و قطری‌ها؛ از ما خواسته‌اند که این موضوع را به ترتیب درست انجام دهیم.
🔴
حساسیت‌هایی در جهان عرب و مسلمان وجود دارد که ما در تلاشیم به آن‌ها پاسخ دهیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128598" target="_blank">📅 09:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128597">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a337c7ba.mp4?token=ZJ17jScNpvBJUA50so5-8KEcg7HPMlaUBYK18NajD7PdZEXMGqAjlIHRwP9bAVGF8M2oh9rXVwqNJzdyUFaW3AISSQNqf2r2qKmsE4M2tjchGGcI0QxrrLuwH_e4Fg1cAaN-Q4PmBHR5vYyHAejnbddQ2RyZn7s_paQ0TMuM3XJUMaFJKxN-nhiEgIxoq5GTFmjWkRz70e3fv13LuOYujgWHhD_z1SBJxdwybGYpS7U4Me2peOAQwEodx4CCg2SZ4UHiF8RgWvlLffk2AXOEVnhWMCyWNATNhSc_x7Ebj3B-NhFP4vx70zxdodRHakBdQATQ7HILu6XbJtFtfDpz6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a337c7ba.mp4?token=ZJ17jScNpvBJUA50so5-8KEcg7HPMlaUBYK18NajD7PdZEXMGqAjlIHRwP9bAVGF8M2oh9rXVwqNJzdyUFaW3AISSQNqf2r2qKmsE4M2tjchGGcI0QxrrLuwH_e4Fg1cAaN-Q4PmBHR5vYyHAejnbddQ2RyZn7s_paQ0TMuM3XJUMaFJKxN-nhiEgIxoq5GTFmjWkRz70e3fv13LuOYujgWHhD_z1SBJxdwybGYpS7U4Me2peOAQwEodx4CCg2SZ4UHiF8RgWvlLffk2AXOEVnhWMCyWNATNhSc_x7Ebj3B-NhFP4vx70zxdodRHakBdQATQ7HILu6XbJtFtfDpz6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس درباره ایران: ایرانی‌ها در موقعیتی هستند که می‌گویند می‌خواهند تعهدات بلندمدتی به ایالات متحده و کشورهای عرب خلیج فارس بدهند تا رابطه‌شان را تغییر دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128597" target="_blank">📅 09:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128596">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f62be1a9ab.mp4?token=GrGap3bHLjelKp_kOV9UtkAJmFjlgT2WBxVwD-PJWx0fPrKpVeU60Wl3EkIm00y83fIR_hL-PpQRaGjsVqJxQCD1Z8-RO1HCNctdiixHUUQM-9vfgrQx50orUeGI_R_RJMTwEwwKVXwRLcx19MyJFtjSKJvMBzXcHFFryv08fyuecloykXWPIBpUTF8HR_2CkVVSQ_nN9pkW8ur9yMt96nhDLLUALldchmdDgrQ4AmDgYtRUTNi0oZhz5M-_BrmcGfzUTyPYg71rGjIPqE_uuXBbZS8ZFaOqcEn6DR-bkkfzXYRIgfIfiK7zexasWJQsxdahpMkZY0WldZ8XQ_Zz3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f62be1a9ab.mp4?token=GrGap3bHLjelKp_kOV9UtkAJmFjlgT2WBxVwD-PJWx0fPrKpVeU60Wl3EkIm00y83fIR_hL-PpQRaGjsVqJxQCD1Z8-RO1HCNctdiixHUUQM-9vfgrQx50orUeGI_R_RJMTwEwwKVXwRLcx19MyJFtjSKJvMBzXcHFFryv08fyuecloykXWPIBpUTF8HR_2CkVVSQ_nN9pkW8ur9yMt96nhDLLUALldchmdDgrQ4AmDgYtRUTNi0oZhz5M-_BrmcGfzUTyPYg71rGjIPqE_uuXBbZS8ZFaOqcEn6DR-bkkfzXYRIgfIfiK7zexasWJQsxdahpMkZY0WldZ8XQ_Zz3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای "سسنا ۶۸۰ سایتیشن لاتیتود" هنگام ورود به تگزاس منفجر شد
🔴
تیم‌های اورژانس به سرعت به محل حادثه رفتند.
🔴
ورود به پنجره کابین خلبان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/alonews/128596" target="_blank">📅 09:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/057ad2526c.mp4?token=IpbCQ1H7c2WXWKlqfw97IS6AYWq16xG7AlB-1kChetQ3qtJvhueNWMCj2vACVAhaidz_7JOR4bGnciRauV8ZWA-sVhpX3KfSS15oZFYyaViXL24UjpZ3IkSkHVyoG2Si-LRAEPy3_tMm6EkTdoWrhlIisGK8BXe-ietO5jpF3XuVPs8QhqFabcPAUfB10F9muniePGLrEbOWi_tvtv_OqI8KQQZNHyGs-sX9ctcHt5TzvhzFLHw2aQ3izHksgK-lHstczKvjC_UNpf9XPeC3UeL7wkQMZBBucW2G5WGokgndK-oISzSzV7QJfieTybduQZ2yWoa5IGtukdT6i3YTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/057ad2526c.mp4?token=IpbCQ1H7c2WXWKlqfw97IS6AYWq16xG7AlB-1kChetQ3qtJvhueNWMCj2vACVAhaidz_7JOR4bGnciRauV8ZWA-sVhpX3KfSS15oZFYyaViXL24UjpZ3IkSkHVyoG2Si-LRAEPy3_tMm6EkTdoWrhlIisGK8BXe-ietO5jpF3XuVPs8QhqFabcPAUfB10F9muniePGLrEbOWi_tvtv_OqI8KQQZNHyGs-sX9ctcHt5TzvhzFLHw2aQ3izHksgK-lHstczKvjC_UNpf9XPeC3UeL7wkQMZBBucW2G5WGokgndK-oISzSzV7QJfieTybduQZ2yWoa5IGtukdT6i3YTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم‌اکنون حمله هوایی اسرائیل به النبطیه الفوقا و شلیک موشک به اطراف کفرتبنیه در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/alonews/128595" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128594">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
شریعتمداری: درگیری ما و امریکا، ماهوی و وجودی است؛ تفاهم اخیر، اصل درگیری ما را تغییر نمی‌دهد!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/alonews/128594" target="_blank">📅 09:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128593">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
با فعال شدن کریدور جدید دریایی بین قشم و عمان پس از جنگ، محموله‌های خودروهای خارجی به این جزیره سرازیر شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/128593" target="_blank">📅 09:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4M0TRVwL6CvtdRUwFt0vLaYBpWOoevvn106rDHUBSJa7RWB-RwqYlKgFqcVz3soX-MimkSqz6T6Ss_HeoiIBNbOMYrFMnhfNEtjCWbKGgTRx2yg9SnCxZ9-BlpfZOACsVp0ZR2ByOshqP1W2bhuNRZMkWUN2GuPwcm4-tLykbBIXx4HnZFl6BwURK7FL9oWloVjHKLr8TowOSLDV3OzmQGHt7uAPyEag__Cje6U30SSn1dDBnYAxEZPUr5snMtG1WcPFzTtXVOj68RhKXpWtDqEMFYtSgvSphZBrle3uBHIGRETBXn6kYZIEudipMEk5r4YFbM-CKexE-iaDD1S4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل اعلام کرد یک انبار تسلیحات جدید حزب‌الله حاوی ۵ تن مواد منفجره و ده‌ها پهپاد انتحاری را کشف کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/128592" target="_blank">📅 09:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a5486709.mp4?token=N6M7ZOXf_yhFsmQqSNB2L_Be0T1EcZVnhwwqUMKwZcwvwtP7ppCLITA85uu01nBKYgmOy1NfLSWpmMTpRGZ-ZoWRMQo-ozNbgoBd-F_HZ_Zs4C7igDvQ2_0Z5X-C_BCrPSixAuwit26tDso3PSzt-FGagaOBKLALPpwtmreCBK24yq07GjkSox1-HkZpOMWORgXAllZMIS5NocE1GM53qFt7YNvGIUdHhNtWSsZo83QJmqFEsH4GAAUqAfQfMjOxQV559pd8dykMYpF6qmVUeYp4ePRje68clhYt2WMLzVrBCTDnDxuIV9Dep2JHfi15l354T_s8UQrVxOk_jDSrNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a5486709.mp4?token=N6M7ZOXf_yhFsmQqSNB2L_Be0T1EcZVnhwwqUMKwZcwvwtP7ppCLITA85uu01nBKYgmOy1NfLSWpmMTpRGZ-ZoWRMQo-ozNbgoBd-F_HZ_Zs4C7igDvQ2_0Z5X-C_BCrPSixAuwit26tDso3PSzt-FGagaOBKLALPpwtmreCBK24yq07GjkSox1-HkZpOMWORgXAllZMIS5NocE1GM53qFt7YNvGIUdHhNtWSsZo83QJmqFEsH4GAAUqAfQfMjOxQV559pd8dykMYpF6qmVUeYp4ePRje68clhYt2WMLzVrBCTDnDxuIV9Dep2JHfi15l354T_s8UQrVxOk_jDSrNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیراندازی مرگبار در بیمارستان ویلیمینگتون ایالت دِلاوِر آمریکا، یک قربانی برجای گذاشت و عامل مسلح حادثه همچنان متواری است.
🔴
پلیس اعلام کرد نیروهای امنیتی در حال انجام عملیات برای یافتن و بازداشت فرد مهاجم هستند و تحقیقات درباره جزئیات این تیراندازی ادامه دارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/128591" target="_blank">📅 08:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128590">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6789100e6.mp4?token=rI-gN2WurR9bPmHVULRTd-42DpcMMX1a3k14wo5f-wN22TlYsC4D3zolnxbkV5EsDfkB9SH2Mv_rJAGJpP9PSrHxEdF5DbzKOndVL8OzU6YidBwCJc6e1zdrUsG1jM2XdMzNcuK3ruwFIEZxxlOUXsy1A40Td-YVbJWccjWb0QyNHsK3foW5itd0TwiYq16m601Fx7_cEzgppvU8xAy7kWH0bIqX2OAqVgI8yTWx09fAu_PLURv_COlj11ZTt9gmOgbR4VV6XsT7O66_u69OHVtQbt00qwIb5xgFYyL7ko7r3Ysu1sLglUf5GAmFZkF1f-r9ouP8sK5ciAYzanQc4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6789100e6.mp4?token=rI-gN2WurR9bPmHVULRTd-42DpcMMX1a3k14wo5f-wN22TlYsC4D3zolnxbkV5EsDfkB9SH2Mv_rJAGJpP9PSrHxEdF5DbzKOndVL8OzU6YidBwCJc6e1zdrUsG1jM2XdMzNcuK3ruwFIEZxxlOUXsy1A40Td-YVbJWccjWb0QyNHsK3foW5itd0TwiYq16m601Fx7_cEzgppvU8xAy7kWH0bIqX2OAqVgI8yTWx09fAu_PLURv_COlj11ZTt9gmOgbR4VV6XsT7O66_u69OHVtQbt00qwIb5xgFYyL7ko7r3Ysu1sLglUf5GAmFZkF1f-r9ouP8sK5ciAYzanQc4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی جنوبی ارتش آمریکا از حملۀ مرگبار به یک شناور در آب‌های شرق اقیانوس آرام خبر داد؛ اقدامی که جان یک سرنشین را گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/128590" target="_blank">📅 08:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128589">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
تنکر ترکرز: ۳.۸ میلیون بشکه نفت خام ایران از محاصره آمریکا عبور کرد
🔴
تارنمای تنکر ترکز بامداد چهارشنبه گزارش داد، دو ابرنفتکش ایران که مجموعا حامل ۳.۸ میلیون بشکه نفت خام هستند، از محاصره آمریکا عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/128589" target="_blank">📅 08:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
منابع عربی: اسرائیل حومۀ شهرک نبطیه‌الفوقا در جنوب لبنان را هدف حملات قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/128588" target="_blank">📅 08:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128587">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وبسایت خبری سمافور: مارکو روبیو، وزیر خارجه دولت ترامپ با انعقاد یادداشت تفاهم نامه با ایران مخالفت کرده و هیچ اظهار نظری درباره رسیدن به توافق با ایران نمی‌کند.
🔴
وزیر خارجه آمریکا امیدی به رسیدن به توافق هسته‌ای در مذاکرات با ایران پس از امضای یادداشت تفاهم نامه ندارد و تاکنون درباره امضای یادداشت تفاهم نامه با ایران کاملاً سکوت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/alonews/128587" target="_blank">📅 08:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128586">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1Snqp7yeZuoBLJ6YBV06NaVKIrm-NOWKv-cJVGWn3h3-XSjsdwDVKIGTTOQvaI26eud3yqQCbASc51sKPz99dMSXJRAOHkpoENEVWb0UxcaKeAIFjQ4Jwz5xiZR-fMR8IeQY-MTiZOD5c3hqBYmYZXZ8azMvEAZgSvSgiEN1o16INzVZUZfS7AWK_CUQ4DXwAROuPdl4aTo2cfQxw2VFV9fV4zDRKpTc3iikeZV0vxjpSP58-Gjw5UJ0GolYO2L9ygbG8mu08qpZdEQk8NMVW-qHpVxzL-pDlAHRh5MjhdUrq-G7nx5BgK0j520wJCSatDC7HDVAQTj3FSfC3berw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: به گفته مقامات آمریکایی، معافیت فروش نفت ایران فقط شامل محموله‌های نفتی می‌شود که قبلاً بارگیری شده است و شامل مجوز گسترده‌تر برای از سرگیری فروش نفت ایران نمی‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/128586" target="_blank">📅 08:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDdz0PxSgt5Oc4mP7ErzpGEBvFNLYL7nesKf-PohOMuyq_Vk7P9LWS5GYUXdQLA2VomLLekpl9_Y-e3TQ3SN7vjxFJcgXGw-fjEi3AtzTQnSnlq4vRYf8b7i1oJxlC29Xt7iK2i59j0Icxlw2pU8Zp9_7Sq3uxD7UM0l2JJneKW3dr_Y5Gl1u4r_07DBpWquYjlKzgCNA-R1iCxYQkP5o19q57N4dZJVZUAKraIYsSBuk0JHcUtA97PB4otphdusiXCGoh5HmIHojD5CE7hLJ558RpitiUDyPSQlvZ27Jx6hls1Fu6MDM-RGYJxlhGt-g5Eg40Wr0SyRw7sd7glv3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید:
«نه سلاح هسته‌ای، نه لغو کامل تحریم‌ها, نه پول»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/128585" target="_blank">📅 02:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgecfJfuavGNKvg23RMKniyFXtzPpMK3wGHHlNd9xpaQ9lX383_QZmM_BSzwXQ3HTdO2gHUZp6mqM5T1HShLVrpCrAVVt6yP48HPicwXQM2qQHJrtWB_twcHvvxZk0tXrVnS7d_UPFcECkMteonuuaENP7sE7Qw65pFzPk30hRint1GoxAD61NPJa5zZfmKzAdQouesx_9SztQudPWufYBZa6l23MHBrfdwSOOQ6rdDZd_f-BGSaBrHhacMc2pcyAvW3IMnOcfpo0RgnH6egTFl-OudhkTmWYlspgXwVApUlLDWezDh61lRV-WkxETSZ3MzueX-xIQiVXg4QUfiBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنای آمریکا به محدود شدن اختیارات رئیس جمهور در جنگ رای نداد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/128584" target="_blank">📅 02:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128583">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LQv_i_dGAx9a9WpMFckpqldapl65q3mGnfgAeHichmR_6WWH2cTCvxFpGlZvkdC8GtK6awiXmQSkyHxLmTI63w8uCCoJJ5_YHIEnvr4F1udDanZR8e3DCLbaRUGA5Sxv_to4R--I0V932q9ncPVSbU8ktSr7Gvvmx0o8civ2tzshJG1HSajG4SbgnPDdgW4ER1oU0idds35s7Df6dnCJCKM6qWc4HdycQ9f-FBpFlmAvnbS5chgTwq6JQKNwk2w-S5sUXqhXw8mzDQGNwAeN66lBao596l98MW1EVYdpEsqUFlaXcFceOliurUNbKVxFFyrJfp49vB1r-Dir9LgPXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاملا هریس،معاون رئیس جمهور پیشین آمریکا:
«هر مذاکره‌ای که در جریان باشد ترامپ به نقطه‌ای خواهد رسید که در برجام به ان رسیدیم و این چیزی بود که خودش پاره‌اش کرد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/128583" target="_blank">📅 02:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128582">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a96e36d925.mp4?token=OJOSlJwv34OzvVFf5HHBJYROQ2BsA4_MG5ZCF2rv4i9ZLw70w0YSQWZRoexp51-9Ssj7vTboDRGUu0ZrcOkk7Z7jA2c3FjpJEFi8AJ8mSpp4k-BXT2BsR5wKh52UHdkYLkZm2ARtqDOdS5UjCFUn3qZuLO60nNp0LBl8SIpcH8OqgzV7vUJNrupCFXLLNdTHgDBhpLfr3aglN-xvoowNuiXvrWJnoeSfAXh1lPLxld-5f6ULBI-cE_mmFVDq9Bnk7Yl7G6tidWmxPTPTjBn3RAWmLmLn9M0uTca7hlSMU_CWIGgkn55Uv4jyO3UJ0q5URq_iTNCRWDD_Ff9bWVCUTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a96e36d925.mp4?token=OJOSlJwv34OzvVFf5HHBJYROQ2BsA4_MG5ZCF2rv4i9ZLw70w0YSQWZRoexp51-9Ssj7vTboDRGUu0ZrcOkk7Z7jA2c3FjpJEFi8AJ8mSpp4k-BXT2BsR5wKh52UHdkYLkZm2ARtqDOdS5UjCFUn3qZuLO60nNp0LBl8SIpcH8OqgzV7vUJNrupCFXLLNdTHgDBhpLfr3aglN-xvoowNuiXvrWJnoeSfAXh1lPLxld-5f6ULBI-cE_mmFVDq9Bnk7Yl7G6tidWmxPTPTjBn3RAWmLmLn9M0uTca7hlSMU_CWIGgkn55Uv4jyO3UJ0q5URq_iTNCRWDD_Ff9bWVCUTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا رب روا مدار روزی گدا معتبر شود
@AloSport</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/128582" target="_blank">📅 01:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128581">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzHheEk5GiNTXKgAKaweaOlNtEy9Im56AJKsXOyrvolCmbiieVW4n6A5h0DEL_tFPFj9ygBsWYcGuvsQRdwJUkEPrTL5W6fC3F06AsY-Ck4rjYpd7bwcG2Ms3QBcafBSG1rNvjCgBHO64Pr-YlIY2SqVIOug7iZhCRQnpQiags54Wfrjjml55Ne-QDTV0XelU_KG6jYkdKwsoiUL3MYgonOzVL9bItxWm1HKvKI8csyE0B02XQrsfk8J5okpAJ-Q3S6uQjpl-RWhVkUabPf2yl8BA2IG2bUSFCaIoI-J9zf8qeSKi4TpWEPz6JQQYnED7IopetQFX_tDsSYoc-OEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارش شبکه خبری ان‌بی‌سی، سپاه پاسداران انقلاب اسلامی از زمان امضای دیجیتال تفاهم‌نامه در روز یکشنبه، هر شب پهپادهای متعددی را پرتاب کرده است
🔴
یک مقام آمریکایی می‌گوید که این پهپادها توسط سپاه پاسداران انقلاب اسلامی پرتاب می‌شوند، در حالی که نیروهای آمریکایی آن‌ها را قبل از اینکه بتوانند به کشتیرانی تجاری، کشتی‌های نظامی ایالات متحده یا پرسنل در منطقه تهدید کنند، رهگیری کرده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/128581" target="_blank">📅 01:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128580">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cf13291d.mp4?token=EfRYHXPBooPavGtKAD31aaBOFU-wR9M_q4KWwC-oxn_Rhmo4Fhg2JP1jsh9zyHntA_ZoNOkKoEcNoPaKro1x0KqN8HuHnj7kDOguuHNPkYQ02FNqyoykzhkz2cckE7sA9ywc9Aj7wZ-pRzGs-gVaEtLgkbmkBJtcOmaoGN2Am6ASYdFSdRMH-KykUWzU_hdkYpyvt45pPMkRW1swbOzdG4CCAfZ51sxlGTJ55JPkxDwvj0kBxIV02ZEGokiYWJwuDzObeoZ3HMkr1cUNLViOJJ7jRD09ObzDreTk3diQwyZ-1LWLOfUzD5tXjy7-zGaVMLInaMOdNBH79GN8DEhmVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cf13291d.mp4?token=EfRYHXPBooPavGtKAD31aaBOFU-wR9M_q4KWwC-oxn_Rhmo4Fhg2JP1jsh9zyHntA_ZoNOkKoEcNoPaKro1x0KqN8HuHnj7kDOguuHNPkYQ02FNqyoykzhkz2cckE7sA9ywc9Aj7wZ-pRzGs-gVaEtLgkbmkBJtcOmaoGN2Am6ASYdFSdRMH-KykUWzU_hdkYpyvt45pPMkRW1swbOzdG4CCAfZ51sxlGTJ55JPkxDwvj0kBxIV02ZEGokiYWJwuDzObeoZ3HMkr1cUNLViOJJ7jRD09ObzDreTk3diQwyZ-1LWLOfUzD5tXjy7-zGaVMLInaMOdNBH79GN8DEhmVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تیکه عادل به خوش چشم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/128580" target="_blank">📅 01:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128579">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
خبرگزاری نیمه معتبر تسنیم: به گفته منابع اطلاعاتی آمریکا، این احتمال وجود داره که جمهوری اسلامی در واکنش به حملات اسرائیل در لبنان، بدون هیچ هشدار قبلی یک حمله غافلگیرکننده علیه اسرائیل انجام بده.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/128579" target="_blank">📅 01:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128578">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdbbf14f6e.mp4?token=czIdhEVCNSwMc4kBV_Nv84xeCCgj52rtdIE4ZzXAnQmbRXwibakdToeQT4vLcH7LSJzWhR_X_1yratdkt9OQt3jlxPtkOUuQPSZ92A_jAVAJ436OOFyCo9nmyjS9giPytcFvNg1U8lotuqwfReMIX4ID4rKnZ00hGDsjBoHnqqNMFKXRLYxtQypbeI4OWywMns83aYeLG_xGWDKZ3fdjt7wlpsF-eaVZSKiXbDeemcQGBrVnpI1doEX1w4D2e9G6xdeK1GgX8X9P2dEkMdI1NTFKHJ7QV7orpDPnWJaF7IZBx5W-FlSnw8uuyEbKYNafM2msBUDJ6c-fCB_CA7VYVFVuW4ur-fbjB5c8RaDH_czJnhSGOlFhlUKxm0FwOi3vBObdy486LNi3GLr1KRs-n2Fkwxt4-wbqhkCeDIRJbd4U_SRsnqlYFRqLG_dRWhlHAjF9VfGH8EwwTfx0Q7d5F02z1tpdyOcn4yYJHn7HZNTUCSnk5x8I6249ycPNkNUjdpbgu3hnafxokhc3_2qxqtjKo3ZgN0kbY6aK3EzVhM8SdLLag3P-t4XUweDTPSujT--U56RthsdYh4AUi1o61oSBBRtAzRO_inKUbXr6LJxOtWEyMKJAnn5VLEsCCkwd7uzPEw8bxRQHbHJQmqQ-8N6N0e9lShXOK4KM9rhlhIM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdbbf14f6e.mp4?token=czIdhEVCNSwMc4kBV_Nv84xeCCgj52rtdIE4ZzXAnQmbRXwibakdToeQT4vLcH7LSJzWhR_X_1yratdkt9OQt3jlxPtkOUuQPSZ92A_jAVAJ436OOFyCo9nmyjS9giPytcFvNg1U8lotuqwfReMIX4ID4rKnZ00hGDsjBoHnqqNMFKXRLYxtQypbeI4OWywMns83aYeLG_xGWDKZ3fdjt7wlpsF-eaVZSKiXbDeemcQGBrVnpI1doEX1w4D2e9G6xdeK1GgX8X9P2dEkMdI1NTFKHJ7QV7orpDPnWJaF7IZBx5W-FlSnw8uuyEbKYNafM2msBUDJ6c-fCB_CA7VYVFVuW4ur-fbjB5c8RaDH_czJnhSGOlFhlUKxm0FwOi3vBObdy486LNi3GLr1KRs-n2Fkwxt4-wbqhkCeDIRJbd4U_SRsnqlYFRqLG_dRWhlHAjF9VfGH8EwwTfx0Q7d5F02z1tpdyOcn4yYJHn7HZNTUCSnk5x8I6249ycPNkNUjdpbgu3hnafxokhc3_2qxqtjKo3ZgN0kbY6aK3EzVhM8SdLLag3P-t4XUweDTPSujT--U56RthsdYh4AUi1o61oSBBRtAzRO_inKUbXr6LJxOtWEyMKJAnn5VLEsCCkwd7uzPEw8bxRQHbHJQmqQ-8N6N0e9lShXOK4KM9rhlhIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جون بولتون:
به نظر من این برای ایالات متحده معامله بسیار بدی است.
ترامپ به پیامدهای ژئواستراتژیک این معامله فکر نمی‌کند.
او فقط به یک چیز فکر می‌کند. او می‌خواهد تنگه باز بماند. او می‌خواهد نفت خلیج فارس در بازارهای بین‌المللی عرضه شود.
او می‌خواهد قیمت بنزین در پمپ‌ها پایین بیاید. این تنها چیزی است که برایش مهم است.
ما نمی‌دانیم در این معامله چه چیزی وجود دارد. اگر معامله‌ای عالی بود، در دسترس عموم قرار می‌گرفت.
به نظر من این تقریباً همان چیزی را به شما می‌گوید که نیاز به دانستن آن دارید.
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/128578" target="_blank">📅 01:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128577">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d586f8ae.mp4?token=BTWXXL5GRrN_ghEU17325G1GezAQDZqzP9dyB0y5aZaXYUad3OKEeuGD-iSTDKIVmkoI1ng1M4KR6anKwQy_GDJbu2lOL2_713Z3FY_fhb2Kd-Zp0Xhm7TucmAnK-gp3Siqv-4FXOkU8vtnjW1tGUqUW2jh_Xery7nAU82WPW3VMc2vRaden0T3qB5I8wK957LPdrPBDQxAtRvNJfGp1jwWP2zAjby5siGmW4nBEF_jK7UU8kcp-2hQm5lhoN8Ea3nAtwBriEuyaDLFdikj5YUpp1ffw4HSY2Vp6CzkriLKuAgXmEIJ6H4tjc8YHfd7ZAsK-eNDL0j9AISNJq9lGnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d586f8ae.mp4?token=BTWXXL5GRrN_ghEU17325G1GezAQDZqzP9dyB0y5aZaXYUad3OKEeuGD-iSTDKIVmkoI1ng1M4KR6anKwQy_GDJbu2lOL2_713Z3FY_fhb2Kd-Zp0Xhm7TucmAnK-gp3Siqv-4FXOkU8vtnjW1tGUqUW2jh_Xery7nAU82WPW3VMc2vRaden0T3qB5I8wK957LPdrPBDQxAtRvNJfGp1jwWP2zAjby5siGmW4nBEF_jK7UU8kcp-2hQm5lhoN8Ea3nAtwBriEuyaDLFdikj5YUpp1ffw4HSY2Vp6CzkriLKuAgXmEIJ6H4tjc8YHfd7ZAsK-eNDL0j9AISNJq9lGnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری : گزارش‌هایی هست که می‌گن قطری‌ها دارن به ایرانی‌ها پول می‌دن درسته؟
🔴
ونس : درست نیست، من اون گزارش رو دیدم
🔴
مجری : هیچ پولی جابه‌جا نشده؟ ایران حتی یک دلار هم از کشورهای حاشیه خلیج فارس نگرفته؟
🔴
ونس : درسته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/128577" target="_blank">📅 00:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128576">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edcf3e3aaf.mp4?token=iuU_lI94eOXeYtb-PMjp3UK02QtdxY4m9uO685LXRtezx-GLaJVtlm7ShTigBhvX9yu6Ai6uLSNnyBE4Jr51jYi8LyMNVKO22XC7kiNaYamOIYNEdJPc06FblfIymVBZErqcsG3xNCiJu4fKns8X5t1FU8OCuOOQSadjg4lZozAg6YU50HTd4SVkOGVd4JNaBGtCPp_U_Cf1PGBrmLgExIEFxlX_-Yv6TyV4xMEUIoGRQVFvKVtlTAJftQZfjm_pHWfpvHZdz-GNpBAr_9dAPVp36oVPPVvX3AK0mexoxgGDk7aNkv4Aim4eEfAWRAeuiQJhumU4PJMTnGWdktWOMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edcf3e3aaf.mp4?token=iuU_lI94eOXeYtb-PMjp3UK02QtdxY4m9uO685LXRtezx-GLaJVtlm7ShTigBhvX9yu6Ai6uLSNnyBE4Jr51jYi8LyMNVKO22XC7kiNaYamOIYNEdJPc06FblfIymVBZErqcsG3xNCiJu4fKns8X5t1FU8OCuOOQSadjg4lZozAg6YU50HTd4SVkOGVd4JNaBGtCPp_U_Cf1PGBrmLgExIEFxlX_-Yv6TyV4xMEUIoGRQVFvKVtlTAJftQZfjm_pHWfpvHZdz-GNpBAr_9dAPVp36oVPPVvX3AK0mexoxgGDk7aNkv4Aim4eEfAWRAeuiQJhumU4PJMTnGWdktWOMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : اگه دونالد ترامپ حتی به عنوان رهبر عالی ایران هم انتخاب می‌شد، دموکرات‌ها باز هم می‌گفتن آمریکا شکست خورده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/128576" target="_blank">📅 00:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128575">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
جی دی ونس : روز جمعه مراسم امضای رسمی انجام می‌شه و این موضوع عملاً شروع این مذاکرات رو کلید می‌زنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/128575" target="_blank">📅 00:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128574">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aa0b57d8f.mp4?token=GHP3eOmHKXDFoaAZOttZ-Dn6BiiexfI_Dp7Ak_jUfMggtVHIRwKCYVq4WzlI1mdAsVeA8cs9kREovnrmMDS22VobacV6FaF9Y_TO1eKqF7Z6QY0LjXoxTe_D1lgUirCaZQq5QmEeSfJ_iAXgb5bgHGylRHKYMEKiD_novlFQV-vSO99bEY8LEkY8IswOHjxIWmIwxbxHEPXgtq5YR6CpYXepONBLIhLVfrdgYGBw2s_tZOr2Kf3qsWtW3jgT6Wq1HWXa7_Fnxbsl90rODuByBlZWrGjIOmT_kAJi23gKhCPli4vyQeImgGT0Wkcwnpc-BYGodbDH5tP7Ho5DBQOPpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aa0b57d8f.mp4?token=GHP3eOmHKXDFoaAZOttZ-Dn6BiiexfI_Dp7Ak_jUfMggtVHIRwKCYVq4WzlI1mdAsVeA8cs9kREovnrmMDS22VobacV6FaF9Y_TO1eKqF7Z6QY0LjXoxTe_D1lgUirCaZQq5QmEeSfJ_iAXgb5bgHGylRHKYMEKiD_novlFQV-vSO99bEY8LEkY8IswOHjxIWmIwxbxHEPXgtq5YR6CpYXepONBLIhLVfrdgYGBw2s_tZOr2Kf3qsWtW3jgT6Wq1HWXa7_Fnxbsl90rODuByBlZWrGjIOmT_kAJi23gKhCPli4vyQeImgGT0Wkcwnpc-BYGodbDH5tP7Ho5DBQOPpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لیندسی گراهام
: صادقانه بگویم، عربستان سعودی و اسرائیل خیلی به ترامپ بدهکارند.
اگر این دو کشور با هم صلح کنند و روابط اقتصادی و تجاری برقرار کنند، این اتفاق هم برای منطقه و هم برای جهان مفید خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/128574" target="_blank">📅 00:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128573">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سناتور لیندسی گراهام: مطمئنم که رئیس‌جمهور ترامپ توافق بدی را امضا نخواهد کرد
🔴
یادداشت تفاهم (MOU) آن‌طور که معاون رئیس‌جمهور و دولت توضیح داده‌اند، بسیار امیدوارکننده به نظر می‌رسد.
🔴
من ترجیح می‌دهم مسئله برنامه هسته‌ای ایران از راه دیپلماتیک حل شود. تردید…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/128573" target="_blank">📅 00:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128572">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سناتور لیندسی گراهام:
مطمئنم که رئیس‌جمهور ترامپ توافق بدی را امضا نخواهد کرد
🔴
یادداشت تفاهم (MOU) آن‌طور که معاون رئیس‌جمهور و دولت توضیح داده‌اند، بسیار امیدوارکننده به نظر می‌رسد.
🔴
من ترجیح می‌دهم مسئله برنامه هسته‌ای ایران از راه دیپلماتیک حل شود. تردید من به خود ایران مربوط است.
🔴
یک توافق خوب چه شکلی دارد؟ هیچ غنی‌سازی‌ای نباید وجود داشته باشد.
🔴
باز شدن مسیرهای کشتیرانی و توقف درگیری‌ها به‌خودی‌خود یک موفقیت است، اما اینکه بتوانیم به مرحله دوم برسیم یا نه، نمی‌دانم.
🔴
در مورد برنامه هسته‌ای، بله، قانون می‌گوید که کنگره باید آن را تأیید کند. و ترامپ هم گفته که توافق را برای بررسی به کنگره خواهد فرستاد. پس بله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/128572" target="_blank">📅 00:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128571">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
معاون رئیس جمهور جی دی ونس:
پرزیدنت ترامپ هرگز نگفت که هدفش نصب رضا پهلوی برای تبدیل شدن به رهبر جدید ایران است.
🔴
آنچه گفته این است که اگر مردم ایران بخواهند قیام کنند ، عالی است. این کار اوناست این بین آنها و دولتشان است.
🔴
چیزی که ما می خواهیم توقف برنامه هسته ای آنهاست.‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/128571" target="_blank">📅 00:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128570">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e8bb5c7ab.mp4?token=IlXl8BWBpcdHV1ljnRbYI8Bs8QEZB_BMjthlkA5OU9Xn6CEKdORtfgkJPZyaD3DUp_rCRi_IE74g-Izw-FtQYiSaz4P1q0wa20rC3Ud9tt0lSuQdHAarDWz8hgyUqGjJEqDkwUEfcJ-J610D8zX2PxZTuYM0m8Hb3-IQWOFIpITdR6vdOxC2aj1p6y4X747-PeR70Tae1GndBDwORsJlIJhs6j6SuNt-Uo2milb4uHd6MfL2Huvmga96wW8cqkvQbWOx7jovp1o07xBirVTJThW7rdUO9JEgZKcd1LUhOXyvrQWwe5Bdo3BEMtjSbn954AG-9wsp0OCOb9_sxmRCNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e8bb5c7ab.mp4?token=IlXl8BWBpcdHV1ljnRbYI8Bs8QEZB_BMjthlkA5OU9Xn6CEKdORtfgkJPZyaD3DUp_rCRi_IE74g-Izw-FtQYiSaz4P1q0wa20rC3Ud9tt0lSuQdHAarDWz8hgyUqGjJEqDkwUEfcJ-J610D8zX2PxZTuYM0m8Hb3-IQWOFIpITdR6vdOxC2aj1p6y4X747-PeR70Tae1GndBDwORsJlIJhs6j6SuNt-Uo2milb4uHd6MfL2Huvmga96wW8cqkvQbWOx7jovp1o07xBirVTJThW7rdUO9JEgZKcd1LUhOXyvrQWwe5Bdo3BEMtjSbn954AG-9wsp0OCOb9_sxmRCNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
در حال حاضر افرادی هستند که می‌گویند باید نیروهای زمینی به ایران اعزام کنیم.
آن‌ها می‌خواهند دونالد ترامپ صدها هزار نیروی نظامی را وارد ایران کند.
ما به افرادی نیاز داریم که از داخل همین جریان، در برابر این دیدگاه مقاومت کنند و با آن مخالفت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/128570" target="_blank">📅 00:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128569">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fb6fc009c.mp4?token=KCT__1fcHJWrw8_6yfsaLE8U2CNIsz08KZ4scLh2uCJ-9Tl6efq4cdkaavjHKgCgeaPU_6KVB8zzcrFtL6Ua9Dyh4PTlhLRmtPclC2A42-28Y9rmqsCAmvbO3to3dBpDs2VChTJ42V5t7pzf0_QnuoQBFlhxx6LJgL7KkEDI-7fZLBp0lMVJjsNuJvtxNnTpd0cSxPYmddKoUUY19ypTuEVPvTh9WEYRCSkaerwKR9bP5AP0dB08vPDeZoUloZf9X_oLLJ00EVwGv9MHKJU7XXAuH6nOXQZ2h3QeShYg3joTMgMwSnoYHMSc3NbBVCyTXHSFcSdndtzL4P67IBhYD4zjyxe1BKYTAHFspILNHF60bZAQz8qz5ff0gG2onTeNBQ77TNZND1lybHNdr00JSA34WWqmkNQ6Q7mOsFuaZQAyAfjTlboljsV6KjbYaQpMq-ZY3PMescYWyIpv90-ZdJQCzTt0aWPbNv8_uzdWTOgK5bQOQDQAfvTP_MTEuumj9EcrYkmFO46tNHNElfXTbB9fueWctewlKiuW3hrawdxclebhelqlBSAAN5xAeBnQtrlUCV4b3ZIvXNr7kAnmg7KsIBgmqHXlKHf_uiOOyz95kRn6IHucWK_6cqNXSk8F01OCMWcFbK1RhzzUfee8_FYuupjoScDy6_TKZ-o99KU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fb6fc009c.mp4?token=KCT__1fcHJWrw8_6yfsaLE8U2CNIsz08KZ4scLh2uCJ-9Tl6efq4cdkaavjHKgCgeaPU_6KVB8zzcrFtL6Ua9Dyh4PTlhLRmtPclC2A42-28Y9rmqsCAmvbO3to3dBpDs2VChTJ42V5t7pzf0_QnuoQBFlhxx6LJgL7KkEDI-7fZLBp0lMVJjsNuJvtxNnTpd0cSxPYmddKoUUY19ypTuEVPvTh9WEYRCSkaerwKR9bP5AP0dB08vPDeZoUloZf9X_oLLJ00EVwGv9MHKJU7XXAuH6nOXQZ2h3QeShYg3joTMgMwSnoYHMSc3NbBVCyTXHSFcSdndtzL4P67IBhYD4zjyxe1BKYTAHFspILNHF60bZAQz8qz5ff0gG2onTeNBQ77TNZND1lybHNdr00JSA34WWqmkNQ6Q7mOsFuaZQAyAfjTlboljsV6KjbYaQpMq-ZY3PMescYWyIpv90-ZdJQCzTt0aWPbNv8_uzdWTOgK5bQOQDQAfvTP_MTEuumj9EcrYkmFO46tNHNElfXTbB9fueWctewlKiuW3hrawdxclebhelqlBSAAN5xAeBnQtrlUCV4b3ZIvXNr7kAnmg7KsIBgmqHXlKHf_uiOOyz95kRn6IHucWK_6cqNXSk8F01OCMWcFbK1RhzzUfee8_FYuupjoScDy6_TKZ-o99KU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس:
اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های مصادره‌‌شده به ایرانی‌ها منتقل شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/128569" target="_blank">📅 00:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128568">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e8bb5c7ab.mp4?token=JIjKiLDK0rajeuKH8SNrI91dJrRC05vHZCt7N8XKelTN6dqtZZfnLThPsvUByDFdbRFGQt-K3mveTvLqeJFjtQd3xpRI3pqTeWFwUDSc-iPeSAYgkrOzbAALaOmFdzVgD83kjW9J4yK-o3dFeQN9ooJtThdBKMfAH5tS0hCU7LrqG2xejnDduTF4QLA3zkOE8YBngl0upz5t1QuaX3u05_g83ufE08QtOH1j4g--dTPMkP_-p6Vi3fjvp0erssINFzm3iQoCFMZk4Njoiygw88hpFDLOyjLqStLYgbzeEXmqagrhwvorPbVAeoV82SUVNBZK8wSOLUQ6rx5g0fHprg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e8bb5c7ab.mp4?token=JIjKiLDK0rajeuKH8SNrI91dJrRC05vHZCt7N8XKelTN6dqtZZfnLThPsvUByDFdbRFGQt-K3mveTvLqeJFjtQd3xpRI3pqTeWFwUDSc-iPeSAYgkrOzbAALaOmFdzVgD83kjW9J4yK-o3dFeQN9ooJtThdBKMfAH5tS0hCU7LrqG2xejnDduTF4QLA3zkOE8YBngl0upz5t1QuaX3u05_g83ufE08QtOH1j4g--dTPMkP_-p6Vi3fjvp0erssINFzm3iQoCFMZk4Njoiygw88hpFDLOyjLqStLYgbzeEXmqagrhwvorPbVAeoV82SUVNBZK8wSOLUQ6rx5g0fHprg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران:
در حال حاضر افرادی هستند که می‌گویند باید نیروهای زمینی به ایران اعزام کنیم.
آن‌ها می‌خواهند دونالد ترامپ صدها هزار نیروی نظامی را وارد ایران کند.
ما به افرادی نیاز داریم که از داخل همین جریان، در برابر این دیدگاه مقاومت کنند و با آن مخالفت کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/128568" target="_blank">📅 00:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128567">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965eebaf12.mp4?token=AwLJzwnjCVR4QuxFs-PGJCuLaP8l_oEdBnprJEd22jO7_CkKxxOKtnLYX7XL_RzSOTPIyLTJh2Qauy_kD3vLJTtty7TOtvT9jhQoBoppY3aYYvnXMg634OAY3c9tlMcr5buRGml8Ko08grbZ-IW-IzP_cYtUsNNXhcHCt6oihmkGEw4RHNZfCGtPUSLaJGEXZmjDJPra9ahmxaBA16YZajGwKTjmBZMOX5jpyc3ZcQCkdnnoUY8mdDbR1xt6cOmAEXCEM0waqLGWI5Qe7eZLoXQOasU_GDZSETqO1sHWdhMRRKR7tsAXa_6yaJfF3vj2xj6KLESCF29t24Ymd7OwzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965eebaf12.mp4?token=AwLJzwnjCVR4QuxFs-PGJCuLaP8l_oEdBnprJEd22jO7_CkKxxOKtnLYX7XL_RzSOTPIyLTJh2Qauy_kD3vLJTtty7TOtvT9jhQoBoppY3aYYvnXMg634OAY3c9tlMcr5buRGml8Ko08grbZ-IW-IzP_cYtUsNNXhcHCt6oihmkGEw4RHNZfCGtPUSLaJGEXZmjDJPra9ahmxaBA16YZajGwKTjmBZMOX5jpyc3ZcQCkdnnoUY8mdDbR1xt6cOmAEXCEM0waqLGWI5Qe7eZLoXQOasU_GDZSETqO1sHWdhMRRKR7tsAXa_6yaJfF3vj2xj6KLESCF29t24Ymd7OwzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمار فاجعه بار ستاد مبارزه با مواد مخدر از مبتلایان به HIV در کشور
🔴
از هر ۸ نفر معتاد ۱ نفرشان مبتلا به ویروس اچ‌آی‌وی است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/128567" target="_blank">📅 00:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128566">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سوال
: آیا ترامپ در حال فروپاشی است؟ او تازه ۸۰ ساله شده است.
🔴
هیلاری کلینتون: فکر می‌کنم او قطعاً همان چیزی نیست که قبلاً بود.
🔴
دونالد ترامپ این روزها مدام در حال خوابیدن است. او این روزها خواب کافی نمی‌بیند.
🔴
جو بایدنِ بیچاره!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/128566" target="_blank">📅 23:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128565">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
هیلاری کلینتون: وقتی ترامپ جنگ علیه ایران را آغاز کرد و سپس از کاخ سفید شنیدید که «هیچ‌کس به من درباره تنگه هرمز نگفت» و پرسیدند «تنگه هرمز کجاست؟»، این چیزی است که نمی‌توان آن را ساختگی دانست. انگار فیلمی است که به دلیل عجیب و غریب بودن از آن خارج می‌شوید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/128565" target="_blank">📅 23:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128564">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=oY61xMBzcwagZ2I7RYz0FhaR4N-4VTVRys8vUKX2hQlOfpPCHhpy3bHnsnw8om1sz_KWii8ZHpQVu-i0xg5JNIOVPTGe3hqfbkvcAR5PZMJA1pWDKBpEcXO_NbwSd2uRu1smtNKv8xtx8mFsh5Ia5fS2SquREiRdplbFctRsXVvFssVJwVZyB_AfDkL2T4QeBpxfD79XfTnn5DWCrD3li_LdYksbBE57aPiVTaw93-g00rKEiOxJw6yeuHIpW_2MkrxeZXNnUDnMLfDOkvi-iz1OBGbMUuvjEb8IfrIm1L1PEKWSrbjZuT2LmqdyYYxYQKPhRYhj5yIAKffZLc_Pew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=oY61xMBzcwagZ2I7RYz0FhaR4N-4VTVRys8vUKX2hQlOfpPCHhpy3bHnsnw8om1sz_KWii8ZHpQVu-i0xg5JNIOVPTGe3hqfbkvcAR5PZMJA1pWDKBpEcXO_NbwSd2uRu1smtNKv8xtx8mFsh5Ia5fS2SquREiRdplbFctRsXVvFssVJwVZyB_AfDkL2T4QeBpxfD79XfTnn5DWCrD3li_LdYksbBE57aPiVTaw93-g00rKEiOxJw6yeuHIpW_2MkrxeZXNnUDnMLfDOkvi-iz1OBGbMUuvjEb8IfrIm1L1PEKWSrbjZuT2LmqdyYYxYQKPhRYhj5yIAKffZLc_Pew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرف حق پزشکیان:
مشکلات خودتون رو خودتون حل کنید، من سیاستمدار نیستم من دکترم، برا سلامت مردم اومدم رئیس‌جمهور شدم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/128564" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
پزشکیان: حوادث دی‌ماه سال گذشته قابل پیشگیری بود
🔴
بخش قابل توجهی از کسانی که در این رخداد‌ها حضور داشتند، با آسیب‌هایی همچون بیکاری، محرومیت درگیر بودند،
🔴
اگر می‌توانستیم زمینه‌های شکل‌گیری این آسیب‌ها را شناسایی و مدیریت کنیم، بسیاری از این مسائل بروز نمی‌یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/128563" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128562">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
کانال ۱۵ عبری: سند تفاهماتی که میان امریکا و ایران در حال شکل‌گیری است، مجموعه‌ای از امتیازات بسیار گسترده واشنگتن را در ازای پایان فوری جنگ در تمامی جبهه‌ها، از جمله لبنان، نشان می‌دهد
🔴
واشنگتن متعهد می‌شود محاصره دریایی را لغو کند، تمامی تحریم‌ها را بردارد، از منطقه خارج شود و دست‌کم ۳۰۰ میلیارد دلار برای بازسازی ایران اختصاص دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/128562" target="_blank">📅 23:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128561">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
به علت پخش و انتشار سوالات امتحانی تو کانال های تلگرامی هندی، این پیام‌رسان تو هند تا بعد امتحانات فیلتر شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/128561" target="_blank">📅 23:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joBb7tLs1jwfQsvuAIcQME-6gXVsKyvma7VDh5sEkEQ7oEHfVeHU3ckceDaNdKbJslofv7gl15WyrUkC83lnw7Naxx28jNzVxA2JPSkVKJLaEfULlkWp7w1wM4ahgQ6-qNyczX4PzRLtN-3dOsx_krbT_gzMqW1kQrVAQstpAJLflQ7onHFJcnTm42dF4qoLtpt4xZmBPwuYDQSgCdWIFY77aID-SnMy8m71bhs7KgVTkDsmDxTT0pGcxc_U4MRQSR8E-koXoFrCDHhNyo9n-WQWIryC__3FEnMPwRR-VJSnXPr7QU0l-Ne42PSchQJgBzRk7d6CRoHbIxgGWjBr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی: خداروشکر یک امتیاز هم نتیجه خوبی بود، با برد مصر و حداقل تساوی با بلژیک میتونیم اول یا دوم‌گروه بشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/128560" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128559">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb9e0a16c.mp4?token=iZtb9ff0bH-YATvVuZz80eVT1l7LjbtNoyoEB_kZ6qb62Y8dXPc3vdIvlqJcHxf9Rva1liLmUSyqbk_l84nYs2Uzw8mCLhy_F_wOs4K6nNYXRnvISAOCUfvoZ7H4MDZwIuUyNw_VXD4Hm6czns1owPm7eYoQpevHuQ4s5l9te8__N8d8mQhoE1XnL32pOfTR3s4O24eJX64BhR9s1gGXVVEj28hjSX16SQ4_u8bGYhU7LQQnFa6wllLnFWdVUiSFQC2i5foeE2_mspM80S-umcbt5YUFYQe2_0LJx7tTGHkS3r4Yvy1lEITOxLifLG2_UQfefb-kFX3pHWVT61FlpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb9e0a16c.mp4?token=iZtb9ff0bH-YATvVuZz80eVT1l7LjbtNoyoEB_kZ6qb62Y8dXPc3vdIvlqJcHxf9Rva1liLmUSyqbk_l84nYs2Uzw8mCLhy_F_wOs4K6nNYXRnvISAOCUfvoZ7H4MDZwIuUyNw_VXD4Hm6czns1owPm7eYoQpevHuQ4s5l9te8__N8d8mQhoE1XnL32pOfTR3s4O24eJX64BhR9s1gGXVVEj28hjSX16SQ4_u8bGYhU7LQQnFa6wllLnFWdVUiSFQC2i5foeE2_mspM80S-umcbt5YUFYQe2_0LJx7tTGHkS3r4Yvy1lEITOxLifLG2_UQfefb-kFX3pHWVT61FlpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون سابق رئیس‌جمهور ترامپ، مایک پنس، درباره تفاهم‌نامه آمریکا و ایران:
من نگرانی‌های واقعی دارم، حداقل درباره آنچه در بحث‌های عمومی مطرح می‌شود.
🔴
در طول سال‌ها زمان زیادی را در اتاق وضعیت گذرانده‌ام. تفاوت بین آنچه واقعاً حل شده و آنچه در رسانه‌ها مطرح می‌شود را می‌دانم، بنابراین نمی‌خواهم پیش‌داوری کنم... اما من به ایرانی‌ها اعتماد ندارم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/128559" target="_blank">📅 23:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128558">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
عراقچی نمایندگان مجلس رو در جریان طرح‌ها و پیشنهادات مختلف مطرح‌ شده در روند مذاکرات قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/128558" target="_blank">📅 23:16 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128556">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbiKoudNSp-I9anmEb3PF2XHv1to-5-NV9rFQ2w460eiS11HDVjCzIR6yqb52eycTzZf7qoxgB8LORXrEC0K7LEholx3nTUJ2HBOfFGqxVIUXyfOaEDY8oT1oFbN5VD6ZwXwOKvWwcvSJ_nDFL5hFDjrHgbBLzhlmHIdXTSHBGFpyzQYxacng60uFHSfa0HOqRr_tDpGxsUD3xC126xIzFt9oqFlT1zTCET6hSrSlLc9100jlTj41QCuO-t_znNoqtK6IkATmQHLgbkH5BdjSi0xtf_zsRfpOFKjJuZe7l1bkmLtps6Vc6S2QuY7eMLpdJUgJGGYaYqWkZhUtsd1yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbKRZSRmwYpTiEyv-Nz8ipLCrngB8pOTg0iznHbUaEQzw-hRvt5tTSPcnl79uxC5pzOb2e_mcOok6KFHLhgQABNzt2549Q5A5iI9SU-e1lxzvRQQj9BOydOjawi_9KVKYpaBF-Ou8ynU2zy7qfWmyp_MziSpIIkzlVwW1_WMhMLp5g0pXWuiq2m_NRj_iKoTA6SdBOUX_nbjrnsFletzLrLVfVgToWqjxE8Y9eBo3MveRN49EZO--uPJE-fR6_CJ0JmndoaI_klDV1IsoarOGebdd3NQ3euUiWrOJu8Ls2l77tugrHcCvItfMmiuiSga_JHICH01FIe0Z4fSF8_OPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
دست ترامپ امروز در اجلاس هفت‌گانه در اویان-له-بن، فرانسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/128556" target="_blank">📅 23:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128555">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93292ab714.mp4?token=RSEVsNiDkviAZRwPJIjZBAjKYsJUmcGvfAYkYcEuAV_cGNTWaf6aYGVfWb23JPjr51GYXmjd-tSQmZw5-hQxvvypgOh7LRL8pKBHMa-sudsBGKOHYcffPPS1uEhkwQYfT6ZTjUGg2iZroz4NKHIZAK7-OMGPCMiJvBB8_bP2jUX2cPRyz3QEMsON8G7PbwIwFz8RpH26Rf2aWziK56mkjLsAfnZFa-4aYqwPU__IT7ZVmBz6ve8_LEGmfRHRlKblVXvxGIV41KPmRCn-I6PtQeNBYAtCxYXpCNwSxxs2FgJuzLBwfTtePtTJvaoQJqQ3LeSrT2Bnqu7Qb8ihqEIPCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93292ab714.mp4?token=RSEVsNiDkviAZRwPJIjZBAjKYsJUmcGvfAYkYcEuAV_cGNTWaf6aYGVfWb23JPjr51GYXmjd-tSQmZw5-hQxvvypgOh7LRL8pKBHMa-sudsBGKOHYcffPPS1uEhkwQYfT6ZTjUGg2iZroz4NKHIZAK7-OMGPCMiJvBB8_bP2jUX2cPRyz3QEMsON8G7PbwIwFz8RpH26Rf2aWziK56mkjLsAfnZFa-4aYqwPU__IT7ZVmBz6ve8_LEGmfRHRlKblVXvxGIV41KPmRCn-I6PtQeNBYAtCxYXpCNwSxxs2FgJuzLBwfTtePtTJvaoQJqQ3LeSrT2Bnqu7Qb8ihqEIPCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار
: آیا توسط دولت درباره آنچه در توافق با ایران وجود دارد، به شما اطلاع‌رسانی شده است؟
🔴
جان تون، رهبر اکثریت سنا:
من قطعاً هنوز این کار را انجام نداده‌ام، اگرچه ما درخواست آن را داریم و فرض می‌کنم که در مقطعی از دولت در این مورد شنیده‌ایم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/128555" target="_blank">📅 23:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128554">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رضا پهلوی: بمباران ایران باید ادامه پیدا کنه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/128554" target="_blank">📅 22:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128553">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6Z9wrTBW-q3JoiLXCLwv31AVL6-iMKvqt0JT9moVixHyVW5s5YMDIFczD-vbCpFb8ZrdmgqpXs-W1A1qPUboxr8Sn9p4uyeaBePaz1sgdzxo54i2oDg5e6NXFpDSagsicESlkwzy7CJlPw15rAgC-dL4hzEYgJzG2hwwSLLnjbVStC1mNnBWgsa247pJ5AnrHMIYrXU-iSIzLMP--aCvXDjhCx62n0vjQibOj6i-wzcXqQTxLFHnqHaMFrO7JA-NiFUazJjnwneN35vYVwINejMvSRzS_3iNhwX2-_osy7IViwnRZKz-NFhcrwHVslwTUfisW0NRqm6r2g8f4XmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی: بمباران ایران باید ادامه پیدا کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/128553" target="_blank">📅 22:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128552">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / گزارش ها از انفجار در اربیل عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/128552" target="_blank">📅 22:47 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128551">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
به گزارش ان‌بی‌سی نیوز، کارشناسان ارشد صنعت نفت هشدار می‌دهند که علیرغم فضای مثبت ناشی از توافق میان ایالات متحده و ایران برای پایان دادن به جنگ چندماهه در خاورمیانه، بازگشت بازارهای نفت به حالت عادی و از سرگیری تردد در تنگه هرمز فرآیندی زمان‌بر است و احتمالاً چندین هفته به طول خواهد انجامید.
✅
@AloNews
خیر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/128551" target="_blank">📅 22:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128550">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVXEeY50ugz3CajRi5DkNzO8GaylL7-dzoYPaHktNp2JltZ5rp-_1ihf10Xjl-6-Oc6HX1W_phwtsBKh3VQ9SwlhPNR2QkcsPQNgr8Sd1rin9jYD6FMSYoSEv999zfD8If-UVY5yyMcLSk5v6gSBDe1syNd7xR9FdoEr9Gy4xjJHl0SfPRkvYVqsrVFcfoemRSjzzON8RaeAaQcTg8Ma0eJk4JPUstL2bHAbPpeZHfF-lNE3tDaeJQA1iTTr8c7_k8Md5OKV2Qv0yFges5TimfUd4pg3DcfY_nYOu440ne81gA9dxvmIqQh4yPg6eGyce25ofBUUE-yFOechEUuV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: تفاهم‌نامه ایران شامل اعطای صندوق  سرمایه‌گذاری ۳۰۰ میلیارد دلاری است
🔴
تفاهم‌نامه بین ایران و آمریکا شامل برنامه‌‌ای برای  تشکیل صندوق سرمایه‌گذاری ۳۰۰ میلیارد دلاری به منظور حمایت از اقتصاد ایران است.
🔴
این صندوق تنها پس از امضای توافق نهایی راه‌اندازی خواهد شد و شرکت‌هایی از آمریکا، منطقه خلیج فارس، آسیا، آمریکای جنوبی و آفریقا متعهد به سرمایه گذاری در آن شده‌اند.
🔴
این سرمایه گذاری در حوزه‌های انرژی، لجستیک، تولید و حمل و نقل  خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/128550" target="_blank">📅 22:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128549">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سی‌ان‌ان: ایران بخش قابل‌توجهی از توان موشکی، پهپادی و دریایی خود را حفظ کرده و همچنان از ظرفیت لازم برای تهدید تنگه هرمز در آینده برخوردار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/128549" target="_blank">📅 22:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128548">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIHqzhbV7Rh0uGUfXFibb77vIPA1ZbPP-MPAZqQeljvDNOfx0uNHenPYuQJHJlEHt3AE5v5q1g4JZLbuDb4MgSh0ETd0XOOPeVOW_S46CZETvyGSD0S2xcYljVHCEmFQ6k_DAtbBENgrqnpe6GJF2lX8LUT-95_FuZtdL817Su9CZZBvP5aizhrUSt2jLLZmgH-lcwkReMUFTBsU2wTQYfCje7jb0DITrwMMV8C3gDwNjJuFrUJNdb7kB30PHIC7G1jmRctToCsEyc85nXO__TYNXhD8DtrUorxu0EnHh3iyzQ6HSEnCdNyf7LWPHt0bqfRW2HaxY0FSg8idmABqKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب لیکود به رهبری بنیامین نتانیاهو، نخست‌وزیر اسرائیل، فعلاً کمپینی که بر رابطه نزدیک بیبی با رئیس‌جمهور ترامپ تأکید داشت را کنار گذاشته است، زیرا ارزیابی‌های داخلی نشان داده‌اند که ترامپ در حال حاضر نظر عمومی رأی‌دهندگان اسرائیلی را بهبود نمی‌بخشد، طبق گزارش i24NEWS
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/128548" target="_blank">📅 22:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128547">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
هشدار قرارگاه خاتم‌الانبیا : ارتش اسرائیل تو دو روز گذشته ۸۴ بار آتش‌بس جنوب لُبنان رو نقض کرده
🔴
با وجود اعلام پایان جنگ، هنوز هم به حملاتش ادامه میده
🔴
همچنین هشدار میدیم، اگه این حملات متوقف نشه، نیروهای مسلح ایران پاسخ سختی خواهند داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/128547" target="_blank">📅 22:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128546">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uu9I32Z-OtGJBD3y_-jelF3YWIQqqpRRPc8sAnSztmmNzNL7hQLMxmxEwaXDTrqgw-ycGZuj85T-EySx24PFQIdTU904Dklz2m1Gz1l-I63kq8nMy2EeJ6tbXYrGQtmHS45y5uEI_PXDqSFTvkgSQqrM0su680e0TexHGcxvdZ3E634u9kq_rmqXuPc4OKyCyynjBSZesNBdXIlIORAEsWvfVsut6vZk2xPM9STUpsv45T_qO42eKYnfPpb_qt-eylO80Q-hDSfsH57yvNpUXRBgSmS1viktGmbieIdUg_0wlDf3V-cbmZlszxWwZzh87YsIMsuwLjKDa1cESzeE7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز : بیش از نصف غرامت ۳۰۰ میلیارد دلاری ایران از قبل تأمین شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/128546" target="_blank">📅 22:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128545">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
قطر: هیچ بودجه‌ای برای چارچوب بازسازی ایران اختصاص داده نشده است
🔴
الجزیره نوشت: ماجد الانصاری، سخنگوی وزارت امور خارجه می‌گوید: هیچ بودجه‌ای از قطر تحت چارچوب گزارش‌شده ۳۰۰ میلیارد دلار اختصاص‌یافته برای بازسازی ایران پس از جنگ پرداخت نشده است.
🔴
او در پاسخ به سوالی در مورد این رقم به خبرنگاری گفت: «ما نمی‌توانیم در مورد ۳۰۰ میلیارد دلار اختصاص‌یافته برای بازسازی اظهار نظر کنیم.»
🔴
با انتشار اخباری مبنی بر راه‌اندازی یک صندوق بازسازی به ارزش سیصد میلیارد دلار برای ایران، رئیس‌جمهور آمریکا روز دوشنبه گزارش‌های رسانه‌ها در این مورد را رد کرد و آن را «اخبار جعلی» خواند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/128545" target="_blank">📅 21:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128544">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
کان نیوز: مقامات ارشد امنیتی امارات متحده عربی در آغاز جنگ علیه رژیم ایران به اسرائیل سفر سری برای بحث‌های امنیتی در سطح بالا انجام دادند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/128544" target="_blank">📅 21:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128543">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری/باراک راوید، جزئیات تفاهم‌نامه ایالات متحده و ایران را به دست آورده است، او می‌گوید ۱۲ نکته به شرح زیر است:
🔴
ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان. ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند.
🔴
ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
🔴
ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
🔴
ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
🔴
ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
🔴
ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
🔴
ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
🔴
اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد.
🔴
هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود. ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد.
🔴
مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/128543" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128542">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
فارس: برخی منابع نزدیک به تیم مذاکره‌کننده ایران، ادعاهای شبکه خبری العربیه در خصوص متن یادداشت تفاهم ایران و آمریکا را تکذیب کردند
🔴
العربیه پیش از این نیز گزارش‌های نادرستی در خصوص مسائل مرتبط با ایران منتشر کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/128542" target="_blank">📅 21:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128541">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سازمان اطلاعات داخلی فرانسه، اداره کل امنیت داخلی، استفاده از پالانتیر را متوقف می‌کند، وزیر دفاع سباستین لکورنوی به نگرانی‌ها درباره وابستگی استراتژیک به آمریکا اشاره کرده است، گزارش خبرگزاری AFP
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/128541" target="_blank">📅 21:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128540">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
فرهیختگان: بیش از ۱۰ هزار پزشک زیر میزی می‌گیرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/128540" target="_blank">📅 21:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128539">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
یک مقام آمریکایی و یک دیپلمات منطقه به تایمز اسرائیل گفتند که آمریکا خود را برای ارائه تسهیلات به ایران در قالب معافیتی که به ایران اجازه صادرات نفت می‌دهد، آماده می‌کند.
🔴
اعطای معافیت تحریمی پیش‌دستانه آمریکا در مورد فروش نفت ایران نشان می‌دهد که در واقع برای برداشتن برخی محدودیت‌های اقتصادی، نیازی به امتیازات بیشتر از سوی ایران نیست.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/128539" target="_blank">📅 21:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-128538">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
عبدالناصر همتی رئیس‌کل بانک مرکزی به خبرگزاری تسنیم: پس از امضا و آغاز اجرای یادداشت تفاهم، اقدامات فنی و بانکی لازم برای راستی‌آزمایی آزادسازی دارایی‌ها و امکان استفاده عملی از آنها انجام خواهد شد تا اطمینان کامل نسبت به دسترسی مؤثر به منابع فراهم شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/128538" target="_blank">📅 21:09 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
