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
<img src="https://cdn4.telesco.pe/file/vq9EcK05IhezTAKDrTocdUFZPuqYFQ6U_t4hG4UvIN_UxhTCntuylm22B-pXCLUxTOI8T36K2uzz0VrFAgwj5hGRlA0zDjYBWDqhjxmvxEdEaPKNT47PQIq7v2xVdN1G8Yy-xUxSAz44yZ9nUkqyK-Oe6n9m79Yt9k2Ga-TEnvxPziRiyNg_1p8rDvQ10JFiz7qGOxOwPqwNYoYm8yyelvDVcVTOEV8gnYhyLHBlHgNP-Zy-hYb395FsMrQeGtyK8InAcRxjFYrVR9bSfyIqCx0Pp9mgGPBxzblElmkuuUUXt3hcPWdhRqYxrKDVk1ynXPZ8x_snd6XFN84zPvGS8w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 17:15:48</div>
<hr>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=iXkZIesf_0px6glUvetWH4uKA7kXKNzRDwLGoNPJOwWcQcnrh0vzahwmzPz8VyrZO4W2Q78p5fp4cwI93e5uUfKhzc9NPj5AlaP-d-ztU1UsgwYHx27muJc0oBYfRsBtGE0dlm6K4uV0xS92WfWOCHy9CzYetIQl3ATjkrp5KLoZRkKs2WQa9qxAmiyoMU62NMKk0MUc5yITYHy87tfGyPUjWAv_6reI63QgTorp7oUBB5WQfa9NyayaRFWMWi570U2Vk11EAPpi9TuZFBeYHFFJw61Gt49l-RyZHvM6gYySeAMqgIdyuvGugCsPyjFC3xUNftKwPDsZV6_2uPXrOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=iXkZIesf_0px6glUvetWH4uKA7kXKNzRDwLGoNPJOwWcQcnrh0vzahwmzPz8VyrZO4W2Q78p5fp4cwI93e5uUfKhzc9NPj5AlaP-d-ztU1UsgwYHx27muJc0oBYfRsBtGE0dlm6K4uV0xS92WfWOCHy9CzYetIQl3ATjkrp5KLoZRkKs2WQa9qxAmiyoMU62NMKk0MUc5yITYHy87tfGyPUjWAv_6reI63QgTorp7oUBB5WQfa9NyayaRFWMWi570U2Vk11EAPpi9TuZFBeYHFFJw61Gt49l-RyZHvM6gYySeAMqgIdyuvGugCsPyjFC3xUNftKwPDsZV6_2uPXrOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg-J3o8JERmmNGajH2Urn0CIPz47bgg1m7EPoI5qNRKq379Cr34SUMrQ9iwpzyxDekpUApRifSZ1N28XqIDjz1iw1whDm4pxPOGe6YHoL0Q0IR-uA0eWsEX8IxV9XWMN5UaWjhoVUh_hhz25o8Gp5QmxMQVqLeDaODVY-IoHCH2goYRcc1C8XHHNbiOoIxXNyW7vs-WzRcEWgIreIadwdIC7LQOLHdT1SBPYW1uIxP60HRboDYPRKw3OQ8xICliP7RCMtyzCKuMP18seNfdsc7tV3sN2FQpoh3qW_EPqhs0sz_3RMqUP4WGb7rEeF14OPq0G1ALs7RStzmvr8OeOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1Z3h8Ou9kCNK3me5TupTtqN4aef9PZZOYbb5VKwGCC37HnaqdXewWdzVGh0pkwEKtX2tOPBEEUJT1cplgljjuI1gYwg8hIPNS-l17-HOH8QNmjK4BvEmGHVccZoMkvKXU_L1SyHlf3f6KS_JrsgVOsH9TZGvGFI2gy5dk0zoOzO0JcXa8SLchzZiPBwA8NcRtEzMFnmLxZptodoJdOSBFPZKpuCXrwx4-DG3GDfQQ5ZrUUHQB-p8ZwCF89UOn7Qe-9a0JM_zDxXNkmaV8Tm81xY8eI-Qe_cAi9y-i3CDA-c7w_CT842Jb1hJixgzImHiuPYQOB8Maap5BoFllcZoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=ibX4FAhdrw0M7HK2Rtqkn3kvOVGfbvdWaUlKl856LqWgrMzC4WyjGh2QKYBJporY9qErbzTdP7IW5d0SaRPeO1skkCVOGSq9CciHqTGncDQYtuhiaKjjRF7wKl-6xvce7si3iBcePj8cH53e8S45bVBxn5nlEAzXPpNPe7NToMx0hg81W6u_H-VNhRtWLqACDm20r4vQYwVwgrvY5V42fSi22xHD9YrsHwJkwY_YRGZKP3nhMZgR-oIq3UalnfAmA0sK2KegH2Ujh7_WFml3s5m8vaqA-P9F1FR39KGW3bVqRRD4IKFEwnBdLWTW28pM4X0DWW3MwM-wqX68Q6Fl-G7mR3t5QFznzkUQS7lqjJyKDF9BpS24mWK_CZtGl19gLjnuZlVw4RdR9NqKpp4qpNp1rRuWsSoUwp85YUQ6Ss5wEkJa-Ly3dKbMz5R_AMgFEpfCkotKziLMm1EV9dlEByZwH-NfxusZmSEKqD8z2HqbGgtgKLEdhCu21Xnm51fuVIPQy7RkXz0ZOxDB7hyq5UIgxrcwEV_9NUxaBCwTD1CDP3CjqwGWN6JilyoxB0VaWVMQG-69gaRbJAbHRh47w4YYtyFcYQPcbEkGMjlGaV2gDSKemLuweRJizaA2MzB3JdsG6CjQDKjkQIWiTQsKMo_V6HfEEl18DRHx-HMZ1_I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=ibX4FAhdrw0M7HK2Rtqkn3kvOVGfbvdWaUlKl856LqWgrMzC4WyjGh2QKYBJporY9qErbzTdP7IW5d0SaRPeO1skkCVOGSq9CciHqTGncDQYtuhiaKjjRF7wKl-6xvce7si3iBcePj8cH53e8S45bVBxn5nlEAzXPpNPe7NToMx0hg81W6u_H-VNhRtWLqACDm20r4vQYwVwgrvY5V42fSi22xHD9YrsHwJkwY_YRGZKP3nhMZgR-oIq3UalnfAmA0sK2KegH2Ujh7_WFml3s5m8vaqA-P9F1FR39KGW3bVqRRD4IKFEwnBdLWTW28pM4X0DWW3MwM-wqX68Q6Fl-G7mR3t5QFznzkUQS7lqjJyKDF9BpS24mWK_CZtGl19gLjnuZlVw4RdR9NqKpp4qpNp1rRuWsSoUwp85YUQ6Ss5wEkJa-Ly3dKbMz5R_AMgFEpfCkotKziLMm1EV9dlEByZwH-NfxusZmSEKqD8z2HqbGgtgKLEdhCu21Xnm51fuVIPQy7RkXz0ZOxDB7hyq5UIgxrcwEV_9NUxaBCwTD1CDP3CjqwGWN6JilyoxB0VaWVMQG-69gaRbJAbHRh47w4YYtyFcYQPcbEkGMjlGaV2gDSKemLuweRJizaA2MzB3JdsG6CjQDKjkQIWiTQsKMo_V6HfEEl18DRHx-HMZ1_I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhXcTouct6Pg7yg06yPl0A-5DgcPdeAM1A28gRsPvu-IwB-9v5X3qe1jiApwIBbW-ro_a4CTcRSMmOCbmj6w4vCRCf1ngE15pxEUp2vysYjO5u5EqHPZ9Ty4O7njXvFzbmd6ZEsjvONnTPI8FxQCMsgf0FMqD46wDTjsreLgrUYUreAFKc12I2y6AP_T1Qv4EHkFW1s5sIHOuYZ3KXruoGsKWXglpOid_TSLDCYPVUBMRxKX-tJ7vTQ-b-4z9VCg-FT8yT-Ym8uG8dQ_qi8O-vt9hIXm-BtoQ-gMsoBc64VmjJ4lXWB6fbEk2q2vtItad5UySzKKm2MfV9Zr5AXPLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=N5ifUiGPDCl5saaFBnbi1G_0TDJ6WZqTVKtlc-Uy3FEQBf4yv8o0ll06kF6uFAYeiFHiIlG1OxYCZ2Cab3hV7ZqB3-BKs5MF1HoEfN9d3tLgBc04lwWLc6bNihc5cPqUzmOkbwOvkpwi5SLmM2dc-5LcAseUJVoBL_dAqmw5rIt1CQjhFjYZLr3KA3XXRSlgtBEBOVE9-QGX1ra15kl4_qn96gJVfWjJ9IN7vFU5ix8E3n7yrDQHGpmgbG66vN9vtVSbBX6j8mZjKeyjN7hWdoPsJiHagpEw65NEJv5zfXAcKwshkS9QH-_BFKmOhwtLpTTFux7Vj61jkgwzq2bsYLVQCrVAr6Iu3YIFqzNF6jtM7rSvyBnZD7a1wkCd2Saljmk7HGcZivHcrLJjCWqxdpA4qE8Dfsz96WRb0RepCUXCQ8Vcu6DJ3r5w2vr7h90AdV2oM25Otl5WRNVrqg4I6PR4WfoaWx0cLr-kJqhdySwB2QM6DgfA8a3pFHyEWIKi5HVeRkEWrtG4G6LQIGSO_eM_4RTk8kzfR2uq_HJbpiFZnO-vwuPQCm4rbekCSJfKC_b6QESdXjA60koXLOI07bsvvSWe8-6eZxO-cGfC70exKFLcjrGLummbIjAJ2xZgVvq3r1sYc5Wb6MOHYdCgif8N3HSLC8zGV7WfXDx4PMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=N5ifUiGPDCl5saaFBnbi1G_0TDJ6WZqTVKtlc-Uy3FEQBf4yv8o0ll06kF6uFAYeiFHiIlG1OxYCZ2Cab3hV7ZqB3-BKs5MF1HoEfN9d3tLgBc04lwWLc6bNihc5cPqUzmOkbwOvkpwi5SLmM2dc-5LcAseUJVoBL_dAqmw5rIt1CQjhFjYZLr3KA3XXRSlgtBEBOVE9-QGX1ra15kl4_qn96gJVfWjJ9IN7vFU5ix8E3n7yrDQHGpmgbG66vN9vtVSbBX6j8mZjKeyjN7hWdoPsJiHagpEw65NEJv5zfXAcKwshkS9QH-_BFKmOhwtLpTTFux7Vj61jkgwzq2bsYLVQCrVAr6Iu3YIFqzNF6jtM7rSvyBnZD7a1wkCd2Saljmk7HGcZivHcrLJjCWqxdpA4qE8Dfsz96WRb0RepCUXCQ8Vcu6DJ3r5w2vr7h90AdV2oM25Otl5WRNVrqg4I6PR4WfoaWx0cLr-kJqhdySwB2QM6DgfA8a3pFHyEWIKi5HVeRkEWrtG4G6LQIGSO_eM_4RTk8kzfR2uq_HJbpiFZnO-vwuPQCm4rbekCSJfKC_b6QESdXjA60koXLOI07bsvvSWe8-6eZxO-cGfC70exKFLcjrGLummbIjAJ2xZgVvq3r1sYc5Wb6MOHYdCgif8N3HSLC8zGV7WfXDx4PMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCt7WIrLk9WsA3xTCbmCtVYMf4at1GEaIJWUrO6AW9EehlpTuUZ_OS-ZgIvNLH7pcDiCE5noJ6AxaXaPhMGulo7Rx21QXZfJBTS89omPt0JbTzw6IAB2REBdntuvlvL6p2gzZh8MZfVidoBp59YM2ivec11yKBp30L_Z07kgfuMseKomYfzPnJzMbBKp8Yjg8PEG9KwvZFiq6BkUcOX_PNrEUXTTJT6N_heB89fe0NrrASVHG8e7DifOZqgKdEIxmi5DMJCG3s6TqaADRjFAhfeNBebE4t3CB7xf8ZOnUuP6HQkV70fGMc9EvPmHFSZcs-S-Yt3VIiE1VC8D0vn2Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N2sHqPSbj5b9BCU1zsEcrqxrAKtloocIis0uVnUTlFXj6Sp27iF9qp6isfUZZqlQnEVlPVYWjPzLBPFIvMhEevb8j-n1XReyXtEdWGSBCQfs-_URV_0eOMYMOh9uycmnVXwGb5jFBAC1B2vf64gM71jELP_YLKzIpzrSKSyRC80U2wezd_1JjcqtuDG_34gZAUEJPWOXrrAY1Aebof_30oMmE5DDIkpq7TMyMOFNpxNNUb4MjgWGfvMuV0DETtzJBqnzrHpL9kMabC-DHwPRRxJkTVRJ329RwYqr9yZRd5GMOqPsQDaWdaKf5vGewXHQqx569siLMipIYyh0ELj9qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhp9yHmgt_V0PGzpaRbkY9nAMtYdJ2sQxVbAH22AWdSFI5PAU0wZmnYcb96Bht4p5HZgxbav9dmnEup4aSydmyvJQqKkno3WsZIcmNNoczjJHLMWexOHwBMtwYYIFdU0xk0yK-mYU1GvtR4cMA0lNOJIOjWnzyfWRbIH-jlHw68xXb7kltdWvxCub2J2zQkzdETkshnVTLceO2Vi_qcJjB9iV9QZgN6ML_e4ojUz7_lz9VTuWUJbWIDapDHmGX6qLGuDmVMkOgsKHtlpB_9dywZROBrkJQI_4NoK-HrQkOuWrOqMnXue5Qf4PrEYwkwRU287h4rqxVi7j9ULZ1JsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCN7nMZnEykdlZX6SYFdFkDhsVJqVrCvfsHR9a8Iv53-WIwlq8gUMW2IJOQwaunRm7AMs7VRJv5s-XzFXIqoIHzq_ppL43aKHJaBgDqChqV-RHo_R06Y_LvEt_tfyMSOMIc-mBm0cZR3kWtOtY_413c5PtIbXsbWe3L1StKdaYkTbjlvxX78NaEBm_bG5uCBppDkA92LIlKZSImS4ba605XeGL9cA7OflckvYqK6jZGRK2f7CE5cej7SD_QJRX_LWeaieAAwsQVPn-ESM4zYh08Ig_XTm9BHw3Mnv8cQ-p0suOmUPvNlBFA8titJAavkkfwNd5SPxoDPpEnwm4xSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW4DI4VzcEDGwI7sTI8KFof4rVVq619MEP5mj4xlAjpAxaGggKYzpBmsWkWMvOIsOVcMoI7d8ayakKQdeiPkSDbpX0VsLdGM-hTZ7ivRTCQ56-GlJwbjwihUHrarGMhXPf2AdEAg_YNpv3WdZxXf2Y0fV-a7jboLoTyYe9RXsR7j5eIURNgZAiID7M4pl8A_QIMB1q-zYADrAmwxZwXv3h_bfg5w_Ifbmnl9pEJRuRqAIa-5yut9wyxdJUNj3iSgy6XpuJbHPcX0ap7e9mfWNbnmhfP0_nCnsDkxrWbMYlWDN7D9m4yjv5kmIMWnBcjyEeyAACSXrWjGX6bpuQgiew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_wdaokjfP14MO3O4cQwQty4gRhom9foGXTtCR6620rOxcpCGSFKISXgwJedHERc7R0Ed2kWmV2ejeNzEz6fyX2C4SLp72LQ0nj92x5IRMZ4F6tQRgIT4sA8tHh4s3WuDRfhaV8ZAHTjixQ5Q8k4ET20gHIXJunFtNAvMNh8bRkbrrZXxmpXnCINFGj9DPe9mQZdUqPNZN_FimY067f-JZUdp06XF1GV7hkNZVW8CZRg1t0JQNxWvVhUD9jDObY-9YE5qy3ECmtLFrs66io-0MfZNUfkKMabIKxH2DADnED8nfYpV8hali0iVXUu4jad_hvYdDS5VXlSLgGtDQL7ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s32jaGnHRBqG3tQsxCZhw4MbKtaURpfOZUSKj5yRM1-uts-60kAvvfhbYp6ESHV4213S10Gk3Ri0cBRfSoGfXL-aCiCnEDUZIH9qH4isQpSMbYWMFSCzQlqR31bVwc2iHNnGk06QUn6JNDqzDkKAg5wanDEGTe0-BsNRAKu93t_Vg_2TJgMr1pSJoGj0h4nAOK48vCJ92VNwo-BOtbIa5u1JYkDzm82sykMpjlYFcSXITR-CdOqCc-5iiapCO5JvTGM-kC-nBGIVXzRVjZjhG4mZhVT7x6wy9J8d6FC0yKza63maor-jHS_X0_t6poyTAoSyIXBHY4lOZmf8APwo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUc5AXzvGLOyW3w5M1MEgbJXCSkaTP0Kyx72HCkIzqrqs6z6zINcPhxLUEqTYo_lZFltas0shcBD0VMeB6kdHpWcKKzm1TkNXPDUmI-gr9HK2Th4W8D067vm8tiIS223pRIQo7rjx3U61WDd__szNishmXxKM59u2sVLoOufXGZLVZoWUe_LhwagK5AZWdHhlRGV15GC6BdUriW9FQebX3TVfKtiF_2Shm0t0Bi8T7F1V0fUk5Bs-Ymtt9uqCY7-4POcz1GYmUO6lfMiPIPmtA619UGKSajgxVpGZwzNAjqRdxJ8O33HLZOE7720pRTJOktVq1yDhlwofOfchDjp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAgdWzYmDCHqV7lESJqYmYdzqZspsgzQrVulXpsJBWXOxpsWOOGgp1gqg6_eY4kH-F1axDuIZXZYMSfOF8ujx8nlAckSLwoMUp2UM9mNOmaQd6C3MDFCfiTqafDuuDBhvU1LD5t4ZaTuTY8kfDYXPn38gMvRdIHCA49OR3tg9wgLPRigJHnuCfoyiJIeJAwdjw_GVt8gAnoUilTOWgeXnimFBwpH6uPOnxzyPW_q8mfxpeSbPNYHAmAbHzhMbY83vf4lEkdAUwx0YCdX-bOEg14FJ9PN098BQPugrB-qZiTv3oJswuoza484kKORJcVrcybSQb18d-x6mCKNzyPl8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYoV_O99lnWooKx-nYegGmfdXtZlBDp8u9R8mnSGgivlwW8YfEIiuYDkicvc9CE0gKnzVECf4GX77jS3oL3S51og4P3bEsHHt3zXqx6z3Vu7Q_DXj-eamwCSb-KzFukmHbeGu9PVl5nDtxQkumjcM2kzEugrZZXEv_QpVohMPPht9zmgUpHChHo8uo1_M8QfZMDm2G1k4hoBhoMlShBK6115ETDxMlHTx6RHocYDci4LFurPUEb2NzwnxsGJnwykZAoDQ4jBVncRntIYvC7h_d0atNseWjro3CGxx7oHEJk056U_mFEjcAwBLT3RfP3N0qmnlPQ2PHwM2fBbpa-RAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amMOmpwkFHuiCom9VO4CCTqdxwW6w6LPstjVrGauznyp5xQ-ZYv2fmJoLr47DCZ5mYoIF0tGqeQ2wleOflyr2yUE_n8DzhO9KvBSEik9aBcHAvtT5-2WobxiePpESozFFX0o5oBFpjCQs3Liw2g8Mf5kC52xQQNINJngjWJCLzktNLvIMWpIr3YqYLz6Zi0ggaK77_3q8HUaP-v2Zh5taHd5SmND9rNoJ8LYU7QzNJ9ZoHnsVWMpAX9wggJe78xb9DDDk8jCLrGdaPlqZxZivHFNCaHajf3zMExfbRHK8sRgSLDQRrnv_tPn1cRH0X85tWFa_fIuzvOSeHPJ5L51wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HixJNmfAkD-PpV6uxhuOgMr7N9UHNwRsV-xbGNGLMM_7q8jx9OqGY2KJYi--s4JZpWhQjTFb2WFJxTgdFLlFKIjwqzB5_1jgMTf-SaQ35rwo9xuFZhs6DpHJuCyuUA9KsiSHO3Tt_4tRofCxaFMmP-g0PPsRZmX1AXXhViTQzRxflH6rpWKa5bXghP3TG7qv_pxDnqXHDZ04qHKstgfwqjPukbaM5JdLLiLEUmm5izVWBjQcC5EIfh1yGVjyt63AxJ7Oly_lLSllKxTor8QUkAOpUQvzPm4E6d7vFWBVywc7qO6nAXOtmzpqn8z5I7tt6DYwi_w5IdNsuDuQAY_l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyPCXLaGoASz9-2tniLnePiJKUVc4oL8SRDamLnUTG6mz2hqxjWw2OgGHYWqIhrviSstyYr-rfQZ0ULPy4YOsicwJaCD0O0Xb7ER9dvglXp1_1pKgcAogpE0xFyU0Ho6ToXOocOgq152ASvWY5LNgyXTx3bDP5sLcMF4BsY8XNcZyexCNUZWi7rZEWYgPgp00i1kwfHXKN-JCNexPJ2PsKJcmRpTgcZKAqynhyR_jSyRKMuvEVZMYGaRkK0T4O1s8Txvi7wZNwpLhlT-8ufpU-tmw54sCcmCKkVjJ71rBorko9FxLmAUrf6GNFtemR7HMBj4ugA_621f9N1Tms7X4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3uxBSRXtc4o2_wRfpETD2QVDB2rU0pQdjS0mHkcrVvgXvccOn_hJMFl48UuPujsI7WsMFy-h45eGhlnsGE1lshETw4vJbx4lHKIyY38GVKt2L1kfuynoiWxnx8YLi80PyGuZcTpuoY98-3TAXsJyFSeRXoQfKw1OVbxMCBTd5U79bXl7L25nPgyRp1nMxblDUiCootqST-vgmzIuVjekoS6tZnLWYKQki-V8Qvtlc-iKJ2EgpDUKs0K0aMMru_cBz8olkiA_TzNbOvAAX43doGAQmzru6xuLuoifD9riS2OLdldHwuFSVYl3vIfFemiaFWfZAUSLxFFFsqgO5edKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFZzxLfVUi4XnRfnLCBRpSEn2D0bGX3-YUYtwFBy8IZYrKKwGHE_8nVBsB03UPwXbFwGrJAYIlKmoqtPwhx85uynYeU3xxVpcxzLDq8XekTC995VJiKZDJmuqd4jMNDhg9UlEJzBXdfhpzkGsuxSQlsbS6xxabN8ydl0s7jlk01b4XDY-RN12_L5nc8zGFVvFrS6_tToI5kZGYE5kD2XsvSvmHoJ9GD7cV_YIitmC6yOtXUTu9JeRaOEQm22y5yQ8HSmsohDY4lEmM0BQ13RqOj3BbhLtaN8ABF_ClGsCKHRlRh9jMInf5fD6Tt45zWH9pmz7owe8mZXYFnsmeNkDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGWqyDz2kjhxtiCgb5R-rPVZxCDn-PUGu7gfbGBhfRYDOIORDzcsFQdjdEanUnuFGy13rrWwcwfHNSwKGLpG5VJEpAKi8fPmuiHgVXWOc3uoGJNxa-_sTueLeMW1CaENsRTU1FsufgPUH_OqbeHdrsxGEt6BcflDl3ZmHzFbrFazhuXhDZUtDlLqJ5JpfYjTQsrQ6aCnHkmGK8IBi542bCywhrJu9ZdjxpauSuT0K-DeEa5yshBKTKp3Z4ZYiNz8vYXSZXhZg3xFwiQ0fQUmw6UYiuEj6Xz-Gn1IbWG7kmPTuS8fOD5SLMeXKeo3Wes1Vc1tSIvAMVZ4lIMxaZdQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6RLxn0TjCefgK5qwkGXBCv6POpaaG3M_lB4h9nOaI4f-A4KX9KLd6X_BcW432CuWYIN3F3JjVA6MCemsR7doLVj115NPA4oYpj3iWnxK8zc4yN0nqklALjBB2n7KUjqppyJQ-z5NKbh6ju2Hldp4EXJ_JsHql2DHJPW_5_HnFl8FSxY8VngT1IsDTF5WAXRNda6tJ7SCNIWX-meZtQOqtTiM3yfOMg_1CtzDWpYYQkdLyv3o01DkxTG3ZiPBmpO5bLLqF-M1WX_pMiaFN01c_I88F2ajUj5SHz41E7z9IP8CyCI1hfJpVCE1a9lMMNyuNAxX3a0BTWZPDcGWFQOJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mbAtIxfbrAp8rIgpCJXpZTiqsaBMqPm_OQqcF7L4o2fBKab2wv2GFQuq4rzbs5dA-6-1pk6OeexU_IFQcth9G4vZ3LMLJp8yTJ4W8X_0H3cxWtV2Rnoa4KlCBhpkYEqTfzLURmTnnB5o9dcd68Xvo984RFB1rF95z_X-cr9L9sQZOWF7BomhRYEAxTi_w4gCohbjr5KWz8DPtNewpFcEh5a_bERv6sQTVPkT9Pg8vfNampyyWpn-t8ePGF0eCuX1gJ3ZaxFN-5w6WW78Ivh7DYxFwdn-6mNUOfsqUwOuKOKCH48anL-5AKTjoDIplR5Gq6z9dBnx_HhKwaVx2-cnoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFZgA94GZm-Ls_oD_65Qgi8fIP8HvINGhZJhwkomuqcBQ2oKMV5DZ5hZyyAz2GCGG4B8b888fq651A3qNWKWlc174zFZDw7wZ2NYImecAZ7Yc98BNY-lernLvyzufjIf0AtysHg7BdI2Wkzk9UNU7psD0qHZml6X1sUwU_rak4Wh4UZJ4K99EUnAv2dZxkLVQX4VHdzX7JQ6R5Bih6guywL0cSKTC3-v6oGmSZ3520g_ZgIWdFvKvIuUhyHcHLBpLT8Eo5zP2-7RJjEcckgZ0vkJ856Hbqjo_iUZqYz52qOKY40ZBufbbKyTUfPrwH51xo5F7sgjTWtxdWsfQSVR7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU79LvQo6ZSN9yiv2FTmKRZtNNCRApYuoXpfvO7qEvYvxkfoCrQq7vpoJky7rg1XPs_FW0t87zf6o_snFrj8Wno2TEV6hufB_CnqwXDjpBtNaP83z1KRpSCSskklONUw0tZYs-dKyvVuulqG1tvxPCaDCeujKsk-EyBONv8nSseodW5kFx3PSq2L1bs_HwgIzMQZH8o5GZNuxva0ILNPu7u4_RTCAF10WVhNhlEIXtogEtdug_NidYqaRwBRrAd7hrnlYlZzF-5Aj0OrOxWNs3Rq4U4efx3eUCsY9ZBxfmTbNlLlSQzx8jqOKpLmMLMHKAhSQKlG4vJUrQL08J2Fqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgqwHDjvRW8GxZm4Z6udOAvvgXhOanxzFdXKPWrFYEBTrlsU0tO_Krp2E4CJJ7DCkw0mvBm78aG7D-FiC88Ob1_u2Ey2Zvz10cwsnzVeN930HVhnu0wXWe351cCH6pJxDGJ33TqEhqK2NlySDEsNSOT3tTgJvrSkBat8FtQEbHEqiv2OBrSyLxnjq_bmMSCHYFgGyTrQgx0-d_SuKWp5LGcpE8PEdzWeRqAGv4_hqIhSWL3lWTkgvvy-u7vO5ySbrXwtqFrZqVtRN2LIZSMMU-3vZwqYUZox4ukOwryv1N6OAIpKWZSiHWl_8uH3gIIXTH4gFkcOs8beVJPH4Imj5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II7l2wJxedLCA1f43pxujgXSXKs8VYOOz3NhhQODLW0Gkk8Rci7xqh4KnEPoQvo85m5PCfW5Kxms2FxYcAGyjJYTCy-A6FHFQVPb07fR0xVIafHoNoLkreshs0T4UhUCsVM2mOQFGxq3_5B7qU8IKWo20HLdOfKgSQ0aLT7dnkOXhCrf96v6B7xvs0M6T4S6GvU6dCludTLkUGIZpPhbFUDXFmLnX_wIf81josYrdcOoZ9KpClhmNvqvgIQJBlEICbbw_R-qDo9_r30mf9syqeWVZ77LD2FE9VAZAxbULsM1iDjdTHQTcnho4exH2EWJhpgEmSjOaXksaawAXbJbsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVHOUi64j5ivD45cllWx79CB_ZHLexvkIqsU707Ef-j3y30WqFBlPSv2VwB5ShUdzyM1PpZ8SLVL9uXKtEq9sgnYO8i73qU4utWRd2xd1C3OXNORinFy2V7SNWo0kaVMY-GhbrvWO3f4LtMszf0vp43-9AzWfMWCcvX7OQQdcveHDmrg-rpZXvE2vzLLjDhaJFDl9B3IB1mEvs8SiztyIyby6K8pLH3B4xLftpSsxPQmmAOrZh5rNrJsHrhbNZ0vVuOK_TraQNNAIvEky7sAEWOZmvRSHuykftSAS3IBNb9JKgVS9KID2n7r8Yp0LcAm_xAwJgGCos2vLKuPvglyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvJ7xSS8k6iG3axnx-DWahapl9bp4g1v--sPO6M6TZJHtwAHlZVMIrkjGgOqjlOpgdpGxu7x4a0unA7ancnAAtMNxz4NgnJYbm8IGCkbBOiPqVUAh_UW-vyR1C9txZiKCrEDOfbIM39qaFqaxtbAD1U-ZIWyFWujG0YFFL24yc80VrS1Rv9HjAY9xyP-kGVFasqHALIdp2fNez6NXPz5jDtnLAyfzSRjcqMB51zjsWbH_w6EU1dV_e29Lcz4kTXn15yy2pwUTdgCxpHSc3mVfoLUDBlpnGRUFLbG7YxblyrHkV5oCQs5LUZWRqJp9WtO2Wj1fdUuBlgVJBkWsTP2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLymW1f63xAdScPbThzPq_PbPGvvz0jp1JuFl13iT2nrWfNQo4NXLW0r0fPu9eL6FwE5aouKmC8oWSPjTPSaFXx3CVjv3NWHFbbvFY6P5NVGpppbNZFhSEeN2_FW8nJaNYxdJHAmDfai3UO56MR1rlq9DaCnn9Lgl-3pnoAbmvN5ecwT6-htuXmtrmyxdrwX4XJdbYngvwnDwMTteHArI2q7ZmLm4GdcFqRVbU2Z_H0-Zj9tpX-GkmAVH6QiYzhYYbeA5FLiyLICtb8-7sU_gPSITMvdYrBvUx6luHFQE2x4sYMQq8RSzCBVetBXE2YI7UnBF9l1GNMZyqJCW6mmfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMOAXwaYj7iS397H4VOSi5Md7CrQgdZD7-hmkmo_MjsWd8CsxSvQgyv6Q0XOfyUnlZ8U1WCLYSAdBweTfLmQIbl7Ce1jou5MDDS2Mm5WZrOJ_EFKyqnghpItF53mAzn9V0LuJ-XySzDicP8zON8yTDcsyZt_CuC_Dwa_GUPYUNBNj57x6qxdAmLj0Nh73VPMHYZIK8RdOJbBYaE7zrevqYcPyR8wAlXih0lamjjB1L8iya12-QEsrhxomv0TvXAi7Wzmx9G-WQ59SEqhpSB-LXGD_FTCJ4858oI58kzqniqDKlJpbd_ocCFArhVsnptOw4j9WUCTQKwkIIhdRcjrKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cx08qm2TsE8B5JTwMw9uJULYQr8tlWvqopO6DPzFrn8lUlal2w6pZesAc_9JVi0Ipl7TnCBl46VA_ltEmJbj1bBG-Q02gl94eHGLOIMc9wBq0P6D5W4KJ8Daq_eu80rqpxQ4D9BXlgBFD9ay34kBcrkk5uoUV-hEbVKy9j7SOEpJlSFJE2fu2tph9LKxDgYvESYdLO56mhoaXkqgX-CO_bV9iDufcRn7FNFbqee-e4bD95UfjZtImjt2dC0h6X1_fG6u5QraYvMzMs_cP0iUUiwPZbKlJJ9gbKe9zGHbFXreInNQdzCJRHe58i8nIITVgLqskTd0vLzDoNBjThsmvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foHY3K5DGUdehwUJTcQkOc5ke7poYPUNf_3ws4ZXWJU_b26btkVlEkJOc74xJH4fZbA4T5pnx23Za22qKwX3UqS-kiyeVU3-fTUU6G5fojkti8TDNj5P2kaWbq5pQeLqLYVVn4n_eBQHQs5GCF2F3IUQipwnc39DwwAmKilMH3_HUvfBxyEDMQ2l025A7G-Fcj7ElFJfCEID7M1rJtIQczuxMh8BfQb-OPmBv4-MqQdWyqP9cnRmQf7CvI_Na3o-TwoxBGX9_gOO_K-NUrUWBsuHvws80WZ-949GFEPEgQhikYd76mgHQUTcwssC4CYcBe_HTv32XyKdF57a_557lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNP-4KWV6h18eTsszkxbBTUV6nj--QwQ3BOrlf1Ha5lM1FnFc9niMD2Vi2vvWtCM8Ez8Yfn-XDvwULaEWpksY83H6HLEVb2nZs-Ll2OXM2O6Wgikciw0rQh7dtrJPoyrggCraq9Rs2MVPkjjIbscciZiGoUn2Bs8GyK4eYQCoBeMOW5C2OjbMkQxRWU_k_MQ3IDX0YWqtCPYVgiUHEjjoqot23o8VSWGp6vE5LjKg34bjeMftf9XLWB4P4vEmY5oVei8tEZxr1B9AD5vBhc4_Y-ioq7zOoGkh4Jqxuo--BQhYRwezIv1rQXP_WEwX7eNpYwrs1YoIYzZ7IhnPlRxJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfY2quNucizQNacm1ERSDNPJNMuBNbB8yRyifxtsMvolGElibkNahzVMPMQoem0HZnHY07ghBG2QJbI_c83ypTJq_HCWEfFXIDF9dgsjTx9mWz5e7HhplRGiwWz7hBuSWpT8G6kZ2c5gc7X3L85ZN5Kbw1oTK_lHQtdPkJOX881qoIB_Fc7QWFAu32HBSlt8EllYg4ySsWPMetwwkJXJV0uO3BkaqTBrXvRiBl8pamdF3jC37-MYHTM9mYWo2TdG3x8XD1klnEAUuFxw23ayB-z_PunWOpKRb57R4IgGYntU-mNrgRUAnVJOuNhCXmstPcTU3-ybAjssH8iD65MtsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfzqh7ZmvS63FfEoSn4CO2vuLc4z29DdBLtFbpQXLstXHxB1k2O4kXNZgrKICkEZKw0fHFCjDlPRoRpnzPAsQ7QPuxmDWVgpl6WbjDmTCxqO9x8C0DfEJ_W59v3sgdXrwYotHE95D-J3COglYH3RpugWL9wPrdMmGwBdldrxvIe9MMNJkXgf7gn3OpoBKj9lGcdWtTPsBTPFEmfO3yDDhpx5GhDsWgXK1TQWj8i_kjQjvg0wP1vYfvayntD1TJiXpZiP3V678boMYQ8IAP_lgJPATbR5I0O8Tq36Cn9uWM0r1UGNQ0EJcZp8kytMoeVuN2Rr2bH7qWvD5_nwe-xE6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCDp7CCaxKpgqnp43fy7m__1wtxnU_5k4c8M7ySZBZEA5r-Y0KAtdsxucHnZfzKnnGnb_ksUZRe98-hnMN17S4Z1sBpESMf4dmo0x_VAAsxXweUeKJYGa9Jz1ukqvG1LM72A53uIbxwUE1lmWObzojQfJeZrZG3XCrZceDkCWAXq9MKxRfZcGWjLlT2FS9roh4NzXA83ZBeqxa2NwsdKatg3ILgWlJU4s4GcdVYJx290MWysomQnzrQg9jVmD6znzhTtqBU2Jc8v2Su2XtaM27XofXe94x_0vijLJGiz6vFTv5H5i-j7MU9kaSBRh2pktRzch-0bk9uAbfFJEmuzaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2ayGjsbq3IYFpbOwPkTWcEXdsUBt9oy-iwTBQMwUo0r2N-cYM8pC5bY5QWIKAJAZrNzz2C-rEZcqcLm1eb7AZZgwCetl-FEnaPPUUlJePPr4h2KprujmPpMcizj9rYoPSg_Oz9jrGZaI5lTqDufRoDrqC6rL5wALKI1apY-U4eCXjQmBnLcaolS4LuJvGsJLqTP9gy60ofiYr8-iHWpeBd_rkag8C3vWYteNFLq3zn0s65u3V5xAY-gg4oGL8E4r7h-w8Y80aTRW7mBSvOdIumYcMydCK0jeqlBmYkLsTgyLmdWbNDC49Ykvz1BzqwV8GEzmehl9iltpHo6qw2YEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKWhV17elD4AuEB-m_Hg45-mVIiiVZcO2_8H4D5RC9Lj1cdbjDfqvounuwJkEqd_bTgm6o-pUF0CoVT7kO4iHCX7MDobN0VUhb1cbCBbBc17n_c_4ht8hHtsJC9YVhYKpNSSPZfAVgXNqWel9k_kHyadELr48K_yqne38Dlhzegc-D-_BDmDDrbgBWyyEqRMSY53ogJdtgUqZHaf55XznCG6Vh_oAFxyz08nEhvzHaewSEE-FdXTTXeIEOvCobJRQf6_V9_GgR48UnI4NKMQn4gKZVtcJBhq2WL6lvLAUkkuyzS2NgI3QoRo6AiuTdSh-ymNOGzvogwRbyxbmQt5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=CVmCkaIgJVk6qcEr6lXzlqdV82BrF2GvDTeX_IaVlq86JMRjsgfy9F376w_z064GnMv7EiXabL352Xmd0RXgYT41xIzeL0bnmG7NRPyVwPI1oLvfhTOQcDICwO7KDvbz9MiY6lpVGrOFkWFX3hOK_OQrmSZW3xeWuaxXIWu12QIaXZxUeJ1_wsd6obBC44JTCybOTPjDPgzva9CC13G6LQ6V_0vxnkBduxojOEaQA5yxUnmL9lWyYfBcse68eD8daYjFnwtmKhIJL2owJOMfVYyGZgVfWiSU8PoPHXlw7UHAMWDG3QE1hfV4Cx5QOxahLCVcEC_d4cpCkvcNjAa8bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=CVmCkaIgJVk6qcEr6lXzlqdV82BrF2GvDTeX_IaVlq86JMRjsgfy9F376w_z064GnMv7EiXabL352Xmd0RXgYT41xIzeL0bnmG7NRPyVwPI1oLvfhTOQcDICwO7KDvbz9MiY6lpVGrOFkWFX3hOK_OQrmSZW3xeWuaxXIWu12QIaXZxUeJ1_wsd6obBC44JTCybOTPjDPgzva9CC13G6LQ6V_0vxnkBduxojOEaQA5yxUnmL9lWyYfBcse68eD8daYjFnwtmKhIJL2owJOMfVYyGZgVfWiSU8PoPHXlw7UHAMWDG3QE1hfV4Cx5QOxahLCVcEC_d4cpCkvcNjAa8bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaD7Z9Z2HMmeLBgsMXeeak1P_JEImPeS_Bd2lVEi2Rw44XitqzCfZfa8eOKjOLtaQenawuFhlT0B9jQ5VyCl1aWLPJ8SIh0vGcuagOKWeC5Rv5HtMe0KgOcZcNPj8zcHow2lIP7bRRJzZ-PhO-VykcSbNnAeu0bB7hwIiHhk50KB612jqBcRgSysWXTNUqt4dfg6grFg_0EKDOQZDCDE0iVrBgegxBOaxqMau9M0GGdc1m-2R7mpsn6G95_YJqK6fOBmEJNQHZrb2Yk9BUvdGl8hax598VzzXa20Pz5RDXWYoj1AfpYhYJ2V1r6ImEPo3eTP1_uWcMvKRKnU15nCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=lFRlmSJtPV7BuzMTkU8_cTkOs4Slhxcq_LMaVlNzEgcglWYo1PQ4vgZXWOPJjapvKvkZRKEpK3uhAHdHuA7dNYsxXfsuL6sgd1QFaOyWybDGzTQaoFs_b_Ed04KT10da--JnmkNaCWsRzfvtWcEo3zOn2b2UNszbMobC8aPVNgYZufJRnW2aBzmEXhBxHFXNgCGswVzj22wSrpvan1JBQefD9toBzhMzBO0--hvplHOxILkI19SDZXSIDaumN8Q9Hoh_e8Cps8VSV9iwvwhdB8yVtOpE7eBsaFfgFrT4-m4w2RGF42zaulCefSoY1dNUirjJs5SCSXr-44KYl3FMNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=lFRlmSJtPV7BuzMTkU8_cTkOs4Slhxcq_LMaVlNzEgcglWYo1PQ4vgZXWOPJjapvKvkZRKEpK3uhAHdHuA7dNYsxXfsuL6sgd1QFaOyWybDGzTQaoFs_b_Ed04KT10da--JnmkNaCWsRzfvtWcEo3zOn2b2UNszbMobC8aPVNgYZufJRnW2aBzmEXhBxHFXNgCGswVzj22wSrpvan1JBQefD9toBzhMzBO0--hvplHOxILkI19SDZXSIDaumN8Q9Hoh_e8Cps8VSV9iwvwhdB8yVtOpE7eBsaFfgFrT4-m4w2RGF42zaulCefSoY1dNUirjJs5SCSXr-44KYl3FMNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUUvGL82LD5eYAREzmQsG2c6zbj4xLLjXWqi4k--Vh5ZTkMaCA8JunOwAavUoLUTEO-aMT1H2B8T5cmAlbu9-R1tCNsE7U0Qhxe5uXwc-_8XUhY5Zs9BWpgFygHu-AtoRbknvCsJA70QAIJ4UbURVMuTkA6-vijXOygbIVI3WIdX6IpIHUEhpXyAKx9AnUq_spK93Z7eIdwXVnoB1Z9MJLDee6ekJnGOSuV_OuBSxTUZn85RJpCvTbT1jfR2xByp-0kJzB36y3efxZCokmSEuNMkq3TuuZrdQYWvs7vXj0KJwaABPGLwgyZGirm8CnRwpNxY_HztgxqRYIP7sOknsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WafTV0buNz98xC3Cb6WNA34Y0t42OSxs_gDbcS9uAwMkybD2oguCZJkER7YzNq2qOhtIaNSycLZNwrsVF36GlCUM-rS8W6kAiHFaNIgRDW_ogf6_KoLks79OULru8cko8xoO6rDgUGaasbsHZQgI7oE3OC8o2wL8Zy9LjAnrQlBwZAf4kN8I3os6serJjEnW6m7jeRZP1cwWHmU2GOfgfX7jS9U_KVBLUqkC48RoB_xVP7M-KUYp-spKMtTkTO9jFWH2NxjnkvXDxzwLdKd-S5ROdqyIf3FC0J_ekmvkHtwqu5osJWTGsxdj1dqymJbGQ1P4Vt2SOmhb-HFd8YhPcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=dnb4eTEaNsxVZz36-r6yFEkIVVwqaMvTvc_tkLH_g3XNkicRbQ6VgNoF-hlaU_pLvDJng42TtvsUSjmuuDtr7SE6VBwTHhvKADEbRhJMSTKIN7Sr-TcuD6A0cbu7VLN0iErd26fne7s6lhU1XQ23SoF6ipDzNQo7OEULxor6EaFq2uxVc9YnNDoP7TpfnaiFeklKi0Cx5Zwt0vWnGdtXllPjLbPoWRD-ZYdpm7XxB_jbFi45H6VotVGrtPOhzovt3EFMBgUMHnP87kbOCwcn77GpetEVPOWs3T_YGnP8SxdcmXTkHJr2B2WXGgvaAdf6hR_7xakk22Tn-zF2W3dM2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=dnb4eTEaNsxVZz36-r6yFEkIVVwqaMvTvc_tkLH_g3XNkicRbQ6VgNoF-hlaU_pLvDJng42TtvsUSjmuuDtr7SE6VBwTHhvKADEbRhJMSTKIN7Sr-TcuD6A0cbu7VLN0iErd26fne7s6lhU1XQ23SoF6ipDzNQo7OEULxor6EaFq2uxVc9YnNDoP7TpfnaiFeklKi0Cx5Zwt0vWnGdtXllPjLbPoWRD-ZYdpm7XxB_jbFi45H6VotVGrtPOhzovt3EFMBgUMHnP87kbOCwcn77GpetEVPOWs3T_YGnP8SxdcmXTkHJr2B2WXGgvaAdf6hR_7xakk22Tn-zF2W3dM2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kM2ayJSPI06d8YAdh3XWEiuIFZnQSwduLU7pYCNlK7W1siilBZuRpbkR96uqDKQBtLh0z-ipDre3Pl_5N80eMO0j98ndqkdXztsWzCQwfEbo4yZiM6QHCcc-uDK-YXKhIKvnfU1QvyHLKcV6rON-BbTC_rppxcOGQfyt0_qtzS22nnxkPi02Z_qIsHTFjJTsHYEtDvWLMNv2kxn92kRnr9C-88SK7103s-LxhjqpOGuMiDYsIC85X0o8PANzq_gXoqf1ejA5YMlM1OJYPPyPMOlZpdHolxrb235REaNUcYxO8mXtTYFSudCHfg4yfmwkfaO6lPzy3Sre5UoDwzXgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DApB4r_eSZkdbbuqOpKdgD4bSP08oWNQmorfQLpaEfexO6SmWL9bUcpMXpavLts4boI0HCCvT3tG_l1Yu9Krs38YABtXWbTq49Q-fzG4fpKvxvvlugXUoDJlIzuFDNxrjbMDVM_T-eEQY1cA8ReH421gFaSNxd28ZwUraWjfTPtf6vGDJHlIP5uZNCXgDyIdjC40vT6qkFGXppb411ehegFgzVnXeswZku4-YGDmZVsF2Drh5zC1YyVqgnFMr808nndo2grtIprQFc7gQGVhebz1RnYAzw_uID-46S_zMScDzp6uBKkb16swInf6dq7aN6Bz-UqV7m_oWyGgfJR3rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxfDacIqUtRVRdpmrxrdVftGxE5mwv0_cTb4-z2Oe48IYeMReFN8fhPutGMZc0eTPN7eKuOTjX8SG4UG1TWvBSTW1uDFS6mn6mNBUoeDiDOiGWyKJlQifrWOSfBVuJ_W5ilHswCcVylWEQC3uHNMxXFO0e2559sqjQWB1tPtPFPrL7KtSPuyOtOS1bNbgyqW4HyFLOEvbLz9DdGvAAiKK-1sayLfJ9NMFG2ffoprw2LDc5tOmtmu7xilzpuUE2dM_ZBAGARjGvdIDIztskie7Zceps7XLb6dv7SmQSEwsnVhMNWXcNb9xyh2AhBhiY3Ild6kwcTtqmgxMhksN0NrYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=NRQQl8bTk7u-CVbUlJvaTEtcdWwWOlyQjFmfXGcDy9yhhx9NVR_QVq3kDtiqHf4-XkwGItVzDiqDyvTxHHWvWCt8hBQ9trm8Jj_07F4SEP5NaiOMmcBKDRnZnCe2R6HmTFRZh-pw4vUeY0bml2Tc8nTRl1UfQUvy7N3n5fGsfbh_oZ1D7lCapDWfwceZp7q9belvSAnmEIaSGwW6MtGEHsW4RAOsohLIXs1HrqnB0pQrzG_Fy9bKxuyWz9K2F-xyxs2vRJzDFeVr63vY-BKXNGxPkUSGwyglGrLhrqIA4ZQjYqBu5jmsWR3gOaffea_XlufyWwxraVwI5t1tq2tjTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=NRQQl8bTk7u-CVbUlJvaTEtcdWwWOlyQjFmfXGcDy9yhhx9NVR_QVq3kDtiqHf4-XkwGItVzDiqDyvTxHHWvWCt8hBQ9trm8Jj_07F4SEP5NaiOMmcBKDRnZnCe2R6HmTFRZh-pw4vUeY0bml2Tc8nTRl1UfQUvy7N3n5fGsfbh_oZ1D7lCapDWfwceZp7q9belvSAnmEIaSGwW6MtGEHsW4RAOsohLIXs1HrqnB0pQrzG_Fy9bKxuyWz9K2F-xyxs2vRJzDFeVr63vY-BKXNGxPkUSGwyglGrLhrqIA4ZQjYqBu5jmsWR3gOaffea_XlufyWwxraVwI5t1tq2tjTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=S4HB059knyuv3dowfW8_89ro2ShKB0VKVjXktsnk5tl9O9sypb9dHM0qtEt4FUBE4GpZY4cyDIoHyN8D9VxN5a9y6iAlVHKnfUifTIE26F3iriSth4v1C8t2twsqYkUq_hMnWg0pFBHJpDHdt1IyHKiqTr7on2uKDHWZqTlZJ1I-WX9pMko13YA_BjYlQTpgTNcUU2t8ug3y9PYeVHr159q08Gi59zj_6lxi9x_RFYpliMU4IvFrytaJXbYOVKKM8iug2z8-lc3bcxd8fs2kSHdK_iidY7IQHVVjk3YP-sLk2wQbj4gW9BtzLGODCaolk_lmehZFER97pPrpSItEvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=S4HB059knyuv3dowfW8_89ro2ShKB0VKVjXktsnk5tl9O9sypb9dHM0qtEt4FUBE4GpZY4cyDIoHyN8D9VxN5a9y6iAlVHKnfUifTIE26F3iriSth4v1C8t2twsqYkUq_hMnWg0pFBHJpDHdt1IyHKiqTr7on2uKDHWZqTlZJ1I-WX9pMko13YA_BjYlQTpgTNcUU2t8ug3y9PYeVHr159q08Gi59zj_6lxi9x_RFYpliMU4IvFrytaJXbYOVKKM8iug2z8-lc3bcxd8fs2kSHdK_iidY7IQHVVjk3YP-sLk2wQbj4gW9BtzLGODCaolk_lmehZFER97pPrpSItEvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKFlPjtFZZrPYteOvoY7LYI8NKIgaK5xmuaXb_uATj7551pjFanu_cJN1FvwCrb8IIrEQcRj6f11mL9tCVKoPxXsMug74Y0EPCYyz-FMj1agNGeusK4PiJtH6v5_akZ6Shuzo3lkpNIQl6WYutNIEPN6vGV8Nw3EIrtJy69yfCxI0uQ9WXCyLJ7hweRInaHEbfbHIgTvlOS_egUhUzVUQz-T4O6GNa-cSvCSvolHPKg_1BQlUWMFndsRrAYWiUEnFGhN7HY5bLHNma16_15f0M4u-moND81KWFEnQdltW-YRkIN58dYVJQjERDRrYaER5fLgDy1G6kHwsGZvoTwhfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6-M1mXfK0DdfGBHDwNeLHEMkxkwYGvxMWnb_crI354cdIfil-NVhNQVsq6UPs342GmKXOuwMTYlg2MC3l6Iz1noRWnG4Fy7adparPtfzNlVDtu5pcODk9nWdYNaDQ76gYW3uLxStWdhFO6Y0NrCi-KG5cMNz55SA2tP4JtjB16xchZCt08ziEZX_-OELpxbVCaSlcX6ZhgSoT-i7F_eccHzVRahq55aGm4t6RT3TBi1iBAusuB2MBzoWmr2scaQqlX5-MXnkCTNBcFrjmguqqnZ7nN9U98bnVwYM4gxMvBUUMAueVq15l6yxvvI8WkL2TTL-w167ibG-uyClowWIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JBASwUPtM1CghH8d5mU2fYwWP2Hbqb7ZcLIq6gOPgwDH0DYQN3kzt3ITZBwBTu3_Ac_nlfe3OgW13DA20V_0oGxZbGIROI2M5i18cXRYPaHpt1PWvuWGUfEqusWmNDsVxxTsCyJms5STA1onB7Xcnr4_IZuzYAyBtd706M-11yKukB2oExzXC0LRa3mKJ8V1RKuW9iuIpZeK9gdywDQKwhNT0D_KObQKaRGKb7vbYxr7F4m4ijSIm5qP6XEpWWB331UXykEtjGKFgynBqls4TMO9oc25GNUc9YjNb-7w8Xhtcpg7wiS1Ix5BMmi8qEqTW7eXg_F3lN6DxQUM4k5CjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxGxh7zcvajuDdhSS2859fv8Baxdxn5A7Xq-QBgYM45dgzcyaYGBtUz5TRaRzBPXN3iXRxDSgC48z6QUq6MgtV5nW7SbvCyXKiwZc_3oOFHsdt-GuUvlqLrNumEkYzv02hWZv2WEOc7rVnSWmmcXl93J9Vo-rN7rAZ1Yx_zBFbF-mXes_PupfJxXxlMaJkie8StmaHrdnEf46OaX8nG1Xv5UN9L4kd7_X5DMeUQ9SS1poxYmzBTS2Dqn8ANo5X7TsafeJXvYXsk9imCDwTnzCABiHsNw8ZxPrrO_6OnGAGS_RhS9gGf3LU3bshLV_s00iWEuKtR_9aCibj9iFzLgHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urdEjtmSvLglxP-Bc2Byl9I5zH1_VLwSU4qUJQ4_r9gOaOTahFIwduKUKdqEK885b-7NgQQyr385vhcl5fhYXp1ylOlgz6yjApcQgW9634-SpcIN8AledpmGCmgoYNUeR4GwI4fiAC_ByGg5QpyEhu4A9A77hpowSKRbhylkqL5veOvTumP9mVYbuvC2IkGIOeRCqREOcZebuWcUb7d4mVkIw5A7hJzh9EP68WtdCQMEeF7rkl4-JaFy6AKe2yJ1C0oxolFyPSlOYeOEnhKqaUZO7mfiGrfyG7WdxzUnt9my8Tvcw7KdaiZ_6Re12q6Pp-AynOaRydQKR_B81cIYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMbF1AMrXiMkeio8Juyuo5_uv3aEoqGJG5j5b6kefeIC1OyV5-gMvtn_8x6maUEzcd6WRAtVY2-sa4TOQVxwM--7UeZqe7pJj6Fth2lmlgyx8pfv1XBqUUGXkhya6CGoCVi6c-1uwtBcGrtNCX_3DoXvSvHOc89JX5McG79oPJjngGxlXylRdyeJc1kfo9qHFZZ2pWmxu_k8o3-1ZW4gUzNzYA1oOyiOdtQ86YWErkGOjyXRPDBVpKR6tbwFuEaxuTu3bx6c-xGvTnNYHAoNITkd1PuZWFyNk0M87vnEuQeSax_axWpXnxjAXA9Yl9esXdjQxh-Qbkwe5-Zq9EjiYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NyvCriuKDo6nxYj-mXGDFOnLdUtUA8BSC_EDOLTLk-pHb5wBpF3qZtXgAVOjmVaunZ8cKc5EIs7jWsD_C3WlEL0Z32_mb_Dbpgtd9NAdguyrqvXOndjesAUceonP7y2Q9MAC--8XSz3OqY51vq_5eWgwzY8jOnVy-_qunrmfq54-rNh8-WcGdoEJS2vpbSK8K9buABVYY6TwhSGrFBx5rjZ0cpB6Ekum1XEZzv3M5ZYJC7Z7G4kxrewxtPuvT6c1udIhrnMP0ULh18Zqv85O1F_9bG8ieruIbdk0N7fkAe65mem2dvjibobFU60YaL71egegO9UfY10epauLp71Ugg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=sxmsCBpjmBnfj8-lM61CVmBWW6iFQb5cgFiTj78G284qzNIFbJY8QfEsunbsfmNHFqjBlKGhM2iOHNh15dnJKF5gL_SfPZuGTLUJVZhuRoS1DI-x7pGw0tgwJthmxgLH23lGXdC6H0feFIPqrtusLan9A-H7q6WZfBHB7iGBgM7zlbY66v3aV9c6bxm6bAvfcOOlMsvk6aWfdKn3_vmQi0UmiPEh5YB1p6uw4HrSaHhSb5TwOLTlbjwzrmkCIYGrY1AGg__JE2g_3ugbFfUD1sT2NTFVP84RFWgFMvpcuHojTskCKkO9fH5L_3LSi-LvMoOhowDKkRjsEs4s68lKpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=sxmsCBpjmBnfj8-lM61CVmBWW6iFQb5cgFiTj78G284qzNIFbJY8QfEsunbsfmNHFqjBlKGhM2iOHNh15dnJKF5gL_SfPZuGTLUJVZhuRoS1DI-x7pGw0tgwJthmxgLH23lGXdC6H0feFIPqrtusLan9A-H7q6WZfBHB7iGBgM7zlbY66v3aV9c6bxm6bAvfcOOlMsvk6aWfdKn3_vmQi0UmiPEh5YB1p6uw4HrSaHhSb5TwOLTlbjwzrmkCIYGrY1AGg__JE2g_3ugbFfUD1sT2NTFVP84RFWgFMvpcuHojTskCKkO9fH5L_3LSi-LvMoOhowDKkRjsEs4s68lKpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=VoFDgQLYdr64a6hRal0iCyekA41lgKkl090S3EIcY6suIQgRfg0_l-VmSId-JTdxT4eie2nLwfB2PVWU4xANtoGuZVh6MI-yVMaOv8idHsOmgtsuzmYKadyhRJxDUhvoHChmbAG0UH1NOs_yc28xU76iOorAhU--G2adM2XQ50Sd9xqJeg88MDzd1UXu70nXu9fi_WvKmUK9uIWZh8ErNcFFyeGda5B9hpxbupkpSYFfc_e6iU8NdB8e5s-dW9XcOpTFnhDXqGGuOHWpgJPOzs2IyvTsx4toYG8zWPRw7mTwOpsoe_mxHc8qpAiN6g-uQeh-krh60p-zj88Sxa2VRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=VoFDgQLYdr64a6hRal0iCyekA41lgKkl090S3EIcY6suIQgRfg0_l-VmSId-JTdxT4eie2nLwfB2PVWU4xANtoGuZVh6MI-yVMaOv8idHsOmgtsuzmYKadyhRJxDUhvoHChmbAG0UH1NOs_yc28xU76iOorAhU--G2adM2XQ50Sd9xqJeg88MDzd1UXu70nXu9fi_WvKmUK9uIWZh8ErNcFFyeGda5B9hpxbupkpSYFfc_e6iU8NdB8e5s-dW9XcOpTFnhDXqGGuOHWpgJPOzs2IyvTsx4toYG8zWPRw7mTwOpsoe_mxHc8qpAiN6g-uQeh-krh60p-zj88Sxa2VRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=CwyIbOzBJsL37kXDlD4R20Yft3rdzn8ZTinN6HxEEO7lXWgYJK-Jgd20f7z_DMwSmIJhFvuHeqO3QckYkVPaPIADSrrDWzH0j3xvrQEZ2PQESeWiqWXKa2UKVPjbohTchrZHRXOEYcziqnO0UCibtyXPf-5VTjnjyJwOwjOg5QsbA6iSjKu-D6tnHl221ZcqIFnimkQj9nnAdUCnJrx_d2i8xHX2Wv4fNviwowl8bzC1jViw4TdUM3A_Gs5_5VjtUZ-fVZyfCETg72lhA8r_HhEW2MbDk0cQsd0t6ugxUIW04r0drfihnt0DkSZMORAURHwZ7DoGxzLNJDaFZok29g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=CwyIbOzBJsL37kXDlD4R20Yft3rdzn8ZTinN6HxEEO7lXWgYJK-Jgd20f7z_DMwSmIJhFvuHeqO3QckYkVPaPIADSrrDWzH0j3xvrQEZ2PQESeWiqWXKa2UKVPjbohTchrZHRXOEYcziqnO0UCibtyXPf-5VTjnjyJwOwjOg5QsbA6iSjKu-D6tnHl221ZcqIFnimkQj9nnAdUCnJrx_d2i8xHX2Wv4fNviwowl8bzC1jViw4TdUM3A_Gs5_5VjtUZ-fVZyfCETg72lhA8r_HhEW2MbDk0cQsd0t6ugxUIW04r0drfihnt0DkSZMORAURHwZ7DoGxzLNJDaFZok29g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=UnRLSfgpJQ8RNWmkO4LMGSTl5HBJFYY3H009v1dUnMzc0FwfsDlr-zgTU2750jADx4oh2fXCWqEv0At2ztZDMyZPec5eO_I7RWufNHa5188mPE2SL6ofkk2lzs5ok8ovfohT6gPRzCOlIxlcqG2rOUsBd1usw-8CMex5Yujm3wXopcAjz9chiezRHT7vIriNrYs8d_zkD4Dk8YWlciUGqT6Z5Ln6VUCdGznPRGaCRghYZaOFUTbAuwp1loEA-E14BmeXJEkpo2ixk0-yspdsuRjSh4M_jEzm68DUuzD1hlXKADVv_UxVvYX4hdT4na2lRGjxTNB-RnvgTR-XM3nw2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=UnRLSfgpJQ8RNWmkO4LMGSTl5HBJFYY3H009v1dUnMzc0FwfsDlr-zgTU2750jADx4oh2fXCWqEv0At2ztZDMyZPec5eO_I7RWufNHa5188mPE2SL6ofkk2lzs5ok8ovfohT6gPRzCOlIxlcqG2rOUsBd1usw-8CMex5Yujm3wXopcAjz9chiezRHT7vIriNrYs8d_zkD4Dk8YWlciUGqT6Z5Ln6VUCdGznPRGaCRghYZaOFUTbAuwp1loEA-E14BmeXJEkpo2ixk0-yspdsuRjSh4M_jEzm68DUuzD1hlXKADVv_UxVvYX4hdT4na2lRGjxTNB-RnvgTR-XM3nw2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=h5SVPE_pDpr_iRTuqDN_LADWlK0NwbnFu0QSkcG-2E-gDDwN02Vb_LjvjPOd--WwOpom09SnceZ2d8gsQjEJmwltmvvDgJmDfptRVBQJ-Lc6TrUp_d7l1yQTfZ-tBNs8hTB_9CScg6nY9ljP9WS3XsNNzYu-LWJ-23Tm-02BPyHbHx33eaVkj4ztXnpTUPcD4sTPepSzugJwLE_vtqZz22JSar6uXlz7DxsNw81IQFORo0vF-ad8H8kwjJ4o8CAr8WerRCuwzEIg414tMdi-cpd4OufI-0N5DaGE7ynY1wsjQnn30m1fAt_94nRWnFYvSF-6pb5gorZTcfkJZr30nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=h5SVPE_pDpr_iRTuqDN_LADWlK0NwbnFu0QSkcG-2E-gDDwN02Vb_LjvjPOd--WwOpom09SnceZ2d8gsQjEJmwltmvvDgJmDfptRVBQJ-Lc6TrUp_d7l1yQTfZ-tBNs8hTB_9CScg6nY9ljP9WS3XsNNzYu-LWJ-23Tm-02BPyHbHx33eaVkj4ztXnpTUPcD4sTPepSzugJwLE_vtqZz22JSar6uXlz7DxsNw81IQFORo0vF-ad8H8kwjJ4o8CAr8WerRCuwzEIg414tMdi-cpd4OufI-0N5DaGE7ynY1wsjQnn30m1fAt_94nRWnFYvSF-6pb5gorZTcfkJZr30nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=Wb6Ahk8LzK8DCrTEG2FHiAyl-BMhmMD-_5tiZhBfvg8MbeVm5Vhyuri5JGHVgJqBeN7Rhv2ppU1LaIfPqyGy4y5vohYHzoAw-uQQP7ga-zt275nUWxcZuTxzOWEg5ZtO4TFKmb7UDKZKL7aR87ifmTdDdli3ZciwAendpVKBrfxHoAan3Ya1k9Bk2srgdWllHgHeOMpWvw4WueVF67yBvBzf5_-1a7eOkvlZjI4TV3QGbPzgKo9QqfgxGMXXk8nQgCKyRIwv7joFKvLHG8YXLBlUlXT3wY3HkRUkDJ3K8CRBeu11qVUU60Q11U2WoccpXdtoHHVC40l4Si6Us9B3Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=Wb6Ahk8LzK8DCrTEG2FHiAyl-BMhmMD-_5tiZhBfvg8MbeVm5Vhyuri5JGHVgJqBeN7Rhv2ppU1LaIfPqyGy4y5vohYHzoAw-uQQP7ga-zt275nUWxcZuTxzOWEg5ZtO4TFKmb7UDKZKL7aR87ifmTdDdli3ZciwAendpVKBrfxHoAan3Ya1k9Bk2srgdWllHgHeOMpWvw4WueVF67yBvBzf5_-1a7eOkvlZjI4TV3QGbPzgKo9QqfgxGMXXk8nQgCKyRIwv7joFKvLHG8YXLBlUlXT3wY3HkRUkDJ3K8CRBeu11qVUU60Q11U2WoccpXdtoHHVC40l4Si6Us9B3Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=Axfiei7r8Ad07CZXkV95wl7RILViwqF056mJBxVEd1C24HxUkw8ZKw398-Mw-zALu0HivA_NVanmTGQ5cG416LbWg78uOGxbMZozXxkP5Xvue120Hk_3xAH9K3xMIPxwFlqWrPmpKjG-BN-_dJwzWACr4ffjo13XouadTq7zDIg34dD5ur-vgeaAes0IAn5KlVbliYeRMgG1Vo2VEh3-fZn3WTCo3T86IAIB__oRYOn59hXYbbtmX6iQgybpvvA8ivDsQGNsHz4VWVv3AL6b3ZXCxSno35RcwqecTHqW2tfNeDxs55r3XQlc_ZRM-wTgOkaxj2XjMNoLMR1854u1ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=Axfiei7r8Ad07CZXkV95wl7RILViwqF056mJBxVEd1C24HxUkw8ZKw398-Mw-zALu0HivA_NVanmTGQ5cG416LbWg78uOGxbMZozXxkP5Xvue120Hk_3xAH9K3xMIPxwFlqWrPmpKjG-BN-_dJwzWACr4ffjo13XouadTq7zDIg34dD5ur-vgeaAes0IAn5KlVbliYeRMgG1Vo2VEh3-fZn3WTCo3T86IAIB__oRYOn59hXYbbtmX6iQgybpvvA8ivDsQGNsHz4VWVv3AL6b3ZXCxSno35RcwqecTHqW2tfNeDxs55r3XQlc_ZRM-wTgOkaxj2XjMNoLMR1854u1ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yr-s7C0Ek2868BPgJV5s-EYDX29TZ5Jga8__m8aC1D3ATG32RjgelZj4jEE4_ysbuR8Xo9KtlHJI9hepNPICeOWtfbcPNusa2LFUxLvWQp6X6i2Go8amRsTO0k9E3iR41cw9sSPdFtFUL7DD8WPW6wPGm_lhUFZW81HbsDiRnCYlhbGz8qTmIINZpd3Eo9Q8e-W8npVqeFtGptw1mDOn22_stVZJeuHJ0FFOiKJrr2RyIgRDid-pIqUMDJhioRUmAJxw9YHsCboDt8ST3u93T6jGG5aijcIy2eRL4n5ti0D2S24IaunpD01YP84sjUDapUf-numat0OsVTor3SidEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=Fv0lkNDYDXP4AQtsdwmg7l4GHbAMSyUGwP2oYAKyQDjoDZsPfUwyUsdsKHHnyAFmweF2Ec9hS4pUeAB3nUwgejFdmG4wAglJfWgrd7OvDHpWGZ4EyPryGzs7SWJTJmk04D1UKRNlXej-j6dHOfgGwsBeCRdqVHd0Hhtxa77UzwqKQlnj1DPqRnz74rAkLAgeJJBBmh6g8sPhsRhLY7mjtuQnMRfkwGh6PzRps7F40GMQGqGthnSO6_BEGWcvnlkwJx9KGWtCakTArvTBf9bcIvsHGlV1Y8NfEIFi3NCshUSqxgqiPEQ4Hxj1DB62VSxWFJri0tW-tSZUr11idhGVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=Fv0lkNDYDXP4AQtsdwmg7l4GHbAMSyUGwP2oYAKyQDjoDZsPfUwyUsdsKHHnyAFmweF2Ec9hS4pUeAB3nUwgejFdmG4wAglJfWgrd7OvDHpWGZ4EyPryGzs7SWJTJmk04D1UKRNlXej-j6dHOfgGwsBeCRdqVHd0Hhtxa77UzwqKQlnj1DPqRnz74rAkLAgeJJBBmh6g8sPhsRhLY7mjtuQnMRfkwGh6PzRps7F40GMQGqGthnSO6_BEGWcvnlkwJx9KGWtCakTArvTBf9bcIvsHGlV1Y8NfEIFi3NCshUSqxgqiPEQ4Hxj1DB62VSxWFJri0tW-tSZUr11idhGVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALgjq_N7daps02RP0iZI5MNEMNENJbvfTAl0oJ0uRsFPWi9RD-Lxh809grTyHN4ArkznNSuZVuJ3-u4Byb8rjc0A_ElYD2RtgTH94nUUtbuOby4EaOe5dhYbRt-QO5FinFLVMLDEYs9le298kjhDjH06fEeAl6e8d6om7NlvZAVbWrH4lO-HJr_wRmDpOTY2hjcXyM2qyOMuHC2o36dvoidaPeF6eJwzgsjuJErbYWkZVJnqycRVfj-RYmBYKQhDr-CytOI2vYWgO1q6FCggBYK8ukgagwwqONl95dmDz7cB0YJwH2l_sxgP9wIfEHG_8sRkmN7jdf2nlXrVPslfJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYjIQ9gU9Sm40R7BhErYJmb18K17JMwR8Y9E9tNQY9lR8Fs6Xsrn1QCTLnZ9Y2GI71dC--0T34Ygde-9C9lRFo59MGfHya4El8cKTDrVbLPHV7Vq3UWUIQjuzO6jdfrJdwfAxFZD0XW6BKwCIQ4lWl0xGx6gcFnKZFIoUIA8OWUZtBxEAOSSg7nKMwfRkAlPKoW7hYNdxhaD31YwvQRRBFGZGmcI6BmR0XkZ6U-LRtxld6eYklOe0EYa9ZI877Za1dcr3OzgOPvHfI-U5_jagmcyg88LLMKw6hguo0sg45bXtJZ3D5B_Z9lDl-AXTMj6F64AlBULhLmnw0IjVIoYRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWidkawijRt53BvIRrpTJx3sDMdJXypxbxncWEN8RB070qlonCgMj7NmRnQslbbDWGGpR6H_6gzLQ_qwOaMYt-BQtYgMx3ykWoG6Wqik0HmI9rWt0VvG0DUsZ6TRYwDhnl9nE6XZBK7lntECFa-Eno2R09vF9dc-l8lhy8cbLstwuKDrOn35Ijs33U1WGXn4v4geFnC3tYOJgRovvqjWHSOuZ3eCCO4SudpNi8p1uCnxKwmgLWU8cgFdoxPl7uGjd39ByMhjOOcUvbq_JnAcUx974E-wOf-7vD-8a4GGdz9v2nhVZ4WEvfsZqz2Fa6OWZId9ua_a72PwWk2Jmb8Dlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hy0iJnASD0ye_ZAXjh_6eTtc7Usdv3KXKHoZRY8BMsmJO__Akb8BD2HU4sst-YAPOfw9f1Py9UKJGjBy_s8MDVO5FaTmiEbZy_XoDaDXLmvzo1sTfNYhFCqynAOyymqhRtYqaBslzrwhxsjI8oKiN64UR8p-jYLKtYgOheMgSa3kyFgydQv7K5Pctb4xNLCeBhN__Iew6iK2Trt85cEWWaMAg9w9PObNvNXo8TzAYYSVJyePh6vH1sNcA7G_pNWmlN4UWYq8lTWf6p_6BB256ZmRSJYCC10P0WplM5e8ul1FFz4MnSAxASTZhIwx-GBisnElkjx4FIZGdQ5J5d-ZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=V-o2q5DglFsBTg7OWk0TH2kc6i_fpKVCvFUZE4RQfzBy0p-Jqb62GJBxl044zJ1Iax-_P8D0pt-xEDA5sCUg_AncegmVb7vj71StkzYYUDU6EyVjjdX-ItR0kC7DUW32U6lwqZ0Ksmj03unYVnS7oXTjqIMn-tyLFKmFXvLGewBERjPuee9mStOXXAGLxTjycJ7sY0Y-CCOpyEmj92FZUdMBiXHPWycbXHUlJKxzWGsfvTYF-ujk_GMbf_cTpoONnrMERNDfiurYJmMRdtjPYs3Plqe3ThkympIiz1SUIqW9sAlOqM2zeynE-Wee9q42EFl2Yw3t_OZjJWuvGvRqgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=V-o2q5DglFsBTg7OWk0TH2kc6i_fpKVCvFUZE4RQfzBy0p-Jqb62GJBxl044zJ1Iax-_P8D0pt-xEDA5sCUg_AncegmVb7vj71StkzYYUDU6EyVjjdX-ItR0kC7DUW32U6lwqZ0Ksmj03unYVnS7oXTjqIMn-tyLFKmFXvLGewBERjPuee9mStOXXAGLxTjycJ7sY0Y-CCOpyEmj92FZUdMBiXHPWycbXHUlJKxzWGsfvTYF-ujk_GMbf_cTpoONnrMERNDfiurYJmMRdtjPYs3Plqe3ThkympIiz1SUIqW9sAlOqM2zeynE-Wee9q42EFl2Yw3t_OZjJWuvGvRqgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr1d-gV0g9CpP91Ji0KSgF0QtMo9p6IsYt7gKQjKBzk1rF6OTiA2Xsymfvpr5LGqXPhi2vQJcmVj8Mas_rjAfmY_ZEHVLsXlUM0EGIHCwmhQcVNvtphrv2suBXmfupfkmeP9GyuP9QrniWFxhMmZ5zSM_QtT1MT2o-uMUy77SjT7-zn21CsDpHAk0E7VZP07YlRckwsqTra2km064plH2VyLx4uuewkT8wWdwNehy840WyC2_k9ptZT8P7p7M4bkahTznZBfSUHVcziKyEZ1Q-yJqSXb_VzFd3X_fBwjAwy6hnoXFJNcHS9OHGa5SYO3hJWIlfzWDmu2WSoKF0iZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=qgg87kFlqqD64vqupDDsJTwERy9k_ZLM_BuhM3xqqqrnAe3d1ktd8wnsr76c2cJ97CUluwdP9LknGmhrgXYZKBQjP1GUlj8obsH4AxM7IEtqtrHFWP8-EbVQ5fa6Este6qc4MVSUNrmtY1pZHArOVMlCJR0vBJO97UVdHJGIzUK4cg3AMDSqaq90k_8KyDSym7A9QTwcpRDy2nCKkFWB5-OuNTUQK9hVBxEoFPyHJTmnBL4pcetKBHKMs8q-Ak8Xp1znJ7-_ygsU_MBNxVpp0r3ceIhH-zhCDO9ydWoZZgdQxq4QFbk1oxc133TjApHiCO3gAF7ysER2xSyOhyUS3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=qgg87kFlqqD64vqupDDsJTwERy9k_ZLM_BuhM3xqqqrnAe3d1ktd8wnsr76c2cJ97CUluwdP9LknGmhrgXYZKBQjP1GUlj8obsH4AxM7IEtqtrHFWP8-EbVQ5fa6Este6qc4MVSUNrmtY1pZHArOVMlCJR0vBJO97UVdHJGIzUK4cg3AMDSqaq90k_8KyDSym7A9QTwcpRDy2nCKkFWB5-OuNTUQK9hVBxEoFPyHJTmnBL4pcetKBHKMs8q-Ak8Xp1znJ7-_ygsU_MBNxVpp0r3ceIhH-zhCDO9ydWoZZgdQxq4QFbk1oxc133TjApHiCO3gAF7ysER2xSyOhyUS3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=YW-EjD5_LiW6jVmsfDLF3uZEnrfLgRAqcY3bEMbZkE1voVSf03GXGDoz2PJMLhEpciNRnQNab2lqaLOfF0BwmpXprKWACHUtj767xAcOPFPUrLIN072wK3VKkpVg5PmtHikBAW_2FozjlTsqSl3kNtCuXX-de0RGPYs_AlU3Ow7QGj3z8yJq2xgol3dykJP-aTxR0_ltilvRmvgfmRJKZ9UaPFXr98HlXIT3NZb6Qr_3oBAwFJ5behjLj5Bt6MPy68YuFeNeU8HEfQU4oGD3ZqcbMxJ-OsX-GifVD-xU0Xle3vyljx_Y4KZsjHknkchrMj2Op1-Mtvn7jrSdclftHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=YW-EjD5_LiW6jVmsfDLF3uZEnrfLgRAqcY3bEMbZkE1voVSf03GXGDoz2PJMLhEpciNRnQNab2lqaLOfF0BwmpXprKWACHUtj767xAcOPFPUrLIN072wK3VKkpVg5PmtHikBAW_2FozjlTsqSl3kNtCuXX-de0RGPYs_AlU3Ow7QGj3z8yJq2xgol3dykJP-aTxR0_ltilvRmvgfmRJKZ9UaPFXr98HlXIT3NZb6Qr_3oBAwFJ5behjLj5Bt6MPy68YuFeNeU8HEfQU4oGD3ZqcbMxJ-OsX-GifVD-xU0Xle3vyljx_Y4KZsjHknkchrMj2Op1-Mtvn7jrSdclftHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9yIU9f3ClXn79aBrLjqEDCZPTh0-LMA1xIclOm-i4YABg9FnsYi_H-tihgKfKJFsYQMXEBtS2SBI1pJD4zFliZ44REr3WHcLNZjzNVfgR22isChJGjPjzn-bVG_PdyGlYR5dmwM8h_8uQG5lkY6WczYxUezZkBTvGv86DQJfPSvxsug1UBfah2Oh6JteWuzsikBNNHIbqlXqq90L3EnyDADIMEFDbiSQuz2xVvWbplZnFAEFY0U7EaGw5qPeNR9LQyrUzoVmbsIldqI6ic-7DuGHcsTbD-NdQPRP4ZZCHt56dWNqc3m-rJccOsG5phfa3cW1zcM7gGHO-Kst5yzzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
