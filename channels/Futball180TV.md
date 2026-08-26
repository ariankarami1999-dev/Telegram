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
<img src="https://cdn5.telesco.pe/file/tDWV2_ApRonjYs_Tms2fFOjKcfHNNtM9nCLnyxqerfLyxSXxrnoKIYbL7HzV2qGKdijxm32HUFbtSLH4pkbwXrp9XQb0WKLq4PdUpKOg8oI1WgW8eeS-rpA0BHsPRSqdW5uHvF3WeLPmUMgyXJUqXlnSAOwcnzA9piwYsOXfllKTjlYi0Mi2OZSP93TdlEfIjGS39JncT5J4dczSA8dAB3kVxwAcdNMo2SyIgZJ-iQmAM-A8BoiP7Ua1aNmDXczcJqlbuiP8tLg0zkYievyNXvDcPD5QdafIGmR4cxbF47tDpJ2OurakDf_n6Nx6xVMz4ep5InfdtauFoOTgvAhkYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 442K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 23:53:56</div>
<hr>

<div class="tg-post" id="msg-104742">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/592c7db362.mp4?token=XVo5xr1euY2eaqe1dzU0shFzFdng-iQeFAlAHNI13yMnzrcqwIKSSp6wOix0aKwLUmZv7_f_q74M5xU-smAxlyxoWZT_unp3U5HATVICLJ9K0BhV0TXIHRQx_iFxNMFxf2v80y4NrEmy54X8K5oWPvQ2FmXy73EFUdJwY4ghYX8bjGan76MxK-BC7nHNdNN52yzOtXqPQqy6DrsM6bJIKrtHf8P6YQOuDwDo8hsKjaDYyKJFYahuoIJtfb1_4-4plsXl_8uFWstEVjSMr9Hj_8g19ICG7RDr65TUvFLnOM5DKY36dqmVaxo5rJHh1c8GPRu0j4iN7G4dh6oYg6OPoKwbb4ol_UOeBdqE4KMt6fzHx-3zOwCXwZs3QnV3nZgfnFFI6u22N7UTdB2ZHfJZqfV-aLabHtzRd2xb0enjy4kuOfUmuCcVXn76_ycbOSsihmW8Op0ff8t6PCanzcoK20PKwYPtC1lfZ-jjhKdrmr3e7yQOq6DXlPs_jSzI1Ba0cFYPiEvuTqsegRYt-f2cjTgISekPqEppkBmWf5fLQj4JTedB3_XyhMPyQeEYdJKVRLEemXgIvk2q-EbNd9yUv_mYvEl42JJqE0dceVKdhoP5ZqP_nY6BlSnyRe84KCEjTD5wcxRs_U35P07mW7_2eGzp6B1Y7z-gCHpa8S7VgiA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/592c7db362.mp4?token=XVo5xr1euY2eaqe1dzU0shFzFdng-iQeFAlAHNI13yMnzrcqwIKSSp6wOix0aKwLUmZv7_f_q74M5xU-smAxlyxoWZT_unp3U5HATVICLJ9K0BhV0TXIHRQx_iFxNMFxf2v80y4NrEmy54X8K5oWPvQ2FmXy73EFUdJwY4ghYX8bjGan76MxK-BC7nHNdNN52yzOtXqPQqy6DrsM6bJIKrtHf8P6YQOuDwDo8hsKjaDYyKJFYahuoIJtfb1_4-4plsXl_8uFWstEVjSMr9Hj_8g19ICG7RDr65TUvFLnOM5DKY36dqmVaxo5rJHh1c8GPRu0j4iN7G4dh6oYg6OPoKwbb4ol_UOeBdqE4KMt6fzHx-3zOwCXwZs3QnV3nZgfnFFI6u22N7UTdB2ZHfJZqfV-aLabHtzRd2xb0enjy4kuOfUmuCcVXn76_ycbOSsihmW8Op0ff8t6PCanzcoK20PKwYPtC1lfZ-jjhKdrmr3e7yQOq6DXlPs_jSzI1Ba0cFYPiEvuTqsegRYt-f2cjTgISekPqEppkBmWf5fLQj4JTedB3_XyhMPyQeEYdJKVRLEemXgIvk2q-EbNd9yUv_mYvEl42JJqE0dceVKdhoP5ZqP_nY6BlSnyRe84KCEjTD5wcxRs_U35P07mW7_2eGzp6B1Y7z-gCHpa8S7VgiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌تساوی سوسیه‌داد به رئال‌مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/104742" target="_blank">📅 23:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104741">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گلگلگل تساوی سوسیه‌داد!!!</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/Futball180TV/104741" target="_blank">📅 23:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104740">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf83d89368.mp4?token=uUq3AzPo9lcfVWRplCwg1sC1IQfaO9Beh65f-0w6OPv7eL1UZLrLeY09fyAhm6N9GB_IfN6vObbXOpVMOGLaUsKU0E3qVWDzAAbHyOrgFTVK1oIlWIRDyfsQUWf7EKwmj8xPhYvGJolHP-h67biE45FjQax_hDNVXMeggUgoXunHNNOlai23Dq05d1T3HC27fhJ2Z_PSuxUZ2hiu36r2I04VZHWAq29SiaDB28E1tXI7VLr5REvwnz6uobUEeGjz8sYwXwRVi1Fu_9eY9rlu0LEUhtvVe0SS7WtHh50bE5ZZhWsufhjpZ2YLsX6BjvEVtpvsewrbwgRULbt58KL5pw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf83d89368.mp4?token=uUq3AzPo9lcfVWRplCwg1sC1IQfaO9Beh65f-0w6OPv7eL1UZLrLeY09fyAhm6N9GB_IfN6vObbXOpVMOGLaUsKU0E3qVWDzAAbHyOrgFTVK1oIlWIRDyfsQUWf7EKwmj8xPhYvGJolHP-h67biE45FjQax_hDNVXMeggUgoXunHNNOlai23Dq05d1T3HC27fhJ2Z_PSuxUZ2hiu36r2I04VZHWAq29SiaDB28E1tXI7VLr5REvwnz6uobUEeGjz8sYwXwRVi1Fu_9eY9rlu0LEUhtvVe0SS7WtHh50bE5ZZhWsufhjpZ2YLsX6BjvEVtpvsewrbwgRULbt58KL5pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول رئال‌مادرید توسط کیلیان امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/104740" target="_blank">📅 23:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104739">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">امباپه یکی برای رئال زد</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/104739" target="_blank">📅 23:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104738">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rq11yY_FRlZ_XPclXayNYbATL_oUXkRU2yIXvKrIUUZlN5ArMgGmsuIDm2neVI39tlPeVb83qQn1cNSkrQzvk8QKaCl8zIpVo1hfzWSnwNOUFpT2dDniAzUzQMWu0trUh-z7OhGvaDO2d0ZaftLKlBhJYqTGImMKLUqadPhk6xNkr44adifn9C4ZHeyFtsVphKrC0CCzvxB6-5glNs8168gtoOuD8K3SpmKW1ARjdyjS3kC-fhho5EE8O7un-MKaMei4c7U41LIXO9DPWHPmcojI8SiuvFPFbe0GzES7caQbGnnaLSbZAalyr6hf7P0BpbkQcRfoeZnFvQjMqadicA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جرارد رومرو: هیچ توافقی میان آرسنال و اتلتیکومادرید بر سر خولیان آلوارز وجود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/Futball180TV/104738" target="_blank">📅 22:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104737">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvOW_VHRQ7vlM8xCUsQBh87APjWq0nM_lDjMGBdMsHZWA-659A-d0bBSG5BTS2b8Az_LBxCIia8ij24bBv6VtDeg_IjCaO1T0gIJiWG9GUKtOFzeimXPLbCPgsf0OfosK8uu5vfFv9WXyluhTjX1J-AwzeBYBtzIxQzxkEAE0e3MSuxy3MM-U1wF0TxSnsyhx5o9N9hk-ParGdzM6IMxOa5-dVsoOKLvjDIXnjKEaF0CuZ0veb8EdE-jjY3IhhPVatfpKZIWZdo1EM_Fci4tol2WZaIC9AnkSN1Wnng6IZUvncSdRb6zkym1Nyv6PLc-aMEkJDa_gaBxffHrfG4PiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🔵
🗞
#فوووووری
از رومانو؛ اولی واتکینز از استون‌ویلا به الهلال عربستان
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/104737" target="_blank">📅 22:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104736">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a7a829591.mp4?token=ptrb1kxNuMqei6d73ydRUfCvIl3v-vmScyhA5OgAbu0SD2RoTd0kAE80mDuSsV7fhi8iK7OUm1kOaGWKXaTn-QiXl1TMyOpMFtjzgEMGB9Tl9lLN4T3a43VWxPsb2xSRG9YYUBzZPiiDys2xzNDKHN8u20Al5Dwve7cTfbpve_im_1g1i5_G_CrnQKabMNq9XmZK3gAWkE-l-wBfmy8J1jvrN2wJ8PVo0j642evueNFVsLT5QUzBoEM761rt8RiUYNrdx94j_Lm8IFPNYmVwAIA_UQhcjcafl6601KDgZquaNold1y6u2xZtBwskODfgDjOTsnKAeQWbh5yfvtLWqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a7a829591.mp4?token=ptrb1kxNuMqei6d73ydRUfCvIl3v-vmScyhA5OgAbu0SD2RoTd0kAE80mDuSsV7fhi8iK7OUm1kOaGWKXaTn-QiXl1TMyOpMFtjzgEMGB9Tl9lLN4T3a43VWxPsb2xSRG9YYUBzZPiiDys2xzNDKHN8u20Al5Dwve7cTfbpve_im_1g1i5_G_CrnQKabMNq9XmZK3gAWkE-l-wBfmy8J1jvrN2wJ8PVo0j642evueNFVsLT5QUzBoEM761rt8RiUYNrdx94j_Lm8IFPNYmVwAIA_UQhcjcafl6601KDgZquaNold1y6u2xZtBwskODfgDjOTsnKAeQWbh5yfvtLWqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رونمایی نیوکاسل از نیکو گونزالس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/104736" target="_blank">📅 22:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104735">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKlc2asHwqlHZhz3jAa2B2djKkCQHJH7V7jtQkplFWCYv6x-gOdRxpESO1veqI2RfVzZhhbMGUhpvQdaDmsDAHasJ-Vnh0vTwG97VFZUNf6Fj7SzTkvM0GQmomW2I-wqeA-IWsWAoGL-sNeEyLslKiAf7Ire7f90HShKXeCL9hHwx2cJfqxcscLHif30jnxR3lCzvYSZHo8zldYqIoye85QyvNWm1R3Or4de9sEHatPUmeJu2xl1j5WSCBW4aSiIvfl2iCLZjdEZ_3Ac5iLi6p34nV3AVaBvPPyMxC2rO_fUW00JjSgLK9xiB9mh3vPbuV43qkT6tsiJGNI0SY3gDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اتلتیکومادرید و استون‌ویلا با نیکولاس جکسون به توافق شخصی رسیدن و مذاکرات با چلسی برای توافق نهایی ادامه داره و بزودی جکسون راهی یکی از این دو تیم میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/104735" target="_blank">📅 21:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104734">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c61000564.mp4?token=TYSeolXhud0-Aq7XvtzJ_K5aTTmPo0uZfN4WE6t9Mne4U-m1PRgdm1jD-h3p8POtXRvL7vcqOXAKqQwg5JEk3tuRtWmt4KYtuR8lyAHxaSTldvHsSxfgrBW_92ucZE9xKq-9SD21-y3MjThtNRnP1crbkB9xmrr2T_7DGEvrlO89tYaU_XdnItRlBWX-JCoAPwzgBHsC4OQYwcY2ybdVZC8OT53Z4Yv6hBtX0LTaQXFYT43FuP176xlJkA1p35LbP1Z6me9EuNKBYzAE9zr4uldkb4V9aLYyS9oU0BAzLHFLvHAcHBEu2gSSP-jLLJzIt_I7CpIbadRekGGnEl9Mlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c61000564.mp4?token=TYSeolXhud0-Aq7XvtzJ_K5aTTmPo0uZfN4WE6t9Mne4U-m1PRgdm1jD-h3p8POtXRvL7vcqOXAKqQwg5JEk3tuRtWmt4KYtuR8lyAHxaSTldvHsSxfgrBW_92ucZE9xKq-9SD21-y3MjThtNRnP1crbkB9xmrr2T_7DGEvrlO89tYaU_XdnItRlBWX-JCoAPwzgBHsC4OQYwcY2ybdVZC8OT53Z4Yv6hBtX0LTaQXFYT43FuP176xlJkA1p35LbP1Z6me9EuNKBYzAE9zr4uldkb4V9aLYyS9oU0BAzLHFLvHAcHBEu2gSSP-jLLJzIt_I7CpIbadRekGGnEl9Mlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
جوری که رونالدو به گلر کسخل النصر دیشب داشت گلری کردن رو یاد میداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/104734" target="_blank">📅 21:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104733">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QwVYdGLRqnFIVbHe-N_67ipuJ4iphjnV9COLAxD9Ml_M_TgZCds4GAYKICgsiohIoXQISoB2f75n6tJX8aU2am4YllxCS5LzjozKRC8FGyeO3Pvx4TOc97jFwD3K_izIE9wEyv8UbTaWxcIJmR3fgpqoVsoEzpYnPYJjcs2sXMLmg9-UmMh_fNEtEeX27U8aLBsr6-9ml6RxbIhUAt0oTACbOrZ3dViG6MlE23WLKtJYYKTObOdc8LFHvuxar3toDdW-dlqgCjWXcACPaICPqu4GrcB2zNlIyJYkqduEMDkLyXjTQ2CB1fyN3UFjfQSEp3jmp5BVWaEzi-qPwmyhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
ترکیب رئال‌مادرید مقابل رئال سوسیه‌داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/104733" target="_blank">📅 21:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104732">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/576668f60b.mp4?token=nI8K1VUEgp5n1QPMG2_Jl76k5XjSGOlveo7ye4VfeYJUI-asAsyCFeIN41wjFLYRy93342vStEyTSSY9ia_LicJgmGWxvnCCsukIBVS1fo7I39Tv8uwr3RZiXFS0i5OsxMdDQqoAoPAGvWpkWf5bxsDQqXqh9emFxEd5c01Iko0D6Ar9HC5NyiZr2Xi8Ffia8-xuLgzPoowWy3FngLEM9887aqxaAXxsXSEd33aPkKk1qOFQ7j7UyCTxJnG1r3vb8-fe_YMD1yQtXjQMAhUY3a3V6e6yV5WSF_0gLBSDIEj9JPJ6qvq-4dpSLFmBHlTOWkKZV8YY72xVSj__scO-Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/576668f60b.mp4?token=nI8K1VUEgp5n1QPMG2_Jl76k5XjSGOlveo7ye4VfeYJUI-asAsyCFeIN41wjFLYRy93342vStEyTSSY9ia_LicJgmGWxvnCCsukIBVS1fo7I39Tv8uwr3RZiXFS0i5OsxMdDQqoAoPAGvWpkWf5bxsDQqXqh9emFxEd5c01Iko0D6Ar9HC5NyiZr2Xi8Ffia8-xuLgzPoowWy3FngLEM9887aqxaAXxsXSEd33aPkKk1qOFQ7j7UyCTxJnG1r3vb8-fe_YMD1yQtXjQMAhUY3a3V6e6yV5WSF_0gLBSDIEj9JPJ6qvq-4dpSLFmBHlTOWkKZV8YY72xVSj__scO-Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و ژابی آلونسو که دوباره خوشحاله ...
🥲
👏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/104732" target="_blank">📅 20:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104731">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpOiTsJV2aU7ltjslw2do1HqOpfpBJRc0Me-S7E-KXoAXifCISzS7Amxcu5Fu5_yujeeN5ORwMtmkCaZBkGq7Hx7Qa8Vp-rKN6slsUtNZlePHq7JBWv7D9vPa_BNo1in18feUhzCcZdBuBzKOWolUQwC0rCCwlyUZ6af2f_iFtH9DcsK58lIyT65qn_kh3oa_nl_TvlCOXenK3si6KD5KUe6VcF3bGFctn-5IjYos7JEAQFSjkqeba75WNWClDgaGbrpFkSsFPY_xYq9HRtTj-t4_52hE8ylTOahJrl2Rg32Pb6Ym80hZb8AeCHVSWtC2WTXv2BJghDfQPbrlygT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
هفته اول لالیگا اسپانیا
🇪🇸
رئال مادرید
🆚
رئال سوسیداد
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/104731" target="_blank">📅 20:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104730">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
🇮🇷
عصبانیت و فریادهای محمد نوری سرمربی صنعت‌ نفت بعد شکست عجیب جلو فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/104730" target="_blank">📅 20:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104729">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6p3RhIYBUyclJsaRjoOKoO_GbhWJngCC38Hp_Or8VP-N43QHtqzEraN3nXgRJc3yMVzOqXU9nMAadEf9sFGMss40PeFTpJfE5z_VW7C1mOR8MEotrKORb8K8TTJ4955dIzaLdfkBlV-kb1W9s9LiLX7rN343635178CrUAt0RqOZNMHPlOKmbWNfep7EitsrDLXPhG3qNa1MCdWdvMUiL57NTLL18-cgsFsWjfzUg__IkO6WaxeGBuIdTITZ42ZTWs3XbOH_dZZ1c4Ygu2Cp610KXfg8BG99p8BDnuTCVGxcMUbErLMvfjaYbtA2dg9Nv2LPQv8Z7mPeC6LpjIURA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یک حساب کاربری که فقط اخبار مربوط به باشگاه اتلتیکو مادرید را منتشر می‌کند، گاهی اوقات منابع آن قابل اعتماد هستند:  جولیان به احتمال زیاد به آرسنال خواهد پیوست و به پیشنهاد این تیم موافقت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104729" target="_blank">📅 20:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104728">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQ4i0ywfGwZ0F3mfj1ECbMPxPz5Nwl8ltDdgljmCx9a3VzHlHdiNpERD954tcSKE9whW7Vsy257niqNy4maDOBjKJ8slM_bZPB6g566JtklFGPsBQO_IBUdk1pGXwcMOHcrgUsNmRgLGW_ImlhhPDMydgYPUnDdANpPTW48YO-0Cao6R1lf_J1i9aYwyKvVEwqWgOg4v20IzjxcCM3sYtgEeJGpotoGHx_LWA9P32KcyQpwa-TUXignxhsTeegujWpOqiidjJtz2To9u0cYSDttSakMWdwIII-iqAtOu7Jpp-UgKwTyItMdnO4FaaE1pFq_ldhf8Kft6bIECVH6U-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اتلتیکومادرید و استون‌ویلا با نیکولاس جکسون به توافق شخصی رسیدن و مذاکرات با چلسی برای توافق نهایی ادامه داره و بزودی جکسون راهی یکی از این دو تیم میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/104728" target="_blank">📅 20:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104727">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e019b361.mp4?token=Mxj4rBy1dzYo04oBf4I4t0qbijlBYkVxYqgb94abxgZ5U1GMB0PC9BI-h3ipZNgo8rfx52uXVRSR1p2Il2CaFjoteB4q2LtCNvPafKFVF6xK1we0VWJ5-1UfLojGwyIwQmVgGQ_ruefWGP0RP5FOxog1R_OUFtZA9lOG99VTptNSXuCq9WW8v4DYciv_xWflPn3AoZ9MvMWtH0pEa5qFEKnGRVnLwv-hRBiCQOFKKPKtMnSwNrQwFWjV_cJlC9OUFGWBBFBW2FQ6xhfFlTcQZ7mTwJL-5l67wIIGLpbddurHeKCGZeqEG5m7qBUf4Kf2OEzO5zPI7czy46pXF2pd9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e019b361.mp4?token=Mxj4rBy1dzYo04oBf4I4t0qbijlBYkVxYqgb94abxgZ5U1GMB0PC9BI-h3ipZNgo8rfx52uXVRSR1p2Il2CaFjoteB4q2LtCNvPafKFVF6xK1we0VWJ5-1UfLojGwyIwQmVgGQ_ruefWGP0RP5FOxog1R_OUFtZA9lOG99VTptNSXuCq9WW8v4DYciv_xWflPn3AoZ9MvMWtH0pEa5qFEKnGRVnLwv-hRBiCQOFKKPKtMnSwNrQwFWjV_cJlC9OUFGWBBFBW2FQ6xhfFlTcQZ7mTwJL-5l67wIIGLpbddurHeKCGZeqEG5m7qBUf4Kf2OEzO5zPI7czy46pXF2pd9jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فاطمه خلیلی بازیکن تیم‌ملی والیبال ایران که به زبان انگلیسی به طور کامل مسلط نیست، دیشب خودشو در گفتگو با یه خبرنگار به چالش کشید که مورد تحسین رسانه‌ها پوشش‌دهنده مسابقات قرار گرفت. ببینید صحبت‌هاشو جالبه
😁
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/104727" target="_blank">📅 19:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104726">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaevHRynWQIVGjU5XNCvPUbASOOVp-jC-7ETJ1b4sg3h1k8gESmbnTy8xBzZeh9jmWO4NsG5qPi3IAB3qJyCzG6BJcZXRVBKg8Pu-l-UmfAFDYRYPYjXS87qTe_nC9rpvUGbV3S-tXZcAeazFsTD2iTqFHWafLqSek-yPPb1D8j_y0nYQBpCcZ5S-FkD6iicGoIXe2x8J5mjVc4IMtYTQn5gLv8kzY48nt9SE8crGpzKzupLhO4kD6Rm3xH3Er18cZlvSvgdYKeNMvBEYKx6vB2LZ3mExEzsjRerI5_N0wSgq9EkDVjtaaNYhoFK947WMO13DWItf-TZ56VCZQ2gKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
یک حساب کاربری که فقط اخبار مربوط به باشگاه اتلتیکو مادرید را منتشر می‌کند، گاهی اوقات منابع آن قابل اعتماد هستند:
جولیان به احتمال زیاد به آرسنال خواهد پیوست و به پیشنهاد این تیم موافقت خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104726" target="_blank">📅 19:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104725">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64ba0d1ad8.mp4?token=PtTsaDwtfabG_Cy-GS5w-YEW4xqDPP463IaN7UG2Lm2U9wEDduMJjy3_6GiiW2Sn6qjgVLOYuCZWXgSipG2TSGz3KeTbmR_4qZ56hgO0uM642E5pc66SGKBR8LaCjU3bHylVJfgaPn1XzkNDp9yZINpGhUgUgFoN_TYVUBx7N1GgOpNqts4zA6riia1GqRJxJTaTjrMu03iCWPDjd9JZbpXcxB5Cw_YnhH2HhGwPmseI_34WshA8vv6fLdmDAn8J4XUQ3_0o1LFFYv-PxeGSPPEWmzbvJYUPuqploQ96FddTKLUAuuZIuLuWM6f-S9KS4Td49vnILIOl5bO76HnuDmPuhrOvYDM7NRaboE_nN2nbsDi_VdpyATsDL7qHpxY3AGKr-sYWyGjKU_32yqi8YhadBSiBx6z-WG3m1dUnnzR6_UCDBdp3_LBXEj0NgfHERMiB-5dbe2pREVuv1jEcJ8wCLfurAowI--HDSUm6c4TrXQnoT8NIU9md7GWqopMY74GKbAv6qs2UYgrz5f5MsSchmNkAd16hhdeL9OUTkZy5Rs4jgA4k7tAbD9caaUIYsSFg2lKJ2_tLt91aq3-13UxfFNSzL9Af7l9Kd6DL9sU_VmU85ht7nI-060XdJ92fRu3IFnYzH8ch4zNuuLTuvdTJw70VT-zXUVs_AHMYZk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64ba0d1ad8.mp4?token=PtTsaDwtfabG_Cy-GS5w-YEW4xqDPP463IaN7UG2Lm2U9wEDduMJjy3_6GiiW2Sn6qjgVLOYuCZWXgSipG2TSGz3KeTbmR_4qZ56hgO0uM642E5pc66SGKBR8LaCjU3bHylVJfgaPn1XzkNDp9yZINpGhUgUgFoN_TYVUBx7N1GgOpNqts4zA6riia1GqRJxJTaTjrMu03iCWPDjd9JZbpXcxB5Cw_YnhH2HhGwPmseI_34WshA8vv6fLdmDAn8J4XUQ3_0o1LFFYv-PxeGSPPEWmzbvJYUPuqploQ96FddTKLUAuuZIuLuWM6f-S9KS4Td49vnILIOl5bO76HnuDmPuhrOvYDM7NRaboE_nN2nbsDi_VdpyATsDL7qHpxY3AGKr-sYWyGjKU_32yqi8YhadBSiBx6z-WG3m1dUnnzR6_UCDBdp3_LBXEj0NgfHERMiB-5dbe2pREVuv1jEcJ8wCLfurAowI--HDSUm6c4TrXQnoT8NIU9md7GWqopMY74GKbAv6qs2UYgrz5f5MsSchmNkAd16hhdeL9OUTkZy5Rs4jgA4k7tAbD9caaUIYsSFg2lKJ2_tLt91aq3-13UxfFNSzL9Af7l9Kd6DL9sU_VmU85ht7nI-060XdJ92fRu3IFnYzH8ch4zNuuLTuvdTJw70VT-zXUVs_AHMYZk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشت‌صحنه کوتاه شدن موهای وایکینگ دیوانه!
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104725" target="_blank">📅 18:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104724">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گستون‌ایدول: دو باشگاه چلسی و تاتنهام درحال رقابت برای جذب امی‌مارتینز سنگربان تیم‌ملی آرژانتین هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104724" target="_blank">📅 18:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104723">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5429d657.mp4?token=mMBw7C9IqgU2GRvciuJqTwadcoMzIi9WAC7cXXlWJAsyiRdXMTIWYiafCTqYVUBrqb-4zioddDOOExRTsfQRoFaiSOHH0i7B7k_rtlD-5m5ma1II-FZIvma3mR3593UOY2brJgVOET9GQ7vlMubRFlz3mkaNYcoZPZ-5GDzReurb1yDEg_BGk7WXgwapqDelMgd3QdqUABBcV3Vv7hE4TLorf5II_JW7cGOzO9VqvQj_9QQ1dyPjoaMnYOcp2zUBMiT8Htof4jbstFdmQCpaxCMUIBy2PH5Qhg4gTwSaXw5p-olTM_gcyxBR3a0OSU6-HiltkeDfXBzsYupSBsjOEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5429d657.mp4?token=mMBw7C9IqgU2GRvciuJqTwadcoMzIi9WAC7cXXlWJAsyiRdXMTIWYiafCTqYVUBrqb-4zioddDOOExRTsfQRoFaiSOHH0i7B7k_rtlD-5m5ma1II-FZIvma3mR3593UOY2brJgVOET9GQ7vlMubRFlz3mkaNYcoZPZ-5GDzReurb1yDEg_BGk7WXgwapqDelMgd3QdqUABBcV3Vv7hE4TLorf5II_JW7cGOzO9VqvQj_9QQ1dyPjoaMnYOcp2zUBMiT8Htof4jbstFdmQCpaxCMUIBy2PH5Qhg4gTwSaXw5p-olTM_gcyxBR3a0OSU6-HiltkeDfXBzsYupSBsjOEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش میثاقی به وضعیت استادیوم قلعه حسن خان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104723" target="_blank">📅 18:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104722">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72db3ef094.mp4?token=pNvVL2zlWJOG-kcJc7D1kgvDhvPazSdk2oszoD7uCn4UtSXmP1EXRHaq5K8qubOJ4VkousYvhP0CvGsRt3QeKuLhssD1ZxgqSZZPr6_Tk9rWCrxAUM-5yi_akDl5tGOtvJ_HpsQHOl-vCqunDBMXNPatdhv6Fx7SlR7Bg3y8yxDHIUyNkSB255q69PBrFV717wXUNLnALU-EhZ2p_epp2VvkT4Ze8DZZHkfd1IHUvg7AYZDbIYAmdWBADB__gFqta16xVY6ieFr8hlJ2haM2XVnIfvPzznYXdfcAVqJcGPJitG-wW4Xvh2BoBEzUke242U8U-Ssa7S-IXhVXOc31ZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72db3ef094.mp4?token=pNvVL2zlWJOG-kcJc7D1kgvDhvPazSdk2oszoD7uCn4UtSXmP1EXRHaq5K8qubOJ4VkousYvhP0CvGsRt3QeKuLhssD1ZxgqSZZPr6_Tk9rWCrxAUM-5yi_akDl5tGOtvJ_HpsQHOl-vCqunDBMXNPatdhv6Fx7SlR7Bg3y8yxDHIUyNkSB255q69PBrFV717wXUNLnALU-EhZ2p_epp2VvkT4Ze8DZZHkfd1IHUvg7AYZDbIYAmdWBADB__gFqta16xVY6ieFr8hlJ2haM2XVnIfvPzznYXdfcAVqJcGPJitG-wW4Xvh2BoBEzUke242U8U-Ssa7S-IXhVXOc31ZTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما فقط رفتار سرمربی آلومینیوم و شمس‌آذر رو ببینید.‌ بعد میگن چرا لیگ‌ایران سطحش پایینه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/104722" target="_blank">📅 17:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104721">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/104721" target="_blank">📅 17:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104720">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAjZmuxN-jXAYuaF6mJfa6FuIsha6aYH_jBkmrhoYAyQytcnERPBGhv0pkADFulP1YSoIuUAtIRizJmsyYCZl1QvzXqCF0vewj__SaDMh3PopnqzyvMK_-NTCcRUK8WIlkEam5XuSStyV2MdpFQ8uFRcY0MY9uTrgTkJvZBjneSqjiMBHXElbhau5Oo1jETjF70qEBIG_YUxmhl2cdOXHW9SCmfzZVXfLPYbZYKS7b4DEcBR1wPV8KTkX4cKvJkrCs8rX_DgKRnisWrEmTW1AV1Hj657W_eaebZQgVX10FFQp8jIExEzphX_bpMfUGLz8LcKAcih9H989uDp-V8_65xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAjZmuxN-jXAYuaF6mJfa6FuIsha6aYH_jBkmrhoYAyQytcnERPBGhv0pkADFulP1YSoIuUAtIRizJmsyYCZl1QvzXqCF0vewj__SaDMh3PopnqzyvMK_-NTCcRUK8WIlkEam5XuSStyV2MdpFQ8uFRcY0MY9uTrgTkJvZBjneSqjiMBHXElbhau5Oo1jETjF70qEBIG_YUxmhl2cdOXHW9SCmfzZVXfLPYbZYKS7b4DEcBR1wPV8KTkX4cKvJkrCs8rX_DgKRnisWrEmTW1AV1Hj657W_eaebZQgVX10FFQp8jIExEzphX_bpMfUGLz8LcKAcih9H989uDp-V8_65xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g4
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/104720" target="_blank">📅 17:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104719">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cecc802f04.mp4?token=fN1DUc0TIf7auLA2ARzKe_RVo_ro95_sguiEd0g70kryEQ42Nr7QlB8XcVixfoyGsm3xlEBpgtY3htMbMjSijcCst1dugjDk6jxWTN2KII-5Mc6OoWPDAsIRVOsrvx6XrNzJBTwFMFQUVZ-oxErlA8nWB3uPN48_2dv-LXRi9J4_mKMbKC5suu21lSIMi4NTeyyMS7tV8gzIEyDjSAQtwXcuNaEF0kwxktFpOVd2VxTHo83djKWi6AbXnQ6VGgY_xyCPqo_Y_kVOkW0a4hx0Z2LZXc2K7lGK2P1fmw8MZwyY-OYh735RMWl_SB2jSLLeqyOYdEsM1nCHd_YxrkS3ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cecc802f04.mp4?token=fN1DUc0TIf7auLA2ARzKe_RVo_ro95_sguiEd0g70kryEQ42Nr7QlB8XcVixfoyGsm3xlEBpgtY3htMbMjSijcCst1dugjDk6jxWTN2KII-5Mc6OoWPDAsIRVOsrvx6XrNzJBTwFMFQUVZ-oxErlA8nWB3uPN48_2dv-LXRi9J4_mKMbKC5suu21lSIMi4NTeyyMS7tV8gzIEyDjSAQtwXcuNaEF0kwxktFpOVd2VxTHo83djKWi6AbXnQ6VGgY_xyCPqo_Y_kVOkW0a4hx0Z2LZXc2K7lGK2P1fmw8MZwyY-OYh735RMWl_SB2jSLLeqyOYdEsM1nCHd_YxrkS3ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئال و سیتی فردا تو قرعه‌کشی لیگ قهرمانان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/104719" target="_blank">📅 17:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104718">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823997ed12.mp4?token=JUDjd0odCJ4l22Du9OeIdusHdzTd6dMgq4UYMVoG3BZUFnDUD1Oyu3e-leFOpDoL6gQuMq9opJ0Q5bACduRnqKdfQ0VpEaFH2fiKuuxRVW5tAFolT1jkNx6kr7QaxxpXQ9sV5d9WztReVb_LGWz4B0DU094WrTyg1wVOpj0Fs6iNzo7DMhF6MawnwLnmujyk8qs_poh7wt6WHZdJFJaZc7FrQwAnTeXbj8ywAvgaoCK1JWAECcT3PpPGH43Rdn-wYqoFxHEBVsiPQdnGAy57a1Fd92-tyIYX2kJ0l4Vwerm6n6RpNAD43YChooX6WEsrI4W7R8WpdPtvV_2plGQk_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823997ed12.mp4?token=JUDjd0odCJ4l22Du9OeIdusHdzTd6dMgq4UYMVoG3BZUFnDUD1Oyu3e-leFOpDoL6gQuMq9opJ0Q5bACduRnqKdfQ0VpEaFH2fiKuuxRVW5tAFolT1jkNx6kr7QaxxpXQ9sV5d9WztReVb_LGWz4B0DU094WrTyg1wVOpj0Fs6iNzo7DMhF6MawnwLnmujyk8qs_poh7wt6WHZdJFJaZc7FrQwAnTeXbj8ywAvgaoCK1JWAECcT3PpPGH43Rdn-wYqoFxHEBVsiPQdnGAy57a1Fd92-tyIYX2kJ0l4Vwerm6n6RpNAD43YChooX6WEsrI4W7R8WpdPtvV_2plGQk_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
😐
نهایت‌واکنش مجلس شورای‌اسلامی به تحریم ویژه‌ آمریکا و محاصره دریایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/104718" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104717">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIuPh-AU_4cB7paafr5OqrBeMfv4obzTmND1wCum_yahKlonRi_eSCW13iB10OlrAvJTwsbja0eIpbmxmifcnMc9aUntb0FBmpESmN8nCLVCoFDLnOOyZu9XHfpcfsezH6U9RU8eZfHqH8zSJt_3FpANUlLV20404DTZwFToHYroQjBzfb4B8dpJZLs4p8blTp6xko-2UJz6w7rXmBOuj8X-7uGJquL9llZbk8oKJR8zop6YfcuZVHAafJt2X040KxypgVdEeCNQu6LdEPMB00AbCpHjHqYORo9c4H9Legvi-fenC9f_jKVmMMgMKz615gj3hzV-VLd89BTB2qO_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
بیانیه اتلتیکو مادرید به MARCA:
🔴
«بازیکن را به‌عنوان قربانی نشان می‌دهند، اما تنها قربانی در ماجرای خولیان، ما هستیم.
🔴
آن‌ها از نظر اقتصادی و اجتماعی به ما آسیب زده‌اند. احتمال فروش او به بارسلونا ۰٪ است. این پرونده دیگر بحث پول نیست، بلکه بحث حیثیت و عزت باشگاه است. احتمال فروش او به بارسلونا ۰٪ است.
🔴
یک کمپین رسانه‌ای شکل گرفته که شامل دروغ‌های زیاد و روایت‌های نصفه‌نیمه است. اتلتیکو تنها باشگاهی است که هزینه تمام این اتفاقات را می‌پردازد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/104717" target="_blank">📅 17:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104716">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb2788185.mp4?token=d1XYvULGDp7f7tharHOdTWoaQ4q7k0aJOh5B_pEGpSaigE-cW4Y4gwBfq49KKddER-i_J9kVapneq0Y-2i7O9azFlUHqgYmYU38Qo9QsRs_pkl_k8zZxQwpafzx7GJSF0mUinTTVcSjuaQdicGQRht7uuo_z7hhqgN_958RfvZ9CUSSa3mf8UEqk3RkzNTl2P8Q2J4enOVScVo6IZLoOKtfWFoluswII78iTD2Ixz9DFf2fjYens_e9Cg4Lj_ubsnn1-4T4eyFSNssHdGnJAWy4sxD8axXfsIvbgSX7lrR6dqkCAYa6ngO_VvbTMwjsf4NuxA-FeZFU50Mzxl3F-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb2788185.mp4?token=d1XYvULGDp7f7tharHOdTWoaQ4q7k0aJOh5B_pEGpSaigE-cW4Y4gwBfq49KKddER-i_J9kVapneq0Y-2i7O9azFlUHqgYmYU38Qo9QsRs_pkl_k8zZxQwpafzx7GJSF0mUinTTVcSjuaQdicGQRht7uuo_z7hhqgN_958RfvZ9CUSSa3mf8UEqk3RkzNTl2P8Q2J4enOVScVo6IZLoOKtfWFoluswII78iTD2Ixz9DFf2fjYens_e9Cg4Lj_ubsnn1-4T4eyFSNssHdGnJAWy4sxD8axXfsIvbgSX7lrR6dqkCAYa6ngO_VvbTMwjsf4NuxA-FeZFU50Mzxl3F-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جناب بالیبا خرید جدید یونایتد که استعداد ویژه‌ای در کار با عضلات کونش داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/104716" target="_blank">📅 17:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104715">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6091db717a.mp4?token=iTwHmisAdYWWUue7ocJfGUU8admFDbBCSAqM6-j_bWm47myw1OP1v7szZPakQ4PWCtnkFGJzlbqGW2JKq7leg7h_3vg3ufu7w2CGPyEqKQz0uHIn_doGsAxnz0qXLlxoUojz8lTmzjUCzt1Rkm1B2Bce6UP83dXO5j_cpsPPGvD_nsYe0-VxeaPh3quXN9s6PP-8IyX_wCGqKneJygtlRs3oab2S9cO9YTgBoiaxdDUakZCmuQlKizbXh42iLj9vEo-BKaKWDDJOf1gDeS_UDKaYXvuPMtOMGnoG2nM3OxuUyByS7SoweiGuYd2wYutjQSAxXZifKgZ8b0SuyijcRnXbC4goj017FjNRgmDonYSTHewzrweXNgY9Rs8qd_mlJA0xl4HK-0PMJ5bM8mI4buXVESiEqrO_DyVWPBZVy7-VNLxEWSXLK6W5u617LLHkT3VkNipigTWqGDMlKJ0M5O7-U7TDfAF7aiT1lPT6Zc0ZBnuiplFWpzqVs00ljxiNpvzqNmqbVC5VOpIxUkmIAwuLLmFmogYSr_KSv_P_sFXDyNBagCricd9pn8q2qPEYSu-djGk9x-NCpIjphcqDWvyW3demm_OkzwVvgxGwIFoB0WnYE-N8hoU-L496kNz83d8DYbUhSPQYYQ6_X6yAv9oeC5aZwehrEzEc-eYmMEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6091db717a.mp4?token=iTwHmisAdYWWUue7ocJfGUU8admFDbBCSAqM6-j_bWm47myw1OP1v7szZPakQ4PWCtnkFGJzlbqGW2JKq7leg7h_3vg3ufu7w2CGPyEqKQz0uHIn_doGsAxnz0qXLlxoUojz8lTmzjUCzt1Rkm1B2Bce6UP83dXO5j_cpsPPGvD_nsYe0-VxeaPh3quXN9s6PP-8IyX_wCGqKneJygtlRs3oab2S9cO9YTgBoiaxdDUakZCmuQlKizbXh42iLj9vEo-BKaKWDDJOf1gDeS_UDKaYXvuPMtOMGnoG2nM3OxuUyByS7SoweiGuYd2wYutjQSAxXZifKgZ8b0SuyijcRnXbC4goj017FjNRgmDonYSTHewzrweXNgY9Rs8qd_mlJA0xl4HK-0PMJ5bM8mI4buXVESiEqrO_DyVWPBZVy7-VNLxEWSXLK6W5u617LLHkT3VkNipigTWqGDMlKJ0M5O7-U7TDfAF7aiT1lPT6Zc0ZBnuiplFWpzqVs00ljxiNpvzqNmqbVC5VOpIxUkmIAwuLLmFmogYSr_KSv_P_sFXDyNBagCricd9pn8q2qPEYSu-djGk9x-NCpIjphcqDWvyW3demm_OkzwVvgxGwIFoB0WnYE-N8hoU-L496kNz83d8DYbUhSPQYYQ6_X6yAv9oeC5aZwehrEzEc-eYmMEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
درگیری وینیسیوس با آردا گولر در جریان بازی مقابل اسپانیول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/104715" target="_blank">📅 16:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104714">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa2e0d67f9.mp4?token=a7pMYY0SLTpSaQqPBQuUOKhO2GAq5t5P8is6Wso0UQou4iPtakbCUBQZ9bg2AS7F4_sbUL0vB0Fjx6yQ-xhrBVB1RPXluewAD9XcWZ-zogpG-BaoRvq35PLzs4zuVLpzLvtDAzkI3m2TJ6NdBCJaw-b_FB-xI6EVpYuuakNWViFvN_SR56XXyEakx4obkc6dXUUkXbdGHQeewikJgYWeySON5RhY46gsO-XcIrHI2TF9oFBhXpzm4Ho9DckGEpK71ncVJkdFmV7vxSBNPwJFgUGRiWbgci6cnpDwkzA1NzBMvDj9CjzmzaH7z77KTf1Xe9e_rA_PtaIhR3BZLc6Uug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa2e0d67f9.mp4?token=a7pMYY0SLTpSaQqPBQuUOKhO2GAq5t5P8is6Wso0UQou4iPtakbCUBQZ9bg2AS7F4_sbUL0vB0Fjx6yQ-xhrBVB1RPXluewAD9XcWZ-zogpG-BaoRvq35PLzs4zuVLpzLvtDAzkI3m2TJ6NdBCJaw-b_FB-xI6EVpYuuakNWViFvN_SR56XXyEakx4obkc6dXUUkXbdGHQeewikJgYWeySON5RhY46gsO-XcIrHI2TF9oFBhXpzm4Ho9DckGEpK71ncVJkdFmV7vxSBNPwJFgUGRiWbgci6cnpDwkzA1NzBMvDj9CjzmzaH7z77KTf1Xe9e_rA_PtaIhR3BZLc6Uug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
علیرضا فغانی: عملکرد داوران در این‌سه هفته از مسابقات لیگ‌برتر قابل قبول بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/104714" target="_blank">📅 16:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104713">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b6ede186.mp4?token=Cpo0nnZrkKUvK9fy4vkPpOWg5atzlDSltzadBee-SctUgCzymjPMB6eogw6k1TsufByMM4Gkb05qyU_hVdcVLo-Wy8yqY1NiDLu1sX1aYqgLWP0yb_wPbsY8dyd8LMIi9wApi_j39LsMl3MPSnI_YcH-3z3DffxG5IfE9qpNRcsSGXmGO5WLbnSZ-hNY3gkF4laLlR1VS3acswegXriR8993q9HID_OmfCFfHs74bKej1rF3Ri-3s02gb_Ck7DvavdrjoiOW_8OhK-rwpxlQWQdr7ZIb8bW3LOHSyz8UG8MghH_An1wjOglRSgWvlZSdF3LbUTN3B2cRzvdkk7wz_FVZp3rvZlNow7rXWpVD1WKSqRS8uVdBl_32WHLYHliRjjCc6hK_y6kHrJOOdOfGrgo-a7pzrbqKs5If8AdaLXb0PpeFMhRprkR6d46eB1wpVFI9lCMAERFQU7TCvLxHCCsN19LyWyUHIWsq852OhqlsDWervT6ImmlHO7C3WUrGRe4YWKCjh6fucXtwv0z2D1kxpaRnew_7UGhC8sKC8xaAb8fvtznUlCqK_8eB8XbLcyXdSPCF5pv3LXhWQuM0iIcwK1DdrwToVZyROzU1Ak2k9MLe9tQ-CKKS4JOZGJTODEgV7pm2jTVITQ6QFAMDIT_8Z37_6UVkgnh3BXAM2OM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b6ede186.mp4?token=Cpo0nnZrkKUvK9fy4vkPpOWg5atzlDSltzadBee-SctUgCzymjPMB6eogw6k1TsufByMM4Gkb05qyU_hVdcVLo-Wy8yqY1NiDLu1sX1aYqgLWP0yb_wPbsY8dyd8LMIi9wApi_j39LsMl3MPSnI_YcH-3z3DffxG5IfE9qpNRcsSGXmGO5WLbnSZ-hNY3gkF4laLlR1VS3acswegXriR8993q9HID_OmfCFfHs74bKej1rF3Ri-3s02gb_Ck7DvavdrjoiOW_8OhK-rwpxlQWQdr7ZIb8bW3LOHSyz8UG8MghH_An1wjOglRSgWvlZSdF3LbUTN3B2cRzvdkk7wz_FVZp3rvZlNow7rXWpVD1WKSqRS8uVdBl_32WHLYHliRjjCc6hK_y6kHrJOOdOfGrgo-a7pzrbqKs5If8AdaLXb0PpeFMhRprkR6d46eB1wpVFI9lCMAERFQU7TCvLxHCCsN19LyWyUHIWsq852OhqlsDWervT6ImmlHO7C3WUrGRe4YWKCjh6fucXtwv0z2D1kxpaRnew_7UGhC8sKC8xaAb8fvtznUlCqK_8eB8XbLcyXdSPCF5pv3LXhWQuM0iIcwK1DdrwToVZyROzU1Ak2k9MLe9tQ-CKKS4JOZGJTODEgV7pm2jTVITQ6QFAMDIT_8Z37_6UVkgnh3BXAM2OM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🚨
این ویدیو رو نبینی امروزت به فناست :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/104713" target="_blank">📅 16:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104712">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD3j-0gCXmqOByqZ_kXUTCgb-9NlfqstprttZVkHRSWljjzN4UYyuT4gLCvDm9_Mttwm-c1tVM4tH8A43iEq2faFSZskdB5lUtfcm5Vp-L2XvNjiGXr6sYlA_RavwZwEVi54Lu_l5N3Z3TkmFiay5qAinJY4xcDfWTqZdLK_43Z6ysXsjDGLHD8KHCgBpTrxnuSewmKltmwSA49K45iI-pugM4UfIXp1Rypx-hB_BoEHrSSlu58zNSsxjDFMTQnPt8FF0XVdClXdtbm_EMtQ4UJboxn2In2_VQ-W-8WjiAbBWtT637LazNAv3QRHyhpASZfFf_qP5PDCkTxjx2lhxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
🇮🇷
استوری رامین رضاییان و دعوت از هواداران فولاد برای حضور در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/104712" target="_blank">📅 15:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104711">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🇪🇸
🇪🇸
#فوووووری از گستون‌ایدول: آلوارز قراره دست به سیم آخر بزنه و فردا پس‌فردا تمایل خودش برای جدایی از اتلتیکو رو علنی اعلام کنه.‌ منتظر اخبار داغ باشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/104711" target="_blank">📅 15:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104710">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQeOTxu5ORcFHhvzVaY_4gGkXAiyPOFD_340D5dDYGwv7eHweE7BdL8yhupxCaibE6ibqJh8cppSAEy1Sk2FxvyQzWs1xlGKpiQzsvEK5i2AH3UnyX0snVp9gOrdsAv_c8d37-WVPGVU-FpeilLKwba6k_0OtORxWDURpes-yYuz_NCU-52W4JB_v13XwpaeJ3h8FegmdrSSsWDjBXRxBMgUbxI_gFPIr1O71h8P2wah3RiQKV77BMGtIpuF8NHFKGejnKAc_1zAf4LGOoPYm_5PMNs5PkDCkvGI5kSp-NcFFVH51Na7IdvDyeajxOLK2MwiTa-KOJ_l6748RbgURw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: مذاکرات دو تیم لیورپول و کريستال‌پالاس بر سر اسماعیل‌سار به رقم ۵۸ میلیون پوند آغاز شده و احتمال زیاد بزودی شاهد حضور سار در آنفیلد خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104710" target="_blank">📅 15:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104709">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaMd0i6Rhuid1S50RJAJ1QD7LtMKlPN9oXrlAXDzArGsvSUHnBco8InNiSKlfiQcbh0a2nR6YhwcnMMf13w-2iWvurVdOgKml4TWNz1tvMCxJ9n2AUuKVMqeBBAQAtdlxNs42H9fi2lminUVIPfM-18i2sizK-UuGn-OAwiHIllkrVblpsE8ySOSk6GJNll-wFO3l3pEqyN2qJgB4l9hrTovfbizT3HV6ESWD9QpX97VBcPLN2vW5upKRzwAr2qxNgFjDEC3RJcmJ4kEaC58o0_ChdgvqYTZkkK4Hq-4ecjR_5Y0CCx6DoNK3GHcugxN3e5k8sOcmE_pkGFYN_mGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
بدلیل اقدامات مالشانه هادی‌چوپان در ایام اخیر، ایالات متحده آمریکا ویزای این شخص رو برای حضور در مسترالمیپا صادر نکرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104709" target="_blank">📅 15:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104708">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYMjNsiwYcRU6AU8v6qiEOqodu99WGgWG3bnEPdVW0hMGllrTKffdzvJzfQ_54omvb3SsDQHa8ZntCMuz_Lh9lSk37zsy-1sWE_IRIt3xAbwtnVMy-i1PCJCMtCeFetNj_HZln4ttUaV4KPYqfTXxJ2goNkuGtwBGr9x9-wsHrA45IeYucmGLaXlRZYxN-71FlrWI9qB8GpfaqH2xUBl5R3nGxM7WCtdO9-yhLcLq12L4GcuhXMv4ecqtEMMYgKtYVaGSU8MZejJYSPFBEs3OpH5h5v_b_-4GTw-SZxdgMkAg9bhBiBybBPJ9QRpIeywNQ2KCUQ-3dIUrSCLh9-dPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
عذرخواهی عارف حاجی‌عیدی از هواداران استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/104708" target="_blank">📅 15:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104707">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1136d451.mp4?token=CbHWIwe0xyMn_DgEWgfBQ75xmd7aV0T9ipEzMH4vxx8qkHzmi7eZZWs0cqOniGcstx4XOBivFsDJu8I_jdCELT3UYs8VXZK8_XJjdH3L7-_wTc30F3PXyrhQpuDxmkaJ4VNbOk-kYCMo5924crANNU-59nXWMuAsjCr2aepHA5FWX2F_BAtG_1VKTWS4YFyWUAfwXAIETB4WLMNjA5ZVlHv--VQ7n3-sDMG1pleUkbYXZDDbPLUpmhL2bEp3WiAkfP2TgqftRkUKaiPHaWNft7Z7gQdQDrgjVK-cCpp0AfuIJvWM3OwjMvkAs5onLLJLtAsqQ5IQg_9oY0aC4vyV0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1136d451.mp4?token=CbHWIwe0xyMn_DgEWgfBQ75xmd7aV0T9ipEzMH4vxx8qkHzmi7eZZWs0cqOniGcstx4XOBivFsDJu8I_jdCELT3UYs8VXZK8_XJjdH3L7-_wTc30F3PXyrhQpuDxmkaJ4VNbOk-kYCMo5924crANNU-59nXWMuAsjCr2aepHA5FWX2F_BAtG_1VKTWS4YFyWUAfwXAIETB4WLMNjA5ZVlHv--VQ7n3-sDMG1pleUkbYXZDDbPLUpmhL2bEp3WiAkfP2TgqftRkUKaiPHaWNft7Z7gQdQDrgjVK-cCpp0AfuIJvWM3OwjMvkAs5onLLJLtAsqQ5IQg_9oY0aC4vyV0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
آنالیز حرکات خاص یاسر‌آسانی برای دور زدن مدافعان سپاهان و گلزنی در بازی قبلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104707" target="_blank">📅 14:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104706">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f87467034f.mp4?token=U9m6Ve8uXLOklQETj5O3XwuoPKpv5_C9BdAABFUZOd0QkPVHS3NJ3rVPoUk5S0N7lwMafi5U6jbCdopdgOYWfpSKab4C8RVgMyRB9dWsLTVvkyvVLOsPXACL26x0vG042r0_-FmI8VlneRXpbILDIpiYcG6Xd-4z06jT3W2r5V0ubcByQj8zArdO32vYb-30L8kWpsKfsYfqxpOKy5ZC3VifLerbb0wOLuwlSxsmTsUUU-IcRdgj6Pqa6Vlw338hnMTSEmZ5q_YgPqy06cPMu9rY-m0bsFxzAip15L9elaSxheFDvOtuHsxcLZj-2okaVr8tGNP96_flJ-Y4WAASRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f87467034f.mp4?token=U9m6Ve8uXLOklQETj5O3XwuoPKpv5_C9BdAABFUZOd0QkPVHS3NJ3rVPoUk5S0N7lwMafi5U6jbCdopdgOYWfpSKab4C8RVgMyRB9dWsLTVvkyvVLOsPXACL26x0vG042r0_-FmI8VlneRXpbILDIpiYcG6Xd-4z06jT3W2r5V0ubcByQj8zArdO32vYb-30L8kWpsKfsYfqxpOKy5ZC3VifLerbb0wOLuwlSxsmTsUUU-IcRdgj6Pqa6Vlw338hnMTSEmZ5q_YgPqy06cPMu9rY-m0bsFxzAip15L9elaSxheFDvOtuHsxcLZj-2okaVr8tGNP96_flJ-Y4WAASRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سردار آزمون به تیم ملی بازمی گردد؟
🎙
فاطمه مهاجرانی سخنگوی دولت در یک مصاحبه جدید از تلاش های خود مبنی بر بازگرداندن سردار آزمون به تیم ملی خبر داد و گفت:  سردار آزمون فرزند این کشور است و اگر خطایی کرده نباید از خانه بیرونش کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104706" target="_blank">📅 14:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104705">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BA2bPmOpe3_aJPKVmiW1QHz9PsiNBpwToRLHy-EtI0DeT7WGGwXLIoU_K-6SdPaNL3C367D_DIivNObkMh0njWohR3d2PU3e5XzApbNlWtY_j6-pzuTsrR5PaqK7BM17rgmMidyewvuVzY_txsBHbh387qNnMQEcrOgbZoM_uW75EnwTgNkHMHi_VgeJsyP85PzXaRNpWaO2-08sJdtUzlLH22-VDDpeeBRffaai-qFxzm8JOz3ONlwfC_6Tc5z9wsOHK2RZN1cOvwtphCNnacHxD09vpWymNVC2SF2uIxIEddFom3Nt0XJs7JbSTSiOZKHShhLADxm6bLjzJE-VVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
در اتفاقی عجیب دومینک‌سوبوسلای تمام پنالتی‌های خودش رو به سمت چپ و بالای دروازه زده و با این وجود هیچ گلری نتونسته توپش رو بگیره و دوتا پنالتی که خراب کرده هم به تیرک خورده!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104705" target="_blank">📅 14:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104704">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635ed4f4de.mp4?token=eR0TzBm2ekmnr8D9mHMp7Or48sIQe0CqksjMq5CG2At5eMs457YlMSuUw0YjG2jJvfr8O0elu_xnfNATMAq9EsdYby_kwNBSK7T3UmfqlE061YW8pQH7bDCOSHmgZzWT7mfkMq74AmVIbB5rqAYlpFZoP9TCt283SE6aCBu4QrnQQH17bwvgWDggMCxXTxNmwNP3Udcdmhp5ZRTE7DANgCqtQ9QZHkfLmc5kkV6NyLL7m2o69I4JiwSXztWlyO4VO2FtNx7beNZyg1s3BE6EbsqFZPo2JXYhFODaR0W56z6mHtPM2cAOjsECYPZIVKkt7QwsHULUbOjZRyB6qWgS9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635ed4f4de.mp4?token=eR0TzBm2ekmnr8D9mHMp7Or48sIQe0CqksjMq5CG2At5eMs457YlMSuUw0YjG2jJvfr8O0elu_xnfNATMAq9EsdYby_kwNBSK7T3UmfqlE061YW8pQH7bDCOSHmgZzWT7mfkMq74AmVIbB5rqAYlpFZoP9TCt283SE6aCBu4QrnQQH17bwvgWDggMCxXTxNmwNP3Udcdmhp5ZRTE7DANgCqtQ9QZHkfLmc5kkV6NyLL7m2o69I4JiwSXztWlyO4VO2FtNx7beNZyg1s3BE6EbsqFZPo2JXYhFODaR0W56z6mHtPM2cAOjsECYPZIVKkt7QwsHULUbOjZRyB6qWgS9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
شور و هیجان بالای گزارشگر خانم لیگ‌آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104704" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104703">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e638c7d28e.mp4?token=HQi_TlPqHRwewkIXVSnWtNkduzb9F38j671dv2imvp65_d-_rMm55knIPoFz1dez7DMUMZxnJmCkJHxnv0XYLSiX1nEc0q576Z4KA6aRtzrt7ap4TbDcej9baV8qCOVXoan1Isq9dcZ4h072HgoZbOFlbXODRz_mSeAux6hmaE6VU5wCYjP2w06NbMUtx86FbFkpd6lT2q0zZB53sUx5ES6xnR4EKfL7ykGMWgQfHiDX8MebQyORCYFlx5ej1Jh4rdqVDQT8Cnrq8BpfeD3ttYSPd-ZeqbcfIheY-dtg2uYL2d1rFj6sQjMfUnkVcwgjGMeCOtwcWgeVwkND0vI8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e638c7d28e.mp4?token=HQi_TlPqHRwewkIXVSnWtNkduzb9F38j671dv2imvp65_d-_rMm55knIPoFz1dez7DMUMZxnJmCkJHxnv0XYLSiX1nEc0q576Z4KA6aRtzrt7ap4TbDcej9baV8qCOVXoan1Isq9dcZ4h072HgoZbOFlbXODRz_mSeAux6hmaE6VU5wCYjP2w06NbMUtx86FbFkpd6lT2q0zZB53sUx5ES6xnR4EKfL7ykGMWgQfHiDX8MebQyORCYFlx5ej1Jh4rdqVDQT8Cnrq8BpfeD3ttYSPd-ZeqbcfIheY-dtg2uYL2d1rFj6sQjMfUnkVcwgjGMeCOtwcWgeVwkND0vI8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدون شرح
❤️‍🩹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/104703" target="_blank">📅 13:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104702">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chCVwnWmDd99iXRNyinDI0r1rJ34Xvr9FOD3eX58rEOiogRdhC9SSEQtEHodg0SLKSc635jOLFeubDswgnGWOLHw0wzs6pcuN5SrZAXe5mvaf4hXehsaC8lBlGN11AdQbAdhGiCnv5fRZeY2sv8yRQHtXraV4nwLUAtcrwL1nQYIni_g70MVMAobpvecypM6w3rf4s6cbMuuFsmAeIrHVPIbXVTNOZUnUS1brhkJgfkje50tyyZ0DiB41YcfmcTjXakLOOZouXBjKs3nEcNa18ziWh8BOxlzBAT081vDmZ3Va4QwmPrz_tzhC5aNDpYBvtmzFp9xEx_a6Pv6UnsBNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
#رسمیییییی
؛ قرارداد اردشیر قلعه‌نویی تا پایان جام‌ملت‌های آسیا تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104702" target="_blank">📅 12:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104701">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇪🇸
صحنه عجیب از کتک‌خوردن خشن هوادار الچه توسط پلیس اسپانیا در بازی اخیر مقابل بارسا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/104701" target="_blank">📅 12:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104700">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f195b85bac.mp4?token=Q4ruGs19cozHJj5MGExbrh64nQclo3aItXu6r6KBfVQO3HIxsoyaZr35dYKXCAs56um7lIn6b6ZVDenGRUt6eFBps6N03HVLIAZ0leQBZ_PAT7h4Hx-Wuhw3bazpjvyCe3kV1TGQ0RGfaP9wH9_mXv1xWy36J-oOVZYjjCNEcWAgz0nh4S7S8FRryi7u_6FrR91cTyZS3by5u-S8hg6qe7k9ZQEHWFPIC_u1yifemXLbuJNyyjTZkb4LZusrag1yQEbJnmlJHX5XBtg49_qJWXTQ1lVIwBr8PzQBL_x2ClM0j_MWzI3h2CJPfNhY4cvN4Pufuu5VmV3ZojUyTuU7WLhPdBIEUi5IxUkzLlEgaQghIdvH60l5Wszgwwd4Cow2QnBr-4sGx-J0hGBWgUAoyCHTYhenbrFzgSEwJ-x9o94JVQD6LTz9u96yhnosbkttLSMPtNpFUQ3fzPEk27qc2F8QTLyn1tIhswpBDYGRRdBHvvb-1Ze51atApIGAAYMZs3QPdXrdgPhRuy3LjwU6jy5kal1lKyh4bgOzOyn7YL_IsTYFckG_61QBhYHHb1yxwfJTZnHt7a4i4o3CvimceqbWdX-NKJmODbb82qNQNxw56GhCTT6MCljBW0XQAn7Oye39hT767a-dzJkNHrs2NwopbhXrjdOPz7PxGmoPQU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f195b85bac.mp4?token=Q4ruGs19cozHJj5MGExbrh64nQclo3aItXu6r6KBfVQO3HIxsoyaZr35dYKXCAs56um7lIn6b6ZVDenGRUt6eFBps6N03HVLIAZ0leQBZ_PAT7h4Hx-Wuhw3bazpjvyCe3kV1TGQ0RGfaP9wH9_mXv1xWy36J-oOVZYjjCNEcWAgz0nh4S7S8FRryi7u_6FrR91cTyZS3by5u-S8hg6qe7k9ZQEHWFPIC_u1yifemXLbuJNyyjTZkb4LZusrag1yQEbJnmlJHX5XBtg49_qJWXTQ1lVIwBr8PzQBL_x2ClM0j_MWzI3h2CJPfNhY4cvN4Pufuu5VmV3ZojUyTuU7WLhPdBIEUi5IxUkzLlEgaQghIdvH60l5Wszgwwd4Cow2QnBr-4sGx-J0hGBWgUAoyCHTYhenbrFzgSEwJ-x9o94JVQD6LTz9u96yhnosbkttLSMPtNpFUQ3fzPEk27qc2F8QTLyn1tIhswpBDYGRRdBHvvb-1Ze51atApIGAAYMZs3QPdXrdgPhRuy3LjwU6jy5kal1lKyh4bgOzOyn7YL_IsTYFckG_61QBhYHHb1yxwfJTZnHt7a4i4o3CvimceqbWdX-NKJmODbb82qNQNxw56GhCTT6MCljBW0XQAn7Oye39hT767a-dzJkNHrs2NwopbhXrjdOPz7PxGmoPQU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
امروز 4 شهریور، روز بزرگداشت نمادین کوروش بزرگه.
🔴
هیچ منبع تاریخی دقیقاً نگفته کوروش بزرگ کی به دنیا اومده، فقط حدود سالش معلومه؛چهارم شهریور رو آدمای امروز، مخصوصاً کسایی که به تاریخ باستان علاقه دارن، به شکل نمادین به اسم تولد کوروش بزرگ گذاشتن
🔴
دلیلش هم اینه که ماه شهریور توی تقویم باستانی نشونه قدرت و فرمانروایی بوده، واسه همین گفتن خب چه روزی بهتر از این واسه کوروش بزرگ
🔴
پس در واقع چهارم شهریور تاریخ واقعی زادروز کوروش بزرگ نیست، بیشتر یه جور روز نمادین و فرهنگی برای بزرگداشت این قهرمان ملی تاریخ ایرانه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104700" target="_blank">📅 12:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104699">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTNNN0dJ14e-tIMvdhwwZeWHAo-Q0ogFb5hNxpqc3Dx5DiBmyG5SrwiDvljISbvUgmq4S_0Ip_LuPFpr3NLgWtQPV1VJppPRDWnqXkLCs6IRdEzOgl_9D6528gqvNOqo78YqTJHknbGJG1oeLbbSyxLbOn4Yoo3z2H0gdBAP4ixEeuKa30ALLzfyZJ1SD92_gHEif3lsB0Pm3c9KOgEW7r7tGLzOgfEmxqUMtywmVk0TPHLv1JbZAICQjQQ1KMZ7x6sl9tlhwfOuMjysC-KuGbAQ8Sp62QEUgFFUQakKNQ2nziKHXqFREdpfbJIJuNfLCV9w0BzqjDfCytN60gE7-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رونمایی از توپ‌فصل‌آینده لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/104699" target="_blank">📅 11:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104698">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P50JFLoGv862rZPxklnzgqK5_xuCWsc3hpDseo_raC2xHVwPy3pZ_p0NkZn9frJexi7dBs53TR1sGwQ6TnSYS6X_fHQ5pA_e7YgN9waLc2ilckHsbF85spziZeVNklsXBVbO37xJpN_r0-ZPQD3C-8ndoyQ7_FwQ-QoMSr3qaKFVN3ZHZGC6I67NSDosVDV0OBrv8ZV34bBU3jgSoYP02CF6crCphojWB9-mTSAbEf0GkndvKzk1KLLbMBOdl6kd4Y8c-lRlI_L2Rae3god6DadaywB2wNVJcB8JazRXdINBMvgDNdIoSsY6nnHVY9umHQdthuDpkZmlid2bXxJyNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
منابع خبری اسپانیا: خولیان الوارز با تیم اتلتیکو تمرین نمیکنه
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/104698" target="_blank">📅 11:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104697">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jx2VITk8BX2yM8dTacZa2eZfjqn5aRkhWzNy6r4Aj_IE5YOGwhIW6KYHX8sCpH1NQrzpT8lthehJzmUK-HjymSMecEWyzbegqbIYaPYYze_ltDHVWId2l1sbiszISh2pIColv49v_Mc8oTEnKnU0J-4F2r2SfGlMh_mIRvVd5T2kRCrR5JtAhyCCxfcvN3ERNAu-Szvq-xlQccevJOXNN_KpQal3NU1CA7Wg72odHDoUl9SSLVVCZKyftZOoRutjCaPF627ejvb-Z2XWIMCue6Cju1P3cmJTwK1HnMAXbhQItea0gORjl5aPAyjoSSfs3ZNZSxZ1qsnBoRNTxIbQMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کنان‌یلدیز ستاره تیم‌ فوتبال یوونتوس بدلیل مصدومیت ۳ ماه از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/104697" target="_blank">📅 11:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104696">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290e961780.mp4?token=IzTDlAhIqBjrBg8u-HEzBIAL_GfuNEW7fO7UbB5WbFxSt8TmKN16QJL_K-HV-WJMSFD13R7Rw5Yy4QPINTDCR1Z4F6XUsH2BVKLNtJP9FyFvP-Q8CRAl3UQEllQU1vvrTrp-OYDmH8CtLVBfslmJmqLiF93dbY30j7yP5_ortnk6TBGn8JM3h4KKa8h98_4xZnC7gzNwcSpVkqTqAHgWaex5UaC2AquIJ9w5Pd27ItszTZrnURlye2O0kcLjzr_89DBsVEqfvsAkD7v0gJHP96n279j-nkQiJK-we_VrvN4xMiIqvoFZxx-aM0SwnLUXrmsiTzMZyCm9suM5m_d7zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290e961780.mp4?token=IzTDlAhIqBjrBg8u-HEzBIAL_GfuNEW7fO7UbB5WbFxSt8TmKN16QJL_K-HV-WJMSFD13R7Rw5Yy4QPINTDCR1Z4F6XUsH2BVKLNtJP9FyFvP-Q8CRAl3UQEllQU1vvrTrp-OYDmH8CtLVBfslmJmqLiF93dbY30j7yP5_ortnk6TBGn8JM3h4KKa8h98_4xZnC7gzNwcSpVkqTqAHgWaex5UaC2AquIJ9w5Pd27ItszTZrnURlye2O0kcLjzr_89DBsVEqfvsAkD7v0gJHP96n279j-nkQiJK-we_VrvN4xMiIqvoFZxx-aM0SwnLUXrmsiTzMZyCm9suM5m_d7zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
تفاوت آزادی بیان در ایران و استرالیا‌ از زبان اسطوره داوری دنیا علیرضا فغانی
وقتی مجری از او درباره فیلترینگ فوتبال ۳۶۰ به‌دلیل انتقاد سؤال می‌کند، پاسخ علیرضا فغانی شنیدنی است.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/104696" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104695">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/Futball180TV/104695" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/104695" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104694">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gl4FUyyLAbA3PaQ84IJGkzPL_phsCJ47hM1I5FWqf3fcuv18ITPve9bGYo3qOVDaCNKcPSabiAZdLQutG_7b6q_LmO6d6Fafdo59nix8lBHIbrxeXvzi1-RcOT2o_vcpwxHBicuS2Zza3Cy7o8wd7MWTj-F9A9WD1Wb0HhtqwBfXt8NPZvYMrenLs4TG6YIxdFNUG5e5Qy0lnfRa9Tw-04_VpKJ-YAcEOSjWTxVFMS2Um4iNoIZ0dF_Hs-PFZ3xUr6fUkG3xdosS20lZXQU8blepC_PSBbRRSjUy7EPLbpcB5xemtDpUeJ9aAIEZweqWsod3WvtjMbdVco4G6BS4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r4
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/104694" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104693">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb7772379.mp4?token=bHdPmFMrNlPYsnEKIo1np5obuog1Xah9D_A9zpfezBtIqhiUA1N2Y2ZdN0aO9LTVE4G5wYcOvUA8bNSgOFNcqIgcG6-m6KAS4Iyb2aqCEH5Kni_Ehd2SlYDUHNFNfXKFHz-JJusrfdVSeywf2WOMaceKiLRNNKaWUdZ9Lizkt-wzrXHwQzb4S96vieXg_RbMZ5-XD4lAi9gsc0HPs2gLGM9w1krTg8ODxO5d-VvoTZrC_jkoSCUExcPdRczqXNc7Rtkv2m8dDp-_1IUEj6gon67GUi4bFEXyNlxhl1Pb4p_C-haid7tvOVRbgIZWV3oS5sk83pbtDLT34Qh7ZyRw0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb7772379.mp4?token=bHdPmFMrNlPYsnEKIo1np5obuog1Xah9D_A9zpfezBtIqhiUA1N2Y2ZdN0aO9LTVE4G5wYcOvUA8bNSgOFNcqIgcG6-m6KAS4Iyb2aqCEH5Kni_Ehd2SlYDUHNFNfXKFHz-JJusrfdVSeywf2WOMaceKiLRNNKaWUdZ9Lizkt-wzrXHwQzb4S96vieXg_RbMZ5-XD4lAi9gsc0HPs2gLGM9w1krTg8ODxO5d-VvoTZrC_jkoSCUExcPdRczqXNc7Rtkv2m8dDp-_1IUEj6gon67GUi4bFEXyNlxhl1Pb4p_C-haid7tvOVRbgIZWV3oS5sk83pbtDLT34Qh7ZyRw0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ژاوی هرناندز در اولین کنفرانس مطبوعاتی به عنوان سرمربی تیم ملی هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/104693" target="_blank">📅 11:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104692">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fdf3f04ed.mp4?token=W9tJWbzZjs_OsA_Bg-ymNVki6dmdl2_Aem1jFdak8GRplFp8r8EykEUhSoHT5AO9roaSCHo4zo9sJ-PB9pXdiUWld30RJc157Fw5_NC-AGp16hMAfOFOO0xi5cQMP8D21b50mkZfgVH8SsDPHRvYwvhHuyft6p65pctr7cfqsdxjgEArahwM0hja8k6XzoIFpKpj4-CoOyxbYDMnp_HNiK80FVvPzXUEU2mM5q2lWx8xaLegJbnCS21eZ1IM-gqEEb0BF2oMAjzhxKuUAjG-Z9rzYollowHPC7pXoq5l9jL43aFlH70p84EGGcgcV2A5DRq8eJ33C-hKhPjmmPpAQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fdf3f04ed.mp4?token=W9tJWbzZjs_OsA_Bg-ymNVki6dmdl2_Aem1jFdak8GRplFp8r8EykEUhSoHT5AO9roaSCHo4zo9sJ-PB9pXdiUWld30RJc157Fw5_NC-AGp16hMAfOFOO0xi5cQMP8D21b50mkZfgVH8SsDPHRvYwvhHuyft6p65pctr7cfqsdxjgEArahwM0hja8k6XzoIFpKpj4-CoOyxbYDMnp_HNiK80FVvPzXUEU2mM5q2lWx8xaLegJbnCS21eZ1IM-gqEEb0BF2oMAjzhxKuUAjG-Z9rzYollowHPC7pXoq5l9jL43aFlH70p84EGGcgcV2A5DRq8eJ33C-hKhPjmmPpAQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلنگر و صحبت های جالب انریکه درباره رفتارهای دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/104692" target="_blank">📅 10:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104691">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mboyftFkAB2MmapyYujar8KYgt9Q5au2acjqE2eUjlK5QaytAkLgHhLG7bmR1OVioSagR1Irwi_WoEROWVXDm2BWwLezWjkkwRXpucO1WTm82B8Uz28eWhHTyPklEphzJW7zXq7eQylu-ly_TkA_ejUP17IBsrdOsSfiUs6jUHGmZt6hYOpvbDyc7QumE1Ituj7i6Pi7LDQDcd9LWC3FK7xDPsXJyvtyk6at5pi96mV88zlHeyIgrxpnKQUewzbH6YyDh7Zluji41_Z4QXk483JYxB0fKdhdC5slPO7cOFwG0e7YkKIim1QJwpYiK9uSOC-Vo1t732DPyLeDGwJMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
اعلام اسامی داوران هفته چهارم لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/104691" target="_blank">📅 10:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104690">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=jniXtXuF6BQrkqruRXqHrmUrI7cX5uW7SUA0icQAJYXqe8WZyhjuwTGcNW_wNVdcompA6CnVejwN1MhuHnIAbWDqMXO8_1P3VTIFo1bbJzb82V0WCJi9qgIK9vAu3-IMFxL409zDJkk4l0jZnulbnnAzIcFY3AF76zOMCtiOvaZWAsQ_9CDcmtk_vGP-Ku4LjSSotK8jOlialFjHz6xjjx3g4JAXkjo83D9tJYWK6R3Kddsom3WX9YXIS3Y7Dy9oWhZ6AhILPFSO07ExggBnJPuuWE92aBJmtJIC5UfzMMn3N_Iup-Tffur4zsHQE9dKVFrOz6ianC5QPn-2_0KiBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=jniXtXuF6BQrkqruRXqHrmUrI7cX5uW7SUA0icQAJYXqe8WZyhjuwTGcNW_wNVdcompA6CnVejwN1MhuHnIAbWDqMXO8_1P3VTIFo1bbJzb82V0WCJi9qgIK9vAu3-IMFxL409zDJkk4l0jZnulbnnAzIcFY3AF76zOMCtiOvaZWAsQ_9CDcmtk_vGP-Ku4LjSSotK8jOlialFjHz6xjjx3g4JAXkjo83D9tJYWK6R3Kddsom3WX9YXIS3Y7Dy9oWhZ6AhILPFSO07ExggBnJPuuWE92aBJmtJIC5UfzMMn3N_Iup-Tffur4zsHQE9dKVFrOz6ianC5QPn-2_0KiBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حشمت مهاجرانی سرمربی تاریخ‌ساز فوتبال ایران، به ثمر رسیدن اولین گل تاریخ ایران در جام‌‌های جهانی رو با روشن کردن یه سیگار جشن گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/104690" target="_blank">📅 09:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104689">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWIhflvYA5_rhy7tMYndxuTivw8uPZomPUEHI8NEgxJgduw160k_bSUAh381X988V0Zifn7GcFZpFDM9ge7LZiHRLEp6KrAJELMuLK3AHxxPL2-94OVIHwzmaFwTqU2qGlMMbA0exlsvNfqZoVySOaAhWueO6t5bgH81qVUQlsE5eMd_QiCuuUk9ATOHoA9k5dYaF7BY8zBKEhH0DGr1pjF7Nf_LZd4Fl8WdXW-j9hsv_T69v9z4ohlCUOrc9oan2nV8soCYoquZGxke4kw_CDx21cmL49q3gj3HBKxGEtUIZeVXda70NmofgRzR6C6rcVKEBtXXJY2Fwfh-Gcuzvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
📊
محمد صلاح در دوران فوتبالش در تمامی ۹۰ دقیقه مسابقات گلزنی کرده بجز در دقیقه ۹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104689" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104688">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdb56b243.mp4?token=uHCHEryLMTVwhx2iQ6SQH2ABSJlvzi2IQrAuTlmD0kEn__2ZpKq3y4w0loUKnm7EhrX-8Lr1X5xliKINf-0nIvBkb8eXXFmILiTqXZAEAFLASBmhXlOW5EgduELUv1w9srnNx2JCJfBngD1DseCFlWviO-wGiDA5OYPlF4SY6-SxUuMTmMCtStvvEaDxVqzCkA90ePM0EYuH5ApYrsOvtlWCPNxiAatRYd-MP6DjAmDAoSvULcq118IPD3YcpIlEB37dN_M5O5zIDaiCQjcOVqcnwWn6aaeW6x16y2GUIQEMU4_HUNIk212pJUcK6ueGnAbKVOAZcQvtpCN7qcJYkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdb56b243.mp4?token=uHCHEryLMTVwhx2iQ6SQH2ABSJlvzi2IQrAuTlmD0kEn__2ZpKq3y4w0loUKnm7EhrX-8Lr1X5xliKINf-0nIvBkb8eXXFmILiTqXZAEAFLASBmhXlOW5EgduELUv1w9srnNx2JCJfBngD1DseCFlWviO-wGiDA5OYPlF4SY6-SxUuMTmMCtStvvEaDxVqzCkA90ePM0EYuH5ApYrsOvtlWCPNxiAatRYd-MP6DjAmDAoSvULcq118IPD3YcpIlEB37dN_M5O5zIDaiCQjcOVqcnwWn6aaeW6x16y2GUIQEMU4_HUNIk212pJUcK6ueGnAbKVOAZcQvtpCN7qcJYkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‏
✅
نخستین تیزر رسمی از سریال مرد سه هزار چهره به کارگردانی مهران مدیری منتشر شد. این سریال بزودی از شبکه‌سه پخش میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104688" target="_blank">📅 09:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104687">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKgWpSE4CiGeAyNx7d-j9L6ZCO3tgvJjZrbBrQW3nxaMvYUti7GNjCq1gg1RWDvqWCJxD7A_H1rmcuMVtDxmxz7E7rnz48bsq6z8wD18Y3r_dCG93tM_A3Nm6jswKglcCuVQXLmZ78VpzUlW1YZXexaT-Yta_pdmykU4FDbLnx8n650x1ZOdJ4IJ_zNPhnhHbdNlI9lZ6xBGB5s2JTCxf9eBchzJJRQuNsadvZpgf-nffB7Y6hekVLEB2w7t8vANluYNl9-IYvxbGCG6VXeXp0V-q4VVC6MilwD8ovMIwb9ErtBh-4ZwyXRcgn1KPaEI9F0oWv0stt82jvjyz-oUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق‌گفته برخی منابع خبری، باشگاه منچستریونایتد قصد داره در ساعات پایانی نقل‌وانتقالات برای جذب کاماوینگا از رئال رقم ۵۰ میلیون یورو پیشنهاد بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/104687" target="_blank">📅 02:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104686">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/strj968iBg21O0GxBSf7vUAmtUd229hKj872xWTv7fSYyyt-gAnHn2aGXZZ9psCl4Ao_fgTDiQedZVQbi3BY_dg4MmhVLg4AleULEyUYhyu6VFZj0tS5_qQtXG1cMG-uT2ZEmb4JDYxyaQkwP_yGtbPTAI14Uhy3RdsQujv_9vkEqvP5G1Q2Su2yN-2OhO3trzP6lCwudpdme96S5aQNcnNq_N3B6NnAL-AD7cr3pUns7lnYJwZwsuDEUwXXbq2iCYgko41OOlaJTatrAim_a7k2G9rk519I4xQkbv8RPKsVzUoKdCedKUJDm6Nwth_UUQ7_yBrBHcMYlGaNrnH8aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇦🇹
تیم‌لاسک‌اتریش که در بازی رفت سه بر صفر از سلتیک‌ باخته‌بود، امشب تو یه کامبک سوپر تونست ۵ بر ۱ برنده بشه و در مجموع به مرحله گروهی لیگ‌قهرمانان اروپا صعود کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/104686" target="_blank">📅 01:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104685">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSCyPiFloGNP5-Ye2DblT__Zvgm3zzOVi1gmSHlSrVjRW3IIpM5K3Ca_Ik7WpLk_pUoYGq52p4qyrl9MVKxCb0xoGSWvu3fJAxr7lnZWv6ptjmJJr2_W-3nJfqa0Oz2pZj5GT2jKKA6UD7uj7tDsTagg9W09OJifcrBzUL8hJuZKGDWmbXr2VDVU2Hctuf0vHRXA8_v0F37-lziwEfcfoP9YJsIqfRehST0sfb2hQfBlebKIbwWr3jKDHuK59B8AaDP8iNCgxN5YG8ILEnNBkoX6S35za_8cCFnriXaDCk3fTaDrAk21-DP6uelF-7KD42H4EpdDrqRHKsnHO-LhuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسلونا ۱۵۰ میلیون یورو دست به نقد ایستاده که آلوارز رو بگیره بعد خیل‌مارین مادرقحبه نمیذاره آلوارز جدا بشه. حالا اتلتیکو باید بمونه و یه تیم ناقص و‌ آلوارزی که دروازه‌خالی هم احتمالا به زور براشون گل بزنه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/104685" target="_blank">📅 01:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104684">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qdUV3fuwxYOSIq3DWX87LF9Cr0ow5vLxFivmIFKwd2lRkWnI8_vK7kcoYTYCFC4LwVAzdI9Sd_yJipfB20DKaOAdU9uGx62yfIYnE4aTLCwW2g4bKpRQHqQAUE3_y0eOKFbpaWr39PPFXtO10XAIkMR84lHiFrgz0-BvYD65vcwu1f32x62WA16yCC0NQfsU9aHbIoGv0OVp_q6TQxzv4ktF8MooXig_pIUxovXZsoFv10qlwCpl1FJFtc3IEKoqL4PVnAcvDPWOSf7DYCIR-6c2hs6Q9AzgGZSCnQLFz5z5haJXEDz4fAcROWnIlOl8kLe7wudbU_YUkp5K6Xdm4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇴
باشگاه بودو گلیمت نروژ با برتری قاطع مقابل حریفش راهی دور گروهی UCL شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/104684" target="_blank">📅 01:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104683">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBGpwAf8Q3oCenKdjEpz00ym0uVLdwFstIeTxEqf1fkdHVEHOaXeZEbbR9CYjHqTmBViA8rCIPNOnRkFyMDxq7elfmrBbAlelSHDm6ToZCqhUVQ5kAekqryM1debpyEvmGlfe6iLejBXo9LOPqPQ8StGsa_Lux-qcJWm2basWTfm2iLi2capMZB4LyX1WL_SotmfRxCI93GgfSCoNwTXMoeF090OA6gOv6cCQEMTQgYFs4CPm82_2rfp6DIGm9A0sZV89wqYGi46SXHgssU68XRk58N9gjZ3zr2g4HmF4WDC77a9fMze56UCCdr9Iyz-TkNz2tXYk3dhaduuSCvZvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
✍️
اتلتیکو مادرید نتوانست با تیجانی ریندرز قرارداد ببندد، زیرا شرایط مالی دشواری در این باشگاه وجود داشت.  ‏
🎙
پدر تیجانی ریندرز:
🔻
‏"ما امیدوار بودیم که با اتلتیکو مادرید همکاری کنیم و دو پیشنهاد باشگاه القادسیه را رد کردیم. آن‌ها بسیار علاقه‌مند بودند،…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104683" target="_blank">📅 00:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104681">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC5JZ3tHZkCcZrERv-PctH5AIztWlgLUryv4Y--HvWtKa_fndzYH73Rg2tYmRfaeeKsxBXQMhFNQtixF4Wux_fD8p20ZCJNtNABUhoRg_HkE56521TcefX-WMTsUXWfEVJYotOP-W2XT7NZPChX2ax5DNbmdF7pR6FTrst02WUgr6hb1VQ78o4tmh2MZsi_y4jFRsKsfcvgJHqZz4Brw86-dWUxuY221FWWBZfOzFlWdzLLlXQt2EBdAp-Xdx8LUcKJRlIVaLzUl6DMeTSJd7bshycMJZIAajcTc0x2NiMv1qpus6l0z9jsrpKJyhH1LaobtaRYcmPT8r5xn7QkeLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇸🇦
رومانو: اولی واتکینز قطعا از تیم استون‌ویلا به الهلال خواهد پیوست و مارتینلی هم بعد جدایی قریب‌الوقوع از آرسنال در یک قدمی حضور در تیم اینزاگی قرار داره
!
گمونم خدا به تیم‌های ایرانی اساسی حال داده که قرار نیست با الهلال فعلا بازی کنن
😢
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104681" target="_blank">📅 00:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104680">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i02N9uwU5fnfB16qogmhiAUElHC5lqYS_3__W6d3LlnzNvCLlyvmfAMyvVExF5zyW31M5LsapDlpGIV4fl2pLcMI-3T02eqeDsyI0OXzMIsuxWtES_ljcHPipGzxcPkld_sLu6Bn7v8TXLnoj9CFJvaCMNwBbtiEIgCehCgio-tbY6IETNsVcnlw7t5qwsrLIeI_T0abj0XFjfLXMX88d_o6A_-z8xiXMO6AIF9Yc0eaaBuWCsEK6xWlwEgWoDhp-Fa8k9PtOLcNQNUlOe-fxMQqpGAQYQQlQjxCeZpvQs7qw9ziS_PfVUtz1X7hIcUAiRJOqBxSV-v0ngzN_cK-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
✍️
اتلتیکو مادرید نتوانست با تیجانی ریندرز قرارداد ببندد، زیرا شرایط مالی دشواری در این باشگاه وجود داشت.
‏
🎙
پدر تیجانی ریندرز:
🔻
‏"ما امیدوار بودیم که با اتلتیکو مادرید همکاری کنیم و دو پیشنهاد باشگاه القادسیه را رد کردیم. آن‌ها بسیار علاقه‌مند بودند، اما در نهایت به دلیل مشکلات مالی، از این معامله منصرف شدند."
🔻
‏ما بلافاصله دو پیشنهاد از باشگاه القادسیه را رد کردیم. تیجانی هیچ تمایلی به انتقال به خاورمیانه نداشت.
🔻
‏آن‌ها برای بار سوم دوباره تماس گرفتند و پیشنهادی را از طریق تماس تصویری ارائه دادند. سپس، ما برای بررسی این موضوع به آنجا رفتیم. آن‌ها به دنبال این هستند که بزرگترین و بهترین باشگاه در آسیا شوند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/104680" target="_blank">📅 00:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104677">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🏆
باشگاه صباح آذربایجان برای اولین بار در تاریخ خود، به لیگ قهرمانان اروپا فصل 2026/27 صعود کرد. این باشگاه آذربایجانی در سال 2017 تأسیس شد و کم‌قدمت ترین باشگاهی است که در لیگ قهرمانان شرکت می‌کند، با عمر کمتر از 10 سال.
🇦🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/104677" target="_blank">📅 00:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104676">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myrMNO0tjjF74aCimg2mQS5oTwsUzBnb-3x__hjadCerpBn8QidiYh1_FcQ5GLA7qr3bXC7uG9X3KwAN2z881hxN5Wouc1jsM3hZ4JzSpdjzbqWzUYH4EkXDk9D39GqmlTIgj86skDWvyMNFBXgyRFraPU_8JjZWnU4B4iPEX1C4MeYoyPH7mdLGiFF7Rz1gfRouWmW_LEa5B35KOzoCVw2K2Oq9QJ_66MsRaITQ416XIZZht44MCsm1CkZAX5TpohFcV_OogWWKa4AnoTmb6DDwF-hLV4_vGo4zWGCsqvfyoMHn16tw48gpDZ51AW6xjXXIvFNlH3n5EOefREN9SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
باشگاه صباح آذربایجان برای اولین بار در تاریخ خود، به لیگ قهرمانان اروپا فصل 2026/27 صعود کرد. این باشگاه آذربایجانی در سال 2017 تأسیس شد و کم‌قدمت ترین باشگاهی است که در لیگ قهرمانان شرکت می‌کند، با عمر کمتر از 10 سال.
🇦🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/104676" target="_blank">📅 23:56 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104675">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNm0PqWty05FaSUkZdIbRbx1kUYpvnwnUrWZejiQjuGoCFiAgOBEAbRaNsid534Il3mCQ_cO0YrpCelkhwlAwa9cxcSMR33sLc1LCyGnLYuLosMFLKuKK4mPhekhb2CCvoN2IEgpnQoGJChnQMeQYpyLUzluOUJKfL-RqSnZK6biYQlVpH7WodlG2IB8oMREnPWX8h8X4MLbTR0TiiSAKC9wZ55NXSRXh0hL7Z__ubbJXPnDCTGf7v01MuiNpLm5QW5FEvL4SQB7HhgyqMwaW-U302PqohR46oQDX2bP4B0MSskODfTfwA7JE49bzc5mTqZXmuqcTYgaK_KNtf4uUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚑
🇮🇷
#فوووووری؛ اوستون اورونوف در بازی امروز دوستانه پرسپولیس مصدوم شده و تا فردا وضعیت دوری احتمالی‌ش مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/104675" target="_blank">📅 23:42 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104674">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41704fa8fe.mp4?token=rCPRJOhP7qBcKYpeuRcEJpjnJSLsVcX_fTLjbrLWwKAefdGiZhXJIxx20qcLuMIoiHRtxERUhlI752fZvyBCD7yPgJOCtyLPJPu8DnSVSqo80Y0CyoU5rl4oU83SW4o8M8EUaIZ0ecGcZW98Aq0VyX9V1Y4Ph_OqGTpJaOZukYX5hWrX_jYi9T73UTSHjnIOdW2Grtqm2RgQ-ZYe7TNKh0mkrybA_6keuFZQunBUQD7ht9d0k2fPAZXlXPcVAqrpoWFxjDC0F2Q0kHtOiGGdGJ_hcIAgOk-yewyfN56TpdUNXbGtPb_pF9vj7Qlp2Ek7lYj2J9Td7_nuqEiApHzQPF5h4DLDbnmz5_NzA9x9Ay99oAa88to4b91nET7fQXy3R8VeONONGwlnq90M3xIBnY7LWDtAyiLBp9ek97aw5BAhlMy2ln2HBaaS-JEDRfTfV6YVTl3NkQ18gGRLvopk257xqHxAGk7N2sTsqL_ALFajXccylsCwJiJWiXBY3rSc2CiwCOo0euVcV5FfIABZHs4-oitau0u86XZH2J8n44ghA2UdcdKWsyMNFYgGrqnQRjmhRBudwIakG2IyyGlu54phinMIJTs_uIsV1u30-Us2YKACJlHzFEObOYpQmQgGuI0AZEst6vitOmwxTBXu7tWbM8Tsk-SaNPhQ6ntj3wI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41704fa8fe.mp4?token=rCPRJOhP7qBcKYpeuRcEJpjnJSLsVcX_fTLjbrLWwKAefdGiZhXJIxx20qcLuMIoiHRtxERUhlI752fZvyBCD7yPgJOCtyLPJPu8DnSVSqo80Y0CyoU5rl4oU83SW4o8M8EUaIZ0ecGcZW98Aq0VyX9V1Y4Ph_OqGTpJaOZukYX5hWrX_jYi9T73UTSHjnIOdW2Grtqm2RgQ-ZYe7TNKh0mkrybA_6keuFZQunBUQD7ht9d0k2fPAZXlXPcVAqrpoWFxjDC0F2Q0kHtOiGGdGJ_hcIAgOk-yewyfN56TpdUNXbGtPb_pF9vj7Qlp2Ek7lYj2J9Td7_nuqEiApHzQPF5h4DLDbnmz5_NzA9x9Ay99oAa88to4b91nET7fQXy3R8VeONONGwlnq90M3xIBnY7LWDtAyiLBp9ek97aw5BAhlMy2ln2HBaaS-JEDRfTfV6YVTl3NkQ18gGRLvopk257xqHxAGk7N2sTsqL_ALFajXccylsCwJiJWiXBY3rSc2CiwCOo0euVcV5FfIABZHs4-oitau0u86XZH2J8n44ghA2UdcdKWsyMNFYgGrqnQRjmhRBudwIakG2IyyGlu54phinMIJTs_uIsV1u30-Us2YKACJlHzFEObOYpQmQgGuI0AZEst6vitOmwxTBXu7tWbM8Tsk-SaNPhQ6ntj3wI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
ویدیو وایرال شده از دعوای خیابونی عجیب در گیلان که یک مرد در دفاع از همسرش دست به کتک‌زدن دوتا خانم دیگه زده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/104674" target="_blank">📅 23:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104672">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkLHYw4Hylq5PKCkKX52bkPBks6eOEHQcd9GUVfpxLH5cXCirH3S2YhfV4h8WJFdK8A-qmWRvsWlKlpfdysGSoLfblk--q6UzN-g4UIUz2pRW5xbHh5jcXZmVwVQee58BDT4aruB5s5_sd1U980CZXM-OQQMZQr5r_lINx3j3JIFr--CSq8AJLSh8wVuIBZEUYSX6DGlHJ1f8FqzLVIwXkuYEL5haIKrs5D-VfTSWGKc_6b8-MxuwqFPeWeQQqAfkfXj2sPOzi6ZaTUiXRMzjo1nPXtK4QxNpj63FFKp3StAxJ8IwMAf2oehU2OGmSNdptdUzXRkoDisebppwZ7_YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز، برنده جایزه بهترین بازیکن لیگ انگلیس برای فصل 2025/26، بر اساس رای اتحادیه بازیکنان حرفه‌ای.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/104672" target="_blank">📅 23:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104671">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fcFDenyt6p-IRJaUTX8gLqyEyZBlII3olHOe5nYX4aJFvjr2ZX8M2SKTW8_chynxQ0Cbzmycx_MQMFoXEH5X6onZANwW0JxpAQWhu4JDALE_HrV2vnFoGa5bmt3mQvD6EnL0tA-As-BBYrptSZuKNUULtOBT-gskqPN_5UhbmpQtrlarqrhxpUquwYDEGtRcrexWjlmHGNLDlL9zFnXA4gcRl-Q9r-7Quk-q-R2cLB7cpns_vwGA2eC6dT14TKj1nWcKDkEgPEgmphA_oLSBV9-gtBw934UDkQCwVwGNPBnKmP3O4E896HAdjEyLplpn_Ac9jQ2FDPagIdNXRnfwoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب منتخب فصل‌گذشته پریمیرلیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104671" target="_blank">📅 22:44 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104670">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/090cee5ae0.mp4?token=ICH5o0TIgu9w99ovHd3ZOEYLg-qzS-ayLVKRBuhacDvLd0MVq5nVNurQCk0iHt2HQwyGSDJBP9WUNpj6RUG0bsm5vsMoKUe2pcqSO4QxK008dP_-a1twebRBb2MjLgrHI7Wz4xDKViQLMIaC2sLfWeNrPgr9jrt2alV7iWfgjBF5Bq5f0mGlCvu1jNxhjqz0uPGB5aUcsJUPICvSHWY85X7Hoq-5XfRXQEdbf9BgYaQ0vQR0Bhi75ZHADL_ZqA-SZDLRnOvaKbQRpDoHwTwSNjk6484iCuoUKL9PmTgcitnA51EHHZX_hh1tiZ6-ehIsIQBG3QM7pdcn2nhuc2hwGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/090cee5ae0.mp4?token=ICH5o0TIgu9w99ovHd3ZOEYLg-qzS-ayLVKRBuhacDvLd0MVq5nVNurQCk0iHt2HQwyGSDJBP9WUNpj6RUG0bsm5vsMoKUe2pcqSO4QxK008dP_-a1twebRBb2MjLgrHI7Wz4xDKViQLMIaC2sLfWeNrPgr9jrt2alV7iWfgjBF5Bq5f0mGlCvu1jNxhjqz0uPGB5aUcsJUPICvSHWY85X7Hoq-5XfRXQEdbf9BgYaQ0vQR0Bhi75ZHADL_ZqA-SZDLRnOvaKbQRpDoHwTwSNjk6484iCuoUKL9PmTgcitnA51EHHZX_hh1tiZ6-ehIsIQBG3QM7pdcn2nhuc2hwGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
سخنگوی دولت پزشکیان: احتمالا قیمت آزاد بنزین به حوالی ۱۰ هزار تومان میرسه و ارقام بالایی که مطرح شده صحت نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/104670" target="_blank">📅 22:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104669">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TK65sTaUwua2abgsjgf4urSRfF8L0iLhueGw6cVP1-p-uVQFdY_EYrLkYjUznc9FtpjyjuYxYmP4KdrwlOib5RKNc38L_laPzX0AR7WVF3jVigS8tOCjAWzdOcP-xCIIutVgHDpVOkXe_g7My0jQP2hlN9BAutbOAKEdskUzbftIknGBUxUZcnylaNYpaFgtKp88k0YYYsmWKcIRHjDnPevYK2mfF82mhqA7nKXQIaArWbrgHPfvzgGvnBY2aCTX0bPJAltn2SBR-jreabEcAr14PQVkMLWZlOT0ziweudLGydn4MiJ8nmihoBP6T7yTEbTi9a0LGNlaj9K1UFWf1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گستون‌ایدول خبرنگار مطرح آرژانتین: مذاکرات سیتی و چلسی درباره انزو فرناندز آغاز شده. ژابی‌آلونسو در جریان این انتقال هست و در صورت توافق مشکلی با جدایی این بازیکن نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104669" target="_blank">📅 22:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104668">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2063216dff.mp4?token=QpIOGpmoHsicRf3AhZCUF3YN4q7RAOjNnPHBv8_z9-wPDFV3MYs--oq1DU_BGT1GMfeH3qJUl3gh7IyVg0Uto1Y-fv95tjRG8zKf4iGF-KWHw--hBYWi3MsgI9iSlEHEVz-EYJdXB2HX2zQKTAgt8i66B4i8P5JpVPFqqsktJy6Ynzwy8lgMKOfccvjVwhy8pE5xNVLWWSGaNPsXBfwXc2uBIPTe9lZ_0-EvXBIuBidHVr46RKs4fKx5lqFWV6iv0NkmydAS_GeTS8d2XIVWghfZuXayF3abb4mvW5SH-86nHV9Qq6d3xoumhl88lp1LGLKBRX9_aSER7zP8DmodM48o9n2KKARAt6ipjxNZUhqDe9YiaMbaZ5AEnSIoDdCMQjapDMGSyA2Yxyw8FMgo-150_qy9BdQZQ93ipDSKOCOre58RQtN0NU0jLj2Y9wXjnSUGlZUOvKPhejz9aNpVxV_xiX1jUOQRHom2LeDF3oaGNxUsz6mRqJlvBpNl1yN7K9hN2m3qSwApesVoiueTMp16KGR6bLMYcSeGZJAyONJUWMIsW_mn_xUdB6ZnZNr1NsvwXnj7f4viQVcYw_kTKjM61E_4PVjayf0ZbMr4PRuPwUNMIQPhVdn7WtYaGa9qsL3Gp2FqMzFg37lYP2M_gZpJldYLxPMIwK3TxbGIndw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2063216dff.mp4?token=QpIOGpmoHsicRf3AhZCUF3YN4q7RAOjNnPHBv8_z9-wPDFV3MYs--oq1DU_BGT1GMfeH3qJUl3gh7IyVg0Uto1Y-fv95tjRG8zKf4iGF-KWHw--hBYWi3MsgI9iSlEHEVz-EYJdXB2HX2zQKTAgt8i66B4i8P5JpVPFqqsktJy6Ynzwy8lgMKOfccvjVwhy8pE5xNVLWWSGaNPsXBfwXc2uBIPTe9lZ_0-EvXBIuBidHVr46RKs4fKx5lqFWV6iv0NkmydAS_GeTS8d2XIVWghfZuXayF3abb4mvW5SH-86nHV9Qq6d3xoumhl88lp1LGLKBRX9_aSER7zP8DmodM48o9n2KKARAt6ipjxNZUhqDe9YiaMbaZ5AEnSIoDdCMQjapDMGSyA2Yxyw8FMgo-150_qy9BdQZQ93ipDSKOCOre58RQtN0NU0jLj2Y9wXjnSUGlZUOvKPhejz9aNpVxV_xiX1jUOQRHom2LeDF3oaGNxUsz6mRqJlvBpNl1yN7K9hN2m3qSwApesVoiueTMp16KGR6bLMYcSeGZJAyONJUWMIsW_mn_xUdB6ZnZNr1NsvwXnj7f4viQVcYw_kTKjM61E_4PVjayf0ZbMr4PRuPwUNMIQPhVdn7WtYaGa9qsL3Gp2FqMzFg37lYP2M_gZpJldYLxPMIwK3TxbGIndw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🥶
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسله بعد ترک عربستان و بازگشت به اروپا؛ عجب حرارت و شوقی داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/104668" target="_blank">📅 22:04 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104667">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ushjcr58mFWjE2pPi_FSxifVBB_QoIAK1fhhLLjuhFkgvvGC5Zv0VI49Yilr0yGmvAZVkT8K8ci4xzZ-FrRrqTHsXab0u0FDLQL2OUNt20Ph69HjeoS3v-oKV_4JmbL9kx21iBqcCauRnXaF_oHdez1Ql_cfAIYrcbE9S1m9WMPAsjDAZavboGfs6I2BS7TcL3dZVXTsWtwTYUVKUOLRi-RrkgADUka0XzUjsNFqGM_3vfs76gywMe-nVdJMVfZEtrOFHP5No15-RKoOHalKz3XfGN6ry0O4SDtim6BClATeMfX61GpJxzRzKonBx7a0vIfywGanN6QNoOq-O0y7Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نیکو اورایلی جایزه بهترین بازیکن جوان لیگ برتر انگلیس را برای فصل 2025/26 از آن خود کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104667" target="_blank">📅 21:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104665">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccff2e7a05.mp4?token=Rx-cNfGIhpuId60Qi_uWar4sOojMnX2GuxO68ZaxEJ6AChl46Vbv96Z8hNO60skHfJc8sidv5ZElKEXW4F5pb7ZsEn2ETQmMvaR0zM-CChny11u2hTvWRoxuBYwrgNPt03rQAadUBcpXtJBw88H9lvjNd0rr7-Ci9NK3ghS0Njtqc1VXfEsyV9ooM-xwwxeBe74HFAeaqjmBhRFc2Nl2eeucmZMU2nYNZ9lgDkYLUEvPdd5YqjqGv3iaijO-7llKPBOaKn447kdP5wkcAb9w-7LaEJRK81a2PxYqr3bUHmrEcXVz-DP1bWVhfyv5SoJnll2YdMGoiQt2XExbXur4sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccff2e7a05.mp4?token=Rx-cNfGIhpuId60Qi_uWar4sOojMnX2GuxO68ZaxEJ6AChl46Vbv96Z8hNO60skHfJc8sidv5ZElKEXW4F5pb7ZsEn2ETQmMvaR0zM-CChny11u2hTvWRoxuBYwrgNPt03rQAadUBcpXtJBw88H9lvjNd0rr7-Ci9NK3ghS0Njtqc1VXfEsyV9ooM-xwwxeBe74HFAeaqjmBhRFc2Nl2eeucmZMU2nYNZ9lgDkYLUEvPdd5YqjqGv3iaijO-7llKPBOaKn447kdP5wkcAb9w-7LaEJRK81a2PxYqr3bUHmrEcXVz-DP1bWVhfyv5SoJnll2YdMGoiQt2XExbXur4sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⚪️
ممبینی دبیرکل فدراسیون فوتبال: قبل از جلسه فردای هیئت رئیسه  تقریبا به این نتیجه رسیدیم که قلعه نویی سرمربی تیم ملی در جام ملتهای آسیا باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104665" target="_blank">📅 21:23 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104664">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFMyQ4q_RJGEguRi_CtuNxYss5NYeSi1pvZu8UTEeniwqbDNSl6NztNSTvRXYsCQkmeK2cfVngz59ZvfP6G6-a3xI6yHbfaAms6YsfRjgCGe5EuHR8aJboQgBg4ADhpwUbZlFJ6M-HvpLVgZbxmu80_POUg4ugdbYggSFJX5wiB0g-7eVFmsiUykOIDKA3iBKt-Tp1WauTkgDSPyX47efU5EJ2MPsUSzm3_e3h3O7DNyuJn9kEaCZYLD4r7VlVEqOZRuii8an0w886SjsZcjcGs0oekMVglNNMXMktKpcvJwEC7yHidZgTUR26TL-scDBUqgxu_CatsOHDvBZGvbSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚑
🇮🇷
#فوووووری
؛ اوستون اورونوف در بازی امروز دوستانه پرسپولیس مصدوم شده و تا فردا وضعیت دوری احتمالی‌ش مشخص خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/104664" target="_blank">📅 21:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104663">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db2b316284.mp4?token=LCu_Ok1VAH7etlu4wyoT6XWGN0Xb6sIsX1ksQYpoA6qY5uXDzxdZADqDFUkzrMj3YMG-LadHosrTvpq32OiWMPLBD_Fb-__yENMenXGNItzIZ7OxNbd9HPbba4kF_HyfPJ8fsk-oCDyslvtO5r8C5GvJL1VNx_uLTP1DRCQSyAe8BCWzD1yVo0fuppKZA65swGr0fmeQOta5YJfyWd5bS8HTQclS3w9KH6Bku68pOnYYVifGcpOKug2qC2yUKI7lfo4AHD06ip0AiQrYgu5gh-alFv8eX_wlodrC7TPjJze2QOMjwK0pINRWwS6x7_8X_ijzHyZU84cSdrpDn720hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db2b316284.mp4?token=LCu_Ok1VAH7etlu4wyoT6XWGN0Xb6sIsX1ksQYpoA6qY5uXDzxdZADqDFUkzrMj3YMG-LadHosrTvpq32OiWMPLBD_Fb-__yENMenXGNItzIZ7OxNbd9HPbba4kF_HyfPJ8fsk-oCDyslvtO5r8C5GvJL1VNx_uLTP1DRCQSyAe8BCWzD1yVo0fuppKZA65swGr0fmeQOta5YJfyWd5bS8HTQclS3w9KH6Bku68pOnYYVifGcpOKug2qC2yUKI7lfo4AHD06ip0AiQrYgu5gh-alFv8eX_wlodrC7TPjJze2QOMjwK0pINRWwS6x7_8X_ijzHyZU84cSdrpDn720hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
اشک ریختن هوادار فولاد خوزستان در بازی دیشب در آرزوی دیدار با رامین رضاییان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/104663" target="_blank">📅 21:03 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104662">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqcZ0KdJFqlz6XKUWi9mN8oorV7vlrUwNVbqNbJx-CgT5F6YB9tE24J6rChs_pjhSg_HoSjbN7JAx-jD-5ykLJIyHsx6I1dPJw33zDeTlbMEy-0CpDMXhX7CTN3w81xLunfLmH7OukRWTRWt4pbzJ_UftWcdrYm76c6Boz6FQxdnAVgINu3DPzKcoTLWnvwXgvkJv7-mLttZOcV3sAsM1anI2PfFZP4XySzyOPM7KPdLiJ_PzuXbEcSPiCFM8qNZ_erV4XhzeaYrmYbZS5m12lCNu7RQbSDJd04ehy_m9J7sjsGYYg2P5ne3hm9n4D5aGBZ1KsqsNy10rzHHsX3tew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: لیام دلاپ با 50 میلیون یورو از چلسی به ناتینگهام
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104662" target="_blank">📅 20:39 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104661">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FUSMtGa2EmFKMszOqIYwMfCDH1fLXGwEbxniv3j9fzgtLwcuI7WT3doegs7i5qLWthxGGeJSFJslvQcS5Vc9khdZR9ZFZaVZvBL3hqEhB3rtgskD0F4lZCftVc5M4cuAGCddyGpqyfX0M0By-E7ggxbUUZHAyNEIhT211pNUQpeESHOfaatsWmTVi84tnWuvBsytzCgQmUxP-y6G58ns4KTueYzotDuCe4HtJvLlBc3IB7LdMlOTmS0J72_0mnqPtYiT32H1pfGOQ8uyHbokIqBTJDkIK7Yweam7oHkv8neXSIzbiIJ0W99hJNNcnWkEwtYFMCTJ1kAAsghG1Ahubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو در ترکیب فیکس النصر مقابل الاتفاق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104661" target="_blank">📅 20:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104660">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcPi42NpWjNULN8OoUzCOFmJmE3gc_7Uxpy31p_Qi5rj6yE3f63bnZSQ_0MSu3vMDRwXDt09VexoGr8W_6fP9A3JVs8dOGdNB86QtWUdxOgaeqnywciI3Qjd-hpT_828ZkRYPbufNkWIBc7dtDvx-OX4pFvgsn_FP8qmDggcJdtEeAT4erNi3CbDufqsv-d8m_aeCN0CoHhh2tiLDv_osm97kIn5FyzgabvnT9_984yfeBMGiXmpVp-sxba18DyeXclsb1Ef3MHcv1M0F1sa_KPm-1G3zPbVzLqi0185tiwJirV9JftQkMYZRc5UQCpZkyjrJS2FgRTLeOccUNWhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
✅
🇮🇷
🇮🇷
بیانیه باشگاه سپاهان: رفتار عارف حاج‌عیدی مصداق بارز رفتار غیراخلاقی بوده و از تمام هواداران استقلال عذرخواهی میکنیم و تنبیه‌انضباطی متناسب برای این بازیکن در نظر گرفته خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104660" target="_blank">📅 20:06 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104659">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuFI28I4jBeShXDE-oRn2IsXIAykuec4AB-lHOPC_CiXB-LbaoP1rfzfbAbeAyW9sO2O4Nk8PXJ0dGHXRnCLs1ziFLFuHOfHx9Tdu_p1Lc3aXmsajbWm6I4NL8z3Q1R5GJHZmzRcrMyGJlPembfieCkxsPSsad9zqVnToBo5C4RwZEzX2AFwg9sCZZrfvxjMibGn4wYMdwPiXU0W_5vyPBgCdic3xYtLlML7d2EPogxoPZ0-UCjb0KZhV2JoI88mpDpclQZA19cDGHCnex6vbAd__Gbg-VwZeN3OBicLyaYQrIpeatGb1e7pVYFALqEukJKAnz8GyvGbsXdT19XB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
دیوید اورنشتین؛
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇫🇷
لیورپول و پاریسن‌ ژرمن امروز در حال انجام مذاکرات کلیدی بر سر یک توافق احتمالی برای بردلی بارکولا هستن.
🔻
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بارکولا میخواد به لیورپول بره و نمی‌خواد قرارداد جدیدی با پاریسن‌ ژرمن امضا کنه.
🔻
🇫🇷
پاریس این بازیکن رو حدود 145 میلیون پوند ارزش‌گذاری کرده، در حالی که لیورپول می‌خواد معامله‌ای نزدیک به 100 میلیون پوند انجام بده.
🔻
✅
مذاکرات امروز دو تیم گامی مهم در جهت مشخص کردن اینکه آیا میشه به توافقی دست یافت یا نه، تلقی میشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/104659" target="_blank">📅 19:49 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104658">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48bb1d2255.mp4?token=m7x9B01iDgAyluaXVjgp00zcYS8rcmg3y-cDPySVYzdJxiMlf2f4h2s2xWyIROPVdDBckaLYQTyyMdKjsbvq527HE8B1_DmczYiIKUXCsxXGWDStwdgvfWz9bmyvFj1iUjxCLO6dDVgHEZVa8M9qkaloSeQWo9zF52LWwrz_RGzDkxJbOmsgRW4Xqruh4GU73--4sFhOcONW2VrwyQYyHggWAa72OHok3IPqfT-CEhiuDMm4YjiotEJq4Mg65_3U0aJpu2FvNiAzcldNuId0x0duXhhKVhweCQ1wmtHbR8n4AtQE6YuD5pDdWpPQTJ0L47Pv3uUuBy08XtETf-VziRg8Np62SthOvvudMjbhzwlU63pu18iVn2YFFwVlQuuWN1HUlfbldhLu0dtBftsQKGbbFF-tRA9P3AtMcC6ig0WEBEsyMXYEdWZdM-Rdvd8V8z-6Hj12vrGVqwdcS9rN8tiqeGOkIvl98a_zJjiTVMjhDkX8Flbjlj9L5SpDGCAljw0Fe4dwyPe8gM9zaH0I2KLR2bNQ-1XVdt6ciZT9TfHaMB5qzv8iMeuluHuuv2zHRELmopZPL0nToDVUmBgrJwSsMg8mKwB0htboUbmYJ6NRFbz9DlFxq5q0x6FZNEwi4Kfxi_842uD4_w9aDITto3na4nkHEIVqAcgz7NW2U5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48bb1d2255.mp4?token=m7x9B01iDgAyluaXVjgp00zcYS8rcmg3y-cDPySVYzdJxiMlf2f4h2s2xWyIROPVdDBckaLYQTyyMdKjsbvq527HE8B1_DmczYiIKUXCsxXGWDStwdgvfWz9bmyvFj1iUjxCLO6dDVgHEZVa8M9qkaloSeQWo9zF52LWwrz_RGzDkxJbOmsgRW4Xqruh4GU73--4sFhOcONW2VrwyQYyHggWAa72OHok3IPqfT-CEhiuDMm4YjiotEJq4Mg65_3U0aJpu2FvNiAzcldNuId0x0duXhhKVhweCQ1wmtHbR8n4AtQE6YuD5pDdWpPQTJ0L47Pv3uUuBy08XtETf-VziRg8Np62SthOvvudMjbhzwlU63pu18iVn2YFFwVlQuuWN1HUlfbldhLu0dtBftsQKGbbFF-tRA9P3AtMcC6ig0WEBEsyMXYEdWZdM-Rdvd8V8z-6Hj12vrGVqwdcS9rN8tiqeGOkIvl98a_zJjiTVMjhDkX8Flbjlj9L5SpDGCAljw0Fe4dwyPe8gM9zaH0I2KLR2bNQ-1XVdt6ciZT9TfHaMB5qzv8iMeuluHuuv2zHRELmopZPL0nToDVUmBgrJwSsMg8mKwB0htboUbmYJ6NRFbz9DlFxq5q0x6FZNEwi4Kfxi_842uD4_w9aDITto3na4nkHEIVqAcgz7NW2U5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💥
ستاره استقلال رکورد جهان را شکست
🏋️‍♀️
عبدالله بیرانوند از تیم استقلال در جریان لیگ برتر وزنه برداری با مهار وزنه ۱۷۲ کیلوگرمی رکورد یکضرب دسته ۸۵ کیلوگرم جهان را یک کیلو جابجا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/104658" target="_blank">📅 19:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104657">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c5505a725.mp4?token=jhKnXq26aJPbGUYaoMD_2op5CbKMqKhkoHynBBBELV6_MDd4rHG3pnQhvXO3mNk-FRYVFxIT2_tCXgslk6zMzYan6dafx7jqu3etUX8dTDA313inSouZVQNkFTSR_b2J1fS7dcANbCpCf55PPbLiv1MZ2aJPzRWon4XMwp2I_5Q2iMjojzQyY-rlgot94QSKWEWLBMg2yN0pC1-j39ujfNMl8QWhd9yZzAG0wRmiB1MLPEuCeX-8jxqilH_QyGRgJFkVZiSKnVbiE0Mj519kGQvL1ElXH34PiZNRte9qnGmzTdkEAzoAR3JFIhZcd-dXeltcFOK2gtzInGkhUWUtZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c5505a725.mp4?token=jhKnXq26aJPbGUYaoMD_2op5CbKMqKhkoHynBBBELV6_MDd4rHG3pnQhvXO3mNk-FRYVFxIT2_tCXgslk6zMzYan6dafx7jqu3etUX8dTDA313inSouZVQNkFTSR_b2J1fS7dcANbCpCf55PPbLiv1MZ2aJPzRWon4XMwp2I_5Q2iMjojzQyY-rlgot94QSKWEWLBMg2yN0pC1-j39ujfNMl8QWhd9yZzAG0wRmiB1MLPEuCeX-8jxqilH_QyGRgJFkVZiSKnVbiE0Mj519kGQvL1ElXH34PiZNRte9qnGmzTdkEAzoAR3JFIhZcd-dXeltcFOK2gtzInGkhUWUtZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
❌
⚠️
علی‌محمدزاده: پژمان جمشیدی از اتهام رابطه جنسی عادی هم تبرئه شد
!
💬
محمدزاده وکیل پژمان جمشیدی بازیکن اسبق سایپا و پرسپولیس و تیم ملی فوتبال ایران: قبلا هم پیش‌بینی کرده بودم که رای پرونده پژمان جمشیدی چه خواهد شد. خوشبختانه، متهم یعنی پژمان جمشیدی از اتهام تجاوز به عنف و حتی از اتهام رابطه جنسی عادی هم برائت گرفته است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104657" target="_blank">📅 19:07 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104656">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ کارلوس‌بالبا هافبک باشگاه برایتون با عقد قراردادی به ارزش ۷۰ میلیون پوند به تیم منچستریونایتد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104656" target="_blank">📅 19:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104655">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4-uuTwi_Mk-r8zfQFxta5eZKsdOQmPL5NlAuND2GhNKU4_w5xxmRe0bAHNoNVGnDL94dCb07swd8HcXoxMLF5sfaFpyheZbJftU8FP_8ev5L-LUlVT7Rl6f0Kkr2W5GMjblO3eSbaHWa-RopCgjFVue-CMDKeE0pnb1J6BzUyq6aFrlpzBGWu60rfVrnLcEY1pt9nkAkXB2UOoEPTD4KtKSNfmnRhmUTq3yxSPEt9mDIDMZTsG8uhnnUcOSSZct7i29lpV2aRFM_xOkM-WH2FJgd_XxqCfQCZ64rAw2N7L0KDFxDqlkxCLXDtPMBj7HN8x0Wjmt3Xs_UHgN3jKoyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
پرسپولیس در دیداری تدارکاتی با نتیجه 2-0  تیم امید این باشگاه را شکست داد.
⚽️
شهرآبادی و ایگور سرگیف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/104655" target="_blank">📅 19:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104654">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4xClmF4EQ2Q8nQDFuAp_6Uzu2Z5vVJQ8wasjFPOOnxOu3Bn2iSNii4DSwVxFZlPMa7d0px3y1BPjwNGQVMp5glPBk079iMXDvxUlL4k9Yot-g_WtXqr-5MH6sIgMBwSkEzpn34KfdyE8ndhLs_5a9JxhZ-40d8triGDtke7n3m3kfDvTlGGCbOXzRmWP_ap7NuLE_tNbeFSC3FDSaDZf0R-lw1NoqYCW5KATKzxCdx4Jwj2xZiCkeqWQfu9E7s8r4gTQQdu48cHd0RcaGIwvgTH7OvKa1hsb_W6IPWmLAIJYzLXuyMx_W9hQkgXsZeQLAhK10_h75qO9rzozcFOgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
حرکت منشوری و عجیب عارف حاجی‌عیدی هافبک سپاهان پس از بازی دیشب خطاب به هواداران استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104654" target="_blank">📅 18:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104653">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33e507f396.mp4?token=O84wp0AoTGY3oAqVd0pOm8dUdBQjND8aS0aRLaHa9hysl89VlSlCj_GWP-gIygQGivwJKVrJBDbF1FGpvrGZuFoaK2oAX9sBJP1vV7P6k1xd9I4JRA6fASpsbEaDhCcDNc4Y6qqoD0nTTxEOyobpb6IkTdayZBw0IDyhNSGmU4tZZRcQCTazE4idGKav-dwhV1pQBGCdwlzciPyW3pc0s_-zJ8Yl7twIvfTRqNVaNgvHgzfLON53q9sBZSAjTzd4mbtEWncO5Vr1ykpvx_n_4O_BUNzg1_IA5UsY793uNn2Arqi7y3gD2B75-QmPGQNUqdaqjj8pkDTHuwr3BVDt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33e507f396.mp4?token=O84wp0AoTGY3oAqVd0pOm8dUdBQjND8aS0aRLaHa9hysl89VlSlCj_GWP-gIygQGivwJKVrJBDbF1FGpvrGZuFoaK2oAX9sBJP1vV7P6k1xd9I4JRA6fASpsbEaDhCcDNc4Y6qqoD0nTTxEOyobpb6IkTdayZBw0IDyhNSGmU4tZZRcQCTazE4idGKav-dwhV1pQBGCdwlzciPyW3pc0s_-zJ8Yl7twIvfTRqNVaNgvHgzfLON53q9sBZSAjTzd4mbtEWncO5Vr1ykpvx_n_4O_BUNzg1_IA5UsY793uNn2Arqi7y3gD2B75-QmPGQNUqdaqjj8pkDTHuwr3BVDt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
واکنش محمدحسین میثاقی به تصمیم سهراب بختیاری‌زاده برای نیمکت‌نشین شدن علیرضا کوشکی: با تصمیم سهراب حال کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/104653" target="_blank">📅 18:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104650">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9040b715e4.mp4?token=cGtWkz5J6lK9z7vxcR-P2PmwhqcJTfhmEhQjd_cXuXrQ7na9JcfnfeZmIJZ-sEWTsWzXMA3SDSJYv3Wd-n6-zn5HW4P4UbZpG11aJX_Nyp0-43-P5hEIBgPpHLdibLUKIf2Peb8owUnB_CEQsDZmdhveuhD3g566BwfbUYS3m6UUMuMIB_l5XxqPZe6IBXPkZRyARRpSEI3ISDjzHRPPQaY5FE0JPbaV9ApKTImq6Hzn9PZDrX3dztsG1iksxjvyberJatpEP8670l6GyRCibx-zsCDuOcuDJm41FTEND8iu-ioZRge_QEKRnPwHwRR5kXqObJEBzPgGgTxXuNUwdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9040b715e4.mp4?token=cGtWkz5J6lK9z7vxcR-P2PmwhqcJTfhmEhQjd_cXuXrQ7na9JcfnfeZmIJZ-sEWTsWzXMA3SDSJYv3Wd-n6-zn5HW4P4UbZpG11aJX_Nyp0-43-P5hEIBgPpHLdibLUKIf2Peb8owUnB_CEQsDZmdhveuhD3g566BwfbUYS3m6UUMuMIB_l5XxqPZe6IBXPkZRyARRpSEI3ISDjzHRPPQaY5FE0JPbaV9ApKTImq6Hzn9PZDrX3dztsG1iksxjvyberJatpEP8670l6GyRCibx-zsCDuOcuDJm41FTEND8iu-ioZRge_QEKRnPwHwRR5kXqObJEBzPgGgTxXuNUwdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نباید هم بترسید؛ آقایان مسئول می‌گویند از تحریم و تهدید و محاصره اقتصادی نمی‌ترسند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/104650" target="_blank">📅 18:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104649">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
⚠️
بخش دیگر از مسابقات جهانی ربات‌های انسان‌نما اینبار در رشته وزنه‌برداری!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/104649" target="_blank">📅 18:10 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104648">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d29aa087.mp4?token=VIDg70iZXYuEetLlp1J4RaJI2Iw_y-m7GnHd7IUqh7iRpyXP0ogfag4LhXFgdGxi46bhVii46kxXdRGLTuPqHCGsXQaQxl9-dD-3CWSo1GXPmgPVwG9xQsKEW4yCqs5qTRO61msjp92ZTT49P1oOsinGa8-rO0EImd-uT8j7BGonPg8MCDLLfiGi1epQB4gXcuPZ6prQqUkLkvRfv0pMTcBV6Cu7Ud89ncNX12qYemPpBY3chkeJgJJiXcSsHAc7EdV5so0yC6ItJsJyHQuEpcG0__2dHTSNlc6ul6QNl3i5hfg4RWgmFXYTLdRlS9YShyBRfVt7kFfuAlkpXqg1kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d29aa087.mp4?token=VIDg70iZXYuEetLlp1J4RaJI2Iw_y-m7GnHd7IUqh7iRpyXP0ogfag4LhXFgdGxi46bhVii46kxXdRGLTuPqHCGsXQaQxl9-dD-3CWSo1GXPmgPVwG9xQsKEW4yCqs5qTRO61msjp92ZTT49P1oOsinGa8-rO0EImd-uT8j7BGonPg8MCDLLfiGi1epQB4gXcuPZ6prQqUkLkvRfv0pMTcBV6Cu7Ud89ncNX12qYemPpBY3chkeJgJJiXcSsHAc7EdV5so0yC6ItJsJyHQuEpcG0__2dHTSNlc6ul6QNl3i5hfg4RWgmFXYTLdRlS9YShyBRfVt7kFfuAlkpXqg1kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای تارتار والا دیشب پرسپولیسیا نه پرس کلوپ، نه‌پاسکاری گواردیولا و نه سانترهای آرتتا رو ازت ندیدن برادر. قبل حرف زدن دقت کن استاد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/104648" target="_blank">📅 17:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104647">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f287b16532.mp4?token=oVz64wMssBQu1Ne4Q5alxbiOLF4_X_FG9wkHOcG7Yz974pJyKX2Dq_rB9pzCQOfTTxdw7l7lu1oDnYuX7wO0MrRkkHLpiW47jnrXNUWTNB4sL1I9zxsVd6od4qE_VtK-Pe6lV45kgzHT6p0vOYRz153XtFf0K1xOCmy4Dz0gK1puZZYqw5P6A0HzzvxL7lhFCxIoVf6x3X5qBh7swlWZXScC11xUQ6_bPk4mLLp2snk4L5OcAN5zkXe15Ckb4YaXjdd5wyEEmLQQ6VG1zCywrobtQ2znNZYu1EM6el0yz-edgFphY8mKVX8WkiuVrC6LrD6UH8_uLWKDmz-W6vqZgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f287b16532.mp4?token=oVz64wMssBQu1Ne4Q5alxbiOLF4_X_FG9wkHOcG7Yz974pJyKX2Dq_rB9pzCQOfTTxdw7l7lu1oDnYuX7wO0MrRkkHLpiW47jnrXNUWTNB4sL1I9zxsVd6od4qE_VtK-Pe6lV45kgzHT6p0vOYRz153XtFf0K1xOCmy4Dz0gK1puZZYqw5P6A0HzzvxL7lhFCxIoVf6x3X5qBh7swlWZXScC11xUQ6_bPk4mLLp2snk4L5OcAN5zkXe15Ckb4YaXjdd5wyEEmLQQ6VG1zCywrobtQ2znNZYu1EM6el0yz-edgFphY8mKVX8WkiuVrC6LrD6UH8_uLWKDmz-W6vqZgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😃
رونمایی از ربات رونالدو در مسابقات جهانی ربات‌های انسان‌نما در پکن چین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104647" target="_blank">📅 17:20 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104646">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KemAA1R65ySx9YF8qkg_Bls0m-c3F24VrIqZQ1d1N_sO9iVMdX4X8e84syiPNY9eZL_5oSIA87NNcofuY6y7-9lOboFk2xurC0JTermIIs7QlrYxOfPMKtuM3pEEnYYcEr01KcALZsDs5U3v4Y87FzDbodQ_gzxTmRQGcn4uHwEMAVwZZQXdm2Pu3Ayumi8DpA1igRuotcNxhLpXUcNW1lsQ4zWabVPrK5I6GRacmX_PujdKBZ1eVZ72L3BOnzbaJvODSPusyniWGR7-PYQQMAzyYEVAihGFnhcyZnt1tZ9VvUzv_1nOm81u013O04HXWB7UkBqn9F3Pd6xEGwy5DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
روزنامه RAC1: بالده اگ پیشنهاد خوب نرسه به موندن فکر میکنه و فک میکنه میتونه فلیک رو متقاعد کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/104646" target="_blank">📅 17:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104645">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2f481f1fe.mp4?token=k5zxJ7irLe9o45NUuGAyIfywp5sfYY-L_LCbtegFG32yuPCqSBLPhTprCWz4DoORpuztDMdLAytEeg_2G0NI3h5Ty9e0-W6pqnRkRmoorb0rqnNcACfS19Ac6tfUKSDHm9Rh1PsgV81lihnq3sMQ5YErQlCzrNxL_mPo94Xem0UyAoEnacCoIKXYGE1JH3O10Y_vATGuT8vTFg52SBC-yxYBzUvaFrM4fACfjUDzXz0YzmnVhVZAzdfMvoopMRggdBAupMWQCCW8JjgaeTI-GSSBPtv01wGg7CT0A1so-IR38z0SxVe6Xfpl2v4koiKWn2uRU5sdnzh9W0AcAN3zfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2f481f1fe.mp4?token=k5zxJ7irLe9o45NUuGAyIfywp5sfYY-L_LCbtegFG32yuPCqSBLPhTprCWz4DoORpuztDMdLAytEeg_2G0NI3h5Ty9e0-W6pqnRkRmoorb0rqnNcACfS19Ac6tfUKSDHm9Rh1PsgV81lihnq3sMQ5YErQlCzrNxL_mPo94Xem0UyAoEnacCoIKXYGE1JH3O10Y_vATGuT8vTFg52SBC-yxYBzUvaFrM4fACfjUDzXz0YzmnVhVZAzdfMvoopMRggdBAupMWQCCW8JjgaeTI-GSSBPtv01wGg7CT0A1so-IR38z0SxVe6Xfpl2v4koiKWn2uRU5sdnzh9W0AcAN3zfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتایج اینترمیامی با حضور کاسمیرو:
4 باخت،  2برد،  2مساوی.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/104645" target="_blank">📅 16:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104644">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29f38711d1.mp4?token=ZryyKG0r6KkhLwhsM035ZtTAF3G6SkTo_f-QJnHnsGjKmsUkDTY7kD8kcefpCDRtOXEFbAQUzGfZStLLyRkLyKS2B8EMC5DdRrcUGLWqwZqE1Y-uJ0CN9Ke7JckVvZGU8pS1IZIw2czjLFnJOpLTpWggQ7iX-2OOAKmRQEtwWbe6-coib9WVk0OcWzbtYcYOymspZBhyNxz5nelnCUJdULA5ziYX0QwXVadZz8pXmVU9I15h4sNvGR6SJc03kEDgL8umX_QZwFj-TDHz14OGxsNzMytvlDkNJqhsg0YxEikPlyv6wxNdX7VFysrJz8pw0hDj31fXXZFlP_90SaGFTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29f38711d1.mp4?token=ZryyKG0r6KkhLwhsM035ZtTAF3G6SkTo_f-QJnHnsGjKmsUkDTY7kD8kcefpCDRtOXEFbAQUzGfZStLLyRkLyKS2B8EMC5DdRrcUGLWqwZqE1Y-uJ0CN9Ke7JckVvZGU8pS1IZIw2czjLFnJOpLTpWggQ7iX-2OOAKmRQEtwWbe6-coib9WVk0OcWzbtYcYOymspZBhyNxz5nelnCUJdULA5ziYX0QwXVadZz8pXmVU9I15h4sNvGR6SJc03kEDgL8umX_QZwFj-TDHz14OGxsNzMytvlDkNJqhsg0YxEikPlyv6wxNdX7VFysrJz8pw0hDj31fXXZFlP_90SaGFTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هری‌کین در نقش هافبک در بایرن‌مونیخ
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104644" target="_blank">📅 16:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104643">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88cac48e79.mp4?token=enxhhV2l1TMYCXJSYerskDnLN9V5yEKBdfFlvn83Mkd_GVPOZ4jKNc8FiSdrG2KMWQNwtUw4CCFEA0YKZ_dX8UxvgBJpC8yinP8zUbIwEK5ichK3nqeAyHGWu73R6mg4YeOFLnIiZtU8NDEU6Z4QWqutliVBtcDHRLyeRE-GEqA1xL83eMJoYT453J87BxYXEhDpCByxDudUwoqBMxeZ2nxzBY1aRR-Ru58icZQ2G55GYLYfsIY7B4NHHzqbUkmlgl9AF728LfObsz8fwvZIGjv4pEmUpYioARvl2CRs1Hu2AxZ32Chb6jC4CM_lb4JsXX1OkpbixGpSy0TbeJ4t9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88cac48e79.mp4?token=enxhhV2l1TMYCXJSYerskDnLN9V5yEKBdfFlvn83Mkd_GVPOZ4jKNc8FiSdrG2KMWQNwtUw4CCFEA0YKZ_dX8UxvgBJpC8yinP8zUbIwEK5ichK3nqeAyHGWu73R6mg4YeOFLnIiZtU8NDEU6Z4QWqutliVBtcDHRLyeRE-GEqA1xL83eMJoYT453J87BxYXEhDpCByxDudUwoqBMxeZ2nxzBY1aRR-Ru58icZQ2G55GYLYfsIY7B4NHHzqbUkmlgl9AF728LfObsz8fwvZIGjv4pEmUpYioARvl2CRs1Hu2AxZ32Chb6jC4CM_lb4JsXX1OkpbixGpSy0TbeJ4t9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😞
وضعیت روانی خولیان آلوارز در اتلتیکو دقیقا با این موزیک میشه شرح داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/104643" target="_blank">📅 16:05 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104642">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed5ac9e8f.mp4?token=Qg3Wz45gQ9mblYTRR8dc57hKmJycR0N9XkXUurTxOI9xKRV7nRd7KQ1kRKuhEzAI63xobhuvbWxD9irJOBRMWHr_Yj8KtWHzoeV_fjZhFYJH6ipMInPbbXPG-Zbcf2sJJ2kQtTgGABk2GDHbPdW2R7hfA6j40-b4h7jnQWsTUOB3KEvVE8bqUGAXr5LGv_JoIr8sMLPHgarPKJwOyl5oP7hf9v0-plaUQex4qq_eLknOAlAwbWehdulrINuFgebmlAvlIjgESEfoWx-TitUDqtfxMbBOG8QIqRfEHXw4QLqL87gTg75jzVNtZwsC5N-xUH_Td7OEIHNArE8jLQlzkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed5ac9e8f.mp4?token=Qg3Wz45gQ9mblYTRR8dc57hKmJycR0N9XkXUurTxOI9xKRV7nRd7KQ1kRKuhEzAI63xobhuvbWxD9irJOBRMWHr_Yj8KtWHzoeV_fjZhFYJH6ipMInPbbXPG-Zbcf2sJJ2kQtTgGABk2GDHbPdW2R7hfA6j40-b4h7jnQWsTUOB3KEvVE8bqUGAXr5LGv_JoIr8sMLPHgarPKJwOyl5oP7hf9v0-plaUQex4qq_eLknOAlAwbWehdulrINuFgebmlAvlIjgESEfoWx-TitUDqtfxMbBOG8QIqRfEHXw4QLqL87gTg75jzVNtZwsC5N-xUH_Td7OEIHNArE8jLQlzkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چلسی که بوی قهرمانی لیگ‌برتر به مشامش خورده
👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/104642" target="_blank">📅 15:40 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104641">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
▶️
❗️
صحبت کنایه‌آمیز و جالب امیرمحمد زند درباره‌ وضعیت فوق‌العاده فاجعه‌بار مملکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/104641" target="_blank">📅 15:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104640">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61023bc5f8.mp4?token=ohEofCDgaVck4c6B0abxnGBBpHj7Av9y6a6k96ItKkZyk59Upt96M5JHvz1JAJMm5E5DTtZBZ6ljnLF2EnKQg70wcvF7Qf-OoSa5Qd1eWQHfJK98TXxgG2CnAo6XdDhHsza0KrKY5aE-aCzfY5FI5nZFc8Bb18E0xdadsg2XiglTr5jzkpMJWm74UuNzqtNvPkzHnvxBRbH1ItEwlibBgdZL4M7pDWB3QAdk_koqqC_3a99HiWB09CtWxYmP72E9jjpnH35Ia6iJOll4wPDxRqVGfldNXyQYhGR-RTaRTZQ3ywH7QhiJ2BALV0hYRaw9nshRn9dzQ1qA1JItjya1OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61023bc5f8.mp4?token=ohEofCDgaVck4c6B0abxnGBBpHj7Av9y6a6k96ItKkZyk59Upt96M5JHvz1JAJMm5E5DTtZBZ6ljnLF2EnKQg70wcvF7Qf-OoSa5Qd1eWQHfJK98TXxgG2CnAo6XdDhHsza0KrKY5aE-aCzfY5FI5nZFc8Bb18E0xdadsg2XiglTr5jzkpMJWm74UuNzqtNvPkzHnvxBRbH1ItEwlibBgdZL4M7pDWB3QAdk_koqqC_3a99HiWB09CtWxYmP72E9jjpnH35Ia6iJOll4wPDxRqVGfldNXyQYhGR-RTaRTZQ3ywH7QhiJ2BALV0hYRaw9nshRn9dzQ1qA1JItjya1OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک خبرنگار اینفانتینو را گیر انداخت و مستقیم از او پرسید:
«به فوتبال خیانت کردی؟ چرا استعفا نمی‌دی؟»
اینفانتینو اما هیچ جوابی به سؤال‌ها نداد؛ فقط نگاهی به خبرنگار انداخت و گفت:
«چه مدل مویی! آرایشگاه می‌بینمت.»
وقتی جواب سؤال‌ها رو نداری، حداقل درباره مدل مو حرف بزن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/104640" target="_blank">📅 14:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104639">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fizbhcWCadJ_RjdJ_dforNIfPxsNlP-YzR7879al39DeYquC_8n6ZiHpbHaKpwME_kgLUcFjbQQeAGg8NyhqZrWnluYmlk7AhSj0j6JYjKmfi59wJ6epRZ7vBB_s1o4vKS16ZZ9SypcRJg1onV1mIv2d13Dlew4QnI2rc5bsjmFQHEoj4E6Xq-WrcspYWoLn-TIWvWBgHkp7WI2eSNDBGzgLgF8vvrVfmHCyR6Zu-8gslF4ZjWhW3x1cxo7oZgyjE5j-KfJgbXKxesNtPB3p6LHiFTgKUtOZLXBFw2Jx2mPNweQN1U0Y5aiexDdu-Sayqjai7mT9Df_PpbpV6sIvcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
اسطوره آرتتا چیز ببخشید تارتار دیشب گفت که بازی دادن به جوونا تاوان داره. حالا عکسو باز کنید ببینید سن بازیکنان ترکیب اصلی دیشب پرسپولیس چند بوده
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104639" target="_blank">📅 14:19 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104638">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dauExanztqhG34kye-0EwvAM7TqB3n0xwf7sJQzdsbFB1-PeatDxkAgBcFzQ41h4Q7wMsmKQHUEyLxO9adWpug04EJK1c3y387GOY_SHbI-ZzLpDS_pyWTpXWQX__qV4jfLSFAIKfH_P-Q_UL188GzDYzhKIaNpYtJeVXFi9OVPTYgBR15s9WEjxo7Q5BTeoYUwHaKdtyQ0opU9LuiQcSBwlEe-9r1qveHmIF9ox9JhZ9-L7pViLATdfgysOulN1IqTFvLtjhKWyoFb_UnrgjDYEUOmJ2zgE9E1ZtM3UhPVZpL7qnYNpLCnFn7QNkBHuG6FBUsvtQeD4iBMfU6p64g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
منتخب هفته‌دوم لالیگا؛ پنج بازیکن از بارسا
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/104638" target="_blank">📅 14:13 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104637">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f029f12cc.mp4?token=vlMUaP0B_L0JUIU5NQkujQQ9c9CS2sUpWwdPKaVdUwsQOn7b5XOVFOYCjsl6ZILgbzzD10FOU1T67TvoZX7ZdWVJ7MOysQJQa8Dezxk0O5HkmkbVNkW7LY2ZsGirYnibbB_W7N-wSNAhghGS0YKDBB4YoCe7pYO7TQfCKQyDvEwKzKzSBg_vux0zG8K9flXFJoBbWvm5c43-ZVT6RBnY8VdCNtvR8JiVdQs5wRzBy6ZJG0PVihZGc50s4wGYEk0Kh5ZfxrmTrf6uvEhnwx7bO40ME0yhv6TJ0lziovSUw2T1T-tbqG7NcQ2AD5Jr_2uVmobaQpOmaIkvrlmLiqId4APrAvFcfdA36v9I6pMSm4fr_tx-Tp9TSV31nNea4YFdAj0_cfrujTqVY5zjCFvDMOlWe2YRPEcVJhulu67a_a_dlFzsGWK4U-9Yc-wBUaUSdqCDX54GsfOINDYuEiMcGPd9T5q38T4U_QxwqY52-20UvQLEzBRLyWDKKlE6iZ1R_NcuOox57KrlTlwPHe90oxJ79r8dhx0EGCwiH7oabsnM7Fa1FWByRz8wnDSLYIt0Jvz3RPMLNJ4QUKHZBYp2D8vXumemWopJlV6jkzhiCQ2WJQ_e1CNZKI_L1GrOB5YGlAY0uE8F_t3VQU8mK-cJTaqhSgL9UMan1Gw0OyvUuQk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f029f12cc.mp4?token=vlMUaP0B_L0JUIU5NQkujQQ9c9CS2sUpWwdPKaVdUwsQOn7b5XOVFOYCjsl6ZILgbzzD10FOU1T67TvoZX7ZdWVJ7MOysQJQa8Dezxk0O5HkmkbVNkW7LY2ZsGirYnibbB_W7N-wSNAhghGS0YKDBB4YoCe7pYO7TQfCKQyDvEwKzKzSBg_vux0zG8K9flXFJoBbWvm5c43-ZVT6RBnY8VdCNtvR8JiVdQs5wRzBy6ZJG0PVihZGc50s4wGYEk0Kh5ZfxrmTrf6uvEhnwx7bO40ME0yhv6TJ0lziovSUw2T1T-tbqG7NcQ2AD5Jr_2uVmobaQpOmaIkvrlmLiqId4APrAvFcfdA36v9I6pMSm4fr_tx-Tp9TSV31nNea4YFdAj0_cfrujTqVY5zjCFvDMOlWe2YRPEcVJhulu67a_a_dlFzsGWK4U-9Yc-wBUaUSdqCDX54GsfOINDYuEiMcGPd9T5q38T4U_QxwqY52-20UvQLEzBRLyWDKKlE6iZ1R_NcuOox57KrlTlwPHe90oxJ79r8dhx0EGCwiH7oabsnM7Fa1FWByRz8wnDSLYIt0Jvz3RPMLNJ4QUKHZBYp2D8vXumemWopJlV6jkzhiCQ2WJQ_e1CNZKI_L1GrOB5YGlAY0uE8F_t3VQU8mK-cJTaqhSgL9UMan1Gw0OyvUuQk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
یه پسر حدودا ۲۲ ۲۳ ساله با گل رفته بود ورزشگاه رامین رضاییان رو ببینه، رامین پیداش نشد و ایشون هم نشست یه گوشه گریه کرد:)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/104637" target="_blank">📅 13:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-104636">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c97e761449.mp4?token=LUsQVwTDCap31Cdfgzte0W1DVDjFrBax9MjSnTsSbYDco4x8Lays3yCSpV2movLCMcWht44Fyo4N8h8d0iFlso1OOgJQtwS7BbPkPtzRa68Z5LMygdTIewXjm7fiqlZqtWwTElUFIzoaZxiimjg-Fajn7ivjcuqUbQz_wj5u0r0I2yUedjIHez8raT0KiBHKBzo9toZ0qt4FFhbI3a0a_X2FbEBY8IQs0WRKbiNUlFEz0xj3lLL_6eDMtgojNSqRevQNv3O7u56WjBHchD_tfFdjErc3BV8srAlArIqcK1nLfA8NbzXb9Mcf8VAX6PKfa3thpVwTrhfw7QdB8m36eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c97e761449.mp4?token=LUsQVwTDCap31Cdfgzte0W1DVDjFrBax9MjSnTsSbYDco4x8Lays3yCSpV2movLCMcWht44Fyo4N8h8d0iFlso1OOgJQtwS7BbPkPtzRa68Z5LMygdTIewXjm7fiqlZqtWwTElUFIzoaZxiimjg-Fajn7ivjcuqUbQz_wj5u0r0I2yUedjIHez8raT0KiBHKBzo9toZ0qt4FFhbI3a0a_X2FbEBY8IQs0WRKbiNUlFEz0xj3lLL_6eDMtgojNSqRevQNv3O7u56WjBHchD_tfFdjErc3BV8srAlArIqcK1nLfA8NbzXb9Mcf8VAX6PKfa3thpVwTrhfw7QdB8m36eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حسن‌روشن: بنظرم تارتار امسال موفق نمیشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/104636" target="_blank">📅 13:35 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
