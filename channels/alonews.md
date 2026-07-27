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
<img src="https://cdn4.telesco.pe/file/cQ79wbpHrLoLNW_V08LYYBqZCW7DauVVwShr6iOeZvfqQdj8SSg-QuMkso11oqHTqQ3kA_-RV7rQwWNWbd_IHFnkC2rzvJC5f8KRCUf0ft9FSZ31PPiYFuhXweAr9el7ZlYmsJylD68F1Dl5R0cRVmosC6OFYK5hOxDaagLqNpKLO9rxMsZuq8DPo_xr7XYAxWPVsxPuJ7OwgwsZstWrHJK6vlTukEQzy2amHc6oDbSQS9GRmOTgu4F_oLGQUQawHmhKYo-eiA7WFop5JXz3r1yk_kYn83BgNruI1Eu6Yc0aQsGDmR_pLnuvFR-SvnmcAa6e2pHwqNVtgz6_ndJnBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 967K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 23:44:36</div>
<hr>

<div class="tg-post" id="msg-138009">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73846f9e59.mp4?token=Cr8Jj58F_K08IfnCLbPcbuUfXOEs26DwqVZBIWfmGtfps89sISF6u3PTY9iLzU4YJ1Dk7La0kKic_XVOoAFZqsPVRoEHS9TXlii_HTCURefPE3pnhuReq23MPqD5s2Gz20dGTtcWDxiKpBoqfk92SWjoF6riXBWYDyX75FehFK5kTCBLC7P3_0BLqEuyR6gp2ev6w3yQ5C_h7go5hK-0_zuV55zBu3xaswoufapWVAOZcEQFiOnT2X4NqWDRQp6ZT1Qwi8UkAD9_J7gm6pK9GhRm6fZYKTF6z1_BQT2r36BIiKU4I0x7bS7BcmDBttdO7fuUbKWBosniLF1ZWZnuUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73846f9e59.mp4?token=Cr8Jj58F_K08IfnCLbPcbuUfXOEs26DwqVZBIWfmGtfps89sISF6u3PTY9iLzU4YJ1Dk7La0kKic_XVOoAFZqsPVRoEHS9TXlii_HTCURefPE3pnhuReq23MPqD5s2Gz20dGTtcWDxiKpBoqfk92SWjoF6riXBWYDyX75FehFK5kTCBLC7P3_0BLqEuyR6gp2ev6w3yQ5C_h7go5hK-0_zuV55zBu3xaswoufapWVAOZcEQFiOnT2X4NqWDRQp6ZT1Qwi8UkAD9_J7gm6pK9GhRm6fZYKTF6z1_BQT2r36BIiKU4I0x7bS7BcmDBttdO7fuUbKWBosniLF1ZWZnuUYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در روابط با جمهوری اسلامی ایران به موفقیت‌های بزرگی دست یافته‌ایم و ما اطمینان حاصل می‌کنیم که آن‌ها هرگز سلاح هسته‌ای نخواهند داشت.
🔴
وقتی کسی می‌پرسد: «چرا ما این کار را انجام می‌دهیم؟»، به سادگی بگویید: «چون ما نمی‌توانیم اجازه دهیم آن‌ها سلاح هسته‌ای داشته باشند.»
🔴
این موضوع بسیار ساده است. این تمام چیزی است که باید بگویید. نیازی به گفتن چیز دیگری نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/alonews/138009" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138008">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
ترکیه فروش سامانه S-400 به مصر را بررسی می‌کند.
🔴
بر اساس گزارش Defence Arabic، آنکارا در حال بررسی فروش سامانه‌های S-400 به مصر است؛ اقدامی که می‌تواند یکی از موانع اصلی بازگشت ترکیه به برنامه جنگنده F-35 را برطرف کند.
🔴
گفته می‌شود این موضوع در جریان سفر اخیر وزیر دفاع مصر به ترکیه مطرح شده است.
🔴
مصر هم‌اکنون سامانه S-300VM روسی را در اختیار دارد و در صورت نهایی شدن این معامله، توان پدافند هوایی خود را بیش از پیش تقویت خواهد کرد.
🔴
به گزارش منابع، ترکیه این معامله را بخشی از یک بسته گسترده‌تر همکاری‌های نظامی و فنی با مصر می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/alonews/138008" target="_blank">📅 23:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138007">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b21566da8a.mp4?token=cQDXBKenuBsswheWIlBr2rNP7uoxZcnazFCSJoHshS-5njNPdWA8dtVNLF1zAnrCfcaJ_wmzNg9TZhIeHocPkRnqRfZ0atvw8HFlZDutgsEGcEfJKnB6PDwikNJtbZJxToGHCHRWoYNrWftauw2sGI7bgqbAmAePXI4Wb7upGo5HI6SZt5AmHOuuDkK1JA9BhakBl450qwNQdeW4zOiBdIuMNL9DFhDhvpKLLeIyG1myR8nhTDM-0hocOlZkCki1q4iQuGEBTYYi34e5EJdBmPTRC-oVfjua9Mt3zjtjc5dPRB4oVWdF4z7YhKxWwye4Fn2J9p8tnChtTYzKzadKew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b21566da8a.mp4?token=cQDXBKenuBsswheWIlBr2rNP7uoxZcnazFCSJoHshS-5njNPdWA8dtVNLF1zAnrCfcaJ_wmzNg9TZhIeHocPkRnqRfZ0atvw8HFlZDutgsEGcEfJKnB6PDwikNJtbZJxToGHCHRWoYNrWftauw2sGI7bgqbAmAePXI4Wb7upGo5HI6SZt5AmHOuuDkK1JA9BhakBl450qwNQdeW4zOiBdIuMNL9DFhDhvpKLLeIyG1myR8nhTDM-0hocOlZkCki1q4iQuGEBTYYi34e5EJdBmPTRC-oVfjua9Mt3zjtjc5dPRB4oVWdF4z7YhKxWwye4Fn2J9p8tnChtTYzKzadKew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
در ١٨ دی مردم رشت شهر رو بصورت کامل در کنترل خودشون داشتن بدون اینکه خون از دماغ کسی بیاد.
🔴
ولی در ١٩ دی حرام زاده های حکومتی با آتیش کشیدن بازار باستانی رشت برای به قتل رسوندن مردمی که به اونجا پناه برده بودن و به گلوله بستن مردمی که سلاحی نداشتن، جنایتی راه انداختن که هیچوقت از ذهن این مردم شاد فراموش نمیشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/alonews/138007" target="_blank">📅 23:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138006">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
نایب رئیس مجلس: همه راه‌ها را با آمریکا رفتیم و جواب نگرفتیم
🔴
آن‌ها فقط زور می‌فهمد، پس چاره‌ای جز ایستادگی عالمانه و هوشمندانه نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/138006" target="_blank">📅 23:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138005">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0413f576f8.mp4?token=P-Nt0-YqbOxfjKjCNDTdTIbtvCBXco6m8YwrMgffMa9-8qNEtni-PgDT-aqRwkgu3YLG8koBx5fG3P9kawJKIuyt21-4NWiaDxIAQXHJfhuyjm5-5uCtDwqIXnoeL0YaI_mO_lBLgyoBrdQoHmM0bd1eaHhJF5jdrRFkqWmKNBeVkWQZJh0TeWByOVU8d3hmJCAzU0ka6dmAKnSHdZO42ueZxbitV9zv-0vt1Tgim3rZDAzCqEcpVQ9EPNXPWdKsrMVRD3xjJ8Rh76r-1dz5fEh2fTPckthBCv9JGvOlbwuZx_EXHDPXMRqMVeJSag1jnh3Gd1ZHcuLMOhxly1hflw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0413f576f8.mp4?token=P-Nt0-YqbOxfjKjCNDTdTIbtvCBXco6m8YwrMgffMa9-8qNEtni-PgDT-aqRwkgu3YLG8koBx5fG3P9kawJKIuyt21-4NWiaDxIAQXHJfhuyjm5-5uCtDwqIXnoeL0YaI_mO_lBLgyoBrdQoHmM0bd1eaHhJF5jdrRFkqWmKNBeVkWQZJh0TeWByOVU8d3hmJCAzU0ka6dmAKnSHdZO42ueZxbitV9zv-0vt1Tgim3rZDAzCqEcpVQ9EPNXPWdKsrMVRD3xjJ8Rh76r-1dz5fEh2fTPckthBCv9JGvOlbwuZx_EXHDPXMRqMVeJSag1jnh3Gd1ZHcuLMOhxly1hflw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ گفت: خیلی از جمهوری‌خواهان آدم‌های خوبی هستند. ما حزب بسیار مهربانی هستیم. اما اگر بخواهم صادق باشم،
🔴
شاید نباید این‌قدر مهربان باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/alonews/138005" target="_blank">📅 23:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138004">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ : اون حوضِ زیبای کنار کاخ سفید... یکی اومد با چاقو خرابش کرد. مریضن
🔴
الان داره تعمیر می‌شه و خیلی زود دوباره درست می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/138004" target="_blank">📅 23:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138003">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/190b4a0822.mp4?token=r6VIkZ3ttQd1HRVScb0h_1vltgQ4A-tddOvK2Dxw4mphmfZD0BIX35Yx_RVbom9_Z5vXcVJByhqtLrL7PNvT4sBwOR__GqnqCPM1XI5hpI5eL0Fj79TrfHqdsFtrjJSG-Khl8XoJ6x3CeSdquOk-A_IIgLGzY8ElgMKmPxwoXc9MkHfUlD4iVPW_JSfls6BSZJ_6_Lyh6DAUBG9Z07l1jZt1D1nvrJgOrqkJWBLmq3X9aixTOGtr0YS1Jazmw236Z8g5W8GxzDPdM6r2W3X2XDtkO3dOt0sBCfmw1qKp6f_T8PgDZCsG7w0Pu4ge1FAcz7lhWgQZHfssZNSPaM-t8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/190b4a0822.mp4?token=r6VIkZ3ttQd1HRVScb0h_1vltgQ4A-tddOvK2Dxw4mphmfZD0BIX35Yx_RVbom9_Z5vXcVJByhqtLrL7PNvT4sBwOR__GqnqCPM1XI5hpI5eL0Fj79TrfHqdsFtrjJSG-Khl8XoJ6x3CeSdquOk-A_IIgLGzY8ElgMKmPxwoXc9MkHfUlD4iVPW_JSfls6BSZJ_6_Lyh6DAUBG9Z07l1jZt1D1nvrJgOrqkJWBLmq3X9aixTOGtr0YS1Jazmw236Z8g5W8GxzDPdM6r2W3X2XDtkO3dOt0sBCfmw1qKp6f_T8PgDZCsG7w0Pu4ge1FAcz7lhWgQZHfssZNSPaM-t8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: به طور موقت، تنش‌ها کاهش یافت. اما آن‌ها رفتار مناسبی نداشتند و مجبور شدم دوباره وارد عمل شوم.
🔴
اکنون آن‌ها دوباره رفتار مناسبی دارند. این شبیه به نواختن یک ساز بانجو است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/138003" target="_blank">📅 23:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138002">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ : یه کم ناراحتم چون شاید تا دو سال و نیم دیگه رئیس‌جمهور دیگه‌ای داشته باشید. شاید
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/138002" target="_blank">📅 23:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138001">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/006cb45ccc.mp4?token=AdCfUHPQkuTC77gcro0HGAoGZ6sypcYF0Nogs_PjsLqxESxkhhIhD9iEgnuhkFdOKAqYchNknbybDi0kxwz8l6wVwFOmq0amdH3u_qL96EJ4n-FXbppndkIUCKZyl9XPASh_AwpL1MjnQJWMZ3cysbp_CKf6cUmbN0CgG_bklBqLB2J3hNxdZ3V2FtrKZ6-a3xCBWRBU7CYlOq_FIWlcmvtaMKqVYPqvqxaIoBqxTDIgSW-t8p8Yq1NKSsLat4pYYQx1WPE9JZIjDTDie2PR5AgXZMoIP7W_cSWjbk_byWQCtiur9ujYQu8LcPk-FzN3vsO5BVnHljz02VOIpRHj7A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/006cb45ccc.mp4?token=AdCfUHPQkuTC77gcro0HGAoGZ6sypcYF0Nogs_PjsLqxESxkhhIhD9iEgnuhkFdOKAqYchNknbybDi0kxwz8l6wVwFOmq0amdH3u_qL96EJ4n-FXbppndkIUCKZyl9XPASh_AwpL1MjnQJWMZ3cysbp_CKf6cUmbN0CgG_bklBqLB2J3hNxdZ3V2FtrKZ6-a3xCBWRBU7CYlOq_FIWlcmvtaMKqVYPqvqxaIoBqxTDIgSW-t8p8Yq1NKSsLat4pYYQx1WPE9JZIjDTDie2PR5AgXZMoIP7W_cSWjbk_byWQCtiur9ujYQu8LcPk-FzN3vsO5BVnHljz02VOIpRHj7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران گفت:
نمی‌توان آن‌ها را با پول یا امتیاز خرید. باید آن‌ها را شکست داد.
🔴
و ما داریم حسابی آن‌ها را در هم می‌کوبیم. باید ببینیم در نهایت چه پیش می‌آید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/138001" target="_blank">📅 23:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138000">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ : الان مذاکرات سازنده‌ای در جریانه. ایران می‌گه : لطفاً، لطفاً محاصره‌مون نکنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/138000" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137999">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be3db46cf.mp4?token=q96XCCewOVyvD-yXovWl-VRAs4tSwgvCKxAUTN8jnAgAWl8ORyUksClkIeL1mWNugW5jf9LvI3Lq1V3SpjTtBAmFUTlCYUXuC28LuYC_7IkSFJ6vaRlN75j4XbpIZcUZ-YVLniaEUFz5qQ9qqAHl6wxTwObNo3kL_AE732i0JhV7VEIj1C3d6_wnispb9qX2seXvVHsugIonDbtD5937fbMfrO1dx9zVHgPsp8rLiLzMBEy8DNXyoTdJgJ0RLMSwQUjWBqkAWyeBsKk-BXBE92_PGGyTuiKk9zvKvFrHM_WIo57KWm1HHRR-2cvNLqj3swMlYltflE3EHmxxM5BpXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be3db46cf.mp4?token=q96XCCewOVyvD-yXovWl-VRAs4tSwgvCKxAUTN8jnAgAWl8ORyUksClkIeL1mWNugW5jf9LvI3Lq1V3SpjTtBAmFUTlCYUXuC28LuYC_7IkSFJ6vaRlN75j4XbpIZcUZ-YVLniaEUFz5qQ9qqAHl6wxTwObNo3kL_AE732i0JhV7VEIj1C3d6_wnispb9qX2seXvVHsugIonDbtD5937fbMfrO1dx9zVHgPsp8rLiLzMBEy8DNXyoTdJgJ0RLMSwQUjWBqkAWyeBsKk-BXBE92_PGGyTuiKk9zvKvFrHM_WIo57KWm1HHRR-2cvNLqj3swMlYltflE3EHmxxM5BpXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: مدتی بود که اوضاع کمی آرام شده بود. اما آن‌ها دوباره رفتار مناسبی از خود نشان ندادند، و من مجبور شدم دوباره وارد عمل شوم.
🔴
اکنون، به نظر می‌رسد آن‌ها دوباره رفتار مناسبی از خود نشان می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/137999" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137998">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38d9a0a947.mp4?token=uGnQ6kC5FSIYd3pB-tKTGxCltolyyp44sXzGE4sa2bhZPqwy7NfgaKBHRXy_mLT1ilSiNfhKJ88kOOtQnNtf4SX1BbD4CzV38vLXsI7QvZfFqnoocT81PVf29GcPsZa7dezBnLFnUTgomgWH-9MoB1dky97rkpi64yvlVq0rB2ci0aoyfMmKhbENqLb4DCvB_oM6xNATOkssZqD9CUSm1LfEF9jFmn7Q0ps1KPUvMm8v6PN_9yBcWUUImSlZwChynM2xfeKrsntwo96L0TTMM92_I0xzJFPkRU4gNXJ4MAQQ622cVtiAwy2K5zGCxe3Dmze-RAr3ox8IlQVgR57atg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38d9a0a947.mp4?token=uGnQ6kC5FSIYd3pB-tKTGxCltolyyp44sXzGE4sa2bhZPqwy7NfgaKBHRXy_mLT1ilSiNfhKJ88kOOtQnNtf4SX1BbD4CzV38vLXsI7QvZfFqnoocT81PVf29GcPsZa7dezBnLFnUTgomgWH-9MoB1dky97rkpi64yvlVq0rB2ci0aoyfMmKhbENqLb4DCvB_oM6xNATOkssZqD9CUSm1LfEF9jFmn7Q0ps1KPUvMm8v6PN_9yBcWUUImSlZwChynM2xfeKrsntwo96L0TTMM92_I0xzJFPkRU4gNXJ4MAQQ622cVtiAwy2K5zGCxe3Dmze-RAr3ox8IlQVgR57atg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس جمهور آمریکا:
با وجود علاقه‌ام به رونالد ریگان، او اجازه داد صنعت خودروسازی آمریکا به ژاپن و کشورهای دیگر منتقل شود.
🔴
من در زمینه تجارت، از ریگان بسیار بهتر عمل می‌کنم
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/137998" target="_blank">📅 23:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137997">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ : همون اتفاقی که توی ونزوئلا افتاد، داره توی ایران هم می‌افته  فقط مردم متوجهش نمی‌شن
🔴
اینا رو نمی‌شه با پول و امتیاز خرید
باید شکستشون داد، و الان هم داریم حسابی شکستشون می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/137997" target="_blank">📅 23:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137996">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bed1c3e10.mp4?token=AyBUV8eEFBkNRknPxt15LVoBbGg2ab8n3NfEPWhXRc1Gs8OYS-jnfuvCJLz7iIqSYd7CIWChTGVGCZ3HB3A5Pfkx1TaKnRU9Ie6gbYqUKi9e45zUEMXj81G9cowGg3yQwsDLc_XAN6nilTwx4B3Uv6v7znKHfmlMFRf06NCEBvhcc1XMc827Om0CH4WHK6eKsOQTjXmB-2e8h8Pfo42i5AERghKAUIC57Xe8DwDbdMVynI6qfUsos7DEnOFrnQq5XRmf7pTSVhwX7K06B8vplGeERYCGarF8kPTBQSR2_ZceJ5ywlWBMu4jJegUY3RRNovYoA_DJgoS9vbnjmmCVsoOvVCeuQ_vmwnwkdZvZctOV6pK5VWnrPMMyUvvf87IpvTv-q1OayQ22noSalZnX8o1I73PN53MdNMnpa6lyP71Y2p4Tturea1Hi9IiIXZL2x3AyfLaPnIT5dtIXAsRJo0rXDZNYZWSItsPFT1orPBdnG1ZxTtJ_5KTPlH-XeITRghAeGsCe2ORdEO3aDSCrgniR0hIdyCFkpmEz6Tq0ErLzEWV7VAdYxRsn_URq6fyoFyZIkCxb-N1YY8cWnvfBx-bX-qduEGbSbcpeJM-2ISEiBSW4jmB6pZAcYVtFkvn1Pr96v_9TY_ecYe_dO2wlQcyFVaHMjc9il9HItmoISfs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bed1c3e10.mp4?token=AyBUV8eEFBkNRknPxt15LVoBbGg2ab8n3NfEPWhXRc1Gs8OYS-jnfuvCJLz7iIqSYd7CIWChTGVGCZ3HB3A5Pfkx1TaKnRU9Ie6gbYqUKi9e45zUEMXj81G9cowGg3yQwsDLc_XAN6nilTwx4B3Uv6v7znKHfmlMFRf06NCEBvhcc1XMc827Om0CH4WHK6eKsOQTjXmB-2e8h8Pfo42i5AERghKAUIC57Xe8DwDbdMVynI6qfUsos7DEnOFrnQq5XRmf7pTSVhwX7K06B8vplGeERYCGarF8kPTBQSR2_ZceJ5ywlWBMu4jJegUY3RRNovYoA_DJgoS9vbnjmmCVsoOvVCeuQ_vmwnwkdZvZctOV6pK5VWnrPMMyUvvf87IpvTv-q1OayQ22noSalZnX8o1I73PN53MdNMnpa6lyP71Y2p4Tturea1Hi9IiIXZL2x3AyfLaPnIT5dtIXAsRJo0rXDZNYZWSItsPFT1orPBdnG1ZxTtJ_5KTPlH-XeITRghAeGsCe2ORdEO3aDSCrgniR0hIdyCFkpmEz6Tq0ErLzEWV7VAdYxRsn_URq6fyoFyZIkCxb-N1YY8cWnvfBx-bX-qduEGbSbcpeJM-2ISEiBSW4jmB6pZAcYVtFkvn1Pr96v_9TY_ecYe_dO2wlQcyFVaHMjc9il9HItmoISfs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :
مه‌هی‌او!
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/137996" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137995">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0eae498d1.mp4?token=JoMI777w2TIuUulEWqlFs2n6meI8jihl1uNYU0GdHUXsXOD8tiAUUztNX1kLZowBRQnH0F4VbSzLveLiO7Y8OIob18QaA9AFyX8j_GBEHnPQe46EMMNpKZ0fboN4QU0CJdbVS64TSjhshsmhUWQynv_wfAJaurxBPGn3bFDqeTQLtLjJTc_TZd9dIxa-jmkkDpn63UFtWjPwhfTeBQmFwIx-4vv-dznFA8FIG6T4zu83h-FThNoRStQ-p0R1-8Vk04xTvaRm3Rylz9eERmvaXz-dFDAWMMOU3ZWXVtGjkqlE8xNaeh5OFxA3WOLL65b16dM4qFPQIwpk7sIiVPB1zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0eae498d1.mp4?token=JoMI777w2TIuUulEWqlFs2n6meI8jihl1uNYU0GdHUXsXOD8tiAUUztNX1kLZowBRQnH0F4VbSzLveLiO7Y8OIob18QaA9AFyX8j_GBEHnPQe46EMMNpKZ0fboN4QU0CJdbVS64TSjhshsmhUWQynv_wfAJaurxBPGn3bFDqeTQLtLjJTc_TZd9dIxa-jmkkDpn63UFtWjPwhfTeBQmFwIx-4vv-dznFA8FIG6T4zu83h-FThNoRStQ-p0R1-8Vk04xTvaRm3Rylz9eERmvaXz-dFDAWMMOU3ZWXVtGjkqlE8xNaeh5OFxA3WOLL65b16dM4qFPQIwpk7sIiVPB1zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:دولت دیوانهٔ بایدن کمونیستی بود.
خودِ بایدن نه. آن‌ها به جو گفتند:
"جو، بیا کمونیست شو."
او هم گفت:
"اصلاً کمونیست یعنی چه؟"
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/137995" target="_blank">📅 23:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137994">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
ترامپ خطاب به یکی از معترضان در میشیگان گفت
:
او یک کمونیست است. ما در حال رقابت با کمونیست‌ها هستیم.
ما با اختلاف زیادی پیروز خواهیم شد.
می‌بینید آن‌ها چه می‌خواهند بکنند؟
آن‌ها می‌خواهند خانه‌هایتان را بگیرند.
آن‌ها می‌خواهند پولتان را بگیرند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/alonews/137994" target="_blank">📅 23:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137993">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8546f48c6c.mp4?token=jCx9CR15TYhBTe35mYgbYBJKwd3gLJcyUvZ6al3r4pGZTvbez1ZSSSjOiB01MyXfLzX4nYoSFL3t8ra5Aa6vaEULVI7su9QS7RvvSqr4tq8XUDNgvo9wyvlA78Ge7Xc0Zrx8yOoH2-YjcScjHpQ1Q3bymkvyw-nd82cnFAZmrQFYV9jCDctWVFOBxMCzVzEi1TEtbiyIyn0oeHJm7VFwwGCbRpqtmgxpsYJ-xadj2y06oIPY5ZTO0_PeoVhxhCfeGv2A0u05OX4EFRSS72UubtcL3lPayBR1beCVmpNkeBzJ-TXMUYhg9sfAhHsJBZcnffERwJjwrtMwU9lKGYq9HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8546f48c6c.mp4?token=jCx9CR15TYhBTe35mYgbYBJKwd3gLJcyUvZ6al3r4pGZTvbez1ZSSSjOiB01MyXfLzX4nYoSFL3t8ra5Aa6vaEULVI7su9QS7RvvSqr4tq8XUDNgvo9wyvlA78Ge7Xc0Zrx8yOoH2-YjcScjHpQ1Q3bymkvyw-nd82cnFAZmrQFYV9jCDctWVFOBxMCzVzEi1TEtbiyIyn0oeHJm7VFwwGCbRpqtmgxpsYJ-xadj2y06oIPY5ZTO0_PeoVhxhCfeGv2A0u05OX4EFRSS72UubtcL3lPayBR1beCVmpNkeBzJ-TXMUYhg9sfAhHsJBZcnffERwJjwrtMwU9lKGYq9HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ گفت:
من بیشتر از پدر و مادرتان برای شما کار کرده‌ام.
من بهتر از پدر و مادرتان با شما رفتار کرده‌ام.
و خودِ آن‌ها هم با من موافق خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/137993" target="_blank">📅 22:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137992">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c3ad23df.mp4?token=oE9HHHoMUojc8C_qIaSKxhxi0jpbCUFqAdtwjRXiIQsy8-jDbVOHY8qxfP5bWMNPf00TtRTsiyjO5CTKUR5lRhUSNLdiiWA2hMby7SIKLVC7O-KGc09RROKqduwKiaarv1jX_KTRHVRggCTif-0UWUuNfimAzDAPobMKsYCY3IJparWi_qDIn_4yryWeXrfJgKIrvREAxRHwRhPHbwMt37IFFZ344w9aJ67j8zB8QhfF6ucSuUnFWCtZ_qH5jCTWlqoce6GwZpSM8zfMekfCdumi_EohQPGEhMkrmzhQ90-wpX8SGLUbDtDH7xtykrCtV8Fa6N8mIPycvCuu2pIy_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c3ad23df.mp4?token=oE9HHHoMUojc8C_qIaSKxhxi0jpbCUFqAdtwjRXiIQsy8-jDbVOHY8qxfP5bWMNPf00TtRTsiyjO5CTKUR5lRhUSNLdiiWA2hMby7SIKLVC7O-KGc09RROKqduwKiaarv1jX_KTRHVRggCTif-0UWUuNfimAzDAPobMKsYCY3IJparWi_qDIn_4yryWeXrfJgKIrvREAxRHwRhPHbwMt37IFFZ344w9aJ67j8zB8QhfF6ucSuUnFWCtZ_qH5jCTWlqoce6GwZpSM8zfMekfCdumi_EohQPGEhMkrmzhQ90-wpX8SGLUbDtDH7xtykrCtV8Fa6N8mIPycvCuu2pIy_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرزیدنت ترامپ
:
من رونالد ریگان را دوست داشتم، اما او اجازه داد صنعت خودروسازی ما به ژاپن و کشورهای دیگر منتقل شود.
ما ریگان را دوست داریم، اما در زمینه تجارت، ترامپ خیلی بهتر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/137992" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137991">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137991" target="_blank">📅 22:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137990">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوووووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/137990" target="_blank">📅 22:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137989">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
🔴
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137989" target="_blank">📅 22:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137988">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d2424e0d.mp4?token=MVf0gUC131muOdezlWJjeQHheTD5aXaq_qx0S6a-8q7Yk54pnwNAPFloz4PMjZLIK9XLfrJA6wyNDHjn_zPfCZKyJyuHdCnggm-Oj3btqeJrmDWnRApwgRytgRMdAZcCqmST-Io-aPWtOYfulIMNgPBiG8lsfe78-Yhel5ggu3HevwHnQbZ-V57p5EoH7Xs5U5PRz9o22AtSGoZKsHfD7lUxFY5hIchlKhyD3mlu--kLLxPm8HKahQDU6YceYqDoqKuX9yRqNRjwvSJp0eb5VXG_ZZIdEYvA8GQSAUk1JfJo09TdTnavLxlsyWNL6k_hne2eCdqSISnZ-abDk6pCYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d2424e0d.mp4?token=MVf0gUC131muOdezlWJjeQHheTD5aXaq_qx0S6a-8q7Yk54pnwNAPFloz4PMjZLIK9XLfrJA6wyNDHjn_zPfCZKyJyuHdCnggm-Oj3btqeJrmDWnRApwgRytgRMdAZcCqmST-Io-aPWtOYfulIMNgPBiG8lsfe78-Yhel5ggu3HevwHnQbZ-V57p5EoH7Xs5U5PRz9o22AtSGoZKsHfD7lUxFY5hIchlKhyD3mlu--kLLxPm8HKahQDU6YceYqDoqKuX9yRqNRjwvSJp0eb5VXG_ZZIdEYvA8GQSAUk1JfJo09TdTnavLxlsyWNL6k_hne2eCdqSISnZ-abDk6pCYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرگزاری عبری زبان
: ارتش اسرائیل با احتمال بالا ارزیابی می‌کند که پهپادهایی که صبح امروز در نزدیکی بحر المیت و هفته گذشته در کوه هرمون سرنگون شدند، توسط گروه‌های شیعه در عراق شلیک شده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137988" target="_blank">📅 22:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137987">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHh3tBYvWCi3p5zq9c75mwn8r6h5G16IMpHwQSWJLalfrkX4qrphYOwiFE73rSIk-6B0oX2otnPW3JiUhKeLBXfPLypBNIkqPmgTby1jsG4HNfyV9u2H0QbygERr9CLVLqzw0JKbVDRwTWAnE4NZMpj7Hloxnmv_5a72y9kdFZ3uKis5sPH3Sxjr1HMpisoDse7pgT_3vo_guNzhogrjFfl-C_8RoOhmuetrq7XWt1s7jIlnSdmVu5kUSZIjsAZ5R3a5OFquA9oplivMxw4jbVkMJVHeISqnDBrT8LSDwO3wCKpMQz3ywtxmqbj7fp26ZnJMsrPXSdLntcx-E1MIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی:
مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137987" target="_blank">📅 22:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137986">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAZZXs2sN3UoIAadw4HjtJCPyZgzLjjfxM7bY9uk2b61YM62UhHI-Jm2B1lYLwNMT-6FS1UQUQ6-60JPijtWpoeGpKKXEdaKM_5rO02XASJupUa49QC10_2UJqeFP_3y1Rq9dSgBBuvMdiy7R3-4M7r9Jo9LcBKgjR_a3Fi1uVEX862YrjpWGgf1IwCS-_nmxlzjECuSLltyKDic4wSflSPfOJR1AyIu_i7RAiu77MR5kPSATXK4TAUpLtgFOn8XaWrBkplsSx3FwUinYOKwCUEN5tpu6vtbZll2jQFtUUgRa9cFpDrJuMIYhnIJKXdwfEsX7uisSwJXSBd0lIsZrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام آمریکایی به الحدث:
مذاکرات با ایران جدی است و ممکن است امروز شاهد پیشرفتی باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137986" target="_blank">📅 22:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137985">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
مقامات آمریکایی: مذاکرات ترامپ و نتانیاهو به موضوع ایران و توافقنامه ابراهیم اختصاص دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137985" target="_blank">📅 22:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137984">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کانال ۱۲ عبری: نتانیاهو در دیدار با ترامپ اطلاعات حساسی را در رابطه با ایران به او ارائه خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137984" target="_blank">📅 21:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137983">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2-lM9gal3hJWUnrlHT9gSBxKA1XWFlLeN8kLYzn--G4M8H5Mq6vqGPBYhU31LpvTORfs8xvfPxwDrttESYQAI8aEemMky5VnlnuTOomR3I7JJnhmmgrAl6NwX6vr7qv_BNMkyX7yQl9Z9_sPY9Eoo0PTKNEzEepG3q67H1p1WkGtpmhXwFtvNwI5l9he4U45Hapa6V6pkPlbJeaKbTUzP40lUkLM6-z3J2oTciEwGdnJk_vC3h0niEZWLt-EpW66XHVbTi3hhtkpnoAtZkn4dVDK-jYyVwJO7XdR23MJts1GWMT5Rlf4CZezr9d4Mvu4feAdduzsjri4m92s85uUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی پیش نفت به قیمت ۸۸ دلار کاهش پیدا کرد
🔴
۱۲ درصد کاهش قیمت در ۲۴ ساعت
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137983" target="_blank">📅 21:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137982">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
رویترز ،مقام آمریکایی : ترامپ با نتانیاهو درباره ایران و توافق‌های ابراهیم صبحت میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137982" target="_blank">📅 21:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137981">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مکرون: اسرائیل فورا باید از تمام مناطق لبنان عقب نشینی کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137981" target="_blank">📅 21:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137980">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fa2zCv-P7Gpf1rVhuNqXUqr9xB_qYP-UVmgpO7cm1TZ24RG-j9jk1VW8MPEk6WDy6i26clQfH1OAXMt3LdNMC5q5lPULsaRUhqSGrQtUeJY75VTEGWWdfTN4muZQPYcGj9rqg0GO5gKiiS_UhaaYzjUwhSvXRyj7jlHMV4Jtd-MrPudbPTwDjx2FuuOPCdFNCATaAWTfSb4bBEGcMSv2JjfYAgWExzzz8TVcfWowl1W70mzs9zpon-4AkG7D6PHClVjrsTkvB-00gijsKfIe9dv3i_yWDVKSeE4Rzq8gFEYz7SGoM2fYv9kT0fWWv0y0OtXjaQGKFjdk5_8_h3pZ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مقام آمریکایی به الحدث: مذاکرات با ایران جدی است و ممکن است امروز شاهد پیشرفتی باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/137980" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137979">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
دفتر نخست وزیر عراق: الزیدی دستور تحقیقات امنیتی در مورد آنچه در بیانیه عربستان سعودی در مورد هدف قرار دادن آن با پهپاد از خاک عراق آمده است را صادر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137979" target="_blank">📅 21:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137978">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
شبکه i24 اسرائیل : نتانیاهو در دیدار با ترامپ با فشارهای قابل توجهی در مورد چندین موضوع از جمله سوریه، غزه و لبنان روبرو خواهد شد. این دیدار بسیار مهم است و ما امیدواریم که راه را برای عملیات مشترک اسرائیل و آمریکا علیه ایران هموار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137978" target="_blank">📅 21:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137977">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
استقرار نیروی هوایی آمریکا در قطر و عربستان دوباره تغییر کرد!
🔴
در پایگاه العدید قطر، تمامی هواپیماهای سوخت‌رسان و ترابری بار دیگر از پایگاه خارج شده‌اند.
🔴
در پایگاه پرنس سلطان عربستان، هواپیماها به آرایش زمان جنگ بازگشته‌اند و سه فروند هواپیمای آواکس E-3 نیز دوباره در این پایگاه مستقر شده‌اند.
🔴
به نظر می‌رسد ایالات متحده در حال جابجا کردن هواپیماهای بزرگ و راهبردی خود از پایگاه‌های آسیب‌پذیرتر نسبت به حملات ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137977" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137976">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd0b82ccc7.mp4?token=EH9X4HxnwaI_D8EE7sPpCOjeo697j4EFOiTnSMDp9l5WuVpUw51zciTk2a1bzX1Y6q-lk-5jY5A2B0dyf_5_bSfhbJ140BtDSUNxsmmXmMa72P1LQbNW5uuz3omDlJhgvvBkFVqfcYxZ0GoCIiFsUtf3Vp5uM4fHeP1NxInrFqH_CRIzXN1Zdp17_NFAgNB5CzOkC1yEhEAZIyCbyYZBjNytBY7UzsUHAoJYUQFai7IIKy9av5Y-QtISe1UZCoCcV23LKBMi6gWEkbxoz72_dtP_O-ZRX_5nHBZ7D6FC65L_UMSllm3MQx92l1gPpC49MWYIrM4PAtk9l6gUy0KHuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd0b82ccc7.mp4?token=EH9X4HxnwaI_D8EE7sPpCOjeo697j4EFOiTnSMDp9l5WuVpUw51zciTk2a1bzX1Y6q-lk-5jY5A2B0dyf_5_bSfhbJ140BtDSUNxsmmXmMa72P1LQbNW5uuz3omDlJhgvvBkFVqfcYxZ0GoCIiFsUtf3Vp5uM4fHeP1NxInrFqH_CRIzXN1Zdp17_NFAgNB5CzOkC1yEhEAZIyCbyYZBjNytBY7UzsUHAoJYUQFai7IIKy9av5Y-QtISe1UZCoCcV23LKBMi6gWEkbxoz72_dtP_O-ZRX_5nHBZ7D6FC65L_UMSllm3MQx92l1gPpC49MWYIrM4PAtk9l6gUy0KHuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از کشتی ایرانی که مورد حمله اوکراین قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137976" target="_blank">📅 21:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137975">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
بلومبرگ: ایران و عمان درباره راه حلی برای مسئله تنگه هرمز گفتگو می‌کنند. یکی از پیشنهاداتی که مطرح شده، باز کردن مسیر میانی تنگه، در آب‌های بین‌المللی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137975" target="_blank">📅 21:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137974">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afba5829f9.mp4?token=tJq_aeNZBRAHYeZufqtF_fawZv_KVj6CVew33fV1bNOZacfa0aUSFHos9_9MqCXZ58LMDgEjseJrFobpOUUCPImtmAOxR4W0aKPmxMeGp6assKqZEEtsnSn09jPfEpDtrC7pSa4qvWJC2ASfl3eS4IhgFrZNCTtL1MwHfjc7LINpk7uNRxRvVTbxmCqAr2WKOjqLakSdw7zb6aUI7ILDOVSg7olY3_um9NnkhDUldGQ-cwv2BXtWH2uwL0EjqAZKjw5_Dt3FcVNOpvq-bG2fxVQVlv0XB4VI-J8XwRQ42rSxDDesDZDGhgKBuguG8PjvDmcVpO79gXPksymRQp79rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afba5829f9.mp4?token=tJq_aeNZBRAHYeZufqtF_fawZv_KVj6CVew33fV1bNOZacfa0aUSFHos9_9MqCXZ58LMDgEjseJrFobpOUUCPImtmAOxR4W0aKPmxMeGp6assKqZEEtsnSn09jPfEpDtrC7pSa4qvWJC2ASfl3eS4IhgFrZNCTtL1MwHfjc7LINpk7uNRxRvVTbxmCqAr2WKOjqLakSdw7zb6aUI7ILDOVSg7olY3_um9NnkhDUldGQ-cwv2BXtWH2uwL0EjqAZKjw5_Dt3FcVNOpvq-bG2fxVQVlv0XB4VI-J8XwRQ42rSxDDesDZDGhgKBuguG8PjvDmcVpO79gXPksymRQp79rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
: روسیه تجهیزات نظامی زیادی به ونزوئلا داد.
🔴
ونزوئلا تقریباً تمام تجهیزاتش روسی بود.
🔴
ولی تهش چی‌شد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137974" target="_blank">📅 20:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137973">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا اعلام کرد در چارچوب برنامه نوسازی نظام تحریم‌ها، نام ۸۴ فرد و نهاد را از فهرست‌های تحریمی حذف کرده است./همچنین چند کشتی با پرچم پاناما و ایران نیز از فهرست حذف شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137973" target="_blank">📅 20:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137972">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ : اوباما مهمات نخرید
ما مقدار کمی داشتیم و من دستور ساختش رو دادم
🔴
وقتی من رفتم، بایدن مقدار زیادی از اون رو به اوکراین داد؛ اعدادی که قبلاً کسی ندیده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137972" target="_blank">📅 20:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137971">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dca0922d5.mp4?token=pGq8SW448-yJoocLiPWJsqTajuAtU-nRZuMzaywYnqfJ5S2uXHgehjunpvaoZmX18Bu3KRvHoLt83J4Ax559c39BXLTO3g0aia_cBbgmfsBBZhLYGr2Yiv6ZWLi7hwFlTNYysLe9peFbe2B11oDrzTvfRHNz6IoIfDfVGeVRYP-hrbx6S1m81ezmoSMdCSBIOdXj_ZU53Si89_UeqB0i6LPnt8YcioJBX8TlTyGVPxpd0dLBcCAwcsZV-elDMLAiMVowEZ6DxSkNPgqwAGJCbzvdY8b5QdhBpWF6wtVBFLugRPdEdRAqUuKufAX2Pn1416t4vz7s9R9wSu4NfSk_sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dca0922d5.mp4?token=pGq8SW448-yJoocLiPWJsqTajuAtU-nRZuMzaywYnqfJ5S2uXHgehjunpvaoZmX18Bu3KRvHoLt83J4Ax559c39BXLTO3g0aia_cBbgmfsBBZhLYGr2Yiv6ZWLi7hwFlTNYysLe9peFbe2B11oDrzTvfRHNz6IoIfDfVGeVRYP-hrbx6S1m81ezmoSMdCSBIOdXj_ZU53Si89_UeqB0i6LPnt8YcioJBX8TlTyGVPxpd0dLBcCAwcsZV-elDMLAiMVowEZ6DxSkNPgqwAGJCbzvdY8b5QdhBpWF6wtVBFLugRPdEdRAqUuKufAX2Pn1416t4vz7s9R9wSu4NfSk_sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پولی که از ونزوئلا به دست می‌آید، صرف چه چیزی می‌شود؟
🔴
ترامپ: صرف اداره کشور می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137971" target="_blank">📅 20:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137970">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f19b14e9.mp4?token=r-bTSsN2COOCs1eDfRs-XAlQLMC2rcQDNkW-cUnvt3SVeszjGTJ8Y4tzB7q53bPjrtIoZf7couDAN7vKR-0drEYyfHDijH6NWXk3M4rmwwQFQMcFtt9_3IQPqNV6Yiij3P_mEnv2A2KWN4b77StQ8FHlwSnaIuyJpvzcjI611tSU0bWy_enEcDXx4AdshssioRX6Ukr-xL4SfpwTwDHZntWF3ZPxT_jRkgEyDfb7PgRzyKUPX5KCHWBpaC2h5DJFASRqLW5TdcXrHTr8H-bBOUZcxqbY1Xm1AKrX8lSDEKn42MiJq9p9fnMqksYQ8uisq4p-H8TnTW_ST1EkdvzxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f19b14e9.mp4?token=r-bTSsN2COOCs1eDfRs-XAlQLMC2rcQDNkW-cUnvt3SVeszjGTJ8Y4tzB7q53bPjrtIoZf7couDAN7vKR-0drEYyfHDijH6NWXk3M4rmwwQFQMcFtt9_3IQPqNV6Yiij3P_mEnv2A2KWN4b77StQ8FHlwSnaIuyJpvzcjI611tSU0bWy_enEcDXx4AdshssioRX6Ukr-xL4SfpwTwDHZntWF3ZPxT_jRkgEyDfb7PgRzyKUPX5KCHWBpaC2h5DJFASRqLW5TdcXrHTr8H-bBOUZcxqbY1Xm1AKrX8lSDEKn42MiJq9p9fnMqksYQ8uisq4p-H8TnTW_ST1EkdvzxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
چرا می‌خواهید سناتورهای آمریکا در واشنگتن بمانند؟ نباید بروند برای تبلیغات انتخاباتی؟
🔴
ترامپ: چه سؤال احمقانه‌ای!
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/137970" target="_blank">📅 20:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137969">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81f5ceb040.mp4?token=UGPa1M8FSkMHugDXGsG4bLrQS4GoVuSRT1qThLcDVSdk9GCQWZpyAiHjkQ10E4IDKrLLkDX7JPUm4KDgg85-hsqSUPNPQNP_ICAe2fjumpXEcgjvoQCoOhw_bMVCibppbj9166pyAmnrMQ51FZn9XEtVfllQ90blVUTL0_H6icep_jGoIIo8TOhv9RIliwPTnBmb4IxJuKYBsfY8t569j6XVtvM2AgOYEp-kGi2s-UiLV3b4xMv7G4AAzwvUcfXl1Pt2FQ6RQ7slVMLHtiBWDK9AZDM1yPyHt8-rstSHrx298hSTUWxrzKAzho774oSpTK3JbUVJKIihki8cipCAiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81f5ceb040.mp4?token=UGPa1M8FSkMHugDXGsG4bLrQS4GoVuSRT1qThLcDVSdk9GCQWZpyAiHjkQ10E4IDKrLLkDX7JPUm4KDgg85-hsqSUPNPQNP_ICAe2fjumpXEcgjvoQCoOhw_bMVCibppbj9166pyAmnrMQ51FZn9XEtVfllQ90blVUTL0_H6icep_jGoIIo8TOhv9RIliwPTnBmb4IxJuKYBsfY8t569j6XVtvM2AgOYEp-kGi2s-UiLV3b4xMv7G4AAzwvUcfXl1Pt2FQ6RQ7slVMLHtiBWDK9AZDM1yPyHt8-rstSHrx298hSTUWxrzKAzho774oSpTK3JbUVJKIihki8cipCAiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیا چین در حال دزدی از آمریکا است؟
🔴
پرزیدنت ترامپ: آن‌ها ما را زیر نظر دارند، و ما هم آن‌ها را زیر نظر داریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137969" target="_blank">📅 20:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137968">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bea6d733a8.mp4?token=m4swiawRaaUJ7CGDsssXUifR5uFpBAgISKdU-PEBeA51uBBe6zOvggqrgatI-6STpViQEvZxVkzI5dfPD2qZCVutPemRkZ0jjg2zDKLI8ZKWdAmBgq6EEkzBT5C2Lpif_j1YG00Bv1l-b6ALQS5a4OoPA5wf6bZ2wdUZc24X7ZIWSEs0iNOEzwtZqDfjMrYd5ovpt3e6HMzlc4GYvlQ3NkSQq2lqcV6U8fhsboNG8ZUYPFuXAnXmaWZOH_iVOvBVxi-5QiigbClxkzmqymaa-fdf5NF0CoBC6AawW92jJV7MYuwfrx1U4mwllS_A-3lszH5-LnYAGWbCxwsWgbmo9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bea6d733a8.mp4?token=m4swiawRaaUJ7CGDsssXUifR5uFpBAgISKdU-PEBeA51uBBe6zOvggqrgatI-6STpViQEvZxVkzI5dfPD2qZCVutPemRkZ0jjg2zDKLI8ZKWdAmBgq6EEkzBT5C2Lpif_j1YG00Bv1l-b6ALQS5a4OoPA5wf6bZ2wdUZc24X7ZIWSEs0iNOEzwtZqDfjMrYd5ovpt3e6HMzlc4GYvlQ3NkSQq2lqcV6U8fhsboNG8ZUYPFuXAnXmaWZOH_iVOvBVxi-5QiigbClxkzmqymaa-fdf5NF0CoBC6AawW92jJV7MYuwfrx1U4mwllS_A-3lszH5-LnYAGWbCxwsWgbmo9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : چقدر دیگه به ایران فرصت می‌دید؟
🔴
ترامپ : من زمان زیادی دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137968" target="_blank">📅 20:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137967">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff0e22e8d.mp4?token=QVsl9Rc4r-pAS3CfYrPBQiKBMcSKuW1V7UQJmpDJ47NK2IytCCGb2uhWGvd65qNQziPzx-Q5uQ_-u29bDScUbH0hgHEmw0AFO0Vcr8yHffHFL5QIAwrI-t9NJo4vsMDQI1vzGq4ceUu1_prK_0tEpYdgeyiON49-AHAKFX4RyIu0B76vyBDtAycN9fLH7FKTzFalUPqYjjYKu1X1jbbSeJRTFbEgvZrOEPhSTrntKi1gEBCATqV5Se8WE8NVF7BNJrkjgdMinz5l6OzBgKPSgSzyE9dXb4fBoYLyKCS2_j7S_vvcVqNiSv1xkNUWLTfbNCZn8HHTyz2n8oETfgIy0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff0e22e8d.mp4?token=QVsl9Rc4r-pAS3CfYrPBQiKBMcSKuW1V7UQJmpDJ47NK2IytCCGb2uhWGvd65qNQziPzx-Q5uQ_-u29bDScUbH0hgHEmw0AFO0Vcr8yHffHFL5QIAwrI-t9NJo4vsMDQI1vzGq4ceUu1_prK_0tEpYdgeyiON49-AHAKFX4RyIu0B76vyBDtAycN9fLH7FKTzFalUPqYjjYKu1X1jbbSeJRTFbEgvZrOEPhSTrntKi1gEBCATqV5Se8WE8NVF7BNJrkjgdMinz5l6OzBgKPSgSzyE9dXb4fBoYLyKCS2_j7S_vvcVqNiSv1xkNUWLTfbNCZn8HHTyz2n8oETfgIy0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : اونا درخواست دیدار کردن اگه ما خوب عمل نکرده بودیم، اونا درخواست ملاقات نمی‌کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137967" target="_blank">📅 20:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137966">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ درباره ترکیه : ترکیه یه کشور خیلی قدرتمنده؛
🔴
فوق‌العاده‌ست و یه ارتش خیلی بزرگ داره، ارتشش هم تجهیزات خیلی پیشرفته‌ای داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137966" target="_blank">📅 20:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137965">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6384fa75fc.mp4?token=M5sZa95D983ft3cxd8aIi0pEQ0AOHsY2WZhSwE724s2ZogC9KrYjFCOA5l-d8cX__U_Q0pKQ8ib8pw8PeLxUUvJqa77chqBTg_QwdU6FrqapnFTaZHZu5f425QynikHn0agU3cT1y_KZD8DAtQfh-7wPW4CQ6Co7EI0Mdy-73K1xrQvcWLIGP5-3ZVvoZquP7mc4Q_cCdWak2BrNK7MWMBBHsg7IbbthtHYl58Fi-RpJLxdcmy2SiW8pXL7puuxzfDf2Vgnu9xgP__vTUGUwNKT5ujOTYN6VTSTOIY10YLUTA_8aM7VODo7JeuHtrS_XOF-GSyNc6RK1uUy1QTCmBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6384fa75fc.mp4?token=M5sZa95D983ft3cxd8aIi0pEQ0AOHsY2WZhSwE724s2ZogC9KrYjFCOA5l-d8cX__U_Q0pKQ8ib8pw8PeLxUUvJqa77chqBTg_QwdU6FrqapnFTaZHZu5f425QynikHn0agU3cT1y_KZD8DAtQfh-7wPW4CQ6Co7EI0Mdy-73K1xrQvcWLIGP5-3ZVvoZquP7mc4Q_cCdWak2BrNK7MWMBBHsg7IbbthtHYl58Fi-RpJLxdcmy2SiW8pXL7puuxzfDf2Vgnu9xgP__vTUGUwNKT5ujOTYN6VTSTOIY10YLUTA_8aM7VODo7JeuHtrS_XOF-GSyNc6RK1uUy1QTCmBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما توی همه زمینه‌ها و در همه چیز، از همه جلوتر هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137965" target="_blank">📅 20:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137964">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec41e14555.mp4?token=IrVsqkaVoFSBG85hwW8S1XHf1TgmKlqjgo-083NF6gltOMQmcmZdEtfrFDp3VxLXiZL2jLY6O-dQMWJnrYU0TsLWWd9h3GCtj_Kjj5ZhBrnqRU4h2c9vb-LiEGxCEqueUIOlLbofvs0C9lwW2WTtinanFVshW9DcGl51-Ina5NrufkcuW9p6CgZkoMdmc634jMfjrj7L-kDHehJeRGVQMuNRxw3yo7t72CVKeuWie2-0yiMhbZXrd2GPQQtVx-elujf-do58pu1OQ6IDNAbfKWxKroYlyh6my1OXJhElUMDZEF4XKw259ZxOfNguktrRSTWlyovrI56FAKN8EoeP5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec41e14555.mp4?token=IrVsqkaVoFSBG85hwW8S1XHf1TgmKlqjgo-083NF6gltOMQmcmZdEtfrFDp3VxLXiZL2jLY6O-dQMWJnrYU0TsLWWd9h3GCtj_Kjj5ZhBrnqRU4h2c9vb-LiEGxCEqueUIOlLbofvs0C9lwW2WTtinanFVshW9DcGl51-Ina5NrufkcuW9p6CgZkoMdmc634jMfjrj7L-kDHehJeRGVQMuNRxw3yo7t72CVKeuWie2-0yiMhbZXrd2GPQQtVx-elujf-do58pu1OQ6IDNAbfKWxKroYlyh6my1OXJhElUMDZEF4XKw259ZxOfNguktrRSTWlyovrI56FAKN8EoeP5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار : آیا نتانیاهو می‌خواد شما با ایران به توافق برسید یا می‌خواد حملات ادامه پیدا کنه؟
🔴
ترامپ : نتانیاهو آدم خیلی خوبیه. ایران الان فقط ۸ درصد از قدرت قبلی خودش رو داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/137964" target="_blank">📅 20:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137963">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: ما هزینه جنگ ونزوئلا را چندین برابر پس گرفتیم.
🔴
همین اتفاق برای ایران هم خواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137963" target="_blank">📅 20:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137962">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ترامپ دوباره اعلام کرد: اگه من نبودم اسرائیل وجود نداشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/137962" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137961">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ: ما مهمات زیادی از انواع مختلف داریم. بایدن مقدار زیادی از آن‌ها را به اوکراین داد، و ما الآن در حال جبران و افزایش دوباره ذخایر هستیم.
ما به قدری مهمات داریم که تحت هیچ شرایطی نمیتونیم تمومش کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137961" target="_blank">📅 20:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137960">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/794142c13b.mp4?token=FsF__0J-urO1z3_BC6dTCxWpo6C0tg0_l2AFJ7aiwoU8oXOrTprWpKLLYnlaDe8Q6lMwtnbbdL_tGebaT9H-eP4RD7YgKEgXm6OKTXACiEVY8Aj3mHXRVD92bkXbL4lJgcrd3u9vxQlhWMKJ-Fv_kfKpCExe1n6HpUbPdCgiLry3-6JPAzd5iDxLtOc3MIOoDJixJSuZelaPkRRZG5m38B8-OMBqA2fH0AUdNiFSFCmQjEkZoBMSH9nDiADnhnQz_ruu4PZjx3nAXlzgV5we6SXmRhierNNlKpyB7afghK26xn0hRla6kYCg3bsZVHhsSAtbPLDhM9XSVuEFmBblHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/794142c13b.mp4?token=FsF__0J-urO1z3_BC6dTCxWpo6C0tg0_l2AFJ7aiwoU8oXOrTprWpKLLYnlaDe8Q6lMwtnbbdL_tGebaT9H-eP4RD7YgKEgXm6OKTXACiEVY8Aj3mHXRVD92bkXbL4lJgcrd3u9vxQlhWMKJ-Fv_kfKpCExe1n6HpUbPdCgiLry3-6JPAzd5iDxLtOc3MIOoDJixJSuZelaPkRRZG5m38B8-OMBqA2fH0AUdNiFSFCmQjEkZoBMSH9nDiADnhnQz_ruu4PZjx3nAXlzgV5we6SXmRhierNNlKpyB7afghK26xn0hRla6kYCg3bsZVHhsSAtbPLDhM9XSVuEFmBblHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آیا شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🔴
دونالد ترامپ: یک اختلاف‌نظر کوچک بین ما وجود دارد، اما در کل تقریباً هم‌نظر هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137960" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137959">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
خبرنگار: نتانیاهو با ارسال جنگنده‌های اف‑۳۵ به ترکیه مخالفت می‌کند.
🔴
ترامپ: هیچ‌کس به من نمی‌گوید که چه بفروشیم و چه نفروشیم. ترکیه متحد بزرگی بوده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137959" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137958">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
خبرنگار: آیا نشانه‌ای از عربستان سعودی در مورد پیوستن به پیمان ابراهیم وجود دارد؟
🔴
ترامپ: ما در مورد آن صحبت نکرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137958" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137957">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترامپ
:
ما از پول ایران برای جبران خسارت‌های وارد شده به کشتی‌ها استفاده خواهیم کرد
🔴
از پولی که ما از ایران در اختیار داریم، برای این منظور استفاده خواهد شد.
🔴
به نظر شما هم خوب نیست؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/137957" target="_blank">📅 20:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137956">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ترامپ درباره ایران: ما در حال انجام مذاکرات خوبی هستیم. احتمال اینکه اتفاقات خوبی رخ دهد، وجود دارد
🔴
اگر این اتفاق نیفتد، ما به همان کاری که دو روز پیش انجام می‌دادیم، باز خواهیم گشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/137956" target="_blank">📅 20:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137955">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc61b4ad75.mp4?token=Uv0q-w8kEHG2LdFGQGF40fyeqO31NlIsUPxN5F8MIKgSQtviqLUznF7Y3k6uq8EuGJGOTcjRtD65DMtljRz-4490ukpsE6-LvZ1K0ok6OhNiA8uZO20BW1ehiRYeiKLbBKKND9JA9YPBM30ARLKH-1yNtQUOhxiX7s6CooFKD9Pdsu8CwOItE2fEDxX-paDYKfPcvc52eFAAw3KrREHg8NJn0Dl2eUph8c8Plyff_ygv8EuZ53zIOTaSZxzS9D7caKEFsXjpA2ElmVgaW8bFWKyXTLVbfhKj6G0kVC4Av1GPfPD5Tbwd4zL8uJrqoOOWF7k0yrwgWPMAT0iFf8jrOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc61b4ad75.mp4?token=Uv0q-w8kEHG2LdFGQGF40fyeqO31NlIsUPxN5F8MIKgSQtviqLUznF7Y3k6uq8EuGJGOTcjRtD65DMtljRz-4490ukpsE6-LvZ1K0ok6OhNiA8uZO20BW1ehiRYeiKLbBKKND9JA9YPBM30ARLKH-1yNtQUOhxiX7s6CooFKD9Pdsu8CwOItE2fEDxX-paDYKfPcvc52eFAAw3KrREHg8NJn0Dl2eUph8c8Plyff_ygv8EuZ53zIOTaSZxzS9D7caKEFsXjpA2ElmVgaW8bFWKyXTLVbfhKj6G0kVC4Av1GPfPD5Tbwd4zL8uJrqoOOWF7k0yrwgWPMAT0iFf8jrOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: ایران در طول ۱۴ روز گذشته، ضربات سختی متحمل شد.
🔴
آنها به ما درخواست بسیار مؤدبانه دادند و گفتند: "لطفاً دست از این کارها بردارید. بیایید ملاقات کنیم."
🔴
در حال حاضر، ما در این مرحله قرار داریم. باید ببینیم چه اتفاقی می‌افتد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137955" target="_blank">📅 20:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137954">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
ترامپ: از پوتین درباره ارائه تصاویر ماهواره‌ای از ایران سوال خواهم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/137954" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137953">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
ترامپ: حوثی ها اگر مزاحمت ایجاد کنند به آنها حمله میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/137953" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137952">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بنزین راهی ندارن گرون کنن شک نکنید …  فعلاً تو موضع رسمی می‌گن هنوز هیچ تصمیم نهایی اعلام نشده، ولی وقتی چند تا سناریو هم‌زمان روی میز بررسیه، یعنی اصل ماجرای تغییرات جدیه و فقط دارن روی مدل اجرا و زمانش تصمیم می‌گیرن. گزینه‌هایی مثل گرون شدن بنزین آزاد، تغییر…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/137952" target="_blank">📅 20:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137951">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
ترامپ : اونا می‌خوان با ما دیدار کنن و ما هم داریم باهاشون مذاکره می‌کنیم
این شانس وجود داره که به توافق برسیم.
🔴
اگه اون کاری که ما انجام دادیم نبود، الان حاضر نبودن با ما مذاکره کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137951" target="_blank">📅 20:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137950">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07935bf061.mp4?token=eFvehxrne1dYFQvm-Hd_djtioy1EepZpn9X6vK7743CMYBFCNOeAluPy84MYnYF1xvO1Mq-9toFh6KOwlnl_PiaPr96crfh-4allc9FBMJA8U6O1pL8zidFQSyrP2lMUdj8WRjICAt5FgwRqVmMg2g4iZ6rkjgcWnCyIeWOJQWnxHljl3MjuFkXUReLQvEXFKrG5pj6PRq71-281-PbtPJVw0f8OE3JPFMX9yezamCG30JUIIgxJrVZEM7fTH1qAnZNU12yIrl0WUyMTe8QS8YGc4JelXSDVhJsTFZOfH6mQ811mo_dnxawh1agqGvyocIl44Mz9t6u40ovkj0xYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07935bf061.mp4?token=eFvehxrne1dYFQvm-Hd_djtioy1EepZpn9X6vK7743CMYBFCNOeAluPy84MYnYF1xvO1Mq-9toFh6KOwlnl_PiaPr96crfh-4allc9FBMJA8U6O1pL8zidFQSyrP2lMUdj8WRjICAt5FgwRqVmMg2g4iZ6rkjgcWnCyIeWOJQWnxHljl3MjuFkXUReLQvEXFKrG5pj6PRq71-281-PbtPJVw0f8OE3JPFMX9yezamCG30JUIIgxJrVZEM7fTH1qAnZNU12yIrl0WUyMTe8QS8YGc4JelXSDVhJsTFZOfH6mQ811mo_dnxawh1agqGvyocIl44Mz9t6u40ovkj0xYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: در مورد جنگ ایران، آیا به دلیل توصیه‌هایی که هگستث در ابتدا ارائه داد و نتیجه‌ای که گرفت، از او ناامید شده‌اید؟
🔴
ترامپ: خیر، او کار بزرگی انجام داده است. ما ارتش آن‌ها را نابود کرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137950" target="_blank">📅 20:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137949">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
نیویورک تایمز : ترامپ در حال بررسی سه گزینه اصلی در مورد ایران است: تشدید اقدامات نظامی، تشدید تحریم‌های اقتصادی، یا اعلام پیروزی و عقب‌نشینی نیروها.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137949" target="_blank">📅 19:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137948">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
فوری / هم اکنون تیراندازی نزدیک کنسولگری آمریکا در تورنتوی کانادا
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137948" target="_blank">📅 19:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137947">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016013f411.mp4?token=TI-uZpzDUmyIsIcFe_MmeuvvDeymUQOoljIdNrLterVofoRoPTwbLYZFtNq34rxpIenbwip0TegIAGLX808xlwp56D_3BnQEdDhwl6sGwNnGzug9LuclpzRSu-AmHFW1yqsV9Vv9rxqwsFqgaA6K7PG0yVifv2MRmUByMGR0EAi7TQzthq3wr6n9skCOaz9WO-hEzljDFAlo24T5hCbV3MQLQn7lrZnc9VcKasjAQeWPMcAWtPwdF37qJp8C0jERI08DNQ_-oyVTRVugqstonjnYuuE-0y-plDH8P5KjZeXX5x_VZx-chqdSi9W6LCP4_A3uiX2zryXmxCweODYTHH-9TwOTZEVUh6F5OyMXcp1BlMzPuKutqzE5Rdg8J2WktsR617_H1WqBeTKVVcqkaMfsnfSxAHvShAp21q5TJcDQ0LXHGTv3BzgH5Z8PtHqKWeUQHiuiKRFfY36zdSiRrNWUOfXnD3kkRggGvusOdpjchpyGXH2quLrHHnzMCfyrPNyi0zsjBH-VPpeqBoFkJeIj8WXT-FgWKfmr6UsjVoSK2ItCzD08pSvsWRLqEar3y_Yx7JBRBKM0v2POlrejal5nv72uAYRc-gFZz-Nxnms5q9diKBjidccwMCMLKBX140w6cNm91rF32u77iMWYTk-iJLN0VAcLsCsKGHv8_yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016013f411.mp4?token=TI-uZpzDUmyIsIcFe_MmeuvvDeymUQOoljIdNrLterVofoRoPTwbLYZFtNq34rxpIenbwip0TegIAGLX808xlwp56D_3BnQEdDhwl6sGwNnGzug9LuclpzRSu-AmHFW1yqsV9Vv9rxqwsFqgaA6K7PG0yVifv2MRmUByMGR0EAi7TQzthq3wr6n9skCOaz9WO-hEzljDFAlo24T5hCbV3MQLQn7lrZnc9VcKasjAQeWPMcAWtPwdF37qJp8C0jERI08DNQ_-oyVTRVugqstonjnYuuE-0y-plDH8P5KjZeXX5x_VZx-chqdSi9W6LCP4_A3uiX2zryXmxCweODYTHH-9TwOTZEVUh6F5OyMXcp1BlMzPuKutqzE5Rdg8J2WktsR617_H1WqBeTKVVcqkaMfsnfSxAHvShAp21q5TJcDQ0LXHGTv3BzgH5Z8PtHqKWeUQHiuiKRFfY36zdSiRrNWUOfXnD3kkRggGvusOdpjchpyGXH2quLrHHnzMCfyrPNyi0zsjBH-VPpeqBoFkJeIj8WXT-FgWKfmr6UsjVoSK2ItCzD08pSvsWRLqEar3y_Yx7JBRBKM0v2POlrejal5nv72uAYRc-gFZz-Nxnms5q9diKBjidccwMCMLKBX140w6cNm91rF32u77iMWYTk-iJLN0VAcLsCsKGHv8_yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زوهران مامدانی، شهردار نیویورک:
من علاقه‌ای به وارد شدن در یک بحث و جدال با نخست‌وزیر نتانیاهو ندارم.
🔴
آنچه می‌خواهم بگویم این است که در شهر نیویورک، یکی از اولویت‌های اصلی من، حفظ امنیت شهروندان یهودی نیویورک و حفظ امنیت هر یک از شهروندان این شهر است.
🔴
ما می‌دانیم که در حالی که شهروندان یهودی نیویورک، اقلیت کوچکی از کل شهروندان این شهر را تشکیل می‌دهند، اکثریت قربانیان جرایم ناشی از نفرت، از همین گروه هستند. این غیرقابل قبول است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137947" target="_blank">📅 19:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137946">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
سنتکام : کشتی تجاری تغییر مسیر دادیم؛
۲ کشتی از کار انداختیم و ۲ کشتی هم بازرسی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137946" target="_blank">📅 19:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137945">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
سخنگوی کمیسیون انرژی مجلس:
حدود ۴ هزار مگاوات برق به دلیل جنگ از مدار تولید خارج شد؛ قطعی‌های برق جنوب به همین خاطر است؛ همچنان به ترکیه گاز صادر خواهیم کرد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137945" target="_blank">📅 19:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137944">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AUvZR728eoi-enfD7V3SDaaoFEznFTFvoniSnyXHiCD07Ch7ks1n9PMZ0NBA5fkBx46Yz6OFtVRGJ949LHZrs-06i7MYVlwPptC-zCYYSSxPJc40BCWUZMFtjH6FSyZEMPv_mRpS_TpGSZ-uTxPjpa1Jf9d3NuDuuJT0FX7ramHJ-OI51wmkjSnhghuxUCfeJtDrqpX1Q70PzOk2X9rK8v7e0JCDiySH6R_4MB8cdkaBp3f6fHr0x6T3h2t50cVlJpzbAycsz3MzD6FoKgmQkvFBp6AWatVspVJlbPs2n_Drz-4gS10hm_dPe7B5ZNgLHAG1xcdODhhuQ2x2xaZV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کرملین دیمیتری پسکوف:
پوتین بر هر موضوعی از الف تا ی مسلط است؛ او قادر به درگیر شدن در مناظرات آگاهانه با متخصصانی است که تمام عمر خود را در زمینه‌های کاری خود کار کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137944" target="_blank">📅 19:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137943">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
رئیس‌جمهور اوکراین، زلنسکی، برای اولین بار با نخست‌وزیر جدید بریتانیا، اندی برنهام، در کشتی اچ.ام.اس کوئین الیزابت در پورتسموث دیدار کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137943" target="_blank">📅 19:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137942">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ترامپ به آکسیوس گفت که همه کسانی که در مذاکرات با ایران درگیر هستند از او خواسته‌اند که حملات نظامی را از سر نگیرد و افزود که او معتقد است تهران می‌خواهد به یک توافق برسد.
🔴
ترامپ  گفت: «همه کسانی که با ایران سر و کار دارند از من پرسیدند: "'حمله نکن".
🔴
در پاسخ به اینکه چقدر مایل است به دیپلماسی زمان بدهد، پاسخ داد: «زمان زیادی نیست. یا سریع پیش می‌رود یا اصلاً.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137942" target="_blank">📅 19:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137941">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
فوری / ترامپ هم اکنون: در حال گفتگوهای عمیق با ایران هستیم و اگر موفق نشدند، به عملیات نظامی گسترده باز می‌گردیم
🔴
مهلت زیادی به مذاکره نمی‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/137941" target="_blank">📅 18:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137940">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری / ترامپ هم اکنون: در حال گفتگوهای عمیق با ایران هستیم و اگر موفق نشدند، به عملیات نظامی گسترده باز می‌گردیم
🔴
مهلت زیادی به مذاکره نمی‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/137940" target="_blank">📅 18:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137939">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9JnNiXIhKTlcK2xk_bmLME5BkLrS6EtlfHrGpVvxZLvM7cDhYXSetnbqh_wiN9ci2ABadiYGdYK7-yqH5RgXJ1gPgC3TWvSoJzSjgy-7XdxRpIk8_5SrgvF8TNaDY_nd9m5Z2k57LmkfnMldOD1h-5xmlW5_-XcxcuZQs_czWtK2241QyJdT-jyxB-g-1bYUa5tIh3vjCjWYqJBu7hWgIR-jugDSkBu-ADzW9rYOoUVYy2MdKV7azAPVqnUpccK7rD4G4CPDiUFH8Vu001_lF7tNFec8sz2PcJUA5KIzjsAqHkkeCHzccTNPtkctxPkN2rn0jj2wmCwXvcQNNz_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش خبرگزاری آسوشیتدپرس، میانجیان قطری و پاکستانی پیشرفت‌هایی در راستای از سرگیری مذاکرات بین ایالات متحده و ایران و همچنین احیای آتش‌بس موقت داشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/137939" target="_blank">📅 18:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137938">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X86BEkK267ijHTO0AF35UaqYdMREU3iLqR8sPmT5ae4CU5TfQQS5uLozcgRSUntgx8tEN4jqrhBZ6cgJY9lRzHB1Y6_Ueilx4X4NhuAvQFqDpLwWoDoncCQct1Pm9apMoTj3iPrd99RgCBqPziyO8y20v1CmjrmBoIFmk1yycaNDrE8Sps6YKwHHMFohze3x64eL4anaSKk4on-N-YYtENNGsGxFVN0QmzmV-bx72DX6ezDNPt4wmjLaHgXE_pELabMdCieg5vEQrZ7GIXRR_ahr33KfUhlC-rG22sYULC4mJQvzRCmwz-jvCfgc2hw7d-IRH3YoCPMokTRRL98ySQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کویت قراردادی به ارزش ۱۶ میلیارد دلار برای احداث خط لوله انتقال نفت خام با شرکت‌های خصوصی آمریکای شمالی به نام‌های بلاک‌استون، بروکفیلد مدیریت دارایی و کی‌کا‌ار امضا کرده است. این بزرگترین سرمایه‌گذاری مستقیم خارجی در تاریخ این کشور است.
🔴
بر اساس این توافق، هر یک از این سه شرکت، سهم مساوی از ۴۹ درصد سهام یک مشارکت جدید با شرکت ملی نفت کویت (KPC) را خریداری خواهند کرد. این شرکت، حق استفاده از خط لوله را به KPC اجاره خواهد داد.
🔴
کویت از این معامله، مبلغ ۷.۸۵ میلیارد دلار به عنوان پیش پرداخت دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137938" target="_blank">📅 18:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137937">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
معاون شرکت آب منطقه‌ای تهران: شنا در سدها ممنوع است؛ تاکنون ۲ مورد غرق‌شدگی در سد لتیان گزارش شده و از مردم خواسته شده برای شنا به محدوده سدها مراجعه نکنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137937" target="_blank">📅 18:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137936">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
خبرگزاری عمان:وزیر امور خارجه، بدر بن حمد البوسعیدی، در تماس‌هایی با تعدادی از همتایان خود در منطقه، تحولات جاری و تلاش‌ها برای کاهش تنش را مورد بحث و بررسی قرار داد.
🔴
وزیر امور خارجه با همتایان خود در منطقه بر اهمیت دستیابی به تفاهمی که ایمنی تردد در تنگه هرمز را تضمین کند، تأکید کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137936" target="_blank">📅 18:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137935">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eae8240a.mp4?token=Sw0Saubo_7YPjva0kW9KFnEED625QpgQMQn3ac-B_DTBOYASCl_oglzfrb1jub5soKPQbwNAwihx0nyzXy6xZb9jo0GAMYyLJzJdHXKChKhTJuXxXwt05l9IEl_x8ZnPIHY6qASr7b1x0uIMXuMtCo24pRmTI9-RRVHefl54fwk_MJ-8jbvPRCYlluK4qGbFPCJ_EFCJ7Y37cyWnuLBIZJrw8s8Wl0EghLd53HoNFUJ6x2rW0Tmk4cVpGYITtzSr5kHfKR366SnuiFFb4hinhSZkNMzUvA8idR_-VLiLk1l_RjvoEy42UdNQuF42bl0rckB57IuIw-uHiRAgaoAF7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eae8240a.mp4?token=Sw0Saubo_7YPjva0kW9KFnEED625QpgQMQn3ac-B_DTBOYASCl_oglzfrb1jub5soKPQbwNAwihx0nyzXy6xZb9jo0GAMYyLJzJdHXKChKhTJuXxXwt05l9IEl_x8ZnPIHY6qASr7b1x0uIMXuMtCo24pRmTI9-RRVHefl54fwk_MJ-8jbvPRCYlluK4qGbFPCJ_EFCJ7Y37cyWnuLBIZJrw8s8Wl0EghLd53HoNFUJ6x2rW0Tmk4cVpGYITtzSr5kHfKR366SnuiFFb4hinhSZkNMzUvA8idR_-VLiLk1l_RjvoEy42UdNQuF42bl0rckB57IuIw-uHiRAgaoAF7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
مسیرهای جایگزین پل‌های آسیب‌دیدۀ هرمزگان آسفالت شد
‏
🔴
این پل‌ها در حملات آمریکا آسیب دیده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137935" target="_blank">📅 18:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137933">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bad2169d47.mp4?token=sjJUIfbHaR6wrP1FIqiK2-GPVBsDvutp3ZTC6hwN6TwMHTbxfMIv8OkbWSlZ6D0T2kDnCExFrSe0zowx8PCxMNRjKPu2LvDhZgTkHs3gVvqLEzkhDcqH2Ah67VvmOl9hJKV0lPasR_1Ljm1RD5Ds_QHuoNMoESBRJM6WoxmUNpJZnio8ayd3p0bInPEhgZdjjvGgeikKb9P5BUtgr4bJ-WEXy1BzZAARATTI-5D5aMATWDkrmMGp4Gxe0oOHo92oI4QRW0GtfXM8GDGdrYu3tZAvs4UY_9iJNl7nS0T2E3nO8KbfauFnQQtW_mvgiMVtG1dapRci_8N1s8QBXMQ9PYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bad2169d47.mp4?token=sjJUIfbHaR6wrP1FIqiK2-GPVBsDvutp3ZTC6hwN6TwMHTbxfMIv8OkbWSlZ6D0T2kDnCExFrSe0zowx8PCxMNRjKPu2LvDhZgTkHs3gVvqLEzkhDcqH2Ah67VvmOl9hJKV0lPasR_1Ljm1RD5Ds_QHuoNMoESBRJM6WoxmUNpJZnio8ayd3p0bInPEhgZdjjvGgeikKb9P5BUtgr4bJ-WEXy1BzZAARATTI-5D5aMATWDkrmMGp4Gxe0oOHo92oI4QRW0GtfXM8GDGdrYu3tZAvs4UY_9iJNl7nS0T2E3nO8KbfauFnQQtW_mvgiMVtG1dapRci_8N1s8QBXMQ9PYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون مجلس، خضریان :
عمان به لحاظ حقوقی نمیتونه بدون هماهنگی با ایران تنگه رو باز کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137933" target="_blank">📅 18:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137932">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخنگوی سپاه: ما حقیقتاً از فرصت آتش‌بس استفاده کردیم و آمریکا نتوانسته از این فرصت استفاده کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137932" target="_blank">📅 18:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137931">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
روسیه به ایران پیشنهاد داده است که درصورت تمایل میتواند از خاک روسیه برای پاسخ به اوکراین استفاده کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/137931" target="_blank">📅 18:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137930">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل: ترامپ یک تاجر است، اما در مورد ایران بسیار ساده‌لوح است
🔴
مذاکره با ایرانی‌ها هیچ فایده‌ای ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/137930" target="_blank">📅 18:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137929">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZW8_T5SrR-wtSAW1tQfI3OahI6TiSthE8l-dtgffICXto1hijE1sv5LlDoC1mRyzy6migsdnbnBEUJLcp_H_4TZXyupDTWPXXLDQH0HXbo-XmwxXokcTrqHCWI_Cpb7YXR7XJJa96Zy0vfIRK3gcCF7H3ZPIjygD4Q5--cO6H_ngXbOtB90TnATMhExGCDP00bW7kFY8I6udnrIFYX8HmW-7KpIz_sFkIEqT7NeXD3K_w0Fgbsa-iYpREAx8vT8CkWSrL9P90IARtC6VAb0_Evpp4AyK707WfZ6lakVVifaKh3iYKU8j3BishTr7WGeDYMZc64tvmRtypB62o8B6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر ماهواره‌ای و ویدیوها نشان می‌دهند که دود غلیظی در مجتمع پایانه نفتی جنوب یانبو در عربستان سعودی، واقع در دریای سرخ، مشاهده می‌شود.
🔴
این مجتمع برای صادرات نفت خام عربستان، به ویژه با توجه به مسدود شدن تنگه هرمز، از اهمیت بالایی برخوردار است، زیرا یکی از دو نقطه پایانی غربی خط لوله شرق-غرب این کشور را تشکیل می‌دهد. نقطه پایانی دیگر، پایانه نفتی شمال یانبو است.
🔴
به احتمال زیاد، این حمله در شامگاه جمعه یا صبح روز شنبه، به وقت محلی، رخ داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/137929" target="_blank">📅 17:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137928">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqzDgXbEAHeqC-zjna3580GP31CwGmVqNGjb2ABhUkp-YBHiLrufO_-l2IM4rhkEGKwmOZr3jH_oa3_1a3OKYovZ1m5vC5-GWPpi5KuaGKwVyyztTAMiUqpdJ3XOQE1jEN04h9KrdacAInyx_bw-fqt4jvTR7mkwaIGakoohI6XwEwuQ-FNmWncCqXALmJxRoG83Jp1lWnYc0mptF5tcaM-mw1o7HjFwn0X_PyBaaijdsPoHMFmgFKZs1XDU0A17JwkPDzXabZy39cN8orgdY-zljCwz8ZassTFD6yuseDQgf5z_dsg_eH23t9TaFZG-GpHPdHjc2BXrfheaKTak3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مردم ایران با میانگین درآمد ماهیانه ۸۵ دلار در در بین کشورهایی که پایین ترین دستمزد ماهیانه رو میگیرن رتبه ی سوم رو بدست آوردن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/137928" target="_blank">📅 17:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137925">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uKOUoqnkEY1Dh-qcmEBIkH-nXaiQONtAJFykFV9zoe-yGHeeqA3GK9y4Wq-PZYy3onmUShRkWKc7L3JK1Nn6Jh2XMUUETFKRRg5TabtjE8bKdRJWhBKCYB80In0noRmccIKQOi-T22ntpz98n9KNcl1NA_4C5q69fzgC7TC23JkhlL9oiN1OOdkCm3bQpmiYhgz3hjRLH-9df5xURQ0AQp5uMAdaqyPsCOXWSR5oA_8JZ2GoFysgSaZ0jN5sZZoUwMGySHGYhkM03WhIldF4LFSNKc0Cuw1J_hEf_bmn1OgLtqm0klJqCKCjvEtXitsvg9RIXkcxipOvee8Rsbg6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vfZ8XrDfK90YShmPNnOlsxcoZ-2w2kJwZJ9iCFS_lXq6QbuC3_dxcANnMQHrkTk0kcW_KBpD6EufjHSgoBoZtjQuPmMoxVMQep0fS4kZglc1dk96japOBQbxT1wD1lgtx7S2VxNYRbtvVOew-wQ9rw9UcwSLHKKHy04JGwYrVg4D4R33FFfYYH1Go3wrYrhE0SxezV39cg4C1Zfyvadct72--MX1F3LlaB1m73voehDEvPvI00b07P6Z-eOCAkg2ScmCWw_eLPLX0loNcyrVx7YLOoAchcswt5t2eXBl32hGR2K5yCPkkYvmVYxg-w5bxrnwqcjLRyLEY2yBNdaYKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
نیما تکیدو به جرم برگزاری ایونت مختلط(اقدام علیه زیر شکم بعضیا) بازداشت و صفحه ی یوتیوبش توسط پلیس بسته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137925" target="_blank">📅 17:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137923">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2YNmQ1BhcWGX21TbTxOtOPJGDeNSz081wxL8CX5RiQoraMu0mxP_0slkoihwWya9OeUKll-QQsNFvwJPK8gr6tPKU2R4OKX3Gw0WpHqEpLaq9IRyKeZ4HaWeh5bvBkTdcb4C2WKTwmq5hzQUWaW5nQpr5Jv0A3IAIgLfFZqUs_ywKGRkuvzvc0s5CY9rkFPbrMY9YaQeebJQiwE6sGmiPxWTSCP-e374cmRd68sMN4n7GzppNjkSeP0Q5LI1S6ry7cDQspe8oSMwJe3Nezq15E4JAsIpMBcBxR0ieelPFrsOGQ5aBOyMIm4eD0WuBdv1TLmeWF3eXEw0Q2C9EhjLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IaRi1bPP9OJmSxrZY3IplcpTqoEGDk7xSWng88RiMp5Yl8E7v6DlTb45wM2C4BGAOs2YHR2XcTHlBZY_2MkYgTwUM2vlwRT5mdgRUP7sEUmHWRzAEI-Zv2KQua6GHvzN4fRtNA78RITFoRTvPzyiQ8AyRx7TMBMYaAxe0XADoPYncXEtmtLaXBBMRE_JlMRKZMjJI3y7kJpAggJXQY5v0tZTFAeYUwo03YH4z_2qMygXrRFg92EehDZKJNjgP67W3yCaWv4lJ1uXZVRA7Q_31kj6KKmNpXuAjf6HX1wMS20BOcCMrRhvPcSSJRigPhfbgCFbgNM3nzn8ecqJMjgn5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از خطوط انتقال نفت عربستان در شهر ینبع که توسط انصارالله یمن مورد هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137923" target="_blank">📅 17:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137920">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJv4fkM1JjiFVhLP2eRAVk4LBRRF3VIpLwxyRy5mESN1i4iugg1WhqxQ3J5OcHuMlJ8w8hG1rbuyrOB9s24ZLknVChakjezY-W50RoQMQ7sBMBx7abaWLGTHWrOl3GGUBFqb2cvPlwbTblOKLEcpw24c-fwc4BhmtLG01NOk2V1kvUgdMR19qOuNh_vVn9FzT7KyDgV85PuVfdAGCDsGylAEqQu_quZTBTyjq5JzzBIlngkFLlo2vDgwo5ObALiDoBVPYVKi0KNKq3lM_I5-9H8Mneo7z773aTVUSxomeas1kQQqZp8TS2hedIngn0CW6ynh3kMQ7WrW4Io3_2mAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf188f0688.mp4?token=q1RqZdWi247pL0DynhKhl9oEEsFiXPOfdF1L0LxR-Jvc6divaBbllhTOJ0hqZTKqioAF_8O1nZEiBl2ZvVVLD-h4lgc6f7Hmqejkwi1YtC8ZeIbU_L1lIhaF8cPXZizYMgOoLu0LsDVnF3rMyonO-xi8Lt9PacWV7hQKXSWaj-irElqRnuxlYkia-1-iFGIkxjnPbZks01gdGS6ct7TUwYRtbISKSukuAZUyEAKyak7vMB-t51jZ_n8QyHbLYTUvR0kvIvdFI2MzXH3MD9mDM1V9DfB7rcsN0GTDowkNMt1U929n9ymEoE87UPdf8QjZu6gLAWOth_kBgkI727UfoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf188f0688.mp4?token=q1RqZdWi247pL0DynhKhl9oEEsFiXPOfdF1L0LxR-Jvc6divaBbllhTOJ0hqZTKqioAF_8O1nZEiBl2ZvVVLD-h4lgc6f7Hmqejkwi1YtC8ZeIbU_L1lIhaF8cPXZizYMgOoLu0LsDVnF3rMyonO-xi8Lt9PacWV7hQKXSWaj-irElqRnuxlYkia-1-iFGIkxjnPbZks01gdGS6ct7TUwYRtbISKSukuAZUyEAKyak7vMB-t51jZ_n8QyHbLYTUvR0kvIvdFI2MzXH3MD9mDM1V9DfB7rcsN0GTDowkNMt1U929n9ymEoE87UPdf8QjZu6gLAWOth_kBgkI727UfoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
در حالی که وزارت دفاع عربستان اعلام کرد پهپادهای پرتاب شده از عراق را سرنگون کردیم اما تصویر ماهواره‌ای امروز از تاسیسات نفتی عربستان سعودی در بقیق منتشر شده که مورد اصابت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137920" target="_blank">📅 17:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137919">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b27761eb0.mp4?token=PS6KACaSKjd3nU7e8wA-htPQdS-taS3cu9qiL4RitBaTRvFXNoGw1ZRsGTZhw7OSqQjXXbgT4nWmy6aVPJEewu9F1tQzlhT0_rViouRDxJVUp3kv42hWnCr0QN5Oo5KegHe4T3k8HgB-FwzUyGksNCDfmXlmj1Tw4L5uyvSq5iBFfpdFVRJXNERl-y-jpG_EohtJDWz83ueiRXt0-6BtP_HrKTf15R2D__gwgiGSKTiIPnWqkkBDKRAcJlfJlcpodyVLBCIcYx2etUNiMyw28Kl-Gs6ZpBKygRwGiI5FoQUM_BgZ7FUpkGRj9dfhl1_Us1_QiR6ouQbJ3GK8fE4u0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b27761eb0.mp4?token=PS6KACaSKjd3nU7e8wA-htPQdS-taS3cu9qiL4RitBaTRvFXNoGw1ZRsGTZhw7OSqQjXXbgT4nWmy6aVPJEewu9F1tQzlhT0_rViouRDxJVUp3kv42hWnCr0QN5Oo5KegHe4T3k8HgB-FwzUyGksNCDfmXlmj1Tw4L5uyvSq5iBFfpdFVRJXNERl-y-jpG_EohtJDWz83ueiRXt0-6BtP_HrKTf15R2D__gwgiGSKTiIPnWqkkBDKRAcJlfJlcpodyVLBCIcYx2etUNiMyw28Kl-Gs6ZpBKygRwGiI5FoQUM_BgZ7FUpkGRj9dfhl1_Us1_QiR6ouQbJ3GK8fE4u0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن‌گویر، وزیر امنیت ملی اسرائیل:
من خوشحال خواهم شد اگر دستور اعدام یک تروریست صادر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/137919" target="_blank">📅 17:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137918">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0828052249.mp4?token=fMkNcO0pjjsGOJVOqFZj05yAPkeThM4R8LmT3yjaJiGYvOxeq6uAxv31uPV-MvtZMKfvJ5UJ0Ok6au4VSlbFbASndjdWDPkV_sgkco3NvfLKvcNIIsy58zl7g2VCZZH5TslsaIR7MTXPGaR2_x2DHXZo40tXsUP3dXf8y9IN9qnWijvVSF8YO1zPqiqRsy7laYvucNSkcTmv5TmMhpGLQylzsFnV-wuu72tCRkZ5A9e_C3KRaiRHI_mQsU9yymC8sFQDyYNS3tgLVzheZl7DYGI6bog7UUVpDsLQWAb-NmfwDN4N2o6ZcqU8RjmI9m5CHEgdDjOssaA8fWgld8crJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0828052249.mp4?token=fMkNcO0pjjsGOJVOqFZj05yAPkeThM4R8LmT3yjaJiGYvOxeq6uAxv31uPV-MvtZMKfvJ5UJ0Ok6au4VSlbFbASndjdWDPkV_sgkco3NvfLKvcNIIsy58zl7g2VCZZH5TslsaIR7MTXPGaR2_x2DHXZo40tXsUP3dXf8y9IN9qnWijvVSF8YO1zPqiqRsy7laYvucNSkcTmv5TmMhpGLQylzsFnV-wuu72tCRkZ5A9e_C3KRaiRHI_mQsU9yymC8sFQDyYNS3tgLVzheZl7DYGI6bog7UUVpDsLQWAb-NmfwDN4N2o6ZcqU8RjmI9m5CHEgdDjOssaA8fWgld8crJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس: ذخایر نظامی آمریکا رو به اتمام است در حالی که جوانان ایرانی زیر درخت موشک تولید می‌کنند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137918" target="_blank">📅 17:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137917">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMlzNs24liae848A0-MDCubzqDVFrJG53Fgdl6wPASy2i-yd4xApuC8J9pzn9D2R1AmejkYXgmpmUpuYtMePdXyfvMTowV7Seb-Za-LdE8sjAMeKV7eoiTqBB0-t3pYfTL_2RN05VJYLmunZscEhhbHUWSKRqpjPcmUHUzQ24Dr1nygA7SIEwQ2Pj49amKcvof7KEkWm_3Gc8AcGbwXtvpBaPdCO1--Rc6t2nymRyV45mz8X9cSqr8P9cw-dCtvPBXsky4ondaRgTod5rD_dzaEV1vuoSZELWvNY5yGLTwbQYgSiqIDxBUXdccZL2UnnBWcnwJWn2BenfJFtHOW92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تتر بار دیگر از ۱۹۰ هزار تومان عبور کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/137917" target="_blank">📅 17:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137916">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QphYDPatfEFUIa_jhSZgH97nJmpUAb4rMjgPddABQy1eMzZg4ilERh8eCMGnNrPOEg1KCXsxFkJdwX50YuKS0qOu1Y81ZZbS3P_bPah6REygpRq9bhHAATWu4FkLpUZNspp09KHT4RJdkpoFpxRA4apawAjku2xdwM4tfIL_vppxnutWOKzfRsmycN3VXakeTFr_Yi4c2e4BGiTtGgbEH6mt8f1cEcQtNhUBSSOMS6NgwWqbCbxL6-N_TBUmciwSRSfbwXaOIdiM5pZ4WdqUsOAyAOGIfJT1NT_6uFU8bi2cC1MM2gYWMvYKA5Fh87Tr_JZyYwg7ithPeGzS01vq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اندری سیبیها، وزیر امور خارجه اوکراین در پاسخ به توییت عباس عراقچی: «تهدیدات ایران غیرموجه و بی‌اساس است. رژیم تهران همدست مستقیم تجاوز روسیه به اوکراین است و با ارسال سلاح، جنگ جنایتکارانه مسکو را تشدید می‌کند، سلاح‌هایی که از سال 2022 باعث کشته شدن مردم اوکراین شده‌اند. ایران هیچ حقی ندارد که خود را قربانی جلوه دهد، چه رسد به اینکه تهدیدات خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند. ایران با این اظهارات، تلاش می‌کند توجه را از تروریسم روسیه علیه کشتی‌های غیرنظامی در دریای سیاه دور کند، که امنیت غذایی جهانی را تهدید می‌کند.
اما موفق نخواهد شد.حملات روسیه به آزادی تردد دریایی، محور اصلی جلسه اضطراری امروز شورای امنیت سازمان ملل خواهد بود، و ما انتظار داریم واکنش‌های قوی از سوی جامعه بین‌المللی شاهد باشیم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/137916" target="_blank">📅 17:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137915">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
معاون وزیر خارجه: در اسلام‌آباد طرف آمریکایی ۲ درخواست افراطی داشت و گفت اگر آن‌ها را نپذیرید مذاکرات شکست می‌خورد و ما برمی‌گردیم؛ ما درخواست‌ها را رد کردیم و گفتیم برگردید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/137915" target="_blank">📅 17:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137912">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sjD6Rz5jjJ1ljv8V-RukV43MG3pNGC6TeyxZX6zp6VESn4R3ORN0cOwVHit7E6Xvhw2xlOYtGl_fUr-j1N-rVflVDp_xPFx2PKyCmSgppnrwLaCgOra0t2krUrSxFY8Eq058t9o80tbqFcZDeO1V9_p1ajAPTglC1pnEReUi_lpjTdePDbiNZ2dAL6cylR0lbuGpbrOdmuVwLw1u-GddaHYr6QcIvji_fX-aTqqQxcMUY5v1y-ZMwHZoXDJN8h6a7qVBefzXsiR2kWA3hNWQyzsX8WYEwFT_eArif8R7DozpB9jb3x11A9xi0eljyYqsUb1z9wPQ98RB09PIk8EH_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJVYNMmAQETuvgrdMyxNI6w7ZeO_q3HOf74jdb7ZhhBOlQjYm2Ci48e09z6TNoZoyPKkqHPpFkPXsc0zllKfvXJT1O8YUyrvFO04a2A7REmqtX2d65MdDGHsHdX_r9GIcUK0S2izwBFv_aKGz8gQGbykhUlA0hfkiMBBu0U-XYlW-HhcwO6OoOvr8rv5UHmvMRc1LvLJwkb9OKYF7FtOawsoxmKsDnerrTALzEwa-wsbct7s40eTZp104ooUft62U4CMaAUY-zTyJFr-daje_2KMsLY8Yie7giheiaIZ8oQm3dMX7tIuKhIermp3dDDmOIz_FE2T4u2S8wgAo1wjbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8dd49a21f.mp4?token=QOaiFgox4ILWQQgkXkRjFHzbDdOcTWnKWmAPeASan_nJH4eCK-kryHmBmXfA6lH6R1I7z7Xx4qGa7I36afM3Jw32oqbqPT_jidmIcwxMydwsW1kgbms9ZFMrZsU6SUubq-9XhEmO0T2qwxl4RGPZwprZQQ50wXsjE2GXMENaR3ij24lk_a8R4o2QH1u9C9JyrSxuGBE6noP8w1hyOhB_6O9IAW6L36H4RWVgl-9sU1M-BcXTV1ZLPOZ9X-9yf_xDhQcOiIxK-Jn9wZu6LnM62GrSHZnHtOLdGhU0nmvkR0O6WiFT2sWLXFIgUAjQkiTnxLYhOwOB70EzV6162zo4lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8dd49a21f.mp4?token=QOaiFgox4ILWQQgkXkRjFHzbDdOcTWnKWmAPeASan_nJH4eCK-kryHmBmXfA6lH6R1I7z7Xx4qGa7I36afM3Jw32oqbqPT_jidmIcwxMydwsW1kgbms9ZFMrZsU6SUubq-9XhEmO0T2qwxl4RGPZwprZQQ50wXsjE2GXMENaR3ij24lk_a8R4o2QH1u9C9JyrSxuGBE6noP8w1hyOhB_6O9IAW6L36H4RWVgl-9sU1M-BcXTV1ZLPOZ9X-9yf_xDhQcOiIxK-Jn9wZu6LnM62GrSHZnHtOLdGhU0nmvkR0O6WiFT2sWLXFIgUAjQkiTnxLYhOwOB70EzV6162zo4lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
امروز تو صادقیه تهران یه تاور افتاده رو خونه‌ها و ماشینای مردم و این خسارات به بار آورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/137912" target="_blank">📅 17:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137911">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
بی‌بی‌سی:
از آغاز جنگ با جمهوری اسلامی ایران در ماه فوریه، بیش از ۶۰۰ سرباز آمریکایی زخمی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/137911" target="_blank">📅 17:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137910">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
سی‌ان‌ان:
موساد اطلاعات کوه کلنگ را به آمریکا داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/137910" target="_blank">📅 17:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137909">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYbUQVpRgqTPTThQPZ5Uj0ilWHK3guhsx_xTput0pBvj5Vr2YxJzf3ORyclzdGoKkhEtjlmbIWhrifFbAqoeTDruycb4VbXjVCSm8OOOlxJNHWSnRNsLaQH1NV-Euo2TTT4Rr9esOrRW_eEtXE2VmTF_bxqdtc2yruKY7B_hwogGWT9_XAchPc5qcafDTyBv8h1bpxz_-NERRd15azJsC4eHC-JBmrvA5NUhgzaywxycdcasCox8Ogcod7ruuhpkopvC69lD5lV1sYTs6TubpTdccOap1DEkdTAh0AymYv-4rwm8X8bZ6RdwPjtJtEbAbNrgduYI7K4csSAA4o4dgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حاجی‌بابایی، نایب رئیس مجلس : ما هیچ‌وقت با آمریکا به تفاهم نخواهیم رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137909" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137908">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
حوثی‌ها:
خطوط انتقال نفت عربستان را هدف قرار دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/137908" target="_blank">📅 16:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137906">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
شبکه سی‌بی‌اس: جنگ آمریکا و ایران موقتاً متوقف شد. ترامپ راه مذاکرات برای رفع بن‌بست تنگه هرمز را باز کرد، اما دولت او اعلام کرده تقویت نظامی ادامه دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137906" target="_blank">📅 16:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137905">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
بنزین لیتری ۱۰هزار تومانی تا چند روز دیگه تو جایگاه‌های سوخت ثبت میشه و هرکی ناراضی باشه میشه عامل کودتای صهیونی
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137905" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137904">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ایندیپندنت:
پس از حملات ایران به پایگاه‌های آمریکا در کویت، ارتش این کشور فراخوان جذب نیروی نظامی منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/137904" target="_blank">📅 16:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137903">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
میزان سوختگیری با کارت آزاد جایگاه‌ها در سه استان افزایش یافت
‏
🔴
نواز، سخنگوی صنف جایگاه‌های سوخت کشور: بر اساس تمهیدات جهت تسهیل در سوخت رسانی برای زائرین اربعین، میزان سوختگیری با کارت آزاد جایگاه‌ها در سه استان کردستان، ایلام و کرمانشاه از ۱۵ لیتر به ۳۰ لیتر افزایش یافت. سوختگیری با کارت سوخت شخصی ۴۵ لیتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137903" target="_blank">📅 16:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137902">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
دقایقی قبل به تاسیسات نفتی در شرق عربستان از خاک عراق حمله پهپادی شد، وزارت دفاع عربستان اعلام کرد پهپاد ها را در آسمان رهگیری کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/137902" target="_blank">📅 15:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137901">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgERP5YguZtJ9LcpnqxywA4k53RRNpl92jK-poFUYgm474GbAPv8g4m9ZZg2plo7JMTwf50abz9Yre2PhheAQMWLDoVW8QZqOmNKG6pJhB1rgHoy9ZoPLgFY85ujkG4HRQUBxy36kEaWh7vFzYWFdI8oKPtl0f5f7jqDgBMgBz4q_-lwXMAmUSWk7ZAS7uxdRm1UGIWYQ9KvZWLcosNIujJS-tq3YzoZDrMHki989fjb0hBSyQNRacdD0olerin2kebKoVUVfAKsTSfIqMGxQAkXkPgEcu3Rxl6HDXG9nNDNwK6uyG2GbJciE4hxgcZTooRQk8601_AGXnXvTvmwEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش روزنامه جروزالم پست، اسرائیل معتقد است که ترکیه در تلاش است تا از طریق شبکه‌های اجتماعی، بر انتخابات پیش رو در این کشور تأثیر بگذارد.
🔴
مقامات امنیتی می‌گویند هدف این کمپین، شکل‌دهی به افکار عمومی، ایجاد اختلال در روند انتخابات و تشدید اختلافات در داخل جامعه اسرائیل است. این مقامات، نام حساب‌های کاربری، پلتفرم‌ها یا سازمان‌های دخیل را فاش نکردند، همچنین مشخص نکردند که آیا این فعالیت‌ها تحت رهبری دولت ترکیه انجام می‌شود یا خیر.
🔴
این ارزیابی، ترکیه را در کنار ایران قرار می‌دهد، یعنی کشورهایی که مقامات اسرائیلی مشکوک هستند که در تلاش برای تأثیرگذاری بر انتخابات هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137901" target="_blank">📅 15:53 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
