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
<img src="https://cdn4.telesco.pe/file/groI5xTpwv63gfZoi6J4nCDzOlcRYiL7alhPvmfSys8QS9iuFLn3N4KNX-dCNvym4v7j0bdQxS-ogrXW9QKkfhpqlFGC3LOOBlCFSi8DRxzRuhYuE12uKp8IWm5Q8oYnn5Dd6VABPOEdQ4RbRomkd5R03bDxF0BH2YU7It7nbLOcUU9Cvz57HF-l9sqznIzP27GAnZa4Wd98L-up_IT86s7Q0swHckr9_HxE5knU8gqfbWkSkbl1uv0dmCtMAmd5XZjW_L0lexBSNtKYIUgxAC_TWi6gkWzI0GZNdqQS4Ab_2Urlor3LYszHLvS5KhYuyEDAEpu4KLX0Q9TxtVkY0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 139K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-10 13:43:38</div>
<hr>

<div class="tg-post" id="msg-69355">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/917485436c.mp4?token=FEOkF7gZuO8e_rhVzD4hp_Yi4tSK-VI2eVseVWC7DpjGTq3eWAco2U9UWPbONzB2TUXzFRYaDXRw4ji59epu_I1jJS3NxyQ1VNlPcC7bJkvRrgDqrw8GOWWyInlDXsaMf6P8FOF-WmIEB98d4A7lervTWwOlsIj3cwfO89sxDG7KuR5IRZ7-M68421MCMmL7tGtL7x_Av8Y-hLHCGgWRPaPO2Ds94Cdo_jWWjQlZy2YV8-IcE3004EBzuX80NihFdk2k9ckqk7gPHaMD6nS72ifAjggxxXfniVkuoG5uHnkoizRcAEk9QW2o2_wSUQSGMEx36qB0rWUwTVqUD0SNRJ_96tkQMBGsrsfvcSGy3wUM2CzzQG2ifjkFJCjZ2WVVmn4anLCqKkDwcbQBW2VpFQgYNWYIlKrdJLG2OYEGX_VaFUdeCEixOnY7hGFktL9G5HODfgBefl--uKC7aTWGgTkGwGGZ6HPVsDvrqjrryPKs48JsULjKnQg_wpO5qAb1x7IKEn9_cEM4HIWAsixJGBKgoR2WTf3j45esqHV4aGMWdG86beY2XyR0g5pwWjyj6mfuOE7Z9o7CaSyuRB7aEa5ypu2XxMBfrZ9ZInQpUBUOaZckMdonNWzfMWHt3BHlFP6yjGSNTEyqpoa1AaX5Da-VD9z-VFnkz--P8xQDcr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
آتش‌سوزی در یکی از پالایشگاه‌های استان اربیل در اقلیم کردستان عراق
@News_Hut</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/news_hut/69355" target="_blank">📅 13:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69354">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/532a951287.mp4?token=aqNQxIZn8qqI52meX3weeRolN44rtf-ffVN1710vghGa2buC7Z7klwwnEW-ZNnPbcuWDNVl_ddJLeTZI691aeXj-Ad_xtQCOW7kRHXr6r06g50_op_zC3QGRgFgC3Dx-U6nJUXGmUGEaa0k8hqWO0CFwbDXMoV4bJBfsXDq7BcL8KPa6Xfr8g5-TB22vKQFGUmU4XaPG98lxdkyd67SeDbJJ6oxyUazu3l7VieEb-Sm3mO09sQDBhswSjZ5pbMNWY4f-l-HVRi2rwhwJOuoVpaUvlKJ4Fygi8yfVVQgg_agnpTglbmCWP3x-nIb1iVrtgWRpz540hcjZKmbbtpntxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه لیلی فیلیپس پورن استار معروف که تو 24 ساعت با 2 هزار نفر سکس کرده بود!
دوس پسر لیلی: من اصلا از این موضوع ناراحت نیستم، چون اون واقعا زحمت می‌کشه.
مهم اینه که آخر شبا میاد پیش من، و اینکه من بوسیدن رو براش ممنوع کردم، اگه با بقیه سکس کنه مشکلی نداره، ولی فقط باید منو بوس کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/news_hut/69354" target="_blank">📅 13:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69353">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d26851041.mp4?token=oP1afYrT6-l0X7IVrHxjz2E4qXn8yu7WMwJm8Lil7yCSTAy_zCO6L1eRccbLr3njIRku36wFYyxZWfe0XNzUIcJZTKaWgZHJy0CdCKsfQO8chOuUGBiXAWVWzLQS3W1JQ_rDm3ChiycZBROP--yf2vfxdUVjkSNoTXZc6CK3bs-sYsBr40RmQjvyQ24HTDcW0UwL79qFBff0VQWTqsVPXbFhxvKujRqlxrEWNgjCAEbQhkbKQAqDsBvQ2txyo_9PSbZtr98s9XLyXX7Bv7Yz8s42Gv9DGCS-VOGvYMoceVdAhu0IpKvBG29dNggEHcEanhKQ_mP3uTicdTzwTxFTog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d26851041.mp4?token=oP1afYrT6-l0X7IVrHxjz2E4qXn8yu7WMwJm8Lil7yCSTAy_zCO6L1eRccbLr3njIRku36wFYyxZWfe0XNzUIcJZTKaWgZHJy0CdCKsfQO8chOuUGBiXAWVWzLQS3W1JQ_rDm3ChiycZBROP--yf2vfxdUVjkSNoTXZc6CK3bs-sYsBr40RmQjvyQ24HTDcW0UwL79qFBff0VQWTqsVPXbFhxvKujRqlxrEWNgjCAEbQhkbKQAqDsBvQ2txyo_9PSbZtr98s9XLyXX7Bv7Yz8s42Gv9DGCS-VOGvYMoceVdAhu0IpKvBG29dNggEHcEanhKQ_mP3uTicdTzwTxFTog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عوارض خوردن ساندیس زیاد
@News_Hut</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/news_hut/69353" target="_blank">📅 12:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69352">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=W6M45h0ohiDOIxmUAiZgQVKkysaZHHL27MkCGzHdFpsRQzkMH80HYT9YrFivuB8ioJP_UmwnmwL1hvnWW0UpNTnFu7D3J5zwlFCG701BsBn1Afb2QDKdXevB0XmxNKPWobbYe_lXysh3ZRyvMG8oXGfojQ5Ur2YzVXOb_mbteIK2DpQw59Mb0Nrflj80MM9hv5pGCT942v2TdVFXx3qtoOzEjayoaFd_xINYAdAJZ_8prjKh4jeqp49tKw5phjxl7tZbH0vvoLyTGi6HKgRvmcfRaoXo4W2rL6M4v3RH0JVuub1xVL9pcBSxKjIfN_aHUOK5Fy-GQHzg2DJv4tzQfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e653ac6e6.mp4?token=W6M45h0ohiDOIxmUAiZgQVKkysaZHHL27MkCGzHdFpsRQzkMH80HYT9YrFivuB8ioJP_UmwnmwL1hvnWW0UpNTnFu7D3J5zwlFCG701BsBn1Afb2QDKdXevB0XmxNKPWobbYe_lXysh3ZRyvMG8oXGfojQ5Ur2YzVXOb_mbteIK2DpQw59Mb0Nrflj80MM9hv5pGCT942v2TdVFXx3qtoOzEjayoaFd_xINYAdAJZ_8prjKh4jeqp49tKw5phjxl7tZbH0vvoLyTGi6HKgRvmcfRaoXo4W2rL6M4v3RH0JVuub1xVL9pcBSxKjIfN_aHUOK5Fy-GQHzg2DJv4tzQfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف: میخواستیم خبر شهادت رهبر را ساعت ۸ صبح اعلام کنیم اما تلویزیون‌های خارجی، زودتر اعلام کردند
.
در روز نخست جنگ و تنها یک ساعت پس از بمباران بیت، شهادت رهبر قطعی شده بود.
تا همدیگر را پیدا کنیم و هماهنگ شویم، ساعت ۸ شب شده بود.
قرار شد خبر را فردا ساعت ۸ صبح اعلام کنیم و از مردم بخواهیم به خیابان بیایند. اما تلویزیون‌های خارجی، [ منظور اعلام رسمی ترامپ]  خبر را ساعت ۹ و نیم شب اعلام کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/69352" target="_blank">📅 12:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69351">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⏺
سفارت آمریکا در اردن:
از شهروندان آمریکایی مقیم در خاورمیانه درخواست می‌شود که برای ترک در صورت تشدید اوضاع آماده باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/69351" target="_blank">📅 11:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69349">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=NG6lN-SmDBF1kEQyApB3wQbPvoCxwC8-d1UiqxSRMU9CBsWO3pUEK2dwINAhCg0cLhEj7eX8YcpHYJ4Nu8uNQ58UxzR5ie8g-eNYh7AfhATwbu4mc_kaQ_3HqE-SXRZsjqTHZCKYa3Uf8OQEsP8HevOErGcMtOlx8LXSLWMac19S1nll7k5S80U3n8Hfq-Vgrn2RLlz_b5lUW3SnNbmfJKfA80wwqwZar3bEtMz_UHnGOPuxtQouUJx2OEJbcrfJIUYlNZ3gvHGe8FEA6XPi6wYCJ8entl7JNyqYL6iaFKYW1VdxPgj3LpUNat3KHlK-34R0mT_qWkd-Du_yy1z7EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14b8168f8.mp4?token=NG6lN-SmDBF1kEQyApB3wQbPvoCxwC8-d1UiqxSRMU9CBsWO3pUEK2dwINAhCg0cLhEj7eX8YcpHYJ4Nu8uNQ58UxzR5ie8g-eNYh7AfhATwbu4mc_kaQ_3HqE-SXRZsjqTHZCKYa3Uf8OQEsP8HevOErGcMtOlx8LXSLWMac19S1nll7k5S80U3n8Hfq-Vgrn2RLlz_b5lUW3SnNbmfJKfA80wwqwZar3bEtMz_UHnGOPuxtQouUJx2OEJbcrfJIUYlNZ3gvHGe8FEA6XPi6wYCJ8entl7JNyqYL6iaFKYW1VdxPgj3LpUNat3KHlK-34R0mT_qWkd-Du_yy1z7EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک انفجار بسیار بزرگ در یک انبار مهمات در شهر خملنیتسکی، واقع در غرب اوکراین، رخ داده است که پس از آن، انفجارهای ثانویه گسترده‌ای نیز به وقوع پیوسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69349" target="_blank">📅 11:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69348">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71213a605e.mp4?token=HvV3YPFF7C6rwQGKWV4ObuAD7ud5WcupWaPsDbqs3SjP2tBNAvDPDRfwhcPjynGQihsBv8KxBFryOwB4vYwZuGPQLNJu0K9pFpmU4wzLvptweJv4vmXLqdJ7-BE0__OPvrsDhdGukdLp0NIraXAcE7uCT-vKTJiC9LyXT0_TLbi1PQ4q26v77CdUfJp_920rJrtJRPRVMQzpCs_vcSFMLsbwPbCWukmDz8rrf95xopbZESbqFodDD74hnPMsN9qE4pVKu0PEbe18-VQeuFVtVV3CeZug74Xb2Yk4DiAbBMjYWO5v8XdbKLuc59tPCrK5Cd9INFiDzOJtNvxpS-q0Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71213a605e.mp4?token=HvV3YPFF7C6rwQGKWV4ObuAD7ud5WcupWaPsDbqs3SjP2tBNAvDPDRfwhcPjynGQihsBv8KxBFryOwB4vYwZuGPQLNJu0K9pFpmU4wzLvptweJv4vmXLqdJ7-BE0__OPvrsDhdGukdLp0NIraXAcE7uCT-vKTJiC9LyXT0_TLbi1PQ4q26v77CdUfJp_920rJrtJRPRVMQzpCs_vcSFMLsbwPbCWukmDz8rrf95xopbZESbqFodDD74hnPMsN9qE4pVKu0PEbe18-VQeuFVtVV3CeZug74Xb2Yk4DiAbBMjYWO5v8XdbKLuc59tPCrK5Cd9INFiDzOJtNvxpS-q0Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
آمریکا و اسرائیل برای شدیدترین بمباران در روزهای شنبه و یکشنبه آماده شدن و ترامپ دستور حمله رو صادر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69348" target="_blank">📅 11:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69347">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqjS9yyQR9WE0qztcvrY3fG5xPdGFwIUVGAANHNz65sgGdvRNATLdVAJA5ShnfNgiMFZi5Wi-HT3N5h3fBQDrIFTz3m_TfZGySu3tHqqUN2DNh-_bYZEJG-5z20pj-Cd18YeVplF_um7JgmhBWEautwP4vlR5j5kXvhTGJJNLdn0F8ewMkD7ilpfWaspZPAU7JC9JsHXm4mponQ_q7l8q-SWGLKguymrlTmWSRfYyeZ2SSKkDeuIKZmQpa1BgCbIvQxWcLL7wvfmP_m9yhoFVDPuXNNUhzrd0f-E2VXOzoEhQ2LcAcansFzU7pnQlXjM_JdSvErfus1AvLc2vL8cYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دقایقی قبل یک کشتی در نزدیکی خصب عمان مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69347" target="_blank">📅 10:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69344">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=g0zP31UQ5gOpszwG4vWI175WMdQlfHxa08PCHGtRpn1sK9nA31W4h4BYZhrTXLaasBwAqjsx2ktdAEichwPDA3TJrdJKsQyzh5Njn_rqIwKRPh9rjHlEYPDSeSbYw-WZNHY1uhDoPQDq_fdCC3DlOgfZMuYVw3sFt2dRj7ozCa74PF-qLqVBCRRd9smcVA-mYDF5UMGkGxS7LTyTQyAfdvz5KvWmog5q6Z2NQQ66hlTAmrojBMARFtmcVQlWdyHXu5aeARz5zBpTX2Zpn3e6KvJJMhyiGTaN65D5QyTrDSpsv-DBwtTTC3j0fAVNNvyX6nIGxB0-NitkzhwGA9YrEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/383c08fc2d.mp4?token=g0zP31UQ5gOpszwG4vWI175WMdQlfHxa08PCHGtRpn1sK9nA31W4h4BYZhrTXLaasBwAqjsx2ktdAEichwPDA3TJrdJKsQyzh5Njn_rqIwKRPh9rjHlEYPDSeSbYw-WZNHY1uhDoPQDq_fdCC3DlOgfZMuYVw3sFt2dRj7ozCa74PF-qLqVBCRRd9smcVA-mYDF5UMGkGxS7LTyTQyAfdvz5KvWmog5q6Z2NQQ66hlTAmrojBMARFtmcVQlWdyHXu5aeARz5zBpTX2Zpn3e6KvJJMhyiGTaN65D5QyTrDSpsv-DBwtTTC3j0fAVNNvyX6nIGxB0-NitkzhwGA9YrEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
بروزرسانی از اسپانیا:
نزدیک ۵۰ هزار نفر از مراکش و الجزایر فرار کردن و غیرقانونی ریختن اسپانیا!
برای کنترل این مهاجرای غیرقانونی پلیس فرستادن که پلیس هم کتک زدن.
این مهاجرا ریختن توی فروشگاه‌ها دارن غارت میکنن، از مردم دزدی میکنن و...
مثلا از یه مراکشی رندوم میپرسن چرا اومدی؟ میگه توی مراکش رفیقمو به قتل رسوندم، مردم هم باهام بد رفتار میکردن، منم فرار کردم اومدم اسپانیا.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69344" target="_blank">📅 10:34 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69343">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=rIZM4F3uqhhyg0Y5hNunnUBHQNEKDvEoRvaBLpXo8RFy6k5RAEcRvVDaxvawEPcHUqhQQge2afxcJ0dDCM_87mmZ5bGNSaqFb18aPbMq13_TiyrHMtbSSPcDvoOJ8V_euAKhQL3ocNMel6QM8zHt6-pRH4ol6hhEqrghzL6AWtnUAALo8vzbQ7kejgFiH9jeC4tkzq9vNta91A2UVownMOZxVMSbkCzbx8WPrDnzvkF9tf8qWYslgm0gKgOID5Af10AKvVTLX19m3Jd5HWgwZRJJGZdgk4CHq1PfenVUCgapx458MHXRbfyDkLL7pOvq4dFN2OY1Yb4TIpIJuNLrBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/7cd4da48cd.mp4?token=rIZM4F3uqhhyg0Y5hNunnUBHQNEKDvEoRvaBLpXo8RFy6k5RAEcRvVDaxvawEPcHUqhQQge2afxcJ0dDCM_87mmZ5bGNSaqFb18aPbMq13_TiyrHMtbSSPcDvoOJ8V_euAKhQL3ocNMel6QM8zHt6-pRH4ol6hhEqrghzL6AWtnUAALo8vzbQ7kejgFiH9jeC4tkzq9vNta91A2UVownMOZxVMSbkCzbx8WPrDnzvkF9tf8qWYslgm0gKgOID5Af10AKvVTLX19m3Jd5HWgwZRJJGZdgk4CHq1PfenVUCgapx458MHXRbfyDkLL7pOvq4dFN2OY1Yb4TIpIJuNLrBjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
صحبت‌های عادل فردوسی‌پور درباره ماجرای دست‌بوسی عباس صالحی :
تو عُمرم دستِ مسئولی رو نبوسیدم!
عباس صالحی وارد مسجد شد و کاملاً اتفاقی روی صندلی کنار من نشست. به شوخی بهش گفتم اگه یه روزی فیلتر 360 برداشته بشه، همه این نشستن شما کنار من رو ربط میدن به رفع فیلتر!
همون موقع که داشتیم دست می‌دادیم و روی صندلی جا‌به‌جا می‌شدیم، شب دیدم یه ویدیو وایرال شده و با یه تیتر زشت نوشتن که من دست عباس صالحی رو بوسیدم.
اگه قرار بود دست‌بوس باشم که الان برنامه 90 رو داشتم و 360 رو هم فیلتر نمی‌کردن.
چطور ممکنه من برم تو اون مسجد، بین اون همه آدم، بیام دست عباس صالحی رو ببوسم و برای خودم حاشیه درست کنم؟
من همین چند روز پیش هم گفتم؛ بله‌قربان‌گو نبودم، نیستم و نخواهم بود!
همیشه روی اصول خودم ایستادم و سعی کردم کنار مردم باشم. واقعاً این حجم از هجمه‌ای که به من وارد میشه حیرت‌آوره.
من عاشق کارمم و اینو خودشون هم می‌دونن، ولی نه به هر قیمتی. اگه شرایطش فراهم باشه، تو فوتبال 360 به کارم ادامه میدم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69343" target="_blank">📅 10:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69342">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=HGvuXuXclK7XGX2a2Y6f3VzzXdurC3ap0yFIxmYeKUgphfJm9v50NPCGAEVbuSbwQGV1ghKymfXHXgvbnTbPLyEcKGf4w4EHcOioHew604Mthvc_m3SIScWWpiM4460dJKrQFGgcRthSuRo0ofZgz9-BixGPXd9T7wIIxLCsytGu3QGsDpapWKYgXBUXw6-DNuDP-eySANJMx4Fl8Hz5uMhN-avbRbqHrTdVRZsajShH2EOk2Oq0Pc3tVr-9Ql_pU5H_Vq5Rm7zBfa6o2op5VdcvLQlj5l45LtZrY0q08kP3idlDt0OlbN3C1fRBVW5Tl1Hmp5lmYy3D5so3u9lX9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d1e6179c.mp4?token=HGvuXuXclK7XGX2a2Y6f3VzzXdurC3ap0yFIxmYeKUgphfJm9v50NPCGAEVbuSbwQGV1ghKymfXHXgvbnTbPLyEcKGf4w4EHcOioHew604Mthvc_m3SIScWWpiM4460dJKrQFGgcRthSuRo0ofZgz9-BixGPXd9T7wIIxLCsytGu3QGsDpapWKYgXBUXw6-DNuDP-eySANJMx4Fl8Hz5uMhN-avbRbqHrTdVRZsajShH2EOk2Oq0Pc3tVr-9Ql_pU5H_Vq5Rm7zBfa6o2op5VdcvLQlj5l45LtZrY0q08kP3idlDt0OlbN3C1fRBVW5Tl1Hmp5lmYy3D5so3u9lX9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سیدمحمود نبویان، نماینده مردم تهران، درباره شاهنشاه آریامهر؛
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/69342" target="_blank">📅 09:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69341">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی،…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69341" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69340">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ubIFrIVmfrTWHnuCtbRzu9qoW7Z-60em047zEXd40AcIRseJ5178qUKDUbLuEsoQu4v4e1C1EGV0rV9aXC2UNR64NuWSAGkWJun1LEXmDPE5JDqSQrZD2yY0Qx7Zqfh5ktVWg2TV0pJJbZVUe5ujp6XAcfy-jQPw3XjSwvEHway5b0XoA12PgJLTnQNL1LlzKNkyffKgatA12xmYiAjsk8e-QHrYmeMJOZtJoNYcTz20rRvxdXr37MQidt3rO8TTw3tbW2sAodSCUnfOmGNPgBjrK8mY0iGB55CRTqYBp2rRparGohcKAI7pQEf2Tme6XaFOcN231ukuodXk5v_bKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=ubIFrIVmfrTWHnuCtbRzu9qoW7Z-60em047zEXd40AcIRseJ5178qUKDUbLuEsoQu4v4e1C1EGV0rV9aXC2UNR64NuWSAGkWJun1LEXmDPE5JDqSQrZD2yY0Qx7Zqfh5ktVWg2TV0pJJbZVUe5ujp6XAcfy-jQPw3XjSwvEHway5b0XoA12PgJLTnQNL1LlzKNkyffKgatA12xmYiAjsk8e-QHrYmeMJOZtJoNYcTz20rRvxdXr37MQidt3rO8TTw3tbW2sAodSCUnfOmGNPgBjrK8mY0iGB55CRTqYBp2rRparGohcKAI7pQEf2Tme6XaFOcN231ukuodXk5v_bKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چقدر روی فوتبال باختی تا حالا؟ وقتش نیست سبک بازی تو عوض کنی؟
💸
دیگه دوران شرط‌بندی روی حس و حال و شانس تموم شده. اگر دنبال تحلیل‌های دقیق بر اساس آمار، فرم تیم‌ها و نرخ مصدومیت‌ها هستی، باید جایی باشی که تخصصش همینه.
🔹
تحلیل اختصاصی بازی‌های روز (جام جهانی، باشگاهی و دوستانه)
🔹
پیشنهادهای دقیق گل بالا/پایین (Over/Under) و گلزنی هر دو تیم (BTTS)
🔹
بدون ادعای واهی ضریب ۱۰۰! فقط سود مستمر با مدیریت سرمایه.
آمار ما در ماه گذشته خودش گویای همه‌چیزه. فرم‌های امروز رو از دست نده
👇
🔗
[
ورود به کانال و دریافت فرم‌های رایگان امروز]</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69340" target="_blank">📅 02:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69339">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس لیست اهداف انرژی منطقه رو منتشر کرد:مهم‌ترین تأسیسات انرژی جهان در تیررس موشک‌های ایرانی؛
❌
میدان نفتی غوار در عربستان
غوار ستون فقرات تولید عربستان است و هر گونه اختلال در آن، بیش از ۵ درصد از کل عرضۀ نفت جهان را به خطر می‌اندازد.
❌
تأسیسات ابقیق و خریص عربستان
قلب ماشین صادراتی عربستان که نفت خام میادین غوار، خریص و شیبه را تثبیت و برای صادرات آماده می‌کند.
ابقیق نیز تنها نقطه‌ای است که بیش از ۷ میلیون بشکه در روز از آن عبور می‌کند و هرگونه آسیب به آن، علاوه بر ایجاد بحران در صادرات نفت عربستان، زنجیرۀ تامین پتروشیمی‌ها و نیروگاه‌های داخلی و حتی آب‌شیرین‌کن‌ها را مختل می‌کند.
❌
پالایشگاه الرویس و میدان نفتی زاکوم در امارت
زاکوم دومین میدان بزرگ فراساحلی جهان و صاحب صادرات روزانه بیش از ۱ میلیون بشکه نفت خام است.
❌
میدان گازی گنبد شمالی و تأسیسات ال‌ان‌جی راس‌لفان قطر
بزرگ‌ترین میدان گازی جهان با ۲۵ درصد ذخایر اثبات‌شدۀ جهان؛ راس لفان تک‌مهم‌ترین پایانۀ صادراتی ال‌ان‌جی جهان و مسئول حدود ۲۰٪ از کل تجارت جهانی ال‌ان‌جی است.
❌
میدان نفتی برقان کویت
بزرگ‌ترین میدان نفتی کویت با ذخیرۀ حدود ۶۷ میلیارد بشکه؛ برقان یکی از میادین کلیدی است که در بحران اخیر، ۲ میلیون بشکه در روز از تولید کویت را از مدار خارج کرد.
❌
پالایشگاه ستره و تأسیسات المعامیر بحرین
بحرین به دلیل وابستگی شدید به این تاسیسات، آسیب‌پذیرترین کشورهای شورای همکاری خلیج‌فارس در برابر اختلالات انرژی محسوب می‌شود
❌
میدان‌های گازی لویاتان و تامار اسرائیل
ویاتان بزرگ‌ترین میدان گازی اسرائیل و تامار دومین میدان بزرگ آن رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69339" target="_blank">📅 02:11 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69338">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWQ29HRBg2z_Mw4KjL5ZfryP8yLHViGyhftSRAaouPLohKcXCmw2kYOIh-BsWkOSihQEL8TIVQ06kQkEV3KEcS0ZGcRIYV1YtwyZAMcCpkjTPf0OrogLpeJMu9jukaibvjkl44zKehvEyiFdQpg5wARB1hz721fL3ZLhVlbH06iVY4qpLzcAkjT3gL0uAVj0hm8Yj3NkwKKpvGYp_En9OaXVnJA7_8nB51t-PBiiSoPzuJoBuUkyCFny1z9RbHmh_7jFz4QY_YshHgjTMGVebIR9jCFd893jUWlEGpqOXCPuwJQhk_6tz9DIs7BG-ETCduP23fGzagKSPstPLobh9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:یه مقام ارشد امنیتی به ما‌گفته؛اگه آمریکا یا اسرائیل بخوان به زیرساخت‌های ایران حمله کنن؛
ایران از قبل یه برنامه گسترده برای جواب دادن آماده کرده.
به گفته این مقام، توی این برنامه، زیرساخت‌های حیاتی اسرائیل و تأسیسات انرژی آمریکا تو منطقه هم جزو اهداف در نظر گرفته شدن.
نیروهای مسلح ایران توی جنگ 40 روزه و اتفاقات هفته‌های اخیر نشون دادن هم توان انجام چنین عملیاتی رو دارن و هم برای انجامش اراده لازم رو.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69338" target="_blank">📅 02:01 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69337">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7lHQXPE7qKFL0HhEJRxcvfFziZckvIFNzPAgfmoiej3hdAatRjjD4TSqyz2U76QudfbRnIGTbVFNhYbktPVob4TutvcBed0TvocL6P_DxXv1bt3vFBB790PineDaVkuhwEtxp5kkf7tNjKPYOP91SavAr3StiEVAbS6Ik0YJT5VgItc93cIIT9lpaLLR9fXXxpd05VcQs6jJLuH7tC_8L44_kMFn12cyHDCI0jV3FEYUutlWdC-k9RcQigvglytQdQIZLdi23di2FY9hwClmVj3iFm8MPoDFo5jjNPDWPfD292LhYNyTBHEEoqOv6hQDYojZwtPJgyl5nf5eHsNsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛آکسیوس:ترامپ در حال بررسی حمله به تأسیسات انرژی ایران ظرف چند روز آینده است.
یک مقام آمریکایی روز جمعه به «اکسیوس» گفت که رئیس‌جمهور ترامپ به‌طور جدی در حال بررسی انجام حملاتی علیه تأسیسات انرژی ایران در چند روز آینده است، اما هنوز دستور نهایی برای اجرای آن را صادر نکرده است.
این حملات همچنین ممکن است برای نخستین بار پس از چندین هفته، ارتش اسرائیل را نیز درگیر کند و چنین تشدید تنشی احتمالاً به حملات موشکی ایران علیه اسرائیل منجر خواهد شد.
سی‌بی‌اس نیوز و وال‌استریت ژورنال نخستین بار درباره حملات احتمالی گزارش دادند.
ترامپ در آغاز جلسه روز جمعه کابینه، با اشاره به حمله احتمالی گفت: «خب، ما ضربات بسیار سختی به آن‌ها وارد خواهیم کرد و می‌دانید، بالاخره زمانی فرا می‌رسد که آن‌ها خواهند گفت دیگر تاب و تحملش را نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69337" target="_blank">📅 01:49 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69336">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh6iPzDhPdwlduq07g7itP38E8Ac_7vc7XMh7-VLJrcqiZOdNzAD_li_JdygVvKTDTFkBzYvqI8ao4HLIcH9h3ZxF0aH5uU5SASFnXVoVjOknPI3uGBAqApCMv0O0-t7Fa3O66337dY-0_DtBLPyPuArKVrbtA4zJsbmZ_nwTAXrXJAwsfzBBUKKRyRG7g8YeX5Gp_6tjF8JwuGJ0mGaUlPiCbWa3RwFFsFOAiW_r1BZQHUGW68K_Ip9FbQJDCOnbNZERnIzPAZN7Bro2-pGC4dlF-P4ckw2JSnqAiDouPuOe0HNhtY4uV5yiSPjjeWd3YvkP_IrzUUNU1g2B15Row.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
🇮🇱
سی‌بی‌اس نیوز:
ایالات متحده و اسرائیل در حال آماده‌سازی یک کمپین بمباران مشترک بزرگ علیه زیرساخت‌های انرژی ایران، از جمله نیروگاه‌ها و پالایشگاه‌ها هستند.
ترامپ هنوز تأیید نهایی را نداده است، اما حملات ممکن است این آخر هفته آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69336" target="_blank">📅 01:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69335">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5040574e14.mp4?token=SH7JVFr2wPhWBiSL2IQfVV0QOVFlg9bVaMA3Rid1L9f8izYpnvj-u8wZc98tUVixCnVU6bHFyjNFqbRC8QZoUIROG9Rk_4wyowVgkAaTbViLEdbW8H7Bj7BwYHgNz-VMWtZB9BzhhunKMBtkUFxVbPeEb7tUFZxKVh27ST2IuRrOvrdRYO3bQfuDTNI0IoFgDe_fgsUgwsyV7dWUa8LfJguo11dMIbdYJBThyl1PL1BG6zb9qjVgKWtpI4L2fORSsv2mWuq8je8j9m3W76BAXnMsaCgcZcFcYjoIJ9Dlpn3RvsC_URbzdzzk7eAq2xmdYdUHVRDA_N-er84E0pbAIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5040574e14.mp4?token=SH7JVFr2wPhWBiSL2IQfVV0QOVFlg9bVaMA3Rid1L9f8izYpnvj-u8wZc98tUVixCnVU6bHFyjNFqbRC8QZoUIROG9Rk_4wyowVgkAaTbViLEdbW8H7Bj7BwYHgNz-VMWtZB9BzhhunKMBtkUFxVbPeEb7tUFZxKVh27ST2IuRrOvrdRYO3bQfuDTNI0IoFgDe_fgsUgwsyV7dWUa8LfJguo11dMIbdYJBThyl1PL1BG6zb9qjVgKWtpI4L2fORSsv2mWuq8je8j9m3W76BAXnMsaCgcZcFcYjoIJ9Dlpn3RvsC_URbzdzzk7eAq2xmdYdUHVRDA_N-er84E0pbAIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مهاجر مراکشی درحال رفتن به منطقه برون‌بومی اسپانیایی «سئوتا»
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69335" target="_blank">📅 01:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69334">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.   مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69334" target="_blank">📅 01:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69333">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQMQFNbbmuyn5It6LttqdteVTwTKCG-w26gU5jT7pNz3xIYNdC7BIVMybMleVphQpoo3sB4PAAwd3PENK30M5SQCELb6ys0g88mPY-iefrPW8fcTSXUus0K64j2qEYyn5dh9cvuRG4GDTGM_KsNfv2jA8Li9CaY5-3bD9VYTOPcBZUAvBbbYH14yBrnxpRnAPH-yQ02EfL5OPW3L_Nd9d_7lxkdBV94hn5gTSYVhN--oxgNp0QQ6jLc6n4Ck55TOV0wY-qhL3cnd71OTL_fYaAVSd9xz9CrAxjbVlqVukAcyGLvShiulBhJ7DUk6b2VR_qsCpxeAZHOcbf43w_ukoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛وال استریت ژورنال:ترامپ دستور حمله جدیدی به ایران را صادر کرد.
مقامات آمریکایی اعلام کردند که رئیس‌جمهور ترامپ دستور حمله جدیدی را به ایران صادر کرده است که هدف آن وادار کردن تهران به تسلیم است؛ این حمله ممکن است از همین آخر هفته آغاز شود و چند روز به طول انجامد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69333" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69332">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">چندین منبع به CBS News گفته‌اند که حملات ممکن است در طول آخر هفته انجام شود</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69332" target="_blank">📅 01:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69331">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=uK_vZcItIB2MJ0y-ZcfE3nuQslpiQ-FYU8rvDcPNDKDfbjzKmtjYSVwjrYGS5wkw_H2e_iHHtdZBzvxQwOQHGIrAKiouxUaQvi-nE6sQZxlSr3cUloC423e5hTCpf1zHhkcvuKeeTsCiSPs_oMvLM843XNaqS1YYxVpRnbaguM7InT8lNHzVqk9ETTVi2KowVVYSE3tw3YJHY9dKFn7KdJND3k8bY0x7EgJ7N9AWj2zXc_Z_wn1HOn1vd79JAzHFRlwuAXcC5BGtnBovUyPGjdVl_XzVCQ27zxl3qa02iapiXw-eV7n9fXcEQ6Frtd1ZztSeZEA_t3N6igxd1pT_3IUZwp81pMEPcqqH7xkVdJ41SYxGjU9hz-fV3Z-Tfd9bUWKNQS4GwXq5H-An-_ZnwPsFIKrs0KC9MBYs4cUB1vNxfgO1K5NRNDX9_4fdhnDANyJQ5L3pnvu8rUUz_HZN6HdDOQiJ400I7XcBFBDu1OulVPdfvZKXkhaeYCnxxp43cqVO6yZUrwMMzX13l_SKfiXmV3OL8-ey7Sil3J4YZ4VqxGzYq1gENVx0efq7AyXix_BEpex_v1Crgy48Zl9w9SwGVh5ceBr9gXAgiIx9f2mOuq8ayOSiilnAwBcilfg1EgaRIq9Te3mRFPT_gtdSU-IWFoNHFEoBKR0RpyGopwM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3b500b5c2.mp4?token=uK_vZcItIB2MJ0y-ZcfE3nuQslpiQ-FYU8rvDcPNDKDfbjzKmtjYSVwjrYGS5wkw_H2e_iHHtdZBzvxQwOQHGIrAKiouxUaQvi-nE6sQZxlSr3cUloC423e5hTCpf1zHhkcvuKeeTsCiSPs_oMvLM843XNaqS1YYxVpRnbaguM7InT8lNHzVqk9ETTVi2KowVVYSE3tw3YJHY9dKFn7KdJND3k8bY0x7EgJ7N9AWj2zXc_Z_wn1HOn1vd79JAzHFRlwuAXcC5BGtnBovUyPGjdVl_XzVCQ27zxl3qa02iapiXw-eV7n9fXcEQ6Frtd1ZztSeZEA_t3N6igxd1pT_3IUZwp81pMEPcqqH7xkVdJ41SYxGjU9hz-fV3Z-Tfd9bUWKNQS4GwXq5H-An-_ZnwPsFIKrs0KC9MBYs4cUB1vNxfgO1K5NRNDX9_4fdhnDANyJQ5L3pnvu8rUUz_HZN6HdDOQiJ400I7XcBFBDu1OulVPdfvZKXkhaeYCnxxp43cqVO6yZUrwMMzX13l_SKfiXmV3OL8-ey7Sil3J4YZ4VqxGzYq1gENVx0efq7AyXix_BEpex_v1Crgy48Zl9w9SwGVh5ceBr9gXAgiIx9f2mOuq8ayOSiilnAwBcilfg1EgaRIq9Te3mRFPT_gtdSU-IWFoNHFEoBKR0RpyGopwM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«قیمت‌ها حسابی اومده پایین، به‌جز نفت.
دو هفته پیش، وقتی همه فکر کردن توافق نزدیکه، قیمت‌ها مثل سنگ سقوط کرد.
ولی ما یه
توافق واقعی
می‌خوایم، نه یه توافق الکی.»
🎙
استیو گروبر:
درباره ایران، فکر می‌کنید چقدر طول بکشه تا این ماجرا تموم بشه؟ یه ماه؟ یه سال؟
🇺🇸
ترامپ:
«پیش‌بینی کردنش همیشه سخته.
ما ماجرای ونزوئلا رو توی کمتر از یه روز جمع کردیم.
اگه می‌خواید همه‌چیز خیلی سریع تموم بشه، کافیه به یه عده سلاح هسته‌ای بدید!
اون‌وقت همه‌چیز خیلی سریع تموم می‌شه.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69331" target="_blank">📅 00:31 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69330">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=dX35bne9RlhwtQ5JhL9PyP3-iJA15sfxBpIgke5mgcA_5mBI45lQjAly2-d_7IK_zmZpy43BOIRQwQewr6KyGGkX9aNMJzERuWrsTgWP2WuwtPcCEEL0OODudy0749XzcQSdKsD458fG1rHuY8XIa9Xce2zRZaBg3k2AwO3y5_54J0UGXN5MNq4GJkJw05E8JoT7Hht9SPW0LSTjwt8RE0t_-UhxgYpjd6oUWCFIZqQnvpNlwqjQ9ea0gPoDoWY1B3j0rEiYtYYfcMvlr1h4wM_09vw_N-n4YPWOUY1swVgNZemNsz6Nz0oqcxOlrGKTFk7Ek7HwYwER0JWUoKYwXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7487679e0.mp4?token=dX35bne9RlhwtQ5JhL9PyP3-iJA15sfxBpIgke5mgcA_5mBI45lQjAly2-d_7IK_zmZpy43BOIRQwQewr6KyGGkX9aNMJzERuWrsTgWP2WuwtPcCEEL0OODudy0749XzcQSdKsD458fG1rHuY8XIa9Xce2zRZaBg3k2AwO3y5_54J0UGXN5MNq4GJkJw05E8JoT7Hht9SPW0LSTjwt8RE0t_-UhxgYpjd6oUWCFIZqQnvpNlwqjQ9ea0gPoDoWY1B3j0rEiYtYYfcMvlr1h4wM_09vw_N-n4YPWOUY1swVgNZemNsz6Nz0oqcxOlrGKTFk7Ek7HwYwER0JWUoKYwXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
توی درگیری با ایران، بسته به اینکه چه آماری رو حساب کنید،
16 تا 18 نفر
از نیروهامون رو از دست دادیم؛ که همین هم خیلی زیاده، چون حتی از دست دادن
یه نفر هم زیاده.
جنگ ویتنام
21 سال
طول کشید. ما تازه وارد
ماه پنجم
شدیم، ولی همون‌ها که آمریکا رو 21 سال توی ویتنام نگه داشتن، حالا می‌گن "چرا ماجرای ایران این‌قدر طول کشیده؟"
من الان دارم کاری خیلی بزرگ‌تر از چیزی که اول گفته بودم انجام می‌دم. قرار بود فقط وارد بشیم، توان نظامی ایران رو نابود کنیم و برگردیم.
ولی بعد دیدم اگه فقط این کار رو بکنیم و بریم، دوباره خودشون رو بازسازی می‌کنن. برای همین باید یه جور
کنترل و نظارت
هم وجود داشته باشه، وگرنه دوباره همه‌چیز رو از نو می‌سازن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69330" target="_blank">📅 00:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69329">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=sVDALzo-PCTFDZfsmpMk61QwLICa9nI-Z7wcSrFRhY9AnPw4TNjz5xL-uF2Xx2uemZWcZJTrByXe_A8CGTEoGplh7IhxFx905uv2PlSC6_HfkRPhvO676NfWD63sLexqxKY-6xHF9qo_fRQqvs4XLnLXL0cXV4IH12rjlDK0SVPl7xq4ZQo-f3lnv-XiVve87WZsghkLKMfUk_DSNGlelZtpwX3cd4UEdxtjkNqDqF4lBM5wA3HpcHjayilJD6VvtFW4qSKc5h5c_mhW8IqgPHGb1rxsN6iMSxUILphesR9v5Vo4S5A_4MpT7-HNkhx7nOuzE1P0hHlYwH8wT2t1EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdc86e1f9d.mp4?token=sVDALzo-PCTFDZfsmpMk61QwLICa9nI-Z7wcSrFRhY9AnPw4TNjz5xL-uF2Xx2uemZWcZJTrByXe_A8CGTEoGplh7IhxFx905uv2PlSC6_HfkRPhvO676NfWD63sLexqxKY-6xHF9qo_fRQqvs4XLnLXL0cXV4IH12rjlDK0SVPl7xq4ZQo-f3lnv-XiVve87WZsghkLKMfUk_DSNGlelZtpwX3cd4UEdxtjkNqDqF4lBM5wA3HpcHjayilJD6VvtFW4qSKc5h5c_mhW8IqgPHGb1rxsN6iMSxUILphesR9v5Vo4S5A_4MpT7-HNkhx7nOuzE1P0hHlYwH8wT2t1EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه هموطن که تو خونش کره خر نگهداری میکنه و بردتش رو تردمیل تا دلتنگی بیرونو نکنه
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69329" target="_blank">📅 23:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69328">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glezKd75Od7i-IsZoHFNdHELoUtFdRLhUaSkYdbGbjFxSwm_w0oJRB0c3v4ohnBHrjHnRTNO52s0zKv3iz_DUeLQwwKnP40mkgSH4kRsoQBF98g0a5KFNea6B_jDUvCUbWmmG2dpNY-0fiFiY6LqSahiA2XJ2mKrNUhGX1K2eqZMecuJ35ITt4jJmDt8HD487eqrwUSPgx0UxF2Zf0g4IS4UNsvQxym1djy_-2vWNTOYdV4B6ZPAD6WlXpWfmEh78aQ-juo32WD3Te4gYHKyNOW6C3qoUMPCadQ1eIJOZvy5MsJ4-k_25TQ8L9ZIzLZR_zhBQu9DLuOaIf3OKnM2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام برای بار هزارم:
تنگه هرمز بازه و ادعای سپاه مبنی بر بسته بودن تنگه هرمز دروغه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69328" target="_blank">📅 23:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69327">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=jR9rDpStGW1EpnEWHqbV1hfMnUvZoUDOL2OyfwZoU7AaeisTJphUWfz4Y3EMrYKfC5mjZn564RGuQsJWHhTQxkoV6wA5Zh2itL8cNl2Su6KA9flmbK_RjWrqF6kaDE36TXxvvW3Mg4wfycaoA7b704koyABKdqrDCGtyQYQgisNbjHkUP-qBfiBQrNEBvUnzXfl9qb1x8Br76NfPv3MzhowKMVbePtIhjeMYoks8zv4UBHO_3vNSjobswjul4cbW5yBi9lTNL6riuFpkiI4kQf2_MMa091G7r5r_Hu28HavVXufH4WO7OFwAJUGyyLjMZazhUJiLLyu_5RRHOLbb6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdfe35db6c.mp4?token=jR9rDpStGW1EpnEWHqbV1hfMnUvZoUDOL2OyfwZoU7AaeisTJphUWfz4Y3EMrYKfC5mjZn564RGuQsJWHhTQxkoV6wA5Zh2itL8cNl2Su6KA9flmbK_RjWrqF6kaDE36TXxvvW3Mg4wfycaoA7b704koyABKdqrDCGtyQYQgisNbjHkUP-qBfiBQrNEBvUnzXfl9qb1x8Br76NfPv3MzhowKMVbePtIhjeMYoks8zv4UBHO_3vNSjobswjul4cbW5yBi9lTNL6riuFpkiI4kQf2_MMa091G7r5r_Hu28HavVXufH4WO7OFwAJUGyyLjMZazhUJiLLyu_5RRHOLbb6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
«این‌ها خیلی وقت‌ها زیر قولشون می‌زنن.
توافق می‌کنن، بعد می‌گن باید
7 ساعت
درباره برنامه هسته‌ای مذاکره کنیم.
من می‌گم: "آخه چرا 7 ساعت؟ مگه نمی‌شه تو
10 دقیقه
جمعش کرد؟"
شما
5 دقیقه
وقت دارید که تکلیفتون رو روشن کنید.
آخرش هم فقط کله منو کیری می‌کنن!»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69327" target="_blank">📅 22:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69326">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=X7RPGBPfPcNluwlAumfbFFEsjumhQnXtoaUmfbN_nNW-jG1kYTuoZ2zgpye7kCJDBRN5EmUfETMNpClRnrCUWHjCb_8w5gu_ZDEATi32D6FdCk7FjmY1WFFfTp_wKsoXfmiJ2V7gIp0QEvXZooZ6pR0rb5SRnvBCja-N-UgOIkaCSUFe2-HY5QIBaQvFCxz7fl4xotj6cj3HAKzSw9-kyX-STS6dWw4-NyQQS2zYjFNRZDeNjdIRm1cdRwv3-HXKd2hizbmTvCd4TCM2YuRGtzYlYWKxE9jTqKR0h2o4g316c0cpKiVd9-16ZsQK3YZptOSaSx-4-16Q6_QxRsJUdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379fea6ae8.mp4?token=X7RPGBPfPcNluwlAumfbFFEsjumhQnXtoaUmfbN_nNW-jG1kYTuoZ2zgpye7kCJDBRN5EmUfETMNpClRnrCUWHjCb_8w5gu_ZDEATi32D6FdCk7FjmY1WFFfTp_wKsoXfmiJ2V7gIp0QEvXZooZ6pR0rb5SRnvBCja-N-UgOIkaCSUFe2-HY5QIBaQvFCxz7fl4xotj6cj3HAKzSw9-kyX-STS6dWw4-NyQQS2zYjFNRZDeNjdIRm1cdRwv3-HXKd2hizbmTvCd4TCM2YuRGtzYlYWKxE9jTqKR0h2o4g316c0cpKiVd9-16ZsQK3YZptOSaSx-4-16Q6_QxRsJUdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎤
خبرنگار:
سنتکام گفته حملات اخیر برای کم کردن توان ایران در مختل کردن تردد کشتی‌ها در تنگه هرمز بوده. به نظرتون چند حمله دیگه لازمه تا به این هدف برسید؟
🇺🇸
ترامپ:
«هیچ‌وقت نمی‌شه دقیق گفت.
بیشتر کشورها تا الان تسلیم شده بودن.
ایران هنوز تسلیم نشده و بابت همین باید بهشون اعتبار داد.
اونا همیشه به سرسخت بودن معروف بودن؛ واقعاً هم سرسختن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69326" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69325">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=v7l0U3msJAMepSaJAq2V-dRgqS8hzusIiSyIs_fzBrDAEd0bZ40EY60thHovBV3c0328bxrhwS50c861wnB2Ps97UcfA6rOyK7-FiSERCwHOI6zXE3DGDZ4knZOO-HyALizfkJ9iMM1_8oIpFJjXxsGWj08fIwccSXo22ndGsU-a59ksfw29bqC1mmgJsg4ZZRskX9PJHs-1Tl3-85Xslt6h5qi4Etc2ngQLoZHYB5ZejvSAo_j8y0iy1S8bWE5izpLV25c4Am8SFG4mNOyQWCc39otQHC3ge-M26zH5oSET6_9PhcpXJTy5kGHCklkUgfxlKlMwUJ6FJZVEqEQIKWQf2TgEHvSVk-Pzot7gsDJRiJf_mzTnpLdLLL0SP-JAsanIzr3n0mxrDPybNxzbCdfLkZ_bYnqwzrjBMOZZazb4ylg9uDFX5PYexKKuwesYKEENJel9R8wOjqLJVc_hPC75K4PLeYvidXo7abg9xhLCnWJ9s4kMDnYdR6xksGT5D70faSeK3J4DcflMLvBzdPDwzQ6bOXKq3Oou1QNKXazqkpS5HTxSGAisCAH3sP8b1fR8LJMh4D7VsB_vSvO-ZBEnBgQeQ-DjtLBeDBhSX3RPeCrQZhc3H66naW86wCuJ96sKdl2fL5hLUVoSC3mdC0ykHiSohS7Wpo-GTaL-Juw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d8357e0fa.mp4?token=v7l0U3msJAMepSaJAq2V-dRgqS8hzusIiSyIs_fzBrDAEd0bZ40EY60thHovBV3c0328bxrhwS50c861wnB2Ps97UcfA6rOyK7-FiSERCwHOI6zXE3DGDZ4knZOO-HyALizfkJ9iMM1_8oIpFJjXxsGWj08fIwccSXo22ndGsU-a59ksfw29bqC1mmgJsg4ZZRskX9PJHs-1Tl3-85Xslt6h5qi4Etc2ngQLoZHYB5ZejvSAo_j8y0iy1S8bWE5izpLV25c4Am8SFG4mNOyQWCc39otQHC3ge-M26zH5oSET6_9PhcpXJTy5kGHCklkUgfxlKlMwUJ6FJZVEqEQIKWQf2TgEHvSVk-Pzot7gsDJRiJf_mzTnpLdLLL0SP-JAsanIzr3n0mxrDPybNxzbCdfLkZ_bYnqwzrjBMOZZazb4ylg9uDFX5PYexKKuwesYKEENJel9R8wOjqLJVc_hPC75K4PLeYvidXo7abg9xhLCnWJ9s4kMDnYdR6xksGT5D70faSeK3J4DcflMLvBzdPDwzQ6bOXKq3Oou1QNKXazqkpS5HTxSGAisCAH3sP8b1fR8LJMh4D7VsB_vSvO-ZBEnBgQeQ-DjtLBeDBhSX3RPeCrQZhc3H66naW86wCuJ96sKdl2fL5hLUVoSC3mdC0ykHiSohS7Wpo-GTaL-Juw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣️
حسین جنتی، شاعر : سقوطِ زندگیم جایی اتفاق افتاد که سال 89 جلوی علی خامنه‌ای شعر خوندم؛
من سال 89 دعوت شدم به شعرخوانی تو بیت رهبری و شب قبلش بهم گفتن 5 تا از شعراتو باید بدی ما نگاه کنیم، درنهایت یکیشو اجازه میدیم بخونی.
ولی من شعری که اجازه نداشتم رو اونجا خوندم:
گشته‌ام میدان به میدان شهر را، هرگوشه دردی هست
ارتفاع درد از پیچ شمیران میرود بالا
درد من هرچند درد خانه و پوشاک ارزان نیست
با بهای سکه در بازار تهران میرود بالا
گفتم که خواجه در رویای خود از پای‌بست خانه میگوید
ناگهان صدها ترک از نقش ایوان میرود بالا
گفتم جوجه‌های اعتقادم را کجا پنهان کنم
وقتی شک شبیه گربه از دیوار ایمان میرود بالا
فردا صبحش اومدن سراغم و گفتن تو غلط میکنی با ولی‌امر مسلمین شوخی کردی و سقوط آزاد زندگی من همونجا اتفاق افتاد و اصلا هم پشیمون نیستم از کاری که کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69325" target="_blank">📅 22:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69324">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d259260d40.mp4?token=XT7iSMssw5FjtngR05CTTMqqWxBTi5YGsGhH5DX3DDDk9jBnNcaBg4Wh4s4Sm0PiCWHKqLqXaA0cUTzlkkauZQtDEwbB6jInD5pcnqLOYS09dHbWPIU_A-Li7OhNVN3zfITcxTPLYPXa_0fjZZVtMGiHUIuVWCWtKZF63TnxVP6o3a__d1kT6ysbeDjTuxDYzGfE1iWzESTveFAst8rr07rDVusJqv8mZ2Pthfy-paSkHLEgiN3dbxMmCSU6LWX7RKTb5F03dTdCCrJrAXMmr25I9Y_5b0ciEPPCCKN7HcRatkAk2hFIllMTdiPeEDZfn19Gxdz7wcCxcY1nZnBLj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d259260d40.mp4?token=XT7iSMssw5FjtngR05CTTMqqWxBTi5YGsGhH5DX3DDDk9jBnNcaBg4Wh4s4Sm0PiCWHKqLqXaA0cUTzlkkauZQtDEwbB6jInD5pcnqLOYS09dHbWPIU_A-Li7OhNVN3zfITcxTPLYPXa_0fjZZVtMGiHUIuVWCWtKZF63TnxVP6o3a__d1kT6ysbeDjTuxDYzGfE1iWzESTveFAst8rr07rDVusJqv8mZ2Pthfy-paSkHLEgiN3dbxMmCSU6LWX7RKTb5F03dTdCCrJrAXMmr25I9Y_5b0ciEPPCCKN7HcRatkAk2hFIllMTdiPeEDZfn19Gxdz7wcCxcY1nZnBLj4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت های یک عرب درباره ایران:
ایران از جامعه عرب متنفر است، یک تنفر تاریخی.
همانگونه که اسرائیل از جامعه عرب تنفر دارد.
اگر کتاب فردوسی(کتاب شاهنامه و قوم پارس)رو بخونید شک ندارم که ممکنه باعث بشه بالا بیارید.
چرا؟چون عرب را به زشت‌ترین اوصاف وصف میکند.
مثلا فردوسی گفته:عرب در آن مکان خورنده ادرار شتر است،خورنده ملخ اس، ولگرد و کثیف است.
اما فردوسی میگوید اینجا در ایران حتی یک سگ در اصفهان از آب پاک و زلال رودخانه میخورد.
حتی یک سگ در اصفهان شریف تر از عرب در آن مکان است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69324" target="_blank">📅 20:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69323">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=bnrSF3IpVL-_LCTyjN-tyjJxY5MsXowatfzIfOnqu6TeyLBSF-tPffVNch4VgdZlVCXSYSbPblYXagQRLPQH8yBAO-LqaaY7YdwJ8us02KyyZql8ZtsZs4jG9L-ro7DefK2vqQTDB1yyP4StR3We0lUgnwcmnzyNG6rn3fJxVnpO_HxosfYkI1X1Y-hrQEkwu6SQw0BRvVpZ4b3IWCTmxpPX9QJdXG7GtC7i4Dl0VMlXDoB_3Z-wobdXVJow6U-WKvP2i5iopiZcxydLtVjaBZYCVgN5S3nx1aeUaaoUu7lJtqn06QmsQxRrpPOtbWZ5_d1PgG5LHn9lZ-DwMnhnSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea4c431667.mp4?token=bnrSF3IpVL-_LCTyjN-tyjJxY5MsXowatfzIfOnqu6TeyLBSF-tPffVNch4VgdZlVCXSYSbPblYXagQRLPQH8yBAO-LqaaY7YdwJ8us02KyyZql8ZtsZs4jG9L-ro7DefK2vqQTDB1yyP4StR3We0lUgnwcmnzyNG6rn3fJxVnpO_HxosfYkI1X1Y-hrQEkwu6SQw0BRvVpZ4b3IWCTmxpPX9QJdXG7GtC7i4Dl0VMlXDoB_3Z-wobdXVJow6U-WKvP2i5iopiZcxydLtVjaBZYCVgN5S3nx1aeUaaoUu7lJtqn06QmsQxRrpPOtbWZ5_d1PgG5LHn9lZ-DwMnhnSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ  @HutNewsPlus</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69323" target="_blank">📅 19:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69322">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884550e186.mp4?token=I5oFpXLr3nOh8LjtIo-OeZPK4_z9_YGsD7My6dQ3bQcnIHfIIPYFGIareQ4XFci795CFUJkg1pAcejnV7SoKy_8y88X19MamPSp_RgSc9sh-nw6Hcl6og-lMUnmrFnJiX_Ow2kd3vX3ws_UX-FqRiTguZ_mEMEHihYueDjOHtYMDPgXABFUIwvGRChvMX-N4cnrPcKY4GsSikKkr8fTlZ9y5d39-GDwj8OvDJ6Z0mf-THTe21NhuH6l-sqs9QiNtoF_klhwFRsRVhYvDRBfYUZew_zVOHLUxxXEZSs43dWP-qUEl8LpMYCLa07G6c4jAz2tM51SWaTsTcXKLjlSdLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884550e186.mp4?token=I5oFpXLr3nOh8LjtIo-OeZPK4_z9_YGsD7My6dQ3bQcnIHfIIPYFGIareQ4XFci795CFUJkg1pAcejnV7SoKy_8y88X19MamPSp_RgSc9sh-nw6Hcl6og-lMUnmrFnJiX_Ow2kd3vX3ws_UX-FqRiTguZ_mEMEHihYueDjOHtYMDPgXABFUIwvGRChvMX-N4cnrPcKY4GsSikKkr8fTlZ9y5d39-GDwj8OvDJ6Z0mf-THTe21NhuH6l-sqs9QiNtoF_klhwFRsRVhYvDRBfYUZew_zVOHLUxxXEZSs43dWP-qUEl8LpMYCLa07G6c4jAz2tM51SWaTsTcXKLjlSdLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🤡
یه بخشی از صحبت های خیلی مهم ترامپ: بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ بینگ
@HutNewsPlus</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69322" target="_blank">📅 19:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69321">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=h2Gaw8pqB_-l-VZGA48C2knnyX8POiqPj138F2FPoHo4DNFASgelKce1NEkAnkhX-DmaY0G7WR5GE55ARJY8UhqQmCis7-fpzYGmBMDOMdDMMw6UZYIuX7BS9stCQOSMZseS56ypQDGx3Ldzso9K_5WXcMz0ZyMCk7-51JN7X032xwTh718SAOxBWDgAxK1_57LrQtCKSaKQOpSn8b0Bxe1w_WOtd01GF5WLrsi_yDzi_Xll9vIOpWnn5X8OIebQaOPkilSp1JTZRIo_PVUOJSfNGf9ynavNokJAdrbKvRojB7EjfOJIGDr02oBhVEUBhV5GcjoFGksdum_u3yLR6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caed943dd3.mp4?token=h2Gaw8pqB_-l-VZGA48C2knnyX8POiqPj138F2FPoHo4DNFASgelKce1NEkAnkhX-DmaY0G7WR5GE55ARJY8UhqQmCis7-fpzYGmBMDOMdDMMw6UZYIuX7BS9stCQOSMZseS56ypQDGx3Ldzso9K_5WXcMz0ZyMCk7-51JN7X032xwTh718SAOxBWDgAxK1_57LrQtCKSaKQOpSn8b0Bxe1w_WOtd01GF5WLrsi_yDzi_Xll9vIOpWnn5X8OIebQaOPkilSp1JTZRIo_PVUOJSfNGf9ynavNokJAdrbKvRojB7EjfOJIGDr02oBhVEUBhV5GcjoFGksdum_u3yLR6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خبرنگار:
در مورد ایران، گزارشی وجود دارد که نشان می‌دهد شما پیشنهادی از سوی ارتش برای گسترش چشمگیر فعالیت‌ها دریافت کرده‌اید.
ترامپ:
ما از قبل گسترش داشته‌ایم. منظور از "گسترش چشمگیر فعالیت‌ها" چیست؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69321" target="_blank">📅 19:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69320">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">املاکی تو یه جمله همزمان گفت هم می‌خوایم خیلی شدید به اونا ضربه بزنیم و هم می‌خوایم خیلی مهربون باشیم باهاشون
🤡
#hjAly‌</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69320" target="_blank">📅 19:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69319">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=nLomODfjJFk0Rh9cItxQRBL0q-7cZePvQ-HNytoyewjH1qjCMYzbtrqCDX8sihdz6gTog_PB9_J9JTAEMuWSiDWaUBfJA5PkB_kD-nQthjkIHOuZXf13PCBbcWvBWLuFCXg2R8lkNpqiqgRDQf47qCfc-GtjrPX_AQl8yqEAiW6rVKdrX3AjSvtFruk_QkpxDThPk2ZFzI5FOOO2EDkH3H4hDn8VfxW0njMf_FIAjxFi7mp45txd2XA-OHUdtMyywVOH-LNADRcS-ChKLkFx8eIHqaeOquocn7VjTH0yT--zAK-rwp-ESgy-HcyQZEuCN10sAxL13KZfwJi16QXPFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0411d5fa4.mp4?token=nLomODfjJFk0Rh9cItxQRBL0q-7cZePvQ-HNytoyewjH1qjCMYzbtrqCDX8sihdz6gTog_PB9_J9JTAEMuWSiDWaUBfJA5PkB_kD-nQthjkIHOuZXf13PCBbcWvBWLuFCXg2R8lkNpqiqgRDQf47qCfc-GtjrPX_AQl8yqEAiW6rVKdrX3AjSvtFruk_QkpxDThPk2ZFzI5FOOO2EDkH3H4hDn8VfxW0njMf_FIAjxFi7mp45txd2XA-OHUdtMyywVOH-LNADRcS-ChKLkFx8eIHqaeOquocn7VjTH0yT--zAK-rwp-ESgy-HcyQZEuCN10sAxL13KZfwJi16QXPFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران وضعیت خیلی بدی داره؛ واقعاً خیلی بد. اوضاعشون خیلی خراب شده و تحت فشار شدیدی هستن.
تعامل باهاشون هم خیلی سخت بوده؛ هم صادق نبودن، هم قابل اعتماد رفتار نکردن.
ولی این چیزی رو عوض نمی‌کنه؛ چون در هر صورت، حال و روزشون خیلی بده.
ما فقط پنج ماهه اونجا هستیم. اگه به جنگ ویتنام نگاه کنید، می‌بینید آمریکا بیست سال اونجا بود. کاری که الان علیه ایران انجام می‌دیم، از نظر من یک عملیات نظامیه، نه جنگ.
ایران هنوز چند تا موشک داره، اما خیلی کمتر از چهار پنج ماه پیش.
توان تولید موشک‌شون تقریباً از بین رفته و ظرفیت پهپادیشون هم تقریباً نابود شده.
البته هنوز مقداری از این توانایی‌ها رو دارن.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69319" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69318">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=VO6thw0Bj6mShb7i-7FxiejDmelcAfsIeeKp1t5AufLUYs6Z1Wh7gYOquFxp1AmPuwHqYU0mZKsUlo_Fp9qKuTkk4SCqE9munI6rWgEI_xZ6Pfwd4afQpPMpeg--e1vIfjY3j_UKMqjLNJzuSkjJsfhTc1CKc8323S29KI6EvekNFD3YUwk2itCI28vvDEVdCPNb-R11Q2EKhgdHUD-62lyaX6xfOFpdaWheOr3rZjTC_XC8w8NTFo_VA_D1b7Iq7eDMBTe9Kog-olG3WEdRR9Ye7boQJLTy5tweX7NOtjb-fCqZb9uhzZSZoN73KiJJpGF9kfPycpQyzKfsBLDnFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0ec710b6.mp4?token=VO6thw0Bj6mShb7i-7FxiejDmelcAfsIeeKp1t5AufLUYs6Z1Wh7gYOquFxp1AmPuwHqYU0mZKsUlo_Fp9qKuTkk4SCqE9munI6rWgEI_xZ6Pfwd4afQpPMpeg--e1vIfjY3j_UKMqjLNJzuSkjJsfhTc1CKc8323S29KI6EvekNFD3YUwk2itCI28vvDEVdCPNb-R11Q2EKhgdHUD-62lyaX6xfOFpdaWheOr3rZjTC_XC8w8NTFo_VA_D1b7Iq7eDMBTe9Kog-olG3WEdRR9Ye7boQJLTy5tweX7NOtjb-fCqZb9uhzZSZoN73KiJJpGF9kfPycpQyzKfsBLDnFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پیت هگست:
اگر برایتان سؤال است که چرا حوثی‌ها، با وجود اینکه یکی از نیروهای نیابتی ایران هستند، وارد این درگیری نشده‌اند، دلیلش این است که به مدت ۴۵ روز، قدرت نظامی آمریکا را از نزدیک تجربه کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69318" target="_blank">📅 19:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69314">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=cjFtalDi_Fu44FFjJBLHCsD3APeR2C2KsQGi4qPKx8U1HlkbFfY6vpKFSO72HC3PYxe5xR81VeACwRKuZvttZHYPApq6HqiGpP-z0aQvj-0tSEoMmJ0Gp_3OwjMSIbDkSkokQl_Wom8HcfECAWAm8f9YYu8t2FNfA7BDAOkWzRKo_U0U8wPkqqYp9ubAim9qzxw7i62PwY0axpNX2M5r5p7GabASEmylyq4n_BJlJZ2af6iprNhWFhEIjvwmDnvIS-Hg3F-ydEhVp5gixgmM_rifJ6RsJ2QI2H-9_mMp_DuUzJYLrkO9Pru7XK9jOfI6wbp1zNozUxJtOHXN7SYBTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a849aad2.mp4?token=cjFtalDi_Fu44FFjJBLHCsD3APeR2C2KsQGi4qPKx8U1HlkbFfY6vpKFSO72HC3PYxe5xR81VeACwRKuZvttZHYPApq6HqiGpP-z0aQvj-0tSEoMmJ0Gp_3OwjMSIbDkSkokQl_Wom8HcfECAWAm8f9YYu8t2FNfA7BDAOkWzRKo_U0U8wPkqqYp9ubAim9qzxw7i62PwY0axpNX2M5r5p7GabASEmylyq4n_BJlJZ2af6iprNhWFhEIjvwmDnvIS-Hg3F-ydEhVp5gixgmM_rifJ6RsJ2QI2H-9_mMp_DuUzJYLrkO9Pru7XK9jOfI6wbp1zNozUxJtOHXN7SYBTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
آخرین آپدیت از وضعیت اسپانیا:
- مهاجرین غیرقانونی همین‌جوری تو سطح شهر پخش شدن.
- چندین مورد دزدی از فروشگاه‌ها گزارش شده.
- کنترل اوضاع از دست پلیس اسپانیا خارج شده.
- مردمِ محلی گروه تشکیل دادن و دارن هرجا مهاجر می‌بینن، کتک‌شون میزنن!
- تو بارسلون هم مردم دارن خونه‌هاشون رو از ترس مهاجرین، سیم خاردار می‌کشن...
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69314" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69313">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: به زودی، دیگر چیزی از ظرفیت نظامی ایران باقی نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69313" target="_blank">📅 19:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69312">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇺🇸
ترامپ: ایران در تعامل با ما صادق نبوده است
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69312" target="_blank">📅 19:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69311">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=hoE5iLgL2CiDo2VfbCVgShdtKyodVgcTbkgvCL3gKPdNF8i_9ZsAhOKbtmHUkpSR3M9JBAwvwx-Waqz5mhzSjwqzl0Xo7mXRayOCKpXGTIC99sveDOFxV4QN6xmNDKAXLyGIC7w4ExZCwXorZnaJxMrQKhl-qrKNQ8qllIsOB-vQfAkpcbVgeVwTYV4Qp1-jTclGWtWzEnxAwE6K96i0pvQ-nM69edmECJeiiMmUgAbNDn74ogpnIYlE3BZHt9FGFmW8b0j-Wym87gvq6yvm4NJbTukFGitL4Vyeilg61BieSS-tugFI2jQL5teF4yR2r_uTSnO7uX5szRik6Ytgug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e0b272c3.mp4?token=hoE5iLgL2CiDo2VfbCVgShdtKyodVgcTbkgvCL3gKPdNF8i_9ZsAhOKbtmHUkpSR3M9JBAwvwx-Waqz5mhzSjwqzl0Xo7mXRayOCKpXGTIC99sveDOFxV4QN6xmNDKAXLyGIC7w4ExZCwXorZnaJxMrQKhl-qrKNQ8qllIsOB-vQfAkpcbVgeVwTYV4Qp1-jTclGWtWzEnxAwE6K96i0pvQ-nM69edmECJeiiMmUgAbNDn74ogpnIYlE3BZHt9FGFmW8b0j-Wym87gvq6yvm4NJbTukFGitL4Vyeilg61BieSS-tugFI2jQL5teF4yR2r_uTSnO7uX5szRik6Ytgug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
ترامپ با بالگرد «مارین وان» (Marine One) وارد «کمپ دیوید» شد تا سیزدهمین جلسه کابینه دولت دوم خود را در آنجا برگزار کند.
فاصله کمپ دیوید تا کاخ سفید با بالگرد تنها ۳۰ دقیقه است و رؤسای جمهور آمریکا از زمان فرانکلین روزولت (FDR) در سال ۱۹۴۲ از این مکان استفاده کرده‌اند.
نام این مکان برگرفته از نام نوه‌ی آیزنهاور، یعنی «دیوید» است که توسط خود او انتخاب شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69311" target="_blank">📅 19:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69310">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1sn0zxbY77cvSZ-m5HhSmBaH6EhUqzwhGggBrcbqN9C4gjj4OJC2TWl04JoL-ZzEZq9FRp8CUyoaez79Eg3gArEtoQqZbB0YPPQL3RZl2-Rg0-r740sNs7awupoUmFA1P0195eDnxG8F7nIT_qeAlGnAa66qLWRWRdZDCdW_KtVRyPMSHwqjQ54NqPIRnx0ws3hSIxICqJWXM0fIMOdfV11P71z0X5zBVDrlkxJNRscovLjhiFy0QGppr9dq2n9cS_zIoRNwb5WLpEqsfR9AMpOdJOGk52SLh2BZTJwDOqDPkGk-gddEjbNF1H8yOOKYCrvKR5NbcKRFEx-olu1tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نهاد مدیریت آبراهه خلیج فارس:
به علت تداوم اقدامات تجاوزکارانه نیروهای نظامی ایالات متحده در منطقه، تردد از تنگه هرمز امکان‌پذیر نمی‌باشد. به محض برقراری ثبات و آرامش، کلیه درخواستها بر اساس ترتیب و زمان‌بندی بررسی و مجوزها به مرور صادر خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69310" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69309">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
حملات پهبادی به جزیره بوبیان کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69309" target="_blank">📅 18:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69308">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31550cb053.mp4?token=HMweSE9PdxadX2dMFmNN5w0GbtIlHb6doa9xOOMfL2vYM0ivAZtJm0f6YU1GTgkT143zUhcbB9PUvPMOuIn7rXbn-k3E4pZk2EgpF3sV0nCK0ek7ZtntsP3zRA4kOi3tnVGN65yHOqyVYpDT-2mjD2Dr5N3uEoYeO3npBOuErAIDiCNMDryRNYUC2tkTutCEpxXDL6B9ChEbHM5MT-JFPp8UnYLFBpiXqxt33IQFjsB6j-Q3CHCci61V7aR4Uo0lLCFb1Colm6wK32RSqXGKpWEc62Scf7F-XjNrGDccYmHP6NMPcUN7sP_bUfE2Uj346S5E8sOQOBwmZjX_6CnlJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31550cb053.mp4?token=HMweSE9PdxadX2dMFmNN5w0GbtIlHb6doa9xOOMfL2vYM0ivAZtJm0f6YU1GTgkT143zUhcbB9PUvPMOuIn7rXbn-k3E4pZk2EgpF3sV0nCK0ek7ZtntsP3zRA4kOi3tnVGN65yHOqyVYpDT-2mjD2Dr5N3uEoYeO3npBOuErAIDiCNMDryRNYUC2tkTutCEpxXDL6B9ChEbHM5MT-JFPp8UnYLFBpiXqxt33IQFjsB6j-Q3CHCci61V7aR4Uo0lLCFb1Colm6wK32RSqXGKpWEc62Scf7F-XjNrGDccYmHP6NMPcUN7sP_bUfE2Uj346S5E8sOQOBwmZjX_6CnlJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
رئیس‌جمهور ترامپ در گفتگو با فاکس‌نیوز:
«اوضاع خوب پیش می‌رود. تنها کاری که می‌توان کرد این است که به پیروزی ادامه دهیم؛
آن‌گاه سرانجام اتفاقی خواهد افتاد.
ما ضربات سختی به آن‌ها وارد می‌کنیم و آن‌ها را کاملاً گیج و سردرگم کرده‌ایم، و همچنان به پیروزی ادامه می‌دهیم.
سرانجام آن‌ها چاره‌ای جز بازگشت به خانه نخواهند داشت.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69308" target="_blank">📅 18:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69307">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJNZTC1fuELGybUJ0tTl1GzE_ClMaaJEQbwmsicFu2DlzIw0HZK4RJ9sHytAUC2vnWrzn1tDFjmAMUoJtwXmPrL7lj7QCLOLW0X05Hs4-HjZW_bKe12MLN56ZsCVTICkPEB9KWTXI6vxEbU5FI-_ERzFK_MoVRgT9L1mtreLBaFCwmvH1hotjZ68Y2CB9KKXvnDZ1wAdR1E-6nGHhfztJwesvSfyzofRvGsruxVhdKMkwZN3wFGsHPo1PjZDti-OUCVnLByeMSYCSwj7fdfnVVFwTEfulTNT0x1MF26MCM1H49Vzg-JwtjBkP_C7sv6y9e9vtcQm3UwYpIrVtdamPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
❌
🇮🇷
وزارت دفاع کویت:
نیروهای مسلح پهپادهای خصمانه‌ای که اوایل امروز وارد آسمان کویت شدند را رهگیری و نابود کردند.
حملات ایرانی همچنین چندین سایت نظامی و زیرساخت‌های حیاتی را هدف قرار دادند که باعث آسیب مادی ناشی از سقوط آوار شد، اما هیچ تلفاتی گزارش نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69307" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69306">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4497b03176.mp4?token=WtiXmMabcD1sPRbh6rnuikovW_L_lnM5Ueu1fkK5DHo0aNjzxg5XYJsARHuXrVSKmQ13k4w_hOr8rvZ_SZCkRryudUia11f6One7BMmJemnHqKZZEGsYvYEGNSeXZMCV3iA1qFEyDLswxr-HlDRF7JVJ7id3Gfzamb_PgF1g4u79hdfBWFc_6Ow3g6Ky5Y-OTBPrdtPL6cAmDz-Voy_ETc6EsnUti4AIx6LcL-m1GBQjycRZxV5slop7Rvp18seMAKrQygDegWSzZFZESj9_OjGB1kRRq7uASpqqs3S7iEG-9GVWH_YKDdqSWdTLkL6zI5bieIBJm89GlgQ5QTTeQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4497b03176.mp4?token=WtiXmMabcD1sPRbh6rnuikovW_L_lnM5Ueu1fkK5DHo0aNjzxg5XYJsARHuXrVSKmQ13k4w_hOr8rvZ_SZCkRryudUia11f6One7BMmJemnHqKZZEGsYvYEGNSeXZMCV3iA1qFEyDLswxr-HlDRF7JVJ7id3Gfzamb_PgF1g4u79hdfBWFc_6Ow3g6Ky5Y-OTBPrdtPL6cAmDz-Voy_ETc6EsnUti4AIx6LcL-m1GBQjycRZxV5slop7Rvp18seMAKrQygDegWSzZFZESj9_OjGB1kRRq7uASpqqs3S7iEG-9GVWH_YKDdqSWdTLkL6zI5bieIBJm89GlgQ5QTTeQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کابینه ترامپ برای بررسی اقدام بعدی خود در قبال ایران به کمپ دیوید می‌رود.
این خبر ساعاتی پس از آن منتشر شد که ترامپ از توافقی «تاریخی» با میانجیگری مصر، قطر و ترکیه خبر داد که بر اساس آن حماس با خلع سلاح کامل موافقت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69306" target="_blank">📅 17:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69304">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=QzInei5xcVFAhw9KzHu3v81yONHZITNR9-RESOCbWF1v8-zC5olK5gLGEJtfnEdS8Pk52hLYZUrpWOpyU4MT1n6fiVxoTs9l2AoGX6DXw74lAGrHCJgWBS_77XvjgWRUM8vzjgAwKrTLjwPvdZibFOeteO6B9YaretUtZNoq7XNLZvh3oAdtOKVvSFRxGWMflLejlgMtJVWdCax9ywq2M-bsN-Weahjk6BifXiFLLWYDI297vDdb0jy9QqoeN10N29mu2gzaGFwmmxyNbhctEBlNtBlPuoU12NX9H6sODmDT8vJ6g-sl2iOBpuGdog6ZVVRJlHc2vjAOu1_mIjMs4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006b9f5bfa.mp4?token=QzInei5xcVFAhw9KzHu3v81yONHZITNR9-RESOCbWF1v8-zC5olK5gLGEJtfnEdS8Pk52hLYZUrpWOpyU4MT1n6fiVxoTs9l2AoGX6DXw74lAGrHCJgWBS_77XvjgWRUM8vzjgAwKrTLjwPvdZibFOeteO6B9YaretUtZNoq7XNLZvh3oAdtOKVvSFRxGWMflLejlgMtJVWdCax9ywq2M-bsN-Weahjk6BifXiFLLWYDI297vDdb0jy9QqoeN10N29mu2gzaGFwmmxyNbhctEBlNtBlPuoU12NX9H6sODmDT8vJ6g-sl2iOBpuGdog6ZVVRJlHc2vjAOu1_mIjMs4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهر سئوتا، منطقه تحت کنترل اسپانیا در شمال آفریقا، با یه بحران جدی امنیتی و انسانی روبه‌رو شده.
فقط توی یک هفته گذشته، حدود
1500 مهاجر
با شنا خودشون رو از مراکش به سئوتا رسوندن.
رئیس دولت محلی سئوتا گفته مراکز پذیرش دیگه ظرفیت ندارن، صدها نفر مجبور شدن توی فضای باز بخوابن و مراکز نگهداری از
کودکان و نوجوانان بدون همراه
با
2400 درصد ظرفیت
در حال فعالیت هستن.
الان به‌طور میانگین
روزانه 300 نفر
وارد سئوتا می‌شن و مقام‌های اسپانیایی نگرانن که دوباره بحران سال
2021
تکرار بشه؛ زمانی که حدود
10 هزار مهاجر
فقط در چند روز وارد این منطقه شده بودن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69304" target="_blank">📅 16:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69303">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCAIVdceZWfzhxbbxSvkQB-03K8jkT7YIYnUqvgLXem5CqTpBv8me5Su0-bC2Vosd1bQn2PSKSYqgSTme0uqhhju8ZfC0WV-PyvjiVX9RPqTlJKobPS-h_sEwFzB1Wgay93PyVArB2EzkM_JdWetb2aRrk4ivwFuqlS93SRl3DI80dhnqtpJW3qYQeM8DcNb7GeGJZEqI2GzeTdozXmNXb6twWAq-MxJx8ZnE5dV8KR_egApLsaGpvhJg1rL_mzpFjL3-bKXl_niB5GMXFKgSNj36m8JTXCRTOGSz1AYI4FJAujVMyhDCoXP-ag2ieRjUU8SNsUP89aaRTTtkLj4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پسر رئیس بانک سپه که دهه هشتادیه معاون بانک دی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69303" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69302">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Omf2bwV4UO_2pWzLlaD5mXKHtN2iI5VwCnb6pOlu0c4cFbHVF9NERwAOfK5gVNd0TD6QvDSv9bqEjHl_5Dm4rOCZUFPnuU3ZtqFc3VSztyTrnnXQpR0Hbwxu-Q5-QGS3-Rn18a_yy3JHx8yG9Y77oruqZG7W6jmsIp--Q0hMJgtM8ZdZDfLpXVFOlJiF10lO0ny1jBgWk0OIMSSz1P4SVLnOPBzx3MhY6rdKQhaDEM-qyXUDHLMGslxJDB505mJGZAktfpgOBGlY3NjXwVr9qMYhMekTGCeDB8ly66vWox_j9-hktCs8DECexFxVvnF4W4G_Tpm59mTUC2TI6i7KzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
طبق داده های نت بلاکس دولت ترکیه اینترنت کل مردم رو قطع کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69302" target="_blank">📅 15:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69301">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d06ZiagUmw6tXFhToLIQIzgdT56c1bGLZSYt8rJ6qAG05IkhC4Lr8GE_pymHkbByzmORgHRx34bdjcsSoiQ2QHxnBog9vSwhKVeB_JjSvsYx8NM62aKIsRRoKXacswFUmX3xmZP1jN-Fqb5JZlWmEZvpW4iI3xd0i-ZeSysAayzZ_l_WqHeVrR1rTaoGRH38oZ-uZtVKd_ncpifNEGbvA27u8u-jzNNBZMtwR8zRVb7HY_l048a8Jl1ARVOpR82n6rIHfW91GbWRN3Acci1m2ceSGBsdGHsVRtztp6fWMsptJ2fdUsPf3A9OE0kBrGh0YwMvXrNP3M0Il2JEvKTrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
عربستان داره خودشو برای یه عملیات نظامی گسترده دریایی و احتمالا زمینی، علیه حوثی‌های یمن آماده میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69301" target="_blank">📅 15:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69300">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🇺🇸
رویترز:
پرزیدنت ترامپ امروز در کمپ دیوید با مقامات ارشد دولت، تیم امنیت ملی و فرماندهان نظامی دیدار خواهد کرد تا درباره مسائل مختلف و از جمله جنگ ایران گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69300" target="_blank">📅 15:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69299">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=K__0LrkSgs4J9XACFTrVH4vfVuryZAP_8i2L11coWBQoLn9_dZXIBaFm3B2Kv7qHc6vY6Q3ykeASz4OU5GBvJ83b7SFnZy_8KxXLBLjRW5lVAT0uWS1yKoWgSCykZghHuvpbtaQcNLJLVMZm6QJef5bVIiNZQAgP3BMpNijvKolJkEJo-qJcqSh-M_Zi814D-1gSkXpOwuy1NzzY7aGmYDCrC4J3hS9jCODHXURyIZdAwHH8S3X1sLS8_OMpPuIQWq7rP0U8ax2_EhjCXAY_s1FUHN3g956KEt6gLX9ulrlxCiVL2h7JYBX1WZIQG21NFuLZ5LDJ_pQ9DXewAiAEvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb0ff0fef7.mp4?token=K__0LrkSgs4J9XACFTrVH4vfVuryZAP_8i2L11coWBQoLn9_dZXIBaFm3B2Kv7qHc6vY6Q3ykeASz4OU5GBvJ83b7SFnZy_8KxXLBLjRW5lVAT0uWS1yKoWgSCykZghHuvpbtaQcNLJLVMZm6QJef5bVIiNZQAgP3BMpNijvKolJkEJo-qJcqSh-M_Zi814D-1gSkXpOwuy1NzzY7aGmYDCrC4J3hS9jCODHXURyIZdAwHH8S3X1sLS8_OMpPuIQWq7rP0U8ax2_EhjCXAY_s1FUHN3g956KEt6gLX9ulrlxCiVL2h7JYBX1WZIQG21NFuLZ5LDJ_pQ9DXewAiAEvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
🇮🇱
تلگراف:آمریکا و اسرائیل در حال بررسی طرح محاصره زمینی ایران هستند!
به گزارش روزنامه «تلگراف»، آمریکا و اسرائیل در حال بررسی احتمال اعمال محاصره زمینی علیه ایران هستند تا فشار اقتصادی بر این حکومت را تشدید کنند.
دونالد ترامپ و بنیامین نتانیاهو در جریان گفتگوهای خود در دفتر بیضی‌شکل کاخ سفید، درباره «ابزارهای نظامی (کینتیک) و غیرنظامی (غیرکینتیک)» بحث و تبادل نظر کردند؛
از جمله اعمال فشار بر همسایگانی نظیر عراق و پاکستان برای تشدید کنترل یا بستن گذرگاه‌های مرزی.
یک مقام ارشد اسرائیلی به تلگراف گفت: «اگر مسیرهای زمینی را مسدود کنیم چه می‌شود؟ فرض کنید ایران دیگر نتواند هیچ کالایی وارد یا صادر کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69299" target="_blank">📅 14:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69298">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🇮🇱
وزیر دفاع اسرائیل ، یسرائیل کاتز:
اگر ترامپ از ما بخواهد، به حمله به ايران ملحق خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69298" target="_blank">📅 14:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69297">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=gBqf6VYu9V8cKlOj7URWj5dbBulW1p3_LAW1U0EHJl-4eyGHPSNGeHfxOml5VAXGE2M6MRWMZz_uU9Xx2wKS_qS6fR3h5Nws574QJgKOYWhLjKbaSJVHjw3dNRxEbqS5nP9K5qGUGoT6uJGYlF2_iwXZPPuqEcnSHOA1nFDdbKgDl4Ku_roS2rJxWLe0M8URNKsikIN_3kGcX5byauhvwM0xHET3Mej1Byx5XbmPf3SfoYNI-fZ4LI3gBYOzln5o58ErFco3aiGprw6CFuU1gQEs8iv9YCNN-8SfozjewzYCAaeQIuw8mah5w49keMuJYV4jYelLvuKkXas1SEIw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cbdd236b.mp4?token=gBqf6VYu9V8cKlOj7URWj5dbBulW1p3_LAW1U0EHJl-4eyGHPSNGeHfxOml5VAXGE2M6MRWMZz_uU9Xx2wKS_qS6fR3h5Nws574QJgKOYWhLjKbaSJVHjw3dNRxEbqS5nP9K5qGUGoT6uJGYlF2_iwXZPPuqEcnSHOA1nFDdbKgDl4Ku_roS2rJxWLe0M8URNKsikIN_3kGcX5byauhvwM0xHET3Mej1Byx5XbmPf3SfoYNI-fZ4LI3gBYOzln5o58ErFco3aiGprw6CFuU1gQEs8iv9YCNN-8SfozjewzYCAaeQIuw8mah5w49keMuJYV4jYelLvuKkXas1SEIw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو عراق اهو گرفتن بکشن بدن به زائرا
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69297" target="_blank">📅 13:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69296">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=pEBkFyQrR3ZM0asWsbwFo3u4q8fkMNhs7J8rWoEUrBZblERf3VZ4ZlTL270zBQaAmXcSF-tN3esZwZjUrS6ku6ptShWPdGYH2LlMqHKtqXDdlUnOy4Hn-5K9a4fZDz7WJUiLhIfQ9u9JzgsrdCWz8ahqnw34XImkCNXxaEvO3o8Hjoht8UgI-wtzc-DmuHvVdmDCH3E5BVvxvKqf9UC-MjZf9uD1tlL9O7TvnbAgggZmnDdydQjjK5dsD7BfIOOjvXJ7Re3OChwMLLqgkSR807WdHSizHyAXLZQRxZtg92QxdTp9FEd0vmXdLK9s99oUB0586QwlNOKJCSN_fdX4zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37edae9b59.mp4?token=pEBkFyQrR3ZM0asWsbwFo3u4q8fkMNhs7J8rWoEUrBZblERf3VZ4ZlTL270zBQaAmXcSF-tN3esZwZjUrS6ku6ptShWPdGYH2LlMqHKtqXDdlUnOy4Hn-5K9a4fZDz7WJUiLhIfQ9u9JzgsrdCWz8ahqnw34XImkCNXxaEvO3o8Hjoht8UgI-wtzc-DmuHvVdmDCH3E5BVvxvKqf9UC-MjZf9uD1tlL9O7TvnbAgggZmnDdydQjjK5dsD7BfIOOjvXJ7Re3OChwMLLqgkSR807WdHSizHyAXLZQRxZtg92QxdTp9FEd0vmXdLK9s99oUB0586QwlNOKJCSN_fdX4zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران:
ساعات ابتدایی امروز  ۲ نفتکش متخلف به خیال اینکه میتوانند از مسیر غیراعلامی ما، تحت اسکورت هوایی ارتش کودک‌کش امریکا عبور کنند، بدون توجه به اخطارهای ما، در مسیر ناامن و غیرقانونی حرکت کردند که مورد اصابت قرار گرفته و متوقف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69296" target="_blank">📅 13:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69294">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DwrxbGIu4ih1qMjMq-I-cqvSO13gaNgGeRxC2NJMsi3HpZEDwoI_Z5Ys6DdPHO6yXf9dvqUjlL3NM2ZHvLiT-x9qNfio7_2FEt0gr__zwPj-tvYChKobqWs8LNqXo1xncprmyoaaFD-3TzhrG6yFFjOZWTcUZYzJ5wtpccJ1sivJTlQf92LcaztbrkCuWnArQ2xILJLl6-huH2_UWx091Hkl50Kzh8iD5dJoOIMVc9hSggm4auagFNYasGv4L3JL1h5kFIXYhLVH1-6CKGfnA0LehHBEuHcd3DAey6QWa16Ymd4rS_p59A3wqXlSNB8a6eDixHTP4KqG4j1AaBhhmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=ZeGvkbO9og6nJBp0AKfOH6VnhHQIclG4sKKi_prscMfmgv8zD1YHIvwLNLy1Rqkfz31S02LQbiXNxKlMah29TtVWot_cUyA7rlzGnuGk-B2-3Uo0kB2vss5pSkuWSaOxtgrgaxvLoyEA2CPwF8px6v4hpDJIPoLwEzqqYEeNnZAy3R0UCsPtjgNzSZm0Xk2tRiQbbAFAiGcnfr09Uj9bWfZGCTTAdvvS_yBzjOe__5Po5S23lm-picl8_9m96vyeMBQBZRPdpc288Z7sz7wqf-Ja8VOQK-sP8SspMQnwx4lNzPp5WZ19XnddX-F2Nx48Ortm6_0w5zcfyP4X3rZQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=ZeGvkbO9og6nJBp0AKfOH6VnhHQIclG4sKKi_prscMfmgv8zD1YHIvwLNLy1Rqkfz31S02LQbiXNxKlMah29TtVWot_cUyA7rlzGnuGk-B2-3Uo0kB2vss5pSkuWSaOxtgrgaxvLoyEA2CPwF8px6v4hpDJIPoLwEzqqYEeNnZAy3R0UCsPtjgNzSZm0Xk2tRiQbbAFAiGcnfr09Uj9bWfZGCTTAdvvS_yBzjOe__5Po5S23lm-picl8_9m96vyeMBQBZRPdpc288Z7sz7wqf-Ja8VOQK-sP8SspMQnwx4lNzPp5WZ19XnddX-F2Nx48Ortm6_0w5zcfyP4X3rZQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای توی کربلا در حال پخش شربت دیده شده
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69294" target="_blank">📅 12:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69293">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCjwn7A9P4czwEwocdvOiDy7R6WqYIU4RLuBnyVlWUv50JLhaHaiXJKXL8pk16CC9Qr81v40w0q1i3X3k23CQ3LxuRMBho4LcTrLgmu0iJzawWwzgLDmWNSl-jC_iH2DlT6ZiMuiByEGdjqtFVZRVQhRF1nGtlJEcg4kOskawibH4G6yqIoMATzaCy0JsYen4uAAI-WnxPzdkDDM-M3aNR2YT16X5CrPpCnzuKCN2IXYif-L9Qf26mzxGhotha8oPIT9hMJt_yEVQCRbQtIuvBV6KmwFtPnMZIN9So7BX3KfGXyvTScxMtNgIV1QymmadHoSdlb063gI8jZC7Xgb-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
گاردین:
یک موشک بالستیک روسی کارخانه تولید پهپاد در کی‌یف را که متعلق به شرکت «ترمینال اتونومی» (Terminal Autonomy) —شرکتی ثبت‌شده در ایالات متحده— بود، منهدم کرد؛ این نخستین حمله شناخته‌شده روسیه به شرکتی با مالکیت آمریکایی در اوکراین محسوب می‌شود.
این کارخانه پهپادهای تهاجمی مجهز به هوش مصنوعی تولید می‌کرد و گزارشی مبنی بر تلفات جانی در این حادثه منتشر نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69293" target="_blank">📅 12:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69292">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YpmrMk4Im9VPy8rpA3eXdwLq_hwdUJJ11yBlM7OITA1hkeLbL3OuGjYhEkRLncMdbXrzaIlYiHQeKgFKN3ELLLvBy63kxXWW0ZXdsgPTbZ6eIN8CZ4rjMQF62owP95RM8iHOrV_AH5avn27X9dq0Hay246-vmFrrIxyTkrla0L8417Pv2dAcf16PXphVR-vIvckmt1_8U1zoq-2mbQM0Ym_Y6KcDtgCB7ZBGSiPlkDO4o_mRGZCGrypuQ82Cl12iKg8oorysQQKiXdGuQcjutIvOZTvqk1YKfU5511H5ARAO6iKcB-SCCMI54brWue1bJ-5BNkvxN_ukOxXsKzOPIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم خاکسپاری علی خامنه‌ای، رهبر عالی پیشین، به ایران سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکنند و وقت بخرند.
یک مقام ارشد آمریکایی مدعی شد که ایران تلاش کرد حماس را متقاعد کند تا این توافق را امضا نکند، اما این گروه تصمیم گرفت به این توصیه عمل نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69292" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69291">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=KDkQzCjXPgK8afdHLZw1xfRJT5aDNG8pbg3tjgAzCUMlq625q687giMPUgMUO8ShoKdC6UiDnhvDZ26vLgbVvrzwDgXHiQV2f48jLxlB8q_lNRZEJKa3K4Apr9JQYN6LM_b4utSDBuydd272dGcEbLp81ps7YBKcmfQrDSDFl1LOFCDW-EkHs3FVODSJGxnYPcH0XwRPOMS74NH5a88N8pnZUqDuICypZ90CfpPi3ZFXNnV4wh8PQ2CFJZUrUDdT_XQ16qh4SwdCxEvZy2lnOf3zDN5SgPoAEG36S_rjPfjUoykHFiKeSDe08BB1TXaacaCtYr6f-EJve2yz8cy4yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a885a777d.mp4?token=KDkQzCjXPgK8afdHLZw1xfRJT5aDNG8pbg3tjgAzCUMlq625q687giMPUgMUO8ShoKdC6UiDnhvDZ26vLgbVvrzwDgXHiQV2f48jLxlB8q_lNRZEJKa3K4Apr9JQYN6LM_b4utSDBuydd272dGcEbLp81ps7YBKcmfQrDSDFl1LOFCDW-EkHs3FVODSJGxnYPcH0XwRPOMS74NH5a88N8pnZUqDuICypZ90CfpPi3ZFXNnV4wh8PQ2CFJZUrUDdT_XQ16qh4SwdCxEvZy2lnOf3zDN5SgPoAEG36S_rjPfjUoykHFiKeSDe08BB1TXaacaCtYr6f-EJve2yz8cy4yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدئو وایرال شده از یکی از مراسمات عجیب آفریقایی ها که با شمشیر همدیگه رو میزنن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69291" target="_blank">📅 11:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69290">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMnaDXWFpRaxOqNJACtWeefLAAIFm-bL_Ar8prG0nd_8rMRKFrHnFciv-aAU4L7F9PMEli1oxnIdDRm_r_BsGiX2zBPsIfg-cbtXIJw_Ig27gqSRZbsW9v9gxLO-14WecVIbTwvh3k0AdiObavm2Z5wvD7jlsEGXDI-zHHLSsbFZzFELpp-TohvEO_fy9ea2LXfjpUImlZOI1Wwrw6yIGsIpCvH63DH0jCumLTbzFlyBmYlUXIcRS7LBj38vNYZx0MOqRSsw__FZOuiOrmDQ2Kyw8ta19WXPb4dspPzVBl57-q31qwEfJwCEyu6pE9aBbSEbXR_ezHOvhObJ0zcSvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
تایمز:سازمان سیا و موساد اسرائیل در حال تشدید جستجوی خود برای یافتن آیت‌الله مجتبی خامنه‌ای، رهبر جدید ایران، هستند که از زمان جانشینی پدرش پس از حمله هوایی فوریه ۲۰۲۶، در ملاء عام دیده نشده است.
مقامات اطلاعاتی معتقدند که او در این حمله به شدت مجروح شده است، بیش از ۱۵۰ روز از استفاده از تلفن یا لپ‌تاپ خودداری کرده و در یک پناهگاه زیرزمینی به شدت محافظت‌شده، احتمالاً در تهران یا نزدیک قم، پنهان شده است.
با توجه به اینکه نظارت الکترونیکی سرنخ‌های کمی به دست می‌دهد، جستجو از اطلاعات سایبری به اطلاعات انسانی تغییر یافته است.
مقامات سابق موساد می‌گویند که اعتقاد بر این است که مجتبی از طریق چندین لایه پیک ناخواسته که پیام‌های دست‌نویس حمل می‌کنند، ارتباط برقرار می‌کند و نفوذ به حلقه داخلی او تنها راه واقع‌بینانه برای تأیید موقعیت مکانی او - یا حتی اینکه آیا هنوز زنده است یا خیر - است.
برخی از چهره‌های اطلاعاتی گمان می‌کنند که سپاه پاسداران ممکن است مرگ او را پنهان کند، در حالی که برخی دیگر هشدار می‌دهند که رژیم ممکن است از بدل‌ها برای پنهان کردن حرکات او استفاده کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69290" target="_blank">📅 10:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69289">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=OVvumU4z3fJRQ6f3ydWMs2_yYfeJL1QcJ03xzsqZ8MQ516JHiHr0kA4mCKPK0-gU9E5173mruFZX0q_RPjcu2Xi_CAW3ym3W1SzCyo8fS3LLcA1Kq85dlNHG09NtGkvLnqg0y_DDwOgYxC2hDfVRLhMURPUboltg0PGdZUTrlniQ9GYre0kNkPwO8RHzy38AIzrWsRWpY5mj1XOtyrtv-BxngULSo2hmYVRciLLl5KBWKzbVhmKjRG5Q9br5ocrWZN-vqRQedC44fJKDUkCOy3bh3J2PfDUqox1QkW4yaW2Z9xGfJyxyWQPrwq-WHKhTKt-qDZH5U8SKBZjm3sMSBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9be197f29.mp4?token=OVvumU4z3fJRQ6f3ydWMs2_yYfeJL1QcJ03xzsqZ8MQ516JHiHr0kA4mCKPK0-gU9E5173mruFZX0q_RPjcu2Xi_CAW3ym3W1SzCyo8fS3LLcA1Kq85dlNHG09NtGkvLnqg0y_DDwOgYxC2hDfVRLhMURPUboltg0PGdZUTrlniQ9GYre0kNkPwO8RHzy38AIzrWsRWpY5mj1XOtyrtv-BxngULSo2hmYVRciLLl5KBWKzbVhmKjRG5Q9br5ocrWZN-vqRQedC44fJKDUkCOy3bh3J2PfDUqox1QkW4yaW2Z9xGfJyxyWQPrwq-WHKhTKt-qDZH5U8SKBZjm3sMSBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از حمله عجیب طرفداران حکومت به بنر ترامپ و نتانیاهو
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69289" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69288">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
دلایل سقوط شوروی که صداوسیما پخش کرد در مقایسه با وضعیت الان ایران!
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69288" target="_blank">📅 09:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69287">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=bz_-gQyfihR9nsIhlMiX_FUYDeuhbV0hC4err7iyEwUNqnIMzQaOJq7EwuGZBanZJxRq0PzPIHT05lLEqsLnppB5PnMO6S5_JqZjiB0TKmW_2yd4nsLKjAwJYpDI5JyDgfUVK6o4StHtb0x6mOKyLr9Ah49E8YBOVuCfevlDlL45IyNibE1UgrNxt8M0JtXS_dfKuanYxv0BX32TOAh7RIl-5ants7jS61lKcgg_8pw_KYkoryeWnn_fT7qgZNaM3rQ8Pub6YI4-PQb8Vj86L_CxDrQkSKP9oi_VP6BjNMv1UQO2d-SHmevgQZp5oQCoWSlMW1o-UhqvZzb3ohGY-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/418bb6362d.mp4?token=bz_-gQyfihR9nsIhlMiX_FUYDeuhbV0hC4err7iyEwUNqnIMzQaOJq7EwuGZBanZJxRq0PzPIHT05lLEqsLnppB5PnMO6S5_JqZjiB0TKmW_2yd4nsLKjAwJYpDI5JyDgfUVK6o4StHtb0x6mOKyLr9Ah49E8YBOVuCfevlDlL45IyNibE1UgrNxt8M0JtXS_dfKuanYxv0BX32TOAh7RIl-5ants7jS61lKcgg_8pw_KYkoryeWnn_fT7qgZNaM3rQ8Pub6YI4-PQb8Vj86L_CxDrQkSKP9oi_VP6BjNMv1UQO2d-SHmevgQZp5oQCoWSlMW1o-UhqvZzb3ohGY-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار :
کشور های منطقه که مورد حمله ایران گرفتن آیا باهاتون تماس گرفتن و ارتباط گرفتن ؟؟
🇮🇱
نتانیاهو:
بیشتر از چیزی که فکر میکنی و بیشتر از چیزی که میتونم بگم اتفاق افتاده
.
⏺
خبرنگار:
هدفتون درباره حکومت چیه
.
🇮🇱
نتانیاهو:
خب هدف مشترک من و پرزیدنت ترامپ مشخصه اگه بتونیم تهدید ایران به طور جدی کاهش دهیم توافق های صلح زیادی انجام میشه
!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/69287" target="_blank">📅 02:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69286">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/reEXSJ4nJRSUMyrunpV9Y-oPhy61eTx4ojHCDheBpGJWP5kub3-Y_WrXMBgLDRT9eHt1ktXgYPPQpW8HnkBUFS2wjYXfPBczvbThgiRIkC_XUvsghSaD9TdjUhGyV6Dhtbkks1aE-Wp0RFKfKUVHC-c5aX55Hi4GQm5A3bFs5V57eOjL9areIw-Wrrq0wjvFL7XCFn97doXYKdsMmJURy6DosWVnSYIyF5t6HwFbxB10Ijsd_x9-71gbzH6Bo3w56RL88DjRZMz6NQZVDZDj8L2VbeOIKS9bTV3TSY7lXkeiJt-zRBnedg3TEiqszrV3fmxmra4hI-Akmmil_S-AdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
امروز، «شورای صلح» به توافقی تاریخی برای خلع سلاح کامل حماس و تمامی دیگر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
این توافق گامی حیاتی است تا غزه سرانجام تحت اداره یک دولت جدید فلسطینی قرار گیرد؛ دولتی که برای یاری رساندن به مردم فلسطین، همکاری نزدیکی با «شورای صلح» خواهد داشت. هم‌زمان، اسرائیل از امنیتی که شایسته آن است برخوردار خواهد شد و غزه دیگر به پایگاهی برای حملات تروریستی بدل نخواهد گشت.
این رویداد، نقطه عطفی بزرگ در اجرای «طرح ۲۰ ماده‌ای ترامپ» محسوب می‌شود. این توافق طی مراحلی با برنامه‌ریزی دقیق اجرا خواهد شد. هم‌زمان با تکمیل روند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و «نیروی بین‌المللی ثبات‌بخش» با همکاری نیروی پلیس جدید فلسطین، مسئولیت تأمین امنیت غزه را برای ساکنان آن و همسایگانش بر عهده خواهد گرفت.
یک سال پیش، شاهد جنگی شدید و خونین، بحرانی انسانی و نگهداری گروگان‌ها در شرایط اسارتی بی‌رحمانه بودیم. ما به پیشرفت‌های تاریخی دست یافته‌ایم، هرچند هنوز کارهای بسیاری در پیش است.
می‌خواهم از میانجی‌ها — مصر، قطر و ترکیه — به خاطر تلاش‌های مهمشان و به‌ویژه از تیم فوق‌العاده‌ام که با تلاش‌های خستگی‌ناپذیر خود دستیابی به این موفقیت تاریخی را ممکن ساختند، تشکر کنم.
اجازه داده نخواهد شد تهدیدی که در ۷ اکتبر از سوی غزه سر برآورد، دوباره بازسازی شود!
بر اساس این توافق، غزه سرانجام در اختیار دولت جدید فلسطینی قرار خواهد گرفت که در خدمت مردم خود است.
این دستاورد شگفت‌انگیز را — که همگان دستیابی به آن را غیرممکن می‌دانستند — به همه تبریک می‌گویم!
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69286" target="_blank">📅 02:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69284">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTMlbYsZezCUGRjWOrpwH27ggUzMVeeIJA1rHVwH6gCmff7ASRpcxs8FpjrXPOSjouH2IzAgj2aiwTee0fno5NceIhLs7Ryb_fels8gC2lDpQl57L_7RJzT2LO0c7kqwM1luMCA-s9B3aYJ5QRNi9oAhH_HUu-gR0Hlmcu25hftpeexWF92RIS8MkMlrz62qdvi1UWXSAe_bXk0nQyd2f8rG96zLpBJgQ9lns0YLbRFXoKu1p_WAhjp1A2maU_Lm8pPCZPVKfm62WWzOcMaJV_ortKWEPfolhH5R97hbd9-6CsTcuS3Xjr0X0RO3t2Z1owm36RKR52OFkEgPO7uR-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=TCkoYWHMsXr_eK4JJyxJcAJOKeMpUjnEYuT_woakIrCOR5uFWDDgCbGqACN0mMuFxD8u7v94p6hr3r2JjricZ4cIja7Z-5zt400Rbap4Sa030osDm09f89yfcGUIsQVeDREi633HVPu4_mQLx3fqr_-JaBkc_C4kS-FcegyDQiORyl_rfpQuOZtmvb6b9NfIeIdiUcUDvW-5nu1nshFbNu4DLWxaPzo3H7a0cl2dORBh9gDrJp89AMZq44VRAKar-lvjOukArl7TbSROjH_j8A6uXXAkNEkt2Z3OvlQdFXT0z4_1C5dvfO5LKq0y7tQbyNt5NrTKW_sS1xmMy7N5oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9bb4c4a.mp4?token=TCkoYWHMsXr_eK4JJyxJcAJOKeMpUjnEYuT_woakIrCOR5uFWDDgCbGqACN0mMuFxD8u7v94p6hr3r2JjricZ4cIja7Z-5zt400Rbap4Sa030osDm09f89yfcGUIsQVeDREi633HVPu4_mQLx3fqr_-JaBkc_C4kS-FcegyDQiORyl_rfpQuOZtmvb6b9NfIeIdiUcUDvW-5nu1nshFbNu4DLWxaPzo3H7a0cl2dORBh9gDrJp89AMZq44VRAKar-lvjOukArl7TbSROjH_j8A6uXXAkNEkt2Z3OvlQdFXT0z4_1C5dvfO5LKq0y7tQbyNt5NrTKW_sS1xmMy7N5oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیدار عجیب نتانیاهو با یک سناتور!
امروز نتانیاهو با جان فترمن دیدار کرد و طرف با شرتک نشیته بود و سرش کلا تو گوشی بود
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69284" target="_blank">📅 01:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69283">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69283" target="_blank">📅 01:48 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69282">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromلیوه</strong></div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69282" target="_blank">📅 01:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69281">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">عجب سکوتیه، موشکی راکتی چیزی نداریم؟
🙁
#hjAly‌</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69281" target="_blank">📅 01:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69280">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">▶️
تیزر جدیدی از سینمایی Spider-Man: Brand New Day منتشر شده که دیدنش خالی از لطف نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/69280" target="_blank">📅 01:18 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69279">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZJ-158y5nFqe8d4txqT2Gwsewb9iSXKZ5_u93tFQspNDxv5gVMI3huSeSaxoD9S8vrkIpuGrCw2s-J4DSRGPKEenoqD3aRC1h4DUU6pXU5ZrqgpBPS_DlUvluuqnSSCAb-LLmIFUfIShohKLgOEYDZAg7fwEDmBwyOnXakt2RwykNtjrc3fqJI6xUj-6Giu5avrSMM0chu_vJc7wTCr7AsEbP3qdu5x1j2hjws7N1Bppv7v7V6Dnr3ABbT2aCHG4bhnaR9_peJq2k6DzATuIG7e8Ah0vSUINMEAfGj4je1zdb-nLnMFaie3hf2TAsjSTr-xt-3cPTgAtaxdY1x_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
«آمریکا هر روز یه جنایت جدید انجام میده. حمله به خونه‌های مردم عادی توی جزیره قشم، ادامه همون جنایت‌هاییه که قبلاً توی لبنان و غزه انجام داده.
آمریکایی‌ها عادت دارن هر وقت توی میدان نبرد کم میارن، با ریختن خون آدم‌های بی‌گناه جبرانش کنن.
ولی بابت این کارشون، تاوان پس میدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69279" target="_blank">📅 00:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69278">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba260d124.mp4?token=N89AKn9CguAINEEfM6bA7NiG0KrixKG7D7KHVJhSkkB98SQZlitUzi5XU0ckKH1rUxld0uiNLfGpbm-7Gd8YW5egqQPI9c4_2V8PwiNGP2lvITVy_LjBaZdkmmjtLst-53UHPQh_6H8081AET2HBLT2WUSnvYFupV6lpIs3hb4D_0hcPbPWgklArf6H0gEnZcYlspFosIMmx9eFR6J7P1dWI9eA73dOBS2c3Bgdl6ynWS1VSp4muvd5kZFXv7oxnOJe7ruMtfw_ULOBxE9Px_Ol1kpBe3YIfUXafSpRPHagZsZiwHzUI8RRMdK-UhAyn8yU6S4-eRCVmlyTvvbN1lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba260d124.mp4?token=N89AKn9CguAINEEfM6bA7NiG0KrixKG7D7KHVJhSkkB98SQZlitUzi5XU0ckKH1rUxld0uiNLfGpbm-7Gd8YW5egqQPI9c4_2V8PwiNGP2lvITVy_LjBaZdkmmjtLst-53UHPQh_6H8081AET2HBLT2WUSnvYFupV6lpIs3hb4D_0hcPbPWgklArf6H0gEnZcYlspFosIMmx9eFR6J7P1dWI9eA73dOBS2c3Bgdl6ynWS1VSp4muvd5kZFXv7oxnOJe7ruMtfw_ULOBxE9Px_Ol1kpBe3YIfUXafSpRPHagZsZiwHzUI8RRMdK-UhAyn8yU6S4-eRCVmlyTvvbN1lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام:
یک فروند هواپیمای P-8 Poseidon(هواپیمای شناسایی تخصصی) نیروی دریایی ایالات متحده در حین گشت‌زنی در خاورمیانه، برای سوخت‌گیری به یک فروند هواپیمای KC-135 Stratotanker نیروی هوایی ایالات متحده نزدیک می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69278" target="_blank">📅 00:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69277">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ot5wVOECgvT1brWkTv1wAapC1oAyRVRAbT31kOCq6H9N8kw4aZ0g8YVWbcY9Rax0Rk00WlioTsn7JIizzkQthUXPd8SdIGZOWvpMkBUlhRuzm4Yn-JtCczHNIhQVk50rpuuSYcDne25eAMe9A5lKrgdPKI_brazhcjpInpowaf_xBAHEk-FSWNOwJ6lTxTTzh4M1rlNiJVfD_DZuMMTdwBPC4KxyHk1O-M-krX8BtWk67s6kvrWSIUD6fFNs55w3P--eTnyoeiDhU_eK66ocmcPSQn-e59h-bldsL1bRYp--JvcYR6uQJ6Ysrj3R4ZJ0nQHMRndA_j8PE2N3bZhIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آی‌24نیوز:
اسرائیل کاتس، وزیر دفاع اسرائیل، روز پنج‌شنبه به همراه ایال زامیر، رئیس ستاد کل ارتش، جلسه‌ای برای ارزیابی وضعیت امنیتی برگزار کرد.
در این جلسه، تصویری از وضعیت اطلاعاتی و عملیاتی، سطح آمادگی ارتش و طرح‌های عملیاتی برای سناریوهای گوناگون در عرصه‌های مختلف به کاتس ارائه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69277" target="_blank">📅 23:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69276">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89da715482.mp4?token=puU0KiEmE_ypSYuNjaXoK5Dqrta3cwpLmO0U3SUP8z2mGF3EvfJeBG8Lk1FJL-eQ3f3lgAbPVmoLa-bux4xwDmnhjO0vzb4UGNHYSsBiIRcPGXIlLVA7tDQ9prPEzdWJByF1LQ89Zezjrm97fT0u7feAch9G7aB9Jwfe7ZeUc7Otw7KtNvjeO7IZyedLD39JmNjHgKNiHW1Ghm74anALf4TYykBj0W_I7KxU_UpiNqAWh3hYUCBEjg198FcooMyvE4dAFeNtNcg84KPKRlHPq3CYCzcakDxav1jYk9wtpaJFe7BPsBxPeNayMr1GNSxNd4TvN1rdY3LVt6W4iLvRGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89da715482.mp4?token=puU0KiEmE_ypSYuNjaXoK5Dqrta3cwpLmO0U3SUP8z2mGF3EvfJeBG8Lk1FJL-eQ3f3lgAbPVmoLa-bux4xwDmnhjO0vzb4UGNHYSsBiIRcPGXIlLVA7tDQ9prPEzdWJByF1LQ89Zezjrm97fT0u7feAch9G7aB9Jwfe7ZeUc7Otw7KtNvjeO7IZyedLD39JmNjHgKNiHW1Ghm74anALf4TYykBj0W_I7KxU_UpiNqAWh3hYUCBEjg198FcooMyvE4dAFeNtNcg84KPKRlHPq3CYCzcakDxav1jYk9wtpaJFe7BPsBxPeNayMr1GNSxNd4TvN1rdY3LVt6W4iLvRGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند روز پیش یه پسر بچه به اسم امیرحسین رو آورده بودن صداوسیما که اینجوری جواب سوال مجریا رو داد
:
مجری:
منو عروسیت دعوت میکنی؟
امیرحسین:
معلومه که نه
مجری:
کارشناس برنامه، خانم دکتر رو چی؟
امیرحسین:
فرقی نداره، اونم نه.
مجری:
مامانت چی؟ اونو که دیگه دعوت میکنی؟
امیرحسین:
وقتی زن بگیرم مامانمو میخوام چیکار
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69276" target="_blank">📅 23:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69275">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=rX0tnLA5QG9IdB9teTW_6xA7oCj-hEQ71Fd-msG0gsiEi0mlmij8jndqkhK1U8u8S4s4DumPqv7enwvdThy-bGylOfbCPLs5mV9lmHRPloFOPk69BwOSI59xxxs9o-tt7eXnBAb6g1u8xDS2I5BdHw1TFScO-u_--_zPIexSx_U9y3EJrpRvUPWtbAcIef7NsdDWTsRLa4WYwNwNtl0kjG0unUiIaRb756-mvMjci0fxpqYQFH0JG-98wjADPkQSGHi28_BEo6JU2a1dUal1kfNGTtB19I_xpTFzspIcP-9xsGejoS03Y75fIs5ICLSG06XWWnheF9R01El4dtWlow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/671ccf87ea.mp4?token=rX0tnLA5QG9IdB9teTW_6xA7oCj-hEQ71Fd-msG0gsiEi0mlmij8jndqkhK1U8u8S4s4DumPqv7enwvdThy-bGylOfbCPLs5mV9lmHRPloFOPk69BwOSI59xxxs9o-tt7eXnBAb6g1u8xDS2I5BdHw1TFScO-u_--_zPIexSx_U9y3EJrpRvUPWtbAcIef7NsdDWTsRLa4WYwNwNtl0kjG0unUiIaRb756-mvMjci0fxpqYQFH0JG-98wjADPkQSGHi28_BEo6JU2a1dUal1kfNGTtB19I_xpTFzspIcP-9xsGejoS03Y75fIs5ICLSG06XWWnheF9R01El4dtWlow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نقدعلی، نماینده مجلس:
با وضعیت حجاب میخوایم چیکار کنیم؟ والله جوابی برای خدا نداریم.
یه نماینده مجلس به من گفت از درد بی‌حجابی هر شب تو خونه گریه میکنه و خواب و خوراک نداره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69275" target="_blank">📅 23:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69274">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Royttiglf4CMwg9_SH1PyLWvKuU51mvfWjqnlIc7AFeKH5Nas3zJUnv4deTwsxDLrLJLVvIigouOn6toOJ-shjxp0LFh_wqdZDrlAjSja8jTnqvwYPK4mRsrMhECyfCKWvPN6KNCMm5UHnXFU2aDqZ9e-uIZVAnS45yICQfv9NsElkMOTFBjQeIRuDhRX40dnVZetfcEQJz5JqsVdHPatYsIBjftD-5dgpyTIBr0oRi7E11lHrQJSIzFsk6K62RkX_qYTnfLf18R4A1gH8MOHcG8-1xvRiJMXZm24j2rPfnigwXrhBQnTWz8aT1R6h7QDGyHS5VqwsLea7oNZ3S56g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعدام می‌کنید؟ به‌به چه کتلت های تر و تازه‌ای داریم امشب  #hjAly</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69274" target="_blank">📅 23:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69273">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhiHV9Fia5w9bFNx98SrTduAmD_cF1JyNcaGigLqiRK3oB1b3wsc0xB-S71HZZMiN_gKxSuOe4QpE8VwSWJ6Q0P4neSbMgzhC-6j0XIxBcvaB9PYkHkza5B8YCYCNdKhSYghv6om8-nIWW6iGCFTKgJ4w80IPe8DHNff5rw-w8uDcEz2N0TZzUAJk2YchaoeFihq5QEw1etC0NXvY8Fcf7EviomJpGH-hPkF65Bk1fXFiEtuZ4_rF11vpVT2TGov214iPc2uBJ2bcX4XXOk1W-CIQkkPrIozvZsPd2sRjhXa2U--6l7ptPkGZkLb2_iqhwYXWDPOCZfaLar8MuDrVCvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3fe31b5c.mp4?token=ESpWshazxF0XtRX3D4ET_Y-o6KnPRpcblGphqvzGUvhVN2e0a3hyw6txk6Yc4H-NoCM4R2K599BaWxao6rhwASaBN3xq9h_IgwQXVbUguG0DFSFUuHJreeBCQOFMy3arFEkSqqelQrVrVDpPq4hpchb8gYCqfjyhnb5rZqmq6nbv2H9RACbkxnRoAz59YMLc_HO1v4IwFyKM8Y_KKPenrgcfcMlcb0txcnM-5HZpoGu4BYUtF1RPbhq2R69azTShVEb3hKiIBx5uvP_AsvRXFUIB6Ozc6k5ouXNwSeYGSY8XZ-5WG36NSjYBSl8Fwp-wslz5waa4yEoY9BRSSR7ZhiHV9Fia5w9bFNx98SrTduAmD_cF1JyNcaGigLqiRK3oB1b3wsc0xB-S71HZZMiN_gKxSuOe4QpE8VwSWJ6Q0P4neSbMgzhC-6j0XIxBcvaB9PYkHkza5B8YCYCNdKhSYghv6om8-nIWW6iGCFTKgJ4w80IPe8DHNff5rw-w8uDcEz2N0TZzUAJk2YchaoeFihq5QEw1etC0NXvY8Fcf7EviomJpGH-hPkF65Bk1fXFiEtuZ4_rF11vpVT2TGov214iPc2uBJ2bcX4XXOk1W-CIQkkPrIozvZsPd2sRjhXa2U--6l7ptPkGZkLb2_iqhwYXWDPOCZfaLar8MuDrVCvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کویتی‌پور، معروف‌ترین مداح دوران جنگ ایران و عراق، دیگه حتی مداحی گوش نمیده
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/69273" target="_blank">📅 22:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69272">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2D2uCWtd2YTbBpehWOroCOdzNevjv1krixSNpVx5FspkscrltBYXUrsGL0WokFX45-yHv2-yCFeRiMg_8Ruq_r4-Rwsn_4WTN8b6gBcEZ74jzF8J6b8QGKdmnlG8FEahU4k-4_16sf-GFX-WBUWIvmGtaUYlQI-hFVG4fp4LIIOh0hy9Yzs13RKjtzV51cDPyUHFxdrtXAM4_CVrgFQ76BT65Q1m_FpTDhChtzi5eKoWUvghbl6yYI2-kI8q6bvp96fB9gBjuoBlKxzWgI1my7jMjZ0WzTIoik1IBi3AhR8LskmBkdMjyMOqmCEFMVqqF951pGFoihlE9EAmjGr-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :  روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است. طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.  ظاهراً مقام‌های روسیه هنوز…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69272" target="_blank">📅 21:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69271">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Nxb6QBSs1B8vFc5NuXrKwPvye5__r_8H875ZtOP4cGy0gmB2OfVdq3ixELGdU3LRPrPi12SW2gQmGAJjHYPaX8T_5n-WEi8T481Zw7dmbm7cLBrcurdMIW_uWvCi1y99umlkccZIpxjkBcMHdndvTXuW3O0I9jvyhapcZE7NxXFhjmlH8ZwWfEUl0pW2XsdeOwy9QQ7ABZgrGTv-2TpfLpWg3mlrStZICVYpEHZsEjqvPVZQclqohjVq-eL7k0NoWABl25AKRYsmrW1MPfMU8aBU0sa2yb12hMi9aFItSq1TBze6QMFyRXbLxOLh7XDFcIee8bGm3kt-w4xigRyjrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😄
مالک تلگرام ، پاول دورف :
روسیه به‌دلیل اینکه حاضر نشدم خواسته‌هایش برای نظارت گسترده و سانسور در تلگرام را بپذیرم، مرا در فهرست «تروریست‌ها» قرار داده است.
طبق قوانین روسیه، من از «انتشار هرگونه اطلاعات در اینترنت» منع شده‌ام.
ظاهراً مقام‌های روسیه هنوز نمی‌دانند که چه کسی می‌تواند چه کسی را از اینترنت محروم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69271" target="_blank">📅 21:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69270">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=JkjP0s_R6I3il9m2tMF5yC2HO-Tg47dQwZZuHyAqqqyxxQh0-GdjpZ00Z0pTdhu-Miz42iaPhjzV7F1cxxTydiToXfWdVyxHbpxdWZRfbxA00dp7YXUCgrxmj_Bv2Hw126BWJ8ChMjPMthlLWgvYwpGrNM70y1jIuOt_XyQgz6D7pmbkb1Qisrwj_inERvWxug7gx89Lf1WVVTMrmSrH4K-xK1GC6FEO0CiZs-QzO0kK43YO0xb0s3vKlxcvV3oc44sKT-KA-NKOblsqe_ZIWSOD76p1Rsn09eqWnCtotfl9oe6PW0Es8AkEUmD2HusMzdM9JiCM6df0vEa8JYDoWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7ad22e432.mp4?token=JkjP0s_R6I3il9m2tMF5yC2HO-Tg47dQwZZuHyAqqqyxxQh0-GdjpZ00Z0pTdhu-Miz42iaPhjzV7F1cxxTydiToXfWdVyxHbpxdWZRfbxA00dp7YXUCgrxmj_Bv2Hw126BWJ8ChMjPMthlLWgvYwpGrNM70y1jIuOt_XyQgz6D7pmbkb1Qisrwj_inERvWxug7gx89Lf1WVVTMrmSrH4K-xK1GC6FEO0CiZs-QzO0kK43YO0xb0s3vKlxcvV3oc44sKT-KA-NKOblsqe_ZIWSOD76p1Rsn09eqWnCtotfl9oe6PW0Es8AkEUmD2HusMzdM9JiCM6df0vEa8JYDoWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔝
سنای آمریکا به طرح قطعنامه‌ای برای توقف عملیات نظامی علیه ایران، مگر با کسب مجوز از کنگره، رأی منفی داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69270" target="_blank">📅 21:12 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69269">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=RWxZHof5r8sKQEqVm3S4Y2IWi8I7jwJ2_yKyDZV_zk5FAt5uv9bxJsfCS13doZGreXg3hTNvom60RpRnocSABnS_5p-_daAEB3x-10DRjF9uq_ViE-2jNflsT_KG6kLNP8bKhCbSusbGk1Znk4z0WOemz90-acsg_rJQJPsVVE2gj5rb-f0zn6NBOQhH1EQOR9Vt9QiFY_WdCFH8mSOE1-HCeBec7WQP6saL7YdJCbxBkJ1d_-Kc2Svgi38divdGymnSKoLxH5cI-aoFRkYIKH6JOj4IacLpbFUghk4UHr5dhjMe6pC9r2kGfi2eFAU25mSlSFYvewq2k0H2Euv5Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64cd6ef9d4.mp4?token=RWxZHof5r8sKQEqVm3S4Y2IWi8I7jwJ2_yKyDZV_zk5FAt5uv9bxJsfCS13doZGreXg3hTNvom60RpRnocSABnS_5p-_daAEB3x-10DRjF9uq_ViE-2jNflsT_KG6kLNP8bKhCbSusbGk1Znk4z0WOemz90-acsg_rJQJPsVVE2gj5rb-f0zn6NBOQhH1EQOR9Vt9QiFY_WdCFH8mSOE1-HCeBec7WQP6saL7YdJCbxBkJ1d_-Kc2Svgi38divdGymnSKoLxH5cI-aoFRkYIKH6JOj4IacLpbFUghk4UHr5dhjMe6pC9r2kGfi2eFAU25mSlSFYvewq2k0H2Euv5Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📚
عمران عباسی، عضو کمیسیون آموزش مجلس
:
قطعا تو مهرماه باز شدن مدارس رو نخواهیم داشت.
چون برگزاری آزمون‌ها تقریبا یک ماه تاخیر داشته.
حالا همه تلاش‌مون رو می‌کنیم که اول آبان یا تو خودِ آبان ماه مدارس رو باز کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69269" target="_blank">📅 20:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69268">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=XqlK07s0eJ75sUYAZm4t0I0QN-k5QKVr9r9hM5b9aqse4fW3KbPtFR8eLyuae5hLBQjDQX7mRXi4lUbBTne6nLWnP41xWy4bmkSL95-lNDI47_gF1-u7wqxXaq125WPaalRFR6a8sjFkr9VSdvPW8xXJUF_dA-Ty-lkyGdmRIrSm9lJ6Bp1Ltfck7zjJwDzuXYOCblpEvT2N1_V_zJh2YY4jo1qjeBVWuSdtCArxzGvpb7yJLMLAeAl580tlmDCT3QE6XPhIHmNxXaB5ObPABVbpiQzbRtjhPq6Gm33-COMeebm_TWxKRd_F6ujm64jmaGHLfxGrADtYtbXCZwoSPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dca29ad7e.mp4?token=XqlK07s0eJ75sUYAZm4t0I0QN-k5QKVr9r9hM5b9aqse4fW3KbPtFR8eLyuae5hLBQjDQX7mRXi4lUbBTne6nLWnP41xWy4bmkSL95-lNDI47_gF1-u7wqxXaq125WPaalRFR6a8sjFkr9VSdvPW8xXJUF_dA-Ty-lkyGdmRIrSm9lJ6Bp1Ltfck7zjJwDzuXYOCblpEvT2N1_V_zJh2YY4jo1qjeBVWuSdtCArxzGvpb7yJLMLAeAl580tlmDCT3QE6XPhIHmNxXaB5ObPABVbpiQzbRtjhPq6Gm33-COMeebm_TWxKRd_F6ujm64jmaGHLfxGrADtYtbXCZwoSPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
حکومت از امروز یه طرحی رو شروع کرده که بتونه فضای مجازی رو به صورت کامل به دست بگیره؛
طبق این طرح؛ قراره بلاگرها، اینفلوئنسرها و بقیه فعالای فضای مجازی ثبت و ساماندهی بشن.
در عوض می‌تونن از مزایایی مثل بیمه استفاده کنن، اما از اون طرف هم قراره نظارت روی محتوایی که منتشر می‌کنن بیشتر بشه و هر کسی خارج از چارچوب قوانین جمهوری اسلامی فعالیت کنه، صفحش بسته و با برخورد قانونی روبه‌رو میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69268" target="_blank">📅 20:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69267">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oahOD--4EW4Cjq4jgKNLaExZ5NZ8cSbYeKuBoQ3Hj3qEOIx-dMNAeWqr4tCJq0Sk_qHCihwZ8bIDEYfeI28axksHkN9Qp8ymxPPah7-aNW3DHWLQzIo0-UkOKMcMtfsmodyXAjq1y4UxL7JSnHzKE1ni4S0htGUSPkduXvo7xi5doibNqpbo3m5x_ovoEoyGfLDk3r_TNIhSZsmjR8LpU8tLY37cO26uncmI5MJrJOHUkJO7eh4Rcg9tH1sb_bmiV8ap7JAAWb8WTe-_taYUNDF60mJj6zeSnECUhOUnjquRoqcObCt7iFb6fgzdX7kup_2PjFd0dy634-9edQDwaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46911d7dc4.mp4?token=oahOD--4EW4Cjq4jgKNLaExZ5NZ8cSbYeKuBoQ3Hj3qEOIx-dMNAeWqr4tCJq0Sk_qHCihwZ8bIDEYfeI28axksHkN9Qp8ymxPPah7-aNW3DHWLQzIo0-UkOKMcMtfsmodyXAjq1y4UxL7JSnHzKE1ni4S0htGUSPkduXvo7xi5doibNqpbo3m5x_ovoEoyGfLDk3r_TNIhSZsmjR8LpU8tLY37cO26uncmI5MJrJOHUkJO7eh4Rcg9tH1sb_bmiV8ap7JAAWb8WTe-_taYUNDF60mJj6zeSnECUhOUnjquRoqcObCt7iFb6fgzdX7kup_2PjFd0dy634-9edQDwaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آفرود سواری هم تو ایران ممنوع شد؛سازمان منابع طبیعی:
از این به بعد هر کسی بدون مجوز یا خارج از مسیرهای مشخص وارد مناطق طبیعی بشه، باهاش برخورد می‌کنیم. اگه هم آفرود به‌عنوان یه ورزش به رسمیت شناخته بشه، براش دستورالعمل و چارچوب مشخص تعیین می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69267" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69266">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8AqcI7PV9iNe4QbrmcHAMIvFlDzWyrSt15Z4ZAU7Sj6Q-vdqo8VjOBNmwjveVeJwoYdhig1cQf3_hKeEKbYrSuW8aaadE8E2cUyCiAxuQiFCTWtM0KG6Osin90tX8QsTW_wzrZRbxdsqC_nvYjoKL9rwbRib5IHiAbv4xuw6_OhGPALa2l80VUvAmkCtLNParLczrt-4KqCBP6cK_ul5sYOFiK7L1IaEn0H_NRrfBEj4gB6w5I5RvIOhrPhaTjf7LD5HArAedvd-1cKCngdhO1M2BhT4U6_jqgwIJ3z8Zcxo-6KkMeDmz54_EFNkfniw7nK6sBzMkF06HC5rvfRZs-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbbb58fbc.mp4?token=asUybxu1EgJrfN25tDdO_JMxCe7_TSsBpMGtHw8GsOmoeTcUmJx7L0P2VkWbOR0R-6NRdMvaie-Id8Aw4r2CRp4Ty7ImVL5F0kYb-oaeOTvAs5oaAkxycZYCApCZByT2BaUvapiVyCoKlWGSQ5ZTbc3GHdmOYyrD9smW7WT87JmWfbRYh-8Dq74RNnBfbNj8CH80T1uWgeNRuCpXkIfy89nUM97_Cc5LBMUtEQfSaTcM_wYi5WVGlWYjO45JBF6ZmXzlDWyKcbk1_hiP5DaGVFXG7iPMzCg-g-_xFgx94KFPgmuuPs6CaNcjgdm-HKAjLpzWDcabIddkDZ7nVpl_8AqcI7PV9iNe4QbrmcHAMIvFlDzWyrSt15Z4ZAU7Sj6Q-vdqo8VjOBNmwjveVeJwoYdhig1cQf3_hKeEKbYrSuW8aaadE8E2cUyCiAxuQiFCTWtM0KG6Osin90tX8QsTW_wzrZRbxdsqC_nvYjoKL9rwbRib5IHiAbv4xuw6_OhGPALa2l80VUvAmkCtLNParLczrt-4KqCBP6cK_ul5sYOFiK7L1IaEn0H_NRrfBEj4gB6w5I5RvIOhrPhaTjf7LD5HArAedvd-1cKCngdhO1M2BhT4U6_jqgwIJ3z8Zcxo-6KkMeDmz54_EFNkfniw7nK6sBzMkF06HC5rvfRZs-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده‌یاد مانوک خدابخشیان:
"اگر رژیم مذاکره کنه باخته و اگر مذاکره نکنه هم باخته"
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69266" target="_blank">📅 19:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69265">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=Sil0HAjzepmuIzE4Bv1EvaZKqW1EwI1ZopcurftWMRCv80l7iXaLLDql0M8PNxh9dg8JY1NuAmZ_ho9xPwuLb0gFgNncL9SJQRL1qzEVDTEM_mSAtpHyOFk6EEEloU0yTlYHUHJapMxDQM8r9ACIwleF_B2IMTWlQedIGF_vxPyrtazqwg-h9B3LBl18pSU947Y10SmNqfmL-dPNvo5LyS3MfKQzsNpMxYgJ_xv0cbNOa9FPklYPL8zjD4pbYdnUJlt39KTFcxLEG9u6FkR8OHT-y0HJ9tS2205dsOGoZ1A-VVplMLtT-h60bbUMaJ08BMu_vKjcpAsHavP0y1ca5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cce71ed1d1.mp4?token=Sil0HAjzepmuIzE4Bv1EvaZKqW1EwI1ZopcurftWMRCv80l7iXaLLDql0M8PNxh9dg8JY1NuAmZ_ho9xPwuLb0gFgNncL9SJQRL1qzEVDTEM_mSAtpHyOFk6EEEloU0yTlYHUHJapMxDQM8r9ACIwleF_B2IMTWlQedIGF_vxPyrtazqwg-h9B3LBl18pSU947Y10SmNqfmL-dPNvo5LyS3MfKQzsNpMxYgJ_xv0cbNOa9FPklYPL8zjD4pbYdnUJlt39KTFcxLEG9u6FkR8OHT-y0HJ9tS2205dsOGoZ1A-VVplMLtT-h60bbUMaJ08BMu_vKjcpAsHavP0y1ca5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⁉️
سنتکام:در ساعات گذشته، رسانه‌های دولتی ایران به انتشار ادعاهای نادرست سپاه پاسداران انقلاب اسلامی (IRGC) ادامه داده‌اند؛به‌ویژه سه مورد زیر:
❌
ادعای اول: سپاه پاسداران (بار دیگر) مدعی است که مسیرهای آزاد و باز در تنگه هرمز برای کشتی‌های تجاری خطرناک هستند.
✔️
واقعیت: خطرات فوری که کشتی‌های تجاری و خدمه غیرنظامی آن‌ها را تهدید می‌کند، ناشی از تهدیدهای لفظی و تلاش‌های سپاه برای انجام حمله است.
❌
ادعای دوم: سپاه پاسداران مدعی است که سه جنگنده رادارگریز اف-۳۵ (F-35) و سه فروند هواپیمای دیگرِ ایالات متحده در جریان حمله اخیر ایران به یک پایگاه هوایی آمریکا منهدم شده‌اند.
✔️
واقعیت: هیچ‌یک از هواپیماهای ایالات متحده در تلاش‌های اخیر ایران برای حمله، منهدم یا دچار آسیب نشده‌اند. تمامی موشک‌ها و پهپادها رهگیری شدند یا به مناطق هدف‌گذاری‌شده نرسیدند.
❌
ادعای سوم: رسانه‌های دولتی ایران گزارش می‌دهند که یک نفتکش تجاری به نام «ام‌تی نورا» (M/T Nora) موفق شده است محاصره ایالات متحده را بشکند.
✔️
واقعیت: این کشتی تجاری موفق به شکستن محاصره مستحکم (دیوار فولادی) ایالات متحده نشده است. بیش از ۲۰ ناو جنگی، صدها هواپیما و هزاران نیروی نظامی آمریکا همچنان هوشیارانه به اجرای کامل این محاصره ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69265" target="_blank">📅 19:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69264">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=LPGTu64f6a8cO7J86YSYka0FpbU-7UTpr0iYON2mYbdfxxiLD3BUK1SYSFg2biuX7aMsgJGOFDx5hsIu8rzFeFO8Ov3xGUgySy_E9x0lsYjD2qXsGACf8r8McNohanV0UcEyhwZ0YctIODu1_W1Awu-gsfXxU2xwe3u8ut38lJ7BHtB00uOpk7loROu5DsgUi6za-ucZww6UfLCemqU4i7Qk4SwF57WZvDUJvk7Bnquvq3PK7AAHFi14dmYE5I2W-nGCP-8T_Vrl2iKUaQWdBXfQ9dJXRgHQ_Fzf5E5S62TJQvDf07e7sub0DlqKN5DIskHqJdQI1i0y4YcxCvOmGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/906e47e12d.mp4?token=LPGTu64f6a8cO7J86YSYka0FpbU-7UTpr0iYON2mYbdfxxiLD3BUK1SYSFg2biuX7aMsgJGOFDx5hsIu8rzFeFO8Ov3xGUgySy_E9x0lsYjD2qXsGACf8r8McNohanV0UcEyhwZ0YctIODu1_W1Awu-gsfXxU2xwe3u8ut38lJ7BHtB00uOpk7loROu5DsgUi6za-ucZww6UfLCemqU4i7Qk4SwF57WZvDUJvk7Bnquvq3PK7AAHFi14dmYE5I2W-nGCP-8T_Vrl2iKUaQWdBXfQ9dJXRgHQ_Fzf5E5S62TJQvDf07e7sub0DlqKN5DIskHqJdQI1i0y4YcxCvOmGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه پسر جوون ایرانی رفت پشت فرمون ماشینش ی خر گذاشته رانندگی کنه خودشم داره از رانندگی خره فیلم‌ میگیره
😳
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69264" target="_blank">📅 18:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69263">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
انفجارهایی در صنعا، پایتخت یمن رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69263" target="_blank">📅 18:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69262">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXBouNaxajxDP9pIhss5c64baPO_UeN0G0vM_ihGDHFyfLQYTimGDI6JiEyjp_QodtZbJoi426jl6nUmBvQ3-oX4lI_t7vdPJVdEP_1fSXLerTEBeutaFftQneSSwMi0u6S--yhOR_T_zan_d00S5_LbYSdwY5ZGAsnzAtRhkfbrjV3rds9gf4vXsVwgqBT3haNlnb-_oaP235lfgFUTp66YAPI057RV7EwpAs42uTRFFpXOMpV1S5S1oUFKHCxUdkCdEqDrSfP73l5sjtOqFC5_w5YxNo69dCizFDW4hF1QGUKG9pWKEbOs91rKcsxK0t2VHq4EcPglYQ2eFTm0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه تا از تروریستای مفعول حشد‌الشعبی که در حمله مشترک آمریکا و عربستان به عراق کشته شدن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69262" target="_blank">📅 17:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69261">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBYRC5VcvO4Z6oIlBXZo-1KGzfXxDqkX-GZaucvYjuvnLb3gzsZovulb5hoOOBlKKqd5-Bvd8KwfPGIQfUx7n_QOD-xCDD2pJaVUIQwvmEDlIkcfrqkeE5Jmh5LHyEJgfY87_xR1PBfgPbwdzrYOQ1cc0fE8G83jZ-2kSXYz57CjzgCOOLC_lvQGkGYeHI6iWUZJTtacB52G77tVOz-6hPcs0-t5hj3kmK1LwyYztW6XiJVV3OtbSDomATIhuaK6D6MYsk4bU8LuAWgKX4VWn-2R2IhAO0wPP1t189OWuHNW3PqD64WUvMWgHKW26roZuEojjhLqGZEAwlvBNQZEIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
روابط عمومی سپاه پاسداران؛اطلاعیه شماره ۵۶:
دو آشیانه پهپادی و یک مخزن سوخت هواپیما و بالگردهای نظامی در پایگاه علی السالم به آتش کشیده و منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69261" target="_blank">📅 17:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69260">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=jMXmoQJTXAbXD7c2g2FhhdpB5vLKUhjwNI-vBLRPMkw1XEB_P2X--0TE-jRsoLsBI40j1bT07-jeiLtDOETmhOhPPGaSMhJ1xzWtTkLP1F-42SgbDZQkT8RU-FycVVk9uvaue1frhtJtWUFK7J8ruqlTsUBtXJCx0P9a_CWi15rilec74vUanTizX_OHnZwOqtyLMHOmCToXTPsY8cvc7_Q50XEeXL2pe2Z9PPqh_hiON2WbodOjv55ZMIoQX5xH2mtzcNlfSip4lPPYOVge9m5DsjbotAt7yVSIaWkaWNVkZuxWUiMrY2IAUwh2nXnfteCvNfGnPvlYoIWR1w4yQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=jMXmoQJTXAbXD7c2g2FhhdpB5vLKUhjwNI-vBLRPMkw1XEB_P2X--0TE-jRsoLsBI40j1bT07-jeiLtDOETmhOhPPGaSMhJ1xzWtTkLP1F-42SgbDZQkT8RU-FycVVk9uvaue1frhtJtWUFK7J8ruqlTsUBtXJCx0P9a_CWi15rilec74vUanTizX_OHnZwOqtyLMHOmCToXTPsY8cvc7_Q50XEeXL2pe2Z9PPqh_hiON2WbodOjv55ZMIoQX5xH2mtzcNlfSip4lPPYOVge9m5DsjbotAt7yVSIaWkaWNVkZuxWUiMrY2IAUwh2nXnfteCvNfGnPvlYoIWR1w4yQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی وسط خیابون بعد از شلیک دو گلوله به پا؛ این همون شخصیه که تو لایو دخترارو کتک می‌زد و...
⚠️
‌ ‌ ‌
حاوی خون و خون‌ریزی
🔗
‌
مشاهده ویدیوی کامل بازداشت
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69260" target="_blank">📅 17:24 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69257">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=B_I5P9I0XuAIiNuyVrdXcqNqGm8iKSKh2WaxGvQGfE_SIamZLha7pEhIbIofnxi5qNvHtjNfPpkWzUTZf5QEw7_QLFUJsOopRUWvoUL6QHHtoQeNAbaiUhwunoTgLfrZ89zl7o2-MmhMnScFTJSBQUF5-Hg4Xzh6oSMiM4OQxwSSw5qiglv2adHoS06npVVkNgy24hu4G4Y23DtTZGd8NXUK4tTk-2c6Ih2ZfMtxAddoHkOUN19an8vI2QfkrcP47iZkyrebvHCjCh4Q5T4loZRPewGDpYFbj1-dzPxmra0g261gfKlXLhSCZl4qpAQ3jiB4qliO-bs-5OhWYFMN9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cea20ae2a1.mp4?token=B_I5P9I0XuAIiNuyVrdXcqNqGm8iKSKh2WaxGvQGfE_SIamZLha7pEhIbIofnxi5qNvHtjNfPpkWzUTZf5QEw7_QLFUJsOopRUWvoUL6QHHtoQeNAbaiUhwunoTgLfrZ89zl7o2-MmhMnScFTJSBQUF5-Hg4Xzh6oSMiM4OQxwSSw5qiglv2adHoS06npVVkNgy24hu4G4Y23DtTZGd8NXUK4tTk-2c6Ih2ZfMtxAddoHkOUN19an8vI2QfkrcP47iZkyrebvHCjCh4Q5T4loZRPewGDpYFbj1-dzPxmra0g261gfKlXLhSCZl4qpAQ3jiB4qliO-bs-5OhWYFMN9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حملات شبانه سنگین روسیه به کی‌یف، پایتخت اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69257" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69256">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=NhWgNdKcJKqL2POmOhTxWRY5fUzivdCCTowMXLUpKDHGFlerT3aR-IdT5OGeMJjSovKCdexR0uzNaQQq_0uh_6Fn_hT47X9QNUqzd9UDYF6asiju2hsHg9PqkJrd85s37VX0UM_G1_Za1l_B3oHhsfn76EbecqMx9g_C8_CC6Emm99lDAOZ2LA9j4U8BqSaiws_mnI7DrCNv1Nt8OaG8Yn6kiCt6rvI-hW66u6jhv8O2we-L7WwFZvdUGcHYsSXy26Yd0OxqGu7lNXRXu9C-U1eabcggomjzSssGcXgHk7qDa9dlgo3CHoVo_eie7aaI1e1pEOBSHPUXS4Gp9jscKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d31a669dbb.mp4?token=NhWgNdKcJKqL2POmOhTxWRY5fUzivdCCTowMXLUpKDHGFlerT3aR-IdT5OGeMJjSovKCdexR0uzNaQQq_0uh_6Fn_hT47X9QNUqzd9UDYF6asiju2hsHg9PqkJrd85s37VX0UM_G1_Za1l_B3oHhsfn76EbecqMx9g_C8_CC6Emm99lDAOZ2LA9j4U8BqSaiws_mnI7DrCNv1Nt8OaG8Yn6kiCt6rvI-hW66u6jhv8O2we-L7WwFZvdUGcHYsSXy26Yd0OxqGu7lNXRXu9C-U1eabcggomjzSssGcXgHk7qDa9dlgo3CHoVo_eie7aaI1e1pEOBSHPUXS4Gp9jscKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
صبح امروز ارتش آمریکا به یک پایگاه پدافند هوایی سپاه‌پاسداران در اهواز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69256" target="_blank">📅 16:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69255">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=QDeLsUn7k3Y25pAQf1fHbLGDIizVowWc05A6n4CKyKJg_40-5LNXJV_whbAOIWLMUJPL3fzls6YWhOXpZ18haYBrxWjmAAh9FaDn7J7ew4YtolQowaqppBJ_bfJyqOjUabwLsliPhtHkRiEkddPu40X3vtnoxcDm6IXojVNvX96IDtwkH-men5rVLLDfk7uSKT5183oaSPc0gbXT5ngZA_M-2_on3U7uVxl_fiC3CcNu0pG_0DhASczI5jeEt2Hq0V35g5hPycCvk_wuBVuzQUOupdCv8Sv9PTPVgIK4prY25gvBLK1OxWV6gbqsDRfHqW41pdJ0XpOfvOMHVTZ63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21d6f2f438.mp4?token=QDeLsUn7k3Y25pAQf1fHbLGDIizVowWc05A6n4CKyKJg_40-5LNXJV_whbAOIWLMUJPL3fzls6YWhOXpZ18haYBrxWjmAAh9FaDn7J7ew4YtolQowaqppBJ_bfJyqOjUabwLsliPhtHkRiEkddPu40X3vtnoxcDm6IXojVNvX96IDtwkH-men5rVLLDfk7uSKT5183oaSPc0gbXT5ngZA_M-2_on3U7uVxl_fiC3CcNu0pG_0DhASczI5jeEt2Hq0V35g5hPycCvk_wuBVuzQUOupdCv8Sv9PTPVgIK4prY25gvBLK1OxWV6gbqsDRfHqW41pdJ0XpOfvOMHVTZ63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدویی از لحظه دستگیریِ نوید زیادخان قره‌داغی حرومزاده چهل پدر وسط خیابون:
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69255" target="_blank">📅 15:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69254">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=M1R0pxy0IkfhJQgEnurZ6Cm0-UrGGcqMfnngigDpLXOkV98HMhEq4F8q76q7gydHu3WDqDpqBmBNnvR8Q2cyohb1U26AhFT475uwVoKBDkUrrJ23E6ChjrNtAGbXNsuF-2Zw7x73iFDnogr-bcrXcYc7qM3Ozrb5uUDUMdD2aTN7vpnugpYJMEiVzwNPQB3x8yqqcl1DuoM7duVNQ3bDOxZhDbV4ugSmmHTivKKxVQxg8-uuZHaHJaz7X2GErgs683-pZbTTMaR5Erd4KZ7x7ZsL6L0DIqu9BJtEuAZtruWyEZhi0e3TNxp_hGCGbCDC9eubdmrUyu04ulpZK_78JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1666d9190.mp4?token=M1R0pxy0IkfhJQgEnurZ6Cm0-UrGGcqMfnngigDpLXOkV98HMhEq4F8q76q7gydHu3WDqDpqBmBNnvR8Q2cyohb1U26AhFT475uwVoKBDkUrrJ23E6ChjrNtAGbXNsuF-2Zw7x73iFDnogr-bcrXcYc7qM3Ozrb5uUDUMdD2aTN7vpnugpYJMEiVzwNPQB3x8yqqcl1DuoM7duVNQ3bDOxZhDbV4ugSmmHTivKKxVQxg8-uuZHaHJaz7X2GErgs683-pZbTTMaR5Erd4KZ7x7ZsL6L0DIqu9BJtEuAZtruWyEZhi0e3TNxp_hGCGbCDC9eubdmrUyu04ulpZK_78JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت صداوسیما بعد از هر حمله آمریکا
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69254" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69253">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.  ۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69253" target="_blank">📅 15:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69251">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/c-mvvKA7ocN1idfYsFssZ1B8kBhxtJh_nQQbmcC8uh0Dzd7q-xHFgWGe3YOdLWjJAv_SBMD1OoL3UaduCbCSJxjzjD4b_uISmuMsCyVF0pxZWczbBTrNEX4MmlvzSuSNFXSV5cLGLvtRCsBoivkK63hQUuPuGwdq-Ueu3XlIsqqhmoeRi4Eu_-NFIMisI9a8EnCCWl_ab3Rc_yfwvwhIi7YMQ3XUnxjw_IJL4hnmQAtDLwLdvps-pGo1IH22GWkeRhLSRtmtz9pZeQhQRQTfUKNkAEifhopAQpjJlDlg-FE8AFZWGO0bvRiMbPAb0AlUlnWB8yM2cyUu_TvMxeUWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=ZRrwSYm0Q5fFBvom1lKleEam3ezUnbRYlu7qKrmb_IrlpMBaBHo6TT7kocMiqDsRAK1L1ujDfrAKdzDFdxC7phmFeLtSQ4JBYFXn729oSC-cxPzloC2Q0AYYP_pBQWFkrLh3yBZhBC8tum3qu3DN6RHot2g2n4VRK8Re1ZN1uMbxiKC94usKRvkYTXG4LrXwmm1gUQidi11A4jJbQUONOQCKLdyIBpRqi03Vs7a871yxUTe7uFIukgbUwBHqEQ_Tk0A_TEpKXKB4fOeAFre6ttSnwKl_TFhyExWeqJ22KG8zpp9h9TLwXVHl8j-64XV5921oX8t0Jg4ZnC2sO-fngQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8b887c1d39.mp4?token=ZRrwSYm0Q5fFBvom1lKleEam3ezUnbRYlu7qKrmb_IrlpMBaBHo6TT7kocMiqDsRAK1L1ujDfrAKdzDFdxC7phmFeLtSQ4JBYFXn729oSC-cxPzloC2Q0AYYP_pBQWFkrLh3yBZhBC8tum3qu3DN6RHot2g2n4VRK8Re1ZN1uMbxiKC94usKRvkYTXG4LrXwmm1gUQidi11A4jJbQUONOQCKLdyIBpRqi03Vs7a871yxUTe7uFIukgbUwBHqEQ_Tk0A_TEpKXKB4fOeAFre6ttSnwKl_TFhyExWeqJ22KG8zpp9h9TLwXVHl8j-64XV5921oX8t0Jg4ZnC2sO-fngQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مادر جاوید‌نام ابوالفضل سپاهی، که توی میدان علیخانی اصفهان اعدام شد:
خطاب به یه نفر به اسم هادی: بگم برات که تیر زده بودن تو پای ابوالفضل؟ بگم برات که زیر چشماشو با فندک اتمی سوزونده بودن؟
بگم برات که ۲۰ روز بهش آب ندادن؟ بگم برات که فکشو شکسته بودن؟ بگم برات که دماغشو له کرده بودن و آویزون شده بود؟
هنوزم تحمل شنیدنشو داری که بگم برات...؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69251" target="_blank">📅 14:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69250">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇮🇷
سپاه‌پاسداران:
تخریب کامل سه فروند هواپیمای اف 35 و ورود خسارت سنگین به سه فروند دیگر در الازرق در پاسخ به جنایت دشمن آمریکایی در قشم.
همچنین چند افسر و کادر فنی و تعمیرات دشمن نیز در این حمله کشته شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69250" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69249">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daa6076311.mp4?token=eqKSvAxEKEuaIbQMxbudlaP3quZLrEblDUsDk0U9DIlvPQkbJjgBHCtrDKAKybe35i_pmN7bVo8coc7VVkLzgCVhMZ_lCxEloJHNq37MzbQPnvEPHsUdMg2uR2vhCk2TtnoI0UDr4INYBkP4UrKP8jEQGWSIwqkus4n5VB-Wa3tMPyIWqovcooQ_rRRi2S-Ymj5eYShdhnoBSLfjOAKYUtIXtvprZISITOIntR-Pqdc_Auv47HBvpWsfrSUHCaKzuBpDP5N9LkWMMeTisyq9r4UqXPrTOFH0vXVoRYAFYNCZ3FxHMqQPCK0ljJqZknk1xY1UvdbanO84Wx2MfaPLpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daa6076311.mp4?token=eqKSvAxEKEuaIbQMxbudlaP3quZLrEblDUsDk0U9DIlvPQkbJjgBHCtrDKAKybe35i_pmN7bVo8coc7VVkLzgCVhMZ_lCxEloJHNq37MzbQPnvEPHsUdMg2uR2vhCk2TtnoI0UDr4INYBkP4UrKP8jEQGWSIwqkus4n5VB-Wa3tMPyIWqovcooQ_rRRi2S-Ymj5eYShdhnoBSLfjOAKYUtIXtvprZISITOIntR-Pqdc_Auv47HBvpWsfrSUHCaKzuBpDP5N9LkWMMeTisyq9r4UqXPrTOFH0vXVoRYAFYNCZ3FxHMqQPCK0ljJqZknk1xY1UvdbanO84Wx2MfaPLpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرود دیدنی یک F/A-18 Hornet بر روی ناو هواپیمابر.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/69249" target="_blank">📅 14:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69248">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cob9-aNAk88ezrI1d95plbl-rssdhmR_6X_ngDULFdifLgqHOk2n_iKZObPZT9eCabYhNeeYBFRqgLll3TIZY_H-hULCV6YnPS_fYY59r93ibLyaMa0DH8_2z4-fyKwMsSpqoD6wwbtLL2uYEiXqiEJNz9dqkNHSfToRatkSz71yIEItWgzkFSMBQrAFwq0Shaw3xcVOpE1U5KpnGTexxaBP2KHsceYnTAfFfDafgGUSP_3eirAq_n7ZCrm6U5HnLgh3Pm4UQirOiYoHfCy8CByBA15tSnj8-inmAUAhgNB3tjl16ZoB5leOYgCuNDV29O9RvftCvQz2ta25_BoxHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
⏺
ان‌بی‌سی‌ نیوز:
به گفته منابع آگاه، ترامپ در قبال مسئله ایران «به‌شدت کلافه» شده است، چرا که مقامات ارشد بر سر راهبرد واحدی توافق ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69248" target="_blank">📅 13:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69247">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a176457914.mp4?token=kfXw-A3NHyLw_mtnce-eObbSzXwgpxI4u6xxB9sfOHsH31T3yNepjHwrCZnsxy9PQOmfFS79_o3rIlUH-XUWTdwGL3jEbd3ubQfXk7eUpqPw5AZNJH6rdnktKUnxzz9Y3GBbtpn9zJZXDrGgTHElcI1-NoR-93C6mq0jrrE7XO1eeifkLJdOfKadgKF6AXLorynXaXq7LA5jrkIIOJVKuiECF2i2zbx6wyHicSvH2BgEP01Jo6tvjRN2G__ggz_J9U1lO8RKBmgt4fisaiOxxvO-7F2QKgrVcDfV9b0vBqO0P5UWMwFhwN6uAjBufl9eTiib8pC2n4IberXgG2NPZ4YCulu9IDq27LoMrwPXYZOaKByKQr6o-BSecAYQ_hWySGTDA6iO-hzeifafasiRtXKjDCZIuVHmEcGEmgbxVvf4BeEHosKz7VtT75WW1fTRHkSLYV16wQPjRQAbSd147MJHcFG1lk5NXNnnNanw0kO8efRadqA4lVZ23aLIS34sRrppEzmr5Rv6kyCTStFat-gYf6t23djFUFgm9iIqk451BmcTzdKYo2QDcm5nFXRJpFc_pUQ7LcQbPfEL21c-mq0cntHQUuEJlamFU7vLi5snGY-_seryxEUbKITYzxrnjq5leRKXJ_7Q0yhMLTxBjTUjP0g-XPMSGPBH9coKouE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a176457914.mp4?token=kfXw-A3NHyLw_mtnce-eObbSzXwgpxI4u6xxB9sfOHsH31T3yNepjHwrCZnsxy9PQOmfFS79_o3rIlUH-XUWTdwGL3jEbd3ubQfXk7eUpqPw5AZNJH6rdnktKUnxzz9Y3GBbtpn9zJZXDrGgTHElcI1-NoR-93C6mq0jrrE7XO1eeifkLJdOfKadgKF6AXLorynXaXq7LA5jrkIIOJVKuiECF2i2zbx6wyHicSvH2BgEP01Jo6tvjRN2G__ggz_J9U1lO8RKBmgt4fisaiOxxvO-7F2QKgrVcDfV9b0vBqO0P5UWMwFhwN6uAjBufl9eTiib8pC2n4IberXgG2NPZ4YCulu9IDq27LoMrwPXYZOaKByKQr6o-BSecAYQ_hWySGTDA6iO-hzeifafasiRtXKjDCZIuVHmEcGEmgbxVvf4BeEHosKz7VtT75WW1fTRHkSLYV16wQPjRQAbSd147MJHcFG1lk5NXNnnNanw0kO8efRadqA4lVZ23aLIS34sRrppEzmr5Rv6kyCTStFat-gYf6t23djFUFgm9iIqk451BmcTzdKYo2QDcm5nFXRJpFc_pUQ7LcQbPfEL21c-mq0cntHQUuEJlamFU7vLi5snGY-_seryxEUbKITYzxrnjq5leRKXJ_7Q0yhMLTxBjTUjP0g-XPMSGPBH9coKouE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیلم گوه خوردن نوید حرومزاده هزارپدر که دخترا رو کتک میزد اومد بیرو
ن؛
از همه عذرخواهی میکنم ، گوه خوردم غلط کردم!
بذارید برم توبه کنم ، درمان بشم و برگردم به زندگیم برسم.
اتفاقاتی که بین من و اون خانم‌ها میفتاد رو تو ذهنم الکی بزرگ می‌کردم و دیگه کنترلم رو از دست میدادم.
خانم‌هایی که کتک میزدم، من رو درک میکردن و هیچ شکایتی ازم نمی‌کردن.
اتفاقا مردم خوب کاری کردن که انقدر واکنش نشون دادن؛ باعث شد یک بار واسه همیشه به خودم بیام و خیلی مسائل رو کنار بذارم.
از تَه قلبم از همه مردم عذرخواهی میکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69247" target="_blank">📅 12:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69246">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=vvRDczrfO4Aoaqv7QHNTUsQsZYIDodXhvnYGiQKxX47CxY56d1eSWWkOgHHRP5Jt1ZAHn9yxvBdIPg3oeW2ORVU6U7E5R6WgUicGRGN2kqrjxW92iU6e0Ngs8W04EWE2Hi-TeY8D9xooaTI_osv3F5Q4W3PhvMN0Bz4QTQtjPhAsHQfj2uFdvWYrPffgDSORPxo7bDPR8NZR1SWEypLhLNpW2jnptzaWlT2vITVR6lnfRZMWTEFRv1WBRoqdEuhK76_xVoB1FH-T4cro6pGOMPUaMzltebMCoMCphMChboxZvcrKswbMoCUV86sb71ckbEpalVTKcCIrsRXA19hyRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1958bb40.mp4?token=vvRDczrfO4Aoaqv7QHNTUsQsZYIDodXhvnYGiQKxX47CxY56d1eSWWkOgHHRP5Jt1ZAHn9yxvBdIPg3oeW2ORVU6U7E5R6WgUicGRGN2kqrjxW92iU6e0Ngs8W04EWE2Hi-TeY8D9xooaTI_osv3F5Q4W3PhvMN0Bz4QTQtjPhAsHQfj2uFdvWYrPffgDSORPxo7bDPR8NZR1SWEypLhLNpW2jnptzaWlT2vITVR6lnfRZMWTEFRv1WBRoqdEuhK76_xVoB1FH-T4cro6pGOMPUaMzltebMCoMCphMChboxZvcrKswbMoCUV86sb71ckbEpalVTKcCIrsRXA19hyRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
خبرنگار صداوسیما حین گزارش پرید توی آب و فاز کوسه گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69246" target="_blank">📅 12:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69245">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcpZcuBicUtX7PQ5g5MclrnfYcRI0B3Aen1QZZfqpy_N4YOlkAcveTMYbKaiHGwNUluUchEpJE6lzIDp24s5SNIm9e8dxrrJA4k5fzssRdxc74fHGQ0bA65x43gzPPDo0o_Zwiz-PNZ70s52PH-dEFlGOzuhbgi9eaTSXftKshJ1NHu7cD2nt8joyMrMrs6YXy1fWIV-oFoH1cO-0MjxilXdaJevWiV0bKsnZ_XnqYop_hoRnF3BtGwBD_713_JNOxoOE8GM9NqVInLlpCZce8fEl1gQzbmXDaX-DzGo01IFEd9cEHIb-NbkhodufK-Tvdp0BlBgkdw8tpMBsVUN-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
سپاه پاسداران:
متجاوز رو همین امروز تنبیه میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69245" target="_blank">📅 11:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69243">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQxcq9Fw4XjxHVC-vZNget9dxvbFvcOsPK2vnIDDDjgFbXhfVY8tYBjRZWjHjdqLKPuv41i8LwldcEH4k-nF2mTuVt0gsJYzlsW6Lvt68CoEDwj1faqz2o8J_bOsXuSBWLdUcc7dwElfJnid6P194dgjMuOrsHhS5hAPifr35U73kJGkJZTPLTRXcDQ-2U0bmBvC5WaeZ9EcdPnx3Pz_Ycgqd2zj33HDnK3a5g36UddIZKwA-bdouHCDH3UVu-R5i62QatC4J1pFoqkl2gxZJRZW8R3GVqTAYKpguThNOVfSAHAUbSajI99JXhHUKiodv-MkqldPbf6tAj7R1aBA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854dca423a.mp4?token=gWRdvqFwhJJqRi-jwapN9lMmhVZMhQdlARDyq2sgSpyhITPmajltKP2SCVvUBTgDr28CU6Rknj6knG7Urr2TKUXrJnrVioTWDr1uLL81YkOP8Z_3HHfJQssuJhA2QlF8s4tR85g3lTA-D9mZYvy5b5DhMUm6_b6DDV0pyyKVhPHmDm4fMTwIAbt1WUk2WsK0omBRJhA0x-zDvQdUQtRXsrmjsqWrj64qRRkWOOEMKC8NI530tdcPTWKiF-Rjv9ttH99qa6hCZXs7XupNfZukCiR1AVEYl6kYKqrCn-K31YXKxYXTO3dQkpznGeH_GhuOKkN36t43AKA0d2IV2vQVeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854dca423a.mp4?token=gWRdvqFwhJJqRi-jwapN9lMmhVZMhQdlARDyq2sgSpyhITPmajltKP2SCVvUBTgDr28CU6Rknj6knG7Urr2TKUXrJnrVioTWDr1uLL81YkOP8Z_3HHfJQssuJhA2QlF8s4tR85g3lTA-D9mZYvy5b5DhMUm6_b6DDV0pyyKVhPHmDm4fMTwIAbt1WUk2WsK0omBRJhA0x-zDvQdUQtRXsrmjsqWrj64qRRkWOOEMKC8NI530tdcPTWKiF-Rjv9ttH99qa6hCZXs7XupNfZukCiR1AVEYl6kYKqrCn-K31YXKxYXTO3dQkpznGeH_GhuOKkN36t43AKA0d2IV2vQVeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔞
ویدیوی وحشتناک از یه حرومزاده به اسم «نوید زیادخان قره‌داغی» داره همه‌جا پخش می‌شه، تو لایو اینستاگرامش چند تا خانم رو خیلی بد کتک می‌زنه و کلی بهشون فحش می‌ده.  هنوز دقیقاً مشخص نیست چرا این کار رو کرده و اطلاعات موثقی بیرون نیومده، بعضی‌ها می‌گن دخترا…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69243" target="_blank">📅 11:28 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
