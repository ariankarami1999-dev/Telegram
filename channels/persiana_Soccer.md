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
<img src="https://cdn4.telesco.pe/file/I_6TyvfvTYFRLjeO_IAeJD6kmXInTEaLYe3gWzxJNfjeypcHlgEuszMclycf9z6FXpW5aDsll8OUUXAcvqAGNpS6ushpfhkOeKBEHMiK-0Ma86eQXDmtF3W-Dw0ZI0ZnSw6S4JR9jJkrjcEQvA9mB0cZLif1TcFF5Z2lAXI-KzfVqz7UBrmLersLyhRrsT7AlYrtdgKRBeQklk5On_Q6plgtXDaoX9CjhBkgvIpXK4yjabyBkHLvgjcMQ54Vkx8xvwFLvDVelLJCF_pzYpV6sYFPvkyQwJGTS8_Z-0BTXkG0quF8qmfrnFE_AurGYbGAhpByc-gamQ_pSy1n5mZb-w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 489K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 20:19:53</div>
<hr>

<div class="tg-post" id="msg-30020">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🟡
👤
سه‌سال‌پیش‌درچنین‌روزی؛
حین ورود رونالدو همراه با بازیکنان النصر به‌تهران این حماسه تاریخی و فراموش نشدنی توسط مردم خونگرد ما رقم خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/persiana_Soccer/30020" target="_blank">📅 20:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30019">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWi7m8AN0vDxUhS3o-2Mg3B-rjSo4xDYJpMCyKKNWU-ixsx_tEosoXDtT_HM8CWq64Qom3II5CA3IGJZ7uI3QY0OI9fokY7UBwHDa3JzaWlr7onfwy1vjcGIg16yKHNRHbKQsObm6RFdCiBvtkt5IuOCimTuLPZFhIUSMk2ig5toYBQt387RUUgXRViUgEBOl-_ZtbTU-lXuQo42Wm7YPcGwnHrkKUc29JEPOzMtbDLWBDx9ssA8L4bWq1F5DWF2UGe6KHm7IKDj8lIrTvxTh2emEOuSafjOG1LE2cxEF8bkj3DBf5UrUjKEgMHTn0OCY5NOpmCeC21iR1XaWXtZWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/30019" target="_blank">📅 20:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30018">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIKnJZk6N2VWB63MRQyO2HMrDLigdtgXZkMFLDezM32fmbyC4sI1c2zUF2p6mPbQphFyNwoJzvjuzkDfmaj_cD5Eis7OPrd3JAT5t0JPbPOIWevSqoj35RlLokdA4mX07jYxCa2W6Q9O5Fv3KSX_NUHgLfef1oywUZkxSlpf167JTYb01TcIiaP3QORURu4yp-5wKjdNgAKZamxieEVd4FGCuHAEy0AxtAJk8Qn7XwWNYakt4eeUcugUTEIDz7TF7voXsl_PUbNe2C3KhNl6RcyAMIQTUwT_sojP9VvDEc48Td0F7lFEisGoD4RxWyR56Ulbfxq7Z3feTU0jN9rr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
فدراسیون‌فوتبال‌فرانسه؛ طی ساعات آینده زین الدین زیدان رو به عنوان سرمربی جدید خروس‌ها تا پایان رقابتای جام جهانی 2030 معرفی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/30018" target="_blank">📅 19:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30016">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QRRAKVbeTt6r2hL8aE0ocUW_HB0nd7GWASO3rJ_AMpJ1pUeSSUiNl4IGNAkicvj7_bYGZlAdHje29DVlS8uABfyxH2VM4hkTlxm99SGUhpJfmGUawLxgi8H16iEwUwKJspJyvrroaWMi06SUpw4PXj_ZXfLnyD3phhJql76aizxnqNi74qPSaWG7pwDf8GFHHRlauZ-Y2-JoqpDgfdOv0RxYklzdnB1Rzd9QZc7lwFOf5qgw9UlHBCyFf-PtUX8rp8C8NMzcNz_l1r9qaoutckyoPYpmuxIA3VLCMBSMg97e1mcTQ0lJJQKOTRzrfrfOmz5u-HdBLIdNfZqG6Qh89A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rwTx5DBKkSTqsTTCDe-TNnreJPkUgTluGv0Q0kLy7yh04znAEm9KYthihWnBGhHsqh6sVmMZnfOksSPxOFVgvRG7EhXfGU7wOgO_jpYBcf30TjQYiHNeLDvvHlZadYqTAMd5l8X3nsoHBDxRoJ5JcBmRHIS2WwHhyQ5LMwmw_-p8Tykl0w6ib-YXG4iZSQI2PC_xqjDktMcQFl4CPKIwEZkRn65lNIFfamAJRRYxUnBqDrlfHGaT230r2qRBq5Vvrllw5NS_dV6uYLjxqaM6bodxv9iqv7UCozWSzBdRZQs1uPLkssXeGafNUFwUeW2zoC-dokGcdwR0zNoK2Tun7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/30016" target="_blank">📅 19:51 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30015">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RT7ZOJO--TYNRbLiloOglFTfFo9L6vGe3FRUQ5ax50clgjQVSRwtxKj6iGAO47z9hlnBFCDNOCFSID2tUgdHUI9ruE0sNXzxAm_HtzKe71kchDKByNmlUiQg3EiOj9qYsnmV1CJJHbkamlvOIuBd3pr90Gg19F-K4aVL0Jvpno856yztfB4RnVbqBplo4k1vB4K0PZr6HRaWKDJSF7sn4NLX-5Og0dVMkn9nkdmhHSFEd2QQEUMbwDqIfVq3xLvxRBdcL9Ep_dIeXA-Kpivl2QfEJDSDteVlF7qgU2nreO1TyK8XUCdvpLaYDp3jcPt8nMMB9z7727IpLLQ3KZB3nF4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a036b864e0.mp4?token=cNyJ-r9oQPmlZ7G9f_XpfZwhhh26KpRnMFbtDFexIfH4R77p_INUsQa-a5r8CuSR84jL6E_OhgA8vdILFaa19PB-8w_BujmLvSXjhbDZiAQ2zza66wqRDeDe_mBsC-dtG1ix1khvFNLjVrY1JrEgM5ZnSOxO_0YoNn4VHRS9lgGgpMaqlWelDL8pVIwrT3zAhZnc9BdjplApRWzCNQDbNsmzxG1Dz2yUWMbVfaUp_Qf5FicziUsBNZNrANo2ijKfNERTTKw6zQi72y-wfIGG3gAedrUth7w_zbvjv_L8S3agNHduzzYlAuHGI8o80I0gMPKHnyGOIY1OHRgdce42RT7ZOJO--TYNRbLiloOglFTfFo9L6vGe3FRUQ5ax50clgjQVSRwtxKj6iGAO47z9hlnBFCDNOCFSID2tUgdHUI9ruE0sNXzxAm_HtzKe71kchDKByNmlUiQg3EiOj9qYsnmV1CJJHbkamlvOIuBd3pr90Gg19F-K4aVL0Jvpno856yztfB4RnVbqBplo4k1vB4K0PZr6HRaWKDJSF7sn4NLX-5Og0dVMkn9nkdmhHSFEd2QQEUMbwDqIfVq3xLvxRBdcL9Ep_dIeXA-Kpivl2QfEJDSDteVlF7qgU2nreO1TyK8XUCdvpLaYDp3jcPt8nMMB9z7727IpLLQ3KZB3nF4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بابک مرادی هافبک سابق استقلال: واقعا دوست دارم زودتر بمیرم. خسته شدم از این وضعیت!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/30015" target="_blank">📅 19:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30014">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=sfygSFtmHque8PN44bwQhRpD4ufaJjZDOx3O_TmVl9hc7Rk0FjDTfG2h61h5zroh_7oG3DVaO8mLjNNw1yT2gXf7gnky43tbcPvhoQjEpdBfH2qixGCrcch7DL_h-9hp1_sA7MPkoJ5epNiuff0KvqT66I8Kow-46V3TRTZBLYbM6Tyk6qZUm6XvuVfZmc787rl_UBbrwaupmDOGVKf3advPP6ygFfZeSbGm6ZvVOw5Lx-SK8QdKclt9Ph_llVSfZtQkY9BnBTnGJbf7KSvwa8CkaObsD-M60HDb6yEwGfst2PTI6Fm_-EiAdMqTwY8UQE7IBgiNudPjK67WRlx76bWxd9iGYsrKDRvRmztYq1P6b8S6U_3A3LHvG3mY3DxGCLl00LlJhFW0iI37t2KCpJHtQA2sTmd3EyfGuqKhYYW-dk_aRYT20PZuQt0BzoHQDn5dhwH9yZ8boBSzb6AWSbub_erk4rQ0WNL--8kbwFZORaGPQpnCLrn_UjCQotzeEg3mbB3IcZxpYXJFzCbi9dl63GflpWpXetCxBX59yVz-RfePhPJ8YEAuQQxs9NB1BOhrF5MGnq2sE4aAPNcNMHlyvIt7TTirvoS07H93hgkeBWv1uv8PsUIZvhKCjSwD9HZ4yaLRKgoxD70HKdl3YVkbPZVAy88GSaK8-Gk1hAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595b48aa31.mp4?token=sfygSFtmHque8PN44bwQhRpD4ufaJjZDOx3O_TmVl9hc7Rk0FjDTfG2h61h5zroh_7oG3DVaO8mLjNNw1yT2gXf7gnky43tbcPvhoQjEpdBfH2qixGCrcch7DL_h-9hp1_sA7MPkoJ5epNiuff0KvqT66I8Kow-46V3TRTZBLYbM6Tyk6qZUm6XvuVfZmc787rl_UBbrwaupmDOGVKf3advPP6ygFfZeSbGm6ZvVOw5Lx-SK8QdKclt9Ph_llVSfZtQkY9BnBTnGJbf7KSvwa8CkaObsD-M60HDb6yEwGfst2PTI6Fm_-EiAdMqTwY8UQE7IBgiNudPjK67WRlx76bWxd9iGYsrKDRvRmztYq1P6b8S6U_3A3LHvG3mY3DxGCLl00LlJhFW0iI37t2KCpJHtQA2sTmd3EyfGuqKhYYW-dk_aRYT20PZuQt0BzoHQDn5dhwH9yZ8boBSzb6AWSbub_erk4rQ0WNL--8kbwFZORaGPQpnCLrn_UjCQotzeEg3mbB3IcZxpYXJFzCbi9dl63GflpWpXetCxBX59yVz-RfePhPJ8YEAuQQxs9NB1BOhrF5MGnq2sE4aAPNcNMHlyvIt7TTirvoS07H93hgkeBWv1uv8PsUIZvhKCjSwD9HZ4yaLRKgoxD70HKdl3YVkbPZVAy88GSaK8-Gk1hAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
#تقویم
؛ چهارده سال پیش در چنین روزی؛
کریس رونالدو فوق‌ستاره‌پرتغالی‌رئال مادرید این گل استثنایی رو در دقیقه 90 به تیم منچسترسیتی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/30014" target="_blank">📅 18:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30013">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUnPuzIftZFsLye0LEsI-4LuCHN1QmhRb0rkjr6T4ephGOO1oTlh7yvkFWzigHeUi9mp0fYn6FNutnkgpIcyHpe5FCWSvBJdsNK8fYlbqoJJ7bSxe6a7anvu_gIZzKpdJAkql-5dnpobGItnhZUX0iBAfAJUJfgxwdsSh-P0JhjyEsbxwVjGF5Whv1sD8ZbM2c9YLC03Rm9reje8Bfyk3Wks8t-CIcnA5HgnQ45j_2zsDDfQ-8qGNavoMx_OpKiVse8KfZwNFAiIJuGjmfjLhSF5alPEVInKoUowq3kWJabBQpNzeb8q-32SJTEeh-XQwXUvz62lO3ip-EvmExgoCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🔴
#تقویم؛ سال1999میلادی درچنین روزی؛ تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/30013" target="_blank">📅 18:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30012">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdbXCl9GjqDhllNmAGLJGSqD-1SywTaMFqsw7_5zFZ8LXmA0Nhsq5FfQwvJyovpKoGWSr_YrjGp4KKGm7yuLhX7dYlIp-PLYyUORqL0yIB9Lw2QZPo4JPr0baF-g3dl4oRV83eEJ6wXIw4mJvQta4LuMItVhW38QWOfh10dbGYor_xMLpQ_3QLJgSw09NwgRgFm4TjQb96cJZb738EkBSdoUIjB_CVudR6OZ9L5kkTq1_TrPnZBnrJ0bBtvb2uEh5r4etzLxVVuGZvEIVP5w1f1aRpLZtJWwxZOfOMzTgC9YcdSh-wAmlzXl1XQ1HtElJ4ju6bKAG5fVI2GLs5KJyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/30012" target="_blank">📅 17:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30011">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2GeHS20Zsk2CATjWeynR6vOwlmuVJ5tzAydx8I3EZs7Cw-kFAitx8kECXUKR0j0QQzUCpZLWZXfNffvfh7-_A0GqT0gy26zV_VfWN-U1BPf-jIZjog2yCcQP7oo1k0zNxFZa-zGsQxTS3XFduYxpVht2Tg1xnlG_J4yzbOKW3GWLPzm1wH93WR8Sll59wNPm4BVt9Ytcz3t3SujxYAx1k20S5WgMGp8vBS-6PqThw7CRCXdB_qUTaMIgX0ZrxFWgXYpP0DB9iN4M_7g5EDgrdC3cd3eYwwuYkR4muP02uUGIYLRUGVdSTDGgtCxwAyPQK0lNM-uqiNOrEbbleMnLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلزنی آلیسا لمن برای تیم‌فوتبال بانوان یوونتوس در هفته گذشته رقابت‌های فصل سری‌آ ایتالیا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/30011" target="_blank">📅 17:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30010">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=Msv8obm8o7SWN-f0KetvZWpqdhdSVS-Q66SQqFbRaX-PKiyWn2XKc_OCuqz9uSe7ty2IqMQ7rty1AMSIGMVkD_N56B6F1uNwYeXI1KQdkmcSVdtAKnWgOgKzGE0nHlvF-p7kJLKqadH7wTwikAXZiqxI41Y8RzMU-DvU1khuSLWKjqOTgdcW0Mi7eQQo2PJ58LtYFcSML_IDGHSBPVZcmsZzlaqItVsVxphsqHGcCYc201JExXZ-lAKHo68QLr1C1h89dp-wpesAD20pUbOQ8BhBGVv43azY5Mhg78cIsMXmCATE6OZlxqf-7SE6ggYJ13q6EkGTxcmY-cmkICFvpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9586b8df2a.mp4?token=Msv8obm8o7SWN-f0KetvZWpqdhdSVS-Q66SQqFbRaX-PKiyWn2XKc_OCuqz9uSe7ty2IqMQ7rty1AMSIGMVkD_N56B6F1uNwYeXI1KQdkmcSVdtAKnWgOgKzGE0nHlvF-p7kJLKqadH7wTwikAXZiqxI41Y8RzMU-DvU1khuSLWKjqOTgdcW0Mi7eQQo2PJ58LtYFcSML_IDGHSBPVZcmsZzlaqItVsVxphsqHGcCYc201JExXZ-lAKHo68QLr1C1h89dp-wpesAD20pUbOQ8BhBGVv43azY5Mhg78cIsMXmCATE6OZlxqf-7SE6ggYJ13q6EkGTxcmY-cmkICFvpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ سال1999میلادی درچنین روزی؛
تیری‌ هانری اسطوره فرانسوی باشگاه آرسنال این سوپرگل تماشایی و استثنایی رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/30010" target="_blank">📅 17:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30009">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgDW85xd6QNjiMDXY6nfWrwYB-rs7beYNWOHb51dkc9XlaAP7bJRYojTeV8KWovoGdFyHkSCCxRi6sUzFXQsFYydkssFfapjc84LSEZYDst7TSUxVzzgTM_LceKh_AvGQBZukPZqbX9ga5oO3pCbZaeTP8QRe2PR5Jdb17_4L1lVjd1ifIPGIPAt_n7Qv7mGRAHqv0xOoHV7_irO80sOeRtp8Kp3ru7j0oNUIUenbg83XzwlHwwuvAvUAMnswQOCKqx-NGmOS9WPDc-xF5R7kusMF_58pMEj3YgLbZeRtXbkM5VlLv1hpBu197kf1Y30Iqy-gMVfUrruC1qc3L-C8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/30009" target="_blank">📅 17:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30008">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=IBxWb720vDv1GjU0HohMRYHrD9B3EQcwUF_efB3Gp1zSCY8lVFoCbOC8ObljK-392-BYYwtP6XFtixmu2kxZc3uINVr4Jqvs_hdl0xAr7PrubSTYdekDf3plKv1m0lPIShtcxqXBnGK1so9-6dBdg4qzDGrInFDXbHJubSvXf0IbwL46SWCa6JBkJEqX3JyNMBLlCzzRrsemx5CE9gKMp2UaavPw4Q3-MahSrXIqtQYAgTkLsM563hONTMAFm-4B0jEN0HNs-QbVP6xYnpV6KBhVC_2kbgM6IGohtLtSjSS4fooeXXFEgZ0av2sh7lIk2tY6bJKyscCd-L2R2OjQNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656a3bfd79.mp4?token=IBxWb720vDv1GjU0HohMRYHrD9B3EQcwUF_efB3Gp1zSCY8lVFoCbOC8ObljK-392-BYYwtP6XFtixmu2kxZc3uINVr4Jqvs_hdl0xAr7PrubSTYdekDf3plKv1m0lPIShtcxqXBnGK1so9-6dBdg4qzDGrInFDXbHJubSvXf0IbwL46SWCa6JBkJEqX3JyNMBLlCzzRrsemx5CE9gKMp2UaavPw4Q3-MahSrXIqtQYAgTkLsM563hONTMAFm-4B0jEN0HNs-QbVP6xYnpV6KBhVC_2kbgM6IGohtLtSjSS4fooeXXFEgZ0av2sh7lIk2tY6bJKyscCd-L2R2OjQNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروزصبح‌یکی‌از بزرگترین دوهای ماراتن ۱۰ کیلو متری کشورمخصوص دخترا تو بوستان ولایت تهران برگزار شد که‌ چندین هزار دختر توش شرکت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/30008" target="_blank">📅 16:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30006">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkA5YyDb1jvRSuo0FdSLSWPZpE_auhXa25cK5zlYfwUFj5Ns67CdtLYxZUOJPrgm1-Xq_GZPOxlXuEOZ4HQqNU4TrgNQz2v2cB09HUoe2p7gvGETBe1nxIrom20z6KGN6ynOfPtV6-9vBET1zSOxIIIo5x8lYNmXpQ7MiF7UF7KJWo0SW6EG7_aufhoMgCXmU2BAxDKsBMwpjZq_6mdxGrO5W00McroKki1o-Uds26rNEQBOAn3OKQa452X-LToAaDkBM8YbqfvOpOpeG_43Be0dWHVWkPnxz6h3eXsgSB1EATBireiwOcGMsQ9vGutrOOpFex83wMvYbZuf4JZSiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L7yW0yBsmyOsJMYIKu-0jqNEgZ1joy4KLDbq1Up4_drfxOyZNBW_jjCAhJpSCebHOgak5CEA7C0m8nLO9c3Jxh5YsaQQ3206o7fHiZArBW4jx6tVI01O4A8DE_-Vai_OgsDH9f4duQOcT034UK6JTWngr3ITmuGsySXIlMesaZylFi5vZEhhI3chWbfW_L8clGyTgwmHCs3C6TdaYhWaoIgC4yua4MLL6YR9KcTvqYyYpSJqc4H5jRU183qplroaMRKaqSOnFYYu80PFJ5s0IeH-J8eQMMV4jOU3KOYaLFzCPl0yguPRgd9UgNJSfayko9AJFu_BYZl9DyWbNKraQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
#فکت؛ السد قطر تیم 78 میلیون یورویی آسیا امشب بعداز 22 مسابقه نتونست‌گلی به حریف بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/30006" target="_blank">📅 16:38 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30005">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chlOuJ0qvtfty0qI16ixgzREQP4Qfws9XuOXM80d4TDU_93wZFcH1I1H8cyvzES59anMCdBLzrGfG2cGRyqwfC34E6xg2vUPROAKBFzP_YgFWLJ9Zt6SNi0EcMUoN7fFFXXEPxV0YaW0DRDkhJ4UcEWU5ZaZAM-ZyGHZ2dYj5lqFzPytUsSQSLTSfPi_yZaetR326u1uRc6VhjVBRNv-2thxyfyjwpg17avbvrfsSlcfavKwryy2NHeexkdkm2o443Ba-8PbJ6thxoDuENcYTGsJvRKIsUjAWtQto2H7VKUmkHx4kc7CLgCzQnEsrA4ObpTcR2ZRsVU84aaM6X75fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#نوستالژی؛ یادی کنیم‌از مصاحبه قدیمی کارول سلیکو، همسر سابق کاکا و علت جدایی‌اش از او:
‼️
کاکا هرگز بهم خیانت نکرد او همیشه با من خوب رفتار میکرد و خانواده‌فوق‌العاده‌ای به من داد اما من خوشحال نبودم چون یک چیزی کم بود. مشکل این بود که او برای من خیلی کامل…</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/30005" target="_blank">📅 16:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30004">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEq8TeofjxaLw294Yq-snDKMv8rI8vWJALxNsI86TdcnuFyhjHlmQRLkSGu1uxRVvd0UMVPYatN521Vvvir3FaeUrCu-NM3_zDdAR7JY46-4VRsG5JVkrekKmZwpKsA7wW8H3_oUF1SJq-m9L0M8_-310Oi-k0t8AXRLq0hcp1YphSFGH1ZqTreVVZmH_SVQ6qTyW2CHdhztDCql7V0gqjAQ1sHfI2HwwXdx_TQTVFmbK2wTAPX1S_X1Qf-7jcji5bBBqFMUtHjBcL96-q_2zJeiozFnaPDiZlBMgq4Za7XzKIxU_9Emtl9BFMNz8g7pPZJ60c_mlyCIICB6XmZmmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30004" target="_blank">📅 15:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30003">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3aujRsgqkh1-5Q6LTD6gpCmPLgzMTKXtlpdXGCpg2GwScvj69Vtzb5Y8neAWDw4It1khwfZz2q5tLRKYvv7l8T5Ek1d8G2myW9McTdd5cfz9Y-1Mh2WGP4yoLQaMcGQG6x7H4aeOfaXCpKotvzA7XW0w5vGaK1tUV2H28qBrxXb_MPD91TbIKJxLdET0LLg7aoKB-Jr0xAqq9clbZTxDTPmd4sffQrg9FPByNgacG2a6mowY04pi2OnF8bK3xQLv76Qn26gVVD4gqYI9ipM7u93cEwpmPx15VNN2uNgVC96MFVyI_qRWOuiueRvoqs4cpX1y0X0vazkCxEnHlLzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مدیریت پرسپولیس طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد. توافقات بین طرفین انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30003" target="_blank">📅 15:37 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30002">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULsq8TQz16i42KwR6RYOFSIIqr3huwHcuCVLG0f5yp15uyGY7hC66RHFmxBiYOaAJ2E3RLVJD6rmwIJpG2g__lNr2-7xzmMUdVRq9eMmgqnmgZtPFV3l9XOmxMPewfHKnIQ4CLCC9ZA0U6GTSSve3iuNBMDC_FaR1QeTNTtVEm6BdBLuSbWxC3OpYBOpEoH0WjcAby3SqzXIKb4z2HLImWC6LMeYvS_PbhxQGNDwfjKLxUrYhwWr4Dhu8gWHouJ13grDC5OPlJSxsswGP-zmfYRw-lG9vVIewXUcrRWbdvJDFilerelJiEntFXsre5o0ZFYoeBa58WcOZdj5oUAX2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ نشریه ESPN: فدراسیون فوتبال پرتغال داره تلاش میکنه که کریستیانو رونالدو راضی شه در یورو 2028 نیز حضور داشته باشه و در پایان این رقابت ها از دنیای بازی‌های ملی خدافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/30002" target="_blank">📅 15:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30001">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=m_WlzsXLQ_MNlb4As00ZG2-t3151Dewy4Yl8-JJoXJUzJM5Lyv-CJQ9YaxhZEg-M1cyrweCtHdrfBiH4-rkeV-zcajJgw0kteUjrAVU1TuGOp3sgoAh9KwQfOKp9OobiTdY6AY3UAhEb-RNQQfMdfy0rYIfqYGzxgWDUw9KPOCtnAo9ergHD0rmoon9lFPSimIXuH_yzieNbOgcA1u2FYQ6WBvXvjY8ohS1_GPH9bdZz3qrxeeQX4MF-m3jj8x70QmmLk6Kq1DaR249R_kEug16iX1kYimEzDnhNRI1rFW-OzOThKwuIKuApujVostAZJwxbS6-ZAGBAdTY6oChaLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54c60e1877.mp4?token=m_WlzsXLQ_MNlb4As00ZG2-t3151Dewy4Yl8-JJoXJUzJM5Lyv-CJQ9YaxhZEg-M1cyrweCtHdrfBiH4-rkeV-zcajJgw0kteUjrAVU1TuGOp3sgoAh9KwQfOKp9OobiTdY6AY3UAhEb-RNQQfMdfy0rYIfqYGzxgWDUw9KPOCtnAo9ergHD0rmoon9lFPSimIXuH_yzieNbOgcA1u2FYQ6WBvXvjY8ohS1_GPH9bdZz3qrxeeQX4MF-m3jj8x70QmmLk6Kq1DaR249R_kEug16iX1kYimEzDnhNRI1rFW-OzOThKwuIKuApujVostAZJwxbS6-ZAGBAdTY6oChaLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مارسلو ستاره‌برزیلی‌سابق رئال مادرید: حاضرم تمام پنج قهرمانیم تو چمپیونزلیگ رو بدم تا فقط یک قهرمانی جام جهانی با تیم ملی برزیل داشته باشم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/30001" target="_blank">📅 15:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30000">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdLriqM2nkUmrTxhjSTdI5aJcEfh-sGV0BdpQgpxM4BMyLmHTATPNCihr1_j_8cJ5VqzepTt6RNNr-UPzp2-jXImT6PhpU7BrHz1PyPV2uKtiF1Z-4kV0Mw7si225i_uMKApTGyNfBAquFKwK8_fMTZRJDm9UtWo8-xtIj-uWMww7gFEQy6nz5qGXKIoAOhJ725hv-TxQ8m5vNa5MPzrYSsg7AnMUVSY1SadJbwnN9UQizq7Z9jKJ8Ul_gHfKQJNu45-2T7Imj5SRoFVb7Ce-yOJDLB0LK54tcOXCgBEqZ-6txidu1sPhDuy5jjqfueHDwXvkfZAVgjfuU5gYfXMXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30000" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29999">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVSUY8I3hLeIw9BQJiysmqwt9ojNEs5e4jp8C25nqcBxS1LtFrNjhQer3x3JnJt5BPijlPfKThVUPRqFrJGcjsNJIhO47nLmG1j0EXiCI3f4kL-4cm3e1rMQfNXtGQ8V4KvBCLoPYlkGXrBHLZwGUoJpWeeQik_1yqDB9OA8KVxPQUBwidCN7GGzVX04j4QjX5K56yvWTfx3F4WT6lZLVk4IkSfuAPoA7TNLQotDDji46Xuw5_xphlUBUU3P8uu1Fvl0x3y8-YSxk9ONZxBpeb-LiljZ6J5cL2Ybgnj919Y-q3iAz3fX_cUOm_2znlAsgWgkJqpNhBvLBDYIq7GSQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
👤
عملکردفوق‌العاده درخشان تیم منچستر سیتی انزو مارسکا در فصل جدید در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/29999" target="_blank">📅 14:14 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29998">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfdssbuHzgS_pdB4TY1r18_vlSpLI8sQKGDapZfdO3ddNQV3euj4ZFypQ5LVU1z8_T5FNxxRfuv1xTFKH5lOqPe_js5ZQFP8GbH1XW3gKtCgWMhdvceRvdlXL6ySStYqkrF62yp1ulLV5peAbfulAjDjQqAok3t-GOKpwFtoIOArbjD7IrvF-M53lxEDbbGF33KbQosdgrwg9H_p6BgdBdX8XVuttMnMLlu5EOyu3eBFetmFR9WNckEyDV-Q7HEfj-HcYZyGbhO7Jmj-FyLRh14ba_N1y5-1B_d9j5Xh4Zb24ndR5p_kq2iCO67aNRekYnzDGcSipcUEG7uhTU306g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/29998" target="_blank">📅 13:44 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29997">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=SOn8G8TmMARtsQ9jsTIgZGZDj5oCvjUgQD9KItl2NTLZG_y-slxFjbgUsOV6hpDa_QBYqkHPadCvgRcna3IgaiGZtXQs5rLvR9oF6Z9q4NTQWCbl7zJwgbL9aLyOhDx5Pp-V66x7qJ7YZgfd-EZgCLF1gRRMZCXiPtAhkqTJ2XokDbm7lwms7I6Ouc7w58ge5ABGVZWEbyT51vtq_Jcvo0TbChreBH02tyc3bV2UWtyx2AnCfWjVau2KEG-ihEAWYenK9g-jY0UPKiLgJcJ5drRnWmsHfCa6s0kEWJn0E2Gsq15hAqzIUH3yTVOABi4Y4l0ZjN8EisOQfLCz1lHxVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe8697aa22.mp4?token=SOn8G8TmMARtsQ9jsTIgZGZDj5oCvjUgQD9KItl2NTLZG_y-slxFjbgUsOV6hpDa_QBYqkHPadCvgRcna3IgaiGZtXQs5rLvR9oF6Z9q4NTQWCbl7zJwgbL9aLyOhDx5Pp-V66x7qJ7YZgfd-EZgCLF1gRRMZCXiPtAhkqTJ2XokDbm7lwms7I6Ouc7w58ge5ABGVZWEbyT51vtq_Jcvo0TbChreBH02tyc3bV2UWtyx2AnCfWjVau2KEG-ihEAWYenK9g-jY0UPKiLgJcJ5drRnWmsHfCa6s0kEWJn0E2Gsq15hAqzIUH3yTVOABi4Y4l0ZjN8EisOQfLCz1lHxVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🔴
#تقویم
؛ 15 سال پیش در چنین روزی؛
نانی ستاره پرتغالی منچستریونایتد این سوپرگل دیدنی رو در رقابت‌های لیگ جزیره به چلسی و پیتر چک زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29997" target="_blank">📅 12:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29996">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf51IvkjXUEM2_62Zo9BDW3pRBmdWjXEPXK9iuvqS7qOatnRRCK50mY00D3dXkX0ZM03js1qy6_Z8mEek4nP8RwTc6-IHRWMZX19j0ix9VPmWihn0OQjVS2TNN3vFwqVGgiyEMXX6ZYd95iPbLZ1Ssbc6JYDRdFxRkyI2uERDs8_hlMC_4S3SNYTC_uUPrCmPT_plQujArhyZaCVMshc4g5GBWE4AVNkky0VPOlb3ezjboaCvBPw1P9YCxbAuU7ak8xMauF3FYNeiaoes92iNqn97RjoW9ETV0rtM8LYxULjb7rNzTn7Ns9mUh3OpmlO08hkuDU35DSHX0X8XJTXTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب پشم ریزون و استثنایی فوق ستاره‌ هایی که همگی‌موافقت‌ خود را برای‌حضور در مسابقه خدا حافظی کارلوس توز از دنیای فوتبال اعلام کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29996" target="_blank">📅 12:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29995">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/In_vWZCzBfLXZBJ33w3zrhqDy5ClgcGqG8Q71tBhSoV3Cs7kfAUG69KfsRUPZ09APFNJLwFFbzLNJ_1NCMSYl-8tGtq5sWbVo1-i4OmeZ-irKaRucSwAt-jtt-Np2isiJlK2dLgnGNaMz0s0fCJgwI4XTGOzTriig-jlVzfDX_-jMNFpZ_AEOlir2XfFAbWLBrxkkS_C9tUHegONdTuOAjCe982IcqWLnXnsTWwroxOitl2MdtU35IyxKEqpQicEM8dm-AUOSvGW-OTL2KT8pqs4MeuID2-FlLnmU3tg4TO2UQbibO9ok513RJJvx74Jd6hN48IG67CeojdlCpT0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برنامه دیدارهای معوقه هفته هفتم لیگ مشخص شد؛ سه‌شنبه 21 مهرماه دربی‌اصفهان برگزار میشه و چهارشنبه 22 مهرماه راس ساعت 17:00 بازی خیبر خرم آباد و پرسپولیس تهران برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29995" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29994">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCiu8q5L2A9ODEnPaEG8KLmOgaq8VOMR06h6gsP2dOFRr593SbfYpCAM6s-wWtvmjXA9xA_FMmYPGnNDtfkCsx8BubxBeQp0J-EcVWH5rsl6px-5F1DNQS8Jqqa4Kc-8TrJSrM33RlY0YRKG-7fjJFWCnGCD-VWfB6byA8ZCt_p-hQ4F1ork2WSyluQ6wqoKprLBbFEwL8cecC3JCIyD4lUfohHsI5vRDJwj1Dtvzj3H2T0lfGsCzJDZFQm5uRp0OwyU0ULLQKGr6INCnMmAdtrV7_2KzA6AKQpQJOFWsXCXRX2kjqsyTbycip_VVsHkb7kNqf1pcmDfg6nAX1Kp9IGU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f8f92a53.mp4?token=FcUMq8uOWa7dw-V2DG3ufzKYjaojCDg8PgePMK9YM2QLxPspubtMFJpBR0RmuQKkJigrwHP6lSLC02NQNLucOxpTl307aIpxwEDEHxz0med4k5DtBbSNfzbmrUO0cLHM20q7W7h6HmcEEr8Sm4GPHKYGQubGWnvmoNl4aD0xPWQfbtMfC0G5SVtucjuvKjobBLARqIgNq-gA5-5ngCWjZaJOD3ng07xDkHmxbF4d0pT1X3AFqrw9wK9xwgTWcWPqTs6fKJXqmVRJxidGQVBnFX48FZn4puL6mFZavtDTv6sh_zXjqVDCn4knjQ3EtiLDGjg5XlhqHzHmyPD2C6bzCiu8q5L2A9ODEnPaEG8KLmOgaq8VOMR06h6gsP2dOFRr593SbfYpCAM6s-wWtvmjXA9xA_FMmYPGnNDtfkCsx8BubxBeQp0J-EcVWH5rsl6px-5F1DNQS8Jqqa4Kc-8TrJSrM33RlY0YRKG-7fjJFWCnGCD-VWfB6byA8ZCt_p-hQ4F1ork2WSyluQ6wqoKprLBbFEwL8cecC3JCIyD4lUfohHsI5vRDJwj1Dtvzj3H2T0lfGsCzJDZFQm5uRp0OwyU0ULLQKGr6INCnMmAdtrV7_2KzA6AKQpQJOFWsXCXRX2kjqsyTbycip_VVsHkb7kNqf1pcmDfg6nAX1Kp9IGU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از کاشته های دو ضرب در محوطه جریمه حریفان؛ همه خراب کردند تا اینکه بالاخره یه نفره یه بهترین شکل مملکن دروازه رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29994" target="_blank">📅 12:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29993">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IenKI4Shd-7KNkvbHTlRWYGFRL6VGpUKb5ykXSXu8DnqtbDSBASUhxpWFcvPIaWUvtVyDVM64k-OcmBTNYfSowQVI1reorQXB7_ABeJfazaeawyzwY9wFmhuXelCgHpxnh2dfooyyG94NJkxbSxSyx1kGEWXBKg72oJHxqbUMlz_Jmyh5muRAGE-Ttq3c_pq1q4oIcTpUDJHTmyLyQhvGS13nIUTwzGJPIk28VL5zC9CjuazbvA2TbZPN-_wzXwQ6vhNW6TgzMLwb_iRx_xoMwr6KvlsWYIAN3wz79xKTlAbR8a3odOsDsXKiXvH0DFJwi0LEnTQdHSmi2nqGlAO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
جمعه‌های انفجاری در یک بت
💥
🔄
🤩
🤩
🤩
بانس کازینو مخصوص بازی‌های انفجاری در یک بت
💬
پشتیبانی آنلاین 24 ساعته
🔈
کاربران‌میتوانند درروزجمعه‌پس‌از هر بار شارژ حساب‌کاربری‌خودازپشتیبانی‌بانس
🤩
🤩
🤩
کازینو راتاسقف 30.000.000 ریال دریافت نمایند
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r27
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29993" target="_blank">📅 12:18 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29992">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSJKqjDa4GXATE0dU7yEAksZ_O1Zo2Ky6PUt6u-IjpmvPCJRZkbEgjyvEYQwodXt_63tzcNpLqPMWCpw9mbk9glzjrCrCWnJfqaIYB1QLYrSQGx_pgL6j7-PcVLIF8yLzy9t2lOMrgzFA5UVrjf-0OgQ8AtQCHhEO1zNMo0cQ_n_VCdIMUAuzLll-SiNXzZ6UZ7B5Hxz1aBVUW74eN7KC59pjY_jIgPg2OhNhZSwlW_TS1mO6qmevoAJjbMhN8bDHLZzWShw5aKhErReIgiLN3vX9JnufwLmF_TrhD3OpGjvc79yGfzeJ5CQdjPlE3Hk0J-qLwPYpmP44J5_1zXeBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29992" target="_blank">📅 11:48 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29991">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zYhOdt_AdUQWpukLO7EDtooosS0s9om2gKy8xjl-P_XtyOJPuT1IpwxFKS4BHpESWTHW4MrhCNJO3aXlR712dq_T7HwdV4-VRWLuGaUQgZnexU9RsjibgGDWB6btb_rJZF-PiMn-XcQ08xZEPQlsfiUuVCNMQONmsuetxihel1MOBl-mKbpRf1DqAzC9tiau7k1h5P4ZVrB-eOX2dmByLbThAZ7S0_XxGwyam0bK7xMzI8uaK86DtyLzK4KWb37yOaF7Om2hYpOx2tyDGY2p1KmFyrL7RWyYd-wbP1MV6Ek8A_-3-F4He2F6pGDXgQhWfSPhSZp3XvyDUTBOMsTtpNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d818795d1f.mp4?token=dT2wfmVJ1AMeq1woUyOCmlxNnczm5CBeqiluI7n4SoRZbQswrfl-EOrkx0PhNcG_7UEEVXFYtKDl1Q_QZs9HBmf8rmJRBo40YMZdaDiWVVrOtWjveCC6AhjHgwCSCaMmRIZ2292ErZlvU1o8BVTPYPFzSnjJlU9tKAa-_JQynMQSHr9RVfik0Gw43duRBbJUlXdnh3mNypRjaoCp8PN_UWbmpERLElLzrtWH9qWeRM-UACSac-0TOaWzoRoyswH4DJh0evDAzMXcnViysunGV48M_IBau5tLaL1vYJ53Kn3SgUmJDhkzWYvBzC-j7mHCUKI8ivuCKNETL6Ve2Za7zYhOdt_AdUQWpukLO7EDtooosS0s9om2gKy8xjl-P_XtyOJPuT1IpwxFKS4BHpESWTHW4MrhCNJO3aXlR712dq_T7HwdV4-VRWLuGaUQgZnexU9RsjibgGDWB6btb_rJZF-PiMn-XcQ08xZEPQlsfiUuVCNMQONmsuetxihel1MOBl-mKbpRf1DqAzC9tiau7k1h5P4ZVrB-eOX2dmByLbThAZ7S0_XxGwyam0bK7xMzI8uaK86DtyLzK4KWb37yOaF7Om2hYpOx2tyDGY2p1KmFyrL7RWyYd-wbP1MV6Ek8A_-3-F4He2F6pGDXgQhWfSPhSZp3XvyDUTBOMsTtpNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دقیق و برگ‌ریزون عادل از پاداش 20 هزار دلاری مهدی تاج و دار و دسته‌ اش سر پیروزی شاگردان کی‌روش مقابل ولز درجام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29991" target="_blank">📅 11:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29990">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiJiqAxcJ4s5jd3ksqDaprHbGljwlfYprp45Kybx-gnIdA-S6dd6tCzohGvBdCyZA7ZdAoT1vgtEtbzL_JrzLa55iVGIB-aSq4iIfW3AptZaoqg88E-IFFQPGtMn2LZyywhbVoHkgas92JLqfpDd5831EvH3dfcsFnEn0N1Qqkuq4xrownbNUU1pECOyPYU9GVTQW32TMbjK9db_9oFFOJQFWUBcGM1NQZs78ls6IHDL72fggG2AN7HwY1vmEURDm-JVBZpM5mXbmdvNfHc15nhpA1iG86XIj_j_FF2amxwvIlbHKMzJh5IHvaqefGEXtB_V9CLPAtbNsU4Bpu_7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار جونیور
🆚
رافینیا دیاز با پیراهن بارسلونا؛ رافینیا همین امسال به تعداد گل‌ های نیمار در کل دوران حضورش در بارسا میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29990" target="_blank">📅 11:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29989">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RosLnKfcyKB1Kl3yckG_RZMGGWHZfQt_95v0NRw3N3JW9F2oVomcIASPgsIHkUv_hl6rpJm0tz4spc3uYeYZEsRv-w6ciprcsKDB8zyhvzgM_4KBPcyIjzNQczABSsaQ5NntiZnsz03-89K14DXLvFrXaK-QWHYz_OEFDt9k-8AQVFUlB-9_UHTzCP6mgqd3dkj3GnB5NpmjWy55b4dEQyZuM_atKXfec0o1Mt3JNeuZcQ2WF_F9If1F8J7h91GTYkS_5bNLie0Nul7HkG4VYe5kBrWWW2U_aMTucgeHSVcJpvyu7Idiu08eogiWHqvmliw_I2YCjGO6v0pV_AwiKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برترین‌گلزنان‌ پنج‌ لیگ معتبر اروپایی تا پایان رقابت‌های این‌هفته؛ رافینیا دیاز با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29989" target="_blank">📅 10:54 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29988">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKbls051N-w8up2YsRU7NGg0PN48LLhQe6RDAorDaInMBDKMb0AHI-d9JuztPf8O1KCPdba2wTZS4MEwJ7sN9uwQ8VnH7tbvg6vi3cBCmNGmnO3ddr6VkrPU3VSOu5iyUEdn9avfJX6c-8mwOlUvvVX2fq5BEuvityeAKs5Dv0lOMKk9_2ioEmwVoF8maFxC2XlqNrVlmkU0mzvrz15DuvzJOw-S9JjQCuVwS0_0p9-wlZ97rjSNhWmyJtLstH7yWGTCdoLouG-16_Jf04Yrlo6WW56RaowOh8lE8Wdxm1FCl4YftEZHD1d_ngqc8mUwa9lRlhRiOCNwmg2EKq30Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29988" target="_blank">📅 10:24 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29987">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=rHVTBu55SiamxdJjhZzGSGqEwxr7mvPN10gJXFdItGyBX_5XrnmwieDvlbFxr9AvjDQj1owqYOXeHKEGd4ullyhzV1Yl3NaSNFw3mayCYLjOXsbW6Ed9PlBJC-pyT9mhQ3EXDx0STCo5aPTi_cxE-RgPbReiHnGDls1GpG_G2wxmNPrvdxt3iy7vVXeLjDkV4MA67GYGibtco5hl8qinYk-Z8QGHgAuBlKCXFlWNfKMiHbfJSSvz2sB_hAgw22VfGEPGPYQG2RnVphmzO0XzkziLwDmZIsSacmIcAqrXmKDdsy2OfPVHP_B1SxN8ZRGRTh_zQVhV_tZfQlKyY9GDCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d749b5d59.mp4?token=rHVTBu55SiamxdJjhZzGSGqEwxr7mvPN10gJXFdItGyBX_5XrnmwieDvlbFxr9AvjDQj1owqYOXeHKEGd4ullyhzV1Yl3NaSNFw3mayCYLjOXsbW6Ed9PlBJC-pyT9mhQ3EXDx0STCo5aPTi_cxE-RgPbReiHnGDls1GpG_G2wxmNPrvdxt3iy7vVXeLjDkV4MA67GYGibtco5hl8qinYk-Z8QGHgAuBlKCXFlWNfKMiHbfJSSvz2sB_hAgw22VfGEPGPYQG2RnVphmzO0XzkziLwDmZIsSacmIcAqrXmKDdsy2OfPVHP_B1SxN8ZRGRTh_zQVhV_tZfQlKyY9GDCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی مثبت 18 مجری‌صداسیما روی آنتن زنده؛ طبق آماربببنده‌های‌صداوسیما از سال گذشته تا کنون به یک دهم‌تبدیل‌شده. مثلا یه برنامه تلویزیونی زنده شاید روی هم50هزار ببننده‌داشته‌باشه تو ‌کل ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29987" target="_blank">📅 10:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29985">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a52708609.mp4?token=NCjdTpQXMGE5nr24SL3mbisuaFBVkA49pOjeuEzifxOu2csALJgILIS38pJoMC4o37ho4zR1HUhhr69AaV6YsiNRF9Sy9b1rFWJEeRdVzIzTRI3H8tnDLupNfr5DVWm3i7819SgoAbeGpqH6I9sc-8l7GE5UNQTQLq2t9IACjck6VnBPmJDDJ-11DrbZdV4ijm7D5cWZQZ3KoDm8XDO_jjmDzdVa5PZUSbHarBsQyc7iPc9flRW0t0ljmAzmOgRbdzqwG3KkDh5_dIfuK2Ny9EtEIFU-J8GsWkqATkNSXyvcTvEKZoffxK0zBQbKvSWD4vfewZ5vF1fVQgttOUWP-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a52708609.mp4?token=NCjdTpQXMGE5nr24SL3mbisuaFBVkA49pOjeuEzifxOu2csALJgILIS38pJoMC4o37ho4zR1HUhhr69AaV6YsiNRF9Sy9b1rFWJEeRdVzIzTRI3H8tnDLupNfr5DVWm3i7819SgoAbeGpqH6I9sc-8l7GE5UNQTQLq2t9IACjck6VnBPmJDDJ-11DrbZdV4ijm7D5cWZQZ3KoDm8XDO_jjmDzdVa5PZUSbHarBsQyc7iPc9flRW0t0ljmAzmOgRbdzqwG3KkDh5_dIfuK2Ny9EtEIFU-J8GsWkqATkNSXyvcTvEKZoffxK0zBQbKvSWD4vfewZ5vF1fVQgttOUWP-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
محمدجوادحسین‌نژاد که جدایی‌اش از ماخاچ قلعه در نیم‌فصل قطعی شده امشب از نیمه دوم برای تیمش به میدان رفت و با اینکه بازی رو سه بر یک واگذار کردند نمره خوب 7.0 دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29985" target="_blank">📅 09:52 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29984">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogqBmAS0Ittu0bLFLmmTmu3DtAx4QlXdVFFolbyPEgn5DRk8gYxAZi1Scb6Hc7BeHTgUiPbNbLVHPPgpy0rJxm_mF3rWZc4tpZ2U8gsj1uR8kGVsLp_P_w2_iptLCbpt8hLE5WqV--b_rS8JlQk9Z1P1IXR-L_Jg0NKXb-p8IAiljrb3iQA_RQPXenqKMLJdDwtfLzzsG0_6GrmukmQZRKz1JTECt8H7w6SO66uh-p_61nHTFhj-ri0yijVx91N_Z-ywOpyl8LMEunlR854ytfoceNKV8UExn_bcTzVtuI6uhrhAcNFO69rSiIfAK5ScZssX0NlMKUHGnrGbzW5bOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امباپه‌ستاره‌رئال:
اگه‌میتونستم یه بازیکن رو به رئال مادرید بیارم کریس رونالدو رو میاوردم. او در این سن هم میتونه موثر بازی کنه. اگه به رئال مادرید برگرده قطعا میتونیم یه زوج خطرناک تشکیل بدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29984" target="_blank">📅 01:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29983">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzmfOV8bY5vW40rqrjO-5I_Gos8FEcVL9uKs_tjFGRRllp-31QhfKuAgV7GA0RFteWsN0bc2UZ2HLtRkL5j2c12cqtqyWLCBKVCFXQ6M69eT21MfQ6odTGJrDNmgHhLtNINKSf5h8NAneB0njjEHrf-TSvC_98mj9u0yLGq5W6pfSRYlY1grbRulwnrj6ENtmtyqcmGUQwoRfHFvsycTpE07vHoWdOj21D_H_Q8HMxb9TDFyyonEpbztWJs74VcFCc6ZzJAxm2hXIDLqCDXK9GkLftvIP8buu7I0ZkcQv0vWwLK36R3gK3WQ-1KsbfInWKdiGqNXycQ9d5X2imSRIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29983" target="_blank">📅 01:31 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29981">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXBL_IUrCDnx10h2Y5JlyKyU9D8kd8HBAsq5lUSyRAzBkrmZnJ3t3oKvQKpcIP2U3oCYNZ90IcrjfPTC7UO2Q9sySHftX_SiAv1gJsvZryoP0maQontbn-oH49_lE91vd23lOMqDexJgIpmhDqknszvhx--vJRZDPphqS77IxBKSKBEmto0P-vMu0ulr62ZATaokIu7l0bx0Hk2dwY0DxrHmzgRkZSiwK5-osx5jRgL4m1pv1hAFwtc6opWZib_zW3qS1TzYgS1NjEZdqs7upTegSBWVdofb-dgw9S8SXYvG85nsAM9-4HqZaZweSHCCRmx5A907tynALMm0sk768Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛جدال آلونسو و شاگردانش با برنتفورد برای بازگشت به کورس صدرنشینی لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29981" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29980">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw3LnjSjexzwVG1GQTVslvDCtLsmLLVHMWo5K2v3ktk38CGPIqs4vwRXFXiEgxShVRpEF4O_2CGMcmkdymY8ZIXcVBfNHKa7GppvUKA6an2xuyDrCayfhZ04R91wvpj9T6X_jsvkTs9gCnSYMQsscpIekkC2DZ_sh1Q0pb1Cdo0Kl8o3ZJb3CGpucB8hK13QkKDBISWk20KfZXvxSgVKCRrfK-xcUV-N-R-lRndJcfzMiUu_bThrvb5gDmbfn6rPuFPSkXXwBny_oILV_XL2XV21z0sS0V_au9VEGf66h9yyxunT_hzpssIQfAMMxrdo9UoUCdH1vH7KIcxZ_xUKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازچهل‌‌نهمین‌قهرمانی مسی افسانه‌ای تا برد پرگل یاران اسپالتی در آغاز لیگ‌اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29980" target="_blank">📅 01:26 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29978">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">📊
عملکرد بازیکنان رئال‌مادرید درفصل‌جدید؛ امباپه با 8 گل‌زده و 2 پاس گل برترین بازبکن کهکشانی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29978" target="_blank">📅 00:55 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29977">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4Av9aCPsoJDdqCddCwBVkfYDodn1COugiFGGtXrMVZGEPjBg_vJRads1QqysaGZCRMeMoTkspLK0vyshomKVk_vpLmNGXoK-CHVcfeoGr7kvaftFiND1sI8hyNdYkvkx_eBdF1ISzP4IVRQeJH4fGIhDgqgDtBrwIpF-uozOWFBLcnocVyPeXFpNdUy_VvmMliOkFX0lNwBWhH2-V2p0eykXtGRUm1388AbsFRtdTeXVa3jJprKNuD41Kt67fRZeJ2179xlrfQk6GsqSZjNjPmyzOjLwL-70biYE9Fq9tAMnjymhGB7gpaLOJ0sv94dbyk2iK37Wf8cMzSGhniq6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29977" target="_blank">📅 00:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29976">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwW5mZ2I6JyRr2cu2GSdsvSzwvtkArMt7gjp9n3Z13EANP8200Qo2EyaeyaRo0COJTdm2sl809Xa0L4k7VgsXo5HnnkGXgY2wjC9zAk6yZYCReQt1c5H-NQxRpmPGGgxQdg3PtufbajNnLiyRDkTVug-_YMCu-QPjH45Ae9WUiXT2Spun--dQ6_CEwdxkY9Au7sKp0YdvC4Lxih6nJI7ZM4Xe3izhNwENZLnZsEdpEaA7ZD4SzL03-6jtld0RVZOxgqf8K2PyyCMGglj-mPk-fhn79H_9weecfF_lWv39UglT4s1vYYafAA_z2XVw5vuhZDqZyWpbRl2zXDvy1XcjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29976" target="_blank">📅 00:27 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29975">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeCUOmPDk1TxvTiZ_pVhUjkm5ceW5xbi_O7QLMj4sHDggk0u64_6vZ53FkkR1WycWg3y_5smwPokRYFcQ99YpCOm6J5HsFHTPjxhs2gUzqvY-pw1T2DHJ62fP-jBYOM1hzo-1gWnRymhCVkNHsyNkKYS0QZrNlEzzvVCodPvBL9jwmSPqIyv-ImBmtM4GEzSjB2jSrcvOG-0g5ozBHDUyVO647eGSDGPm-Pvja5nDV5pA4IxBKur2XYlN7HcMcHJySOPp9kv8pd5-nv-sucOR6aM55lM1xhUY7AdDGLTXIQJ_hgek1_gfv_zyIsxIip8OZyYvpoCskVcHpGTg9ECrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این پست برای رفقایی که بدنسازی کار میکنند؛
ویتامین‌ها و مکمل‌های‌مهم برای وررزشکاران در کنار یک تمرین خوب برای ساختن یک بدن حرفه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29975" target="_blank">📅 00:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29974">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnrc0-E0wEjCKqAPGx4EAM4C5BnSStUcvwbiBYqzTbwwM5-Afxhfqxsp69SX0tMEbXXkZDnhwx-NEZScnYmfZtXk1U_IIiymqvljdKpA5XwwI9T9NpNpCUAMLFOi_u5YL71Vna_SXeL4BLMVoWUjcTu6c1q83TtK32YoQKL4p4eg1pldWIAp9lHhAgZwfOBpTYmGA7zfKcIYDlDuhjakkLH0PIx0XaaJz2I4WEFxJf1WIPaakvRO0KwTORaZyZJjHCNkYVvM1PNvkLpbb_WRMOiystQjq0G37lgG9VOs2iVx0P6covQP6HcVlt8k7HLeqV8QItmpptQ2usA5m1FQmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29974" target="_blank">📅 23:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29973">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ala6qJNumOgm7BvrXgwRyRr4pAX-qOC2iOAYBf2d9vk7YICpN9cz7sDfSZery9ShJubi881WGcqUY561kt3sreJRsP5utv8ApLUTFUf3wRB3VwQ38pwoKw21l8ev3wpBZ8ciPR0_JHJJSij0Z0rjHcqxEjin8NnhHqL1spSZ8Nn7ePn51e6WyAOyNY3K8dCK5GF4ENrVKD_gRZ1MS2DnvCt3nvbImTs7SEJbTi6vI-lmO0PgPP3AjCi1CdqHYfh1YXGx7qD0r1D5JY-jPwzVXb3i4umL8XYyEkPhAObZuIul_JnA-yPj8EeRU5yKBcctnNJSQzh8N8VWF7wbkNpC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN
: درصورتیکه‌هانسی‌فلیک امسال تیم بارسلونا رو به‌قهرمانی لیگ قهرمانان اروپا برسونه لاپورتا قراردادش رو سه ساله دیگر تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29973" target="_blank">📅 23:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29972">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8Zd2aKCp6HtWRs_Gj0JaEhzsftX2ev5A0N-UHEZRis5cyJ7McAozkFRWT8juvGHwhB5xr8We4CdEPHsRb72XA8etEIlJeUTu-lVsp8uzaGlI3L3wBMN1r2i9U4l1Nvhoc7t8RsnkRXJMFfmY9TiF7r2uegvjVCud4PK1YlDLTkt8OvmpAQTkedN3vuPsBQy5uxFG5WQ3ocKI1qS2uy0N7DM0BzBKcjuuRaBQrPGwO8_2EHPIaZDPsKS7WCSs8G9HwvpaTh5Gnt8CTCJrx4285GVf2ecOKgiWH7gpYFp7B8D_MA-bkeSkMq1pVxug0A2aawmZM9fygQ0AWVDJ_QDfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نوزدهمین‌دوره‌لیگ‌برتر فوتبال زنان از فردا رسما آغاز می‌شود. رقاب‌هایی که به‌نظر می‌رسد با حضور تیم‌های اسم‌و‌رسم‌دار زیباتر از همیشه دنبال شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29972" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29971">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QB4Afa2ED13-pue830vGAX40wBga6z8us0GtWlz1yj00hz19lomv5Pyu3mx6xjL7UzifdMvkcxeUcSbX-BgBzTvT2rHbtf3cy0QgBHaNum8dTjYdwjptICIGdgfHvDmMi1YQbrNzVxAhoEuQaDuOnhDEFj6GpTscMLK-WzKoN5wN3oH9J5rY6TnUbejChq7n69E4kyTFJHyWrt8WnTZ02gf1RTct85teOQOYjLv8KjphJrYSDc2jQs25qDa1L6e-Rk6jddN8YqulKj1mDAMwdmUUBwedBAJNmc3KZoDj7OH9ucUyG4l1wZ8Ta8u6s-JwsBgAuyOGikufyIhW5YF-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29971" target="_blank">📅 22:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29970">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPH9wkPP6OPuXqLdeYB3fuWS3-qx_VLjbFUktcrOyuSJMwKbzNi3b1s8NOiKyXcJnPtOr_nf9Sgfvg0QqgiSraHOR7FIt800FcIzq5tH_g_NzNi_DoLvUkLUv9Mj9CfpJ5ZRu8nm2xrMKDYOW1hRuD595wdhBNukVUI_kXtHy6OWMPCOTemiaZ88deXYYf_MtaGimpUWfFesGjRNzjpMmjEDF9ER-LaINAGP1c_RBLxi3b9pUedKpnivzeScwq1OZUHGo1K4M2p6PhadPl8tKtV5Iuq1aFUGLTCWF2FekkkWReVffGzNJn5HdfCpRjzp_nf_qJlqh2eCnt3cVw89IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29970" target="_blank">📅 22:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29969">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=icRXyD2FunW01gkthVR3ubwBTNlKs99S9MQ9U8KKwQp2oBH1PEICquJYg-8lLsKKa52fWn4RmdgGvr5WsnGjEu0QPipDUIzBaiKN-a1Xft5KaLkqWA9LgHiZJLg4Ftk1KRz8SsCfXtYTAghuaqRjPjS6qOVC8scoG2QNr7EDXuES_yEjQ3EGzohMBoR2SSeiWgMEVAcbTvZLMm6lD2UAq1_EdfS9i3EmXd_M-MqLvonHB1Udax6LwaxVRYlHJYRCS9wgY0bkyY8CclAXU8pGmuejE60UL4modc9P1vBlMtcUD8MHau70uAh7KT4rROhYvlyVhHoLA-ahoSkSv-PQtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/372ce8a577.mp4?token=icRXyD2FunW01gkthVR3ubwBTNlKs99S9MQ9U8KKwQp2oBH1PEICquJYg-8lLsKKa52fWn4RmdgGvr5WsnGjEu0QPipDUIzBaiKN-a1Xft5KaLkqWA9LgHiZJLg4Ftk1KRz8SsCfXtYTAghuaqRjPjS6qOVC8scoG2QNr7EDXuES_yEjQ3EGzohMBoR2SSeiWgMEVAcbTvZLMm6lD2UAq1_EdfS9i3EmXd_M-MqLvonHB1Udax6LwaxVRYlHJYRCS9wgY0bkyY8CclAXU8pGmuejE60UL4modc9P1vBlMtcUD8MHau70uAh7KT4rROhYvlyVhHoLA-ahoSkSv-PQtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
بعد از پایان مسابقه اینترمیامی مقابل کروز آزول که باقهرمانی‌یاران لئو مسی همراه بود "چیرو" فرزند سوم لئو مسی درحالیکه بعد بازی لئو رو بغل کرده بود،به پدرش لئو گفت: بابا بوی بدی میدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29969" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29968">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=ozEdJVPpnepuYghHzUIvHyGB7pfMJtbnG8rKQQ7NWmx3YRPh4FGi4E8vfcAesfU6uRldAWzJvTRY3H499NGBO8L_b8ogOOA1OvXky3zYG6_th7jwb2G2tzJgeAdGcI9bpOJIS8HyNNiFTdabCICN5hyoruANpjkWObZ8bU5dwsju2SDgL_Oe0usWyfv9bdTczyKQIg5-OOihgzAsTnJO5BSEj88-CYMF1JWair2oRJfTlJDMAv97iRCtet5Sx4GGlMQxo2jBXQ8lVA-vqL-rhP7LjQnimX1OLk8cnkX2lrf0rbGJSMu98TLVQBathiRjLP142Pz_zCTw_QKrpN0SiYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f4c8fa49.mp4?token=ozEdJVPpnepuYghHzUIvHyGB7pfMJtbnG8rKQQ7NWmx3YRPh4FGi4E8vfcAesfU6uRldAWzJvTRY3H499NGBO8L_b8ogOOA1OvXky3zYG6_th7jwb2G2tzJgeAdGcI9bpOJIS8HyNNiFTdabCICN5hyoruANpjkWObZ8bU5dwsju2SDgL_Oe0usWyfv9bdTczyKQIg5-OOihgzAsTnJO5BSEj88-CYMF1JWair2oRJfTlJDMAv97iRCtet5Sx4GGlMQxo2jBXQ8lVA-vqL-rhP7LjQnimX1OLk8cnkX2lrf0rbGJSMu98TLVQBathiRjLP142Pz_zCTw_QKrpN0SiYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌انگیز و نوستالژی از تکنیک برگ ریزون نیمارجونیور در دوران حضورش در بارسلونا. اونقدر خفن بود این پسر ویدیوهاش تموم نمیشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29968" target="_blank">📅 22:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29966">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX3xfYtVFI_VIdEOxjIJw8qsJgi5mzYq-5HrYLmjjLLRS6PcX8HWRT63XdQphlcyoCr5qL_OTj4YTZuQ_tf9KVvhjZcrFVkGQFNVnKxxK_ubA6UMQwJnHGvEOiDMI6uPwCcBr9DImkChgFY9QKbmyCtmOCxKhMEA4bVFg3bGBfe2s4bBS2SyV23eC1KLxTHfuv3bra9BzVW1xu-OScbzVkc7wuuY_lpjOc1VCxnEbrh-r2ugAsu-a1JwWzoX3Ep9pIAcJJo0-n4ihq_bcZBKtzmcEHu4x1JbjM5fbVUVy1aHBjJWavo2qN-8LEUV2l8V03ySMN3PDSDCobVgp5aOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29966" target="_blank">📅 22:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29965">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi6sX8Z6jZqk4wY6g-8VwOj5URRknsRc7RAb1AILZbdP-u2i3wlVNq-vIacK6-DpgDvUT8F-7ouHEo17NrsCaPu3hL1KMvokVOXJz66Wwfl5JdfiUbNnw0BcjYJb6veTGX27WKEOs9P-nZ_Vz34v-Qmf2kSJwPSuvLt_jv4IwzyFjroccdwQaB3vV76nhSegFfUPwBdsXcumgcP2ZWomev6U1RSat60SonQ6fLXjrrmYY06Aq3O0RUjsMouSV-j_WlQY2lkMZS7YCnby2SU21KzjgJowjQq7DK_yQ0rAcIMFZ_be8yiuH4_BrM_03CJhGerzpCEI02PtqbZ7m5pU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک‌تعدادقهرمانی‌ستاره‌هایی‌که‌بیشترین تعداد جام رو در کل دوران حرفه‌ایشون بدست آورده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29965" target="_blank">📅 21:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29964">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAL9OznS1sa2DIv7RdgDzhSGRXuFiXRR-fsrG9umCHTH2trLmFj3wUhP2aHbBbTAFVAx_7GMFZBNfydd09jMTlml4NQH7R75W1mUO-COpnbiOifI_NsXkxQNXvRW27BRs7xu65IVLDlOzIuJBpzE8R8e-A3Cj48yfGAUvvenlU1840lz0K9-0yS1HDVAladZJDpJ5urWdyhtL2qQB65G8E_81E22sNRoKMP19s56B4i9e4mk2ktQF9_wcqleb372aW4PvpE0L7nCmbPt2HovYQ4s2sRxskt84sAxLj49r59uQxLNGhx5qKdhIv4j7xn8K4imrBZB98tQ11B5A0l8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29964" target="_blank">📅 21:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29963">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfvvJXej6I-Ld_2_1WC00uaxM1Z4AcL-uD7tP3-6bc-lvSmwT_vJ4_9WEeLRslD7ZaIs-0xPe2UDKgW-VCsKHWF5DEsQgCIDjRYIOF_5AxMXxr5FO-yOwuRWwyV7pfOJTnah05tqR4fQ-d4YObGfMolxXmpS95Kr63SwP4OQ7oXBWpGZMh0pvMdEiFVXtuXs82RCsN7g298k4zlxV37OPMCQGcioL8MIRf-b9j_NocQJAOeDEZFjKBpHaTdrc5XXvQm8leTKyp_ZVqG9MS4hmJE76Iw9xD-tzw_i-yhuDip5q04OPt9b-6W6Al49nzJ2p1nzhwjRpx0QsV6v0USbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضا بیرانوند دروازه‌بان ملی‌پوش تراکتور قبل از اعزام به خدمت از تیم تراکتور آفر تمدید قرار داد سه ساله‌دریافتی‌کرده. درصورتیکه بیرو به‌این آفر پاسخ منفی بدهد بعداز خدمت بازیکن آزاد به حساب خواهد آمد و به هر تیمی که بخواهد میتواند برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29963" target="_blank">📅 21:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29962">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e67scl7J-PqPnGcPZ9mVxREYAU2T-A8C5wxUlpxZ60Vx0UG2FHGK8JjGqfm_M-dqCxkwaTIm64JFE4owuSGU8ekjdbIeji5mOkz9OK0OdXaSRqfDvyOvuQwdrV6bXWSVazAn605aBGjblPwgSqq0IcBstXIlcXmrMFzMzFsMXsJCVJJLAieqXgAhjqy-9YJhqIkW3z6cGWpDArl0sBb0nnyHrvL1jtmfoddTC1GhG7evuN26albAFwTuVZOu17Kaz4eOiPHAOBGdp_3nEf2x8Bt8nNuelvMdQW20SuuXAqN692UOI-mFE0YVdCfRoVZaSY-x4nCqiZIDVlfd0KCXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛ ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29962" target="_blank">📅 20:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29961">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq-i7pDi1QIR8hY5VomKTtpoDru7Yat2KP8VASuq1btByGlprmvKulda73N2vga1_2kBX1Xm2QOD9AVpVLxz00QCKaaIC08kwgLSNBAHYRlGO_j3riJr49SiRGWJVr3DGVhAz5Ys3w6GWaBSYOCjKZzP4ysOag_EQnsg86gFtKU0x3i6oiHfYN0-2HTr-fhuFEjp-ziOOLkRQF71-2QjvZkVR3DaMBiZuSW4IembUg8tiwkXWKQbdICwOJznIsgBB126LMa3DHTI3hxwkxFLWQwAYwTr_Ryx0s_yo2kiYqFSRr9ptVkyua3Or3VURjosTKlgcKOuVznhOINuk5ebTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگهداری درست از کنسول بازی، عمرش رو بیشتر می‌کنه! اگه داری این‌نکات رو رعایت کن و قدرش رو بدون. الان‌شده‌حدود 300 تومن. دوهفته‌دیگه 400.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29961" target="_blank">📅 20:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29960">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8yJ56BWMgqVWNuyOJlcUH7d1_ZlJ2y5pLYhXBDzQtn4M0dxmDM3CIxLdtELPFCXLrN67q26fusk6DqjFq_aqXRfWcRAdsMvGOrobsueMHwCiv5c08JyQX1rUfiJbVtcUW_aACBv0R0cquFKjRidIXS5VHPFtT6XJLgtrJBkbrkVjb7GPneHnd8C2aAHNuFoKy8Ev55OPryvW5qzLQdhJ03BVabqsxo4jIEAsgTWbab7IPl9YQymub55LRdWX1uS7XgO3ILr_vzRb4CZXI_y09L3ffosUw-hO7OhNf3nxcJkCIJPpEAc1jX8H99A2lrPOceMIgl92KQOJdldHk3d8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29960" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29959">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gF60wMJl2FX0IP5zs9DXoS5ydMuRYHwNshQzqcsYdURb6ginvW_MISByk0SyRBNtMWHDzpnbIYTTgNhwsczwJCLj1pui9RL222M8RtGP4YI18cNzY7FD2kuvpyVvAEWqjekJf7Zq1HQwgxCL_7EqijRvy9AIVPRYBixiHmNahueZJIVH9PGYQAPulR5FBd7I4e1EQGx9cvUBf6kQyt5XPx4b4I8EHJSlFZZ2sC702IOXW_G5SNksibPsvveVX4eMUfKDuK9jzxRmLaopUOt8rMsC4zCD2I-JdwOF6S8Aqu5nNydcqonDFCk3FCzfGPglRyVoglYnQGqIGHA6uDiRfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بازیکنان رکوردار بیشترین تعداد جام در کل دوران‌حرفه‌ایشون؛ لیونل مسی با 49 جام بااختلاف پر افتخار ترین بازیکنان تاریخ مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29959" target="_blank">📅 19:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29958">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0spdw9oSFmmeVFPMc7v6vLCXVvvzW7yT0pz67flFBcIB-rKNRbpLBys0w6y-f4tTZYynyvdN_9YWUjDB_Pu1mOn1eII-AMWM-9ru7cXg_dA5jiMDCSAOIdX3uwTjUQRBWqUKDt704_XByUbvAUfHevjz-i-TgGWILmzakGhS2GEqLzcDlrpXeTRXOsEyaaCVT31Egf8NOImgBiJXkb3OgYx6nIScmz7rNAZ-M_fUp05sTOAtTWH7eT2AKUYRIPjBsBJhua5FrA-KESLwftxLIoC5mn7xryAfCXiRP8TbqP-WhwgFMVLqTUX9wYVMRVLszIFUubYXCsOpZB9LvqgSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29958" target="_blank">📅 19:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29957">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txOLwBd_GFoIjwATef88p8Y9IPqqBcnxlpByqzL9wNlym4XWDpznD3x9udQPWlNYOltydnHiHeqrz5IiyFBiTFu-ltRAJYWzpZaRMkQCpznVgwxwoaQEe4KPju4wdTEREgAFGJhgHTOajZd-L3jqDc0M3_WZ17gX7O_gOzG6FsEHPotQGbspYOAMXSXFcgHaMi3LfFXZgh-6SGY-NR_mjLD3t-_KD4lmaGUzLAufsiLIwk2pRpVRUDo_K1JX6Y0btYmy-jRjPFRDLFU5YSZorhiMpLubsSQ2StjddVfvLDcx7GlJ1WoScbkNRJQ0ORmlIZcfObBX6StS4rNOiHzXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس میخواد درپایان جام ملت‌های آسیا برانکو ایوانکوویچ‌سرمربی‌سابق سرخپوشان روبعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29957" target="_blank">📅 19:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29956">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYFriLMCgdNGpm0gnzc5CbJFoB7H7ELUKLv-O7s-6DTTcKTG7VOtQCVC8FjAbgow4a7YTu9S_AX12iAl9ZJY1d4cBrjoAAs3GOnFsBvRPWLJ4UFneWvp7vu2-EWIp_ho-mgWUwTZm8Q8UGVxsGEqOBw5S7GNqOqW151Th-EV5Vu5RNq2wTuLRmzYHNB2HTG97gG0C3v73lQz4A4GQAWPP7_redd81K3tEZqrh-6Qns4NLX8P0TteYJZu_RQ-nFHPanexqgkEz5envG_g8jegDmlg1Z2UouAL_VH1ZVLfPcKFLfike1KLAd6e9Djx0ZP-9o5ThX254UaE2rRpKmYwog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد پرافتخار کروات روی نیمکت امارات؛ زلاتکو دالیچ سرمربی‌سابق تیم ملی کرواسی با قراردادی سه ساله هدایت تیم ملی امارات را بر عهده گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29956" target="_blank">📅 18:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29955">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLDDoxpOWGj5kJD1lLXFx3ANMMjnMXEEkn3VWUPwiGN0TPHQV90t-xNtM6JQ3b82e4usk9o1MBI79FMJDCDroshZMUUinqPXkCqHDlk27Ncz01tH1l6B8ohdAtR3LKLtSDIqg-kbSeFx3A73Hod85pO54USUFoQpuWbgUgPfoPrwVKRzoerrtmm6HOFSCo0GJySXaqWpnXDmGwcS3yffC_ort7j3UW7XCICGJ3eFdsRhzYt0jFX5QPJaScnnBkNoTEH6SQdjGKwVCSmkU2m8WzDVhgOohG14zwKJs8Tn2fc5Bica83UvQ7nr_30s1DoS5dET7gJ3Zpj541zTxy8x0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ارزش باشگاه‌های لیگ برتر ایران براساس آخرین اپدیت سایت ترانسفر مارکت؛ پرسپولیس ارزشمند ترین تیم این فصل لیگ برتر ایران لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29955" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29954">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=AHLFWEy0AUZxb1Rf5LJvM4ZjIIopDx0rKzaeeZE15hFN4EMs6EF6DWIknYKw2nIHmqRhwWNlirXLETZES8ymYSAZj88xzThZQQtD97a1iro6SBIt_cDF6rJo49FOVEc3jM5tiyG79aGyVq18ZUfvVX-Fij_WWTo34hp1wReynetzRPj9gG7yanIxnS5wYa-iqV443TlOLLurHcNza4DogE47y4Ar0a4sUoKidrYB7asF5x0JBjLaV0NZLPDyKfuw7q0j9g8q4W5qLwEBsS5yuoYnI7thmDY6WmxBX5OBUlTsVqJUUtK4Sa-EqUEZcxGY8tx5g1dBuVosrV0vgrvvEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=AHLFWEy0AUZxb1Rf5LJvM4ZjIIopDx0rKzaeeZE15hFN4EMs6EF6DWIknYKw2nIHmqRhwWNlirXLETZES8ymYSAZj88xzThZQQtD97a1iro6SBIt_cDF6rJo49FOVEc3jM5tiyG79aGyVq18ZUfvVX-Fij_WWTo34hp1wReynetzRPj9gG7yanIxnS5wYa-iqV443TlOLLurHcNza4DogE47y4Ar0a4sUoKidrYB7asF5x0JBjLaV0NZLPDyKfuw7q0j9g8q4W5qLwEBsS5yuoYnI7thmDY6WmxBX5OBUlTsVqJUUtK4Sa-EqUEZcxGY8tx5g1dBuVosrV0vgrvvEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29954" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29952">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9-BiAWF1H5rgWsp9ZeIKJJPwZU_XqSwQssnOnWXhER2cx_wqpQnuTXGvJEQ8wHkoXSCIAkDkKjZPEG5Zt2GBz_BG5gmPGE1oNsPAEC1El2qbX1gG4G9rtaPSFTsbxHPloK-uplj7qwlmDUNtwex2zdFJ122_wkkKEYTfsZdsktyi7b3Mpcx_o55ffc2JCxnC015SNlUTNjUe1BIdGD2-KVq1-dldEDuimGJAQugkQIN4bgzrmzIqsXAZCtRr1fu2WM3-NHj_-M9bMLDU6v1GetyjxkIwrq9FMOz9nHFxeX5I2LErFXagQq-ndUgn_4r7gdmOIo5naacbIR024H3Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29952" target="_blank">📅 18:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29951">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtBgOiAt4GoZXwfHdDSsC-Ksjf0oF__3LqseYrBWyzr_8BGB01O87smipwQ6Nol3dh4ofZpZLsDn9Kq5MMEwZm5tcInJJx-WkE2CA0AREeMQm1pVb_NVE5OaTtpmPNTA5zSULUlI8Luwv5rq5paY3Xoovnbyko5os9IXFNl_1FdhF5G9vwY1NwVupWgOhu0x4SoLy1Eku25Tb9F4SLZd0z1OnRVc0s8WUBccTS1Yf1K4rLTP35XMoBB2udKYR5od8uFBe4BtBnGC798ZIV4_QZ-OXFVugmZLNnVv-jRS7ptosoy-QMAQuI-gB339Zd9IvBeq0ok3ct_mN9g_0Wh9Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌سوپرجام اسپانیا
؛ بارسلونا و اتلتیکو روز 13 بهمن‌ساعت 23:30 به مصاف هم میرند. روز بعد همون ساعت رئال باسوسیداد بازی میکنه. برنده این دوبازی مسابقه فینال سوپرکاپ رو برگزار میکنن که روز 17 بهمن ماه ساعت 23:30 برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29951" target="_blank">📅 18:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29950">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qaq8DFXaHGDMNdtekv9x1J4E6P629J02lq1EB969NBHk8SeWrriEmRbFH--F4lZsQKgNNVdx-apnnIS9MHbYpTff0d7kF0iv6FjNqzKTAmOzP51NBJLq58L80YPpm82jAjCISGSWm2xaiD5JaGfN1YbaJN_5XIWt1V3aGT7uKqw22kjqn3TWxFb1q4--VjyL5v0awwheKWYU58taSdijnTEHK8rLVXHtw4ROcPfcZuQyxCYiBdH_P___awfw4tKrnZlb6cW6lFvFWqc0gnYj14T8zV2YXPkbYYSLia75EJMUBYG1nqLjJK-uoALwEretcwnzL-jPOrwgbMacflQjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌پیگیری‌های‌خودراانجام داده و در تلاشه تا علیرضاجهانبخش رو نیم فصل به این تیم ببره. جهانبخش از اول دی ماه سرباز خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29950" target="_blank">📅 17:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29949">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIF-j8vkoRk00D-g387u7Plrkiprjo92fUoARp_qu6ARgpFNxyAkQV3zlLnHn4isf8gyiM0ODo_Db7O9VH1bmqpyr3mMJ42QwyuQmBRmPCc4yuxtqZt0IcwdamdxjqlnBg9FJE6GLPzQwjmf9YZTA_eFC_3-q9V2zOyxMLx_4GqAlX1Gwsqys4B_oESBW3sq8Sk_NjKqyfKVhFfDsoqV11l7pSCqqDQvXzoIsRZSVQYsNItYqRb2rtkzQRfi3mlevrNlT35w9A102lwU3LOV2OdqHZrsuP-4XdOGemUJx7uxwOZNbYa69SjhQRa7XONVwPnU510TXqm9DKDsfNcniQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29949" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29948">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdFkoVS6fWAGDExjHhqL4FJT-BwtQ2lyMIFpiAHTTr8zn2IvbzHc0-MZ5YReUQ7aX1gmmzIcN20pBBUGK5PyXlNrUBSTYQ2FwkBN8IjHMZxEtsp-3_s2jOxrK5UT64EQ7H43zGGAf9Pl6_Ntj2m3vDWwdSRPpmwBq1-sEcHj-kqPlAak-3r9gCDlnTmeB20WRE5hE80QAUcVlr_ejm50rNi4eYusFDjfzJIZZQM3pvCczku2sEYsRMwzI0Wp2EKSQM9lkVwwoJBiTeqq22QQjpzkDqm8q7BwSXzKThEfPNPgDuSXo_6w3dWPGxxFeD6Wevy-x80HlmlCwa4XjBlHWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29948" target="_blank">📅 16:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29947">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgrSkFqGgrHN5GQ3vFruOERysx_7AZGe5cCQBERUY5gu3HNrcpPRC1gkjDbeF8tTHIaQWLAZiXYrZ6Qv0F78dif-Vs3x6IylHdi3i6MuBNtwOpBKIfXvEmvFTBgBEZzzvGRmrLDPSscBfcDwun7p8lx-ohqQ_HNZdp0OiJqR8a_GgY_Qu26HUSCWSJD-4rTcyAjWEpPCiP4JiaV1naEQY7ClphqXe6m-l3Hm02CpctUf2hC1ukoHJy2ZaZKgFG-DrGg3f49eDbctun9dY06FbAAps_jEyBn8WJQMUwTDmZrWX-jKo6QeFaR322t0wM_a__ckfsCNQ8iY0mjh1VUEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یک‌ایرانی‌مالک‌چلسی‌شد؛ بااعلام‌باشگاه چلسی، شرکت‌های‌گروه سرمایه‌گذاری Clearlake Capital رسما 87درصدسهام چلسی‌راخریداری‌کردند و به‌این ترتیب بهداد اقبالی تاجر ایرانی مرد اول چلسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29947" target="_blank">📅 16:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29946">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5e07abed.mp4?token=R-LlpZCYI6yWsYXltbsIA7tV9rLy5gcGcxbek0AqxnOx6OxiuZbuC-_T7-H6ImkUNA8iIRv36BzWIUL_5ZqAYd5AmyJ6odjqzdkPmxjUigsMWyxTokilEkrCpJepEjE9FJB7RUPwQROPW4g75-_uByJ4PPvJgmDSluB2sbkNWNy_veuWwWju5xSDuowxvOenOrOS-RnhwAszcMzV1YMzxKN3Yh0PPY9uxogcoB_JjhfDrmYLGhg47Fjr05OFrDgrbz6EREwMjLngLSUQrt-WQ0MNKDlXJq5AgAAgAboG-dPHjRFAg2mHn4ScpBUrDo3we8NtyEoFjM0X7QHoGh7ZW72pD3DcPECjuTayFfd83Z_1jRDkIQUafst2f3Ho0hqRjetq5XomrL_NfGOYw6SPvkfjYl48cvIAwbxgLelmEifK4YvAANeNRpA5UW5eJsBKU8DCvFbKjmVih9Cs2lZgq6Sdf3Ju3uTZLP3sOqy0le1eXAphDWKIy3o9sL7-F6TWFjxv9AO4fUmlo3pvGscK8jlBIVVyfl-obkLGSV5Cezz1kF6_lSd4T6IlXA9GpyUsaSu3ra0T7MoJM6YadEPPUyLsEgqjl3ubSBsxkWiXynhV2q_qP9D4b4aiP-2PE4aPr0sTv22HTti_FLwpq0Xie046mxuIAoz3Hgdwv8AJHs8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5e07abed.mp4?token=R-LlpZCYI6yWsYXltbsIA7tV9rLy5gcGcxbek0AqxnOx6OxiuZbuC-_T7-H6ImkUNA8iIRv36BzWIUL_5ZqAYd5AmyJ6odjqzdkPmxjUigsMWyxTokilEkrCpJepEjE9FJB7RUPwQROPW4g75-_uByJ4PPvJgmDSluB2sbkNWNy_veuWwWju5xSDuowxvOenOrOS-RnhwAszcMzV1YMzxKN3Yh0PPY9uxogcoB_JjhfDrmYLGhg47Fjr05OFrDgrbz6EREwMjLngLSUQrt-WQ0MNKDlXJq5AgAAgAboG-dPHjRFAg2mHn4ScpBUrDo3we8NtyEoFjM0X7QHoGh7ZW72pD3DcPECjuTayFfd83Z_1jRDkIQUafst2f3Ho0hqRjetq5XomrL_NfGOYw6SPvkfjYl48cvIAwbxgLelmEifK4YvAANeNRpA5UW5eJsBKU8DCvFbKjmVih9Cs2lZgq6Sdf3Ju3uTZLP3sOqy0le1eXAphDWKIy3o9sL7-F6TWFjxv9AO4fUmlo3pvGscK8jlBIVVyfl-obkLGSV5Cezz1kF6_lSd4T6IlXA9GpyUsaSu3ra0T7MoJM6YadEPPUyLsEgqjl3ubSBsxkWiXynhV2q_qP9D4b4aiP-2PE4aPr0sTv22HTti_FLwpq0Xie046mxuIAoz3Hgdwv8AJHs8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🔴
#تقویم؛ 8 سال پیش در چنین روزی؛ شبی که پرسپولیس، الدحیل را در آزادی شکست داد. 26 شهریور 1397، پرسپولیس‌پس‌از باخت 1-0 در بازی رفت و شکست 1-0 در نیمه اول جدال برگشت، در نیمه دوم سه بار دروازه الدحیل را گشود. سرخ‌ها در مجموع 3-2 پیروزشدند و جشن‌صعود به نیمه‌نهایی…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29946" target="_blank">📅 16:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29945">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-asikxFu3OLWP3ldLc6eLheIKC9uSSQLO9k0CN-DGKfCD7FQopGLm0a68_T0lp-uGh3BP7D4zkSNOMArOnKgnIkp8O6_w_VcEyxStaL7-72Az8rUuKIr1qgaVib6YfTYWPQ2xqnAnghBQNHz9ip5o5-Jq-dIlMHwJrg7iMcUDRCuxsy-_d1XR4tpfVlRiEpexr0sdd5cf3ljsa8t4SEHS2OX6CSAGPsho0zu7XtpMEadncCdyxiDUyGGEg9bJanSbGaKnH9AA_P769iDhY9fNKcvUsbyNf-3KIJ8hdLH7qUnLZeYUDXUNNaOWzvcKmgwbKBBgmEBwEXhieVtnwSAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🔴
#تقویم
؛
8 سال پیش در چنین روزی؛
شبی که پرسپولیس، الدحیل را در آزادی شکست داد. 26 شهریور 1397، پرسپولیس‌پس‌از باخت 1-0 در بازی رفت و شکست 1-0 در نیمه اول جدال برگشت، در نیمه دوم سه بار دروازه الدحیل را گشود. سرخ‌ها در مجموع 3-2 پیروزشدند و جشن‌صعود به نیمه‌نهایی لیگ قهرمانان را در آزادی پر از تماشاگر برپا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29945" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29944">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27095c80f9.mp4?token=aQHIBAhNCXWLvL8WpxKD2Afx1npURI9IIdUweBVytm6FMgiod_vdT876przWaNnp-qTvoT1jtans-0L1X9fqnAqOueVW6RbNRwqP20VlfFKrPp9d2PRbE5Xsbcc3oV2nvql28UbKm5dop3d5Y3EwKFFdDqVFIfFnho-csTW7r52AbHgje4UPuo2OY0KIACJML9R0jYFUh6ZfyrxqFW82FuesQMkgFpZsrntBKcd-iZteLvzH1PeIme6nA6b3NSim79nu1OEBLnzIQzbnD7-NZUHr8grGQVDW93jWGV4lvDmJJHsW8cbXlpFcCszetkNrSypVP9W-w-8FU6sRvglc5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27095c80f9.mp4?token=aQHIBAhNCXWLvL8WpxKD2Afx1npURI9IIdUweBVytm6FMgiod_vdT876przWaNnp-qTvoT1jtans-0L1X9fqnAqOueVW6RbNRwqP20VlfFKrPp9d2PRbE5Xsbcc3oV2nvql28UbKm5dop3d5Y3EwKFFdDqVFIfFnho-csTW7r52AbHgje4UPuo2OY0KIACJML9R0jYFUh6ZfyrxqFW82FuesQMkgFpZsrntBKcd-iZteLvzH1PeIme6nA6b3NSim79nu1OEBLnzIQzbnD7-NZUHr8grGQVDW93jWGV4lvDmJJHsW8cbXlpFcCszetkNrSypVP9W-w-8FU6sRvglc5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ خاطره‌‌انگیز و نوستالژی از سوپرگل‌های تماشایی و برگ‌ریزون کریس رونالدو در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29944" target="_blank">📅 15:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29943">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnIrRU1CZ-xDOljLdifBK7SrXo2gP0cJ7jpRw_rt6NZ4T19qrmwOWfkwY3S7PA9fcJVtn61S2zZdjPe-rsnCGbljS206YhX8VBzS5yoj1zs3rkLv6SthuGOAnMcPKfMC3I6G28CSMmdngVQ4TKnpllKy-lNQa9wLyhvV9P4G7YlhhQZrIuw4NLLrQEUO3MBtXhnzvKMd8bJ9B7ypVoc_O0MgXCxIIe1USDzRCJg22I0rqIigcP4xyrdocxtz5AXZUtxUbAfEfyYAj4dbrYvuIRTOxo-o-IYr0mtkAjDDhLPr3iPdquttLiVuKZ4Al0ZSaLOHZxxwFKTCF4oP9fvatQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29943" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29942">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXNcL1K4s_NQDrhHG5DvpePYlAa55tva6XyXmrc1Lcbu0hTIpl83d-2zzEscf_rNX7b_BRXNCTzIbQGcxWxWGOfdb3MHqmGqrVBeXA29CUzkwgtCP1C_RcQm8rJMxmTQ3YqljB3ZrbRftuPNJcwzmvvaW-454UsMGNuOBOHQefg_JaVhMYoLWujWJ5cIsGpCMRSnrjwycqezL4s1yESleClRIFPSUkwuLvYVhScPrWkHCoNiiimIsTBRFzSCvW89e_A4me9wJ3Ry227rdNyCREQ2PEoqGm-zcYMrD3Xk_EPsJ577BWRoMSB2tBk3mDtmvWxdf4saei9VAXy3VNXgTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
از 368 بازیکنی که در یورو 2004 بازی کرده اند 367 نفر بازنشست‌شده‌اند و تنها بازیکنی که هنوز هم پرقدرت ادامه میدهد، کریستیانو رونالدو است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29942" target="_blank">📅 14:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29941">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VqdjhcXqEVmCtYt5HtHE1HNaWyZQppr9XJJw0_bNpOa16_gGMADqcCzBt-s1gQJjWFKKQvPkhscpZz_vsTu6kX9i_V7NYraQnCa-MViJp-N642CWhoOYqrIhrt5lw0-Lm4minqaV2jlQCnpMfUgnqBnPqQplIMPjE93EOA-qtEvhjdz3rKyhgh6wWxW0aBOf1MqFDQ9-xcFg4G0UkJImCZ4u9ItdmBF05c84DMb8yZxbkXhHOy-xxtiXqAAUUBdUUz7YuRrfsgGiJZbsrFHKOdbDeFyuKRIaCLCWB1CIlIpNOKfsQWKlNb4vM1q--8eHq-rJMLDY5JtjLxsYFaHy-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
باشگاه‌پرسپولیس‌بزودی هزینه حق دادرسی که حدود 150 هزار دلاره به CAS پرداخت میکنه و پرونده یاسر آسانی رو به دادگاه عالی ورزش میبره!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29941" target="_blank">📅 13:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29940">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GE8UG3dvsa_iAmjih7XSCrk5xKqeuvpPC-gq-e57DfpqIyBODv6nV0kreXsAsR4CpoefYewPRHkwg-YaYmwHsHh5KgHvb7IU6V1jlLASnXEyamLoo69OmrY4cXf3rCFgwo3n7_Z8P0UKckxMNAzG72Qq8UaosAwo9NHsOy3javQEdutPR4HokFzCAQwWywuWmN6c2AiG96StHh_w6QX3X_Uu59h3I67arwGFaGy_B5a-p5fGNp49PegLzOqr8c5ncMo6r_bgIxAvx-AGZ_KN-KYWnokMEhFMyTEQT2onO97LmXWistDNvj2hcXl1osbcmudxCBjtverw27kVz2l5TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29940" target="_blank">📅 13:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29939">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6X43YTVPrZEq0nEPVIa2eQ4miQNX9a7WBZWHE5g_UjA69ChRhFu8j8kxJIRO820uOrGseR7PvT-eFjqyV4JvJp2r3XAf5YFCG7tMVRB5gMS6Fqx8mTsambwFSMpHLo43FFp60EoxzH1OnEUPGPr5NjcOgQ9fLP1BDbuszN2tVxGTtMKumEFxjVharTz4byWGXPPkeBoAOaTc-uERNLHDNreJ496LDfyN2GJjgwvuSSd0ZnCY5WvSRLDyQ_fxYTiUj8RiEBQzZvK9L6KXUuhSp10Sp6-myk7dSyH_8ZbXZPZOP_kBtnHTaRN-zaqE2bCgMlfSCemjlC_qiwq9dCFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29939" target="_blank">📅 13:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29938">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnfM6QWFhNBuYfjs7vgDcG-T6vkFDSpXBwimk1A_HYmHbP78PuZ4zXNiQXF7Z648ssIGsV53iXYPmDue0ZOBcznwZDRJINGLGpeH2aCxFg6feimzrKFR-xh0SnogON05zTBWQfVWvcFj_4SHTv2qDHxog3Hpc7JIH2RBi7Th3xD8qJ7BAE_XC95p2JB9Os-NWJp-pHdm2smbvg8dm7rbNYsKAevioYuJhGUElr0ll4dYgDVMCDAlG0Zg0NjPhQAslEyHawAAIpGpivC4mbj4smlA5DKB6Ig0B19QZredcVSTGVm7t88lhiygInzvV9ZIeLwqWq7WAhU5LNruhqRCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29938" target="_blank">📅 13:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29937">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0A27EIjIc15jvLheHayojFJclC_0fBTA9Vb72rRdJHZchfNkeRalgG3ncnMRhare4GjDPjU-yOuMjzjJz2MADfjfnPj6rssv3_RGcPVGHbGJiv6nLujH6EiRc192yFBr26NCHJgPwF3RAzP96tARrErBKPGNk2XsbwwMHnItbVzd7cDyMIvzkc1b_t9lkjiMB7yuj7kKKQiM0Senrr4aHC8aJMbrdesTAWMofWW1PXQQLhalLRl3FB-6xx4_2VGxx2TjXeDZDRnlhMWiMJi7TfnU8Pq0Xje83uV3noYwlAXEOPiPtuOOFC8W9yqXIXZBMFbVUOq7UtXpDmKTGYTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29937" target="_blank">📅 12:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29936">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=YeaDYn_JZb6zUYvctFlZTpmt4RZosWR2CURzzoYsIWSHdaychG5fCeFdVaZUVqxUvlLjLnL8AJlwMP802m6dqqWDApT5udq7t90Mc9LT01JJ1HwTytg45faW9AbaZPEb4AoRFHC9CpVY-4RX56A7STvxj7D-VGwcnswJGpXhmJf4FwPd4a4Hq8CzjMM39Brv-eek-_XfEktEpwomYWnrfYhTk8U0frGtmsqCIPNVjriPw_CugpHejI08SA5Uc0cSU97t9zoxbP_-yKil_PHmBANS0yS57dZ0wRSM6VHKrTWQ_2Q21Iub7m88YXpjKIzzeNUfzrOcFILOJa3eN4Xcm4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=YeaDYn_JZb6zUYvctFlZTpmt4RZosWR2CURzzoYsIWSHdaychG5fCeFdVaZUVqxUvlLjLnL8AJlwMP802m6dqqWDApT5udq7t90Mc9LT01JJ1HwTytg45faW9AbaZPEb4AoRFHC9CpVY-4RX56A7STvxj7D-VGwcnswJGpXhmJf4FwPd4a4Hq8CzjMM39Brv-eek-_XfEktEpwomYWnrfYhTk8U0frGtmsqCIPNVjriPw_CugpHejI08SA5Uc0cSU97t9zoxbP_-yKil_PHmBANS0yS57dZ0wRSM6VHKrTWQ_2Q21Iub7m88YXpjKIzzeNUfzrOcFILOJa3eN4Xcm4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
صحبت‌های دیوید بکهام مالک باشگاه اینتر میامی درباره لیونل مسی بعد از قهرمانی دیشب: ما هنوز باورمون نمیشه که لیونل مسی رو داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29936" target="_blank">📅 12:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29935">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOYpTv15LB1Gmu3wPvAnceTapPq2ZRulAUzpTr-_63xx0z5Qp4-V4G4fbEt0YkMIdRNaeGA91RioRAtgv9jX9dEnI3H21lqOfAambA-yL0ZtwqX-rgnYZPF3b40rPa926xkMsdWPhY_kROUPuGAOHHebPVBCDhi1E8TaLHbbp5d0tSjFUhfwNg9tfOsYeLPdVriVA9logWEpuHjfsuziSCEXEAG3Lr7IgbklZJPu_94AzE_ncevT7Nnd3z1U1U-IeTqO44VUDfd7L3vkc_ZDpgGKF37Yms1nvUULIqXTFb6Jgad8XlFPX-3KHLPFuTEX9RHZwmrrDguZYBZ8A8i-yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روبن نوس ستاره‌تیم‌الهلال: کار زشته هواداران التعاون رو هرگزفراموش نمیکنم. اونا ادعای مسلمان بودن میکنند درحالیکه‌به‌کسی که دستش از این دنیا کوتاس رحم نکردند. توصیه‌ من به اونا اینه که دیگر نماز نخونند چون اصلا مورد قبول الله نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29935" target="_blank">📅 12:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29934">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKyomiDi6aTwWqoOCcsmcnaHFauBjmdVqFiVCnTm6UiiSLB_-4CSrcdfnp8VEvm6LhQTcAIrUbn1LS-Jf5r6fYKpY6-eLMCoPNnXISoWS7i4NlWnjl6dR4bAPufTvWpiELxTOLHwGkYHh5mUdAwf-wWO2FP4sTsN5HXGoIahMVMoTTUAwDzluGrPHHykwEvL5ruGyr_Y03XU2pOOnoNL4GXDvBa2_diOoAvt1q2pFQoP9GWQK-xCSu6rqdkjHsMhMljqldh21dy6h-nSaf0Tm9XoxIodz4ZO0xu5IdcwvIzTctYfU2S3XowpWUy9hzERSP-ak1phGNZ26c1BAWHbTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29934" target="_blank">📅 11:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29933">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nby_Vd3eGmYQWZ--qPsXhzuv-uzQqAGOHsKpIpD_qenJsFNO5bMKKyXj4mulcxx9r51lX_YYtArV7kHYeRKP-bPIezcDkax88bxqRjuwF1R6Xyvh43s2vyg6xOTbF5QKwPISzegmvJUBB3sygX9acl543r6S6-U3flvU2nEIZSg1leOmqKRnxRqbZqlnjSNgs94Y7Oi8tD9frF8irdtDbq6szrnPTdYILSfR2ggt75V0pKk55j8nVmjeBBZbGPEw8wCAluVddDxYrJzLzSt-7muDhisCjwiItYx5gR8vmdQLvEz_OO3V5zOTW8inWjqV1ai4ar2cJ8HQINEtFfXdtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29933" target="_blank">📅 11:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29932">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDj9ynDaF2uMwnGDyicGYrYwXFJCAMH5hG-SJYrI29mF2a-l6Hj3yd-gNoq-BlpsWkNGC33GmL-1MOk2z8wYLkI3MlGbFwzPGtSdRQwa4XxedhVXjvaU1DdiZTkc_-TJG6_FXi3ZiHuiECaiyFtfz8olaZSqLuoAwsSZ5i_7XtZ5wcXGhbz7yfO9u6o9bYlS0ebaXsHZ3hDSMiRRvnJrdVIGGVMkxEWpIMMAhVVdvKEHmvheH63_eJ19XQEJ902U3TbjrRLfcwwbmNZLfh0QJeinuWk6NF1kvgARCpPTOZYCH8A1Xx2dkqEh9fwB3EzEtej9fm4PlWAReR1iv_U8OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29932" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29931">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwE34VtVot7-59dN64wcQ6RabIXdaAaoUlj0mF9UKVCSktHZ77RKwUdMlziWH3XxSfZpKXCKvTJklzU-32oo0Xo6T9aXhsmPjzJv-l8jF4Htt__MUI4F1Th2eEZv0RC24wke_7iQQKD30IYnfaYum9h8HkUZ0GjPqduPUye3Xc1tyiwOxPKKjScsyNFLcG0Dfb9oL-oJIfX0ZduruyLDsGUOcA9VYrZuiJhqchelgK9Usg4sXi29Aprh7ptDAP8V0PdX4BTzecKtzZE-LeT6yQPnOBii-SbuvdRjXrNNwXhOatZ2f4COwv0pZMuhe12qUcVK2equWQ8NIqhegUrP0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جی جی گابریل پدیده 15 ساله منچستریونایتد که در دو راهی رئال مادرید و بارسا قرار گرفته تموم بازیکنان تیم‌رئال‌مادرید رو در اینستاگرام فالو کرد تا نشان بدهد علاقمند به پیوستن به باشگاه‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29931" target="_blank">📅 11:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29930">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyFpK-TCXnU7SdIKhICGEzVeCikCq1OKRd0Y7G9ojfpsC2HsUPyc07GdkTYqZnlmovZ_VVnkDzUW8Sqtmkt_X5xupI24M9-Wrj57OKokpXUrau3gwO1OzAvmIch1mJycUjB645FTp0NGMkwxp3zUa_baz2ySrni6wThIZ_GgEGlIluD2etY8FbaTo11aDRuTaDmpps6qUwizboIHCFP2GuvAt5U36XGm2vPYkIwi29lReco0VIzTZpGbP_imnz3S5-YN-VpqGFvgIO8O9qm13aZeqQdY03QTeZ9q3skSU2LtOytlBThpMgGeUG3ldESOo-14Uh8-aHmYtRROMM_iWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌لئومسی دربازی‌بامدادامروز اینترمیامی روی پاس گل دیدنی لوئیز سوارز؛ این 929 امین گل کل‌دوران‌حرفه‌‌ای لیونل مسی در مستطیل سبز بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29930" target="_blank">📅 10:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29929">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiKJmaULkOCvqgKyL7t-IJDy9EJcESJc0I4f7Zdw4cEgc_dOQgJqJ_ULMdkPHdiWKFYwKEwJhJ0y9OtVryplpf7YjU22SvJe_tuWKozmY04M_x5Ci2DqmrireFfKFGiD6VApotixciBaB4VjGvr13f_LpyasKqdpuEUuIlwmDQKze_FLd99RuuM0sqhVG5M6STLuESWgB2xUKeP4_HdqAZefDRZuJtYJKx--BcENFqRNsjOtPmy79_-x1imNt7V2lVCQZgQKZyI5QH-AsKwxUAPinrA1k00L76qNfx0laCPJwqSCLBUxM7zSpByR6ubkNB92nIn_r4eBfiEY-zLzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیونل مسی بامداد امروز 49 امین جام خود در کل دوران حرفه‌ایش رو با اینترمیامی بدست آورد. لحظه بالا بردن کاپ قهرمانی توسط لئو مسی همراه با آمار کلی او در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29929" target="_blank">📅 10:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29928">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92dd5a0020.mp4?token=RThIZnoh5fkOs8rlDZHk2Oy4zdxgbedeowOqvOSf74toACKX_Cy2kpv7OfZqMcaWVsdl9PqMGwcas2Gy9uj8NkTbnD26f8OIf3ZRon4T27ZXiOW7BAtp8kU2Q3ncCVt7x9OlhBKpCRoFjv9FRdeYWimCqHwMhlD_x3Q42W_OXNVlYotutR-S_5r8YMaC5gl7CibPwXFizAPteqSk9cyeQxRlDjduQLcOTilnqGoFyVslNv6r3kOtQvEqyTCXYOe7W0-BePmquz9gJXh1w9kNjUgk6RefLTDDzFAVmYwDwr4kLIRc8_Z0nZXJRXEJaDZkNqaDaanqpHs96uc0ug1kGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92dd5a0020.mp4?token=RThIZnoh5fkOs8rlDZHk2Oy4zdxgbedeowOqvOSf74toACKX_Cy2kpv7OfZqMcaWVsdl9PqMGwcas2Gy9uj8NkTbnD26f8OIf3ZRon4T27ZXiOW7BAtp8kU2Q3ncCVt7x9OlhBKpCRoFjv9FRdeYWimCqHwMhlD_x3Q42W_OXNVlYotutR-S_5r8YMaC5gl7CibPwXFizAPteqSk9cyeQxRlDjduQLcOTilnqGoFyVslNv6r3kOtQvEqyTCXYOe7W0-BePmquz9gJXh1w9kNjUgk6RefLTDDzFAVmYwDwr4kLIRc8_Z0nZXJRXEJaDZkNqaDaanqpHs96uc0ug1kGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇹🇷
کاشته‌دیدنی آردا گولر دربازی این هفته رئال مادرید و شباهت‌آن به‌سوپرگل‌اوزیل درفصل 2012
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29928" target="_blank">📅 10:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29925">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luIEfAFQhml8LEXA9i_rcDyN9IpZZKMlIQq32leeobOskd_L2WQTHt0xaAsC3GivjIkx2qYf3dsj8dpjfET5r2uqIdMKDCwSV1mmb7M5cP9l1kryIfgn4MAPxCfPgE9MQlhFF6jHaMTYgi-ZE-vO9i49VPo_3aug6p557T6lang6RzoKZLldpb-4WBLncVaoFlIdyp-UwwiwaVID5X5KkwyJSliQhJreuS3eUNDIeH8li8IlTNou93OXzEeU1wJR0-Gogo_s1PYiDloXgrIG0_WaO9jdkwHiZBp6V0IMhQVrw9lL5wrTVlA1Kx28I1VhLvgSsYXltCVI7EmMgCbqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d0f762e7.mp4?token=pIjPCikpR3XH96b266_cpiYN2V_2sUiBceQ4rH_zBEOudPVJyV3ye8YDruo97oW6kyjJZ9MOu4feQF042TF4wAS0puAns6jQpoNeOjj0UFIOgRKcThwG2MBQMqJDImTYfmDEpMrmv5Bzm1oSbcOC1P8qLIORDOxXZM6mLioY5H-Vm8X_1K8ikGWpVobkcFkx597X090i-F-OfNyq6RQhTCaQWr0Wf1nSjcTyMqvSRVgcPPdkWTTGm6JgLFsqZDEoWOXh1qzMv1oQJ5XhmXZmwpN8NLBr04NKMMDf6de6th1m9x-o5aWlAtuE1HrZHjJdOvN0SQGfehuBlWR2amQ7Zo0ql5j-PYEsDaYDpeHkMIRfeobeETojxRlSZmwhQ_W354eZ0hCnUd5T7K5akTmzgf3konsEJzKUSqS-VhFIAUrS7rJoIMTyhwCb2dDPZWHrMzs45gRhZEcM9AZbExkR9Z36BqFuliRkyhso54UdhQEDpA7qSu0E5OGHbZ0pqDiH103rBk6dArhSxACeCd09sTUNyzPHw46IdCdgl0YyeDaV5l4zBqQchPqeo0h0AvNBKdTe0FlQ5xbTSVOipp8Aujdn1vVSjPLzNoNh1meAYm2PRq5ioJBteKRpOubIPMdt67RfMlsT9Ugzws1W3_YzGwgLDaes_bSMV-yMN17YZ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d0f762e7.mp4?token=pIjPCikpR3XH96b266_cpiYN2V_2sUiBceQ4rH_zBEOudPVJyV3ye8YDruo97oW6kyjJZ9MOu4feQF042TF4wAS0puAns6jQpoNeOjj0UFIOgRKcThwG2MBQMqJDImTYfmDEpMrmv5Bzm1oSbcOC1P8qLIORDOxXZM6mLioY5H-Vm8X_1K8ikGWpVobkcFkx597X090i-F-OfNyq6RQhTCaQWr0Wf1nSjcTyMqvSRVgcPPdkWTTGm6JgLFsqZDEoWOXh1qzMv1oQJ5XhmXZmwpN8NLBr04NKMMDf6de6th1m9x-o5aWlAtuE1HrZHjJdOvN0SQGfehuBlWR2amQ7Zo0ql5j-PYEsDaYDpeHkMIRfeobeETojxRlSZmwhQ_W354eZ0hCnUd5T7K5akTmzgf3konsEJzKUSqS-VhFIAUrS7rJoIMTyhwCb2dDPZWHrMzs45gRhZEcM9AZbExkR9Z36BqFuliRkyhso54UdhQEDpA7qSu0E5OGHbZ0pqDiH103rBk6dArhSxACeCd09sTUNyzPHw46IdCdgl0YyeDaV5l4zBqQchPqeo0h0AvNBKdTe0FlQ5xbTSVOipp8Aujdn1vVSjPLzNoNh1meAYm2PRq5ioJBteKRpOubIPMdt67RfMlsT9Ugzws1W3_YzGwgLDaes_bSMV-yMN17YZ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌لئومسی دربازی‌بامدادامروز اینترمیامی روی پاس گل دیدنی لوئیز سوارز؛ این 929 امین گل کل‌دوران‌حرفه‌‌ای لیونل مسی در مستطیل سبز بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29925" target="_blank">📅 10:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29924">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkH1YHI-GGmXitAoYU257zMXCntQPabK0-OfdfSk8-WtJ8zxIDv2XJ28aIU-LjDPa6B87Wza4xKd_8vG23__VnqqoLQraHNr99lZ0uMxXmiwfGjEhRxBwWK99Kn7zZEjXe7XVTIsLuRUFW5vkohj4mqMzE7Cv8dMIMPCJokcVpx20_BvIeG7L5Sf40oJyH84cV0IGR4YoWaW6-3rchms10m6ylTGsk3o56PyIp3vGPfJaCjCYfFIg8q5VCCjmJUVvGM0qMbU_Bt1OARvKV3MfJZbye5dU4HFdevyNztm69rQJ_Dq_WmlVqpt-BjjWe6knLVUmTUw948h0LKhngnfug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یک‌ایرانی‌مالک‌چلسی‌شد
؛ بااعلام‌باشگاه چلسی، شرکت‌های‌گروه سرمایه‌گذاری Clearlake Capital رسما 87درصدسهام چلسی‌راخریداری‌کردند و به‌این ترتیب بهداد اقبالی تاجر ایرانی مرد اول چلسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29924" target="_blank">📅 09:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29922">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29922" target="_blank">📅 09:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29921">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">‼️
کریم آدیمی ستاره‌جوان بارسا دیروز سومین گل خود را برای آبی‌اناری‌ها به ثمر رساند او در این شش مسابقه‌برای بارسا 3 گل و یک‌پاس‌گل به ثبت رسانده حالا پارتنر آدیمی با یه کامنت به یان دیومانده خرید 140 میلیون یورویی رئال که این فصل اکثرا نیمکت نشین بوده تیکه‌انداخته.…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29921" target="_blank">📅 09:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29920">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/29920" target="_blank">📅 01:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29918">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E352hvH8NaSzItJlSHB7GHHfrNC1rW8GooKBzwF8mFUEBf7KrZqrh--OXn36GQMbzXKe5Fvopv2nofoUFiaqVndAJ5kfJ67hoButgrJcZ6CgHhgghayIHLvE2blSVYhzjndgLz8RVkoa01dkjQfvo9pNMbr1qrWzKyVyHyR8SfySsx2w2ibm8e5ILowQX9XmIieIyA9fRFUvJMPazV3UkCaG5kvI9mOAm6ogAIq7NQLiwMlsWqdrcdnqMWWIyVAsH3WCEihgsDfelWSbAyUFfHWl7HDAGmzRraCT7LQUB6lgdeT4i16W-UMSVH4dr32MHyc0Yrwdps_oArPRxHBcHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز
؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/29918" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29917">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1ZpzXFzzjOfpz0ehJMKo5DVcVlcAGmnG2sDAuu4UkygRy70wmWoBHa-XDxEcfLx51HhCWzdr5d5KKzCFjNXZsTDiNLwefjavktv2uJl4NkNOZTfaEUJ-jnlNSgQDZsQ2ffso1va4XsXoxpvWfbYAw5R3SzkcXD9wmO63VBcWerrU7S5ALsyfgu3azcKkHx9yZpRzzH6uc8B7Bn4SHLcqMOts3-BSTRrlUmWQblGPMtFuuB55IA5EFA_rjyFOsV8iLiVmVkVIB7dNzx2rebPJkpybsQe3s2U0WsuBkOZcX7zqSr-9QWbgHkvxSeizP0GYh1din-_W-zO25mFyMyHqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازکامبک‌برایتون برابر یاران کریک تا برد هفت‌گله بارسایی‌ها و تثبیت صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29917" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29915">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUi7-4dqCEV3N0U-V5QiF6S2zSUkl-ITecFUOzl-F2sgBSiEJ_lRyoOJ9yLbQ88hu7WomqZpqO_j2vbrgh1SBxMGQ5BrJ72Ry5l_cY3hPgWFBRxG89TxR-TftXYYU1NVpucMjzlJV2pMGb03xwzFPPAJsWvO4JWFGxcyZBM-HjPKRP4vhWQCojw0cWeMfwJldh-3QclVSdOs-tBuuLWsRshQP0yJFQVf2LlhpyHHvh_M-34opN-y4X4MGv2-tTTdeL5yJ9BzGZ6FKypJhO7LQbvL3lJ0wiupnIz-Z1xTWxW_LZCktZo9-pYg7tMJHp0vfqaiy-Ijq5WHyCW9rdAM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NlNmZSpkUrsNSQ7GGgf0PM-gQZYBguQvpyqpi7qsxUilKkEn2tOpNs6_t03-rTaB3QHULXpw7ZcJU2WldBB6bj0ExGbdcImmnb2VdokFpYqZdOI6nTcRRWdnyZG8Rm_xhRkJctzDzXnrOmFolSaX2_429SQEfJydAzMA_h9d6AzM4eTZjDxvjX9b4A239M5CR23oEzUvNbZYb9aZpyxg8j2R_6zKhM6axSLTH8c09sidhs3peP9u1TYREN0GWPZtO6yBqhqMYclJW2nnySvXR2_IMKs9INRHKA3-l6wdm4FBWIbf41BtAlUJ-7lXuioCfEZbyJpOViBfMvklF9TFQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29915" target="_blank">📅 01:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29914">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2MjtZUJ2Rsn1zccSnr97A0687tSqrFGbuKBKEIRFsM98jFpd_A1KKX43bwPG2YMmBhLxMe8YHCo7IfNhLIC_PB7CrHQDqWiWdPUm0V7VgknS7IyzsSmex8UdN1ylbHuSoB3fqYIgfRdYm2kRz0wPgvHKsfNixsZ6pmVWokOzIGqZPeUWAU87GNq3t2RYAYxuEZCffmOG6no5avDnSX64zQuBrAR2VdrhcXfTBfXHIxSkyRcB_xPfPeo4XmHWpbCyqakfgFRsdYJFKGATnSEZMc3ZYYb_MhHGCWnbjxV-zzAWBqey6RaDVOcpZ4kdVcGanXsIycCRZMUQFvrjno4qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/29914" target="_blank">📅 01:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29913">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGVL89sqztztx-WPweFYX6rXY4BaVlIlsxnYwhZkELKU3ReSs7nTTyGq6wAfVBhOkOnbkYEPE_DwbR6AjnMkDsLQbK9KTpqxsRLg4ifL4eR6GzoPwpLzHTYCWTQ1hisr4RmGA4NzvFcXIh7e6gi1qIrvhLo5x9_ygdFKE34rpm3IKGmNLpSy8rFXq-yJWvjewAF4ckZERL2jeMedqsP4Pix9E6_MG8rcVldSYCZBmq7_q_99xJaaBl9BsYh0eyXuduYq0Ym7pATCSi2CnMijVypEziNryfbu1juk_ZNXQumSSm7lcDKTDFE6h9hsBUe2u9bQEZcUIwikkYlijcSXcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/29913" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29912">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrGWNd3_4fYRXn75vKmMhy9JNXETYl_UrOnxXSHlQMJOV66E33yokwpe1Bld7RosvtlSObQ5rbi0EoTc2j42-eFQYCzhqbL82S_YIRYhFSGu_7vA7_v1MDZw-ktNRrKYl8FFVvzrDvWxss85s84d2KeYEcUGukh3JnBhDXwT9MUTnsCCCHQk45nhwuQPeAC-5gDUCN1KOS6McOCe6zhqZRpQmtfxpSB8P9BwdDBhc6edtgCPCpHv33-Yq94nOCdzWZROKaq4b3Rb7fCz-H2TZow7khoYojFqIH44Kr5jixF9oXPirf13Ne5K90clvPXmbmwxdV0euYVQjZ5eD1UbPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29912" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29909">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCj92F4W9Pstx9pdnDPjMPzAqQpXVt-hDX3vYbULrNmQyHIyeTKRYwM2izGkLpjmhcj-MYfxoqU6Y_lf8WOAaU_KBOVSm1CopNR_os6l9vTV8UMsX2WSNILZrr7qzmBR0_JDX9W7Kzi6psmd_W2CMQZV4dE_vpz0Xi7M7Te310TFnvI5D4zrmN7v2l-gwYUjmcJuZ1sYekay4XErklOcVmU0vabm7tCAX5GqRAkWlbBnwMnHx0VbyZiINHUBCogVyr5SH5buouNrOjz1ZveK_GzDrdr5J7p1t0hLPSdQOCP-7G0Gt04fM2r1nL20IJ0gAFKihVMgVPkhrjXvNy-nIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZbw_NL4pJghNqOeKBSA37XxF8zUoBCgfOKCxIieNXWLSn3UpWYAwaOwFanYC3c3x5FBXsrhCyh9lWKKWn59BfuFVpznfbKXtgnPd1ugTROmhc3oRRNkfD4D2j6zxjffHR0Sz1It5XjqNZrS5f62WjwFtIh2wELmNi1wjhtSlefeeJR4KY6rYAO3bZrVePd9Gfl4FpFpeyZjMo9ebAsMHRkz6LPmMyr48746-aKSIAAGfsItCd_3Qbi-VXZLUhjOSjs0c8hZngEjr-0oxg_TxGe1B1GXiepk-miKwCX378UHtDrVyKBux20Y-FZT3ZXKG3EywWYc_IrJCV39nBf7tQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دو دیدارمهم‌امشب؛
حذف عجیب و دور از انتظار شیاطین سرخ از جام اتحادیه با طعم کامبک خوردن و شکست میلانِ روبن اموریم‌مقابل‌بنفیکا درفصل‌جدید لیگ اروپا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/29909" target="_blank">📅 00:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29908">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dugXVmeOwDB_oMcpYFWZkNyayjc_b0Ib8SVGdzuMnNZM51pHt9GUn2Co8NzBRgpqlZEfttO3THzRsHISRflWJIr1T6rNPJYW2Wwd1QJvophIipy5JIbTmydhrxV3P6dI7E8n6eBWcVK50kNpG6OgHVaR0v8xOSj7GIljAdf1m3IuN6i5ZkhPrTlDCdVOnu4qGGcb9iyBtpVGELk-ubmScOltpSj1dT-52oCMIzYF3jdlCCRv2xnzCHeYLVWvNX_J-b5LXiY-YAz4PYcSBxj_8eBfZeC0BYbc8-AZ8AXYlD1EfEEa_2B8XeShcPP3IJ16HOOg3NhjrWm1l7e6NvGmVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/29908" target="_blank">📅 00:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29907">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZCas6nVc9vaNNSmrY48nY-2YdbJT7ero9oL1KLzXTEVvesu1LL1i6zY2OcXp3up72BdmdCb08CK8bnemEJiKIRPa5w8KkMQp6ajbOGBzsNugseUICXZXqILakX-Vd4mwZqAlAxm1KQwikFyTrFxr-mOXM8wDTg8MNhaHZKUGwA_mScmPedAknjPA86tAowUEknOj3rchQHB6Dok2DpK3Mintf3nH7O6d6cCMxDEKN_TMfYI805kIIhOPphCKgXDfYtCvGrAGO2I4TaR5BFXweNMsKq3SGWGOhhk5dDu7egesaYXRemNY6K0iCwmJH95cSLao27PVJWVEq7IjQlH1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/29907" target="_blank">📅 00:10 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
