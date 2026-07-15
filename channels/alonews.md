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
<img src="https://cdn4.telesco.pe/file/dwZbFyAdL54vlTBLUUxV0mghyeE0dOLbv4XHH1_Xn9lDEwb1L5yhzv_wRnHqPIUeyhwzm6zpPthsNI7CFw6_XDqJRb8wux9jU7TVh3DxkptjTWRGIWr0Td_fFn_F1_QCIHNoz8fF3KDaGSVH2aL0hfJAdZH-rLqyrnrnN2bEk1yYRmNSnGNmd-xdEcrruSd5d-I0ARstqwRkSI-R33_jmQb-neA9CxYGiFuSy5d2_sgXA8hPXa1-Ko7f0fjTCvgh2evvfTTlzlsjt0gewOaM4uCabowKDnxwpMVgOSWmqeMmQIXdwfgmIzYDuvGcorpwJqHrjEBZSHUGASY9YDiFvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 23:34:48</div>
<hr>

<div class="tg-post" id="msg-134565">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده: موج جدیدی از حملات را بر ایران شاهد هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/alonews/134565" target="_blank">📅 23:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134564">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkvetM4zi3NhKWUDSc0kt5gaSMBcqWOCbAroA57dtW-Matb8uuL-wMoihr9axWG2uIFBwq8uD1HQ25-mVgZw3DU-NcQtGLWRfFQ9xUQJylU44xrq-nlNg980LZi6AQB-zpwJu-mIoKEzYty2Ju1TgkR_Cu6Zdy5NbTNZOcpR-Y-fAgBRIddUYkgcXm-WTu6NG8ctjYDuzI001g_gMXPPVcz36MXM2mF2_1JwMzsOmE9ejVPDVO5ZwfWxp6KkDrMXeasSwgs76hVEOFZven2n1czn74xoyNsQMFCJYKuJBtAH8zZ1zEoPkdnhr9mt1o694dEKo4b6TagUk-szdiwq1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/134564" target="_blank">📅 23:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134563">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd19d5490c.mp4?token=rhri5cLsp_BGg1ieMDkllT9dxscF0cLLcKkuvrY1j3i1cL3bXgedOL-yUDao7iUg0a5tUH5AG4fgBnGvjDW7s5qFJyF_bC7LQVomMwcglpUV2jVG9605h5MapQcZ5kCejiP-RUKSVgj33xWaOTFtooPIk6AezoBprVeCeGi_LxSA6p_Z_WhObxCSDWaRxbdd6bmnNdNXJyx6IuejPuZ6_Y34OHPjHMAGdWRP_vRUDBf1BzCOU01A95kLsrZxAv-1oojkajLtVUoFalC5YrTVTRVpVLkuc50jEikl4aG7uc_d_6I4kXxdp1XSe6-gRdJge6AhODZ8K5aTgDZXL0CAVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd19d5490c.mp4?token=rhri5cLsp_BGg1ieMDkllT9dxscF0cLLcKkuvrY1j3i1cL3bXgedOL-yUDao7iUg0a5tUH5AG4fgBnGvjDW7s5qFJyF_bC7LQVomMwcglpUV2jVG9605h5MapQcZ5kCejiP-RUKSVgj33xWaOTFtooPIk6AezoBprVeCeGi_LxSA6p_Z_WhObxCSDWaRxbdd6bmnNdNXJyx6IuejPuZ6_Y34OHPjHMAGdWRP_vRUDBf1BzCOU01A95kLsrZxAv-1oojkajLtVUoFalC5YrTVTRVpVLkuc50jEikl4aG7uc_d_6I4kXxdp1XSe6-gRdJge6AhODZ8K5aTgDZXL0CAVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستون دود در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/134563" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134562">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
صدای ۲ انفجار مهیب در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/134562" target="_blank">📅 23:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134561">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1841f7e8.mp4?token=AsSyDk0P-RXvGyx3aimMAthneulbkKy0g7DCumUUiJr2Tr4QxkWwtjw5qKjMtVPREJ8ZWyApH3Oaafyg1JvUT6Wh7QrFYdMeNqOCR420Vk9mmsp4yrqXHlWXTHIQhAIxxRio2bzSFF8Grx6WqcYk5Gvypa11MJO_p4AoenZvOS05n4nUj1YtubtDNtzN6e0gu0I2TsfYmHZmdEWACApjiFHe13E6B0B5Itk5wXreqT0quM_etOeC89WHT0lqO45oOlEpL8FZPp0oL0kvlrf4K_t7n547-U9vz0paX1kLyb3kX45PPUQduGswJ13dqozqiRQ3qDZpW8M7d4WAp0AjgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1841f7e8.mp4?token=AsSyDk0P-RXvGyx3aimMAthneulbkKy0g7DCumUUiJr2Tr4QxkWwtjw5qKjMtVPREJ8ZWyApH3Oaafyg1JvUT6Wh7QrFYdMeNqOCR420Vk9mmsp4yrqXHlWXTHIQhAIxxRio2bzSFF8Grx6WqcYk5Gvypa11MJO_p4AoenZvOS05n4nUj1YtubtDNtzN6e0gu0I2TsfYmHZmdEWACApjiFHe13E6B0B5Itk5wXreqT0quM_etOeC89WHT0lqO45oOlEpL8FZPp0oL0kvlrf4K_t7n547-U9vz0paX1kLyb3kX45PPUQduGswJ13dqozqiRQ3qDZpW8M7d4WAp0AjgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله هوایی آمریکا به بندر چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/134561" target="_blank">📅 23:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134560">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گزارش انفجار در ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/134560" target="_blank">📅 23:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134559">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
انفجار مجدد در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/134559" target="_blank">📅 23:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134558">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
صدای انفجار همچنان در بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/134558" target="_blank">📅 23:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134557">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
انفجار مجدد در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/134557" target="_blank">📅 23:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134556">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6068a6a93e.mp4?token=rgLBolZrugtyU7YnhU0loQxBxMhwBk0_30rEUFg0UEHoolQL_k7Wmu_dX3ZTLfpj06nS4GYr9hA2mG6ZljTZQjtOl0gshGg7jHBe1qUWp17C0jSgd3sKyw6bQfTEK7PQLPUhfQpPwhhmCpLqV-Wyga3J1bIHm_Iv8Fne7Bu_gZpRyuhIa1wU4EXAboYwuncmWjYGU0G33ihAKApZgZ_3vztmg0aYWVaEogA2Ux3oyjNqcmDdLwkP5RtjOCwGv-n6rEoHVdbBtizVrg42wEwyv9saVBO3mtdiQINtFpiBok9RgWaH_IbliPszX9TE_FI-RD2Mnp_O4G8WQYyaFyC23g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6068a6a93e.mp4?token=rgLBolZrugtyU7YnhU0loQxBxMhwBk0_30rEUFg0UEHoolQL_k7Wmu_dX3ZTLfpj06nS4GYr9hA2mG6ZljTZQjtOl0gshGg7jHBe1qUWp17C0jSgd3sKyw6bQfTEK7PQLPUhfQpPwhhmCpLqV-Wyga3J1bIHm_Iv8Fne7Bu_gZpRyuhIa1wU4EXAboYwuncmWjYGU0G33ihAKApZgZ_3vztmg0aYWVaEogA2Ux3oyjNqcmDdLwkP5RtjOCwGv-n6rEoHVdbBtizVrg42wEwyv9saVBO3mtdiQINtFpiBok9RgWaH_IbliPszX9TE_FI-RD2Mnp_O4G8WQYyaFyC23g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: به این نتیجه رسیده ام که نمیتوان با سپاه پاسداران انقلاب اسلامی مذاکره کرد.
🔴
خبرنگار: آیا یعنی ممکن است همانطور که با داعش کردی، آنها را از بین ببری؟
🔴
ترامپ: "بله، درست است. خواهیم دید چه میشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/134556" target="_blank">📅 23:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134555">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
استانداری هرمزگان: در حملات جدید آمریکا به حوالی بندرعباس  هیچ مصدوم غیر نظامی یا خسارت به زیر ساخت های مسکونی و تجاری  گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/134555" target="_blank">📅 23:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134554">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/134554" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134553">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gsD4deMENxxx9JbHLhwvX0YIqOMsK7SSzyL5ULGLADsd8uUVO4lovAYG2e-vxpSub5ZtSejSIbzCPuhFWoaSW0IjaLQmtu0XMX0LkSWUAj5LWwdpovJFpI9tp7zHr5AaFQL6QyYyj62H7lITCkGV_LcFEL75QyccuRwu3EzTGqKkfKH2V0GDTrfuQ0yHu6z8MBLx04yjvdD67Wn4lT6in4CCcdzEovZtlHK3XAKAEPPhJAniBfauJTt-m-p2nYromAtU49CRcFmydkMrLTzrrW7Ma71PXBrmckJOSBO6e1NTSOxMwuAuaZHQadi8j1LFD8FWABQAOjN9TgviaaVVog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منتسب به کرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/134553" target="_blank">📅 23:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134552">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8fcebb661.mp4?token=YjPmAXVAedsHLeoqLsiqzO3ZmvFpGl5vWgt_Xe_JdS58sbFwQWXFhKE22gc8tP5jOxiwi-s9NYQbkTLYqbT6dbpN4xY5DKz2tnt1XwudR13OAPpPhybr8dOGWWFZeNrBLrKsJHjIxsLa0XXjYGjtUuIVUirctvs2q4D5GvvbqEkGKx5dvAEqlq5LI44Ss8C8MpS7e_2QP9XJ_1Ptx_8GeOKHKBEc6pRN899p_Ef8tbCbIPMXBGpNZ8vXZCGUIjv5F9WI46hxEabvlixS2spYCw1D4XOETHGxEAlVhFBRqhzv5t-9thc1-PVTlixVungHgMuMv3jlCoJmYMEJqj0GMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8fcebb661.mp4?token=YjPmAXVAedsHLeoqLsiqzO3ZmvFpGl5vWgt_Xe_JdS58sbFwQWXFhKE22gc8tP5jOxiwi-s9NYQbkTLYqbT6dbpN4xY5DKz2tnt1XwudR13OAPpPhybr8dOGWWFZeNrBLrKsJHjIxsLa0XXjYGjtUuIVUirctvs2q4D5GvvbqEkGKx5dvAEqlq5LI44Ss8C8MpS7e_2QP9XJ_1Ptx_8GeOKHKBEc6pRN899p_Ef8tbCbIPMXBGpNZ8vXZCGUIjv5F9WI46hxEabvlixS2spYCw1D4XOETHGxEAlVhFBRqhzv5t-9thc1-PVTlixVungHgMuMv3jlCoJmYMEJqj0GMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از وضعیت اهواز پس از اصابت چندین بمب یا موشک به مناطقی از این شهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/134552" target="_blank">📅 23:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134551">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
به گفته برخی منابع ساختمان گروه صنعتی فولاد ملی (INSIG) سه بار در اهواز هدف قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/134551" target="_blank">📅 23:17 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134550">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
اهواز هنوز صدا میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/134550" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134549">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
گزارش ها از اختلال در اینترنت اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/134549" target="_blank">📅 23:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134548">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
تسنیم: پرواز جنگنده‌های آمریکایی بر فراز سواحل جنوبی سیستان‌و‌بلوچستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/134548" target="_blank">📅 23:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134547">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
پایگاه شیخ عیسی  بحرین صدای چند انفجار شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/alonews/134547" target="_blank">📅 23:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134546">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
۴ نقطه در اطراف شهر اهواز مورد حمله آمریکا قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/134546" target="_blank">📅 23:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134545">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
طبق گزارشات مردمی، شدت حملات امشب به اهواز حتی از جنگ ۴۰ روزه هم بیشتر بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/alonews/134545" target="_blank">📅 23:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134543">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEI1Ih41cjn7VzVcebL4KpZnavBel7ttxx0JWC9WJDWt86w89aUqrKF_INcRkzGMfKWss76I7SWhDAbxCuKbFnjn6vlPGNw6ETtBwohVuWt5h36GPkOOq_QtBNGScsptjYnpx1Oh-rv1ut960K5aNnFNaIFUVWnvAehPfVnurtypMvlXykJ4rJQpo0hGxwC2xBh30HGlqyfdrizESf-sCL86CMEKNwq1074XKNZqjj9CF8vc5aNf_l9nf-jLDfbOV-7B0qjrYGDcUsf37zmFUOOpvL8ewrbQ6rzpcI_9GJwAPANBWrlOTaaailLJGcO6BWsSvGjysBvb7HMKnsEZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9507b8c26a.mp4?token=CJd5ZeJ61FZP0InRr7_yjFlMq-jitVNgCv7So3Bhq7Hlm6zCPBc0Hj7rXdD3M8VhBSuqLEYLhPHmfL5d8p5VVGlneaUqTRhz_IPWB53FSiBKj8FGvi_NS33dA4S6PpJKVDiLedp9xaUkEP1d4cpMgJnGQQjVAAXZLTKrgO6qNDXGet_Sk5ekx-N7Q2v-nEd926iJnWKMgbPTgxvJKVPIVK7B_fcELZTowxM_-WGO7bylghp4YcknqOHAoHZDZZ5aUySErInWarQ953afIUqVOIVf7DzbyQhV2EoOhcIeiDVcpixlqtxmn8285RKereDwhtMs3p0g2rbzOWO0Z2GVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9507b8c26a.mp4?token=CJd5ZeJ61FZP0InRr7_yjFlMq-jitVNgCv7So3Bhq7Hlm6zCPBc0Hj7rXdD3M8VhBSuqLEYLhPHmfL5d8p5VVGlneaUqTRhz_IPWB53FSiBKj8FGvi_NS33dA4S6PpJKVDiLedp9xaUkEP1d4cpMgJnGQQjVAAXZLTKrgO6qNDXGet_Sk5ekx-N7Q2v-nEd926iJnWKMgbPTgxvJKVPIVK7B_fcELZTowxM_-WGO7bylghp4YcknqOHAoHZDZZ5aUySErInWarQ953afIUqVOIVf7DzbyQhV2EoOhcIeiDVcpixlqtxmn8285RKereDwhtMs3p0g2rbzOWO0Z2GVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اهواز از شدت انفجار زیاد صداش تا چندتا شهر دورِ دست هم رفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/134543" target="_blank">📅 23:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134542">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
فوری/شلیک موشک از کرمانشاه
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/134542" target="_blank">📅 23:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134541">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/893a539e51.mp4?token=DccBK-q8vuSuN0fXhpR-Az18sImDRH98jZq4xLUDTkY1LLJyY-ioru0BjKipeeOJwQEyuCXW5UWGAsxMqkoQcNY2wsCN63kuuqMRvCPSHkuIrQ10r6pj0McoDncmRUhw4rV_VB4MldwsFs-ytPwSQbTYahzVuzMFY8GjKCpmvwseXKdX-9TP07rAtqNqOfimO_MYDL62NnCIWolm2veaenCo3cCbcOkn_QIVRUkx-tRlnEkNVk82L6SM6z5lQ0pQ95YddD5ndhh3MrrIqRm8AtRyr7vyn1GyVj4vooEbojEa1RyAhnBsaEnQZ0pC_K8b6OWG63y2ZNREB6C0dkfjMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/893a539e51.mp4?token=DccBK-q8vuSuN0fXhpR-Az18sImDRH98jZq4xLUDTkY1LLJyY-ioru0BjKipeeOJwQEyuCXW5UWGAsxMqkoQcNY2wsCN63kuuqMRvCPSHkuIrQ10r6pj0McoDncmRUhw4rV_VB4MldwsFs-ytPwSQbTYahzVuzMFY8GjKCpmvwseXKdX-9TP07rAtqNqOfimO_MYDL62NnCIWolm2veaenCo3cCbcOkn_QIVRUkx-tRlnEkNVk82L6SM6z5lQ0pQ95YddD5ndhh3MrrIqRm8AtRyr7vyn1GyVj4vooEbojEa1RyAhnBsaEnQZ0pC_K8b6OWG63y2ZNREB6C0dkfjMzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی ونس:
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، این تصمیم با خودشان است.
اما ما قرار نیست ۱۵۰ هزار نیروی زمینی برای تغییر رژیم اعزام کنیم، مگر اینکه خودِ مردم در آنجا بخواهند به چنین نتیجه‌ای برسند.
البته ما در هر صورت قصد اعزام نیرو نداریم، اما پیشنهادِ اعزام نیرو عملاً به این معناست که ارتش آمریکا باید کار را برای مردم ایران انجام دهد.
ما دیگر دنبال چنین کارهایی نیستیم؛ واقعاً نیستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/134541" target="_blank">📅 23:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134540">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
فوری/ترامپ: ایرانی‌ها خواهان برگزاری جلسه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/134540" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134539">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
فوری/ترامپ در مورد ایران:
من می‌توانم به شما بگویم که آنها می‌خواهند یک توافق انجام دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/134539" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134538">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383751b9ae.mp4?token=vKpGUPAkDGdZcgJxtZrghfsbzrg35Y0uI_MHx0UPNK9B_mEblekRRQ3OgPbOyeivslDBNjn-NJHWXAzHCckjACuZjGJ_0ZApJlsYRc4Y_JbTe6CcK2-9wjQ7AQyEnd0Feu-jxnDwJ6vJ4slpo419xlhIGeWwXDQleV34Pb0CzUpsqIIj-ktqOsHU2xMwp7vzkQQ72R-q5ZWQJvPPsAnDGLp7o4nmncZYA1MOOKr4ewBZfaGalO-N8ZJiPRbYTaa41OnzCiHKFDjDIBjNKlp7N2eIXBIVSHzZLQ-8zYHiG6YILensWUJoQN3g00nsWkB1xgZ29hkfzc-puL9SAVq8zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383751b9ae.mp4?token=vKpGUPAkDGdZcgJxtZrghfsbzrg35Y0uI_MHx0UPNK9B_mEblekRRQ3OgPbOyeivslDBNjn-NJHWXAzHCckjACuZjGJ_0ZApJlsYRc4Y_JbTe6CcK2-9wjQ7AQyEnd0Feu-jxnDwJ6vJ4slpo419xlhIGeWwXDQleV34Pb0CzUpsqIIj-ktqOsHU2xMwp7vzkQQ72R-q5ZWQJvPPsAnDGLp7o4nmncZYA1MOOKr4ewBZfaGalO-N8ZJiPRbYTaa41OnzCiHKFDjDIBjNKlp7N2eIXBIVSHzZLQ-8zYHiG6YILensWUJoQN3g00nsWkB1xgZ29hkfzc-puL9SAVq8zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فاکس نیوز:
چهره شما از این پس روی سکه حک خواهد شد...
🔴
پرزیدنت ترامپ
: من بسیار مفتخرم. عکس بامزه‌ای است. عکس بدی نیست. بسیار غیرمعمول بود، اما من به خاطر آن افتخار کردم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/134538" target="_blank">📅 22:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134537">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
انفجار در بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/134537" target="_blank">📅 22:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134536">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
موج حملات ایران به آمریکا در این روزها خیلی کم شده و دلیلش نامشخصه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/134536" target="_blank">📅 22:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134535">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
چندین انفجار دیگه در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/134535" target="_blank">📅 22:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134534">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
فوری/اهواز رو دارن بدجور میزنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/134534" target="_blank">📅 22:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134533">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXseAEonHq9i33dgV49Lc3ZJU4vdDpLnLVxmRr-MRHfTeH5eklbBy2niq594-moJyQtjs-mRNUN5ZaDdA42lGym7SMGCiM3gJqdX2vpb-aKym_K_7z3LvivgQR_t_gNJhQUwkVl9LNeeBffj2gIJIh-s2yUSsnHZz0MrA_IzKIqQCl6r_ZgPhF_ylIUK8ltuyE9nJRT5y_P628jI5wHlySsMOpc_EvM1ILn-3iH7aWOPwHT4lS0n604MXwXJA4HaSFe4w78yKc1wkJFZ0cDgtSLbxlxNBwthDE2e8U8wxsaWIepsmb-ZT86vgtnIPp_d-vRfP7TjTfZXg2fjvp4ICQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده:
ساعت ۳ بعدازظهر به وقت شرقی، نیروهای ایالات متحده امروز موج دوم حملات را علیه ایران آغاز کردند.
این حملات به توانایی‌های نظامی ایران که برای تهدید کشتی‌هایی که آزادانه از تنگه هرمز عبور می‌کنند، استفاده می‌شوند، هدف قرار گرفته‌اند؛ تنگه‌ای بین‌المللی که برای تجارت جهانی حیاتی است.
ارتش ایالات متحده در پی دستور فرمانده کل قوا، ایران را پاسخگو می‌داند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/134533" target="_blank">📅 22:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134532">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
گویا لشکر 92 زرهی اهواز رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/134532" target="_blank">📅 22:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134531">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
چندین انفجار شدید در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/134531" target="_blank">📅 22:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134530">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔴
فوری/انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/134530" target="_blank">📅 22:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134529">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
فوری/شلیک موشک از کویت به ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/134529" target="_blank">📅 22:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134528">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
مقام آمریکایی:
حملات اخیر آمریکا به ایران، گزینه‌های احتمالی برای تشدید تنش‌ها توسط آمریکا را تقویت می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134528" target="_blank">📅 22:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134527">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134527" target="_blank">📅 22:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134526">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری/هاآرتص: ایران بیش از 100 موشک سجیل با کلاهک بارشی را روی اسرائیل قفل کرده و منتظر جرقه است که حملات را شروع کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134526" target="_blank">📅 22:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134525">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3U3l1aoGDqoMN7SipQy7SjlGOdy5qF58tK6z3uZRyC8kOJI0B3NsUUfmB6ie2Rvle4vRbOU6-fxwv8SUpPR-iqABfEcmeMDYamr8kSQMmlAEY55gH0jD2yfeLMHe7UWI3PzGCTW-Saixxd5GaqUQuznLPEawP8-2l6EzGq9g0rHHR5YqemfTIuc04u3f7s1NxNUo-4A76gk8PCGi2W3Ni6SaD5tUxREBsqGjYzqd8xQjqk--_dGF_GpF5b-RC_RjMBJriedqvlqSmJahyyuvcToHIYnXOqKraFoTJjSR8oBZSWbKMIMj9WrTif6B4okgztDb1lfMlErzZnv7XOKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمااااااااااااام
😐
هوادار معروف آرژانتینی بازم تو استادیوم لباسش درآورد تا به بازیکنا روحیه بده
😐
◀️
◀️
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134525" target="_blank">📅 22:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134523">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1x8BLk6pmIVGNaJ10c3a7yxYJlXghgQOY_MUv-6PxlATlSHfiA8Iq8l3a4qxKX9bHJgDBWBL5-wIp0PNuNadZLbYqSBhXATPj4aUduwTDSLnG7Z47xx3ommeYEMxAtEDcnPl2uDdKYX7LOF7SN_04oe1LYsymw-2VZNHtpNqMm4K__YxoiPATrZUR9eUw-wiCy_xCRvMjgpQOTeq7eO_A9PQOnTtN6dMuptK--bts8EHQXjXVU6EpoAfw3qUfwvel1UIrXq1bLxPlXKnmpPCXwwRTOPUp-1Tx-Wwgyrg7pZ0kxuNu7MeZcW_C602zXmw2ByTLS6GPUIE3eNT_dzhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3NssZ8YHiMHBgMQHmit0Sh_IJghHm9FUXbmQ6PIBkCf-f3QmXbd0RVIh32GxVZCvfAR4gCe2J6P6qEpTaW5sskfeYYYZrMyAAI8BqFqT0eUNsCH_uGzzMLVuQOJMHT_MKaCJu6bkVc7zOHWtjauqd6WKZRjcZn8vQZco1YvgmTQncdHL3O2jNGl8T93hD4TEyxTrIsIiwe4rZs15pC28_NY35Z_zWbjCIF7Y_1SBP8T5WAh1vZUwBU-MebnFXYqEHg6v00NUnXGJOFKo8vQ2VjMxJnB2nplW-5sGtz702V8f5CLxalkwuFWxEm8J5o9EK1ojknq7WRBt7YcA5wEhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🏟
ترکیب‌
🇦🇷
آرژانتین
🆚
انگلیس
🇬🇧
@AloSport</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/134523" target="_blank">📅 22:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134522">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
آژیرهای هشدار در کنسولگری آمریکا در اربیل همچنان فعال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/134522" target="_blank">📅 22:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134521">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
شرکت برق: مردم نگران نباشن، اول میگیم بعد قطع میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134521" target="_blank">📅 22:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134520">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQLf3O_ZaIKnga9_ryEob_Me5Qspj0VYrpDg2V8rzpSlbuVayABL9vZjRqrdd9pZvzBKWd4DcdRi07ZUTcE9YeNwlepHmxbgzHnQEQcEktDSp-HwCsYulhPd5N6xQjch_00adGA8uubiTIuwAGTstzo5yAFC8sabBSiLKoezD-b7eqpliY828nsJJR2SWRVKjeYzCbsG_BQ52XpuX2LH9yF2ZGThaZ-P5OlFfU3B7jnnMC-ge4tsPdBbdl56aUP4bIKHBXlzhuGx2cBVZskJc_IsFBCRL4we7-jDAjmNo93xWuIn1-PFQKkQ49qfzIU4Cd-79YVFA7DaMCiurpdr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کریم باقری :
اگه بیرانوند گفته باید برای بازیکنای تیم ملی مجسمه بسازن ، خودش بگه یه مجسمه براش بسازن ببره خونه.
🔴
علی دایی:
نگو بیرانوند بگو آقای دکتر بیرانوند
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/134520" target="_blank">📅 22:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134519">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">🎙
علی دایی :
دوست دارم مسی به فینال برسه ، ولی اونجا به اسپانیا ببازه.
🔻
علی دایی :
ما جام جهانی رو اونجایی از دست دادیم که سردار آزمون رو به تیم ملی دعوت نکردیم.
@AloSport</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/134519" target="_blank">📅 22:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134518">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e4434e0e.mp4?token=BQx0udBeXxGcRudeCAjGGsWC6u1taume3ueTSzGUFOhhbrF1bCWyI1VwPXeTTmuHgaiu-zyd3sSusMuqLi0IYhZlN4k5OVzXvba2yoJpcP8dV_dC-1PX8SxxGDuzS9Q1Jnps1WSLI2UhgFxuxGX-quSIcUIASoqnzOh0tV6BwhoKZRTrZGX1hRuMSUbNMAl-2Hq9cU9whgJBJs9KiRuCpm5lMeT_R75bwAftE2u0FYFCNIJNynLTncHGDjx-4gE9iRBLFRAQsusPOuFMsESqO8MP8xNzP7zLSKMYbKRH8wpH7SsuZTrZ8lmu2Rb0P17YT3QvD20bmCjr7RR8Yj5MEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e4434e0e.mp4?token=BQx0udBeXxGcRudeCAjGGsWC6u1taume3ueTSzGUFOhhbrF1bCWyI1VwPXeTTmuHgaiu-zyd3sSusMuqLi0IYhZlN4k5OVzXvba2yoJpcP8dV_dC-1PX8SxxGDuzS9Q1Jnps1WSLI2UhgFxuxGX-quSIcUIASoqnzOh0tV6BwhoKZRTrZGX1hRuMSUbNMAl-2Hq9cU9whgJBJs9KiRuCpm5lMeT_R75bwAftE2u0FYFCNIJNynLTncHGDjx-4gE9iRBLFRAQsusPOuFMsESqO8MP8xNzP7zLSKMYbKRH8wpH7SsuZTrZ8lmu2Rb0P17YT3QvD20bmCjr7RR8Yj5MEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما تو پخش شبکه افق داره آموزش کار با اسلحه رو به مردم یاد میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/134518" target="_blank">📅 22:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134517">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ترامپ: بهتر است ایرانی‌ها رفتار خود را اصلاح کنند؛ من تعیین ضرب‌الاجل را دوست ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/alonews/134517" target="_blank">📅 22:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134514">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd59a07cb6.mp4?token=ZY9wykKy-73RIbVMSQxegvzTss12MfSqoKIR-CJC0Qwyqchi09mOrY0Y7ONAawc1gERfddSSxlmiyXh-aY6MjF54VAws-C-Oinj9eVa-VjoJL86Rqqq_IMroCovpHHgixBR8bvx8YVjPiJA2NYJWUmhqDUkJTOuP27TbM4VRxnSsMDtvJH17L1F6we2dsA330JvfMSoj4v8tN52mxZ59Fs3oniJMgSaZKHG7Fz1SLo7K_LgN2MQtF5lpCb2S8p804vhBIfJX5_xb5i97jx5dM0kYyv-lo_4D1FCfM2eE7yScDKw21s6U5g5wS1o2XBevQBlUWf1uKX8GnaADUetGLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd59a07cb6.mp4?token=ZY9wykKy-73RIbVMSQxegvzTss12MfSqoKIR-CJC0Qwyqchi09mOrY0Y7ONAawc1gERfddSSxlmiyXh-aY6MjF54VAws-C-Oinj9eVa-VjoJL86Rqqq_IMroCovpHHgixBR8bvx8YVjPiJA2NYJWUmhqDUkJTOuP27TbM4VRxnSsMDtvJH17L1F6we2dsA330JvfMSoj4v8tN52mxZ59Fs3oniJMgSaZKHG7Fz1SLo7K_LgN2MQtF5lpCb2S8p804vhBIfJX5_xb5i97jx5dM0kYyv-lo_4D1FCfM2eE7yScDKw21s6U5g5wS1o2XBevQBlUWf1uKX8GnaADUetGLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پدافند کنسولگری آمریکا در اربیل عراق در حال فعالیت برای رهگیری پهباد های شلیک شده از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/134514" target="_blank">📅 22:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134513">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
جی دی ونس: برخی از وزیران اسرائیلی خواستار ادامهٔ جنگ به‌صورت نامحدود هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134513" target="_blank">📅 22:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134512">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e103349621.mp4?token=eunJQEPTUJ79GCsmxHB9tN9QabuPBXPYfiwAebridzunUC1me2FJkFntW5g1ZsmDAdATX1zspjcxH_0ZNZOBSDpTklSuJxB0ZlKtVkvVH2WZDcYhybar45CfV15sqIebVCn5_PQBrQlPc_n3r1DqyWiZbpIVxrJDPf-XPiBT30C4YjdUg-ukYBJvlFkct0iMJzN2h2i9ovzeFYX9-a691Rl-W8iMJcm8ttV0NNhvQ7OF9tsVYWSa7qsTA_QZUtZG0vnKvd6nXTRkmPpPff9YBOQgU1f5g9_Mka9TxuPvEFS3OwQp4XVOa3kN0TywrAwC7H32NMeENfuth_ya8UA1MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e103349621.mp4?token=eunJQEPTUJ79GCsmxHB9tN9QabuPBXPYfiwAebridzunUC1me2FJkFntW5g1ZsmDAdATX1zspjcxH_0ZNZOBSDpTklSuJxB0ZlKtVkvVH2WZDcYhybar45CfV15sqIebVCn5_PQBrQlPc_n3r1DqyWiZbpIVxrJDPf-XPiBT30C4YjdUg-ukYBJvlFkct0iMJzN2h2i9ovzeFYX9-a691Rl-W8iMJcm8ttV0NNhvQ7OF9tsVYWSa7qsTA_QZUtZG0vnKvd6nXTRkmPpPff9YBOQgU1f5g9_Mka9TxuPvEFS3OwQp4XVOa3kN0TywrAwC7H32NMeENfuth_ya8UA1MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دقیقاً همین عن‌مغزها ایران رو به این روز انداختن؛ حرام‌زاده‌هایی که فکر می‌کنن اگه چهار تا کلمه عربی بلغور کنن، سؤال اصلی رو جواب ندن و پشت شعار و توجیه قایم بشن، یعنی عرضه اداره کشور دارن.
🔴
یه مشت آدم با سواد صفر و ادعای صد، که هر فاجعه‌ای می‌شه فوری می‌گن کار دشمن و تروریست‌ها بوده. خب حرام زاده، پس نقش تو وسط این همه بدبختی چیه؟ تو که همه‌چیز دستته، بودجه دستته، اسلحه دستته، رسانه دستته، زندان دستته، تصمیم دستته، پس چرا هر خرابی و نکبتی که پیش میاد، یهو هیچ‌کاره می‌شی؟
🔴
کشور رو به خاک سیاه نشوندین، مردم رو فقیر کردین، جوون‌ها رو فراری دادین، زندگی رو از خانواده‌ها گرفتین، بعد هنوز با وقاحت طلبکار هم هستین. نه جواب درست دارین، نه عرضه مدیریت دارین، نه ذره‌ای شرف سیاسی که مسئولیت خرابکاری‌هاتون رو قبول کنین.
🔴
اگه نمی‌تونین کشور رو بچرخونین، اگه هر بحران رو با دروغ، تهدید، سرکوب و مظلوم‌نمایی جمع می‌کنین، پس این خاک مال شما نیست. تحویل مردم بدین و گورتون رو از این کشور گم کنین.
🤔
ایران ملک شخصی شما نیست که با جهل، توهم، شعار و بی‌عرضگی نابودش کنین. این مردم صاحب این خاکن؛ نه شماهایی که پشت دین و امنیت قایم شدین و هر روز یک زخم تازه به این کشور می‌زنین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/134512" target="_blank">📅 21:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134511">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
گزارش الجزيرة: پدافند هوایی، سه پهپاد را در اطراف کنسولگری آمریکا در اربیل مورد هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/134511" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134509">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f33a9d4e.mp4?token=OwWUnu-6NUGv2GRf9e7zU5eQpG8Pos7YibCpoDNPGs5ab7aZyDlFuIEJ8QHnjA_-oas0QvNC8eopeIBtDrqL3HozNHSnUbj_cuKN5ON5ahMG16eZ0LH9xv9uhQ6QX4TldZLXKZcYrWwo6hWKNLg6pCVgoJF1sbaOP77QceBzlkjzAqI9O3ndFGlHLy0k-nD269NqQuW3wYqQ_AE7NX7EWEZc-nAPUXctKKM2jetFqwFGr1LQSSRGDJNcenWAHluWA0rPqWf7Ux7D5lRh3F9cHqTZTf4ZavHfbsLR23Ev9DeiNKyU0_VS8iMMTphtJlqCj5niEfsqOSiYPisLSFerqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f33a9d4e.mp4?token=OwWUnu-6NUGv2GRf9e7zU5eQpG8Pos7YibCpoDNPGs5ab7aZyDlFuIEJ8QHnjA_-oas0QvNC8eopeIBtDrqL3HozNHSnUbj_cuKN5ON5ahMG16eZ0LH9xv9uhQ6QX4TldZLXKZcYrWwo6hWKNLg6pCVgoJF1sbaOP77QceBzlkjzAqI9O3ndFGlHLy0k-nD269NqQuW3wYqQ_AE7NX7EWEZc-nAPUXctKKM2jetFqwFGr1LQSSRGDJNcenWAHluWA0rPqWf7Ux7D5lRh3F9cHqTZTf4ZavHfbsLR23Ev9DeiNKyU0_VS8iMMTphtJlqCj5niEfsqOSiYPisLSFerqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسمان اربیل لحظاتی قبل
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134509" target="_blank">📅 21:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134508">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
گزارش انفجار بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/134508" target="_blank">📅 21:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134507">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1486415d12.mp4?token=BNLtWzx4Ixh0G0MY2p_Yax9blePwJORwsN2uabRFkoU7F3GBcnOq_dhlrUTtVKjuevwLpuupwtlQeCZpfnFkbHHwZEM0VCOq-nUlJymtVWNPSMTM4uYatX9LNsDTjB4ulkxz8jlJ2qeQthft7KBmTRqH2mR6S_xb8uOwoxrLLdMaVpvuvBXRopRJgbtH5N5p6cnHA21eguM83XDt3ZwCFeUE3G0GWFDL8tHmEkchg_MIym3BSdQWXOWlEQyUS7mVrdjy5D9IfW_6Az7SZOxlEBaKq9z2K3o6jfMJL4RRuahJeXnwxyFp2L4EkNX3h5ooNGLuNYjFO_wttOZQ9QZNZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1486415d12.mp4?token=BNLtWzx4Ixh0G0MY2p_Yax9blePwJORwsN2uabRFkoU7F3GBcnOq_dhlrUTtVKjuevwLpuupwtlQeCZpfnFkbHHwZEM0VCOq-nUlJymtVWNPSMTM4uYatX9LNsDTjB4ulkxz8jlJ2qeQthft7KBmTRqH2mR6S_xb8uOwoxrLLdMaVpvuvBXRopRJgbtH5N5p6cnHA21eguM83XDt3ZwCFeUE3G0GWFDL8tHmEkchg_MIym3BSdQWXOWlEQyUS7mVrdjy5D9IfW_6Az7SZOxlEBaKq9z2K3o6jfMJL4RRuahJeXnwxyFp2L4EkNX3h5ooNGLuNYjFO_wttOZQ9QZNZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حمله پهبادهای ایرانی به اربیل به مراکز کردهای مخالف
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/134507" target="_blank">📅 21:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134506">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c22bbbdae.mp4?token=fDVxiCw9xwwbDDyELuyXWPuy5TCRfD8l3_43df0MGoR6Z_zvLqWf7bGP_WwyJpy7T9eK1ZZfC0r8XiarOsT56A5PZAoaVOwpCHUjD3bJlLmKZtpf2-9zcftl7U7nqFdnZoDyAFvnlHQR_zlFS2bgJ9X7y9jyC8q1nWJpI6MjJzJJ_laWIw3-lH8iPoZmy2fo6di9yMHhhYtIft2Y88NsVJUWJwj0Glzwu4WMI2SGfgpiJvpN_D5lSe3IftL1e_NoGocbp3G_CI68ybQE6C3JW9HdkQ6J9EijDsFTiOS8hbn86z-9SWyJ38_qEGFGTFDaWz9UJSfsaqSXpdzKn2s0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c22bbbdae.mp4?token=fDVxiCw9xwwbDDyELuyXWPuy5TCRfD8l3_43df0MGoR6Z_zvLqWf7bGP_WwyJpy7T9eK1ZZfC0r8XiarOsT56A5PZAoaVOwpCHUjD3bJlLmKZtpf2-9zcftl7U7nqFdnZoDyAFvnlHQR_zlFS2bgJ9X7y9jyC8q1nWJpI6MjJzJJ_laWIw3-lH8iPoZmy2fo6di9yMHhhYtIft2Y88NsVJUWJwj0Glzwu4WMI2SGfgpiJvpN_D5lSe3IftL1e_NoGocbp3G_CI68ybQE6C3JW9HdkQ6J9EijDsFTiOS8hbn86z-9SWyJ38_qEGFGTFDaWz9UJSfsaqSXpdzKn2s0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نیرو: با مشترکان پرمصرف برق برخورد می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134506" target="_blank">📅 21:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134505">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
منابع عربی: چندین صدای انفجار مجددا در اربیل عراق شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134505" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134504">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/slhuXkaIJhd21Zcv5M0vtsxnjRatmFEzFUjbJaDB4QxqPfBcejmfuFD_DMjtBL2j9bX7NFna6SznJJRwOdBA_9gijvEY62-2qUwgkSWDEgkKq9aOhcRyEFWXiXmGONl-WWj9KTPOFf_e3Jqo9OnXJnYqVC_3QNEsAYwvqtC9-ZQTVqF8H2ENuZQVXiRpljInlI70YHt3AJgKvxuB35aYG_hZ2f9oB_R3O9h856qWdKegc1vzawTZ4BdYYYhDAMPQJZAcJ7IkMocxP7vgMmEDC4SQTWbansA9NNVsog4eGSR_JkhAGi7Q_XggiLAbdQAxvfkcN-VEsYSi--f0_7Qwow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکی از مقام‌های طالبان که خودش 63 ساله بوده، یه دختر 14 ساله به اسم نازگل رو میخره و باهاش ازدواج می‌کنه.
و اما بعد از چند روز، این دختر معصوم رو خفه می‌کنه و به قتل میرسونه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134504" target="_blank">📅 21:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134503">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
فوری / فاکس نیوز به نقل از ترامپ : هفته آینده حملات به ایران گسترش پیدا می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134503" target="_blank">📅 21:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134502">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
اینترنتتون ضعیف شده ؟
👍
👎
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134502" target="_blank">📅 21:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134501">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
قالیباف: به مردم جنوب کشورم که این روزها در خط مقدم جبهه قرار دارند، می‌گویم که از ابتدای جوانی دوشادوش شما خواهران و برادران عزیزم اسلحه به دوش گرفتم و جنگیدم، شما عزیز جان ایران هستید، جان ما هزار بار فدای شما، در مهم‌ترین سال‌های جوانی من و خانواده‌ام پای سفره‌های مهمان‌نوازی شما در مناطق عملیاتی جنوب نمک گیر شده‌ایم، گرمای عشق و محبت شما به هموطنان خود و به ایران را هرگز فراموش نمی‌کنم.
🔴
بدانید که ما سرمان برود، پای قولمان هستیم، شاهرگمان را برای دفاع از این مملکت گرو گذاشته ایم. به فضل و منت خدا بدانید که پیروزی ایران عزیز نزدیک است و مقاومت تاریخی شما ماندگار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134501" target="_blank">📅 21:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134500">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obxLfUvoUiHWqJ3x7lTPuzwhWtl-a5Znqp82wAs7ehuX59wehIaKHlYg4ouWadtC3UyyslER7VyJfmEvk8VJHZhnAysEdthazYI0fVDGl-D3-spW62PlSxFUFIU0GGgtM6e0mrJ7T4jkQ1AiOn45DQ4CclQCJGh_zaFClLbxTZ3OohjwvMwbz86wNOn9IKNvzN7bSTO7jNzuRZNpL82P1WM5yK3ocqUCZvB5mfE58BlpJtvzVqK4IotXMWW8IpcdSDc6wKRpim7Z-xtGfoj1-ng4GZ47KeY3iLwoDxvaGTavdwUzyquoApUM3R_SdWaYjoe1Zy0s9EbclvyalnOiaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ایران را نه با خط‌کش جغرافیا می‌توان برید و نه با واژه‌ها می‌توان تکه‌تکه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/134500" target="_blank">📅 21:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134499">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
معاون رئیس‌جمهور آمریکا، ونس: ما قصد نداریم نیروهای زمینی را برای تغییر رژیم به منطقه اعزام کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134499" target="_blank">📅 21:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134498">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
قالیباف: مذاکره در این مقطع همان‌گونه که بارها اعلام کرده‌ام معادل سازش نیست، بلکه در کنار جنگ،  بخشی از راهبرد مقاومت و صیانت از منافع ملی است.
🔴
این هماهنگی و استفاده همه‌جانبه از ابزارهای دیپلماسی و دفاعی، برای حفظ ایران عزیز نه تنها یک وظیفه بلکه یک ضرورت اجتناب‌ناپذیر است.
🔴
جداسازی و انتخاب یکی از این دو روش  به‌عنوان تنها راه حل، خطای راهبردی است.
🔴
ما در جنگی پیچیده با بزرگ‌ترین قدرت مادی جهان مواجه هستیم و در این جنگ افتخارات بزرگی کسب کردیم؛ پس باید فکر و عمل ما همان‌قدر بزرگ، پیچیده و مقاوم باشد.
🔴
این مثال را می‌توان در مورد  لبنان، رفع تحریم‌ها، آینده پایگاه‌های آمریکا در منطقه و انتقام وخونخواهی رهبر و سایر شهدای این دو جنگ تحمیلی هم تسری داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/134498" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134497">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY5E2sGLxExHPvU5Eap6B8I5TSjjVWVHCBfWU4E3GNtu-y8mXJEwfX88FKTyx9tqzrwpptSCQJ4h5XINYjBazFeigUu8lcBiNVw2q8pY6gTFu4eDvZN6FH5HWuu7Pd9eg7VTS4kgh06FoMRMKu-cgKptSqQarWifBPp5jgZSBG_pEbapGvJ9tiG6ForyzD7Esbw9UMkE2vcbL2T_ahX92HVq6dbolyhM7ckpgI86hEUbGJikQ8DoyD3UtvA08tr_sslA1_W7V71bU6TQgy2-tB_S12a0M6ti8y49xGM4U5d99iekULGFb-QOPP8FEM4rRtm1UeIXdGP41-f01aVW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیرنویس شبکه خبر :‌ وزارت آموزش و پرورش از برنامه ریزی کامل برای امنیت حوزه های امتحانی خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/134497" target="_blank">📅 21:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134496">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
قالیباف: ما باید بتوانیم بین دو روش نظامی و دیپلماسی، هماهنگی ایجاد کنیم و نباید از جنگ یا مذاکره هراسی داشته باشیم؛ جنگ و مذاکره دو  روش حفظ منافع ملی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/134496" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
قالیبلف: با شروع جنگ تحمیلی سوم در اسفند ماه، نیروهای مسلح ما کنترل خود را بر تنگه اعمال کردند.
🔴
در طول مذاکرات نیز ایستادگی و ترتیبات ایرانی تنگه هرمز را در بند ۵ تفاهم‌نامه تثبیت کردیم و آن را اهرمی برای اجرای ۴ بند دیگر ستانده‌های خود، از تفاهم‌نامه قرار دادیم.
🔴
حالا هم که به مرحله اجرای تفاهم‌نامه رسیدیم،
آمریکا که به لحاظ حقوقی و دیپلماسی دستش خالی است، می‌خواهد با زور ترتیبات ایرانی را کم ‌اثر کند، ولی ما بر پایه دستاوردی که در تفاهم‌نامه به دست آوردیم، باید بایستیم تا حقوق ملت محقق شود.
🔴
دشمن برای جبران شکست خود فشار وارد می کند ولی ایران با اتکا بر قدرت خود اجازه تحمیل اراده دشمن را نخواهد داد.
🔴
ما بر خلاف جنگ ۱۲ روزه، به درستی در جنگ ۴۰ روزه تنگه هرمز را بستیم چرا که باعث ناامنی و به خطر افتادن امنیت ملی ما شده بود. امروز هم امنیت ملی ما در حفظ «ترتیبات ایرانی» بر تنگه هرمز و عبور و مرور حداکثری ایمن و بی‌ضرر کشتی‌های تجاری از این آبراهه است تا برای ایران امنیت‌ساز شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134495" target="_blank">📅 21:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134494">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4HqCVsGvJZVdnNrSCScSsuwa89b_jPAXLrlskNoXPlcOqXvAH6BCSO41XhRVPaHPqO7zHrM7VQpNj_w-_QezFnLaaOkXj-eb4Fs179boROCc0L-jRuhDGOYPMaS6_XHpnRxMFQPIz6Tf8jNcrswbrQ5iwdJDyGEMrU9QLKuZJYG__q6zvgimh9CLz_2jmOJWYvD6YykiKNELrg0KXSaIrxAWWnfEjBk_QeOUTMSTT-wctJSghjGjMnhgvuFe1jCY_XpW6wDFbeOEi1994mh9NAVvEgqToRVNTK4vIbiahMtc5hUqO29Pj_a4NwN-LsmvSSpUaliDWifHd5YdbyndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت یوسف پزشکیان درباره موضوع انتقام
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/134494" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134493">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
قالیباف: تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد
🔴
اگر قرار باشد ایران از تفاهم‌نمامه انتفاع نبرد، دلیلی برای پایبندی به چنین تفاهمی نداریم
🔴
باید همواره آماده نبرد باشیم و در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134493" target="_blank">📅 21:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134492">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
قالیباف: نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد. لذا راهی جز تکیه بر توان خود و قوی شدن نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134492" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134491">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
قالیباف: آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/134491" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134490">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
قاليباف: ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134490" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134488">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLt-DhRabEGngxiz2pcjxGgXvUx68WpPEMrMEtMp1yELs6aYqB5hfITVzDRPpVGcw5Eq98nb-P7oBRhQjAn4kbXImH5DVNkADu2AjErWn-FQo0cU2MIzIymTG_tOLJNo353qFUrWcLw7sqQx8BYislK4QwXMtSt66tWTGP7PRGfYipwvA7qaeRS3S10yCUtc-IARuEKWDSf7aw-6qpckJgYM2SkSuC7Xo2HCNh-1JcAiUB1-AAin3_fJyGC5TEjGU94HAo4ukq4zxVbVUDzHJQAiDzHsHE8Ay8Q7acL3-u9zgcg90opWKnuRoFnQ_UQE_lJJ7a2vL4EtbYpQ02mG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFL39BXQ0b6BRrwmfvtqC9O5plI49P1lIlBeQXny7AreEJz6wv_zs9n_QfaLdz3-2wRM4_6R97VC-EEXII7tNDyBF5-op-L3bVxqVa549uz44GkX3HzoGLQcNYoHf39fCkqOIDoN_v8fH8rpXYRArsJQhNDUDDBfRqN1PnbDE_97SWyIMq4SBerHn5DFBwIOOqab6zMQU9v-SBciEbXX2s1R09iHJ-Auhhxsw0OCzi5Ef2hcTzX_6ImElWlgZ4hA6DcJ1w1m7lWhHhybicq2J0fKT8wDtjYyKg3Yd26thzmHpbgpqOqGvDX37uX0wHRVhCPoUjplZ_k0A5T51G8ZOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سیلو ای هویزه در بخش مرکزی که هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134488" target="_blank">📅 20:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134487">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
یک مقام ایرانی به المیادین: تهران پیامی خصوصی برای جی دی ونس، معاون رئیس جمهور ایالات متحده، ارسال کرده و در آن جارد کوشنر و استیو ویتکاف، فرستادگان ویژه، را به سوءاستفاده از اطلاعات محرمانه مذاکرات ایالات متحده و ایران برای منافع مالی و افشای اطلاعات حساس متهم کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134487" target="_blank">📅 20:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134486">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
صدای انفجار مهیب در هرتزلیا در شمال تل‌آویو
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134486" target="_blank">📅 20:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134485">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
گویا سامانه‌های پدافند هوایی یک پهپاد انتحاری یک‌طرفه به مدل FLM-136 LUCAS را در آسمان بندرعباس، سرنگون کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134485" target="_blank">📅 20:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134482">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VU9HWlpOrXW0M_Xzr2LB5G6-y5jHMS0YmaAD9VvaVw9cc_v-_9A-PR2Bk1V-uaJzAWlscHVYM0rm_3uWzwv8qzoTfpyPtWp9SlJj41jgEIPNqyPdztU3WBi6pC2Ih5JyGN_5gOG3mkJ8zVlpfmrwh6fvd38kLuXKX5wXjh7i3g9RuQbbCVlGGpZAr2oVIrWCoCt7tKQ3cZLLLAMTHC0cGj6hde_tftcLCre-Qp6JM5wrbi6XPeugX4MGq4V8oDl9iNJPgj1gK3TFT72yag-VcfUpH48RuKGY1SxXRDLjXQp2Z9UvMitZ5BvNZ1zxhNCc83NZL3_Y5XToWdFkJ4tYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qu8DefpiBhBcdsDbi97H5ilRnhvV3IJYqlyk2jt8zESF6Acgmh4Lj54yu_oG5sXjL1QUjSO6ZyOwCyOCyDeqWn7u5JcctG8oUwx6W37gjKTV4oJBbao0UCD-Xm6nyoHKk4XHUtTY3YXe4pdmU5hOEa6n4G_jH_SSuud2fwovLqq8jjGxs6C19MV9Ppdwhsbzlo8JvcICRRywysLKU3nEI4unaxQlPY4y_WSDl1lsQYppxONSqZS86txPCeZT-K0FjCii71Y8KS14JFnZCnV6HRMTU7KsPsFjGs5LIQhIG8dJh_IdjTf7vhUYgOayJanY19PNK17o_BsoWuf4BooqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOCLPNwAYasCo3AoXfjVjU3y1sCuk0pwbCpnItHQMVmQ50nsfPIWUBAeF7rlV7OI64kBAMc8hua-5Xj-E76zKpEPRYKuoivn4AHHUimXTI_kNfHTeC3tNvVZsKi4aVn0TI531gzxq2l851bp0cXB4IGRk5472pwUlF6Uj-yHpNZX88jw0jSv2DsEEGrurczzrRpR9k1eNOVtEcx83Klz-AbXPPgRKwlsSD3WIfD52VjONxIP4j4TgXUgNaFuYv8vvJkNo1SzrWrSBXHqj7UXPHzN_1ja5nuAJQCEcUEocJ8vcL-oUCUSjNnGdHDJglmsVUelF_qL_q4xR0IxnSaqxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
خبرگزاری فارس با انتشار تصاویر بالا مدعی شد:
انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
این پهپاد متجاوز ساعتی قبل با رهگیری و شلیک موفق سامانۀ پدافندی رزمندگان سپاه در بندرعباس منهدم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134482" target="_blank">📅 20:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134481">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/134481" target="_blank">📅 20:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134480">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9n6wMr8FeN40rUfYN-L_-Ja0mtAiQRxxMeu5cKj3jvxg-76MzYqJkzwoIH2xdF8F8wBL53iMvP1MOx-KoGLjJ56GqIGCk3BZq5dswmm46P9-Gv_AUHwszx53aq95r3Z_3-pJGZKk6yMvGBgddz6z7jGcZNOEo7jBQqm5LERTt5KMW3WL3HxDQGF6Q9K4Tf9spwn11ckZKO_6mHGv0xpylK2FTbnYX6gj7iPVoAm-mNm6hM6WK6BEdiLncE5g7NyqH-FCXzgBLxQSwIxdUNNXDOBLHds121G27oUsnTvazXtETE9kMzlOtHppgVR9Dc3-G7o1D0VWjjSqYAXOuyVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134480" target="_blank">📅 20:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134479">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری / صفحه امور کنسولی وزارت خارجه آمریکا در شبکه ایکس با صدور هشدار سطح چهار و بحرانی از تمام شهروندانش خواست، فوراً ایران، عراق، لبنان و یمن را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134479" target="_blank">📅 20:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134478">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
پروازهای شیراز – دبی پس از پنج ماه از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134478" target="_blank">📅 20:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134477">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ترامپ: یکی از بزرگترین نیروهای محرک آینده برای مشاغل، مراکز داده هستند. آن‌ها بزرگ، قوی، جسور و ماشین‌های پول‌سازی برای ایالتی هستند که در آن ساخته می‌شوند. کاتی هوکل، فرماندار، به دلایل سیاسی، تمام مراکز داده‌ای که در حال ساخت هستند یا قرار است در ایالت نیویورک ساخته شوند را لغو کرده است. این شرکت‌ها اکنون در آلاباما، فلوریدا، تگزاس، آریزونا و بسیاری از ایالت‌های دیگر جستجو می‌شوند. هم مالیات‌ها و هم میزان مشاغل به طلای مایع می‌رسند! ایالت نیویورک تصمیمی فاجعه‌بار گرفته است.
🔴
تمام این درآمد و سایر مزایا به ایالت‌های قرمز و برخی ایالت‌های آبی خواهند رفت، جایی که مراکز داده به عنوان گاوهای شیرده پول با مالیات‌های پایین‌تر و مشاغل بی‌سابقه جستجو می‌شوند. آن‌ها باید هزینه آب و برق خود را بپردازند و هر مازادی به ایالت و جامعه محلی بازمی‌گردد. مراکز داده پیروزی‌های عظیمی برای ایالت‌ها و جوامعی هستند که خوش‌شانس هستند و آن‌ها را به دست می‌آورند. نیویورک باید سیاست خود را فوراً تغییر دهد. نباید به دموکرات‌های رادیکال اجازه داد که باعث از دست دادن مراکز داده، هوش مصنوعی و تمام این فناوری‌های جدید باورنکردنی برای چین و سایر کشورها شوند! پرزیدنت دونالد جی. ترامپ
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134477" target="_blank">📅 20:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134476">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RrF1MNsX38pbB7TyopusK8MrXBfWTuVkLjdhyriK6mf-OLoAsG5iv2cdnUddS62cy925L64qlVFfwe8r7CyOWPmbaFFaklXpViskZoCmCDGlN7c8fnehbCFhbvbkJ8LY6y_VNyGth8J5_O_KSioQl7Jo0eDQEOgdJeIN0-HMKF_DsgGl2VST5v2p0Z4vM0t92Te5h7l4ttPUAFKEzYRIC37KeMPhXf9YvzH7D1iphNZVPxbf7eSs8sFEJt4muaxLO8vtTt9B-RnD8Ktkpgi7tVhwN_yP7vrcmFBWiFbUfywo9Q3PpeWyS4ncoRLoNni5ELs7xb5tMa7s14cvRx0wIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید در حال بررسی تمدید مجدد معافیت‌هایی است که به کشتی‌های خارجی اجازه می‌دهد کالاها را میان بنادر ایالات متحده جابه‌جا کنند.
🔴
این تصمیم در شرایطی مطرح می‌شود که تنش‌های تازه با جمهوری اسلامی ایران، نگرانی‌هایی را در مورد قیمت انرژی و اختلال در زنجیره تامین ایجاد کرده است.
🔴
خبرگزاری رویتر به نقل از منابع آگاه اعلام کرد دولت ترامپ در حال بررسی اعمال محدودیت‌های جغرافیایی برای کشتی‌های با پرچم خارجی است تا ضمن حفظ ابزاری که به کاهش فشارهای زنجیره تامین کمک کرده، به انتقادات گروه‌های صنعت دریایی و متحدان جمهوری‌خواه نیز پاسخ دهد. مقامات کاخ سفید به همراه وزارتخانه‌های انرژی، حمل‌ونقل و کشور اوایل هفته جاری برای بررسی این گزینه‌ها پیش از تصمیم‌گیری نهایی در پایان ماه ژوئیه تشکیل جلسه دادند.
🔴
یک مقام کاخ سفید در گفتگو با رویترز، با اشاره به اینکه معافیت فعلی تا ۱۶ اوت اعتبار دارد، تاکید کرد که هنوز تصمیمی درباره صدور سومین تمدید اتخاذ نشده است. او افزود که اقدام قاطع رئیس‌جمهور ترامپ در لغو موقت «قانون جونز» به جلوگیری از کمبود در زنجیره تامین سراسر کشور کمک کرده و دولت به طور منظم نحوه استفاده از این معافیت را رصد می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134476" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134475">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
انفجارهایی در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134475" target="_blank">📅 20:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134474">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
بلومبرگ: نفتکش‌های فوق‌بزرگ به‌طور فزاینده‌ای هدف حملات در تنگه هرمز قرار می‌گیرند
🔴
در ماه ژوئن، پنج مورد از نه حمله به کشتی‌های تجاری، علیه نفتکش‌های موسوم به «بسیار بزرگ» انجام شده
🔴
این نوع کشتی‌ها، ستون اصلی حمل نفت خاورمیانه به نقاط مختلف جهان به‌شمار می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134474" target="_blank">📅 20:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134473">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نیروی زمینی ارتش: پاسخ حمله آمریکا به ایرانشهر را خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134473" target="_blank">📅 19:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134472">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
انفجارهایی در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134472" target="_blank">📅 19:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134471">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / صدای انفجار در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134471" target="_blank">📅 19:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134470">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
کرملین: اوضاع خلیج‌فارس رو به وخامت است/ جهان نمی‌تواند نگران نباشد
🔴
پسکوف، سخنگوی کرملین: متاسفانه اوضاع در خلیج فارس به هیچ وجه پایدار نیست و بار دیگر وارد مرحله‌ای رو به وخامت شده است و این وضعیت نمی‌تواند نگرانی جهان را در پی نداشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134470" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134469">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
سی‌بی‌اس: ذخایر موشک‌های تاماهاوک پاتریوت و تاد آمریکا به شدت کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134469" target="_blank">📅 19:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134468">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران و روسیه خبر داد
🔴
وزارت خزانه‌داری آمریکا روز چهارشنبه چندین شخص و نهاد ایرانی و روسی به را به دلیل فعالیت‌های مرتبط با اشاعه تسلیحاتی به لیست تحریم‌های خود اضافه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134468" target="_blank">📅 19:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134467">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/moSn9qGzXxp4W2YmC4k7NfHVhfd5hYrfMGZyHEx6Fap9QfNpeQfgVatLnRVY8tLM3nvImHNMtCPuJQBO2xnEiVuPQlxWe00_hL4kQI-ArKHsr3iqUewOgHcplYTF_Jj_S30hh-NAvU-Nr0LNpSnnr44x9KYU3qKFML74-UqKjphfSbbqba_sb07wOWgqnOmbfe-8oWCb-VoLndqWL2yhIyiyd22spNfIGngowd0GkA9yR3UIeSnvMTO2XntpQ2VogjaPcfjp7gxBlg5eD_4q_z16s0hBlhw-3yZ1ZseX7-UsQg6UfROC7SpyC7T2tV002heivdRjlm2J_N0Bpnmkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ما به یک انبار ذخیره گندم در هویزه خوزستان حمله نکرده‌ایم ولی در عوض ایران به کشتی های حامل گندم در تنگه هرمز حمله می‌کند
🔴
ایران در مقابل، غیرنظامیان و کشتی‌های تجاری در حال عبور از تنگه هرمز و همچنین کشورهای همسایه حاشیه خلیج فارس را هدف قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134467" target="_blank">📅 19:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134466">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
بقائی:  فعلا برنامه ای برای مذاکره با آمریکا نداریم ، روی دفاع متمرکز هستیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134466" target="_blank">📅 19:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134465">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری / صدای انفجار در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134465" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134464">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بقائی: فعلا برنامه ای برای مذاکره با آمریکا نداریم و روی دفاع متمرکز هستیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134464" target="_blank">📅 19:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134463">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
موافقت شورای نگهبان با جلسات مجازی مجلس، در صورتی که جلسات به شکل حضوری در ساختمان مجلس از نظر هیئت رئیسه ممکن نباشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/134463" target="_blank">📅 19:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134462">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJjKYLfOsj6R2XfpYS4UwvbO21TrM9tx7vTnKKdqfCHBfukfRfGMFxGnpJ5Me5GBuFtKHIVBkMN9hRYU2lL4GoTivV-OfeJnNgMhx-j47F4EYC8FHprQE9P6RAJnxgZxN_161zyliIeCp9iz1Dq5ymkBTS3buHjqPdf75KjlqndKDuzujNqh747OpJ8Hi3zp_xYoCgogL8DGweIl2yufi580M1ZoNieRYSEoiOTt-DYcNkMcpBJKD4ctECQmArj9nFaEgWHCEUVrgQ6dHFIwyVk9f43ZxKSnOwYqC4sabrIDTjekYGFBQIZM7fDEwj55fNLw1B4lkYbbdY1lZvM6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
استوری حامد‌لک:
@AloSport</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134462" target="_blank">📅 19:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134461">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
خبری که تحت عنوان اعتصاب در چارسو دقایقی قبل منتشر شده مربوط به گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134461" target="_blank">📅 19:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134457">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران و روسیه خبر داد
🔴
وزارت خزانه‌داری آمریکا روز چهارشنبه چندین شخص و نهاد ایرانی و روسی به را به دلیل فعالیت‌های مرتبط با اشاعه تسلیحاتی به لیست تحریم‌های خود اضافه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134457" target="_blank">📅 19:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134456">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
رئیس ستاد ارتش عربستان با معاون فرمانده سنتکام دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134456" target="_blank">📅 19:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134455">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
فرودگاه بین‌المللی صنعاء به چرخه عمل بازگشت
🔴
وزیر حمل‌ونقل و امور عمومی یمن: فرودگاه بین‌المللی صنعاء پس از تکمیل تعمیرات ناشی از حملات هوایی ائتلاف سعودی، به‌طور کامل به چرخه پروازها بازگشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134455" target="_blank">📅 18:55 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
