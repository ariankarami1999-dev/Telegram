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
<img src="https://cdn4.telesco.pe/file/PuuXlDQuHGrAPWm3n3CeAy87C8QoK2ptUqdl95nZMZjLE2aQZbL56BKT6agc4_EunMgZZrr5XrSsfVnTn74xtisBqfy28kguvMRW9euvtwCgaE4LolbKTjHEV8uG1qvZtNxOtW1uU8fsVUctFGXbdrBH_MPXl9RQBY9ph0NEZPdz5pGn2jfiDQ1A3ndhwZiAgW44o-UPebWZUJbVzFNHu4Ash9SOPsKBzutyhy0Cv3cRn66nrMOnaT-YtSvMAp_co02blsTmDSlaRGLjcUbfo3XhwmIljG1eXPWUGeRktxQKP2GtSGdTN3I0Ot3n8VrvFcdHhNyPyD7Co2HHfItqDg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 19:58:23</div>
<hr>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5nttENIgEfiwZuj_Reb3t1GJDwvM9OmzGMHBQglcOzJZS7osKp6H4gyPbq8aVf3VEpPlaqdLFGdpugxzWYPC9xIqgHXk7NOM2GvcIyxrOrXfWlYv824aSDBRVOALtBo_-scHBs-rAD5iGr4Z6ZVgBzZNRT__f496MlvWQld8b7LXW_gCr64LhxfrHnvugcxUtiD0ZIIigvohWvnFiQ7lbpW_TxTVCcTxzq97jvA-I1pdz9Kb9NpGk_iDKZaEQJctakHwuXRsOEaNY17-tbUnipccH2djZz_TJwUgrr3mW7Njb8b-_CWxqHV5QeaVNyXImjUppOS-9gZlaeHFDuxAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rip09e5DCowT_2bgFM2V4mdcdlYvac-ZajIMtnS1p7qAA4rl37ZZjKlmHja6D4J-TFcOE3Ez_PNFEfOuoPs91wj9k54OW1JNDAFu-ZW7rNUA_3Bgh2FawlbEEYS8tqxo7cJY38PR_WJtmMCcfLV1wfZphVB3MZbocNKJ8086bPKPaZV4T5N0vzKpZRXSprtwa3OS_-fkWsPwv_e6aySm0AW9K1SVRf95N7vXfTYo0puM8tJqpuoXbi8jFGOmRLd3fZpBVewUKc4I3MPIX-TVCK4gpKjGdeL_VuH-qzYqGsVKKj7GCeHIkFpTSXWvY3p5AJ2OKZG1g3w4TYrTpu8BiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvKU02dxYTYH7ce3t7cDFcG3HV9e_NbL6ahNpiXGYwa8j-eq8FB0mqWk42AG50HpkT2MxxU208YVylXzsaAOBw4iP0oePiOaZYkSdOsxFPsVGPviVd-6AQP4pKhdL4CbqyQkX6WOlGuNzCc4q88zHIddaQ5jHXPwQIgnx1tatD4DR4ThilxwAL3O7q2wtVQoe1nBWO-0hW1CbTZUcgmTqOYPQHFh2IBg3vUGa1Q91jEQxPRjJIJ4Gi5WAR5n5nT93pPg8S9NSUZtsNkMmz_7Yqv6XN-PvGqjSK5UMxb1u8_cAO0tDqpjV5G9OBWT9Id5TdCwZXb0PM8G5841ebq-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
عراقچی : مذاکرات برای دستیابی به یک توافق دائمی با آمریکا، پیش از اجرای این بندهای تفاهم‌نامه آغاز نخواهد شد:
🔺
پایان جنگ در لبنان
🔺
رفع محاصره آمریکا
🔺
صدور معافیت‌های تحریمی از سوی آمریکا برای فروش نفت ایران
🔺
آزادسازی تمام دارایی‌های مسدودشده ایران</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNnpLhEXscABelH1di-uKvhA3Q--JovL62N-xbeEfSpMd9f26hJ9_j8mjoAwLEzHm1pLoKn8amllc6dvSDxfICAFsJrImqslXO_1t11vgUCoRK5_k2zNDS9VbkiiOdSTpzSK6Ysfpmg-A3un2eVIOwLQHI65pzGSGFg68EmWVla9KKSs9CUNtuemXJ8KL8xNFgv_tTTMYNEGcLYaq6_YcD5v6n4NsF066I9ujDyewD3ghgNnFP0aN89A3cgMsbA7QDBUoyzB4vfDn7X-xL3lj7x_JB-rnHhujVf-Sou0Wo3iSVN-Fwv9h8LXBThbOeXa1CmSbm-wC9_VFNGq0xEg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392eac3002.mp4?token=UDmcURaBvjar54HZ46_mDhU6PWIl4j6RJL_jPNQ18QnUiWoe2R2IQFlsub4u6w3I0gX7KzdFZYS6nWac5C9Wy-1yj9zDhvBVbFGIF5AGl6UGa4locrBk9KfciT20Gl1ZP8oghh42ocLO3dwZ9U68bvA-kTAyn333wdDWyNDO0_T0eirkA2r3f6GvWlbC3OxDv2qaM5_xn3YE5HbsjX9aKOpd4s1C7EDmdP0Dhz_a5JA-mLvf3YseR-8soFxpAG71_qtfRNT7c0yhv9ZNoqNAnRLXl8Om_B_H9X1ywiNH5CKchWDtxTEBcS2J_UEgrqauETHzqfQYomzxh1lb2cZqwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392eac3002.mp4?token=UDmcURaBvjar54HZ46_mDhU6PWIl4j6RJL_jPNQ18QnUiWoe2R2IQFlsub4u6w3I0gX7KzdFZYS6nWac5C9Wy-1yj9zDhvBVbFGIF5AGl6UGa4locrBk9KfciT20Gl1ZP8oghh42ocLO3dwZ9U68bvA-kTAyn333wdDWyNDO0_T0eirkA2r3f6GvWlbC3OxDv2qaM5_xn3YE5HbsjX9aKOpd4s1C7EDmdP0Dhz_a5JA-mLvf3YseR-8soFxpAG71_qtfRNT7c0yhv9ZNoqNAnRLXl8Om_B_H9X1ywiNH5CKchWDtxTEBcS2J_UEgrqauETHzqfQYomzxh1lb2cZqwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل :
توافق  برای آتش‌بسی هم اگر بوده در سطح سیاسی بوده، در بخش نظامی هیچ دستور جدیدی به ما داده نشده و ما همچنان
به حملات خود ادامه می‌دهیم.</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=XW4Gw6WK6IDsj9WWu7Vn9XSyDx-rSU5khNhnMKM5VinWd2NeIa7dU08Vc10RvPj3woq2JrCqQaJ2PjIP5LLFaF-bPZA-ARmXQepQrC7NZhxOxRtL3aiBXv_ijJCbIgYDg6keUoxUfz6HOX1fdmHfwZTQvaXby_NY9GFteArowaD28XEmh2T1Cls8SrbEJ6CoijlSLrYxgLvo8ZRULOcUf_jjVxPG2DhYy89vYf30P4RHcmYHM-3Xoo1OaIheNDJPQG5BDjnKSWpMSajXYe0FrY6kCs7SZ56vWzwB_5J1nGPjr0hdGRcbf5xi_2tAkccHhNWCyhWWmiXTuHdWCH-W1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=XW4Gw6WK6IDsj9WWu7Vn9XSyDx-rSU5khNhnMKM5VinWd2NeIa7dU08Vc10RvPj3woq2JrCqQaJ2PjIP5LLFaF-bPZA-ARmXQepQrC7NZhxOxRtL3aiBXv_ijJCbIgYDg6keUoxUfz6HOX1fdmHfwZTQvaXby_NY9GFteArowaD28XEmh2T1Cls8SrbEJ6CoijlSLrYxgLvo8ZRULOcUf_jjVxPG2DhYy89vYf30P4RHcmYHM-3Xoo1OaIheNDJPQG5BDjnKSWpMSajXYe0FrY6kCs7SZ56vWzwB_5J1nGPjr0hdGRcbf5xi_2tAkccHhNWCyhWWmiXTuHdWCH-W1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=hWuQ08SktoRtcmm4-U0smjz3XwiaUe6VmZD2hK-A0QYBmjTzKeNeQZA_4XJIQ-E6RRbn89pem7U1HvJBS5Uw1o9r9kYrCfhUmScddH4CzpmaDWH3IN9O34ip4NWemp9zv5DsHjgwhohHRfn9cqmkY5q4gx0izQjinlLIXH9IoGYb7j0zjFDW1kQtfuFrBGEPUIlBC3XeROu86IgrknbnMuv6LKI3I3h6aAdS9Rh9YbDVjWxs77bBWUNf4UvXjhq0ONv4-xPkXpuKw7M64vzRwZ_KhxZP84NkSBRfnE0R7mXLcKpBoZCtVjjhFvfhtjOW_v2WK4zR2g0M7YS3BBeNrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab675b39e.mp4?token=hWuQ08SktoRtcmm4-U0smjz3XwiaUe6VmZD2hK-A0QYBmjTzKeNeQZA_4XJIQ-E6RRbn89pem7U1HvJBS5Uw1o9r9kYrCfhUmScddH4CzpmaDWH3IN9O34ip4NWemp9zv5DsHjgwhohHRfn9cqmkY5q4gx0izQjinlLIXH9IoGYb7j0zjFDW1kQtfuFrBGEPUIlBC3XeROu86IgrknbnMuv6LKI3I3h6aAdS9Rh9YbDVjWxs77bBWUNf4UvXjhq0ONv4-xPkXpuKw7M64vzRwZ_KhxZP84NkSBRfnE0R7mXLcKpBoZCtVjjhFvfhtjOW_v2WK4zR2g0M7YS3BBeNrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گریز دسته جمعی مردم نبطیه
در جنوب لبنان،
صدا و سیمای جمهوری اسلامی
حملات اسرائیل را به طول زنده پخش می‌کند.</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=r201VltzuQbNkZvcfvayrEnAQmByDB7We05x4jOsQb_IBTmLcxYPeBW6lwn_xTVTUqm18wWB2AB2m18g4I3lozL_zRqw92ntuM2SDc_BM81bDrSMLcNR16HiWvrUeUQPOGIm-BLhuwP5NxHwYHbezldmpF5Q0ms2GgbrZQnmFXdSO3AoeGi3F2NV-tsEYvk7q_tHK_YTWgan34NBJfxaZiHxVn1RpXpVKblNxMuF23Tdr_Ho6qlnrgzB3F6PXKQBmbpwD5HI5qu6caFeadpdyQCOeJiSeqvj_4cr0VCW75YOMKonO8IWHt_nmQf0-oTyDyO0EC2jmz8noRcQ6LtY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=r201VltzuQbNkZvcfvayrEnAQmByDB7We05x4jOsQb_IBTmLcxYPeBW6lwn_xTVTUqm18wWB2AB2m18g4I3lozL_zRqw92ntuM2SDc_BM81bDrSMLcNR16HiWvrUeUQPOGIm-BLhuwP5NxHwYHbezldmpF5Q0ms2GgbrZQnmFXdSO3AoeGi3F2NV-tsEYvk7q_tHK_YTWgan34NBJfxaZiHxVn1RpXpVKblNxMuF23Tdr_Ho6qlnrgzB3F6PXKQBmbpwD5HI5qu6caFeadpdyQCOeJiSeqvj_4cr0VCW75YOMKonO8IWHt_nmQf0-oTyDyO0EC2jmz8noRcQ6LtY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPaWNmtAmIcVVdN4Np0n495OBUtBp9vIU7GVWkyrEQWYqz2mF5gTPAXWmIc3VcxwF_4WrwO0yaq_L480c2oWZJc98GZugjRtea2DOx7b1QANtDIZOb5BLXph5oZKyXvRAGnWVJvbayrcmCA64kpjVz-4GtqpGpN6iFhFRO7xl5pdDqni1F_iHS51fwtxoy-JqwxJDgPR08VuqFxJLo9N6Ha-SQUdsyXDb-EabemFUHVNxbTrcW1tCUdDlMtRltoAS9vMKoUxodAOveRSdOMaMK_VbMrbSk7kz85GlMPOUB2POTGCa1VgcNNeDywzGusdsD-_I3QH3w0yDvYbTPXkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY46CnIybLWW1mW8BLpKqVDtz-UJbIwI8fcqZWCh7qKT0nNaHvIkbcjgYtU1hgVWYeT7G0cT_U5BG5tC5ajfdQPUG-Z1igYe66X2Zf0jIsydyn7VXorg4GVtOt4T7E9V9IKbR-nxO4tNVW7AdIgNyNAMpzQ489PSUZeiB8zm76WDJ5yzyQlm3wfoJOJm-lk4si4qB-WXL9UgVcD-vTwjOB5swNl8OLh7Ws_Y1TleCt480vOWWfFMAdbL4GZHgEgBHtyPDBQkKQMv93Ii8pz_-FAQbUfCedf4T6NaZ-go3wrPVUfNzCdP7ApBqPyoBgjqKw7GU68kpD1bd3Je0msC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=nEXfeO5cBsfBxA9VrRX7j3hOAB4DrvPlMuaZjzViBSZs22oymuUh5uTB8xAGRrohHcED8XXQNsKVR2vdtWSPIEOPuEKmQf_umbWklh1Jvr_B-j-X7rUUEkiw9tSfM03niac01QgebpiMAwvB6zzdRAV-xCYgnK4E15hcXpDvYINcOn-jGF2RAY2mvbD1m1oYZwNO9RqI4hAnzGmL635dms_YY4I_uEcLv6hrDIgmEU0D0usg-yMKADG2-WWUFNjQlgOQ-epDKbRZcGYIbR9kfje23SiJ9yWfnDEM_8nwOTV6dCf2J2vZ-H9fLs5cistZ30uCVtvdFSqxGtyDvLGQtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1dd8a7483.mp4?token=nEXfeO5cBsfBxA9VrRX7j3hOAB4DrvPlMuaZjzViBSZs22oymuUh5uTB8xAGRrohHcED8XXQNsKVR2vdtWSPIEOPuEKmQf_umbWklh1Jvr_B-j-X7rUUEkiw9tSfM03niac01QgebpiMAwvB6zzdRAV-xCYgnK4E15hcXpDvYINcOn-jGF2RAY2mvbD1m1oYZwNO9RqI4hAnzGmL635dms_YY4I_uEcLv6hrDIgmEU0D0usg-yMKADG2-WWUFNjQlgOQ-epDKbRZcGYIbR9kfje23SiJ9yWfnDEM_8nwOTV6dCf2J2vZ-H9fLs5cistZ30uCVtvdFSqxGtyDvLGQtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنوب لبنان زیر حملات شدید اسرائیل
نتانیاهو دقایقی پیش: دستور من روشن است، اسرائیل حمله به سربازان یا خاک خود را تحمل نخواهد کرد و حزب‌الله بهای بسیار سنگینی برای این حملات خواهد پرداخت.
وزیر دفاع اسرايیل : به ۸۰ نقطه حمله کردیم.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh99LCTwYnsTyTnlqFnvtZzwY5LKBUs8tTka5xttXWkjoDPPNXgaJhEjTmSEquQmmpNVgGRZ5uF5wOXBghdcCF2X3I4e6LHGs5NXb5-uyrYaTspnsLUPYultGCPBacinXcqtAlJXW8fGP8wM8eJ49mFmqRGwDvLDaK5yDW6IHYG0JVpryuCocGJuYXhnx6dOkTtCKnYt0hk8tEPuocITjMRIWRXil1Z2X6IEgb1LObvmaE9saJkOqIZq028DhaPUbbRuwPVMRXoMC5GXtPeZn5G7lET0e61ncN9LXVKCaN5NTYOsV1id_m9lox1Hp0sF4sOjfNc9LByGgh-Io986cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Wf9QFXaHilqVDnnMxQbOj6S-7GXKi9rdmSUuJJlj_OWFIHB_eZ2JA_XfHHN4VxvcLGF-yHEPH4rohXrX0ZEv5cDeLFRuHiHN8idwratDGp9IWotd4heKAurEBd8I3zECSig_Ka6mjw_Ye8Y_f3CnQROUGkbDrCiSOC3zR2A3ehJwAlkBxVSwYe5mpa86mvSCCvQSaQii2-n-0NnImjgUuayc5NrITlLfNsuvjFHLZXkyxhkPR_vp24xQ5EMEvpiXH5sWM9aqZfw6YjNm81U46InhCsh5YCApCIcwDlgWbwJGjE8X29j0trjygpeafvmUTjmdQ6NmiYWmP25V1lcn-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c571dca434.mp4?token=Wf9QFXaHilqVDnnMxQbOj6S-7GXKi9rdmSUuJJlj_OWFIHB_eZ2JA_XfHHN4VxvcLGF-yHEPH4rohXrX0ZEv5cDeLFRuHiHN8idwratDGp9IWotd4heKAurEBd8I3zECSig_Ka6mjw_Ye8Y_f3CnQROUGkbDrCiSOC3zR2A3ehJwAlkBxVSwYe5mpa86mvSCCvQSaQii2-n-0NnImjgUuayc5NrITlLfNsuvjFHLZXkyxhkPR_vp24xQ5EMEvpiXH5sWM9aqZfw6YjNm81U46InhCsh5YCApCIcwDlgWbwJGjE8X29j0trjygpeafvmUTjmdQ6NmiYWmP25V1lcn-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاتز وزیر دفاع اسرائیل :
مثل غزه! نابودشون میکنیم!  به آواره‌هاشون (اون ۲۰۰ هزار نفری که در روستاهای شیعه نشین هم مرز با اسرائیل هستند) اجازه نمیدیم برگردن.
کاتز با اشاره به فشارهای ترامپ : هیچ کس نمی‌تونه به ما بگه چی کار کنیم یا نکنیم!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNaEnmYixfZUsj8qZho5tbGaEq6mrjKsxHkhcmvm6c_7z8cuIt9S-6wgRffdj-Mynsicg0kx3qS6ue1jExpkuOSw6X-waoMpUXWGNQ4aUsFdGnkxQoPnz2FI5kLJhvo2pTVbp5S9LSIzrkBH5NKKPiQXy4guMrN4yjxduYxp9i6uatijnb8i19-_5paAl5lKim_jw4NZxzMICNXeEb8YhSxXMjQ-n0YtDS7HLmVxIB9psZaMJkoWmk7SoHbtx1YyzxyeAUM7IohOPyDPtQJ7OcTdI9ru2wzeoPhv6Z9Wa5QuQ_kRdUWRS4_30Kd7Rj2O_YEZvAkcJRiVIcHuQAfwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJ2zZxfnkMNDITMtNtiJdMI0rBt_cuIKIMyAfQvAN5fPRtxVpM5kRcDSXjSyoGTbd_xm6-Xz9fsQVHPjWis7vdp8xQyrZ22GVXohviT3yleMjWwwZO8Uo5KxXUK4zoQ6vDLAc204UQg8ZnW4WGcWV76etpNCnX87pTgTjGJYnwX-lA1T7UjPHfvABBuTKUwyBtMIhuymK7FF6bNomJSSnKOJ3xPWyPxnlhogUnzMBc8yQ4kYjNVwyavJ8CDxFEaiYLNdvtxRzsYc3TBxb05TDC9uxQNHmV5h7zTpnntkPCZ2FQi8hYiyy9V4nFihvOAkv4-kUVnmS5b6nslk0VflGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=YecdkQ-aA1LUuXjlL-RfEOMgu0x-OME0zaVYyGBe9qmwtEJBt9nkqpOqJOgPOyOimB97Ip-si9_-uUeJgkEZvsKSN6esNQnx93J-kmSFT9dVqEjsjaUOxglW4-GrGjb5zgOG-pJioVXiX_1hZlhuH8CYegQh_Qx3QqyTzxaFGkZjAQrurbHBPUtPoKOnkv2EHSakyJlqm2WGFuGO894vxcZYFIIXqapAgxGAStIbnGbEVlagKULVBnKbmJX2AZk9rj8RBJclZ9IMLG_EvTey4o3-eLn0_0c0J09JzRAURuNTlTXNYS2l4cJllzty2ibC3NxQd7FvPQSekn2JkwFkOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=YecdkQ-aA1LUuXjlL-RfEOMgu0x-OME0zaVYyGBe9qmwtEJBt9nkqpOqJOgPOyOimB97Ip-si9_-uUeJgkEZvsKSN6esNQnx93J-kmSFT9dVqEjsjaUOxglW4-GrGjb5zgOG-pJioVXiX_1hZlhuH8CYegQh_Qx3QqyTzxaFGkZjAQrurbHBPUtPoKOnkv2EHSakyJlqm2WGFuGO894vxcZYFIIXqapAgxGAStIbnGbEVlagKULVBnKbmJX2AZk9rj8RBJclZ9IMLG_EvTey4o3-eLn0_0c0J09JzRAURuNTlTXNYS2l4cJllzty2ibC3NxQd7FvPQSekn2JkwFkOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=cyPP31PjYFFyn9KlZ6grgAk8lRkHVMo4rObCCdZFXuPuFYgZV9K7plHF6OCMG97th7U1eQ3HzimuvjueyhutaoKRkpR-i4RWsmCLtVdf210p6woeo1gHlWjKaxvTJmU-dPeGea8ar79zO07z54cXB-nt3ZMG0nTMKRbSXHPk0t43LAaL6sziHB9P9bO6dWcD4Ajia4Q7QzXhJfV87mUaL8sFAGLe8qLyNMemk-wI7x1Jt5_1cRydLwRjjo-QgAP2m_uoxl_Z0Mavv5n9meqZu9KvAgdFQIWoL1HKsiRrXbh7oIgARoSz-dH3UUpLW_IMsRVn_dK6TNcboNvlyQdc1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=cyPP31PjYFFyn9KlZ6grgAk8lRkHVMo4rObCCdZFXuPuFYgZV9K7plHF6OCMG97th7U1eQ3HzimuvjueyhutaoKRkpR-i4RWsmCLtVdf210p6woeo1gHlWjKaxvTJmU-dPeGea8ar79zO07z54cXB-nt3ZMG0nTMKRbSXHPk0t43LAaL6sziHB9P9bO6dWcD4Ajia4Q7QzXhJfV87mUaL8sFAGLe8qLyNMemk-wI7x1Jt5_1cRydLwRjjo-QgAP2m_uoxl_Z0Mavv5n9meqZu9KvAgdFQIWoL1HKsiRrXbh7oIgARoSz-dH3UUpLW_IMsRVn_dK6TNcboNvlyQdc1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR8JAIJzL-MkFoIp9N3X5I0_fFWOsDA_KZ2LYCRXp9cXrXI7an33UOdVHEwsxxgKBH3B0nbnSvZX7uCZkW19xSnyJXlawqi1uBvHyr4FWXvDgaL960otiBzG0jr46ih1I3iADWVDK5XdGMlWaRXn1I9-M4xwpap9F4jbIfwCl82NSbtKfOLyI4VjjPzwA4yXT1P57x84QiQkqUIFgXB8gr_sG7wT3kQC6xgwe4hRiN3yCBC4tTcGh5yboiTRgxyFFEPUCt2aypiwkTyig1CqlAs8weh-PMHsfAheQ_-vqy93mqPinViKts0nZzijk3xGAcAthPX24Aqnp12KciyymQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aECkuhEdwBJ5-V8aB9IruK8z4kJjmNi0Rt90cJopx_Sbe3HSIgjsnxhsMl6_OO7yQb7jIlFp5O1-n96OYPluHTQpiCJFNXqNZM_F0MiqsR_fKAaFRoylxbYplmUnVRFdyx3RYj3RlmaXjLIT2xBhWAsxErCdED5dGjsbbnOS-xUTsIAz6BYj4qWL81clGrGx4AqKgfUZUTbwELYeLqRym3kZLbZnw9ivRqU7b-H_x3A4gyXcqT9ucFP5UG44i3by-49b-sIpfRTS0ihgD645LHkKjVsFu9WwIxa8FOd6CHQ7y1H8yjY-XTar3keaz5KWO1dzPOuIYnrvtbSbYP11yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpM-RZ5JdQKGve3K5rgAZ-UJxoBkPBBHGtjSa93Mj1mK7_IRaTREVtZ1wfdJu1BMdp9dkoWji_x8RGL1pXiwSmyBS6ijjMOy0y0OsfkqGyc-G0O72jQyu2uolzLzCIfzeWRIFQiuIp3WdE-auPm20OM7uRUSBLSl8Lunlj3807mgU7iMdwVcUgFVKy5Ua-hARJtaoibGLgzZbkXU5err3_WZs7OW9CWri3bPH9KYpjZ4dt6Is1fvp3gTigvo5_E4pOu07I10mhKel7NNo8We8RzLGz4ixXdaQGY6e8yL_kVThGBwrqGA1_keHDsmsXfuMLm2KD70yuQiPTcetPsWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=XaN180vLzo1XzHzGZKlJy7L86rcj2UJ4liGlFnuNJkbbQz3OJRAHbSXlwyenih2cDjZlyku5fgLc2ix7UNeQkZPbXEAVqQ8Pdmi90KQsiTzcjjeWMW1IJaHRnvYqWa_rwdwcjeQD0W9mvJUDQRSoA2Ef61AnnXVIEB47L4oOJx8ckOqzRUvJiBksy6V49coCdyZHpOesihyiQm4nqCzV2UCDoAlXHX_y97vWF0P7qzjJwKV9VXmMT2_wipQJ1ktP02AIaCbNUI7RzUEvwojKg4vLzvQK8sF6zUUWeXDbJRs4v7F09mc9yMaWKjmsFi_t6grFd5U9r2vSIdSqFBp_bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=XaN180vLzo1XzHzGZKlJy7L86rcj2UJ4liGlFnuNJkbbQz3OJRAHbSXlwyenih2cDjZlyku5fgLc2ix7UNeQkZPbXEAVqQ8Pdmi90KQsiTzcjjeWMW1IJaHRnvYqWa_rwdwcjeQD0W9mvJUDQRSoA2Ef61AnnXVIEB47L4oOJx8ckOqzRUvJiBksy6V49coCdyZHpOesihyiQm4nqCzV2UCDoAlXHX_y97vWF0P7qzjJwKV9VXmMT2_wipQJ1ktP02AIaCbNUI7RzUEvwojKg4vLzvQK8sF6zUUWeXDbJRs4v7F09mc9yMaWKjmsFi_t6grFd5U9r2vSIdSqFBp_bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWNzIUYyJaeFrGg0xGaFhSlPkAkulWn7j2e4kZ6Nqass_6Y3KtMuTwbo3N9lCcT3omvn1ecNIfhYtrW9U9a5EYLkwL3_qiTnKSU-7CJJkGH-ZhqzuIqxtO3Ph0V-pcdH2Pq3FXNg4g37nwpKY2x9YXDW9IuuhFoiY6kC5zJmjvtaN_mx1LRop-zwgngb359SYeNUhL43v9k9vSATpOql6uoMZTbA-1GuNKgX1n2lgNTUBi75q36VFjGfoJBf4K1WDNkmg-jrpu_YpBnvhExY5X0yQNDR9pUkPDK-Nds6ap1Z1xwS89eObjVWfGSYi9AI0w0Ra-UzAPASrY7_eSx_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو
به
ترامپ
اعلام
کرده
است
که
اسرائیل
بند
مربوط
به
پایان
فوری
و
دائمی
جنگ
در
لبنان
را
در
این
توافق
رد
می‌کند
و
به
رئیس‌جمهور
گفته
است
که
اسرائیل
خود
را
متعهد
به
آن
نمی‌داند
.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkwXhiYR91pSfodkrdV0ELnsF_yH4e7IjWKMsU-s4f6ftjuucISihMfFX3j-fK_jyumayOUihKYn8uO7zqiqf9ElP1pUGIj9gE7-IEsampqYqXxuewFlVEh0IpM2RhkMcelyk8CfOmHQGSloptPVxahZDV-J4jr0Sz0z_PjaPQV1PjP3RqRd5KRIl7bj4Z-Mk95WaXJ051L7M7rOWNxBpurPJ5CuAbBKPUm3Z9IV_440kXXig20PnF7amGpDmskMUDcQykdma5z2iMjsz6mYHXexyfTD6WZBMBwyrfZJgdUkAAbP1yUcquzIRS2PBOttqzkZnZaKUcplJpjG8RJcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">جمهوری اسلامی تا اینجا با آمریکا به توافق رسید، اما هرگز با مردم ایران همراهی نکرد
و به توافق نرسید.
از قضا با اسرائیل هم به توافق نرسیده.
مشکل آمریکا با جمهوری اسلامی
برنامه‌ای هسته‌ای اش بود.
مشکل اسرائیل با جمهوری اسلامی،
اما هسته‌ای، موشکی و نیابتی‌اش بود .
مشکل مردم ایران با جمهوری اسلامی
اما ذات خبیث و خونریز،
غارتگر و سرکوبگرش بود.
اینها هیچ کدوم حل نشده.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhCBW7su0zyE7DgjTyocLqKxQNLz_FHdGl1BabR5cmXEDJz1lZyYLzcWKH8rfzfI3qY5NswsUyQvXYCpKnJASKZyS_m5NhDS3UrjP-oaEmByoF6_3o06TIiQCH3PonjIKY-pDY217yK-5ue0Pq8aHu2iIZpKIWZZp29u7Hpc9-_WS5LYYXMCnC4-gBKCWxzC45KPgVe0rHMZUpYzkKQqFGEM_b5DhHx7PMIpSRowBbk_vBzecNu_92QCN_svpWZ4ETZ_T2yuBTw5hS6LWCfxeTcp1kW5SIwKPsbZGf_0eXHKwHACwCAbTwIzc4b7jhPQDNXoALmT8O9W5v9LPAdtMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbNnV6d7HqKbUFKRGijtPkFfcSuDowOhMfvuPVCPo5N0oqhk4NVnL58WTR85oFOMToP-QctDWF7VY7Ujo7vp8x5pfXRG-q4MCFnhcaXZsWK8y7Lwc4tn6rtSbCjWtTOA-Qiih5Ho6NrNknI8gIMfRwCor2wGYIiLnNT6-ErtbjXqj4YW4QOE5KZKritcYMjQxvHtd_LIlYxXxtr6iV0gFtP-2ExO0ArV5qLXAumV5U0vDekk-DiIaEDSlONEmhgor4UE42b0bkoOHvir4MC8oxtgp9H9NGndSL2qlhOoZZnv0xa5w9NPjaMp5IiXKKVvBNnQVfMc_GsyQhEShkh1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=ZZzZwwCcDPtJufjOB5lhXrPv_9LI97TjSPXkqNd-lN8kSkH9eG37JGrk1rrcXQx0EF-etLBuCkBPZjiImWAtKG1fWvyAG6cIZIqGmQjkur_TMR5fZh9equRkeL1XOQQsi5Deg7N-nkqPN2D3DBKoFGjYWIL8QK2YQwu_W7WCagz0hNmyUt4-kw_TImZDA5ITzQjsa7opZeh2o8FWZaFgLO_UKEXYndc8OLIQ9mQmr87ZiIWnYYDgQc3KMNCqW4ewMeM2HzTexuD6dEMPXtkkAiPpNWyXBBFDEakupFwo38WlSzLsQHPi1w1Up_eeefXVun8unzfZP5t9TDset-7K6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=ZZzZwwCcDPtJufjOB5lhXrPv_9LI97TjSPXkqNd-lN8kSkH9eG37JGrk1rrcXQx0EF-etLBuCkBPZjiImWAtKG1fWvyAG6cIZIqGmQjkur_TMR5fZh9equRkeL1XOQQsi5Deg7N-nkqPN2D3DBKoFGjYWIL8QK2YQwu_W7WCagz0hNmyUt4-kw_TImZDA5ITzQjsa7opZeh2o8FWZaFgLO_UKEXYndc8OLIQ9mQmr87ZiIWnYYDgQc3KMNCqW4ewMeM2HzTexuD6dEMPXtkkAiPpNWyXBBFDEakupFwo38WlSzLsQHPi1w1Up_eeefXVun8unzfZP5t9TDset-7K6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgtCVriizB_mtVQmN2vw8AVDjEmboV1Jg_xZL_fiTx1R9Tk0fisO_0-rmc1EQJ9EnoTXHyeosg2LHK42zSti56js1qAn46x_KMjG7DYllkpaRoqoHDTCpOvbLYPIk-ezIbJeXW1H7NNpfCGHyM2OJi-jwSd6jEOK_m6EygtdPXw7gM7oS8GlVTpXFqlAAOBp_TKNtTJfi7Twk8k2E3cGR6JSnHkEjHK2Dtt-hoyjFFEfhEQ05SMWWVTOuRgcvSEBsVQKI5U8pW8lzI9XlEPX1_rY9Lef6gqdG-H5X8X9yMDYKP_r7can8sJtchQ181qDBrIyim46egYGFYd4FPUwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منهم صد بار نوشتم!
جنگ رو برای خونخواهی خامنه‌ای راه انداختن!
بیش از ۷۰۰ کودک لبنانی رو به کشتن دادن!
جنگی که نه به خاطر لبنان بود
نه برای منافع لبنان بود،
نه با سلاح لبنانی‌ها بود،
نه با تصمیم و اراده لبنانی‌ها بود.
یک گروه مزدور تروریست
از جمهوری اسلامی پول میگیرن
که هر چند وقت یکبار جنگی با اسرائیل راه بندازن!
فقط برای زنده ماندن شعله‌های
خشم و جنگ و کینه!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=pwVUx1LrMblKqrRodZ7rjW-2jd74qGrk0R28kns4lxU2znZA97s_U0FJ3w8l5Re5zBd3dKjkLI-bSewvxXIxt0jXRuW9e_clqYe33GnBRWmvTbs3ezFNyGlIHNbSoZ2UQOid2Pk0aAnAhcnm5m7QGAbFkW4Yt5PvxHiK-E3-CbHar0L13X_qfTeaGOOQIBhhlwfBbdOuHWguXVFHy_5UWmqM_7NLHNAymEcCv5ZLo4ktgtGJPFR-39CpIv6nEZRhSBdu45R3SU46NCTVnTPbplfyRTk1AQBWwFOQkxYUMN4VARRdU46CxyuAs_hVWG3RFhpRKbT2loC1jsDws9T7LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=pwVUx1LrMblKqrRodZ7rjW-2jd74qGrk0R28kns4lxU2znZA97s_U0FJ3w8l5Re5zBd3dKjkLI-bSewvxXIxt0jXRuW9e_clqYe33GnBRWmvTbs3ezFNyGlIHNbSoZ2UQOid2Pk0aAnAhcnm5m7QGAbFkW4Yt5PvxHiK-E3-CbHar0L13X_qfTeaGOOQIBhhlwfBbdOuHWguXVFHy_5UWmqM_7NLHNAymEcCv5ZLo4ktgtGJPFR-39CpIv6nEZRhSBdu45R3SU46NCTVnTPbplfyRTk1AQBWwFOQkxYUMN4VARRdU46CxyuAs_hVWG3RFhpRKbT2loC1jsDws9T7LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=B7qQxSkPuVsmcsAnyGL15yqZM1G0KaK5lux_WVJMduDST7sLg2WmRLbFoUj9P67HaUCdrt0VAThbiCryUOP7PMGJcEBD5lAY0dHQS1Wun8CmME3HZa_Beiaik8_xR1cZwjgMugH592TP_A2MqiGJ9o91go4-OFdrI7FjEsIwrwcyhaRQBZixf7cJJ_RQNdG0nhAxkCpO0gpwyF24K8ZSKswtpY3_2G_7xstPSAAPb1_k4azRgJS_JK2FcCUfSiWEhMkBSo6SxqOAxXuI3tn6M-tkXnzWDG0HwV8bO-DE7NoKwdo9mHhDfHeYMwtPJWL5gK2Cbse-o7_hWJTSQhoYmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=B7qQxSkPuVsmcsAnyGL15yqZM1G0KaK5lux_WVJMduDST7sLg2WmRLbFoUj9P67HaUCdrt0VAThbiCryUOP7PMGJcEBD5lAY0dHQS1Wun8CmME3HZa_Beiaik8_xR1cZwjgMugH592TP_A2MqiGJ9o91go4-OFdrI7FjEsIwrwcyhaRQBZixf7cJJ_RQNdG0nhAxkCpO0gpwyF24K8ZSKswtpY3_2G_7xstPSAAPb1_k4azRgJS_JK2FcCUfSiWEhMkBSo6SxqOAxXuI3tn6M-tkXnzWDG0HwV8bO-DE7NoKwdo9mHhDfHeYMwtPJWL5gK2Cbse-o7_hWJTSQhoYmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfI70m7Ap6j80EwT-PuV4cLp8_ljRkoQ7gV_vAbyxPeH3HSecHfR_csAe0A66FEBKVL3uGZo7k2ywJi6jp9KoRV58boc2r99J8ZQBP5zB2MCR4H8yIPNOpBHDYLI-h6hMrfBk8jwq5DELu34AbmrZ3kjR__p6eLFnynQNJojmZuTnfG3FSWa0X16vdV0TqfyHg-qTeWUbQoRGRWIojXnwABT3zbVXl8gC_9cS01RLkupW7p2INxEby8G9T9rD3YD3WFuZm7B8logAjrJdIeiFMSXOEPjoS74bwDwZ-EWlGL2af0J9wahetwMVw0-P1owCiPi5I0kAzUOHvJUAL7_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=LXfWB9IjKLsFN85eB7i3WHP2ViIP7KutQuKetPjQexu2L9gJCCpF_Rfu1uk6g0RSoZmrsM-MRSlQrLtQdx9aEmlSAxBZBIX9cTxobUfXJvbuCQ30qX7PYhBeFI1jpkrtmPgOewqjHJcc-jjmIJxNLu_i3vFp1-UrPeNr9VWqfIVGo6K1uePiSaWUckvo8gP3HkTdCQ_gs7yDxF8GqtBbAXXt1bHP4uaxIDtpIJFYXw5i_IBkt_TrcJMiPVcVma35_-qPNIrIri9XDvkptjJJKtQqNLONqntXyrnffrMgJXQS1enJPaAMASoiybSpM6Sm368qulkW6bY_HGX-HBeC8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=LXfWB9IjKLsFN85eB7i3WHP2ViIP7KutQuKetPjQexu2L9gJCCpF_Rfu1uk6g0RSoZmrsM-MRSlQrLtQdx9aEmlSAxBZBIX9cTxobUfXJvbuCQ30qX7PYhBeFI1jpkrtmPgOewqjHJcc-jjmIJxNLu_i3vFp1-UrPeNr9VWqfIVGo6K1uePiSaWUckvo8gP3HkTdCQ_gs7yDxF8GqtBbAXXt1bHP4uaxIDtpIJFYXw5i_IBkt_TrcJMiPVcVma35_-qPNIrIri9XDvkptjJJKtQqNLONqntXyrnffrMgJXQS1enJPaAMASoiybSpM6Sm368qulkW6bY_HGX-HBeC8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=mlYfFcRzlZ7X_q1ht165OWrZZmNMtWdl-bvFyiXyly5VveGwDiEDbm7x6VAg89o-XEc8ja6c3t0IH9tazqPGVnmSRbq7NMnFBkuBj2vGdUv-Qysdnnas7OF5f1LZ9trO2eshRW4zPOD3Dv4Gf9KVLbvhv3tu8PBPg1tACPpaA072H6cPER7IgRuBmX8r2KiLqD8-YtDvSYuXm2BXb4yaVp3t1ndhqhQWUXWhA9z2xpVd_WyIPHq9H2CjAztEG93S0XMZ_AlOUMlX-3c0vOn8y74wqMHaS88eoam22MT9D0fbn2iL_KGpViInKzAglelXRXXaQzuI3ZY5TOC2fHH1Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=mlYfFcRzlZ7X_q1ht165OWrZZmNMtWdl-bvFyiXyly5VveGwDiEDbm7x6VAg89o-XEc8ja6c3t0IH9tazqPGVnmSRbq7NMnFBkuBj2vGdUv-Qysdnnas7OF5f1LZ9trO2eshRW4zPOD3Dv4Gf9KVLbvhv3tu8PBPg1tACPpaA072H6cPER7IgRuBmX8r2KiLqD8-YtDvSYuXm2BXb4yaVp3t1ndhqhQWUXWhA9z2xpVd_WyIPHq9H2CjAztEG93S0XMZ_AlOUMlX-3c0vOn8y74wqMHaS88eoam22MT9D0fbn2iL_KGpViInKzAglelXRXXaQzuI3ZY5TOC2fHH1Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUz6yNt7qo413s45GTk5PlFUtQPCKrXpP3tc0bNUJXoxf0YC2NzsxSD5U9wpbC1pQQ7MYTLS1dmnpAuC6tA9L6AvMq6BeCywI8crG1oEOUsR5Tpmu3-vw8FtVgzVJrtvlVEWXus5kY2L0xGSmGGQrVVcayKWkuirGjwSsaroTNmlbfxiyJIeYow6uCqaAw4DeBeuxFk-XwC81zJPzR07pOHYQ6hpwI-FTydXZNlAN4kCiFJcc1TcFGaHLeqtJqJ8cz2fJJaDUxtRVYMdCY-w7r5lcCQfG6QNwshPxTRERPirPyBIkE-sPCgdAHHfp1x9_zx0vniUqDE1J7y09VLW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUz1cKGIUze2fryBEswXAdzxHLOYyAmdwUNDiTPW9im-AYsJ6jAaNt3pWAtgglrsuky4KYCqad3L7HAFPOja8LsyECx-tGMAEVGoGmRQ6U0qmxSEIlWf-BYfMKMz8Fdq7ghmkGOGFkZnSJlvDXs3SsnM4Q5ofbTnpIIa5amGzmhUtb7Mh_ozM1Nkvxq4Af8txJO_cMyvhMKm8pUUJ3nCgGtXJAmhojscIa1Eh_BWpIzZXHGHvaLrfarMztD8F69yXfiTonopSK0uIsZU_6dauFsRIaNsP_kH9pC7sIYKSWsVF3n5t3MsTudhE6AfabszHjuQRQtdfzqwmN2h--AaoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای حزب‌الله ۱۵ سال در خاک سوریه و در جنگ داخلی سوریه مشارکت داشتند
تا اینکه یک روز همه شون فرار کردن!
مجبور شدن فرار کنن!
نیروهای جمهوری اسلامی با کمک هواپیماهای باری ارتش روسیه به ایران گریختند، نیروهای حزب‌اله
هم زمینی به لبنان برگشتند، گریختند.
و بعد به سرعت نیروهای احمد شرع
سراسر سوریه رو گرفتند.
بین نیروهای شرع و حزب‌الله ۱۵ سال
جنگ و خاطرات خونین وجود داره.
احمد شرع اما در این ۲-۳ سالی که قدرت گرفته سکوت کرده، اما اگه نیاز بشه، می‌تونه تا ۱۰۰ هزار نیرو روانه لبنان و مناطق تحت کنترل حزب‌الله کنه.
انگیزه بالایی هم دارند!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBAD3jrRBTJt1ImnlL8Yca9n_Y2aiMPooerailicUngU9ZLoZ7F0A1pI08IwX_Y4tD7lJVDRtx8AB6pIq7kRwzbhV5ULXkgspN4RiqmabEti9ZTuOnov09mYFKVrhp9ROz35ToQmwLuTl78GXy3wkkfqLx2kdvvzU1fuYcodLtDaC52n5w6nbPdbtWdjUWN9wMuq06u_ty_qw7JIGeGQ_AMOgSsXx5TvlAUKLC5soUuQx90WFr8Jj3hwbM12DAh0pmGh50D6Kch9KYX2jOknCRVSWEcGONnBtcb2hy6xtSXlximm1OjWvhR12qhGFM1nzzo5BTOOME7HfAekCuxVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMwu9av0PlH7U7bQ7MYLuRtLuaCIWnvrQ6JVMLSKznHlfaUCjD0pX03hvIWG4h8NBfU8UCIK29mIexqp6gGNomNSt_40dMSPocwBZlwgFJp9eVYHQ_7qBLcug0OJNu6mQI6vSBx_pdWuh6luzpcuYRKMEKY9Hg5fs3LfhA-lsyiRPrNOSzXsJ_WBoZUdga_r1XY7O7Ayod2MF93xindeGwXCpWdO7ja1fad5_SfUjgjcBdiRJkZuXZI0j-oWqe99UKAEsNNzloIkEYktpLj6Z_fTB8HRYONBxCdGzwXJYa2luW8RcnF5zov8NcyPuguj3mDxYmmyJqQA_Rqg8d4GJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=mi1cnJm8Sq6MYbfZisS_DFIVeDFkGWMTlP10dSnnP-OX_E8NyofYbwBKQHwG5-VjzF0CYXcDC6yR9EPTcjkaoD8CDISxAJB0mx-DCS2MvpWr4JT6tsCMAvbVbqeMjh5Yjty2ilLgPWqofD55TEwNvdPl-r-caM9e5WOkWdBGVB8uFhGh4wWGNUzcpVA1hiHpSgcL1dkkmVTUlJnt04CitUh5TdC3q0x73CafF52sKYHaKY5u2Z0qt5X-o1mVBpcNsm4aL-UqttJ2VZq3KCoDYm0u1ld-rdm8ta17A7JgPSFeST_7vb_bG0Ps-0tqdbP3S_1nWFpD8LIfXsJSvmQpdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=mi1cnJm8Sq6MYbfZisS_DFIVeDFkGWMTlP10dSnnP-OX_E8NyofYbwBKQHwG5-VjzF0CYXcDC6yR9EPTcjkaoD8CDISxAJB0mx-DCS2MvpWr4JT6tsCMAvbVbqeMjh5Yjty2ilLgPWqofD55TEwNvdPl-r-caM9e5WOkWdBGVB8uFhGh4wWGNUzcpVA1hiHpSgcL1dkkmVTUlJnt04CitUh5TdC3q0x73CafF52sKYHaKY5u2Z0qt5X-o1mVBpcNsm4aL-UqttJ2VZq3KCoDYm0u1ld-rdm8ta17A7JgPSFeST_7vb_bG0Ps-0tqdbP3S_1nWFpD8LIfXsJSvmQpdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftREQtJyJnBg9aBXKRBTSVf-Sk2lfHeP1-tVD5Wg-fGANp76DI77epOK53yFQ_DxScNYe1SLngHIGwWJ0brm7BXvyeL7DTAAbgYpxdcfniY88KozR2nD1N0Mfzy-0OycJZ8rNm6JLOGMLt5h3LdlzugHqwNk8pkjL4YdpmLxY9GlXz9Rex8sybvgU0X9mf1Lawd0MehHuCfApNALr0ClZK4Jf62yM_iwWOrOk-FFo2W-xQfyuLELvCLZoATYme198LM6dbENmxNB1BVpVUJHBzKfne0ZiqBqcjt7TNgJEQN6YFecdutTQDuF0lCfFMNanMZtcWb83AQBKWaFRjpTcp2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=Shq8OtJYjmipoz0XP54m-J9YRzcQE434yOKPrXeLmwZihGcsOpMxVoc5l9cvxw3RVNuDcReLXfhscNlHH869k5a2aYgfoSyufVX0e1G8DenChcoa9bVLduOrwjLS542R2oU59HXISR_5fQmOD24le8DghTzTXaajLwIRVLWmvBIUMs4X8T04FfjviMkxFI4p1SYdRkhOv7eBMu-fdx5SNn3a7vbt5OJ1ciO5XmuPeBAbIDTYU-nEOV26L5NlI6ElpVIxI5en6dyBaqAjPCbS0gLGxY2Mc12tPIO5-I4AE3dyWqhG9opd3ndlfIY_OOnq7zMIYoCG-W0mUzNihqdftREQtJyJnBg9aBXKRBTSVf-Sk2lfHeP1-tVD5Wg-fGANp76DI77epOK53yFQ_DxScNYe1SLngHIGwWJ0brm7BXvyeL7DTAAbgYpxdcfniY88KozR2nD1N0Mfzy-0OycJZ8rNm6JLOGMLt5h3LdlzugHqwNk8pkjL4YdpmLxY9GlXz9Rex8sybvgU0X9mf1Lawd0MehHuCfApNALr0ClZK4Jf62yM_iwWOrOk-FFo2W-xQfyuLELvCLZoATYme198LM6dbENmxNB1BVpVUJHBzKfne0ZiqBqcjt7TNgJEQN6YFecdutTQDuF0lCfFMNanMZtcWb83AQBKWaFRjpTcp2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCMnTw6TWroGDOl9PLTMzgmjmZPzgGERZyZBLI61KNf9Aqktlm1uxe2jzqGJd2R6cOg5LHIU7lq3VkGgZc7JP4U1NvpS7WLUlnJ3LEWVddFOgOjVlD_iJum0ehkF4KXzu_TXXbgOb9YaGrcG6j1BLNuAG-3xIudmlupPjSrJp45A2OG9KMtpgulJZLuUrtuT_gEFDOzvYig-1TwqDFjwihJTdD1VLG3A9FVBCLELD1c4LESfv32SGhMNvXNS4eIG1pK8Y2XqhnLlBKMlsjVYKrV0w0GtVZjlTpp7q_lkjKYl0RENsdKS-TGaju-UCIO8tW7CrgXTE5oUOW4zrm4ixg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ioZfzVCr5SaGq1UROVD8BV_llhBg6tJZSyFH2lTneSaYJncKpsjA-nyIiwLGlSSRyl3NkkivuyFbdGVB2fczCMQeTT2E0ejRzmsUentvRrpOGpIaQ7IButQHy8wYNv_HWex8QG_B3OrR_DtMfN09eFHyZ1jltU6q2jkfZdk1006qgVX--p58HoUW0J4eKkB3oXoKQum_VJdBkRpWFBlMjo0lC4MKjgQ9ZREJ6Bn9Lwz8JffjVCw_o6AMttlD6nNQfX_vQNpJofczArPJIewU2Dvu6dwNyPQ5u0JvJ7hZvVvFEX2BW5CNGHtI4NShIHYpY6gzMGy7eHydxXoThhJacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBQyvCGGr01JUdCq5tWKDR78BXQJO9Yetlw4oOqY3YWs8mv37QXjkbA4pxo3KZ0Rz2xfMVizNpln8x-6xH1IOQC4e5n0SKxvws5-0lKUbBNgEhGUZeCXXMBWHtz8oFED88rrynesqVdJRCHGD0FisYPQ6ALKJ_-7mxXHo6DL9PKnAc7FLOU2Q9e7rxoH5prcBVhrgaWgdSzS5bjIg3plY3Q6S1cLnf5F3cZq0aYrn9cuBBRpkTPspMdVCtUgOqIthJuT1ohmbqr3ZdCneqvN-bJHfcFTisaDdSV_XZ4SD2q3s6aDCI7zZztUnuIsRFDN5TrV8YEEwxVqo-1aldjhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GOXkhN6pv-SGvI7MN07wdvXFII1bYWPgIQujW-Nby7TVpZhvc0Zso2_MQuF7pSTjCyBJm_q-hNZD0C6npqPzLX8ukEUyoEXdrh-FdjEiqygEttC4JOx3H4PI9_jaB1_8kCSTv9HHAFBl-fDm0u3NnI1TyNvZOjRYK8Sl5ObO8mNNObnQ0_M9yk_BvEGQVA4lnMatA6bFsINb2h-Lu1_WCy6zeqf-Y1grO8KVq5r0MNM7x-SJJSfDzwn3lvPU2VaniAvzGnJYPRDq8L8CC1YfQzqrgtpDRha-WwLlp8YwDdG_BTXtpQ8lA5MoMP3jpadiBFymholiIzRTAKd3DxUN9g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9TCllaNmTTJOiq1M07nD9ddW5gERaHlYFT8sW7HVOkyQt4kZWj9SRuCExGND8rawH1Z1c_cfUFrUoots2ZozNKQx26NLVQxkFpeV-bF9iyvf6N5o7icIESsJ_z41qFuinIQ4JuVsv_V4sfz19DUQ-kTs73_583k9uJzyQ1Zw7XVvWc6rHelzKEA4uLDBNNruzGHzF2GBhbtMC8jqWaWnw9N96nHa6YM5IGtuMGzoL0p8vhRtPSav_iMPZmUSnGurJRhHdg8W1eK6-UPWLzISbka_NpKrXfdT0zcrLuFb95uL4Bm6cLJqhdVJQUPaOblofUnYc9bcofPoeWy2PcF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=FJpWVrDO2C_iE8ZJ8QfQfrJ06XLRhetMXr1kywJ3cONkmMC0eEKyDVrG-d-AvB5huSW6wH8OtkdiyF6htL-qCk5O6nG4Fx9s5UuXZd9yYm0eqcS4_m65MObug2oY94NGgzqxmWiojC5Mb4-v5tDupaHXsYBnb9piGnBVrc1On0C9JwsDJpELInegUPfflUByt7G3kDvjNSRvk-wyilobibnu5STRCzZHVvSXuqrl1ig9sUcLfDIcIW3oAZ5Ltcw1O01R_V7aXaeBYJoQ3iMIqxHXghMF-YD77SpQUX7-JnYVmTBnk9U9JJ4GC0-FtOGyoYyj4QfGBF4aEMtZ8OZUYaAogh4eBfnaLOe6J5_M4rrw13_vpBC0uy2_o_A5Rmjbviq1w334PLXT-2h-HK-h3iHOdfzw5h1oFoBkVrFyGxa-OwMmfTYRfntHKNzzrArcsXXAjy1_NsH0SHD_cTQA5ThOFw0-uBci_OqZZGK7w7_cG11y__4c-OOLSsM-L-NXEl_iNBJAoseRiIrNLNSvvqGHb4BG3Ua9eOjSXfh--gzbYgCHa7rEoIdAvQRO0vYKsycuriaqYN6xl3oCnNEg9POhbhH4ULqWzSPsW352sKEb98h0oyuBfsaVsOQi7Nigw0hAk_zw1fLsW7PqmdoySLSDd_hS8JcATcXZsl7TkSs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=FJpWVrDO2C_iE8ZJ8QfQfrJ06XLRhetMXr1kywJ3cONkmMC0eEKyDVrG-d-AvB5huSW6wH8OtkdiyF6htL-qCk5O6nG4Fx9s5UuXZd9yYm0eqcS4_m65MObug2oY94NGgzqxmWiojC5Mb4-v5tDupaHXsYBnb9piGnBVrc1On0C9JwsDJpELInegUPfflUByt7G3kDvjNSRvk-wyilobibnu5STRCzZHVvSXuqrl1ig9sUcLfDIcIW3oAZ5Ltcw1O01R_V7aXaeBYJoQ3iMIqxHXghMF-YD77SpQUX7-JnYVmTBnk9U9JJ4GC0-FtOGyoYyj4QfGBF4aEMtZ8OZUYaAogh4eBfnaLOe6J5_M4rrw13_vpBC0uy2_o_A5Rmjbviq1w334PLXT-2h-HK-h3iHOdfzw5h1oFoBkVrFyGxa-OwMmfTYRfntHKNzzrArcsXXAjy1_NsH0SHD_cTQA5ThOFw0-uBci_OqZZGK7w7_cG11y__4c-OOLSsM-L-NXEl_iNBJAoseRiIrNLNSvvqGHb4BG3Ua9eOjSXfh--gzbYgCHa7rEoIdAvQRO0vYKsycuriaqYN6xl3oCnNEg9POhbhH4ULqWzSPsW352sKEb98h0oyuBfsaVsOQi7Nigw0hAk_zw1fLsW7PqmdoySLSDd_hS8JcATcXZsl7TkSs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef7iLwg48hT_Zt3ao24Qea1UQf_IwohA2_jQ1pCIIgkvb0z2GsbaofDKjS6WSIN-n_6eMgvb5PHaop78LfPWnZuxR9rrVVdCF0BvUHgBnAn7x01SnQ_xXsi_3Y7mhXQ2NoZKhVA23JNFg_-PE01E06F4uL_r3WsEqGVOp3YzTSquDUkplWuuI354K_yH6ge5uYgW2MeAOHlvVyjH4HWLDAOixD36P2deV6E8NFiBRruDcfDOykIgVJYCqpr2aCd46g4DPOm6or_5SvkwKhG1OdpSVtkE04wmb82B2cigG9iZ68vILc6lWkIjqfGOF2JX6zt2Xo_2NBm0HrXFAzJKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=VdE9ew-tklqCTKRtn9rfPB8EHbMbN4el3m1ui9353NTOi8r1moYhAt_JgWMcccmesF3NTGoTUl9mwIA7PSa1-OavoDLe5OfK4j8H3kjdmHiTQ5PjQVD_MdmrnwH6QxiGP0Lhs9zbV_SB-RfepW6nbexACTIVfjAXbyW4IZTDl3vzI0cvujEV4WEnvruVvANvvfwcwr7-lLmDscVZVZSOZT1V0CQHAm6SZP92f1RJNygvkOGaBR7YyCkt58oJiEHx_uzDtCr4HtZav7Bk82WnzgRabHGwTgQgm49b27C8vB25jlQt7TxaMtbXKxvtLhdNpLMiT1D38dn65TwzYcNumIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=VdE9ew-tklqCTKRtn9rfPB8EHbMbN4el3m1ui9353NTOi8r1moYhAt_JgWMcccmesF3NTGoTUl9mwIA7PSa1-OavoDLe5OfK4j8H3kjdmHiTQ5PjQVD_MdmrnwH6QxiGP0Lhs9zbV_SB-RfepW6nbexACTIVfjAXbyW4IZTDl3vzI0cvujEV4WEnvruVvANvvfwcwr7-lLmDscVZVZSOZT1V0CQHAm6SZP92f1RJNygvkOGaBR7YyCkt58oJiEHx_uzDtCr4HtZav7Bk82WnzgRabHGwTgQgm49b27C8vB25jlQt7TxaMtbXKxvtLhdNpLMiT1D38dn65TwzYcNumIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=Rzl2pId8EElMARc3YZho814RPDdlYtIOKL-FjijuGG3VHDuovQSJ1AK77w6aPqeA7dIwJlBaECVjfapGjIRcY5q8X9Bq5fM45Idj6Lry5G9BxscEZwju_EWxYWmnua6gnW9jEjRPjbOu3_tXo8rewgXKDgQhyrWE0yhyq1zelBd7z4C1lwAVfHVy-AU6WaVosdTWHUyG9FAN_Y7JHPqcNCeX30vW-wPNjXcta3f00m4zdY75Vuq2z0o0pG4ls88NJbWTS5kbGsQCCS98ynZHvwrELUjBJgbQPiNcaYR0Khdmud7r0ORuFjM-KkcEBo-Nm-2KIW1UkMCCUyu4ewqJajl1MAsy4tiNlie8y0bWl_gToN4rNnltk_cGgx4iLajHrcabRwUlIwXWNNu3G3iTwm-CO_0Yqb0WifTGJMTqPo88mwsUqXOLatVdHgFAm53DJUcGX4z9qM4FKR9sf99aKnDfQAH17K-bvL0qdILQwgvR7ywHPHuE54IMDvlmCBP_xMgUID7bPsCiD7otW_Jbl2jt64QlU5eToDH-LmuZ5TQlHgVVFH58_gy5hxsGotZFKpJnYfe8PC9AxlCl6QSnMLp9KrdZBBhfX-Cjv6oMZHtxpFtUkpSzh7X3R8RKns-tv_5xMI8AelGYuDJOxbmAMiSS_AVbcdkwZnzurn6v7C0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=Rzl2pId8EElMARc3YZho814RPDdlYtIOKL-FjijuGG3VHDuovQSJ1AK77w6aPqeA7dIwJlBaECVjfapGjIRcY5q8X9Bq5fM45Idj6Lry5G9BxscEZwju_EWxYWmnua6gnW9jEjRPjbOu3_tXo8rewgXKDgQhyrWE0yhyq1zelBd7z4C1lwAVfHVy-AU6WaVosdTWHUyG9FAN_Y7JHPqcNCeX30vW-wPNjXcta3f00m4zdY75Vuq2z0o0pG4ls88NJbWTS5kbGsQCCS98ynZHvwrELUjBJgbQPiNcaYR0Khdmud7r0ORuFjM-KkcEBo-Nm-2KIW1UkMCCUyu4ewqJajl1MAsy4tiNlie8y0bWl_gToN4rNnltk_cGgx4iLajHrcabRwUlIwXWNNu3G3iTwm-CO_0Yqb0WifTGJMTqPo88mwsUqXOLatVdHgFAm53DJUcGX4z9qM4FKR9sf99aKnDfQAH17K-bvL0qdILQwgvR7ywHPHuE54IMDvlmCBP_xMgUID7bPsCiD7otW_Jbl2jt64QlU5eToDH-LmuZ5TQlHgVVFH58_gy5hxsGotZFKpJnYfe8PC9AxlCl6QSnMLp9KrdZBBhfX-Cjv6oMZHtxpFtUkpSzh7X3R8RKns-tv_5xMI8AelGYuDJOxbmAMiSS_AVbcdkwZnzurn6v7C0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=eiLIqzOIDnCSWdiCH2671od4JsRxYb2HwadvBM2uO-qb-Tj5ZcDEbqwAG3J5q91WOnI6UQTtNqycxhVFhRfHmCkdetedMP47og2gwzBsH9j1JKIetwJ2fme2q6Mv-qJyJyV1Op93E028l_WVf8XINdV5cAAyDJIst5iNCx3e1bMOg80tGsxnuPxRt2VOi9CeX9JxgqutwoIx6AkrDSZhEFyW1uKMOBJAJithanWbIbfxf8kgbHjQOp3j1fYwX1zI-oQtKqKqHjI-nD_RDDNOCp4WhzQCpDP_E2zVSaijVLrYYluqzY1PsJ65GwQsruDfMBChxU7QE8qdoHQLUBqLToi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=eiLIqzOIDnCSWdiCH2671od4JsRxYb2HwadvBM2uO-qb-Tj5ZcDEbqwAG3J5q91WOnI6UQTtNqycxhVFhRfHmCkdetedMP47og2gwzBsH9j1JKIetwJ2fme2q6Mv-qJyJyV1Op93E028l_WVf8XINdV5cAAyDJIst5iNCx3e1bMOg80tGsxnuPxRt2VOi9CeX9JxgqutwoIx6AkrDSZhEFyW1uKMOBJAJithanWbIbfxf8kgbHjQOp3j1fYwX1zI-oQtKqKqHjI-nD_RDDNOCp4WhzQCpDP_E2zVSaijVLrYYluqzY1PsJ65GwQsruDfMBChxU7QE8qdoHQLUBqLToi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dnea8AGvknEItkfXDkXSJJTe_COgtVM8Vpb5PoNxqKVEACzZ5EqrtKmmpEsEgMbVueEFlF5-RdNwOJjffEGh14YR9XAI5tNCwGdgOFy9181P_0TbcpvJJpDCUjk7bds8dAckdZPGyoTwywNIKv4a3ZpfzhUMoM5XYAtauA4kwNyAFnmcYhH7dOw9rVF29lAhNRvkPJInvHr7hwTciIrl0SRZJ7MH-oMKwBiNu9LEvo9irDN9S_ZIRN2Q6-OOnpU3zavBFYueelV_3krhOdmykBi3qFswqzGIhee5EzxLVLzZCA7OFtTmUkVHZ9PFPRR5bO9tFwqUjO1iA2WuqT2VBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWVjWg_Oa6hdI9VEsYq_GQoTj7AZisnwEvOs-p8vQpqH-Bh1aRXDJcjG9Douc1jYopvQu_UB7gA12dFG4oYfdchRvSrt6DcnpHcfaR6Dz00L1u87oxn8kVbOEDhiPnapw1ojPWDBz1T31r4kGavT_jPvjjiiFdFF1rchuqlkP5Sjp9GfQlZZuiVd4bp9wxyzGU_uAUwM-pqakk7ffyrIN0CqrjB7gUo9Q9dQGffdV2-sQ8WaXfLgWiS1NvETmJF2fvgh0fsnwI0JfKi_f1P6d55f48kEkwPQB7U3bRO1fSx4iCuCieCfoJ5vh14tpk7jOjMdyPKJa0UdrNxsUKd23A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzPx6klsGmPQjzyUevchNd7VFpQgpoNOM66H1uz3Kl2urrVG9N2STPG8ybJ8feU1p4HqlKZdo2f221yBu7eF3zb8d2Y-KrXvQUlaRC96XE8tsQrFTXcW5uqqk8WpjiT4k0XONmYmHDCnxNrtU7JbWxvd17YSSuugG3IEA5M5_UPTyoZrlEOwuCHNmF8KK9g12CkRcPQrdPDWzstXBPtBf-fs0RArgb1sYVf1Vgmu6di7YyX4HkoRGP9dcXyyFrsv5S--_E6NLF6-5xfdQRQfuR6BepvWBblySi7ejlBgsIgIKNVeMpXAmSBiYOzR8kQni3h0blgTcZqM_W8X4uT39Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nth4pGkZKs9fYjnIX3Me-qdPR8MHz80AvDVjgb9p9i7jH824O_WSFt6nHjU4GN3nUty0jGudbpMISHy334j-pmeOmLd3cT29UZDbnfe29GWJ3fWVI3G1E0B5eaGzvDh7cmQn0rzk6LFQWLcoQiWO3LQ3i2j36ZN_5pFIizbcrcT16CMsfC5uxfGN7ErAwYIrw9mRl3RxgQ3g2ZdsowwpaHnevaJAUZSKT9iU_14SGEW1c1UIzTY6eXlsJCLqjurdSDScj2VlaZ_wSTXaRrOkevj0D488GXOuYUA4lFKmLqSFnHi3yXSK1SLc1UNY9qVsMqBvnD3FX8SfwifDBMtAMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6xu_d1v0gNjZRzqZsb3DBm5UEho6B5kFiFDYnRvOj17QKC5lB5Yncj8nGyWmg47frxj2EzBFYH6t7xvf2aRifPU0RgJl0t4dpswdOI1xyiN-Alv76dLoTr0pA6hABPzJOXXaUYhOUOPOU77I3cI0cSV-FaA1EZCvBBj-_TpO02RDXOD8V1UxpCC-el5cfjHeo3eOGMnXjKnREC7Ps8jfExgOPCZPp8Ez3PxVJJxTGoJ4FiEFTQ83LQdNleCHDg-l2TzVhiPeRCZoSl5p45QrCnjbSCozZcRpgVB5OHPEbYyScF6Wes_ZpYL5jYZTFhHrwsBvsy0E2f-m4485PyNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=s-GP0AfMwDf_v4HghdJScj8cqtwxIrnA7KWV77wf9nF-F9GtOb_vqLnc_KH9hD02IwSWBL5SuMhtHw6Ij69jSejwnz8fYNqzcowSPJrgdjM3SWUKtDBJbwPjTDhTIjpR6L9qBzhwWxPATI-icli-rMt4_ZXw2sD68mOjW3rB0L5OnTru7Cqjq8z16m8gCMAQxubUw0gwb6WZksdOSZ3hFBe0-F3DStBuN0FUQCzcjwfmYP1bgMfnI6o9-uU_XRg5NYQCYS7n-C6uVyKXKXP4YN-ex6a-FpdMO2CWU-4TXVOhfU6JkATcDSSioqGeMqssEU6eBUjFJ6IBSGPS7JRQaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=s-GP0AfMwDf_v4HghdJScj8cqtwxIrnA7KWV77wf9nF-F9GtOb_vqLnc_KH9hD02IwSWBL5SuMhtHw6Ij69jSejwnz8fYNqzcowSPJrgdjM3SWUKtDBJbwPjTDhTIjpR6L9qBzhwWxPATI-icli-rMt4_ZXw2sD68mOjW3rB0L5OnTru7Cqjq8z16m8gCMAQxubUw0gwb6WZksdOSZ3hFBe0-F3DStBuN0FUQCzcjwfmYP1bgMfnI6o9-uU_XRg5NYQCYS7n-C6uVyKXKXP4YN-ex6a-FpdMO2CWU-4TXVOhfU6JkATcDSSioqGeMqssEU6eBUjFJ6IBSGPS7JRQaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFmCkXm-BBwuizSXeatUrOXmegRpHcjoJiUsjn1z0Dgu49CxgDcTfgSR1S0yNjDQ6uWhNoF8fOzjRt9kxy5PV42EGLAxR8uYSr_Wj78f4Xu_LXh25QtjsgxxbvOan8kYlzt-7I3Wte3tg99nuD-zctRtDu-PDVxm00GEb87JVhpH_rIyKy4j1W5u5e4MpxZd_Q-aLIzVg0naaInQZizAYWW2Wk504r84uX8VqZlfpousagMjwU-IXiAsMwbZKD925Xy5ZvM9bp7VmoMzcUO6YfPM6WN4MjhES5VQdiueGSzJvKy3AP7CvYCkYl5EEQl4VkQfsgNUyu2DqRmKX4hwSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-ND6bg1jn1UOwnyGRH-ia7SlP9hw9Bd3RR-u_eBhRs_526Ecr0V3Xb651tY-MnQxJFWu7Kjx-4w9hGYgCyuYd6zMSGbwxw9UlYe69lzOUeKmxR6E63kfSGV_rk6gs-FHM28-wOeRlJkNDrc_0ZAtjzsHYemJzs0VCAV_iFt9Dc9L4awcwUYZuw_ZtTbuTGIeM16y_Jla9aJfDf6qrKi_ulCVXiKsATd-e7_ijn6xtAvbk7GTKyBWWKvbqmbsWaddul1QKaz9-7cg4MvoP48meVpMfdq37WhP1HHceJd_yLaQEHijyTM4rpD1BESs1hPaXO3Y0UGNspg4_Wf3a3fnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fk3v42tlmlrxgj4Ynq5ASxAAXFYjw0KbLMMwmNkoHmnSYUHODmiijFNg_myUQP8IdF5DXE62AoBVef9si1DGX4U2pTosewRrzu3g5Yjv1zUE53hQ5U5foRx5OMpcw8_kZK9R1KHVF6M26f8QadGVCr3J9jDArb-UG8gCqtQHnJiziptKJ8ddI3a0_kECqqcactlrWJSxYoHlPZhqOOjWZqJU2_XTzcyxN9eZ0y_KuYDsX1Kd--yQpKHRmOip5sCh76l8xg08U9hCQ5oAS7OlYlAw_Gj_mRPsc6PurjJn5Pt3bkguVsVy5WMnLRtDdvpt2gzrUBRTiPXpuE4zTgNmQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzGi7aCp_Fjr_ujFbmBkaDQP8ZO8zl3TJgLKdyMfhK_OKsw55_xBoGm8LeoGdEySKq-KezhCSM5sSETlosCA2ApKzPa8WidMeNYLG6NP5ykTrGSNdNay_GNM38Enufi3tmnpynutnUM__y1O4FkJpdwWoIvbJ_biQhyyb8NduoJCK5Z9_X7qhZ67u2OCS-gBVOuTAJtCbY4nLCdpMsNhYkwiYIotnBJX62Y0H4XiMYcY9R_oIY7sOo9Jg8KzcDXczqqWstcCvoLTE9FlQqFdWtinAyH9O0wAfVQ73eRHMCqwJf3t9nxqdLPMMvuYtIbhkg4ow0-Mqf4gTzQvaEjhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bi42qcMwnr6ra4RUgM0tk6JaufYAzUxx9N4W3rPusD5ZhxJSzGne7eDIbYnnAGSbZp2yXR9vl5GlF3xjDCKRtL1_sNdpByris4IFAYJBQb9c9pPPWPML0WNSMmIZ0PXm4h2nsL0HKL3Tn5IqYRqt5HzGB69Nr8mx7SK0qKT0S31273uMSlR0_jeNjeCim8MVZLwJ7QLc1_neDgNPI77Qgpd8NgUcXMPQQjtZqx16eK57zZ7wwLYANKfe3JovuJvxUawbsf61loBQVLoNPUKyoBgjnEgR_RAxbE130RSETe4LHK2B_0xyAPFu1wFAtqy3I9oFRUuClKMP6s1Du5kyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/azRqiPZsyLzVBJjpFj8kPt7sk2pW-zoKIwO3yDI-KloGawNBpI2ePe_Yxmbfr5lgX6oXRUB9Wmi1bd4yuhU5KQC1Uji2cxxB5rVRO13UfheaLe_G9RHTsGXbdghFL49yqXM7sVBRQdv3crxSGxbVaLoIsNH129xTl1R10BQRi_c7PZbVsWILMKAQht-xRJ2IEZF1Ch1Nnaig9jugFWy7-KnxouvN002rmyAjX_rqv_rDf1_Zna05viXoTMH6_XiMIJrwFqjnPA-mq9lZ7W9Tytzqslsetl-bWAngKCBZqlnGJJk800RWdk_twG7GN3ohx975YIuHQc3LtMmnzHPGbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزادار کودکان مینابه
عزادارن حکومتی!
میگه حکومت همونطور که در ۱۸ و ۱۹ دیماه «به حساب» مردم معترض رسید و دست به قتل عام زد،
باید دست به قتل عام معترضین توافق هم بزنه.
اینها هیچ وقت ایران رو دوست نداشتن
هیچ وقت ایران و مردم ایران و‌ کودکانش براشون مهم نبوده
اینها عاشقان جمهوری اسلامی هستن!
اگه برای کودکان میناب هم عزداری میکنن، چون میخوان یک کردیت به جمهوری اسلامی و سیاست‌هاش بدن.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5550" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5549">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fuk9jVDugSiVK37wNXtap9Z6Eo5Z4hhUEzZpiA3lGe0YWzDJ7QnKJJ7dnpIm8lVp8gtWfwg4SazO27nmme5UA89eUEpiGC3akK87OjNeKB68PGYtcyiQB27tOF-_lp5Ikm0iafUxk3r_nCg7lF3tBwNTUm2OPcz9ruRGSOsu5XUJVkKb0u2ROYgafUJUWqBFA7vEQj5UPukKrB1vZ4eMKbLuqhbJ3C1OwF66stILZ_6yK3tyasvE4sygpmko3ZKV975YQ9SP5FJLbSqu8bPE0Av2Kva1rD5BSeQCoVVZ21-_bEHX1hY7EAn-xCbeteBqcLNMPGE3oIuU4co7HOrJ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ارتش اسرائیل خبر از حذف
«علی موسی دقوق» از فرماندهان ارشد گروه تروریستی حزب الله لبنان داد.
علی موسی دقوق ، بعد از سقوط صدام حسین، توسط جمهوری اسلامی ماموریت یافت تا به عراق برود و به ایجاد گروه‌های شبه نظامی شیعه عراقی دست بزند.
او از ایجاد کنندگان گروه شبه نظامی شیعی «عصائب اهل حق» در عراق بود و در کشتن ۵ سرباز آمریکایی در کربلا دست داشت.
اسرائیل امروز با حذف او،  پیامی چند جانبه و جداگانه برای حزب الله لبنان،
جمهوری اسلامی و البته آمریکا فرستاد!
فرمانده‌ای را حذف کرد که نقشی کلیدی برای جمهوری اسلامی و حزب الله داشت و آمریکا نیز از حذف او، نمی‌تواند خوشحال نباشد.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GgrkWruYbGhFrMYPyhEwFZrk9Y7-e6uWvUER6u40rEXIVMY16jms8T1WJ0Vg64uxtthTnOff6sFIKbo_gWSLw1fYwZKDsgZyCKzuP79HlbKlABNpC4FXYEHEC5TnYa3HEfhFcIZGdcXIqUYhwl61rK4dMbsF_VhZUfDjDCy73M1Vo2y-KqbHyYY33UzQ_X2hyyx-s_Z3GgT2Js-iN0SLTyhCBQQ3CzRuOuBiBvk3-q1VzYQPcl4nGGEy50BPsQI11q3IEcidR1XRmVvWS8FgrPoJnt5gQi_IiknnmEfHU_hDbS1lZ5LM2lMjyqOR9-5ED45JG96pVTF7BqCATX98mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=UmM0hWx751tyfwd4F14gggjWdzLFyYHUCPHHqVek_E0HVK7oWC60KkeWCvx5CaiOi3Ls94nDW64wKzQCj8aXJ232BQeS9JHXlp5Fh7jmsiga7AkX3sHK32jNa_UylS6F--oTniSZOHO65e0YyFLJJuYjzLV4U5NAsB8xhJx0xxUMLNF2c1VKJfpnspGPs7vj9jEiFgsqNTdCHgpXzgMQ6Yt1FUMslGOGMjT8wYg2ikl1-yO9C2VmwCUwUSxqKLDKR_xnqxl23hCSOoYsMsOKIN0Nnv_LVaaA2lwttkv5cXts-4n1_G1ynb3jLJHEXiJNnSGMkxQMf98VnI34xhGjJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=UmM0hWx751tyfwd4F14gggjWdzLFyYHUCPHHqVek_E0HVK7oWC60KkeWCvx5CaiOi3Ls94nDW64wKzQCj8aXJ232BQeS9JHXlp5Fh7jmsiga7AkX3sHK32jNa_UylS6F--oTniSZOHO65e0YyFLJJuYjzLV4U5NAsB8xhJx0xxUMLNF2c1VKJfpnspGPs7vj9jEiFgsqNTdCHgpXzgMQ6Yt1FUMslGOGMjT8wYg2ikl1-yO9C2VmwCUwUSxqKLDKR_xnqxl23hCSOoYsMsOKIN0Nnv_LVaaA2lwttkv5cXts-4n1_G1ynb3jLJHEXiJNnSGMkxQMf98VnI34xhGjJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=VHP8Bjc7M9a3H2IbuVf3Q939TVIyt6R45FhhXKaWzdzv_9uxN3mQg900-ddxCOzoyjnD2_i1nPxMW9ET9WpIAdZXTrUfV4UKlpvPk2LaumENPrhwNBZGCVbNphy-pOCMNNhmbpK8agY0zGmtCj9Ae2yIqPAOAIl1K-OSWyiqmN1qhk-g6ESq3dzTqOibD7zgYRoSonpPWAS7B1z_OOzlvoWnuP8XAOtqBm6g-F1S9Ea1cdnsbAtqhy-GIFNsLeIfsjrwT7-WurjXovv2eKE7iisHMoneWyMwxGVd3Q5RBx33O-yLg62qNkM1u5dSUNlaq3BlQYtZ-GnVKbgsF2Af5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=VHP8Bjc7M9a3H2IbuVf3Q939TVIyt6R45FhhXKaWzdzv_9uxN3mQg900-ddxCOzoyjnD2_i1nPxMW9ET9WpIAdZXTrUfV4UKlpvPk2LaumENPrhwNBZGCVbNphy-pOCMNNhmbpK8agY0zGmtCj9Ae2yIqPAOAIl1K-OSWyiqmN1qhk-g6ESq3dzTqOibD7zgYRoSonpPWAS7B1z_OOzlvoWnuP8XAOtqBm6g-F1S9Ea1cdnsbAtqhy-GIFNsLeIfsjrwT7-WurjXovv2eKE7iisHMoneWyMwxGVd3Q5RBx33O-yLg62qNkM1u5dSUNlaq3BlQYtZ-GnVKbgsF2Af5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=Y1HEKP6EX1rWegH0yUTE1MdfK6LBeFGyaOcHrQbpFYkC1wk3LEVDikCn5-J08vH-RRAgs7FSQ3EQK1MtmfsEjK7s7Om6C2JTqfh00K_9owGsb5xyNUP0YKTgVkXRLb5P8AlgLZNaiGSXlBme_oilvQVWPHOKYVtVkugUSiCB10UnQnlEhbewxuo3WHELQPgVr9damN9-H5PRxf85u8q9mqvGGfCy-FQD0ZrCfGr2azR7Gy0cbZ3AN5VpkotjHoNQTzSjzZ26dOYDlp0_hgQH4wclOTMxehX6d15z-XCXO13eywEQzOm6Tsu6zjji7e2lpHNbBH654-VPcEEmJv4BvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=Y1HEKP6EX1rWegH0yUTE1MdfK6LBeFGyaOcHrQbpFYkC1wk3LEVDikCn5-J08vH-RRAgs7FSQ3EQK1MtmfsEjK7s7Om6C2JTqfh00K_9owGsb5xyNUP0YKTgVkXRLb5P8AlgLZNaiGSXlBme_oilvQVWPHOKYVtVkugUSiCB10UnQnlEhbewxuo3WHELQPgVr9damN9-H5PRxf85u8q9mqvGGfCy-FQD0ZrCfGr2azR7Gy0cbZ3AN5VpkotjHoNQTzSjzZ26dOYDlp0_hgQH4wclOTMxehX6d15z-XCXO13eywEQzOm6Tsu6zjji7e2lpHNbBH654-VPcEEmJv4BvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=AGGkn5QADNm1zTolrowqfrYI3qidsXm-xM6YBenOo6j4c8ZCNA39Ge2MbBw5_Qdjn3FKf9yjH8tP0ZTzEnv3wH-zRc0PUNvmrT6cf2fXSvduCUOwURbhjFGcXQsNtKVlhUemlLIFbaqcnzarRZeoZcdqEsZBbtASkfx_T4Uc5oUA395vNRS1SSr3wQi9yrQ6RDPtxukzaS_qMT3Q_aGZLP7HhUMwXWslpvyi_eHrQFUVneaLEf3oYcR_dpnXlPeF36rSI8eK80aOtSy24ttSL9_mAP7DrxXzCwrL6EaJetk2IQMo21F9HPcT4BrJX2VYSqvkySKqnmTdKNpymF3k6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=AGGkn5QADNm1zTolrowqfrYI3qidsXm-xM6YBenOo6j4c8ZCNA39Ge2MbBw5_Qdjn3FKf9yjH8tP0ZTzEnv3wH-zRc0PUNvmrT6cf2fXSvduCUOwURbhjFGcXQsNtKVlhUemlLIFbaqcnzarRZeoZcdqEsZBbtASkfx_T4Uc5oUA395vNRS1SSr3wQi9yrQ6RDPtxukzaS_qMT3Q_aGZLP7HhUMwXWslpvyi_eHrQFUVneaLEf3oYcR_dpnXlPeF36rSI8eK80aOtSy24ttSL9_mAP7DrxXzCwrL6EaJetk2IQMo21F9HPcT4BrJX2VYSqvkySKqnmTdKNpymF3k6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=pULorG04XKhdtcRCO0_ByO2t1QvD5KmJLaEIvJGosBqwegnt1SEhw023pzlUyDijxcr48f1xfC69bF8oeqOd_Rqt8A0-Zbq4zo2Oy2PCM-Xyuv5_o0IkwbdxepvWLCpzzr55-_8Gt2D304RhmE-BAdF3mArCVKHUKwYmvF34QHIv5Bqg24GDhXofgR-JXnSdYv1PLMae7MNY69oc1CoacRLuHPyaIlXx74tyVzHEYLc86-KxFW3RYBI036XYajpVVCpN083z-9W4GBoZ87v4G7FFYMhe-BlMBNQbBsE74VpJg3ms-Zo13j78N_zBb1UF7bKPszIbEOyLjIImS3IFAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=pULorG04XKhdtcRCO0_ByO2t1QvD5KmJLaEIvJGosBqwegnt1SEhw023pzlUyDijxcr48f1xfC69bF8oeqOd_Rqt8A0-Zbq4zo2Oy2PCM-Xyuv5_o0IkwbdxepvWLCpzzr55-_8Gt2D304RhmE-BAdF3mArCVKHUKwYmvF34QHIv5Bqg24GDhXofgR-JXnSdYv1PLMae7MNY69oc1CoacRLuHPyaIlXx74tyVzHEYLc86-KxFW3RYBI036XYajpVVCpN083z-9W4GBoZ87v4G7FFYMhe-BlMBNQbBsE74VpJg3ms-Zo13j78N_zBb1UF7bKPszIbEOyLjIImS3IFAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=a_A6hDDuIkbFoZdvwl6l0SXEyOkpLS5H87PW2QCHB9sfp8x5cUuaETTClGX54ZZTSXGT6bnIQFC5bKIY1NcXMxuz9A7vrxns53sZvWXLvj20VcWZSFk1pxbLr5rmzRikEjYLFG_8o_5ETikP2fo_P9CJRQwpIGj2clekJQzxrWfQWmRSEZButEPH1K8d9zT0DOlNGxG_9NW5YmbYhjSzd8d7fo_HdfQ4P7gt6kr0VF3rRb9KE5DYUrLkqDp3TVchDMkuMILiF4V3jI4HC-tiR1-dh8lgR-BSIprqSJknryjeA0mVjYig5j4FkqjR-9yIJixZR6OgLNKr74BFevhH_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=a_A6hDDuIkbFoZdvwl6l0SXEyOkpLS5H87PW2QCHB9sfp8x5cUuaETTClGX54ZZTSXGT6bnIQFC5bKIY1NcXMxuz9A7vrxns53sZvWXLvj20VcWZSFk1pxbLr5rmzRikEjYLFG_8o_5ETikP2fo_P9CJRQwpIGj2clekJQzxrWfQWmRSEZButEPH1K8d9zT0DOlNGxG_9NW5YmbYhjSzd8d7fo_HdfQ4P7gt6kr0VF3rRb9KE5DYUrLkqDp3TVchDMkuMILiF4V3jI4HC-tiR1-dh8lgR-BSIprqSJknryjeA0mVjYig5j4FkqjR-9yIJixZR6OgLNKr74BFevhH_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی که گفته بود
به خاطر هسته‌ای
دو بار با ایران وارد جنگ شدند
،
الان با ژست پیروزمندانه! میگه قراره
در داخل خاک ایران، اورانیوم غنی‌سازی شده رو رقیق کنیم!
یک ملت فقیر شد تا اورانیوم اینها غنی بشه، دو تا جنگ راه انداختن،
حالا میگن «در داخل ایران» میخوایم رقیق کنیم! ژست پیروزی هم میگیرن!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5536" target="_blank">📅 22:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5535">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9zZBMHhcsPOG_QRyTmLAaHrrFso8sS5yW7es8CczxZQD5LMWhB-6Z3Uq9muBuwtDdm6JspC_kqzQaaXX8XDC7W20aPsUghaIG55XUJmtu4yBoCT352BwmkZp70ix_aUAdPv6PKFCJ_lpiBQLxFNiLdpsBcUBBkGiFJx0Pau2_D5qixhblkPpz0o5KS9ezL9oVs1yTxmuGXkVJ3eIzg6rqXT7I2eV1-A70kqB8eeKdvw1VRALfEQzbJGsOr1dOWPFaDA16ogJNNJqL93KdrPn_kx7CAHMME2E6HqBfL9KcZfC87F7Wu3TZeGVuxLRxoXww5Cez6wLIb_pC-_145w-8f8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO9zZBMHhcsPOG_QRyTmLAaHrrFso8sS5yW7es8CczxZQD5LMWhB-6Z3Uq9muBuwtDdm6JspC_kqzQaaXX8XDC7W20aPsUghaIG55XUJmtu4yBoCT352BwmkZp70ix_aUAdPv6PKFCJ_lpiBQLxFNiLdpsBcUBBkGiFJx0Pau2_D5qixhblkPpz0o5KS9ezL9oVs1yTxmuGXkVJ3eIzg6rqXT7I2eV1-A70kqB8eeKdvw1VRALfEQzbJGsOr1dOWPFaDA16ogJNNJqL93KdrPn_kx7CAHMME2E6HqBfL9KcZfC87F7Wu3TZeGVuxLRxoXww5Cez6wLIb_pC-_145w-8f8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/orI9aJfx5bbS7cpeiWMTk-yMarytIAFN7Xhil7f4pz6oKbn3qIRl3dheExZ5EYmCgJYq6sSuDZJaIU5_k0G4sIFyC_ZqSVknQ54tcudRvduuyDT2h0_Fv2kllFBBtfdhOfD2-cpMAVdVlm1so0zOiDD5Oalx5bgYcx_9yKAQv7E6LaGD97qKRAKkS6Asuwogjp_x6kOUNAbN6LA8jRPxzRdFEeVKPKi2da1Ht5C2sAbvtqJm6gF0M-HvmH9cNraSzuQwda5ZtDOSP3DjnajaZRwJMFKilJr5NUSEESjfYFex-p8tf0jZSDl0NqejKI3cQrCfpEvuF1DXuMp3GjHIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5533">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=FoPMxU7rwnJFszGF1DR50rZCSF6J83obOqhmr-5kFLfM7daUjhuf_6mzly0JAhFzdyQpxLz0UeFznHdmYBZYWECh87mvJbO1sWGavwnwoQlggE_QlRDnz2RV2Lmjc3xRJp3RSxYwndC7jacKB2qzzvBWr-HNeZGfV0153NXaze_OLtOxJM6-KzEZ5NiEryxeHcZGmXr_0OJLbQGDI6nEG22eAyP-xU_qScu8Zb5OYjOkYoYVtnH8Pysx_3o36rZ-nAc11GFJW1FD_ueghrQcLIfudOX_lYMpqiz0yq0EVPmu3G-QPQf2fGk8F50H0onRh_12IhAMOJN-kP7dv1h4oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4506bacd1b.mp4?token=FoPMxU7rwnJFszGF1DR50rZCSF6J83obOqhmr-5kFLfM7daUjhuf_6mzly0JAhFzdyQpxLz0UeFznHdmYBZYWECh87mvJbO1sWGavwnwoQlggE_QlRDnz2RV2Lmjc3xRJp3RSxYwndC7jacKB2qzzvBWr-HNeZGfV0153NXaze_OLtOxJM6-KzEZ5NiEryxeHcZGmXr_0OJLbQGDI6nEG22eAyP-xU_qScu8Zb5OYjOkYoYVtnH8Pysx_3o36rZ-nAc11GFJW1FD_ueghrQcLIfudOX_lYMpqiz0yq0EVPmu3G-QPQf2fGk8F50H0onRh_12IhAMOJN-kP7dv1h4oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۹ ماه پیش
بعد از جنگ ۱۲ روزه و قبل از جنگ ۴۰ روزه
این تهدید پذیری اگه به وجود آمد پایان نخواهد داشت.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5533" target="_blank">📅 20:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5532">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAXwWqS3Gs61vAqBuQSXiUWIK1gA98ylIC8kcnAUjhIOlP1TkI9G7uf2K0QCd4TudI4a4EAcP7HPkrB1uK8tFzfAYBtRI1NpcP7UpOC_DrtATH2rC8IqGDkllorSPySlwZmrgDie3fMWP5w9iEU5hzijAER0h65Gl853AcB5TVoMGYIZoyh7rsZGBaepYtPq1dbVyhTaZ-E-Ef6qtsTTnz0Hp8KSJaUXMMQ9A6Lo-y2ghAiHS_znKU4IwDwNuENbLxCt0MEb8fYLW7TcBP4LPYUIuXq12tvyxnrYGVYmNDiofKD24k0-CHoJ8_iI5tXAVbZwMsCjWCbVIXR3A2syuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اکنون:
توافق فردا امضا میشه،
هیچ پولی بهشون نمیدیم.
دیگه به سمت سلاح هسته‌ای نخواهند رفت.
تنگه بلافاصله باز میشه.
بعدا هم اورانیوم غنی‌سازی شده رو از زیر آوار
و خاک بیرون میکشیم و نابودشون میکنیم</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5532" target="_blank">📅 20:32 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5531">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGfqVK6rrC1gy3esrbw9KXlsdzl44bDdMPZP5ORFzhF6KcU_jSoNcEiQiraUtsi6fk7uLWGBDo8DHLD1K4RinXUj91I2aiOfdANn9NCuD2OuQHEzn3hm0KosGGKS5zV9H1GfjI20-anNoicwioO7VKYxBpvVpwCYg6gCi_b_glY_61OG3VjF5uzhYgDA0QDfD82mfXyUgbWLbESsXBAw-iA-pC-6gsj2C03UTm-3MNmdnkm5ZqsQVpi7n2rK7Rhl32EP6wAEXNKfXZ_bHcYNI0wChYyK0qgyQB3b8FaG0S_54vsj87xWgq1hNBIkp_Is-XqjL1_bHVWyKbh0GKwTLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیسی خطاب به قالیباف نوشته.
نگذارید خط تسلیم و سازش با
قاتلان خامنه‌ای به ثمر برسد.
(نه سازش نه تسلیم - نبرد با آمریکا!)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5531" target="_blank">📅 20:09 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
