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
<img src="https://cdn4.telesco.pe/file/ELypT830Th04NhLzYxY2_JTJUZ9oB14yBLKNW6x3fLCrPmHjM69rIO7aoFKKsO9JOvI-omLXAtP2irP80tLDbYXzGomE6MX6OM035hLOl8XxsHKhTksb-DoZd9YwjN9mVf71ci9JgdoWA3YsZP6hFfzZjAAxanDnBMUMN1ZRpxYWNrdaIM6K3ZKwwoiZRRKni6z66ybKYUVdhhs5RijU6OdQTItBSv4tDlRn1ZMwu2yfF10Zw-mMunEaxglU4sJIE30dj2PUjLnkNSMded5L2q5ZY93dRq6-py3QOfEIEC2TN3pCg2q_dPXE_tfCPnkdIfAB6HhFfSGVxf3HFCLiTw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 994K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-31 03:41:54</div>
<hr>

<div class="tg-post" id="msg-148656">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">طلا و دلار فردا منفجر میشه
⁉️
همین حالا چک کنید
👇
https://t.me/+WWnSixAo9FA4MDZk
https://t.me/+WWnSixAo9FA4MDZk
تحلیل آتنا
:طلا و دلار از فردا با صعود شدید مواجه میشه
⚠️
‌‌</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/alonews/148656" target="_blank">📅 01:50 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148655">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AmeZn6m4Pqx_C2_UtFZEhWGosjQztEJKX5FEZs0bOnDRVf8l2RRns0NWutjXiSn2lxyK307mZ6hL8QydkBmQ9TUhvWmqv8pyZiDYe1zvJcEbJyJhYbmu-9K00hCIWx6BgIMHlEh05rTJOuSUk0SN3LJBW-_jO-EtB91sevzWL02RtWcDpqiIXox4Wi7ualhYQyKFJwVFC_N80vdToW8IJW75L7myKbck23vCybhsyNyWQiQ2LZ0XyUXVnDAB7qcEZYWt_aPqvMthdsqiQzMiOTlQviDdXrXmnYOR_ChJgUUN05xIjrMmmAREMgoV1lpL0nDv4ZZnB7qS3jkcxoko0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت 99 دلار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/alonews/148655" target="_blank">📅 01:49 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148654">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bff8dd60b7.mp4?token=UkNwLfb0l_EQUzxbRwMRVSCxc9b0sVKWmzhqxCQbmtY4dK1c4l-8nzr1JtKfTugXvNwVu_gI7CJ5ylgSwKpiZE0UE9TvWaQafxcagAY9qHm8JEjxm0CMNStBQW8RwxS1t0UOVcE9t2F9bKvK6VT6yCpZnkfLcgcwfJdgz87BLQ8M7i7sB-r_Cdcoiaz6PePqYO_r-S3Pd1besEJR-VqT9YmJjymSGtMIcrR5eT4c5Pf-b_IfAFvCxCpnfr-138UslJCKvAWiqKvWFBcLr6UKKMgbnXS_5SSIb_D_2K7RaoijrdPwmXYuNS02_cl13gctshlPmp28ed-xn8H8Jx0b_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bff8dd60b7.mp4?token=UkNwLfb0l_EQUzxbRwMRVSCxc9b0sVKWmzhqxCQbmtY4dK1c4l-8nzr1JtKfTugXvNwVu_gI7CJ5ylgSwKpiZE0UE9TvWaQafxcagAY9qHm8JEjxm0CMNStBQW8RwxS1t0UOVcE9t2F9bKvK6VT6yCpZnkfLcgcwfJdgz87BLQ8M7i7sB-r_Cdcoiaz6PePqYO_r-S3Pd1besEJR-VqT9YmJjymSGtMIcrR5eT4c5Pf-b_IfAFvCxCpnfr-138UslJCKvAWiqKvWFBcLr6UKKMgbnXS_5SSIb_D_2K7RaoijrdPwmXYuNS02_cl13gctshlPmp28ed-xn8H8Jx0b_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بسنت وزیر خزانه‌داری آمریکا: ما می‌دونیم پول‌ها و دارایی‌های شبکه حکومت ایران کجاست؛ حتی حساب‌های خارج از کشور و خونه‌های خیلی گرونشون رو هم شناسایی کردیم. می‌خوایم فشار اقتصادی رو شدیدتر کنیم، حساب‌ها و دارایی‌های مرتبط رو مسدود کنیم و سراغ شبکه‌های مالی سپاه هم بریم.
🔴
در مورد چین هم میگه با وجود اختلافات آمریکا و چین، سر موضوعاتی مثل جلوگیری از هسته‌ای شدن ایران و باز بودن تنگه هرمز نقاط مشترکی دارن.
🔴
یعنی پیام اصلیش اینه: «می‌دونیم پول و دارایی‌هاتون کجاست و می‌خوایم از نظر مالی بهتون فشار جدی وارد کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/148654" target="_blank">📅 01:41 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148653">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا:
با چین درباره ایران مذاکرات پشت‌پرده داشته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/148653" target="_blank">📅 01:34 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148652">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
هم اکنون قدرت‌نمایی جنگنده های ارتش بر فراز آسمان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/148652" target="_blank">📅 01:06 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148651">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ: از دست ایران بسیار عصبانی هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/148651" target="_blank">📅 01:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148650">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ: ایران سلاح هسته‌ای نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/148650" target="_blank">📅 01:03 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148649">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: ایران اوضاع بسیار بدی داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/148649" target="_blank">📅 01:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148648">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6810089eb9.mp4?token=TcdPoLoB90y8ihFJ0iDafGLKTx3iEfs-wGYI9Et2XUgfnCrS0xkL1-v3i7-CUkzuPMRFnbjA2Gs2ZWQVTE1yNUyqARwrlbWzDqVzI2nIHZtfeJiNVcVuH8WCHuArVkQpMuiZEJBsrwbUPUYS0PaV-6r9Ap9p_YUTxIV2CNZIQ8yyKyrZeZwwLODak_SZb8nB5JZOTk4Uof6rnUpDBft-bcEVp1jwkPJU0pywG3M3fKzwQ3dUb7wtuaTKRj6S479iDDg_SiUYKsT2fXBeincEeUZJBL0Xz9zscWynooSnjTJ-huNNmOlW1g8A48aXGoD5CocuMxsj7Fkc539h6ssUJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6810089eb9.mp4?token=TcdPoLoB90y8ihFJ0iDafGLKTx3iEfs-wGYI9Et2XUgfnCrS0xkL1-v3i7-CUkzuPMRFnbjA2Gs2ZWQVTE1yNUyqARwrlbWzDqVzI2nIHZtfeJiNVcVuH8WCHuArVkQpMuiZEJBsrwbUPUYS0PaV-6r9Ap9p_YUTxIV2CNZIQ8yyKyrZeZwwLODak_SZb8nB5JZOTk4Uof6rnUpDBft-bcEVp1jwkPJU0pywG3M3fKzwQ3dUb7wtuaTKRj6S479iDDg_SiUYKsT2fXBeincEeUZJBL0Xz9zscWynooSnjTJ-huNNmOlW1g8A48aXGoD5CocuMxsj7Fkc539h6ssUJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
«گفتند قرار است من را تحریم و بایکوت کنند، اما هیچ‌وقت این کار را نکردند.
🔴
به این همه پوشش رسانه‌ای الونیوز نگاه کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/148648" target="_blank">📅 01:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148647">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: امروز جلساتی درباره ایران برگزار خواهم کرد، و اوضاع به خوبی پیش نمی‌رود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/alonews/148647" target="_blank">📅 00:57 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148646">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iRDL3NuU_2BJVERvA-y1xGzvcYTQiH9QasbKy_wOSHPc_jPmmzcOc9csH9MnGnT8cS_KQhvhS8hL6z_CvolmhnUKYZdvY8RS_OGKrd50bVRkV_nisXSrewIi4zQlaBcIV7XmxoVcJhzwT2usdlD-_IY4KMi4BudJTDjNgcwDxaO0lIJFZYt6rL-RtcaMYd2upkoEm7ASl7PmW1_R7aqJcos9w7Si3oFddPHzf75CnXQ3muZbmpRWSjkQqLXj252BWez4kmY7ZiBOJZekLEpOoDnGY9OtrRJjWe0XA26X6t8mkIOVNy6im5Af75Bh-xEddXxv_tdUl9rEtEC1Wccjvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: از تاریخ ۲۱ سپتامبر تاکنون، ۱۱۰ فروند شناور در چارچوب محاصره تغییر مسیر داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/148646" target="_blank">📅 00:45 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148645">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوووووووووووووووووری</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/148645" target="_blank">📅 00:33 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148644">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
فوووووووووووووووووری</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/148644" target="_blank">📅 00:31 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148643">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‏
👈
کانال 12 عبری:
ارتش اسرائیل برای تشدید تنش‌ها با ایران در حال آماده‌سازی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/alonews/148643" target="_blank">📅 00:27 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148642">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pigq1IBqdXdaDaUwT190uCErtD8rFR_Kt50Uk_pBDw9ILRCiRfaP6MLeJPCS-t2XvUEGHwemFIG2cAwtrX36l2qwB64-CIFecKFMpAaKLGqhOF1C46AvOIpNwlCzy6yygxeB39xUS8e8S6Pbh4AYHWO9uvzPdwMSG6qvVRZbGmmGSV15egFGPPmaTF1I6PIfJw16tOHiT1n3lrCn7XuKnCxVUte9hExNd1J0JiL-9AhSKxKG3G6JQUMRuB6CC7MTcF5p11QutUo9p2-QYeTdLrf6rERhnTCLoSdlattqCP4lStE3sYpvEVCn-nh5fG4Wm_rQyJK9kaDJ5r3axn-OoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرکز امنیت دولت لهستان برای ساکنان چند منطقه در استان لوبلین، در نزدیکی مرز اوکراین، هشدار صادر کرد و درباره حمله هوایی روسیه به خاک اوکراین هشدار داد.
🔴
نیروهای هوایی لهستان نیز از ساکنان خواستند هوشیار باشند و منتظر اطلاعیه‌های بعدی بمانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/148642" target="_blank">📅 00:21 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148641">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgEx1LZWhneuAtMfbMHAFY091wBjtHaS-Yf85E_mm7mok_wSWRxPBstMqmQ5maQ_lJ-CkRuA3KIqgKhgjOr3VLLoazasXPs8QOXp5pBZTPbulf-H6QC9rnGdGIo7fsdIlxOqSnX2qGFeXP2JrNV8lpugSyFj-aWZnQ0v6Dn-QEbxYt6sonUQhDi4afTg4ic6mg3qHfL_VmpRVx71bCOHokGHqIhq4f626u3vs7jxt9zZM70WYEkqLbom4T3RmLxE-WvXwyeLRDD6ceBIsWHafp0h_QaRcmNEGadXEmCgCnwNkc7yZH1byAePudwkss9Ym3Cn5woh_kr3sZyXjDqYTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه نگار اماراتی: اتفاقی عظیم در راه است؛ حرکتی تاریخی و بی‌سابقه.
🔴
آماده باشید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/148641" target="_blank">📅 00:02 · 31 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148640">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
نخست وزیر عراق در گفت‌وگو با نیویورک تایمز: گروه‌های مسلح عراقی، تحویل سلاح‌های خود را آغاز خواهند کرد و انتظار می‌رود این روند تا 30 ژوئن 2027 به پایان برسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/148640" target="_blank">📅 23:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148639">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
پراندلی، تحلیلگر بازار جهانی: ترامپ با یه مصاحبه و جمله احتمال توافق، قیمت نفت رو از ۱۰۷ به ۹۷ دلار رسوند. عربستان هم به دنبال بازگشایی خط لوله شرق-غربه و با این تفاسیر دیگه نیازی به تنگه هرمز نخواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/148639" target="_blank">📅 23:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148638">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
عراقچی برای شرکت در مجمع عمومی سازمان ملل وارد نیویورک شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/148638" target="_blank">📅 23:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148637">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28b889a0ca.mp4?token=tsLpL5Nt26GPpBeqt9npygJgBxecFONR1VnCVz6qT1KX4hcKA_5U4-ZogT3Ycme13cOjbrsUFFZeuTHDXsPFv1CaeXF4FAZhD3i_q4sYkqckvu6C2mwiLyr89fFltVseXFvbTd3ntQJx-juvU4rLW_JtT4jas7xMZvPvRGU-o7ZlapbtvQf23C0OzKOhr0KDwsDkjuA0-NxDgkF-81UAZL3O-KNQ0lPV8L9GYQPr04G8hvRFr7Gtua-0lCTrTzfYMAEeXk6OwNR1DBeCYHiCmgMzMEwIguM6dzcJJk36yrxdfXyHvfvOZWkRVucxLOw-qA777Slvl9FdrAu33vUJOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28b889a0ca.mp4?token=tsLpL5Nt26GPpBeqt9npygJgBxecFONR1VnCVz6qT1KX4hcKA_5U4-ZogT3Ycme13cOjbrsUFFZeuTHDXsPFv1CaeXF4FAZhD3i_q4sYkqckvu6C2mwiLyr89fFltVseXFvbTd3ntQJx-juvU4rLW_JtT4jas7xMZvPvRGU-o7ZlapbtvQf23C0OzKOhr0KDwsDkjuA0-NxDgkF-81UAZL3O-KNQ0lPV8L9GYQPr04G8hvRFr7Gtua-0lCTrTzfYMAEeXk6OwNR1DBeCYHiCmgMzMEwIguM6dzcJJk36yrxdfXyHvfvOZWkRVucxLOw-qA777Slvl9FdrAu33vUJOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عربستان در مرز با عراق بالون جاسوسی مستقر کرد
‏
🔴
گارد مرزی عربستان اقدام به نصب و به پرواز درآوردن یک بالون ویژه رصد و جاسوسی در نزدیکی مرزهای عراق کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/148637" target="_blank">📅 23:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148636">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efIi_5rIKRg4mP8As24fTsiN7ur82t_miLJhC38x5H0VBv8s47-H6xZRN39LhLoV-v3sJLkv2t3jXo91aa4zXXLP-2HflkFV64goBnofsoC8MF7xTzwesDbawOb0B-svBvElfVOattBgiY4cWM3y9b42H3yhwPbdfOOTw1rmi7CcLqKKUNYG9yz7WqeFovBD8YcjDbtov26fGdEy0033u7axMp65PRcWPH0e7U0bIE4ZzpYEWyyjCHaEf-uNtdnhJaP5qWsVIgWN0cayptSq-oheoS4e9DTOlYnfjIvyRjTCR5m9y8269O2spsloL1Xds6CL8nGTo7EsCv9JjZo1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : در حال حاضر که در شهر نیویورک هستم، در راه یکی از مکان‌های مورد علاقه من در جهان، یعنی کاخ گریسی (Gracie Mansion) هستم. من سال‌ها در آنجا وقت گذرانده‌ام، با شهردارهای عالی، شهردارهای متوسط و شهردارهای نامناسب.
🔴
دیدن اینکه اکنون چه شکلی شده، جالب خواهد بود. من توسط شهردار مامدانی دعوت شده‌ام. مشتاقانه منتظر آن هستم. بیایید دوباره شهر نیویورک را عالی کنیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/148636" target="_blank">📅 23:30 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148635">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🟡
طلای ۱۸ عیار: 23,707,200  تومان
🔻
حباب طلا ۱۸ عیار: -1.78% ______________________
🟡
طلای دست دوم: 23,391,128  تومان
🟡
تتر: 228,800  تومان
🟡
یورو: 265,010  تومان
🟡
هر گرم نقره: 511,230  تومان
🟡
سکه بهار آزادی: 230,130,000  تومان
🟡
سکه امامی: 233,980,000  تومان
🟡
نیم…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/148635" target="_blank">📅 23:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148634">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5YWaaQ-vNZLi4MRssbChAp-vypSM57q_eNs8FQA_K7d_dac3KucZKxQdghNG9zYh4ryF8WbKEVgAMgPnvPY-JZWMwZveNtOz0SU5Gb3Fof4YTUV0050kWb7rmETrmHFjO-76u7B6wGrGQLbfgFGeNb_MSQOLgp6cKv_ITcxhyGE3hQTxXkifBeDQDFjMHhWsD-nVvRISEvizF_8Xwf4Z37dOFARuykgbiSnZM2gIVsSKPXKWjOpM_uaF6mqa64NWj9OF20Ow0ytansnR1MY5VEy3snC_SMVbBRZEknXj-csfYZejVrTBwgMahW_rrNxUzxcKd6WDIId2pzv1_VpNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی خبرنگار نزدیک به حکومت: ونس اخیرا در جلسه‌ای گفته که وضعیت ترامپ در انتخابات آتی آمریکا خوب نیست؛ باید کاری کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/148634" target="_blank">📅 23:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148633">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCST-GlRhAML9n9LbRhSrg7nHlZbdqbwC4kPoKNkm5xSETrP0_xMERp8XtbYfRYR4DS0dhYnLeJgb9sRt4Fu3LlfbNa0h1Y5nC3vzYKz4fCRPF0pJOAiMYiG51vAyx_iU0VSI9lT2gJT3XveCvtTDp1ceIl06EahYeY-U8xovOwzQQtCofgvRc-h629n1EaXvGHMwyvSKewH37orL5d-XWs8N-mBUgk7vkKCCb8NmHw4bfW-zBVsxA8Lk2pmKXCKHTxd3yh6RqDAkaxvuoHxK1oLkThgw8RRAS6I-9NlEp8Oq-5pzFZZ27FTrY1fodxuzm_52TdIEK9B6Ay4hesynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همانطور که انتظار می‌رفت، شبکه خبری جعلی CNN، نشریه Politico (که باید ۸ میلیون دلار کمک مالی که دولت آمریکا برای زنده ماندن آن‌ها پرداخت کرده است را پس بدهد!) و MSNOW (که قبلاً با نام MSDNC شناخته می‌شد)، شکایت کرده‌اند تا به کاخ سفید و به من، رئیس جمهورتان، دسترسی پیدا کنند.
🔴
آن‌ها یک قاضی بسیار خوب (از نظر خودشان) انتخاب کرده‌اند، مردی که در گذشته به نفع جیم آکوستا حکم صادر کرد، که اکنون به نظر می‌رسد از سطح زمین ناپدید شده است. نام این قاضی، تیم کلی است، و متاسفانه، او توسط "ترامپ" منصوب شده است
🔴
به عبارت دیگر، تقریباً بدون شک و، همانطور که معمول است، ما به این حکم اعتراض خواهیم کرد، زیرا رسانه‌های خبری جعلی و نشریاتی که فقط مطالب منفی منتشر می‌کنند و با انتشار داستان‌های دروغین و افتراآمیز، امنیت ملی ما را به خطر می‌اندازند، نباید به مهم‌ترین دفتر در سراسر جهان، یعنی دفتر بیضی (Oval Office)، دسترسی داشته باشند. این دفتر باید با احترام، وقار و منزلت رفتار شود، نه اینکه توسط افراد بی‌ارزش و درجه سه، آلوده شود، افرادی که عمداً مطالب را تحریف، دستکاری و تخریب می‌کنند.
🔴
تقریباً هر داستانی که درباره من یا هر چیزی که به من مربوط می‌شود، منفی، نادرست و در بسیاری از موارد، خطرناک برای کشور ما است. مهم نیست که دستاوردهای من چقدر بزرگ باشند، آن‌ها آن‌ها را بی‌اهمیت جلوه می‌دهند و تحقیر می‌کنند.
🔴
حقیقت این است که من در هفت ایالت کلیدی، در رای عمومی، در کالج انتخاباتی (۳۱۲ به ۲۲۶) و در اکثر شهرستان‌های آمریکا با ۸۶ درصد آرا پیروز شدم، و با این وجود، گزارش می‌شود که ۹۴ درصد تبلیغات درباره من منفی است. با وجود چنین رسانه‌های کج‌رو و فاسد، چگونه من می‌توانستم با این اختلاف فاحش پیروز شوم؟ زیرا رسانه‌ها هیچ اعتبار ندارند، و این یک چیز بسیار بد برای کشور ما است. چرا من باید به چنین افرادی "دسترسی" بدهم؟ شاید قاضی کلی بتواند این موضوع را توضیح دهد.
🔴
در هر صورت، من وظیفه دارم برای موفقیت و امنیت کشورمان مبارزه کنم. اخبار جعلی یک تهدید برای دموکراسی است، و من هر کاری را که لازم باشد انجام خواهم داد تا اطمینان حاصل کنم که ایالات متحده آمریکا شکوفا شود. "آمریکا را دوباره بزرگ کنیم!
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/148633" target="_blank">📅 23:22 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148632">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2AysXbHBtD_ukB1VKCN8XzCT2iUJx3bi2irf87Mp5A5v4om0HOloPSzZl6ynKMwcvJr4kjO8OU2THifj5yRBgvtL2oy5RIrudqrdfp-iooGvt-1G-oVg-bgkaM_Q7vXGT8mAyxLc5CiJtjl7gfAv1bZrfpiooD_zqG4AvG8Wp1zFiTN0QpsUFQWYxPEvSF3lftiji0xvptfm9lf1qMvnD3rbdxohUJeDoBm0cOAl8dIb3na7U2oTjrDoktSMezPldM4z2EUYC5Rm6dtfRuxH1pAiXqX8PBNVeMvV05kjigDyfHFH7En3DRzp0dYLn_Zd_jI-cjtPp2tVJBfX7CVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/148632" target="_blank">📅 23:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148631">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزیر خارجه چین راجب ایران: چین فقط اقداماتی رو انجام میده که به صلح کمک کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/148631" target="_blank">📅 23:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148630">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
تیراندازی در لس آنجلس از پشت بام به سمت مردم
🔴
یک مظنون پس از تیراندازی به سمت مردم از پشت بام ساختمانی در جنوب لس آنجلس، در ایالت کالیفرنیا در کشور آمریکا  توسط پلیس بازداشت شد.
🔴
نیروهای امدادی سه مصدوم را به بیمارستان انتقال دادند.
🔴
پلیس چندین خیابان اطراف منطقه را بسته است و از ساکنان خواست از این منطقه دوری کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/148630" target="_blank">📅 23:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3PJa-WUnKWGa4rS34AUBLWuGPwAJOkRjMxziMOUpoRZYw5C9mwtNZxTPHg-27QzpWkG8KANeoDIX2KoXCtUozSbAG6RUWN4tyxxVMIOjrc7RZ63sVEIUMpgx9hRFC6IpCxebCc-NK7Cb_9IblDFFtipD7CDyfpqHoUiNGxgTjK05rE4qnyW7vkrZY9dZiRlBdVE8m023qh7nrbRDywZcoQi2a3IpKQWfDXXxHM3T2c1Q_1XeX0-fwnUYdKzybekX0ncpUI08drgZBMY4zkDbFZPxe3Rt4Ob79QOJNPFELihMahs6cG_gyf4IjKOr9F3Va8VD57Y7_UDmF8BVoE87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعتراف یک زن ۲۷ ساله مشهدی به قتل شوهرش:
بهم محبت نمیکرد منم با همکاری دوست پسرم کشتمش و تو حاشیه روستا جسدشو مخفی کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148629" target="_blank">📅 23:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148627">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s3v73Dir1PZsrgv4kz3c-seHkUPf-z3pM2Dvi0auFn4CC_fYSscdBkkDsTokV6lId4uJ2kQUvojxHwJZDdgTqr49Y2qkxtnqAfCMDVSkVMxce4L_uSFfZ096F6M0hKEka0ALRVSVP0Hn-LbSN3KXuOod6d63iTYIU5olv7cjOTsXDGIIPNJVIrXTTeUgdFzSrGYhpQXTIuFoRGpebe97PEo4iCiLK1lxwk_Gg4_nYb22vH0ScdH5psXzbwLiKkvClCLalWy6461K2XXRFa_OPZZ7UW1oFPGQMcmScvlXerTd9yn_fHY3JhlU_BrOzhkeVk0Kyq4nI7ot122mlGzq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3KO-PM5ZSWCqXReUplO807E79g1mUdypZ3wzsyP7h-lRC3Lbxai2XhoUQiXPz3-OqF98Pgk3dpxiwO4vo52Gc_x6OdFiL4Fu-SJhgS7-1aO70fufYj9o0xHoWyAYWaauR91I8TtWw_NqT7WIzNtnak2-B1jD8mZ0l7ce48xa8Os63xK5Tf3idrbS9S9oZFZwIKhQlnYcUXh6opmUvS1SLwI2LqUH1eIcnQojHlTEbX7JA6XqLSN1JHcmanLVw7uccCjzmbqjeACKneLStoW-uFbhDYg8niL1Pkx3jCcSyO4NGzZ9Lrc9JgyhqRu-gTsEjqbiEZRh53-WqUcXNXhfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هواپیماهای جنگی اسرائیل دقایقی پیش حملاتی را علیه مناطق شرقی شهر غزه انجام دادند
🔴
این اقدام پس از آن صورت گرفت که یک خودروی مهندسی متعلق به نیروهای دفاعی اسرائیل در شمال غزه مورد اصابت یک دستگاه انفجاری قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148627" target="_blank">📅 22:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148626">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
گفت‌وگوی وزرای خارجه چین و آلمان درباره وضعیت ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/148626" target="_blank">📅 22:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148625">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/525f2c026e.mp4?token=Z0xL9UjmWq0mDRRe_aN3j0LWOrIWXlEgTKMjC_t0AqbKr4fznqIKVAro5cDA7DTr9ZF6nHkwzrdROSQ4cUg9-cmKXPuTbxEed75Vj5SN8CWWN0GzAtx65Ioo1tKwuRcndLact2jF6SWpVTTmx8Jomn29S4lXoMLogAT61PG8ztvGA5o3c5asEsGjAZNvHwQFIiEEvF6nRrrkWtK6fuO5ugV5jvVt3f7Eg5Q1WyrZB4M0tWsE38vutpGFvmN5WvdMm5dSrScShFF7D6lg-Z5Z5mwwsYqrdeiAsdXsZuu4Pr05vmoTuj7lBLwE84-bXmqVBa1NvwUr-HraFMw3sNQu8g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/525f2c026e.mp4?token=Z0xL9UjmWq0mDRRe_aN3j0LWOrIWXlEgTKMjC_t0AqbKr4fznqIKVAro5cDA7DTr9ZF6nHkwzrdROSQ4cUg9-cmKXPuTbxEed75Vj5SN8CWWN0GzAtx65Ioo1tKwuRcndLact2jF6SWpVTTmx8Jomn29S4lXoMLogAT61PG8ztvGA5o3c5asEsGjAZNvHwQFIiEEvF6nRrrkWtK6fuO5ugV5jvVt3f7Eg5Q1WyrZB4M0tWsE38vutpGFvmN5WvdMm5dSrScShFF7D6lg-Z5Z5mwwsYqrdeiAsdXsZuu4Pr05vmoTuj7lBLwE84-bXmqVBa1NvwUr-HraFMw3sNQu8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
استقرار پدافند هوایی روسیه وسط بزرگراه رو دریابید
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/148625" target="_blank">📅 22:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148624">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bafb25ee5e.mp4?token=UZ4dcaMacyJEziCPxpDSTH68eWoquSubM6cz7fzcZTUyEpcy4eYVBO5M8nwX6BF44wZHCzcG9G_nndtyTsmx-t-knG4bpgT_GgKOW02018VY7K0MrIJcsIyY7Mjf_yo3jviyjc31w5GRXD1aRZiOjlLGdM4lnh3sOJLRhphnWOW8qOJD7aifOLuOONoWX3Hj_ERZuM5WgYUW04kBlYHbcRT5K8Bl_0osAyt6haFlaEg8BvTSzIO_NgeaJd0WeqJsv6ecrAuZgjlAsGr8EqoaNseKuhT5sC8bwzKeZGft_4wtIYMW3g-eALD769qgUnA8zVR3vrdX0_WkKuw42FK_Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bafb25ee5e.mp4?token=UZ4dcaMacyJEziCPxpDSTH68eWoquSubM6cz7fzcZTUyEpcy4eYVBO5M8nwX6BF44wZHCzcG9G_nndtyTsmx-t-knG4bpgT_GgKOW02018VY7K0MrIJcsIyY7Mjf_yo3jviyjc31w5GRXD1aRZiOjlLGdM4lnh3sOJLRhphnWOW8qOJD7aifOLuOONoWX3Hj_ERZuM5WgYUW04kBlYHbcRT5K8Bl_0osAyt6haFlaEg8BvTSzIO_NgeaJd0WeqJsv6ecrAuZgjlAsGr8EqoaNseKuhT5sC8bwzKeZGft_4wtIYMW3g-eALD769qgUnA8zVR3vrdX0_WkKuw42FK_Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو جدید استاد گودرزی در راه پاسارگاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/148624" target="_blank">📅 22:36 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148623">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">💢
قیمت بیتکوین ترکید</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/148623" target="_blank">📅 22:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148622">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DM8P7N2mb3IHEmccnvHky3LhGPDaA_XdOy1QuMU6UYX8-SVmvUmyr2_olN1sDp25wHXdMQVfdsMbhOtOtQr-odfg5DtfADHrZ5H0umxRq5pZk5O5IfaT5mBVvk2aHYBvtfPP-X0Yxx_Msd6Zh3Binxa6Az0STImfPD5QTetTzn8EcbrvLIrOgbhTxQxJTcIew6pkm-guaaaaYWz5MSjcDyNp59SXN4FdEXxc3CA4ZVNLxI2SnbibS3WQzN_vZEfznaMhl1ovswEaaM9MiPX0RYc6-bsxKHBoaFqHRoujmZ3vAQIhuJuWKGGrvNL24BpveWr-OkX-eJt6MGoMCNJGxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با اعلام ستاد امر به معروف و نهی از منکر استان تهران، ورود مایعات(الکل تو قوطی آبمیوه مثلا) به سالن کنسرت ها ممنوع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/148622" target="_blank">📅 22:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148621">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rq4J-oJw84_esCTxJmFAs15BY84TIOdcrBulWqk3IZYWSAoF5ab3bjsxEYjNFcTJxFd09I6ZS5OUdcQ8X9fBXgRDWSuxfsBa0nOm_C8yvI1oBl30FobF3hATDfo62GftXESjeblC-uKjPLrmPxgHFRh_skqg8COGCH4ROTBTD7NrviEPS4RGNMMOoLIkaDX682sGpBUrMoPDsN4mVN3zWbHDEJ03fyQZgI8Dn2mLmk0SS7UsZfiRLrh9d3uNd9mE81YFesmWol3fTcFM964QYDjm1hu1quvRxtyRe-KhpYJMUV57fGt9TBg7peuSF1jfNqteNHZnzGGJxdxF_e5S5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید کاخ سفید: اتفاقی در راه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/148621" target="_blank">📅 22:21 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148620">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه قطر: در حال حاضر بی‌اعتمادی بزرگی میان واشنگتن و تهران وجود دارد و هر یک از آن‌ها منتظر تسلیم دیگری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/148620" target="_blank">📅 22:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148619">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rMNUMGadA_d82G8jhIvu1PRCON-bqy-ekFI3p-oZanehXvBdjGg_8jc0yeeb1sNRTAD8uJrKScu2YjTm93Lc1sJS1PkRZwKtTwDkKiETekQQu4iQeOEAbCx-4CC4oReOJyWsWEcUiyA2FI3WHN2RftTPS60_js8LR16jWayRXJNoQlyld3A8DXtX7ROLXekaX6oTyEcK9wGEGAOj6ygXishFYZYXpIz-TxL3kgcn9c97Q55DRoiLaNTFT4YxmStS7v3e4sNKXrOEXOnFkw3UEBHYYoBz-tgmjffp0tQq1nv_K_5-6i90vG7puiHaXXgj2ro3tu9XYHeIT2UtGm5llw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
استاد گودرزی: هموطن راه در جهان یکیست و آن راه راستیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/148619" target="_blank">📅 22:11 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148618">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترکیش ایرلاین اعلام کرد پرواز های ایران و ترکیه خود را دست کم تا پایان سال متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/148618" target="_blank">📅 22:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148617">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/394c3bbc47.mp4?token=P2sETAf37MtAPHX66-kAyy711wQjfM1jptcx6eHvEHW5TxtzVyZqr3vMYjFvY3Mh4_Qe3lduqExmx0Vn-iu-EsvUuCNfiBSXPKyVmGkITsOP9EflLIt3XFViIw8l9ax86zRks3eg3WgD3YDtU_bk0SrCICfjufK5JM9bQbQeDZIFVJ4M7jCvdj5C2QbECU6l51w09UHJZA_aQ2BktpnItlpg_JblK9Ys-AjXSgaJn0MQNziaU2vcrcqKy1gyrN8DCKwjoLc8NKcKZK2nDDKRGMVVSUAoOZ-YLMHELlVSzjnsrccKBfxv3whL95S4ZKkTpC__UaOV0CdE_eVAi8vKwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/394c3bbc47.mp4?token=P2sETAf37MtAPHX66-kAyy711wQjfM1jptcx6eHvEHW5TxtzVyZqr3vMYjFvY3Mh4_Qe3lduqExmx0Vn-iu-EsvUuCNfiBSXPKyVmGkITsOP9EflLIt3XFViIw8l9ax86zRks3eg3WgD3YDtU_bk0SrCICfjufK5JM9bQbQeDZIFVJ4M7jCvdj5C2QbECU6l51w09UHJZA_aQ2BktpnItlpg_JblK9Ys-AjXSgaJn0MQNziaU2vcrcqKy1gyrN8DCKwjoLc8NKcKZK2nDDKRGMVVSUAoOZ-YLMHELlVSzjnsrccKBfxv3whL95S4ZKkTpC__UaOV0CdE_eVAi8vKwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
متقی، استاد دانشگاه: آمریکا طی ۴۵ روز آینده جنگ بعدی با ایران را آغاز خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/148617" target="_blank">📅 22:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148616">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
روزنامه همشهری : به دلیل شرایط جنگی رژه نیروهای مسلح امسال برگزار نمیشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/148616" target="_blank">📅 21:57 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148615">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
اولین ربات تحلیل اقتصادی رایگان
‼️
🔴
اگه نمیدونی کجا سرمایه‌ گذاری کنی یه سر به اینجا بزن
👇
@Sygnl_bot
@Sygnl_bot</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/148615" target="_blank">📅 21:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148614">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0c34f5f8.mp4?token=KgETzJ5X3F8LHUQyMNTEgMwMHDyjZQQgr9Q2iESWiUfAUyk0oHanja25RhvThd6ZvbFJCjEzRXHg3vOvQOtPKFFlN4mNKEAOseiOu4SHNWBRHMf4Y-adLgow2OkRxFH4WOByAYbUQeP_L72_CLrywzZr0g0Jbi2_tpTYOGJJZWsI7t3zmK14YdJCbZE-aF1thotiogCe8dmGqfBU0A-hY0TpVyW-0VvIEBib69Xz2WcaDm5EHcnapCcvqywY7nFXs_R_T1d-_6XitxYKGEO_4yAC0lfrmravjMRENxwtXLA4nhQhMha1zh0D5OSZps1NuII8SV1JaP9Md9uP-sDRL5Ut0KpeQwAugp14UR0I9OKYHUwXcp0dA3bS-YFfHf_ed09bDT4MgASmXWEkMSCfMpwAp7nH9mYyV_j2bseiyfjtpc99HYHYMPVtdxKK4oktJmySddj2D5lCgJKnUZ0IlDr2JLaRQuWMOfWezmrDYDbPnK6rS11A-7buDcVnAQCcNqIzjS_1nS44rpJEk5sH0WnrrlJeEcQhPDm9KHxEEO3Xbo5ssxhw1JFNWIjFwvOKETO7uw8AAg12O1ULcYu0gOoYBygV-tyJsoEPcjEMw5QHPdl7_jAiMDiHJFEuPXU5sOnKB4EVMjrdFMWfkceoTo4BBPOnsT_pqYcPkPua71M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0c34f5f8.mp4?token=KgETzJ5X3F8LHUQyMNTEgMwMHDyjZQQgr9Q2iESWiUfAUyk0oHanja25RhvThd6ZvbFJCjEzRXHg3vOvQOtPKFFlN4mNKEAOseiOu4SHNWBRHMf4Y-adLgow2OkRxFH4WOByAYbUQeP_L72_CLrywzZr0g0Jbi2_tpTYOGJJZWsI7t3zmK14YdJCbZE-aF1thotiogCe8dmGqfBU0A-hY0TpVyW-0VvIEBib69Xz2WcaDm5EHcnapCcvqywY7nFXs_R_T1d-_6XitxYKGEO_4yAC0lfrmravjMRENxwtXLA4nhQhMha1zh0D5OSZps1NuII8SV1JaP9Md9uP-sDRL5Ut0KpeQwAugp14UR0I9OKYHUwXcp0dA3bS-YFfHf_ed09bDT4MgASmXWEkMSCfMpwAp7nH9mYyV_j2bseiyfjtpc99HYHYMPVtdxKK4oktJmySddj2D5lCgJKnUZ0IlDr2JLaRQuWMOfWezmrDYDbPnK6rS11A-7buDcVnAQCcNqIzjS_1nS44rpJEk5sH0WnrrlJeEcQhPDm9KHxEEO3Xbo5ssxhw1JFNWIjFwvOKETO7uw8AAg12O1ULcYu0gOoYBygV-tyJsoEPcjEMw5QHPdl7_jAiMDiHJFEuPXU5sOnKB4EVMjrdFMWfkceoTo4BBPOnsT_pqYcPkPua71M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ برای اولین بار از طریق هلیکوپتر "مترین وان" از محوطه جنوبی کاخ سفید به سمت مقصد خود عزیمت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/148614" target="_blank">📅 21:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148613">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
سپاه: آمریکا و اسرائیل دیر یا زود باید به خروج از منطقه تن بدهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/alonews/148613" target="_blank">📅 21:41 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148612">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
حمله هوایی سعودی‌ها به الجوف یمن
🔴
جنگنده‌های سعودی در جدیدترین حملات خود، شهرستان «الحزم» در استان الجوف را هدف حمله هوایی قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/148612" target="_blank">📅 21:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148611">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
بلومبرگ: ایران به یک محموله دیگر LNG قطر برای عبور به پاکستان مجوز داد
🔴
بلومبرگ گزارش داده پاکستان مجوز عبور یک محموله دیگر گاز طبیعی مایع‌شده قطر از تنگه هرمز را از ایران دریافت کرده است.
🔴
براساس این گزارش، یک محموله دیگر LNG قطر نیز در همین ماه با مجوز ایران از تنگه هرمز عبور کرده و به پاکستان رسیده بود.
🔴
کشتی حامل محموله جدید قرار است فردا به پایانه واردات پاکستان برسد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/148611" target="_blank">📅 21:29 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148610">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
جی دی ونس: این انتخابات میان‌دوره‌ای میان کسانی است که معتقدند این کشور باید آینده‌ای داشته باشد و کسانی که ترجیح می‌دهند آن را ویران کرده و از نو بسازند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/148610" target="_blank">📅 21:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148609">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
هند نیز‌ به محاصره هوایی آمریکا علیه ایران پیوست؛ گزارش ها از توقف پرواز ها میان ایران و هند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/148609" target="_blank">📅 21:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148608">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
بلومبرگ: روسیه در پی حملات اوکراین در نظر دارد ممنوعیت صادرات بخش عمده‌ای از گازوئیل را فراتر از پایان ماه سپتامبر تمدید کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/148608" target="_blank">📅 21:03 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148607">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7AmbQd4Z8SXQnVIiLCvbkpuA38DqjI51GQtrXZ-VRSvL4vs8K9i5jF2KMyaFPHlOj64-BmT4Hl6f5DOI5EGgtNdso_Ns-rw06K2ffB5ffYuBc9V9d_ke-FLOQvgkLl3fgVXmgd2b_LWsSiuimylQ_LmRUcdlsWc36KQ9gxHssSF1Bc_RsbtHwaxmSMmVBpiVRjSV_vOLp2DSJ9f2GUnslSYq6hdSO1nl8Hj5oPJqof_QvmsTzLamIgnJz2F7tKKSKiFhAHmarrkFNv8E46MKCvFJIgALDJXl28IRM5gHzBYfGcbcQfeToRC-MV5X9HvKTzXEaNl56yCt_fIynBbcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان از اولین خودروی تولید داخلی‌اش رونمایی کرد!
🔴
عربستان یک خودروسازی با عنوان CEER (سیر) راه‌اندازی کرده و خودروهای برقی با نام اگزوبات تولید می‌کند
🔴
امروز از یک سدان و یک شاسی‌بلند رونمایی کرده و قرار است خودروهای اگزوبات به هفت مدل برسد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/148607" target="_blank">📅 20:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148606">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
قیمت نفت بیش از ۴ درصد کاهش یافت و نفت خام برنت به زیر ۱۰۰ دلار در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/148606" target="_blank">📅 20:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAtusa Net | آتوسا 𐎱</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdTnw98V1d4FwZEPiPf-s8iRJnjAR2lUtaWmR_3r3BpgjszNpWMDMVL6iSwcZEaV8e-GT7Fzw_E9Gxh-fJ7w7Vf5fash22hiNf9_I98PoeYxkJ94VwcFmhvSvyZqGTKSFunVBuFGRe_0evV9GKki6PxfafljwLHPBpaHqHo2OnK_Ge4cmjduwmQR4Ege27CU-_VoXvPVAtK0km9K2ciwFiO5MRLvZY3ls1g84iFAVoR8mXUkaCEaNUcLVq6HL_AcKUOcLs1W6EWZ_IhI_vxZyAqV0UiWvmzDyq3oTbZwSkd3G2VR6vSb4j-6cpt_4qPcOs0GGvixIdAPraoGKyE6Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💙
۳ گیگ تست رایگان — همین الان بگیر!
🎁
تست رایگان، آنی و بدون ریسک قبل از خرید
✔️
مناسب نت ملی
برای دریافت تست، وارد ربات شو.
🤖
@AtusaVpnBot</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/148604" target="_blank">📅 20:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e792e78e3a.mp4?token=hwCT1naO0Fz-63p6F7JEHF1jiG-SMgSYOoccfiLfASLBX1J_p3l4abFCCnH8WN4LE8itXZ1Bw6-UqX5AeqVLMglO_kIns8sNBASFKv25HbX09sAIKBNFSjuqJTyDkbX2wDw6EMuVisBM3VVDrsZo2uo5kAe5Q_19k_hmKJlR0ljPFK_GEVYSsm_ygq64FDIkjLvT4nl4d-LgqZ1MR8sFWWeLHzr-OyaA2x8Pt_ivTMJNzJIMbIMzkOgVffjSv_x3MRcKndwBPwWMitvgvfmZvCa1_opHdAaP_yVrY_t5PQ7e4oIBMGEBMs-zmVdG5yLFNzE2qJ231D6k-ZzGmMGEfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e792e78e3a.mp4?token=hwCT1naO0Fz-63p6F7JEHF1jiG-SMgSYOoccfiLfASLBX1J_p3l4abFCCnH8WN4LE8itXZ1Bw6-UqX5AeqVLMglO_kIns8sNBASFKv25HbX09sAIKBNFSjuqJTyDkbX2wDw6EMuVisBM3VVDrsZo2uo5kAe5Q_19k_hmKJlR0ljPFK_GEVYSsm_ygq64FDIkjLvT4nl4d-LgqZ1MR8sFWWeLHzr-OyaA2x8Pt_ivTMJNzJIMbIMzkOgVffjSv_x3MRcKndwBPwWMitvgvfmZvCa1_opHdAaP_yVrY_t5PQ7e4oIBMGEBMs-zmVdG5yLFNzE2qJ231D6k-ZzGmMGEfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / پستِ جدید کاخ سفید : اتفاقی در راه است.
🔴
منتظر باشید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/148603" target="_blank">📅 20:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148602">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
گوترش: شورای امنیت فلج شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/148602" target="_blank">📅 20:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
گروه حوثی (انصارالله) اعلام کرده است که عربستان سعودی اخیراً 157 حمله هوایی و موشکی را در مناطق الجوف، تعز، صعدا و مأرب در یمن انجام داده است و این اقدام را "یک تشدید جدی" توصیف کرده است.
🔴
جت‌های جنگنده F-15 و تایفون که از پایگاه‌های هوایی خمیس مشیت و طائف عملیات می‌کنند، این حملات را انجام دادند، در کنار حملات موشکی که از مناطق نجران و جیزان شلیک شدند.
🔴
گروه حوثی هشدار داده است که این حملات "بی‌پاسخ نخواهند ماند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/148601" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
خبرگزاری فرانسه: عراق پرواز ایرلاین‌های تحریم‌شده ایرانی را متوقف می‌کند
🔴
خبرگزاری فرانسه به نقل از منابع دولتی گزارش داده است که عراق قصد دارد فعالیت خطوط هوایی ایرانی مشمول تحریم‌های آمریکا را متوقف کند.
🔴
در گزارش اولیه، نام شرکت‌های هواپیمایی مشمول این تصمیم، زمان اجرای آن و جزئیات محدودیت‌های احتمالی اعلام نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/148600" target="_blank">📅 20:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ایران ۷ شرط برای بازگشت به مذاکرات با آمریکا مطرح کرد
🔴
رسانه «امواج» گزارش داده ایران برای ازسرگیری مذاکرات با آمریکا هفت شرط تعیین کرده که به گفته یک منبع سیاسی، مستقیماً هسته‌ای نیستند.
🔴
پنج شرط از شروط اعلام‌شده شامل آزادسازی دارایی‌های بلوکه‌شده، پایان جنگ در همه جبهه‌ها، عدم مداخله در امور داخلی ایران، توقف حملات به خاک ایران و رفع محاصره دریایی آمریکاست.
🔴
همزمان قطر و پاکستان تلاش‌های میانجی‌گرانه خود را افزایش داده‌اند و این مسیر جدا از کانال عمان دنبال می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/148599" target="_blank">📅 20:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148598">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8138881fc.mp4?token=vWfxfkeDzuqZBpMbh9Pzksgb_J4ysrdn3zD4qmWnOC0zJuimRieK23ov-el1RhNBISFQ4N_d8CX7jJLdOzr7jBcD7Pv8s2rfPh5hyR_qkG1HI_I3gnFDFZ0JkVQcgdZzVAZYs1ngfdOsE8ZNp-MjrAdY2W6AyvMUfCE4bUCXkeSlDoOW-8J2yaW_U4sEh0yCmIyX-UexuZVkrawqHktSgHjoStEErpiTv2mLAz65z561K8QtedSZTl91rvJvXG6OSCYLFAgtA-yDqf0KNrJNO7yZrN8GYVVgXgl6vfIlFOGTxCa-OHLK5ReePAilFZNWktxOH2jCD_hSKbC5PFt_hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8138881fc.mp4?token=vWfxfkeDzuqZBpMbh9Pzksgb_J4ysrdn3zD4qmWnOC0zJuimRieK23ov-el1RhNBISFQ4N_d8CX7jJLdOzr7jBcD7Pv8s2rfPh5hyR_qkG1HI_I3gnFDFZ0JkVQcgdZzVAZYs1ngfdOsE8ZNp-MjrAdY2W6AyvMUfCE4bUCXkeSlDoOW-8J2yaW_U4sEh0yCmIyX-UexuZVkrawqHktSgHjoStEErpiTv2mLAz65z561K8QtedSZTl91rvJvXG6OSCYLFAgtA-yDqf0KNrJNO7yZrN8GYVVgXgl6vfIlFOGTxCa-OHLK5ReePAilFZNWktxOH2jCD_hSKbC5PFt_hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرکات عجیب یک نفر تو تجمعات شبانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/148598" target="_blank">📅 20:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148597">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: ترامپ در مورد گزینه‌های رژیم ایران گفت: "در اصل، سه گزینه وجود دارد: نابود کردن آن، فروپاشی اقتصادی آن را شاهد بودن، یا به یک توافق رسیدن."
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/148597" target="_blank">📅 19:58 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148596">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
در حال حاضر بیش از 25 فروند هواپیمای سوخت‌رسان در پایگاه هوایی العدید در قطر مستقر هستند، این بزرگ ترین تجمع سوخت رسان های آمریکایی در قطر در 8 ماه گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/148596" target="_blank">📅 19:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73102782ef.mp4?token=Ulx0i_pOt6BpLPXXaUr_zbHfZgc0NbSBiY59T6zyavvrjd1_lBcqi1ciQ6uSJnA7d46zdeMdHru0oIA4YqbaIgAr07LexaFTri9WmYkQnliZEpSId9_8N7CkyLMLIyaeFxKWKCWopha7c8e88JSXp6RnseoorbKRdksKokZ7Ha5lJrjlbdSkCmuIfBcEP2coHRYU83E7X6YVcVjDkAg7YSKXNRVXDxuzP_hQpCAqD1-H26vNmmeksnAu7L9MHCK_vcJ6x2EgjZcZsOkJ8Boc3VWl65vOOod4bkWxgFHgRRuLTf2fyr_4xMG3XvOHGyEw18II4_O_VoT4Zg-dSYeLHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73102782ef.mp4?token=Ulx0i_pOt6BpLPXXaUr_zbHfZgc0NbSBiY59T6zyavvrjd1_lBcqi1ciQ6uSJnA7d46zdeMdHru0oIA4YqbaIgAr07LexaFTri9WmYkQnliZEpSId9_8N7CkyLMLIyaeFxKWKCWopha7c8e88JSXp6RnseoorbKRdksKokZ7Ha5lJrjlbdSkCmuIfBcEP2coHRYU83E7X6YVcVjDkAg7YSKXNRVXDxuzP_hQpCAqD1-H26vNmmeksnAu7L9MHCK_vcJ6x2EgjZcZsOkJ8Boc3VWl65vOOod4bkWxgFHgRRuLTf2fyr_4xMG3XvOHGyEw18II4_O_VoT4Zg-dSYeLHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سفیر ایالات متحده در سازمان ملل، مایک والتز: از آنجا که تهران در وضعیت تدافعی قرار دارد، لبنان اکنون بهترین فرصت را در طول عمر من دارد، سوریه در مسیر درستی قرار گرفته است و عراق نیز در مسیر بهتری قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/148595" target="_blank">📅 19:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148594">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فایننشال تایمز می‌گوید آمریکا و چین هنوز بر سر تمدید آتش‌بس تجاری به توافق نرسیدند. آمریکا خواستار تمدید این توافق برای ۶ ماه است اما پکن می‌خواهد این توافق برای باقی‌مانده دوره ریاست‌جمهوری دونالد ترامپ در آمریکا تمدید شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/148594" target="_blank">📅 19:39 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148593">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی بریتانیا: گزارشی درباره وقوع حادثه برای یک کشتی حامل گاز طبیعی مایع‌شده (LNG) هنگام خروج از تنگه هرمز دریافت کرده است.
🔴
ناخدای کشتی حامل گاز مایع گزارش داده است که کشتی بر اثر اصابت بقایای یک پرتابه با منشأ نامشخص آسیب دیده است.
🔴
ناخدای کشتی اعلام کرده است که تمام خدمه در سلامت هستند و هیچ‌گونه آثار آلودگی یا پیامد زیست‌محیطی مشاهده نشده است. کشتی نیز به مسیر خود ادامه خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/148593" target="_blank">📅 19:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCQW6hqalwKFm8S1qo4n_6lxRFEl_-N7Jf76A1bX7AYvOPZ0Qm2H7dskzS7Rb2Kc-rsL8_o-w_vg5NbEswzdxUsl32EPA3eTUMRHEUioOKW9T4MkQm2TL1nM67anLiWfZj62BfQD3BMC-lnnNHKtAAbQAXSMQNwZIAtxeSGy6P20_rgHF5W_M_1X2eNn5A9ok4wY8enio1y95PyvYTeAjxV2Tr8TJFu6amOwd5TJMmxpqPIJnbMPckyIPx2oLLcjIN77CcFRt25WBZOokIDzVojuZ__bGQiZo7cdvW1TYv4iBOxy1kSk-uz2LMKIbM0KOoEAjukZ9G3_c9SdWCBpVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ در تروث‌سوشال : هر کسی که در زمینه هوش مصنوعی پیروز شود، پیروز خواهد بود! در حال حاضر، ما از چین و سایر کشورها پیشرو هستیم، و من قصد دارم این برتری را حفظ کنم!
🔴
من قصد ندارم رشد چیزی را که از انقلاب صنعتی یا حتی اینترنت بزرگتر خواهد بود، محدود کنم.
🔴
ما با احتیاط عمل خواهیم کرد، و به همین دلیل، ما وزارت دادگستری و سایر نهادهای مجری قانون را داریم که در صورت لزوم، اوضاع را کنترل خواهند کرد، اما من فقط از هوش مصنوعی یا هوش فوق‌العاده (SI) حمایت خواهم کرد!
🔴
پرزیدنت دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/148592" target="_blank">📅 19:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A80gfNL_EGI5jlyjJxnsBbbCiPlCzP0W9ZpRIYYxLNSdhNodaDfZALqvw6fNPLam8VbObV1drX5Aoi9awt7HWc7zOWe3aRE9Z01bA8l7ZMh_krAkd6pkYy9blULhUrhafLqMSXP-4bRRCbtrq_ded3392JeZTQlK9ehtrEylpjGeouz0hgS_ML5BGmRTwlWVM9By7dAzA_vvYhyv5Y8B-nBNbFX4nwDOUBmf3k2oKiysxxulxrLZDPoKausj1xCMM35xP9LYRAvlndUfaXY9kab3nVefbjK7FvcVWLqaNoQTV0fjAS4nJIvHW_kLUrItc60AzNGDODuTpRuF2leMSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عباس عراقچی
:
گروه‌های لابی اسرائیل دیگر از ابراز صراحت در مورد نفوذ خود بر سیاست‌های ایالات متحده در قبال ایران ابایی ندارند. در نشریات متعلق به مریم آدل‌سون، این گروه‌ها اعلام می‌کنند که سیاست‌های آمریکا باید به گونه‌ای باشد که اطمینان حاصل شود اسرائیل در قبال هرگونه اقدامی که علیه آن انجام شود، مجازات دریافت می‌کند.
🔴
وقت آن است که واشنگتن از این محدودیت‌ها رها شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/148591" target="_blank">📅 19:23 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
الجزیره : دولت عراق طرحی را برای خلع سلاح گروه‌های وابسته به ایران تدوین کرده است که به زودی آغاز خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/148590" target="_blank">📅 19:17 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=MdPDHUs_KwNpJkKUxPJ4s7sL5tPANIo_FCzCH5gFXpNIvcoiM-R9iEux-ZVnWq4p5Xx5RfPCs8hf4R54TyGPyGKlfo09k3TcIwZQNEw9h_f0dKSp79iILSi6cyYpBKpXNV_pGDRbw8YgTVlqrfuMjoYa4kvRxrxK3bHHI3a6FHqaQhytBZp3J2G8Nn2O-rgQfo5UxF9Sk6rMpsWwgKNSCCj0eHqFnXgp5EUyAl1dD1uOLZ9BHPvoSJWRqpK7VuRkIxsf-GTFAoBFu9lVfyOn-QCtJSynmQ9PCY3b7TjtUB5yn0H8ODuOHHBSRm2oNij3OueGbeRH6j3Jh_WXGYqrO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=MdPDHUs_KwNpJkKUxPJ4s7sL5tPANIo_FCzCH5gFXpNIvcoiM-R9iEux-ZVnWq4p5Xx5RfPCs8hf4R54TyGPyGKlfo09k3TcIwZQNEw9h_f0dKSp79iILSi6cyYpBKpXNV_pGDRbw8YgTVlqrfuMjoYa4kvRxrxK3bHHI3a6FHqaQhytBZp3J2G8Nn2O-rgQfo5UxF9Sk6rMpsWwgKNSCCj0eHqFnXgp5EUyAl1dD1uOLZ9BHPvoSJWRqpK7VuRkIxsf-GTFAoBFu9lVfyOn-QCtJSynmQ9PCY3b7TjtUB5yn0H8ODuOHHBSRm2oNij3OueGbeRH6j3Jh_WXGYqrO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جِی. دی. ونس در مورد قیمت بالای بنزین: ما به خوبی از این موضوع آگاه هستیم که به دلیل اقدامات تروریستی رژیم ایران علیه کشتی‌های بین‌المللی، قیمت انرژی افزایش یافته است.
🔴
ما تمام تلاش خود را می‌کنیم تا این قیمت‌ها را کاهش دهیم، اما در عین حال، به مردم آمریکا کمک‌هایی موقت ارائه دهیم.
🔴
یکی از اقداماتی که ترامپ در مورد آن صحبت کرده است، تشویق برخی از ایالت‌ها برای ارائه معافیت‌های مالیاتی برای بنزین به مردم آمریکا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/148589" target="_blank">📅 19:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1594857d.mp4?token=csDAc2FSTdLnjWyjtQnf69tNA-YmQ3gm5J06bku05jwne19o6oxBzphZoigB7OLtyZKWdNKOcu5yH0QQ7m2JnpUn0bOePCM9dAbDfx3VpG35R5K6fnb1EhL-_ndLlP7d4ImrSLKfZGsoQ5lNUL5AJipB5ccNPm3sAo78tLr36dAJp_EjDJNzCUOf5CGzgAKjrcVGWmK4RUo3VMZRfUqrqiJjI0wbE6c2XGpCDrGYyYtcbyBEnq-UhLkBLifXZYJEJrpVmmGgoreOy2EQ_5x9o9uKoeB1hE-gIyeR4uEmCRY92FJ4orB3wOORHoJjAdvy3fNPP_Z8fhkkTj6OFqJJFInfn1j_mUcM_3CC_gU89sx9QBeQ91IPYjwxffvc-sGkn9XTPPmW0vXcoHzxaqGWxww-y3WoKJI0TZbcllPFcrT4aWLVMJKVpqea3R_ZLPLXKLOMkstFG8b2EiewlhFi01jrJ24riFoRTuk_Y9FQfZj-LYb7kgIqfHEewW2pgDJ5ernT9uOlpzbDpm95S6A1IrahW1Zh9_eI6-_hLy77IWJSCU00RtP6REt9wv1GN5gLW5v9XlWZaOE4nybznHm_DsLoitOHhmeyo3IJOWGiB5AUYYDJKyJjkUi6jPNolPjOsZe-cTgSjZkOADGJAqZmQJ7X9560ofYcqx78AbxH5OY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1594857d.mp4?token=csDAc2FSTdLnjWyjtQnf69tNA-YmQ3gm5J06bku05jwne19o6oxBzphZoigB7OLtyZKWdNKOcu5yH0QQ7m2JnpUn0bOePCM9dAbDfx3VpG35R5K6fnb1EhL-_ndLlP7d4ImrSLKfZGsoQ5lNUL5AJipB5ccNPm3sAo78tLr36dAJp_EjDJNzCUOf5CGzgAKjrcVGWmK4RUo3VMZRfUqrqiJjI0wbE6c2XGpCDrGYyYtcbyBEnq-UhLkBLifXZYJEJrpVmmGgoreOy2EQ_5x9o9uKoeB1hE-gIyeR4uEmCRY92FJ4orB3wOORHoJjAdvy3fNPP_Z8fhkkTj6OFqJJFInfn1j_mUcM_3CC_gU89sx9QBeQ91IPYjwxffvc-sGkn9XTPPmW0vXcoHzxaqGWxww-y3WoKJI0TZbcllPFcrT4aWLVMJKVpqea3R_ZLPLXKLOMkstFG8b2EiewlhFi01jrJ24riFoRTuk_Y9FQfZj-LYb7kgIqfHEewW2pgDJ5ernT9uOlpzbDpm95S6A1IrahW1Zh9_eI6-_hLy77IWJSCU00RtP6REt9wv1GN5gLW5v9XlWZaOE4nybznHm_DsLoitOHhmeyo3IJOWGiB5AUYYDJKyJjkUi6jPNolPjOsZe-cTgSjZkOADGJAqZmQJ7X9560ofYcqx78AbxH5OY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: چرا در گرینزگاد انتظار می‌رود که ترامپ به پولیتیکو دسترسی ویژه بدهد، در حالی که هیچ‌کس در رسانه‌ها انتظار نداشت که بایدن یا اوباما به بریتبارت دسترسی ویژه بدهند؟
🔴
این مسئله درباره عدالت اساسی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/148588" target="_blank">📅 19:02 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6125f7658e.mp4?token=ZxZNUfpNvnXKOIxgUHx_lazr720XQ0j2KJ8GiW9Z7yWOwCnymRfF5AT4xv5hVJdnPY-TjadsrnwrJ5z0k9oF2S3aRRLLx2mFABHLPU_mAT6zypEHYFtT8qEkLsKO-kxgjx0xHOYzRUYPBeXOjRw7uu7qvZa9B6Mwo5eB2ZG-vDGD0X3kufhGM3ScDqoOIDiwqKB0LI5IYRKvWX72s-cSs9IgfoB332m1DHUbHl5B2rLiUq_iHJhesv3SBchOE1pNfIJAqU97kjxgKfLiKz3eber7nZ4qwG3R_MnWrPkAEURO1Uqku_oILUxj_4QU38cqL7MFy7hts2-dm7k-mwoZlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6125f7658e.mp4?token=ZxZNUfpNvnXKOIxgUHx_lazr720XQ0j2KJ8GiW9Z7yWOwCnymRfF5AT4xv5hVJdnPY-TjadsrnwrJ5z0k9oF2S3aRRLLx2mFABHLPU_mAT6zypEHYFtT8qEkLsKO-kxgjx0xHOYzRUYPBeXOjRw7uu7qvZa9B6Mwo5eB2ZG-vDGD0X3kufhGM3ScDqoOIDiwqKB0LI5IYRKvWX72s-cSs9IgfoB332m1DHUbHl5B2rLiUq_iHJhesv3SBchOE1pNfIJAqU97kjxgKfLiKz3eber7nZ4qwG3R_MnWrPkAEURO1Uqku_oILUxj_4QU38cqL7MFy7hts2-dm7k-mwoZlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس درباره اوکراین:  آیا فکر می‌کنم جنگ اوکراین در نهایت حل خواهد شد؟ بله. این فقط مسئله زمان است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/148587" target="_blank">📅 18:49 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148586">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=M2NbPxrzTFIjmYnirvtEKZZY2oROHoVXY81WM-WtiZZGoa0ITD4hj5LZGAXmhsTtI-2MvW4inaVaZ0e87iPQZrxLubaMt29NGzlB5IwDqfmL4TPVIlSto8RCpIxtF5LRQcMldzOyInId_bISOfmlbX-ddKCRAzJf6YeoBg6mYsF3w_X3p8iTSicZTTYAoClApQgmTYu9iY_4nvM11GwYQ1y3mjxDGSppWmYGQ264MzXsCo3Do2xV4aUqTPk6QmTSTMOvRxI7WxZVENKISRGV1uYfFfufvywW5ncfBbOAW_r05KwM84pl8fJ-YPh_uJcmhyGXCA9PGZ6Z0dYbOJswm2mvmlGq7scitFsDViQkNmn8uyN3Z_aJw4FlLvzRxWJbSQMbsyX4PIc6dKc25AKsXw-OLccZn_Ck_nrCk5BhtB8vPGbAR_3vmWe57-Gln2sphrUMqTcZasSe-K1KmkCjbibZab_sNhBHfOLVvoNEXEKCrcg-6XHOk-F6UU6gMuJaj7rOEsDqo_Fll7NUSJqoiHhvmkJY_7GmWjPigXo8Hv_N7eO7s9FDsI1acZ-iCWWcZdpMY_UprP1RZT6Vp2KfUVWsFlZ95pORJQJ5YgO_nQ3hfMqmOlMgLZ1EHuaqbKPxi7i_DUXDfrPa3Zo1o9UxE-6yY48iC6URm7eSsfjADBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4e4fa6b9.mp4?token=M2NbPxrzTFIjmYnirvtEKZZY2oROHoVXY81WM-WtiZZGoa0ITD4hj5LZGAXmhsTtI-2MvW4inaVaZ0e87iPQZrxLubaMt29NGzlB5IwDqfmL4TPVIlSto8RCpIxtF5LRQcMldzOyInId_bISOfmlbX-ddKCRAzJf6YeoBg6mYsF3w_X3p8iTSicZTTYAoClApQgmTYu9iY_4nvM11GwYQ1y3mjxDGSppWmYGQ264MzXsCo3Do2xV4aUqTPk6QmTSTMOvRxI7WxZVENKISRGV1uYfFfufvywW5ncfBbOAW_r05KwM84pl8fJ-YPh_uJcmhyGXCA9PGZ6Z0dYbOJswm2mvmlGq7scitFsDViQkNmn8uyN3Z_aJw4FlLvzRxWJbSQMbsyX4PIc6dKc25AKsXw-OLccZn_Ck_nrCk5BhtB8vPGbAR_3vmWe57-Gln2sphrUMqTcZasSe-K1KmkCjbibZab_sNhBHfOLVvoNEXEKCrcg-6XHOk-F6UU6gMuJaj7rOEsDqo_Fll7NUSJqoiHhvmkJY_7GmWjPigXo8Hv_N7eO7s9FDsI1acZ-iCWWcZdpMY_UprP1RZT6Vp2KfUVWsFlZ95pORJQJ5YgO_nQ3hfMqmOlMgLZ1EHuaqbKPxi7i_DUXDfrPa3Zo1o9UxE-6yY48iC6URm7eSsfjADBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: اقدامات ایران علیه کشتیرانی بین‌المللی باعث افزایش قیمت انرژی شده است
🔴
جی‌دی ونس درباره افزایش قیمت بنزین گفت: «کاملاً آگاهیم که به‌دلیل اقدامات ایران علیه کشتیرانی بین‌المللی، قیمت انرژی افزایش یافته است.»
🔴
او افزود: «هر کاری بتوانیم برای کاهش این قیمت‌ها انجام می‌دهیم و در عین حال تلاش می‌کنیم تا در این دوره، فشار بر مردم آمریکا را کاهش دهیم.»
🔴
ونس گفت یکی از پیشنهادهای مطرح‌شده از سوی ترامپ، تشویق ایالت‌ها به کاهش یا تعلیق مالیات بنزین برای کمک به مردم آمریکاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148586" target="_blank">📅 18:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148585">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMaO8NKg1zYSRzI2hsdrfyE4aapDRAZQSp_N33zxvX13rn2X8W4ZDq5DE5pmMbSgcEsKk8SqFzb22g8U8GqXOKy8XcqnFLbS-L_LIIKX9T6JVGDBTK84Gu84nzjHrp2uBJ2MkB8Rq9gAtweiqaTRKc5NmUCetwAg8PBEwIzeu7ee0rGqkEhaoYrrBCCbpwgTQkUKPmIkxB_Y-kD3K2Ao5WX9-aXJvtC0qzvqzbeIYvqu0wKT-__a7-5YcrFIa3YEtya003xcDm-aIiNwUy6Zehp_qshlN-gBa0lV-mSi801CJwgL6QI4LgAuRdnXApBQMjO7ZQmzmpgncwtOfWrl8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: فرمانده سنتکام گزینه‌های حمله به یمن را به ترامپ ارائه کرد اما ترامپ تصمیم گرفت فعلا از حمله به یمن خودداری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/148585" target="_blank">📅 18:45 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148584">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: ترامپ گفت ایران نباید به سلاح هسته‌ای دست پیدا کند و برای اطمینان از این موضوع اقدام کرد.
🔴
ایران هم در پاسخ، حمل‌ونقل دریایی بین‌المللی را هدف اقدامات خود قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/148584" target="_blank">📅 18:43 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148583">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f32fb7606.mp4?token=uAcT2zBLdnIoZYpVsZkKhd4Ew0gi8Bsb7NKO9S0TRZJjck_ON7q4juHUsMPMJ6hTiEfKQrE4tBZuHgaKceTOKnZ_8MkExIx2Hrl8ZO23qOT2t9v2DIYEavQU9HhvbuuLhMaSLqnnNFnkOc8FK80BGI2BoEbOW5ceCu5vGsHyjXZF1VwEfzqdqCe1brpxCaznGWqy_6joQ4_U97n-ELUTAXbyP7ksTb4kMWoWHA0eaS5zAq-Wx_syVRbGsQm8bq2YRgISUA2bWpBhS_zKgG3dYHy2rEVQ70sJoilx2VepkpX7ZbnCYt_bSlYchl4pm3qOHPX4Amc3_LXmfJtzaZhHyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f32fb7606.mp4?token=uAcT2zBLdnIoZYpVsZkKhd4Ew0gi8Bsb7NKO9S0TRZJjck_ON7q4juHUsMPMJ6hTiEfKQrE4tBZuHgaKceTOKnZ_8MkExIx2Hrl8ZO23qOT2t9v2DIYEavQU9HhvbuuLhMaSLqnnNFnkOc8FK80BGI2BoEbOW5ceCu5vGsHyjXZF1VwEfzqdqCe1brpxCaznGWqy_6joQ4_U97n-ELUTAXbyP7ksTb4kMWoWHA0eaS5zAq-Wx_syVRbGsQm8bq2YRgISUA2bWpBhS_zKgG3dYHy2rEVQ70sJoilx2VepkpX7ZbnCYt_bSlYchl4pm3qOHPX4Amc3_LXmfJtzaZhHyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران
:
ترامپ گفت ایران نباید به سلاح هسته‌ای دست پیدا کند و برای اطمینان از این موضوع اقدام کرد.
🔴
ایران هم در پاسخ، حمل‌ونقل دریایی بین‌المللی را هدف اقدامات خود قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/148583" target="_blank">📅 18:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سایت وزارت خارجه آمریکا به طور رسمی هشدار بسته شدن آسمان کل منطقه را صادر کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/148582" target="_blank">📅 18:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148581">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07c7962a1.mp4?token=OEwmbJumvC0LCh4bQO-is_r5GP0yaot2bzMwtUPuhsL6dZu5rcsKrB5nH_Rmf6nOiU4MEyD97uedX1VarxaYoigeGNpdl72iPjNsXHGbEcLag3yebrMYuY-cPjmtFibqIPJwGkz9SOva_JoZ7TpEUfHXWkhN_FKfW_fTFRGlSuGafD14d-s1hMxyM1_Uz8fZpj5agOvmyBlnYifIRQUXDDZpOQUrPEZQHYjQ_4i9dGLDGthN9aTPFzzMqzcVRuYVdNJaqXYCA8sPICACn6K4cN4DVC3Dw76j1oiXfLKMSOA6JxyQT8n2pzKFcZZQf0nuB7kxIfhb8iVhOMk-bMbwLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07c7962a1.mp4?token=OEwmbJumvC0LCh4bQO-is_r5GP0yaot2bzMwtUPuhsL6dZu5rcsKrB5nH_Rmf6nOiU4MEyD97uedX1VarxaYoigeGNpdl72iPjNsXHGbEcLag3yebrMYuY-cPjmtFibqIPJwGkz9SOva_JoZ7TpEUfHXWkhN_FKfW_fTFRGlSuGafD14d-s1hMxyM1_Uz8fZpj5agOvmyBlnYifIRQUXDDZpOQUrPEZQHYjQ_4i9dGLDGthN9aTPFzzMqzcVRuYVdNJaqXYCA8sPICACn6K4cN4DVC3Dw76j1oiXfLKMSOA6JxyQT8n2pzKFcZZQf0nuB7kxIfhb8iVhOMk-bMbwLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده نسل ششم J-36 چین امروز دوباره در پروازهای آزمایشی روزانه مشاهده شد.
این یک هواپیمای استلت بدون دم و سه موتوری بسیار بزرگ است (حدود ۲۲ متر طول، بیش از ۵۰ تن) — تا پنج نمونه اولیه اکنون با تغییرات طراحی قابل مشاهده بین آن‌ها در حال پرواز هستند.
توسعات اخیر شامل یک ماکت ساختاری که در ۱۵ سپتامبر نمایش داده شد و یک سیستم لیزری هوایی با توان حدود ۱۰۰ کیلووات است که در کنار تصاویر J-36 در یک نمایشگاه در پکن به نمایش گذاشته شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/148581" target="_blank">📅 18:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148580">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏
👈
محکومیت سنگین قاتل کودک ۱۱ ساله در مشهد
‏
🔴
جوان ۲۳ ساله‌ای که خردادماه گذشته یک کودک ۱۱ ساله به نام ایلیا را با فریب از یک مرکز بازی رایانه‌ای خارج کرده بود، با حکم شعبه پنجم دادگاه کیفری یک خراسان رضوی به قصاص نفس، اعدام، ۲۰ سال زندان و ۷۴ ضربه شلاق محکوم شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/148580" target="_blank">📅 17:54 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148579">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f3fc6cfa.mp4?token=hgGI79lzjBRWK4I4mMjLMx6ud44N9wkeImuiGOkoutd80rK17ynCpWx_lJD3uhjknKSO0sGj534HSvjf9SJQCfA-Yc4SpLHMsn49kjqAi-YnFmeTWKIfh3uctTXoGTdtaOdtUcdIlJlGAo1lEELd3B6jVkcgjfvp8PEnF9QXg7AXTuz_s8NfASKpO78uAlxCzynwGWN29B5XCz9O31smynZlhiZH8YnzevCdOD8GexKVYjQQMPVV-7UzHnE-OyPnI8MMYQcI-p7soy9CDkYwBAUp0QbRK8S9aB97B8sWFBb71b0az5djdbRe-b7V_DsmZrN1zfGfGXJeSNqpi9kq6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f3fc6cfa.mp4?token=hgGI79lzjBRWK4I4mMjLMx6ud44N9wkeImuiGOkoutd80rK17ynCpWx_lJD3uhjknKSO0sGj534HSvjf9SJQCfA-Yc4SpLHMsn49kjqAi-YnFmeTWKIfh3uctTXoGTdtaOdtUcdIlJlGAo1lEELd3B6jVkcgjfvp8PEnF9QXg7AXTuz_s8NfASKpO78uAlxCzynwGWN29B5XCz9O31smynZlhiZH8YnzevCdOD8GexKVYjQQMPVV-7UzHnE-OyPnI8MMYQcI-p7soy9CDkYwBAUp0QbRK8S9aB97B8sWFBb71b0az5djdbRe-b7V_DsmZrN1zfGfGXJeSNqpi9kq6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ظهره‌وند: تست موشکی که سپاه انجام داد اتفاق خاصی بود؛ موشک ایرانی بالای کشتی (آمریکایی) منفجر شد و تأثیرات الکترو مغناطیسی داشت و سیستم آنها را داغون و مجبور به عقب نشینی کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/148579" target="_blank">📅 17:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148578">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دیروز روسای دانشگاه‌های آزاد کشور برای شروع دانشگاه‌ها جلسه داشتن، بعد رئیس دانشگاه آزاد گفت : مهم نیست دانشگاه رو حضوری کنیم یا نه، یکی از دلایلی که دانشجوها همش به ما درخواست میدن میگن دانشگاه‌های آزاد حضوری بشه بخاطر اینه که بیان دختر بازی کنن وگرنه هیچکدومشون علاقه‌ ای به درس خوندن ندارن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/148578" target="_blank">📅 17:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148577">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4e6e2273.mp4?token=ZAw_9IXlFVuozcP1b1ZC4Stg3TOh29S85IbRZ3j4V-_eSBiwzPRoLhMbm0XPqgGmSlT_K8FJrvYMM1eFkgd7H1-qp2oTMQ9yTthCbqD07mqwtmaKGK9rZF6cc6PiMdTASZyx1CW8wQ9yshA7sERBeQjnPZMed6tQQSTnLe6DXZ8xTFTFaeQ9WfB5gxhW9jUaKtpxsdXyreC-T095_AiR6oXrXBRfY41t1Df4K_pZNSuOe3x1kdVVpRNixIZyvHIQUAu7mJ_F9F3mRuo0OKyrh6IxwhQLDKFbsaQGki6bEkYRwHkxJsrNVHQYlE-dtZPO0vtFySwr-8vz4KDIDq776A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4e6e2273.mp4?token=ZAw_9IXlFVuozcP1b1ZC4Stg3TOh29S85IbRZ3j4V-_eSBiwzPRoLhMbm0XPqgGmSlT_K8FJrvYMM1eFkgd7H1-qp2oTMQ9yTthCbqD07mqwtmaKGK9rZF6cc6PiMdTASZyx1CW8wQ9yshA7sERBeQjnPZMed6tQQSTnLe6DXZ8xTFTFaeQ9WfB5gxhW9jUaKtpxsdXyreC-T095_AiR6oXrXBRfY41t1Df4K_pZNSuOe3x1kdVVpRNixIZyvHIQUAu7mJ_F9F3mRuo0OKyrh6IxwhQLDKFbsaQGki6bEkYRwHkxJsrNVHQYlE-dtZPO0vtFySwr-8vz4KDIDq776A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان قبل زدن زنگِ آغاز سال تحصیلی؛ یه استخاره باز کرد که انگار نتیجه خیلی جالب نبود و سَر تکون داد...
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/148577" target="_blank">📅 17:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148576">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=Q9VKKL_34IO0B2fLWs3sQGxLQ-zj1a4lQdKPGxxyuBwTBnZ3TiHPjuI5PNoJLTJoTo_EntIEI7Hp4Pke3ANCAbu7700HcPyVZU2jv7lAJ4_a0mjcFGyoYOKztxgpO9Oo3Tlc4CCtWlhLWMeqrLICLqvAUrTaxH_KTm8zjEW2wrC6gvUp-SGX84MEZrp1iNZParXikbDgyE0YBebGDQESL0KBE0wvkSH38n1r6cQs5Jsq4QA_mVFeB7xTxQAmmiFDLE5EyA5Ub6snogKepfrR6_ZnBOyyTH-_Cn4t7DlWTQY4_rAMUjfHS9mrDsBZHmGEjRe898e0-mMaSK5vcu6yrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26f3ab76f2.mp4?token=Q9VKKL_34IO0B2fLWs3sQGxLQ-zj1a4lQdKPGxxyuBwTBnZ3TiHPjuI5PNoJLTJoTo_EntIEI7Hp4Pke3ANCAbu7700HcPyVZU2jv7lAJ4_a0mjcFGyoYOKztxgpO9Oo3Tlc4CCtWlhLWMeqrLICLqvAUrTaxH_KTm8zjEW2wrC6gvUp-SGX84MEZrp1iNZParXikbDgyE0YBebGDQESL0KBE0wvkSH38n1r6cQs5Jsq4QA_mVFeB7xTxQAmmiFDLE5EyA5Ub6snogKepfrR6_ZnBOyyTH-_Cn4t7DlWTQY4_rAMUjfHS9mrDsBZHmGEjRe898e0-mMaSK5vcu6yrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از پس فردا تمام شرکت‌های هواپیمایی ایرانی حق ندارن پرواز خارجی داشته باشن و عملا محاصره هوایی هم انجام شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/148576" target="_blank">📅 17:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148575">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
یاشار سلطانی: جماعتی عادت دارند گنج را در خرابه‌ها مردم پیدا کنند.  سؤال من ساده بود:
🔴
ماجرای واگذاری ۸۰ میلیون بشکه نفت به ۴ تریدر چیست؟ این چهار نفر چگونه انتخاب شدند و خط اعتباری با چه مجوزی برایشان ایجاد شد؟
🔴
اگر بنا دارید با کج‌فهمی عمدی از تعبیر «موشک…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/148575" target="_blank">📅 17:04 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148574">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3jm0GtJe5aCF7K2oWlj6RFl77AwQSrEL17NZbeSESsytdzhqh_dNXxX5y41Sgn6t692PpC7Xf4pUYXBshEOqEhj2ggMvZ99CRaTsCk6gZbW8Mxr9PF6NZKA0911sQMdgSy0rSocbXZbYOE9CVeY2S20ZklGv1W_JGei2dcs1xj8WhxxFCLNt-RHJ0CiKXpPyuSBmreeyhe7s9t5_vE3zCGHj8ibnNCC4rIZ2kSkJP0Hx7MSP5JHWG0Bdk9gfwSzPVSlJsaMVXspfA_SCC84OIIcMKv27D2lmnixtknCISFkB1H0Q5YnK0xypw7txzDjfpF2LOzkZIxwzsSvAFyDcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یاشار سلطانی:
جماعتی عادت دارند گنج را در خرابه‌ها مردم پیدا کنند.
سؤال من ساده بود:
🔴
ماجرای واگذاری ۸۰ میلیون بشکه نفت به ۴ تریدر چیست؟ این چهار نفر چگونه انتخاب شدند و خط اعتباری با چه مجوزی برایشان ایجاد شد؟
🔴
اگر بنا دارید با کج‌فهمی عمدی از تعبیر «موشک به توافق»، اصل ماجرا را منحرف کنید، از فردا اسناد بیشتری منتشر می‌کنم تا سوءتفاهم‌های ساختگی‌تان کاملاً برطرف شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/148574" target="_blank">📅 17:00 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148573">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بودجه نظامی طالبان در سال جدید حدود ۷میلیارد دلار تخمین زده شده
🔴
بودجه نظامی جمهوری اسلامی زیر ۵میلیارد دلار
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/148573" target="_blank">📅 16:56 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148572">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
پنتاگون ۶ فایل جدید مربوط به اشیای ناشناس پرنده (ufo) را منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/148572" target="_blank">📅 16:53 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148571">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d41b639d.mp4?token=iKqyuNIOmOR8pocul9CB6vHXTh1YL3bm8_2nK1TJ51AFKSnj9eRZ19PwxdEW_E9nAh7U0DJdQe9DdLdj5CsiK0hoHF_yTChWkqVxx6oZqkgRtiSXo8FL7sUTMapJy2OXdLb40x8qwL45OUKu2i1HpLWzHVzQOmu7zT4wnBa0Y4ie0QYCqWZgeTX6n0OP4HEDUlEFm07U686ubckQLqcg4TxtoIPoXy5reD8XIAqTmVXX_VMTOzs4ElflUVQUg_EF9sGCUjgW_OTswOrlyjXDe8b-nj58vCo8yfhP1khLwd0XukPU_YOeVvCfY2tKFvekh8hlJ5cP74pboxieDxM-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d41b639d.mp4?token=iKqyuNIOmOR8pocul9CB6vHXTh1YL3bm8_2nK1TJ51AFKSnj9eRZ19PwxdEW_E9nAh7U0DJdQe9DdLdj5CsiK0hoHF_yTChWkqVxx6oZqkgRtiSXo8FL7sUTMapJy2OXdLb40x8qwL45OUKu2i1HpLWzHVzQOmu7zT4wnBa0Y4ie0QYCqWZgeTX6n0OP4HEDUlEFm07U686ubckQLqcg4TxtoIPoXy5reD8XIAqTmVXX_VMTOzs4ElflUVQUg_EF9sGCUjgW_OTswOrlyjXDe8b-nj58vCo8yfhP1khLwd0XukPU_YOeVvCfY2tKFvekh8hlJ5cP74pboxieDxM-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی و پشم ریزون
‼️
🔴
یکی از نوادگان شیخ بهایی بعد ۴۰۰سال اومده از آستان قدس شکایت کرده که شما برداشتید خونه شیخ بهایی رو قاطی حرم کردید و ما رضایت نداریم و خونمون رو پس بدید
🔴
حالا اون خونه کجاست؟ وسط حرم! آستان قدس هم به اون شخص ۹۰میلیارد داده تا رضایت بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/148571" target="_blank">📅 16:46 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148570">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سردار عظیم زاده:مردم تبریک، ظهور امام زمان بخاطر تجمعات شبانه جلو افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/148570" target="_blank">📅 16:40 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148569">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OaGVh9_WCO6uar4_VciT407mnTmU8cNUQaGHuZqYjhDaiGstdMTaYfH9gd3wGSySQDbSJ7LhgNV49w0BjCbgaCVUNmB4fRgxxwDua8HIiTwvsKzhhd-5FS61HHW1_jMpjb4_DREb0-w0FP5gf7tYYyvJzCe78VVYYdLm5r0UQlaP4WYP2cyqQsaaY-MkB6RK0ck4OJPdbVpL761LT7Y7dYslTXVDeDirnynwZ8yThza2mZWl6fYbEs5f9qAd2ihGDe5xdDoMbO70wNWkMW43f_U2FuZElSWiFpF3JJZgyaR0md5NEByHJU02F0Cc4rc30dj9UphbvKPs62IZBuM0pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار عظیم زاده:مردم تبریک، ظهور امام زمان بخاطر تجمعات شبانه جلو افتاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/148569" target="_blank">📅 16:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148568">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سریال انفجارهای مشکوک در انبارهای مهمات سوریه
🔴
طی ۳۰ روز گذشته، ۵ مورد انفجار گسترده در انبارهای مهمات و تجهیزات نظامی در مناطق مختلف سوریه به ثبت رسیده که زنگ خطری برای وضعیت امنیتی این مناطق به شمار می‌رود.
🔴
انفجار انبار مهمات در «الضمیر» (حومه دمشق)
🔴
انفجار انبار مهمات در «سرمدا» (حومه ادلب)
🔴
انفجار خودروی حامل مهمات در «بنش» (حومه ادلب)
🔴
انفجار انبار مهمات در منطقه «عیاش» (دیرالزور)
🔴
انفجار انبار مهمات در «العیس» (حومه حلب)
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/148568" target="_blank">📅 16:28 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148567">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
گواهینامه رانندگی ۹ برابر گران شد!
🔴
هزینه دریافت گواهینامه رانندگی که در سال ۱۴۰۰ حدود یک میلیون و ۷۵۰ هزار تومان بود، در سال ۱۴۰۵ به حدود ۱۶ میلیون تومان رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/148567" target="_blank">📅 16:24 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148566">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سه رسانه CNN، MS NOW و پولیتیکو اعلام کرده‌اند در واکنش به ممنوعیت ورود خبرنگارانشان به کاخ سفید، علیه دولت دونالد ترامپ شکایت قضایی ثبت می‌کنند.
🔴
این رسانه‌ها می‌گویند تصمیم کاخ سفید حقوق آنها بر اساس متمم اول قانون اساسی آمریکا و آزادی مطبوعات را نقض کرده است. خبرنگاران این سه رسانه پیش‌تر از ورود به کاخ سفید منع و اعتبارنامه‌هایشان نیز لغو یا ضبط شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/148566" target="_blank">📅 16:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148565">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوووووووووووووووووووری/ آژیر خطر در شمال اسرائیل به صدا در آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/148565" target="_blank">📅 16:12 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148564">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
فوووووووووووووووووووری/
آژیر خطر در شمال اسرائیل به صدا در آمد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/148564" target="_blank">📅 16:10 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148563">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا : چین به‌شدت در حمایت از کارزار علیه ایران مشارکت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/148563" target="_blank">📅 16:09 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148562">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d80d29b4a.mp4?token=KOGfBCONNNr_CNZO-iqzYDLKBZ9YmZybqO3gXptXMIhourSLK_0ilnC7DhHAlrEYJs1nIu4J8re2JN-30hZjNRNCVQwMWDTrjPTTdmL6aY-IrHekpcZ1OpJcjkgU8dPvMcYWJE0y64iycURVi39BnaQOYTxn5uZvgoHbEtisaphALDuJluQC2WjhIBvZdOZvkEmpCulSTHhA9K7buDGLNkdJek_Tjt577-NFedRmVD9eOO-ovF_3d7AggXTMuY8oPXJylI-ceXzzvO2AGEx11dvyM89f6G8uymRV8Y_xrJOl-5ib5dCxzjF0JE1LXc9Hzs-Fbo8joK0rMnXBxRDFgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d80d29b4a.mp4?token=KOGfBCONNNr_CNZO-iqzYDLKBZ9YmZybqO3gXptXMIhourSLK_0ilnC7DhHAlrEYJs1nIu4J8re2JN-30hZjNRNCVQwMWDTrjPTTdmL6aY-IrHekpcZ1OpJcjkgU8dPvMcYWJE0y64iycURVi39BnaQOYTxn5uZvgoHbEtisaphALDuJluQC2WjhIBvZdOZvkEmpCulSTHhA9K7buDGLNkdJek_Tjt577-NFedRmVD9eOO-ovF_3d7AggXTMuY8oPXJylI-ceXzzvO2AGEx11dvyM89f6G8uymRV8Y_xrJOl-5ib5dCxzjF0JE1LXc9Hzs-Fbo8joK0rMnXBxRDFgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: فشار می‌آورند و مدام حقوق اضافه می‌کنند از آن طرف تورم بالا می‌رود و حقوق بی‌‎ارزش می‌شود/ به دنبال راهکار هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/148562" target="_blank">📅 16:07 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148561">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6179dbe6f.mp4?token=pNSZNpNbT2tmPmys9sEmLsUSkcKTCVWkoTtawcrnjiWh-Cu0X7jsPiuNUkJ5-igx98CeSJeBmRv1IR8t0rWV1DoBRII72asT94ColLUeCNjwSRB3mG0FfhKuEfpb5ORdVlLA26bY1agwTIo2TZJQHTDrPVjppZndq8CWxL8c7opBRcCmzgAEENCeuOYpkmmWDV8gigOak24rsZAYfHesHGixg92oDOYUzYjDsv6JAUu6Ka7xCQJrwbr3CsBtMevZWoKRlUkfU1_gA_cP_r-Ew5dS2FWhwXqitD9CDlVzXCq9oN9o-FMJDTGqLfA7BkAtqOUf3CR9YNKH1y9iIfuOSbAkNwjj-D0L-N4K4LGb0v8tOaMomitjbtCSXb62Tse1bN8V2O9tdpIkNfAPq1gOFnNAhyJ_lTMVLD8_8snEC0qK55zrZNNdrsY6HG8lDpnyn6P7agUXQ4r31qK8CNthdNxUh5UjM1ch4lI5mDBUIcYioYKvf_qXmjxjcVi_z_tzrUUN2gbaBChfwKi30Vrilj5A2oO9YLNOpPGniXmlBm0o-HjvRxs58kdyJwHw_kLz3wOKbtpNaCCZLWfygfxM2YRj4vUJE2IVakqKVm0HHk1xXBZeOUzcqxvAGHQ9ZhWPR5NdifTeCHzGWVWS8K-9oH35GG4ykNZ_f8k3TsdHiNE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6179dbe6f.mp4?token=pNSZNpNbT2tmPmys9sEmLsUSkcKTCVWkoTtawcrnjiWh-Cu0X7jsPiuNUkJ5-igx98CeSJeBmRv1IR8t0rWV1DoBRII72asT94ColLUeCNjwSRB3mG0FfhKuEfpb5ORdVlLA26bY1agwTIo2TZJQHTDrPVjppZndq8CWxL8c7opBRcCmzgAEENCeuOYpkmmWDV8gigOak24rsZAYfHesHGixg92oDOYUzYjDsv6JAUu6Ka7xCQJrwbr3CsBtMevZWoKRlUkfU1_gA_cP_r-Ew5dS2FWhwXqitD9CDlVzXCq9oN9o-FMJDTGqLfA7BkAtqOUf3CR9YNKH1y9iIfuOSbAkNwjj-D0L-N4K4LGb0v8tOaMomitjbtCSXb62Tse1bN8V2O9tdpIkNfAPq1gOFnNAhyJ_lTMVLD8_8snEC0qK55zrZNNdrsY6HG8lDpnyn6P7agUXQ4r31qK8CNthdNxUh5UjM1ch4lI5mDBUIcYioYKvf_qXmjxjcVi_z_tzrUUN2gbaBChfwKi30Vrilj5A2oO9YLNOpPGniXmlBm0o-HjvRxs58kdyJwHw_kLz3wOKbtpNaCCZLWfygfxM2YRj4vUJE2IVakqKVm0HHk1xXBZeOUzcqxvAGHQ9ZhWPR5NdifTeCHzGWVWS8K-9oH35GG4ykNZ_f8k3TsdHiNE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک آخوند: امام زمان برای ظهور به لشکر نیاز داره برای همین ما رفتیم تو لبنان ۵۰تا شهر و روستا ساختیم اما اسرائیل همشو زد داغون کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/148561" target="_blank">📅 15:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148560">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
نفتکشی که امروز در تنگه هرمز هدف «پهپاد» قرار گرفت، با پرچم بریتانیا در حرکت بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/148560" target="_blank">📅 15:59 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148559">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-8TaZ5Rj6pvbiia-x-FrbsOiz9RaAXMaCZh9UStDGOBufYAZE5wGLn0q6VaJeMOqsCwMoE8-i8Y_VdSmTJXccY0ZWyDRHrI7TCiWPIVb_FU6RBknLr55wZhU54czwgU5b4qBDjPaHlmZtWMK-cPlbGA084rptVKkKusyS8FoHSU1kbtTyaapiqS2Twr7W_aCjlZZTzPvCsBsaacUczmtbX6O21NQqWJ3kSD_H4TMgNZL3hjF55ozKNUqpzF3EsAGYwe-GJE8hwxTQCyyE2JQ9vqISu_FkpCrhXAX8YpBeGfI1Ih3D_K-aeKsTxTilRxO2MlMQXnkaFbUU2ve1BCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:  متاسفانه، روسیه به دلیل جنگش با اوکراین، کنترل صنعت نفت دیزل خود را از دست داده است. تعداد زیادی از پالایشگاه‌های نفت دیزل این کشور منفجر شده‌اند و حداقل به طور موقت، از کار افتاده‌اند.
🔴
این جنگ مضحک و بی‌پایان با اوکراین باید پایان یابد. کل جهان در حال رنج است، زیرا هر ماه حدود ۲۵۰۰۰ نفر، بیشتر آن‌ها سرباز، کشته می‌شوند. چه فاجعه‌ای!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/148559" target="_blank">📅 15:55 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148558">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: تمام شرکت‌های هواپیمایی ایرانی از ۲۳ سپتامبر فعالیت خود را در سراسر جهان متوقف خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/148558" target="_blank">📅 15:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148557">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
پزشکیان: هر دانش‌‎آموز یک لامپ خاموش کند، ۱۵ میلیون لامپ می‌شود. نخواهیم گذاشت چرخ کارخانه‌ها بخوابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/148557" target="_blank">📅 15:47 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148556">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCaGVTkljpgjPvnCr47cMtMBidDWNRrzfmb_LmjLX59QZPfEhAm9DgSM-Yka8DGDfioXEJfoh3mr09brohuSqUBYNwpc1FcSTBw_7asRA2uU5qcWixF73UpwY227WW5WkXhY_PpygTutDD4zb7qHYwriKDLfwdQTBwMTR9GRboR8dPdRHBJAzpR2TZLuZHQIdrGoChThe1-2w-wF96hSKaSGrheHdWPlPkjDELeAqbAwyp0rHmP9Bon5D7cakp-fk2FxAeDjcVcHS6MEn7_B2CyrPtCEWJYjAf6lbnRW1amiqnu07LrCReOahHTYkbQsNyBRcvp05npF2f6UUCwCyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: کاخ سفید قصد حمله به آزادی مطبوعات را ندارد؛ چیزی که من برای آن ارزش زیادی قائلم. هدف ما مقابله با اخبار جعلی است؛ پدیده‌ای که مانند سرطان در سراسر آمریکا گسترش یافته است.
🔴
این جریان فاسد، هدفمند، فراگیر، کاملاً هماهنگ‌شده و خارج از کنترل است. اخبار جعلی تهدیدی برای امنیت ملی ماست و باید همین حالا متوقف شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/148556" target="_blank">📅 15:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-148555">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRr-QDU8r0hWU55FE_yYXMpLcL_zg83A6vVnx8_mT8-H8-Ry3-qkDIy9vJ4Z6yIa0Rjq0pvQHDVo6VubdQweNkrGu9EulzH46bpHo9WAkNlG0wOQaVNZ9PmCXJLe9tjlg5ihzDHexnX8URkL54zLn258J7L4wZIfRhM87pRqhRVINQFxof-MYLtiL9J6Y33Na3x49W2Tnkt3mSNREEvEiUrn_woDEzWqX78x8eRKWqNXtrHcYtCH3NXoTur0w4sTSFcpQUokP_HAm5oPzJ_7za8oeFpBJhDyf6pE2pA0iBVfKWXBlHG5YrcJYApr0LFlRtONFYUhIHOzYn8y_jdzzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: پاکستان پس از مذاکره با ایران، مجوز عبور امن یک محموله دیگر گاز طبیعی مایع قطر از تنگه هرمز را به دست آورده است
🔴
این نفتکش که اواخر ژوئن از تأسیسات رأس‌لفان قطر بارگیری کرده بود، آخر هفته از تنگه هرمز عبور کرد و طبق داده‌های ردیابی کشتی‌ها قرار است تا سه‌شنبه به پایانه واردات پاکستان برسد
🔴
به گفته منابع آگاه، عبور این کشتی در مذاکرات میان مقام‌های دولتی هماهنگ شده و این دومین محموله قطری در ماه جاری است که با چنین ترتیبی به پاکستان می‌رسد. این محموله می‌تواند بخشی از کمبود انرژی پاکستان را جبران کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/148555" target="_blank">📅 15:39 · 30 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
