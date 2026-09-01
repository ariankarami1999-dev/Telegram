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
<img src="https://cdn4.telesco.pe/file/ArCWpLc91Hl_Y6tNgFlCiQcSMDgcHcQ37ryjI9063OdtYjwY22pyGssT6Z16orP7taEkXclLUX78dPVWBwBpDHsKc7z7-OXYneyFNN85MbnG-IA4xK7aj7tQ5uIEgxXxm0EZ1C7OzXOH7rWbKchewtEsOK2UincHD4aXE7oz2jCVkpMnY5QIrR7m1oHcZyxktmctQxmZ-7ffPphNWTp0dfvyJhMIf4geAVUbCytsrlVlS8It11vAwLFyxdCH2Gzea7RteTj-nmU8kOLF-Gcaaihcji5NdI9TdJu0jhpNEXcC0EdhOkJssH48aHmrkz6F7awpRhJ-YIzn-Wd6cwBJFQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 114K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-10 15:21:35</div>
<hr>

<div class="tg-post" id="msg-70913">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gr-DqO097WPWjtqg5AYfTxqyOhcG1aLr41zwFdChibxPe8Lv5iLjCaMkqSetETZdNAy9uzADuN7pPphy_Bl8YUIIeQfEGfWlZtGch-cb6cW6QjT5o2k-4Riy1tU3p-vE-rcNzgZBteT2SwdQ0Y7LhE-y_1vwBnbSt2sC8OvqLr-ON53ACy-l4XXqJm-B6HIdRJYLtNs4yx6wqZ0QueFN1vAjJ3RAimTQwGwa-r1lw5jOevHUaMfLhQoi9ByMhk67hBnRo1YeHkdfYgZ61NfhSkfGlcHsMDX7yj__5o0L_0e-s4C_nemafxs1ToY6Kc4mJiy20Ed7dtEg12ZcxzsbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNtQOg8UyzXKc85u5cwO0hoEC6sruVY3iKFkXbMgydIiJ_e1nd0S6kXOnTJwKDBJI5HWW-gXHdh0LbDH_PB1ksZh-30ILf1d7v6YZWL3I46Y8GiwGrufOZRVnV9jpCfspLJDXGzQvsD0SmXIZJi2J1FUWGZRQ-mi1jCf2ApQP8WhZ0uWL4ZSnzwkqKJoZhT9OCNJELWInp-HgAkODz4qT4sZ8AqzQsSb9Ih1g6KTSzr_EDofnvHijnH_GgKDxLuacx1MJA8jg9P4Uvn5V2dHf8qFvPbA0zLhd6D_MSGV8pZVqBab7HyCt4ewbQIeePmbBOpWx1tG8gzipRGs5DfsaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f05211278.mp4?token=Ecol3IYLhrS3XYLLuA35L9eCNdJ6RNQsZSycm2B_j2PH4awLUZTNQOMKlHDgsy38lxaJvbAJkTzdvePS_2zN_6HWCB8zUc_UX7hqBSU7Plx3Z5gcA7-aaVMswemz-9nb1YslhahJs4_FxohmQchBTVy0opiDZGD1fEQXf8gR2h7Ccd4i9sfLA2YAeYNahybjQhamMp9Adz1IGTqU8KwL1KYxQ6Q790wEf39zvrI-rel7bZs2XkurW-wanwQ0K68qTFcarUI967z-b-uY9NKvcl4VOpCxQE5hle_PGEUrh4VCW5Rby-ie_1fjcY3tpSgYA5vGMJejYJJquyFM4qnpsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f05211278.mp4?token=Ecol3IYLhrS3XYLLuA35L9eCNdJ6RNQsZSycm2B_j2PH4awLUZTNQOMKlHDgsy38lxaJvbAJkTzdvePS_2zN_6HWCB8zUc_UX7hqBSU7Plx3Z5gcA7-aaVMswemz-9nb1YslhahJs4_FxohmQchBTVy0opiDZGD1fEQXf8gR2h7Ccd4i9sfLA2YAeYNahybjQhamMp9Adz1IGTqU8KwL1KYxQ6Q790wEf39zvrI-rel7bZs2XkurW-wanwQ0K68qTFcarUI967z-b-uY9NKvcl4VOpCxQE5hle_PGEUrh4VCW5Rby-ie_1fjcY3tpSgYA5vGMJejYJJquyFM4qnpsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ز غوغای جهان فارغ!
شمال تهران
@News_Hut</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/news_hut/70913" target="_blank">📅 15:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70912">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983da46010.mp4?token=qXo9vOC4XDOc76_LKpWwpuxkzuXZEjPKMVmZ_9LMv_L2r8sQxFAWZMMrpaBEVfYd3rv0kmI2wrG2Utu1fB9dmv7sgq2mLMwC3DS5IPSP9WVbHD2TVvahAxzvJbyEIbfuiwkdV_sEcFo5zOWuTXbrKj90PNoLoFDdVFGk6WTEGKxQDL4xjRkvadudQphRIJjvJETrl9dIPeV8cl-z5B_aUy5TaAYeuhWJRhya1ztk_LnwDhcU-B8bu3bWHc0eDB2lqrSIinBvFq6AUbNK0BGi7wzyRg59FZKsHC8JCkFpHcNwj5iCX2H4IsYPxicyOQkOYeU1zSTbNg7LcY7KhnI5YjifdcihJcy4pjPewPgacBpicd4_x_OhlKQPiQH_x5y5PXlP8dzN5EACZKuKqy9HfarEQu4xVY9gwEzpyzgoWHVoRufhFdWRpYQ42EftOxl57o1DMLHNFLuX8sB8em0283hWcWmOKOXxQex0H46wKI9ZdJZrIkZX766FuIEA13iO2MUO4-LK2yy-xZ135wuCPEjByAkJRafZ-WJlGQmh55zd4fNM88dY5bgwh0t4JM2NFHehT-5acykbOr2xqD-o4UhpPfl1ldkVI3L2cC8lLxE3ntzAraeKOadQbwS45gTzCGh7_OHYrIEXFkFsxX3qKOrhBVYmtxvYQBY88i5sR2c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983da46010.mp4?token=qXo9vOC4XDOc76_LKpWwpuxkzuXZEjPKMVmZ_9LMv_L2r8sQxFAWZMMrpaBEVfYd3rv0kmI2wrG2Utu1fB9dmv7sgq2mLMwC3DS5IPSP9WVbHD2TVvahAxzvJbyEIbfuiwkdV_sEcFo5zOWuTXbrKj90PNoLoFDdVFGk6WTEGKxQDL4xjRkvadudQphRIJjvJETrl9dIPeV8cl-z5B_aUy5TaAYeuhWJRhya1ztk_LnwDhcU-B8bu3bWHc0eDB2lqrSIinBvFq6AUbNK0BGi7wzyRg59FZKsHC8JCkFpHcNwj5iCX2H4IsYPxicyOQkOYeU1zSTbNg7LcY7KhnI5YjifdcihJcy4pjPewPgacBpicd4_x_OhlKQPiQH_x5y5PXlP8dzN5EACZKuKqy9HfarEQu4xVY9gwEzpyzgoWHVoRufhFdWRpYQ42EftOxl57o1DMLHNFLuX8sB8em0283hWcWmOKOXxQex0H46wKI9ZdJZrIkZX766FuIEA13iO2MUO4-LK2yy-xZ135wuCPEjByAkJRafZ-WJlGQmh55zd4fNM88dY5bgwh0t4JM2NFHehT-5acykbOr2xqD-o4UhpPfl1ldkVI3L2cC8lLxE3ntzAraeKOadQbwS45gTzCGh7_OHYrIEXFkFsxX3qKOrhBVYmtxvYQBY88i5sR2c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
❌
اژه‌ای، رئیس قوه قضاییه:جمهوری اسلامی از هر وقت دیگه‌ای، بیشتر آماده‌ست!
کسایی که تو ایران هستن، همگی درمورد امنیت ایران یک‌صدا هستن.
اگه باز محاسبه غلطی بخوان بکنن که آشوبی یا اغتشاشی تو‌ ایران راه بندازن، مطمئن باشن که پاسخ نیروهای انتظامی، امنیتی، اطلاعاتی و قوه‌قضائیه از قبل هم قاطع‌تر خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/news_hut/70912" target="_blank">📅 14:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70911">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqO_NiRXy8nOXVwbUrmwGtnbt9Op3KDMf3BNn2BoNoyeY3WGDf8wAYT9bQ4cN-GKm-mCyGAbKMX0O-Tpu4AMP8uYEI23KZN0HW5a5pP_NTPnEUopueYlZqn6e_qrXk55JyWFBc-g7QXupcgzgYPdcbKis-QoCdlE5lHaRZqEEJ5g8St7LI9j-uTtHAQcqL8shlXbY7yXUXVWhpYir9q9QR44zHB35UKrf6kQd9v8ELFJxzxWv4yss0WwLhOxI9N6hpmg7btT6L1hnconptUwKNUOrtsqs3b87UVQjJP1YU0DHJVhCFf5pIlKePE6KTwbW2i1C2NeMv8uopcUdQ3AFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
ترامپ یک مطلب از Breitbart News را در تروث سوشال بازنشر کرد.
⏺
تیتر مطلب؛
ترامپ پس از نخستین تبادل آتش با ایران طی هفته‌های اخیر، وعده داد که «سخت» پاسخ دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/news_hut/70911" target="_blank">📅 13:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70910">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=cBUz6MAIOikogrXXDDs5yz3Lh9te0DhGAh21nTFt6hhzwzLP5PMfsWpMsO7BTHezbTkbz8KFxB6eug8DkXbNm6x7MIRwJ46O5XsWFwbwgQgifWDQuTixPkpeUJnwr3Ad0CjYLDJhVsniHQyTKF4Bmif6DF4bbVxYkdy1c3dpaDvsgkErFcqZ0CEnT4V77zg9kI88DSjURdCEEVdmIa21O_G2047Krkfw4-tfjRc8xA8iORmS8BRJPoaDFd02vBLL-cMBW9rjg2rna9p6ZpI4Lbe5MCpRvXDKtVLNKCKMjwbeSO0gtAqDx_s3Vh0so-4M9zCn_VCLZSejt2qc5A6WQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c3ff78ba6.mp4?token=cBUz6MAIOikogrXXDDs5yz3Lh9te0DhGAh21nTFt6hhzwzLP5PMfsWpMsO7BTHezbTkbz8KFxB6eug8DkXbNm6x7MIRwJ46O5XsWFwbwgQgifWDQuTixPkpeUJnwr3Ad0CjYLDJhVsniHQyTKF4Bmif6DF4bbVxYkdy1c3dpaDvsgkErFcqZ0CEnT4V77zg9kI88DSjURdCEEVdmIa21O_G2047Krkfw4-tfjRc8xA8iORmS8BRJPoaDFd02vBLL-cMBW9rjg2rna9p6ZpI4Lbe5MCpRvXDKtVLNKCKMjwbeSO0gtAqDx_s3Vh0so-4M9zCn_VCLZSejt2qc5A6WQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
کسبه پاساژ پایتخت بورس کامپیوتر تهران می‌گویند مشتری نیست و سابقه نداشته که پاساژ تا این حد خلوت باشد. یکی از آنها صراحتا اشاره کرد، گرخیدیم!
@News_Hut</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/70910" target="_blank">📅 13:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70909">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=iK3CRZ_cpkuR4yec4iEiE5N_dXQbW4XF4qhvd_Xhk5Cx86BBC4CuYlZgFCzbLldpunKWOLq2SAwPj0kfF8y8PF5mLoGedKyr5GW67AYt7ik3tZcu4P9Pc0inEv_bDOiG8_2Bbc054SNDZKxSzAZAoph2qgUy641fbYLnKMwGTCu9_Q91uwKWII0GNhisZRHuDAm3UxuRpEGYOPRPoZzH2eqFE-2qsn4AtAggPcDjFHsgEJp8Cu6MQMCx-kLrfsB_dLUKniL5SDVnIe8t0KTFf4LaoixO59MOTfEQuMUpw8ejOoYMCh8L96l-EtUhNkYJC9Qd8dvJpfipb8KHbbw1Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78ca2ad56.mp4?token=iK3CRZ_cpkuR4yec4iEiE5N_dXQbW4XF4qhvd_Xhk5Cx86BBC4CuYlZgFCzbLldpunKWOLq2SAwPj0kfF8y8PF5mLoGedKyr5GW67AYt7ik3tZcu4P9Pc0inEv_bDOiG8_2Bbc054SNDZKxSzAZAoph2qgUy641fbYLnKMwGTCu9_Q91uwKWII0GNhisZRHuDAm3UxuRpEGYOPRPoZzH2eqFE-2qsn4AtAggPcDjFHsgEJp8Cu6MQMCx-kLrfsB_dLUKniL5SDVnIe8t0KTFf4LaoixO59MOTfEQuMUpw8ejOoYMCh8L96l-EtUhNkYJC9Qd8dvJpfipb8KHbbw1Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از دندونپزشک‌ها میرن میپرسن کدوم کار زیبایی تو دندونپزشکی رو نمیذاری بچه خودت انجام بده؟
به طرز عجیبی تقریبا همشون میگن کامپوزیت و لمینیت!
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/70909" target="_blank">📅 12:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70908">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=ubdDM2zL9ud0uzurwzONi8YV9qAlySLCj1xIrL3E1dlFrWCFd25aXTBS7muKd4RLuzuSs3eWW_KH1FiL90MDuIGjto3KdNDTqCFdPAa51GjMOQWjEmyG-LJDaOxGL1TPch779plXW3rzBbPXUAtmmA90H3M4HANUsVwERo07CD8ar31JWu2NocHvxd7B6YeKqBHHwor08AjXSdiRcIE1FSczkjPui3Ej_No0xMuKYOdPy3s1D7_ChopZESX3lvzxHLS7z6fV2CFBSomA11hAhQSI4-eVGdMx5ZWTJDV04ny1s9mTAfB3kHugvZe-6jL6mmMeJuN97Mi_oo-Q1CG2-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2e303fbd.mp4?token=ubdDM2zL9ud0uzurwzONi8YV9qAlySLCj1xIrL3E1dlFrWCFd25aXTBS7muKd4RLuzuSs3eWW_KH1FiL90MDuIGjto3KdNDTqCFdPAa51GjMOQWjEmyG-LJDaOxGL1TPch779plXW3rzBbPXUAtmmA90H3M4HANUsVwERo07CD8ar31JWu2NocHvxd7B6YeKqBHHwor08AjXSdiRcIE1FSczkjPui3Ej_No0xMuKYOdPy3s1D7_ChopZESX3lvzxHLS7z6fV2CFBSomA11hAhQSI4-eVGdMx5ZWTJDV04ny1s9mTAfB3kHugvZe-6jL6mmMeJuN97Mi_oo-Q1CG2-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
غیرحضوری شدن مدارس امسال شایعه است؛ برنامه دولت به حضوری بودن مدارس است مگر اینکه اتفاقی بیافتد
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/70908" target="_blank">📅 12:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70907">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70907" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/70907" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70906">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAQE_gC1yvCbDD5U0BbYLpjF-Z2qWruNuaJEcbE_yfOuu_dP237tu_uiB3yoOuvAozObddbBGAcYgEsA63HVx8EQ42Bs-jcfcAhUvHOBl0aw1y0igoZNoBI1NPHnIeHCVrkttyScsTbvGVJtAtdL8tqd0FsoT6R0CcMFyf1hj_i6FDPk7X-RNTKNxT3geF4GxA3aTwfiH9xONYTpCAs2CpQGgXEmLD3MmtXqEkErHR7eOH9O6lgNqoyOBkchj_EwE3qiWzfCaFa_-f4oOkw3iDyuZXetgrko-iAxdoXt5rhEqfdPbTkJyaoop4i36Lf8Q6lJ9n7jcRmMJ0wXPZTycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش بینی کنید.
مونزا
🆚
تورینو
دورتموند
🆚
هامبورگ
کرمونزه
🆚
پارما
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/70906" target="_blank">📅 12:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70905">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=I4IBmlZZGJlm_thhNAVdSosPH2hzhngYpJ5bPUN_AUB1nz2gR6l2NQPeXnWUYJ_-INMDXojJQ4UZn6uq-OQ_Ue_Ytv7QGebpJRaL-O3H6wZLYekdB2Ce2ACqpgy_VaoI9NXFT0acKm9UltD_V4iQgtcxrxGG7eG-txhHrsTxUMaddePe15qul0Bna0MvPyf3ub_YrvK-G1hgCzKYsnohvoVHt6vf3Ty4OtXm0SyDNvu1ZbMLlBLpiGEdRcar6f_xrhsx_vIZcshOlgO9mJZBQJMNhh9H5VLS-GjkLg-2-CRt3z67DQpybSaxwax1phXThu_3q9bY1HB5trdwQ5egyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e393ac5d29.mp4?token=I4IBmlZZGJlm_thhNAVdSosPH2hzhngYpJ5bPUN_AUB1nz2gR6l2NQPeXnWUYJ_-INMDXojJQ4UZn6uq-OQ_Ue_Ytv7QGebpJRaL-O3H6wZLYekdB2Ce2ACqpgy_VaoI9NXFT0acKm9UltD_V4iQgtcxrxGG7eG-txhHrsTxUMaddePe15qul0Bna0MvPyf3ub_YrvK-G1hgCzKYsnohvoVHt6vf3Ty4OtXm0SyDNvu1ZbMLlBLpiGEdRcar6f_xrhsx_vIZcshOlgO9mJZBQJMNhh9H5VLS-GjkLg-2-CRt3z67DQpybSaxwax1phXThu_3q9bY1HB5trdwQ5egyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ترفند یه آقا برای فروش بیشتر:
برا اینکه فروشتون بیشتر بشه پای مشتری رو بخورید
😟
اگه پاشو نداد که بخوری بپرس ازش ببین کجا رو دوس داره بخور براش.
بازار خرابه مجبورش کنید اعتماد کنه بهتون.
بعد خوردن جنستو براش معرفی کن و اگه نخرید بازم براش بخورید.
بعد مشتری میگه هروقت بیام همیشه اینجوری سرویس میدی و اینجوریه که فروشتون میره بالا
@News_Hut</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/news_hut/70905" target="_blank">📅 12:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70904">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=c9jMz_4Pqwj6YGX4K8YhHPs64eVnUprSXLPfgNYAd88-44SrP_cRJAenzfHTLQperHPLXKqIte9dpc18QPNxU1-g-2PV3Tm-38RlQ86XH7IiADFYQCiMmjKe3B3R93g8QwUvjroALYzxUNrHWXeijs6LUDBm3DmdPjtvyNznrM9CgJvRqnATCU0ORne0DGdOnSd7WU_Ixjr_eWWO33UKUF1MoXNVgiXFwhxz4NNVNio8QC69_45dZgSuVn8Ct-gZmcLqTmEI423KwyZWQRL_ptMj8CfEYOx7z6D6qhlXBWjboml7ugDZzSBRNAaPZAIPIzIS3Jz0kN5LzwjM6NG-iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50156c76a1.mp4?token=c9jMz_4Pqwj6YGX4K8YhHPs64eVnUprSXLPfgNYAd88-44SrP_cRJAenzfHTLQperHPLXKqIte9dpc18QPNxU1-g-2PV3Tm-38RlQ86XH7IiADFYQCiMmjKe3B3R93g8QwUvjroALYzxUNrHWXeijs6LUDBm3DmdPjtvyNznrM9CgJvRqnATCU0ORne0DGdOnSd7WU_Ixjr_eWWO33UKUF1MoXNVgiXFwhxz4NNVNio8QC69_45dZgSuVn8Ct-gZmcLqTmEI423KwyZWQRL_ptMj8CfEYOx7z6D6qhlXBWjboml7ugDZzSBRNAaPZAIPIzIS3Jz0kN5LzwjM6NG-iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بسنت، وزیر خزانه‌داری آمریکا:
تنها چیزی که برای رهبرانِ ایران مهمه اینه که سرشون به گردنشون چسبیده بمونه [ زنده بمونن ].
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/70904" target="_blank">📅 11:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70903">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=LQ6u2InwIu-NY3IHhl2OPV07oUGrzgbgyBybSR1t0ja2sgmFBPLZJt5__gQu25gjZVyEBXGloJf8w4be6izBdTeA1Vi3nFPh5VSM7MNNlPUQzVx8tDPLhoqr7qbNTSh7X4GvOcJxb4ZIlvmJO0t02NeZt5kGKORUKSeau132Ynw7GqFMRdYdmb5VboLGhHwJFcCOd2U1YAD9uddpM0K4g29iSDBY6CtkU05Gnv6S-Qv1jBqD-cBP2Es06KA87w0vuMAwI4M5LZ4Hl-gg9_AuTkrUVFUcLlbo4C9hm_Ot13lpCn1PkoYJpSzQXp6-VOVXmGVeyAJUalBC4h54bR-Ixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d67cce6282.mp4?token=LQ6u2InwIu-NY3IHhl2OPV07oUGrzgbgyBybSR1t0ja2sgmFBPLZJt5__gQu25gjZVyEBXGloJf8w4be6izBdTeA1Vi3nFPh5VSM7MNNlPUQzVx8tDPLhoqr7qbNTSh7X4GvOcJxb4ZIlvmJO0t02NeZt5kGKORUKSeau132Ynw7GqFMRdYdmb5VboLGhHwJFcCOd2U1YAD9uddpM0K4g29iSDBY6CtkU05Gnv6S-Qv1jBqD-cBP2Es06KA87w0vuMAwI4M5LZ4Hl-gg9_AuTkrUVFUcLlbo4C9hm_Ot13lpCn1PkoYJpSzQXp6-VOVXmGVeyAJUalBC4h54bR-Ixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حمید رسایی:
هم‌راستایی من با اسرائیل در مسائل مهم کشور(جنگ و مذاکره) مثل داستان دویدن یوسف و زلیخا به سمت در است.
زلیخا برای گناه می‌دوید، یوسف برای دوری از گناه.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/70903" target="_blank">📅 11:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70902">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=P2G0ZvsLcRgMJAUCCHE9YDF3PPwY6vlN8dFkRDkCMEj6cN6D2Rs7n-S6vNO8be8UUgZtnzqHtTi5KK0aa_q5MkErdBI-OkOeAyC6yoNhEDXn4mzVe03vidK9_aj1RLHwiwP5zsPPxx_9pRVjvKYYrgCAs5LmAUyIc99-f-nesFcuYfHk3AYDddwPaslz9rMbU2MSBvpovpS1rMGdOIOjNyj4yJlFwy9v9tjf2JuP_yOLhW7nnT7xMiszogBMpl4FWuxS1Qf23WqadkvMbT6fW0IyEl8lcwGtXYbCtY4nnEcKuiLhSjlvtzK97RNpkn9YfQS-YxUYTpby2oZup8XeuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a64b63295.mp4?token=P2G0ZvsLcRgMJAUCCHE9YDF3PPwY6vlN8dFkRDkCMEj6cN6D2Rs7n-S6vNO8be8UUgZtnzqHtTi5KK0aa_q5MkErdBI-OkOeAyC6yoNhEDXn4mzVe03vidK9_aj1RLHwiwP5zsPPxx_9pRVjvKYYrgCAs5LmAUyIc99-f-nesFcuYfHk3AYDddwPaslz9rMbU2MSBvpovpS1rMGdOIOjNyj4yJlFwy9v9tjf2JuP_yOLhW7nnT7xMiszogBMpl4FWuxS1Qf23WqadkvMbT6fW0IyEl8lcwGtXYbCtY4nnEcKuiLhSjlvtzK97RNpkn9YfQS-YxUYTpby2oZup8XeuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مجددا در سراسر کشور، حجاب‌بان و گشت ارشاد راه اندازی شده، توی بازار تهران حجاب‌بان گذاشتن و هر کس بی‌حجاب باشه، بهش گیر میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/70902" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70901">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=PmxCWPguwsbUysYU4Uuw47xmAr8hB_VNOhNb7tVvcaGunpynBY9sYfN_horHb5V-F447qhi3jl2bFLUaukOIBEFjcvdSQPOXarHcfrxPQ5cmTrNu9Au4bp7agaeDbO1Y1pmPO3Jix0PQs-hyGHcDd8qgI2Su4MFs-C1ThA9Ay-jCV9GIsbu4hsS0xCGKIEikwnk0Gxjb4mL4ecSB-lio8vbMI02ntIYQy3Yk7CwKHMKsHM66bJpdJlA4CM3dg-1KZp0j_IDzXCSQH5Hep9nVK7Q2CI9-udR8lq5zwXjpjlrS36vw9cd8jBdDURmMCVCjqj6gi5GMK8kM-nIQUTuigA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/3f7c0f48e0.mp4?token=PmxCWPguwsbUysYU4Uuw47xmAr8hB_VNOhNb7tVvcaGunpynBY9sYfN_horHb5V-F447qhi3jl2bFLUaukOIBEFjcvdSQPOXarHcfrxPQ5cmTrNu9Au4bp7agaeDbO1Y1pmPO3Jix0PQs-hyGHcDd8qgI2Su4MFs-C1ThA9Ay-jCV9GIsbu4hsS0xCGKIEikwnk0Gxjb4mL4ecSB-lio8vbMI02ntIYQy3Yk7CwKHMKsHM66bJpdJlA4CM3dg-1KZp0j_IDzXCSQH5Hep9nVK7Q2CI9-udR8lq5zwXjpjlrS36vw9cd8jBdDURmMCVCjqj6gi5GMK8kM-nIQUTuigA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر ماشینش رو داده بود دست دوس دخترش و داشت بهش آموزش میداد که این شاهکار خلق شد:
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/70901" target="_blank">📅 10:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70900">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=B55VN1zHUetov_QpZ7G94aAXJW-RdexFqaIv5N6OvzIA6Pf_2BFpfBeMoqt5_oVU2a-LiCQ7iP9zJxrGXGqF9HjrzuW22SWN9_TsXQkFh8NmLNrZEgMErE5Fy5jot8ucgRYRQn46KOziDJmQApi7LzMvwI4OOgsJIhl2ZlMZbDTRCJ0WZ4LdI8lykQXcOku7Iapqgrmb9BhIGKYaZlAcaLfy-4P4XHgjpEpKp3L3qE1aCSwzUUcOtJwYtSkbOjoIhrvnl4Sp4EK_Yy4xMPt4Gam1GbKPphwC-vsBCgKsfbQ0ckxItk-wMUzewNEgVmxqbIN03hAsoLBI1ZM69IVXUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedadf0ba9.mp4?token=B55VN1zHUetov_QpZ7G94aAXJW-RdexFqaIv5N6OvzIA6Pf_2BFpfBeMoqt5_oVU2a-LiCQ7iP9zJxrGXGqF9HjrzuW22SWN9_TsXQkFh8NmLNrZEgMErE5Fy5jot8ucgRYRQn46KOziDJmQApi7LzMvwI4OOgsJIhl2ZlMZbDTRCJ0WZ4LdI8lykQXcOku7Iapqgrmb9BhIGKYaZlAcaLfy-4P4XHgjpEpKp3L3qE1aCSwzUUcOtJwYtSkbOjoIhrvnl4Sp4EK_Yy4xMPt4Gam1GbKPphwC-vsBCgKsfbQ0ckxItk-wMUzewNEgVmxqbIN03hAsoLBI1ZM69IVXUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇳
خب، این آقا سانت رامپال، رهبر یه گروه تو هنده که پیروهاش اونو خدا می‌دونن
.
این آقا برای خودش یه اتاق شیشه‌ای مجهز به کولر درست کرده تا وقتی اعضای فرقه میان پیشش و پاش رو می‌بوسن، آقا گرمش نشه و عرق نکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70900" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70899">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d124e793.mp4?token=P7o0YzAI-4fC8dV9CjgcJtwa_UmwK_M__p2tbTrETu9efqNColnFNnMRWlvBXRJUIozSsKgwVjh-ybCWkWdXXTPE2B3EPjC_Q3wLXaRV4Bj6EaNnsQ9EWW5kpSain7Tx6Sq1y7Qs6IaVpwbZRdqT__jfgWc1KIotbiKU9PcwsCvZsERYBJvb838Vnh38A0bId5jp03IeXLtAcRz7hYXfqPVlVHWqC7kRdpD1WKvKfUKzZIbuU-F63RtUWlWzaim2UAjCQgLoIeBeb36pRiiOyHYZ8OC9T8pw1PXShRYKJBRyJdkl7I73dmHkPhtJVTbsXIbtFEtc_r9e_YzupBUk8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d124e793.mp4?token=P7o0YzAI-4fC8dV9CjgcJtwa_UmwK_M__p2tbTrETu9efqNColnFNnMRWlvBXRJUIozSsKgwVjh-ybCWkWdXXTPE2B3EPjC_Q3wLXaRV4Bj6EaNnsQ9EWW5kpSain7Tx6Sq1y7Qs6IaVpwbZRdqT__jfgWc1KIotbiKU9PcwsCvZsERYBJvb838Vnh38A0bId5jp03IeXLtAcRz7hYXfqPVlVHWqC7kRdpD1WKvKfUKzZIbuU-F63RtUWlWzaim2UAjCQgLoIeBeb36pRiiOyHYZ8OC9T8pw1PXShRYKJBRyJdkl7I73dmHkPhtJVTbsXIbtFEtc_r9e_YzupBUk8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
📰
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی تبدیل به حکومتی شده که نه فقط مشکلات مردم رو که وظیفه یه حکومته حل نمی‌کنه، بلکه خودش تبدیل به یک کارخونه تولید مشکل برای مردم شده.
تقریباً اون ده پونزده وظیفه اصلی که حکومت‌ها انجام میدن در ایران انجام نمی‌شه.
و بر خلاف اونا حکومت جمهوری اسلامی تبدیل شده به یه جایی که روزانه برای مردم تولید مشکل می‌کنه. شده کارخونه مشکل‌سازی. شده حکومتی که مشکل‌ساز است نه مشکل‌گشا.
مهم‌ترین دلیلی هم که مردم ایران از این حکومت متنفرند و می‌خوان سریع‌تر سرنگونش کنن همینه
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70899" target="_blank">📅 09:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70898">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYjsyi8R03fNpV7kMzPdguE2svH1Je2iENfm3o2upF1A-dzn1GnS988Yg8iJCntbxMmWH8z5Mdz-AKBsUuan-AmrveVcaGFpjz72wufmZLv3UkCaYni8HXRdKm2GaUSXx97lVsVof6CU19UMYHCvyHTvcRa0p0fwuuluwKfJ1crDbZNgYXNgPifE-vdWtk_oTXJKlRHSp--AuWOz8fAqbaii0U42LrrGWbxVcoPv1EPprXSk3K0O4Yvr4xcxL_EfXQtQRezS7UmEHPit5-mZqAzOIqRpBKQDWUgfp_dV2GOotKaShDCCGkgUtjDJvojI62tgmrAtiahIPz5bmjnhfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.  @News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70898" target="_blank">📅 08:03 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70896" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70896" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DV8kNJFufhleY8y7y5jtKJXtkFDS8hddYDKc8XFePs1jtJ1whEO6aZmJWU63SeTqbEevSYES1gpTu-u8p0JtkkAPqNKF7yOmXV7zJuIfGBqjn7exFTPIABpWLEEwbi8C86_v5h1_qDpdV7dDKUUUk2CyqXL9avz4qap_XYxp9UgtcKiirunfZ22MVW6y34aRWrruR_BO820KTe4rkz5Vjna8BgKeNLa_kCjWnhaIv7G7tCz6Gu8U8OYIqeSHQTzoNjnCsxMgKhKmPcSU_eWqkIrYwJlQS5U1qd9IYOn_bwyU0BcZZLznoyKJ7QEhs0MdKGPxm5vs6iXpWB0pzx8jVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیرکس‌ بت می‌بردت وسط هیجان US Open!
🎾
🔥
🦖
رقابت‌های نفس‌گیر، امتیازهای سرنوشت‌ساز و هیجانی که تا آخرین ضربه ادامه داره!
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70895" target="_blank">📅 01:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سه موشک از سیریک استان هرمزگان به سمت شناور ها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70894" target="_blank">📅 00:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70893">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO):  گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است. به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70893" target="_blank">📅 00:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70892">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0EY8wprVwSEm4vhKw117kz0dhw1J0N2qe8Hccb7_dEWQkc3Tlu7epGDCzyaMmaDHSNS4YDte2I-F3ncoDL3gB1WVaEtONlT-bO3_fSuQKz3Z9mfQOJi4llFQmPw39cI8Jm7te7UqXjbUCWzFjlLsLA1A6LCt8f4lgeeXZ221HlyeVhh-CMQDeONuDkwKjtscwMBPinNkWSbTEDaYYt6qtp8H-VQZwWmkp2Yg8goLdp5GJs2Z3OFB0Nl3K74uL0Jbcq2uz_9cS3zcOq7WoWksFQgbVvMW7nyKjf4jLzHAC1KFWIAIwGfh8AqJlC-0IkvV0uH7RY1GW7QE_01lGBIZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا (UKMTO)
:
گزارشی مبنی بر وقوع حادثه‌ای میان یک نفت‌کش و نیروهای نظامی در اقیانوس هند دریافت کرده است.
به شناورها توصیه می‌شود ضمن در نظر گرفتن آخرین اطلاعات مربوط به امنیت دریایی، نسبت به شرایط عملیاتیِ در حال تغییر هوشیار باشند. مقامات ذی‌ربط در جریان موضوع قرار گرفته‌اند و تحقیقات در این خصوص ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70892" target="_blank">📅 00:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70891">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=ZCMB7iB5xXvE_FZyXJyXS8zna0lKZkDB5NYuTVTj1vKvnqTDV-25p_eh5tvEJD-ERqdjw_EoXAvNlaoUtbXqsBeP6ZOVuG3eoeCmHxuzwgdjIrPi84aWtDuj9ThCsSzTM7f2_gUYgY9HYz9Hrgz0_ofjJ0E62DYlr1jZI4gsARDO7Dq53du0cKOAKyhYXWjJXqn19EdAKDAE8QdjZHC8XWyeLSyqq-BU7_omSk6fnw4TSvSSYTpsmXtAWvltHjhuIje2fAqMZmiDaO7g3TwRzrxE-atyj-Lk8cDTEznihrEWKdVXBbY_Ui9JRpcL0qoctHe7MwyZ15rzKJ9yjYPgu4cwkC0_xeJO98ilUC-6nAhO4nFim4ri9Qglniszue9W85BaUDSDFBp55rbsG7wzXOtUnF2riTDRnxb2EcbN-Cxw5O6Ga68jufXxjy5FdE_RXD3om-kdJ3uE611roh49pOSsY2PhbvWnjUmoMxriSEFrdXWcD7fo9_Otj8YC5SNVeYR2upe_bhrstHzmb099vxsM4IVxN8gra1-t8_w0K_2wpuh2sb9AtosvfAmiGgDWwCr99ktsB4kxfBJ1uNq6KXsLRIKmgN8BUj2BeK4T3-Lh9M923oLYZLQ3FyHsf75SZ9hmjHSDj8zlSohqcE5y2sy-1fcOxrPdj3grggB47hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1acb363e.mp4?token=ZCMB7iB5xXvE_FZyXJyXS8zna0lKZkDB5NYuTVTj1vKvnqTDV-25p_eh5tvEJD-ERqdjw_EoXAvNlaoUtbXqsBeP6ZOVuG3eoeCmHxuzwgdjIrPi84aWtDuj9ThCsSzTM7f2_gUYgY9HYz9Hrgz0_ofjJ0E62DYlr1jZI4gsARDO7Dq53du0cKOAKyhYXWjJXqn19EdAKDAE8QdjZHC8XWyeLSyqq-BU7_omSk6fnw4TSvSSYTpsmXtAWvltHjhuIje2fAqMZmiDaO7g3TwRzrxE-atyj-Lk8cDTEznihrEWKdVXBbY_Ui9JRpcL0qoctHe7MwyZ15rzKJ9yjYPgu4cwkC0_xeJO98ilUC-6nAhO4nFim4ri9Qglniszue9W85BaUDSDFBp55rbsG7wzXOtUnF2riTDRnxb2EcbN-Cxw5O6Ga68jufXxjy5FdE_RXD3om-kdJ3uE611roh49pOSsY2PhbvWnjUmoMxriSEFrdXWcD7fo9_Otj8YC5SNVeYR2upe_bhrstHzmb099vxsM4IVxN8gra1-t8_w0K_2wpuh2sb9AtosvfAmiGgDWwCr99ktsB4kxfBJ1uNq6KXsLRIKmgN8BUj2BeK4T3-Lh9M923oLYZLQ3FyHsf75SZ9hmjHSDj8zlSohqcE5y2sy-1fcOxrPdj3grggB47hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا استفاده از سلاح هسته‌ای علیه ایران را منتفی دانسته‌اید؟
🇺🇸
ترامپ:
من هرگز چنین حرفی نمی‌زنم، اما پاسخ «بله» است. هیچ دلیلی برای آن وجود ندارد. چه سوال احمقانه‌ای. آن‌ها از نظر نظامی کاملاً شکست خورده‌اند.
من آن‌ها را شکست داده‌ام، آن‌وقت باید علاوه بر آن از سلاح هسته‌ای هم استفاده کنم؟ چه سوال احمقانه‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70891" target="_blank">📅 23:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70890">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=Bndr2fGlvKupq5ucyy8geCuubA10yNfyW_dryQvVz_SzZZO6Bzm6ZUvgcygsq2LtAk18HDypg2_sHZTvLIOvc1bhPFQw_osIAFTxGerslDXOri-DAMHEF1gevS-cWoQ9EOtBUXNO-mUG3ETPlC1QC5BK34WaMhJzWdBO7ks-4U4idbnLo7P55nOx51OlkXLD-myJjYKKU8o8RlrpR8obafrm-MhOaLV0uO5mQpH4Xutv7Mxi1N2LdeReVAKdJRFtAI5UkTm9z8nRPYXfcaEXuZpMrm1QrL1Z1K-94Fm4xafwtuL9Q_X7cW6fulDvFCb0T8NC3okiVc-LwIsI4V1FcC87Ce08qT_8QPjQ2eTHfiYUH3qOmWL7pBc31uE6odW5drP9XlF1jeCXHOBjFhZJr0JWEu-IO0esR_27vNm_2RGvN2TX-IQ_KdQzfkL6aiD9WT4CI3N9RWjDEm0dTvfin2EPUV75LLQOYf47C6bs5qLhYVziPX5oghEvjqC3EOJFSc4yI3TMIOHrOM797Tgdrqm3NTPZQD0HmWk5lkKeZXNGwmryTg3UPyJ0VX1p6sDHkzoPUtzIWudwsK4gWMM7XsJuxl6tio09Rqj3I3yTWEfxeavqZF2xbk_koH3jLZxWLW9j_r0iCmWBmU3K9PH5xhWGJRv_dL8GsHXG5UVvEOE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be4ca68587.mp4?token=Bndr2fGlvKupq5ucyy8geCuubA10yNfyW_dryQvVz_SzZZO6Bzm6ZUvgcygsq2LtAk18HDypg2_sHZTvLIOvc1bhPFQw_osIAFTxGerslDXOri-DAMHEF1gevS-cWoQ9EOtBUXNO-mUG3ETPlC1QC5BK34WaMhJzWdBO7ks-4U4idbnLo7P55nOx51OlkXLD-myJjYKKU8o8RlrpR8obafrm-MhOaLV0uO5mQpH4Xutv7Mxi1N2LdeReVAKdJRFtAI5UkTm9z8nRPYXfcaEXuZpMrm1QrL1Z1K-94Fm4xafwtuL9Q_X7cW6fulDvFCb0T8NC3okiVc-LwIsI4V1FcC87Ce08qT_8QPjQ2eTHfiYUH3qOmWL7pBc31uE6odW5drP9XlF1jeCXHOBjFhZJr0JWEu-IO0esR_27vNm_2RGvN2TX-IQ_KdQzfkL6aiD9WT4CI3N9RWjDEm0dTvfin2EPUV75LLQOYf47C6bs5qLhYVziPX5oghEvjqC3EOJFSc4yI3TMIOHrOM797Tgdrqm3NTPZQD0HmWk5lkKeZXNGwmryTg3UPyJ0VX1p6sDHkzoPUtzIWudwsK4gWMM7XsJuxl6tio09Rqj3I3yTWEfxeavqZF2xbk_koH3jLZxWLW9j_r0iCmWBmU3K9PH5xhWGJRv_dL8GsHXG5UVvEOE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شرایط وحشتناک بازار با قیمت بالای دلار.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70890" target="_blank">📅 23:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70888">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jLrD-_swjoA_3fWUugl3PRY83vV16QJ-hEzd5VoF7hqwTBI2ASM1gZLbveV8kjAh-XhLy2qphuXdyEqEzTLyYCXx9wN5yPHO0cfNy9AbFfFBFazNoSAldGlEzfYAN7m-ezJnBVy6WdQV0BTxavOFnix-KuK93OQhFXirCWrcVkXY5wDRZQiS1DU_1N01pHXO78NQWVRzWNeBQdpM7U0Z8WfXdKBIJv6cb1nsUQUGIpAUdYUsJc623JQHTz3mBZsTKz7n0Thkcwj8Zi3koLXOThZ9eiCbE3WA44HNDfPPxAx71bvGM-xqhfUg8gDIZ74Lg3wFLC1bUFv69LKMFQ0d_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G6nIYPBQdQLPO73vTx8JtGGO8OqhDRpnCPKNztjipbfOaGsPU0l0RHnwvx3C5tfVVpAZzvmc-Og4-XLDKhzM5eVRhTU01x8AsfnBoQSmr_q6Jxwn6V3kIMtwD9ApGtBnCfo-Z5nMflOtd54oVI-TxQ6-59oeLXFv2NmVcrKO9y0lgZGu1ybMHuEDhaNnGLnXTseipMf4Cmri42w2uHpkHGeT_ri90pvDUMuWZWncEXVRucIXky-ktWy694A_q_Lcld0NbvfpzZkwoSNaeO7-IXwUyCEV8DTy64vdtWsdAmXb8Rw3L9JYIxuS1MEZ-bnDu2YAcsD3PQ3EdnrVBiMbyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سلنا گومز و همسرش:
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/70888" target="_blank">📅 23:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70887">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=s9_kKHINmPTg2WL0qVWWw_Mt8Pl_SQpfhOZ4dHmgo4x7cgogxcdXN9cKSGLMbCDNsa9j99ts92DVCArYa_32Nx3jtPOXuBdM1gfRJ7ukHVtX4zBqWZvDU6ZDZejJJm3WLEhaFPjp6BkSR9FKyufdjqofZztN9gMuPlN4ujaD5VSppMEIGYHOaPvLM6TPK9TLOQcAeCvMZK0BNJGzK-2BG4u3PIs6v1LOm0MqDicfbGIZvJbFRXUE5z10W9ExCuasHT2RhKNlvYFb6IMF-M32nedcsFd9JMR16Uz6j1z-lgNZiLb_SyT9VLIuNgXvMBtVKAtkQMNZSRaBZKryGvuYhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f766eae.mp4?token=s9_kKHINmPTg2WL0qVWWw_Mt8Pl_SQpfhOZ4dHmgo4x7cgogxcdXN9cKSGLMbCDNsa9j99ts92DVCArYa_32Nx3jtPOXuBdM1gfRJ7ukHVtX4zBqWZvDU6ZDZejJJm3WLEhaFPjp6BkSR9FKyufdjqofZztN9gMuPlN4ujaD5VSppMEIGYHOaPvLM6TPK9TLOQcAeCvMZK0BNJGzK-2BG4u3PIs6v1LOm0MqDicfbGIZvJbFRXUE5z10W9ExCuasHT2RhKNlvYFb6IMF-M32nedcsFd9JMR16Uz6j1z-lgNZiLb_SyT9VLIuNgXvMBtVKAtkQMNZSRaBZKryGvuYhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
کنسرت محسن نامجو در پاریس، ۷ آذر ۱۳۹۱
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70887" target="_blank">📅 22:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70886">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=qdYtwQc0moXTU_wkEezfzRKScR1VtT-wVZd3FljuwbJdeiiiyjvwuxnbsrXPeL5tYDMM1MxhjLycFQdFyo51pYhx25WkG0k3REIRcoeWnSiCQNwvQw4SJZUFjP7jiDtoxI2sxwBlxceW50UEvOdoGkHAyCCYYNcLwufMFcHHvOrsPqRI2GgjvoXVYxJzOCqLhWE_Vrjok-PkcQKRQZ3iM9hq0sI74WjKA9SnCXTSThqXGK1BvE2sLYVGyGRknibYyinpS_0Dd4MYkm9Ovz1wz0OK4Rh4Rt5-48xtX5eu_Bc0jpBq2Vql-VcC-k0ju_9m_iEZTHUnfMIVEQgCzp7n0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0452a7515b.mp4?token=qdYtwQc0moXTU_wkEezfzRKScR1VtT-wVZd3FljuwbJdeiiiyjvwuxnbsrXPeL5tYDMM1MxhjLycFQdFyo51pYhx25WkG0k3REIRcoeWnSiCQNwvQw4SJZUFjP7jiDtoxI2sxwBlxceW50UEvOdoGkHAyCCYYNcLwufMFcHHvOrsPqRI2GgjvoXVYxJzOCqLhWE_Vrjok-PkcQKRQZ3iM9hq0sI74WjKA9SnCXTSThqXGK1BvE2sLYVGyGRknibYyinpS_0Dd4MYkm9Ovz1wz0OK4Rh4Rt5-48xtX5eu_Bc0jpBq2Vql-VcC-k0ju_9m_iEZTHUnfMIVEQgCzp7n0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای بدل ایرانی آنجلینا جولی:
تا حالا یک دفعه هیچکی دست رد رو به من نزده.
به هر مردی میگم با من ازدواج بکن نه نمیاره.
از هر جای دنیا باشه سریع خودشو میرسونه پیش من.
بعد دوستام میگن تو مهره مار داری دعانویست رو بده به ما.
علتی که اون هم قبول میکرد این بود که چون من شبیه آنجلینا جولی بودم، او میخواست این وجود رو در کنار خودش داشته باشه که مثلا مهمونی میره، پیش دوستاش میره پز بده.
من حتی بیماری‌های مشترک با خانم آنجلینا جولی دارم. هم قلشون هستم. ما ژنتیکمون مثل همه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/70886" target="_blank">📅 21:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70885">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
📰
اکسیوس:
ترامپ طرحی را برای حملات محدود علیه ایران در نزدیکی تنگه هرمز بررسی کرد.
وزیر جنگ از طرح «حملات محدود» علیه ایران که ترامپ در حال بررسی آن است، حمایت می‌کند.
طرح «حملات محدود آمریکا» علیه ایران هنوز تصویب نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70885" target="_blank">📅 20:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70884">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">⏺
🚀
فارس:انهدام یک فروند پهپاد MQ9 در شرق تنگه هرمز
دقایقی قبل، یک فروند پهپاد MQ9 با آتش سامانه نوین پدافند پیشرفته نیروی هوافضای سپاه تحت کنترل شبکه یکپارچه پدافند هوایی کشور رهگیری و منهدم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/70884" target="_blank">📅 19:59 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70883">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f517057c.mp4?token=b_5h78q5TOR9kqvMYXxXe29vRUgd9k5YRBOpzy1fo85bp6MoAVt4Fcq2JV6wDNSfzzkjsvx0jlTGvThG1LuLxmdZldU-Iqv7eAMYVsDreeQB_VZ0MJ2VL6REK446SIEdV516uFe6WbkmRdqMy8AtJSso55YbyccK061pvSsMsaacSo3LPc4XSRdgGncynzzUKIqMMWc_Efs571YjzsmC_n2xgMl4Rv1Pbs1buH7fUar3APViXx30FSEhjj4gIpukD9Dp2aAk857zyiHOJyI_xkkOVpk_nef9AYTBs3kYLSi7ADZsZTBK-jPLzey6gU3IJ591121bS6JgBhB7Bpiw0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f517057c.mp4?token=b_5h78q5TOR9kqvMYXxXe29vRUgd9k5YRBOpzy1fo85bp6MoAVt4Fcq2JV6wDNSfzzkjsvx0jlTGvThG1LuLxmdZldU-Iqv7eAMYVsDreeQB_VZ0MJ2VL6REK446SIEdV516uFe6WbkmRdqMy8AtJSso55YbyccK061pvSsMsaacSo3LPc4XSRdgGncynzzUKIqMMWc_Efs571YjzsmC_n2xgMl4Rv1Pbs1buH7fUar3APViXx30FSEhjj4gIpukD9Dp2aAk857zyiHOJyI_xkkOVpk_nef9AYTBs3kYLSi7ADZsZTBK-jPLzey6gU3IJ591121bS6JgBhB7Bpiw0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
فرزانه صادق وزیر راه:
به علت از بین رفتن زیرساخت‌ها هواپیما بدون رادار هدایت می‌شوند و تعداد پروازها کمتر شده است
👌
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/70883" target="_blank">📅 19:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70882">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇦🇷
پست جدید لئو مسی از خاطراتی که واسه تیم ملی آرژانتین ساخت
🩵
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/70882" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70881">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70881" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
http://TrexBet.com</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70881" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70880">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB_nvCw5eNQsmwRJDsH622AHfozWgooCRHgFe9R6V7Gw0Ff36iZSBEeYM9Lgb4NT5fp_XR8KO1ZQnLTZf3uk4oAr_F-yiIRfoYhLgvxxNkFSrMysQSip5ihzwu6MN9PoQxQJ6wCeKVT-8O_Ip0G-o8sZKxwBXQ8eQWKTZOedXI-rdrqxXdzX_qBNgZ5tGXlugbJKLnBKoCzxnQAx3QfA-g2ltjk2W12n0YDWCKkj7wnOU3sOqOWWsykE_vi3AhvQ5N4CbRK3nAtu5t8lGVIJlzY75rfBhLMZq0ZqMz-SqIiq_wNJnvH7AUbeH29TGTIF5Ej44KLW8kAk4O480GJF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
میکس پیشنهادی ضریب
〰️
برای بچه‌های
TrexBet
🦖
Code TrexBet:
SKCU6
آموزش استفاده از کد شرط در سایت بین المللی تیرکس بت</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70880" target="_blank">📅 19:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70879">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtEqaym-scWnUcyBx-3y531cBXwt9DMF91oIOVoMz-Z-n0JzNum-XEgsEdct3OulIFsPCBjAtg_lBdFR-lDJEm81NL9xUtQYhFv71q5lUXW1ehtayP3Z3mosw-ICfu6DlXJ4bZC9aLlcbrXYN5XPgPoBDWm6wcNCr-U_fpomJ-u6yotDasFCgjpyriR5BdxfCeJuCxYL8XGS0G5Uqdj4MoiW5p3GzHj4Zmn1M4LZmlL-1fsfSZ8zo3lbX9V9uddjmQZsH8awfqg7QKY1upNImV_m3kni0NP4rqY2WeoLYoc38XEtncgpXaHhyyLHToINchJU2mvv0oXDARZEAh1acw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💋
#فوری
؛لیونل مسی اسطوره فوتبال جهان از تیم ملی آرژانتین خداحافظی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70879" target="_blank">📅 19:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70878">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=sMfJ9kMoHYtT9DDkMpiz8nQGc00C4wf6s5CAI2r5_SBraSI-Ee2Os53hjpDlL0N4wehSopG8dlvZNWvA_QJr5sBu2hwZz9AispA7r-k0XQsXbc2fpAjnut2GTxql9Mwe2qQhMc-v5KHRdkIUsqPErFloJpt6v1TCtf_1nzFCO6dmwbPBtIIqWX33jdlS1RNcn6BkwA6TDzBuRJenDtBIISvYcZxFoI-iCfHq3KqvnzAYQqjEhAKL_GfoRkfWO3uaY20YCaADjAh_d5fisdetks6jISlKFugnSDV4eZgrj_Wercv3oAeNej7fNiWGq85uTAOOqOYX8DflhZgjjvNUZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9510f51c.mp4?token=sMfJ9kMoHYtT9DDkMpiz8nQGc00C4wf6s5CAI2r5_SBraSI-Ee2Os53hjpDlL0N4wehSopG8dlvZNWvA_QJr5sBu2hwZz9AispA7r-k0XQsXbc2fpAjnut2GTxql9Mwe2qQhMc-v5KHRdkIUsqPErFloJpt6v1TCtf_1nzFCO6dmwbPBtIIqWX33jdlS1RNcn6BkwA6TDzBuRJenDtBIISvYcZxFoI-iCfHq3KqvnzAYQqjEhAKL_GfoRkfWO3uaY20YCaADjAh_d5fisdetks6jISlKFugnSDV4eZgrj_Wercv3oAeNej7fNiWGq85uTAOOqOYX8DflhZgjjvNUZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدرضا نقدی:
ما انتظار پیروزی را داشتیم، زیرا به وعده و یاری خداوند یقین و اطمینان داشتیم.
اما انتظار نداشتیم که پیروزی به این آسانی به دست آید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70878" target="_blank">📅 18:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70877">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=R5aGnUpXFSp75E1WfxzFcdPIm39hzh9OFzeFew3TOLFRMagLkI2E_jiZgOQs78jlUU3YBlMum3-KxRAPs4O3p1ei6hyQS8XCHSSbtQLRbCbvifi65C8peeXoTPQub6lZIB5FJrIrQBxAKVGtj0ssgUjgSZVsRFQUsy5zy-ossZRG71lPXF_HnsWcstI66bYGkO_oiOTTfKfNqfO2b6zcvV4xHflN0BbUpu7NKnEDK9DWBWhz7i5ymnjJzkxzJGr6UV1tUAc8bR8Io0X5MSWainecMVZD6oyjnW9Pg5rbPsMW5KU7rfpAVQVxYLXyla7AbaVmz3xR0Qp-3S3OHU5nDyiJYYzrCbpAQhiY03KBFJUBRZdhcS2njibMEwdBgpXJ0GvXWbIXW_xtZR6g8_9vXaWUbAfD7cL5-owkFSi5VFEF9wIgO6zEF2d6kwX_z2MlvSbZjocsErh4kTwlHfo6n888Ph7_FvV1mzohYvO3nz0Ow6TR_Zr4O5CE_y-BctNhzRzpFyoJqIOHk6boE0AhXPUvluimfpK9ohr823Cmafg6qRTm2BPScTY7cna30ekJ4J9qQCFq-brlGqz5rvP8Pnq3yzoJmRW5q15_N7MnOqslIGWehsKkLlWA3wYkAW4dAvROZ8sZP8wnzWCQlMY55RBqhrv6k8VUdyFhTDgEd0k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8caf499f90.mp4?token=R5aGnUpXFSp75E1WfxzFcdPIm39hzh9OFzeFew3TOLFRMagLkI2E_jiZgOQs78jlUU3YBlMum3-KxRAPs4O3p1ei6hyQS8XCHSSbtQLRbCbvifi65C8peeXoTPQub6lZIB5FJrIrQBxAKVGtj0ssgUjgSZVsRFQUsy5zy-ossZRG71lPXF_HnsWcstI66bYGkO_oiOTTfKfNqfO2b6zcvV4xHflN0BbUpu7NKnEDK9DWBWhz7i5ymnjJzkxzJGr6UV1tUAc8bR8Io0X5MSWainecMVZD6oyjnW9Pg5rbPsMW5KU7rfpAVQVxYLXyla7AbaVmz3xR0Qp-3S3OHU5nDyiJYYzrCbpAQhiY03KBFJUBRZdhcS2njibMEwdBgpXJ0GvXWbIXW_xtZR6g8_9vXaWUbAfD7cL5-owkFSi5VFEF9wIgO6zEF2d6kwX_z2MlvSbZjocsErh4kTwlHfo6n888Ph7_FvV1mzohYvO3nz0Ow6TR_Zr4O5CE_y-BctNhzRzpFyoJqIOHk6boE0AhXPUvluimfpK9ohr823Cmafg6qRTm2BPScTY7cna30ekJ4J9qQCFq-brlGqz5rvP8Pnq3yzoJmRW5q15_N7MnOqslIGWehsKkLlWA3wYkAW4dAvROZ8sZP8wnzWCQlMY55RBqhrv6k8VUdyFhTDgEd0k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سردار محمدرضا نقدی:
همه فوتبالیست‌ها با توپی بازی می‌کنند که طبق استانداردهای یکسانی ساخته شده است، اما همه آن‌ها رونالدو نیستند.
گل زدن نیازمند فردی با انگیزه، هوش و توانایی است؛ کسی که بداند چگونه از آن ابزار استفاده کند.
آمریکایی‌ها صد برابر ما سلاح در اختیار دارند و از موشک‌ها و پهپادهای بهتری برخوردارند، اما نمی‌توانند به‌طور مؤثر از آن‌ها استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70877" target="_blank">📅 18:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70876">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=YGpcCfuz1npH-cRzqPMZaVuqjmsINz_D3INtwIdr9F20Y4N4AfZIuBSV3zg98cxFyETzhmZP5O9plCSD7dxsxbtwG5QlpmbLHXXB--ZAXs0DJMIJqp0wjCQgKgK9skKZF1N_JTRESpq5bHzOjX8GbFLSmQkZsV36sbAcWMOqQTQ04v4RK813XBbU6UOmvrQRDwEi_IKuDUR1NKiBg7i-tys586hlkukirffTxmYQvIZTicVeSt37VXZzcLE0yBc2T1icjL1hcLDx8ArNnGjx7BO6tn7UvsIeQWTMV6bZw0ks4iIM9VgoQfG0o9lPwsWeVv3zoSgLGgESmRKNvbH2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc022b8a9.mp4?token=YGpcCfuz1npH-cRzqPMZaVuqjmsINz_D3INtwIdr9F20Y4N4AfZIuBSV3zg98cxFyETzhmZP5O9plCSD7dxsxbtwG5QlpmbLHXXB--ZAXs0DJMIJqp0wjCQgKgK9skKZF1N_JTRESpq5bHzOjX8GbFLSmQkZsV36sbAcWMOqQTQ04v4RK813XBbU6UOmvrQRDwEi_IKuDUR1NKiBg7i-tys586hlkukirffTxmYQvIZTicVeSt37VXZzcLE0yBc2T1icjL1hcLDx8ArNnGjx7BO6tn7UvsIeQWTMV6bZw0ks4iIM9VgoQfG0o9lPwsWeVv3zoSgLGgESmRKNvbH2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ماموران نیروی انتظامی روز دوشنبه ۹ شهریور ۱۴۰۵، به سمت کارگران معترض به استخدام‌های رانتی در پالایشگاه لیشتر گچساران تیراندازی کردند.
در این تیراندازی چند معترض زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70876" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70875">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbczI-UyArbdmJf3J1FKXMBbDiFfILcINdrXsMCgd8K08An88URkctlK-nU0Ar36nhwkH_nvvO9XmNQdjl4aAEh2CoRWSg5bkNBe9Cr4uLRkh-nXsmiIpUdVNQDeSOkrr6x_XR8gjzapG4k7_rYn1T0tSoeFj7koW6HZvLVFuRvxS2guSYhuK542KUltwd-WnQqwyWB0uXBU2n9AMxmlQCZfNdxFx787qPaxsC670UMk8J7Mqu1IlqxlOPeE7IQxXv7hXwc-RyISHwCE8ud-uHJsTMA__rbcJnev-YBnSdscgyOzf4sNlnwoMgl3iVY3fV7CFfdy77T6aJOqr8jsLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضع خیلی قاراشمیش (یاغی)
وزارت نیرو اومده هشدار داده که مردم بنزین و گازوئیل غیرمجاز تو خونه، زیرزمین یا حیاط انبار نکنن، چون خطر آتش‌سوزی و انفجار داره و ممکنه با افزایش قیمت سوخت بیشتر بشه این کار.
گفته فقط اگه واقعاً لازم بود، مقدار خیلی کم و استاندارد با رعایت کامل ایمنی نگه دارین و موارد مشکوک رو به ۱۲۵ یا نیروهای انتظامی خبر بدین.
خلاصه مواظب جون و مال خودتون و همسایه‌ها باشین، این کارا خطرناکه و به نفع کسی نیست.
@Moris_news</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70875" target="_blank">📅 18:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70874">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237073d371.mp4?token=n1BEt-Pb-grjd3ZnOqwUwbwjOFXdKdpiRbJ-OymZ7PcrTnZhtf_33FiO2yKL1j1alSxJdfwOo3fvNyFKGgeZZpVbamjbLx3fkZivTmDu0wfS09SIGsmivn6E0gJqlFaDT-SY6dWub8BFLMIIgty5m0kSayUrqzYVNzlFgpzntBxN4e80oxA73gPUC0chsnlrLZsSqjv-e7D0eU5YlPKckHwFy3Uzntkc_IZGkIrgvgkGYaW8FmDDNMikAFQIW7ISBNDmdCvzhqDswIWrGGw_Vjwkbh0YRU5Baj9fmUtN0bd3qlrOSCKNtsYK9src-CxFpOVqbyej7VcmEQpIjQJ6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237073d371.mp4?token=n1BEt-Pb-grjd3ZnOqwUwbwjOFXdKdpiRbJ-OymZ7PcrTnZhtf_33FiO2yKL1j1alSxJdfwOo3fvNyFKGgeZZpVbamjbLx3fkZivTmDu0wfS09SIGsmivn6E0gJqlFaDT-SY6dWub8BFLMIIgty5m0kSayUrqzYVNzlFgpzntBxN4e80oxA73gPUC0chsnlrLZsSqjv-e7D0eU5YlPKckHwFy3Uzntkc_IZGkIrgvgkGYaW8FmDDNMikAFQIW7ISBNDmdCvzhqDswIWrGGw_Vjwkbh0YRU5Baj9fmUtN0bd3qlrOSCKNtsYK9src-CxFpOVqbyej7VcmEQpIjQJ6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه سری دختر اکیپی قرار دعوا گذاشتن پسرا هم دوره کردن و تشویقشون میکنن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70874" target="_blank">📅 18:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70873">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48f793f615.mp4?token=IJ9gXw4FJNrn3LccAWXD2tmWGtpISdsB744yjIADd-wBd5mwgIQ3GImPvMYZWOoXreSBdaDEz5UJjhgxfbGRmgv7XPHYwLCH4jwyhqVOIlzY-2gP3pWqZuKny5gjb0kLEnKEWghglVbRAI495SJ7olugMJJes9Gwp8Sb8y40pTo6gQl9XeNx4qIkdH3EKSagtai2EwYcRTjjMWSj--w7ndyTPrKZB45qpFWDWiYp5JQAhUX5twrFGtA_Tjk212E8r7cm-ZHTZVNY7RrstCmyskIfVCP1y4av8Xo5k0zV6Mixjyw0HWjwWltZ0MszO_TFOOISdyPRkDDqnkJ2i_N_HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48f793f615.mp4?token=IJ9gXw4FJNrn3LccAWXD2tmWGtpISdsB744yjIADd-wBd5mwgIQ3GImPvMYZWOoXreSBdaDEz5UJjhgxfbGRmgv7XPHYwLCH4jwyhqVOIlzY-2gP3pWqZuKny5gjb0kLEnKEWghglVbRAI495SJ7olugMJJes9Gwp8Sb8y40pTo6gQl9XeNx4qIkdH3EKSagtai2EwYcRTjjMWSj--w7ndyTPrKZB45qpFWDWiYp5JQAhUX5twrFGtA_Tjk212E8r7cm-ZHTZVNY7RrstCmyskIfVCP1y4av8Xo5k0zV6Mixjyw0HWjwWltZ0MszO_TFOOISdyPRkDDqnkJ2i_N_HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
⭕️
بسنت وزیر خزانه‌داری آمریکا:
می‌خواهم از اتحادیه اروپا و بانک مرکزی اروپا به خاطر بیانیه قوی‌شان در حمایت از اقدامات اقتصادی ما علیه رژیم ایران تشکر کنم.
و این گروه با هم، به این حکومت وحشتناک چهل‌وهفت‌ساله آن‌ها پایان خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70873" target="_blank">📅 17:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70872">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0baed51151.mp4?token=Fpn7J9NFRLU91kfoSytvmznEgK9mBWXHQh2iOGI-qUaB9L4sFIo4_Fd3n_jWxuDTjK_S1rxCY_ISvrx7zbqNq7wiU3_n9YhYir_3tYUxI2Fgyd7RiX8CfhNXYLJePzbaDCeacUVtevJMdKxBJc5tkvRAnGO_KBmT_ZQq-W75InN-nkJle20cbc-5Mx3Eg8oe_SpnMCACgSgQ3Poqi52iG5q2LHVQUiLHVsGe50D79B9i0FGAIzrDGailHfV2jo5jCMV9QyJhMXU3RUkaAP4dvPYS195-YeUkilRTotbMYUNtp9ckZJcI93Fkeb_NvBSBFOXkQ_uu-kmdZycn_9kfUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0baed51151.mp4?token=Fpn7J9NFRLU91kfoSytvmznEgK9mBWXHQh2iOGI-qUaB9L4sFIo4_Fd3n_jWxuDTjK_S1rxCY_ISvrx7zbqNq7wiU3_n9YhYir_3tYUxI2Fgyd7RiX8CfhNXYLJePzbaDCeacUVtevJMdKxBJc5tkvRAnGO_KBmT_ZQq-W75InN-nkJle20cbc-5Mx3Eg8oe_SpnMCACgSgQ3Poqi52iG5q2LHVQUiLHVsGe50D79B9i0FGAIzrDGailHfV2jo5jCMV9QyJhMXU3RUkaAP4dvPYS195-YeUkilRTotbMYUNtp9ckZJcI93Fkeb_NvBSBFOXkQ_uu-kmdZycn_9kfUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس‌نیوز به نقل از ترامپ:
همین الان با رئیس‌جمهور ترامپ صحبت کردم؛ او به فاکس‌نیوز گفت که ایالات متحده به حمله ایران به نیروهای آمریکایی در اردن — که دیشب رخ داد — پاسخ خواهد داد.
رئیس‌جمهور گفت: «ما ضربه سختی به آن‌ها خواهیم زد. پاسخی در کار خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70872" target="_blank">📅 17:14 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70871">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYqIPCIHtgDg6d7UbdGXG7t-P3I4yZ-40GsiGpLNSGeRfpVPVU42SSBTWuAghLaiyGJ01uVQd6QE3HJQXR6EjyhMfbHzt7hQyar2eUJmEpBqvWv06B2YYyIc6YJBocT_LHkyPGRmJuATVTcKvn0rshPqLUeL67InXt2WNnEkl3dAdIQJDTKEEOaWtOCk5fm88th21F5uE-aDbP76BgMhLt-P8l78h_NEvSTjOt_1v3J0xebAlCjB1ct55FIQVx-WKB3FiTJ6opEpwFIXPykY28zsJxaOkPvAH4tN4jnPOMlwUmEtOrHeb-_CEctcmfdB-fW69MPVnVFjTPta60gGzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
پرزیدنت ترامپ:ایران رسماً یک کشور شکست‌خورده است. کارش تمام است!
آن‌ها نه نیروی دریایی دارند، نه نیروی هوایی و نه پول ملی؛ حقوق سربازان یا نیروهای پلیس خود را نمی‌پردازند، نرخ تورم به ۳۰۰ درصد رسیده و رهبری‌شان دچار آشفتگی کامل است و توانایی نمایندگی شایسته کشور را ندارد.
تنها چیزی که دارند «اخبار جعلی» (از سوی آمریکا)، تمایل به کشتار معترضانشان (که اکنون شمار کشته‌شدگان به بیش از ۱۰۰ هزار نفر رسیده است؛ آن‌ها باید به جرم جنایات جنگی علیه بشریت محاکمه شوند!) و البته ردیفی از «چرندیات» است.
از توجه شما به این موضوع سپاسگزارم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70871" target="_blank">📅 17:10 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70870">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا بدونید شما اگه عاشق ترین فرد دنیام باشی بعد از حدود دوسال هیجان رابطتتون میاد پایین بعد از رابطتتون تکلیف مشخص میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70870" target="_blank">📅 17:00 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70869">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=nyMnhDuQXvBT66K8cJLzHvkR0hBQeTHv6lLJ4zFTNSj2bUOZwI4zxTTEf82Z51_5VeTfPQW5BKNy-Xu5a8c1KG2UpQ4MXMfxtiZb5NPSLL18oaJLLks4nG-CYgVmCYhR6UJsC8AcXSNmXWA5vFzwbtJj8wjYoN9aALExOJlmQnKXrYdwGHX3FQAJHLAPPz3QtGZFhNGCFA81FcD1B1ApE0V17kMuF_Zt2gYwtPcY8xPKbSmuh4vDNtvt1L9h91jlmiiMmB2j-H_PTMaKYL3EE57_KPlkGrakvdIzShwOJg24SXf-zpgU3d1HCYY-fiDPiKR9wSnPylZsvQ5XCWQZ8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841288ee9e.mp4?token=nyMnhDuQXvBT66K8cJLzHvkR0hBQeTHv6lLJ4zFTNSj2bUOZwI4zxTTEf82Z51_5VeTfPQW5BKNy-Xu5a8c1KG2UpQ4MXMfxtiZb5NPSLL18oaJLLks4nG-CYgVmCYhR6UJsC8AcXSNmXWA5vFzwbtJj8wjYoN9aALExOJlmQnKXrYdwGHX3FQAJHLAPPz3QtGZFhNGCFA81FcD1B1ApE0V17kMuF_Zt2gYwtPcY8xPKbSmuh4vDNtvt1L9h91jlmiiMmB2j-H_PTMaKYL3EE57_KPlkGrakvdIzShwOJg24SXf-zpgU3d1HCYY-fiDPiKR9wSnPylZsvQ5XCWQZ8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کاظم غریب‌آبادی، معاون وزیر امور خارجه:
این اقدامات تجاوزکارانه با پاسخی مناسب مواجه خواهد شد.
حضور بیگانگان باید از این منطقه حذف شود و آن‌ها باید درس‌های جدی بیاموزند تا دیگر دست به تجاوز علیه کشور ما نزنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70869" target="_blank">📅 16:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70868">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=sjHaY9PbAx-whVL8FAr_ku264ExCPk7bFTo5fo6huynR6GhxkUgLjpS3F3k1QKj2jcmoFVVQUfxn7BWiMFCNrcRplPW66bzxsZsI0WmB8iX2DGDCspkV1OJBlSfIHLtIlI76FNSVz8uGyy2YmgCysy_R6J6Pt5U_kOL9OdIWsTkgMtBaC4IN2VIZ3Yr0GBGJrWL3ZTCZkx3DNE7nhBxKZh65YA8-SX70CVKsaG_Ed4yjEB24gGZGIuePzSS3UJZ9p732m1PM83pQt1HDyYAU5r6Q4cxlBuyoPm7yMLhCUp8kPr64CvGdG16Vnvgpy8XMAOmgmMyixebZezSXoHgqxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3748363c9b.mp4?token=sjHaY9PbAx-whVL8FAr_ku264ExCPk7bFTo5fo6huynR6GhxkUgLjpS3F3k1QKj2jcmoFVVQUfxn7BWiMFCNrcRplPW66bzxsZsI0WmB8iX2DGDCspkV1OJBlSfIHLtIlI76FNSVz8uGyy2YmgCysy_R6J6Pt5U_kOL9OdIWsTkgMtBaC4IN2VIZ3Yr0GBGJrWL3ZTCZkx3DNE7nhBxKZh65YA8-SX70CVKsaG_Ed4yjEB24gGZGIuePzSS3UJZ9p732m1PM83pQt1HDyYAU5r6Q4cxlBuyoPm7yMLhCUp8kPr64CvGdG16Vnvgpy8XMAOmgmMyixebZezSXoHgqxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین شهر مراغه رفتن سر چاه فاضلاب میگن با یاد رهبر شهید پروژه رو افتتاح میکنیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70868" target="_blank">📅 16:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70867">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtTyKk1xO7NAEsncD9pHbq0kKuvYEC8TDYVx6P4GxlVwIo3DLi_CABf8DVDVDwZe8KIwHR1BqFVbrRnnSnwUKkFc3XAIxRllcc5Njskp5ZSAUA5Gno5jDjsiChBLzTfA6Uam2X78kLdCp0PqbGXDH3_3fLkWwU06j2idSxM2nFWW2YQK6kAT3-9k29b6YoQYnUEd4Zs8B-gTGLppmfByJbg7uRsdL6Fxi29jQrNwReHtzfIO9-sBxz3g4cXFqzkYbvteAR3FCtTG7e4hDSlaj6xoqdz4Bz0DJcrLlyrhQ4uL75grQzxavBVxzdScoichHmOZLJUIoXy71bsoJl2o-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
عباس عراقچی:
نتانیاهو به زبان عبری آشکارا می‌بالد که چگونه دولت آمریکا را فریب داده و به نفع اسرائیل، آن را به جنگ با ایران کشانده است.
او صراحتاً و با خنده از این می‌گوید که چگونه با اختصاص ۱۰۰۰ ساعت زمان پخش در شبکه‌های آمریکایی، بر آمریکا «تأثیر» گذاشته است.
اما به زبان انگلیسی، از رهبری رئیس‌جمهور آمریکا تمجید می‌کند.
مار خوش‌خط‌ و خال.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70867" target="_blank">📅 15:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70866">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=YwRPx62hwkPzY5t6mkCtYowDLOR8cBFwkAwS8Je35uW-UbYn5Qv-0zc0E5gsAbe5FJvUJYNZSfE1zXJ2pga8KbBYKOv6SvaO9SWFfPndLbJfoCF_H8d97ugxJyqD1lYfhGG2IpIElKJN72FgsrIPwjZzZ89onOUgA1NacsIiquilwHgzVQKkuWI3ELyHAh42mh_bai1K_IoXUCkBeAx_tvZaNAOEMIQcf3HfJB2gLG5lpYFZCrF4rgNQ362Jrd6Phmx_Y4Hg_yk619QivsP33a8MDISS45YRzZ2Q8cZrFcE4F9I6gY7N3IBqfJfvuYPiq0qWJGo9kGn_caGP4fK46Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0638c8610c.mp4?token=YwRPx62hwkPzY5t6mkCtYowDLOR8cBFwkAwS8Je35uW-UbYn5Qv-0zc0E5gsAbe5FJvUJYNZSfE1zXJ2pga8KbBYKOv6SvaO9SWFfPndLbJfoCF_H8d97ugxJyqD1lYfhGG2IpIElKJN72FgsrIPwjZzZ89onOUgA1NacsIiquilwHgzVQKkuWI3ELyHAh42mh_bai1K_IoXUCkBeAx_tvZaNAOEMIQcf3HfJB2gLG5lpYFZCrF4rgNQ362Jrd6Phmx_Y4Hg_yk619QivsP33a8MDISS45YRzZ2Q8cZrFcE4F9I6gY7N3IBqfJfvuYPiq0qWJGo9kGn_caGP4fK46Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه وایرال شده از صداوسیما:
یه نفرو آوردن برای مصاحبه؛ بعد خود مجریه فکر‌ میکنه صداش نمیره تو میکرفون؛ به اون میگه اینا رو بگو اونم همونا رو تکرار میکنه
😂
آخرشم میگه دم غیرتت گرم به‌به چه شیرزنی بود
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70866" target="_blank">📅 15:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70864">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=oyXdFnu2uPJULTwo7YmDiG2CTB001haYpky3HfBVDPUKDfLR8zhcIHPO-Sm_uStcTY20kGsNaQV3k1IB0CYGf6XpjGGQdmtAcaEOOska48TOGN2IVdSDZkOjsVr6lV_oSPDxxxgRK5MQWBMhq_cDfYMVLytTH2USk685weyIISg-xDXtZZmRRx84WYehX7zicFsSN6qh_B2oixLAtd3unucx0N36gwbIrN0ltGQsHxOaSjJm2E_AuMdZ6pP8CDxpb9PMo0Kh2OUygLG7yxG0LSwuWmezIOwSayMfF-f4WYP5oSC-77eArGNh0mCiiRQT551X8931bsiW2p2RTWUszg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1fde9913.mp4?token=oyXdFnu2uPJULTwo7YmDiG2CTB001haYpky3HfBVDPUKDfLR8zhcIHPO-Sm_uStcTY20kGsNaQV3k1IB0CYGf6XpjGGQdmtAcaEOOska48TOGN2IVdSDZkOjsVr6lV_oSPDxxxgRK5MQWBMhq_cDfYMVLytTH2USk685weyIISg-xDXtZZmRRx84WYehX7zicFsSN6qh_B2oixLAtd3unucx0N36gwbIrN0ltGQsHxOaSjJm2E_AuMdZ6pP8CDxpb9PMo0Kh2OUygLG7yxG0LSwuWmezIOwSayMfF-f4WYP5oSC-77eArGNh0mCiiRQT551X8931bsiW2p2RTWUszg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حواستون به دوربین مخفی توی ویلاها و اقامتگاه‌های اجاره‌ای باشه!
موارد واقعی از جاسازی دوربین مخفی داخل وسایل معمولی مثل ساعت، شارژر، دتکتور دود و حتی گیرنده‌ها و وسایل کنار تلویزیون گزارش شده.
پس وقتی جایی رو اجاره می‌کنید، مخصوصاً اتاق خواب و فضاهای خصوصی، یه نگاه به وسایلی بندازید که مستقیم به سمتتون قرار گرفتن. سوراخ خیلی ریز یا لنز غیرعادی روی یه وسیله می‌تونه ارزش بررسی داشته باشه.
البته اینکه «جدیداً بعضی ویلا‌دارهای ایران داخل رسیور ماهواره دوربین می‌ذارن» رو نمی‌شه به‌عنوان یک اتفاق فراگیر و تأییدشده گفت؛ امکان و نمونه چنین کاری وجود داره، ولی تعمیمش درست نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70864" target="_blank">📅 14:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70863">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=iuU8JEU2Fr5yp8IDBHi8zosp8-vbBm4pfY_NUN7QMClgY-PwJoUPGXS_DeofiLbSJGS-Pd1oD7EBR__w9wmdx1jAWLcWQGRb8x8HgH1KcmFyB9aDqmZpm1kBk8xxrgYJhOZi5-UMC6pSpe26X7e5PQJdbxc_HN-Oh7Efe6n3MGDQ5-MGIUo8yPocwskmHXRZEjQTt0SRMn__iDI4-NzsbZP3jsyQgVabOKMb9MB2_m57Wpc1B_oViO_LtZjSYtLPRT3TOJFTe9dEB5a0YZMsbncoPxUl6YnfbNVxLbe_9J735K47yLLdmkIm9dXJYuJ2kPTegHhjHaCS-zYfJZFoWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0345fee55.mp4?token=iuU8JEU2Fr5yp8IDBHi8zosp8-vbBm4pfY_NUN7QMClgY-PwJoUPGXS_DeofiLbSJGS-Pd1oD7EBR__w9wmdx1jAWLcWQGRb8x8HgH1KcmFyB9aDqmZpm1kBk8xxrgYJhOZi5-UMC6pSpe26X7e5PQJdbxc_HN-Oh7Efe6n3MGDQ5-MGIUo8yPocwskmHXRZEjQTt0SRMn__iDI4-NzsbZP3jsyQgVabOKMb9MB2_m57Wpc1B_oViO_LtZjSYtLPRT3TOJFTe9dEB5a0YZMsbncoPxUl6YnfbNVxLbe_9J735K47yLLdmkIm9dXJYuJ2kPTegHhjHaCS-zYfJZFoWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
پست جدید اسرائیل به فارسی
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70863" target="_blank">📅 13:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70862">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHpOCihcvkFUWhHE4hqDi2qidZphyXcJrofON5RuHn0Tg3Y8AKK4sSjMtqnDzZRmwE-TRKm3FU0HvvLuVfHRLRlemls1K9Q620fAPMOSPxRuBgg6AO4WZIFXJHBhSQNEGtOCDcjxxnWDMIyXjJ3rgmZg93jftfBQJdyFgq2JLPEfFymBBy7VyWWfJ8fZNghk-OaIkSKRbGfvd_JSmWI7JaE8uQx5BpWYsQA-0QsaL2e05HEG16PW2xYEV0o1M52YUP8wUvtRsavcvzAQkBFC-OYarvrnK36H0JnlU8HuStkWpgEE-JF0Xni3Fg-u8DUHtUxw8ZutLJWJKQH5szqETw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت، وزیر خزانه‌داری آمریکا، به خبرگزاری آسوشیتدپرس گفت که دولت ترامپ قصد دارد در راستای کارزار خود برای قطع دسترسی ایران به نظام مالی بین‌المللی، در هفته جاری یک بانک دیگر را تحریم کند.
بسنت اظهار داشت که واشنگتن به کشورهایی که همچنان با ایران مراودات تجاری دارند فشار خواهد آورد تا روابط مالی خود را قطع کنند، وگرنه با اقدامات تلافی‌جویانه آمریکا مواجه خواهند شد؛ او در این باره هشدار داد: «اگر ناچار شویم، این کار به مثابه خشونت مالی خواهد بود.»
انتظار می‌رود بسنت این موضوع را در جریان نشست‌های گروه ۲۰ در «اشویل» — از جمله در گفتگو با مقامات چینی — پیگیری کند. وی تأکید کرد که در خصوص اعمال تحریم علیه پکن به دلیل ادامه تعاملاتش با ایران، «همه گزینه‌ها روی میز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70862" target="_blank">📅 13:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70861">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=fidm8LLcQnbOm0aeBO3kbLQ3XNHBjzB9UOk_jyW65moZQcUAJoGUGyvP-vYgaLznPCm6c2i9psqRFhX4CDr3IfvDWpy-ZzF2Ip4AgdLyl4MkIbnTbKiyVZ0YFaiUvjZN4qKO4WSsj6TA6yfdXdHA-oLTiFEyG2oZMLG-rFCJ3F7OAazXjlnuGEQ5C8KHzN7M-Vpt5C2ug4sp-UlpNqIl1WtlusBVDTHdIpXsKXyokQ4CUSa3W-PBiKJznkm7AazWqgTscJwMYXzPbrY63582XjfiAUkDbg6szNOmEBZKUJqepCCybxSjGuGadEuOOCmAnD4ePIufn8F6dJgxRrdXAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d9350e95.mp4?token=fidm8LLcQnbOm0aeBO3kbLQ3XNHBjzB9UOk_jyW65moZQcUAJoGUGyvP-vYgaLznPCm6c2i9psqRFhX4CDr3IfvDWpy-ZzF2Ip4AgdLyl4MkIbnTbKiyVZ0YFaiUvjZN4qKO4WSsj6TA6yfdXdHA-oLTiFEyG2oZMLG-rFCJ3F7OAazXjlnuGEQ5C8KHzN7M-Vpt5C2ug4sp-UlpNqIl1WtlusBVDTHdIpXsKXyokQ4CUSa3W-PBiKJznkm7AazWqgTscJwMYXzPbrY63582XjfiAUkDbg6szNOmEBZKUJqepCCybxSjGuGadEuOOCmAnD4ePIufn8F6dJgxRrdXAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
🇺🇸
ترامپ با هوش مصنوعی جزیره خارک رو نابود کرد.
جزیره خارگ دارد به تلی از خاکستر و آوار تبدیل می‌شود!!!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70861" target="_blank">📅 12:08 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70859">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=U3d4IjmmErz-czvy3-v8soCg_siFVK8lv6hU1DPAMZg2UzhG8tGIJ69n-WnOGtcuky_NyPTUYCyLeDAovJ4NXV8TPrZrbm9ZvpXvVObbhLOqXk93i-x6kWV0Zdw1lCWv6vaSMM-9m0OtsOgxpNbdIsOTH9IXlpgu1GirvHn7LW8dZ3ZVZXSESua3Fr_KVDuKXwOsYeZXyzNq2r2SOj354dpPKkPjRhBOj56JReRuxU5YJa6IKRpIkbTnCetKASWYKZ3uqNtA5MgL3GXjx3kUq3KmR0h3uV0J1y8g3rwrfbzinod2f_70UbIYuybIi2UXO-TAM833g81kEcOiPbrgmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ae1b8230.mp4?token=U3d4IjmmErz-czvy3-v8soCg_siFVK8lv6hU1DPAMZg2UzhG8tGIJ69n-WnOGtcuky_NyPTUYCyLeDAovJ4NXV8TPrZrbm9ZvpXvVObbhLOqXk93i-x6kWV0Zdw1lCWv6vaSMM-9m0OtsOgxpNbdIsOTH9IXlpgu1GirvHn7LW8dZ3ZVZXSESua3Fr_KVDuKXwOsYeZXyzNq2r2SOj354dpPKkPjRhBOj56JReRuxU5YJa6IKRpIkbTnCetKASWYKZ3uqNtA5MgL3GXjx3kUq3KmR0h3uV0J1y8g3rwrfbzinod2f_70UbIYuybIi2UXO-TAM833g81kEcOiPbrgmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آزاده اخلاقی همسر محسن نامجو:
بی‌ناموس تو که چهارتا ورقه گرفتی دستت گفتی دارم میرم همین سرکوچه تو آمریکا پرینت بگیرم، تو فرودگاه امام چیکار میکنی؟ چرا چمدون من رو اصلا بردی؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70859" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70858">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70858" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70858" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70857">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ_2_YTPJPC6IypvNFg3qwQtrPcp6zHVqC7LfoJuq5FGeN_vAICTVofkH-pH-KbKnAVtu-zXcnXP2vjEYR5XGr0VM_lay9RVz8rPIyz7TW9bNMysW_o0bDArMK1CouYszymHitiyW1ju_yP9rXxyrs2CpwGZT-7bUMoHSL-vQq94WRWpSiGev7DprTbEkHZZqlMC5AC6rYhkCAunAGl7bncm7rGhsaQ-hRZLlrUOeRIMFxLXTSZbOCU6ReAUAiuq-mtkLoLmIPlQkjPdCM-yx1XYj1mhllOhUuJKqoE4QgwCbYoJ2Qb8Qbj4tU_4A12Dmtbh-6Fmm99T_yHATtY_hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آرسنال
🆚
استون ویلا
رایو وایکانو
🆚
لیدز یونایتد
رم
🆚
لچه
بولونیا
🆚
آتالانتا
ختافه
🆚
اوساسونا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70857" target="_blank">📅 12:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70856">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=pitBHn4knwC3s907B7x4yyEF5e-XTfBatkeWO7OipT4fBCeyeQeSBofjqcNfrap2qlk9FfNuZ9Cxtj6GYJzpdWUqZ6mAVbXCyzIo6uDz69d31gxtdNhiKloqKdFB_Es_TeIXzWCyFBx1JaGUBv0Nor4aEu7lYwVClNM8S0P4Q0B9DhKezuYWYRuiqEtBkQZrC4Zl6PWigh3ShnSLRUFWgjPhPwKG9z5HJSZs-oKJh5553lYg2V-sCqKNyVf3Z9__2RKU7RgOrC8x5sx39YkeRz3zoUoyludxoyYKZvisVbyude9n0pugJgs3vo76hycVhwGo-CCZFPOGdQh4e14Otw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/862d93bdfa.mp4?token=pitBHn4knwC3s907B7x4yyEF5e-XTfBatkeWO7OipT4fBCeyeQeSBofjqcNfrap2qlk9FfNuZ9Cxtj6GYJzpdWUqZ6mAVbXCyzIo6uDz69d31gxtdNhiKloqKdFB_Es_TeIXzWCyFBx1JaGUBv0Nor4aEu7lYwVClNM8S0P4Q0B9DhKezuYWYRuiqEtBkQZrC4Zl6PWigh3ShnSLRUFWgjPhPwKG9z5HJSZs-oKJh5553lYg2V-sCqKNyVf3Z9__2RKU7RgOrC8x5sx39YkeRz3zoUoyludxoyYKZvisVbyude9n0pugJgs3vo76hycVhwGo-CCZFPOGdQh4e14Otw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای ایشون که داره وایرال میشه:
با این شرایطِ گرونی، هیچ دلیلی نداره که شما به دختر مردم غذای مفتی بدی.
اصلا به حرف کساییم که میگن مردایی که پول میگیرن پرنسسن و لَنگن گوش ندین.
خیلی از دخترا بخاطر اینکه حوصلشون سر میره با شما میان بیرون و یه غذا میخورن، پس دنگتونو بگیرین.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70856" target="_blank">📅 11:32 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70855">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=EDcZFBS8R1p66hyt6-yCvljL94J8yWOtXfkDx8I8oWOBPl0jNIfz71EX7H2G-5LqP6i9q05WNaatDZmKZnvT-Kr67MDv-KnXaoOGog3pPLuSX8eUu01AnPQfZE83GV8PtLnzHeTtMph-z-ZQuiUYGQEO335VBJmPafAk0Ib6xilYIXhkwIOdS59wQj5Wy7-XW1eRknLlsZZcM1fqDu-ulxYirc6O0fMLGmnCOtjdyetXQKXg2I2A9OZGytH0QNV9Y1dp5kk2D8obxkh50_QtAvqrMK7i-n5Lupak11Pkoky1I_cJxKk-kLO5OSYMh7eBLCRVNsRqA3TzB8mPh5mTBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553aa7e97e.mp4?token=EDcZFBS8R1p66hyt6-yCvljL94J8yWOtXfkDx8I8oWOBPl0jNIfz71EX7H2G-5LqP6i9q05WNaatDZmKZnvT-Kr67MDv-KnXaoOGog3pPLuSX8eUu01AnPQfZE83GV8PtLnzHeTtMph-z-ZQuiUYGQEO335VBJmPafAk0Ib6xilYIXhkwIOdS59wQj5Wy7-XW1eRknLlsZZcM1fqDu-ulxYirc6O0fMLGmnCOtjdyetXQKXg2I2A9OZGytH0QNV9Y1dp5kk2D8obxkh50_QtAvqrMK7i-n5Lupak11Pkoky1I_cJxKk-kLO5OSYMh7eBLCRVNsRqA3TzB8mPh5mTBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وایرال شده از طرفدار حکومت با پوششی جالب که میگه:
آقا فکر کنید شعب ابی طالب هستیم و محاصره مون کردن
این محاصره از شعب ابی طالب سخت تر نیست که
ما مذاکره نداریم و آمریکا هیچ غلطی نمیتونه بکنه
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70855" target="_blank">📅 11:02 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70854">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=pcOyDf6gf17g4MXJfVj_1BiqcbtmMsEYNM2WDoS872LgzvpK94-cxUl0q7mqDqWZ0pdGxcu0Co_NSD5hJyDA1XJ74jwf2YOw9Mn3K6IpO4UDQCHvieRPAX6LXgSG5FaCrHYjNGI2iinS4eS5ds0Mwj47r-XAiuqu_tf9LR3Xp7Jee3Ne071WRZso7K-oJe9x_-EeMwMU6RybFDG-IJeXi14EEHz5LqG6-jokaNiTHLKYbIxxFQAoZRQMxr5fj_sY0IzgTuME7lA3clvOg6T2nLDu9J7-97r0qpAM5r7i_eNtTCl6GFA0FmIG_-kINhAcUXDioQ080aGO0Z2b8Uwz3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10096c1b11.mp4?token=pcOyDf6gf17g4MXJfVj_1BiqcbtmMsEYNM2WDoS872LgzvpK94-cxUl0q7mqDqWZ0pdGxcu0Co_NSD5hJyDA1XJ74jwf2YOw9Mn3K6IpO4UDQCHvieRPAX6LXgSG5FaCrHYjNGI2iinS4eS5ds0Mwj47r-XAiuqu_tf9LR3Xp7Jee3Ne071WRZso7K-oJe9x_-EeMwMU6RybFDG-IJeXi14EEHz5LqG6-jokaNiTHLKYbIxxFQAoZRQMxr5fj_sY0IzgTuME7lA3clvOg6T2nLDu9J7-97r0qpAM5r7i_eNtTCl6GFA0FmIG_-kINhAcUXDioQ080aGO0Z2b8Uwz3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ درباره ایران:
رهبرانشان از میان رفته‌اند.
تمام... خب، تمام تجهیزات ضدهوایی‌شان، منظورم این است که همگی نابود شده‌اند.
آن‌ها آدم‌های سرسختی هستند؛ آدم‌های باهوشی هستند. اما... خب، بسیار شرورند.
تا سه ماه پیش، پنجاه و دو هزار معترض را کشتند و متأسفانه، شمار بسیار زیادی را هم به آن فهرست افزوده‌اند. حتی سراغ کسانی که معترض هم نیستند می‌روند؛ به خانه‌هایشان هجوم می‌برند، آن‌ها را با خود می‌برند و به ضرب گلوله می‌کشند.
خب، این‌ها آدم‌هایی بسیار خشن و شرور هستند و اگر سلاح هسته‌ای در اختیار داشتند، اسرائیل نابود می‌شد.
اگر من رئیس‌جمهور نبودم، اسرائیل از بین رفته بود. دیگر اسرائیلی وجود نداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70854" target="_blank">📅 10:41 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70853">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFiOSY5su-suOY98nYgG-PGsBlhUHE5h3szFl5uOD0Z_5lk0VZOXH1oaqaLZLU5goSA0TjQN1H3EBUYtvS2S-LF1jmlhA7G2PKFv1lhJYfdQ37pVleCyduZHhoGutLnJMhvvkptdZ_NeEd-lEGN2Dzhj0onxOBZufJ7X95o8np_L9AB-t3Lsj_KdhJwenCtg_BM7rCQrCRAHMZnvNcEHebmao-84ECzh-pI7zj_BcOTwZ03_x2CQ72xLQ3KzbS1iz7QOd-ZvhoCiiN1KifdyTwaFn90qfcvia71deFknOuaCWAQIhiagSVI4gEbcOAPBDHkICeKzRbjVk7az7cJB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
〰️
سنتکام:
❌
ادعا: سپاه پاسداران انقلاب اسلامی ایران در بیانیه‌ای اخیر مدعی شد که حملات نیروهای آمریکایی برای جلوگیری از مین‌گذاری سپاه در تنگه هرمز، «اقدامی تجاوزکارانه» بوده است. این ادعا کاملاً نادرست است.
✔️
واقعیت: نیروهای آمریکایی علیه یگان‌های مین‌گذار سپاه که در تنگه هرمز تهدیدی قریب‌الوقوع ایجاد کرده بودند، دست به اقدامی محدود و دقیق زدند. در واقع، ایران عامل ایجاد این تهدید بود و ارتش ایالات متحده برای حفاظت از دریانوردان غیرنظامی، کشتی‌های تجاری و جریان آزاد تجارت جهانی، آن تهدید را خنثی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70853" target="_blank">📅 10:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70852">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=uK_izMDy-O5DJQwmNfZEO-fTb4wCpP_MhxdaUdbWCAdNyb8rz4pxKvwO7XOzGf7LaRSxu750z5QRC-EJcdGKGtHsg6GqGXbFnpvfmO-yA1LGKgYrzhofKtPjPAJe3JjWO0cm2WDnUBiszyKpUX82wS39K7Z1fiSQj7uSAP7aW0FaezqJ-Dow4RjguThDUQTXHWK9tl0AYUnhQYKVW_b2rplx0BitPq8bV_KAyh3n1ELp6z7-fU_0wJgcBlrmucsIMH4kwo8Xm0vnn2dFyep6FB2H-F2EhSjrL0kWuuA7o8QS5PEm6omoAjKXo04v5m1t3q1cQlgcNMfSHVluXokmeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aef58f7de4.mp4?token=uK_izMDy-O5DJQwmNfZEO-fTb4wCpP_MhxdaUdbWCAdNyb8rz4pxKvwO7XOzGf7LaRSxu750z5QRC-EJcdGKGtHsg6GqGXbFnpvfmO-yA1LGKgYrzhofKtPjPAJe3JjWO0cm2WDnUBiszyKpUX82wS39K7Z1fiSQj7uSAP7aW0FaezqJ-Dow4RjguThDUQTXHWK9tl0AYUnhQYKVW_b2rplx0BitPq8bV_KAyh3n1ELp6z7-fU_0wJgcBlrmucsIMH4kwo8Xm0vnn2dFyep6FB2H-F2EhSjrL0kWuuA7o8QS5PEm6omoAjKXo04v5m1t3q1cQlgcNMfSHVluXokmeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سرهنگ خلبان بهمن فرقانی، جانشین فرمانده پایگاه چهارم شکاری دزفول :
زمان جنگ، آخوند رسول منتجب‌نیا به پایگاه ما آمد و پیشنهاد داد برای بستن تنگه هرمز، فاصله عمان تا ساحل ایران را با قایق‌های موتوری با طناب به هم دیگه ببندیم تا عرض تنگه بسته بشه
به ریشش خندیدم و گفتم: «چرا مزخرف می‌گویی؟»
زیرآبم را زد و از نیروی هوایی اخراجم کرد!"
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70852" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70851">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=aQVjb3d8jDfSvH1sTAMVIJnt1c-grMmG7Q2vQ13jUzbi5_RKgLs6eqtH5tdnBk4vYyw4igeJTAa9Rcz0lMyI9OCGXah1Moe6EDNZxVIijJvg_8ODcw8T-rmIma-8zDG8ZBuDlxA1kmJCGkjJLxtEQd_P87tVOu2PV70yVlxVG2nq4ipNAG_OJ4E1NyZ0ldX2hvJW-WzqGL68gqVGO8Njo0NQJdF19ZaSfKP_HJvhpIJuI_trlFStN226_wobr3jviKteYrh8IyFVndi6LAMACsLke4aBGzAK1xGMk2Z3uzo7hRJVJxNV9QQZf99HgeQ9Ej6pieqi-F5QRXO1ul3YyIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8771a258e.mp4?token=aQVjb3d8jDfSvH1sTAMVIJnt1c-grMmG7Q2vQ13jUzbi5_RKgLs6eqtH5tdnBk4vYyw4igeJTAa9Rcz0lMyI9OCGXah1Moe6EDNZxVIijJvg_8ODcw8T-rmIma-8zDG8ZBuDlxA1kmJCGkjJLxtEQd_P87tVOu2PV70yVlxVG2nq4ipNAG_OJ4E1NyZ0ldX2hvJW-WzqGL68gqVGO8Njo0NQJdF19ZaSfKP_HJvhpIJuI_trlFStN226_wobr3jviKteYrh8IyFVndi6LAMACsLke4aBGzAK1xGMk2Z3uzo7hRJVJxNV9QQZf99HgeQ9Ej6pieqi-F5QRXO1ul3YyIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یک سرهنگ فراجا:
متأسفانه مدتی عده‌ای از مراجعه کنندگان و یا به تعبیری ارباب رجوع به ما مراجعه می‌کنند و در خصوص گرانی‌ها معترض‌اند و هر بار که به ما مراجعه فکر می‌کنند، فکر می‌کنند که مسبب و اینکه ما از دست ما کاری بر می‌آید و نمی‌توانیم برایشان انجام بدهیم.
آقایون مسئول، عزیزان مسئول، به خدا گرانی بیداد می‌کند. آقای برادر تعزیرات، آقای بازرسی کننده، آقای بازرس اتحادیه، به خدا با کت و شلوار اتو شده و موهای ژل زده و عینک دودی نمی‌توان با فساد مبارزه کرد.
آقا یه جای کارو درست کنید که یه جای دیگر را بخواهید گوش‌نظر بدید. تو رو به خدا، تو رو به هر کسی که می‌پرستید وضعیت معیشت مردم را درست کنید.
فکر می‌کنند به عنوان پلیس ما از جای دیگه درآمد داریم، از جای دیگه خرید می‌کنیم. به خدا این چنین نیست. ما هم مثل همه شماها از همین فروشگاه‌ها خرید می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70851" target="_blank">📅 09:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78504efb49.mp4?token=YT5S7jYwduk1t0G4OkZQf2tej2lfqyO1BMtfD2tq8I0Z5qsaHdYAqnCkFH1T5YuxMdq0aVYGQyJhIquVo3eMUH54rwp9cUbmCbX17WH4Qk92vVbKks2tp2fH89PVH9qrESxfqtwkvGbCeC2Hwq35JU1awa6zljgbTk4Vbwtqk1mqqKwEygfb0hnuRcIMBd6GbBHy9dIiSpFP1V_-31tDUGp3h-YrwUIu40x1sqMcrin2R6hpBEldqCenNVnpRO3JWhgiKYs0j38uA9PdmL0AeNiZbkAe2ZhFOqh3nGYizTsvrIIxr6L6EU_lQqX-R0i7H1kW3FK04QqKddyilrhptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78504efb49.mp4?token=YT5S7jYwduk1t0G4OkZQf2tej2lfqyO1BMtfD2tq8I0Z5qsaHdYAqnCkFH1T5YuxMdq0aVYGQyJhIquVo3eMUH54rwp9cUbmCbX17WH4Qk92vVbKks2tp2fH89PVH9qrESxfqtwkvGbCeC2Hwq35JU1awa6zljgbTk4Vbwtqk1mqqKwEygfb0hnuRcIMBd6GbBHy9dIiSpFP1V_-31tDUGp3h-YrwUIu40x1sqMcrin2R6hpBEldqCenNVnpRO3JWhgiKYs0j38uA9PdmL0AeNiZbkAe2ZhFOqh3nGYizTsvrIIxr6L6EU_lQqX-R0i7H1kW3FK04QqKddyilrhptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل به فارسی:
جمهوری اسلامی و سپاه پاسداران سال‌هاست که ثروت و منابع ملی ایران را صرف تروریسم و جنگ‌افروزی می‌کنند، در حالی که سهم مردم از این ثروت، ایستادن در صف‌های طولانی و بحران کمبود بنزین است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70850" target="_blank">📅 09:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70849" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70849" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70848">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPnDQSlE1KjGuyzCMzD4ojf_6j_5P3t12T0pRLS8JE0EnkX9dI567FBnVf77m3Bs53CrjR3DuCHhgcE7ff8KbkvAmapcI1uy0aZTAdebJQ42Bvxaw1e0WjZyPOKhzWRosnOfB12OR_aLYTB13nBhhEemQFdhqALjjS-E_qIrFz_Qkqgyjpe29x55ylxkTPzk3UFT9qUK8g-Hd0FC6eMXcLm3u82vRHQPC5or3PHz5bLntHnrW8QziF0OQ_ZooAVoUamYjQ87Iw6Keic1ULxcfFz0iYYc2ASdNu_MWAhtgglGpv7mog3D9yPInwa06OxCcuIkiqS3DOXLhOO3BA7nmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70848" target="_blank">📅 02:06 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70847">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
نایا:حملات موشکی به قطر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70847" target="_blank">📅 01:50 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70846">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-text">یادآوری: علی خامنه‌ای، دیکتاتور و بزرگترین جلادِ وقتِ خاورمیانه در ساعت ۹:۳۰ دقیقه صبحِ ۹ اسفند ۱۴۰۴ توسط ارتش اسرائیل و آمریکا، تکه تکه و تجزیه شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70846" target="_blank">📅 01:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70845">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بچه ها بزارید منم این وسط یچیزیو یادآوری کنم
👉
#hjAly‌</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/70845" target="_blank">📅 01:48 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70844">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMr. NOBODY</strong></div>
<div class="tg-text">خواست پاتریوت رو با لهجله بیریتیش بگه اذیتش نکنین</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70844" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70843">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɴᴀᴢɪ</strong></div>
<div class="tg-text">امیر پهن مغز پتریوت چیه؟</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70843" target="_blank">📅 01:47 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70842">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYxvZHOrq2eJeuAer44z3MhLs0WNc5NBCNJ5BDdAUZ9SjPpXsAQIf9NiAo9KR60QgJKsfKnrixfxCQbIFFtSPm-nhHUj4LpYy9cdX0UWL6OBeY7MR0IJx-ZHho0-JWv7WbnUAcH3d0mcxj-zV4yMRIm61gsI5lWuPcnhOy76gqrTEhL3GBUKjTuD6-4fSupboECTdzeXiMRmBys8Z7THBvleIn5CxIOP95NMrcNPnTgWtR78r0DUEncHSgUxx0Ki7KiAi7v-3zFk3bfGu3rx6ltvLMxAhkI6G8PwwdTU41p2BRU53VUFpLPl-OXCYF9t-D1-62OPsRoSU8DGInz8FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا برخورد موشکی صورت نگرفته، اکثرا رهگیری شدن #hjAly‌</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/70842" target="_blank">📅 01:45 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70841">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=bp53M5UC_CiR6SzOSmavqdSoir71irlOcY2uZrk7YfvMgQhQLuuva4DNJWNCpg-r4KXxeFc9whAcO_wwXTcwDGt2iZm2kQqH9cqfexJMfe_K4P1npN8b_5JU9GUaZfYKlqBTZceUEHjrwEFT6zrZX1xrO2omvrbSxLjzlvNs8WWFo1AF9Msd1xOO0my_jYNqW2MVDszzUa19xOMPXFgsone9KNpYCsWx88LSPhnGDvsb7keve0nB8Tf8zvtDYrIReUNA2V0pRD_bK8CNKWjX7TA2ctOlv7-ykyW5bsWcmAft-DBrX1ynJbzB_ZKqJWQPy01sN5Jsx0DEvUogXiMBig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f04fa470bb.mp4?token=bp53M5UC_CiR6SzOSmavqdSoir71irlOcY2uZrk7YfvMgQhQLuuva4DNJWNCpg-r4KXxeFc9whAcO_wwXTcwDGt2iZm2kQqH9cqfexJMfe_K4P1npN8b_5JU9GUaZfYKlqBTZceUEHjrwEFT6zrZX1xrO2omvrbSxLjzlvNs8WWFo1AF9Msd1xOO0my_jYNqW2MVDszzUa19xOMPXFgsone9KNpYCsWx88LSPhnGDvsb7keve0nB8Tf8zvtDYrIReUNA2V0pRD_bK8CNKWjX7TA2ctOlv7-ykyW5bsWcmAft-DBrX1ynJbzB_ZKqJWQPy01sN5Jsx0DEvUogXiMBig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رهگیری دو موشک سپاه پاسداران بر فراز اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70841" target="_blank">📅 01:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70840">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن  @News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/70840" target="_blank">📅 01:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70839">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:  از خرم‌آباد صدای انفجار شنیده شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/70839" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70838">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
گزارش ممبرا:
از خرم‌آباد صدای انفجار شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/70838" target="_blank">📅 01:25 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70837">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">صدای انفجار شدید تو خرم‌آباد شنیده شده
#hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70837" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70836">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44471a1938.mp4?token=XneqjkFHPBxEnWTGnabRwRiz03zX2x1QUh33QzVGIK8JZlUbMlPwsoyHUakF8M15IlHg53Ii7i6tAS7jOX_o7Iwg3Nu7hgLPw6jWjHBaA4j-B2SO_MNjpN0FO8u-pX2rm8YP3n_CchQBl_HTA993L0Uiw_-3UqlnFR-XOCpsPF9XATazwz1U5RWXRU70WGsYVIO3bziJFK2WeaJZqd5jYj_6YK-L5Y3ye7wXQPgxjnurWd72Ko3dnXSY6A7hpCUSkpZCaNOPT6LSdPDfaKPCeN9zf5TsYJL5WWFt1fjXoUnAgIhoVMTipCE-V-0kmtrNdZAkhWYZh5p9wE7CsBJMMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44471a1938.mp4?token=XneqjkFHPBxEnWTGnabRwRiz03zX2x1QUh33QzVGIK8JZlUbMlPwsoyHUakF8M15IlHg53Ii7i6tAS7jOX_o7Iwg3Nu7hgLPw6jWjHBaA4j-B2SO_MNjpN0FO8u-pX2rm8YP3n_CchQBl_HTA993L0Uiw_-3UqlnFR-XOCpsPF9XATazwz1U5RWXRU70WGsYVIO3bziJFK2WeaJZqd5jYj_6YK-L5Y3ye7wXQPgxjnurWd72Ko3dnXSY6A7hpCUSkpZCaNOPT6LSdPDfaKPCeN9zf5TsYJL5WWFt1fjXoUnAgIhoVMTipCE-V-0kmtrNdZAkhWYZh5p9wE7CsBJMMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعالیت پدافند در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/70836" target="_blank">📅 01:18 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70835">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خبر متوقف شدن پروازای فرودگاه مهرآباد هم فیکه #hjAly‌</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70835" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70834">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
🚨
منابع عربی:شنیده شدن صدای انفجار در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/70834" target="_blank">📅 01:11 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70833">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🔴
گزارش ها از شلیک موشک از نقاط مختلف کشور به سمت اهداف آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/70833" target="_blank">📅 01:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70832">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب  تلگرام یه‌پا شده روبیکا... #hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/70832" target="_blank">📅 01:07 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70831">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmVGvpk5AtjVeAaK1Xb3GKoY76crZzJ6EajILxH1ME5agLCCaCUiVfM75t-fiwn9885CAh9K-3s-AdAyCtazTdKmP9IZwYZLu-42T-Lm17FF2yGTgFKCWm1lhZlxpxdlTAT51t9pqui8aUCOOckiaa39t2RbZ7RC6YGqeoxQtRTQSjthIl8nt54LuFxCpLrbjcWQobN3bn_STSCOwCpqIQtQxdA9tXHbwy3RB9_-4FxlPe_2TTWgYfM1isUoFr22YYhnrCfM7LJBR8M2uvL6cC-Uk2bMpx-z_MJDFziy6EaYv9edvu90dpB2xHjt-Sf2g4Rmmu_wKKsKi2i4J7wF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست جدید ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/70831" target="_blank">📅 01:05 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70830">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=mz0DOroSeXtIkPSxzfU_thH0wc1A9iRHj0XS-hWXEji1ptVzaWT2h2jWkJk69c1yu-efuboVCLusrim9tVxwt_0mkREsadK6T89x7d4W-4fGjfecSKkyjkezaPwzzYLVmgENzi9VbtW1DwctSN5FFRrMPlxuYqiIKMuRpcSWp5R8rSVq7SbRZ1fYarogZ0NKbvf6JEEX7NY46qI5C0eZudZSuJV-WwssG1DOxJol6A8l-YQ77csJK_2XP_OHPKZbu-qnPJ2U-ytt2EsKTSsw-uT6JigtYZjHa2fYJR9heFo9JDzXCPG43j5hFlKdnQYvFRWFhScFhJDrXKjNb2uTcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e895af3e4.mp4?token=mz0DOroSeXtIkPSxzfU_thH0wc1A9iRHj0XS-hWXEji1ptVzaWT2h2jWkJk69c1yu-efuboVCLusrim9tVxwt_0mkREsadK6T89x7d4W-4fGjfecSKkyjkezaPwzzYLVmgENzi9VbtW1DwctSN5FFRrMPlxuYqiIKMuRpcSWp5R8rSVq7SbRZ1fYarogZ0NKbvf6JEEX7NY46qI5C0eZudZSuJV-WwssG1DOxJol6A8l-YQ77csJK_2XP_OHPKZbu-qnPJ2U-ytt2EsKTSsw-uT6JigtYZjHa2fYJR9heFo9JDzXCPG43j5hFlKdnQYvFRWFhScFhJDrXKjNb2uTcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش ها از شلیک موشک از سایت موشکی بیدگنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70830" target="_blank">📅 00:58 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70829">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">همه‌ی خبرایی که رسانه‌ها بخاطر ویو گرفتن به ترامپ نسبت می‌دن فیکه، هیچی نگفته درمورد حملات امشب
تلگرام یه‌پا شده روبیکا...
#hjAly‌</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70829" target="_blank">📅 00:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70828">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFDGQ4c4cUGm5K3jeI8mQKkBO6Ejpg2lFZVOg42IfN_MBiL4KTZDoMbE31BYVtdG9YY5R2rs2jrYHWodJ4gUbWwuADTlyIwlE6ucTema1QxgamWWeKtjIxKdRy12Wo5voo6ri5rtRxauktoyWsR-QDc_dz9s_4NJrX7m8_TMVgWrB-PEVFPIyk51ujqCmi8YNJxZPY_bwqgQzP_rk9menHdOktt3_j6XvMfwcW2QIX1X9yg7gYBlNTGfKFuXLP7X_Hl9aEQkqcl2BAr4AVc9HYnRl-rZRMTb1dttQuKma8WJGhvgNpEUtlQhDcWmxgVugMwcMXGinHTEhN2Ntr-EpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
ابراهیم عزیزی:
یک بار دیگر اراده ما را بیازمایید و بهایی سنگین‌تر بپردازید.
انتقام در راه است؛
فقط فرار کنید!
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/70828" target="_blank">📅 00:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70827">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=vqsIdceH0df-JDmL3_uZ8c35RmdmS2l6jx9jAoGn0fWR_0ZKZhLYKjCfDsaLXV4W64wgBfO1cKeb7fQ-fUyCO0a2KI8g1-eCNRwSsKPz2vLt1TB4TB4IEAcCEQUYU_g1SEre1vvQrkymu_HrkmxMnOR05lMfqnBA6H9XuonsYzkp5eeo8nWAHYgusuKjJuRHXkjew_xyxcTygee5qMP_vkfMMaw-QAv-Tu9JT4XqqPRjxSHkYYefGTIwVNp_Oc1Ck_35tIlEC_H6caApnu-KTc3Mn4BBjO0GvUpZfC3A8BsgKyG35gZ-N88eK4-80PelroZwQCQLzHej-xbN6PgNU240vhCJn7vU65C5kLgAhNpqPL_Nxy2_KrwqN9TjxZZOdMmWQDaqTGMtTq3djGshJ_iF1M0Br7Sg1EuQraGAr2GHMsq9A7O-IVrQKLrQlmlpe-prcm49GIWm6bg5ovW24tsa8_uEqmibApZwvIpdCEBylUT13Gu5kcJFzWNesLu6IvHMhoKzqkgfOXJ3EeJn5zSkmVDSBRH2F2IxmzlwwuSduKn6Xm67M6ECcE7MMCMalTgmDRiHmhM0qmM8_B7LXBZQOXRWEJhkaVP7bf1CfwSBgX8j6OSZqNn5U10Z6k7R3-ixQvT27K_BoAoOwjfDkP02Le8UjUgUhJ0ddZjENxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06c56b11a.mp4?token=vqsIdceH0df-JDmL3_uZ8c35RmdmS2l6jx9jAoGn0fWR_0ZKZhLYKjCfDsaLXV4W64wgBfO1cKeb7fQ-fUyCO0a2KI8g1-eCNRwSsKPz2vLt1TB4TB4IEAcCEQUYU_g1SEre1vvQrkymu_HrkmxMnOR05lMfqnBA6H9XuonsYzkp5eeo8nWAHYgusuKjJuRHXkjew_xyxcTygee5qMP_vkfMMaw-QAv-Tu9JT4XqqPRjxSHkYYefGTIwVNp_Oc1Ck_35tIlEC_H6caApnu-KTc3Mn4BBjO0GvUpZfC3A8BsgKyG35gZ-N88eK4-80PelroZwQCQLzHej-xbN6PgNU240vhCJn7vU65C5kLgAhNpqPL_Nxy2_KrwqN9TjxZZOdMmWQDaqTGMtTq3djGshJ_iF1M0Br7Sg1EuQraGAr2GHMsq9A7O-IVrQKLrQlmlpe-prcm49GIWm6bg5ovW24tsa8_uEqmibApZwvIpdCEBylUT13Gu5kcJFzWNesLu6IvHMhoKzqkgfOXJ3EeJn5zSkmVDSBRH2F2IxmzlwwuSduKn6Xm67M6ECcE7MMCMalTgmDRiHmhM0qmM8_B7LXBZQOXRWEJhkaVP7bf1CfwSBgX8j6OSZqNn5U10Z6k7R3-ixQvT27K_BoAoOwjfDkP02Le8UjUgUhJ0ddZjENxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
#فوری
؛نتانیاهو درباره ایران:
من این رژیم را به زانو درخواهم آورد. به این امر متعهد هستم. این کار شدنی است.
آن‌ها بسیار ضعیف‌تر از گذشته شده‌اند و در موقعیتی متزلزل قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70827" target="_blank">📅 00:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70826">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
آن‌ها از برنامه هسته‌ای دست نکشیده‌اند. ما آن را به عقب راندیم، اما آن‌ها کاملاً قصد دارند برنامه هسته‌ای خود را برای تولید بمب‌های اتمی از سر بگیرند.
بنابراین، این تهدید از بین نرفته است. ما این سرطان، این غده سرطانی را ریشه‌کن کردیم. می‌دانید که اگر سرطان را ریشه‌کن نکنید، می‌میرید. این همان کاری بود که ما انجام دادیم.
اما سرطان ممکن است دچار متاستاز (گسترش) شود و در صورت بروز متاستاز، می‌تواند دوباره به تهدیدی تازه و بسیار جدی تبدیل گردد.
ایران می‌خواهد برنامه هسته‌ای خود را از سر بگیرد.
من پیش‌تر یک بار مانع این کار آن‌ها شدم و تا زمانی که نخست‌وزیر باشم، مانع انجام آن خواهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70826" target="_blank">📅 00:42 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70825">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AX0wmEebBw2BUy79YxBXHft7H4flFDE7OhHdvkkbGX5obx0642c2yAWgaoap9mqVz-aji2kEGldMzEubRvRqiMMcXtp0D1HkRmSZLbptrggB52nY03Z0E788p0aWNEw5u9mjntYsaPtIioBmVKQwi-Q1ncP61ZwX4t-2ib_pzOAbyzyXGoZhCJ1ukrDUH_aMBrtUQN2LI_MGkaENCwwlgv_LGY0lwb-LulVuv0ViBKBCT5Maq3CuuGh3938lV0xdN4tRo3KGqWESFyxvOQBs-lJn4Yx0iKZITNcfgy2moySgIRGGMQ_ZB_HsY0LJBTRWqNSaATFTDLJo_XlPfjHFUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
سخنگوی سپاه پاسداران انقلاب اسلامی:
این اقدام، یک خطای راهبردی و مهلک از سوی دولت ترامپ در چارچوب جنگ اقتصادی است؛ اشتباهی که کفه ترازو را به زیان طراحان آن تغییر خواهد داد و هزینه‌های سنگینی در پی خواهد داشت.
دشمن پیامدهای این محاسبات نادرست را در هر دو عرصه اقتصادی و نظامی متحمل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/70825" target="_blank">📅 00:37 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70824">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
مجدد صدای انفجار در جزیره لارک شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/70824" target="_blank">📅 00:23 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70823">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری؛سپاه پاسداران:   تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد  @News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/70823" target="_blank">📅 23:48 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70822">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
#فوری
؛سپاه پاسداران:
تجاوز دشمن تروریست در جزیره لارک همراه با تنبیه متجاوز پاسخ داده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/70822" target="_blank">📅 23:40 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70820">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4ZVbMtu40-2FiguZsScv6_ASMU74Q79GuQiUReLKBSbjQvQLkuZd50XMWDmxQRKdwXi2sBDA66R7802CYkQboLSeyBbNxeuLv7vmmRARLRz7Pqx1Ju5CI3stPMy0YI72yEKp8TFhXscSNpG3b_ZjCOv66uEbw7sMSg8mh3ElTymfQNpmmKRZMxiK-NNmCrR8AcqjXAki1I3bOSuOFCfoQo419j0iMEn9QLAVW-7FMtiFZAqoy-x873d1D9s06MAoWyggmikkGIcny-daHMvFRtVUBEBYXpTuwGpxlDyt7KLIzAF2WvBoeooIsCHM7Q5-ea8hSIr8cPsPBk2kf4kxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d778b593.mp4?token=GqD3lZY-3ARK_4E0Y0pqcBEJtSC06dNPxe0a0lvqM8q0MO50_fJ4ruBeiTKg2jNT-Ichf0RdaqoDDs8CseMzffmfaGaGTuKQiYTM6-EA3MiGi7c1RwiAvJFuzj5R6mG-WIM9z27ljxzKjLchdbhqzlhd9J7BLOf6K5e4_zzZtXzCMtvh87nmLJ8Mk-vKIbU-DjwdNOkxJjKkbcdXzqvJo1I15dB1achxxnA3eazxW2ddcAncU_VAlx4MsCp7Pu6zZ66Jevkhlv4Tp8GcasSwhvuFeqX8NQ3MUsQaP1e4xn43xIl9Krs6q02qYWRTyRyMOjPHGPGvZ9dj8DfCNEbfFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d778b593.mp4?token=GqD3lZY-3ARK_4E0Y0pqcBEJtSC06dNPxe0a0lvqM8q0MO50_fJ4ruBeiTKg2jNT-Ichf0RdaqoDDs8CseMzffmfaGaGTuKQiYTM6-EA3MiGi7c1RwiAvJFuzj5R6mG-WIM9z27ljxzKjLchdbhqzlhd9J7BLOf6K5e4_zzZtXzCMtvh87nmLJ8Mk-vKIbU-DjwdNOkxJjKkbcdXzqvJo1I15dB1achxxnA3eazxW2ddcAncU_VAlx4MsCp7Pu6zZ66Jevkhlv4Tp8GcasSwhvuFeqX8NQ3MUsQaP1e4xn43xIl9Krs6q02qYWRTyRyMOjPHGPGvZ9dj8DfCNEbfFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
یه نمایشگاه عراقی اومده پژو پارس گذاشته برای فروش؛
و اما کامنت مردم همیشه در صحنه :))
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/70820" target="_blank">📅 23:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70819">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
#فووری؛ باراک راوید به نقل از مقام امریکایی: امریکا امروز به دو پرتابگر ایرانی در جزیره لارک حمله کرد  نیروهای سپاه پاسداران سعی داشتن موشک‌های حامل مین دریایی به تنگه هرمز شلیک کنند که قبل از پرتاب توسط امریکا منهدم شدن @News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/70819" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70818">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/URV-_29hJBocr9sjPzu7UZbLtfG7T9X--Vo7JZXcp5HwUTOQ5OBWgEGzSsiN_oOFbKdxwPVihLAceghatPcZGINf2fBgqjeA9QpSPitVXVlzIq4jkMDPYq2_uMzfCJTd-IcoHZ1gPYIXVNMycK03e7ozAXiKfzjamw128xRTuBnZdGXoDTUtolXmNdQrjXrHkthMaRuPX9b1HG9vjxcM7HvRT63Gnsa6BrbfwxoHbgMxdsKqriIIjPV2HSfwVLGuBiZyQRjPE-RtwrpYMsZlJv5SYOwFtx6SAKEwFOxgzdOOihCDM9ShY2JLPcNWaGW1lcJFOJiHXJeZwtTrRE6GhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووری
؛ باراک راوید به نقل از مقام امریکایی: امریکا امروز به دو پرتابگر ایرانی در جزیره لارک حمله کرد
نیروهای سپاه پاسداران سعی داشتن موشک‌های حامل مین دریایی به تنگه هرمز شلیک کنند که قبل از پرتاب توسط امریکا منهدم شدن
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/70818" target="_blank">📅 23:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70817">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6826005e4.mp4?token=gja56Zzobfh1esPXS-QPOeEWhdkwT1MOQYd8HCHW6ktngeULB6rgViJp5FdkWyt6zZrWlKMPEszbQbNuW-phHTPSaZOzf80_zhnPGiKeOV0FJK1mgCMNnwWtH2dUOlyD76yR75dcbbf9ANykYhxsYVofhOFwwz03O0fDZTZcTEYknoHwhOnOjq5T5PmFDcYIVRYM2F52pVVeFnqEXIZvZakuA9SeKS9SNOiMpiBSVnjwUhPxhobkYQEFbfT1ptLO_T8rJl8Ny9_5F6jubBTCn9z7F_acszF78lMHt8-RdcQT73mfv1NWS0D_EvbTt-ZjuPftfLyTTy4y7y1uxZiTPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6826005e4.mp4?token=gja56Zzobfh1esPXS-QPOeEWhdkwT1MOQYd8HCHW6ktngeULB6rgViJp5FdkWyt6zZrWlKMPEszbQbNuW-phHTPSaZOzf80_zhnPGiKeOV0FJK1mgCMNnwWtH2dUOlyD76yR75dcbbf9ANykYhxsYVofhOFwwz03O0fDZTZcTEYknoHwhOnOjq5T5PmFDcYIVRYM2F52pVVeFnqEXIZvZakuA9SeKS9SNOiMpiBSVnjwUhPxhobkYQEFbfT1ptLO_T8rJl8Ny9_5F6jubBTCn9z7F_acszF78lMHt8-RdcQT73mfv1NWS0D_EvbTt-ZjuPftfLyTTy4y7y1uxZiTPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
محسن نامجو در کنسرت نیویورک، شانزده شهریور نود و دو
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/70817" target="_blank">📅 23:02 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70816">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d075c961c.mp4?token=hQZuBTgy9ZqmqBtPnqKYAyhH6_qtl8PPW5WIU2G4jT9rhDkyBxdQZTEj6nkmXeqjwlOHy5TCJZ3_4sBXxDFf4t9P2CmvTORN7_BXKg9G_V5TtFgNQNDY592qEfQQCOLEI7YTRe1Li43iEkMsZSpyVNqYinB6wYo6-yD3G1BumhIfHvvSsJCZeV5NsliClsTLwU9MXPykNK2vdqGFboLtZDhwxTj56eUaequfP8mw0c6fC2z-J6NWFAMltioxSe6YUWotAlWGh04zDf6D12XDYwxobsLazhK8QNrR1fZDXZXwcuqdA4N7HWL9HaqLryZ7QzYezTxYK_y1V9jjNSvVljW8stukBbyQt2K_GlhxAcCwR-ywjvFcnc_PnMNM7WqcJ8w-_CQd8y4X7tL54C5EJjYRFV_n4bo2CE-tjuzjCWwP7W1if9TZ_dCFb7yGRJPBhKTN3sgcdt_Y1S1Nuet-_vNZmOoUWl78ELY11ev6iXcFvltX5K09ACq4g_AIiDBuUMNbZzjSIRobV_HSRR0hDsWgSwQtR56UYeVS0jMxecKYMhKDW54ueh5PmkUv3-dcw_ehQXztgZ_JjvpdFV9r7hxoRh7OcQ3vDoatFLdKyMqKUWhtIkOI3vpxsBzP4QkXEFyKLAmNaWF_D46DizBve39Mw0vaen-c4s3xLTak_Ks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d075c961c.mp4?token=hQZuBTgy9ZqmqBtPnqKYAyhH6_qtl8PPW5WIU2G4jT9rhDkyBxdQZTEj6nkmXeqjwlOHy5TCJZ3_4sBXxDFf4t9P2CmvTORN7_BXKg9G_V5TtFgNQNDY592qEfQQCOLEI7YTRe1Li43iEkMsZSpyVNqYinB6wYo6-yD3G1BumhIfHvvSsJCZeV5NsliClsTLwU9MXPykNK2vdqGFboLtZDhwxTj56eUaequfP8mw0c6fC2z-J6NWFAMltioxSe6YUWotAlWGh04zDf6D12XDYwxobsLazhK8QNrR1fZDXZXwcuqdA4N7HWL9HaqLryZ7QzYezTxYK_y1V9jjNSvVljW8stukBbyQt2K_GlhxAcCwR-ywjvFcnc_PnMNM7WqcJ8w-_CQd8y4X7tL54C5EJjYRFV_n4bo2CE-tjuzjCWwP7W1if9TZ_dCFb7yGRJPBhKTN3sgcdt_Y1S1Nuet-_vNZmOoUWl78ELY11ev6iXcFvltX5K09ACq4g_AIiDBuUMNbZzjSIRobV_HSRR0hDsWgSwQtR56UYeVS0jMxecKYMhKDW54ueh5PmkUv3-dcw_ehQXztgZ_JjvpdFV9r7hxoRh7OcQ3vDoatFLdKyMqKUWhtIkOI3vpxsBzP4QkXEFyKLAmNaWF_D46DizBve39Mw0vaen-c4s3xLTak_Ks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇵
🇨🇳
تصاویر بالگرد چینی از  سرچشمه سیلاب مرگبار در مرز چین و نپال
یک بالگرد چینی خود را به نقطه‌ای رساند که در آن یک یخچال طبیعی فروپاشیده و حجم عظیمی از آب آزاد شده بود.
این حجم آب با حرکت به سمت نپال، خسارات گسترده‌ای بر جای گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/70816" target="_blank">📅 22:15 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70813">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iW6r8imFnk53GitFKnZHexFLdt3aPs-hQW6RZZunYdfeFjSEy260Ic-SFEbSFJSszQT3qOV7SwpNKdhaSlsmjB7NlTOS9UuCpFluclym-7-A8muP75w1hbPU5V8tAcGx6M0_3-zLFKKg0mPrTJM-6WYqA42cplD4n9I7IJL7_ylegff54dXMmaPaYTjDmCjeS_5l0V08L66oGo1RM3y-Xj1fBZ_63wfkGqyxJKuXl6vDDnn1QOxQD6ollsWXWLqQGvpQ9-Nxm0AtDCpyK8t_sPZOHAllX-2__y_ZEbMg_e0ut3-34s0-N0JW-7zpnDwE2xklVIpiGYncR13d-Ng8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LstSHHUXiMcUmmdzUbOKah8GCR1nBk9TIcksYCBAvc7YpiLU7SRyA_mhw-RMfPW8lB73jVCSnlygxFyn17BNi92zWMwXR6rj0tafQJBCMekbPgsP4XAJcQ3xZAvS2jsPhPtzbHHPGY39JOOFTsWlBLcVMRUR3HdabVVyNIC2DmNk_R74bDH71jrKoJ4uzHeNC5D1bBTuHK3HzlPFBcg_OBWZOgk_tX0jN13Osjmi6g58HnK5H93C74pgPXfcZ4AvGMfvZ1VxoDpgExh2ngPY3n3pUogakCZCw06aYf9A5FBD8hAz6A1fU9zPOR1AJEEkbI2WrqObtBRkZX9vJZug7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X7xaKQygnwvFGvYc0zB3cloHZHAMFr0NZhuNqBQ2A8CfcaWDh5AZPzDWeOiuwjW_sj6pTbMWBEtbE2_We_BBgAAhRejf_COnkQ2xkJPnxU2uB6JZc_I_W4El9mL6VDOMd5NCF0PebEWqAFUFzp9UTEnFDDw10LSxiYUu4COVvzLZhvlmBE4Ftx4JMwEdl53bzN010xN2aGDl-lD1sqaJ2w9ptZQNRIeuG7gJXC2WhOvZ6wLsce-eB-Z8wo6QVMVncGrpqACAPgDSVNCIsgoMMLPWsZCZWxk7BcJy-arIn-yJy28yOdF5WJFqCezVLIunkCi5nGo853Zx2Bxc6_T7rQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
از کیوت‌ترین عروسک ایران به اسم:
کون‌کش، رونمایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/70813" target="_blank">📅 21:31 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70812">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cedd59487c.mp4?token=JgZ3PZVBa-fmoPY2zWJ_29g8SH4s9UCnoVkAhGFj64yiRbdoJ2KY7ZDK3q5xxaFEOi7kjgLVeWkVSZqthkUOCHwLA7cnfZWVqnUyCTV-zgOOqhQoCcwH6K_pTAeyX4w7GQXfD9Tvp0_RY_J7_vzCUrC3-8zgquSlx1PQ1wAqKP60wsT1jniseoiCu8yhNVc5QBEGWMQ-iPYqW5uiMGDEBvFptc5lW5-MP3L1pfB5gvEfG5EXoVH1Wgt51xe0KNoJm0mGEPqKm2wNSI9C3r-cw0HSI6xv-qRGn18FPHu0eW7FLz7KCz1ShIl9yjPiuAh7uW8wbOqYQ4Olbzl6V4r_sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cedd59487c.mp4?token=JgZ3PZVBa-fmoPY2zWJ_29g8SH4s9UCnoVkAhGFj64yiRbdoJ2KY7ZDK3q5xxaFEOi7kjgLVeWkVSZqthkUOCHwLA7cnfZWVqnUyCTV-zgOOqhQoCcwH6K_pTAeyX4w7GQXfD9Tvp0_RY_J7_vzCUrC3-8zgquSlx1PQ1wAqKP60wsT1jniseoiCu8yhNVc5QBEGWMQ-iPYqW5uiMGDEBvFptc5lW5-MP3L1pfB5gvEfG5EXoVH1Wgt51xe0KNoJm0mGEPqKm2wNSI9C3r-cw0HSI6xv-qRGn18FPHu0eW7FLz7KCz1ShIl9yjPiuAh7uW8wbOqYQ4Olbzl6V4r_sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکتر برا مراجعه کنندش تزریق لب انجام داده و از شدت ریدمان، خودشم نتونست جلوی خندشو بگیره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/70812" target="_blank">📅 20:53 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70811">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REw0tkk_KEaez2sirb--LyTiNJnnKMU64woSFaUp4nX0qFhbrcEViZV2CdYaADhtCL9wTc4CH5E61Ft1T2F3lCxOVGujgyYqs9e4R1Faku3CSAj2H1uzzJFtgPII3-8AftZTfcldO_Ksgwbr7N1NMqr9Fj_4LkSnL1Eye59ASLajOP2TJBuwgGQSR0jjatP_yRXqsISk4IAxygOdPRDMfxTROM_6YJNzeyM6rwqb4LSZ4_7bPTG5lJxieeEypd3Dqnk4s2XmEWjQEwOhqJAOR_KyzWBt-pLXN6j_LAE_YCaGNs_tbl3va2rw8cx-6JH_twgTXSRUghsu8NDSz6YUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا UKMTO:
یک نفتکش هنگام عبور از تنگه هرمز در مسیری به سمت داخل (شمال)، در موقعیتی تقریباً ۱۲ مایل دریایی در شمال «خصب» عمان، هدف اصابت یک پرتابه ناشناس قرار گرفته است.
این حادثه هیچ‌گونه تلفات جانی یا پیامدهای زیست‌محیطی در پی نداشته است.
موقعیت مکانی حمله نشان می‌دهد که این شناور هنگام استفاده از مسیر کشتیرانی تعیین‌شده توسط ایالات متحده در آب‌های عمان، هدف قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/70811" target="_blank">📅 20:17 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70810">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am3IyJ8st6oSF9hsXqPm-XuoX3iddwlxQB2GlXZd2lBEonHOQKuvuc7H4ODamTfxcc67A0jOa_K6Iu1Wh9idnbtlZMVm2MiYQNEDgQG2T8GjRGCMssLZWEHO2uvGkpJ-MhGSOwdJ765LovU1No14uosX2jXfWbcKPGDXOGE0y5mlBBtajnzDHhZvFkS3Uag8b13TD-eCdnsSmKBZ_vlTumU4_6RLqJe_lVOzzRUmhxCEcXVc6iwrEs6YFQGaWSg3yOrWfAOJwCLdrRnZnN-mobSwdp_ErfFPINiNLimFfvnahyef9F9SdENz-3nz6lC72n2YG1mgprckMO1ObUOJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترامپ برای اینکه لج کانادایی‌ها رو دربیاره، اسم دریاچه کانادا(Lake Ontario) رو گذاشت «دریاچه آمریکا»؛
کانادایی‌ها هم کم نیاوردن و از لج ترامپ اسم دریاچه رو گذاشتن «دریاچه هرمز» و تاجایی که میتونستن این موضوع رو تو فضای مجازی وایرال کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70810" target="_blank">📅 19:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70809">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ce04d5d87.mp4?token=iZB81WaSeWOkTTBtMqSdxq3Np2YFFJsuF2ZXitxptJiGsmKtA-FiHBtmdNu1975wAcgM1zwubQFY-hsM-M4blypTMaRULlC_MQ3SM96CFUc4_KKrpyopNqJUtNFyZZ_51zzZF99p0RIkbISohPPTC1TquXhsRy78UrtTueQuys6z6r0KCdDxhumfXO5l-8CezU7unUCr7cYGBleJF_dBB8DE2_JqaUtq9erw3A0UbUhgM7UifzmceEG9fdLltTg7S0x2pKyDLD-d2BNGsSSiwFMJAOZsHlFAUZRZgBUmnKrrWKOK9gXESXBlx3MWf9stKSRitkTOvSmKcNXVDoAAyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ce04d5d87.mp4?token=iZB81WaSeWOkTTBtMqSdxq3Np2YFFJsuF2ZXitxptJiGsmKtA-FiHBtmdNu1975wAcgM1zwubQFY-hsM-M4blypTMaRULlC_MQ3SM96CFUc4_KKrpyopNqJUtNFyZZ_51zzZF99p0RIkbISohPPTC1TquXhsRy78UrtTueQuys6z6r0KCdDxhumfXO5l-8CezU7unUCr7cYGBleJF_dBB8DE2_JqaUtq9erw3A0UbUhgM7UifzmceEG9fdLltTg7S0x2pKyDLD-d2BNGsSSiwFMJAOZsHlFAUZRZgBUmnKrrWKOK9gXESXBlx3MWf9stKSRitkTOvSmKcNXVDoAAyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
حمله پزشکیان به صداوسیما:
مسعود پزشکیان، رئیس‌جمهور ایران، از سازمان صداوسیما به دلیل سانسور خود و سایر حامیان تفاهم‌نامه با آمریکا انتقاد کرد و این نهاد را به اتخاذ رویکردی افراطی متهم ساخت.
پزشکیان خطاب به جبلی رئیس صداوسیما: «این روزها دیگر اصلاً تلویزیون آن‌ها را تماشا نمی‌کنم. آن‌ها مایه وحدت نیستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70809" target="_blank">📅 18:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70808">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58b978362a.mp4?token=b2r-ruptBsUrF8u-94Z__quH7POMANriZ93S1-IkBwNGUWlbYG0IOSv16ULiQvdxrCkV5Vjvz-F75CEqkoxG6_kYftqZffAtfHL5aPvZ4ASGFRCs7ZQ_QZrxW2KiLZooS4LTlxz8xGOWmTJ4b6SeQtjSpqLBqwjxLfY0qHUaJBBrKCp7xt0_hVJEPS1mq1tjNf2aBMAOqhOU-QvxzVEkeLjzB1D6A9I5FYiOMfN7GKsulcJn51Gq1b3kCFpVsmvCClsx-Zb6lFrbzsfIHvSGkxdJftRqv5xaTMPF34NE3jWuRbljQAxL5gO2bJtv4z0Jm-bl4LAr4O2y34WxOIW66A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58b978362a.mp4?token=b2r-ruptBsUrF8u-94Z__quH7POMANriZ93S1-IkBwNGUWlbYG0IOSv16ULiQvdxrCkV5Vjvz-F75CEqkoxG6_kYftqZffAtfHL5aPvZ4ASGFRCs7ZQ_QZrxW2KiLZooS4LTlxz8xGOWmTJ4b6SeQtjSpqLBqwjxLfY0qHUaJBBrKCp7xt0_hVJEPS1mq1tjNf2aBMAOqhOU-QvxzVEkeLjzB1D6A9I5FYiOMfN7GKsulcJn51Gq1b3kCFpVsmvCClsx-Zb6lFrbzsfIHvSGkxdJftRqv5xaTMPF34NE3jWuRbljQAxL5gO2bJtv4z0Jm-bl4LAr4O2y34WxOIW66A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
امیر ابراهیم رسولی، دستیار قالیباف:  ما تا آخرین روز خون‌خواه رهبرمان هستیم امّا پوشکی که من برای فرزندم قبل از جنگ می‌خریدم ۳۶۰ هزار تومان بود. امروز همان پوشک ۸۶۵ هزار تومان است. باید آرمان و شعار را با واقعیات جامعه تطابق بدهیم.  @News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70808" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70807">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyADM-3H1scZI-XWAfwI83QT4v7VJPXyLLmGGqMX0fH_n4Blv_FwQa_98pgxY9ulzch4EXcn4ljTjtHg52NUVuRbL2v5EW7mOpKXuK5iJhKpgf0OF4lswHtbgFSthBuDWMrLIVwRxfO35lss3LOodHCD04NOEafjqs2XwBS7jOlLhEXEh1jxwcTZTnVTEbRZmERT8__PSRvLInlyMwLT9ldU7_jwho4b9uiFN2SbxP_1mSc9XENCGA6L7JiJjXGeB6PE5b08tmox0DXNJoDyO8dOzNRnFZHenG4F1WfO887jcuWYGalVrsmUdculW0evXc4Nehq0zJvcXgUZEg2qUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
@Vision_Bet
@Vision_Bet
@Vision_Bet
@Vision_Bet</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70807" target="_blank">📅 18:39 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
