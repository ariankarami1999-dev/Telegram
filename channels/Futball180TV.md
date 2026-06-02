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
<img src="https://cdn4.telesco.pe/file/tlyKg76lpw8Dwz9VZcua3ejW6ZAgoBIZWmcmyMxPLgvRAiKIIB3RPFsXSUyJD3943lL8JfUwepa3p0I7HGKOFvuypCu04HQOMbuVfcqggEU2Pa-AxbengxfO3tp9bNWF2bqVvQPgs21hldZ0NB2MOfk6-yuQT-CgTyjJK3qbkShnUGzBywrVN8N-yehekMNu3bmzaF50XesgEJDJiIfl-4kgoGpkIWzLpdXQIcME7BkRLHYNlFGJNCxI3RoZ4KNQJZj8a2Fn93LGJkFPpIoL6YnTRYn38ZsNaj7euayJSAVW6Hh4nyB7IVK9Esq1RWJyzZKASIUnFjFQLHUiXLv8jQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 157K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 03:37:39</div>
<hr>

<div class="tg-post" id="msg-90659">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfff56a47b.mp4?token=VYff1E4bBh095A0x3V4K1wRcuLoTvBMHlQw_rGNG4PLWlNjFUuhhPOpGXsmKkM99HP2TTViszNZQ-DT9xoImCS3Pi0dAJWpZJexymBko34RlIbHKsITcWVy7JF_o_xLW61e4IUpw9_XzBx8gOsvXKsvpq5EYyjS-Jr2NMoENqovs19_lxtahzsNVRWvVfdp37h-_htdy5CemLsDO-0S9x6_gTR9niyNkl6Ing35MINpkWuPeiVqjlL3AvBeJZ_-525n50Qa3jcIIQKvxml1YJihogFHV4AI0a8og1BM3zDo9pUD8HV4AUmMrQTsLLk67FkSrY7-FC5SufalOMurmbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfff56a47b.mp4?token=VYff1E4bBh095A0x3V4K1wRcuLoTvBMHlQw_rGNG4PLWlNjFUuhhPOpGXsmKkM99HP2TTViszNZQ-DT9xoImCS3Pi0dAJWpZJexymBko34RlIbHKsITcWVy7JF_o_xLW61e4IUpw9_XzBx8gOsvXKsvpq5EYyjS-Jr2NMoENqovs19_lxtahzsNVRWvVfdp37h-_htdy5CemLsDO-0S9x6_gTR9niyNkl6Ing35MINpkWuPeiVqjlL3AvBeJZ_-525n50Qa3jcIIQKvxml1YJihogFHV4AI0a8og1BM3zDo9pUD8HV4AUmMrQTsLLk67FkSrY7-FC5SufalOMurmbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
حمله شدید‌اللحن مجری بی‌ادب صداوسیما به مجریان معروفی که قرار است ویژه برنامه جام‌جهانی را اجرا کنند!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/Futball180TV/90659" target="_blank">📅 02:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsgcYzipWjwxdNfjK5_0Y9bYuWQse2VOZIlokDm_tiwTsUv-tqJ5HKwveJtFNrNCxYxjoRu0dy0vAS-pgXg2KJONxC79ZBVYU_BKNl3oK210sXZsGvFvApN87csQHU2Vtre_nLTNmwozI1sgP92Vf2Xshko-Q-EKPp4kIY4hcWXSzM3-5Y0IoRshhS3dkLFr8-ZQBA3caBz_Um8z2u8ktT_5ViCm_xavT3zjsqvtO2kVrsZ8uhV9Jqo67N2RmqdS3dU2iRmkXx1j20X0ckyC5aeyRZep4ZNTzK0AtmozRkiVUbmvb8nnXeZruZaHQJUR5n4AOJ69woHv7scUBMeZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
یک‌رسانه ورزشی برزیلی اومده جام‌جهانی رو پیش بینی کرده که در نهایت نتیجش این شده که در تصویر می‌بینید. موافقید
👍
یا نه
👎
؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/Futball180TV/90658" target="_blank">📅 02:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njCRvZ5AF5hhHDHkV1EnCjxZ0UV_ZqWEw1v0DpEJFf_YXZCHaHob0bu-qgeelcfZHwCmSH5EP81_kLPT8DKw7d8ZqDKOBNoNxxv9kD6ySCgm4T3qK3SnKGTVwRITxPPjnAYfj1KmjhmKgsDsdp9l8RlC3mVZFq16gT57-LoTS-nGJgAWk72YUL8Ac7gMlzFxmgzCXeI3PhNSuYZL2ptBTF6UAcUsDaLJz2BxO69rFJZbU3rG2FVOHaTgxj7scSrvTQmR1AqlGPVCrcmwx2FIT4JDwpGdoiaCp9-XcQuyd-FG-RUWBzV4r2CqcK-el9_yRqjtIJc2gGfaYg8gcVCmjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚫️
#نقل‌وانتقالات
؛
یوونتوس به دستور اسپالتی خواستار جذب براهیم‌دیاز از رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/90657" target="_blank">📅 02:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/Futball180TV/90656" target="_blank">📅 00:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90655">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=eFwZ11JW3hUOtHa7ZjBtDeXkXkf7RikgRmMIf6omD1P862MGRS4XVwQzFy9ip7amkDn6ADv9uCv8aHmpXQIVLc8SS6kPmrmjgi1qeZ90dssFFUyhaVNfoHhHNMZ_g9QKwOlubmocvvz6kxsvejgyEFaA2E_CZ3kpDTYU_Acz2zuhtBYzbcoxGRtpgJ3bxWWXRd6jL0MIN2Wdq3QznQvdTPWNCuL5E80E08o53AOYQt-2lS_FCsRAhshv6tWhy9sHzdAC56M6Fj1ANJdkD9lodtTS2XqSzCi50OIxVBU9zH66_sikuMwxu4KGAbEAaFuDdLSXYZ3N04sl0QMnd-ymxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e488d912f.mp4?token=eFwZ11JW3hUOtHa7ZjBtDeXkXkf7RikgRmMIf6omD1P862MGRS4XVwQzFy9ip7amkDn6ADv9uCv8aHmpXQIVLc8SS6kPmrmjgi1qeZ90dssFFUyhaVNfoHhHNMZ_g9QKwOlubmocvvz6kxsvejgyEFaA2E_CZ3kpDTYU_Acz2zuhtBYzbcoxGRtpgJ3bxWWXRd6jL0MIN2Wdq3QznQvdTPWNCuL5E80E08o53AOYQt-2lS_FCsRAhshv6tWhy9sHzdAC56M6Fj1ANJdkD9lodtTS2XqSzCi50OIxVBU9zH66_sikuMwxu4KGAbEAaFuDdLSXYZ3N04sl0QMnd-ymxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
🎯
همین حالا عضو شو و شروع کن
👇
e11
https://t.me/+6ckCmywafrxiYzk0
https://t.me/+6ckCmywafrxiYzk0</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/90655" target="_blank">📅 00:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90654">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQoRQ2gym5OuEpEc67CLiS2y9u_kZxgB11rf9xg06HDdYhUMdXrIiApuMdyy47ZlT7ZWJx5DJOj6tslHJ-gatuhL2FUyhK0-E4UQ6yT_oCiKS1SIb0afHA4m7Tpfk4-wJcVWdXN2_QIq9epm6iQPmXOWmMvBZFUOiuJ7raMkIpzBzGqCt42WCxHRqBWwy5Y4vJsUcjSVP1V8xS-BnODvoX4K-ci8-w7gFW31WIJyElnVN8Kx6_-iCViHkx-2kI2z5gia4O6FbVLBx2J6yE2IQm-yUiPXGz9aRki1z-2UVXTM7-adZHSZsQpxpI8uE03SQszQ3BVP4VlnBtMxl3NoOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری ال ناسیونال بدون اینکه خندش بگیره گفته رئال پیشنهاد معاوضه والورده با فرناندز رو داده و چلسی حتی ۲۰ میل هم حاضره بیشتر بده
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/Futball180TV/90654" target="_blank">📅 23:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90653">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">❌
ملی پوشان فوتبال بابت برد مقابل گامبیا پاداش دریافت کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/Futball180TV/90653" target="_blank">📅 23:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90652">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">کونسیسائو رسما از الاتحاد جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90652" target="_blank">📅 23:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khd7lorgeAkcm5iKKaYpnNUZ1xAHqxyFhuwEeEsITubBXi0dl4snu0qOkXps9wWVBB9EO-q3lFSxq1A1-a8KJZ6i-9L4kJec2gXIa4KNGnhFGve5uz4HMTdWwDJw08zs09P5fV5fhbF71UfjoUeyZY-yP0J0RBqrXRIbkKtpvSm12ytzh5MOZ_Y4pJTBwqwo4Cf3mLd4JUaLqEwKyEtaoouqGddiUHFjcdZcURYctVkml-I4kna51jmz9wH6sFcGNOurQstKwAqHVAzSixho2u69_fv6MeYOXNkbDuv2JfTL-mId_w2RcVCnMZ9atiFvlUfidV8D50IHv-1ccuWFRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوبوسلای به این شکل رفت اردوی تیم ملی مجارستان
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90651" target="_blank">📅 22:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u69kd9MgLXhk5JdmNuz1SUOmbb6jBIqPDIWLjh75jk_LBWWeWs6I3OxgEQT_N6Zyn1SEoSsJk_2dJQQTVTGJI3HxzYi7vQhBCJ9rs0RiEb5V8RkzivKTuDeFDGIoFSanrFQULavuh7XUCYMCVGPWbHaFifxytwODFBvcUrBes1hrEeHTvw8CeJZ25D6v9-L6hLhZFMdts087UiIzdsNSdjuTPLrifCq3pMqwKk0Hb6dzM1J_qZf9r2GXd_EACGaUsGCi_sZbcYI3weMTT4q3YkvO6MwQyu57X61ChimgZRjqSEvXKalsgxZyOiW3tv8KegdIrkoBtWO4K72nEShlrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره پیراهن بازیکنای اسپانیا تو جام جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90650" target="_blank">📅 22:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJkxqjJ3tKiv71csyWdYEWZNIxa0s0XajEdy9qCScD8c7YEIuOS5KgS901M37m7eYgx0IbdP5ZWokpGn90qsZqPhuKKfP0LDHz5aDrfBcS4iAEWaVkBEI73mB19_MzANb95DZ0VC-SJTcwtpUlmYkEc4mjGYVnqbpX9GYZmPcg8DvsYZm8nB46bEB8uiJ5hfBqv74pWLKzXvX0ScBhRWzHUvEaEJrZf2xx6_Uk-NT4u2GnqqwgCyrMzgGIDn3QFRIXggYTj6gSYIeR8goaMLesrFjyNF2w9sEdQ587xsVyBXTyxusw1Oe2GsCLyaCx8cJvLSTWjQs8bT5e7uUoY8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس ورزشی ویژه اتصال به اینترنت
🔥
⏩
به بهانه بازگشت اینترنت ایران به دنیای آنلاین جهانی، روزانه با حداقل دو میلیون ریال شارژ حساب کاربری و ثبت پیش‌بینی میکس معادل شاٰرژ ‌حساب بر روی رویدادهای ورزشی مورد علاقه خود، بدون توجه به برد یا باخت، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/BACK100
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90649" target="_blank">📅 22:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90648">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHAKF13nXgQ4z3--oNDEUipzUVuj2GeQXSkKm7lYvjlIIFd1QMasB4zONjVqYporB6iflz-PpW0qftA5HtTc6Kglb29LFwRQTxtUWbauIxRAUaeLY5FLtv2ePqWPRIkz2lEKwm4A4hSR_tZPEYOIG-OjCov8j5LperXzGD7kczy7G9_z23Nu-7o-lQnu4IIs0lZLpDXWs5jYvIPX-cNtuZe8goQAezBrXjSw1j0ii2RLDOXH29_Hzx6lfQi31RUD4t_P8OugTiV2M9CPSd9kiXDb82J91uqJHxr2WiRRBnszVDnMdDJbLPXasyfW2foMsMybxq3nQarkf6axxABb5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو به تمرینات تیم ملی پرتغال اضافه شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90648" target="_blank">📅 22:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90647">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0cb16154.mp4?token=k0t5AOnWLy-iT4WHuan0yatyr5jpbMq7V5TLjCDwt_-HnDZO9XGqj36Le1s8vCYNyuSbTgEtuGpFOcmtx8wv8jRHqA0WLATRJAbv4OiNkBaE1kHPYmTG4CKjwB-dYRJi9p7fnFtAxMjzO7LV8K7RHqamRYL1QoAHB15POIchSaCz1pSPPKIH40JG5ueRIZqcQYCLSl7hhyerx5cryT7tmtxtifjM8X5CGlkLFk5fPCjrVzsA_YNTmJbVpy8UDWIVMsZ-RRiDnlyogkdZ-9hObFmr6_5wmfQm9r1J88Wrgy-xff2Nq5otIv9bvTEnJ0lndAtqK9mI3xYJF3jibc31L5ulAS5KswrqSl01B_kXQni4FpkzyAKgirpsMxS-R-gOazfQHPXc_ULxIgzxpVfO8MqKe8DpC5dBZ3T_f-Cao-jmhp9TTWhFUCPHejL6Jbu8uHdlxtTW4JJCPwZQ9B8Fo66wtlFPNwbCm3pWvxyfvteaaBSQonerlgRMR2_bDCklHwSubUDcVbQ0tx7npF4Da91juwtMX7Cm_wLXaeIhF73eU2kzXeFtfn6qMmSTMtNoMTmh2CKaLR29vKcA1yFeo_4-AX-TYox2sA9Zux3UwJG1mz-qHF-_95LD-cKk0FTuOFvkM2_1jjeK3fdq5z-9GuBxLABVyGc_qrKaG4eeai8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0cb16154.mp4?token=k0t5AOnWLy-iT4WHuan0yatyr5jpbMq7V5TLjCDwt_-HnDZO9XGqj36Le1s8vCYNyuSbTgEtuGpFOcmtx8wv8jRHqA0WLATRJAbv4OiNkBaE1kHPYmTG4CKjwB-dYRJi9p7fnFtAxMjzO7LV8K7RHqamRYL1QoAHB15POIchSaCz1pSPPKIH40JG5ueRIZqcQYCLSl7hhyerx5cryT7tmtxtifjM8X5CGlkLFk5fPCjrVzsA_YNTmJbVpy8UDWIVMsZ-RRiDnlyogkdZ-9hObFmr6_5wmfQm9r1J88Wrgy-xff2Nq5otIv9bvTEnJ0lndAtqK9mI3xYJF3jibc31L5ulAS5KswrqSl01B_kXQni4FpkzyAKgirpsMxS-R-gOazfQHPXc_ULxIgzxpVfO8MqKe8DpC5dBZ3T_f-Cao-jmhp9TTWhFUCPHejL6Jbu8uHdlxtTW4JJCPwZQ9B8Fo66wtlFPNwbCm3pWvxyfvteaaBSQonerlgRMR2_bDCklHwSubUDcVbQ0tx7npF4Da91juwtMX7Cm_wLXaeIhF73eU2kzXeFtfn6qMmSTMtNoMTmh2CKaLR29vKcA1yFeo_4-AX-TYox2sA9Zux3UwJG1mz-qHF-_95LD-cKk0FTuOFvkM2_1jjeK3fdq5z-9GuBxLABVyGc_qrKaG4eeai8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">2 سال پیش تو چنین روزی رئال مادرید با شکست دورتموند در فینال لیگ قهرمانان اروپا برای پانزدهمین‌بار قهرمان شد
تونی کروس هم تو این بازی از دنیای فوتبال خداحافظی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/Futball180TV/90647" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oF4pGB90MuccL4T0gp1voqNYjNTkW0ISQSmCiIavzNf4LA0qFkKgHV_Mwb35BbVOglO-AjrrgPZIiW2vfwGj_HJOfwRuJ12fJWvNlm1AtlMnk1ljZ5JLGsCmm4b93uWqs5r14nxVu9ScPKU-HUP2j7ugmjWnaz76kFAFyWfmg6H614IY8bUWiNEkBOS_q4B574tVaMGaYk-kjlMRrL_QRiwJrn6KxiBBgwRiDhtgVby7b-rB4Xw-meOtO6EIO88bk0CPBYcERN--lcDF_2hkjCjoQbIKGWQzJnTHrRee8ehM1_TcrxnAnINhzyukdnx2XE8QM8h7TOrUU_ip667F5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
فهرست تیم ملی کرواسی برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/Futball180TV/90646" target="_blank">📅 21:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90645">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3288c4bc89.mp4?token=ege79axSErF9DRPPiyAQI9OzxrpTI830YNVVdqfyMXqU9QUF8oBdTTUUU5fWYioALWoBVU-x9KB08XzXnulC5p4jsi38aQDJn1Qjxd22rCzpf8pM3er9pyCvh820Il539TnfPvStyhLZojEj-MOZsdrh7j7u8PHTHGEjcyuwDIBrJBsigB3ZZlHQXM_Zjb6WihXR6m6zWbGB-gIXBYUeeSZqF9MNGgpP1R99fm3BQB3i1wX7FOYaTe_902v8UKke6j0-lgWjcRTpigKnz63TVa7iK-RdYB7PD18T4DhLxnqeaUgCiLZ9aa6SOHpiq7DWq9heKIbk25XCGkWtXaKcUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3288c4bc89.mp4?token=ege79axSErF9DRPPiyAQI9OzxrpTI830YNVVdqfyMXqU9QUF8oBdTTUUU5fWYioALWoBVU-x9KB08XzXnulC5p4jsi38aQDJn1Qjxd22rCzpf8pM3er9pyCvh820Il539TnfPvStyhLZojEj-MOZsdrh7j7u8PHTHGEjcyuwDIBrJBsigB3ZZlHQXM_Zjb6WihXR6m6zWbGB-gIXBYUeeSZqF9MNGgpP1R99fm3BQB3i1wX7FOYaTe_902v8UKke6j0-lgWjcRTpigKnz63TVa7iK-RdYB7PD18T4DhLxnqeaUgCiLZ9aa6SOHpiq7DWq9heKIbk25XCGkWtXaKcUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
چیزی که رفیقامون از باشگاه رفتن یاد گرفتن:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90645" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90644">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/90644" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90643">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCAvF2WvEuYzM49TeRAApo62B5tb4I6BklASG5viJs4zd3GeMqcALHg8xvpcamfLuLfJ3S7wqA5BkbchTx1UxC4E3vD4vo1deTQWYIE6yb8lE0qKzfaqUPIsRJJLPXzeVK0_kibo0TW_rIAR2QvaWmlWGTYMCU1S1n3T-H4k4kMYRlXlEp2me8ZY20sb1TyM0mBpH__Oonl4c92TR7pYquBTDP0If98_6n5CtzgoWolmf5VzMWLe39FRQp_WPdkZFeYi2VQngeO_2NnGm4F4vGCRV0T7dY8A-PUmj4Ug-OGXF-B5FQmpZdfY3U2aAsIU4Xy8PuPlkU2YFggRgeAung.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اگر میخوای قبل جام جهانی با بازی های دوستانه مثل رضا کینگ کونگ پول دربیاری همین الان وارد کانال شو
👇
👇
https://t.me/+YF28GUBRSZkwYTlk
https://t.me/+YF28GUBRSZkwYTlk
‼️
با درآمد دلاری پیشبینی های این کانال شرایط بهتر میشه  g11
🔥</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/90643" target="_blank">📅 20:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90642">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2260d09ec3.mp4?token=Gq_0Vr4p8SLsvB_rKgo3Zbu7Dqq092d_WozSpLJcHB8K2zftkg-6ObRoupNFJkCFyOtLXNk1XpziJJJIuZZZa8CDmAL_X3mkrjSUU1kQR8mxHLoP8pRkUA2qRDlUhXmhYcapOUGUi_E1xA5g75nn48KONwZbZajUPKmz4QlBvDPCza1LchNqJQyPksXIaNLs9vfaFAEWy5L1UemMEz2FdACONyA53yBo_3YMB0PcvDEdaFNDzy-m1E1HizAgQtukW7MOYc63Gv6Gp55ho4hLYhvyQFgMF_cIgEshIBpfHhg5FCrw8XsMM1HRF1JHKu-pRe6InuxxFU-f3UUqMz-PJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2260d09ec3.mp4?token=Gq_0Vr4p8SLsvB_rKgo3Zbu7Dqq092d_WozSpLJcHB8K2zftkg-6ObRoupNFJkCFyOtLXNk1XpziJJJIuZZZa8CDmAL_X3mkrjSUU1kQR8mxHLoP8pRkUA2qRDlUhXmhYcapOUGUi_E1xA5g75nn48KONwZbZajUPKmz4QlBvDPCza1LchNqJQyPksXIaNLs9vfaFAEWy5L1UemMEz2FdACONyA53yBo_3YMB0PcvDEdaFNDzy-m1E1HizAgQtukW7MOYc63Gv6Gp55ho4hLYhvyQFgMF_cIgEshIBpfHhg5FCrw8XsMM1HRF1JHKu-pRe6InuxxFU-f3UUqMz-PJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
‼️
دیشب نیمار حین واکنش به تشویق هواداران کونش پیدا شد که آلیسون زحمت کشیده شورت نیمار رو کشید بالا
😂
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90642" target="_blank">📅 20:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90641">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f80cea5c99.mp4?token=JQcta9gjg98ajbNf9o2qHE11Jp1fBybPt607J1bVFYASOHoF7XDaR4JFtNv--x05SjHaa5qorgCSlcVGNMFCJ7KQUnkIBX5MGJ-9GERu8HNOywb5I3j1VuR0F5GVV3ph20bw4_vE-zqgwr2C-xSfHN18gJzJ1XfTWUl4Uy7xQav9Qath4BNquzu2_jMrGEXR2aNTBCWZpIBUA-XvEa35dQy-SHczupl2Eq8sWTs4AdS-3Yf9OyZRsKL3QJhAsX3ZERRd_p9HuFe4yzK7e2EI5WYgz_QVDFbclFrpntlSJ2Ev_lHBS-3qqJzl2XL2UtVQzOFhmTe-azmegvpGCiKqmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f80cea5c99.mp4?token=JQcta9gjg98ajbNf9o2qHE11Jp1fBybPt607J1bVFYASOHoF7XDaR4JFtNv--x05SjHaa5qorgCSlcVGNMFCJ7KQUnkIBX5MGJ-9GERu8HNOywb5I3j1VuR0F5GVV3ph20bw4_vE-zqgwr2C-xSfHN18gJzJ1XfTWUl4Uy7xQav9Qath4BNquzu2_jMrGEXR2aNTBCWZpIBUA-XvEa35dQy-SHczupl2Eq8sWTs4AdS-3Yf9OyZRsKL3QJhAsX3ZERRd_p9HuFe4yzK7e2EI5WYgz_QVDFbclFrpntlSJ2Ev_lHBS-3qqJzl2XL2UtVQzOFhmTe-azmegvpGCiKqmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شیرین‌کاری اودگارد در جشن‌قهرمانی آرسنال
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90641" target="_blank">📅 19:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90640">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/90640" target="_blank">📅 19:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90639">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
فرمانده قرارگاه مرکزی خاتم الانبیا
:
با توجه به نقض مکرر آتش بس توسط رژیم، در صورت عملی شدن این تهدید به ساکنان بخش های شمالی و شهرک های نظامی در سرزمین های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک نمایند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/90639" target="_blank">📅 19:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90638">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e11054c811.mp4?token=gwf1-LIburJpIfHNhFt6_bDvLFF6Pl8-pMyd6IF7_FyUYCH4luXAg3wqO4xPYb4CySp8w8e9mWMJ9P2-n09CHvIigBWA4cePubecYhhPv48CqqwLtJ7tvz81sUdnSL7TlagiaiTxaUd1lphE0Z25n52qqOUfc5EatJIJlnqOPwD1XlHC3JHcM2poMJPHzYPzJgxduyg5LVUv00rOOUa9COblY_o2wIG0P5EwMEkzxI5WoTzw0QtPj2OyZSGpTgHuYeuoXBy8OqeubIBkuspzn5bkpcp3tinmeVkty0so67Rl4P5E0U_IHCUKE3Y9Obc6uS7Lo58C6KplZQ6aDqw7UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e11054c811.mp4?token=gwf1-LIburJpIfHNhFt6_bDvLFF6Pl8-pMyd6IF7_FyUYCH4luXAg3wqO4xPYb4CySp8w8e9mWMJ9P2-n09CHvIigBWA4cePubecYhhPv48CqqwLtJ7tvz81sUdnSL7TlagiaiTxaUd1lphE0Z25n52qqOUfc5EatJIJlnqOPwD1XlHC3JHcM2poMJPHzYPzJgxduyg5LVUv00rOOUa9COblY_o2wIG0P5EwMEkzxI5WoTzw0QtPj2OyZSGpTgHuYeuoXBy8OqeubIBkuspzn5bkpcp3tinmeVkty0so67Rl4P5E0U_IHCUKE3Y9Obc6uS7Lo58C6KplZQ6aDqw7UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جام تو خونه میمونه
😉
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/90638" target="_blank">📅 18:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90637">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cg3pCt7ofhOfAw0EHBeJhXGEM1i2qcF4tsjdbvqvKKBWeigbyCuALKlPLWK6fkYe9FoeO5o49Ylj2AvVJDLMgsB_gDOPq-Mp8HLhzUf8in7DfxJuA2yASukGt6iS4lA4CSaKvbOItMz66TBTtwIjKTqgkZmw_9e8fURtZVPgjtA3ghk_SwHi1VoWM92YV6-ySww6PynyoFDXgsdRAvpg47yVxexFISfjSJlqb22DigLAUbXAIi21WD_zCHjT8JqcUeKgnH8ortIQKpKL7Of_Zv_q1UXzPyGBJYLGKRB0KyeQuVpvNBpvmu0JoAgJyPO24WQ73zkFZcVipesiuJc-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بعد از متصل شدن اینترنت، معاون وزارت ارتباطات برای اینکه پیام رسان های داخلی ناراحت نشن رفت از کارکنان پیام رسان «بله» تقدیر و دلجویی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/90637" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90636">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QBN92qBLVsW1DBIYCOd4RKdGJz_VwYJbTMNZCyfnASz6beGUhSPmzhKDnv9AuKxT3cl2JFfB8HBzAXXzVf-_qA7r82T0coeLSx4lPtgyM5Jgv75Hx0B9PR3RJmhNYInPJNVtRO5Njso7dkofukTlK4U_WLLlsnSVw0Cg5BYbFpkWnvqCKn_KdSJFn4-_ltEgQBItbL7PpV-b8w3FSHBY00RMxgLwvV7jdh-GGtysHJvySFSCWhyQLvlIYncYsz97aJ1C70miVkh75ovn4mDI2OXhWt3TgJKoJ9UbZ7YaAe-wogcsiWIdooYuSSnUwFsKCWsa6Fy6fKm-e5QePOydZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعداد قهرمانی هر کشور در سی‌ال:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/90636" target="_blank">📅 17:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90635">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a15c25cc8b.mp4?token=RUYEUvG1RWLrzfnTX010hmefXGZnmne_uYJ6uQiJIuqRB16AdToPn4eDXV0rsaMuqhfrVGEfwOj3NX2DoE29S-hKDrgDsmuLRTeB2IyOjzzQ_o3ZUeGaVE21JWghzURRdr-ftg64Ghi3f9kqa3_tA_Iopn26uZ6n93MDSlRcaphOI4_ecc09uWb3UjKUP11LWwEw8fHZ8a0Mat8BukWYFDjtM6_VdSMP6iiI5YgxwAos2ihyxxaZH-vbZ7s9NDNUdPYSWCPu3MztLgMxMS2Ildu2AN4Lg4pGrcVfj6POahtCG6U20Wtfp8Ti7KG_XOu7_NSzIls4gBXCfnjG0NJR9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a15c25cc8b.mp4?token=RUYEUvG1RWLrzfnTX010hmefXGZnmne_uYJ6uQiJIuqRB16AdToPn4eDXV0rsaMuqhfrVGEfwOj3NX2DoE29S-hKDrgDsmuLRTeB2IyOjzzQ_o3ZUeGaVE21JWghzURRdr-ftg64Ghi3f9kqa3_tA_Iopn26uZ6n93MDSlRcaphOI4_ecc09uWb3UjKUP11LWwEw8fHZ8a0Mat8BukWYFDjtM6_VdSMP6iiI5YgxwAos2ihyxxaZH-vbZ7s9NDNUdPYSWCPu3MztLgMxMS2Ildu2AN4Lg4pGrcVfj6POahtCG6U20Wtfp8Ti7KG_XOu7_NSzIls4gBXCfnjG0NJR9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇧🇷
Vini
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/90635" target="_blank">📅 17:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90634">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da899e08a7.mp4?token=RoSAxFLCdP3FeRvDNwmNXPHA2Ll_NKM_RmIrk7L7nRt0Vwtv5H4GG0UEsgOUg-jTcZ5_QIR84Uhq8zCFjQiJoVjKcOStKki4RTC18x_xJ9WJo4ujWB67zjasK9QEr56Rc_D3DfcdHJ1Bx88EagOG0pqzvdyNyz3viOoPmRdqBtrZGtTKKU06gk5yjaqM323Rz5qpBUzkwSDupmaMAWWkHWhlgNgIK2MgUQ-Y-paVDwS2-XpZCCUCPUnZe0EyjVOkm3REIyT0MO_8RdSDUbtRQje2-jGlxWFy0J6V0vUIjtUnCDRwf-SWm5fjkKMX7l0L5WMxP_P2dTBKDP4CLzBgBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da899e08a7.mp4?token=RoSAxFLCdP3FeRvDNwmNXPHA2Ll_NKM_RmIrk7L7nRt0Vwtv5H4GG0UEsgOUg-jTcZ5_QIR84Uhq8zCFjQiJoVjKcOStKki4RTC18x_xJ9WJo4ujWB67zjasK9QEr56Rc_D3DfcdHJ1Bx88EagOG0pqzvdyNyz3viOoPmRdqBtrZGtTKKU06gk5yjaqM323Rz5qpBUzkwSDupmaMAWWkHWhlgNgIK2MgUQ-Y-paVDwS2-XpZCCUCPUnZe0EyjVOkm3REIyT0MO_8RdSDUbtRQje2-jGlxWFy0J6V0vUIjtUnCDRwf-SWm5fjkKMX7l0L5WMxP_P2dTBKDP4CLzBgBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حدود ۹۰۰ نفر در جریان ناآرامی‌های پس از قهرمانی پاری سن ژرمن در لیگ قهرمانان اروپا در فرانسه بازداشت شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/90634" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90633">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🔵
باشگاه‌استقلال با محمد خلیفه به توافق اولیه و شفاهی رسیده است اما این گلر جوان اعلام کرده که پس از جام‌جهانی و برحسب پیشنهادات دریافتی دیگر خود، تصمیم نهایی را خواهد گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90633" target="_blank">📅 16:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90632">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b05db8d1.mp4?token=DqJKdwD_idhHP8VZBiAqNP6NLRRW7DAHpheyToCpWiYh8G-nGtlt8Eau8FQouJFokILlrkvulOOk2jxuVcl_x1gmiq_Xa7rNZMXEvEOVXxzmDY1akOB0L-Hf-jQ37JhqLTSA9412KrQ8sqgbo33nMiGHo4ISN9AA-_0UtoZLCV0hCspChqHL6cFrl6KISjRXEe1BGpGvtCnqF6J1UBZOMytOs8sXgzFR29fGi4EfP8ylWc2Evv6Y1rEtF_Od2JnlvzBR-c3y0QfLH__nJuFF-BbD2Z6q0AOjBfrlplhPvA_w-vwokkCqKqkQd7ESIT4cnAAd8YOFiSEb1u8o0YInPDuSI2_gCLFIfobCXXbfZWKhAJxAEq_StDHxzmDn6SIGjYl3tWNUC1AMcxKetEeuWmmXNpKrcgBz4ecnWoRwHfbP15obeiiYr70PyzfO0mewYnGr3qCCjc4rJ_XlaYvIuY8Fhn5Bb62X4wq-uqtsHVcJFzsohbXX6BcX6uK_VyCT0gmD2K8N6qjONmVyRe3Nf5LAUB8un3I-kkIqiJ47ShSx4qqXZOqS4J4eab4oeB5m-aIrYcV-kF09bygwThbsYaQ2woXVpY8oU6Bxrtix3G7Ds6aVE-TawCQDaqtOP1fh33hhM5OdyJ31KMYfas9lJJEb4l8ZL5nd-5BQGvYUGLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b05db8d1.mp4?token=DqJKdwD_idhHP8VZBiAqNP6NLRRW7DAHpheyToCpWiYh8G-nGtlt8Eau8FQouJFokILlrkvulOOk2jxuVcl_x1gmiq_Xa7rNZMXEvEOVXxzmDY1akOB0L-Hf-jQ37JhqLTSA9412KrQ8sqgbo33nMiGHo4ISN9AA-_0UtoZLCV0hCspChqHL6cFrl6KISjRXEe1BGpGvtCnqF6J1UBZOMytOs8sXgzFR29fGi4EfP8ylWc2Evv6Y1rEtF_Od2JnlvzBR-c3y0QfLH__nJuFF-BbD2Z6q0AOjBfrlplhPvA_w-vwokkCqKqkQd7ESIT4cnAAd8YOFiSEb1u8o0YInPDuSI2_gCLFIfobCXXbfZWKhAJxAEq_StDHxzmDn6SIGjYl3tWNUC1AMcxKetEeuWmmXNpKrcgBz4ecnWoRwHfbP15obeiiYr70PyzfO0mewYnGr3qCCjc4rJ_XlaYvIuY8Fhn5Bb62X4wq-uqtsHVcJFzsohbXX6BcX6uK_VyCT0gmD2K8N6qjONmVyRe3Nf5LAUB8un3I-kkIqiJ47ShSx4qqXZOqS4J4eab4oeB5m-aIrYcV-kF09bygwThbsYaQ2woXVpY8oU6Bxrtix3G7Ds6aVE-TawCQDaqtOP1fh33hhM5OdyJ31KMYfas9lJJEb4l8ZL5nd-5BQGvYUGLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
ازبک‌های‌جذاب آماده رقابت‌های جام‌جهانی
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/90632" target="_blank">📅 16:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90631">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079475458f.mp4?token=GHxxRDZDLjlqXX5nk1mCJEJw3Ifq2gE6BFL6wslJDg9vjUMxVcfBNt2Oh-sQRd5G_b-JLrWytyqiYXEGGl-p7X4wdcuIx3nqGkY3pHi1R6GTynu5R2pi10Kgs8HipiYzrYvvY-B7ExU0VS-7YTbQbDACtF5uJXlhfjTy91nZKFO8V8VBpuwVxbSnEbsjOyjJimc-Ttm80guFlAtgUJ-yBI2s-rUnIstkaaPuHmseo0vKPwvOJQGp02YwR6u5UCmzYIzYurFOlyjlYdG1fdkJOqWgoHDgzKqWtt6V1EkuFHCmB1rf9OPRIpNJRvliSwmKQ9FAsn2yxtOpv9WnnIaQ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079475458f.mp4?token=GHxxRDZDLjlqXX5nk1mCJEJw3Ifq2gE6BFL6wslJDg9vjUMxVcfBNt2Oh-sQRd5G_b-JLrWytyqiYXEGGl-p7X4wdcuIx3nqGkY3pHi1R6GTynu5R2pi10Kgs8HipiYzrYvvY-B7ExU0VS-7YTbQbDACtF5uJXlhfjTy91nZKFO8V8VBpuwVxbSnEbsjOyjJimc-Ttm80guFlAtgUJ-yBI2s-rUnIstkaaPuHmseo0vKPwvOJQGp02YwR6u5UCmzYIzYurFOlyjlYdG1fdkJOqWgoHDgzKqWtt6V1EkuFHCmB1rf9OPRIpNJRvliSwmKQ9FAsn2yxtOpv9WnnIaQ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همچنان حاشیه‌های دوس‌دختر امباپه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90631" target="_blank">📅 16:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90630">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc7d5cd4d.mp4?token=s8QWXrOMPG786LVRA8wRAorUHo6kwtWzyaowPOCl0qhHeZqQJkT1nZJ4NGtAN3BXVX91gVgbGkKsTYVZ9ZJuSfB4ZDehYEj7bMp-PkYea2RNn5zVhYzO_MlUUURnGTE5WXwwNScoSrKSnqCom8ASW073YzsTwIQ_9t_0fp32HOWNCvVAc1uRDpVomU7RQOcxOLfgHvdlacIwRGT2l_8vieTKmgmHPLhSFmfdW0QaB36bD83LkW16aElnXsv4pcPIW6LVrdIOFA3lF9pGwZyYj0VeFxhw8cs-KHq2uxDjFW87N8rrJMpebRBPpikPXkr--cpmkw7FGLbvf3ML7HiOsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc7d5cd4d.mp4?token=s8QWXrOMPG786LVRA8wRAorUHo6kwtWzyaowPOCl0qhHeZqQJkT1nZJ4NGtAN3BXVX91gVgbGkKsTYVZ9ZJuSfB4ZDehYEj7bMp-PkYea2RNn5zVhYzO_MlUUURnGTE5WXwwNScoSrKSnqCom8ASW073YzsTwIQ_9t_0fp32HOWNCvVAc1uRDpVomU7RQOcxOLfgHvdlacIwRGT2l_8vieTKmgmHPLhSFmfdW0QaB36bD83LkW16aElnXsv4pcPIW6LVrdIOFA3lF9pGwZyYj0VeFxhw8cs-KHq2uxDjFW87N8rrJMpebRBPpikPXkr--cpmkw7FGLbvf3ML7HiOsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
دیشب بازیکنان پاناما بعد شکست ۶ گله مقابل برزیل برای عکس با نیمار به صف شدند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/90630" target="_blank">📅 16:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90629">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
لیست نهایی تیم ملی برای حضور در جام جهانی 2026 اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90629" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90628">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59f93bc5a.mp4?token=nuxs2WXTSYbX-KxOoooYj4KZiT8-Vr669TBlzKpxt4mX5XFZzNDZPf90DE95soHCqVXSfs7MZ18mo8t1dQ3LaUHARPrbdkU8D60ET-t9FPWQk71ZW6MQoLVpAevsnhFeNq6-yt6ddDRfBO7v_XxjB7yTX6_3-TWEOPH9GDLNUq0RLB4ApX2cJ_bxeNxAm21N_1skVCUTPax5zxK_ZW0GsqthDMS29f5JSRUpeD-SnkMkuYDrR3EjU0LTViQmH9oN1-uEgqBfemK80VWn5GrVB0AxR6Be97vJQ9Hwl6EQIUU0pU0GelCrgNpc9_BXSca1QD15fCJc-H4m9mfAgrlQ_wq5sYf531oy3_rIskBJF7N0Auc9YNMLdH-OR9mOOy2hW8RvF663ueR_bZfmzFgR93dcINvL3XDyQTPed6dhE0i-xB974FNT9Vji0C8_syraGHIWa1UO63GiVXKGI52DgoP457fUrIK9qyQpdrDVYaZuoNZ6aE5sqcLEvabUgVztqL4ktTW6FbiJ0li4gFD8KFxywV-wn0D2KQI8y9DHtsdZkM06pEILvJcQuysJTEE4yuE413gmG3yJN44HJuC6jGMKIEqxEmpj5OvQMtF_qXLSscW5Em8UT1QZxHk5xuhw9dTrzby5h0hrPZSDcSMGDaE3gGI47t_sHg2SczB9s44" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59f93bc5a.mp4?token=nuxs2WXTSYbX-KxOoooYj4KZiT8-Vr669TBlzKpxt4mX5XFZzNDZPf90DE95soHCqVXSfs7MZ18mo8t1dQ3LaUHARPrbdkU8D60ET-t9FPWQk71ZW6MQoLVpAevsnhFeNq6-yt6ddDRfBO7v_XxjB7yTX6_3-TWEOPH9GDLNUq0RLB4ApX2cJ_bxeNxAm21N_1skVCUTPax5zxK_ZW0GsqthDMS29f5JSRUpeD-SnkMkuYDrR3EjU0LTViQmH9oN1-uEgqBfemK80VWn5GrVB0AxR6Be97vJQ9Hwl6EQIUU0pU0GelCrgNpc9_BXSca1QD15fCJc-H4m9mfAgrlQ_wq5sYf531oy3_rIskBJF7N0Auc9YNMLdH-OR9mOOy2hW8RvF663ueR_bZfmzFgR93dcINvL3XDyQTPed6dhE0i-xB974FNT9Vji0C8_syraGHIWa1UO63GiVXKGI52DgoP457fUrIK9qyQpdrDVYaZuoNZ6aE5sqcLEvabUgVztqL4ktTW6FbiJ0li4gFD8KFxywV-wn0D2KQI8y9DHtsdZkM06pEILvJcQuysJTEE4yuE413gmG3yJN44HJuC6jGMKIEqxEmpj5OvQMtF_qXLSscW5Em8UT1QZxHk5xuhw9dTrzby5h0hrPZSDcSMGDaE3gGI47t_sHg2SczB9s44" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
یه‌کم از جنارو گتوزو ببینیم که دیگه بنظر بازیکنی تو میلان و ایتالیا مثلش ظاهر نشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/90628" target="_blank">📅 15:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90627">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIxCrhpUeCgzhAdm1gAcjiYGe6cHy3k9jQCMvvE5BBVntKSzvVxkVTZRietAB2EgqcM7pQjsGvGesdVAMLhJlKe6Eb596JxPct-0FszVVGmterDKCBU-u4f8wxQxZOqcAlShuYBjDkYLyapFgT1e4sZMx14U3za6389gvhAMGWlM-Gss2p_SewMUvxxi4oTAWrlczhLA4Cio1AMNqYioBTqSFj0FZcJ-E-4pt9Kt_LYx6FhJWwo6HkGh0jiEDHFjM5Y_JYezaXtzn8fsHTPyD0NTRBtGvT1l-JCXY3PouHfwck3AwyRnGUIBKHaIVgNWZRqOLLSVyZ_nI5R0m4Uh_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست نهایی تیم ملی برای حضور در جام جهانی 2026 اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/90627" target="_blank">📅 15:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90626">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda3613d9c.mp4?token=VdURybvzpNNEb5dzuVveA3lf7ubjUsk3zmNE1SFm-tp-e-lscDm_-mDRSj9hltUVgpu7jsrpyeRUC4cd0xO6lac3EqLPcuQ6zB1lz1JrRevpI4MXGPjZyQzi1ERtpv83mqcKiYRq_PUUYeYS58BxjGoTK_aSf6C-cLszg0fUQACHkuEYFQhAp-qJAKOPb3K_4qoGg7fY1_5zU6ousI4sp55T7DS3yDaN9y3wBcqRZP0_fEEPHJ1uYRa6WxiPgYr7derNc2YcNUZS_sHxx-mL9osJdJlc4DcY7PabEEo3aSC2tUy9o8LbKcjOb0gQsXC5MYDdxD_8RI6r6TlJNwrnRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda3613d9c.mp4?token=VdURybvzpNNEb5dzuVveA3lf7ubjUsk3zmNE1SFm-tp-e-lscDm_-mDRSj9hltUVgpu7jsrpyeRUC4cd0xO6lac3EqLPcuQ6zB1lz1JrRevpI4MXGPjZyQzi1ERtpv83mqcKiYRq_PUUYeYS58BxjGoTK_aSf6C-cLszg0fUQACHkuEYFQhAp-qJAKOPb3K_4qoGg7fY1_5zU6ousI4sp55T7DS3yDaN9y3wBcqRZP0_fEEPHJ1uYRa6WxiPgYr7derNc2YcNUZS_sHxx-mL9osJdJlc4DcY7PabEEo3aSC2tUy9o8LbKcjOb0gQsXC5MYDdxD_8RI6r6TlJNwrnRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
کشور سنگال با انتشار این ویدیو نوشته که ورزشگاه لس‌آنجلس یکی از میزبان‌های جام‌جهانی مشکل جدی در چمن داره و خواستار بازسازی فوری این زمین شدند
در این ویدیو مشاهده می‌کنید که توپ با برخورد به زمین ارتفاع نمیگیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/90626" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90625">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">52.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/90625" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
✅
🎁
کد هدیه 100 دلاری:
Sport100
🌀
کاملترین برنامه موبایل
🤝
اسپانسر رسمی لالیگا
🥇
صرافی معتبر
🌐
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90625" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90624">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMelBet | مل بت</strong></div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🌐
اسپانسر رسمی لالیگای اسپانیا
😀
مورد تایید سازمان Gambling Judge
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/90624" target="_blank">📅 15:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90623">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhbVL23_I3QgCjKVCUuL63M6IfLe8fdNUuSrQlWzchLCwz5ODb_2YSzJLm-kVkxmIdF_OiHeOPXGQIwaKfEi9A8NpSRHAfwemN12ZjnoHIU71Yyrmr-f8ZyWdrlUZlbuhBOxeSb5rpBqXt31AyoZAGuaWtbvsT-nOFzMIQqeW0biVRYc1-gA_eB4BQ3vfJwMfMPRGE-vpgIEO5jPaBNijPACo2o37EXXrCRWqgVuy_Y2q-VQ_KYK3DzUpwTsC4KDdH8UVkfUaOIStn0wcd5f3J_twv7k78SlgeIW8uV93qSrVuxXTegVudxYX0xZ7WOxdih86W9cLR8q7ph5H_V1YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی و بادیگاردش تو اردو آرژانتین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/90623" target="_blank">📅 15:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90622">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RM_3Hi1Yq4cIa4VQ6pVqHqGrPOMc6u3coWhzoaQSaBntbcuHMh22bbJYGGi_Us_rAP2Y00iQlTM5P9XV5ce7Iojl304kjaEE4K5JU4Eo5qG-T8nWXbKMtiB029lbkXS2nY4Myn9pfR_p0hm3eKdJUCIOAW44fMOVDKGfurC7_NnV8g3-UZcgyWImGmB91lIF2wQysWvOPRuLEn6VpFLL4QIUSqZYcoSNUrXSoB2K1d0AK-8eayg7zk_oTIhhePU71qD5z1Uxdc1UNfKpnvKTCzPMS3XyNoZVAzIuIEKWbUPxEAx4SQHK1xb01CkFNELNzWnu8_TztjJDzXcOKqT5Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فووووری
؛ با اعلام رومانو، قرارداد آنسو فاتی بازیکن بارسا که به صورت قرضی در موناکو بازی می‌کند، دائمی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90622" target="_blank">📅 14:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90621">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0da9f9a8d6.mp4?token=Io7D4SHfzaAkDfhTUPwUtbn2h10HEqitbFPpoGFv5NDRbQS6pMa4_W-knZcr6mFAsC5GUij1hnhrkTOBGNbYaxF3SZUBmHxXIlKWnCUf-ct_aiJkY8_8xE0QgFsJKKqyvGGl-7o8j1mYJOocFZjzYAvgqIyppiO3isKFj2ekDXIOnem8Tdm7Ys_zezodZ8QLPPIjD74aVjokrOcrrQadonRX26In10Uw1bLphGVgWL099uQ0Emb4wzKJRTwaXTzHMYpHetmsBA2sU_B6JDXY0SBGBRf6yMf2N13W-ea66WPgzYS3bndHMYo_OypzFVFubspDZoBv1Cugo-eRGGbBAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0da9f9a8d6.mp4?token=Io7D4SHfzaAkDfhTUPwUtbn2h10HEqitbFPpoGFv5NDRbQS6pMa4_W-knZcr6mFAsC5GUij1hnhrkTOBGNbYaxF3SZUBmHxXIlKWnCUf-ct_aiJkY8_8xE0QgFsJKKqyvGGl-7o8j1mYJOocFZjzYAvgqIyppiO3isKFj2ekDXIOnem8Tdm7Ys_zezodZ8QLPPIjD74aVjokrOcrrQadonRX26In10Uw1bLphGVgWL099uQ0Emb4wzKJRTwaXTzHMYpHetmsBA2sU_B6JDXY0SBGBRf6yMf2N13W-ea66WPgzYS3bndHMYo_OypzFVFubspDZoBv1Cugo-eRGGbBAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
یه بلاگر اروپایی اومده فینال چمپیونزلیگ رو اینجوری بازسازی کرده. حتما ببینید عالیههه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90621" target="_blank">📅 14:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90620">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBr1R4297vkS1GkxYrSDwRjeY2p5CbCtWTfS7wAS2DAOUDSZbZbNq_fXOrSjKI5iUTz-6saWnydbMEFFf4v3oaBOiOWI5UATPB7Wzo6ZDbBen0w3g01y34bbEBs6ByjrRdeHjdQZifeU5kUfvycYEnsGFk2c1iSSU27g6TroW3Xa2Gv1n81OcOkQgVdg-1cy3RqDT0smY0zp7c0JtIpL1T1Q_NunwLON-FybnhmOLtUEChhhvui9kTGtKwVnqGqkhOXeWtZOJZsqQRY2Vy-up1iKfvlP7q4Sio5JnRKycK35PGOhSyOTnChzeG19RFq1M33VzqQvYH49Fv2_WCAYrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#نوستالژی
؛ سال ۱۳۹۳ و همزمان با جام‌جهانی ۲۰۱۴ برزیل، بسته‌بندی خاص چیپس در ایران برای تزریق نشاط و تماشای مسابقات در ایران...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/90620" target="_blank">📅 14:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90619">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
سرزو (رئیس اتلتیکو مادرید):
«جولیان آلوارز بازیکن اتلتیکو مادرید است. نه فقط برای فصل گذشته، بلکه برای سال‌های زیادی در آینده. ما همیشه در حال تلاش برای جذب بهترین بازیکنان برای تیم هستیم. تا ماه آگوست، وقتی لیگ شروع شود، هنوز زمان زیادی برای بررسی، پیگیری و انجام خریدهای جدید وجود دارد.»
﻿
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/90619" target="_blank">📅 14:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90618">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEPL0oxibqAN33EUQgfuW78sLZTWC7XMzsQgfsZ7jF1n4AZw3WtnEzMDtlafJCJL9JBWfHVpRC7QpWxl0a4kBwsIPNKCOmvH7L--ae67j2naHJ-pskl0ialD_Hd5EPmgYqmDM4pKdERwZ6NPEHIsV2f9fmqZj2bQDeUVk4CxKiRxVz02nbSGjLaV6w0Iea3FIZ8Mqdi1iV75sc8HS0uTSTJ_sHiei2uTKs7an1nqGk5eA3dVrS94X4IsFKgZKpW1KDBgzYI66SWkvxMSL9d44eM3E0kR7pOXK-_4J9nC7J5SYOkmIHY-e1nd6uULRmYZCcCFlFbRwzYQMQ7z2zu-Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
⭐️
مقایسه آمار دزیره دوئه و لامین‌یامال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/90618" target="_blank">📅 14:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90617">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14d1ebf50c.mp4?token=BOaPS7X723okI14tP8dU7VrDjD1CroneD5gVv6RPDuihjekB9xTXXySID8FXHD8FoEBaOqRFL4h80CRNANbZJm977jbbYmCbhynMFEJcK9HcsAlcLuv3FGZKVZvQTQHXD9RenE1F6oDuTOcg3tz3vh8sN-aogwBHbHTVzODqR8UXcyOtuCXp4RE45qbeaMLfoQg4-OlwF5k7fLOc_J2HEeDmL9ICJq3msqXHd1EsWJ6siS5Xcbp1DBBE6b17_-WJScglnCA6I9kk8KyixV5bpcUlIhXEtzmuMwTrmTzaKUcb2VLM_9KwkXBEbx85Bn6aGee0rC0q8kHRCqXNSro6xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14d1ebf50c.mp4?token=BOaPS7X723okI14tP8dU7VrDjD1CroneD5gVv6RPDuihjekB9xTXXySID8FXHD8FoEBaOqRFL4h80CRNANbZJm977jbbYmCbhynMFEJcK9HcsAlcLuv3FGZKVZvQTQHXD9RenE1F6oDuTOcg3tz3vh8sN-aogwBHbHTVzODqR8UXcyOtuCXp4RE45qbeaMLfoQg4-OlwF5k7fLOc_J2HEeDmL9ICJq3msqXHd1EsWJ6siS5Xcbp1DBBE6b17_-WJScglnCA6I9kk8KyixV5bpcUlIhXEtzmuMwTrmTzaKUcb2VLM_9KwkXBEbx85Bn6aGee0rC0q8kHRCqXNSro6xoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بالاخره یه ایرانی هم پیدا شد برای تیم قلعه‌نویی چالش اخیرا ترند شده رو اجرا کنه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90617" target="_blank">📅 14:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90616">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz_WRCyOHMRA67dTKuB1c6bKG-DQCGXLaPi9v9mHSPMntddkLO9uPJvkGJ1nGI8upRdM3Z8lpfgveq-H-nkxMmMkaaETbDZhqQQxIiKVgAXxwPVYRkkShaquHeeL5dWGMThn7EjrZOsRRYi3cMc23CgPb8-VLGomkFl1xuixKsAthJ-NJcmCi4SokZ2IQyl09Zh2-kv2MNn-0M5klU6qPL7GDQan2jg0Ioqd0TvxRP-JPZ9dynzjlsL-kcT6gqdocEXaX6WXo4Pc5ZbkwMBktd1NC6dgrYfGgz8aEpVV7f79ab6aQWaD1vQt5m2nOiXUid9HrK-pQF_pzTcpOQPAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
داویده آنچلوتی به عنوان سرمربی جدید لیل فرانسه انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90616" target="_blank">📅 13:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90615">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
#فوووووووری
#منهای_ورزش
امروز حوالی ساعت ۱۰صبح در دانشکده پزشکی قزوین، یک دانشجوی مرد در ابتدا همسر دانشجوی خود را به ضرب گلوله به قتل رسانده و سپس با تفنگ، به زندگی خود پایان داد. سپس این دانشگاه تا اطلاع ثانوی تعطیل شده است
😐
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90615" target="_blank">📅 13:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90614">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a22b3eef4.mp4?token=qXImzvwVUhQVU7jYPxWBA995vhKV3iTf32ie3cAazMkut6SyC4-TRm0fVLV1_x9zuJ2VoPMMk-nBb-qksC8YxtZrfBCLkZWPwlHNuV_NizNHh_gQ_5P0KTXBl_CVWJm0VWp3pgDFiubJW63fBAKUmiP68SsM78mLsxJFmS0RpigAvxTd9G_tL300Qz2MPGH_x-M14wNCokaWDG9cGHxq06dAqdD20C-ZsqaGsd1l43Of8DBpamWbsJF0P4B-MQrt1jaq7pFSb_prNjXKrmgn8TP2JI281CjYKFf9WsuHgEUYBGL5clVRyOt2ACZra_NkrLKlPgrJihCmXQNb60ixqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a22b3eef4.mp4?token=qXImzvwVUhQVU7jYPxWBA995vhKV3iTf32ie3cAazMkut6SyC4-TRm0fVLV1_x9zuJ2VoPMMk-nBb-qksC8YxtZrfBCLkZWPwlHNuV_NizNHh_gQ_5P0KTXBl_CVWJm0VWp3pgDFiubJW63fBAKUmiP68SsM78mLsxJFmS0RpigAvxTd9G_tL300Qz2MPGH_x-M14wNCokaWDG9cGHxq06dAqdD20C-ZsqaGsd1l43Of8DBpamWbsJF0P4B-MQrt1jaq7pFSb_prNjXKrmgn8TP2JI281CjYKFf9WsuHgEUYBGL5clVRyOt2ACZra_NkrLKlPgrJihCmXQNb60ixqjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بعد فینال Ucl بخاطر شرایط جنگ در اروپا، استفاده از پرچم روسیه برای سافانوف گلر psg ممنوع بوده اما دوس‌دختر سافانوف با چنتا تیکه پارچه برای شوهرش یه پرچم می‌سازه و بهش میده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90614" target="_blank">📅 13:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90613">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnD7sPnov07hlBJIkES6K0yyA9ovbuBxvw1XlC6OPDiSlFbbfAeiO74ITTsmY3yynJq5Svh4o4-R1eZ_jCBep_TkFs2-cHmXEVlTm2swymOOI1qSb4s99y4Jok1bXVzVum-yR02mfFXTumGff4DYlLsmMHZSCpTsR_m-npZQmC9yF4ldiYA4S4T3_UizWT64kU4zr56rqwn17wSuCkoq3hNDCTIFFITUKjOBoEnnbCUmLNItL4qPt9suneQBM28b48oSn-wiWwycYM2xjmyb1O-2U5D2cTO7rmX4-xgkkQiPYKUlwBX3rTYwN3f7yaZhrbZD2DmkphKIYQrqvIj0pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات
|نمایندگان انزو فرناندز درخواست رسمی خروج از چلسی رو به مقصد رئال‌مادرید به مالکین شیرهای لندن ارائه کردن. فرناندز گفته به هیچ قیمتی حاضر به موندن در لندن نیست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90613" target="_blank">📅 13:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90612">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtKP7IuyFp1fvJX016971_agk45ua8weGXN4-ZV1zRm7TwW5aAEhldL3QvBj6XEmbkhkWhOC8Or00f4lM1brXdluKRgAdsC7KAo2SasOpAjgIwkoptAZVItX4d9_RPnzWsnQ9952aXM1eu7R2ABrHVwUOECStwbObjxzpddN4ecgkXyf9-1Vv33-jB-pyqdQYKXRP2v6VEcrqKPezSxTndh_7ulpLwXevVexh3NVSz0u_-JfCkI_0f7LyIzvnnvRvPa2nRDJ1j4C-zm8tWGh1LV5KRHwv-fUZEi5DkrGme_fW3vFcd_4m-jGmTw_4HWhT9sApBX51ejzRS36lCvG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
مارکینیوش با عبور از دنی‌آلوز حالا تبدیل به دومین بازیکن پرافتخار تاریخ فوتبال شده و‌ فقط لیونل‌مسی از این بازیکن جلوتر هست
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90612" target="_blank">📅 13:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90611">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B90uMvLM-yUBJHzoXmdPfmmvAtLjZwiO8PL363NlCt6imgU0mShocaLkrOLYt8qbC-osnYTfzEtA-9Pz_-fi7b6nHnnr0GN_-ad07K-xeaAsRyTMJH6ClXgfPHdXqgfiiU_VgVMijl8CSgOCxQOAIYcw9zch2YBV_oFauISuNYg5P4qL9YVPvo-jMvWH14gfWwMt0pVUdWqQ2x_A5ZkZb6LxNobf0Dh-ow3FQkmlJTj5bmhHzL-6kmILOrIA4mkanhJhyyPT77braCupJ1SrX3x_LbzsY4w5hNiawzKzaKotzN75W06yQ0Hb8TjwMdKQDuYmh46GDmjjz9dO9iWpvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
داستان خولیان آلوارز تا الان:
❌
تصمیم نهایی گرفته شد: بازیکن در اتلتیکو مادرید ادامه نخواهد داد
🇪🇸
مقصد مورد علاقه: با بارسلونا بر سر تمام شرایط شخصی به توافق رسید
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
خارج از داستان: آرسنال و پاریس کاملاً از رقابت خارج هستند
🇪🇸
فشارها: بازیکن و نمایندگانش با تمام قوا برای نهایی کردن قرارداد فشار می‌آورند
🇪🇸
🇪🇸
موضع مدیریت: بارسلونا پیشنهاد رسمی ارسال کرده و منتظر پاسخ اتلتیکو مادرید است
👀
🇪🇸
طرح جایگزین: بارسا پیشنهاد دومی آماده کرده در صورت رد پیشنهاد اول
✅
پایان مورد انتظار: اتلتیکو از تمایل بازیکن آگاه است و نهایتاً مجبور به نشستن پای میز مذاکره خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90611" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90610">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmoYAWNqPjqFBk54PDY_6UpMbgolXo7q3RTaSe4vrEmiaWeRmLE9caw6L4G1dIakKx7RK-5kv6WMJ6vxwVQ6jvnxTJpkZ-JQznyqSHKSDKLUTQvpC9qP0eLGwldlIv8Qb7UNOs81cCkQ9pkPPezsww9QZmZQ11y_UrSoxhbUsq82K8KMRBv-G453_nyMiLy5R6rwzfXs1y2rOWrCgKyC0_JA9x6xVaaWIwpPmsK_FFkyLLb4ElFNSD5hx_dK3mqECLpU0TrRBUE2h6zV48W4YBUx1ZuH3p6yAOZOwg3Ox5O2VP_07YZvNDvbIUSIByERLT_j9KtZ5zQM9OG_oLxsoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سافانوف گلر پاری‌سن‌ژرمن و همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90610" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90609">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/90609" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90608">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFRZio9V4wVRljg2LzxRnYhDsAU7lV1itGYjjFMRAkPNbn5nj1VuOUxI5RT8JmECEUC7mZa6N-6bQeVgjOV_b_1946ZPyhMq82x4TNqfywf91tajkyznEOcW_ws1H3Hy09iF4Fd716zBihZO9VNKdUpNXXUJM2i_dK493L75Xbyt40L165NwiB3nkode4hujQqYfZLJaP1sCFUDLtVug7Deb-xfH_401uD7aw5kjRfPz-EuadZ7XR3_HzF0opMGtHBwLZSgk2T-x_utHhLRZelGm3G1CK9oUJdTpt2mt7UVNljRuFxH4oRkAMVXjcyQPYtwRF6XvC8mnH-d71cJnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌇
بونوس‌های شبانه از 1xBet
🌒
هر چهارشنبه و پنج‌شنبه از ساعت ۶ عصر تا ۱۱:۵۹ شب، برای واریزهای 5.50€+، 50 اسپین رایگان در بازی
👑
Crown Coins
👑
اهدا میشه!
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
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90608" target="_blank">📅 12:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90607">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9fc7368f.mp4?token=q5s7MBlauoDqGgIXT9smeDoc06lvdMWjLCmk8yDsgN6mRQcrSZG63WXjxe0L-bIG7FRM6kWWcM18ckQMjRLZ1iRIEmCci4S_eMGHx-e7LvjrViMNpZtD2EaehmFgyvjwan8whSd1ad6Hi5VYoD3xlBejL6dSGNPaOe3uFeJ7rsLdxr9h4PET7wmQanLbsN0MVzy5WnEHkk5fYLwvaOboZZZrkTD-ohkY_hAJZIfCACarGXoD6V5BfFTaCXrTDQ1cuRtzk89SPGRt5VojzyOm19I21PXSW2L1g-N6LOJFJG42xobHHBMT1GazE4bfXAi89f2goyDa9uFL5OYlrfsHWbC3hLUmdPf75PcQLChM1HvKWbvqeMMN-ihJqrOR-rbchtWoPvnYbbh4ntkme64bOQQq3KrCF47LoKrX9KNJkyA19mQS7kGbKRJMJ_R2RpMW8ELJWagmigtTBcwji_mhRN2cs3ZDcxrZquXCopo7cbXZ697E6QJI30dVnZDdW1dLEX9Stw6Eo1Lbp7V3EMG6XnJI5rRTC1ShUame3RpEyOuClX1rbs5ccTyN-EcNSfqawZaUkuE6o7WEi2AsmaF0LZi0h1ZKMp4W9A46BoaUF8iFUkKhDa33xWsZytTujzo9SIcoWUgYgKKbqIfqn_hvwPY589BDmO9OSQHXYRpu8XM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9fc7368f.mp4?token=q5s7MBlauoDqGgIXT9smeDoc06lvdMWjLCmk8yDsgN6mRQcrSZG63WXjxe0L-bIG7FRM6kWWcM18ckQMjRLZ1iRIEmCci4S_eMGHx-e7LvjrViMNpZtD2EaehmFgyvjwan8whSd1ad6Hi5VYoD3xlBejL6dSGNPaOe3uFeJ7rsLdxr9h4PET7wmQanLbsN0MVzy5WnEHkk5fYLwvaOboZZZrkTD-ohkY_hAJZIfCACarGXoD6V5BfFTaCXrTDQ1cuRtzk89SPGRt5VojzyOm19I21PXSW2L1g-N6LOJFJG42xobHHBMT1GazE4bfXAi89f2goyDa9uFL5OYlrfsHWbC3hLUmdPf75PcQLChM1HvKWbvqeMMN-ihJqrOR-rbchtWoPvnYbbh4ntkme64bOQQq3KrCF47LoKrX9KNJkyA19mQS7kGbKRJMJ_R2RpMW8ELJWagmigtTBcwji_mhRN2cs3ZDcxrZquXCopo7cbXZ697E6QJI30dVnZDdW1dLEX9Stw6Eo1Lbp7V3EMG6XnJI5rRTC1ShUame3RpEyOuClX1rbs5ccTyN-EcNSfqawZaUkuE6o7WEi2AsmaF0LZi0h1ZKMp4W9A46BoaUF8iFUkKhDa33xWsZytTujzo9SIcoWUgYgKKbqIfqn_hvwPY589BDmO9OSQHXYRpu8XM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
برخی از برترین گل‌های فینال لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90607" target="_blank">📅 12:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90606">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASKqjsj6y7sqUisT40DdXnePjHZdlLqVU_MoC81sT3HpPXy3rK_uHz2gyf4XAXebIHXXIILxPPIWK7iPCK6esC8SJCVDu0WSs4LUnfak753x17Kd22j9KKB8ngPSNicbA9_GHjdii4sLCn2tsZlEMPVx5mSxKjoqat3EU9u-jHe9BHosgElevCu1DaMGoweIEP-T0noZn62Oas2Cu6J8OQFrQZrmK3MvdlRos1OQy57pKQ9XibafPfzG_KB-mP-FzIhcmEgYQvKGdRDtvtJyD7sffWynhxgfNmJBurFRoIYNr_2JF_11ZEGFPD-ppVHUt-_ko5bp776yb6M9ASTGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
گزارش‌هایی غیررسمی از فیفا:
❌
فیفا قصد دارد «تمارض یا مصدومیت ساختگی» را به عنوان یک تاکتیک در جام جهانی ۲۰۲۶ ممنوع کند
❌
دیگر اجازه داده نخواهد شد که از آسیب‌ دیدگی دروازه‌بان به عنوان بهانه‌ای برای توقف بازی یا گرفتن دستور فنی از مربی استفاده شود
❌
بازیکنان همچنین نمی‌توانند در این مواقع به نیمکت ذخیره‌ها بدوند تا دستورات تاکتیکی بگیرند
✔️
تصمیمی که هدف آن افزایش سرعت بازی و کاهش تقلب است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90606" target="_blank">📅 11:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90605">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7181ecdb60.mp4?token=JK-JxAlzqgIHoNXcmP6ZZld-2NJvQcy4FFYAysDacUYDhqqJYD9WbgbUj04xV-lD0RlIs_QCcukQu_pUq7KBMaQTSv6L1G1zXBFfTdch5FPu-YUdYBNDIGPF8h6N2RNbxcKwjAkniv0EUpuxnAJRULNWt9GQI_dzz6Hv0T8vnfW2ALasBKGConluAAXmVGkmIvIV9zmTY4kZkJoGY3k__6ZpNEkZxQsT6kNL2Mj6wnRya54emUoS6MwNPrb_WhTXNrEEAqQVjfhKezf7p3jZOUb_eI8uNv_W4OUOosH_aydxeG4YJMihi3RCSeLlNwWWVb37C6avhdmF3Y8TOynTEB-72E_UcF852aHIPDSyIhqyqulJMCNArkgSg_-1k33feOTeHx6VxL_rQS8JNnXucwpxpEeb2hMY_moALWrC3023HaYCArL-bxtI2OcN2q4yduJVh7J6-iVP39ztfy1GuwqcwvSXwrI7MgZz7jpP_5mDGZb0YltKxVP0rlnRmJqtf-NMO6MAGNh-YreJtFs4JmX9j6D7EbEfT8P0Jp0nnNu9nz2rfe1LujFF0PlnvI48BiSvIWAcJEpdtGskRZgVkyAmQlQUEDaGunldZGGsuV3C5DrmFvfbRFh117hGEhDT_yLRgDx09fUSIFkTfaZf5K4sC5osuSOaGJmKrkZ30zc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7181ecdb60.mp4?token=JK-JxAlzqgIHoNXcmP6ZZld-2NJvQcy4FFYAysDacUYDhqqJYD9WbgbUj04xV-lD0RlIs_QCcukQu_pUq7KBMaQTSv6L1G1zXBFfTdch5FPu-YUdYBNDIGPF8h6N2RNbxcKwjAkniv0EUpuxnAJRULNWt9GQI_dzz6Hv0T8vnfW2ALasBKGConluAAXmVGkmIvIV9zmTY4kZkJoGY3k__6ZpNEkZxQsT6kNL2Mj6wnRya54emUoS6MwNPrb_WhTXNrEEAqQVjfhKezf7p3jZOUb_eI8uNv_W4OUOosH_aydxeG4YJMihi3RCSeLlNwWWVb37C6avhdmF3Y8TOynTEB-72E_UcF852aHIPDSyIhqyqulJMCNArkgSg_-1k33feOTeHx6VxL_rQS8JNnXucwpxpEeb2hMY_moALWrC3023HaYCArL-bxtI2OcN2q4yduJVh7J6-iVP39ztfy1GuwqcwvSXwrI7MgZz7jpP_5mDGZb0YltKxVP0rlnRmJqtf-NMO6MAGNh-YreJtFs4JmX9j6D7EbEfT8P0Jp0nnNu9nz2rfe1LujFF0PlnvI48BiSvIWAcJEpdtGskRZgVkyAmQlQUEDaGunldZGGsuV3C5DrmFvfbRFh117hGEhDT_yLRgDx09fUSIFkTfaZf5K4sC5osuSOaGJmKrkZ30zc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پشت‌صحنه فینال لیگ‌قهرمانان در استودیو گزارش‌ ورزشی که دیدنش باحال و جالبه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90605" target="_blank">📅 11:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90604">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=VYoB7Ue7C4J9RAU-cAY3RTRex3gDK0pYivw7tIHMgMjsrKE8zuqfC_EVT-6T2BV7a2cdBToNAepWUlkD9xda_Nyo4EXsUc0JnZBbuEdxGZgPFXLkRa_70mjSnhYfEHK_CggGHLpLJr3ce3H218bwFfh4_PipOVZ5NMD6iIkAzgz9Zh5cp_44Wp-XYf9i0pUFW79EScrIaqqFUrNE_04xIkTcl-yQQr8PaEqJUnmXR5QAhs4g5-fuUC5p8wqasYGfwmBPZiApKWZ_EDXh00YjxIarbwP0wq6pAYpUjDBOmtY5ql6c11_pYhI09eH8eNCja3P62ODqQdGsXBn0rKdwfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05ff67e8c4.mp4?token=VYoB7Ue7C4J9RAU-cAY3RTRex3gDK0pYivw7tIHMgMjsrKE8zuqfC_EVT-6T2BV7a2cdBToNAepWUlkD9xda_Nyo4EXsUc0JnZBbuEdxGZgPFXLkRa_70mjSnhYfEHK_CggGHLpLJr3ce3H218bwFfh4_PipOVZ5NMD6iIkAzgz9Zh5cp_44Wp-XYf9i0pUFW79EScrIaqqFUrNE_04xIkTcl-yQQr8PaEqJUnmXR5QAhs4g5-fuUC5p8wqasYGfwmBPZiApKWZ_EDXh00YjxIarbwP0wq6pAYpUjDBOmtY5ql6c11_pYhI09eH8eNCja3P62ODqQdGsXBn0rKdwfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اکسپوزیتو زید جدید امباپه درحال قر دادن در کنسرت دیروز بدبانی!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90604" target="_blank">📅 11:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90603">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4pYKbUNr7L-IISiVhl7zbv-c-_M1wB28Yqv_dwBbJiX8TwwKNU_rPG7y84fFdgZUUZfFLQ6wYNGS09xFqXOo-gFqnJn5M_KxJFCw4XHk0jGaQmZ_1WsmvqxFi9dLuyUo-ivVhEqlmmNue1Bk3LpDNGxLdm0t6Pq1Rqs9i2Xa0hJ8bW83WBEpt7IZ9_wPH6siACZu_1Br5Jtm72nB8NtKwT3-pQQUfBKZkrEn6xf-kt25RO0dHZd698J19vMXMco3dOHDYOoMfWq0frjoZHuH5CfJXV_2eI9kMiXQhstFh5zlnDwFLEtYeJvZaE646W5tdJY5fF8Jqrj0cRuLFtNzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
👋🏻
جیمز میلنر ستاره سابق تیم‌های لیورپول و منچسترسیتی از دنیای فوتبال خداحافظی کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90603" target="_blank">📅 11:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90602">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4e59e2547.mp4?token=Aqzd7rtPStwn37vpnjDU_3z6k2s78aBe5X4iNdQR6uw_r2f-qjSxcqFMJCsKcTruYHx4wHcugRhMLAx5gGxX-Z4tbDflfjLrT6mlNBA19p-dhI-nv7f2QKNEGJIqbfUzfJe7bPmWmuUGOh5ZnV_xLCJEYonyOAifL0j79YE_w1xE6WmuNLJ0tSgb3EINXAnhWkSgRJbQI7VMZ3UV0DMy_dGbh_x7n7gaQ3xrcDH3S7xPAi1H0G6E5rGecBqp28vYOKB7mGa6MX6w8Ukfd7uKAtvU8XscKupaow6JWe0qTwFXgozM-UfspmvSx4E0LmLABtIfIEKwb4AnbsIWR7XzZT3Wjl5k9ewb0TgLK9l6aF2COegOMrMxv65f7uuXAIQLd_xWR6kZQJFZc_nNHyNzrw2XJ5yF9ZO0UgndKT9UctYa2bBHT7HOeEvdOFMjcWY6I-xLEieOSsBScs71R3WvjQeHZxmTuLML1qxbPL5AGs5HTB9vknge3kWTd-EvXCwURzbC9yYmUHskgY5vvQ_EG1Z76LDCBzeTUv5oWG-y0-1XFtLdDEWTbIEObbz0NRXKyKDnd0muZvqRzcuWYKYpMb09EvzzSTaFspWDFYsNFdqtxJIj_loq2cib6_ytDe7dSS_6mjT7FKYcbOO1nHbmXaGVXbFHNna2tWFeg2aNSfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4e59e2547.mp4?token=Aqzd7rtPStwn37vpnjDU_3z6k2s78aBe5X4iNdQR6uw_r2f-qjSxcqFMJCsKcTruYHx4wHcugRhMLAx5gGxX-Z4tbDflfjLrT6mlNBA19p-dhI-nv7f2QKNEGJIqbfUzfJe7bPmWmuUGOh5ZnV_xLCJEYonyOAifL0j79YE_w1xE6WmuNLJ0tSgb3EINXAnhWkSgRJbQI7VMZ3UV0DMy_dGbh_x7n7gaQ3xrcDH3S7xPAi1H0G6E5rGecBqp28vYOKB7mGa6MX6w8Ukfd7uKAtvU8XscKupaow6JWe0qTwFXgozM-UfspmvSx4E0LmLABtIfIEKwb4AnbsIWR7XzZT3Wjl5k9ewb0TgLK9l6aF2COegOMrMxv65f7uuXAIQLd_xWR6kZQJFZc_nNHyNzrw2XJ5yF9ZO0UgndKT9UctYa2bBHT7HOeEvdOFMjcWY6I-xLEieOSsBScs71R3WvjQeHZxmTuLML1qxbPL5AGs5HTB9vknge3kWTd-EvXCwURzbC9yYmUHskgY5vvQ_EG1Z76LDCBzeTUv5oWG-y0-1XFtLdDEWTbIEObbz0NRXKyKDnd0muZvqRzcuWYKYpMb09EvzzSTaFspWDFYsNFdqtxJIj_loq2cib6_ytDe7dSS_6mjT7FKYcbOO1nHbmXaGVXbFHNna2tWFeg2aNSfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه صادق درودگر راجب مصاحبه و مناظره معروف و جنجالی شبکه خبر
🤣
🤣
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90602" target="_blank">📅 11:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90601">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05002ce01c.mp4?token=mzZBd3AfPrkQrHABQc53KwjoIVTvGoeEJSH5dgEq4-CBrswXvCs9Gt50G3dHuwqpYuKdgg_0Ba4aikcC5hytOrIDB0C6-2shThrwdjVtu7i5iLVPEhknXITfRuWdts0PExmKw2jW9-9m4T9p07BaMUM5OB_GbEskIB3Kr6aPuBXkgaEpIOLdvRGfqsAxFnmX_uhfbOtxT5L5_Uj2uejfNImzxyNnC2v33ly96r5-I3r3XzIdAJbnZo9Pt826vn1I8TDxJVsuxGTWEEDEExX0R2fnMU72pY8RYDVxfgfVAhNYT8ifKUbPMr7ML1fulEeC1edenjgVeQWa2FFm2eroBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05002ce01c.mp4?token=mzZBd3AfPrkQrHABQc53KwjoIVTvGoeEJSH5dgEq4-CBrswXvCs9Gt50G3dHuwqpYuKdgg_0Ba4aikcC5hytOrIDB0C6-2shThrwdjVtu7i5iLVPEhknXITfRuWdts0PExmKw2jW9-9m4T9p07BaMUM5OB_GbEskIB3Kr6aPuBXkgaEpIOLdvRGfqsAxFnmX_uhfbOtxT5L5_Uj2uejfNImzxyNnC2v33ly96r5-I3r3XzIdAJbnZo9Pt826vn1I8TDxJVsuxGTWEEDEExX0R2fnMU72pY8RYDVxfgfVAhNYT8ifKUbPMr7ML1fulEeC1edenjgVeQWa2FFm2eroBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
#رسمیییییییی
؛
گل فده والورده به سیتی به عنوان بهترین گل فصل لیگ قهرمانان انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/90601" target="_blank">📅 10:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90600">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aChMRVcawUFok5kRox4WmwrnsTZHP9EAay21xbEUqSZMaWyVd78upCLOlSkmEYAuXbPlUwQlHPMo8LopJOYzTew2r4WTWszwhL50GKxmAu04KUxVSBH2YFBjQbjl2XIbItFdtP-k5wTkWrEAsZotYoSv4wK9neZomNtJAaNyn8Pcz0QvNYwWvPxKEhklx-VyIHn7nEzq3DASR3qdDcaKvayOsMbs_DSxNg08VWRHtSQAiMaCsCbgRPzsMFUmT46-EoMPXtW7FvkplyJVWEA0_rYV0Um--IcbSzpJFpF4EYIUcJf5Ru5p60MAo6ezA-xvroZEa06kW4XgmVUNkSuJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
علیرضا فغانی اولین داور تاریخ فوتبال با سابقه قضاوت در چهار جام‌جهانی مختلف
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90600" target="_blank">📅 10:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90599">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
⚽️
❌
🔵
#اختصاصی_فوتبال‌180؛ فرهاد مجیدی سرمربی سابق استقلال بدلیل موضع‌گیری در اعتراضات دی‌ماه، شرایط حضور در لیگ‌برتر و بازگشت به نیمکت تیم‌سابقش را ندارد و شایعات مطرح‌شده پیرامون حضور وی در فصل‌آینده کذب‌محض است
❌
درخصوص نیمکت‌استقلال طی روزهای آتی اخبار…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90599" target="_blank">📅 10:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90598">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuSU92EOKbwY6bHSGDVgRpRvesUD9J1Ys3IQMkoUd9tj6hoS8Vdq0D7wMnusqLQtMjAcHMPxKRv8XXNlmp6RoWyHIKZd5aotYneKePURsRFI3Rhv3UfT-hXVoGBvGAZcAPaU0S2kUK6fco5g9ZOuejvspuorF4MXzjtfb08kW7w4iHK5tObqZF5QfccVm8WxB5-cX_caVSvQFAoGRIBhMLgsjSatKWRx2EQO-ThcXApOnKbAQZaCQ3kX38YWGt43px8EpaTRTKOkYCnClvEKuxm3ellfimem7xszRquDrl1IYCAKnMiXCCObyVhBxpbD_11dItYpdH5SV3PszcVjwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
؛ گستون ایدول خبرنگار مطرح آرژانتینی: با جرأت میتونم بگم که آلوارز در نهایت از اتلتیکومادرید جدا میشه. پیشنهاد پاری‌سن‌ژرمن بسیار بیشتر از بارسا هست اما آلوارز فقط و فقط به بارسا میره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90598" target="_blank">📅 10:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90597">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/458f4f6058.mp4?token=mB487PnWfTcNQVTglnqrKz1St_TLLd8uCEfMIY2hnltsXAcUuYKomzn1kG0p7k1iUrz87bJEDKX4RIFgAEQkXwJ7StRMEHN5LDWU3R0aMUNsvvb6als2Z9CilmSz21PPr3RTF4vLEZHCs5xEqdz8VEoLIEKQwBMBPen--gAldQZhghJ89QFhdCxkEAsk-2eiZQClQOdugnHVE-q0vYcRoq6PwaLFwOXIZP1zzqIH5MG5zz82DBuHMVlFpdHO8mpp6X_2SBMxNovkUu2FApElrcVrHl89WMP7jt7f4XMY0c4E6fhAmpCncq_Om4wk8e2-hUEs-AH4JpTYg4ZwLgGwFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/458f4f6058.mp4?token=mB487PnWfTcNQVTglnqrKz1St_TLLd8uCEfMIY2hnltsXAcUuYKomzn1kG0p7k1iUrz87bJEDKX4RIFgAEQkXwJ7StRMEHN5LDWU3R0aMUNsvvb6als2Z9CilmSz21PPr3RTF4vLEZHCs5xEqdz8VEoLIEKQwBMBPen--gAldQZhghJ89QFhdCxkEAsk-2eiZQClQOdugnHVE-q0vYcRoq6PwaLFwOXIZP1zzqIH5MG5zz82DBuHMVlFpdHO8mpp6X_2SBMxNovkUu2FApElrcVrHl89WMP7jt7f4XMY0c4E6fhAmpCncq_Om4wk8e2-hUEs-AH4JpTYg4ZwLgGwFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیکه علیرضا دبیر به پزشکیان بخاطر پوشیدن تیشرت
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90597" target="_blank">📅 10:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90596">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgEA6-fNoWEra3qdSIKTOXx5ysFOHrnnVkBDbUVJU_b3KliQw6gEIkTLB0QRF4sz_J2ippFxBNPsT51mx4uRgG3ax3Pwlh5b5GvdRgJZD6_rfEaJGElQbFI9vWf7v_Mzt9MAZ4ib1ZfL3PIf27PS7nRzSTjGgyRNIMdvgFuICfXQ2AcIdRBE0wFcB1zaksAurnd2O64DowKTEwBMOAhv2hLXmArsUtAIQngaiv-brUCdfC20uygK8JJf3Njjj5fW70kai64ArLp0pCyphQgblvq6EooqIA3mWpNpcBqznbKP4_wxEbgujfwv5aL4l2oD8SSAbn9oRYcGXPdIH3UjFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
تمام استادیوم‌های جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90596" target="_blank">📅 09:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90595">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHW7iHfcdf3puZV_L1Z9XQjZTW87MYA1XukIXRKVXDDoO0B_ibgWw1ZPQzzo6rlKwAfs-hoE-tK7r0dIvuLhdy7QgLlhMOJa6PRXe7LjmFXvNiEoanCS1R0hD4MVRWcPNMGDU524vkb6dxNoWuoTeEQeZImTuQQM7HhwqHm-G6WkaoPvbeDNQH9RAu5U_dlRKGR2LrMfy5LjSFGcfly1n6wuBHojL8q39gawA2b7Vp3vgrkjDsNdRgH9_eBcsZiZjGbbVk7jGZtt_qWao6aiRU346czBYYVueMZDLOKjRLG4DmXbIx2e_AQaZDFEOp1iPEJvneJajK7g0QrIEUuCLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ابراهیم‌کوناته‌ستاره خط‌دفاعی لیورپول از سوی صندوق سرمایه‌گذاری عربستان سعودی رقم بسیار نجومی‌پیشنهاد دریافت کرده تا به فوتبال این کشور ملحق شود!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90595" target="_blank">📅 09:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90594">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=d0SUcgpM5tt0G589LEY0TdumK_xekGmpSCIz2v2-yzM1wcaEQZA1XLfHoie5OV2ric5hLSFzuZttLXH9LoRa-XMwl-MEthDcn0eGVJ5EfmMFfBwZuKVY_vt7_yetO-hwIRZyct3S_jE2IIPt9wNxR9WMTMn0iWAEJFBMUgywABeAW8MzXcGs-KT5-WHBdJ4lz5f3znYFDFhooVJM98j4c2EXYxaGi5bUtp187CTdVotQSKL_ZWdDGO5ScdVGNyUUEnJf9mIulfF-Ffq7Nnj1IeDh3Bqt0oC8wck3FiMXUhoXE-nNpb0pHkDJZQSjgJGiMhZLoItBR7b68ZvrcBWyag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f927e35e14.mp4?token=d0SUcgpM5tt0G589LEY0TdumK_xekGmpSCIz2v2-yzM1wcaEQZA1XLfHoie5OV2ric5hLSFzuZttLXH9LoRa-XMwl-MEthDcn0eGVJ5EfmMFfBwZuKVY_vt7_yetO-hwIRZyct3S_jE2IIPt9wNxR9WMTMn0iWAEJFBMUgywABeAW8MzXcGs-KT5-WHBdJ4lz5f3znYFDFhooVJM98j4c2EXYxaGi5bUtp187CTdVotQSKL_ZWdDGO5ScdVGNyUUEnJf9mIulfF-Ffq7Nnj1IeDh3Bqt0oC8wck3FiMXUhoXE-nNpb0pHkDJZQSjgJGiMhZLoItBR7b68ZvrcBWyag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو رژه قهرمانی آرسنال بیشتر از جام لیگ برتر به کون هینکاپیه پرداختن
😂
😂
بن وایت میکروفن گرفته دستش داره اهنگ میخونه هینکااااپیه کونتو نشونمون بده
😂
😂
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90594" target="_blank">📅 08:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90593">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d9e66e04d.mp4?token=gAwie9r4zXbgk_ZzrYXu7RzxSVXedEgmT2h79HUtazvZzxoi3F9YI0UauCOLaDz-8VBAxKSus5ksQOBvbImiVyLUoGBKjePq1FrKaOvvehZj76H8l_UvPv8hLDxiopW1MFMBIUApV6d0H1LQ4T38fz_YLSzsEGg6_uh4QpX_gC72YOsYZhbeQTOfwe5DC4O4K8NCE7Fb20qXTsd7hXhYoW--sgqaHpK_PbJG8M_IE8xv2oCIFoswzMFpCjt7xJKbxdZAJ8wkhpDwExZyBrZ_Pd6fTDGFRMFJwSsBN8sji68npjbrfLAKaaU4DHhn2fIwpdb952CHnqRxfKmp98Wz8gkdFWpcvKHZgXeuuk1pw02ATDwG1nU4fxCYcSn-IaYTbKkyJnUpf1tWOidQtVEyznOIAdQKQZdR0YjfFn0Tyo7fHyjiibfq-wZAGsAKMd_bvWeqmoo9JF4M_Rl70tGoizkGzJmjxIbeuKJkI_zxcv-9auFq5PJDhU_N__oCU95OBtLlLCjFcNX16F-2L32epIaxAAUVjm0POwgWEQsnlWMGDTtuXqxSodSMno_t7xhkFvzlevbBGXd1qRX8LhVjsMcvOoaiLnjl84w93uZyxVm2Do4oJVES6_lrGAkMk_Ef66gWl5VHpwgpU677jWXmYapyFX9p3TsH6rPCRpHWnPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d9e66e04d.mp4?token=gAwie9r4zXbgk_ZzrYXu7RzxSVXedEgmT2h79HUtazvZzxoi3F9YI0UauCOLaDz-8VBAxKSus5ksQOBvbImiVyLUoGBKjePq1FrKaOvvehZj76H8l_UvPv8hLDxiopW1MFMBIUApV6d0H1LQ4T38fz_YLSzsEGg6_uh4QpX_gC72YOsYZhbeQTOfwe5DC4O4K8NCE7Fb20qXTsd7hXhYoW--sgqaHpK_PbJG8M_IE8xv2oCIFoswzMFpCjt7xJKbxdZAJ8wkhpDwExZyBrZ_Pd6fTDGFRMFJwSsBN8sji68npjbrfLAKaaU4DHhn2fIwpdb952CHnqRxfKmp98Wz8gkdFWpcvKHZgXeuuk1pw02ATDwG1nU4fxCYcSn-IaYTbKkyJnUpf1tWOidQtVEyznOIAdQKQZdR0YjfFn0Tyo7fHyjiibfq-wZAGsAKMd_bvWeqmoo9JF4M_Rl70tGoizkGzJmjxIbeuKJkI_zxcv-9auFq5PJDhU_N__oCU95OBtLlLCjFcNX16F-2L32epIaxAAUVjm0POwgWEQsnlWMGDTtuXqxSodSMno_t7xhkFvzlevbBGXd1qRX8LhVjsMcvOoaiLnjl84w93uZyxVm2Do4oJVES6_lrGAkMk_Ef66gWl5VHpwgpU677jWXmYapyFX9p3TsH6rPCRpHWnPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
وینیسیوس دیشب با این گل خودشو برای جام‌جهانی کاملا سرحال نشون داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90593" target="_blank">📅 08:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90592">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE1zZB9i7l0nyozlr7bt6cs0LUhkRKasalqegj1V00vB3TRuXB7uUnZGYUJ8Wfx6PoxsVx1WvkFl4u1_-6aEg2CLmwiebnj6995tUUW_v7pS3bLRu6rACBlbtS5X85fkcQYXhHJJDfzhRB2b5jdvtXbxGRkoqBuQ0e720XKVHvToIY892utOhZkWBTEqI-EBFedZa8lqmWRcj4wEVDTPRJ-TOPRCllQTnCLZXTDdPwp5ryXF-JqwW4PqhoSxFrQiBT1Y3_25DiH65hljJFwO8WXTznA-NXEW6_j7COIseGh6REj3GRYziGqB2qj065J-T_tHtJ5kr3X-y4RNz4BCPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وقتی همه چیز متوقف شده بود
پرداخت سود دلاری اطلس ادامه داشت .
📊
ربات هوشمند
اطلس
یک سیستم سرمایه‌گذاری مبتنی بر آربیتراژ در بازار کریپتو است که با استفاده از اختلاف قیمت صرافی‌ها، معاملات را به‌صورت خودکار اجرا می‌کند.
تمامی فرآیندها شامل اجرای معامله، ثبت گزارش و پرداخت سود به‌صورت سیستمی انجام می‌شود و کاربران می‌توانند سود روزانه خود را برداشت کنند .
🔹
بدون نیاز به دانش ترید
🔹
واریز و برداشت آنی
🔹
پشتیبانی ۲۴ ساعته
🔥
ورود به ربات و مشاهده :
👉
@AtlasSmartBot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/90592" target="_blank">📅 00:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90591">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
اگر همین الان توی سایت #وینرو عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر،…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90591" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90590">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2Afj2ms-F85dpOJWzfwrEf9pdumHUYvcKc-TzYlQZyetRJocMVwxIL8BZTM05n7-KSBpmNV_DVOFGVjEv-XCP6ZKFN4U8Ty8b571kdupYmJWzOs2WE2tZ1GGuPFAb6CX-bmA95KYwiO2A1STT8lCIkWmDiuKfdLwIcwsHrtU04qVSdAk5-cbM5qLK2t7M_n-2t2t3iCMVVRvtpg_xYSEr2EVMPpCT9ITDBwGZ61JQfyo4ZF4OD1ZRNCoLP1nzwN5tPG7WTTPl3AVoQb0o_0UJsPCOxwO8e6qebPklyB5kvgdH18sLrtsJWSpclBZsa1JJngfghGkSELPvbzqDvmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اگر همین الان توی سایت
#وینرو
عضو بشی
🤩
🤩
🤩
هزار تومان شارژ رایگان میگیری
❕
✅
من خودم عضو شدم بدون واریز ۵۰۰ تومان گرفتم باهاش فوتبال پیش بینی کردم پولم شد ۲ میلیون
❕
💚
خیلی راحت هم برداشت کردم کل پولم رو
💵
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
🔴
این فرصت محدود رو از دست ندید:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
a10
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90590" target="_blank">📅 00:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90589">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFdkNuPSV9ZJRjf7rlcPi08M6HxFATaNz_NErjUGp-0UmNF2Paf94sU0HqxwKgo_HBDrprb7mgQcS8c3UGqESKgWIJdLDbY9WyPOLJGL19TIM6WUMqOozJfmtx-I1KsoKxeoLp_KgWklN_4hGLSRcChiklwi4OHtdMNm2aw1ZKZz2Ogm-9sdfF-ebPNJoeQPTaleb6V_2Te8ku3hlZRhoEr6ao-gjlMjpACoBAboyPYlQlC4uJEjt_NgISrhfwGxuifO86IjP3oNdzk9LJjIZULVAvX0Bjwa64-KDgvbU_qS8tJ6OCL4IWyyk6EhPBZbu4VaeMGydXSr5B2-aRyGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید از اسطوره های فوتبال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90589" target="_blank">📅 23:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90588">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🎙️
مهدی تاج:
بازیکنان تیم ملی دنبال پاداش و حواله نیستن، هدفشون از صعود فقط شادی مردمه
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/90588" target="_blank">📅 23:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90586">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7K13bdcgZm7dhmNYLqlObHHZedXhcFhdEH98Ljvl-1P1N-UhbQODWFEPqI4B0QgmuZNGuULtn-y4OclNtoSIGhh29P6-I_MAesR3QktpLizFNCneZJl9nHVXlt59oh2dbcPDsPBpLHbpFD5nMRl6OiJF5ZWm7S9IqU34QJI3JhKfKFMzLAke4GkhOUupCvciHccQi2pnWcWXFiH9Bzoawnf9EbojATEsoNiWWP9QgrhUDBLJVITbaTJHxZkQ8u8VLXd8rSrM0a99x6bNtzXpF_LZ77TCXodDwDvFv9IB43JGQTGhSiMndAIFG-gKc94Iko1OhPhk_uphHvJD_IInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
ایندیکایلا :
آندونی ایرائولا سرمربی لیورپول شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90586" target="_blank">📅 22:53 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90585">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acjD5NnxlfDv1M-Dpz230srBYMdUjeB3NOut0FIuCHRz8MDyfrE7nzBGOyXIHPuMfxruzc8LZXeBMf6fIwoyVs4OxQpU5h_IpcElAgN8c12SuArjFFTxpRz3lFurzcL447wRcMz2TYE8CtcmJG-yCDY4ILZp3IAvDuGHobVOagY_rAGXseY4XgyjNrxedY_hX5GQNXK8KKqBHBJet6GEtfPNS1gqcdWSK4eSHiV9l03VOwKpoW1HTOdyNQ06FdS9ZlelmsD87pPIjJqaSlOQogyJWNyzwgqZ65MiowPXkj_5VJ8GlwSfUyBKRChyZYvVaXZPmTEqsx5Ta3A8dJnZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوورییییی
پدر آلوارز پیج باشگاه بارسلونا رو فالو کردددد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/90585" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90584">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahit9Ez0sEMqF1rSzASMDPUcMoGA5Ug8EKPrmIO8GXbzUKPnS__yVLSA9ugBhjZv0LgcQyGEc_0e_tuHcN9rVIo3O_3q60E-SXROrkGEhcxaKa0Wpbgc0vowl_R-FW91WZTXSXuS8RfiOdA0NR7PDMPpRuXWNcPK8Xk4miXvD0pR_GH5bwY2OWGK5rsXw4ZZvf_h8sXuLAiAxeZGnUyWQuwpuQRR3Nq8UcZLGD-X2bfLYSNtoz3Prb1TYMrzutK8ydc_P9zVqbKBYG5vxROiV6RKh-atSpo7DUz6f3w6UsWrphXJYfHnmpcnmc-rn30UcXmrMPq5rhyhrJgKDBY0Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
نروژ
🇳🇴
-
🇸🇪
سوئد
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
دوشنبه ساعت ۲۰:۳۰
🏟
ورزشگاه اولوال
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
سوئد در
۱۰
دیدار اخیر خود،
چهار
برد و
دو
تساوی کسب کرده و در
چهار
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳.۷
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر سوئد
۳.۴
گل در هر بازی بوده است.
🚨
نکاتی در مورد بازی‌های رودررو:
در ده تقابل اخیر دو تیم، نروژ موفق به کسب پیروزی در
چهار
دیدار شده‌ است،
پنج
بازی نیز با نتیجه تساوی به پایان رسیده و سوئد در
یک
دیدار پیروز شده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۲۷
🧠
تغییرِ مکررِ سقف روزانه، نشانه وضعیت ناسالم است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/90584" target="_blank">📅 22:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90582">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e5c0ed52.mp4?token=LmS8cq0Eh7E0ZzPpywET477FexEQ7iTWqwSAU3fijUKyJ105On5qPRHLSeidPq0UhokSa5AYZiaqPB1zVnJVKBxiUyNc3xSMXZhQwuKu8cR23H0AiJOshZp9L4mFZJC8j9BVWgFtFE1TSsSh8Os4VvW0f9cyZZtu_6BmaeYmiJvvVBaeUB3Bjqw6oYiZKshkZenVmcPPLx90s2QWuGS-RDJVDXeQu7byv_5GBykvIvAlAUCvaUcxARS4ahyDSj_AiXYOEgesJLJDK7dbWfxnw2YwZx3HN9sk-x-6fWk0UBBR-SCeZ62eyZwiLSkN151oLPH9YLsLjEuUCioGm_754g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e5c0ed52.mp4?token=LmS8cq0Eh7E0ZzPpywET477FexEQ7iTWqwSAU3fijUKyJ105On5qPRHLSeidPq0UhokSa5AYZiaqPB1zVnJVKBxiUyNc3xSMXZhQwuKu8cR23H0AiJOshZp9L4mFZJC8j9BVWgFtFE1TSsSh8Os4VvW0f9cyZZtu_6BmaeYmiJvvVBaeUB3Bjqw6oYiZKshkZenVmcPPLx90s2QWuGS-RDJVDXeQu7byv_5GBykvIvAlAUCvaUcxARS4ahyDSj_AiXYOEgesJLJDK7dbWfxnw2YwZx3HN9sk-x-6fWk0UBBR-SCeZ62eyZwiLSkN151oLPH9YLsLjEuUCioGm_754g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عثمون:
سال بعدم قهرمان میشیم هتریک میکنیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90582" target="_blank">📅 21:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90581">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpbjCw_kOuBF1x6x54dNpbU3sL-hyf16YkBGEM1FCysFL8NZwjBHYYj1NwcbjMhaxjkGD9gxxORZsSNXZr46X7bQDtVixI82H-uPZonw4AXa0DVaz0BB_ac4cEk3S52rcp5WuY9_1hN17Bkdji-TEGeIn4GpIVnzY1frBX0CjorTK6mmVTiDyoqPX6N-MBQ9PiKjpeu06u9GQrwEII5Yt_gjz2M2ZkjfHWpOP_DxDgXG2-59Kqq2YVRQ4XcapfmqR6aOfwNZ5ks-CMOZayt_ks25EBBj6YswAyT3qITnUzWV11DwPU4yshGS5B5TaumzVnr2EsP3YOp5k9uqWkhnxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و جای ژانا همچنان کنار انریکه خالیه...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/90581" target="_blank">📅 21:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90580">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f41d871c.mp4?token=v2mc8joIahpw7RkEE7yALgU6K8r3fmmpqq85JoDEcudILaAFzFK8w57NWOGX_4iEyNbgyKL-UnkXMuANmMZT4bR8wOT8tvus6Jfc-9zX57aW08aWlua3uWbYKuMfbxkppSHResUmgUMONSVoPHr3l9HtziXqlhqvtK132iZEPvm_hE2_7ZSlm1jyPVj3DmZ1McTYfnqsTj5u_C5xRh843yuy3ty6C2j1p0DhhZ0aASzjtiw4kRubLfQuCnMdkhiM3zbTLPuChzFoXx4jTQp2VXhFA2Y2AUY5KMSaJW-wwfgdRMQjwWJUFgYCKW3gpQNP8mVNu-AHOhaIRqoizUsVfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f41d871c.mp4?token=v2mc8joIahpw7RkEE7yALgU6K8r3fmmpqq85JoDEcudILaAFzFK8w57NWOGX_4iEyNbgyKL-UnkXMuANmMZT4bR8wOT8tvus6Jfc-9zX57aW08aWlua3uWbYKuMfbxkppSHResUmgUMONSVoPHr3l9HtziXqlhqvtK132iZEPvm_hE2_7ZSlm1jyPVj3DmZ1McTYfnqsTj5u_C5xRh843yuy3ty6C2j1p0DhhZ0aASzjtiw4kRubLfQuCnMdkhiM3zbTLPuChzFoXx4jTQp2VXhFA2Y2AUY5KMSaJW-wwfgdRMQjwWJUFgYCKW3gpQNP8mVNu-AHOhaIRqoizUsVfoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
پرایم‌گرت‌بیل واسه دوستانی که فراموش کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/90580" target="_blank">📅 20:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90579">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/870d923735.mp4?token=V0jq39Quo3g6RsIWauryZCVqpaRCs5Xg4jLVEod1JP9dhlmkLoFN1NoHNXlCF0pcafOqZwo2SA8cg1rnWSdk1rmsKtyr_GMZwX3YJnJriC8Jnljp34OMNuR20fMqu9uATh2KGWJnUUQfe36Gy5CIwwUl_xy7jAh7gQ0dMNmdinZeo5IINaBqwyjg_3HT4WqFqD3xPvLJT7RZUxUL6coidDu5NAcTDlArCdVMXQJm4tgCOBeOWQZWHlPBrS68vNS6RA86eJqTCflV4kyi_b52xDgnTpigkzAAAN0CzYYyMxl4yftprxbFJTRMgid6QOkv5oM26NOjqS4dOOysZYcQdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/870d923735.mp4?token=V0jq39Quo3g6RsIWauryZCVqpaRCs5Xg4jLVEod1JP9dhlmkLoFN1NoHNXlCF0pcafOqZwo2SA8cg1rnWSdk1rmsKtyr_GMZwX3YJnJriC8Jnljp34OMNuR20fMqu9uATh2KGWJnUUQfe36Gy5CIwwUl_xy7jAh7gQ0dMNmdinZeo5IINaBqwyjg_3HT4WqFqD3xPvLJT7RZUxUL6coidDu5NAcTDlArCdVMXQJm4tgCOBeOWQZWHlPBrS68vNS6RA86eJqTCflV4kyi_b52xDgnTpigkzAAAN0CzYYyMxl4yftprxbFJTRMgid6QOkv5oM26NOjqS4dOOysZYcQdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه صفحه هواداری اومده گفته که داوید رایا با این سطح هوش تو ضربات پنالتی نشون داد که اصلا‌ گلر خوبی نیست و قهرمان نشدن آرسنال هم یکی از دلایلش همین موضوعه!
این صحنه مربوط به یکی دیگر از دیدارهای آرسنال هست که تو ضربات پنالتی جناب داوید رایا قبل حرکت بازیکن برای زدن ضربه، شیرجه میزنه
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/90579" target="_blank">📅 20:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90578">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">امیر قلعه‌نویی:
چیزهایی که سه سال اخیر به دنبال آن‌ها بودیم، در بازی با گامبیا به آن‌ها رسیدیم. بازی با مالی هم محک بزرگی برای ما خواهد بود
😐
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90578" target="_blank">📅 20:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90575">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GI9haC5H38ZV0aGT6GL2u1w45COo9JB18RNA6YmPTrr6HRNNOBmepbVDSqvn7IDqLN08as-JRh2R5230Ae4JdLHOUWHPy58qgwcOX-w0FRE5F6qWeSZ9GGlCOibzWEnH9KYieEnYnQhxGKwqBue4krBHiqOm3ZBZEbGgGC3B5UOALU2hGSwke44bGrHaDea3POfmmkEYucxm3lRsgHRBRpGZoKlfdhrmTvmyD8sRhtLlL_yRpTXtkaG9rwU7-bqmNObYgskrAteCf9shYdVBEypnK295h5vJO9t_KrFmVscZ5eaolC4TTzjaq8Xc4GuUAVEW-EHSprxwZ6VFWlwYKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
در جدیدترین آپدیت تیم‌های برتر اروپایی، بایرن‌مونیخ همچنان صدره. پاری‌سن‌ژرمن به رده سوم اومده و بارسلونا جزو تیم‌های برتر نیست. در مقابل رئال‌مادرید تیم دومه!!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90575" target="_blank">📅 19:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90574">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
‼️
دیشب قبل بازی فینال یه هوادار یونایتد میاد یه آرسنالی رو اذیت می‌کنه که در ادامه ببینید چه بلایی سرش میاد
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90574" target="_blank">📅 19:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90573">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLpRfz3czAS364MAwgAJwVed7XIaKGUP4bITQjkXpRRjFpqM7heA9ukZxjWybe-1of3GsKI2b_MJe0EbIFPLaC-EVz-IwU18EHf9bhpALDVYahMaU_6_2kax1DnAcg_5I2TIYOInmVVBMkvTAdpaHr-Mk-YU4czAN6WepdY1oSosAj_KbEQE3C6T67H9pf5iHB_ujZhbaBX9WjMT7KCsLBguradv9H_gMJ6WefZHdZbdygVGs_t_TMKv4EDOUQYMge2x6ZeIiW7CfCfiLnwEzBJoTs5jOZFqdgn_IC9Cz6ulPpnzhaAD6dyuCOwI1Sv5WTlwdD_ni9UFGHuKjrfE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
کواراتسخلیا به‌عنوان بهترین بازیکن فصل لیگ‌قهرمانان انتخاب شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/90573" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90572">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">💩
⚠️
دیگه #فریب بونوس های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی #وینرو و با عضویت 500 هزار تومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io  کانال بونوس…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90572" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90571">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJ-cj9GhPiUz9IZYHicA5jYsOUw3kQ7H_5ZqpZ-Ta048ChAHpytDDfosBBD9JyHJXfVG0LdFDTK85kDvtdTufNp7L3ySaU3od_9zunHE-5HNx3O9EZ0MI05FZhZPlkH47wXIlfopg3sF4X0r_rkxcaqRBij6ZG63AGGlUfoM0TXP5YINzj7VYsvWFr0BRSn-DNsJxzQS8VgNbMez0pu6IxKEZpeuTUiEBJfo4OpVAprnb_0-VOZ_Hvl8H1gfRZL4AQviOoCfbWsOZJx-Hwid8LuGPh1WgZ5ofI2iG4gz3CbIlHwHiHxVMFbkZE022rc2RNBkmRIfNGNSS9VUDrgReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💩
⚠️
دیگه
#فریب
بونوس های الکی سایت های سودجو رو نخورید
❌
💲
بیا توی سایت مورد تایید ما یعنی
#وینرو
و با عضویت 500 هزار تومان اعتبار بی قیدو شرط بگیر
👏
🤩
با عضویت
🤩
🤩
🤩
هزار تومان اعتبار رایگان بگیر!
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g10
📱
@winro_io</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90571" target="_blank">📅 19:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90570">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
اتفاق عجیب در یکی از بازی‌های آمریکای جنوبی؛ یه بازیکن وسط بازی سکته ناقص میزنه که با خوش شانسی محض و اقدام سریع، جون سالم به در میبره
😕
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/90570" target="_blank">📅 19:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90569">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">کنفدراسیون آسیا با مجوز حرفه ای سپاهان موافقت نکرد و بدین ترتیب فدراسیون باید یک تیم دیگر رو انتخاب کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90569" target="_blank">📅 19:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90568">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2pc5PZBb_W1_ewvnwaw3GvapRE7zH4boaY6tHXkBzj2BTvi4hYDSMBq8U6ITdmDk6ybxa22M9WeFQ08IW-BCSOxnBRaJwJiLeHesz8x5HqYCc8x7FSIRZOWl9o4XhqzAFP_Jbk6nfBb1sFk8Rx18cwid4RHYRyksgCwOgSrFFNnFruFBv2Wm5tVhF2wLV3FN8vka0GRKTuLW7J0HWC7QrE9YNF5bCmkQVtxOAclfkpxrLoShm6EEdczdvMA9NvG9B8S1gT1gDy2z6XRFyis0Hm4o3Wygzbs1oGDnCMFmMkXLeKRK0yvBZZ394vrsQiSlFbzhfh1Z8R3oaO5Z7VluQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌ منتخب لیگ قهرمانان اروپا فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90568" target="_blank">📅 19:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90566">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fum_siNe7ipef4QzkG8z8VW8JGI0LNYBLcsi_vNQykzAOY8ChgaV2y2DP1JQnIHNJdDLlKfi-ceQI1gsQeNWiprBACYv0jdFfOoN9N7-HuWE7NHCMI4pGZu7PalvknckjmpTi4FO0s9CTQWBi0AF1cKZaqvxj5aBWOGlnNdHkXYLrWvSy0xANmaAJ02WMcD4Q5bdnqqllciMCWW6zVrMUWK_Zcy-d9yVcXrLgvc5npivkNk4xG81NZeynnVHwXtveOdFuMyQA0D-RkvcejxUtj_cXPnM8I7GW0qvF8-5tLEwqVel1y284pzq05MMz7V2hB4hX6YamZMkY4zzNQPPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حدود 1 میلیون نفر تو جشن قهرمانی آرسنال شرکت کردن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90566" target="_blank">📅 18:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90565">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c385efd6aa.mp4?token=oQPvQJcgJVOhgXuFoUrlSFnP4VO9Ry8yiRmJYRdTwkiTrjVX_kloIVdyJhv2NT6AApmy8yRwdae1NL9MJ-GQESAyXaphEOc7Mv4o2SqSJ3T97dGGJtasjFrampZKNy_hoovj8DVROj7TX8Kww0zXVbBYUdftqXfChsoAilATTMI8TPoOF_IhlCjPwoCFP975do83V1v6loY7Znb12ABNx66sItSt3vEpoLnT5OrFp9_Ulk5r6hewwb9vrQZBhAROYN1e-ecGNsK7F-OR3llKFF-_hWWl44aQgPFUEnOkNqNJRvajgqsl3L1RnPlaa252smvr4NcmQZafpLvYYkvlig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c385efd6aa.mp4?token=oQPvQJcgJVOhgXuFoUrlSFnP4VO9Ry8yiRmJYRdTwkiTrjVX_kloIVdyJhv2NT6AApmy8yRwdae1NL9MJ-GQESAyXaphEOc7Mv4o2SqSJ3T97dGGJtasjFrampZKNy_hoovj8DVROj7TX8Kww0zXVbBYUdftqXfChsoAilATTMI8TPoOF_IhlCjPwoCFP975do83V1v6loY7Znb12ABNx66sItSt3vEpoLnT5OrFp9_Ulk5r6hewwb9vrQZBhAROYN1e-ecGNsK7F-OR3llKFF-_hWWl44aQgPFUEnOkNqNJRvajgqsl3L1RnPlaa252smvr4NcmQZafpLvYYkvlig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست اکانت باشگاه الچه
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90565" target="_blank">📅 17:35 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90564">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTtPi1LGEO9rcORj8EMyO9t7odSmyvgPNpMVhX6xEkZoQHNwXpRisNVJihwpFVtJQKID3YGylmrSIrfjoY8SRsPVoDJ4gesjr7hnmypDELZ-m1H0wQBww6Rj8VXR6HO5okrymVqneGyusxSB0cDNodmqwZhbz1TF3SyV8bTDAnzFuVO7PSTdvv8vqmtjj-N0tM4DKad9JrEtuWszxq4BIndrIkfzBNHbK6q7QK1kLx0c4I7wmPWrPtUcZWl_gdujflqGqGUQANk6lVNy3Y394gM7G_QE-MIjkky1Q_thL09MIRfQDlMzjOtUiyAJdfOhpGQnlPql278olrbfvIUk1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بیشترین تاثیر گذاری تو لیگ قهرمانان این فصل
🇬🇪
کواراتسخلیا : 16 گل و پاس گل
🇬🇧
هری کین : 16 گل و پاس گل
🇫🇷
کیلیان امباپه 16 گل و پاس گل
🇦🇷
‌ خولیان آلوارز 14 گل و پاس گل
🇬🇧
آنتونی گوردون 12 گل و پاس گل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/90564" target="_blank">📅 17:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90563">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f90b184b2c.mp4?token=IiliLULFDMN0AVcTyqSFMO4BWXgoboQbXEw6VRQYC-0JRtcusG0Z2JfdYueyTM3tnLMih0tQ9vAZnCwgJ7dcxzXC735XIDpzfbc6-ye_QIQmwb3TcQWjggxgn6Zra5gVzf1nNYsa1ao1HxnPz-EZoIsuAHWO6tC4oP03CR22fJgXwY4S9r0Jaf9JJjvJ6JWPsyJXtNZwbN4-evEwIPug1pyKmCyfs6YDVHmZdmPc0LH32tAcRdQq8Fl1JThZK4NeUFX-o3xgmVQfl6e5z6g3QGhVPhi5RPXsTd45oWYMV4TY2_q5vYPUGTyoPGI2NKsIdItxcXRCYIQUQnBCoDK_1itNKVEbIx-STuK_mE6cjSCwpu-JmQ96YGZaBnMpOQAUFEk8C5KElRW5FYiT9eWHUHMi14wR6y9krb_9SD9DqL0ZSVQ2auV9VLAyvyekPrGSdS-LJwbX1uo6yKLgxiLSvnxDaZ-DS9XLWLO5dp9EOuBdz43OjB1dyudmYMR2X3zKUVpI3QYr5XrVLbEtrBID32NIOwPVFnK0yGj_fNuE8gX3qrU-CwSneZ-5OR7Uf6p0x_bgLMYBfPAjmju0a_8c4_ck1oij7zMZKAu7kw24gp3-pTODVgO1gCOUHeI1edHYj1qWSRa5OHVnkUpPR_K8k_D-5JN1Ah2FpI2NEAFEPMs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f90b184b2c.mp4?token=IiliLULFDMN0AVcTyqSFMO4BWXgoboQbXEw6VRQYC-0JRtcusG0Z2JfdYueyTM3tnLMih0tQ9vAZnCwgJ7dcxzXC735XIDpzfbc6-ye_QIQmwb3TcQWjggxgn6Zra5gVzf1nNYsa1ao1HxnPz-EZoIsuAHWO6tC4oP03CR22fJgXwY4S9r0Jaf9JJjvJ6JWPsyJXtNZwbN4-evEwIPug1pyKmCyfs6YDVHmZdmPc0LH32tAcRdQq8Fl1JThZK4NeUFX-o3xgmVQfl6e5z6g3QGhVPhi5RPXsTd45oWYMV4TY2_q5vYPUGTyoPGI2NKsIdItxcXRCYIQUQnBCoDK_1itNKVEbIx-STuK_mE6cjSCwpu-JmQ96YGZaBnMpOQAUFEk8C5KElRW5FYiT9eWHUHMi14wR6y9krb_9SD9DqL0ZSVQ2auV9VLAyvyekPrGSdS-LJwbX1uo6yKLgxiLSvnxDaZ-DS9XLWLO5dp9EOuBdz43OjB1dyudmYMR2X3zKUVpI3QYr5XrVLbEtrBID32NIOwPVFnK0yGj_fNuE8gX3qrU-CwSneZ-5OR7Uf6p0x_bgLMYBfPAjmju0a_8c4_ck1oij7zMZKAu7kw24gp3-pTODVgO1gCOUHeI1edHYj1qWSRa5OHVnkUpPR_K8k_D-5JN1Ah2FpI2NEAFEPMs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برزیل از همین الان یکی از مدعیای اصلی جام‌جهانیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90563" target="_blank">📅 17:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90562">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDPtmkA2h_gGuBd2brnJZxfwILLt_oEZWGPpj2pl3lljM7X0wQkbspP0gk2qzbgvY6EPh4yfVC3QaMDmUEUNmeDs-KfFYM00qM2jz3IUHCLNixST-jn1nr_Fq06UXUOdE9SyARVxnuzxWnER829XQyFgP_j2R2kg0qgl0A7msPgK0I3VWcFY3AEPtjQ0-JzOuejZOl2z5CPBR87_O5G30uSQXxTBDVMjzwODtQhIqXM4VLQUi0GKFMqrYXoQ8Jp34gQXzay7bvN3R8OBhLibsr_Wmm69XaT4qy4C4ZCoeccIboYfWH4-vZjaJTiO_0sHlpu5H8uNrORqWqM_t2CTXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نونو مندس ‌23 ساله با 19 قهرمانی
🔥
1 لیگ پرتغال
5 لیگ 1 فرانسه
1 سوپرجام اروپا
1 سوپرجام پرتغال
4 سوپرجام فرانسه
1 لیگ ملت‌های اروپا
2 جام حذفی فرانسه
2 لیگ قهرمانان اروپا
1 جام اتحادیه پرتغال
1 جام بین‌المللی فیفا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/90562" target="_blank">📅 16:01 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90561">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JseS_LlArIpYJu7QccXehACytX5jRippKbb9PBJ6GEg7gcW0dJlSq4KODfWyvNS41wS8EJeSPFLfmbR4LWP1Hvm5n4iQJuS1qelzjGrcv295UvwZqLznCCUSLvMZa70tEn9BjgOfYoiY_RRZ-qrtyQN0AOiUt1NqgX7L1iOG762Ix-zuswhAjzJXXbmA1Qpp1DRav83EKNwqUMhC-TssSJoolCrqvudZt1gdI5vpCLopUl6E-K8XcekJAUy73jIhDAeaNuRlITjkvGqDYqIfQ93QVbXofxWApV8vdPeJAoR5QAKSNpFaeZCOdgWs9fjOkzHKPaUraag6K6q1uv0Q4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🤯
🤯
فکتتتتت پشم‌ریزون اینکه ویلیام پاچو مدافع پاری‌سن‌ژرمن این‌فصل در اروپا هر ۱۷ تا مسابقه رو کامل و بدون تعویض شدن بازی کرده که یک رکورد خارق‌العاده حساب میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/90561" target="_blank">📅 14:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90560">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHNyGM6C5SipNrpzHzvPO0hhJ1uZc1gSZgMqpPYKNFFunZnohzNfWK114oqDMg9eslfnwqAKb30aio_Y928CLAkXBd0bmJxef1Jh__9g0RBjNeqNX1JHOwUK9cyXR1jG8cvmdY-asgE85eYSvVl_nIOqEeHvK5AvJTnG-ZmC4Q1_JYazzwvKfyyKanTPZwVaEQwfvu1rIZ8nYQoQCvP3TCLeG_r8-N91THkauHiTCC1Oafjv3eH6dEr4cEL1mAGtn_scykqxV8azcctrhscGk5sjOJ4eO1qDtrjDgqRKeWrtrLCs5-q088XxA-kmpjv8VwDBceJVeV4UGWO9YraJKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🇫🇷
وقتی صحبت از ثبات میشه؛ کافیه بدونین ترکیب اصلی تیم پاری‌سن‌ژرمن نسبت به فینال پارسال تنها یک تغییر داشت و اونم گلر بود. خلاصه که نون تو ثباته و ناصر خلاف خوب بعد چند سال فهمیده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90560" target="_blank">📅 14:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90559">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeJucb9Mm-fKu1EYaw78TqtcX9WkuytHpQvqn5ksUCRCvDpEdZH-RHRtYFEGL2gT8oEJ70aROkPynfmtk_T70T7-yb1C3miR1Br7_C735Uc1vNtEqGC-nxwmkYIigLNObowAiCP4a2bZbyvMIrTRIDBVVUC1L5WyqeKsMWEflcwjA95OIsqN_K00Cau41cWzQNhYJXaPjuwHucBU9K3OAVFE8kIvCU-w4OprQJI8_SMtDyI6Maol31cpxTRVMAuPIwKCNf_RMXXeJG89TTyVIUE0TD6mY-Ku8fKIuPfpdBlT2h03lwCpdH8C-eI2e-z5vm-nbL67ib6RWJeuIltbhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید صابر ابر بازیگر سینما
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/90559" target="_blank">📅 14:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbCLFyC9EJfWOzm7ut76Dwt7HfMkt5wrxer40Aun93qaRCc-0JmB_5Xa5BVx-kPtuxKYzYtmNFI3bdagx1zb9O-wOIF6LeGQdF9ffnxKMrvL5gQhfT4nHOaSYpwHV5H52ceiyuXeChY23nzatovxwtievMXCRjXiLk0cvxWuNxgTOSOLLoYH4_e85wXJYBaXibIWmqQEQ6HHzu7aHXYjD8PR2NwueNyNOu9tQ_MdcGeTA-WB5XOVSs2lsM3qsv-qK_bHIHi7L3mWZzl4hKP5IOgNJ7dbInORnZKu7f0c-PjCc5dQvKzitknCRUxrTyJRnhKDlkmvPZ2XVx9XpnpbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
‼️
کوارتسخلیا: بازیکنان آرسنال بویی از رقابت جوانمردانه نبرده بودن. اونا خیلی سعی کردن منو به بدترین شکل مصدوم کنن هرچند تا حدودی موفق بودن ولی درس خوبی بهشون دادیم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90558" target="_blank">📅 14:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyrsOp3nZRtQjVkqognphwBQApX34tcP2WDgXddkNxvrPACfQOCnBaGu_egckwD68KTUpZHzTp9Se-m2IePsGEcjkAFO00e6SmCEiJY3fm8aQGAvG85qzd3a9ouq9NR-beoFgNSbO58px3P-jGAvMguCerLFc3cSTnALpA10t9AvUTqqP_bT8QLELPuYrJr8WWYDy5eJ8fVDwTZDiQevVTtM6r_H9xeBuQs6muZmBUYeZNX8XAJuurleaTnRNGmVyiVRNRYj5A7rqHfvGK0qW6wJZQ2lW7xkI-OAQySFdJAPvYz-OC8BINY_8i7SW94gWU5p32KONSPiX6pHFL4HLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
وزیر کشور فرانسه: در‌ پی آشوب دیشب خیابانی در شهر پاریس، بیش از ۷۰۰ نفر بازداشت شده‌اند و حدود ۶۰ مامور پلیس شدیدا مجروح شده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/90557" target="_blank">📅 13:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90556">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgHz6gn12IyEEC4hRfVqoqYlruqpdzexEWGpVj5G1B9vnNJwq_f_GrgnbOvqU35KfNIV0I4Of93dQ8G3n-TGgOewDDC380hUlH9FWYmoW3-Ryp4VVMb8rnvir2RvsgAuRbsmn-2RxevWOdAKbl7mjhKVq_daCa15vBMP0wftywpBtJwWzdCCavAu1wck0dek0jSxOsGwh5so3693rGuRFK5Uhi-RR5c-Q1MVH4Voh4o0x0AinGaUsYpP5nkk2fwAHSbP08vB5Bgr3kfzgnL_mseXDhPTRhB8PDcW8CYgGMpsD1GKY95V218FBD6pWZN4xWFsqxo9e5pJojx4ckWa_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
وضعیت وینیسیوس و دمبله با و‌ بدون امباپه:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/90556" target="_blank">📅 13:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90555">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKXXQbSmc8lz9KqDcj1Riwxv1oWfAINpLmRKvIDNjTDm7KNToG_YITGGIoZIOrGWqp_obUzcIWb_iXyljVfUPU72Q1gC38szVsBvUAa-TKUjIfeA1QHhgzBvV6J3OOb_qn01zER4u1KV7snlOGFmo4J89_6606xhOfvcuYLZPT21fpjdandBI9ftr8Jql5lOFnbQU1jmDoT4ySAOhcPyDDwuhA_GqFgMoV7uUAGx6oU4XGLbwNeXtsn5gqaiqgB41FB6D-MZs1fL64wHJnsr1_CkQBWqdRcwh4OtS8khYpDpW5pUWsTC-CxJHc1JcQg1WfyF_byDKfYWc0WFzUsKEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مونیرالحدادی بازیکن استقلال و همسرش در تعطیلات
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/90555" target="_blank">📅 13:21 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
