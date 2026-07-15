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
<img src="https://cdn4.telesco.pe/file/lFrN6vs2N8L2eKLbjCUVHztZ18qDw2l2LF2EwNurIJ63TcJWTpSmsyrcGSvydeVDd6FSZtgNUanLezaRCf_lvjRHViJDeMxQAyNXaU-Z6EQhV-WNqrBdosWID43fd533KHYGjtWghF5iMQRZYkryFgZ5BX9cu20WWdkf_J_zO111LXUvGYcnA_EuYYTzR7mZFxpaH_PtNTUpOsDTM99pBJsqOkgZFI9AgLpZrn05x8NFVwiYIsvsFWUXXwZMt7H8zKRJeyTI1Qa3wMrB7bCQmHq5YHb7Rwix7Lt20IVKmJbtfrzJgmVaOSAs4dzBr0gIggHc1qpg0_YdKbl9-vvH1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.39M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 10:05:15</div>
<hr>

<div class="tg-post" id="msg-671288">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa6c6c7f0.mp4?token=Ee-iXpa7pDcH9wNbYaJDaiQzW8h8cXBeoTKOI3tz91-sdEkFgS_xagI_Zi0mLvywWIuIecn5SAnCCSGn0Jklz4e1gjfTm414w2oBVjq6zmYCYOZ2dzjsYKSmyKaWZpmy3_fVef_A0RgzA3JjIGKsQKAbBss3tyHiaLqsbyiDhzh45MCIQK8IKDuOHM40MDiWVbY4WchwO0_R7e_7EXE62v8YHGdhjSUV7_BitUqs4SW5kMSQ5z9D5iq9DUT-dEHwXaMlUhm6PTnQiplo-BzHu80VEX6H4dOOrY39lw0yuXqKJ7m_TKXHJTr0Inpj_xulE7N9rsSM7Wyo6SrUYdCmug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa6c6c7f0.mp4?token=Ee-iXpa7pDcH9wNbYaJDaiQzW8h8cXBeoTKOI3tz91-sdEkFgS_xagI_Zi0mLvywWIuIecn5SAnCCSGn0Jklz4e1gjfTm414w2oBVjq6zmYCYOZ2dzjsYKSmyKaWZpmy3_fVef_A0RgzA3JjIGKsQKAbBss3tyHiaLqsbyiDhzh45MCIQK8IKDuOHM40MDiWVbY4WchwO0_R7e_7EXE62v8YHGdhjSUV7_BitUqs4SW5kMSQ5z9D5iq9DUT-dEHwXaMlUhm6PTnQiplo-BzHu80VEX6H4dOOrY39lw0yuXqKJ7m_TKXHJTr0Inpj_xulE7N9rsSM7Wyo6SrUYdCmug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۹ مدل ساندویچ فوری و پرطرفدار برای روزهایی که زمان آشپزی نداری
🌭
#آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/akhbarefori/671288" target="_blank">📅 10:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671286">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
شارژ کالابرگ کدهای ملی ۷، ۸ و ۹ از فردا
🔹
تمامی سرپرستان خانوار، از فردا می‌توانند با مراجعه به فروشگاه‌های طرف قرارداد، از اعتبار کالابرگ تیرماه خود استفاده کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/671286" target="_blank">📅 09:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671285">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kUSedW-mGh__iz0B2FzcQrq6kO3qXdaD6btZ4vViOWvUsKRsERMhSYEy0ZOKWy24qaGCbZcA8CO36C9bh83Eo4veeIIpRBavbGdUclD530FPELI9ueVI37H8sHni-7HPWqW_G_afKVuVLz3yNW-27DyKmwvuQ1amuclbsH6Vzg-P-EHrSNjhMe0ezSYISpztn92gwYHzQlkjZSu2HdfZm94HHKKaRXSy1O_SlF7FA8vFyU4s_SB3qfAs4zM08UNPGvSgJmgoCL1Q0YQloOiF9A9oJGGZuAb8H6JcUedawmt721mWo2vfSqngfIeL3EFJOTN3NbrjmobS8I2Way5Kig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکس روز ناسا از شبح‌های سرخ‌رنگ در آسمان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/671285" target="_blank">📅 09:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671284">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FaauKcP3_KMlbKlSIHSrYIWMqGV4aKCFsFmipZp00lcx0uym9n6NXyMatTVS6b62Zkao7PuC9WGrR8TUqV-ipGcfmzeQQfBSD0jUbFG6eV7t2TC_kfcKkBq2DG18vsEIelunD8mg__36skO_-1Tpz9TTRIbos5DzukqWRtruFWZjD9cY2EPvEZqsOD3E0vNjfRXrM_oSeKxR3u97Qm6nWxINqdGcKz2YMThQoOei7ToePX8Dae3RdEnDOBmy8pExi4PTKX-YrzNF1o6pElJ1Q4XbMrVvW0RM6FDHBZPyXRYD_-k64O1u_cFA4cIgaZG2e6z5xnuE08TYBYV8D9y1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آپدیت جدید تلگرام با قابلیت Community و ویرایشگر پیشرفته متن منتشر شد
🔹
اولین ویژگی بزرگ، ویرایشگر متن پیشرفته (Rich Text Editor) برای کاربران پریمیوم است که اجازه نگارش مقالات طولانی تا بیش از ۳۲ هزار کاراکتر را همراه با جدول، لیست، نمودار و ابزارهای هوش مصنوعی می‌دهد. قابلیت دوم «جامعه» (Community) نام دارد که به کاربران اجازه می‌دهد چندین گروه، کانال و ربات مرتبط را در یک بخش واحد کنار هم قرار دهند و مدیریت بهتری روی دسترسی اعضا داشته باشند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/671284" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671283">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPJfXxatoDDYAVQfknJltvnWeBs7DVfu9sa2aqhXFu5hVPyHBQ0J-tF-7l3W34qJZUlldbaBK4nfaozFA2hLtRKbMnLTLbZV2i8ICcgmKHdcb_pN_A1OvHnzoKVqdnUyw1UHwObSCO29JbkEhYB0-rEC9VJ7MyLH_uKCE-9WTJ96ygMbJQsKfIRElV0cZXQiMBGY_n-JOXBzru9-zNZaIVuSZZD5Bw3ghoYHjOG4Idyh_RRrdD8jD5YheXGis9UNLPv64-BgrSfFXnTyLtqA0kW7UnZz1i9KZ3qENAGwZi9rio3zQbH_HE3N_NrLcONyh4x1WXG3o4hwJBkjpdbuGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از کنار
این علائم ساده رد نشو!
🔹
بعضی از بیماری‌ها سال‌ها بدون اینکه متوجه بشیم، آروم‌آروم به بدن آسیب می‌زنند. اگر این نشانه‌ها رو به صورت مداوم تجربه می‌کنید، بهتره برای بررسی بیشتر به پزشک مراجعه کنید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/671283" target="_blank">📅 09:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671282">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
دقایقی پیش اهالی چابهار و کنارک از شنیده شدن ۶ انفجار شدید در این مناطق خبر دادند
🔹
هنوز محل این انفجارها مشخص نیست و نیروهای امنیتی در حال بررسی این موضوع هستند./ تسنیم  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/671282" target="_blank">📅 09:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671281">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYci3H_kAfiIIFabk-Yuq_90K3_YkzfO-x_G0Z7xwgWe-1wvJv1ZqKxdFhaHC1l_cWS2PrXf6EOmrSYvN4m5Xsim38sw97O3yfDMmZ0-YE0CVbXqSEipnHFke96FoAIkFfGtWC-GJTjo1wLOv0XjLAiQjolrXb2z9wMiNG_haW_OMpZ8j2jxThVQ-fVVwtE7LjMIQVnJOEm0ybJPeDRm1tTx9BKdVpgVVH19z0FDgK9olcW2mNtjvugwGPyf5-_k06tX0rRnNBvvQlKT7LOkkmcqg6AhFLYVw1qqXVmJOXk2MaH03m5VVRas26CDZYehG1LXj5eE1PIXZQGjXHhprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با اعلام فدراسیون فوتبال فرانسه، زیدان رسما سرمربی تیم ملی این کشور شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/671281" target="_blank">📅 09:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671280">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842ffd17fd.mp4?token=qXOx2k1LDrg83uEGY59QtnYNQ_FlYdOitQk8eV45AYXPYDK9lvJqUCxCaZXn3wQ5Oxm0z5sPCTTDjHPJhxktbJOomSFNqhZ_yRyLu65JJrcx0H5UV-OaseZ6hGof9c93Kg23ixu3eo3dHj_PVKu3dyiGiP3FuaSbYmOru28HaffW504fSnW-bMwLn-PmsXishmIkGBKnttMNuz2X_GupxQuU86YCpfTCFbuBqGYrHJeQfHy1_KTJR9mpWKeLBmtz-iOZSTNJvnFoSQ53tz69bgABrzSfO4Mtp74qBGfWPuqBxCoGCxpa2JZssvjwOXC4xhqEKDyBBmauWISjQtaWKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842ffd17fd.mp4?token=qXOx2k1LDrg83uEGY59QtnYNQ_FlYdOitQk8eV45AYXPYDK9lvJqUCxCaZXn3wQ5Oxm0z5sPCTTDjHPJhxktbJOomSFNqhZ_yRyLu65JJrcx0H5UV-OaseZ6hGof9c93Kg23ixu3eo3dHj_PVKu3dyiGiP3FuaSbYmOru28HaffW504fSnW-bMwLn-PmsXishmIkGBKnttMNuz2X_GupxQuU86YCpfTCFbuBqGYrHJeQfHy1_KTJR9mpWKeLBmtz-iOZSTNJvnFoSQ53tz69bgABrzSfO4Mtp74qBGfWPuqBxCoGCxpa2JZssvjwOXC4xhqEKDyBBmauWISjQtaWKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اهتزاز پرچم فلسطین در جشن صعود اسپانیا به فینال جام جهانی
🔹
هواداران تیم ملی اسپانیا پس از پیروزی برابر فرانسه و صعود به فینال جام جهانی، در جریان جشن‌های خیابانی پرچم فلسطین را به اهتزاز درآوردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/671280" target="_blank">📅 09:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
الوفاق بحرین: علمای شیعه در بازداشتگاه‌های محرمانه هدف شکنجه قرار گرفته‌اند.
🔹
رئیس فدراسیون ووشو: پرونده خواهران منصوریان در حال پیگیری است.
🔹
تسنیم: ورزشگاه آزادی تا دی ماه در دسترس نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/671279" target="_blank">📅 09:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
مرشایمر: جنگ با ایران وارد مرحله «اقدام در برابر اقدام» شده است
استاد روابط بین‌الملل دانشگاه شیکاگو:
🔹
اگر از نردبان تشدید تنش بالاتر برویم، به نظر من این ایران است که دست بالا را خواهد داشت، نه ما. این فقط یکی از دلایلی بود که باعث شد پس از چهل روز، جنگ هوایی را متوقف کنیم.
🔹
تا این لحظه باید برای حامیان بازگشت به جنگ کاملا روشن شده باشد که ایران توان تحمل حجم عظیمی از فشار را دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/671278" target="_blank">📅 08:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671276">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTXx3qyxlWjEmCdjoF3kSKV-PUTdeYagk1k8zTps7fL8iUjcl6AsUXcgfUj7fMja5vdqvOmN-SKsACEEM9_T5052I1j_QkWYBpRKivrR53IP6yEwEcy6e6d_kBZeyaCb-V3j7VG9YuXyqCfUJwphMiXemL9nhZMFQAU_Auh9MCaVX6QAQRq6yJaKkhO2x45Tebu9c3sHtkMgNTzkeSKZk8WtXYlJpkm5Ar-C4dCkQWmTFsbV1DBWaapWENstGlPVXZYRC-sYTtQsCnzKMtelpCGJPE-Rht0rGhvYIsPV3uNfFIzxehRFt1D_IeHHAHUWohs-4vmEy2eRs-vFrO_LRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7yB9p9JtobnG2ejJok25YCduXXCEHXI5HDHBLmaVbwnGujpzhMP2wc9iJhsZrgV33tPOtdIZZlD4Se4fRBKWz17GHUVcUaYxyDm9yrvzifXwSoSpE2oTJzFXOJF-DuAkbFZITiF3eSjq_HsFf0mV8mTlxPWSsoYE701mzXWIKDd8bz4sueRl0TDekutp56JtQIM7rL-Z7gqlLtFkAcJd_SyAV23YLJU1xrng_vfd8FAnO2BHxWAKWLuBwILAxLCk8iKtIJGnUAvMYf5sYCn-m-E2J-VcSl1IClF18ZBQssKQlTOtEHT7rcmS5t1pyc-0XSz0oTAAochitU4FF2ARQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویر ماهواره‌ای از یک انبار متعلق به شرکت «کویت و گلف لینک هلدینگ» (KGL) در منطقه «مینا عبدالله» که مورد هدف قرار گرفته و به طور کامل تخریب شده است
🔹
این انبار، مرکز اصلی لجستیک و پشتیبانی ارتش ایالات متحده در غرب آسیا بوده.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/671276" target="_blank">📅 08:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671275">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdRRZioz8kbLGgqJMhdYm1VcFkiI5FbKFMlPwjDXsE6b4bI967PKEey-pkMUM10KSOAnL-d2FYxv4RupI5_s9FTQ7AEPiw2__pVC--4Hu70vwHlpx0YOa5moaxSGrdASQKnaJiatnkN6Qv_ALVPoeYWWVLzB37dw9OtHXx5omtLeDpxo4DcIOSW03Z8uKPfAY5bYWzvuT4h17nwdy_chSBj4sH8gDlq9ayrP8M7AiVHe9KcBAuKt3zdcxiVHSwrVTROQj79Cff14aW3z3aW03fV1vbhZpjlDZaCFrlQcXsS59AGJy9iBOLFtpiykCQsU_Z5RvokQAsfaqe0D47cW_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه‌های ساختمان با کیه؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/671275" target="_blank">📅 08:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671274">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnAUA80HK_srgNEm42YuJ-iOoULwQnaMN82zoHyUTzgy2LinojKH1uEpo8Y2z70tuBFfAz8QSmbErJTB3SDiQ83tPjG5p5FFsyRxOTJaglk_Vzo-CIqOUQArVAHpm0mvoWe4ncJClVsGw8SnZ1TLGqg7ACU0C0J-NONZJsVtDNweKJSds9msW9uf7QGLZ6Cxphsf8rFNmaqHXQ2aRfMVk4Xe2U4GDusFOtK0JY4TUaJtb9cOM7ZXI84HIcWyLjqb95SKds42m1hWTbZDb19DvjWH3FU-lygHLtTKsz1qNz2N-2BEZR0SPrXCVFfQlP4NfqSguuKUDJ_1WRcGOPYarQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان روز اول نیمه نهایی
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/671274" target="_blank">📅 08:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671272">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ایندیپندنت: ترامپ ۳۲ بار اعلام پیروزی کرده، اما امکان پیروزی ندارد
.
🔹
شورای شهر تهران: نگهداری آثار ارزشمند موزه‌های تهران در مخازن امن/ بازگرداندن آثار زمان اعلام رسمی پایان جنگ
🔹
سازمان سنجش: فردا؛ آغاز آزمون ارشد/ تاکنون ۴۸۰ هزار نفر کارت گرفتند.
🔹
حمله رژیم صهیونیستی به مرکز نوار غزه چهار شهید برجای گذاشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/671272" target="_blank">📅 08:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671271">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dad1458dc.mp4?token=UkyHCSYD_MFgRqd5T6yAVv-I0VkG90SUPcpBBOFP8HI7YwR1pxDJxozoePqxJy_E07BgA8RIqT8iFA7aIWGwB648avV18svbhfI6y69hHkvgtBavvJiDffgswazdWj-MbUE5ANsAD1Hx4YURI8u00M4oORy9siepcEx4_F7x7QG74rAEsCYEBFS6pGVEIM2wp95vsMKYaARhYwNL0yrH5DF73noPPk6xyn8Cj2XW2DUEnHjNp7CsVkbEWUNprHS4aCeqWKYLDAiPIZeImupfSjJsHgdigfEyDVcSDZzerU9JrpD-2Rpa1A2ipmgTbkvlzlqQ4hMl0k9KMoeoypnmfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dad1458dc.mp4?token=UkyHCSYD_MFgRqd5T6yAVv-I0VkG90SUPcpBBOFP8HI7YwR1pxDJxozoePqxJy_E07BgA8RIqT8iFA7aIWGwB648avV18svbhfI6y69hHkvgtBavvJiDffgswazdWj-MbUE5ANsAD1Hx4YURI8u00M4oORy9siepcEx4_F7x7QG74rAEsCYEBFS6pGVEIM2wp95vsMKYaARhYwNL0yrH5DF73noPPk6xyn8Cj2XW2DUEnHjNp7CsVkbEWUNprHS4aCeqWKYLDAiPIZeImupfSjJsHgdigfEyDVcSDZzerU9JrpD-2Rpa1A2ipmgTbkvlzlqQ4hMl0k9KMoeoypnmfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگه قدرت و استقامت پاهات کمه این تمرین هارو انجام بده #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/671271" target="_blank">📅 08:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671270">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRokcArFZmfgZa9AMHRrb7zEL47_HH8fBsKIe1jEh2J0mckaisipCJ7go_fjdLluoETtdUnah-8RzkPr-v1a4SCvq3mn7__PiYtIbyYpT0_brKOZlbL_eaxi-qVBO0BwwCSq6fU4k6i6AmERpgNhcQTV6GTfE0l6rDoGWDOeWEK5L6xTHpB7-st2KULMZ9SAxvid7-cfEZRWEz68Wbn7CvGAwlYSyG2m4t1zE3f7fwGhMjSLsynpxaudzUtyS595wpGdENiaqPEijsh9mkrWp-fzFqIivpCGjaiYqPYIqwlmW1V4WVTuTcCIMX_qPRheaTqmTZ72zcc1XVc3i1bLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس پنتاگون برای عراق شرط و شروط گذاشت: یا ایران یا آمریکا!
🔹
وزیر جنگ آمریکا همکاری‌های تجاری و دفاعی آتی با عراق را منوط به تثبیت حاکمیت این کشور و خلع سلاح گروههای مقاومت تحت حمایت ایران دانست و از بغداد خواست میان این گروه‌ها و گسترش روابط با واشنگتن، یکی را انتخاب کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/671270" target="_blank">📅 07:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671269">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Is-uB0zPWtgWs8UvtDR7nb-PXQJ1FrsJPiKh045zdkScriJS_PGGG1Rj-tENg5fstcY2O19kdY-4I2A1PSJ51VOnHeYnhC8FMDRrLxDkczcn1XNhGr-ZSgIBMmBR3d97X9Gn3WCoSLSdC15MPSOO4Y1HAFMA29WuLgYwBp9sXBeVv70tIknAWCqYZJTZWTABJotBaePaq0QSyUuY343__E1H3QwX85-xXfL1ivOEppII3zbbx2OXYZAyeGg-epKGvlMNgCiLQotexIchQ_zUrGUFbP7_y8iCaQpfZ-zU4W76tpNE91amU1C4FlGa6f17NImYA1gvDY6NjlT5L-xWIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لامین یامال در هر رقابتی که با کیلیان امباپه روبرو شده، او را شکست داده است
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/671269" target="_blank">📅 07:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671268">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIk2yi0HbRRLDdKGCgXYXv8Kv1EfyDAufiZjsarFQoIEcTq8HSIbFBxdMYT2GckSFVcF-205K15WJLp14Nw2E5fB4TqfdHl22ROcNkwkYVjahtPeoyVelyYTgmfC7sim15VkJ4QFNkJKq8SkGD5E8m1ve6_4uRS0CYtE2A2TT7oJON7Aiz3YybKC1qwXUZFs626CgT_YCZ-a2jCjBOQPznNXHLHiLT1B_NW7tA7AwDFX-jv3UnM5dmwcDTBu-AtibdfeUEVfUsqNlZk1dbx6Ng3ZyEUxf0MJ0XGVGdyrb97CP1Qk5Qo-yC2Nkz9QWrS-eOzkDZgYgfnJ_WnfnIAMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار افزایش تابش فرابنفش در روزهای گرم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/671268" target="_blank">📅 07:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671267">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست‌ کافئین| فصل‌دو،قسمت‌هفت</div>
  <div class="tg-doc-extra">زکریا رازی</div>
</div>
<a href="https://t.me/akhbarefori/671267" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
🔹
محمد بن زکریای رازی
🔹
در این قسمت، بزرگترین کلاس درس تاریخ را برای «فرار از تله‌ی تقلید در بازار» و پرداختِ «هزینه‌ی متفاوت اندیشیدن در سیستم‌های سنتی» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/671267" target="_blank">📅 07:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671266">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ec242e86.mp4?token=h3ab3FIo65bDKFtIG-fFcWOmpZWUpzhNKxhCn1DzUC7cpJlHkSVwA-dOdWT3hICFivBetNaZUv_HMnINAp0pl8FhTUIeREuSSLW0yi1NqWmNMaumPsfiQNL1pCzX-noL2kUZuJ6qHqCo1iXsiloQnz-8DJzziVxhO7HoKhlujuUQJ3MZM7xsxuo2k_X5rKqPugW_4M-aKg1aJnN5eUlGvZFMpQ8foLUbjVpm5d2LZpEAceHOrgeiBmRjSLmR-Vpg3tvZ--gRNHK0vwDqm2v94I82URs-jvAXnHMzUqe4RCH8LjnTcPYjXp9Fo_QiRwcEc3YnACyBct-Y7Ib5aczw9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ec242e86.mp4?token=h3ab3FIo65bDKFtIG-fFcWOmpZWUpzhNKxhCn1DzUC7cpJlHkSVwA-dOdWT3hICFivBetNaZUv_HMnINAp0pl8FhTUIeREuSSLW0yi1NqWmNMaumPsfiQNL1pCzX-noL2kUZuJ6qHqCo1iXsiloQnz-8DJzziVxhO7HoKhlujuUQJ3MZM7xsxuo2k_X5rKqPugW_4M-aKg1aJnN5eUlGvZFMpQ8foLUbjVpm5d2LZpEAceHOrgeiBmRjSLmR-Vpg3tvZ--gRNHK0vwDqm2v94I82URs-jvAXnHMzUqe4RCH8LjnTcPYjXp9Fo_QiRwcEc3YnACyBct-Y7Ib5aczw9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زکریای رازی و پرداخت هزینه متفاوت بودن
#پادکست_کافئین
| فصل‌ دو، قسمت‌ نه
☕️
🔹
ابرکاشفی که نشان داد چطور یک متخصصِ تراز اول، می‌تواند با زیرِ سؤال بردنِ پیش‌فرض‌هایِ صلبِ گذشتگان و اتکا به دکترینِ «تست و داتایِ تجربی»، انحصارهای علمی جهان را بشکند و فرمول‌های جدید خلق کند.
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/_pAcf2fyVaU
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/671266" target="_blank">📅 07:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671265">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J70BLF9BukfGuzyA8fonerFLDM4TFk0LqA4MDvqMzv63AtKBu9xxf6aL24YR7MFmnDlaqFVuBCUcxZRA1WAtlhlsulqlSU9vfjVqTkmB0fRiXnGFNu6P1jrUNYLfX5qs8NvxXtbmwi9whXEWXulcaME7Sp5oeDVW6O-SYIbD8iSJF1TASjNqhS95X4SFaQpzOWn9BXXHUEtGU5Xi6bGLqB2DI5bbsEdQgN1NHeWdGHH7V8S2hOydDrtqVtD3Jz-ptoLkpgRSQh50z8OyA5TzKmleys9-yYTqmAHyuPODQnggdVqcYVEO09KmKgk1jJqb9MiUQd4opA2to2pN6k3azw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز چهارشنبه
۲۴ تیر ماه
۳۰ محرم ۱۴۴۸
۱۵ جولای ۲۰۲۶
چهارشنبه‌ها
#زیارت_نامه_ائمه_اطهار
بخوانیم
⬅️
متن و صوت زیارت‌نامه ائمه اطهار
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/671265" target="_blank">📅 07:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671262">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
حوزه‌های امتحانی نزدیک مراکز نظامی جابه‌جا شدند
آموزش و پرورش:
🔹
تمام حوزه‌هایی که در مجاورت مراکز حساس یا نظامی قرار داشتند، شناسایی و به مکان‌های امن‌تر همچون حسینیه‌ها و مراکز عمومی منتقل شدند تا محیطی کاملا ایمن فراهم شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/671262" target="_blank">📅 07:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671261">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۴/ پیام مهم سپاه به مردم کویت؛ مرکز ارتباطات ماهواره ای، رادار دفاع موشکی و هوایی، مجتمع پدافند هوایی پاتریوت و آمادگاه پایگاه نظامی آمریکا و سکوهای پرتاب موشک های‌مارس در کویت منهدم شدند  روابط عمومی سپاه:
🔹
مردم شریف و کریم کویت؛ شما به…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/671261" target="_blank">📅 07:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671260">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2c6ad201.mp4?token=J6G2HZ5zRIoa4NcIQTsdoBeb6LeTtnkbheps-FxTWQFqCDXacXFKZBFgKNwvRC2Nq1uY6Eiwwm6Uwojey55teENYM4fFDgNngm1HcqO55eq_jJJnZ2KRLAAID_JrH16j6IoU1CZY8ctIuzimBlpqWFhOCtxIk4M3JLRXN9Wh8719uFh0STIuH6CKNRF8ZjOQpQB7pl3Rz1-_sHuiUBXs4YJ3qTjCRdcaxKxPCKbq7d2MU-8HVDxrmxJDRlU-8heR_G9MH5sJDMi4c_7PEvnuCWT0VuVSflyMtIIObqxFP111fhGXd1AE-RSq5Kcufu2szCO0hEXt3axDb3ovJpiD9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2c6ad201.mp4?token=J6G2HZ5zRIoa4NcIQTsdoBeb6LeTtnkbheps-FxTWQFqCDXacXFKZBFgKNwvRC2Nq1uY6Eiwwm6Uwojey55teENYM4fFDgNngm1HcqO55eq_jJJnZ2KRLAAID_JrH16j6IoU1CZY8ctIuzimBlpqWFhOCtxIk4M3JLRXN9Wh8719uFh0STIuH6CKNRF8ZjOQpQB7pl3Rz1-_sHuiUBXs4YJ3qTjCRdcaxKxPCKbq7d2MU-8HVDxrmxJDRlU-8heR_G9MH5sJDMi4c_7PEvnuCWT0VuVSflyMtIIObqxFP111fhGXd1AE-RSq5Kcufu2szCO0hEXt3axDb3ovJpiD9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از خسارات وارده به مرکز تعمیر و نگهداری هواپیماهای جنگی در پایگاه هوایی العديد قطر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/671260" target="_blank">📅 07:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671259">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
صدای دوبارۀ انفجار در کویت و اردن
🔹
منابع عربی از شنیده شدن مجدد صدای انفجار در کویت و اردن خبر می‌دهند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/671259" target="_blank">📅 06:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671258">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
استانداری خوزستان : دو انبار غلات و آرد گندم در دشت آزادگان و هویزه مورد اصابت پرتابه های آمریکایی قرار گرفته است
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_khozestan</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/671258" target="_blank">📅 06:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671256">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۳ سپاه/ پیام مهم سپاه خطاب به مردم اردن؛ آشیانه جنگنده‌های اف ۱۵، ۱۶ و ۳۵ و تعدادی از پهپادهای راهبردی MQ9 آمریکا در پایگاه الازرق اردن در هم کوبیده شدند
🔹
سرزمین مقدس اردن قدمگاه انبیاست و جای اشغالگران و جنایتکاران بین المللی نیست، انتظار…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/akhbarefori/671256" target="_blank">📅 06:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671255">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۲/ مرکز مدیریت ان اس آی، مرکز کنترل فرماندهی ، انبارهای بزرگ قطعات و تجهیزات نظامی و مخازن سوخت ناوگان پنجم دریایی آمریکا در بحرین درهم کوبیده شد
🔹
مردم قهرمان و تاریخ ساز ایران اسلامی، ارتش کودک‌کش و رژیم عهد شکن آمریکا شب گذشته با انتشار…</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/671255" target="_blank">📅 06:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671254">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
سنتکام از پایان تازه‌ترین دور حملات خود در ایران خبر داد
فرماندهی مرکزی آمریکا:
🔹
این حملات هم‌زمان با ازسرگیری اجرای محاصره دریایی از سوی نیروهای آمریکایی انجام شده و هفت ساعت به طول انجامیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/671254" target="_blank">📅 05:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671253">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۱ / KJL مرکز اصلی آماد و پشتیبانی ارتش آمریکا در غرب آسیا در مینا عبدالله کویت به آتش کشیده شد  روابط عمومی سپاه:
🔹
دشمن آمریکایی که شب های گذشته به بهانه اصابت کشتی‌های متخلف به پایگاه‌های ما حمله می‌کرد، دیشب هم که هیچ کشتی جرات تخلف و همراهی…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/671253" target="_blank">📅 05:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671252">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
تکذیب سفر نتانیاهو به واشنگتن
🔹
کاخ سفید بامداد چهارشنبه گفت که برنامه‌ای برای سفر نخست‌وزیر رژیم صهیونیستی به آمریکا تدوین نشده است.
🔹
پیش از این رسانه‌های صهیونیستی گفته بودند که نتانیاهو قصد دارد برای گفتگو درباره موضوعات مهم به کاخ سفید برود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/671252" target="_blank">📅 05:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671251">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱۱ / KJL مرکز اصلی آماد و پشتیبانی ارتش آمریکا در غرب آسیا در مینا عبدالله کویت به آتش کشیده شد
روابط عمومی سپاه:
🔹
دشمن آمریکایی که شب های گذشته به بهانه اصابت کشتی‌های متخلف به پایگاه‌های ما حمله می‌کرد، دیشب هم که هیچ کشتی جرات تخلف و همراهی با آمریکا را نکرد و طبیعتا اصابتی هم نبود، برای پنهان کردن شکست و ناتوانی خود تعدادی از پایگاه‌های ساحلی و نقاطی در استان‌های جنوبی کشور را هدف موشک‌های کروز و بمب جنگنده‌های خود قرار داد که رزمندگان مقتدر اسلام با پاسخ‌های کوبنده متجاوزان را تنبیه و سرکوب کردند.
🔹
در موج چهارم عملیات نصر۲ با رمز مبارک یا اباعبدالحسین (ع)، KJL مرکز اصلی آماد و پشتیبانی ارتش آمریکا در غرب آسیا در مینا عبدالله کویت به آتش کشیده و منهدم گردید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/671251" target="_blank">📅 05:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671250">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8196a05790.mp4?token=TpruVTcPPsUoXlt-iaxtIWnrx6m_6Q9rBgDFqrgeZYou6TjWb3_lc-S3eWqabADLRwaaWVn7dklHcYBPAkaPIiTS3hroqpCQlRApxT3QDeGfEn_EsDRurKYtq_Ws8fHh7YiEGrVzCf6JUSFCMHPjh5oZAL417vldbSTmkzfuzHVYQArVtIhFtjZH7l5BLnGpj9J0xwshYbc1FabzDrnFPlqdQK9SFZWc2kyNBqcVrF11u3vUUZ577Ee2AUWYwoO07QIuxB1xK0QzRe_DJbYIcUMucVuwxern_A9nqoDZiKkqUV95tORXkJRfrmkQeenfvQdJ3x24SaVJRqjyEMVr8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8196a05790.mp4?token=TpruVTcPPsUoXlt-iaxtIWnrx6m_6Q9rBgDFqrgeZYou6TjWb3_lc-S3eWqabADLRwaaWVn7dklHcYBPAkaPIiTS3hroqpCQlRApxT3QDeGfEn_EsDRurKYtq_Ws8fHh7YiEGrVzCf6JUSFCMHPjh5oZAL417vldbSTmkzfuzHVYQArVtIhFtjZH7l5BLnGpj9J0xwshYbc1FabzDrnFPlqdQK9SFZWc2kyNBqcVrF11u3vUUZ577Ee2AUWYwoO07QIuxB1xK0QzRe_DJbYIcUMucVuwxern_A9nqoDZiKkqUV95tORXkJRfrmkQeenfvQdJ3x24SaVJRqjyEMVr8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرحله هشتم عملیات صاعقه ارتش؛ ادامه حملات پهپادی ارتش به پایگاه‌ آمریکا در اردن
روابط عمومی ارتش:
🔹
به دنبال  تکرار حملات وحشیانه دشمن بد عهد،  بامداد امروز، مرحله هشتم عملیات صاعقه با موج جدیدی از حملات پهپادی ارتش جمهوری اسلامی ایران علیه پایگاه‌های آمریکا در منطقه اجرا شد و محل استقرار جنگنده‌های اف ۱۸ و سوله های بزرگ تجهیزاتی ارتش تروریستی آمریکا در پایگاه الازرق اردن، برای دومین بار، هدف حملات پهپادهای انهدامی قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/671250" target="_blank">📅 05:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671249">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8efU9wFNN0lTy-aL35Pq_LMw_ILCJaYFBzLJa8vxKp5_Qy40BBtVsBqCGzjR0if1Luy8havLUBtiHr7pwc0OT6kIbli1mxYk0a-I4eK6-8lzBLbint9Lq9ui_1BJCIR_Fza6bxeSMJDjd1aBiwwuJsyi5L7QLTcbFKQFEGex0ZyDvSDIxR4iEC6W3pcR9jwCzbV1Uf2BN4ZUR3DRpyVxV1NlbhPxZZJ94rQeJBw8UpzxlXrSyb-UjOWUgdizv0Gv6YipvsVqvKgR8b_MOJCB7WYukyuvKQsCdYWR2mAiLcIt4u9CDUyPJxZqzkCFSp_qMZsS1qg8LoGfhV5CCGIUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت پهپاد ایرانی به منافع آمریکا در کویت
🔹
رسانه‌های عربی با انتشار ویدیویی مدعی اصابت دقیق پهپاد به تأسیسات آمریکایی در بندر «عبدالله» در کویت شدند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/671249" target="_blank">📅 04:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671248">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7f2f24fb.mp4?token=giHEVblp_8rvuaHad0KvcVszWrKDsBLWmeX4PZyDvpxagmmfL1vwIjq8id-mRxMbTkwa8ea0tZ4DDb91SzTxjOlSJwJnDhbeyno8hr_m3Y-mh8tGeQiH6Q73A3VKYJBUvFEYcpSRlwl92pqLr8Mm5j60idYkVyebPBt2sK_sB-7rulWArU-N-fg4mq2X8f3alIEQNqiXboTzFlukEItHPKq2JhQOafZWty9_zoZfSQoSr_Ycj9CWfG9jSVJZYSZ_A57mMxsAiwFSk7tdrrufohcAyv6hCFrcj8uVQj6cRPbpi2wuW2Ca5uwTfmQCFmFavQ9LmMpk-r6rZYNIfeI_cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7f2f24fb.mp4?token=giHEVblp_8rvuaHad0KvcVszWrKDsBLWmeX4PZyDvpxagmmfL1vwIjq8id-mRxMbTkwa8ea0tZ4DDb91SzTxjOlSJwJnDhbeyno8hr_m3Y-mh8tGeQiH6Q73A3VKYJBUvFEYcpSRlwl92pqLr8Mm5j60idYkVyebPBt2sK_sB-7rulWArU-N-fg4mq2X8f3alIEQNqiXboTzFlukEItHPKq2JhQOafZWty9_zoZfSQoSr_Ycj9CWfG9jSVJZYSZ_A57mMxsAiwFSk7tdrrufohcAyv6hCFrcj8uVQj6cRPbpi2wuW2Ca5uwTfmQCFmFavQ9LmMpk-r6rZYNIfeI_cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ‌کس نمی‌داند ایران چقدر موشک دارد
🔹
مجری: به نظر شما ایران چند موشک باقی گذاشته است؟
🔹
ترامپ: آنها تعدادی دارند...
🔹
مجری: صدها؟ هزاران؟
🔹
ترامپ: نمی‌خواهم بگویم. هیچ‌کس نمی‌داند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/671248" target="_blank">📅 04:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671247">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
وزارت کشور بحرین اعلام کرد که بار دیگر آژیرهای خطر فعال شده‌اند و شهروندان و اتباع مقیم با حفظ خونسردی و آرامش، خود را به نزدیک‌ترین مکان امن برسانند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/671247" target="_blank">📅 04:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671246">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da70cb380f.mp4?token=XvAPvso1qkIQfSw0DsYnIDeVDuKS6rQYpQy6rpZHKjLj3MquZUlA7oJ3s4iS8ZSLy6-h2lvj5tRJjhg_xhejlI3CuW799JoSvdU5s_N3ytGur3W1hJ74kppb0b0dQ1K3lrMQb23Goz10jFes-AQxoZ_2jUNcLVcWaGBWeYA-Q9bnw1gFeGvhw91XVxwtmdmtpye3Xuh9l7VxKCVs9Qk4Uh67Ir52R7b8L3rGmswtVTNh2H_yv0m5mY9K8ZS5nLxHy3TpgNUq482gZtLzBK-Se8xPj9hWqSpCB74yQEPGOSc8vIDF8EqsB36ZzRqMdVn6c9ICcWlC5Dlf6w-Dk9MoXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da70cb380f.mp4?token=XvAPvso1qkIQfSw0DsYnIDeVDuKS6rQYpQy6rpZHKjLj3MquZUlA7oJ3s4iS8ZSLy6-h2lvj5tRJjhg_xhejlI3CuW799JoSvdU5s_N3ytGur3W1hJ74kppb0b0dQ1K3lrMQb23Goz10jFes-AQxoZ_2jUNcLVcWaGBWeYA-Q9bnw1gFeGvhw91XVxwtmdmtpye3Xuh9l7VxKCVs9Qk4Uh67Ir52R7b8L3rGmswtVTNh2H_yv0m5mY9K8ZS5nLxHy3TpgNUq482gZtLzBK-Se8xPj9hWqSpCB74yQEPGOSc8vIDF8EqsB36ZzRqMdVn6c9ICcWlC5Dlf6w-Dk9MoXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت موشک‌های ایرانی به اهداف آمریکایی در بحرین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/671246" target="_blank">📅 03:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671245">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
پهپادهای ایرانی به کویت رسیدند
🔹
ارتش کویت از فعال شدن پدافندی هوایی این کشور برای مقابله با پهپادهای از سمت ایران خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/671245" target="_blank">📅 03:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671244">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba861f0f8.mp4?token=dnsSYal6-iUvSndKee4XIty83d-8zgjz1bvnk-ol-94iLMR_ZU7rHRNGkK5-EjjH0Vbo7Z_oXE6UgfGeSfsMMzHEalnGqpIgwFzDRxru8qn3xGZRJUXRVlYSArsqUp69g4Ude4AEKtpQS0_63sbJ_msmQmUC8x5C9Xcx09E688fMoIl32A-rolDWlDjpehDqKYV7pI9aVb1Nq_02rEG2mMYB70nQiYhzGgvd6akpEmFQXxr_7jJoSrVNFFrlUR2rOplScgkqt7Q6hmFPlTR1CfWKw-6ZsV-7POlTTsPsyA1znwGaBr3Z2V8Ip-nJUj0qM1aHWpnJctEdWhfU_SU8pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba861f0f8.mp4?token=dnsSYal6-iUvSndKee4XIty83d-8zgjz1bvnk-ol-94iLMR_ZU7rHRNGkK5-EjjH0Vbo7Z_oXE6UgfGeSfsMMzHEalnGqpIgwFzDRxru8qn3xGZRJUXRVlYSArsqUp69g4Ude4AEKtpQS0_63sbJ_msmQmUC8x5C9Xcx09E688fMoIl32A-rolDWlDjpehDqKYV7pI9aVb1Nq_02rEG2mMYB70nQiYhzGgvd6akpEmFQXxr_7jJoSrVNFFrlUR2rOplScgkqt7Q6hmFPlTR1CfWKw-6ZsV-7POlTTsPsyA1znwGaBr3Z2V8Ip-nJUj0qM1aHWpnJctEdWhfU_SU8pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس صداوسیما: آقای خاتمی می‌گوید طرف‌داران جنگ و انتقام، اسرائیلی نیستند اما حرف اسرائیلی‌ها می‌زنند، ما هم نمی‌گوییم که آقای خاتمی اسرائیلی است اما ایشان دقیقا دارد حرف اسرائیلی‌ها را می‌زند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/671244" target="_blank">📅 03:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671243">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/599c252863.mp4?token=DB0Kr9XSghJK3B6t2cuxuTV-pCzmXTIXUtm80my1HCCc4fbYiVIMqCMkf_sE0P6ajM6TN-YJ2afQirwod7fTvaSWyFUIMqRZkCMtXbkJAPhoaoteRswYjc1S1X2f66T6pLIrMXarMnKER7BZ6LsfrrTx77fmjcvOYxN3GdMc0jHZlKoWmWYWXme76G2HKH6I84GTCldujrxjLELCmic9rdfOBD19s1i8nf9sRpf4h3RIRMrkW7eEzftUbM_c6A2nWCkp4phlzwiG4fTzJHf5irDR6purzsoBWS2zYi79BtXUNFq4tYuFx_aAHEcUNvfXq2VvFeaJ_vAaLqMuZm-CqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/599c252863.mp4?token=DB0Kr9XSghJK3B6t2cuxuTV-pCzmXTIXUtm80my1HCCc4fbYiVIMqCMkf_sE0P6ajM6TN-YJ2afQirwod7fTvaSWyFUIMqRZkCMtXbkJAPhoaoteRswYjc1S1X2f66T6pLIrMXarMnKER7BZ6LsfrrTx77fmjcvOYxN3GdMc0jHZlKoWmWYWXme76G2HKH6I84GTCldujrxjLELCmic9rdfOBD19s1i8nf9sRpf4h3RIRMrkW7eEzftUbM_c6A2nWCkp4phlzwiG4fTzJHf5irDR6purzsoBWS2zYi79BtXUNFq4tYuFx_aAHEcUNvfXq2VvFeaJ_vAaLqMuZm-CqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله دشمن آمریکایی به پادگان ارتش در بمپور/ هنوز آمار دقیقی از خسارات و تلفات در بمپور در دست نیست
🔹
حدود ۳۰ الی ۳۵ دقیقه قبل بود که صدای چندین انفجار از این منطقه شنیده شد و حکایت از این داشت که جنگنده‌های کشور آمریکا به پادگان ارتش حمله کرده بودند. ظاهرا شلیک‌ها به سمت آسایشگاه سربازها بوده که در حال استراحت بودند.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/671243" target="_blank">📅 03:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671242">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای چند انفجار در بحرین خبر می‌دهند
🔹
گفته می‌شود این انفجارات در اثر شلیک موشک‌ها به‌سوی پایگاه‌های آمریکایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/671242" target="_blank">📅 03:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671241">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6d169a6b.mp4?token=BvLsG4JL8PUq8wn40SPZop3G5KG28yzyFgV9s4wjMl2ZYKKnCbFiwq1BU1yC65KDYryg1ygNFDFz0ZB7tX6mxVeq8n1Vb9Oth_lv64jpw9UnFiXPtca30AmvjN8SWSnqOga_GWT7xu6oWfOFzKoqGWro7wgdreHQkBNAOuKbOI3U8b9OTpiHvBUKbntUejL0PdCCl9H3jnFKYfXYLdJZR4BZ9cMgjhqdxyJ6TbcgN2OzmrMyremUh5-Wc_788Lw0kOcbe1bwUY-cJuZulLhMuvzS-naM0J9tGNwJa8Ul7tlOsF7Y7a73pZ1zFGLDaCUwwIVHRMlc_nKZmXq-li3vOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6d169a6b.mp4?token=BvLsG4JL8PUq8wn40SPZop3G5KG28yzyFgV9s4wjMl2ZYKKnCbFiwq1BU1yC65KDYryg1ygNFDFz0ZB7tX6mxVeq8n1Vb9Oth_lv64jpw9UnFiXPtca30AmvjN8SWSnqOga_GWT7xu6oWfOFzKoqGWro7wgdreHQkBNAOuKbOI3U8b9OTpiHvBUKbntUejL0PdCCl9H3jnFKYfXYLdJZR4BZ9cMgjhqdxyJ6TbcgN2OzmrMyremUh5-Wc_788Lw0kOcbe1bwUY-cJuZulLhMuvzS-naM0J9tGNwJa8Ul7tlOsF7Y7a73pZ1zFGLDaCUwwIVHRMlc_nKZmXq-li3vOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اصابت پهپاد ایرانی به منافع آمریکا در کویت
🔹
رسانه‌های عربی با انتشار ویدیویی مدعی اصابت دقیق پهپاد به تأسیسات آمریکایی در بندر «عبدالله» در کویت شدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/671241" target="_blank">📅 03:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671240">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22c595e8a6.mp4?token=Ffo_058_JFvQOEFcssFZbQfkmtOwZOtFUyLER0MP6wbQi5lHgHuuognUAHZim3iHuLfzzX6mhf35kKN5pHWJA8YeAl7FSx4qYXPg8c3jq_K_FSp-1-C-xqN1ebx1dGu6MfhE-9anivOmHiUbF2hEPpTK-GJqkuPfT1nKcVqIHbM3pXPJhkANMVOKf9I3zztpzFTP006OUMgSjJVBShi-6YCTKsYq2ToBPpTZ1138sUiATzyJSrKNwY10ZyUG-XKqjuL9ZGh61FikyXoyGncMtWoEPNuYQ2pcZCay5iqnJ5QDZDsC0KSPzNQZ-EDD0SNDMaZriQPw2l-4jwM7OrHEFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22c595e8a6.mp4?token=Ffo_058_JFvQOEFcssFZbQfkmtOwZOtFUyLER0MP6wbQi5lHgHuuognUAHZim3iHuLfzzX6mhf35kKN5pHWJA8YeAl7FSx4qYXPg8c3jq_K_FSp-1-C-xqN1ebx1dGu6MfhE-9anivOmHiUbF2hEPpTK-GJqkuPfT1nKcVqIHbM3pXPJhkANMVOKf9I3zztpzFTP006OUMgSjJVBShi-6YCTKsYq2ToBPpTZ1138sUiATzyJSrKNwY10ZyUG-XKqjuL9ZGh61FikyXoyGncMtWoEPNuYQ2pcZCay5iqnJ5QDZDsC0KSPzNQZ-EDD0SNDMaZriQPw2l-4jwM7OrHEFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلمی دیگر از عبور موشک‌های بارشی ایران از پدافند آمریکایی در اردن و اصابت مستقیم به پایگاه آمریکا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/671240" target="_blank">📅 03:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671239">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/078c717ca6.mp4?token=UjWpqYOs5bXBoH8sAU2AEA14SuH9Qt3xpKDfZZiUFMWdF8ECT1V7wyhM37aLWNepWyskax1pO5_mb9oPSv975U0LrfPkRveS-1m8PUgksbBhLe_2SPmi7oVKOTkmZOc4KUqNYndfit0t99lqpIzpvQVXA9FbRYCUsGQq7LkUzU-l5vo8Mfe6AmdpIj6OXo5CjR3Qwr2hG8qg27_KTvvAIJrgB4D0BleqsYq0D3oHptVe-umBqkiOC3HOE-Dcvy2iusuTttZfOozLIQzWbYIPNU1LRSwCyUZGHgCddx5bhSM6A9_DbP0dg-IgsG6Pnr-r81gkTb3V97DscCwJiw_HBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/078c717ca6.mp4?token=UjWpqYOs5bXBoH8sAU2AEA14SuH9Qt3xpKDfZZiUFMWdF8ECT1V7wyhM37aLWNepWyskax1pO5_mb9oPSv975U0LrfPkRveS-1m8PUgksbBhLe_2SPmi7oVKOTkmZOc4KUqNYndfit0t99lqpIzpvQVXA9FbRYCUsGQq7LkUzU-l5vo8Mfe6AmdpIj6OXo5CjR3Qwr2hG8qg27_KTvvAIJrgB4D0BleqsYq0D3oHptVe-umBqkiOC3HOE-Dcvy2iusuTttZfOozLIQzWbYIPNU1LRSwCyUZGHgCddx5bhSM6A9_DbP0dg-IgsG6Pnr-r81gkTb3V97DscCwJiw_HBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرار نتانیاهو از کنست در پی شعارهای نمایندگان مخالف
🔹
نتانیاهو که همزمان با جلسه رای‌گیری درباره لایحه معافیت یهودیان حریدی در کنست حضور پیدا کرده بود با اعتراض شدید نمایندگان روبرو شد.
🔹
نمایندگان مخالف با شعارهای «گم شو، گم شو» و «ننگ برتو» نتانیاهو را وادار به خروج از ساختمان کنست کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/671239" target="_blank">📅 03:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671238">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
خبرگزاری رویترز: دموکرات‌های سنا به دلیل مخالفت با جنگ ایران، لایحه ۱/۵ تریلیون دلاری بودجه دفاعی آمریکا را متوقف کردند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/671238" target="_blank">📅 03:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671236">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c25d764910.mp4?token=LRSb1WCDb0ifDZrssz29Ef4rMqvdVSJs3XGljSKSh052I38rz4nZ-x2V_CmGFiVtZvHfj09mDv-9CrD2Od1YqXpaf7mMdG5XiWAgaRE2dUvo1GnTaJnYZ28_uqu8TBU1OxZEU_a6KWMlEJAsn7c9YwKrRW_qMemx_IyhTLF9anE5wpWPk2Axb1h3emhgn_odKWJh7tSFRUMyZmgsEkYjBeHxVRd40JNgd6GzwS1XeubLQ-RujxRG3HbQJaxDpkX1FsiGSwYKdv19nTaauWJf5GtgsiDJxHgVdePWivIqUg4pPXjpYtpLqg17e1ZXeSNIaIxpzMdkn0b0oioRDcKcHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c25d764910.mp4?token=LRSb1WCDb0ifDZrssz29Ef4rMqvdVSJs3XGljSKSh052I38rz4nZ-x2V_CmGFiVtZvHfj09mDv-9CrD2Od1YqXpaf7mMdG5XiWAgaRE2dUvo1GnTaJnYZ28_uqu8TBU1OxZEU_a6KWMlEJAsn7c9YwKrRW_qMemx_IyhTLF9anE5wpWPk2Axb1h3emhgn_odKWJh7tSFRUMyZmgsEkYjBeHxVRd40JNgd6GzwS1XeubLQ-RujxRG3HbQJaxDpkX1FsiGSwYKdv19nTaauWJf5GtgsiDJxHgVdePWivIqUg4pPXjpYtpLqg17e1ZXeSNIaIxpzMdkn0b0oioRDcKcHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه شیرجه و اصابت دقیق موشک ایرانی در پایگاه آمریکا در اردن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/671236" target="_blank">📅 03:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671235">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
یک واحد تولید آب معدنی در اطراف روستایی در بخش موسیان در ایلام هدف ۳ پرتابه دشمن دشمن قرار گرفت
/ ایرنا
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/671235" target="_blank">📅 02:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671233">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2jC0ePusLNN9UZZU8D0pekDL2E_8m777MhaQbrnyuVtWeBOHiw4wSHXos1Nu19juNQD-7T5BWkJG-lxpM_JR9FEPzBWyMLMWQgGcUIlFVo2PkjjkP6NzOo5A5F3VLhXfcmdqm3sDkWTZqp5ysZUQeI7LShy7kSjDx-7QEZZu-6-U5AvQQY_iEHhKTiaMhCq97lhbaPeGq6t6hD86Us4TV61wCRmB3ESRsH1fUK3bGyhnelQwOovAEzH35UXjfUuASDmPw-WvgMwVLgkqxEPgMIpPJU0ul9uxWc_rnT9R-dShpwrz5GYsVP1G184TCHFawmzrElTccPZnizsnvCnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اصابت موشک ایرانی در شمال اردن
🔹
تصویری که رسانه عراقی از اصابت موشک ایرانی به پایگاه تروریست‌های آمریکایی در شمال شرقی اردن منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/671233" target="_blank">📅 02:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671232">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a59ef456c.mp4?token=R_ebk8f7vlkjQZd56m4v-EgRn4xzcZGHiwo9t3lfWJ47KPxQsXyB096CKF0yc1PBgqwzHy3gDmayRcj5eumdq8n-lmLRK7hi8A1ZmwWylqsMtZRXYPR2q-9DkwSEQNmmpn-Xcw5RwRYSQ2ufhNtUANTcOWsgrFFVqmJ1oWl98ARzyp3X1J0zIGielEPkhsf2kijZDqg9C6Sd_SQDc97NP4pWUc4yy5u_1wmvbWAUughWoCpag3zIUwYes-03r7sOmAmLE6138ZmTugXtLspy59wHA86mstdI3B8E4B7AWbWfpRKJTgwPh3ykUbmhoA98alBJlvE_EvnEab9j-P3ubw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a59ef456c.mp4?token=R_ebk8f7vlkjQZd56m4v-EgRn4xzcZGHiwo9t3lfWJ47KPxQsXyB096CKF0yc1PBgqwzHy3gDmayRcj5eumdq8n-lmLRK7hi8A1ZmwWylqsMtZRXYPR2q-9DkwSEQNmmpn-Xcw5RwRYSQ2ufhNtUANTcOWsgrFFVqmJ1oWl98ARzyp3X1J0zIGielEPkhsf2kijZDqg9C6Sd_SQDc97NP4pWUc4yy5u_1wmvbWAUughWoCpag3zIUwYes-03r7sOmAmLE6138ZmTugXtLspy59wHA86mstdI3B8E4B7AWbWfpRKJTgwPh3ykUbmhoA98alBJlvE_EvnEab9j-P3ubw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تلاش سامانه پاتریوت در اردن برای مقابله با موشک بالستیک ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/671232" target="_blank">📅 02:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671231">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
وقوع انفجار در پایگاه‌های آمریکا در اردن
🔹
منابع عربی بامداد چهارشنبه از هدف قرار گرفتن پایگاه‌های محل استقرار نظامیان آمریکایی در اردن توسط موشک‌های ایرانی خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/671231" target="_blank">📅 02:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671230">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
بیانیه سنتکام درباره عملیات‌های ایران علیه پایگاه‌های آمریکا
🔹
«برد کوپر» فرمانده سازمان تروریستی سنتکام بامداد چهارشنبه مدعی شد که ایران طی یک هفته گذشته، به ۷ کشتی تجاری حمله کرده و همچنین تعداد زیادی موشک و پهپاد به سمت پایگاه‌های آمریکا در منطقه شلیک کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/671230" target="_blank">📅 02:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671229">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
حملۀ آمریکا به دهلران
🔹
دقایقی قبل، یک نقطه در شهرستان دهلران مورد تهاجم و اصابت پرتابه های دشمن آمریکایی قرار گرفت. هنوز از محل دقیق انفجارها و میزان خسارت‌های احتمالی خبری در دست نیست./ فارس
#اخبار_ایلام
در فضای مجازی
👇
@akhbarilam</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/671229" target="_blank">📅 02:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671228">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
خوک نجس: ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم
🔹
ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند.…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/671228" target="_blank">📅 02:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671224">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f4c90a8b.mp4?token=gzFC5C0u7ItP_E0pM3qLhX7imKt2lN4sBnwXpv_fuHeJmTEad7bWT12KxysjEqvJUrZa2D55vwfm_6z6Ah3hHYEBHftuBNmqTe7cMctNfCASGo4n1Rt29xtQ9omkLPGGm8Q5odQHxmaMy_awVsWnmfCk7h8p_upmv3uaFDmXDBeM4tdClqizslFpDoYitWF0RNft21KaWPx7-_-u9QoxdRl5DSIDu_hvPMUEQHDwM-BX80mhNMnI_iweExoZGdk3-f4JxmiVkq2fXl_fhRSXAlZ1lEYKCJC7vfYhzkz4nGI_xNScJcLpam8p8y-3F1E9tvbBLULOUO0TVbgUD8-e0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f4c90a8b.mp4?token=gzFC5C0u7ItP_E0pM3qLhX7imKt2lN4sBnwXpv_fuHeJmTEad7bWT12KxysjEqvJUrZa2D55vwfm_6z6Ah3hHYEBHftuBNmqTe7cMctNfCASGo4n1Rt29xtQ9omkLPGGm8Q5odQHxmaMy_awVsWnmfCk7h8p_upmv3uaFDmXDBeM4tdClqizslFpDoYitWF0RNft21KaWPx7-_-u9QoxdRl5DSIDu_hvPMUEQHDwM-BX80mhNMnI_iweExoZGdk3-f4JxmiVkq2fXl_fhRSXAlZ1lEYKCJC7vfYhzkz4nGI_xNScJcLpam8p8y-3F1E9tvbBLULOUO0TVbgUD8-e0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موشک‌های ایران در راه پایگاه‌های آمریکا در سراسر منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/671224" target="_blank">📅 02:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671223">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
آغاز موشک‌باران پایگاه‌های آمریکا در منطقه
🔹
منابع خبری از شلیک موج تازه موشک‌های بالستیک به سمت پایگاه‌های آمریکا در منطقه خبر می‌دهند. در این میان آژیرهای هشدار در اردن به صدا درآمده و پدافند موشکی مستقر در پایگاه‌های آمریکا برای مقابله با موشک‌های ایرانی فعال شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/671223" target="_blank">📅 02:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671222">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
منابع عربی از وقوع انفجارهایی در پایگاه‌های نظامی آمریکایی در اردن خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/671222" target="_blank">📅 02:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671221">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dacf0d7f3.mp4?token=d-fJCjFa8Tz0tvZ3MJ88fun2kVTJptI2unUZD2H01Mt88KOgANTrFE4Z9bTQ-BEKDDpWh4nLuN2d-5YoteuolY4r834j-XRg4Mi2DHX3H1hWMd1zaSeyc_hvSb9vz_wA-wYTWYlhzDcJIYHDcF3e2rFxOu5xVvnPSDteV6d36V79rw4EiI91Af8DGxv2I_OT5GYxAySLnPkBjqFNl7gvDtnbU_qffiDlxyGG3VqDZzt7bGe3HdEAEzuLf1hPwqkrWoTUvKFWXWF2os2Bn3i4jAvbPLwzaAPB01zftYNpByCT9CRUgFu3U6noMYEjlTZRJU1Pql2l136edpPwOR7kUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dacf0d7f3.mp4?token=d-fJCjFa8Tz0tvZ3MJ88fun2kVTJptI2unUZD2H01Mt88KOgANTrFE4Z9bTQ-BEKDDpWh4nLuN2d-5YoteuolY4r834j-XRg4Mi2DHX3H1hWMd1zaSeyc_hvSb9vz_wA-wYTWYlhzDcJIYHDcF3e2rFxOu5xVvnPSDteV6d36V79rw4EiI91Af8DGxv2I_OT5GYxAySLnPkBjqFNl7gvDtnbU_qffiDlxyGG3VqDZzt7bGe3HdEAEzuLf1hPwqkrWoTUvKFWXWF2os2Bn3i4jAvbPLwzaAPB01zftYNpByCT9CRUgFu3U6noMYEjlTZRJU1Pql2l136edpPwOR7kUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به احترام جنوب...
💔
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/akhbarefori/671221" target="_blank">📅 02:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671219">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uj9lSbtj1Uq_6DAlYnhfc-MdU9knCRLWN-Ch7plUjk8UCg2JpVJQLsF3z5LMyjuEBz4bgQ6iYPfxPrzQmIrKQBwL3gvkA-GEYyCCeXeYnO7xMEGVokUPcz96JL2ljJR5EOT8Q39zFy4X8AlwN9bcBIYHcwAnbphVGUOw7J-miXnSzMYPD7TapUlW82QK7q_wpA_KixELNMB-CpPSVOgF620-_mi034HfMQzATKHpeRv9wSOHBe2tVI6eEuakf6boEowZNRTLEv3cUiNhleQ4LlgQ8YrIQX6zY3v-2EYZQf6W6yLJ20mE20JtnVr86vJSmtVzENryqcG3K6F9cpQg0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5FdoTJ1F3nx_MbIhxEj1asvDSSAeDKOmENY9_qB_wNd6SQjwc4nLV9F7b3L_U5I5rLF6rj36nwXcWig_LHcdXN-bN_LU5jRg7mB-p12Xs8iTJc4DF1auK_xtTirkpHtGDRO9DteLzesvLLzuakAivfkZs0kLpp80WjtWQgw_amnA7qsNGi8-K8wdMpQwdVbxtwXj7ivZ-NW8vmfMn5uMxghlqVCCW8qhcikUVEv1vr5gPejXyf7O6fJaR5ryfsFyXuZv9z9o6DvL2K110VS6UT6HNhLSDPSTZEUXngdV86mGxWKiBXBtwcNnmRBih9UQWt2hklgzfqgig0a7ObL8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویری جالب از پزشکیان در مراسم مصلای تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/671219" target="_blank">📅 02:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671218">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
شنیده‌ شدن صدای انفجار در کویت
🔹
رسانه‌های عربی بامداد چهارشنبه از وقوع انفجارهای مهیب و متعدد که باعث آتش‌سوزی در یک مرکز حیاتی مهم در کویت شد، خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/671218" target="_blank">📅 02:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671217">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0021e2c0f.mp4?token=AC8O7-pL2See3LJfu9GS8ncH3GtwJ2pzznCnM_bouYDc2e5-tO7sJjSDLDAK86JfMftzrRFhd9h5pcwljd0zaa_v0aC9csUBSXRfENuTulye-dPoEDEwgHQKGMBduBmeAL-IRcFgkfgk_LzDmNwG74_2QQWs5ioB-JQN2VCVnNHUh3VzXaVN80O4Y387bVylbVKZ2_FzCizMYdn0b4xQsa7QcENshpa7Z85AATh00CumtvlGV0q_f5n2h7-RM7kreKk5m0TLsB_fzvD9tXLr0qzKvSzln4aKd6qUG5phh_cX871l5xZ1D9nx90BlQYWXRGEj_goFva36n0Rl1-0uCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0021e2c0f.mp4?token=AC8O7-pL2See3LJfu9GS8ncH3GtwJ2pzznCnM_bouYDc2e5-tO7sJjSDLDAK86JfMftzrRFhd9h5pcwljd0zaa_v0aC9csUBSXRfENuTulye-dPoEDEwgHQKGMBduBmeAL-IRcFgkfgk_LzDmNwG74_2QQWs5ioB-JQN2VCVnNHUh3VzXaVN80O4Y387bVylbVKZ2_FzCizMYdn0b4xQsa7QcENshpa7Z85AATh00CumtvlGV0q_f5n2h7-RM7kreKk5m0TLsB_fzvD9tXLr0qzKvSzln4aKd6qUG5phh_cX871l5xZ1D9nx90BlQYWXRGEj_goFva36n0Rl1-0uCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک نجس: ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم
🔹
ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند. اگر آن‌ها کوچک‌ترین حرکتی انجام دهند، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشد را انجام خواهیم داد.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/671217" target="_blank">📅 02:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671215">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de4c546ec0.mp4?token=TgGkKibkfsg_KKXIhm-7b-eKb48NveSROzBPQ8Pc2OFIB8NcqggfT1Dtjl-nXhNqdMpsd7VHpi1T4JSl7Hqe6La-eUrilCCQdAwPTefbFUUMWjfY_qoyRKM-45NCSMikAKo-8socJjr8EiCHvEBLtejtwn_VD2xNiiJlpuiahT1_zeXRkg0dQhWoW1VXeSc5AodXCWN1ifag1ldJczs3Y6voTTuSfXE09Pna0d6Jb7_IMO4yu88-4LTgrTO91Hsfx0f0xDzD_NdxEagm-9PA42RwiVYY62sc3VBZ_kI-3vbuhH2DTW1pEvr22YH1j0Mp0soZVNt4iWlrAk8z_qzKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de4c546ec0.mp4?token=TgGkKibkfsg_KKXIhm-7b-eKb48NveSROzBPQ8Pc2OFIB8NcqggfT1Dtjl-nXhNqdMpsd7VHpi1T4JSl7Hqe6La-eUrilCCQdAwPTefbFUUMWjfY_qoyRKM-45NCSMikAKo-8socJjr8EiCHvEBLtejtwn_VD2xNiiJlpuiahT1_zeXRkg0dQhWoW1VXeSc5AodXCWN1ifag1ldJczs3Y6voTTuSfXE09Pna0d6Jb7_IMO4yu88-4LTgrTO91Hsfx0f0xDzD_NdxEagm-9PA42RwiVYY62sc3VBZ_kI-3vbuhH2DTW1pEvr22YH1j0Mp0soZVNt4iWlrAk8z_qzKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دروغ ارتش اردن در رهگیری موشک‌های ایرانی؛ موشک‌هایی که به هدف خوردند اما اردنی‌ها نخواستند ببینند
🔹
ارتش اردن امروز اعلام کرده بود ۴ موشک بالستیک ایرانی را که به سمت این کشور پرتاب شده بودند، رهگیری کرده است!
🔹
ویدیو منتشرشده از پایگاه ملک فیصل در جنوب اردن که ظاهرا هدف حمله بوده نشان می‌دهد سامانه پاتریوت مستقر در پایگاه در رهگیری موشک‌ها ناکام بوده و تقریبا همه کلاهک‌ها به هدف اصابت کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/671215" target="_blank">📅 02:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671214">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
کاردار ایران در لندن به وزارت خارجه انگلیس‌ فراخوانده شد
🔹
وزارت خارجه انگلیس‌ می‌گوید که در واکنش به آنچه نقش نیروی قدس سپاه پاسداران در هدایت گروه‌های نیابتی برای انجام مجموعه‌ای از حملات در سراسر اروپا خوانده شده، کاردار ایران در لندن را احضار کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/671214" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671213">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
شنیده‌ شدن صدای انفجار در کویت
🔹
رسانه‌های عربی بامداد چهارشنبه از وقوع انفجارهای مهیب و متعدد که باعث آتش‌سوزی در یک مرکز حیاتی مهم در کویت شد، خبر دادند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/akhbarefori/671213" target="_blank">📅 02:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671212">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای شیطان زرد: نمایندگان من یک ساعت پیش با ایرانی‌ها صحبت کردند  #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/akhbarefori/671212" target="_blank">📅 02:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671211">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
فاکس نیوز: ردیاب‌های داده‌های کشتیرانی نشان می‌دهند که روز دوشنبه تنها ۱۰ شناور از تنگه هرمز عبور کردند؛ کمتر از ۱۰ درصد میزان معمول عبور و مرور از این آبراه حیاتی. وقتی می‌گویید تنگه باز است، منظورتان چیست؟
🔹
خوک ها : «اگر مردم بخواهند از آن عبور کنند،…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/671211" target="_blank">📅 01:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671210">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار از حوالی حاجی‌آباد هرمزگان   #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/671210" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671209">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شد
🔹
بررسی‌های میدانی نشان می‌دهد که لحظاتی پیش پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شده است. تاکنون اظهار نظر رسمی در این زمینه صورت نگرفته است./ مهر  #اخبار_بوشهر در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/671209" target="_blank">📅 01:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671208">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
فاکس نیوز: آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
🔹
ادعای خوک نجس: «نه. گاهی اوقات به عملیات زمینی نیاز است.» #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/671208" target="_blank">📅 01:54 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671207">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
فاکس نیوز: آیا همچنان قصد دارید جزیره خارک را تصرف کنید؟
🔹
ادعای خوک هار: «نمی‌توانم این را به شما بگویم، چون اگر بگویم، کار احمقانه‌ای خواهد بود.» #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/671207" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671206">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
اراجیف تکراری شیطان زرد: اگر ایران به میز مذاکره برنگردد، تمام پل‌هایشان را هدف قرار می‌دهیم
🔹
امشب، فردا و پس‌فردا به ایران حمله سختی خواهیم کرد و در مرحله آخر نیروگاه‌ها و پل‌ها را هدف قرار خواهیم داد. #Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/671206" target="_blank">📅 01:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671205">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d78523d3.mp4?token=Qs8tNw55TIW5BlAg-JQshn3IqFWupotly1aWX1aVKiZY16u5jpE-CW4c8oVqbX6h2B2iK3vf-w4pNjqtA9jfceQltYu_rbi8XhnC3069uL8ClvI-rXmlavSfwY4jB8K1zJuuvMG_WXltTntJxiw3_3p2nby-HS4F2Tzu_GRCsz5ZbNOHLuIVDpHoODqzUiG5f6OL9PoOuc0LevMt1RmDQSlW_ASSn0S-iDepf4vhDPaKnOfmXC4BhLUbFeu041QeazJ5CbuaPkfVDF9gG3ZIGj1aWrcaQXZ1b8lzbNZ7KDWEs_UmVUF0qti2FBUsrhkGD7Gn15Uc1dC53H3RYoV9Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d78523d3.mp4?token=Qs8tNw55TIW5BlAg-JQshn3IqFWupotly1aWX1aVKiZY16u5jpE-CW4c8oVqbX6h2B2iK3vf-w4pNjqtA9jfceQltYu_rbi8XhnC3069uL8ClvI-rXmlavSfwY4jB8K1zJuuvMG_WXltTntJxiw3_3p2nby-HS4F2Tzu_GRCsz5ZbNOHLuIVDpHoODqzUiG5f6OL9PoOuc0LevMt1RmDQSlW_ASSn0S-iDepf4vhDPaKnOfmXC4BhLUbFeu041QeazJ5CbuaPkfVDF9gG3ZIGj1aWrcaQXZ1b8lzbNZ7KDWEs_UmVUF0qti2FBUsrhkGD7Gn15Uc1dC53H3RYoV9Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد به فاکس نیوز: حملات به ایران تا زمانی که من بگویم دیگر کافی است، ادامه خواهد داشت/ ضربات بسیار سختی به ایران وارد خواهد شد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/671205" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671204">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
شیطان زرد به فاکس نیوز: حملات به ایران تا زمانی که من بگویم دیگر کافی است، ادامه خواهد داشت/ ضربات بسیار سختی به ایران وارد خواهد شد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/671204" target="_blank">📅 01:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671203">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار از حوالی حاجی‌آباد هرمزگان
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/671203" target="_blank">📅 01:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671202">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
ادعای آکسیوس درباره درخواست ترامپ از نتانیاهو
🔹
وبگاه «آکسیوس» شامگاه سه‌شنبه به نقل از منابع بی‌نام آمریکایی و صهیونیستی ادعا کرد که رئیس جمهور آمریکا از نخست‌وزیر رژیم صهیونیستی خواسته که نظامیان خود را از خاک لبنان و سوریه خارج کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/671202" target="_blank">📅 01:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671201">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
درگیری و تبادل آتش در تنگه هرمز
استانداری هرمزگان:
🔹
صداهایی که هر از چندگاهی در بندرعباس، شهرستان‌های ساحلی و جزایر خلیج‌فارس شنیده می‌شود مرتبط با درگیری در تنگه هرمز است‌. در حال حاضر درگیری در دریا برقرار است و تبادل آتش وجود دارد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/akhbarefori/671201" target="_blank">📅 01:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671200">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a8cd6015.mp4?token=OWsKXJs6suQc-VLsT4ZSyplSYSbMa6YmnG0sS4uOOiyO3nMhZsK5KCJ1s5MvYaOm3vbFbR85EVEbui4JotD81HXKLR0JHRQHtdvkp_EQRGSzb6pirwoAaWtM-tpURM8PLsYKnFOUv3jZTAeWB9U8UGOzT83ekcYwybUDqFoZqQ8f64kYfTZQUkzNnjhwJW3yDAFh85rO3lxeHrduHXyo6KIoi44gdvTSI9PaOKYB5MbIaMz9l4HOxP6XOc99_oSgE0iIowQJUmVniPa5zs0shOg_9dt09HNBOML9OsJxkAv4snoqmBs6yjYCbY4nVsv5qUwhMwMeG6iwOlH-y_1uLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a8cd6015.mp4?token=OWsKXJs6suQc-VLsT4ZSyplSYSbMa6YmnG0sS4uOOiyO3nMhZsK5KCJ1s5MvYaOm3vbFbR85EVEbui4JotD81HXKLR0JHRQHtdvkp_EQRGSzb6pirwoAaWtM-tpURM8PLsYKnFOUv3jZTAeWB9U8UGOzT83ekcYwybUDqFoZqQ8f64kYfTZQUkzNnjhwJW3yDAFh85rO3lxeHrduHXyo6KIoi44gdvTSI9PaOKYB5MbIaMz9l4HOxP6XOc99_oSgE0iIowQJUmVniPa5zs0shOg_9dt09HNBOML9OsJxkAv4snoqmBs6yjYCbY4nVsv5qUwhMwMeG6iwOlH-y_1uLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ناوبان جانباز کنارک: موشک دشمن را دیدیم اما لحظه‌ای عقب نرفتیم
🔹
ناوبان جانباز تهاجم آمریکا به کنارک، در روایت خود از دقایق پیش از اصابت موشک تا آخرین لحظه مأموریت می‌گوید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/671200" target="_blank">📅 01:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671199">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
استاندار هرمزگان برخورد چندین پرتابه به بخش‌های شرقی شهر بندرعباس را رسماً تایید کرده است
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/671199" target="_blank">📅 01:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671198">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
شنیده شدن صدای انفجارهایی در پهنه دریایی شرق هرمزگان و سیریک
🔹
بامداد چهارشنبه صدای چندین انفجار از مسافتی دور دست در شهرستان سیریک شنیده شده است.
🔹
به نظر می‌رسد صدای انفجارها مربوط به تبادل آتش و وقوع درگیری‌هایی در پهنه آبی خلیج فارس و دریای عمان و همچنین تنگه هرمز است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/671198" target="_blank">📅 01:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671197">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
معاون استانداری کهگیلویه و بویراحمد: هیچ‌گونه صدای انفجار یا فعالیت پدافندی در شهر یاسوج رخ نداده است
/ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/671197" target="_blank">📅 01:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671196">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b85d1a2c.mp4?token=jvLQedzk8IYRy5wyJLSgjs7k_hmFH6IVbFV7MBa9bXFtODIpHYDL1P-QknszPex5EGEs7gjIKzb0TTrxGXAq215B3aEOjo43USLdP4XZNdtFoQnSeohhEyWM0rOuJHESvY9Vzyc_V3q7uApLiUUx50wbhawe25P6jgcQ55RaPq_eTXBCVa_nEPxM19_-JMpP4qCpLp47KvGIQGOjtPzR-ya-MpMALqIM40P13_g34w7LPNCPNaFZKQaChdUE7AfaBy3As22_BPJVcnxk4Yol9cCNP73UPMo4EVLipmehjKtyoF3BuiKyXc3Pg8dQils8ppjJ_ItkHZAAI6Gw-j32UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b85d1a2c.mp4?token=jvLQedzk8IYRy5wyJLSgjs7k_hmFH6IVbFV7MBa9bXFtODIpHYDL1P-QknszPex5EGEs7gjIKzb0TTrxGXAq215B3aEOjo43USLdP4XZNdtFoQnSeohhEyWM0rOuJHESvY9Vzyc_V3q7uApLiUUx50wbhawe25P6jgcQ55RaPq_eTXBCVa_nEPxM19_-JMpP4qCpLp47KvGIQGOjtPzR-ya-MpMALqIM40P13_g34w7LPNCPNaFZKQaChdUE7AfaBy3As22_BPJVcnxk4Yol9cCNP73UPMo4EVLipmehjKtyoF3BuiKyXc3Pg8dQils8ppjJ_ItkHZAAI6Gw-j32UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پایگاه‌های آمریکا در منطقه آماج هدف حملات پهپادی ارتش
روابط عمومی ارتش:
🔹
در مرحله هفتم عملیات صاعقه و در ادامه حملات کوبنده پهپادی ارتش جمهوری اسلامی ایران علیه پایگاه‌های آمریکا در منطقه، ساعتی قبل، محل استقرار جنگنده های اف ۱۸، ساختمان اسکان و سوله بزرگ تجهیزات ارتش تروریستی آمریکا در پایگاه الازرق اردن، هدف حملات پهپادهای انهدامی قرار گرفت.
🔹
ارتش جمهوری اسلامی ایران، تاکنون ۶ مرحله عملیات پهپادی علیه پایگاه‌ها و مراکز ارتش تروریستی آمریکا در منطقه انجام داده و این عملیات تا رسیدن به پیروزی نهایی استمرار خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/akhbarefori/671196" target="_blank">📅 01:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671195">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dko_dgPE0uOaa_0OCNUSzNCRpoN_v5_RJj52KMMfc0qa6LmRCKriU82HoFEUZesGnEOlSY9lEJ35p28ywVK8gayMqTFMXZI6vFdIGsltR-1lrlS1DH7jsN3EqDYQZp4-lwsTwVbjfFFbfkuuLv5szagdFWEajU1DEKQsYnMlbuKuqyWLwZgNIk2gSlq0JzOy1qdPxRBXinwTohvPLO5tCzv1FpF-tE4JZ1SCkPXY-v7J1n6LOz9ggzXvq8oJ-6bGVXfl4vypd5vkIIgwwElzkXV49Bc1Vq2LM2wxf3UDAg7eKJdwcpIeVBG8dCmJEclioEj-PWPHZbRKN940PY58Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پوستر فیفا به بهانه صعود اسپانیا به فینال جام جهانی ٢٠٢۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/671195" target="_blank">📅 00:58 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671194">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
صدای انفجار در بمپور و چابهار
🔹
دقایقی پیش مردم در بمپور و چابهار صدای چند انفجار شنیدند. هنوز محل دقیق این انفجارها مشخص نیست و مسئولان استان در این خصوص اظهارنظر نکرده‌اند. اخبار تکمیلی متعاقبا اعلام می‌شود.  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/akhbarefori/671194" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671193">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
صدای یک انفجار دیگر در بندرعباس شنیده شد
🔹
چند دقیقه قبل نقطه‌ای دیگر در بندرعباس مورد اصابت قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/671193" target="_blank">📅 00:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671192">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a8203838b.mp4?token=nYlS7y2O1M8dZ1qFFrJrDah5l_lHZHmMrlseBmcbzCMhglEQ_lIFZ23IAzgqoWVOo5m5rcrtjQ4HblWJSdXE_f8jDPv21WL7DfGkvE2oALjRe9NRopbxIUD8pRJTzqp6CGLEQ0x5hEe1ORejzo_HOzRrHdqp-nTktvIIYneWPk_KKsrhXwuUgiflK1-xGqN9ceEhm72O62X60CrD0jvfAForxI-Gd70wAp239IKI0eiXiXjrejvTwJlZjlPPBEiixLSwE5wFJXlYUf_immOhmJ8QpLyWYgbK5RygCgZ1XwSESH-SCz-JEHpCq5iwaQKpYMtsSfmLcsFtFVH6RrV67w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a8203838b.mp4?token=nYlS7y2O1M8dZ1qFFrJrDah5l_lHZHmMrlseBmcbzCMhglEQ_lIFZ23IAzgqoWVOo5m5rcrtjQ4HblWJSdXE_f8jDPv21WL7DfGkvE2oALjRe9NRopbxIUD8pRJTzqp6CGLEQ0x5hEe1ORejzo_HOzRrHdqp-nTktvIIYneWPk_KKsrhXwuUgiflK1-xGqN9ceEhm72O62X60CrD0jvfAForxI-Gd70wAp239IKI0eiXiXjrejvTwJlZjlPPBEiixLSwE5wFJXlYUf_immOhmJ8QpLyWYgbK5RygCgZ1XwSESH-SCz-JEHpCq5iwaQKpYMtsSfmLcsFtFVH6RrV67w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار طلایی‌نیک: خون‌خواهی رهبر شهید به فراموشی سپرده نخواهد شد
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/671192" target="_blank">📅 00:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671191">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
ایرنا: شنیده شدن صدای انفجار در جزیره هنگام
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/671191" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671190">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شد
🔹
بررسی‌های میدانی نشان می‌دهد که لحظاتی پیش پدافند هوایی اطراف نیروگاه اتمی بوشهر فعال شده است. تاکنون اظهار نظر رسمی در این زمینه صورت نگرفته است./ مهر
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/671190" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671189">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
اصابت پرتابه‌های دشمن آمریکایی به نقاطی در استان هرمزگان
🔹
اصابت پرتابه دشمن آمریکایی در قشم: در ساعت ۱۲:۱۰ نقطه ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
🔹
اصابت پرتابه دشمن آمریکایی در بندرعباس: در ساعت ۱۲:۰۵ نقطه‌ای در بندرعباس مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
🔹
اصابت پرتابه دشمن آمریکایی در هنگام: در ساعت ۲۴ درست در نیمه‌شب، نقطه‌ای در جزیره هنگام مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیل پس از ارزیابی‌های اولیه متعاقباً اعلام خواهد شد.
🔹
بنا بر اعلام استانداری هرمزگان، در حملات جدید آمریکا به برخی نقاط استان هرمزگان هیچ مصدوم غیر‌نظامی یا خسارت به زیر‌ساخت‌های مسکونی و تجاری گزارش نشده است.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/akhbarefori/671189" target="_blank">📅 00:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671188">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
خروج نظامیان آمریکایی از عراق تا پایان ماه سپتامبر
🔹
«پیت هگزث» وزیر جنگ آمریکا شامگاه سه‌شنبه در دیدار با «علی الزیدی» نخست‌وزیر عراق گفت که تا تاریخ ۳۰ سپتامبر ۲۰۲۶، تمام نظامیان آمریکایی از عراق خارج خواهند شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/671188" target="_blank">📅 00:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671187">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
صدای انفجار در بمپور و چابهار
🔹
دقایقی پیش مردم در بمپور و چابهار صدای چند انفجار شنیدند. هنوز محل دقیق این انفجارها مشخص نیست و مسئولان استان در این خصوص اظهارنظر نکرده‌اند. اخبار تکمیلی متعاقبا اعلام می‌شود.
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/671187" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671186">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
شبکه کان: نتانیاهو، قصد دارد در روزهای آینده به ایالات متحده سفر کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/akhbarefori/671186" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671185">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iz-pxZ8-hlstEExd-szart5slYTHHzKPoUaXthJts8NermZwYiyrpXA_4c7-yjy2WGWxTORkxowJ5UoUEpBBBsZrGOfABFAXR2iq_lRg5IHke9zZFzfqlE3SEphbxvcj2Ds-9mNugg_MwG5RLz6zELVryk0mP5BEOthSnYlKMy399CgmEo4RV6F5N3zx7HHDKE-LmTRGQBvw8FsHhJ947cc_DN-JjehvJ2ow84U_U8jPeqARlJPbQR5LySLKHsEgouWFMfEwu4m4hbAfKKKQyAGBc46TVIe0VuRXMDmbpj-B5ObtFzowiziT4y7XyLHQm0JysvLKoN9UIhnVgLZBBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل دوم اسپانیا به فرانسه توسط پدرو پورو
🇪🇸
2️⃣
🏆
0️⃣
🇫🇷
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/671185" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671184">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmVkNU-l47LjmLejp5kJQTSC4KuvX5icGs_VDIAfp6AgwqUVeHwuPeX_wyqA6X7_H7pk5FswFnjMwyb-dMp0leDb_pd5lEuBKBVyvcuNP5c2gHJG2xhpMve6yWI_yekSRZIKzXuTOwwhDsdEnau3juHfuzDfD_JXRYe97QlpsfPTTe8gPWH1QGZhhttU_yhXq1lNIzcKSbiN6SHGLagXXij8s-3DxH03pMHjFXsfk_3t0UFeWgG4ADxwoNKXZvtUBZmMoNhY_AEgxV7rdVvZIXG_Dx7wFEStIDpgiAep6TIw9fI_7vKAG0OLukPKmXcZi17PxV6ZnoC4pP5FrDOQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: حمله به پست سرمحیط‌بانی در استان هرمزگان، جدیدترین نمونه از جنایت جنگی آمريکا علیه کیان ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/671184" target="_blank">📅 00:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671183">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ee44b24a.mp4?token=EM-T94YlzqA7ylzY8Lcw1-3K_R-itu9uY0KKafRxJgecWadskj3Oc8p0sp8xdUuh8g4FOLV79d29VGO_239_tAeUl29LRb7xBZ3WC291PW2R1j12fDfLhzeGDT19ED6y_YSdspNRK2J45W6RVXmcJKZu7k4ndE0K_W7fRWBnGm0u-nezazhoVNg06A5YE5UY4LyhVAhzDXOYpf0UeoCsDLbrrkneRfUDIv2r4HCV6lvHKV7vZvGcuTaOOt7gtgEw4RqXhVsNASqX_9nbuhPY4EdoAmoG-pkFyrtWVCAsd6p9LsGL9QizGJoOtWtmIz0b6bw0k-CJ4uei_UlgeMuGQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ee44b24a.mp4?token=EM-T94YlzqA7ylzY8Lcw1-3K_R-itu9uY0KKafRxJgecWadskj3Oc8p0sp8xdUuh8g4FOLV79d29VGO_239_tAeUl29LRb7xBZ3WC291PW2R1j12fDfLhzeGDT19ED6y_YSdspNRK2J45W6RVXmcJKZu7k4ndE0K_W7fRWBnGm0u-nezazhoVNg06A5YE5UY4LyhVAhzDXOYpf0UeoCsDLbrrkneRfUDIv2r4HCV6lvHKV7vZvGcuTaOOt7gtgEw4RqXhVsNASqX_9nbuhPY4EdoAmoG-pkFyrtWVCAsd6p9LsGL9QizGJoOtWtmIz0b6bw0k-CJ4uei_UlgeMuGQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عمو پورنگ وقتی اینارو گفت نمی‌دونست مادرش این برنامه رو هیچوقت نمیبینه...
❤️‍🩹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/671183" target="_blank">📅 00:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671182">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
تکذیب شایعات درباره وقوع انفجار در شهرهای استان خوزستان
🔹
در پی انتشار برخی اخبار و شایعات در فضای مجازی، اعلام می‌شود به‌جز چند انفجار در اهواز که پیش‌تر گزارش آن منتشر شده است، تاکنون هیچ گزارش رسمی مبنی بر وقوع انفجار در سایر شهرهای استان خوزستان وجود ندارد و این ادعاها تکذیب می‌شود./ ایرنا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/671182" target="_blank">📅 00:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671181">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ستاد استهلال دفتر مقام معظم رهبری: چهارشنبه آخرین روز محرم الاحرام و پنجشنبه ۲۵ تیرماه  آغاز ماه صفر ۱۴۴۸ ﻫ‌.ق خواهد بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/671181" target="_blank">📅 00:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671180">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
اصابت پرتابه دشمن آمریکایی در قشم
🔹
دقیقه ۱۰ بامداد چهارشنبه نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیل پس از ارزیابی‌های اولیه متعاقبا اعلام خواهد شد./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/akhbarefori/671180" target="_blank">📅 00:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671179">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0099aa6ab7.mp4?token=r2roTCG1Mt-J6-YZ0agZgr_O4lxWHwc-sPX_7COW8wzfAnvBgs99qCMi1PcI6A0p5stUobGE0nKM_IeJSKulMumY0eqrn1eTlv7VCbh7i5cR62F_EvSm6XW_ssGMox6i5R97lAkaDBqRnu_XXQHCuwwEuiOIqLmWZL3LBMIEsI6UVjNpbHUQ_a4hM0pBA_8YmxQM8ifB1IYaGaALQ-GjCKJzFtHJmr-X1VphKFeFwhZMAPNFtBL3HiccH592A1XfOhd_bENlgy-7FXxRS2mhsPlMcIWcOvnib2ltp94aH9Dv8od07fRjySFTGXhLwb3gB9ZNq8WDw2ZJjWFRKmh08b1FxYfoHUOcA3zJYwuxLRB7W2OoBOkOpkNFNMUDd7HKvb3bHRv9zW1aXPdwvkxxqPSrqspWLmjOtVTuz0nalAIOV4Dw43QctTLi-tETXdUS_ejbswr1YtXolbZWZh6lKlNAtJ5XOl57hMNcGTjzqT_hhFsPtQI0PLiN3fgmIT5ri_cs0ctWVI88p-eLLSn6LfFYsDQiq57-ODznjxvGBzTHkXteMHhxXm04_fACiswHvbldsuC55VUobWoKDIHAE2dr2-gDKO9MwhGQMPOvAYC3aKNCt5u6W3NiBSkdzEW3vLcWL0fz24G4HwSXYDKMrGWch42BmiQivPAGxOX8EeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0099aa6ab7.mp4?token=r2roTCG1Mt-J6-YZ0agZgr_O4lxWHwc-sPX_7COW8wzfAnvBgs99qCMi1PcI6A0p5stUobGE0nKM_IeJSKulMumY0eqrn1eTlv7VCbh7i5cR62F_EvSm6XW_ssGMox6i5R97lAkaDBqRnu_XXQHCuwwEuiOIqLmWZL3LBMIEsI6UVjNpbHUQ_a4hM0pBA_8YmxQM8ifB1IYaGaALQ-GjCKJzFtHJmr-X1VphKFeFwhZMAPNFtBL3HiccH592A1XfOhd_bENlgy-7FXxRS2mhsPlMcIWcOvnib2ltp94aH9Dv8od07fRjySFTGXhLwb3gB9ZNq8WDw2ZJjWFRKmh08b1FxYfoHUOcA3zJYwuxLRB7W2OoBOkOpkNFNMUDd7HKvb3bHRv9zW1aXPdwvkxxqPSrqspWLmjOtVTuz0nalAIOV4Dw43QctTLi-tETXdUS_ejbswr1YtXolbZWZh6lKlNAtJ5XOl57hMNcGTjzqT_hhFsPtQI0PLiN3fgmIT5ri_cs0ctWVI88p-eLLSn6LfFYsDQiq57-ODznjxvGBzTHkXteMHhxXm04_fACiswHvbldsuC55VUobWoKDIHAE2dr2-gDKO9MwhGQMPOvAYC3aKNCt5u6W3NiBSkdzEW3vLcWL0fz24G4HwSXYDKMrGWch42BmiQivPAGxOX8EeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
راننده‌ای که کامیونش را وقف برپایی موکب رهبر شهید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/671179" target="_blank">📅 00:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671178">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
غریب‌آبادی، معاون وزارت خارجه: دیگر چیزی تحت عنوان تفاهم‌نامه اسلام‌آباد وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/671178" target="_blank">📅 00:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671177">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه خیریه مهرمبین</strong></div>
<div class="tg-text">🔶
فراخوان کمک برای خرید سمعک جوان معلول
🔸
بیمار نیازمند حمایت جوانی ۲۰ساله است کم شنوا از خانواده نیازمند واهل یک روستای محروم منتظر مهربانی شما عزیزان می باشد
🔸
هزینه خرید سمعک ۱۰۰ میلیون  میباشد امیدوارم با کمک شما عزیزان شنوایی وصدای زندگی به این جوان هدیه دهیم‌.
❤️
هر کمک شما، امیدی تازه است.لطفا این پیام را برای دوستانتان ارسال نمایید.
شماره کارت خیریه مهر مبین:
6063737004808968
شماره شبای مهرمبین:
IR820600260201108691003001
پرداخت آنلاین و اطلاعات بیشتر:
https://mehremobin.org/help/
📢
گزارش کمک‌ها را در تنها در کانال تلگرام خیریه ببینید:
💖
@mehremobinn</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/671177" target="_blank">📅 00:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-671176">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMZ59aXoY8gVJeDou6pJUvqIwr0WEq62r5hGQWgG1nTXTvmhVetsjlWv8nq-NOZR873JZkfRbmlkE10v4zndPLtIWd3_7xhggmGBg4_ahhlQB61VQwccttB82R3EusuRAQIlEE1K6jCvaigZpl148Hi-yeR7F3QoqXdWh-Q3cNdXiioIYPBOfqaMtTUcC8JvVr30HejJjztzE7iTNdCqdSPP4wmsvOq9FtLXU-_WkZae4fwgTYddVhAfztnKAxNIq7BxJagcWxyim70Vb-2LcNgs3on2Sw0t7ao9QXvo1o77Yfzqml-mZuqQW2Jxbc-TFMErHZOUCRAffmniB5OcNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/671176" target="_blank">📅 00:00 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
