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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 02:15:05</div>
<hr>

<div class="tg-post" id="msg-5642">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81ee77286.mp4?token=viJq7NYHpdctnqvUTHmTh8Qe-IlUik8xBXOy8NQwNUGEOfDzAB1bvASo1hKKktb1tWnzJWT7V16X5rOhmou5mEa2xh9en-ANmsFzh5TQ2r3WTojHHAfy9VxNN2QZROVgvrUJ-OdhSAtIVrCN145Tb2si_gjpkAlQcvsdOXk-1erSqYFtYNzbBoMMvASKHCbpwAMR8DQzEAQYuyx5bH0q05HwrrK4exl_61jyzv7FOztiywBu5OnB4fmTT67_LRrCwzqOV-OA94AOTnsncvxNUcdD1ymFMzn-D24jAuZWmLmqsswviVMWEha_5qyrveP5oqrtioAHrVVAxvauCqSkvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات اسرائیل به جنوب لبنان  بدون توقف ادامه دارد.</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farahmand_alipour/5642" target="_blank">📅 00:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5640">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTb6ll6mo8_3poAwGuJvYlJQ3J3CPq2Bncv_Y9NIZS_6UDTcd1ZGicb7AcxviInTJwGrXxrPiBBFF03i8X3MDBWYG7kTPr8niwfgjMhmvix0FM38ZL-Cg8MnsYhidZ7ZNg6LVlZrdwho7Vo3jIlyHZUVRmK424vset_yaUUeYybw1Ua9nSJAW-pmrGlp_FAUuNfoqD0990XKLxk44Xp6gDAN4YX3lXzwT81kny3GzFwy3NGREOBvw2WL_kqvCS4ZApJL_r6Tp9viK1WyP8AugN4DLnMYsXckq7C_5vm8y1XSe6PSCDXn_MruWZFQLKttPMCnLuk54NxEkXkssL5z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vOzU-u4qrvknyaI8POmRHrvIAFwk_1hiYryDngCoHXGHPI4RHGyzuQLILziOkCVIWL6fe94egh4Dg8ljFE1ItJP85cB_iY-6aEdqOAendQpRIjRo_f9_JEqo_NQGOmY9vMh-oYouVRMVqCazw6qdnghM0Co2pMwfttacz59EJUrfGPsxrwH6kexYF-RkUlB7l8XXC-fRiVN1MqC_eDFR41wwj1b-3wBAHfKIEk--h5_ku1XYDBKova-f4xxasZH83srQc4EllQ0G_tdBjZmdroO_BkQ3Z92oLCz6nvmpmvpenTwrG0OH85R0PRU37MIvRNxOs0Jg2MLU7WDk1k6vRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فرار گسترده کسانی که میخواستن انتقام خون خامنه‌ای رو بگیرن!
تا اینجا ۴ هزار کشته دادن و ۲۰٪
خاک لبنان رو هم دادن به اسرائیل!
قالیباف دیشب در تلویزیون جمهوری اسلامی گفت : لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5640" target="_blank">📅 21:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5639">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/5639" target="_blank">📅 21:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5638">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxyJKAnXOSntZi3sOwYR6XnrhJBQOwOTeY8ND3rpGHq-49Qce25RVtEpyN0Zn528Q68yxOwVkuEnPlKQm3A-TruHQt5Eg5aY1Gn8s2p9GyoxVI4K7hXorBOtCCUolwJVG4oRbU1EZ82Rclp2RH6vlBFZMhcGa0kXGvGtBfGV9bXIOKLEdQrqTY0-Tc1llzqK17iG-rQvOEzsom-GEbG7djVH6Q5vlp1tua6w4kKUvQ6aitaLgJabdd9FzelugCsOJqTV0T0mi0alYy7BHxgv35KthJLnaZYsHbbOOyosdbGvprVCZyixsxD6dLu43eFUr03bc6KfQ6_md4ZfdTk_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنان دقایقی پیش رهبر گروه تروریستی حزب‌اله نشون میده که این گروه عامدانه شب گذشته آتش‌بس را به شکست کشانده تا اسرائیل را وادار به واکنش کند.
نعیم قاسم :«تا زمانی که قادر به ایستادگی و مقاومت هستیم، چرا باید تسلیم شویم؟
ما تصمیمی حسینی و کربلایی گرفته‌ایم که هیچ سقف و محدودیتی برای آن وجود ندارد و این تصمیم کربلایی همچنان پابرجاست.»</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5638" target="_blank">📅 20:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5637">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5nttENIgEfiwZuj_Reb3t1GJDwvM9OmzGMHBQglcOzJZS7osKp6H4gyPbq8aVf3VEpPlaqdLFGdpugxzWYPC9xIqgHXk7NOM2GvcIyxrOrXfWlYv824aSDBRVOALtBo_-scHBs-rAD5iGr4Z6ZVgBzZNRT__f496MlvWQld8b7LXW_gCr64LhxfrHnvugcxUtiD0ZIIigvohWvnFiQ7lbpW_TxTVCcTxzq97jvA-I1pdz9Kb9NpGk_iDKZaEQJctakHwuXRsOEaNY17-tbUnipccH2djZz_TJwUgrr3mW7Njb8b-_CWxqHV5QeaVNyXImjUppOS-9gZlaeHFDuxAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067993854494622141?s=46</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5637" target="_blank">📅 19:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5636">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rip09e5DCowT_2bgFM2V4mdcdlYvac-ZajIMtnS1p7qAA4rl37ZZjKlmHja6D4J-TFcOE3Ez_PNFEfOuoPs91wj9k54OW1JNDAFu-ZW7rNUA_3Bgh2FawlbEEYS8tqxo7cJY38PR_WJtmMCcfLV1wfZphVB3MZbocNKJ8086bPKPaZV4T5N0vzKpZRXSprtwa3OS_-fkWsPwv_e6aySm0AW9K1SVRf95N7vXfTYo0puM8tJqpuoXbi8jFGOmRLd3fZpBVewUKc4I3MPIX-TVCK4gpKjGdeL_VuH-qzYqGsVKKj7GCeHIkFpTSXWvY3p5AJ2OKZG1g3w4TYrTpu8BiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت لبنان : از نیمه شب تاکنون ۴۷ تن در حملات اسرائیل کشته شده‌اند.
پس از انتشار خبر کشته شدن ۴ سرباز اسرائیلی در شب گذشته، اسرائیل دست به حملات گسترده به لبنان زد.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5636" target="_blank">📅 18:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5635">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvKU02dxYTYH7ce3t7cDFcG3HV9e_NbL6ahNpiXGYwa8j-eq8FB0mqWk42AG50HpkT2MxxU208YVylXzsaAOBw4iP0oePiOaZYkSdOsxFPsVGPviVd-6AQP4pKhdL4CbqyQkX6WOlGuNzCc4q88zHIddaQ5jHXPwQIgnx1tatD4DR4ThilxwAL3O7q2wtVQoe1nBWO-0hW1CbTZUcgmTqOYPQHFh2IBg3vUGa1Q91jEQxPRjJIJ4Gi5WAR5n5nT93pPg8S9NSUZtsNkMmz_7Yqv6XN-PvGqjSK5UMxb1u8_cAO0tDqpjV5G9OBWT9Id5TdCwZXb0PM8G5841ebq-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگذارید</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5635" target="_blank">📅 18:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5634">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5634" target="_blank">📅 18:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5633">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNnpLhEXscABelH1di-uKvhA3Q--JovL62N-xbeEfSpMd9f26hJ9_j8mjoAwLEzHm1pLoKn8amllc6dvSDxfICAFsJrImqslXO_1t11vgUCoRK5_k2zNDS9VbkiiOdSTpzSK6Ysfpmg-A3un2eVIOwLQHI65pzGSGFg68EmWVla9KKSs9CUNtuemXJ8KL8xNFgv_tTTMYNEGcLYaq6_YcD5v6n4NsF066I9ujDyewD3ghgNnFP0aN89A3cgMsbA7QDBUoyzB4vfDn7X-xL3lj7x_JB-rnHhujVf-Sou0Wo3iSVN-Fwv9h8LXBThbOeXa1CmSbm-wC9_VFNGq0xEg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو : به بیش از ۱۵۰ هدف در لبنان حمله کردیم</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5633" target="_blank">📅 18:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5632">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5632" target="_blank">📅 18:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5631">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=XW4Gw6WK6IDsj9WWu7Vn9XSyDx-rSU5khNhnMKM5VinWd2NeIa7dU08Vc10RvPj3woq2JrCqQaJ2PjIP5LLFaF-bPZA-ARmXQepQrC7NZhxOxRtL3aiBXv_ijJCbIgYDg6keUoxUfz6HOX1fdmHfwZTQvaXby_NY9GFteArowaD28XEmh2T1Cls8SrbEJ6CoijlSLrYxgLvo8ZRULOcUf_jjVxPG2DhYy89vYf30P4RHcmYHM-3Xoo1OaIheNDJPQG5BDjnKSWpMSajXYe0FrY6kCs7SZ56vWzwB_5J1nGPjr0hdGRcbf5xi_2tAkccHhNWCyhWWmiXTuHdWCH-W1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc70f2404f.mp4?token=XW4Gw6WK6IDsj9WWu7Vn9XSyDx-rSU5khNhnMKM5VinWd2NeIa7dU08Vc10RvPj3woq2JrCqQaJ2PjIP5LLFaF-bPZA-ARmXQepQrC7NZhxOxRtL3aiBXv_ijJCbIgYDg6keUoxUfz6HOX1fdmHfwZTQvaXby_NY9GFteArowaD28XEmh2T1Cls8SrbEJ6CoijlSLrYxgLvo8ZRULOcUf_jjVxPG2DhYy89vYf30P4RHcmYHM-3Xoo1OaIheNDJPQG5BDjnKSWpMSajXYe0FrY6kCs7SZ56vWzwB_5J1nGPjr0hdGRcbf5xi_2tAkccHhNWCyhWWmiXTuHdWCH-W1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پخش حملات اسرائیل به جنوب لبنان
به طور زنده از شبکه خبر</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5631" target="_blank">📅 18:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5630">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5630" target="_blank">📅 18:14 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5629">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=r201VltzuQbNkZvcfvayrEnAQmByDB7We05x4jOsQb_IBTmLcxYPeBW6lwn_xTVTUqm18wWB2AB2m18g4I3lozL_zRqw92ntuM2SDc_BM81bDrSMLcNR16HiWvrUeUQPOGIm-BLhuwP5NxHwYHbezldmpF5Q0ms2GgbrZQnmFXdSO3AoeGi3F2NV-tsEYvk7q_tHK_YTWgan34NBJfxaZiHxVn1RpXpVKblNxMuF23Tdr_Ho6qlnrgzB3F6PXKQBmbpwD5HI5qu6caFeadpdyQCOeJiSeqvj_4cr0VCW75YOMKonO8IWHt_nmQf0-oTyDyO0EC2jmz8noRcQ6LtY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73e57c3fdf.mp4?token=r201VltzuQbNkZvcfvayrEnAQmByDB7We05x4jOsQb_IBTmLcxYPeBW6lwn_xTVTUqm18wWB2AB2m18g4I3lozL_zRqw92ntuM2SDc_BM81bDrSMLcNR16HiWvrUeUQPOGIm-BLhuwP5NxHwYHbezldmpF5Q0ms2GgbrZQnmFXdSO3AoeGi3F2NV-tsEYvk7q_tHK_YTWgan34NBJfxaZiHxVn1RpXpVKblNxMuF23Tdr_Ho6qlnrgzB3F6PXKQBmbpwD5HI5qu6caFeadpdyQCOeJiSeqvj_4cr0VCW75YOMKonO8IWHt_nmQf0-oTyDyO0EC2jmz8noRcQ6LtY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به رغم ادعای رسانه‌های آمریکایی، در اعمال آتش‌بس، رسانه‌های اسرائیلی از تداوم حملات و عدم توقف بمباران‌ها خبر می‌دهند.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5629" target="_blank">📅 17:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5628">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPaWNmtAmIcVVdN4Np0n495OBUtBp9vIU7GVWkyrEQWYqz2mF5gTPAXWmIc3VcxwF_4WrwO0yaq_L480c2oWZJc98GZugjRtea2DOx7b1QANtDIZOb5BLXph5oZKyXvRAGnWVJvbayrcmCA64kpjVz-4GtqpGpN6iFhFRO7xl5pdDqni1F_iHS51fwtxoy-JqwxJDgPR08VuqFxJLo9N6Ha-SQUdsyXDb-EabemFUHVNxbTrcW1tCUdDlMtRltoAS9vMKoUxodAOveRSdOMaMK_VbMrbSk7kz85GlMPOUB2POTGCa1VgcNNeDywzGusdsD-_I3QH3w0yDvYbTPXkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره : از زمانی که آتش‌بس شروع شده - از دقایقی پیش - تا کنون اسرائیل ۱۲ بار به جنوب لبنان حمله کرده.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5628" target="_blank">📅 17:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5627">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZY46CnIybLWW1mW8BLpKqVDtz-UJbIwI8fcqZWCh7qKT0nNaHvIkbcjgYtU1hgVWYeT7G0cT_U5BG5tC5ajfdQPUG-Z1igYe66X2Zf0jIsydyn7VXorg4GVtOt4T7E9V9IKbR-nxO4tNVW7AdIgNyNAMpzQ489PSUZeiB8zm76WDJ5yzyQlm3wfoJOJm-lk4si4qB-WXL9UgVcD-vTwjOB5swNl8OLh7Ws_Y1TleCt480vOWWfFMAdbL4GZHgEgBHtyPDBQkKQMv93Ii8pz_-FAQbUfCedf4T6NaZ-go3wrPVUfNzCdP7ApBqPyoBgjqKw7GU68kpD1bd3Je0msC4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «این ما نبودیم که از سر استیصال پای میز مذاکره رفتیم؛ ایران بود. کارشان تمام است! بگذاریم این مهلت ۶۰ روزه هم طی شود. هیچ پولی دریافت نخواهند کرد؛ حتی ده سِنت!»</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5627" target="_blank">📅 17:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5626">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">با میانجی‌گری قطر و فشار آمریکا :
آتش‌بس جدید میان اسرائیل و حزب‌الله از عصر امروز برقرار خواهد شد.
بر اساس این‌آتش‌بس، قرار نیست نیروهای اسرائیلی - فعلا - از  جنوب لبنان خارج شوند و آوارگان لبنانی قرار نیست به خانه‌های خود برگردند.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5626" target="_blank">📅 16:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5625">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5625" target="_blank">📅 14:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5624">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh99LCTwYnsTyTnlqFnvtZzwY5LKBUs8tTka5xttXWkjoDPPNXgaJhEjTmSEquQmmpNVgGRZ5uF5wOXBghdcCF2X3I4e6LHGs5NXb5-uyrYaTspnsLUPYultGCPBacinXcqtAlJXW8fGP8wM8eJ49mFmqRGwDvLDaK5yDW6IHYG0JVpryuCocGJuYXhnx6dOkTtCKnYt0hk8tEPuocITjMRIWRXil1Z2X6IEgb1LObvmaE9saJkOqIZq028DhaPUbbRuwPVMRXoMC5GXtPeZn5G7lET0e61ncN9LXVKCaN5NTYOsV1id_m9lox1Hp0sF4sOjfNc9LByGgh-Io986cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به خاطر حزب الله لبنان ، مذاکراتش با آمریکا در سوئیس را لغو کرد!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5624" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5623">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5623" target="_blank">📅 12:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5622">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNaEnmYixfZUsj8qZho5tbGaEq6mrjKsxHkhcmvm6c_7z8cuIt9S-6wgRffdj-Mynsicg0kx3qS6ue1jExpkuOSw6X-waoMpUXWGNQ4aUsFdGnkxQoPnz2FI5kLJhvo2pTVbp5S9LSIzrkBH5NKKPiQXy4guMrN4yjxduYxp9i6uatijnb8i19-_5paAl5lKim_jw4NZxzMICNXeEb8YhSxXMjQ-n0YtDS7HLmVxIB9psZaMJkoWmk7SoHbtx1YyzxyeAUM7IohOPyDPtQJ7OcTdI9ru2wzeoPhv6Z9Wa5QuQ_kRdUWRS4_30Kd7Rj2O_YEZvAkcJRiVIcHuQAfwVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل بیش از ۶۰ حمله
به مناطق مختلف لبنان انجام داد
به ویژه دو منطقه شیعه‌نشین جنوب لبنان و دره بقاع</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5622" target="_blank">📅 12:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5621">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اسرائیل ۲-۳ ساعت فرصت داره
توافق جمهوری اسلامی - آمریکا رو به چالش بکشه،  یعنی تا قبل از بیدار شدن ترامپ.
اسرائیل می‌تونه شرایط رو طوری مهندسی کنه که جمهوری اسلامی یا از پیش‌شرط خود برای آتش‌بس در لبنان عقب‌نشینی کنه، یا آتش‌بسی برقرار بشه که حزب‌الله رو زیر فشار سنگین نگه داره.
در چنین آتش‌بسی، نیروهای اسرائیلی در مواضع فعلی خود باقی می‌مونن، اما حملات رو متوقف می‌کنن. نتیجه، ادامه آوارگی بیش از یک میلیون لبنانی، عمدتاً از مناطق شیعه‌نشین، خواهد بود؛ وضعیتی که فشار روانی، اجتماعی و اقتصادی سنگینی بر حزب‌الله و جمهوری اسلامی وارد می‌کنه.
در نهایت، حزب‌الله یا ناچار می‌شه این وضعیت رو بپذیره و هزینه سیاسی اون رو بپردازه، یا برای شکستن بن‌بست دوباره به اسرائیل حمله کنه؛ حمله‌ای که پاسخ اسرائیل و تداوم همون چرخه جنگ و فرسایش رو به دنبال خواهد داشت.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5621" target="_blank">📅 11:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5620">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_D9-fR6H-wWgQgtR0cOmrP1Xi8g4z3I_IrYiIKcskOI4bLlVQW-4g9K-4ocS3JBEAAj8npWb0t8AFG7BPlML_Jjm8bwCs1GeraFWfXoL_fHqos2BJvQ9_DIm1WpzkIab-Lp_cL0K2-uY2CJ6oEUoaLnI8ygdbIaon0NiyUHqbrlRvF_jCbsKKdBm-Qr4k1uskU3mUDmHQs2Q8C63GWb1PpX_oO-8Zm3LyBv9krciI0W6f_dkj3R2IhcHOF9ybe2YOvY0_Rs-HlS9p_UlZMgEEh5KBCux-FRpqrL2hO2wpAEuZfIW_x277mAd3SiYEA5tJvHtGG1VkUObg7pdD9QWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان در واشنگتن ساعت ۳ شبه! چند ساعت دیگه ترامپ بیدار میشه و شروع میکنه به توییت زدن که سریعا باید جمعش کنید و…..!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5620" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5619">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
۴ سرباز اسرائیلی شب گذشته در جنوب لبنان کشته شدند.
اسراییل از صبح امروز دست به حملات گسترده‌ای در جنوب لبنان زده.
🔺
آتش‌بس در لبنان اولویت نخست جمهوری اسلامی برای پایان جنگ با آمریکا بود.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5619" target="_blank">📅 10:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5616">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=tiRqZAFew111VNjbYBckXid7pfuyp1VIojMsTGNuMT-lNRPZQdT0zbqL5BJx3jFscP1PMzlaplM44Hjz6zqM0IC5z3scIfmxE-w_YFn-MSTxAIbNBBObY_3pcZLlEKHGHSdCs-s1e5igeGpKt-B_qvrZqigGDEOFG_HnMgUhsTLpkD9NU8hTyWh2O1T6tQ_qU5ZYp9Dmv4W0HZCXnxzJm4HZbXq0-GFbgJIpSoSRAU4xR8iq1NCynjYwy6NCGueJrfaQJPupo4mXWIbO0hyjew1gW0Vl7n1OQQmRu5Ej5_vxj-fU5Aa-HqCPc7mcVrv6FtDkQ9cXYaz_nElF07MhxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f85867e09.mp4?token=tiRqZAFew111VNjbYBckXid7pfuyp1VIojMsTGNuMT-lNRPZQdT0zbqL5BJx3jFscP1PMzlaplM44Hjz6zqM0IC5z3scIfmxE-w_YFn-MSTxAIbNBBObY_3pcZLlEKHGHSdCs-s1e5igeGpKt-B_qvrZqigGDEOFG_HnMgUhsTLpkD9NU8hTyWh2O1T6tQ_qU5ZYp9Dmv4W0HZCXnxzJm4HZbXq0-GFbgJIpSoSRAU4xR8iq1NCynjYwy6NCGueJrfaQJPupo4mXWIbO0hyjew1gW0Vl7n1OQQmRu5Ej5_vxj-fU5Aa-HqCPc7mcVrv6FtDkQ9cXYaz_nElF07MhxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف میگه لبنان ۴ هزار شهید
برای جمهوری اسلامی داد!
از  این ۴ هزار تن، بیش از ۷۰۰ نفرشون کودک بودن!
بله این جنگ نه برای لبنان بود
نه برای مرزها و خاک لبنان بود،
نه با پول و سلاح لبنانی‌ها بود و نه با تصمیم رئیس جمهور و مجلس و….. لبنان بود!  حزب‌الله لبنان به عنوان یک گروه مزدور مسلح
به خاطر خونخواهی خامنه‌ای و با پول و سلاح و خواست جمهوری اسلامی این جنگ رو راه انداخت و اینهمه قربانی گرفت!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5616" target="_blank">📅 09:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5615">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=fraIeclKbQm4KpjNJaVOjqH6vuIAX1Qcak96L_hxttwnugxkznB26bPu0v6zERxmWKPwNnXyYcG8_kFnUgWkH_pmbD6i673hxQ0TQgiRffYOcsRmwvSv5wql6w_9DgKD4y6W5r_Q3-lQYLsbTJmn73ARP_PvB_c51QXZ-6Uyl7U5-stFr4SckwMMLxhNb6LcsEPKkWXoHlE6DT5dgjh324DqzQRFSJY0oQ8FFcxRiPJjXQRCZZ5FqNHH8nne4eq5f15UAC0KHr9III5Fsi5Q_-dZDhx_FQmC03KfasUbjzobRdOzRzePqpfOccAxICD8Mac0DEtM4JjJuUKpxwD6xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/874e16f27f.mp4?token=fraIeclKbQm4KpjNJaVOjqH6vuIAX1Qcak96L_hxttwnugxkznB26bPu0v6zERxmWKPwNnXyYcG8_kFnUgWkH_pmbD6i673hxQ0TQgiRffYOcsRmwvSv5wql6w_9DgKD4y6W5r_Q3-lQYLsbTJmn73ARP_PvB_c51QXZ-6Uyl7U5-stFr4SckwMMLxhNb6LcsEPKkWXoHlE6DT5dgjh324DqzQRFSJY0oQ8FFcxRiPJjXQRCZZ5FqNHH8nne4eq5f15UAC0KHr9III5Fsi5Q_-dZDhx_FQmC03KfasUbjzobRdOzRzePqpfOccAxICD8Mac0DEtM4JjJuUKpxwD6xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی سنگین اسرائیل در جنوب لبنان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5615" target="_blank">📅 09:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5614">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUIQuQm7IxTEchFcV4u_35SkpCrKzuQsGTokTjrCU7pH0F-s_8lCFbOCnzELze92W3xasCGJArRvISnas71x0z-_pQXd0pRiyxlan2RvzehRHYZAFDXFmTj76UOqHpRA3CMziR_XEqGDOlAwvKJOm6qZwd8mUpuLOXomSKUQvaooWXTMpT9A7a8yAnms9iY823Z-aTg284wROapJvq4JRKdHdy1-gLvwKjYXxxHgtDDB_lEhIWrdoPZ-TvDlmXEx8WzG0qxJaf5at4-YLnwHJXv-SL21nzcAEjJwHem1Z_Cn523M7aNng1cfw3OegAOMpEwnTs6b4CeQrUczlR08uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروع شد :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5614" target="_blank">📅 09:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5613">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T938Nqx9e13Y1WlXsSXa4oz_5m1y7IY8WoV7l4dc79GwR2FHenqBpdin-qS3yx8zPzZLROyhurKm0ISkytwbBBLksGa0UcpG0xznfagbAlA-nabOsiqakY5upa5iUsyl6z4ZjKw0MTaeKF-7kDSdqNfRJjeyDG9W2K2bxrVftR1E4chEFTLTcClGkqQG9FoIlXZXhEAeurfD1DLosJPxC5RdqBX9qGHjUYWv0yHYL5vpwNnvmQ_VYtmG85IizRNcZJPr1XSK3svPsPZ6o7YzsiLOWjUaboZBYm134tY41PbwYPl755HtBpVW49pq2joMFYcJ3-ESawFd6Gx3OuM8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای تفاهم نامه را گردن نگرفت: من نظر دیگه‌ای داشتم ولی حالا که پزشکیان به من تعهد داد و قول داد، منهم قبول کردم!
(اسمی هم از قالیباف که همه کاره بوده نیومده! چرا؟ چون مجتبایی در کار نیست، خود قالیبافه!)</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5613" target="_blank">📅 21:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5612">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
ارتش آمریکا رسما محاصره بنادر ایرانی را پایان داد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5612" target="_blank">📅 20:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5611">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCzHhPmijmnyqFjpo0CMCgS7UK5csDRNstSvmg9_I_15-PH8eCERXwvlLL62KkbhFAexyALevvfCCp9Goyr6qSV82rjS9g5monbRGVvJMZo8g8YT4EoThRYd__D9k6iUkLmvQn-mXOJu5QJk7c8MfES6ucIBTTXUm3J3bmQlhU_xPXkyadV-vWMXoshrcSlZoPTF7pkEznBVMimJw8cemSk0HPNGqUimjHIkfNJ-XgDq7K4n1nkcjfNVZxalCmFgB6mQALkpW59GogaKWGmIMvHxcy-GAUFwLz_k8rs6cz8ePH6B3nDiIZuFI9MqSKqtxX4cuG9vn1GJ60J6_WgnEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏فارس: با وجود توافق، رئیس ستاد ارتش اسرائیل به ارتش اسرائیل دستور داد تا برای سناریوی حمله در ایران آماده شوند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5611" target="_blank">📅 20:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5610">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‏جی دی ونس: ‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد. توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5610" target="_blank">📅 19:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5609">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‏جی دی ونس:
‏ دورهٔ ۶۰ روزه رسماً از امروز آغاز شد.
توافق از دیروز شروع شده است، اما ما شمارش معکوسِ ۶۰ روزه را از امروز آغاز می‌کنیم.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5609" target="_blank">📅 19:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5608">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=Q9pLN-VUshdFr83YNKMRDh7o4_gacSLEU6XIl_64PLAFkyuf3zbhLtbmFFJpD1R-2LtcBcm_IqDCZPKqVif4lO2VUEH4IWt5ig1XEzCaWVM72JAg2mNxRCZLDh9ul17-f90rwcYWtR5608vEc4batQvnR_2d1X_9hV64-kCYzJOEkvgE-n7LthpM-xoGglhmxVWxnbfKrUrwle-mXux_bS8PcFSqRA6q5h2umRjJTWvPn6cz8wcvXCZrTLYDFHyQsJRnGceZZ_R1UhyxUHci9x_-4xdOBBTLrmFC4Zwu6R1CTq2GQjZxKFkygIaXYZuoE2ndkwM60R_qJnDvLpB_Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a26295b74d.mp4?token=Q9pLN-VUshdFr83YNKMRDh7o4_gacSLEU6XIl_64PLAFkyuf3zbhLtbmFFJpD1R-2LtcBcm_IqDCZPKqVif4lO2VUEH4IWt5ig1XEzCaWVM72JAg2mNxRCZLDh9ul17-f90rwcYWtR5608vEc4batQvnR_2d1X_9hV64-kCYzJOEkvgE-n7LthpM-xoGglhmxVWxnbfKrUrwle-mXux_bS8PcFSqRA6q5h2umRjJTWvPn6cz8wcvXCZrTLYDFHyQsJRnGceZZ_R1UhyxUHci9x_-4xdOBBTLrmFC4Zwu6R1CTq2GQjZxKFkygIaXYZuoE2ndkwM60R_qJnDvLpB_Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گسترده اوکراین
به پالایشگاه نفت مسکو</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5608" target="_blank">📅 18:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5607">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKz07_AdxfZ5uTVUCB5C0Aez7PScKbs80j5C6tYKy6oZF13G7n5X6-cWJTX4zOa9PhqJIqsQZXDoSOwY9Dto_qdXzJWMpBeLb5g3IvMurOsc5Vj3KIuHxAjNTUSGnUzivKqVLzOJB_EorTU9YisB-vZGf1L9Mp28Yk4Hbw_Imrne74kQdouqb-I77uQsaEsDaNU95DKVWfyNorMRUhaJ4tsW2SIe7nVLNuNVuiHzfwtIEbAru8rHrYlFpL1eZf-0Tq43531FKZbJxdmXJKLejnkdehUtHloLApdroGAwtCvmorcnFJF2_KsVGQp3LnJZ395p3eXrMFvPkGusqq3i0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: نتانیاهو به ترامپ اعلام کرده است که اسرائیل بند مربوط به پایان فوری و دائمی جنگ در لبنان را در این توافق رد می‌کند و به رئیس‌جمهور گفته است که اسرائیل خود را متعهد به آن نمی‌داند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5607" target="_blank">📅 15:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5606">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5606" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5605">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nuszPBb3GhQpJ95pB0VhEX6lDiXvGiJaBn1E4ZJvrTZSxjVYyqhWjwJVdnzyj4Wvi-rwbgqqASB66sGjY4_caB79z-qcJXr8MFEynqIG4DW7v6-JFswuCQ8dTldh0UoHYugd9F0vIojizx4TlpOUpRcO8IqDj5wVGf63zkTwq-uDqew5Elmw8j-xp81fAFmH-j_j1Eazd6WmhP-LAhFM28VTWhVz0aa7s9S6-hBg4cB3fTrMeGKUF8tvp8WD3XmhLqGDgR_qylxtHIQtkQKM8GsCypf7xAN4GjKrHvk5F6tIWgGwqHt8MiBVv4XWWzPOfft6nR3izwcH5vF-inO5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2067504670449250653?s=46</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5605" target="_blank">📅 10:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5604">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5604" target="_blank">📅 08:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5603">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خامنه‌ای دو جنگ به ایران تحمیل کرد،
و برای ۴۰ روز بیشتر در قدرت موندن، ده‌ها هزار جوان رعنای ایرانی را کشت،
و جانشینانش، هنوز او را دفن نکرده،
بر توافق نامه امضا گذاشتند!
۳۰ ساله لجاجت خامنه‌ای
که هزاران میلیارد دلار به ایران زیان زد
و جامعه ایرانی رو به فروپاشی رساند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5603" target="_blank">📅 08:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5602">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbDxjrk5dTqNgiqcYh1RzCp9AwwYPKWUXvLHEXaJzrj02BVuZFtfVmllg78ZBn5shiTSSAY3D_6ylR7hLqMbw7x8wevvn4aaEf7SJCKvmP0P8Aj2nck1mv1uQw5kCk8W9ROiQgGYFegiePIa66sb9kvSm8xPB0j_krIZJbZ_fj5jNBAJJby6rf-HVxYDvLY4VP7HaxDzdMe35xEhSbUJ4VzDb6RwWFLCBFCss6MmlErIdZJJIiUnGWWFJz8h3jrIMB6w2zOHdB7ftcHvid0AtRh6iLDBZru2AxKKPYBWRIzDIUfMRB-pdBxbff7BRNVW96iudPAFnkW0zQxfQlzLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت سال ۲۰۱۷ ترامپ :
«ایران به آخر خط رسیده بود و آماده فروپاشی بود، تا این‌که آمریکا از راه رسید  و در قالب «توافق ایران» به آن یک طناب نجات داد: ۱۵۰ میلیارد دلار.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5602" target="_blank">📅 07:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5601">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9SlcujO9rW4yDcO6ESrJnPXNeAB6kGrcSkjik2FV3cGbNiUbyZJx2GUw3EjnTezx6QigGICun3WXmJiZqcZzrenS8qgxeyJ-uf5cz6A0BRy7Pitb6IIGE6Py87i_uUl18l0SVnm5CXCBgzu79VWgx71vdO9g0rt6ICmWvIx2Rtcu0Q4zn7I5vpxcFfWrmt79y9FYNgqWz-VpqV0irfO9Yz58VRWYxIKYc_tjvcx9s4rHxCK_rwnk2kLCXX9inzWmLNCaUbGNLORPedkYx2sSCveDk9xEMWEWZvQzxn5EGlYk5AyU0bDYRvIfMCjTEYqB5MOxfbmCb36oYljPBks7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی  را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5601" target="_blank">📅 07:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5600">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=rWcBt3oGZhtg1IxooY0TqaQpZzjGSmCh5-NF78iOdPXCqERUV9DZDAzDBbJnZ6ig4tfWR_0-PK6R-Mh26XpS4qE1pyCts05jenx43OroCTD_D57aX3vp6t7o9JWCv9CvV_d-LKyZkxDsvhJJ0SNhVNUI80h_-0_joN2U-v2Si4oIFultcy6Z1J5U4TpZXxYVRAZQjnTKO_nOpoSoRxiiZKUt-HF1DT_QwL-R-q9xT9Dx2HssMQLmkFfCQsiEgzkOwRZEZiT1gN8M9yurPqlj5yeicyYPj0nopG8LfIZ206SLirPZ-xOm8HmKctDBiR0ZJSJATkCFw3SeBfGZTHEKSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beb54ade63.mp4?token=rWcBt3oGZhtg1IxooY0TqaQpZzjGSmCh5-NF78iOdPXCqERUV9DZDAzDBbJnZ6ig4tfWR_0-PK6R-Mh26XpS4qE1pyCts05jenx43OroCTD_D57aX3vp6t7o9JWCv9CvV_d-LKyZkxDsvhJJ0SNhVNUI80h_-0_joN2U-v2Si4oIFultcy6Z1J5U4TpZXxYVRAZQjnTKO_nOpoSoRxiiZKUt-HF1DT_QwL-R-q9xT9Dx2HssMQLmkFfCQsiEgzkOwRZEZiT1gN8M9yurPqlj5yeicyYPj0nopG8LfIZ206SLirPZ-xOm8HmKctDBiR0ZJSJATkCFw3SeBfGZTHEKSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم نامه  با جمهوری اسلامی
را در کاخ ورسای امضا کرد</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5600" target="_blank">📅 07:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5599">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">تقام‌نامه ۶۰ روزه بین آمریکا و جمهوری اسبامی امضا شد (الکترونیکی)</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5599" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5598">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vabMplQHCRPv7cVBYw0ihzq1sfY5Hnc4ayAjYoq8W-x8l6VFeZ-nq37_ukJL1qbqCbTNveUqgFbUT-IPEIeajIesclkT6Obun_Gl2bPqrtKYuqPHb8Z3kzcPSmgF_xdV6mEFBqfRW62D2eU66esPyD6HneV5aGZbdvpgHpa5WA1nWOuI2hACEL4VUU-9rgD8sPURhOTMjgm8_VuqvCnfSQCfQGvi0nlEw5WhmuAlTlDBcUIVbmiLDyo2DkI5zdwSwfmJKJ_9m4LCRksMQGaJ5K2kNJS5Tme3qx0dpzFSzAL9mEEbCX604LJWAKZinKlIjwMwbSCO_d18mXqUeoD4Sw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5598" target="_blank">📅 00:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5597">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=eNkbCNrJRIoKB7_593HCOwV11YwE_xMF4n_gDYKhQaePrraBxgz-d_VeJtLftrF9G0ZReFBXbNE4du47j_5JAuLY9idF4tZ5s4iGAieNaFdMAJJNcm6ttShBGJtSmGMJPmt3qyIz99TLu-AFtI1sPf6Ym_aseOsxMSSmM2D0CdYN4XTsWRXRRShYZOjJqmPGH83Msz1jC2l32OdbmzpzJTAQ4xDH21yzClwDlEOcOUk3OyUsES26BeYKprvFPQmpTMWKOwbnfNlnDe53j-xDG1iMwcC-DT-Uys8ih7IEvwtQnnygxu48qlyaiqfFlegdzH6dsOQQSlWAkuYMPA-lig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07cb3775a.mp4?token=eNkbCNrJRIoKB7_593HCOwV11YwE_xMF4n_gDYKhQaePrraBxgz-d_VeJtLftrF9G0ZReFBXbNE4du47j_5JAuLY9idF4tZ5s4iGAieNaFdMAJJNcm6ttShBGJtSmGMJPmt3qyIz99TLu-AFtI1sPf6Ym_aseOsxMSSmM2D0CdYN4XTsWRXRRShYZOjJqmPGH83Msz1jC2l32OdbmzpzJTAQ4xDH21yzClwDlEOcOUk3OyUsES26BeYKprvFPQmpTMWKOwbnfNlnDe53j-xDG1iMwcC-DT-Uys8ih7IEvwtQnnygxu48qlyaiqfFlegdzH6dsOQQSlWAkuYMPA-lig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیایید برای من تصمیم سازی کنید
تا من تصمیم بگیرم!
قالیباف همون مجتبای پنهانه
مجتبایی در کار  نیست!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5597" target="_blank">📅 23:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5596">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
ترامپ : یک کپی از متن یادداشت تفاهم بین جمهوری اسلامی و آمریکا که قراره دو روز دیگه در سوئیس امضا بشه رو برای اسرائیل فرستادم.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5596" target="_blank">📅 19:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5595">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
در حمله پهپادی گروه تروریستی حزب‌الله به گروهی از سربازان اسرائیلی
۵ تن زخمی شدند
وضعیت یکی از آنها وخیم گزارش شده.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5595" target="_blank">📅 18:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5594">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=J0f70qGAJE30cH5EOOAHbzhH5gKtI8R3Zg4fh0Vf6Nihydm731F1e72Bk7msg24VJFX-s6GXoS7yvlpDo_SLEKLYzJrxgh6nsmdM2OhA_SkfUNLMBe3KNi2b9P5KLMSg2gLeGdpmQyGl-BP2uWpyUmOICLdxBPrZrg5iCbirWh4iyRUJBZUxkTc8iEzh5WzSbkNwbVzcpyEOtwAxsLQf4rJk_1KsRfs4k4TFIqA3F5iWGoWA7VSVWwmzmU2K8xF8AtdRaPip5cyA5YXyaNQ7OEHQDoQqC3XZFbo4ihvCI0t7kpv8Y_FveyH1kNjVXp0YMSRO1OOknzGXkE6QhlBH9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a303f3592.mp4?token=J0f70qGAJE30cH5EOOAHbzhH5gKtI8R3Zg4fh0Vf6Nihydm731F1e72Bk7msg24VJFX-s6GXoS7yvlpDo_SLEKLYzJrxgh6nsmdM2OhA_SkfUNLMBe3KNi2b9P5KLMSg2gLeGdpmQyGl-BP2uWpyUmOICLdxBPrZrg5iCbirWh4iyRUJBZUxkTc8iEzh5WzSbkNwbVzcpyEOtwAxsLQf4rJk_1KsRfs4k4TFIqA3F5iWGoWA7VSVWwmzmU2K8xF8AtdRaPip5cyA5YXyaNQ7OEHQDoQqC3XZFbo4ihvCI0t7kpv8Y_FveyH1kNjVXp0YMSRO1OOknzGXkE6QhlBH9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏قالیباف: باید سنگر را از بچه‌های لانچر تحویل بگیریم و مردم را از زیر فشار اقتصادی دربیاوریم</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/5594" target="_blank">📅 17:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5593">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k--CBVdJVajXLcSv2ZWKgf9MQ_MBgbYiGaPDjKu46EpEgjTsjiZktokaeRhTEeNeoxOAl8CIfgMxOz9teiS2bTBfRNrZwCaX1jM2Or5RvUxnbny8Gx8X6Pc6az04MkWsc4JHPjKJu8ReUvrR6siAEyc57WwPxo5hifeRfLwftnG4oC8eYig9teYsMYmloNp94Ialfr5IrnITfx14DIatDIVgrApO0Hr-N6FUxOL2jHJTOOYUWh_Fd4YIzjs_1L3CIE91n6GLT9qvrLtv_uX9DHAbJdORQwI66LEaDsf3SVu_UO-fJKM4NaVJdzotDOZLOAzqt64LbyIAF9j9RV9mDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ دیروز به شدت انتقاد کرده بود ار نتانیاهو برای ادامه حملاتش به لبنان
و بعد تا جایی ادامه داد که گفت بدون من اسرائیل نابود میشد و …..
(به اروپا هم همین رو میگه،
به کشورهای عرب هم)
ظاهرا نتانیاهو خیلی با حرفهای ترامپ موافق نیست و امروز در لبنان پیامی هم برای ج‌ا فرستاد و هم برای ترامپ</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5593" target="_blank">📅 16:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5592">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.  چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5592" target="_blank">📅 16:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5591">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون! اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5591" target="_blank">📅 15:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5590">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=k_h1NH78AlNlPm_bVRGORAEXRN_Eiy9hF65-CEMBbJg8DkWhlKnIPYAQq0dXavhCLVlhNy1LxY5dXa7j9bo8PCUV12otcVUAJyQEwpRLk3UmcWXQUY5ba9FZziZAVf-reTrIs7qZD6my-2pN20l1HMrnBQAYn0WZzgnjgFO96RVGbd6V3DsOHUUIOKUMMGXP-sj6cd1dMSIk9n_10lO3Q-wqGk6BVK6wEZvqF4jV-oQYpzGjHK3lHX1PIQ-gkSU2rRpvTot6P1-rWUJeWQVr9rXme06YnO3ner7UTnuN9uEMlx0D1X1UQgKHuOxi5zOMIwluaPlbeQF2Q-QHJqjaNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b324d61ab0.mp4?token=k_h1NH78AlNlPm_bVRGORAEXRN_Eiy9hF65-CEMBbJg8DkWhlKnIPYAQq0dXavhCLVlhNy1LxY5dXa7j9bo8PCUV12otcVUAJyQEwpRLk3UmcWXQUY5ba9FZziZAVf-reTrIs7qZD6my-2pN20l1HMrnBQAYn0WZzgnjgFO96RVGbd6V3DsOHUUIOKUMMGXP-sj6cd1dMSIk9n_10lO3Q-wqGk6BVK6wEZvqF4jV-oQYpzGjHK3lHX1PIQ-gkSU2rRpvTot6P1-rWUJeWQVr9rXme06YnO3ner7UTnuN9uEMlx0D1X1UQgKHuOxi5zOMIwluaPlbeQF2Q-QHJqjaNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ترامپ : تفاهم نامه با ایران پایان کار نیست، اگه خوشم نیاد ازش، دوباره برمیگردیم و بمب میریزیم روی سرشون!
اگر رفتارشان مطابق خواسته ما نباشد، بمباران بازخواهد گشت!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5590" target="_blank">📅 15:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5589">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یه سوال اگه ما ترامپ کشته بودیم ، امریکا میومد با مذاکره کنه یا نه ؟
اومده میگه کشتیم که کشتیم بیا مذاکره کن یالا و هرچی هم گفتیم باید گوش بدی
نائب امام زمان کشتن و گفتن بعدی هم میکشیم یک صدا از یک مسئول درنیومد
اگه الان رهبر جدید مارو شهید کنن کی پاسخگوعه؟
دستم میزارم رو قران یکی از فرمانده ها گفت که نزارید نتانیاهو این ده نفری که اصلی ترین امام های کفر هستن زنده بمونن
الان اون ده نفر زنده ان و اقا شهید شده</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5589" target="_blank">📅 09:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5588">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">قرارگاه خاتم‌: اسرائیل طی دو روز گذشته پس از اعلام پایان جنگ توسط رئیس جمهور آمریکا، ۸۴ بار آتش‌بس در جنوب لبنان را نقض نموده و همچنان به جنایات و کشتار مردم لبنان ادامه می‌دهد.
چنانچه ارتش رژیم صهیونیستی به شرارت در جنوب لبنان پایان ندهد، باید منتظر پاسخ سخت نیروهای مسلح مقتدر جمهوری اسلامی ایران باشد!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5588" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5587">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=Ifd4lHFfe2eCcVyeKufnQzGWQVFxfp5wRbvInmkQDTpb-dP7PYqwniW4Tm_tARAqpYwGjHZqXB-_5oZxfyjO7Vs-zcygwgAUhGvz1ILUaZduoHEDnLXsY_To7UeEDDMTIOJVksgLoNKYT63poaedOaqpokhJwdtYP3p5FYn1OIxfMgi0QZp00iYlCkhQG5X-1MsVB9VGo8udHRirKUxt_afuqPX04rAgW5fyAap2wPq9NNzdrZqsP_WWJFTU7zmSYQlSqP3UXOHgpN_3Vh2nvrh-QYQxLVxWnzCbhAL7z3igE_zMrZ4Ql7NiLBBPCEnA7D3XThoRixkb8AsYnK5fGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c06210b9a.mp4?token=Ifd4lHFfe2eCcVyeKufnQzGWQVFxfp5wRbvInmkQDTpb-dP7PYqwniW4Tm_tARAqpYwGjHZqXB-_5oZxfyjO7Vs-zcygwgAUhGvz1ILUaZduoHEDnLXsY_To7UeEDDMTIOJVksgLoNKYT63poaedOaqpokhJwdtYP3p5FYn1OIxfMgi0QZp00iYlCkhQG5X-1MsVB9VGo8udHRirKUxt_afuqPX04rAgW5fyAap2wPq9NNzdrZqsP_WWJFTU7zmSYQlSqP3UXOHgpN_3Vh2nvrh-QYQxLVxWnzCbhAL7z3igE_zMrZ4Ql7NiLBBPCEnA7D3XThoRixkb8AsYnK5fGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواستم بنویسم هنوز کفنش هم خشک نشده
که حرفهاش رو رها کردید،
یادم افتاد هنوز تدفین هم نشده!</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5587" target="_blank">📅 21:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5586">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h29gpki-JQL79pPyOkAxn1k5qq9m5YVwvYQ3f22CLeSBD0-ypUOd8DO5TVx4_3a5aEADCBs1RLRaMIgMCQTilrXmijBKwjZBduSsW-q2pLY0026Qhwug_igP3g6oQ616M7Kf9HFLnwPnaFUWxKD_QGne88URDVzDtrGzonf8ytCErK1dG34xq6tl3G-iJbKU8X0KWVFEEhOfZKJtsdKW7C5v5HQQWHaQwqoM4tfL8YYR6DNwpxo8t0P9rzsWmFl3i4EORiQCW9U4C0zMrqbVABJBv0EI_zNIn78VFsCYLw1OsjAezHhrYdDzFBEFQFZN9P1BNMp-L0vG5NC7KsstfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات گسترده دقایقی پیش اسرائیل
به جنوب لبنان</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5586" target="_blank">📅 19:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5585">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">واقعا فکر می‌کنید اگر جمهوری اسلامی
بمب هسته‌ای داشته باشه،
دیگه «هیچ توپی تکونش نمیده؟‌» و
امنیت‌تون تضمین می‌شه؟
یه سؤال: اگه بمب هسته‌ای چنین تضمینی میاره، چرا همین امروز با اسرائیلی که ده‌ها کلاهک هسته‌ای دارد،  وارد رویارویی شده‌اید و هر روز به حامیانتان می‌گویید «پیروزی نزدیک است»؟
اگر سلاح هسته‌ای واقعا مانع شکست میشه پس باید صادقانه به هوادارانتان بگویید : نمی‌تونیم بر اسرائیل پیروز شویم، چون اسرائیل بمب هسته‌ای داره!
اما اگر معتقدید می‌توانید با اسرائیل بجنگید و حتی بر آن پیروز شوید، پس خودتان هم قبول دارید  که بمب هسته‌ای تضمین مطلق امنیت و پیروزی نیست!!
پس چرا بدروغ میگید که اگر جمهوری اسلامی بمب اتم داشته باشد، امنیت کشور تضمین می‌شود؟</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5585" target="_blank">📅 17:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5584">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PiKWejxzmAyujLCW1RpwI5Dc_aZcvyF7ok3XNZZHbiwwVzLvvfpTAZJFkh7Gs540fnghrSJZbb5IRT_ZzbY-C36NQv8q_lsLaijlBSQeUrRfqwjrO-GXsMtrigU4ThsEocuh66arhh73cHlf8wvBNFQ1OsEiRnkCnpa2mex7F7uxAQWo2_I-imA0fRU4Mj7Kt5c1GLnhyLzJfavtYfaM79K3Nb3e5tQy2xzH7cqLF_VZwqYHFnodwil-iEnSsnwiDFTVINEoy3BRaqUx8g_FI1UdnTNTr83NTsTvwD_c-n3Dc52KyICxYjWLsrAgCDs7YJ8FBio6pG4tGkUSNIu9bA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5584" target="_blank">📅 16:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5583">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ : تحریم‌ها لغو نخواهد شد!
بستگی به رفتارهای جمهوری اسلامی دارد
(اول صبر می‌کنیم ببینیم ج‌ا چی کار میکنه بعد در صورت نیاز، تحریمی رو برخواهیم داشت.)
ترامپ : صندوق ۳۰۰ میلیاردی سرمایه گذاری در ایران کار رسانه‌های فیک نیوز دمکراته پایه و اساس نداره! (البته این حرف رو خود ونس هم قبلا زده بود که الان ترامپ قاطعانه رد کرد.)</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5583" target="_blank">📅 10:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5582">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyVpqM7iuZm5RYbXoBBHbd6p5KFVOxeJTaf2A25pCqlzMdhk5liuag-jrvrBPq-Kkx9yan8w9xtBSTDV7_EEyIReGrDqHgObI7MYmfkIrhb53XeE-2xgZyZWVLMmulH5j7dYV9opTgCG0CTZppFHfHqwKdvr1ry-5CyL3jbypSUOzptzGVzVxvul6j67U438uTKp0-pn8yPyRlymewiqDzraSAMMUxtQEnEopzAvS_I0o5O87v7SUOaEgqv7gxmOuQJEllhHOeKxk2ESqrtOi2YszQkKyr3NgtcaRxbIdIdBH2DcGzt8XDVg-z77xg8xt-f0IW-1ySKKR_tSNzHHJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موساد و ارتش اسرائیل معمولا نتانیاهو را فردی معرفی می‌کنند  که بسیار پر سر و صداست، در حرف زدن جدی و قاطع است، اما در مرحله عمل، و تصمی‌گسری‌های بزرگ بسیار مردد است.  بنت اما متفاوت است او کمتر حرف می‌زند اما جسور و قاطع در امضای عملیات‌های پر ریسک و ضربه‌ها.…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5582" target="_blank">📅 10:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5581">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAuTslEUiVOoUhlc-7_yhe1h7mrPHRxfDZHzEcxnd1hXvrc7iogsumn1q1OcnbtUSZEHMUIUcYvMNUrfAhu2RQJhE-F-PwK8ZGQNFC55asezZ3CEscd5l12_PGo27nXQedNHvsTwqO_ff3n-dCiS5CTOPGS1edu5Ojdz4FmHyruBzRKZ9aUuQaypifZdsR47OZSYuK-J7FBcUXMJu5HkTGAJoB1lBBanmg4LQuEiN4KgieiizpAHjzHOdh5dkffpLBLfHTe5wWPh859wIryygpmdWmnEeHC-M-Qr99SVWfcrpBjQGaxKHMFXj2IfMvk2dUx-SOg7IpTjzZ2bobwY0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">او که از منتقدین سرسخت نتانیاهو در زمان جنگ ۴۰ روزه بود و به او انتقاد می‌کرد  که ضرباتش به اندازه کافی قدرتمند نیست،  و اینکه نتانیاهو زیاد از حد تحت تاثیر ترامپ است، دیشب در یک سخنرانی نیز گفت که راهبرد نتانیاهو موجب شده است که درگیری‌ها طولانی شوند.  او…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5581" target="_blank">📅 10:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5580">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=FTM6veipjUTbjduUA-MHnulfJXxuzz3Wd-IZK3VWg8lFv5H6ST2aXgSV3GooTeVKavkw3qu9ZSs2bcy4lyOzQg8KP4nrNZ96cOxBwfYSVJuvIKteJTL3qZ9HD7wBZHzPm7OxIWb3N5PkPOnrF_DyOfQCvqyzSjzVaJc7dvIqLqOfx-95fhtWSMiocSAY13g7e-2e3yr9Lsv6y958h5qK4rUR24l0AqD65uVxV7UYja9rpH4LQQtVoDpxK7wAmqn-kXpYSYbi7irQKRtgwv0CQds7cnePXOkVacw8so5LpzCGeee7t824_v4YSFWl-T-hs_FvsITeRukxteC493tJuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acbde994cd.mp4?token=FTM6veipjUTbjduUA-MHnulfJXxuzz3Wd-IZK3VWg8lFv5H6ST2aXgSV3GooTeVKavkw3qu9ZSs2bcy4lyOzQg8KP4nrNZ96cOxBwfYSVJuvIKteJTL3qZ9HD7wBZHzPm7OxIWb3N5PkPOnrF_DyOfQCvqyzSjzVaJc7dvIqLqOfx-95fhtWSMiocSAY13g7e-2e3yr9Lsv6y958h5qK4rUR24l0AqD65uVxV7UYja9rpH4LQQtVoDpxK7wAmqn-kXpYSYbi7irQKRtgwv0CQds7cnePXOkVacw8so5LpzCGeee7t824_v4YSFWl-T-hs_FvsITeRukxteC493tJuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">او دیشب در یک مصاحبه گفت که دولت جدیدی در اسرائیل شکل خواهد گرفت و امیدوارم که من رهبر آن دولت باشم و میخواهم به جمهوری اسلامی بگویم که من بدترین کابوس شما خواهم بود،  تا زمانی که مردم ایران آزاد نشوند و  مطمئن نشویم که شما سلاح هسته‌ای ندارید دست از سر شما…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5580" target="_blank">📅 10:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5579">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieKDIC6aJ4RDaEoCZqGPdMmXPI-XfyDzA1QBBbCP6d5_sacLzDW6UCEJH6wjaIJqUVs2Yz5czb1CgOTborQGvbjtwCRNLkc0p6zU4mKsoAHgbIa9jBQj-0goL3W3dZLlBsqaTSgXgAoagU2GE_s9J33lwhccjoU3CBhhDCIIZtmqC2gZ1mEK3jPqI51s0yD2i7zNI-vK_J7K_-zBeLGXT08jHya9og1MTIO5zVWtVPwMKyADydpfFkQJOYRe-gR9buqUUN_ZGYRugtcdem8d0n5rofWDumXawW0bCO4XTyRJktO5z4_SI8JQ0cSY5QyPFf1r_MEoQIAma2eidjSeQKBc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07ccaf02a3.mp4?token=QcWq4POyWYeTHZUovg6WowBqPHBXp7HerpiZBFpFa13V3rjWCJrsIRZT7ckPrcvJs8peksS7XeYEG2IwEOV096T5sR_W9XlavTvSssQ44rxJAUCdKNdpuhIa4VSNIWt8qpm6g83z8BMRSvNIavxX7VSURPk-aCF1DkwP6h7Hj67_R7BMaa-Qiv9nv5AQwn7y0MlAmCvhzE9yE84fZkmC7ij7hkqXxgk0qDio7c98lqwTGVfMI_zdK_HfdA6KJvpiYwbQUtpPh5d8dnDPRyDrdNyRMTFGl6LG87dq85i9_ckTx4sWHbgrlLjhN-zb8al3P7fmgJZddjtwMGZFw4LieKDIC6aJ4RDaEoCZqGPdMmXPI-XfyDzA1QBBbCP6d5_sacLzDW6UCEJH6wjaIJqUVs2Yz5czb1CgOTborQGvbjtwCRNLkc0p6zU4mKsoAHgbIa9jBQj-0goL3W3dZLlBsqaTSgXgAoagU2GE_s9J33lwhccjoU3CBhhDCIIZtmqC2gZ1mEK3jPqI51s0yD2i7zNI-vK_J7K_-zBeLGXT08jHya9og1MTIO5zVWtVPwMKyADydpfFkQJOYRe-gR9buqUUN_ZGYRugtcdem8d0n5rofWDumXawW0bCO4XTyRJktO5z4_SI8JQ0cSY5QyPFf1r_MEoQIAma2eidjSeQKBc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفتالی بنت، مهم‌ترین رقیب نتانیاهو در انتخابات آتی اسرائیل است،  در آخرین نظرسنجی‌ها محبوبیت او از محبوبیت نتانیاهو پیشی گرفته.
🔺
بنت قبلا هم نخست وزیر اسرائیل بوده،  او کسی است که برای اولین بار  جمهوری اسلامی و نیابتی‌هاش رو به  «اختاپوس» تشبیه کرد و اعتقاد…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5579" target="_blank">📅 10:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5578">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUDQrFYmT-AhTCJ3fFECZZBfzhXUwvikTQ-JxYfeFESZDf8w4H86GWndrf0v51-IsU-dYyucfp0gEa9_E9N0-mmnumH14YRHqie_obGpEa-0JZOLD1PJVtYBdh52d-MSmXoe3RzM75GfmXbEM3Q_9GVxuF2bDsB7jFy1FRJdDps43Sv7n0rTzuwFUhBkvyclnhY-Iz0RPN_QSHmiCUnM4g1lo29z8WRgbxxvsBRFgEC8ri3vgpGY3wSf7sPvnfgw5TPubvsdgmxPE8Rt1OriFtWkWfP_zJAEVk1gKgNK6twI34UYNozfYsvlfmaGrxt5L64Ujzfeh6UWoc2RlsIagw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FolYG9rPSpPqdJNOFjkvtlCif2TReAVAExrGE5qEmGOI1zD4gp3y2UT51Vj1zzDsJWVHk3VdqYCbdZEmMhQNvONtkRlVaOUY9Q0wKFhZqmcHs6Q4DDK2PAHVyCPoh85IYrhyjIRVaZdDTUvfn6dL0on-Ng6IlXqfSnEwuhs30PANz-PJDW1Ea20qhihIBren7nCgxw6plALiuk3NqztdaXoiU8JgYQ4TRnE9r931iWG7aheNJ7tee7hwV-JZOcXOw_d4Fux9eF0nacC4b05bASt4AYn0V61vLEVGDosvX8UICKDnyuy6NB4hKdwT4wreORCScx0lcx_s9zpA-kmGoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اول هسته‌ای، بعد موشکی …
‏به مزدورهاشون که هر شب جمع میشدن، گفتن که چی امضا کردن؟</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5577" target="_blank">📅 09:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5575">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9jKowVRnfbbZ4zLdCA4jFX8NtbN6gaShSlsZAZbIA3n4trNmtSzS6letZGwFBt_uqZoe4t7uSwpqJ6aQlYtSGTAfd9TIq6wAgaizmEh2mzVpc16gSwjYw3Xypr8QGjlRv395k6jWeLIahbmTVtHlvvgetLSga21LFhdOvWrSJxhjv9M8ha0Rbt_dhpUwMiT_2H4eDAx1Hg4so67oVne4KqNgcWxF8SBSmXmjtlItg8OcMXvaOcUa2bb_UqvpKnDXJZzDpga8ORjsSL1x2mcvMMqCtlK677UCyyicQFdyQX_HuHqFt4XnIFpu3zM70qv0hxzWo_LIVIPgaJHZLeeRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l5HyzDtAmVn4Kq2XMInDA9gpG0d_tcox2IcVIMD4KTNIXveqprqFI6K0IHEF3ytge6mEC_GkpIaCszynF9ilzj9--tFCbJH02MbQmaP4FF9e9nSZr3tgl21G3-JHjWY-9G3xgu5h4kAp6RnxCDam3RUuxKewyEv0VnJQ9KjcR-aLUc83C1kQ5UQ3ga9vX5EPbGqTfEqmv_j95We9yJxBVg_JDx7_WXyisRegDoshr7oGLfBaMjUXNszVYGY5fWbyeNdrRVf1rpo07WQmivjsuDavjh5hAhRiV5khtWpGCWqsp2tTSTSRYd6bxZvpXHNYrVi6va2YkyvLj79Nm6xPaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین شنبه زاده فقط و فقط یک نقطه گذاشت!
نقطه او ۱۷ هزار لایک گرفت، دست خامنه‌ای ۷هزار لایک! رفتن گرفتنش و بیش از هزار روزه زندانیه!  چون فقط با یک نقطه دیکتاتور رو در هم کوبید!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/5575" target="_blank">📅 09:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5574">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0A-LNVSspxjRiCEAL8Or1cZ9lx_H01lk1MMitw3AiVaZ7goq-fid2GH14CwW6V6hEaGgd6jAxrzTYd3EwrE39vBCpyY3CjqJpcWmwQa4OLq73CAsDNd9kPpNI7xh5iHvJV6qZc6v03Qx1vR9vIRqxKUCJxUZOwEoIyjsRG-3Iz85GINWokFYY8PPzKUNFByyUZQyTJBDBqq4GBrv9mTF2pzG8MZ6ddCZWRU1AnAiQrMRF9oafgt4Z0A1aLYntFLSde1C-VpaUZfQUteJg4stU6XoLKBOciFx1phOtmG_dlAsTnXnMlCjbHoY-MHzXBTsPC3aahRt-HnY7VbXd5osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیده شدن صدای سه انفجار در قشم و تنگه هرمز</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5574" target="_blank">📅 01:14 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5573">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=SMCxw7SsnuEfRD-bRxVifm5Y_XlAEkGW2e0C710Sqc_phD_9r05QXQj7ZYxxdHWuhNp1MVhb5gmMiKqfWQ4v0f1A5fbTO_8UPimxAfL8JNRZvtGSPmzg9H51Mm-UdAn4a1247bPeEPwdf4DjttnDjxItS3kPJjChG2pYrcHh8CkkHFP4ML0XysAS_hPiAGJHhkl3BZ0tY_uNN6jLQQdh_ddqASF8Y1CytRjWVpXlfGfleKjRr54BQ4l03xAL3XwR_c3iPiFwcyDa-8Vb1EUdt3IlbAqJvTQyzdBtJg9un84663t4uUR-jWHQjim1wDdk4aQnevj43rBg1LsfI6IwPjBf51T8wgNVcjnil1FdXDT4uX6CSEnMW5fpua78jpmISNFNGYW6gAdTXzBRrqWyzakK7GTMA5JD33P2icdzDZpqY0Y2gUGlcLQdOvcxQTbdBADTrJvcVrnzNJ7jSSs8-QD31OdIXwNCl7VCcSMcPHTUvZN4riF2HR45_O0GzPJcgph8gFWkghFeOfNS0mymBwgpEMOEDjJivruVOGRiWpaOGA9wal3gNxQnRWcEsAxNWEklRjc7E58__0oY7qYvl_KKzfH6olxmGyeBikQmoM-6CBL6910AQM0jDm_VnZaDXqja54jpzD6ai3irMX8EcqDhvwjEhckGZ1xfjUh37e0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339b1d2d78.mp4?token=SMCxw7SsnuEfRD-bRxVifm5Y_XlAEkGW2e0C710Sqc_phD_9r05QXQj7ZYxxdHWuhNp1MVhb5gmMiKqfWQ4v0f1A5fbTO_8UPimxAfL8JNRZvtGSPmzg9H51Mm-UdAn4a1247bPeEPwdf4DjttnDjxItS3kPJjChG2pYrcHh8CkkHFP4ML0XysAS_hPiAGJHhkl3BZ0tY_uNN6jLQQdh_ddqASF8Y1CytRjWVpXlfGfleKjRr54BQ4l03xAL3XwR_c3iPiFwcyDa-8Vb1EUdt3IlbAqJvTQyzdBtJg9un84663t4uUR-jWHQjim1wDdk4aQnevj43rBg1LsfI6IwPjBf51T8wgNVcjnil1FdXDT4uX6CSEnMW5fpua78jpmISNFNGYW6gAdTXzBRrqWyzakK7GTMA5JD33P2icdzDZpqY0Y2gUGlcLQdOvcxQTbdBADTrJvcVrnzNJ7jSSs8-QD31OdIXwNCl7VCcSMcPHTUvZN4riF2HR45_O0GzPJcgph8gFWkghFeOfNS0mymBwgpEMOEDjJivruVOGRiWpaOGA9wal3gNxQnRWcEsAxNWEklRjc7E58__0oY7qYvl_KKzfH6olxmGyeBikQmoM-6CBL6910AQM0jDm_VnZaDXqja54jpzD6ai3irMX8EcqDhvwjEhckGZ1xfjUh37e0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«روزانه داره ما رو تحقیر میکنه
ما رو به لجن میکشه ،
به رهبر  تهمت جنسی میزنه»</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5573" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5571">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHkjCBul3yvw3XqF5D7B77FlaZLQ07RAw66DRfRH0oPBzzVq_yM0ObKUfEuIcnnHxCNhhS3lu35_-Jf1-f1NR1mHLY7qmBAeWdniIMePCF67Eob20XaC7CES3_evpUr9oFmFVJZIlkVN14gO0gLVeMPK_X4ERDX2X4ecOe6xciyNPSKFA91RsYdzs3d-3DZcIDg9xL1DSWHRD26UGbdf3OypReh1KUCW5IvCtXAi6VJA3STi404FyapNEl37TARM8u7LGQ6UUZrRa_gvp_tS6pQAzBnbHdP30fNvn0f22xs3M4fpSV4OZa9v7WbmcZfdseVzRDWQXy6_m-992e7CVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=UAYJ90nTd6pgp5aizlVmu3um65FXB5B9ZE0tllVExYenLJF7_0DMb4goHTf1I9Mwfm8fYOIOo6M3ZY0QlSPgrF1rV2ACKidvJuorUicMLZfG_elj6yN1umce7tvjFwvxu-58VO-dOOh-3g_KbXIOqbAVjX5XE_3evww41n5lx-74VltvMo-d-dXomHVLlwC-VOH2qSVu4Z5c8lTIh_CbtZaJcd-x9J5_LtFO6f3nSovYVPp06VuLkbSjDDXyYmDg29fYbYtqQUK4M_hkR2jveRWv2W2r2O0KCMHSngFvFhlvIdFBl8S9ALn_WQMNYubnHPB9WVBB-VfHlu-71po-Hoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6704b6dead.mp4?token=UAYJ90nTd6pgp5aizlVmu3um65FXB5B9ZE0tllVExYenLJF7_0DMb4goHTf1I9Mwfm8fYOIOo6M3ZY0QlSPgrF1rV2ACKidvJuorUicMLZfG_elj6yN1umce7tvjFwvxu-58VO-dOOh-3g_KbXIOqbAVjX5XE_3evww41n5lx-74VltvMo-d-dXomHVLlwC-VOH2qSVu4Z5c8lTIh_CbtZaJcd-x9J5_LtFO6f3nSovYVPp06VuLkbSjDDXyYmDg29fYbYtqQUK4M_hkR2jveRWv2W2r2O0KCMHSngFvFhlvIdFBl8S9ALn_WQMNYubnHPB9WVBB-VfHlu-71po-Hoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین فینال رژیم منفور شوروی</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/5571" target="_blank">📅 00:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5569">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=fhJESHPClAu_ZMt_8mD0wqDJnjhRpqHcS3XM7V10DJ6GHUvwtXtgWjYTBOwGpoXZG0BcfcCjhpkO3I31xKUiq3vii1aeZLT_7eDxDE4kM8HBKBaxVBmWaJbjxkUhQdNMqxo3Z3dmiYHu7zaMHwKeNs_Zn0KpAvYlPicuR-cG2MfodKxq2j5mUX__pXe_5KX-TmBtFYbTF9ynpBOVkKjMyMi7YWJglVFvzeHk2RAtrT-NUOYX9RjmGy68ImRG2u1y7P0DJkXC6cj3YhCXNNk5fQCCSsET1CfCfNRfRcUYUthWZfZSDtFwuEOpr5bum2GK-hpAjb1e7caWJeAWvPNlI34S9a15XyMlZ6vBvmmnIWug2-1hyn36nmFlrkDJrRY5P6TqI_oHkhgh-_Ea7GgIu5XG184P3gQaTa0P4dE0WV-aOv93hqlXFThCg6W6Gk5s3Fl5bwmMqS2mY8MPqPHhC-rdcGxVs90bi58e7shhV3w6fszGxPT7YHKCPdqGxqmRgjLa_ULbIvVhmoJNSM0JK-oUyN0g2obkONks2k4mgP3taNMpVB9KL0pp64JtgAFJA4zJFUh9vHHdOKGog5FmSahYyDfW_d_lQi5fu2cmQruT6ESaR0f7pZck-O0wj4s3euxQm2EhUfQEPIZYmcXWzaK4wU3_cS05a_Dw-0AkQLM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c6d87c75.mp4?token=fhJESHPClAu_ZMt_8mD0wqDJnjhRpqHcS3XM7V10DJ6GHUvwtXtgWjYTBOwGpoXZG0BcfcCjhpkO3I31xKUiq3vii1aeZLT_7eDxDE4kM8HBKBaxVBmWaJbjxkUhQdNMqxo3Z3dmiYHu7zaMHwKeNs_Zn0KpAvYlPicuR-cG2MfodKxq2j5mUX__pXe_5KX-TmBtFYbTF9ynpBOVkKjMyMi7YWJglVFvzeHk2RAtrT-NUOYX9RjmGy68ImRG2u1y7P0DJkXC6cj3YhCXNNk5fQCCSsET1CfCfNRfRcUYUthWZfZSDtFwuEOpr5bum2GK-hpAjb1e7caWJeAWvPNlI34S9a15XyMlZ6vBvmmnIWug2-1hyn36nmFlrkDJrRY5P6TqI_oHkhgh-_Ea7GgIu5XG184P3gQaTa0P4dE0WV-aOv93hqlXFThCg6W6Gk5s3Fl5bwmMqS2mY8MPqPHhC-rdcGxVs90bi58e7shhV3w6fszGxPT7YHKCPdqGxqmRgjLa_ULbIvVhmoJNSM0JK-oUyN0g2obkONks2k4mgP3taNMpVB9KL0pp64JtgAFJA4zJFUh9vHHdOKGog5FmSahYyDfW_d_lQi5fu2cmQruT6ESaR0f7pZck-O0wj4s3euxQm2EhUfQEPIZYmcXWzaK4wU3_cS05a_Dw-0AkQLM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو : تا زمانی که نیاز باشه در لبنان
خواهیم بود. نبرد ما با جمهوری اسلامی
پایان نیافته.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5569" target="_blank">📅 22:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5568">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=iAOHd7dqAi358wRV7DctQIFjFhbzBYqlkh8lKJnTKAcncYvqfCKRaJFSQwrRcD4xJx4bHM35YFrKdlwzhbsDGCT2WABLkjg9c1OD1a_zJ2TXsIZwzXinyzW1oN41PjaKX8coMNXHtLej1uOGiJqq36TBN5JqdgCRH0bGoskumygbfPwUcgL8efxF0LOsMAVMpcnUkV-NLcbADO8nNdyGWMqImsSWrJqh33mNrj4b4DTK-VDYawJymsutn6hdrnWQF3YQf9k6vu_3jULwvhznXoqJZ5ak-s7fgdgbzcqpjSkK30g2x-QIwwt1ZbjVL5UKOrdg-Rj5EBkuIgfvXIeUtYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f3e1d072.mp4?token=iAOHd7dqAi358wRV7DctQIFjFhbzBYqlkh8lKJnTKAcncYvqfCKRaJFSQwrRcD4xJx4bHM35YFrKdlwzhbsDGCT2WABLkjg9c1OD1a_zJ2TXsIZwzXinyzW1oN41PjaKX8coMNXHtLej1uOGiJqq36TBN5JqdgCRH0bGoskumygbfPwUcgL8efxF0LOsMAVMpcnUkV-NLcbADO8nNdyGWMqImsSWrJqh33mNrj4b4DTK-VDYawJymsutn6hdrnWQF3YQf9k6vu_3jULwvhznXoqJZ5ak-s7fgdgbzcqpjSkK30g2x-QIwwt1ZbjVL5UKOrdg-Rj5EBkuIgfvXIeUtYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دیشب به ضاحیه :)</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/5568" target="_blank">📅 13:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5566">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGm55xGcRfkF2JpUi2sR_9Rk8umfMp6z4poz_hHKPY98UOFBIJFQFhrBYcUNSfpjUscskSNfKD3qCaGdh58Rxk44eOSbMGYy7VAKJVcZNLtxje1A2nEgUpXhG3S8v-6KCKbgLxvRFixBdmP-yaWR01AULahZnO0YWa0mHCThkf0N5y91IErtpIjf9wKYdpmfRZkZN8kt-HnIgp8cbop4vcUMKsmDWSmXPAKbrJ2uYoxMSsCygFRqmOooZRUCtKZ8qvZMnCJX5kDiHWsuKqZ6krAdQ719vjNiCbrv2EhOY2kc2vS6FkV4-dE79A4KXyYt9X1hCN5rlyIZVfBYQPEkiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kv-NzbVj_hM4bxrROw8Y7SkpqOpuPOZbRKev8L3ACojCvzhWS2HzBsvCX9QsF8gi8iOBKevDcdzm1aHe7HJ4ngM5L7Jdf6rUY758_C8eH80Wc-Of_WSN-LFh2z1HxJCCp9OPLrPHbl2tvzMognHGYi3NWRmRNGVr07b2KcSSMUokUb-hCzfEiyT8l50Wp8LnuYwBM9xAQVv98DZ3cCuWk70rZoAc3AQk5kWAYp8nHGLodDpwCPWbwhQruNYWG8QRH5_hAmNF5dJHE3gMskPVYiabSHMbm-KeakFJBudrfcGh8o-WPONEbePabILblvmxtvO6_bWIu1RZpYBEAyoiag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/5566" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5565">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzRkjxbI8u81ytW2mebZyNvieDnPXmGYBiPk2h2pT2udJL_oCYC-kO3zF7tF9tx75JY7L2MB_v0yObBci-4O1FM9LQ8yEjku-01XpZuCe1OUzshBmgyDAvsl0sy-3xBdike8QlUHb97JSMTS_d-_HilmM7cTaKPZmyWGESo46Nd6-_u0GZNUrwl8NsUxy7YMP078U3RSP_krCFeGEjo6iE4phyFHIFqRta54KoVkYq6gmX6K8duMVyp219SRdnkYQ2VD4ybuRGxAuMfiMQQxGe2_Dc6lCm0cwXEBv2a72n5ilCBK_ShIMVbB1k-IAH-nB2hmsSQ6dyz5Y6XKwXixaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم وضعیت لبنان</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/5565" target="_blank">📅 10:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5564">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ez_TYODJY4Wuc-YRCltepyPzBwm8Wr67-FVebWXs8mYRtoPFw2p1EBPtRymIrxPh0Qk4jxVKes223YpPWk7d703UIFTvnaccwiisk_tVMveIx1S-aVo4O2k7wUsGDWRKgkS5CS94MdOtLVr1iomsUEk83DLjkzRkDCss6y1p_aL9Bqn39vSAqN06vybNqlKnTB8MNTRag-Nx_BrkVp0oEMUVC1lY8Bj7kAeiktFset6A4fxRl_Qf3WNM69-u_nMbrPnNbnQ-cDdFYWwsNE0B_0aDcnvZ6J2iCdnF2t4xJY6t8yNYfkO9Mo4oSWR0zuKd7HmwXX_0ROFCS75OI4xRJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی کمیسیون  امنیت ملی
و سیاست خارجه  مجلس دقایقی پیش متنی از سخنان وزیر خارجه عمان را منتشر کرد که بر اساس اون، جمهوری اسلامی موافقت کرد که  «هرگز، هرگز مواد قابل استفاده برای ساخت بمب هسته‌ای را انباشت نکند». این تعهد جدید به معنای «انباشت صفر، ذخیره‌سازی صفر و راستی‌آزمایی کامل»
بود که سخت‌گیرانه‌تر
از توافق ۲۰۱۵ (برجام) ارزیابی شد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5564" target="_blank">📅 10:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5563">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رسانه‌های جمهوری اسلامی،  حتی بیانیه شورای عالی امنیت ملی،  تفاهم ۶۰ روزه (که هنوز هم امضا نشده  و ۴ روز دیگه احتمالا امضا بشه) رو  «توافق» «پایان جنگ» معرفی و القا می‌کنند.  در حالی که چنین نیست.  یک تفاهم نامه است برای یک دوره ۶۰ روزه که طرفین اقداماتی رو…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/5563" target="_blank">📅 10:37 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5562">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،  ۲ نکته رو به عنوان دستاورد مهم توافق پایان جنگ با آمریکا معرفی میکنه : ۱- پایان جنگ در لبنان ۲- پایان محاصره دریایی.  ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!  چون رسانه‌های غربی چنین موضوعی…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5562" target="_blank">📅 10:32 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5561">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MqpTRcPngxQdeTEOaD4GEMjDacWvwsjumO-oDKvtYd6F0IlXZqbqkCMRyMtTKN8ucEin722pEFsSxNMW6q0o-wFcRX-XOjrfeElUddhQ75uCvbN84drDRGhCPawVZm8R69yD4Fu4xwHpmQSV6H1FpApEZuZ4Obm9ff_u5hJIZxChRxFxw-drdkDhe6TK40v4hM0UH2u1X8qyCawX4r5qXYiX1d8CBrXzaUoAvriP8rQsZKpslOtbt9B6Zq2TXM36XhCXwzVulSAqODBcRs96cqYMhMJZrAOXXF9HXXLi13uduGliXdrApRLfba8fhmPlARBMmdYsRd3fvFQELvyDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه شورای عالی امنیت ملی ،
۲ نکته رو به عنوان دستاورد مهم
توافق پایان جنگ با آمریکا معرفی میکنه :
۱- پایان جنگ در لبنان
۲- پایان محاصره دریایی.
ولی موضوع پایان جنگ در لبنان (که در صدر شروط جمهوری اسلامی بود)  بسیار مبهمه!
چون رسانه‌های غربی چنین موضوعی رو
به این صراحت ننوشتن!!!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/5561" target="_blank">📅 10:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5560">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=TVt_IwmFg92Fm205hcv5QOtkqV097Uv-l86Qc3OmL-fcHRaHAIKXZY0Gm4hHt5s3yGyJf1xQBpD5dG3RImwUWWK2i9PsXL2ph2hCM8ooPTgcc5X_LNWFjeAa7RndBRFWpMQ8AEem_FnlziMPfU5FQ4-mfTuZebWnQmjZMbE02Uk841bTkcXJ2kBYSrhajKP_XumaI9WXJlF9dC56uAGGXJeNjDMONZdNzMUchU4ge6Br15K_kPXljE5xnD9W3qO5SAumjxVAIJWrj0z7aOkzUvkzeCxtBbWQNad1bh47FdptwC9aYDcu-TgEpBPDT3TdBQR_AdXBCrosPGcJ1J_vDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7e760113f.mp4?token=TVt_IwmFg92Fm205hcv5QOtkqV097Uv-l86Qc3OmL-fcHRaHAIKXZY0Gm4hHt5s3yGyJf1xQBpD5dG3RImwUWWK2i9PsXL2ph2hCM8ooPTgcc5X_LNWFjeAa7RndBRFWpMQ8AEem_FnlziMPfU5FQ4-mfTuZebWnQmjZMbE02Uk841bTkcXJ2kBYSrhajKP_XumaI9WXJlF9dC56uAGGXJeNjDMONZdNzMUchU4ge6Br15K_kPXljE5xnD9W3qO5SAumjxVAIJWrj0z7aOkzUvkzeCxtBbWQNad1bh47FdptwC9aYDcu-TgEpBPDT3TdBQR_AdXBCrosPGcJ1J_vDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام خبر امضای توافق جمهوری اسلامی  و آمریکا در صدا و سیما.
ظاهرا حمله برنامه ریزریزشده‌شون به اسرائیل هم لغو شد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5560" target="_blank">📅 01:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5559">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtdAA8WvQq0xvGfD6Xqxw5k4QGsw8GS0pE0cTSbayIXBzARcJ-4XVgp99-Xi5fqPCtiYF3qfiPEBU31cDROMDr4SuSaE1ZwXBdALnRKv6p1SbDRKRhA6fwGRY3ylcXbWyOBX0aIdbflYKTJpJigaABjmp4pZyat-iMUpOFlarU7Dliv3zFghKlGjUsohnwnUKjEmOV5_U0irdskEsyyzY_MS60wYf8xSKNWF1tyfhZikZUgaickC_f4KkwKFawE88BmZogE1AYh5SJoiilBOqjy-gZuf_omONp8NVdF0yjomLvSeuKi44NnDhuXg2kvlCz7_kaN0yF5tyBdM_0Bq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تهران ؛ ترمز امضای عجولانه توافق کشیده شده. سعید جلیلی جایی نرفته.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/5559" target="_blank">📅 00:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5558">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
همزمان با تشدید تهدیدهای لفظی سران جمهوری اسلامی، اسرائیل بر شدت حملاتش به جنوب لبنان افزود و موجی تازه از حملات را شروع کرد.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/5558" target="_blank">📅 23:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5557">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh6YOhNfHqA77eWZBcUhYxZ68D9kwRm3SKfepMLsihlqg1zE4DJCInfqLHSnlQxDoN5Zn9pbxEVNc-XSW4DFxehuWZ_gYiCS9Dwl0j0glGVdFZwgx6Rjh3V7_0CWIssWnQpKe-Mqt1RlCoQSAoXxtc4_uJcqU9zHWSqp2OEu_HYQn9l_ptEiCBS7JkET4rfy7wO1IRtvcnZsC6V09J-50jnH6HzvxovUouqkPeX43bTm0U-eL0IvX1S8xK0a6JTPnQ8Ovde5wrd83ubxZ-NYkphGKVPOO7XNpsjTCT2rPU5JFycOQLzk4r_q537b1417AB8qIa4uWIS6UNlrdDSQrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ولایتی مشاور بین‌الملل علی خامنه‌ای</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/5557" target="_blank">📅 23:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5556">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/5556" target="_blank">📅 23:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5555">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwVu6IphwehSJKsqiUyJ2amzCURXzBUiWFpcYFrywGjxHm3RyWM8LHbTFV7UIBUF44MpjiMkmao991sr4lxyRdpEOTfgftt3YcmJpOeK-GRqPnnw1DzuCNmC6hLqqJfSBpKNHvXLFi7B2ZOS34BCgBqX26ToGRK9qsTEEmGpwZFg3BBDmtDy1Hc0ufvGxB4_XJjhD8PspPCiHd99LzLPcHDjS1RXa-S1jip10gBLhUZaO9urZt_OrCYohdmA26ww7wn0mfUM4B3ULOMRYfsG4UYE5X5FnJxCvRKUdX2cux4oKtDR36pWHBmJzyI_1A6aeuFTN-chm7bpUck4HjBnuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف «تمامیت ارضی لبنان عزیز» !
«بساط جنگ افروزی اسرائیل
را برهم خواهیم زد!»
جمهوری اسلامی به خاطر حزب الله لبنان
دوباره میخواد وارد جنگ بشه!
آتش بس به دست آمده میان دولت لبنان
‌ اسرائیل رو رد کردند، به جنگ ادامه دادن
الان هم توافق نامه پایان جنگ با آمریکا رو کنار گذاشتن و میخوان برای حزب‌الله
وارد جنگ با اسرائیل بشن.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/5555" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5554">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
زخمی شدن دو سرباز اسرائیلی بر اثر حملات موشکی حزب الله</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5554" target="_blank">📅 22:48 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5553">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
لغو تمامی پروازهای غرب کشور!
آمادگی برای پرواز آبگرمکن‌ها
روی بیروت خیلی غیرت دارن</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5553" target="_blank">📅 22:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5552">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu51chrH7gaXsmG9ApnQYzG2PwkjfKoZaKwuqrFav-EQiqYVNc-mmN1P7GJ9UmVKGwxnVvJZ9taJ2HyzJSUj6n-t6q6Y1TTc3b5UNHMA6cvytlhOcpkkw6h6-gXz7qBfYLgtCOe6Fef678vqXwamediO3EOO2ChbV5EKGMlVzbsDu4s2QTzuZQa_xuYdZpe0X7O1n1OEFc2YJvnpEVOhg-_jwaLz1aeWMvGOQeIRsUUs2yrKQB1lLf9ipwRRbYXKfh5mxHTBmPdrRxu2fDNOw4N9x1HP9jG6cPQ9cqSLnfKxzA8viW4SaKe7jcszHIAiObqSQEajNYssK6hMF7LkAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر شورای عالی امنیت ملی
«لبنان جان ماست»
پاسخ رزمندگان اسلام در پیش است.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/5552" target="_blank">📅 21:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5550">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cr8Zn4BHdaxoTZazBUcf1glOiAGMfg2lAYegvQInnxm1SecTccNi-6c0bPVkSNZPqBMjz592U9hu8UdVZ8OGAU7M_SE2Avlru5myMKXO6jHyB0JlG2fL95T0_Uahm4BEIfymfuXDmZk1FAgutI7b3d6Iw5zljel5krsANNWamSysDJtGPjWjn7dtYos0j6kQRu7p5fHbzApmyyly3FEsH4BiTfPF7G0W4M2F7oDxqCvZ6Tg0g5rIUGmItfiTlyCMJHsY71_yZvpOm3L-CZIzDkwAaLyvGZKn7HLCiNWqIxE0P1CwY85d-vx40O4-RmVWQ0ArBFUn6Zj8uy0BotaILw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FGTAk4IP3UVW6WQITV6XvzcRFe7-3OCJ5PGOOlJD0eBx3tIZKpHmAU06DUnk-9fD2k8Tik5M3Rz3YWnjC8KH6QLDjQZq6Sk4gm0yXnY8tyKfytivq9M7M9jP0F2K83cxVeZTwxqBu99so1DJDhLo2Bi-f9KRCmVt605cjzOImWWe_ByPlYVO9DXurrCucHWdxFw16s1AC0VnOIzIoZHa0X6lsM0b2RlqMhWi0xfMqJSfmnUmNmXGB89BvDZrGTDxkM6VsBt0rNWuzrOrEOOozEH5g1XvqYMlzcLRrQuwJul69WabnOdSwj3ZNKOSd0o2aps0x8WFtEBhFT6ZSsvKDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ : نتانیاهو نباید دست به چنین حمله‌ای میزد!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5549" target="_blank">📅 20:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5548">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
ترامپ : به رغم تنش میان حزب الله و اسرائیل، تفاهم‌نامه با ج‌ا امروز امضا می‌شود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5548" target="_blank">📅 19:43 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5547">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHRt1AVzVHLy3cf8O8IDe-djPCHiuuAwZ9VSxSldT1mdAxonf-w5YmUZnnxiYhvNSd9icwm1TGTJAZTUJ8ViRIQjl7ROwDWKp-iyJajiID37q54scCCAG-PXkUiZTrN9k2xMFHSIZC95r_3HJkou1wEpvohw6Sr6fTGDsai2vFdsXAgEojb0gHGNN2oGrA4wPwzW2aPSg28M8NAPuQ2f8nkZ0OPdVMp5LvNQqO9YAXSmt2JrKrzXm7ey9tVdAke2IJVP2K7_0oHDhw1ycfunI1oy3v9MmNotlZ07lyI2-QfbLOzrQsERLAaaY1krOQ0IIlBOtfup_2o8wJb8oP_r1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5547" target="_blank">📅 19:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5546">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
حمله پهپادی حزب‌الله به اسرائیل</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5546" target="_blank">📅 18:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5545">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ : اسرائیل نباید به بیروت حمله می‌کرد، آنهم در روزی که ما با ج‌ا در حال امضای یک قرارداد مهم بودیم.
اسرائیل حق دفاع از خود را دارد اما حمله حزب‌الله به اسرائیل چندان جدی نبود، کسی هم کشته یا زخمی نشد، می‌شد بر روی آن چشم بست.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/5545" target="_blank">📅 18:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5544">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قالیباف پس از حمله اسرائیل به بیروت : ادامه مسیر توافق با آمریکا ممکن نیست.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/5544" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5543">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubBWdq5zBw9SkLQZOUnTZU-d9WzXw-6s73-wo1CAkgCBzyKVy2UO8zYN8wH5kVc279xZIHlvHqlNWWWkyqapPot_8YfBLmDEg6oq8dMSr_881behzb40Fy_MzwrWfVD5IQ5NxwsyxEYuR0BHV0fNblyzEC_YeKdh34EDgXXT81KREw2bDsHJL4uQ_QGHb6B9Fk9Gy-nAKGGq1fD8wh0d-Yn10agQzG3GSdkaPrsPe1ygT9Dzhizj5YH5SP_x-zSEntCqRVNGk0vVK2qfZPptDq6k5BFnF3xUuf3DOKwUSSH1kUZ3ij5bL-j5wWImes_6FctuC8EVSCuUdwDeMmt9LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل در حالت آماده‌باش کامل،
در پی افزایش تنش میان اسرائیل و حزب‌الله و تهدید جمهوری اسلامی، سخنگوی ارتش اسرائیل از اعلام آماده‌باش ارتش اسرائیل برای پاسخگویی با حملات احتمالی ج‌ا خبر داد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5543" target="_blank">📅 17:41 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5542">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=qDTnvfEomRLNnwuC8fU6u5e4S3HWbI7yP8qch1TIxiVx6ixM7u47Yn_jr7XFR_ql_fc4bxrKZI5HZk0wJcz83mH-P4gQE64vnKg_LzY5J939fcEiM3coVnF9VEnkNFTjgWwu2byF7i7rFMq1xi2NnWKpYiuv1XODH8NSjpM0O6V1FQ8LId4kEQKAhlyAKfvB8YsO58NBPhnbl-tjfWG6EdNHfM1SZFGKJCh58ptYumzWhyF2v21tMDHG_TABjNl5qDqkuXJbbnX9fbQHBSL6QgGSHiGgPcrKH4uioMYJ36zXoFeD2YTTiWI_TASIMRJ8zLId-B4KI6YciRGDtz357g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088d817c4f.mp4?token=qDTnvfEomRLNnwuC8fU6u5e4S3HWbI7yP8qch1TIxiVx6ixM7u47Yn_jr7XFR_ql_fc4bxrKZI5HZk0wJcz83mH-P4gQE64vnKg_LzY5J939fcEiM3coVnF9VEnkNFTjgWwu2byF7i7rFMq1xi2NnWKpYiuv1XODH8NSjpM0O6V1FQ8LId4kEQKAhlyAKfvB8YsO58NBPhnbl-tjfWG6EdNHfM1SZFGKJCh58ptYumzWhyF2v21tMDHG_TABjNl5qDqkuXJbbnX9fbQHBSL6QgGSHiGgPcrKH4uioMYJ36zXoFeD2YTTiWI_TASIMRJ8zLId-B4KI6YciRGDtz357g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بدونید که هیئت پاکستانی
هر بار که میان تهران، برای مذاکره نمیان،
میان تهدید کنن!  که رهبر و فرماندهان
شما رو بمباران می‌کنیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5542" target="_blank">📅 17:34 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5541">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=O8G0uQeFiHhsnB9HiakFygf2U8ABYoo-R9Z3L5fEROsht8anWrdXjiQRnEO9x8n81FzNiqCy3VOGju172YIl1zxwEjrAQH-B_HiW0NBJbhjlIIUS1-b5Cuxk85fzhcT0REKeoOVcHH1g7d5se8HQ6OHPeOaNpVhGum_Fsddw6c9ZdhcutiyoLTxFZyhzrAGpwksi_zVBVGNtmNi6LcGfusUQ-79DXiWaQDgn0VNQG5G8dybTz46vnRFOGfLmwj9OdyLM0qLE4e6pkFGh-5FtK2Kpkau1Di8LKmgXARGqxu1Nm9GxysBnFRR7abR4FMQXpIlL8sjFHnr7Mixa3pSeYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45ffc6366f.mp4?token=O8G0uQeFiHhsnB9HiakFygf2U8ABYoo-R9Z3L5fEROsht8anWrdXjiQRnEO9x8n81FzNiqCy3VOGju172YIl1zxwEjrAQH-B_HiW0NBJbhjlIIUS1-b5Cuxk85fzhcT0REKeoOVcHH1g7d5se8HQ6OHPeOaNpVhGum_Fsddw6c9ZdhcutiyoLTxFZyhzrAGpwksi_zVBVGNtmNi6LcGfusUQ-79DXiWaQDgn0VNQG5G8dybTz46vnRFOGfLmwj9OdyLM0qLE4e6pkFGh-5FtK2Kpkau1Di8LKmgXARGqxu1Nm9GxysBnFRR7abR4FMQXpIlL8sjFHnr7Mixa3pSeYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسانه‌های وابسته به جمهوری اسلامی :
خبر حذف دبیرکل حزب الله
در حمله امروز اسرائیل به منطقه شیعه نشین ضاحیه بیروت درست نیست.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5541" target="_blank">📅 17:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5540">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=gun6Z3si4w4qsXuSTbjx5zG7JCXINezuNiPznWTvK63ySBm3ciQGWAL4wj_ecp60-ay9DoRBoHh7d4k46ok2t8fYO94-MszcunS-K48sXMlILp42vuCvwUq2eMhbE4uu0G7v3Mid5XsWknI3z56gCaUoCe9IwyVyTVAx-odu7dUbInRqNK8rmeCEqyUl5Sc-_0orEIHqy41Utw8Nym4eS1yMVkUhk_ZctapwCaOiJQWWgBTqP5KUUBulQo0yan1DQ21JfYTJXzSrA_QyLfKqmdENmRS01qEJIsxNly3q75oj-hVieWT6JsM55sijgnR-DdwXZs8dPH5-eg9Xwyy0Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63093fbf2.mp4?token=gun6Z3si4w4qsXuSTbjx5zG7JCXINezuNiPznWTvK63ySBm3ciQGWAL4wj_ecp60-ay9DoRBoHh7d4k46ok2t8fYO94-MszcunS-K48sXMlILp42vuCvwUq2eMhbE4uu0G7v3Mid5XsWknI3z56gCaUoCe9IwyVyTVAx-odu7dUbInRqNK8rmeCEqyUl5Sc-_0orEIHqy41Utw8Nym4eS1yMVkUhk_ZctapwCaOiJQWWgBTqP5KUUBulQo0yan1DQ21JfYTJXzSrA_QyLfKqmdENmRS01qEJIsxNly3q75oj-hVieWT6JsM55sijgnR-DdwXZs8dPH5-eg9Xwyy0Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله اسرائیل به ضاحیه بیروت
حمله اسرائیل پس از حمله حزب الله
با دو پهپاد به اسرائیل صورت گرفت.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5540" target="_blank">📅 17:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5539">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=lBzLSAIK8FgcRoz33jsnwMslquxNFS4-5vScm-iPLx_0-HXOJN82m_SenBjHVjc9x9T1bch8Qo-ksSPGWB29t9g3SMmjrPGsBTTgx6d1Rh3UYH69mxSmDXNduUD5XVXcWLOUz7BQh74KfP8drNWkd4XrlRS5NgDw3mFJBMVDLXN_miGq8Wuk5iO64fuSnVLTiM0YXy4cu2Sg62cjpzWGxEJO5jp7uBwYPzYkZiH5iZ53sfx1BiNTaPb0Af47DXs9rgksX_ypeMPCBcBNs93dgAhpogLNZjyybRUcpF0zpPj7GINY4vs2iVxiTZu8CUmLWISYCXiq2NYeYCmxZ4uR8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d41455ed.mp4?token=lBzLSAIK8FgcRoz33jsnwMslquxNFS4-5vScm-iPLx_0-HXOJN82m_SenBjHVjc9x9T1bch8Qo-ksSPGWB29t9g3SMmjrPGsBTTgx6d1Rh3UYH69mxSmDXNduUD5XVXcWLOUz7BQh74KfP8drNWkd4XrlRS5NgDw3mFJBMVDLXN_miGq8Wuk5iO64fuSnVLTiM0YXy4cu2Sg62cjpzWGxEJO5jp7uBwYPzYkZiH5iZ53sfx1BiNTaPb0Af47DXs9rgksX_ypeMPCBcBNs93dgAhpogLNZjyybRUcpF0zpPj7GINY4vs2iVxiTZu8CUmLWISYCXiq2NYeYCmxZ4uR8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان : رسول خدا و اصحابش
لت و پار شدن. :)</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/5539" target="_blank">📅 11:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5538">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
حملات موشکی حزب الله به شمال اسرائیل</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/5538" target="_blank">📅 00:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5537">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=he5derCo92gu4DD_zyF_J97Cl2T_BHtpykPLKYOJfJBalM2Tg5KSFZMJqVIhiuwGuwto_s7MYOgPpnXxjTtJU6y6mo_P5LDUYkUtZ5-zXJ9GPL0pROsHFCrOXFbqh1FlCUzjtV7PzwNjxxyT0OvXnvYciMso9Q0MVEyeCITR9GXs4faBLqR4bYO31YLgeTLm5aFrRBsvm2EzYb_3lPRmDxBBxKOKBW4DBHQ8Ai8S4bxDXj4ETd9X1pmaFXjRt9yeIRjW1rTdnN6CejivJMy8C8UxOBOJI947D3At_9zd2Hg0cSFIavGsTuE2_wpyHlsAo_7y-o_irgw_RNc09aAXPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef094183e.mp4?token=he5derCo92gu4DD_zyF_J97Cl2T_BHtpykPLKYOJfJBalM2Tg5KSFZMJqVIhiuwGuwto_s7MYOgPpnXxjTtJU6y6mo_P5LDUYkUtZ5-zXJ9GPL0pROsHFCrOXFbqh1FlCUzjtV7PzwNjxxyT0OvXnvYciMso9Q0MVEyeCITR9GXs4faBLqR4bYO31YLgeTLm5aFrRBsvm2EzYb_3lPRmDxBBxKOKBW4DBHQ8Ai8S4bxDXj4ETd9X1pmaFXjRt9yeIRjW1rTdnN6CejivJMy8C8UxOBOJI947D3At_9zd2Hg0cSFIavGsTuE2_wpyHlsAo_7y-o_irgw_RNc09aAXPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زنان کفن‌پوش ولایی در برابر وزارت خارجه و سر دادن شعار : مرگ بر عراقچی بی‌شرف نفوذی</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/5537" target="_blank">📅 22:58 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-5536">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8679568b89.mp4?token=FKpTYPfylYcMB0n3JLdgJD6HEuytkMPNIsDvUNKs4d-nWY6EgkJiMClanR8_nZaqaNrwSVvFscIA2jsgF0IGf4d8PfJ1djwQkyzsIfqutQ2ZoaeTt2IsZbiVjhNCP5BLiDAdKnW8vMJE_JEJ4fMXPx8bUsOnEquttOvLMefs8G2xSsx2Bb11t77vwVe7JSBE2CAIntFtU8BjajzmSUcu77SCorJOnWUBhNkbbjtI_iFUtscLlSmPZyCAp7V3v6OuzjxuTGfbsvgMotPv-J6vUH8PyuLvCdS3WZ6CUGMAYshYByhyEHUqiO7vQ1ZfeYBnPY5TtK8jazCrYYUIt0grVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8679568b89.mp4?token=FKpTYPfylYcMB0n3JLdgJD6HEuytkMPNIsDvUNKs4d-nWY6EgkJiMClanR8_nZaqaNrwSVvFscIA2jsgF0IGf4d8PfJ1djwQkyzsIfqutQ2ZoaeTt2IsZbiVjhNCP5BLiDAdKnW8vMJE_JEJ4fMXPx8bUsOnEquttOvLMefs8G2xSsx2Bb11t77vwVe7JSBE2CAIntFtU8BjajzmSUcu77SCorJOnWUBhNkbbjtI_iFUtscLlSmPZyCAp7V3v6OuzjxuTGfbsvgMotPv-J6vUH8PyuLvCdS3WZ6CUGMAYshYByhyEHUqiO7vQ1ZfeYBnPY5TtK8jazCrYYUIt0grVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVaVtZS4p0aPHmBSwrdaHYN5e1xC_vUnIyxKugQ7Fg0nvS_8NWwvAM5845SbZ1X1YYEfMOtZzNIefq9B9M-VCw_PsfsC6MQmj1iUkGBCTMuXgm7L0Ty3kQT4-MEezAkEIuUqIlKWiBxgFNQG31YGZGUkhz3KDK1niwxgINwu7ytiiM8HQqCoIWLMD69LQDmTyW3tHOHgXiNnnvKJ9zGJH_TyRHuqA6h7-nujQKfY02i9K5olwxUtBRUqTKxxl1tYNftiwEIVELeV2pm79HQ1hfeEPbUWNdP5e6xbIPoiOsnjG93feqTHmOl3RIOXO1NDzXD2Z90IE2v4SeQAFe3IPaP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8066c06.mp4?token=VRBqP1E0gokN_Dz6vcM7FMp1ExWfjm9AFCCh4SsgWbGnNZvAd3mcvRptajQP5ZAI523ErHXwfY6VMDc5iIQIHHKAfmd06AcbQ-8mgWzk7GvQlXeFmDhY5A_uvMD1zeZs1DYOwGVt62JeM9lmlrwQhdMP6Vaye_gNLbKVYc4TUrXduhVeWNGaEQE0NBlvoNMSxPnFESqiK6pfQStifT33wv0o3Y3ecpQ5BT8hPxjjgBBJ_HEkGaDRP7JK7qo0-2IDcjBGzd3KBnmdarC9485uT0UUPdlBEqBv5j5QcLWTQqqL8dpNeL1K3JNOS9s2na1x9YaKoPZW3MeJzDs4js9IVaVtZS4p0aPHmBSwrdaHYN5e1xC_vUnIyxKugQ7Fg0nvS_8NWwvAM5845SbZ1X1YYEfMOtZzNIefq9B9M-VCw_PsfsC6MQmj1iUkGBCTMuXgm7L0Ty3kQT4-MEezAkEIuUqIlKWiBxgFNQG31YGZGUkhz3KDK1niwxgINwu7ytiiM8HQqCoIWLMD69LQDmTyW3tHOHgXiNnnvKJ9zGJH_TyRHuqA6h7-nujQKfY02i9K5olwxUtBRUqTKxxl1tYNftiwEIVELeV2pm79HQ1hfeEPbUWNdP5e6xbIPoiOsnjG93feqTHmOl3RIOXO1NDzXD2Z90IE2v4SeQAFe3IPaP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توضیحات نبویان در خصوص وضعیت تنگه هرمز در تفاهم‌نامه
- به محض امضای تفاهم نامه، تنگه باید فورا باز شود، بدون حاکمیت ج‌ا، گرفتن دوباره تنگه و اعمال حاکمیت بر آن تقریبا غیرممکن می‌شود.
- هر بار که متن تفاهم عوض شد ج‌ا عقب‌نشینی کرد</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5535" target="_blank">📅 21:27 · 23 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
