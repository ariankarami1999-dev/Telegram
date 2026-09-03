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
<img src="https://cdn4.telesco.pe/file/qfCx6nJAYKZruNdT-eLoGwGfPj3bJg64BJNDx4Gx9I0d5Iwhj9vCHY7YTZX187aQtcaRqthj8mwIgDUNDUyvYpKa9AEm8kp4OAO47J9ZJn3uaDMgxQ-Nxwyz64f_ueSRRA1EGaZYW82y2wPKI4jmA6XPfI-gB_HBeXjZnGftrglMYf9qeMLQsbbW3pIw3X4DDt4VaaA1TsOPoZ4JfCmtl4POZtWVnGN8w0kV7mqvhaxlyF5V01e6ycXV9V3iGvaCW3hO6OPMYxJExD5HsZEUOEo3ejt1hroIdNH6FJ2M5PB9fIQZ8MoRjSRtZD0jELFE9Ax9fbhpPf7q6rSFidr7mw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 618K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 12:48:51</div>
<hr>

<div class="tg-post" id="msg-28970">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKYv7-JG2CD6Q_qo7Z6Pb7oTXUkGNf3WSCtwx5ZtewzaTxjOAHNiLr0POFTvL8-SgHi7-NBiMpKgy4AWLpBOODDSIghVC-kfdFNhdtqt2VID66ntBDQ7f9mbzdpQJCa2mhf0EoY63xzTsjlMYZzQtyinEU01JdC9pY-TR-5RXs4tYzIfrXmRf_JITFXGnzmFN0YZlmlqJLwf5K2J8rxsSkpoBOmNgmmferh8inNxH54iqnLzH9cr9EHTPHWbRqMeSEIYMaI59yDr8RTlq2QxcxwqHgrIMC5a2-a0h86o4GMKw-3JSzEMf7Q8gV38ZvCm0JEndOjQiQmB7RCFNJSTOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
ویدیویی زببا به مناسبت خداحافظی لیونل مسی فوق‌ستاره39ساله آرژانتین از مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/28970" target="_blank">📅 12:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28969">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=biQo1CBzEyD1eiHg_9XLRK8kIWoyapqvvkS6zXHR6vm0OAlbL3ID7Ts1VqLXlYA1cbYiFqC8uML6oq0d1Nh9uBOSYWbVoRf5rjdvuwVDosbqJJ97ETvWSJGeHBUyiR2LxJfwITWA-U7vq0gpHiU2g90nwEAqXr_jciQv7KhGVzQWEj-nAqhTzvIsYlGB0f2RV0KSwOYmdoLOjaAHIc3A9NP2oBJ-PQnk3STXTV9zPv3Ti6JqQuoN8hCyLvmWNZ0O_c6N7ie7pqVQAQFpGJj9n5YbvqcNP-lyZPhvb8fV_tdKTtbw8tk5r51nfoKr0gYnJMfklyrY5geChP4XwoWfZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4732ab1f.mp4?token=biQo1CBzEyD1eiHg_9XLRK8kIWoyapqvvkS6zXHR6vm0OAlbL3ID7Ts1VqLXlYA1cbYiFqC8uML6oq0d1Nh9uBOSYWbVoRf5rjdvuwVDosbqJJ97ETvWSJGeHBUyiR2LxJfwITWA-U7vq0gpHiU2g90nwEAqXr_jciQv7KhGVzQWEj-nAqhTzvIsYlGB0f2RV0KSwOYmdoLOjaAHIc3A9NP2oBJ-PQnk3STXTV9zPv3Ti6JqQuoN8hCyLvmWNZ0O_c6N7ie7pqVQAQFpGJj9n5YbvqcNP-lyZPhvb8fV_tdKTtbw8tk5r51nfoKr0gYnJMfklyrY5geChP4XwoWfZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قهرمانی ارزشمند و شیرین کیانوش رستمی وزنه بردار ایرانی که عده‌ای نذاشتن برای ایران وزنه بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/28969" target="_blank">📅 12:28 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28968">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=Z5pV66KoEtbEvvl6tU5Y9Ye4zeXzFE1IL8jGAWpvlCSq-GWXhToTewYiz5XrMiRz-_yMTeEoF7vrJeCpRE-MZZkWYKzK_iNtoghenyuUenrx27v2VrxV4zoPtM0y5c29e9moD9kOQ09xaU4LMIpYfnM0XXzs3KkovlcAVuZih7HmjZeX4a9yMcs7PFig14_o4zRpKjwjczRn4Ftz_hZKDg4itwKasJfaS0OO0Mik9gerU-O6kN5OEOnq70_9fyP79QAUMYzWZVHyK_0l2e7OrGBdzJK9wocGM0P40PiE2rGHIFBa-cf1oGloomeld485aP7IpSsc5sN2MpkFmShBI7UYh7MRsg-MkwHrEwZY2lw7NHbl7GK8zT-PaN6GAo2vQ7ts88OeA3SApV5x8vnCznZdogor01A8y6OV-q7J-xflTIzZOhrC1ctM4XgebxER8RGbDBeF0j8zB8Y7AUWuxwOfEdMPb2QgEF7vCg4FlzJuoB6I9YMLBWf2dDCttnaevJft9WZPiQ61L1ckeMU1sVt3pFpBiTT3KD8T7Ecp82e25YJihI3FOlb8cO6A-bkEZkm-lykQV7qsQ4saf34bdvE3T-pnV1e0VcebkWeOP4o0Vsby4n4PZxsGdgogO9Qvc-ssZYqEbum28X10yZmxy9j-bddUNQlWrXoTaRzGcxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd1ba5efd.mp4?token=Z5pV66KoEtbEvvl6tU5Y9Ye4zeXzFE1IL8jGAWpvlCSq-GWXhToTewYiz5XrMiRz-_yMTeEoF7vrJeCpRE-MZZkWYKzK_iNtoghenyuUenrx27v2VrxV4zoPtM0y5c29e9moD9kOQ09xaU4LMIpYfnM0XXzs3KkovlcAVuZih7HmjZeX4a9yMcs7PFig14_o4zRpKjwjczRn4Ftz_hZKDg4itwKasJfaS0OO0Mik9gerU-O6kN5OEOnq70_9fyP79QAUMYzWZVHyK_0l2e7OrGBdzJK9wocGM0P40PiE2rGHIFBa-cf1oGloomeld485aP7IpSsc5sN2MpkFmShBI7UYh7MRsg-MkwHrEwZY2lw7NHbl7GK8zT-PaN6GAo2vQ7ts88OeA3SApV5x8vnCznZdogor01A8y6OV-q7J-xflTIzZOhrC1ctM4XgebxER8RGbDBeF0j8zB8Y7AUWuxwOfEdMPb2QgEF7vCg4FlzJuoB6I9YMLBWf2dDCttnaevJft9WZPiQ61L1ckeMU1sVt3pFpBiTT3KD8T7Ecp82e25YJihI3FOlb8cO6A-bkEZkm-lykQV7qsQ4saf34bdvE3T-pnV1e0VcebkWeOP4o0Vsby4n4PZxsGdgogO9Qvc-ssZYqEbum28X10yZmxy9j-bddUNQlWrXoTaRzGcxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تمام موقعیت‌های خطرناک دیدار دیروز استقلال و پرسپولیس در هفته پنجم در کمتر از یک دقیقه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/28968" target="_blank">📅 12:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28966">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvMtjZPPkwTq8_VCJ7sRnmcx0ogGK6VhTJ5O7k7eHQD_dd3SaVRRKYB9BgieliuRgkhukxnIfRc3zdV7eLX1dnAxaMFm6fiZyoX2e9B1T5RaImMk12GLVGhHJcmWLrAk00bBHX56hRRng7bhwx_MWmKaE_m7sOgOvrQOxk5txAm9q5doWRrKpiEjZByu2ZLhrFmvfoNJ4qLtw6yLOfIpUI_legcXi55p8zbsM5QBwf7q1i4EgI9kVYseOX_bMJkiQfTLvaMEqd0adSfzy7BnwjiPuHdkBK-f_XiewoUfQRFxPKKDjsW38kWOUdgVIC4gQpYSxVIYH2fIOz834KGaxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#فکت؛ 3107 روز بدون شکست در جریان بازی در دربی؛ پرسپولیس آخرین بار اسفند ۱۳۹۶ در دربی شکست‌خورد و از این‌بازی.تاحالا ۱۹ شهرآورد متوالی بدون باخت درجریان‌بازی‌را پشت سر گذاشته است.
‼️
سال1396:قیمت‌دلار 4500 بود، طلاگرمی 140 هزار بود، کرونایی‌وجودنداشت، پراید…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/28966" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28965">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUnp6zNZsCOnob6ZUmqQ48vxUEULBKUWaB22FQdZhdZEZ8GYRhkyLINqTH3jk6LljMxEKkyT-lesEBltbg2CaeHKAd5MuNIn_sHh0IM_icuJk_sZYqMdk6Kd8w5xU8BLffd2qj3CofuFnSTITEwFEkdpJ5JTsTYPHAuD8vVnJsGPM53D-lhCQGbYtv_ukCQ_YHWAlKHZdUsXOH7Jwr46CXDuq11Wf6qV4We8wky36F9FQ98Z_aPALZNsWVE3GEIdUWbIBnABv3kIVKSgZcWuwDI0Vt2oOZXDVHq3LhtvuhZ79K9Dx6kgBS7-7Tf9BIWSGGGlvU8KRuXQCZ5QNrQEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/28965" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28964">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StBRRFlGmeQMGIUYCoL2w4wxOVOIkOJjBFZX-fJCiiBq1GV-jgym2Lf0XkpdHPwTknM6cB3iB7k_1DBh_brVzEhaK2px1nKKp5GynAT7MiSVHh5PjRFvAUI3a-Zsx9exz8gF0vgR8jjv3BpbE60mAACsp4XxSv4heFefzbVPPwczPkRE7GNEKVEWHsQ6L-xPGpYawsz62lp7JJIn1177euBffiJfxZMatRQETGRnh2opyBywY62ssLjH0x8RbiCpBKm80F-IL0rZQQUTkOsYYUT6r1IvqBRrSGw1cdDNlLdCZvO5iY3YQ4-WNlolr5F7CzFOQEGpZk1xYrdaZifZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/28964" target="_blank">📅 11:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28963">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d582283b.mp4?token=s8jieAjWHjpZ2-tTXLl2L5YnhYJwLmPz-nan8fPIHYEiSbyvCnOn2LVKpy-Sk7YiW79wUiIn5ul01O2mSnG4ANHejg-EuFP1gJOSbOUppvV2jt-knBnTuv0df-QtjP1OihxT5kDMofUQHcSnoS3q4CbWSvZ659Lw2HDIlICJikKSOygjsVMeYiyj0cn3z2sn_s0bbe4p826MALYDC6E8GAuOfxKhif4F-m6iBM8aHgPfABapXKTJjx3_hvlriVr3DpFqd5q4fMpw51vrS1vaop30n2Z9WEcxltvtcV5O5IcnzPtg9XzHj-zdEmUZoylR84Wwf-aKxQ8US4zwapDzSxdaHZ8WFMWh_F_I6XkmtsHKwHHjjZZfvdQ6XPX9UQRWaXnBHJwpdCVLyJEok3soWUmz9gU27YqpWeMaXMyckBC8NOjA1xnrLDF5MUaysJZlsc5QIQQ3utBdbfptPsTpvntwjoLoQ1mFB7FrpxAih2oTWhvvXyvshUxmGegYCaYDbub-W7w1fHstIW8qHihKqUCx42UiakQxQ7QyCf5YstTa2XtUXmfxyjgcG4UzTzw4VGfej4iAV4RD-t7Es5pnf88IVxfkCaLbJrBETs1punO4RiNo-D_AJ7Aer_yWB9q1qnA2nsqVtUTpdH0YbwlXF2kco5SUM1tIBuzgEOmH_uU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d582283b.mp4?token=s8jieAjWHjpZ2-tTXLl2L5YnhYJwLmPz-nan8fPIHYEiSbyvCnOn2LVKpy-Sk7YiW79wUiIn5ul01O2mSnG4ANHejg-EuFP1gJOSbOUppvV2jt-knBnTuv0df-QtjP1OihxT5kDMofUQHcSnoS3q4CbWSvZ659Lw2HDIlICJikKSOygjsVMeYiyj0cn3z2sn_s0bbe4p826MALYDC6E8GAuOfxKhif4F-m6iBM8aHgPfABapXKTJjx3_hvlriVr3DpFqd5q4fMpw51vrS1vaop30n2Z9WEcxltvtcV5O5IcnzPtg9XzHj-zdEmUZoylR84Wwf-aKxQ8US4zwapDzSxdaHZ8WFMWh_F_I6XkmtsHKwHHjjZZfvdQ6XPX9UQRWaXnBHJwpdCVLyJEok3soWUmz9gU27YqpWeMaXMyckBC8NOjA1xnrLDF5MUaysJZlsc5QIQQ3utBdbfptPsTpvntwjoLoQ1mFB7FrpxAih2oTWhvvXyvshUxmGegYCaYDbub-W7w1fHstIW8qHihKqUCx42UiakQxQ7QyCf5YstTa2XtUXmfxyjgcG4UzTzw4VGfej4iAV4RD-t7Es5pnf88IVxfkCaLbJrBETs1punO4RiNo-D_AJ7Aer_yWB9q1qnA2nsqVtUTpdH0YbwlXF2kco5SUM1tIBuzgEOmH_uU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇭🇷
لوکامودریچ:
رئال‌مادرید خونه منه و دوست دارم یه روز برگردم اما نه اینکه فقط برگردم تا اونجا باشم دوست دارم روزی برگردم که بتونم مفید باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/28963" target="_blank">📅 11:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28962">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVDbQ4QckgfWRW_-VpDwJR8zsCdujS299DczKtj3pq0wU6yMotWvz390Lyh_55cBzj_gYJQsj17jeELQfcKwCCxkU6_6aAVqP9K4mcDg-A1U8etvCqDjDQSgjZijjeBtDRoSEQY2UybE1enbqA4nCt8OXX5hGX9hUI2RVZLs7AK6cZAB7LZZtGNTMLkexePz7DSMHidfbxn5DoszKu4EWYQpr2tP_O88-J2jQj517_cmh-Y1SUe_RFDhwoJdJ1KIBTiCTauAz6EauK5xJNquIn2TG0v4-X-ZzpDNWh8wq9R2exM2Q4U4YCRDVhEJ6SoTyvLqFpMJJp9t-rrFFUqglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم منتخب بازیکنانی که در حال حاضر بازیکن آزادند و با هیچ تیمی فعلا قرارداد امضا نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/28962" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28961">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YnJwzC5Y_UyGSY7lpIbQuoHaQYAjqMBBdghr9aikHOwpSjXx0t84AsWUn1-pFvMEEOfQY2BameXjwoWmZqcdbobUlqVdR0ohMd5I-FFNqVHZ0DLf61QpsnpC-YnJrseQsfI1iTr3UIXqvwcUimhrGguhM0jZrRN4g0xmR1NyDNJqn9TRvwY60gDY1Uhq2R29-j8gD9d5nEYq6GkjtwQAUsdi_1nqKkw9tQWsIwo2GZQwBkFbUw2vMSY9TBMZmik0PaH1XIK8YPe0cxVcd7jrfv20mLVWjTuLzpOl4isHfRezzveT9DQwIKPXWCyUm3pUWAqi5LR5pEy1TO6qYJCxhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌برگ‌ریزون‌لپاریسین:پلیس‌یه‌فرد ۱۸ ساله رو که عضو باند آدم ربایی‌بود دستگیر کرده چون در حال نقشه کشیدن باچندنفر دیگه برای دزدیدن امباپه بودن تا اعضای بدنشو به بالاترین قیمت بفروشن:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/28961" target="_blank">📅 10:44 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28960">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOcGOP5tcNDx23JZo4j5p4hFGZWsXEr6Js76BlnejWI1U6xbaYxblHBBsGLyuLo5k7WHO93GiB4rnu10u19a5c2UpP0zP0isrChSIqb_BPbNgqX7JPNdP4e6UqHcrXqWVOkO3_dXW5ufERB_yECEMWSx1wVPkguC7xJyKVmRDJ6gnZFV92wVLpveOd5AgkaKXHxp2ZW85o8gGhlS9v8sVPnAqEOuWVpm5rCkjX5HHf4IapIsBhHOk3Qsl8BFr3xjIAtrEaDjN9xP1a91NOPVPTmsY8Rb48zeEjO0PDDkzLLX9AoW4jO9Hzhr1_y7gOalWsxQ9LXISMoyRB6HEb_Vqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
👤
بااعلام‌رسمی‌ فدراسیون‌فوتبال غنا؛
قرارداد کارلوس‌کی‌روش تاپایان‌جام‌جهانی 2030 تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/28960" target="_blank">📅 10:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28959">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ptk8mfMcJaQSH7SF5CuRY4w2PVmmlJDAfwMQhNLe3McgIbegOcRA_N052jRDqw22YJvKoTzxXk75COVwthmbgzUaHto74qf73oRKjCGVG0oZVevsgxzTRKYpe91-EW4f8Ug7-Im87aaHRpzX1OHuPDZ9GgDTfsrDb4pk2HX6ZVnLJZB1JexAJ9B9hfP3OxL5TlhaCRA4PgJ0mqYlY9_wxH_eCFlFMiH8RQjZSii5EKiYXhQ6xU3zwtlO6FUrQiNghesFO77qzeLIvfBP57mts5FTGXQA20ieTqEXyS3p-a35Nv64ILHit_HAVRKGv5IXSyX3d9tuUKVtFGbKN3MYZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/28959" target="_blank">📅 10:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28958">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMXGO7sAIu-m_ZoRYgS8y0esSAegi4gpr4cET7k4-tdO5YKeo7sn7jciItSMmMzD9Ks7gTMJShAcVaYIwXKXQDA5aIvm3Zh_VvvaQWzn1GHHLc-hmxB0Y2ZLN26PvRfJSAdsuGPWEO_hMTWwwaqciOFi9H4ZKaXFY2nPT16D6n5PnPrt-GSkuc2Pj4cyz7y_yBxSlOSdh_2OR-dpls8R1i35bN54z6cZnxr_NPSuIYgc5GGEyBt2KIFjlROjB2B2OmUiRVeo3zEltW3gSg6eCsQTZ_jFU0d7OzCqBAapr-9BS4Gcsls-O8rNCE54EJeo9AQRMppUR7D0cuMyE3EtHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
کامنت‌منیر الحدادی‌برای یاسر آسانی پس از دربی:
«به تو گفته بودم که تو دربی گل می‌زنی
.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/persiana_Soccer/28958" target="_blank">📅 10:17 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28957">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHYub4oOmsQ9Tu1uislo6IBt67rFVzqCVZ761QT5ZFb5XprbuMDd7oCM-tQS9uamIwomKMxr62gC4Z3PXhj0ifwNKkT2moOZo8CrFHP4K7dkjV-ikc3uvz258S9VykcNPl-SE8vJ2XYvn6DkgNPj9y6_zDh0q94OcdWmI_OIoIznFznNlKjBqO0G9mEh0YHN5Kbpw-yKRnmuB3zLE-VgAYjM1tINh3E4-wt8PJ22TlVreg7oj2XLofHhnoRrBA2A2vwNRlnsEc71bh6YZX6mbmr-1wmY94rH4cCZlB9sa_LdlVDtYLlWBdGKWTXGNigY3LlikdvBB18_mLm8E-YLAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/28957" target="_blank">📅 01:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28956">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVggffYqmowiUhrXCGQC-DKdtOjFP16ons8gvNLDbDo6zadsJpRA_W0LnXOhk6oktKAO_1ZYB0s0jn1RuAf2lmW1TdxMELNep6bKDvUrkFfQjQ_vatec9tZkMXjeRCkqjWQEY-17W96IKJ94dG9ffQR5DUm9aDADFxq64YFq3rEJuQpsBK5m9nwA8RDW4wA_B0ff6QAttmanUcOc-D30XhkwtVM9ohv7grWr6UgP6650UFtuLMkYCRo827PDWkyrCV7It3BuLchwTq_b0sqaG85B9ELJT8D_71LUP5FzlMYTYaXOyIIqEZVGSUkGNEDNlxdHtGU1YueGoV1cbswEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
#تکمیلی؛ جواهر ایرانی بابندفسخ 2 میلیون یورویی راهی فوتبال پرتغال شد؛ رونمایی بزودی.
‼️
همانطورکه بارها اعلام کردیم باشگاه ماخاچ قلعه قصد داره به هرشکلی‌که شده محمد جواد حسین نژاد رو بفروشه و حسین نژاد اعلام کرده بود که حداقل تا نیم فصل به لیگ‌برترنخواهد…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/28956" target="_blank">📅 01:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28954">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy4o4NgxKy8RLSc4tX8s4erVoJfZO-4xuo7bsbR3f52xafhiaSBzc4p6GOvzMI_wbPaaFl5Xk7khCayPgyQejckn_PDKiGNP_6nML6vj8i31NrNa5FiyAE1zhpoPbxE2t4g6LXE9KfQD98OTMI-dm7aMbX2qnH9GNNljMZT_mwhPSxCgHc_ZprJBdWrxQvk3DGdScwPTi4U90uxkdZI4FOZDEvzTPqEPObLeRyxe3JAPdfx75wmYPU3-8zxIZeIrcxsjqVyvijawLMzYEmUgOLkJXQgS2lGUQFjdMgTYdRtUSUBBww-D1E-XzUanb1TJnKj6qoxzcAb_A0S2htybPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛آخرین‌دیدارهفته پنجم لیگ و شانس صدرنشینی یاران صیادمنش در لهستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/28954" target="_blank">📅 00:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28953">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwnWSdUl70tFw04STmRNvYgqLcSIs1jnpzSbXAf6oECz0rhxbOllL9Nwp3E91q6mhA3yqVlQMG5ztICYkLbFxhNGmXBGWk4mbx4NSQ6AL9kX17USzUIk8j2teehtu55iAWU94CLJtWZu3-htsodFRsI22Te3-OhJLLIJWLmSZExhi5z0YNahLz9xMFGs_hTWcTBMPyE8EFip7vFCl0CeBVwue7Jb76E3ZRrOZ8NrVGFwW4vpauzPdG4C8dsUJThzXsFfbMINXCJrwg58_x8U4gUAJVrHkp7SdQvO_4TvmXJqyLrJ3R1ujEuRGqNWmj0knxdRQk5Z3jbEFldKN2TzVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌ دیروز؛
تقسیم امتیازات در دربی و صعود بی‌دردسر باواریایی‌ها درشب دبل هری کین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/28953" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28952">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b6gIeHfutL3M2ThrTUN9OfTzpzuK0YQ-8ZVbp_A2_mNKUd71KHTF4pE1FcBqQGbE6ThcdyJ7HrIm40gK3-V1CQUpaqBFnwYB4-WuvmLjvo_3fcyXR6Jpp7tsbYdHVp9wZ-v2ROUUynmwX9qh98rYPRjIl2T3NKbOsE8PL2Lz0Uh8Hc6mGa-oZXBjJPLjMvxLQ-Y8_W1quAy2CR49VeFRlMWS4YpwO4jAXdBjNoRjQEOEd7-78BJkrDftnkRZ2M7gciwcI-0KXMTxw2nrJKTYrJVBqKslEiQSQDlZ0LO5Y7LWTFXDD9SQx-0MmpFL7XLMuk-KFHPNUuRf_ibfVZu1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین‌مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/28952" target="_blank">📅 00:56 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28951">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UMeCeHxjUFOEBOrFTgB1J45cCdeSWo9cTa7KcKMJyL0CK0WP5APxPf9qykWTakWQateY8esMcxH4RbT3qKC_tM6EtftMp_3gq7g3nMddSI4N9N98T5zH0dQ73TEBhyk3n2PH0YjzRTgqPGXPaTP_wR8io9MGw358AFqE6-kbaKBH7H3cJDrZkS13Prn9aTbbq5N0ilm8rRvHPEO77uLknXA0ERk5W2H8NJ58fTetyi_6KZRB4pRspsD3s8lFx949uD3Agl-owFp-WRsWHX2a5ReKnspoR9o7MI6T88XQy-5n_dqP9VrE9FjrUqDwzVjVwa2o7lQQofot7M-0ZrdlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/28951" target="_blank">📅 00:27 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28950">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwWdvw3104k1bbTkIUYF_msaKW9c0GEd9xcy-cli9wQaWNiYuBZR_Zu07X0beWVDkAIX4ZwPBXcZimzBEqE1Tx7K5XWbqj_BqTSW4jY6THOslEmifu-q5r6053ePoP6v5pVJSMceshY_tKCdfHUHK_NNLzMuecIJxA4mwhJyXxXbNNnc9SkIwAf9tCCdxf0LM7nfc7M9hp_rxtIhtawN8cy-qje-d0Z4U4JGVNFdMQMJQTN7FvvOIOgmw05UmWbtFj81ZOhANFRo3guCHa398F78IKW0uGkii1VWFTjtDYGW9Da2Hk1axwhDV_bge6QT0sbQELRBoW2MREmvt9YuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علاوه‌براینکه محمدحسین‌صادقی وینگر 21 ساله تیم پرسپولیس ازلیست‌ سرخپوشان خط خورد. دنیل گرا مدافع‌راست‌مجارستانی نیز از لیست کنار گذاشته شد. همینجوری‌پیش‌بره یه سهمیه‌خارجی سرخپوشان برای فصل آینده رقابت های لیگ خواهد سوخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28950" target="_blank">📅 00:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28949">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=slVNa96Ym1CUAEX6FyiFTSysFmHlhrR8LlmehrLtriLnK6UqHFaOxNv4g6CDLTVaCjKZ69lmG5vPWWDcvWhEX1Y_8y5bbEhRoIaNDO_gM_gCwxgWFQizqXFqkeNlXOYGfGcZ57W_NK6OTMzo97wyQXu3j6mo_RPtJZn9dpRixmdBMuMYA3gpxHWJ4szL3D59ffWvB1yZJeq5u0Gdb6rTzgan1ua_fEGYnv-D1W-cBeOGsO1AUfUROuVERmh5wxmkjLvCmQ8dLzJvk3TYR3jQLAaf0eNNuNoT4t3RClpnnk9deo87_3QNRwEMbkCAh9b4mYSGN87KE5MPGefvL_Lnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3296c641d.mp4?token=slVNa96Ym1CUAEX6FyiFTSysFmHlhrR8LlmehrLtriLnK6UqHFaOxNv4g6CDLTVaCjKZ69lmG5vPWWDcvWhEX1Y_8y5bbEhRoIaNDO_gM_gCwxgWFQizqXFqkeNlXOYGfGcZ57W_NK6OTMzo97wyQXu3j6mo_RPtJZn9dpRixmdBMuMYA3gpxHWJ4szL3D59ffWvB1yZJeq5u0Gdb6rTzgan1ua_fEGYnv-D1W-cBeOGsO1AUfUROuVERmh5wxmkjLvCmQ8dLzJvk3TYR3jQLAaf0eNNuNoT4t3RClpnnk9deo87_3QNRwEMbkCAh9b4mYSGN87KE5MPGefvL_Lnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری جنجالی از بازی امروز پرسپولیس و استقلال در گیرس عجیب بازیکنان دو تیم که منجر که خونریزی گردن عارف آقاسی مدافع آبی‌ها شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/28949" target="_blank">📅 00:03 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JpJ2FWG6u3jokEI9p7VzC8QPYiM4hOs-vRbGV03D1u2Dgk6Gr6s8B4GbDkY5PNx9FS4-bZ03H6xyMgAVFWfUZvCLFklw_elmI1X0SNLhj88g1tBYJ41y2Qt2uYtBj9TJasxh2BIV2duVavkxcEU08z9h9bnUEW8UakF_lAzNJLq7Uv0lWvSwL8mqT6MrAXFGzTv8D_mumA5u479Vz63j1I_U5TJ5hxu0q0cYib9h7Lz4_agOXuFzy4iHEW1yXCYf5Yfh6umZadic3H_Py-kXAgAWK5my11ujJItO3CeGX6tY9qyVxryGwRprdo42bKStJqc3oTkv_jDuxF_i9i9Sqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات: پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28948" target="_blank">📅 23:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=EMqj6dlHzlIp5us28GJlmvoq2N7zsofkMpLdCvHJLP8bEwuGOdHL7VzB_BqCQbgsRbgMlzxDrQmBF7ZElFjuTCQa66uEFNLlLgNjYijvpS87ucroOHZOqCYXa5IemByZyWndMMveX5yGuRao215TonBCacBjMpQQuX728yBtRt8RkHN7-5iOE0Xxc-xJag1ja8YAA31H_r0k15n44avYdE_tc4tZXUjiFQFV6AIOS_WSRMI9Zfjm-8s5K47VG1Mnzx8cobIgEZu9eN_HlP3jUGD2lYdqfC-Se1pXb2VqG2W4nJTaHGp0Hg8BXvVAoTqFqlZJ6dwVI-JB8yr9juxdag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd255c037.mp4?token=EMqj6dlHzlIp5us28GJlmvoq2N7zsofkMpLdCvHJLP8bEwuGOdHL7VzB_BqCQbgsRbgMlzxDrQmBF7ZElFjuTCQa66uEFNLlLgNjYijvpS87ucroOHZOqCYXa5IemByZyWndMMveX5yGuRao215TonBCacBjMpQQuX728yBtRt8RkHN7-5iOE0Xxc-xJag1ja8YAA31H_r0k15n44avYdE_tc4tZXUjiFQFV6AIOS_WSRMI9Zfjm-8s5K47VG1Mnzx8cobIgEZu9eN_HlP3jUGD2lYdqfC-Se1pXb2VqG2W4nJTaHGp0Hg8BXvVAoTqFqlZJ6dwVI-JB8yr9juxdag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از این کل‌ کل بامزه نقی و ارسطو دو بازیگر پایتخت با عادل فردوسی‌پور در برنامه نود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28947" target="_blank">📅 23:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdGucIQDVN6utVJRSFBExqavBnZ7jFTCuiirwK_gxnVpW36Bz-qmtrM-T_UzjfxGbmzLCR4lCu3JdDONQI3MiXbLuleTCnMC3CroYm_eXxjRyqJYwwziziVqgBSAPwtb63t1Gy7HOYE9nv4U7eCRWi2bjK7JBAjpCYlHZ3I8m4PU04P7q-B4Ds366W2RN6pFMdSF-zhNdmrI-Fqm-HV_eExsvgRvXNKqvrDammCl5jHv5WY-YpHsTvNkp5yc08f1eMxvHm1zNsy231FsfHFRov9bhdB4bjxBsKqXLMDB_kKazsUAjTktHxMG4bhn6KYaaqvSxumeILjZaQ05mkGxPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج دیدارهای هفته پنجم؛ تراکتور با جواد نکونام صدر نشین لیگ برتر باقی موند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28946" target="_blank">📅 22:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28944">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WY03DxhVsKaZIe7UUv3BERusBKYPKRJghGnwLs2ZiGnY-0rNt5KKKC3KWiokIbrW82DVCPABfcQ1n6p2No54OB5rn3Wfx4_GwmUdeGzZ-KX8XDFBJxlJ4P_hABHBzpgrGS51CHDzDvchk6O1bDdSBibhEbty1xNrEEcNeUOnlBWuMbqKu819oxl1Qm3TEzEgdkp92jLxF5mMjMjKz27WRlTBoXMaVs3f0aCMMUiHCmU1_YujOOoZdqqdW18BZ-NBztQfF9A58sSmlk-0Nbp58xPdOzoYHCPBxjyqUjqi3XfheFyvlMWJD58P0GkDmc0INoeymox6cSMmNcOxN3LN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UKqtjncBQYablzamVCMz9vKAd6b9nvCMG5u7Zo-7PpSI-DwnMKVkxOx3L-gCPKHhnwH3fsyu4UYlSwFPpcru5emZMfwLBiTuAnFu_iGreQHHyxzd0mfXxjsY9-NiKtE7JG_bC72onrCikesuugz6TwgXUhoRgIJlJh5b_ZXIN72OtCxlDyAGtSEh8ztxF2XQJOFVWZYoPpJYrwUKPLp056SI7Ol5G5gowFTKAJsykUq9XPq9AAIHtfmYu5Dv0OUagaqLJP_8PUOTsW9gmXoSrtWQFkiEeqYG9zUntsD2tzQBfVMbSTIfiFzYL_FSRh48kWhYaXYMOdgtHg7_bHdJBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28944" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28943">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJTNGFwXal1NqqayPoJ7N9GAt_J28wa1KGHoQTdCDyO0mp8-BS_kxJ3NopbaK37im9S8Oc7xbKkK2gAwYz2EhKMpxcHQ_BQ1oYY07ySMgsvOqGQTjqUT_PvztJ41mxUTyMXwg9WyNEjMx4c5ogbepWV_TM0zM5vpg2hKIQE1FUGr3sKQ7_WOJKU5vNFGV1bw2NyovXHthVu-XLgoTgIi-gcb_Y4gVRfKyw1CaSbeS9hD_dDzFAATvz3vOYGPLxGfLtVv4vgOZePwvFsI8cAy7Ym3tGNtYvD5roEUsljB7A2i8nzjf5Rf_h2hYRT2MxQTJIRAGscEH_gDAC78E_rVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌پرسپولیس‌بابت‌استفاده‌باشگاه استقلال از یاسر آسانی ستاره آلبانیایی آبی‌ها به کمینه انضباطی فدراسیون شکایت کرد. آسانی زننده گل مساوی آبی پوشان پایتخت در بازی امروز مقابل سرخ‌ها بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28943" target="_blank">📅 22:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28942">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9SLSyv1g81TnkCR31mjEvtyVJagge75LHX_9z7BxnGBdUABYWZRnahdTjzK8sgxDnjKgNivOilKBW4TpoJxR92sw9bxhMWm_2G4wrqkU83vAVOBgaNOL2QYWldGzHjFcQLVArdFvlrKM-hl6IJeqvhbkmZ10mMCCqlF-BA5cq7xpzKyPTq3NNm9ENJEVb-0Xu0Dsw_cPzw1X71myPXEuzwdep0Eye_LvEibOi9Gp_c_dVbmznl9HoyEsrEbWN7UOKlMVh72p0luXZGt_XfySBqb00v4nKuMbOCMb6vUNU3Dojts4WPqkIaOLR7AQ7I5vZt0iGb6oQ4ZjKd_kSvBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبراختصاصی دوهفته پیش پرشیانا؛ اعلام رسمی کمیته انضباطی فدراسیون فوتبال در خصوص تبرئه شدن استقلال و یاسر آسانی در پرونده شکایت مس شهر بابک و سپاهان.
‼️
دادگاهCASهم از هرباشگاه 100 هزار دلار میگیره آخر سر هم بهشون پاسخ منفی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28942" target="_blank">📅 22:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28941">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=FSFGXOkty2Bg5nx4_o8u8qvF0UqSFh2kdkP3VnPRptaxDFcRSkVLPW9CAoOWqn4GzygpUI04VMK_lgsRRDTTnL7nGCrVtIcQZqffrU049gINuwG0exKawZoguDG5E03CNVavhdFPqI2pYSSGRci_CosZocWHc2XcMmK6X7LLvLMFIJyQFG9ZyTgVUJzsDKjGt67u0xEwMvxKuyjtGgohoTiqTj_iHB2yizzAv6iwzILAHstfkJJzOyU6W5SOOiRXzWLKHqvAopfkLMGRjdTvO7LbYk2wUVfCMiSCQhXnJpD3ZwbQkLZT6EB-T4V0oXz0VsJAMgb2_dZP6MoxyQJ9iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4240a550b1.mp4?token=FSFGXOkty2Bg5nx4_o8u8qvF0UqSFh2kdkP3VnPRptaxDFcRSkVLPW9CAoOWqn4GzygpUI04VMK_lgsRRDTTnL7nGCrVtIcQZqffrU049gINuwG0exKawZoguDG5E03CNVavhdFPqI2pYSSGRci_CosZocWHc2XcMmK6X7LLvLMFIJyQFG9ZyTgVUJzsDKjGt67u0xEwMvxKuyjtGgohoTiqTj_iHB2yizzAv6iwzILAHstfkJJzOyU6W5SOOiRXzWLKHqvAopfkLMGRjdTvO7LbYk2wUVfCMiSCQhXnJpD3ZwbQkLZT6EB-T4V0oXz0VsJAMgb2_dZP6MoxyQJ9iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/28941" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28940">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">📹
خلاصه‌دیدار جذاب دوتیم استقلال و پرسپولیس در هفته پنجم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28940" target="_blank">📅 21:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28939">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaKgVYXMxW3PwSKTlnqh24qn-RxFjNOT8THlDGZ6_oNGVkM-ZYGjBUpah2uwVV0PPQnvxAfTxyMbTxZpLFl585yIDFS8gw7kQvQkgeE8VJVwv3JqBSm8WvWUr3I9LhFQtTHElFBg90IFjA22jEgOR9_YcAKyB4en2nnAwmNxASA60AvZs18CV68yK-uQ7W8LhxvS2APFj17KwslK-eR0LT_H3S04vtOKkkRTke0IXM2yyyXojHCAEpxnVqjk--d5owbxVAkx0YKklJruKPuA7ZfgfqYWVzg2jqD4uz_iWeVQvx91sybSw68GJ5CjiKjqCDnErg5MWftpyIEb-_A1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ شهرآورد 107 پایتخت برنده نداشت؛ تقسیم امتیازات سرخابی‌ها در نقش جهان
🔵
استقلال
1️⃣
-
1️⃣
پرسپولیس
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28939" target="_blank">📅 21:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28938">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCFHZK6Nw2dcoq_9de2WjY1VxVXvEhEtNA1cSiTJF7OTeXxdnqnwpHmkLy2s268iZjg4KT5tDSuUrD2-swElQCK1G3Fj9qleNu8qQ7mhCiFr3biiIU7YR9_w3o-14UZeKHKTqjmIAJAdeGSll9jSVOpqQdxLvjdb3yKUeAhHJUiTXnS0Q-XLanKmrTkHjr8vXG8LWw6_aRc78bXBQ6EHCYNx2-LGfkpelK7gFRQAGfKnpI2qqy6FbIf21xBfcRbwKCJsz8WIa79s3XG8mZrDBlcMDEIn7qzjDZNh9v1AZWkpkARNuPIIYVGoQ2aDWV4_TiWgs8Xi3RRMSoX42N-OOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
ستاره آلبانیایی بازی رو مساوی کرد؛ گل اول استقلال به‌پرسپولیس‌توسط‌یاسر آسانی در دقیقه 60
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28938" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28937">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sJPhtGfnKXH9lJjiyi8SKn7FC5LSasuxYGldPDCoN4rcMki9Mqim0ObWKJv-8yonO1qt1a8t2m8w3HUOV4SgaEfJJ4ISRpeqylqhZVJhj0hThd945tYGvhORhIGuisNt9B46CNVznTRoCM-E6LF4mMEk4fli2Macia6zVDMT6dtU7LlOQgFyGtmQQfzaFGnrA3sONnJYJWqi5nqkcEa9VmXGeI8Cl9lUCb6tA5GfCehKbJl0OLBSHyZRMzMB35STuXncFqIGM94PIhVUzoC0LvQJj1JmNV2UVqhyyfkKT1qM2k_R-PM7gMKK6NAwQ5L7mNSlTSwdpmsw3Lj-2eAnaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba22d8800c.mp4?token=sJPhtGfnKXH9lJjiyi8SKn7FC5LSasuxYGldPDCoN4rcMki9Mqim0ObWKJv-8yonO1qt1a8t2m8w3HUOV4SgaEfJJ4ISRpeqylqhZVJhj0hThd945tYGvhORhIGuisNt9B46CNVznTRoCM-E6LF4mMEk4fli2Macia6zVDMT6dtU7LlOQgFyGtmQQfzaFGnrA3sONnJYJWqi5nqkcEa9VmXGeI8Cl9lUCb6tA5GfCehKbJl0OLBSHyZRMzMB35STuXncFqIGM94PIhVUzoC0LvQJj1JmNV2UVqhyyfkKT1qM2k_R-PM7gMKK6NAwQ5L7mNSlTSwdpmsw3Lj-2eAnaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دروازه آبی‌ها بعد چهار بازی باز شد؛ گل اول پرسپولیس به استقلال توسط محبی در دقیقه 50
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/28937" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28936">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=r7VlSSUr9sgDGkvwG62RVDd8nNfTruFdSZsftRI2QJqLKbLYq86xm900e9-Wexo_IMk93WzZ9NbpO9ht3J8YR7x_CcLsbULIWiWaOeUz_TraOWegB0sBimqEtIQcY4mKAxgwWnKSuCaBTxGdouTm8MlfdY2yNUyGsZ-gbjvnMYOLT8blJ58QBJX-XipGhi9fkQdVoUzKmda_pg18V3OH5nlGuO2sisXRjzy7_QmWQddknO8D1icBdTFjJaeJwvv_m8EjCCIjP_2iUisDVj23-W6k1fVsorcSoM38UUpUUdMXPo2yt11OtuwzXXqTvQcTmO3g0OxTop5W5el045M_SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a3fe7b44.mp4?token=r7VlSSUr9sgDGkvwG62RVDd8nNfTruFdSZsftRI2QJqLKbLYq86xm900e9-Wexo_IMk93WzZ9NbpO9ht3J8YR7x_CcLsbULIWiWaOeUz_TraOWegB0sBimqEtIQcY4mKAxgwWnKSuCaBTxGdouTm8MlfdY2yNUyGsZ-gbjvnMYOLT8blJ58QBJX-XipGhi9fkQdVoUzKmda_pg18V3OH5nlGuO2sisXRjzy7_QmWQddknO8D1icBdTFjJaeJwvv_m8EjCCIjP_2iUisDVj23-W6k1fVsorcSoM38UUpUUdMXPo2yt11OtuwzXXqTvQcTmO3g0OxTop5W5el045M_SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/28936" target="_blank">📅 20:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28935">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=je0z6aQ7dPFPytVIS8TgfvDGg5bj3WnvtQf4wfKaLO_tFAbBlrQUfb4mTyUUZCWzyMXB0eM0qZ7AZ3guiLkALVpjd9fsUTdjf5d6pMi33wNddDR4A-1vS7oJrGc8iphJuptB4WmdKPVXmhId2vFw-BIXJCqdlzKjb08VMimJclaKyxMCukElttpSNXlOTt8S0r4k4PVWPlSQZQIS9BhOvYeE4GydoFA3tT2N-23WDlQMvTyL_TyioV3TdMuJvTyXr_ucNt7ixvup8MDVn5ovTcxtwYrR-aKBCG4KFeFZjTheUovURh_Hp8anUMim5jPY9IT8wRZ_g300RU2qtXap0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9ae878bb.mp4?token=je0z6aQ7dPFPytVIS8TgfvDGg5bj3WnvtQf4wfKaLO_tFAbBlrQUfb4mTyUUZCWzyMXB0eM0qZ7AZ3guiLkALVpjd9fsUTdjf5d6pMi33wNddDR4A-1vS7oJrGc8iphJuptB4WmdKPVXmhId2vFw-BIXJCqdlzKjb08VMimJclaKyxMCukElttpSNXlOTt8S0r4k4PVWPlSQZQIS9BhOvYeE4GydoFA3tT2N-23WDlQMvTyL_TyioV3TdMuJvTyXr_ucNt7ixvup8MDVn5ovTcxtwYrR-aKBCG4KFeFZjTheUovURh_Hp8anUMim5jPY9IT8wRZ_g300RU2qtXap0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرشید اسماعیلی هافبک تهاجمی سابق استقلال با این‌گل دیدنی‌اش در دقیقه 90+8 سه امتیاز ارزشمند رو برای ذوب‌آهنی‌ها دربازی با پیکان به ارمغان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28935" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28934">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igWYY_ycNGP5pM4FEmWQxTSAEOuYRMUHxX5if3ZRh-11WhUibmkZeDSI2PYE-cKqOqiqJnJd7pZ23oV8XdFlUXCrLvC9jNdzoEW_rVRMldDGfCOvTp7Gfru2ook5Rf1-pHVu2gFeT8WDRbpAwgxh-R3kA9714W_AQ0EEGmJjsG4e6NPSDdX5tverWO_BSomPpTk4QO4Htypr1uZ_T8SD7-HT0Q4tGegTLQ25wQ5Yo5my7KRMaTZ-fuLj3K67UX4-FlqYzAzVghRkDOVP3ICp2wmw7uGTbg59V1XiVL_olcgNJdKfH-eLo7DXYLD509V_cmTKh4wnQtkRu5GtlcQKmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمارنیمه‌اول‌دیدار استقلال
🆚
پرسپولیس از نگاه ورزش 3؛ هرچی‌جلوترمیرفتیم بازی قشنگ تر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28934" target="_blank">📅 20:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28933">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ld7sRZ8yl7CsOuKNSeYfbh6vD5H2qrR4wtXAgng8T4LWoM4KHghi9RTbvhgCGZgHxO0_CrO2VdYsNiZ2Jf6QDGWgnuXDXZo3m2o0baDa7fs9xT5Z2EkuZjbyre7FL63tSi8n4YqtzVmlUgPvdKquS1oKBUUTIq6Eaq411mDueM2-4_T5d1TuyMKi6Nu08q2z-8a981fW7IfAhSCAZahVwDqHP4JyPHDXwiHVLP9Ni7bTE36dj8ClhYjekMzHXgN_K8eeYU71Pc0RCMGCHLDlhxva2Eg0F3hA210ZU4A5GnEDkG4u4FYO6ve-i3c5pA-LwW4DP7C858crk6iDW5gm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب سپاهان برای دیدار مقابل صنعت‌نفت‌آبادان؛ساعت 20:30 شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/28933" target="_blank">📅 19:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28932">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJTRI8ltikY9Lx_i3iyWGzXye5fbRBzsfu8aBiWvxbYSSa4k5q4nV-1yJK2eNeDmfKxfhp_S9IyQxFfCVh4gKLbAnt7bEM1fkGNC4k5m_Z69B-xrxoQ4p13HaYLqF3YaBVAmfPleDJo3aKNkX1E7wFR9Pa4eb0EJMoHBpdUIyng0puKGoIM2w_h_KFWWG3k_pPJGfXBcPOyhYo1ugyqPd_2xyftwLKb1riLuZ0KfYo6AzZP2_M7FCwzVRSG9JaFZjhyB9umhY4VZO4AKV77e_bUkAJ5caCL8YUPqJF2Y34jKabdnv0GHVy_ijL6v0ULyoQtXfTger1CNkAcIY23EKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
سید ابوالفضل جلالی، مهران احمدی و رستم آشورماتف سه‌بازیکن‌مصدوم سرخابی‌های پایتخت به دیدارحساس‌شهراوردپایتخت رسیدند. تقابل‌ بزرگ دو تیم استقلال
🆚
پرسپولیس یازده شهریورماه ساعت 19:30 در نقش جهان اصفهان برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/28932" target="_blank">📅 19:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28931">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=LTmTZRXzW2rYx3QLpnRkbqBD1XgcLEyxX4j8emmICO-A66oQLN7GPv3-p_aiFBofrjpVRwhIC7LpME2NO2zyRd0_uFRF3Ehm1IccPg_XvRbCavMMtdDkHlIugo1vB2GnNyGQ8Oi3dkFqo331PY_RNLR9VsCsQ46cE21mojNE59ZzGRPeUkQpsLsTID529chMBq1naCOgaKJgk7epOzAn0g94mWLgIDbaahwy1JGc6N6BMRkpkNhO8UQA6q28VOFN_5KDToWbm_upltx31lIKLs-QaaURwX3S3eeTmsMfZdy0i7b3uYuobdv6k6GgtOcMKwGrTmQxz2JzRtoq8I1uPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b4d98d669.mp4?token=LTmTZRXzW2rYx3QLpnRkbqBD1XgcLEyxX4j8emmICO-A66oQLN7GPv3-p_aiFBofrjpVRwhIC7LpME2NO2zyRd0_uFRF3Ehm1IccPg_XvRbCavMMtdDkHlIugo1vB2GnNyGQ8Oi3dkFqo331PY_RNLR9VsCsQ46cE21mojNE59ZzGRPeUkQpsLsTID529chMBq1naCOgaKJgk7epOzAn0g94mWLgIDbaahwy1JGc6N6BMRkpkNhO8UQA6q28VOFN_5KDToWbm_upltx31lIKLs-QaaURwX3S3eeTmsMfZdy0i7b3uYuobdv6k6GgtOcMKwGrTmQxz2JzRtoq8I1uPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره سیروس دین محمدی از بیخوابی در شب قبل دربی و گرفتگی عضله در دقایق ابتدایی دربی. ماساژ درمانی؛ جان هرکی دوست داری ول کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/28931" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28930">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIIvYLexWLRsq3-DrVonIcYdnNrPShYokVnbTQWtvRGt2p81BEK-APS42-CclqxPqaxVclzRZLRtrvWFdynJODPcPG_xcMZ8MM9rhww0iwmM4QeNsr5oNUxMesoUEaP7UyyRnJUlkRhaCZYjSMEC_RkWE_cfuusFv3LYypQeayDw9GDYPb_vveBAru2UQE_USaMUMoPpFZZr9Dob9nJDhGjaJ2X3VUQm5c66Jgv05ls7kZov1WmF-e0kZhXAvYOS7X8Gu3SbBx8x8W2adMZaTHpD8fAHAyYawjmo2VODfDe8fGFC_8zFgUKgnUltE9eaMop0wMyxpJo7Gv4_rFeJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست کامل بازیکنان اصلی و ذخیره دو تیم پرسپولیس
🆚
استقلال در هفته پنجم لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/28930" target="_blank">📅 19:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28928">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg8RQWGvS7c7LgHfkOtijqBEnV0cDau-XxYqjUT0UVT-vUtT2fraGKATYiUOj_zlAo7nWwmri3UY6hLuvVo2_awBk5SI-dAqv7MdurHWGTd55EHsmWkw9LnTC8wC9qAJhZRZgAN2Pw6wiXmqlDRf5-3W79cjz6ymZqGRkqLxZb1EkomCcJpwhpdlQ8BL1QyIeI-8IiSWdXIrQApXdjCDa1L5k3HttrtKDkflBRskhNTzwXYhbJ9AzeoM_ts9VmrqJwKt0sUVzdIa0ueETS2QKOYNNs-gONVpAkn1NohoGqQYpllXFmeYmTBUyjyIYlGdjrTvEU0ftgdLzrBPCnrgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/28928" target="_blank">📅 18:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28926">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXCD05ycz2lT2mHJUVdA1yNrTjh54iiu66lk5Jz-rtqiDWRI-RsRRRQUVuqhlU19TADW1gZa8JcNdsFa7pm-Anyn0FQPOTi96kAwLQm7LEyWwSsEGaPzJ9A1tYbObAo3roiFI3JjLLo19QXKTu8IzjzGpi3E3loFwBlGxST7cOc6Tye7lMJeaP1SQ_FsxvYajhZLVmj5oKSAkeKQDDFqqoyXrxbriK42eLttntfwLU03FPdtOPP77oocor03vPx3pY9vjmZtaJsJLuFtQj-GC4X83J3feAYrxg-SaJtPglhTtquY_aLTt6kpnEkX6QIO6EYaSC5iNUvRyPA7Qv-veA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/carUBFQQ0x31e4Z8xHFNKvMsWlYzH5eE-gz_P0edhCLb4am9AEujVHxTicahqX8dUEvTP516MZFXcPoa_7Qzn_crEV7fuPKcpH88TGDa2plswpI0kRQkIqif7wLgs3MvI5iDGiao6FzIX-G-wkoElQnQlK1qhUtpxaTtUI8QnCwyHm82gqdn6f_zEA927_SGD1-8asmKa4zhTPVoxjWu3h0Kxv_YidQxE-wuBk6I4K-JT5pIDPF5EfHw05ZiPcPRVkf798bMSMjdZRXX8c5onQsU9IrQl4gw5MZzLbFhlcCGPMzbXUyb-E-IU2r7k63galiasHLr1mROBo57YRYz3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛ ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/28926" target="_blank">📅 18:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28925">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqEVh8SselVcL5qAC170N9xFdE3Lxjq04byOt1QMdP89Dkt11RrWWdsmLgejeEX9708MWo07h9smCPNs22KCsLi4_f543rpvULf8_vvIhqgoBgipVhWDdFIWtI6wKJ2VL5ukkE5Erw7PsO_uujiOShsfdnhU_5fGt2BUF1I9AVC7W6o0CpRpNXTT9Rj-OhzSG2eGvGs8IBp4rU2Bm0nYlTACWKN5ZXEgiv5LTXSWF2bjAlT4hin9aarrf4j1yBIBEp-O7ObAK7_1LmbRt5YztH9Iaq1DfkckIwjBaeC06wSTdnW702Q3a9HGMGMT5SE5W0aHRgPA5utuPZlxs1x20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر لائوتارو مارتینز: لائوتارو در آستانه پیوستن به بارسا قرار داشت اما اتفاقی در پشت پرده رخ داد که باعث شد این انتقال منتفی بشه و باشگاه بارسلونا با گابریل ژسوس قرارداد امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/28925" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28924">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD8Hm6w0MboqcZH540oG34XASLpRQOmcSQVoKSQiULI_iQOqyYntmnGdL8jxQEIZ-VBRR44DFUYghk33E6L5i-YkUvo7iCRykvqwcPWSaTHXwjLTpsIn5buoPJ6ihSqj6m_mVFu1_ViIUY2bnAu4-f8lykyCuIHc_4q4r_l1Iqtx_639mJ6IcbOpkeZvJb_BlXCZMhICmKb75W9148_FwoCmJSOgxMjzbZWiRwvH84bMZrgs6mTC9QGrkSiofw6yJ78U5pcnilOTbe8u00HsUsPJFGqYSnjbQ5Wevxe86aS5HxIuVgbfZuqQXJxE7zExkVBNgSI95pGIB_a44cGB0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لیگ برتر؛
ترکیب رسمی پرسپولیس برای دیدار حساس‌امشب با استقلال؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/28924" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28923">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwmmE_yi7rFGRhxW5XVDsSdAOOzg7TTLzuUcKJXgQo87W7XGdbDM99N8Gb1NBsogSvUkZdMFSCVvlKFIfKqa5xVPCFy_p3Ij5oBODVFFGT7P5iX1a0EwJyfcPDKIcIwblwDa4Q-ZO7w-vGgnaCn_YEHfs-m38A3l340R_WpMsdH3bCjO9i2EUjrre8lVB_g92RAZFImR5h_pkiP89gHjTA_XPkKfeowDOMravVyAY4iusGn6gX-yT4aoCEbRnBUmVWZ9WcEr9vqXUk1gQDY8fTW9Upd_yKVDDCWboH2ZeueuPrvNzeEjhfocnKoeG3pB-u0z1k41gWEbp0xTsDgAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
شماتیکی دیگر از ترکیب احتمالی استقلال و پرسپولیس برای دیدار حساس امشب دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/28923" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28922">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAgf2k2NP1NHIEdZu6W24lG6kjdP44u9It2oXcu3pg0r3h_PB8BTLVT0mELQ1v-fpT8z7VkDL57oZg-ZT8s2j9jvYab7DV8YD23dboc9D0eOfLmdcUSGZprCA9eyuQpvLzSik-BHa_xWPKv7NqPJhKf3Kg2uBgreSaEm0YnVx2cKM2dDVxPQRUe0_VVXnFUeO9zL5MBwhT6lQYrQtdzqVJcK7seKdccww98Lp0eg8DNbHQra2W8jiZYnMkchrgWJQY4-AHp7t54cG9wrJkgJ8alK86-YyL6kdZXDjRM2xyYCrtamNnqhua-F9rweHT2XbPfBqil5-g0PIeYqac-YVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی به‌عملکرد سه مثلث خوفناک فوتبال اروپا درسال‌های‌نچندان دور؛ کدوم خفن تر بود بنظرتون؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/28922" target="_blank">📅 18:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28921">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=pQi_Y64tlhHw7arEI-WSg17WHNNNVfRF_G4iRkgmHKWQNDru_Z3-6YKp5BgpTLjAr_V63BpFoUSSLrDnYCaajrwnofpdBhqvIhR5LJkRv_AJ-qmapZeIW1yV_-lt2ECsgjrtnoJcIUlV4TBAXbarw6u4J_MCvv5Qbu06C9QXN5cQAQEg2e2wmccdtwJMUgyxcbkJywZUmW7uo_sC_y6vfXSo7vCikG6k63f0kcy44YfI9PqIXvREaKOdvGUUEP50ihdMegStQw3GXE6IUiagrJ2v1WMg0TxU4SCfjzt7c3--082ywpJhXXV7LioH2g18AQKfejdmbsrmpEaQfxgK_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa3087d7af.mp4?token=pQi_Y64tlhHw7arEI-WSg17WHNNNVfRF_G4iRkgmHKWQNDru_Z3-6YKp5BgpTLjAr_V63BpFoUSSLrDnYCaajrwnofpdBhqvIhR5LJkRv_AJ-qmapZeIW1yV_-lt2ECsgjrtnoJcIUlV4TBAXbarw6u4J_MCvv5Qbu06C9QXN5cQAQEg2e2wmccdtwJMUgyxcbkJywZUmW7uo_sC_y6vfXSo7vCikG6k63f0kcy44YfI9PqIXvREaKOdvGUUEP50ihdMegStQw3GXE6IUiagrJ2v1WMg0TxU4SCfjzt7c3--082ywpJhXXV7LioH2g18AQKfejdmbsrmpEaQfxgK_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
کری جالب و دوستانه بانوان دو تیم استقلال و پرسپولیس در فاصله دو ساعت تا شروع مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/28921" target="_blank">📅 17:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28920">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ea0yh9g32ObihxuJ3zl_OtyhRgiMgUrHBfMojue_0RKqOpNOr_vTr-zp--QCylfW1uG5JzLwCjPQ3HY7RrlhCepOQWJ8WXXVAB98lhVTCZbhHjbqS8I6pnjcbpamwi2X4Oh1Z02PMJqvYcHloezRS2K8szLKqy0YJViUp-KSwgk1Qmn45-lI--Mt-aNVhCw2ApzT14qq3v7zQk6s1ByRtOY8W20AHCBR8acEoQPmCln7Hd5oyJv0vvGgrFItrzkSvLTACQD-X053Rjdb2lTvic7R_811pOrC_97KBIpC1Ly8PVKBF3MZw9HlsT4VgJoArK1kTRThDsBuUF6yqoPbOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
چهار دربی‌جنجالی دوتیم استقلال و پرسپولیس در تاریخ این تقابل‌ها که نا تموم به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/28920" target="_blank">📅 17:17 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28919">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKYHNi_-oK-G3N02ZI4vHk0wfaSdpg1Q2auLRVpWK3CpDa9hpvq9_kQP-_sx6sn4Q_7HYhjloPy9e1NCdEtL1QtKV2Xrq0hj15Ms2hdg5agnT6ErnXN51GPcLGbWLMpLhjy6liEd3sxMp7vt4bNm0o2E_YLoSRPS5xtfshBaxt_JB4mmforYh4gfXyWs8sUN0gX2O8xLQ-8ruzbKR1Mth7rXgCNn0dQeXWbrRGUV2ui5vun2jLKB7Ec-Yj3jU_-uh6gBa4U4yBKYNPfmJJDfz-K-ADIKeKmlwdotKjl1gm1NI4Y2eBOQRhoTVCRePC8Zz7yYPayANoRem3StWRsviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد پیام نیازمند و حبیب فر عباسی دو گلر سرخابی ها در تقابل‌های خود با این دو تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/28919" target="_blank">📅 17:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28918">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tovri9sJ2eojfkgNsZUfCuI1ojzSMhxjUG9vPovRXk9yW81YzjB76_Y3iXNHO_pFZ_x1WJplSb8d4ZZQKDSu2LLkNCHM8lty9SVa1XPBl-2ivXBvblZ-WJQ3RsnKV_2ndF3q_ED-nmrdT2UBgfxoPJEaGGkrQKxta_8Q9azs8J0FMTCRuVP9cvSothMFrrl5AjOa7IMfch1EamsXaCSwRVKPkSyXa3cFSjrPMhZnuHyOq6QeSgeZe_W6AOoCILkcQNvqN5UG3yX2nus7G41saDWRKmB3V8ODvod-vPnOxqECZk6y1AZHGFAgt5sMLnI6ZbdD0EA61JxXgawcpv8jKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مسعود جوما مهاجم سابق استقلال با عقد قرار دادی یک ساله به تیم الحسین اردن پیوست. عملکرد فصل گذشته جوما در فصل گذشته: 33 مسابقه، 19 گل زده، 8 پاس گل و نمره 8.1 از سوفااسکور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/28918" target="_blank">📅 16:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28917">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT-Fc7cOyF75LYWh6RmUw4qJcdSSGeKuQ1Hq5ewBzYx2p0SBeVXlezUjEj8t9LjuCNx9bkrbMT0wvQ7lP3iZx9OgZutwtYPC5xyaEeHwCZgeUMF-Tawe_Zgq8zJOOST4ocQLcc-Lezf8XSInKEEw2PIJdT1NX0yPKJm0L2xi38AzhldaIS741SU-juNnhOiNbauJUsZTV8gFqk_I2V4BqPYgpZY1hMeVZWClJK9uQZyz1vDzPnTSF0mQCk_2LQOrQLheaXrzBt4q-6SkVSqolbqTWY8m5UXStOXTx51y5rjGHSaqXQtD04bvr7a7mAGeQ3W-BGn1r80tfOjov8ACdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نگاهی بیندازیم به عملکرد تارتار و سهراب بختیاری‌ زاده در تقابل های خود با استقلال و پرسپولیس به مناسبت بازی حساس امشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28917" target="_blank">📅 16:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28916">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOJ2MaqA0Z9ehkl4b-rp5t75V67oK1b7gbfunHKsXXixKFGhZ8Y2G4cDNSHv5U3EjTDAa3mlftmky1kKZ726zi5Sy4PtBuGfZ9aXKjBhJe5y25ZWvlC404GF9KR8y18lHOQlSH40732wBWXy4vbcY2jXFvfmSN7uhAAH4Eh1WeeCIQ46LKGZYoRd6sSYpa36oMj48LkmpCA65nMIVCnObqjKWDbIB6fwD2Dn_zUtQe7xewNbbi1bjMlaSvb82ggduC8pY5BLFXC4DJz0Drm4M9gSVMdVi4sV1ZCWwQB6QbKkXlNMCpjFcX2A50YG10Yxr2NLAWTVIr2D1Ue4WonwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
درآمد فوق العاده 200 میلیون یورویی باشگاه رئال مادرید درپنجره‌نقل‌وانتقالات تابستانی امسال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28916" target="_blank">📅 16:03 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28915">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl_K0J6qM8qzaSY8JO8J3EsZjjBIYlTZ64GeU86TFWgPT0hEeq9zhtRY3jxoy56wmyTSbGcp-aZmrnFisbOs6-SXjE-dF1eHmbJJfoCTqNMLiIulHk70SS3LI00F1c0hfMegYzxICa8p5zBobKC4T1qtvUFvlV9-6nYd9jccMKp80JVds8_89B-DrvOzEPvFltno2N4xUOC1StIl5YNgb1o4SlloDrsvC7deWYFR2UpLNwqPatV_sZDFN8pcIW1rJrTEnsHbwoAfLqfGV-jiOtRGQgnAqePwj3W6nkVUD-j74AzLnTa2WYoAeSmytVK2pYw4Fb6TJmkB3lwYQqXJZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیتسو موسیمانه سرمربی سابق آبی‌ها رسما سرمربی تیم ملی آفریقای جنوبی شد. پاکو خمز سرمربی اسپانیایی‌سابق‌تراکتور با عقد قراردادی نیز سرمربی باشگاه مراکشی رجا کازابلانکا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28915" target="_blank">📅 15:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28913">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1oKnuRBp2Rwn6ZJmIlMgRUAdoSvAAxziHGrg2edd-tcdZofyWX5ZDdWR2MQRBQ2UX_nq0NmrXCSpltU6Ox4CrGYbHxGuzBDG-A3-70YpnPeWR5ceAjssdaqARQ0mc96hEdFy9HH5uTsgnVPtN15X4oV2bztgeyWA7kkhjRIAo1afwxZ367CEA-fOJZBBqeEtRCJgoGB6DR-Y4-1R5Ij6zAy5LbW3VIZgDXMcM8yHIEs7g0ehTrUMTvVJ5p3_N-OQiwjjjkt7KUQ1KcWiU0vlV1-ff9ec4Tza-10iCen7E0iZog81zIjzMZGfQ_OPLbcFRH1WY960spTQDEpeHV_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7WTdyXQGNknLJ0sMG6BQUJVBf3lUMiLedNX_jH4UOGixvOoQeyyCLNJqimDwBcN6NK-XJ55CpwITBsQqoEs6yWhniQPdbesfDtRICDhtBQKkLCK8nO-ELm36ybplgr9kk_7693gL6o6TpHetiOg2mqmCyaKwP12vWCgSYpt7zPUdBzq_ww7hw5mZHap1ie0sgqsn5rtm6DpGPyKP2ajRfH5sBwZkPBKTaVktKzMk6gA5QxZzixHN35IKmnrQYlLNIXAYeYFK2X0avjClVzyw2FheMVEJpSu9UJMwJcywnBkjAAlfg5aTln843I_N3bxXkNvlcYBkHinI9ViRrFKSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28913" target="_blank">📅 15:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28912">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YogSCvZNMJA10UHpNLCmffeMZuP0pyfQ4WYGc_l1h_Nc5qEBrBiGy_y1oTV_iCpinRUYdl3J1O4u_JvXdorqYvYxTLdRYrh5RVucytorW33wNjaQSz9gNWYdXGZDjbswZtJm63jz8Zlk4S4U194n2RHbqqDEqQcx2AvfJJip07-HrofTeb2FHJDebb3p8gJ0M1bloaZbiUR1yCj2oVtW04YJV3WYyrslDmGScvud0RZYZ1iw1Yaym8KGHCgi5Pz2n-XZ-6iXhX2UO2T1QHOUYcgeIf6tYBXl1eOOZUD_cYJhkiP3c5nYZ3f1nsfWaPZgvGIqh5nT4gSiv7t1LEK7pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه و عملکرد دو تیم استقلال و پرسپولیس درفصل‌جدید رقابت‌ها پیش‌از دیدار حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/28912" target="_blank">📅 14:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28910">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaulHS6TS1KMMWWzJYtdRh6rRL0kgSVih5IZB7J6BJbfpaDroRRUoEH9kv9CoT-yaO0aO2cF4KUJndHKhkmGc9fCLx0apBBJhiBsZwg-M6mYfxg5SyMDe7ya3fjkiflzpjf0aWp_CrNlH3VzyOkyGZuOWnHumyvWHG19JycoFOJNHcMO74vxeb05UyHxJoafpyUyqdSMx__i1bh4G_F-qIhGiZ80qjd2ve_zHxKySeUKWz-uWOlph-OSjyNJvW1kgyIDN7Xw6UekoBlGrtlbYMEtCYpbeLXYrKjHZfeiSJ1xSBcHYTDbPxO2bqgh0hyW-NN6wCVquUVvItOaA_rVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28910" target="_blank">📅 14:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28909">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=FjpHPXCsmcRfenm4D2bQmsgY0_sauTfyaWu2RKlhhST3B56bsLwAlKt6rlrswRhqqjj_plc9AHKpASDN5SlX4c0YKajHclcrJYcGWxwZ_OceHtSaz3dmruORxHCqdlsn246-oXvNKlKvV08jhNXRlM5XfL5u9BFxZkgO8DQx9L2FUpIssUI1Cn6lFvTuYNGQymCnoeP9IyE1v6B1c6ClL7YGqgH_1zUZWwoXpBkNg3UKl7cPypFp0fbEIsZNW5DPYQ5TkYFF4fl-u0IDq9yzY2TLbIFmZhlEUQ_F2yZ005JKqNL0AuQyiiiWa93fVSjzsBd4HVxrylKWZhJdOspAtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0f14bbc.mp4?token=FjpHPXCsmcRfenm4D2bQmsgY0_sauTfyaWu2RKlhhST3B56bsLwAlKt6rlrswRhqqjj_plc9AHKpASDN5SlX4c0YKajHclcrJYcGWxwZ_OceHtSaz3dmruORxHCqdlsn246-oXvNKlKvV08jhNXRlM5XfL5u9BFxZkgO8DQx9L2FUpIssUI1Cn6lFvTuYNGQymCnoeP9IyE1v6B1c6ClL7YGqgH_1zUZWwoXpBkNg3UKl7cPypFp0fbEIsZNW5DPYQ5TkYFF4fl-u0IDq9yzY2TLbIFmZhlEUQ_F2yZ005JKqNL0AuQyiiiWa93fVSjzsBd4HVxrylKWZhJdOspAtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
به بهانه دیدار امروز استقلال
🆚
پرسپولیس یادی کنیم از این سکانس به یاد موندنی سریال نقطه چین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28909" target="_blank">📅 13:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28908">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_EKAAweuBc1OGiXeir1I1cxGoBIUtWLHuBCb00Ox7vqJDv5mDc9IXnSQATGVpIWBgetMMQ7YOGRKPNaSmpLcdmY-0z9xrRDT35qeoQS7v52dn6YMJes_o3hcVMoqE6zGcyi6eZpoNt-M7aFl2xSE2TWw41-9I7O7RzVQuRjDH9y9tg2aMiwisqJp-1tcQk53wiLjk24hj6guhLACnB9AjKzagg6EQSRfWcUvctdHMW5cvQVnt49aE0gQIjOOmDJcZZVpNzIUGtvUA6nwCvA-1Q8zihd1sWKZ1Ljb7CsChritKlrUG55vQuazeAY8naw3hzJ_uNAuvXJ5Ak69s_ysA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/28908" target="_blank">📅 13:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28906">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oYhGeGyjGnMgk9w_QB2-1L5EwoBW3mKzth6nK3e0qtCnP-ANfgk4oMhRXIVn1Q9Dnj0PEk7Q4dxnr1_1PcWRyh_I8dlffksgIqOZFoZME55PhQhf9LgrKZZQW6OcRoL_JOjRhApDdTJu0Ti8t5c0IHJdy3Hqt3lkgW28amY6kjNLK4jfAuIJ-amk_1mpl49Zzmq7n4WAAIb-9GBMfxx5g6lTf1mxwu5DqOTVa2iGkJ7sR5zGZ2Cv1zceZ2JnI2tqY15oek0RSfZ8iwnbpYnrp9GLPzny1oKH5y7eW17yl1smfgl2fjCFotZJcA3Xqlmey6ACUHZtj_zk0TmRJ9tfIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_Iilv1hkrdJEPOm7rkiXtbl2jZuvfpWbX-0N3g1pdqX6yfE3VmYeIR7uWKsg5nHs3j5TN-DKLWM2oBCQKeMP4DrECY03TV8Qs9AFUsAq_DaaZHXsMP3sB31MNgMONoZKLq4MuTYP8yS6XwS-5LVbFKqrMJYbjdH4ge99dVO-AUsOLzuWjN6aYTI5l7vy78UtYt-4ekGJ9X52-0BxqFdRIG1HQzDyWZ-Wq25Nc6Zv86wl-JtXwqgcoINpzjh7J3vvKFjG4j1YXQQC5ZMqNIX4QhLYDd6VUsE13-BZMOl58A320FOmPbUeIfKMNEaoj08xKsUq_R62L95YYJtZXdLiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رکورد داران بیشترین تعداد بازی در دربی و رکورد داران بیشترین تعدادبازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/28906" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28905">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr9__Vp8XhIKU_xEq7QeGv7AGUe1tEJARjAMkDaI5bWonJ2-W-RzVYQszqHUcuehJvlBWZtCih0bsQ0_e6q_-4_ElQMAbd36aoQ9GuGO4KS9E291OdOXTjxdu4mtlfAVgfbrGbqkZJ5OJ1fjplQhDkVkDJ3Nip6ctF_I_Ai_Mkk15I4Od3RrFh44ya6sCZZGxIbBrCa0MA2cumQ8-fC8edt5UwDQMpoZB4K_Y3ICJbjVNxPSsztvXNycYslRMDAfeLGfU_5YF3eXuIXmlKLuHE92WTgLVLH6dcB9DQrSVa3NtkzwiaR3XDEtMW7IPzQPoiDCZpDDoHkuozeeMoSJ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/28905" target="_blank">📅 13:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28903">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6Vn4iS9lygqi6bfpQuij3Enq7SgH0sZBG5TANb5MgMdRQaYTIjVMTCxpjQGbnTmj_PgQJSfE9A3jnQPpCmuh7GbpALyL4Lpzpu_Hj4FRMUUVmeyRai0GAYVImFtT6gAG3C3ft1TKDJKWcVz-V_690-12lfJurUNrBjDbXWytZvEYaqhpSqYJfn-TFT9inKSR7PqEY6CUfr-MDStIst2XXF2DzyEMy3mRdI4D7MHKcstZwmVAVIJ51a7v_OhMNmfvsvikZZ6RMFm-RZV7fJ9ZGOvINsvQ7vp1gWN92__t0od0w8yEAbOjLm4pX7Vwn-CluSkKrf5WEOz-NtxZm3B6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از ۶ روز پیش که همتی گفت ارز به اندازه کافی داریم و توبازارمیریزم. ۱۷ هزارتومن رفته روی دلار.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28903" target="_blank">📅 13:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28902">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=I-8tfA9e--kTPemxXlpYQOw1tPMTULlQ3E_2XzTdocdTqESPODmY-lugDXXNg3Y2Uo7bOMfGWak7Ssp2eK5BU5CAFA71QcTUFjLfQGKauQhBDF1Z0OsT6shZJ8UNA5Xa9ndnaHJcYjQVAlLeOR06GnQjgA1cLcelVx0cchKYuiX7WpnFAwFuoZFXL7nMdMp6tz8DDZLlojqOM9dUZHYi4YmuFUBnqB5o78FMreVIofLqN8C-HBwZAoOj7gVfq5X_pR6ahqS0Txh0xBGxs904dcpCe6U0JSpHxfyfoag5tyXfEMV73yT4pKltTSUsCu2o0J13PiJL3Grl4r4D6as6OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c042e7e205.mp4?token=I-8tfA9e--kTPemxXlpYQOw1tPMTULlQ3E_2XzTdocdTqESPODmY-lugDXXNg3Y2Uo7bOMfGWak7Ssp2eK5BU5CAFA71QcTUFjLfQGKauQhBDF1Z0OsT6shZJ8UNA5Xa9ndnaHJcYjQVAlLeOR06GnQjgA1cLcelVx0cchKYuiX7WpnFAwFuoZFXL7nMdMp6tz8DDZLlojqOM9dUZHYi4YmuFUBnqB5o78FMreVIofLqN8C-HBwZAoOj7gVfq5X_pR6ahqS0Txh0xBGxs904dcpCe6U0JSpHxfyfoag5tyXfEMV73yT4pKltTSUsCu2o0J13PiJL3Grl4r4D6as6OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکرین شات بگیرید و نتیجه دیدار حساس امشب دو تیم استقلال
🆚
پرسپولیس رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28902" target="_blank">📅 12:45 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28901">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEZUPkaz-RpPuMcewGH4YhN1eysStEcLXxVzEafGnfmpVrpZLUguSpghscfNS-w3wpYDUKxWQpcWC1y8Da8tR0iUCuOJQ8cVe3gISMRADqfEQUWhzR8IztfOXDdOBla3Qz_99BE-ajSr-zsWUcOlHrPeLiPPkxF6LsSYmGy_ny1Lq3QRRYjlHkhOIMLLNkRvJwXx2Yrguiger74b4CCwqpzrm4OjQ1j7gt1OVDeAOr_Jg0UJM9MdAHU40TiDMIN7vz5yUH7lYBObcntcMp8PqRSt0t3L_3NLKNudQqIoD4M0TVKYXENzrdRHzfNzkyfy7O-aC9aXJasBX_zuzNA_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
گرانقیمت‌ترین‌انتقال‌های‌تاریخ‌فوتبال‌جهان؛ نیمار جونیور همچنان در صدر جدول؛ انزو اومد پنجم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28901" target="_blank">📅 12:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28900">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnmkOlozmdOvQ318lWejfEsUp4nMoVeVeBFX8aSb8zBMSFyq7AautaxoUiURox6wqbJ_GDiTg2kQvVU-ONFRJC096ckkAhl1hX-lV-UM1gHr3YQ4k-MmCf0yvb1Hy5kzv2DC5vNcoM5UBeFnsA4nBV7ctjtMDRTNfaCdSBetjZLr-irvIXP_LsL3XBTSok23-91NwRbCO3SmWBUleuP84XZMRlvA0st7UTMqF_qXEKwnQcg49I6gdUvG7Fy2kUUEQEkgG3QdNdTiEUTqKG41u4OJnxh3VexIHRxHcy4jpgGDaEPqFL2B3_PVYWpyDggNFaziMlOOumap6SKXAQ08zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌گرانقیمت‌ترین‌بازیکنان‌لیگ عراق اعلام شد که شرزود تمیروف مهاجم ازبکی‌سابق پرسپولیس با دریافت سالانه 1.2 میلیون یورو به گرانقیمت ترین بازیکن حال حاضر لیگ برتر عراق تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28900" target="_blank">📅 11:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28898">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7N0Q3kvEB7_EhxxOx54kS4dAcHDg8zqRT5xSIWsDRWap8RBoqvHIZM7X9vUHLrYCIwmGudseuRmH4cNHoEC4CuQjW1bgRBd8MMaP1Tbn05CRXZNuGF_0p8S5NvzqnTCNKXyXuzdN54U2X7-KJ2o8ajozAcbexANF_SjWtzlHz7zcyKFEFM_EeyqoghTD48OYtC4e6l7GBjSH1gIh0dgXjRU4SSftFVckOtaXp9VmJ5k2j-faMVXQtRWSxj5Y78ZPGKkGSk83u2Jl6eptmRGELJ6iFYCFjZvwhNnNUanAkAuJbF5moZNbe5uRUwD0Z6-Sjjw-YQgd7EUdxsz1fSfzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=hLb64tITr5FyzCyLZMYCZlYcBhtjj3NcUzfFEB6wucYjv-irE88b9tXdGn9QTlaC7ED0WwwXeFbKNQ_2huYTuwKVYN4IlROP9V4SnSR6453APTa_ws_C9RNr2bFp-RnCdxrZXRPaysLgHG2xbuw3F7PTO7ZEwiJQN_E0QLq81FpF2u40SeuWEwAD5v08-ETvqCiU9l1X_1TWqL6TWJVCae3_w9BhTS2jDn1LPZYHUtX-IP0m4B6Oc5byLFvQAItq-igM7K8CCMkBBZeHTFh4D6FAtNkATTwFSX8tI4gC7cz6EZ_NzTRRAyBzMEXY16x2q1CwbCPIWp_vRszkrekUzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a48b60637.mp4?token=hLb64tITr5FyzCyLZMYCZlYcBhtjj3NcUzfFEB6wucYjv-irE88b9tXdGn9QTlaC7ED0WwwXeFbKNQ_2huYTuwKVYN4IlROP9V4SnSR6453APTa_ws_C9RNr2bFp-RnCdxrZXRPaysLgHG2xbuw3F7PTO7ZEwiJQN_E0QLq81FpF2u40SeuWEwAD5v08-ETvqCiU9l1X_1TWqL6TWJVCae3_w9BhTS2jDn1LPZYHUtX-IP0m4B6Oc5byLFvQAItq-igM7K8CCMkBBZeHTFh4D6FAtNkATTwFSX8tI4gC7cz6EZ_NzTRRAyBzMEXY16x2q1CwbCPIWp_vRszkrekUzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
نظرت راجب آلوارز چیه؟ لامین یامال: ما دیشب ثابت کردیم که نیازی به مهاجم نوک نداریم و همین ترکیب برای دست یافتن به UCL کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/28898" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28897">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZQptj-zh94aWKzgyubudVoMp3X5-75n8jefDpTFo_n30gBqXAeO0FDzkDwh78SxHn2h3KrLmg16pKluQyViWIQy-ZewmbjiJ_o98i6JQoCGmdeb9kncG19CidxIZQreFskcGjzT4Zp9Hgfjz7UydOzRI3qONA5wH2Z3tXM_mFeInVDMeiS3zs3PhVCoovZuVOcqCkUg8p0VksH0Z0AQ2ZoGX-TXcxgXhi_ZjVc9D9DnhsR2iQkQl0-ZwGXlHELafL16-cH2U8D2_qNkZh2NZr51HQEOlyjntFpdcWTQm4TBBmc9vJVJk8q6SpwODC261zfZuoO_wOR1e11nkZ1AgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه‌باشگاه استقلال این هفته با عزیز گانیف ستاره خط میانی ازبکستان قرارداد امضا کنه بازگشت داکنز نازون به جمع آبی‌‌ها منتفی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28897" target="_blank">📅 11:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28896">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siczA1n9yJl4A9DSjHHYkAiOFm3UCIkjvZuP1rDvy4UYUduNa7-bz1wWVeJhdZuj4-BaTyCDizU0emPp8O8jSCSW4Z-S9GL3ful6rc8ogeLVqqWj7WmciUp1p3bV7jpCuAwlTNLPPC8K5VXVsgz4-L2UE3EU3tSr4KzGgLUoTgRNHarR6IbCfmfwTFCVz6guxUqdk_eFDwjqR-rs4OoNsEwwt3skUfBJJPmK-_Cjz1VERJJAfIqi21HSWHYPeQj6LtQwDVlp1H7XA5jDRz-3s68i47veGHkXGpqx0s46RywmOI0PbGhtKSQ2DrjQnyXkaiqfkQxHKkC-39D1gBGziw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دو شماتیک ترکیب احتمالی از استقلال و پرسپولیس که به احتمال فراوان فردا کادر فنی دو تیم با ترکیب‌ها به میدان خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28896" target="_blank">📅 11:00 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28894">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOp1mCHvKZlEI9-NQLLiTfi6AbjGuEVj0NA_qq49ZE9EPi89LNAk-H7acHcLdt3M4Y97TFmf0bpHocwBxJmyOBPRzMnwWMtGYs1TZ0PDgs5JRdklkbgRKG4TnA9ZsZQa1r94cMvq5NSL71nh1mxrSomtMMX91pK5BwXCUUFCUeOkeqSN8DocW8XxcETdNOJiJcImElK06CfFaWl9Raq3K1UCY9jRh-qtlSyIeKNm_oZzPNYOJElUnEPgVyfWi12HckLUzxR-v9k7Xb0eEqMriHdQ7548X8KwY59IXp9icF6EZW4d-B2y5yQqDPd_VBaKSIGsduzXwZUNNM4iG-cT6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSpnA9vg5B7jpORDbUvEWXWC_tXV2bvA-o10jERmWXIOpbsJap6KoJdArES5ALfuoKqhi8GB0pxAkHq5m3fGByisu010Gz71187Fcj47ANuFhGGWbxo9yp2loG3c7vfIoqY3y140cuMgRaB5Id49qoalTRaE3lODtk9tLVjvy24IU3fJTFByRAs2hEO15vZHmW35LHaGbemhzQNOSfBpP79HgLCDRXo30Jx72sKjiJeFVTtbOzhWec4MnnJmPo3X1UjOAM502UalLsmSb2LWc6cmbtXUqCxp6UoiLTXVUy9iu357RfCec4TH8EEkKhKbdyPrKkxvjimx0AVXYn8zYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/28894" target="_blank">📅 03:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28892">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBAXezJXU3HGlB8Wf6IgzQMRWdouGZ9aSAItJdV5mb6NdYHps5HRqoYRA0ZR8dqrQrvO7aRAbkUfpziDRju6sMhaK8gtKFBZ2MpZ5dhX6VrWB4TXU3hN24e0idJczrd99rYT6d_d-7AFTOjWaLPT24HdCQEEIkaswfxWC7Zn4aLnoYATSKRfNGudUS0XWoqcDQf1HYln47269rD5STyiBzzmKufXv5-3fwjG7zIqOVY5RSYBQ__YfXjJ5TCSxi3L9lqKn2jl0BcVtfv7U2DReR_AyD_jUjvdN0FaHx4I7Tr1NIPPv1b9sWbxeeAe8HzIYcLxreH33TzsZ49WW43akw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/28892" target="_blank">📅 02:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28891">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=QZD8hrRcJUB9fUl-PyDTKI7T9PmFtOAuuZYSzj0TF1SNLIt42MaSNB8ul0ukg4aia5ZDMf4oesWZs_nEwHIBsm88ZpGgctRlEMWK8lzXH3LmnS2zrE00mKT8xW3R0fP-1Kku5QQWEnilkY1xuYuTJwx7ruxV_CsaolRNZkGZzNHCphOYEA8se3uOG8S1ABoRHBVyYEHoCxQavcUej1Ld0Bf96vtRgswWT4-xo6UKx00C3Ni5tahAkq7MndHoHDgKY5wEH9nGizRSa89MeJI4cQ8rCsLQvEg4g2CGnQBd3GAC7ebwGPXQ6fM4s7HUfGE_bwXS20bmPZu7T1Ojmw-a3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfb2092e5.mp4?token=QZD8hrRcJUB9fUl-PyDTKI7T9PmFtOAuuZYSzj0TF1SNLIt42MaSNB8ul0ukg4aia5ZDMf4oesWZs_nEwHIBsm88ZpGgctRlEMWK8lzXH3LmnS2zrE00mKT8xW3R0fP-1Kku5QQWEnilkY1xuYuTJwx7ruxV_CsaolRNZkGZzNHCphOYEA8se3uOG8S1ABoRHBVyYEHoCxQavcUej1Ld0Bf96vtRgswWT4-xo6UKx00C3Ni5tahAkq7MndHoHDgKY5wEH9nGizRSa89MeJI4cQ8rCsLQvEg4g2CGnQBd3GAC7ebwGPXQ6fM4s7HUfGE_bwXS20bmPZu7T1Ojmw-a3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار!
شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28891" target="_blank">📅 01:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28890">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxL04w7WDmFuuwf5uibTBaT3OqlJmErf_H_iIRqGu5YUwz9wdmQO8uBWh14QiaomcrELPRjAcmyRNno6K3W6dTZaNbc9BEfNjTx0fX_erjBgiVq6zevWGZNSCJJ55kfxDdm0CeVsBq6RF1FHhbhvJMVxd-Io7bD3g_Csjb9trAqmgKDqwtrOqNI3uDYvVRbvNhfyfCJhY37HvF3iBKK4XPE4cSxbBPT8dUCrM_cL2NES4nNflBpIASY12gQQDrGObnN6lqIOEZUfX_025r7EPkyYEhvdt87w6rKj_4MqQjsh-qpQoWMmWQ5SZ4S0H7vAeEACzUHe9ewkO55rvhjwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ دربی شماره 107 با جدال حساس استقلال و پرسپولیس در شهر اصفهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28890" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28889">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNdBoiIFcvxMN_Ov-EIKdolsbe0n6NphzRmbNIhIrTz6g0HSvXFhcXFgewPgfsPGP4apREJx_IyCrMhA2r1lQ5toKFJiCphFtRWW2BXRzCggl5b4QB-Jah3Ppt4vYss5dP6q_3DYYxDie7hGt5I44jSS7hpmS2Gx0cSRjAAq8BI5rW8UBhw-fyACC7WUpMUmtislBF_JGcNo7uyhZUg-jLiHS2u2_tUAUt4IReN3eGc42fD8lzg8Onsn0qkEdKpYL8uZswfhG8AcmsMj1SPgOw3NBd4F8gXKJqorLrwZhdRMezaxOKsecioP1a6-GXh_jNKuBvmjlr3Ms18x-Vax8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدار های‌‌‌ دیروز؛
ادامه روند بسته‌ ماندن دروازه تراکتور در این فصل و برد قاطع الهلالی‌ها در شب گلزنی تازه‌واردها؛ واتکینز نیومده گلزنی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28889" target="_blank">📅 00:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28888">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciOoJdZqp530L1QewCzxaViLv8zSXV7Y_RwK28fMMwX0TiN2jyGtbv9O2cMaheKjg0LOUzPQtpd1mWdVzCT_wgEnfSXdkDUTaP8HsYTL54DOi1WtZWPjG-N83mQKTXoN5BT4Bz2eTyaoAsV-OWmDRNB3DYX68IRIps6-zdlB6uHgx2YFzcO7Wmu-b7yNu-LYBme1BkGw2vyrD6kkKhY9SBwCpUKyclE7CB_M_-qsVWPTPaz3MHLJxzkvHM-xQ2hwh7un6dSpiBD0pu5SnVKw1YP8d25HggkEeeHg0_qK7AZ4gnjhJ8fCv8lhmQoDx7s2kwJOJLXGdXau3tPGvoW7SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
بعداز دست‌دادن‌فصل توسط ترابی؛ شهریار مغانلو و امیرحسین حسین‌زاده دو ستاره پرشورها در حاشیه دیدار امروز با شمس آذر نیز مصدوم شدند و میزان دقیق دوری آن‌ها از میادین مشخص نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28888" target="_blank">📅 00:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28887">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv6ZB78QB5DuTWvKhBpN2_nvFh0lGg-OVMMe5qlIw34LtYKpFKhwGmB4ppgi4S6m2tRn0R9ozmwkI74u6fYt64mw13UThrpXAiMJScZN9wfrHqHkkYfm5gFrn0_8xgcSRGIiZHRFG98-7h0nOrNjJEk0yg5Ga7BV2rHnTjr3YA3QlNgrFrUFWr-WwMfkMdkMR2SRHuYVgSo_taw_Ys_4vlbQywUmXnXrdIh_eCuiOPCGVRNTlFis_apWGjVG6sppHuoCZDkVeaV-gGHiWzOXc5CW_6b4rAohiSbCLvKTMoj38H8pYjU96Q_NS8bbRS9HMJX9KbtOq2QACL8tb9YVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/28887" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28886">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpAQQKH-GVzsg6HZJAqStPVdf59osBn6RijLOe7tSHwCUpAtZ-gFlrGnYjY3vXl2O6l3XKRxbmfK0b4MoAQKRpStU5-TptAZ-GZuoE3d4WJx1hntomWv2gDSGZws_WRuAoq2m1gSqZD9iIELej4vJsYa_tP03P_3rOvWiNxv2TrU-WlvM0uOphhKGdVMJ10qBVcDfJfegdZh6-Ld1204ocPybcbSHJAmk7_rDeOJLXDcI7KZOnqZbLBYNQ7Kt-EzmYNqKhzmdbL5jCJNvoUrBY-2Nzwi436xzgpPI4XDJRRU_h04hfTV7Aman88FT94Ss3qSh8GSJgbIH5-CQyLHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
لامین کامارا هافبک دفاعی 22 ساله موناکو با عقدقراردادی‌بلندمدت به‌چلسی پیوست. آبی‌های لندن برای این انتقال 65 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28886" target="_blank">📅 23:57 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28885">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GsReSTbNSQmE0JbWMDJOGAMboefhpJ2-vCCfN1jgh2N65b0_tF9-Di7cziTUX2CQbjWpiI6XRcY5gjdy-zxoQl9tIhTgkrzlnQPNNJTKCOgVMwQs0QEn-SwDvFadJcdqYZCOXUoJ-m1CFKugEpo5LPrnFFqGvivj3eLvzAAWvK-iFY97DWNc5vWLG89WUV_jrOOdcVAKecT1AalI8aV_P8u_Ifmp4tnb76Sl3C-31-HAtZicurDXi1eWp2P2kxcn_ACo2bQs8MdZTJfsP3F4u9HIrQcF9P8sV0crlsUGbLz2ihF1Mx6UvUemcPuHzTIBB5JlchVu0YBV3BjiMQuJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره "9" های بارسلونا از فصل 2004 تا کنون؛ گابریل ژسوس صاحب جدید شماره 9 آبی اناری‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28885" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28884">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFFNUVb6Ny_ZmTFIuwoUNfYusquKWYlSl-q_S28J5PlY0I8rz98udn3c0Gq8ks9ttqmy5cXPT5pk1RFncm4tS56jBeK39WUlSFgyMGOKp9JanKG9xwU_g5Bq3_sWtBmzRr83fHMSdq3SJDapknjU-WquXAa5BsJYhnnAEycaO3NSZ39cWiMmrhbspzCo8ochmGKJfhpRaoZ0HRspRSvA87SThvT12EunDH-8wfytCe_rUAK6Yzf_Eiiyi12zYj_cqMgVqgna6pkMMcyQB4XZtPSaYEpVMvwk6rWjAwETizQTu-d5UGlidZg8HYfcNruusHfKnpSsNNRmDK6EyaiOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس برای دیدار حساس فردا مقابل تیم استقلال در هفته پنجم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28884" target="_blank">📅 23:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28883">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XL8ZJWE1HN0R_PDYlRm2tWTCbSi8lpUIHBS8bzlz9ee0MwCrzR0iti1YubUoyrYoRDkWZHVAh7xrfStj_8VdSbFOT0E14TflHfAdr7bINmidgFWnA-I5EXwpAihsLvBlRT2YUKkITgGMi33qxNnIRaLFSAVyfcr3ebbmfZpdr1zo5CFcbJt91E3bFP4mM-nsH5f36OzW3kwMPojLKVjzZo7u2NnYvgdBW6aYL3UDwMP0xATbVQ3wycn5SzUYsmQDz5quKD7rhFzfPR3qaDEvRMZJgnZHV9ONETuBNWajRloj2JzhQO3Mni4x3bSYyfHhfWU9Y0k3lrv5Bbk3sH_ZKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#فوری؛ با اعلام رومانو؛ انزو فرناندز ستاره آرژانتینی چلسی با عقدقراردادی تا سال 2032 رسما به منچسترسیتی پیوست. سران سیتی 125 میلیون پوند برای جذب انزو به چلسی پرداخت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28883" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28882">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghoUyIJGENPBRJHWW2Xjx_MHbqMDYpYCltMYoiQemS9dCRDMCsOFiULngyKO1NbH7xVRhzc_6WKP9njbMiXj82otTYsYsNTG3pIt-0ty63PRKjFpiD47Sp0QCbNrJDrgL4jJVdQzC8HkjTaEy9fi6uQnAMBWuT9Upwg_uAK3cByYpS51EkUMtE1WcdWXJ13Fr1qyIeNLXV49d5ddxTUkRNtUVlHIJtQN7oJvAUXa3KfWc29z2tIGeFmJs_-mO2qiuUcl1ft-IFsP0nQqDiaGw3hqSsSSuGdh5p0Xz2ux8lf8SskG3JsrKPHd8Z0Kxw9x69azBYWKZVaCJj8lwKFbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
به‌مناسبت‌مسابقه فردا؛
10 گلزن برتر تاریخ دربی تهران؛ علی‌علیپور تنها بازیکنی از این لیست که همچنان شانس گلزنی مجدد در این دیدار را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28882" target="_blank">📅 22:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28881">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ttTYWs0cqilLnY0Ujs2pS91XtMXGnLZR1fi-noGSCkAM2YX3IuRNGAlXh22-Y7FBXO_CeTLKxUzJs3U83czFlGvi7vaCY1EPfXYMsC0Rf3nJdkLr-B3C6Hf49cE9nXH-bjqXub8xavl2bA8mwWdzGBdtrKUS4SACRXiz6qfPV2NNpUN2__aHMfnx1S-Sy057v8yvO87cTvik2qu7G2CtqObRPDtE3vbKGC-6awkmY36VOYVUbS0TW_HCMVEZF81gKqAOwE1EZAvBiAjzcoh0j-cv2v6elMI5cOWm_SthFpKvYAle1lcC81wcuJ0yRnzjyl2rn2noJkas8gWxo1CTMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/28881" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28880">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=Nytjq8Qv56jMRFfRvSrlyGf58sOZsiizhFeJpigXdHLlP5oLvCebEaHSwtv8o_ZYnXVECHzf-tbZN8fTL_BEMVuvN2r44yDi2US_GcCogemhcuOFmHmr5PcC3gJ-YN8ehnevHfwaxp2hFQSjos7j96vlquKy1Ycbv0vsC32o5MxeWhv5OMr6z9c8mBnPTCI_O7LNd40x-0vrtN-qcUlh2IXw24U3uNVTlWoxYOREUawgRPdea3INYXhnPZcbokIq6erajKyIkviOHq1H1iL-QK0UbRte45B2mmC6DRikys83DszpbU0Iiq7_aaAPLjdptl5kA1BdIalWf3g5Au1KLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b85bfda8fc.mp4?token=Nytjq8Qv56jMRFfRvSrlyGf58sOZsiizhFeJpigXdHLlP5oLvCebEaHSwtv8o_ZYnXVECHzf-tbZN8fTL_BEMVuvN2r44yDi2US_GcCogemhcuOFmHmr5PcC3gJ-YN8ehnevHfwaxp2hFQSjos7j96vlquKy1Ycbv0vsC32o5MxeWhv5OMr6z9c8mBnPTCI_O7LNd40x-0vrtN-qcUlh2IXw24U3uNVTlWoxYOREUawgRPdea3INYXhnPZcbokIq6erajKyIkviOHq1H1iL-QK0UbRte45B2mmC6DRikys83DszpbU0Iiq7_aaAPLjdptl5kA1BdIalWf3g5Au1KLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
الان رونبینیدکه بازیکنانِ ایتالیایی عرضه‌ی صعود به جام جهانی هم ندارن، یه زمانی وقتی می‌خواستی مقابلِ این‌تیم‌بازی‌کنی تنهاتاکتیک و راهت دعا کردن و کمک خواستن‌ازخدابود! به معنای‌واقعی‌رقباشون برای سلامتی ورزش میکردند. این ویدیو رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28880" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28879">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQ4O9oQZ2MqLogVTJManta7FzpHlWfnzdQU6ZcXC1ACqGV54Q2DiyzzlPF4S4-sn6MIJ89_MzvCGvF4ZdihOpEc6HzMVSTAkMGez-xjSxJ3k4koR3CTHrzLWp1lzQFmp8uAta55EY2AqtMvaiYb3tGszz-fIvrkEskbyV7ggSjdnLIAR_xEOFX0PtmBSvtrF4bH_vuaP5kjOsEmcXg8mNv3MGB7cyl0yx7BAHV3Uo0vS04JAJSUBZEGpLSfZ4m_JwzhOqAFJPmJfEHocqN-ut2uO8b5osqcHl-RPXnujMRnEHmLQyvDCW5BcemwXzgpYHB0NOwwjtH53hkPbZsi5xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
به‌ درخواست ژوزه‌ مورینیو؛ باشگاه رئال مادرید قرارداد دنی‌سبایوس رو رسما فسخ‌ کرد و این بازیکن بعد از چند فصل حضور در این تیم جدا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28879" target="_blank">📅 21:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28878">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-nKBK0V35tuaxY7Vp8kpY_Ue1As8JlOgeAfsOWNlLV4N4A8ULBcA0HdKzqyWqeRzMGG1KotFKfOhTMEQ9dAr7wa1ymlxOZXf160slzSICjO9B2c7Akj5uHK1uVfu1Idmq5E0HXklPhVNyUyPGgHRqIGNAvp2t8eK3rZc3_LRVwRRh4R6jFGKttDc48jxygItNB2-IzOLuLOStLcYlGfkTsPdLXfMpKCx9Q5k6kor5oCln6Y28EmubDwfysC3ok15cQHb3YV0g_79uSQB_rkMbiVFt-_lOYcQKIV3sTsdKp6YU4VUkwylXtI5gzo67eh6NjnU2b8f21mYvys9uyb7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر
؛ توقف شاگردان جواد نکونام  مقابل نماینده قزوین ایستگاه پنجم به کام بقیه رقبا.
🟢
شمس آذر
0️⃣
-
0️⃣
تراکتور
🔴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28878" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28877">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=jTfZXAY7ZlT41xd1cJshcl5IhRM8PIR77914DW1T96KW9M8oGzCwjbNtQ6u1bo0-hhsUmXG-KmnV2BwdzS4EM_Q2V84IR-47GGW4s9O_y_ahRkXS2CJ0Bxo78J-hrmEYyswSSbTzwzR2EKLu0MFT2RYTB69fzCvoL5xVM6PJ0-jjH2rCGdDDzBNuH3nZrhF5SDe41CzZ-07VGwibx1AqjmzSJuge6k3vhMq_HLGtLPhWNeqHgsicm3dwmAQja3ifhES4bGT8MIXG-M80y0xIhuOB7T_t1imB1vOG69p7o7q3fHK-T_gGHgRxZsjQUQLq6wbhp2EVvHd_wI1wFMH6Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af26bce4b8.mp4?token=jTfZXAY7ZlT41xd1cJshcl5IhRM8PIR77914DW1T96KW9M8oGzCwjbNtQ6u1bo0-hhsUmXG-KmnV2BwdzS4EM_Q2V84IR-47GGW4s9O_y_ahRkXS2CJ0Bxo78J-hrmEYyswSSbTzwzR2EKLu0MFT2RYTB69fzCvoL5xVM6PJ0-jjH2rCGdDDzBNuH3nZrhF5SDe41CzZ-07VGwibx1AqjmzSJuge6k3vhMq_HLGtLPhWNeqHgsicm3dwmAQja3ifhES4bGT8MIXG-M80y0xIhuOB7T_t1imB1vOG69p7o7q3fHK-T_gGHgRxZsjQUQLq6wbhp2EVvHd_wI1wFMH6Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نشریه‌‌بیلد: هکتور فورت برای پیوستن به‌‌‌بورسیا دورتموند به توافق رسیده بود اما مخااالفت پارتنر فورت برای زندگی در آلمان باعث شد که ستاره جوان بارساییا قید حضور در دورتموند رو بزنه و با قراردادی سه ساله به تیم رئال سوسیداد بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28877" target="_blank">📅 21:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28875">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHfBQM7eGUmQxi2lJDFck6fMQfLo_uMFvHd0piIbclxgV7OU6Mc8JuuB_WMpdCWFpmCwFl2HWwAKkGmBwiJEitMmG0CcTEFjf4TN9y5tWcMaM0JlnIb34dfVBJAvxQo1_gioGMWo8eWAQAFM7w8yjkvrh4ms5vFeGS876oJ07-E6Pi5W1x7rnK5UL6uaDbw_6sfypb5BZOTh-NVlk2pclPEIELA4loPvpd_RT0ikE_k13Q5XUr0s9BLHKkWlGk0m2fBtE2nfJFz_IjXroMxg-2fI6jdmOItaTqDh815C6gCQlu-xl98Fdug5-7X0BtMGz4Hv3UWYZ56ooqlJP1Kicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28875" target="_blank">📅 20:39 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28874">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGYVNp39NW_3UKMviolwpEZ-Bc9EM0xtAeOoD4j95AxwTGHGeZ-ID1ivBkf0iJMYRaeackEiuVenK4UheAQaGwi-tu6R57g7H8Cd5QNToGSOMyHvuYlr76aIzTFqm28way7QXQ7h_bZEbBOOl2ka_lM-9HQPTEJ-zBpXvadJPKbQKi5u9fFQhjUpo4Vn7N78NUQKtRSmBuIifILF1OMGndSeNyks-aTWSYzgfqYUpy0WeH_sPSq1hKofvoIlfttdmAAOwFwurLap8z9divqaJveagB3BNTKDTP2w-AQ97VSJxpnqCTSXgwGQz5P9r2OYVK73iPngSa41ShuKeeOBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خبرنگا رسمی باشگاه چلسی که گفته مطمئن هستم با ژابی آلونسو قهرمان لیگ برتر میشیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28874" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28873">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RhwA2ail3VYdQSXmAhAeHSe_GOivpeu7ecN3jeC3lidZW2-HozdpQTAAduLB5i_KP_mY24DUGC_LwUp5T2lAC1_jJKhtI_ARClhjcuPljdsvY59JhewFXG8hV7powNNSuw8T_A2OHuSfh9hYzOef4rvBPcukptTH8QP6Kv7HwONP9s9_r9-ON7LtCKOz-eX4ItC9K8F2fayfoHkIlkFDCvLEgk2W0LTDo6SeyjtLT1FoamSTDYmdqie95UrRNL3jR1PANXSwQPrwp7Gwt9-YWPMXY7kbUe-eh0tYnQqZtIlFSdBSrD7ojxhYBVjd2G941LWCQsi7NyCOZF_t1NulHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28873" target="_blank">📅 19:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28872">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3NT7pL4oj0yjJ4FzHOvaj679Oy5J_slQ_2Wuf6t2X4LEotZ7A_gnfspNcTiJF-4_ntx0zuEFCPNCDHoYW97jyqZRvvHBYlhb6SqcvlDxYi-NeAnLK1Rm82ltYyVV5c1PsDIidmMTrDKWwNleeSRRe34jvYRQthiZ7iEZvyYEe8YazFCBp4DX9evBf4pFw0ySc8ezIFJ1RwhAVd2apbhulsgd_-5K5A0UxLfbm_bBfc6Lwop5k0o2ViwWMIny29MSpW7n3gWu7BsWKLHnInvUJiMeg0bFRs8tBzi0XYvZ9nLH9KDMjwyzqHj3biJiJ_f5ejFKkAs3sR8JtQVBli-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ تا ساعات آینده انزو فرناندز ستاره آرژانتینی تیم‌چلسی با عقدقراردادی تا سال 2031 به منچسترسیتی خواهد پیوست. بند فسخ قرارداد انزو در منچستر سیتی 100 میلیون یورو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28872" target="_blank">📅 19:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28870">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mOaxt2VVEncT5TDiJQ3Pw9wNou49dqqjr5HBHLM5Yt526fmryOslhMJsUBvYRHjmNiDKXjDELyDdUa_5vpqggPZ509xcVSUWvyBpxBoWzxS3nOrYS7xiNceB0H29RKV-5jCDfsVkMcGpu1Z7sGHNoc9M_az8VgLIWT7HXTgUVa5wXFkQSdfohzK4475hlKmzm_hRpi7TfO9wRYg5Gm_qphGAlfUX6eE5cCrN56yy06fNKNHUG1n3jM1x-yTQhHhDFREZlsP2Xh3EtRMSnUZwausxA2fWIiP5Fgs4kM8nCi5QvIprOI_6Eychu4XiiVrJIwhS4A79vH5OT_WxIhdEVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aftBcYinEbw5Wbrd12b8e4vs8yeOnEDhuFdecLL9VHC8SzsTT9DERWZRuakC6gA_CJ6HkTYgmlMFLCvh_opscHvPez-zvMq2cZGbS6CztXMuc4U9es-HnRVTuwh4B47cKBDvwINaUDcB3wSLQh4VTmrXT-C3Xpwgmz45db7oPGmXe39P1PjShxgEO20uhZYApuXa-3UOusX5BEs2NXf3nR_K6r7NC4FnMin8Hy1uKchA_uYborGfDTCNxtGJUsffaHGPSbiYqriCtqrTVZkBOFlKjktoBApUeuDQrUIr5vQCnRcJwWf2quxEqGl8fz8Jk3nlz3qdu2vo3nLvNHqTLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📱
کاپل‌های‌ فوتبالی که رکورددار بیشترین تعداد دنبال‌کننده دراینستاگرام هستند؛ امباپه در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28870" target="_blank">📅 19:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28869">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XC5W3iqk1pq57st_SO6EXCujqqrCkxUJsOvypO29lzCOiHAp4QVit6dzSv2wZqiE7PH-1bFXOWF3HuHn0bDY7s3HWQHuvlyI4hX9SS0ZTPiCEnwD4DsfTG8dqFBezXzTJ-aDXgmy9wt9dQc31PJbP6UFW4eVnPLXHOw6oDfe8aGDV3cAm0YW4-B-hQskd79VBNmhZI-CKQnDIDOmvLAaNLrwd6OnlSUfNsC0NBkmxAfpJwZjBBuTde0WR6G87GS0SQ3xQ0qupu_vd1NEUL6aMcTuOgjKZahsy1HoFojCl1_nEf2q2ELy0xKBmzjAIAz1Rcy6PSkh1q_CwVusWNuzFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28869" target="_blank">📅 18:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28868">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQri4kgfPq7b5NnMlKhWBN2KSOr9o_SdRBWnmrMkX8Ue2CuuEaSxoqtQn1pwaqPcr4EXtNNpbetoE8cjsrLwZDua7GIkUn73Mr13XsJxqxbmOlRts2OH7ClBu1H15GLxswvNNOARZxcOwcA5RCRP1f_aWUV5AmRAkmmQr_5MISp2Ti6LXEapcwxbyjX8Ek4zEuaB1_I4XG6jbxPwtMHJK3X-hGyH6LUJQFDICNalCYI1xWgTyuvIoKycDL7Y3F9z89LlkgclJH6uEXEcpbLEZvSGtVSYif1p488trlnwlKrVUxM2_im9QZzHZUH6L3NYx8zpYMXGuaruFy8N4SGhuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇫🇷
#تقویم
؛ سال 2017 در چنین روزی؛
کیلیان‌ امباپه باعقدقراردادی قرضی همراه بابند خرید دائمی به PSG پیوست و با به ثمر رساندن 256 گل زده با اختلاف‌بعنوان‌بهترین گلزن تاریخ PSG تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28868" target="_blank">📅 18:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28867">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoJLrPTobfCus1c3zrS6oLiKWeDh4lh9JbJgOEiLcbu_ZrqZxqh4iUPXKtjjdlzDlGfpV9NCjy9t23wpQVmqS-utuUUeJYV0TwUN_K65nSqhJJCN5JUJ2gItot_w8Ok8VBsYNOgKgnJ0arWakgpr_1ZypX_Ti5i-V2-nHT6crrBM1x6SinpuAi-arZaXNMZPQFITB9GSt6a55x5UxXNsSvXk3spymYP_bXbS0RWFcmGlDh6zlwfiRDa8agbpaMOTxR2Iq-tGyVvktBKG31SdPxC3ylQiY4rjx5pZDkNOHerppVqNhdB2mct3oMyFUHnY0p2fPsCNHhfPy36qfpB38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌برتر؛
شماتیک ترکیب تراکتور برای دیدار با شمس آذر؛ ساعت 19:15 از شبکه ورزش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28867" target="_blank">📅 18:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28866">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrGeN3ammwdloaD6cOeDBgJDhKnsK6dQMF5icqjFcYLSkzd7CXMwtkN8Ih6Jhkk7VteodNXSKzeANENSy_2zqrwt-bSnH2tdskgpS2DNUviIH2pme1YopeAQ9eIi1XBu7WywKDsLPuUVrOOrFW6S5FiTtpuVdP2OmXEHmhONGoPqlpRt79_zH9iOOaF5jGPBe27_rTPKZtNxrEyYrzoMwJkNPTtiOIRJu_rd4h9yPsTLuCNvRo6gge2ZEyAgbzhBEN0jfzi1fgaalTCNEoyCbks-CBo09OtAZTDKdwEveeJdHB9mXwRRHCBhgK6G3OxB16CyKJGg8W-UOMh6nAQx7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و…</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28866" target="_blank">📅 18:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28865">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thytvCj_Az6TOe4wHxZQySopQEOtbgKUJKw6ZHrPYgjpzSIxXx4Zn2t6dTjcJDhVGqT3ZMz_0KTMZVC_gXZMv-fGMohrR8kOcFEaKngzQtFzKcW_sTHV5lfwhBVhAFA6s9vsz6ZsJXR3vTXn6SW68SVI4yw75CZSyEXMNz8FOi7Ytd30svNVuQdxRwQ02TjYf9_6MOv2puWmBP0-AZSVo9kw1XTV3Vo3qkutVaBVbBUrXFe6VToJGquyajE8cBVvUYqcfe1kQNpwpbcDGBQZwI8dZWA_2i9xjA0QgYOVPDVT_OlB5yUWmUEh-b810TA3IQ6lFEqeqskEblnQfWQj0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگار نه انگار فردابزرگترین‌بازی باشگاهی ایران قراره برگزار بشه. نه تو مدیا، نه کف خیابون نه بین مردم‌هیچ‌اثری‌ازدربی‌نیست. خیلی‌ها حتی نمیدونن فردا بازیه. مسابقه‌ای که از چند وقت قبل از سوت آغازش سوژه اجتماعی بود الان رنگ و بویی نداره. فوتبال، استقلال و پرسپولیس به بی اهمیت ترین موضوع‌بین‌مردم‌تبدیل‌شده و این‌حجم از بی‌تفاوتی قابلیت ثبت در تاریخ برای نسل‌های بعدی رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28865" target="_blank">📅 17:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28864">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57ae770053.mp4?token=Qy7B1em6o_zvtqBLdhWOwwoLd2Fn_QCSVhtEr4UMHVPb7_N1-k05BbxKVejlvNq9fLSQWIMSHMHZUgNDBN5mLoX6Rlal1FABQKo1QXiftCK2jxTFxa01oVaWuVOQQSiTwIftYs1aQkyMYtmumIlLJKnahC5Swo3wd9HPxlLydUPBHCArj0xpNfM6i2zOa-fgTNWxW-0tmN8hHyHU-sgOZ2I58vazi4kmgKzs6y1fVt3l4E_BywCsg8ZpoQpiSBDNbai5KqjNyfLX1Av3uA7iFjZVblea5AB59t-vu4bSrNFGppoF-J_8g6R4Xel6WkazeOYrGJWMV9_CxdcrUk9X_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57ae770053.mp4?token=Qy7B1em6o_zvtqBLdhWOwwoLd2Fn_QCSVhtEr4UMHVPb7_N1-k05BbxKVejlvNq9fLSQWIMSHMHZUgNDBN5mLoX6Rlal1FABQKo1QXiftCK2jxTFxa01oVaWuVOQQSiTwIftYs1aQkyMYtmumIlLJKnahC5Swo3wd9HPxlLydUPBHCArj0xpNfM6i2zOa-fgTNWxW-0tmN8hHyHU-sgOZ2I58vazi4kmgKzs6y1fVt3l4E_BywCsg8ZpoQpiSBDNbai5KqjNyfLX1Av3uA7iFjZVblea5AB59t-vu4bSrNFGppoF-J_8g6R4Xel6WkazeOYrGJWMV9_CxdcrUk9X_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل بخودی های فصل جدید لیگ برتر تا پیش از شروع هفته پنجم؛ هر هفته گل بخودی داشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28864" target="_blank">📅 17:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28863">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qT6GxEMVmyCyKuF0cOmCWsVr8xTLIYUS3Bg6pcWewfT4dNsZFBStB9AQcDMzUPs0J-0s6JAO954_cQwO6VHzjWEOi_mOQU2Tgx5ZJ_pks313Jf2Te2xyVseGRl7SFDngan8fO_Z-5_ebN0iE_5c-kvVs-4hltocJgCwMdO_zXEerL11d09mV_Mi6rj4DPXALiDovYqi2iurkAgTBzy92vwpbc0wccPZyRlDc5g8Nc0M7aMU8ij6-HAor4XDYNT6finllJvjx3Tnp18l9_O-dINo7EDO5q6R2ZjtJHvzC_hKqEOrw7CuIuSqhuDhnX8kGtOO_6e4_t10h_Wq7uia-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بااعلام‌باشگاه‌بارسا؛گابریل‌ژسوس‌مهاجم 29 ساله برزیلی با قراردادی تا سال 2029 به این تیم پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28863" target="_blank">📅 17:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28861">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvqDJg-CuPKQ_dNbLm-0Jpe0LlIgrDi-tN8w8xJS5AVPGlLOYkIMR91prgiL3g1o_Mz_3p8PVw1GN4SZ-NoznpWtL3sWqrGay3cYpA09Wuian_DqU4hzfJsFTVRavMG77RjMpInP9PAiIrQO65y4LVce3xVlrTXXb6Y-R_rtNmCO2kFRoG5ZCdR96BlUrbfWHP2tH0viwNiTqHWOYpqKhK6CuHsCKgRlzimVZxQlHEzaU0FIix7ZDWzBbUdtLhE3ichetoSAgGuyz4rbu1vLEj7mzuoHHSwh3o5NbzKCPQka470IS5MID3KfiJ_3_iMG0h1s8aarwtwpZMSA3bMObw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D26dM0rlQ7u4J6x3baGkdlkX2hC6lRM8ulsAb1moz16rGF_lIquS95zThzuBqsyY6_yshj2MnWCpXyVtQHmNtC84KPBs-MsUl_eAhii4_HJtl13zrKeE-btN9ylOC_maMvtNG-r031itNzqr5Dy6AI3RI_pZABwsGGfP6tq68zOfecLq80vTajdjBJUd1QN0wrGv6iQ5hoNTrgIA-aISsS_Vhox_H1gu4fYpn4LgIv0S-8yzjzOus1Y55SHiZvcVRC88HjQHUHLNlsgTvp6WS7p7CJR9dNjwSI0lB2hrExXFQKrWvLnDeWPYAwWi2uTxk3KYpaZGWkpvON_O-JVIPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
خبرنگار رسمی باشگاه‌شباب‌الاهلی امارات هستند که از نگاه‌او سعید عزت‌اللهی بهترین بازیکن این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/28861" target="_blank">📅 16:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28860">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJf2O9qT6999Earek2IIUOI_ugpnOb0d8ZI_dRfvNYaIxoIDFpRQ-p2LvCCr5rdRYv8foAppOz8ZOGvaJn-8K6fGlX7LewxG2dhd4BzxASCrER8G4Lb5C-4nL19SC-QNnQtndfeilp6y1hys33XECUTbw7bEa3JoE_KevWU1q-iPm-XBeds64rVjWfE9Kpijw-Od8CH1TqzfiiuNGAewKBggX8cHyYXca9zZl6wmtrA3ozxoUAfY7KkDg8WLmmRbdm6rUYvxT9JUnW75dbB68YN-HmzIFW1qZtLBaqduyXv0EPXSODrRpPg_s_nPBdDnM-BL25Dqbklum_y4v9TrCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ قرارداد ژسوس با بارسلونا قطعی و دو ساله توافق‌شده. سران‌بارسا10 میلیون یورو بابت این انتقال به باشگاه ارسنال پرداخت خواهد کرد. تا کنون بارسلونا 174 میلیون یورو پول رضایت نامه داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28860" target="_blank">📅 16:22 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28859">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvbUwl2KEb1JHdbokYVVuTU16eK1ZKaFBYH1bujJY90FuP8v_Yv5db0XyeVBaDAze1qIWwi4dF-zsZ6n1xm6h5bL0RWZUUFpl2cprNLpawI2Fed54uIPXRoJM6ZUdsAc6--sMdUfIJ6QZMPhX_QL8cnLs1GjHuLT2jt0bC6oHsCoycHQE6CBKUlTUxZYT7FLT_7ge3exx1jIIm2u3Td9ch8LemQLhEcLd2faBE84_qDhdEIbHnjRJ6r9Go9TQcCmTFS272pnKdeF8jJL-a5E-uy3plGZZBpQ-18r-mLq2_P4-3MWhEy0oq8_2pScdyo9i2dp5Ti3N8Y_K-URwWGSeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28859" target="_blank">📅 15:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28858">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOhf7u_e-n6MCjxFbEcMCJHw0CcyAbRuWJPEUPBcw-mAETeJ_F8fL75qMkXdwXkUj334LlCuHKToXmbU1UIeLCT5YvZN8hrc2CeC8OlnkfRYwPuq1b6zbegjbxLYla0b4TWDG43K1zcHwAeoEPWw6bSlWGN-q6xoejEwJweiK8OvLONgxEU6jhKet1owp1uvhST02bz3biEQWEYljPV1ezylTRqLBtSnfvsMLvrhJ0W11SxzlD-89Sed7dQCMKBSeW4S7hDxhAevTSflZOhTwK-uzDos_7iCxLFO1hg_dEkpaBM8ohL2t2PGn98QwQ5MdYl-u3oaIldEb7JW9dNiBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌رییکای‌کرواسی با انتشار این ویدیو خبر از عقد قرارداد با محمد محبی ستاره تیم ملی رو داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28858" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28857">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJt62sEVl5fb6_eKdB0nCnU73EYbbzTTVXhYqJcq83k63MxjIgSwDq0jIqwD-hLYTZcYHuGijljEYwfE9OXxOVoLJJXmfu7FzXoD5vGq3A6LUrcktGs7x2BhkzBDK92WykfW1ND7FCv6ORbsj7KHb47aAefItF0xcvhtzd3tkE11MK0kVt5en9q4QA4lWQKO5Pwk8zRAMEQ0mTu1Qcdo_j8p_tkiGn2y71Dg0UF7fc1t6KCrJ2NHyA-ZrtCpR6yyOXf_hNq8ZiVHY3ZTDLitYUQC-2uOn0Q67SHWjRuC-pENDTg3f1Sv-JmwWdTnNFdpzA0gZfG-7zJmbBhG01GyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هوش مصنوعی دیگه داره کار رو به جاهای باریک میکشونه؛ یه چیزایی داره درست میکنه که با واقعیت مو نمیزنه لامصب. اینو ببینید‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28857" target="_blank">📅 15:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28855">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=rWcbcp_K0VslAIBPhEv_GUSEXitt6o5ZX_dQ2Bbw6U5YJ1RHASKDqLL8BztzdmoVDUlSCKcKaVG7UNmvfn-eLKba65b_m7j7O27Zvfvg3TYBUznzNuUYMmElr0IolN99BQ4R6a1LTeVkmYGJkcXWxsuMxLrywGZ1gm68Hlzxfuo-uw6elBZRy_qC8bkxSae-N4BvqYt0QPnWXj5YiXf2WYEf_Wf-HIquVIvoEwdOlZJQJ-F2Y8-IB4AaEQw1zk2BXF69FDoxnSNriXKbhb3wmwHJUw-oqvyrtVgUrcWKRGjp-BL9_MKCJ_y2_cKzSDA16EvK8Idw2GmBpm-ii7gKdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d453f3d9b.mp4?token=rWcbcp_K0VslAIBPhEv_GUSEXitt6o5ZX_dQ2Bbw6U5YJ1RHASKDqLL8BztzdmoVDUlSCKcKaVG7UNmvfn-eLKba65b_m7j7O27Zvfvg3TYBUznzNuUYMmElr0IolN99BQ4R6a1LTeVkmYGJkcXWxsuMxLrywGZ1gm68Hlzxfuo-uw6elBZRy_qC8bkxSae-N4BvqYt0QPnWXj5YiXf2WYEf_Wf-HIquVIvoEwdOlZJQJ-F2Y8-IB4AaEQw1zk2BXF69FDoxnSNriXKbhb3wmwHJUw-oqvyrtVgUrcWKRGjp-BL9_MKCJ_y2_cKzSDA16EvK8Idw2GmBpm-ii7gKdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
باشگاه رییکای کرواسی بزودی از محمد محبی خرید جدید خود رونمایی میکنه. قرارداد دو ساله و رقم بند فسخ یک میلیون دلار توافق شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28855" target="_blank">📅 14:32 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
