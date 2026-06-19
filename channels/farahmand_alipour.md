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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 21:45:51</div>
<hr>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTb6ll6mo8_3poAwGuJvYlJQ3J3CPq2Bncv_Y9NIZS_6UDTcd1ZGicb7AcxviInTJwGrXxrPiBBFF03i8X3MDBWYG7kTPr8niwfgjMhmvix0FM38ZL-Cg8MnsYhidZ7ZNg6LVlZrdwho7Vo3jIlyHZUVRmK424vset_yaUUeYybw1Ua9nSJAW-pmrGlp_FAUuNfoqD0990XKLxk44Xp6gDAN4YX3lXzwT81kny3GzFwy3NGREOBvw2WL_kqvCS4ZApJL_r6Tp9viK1WyP8AugN4DLnMYsXckq7C_5vm8y1XSe6PSCDXn_MruWZFQLKttPMCnLuk54NxEkXkssL5z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOzU-u4qrvknyaI8POmRHrvIAFwk_1hiYryDngCoHXGHPI4RHGyzuQLILziOkCVIWL6fe94egh4Dg8ljFE1ItJP85cB_iY-6aEdqOAendQpRIjRo_f9_JEqo_NQGOmY9vMh-oYouVRMVqCazw6qdnghM0Co2pMwfttacz59EJUrfGPsxrwH6kexYF-RkUlB7l8XXC-fRiVN1MqC_eDFR41wwj1b-3wBAHfKIEk--h5_ku1XYDBKova-f4xxasZH83srQc4EllQ0G_tdBjZmdroO_BkQ3Z92oLCz6nvmpmvpenTwrG0OH85R0PRU37MIvRNxOs0Jg2MLU7WDk1k6vRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=WX2NoFfr-IVtWX9LMI2VRv1e64HxnTyaTg95AcYPKBGfP84YX6Nsg0mMHiiZHlpGvH-s6QLEvoyE7Fp7jOAiTljtDqTPepZosX-rAp25XkIo5Gg-x-FO2C_DO68DmTTna9VnBo4HxvxCQUvz355JXvRlctYOmPcG8mPzoNTVu3UdtQFZ2Srd9qWHew94NhCIvSxSMCfnm8eA6B5Cgrk0rrsSash0UbLpVsK37cjML78ec-Q9OlkyWmU1fk_q7qEDq9r6P0C9HW3JvVR7PXeKuj-rdzcMmpU-780XgPdrcKq8ydvbf_UQ68OREssd5CYkLCZ35WaWR8xNijmd64KpSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f791b65d03.mp4?token=WX2NoFfr-IVtWX9LMI2VRv1e64HxnTyaTg95AcYPKBGfP84YX6Nsg0mMHiiZHlpGvH-s6QLEvoyE7Fp7jOAiTljtDqTPepZosX-rAp25XkIo5Gg-x-FO2C_DO68DmTTna9VnBo4HxvxCQUvz355JXvRlctYOmPcG8mPzoNTVu3UdtQFZ2Srd9qWHew94NhCIvSxSMCfnm8eA6B5Cgrk0rrsSash0UbLpVsK37cjML78ec-Q9OlkyWmU1fk_q7qEDq9r6P0C9HW3JvVR7PXeKuj-rdzcMmpU-780XgPdrcKq8ydvbf_UQ68OREssd5CYkLCZ35WaWR8xNijmd64KpSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی ونس به جمهوری اسلامی:
گزینه اول:
به رفتار خود مثل یک رژیم تروریستی ادامه بدید؛ در این صورت، به معنای واقعی کلمه هیچ چیزی نصیبتون نمی‌شه.
گزینه دوم:
مثل یک حکومت عادی رفتار کنید؛ آن‌وقت آمریکا، برای مثال، به قطری‌ها یا اماراتی‌ها اجازه می‌ده در کشورتون سرمایه‌گذاری کنند، البته اگه خودشون مایل به این کار باشند</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxyJKAnXOSntZi3sOwYR6XnrhJBQOwOTeY8ND3rpGHq-49Qce25RVtEpyN0Zn528Q68yxOwVkuEnPlKQm3A-TruHQt5Eg5aY1Gn8s2p9GyoxVI4K7hXorBOtCCUolwJVG4oRbU1EZ82Rclp2RH6vlBFZMhcGa0kXGvGtBfGV9bXIOKLEdQrqTY0-Tc1llzqK17iG-rQvOEzsom-GEbG7djVH6Q5vlp1tua6w4kKUvQ6aitaLgJabdd9FzelugCsOJqTV0T0mi0alYy7BHxgv35KthJLnaZYsHbbOOyosdbGvprVCZyixsxD6dLu43eFUr03bc6KfQ6_md4ZfdTk_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5nttENIgEfiwZuj_Reb3t1GJDwvM9OmzGMHBQglcOzJZS7osKp6H4gyPbq8aVf3VEpPlaqdLFGdpugxzWYPC9xIqgHXk7NOM2GvcIyxrOrXfWlYv824aSDBRVOALtBo_-scHBs-rAD5iGr4Z6ZVgBzZNRT__f496MlvWQld8b7LXW_gCr64LhxfrHnvugcxUtiD0ZIIigvohWvnFiQ7lbpW_TxTVCcTxzq97jvA-I1pdz9Kb9NpGk_iDKZaEQJctakHwuXRsOEaNY17-tbUnipccH2djZz_TJwUgrr3mW7Njb8b-_CWxqHV5QeaVNyXImjUppOS-9gZlaeHFDuxAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rip09e5DCowT_2bgFM2V4mdcdlYvac-ZajIMtnS1p7qAA4rl37ZZjKlmHja6D4J-TFcOE3Ez_PNFEfOuoPs91wj9k54OW1JNDAFu-ZW7rNUA_3Bgh2FawlbEEYS8tqxo7cJY38PR_WJtmMCcfLV1wfZphVB3MZbocNKJ8086bPKPaZV4T5N0vzKpZRXSprtwa3OS_-fkWsPwv_e6aySm0AW9K1SVRf95N7vXfTYo0puM8tJqpuoXbi8jFGOmRLd3fZpBVewUKc4I3MPIX-TVCK4gpKjGdeL_VuH-qzYqGsVKKj7GCeHIkFpTSXWvY3p5AJ2OKZG1g3w4TYrTpu8BiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvKU02dxYTYH7ce3t7cDFcG3HV9e_NbL6ahNpiXGYwa8j-eq8FB0mqWk42AG50HpkT2MxxU208YVylXzsaAOBw4iP0oePiOaZYkSdOsxFPsVGPviVd-6AQP4pKhdL4CbqyQkX6WOlGuNzCc4q88zHIddaQ5jHXPwQIgnx1tatD4DR4ThilxwAL3O7q2wtVQoe1nBWO-0hW1CbTZUcgmTqOYPQHFh2IBg3vUGa1Q91jEQxPRjJIJ4Gi5WAR5n5nT93pPg8S9NSUZtsNkMmz_7Yqv6XN-PvGqjSK5UMxb1u8_cAO0tDqpjV5G9OBWT9Id5TdCwZXb0PM8G5841ebq-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNnpLhEXscABelH1di-uKvhA3Q--JovL62N-xbeEfSpMd9f26hJ9_j8mjoAwLEzHm1pLoKn8amllc6dvSDxfICAFsJrImqslXO_1t11vgUCoRK5_k2zNDS9VbkiiOdSTpzSK6Ysfpmg-A3un2eVIOwLQHI65pzGSGFg68EmWVla9KKSs9CUNtuemXJ8KL8xNFgv_tTTMYNEGcLYaq6_YcD5v6n4NsF066I9ujDyewD3ghgNnFP0aN89A3cgMsbA7QDBUoyzB4vfDn7X-xL3lj7x_JB-rnHhujVf-Sou0Wo3iSVN-Fwv9h8LXBThbOeXa1CmSbm-wC9_VFNGq0xEg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=XW4Gw6WK6IDsj9WWu7Vn9XSyDx-rSU5khNhnMKM5VinWd2NeIa7dU08Vc10RvPj3woq2JrCqQaJ2PjIP5LLFaF-bPZA-ARmXQepQrC7NZhxOxRtL3aiBXv_ijJCbIgYDg6keUoxUfz6HOX1fdmHfwZTQvaXby_NY9GFteArowaD28XEmh2T1Cls8SrbEJ6CoijlSLrYxgLvo8ZRULOcUf_jjVxPG2DhYy89vYf30P4RHcmYHM-3Xoo1OaIheNDJPQG5BDjnKSWpMSajXYe0FrY6kCs7SZ56vWzwB_5J1nGPjr0hdGRcbf5xi_2tAkccHhNWCyhWWmiXTuHdWCH-W1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=XW4Gw6WK6IDsj9WWu7Vn9XSyDx-rSU5khNhnMKM5VinWd2NeIa7dU08Vc10RvPj3woq2JrCqQaJ2PjIP5LLFaF-bPZA-ARmXQepQrC7NZhxOxRtL3aiBXv_ijJCbIgYDg6keUoxUfz6HOX1fdmHfwZTQvaXby_NY9GFteArowaD28XEmh2T1Cls8SrbEJ6CoijlSLrYxgLvo8ZRULOcUf_jjVxPG2DhYy89vYf30P4RHcmYHM-3Xoo1OaIheNDJPQG5BDjnKSWpMSajXYe0FrY6kCs7SZ56vWzwB_5J1nGPjr0hdGRcbf5xi_2tAkccHhNWCyhWWmiXTuHdWCH-W1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=r201VltzuQbNkZvcfvayrEnAQmByDB7We05x4jOsQb_IBTmLcxYPeBW6lwn_xTVTUqm18wWB2AB2m18g4I3lozL_zRqw92ntuM2SDc_BM81bDrSMLcNR16HiWvrUeUQPOGIm-BLhuwP5NxHwYHbezldmpF5Q0ms2GgbrZQnmFXdSO3AoeGi3F2NV-tsEYvk7q_tHK_YTWgan34NBJfxaZiHxVn1RpXpVKblNxMuF23Tdr_Ho6qlnrgzB3F6PXKQBmbpwD5HI5qu6caFeadpdyQCOeJiSeqvj_4cr0VCW75YOMKonO8IWHt_nmQf0-oTyDyO0EC2jmz8noRcQ6LtY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=r201VltzuQbNkZvcfvayrEnAQmByDB7We05x4jOsQb_IBTmLcxYPeBW6lwn_xTVTUqm18wWB2AB2m18g4I3lozL_zRqw92ntuM2SDc_BM81bDrSMLcNR16HiWvrUeUQPOGIm-BLhuwP5NxHwYHbezldmpF5Q0ms2GgbrZQnmFXdSO3AoeGi3F2NV-tsEYvk7q_tHK_YTWgan34NBJfxaZiHxVn1RpXpVKblNxMuF23Tdr_Ho6qlnrgzB3F6PXKQBmbpwD5HI5qu6caFeadpdyQCOeJiSeqvj_4cr0VCW75YOMKonO8IWHt_nmQf0-oTyDyO0EC2jmz8noRcQ6LtY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPaWNmtAmIcVVdN4Np0n495OBUtBp9vIU7GVWkyrEQWYqz2mF5gTPAXWmIc3VcxwF_4WrwO0yaq_L480c2oWZJc98GZugjRtea2DOx7b1QANtDIZOb5BLXph5oZKyXvRAGnWVJvbayrcmCA64kpjVz-4GtqpGpN6iFhFRO7xl5pdDqni1F_iHS51fwtxoy-JqwxJDgPR08VuqFxJLo9N6Ha-SQUdsyXDb-EabemFUHVNxbTrcW1tCUdDlMtRltoAS9vMKoUxodAOveRSdOMaMK_VbMrbSk7kz85GlMPOUB2POTGCa1VgcNNeDywzGusdsD-_I3QH3w0yDvYbTPXkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY46CnIybLWW1mW8BLpKqVDtz-UJbIwI8fcqZWCh7qKT0nNaHvIkbcjgYtU1hgVWYeT7G0cT_U5BG5tC5ajfdQPUG-Z1igYe66X2Zf0jIsydyn7VXorg4GVtOt4T7E9V9IKbR-nxO4tNVW7AdIgNyNAMpzQ489PSUZeiB8zm76WDJ5yzyQlm3wfoJOJm-lk4si4qB-WXL9UgVcD-vTwjOB5swNl8OLh7Ws_Y1TleCt480vOWWfFMAdbL4GZHgEgBHtyPDBQkKQMv93Ii8pz_-FAQbUfCedf4T6NaZ-go3wrPVUfNzCdP7ApBqPyoBgjqKw7GU68kpD1bd3Je0msC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh99LCTwYnsTyTnlqFnvtZzwY5LKBUs8tTka5xttXWkjoDPPNXgaJhEjTmSEquQmmpNVgGRZ5uF5wOXBghdcCF2X3I4e6LHGs5NXb5-uyrYaTspnsLUPYultGCPBacinXcqtAlJXW8fGP8wM8eJ49mFmqRGwDvLDaK5yDW6IHYG0JVpryuCocGJuYXhnx6dOkTtCKnYt0hk8tEPuocITjMRIWRXil1Z2X6IEgb1LObvmaE9saJkOqIZq028DhaPUbbRuwPVMRXoMC5GXtPeZn5G7lET0e61ncN9LXVKCaN5NTYOsV1id_m9lox1Hp0sF4sOjfNc9LByGgh-Io986cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNaEnmYixfZUsj8qZho5tbGaEq6mrjKsxHkhcmvm6c_7z8cuIt9S-6wgRffdj-Mynsicg0kx3qS6ue1jExpkuOSw6X-waoMpUXWGNQ4aUsFdGnkxQoPnz2FI5kLJhvo2pTVbp5S9LSIzrkBH5NKKPiQXy4guMrN4yjxduYxp9i6uatijnb8i19-_5paAl5lKim_jw4NZxzMICNXeEb8YhSxXMjQ-n0YtDS7HLmVxIB9psZaMJkoWmk7SoHbtx1YyzxyeAUM7IohOPyDPtQJ7OcTdI9ru2wzeoPhv6Z9Wa5QuQ_kRdUWRS4_30Kd7Rj2O_YEZvAkcJRiVIcHuQAfwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BJ2zZxfnkMNDITMtNtiJdMI0rBt_cuIKIMyAfQvAN5fPRtxVpM5kRcDSXjSyoGTbd_xm6-Xz9fsQVHPjWis7vdp8xQyrZ22GVXohviT3yleMjWwwZO8Uo5KxXUK4zoQ6vDLAc204UQg8ZnW4WGcWV76etpNCnX87pTgTjGJYnwX-lA1T7UjPHfvABBuTKUwyBtMIhuymK7FF6bNomJSSnKOJ3xPWyPxnlhogUnzMBc8yQ4kYjNVwyavJ8CDxFEaiYLNdvtxRzsYc3TBxb05TDC9uxQNHmV5h7zTpnntkPCZ2FQi8hYiyy9V4nFihvOAkv4-kUVnmS5b6nslk0VflGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=QLCogIuiYkfx-j25ar97eSOU9ihbhAxGdSc4h5ksdB-7EbJvZYT1fqWOtb9llnmb-riTzdu-FtvaBrDcnjsiMwrCti41k6DXky_XjDJ5eZHvzfEdoLgUH5Hu8aki1emNFgc3XpDOO4IGA-E9ojnfgYYwJRvVZ-cnOQ8FP3xYVLUWlVluo4VtVcN_BYQv5XmbVLhNcm_26zOaaqw64wf25jrzQZDOOw2bRZJO-_MuVa2ujalvedXA3U0rhbobf0NOfsoWXdk-ioLEllqCIfYnr4PPdiEumi0R3-hNZylSIUC9u_QOe-Xe8eJY1pPOqqbTF2zpNgo8LPMw4gjEuB3vMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=QLCogIuiYkfx-j25ar97eSOU9ihbhAxGdSc4h5ksdB-7EbJvZYT1fqWOtb9llnmb-riTzdu-FtvaBrDcnjsiMwrCti41k6DXky_XjDJ5eZHvzfEdoLgUH5Hu8aki1emNFgc3XpDOO4IGA-E9ojnfgYYwJRvVZ-cnOQ8FP3xYVLUWlVluo4VtVcN_BYQv5XmbVLhNcm_26zOaaqw64wf25jrzQZDOOw2bRZJO-_MuVa2ujalvedXA3U0rhbobf0NOfsoWXdk-ioLEllqCIfYnr4PPdiEumi0R3-hNZylSIUC9u_QOe-Xe8eJY1pPOqqbTF2zpNgo8LPMw4gjEuB3vMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=hi97VRcYTffUJa3ZwXhvjFILZ5whgL9rDlWkXxwhNU9MHVLivcczn2K9ukfckNb1YgKT9Elm-Nh12ejZYNFD7pxYL0VLElGDPMbduXw_wbtOHR35fLYdxbOaDS5PgVgmJcUBnnBUIHwMlIdGlijXTCiILixJUK4z5KQSf2kS0p5oY_xvkjyerilM2moXQ9-PEXBdXnU2bl4MRjxuMcwksRj8sUXklU0bvHRBNl7Wa-jtiZsVM_zC33SB-2SWc8Gt5ftPodj4Om7zCYMpx9NrHxUJCyPxCnsetz3gUGB5ZRgkbo-HZNl3u3j4DUA9dkmgM9FvwuHVgkelNb0NnU9QVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=hi97VRcYTffUJa3ZwXhvjFILZ5whgL9rDlWkXxwhNU9MHVLivcczn2K9ukfckNb1YgKT9Elm-Nh12ejZYNFD7pxYL0VLElGDPMbduXw_wbtOHR35fLYdxbOaDS5PgVgmJcUBnnBUIHwMlIdGlijXTCiILixJUK4z5KQSf2kS0p5oY_xvkjyerilM2moXQ9-PEXBdXnU2bl4MRjxuMcwksRj8sUXklU0bvHRBNl7Wa-jtiZsVM_zC33SB-2SWc8Gt5ftPodj4Om7zCYMpx9NrHxUJCyPxCnsetz3gUGB5ZRgkbo-HZNl3u3j4DUA9dkmgM9FvwuHVgkelNb0NnU9QVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NpEVmFIahyeuo9bw2abzsnAWN-kr_NafUgfwNXtt3JerxW6XpfKUAWIYsWvjf_haOejplwN2236iW1ooQfHArYLmnQCEFhTYzt3vAm0p0Mc-hqb8igXfQbY50bcSEdVaOoncnKGLXVUMnrywSOWn4Frd8X-txLMi7EMpoxFLPmpBxVFiWiswvJSQn8vO33dhFw0yRMidPtMCs95RpyXoCpphj_29kufNfROkg0LJT5Jt2_wmnYdo525BIxpaS5HLPtPNw3bJB7Krdl6w4i9PxNf9q9nRtTqTBGe3nAW4O7VTKNoMf1bUNTxUXUWt0z2iTgvC0z_4DKy0UB4XubxRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr2Im1Wha48ufzf2KuVHjRLn2APjYIKIsVCj2oLtxGv5FZOe4RUGATZsbDLYku_oFTD7c85JcpjCD8PoqRQXtfVYvR6pCN5DPCUyrQiEI8hRPRPUiD13yiAG-LoNdYgozeacDUQkm8nLlFWdQjn9vsJMnS4N6j2HWED3rdXvUOtLnPmSJw7keZfLWVIX7Ki6wemd95RGeKbHHOTrrzMtNeFWtVbxLj9MK6f9__V7n2zAzUjnEJTOfcmoW8raTMOBe6njEM5_LpdCQjYkreDqA8C972ihoyKuDSss7T2Bzxsib6p6laqMHpJaAVL9xDIre2vNNMd1nof7xzoLCXjd1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfe3lt-4GaPthNAIVrRgJGCOJPbHriQWJWIDiERIyfLMyHhHapcJMBu01Fm_fT4U5YdFVoLtPCQxue6tCrHys8o1kGSSHR7nHSSJnaTzudu4w6QzIUWPGjV7gGBuCiDFw4rOPecP430XcPa9gbX85Bv1fC06Dirmtv3S8ZXAGZgbcPMJhF83RcicqRdk4uQxH1RB6P2yyrL9q9eDR9HC_jMHoV57v9-ckwbkp3ku4cQvxR4EVL4M8U-T-PFUV_k18B4yCKvyWIxuoJakh2MKHjUB9XFlzTJs5EHyBlRENCgAHDg3X7BTbgV3jyss2HxSHoxByMEgiGsrqHW7El-IJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=gnynrD_vas0GwC-Ze3ANriaDQ7OXCiDH0fIO2FJ45qyZIIOcwj5Bnz2lvP3SgBWvbfgzALgg9TcjT2JfE72_nTN-5cucpUCjpYpiegELIotxEnoSsmxU0-6FWaDi0J356hZLVQ_gfqxjG8VG5bGcRupn9jTYFYSa6vI8r9nh_Cbw4TeVGBWfbkjr6HjvsujOdegL_yNiGTTEpra3D7wXULnvMHXZa6fawOF8Z9zOao41_2D1aBET0Roh5lyJqKBDpC5ptPaGCEq7urNIaNx9WzYDwU64DC7AfeQG4cPt3WqXEcDCmXerl_iHxGx56ANaJDCyaQ-5ktyk9HAOaziD2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=gnynrD_vas0GwC-Ze3ANriaDQ7OXCiDH0fIO2FJ45qyZIIOcwj5Bnz2lvP3SgBWvbfgzALgg9TcjT2JfE72_nTN-5cucpUCjpYpiegELIotxEnoSsmxU0-6FWaDi0J356hZLVQ_gfqxjG8VG5bGcRupn9jTYFYSa6vI8r9nh_Cbw4TeVGBWfbkjr6HjvsujOdegL_yNiGTTEpra3D7wXULnvMHXZa6fawOF8Z9zOao41_2D1aBET0Roh5lyJqKBDpC5ptPaGCEq7urNIaNx9WzYDwU64DC7AfeQG4cPt3WqXEcDCmXerl_iHxGx56ANaJDCyaQ-5ktyk9HAOaziD2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpDyamzNN_kodBx9suFIxXKtA7ivxvVjN4JZN6iIA5tjH1x--iX0GRm7XMN-m6LtoPKHcjp7Imjx6Ssb8lFZmIk9I2ZKYg3nmECz6e5CbrTXSrDsXQbTpOMby0q1c8Y1OvSliVRfyX8PNFPfhz0BQ2WDLD_EFS7Eq4yID_xqaz0I0aa21lQypD0AEUs9Ebms0vhSJunbzXdFU9kyp2iRMMokR6zpz5BAtMhUf2cCP4WMXQb_zdiBpGgf7e7-iSu6XEmVX-0b2UA5i49JsraAyf1d2e_h9CbzV1yYPg_SkZymvE53VFgUp5-VIQKg5PK_li6uPUChsEuG18NJglYuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2ZTP9YQH9zgMrNGSodxF8wpBlFgk90QdYDNkYz6fwz5vFimuskyYB29EGcthT8sqi2z3zNFPD-vcp-9USGNbAxlBwAkDCEdwOkaGB7xnZuCt48zOBA3SXSXLplO2cnaVmqC2iREGwJ-AIhscahDEAcarcpKgpBa0x4S50pGc3mqWTLRMm2UYAlfbVY3OEAY-o4KuvFQXDVi1jNyl39duBYCEKoAe_MPXCd-ON7C2S9Chs--qJCJRa2RVAtULG1_0exIODU9E5_Ai1LxdTWbu0_gJWYlJa4Jpk80sha-oK0vtpz6Makk-Q2-VEDbkDfNI56DvBJqCEvJ0HfFIMNe4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ5gmkbet2yJXxb95laQr9n4ucLzjd253OmtnP78gqUycU9gcfbKaY74epAGNMKtCKcr4tFuxs5XGpHmX4IxFdL9mZrrEYKeOLtmM6UisufabDSMfh7lAQtNzreGipCdo-RJ0r_TWcJDKKTUua4wje9M_V8jz6k1xcSQMyAtOBsgcNxNV4Bnu39_brbEM4RSfbWCgejQ9Kv-Ifl5jp0p0m345Ij8IN4VN5qc7EqJSNLyfPm6t2z8L7tShqkvA20WN9uHC5gG-7fiiNCIpW7u6xYmqVYizeBU7FM8JZhHDPXUAUoPgBOWi2WwPD2g2j_XoYnf7uEPedrxPW6gHe0p8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbNnV6d7HqKbUFKRGijtPkFfcSuDowOhMfvuPVCPo5N0oqhk4NVnL58WTR85oFOMToP-QctDWF7VY7Ujo7vp8x5pfXRG-q4MCFnhcaXZsWK8y7Lwc4tn6rtSbCjWtTOA-Qiih5Ho6NrNknI8gIMfRwCor2wGYIiLnNT6-ErtbjXqj4YW4QOE5KZKritcYMjQxvHtd_LIlYxXxtr6iV0gFtP-2ExO0ArV5qLXAumV5U0vDekk-DiIaEDSlONEmhgor4UE42b0bkoOHvir4MC8oxtgp9H9NGndSL2qlhOoZZnv0xa5w9NPjaMp5IiXKKVvBNnQVfMc_GsyQhEShkh1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=NWxiyOaGGe7G_QqHQu-A-BFQ3vNuJ7_Fur802BJLJYu8WfDzA-kA4xqvZGz0BDBMLkgGi4gc6fZJb4Ut0L_shfnbfmOylrI_rLV7gg6A9hx8trEt7v2MiY2dc9nrqlLU-R-AknhWgEp5J17eh7_RjiSiYah-i997_T6Y5gLZQkYkhf4TbskcBjdKiCabIboV0P6TsFCWTrgnpK24ihx6dUZhbyJ1-5IJDp6GsqVr0XbM9raOCG743SEeaFBn1YvltZFMAxoTkdj_WDjHcRmGYngrdDoOgnQiNAoEDZULFPtoXXhE2DSPywxQ3erVLw0119Ruc59oD-qBL2Iob2JOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=NWxiyOaGGe7G_QqHQu-A-BFQ3vNuJ7_Fur802BJLJYu8WfDzA-kA4xqvZGz0BDBMLkgGi4gc6fZJb4Ut0L_shfnbfmOylrI_rLV7gg6A9hx8trEt7v2MiY2dc9nrqlLU-R-AknhWgEp5J17eh7_RjiSiYah-i997_T6Y5gLZQkYkhf4TbskcBjdKiCabIboV0P6TsFCWTrgnpK24ihx6dUZhbyJ1-5IJDp6GsqVr0XbM9raOCG743SEeaFBn1YvltZFMAxoTkdj_WDjHcRmGYngrdDoOgnQiNAoEDZULFPtoXXhE2DSPywxQ3erVLw0119Ruc59oD-qBL2Iob2JOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-ogDom9r3k3KVsRUQriGQpqrV531tzEHnem1Ezjq-tPBXOzLpGcEHYEG_OICfqrdfhih5feGez03Qa_MZCW094I8rrMN2nGFxH_mB_DUr56L8pm8muHQQqWvBSfyZq1SnIqlX2qUqqo4xZI1rulRJ_6VPe9NUOd-dvRxOdUIrrHTxn6NTv423u_WOAO3iYYQMHppqmhQ8P18RhTGe849V63ZuWSpcZgss-Srrpwqlvbv4BXpnXyCsVBABEpF0kTnzLaxMYWAMuHbkzkUhiLLhJ3KyuzypGns1HCW5H4Z-REq2psH_BH7MHUH89SbwdxPvU2LIMDyudlGOVBhWf3qw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #56</div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlXUz_FRbZvim1af8wllwgUDvTOGNv2TG22D_reA4yclxGn-Ij0Gvc8akArcmNXD4u337LU3R5fdAmZpHY0TL9M5ssrNxPcbWrjLqEbpVHAGVDX8CR69Z0SLKzucXmOQou5zZqZGTN42Vk7GPpiFtJBEbSyTvoDtbP3RrtgeWZzNoawTK9WDLsstpBc4DHhFkkGKBJS6yhYFT32y0ORWAgzjNkzwBqgLvyXN-r49apRK5zEdzeB79NApuWDjydmNY_mROqO5tgGwnKRa1c74QA77hkiGZG0kDK7I1hvCYegEo2gycYxKFB8wsKiWkZin2-VuatJNA7Xy9v_AI3Plyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUz6yNt7qo413s45GTk5PlFUtQPCKrXpP3tc0bNUJXoxf0YC2NzsxSD5U9wpbC1pQQ7MYTLS1dmnpAuC6tA9L6AvMq6BeCywI8crG1oEOUsR5Tpmu3-vw8FtVgzVJrtvlVEWXus5kY2L0xGSmGGQrVVcayKWkuirGjwSsaroTNmlbfxiyJIeYow6uCqaAw4DeBeuxFk-XwC81zJPzR07pOHYQ6hpwI-FTydXZNlAN4kCiFJcc1TcFGaHLeqtJqJ8cz2fJJaDUxtRVYMdCY-w7r5lcCQfG6QNwshPxTRERPirPyBIkE-sPCgdAHHfp1x9_zx0vniUqDE1J7y09VLW1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWVc_4WBs8d4vlWnrQTixkKgVIdiZv7Qz1N_-IC_jZDZqkQHQvAGqHzxXuEW7JbjwwBWsRDZTzVZAG1KkWXrQL2zfzguYRAF0BzVHkHoAKQ4juOCm5dubi9p2_lGK0AcAnGZbwFDNHAxroYqFLFaOk8T5rUyhXKR6IQf9huhUc0lCCF3EJ_SaBeTK33PCQMn49Tlv0Ynm9IIINgZ7Qc1ejnnZ8f8W1asI4RCfm8ktTW7stSChFufEjF0DaD2dPYvqFjZI0UwWKh2kbIvMxgWnYJ1o6c0QzCgR_MgySMl9cIUmB_HzLFgRkPYIbjkgE8UaLwF_xFnbTtkq9garzu1eg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBAD3jrRBTJt1ImnlL8Yca9n_Y2aiMPooerailicUngU9ZLoZ7F0A1pI08IwX_Y4tD7lJVDRtx8AB6pIq7kRwzbhV5ULXkgspN4RiqmabEti9ZTuOnov09mYFKVrhp9ROz35ToQmwLuTl78GXy3wkkfqLx2kdvvzU1fuYcodLtDaC52n5w6nbPdbtWdjUWN9wMuq06u_ty_qw7JIGeGQ_AMOgSsXx5TvlAUKLC5soUuQx90WFr8Jj3hwbM12DAh0pmGh50D6Kch9KYX2jOknCRVSWEcGONnBtcb2hy6xtSXlximm1OjWvhR12qhGFM1nzzo5BTOOME7HfAekCuxVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijWC5NL3LuUkq0AvWzvgPdxa9-EfEZ4OxmcUJTuftmZHIBkbC41QhruVx-RvTFWESW2I5kP-9kdlBFJ5q39MlbX1yzBoF2vKmxu84rc7fYChXAB0aEqt2JemquPT0EAa1TrWvP9k2lknMrPxMPEyuB-0fyCjAOWVqRqqEnotBJJzMLMv2b8s1c-wpZNBiGJuysawVLFQxpD7jhLF7_xanYqClRA1WbH1I3baPgKCm5U0mH5Y--HWmtkeVIZajQBD5cVmXL3TmzWfEyKquTCXokNWJH7axxkOkAMt_bRI6EGworT1MhCYYytDhC_9EtSu_akUDet4VCDaZADjR-y7iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=mi1cnJm8Sq6MYbfZisS_DFIVeDFkGWMTlP10dSnnP-OX_E8NyofYbwBKQHwG5-VjzF0CYXcDC6yR9EPTcjkaoD8CDISxAJB0mx-DCS2MvpWr4JT6tsCMAvbVbqeMjh5Yjty2ilLgPWqofD55TEwNvdPl-r-caM9e5WOkWdBGVB8uFhGh4wWGNUzcpVA1hiHpSgcL1dkkmVTUlJnt04CitUh5TdC3q0x73CafF52sKYHaKY5u2Z0qt5X-o1mVBpcNsm4aL-UqttJ2VZq3KCoDYm0u1ld-rdm8ta17A7JgPSFeST_7vb_bG0Ps-0tqdbP3S_1nWFpD8LIfXsJSvmQpdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=mi1cnJm8Sq6MYbfZisS_DFIVeDFkGWMTlP10dSnnP-OX_E8NyofYbwBKQHwG5-VjzF0CYXcDC6yR9EPTcjkaoD8CDISxAJB0mx-DCS2MvpWr4JT6tsCMAvbVbqeMjh5Yjty2ilLgPWqofD55TEwNvdPl-r-caM9e5WOkWdBGVB8uFhGh4wWGNUzcpVA1hiHpSgcL1dkkmVTUlJnt04CitUh5TdC3q0x73CafF52sKYHaKY5u2Z0qt5X-o1mVBpcNsm4aL-UqttJ2VZq3KCoDYm0u1ld-rdm8ta17A7JgPSFeST_7vb_bG0Ps-0tqdbP3S_1nWFpD8LIfXsJSvmQpdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieBMkzzInSnX8JpL1iNEw1jUvQr07SeKmtjOAGPY90i5PO8vq_NKsG6-c7JhhW1BKLwSZBOtHE2L3HXi1opRW8Qs6pE6vI3ZJTQIdnaiBjbNfh6LmaM6qxVWCfid8jZ6PtfAdl6oN_LkKmAjMoi0j21U5bmtU9PMAyUMlIfumhwy3i5YCwUM4fzSawjXf-JXco6YYDxbXm1OYqHFZSfNq4Pp3ovy6KS5Ypmw7lbwBKA1SBRXC7hYF7BYf8Yic56lwmpQno_NkL0qwoCVilBwBRVWNH4QshEc5OOiyELov1d2iTvvUacDWSTEG9IXTV5JSkQZpv8Bv74MPY3upN95pqIE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieBMkzzInSnX8JpL1iNEw1jUvQr07SeKmtjOAGPY90i5PO8vq_NKsG6-c7JhhW1BKLwSZBOtHE2L3HXi1opRW8Qs6pE6vI3ZJTQIdnaiBjbNfh6LmaM6qxVWCfid8jZ6PtfAdl6oN_LkKmAjMoi0j21U5bmtU9PMAyUMlIfumhwy3i5YCwUM4fzSawjXf-JXco6YYDxbXm1OYqHFZSfNq4Pp3ovy6KS5Ypmw7lbwBKA1SBRXC7hYF7BYf8Yic56lwmpQno_NkL0qwoCVilBwBRVWNH4QshEc5OOiyELov1d2iTvvUacDWSTEG9IXTV5JSkQZpv8Bv74MPY3upN95pqIE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jw5vcXnOMEL5ywLW8VjhJL4GiDbt5oGIlVkdm_bJaQhoUdcgTAq6-gRGDDoAs9fmcrbq3vsDTb2oBsVhtsUYGJaNJ03GHVpAQ5efjmA0KNKRPIQpuX5mBv30IwRtpX4I7ukXreV6i83D9KQhuIW53uvb1PdrvS_9s3JxUmpn8VfxzMMp8GWRwX3h0x-0_-Op4UCOV8JRwEZ9h2JWmDYd9vZYwoqBRfW_JKkI08g5bSSNHWp98iM5MD9YcG6QLxaW4dmFW91zGa9RgmXbFwE0euBylmCZi0HJCgDgOvDidOWW7v-3RxqQytUPxmwNTpT1C69Qq2g3h0h05j25ZtxC0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها
محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار
جمهوری اسلامی و نیابتی‌هاش رو به
«اختاپوس» تشبیه کرد و اعتقاد داشت
که باید به جای درگیر شدن با دست‌های‌
اختاپوس در لبنان و غزه و سوریه ، عراق و یمن و …..
باید مستقیما به سر اختاپوس کرد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5578" target="_blank">📅 10:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5577">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2thdvjUW2WXgqhV2HBP8xTue03vVEDir19zHOa2gZvagI4zQkfZcyu2Vqw0SkVtwe8KqALImf_mg0BJ7r1uousw5aXIp6gpqMd_lgqZXWmjT4FWPjf2QtnyH_BTOkbqhGP5d9nPIzxE198xNoijpca-sowj5sJ6kfy3JLR6L_4Gn2tEktvTbwtqvrj-S--1V_v0i_PoHyRqxJ_aP8yGMVkJnbzbTlfu4wHe1sYFHrOJok6PWHq2FdthLiKecHEv6KHQjaObl9p_RJgE9BJLs5-T28M8eI2ci8jHIUJZ7E9TXkPdKpyk1PFO6_kF_kDDb9uA-w3Pl-WCbLkx02hhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dQdQNOa_-bcdTIDetDrlwOuf2sqj2QjpwV-sblBRRvq4PNyAw5_wGIBpKVZLtyMh9AnRA9SZEZDuD-wJDxD6fhEt0w5AwYVVOKZAr1rigdzcXDZowQqkjLa22EXmni93MaTzOGQy-Gg_bEastT8-HFk86EmfSeZxgN4q-2TdqfR59qL2mqlshEP6I0L4z-C4h3_SzrduDTI4gx9mI_fO8EPIwGFZSKOWeWmX390vlUQ1FkIdAOcJQ5XkOYmyb6mNQGjZwyhzRy4pUm2gtz6DPPUHCCGpFrYZcTyLmW3G_pPJClcaUROhCmZFdpnL0SBFDdvN5jdbS_4zTsW6mVpc1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C7EGPTC39J0ft4Bh4XzoSvHDWDo53A4zHEd0TjJZ8sarlXeSJDhuS0CwhXWaYdKIiCNIXz_mxKt2_-tmN8bZQqf13wOUI_zg35ZvG8l_AlSdHRBKQfenOSTIFr103xX1sMoaB-qJphlTBR1gsPLbdcfXIPqJLMPM5tD6jhCqIRpifbbecqjAUiLEYJMhGOjWOPBsksYmcFldzjEuFBE-2xU1TSAAWiitlixx5z-577qLhWH-gBF3Cv_Qhyce6SUDhwNfJM5e0hW2EOIlP1T38_nMYe24PluEzQQC6_9TO3pDdisQ9ctOvhsfLpQa_QqYc8bBGTUsFQVJ0-oIvA1EYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C134VNomc6DlE3Q8izP1a232EUoJKuHs2vsLH5YWQQYDAK9YieDwQI9OTqHa5KN7mis7D5b3Y3QNCYbdwFKeZaRut69p9oOm_kkPlsCw1LNiMkXehZthHIo1y8RtNIPrOobKvzWNvhTQQx6LGU0_1wDAC50OR0kNflfOU6NWiJRLgQh75Hd-Ox9tUa_KeyoGEyrIfZMypAlL_8db8T0a0JntpPwdkWOMdctFRTZjFBWw5jEXrslqvdtc32mcA0CvSq_D7nbAephWkhSrkvwF5awRBpYvNwczo0zO4TWGR5MbWrE0hXNsBxA9yBUsO59PD0LAdRHW5c5QwjdNw6a9zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=ECEB1fDPfByOtOB2pDC7heDpLllRUFobUOjfr8kyZqnXm_i-G0jgIAySs0I74qb-HBol0YhiNG_bFQKwGhBQARLzcA1Lz_JcSxtujiGHpUKTMIsnbLI9ArA3zft0CHaDp9ts7tXnb-xGLpELTJ9f92tw8KDrovaxPKOu-42sboNYuxba340Gjw8oYsv8tCltUpIzaDFvjN41bIDWm-RZ6najMgjpSLI7Ggtmw5i0lLEHh-pegdiHYNiQPKlNwGCceFECgP0j1eLYPzdMNwOjMwrfG8Z8zvlklhwF2And-xwprDODaKrIrd1igZhGScN7QMV133i8Lmdof6tsrtNJoa01gmutI7hWZlZjkFJ2wwrU2zSJ3NEFXXvI54NTROAM61iq9uUDdEWsdFzj7av-ke7v7-ux7Hr5-gEoqM-TMQAeG7gR0IZPt0acuTgw9bxxmzwdABEv6fG34TfVwYqEb6bVja9w09LM6I8fIevo7lIW6AeIwgWrBuXcWZfZGcYik5GPfJqYQGVljZHvigvDH_OXtIbsHfKzu1NfvUw6bQ257XPyxF6_RQcc7BBIfJi5u9M7StLsKnFO_wTpZEHIne8loGEZph1_7fRdk43bfwJzNxLUKDAll9x2hFhKsdmrbC-CEHkHSS22dyIyIN9xwfWVnFF9GlUC7r9Lodiyjs4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=ECEB1fDPfByOtOB2pDC7heDpLllRUFobUOjfr8kyZqnXm_i-G0jgIAySs0I74qb-HBol0YhiNG_bFQKwGhBQARLzcA1Lz_JcSxtujiGHpUKTMIsnbLI9ArA3zft0CHaDp9ts7tXnb-xGLpELTJ9f92tw8KDrovaxPKOu-42sboNYuxba340Gjw8oYsv8tCltUpIzaDFvjN41bIDWm-RZ6najMgjpSLI7Ggtmw5i0lLEHh-pegdiHYNiQPKlNwGCceFECgP0j1eLYPzdMNwOjMwrfG8Z8zvlklhwF2And-xwprDODaKrIrd1igZhGScN7QMV133i8Lmdof6tsrtNJoa01gmutI7hWZlZjkFJ2wwrU2zSJ3NEFXXvI54NTROAM61iq9uUDdEWsdFzj7av-ke7v7-ux7Hr5-gEoqM-TMQAeG7gR0IZPt0acuTgw9bxxmzwdABEv6fG34TfVwYqEb6bVja9w09LM6I8fIevo7lIW6AeIwgWrBuXcWZfZGcYik5GPfJqYQGVljZHvigvDH_OXtIbsHfKzu1NfvUw6bQ257XPyxF6_RQcc7BBIfJi5u9M7StLsKnFO_wTpZEHIne8loGEZph1_7fRdk43bfwJzNxLUKDAll9x2hFhKsdmrbC-CEHkHSS22dyIyIN9xwfWVnFF9GlUC7r9Lodiyjs4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYpzLmr1OK4PW68F33MSCtcGEGDTIa39GCy2O1vHzDvumz5VZ2Q1fDs6-GZjKpHifmw9vlH9TSg5ZS3dXqJpBh8PvRTh8IbrCdCZ1NehwiSiNgr90nQiUluJP9dT0NPXKMESwsojjnBn-Gw8ijnhoGuf2g0Ex0GO-n9uu0e6ta_Z0ET_cF8yhPdr0MZ2cujU4GAbI6Vs6KXNi2crVZ20GZNpM0oJvGs_szmTMGz_52eOSWexJq02X6fpK4g1BrVwSMBsSjd2XVZhhjhJ1mpS7mzcI5CigTDPMG6IUhpPoY5K-b_bWrv6qQ-h4QLgkZh5lSa_U1CfK74u0nV5wbWMvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=J2haIs4pjIg_zdzKSfeqQt9qQ8KQxkyEwYqjjdCXTnUdAucmlgjXGy8Qw3zO33zIYoxMW9Z-MH61gxbDxPCxCP55i4_MFGkqVND-R8D5xzdztuLBMs99g4SB4WuqBb1s-lUGTWT48K9CNBxPJFeqvdLTzn5rQLWwMecQDwxTSQj1Bh4YqiKk--ztkPUI67wu4K-y_GBkpjZYX5Iuc87WQT5Nimw9QiWqVsNQzEef4TTmvi3_5VvPRjLsMoFzunUgwyPuRZLNX0cx1Vi0WzKf9OQU7l_KH7LFnCahxK9emHNnsXSkExT29zp8R91S0qII88SfJXAMzWm_SGYvx_E2ZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=J2haIs4pjIg_zdzKSfeqQt9qQ8KQxkyEwYqjjdCXTnUdAucmlgjXGy8Qw3zO33zIYoxMW9Z-MH61gxbDxPCxCP55i4_MFGkqVND-R8D5xzdztuLBMs99g4SB4WuqBb1s-lUGTWT48K9CNBxPJFeqvdLTzn5rQLWwMecQDwxTSQj1Bh4YqiKk--ztkPUI67wu4K-y_GBkpjZYX5Iuc87WQT5Nimw9QiWqVsNQzEef4TTmvi3_5VvPRjLsMoFzunUgwyPuRZLNX0cx1Vi0WzKf9OQU7l_KH7LFnCahxK9emHNnsXSkExT29zp8R91S0qII88SfJXAMzWm_SGYvx_E2ZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=e15zHI-7aRzraBoZbSaJlbEp7GGdz5-T3NNqHGI609NkoegRVAKgR_QH9Kp4F5DY1egL0gw7jTroT9Wr_G2ArOYraF76pq3udJx78f3cCZ445my4W6SModr14LFwQAtFkbk_EuZSsLttsYkvEO_TQC4YWbvQIVvoDbGBcbcp5NWbKf20AwWkedLi1m9wSqbOTVZiADJsuYZmzC7TYsDbw_-9CoOzT6RBmHOvYzh1u9mfesCrULy_FiOfPl8wQVyGwz3m1BOU-5xX0eW_r5cVYMtgxa8l_dj0dsm2R4tDaNo--UWNLgWQxZK4ZmPcnXu4CkuNGvPqNyq354BzKPFL4JMCnFZi5DLLUSZCmRMOdCqGPbg7mFXTnAF5HQOqDAXaj7omwAGHpgXo-cZu0ZE_ATHXPukOfmh5ZaS1KEZajdVqzeTijK-jif-sBZd7WZkSf0orYSEyREWLHZINoMVP0t3T5ZmzkVoT_vFpqw1JFlFMARDuhHA0Zc0-FHlzmfHsif7QVpTc7zz3NIzGPlAq-vwXiqjxlaB8NAYWZM97_A9idu4XxfbiUO2dEQ_Zg-wlIQ3rPhVbDASplYvueajWx7faCcQf8y8hopmLRxKLzxh8HXkrbAu0C8OoKSIuhsyT84gu4L1686G7REjl4Q-VYTkFkkYg8ejgvI_eKFtrCBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=e15zHI-7aRzraBoZbSaJlbEp7GGdz5-T3NNqHGI609NkoegRVAKgR_QH9Kp4F5DY1egL0gw7jTroT9Wr_G2ArOYraF76pq3udJx78f3cCZ445my4W6SModr14LFwQAtFkbk_EuZSsLttsYkvEO_TQC4YWbvQIVvoDbGBcbcp5NWbKf20AwWkedLi1m9wSqbOTVZiADJsuYZmzC7TYsDbw_-9CoOzT6RBmHOvYzh1u9mfesCrULy_FiOfPl8wQVyGwz3m1BOU-5xX0eW_r5cVYMtgxa8l_dj0dsm2R4tDaNo--UWNLgWQxZK4ZmPcnXu4CkuNGvPqNyq354BzKPFL4JMCnFZi5DLLUSZCmRMOdCqGPbg7mFXTnAF5HQOqDAXaj7omwAGHpgXo-cZu0ZE_ATHXPukOfmh5ZaS1KEZajdVqzeTijK-jif-sBZd7WZkSf0orYSEyREWLHZINoMVP0t3T5ZmzkVoT_vFpqw1JFlFMARDuhHA0Zc0-FHlzmfHsif7QVpTc7zz3NIzGPlAq-vwXiqjxlaB8NAYWZM97_A9idu4XxfbiUO2dEQ_Zg-wlIQ3rPhVbDASplYvueajWx7faCcQf8y8hopmLRxKLzxh8HXkrbAu0C8OoKSIuhsyT84gu4L1686G7REjl4Q-VYTkFkkYg8ejgvI_eKFtrCBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=XUgYIjFzK2Zl8ufwglxa-KJ0kiXa_u1e1ZwjQz_PErTxu6YDe7iHhwhNxCrQuLT394BYpaAA_yN0TlQrNhlzoStwWrT38dew8PADQo1VDEb46TNZFolhJhSCICQVeWDMyKTlsmP7FUG217_C58PjeCbKe3KndHiowFj8ubfiXxeqtE7eTB64heGyUDRjZGEhym6StTdaWPtQPG_XvZlKWBF9c28s5nrHj9mwr-LznadT9olgFvZE3W0ZxoQishR7M1vtthGHOK7tIRUcp-DAC8l5otGfxnkyV4ThGv-hoNZsSxNQlRbkngYHFyAytcajpPTK6TrV8JMETQPeNicGvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=XUgYIjFzK2Zl8ufwglxa-KJ0kiXa_u1e1ZwjQz_PErTxu6YDe7iHhwhNxCrQuLT394BYpaAA_yN0TlQrNhlzoStwWrT38dew8PADQo1VDEb46TNZFolhJhSCICQVeWDMyKTlsmP7FUG217_C58PjeCbKe3KndHiowFj8ubfiXxeqtE7eTB64heGyUDRjZGEhym6StTdaWPtQPG_XvZlKWBF9c28s5nrHj9mwr-LznadT9olgFvZE3W0ZxoQishR7M1vtthGHOK7tIRUcp-DAC8l5otGfxnkyV4ThGv-hoNZsSxNQlRbkngYHFyAytcajpPTK6TrV8JMETQPeNicGvoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c34RPTfV4h1BvjSnUAGYT6dT2SYF5LpTvRm-5pSEPJXSLQVdSXrnFy8KIn8J6De1CQMGwjnj80WDgepBD2P3WihgQI_NhXfPrc5iDhctZjPGOjbz-0EgYot-_ijo-XXpuMw9q8RrZZr_v1Bu9Lv9nWfjE6bb18HYd_fCAn-Gi_qHGc7i0K8DhAabzEBzxJysPj7Knu-ZJZD3sW7U_cG6OU-l0eBy-mcU70XPG207FDM5uTkl9QYC_qy8fcivOlU9qoRwchpWY2MBO1pRLYMYwRY_2VwnNYnYamdnr4Z2Jc1Ul6_yCxxnZz0WebyY8flbj0E34XZitfj9Dl_Amdzbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EiqSnAPO3kuE6Lj-_FppxJJ_uZMWuCAl-hUlBl6x8I_eZWgO5Qm2dW6f6r4nOdn6DcMQZh9bOFDFyxLe2k0UYYUnwswBdBbYPYuIrVuKrumdfiLhKrL6nkkuSsB7vJKNUmeqrVOdTtzH49c26h7jaseD4xMvBHyfW9bDKEUpPKwPdKftMMfx1jYoDF2LKtTxQQcP1uFThNfT214_vSH9IlPgMhsoITSReEw5-5CeIRhnFnV49BgDYcTmlRTupZYXQLhRpoGSpQol4LXYOU8pQA0T4doYeqRZ5uYs7kZRk3EEx7GUfiPiwWHex9Izfx2aBwXVJsOfFN8veU7gTI08Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0MLUwPi1hjGr1Wro8DknjpmSawbHnce08astuZLNCPMG2ezGOB2OEaBgbOpU61nuqZ0_gRpi9WVf9ggKPGRXJ_VIMLkXlSJqe8Kfyhmann4xdXuZMh0j3Tu6DpwCt37q5_gCAEglOROFk--vdN266I-7vzBbw6CTcTylGdFOqAFPyLVt3ehplyo-BRnmaqAKMQ05hprB3zQ_OP_Qaqqu3Tr39UBm2ijmECe82v8Y_BGLRTh0-leX0_vcfdo82zk57pdpF84AoU3BmKJO3SnLvKz9Tzvu8EH25FrMzSoIDxhlbjPkCOihkPHG7eenB8Oaa_EF_fC5P1dxICHcUpTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt8R58LThkJQ07I4b6Dte4oAyUsHPLg26QcysC2lnj9dsWp9Zix9LeHYP-Ed-G-LIinpZsjB8NJPoxyenuBvnoTZxJAM4AqQeD8mbZjCGlu66-cCfsd8f1QECfi69PhXX540rMdMsGABl2t5EQCXAwrS3ntMGHiJP4cC_bpKgDHwLzcjKZJzUypYm8aaPSjBkDUnKaFcB4Eum2sutDUy0WTlpZG6xGimz6l05Q3E67gDhvSggKGiNnXmXu3wZ-qENl_RTHxKMZOc4YWNuR-HDFzuFeFaKazO_T_Zu1l3_AZ0EwY4wAu6nggnVb4asWW0wwou0EU8oJfU3vOF5m1a1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4FMwFe47g-a83q5b2ko7LU-x3tp6cFHdTFJpgUnPi5orxpC0MHPyo6bbtbkc-eCmcq4HLrgIHz7uscafAdCxjpES2dNOSG4T1A3WpXELzA-E-MFiAPLkVmlJe7ZBKLx13BESskHLOBnK36-LndxY0Lvf1p1-aA6aSirXV80AgIlfUgRd6XTsE-090fJTEjZAWZkR2Rt4-wA92diFPwXzSjc_GscXt1-mEcPMvlm-pqEoxYmigfvcIv1UcYBEuyfIIgJiVtV-VTolYfNTESPH1BGrtm4ewGeRSCiu-RtV54uNAptVMWp3GKYe90VdlS87cdkd1-JUM7MEe2Mj2A-jA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=SpgorMd3yxQRUEGeCQvRB_Xg_GsJzrvtfl-EIDQoDrktEsvD3y-k6penhGhTVl0ns1HkuoJVgfLRiw4vnreS_yGl06eKNpVZjUrwP14FKrTHpoUwYUHFyal8YXttYjMiyc6gkJS7yqmfB-p-CAv3OSwM9o_ysB8GESyaSfLKip2wMcI-BQfFzLc4DNiLpLMAL21mBkKxidqaCy0zLPQTsRfvBMFj80_N6tmhPy8pgsTTByfTcccUx4ZV7cSk21Jx6TEvi1b0poDW5TIMYQxDhCSmxUDaEZs1DIMMsQsn_-VfpI-_7QI3Y-KuKCQgeqToIR8decbLmyD-03z76VtXZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=SpgorMd3yxQRUEGeCQvRB_Xg_GsJzrvtfl-EIDQoDrktEsvD3y-k6penhGhTVl0ns1HkuoJVgfLRiw4vnreS_yGl06eKNpVZjUrwP14FKrTHpoUwYUHFyal8YXttYjMiyc6gkJS7yqmfB-p-CAv3OSwM9o_ysB8GESyaSfLKip2wMcI-BQfFzLc4DNiLpLMAL21mBkKxidqaCy0zLPQTsRfvBMFj80_N6tmhPy8pgsTTByfTcccUx4ZV7cSk21Jx6TEvi1b0poDW5TIMYQxDhCSmxUDaEZs1DIMMsQsn_-VfpI-_7QI3Y-KuKCQgeqToIR8decbLmyD-03z76VtXZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeotRbLwbAd6VcgSfIEIiTs4OaNtxBup2iUF8zsnBZXZkxbSIJYYaJthb2tNN0qe76KEIIl0g7bI2XeHckTUAY7AOJ4Ke5C2Kl8NT1_GzfQU-gkGIXn2wPMBqXu3h9Q9acUXhJhlyMkciQ7D6VLRe7GH3FGSLt7Zg1MGgKbmO2keDBBlCw4hC-u1vtzLeWpSnuvwk7hy9-dXW1FxVgPBxBW5EfRxePgI_vfnQPKg4yCblrxDhaScpKcqqtKe9Sk0w-dsm_3c7U67_6Y9iLyeKGYeCGTqxa4gn2gR0jMPjCI3RGtIwgipTc0DAMVMw0iYMKCRckC8yFOsLncO4qyncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH75FnlyvedQGuQk9avL2KzImz0UXe7yyc7d_YMBNvALRqp6HpGIRa0dTTcerb38NwfUxjmkZ8FUM062RAq8aMffSkz5FC6PKJ7XnJf1BGNW3O3honBzaArwON2E_y798n-_Sb6uUG0LLfVa3EO68gZrVWk2sAglRfHEzOOBrt3gUGZYhsuZHjFoLfZNRImT9loZE4AqS1BNx9dRxKu-mwi9kZdrIBFMnq7bQ2l5-isHMylr1etXyHzl0KxEZaCZpfotAazP0Y7m1oEyx5-B_WQFwRVxd2Qs6t4B5UkhPjTch5Pa0qVun-Q3JVUPelY1SJTeH4-33tgH3PGaXjlSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sARSgPLOgF_FRrc-NEPAk9GO73AZw_Cb0_8o_wX4dxA5w3iWmg4joI8kTaxoO504DKDz7nrUuAm1n8PmSoGQcutqJAtNRdZS_XG-Edpkt1FqW-riuVdjcI4Ncg1soH04E4yTCqGJmLuqS7QIFxFc0HHFozfhypjKWUxY9vnYhTuALmu_VB2CgTkVGhtGeK4k7AR6DFM5y9a1Jtuxlwvx1A8nCFxW_y0Ae_yuahG-RpIXvaXk9tP-LBxYiI4Cn0GZ28tOr2TfoUxb3q_NbwU7LBGNg5F6UJr3AqXsPRy7eV7uPRhU-9YLAU_5hixmzeDmkrXJQgSp2iWN5xYPKhk_oA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUaR1G7xoRZpDoPiks17PN55ZYSK5unpF2fDm4JY53SS-QTvunyN9KvNlz9fuc0tTy0PQL_y1xjZwT-DJQ_QoQNUNbGBTlpd3W6BKt_da6BG1lE-JdntoeyYcXkxSmUS-20f8xpaUMkg-8yo51akXGl7All85S0fM6QcsewXQrVMIVxINpjtJpxxDDIu0ts0di6xTdFU3LNP2hbv3IOW_FD6M8yV2R3xCiMXfnpYi0jwKTG6KvTqhL9Linq1EjREaq53KDYcM0gjbthpQJzbn1_CZn167ryM5eCqXrBSb63ME7euUCuPFzMESqa9TRzRWl_mH2MMaX7D4UhWawJbLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jUpEfCkgD2k3QwTLi2sm8zXxNlx8FOXcJR6uJIW_Xh9CrKOsHaCRgkg_EpTYtM0VX3xxAlpPtbt9m-pdh8jp2joa2Ms2AaCEtBBbIhLeF4ZAlpgfSSnvOoKLNQxS7sRxBHwvfuSGXjCeo_mnrnAo5OuJ02Gm1Vyd4QV2m02Z2oXmhnFvd48XU5VXZcFtf_7-1s-k62N5GZzWuhQCULKbAX5X4Av64LFnpDREBCkX_Ixu9m55S-PJzwMy8m_DPoC8yk1Jzm7uMoOft6HaDMDFEdDOzJ4YJ3wj-ih-gTY6cxjCOtIfh363CTeWw1-GRyF2E4ft_04_mg004z3ZhYp6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mFA3WgM6Iv8STMxfaT6P2I2WldWRhAY-LZbSnvU8xutEJkYSKSRaPuGV67DEHSd9r6MabF05w-e1Uqt1GW6l_gvtxSGmH4pxcgsf6_zHZlsdtS_DngfTr_qdHLR3GB5xTG52bNf2u_PRNBjXzb0zicRjC7hfgQ5M22IQGetDsGx_7RR3yht6lgzmt0r73dusaGZejHmIz_Yz-ZPw1kTx3Za3jSCVrkgk6Hj-XugwjsNxo0pgI0xujoQe-z6yrvpxWf_8VXV7-khRlzSsjUMcqTTam3N5dQxwoNxtjrYlZ6R0T2ys5Xwg1bA__14-517gZS3L6FFHMvi_9WUSDeruvg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d1vupsSNQAMmJhSUtUB6gDTbrH2omf8vBUDjbrYq0gwZPFAzwV6mqKBELlbVviXRw97g8ZJdRR8eobLWpNVMB236op0mpZqi9Km1RSv0Mmt1zSdS6l0neX5Rcq-JHB3beSSxILD5jEHNOsdlbkQ81FG-NmhU6uEiB39MSllXG6nO9fOO4bhvHvo6hIE26KjPeHd8IkA_ogZQmuprhz_z9m9lf3R21aDOih0S9UJBeokeIiHjsC8tRul_Z2bFWaDJCZNJTzdL27QT9TZ1xStEU4XEVnGjMpOw7GjdUzq2NaCs9Ye_3ogOd9rOOQnOEr0Hl9HOXm4dtzLov1sT231fXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqG68dmzMS_8kcZ03eKvdjqOrCIg5PGiL-p1URkFRfGh2n3_NdLNB7f-J7f8oZPj-lyYTrLc9fHTRiilAn1J9dXwThgRudpVteMnyODZCJUsH3HP7py1hLmb2pS4N8cykp69TtyLvrgAIuhgI6lhsnmSXKMCGE1T2pD9wlNpm7VGq22cg1cfqPG89RZJAu9b_-jPP4Zq6HLhgHFjFaWfsPQcwhOLIe6aWmPP6c4RJ86AtWfi2icdA_hVMhRf70HkSmi6xepVpt8yULSNNoXiA1yDrKWieEpb5dTwxRJLxdnQ1O3bgDGeGIZg4kgsWkYIGx6cxzRo3MpEw8Jl03Qiqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=GWYnMNjFY8X7uddswKqBx2HtGBOwKmF5PuwnQBMeaNdSjnBEfugRuFeEBV41uuuUofhwAHad80ew4ti0THHded4Dx-fFpb63TMdRJHnRtsjSX-szJm-q-bLCjWia4TX0rwGpMLLfDZSlFlxy2zMjyUUxjdGAWp_UdxjNhxjxs0CpCKZ1Jjf6N_T7yku2Brx78qp0n4_-5R1l1U_Xju8cP8qlh2sRUgGObF9K-AfcoSVnpRY2zC2QlHMS7iUlmQWHUYIfBP8N-LXbioq_kLbqB4yOau-mPWMyvWhyKA2L0WgLI36mlBkwRA229XvbXtvR7hQOrc2wJM-EyOFkPdQL-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=GWYnMNjFY8X7uddswKqBx2HtGBOwKmF5PuwnQBMeaNdSjnBEfugRuFeEBV41uuuUofhwAHad80ew4ti0THHded4Dx-fFpb63TMdRJHnRtsjSX-szJm-q-bLCjWia4TX0rwGpMLLfDZSlFlxy2zMjyUUxjdGAWp_UdxjNhxjxs0CpCKZ1Jjf6N_T7yku2Brx78qp0n4_-5R1l1U_Xju8cP8qlh2sRUgGObF9K-AfcoSVnpRY2zC2QlHMS7iUlmQWHUYIfBP8N-LXbioq_kLbqB4yOau-mPWMyvWhyKA2L0WgLI36mlBkwRA229XvbXtvR7hQOrc2wJM-EyOFkPdQL-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=VAEzCHl7ZG4u3qpyjSRBVddk8KWIoPZez5PC5o6tapGurAFPn_38XHhQqL_SZnYYYjJB8a4aeVa3QPkA-ZefIbOcT3UHjYVAHyGZM1w5SsyAgDoYgVs0T4bf6UYI14kALHNvPGybw-okA_XNq-D2k7w_VeuxwpdmqnODBUKS699LFJprnocNmndY2AKBQwASgRg8tYBNca0n2llEsHGOgV5e2w8a9MpIsSb0QLmyyyQhOij8ZDt3AFcdZlUNoSd44wvApeEoIkgiCtQZI8mF4-Jda-IpQ3jFgmFfagirRFIVVvRYm2Xnjc968h2cmhWdeJBTJLS7GB9iwL6AH-KnCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=VAEzCHl7ZG4u3qpyjSRBVddk8KWIoPZez5PC5o6tapGurAFPn_38XHhQqL_SZnYYYjJB8a4aeVa3QPkA-ZefIbOcT3UHjYVAHyGZM1w5SsyAgDoYgVs0T4bf6UYI14kALHNvPGybw-okA_XNq-D2k7w_VeuxwpdmqnODBUKS699LFJprnocNmndY2AKBQwASgRg8tYBNca0n2llEsHGOgV5e2w8a9MpIsSb0QLmyyyQhOij8ZDt3AFcdZlUNoSd44wvApeEoIkgiCtQZI8mF4-Jda-IpQ3jFgmFfagirRFIVVvRYm2Xnjc968h2cmhWdeJBTJLS7GB9iwL6AH-KnCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=ugG2uyo4bgRUhaQAZyAMHgtKMlWMNA7T8SWR1gP6WJLFBNGm5CCxNiE40cHo7wJzMoKf14HJI55ERQS0FC8Vj3M8Xnw_wze2yWuRt1BgJpEUEYPmoZRB0tUgOCs0ZNSsYIuw_Yf_G_w49y8FSKE7zx-h0rKQM_H-YZVPQ6YApezdHf0f4SXQELDT9L2Nuwc-i0fmh6Xg_TSbVy-wFwu1SfYVccKhB04Kf0N8kGtPXbICtlZGiKzGR5aHa1sZ_W1is-gvPTMo529J46EVczpfyVqrHuBl7HgV8Yqu7NSRwv_sFxuqW5EmLIrSueQOt80FglfwdJDMykkuSTAX1srqAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=ugG2uyo4bgRUhaQAZyAMHgtKMlWMNA7T8SWR1gP6WJLFBNGm5CCxNiE40cHo7wJzMoKf14HJI55ERQS0FC8Vj3M8Xnw_wze2yWuRt1BgJpEUEYPmoZRB0tUgOCs0ZNSsYIuw_Yf_G_w49y8FSKE7zx-h0rKQM_H-YZVPQ6YApezdHf0f4SXQELDT9L2Nuwc-i0fmh6Xg_TSbVy-wFwu1SfYVccKhB04Kf0N8kGtPXbICtlZGiKzGR5aHa1sZ_W1is-gvPTMo529J46EVczpfyVqrHuBl7HgV8Yqu7NSRwv_sFxuqW5EmLIrSueQOt80FglfwdJDMykkuSTAX1srqAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=ZlTQazTsk09jB6B8MX1EAk9KfADCy3eD0t9xAqxEcy8uy1RzSN93VJrIYEmTfG2KqrBEO4W-m3oWtqZUOtHkM4peHeJqTUxS4P1nEObJQg5EDcpvexA6RDLBKNb4Zap6lZUb1O2jHNpT2dTT98QfB9WCblpmLhbbCYvkEZ1csXyJua7o6aB9sQ7RuhVWF-PeSoMzBfh_CvQ3Ok15cl2R6WgNbc2S9GmFnv5yp292e_ArqyZSaWBvG2VjmVi23KQJcqq29X1Vxe4bB1x532DEfQ5CNG8tYewuf8VihTQft7E3LjqzTWmNjtv4UJKB4uKqMb1r2WDGkSqv-w7Q0adr_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=ZlTQazTsk09jB6B8MX1EAk9KfADCy3eD0t9xAqxEcy8uy1RzSN93VJrIYEmTfG2KqrBEO4W-m3oWtqZUOtHkM4peHeJqTUxS4P1nEObJQg5EDcpvexA6RDLBKNb4Zap6lZUb1O2jHNpT2dTT98QfB9WCblpmLhbbCYvkEZ1csXyJua7o6aB9sQ7RuhVWF-PeSoMzBfh_CvQ3Ok15cl2R6WgNbc2S9GmFnv5yp292e_ArqyZSaWBvG2VjmVi23KQJcqq29X1Vxe4bB1x532DEfQ5CNG8tYewuf8VihTQft7E3LjqzTWmNjtv4UJKB4uKqMb1r2WDGkSqv-w7Q0adr_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=CQOy9KZS5on7dSevyTpJ7VSj6p3KA6ft7gIwkR1A-m-IMKCJxAttqtxMfb9C1gubbrKDw7okg51FTezwnuzcvdPNZdzAIjIvXVPIFwyhCpXWKceTxYRYeWgQdHXFlnLjwVoeu34UL5qlwpzNjn7Ze7YZd3siqW7pcsiZi_AzhLDWqKgBdnGSblOUlNxr8OYhJHTdHtuyUJTG1YcfdfB9gTwak912vmI4jcuYrh1MmsS4qroMxEIgC6rvxH_n4VyPdXoKJYGhNQKAC_CCpeN1LlzZT0YGPZb5_oFKCm3D00U6cOZ0UJI0WzocavQK8JqrpgPPytSrJWOv3y3ElXd5BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=CQOy9KZS5on7dSevyTpJ7VSj6p3KA6ft7gIwkR1A-m-IMKCJxAttqtxMfb9C1gubbrKDw7okg51FTezwnuzcvdPNZdzAIjIvXVPIFwyhCpXWKceTxYRYeWgQdHXFlnLjwVoeu34UL5qlwpzNjn7Ze7YZd3siqW7pcsiZi_AzhLDWqKgBdnGSblOUlNxr8OYhJHTdHtuyUJTG1YcfdfB9gTwak912vmI4jcuYrh1MmsS4qroMxEIgC6rvxH_n4VyPdXoKJYGhNQKAC_CCpeN1LlzZT0YGPZb5_oFKCm3D00U6cOZ0UJI0WzocavQK8JqrpgPPytSrJWOv3y3ElXd5BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=hc9cvCMjk3AvGmV5-J94sUTsv7b8orvH-5tf9HMVy8IKLwVv7R6PdHnrIqdRcati5FcK_DymEmBpU-3VlErQtH-svalPuZ6OoS1PNEH4Qpyo9dRMBJkFuek2aYh0MwN4WtZNk0F6evD_EswDh9xJRrIG0a0teIBr5-ztIwmkDbmzf7Dv84-wcv5ftHFsNpNQbIT-8jmoZF16v4weudkwu36kKsL5hPuLWchYEIB7hs7BcYt0VbTtXsf_nXws26oGcV6ll5l0imTxjQJSTsCPctrQACXIynkllmkC9s8T3NmtaHUHk8V_w5CK1e7huKbOczEb13apobfb75kJXi3W3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=hc9cvCMjk3AvGmV5-J94sUTsv7b8orvH-5tf9HMVy8IKLwVv7R6PdHnrIqdRcati5FcK_DymEmBpU-3VlErQtH-svalPuZ6OoS1PNEH4Qpyo9dRMBJkFuek2aYh0MwN4WtZNk0F6evD_EswDh9xJRrIG0a0teIBr5-ztIwmkDbmzf7Dv84-wcv5ftHFsNpNQbIT-8jmoZF16v4weudkwu36kKsL5hPuLWchYEIB7hs7BcYt0VbTtXsf_nXws26oGcV6ll5l0imTxjQJSTsCPctrQACXIynkllmkC9s8T3NmtaHUHk8V_w5CK1e7huKbOczEb13apobfb75kJXi3W3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO92UfRcbWY7P-OAqjucFBNylyVR-5KXZUrqxeFOg2s45UEscE7R4-t7venZEnB7NkBswh0kyPkODfryn4OmQXJQe-zpjZBsaNrwqvHUkOh_MhnCwmXVq0Uy3bm85dTEkFbVBVFAtiqyed_DTUXPsiff4k7ASYi9O3H8I43KoXVvOU9cCGducEHTGQba_EyIgZjzClKu6AsFlXp-SSCla2_zmp_0dYG_s0nkYsE1Kxj8J1m7krTUMtb5pBL35uHA9j5gj4i49yZDbMGysfbY-0Ng15EXISo6jMwMYOexf0fMY9dzWo077M9zWM8UXqgfcKtoGBhB9oZ92Criw48omxwFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=HR9Ra1AMngIxOTv4nFCZwvQbZhGPLGyipP7yMXfYqM_t-FEZE152kRG58XZFuUzViEIW8Pe3PNAEX4pm-hHBdVCMgqeHVLVYA-NdZkar7rjR6mZzG3p14vKd1gVDJAoX191GMgftge47z7W1CjXzf5c86pO9gkdovJAFKmkSBXid0Eyt4cAbGstBBRPzAwlK5P06cMoQgZz-Z4Tgsbl6HhzF0Zx-xgHc3eVJq1CPTUt1KDA-qZLm79-9jk6DI_3ZDLVgV-q4-UkAKz2-qt8P5s85tofd6AUQpT2X8k6ohSMRvo3pC1qemVmXg4JbqA-aL_xaV1LLindKp9CWyTIO92UfRcbWY7P-OAqjucFBNylyVR-5KXZUrqxeFOg2s45UEscE7R4-t7venZEnB7NkBswh0kyPkODfryn4OmQXJQe-zpjZBsaNrwqvHUkOh_MhnCwmXVq0Uy3bm85dTEkFbVBVFAtiqyed_DTUXPsiff4k7ASYi9O3H8I43KoXVvOU9cCGducEHTGQba_EyIgZjzClKu6AsFlXp-SSCla2_zmp_0dYG_s0nkYsE1Kxj8J1m7krTUMtb5pBL35uHA9j5gj4i49yZDbMGysfbY-0Ng15EXISo6jMwMYOexf0fMY9dzWo077M9zWM8UXqgfcKtoGBhB9oZ92Criw48omxwFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5534">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlVarc-andjDlidIglw-cGyNgxY2nkvv97_Ini3Z79qMPCMNlOe4uzam7uU0ZCb71lD9pwMZYwvX0jK0m1-wPYhLyuLErzByoH_w6ceiRn9oc_eIOJBEERUeryc2nk-GirctKkkoMq9wO5xejvDm7a5lw4gY-r9tbPdZx1BUI90ebHp6HJWBCt8ncAgJSZa21FKZ2b6h60ly2woywp8tL3myRJ139yIEehYeuoAyIrOq458cHJ6Hp88dQ2ITbVk9M2fd3j_SMX-OPi0Ic2eqATkwQHhHKZYHDSmtM5Czc3QQ0PGzXOXfphN8uj0BTHhZntoNMZ7BjpJkk6vN9KPMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: اصرار ترامپ
بر امضای تفاهم‌نامه در حالی است که مقامات ج‌ا  صراحتا گفتن  تفاهم نامه هنوز نهایی نشده</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5534" target="_blank">📅 21:16 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
