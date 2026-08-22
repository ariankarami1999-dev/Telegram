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
<img src="https://cdn4.telesco.pe/file/SJsRXNsIPgfSqQloQ_Ckj9Ii9irng4E-hoZXXHAOM54h5Mqz_nJ1zTighorMC5wE8YNSjBJb2u2C_NKGV97HsjwyExmHD9SokS-ny0T1tMX4lGFa1YUHrlEI7YIaNxF7bxP6c_TQ5tbsNEvbDFnqbmNEkM3_vL6OI2LyfLJPt5M-K7PRc2svfdlZJrYehq_MDFIAW7njHsn6Rs4etvyNNn7r6VY91pyIsZOivTTCDUNHAIALHtfD4DFwOZQX2x09_TYqGZhJEZKGJtS6nstvnx7GAC8unI6B30fRzvZKhHl2CPbSwmawRUKOW3vkDD8OVsqZBek1UPPcfbpMwvSulQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 616K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 15:12:14</div>
<hr>

<div class="tg-post" id="msg-28241">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTS8OaGN7If8c8myBvfNyr47b_sIiKUZLn9-VmX57kCb4u7qsU4b-7eEzv1IrTvBuzLTZ0NBo22IwV8nYDOdUWNzYVkZZ2JJuwJKnqrXJuYhdLp7FKcoTWWPBCsv9JgkhYrhcy9Fwf_VWyf4ZkH2Pjx009oUUKQuRz4pVONZnCHAmJ0-VDe0tZYvk2Xj4sSqhQby_Xi1RbMYvWjRQSdD8Wl1cCftAduzuGjGY0iPXu2M67Cp-8jQYV6Efva8flrpeTFKI6avDQl_QJskqC5GqDifN4wt-JBnxGIvIeAzwgeMnX0w573DBIPSVxKcPw096vMhVMC8U2D3ofj8NuoEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بنده‌خدا که یه دوخرچه سوار حرفه‌ای بود و ۱۲کشورجهان‌ روبا دوخرچه‌رفته‌بود و هیچیش نشده بود روز های گذشته تو جاده کرمان با میکسر سیمان برخورد میکنه و جونش رو از دست میده. طرف هم بجای اینکه تلاش کنه جونش‌رونجات بده فرار کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/28241" target="_blank">📅 14:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28240">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-6k5V_Ii7V2vrKj1qYBKGFfUrMmoDNi_qdmaxccKQC2RyvMsx2F8OqZ4BpWAwyVgKXw9KF9ZYUo1sHK0obh5heJfVVkL96n_l2wUAnvpRMedrn94QYqnJz6nRVmQMUeC-NKmjJfZLHsxUrUTQIny5lIbQ6AEosUUogki6Xqm6KV5nacctuWOXibQmLTp6e5LeX7OaXlcRqiMWi3TtT-s0O_is1ROfTFX5fiHX1jVoioulKKQrKMCDsI3ccIIEX4WzLpR-RashpJ6cZomuACaaArx7b9J0SFXZjaZ4myNJdWiZxQF1hiXyyCYesa61tpSm0OJIukPtxjTK6o1BHcTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌کامل‌بازیکنان ایرانی در ترانسفر مارکت که فعلا بدون‌تیم‌هستند و در مارکت بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/28240" target="_blank">📅 14:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28239">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FoSBG3F7c1gIOOQ_R4OBp7C7T7wm66BPUzCx5mOuBrYkoiYW7C7R9Zxm_hjTwZbc_U-PDHCqHmxGbKLxV0b1Hk6n3Du5wLSmHyWToHcWLm_ivEAK02ZHRU91ZNCdDZQnk-r_IZ7L6D0W1HvI-gK08VpiRyB9fP_HZ2E4JIWUpgcD1TCWv3o7pLRyOziXzNxQSMOdzs5IXLDAiTiM0_PLvVGs4iQccm6RjJQ4XZJ2yJLSHE2zoWh3x-zBszkISztJtbycYKWLqfrY22ToJMV4XQM3ch7iAP1_V7H5WRW38Ha_zSnViMh4G8Q8Fv8eEXO1p-ZnigR2kk9R1s6eUmt1TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه فجرسپاسی اقدامات لازم رو برای جذب علیرضابیرانوند انجام‌داده و قصد داره از اول مهر ماه این بازیکن رو به خدمت بگیره. بیرو هم درتلاشه که با پارتی‌بازی معافیت تحصیلی خود را به مدت دو سال تمدید کند و در تراکتور موندنی شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/28239" target="_blank">📅 13:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28238">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1fb0883a.mp4?token=ttO4vc6jfewUh6hQ1lHK0uH9Y0ol8bKEO3j96AxoEAgdTkCvc9v9qVpKqayboljG9nEM08ns6RbnmOoDMzSudMqOOwmXQr6LhHWyeKyMqu1fAKvNuF4jllb6CvL29qB211caVGRPBx1Ap8jp1t4mWi5sMK1qhjICPZPFYTgfb97YpkW2osxP1UYQYheYbwflqJN8K3cwgiubx8Hz0aqMyEhcvJ1r8CObiJVjcTs9Az2zKB7ZBXxAF1yIfZw5_fgFpPNtct2kVtJjGJUithlm0D8HA-f6vcpH9q1CfKuLj35Aty6vf8q1oiFa4Rp_Xkahki-FDHW0VQ2GwTY4XVu-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1fb0883a.mp4?token=ttO4vc6jfewUh6hQ1lHK0uH9Y0ol8bKEO3j96AxoEAgdTkCvc9v9qVpKqayboljG9nEM08ns6RbnmOoDMzSudMqOOwmXQr6LhHWyeKyMqu1fAKvNuF4jllb6CvL29qB211caVGRPBx1Ap8jp1t4mWi5sMK1qhjICPZPFYTgfb97YpkW2osxP1UYQYheYbwflqJN8K3cwgiubx8Hz0aqMyEhcvJ1r8CObiJVjcTs9Az2zKB7ZBXxAF1yIfZw5_fgFpPNtct2kVtJjGJUithlm0D8HA-f6vcpH9q1CfKuLj35Aty6vf8q1oiFa4Rp_Xkahki-FDHW0VQ2GwTY4XVu-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سهراب‌بختیاری‌زاده‌سرمربی استقلال: نظم و انضباط برای من از هر چیزی مهم‌تره. فردا علیرضا کوشکی رومقابل تیم‌سپاهان فیکس نمیزارم تا بفهمه اینجا استقلاله و نباید رفتارخارج‌از عرف انجام بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/persiana_Soccer/28238" target="_blank">📅 13:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28237">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21259a9796.mp4?token=bH140GMMK8rC0HfGjjM-tphnYv3soYxpV_MG0R-IXpcvo2P8I7awKPrWHXiWhrw4x3BxHxfspdJfZQ4Qk5tG1vkrwgneR_zzSyu_OPbby9ZrcUz6ArcH4fkiMTdrdK2-I9L0yU6eTs9fa6iYS1fBIu0DG5EWZlffc-4bwkkf83JmY0z4gEV-cSd7ZN0aoQpbvY6LTPWy8U9NKCuOqs_sbtAY2PxhW-cr2kiztkJJpQ64upWq5g_NTIILauapdXEDY9KEjny5Lf71NKEX0zoVuQ-wH0U4hhIGBwS7HswUjWwImXK9UQkRiVFOZgBUT6rlt6lKwhTgU3iTumXH_IxRyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21259a9796.mp4?token=bH140GMMK8rC0HfGjjM-tphnYv3soYxpV_MG0R-IXpcvo2P8I7awKPrWHXiWhrw4x3BxHxfspdJfZQ4Qk5tG1vkrwgneR_zzSyu_OPbby9ZrcUz6ArcH4fkiMTdrdK2-I9L0yU6eTs9fa6iYS1fBIu0DG5EWZlffc-4bwkkf83JmY0z4gEV-cSd7ZN0aoQpbvY6LTPWy8U9NKCuOqs_sbtAY2PxhW-cr2kiztkJJpQ64upWq5g_NTIILauapdXEDY9KEjny5Lf71NKEX0zoVuQ-wH0U4hhIGBwS7HswUjWwImXK9UQkRiVFOZgBUT6rlt6lKwhTgU3iTumXH_IxRyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
تغییر چهره برگ ریزون و باور نکردنی رابعه اسکویی بازیگرسینما و تلویزیون درسن 60 سالگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/persiana_Soccer/28237" target="_blank">📅 13:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28236">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bBZsI92WKdtBxQkREcUu7XQE84MXOZaVBE9G4sCwM0ARv0SRop8IiBE0W68hvRRqyIu7Jt2Rx9wkHIuyjFvRkDPkqHqJ_EWuOA1sJqm-CESybzRSAeD-cGC6nBvw2dQ3bAY_3A2A1a09hlWp080kLOmbtEW-iSA5W2czpnqMiyAMJefh9iXg4tyUDAUyzXW0R83vOpHaRK31NVtfOUyGYZGEtyuxinHlz38VIzyQN_Na6fHt93uxDF49SV_jhpfut2so3fT4_U8rNcbsF0VDOtN2cNs19DGmQgGJcuNnJPscfOcsfdV_O43NlEUHKVDVTg1f0B_miZlRJx396-YmEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بدنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
؛
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://t.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/persiana_Soccer/28236" target="_blank">📅 13:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28235">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuFG0hjY8cr4Ma_5-RMUZ-GZt2W5Rj7lVKOh90xiaPkWTTwWXKMXX9lVNY39HOEk_yEFBAhbGaHR6f98mJjrthMBgBqdGCmwLTSCCxlpp8FOc7AjvuqxnD4kILh67r4a2uak2zSu6t9WZxUqjk14Hgat7ysJV333xKrb6ZnO0Q6zuknQvT666gZdIZgK1XfjkKiwTlwMkfHRZrsHhHlt4uBojJ9yHPIDEPny7khcF_qQ0Blbjhq-w6TRewOj4s8G2iU7k8KX3N7jr2SH2-UqAtvU-s45S2eN-3tfuyXDDK08KOcwWKMq6HUSRNzsWE6fK7ibPM51Gmk6wrrc1yp5Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رودری با پیراهن بارسلونا پیش از دیدار با الاهلی مصر در جام چهار جانبه خوان گامپر؛ این اولین بازی رودری برای آبی اناری‌ها بعد از پیوستن به این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/28235" target="_blank">📅 13:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28234">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeXtde-u2peTYSH_MDJbMYFbKetFI1vbq-WOsfX6ohnrrTZLe7vktps3_-hoaZmjMs3tiNO2PTbU7MozTtFr1JSNNRhZcy1GBAjaEIuHd7iWWDHkd9iVlNzP3Gk3vUN3xXmfvVrX5_m_T2cw7D06TGmfrp4LM4xl-cT32koLhGhoeMVWvl7xWI4O2D8XTeMXgE5u-LLbuDEHXL5mbGRavEZwMGBNX71Tv14icudJBCLNeW6qH_MWrhhswRJACTkKLpBJ6aERdLaY2r4uiYKL2JmGUP3CQ_5fI26cu-SP5SY9_jrM-F7hmHpfFb-pIkGlMk-hOGdj6kBl0tsChT9-Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
مدیران دو باشگاه تراکتور و استقلال به فدراسیون‌فوتبال‌اعلام‌کردند باتوجه به همزمان بودن بازی‌های آسیایی این دو تیم با بازی‌های آسیایی تیم امید هیچ بازیکنی رو به تیم امید نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/28234" target="_blank">📅 12:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28233">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv76CLLUOrJYhjZ2c9hRBblXC66WL8s6Wq6WqrGVb6EKXhwUgLDRMxOk5orxvrcr3rzTuf2azjrVWPLVQOfwFPG2kX1VAZg_fH4JXlRNGHHNybq_MzbI3KTaCQIm8Ht3WgmUU6XvVbWna_EPifvQ1Ij1C2GuVC_SdG15E9CArH0HvkQjIluBH8lNpRoeLzxB6vC3c9fIzu5Jj571xuzhKDccZfIKKuxeu7FMUUnBUQYPul7rrbOkrlHMEBFKnhj6B7rAfr7-6djO2IVQmpauYkCsJBL6e8l8yDyyrqL2qVa8XnI_i_3ZgyttiETt70nJp4_u3btORlvbLqpT6jiDLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سهراب‌بختیاری‌زاده‌سرمربی استقلال:
نظم و انضباط برای من از هر چیزی مهم‌تره. فردا علیرضا کوشکی رومقابل تیم‌سپاهان فیکس نمیزارم تا بفهمه اینجا استقلاله و نباید رفتارخارج‌از عرف انجام بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/28233" target="_blank">📅 12:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28232">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3M9S1EnZOesgE7k1ypaCvxqxmHRkdWsD3nnB0We419OImOBuYmxn6rohVVWeE-zN2_K0HnofEC_N-F6km1Xri0evL2kndsEMPiIGtge4cq0xUxk5WwHObY6_qvETO491XE8OHityRLNH2qKMdooLu4Wg-hL-HjYUs8n3eOuuVr3sjL4NGEw_TZTGiaIVrltAVOIIgcYImNI1GMVNx-vObtJdxrLCNFjEKThS3WredP5hG-GV0L7e21ZBlhYD0VG2Hjp_fiNod2W-kdZi23_uqq2LikrcPROivwc2f35RBg3eAV_87ne-GJjOknTaMWLrdj3RUr9xMLxl-JCq3KHlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ژائو پدرو مهاجم برزیلی25ساله تیم چلسی قرار داد خود را با این باشگاه تا سال 2034 تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/28232" target="_blank">📅 12:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28231">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHpIGtloPILxqne7PBwVSq1vcY92Yfy0ew_nab-Uc77pGNdsin0ZXvtQMwzaBsawMJpsz6_1XkxDBLu2DxNdnu3hEKF07CpXsDIYtqC2_-yYYuoKlbaDZgx7m1omT8z7tSAU79Sua8YmHGTeU-MeT_rb4JJ7iJbP4KVHPT-XCbIvKe8vmOzYTCBGY4_v7JEhSZZNHLzdmUe9-Aclcbzscv-30GfkxY--16SzL0Dw0U8KcEOqAs89T2wu-KtAqCarByVPCUS_a17fQgJD8AELfqEAZHNAUoF3BDjbcnpZsl_vGYAjNPXhJE8v1qi8NuMh-vPIScEX6gRB94NuI85emA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
داداشی‌های‌فوتبال ایران؟!
پوستر دو باشگاه استقلال و سپاهان برای بازی‌حساس فردا شب دو تیم که شبیه به هم طراحی و منتشر شده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/28231" target="_blank">📅 12:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28230">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT2ilhUGrOQycUGRfWdxjhxnuKa-pLFBf_K2Y54RXrggQFweJIxt9B8OJDD-t_jFwDCHZ0IPMI3lgI7cKAlppeqgPkz1d6zmyS8eRZ35R3BaT0BrlZkZHPl4Qg9vyR0Bhvwgh4Y9-SWSxgdmz9hq-GP3d1ZsGQcUUtv5z0UVrjIYzNZ8zp-owx4ruPNU7cSJ_QUJ-346XNqtIefWL-Qzo1v2lgHx3R3vKsVukJry-6U6DDkB-rVXWZzfeTU2tcjMvtNXUUgp_cBnJz8-g0CVENOX4yj7nfMCxQjK7I23be3Dw-Z3Ke09nVPOfPHBaXYSJLGSSBvHZBBlN-x47_Ddgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درشب‌پیروزی‌شیرین‌چهاربرصفر النصر مقابل الریاض؛ کریس‌رونالدو موفق به‌گلزنی در این مسابقه شد. این 977 امین گل دوران حرفه ای CR7 بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/28230" target="_blank">📅 11:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28229">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERW9sa-45nsILoz7oO_H6BweSyp9XBNfpElGSuZi3jtHUGCjwqY6f8VfXs9ge-wAqGqM7u2HaGUqBckEmJtgXn5SbfShgUcF4-xQvIoB1ZVxjmsv4DdGpOLDY8pR2Cvts2YI9NADnunQyqvIfmZlY85LFudAtqsScJCCJLQdw6zd7mSrBUgy33M5MN2BZu9R4d73eyr9lk0pFqdAX9yMCo7-eiBRMhPD7rl6joQH6d64oY2xBSLrEFGRxABN62OQaEea6JMgp2xq9Dx5bK_BXrcrydf3h36rMZ4pkONvO92cpwCjv540YkCY9_yGp3huSqt0BP0dvqQjhv4O-nBEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
با اعلام کادر فنی تیم ملی امید؛ علیرضا کوشکی، مهدی‌هاشم‌نژاد و امیرحسین حسین‌زاده سه بازیکن بزرگسال‌تیم‌امید برای مسابقات‌آسیایی هستند و خبری از علیرضا بیرانوند نیست. همچنین تراکتور و استقلال گفتن به خاطر تداخل بازی امید با بازی هفته اول این دو تیم در…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/28229" target="_blank">📅 10:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28228">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsbUh6btCRzBrwEWC_hzVVlcLkLGC44rlfas2Sbm70OYuYj6vaa5DuUjQVc1HV2iu-w0V_rRkgz2cyJFO9X2hnZ0Ls8TZ7qkTYb-5LqNCzQaeF262Vdt1cLaChIAKGJcFyWezry9lWQ7HO0HmaiG9KpZjXGLGsWfZGjgiyFmNy5fPpgJdB6P_rioQmNfyG4xHmNPlR1STQt5nDZvuXlwj1eV1wlAAKhXFBOY4_iG7A7Mprq7PGmmMT2PVUylfQU9KiP96FXO3bSZDo9m8xOWwwsFc2Qbjqp7KvqtH1P_PHYmeuFjHCE-tSSFJHBEDHgFfnF7WQpUUF3r5AM6mto45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ سردار زاهدی معاون‌نظام وظیفه عمومی: علیرضا بیرانوند ازمهرماه سال 1405 سرباز خواهد بود، و باید ازیک‌مهرماه‌به خدمت سربازی بره؛ زیرا مهلت معافیت تحصیلی این بازیکن هم آخراشهه و بزودی به پایان میرسه./ حالا اگه یهو زدند معافیت تحصیلی بیرانوند دو ساله…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/28228" target="_blank">📅 10:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28227">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hD1F9NvnlsU3uY3F1FY2xJHSnjnJOQSlebtA3ql9P-n8TWZjgsmWe1jYO2bM-okwPSpYQ6M245qN8--Wia9tTmu3TaU7CoTRSnmwf-8NLf5QBNdq_RmeaZ5YEiKQ2O-rJn7HenfeOPdJ_Z_4v13uwDmYGS73dUsq4CLymW-Wtm78up41QLIfFvwUKWxJi0-UX-rj3S3gFtwFORfR5vs57ZmjMWff5mODoW_yibQ_i-sDt4OmiKRw8Hh8_CrBhuF1tGPP3IQ7CMQ-quYA02f-008gquZBXnZrOnIU7S9ibWmTNhl--Bp3ogUzCogOML0vGr2CQPs-Lersz7vXDRaveA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک‌باشگاه‌مختلط در تهران به خاطر مختلط بودن و کارای +۱۸ پلمپ شد و هفت نفر هم دستگیر شدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/28227" target="_blank">📅 10:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28226">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POG6h4KNS967qjqaoXauu5ULFgNZGzyJP4h07EexfB9QCDUI2Ze0FenrMDeTGE97wsuxs6v1pTNsbV5iXUh8A2lGjW4Pyo-m9CM2a9nN5QMJ7M-Gq4fRu1Shb14SZdjgWmW3BLNuBDOf6mAmC4u1RAvYv6EWGTWKBS0y8ONnF5SFfb0KZaVb9AjnewJth2FldE6ai3xSLHX7cTS0oKgrQXwFyTjonGbULBGjKAwkipQBu9QUj13s3IjTZ8MLNLM3MhxZ-a98resmHyRAxrU0_sr0yj4x8fCE27iOt8UG7XbO98kn5gU3Ad39R2Q3GEph-B-uZ0xaRZL8MLtU1ZVLqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام اسامی داوران هفته سوم لیگ برتر
؛ پیام حیدری داور دیدار استقلال-سپاهان شد و امیر عرب براقی دیدار تراکتور-پرسپولیس رو سوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/28226" target="_blank">📅 09:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28225">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9413e45de6.mp4?token=JQM5z-0YB8An5A7NLc582KsyPdu4t3gwf_lNnY6D6TGm4-OVZuancrhfng1wrAmvawk0Upv1Jtml4dloKL9BNgTZqxJXF2KMXM0kFwZpHm4qDf_cJ6q4mUxGSFp54rB9o1EEFHRGb__giVSdzZPyXZnc9JhCvZpccqMFhz0etZriZWllJfVCsfKLbFEb9pvvFzzKi-IRN5Iw8OLMhXjZ1200SCimSlGOQcIjLOYYbCMamz472pR3CyWLde4JqEY1ptrULRU0yDFa6Cq-EuuiK8504K74dDP9A9-6UII9Y5L1ly-Pzpw5S-x-Z7qd_JJkS98jreROZu7nfvsID5EB6Gr6AeRu0Hh_mIXPqJNrPdv4zEKi1F6-8dVeEvC6RtnMLOXZIdK2a1Sa-_xZEYXm8gx8yx0nHYzPYUCcRxhbhIq-MUCe9gjvTXkpFXm9Mw0grOaDJqTGIVVH9vdsei3i-sScyxh51EIIpg3eeh1IoP_HBJ7WnJK5LsTsaWyud53ogs3yNcLRxph6t9x7pJ3PhQj8LKXcdcCAbS6BCDMA2YpQpbF8zLFjQSE0n8UWyIVxRZ10Me_0o2Lc-7RkB4iBi7gRDrQvBZzEDvZN8gLI8SDbMw7a0FECcx0-1T3uNcrpqrjolaehkmhTZbsQTe_S3d71UG9rVbqKH0bP9IZqkrY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9413e45de6.mp4?token=JQM5z-0YB8An5A7NLc582KsyPdu4t3gwf_lNnY6D6TGm4-OVZuancrhfng1wrAmvawk0Upv1Jtml4dloKL9BNgTZqxJXF2KMXM0kFwZpHm4qDf_cJ6q4mUxGSFp54rB9o1EEFHRGb__giVSdzZPyXZnc9JhCvZpccqMFhz0etZriZWllJfVCsfKLbFEb9pvvFzzKi-IRN5Iw8OLMhXjZ1200SCimSlGOQcIjLOYYbCMamz472pR3CyWLde4JqEY1ptrULRU0yDFa6Cq-EuuiK8504K74dDP9A9-6UII9Y5L1ly-Pzpw5S-x-Z7qd_JJkS98jreROZu7nfvsID5EB6Gr6AeRu0Hh_mIXPqJNrPdv4zEKi1F6-8dVeEvC6RtnMLOXZIdK2a1Sa-_xZEYXm8gx8yx0nHYzPYUCcRxhbhIq-MUCe9gjvTXkpFXm9Mw0grOaDJqTGIVVH9vdsei3i-sScyxh51EIIpg3eeh1IoP_HBJ7WnJK5LsTsaWyud53ogs3yNcLRxph6t9x7pJ3PhQj8LKXcdcCAbS6BCDMA2YpQpbF8zLFjQSE0n8UWyIVxRZ10Me_0o2Lc-7RkB4iBi7gRDrQvBZzEDvZN8gLI8SDbMw7a0FECcx0-1T3uNcrpqrjolaehkmhTZbsQTe_S3d71UG9rVbqKH0bP9IZqkrY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
ویدیویی‌کوتاه‌وخاطره‌انگیز ازحرکات دیدنی و محشر لئو مسی در دوران حضورش در بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/28225" target="_blank">📅 09:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28223">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VC0HsXQJ__KhcXiGQsnHzW4GatAR6zSYV5r2DLnxSmWw4_gXluQRqFr5uJ3IPchORuOPu5D91tnuExCZouF5d6XfwcRRry764uc94fMOpIUsnUkUaaROJ35_8Kclrgd_2kEnl1WEv1IFIUvCAneBWqulL1DRx4mq2XNlejPRO8eKQrt2GHAMK7V9NTy70JAs3rmjzVlYTWrDpXEEmVEHm71ukCHu2yUs6-6LuMBLBxrR4irAIHpz3d8PuiKHlHI2oNH_OfuFDeyfu-5dOjkIF8Dj_pMpLgaVKJ_l4qdLSTO9fSId3231BOUZMiTQNr4oaNYRypJx5Yy025YEWUfjiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد حساس دِرکلاسیکر در سوپرکاپ و اولین گام آقای خاص درفصل‌جدید لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28223" target="_blank">📅 01:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28222">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7Clod8hZR6PmxMXf-Yk6kHEZj0gm6V-q4nSN6j-Kd8CALXayu0EgOe5-pWCNmS5BhUL_0QjxvLFDFfXIOTEPqxJGxSOwr02NXPMDVl3xc5omwDGrKahJ64gWbruAENnGHMGEvA_JKGVBmW26TSrs4gq_WnJV7ZbwgmthjXxO_CdMxIY5Zo4d1jzaHahV3cgpjIzgkf9FO4WTmPFG_2rFF5BRTwUie5FfUuyj5P4drKAImmYTbnvGMsNx77F5xapiJ1Ar9pcJAPTdjm175wUoXK-y6yy0fotdh84vzDFeoxlePRup6zWIqtydujvXlUeItilO9P-ICjugvZKbSVG6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌ دیروز؛
از برتری آسانِ آرسنال تا اولین گل رونالدوی 41 ساله در آغاز فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28222" target="_blank">📅 01:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28221">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=jy7EoKuxXs-yBZZ_xG4pUmxWc8R2fsk7tY4_Zzj9qMKpkLRKKz3UuuiNecIlKkji6kBwumt0gv3WhPsp1BYaz_V4Cw4zI9p_82OmykqCt4IFWaDrgUTtSQoY2nLRt6g0sPj1O8KzQHIiOgRT44YzFFXMgI3yKkS9Xvhkn1nB5ak9208QJ-O5D2hwHyC-DVFqYsfkS3klXEFbKmxEPe7SzQ8Ie-Gp0SLX2gHIsUQC-6umu1yoseTOaxQuCDnfyedY_5udx8XNr27mUIOVskKvcNhNq6M26GWjFK-Z6yZxMDeF_hmb2IjttTRgaEwcOeKejLqOXzqb7Nc6jMGnlez9mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=jy7EoKuxXs-yBZZ_xG4pUmxWc8R2fsk7tY4_Zzj9qMKpkLRKKz3UuuiNecIlKkji6kBwumt0gv3WhPsp1BYaz_V4Cw4zI9p_82OmykqCt4IFWaDrgUTtSQoY2nLRt6g0sPj1O8KzQHIiOgRT44YzFFXMgI3yKkS9Xvhkn1nB5ak9208QJ-O5D2hwHyC-DVFqYsfkS3klXEFbKmxEPe7SzQ8Ie-Gp0SLX2gHIsUQC-6umu1yoseTOaxQuCDnfyedY_5udx8XNr27mUIOVskKvcNhNq6M26GWjFK-Z6yZxMDeF_hmb2IjttTRgaEwcOeKejLqOXzqb7Nc6jMGnlez9mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حشمت‌مهاجرانی‌سرمربی‌تاریخ‌ساز فوتبال ایران، به‌ثمر رسیدن اولین‌گل‌تاریخ ایران در جام‌‌های جهانی رو با روشن کردن یه سیگار جشن گرفت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28221" target="_blank">📅 01:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28220">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80639b9fd3.mp4?token=volZBWhGJ1p-OPPZ-RwWocRvIibR7_8j2ctviTDRexccdfFHhJPC2vMXMvf-43w-lC7Kd0dJd_LKpLTy5-zko18Cf5LrkDsbUJ5d0Hqa2lRWaOEkdvrpOkc293GkR0sgn7AEonnWTdtXhuykl2-sjV46oQRBR3nA0n2_OgTY1YGcg8sxM4SwA2Q71w45KUrUVF6lROJWsMDRLha5_q-ZkEThJI9NhDqLq9_4Q4FUi1IH4jXNdzkhI6VoiVyvxQKoTf5KiiGlj50T0NvBodTbg2yh5hrrqLlTqh8apnbeittDtAreA-Bq1kg8OgwbuZTTNdXMhO1j5l5DpfxqT8x2qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80639b9fd3.mp4?token=volZBWhGJ1p-OPPZ-RwWocRvIibR7_8j2ctviTDRexccdfFHhJPC2vMXMvf-43w-lC7Kd0dJd_LKpLTy5-zko18Cf5LrkDsbUJ5d0Hqa2lRWaOEkdvrpOkc293GkR0sgn7AEonnWTdtXhuykl2-sjV46oQRBR3nA0n2_OgTY1YGcg8sxM4SwA2Q71w45KUrUVF6lROJWsMDRLha5_q-ZkEThJI9NhDqLq9_4Q4FUi1IH4jXNdzkhI6VoiVyvxQKoTf5KiiGlj50T0NvBodTbg2yh5hrrqLlTqh8apnbeittDtAreA-Bq1kg8OgwbuZTTNdXMhO1j5l5DpfxqT8x2qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار از ژوزه‌مورینیو میپرسه؛ دیومانده گفته حاضرم برای‌مورینیو بمیرم مورینیو هم میگه این یه اصطلاحه من که دوس‌ ندارم این اتفاق برای کسی بیفته ولی کاش میگفت حاضرم برای رئال بمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/28220" target="_blank">📅 01:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28218">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5613ee8bb.mp4?token=EztvYSu40ZROqLZfE4FbB20VTM3tnw9EYR-3fbK7rrONjf503mtBNnsSaLzQ2K5WGWc0lBKTevxVM0JGnOxZSxT1ret-zNLTD30xcM5Bv_6yKrBUxKLN_nJzn4QrGmuvM4Fgfq_1DTUi8gifZ9KMAn5nDcLlaZEMDM5hCbwreUlCoGOGLY5wGZsan7sNjQEUcFhfYuheAq_FfxxMNaTA-17ta_SrNUvHpFfK_D1gersIjMfdFj6TY9T-QO73EkhEEZ-3QjaXjCobjo5jr1SfHTG8W-COMtAURQO6rrAg8b5D3gVBSddqsAXpd09sXWZGcWlPjlVPqiCXFZue5r6Nvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5613ee8bb.mp4?token=EztvYSu40ZROqLZfE4FbB20VTM3tnw9EYR-3fbK7rrONjf503mtBNnsSaLzQ2K5WGWc0lBKTevxVM0JGnOxZSxT1ret-zNLTD30xcM5Bv_6yKrBUxKLN_nJzn4QrGmuvM4Fgfq_1DTUi8gifZ9KMAn5nDcLlaZEMDM5hCbwreUlCoGOGLY5wGZsan7sNjQEUcFhfYuheAq_FfxxMNaTA-17ta_SrNUvHpFfK_D1gersIjMfdFj6TY9T-QO73EkhEEZ-3QjaXjCobjo5jr1SfHTG8W-COMtAURQO6rrAg8b5D3gVBSddqsAXpd09sXWZGcWlPjlVPqiCXFZue5r6Nvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار از ژوزه‌مورینیو میپرسه؛ دیومانده گفته حاضرم برای‌مورینیو بمیرم مورینیو هم میگه این یه اصطلاحه من که دوس‌ ندارم این اتفاق برای کسی بیفته ولی کاش میگفت حاضرم برای رئال بمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/28218" target="_blank">📅 00:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28216">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1ME0Ff5mSBJkvP4KRbiz6PTCRErSWaovP4KLgPJYodVDdeHk5gvYLv7aN5d2xrJpxf-2cz_4Hp35YsjHHxuTqw7h3Wa4P96vTgXBtdkJJv3DtRsno59EX3WI_tnfYS8lNJrmGR43UiDIrtRccqoQb28beze9yPHDu0zjANq8FuRaw6XzieSzy8e9O_Gq_fLFIeUPOUdubl0NvMILdcKSzrGZJqjwJTBZP-8co9w_Xu2JsHXBOXyG356v3Ga_0x0GikUuPn0xApm03CfHr3Hxc_Og9OljGOryLqDqZJY_cOTSQbrLXmWurczzE4uNjy7rU3Q73kYrLxncZxsOIQ-zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس: هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28216" target="_blank">📅 00:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28215">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🟣
هفته اول لیگ جزیره|برد قاطع و پرگل توپچی ها در گام نخست رقابت‌ها مقابل شاگردان لمپارد.
🔴
آرسنال
3️⃣
-
0️⃣
کاونتری سیتی
⚽️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28215" target="_blank">📅 00:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28214">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_3SA5J-toHDmjd7kl_kmtHUlu6b4bkdcf6d3Z8S1fN9DOG8WMkxnRhBxAoxd_qsSGjNIleCGlbuhcCAMVw7D__mAg28e_VcM_PYFo-md6JgvRMt9tYF3TSb6dRk9Rrb6WXrh0WUgBEDyrlXF3_jbNlJzaiNNNA2IUFDWhhkOQxUnv1QNwEQqcdRXBBFXFL5hyT7MVXrPt5z_GdFUkW33FGJRMtwpROU4kQZbDV1ogJQvImTf9JNQa0XCcDEV088CFEuVOVUaktTqOdASoWFOW1bB3bOacfYTnJtSz6gx2-AjKu90_ByyabfTUVxvw_HmxLfvJLQ8bAmAsXPBqVP3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ بازی افتتاحیه فصل جدید پریمیرلیگ با دوئل تماشایی شاگردان آرتتا vs لمپارد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28214" target="_blank">📅 00:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28213">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6905786d2a.mp4?token=JAovtuWPyUOJ4L-5mwHP6ljl5G7daY15LOfmjbS5CG_LQQGgneGzH2lwE9R9MOsIQbtRy0GKAckMglXgbyoQeABm8XZmiayg0-yb8U4FCvM6HG-mK0SndLbjys2fHVKGgEiV9S3nhUDw7Mw4Bur6-Tv_Irm_DtwQcqnikSLOTz3aFokL-y7bjTNhbdJ4hiMWFuqyZ23KcHPYoCNghx8g-dGY_pGpDsel73GeqV9OMJpCTUQZW3Mox70NZltmhvhgiFJmqj_AMdcStf1o0Q3CtTVcrFOsra9CqFkr8QGzxtYsOYlxStjvH4n-6hTZFXOfYlN0o-Rlkf3RA31vPEgfjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6905786d2a.mp4?token=JAovtuWPyUOJ4L-5mwHP6ljl5G7daY15LOfmjbS5CG_LQQGgneGzH2lwE9R9MOsIQbtRy0GKAckMglXgbyoQeABm8XZmiayg0-yb8U4FCvM6HG-mK0SndLbjys2fHVKGgEiV9S3nhUDw7Mw4Bur6-Tv_Irm_DtwQcqnikSLOTz3aFokL-y7bjTNhbdJ4hiMWFuqyZ23KcHPYoCNghx8g-dGY_pGpDsel73GeqV9OMJpCTUQZW3Mox70NZltmhvhgiFJmqj_AMdcStf1o0Q3CtTVcrFOsra9CqFkr8QGzxtYsOYlxStjvH4n-6hTZFXOfYlN0o-Rlkf3RA31vPEgfjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکت خفن و فوق العاده دیگر برای در آوردن سیکس پک‌های‌شکم؛ این‌پست‌های‌کابردی رو یجایی سیو کنید و برای‌دوستانتونم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28213" target="_blank">📅 00:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28212">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSjZSHy4qz7O0PKA6bb9lgGIcTRIdl7WJbsOTTinZYMZbovxYN1lL4FcdWK-Zn2nz6J7qNFWIuIdgVl7am_OsuPNDAB8TOzg4QFq3_KWZMsjlP4Q1LKOdJbrn8T2VuIYthPg9xdvPZRvlsKlaTFVFqyq7jvxkWRWJfDFi8PCr4HDLromKCYr0ZmyP587uqP3JvMgqQo8n3dnlXqIb8kHGh0bPghnGTdjvdlozOGr0_QDTN11T9XmQh69W9gnzJF32kwN0PIkFD-hY-_ihORkhePunFRZ9cs57UeYnQBUG4S0PEZRO3Ijp0h5MjDexH5OPWQjJodSHqwVo6oPtJ-L8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باتوجه به‌اینکه ابوالفضل جلالی در پیش‌فصل مصدوم‌شد و جدیدا هم‌از ناحیه کشاله ران دوباره‌مصدوم‌شد. مهدی تارتار رسما درخواست جذب امیر جعفری مدافع‌چپ 25 ساله فصل گذشته گل‌گهر داده و باشگاه بزودی باهاش مذاکره خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28212" target="_blank">📅 23:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28211">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfqkQC9-WxNboyV59RYTHI11dbzR1Jx6Rf249i3_H25q3Q03AVInEeLj29ygIPv2mlP_Jo35DrTuyERDk26Fj_Ob1Z24QomthloXSnKGYDB2SdNwybdOtoJdwesUaUK2X1M1vVzYRIo3fxzRe4PXBIJewHnxLJnxlYJg00nSWgujaNjLSIzOcEYtk-NhsMVo1K_HM81XY37xDVVfVOM-YaMV7F1l92P1nlRI2ZfG_Sy-YE3RWkxH6ds1-pL_9D_TGrvwPFnJvrGRa8CEBoGuwjm2OYWvWxDbham7RKGIzWyIXnVXGSpmXdxmloD-Zn9_qxp-O1fqUjT3V3n5uBa-NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
طبق جدید ترین اخبار دریافتی پرشیانا؛ باشگاه الوحده72ساعت همون"سه روز" به دو باشگاه تراکتور و پرسپولیس فرصت داده که یک میلیون دلار بابت رضایت نامه محمد قربانی پرداخت کنند تا این انتقال نهایی شود در غیر اینصورت منتفی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28211" target="_blank">📅 23:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28210">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDgWxAZkSDshi5ApjSK-CF0yFzIozQoRBVw8dHWo3nMc1OnG704tyDzRNUm1E-4P-qrbICSt05VVZXeAsdVazfIA1lzvDTrUK6nEUbJQf8MRXfaGD7i3hn7YuAnms_1wyMMHxR6uErxnx_Edq2ttsesLhKwQdN5blTE1xM5EJ0M7C_3XubrCcqviq9KcQIjnCxoSsNwhisGJpEcG6LhXdd03vzQFOAEYHPdbnI-T7hwUTBvAqnf6G1alMmjnH4iketsNHkAdANQtSl4e9TgFbm6ZDefZobrUQ1iywZIrkmOXW1pKQc9Lizkk06YqRgU62OyHXEYchZnRhnWi1ev0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فردین رابط ستاره‌سابق استقلال در کنار همسرش در پایان دیدار روز گذشته تیمس در لیگ دو لهستان؛ تصاویر بیشتر در این باره در ‌کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28210" target="_blank">📅 23:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28209">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EFl7FFSZXVQtYSyuzAZmbCh6ABkQc-26mxbVwRSU7Hmdw8_BkU0-SRx6TSIgMENKQKU0xggvd77EEea8WVNEtjLCWOuMaflQjJIGrYlOG9jHXXqzUHYptZdkDflTIWGUGaIokdOAdS0YIceOvQ1ZL2vC5S8M2ZLb5vrr6lUyQZIdlDY1wYIPjTg2FOdBTvuVO4XyiCyPjcKYb5T33v45ovrhNmWw5SVAb_97h2WbeDROhfCKVjqee-BK6cmXcaek4ZsBdyrSE42gZ9KNe6YyoSlxL09AXywHmdXnxbod-S6KcXV2Ij3ZfEjJnIbB8jvxrjTsneyyZDnbhHAUsfcAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
گاستون ایدول خبرنگار آرژانتینی:
لائوتارو مارتینز قطعا دراینترمیلان‌باقی‌میمونه‌. هیچ مذاکره و پیشنهادی ازسوی‌باشگاه بارسلونا برای لائوتارو ارسال نشده و این انتقال در این پنجره انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28209" target="_blank">📅 22:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28208">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/948db539fb.mp4?token=T4VSNd6SYOPtAVUGtG3RbuaW-pRyHhxDX059uLg91cLE0QA2QN1rnABrVgRkblb1ketvDox8mtbuICtSm8sIPjGU_TtE14yMyndPa4xO6HZ7pTW_MQRgjN365_1e4M5pQz7Nlm0qIGOmLcOxTO9z1ZL2tdHKNo25MvsAKBGvuIk8_aW2BwlqFSXvMDvbXs0mAzGP2BLRdBYmrQMlAdhUrRZN5ye2OhTHIRLDbpWF_oEYtDF5Tz73jPcKEGvMgdczxlvzOxHz91yM6ZxSlE0076393UReitpWJyK5h865c6d6YhPJHbT0NrcvU5kHfnG3QPy4-V8DwX99qCrZUdZuEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/948db539fb.mp4?token=T4VSNd6SYOPtAVUGtG3RbuaW-pRyHhxDX059uLg91cLE0QA2QN1rnABrVgRkblb1ketvDox8mtbuICtSm8sIPjGU_TtE14yMyndPa4xO6HZ7pTW_MQRgjN365_1e4M5pQz7Nlm0qIGOmLcOxTO9z1ZL2tdHKNo25MvsAKBGvuIk8_aW2BwlqFSXvMDvbXs0mAzGP2BLRdBYmrQMlAdhUrRZN5ye2OhTHIRLDbpWF_oEYtDF5Tz73jPcKEGvMgdczxlvzOxHz91yM6ZxSlE0076393UReitpWJyK5h865c6d6YhPJHbT0NrcvU5kHfnG3QPy4-V8DwX99qCrZUdZuEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نون‌بیارکباب‌وسط‌برنامه؛ اونجایی که السا فیروز آذر گفت میای کار داشت به جای باریک میکشید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28208" target="_blank">📅 22:28 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28207">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIJ2GPj2NQT_HjyrUfNfdDS-XIUi126xdLyYlmOleUhrILi_50H4xTR7Dbb_l_vIoI1qyUA3eivDg3Mq5w7-dpE8KZ1IpfsKFqDn3N8XTz8rhGfJrRE431VJGorusmgqF1KTJm30Lz8yz3G3sRN107C98Ri16Rw9TH5HTJAjx1i4ITRmvjqw6F9DuE4Yz7eBd9IJWe5bTsJKWku3M6-UwxPjF0J9gN1Tw8U1RG9CLRSo7HdPeBB3qKL5f6lqmeJfLa-4bcNrcKQUhNMcY-5L1RswCGbPvaq9-I-rZG3aDx8SCODaNY3yg1W_8L45iMjZbRzW_7Grkxt0yQf_ZmHclg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درشب‌پیروزی‌شیرین‌چهاربرصفر النصر مقابل الریاض؛ کریس‌رونالدو موفق به‌گلزنی در این مسابقه شد. این 977 امین گل دوران حرفه ای CR7 بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28207" target="_blank">📅 22:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28206">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaBVStWXvjb1I0VjjO0W_XY2e9Hooost51oghTff9hVAz5RPPb0bd3wYAnPMU4RxScknpHnODivZlhMEN8ID_Jn4rsOWr13UbV1o4oGADu2h7UjQg2jwYm1Wimd_QUPrrFYFWVJAC6uzSxcSjnHAdnX3I-Sg-1Q23uwuA2jUPtWo-_9xfTelVy14JC90OTQXArmnspYtMKpeJ9mvXiT72WbTUzGZf_mA3eH3_ZAJJgKrqIMaHElWPwb56jc4mo2JmneouapajkjwSH4X2Mwjp4addsSvcwBeE1ZB4fmA0f3SHnh8Sfwir7Rm_PwptvqgE6jxKpc3GGCl9c2K52ihPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ایجنت‌ایرانی‌نزدیک‌به مدیریت تیم استقلال به فابیو آبرئو اعلام‌کرده درصورتیکه باشگاه چینی بیجینگ گوان به او پیشنهاد تمدید قرارداد داد این پیشنهاد رو رد کنه. مشاور نقل‌وانتقالاتی تاجرنیا به‌آبرئو اعلام کرده که هیچ مشکلی در ایران برای او رخ‌نخواهد داد…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28206" target="_blank">📅 21:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28205">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1EInrZcHmNy9lYzRD3FEQ2UVJeyLZI_rtQ42NGcF33UIidcEAXsC6yofx54jMEbb1cAL0QVAyfibCifiTaFn5_7ZHtncB8UrVPmq6CzBBTzfUXbBXa7EcSxHvhtK5ONatOt9kybWcm9He8II3M3e4zHlKvBXqQ7QSZpK99VkNJ8a-B3HX__K84GbEGmQrlfXghxaXrP2cxqdu55zbwlMo8FPkNt64rVNqUrI9TFRY0F4fFzbkWZcgYPOcCXMNTDMs_WqAaFfdh6WxSzdvZWJsAxhjhD-O4DqVHdQ_tAc9q4H4KOAtjnFRgsLmUQ9DBG7CAgZzqxZOPTmTZfKWZRdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی طارمی از لیست المپیاکوس برای مسابقه این‌تیم درهفته‌اول‌سوپرلیگ یونان خط خورد و عملا از این تیم جدا شد و بزودی پوستر خداحافظی با او منتشر خواهد شد. مقصد بعدی او لیگ‌برتر اماراته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28205" target="_blank">📅 21:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28204">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvgVoub793zwUcTtPrCjcARTr3OoYxhAgj7HQbcZIVijq-MPx1M5VwUwAEb3-ZOT5GZmWOQBa9LBaybAP3uH1PaPJsC4ZJqPvo-f1DmAIa1a9HvTnhW9wC3k-E-Qs1RE28M2ad7JCJhMNegz_H7DSEbwCkN_ZIY4yrIt1TYmOHV26ZrBGTV7n6iCxpEE8Y-ys4CQfGwOazAOE9KAjj3t1WNRRV74UTqxbdp5gz6WshGzX7Wn7AYMLrq2Fjql6LYFiaYFdr8VUyzql3mW4rAtQEj_c8OyWiQ6GHAnNtienD2wOGtTIGPWABUN2HqmW5aLlDzmXU31f_jHSe-Hf2NmRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شروع‌لیگ‌برترانگلیس بابیمه ی
🤩
🤩
🤩
🤩
وینرو
🎲
⚽️
مارسی
⚽️
✖️
⚽️
استراسبورگ
⏰
امشب ساعت 22:15
🚨
ورزشگاه ولودروم
🎲
با شارژ حساب کاربری و پیش بینی رقابت های لیگ 1 فرانسه در صورت پیش بینی اشتباه تا سقف 50 میلیون ریال فری بت از وینرو هدیه بگیرید.
🔥
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sg30
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28204" target="_blank">📅 21:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28203">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6923293dae.mp4?token=rJqjfMWUJSvPL3nC2-MdCgleEijRU-6ryQK5JlEUFb4kjVI8Vaqge7ROU6l-SvKOhkPS2zyphnG0ijBpvsM4Vv8dZN4x4J4b_UKeraDJ3DupJA-wC2oyQPmA34mtv5opTMH8U8Eb5Di0Bi_KH4PENRaZYRugn01Ej1HPGwPNJxwQBWwel_ED2OgbIbDJnFseXvSLPh6X36OHXgpHPZUD6sv99U3KC6R-7v_FuhIlNQO1TWbkqS-iN8Oy3UodTkbmbtdIZqVP7ySp9_Xx6XoC82viYGNqsBB-km5F_wj-wJU38MIQUQrZMQn5YMQs1vSL2b5-cjAnaypkHmvtiBDwgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6923293dae.mp4?token=rJqjfMWUJSvPL3nC2-MdCgleEijRU-6ryQK5JlEUFb4kjVI8Vaqge7ROU6l-SvKOhkPS2zyphnG0ijBpvsM4Vv8dZN4x4J4b_UKeraDJ3DupJA-wC2oyQPmA34mtv5opTMH8U8Eb5Di0Bi_KH4PENRaZYRugn01Ej1HPGwPNJxwQBWwel_ED2OgbIbDJnFseXvSLPh6X36OHXgpHPZUD6sv99U3KC6R-7v_FuhIlNQO1TWbkqS-iN8Oy3UodTkbmbtdIZqVP7ySp9_Xx6XoC82viYGNqsBB-km5F_wj-wJU38MIQUQrZMQn5YMQs1vSL2b5-cjAnaypkHmvtiBDwgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
آمادگی بدنی فوق العاده کریستیانو رونالدو کاپیتان پرتغالی النصر عربستان در سن 41 سالگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28203" target="_blank">📅 21:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXVbC7FfaRchZmczuvjmUJo7ArFhsEyRygbr7IcsWeO4WB6EiI5QthtE8SzuUviiVI2IiWh0icyJS6AUKVbs1VDfL1TCenU5m_-x3A-dGSGqRX756l3aeMrleFi24WZG0yhBLBQ2sqHXLeqPi-agYXQePZE2Tcys5f44rPpnKQ9qrs9aSb-PLUY69fpSCqTxFFbC7jT-N0EY2nIJnQxSNHZliHzPZuS0L2D1ghP4FGyOh5vhMl1rhFJAc1pVbeCS8gCvxmKRS_-TRSTEDUhFpuhOuczExEgOKQtUIrK_No0batsQEoTSzWvSZjT8efN9VRIjFX3m5uRzW6cRg2LiUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28202" target="_blank">📅 21:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McRWXVJEzxp7w_tBBbHvrjXChMLJ8mpkI3JaNd3WP03z1x6bmo5gZFVtzcynSVeRxRihNW5EUj2_5FQnw0Ki83jOjCykytnMJBTdbI5o0t_19VR4QfqXISuy4T_n2YV9k1SM6Ip9GoXqeYjpqR5WSrU5FJ8XqqPHNnc97iXd-kmqhdHJYSFKtDIhFGgvysRSo0w-dQx69xunQNozIAmpyG-GludcGYMOgzNb1U3nuJQ4fy4bpxHF00Kb-Ai2wU1fPrzDigIQBE_nDeJp0kY0wgPDdwI2V8tAL1Eso8jWlhzqK9xGV1C1Cca5YwF8ammUwzlC19G3QYN2a3xPcnOsvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
شروع فوق العاده الهیار صیادمنش در لخ پوزنان لهستان:
8 بازی، 360 دقیقه حضور در زمین معادل 4 بازی کامل، 4 گل و 2 پاس گل، نمره 8.3.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/28201" target="_blank">📅 20:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoYHnF4zpxRYBR_nZ8Ksr83EqR3_O_flcO-8mlqD-PMtWSQtawSyQYaL3309pJJA3OV-0dQUCfckt9xqSrh43mwvlaGsf_0GHtgcsTBQ24_UJoKcRyDmVWlfK0rsadoSWfuPZ-g6tz71EdUzGcgizenyhjMAs3BX4JBdj0s7v7seZIlIza-ooGgnazSBEUpGkmbwwH7Ye_HjNxsjGG6ukEWxoRfGZB0u75W5wPRydnAlLuq8hauy1ZzpImjGUbHMx69qLzzFZg9KWx3BsVcpsQ-2ijhOzolqLywRIwlXU-sByWchR5clkUewHWm_AbN9r52mja72NdZwGMaZz8gaRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
گاستون آیدول منبع معتبر: بارسا میخواد آفرش برای آلوارز به‌120میلیون‌یورو برساند. بازیکن هیچ علاقه‌ای برای بازی دوباره در تیم اتلتیکومادرید ندارد.  هنوزشانس‌خوبی برای این انتقال وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28200" target="_blank">📅 20:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3847125faa.mp4?token=NKO8AZ3fmlj1ZglCwhDPRHhif8ZV6JtEj-NT_SO2XAbtSnvLf0HQIlW-x_mnvhTgGvHhFaa-EZG4qxSVwcD_zci-D4T0ss_02Ml7sSQkmZi_kFvH1pezY8kCWKGZhwSep_NXHxgHnZFJC7PaHF03d-XDvDsySxOGSDJ1QTAQIkhsuCkEv_emVMKyshg8JK9h43QWw_5Bem4S-CCVhjvQ81MxYmMFby-b040OpO1CZZThNkLaMu3ABq30TN9s7ley94PTZEUtUY2sWrsD4fRyUA3In4M6zc-LTSwB22Ncupz65MXyL5WbzfKMaaIvnMhd88dnd6kHAQy21m7AZequXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3847125faa.mp4?token=NKO8AZ3fmlj1ZglCwhDPRHhif8ZV6JtEj-NT_SO2XAbtSnvLf0HQIlW-x_mnvhTgGvHhFaa-EZG4qxSVwcD_zci-D4T0ss_02Ml7sSQkmZi_kFvH1pezY8kCWKGZhwSep_NXHxgHnZFJC7PaHF03d-XDvDsySxOGSDJ1QTAQIkhsuCkEv_emVMKyshg8JK9h43QWw_5Bem4S-CCVhjvQ81MxYmMFby-b040OpO1CZZThNkLaMu3ABq30TN9s7ley94PTZEUtUY2sWrsD4fRyUA3In4M6zc-LTSwB22Ncupz65MXyL5WbzfKMaaIvnMhd88dnd6kHAQy21m7AZequXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شهاب زاهدی ستاره سابق پرسپولیس: قهرمانی فصل قبل رقابت‌های‌لیگ‌برتر حق باشگاه استقلالست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28199" target="_blank">📅 19:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28198">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03ed3b401.mp4?token=azhb0Ij3iryrDp61nDwbrPl_okLw8b41hqpCI5dgfjZVaWMbENX-Gmx8dPfAHmxzpaBDqydxAq5Hg_jj9U5QF0P329aON2J3gFA_yreCnqlnwHbBn0aAFH8lPvQvsg7nbZs7miendk9zvcRjJ-2SO7x5aa4ZhzFygZvkbztAS5juOfprJ5_w-0J_bRvWzDxiTWRgQN0E9ouMN8Wti3qfLg92nFAUHkb0uI39z9q8A4UgHyCyF41_kzyrYIvHIww_5nIcRcDZbOFi_CO1QyHwWuZJSV2rL506p3tOmxxpnbaT1-ZAYVURp_FHDT1rEZaZHnGQ1OUnUdCbkslQVX6hfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03ed3b401.mp4?token=azhb0Ij3iryrDp61nDwbrPl_okLw8b41hqpCI5dgfjZVaWMbENX-Gmx8dPfAHmxzpaBDqydxAq5Hg_jj9U5QF0P329aON2J3gFA_yreCnqlnwHbBn0aAFH8lPvQvsg7nbZs7miendk9zvcRjJ-2SO7x5aa4ZhzFygZvkbztAS5juOfprJ5_w-0J_bRvWzDxiTWRgQN0E9ouMN8Wti3qfLg92nFAUHkb0uI39z9q8A4UgHyCyF41_kzyrYIvHIww_5nIcRcDZbOFi_CO1QyHwWuZJSV2rL506p3tOmxxpnbaT1-ZAYVURp_FHDT1rEZaZHnGQ1OUnUdCbkslQVX6hfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
بازگشت‌عارف‌آقاسی به دوران خوب خوبش؛ اعتقاد بختیاری‌زاده به عارف آقاسی او رو به دوران اوجش برگردوند. مدافعی که دیگر سوتی نمیدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28198" target="_blank">📅 19:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28197">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb84d0efe1.mp4?token=U2sI-QVW70mvxJIiqFLmObP09U44qQmBeuoB_Qh3I7TDsCV3rbnRHiblRCKGAlORhFi2MzgciSsJleMj6IPwpiZq_oc9RLMmCKRxzWDJovwAGU1s2qbqoOewwkAiw1kgTH1bDXRUclx_2M2fsFLdnQbiByBYHCmQHZIpHmKgJAOM2UQqY0zPBDUH3AdULdPy6B8JrFdPFBOtzm5WUW6N3TP3I1pCmHMshfiKMNYg_szkpRCrgJ47oekQRl7R8swnJdilbI0RfFONLro1z32m-5Jat0pwuQEbkrc1SPkb1OaLRAjVSdaNwdDS0PNCX38uG6CD4rQPSVLM1RGVUxhK6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb84d0efe1.mp4?token=U2sI-QVW70mvxJIiqFLmObP09U44qQmBeuoB_Qh3I7TDsCV3rbnRHiblRCKGAlORhFi2MzgciSsJleMj6IPwpiZq_oc9RLMmCKRxzWDJovwAGU1s2qbqoOewwkAiw1kgTH1bDXRUclx_2M2fsFLdnQbiByBYHCmQHZIpHmKgJAOM2UQqY0zPBDUH3AdULdPy6B8JrFdPFBOtzm5WUW6N3TP3I1pCmHMshfiKMNYg_szkpRCrgJ47oekQRl7R8swnJdilbI0RfFONLro1z32m-5Jat0pwuQEbkrc1SPkb1OaLRAjVSdaNwdDS0PNCX38uG6CD4rQPSVLM1RGVUxhK6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
میثاقی‌مجری‌صداوسیما دیشب‌از پوریا شهر آبادی مهاجم جوان‌پرسپولیس انتقادکرد و گفت باید میرفتی‌ قدردانی‌‌میکردی‌ بابت‌‌پاس‌گل دیدنی‌ بیفوما که این‌حرفش‌واقعا درست‌بود اما آیا خودت از عادل که تورو بزرگ کرد و به رسانه‌ملی آورد تشکر کردی؟ یااینکه رفتی شکایت‌کنی‌که پلتفرم 360 رو ببندند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28197" target="_blank">📅 18:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28195">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQfOvvTAq65colWzC3_Ttd7pDuFrTwhT_lpNMc5Gie5BsDe0Xsal12FDgTN96KqEu1m3W1XEKmgRin8-1JQOdWm2K8GugPu6y8-_HhfMnztcygKJ66gdkA6mag-GU1FkiEMQ-yfHxo8RFByT9WL6JIee-KoerdDD_t-M2ZHtqKO3IHTJelBzl75GVcqW63fEBs_5JD0oRGY5NCljFpVZ9ObxbmJRhLb-JlEJwbBNfZ6ngQGPC4P7R0CtRCmtTfnj6FGgf5JkFwB98t-Vx0TMGavNcIzbT5-da0dTM5fu_VGC8a5_BQCfsU2Xo-C1PqWE7iVfql5IQDh6kLhuS2btwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dkwJ0DAR4ELP-rQUu23WW1LRnpgv3JHYm_ZPkz9qyaYUpa_kTRaseF2y8KrtiUt7ZNYOEd1Aw0kNW927kD7Bx45_iY8_buYGsveepBPbBCOONaaP7Y3nAX45L_4TcHBsYRKPXH7fa7TJugTTjdnn14YaRYYEV_542bsL_FOl32nPHkS2qt9HE5DMnQLsP47gLoAm8v6cmI383pAycVwkT5t3Q8ptRwm6hFb6ZFAeb4eKIqocaRjHV49RCoVMG1PthaoGlthNQblYFuHg159t2S4i7xRPT2O9KUc6irZzdL23B3hKYhIBfABeKvl5JoyE3b2R8X7ACd4D_d00ZQUaEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
علی‌دایی اسطوره‌فوتبال‌ایران بمناسبت تولد دخترش کادو براش BMW X2 2025 خریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/28195" target="_blank">📅 18:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28194">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHKTt1ndTDouVW3Qk_coNBJJOGBHWcuetGjYBTNFAE2vgitw6rQHjxlePRexmU2EMcmpq0UsCp_ZYJlGmTxuJFFomstGdBH52fuXkTuJR88TSWYGKkfBcFy7QX8ZCLx7B8Ralq3zZfYx_kmE7rfhJf7_WIxKKqRClrcZY6JqlcMHgcckO-PwlbxBLWwdUUEo8iN58Dljnomnv4pcYW_Ihh7RZc68YwpkYbBVpJsJxRkqFijUCzj0txDojHn9X17yoJeFEdgvuDVbny3P7iFB0GIuiibPM_5t-eca8-SZVg-_2NNa02NrM-Vbh9A1qaejjqiKKHW8Kre5N9JNhTtDaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیفا ستاره تیم ملی آرژانتین رو نقره داغ کرد؛ بااعلام فیفا لئاندرو پاردس به دلیل ضربات مشت به گاوی ستاره لاروخا در پایان بازی فینال جام جهانی 2026، از حضور در ده دیدار ملی محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28194" target="_blank">📅 18:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28193">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBaxdqMx_8x6bsylUF1nI6CWYYeEb-Td_KrjWEZZbvyfEwXTFwxN9w1RpZgAqKzneqAlVJBvlqDmjLII2ED8nin9DUDVdpo-OR23PLJqUlhgqhtdj2rq960WTktNj8RbEaEGdJM80lJvP5NJrOFmtOLw6TXpPRddlZPPy1T9Z5w35HnpBkxCMumh6g0JHbCjlc2WiavI5rfDXkqbIUoCUOIHfaX8D-S4UJagO_gP2ZznxFhB_VbqKVU4eHUu0TL3WWfStVMp3xyPU-6CzzZ2XGJzTCA0F3p2aGsO0Rw-H5DjaHfEe3yp5q5YN4P_rUanQtHNGJ8oTOEott4lzntl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیفا ستاره تیم ملی آرژانتین رو نقره داغ کرد؛
بااعلام فیفا لئاندرو پاردس به دلیل ضربات مشت به گاوی ستاره لاروخا در پایان بازی فینال جام جهانی 2026، از حضور در ده دیدار ملی محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28193" target="_blank">📅 18:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28192">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDgTi6feIRv92wVmHRYFn2UyKbTz2HUt8oj0cXgEbLG-WXUBkKeRKkpdeKhjDSBrqhxrG_gKM5mcrwLaFqtexXReiIcAhW3pM3VFemO0XodqjLelc__V7lwq82P9r5nrP9EpZAmPu66qIO-o5-VjjKHfgm0kIDE1a2lWVW-tGGwAbazu39dTXgQmJTH_by2U1HGkbmdP1LAp2aQAWh6EL87KTk-NwbQ7Hxya_NChWipFe5CrMwtnqhejP_evgGVirgTn802P0U1vWfRy5mFA9-JLYEqq4j0C-i4pXz3n9C4scB49keaguJrlpRo94tvlXVfgixdWn1cnWVVuOpgtHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ امیر جعفری مدافع چپ گل‌گهر در هفته‌پیش‌رو برای‌انجام‌مذاکرات نهایی و عقد قرارداد باباشگاه‌پرسپولیس‌راهی ساختمان‌این باشگاه خواهد شد. حدادی با ایجنت او مذاکرات مثبتی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/28192" target="_blank">📅 17:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28191">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qz2J5yQVfoM4w-EGdL29ihxmWXpLLseG-zb7lwx9haKGK5DTeaTCIVOEplqmCWEzh9bf3Q4323L4yQlsfqrExlqD3Zhpx51sNmVCx7R1ntB3voY4zRCOdTceQDGN-B-IHp29s9k6yRJkIKq9Q8Mxi3EnHnbf1sZia35U1ZIv_Fb76pgopurtMuHBUrr_Y8lQTtPCY9-GxrOjb1E7UChNkzOiEaU8FhuOiCK3XnLzk78PM2gQr5gjmMzC3r_sXpQ_zj2Rcaep6e50bKCJCyB1KL9NpPQURXuIoNtLgslga3U7-iLhDYAP4dpk2NLieH6iqcuecT42TWx2mYYLvu3EUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسانه‌های‌یونانی: باشگاه‌‌الوصل امارات 1.5 میلیون‌دلار بابت رضایت‌نامه مهدی‌طارمی به باشگاه المپیاکوس یونان پرداخت خواهد کرد. با خودِ مهدی طارمی هم 6.5 میلیون‌یورو بسته‌اند برای دوفصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28191" target="_blank">📅 17:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28190">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMH6vRwilc5j7CNb129dytmEK5VBn0j7ZZFwI7Lf0za4TSwCAw-UQpsrQhcLm-XMe316Ab8DHXPuE_vTq_iJr1DtYgkzZAM7NIwOHnNg3Lhoz_jIaSErUpP14c8YbfNCi4l0ay4vlUIXRy-obZWvMUNhnyng1woHyA5JEfTW8YZ4NSUNHPF5OwuP5P7MsMpyJnDnMVeYDwEKIdwh6IWhdrwPIq8ChuWWLhgbuW2UwVCDTAjQ2-NnJ9wGX-ILxpJyRS_hSEFNajdMOYRplDql6P3rWM2JN_L4zz_dKGqXEkHe-NKi7LMveE7DT1IcCktE_R2IJYbNlaw3DOzKtQAsjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه الهلال برای جذب اولی واتکینز پیشنهادی 45 میلیون‌یورویی به آستون ویلا داده که به احتمال فراوان باآن موافقت خواهدشد و این‌ستاره انگلیسی با قراردادی سه ساله راهی عربستان میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28190" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28189">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18f9090bb.mp4?token=UdCa4XFHZqqSY05lMcr2TP1akoXSugUcwjmlIHv3kYx5bmGnE2RhTLmv_BetZ2Ii6oaPyZCJNnOcaewPPyQoYmuewy9oYSC9ZdajkE1NQqe1QazMBsbAyld4rzYJyNsCN0En4aSnlB0XPMhpW9n5xjUSDcZyEHPiaKF5DZIppDjuybU2hPDXYuomRPciXNKRt5st2AsZ2DjH3ieyfgaXRuFdN1tzq-jwaano5c4HOX4jHGWM5urwzAvKmMysiMQABHGMmAITAr66qrl-aTGEca7cSk9nHsNe3BsWRdLAIhDcpEOHJw7RYFUOTftzHhggE6AFlRvO9yoDOwGAdNCe04Jw1zXeAflHM6KlgSYDEqd_X8opSRXkV_SN2dePzt_8uE7ZfvVGOj6wPScZBaRtRnqlCrbK_RpPtJLFG7kSWV8tKoHwl5mJCSnFbEs9UqPUDe4c_cmyinlfVgJsOlSVtz5cBdkRvn-GN4gdK83lbsUtrDuD6IAH3kxvfacIimqIRjY9GGU2wubSjOn3O2XI9o4cL7p8PATSZWBTGWZIc7-G0Te6Fh_Gd9VZQFLuPnV4FsSUUsuitweu9-rzB6HpiEbDZI5q6VxgB5heRts0sCW5Kv8MRcljqnMJ6Iq21Wq7DOB6it-ChrPn-SSGfnP7mrqiE9p83VVBzTQ047hap2s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18f9090bb.mp4?token=UdCa4XFHZqqSY05lMcr2TP1akoXSugUcwjmlIHv3kYx5bmGnE2RhTLmv_BetZ2Ii6oaPyZCJNnOcaewPPyQoYmuewy9oYSC9ZdajkE1NQqe1QazMBsbAyld4rzYJyNsCN0En4aSnlB0XPMhpW9n5xjUSDcZyEHPiaKF5DZIppDjuybU2hPDXYuomRPciXNKRt5st2AsZ2DjH3ieyfgaXRuFdN1tzq-jwaano5c4HOX4jHGWM5urwzAvKmMysiMQABHGMmAITAr66qrl-aTGEca7cSk9nHsNe3BsWRdLAIhDcpEOHJw7RYFUOTftzHhggE6AFlRvO9yoDOwGAdNCe04Jw1zXeAflHM6KlgSYDEqd_X8opSRXkV_SN2dePzt_8uE7ZfvVGOj6wPScZBaRtRnqlCrbK_RpPtJLFG7kSWV8tKoHwl5mJCSnFbEs9UqPUDe4c_cmyinlfVgJsOlSVtz5cBdkRvn-GN4gdK83lbsUtrDuD6IAH3kxvfacIimqIRjY9GGU2wubSjOn3O2XI9o4cL7p8PATSZWBTGWZIc7-G0Te6Fh_Gd9VZQFLuPnV4FsSUUsuitweu9-rzB6HpiEbDZI5q6VxgB5heRts0sCW5Kv8MRcljqnMJ6Iq21Wq7DOB6it-ChrPn-SSGfnP7mrqiE9p83VVBzTQ047hap2s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
جو سکوهای ورزشگاه پارس شیراز در بازی این هفته فجرسپاسی برابر صنعت‌نفت آبادان درلیگ‌برتر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28189" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28188">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0qLna2wBy0MSNY3R_m8rb6oPwj2FArfIXyK4o-2YEg1WJcggqp6zUhyd7WUPsaxSQAlAolVSiKDythZepPYm13sU12HSj_DroXEpED-rV7Q4lpmkgdYf7pGqDmoL-2uHLmkunURDD1GLWfbqHAr9bTyyklWkY4lRvIrRjFgQTUnLr4CdPvnKlwczmVNLYZTP_R7yTKk2CJPYTpxoSJ4dhkz7TVx8QnuQm9Mvoth3Pdo8wKohswTbnHRyW5mhM5atpoBgDlOgAws0WeNKxTS76CuqEfqGz0pEMrV1_7qumZlyTEw3d-ay9HqcGcgJxq7Mum4eqNSFTo5lxxMPyxHHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته دوم لالیگا اسپانیا
🇪🇸
رئال بتیس
🆚
رئال سوسیداد
🇪🇸
🗓
ساعت ۲۲:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی در بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28188" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28187">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phzEnV_t3dbzmzf7aTt2sGy0jY_4tdRbOir1MqG_wz2juOUz_RaKxasJZUfEfBWbSKnLOP_MjHZWclmJLdIfJooSdnf5STwFa86FE8cgfI_KbVjq3N6sIaqnfIhmPLDOo3yiglYe3RceHF9dnwFSwvdXVwqYLAqawMOvj6C8UjNZHhUNba6bweb-bNtpARW4pwts2GZciFlgxBCVARcBfs3K9n7n_BzdRGI9zqSfIOlSk-Uo8e3cKSv3CESzJDISpqad8QUh8iTseC1JDhLtNH6-elcMvSV3eMquGSqof9sxb30uXWQURWf297_D9Jw1jDOuOiXEmfb5TSMnHRjujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28187" target="_blank">📅 16:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28186">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKGMqpDPBoEm_05xXJm1YhowD3X_3ptyZApsUMMB00Aff_z47EMBce7U-zWh6gDepuJSyC6SbGEaOf7ghouTixUMxMefOiP1MHiVC84JhDZY3odss_qnYIS-2BMS19nUffEsiV_OfhsI6eivk5qQM9tJlaJ6xL8eoDC1m3DfsJ-rSccLZ4PoF3hEnrXAJTPVBR7zId81mwC_iOeWhu0i6LLG-qa5K3DKchXndErCML5Ajgy-ruY_WphumdQBNDjpr1unsgp-GRqb1zdowE3ZPEgtDSFtz0hKEC0-pkLPYqYt0iwQpR75znvXUolItWqtBoN0sOaDQvf_-Z2r4FxZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تراپیست ریچالیسون رو یادتونه؟
از افسردگی نجاتش داد و حالا ریچارلیسون برزیلی این طوری از بانو آماندا خواستگاری کرد و آماندا بهش بله گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28186" target="_blank">📅 16:12 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28185">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrlLNnC5meDhEo5j6bEGNVz2MFiMGhXstVgqGhjDuRweYadN2fohJ-qEJBnI0nc33acdvhRgzLiEM53VHa9ReeDg0oAG9j_GyitRZ8fUqoPxypQHUVi3fiLN0Ur27IPv66ucnHa-mbUSbyXo8WVY95ittW0y1HPUsovS81Tv96ovmKPTKC8rZe6Fsh6mQFLURFwpCel0FNjP3Z57azXGGWwiF04oVWcFvPsgx8uyP1VCCy-hkGynrkOPgR4W-ShyVNecGZwKD5WzKn1qU1onSMq0IO3AysoB5hRg8i-IGIBo2NGbzFrKj-IWf17WnOLigl-y-Is9XOxWJnhWPV-oEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد زکی پور مدافع‌چپ جدید تراکتور به دلیل مصدومیت یک ماه دور از میادین خواهد بود. محرم نوید کیا در مصاحبه اخیر خود گفته بود که چشم تو چشم میلاد زکی‌پور گفتم اگه تو سپاهان بمونم هیچ جایگاهی‌نداری چون زیاد مصدوم‌میشی پسر خوب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28185" target="_blank">📅 16:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28184">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7c_h6BOFH4Pka4yfleFLvbzW67gDcTRuY9meFZ8tedEiWwH0Uf9iyH1wUFw-j3chz_bsLClFYtEfkL_YrpLLYxfW-ientRrG2YmFoVkJ0BUzxU8YQltdxTtuNGMj8bt09_qlLQAcAOR6UiXefNqJNr5UnB6YhC8pgfmLoHeRPfSRAvN_2TyBb0AL9s6X5jWAis3mUV0yogp9M3SzEYhgLPt9VUPSSIFs-RTI15p_FR7e0xtdKCCWr3Uqn3liOA72iU47W5EIS4EYqgJLtKvTm-wU7tdpUM556hw3x44he_RLeJmAV-ea6NxTjbLvt5OlNaeTx8jACQ-nmM_pFRwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
برنامه و تاریخ دیدارهای دو تیم تراکتور و استقلال در رقابت‌های لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28184" target="_blank">📅 15:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28183">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S__ENHkLUhpy38dYYPzlfMD722epoiP9gBvhECade_Bhfk2nZkHGo5nSmChW4PwxMSEGTbYZw801sji8VmGr-PWus72e95ZY5nUjqghvKkKoa8Ro32sdQ5CdbbtHdRQiBj1Eu7WnEtYqEp6RpIrjE3ilU1DFIvx5y7KHJEIgBzP0jG5VjfIu8bHrD6GbTLDo1GlcghaBWu1JdHltdlzeKZPlY5EDAZ0JJYfp5_aoLlqgeO5j4UB01hc3juak8blP9yDyVc6bG5i8K6HpgHaxYpSkEZKD5hZGX83YACUVIyO1gp1Sn7I_C4O-dW2ZvfPwv86RPIyDHB7NoILaAiFA6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ادعای کارلوس منفرت:
دومینیک لیواکویچ گلر فنرباغچه با عقدقراردادی دوساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28183" target="_blank">📅 15:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28182">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ooQu7jGLgmnFpTBojx_DUsBKskgDHez6_Rj_La6OF6P1LqjuED7lkctff4eVvW52_aEikBeWFz4yTCaqDyKhQ8ZbAEoOoYvmSLS9SkhrQAoZE_IljOwgAnMLLybhjq8JCkhITqlteShjdjKqt2Mg-e28NDIGLdXHNQiiqmyAp4tHU_NBL05--uOUhPOPKYaAYta0GIgxUCdmr7Bo2G4SNOUBYeFNKtAS_UR3T-emE3lM-V9VUFHG6mF_j9u5DaWvKu3vhs74z4gSqA9k9jl9RDCCWG3hksuVy55YlR440-5KcYpnZvEYzhk7VaPYmjxqcHMnzLOXshiePCwbdbY-KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توماس پارتی هافبک‌دفاعی سابق آرسنال با عقد قراردادی دوساله به‌ارزش 3M€ به الشباب پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28182" target="_blank">📅 15:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28181">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptoT_ckxg7OJUXLHmpjRMIXzJgXbnxh6JDATe6TvdcFmi7V8v3k7Rf2gI97LbVECBK9bP3ZtOtujQtgxh7wT2MzCqdL0wByD1S7SjynosdsFQf2Uh3HmTKSdX1-fkKdZ7QsJUnhqwZ4rzCHccfQvyaky2I5e64R5Sx6FVmY3wFn06p3XamLG6mfEL22Pvq17k71UidWkD0S9e97zzaZ-NX1YmHeF8JE3MY5w_jv8ARQegn4zKICWoM0NubQsdSftiz1flFbqmcpoge5iAbkJ9cuKCnELEiQcHweMrR-KPMC5wPrtw2NdTmglzBLsLsjjOj-e_km-9KwQk3hRRIiS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ محمد حسین صادقی وینگر 21 ساله پرسپولیس به مدیریت این باشگاه اعلام کرده وقتی کادر فنی اعتقادی به سبک بازی او ندارند قراردادش روفسخ‌کنند و رضایت‌نامه‌اش روبدهند. صادقی بجز گل گهر از سپاهان نیز آفر رسمی دریافت کرده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28181" target="_blank">📅 15:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28180">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx0JOhRafj1GN8k78sKMvEoaFv2m2JVpmdXFC_UgaDBxj6tqHPOC17u1HeW-RSA4xP9sgWmI_IkdoPJyxr5P0Z_I4dGplkT-zc_2Uy61kxQZgduiKuW7yO0T84ueh56JxDziAIOH2VjhsWod-qm1dG4z9sxNHC92H4kh4WLFl6wLzp32OuiI3pfzV6zIPYsux6dV35Yc87YtSyYFF2lsoQ9LvFNZOBAJdA_L7T3eKwzc8KbJ3F-EzSxjFb_df6DSOoy3o03JQgdMbFZMNAlb1O8-lwE4Yb77HCH_-P43y0pgf7uy3oRxEHNq3MYUy3GwLj5nWIOlqvyPyVGneB7bdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ شهاب الدین عزیزی خادم دیروز برنامه سه ساله خود را برای مدیریت باشگاه استقلال تحویل هلدینگ‌خلیج‌فارس‌داد و هلدینگ تااواسط هفته آینده نظر نهایی خود را درباره مدیرعاملی عزیزی خادم در استقلال خواهد داد. عزیزی خادم اصلی ترین گزینه هلدینگ خلیج فارس برای…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/28180" target="_blank">📅 14:18 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28178">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EwzFwOkRFfr7NA4iIRnHHeAwDNsWT5y8hzNWsOxj405wDvOemHiTcItccqS-ybdnpwdCNH5aBen0cKbnIoo30W58UwsiJLtKZK-D8riBsOGI_OB5Y1Lpo_phN20anK0XWwWi95KmZ-tdWVfHk8SwHfKM2gRAcvzCDY3KoFOD7DF95sI83ECKx9_7V09p9mmIkvzfNAT0ShhJcYvpkeSRs3X18zStGn8MPTTqezrXzaGaqYqMck2rHblvuvo925WKzm9LpZ1HwT3wFA6lUIkJLocbckaOEVNBboU2uIW_cQ2bdM3V8PzFaPRfsCSxxDBcAjn46ia4MIMyYhnkOBl1EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OhRqBimTj0VH35-pWE2Gax4l4w83EMQYHamE2xlUK6ecneJiCZRfr1Wqg9y1PXscDXbrnZia4Kb9mqDW6ewl3Fiip5PQVtVw_D_hYFRy7vAQqXB25z0GrGVbpEyDO-V9zbTyyEOs-6g9kuezu1lceF-An-jbB1___XjAVJK3js16vKcRoG7sFbPcjbOY7YC_VctHl-mOOJ8vOjfO9oz6w7TqOUexxLmXqaBoAPOPCBkV5CYn7MEatUCYHRabrRG8KNskal1cU558-27xzlyYTxiw9zq7brCSmUkALj7Loa9wmkKkRC9kOxoakm62jSJcvCFhoXHJjqt3S4_uitFqqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
🔵
برنامه و تاریخ دیدارهای دو تیم تراکتور و استقلال در رقابت‌های لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28178" target="_blank">📅 13:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28177">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66740b5afa.mp4?token=u2a1j-3VW_v_gd9M_VCWXpNa2tvGkpRIx-r7yvD5QQf50T3KbtGGAt7bvkNv4OIOLf5klI9ZpO4830WCyS95V9Ijo_p1ofv4PdVaUoxtY4GU0vRPwtkVHzn-hf8TStPPYVNZfqze8CC81gnDWosBrLaP7UU4X4jC5qySkqtQul7xDIr6cRJ7q_NSpunECdyIVDiduO6hLVe7840yvRaAji11709_upwy_-lZbKRlu4cHVU4W9q77b8mHLyEgKwd_RcgaduU55waJxpKNDJRefzStJtDBV3PTAyDG4ilTvsqJOm9qsWHcwmFKwlfzGJhfq7rET70FKzX3oV-pud2xlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66740b5afa.mp4?token=u2a1j-3VW_v_gd9M_VCWXpNa2tvGkpRIx-r7yvD5QQf50T3KbtGGAt7bvkNv4OIOLf5klI9ZpO4830WCyS95V9Ijo_p1ofv4PdVaUoxtY4GU0vRPwtkVHzn-hf8TStPPYVNZfqze8CC81gnDWosBrLaP7UU4X4jC5qySkqtQul7xDIr6cRJ7q_NSpunECdyIVDiduO6hLVe7840yvRaAji11709_upwy_-lZbKRlu4cHVU4W9q77b8mHLyEgKwd_RcgaduU55waJxpKNDJRefzStJtDBV3PTAyDG4ilTvsqJOm9qsWHcwmFKwlfzGJhfq7rET70FKzX3oV-pud2xlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/28177" target="_blank">📅 13:28 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28176">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwFknWes13Ms69fcQbRjqPWKHgKWOecI0NifO_5Df3M9d8AUuiuLXwtbf-aXC7IGf19Wcx7TLGYlsNxZj4kSAr-mwlod3_NUU8T_BnbAwUMUKvoqZijiHooOp-OF3S8Rk7EoECcWFOAqwnPT0D_zMztCRzYZ2oyjWZKWsDeV9e-bMaPoeiiCU4lGGh-iR24LL7hdtc0jW0uhuW5U9pOQNYZTdfWhhHlQBA17DXkAGggi28L9PynIBoSXlWgfQPJvONtppGfunAGGbS0AVlXlB7QSio9ibEnXZM7S10hKEaJKKRqT6pWudHOfpXsbpzHJuILm57cg_9BcjdpErGJZLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ فرزین معامله گری مدافع چپ پرسپولیس بعد از تمدید قراردادش باسرخپوشان راهی سربازی شد و در فصل آینده در یکی از دو تیم فجر یا ملوان بازی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/28176" target="_blank">📅 13:25 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28175">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdtS9p7sp8UYeZqFrQMVoaNjzH3sB2tUQzHhRwkNQNLbPaS9MgCk-3SOYorkNuoLh3NDiz5V8wxqtCtETjHkblVL1ekgOfAjv0Hck6p3LWgjrHltV9W_9EypytD6ZSLQUDKQRmCIFM9O33Y_NRVHBQ2i1UnHhUDRC_Ssey1GjZjNelM-zwjqYZuhsylkBneniIb84fEY3JXwnh5kDngraTL0aSNXjzXdud-npcSzZONzFrq6A6hdYnZhpGR2Nss1gtOLErr_a5l7CnrazBGZDrBITNEL8GV5OCX9wdxSKbk_H7LGUuXvDkUfJ_2ruQMT9Sx7gTsU-Cb01qgOMZBDlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآستانه‌دیدارحساس باتراکتور؛ ابوالفضل جلالی از ناحیه کشاله ران مصدوم شد و فردا بعد از گرفتن MRI میزان مصدومیت او مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/28175" target="_blank">📅 12:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28174">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gao8bFXJqSZz0jeqqRidNyak_2rC_47AqfEESuFAgir6yv1U0mMf73hS3NGmuVSk_meDzlpDZO1kxORbMwSY_tSbVBYA34UyRAsgONA2rxxzQRrgoqf_NIB4N0v6h7BuRpfN6K_fLEWT6VcqnOr3VZyeU_JPDqt5zoSbCpHwPpN8Q6MZvqcjMsqHQJOwjo_jM5akFo-ajQL7Yr58D-zSYBDWk3dLO0vqNu8QhjydHsTICDT0cNawf_E6GlVEBxUTtIEv5CjCKORyeYiNQKTENk6XeibCM--qmPho5jPXro1sxFlmqw3eR5F3VTX_670twbatc65BU3kK6C_grTJ9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
روزنامه‌الشرق‌الاوسط:
باشگاه الاتحاد به توافق اولیه بافرانک‌کسیه بازیکن ساحل عاجی سابق بارسا رسیده تا او به عنوان بازیکن آزاد به تیم بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28174" target="_blank">📅 12:44 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28173">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4zjf3b_prWZIwZIWgEkmAXydlrrP46d-xPJ4cyC1kRQJOyfP5Ey1VdTZw4DncT1xFrcxXELGq6pa_fF2DjeutKg-vJN1ugO5TkZCPd_OQRwsuRWLHTGSUiwsTU9d9feV9aUEMxZPxxRdguhnWXcpHnsjW-u1afJi4lilwa2kTBdRO-7-zwAoGhYQ2rPw1UTnEsGW8vCOYmhdeKXleQo_jwIWlKSjfmjhSde4J_EqXHxVw9NSHE1C5tBCgPE3Y4YsxyHBRQHVd18IqO1UBZt1XrxdN63P6ZLhxFpQdoe0XlRBJGJGY5JK3SEz_IsxehFxpyvG4qUJoFta2E54MtO3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت‌امارات: مهدی طارمی به‌آفر 6.5 میلیون یورویی باشگاه الوصل امارات پاسخ مثبت داده و به احتمال زیاد این انتقال بزودی نهایی خواهد شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28173" target="_blank">📅 12:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28172">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3bd66449.mp4?token=iI_vm_7I_B212IVS5KpsdkbGdi93NULae3CB98gS8zvQvH3lIznTE5z1Z6ePz0XZCPfJ0FKs-thzi3u3HM5uOS66g9fJJOMThqblHzJRMK28Erhc2jmlD7o0c6-R0GG0yHf9xych8kUUzAKxiEvSUsdOPHYNSAsPHUQfmmjARxLt3ZPuHhsErgkUF9MT-kiDxSpwZQsgYHCSm8XdLOi7NBNBZCLSTXaXL_RaLszF0kX2raEmuiGmb96I4ChTi8B6wZwkUlvVJJDxSQCAFs_6M3QrThSXDDdYNy9e9ybz3r1ZiqN0uFDBwlzt-OaWSw3SUVsCL_6I_xcvFbrAID5Z8I18h7NT2BrTu1xUI3dDh557sKJz59qZWLoaeZvfylvbiJ1vSI6IaGKw6hBZbIzGcwZ_a56w2Kh2OA-P8OffJQMd_Tzeb9_SbPO8KIaZ4gCzA_pTZvBotrorBStPxKhLk5NhifctZULs57uhqonKIf5vefnHyZNQmeRTPbLFjovgJ1nDn4K08okMR7GRrWByXov-tGejd2Dc-q4VbRLUkQ8TAdY3Ya234GZdfeWiCgZzY9JWXFgFGoFgQ0zd3kru6E2NGmRoTnFqvTq2xk14cFTRrKnd0brkdHkksFTrrn_KySx-cBHNSoskX4koQl3yuaVI5QP8HojtsfPI442sX9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3bd66449.mp4?token=iI_vm_7I_B212IVS5KpsdkbGdi93NULae3CB98gS8zvQvH3lIznTE5z1Z6ePz0XZCPfJ0FKs-thzi3u3HM5uOS66g9fJJOMThqblHzJRMK28Erhc2jmlD7o0c6-R0GG0yHf9xych8kUUzAKxiEvSUsdOPHYNSAsPHUQfmmjARxLt3ZPuHhsErgkUF9MT-kiDxSpwZQsgYHCSm8XdLOi7NBNBZCLSTXaXL_RaLszF0kX2raEmuiGmb96I4ChTi8B6wZwkUlvVJJDxSQCAFs_6M3QrThSXDDdYNy9e9ybz3r1ZiqN0uFDBwlzt-OaWSw3SUVsCL_6I_xcvFbrAID5Z8I18h7NT2BrTu1xUI3dDh557sKJz59qZWLoaeZvfylvbiJ1vSI6IaGKw6hBZbIzGcwZ_a56w2Kh2OA-P8OffJQMd_Tzeb9_SbPO8KIaZ4gCzA_pTZvBotrorBStPxKhLk5NhifctZULs57uhqonKIf5vefnHyZNQmeRTPbLFjovgJ1nDn4K08okMR7GRrWByXov-tGejd2Dc-q4VbRLUkQ8TAdY3Ya234GZdfeWiCgZzY9JWXFgFGoFgQ0zd3kru6E2NGmRoTnFqvTq2xk14cFTRrKnd0brkdHkksFTrrn_KySx-cBHNSoskX4koQl3yuaVI5QP8HojtsfPI442sX9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی‌از عملکرد خیره کننده و فوق العاده پوریا پور علی هافبک‌دفاعی تازه وارد پرسپولیس در دو بازی اول سرخ‌ها در فصل جدید لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28172" target="_blank">📅 12:40 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28170">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWz919YTSx9GdI4DOOCDQYc1zonEgBs0vkkZNpmWIKEBkyo_QRBjvgJFV1UYF4Tp9hLASCeKhpBiO5MuxE5Z8WnjlCIwD_NT4SyKCLqpARTdxQ-YUlG4wafKUSLRt4vzMBzceKfNF19i0tRnD572nWhwuw7kY7xAB26EVMiJ81_IYrFSm2sg1RGU0vyLGs0Laz0VvcZ0tqseH__XJcQsSwszSD9pWvJk6Y1hZek8EzsVJG2gquOns8ORyxaeGjNEIEKLUkCD73xd-x22TyqzFGa9ygmT3BOaPzeuA0h34Y8YEyxPgHiPBkUxhf0Br_0UieBG5uh2uq-SI9Z-leprXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیرو خبر ریپلای شده؛ معافیت تحصیلی علیرضا بیرانوند به‌مدت دوسال دیگر تمدید خواهد شد و این بازیکن این فصل نیز در باشگاه تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28170" target="_blank">📅 12:26 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28169">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌پرشیاناتوسط سازمان لیگ
🔵
بااعلام‌رسمی‌سخنگوی سازمان لیگ؛ یاسر آسانی یک قرارداد دوساله تو سازمان لیگ داره و الانم داره سال دومش روسپری‌میکنه و قرارداد جدیدی منعقد نشده بنابراین هیچ مشکلی در این باره وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28169" target="_blank">📅 12:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28168">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X45IZroIY7qOL4gCmJirg91hRQoKAeUEm3ZCes-eZxxfOzmpxxd0Pq2XMvK9O2KfUOw5P6lPgcG2PXqQkcZ_KKHvIPK2yE1ctFaiNV3lUKzIhVpjXNw9X2P_n8BuucICuSfKIoQv7HArvHLtj59NssPv6O6wsDBFv-Oa7RmEjbuQx1RoVKoFe8qRWIxTR3Xnz8qWC8fywFpolDRMl1ppwv8qqcOQzOT7m9rDiV7EfVZ2kpMpJ3afs_bfBXqlgbyKmVKBko-wYdPzkzevxwMDm6e4x9AsQrVf3z1Hi059sVVipBSgZ6xjZZqWMkksnrGhDQ6b0jfmOLmqkPvCcsCDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امید نورافکن ستاره سپاهان بدلیل مصدومیت از ناحیه همسترینگ به احتمال فراوان دیدار هفته سوم مقابل استقلال در تهران رو از دست خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28168" target="_blank">📅 11:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28167">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HvxCODh1qA0R5HIQWGPi3lBeL1iLbrh59mDTfYxuo9hYFIjSnxkOBiMvPR10hZTAV1zGkgEKB1hPM-6J69av6cK0t6B7jeG8_Lk33VLgGXi7Mra_lYg0P_MxFFnaRA6_SeeGhNUabQFlff0_azb0C9xNNypx_hyyBEDjHbjocM-77GWd9E-Q5GtwLjv82RR4oEb6qGdg8rk4QRaX5Pz_FOGeI8kA4gs6mzhXYM1ImiIISRd6vppaJeVTzECfMDNmhhDT_hrNd6n8QwFgyNEUYuNRfszsoIBYRSQbSR26A_lma-jmfwBfPXwS5bQNuNebyHOj4IqVTYxCXQyMXisX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛ باشگاه گل گهر سیرجان به خواست مهدی رحمتی با ارسال نامه‌ای رسمی به باشگاه پرسپولیس خواستار جذب محمدحسین صادقی وینگر جوان سرخ‌ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28167" target="_blank">📅 11:23 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28166">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGqSUA4FsDT-qcjR63OscPxw1H7vAUpJYVHJLJrCHVPcczyVM7rmFz0agfEFxjX2mggnq6NTBrn_Nj1R2BvIJKob9EHXDsdRrYppvLT35wdwpvnQFi1d_v_aq2_2ooJmH2JZyO3CBV3PzhadSilBQPn_KL4lSBBcwnI_FLmXGSPZUyWYA1ppc66KiBNAmbiBJlUw1O91c2GFtUa2rsDtV1Tmtt4JAnlnbPvogcrETGP2CLMaQD_FcrMNI6glDAeqMAJLukPXlcyI6g3TbaeaFStp02FS95hzjdShhiTZjX7tF2hCEPkw5TsV1sXlG3jZhmR5_xPBRhadXEOfq6RB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
تنها سه و چهار روز تا شروع دو دیدار فوق العاده حساس هفته سوم رقابت های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28166" target="_blank">📅 10:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28165">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/035583e200.mp4?token=huX1OMcs-_Cc_3F8c77V3NXrWzULAqnsNu6MsQ2Yj2igjbrghBt5o1QtgKtXcPvXoh_fbaS-7MHYW9eKXsWiVJQZY0ZRSixMVneeQDHyY_2NNOr7YKNQe0ZzhvScFG9uTGJE0KyBPyArJ__r0npE3e4h_miA5n5lGxovshVmkDen_yA812aI0dfa46DTuiE3e0WUvS48SmBRC1IaVEKnFOIqDMO3t2hb4lrACVR9_rovoKG_FK-4M2563u7YIY7K-tBjwCsWhQkh6VXdPebUscdo9iZ76ypjGVL38-9uCglowINLY15kMyJTgilLUih-sfpxTMTMHX_hUVftdI7t6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/035583e200.mp4?token=huX1OMcs-_Cc_3F8c77V3NXrWzULAqnsNu6MsQ2Yj2igjbrghBt5o1QtgKtXcPvXoh_fbaS-7MHYW9eKXsWiVJQZY0ZRSixMVneeQDHyY_2NNOr7YKNQe0ZzhvScFG9uTGJE0KyBPyArJ__r0npE3e4h_miA5n5lGxovshVmkDen_yA812aI0dfa46DTuiE3e0WUvS48SmBRC1IaVEKnFOIqDMO3t2hb4lrACVR9_rovoKG_FK-4M2563u7YIY7K-tBjwCsWhQkh6VXdPebUscdo9iZ76ypjGVL38-9uCglowINLY15kMyJTgilLUih-sfpxTMTMHX_hUVftdI7t6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیگه‌فیلم‌های ایرانی هم نمیشه با خانواده دید
؛ این سکانس جنجالی از فیلم «زنده‌شور» رو ببینید؛
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/28165" target="_blank">📅 09:55 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28164">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL-4ZVepsn9HgHIg6HGNeFW2iO9iGyVGaJNK5YOdp30Y7Sgs5JmAN5IPe2vaH9tS0SuOF60i1vqCY-ImVxljHX5i7CCi1IJ7c19gaS2ydTloWqBMVYqD_vE4sw-1pPnnY9XHXWhSi-kOKeq0tjvgUENyBNHQO-FKuGJ9nlnCNIDsXHOvkVGasa-g54LjU3_UE4RAlOkRK394IVupPXCwhtFKQh1bDmakWi7dnpgEUC3UMlFqOqeOhw56KCaDMrtsOxEmN2V3i8O7_C1ubVqEJm_i3G4ISLAkYHMrXz_d5r_pFvcM1GbgwVYdX8qE3RRlFQBAjH_2Vykw1m-VG4cUlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
با اعلام باشگاه بارسلونا؛ ژائو کانسلو مدافع راست تیم‌ملی‌پرتغال و سابق اینترمیلان و الهلال با عقد قراردادی سه ساله رسما به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/28164" target="_blank">📅 09:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28163">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rGjzBBP7jCZLs1ra3MGRoQVnvKPmny5Mgc2lh_-z5DKHmHmLI3fqb8Lk7PVrOaAU8FWjZUpCdBN6hSQ-6ZBtIl9NPceWUU7L_aOruzGN6jES5-NB7LaHEKlOfz03TBqVT3wVMu3Snt_AGq88WOgq_XCreY4tYgTMhobR5Z2Ou4NvBZGRDK2zZ95VOSlveevs61Zhm3FISfDyX0dxbfrRdxlVElhanvsaGk53xku8EhEUE_9OiNlx79JY9QqgoemSquOlZlt79I2ap2_k3BffP6-b7sfuYNCamnX7Fx9tvFBGUp74c3SUcr2sQfp16wEaO6Uhlhm0OFlu67tUB9AZ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب بالاخره هر کسی هتریک خاص خودشو داره؛ یامال جان آروم‌باش داداش تروقرآن، هنوز 19 سالته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/28163" target="_blank">📅 09:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28162">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcJHb7uzc6zODLRBxz2GMumwn9VShe-8H8yJULAg_nBxpJm9LDa1Ea5utr6E6ClSPVrVmrvrM4StXOaxHdKwToskAUwIg8LLVllHcddIPRq0YW_I78is6snsdVjrQq3VLlDIoQs3IEsflzhM8Cp7bLyE4AUFmMNZ7E4Xbr101T8nGYhKRJA6U_HNAct59tsPEW9eQg_su5uChgpGIt1-BwT63yChTu-XVblOQ9YGftCJIhxZQONgnTFVWLvOPwEiCQxSmra9Z-o__Ucgw2ityt-KOTgE0Tbz88G1KVzf23BVRAOh0NCyhvpSc72ia10YHWVaTpVns06XVUG18ZKv_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
استقبال‌ویژه‌بازیکنان وکادرفنی‌تیم النصر از کریس رونالدو بعد از ازدواج رسمی‌اش با جورجینا؛ وایب صورت CR7 خیلی خوبه. حلقه دستش رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/28162" target="_blank">📅 01:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28160">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acZVWYCgkWgMWe78EX4H0TPAg3TM8bPURy5FBT4TH2I3KishOmdc6x42NgdUmQAk5h0m5ABOQlY1z1xqkRDmL0y756BHNJsTZGYCfp90ufeVBdkNlKra0MtGNDPuW8Tgd3ciZYfFcCG80yH2Ukok08jHep00ghJAQd3l2nq7rmZ1Y-Hj61Ayy24OuEkEPJ6gO2W1IdAUp2IIqHV6u3F_2BMbbNVtlSvjwwWVno0UqLybP9yrnfKGe42qRWaPHtC-zyzCDP885NQ_Sjz_IOENhlUfFbuj5g6VJC9qbXmrxUs-M6VcDqO8ylT_NMtPp1VQQYB_YuVBMidT5vJJcSWj0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
بازی افتتاحیه فصل جدید پریمیرلیگ با دوئل تماشایی شاگردان آرتتا vs لمپارد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/28160" target="_blank">📅 01:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28159">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJPmPf3MEeXF6L6LGDTxAmsDEx9V4ttBAPAO_n0mRtf24pDhJsmOeaMeEynp4xUamC6u2EaL-lIeB1aHYY6HqR_C7l0N7YtAG8vxHxGdXqe9V0AUpcfOEuzlFuohKrohOnmEv_bq026FxYX6k6QDNQ3rSvOfEgudnVv7VWUgQ9M1bV2qUM-cXhR1RT8u1vs4Y3Sw5r3gr-DHnVMI7QW5eKXzAIOzx8SqMalSvSbFLzZAuZncpM9MsmkZKEosIvsLpASjS46us-TeKXBpYpdbTgCZYU7LywxpcNRemMeZr2YeF7zqcOHg84r6Rs7q7OPjltn2obG4DdNuB46gGJEIIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
آتش‌بازی لخ‌پوزنان در شب درخشش‌اللهیار و دومین‌بردپیاپی الهلال در آغاز لیگ‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/28159" target="_blank">📅 01:15 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28157">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moAYAITY1Jo3XDl3E-DPd4z9W4RRICIox43FinIm8OeG5imfCrQeRXT-cCzaMru6Ib8Y4P5NGGqQZYF1ST2tf9svzmRTfVtsAcplieHyLQeL1V6QNiSxUc1-TABnSCV99qP0rySTQUh1TWRhH33rv0XQjpq1VE57w27bBDLD9eEicqktrfa72RUDghvo1Gqll1C9FGyN2OIlFc8zAXPo_U_Bn-YQLsnTWh_ahnJzGMTAtIaj3rZ4w9qaX3Qa6hCGR8EwnF46U8hI_7YAGH4dGNawCmX7drKCP09aoyCHmdVv3LOL9y9f7R9-89NtTAXKH-0L_qDE1GdaK8ax7WujvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ علیرضا بیرانوند دروازه‌بان‌تراکتور رایزنی‌های‌خود را با نهادهای ذیربط برای تمدید معافیت‌تحصیلی او به مدت دو سال دیگر آغاز کرده و پالس مثبت هم نشون دادند و به احتمال زیاد بیرانوند شهریوربه‌سربازی‌نخواهدرفت. سهرابیان نیز به همین…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/28157" target="_blank">📅 00:53 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28156">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XVs7kdE6GBrxxjIThGzsXnTYBaC_oH1IAFS4qevYEKLNX3cWe4zCbBLO7KbqtCslWmyj4oQGCuHlI83nT2G6EvdcGNYszHJw1HCO_K4UOX2C9L2rVUsAgpCKMQ5hWFaohky4UGSrBX5vCS8JldUsa9FEUxbFyD1M38QFK7yO5AQ5zGY7JuuqtqyMe-2hKab2OIi1_zsPwz1cvfIr3hVS3lprmZp4wxZIHN_HTQiVnRMmadIV-mX0VKCXi5c__bNmEQP85y0WyRwseRUYr09f4EFEm1eGNzKNJSscIf8jGA7yDiEt9olTqZqmymxa6ByBFW373eWz4ycJkdipOs9HKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه الوحده امارات: محمد قربانی از تراکتور و پرسپولیس آفر رسمی‌دریافت‌کرده‌. درصورتی که بر سررقم رضایت‌نامه با یکی از این دو باشگاه به توافق برسیم محمد قربانی رو خواهیم فروخت. رقم فروش قربانی رو به دو تیم اعلام کرده‌ایم و منتطر پاسخیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/28156" target="_blank">📅 00:41 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28155">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To0FPGlQkAVc5N2r7qo1rDXvgi16lILhR6V2TTHGwzdhbVB54LJ2XTPwmiIsw1ekXck62HZP4MdVqzPLseOloq7NW3St6DKj1v2oeL6eCLgXaEU6Rh1fpQvKw1TQP2CpPgoUDMqtC08arwZozIBcK0K8JBLE6gvXqOFY-tMyyR3HsKVLqTVtZ446leDXb5Ipqc2TG0fwRNB5wE1qdKOPR7JZaNswYiHLClsrOxx9809zbWbNKjRyXXUI4HUvCGwKACed758AzJqXfszLZ0ME43IB7qXQa9dsVQlfn81JuTw6GMhoDKLXxRR2e1p7t_ufpnDmu1SmLbApUPRBiXwSNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچند شکایت به جایی نخواهد رسید.</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/28155" target="_blank">📅 00:11 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28154">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKgLVJTtxPl3cNjrkBgmieyfpNnv8-etPClsukE8F_2XHRd3JYGoToud6iFOv-fkbSttE1oQoPHKFaBhvY0qtREsITM86MQfN1ArfDE81cMejI2mBQmI4G8PH96ETURvmC2WgDcKsjFAgjF3ElRJrpi4y-JIrQ-vp3q-DWW_ayMCY2a6vKiuDzmVC1VL00LGY4CQnJK-mjvjHZhUOePuqMWGg3Bp2rtywrr1agT3FqUuS7hmR1UwWMaSIPbKpv8-0B0aIad3817_XKsaL5ZKS3NvfpoH89ZYq3CGrP5e93JZPTvgn2KtvLlaGSWNXYHZT6yJwS2JvQ_ez0g1fGgHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/28154" target="_blank">📅 00:03 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28153">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9o6zm71xMIiY768lfFl8N607x8NOaoL9mgxsSp6NFhCc0jilXAUOOSdVMc_oHixQrax0B8NCrWHzYucImfQOXrLLIFJmhxhrclrgCR8pDCyeCN40F_TRJEHSS8NyIMN87G8FgC4pyLMYYrsl0xlV5n3aYPfDilZ2LpNU1y1M5dDKWYtp3xpUW1TmVTLwK0F_XmSWnBi4Fu65F8CAI3NmGFZ2CJCJoQeuGErMXTJlg77S-bD4_n7hsVBNcKpTWm1iGm3yJgSC9j8vV_FKtSI5A95rlLjFaJdGALKbTQrHylAeYljNSLmxqJSkYfiBv-qeb3GQjhSYAcVWbLnCxRoCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلیلی‌سرپرست‌پرسپولیس: اگر استقلال تصمیم بگیرد دربی رفت 90-10 باشد چرا که نه ما موافقیم، ‌اتفاق بدی نیست که این قانون یکبار اجرا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28153" target="_blank">📅 23:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28152">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2UP_KQNijnV42noIN35F1zM3EIt7Lfa9F4fB7yctvyjOAdax4EevHpTihm17HvE-pVvwctOuWtoGoNh5CJv_ucy4kK4o2umycfBp9aNTRsWEWmOQwHdKiFHTzUHxPmIx3tzo6PK5Pf6iQ2L-XAF0mq5Ggkw6iiCAOztgL5vRNt-3jH6ATy2mT8DcLNioJSEts7QuYZH4DHtCs3UGwFBJBKB9E0D5H9TRLuQmlYwer4HKVAMPw-4Pos-HAHnJfThk0JUkiD3bMHKh5SbNnvrYib9mooMsF4cxP8l6HHRMr84kon9ve26X6iv4fASypNayEDnBYdpDvKt7pgRlU71Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
باشگاه تراکتور با ارسال نامه‌ای به فدراسیون فوتبال‌خواستاربرگزاری‌دیدار حساس این تیم در هفته سوم لیگ برتر مقابل پرسپولیس با حضور حداکثری هواداران این باشگاه در ورزشگاه یادگار تبریز شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28152" target="_blank">📅 23:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28151">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUDW2Vy5XoydIeYO03alGylVO6xpdeBWrnUAb6bMoyQC_qo3O_txFTEefLWP8lytLMB_yLGESu2daCY_WDe9PLwy4hhgkjAmVMOXch-ppKuTZAPwFmSN6PsEWB5Hde5ni0y2saDAUFdI9FXwbj79548Ik3CkU5WkiIOWu2F5h7UEPiRB_45BpWDxgLvcOApb3lfXb2RDYyslOw3xGIl7SscLIT_03_3JAfSrEUE-38WclvM2ForHWRVRqzhH25WQBc8oj0acfpHblY2mfBL1RsxceLHJDe0Fye0iq1LzeKp3k0kFr3op-Xii6Ybhrj5bLRLGmXYlIVLtzPGpdM7FSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی لیونل مسی در بازی بامداد امروز اینتر میامی مقابل فیلادلفیا؛ بازی دو بر دو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28151" target="_blank">📅 23:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28150">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-9noDl_iG4eVuP1f8Lfp7t5GKqJMx7F4eIZDnooyrDOi7mAzsHNOUPUTeizeqQefnZUjFrKpMd9EEJzWh7vgcD4j1SMzJzqw6kynCdB4_LvRiPXtYmRo2FKPUHI95suyyCfx61qnhW3AaMeFV5mYAh_ij8w-40UYtpfOM0x-n9U5JJy3f708NzoDuLbxhFbhJZtdMhL6JNKpB1MgrttucLZZWx6XE94wdZtOaT5F3NsZNXmalJTKymLquODxCXPcjPYatEqCq2Rl2lqcb-ZLIWB99DzE-onQYbKCZQBdJod1uADhoSrtwRM1h2ibQO7ou1vrMJQ25XnHeSEMDDVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#اختصاصی‌پرشیانا #فوری؛ پاسخ‌ منفی ستاره سابق‌بارسا به‌تراکتور:برگردم اولویتم استقلال‌ست.
‼️
منیر الحدادی شب گذشته از طریق مدیربر نامه‌ های ایرانی خود به باشگاه‌تراکتور اعلام کرده باتوجه به‌شرایط منطقه و مخالفت همسرش فعلا برنامه ای برای بازگشت به ایران ندارد…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28150" target="_blank">📅 23:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28148">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mibDE7aBQQHNXA1DP-1rH_mtJEmlqFs0PKnOpe-_8UC257gzbHD7WVWZHUzu0LxxvcUClntKa9uIuECpe4w99rQFXDi3okfuBgDfh9XocZlBW8xQazKLnLRCxGd0dUoPsWDzXSw_tC66BgD5PBDPiC8ttj8Q7ei1OYe4jeWjrealnf9GEAyYJ9p8jOMxllHcz8WUkYOpK4DLwe9EbdVpn56Zm1-egE37C0MvWp4j7sTUOeuWcC7yt5ZBAmDOCC-NJu3eGzwGobQkFUBV7yuvaYoa8Q00jtO9k5v0RjIFqcBk5c-a0yGjafKCHyPANxhLqwbkQzxiI2tjHZwMioy7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PLok5TCFy2Hbp9ML175O0lB7H0JzyXVPWSNbFRnRqfe6o3ZSuHba3G3717YDq9ZeLDIQA9iFdysh6sUAncVgizhe9X4S3H_VBGUeQVJmSUmHb5lXDhBUdfXIopornLkYWfqspiXAo2-Cfee9v4ssrQt4Nw4hsnQ81CBjjkpfEoTxFooWZYzQvQfd75XBaP8z-hQdF5C47Bsa3VOvp7n8XDchgu5hcb7zqie8ftb3zAsX9jcEuiESTolCUyMen0d29XEXp98TPbhsQeX220FRTELwbyqFNRwKV6AeWXh4j4szWKx1eoskIMkEXwZEzc-zoFxRqM93lr_sCaRFpKL4SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇺
مجری ویژه برنامه چمپیونزلیگ که معتقده امسال باشگاه‌رئال‌مادرید قهرمان UCL میشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/28148" target="_blank">📅 22:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28147">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJhn24pFZ5nDBkNc7vMeayMqoVN_PJp6M-pdJ_2IHL31p-lVJGDizbWayEe4pz6eUohwBB5R4uXbxAE2XjKdxB9Qa0IsLSJXhXB-Pxjj6Me1A74xss6l4rLt2KNIkSbSCtmFVvDTkVW2_sys4XoOHVCVUgbsHMsZkz-jpTPNyytxXn6r435SWBPNPj0KbjxMYQyMMQ5J7OR41JH0I_yp-6JHxgZd75bfbObjQJRhB8qKBVSyNxMut-NEFSfIRQAi-jZrfIFFiTnqKwPhAnhkYO4ZhsnXUPW1CS3wT5YInm7FtiHjCK-MvNVdoWpEk8QwP4nXxosDazSgrg3NzNK1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لوسیل امشب درهفته‌اول لیگ ستارگان قطر به مصاف الریان میره و شش تا از بازیکنان فیکس این تیم ایرانیه: آرشا شکوری، علی نعمتی، امین پیلعلی، امید ابراهیمی، حمیدرضا فیروزی و فرهاد زاوشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/28147" target="_blank">📅 22:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28146">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE3wiGV1AmZH6UgXf_lZFUZSIaOUy3roYpZUmrs1p9kakAORccUMTfEpGpTFKPnHXa7vgpqvXJBhTLRCYFNLlsQLwn_WzWdTtrhy9YL2loBDsnP_pZnX4m-fhg9J19tRFe27swTUuBIUz3XCZMiDJk7bJ7oq5Ljdm5aBvkKKo7Rnemo1iVYnkc8iwkybRXeLDuxvkn7zr6SAJQtHZ_6ZuEBCv1Wc6f962VqTOKsuk97Th2kLSyKtgd8ORNNqFS8MHhMEsmm3Qw9skGxLhw39lt4QiYps713GXWCsaQeVVVmwNe9DwTPDrHHtNyY2qANqpVkkiXGd7m1-U55HBfhLFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه الوحده بعدازچندروز امروز رسما تخفیفی 200 هزار دلاری به باشگاه‌پرسپولیس‌داده و بمدیربرنامه‌های قربانی اعلام کرده درصورتیکه باشگاه ایرانی یک میلیون دلار به ما پرداخت کنه رضایت نامه قربانی رو صادر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/28146" target="_blank">📅 21:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28145">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oa_S-tfOoMd_kaF5YXR7mtBsWlwcYmdp4KgFAKi_wMLdFRbGeR99ddU3R5w09ozYwhL66WzUbKUYszv0AFw0v_rNFSnDK-liuReFMg5ebd0rczS7zbtsYvEhCDONhcoQcHwusuJOmGbiXFRjLf-JguSnFzzJxi4qHr9Ds-hkIFwOlFA8IlIz5MwRXIy0eZYdikKH_6IXc8FrqkRB5SjO1YjOIbh6E7b83TJUOcZvLkHtmnNr-p2hy1dSIKtFKa-R2OVgmMfYowAjaDKE8_CPlxxPnBO4yGMVoOp915Z6CyHgAeY_qzdOAi6TRmvztBGX5TUpA8aRpZnUQQWW8fjHzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت‌امارات: مهدی طارمی به‌آفر 6.5 میلیون یورویی باشگاه الوصل امارات پاسخ مثبت داده و به احتمال زیاد این انتقال بزودی نهایی خواهد شد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/28145" target="_blank">📅 21:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28144">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/519060667f.mp4?token=o2gExsWxPhGu_cD0itC8WEHQWfSLxkao4iDNY_SW2EYwye66g9g76c6-HOPr08ZC0AsL-odmUECKgQz7LUnzfDbhEk3pPvYoUBWmAf9aQ9W8fJ2OJszxggXlX2peLAxLTcDRddisyiqK6M9gx-Tp8lHpZaNzXFSHCqzjl4qEVOyCC4hJgCxGUfr4dbAA19N63TMV8n-eh6T1D5G5HGD1xwI3WQxKw9mfu-qdAeMuaNMRxVB-N4g2ntD3uhknbg8j8S6INB2CjD63lkK74Hhhnrc3Wfd-PPcirQiJ3ySh3pW2yuzfbZCfyCiL6UIPfF6l88bctB4MpP8DevhslXeJcoBPhpkRs87jCkkn4xFJrk_IqlsFNDoyZnZpBT_yzH7uhgouvPsCSY4Jvbxn-V85OOReY2jutrbGVt8b-Dn1aCJtQ0ngC1-J8gttQiMMTm43b62m7zPv-mF7Xvl3wxA73cKjE36xgYPUDvC6PwNR1KHxwVbq9wkFhizjHnn_m3q6xlaUMm5OCWngoi3tWmYJx8DVO7YpBIzRkCw3PWt1F38HqxiUSgjhV6CRmunUoJHbWK4gfH_6dP6HK4bnXFj6xut1299kaV-QtANsnuSEdmQ03csHnjw01AeJ0NRXls2p497tlOJhvaSe9EZUPbmTaVgSXrmAQAM2KSMCLqbKWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/519060667f.mp4?token=o2gExsWxPhGu_cD0itC8WEHQWfSLxkao4iDNY_SW2EYwye66g9g76c6-HOPr08ZC0AsL-odmUECKgQz7LUnzfDbhEk3pPvYoUBWmAf9aQ9W8fJ2OJszxggXlX2peLAxLTcDRddisyiqK6M9gx-Tp8lHpZaNzXFSHCqzjl4qEVOyCC4hJgCxGUfr4dbAA19N63TMV8n-eh6T1D5G5HGD1xwI3WQxKw9mfu-qdAeMuaNMRxVB-N4g2ntD3uhknbg8j8S6INB2CjD63lkK74Hhhnrc3Wfd-PPcirQiJ3ySh3pW2yuzfbZCfyCiL6UIPfF6l88bctB4MpP8DevhslXeJcoBPhpkRs87jCkkn4xFJrk_IqlsFNDoyZnZpBT_yzH7uhgouvPsCSY4Jvbxn-V85OOReY2jutrbGVt8b-Dn1aCJtQ0ngC1-J8gttQiMMTm43b62m7zPv-mF7Xvl3wxA73cKjE36xgYPUDvC6PwNR1KHxwVbq9wkFhizjHnn_m3q6xlaUMm5OCWngoi3tWmYJx8DVO7YpBIzRkCw3PWt1F38HqxiUSgjhV6CRmunUoJHbWK4gfH_6dP6HK4bnXFj6xut1299kaV-QtANsnuSEdmQ03csHnjw01AeJ0NRXls2p497tlOJhvaSe9EZUPbmTaVgSXrmAQAM2KSMCLqbKWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گلزنی‌دوباره اللهیار صیادمنش برای لخ پوزنان این بار در بازی امشب این تیم مقابل تیم کلاکسویک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28144" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28143">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWAuq_tua2Xi2oQtMSS1E_ODE9n_CvHDxBDe-iX6vfVTMNUP17CUJ9zsTaKMNX17e9udcs8UWKzkSpk90PpdPeGG03_hzj8Zujz79zHaZ7Og4QGdS_2tOMCjArphEac6WsClNDLHYwdXhpIPpK_rSAqVmCjsqGQIsz08rZJw62QMnkZ8yl18tO7__4T3N7Y4pDdy_W2HYyx0M_HqiaKzGdIRpp7cc1kTUtssiK5Su4mQS_neFYElR4M4T-TESpx1rHEgimjqhY-371qoAaoMVTguwI5f3Zn2b9sX4RDHG0Id38N2A6XX94fahk1vEW0KlDQ9t6CbHV7c3otHVNcnDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ سایت اسپورت ۲۴ یونان: الوصل امارات پیشنهادمالی‌سنگین‌تری‌نسبت به شباب الاهلی به مهدی طارمی داده و در تلاشه که این بازیکن رو از باشگاه شباب الاهلی هایجک کنه. تیم الوصل یکی از حریفان اصلی استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28143" target="_blank">📅 20:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28142">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11d47c7d57.mp4?token=pB8T1sJ4RQGv6Yz1OUQlmwgvJ6dKbxFUp4QWMdZw148rNvwKfTnXdTL6abQfCVfofiSXr-9ZZPpQVbhb2FNyOloiSV4BH1Az13cPg0rkyUqSlhOdJSTSQ83Cqttvhx1Y_aZMHmf1wNIqX6NudpvYRV5y85d7di0EGtoFu2MOrLw6_N-W9LOWRMER6mBDid2dbUNekytvoxSLVCxzpkOZJzFFoyK9BjQqqfgpc4v1H9vU1x6g4ry6lpY80F4l4AptVA6c1jqaPleM23mBV9Uq8iDBrkUUU4fJCaC7ZUOTuEFh22ngLg22Fdsmpf9vIUeejngq-16GmfKNTkijUh08xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11d47c7d57.mp4?token=pB8T1sJ4RQGv6Yz1OUQlmwgvJ6dKbxFUp4QWMdZw148rNvwKfTnXdTL6abQfCVfofiSXr-9ZZPpQVbhb2FNyOloiSV4BH1Az13cPg0rkyUqSlhOdJSTSQ83Cqttvhx1Y_aZMHmf1wNIqX6NudpvYRV5y85d7di0EGtoFu2MOrLw6_N-W9LOWRMER6mBDid2dbUNekytvoxSLVCxzpkOZJzFFoyK9BjQqqfgpc4v1H9vU1x6g4ry6lpY80F4l4AptVA6c1jqaPleM23mBV9Uq8iDBrkUUU4fJCaC7ZUOTuEFh22ngLg22Fdsmpf9vIUeejngq-16GmfKNTkijUh08xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیویی‌از عملکرد خیره کننده تئو والکات ستاره سابق آرسنال دراین تیم؛ به هیچ عنوان از دست ندید ببینید و لذت ببرید از سوپرگل‌هایی که زده‌. اگه الان میبود قطعا ارزشش بالای 250 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28142" target="_blank">📅 20:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28141">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19a281101a.mp4?token=YQOK23G2B_Ye3faX9oBSwiHmR6BCfpEv_24qgMsB40MdOC0hOqJw1v2SDidOyNNVYSep2ATaiPuhS7DQHrU8S3X9CD8IlXaik5rTyiZaETFVGsiSx6yg0GGCeucUAwOHHdQkiJntNcvM1w3zTyLH_D-nApsRkJUQaqMQFzkhDGKl5CxriOBmXwphGNi1ZjR2Zz5bxFENUJ_9KWnrl6trU6vIYpTDAet-n3AxDDlTEf78YSTYhKn3Le4zEYZW4_LaVe5nJ1hQkUm_QmJg0tuZuZge_JDaj9_cEuMF_ofB4zq7G7FOECM8-KDeAICm8WeFtNw-RGpW7yxLPuoVbkGPmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19a281101a.mp4?token=YQOK23G2B_Ye3faX9oBSwiHmR6BCfpEv_24qgMsB40MdOC0hOqJw1v2SDidOyNNVYSep2ATaiPuhS7DQHrU8S3X9CD8IlXaik5rTyiZaETFVGsiSx6yg0GGCeucUAwOHHdQkiJntNcvM1w3zTyLH_D-nApsRkJUQaqMQFzkhDGKl5CxriOBmXwphGNi1ZjR2Zz5bxFENUJ_9KWnrl6trU6vIYpTDAet-n3AxDDlTEf78YSTYhKn3Le4zEYZW4_LaVe5nJ1hQkUm_QmJg0tuZuZge_JDaj9_cEuMF_ofB4zq7G7FOECM8-KDeAICm8WeFtNw-RGpW7yxLPuoVbkGPmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فوری؛ کریستیانو رونالدو اسطوره تاریخ فوتبال: احتمالا این‌آخرین‌سال‌حضورم درفوتبال باشه و میخوام یه‌میراث فوق‌العاده از خودم به جا بذارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28141" target="_blank">📅 20:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28139">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4de76fc0f.mp4?token=Nw4GxpsGoEAVBdJfGEHr2oJYY154d6xJmct-yCdWPXOt5IH5QfvYK_tIV4p-v_j6XAmhzklqrpTxa_E-8xjqBeoGiO-toR3NvSQwwF3rA7ROsJify1V8XkRFucLA20oCq7DrMFHUYfEoZAqowhS-8tyfV4D_Hp3XoRdl-5syZXn-7RjeKZ3proHBNhtwpV13oWZkiqkuwlBwG9BSRBpHiGvGsX85lvMbIu3PwbvHNMDE6qopHGO2y7kkHLCUAp6hINVifUPbFCpoSixVO6Zuo8HDr9zb5IOkWmia5KIhXbXpqagDGWZCaD0PiopwiD_WmjPiy0ppUek9kgpzQAAX_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4de76fc0f.mp4?token=Nw4GxpsGoEAVBdJfGEHr2oJYY154d6xJmct-yCdWPXOt5IH5QfvYK_tIV4p-v_j6XAmhzklqrpTxa_E-8xjqBeoGiO-toR3NvSQwwF3rA7ROsJify1V8XkRFucLA20oCq7DrMFHUYfEoZAqowhS-8tyfV4D_Hp3XoRdl-5syZXn-7RjeKZ3proHBNhtwpV13oWZkiqkuwlBwG9BSRBpHiGvGsX85lvMbIu3PwbvHNMDE6qopHGO2y7kkHLCUAp6hINVifUPbFCpoSixVO6Zuo8HDr9zb5IOkWmia5KIhXbXpqagDGWZCaD0PiopwiD_WmjPiy0ppUek9kgpzQAAX_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول پرسپولیس به اس. خوزستان توسط محمد خدابنده لو در دقیقه 6 روی پاس علی علیپور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28139" target="_blank">📅 19:59 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28138">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28138" target="_blank">📅 19:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28137">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAZTlv3t4zVKkbeYI28OjJpVSYTvhHXCRT5IqlZvfEgeIzU6UgRevtTYvuAev0y5E6oJtiQEgQgFeNtGY44dngwRGP9N1BzWIkujH1CoVHDThSr_s3E0zAYrv0s-ecoDvhKCrpopaW5n3g86lY14cx6Dth_PXWX4X3kkJVdz86V-qr21rbGf6ROhz-sh125ieG54n2eYyhzrd3uG9GxY59jIWsJnOsR03T4foiKXQJ0zr5Q9YNr4Cw8VtV6-P2eKpfAAoHgOhcBMOKz8bSXB1_rw5qUfLqPuFxw-bo-FDhRlP3ezg6nVOO2q9e5Rv8GS0mQ7FsItT_bG07mT-2oukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستر باشگاه آلباسته برای منیر الحدادی ستاره مراکشی جدیداین‌تیم؛ کل دستمزدش برای  دو فصل حضور در این تیم 900 هزار دلار امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28137" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28136">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpEeAPxt9cm8KqHns8wAB5AeLyG88eyCtIAoxU9Ym904NfeJhPJ2s991OP4rtF1RIc7KZlVTCzY5hnVfRiraMpl2JejydSweovNsU0ai4k1GwXN-9HSqC0eOUrtHmskPlJAkYDtuxoeO-wpvWiqzUOKObN1TiRiKrBJpEwXPI32e0iE-dKQs2FpqA26Lx19-RIOvl-d_bLlkzj8YoK68qLOlp1khFs5ZyxDFJHDahEjj3SPOYru_GmnXmt6U8lQLcTJB1aHaqwC0eCYBeOl7o5PuutIV1fSnTIeW_FepyxMqGxjdpS2EG6S1Zo52rLmaVAa2TnORE6ASTzY_VbU8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ علی نعمتی مدافع‌میانی‌سابق تیم‌های پرسپولیس و فولاد خوزستان با عقد قرار دادی دو ساله به تیم لوسیل، قهرمان لیگ یک قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28136" target="_blank">📅 19:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28135">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asL-0cE0D1JUPy5XOnFKip1ToNbi6NZQEL9aXn2UxvfRvfQr0D6nA-_1zOWOgXLnSJG2pq2yCo6iMVL8td0lXCqat10_6PqLNhfO7ed5MbkLqrWhelh5Gz2C-PzdkAOscf9VM9ufoIAXBeQHt24e1P-w6gbXUybh20lpwkT0euXLJTU5jLQvQ9QbVnp8HAaCgiMqPM1cN0OOXCIQYdutTHgICxK6y63QxDcsT7AuO3N8SWnBRyhqpN6g6ccdSses-NLshVcTOM5XsKe0gIXF3pgq0SYIh3sM05y1LyXrQs8rcV_iRFTidna850ut_ANlQuOGVU0KLI8KIS3BbC_Szw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رونالدینیو شاعر فوتبال‌جهان میخواد در سن ۴۶ به‌مستطیل‌سبزبرگرده و برای تیم راوانا در لیگ سوم فوتبال‌ایتالیا که بخشی‌از سهام این باشگاه روخریده بازی کنه. رونالدینیو اعتقاد داره میتونه کمک کنه که این تیم در سال‌های آینده بسری‌آ ایتالیا صعود کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28135" target="_blank">📅 18:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28134">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXed62t7at9qlmK_ZrVuSNbrRZcTYoChr9rCZzqoJIwlv5WDPVn9Bg4MoE-VJczMjd6PkVPv7RQOYjC92h9U6rx7AAGTKSpNcztlYo_v_Md8_bQzp8OH1opEJrfZDzCASdQcwipK3HHSyv6avDhJY6PiLrmheb9Vup6QJQv_nmB_S2bKvZ0oZ3ZP3r7zxFbSsb8cU7Sl7RYrN9nGWLw4uzWDgrgXZ6bHK0epsi636_JidubbjRDOp7xHk2QBFktO2xI3480TrXZn3nn63uJ96s_iXPTRjL-tvTgOg-Qv0STJ-5kboSMf0p7JyN3faMobExhjfXOSpV1ZRFMtaCxk_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ سایت اسپورت ۲۴ یونان: الوصل امارات پیشنهادمالی‌سنگین‌تری‌نسبت به شباب الاهلی به مهدی طارمی داده و در تلاشه که این بازیکن رو از باشگاه شباب الاهلی هایجک کنه. تیم الوصل یکی از حریفان اصلی استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28134" target="_blank">📅 18:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28133">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad771d7af7.mp4?token=KezeVLfBog1O10m-aFsw7bQGiEgjHEf9Tmj8ts3Vc3voXGuKOW_L0DPjKI1J8-4pOR-FpYBTvWFHXb_hTC2XmGjzcFBQgZXZOUMQbuR65iBjfDbSzw_gEZV_cWzGhjmG2T3_44gOlknagtyX2ylkDx-jcjDjW9UNUSb_u3CThiDhgz08oJtQ2ITa4iTqjE6c0LaXYbbeCQHwU79IlPDSjVZ-7LZV_JrS-aLawgDi7BIFjfvnlDJPf4OhuZQVxeD_ai9wmSZaDKpz1ewiYV8ypa9rB1nc76Ra5iJKbW3y5kfiP3eEnPfoJCTSA11EmVyUNL8LxpL8Xef4eOQhCeBbMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad771d7af7.mp4?token=KezeVLfBog1O10m-aFsw7bQGiEgjHEf9Tmj8ts3Vc3voXGuKOW_L0DPjKI1J8-4pOR-FpYBTvWFHXb_hTC2XmGjzcFBQgZXZOUMQbuR65iBjfDbSzw_gEZV_cWzGhjmG2T3_44gOlknagtyX2ylkDx-jcjDjW9UNUSb_u3CThiDhgz08oJtQ2ITa4iTqjE6c0LaXYbbeCQHwU79IlPDSjVZ-7LZV_JrS-aLawgDi7BIFjfvnlDJPf4OhuZQVxeD_ai9wmSZaDKpz1ewiYV8ypa9rB1nc76Ra5iJKbW3y5kfiP3eEnPfoJCTSA11EmVyUNL8LxpL8Xef4eOQhCeBbMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
🇮🇷
تیپ‌واستایل روزگذشته رامین رضاییان روی نیمکت تیم فولاد 11.5 میلیارد تومان ارزشش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/28133" target="_blank">📅 18:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28132">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNEp1SiG_K3g4tRADzbIpJlbyk89UzuAWVMp60prwYXer-eHbA8A5--lpp4l3WmOTxSMqr-evdc5sf5-uNwKImcnwSWzViOK-ep7xLiNgIYqHD7Uq1uSDC9zj7nTZ-mxqsGIRv-q-xsvrqI3HHhs0TG0T7cTPGoYsSyI24h9pN64YDEb1N4i9kRwyo5qDFYXpjEqXTlFr-gjz48SDwC1usaE3TJtZRcCMQypS9sfPG86BwwUjKxviqHjIqMUvBcKhOIRelhUjzP6Eww8hyNKwCvPCMVURmCjYki8xxQBb4jVRqYxp182V-Ty8unh6CzxluTrPwll_3bJa0XX7N9y8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ سایت اسپورت ۲۴ یونان: الوصل امارات پیشنهادمالی‌سنگین‌تری‌نسبت به شباب الاهلی به مهدی طارمی داده و در تلاشه که این بازیکن رو از باشگاه شباب الاهلی هایجک کنه. تیم الوصل یکی از حریفان اصلی استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28132" target="_blank">📅 17:54 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
