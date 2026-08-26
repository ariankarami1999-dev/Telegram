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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 21:39:48</div>
<hr>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=DL7hEO4X77I4cEMEo7bE3Q-5zDxTaGnL_QF9hZ1pyBJfPlXgYpxpTVLeLpS6bKECpmK0daNh-8BEelw4N7cvjpNYEoQEI7XFqMPTpF9TYHpBWUYGlcQSlwkmq8VmqwY2CTBMhgQwg-Yvy5eLxVe75ZKpy2m-I31FD3HK6cdTP4SsuZvX62y15pGXIjqGa9FxcIXz5Qk1qFr07MlpYi_gqcLHOvXSB3680QDTXoj5-NJnz-v94579YPdhrs3hPRKvawJaAIQfLtnYItVvNlUfL3oBIIbOdhmC66aD8NBRV_KmrrchgIwzdqhNAv4OyvqRGF9Z5LIs4ej2dpM6_6SDxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=DL7hEO4X77I4cEMEo7bE3Q-5zDxTaGnL_QF9hZ1pyBJfPlXgYpxpTVLeLpS6bKECpmK0daNh-8BEelw4N7cvjpNYEoQEI7XFqMPTpF9TYHpBWUYGlcQSlwkmq8VmqwY2CTBMhgQwg-Yvy5eLxVe75ZKpy2m-I31FD3HK6cdTP4SsuZvX62y15pGXIjqGa9FxcIXz5Qk1qFr07MlpYi_gqcLHOvXSB3680QDTXoj5-NJnz-v94579YPdhrs3hPRKvawJaAIQfLtnYItVvNlUfL3oBIIbOdhmC66aD8NBRV_KmrrchgIwzdqhNAv4OyvqRGF9Z5LIs4ej2dpM6_6SDxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKc0l2K6l13aEdQliPnwvI2yoAGKD8XqP414ax5EX-8Pos_myb1LT4cDG0Z4u86w-HNglTu4ncJvb8I-XiExMrZDufTcV6wFxspe5EZU_C9AIE2ASUcKFPcJCOAbWPspQ6v29ZyzZAWEJuK3syTypZ67cBO2OOvgXMnqp6NwkaM6kTmP2CqQ2IpTsXPEVoPRhaYP4RKcI59ubmJ0-ncACH4oCDqkEsPGPeZs2Od7zODeaNz5G6H9G3mUKm2faZDq1U5QZlVb2H41O3b7AN1peaURLU5vivZebOBKLFWJCLSQ21_vl6-qdDmOttIV5uXIiUqi1v5xWMbnuX3HaHeSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=VQzIpLWJL9LZr_DYVcHKcGT98sEuQhgdcFiPU1msoWWR5A0H6Gtuvi5AskHx3HZsGUEPXwbxaNRJOjbI4noHHfQutlxuIJqLzlKJZAETWCmpWSAv7cB1b9O4xDk0enq-bpEcnXwON-cTzmnnseXe62KCq2H7dtmuV5_7JLlVDZvnfmNKwwRSrPlibItvQ18KcIYDl16UdKzxfZuxeW_SIjczFRmWHcF-ZW4AI72O-986qfFRXiD5h6TaLAa5yafFxQQjvXyitRMK2gUNt878rfkBD8QbcAFZpjERLdtk4dSAKfLw8XV8LS5lAy_JhHKGgMJzf_dmi1piWiE7MQQbVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=VQzIpLWJL9LZr_DYVcHKcGT98sEuQhgdcFiPU1msoWWR5A0H6Gtuvi5AskHx3HZsGUEPXwbxaNRJOjbI4noHHfQutlxuIJqLzlKJZAETWCmpWSAv7cB1b9O4xDk0enq-bpEcnXwON-cTzmnnseXe62KCq2H7dtmuV5_7JLlVDZvnfmNKwwRSrPlibItvQ18KcIYDl16UdKzxfZuxeW_SIjczFRmWHcF-ZW4AI72O-986qfFRXiD5h6TaLAa5yafFxQQjvXyitRMK2gUNt878rfkBD8QbcAFZpjERLdtk4dSAKfLw8XV8LS5lAy_JhHKGgMJzf_dmi1piWiE7MQQbVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=iXkZIesf_0px6glUvetWH4uKA7kXKNzRDwLGoNPJOwWcQcnrh0vzahwmzPz8VyrZO4W2Q78p5fp4cwI93e5uUfKhzc9NPj5AlaP-d-ztU1UsgwYHx27muJc0oBYfRsBtGE0dlm6K4uV0xS92WfWOCHy9CzYetIQl3ATjkrp5KLoZRkKs2WQa9qxAmiyoMU62NMKk0MUc5yITYHy87tfGyPUjWAv_6reI63QgTorp7oUBB5WQfa9NyayaRFWMWi570U2Vk11EAPpi9TuZFBeYHFFJw61Gt49l-RyZHvM6gYySeAMqgIdyuvGugCsPyjFC3xUNftKwPDsZV6_2uPXrOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=iXkZIesf_0px6glUvetWH4uKA7kXKNzRDwLGoNPJOwWcQcnrh0vzahwmzPz8VyrZO4W2Q78p5fp4cwI93e5uUfKhzc9NPj5AlaP-d-ztU1UsgwYHx27muJc0oBYfRsBtGE0dlm6K4uV0xS92WfWOCHy9CzYetIQl3ATjkrp5KLoZRkKs2WQa9qxAmiyoMU62NMKk0MUc5yITYHy87tfGyPUjWAv_6reI63QgTorp7oUBB5WQfa9NyayaRFWMWi570U2Vk11EAPpi9TuZFBeYHFFJw61Gt49l-RyZHvM6gYySeAMqgIdyuvGugCsPyjFC3xUNftKwPDsZV6_2uPXrOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jg-J3o8JERmmNGajH2Urn0CIPz47bgg1m7EPoI5qNRKq379Cr34SUMrQ9iwpzyxDekpUApRifSZ1N28XqIDjz1iw1whDm4pxPOGe6YHoL0Q0IR-uA0eWsEX8IxV9XWMN5UaWjhoVUh_hhz25o8Gp5QmxMQVqLeDaODVY-IoHCH2goYRcc1C8XHHNbiOoIxXNyW7vs-WzRcEWgIreIadwdIC7LQOLHdT1SBPYW1uIxP60HRboDYPRKw3OQ8xICliP7RCMtyzCKuMP18seNfdsc7tV3sN2FQpoh3qW_EPqhs0sz_3RMqUP4WGb7rEeF14OPq0G1ALs7RStzmvr8OeOTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=N5ifUiGPDCl5saaFBnbi1G_0TDJ6WZqTVKtlc-Uy3FEQBf4yv8o0ll06kF6uFAYeiFHiIlG1OxYCZ2Cab3hV7ZqB3-BKs5MF1HoEfN9d3tLgBc04lwWLc6bNihc5cPqUzmOkbwOvkpwi5SLmM2dc-5LcAseUJVoBL_dAqmw5rIt1CQjhFjYZLr3KA3XXRSlgtBEBOVE9-QGX1ra15kl4_qn96gJVfWjJ9IN7vFU5ix8E3n7yrDQHGpmgbG66vN9vtVSbBX6j8mZjKeyjN7hWdoPsJiHagpEw65NEJv5zfXAcKwshkS9QH-_BFKmOhwtLpTTFux7Vj61jkgwzq2bsYLVQCrVAr6Iu3YIFqzNF6jtM7rSvyBnZD7a1wkCd2Saljmk7HGcZivHcrLJjCWqxdpA4qE8Dfsz96WRb0RepCUXCQ8Vcu6DJ3r5w2vr7h90AdV2oM25Otl5WRNVrqg4I6PR4WfoaWx0cLr-kJqhdySwB2QM6DgfA8a3pFHyEWIKi5HVeRkEWrtG4G6LQIGSO_eM_4RTk8kzfR2uq_HJbpiFZnO-vwuPQCm4rbekCSJfKC_b6QESdXjA60koXLOI07bsvvSWe8-6eZxO-cGfC70exKFLcjrGLummbIjAJ2xZgVvq3r1sYc5Wb6MOHYdCgif8N3HSLC8zGV7WfXDx4PMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=N5ifUiGPDCl5saaFBnbi1G_0TDJ6WZqTVKtlc-Uy3FEQBf4yv8o0ll06kF6uFAYeiFHiIlG1OxYCZ2Cab3hV7ZqB3-BKs5MF1HoEfN9d3tLgBc04lwWLc6bNihc5cPqUzmOkbwOvkpwi5SLmM2dc-5LcAseUJVoBL_dAqmw5rIt1CQjhFjYZLr3KA3XXRSlgtBEBOVE9-QGX1ra15kl4_qn96gJVfWjJ9IN7vFU5ix8E3n7yrDQHGpmgbG66vN9vtVSbBX6j8mZjKeyjN7hWdoPsJiHagpEw65NEJv5zfXAcKwshkS9QH-_BFKmOhwtLpTTFux7Vj61jkgwzq2bsYLVQCrVAr6Iu3YIFqzNF6jtM7rSvyBnZD7a1wkCd2Saljmk7HGcZivHcrLJjCWqxdpA4qE8Dfsz96WRb0RepCUXCQ8Vcu6DJ3r5w2vr7h90AdV2oM25Otl5WRNVrqg4I6PR4WfoaWx0cLr-kJqhdySwB2QM6DgfA8a3pFHyEWIKi5HVeRkEWrtG4G6LQIGSO_eM_4RTk8kzfR2uq_HJbpiFZnO-vwuPQCm4rbekCSJfKC_b6QESdXjA60koXLOI07bsvvSWe8-6eZxO-cGfC70exKFLcjrGLummbIjAJ2xZgVvq3r1sYc5Wb6MOHYdCgif8N3HSLC8zGV7WfXDx4PMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amIwKnkHQqmiDNirSRkbVKNe8tx3JmJ8z6ix3uK8_VpYrxPN33HzkdwiMvYnhGoqmnaa7MV1HYDIZq5N5B2PrckvaQI904ZC2ibEiI17G29KTHtU93OAZoK-jsKp1j5_Lvnhv9T77NY8KllPrmiK_ctGMEcWdd8YHA5_E_An4w3RBufYVZAopM2EjO1EJyFgJUdrJAadc9SYI7dDAV2YBsMheHLtdapf0ijII8M_a8Xc9DD1ZyqBN5MUPA6H36yptWpfQ5uddi-vYxPiOvR3DnQTjS0HDGoxl7q6WitW3Z7ayRvLs9oPdgSZT0n7R3gmhWht3KEPg6vtFqP0KuHb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0VwMlhjGj-jCMtayS8xxHZ6puz4USywLVcywXIpKW7i1JAbu7vdDmBo3_OqgymdCEtpbq7D03LmD-uoMAGn8r4sU1A5_qaE_8H4FIn-LewBGe6BnGT395CwEvEHW8vs_i-vSr1vOoWvAESGVk1d56RnrzMLUa-1vwLqm-VlWGOvc-Cl1BvCUR-LWSWsYpyO9nf83MqpxUtu61HF4QDgn-K0WGGCrllMgOEOjMiBLZ1-PtoyZJxaWtAMcgwDEgwgUDND7UVgpq5OEi7cgu88-v2RfWWlYARJbrKlwaeBcBef35OkMIO0vBEhgprWXpR_aspn2Q4o2h5f6nJ7GYABwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhp9yHmgt_V0PGzpaRbkY9nAMtYdJ2sQxVbAH22AWdSFI5PAU0wZmnYcb96Bht4p5HZgxbav9dmnEup4aSydmyvJQqKkno3WsZIcmNNoczjJHLMWexOHwBMtwYYIFdU0xk0yK-mYU1GvtR4cMA0lNOJIOjWnzyfWRbIH-jlHw68xXb7kltdWvxCub2J2zQkzdETkshnVTLceO2Vi_qcJjB9iV9QZgN6ML_e4ojUz7_lz9VTuWUJbWIDapDHmGX6qLGuDmVMkOgsKHtlpB_9dywZROBrkJQI_4NoK-HrQkOuWrOqMnXue5Qf4PrEYwkwRU287h4rqxVi7j9ULZ1JsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCN7nMZnEykdlZX6SYFdFkDhsVJqVrCvfsHR9a8Iv53-WIwlq8gUMW2IJOQwaunRm7AMs7VRJv5s-XzFXIqoIHzq_ppL43aKHJaBgDqChqV-RHo_R06Y_LvEt_tfyMSOMIc-mBm0cZR3kWtOtY_413c5PtIbXsbWe3L1StKdaYkTbjlvxX78NaEBm_bG5uCBppDkA92LIlKZSImS4ba605XeGL9cA7OflckvYqK6jZGRK2f7CE5cej7SD_QJRX_LWeaieAAwsQVPn-ESM4zYh08Ig_XTm9BHw3Mnv8cQ-p0suOmUPvNlBFA8titJAavkkfwNd5SPxoDPpEnwm4xSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW4DI4VzcEDGwI7sTI8KFof4rVVq619MEP5mj4xlAjpAxaGggKYzpBmsWkWMvOIsOVcMoI7d8ayakKQdeiPkSDbpX0VsLdGM-hTZ7ivRTCQ56-GlJwbjwihUHrarGMhXPf2AdEAg_YNpv3WdZxXf2Y0fV-a7jboLoTyYe9RXsR7j5eIURNgZAiID7M4pl8A_QIMB1q-zYADrAmwxZwXv3h_bfg5w_Ifbmnl9pEJRuRqAIa-5yut9wyxdJUNj3iSgy6XpuJbHPcX0ap7e9mfWNbnmhfP0_nCnsDkxrWbMYlWDN7D9m4yjv5kmIMWnBcjyEeyAACSXrWjGX6bpuQgiew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPo1yGulPmw2EV9QY8pSsiGSvy1p-SRXRqxvp-6Qh2mKqU_sQ_3Vg5_Rd9jF7-TOIrs7A9kSf-anTJtvY8DjcEbmtx4XbuCrdk3Pd8phslKt-BKX5X6gF21wuxsR_XMdmTwxsv2pYFLx0pXt759UaFfTP57vABImgPmAfAw35G-eyKzzN6UsKR-64_ULxVWCWLoL8c9KfhGlDMnsI2ZixbDVNZNE93j0eWNiQRe6MJOEAheTwo6fb1_WrLIuyJtHCbQkxx0dbImX5MBW5GGUuA5ngMxx8MnlGsNtxsEpgDeyunwfx9qXY33M-XEkAdwslOTvWsrRlBkdjPIdsw1XjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s32jaGnHRBqG3tQsxCZhw4MbKtaURpfOZUSKj5yRM1-uts-60kAvvfhbYp6ESHV4213S10Gk3Ri0cBRfSoGfXL-aCiCnEDUZIH9qH4isQpSMbYWMFSCzQlqR31bVwc2iHNnGk06QUn6JNDqzDkKAg5wanDEGTe0-BsNRAKu93t_Vg_2TJgMr1pSJoGj0h4nAOK48vCJ92VNwo-BOtbIa5u1JYkDzm82sykMpjlYFcSXITR-CdOqCc-5iiapCO5JvTGM-kC-nBGIVXzRVjZjhG4mZhVT7x6wy9J8d6FC0yKza63maor-jHS_X0_t6poyTAoSyIXBHY4lOZmf8APwo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUc5AXzvGLOyW3w5M1MEgbJXCSkaTP0Kyx72HCkIzqrqs6z6zINcPhxLUEqTYo_lZFltas0shcBD0VMeB6kdHpWcKKzm1TkNXPDUmI-gr9HK2Th4W8D067vm8tiIS223pRIQo7rjx3U61WDd__szNishmXxKM59u2sVLoOufXGZLVZoWUe_LhwagK5AZWdHhlRGV15GC6BdUriW9FQebX3TVfKtiF_2Shm0t0Bi8T7F1V0fUk5Bs-Ymtt9uqCY7-4POcz1GYmUO6lfMiPIPmtA619UGKSajgxVpGZwzNAjqRdxJ8O33HLZOE7720pRTJOktVq1yDhlwofOfchDjp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAgdWzYmDCHqV7lESJqYmYdzqZspsgzQrVulXpsJBWXOxpsWOOGgp1gqg6_eY4kH-F1axDuIZXZYMSfOF8ujx8nlAckSLwoMUp2UM9mNOmaQd6C3MDFCfiTqafDuuDBhvU1LD5t4ZaTuTY8kfDYXPn38gMvRdIHCA49OR3tg9wgLPRigJHnuCfoyiJIeJAwdjw_GVt8gAnoUilTOWgeXnimFBwpH6uPOnxzyPW_q8mfxpeSbPNYHAmAbHzhMbY83vf4lEkdAUwx0YCdX-bOEg14FJ9PN098BQPugrB-qZiTv3oJswuoza484kKORJcVrcybSQb18d-x6mCKNzyPl8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYoV_O99lnWooKx-nYegGmfdXtZlBDp8u9R8mnSGgivlwW8YfEIiuYDkicvc9CE0gKnzVECf4GX77jS3oL3S51og4P3bEsHHt3zXqx6z3Vu7Q_DXj-eamwCSb-KzFukmHbeGu9PVl5nDtxQkumjcM2kzEugrZZXEv_QpVohMPPht9zmgUpHChHo8uo1_M8QfZMDm2G1k4hoBhoMlShBK6115ETDxMlHTx6RHocYDci4LFurPUEb2NzwnxsGJnwykZAoDQ4jBVncRntIYvC7h_d0atNseWjro3CGxx7oHEJk056U_mFEjcAwBLT3RfP3N0qmnlPQ2PHwM2fBbpa-RAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amMOmpwkFHuiCom9VO4CCTqdxwW6w6LPstjVrGauznyp5xQ-ZYv2fmJoLr47DCZ5mYoIF0tGqeQ2wleOflyr2yUE_n8DzhO9KvBSEik9aBcHAvtT5-2WobxiePpESozFFX0o5oBFpjCQs3Liw2g8Mf5kC52xQQNINJngjWJCLzktNLvIMWpIr3YqYLz6Zi0ggaK77_3q8HUaP-v2Zh5taHd5SmND9rNoJ8LYU7QzNJ9ZoHnsVWMpAX9wggJe78xb9DDDk8jCLrGdaPlqZxZivHFNCaHajf3zMExfbRHK8sRgSLDQRrnv_tPn1cRH0X85tWFa_fIuzvOSeHPJ5L51wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HixJNmfAkD-PpV6uxhuOgMr7N9UHNwRsV-xbGNGLMM_7q8jx9OqGY2KJYi--s4JZpWhQjTFb2WFJxTgdFLlFKIjwqzB5_1jgMTf-SaQ35rwo9xuFZhs6DpHJuCyuUA9KsiSHO3Tt_4tRofCxaFMmP-g0PPsRZmX1AXXhViTQzRxflH6rpWKa5bXghP3TG7qv_pxDnqXHDZ04qHKstgfwqjPukbaM5JdLLiLEUmm5izVWBjQcC5EIfh1yGVjyt63AxJ7Oly_lLSllKxTor8QUkAOpUQvzPm4E6d7vFWBVywc7qO6nAXOtmzpqn8z5I7tt6DYwi_w5IdNsuDuQAY_l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyPCXLaGoASz9-2tniLnePiJKUVc4oL8SRDamLnUTG6mz2hqxjWw2OgGHYWqIhrviSstyYr-rfQZ0ULPy4YOsicwJaCD0O0Xb7ER9dvglXp1_1pKgcAogpE0xFyU0Ho6ToXOocOgq152ASvWY5LNgyXTx3bDP5sLcMF4BsY8XNcZyexCNUZWi7rZEWYgPgp00i1kwfHXKN-JCNexPJ2PsKJcmRpTgcZKAqynhyR_jSyRKMuvEVZMYGaRkK0T4O1s8Txvi7wZNwpLhlT-8ufpU-tmw54sCcmCKkVjJ71rBorko9FxLmAUrf6GNFtemR7HMBj4ugA_621f9N1Tms7X4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFZzxLfVUi4XnRfnLCBRpSEn2D0bGX3-YUYtwFBy8IZYrKKwGHE_8nVBsB03UPwXbFwGrJAYIlKmoqtPwhx85uynYeU3xxVpcxzLDq8XekTC995VJiKZDJmuqd4jMNDhg9UlEJzBXdfhpzkGsuxSQlsbS6xxabN8ydl0s7jlk01b4XDY-RN12_L5nc8zGFVvFrS6_tToI5kZGYE5kD2XsvSvmHoJ9GD7cV_YIitmC6yOtXUTu9JeRaOEQm22y5yQ8HSmsohDY4lEmM0BQ13RqOj3BbhLtaN8ABF_ClGsCKHRlRh9jMInf5fD6Tt45zWH9pmz7owe8mZXYFnsmeNkDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iad1gy_m49kb4YbW5ZiReW2siUOTJs54NgXI4E0pLFv3EnidVv4MpzEd9lPfNIXS79xXWe8I5wqJBwcTelWxBKiFD_wkZ3Igo11k618dE1iZdmxfOnXry2wamO3TwSxw89ZjX81NWK6Q6VbmHJ4cD0XfszDFuJ_d0j9X1pZXBu0xk2QfTbUCTLXEnRP_IX9Hi1c_ZO4jtqdtCZ1c5cCH1l8gv8t3ts4f7ddcHtlSP5b1qs0OsD0iykvRj2BjfheVnoun-WwEkCxSF9VwNQF-92CnHfLHyW5aHyc4bln9DCihfscJXb-Ne_fhjIuYcFt4tqFPf2hJVS0dUIcc3e6Mlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T5_sjc78-lQGCuvgsw7sMPjQAxufhwjhEZCKTXw_9wYgig4_JCZNSXJKt2nhdxWOxrHb0eIf1YqIRrpwhIN2VOD1qeneKSSCh3iUId3rE2shNlSI-w8to8SnN73G5JkFR_g-TmjsxOH1ftFpRhQKYXe0itTEObMxHIdynaIhqrKSQ95c3JtMPVWKXxs_qGhvtyJpLztph7_zptE9ru4_vCugn6j-mgP6on5qkja3E2wQXd2VJcklKPRdVx1SssCcowK0h9dlM8iUgKoKq7KL55BVQH3qNyzOvveDFfIdhC5Nt_RF46gUhhLhh5atI4zTRlaW0KSQbPE3fpDMGdY7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sekXauvD7fzwRdUzvg-iidWYUaRCSoq9y4OPzS6Q0Z5_oHgdVj2FwJCSuyA3IzimK3_Q8K6fJ4aLZu7IFTcQ3gbnFfLGPILTISnzOULBUv1lxB0uWirsaXo7LJovUpfNj0_k24xt_U13xh7rzzHj2Y0PR4SrkBeLfTjsoEz1lsA0S2MGNQORupOm6Q1FTNY9iOJ3P8O8KJN8-I1pzsTwqb5J-TYTBkWmBdzfWTJUHJymxCU4xQXd7bnMg--w4xdAy0qbgWXxIdhHEjdRuYGcnGupWD5wJzQdPCcGov78nOCCo2QbjG68fz-KrvYkxM25N9BnFZw-5HkIEYNnkf035A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heUnF3Tka34ev1RfumYjUkDPQ0blfiQktePfOxTF-nkg0zMmBVTo_feaxfDCWpuCjuVkr9K_JW-OWFo_NvKJUMBAMz5ilLepCZakGPNRWXKmxl68jS5NW-bRGDdkMGMqX4lZUZwcWTJy8FO-W29eQvHZat8McOA5cJL_TUvDKnUELDj0J3p_AMVsGTIrPP0q6O4M9GvkSB-UklewzAmj60SuqNbpaHvr3EjUNkLVVAk8l8-F7_S26hChoN-qQBoQFfBN8KyGx56IbtmlCzf_1KbfdXnfey62qpUBIuHJz7VHfViIYWe1EWbKVx_ZdicgrC4YZmoAxFfqhrmlXJU93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU79LvQo6ZSN9yiv2FTmKRZtNNCRApYuoXpfvO7qEvYvxkfoCrQq7vpoJky7rg1XPs_FW0t87zf6o_snFrj8Wno2TEV6hufB_CnqwXDjpBtNaP83z1KRpSCSskklONUw0tZYs-dKyvVuulqG1tvxPCaDCeujKsk-EyBONv8nSseodW5kFx3PSq2L1bs_HwgIzMQZH8o5GZNuxva0ILNPu7u4_RTCAF10WVhNhlEIXtogEtdug_NidYqaRwBRrAd7hrnlYlZzF-5Aj0OrOxWNs3Rq4U4efx3eUCsY9ZBxfmTbNlLlSQzx8jqOKpLmMLMHKAhSQKlG4vJUrQL08J2Fqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCXY4mOR5giBNvcCydGjHLSZZ67Mmx9ES2zGSCbSoOSkRbmWsn-CoXe1nbw1HDvNxBpocSFP8xk-OqsyqVLUxtMb4-WYXl5DaonqMIwuRPWPWRAQKUD1i_ICeMqVngkw5HG3w4S38bTcXAMH4BnYx_NiptMDPgKTHMG68tHrV3UvhYivUI1JHAmMqmzle6aPvHlm0wAa_SK8teeVUY4udxHpKgEM_jjt7r7EuKsH3mrkJ2PZ8HhpUdtX5T44YmOPpabw-uHgw92MMUjMDabFPZ0XWd0wIyoo77u4tzxdgEpqioK-qORx0TaAky1Hs8xLXITO6j_PGDx005rfNupXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYrsPkCqcirxYdHfDz8HvF0dG29aWqdQTorf6Wlj8ry6ZAIUvtUlCtrroYpbmdVz61u_gukdEwaVeI0mCimrAoEM2HtF1uIxuE0u4gX4UIkERh9fNDtwblnisWp-Wb9o9uC3j7qbjntNp4CmWyxnP7mtN0ePLrPi9_5E5Y1QtAYqKveH3HxZcTwP9lsVdRAsbrCF2WsL_BX4SOjOm9nx-jxQNQ_WF2Omh45GxeCUJuq7U5B5QH1H7YW97jXEdVVDUEJKuEGcDg1HvDEbc2FevxgyobvjVdhKIJ0jnOFLd4ERle7kH6UwKr4RVq_OJsFpFTDscu5QPP8nK536AKGWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHQWvnhAwLzud8QqRnxof6F332TVjFZb2pgUY0iJC4HY9XS_2MrCEwBc5jmbEdFCMMD34F2UKIDNYWTOORg4tJa_4gDr1Oi-meWdS7iwY3bIFTFh5clCjjtljJQa_JFplK3OhY5Vyt0PeMt0jFNqUgsC4mRYg96WLbbpT3_GNO8MaHJFRlDPEzXSnNMgbZd6CHGI_jamjg0MrBSYMuYPL_AuX3YTRf_OjmEUrlwqxVCfx-M32tW30SotjRGtRffO6zfVDNBRUWTtwcqG3YMGOXkQ9kWG93MIzBxPy4F5-Us3RpispnZwurisVsAuVAYD4wVDHSuZ_Yk7t8uc0m11ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMeUxo5l56w3YHYIxp9oOjxy0rRG2EXssk4IVba2ru-KQY-5fGh-UBG3gCb5Cb0IW8CUMXp6gToORw0Y9h6apcxyxlvE_XrYaF3Ht5Vp59tuO5ZJ6dF8vKxV_drPYcHmxCWtU39d0HscY-xXambyXMc0n1Xq1Brn1CEB-tKMtfw9zUHEJxKexzqaCqy29hgf2yuJBQzbb1rFq7_D57DpwMoCD1Tkxp3CtH9ECM1gXC0SsAOAmqaFO_c7kA8Ao-Y2mHKj2iv4jEj0lUglaPinhGZrFBaVuNZfkcidMay5FnZmi3zvYuQEPtqoOzbuuj1je73xxCt7tIGHlTN4waU7EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfkLtQQnKWNjG4m3rzbPHGYEJwTLdS3hrWWztUqR-MLslB2CiQ-XRmcaVVf37oQWPkxXIvpCmwjJH8O3-odckr_Qjy62gI9aP_kT-Lr9j3x4ZQllxAbm2warRRUa-s2PSPLA7U0oxwHqFXrNYDa5J8CYus_o_82YKfDohTv3C5Fg4cCB74-FjGieZBLXZzvglPz3HKPNJYRhRYevk4jZ8u_qk2C1BcXVoCtfXhcRmSc-n6I9E84x6vAmpAsx2-P2gy4ZIl3ekfjOYtJzqOeR0CCUCcF4mxmPBNdrqacv8lNVxhqoc1I-hdRlqFm2c3M_yWRZJ74wM1e9ExoIEs8hfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XabWancfH7Pw-Gf8Uu39E4P7S20lStfC4l9BeDp_vWnOp_LaDgpACs2GPQKe3uM8IHAxtgIzv-SyboH8CpTOqseqBwptbu5RlXqE7Bl7_VFDx--A8GGyCyQ7kq_jCWTGe-8J-UDfmmuc2gknGXRyt--99-6whh7trD3rkHwkssynlFA0fNy_CXtVPWMTbSM0mmYcXLUaHneyGxST0UobYYTmHTHT5B7UEW5i0Qd3AlzCpk976R_HbekP4prP8wi4BalXq63BezBJe5Nb9hSG4GC5IIk5-iEYrCVdhWn3rjzHndpA-9aStDRjrWWQZCQcbiSVoni1eAljBpQCHAqABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRqXrAMV5j_EHy53ClzXoyCcxwzfqutU0blTelPUFw8RSweGQMgXWOgoMv8oB81CDEC-SsFbLREsGdFEcHy69Z6mguLzMh2VUezHomlbp8zJC1EMEYg-KOZID2KoOaecZF1x1j6uq1bjVmQRmSONhh6Rhqg0aZVzeodW1yzBYmSP0bQYPRxJ3Qd0VuywILHRr7psm4TQ23bG2GlzC9GM7_6vk928VzJ0APsb08vIQWF2FJtQDfFRfSOY3Ud3fsI1e7DDTWp1R_k6RB8dTINK0yLSqQ5aL_8r_Fm5y0Py3Y8ySURyl0OAo68kIFMPDvRXeZtW4LuaDFWOY3FTM-NCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEIIXynbRdStYxmB9YLkhFChL8sGRJFCllyK8QrLg_ipBjU_Ql8MbjU_M3v5yr4-kuXzJ6RdwsDf08U4YKz0K1V28FMg3CRi0Guo6Ka9dUhhnwgsvyg_PLNBk0KAEzsH-2phmVstr37Hc28CN9N53bKJTzz0Qjww7fiLR2Z0YP2MWZXcuteOLz00h_EkanwIR_sNycu-MFLktpR_oWhAL6mBopvcwgWF5S5qyogH5E9dwToWPX-q0DGbaotfbEeMA31Dm6z28modo6VDkoVXVQix-em4wt7Kj1ikyssjUsAA9tW0GTrrDkBlqq1g6E0DOxo1o0AKjMslE7b_9noDJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNP-4KWV6h18eTsszkxbBTUV6nj--QwQ3BOrlf1Ha5lM1FnFc9niMD2Vi2vvWtCM8Ez8Yfn-XDvwULaEWpksY83H6HLEVb2nZs-Ll2OXM2O6Wgikciw0rQh7dtrJPoyrggCraq9Rs2MVPkjjIbscciZiGoUn2Bs8GyK4eYQCoBeMOW5C2OjbMkQxRWU_k_MQ3IDX0YWqtCPYVgiUHEjjoqot23o8VSWGp6vE5LjKg34bjeMftf9XLWB4P4vEmY5oVei8tEZxr1B9AD5vBhc4_Y-ioq7zOoGkh4Jqxuo--BQhYRwezIv1rQXP_WEwX7eNpYwrs1YoIYzZ7IhnPlRxJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfY2quNucizQNacm1ERSDNPJNMuBNbB8yRyifxtsMvolGElibkNahzVMPMQoem0HZnHY07ghBG2QJbI_c83ypTJq_HCWEfFXIDF9dgsjTx9mWz5e7HhplRGiwWz7hBuSWpT8G6kZ2c5gc7X3L85ZN5Kbw1oTK_lHQtdPkJOX881qoIB_Fc7QWFAu32HBSlt8EllYg4ySsWPMetwwkJXJV0uO3BkaqTBrXvRiBl8pamdF3jC37-MYHTM9mYWo2TdG3x8XD1klnEAUuFxw23ayB-z_PunWOpKRb57R4IgGYntU-mNrgRUAnVJOuNhCXmstPcTU3-ybAjssH8iD65MtsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfzqh7ZmvS63FfEoSn4CO2vuLc4z29DdBLtFbpQXLstXHxB1k2O4kXNZgrKICkEZKw0fHFCjDlPRoRpnzPAsQ7QPuxmDWVgpl6WbjDmTCxqO9x8C0DfEJ_W59v3sgdXrwYotHE95D-J3COglYH3RpugWL9wPrdMmGwBdldrxvIe9MMNJkXgf7gn3OpoBKj9lGcdWtTPsBTPFEmfO3yDDhpx5GhDsWgXK1TQWj8i_kjQjvg0wP1vYfvayntD1TJiXpZiP3V678boMYQ8IAP_lgJPATbR5I0O8Tq36Cn9uWM0r1UGNQ0EJcZp8kytMoeVuN2Rr2bH7qWvD5_nwe-xE6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mCDp7CCaxKpgqnp43fy7m__1wtxnU_5k4c8M7ySZBZEA5r-Y0KAtdsxucHnZfzKnnGnb_ksUZRe98-hnMN17S4Z1sBpESMf4dmo0x_VAAsxXweUeKJYGa9Jz1ukqvG1LM72A53uIbxwUE1lmWObzojQfJeZrZG3XCrZceDkCWAXq9MKxRfZcGWjLlT2FS9roh4NzXA83ZBeqxa2NwsdKatg3ILgWlJU4s4GcdVYJx290MWysomQnzrQg9jVmD6znzhTtqBU2Jc8v2Su2XtaM27XofXe94x_0vijLJGiz6vFTv5H5i-j7MU9kaSBRh2pktRzch-0bk9uAbfFJEmuzaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=DqJRRXiwkpRlEx9Hdb2J8rICn6tRVN5a7NPLXv154rHg9K9lvdLVmLYg1By4GM9WqLRkcpRvJQFI_Rte1PUsS8BanWEwhY3C1ENzecggg-1FzzDJxtb1BRKICJNgj9aKQI0bmAbsTioTo94e0zGtQWGLhFDliY0H5SiCAbXnvk8aqtdob_h--oqgjW4RWtbBrq3w19HA6cYA8ebtzhaQidEQvL7JwGGIZUgsLZegMRZzk7-ZsvPBATrefo8wFybYhmAtzaeC0pOoPj-llviavgQdagRJlLe4_1_cIHq3gUR3GqcRMp-ngnFHuviwpxqamf40vI0X48XQeG3GhTL7sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=DqJRRXiwkpRlEx9Hdb2J8rICn6tRVN5a7NPLXv154rHg9K9lvdLVmLYg1By4GM9WqLRkcpRvJQFI_Rte1PUsS8BanWEwhY3C1ENzecggg-1FzzDJxtb1BRKICJNgj9aKQI0bmAbsTioTo94e0zGtQWGLhFDliY0H5SiCAbXnvk8aqtdob_h--oqgjW4RWtbBrq3w19HA6cYA8ebtzhaQidEQvL7JwGGIZUgsLZegMRZzk7-ZsvPBATrefo8wFybYhmAtzaeC0pOoPj-llviavgQdagRJlLe4_1_cIHq3gUR3GqcRMp-ngnFHuviwpxqamf40vI0X48XQeG3GhTL7sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/us8ma0clILiZt8TI97hXeE3YdNO3QnCc_Si58SHieqX0ONXLOU3BfXLTRdlty2_2DF9tE8Aqcum_9i0kzzvctG7v6eftqFhG7a-djOOP5Hd-RtKxqO2Sxc-jkQerqXDkDBLRwLnqqe7QOueU6mnbbrtWlT5v5fSQaubZy5mhI22Gpw3bW-fj68AeQSAcgX8XCh5nsdSoBLQzsGxEzFn_6rLI_zyAGxVHYpJNjMvs8P_JOAO7_ASTAV8WnhWdZaiIcTYv7J3ef3Dk-S8GLIJ7xWfbKKYV0T5MFfoA1ruhzbvWwFrSZP0fQR6cYaFn2B-Gbqrt8052OacBP--mzakjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=Msu-QQCbmu_BD6KUzuLtLjIRdvId6ihf_Pu3Fz5xss50MrM8g4BVudlihGSY79WXZ8ftkq2s5pqDSIqw3CWdt0MiUZl-0DhD2IGqKGIFP8Ol15GgTaVAya-HynkNPQEbUiIrER0XW1kH0LrZSqWAcibYh4MSJOkA32kBkfdrzUYinZUrH20ZapKmdBg-to6ghGUFhOhWuRJ5ncRZ2RVWjvE5xBOpt5C5y3rQg10jDzNEh6bqZam61RibijrLZkbFoLWTsd7PnSr6cE5w-R9MHyqW-GPiGxf80jxCNZgfJyXo9KJrzcsGZfa4f6kvUreuJAgoKQNGqPiCFa1r-f7hgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=Msu-QQCbmu_BD6KUzuLtLjIRdvId6ihf_Pu3Fz5xss50MrM8g4BVudlihGSY79WXZ8ftkq2s5pqDSIqw3CWdt0MiUZl-0DhD2IGqKGIFP8Ol15GgTaVAya-HynkNPQEbUiIrER0XW1kH0LrZSqWAcibYh4MSJOkA32kBkfdrzUYinZUrH20ZapKmdBg-to6ghGUFhOhWuRJ5ncRZ2RVWjvE5xBOpt5C5y3rQg10jDzNEh6bqZam61RibijrLZkbFoLWTsd7PnSr6cE5w-R9MHyqW-GPiGxf80jxCNZgfJyXo9KJrzcsGZfa4f6kvUreuJAgoKQNGqPiCFa1r-f7hgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laJGOQNa_OfnL1c-9Moih-7IugfTIVZOLBoewIOFyNkfPsgg9VGyTMWi7eeAo2TMRx0fy43b7xxoT_rU7PJ0zcSSWtxThSHvuKeKErBmN7T4ignZtmu4Os48ajcIkwp5MsvOQvBSp2IAJ_AAuZcLmr4JLsCmrn8KmjF5IF3A3APnJjg11pYVaMhxe1_L-pWzjkQM5vUIvkvxLxMJon6IRdaZEOJX1nheRfDaGZbrXzC5MfczTPhAFJ4O3vD2shBKYm9uRJ_zQ3TC3i4f-tKgrjQ9_Vm4PiPHrbvnqT6VdCxQDu4sbK3hvmok98b0z4LO37FZF5jGyVHc-kXKFixyOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOfIuOYUWSNv6cU1iZzaZ1TsKFhDgdu2Hq0Jsr1WF-pnPoFiHV-6g9AzLAiET1w0jSJz4oT_5qS1uSV4yCKpbDwe66Gskmj_zGlC95vO29OtdiwKI4QZZMGJ3Frgh4phr8GZbGNe7I8k36g6q7afx6AFbn4iyZnc9SiOrPH1UJ_T5QrinUPFRjVDJ-fj5mEMY_XLJvPE5nuXBIUF1zcp9Ewg4I3EIHLPXDghwj-AKq-lnUg6NKH_wNg9A0cTFO-vxppTLoly6NNRx0ovZlxYbCI4ElxRjC_gN2jBCX-X3CPYFVaWqhqlsna9E4yzXnJYBBqgH39Jbz0VtQ79IqDSlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=mm95l2AP_kt_SKaIv0geMZrCFXABvQlzdI_0vsbvuRTHuUpdlrVgBYWgLhh-R97zbFsPqNV2FwYh1tMKW74f20qLIAhHrtdWp8R36jVySobULiwDF1pcnaqcCV4xwht3PfyZ2-8Bm4CR3yH1aJcueq2Zd-xUW7cURC8caV2_ae8J7VPtj7FP3GkzpOl-lObknDUDlKP7qcLWnlbPVNXdn25TJdOHz4VY-t-qXtClUaxOW93iKoSER71jVfVebeGZ47mMDL6tOGJOcEmCIl_vQ9otzahhdjx_VO6YSBytO-f1PSawuIvhtaoM2GCp2WcYsCMU6H5hGXgcGjMbS6hM1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=mm95l2AP_kt_SKaIv0geMZrCFXABvQlzdI_0vsbvuRTHuUpdlrVgBYWgLhh-R97zbFsPqNV2FwYh1tMKW74f20qLIAhHrtdWp8R36jVySobULiwDF1pcnaqcCV4xwht3PfyZ2-8Bm4CR3yH1aJcueq2Zd-xUW7cURC8caV2_ae8J7VPtj7FP3GkzpOl-lObknDUDlKP7qcLWnlbPVNXdn25TJdOHz4VY-t-qXtClUaxOW93iKoSER71jVfVebeGZ47mMDL6tOGJOcEmCIl_vQ9otzahhdjx_VO6YSBytO-f1PSawuIvhtaoM2GCp2WcYsCMU6H5hGXgcGjMbS6hM1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bD_0e78b1k1e_rEX7HM4qhonSfwd26WFahqsXqfVyr0nOhKAFSB4Gwv8ApNtPzS6KR83QWdY1jF1znSIjFZzfjUBCrTrnzk60U0joWk1a0fn5d6vNN0508lTVuIOfEiB22mv2g0yHEPKIOhcngRQvWRpV_vYmoRERTqbZb_ESUpG7tcEALDFeH6T-SwDE7vdKe_xQr8GlaLClMclAMkS411GYESv5v-EBtIQfM8-5JavNMVRSppPOnyaF1cGWP4IsFfoLm6N22CT_URiBTJIXgWa-KLczA4K1QTebKmhH2UcRdIFTHmI0UFeH6LPyD1CO5O3a_cF_bZmICp-2dny3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F-Zas6CWic5X1SpbGOmcXAlU9KY89H9zSJAatVzoDbXZ1JuNoalyvxxSZP8X1R6ZAiJnAe3Z7xXqx14ez8Yqm6A6W-ISy8ynpluccb3wb4vIMRNfh21gmxJB49KSMmPBi6ZtxEzhe-H7U9D96Uh5vkRsKiGeU5ANNLJpJNUqs1gUsyR6ymjxxABARU2D15e_z6M0-_N6I4Y__ip5eNLDDjCs_CeNFkTpLWK-XBvuYU8PGJxwU494QeS7-1lh5njT0VHzTC8UQi0_xlUMMrCz9aEL6JO8mjdaxNoj_WUKvmvWmUtcGxkGBaNWAw6gDxzTajHqckPY-xAleEiypE7p2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH2ZmRk_t7KMeheOJMhmXQPBq2DyKR0O-j9Z2O9SNQQYJaI-NmMr2mI3jdSb-ybmcr7rvRMLf0BrCCO3z3bDJwiFmzJo940ML6dwcW1xjPT27AIkVi07N_A6e7_8fIhPiuhzU_CmcR3jyBJi8xMuZ9_lg60AcQQK6eSquCXcZg9XMZqvT6F-mumjvCo3HOApUl0KJB0GmuEG8SJH1oYAZK7XNh04gUvoYHvIG2u7oEAys5hOlnPSH6O6ygjf82qav2nG-0Ea924OzvFo-f_V3X9v1PzSBfgD6aROMN6zWQbMmL7nKiMZ1JPrMQa5oSxbM700DFpQqDUcnY7havRdTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=UL7gwuGK81Bs-ODb8enpAdRkX6jhiqRVZw7m7dJPYtVpRhhFfZPbtwgo_4veey_sF_aKUvoWpHQQGHDPg-9qv3x6Jw3tqT8aAhdGZmvBcLgqU0CHaVMYqkho95p5XXiJB_4zJQpMPrQZGv_8rhtXngq3vPVLgk44EvMMVidY64Q8n4PMLdICh2WgLFLVMqztlZiBn9RZbRO2kwYKzBkrCepcyW5STU9Nx88WttY6Ie6gN9mou-dMkZXP3C7BUfib2sIShI5EZDxcu_5heW9tuiOilgI3lYTeDyE-cMR_KmEbji3hS6BNVNI-SBxwjYN-H9835mxk_SGTkcA0fts6ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=UL7gwuGK81Bs-ODb8enpAdRkX6jhiqRVZw7m7dJPYtVpRhhFfZPbtwgo_4veey_sF_aKUvoWpHQQGHDPg-9qv3x6Jw3tqT8aAhdGZmvBcLgqU0CHaVMYqkho95p5XXiJB_4zJQpMPrQZGv_8rhtXngq3vPVLgk44EvMMVidY64Q8n4PMLdICh2WgLFLVMqztlZiBn9RZbRO2kwYKzBkrCepcyW5STU9Nx88WttY6Ie6gN9mou-dMkZXP3C7BUfib2sIShI5EZDxcu_5heW9tuiOilgI3lYTeDyE-cMR_KmEbji3hS6BNVNI-SBxwjYN-H9835mxk_SGTkcA0fts6ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=k9F9Slwi8HjPznWBOi5oY8KPoaUh8WNTKemhuGK73kDPK7JITK9pLyl73fHkifDxLn_FtWE_hXJ5Gr1bPSZOPYrlDeEGepU5g7xqkmE70MXgqPmCTWlrROf3L_4pyvlfla-d9C60xcD5ltY_JSfmdbzQT0kS2FueI-WkWEGjStvIOt62TdS84GTkuVGRti0CgWWjuVob2QqyRAV_jDMas04M5etx8WpXlZTg0Bs_uS7z9TD71yhiYNzpKFWuw50VNAouJb8ArGeHRc0w5UUCbR9p-A5EvSL1nlBQYImlY06EBDewYVhmlOtn7I377aZpT9Bu37Aj3dKFUrXGlpoO2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=k9F9Slwi8HjPznWBOi5oY8KPoaUh8WNTKemhuGK73kDPK7JITK9pLyl73fHkifDxLn_FtWE_hXJ5Gr1bPSZOPYrlDeEGepU5g7xqkmE70MXgqPmCTWlrROf3L_4pyvlfla-d9C60xcD5ltY_JSfmdbzQT0kS2FueI-WkWEGjStvIOt62TdS84GTkuVGRti0CgWWjuVob2QqyRAV_jDMas04M5etx8WpXlZTg0Bs_uS7z9TD71yhiYNzpKFWuw50VNAouJb8ArGeHRc0w5UUCbR9p-A5EvSL1nlBQYImlY06EBDewYVhmlOtn7I377aZpT9Bu37Aj3dKFUrXGlpoO2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iftAkvIsdTjWLeDTpQdAft8662BfAhl7d9jqVlw2T-_FW4DQhJ5bCifYK6BUDkqWmCYiKnPX4ueaGHKkK2VC1F5-zdTj8v7YFxZDgdfGHaLku_sh-dqA7kxKpwnflH1XvYhU-edZ-gdB-KUOC0oVTV46zU-rWhMl6gnPa8mL5YaNCh2cG6gonUAqHuzNNWFOq6evS3DpIz8p8RqNlzZdRhTMPGH4Q0j02i-lgsaGA9IbyVwx_AfxgV4O-k2r_jWGKc8yf01Z7xp1HFOwFFkTAGBCIFAp562450bx9e5QlqbZYMrUaxT615EDTu0NvINGkvLP_RWpvrnJEvWCFDLgiQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP0aQcVCSxn7fRJKjgGYGu9HulDT7Q_1NPYGW4B3fE2Yq3IAEJjG9L0iXVL8acOSso0UiP4GY1MfwPXqcmN5oZBul0eYX7z_YWu30ZOayWC64H-HdJxCxtobcY35G1otY8Paa8iBgRDC5xSl25s9tCjbBA7rvZMa-HECpO8HKDQ0DCoIks5_axejtl9wRdVQ855y-jpJebxJ015XfyNwE47QQhng5DPXnNouUbDyJJ3PaqDZ9pAcSPtMONn-3ChV8FQ7ia8TNqS67a2hlkuwpJZNkRnLZTIJLDdH_PMLZj9YbInMbK94-n0NlTsYgVAeccpuaQrU4kPwMcnj9GJhZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixgQJ-BY1FVJBnnqAbgGeoFr3G1GD9SS0aeomwqvjvoMzB83KTSOIQyUhjC_dBCGjN45Us2MeG4lgLiNAFKy0x54wvEp1F9OrCX8FocCng70dggpItSbxh4tH9iDdZFaZy29rqtbSwleIbT1XoW5Id_-uOh_M4w4am-KSZ49X_w4qjaV1GpQ6GH3B9TkfRjkFKZw-h7NgyM45Hj5gjp3bftDmXs6kNQfxNgXUZfYOqyEV6nQ9xuiMWSq6eN-5b8xl5WlADbqEfnRbYXKXQAy0RDNo3zoBUYOqypduHNIsILMDohXCX5iiEV6GbpgrG13gbodpbHGBHMEopOZ_rGvvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiftPjTQNsg95X_pSm8NPcsLdTUFzGxwoWhsHsicBX-PTxf2CKfT75pZ2LEj3-iXQoiC4S-5ezsbrnpiYPj2vtwkIO4CXR03KTFst5t164pi_eRQDB05uiQeRnJ9LlxQxCXRpdpnCzz62ylrYrvmWQeqaY-DfXhat4moLj06iw3zW2y6j0EkmVcS3MevZvPMC1t87bC0sR2QkPt746LJnMblVNH2ihA8Xc-MH99js2X3MRGDtBBkUbtJpxQrYxjPrtHUvv6UljUl0gsh7hrU0fEZpTUDuUGtsuoSznlO45BJI8ik_PB2gGvqnf9_N9t3ZCnJcvJUai0WcM4_990FUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNuAO5nkDqi3qS4H1PxoWVilB0vqB-MXdA1RQt-fCES1lCXFUsf3ijSu4UDQm9aNhklAKGH38_pgEgS_p2YBXQx4jZhXftjX1IAlf6A-Bi63NPxTjnFRqCAVtTeeJwUNU5iWs5IY3U39tmrbDDxI7V5o3xG_lmsz2gqifMgnsk6_APWVJvrukZ7mpeGKD9zzJtPG7u212b-nHDI5sdvS-xQLbKP67agViPfLC2cpccAc7s5Gfn7hUAtVd7ZmJrngzZqArNxWpazfkNF9k7eR9CXwdvZIyEa5H5Jgv2zwmI3nS-4sDucJaTESmvG7_7QULaZWeUeCDrB8zZbgdc3wpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DK4fQiDCxk643AQd7ryLEHJsYZ_1MEnfZjy3T4SacsHgPQkU8QR5MT3iML8K9qwmKyzZTF_8qqMYtDyvm0HNafUiXbKlSYKHXRbkBSVSOfCvromZr4JKVzAF0agplhHqsd0pliErbGYikzd0-5DaVKr8XbYNSZjOVdXEfdpOHUic6cG6hmy_OvpN9ObHcAg-pd0ZsdIwrerW5fpOnzON1WIGhI8xDhIh2tjXlQeI0H9fzEMLpXIx7Uvrt0dVEWgzUgx0BBCET8P6HLwfKwJKAT9Hw15EkAQKeACO-445a0_uYuFeQ4bc8Qxa2ABmi2zrFFqKah8eRAoEVpd1nMqAzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2ge_4V5kvDvAZT_QmP8D-7NzRJEJq7F8suwfaD8OScxT9Qhr7Tgll2K5VnKapif3ZJ3P0Yrauws30NuxMcJUJYCxDQPlB9JBd0NxulUNRHeKuwmoE1o0EkHINJV5EszpwCFC0JSYmob9D73tcJCvIye_9NNvN5dCuuA61fj7wH3F18ndz-HIGFW3bgURxkRkE69PXQH5AIFp4Tq5D-vYUhpOovNXppgM3ScWjWapQ-reao3h-YyH1p8BkpZjyzEvXZa9qdLQJaLLrxZkN2t6F3LneI-Miv_nJ5pXhNNGb_YifmGjsC-wZq-Fu5v7g_0NjKhCs8IhT4nsGIkBe5cwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=pjB7wkl9GzQDVqfVRCRSP2O5yP0GfnUvfo3SsxKCoY9dsllHjZ1iXCdH_vtmFHNvwVXUElwYZhR0BAaje0L2kEDIKQ42gmjt1mBI5xQXjjO8IBNQcUd8qAvPUzlUInEaInhSQ4N20cGYRlLS3N75WUmPZE1VOfFCz8_sMOIeo_Y6t8HMVoneoSwUt93UfIv6FFjhlRapFZMDfptfNBa4Kc_RYTrx5DB8zZ9KIo0Ru4YJyVQW0iWr8nn-lrZDqMWf8i6pE_2QHKVSSM1b9CrgJjSRPVuXOigbYku-nk2Lr5j182pZGVFBY18b61dSsCNnxPjx9xY3RZoRr-EKdUlJcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=pjB7wkl9GzQDVqfVRCRSP2O5yP0GfnUvfo3SsxKCoY9dsllHjZ1iXCdH_vtmFHNvwVXUElwYZhR0BAaje0L2kEDIKQ42gmjt1mBI5xQXjjO8IBNQcUd8qAvPUzlUInEaInhSQ4N20cGYRlLS3N75WUmPZE1VOfFCz8_sMOIeo_Y6t8HMVoneoSwUt93UfIv6FFjhlRapFZMDfptfNBa4Kc_RYTrx5DB8zZ9KIo0Ru4YJyVQW0iWr8nn-lrZDqMWf8i6pE_2QHKVSSM1b9CrgJjSRPVuXOigbYku-nk2Lr5j182pZGVFBY18b61dSsCNnxPjx9xY3RZoRr-EKdUlJcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=QjWoI09AGn5xjH5I_tDhqZyBnlF5DSJfXIVzY7z4sLdnuK68u3VYEenci0JeGoOXTJlvmXeszDi9YMDsZvP0rFa_SK7qXbF-AC_goXikxCgCH74ooW7hExd7FusLiVQYHI2NTzNSnCpqPS9CF9CU4o6PVx1XRe2dirgXzwjjbUAV2miH3Qq3DtTT40h5WhXlCYNzSGKfoDH-ME2bg1tdlkiFtNTzBTR4ed-jiM7fgDfKNvw6yZu6bP5cEPIIiz_es2JYNFvchtW5fxC6UuRjmR2xSpxa40_LK6xUqQAEF-f9Tfv_a-S2WF_BxukvtWmtr8wtue1e7bdrsdGvEsab2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=QjWoI09AGn5xjH5I_tDhqZyBnlF5DSJfXIVzY7z4sLdnuK68u3VYEenci0JeGoOXTJlvmXeszDi9YMDsZvP0rFa_SK7qXbF-AC_goXikxCgCH74ooW7hExd7FusLiVQYHI2NTzNSnCpqPS9CF9CU4o6PVx1XRe2dirgXzwjjbUAV2miH3Qq3DtTT40h5WhXlCYNzSGKfoDH-ME2bg1tdlkiFtNTzBTR4ed-jiM7fgDfKNvw6yZu6bP5cEPIIiz_es2JYNFvchtW5fxC6UuRjmR2xSpxa40_LK6xUqQAEF-f9Tfv_a-S2WF_BxukvtWmtr8wtue1e7bdrsdGvEsab2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=o0KEqtyp3RIzizDnAw9MIHoHvKBsTzPix348g5MVusNBn9Rp1iF1WbRdm55X--B6kuzHtHpFLMVglYlECelJFEPzsTOv-ZeR1qUAHh8Kuit5hBY9Rao1aPDYSQcLCfxwbGcufpHtfGXpZEdP-hjahBuY_vWhQ4LPflok86Tb_z9uN4Cvi4UtB6IT43vDuWuUc8jc280LDqY0sRo1ZCDw9jlic_0TdYBEKhRPUKmNuAvm8Mb_gTAWSkq3AK2ZHjuWTaO1dTYelVSUTO2sB3vg9fJIT6EvR9RyJlQXhaJIakKo2_6Z41pw-RXMxqrOTTQezrmqCsQBep7wHixqb4oDzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=o0KEqtyp3RIzizDnAw9MIHoHvKBsTzPix348g5MVusNBn9Rp1iF1WbRdm55X--B6kuzHtHpFLMVglYlECelJFEPzsTOv-ZeR1qUAHh8Kuit5hBY9Rao1aPDYSQcLCfxwbGcufpHtfGXpZEdP-hjahBuY_vWhQ4LPflok86Tb_z9uN4Cvi4UtB6IT43vDuWuUc8jc280LDqY0sRo1ZCDw9jlic_0TdYBEKhRPUKmNuAvm8Mb_gTAWSkq3AK2ZHjuWTaO1dTYelVSUTO2sB3vg9fJIT6EvR9RyJlQXhaJIakKo2_6Z41pw-RXMxqrOTTQezrmqCsQBep7wHixqb4oDzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=QF3GOGYD35S7kEFVg_EWPgj2TwGlnJDPGiWdpeF8DvvQocgx2zULH8oycXnbJFHfD4-sLRuend_3o3BXZTqvDoSMh3E_bM8_TV57P5SmymRv3Qn-Uh0Y5latQ0XU40xruqmb-dR0m1mbA9m10sXIgA8fh4fpO49Q3SY3FcTSTP0MG7fFFfoAHHvqF_CjnrwHRU0qRHcXkM1-gv0hq22-3xUvFzC7fIwzs76U2kwhOkC2qGM1T6Cv8-NEmGX6i4kzRy8FY2uIAilXFaoERbhF08H-1ftUxg9sJbSJXYpHwKSx8nRF5Fp1xI5ufnLwfs2QojTaa4Afk7l9UZlLu1Slxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=QF3GOGYD35S7kEFVg_EWPgj2TwGlnJDPGiWdpeF8DvvQocgx2zULH8oycXnbJFHfD4-sLRuend_3o3BXZTqvDoSMh3E_bM8_TV57P5SmymRv3Qn-Uh0Y5latQ0XU40xruqmb-dR0m1mbA9m10sXIgA8fh4fpO49Q3SY3FcTSTP0MG7fFFfoAHHvqF_CjnrwHRU0qRHcXkM1-gv0hq22-3xUvFzC7fIwzs76U2kwhOkC2qGM1T6Cv8-NEmGX6i4kzRy8FY2uIAilXFaoERbhF08H-1ftUxg9sJbSJXYpHwKSx8nRF5Fp1xI5ufnLwfs2QojTaa4Afk7l9UZlLu1Slxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=SKPTsvZzSrk-j6nFy0CbwzxFWZ4jYZyfxSHew3rVZKs4jlDd5F0IswwkqYDUqwb_pe9lDhPGtFiO5PbReVPCxsZiuXl7Ea24Zcdk7zpmES_CZflKVA8bRqlAcM9CHzKQHFaoMUEykUO-4REsWyuzT_UdBNKV0Ic90-GG4oeuaSiSoWi7Bd-qKBqs5U3HehnzVjufoE-IeY5VZeftnJVxR-F1tts6xFcXF8G9mNlpxEhrDH3JW26-NlP5ST53klhRbjmShQge-vPganH0X8kecBHleDHwVuzdiaLDa0HaX19v_Le_J8xlMm75LJj9ozVqdC6b0__EAt0QrRaHVxs7_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=SKPTsvZzSrk-j6nFy0CbwzxFWZ4jYZyfxSHew3rVZKs4jlDd5F0IswwkqYDUqwb_pe9lDhPGtFiO5PbReVPCxsZiuXl7Ea24Zcdk7zpmES_CZflKVA8bRqlAcM9CHzKQHFaoMUEykUO-4REsWyuzT_UdBNKV0Ic90-GG4oeuaSiSoWi7Bd-qKBqs5U3HehnzVjufoE-IeY5VZeftnJVxR-F1tts6xFcXF8G9mNlpxEhrDH3JW26-NlP5ST53klhRbjmShQge-vPganH0X8kecBHleDHwVuzdiaLDa0HaX19v_Le_J8xlMm75LJj9ozVqdC6b0__EAt0QrRaHVxs7_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=PbmxoC2AfCR7Bry00wFLwrsROEb2eHHt-BgmihEr7dqbnhAb95WzghTQc6CCzHF2nBEEYMgU4uZSa-zieSwE9Dp5mqEBA6bCLEnr32k-LhkfzHrQkmg0z2RkTiYfMhdIdp7lEKtDvCIsMx0saVBYAzdt4Z8doKkaCAiftJpByNnVqa_yZYK1Vu9RG2zgFxU1sVw_BA73-7bB9kkaofOwkgTrj7KHF4Dd-fCTCNpowwikdxeeOJpFjO59R9vClB8hwVa57vdrnXDIUC6XAWu49Ilrepe7dKSn0hneuW5XrJGH1yUN3x9OMKPqHVO2aY3TVYVQrmJuftHKQMru-IL43A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=PbmxoC2AfCR7Bry00wFLwrsROEb2eHHt-BgmihEr7dqbnhAb95WzghTQc6CCzHF2nBEEYMgU4uZSa-zieSwE9Dp5mqEBA6bCLEnr32k-LhkfzHrQkmg0z2RkTiYfMhdIdp7lEKtDvCIsMx0saVBYAzdt4Z8doKkaCAiftJpByNnVqa_yZYK1Vu9RG2zgFxU1sVw_BA73-7bB9kkaofOwkgTrj7KHF4Dd-fCTCNpowwikdxeeOJpFjO59R9vClB8hwVa57vdrnXDIUC6XAWu49Ilrepe7dKSn0hneuW5XrJGH1yUN3x9OMKPqHVO2aY3TVYVQrmJuftHKQMru-IL43A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=Uep8RiYsVJwfdZBRcmMsaYChGvBqDffqs1E5mdn-LuLDOIkrK6bt77KEgNCGmlKkV_YtK4jTCDfk0l9ZKyAyYHR_selSOIGkgwPp20qtxfQTeKD7eaZYnpq48VwYyTdiubdSE_nASgi4Yx1jU9rHd3oO5G4Km05VL7LHmrf61paWZbK-8XgJmzsd7D91tLGNSIlJptCVZVfwbH0YDSDtaYxiSFgD8-TmQoKh5po7MZKFGJr2ceHrUM1-h0nKBtCWaVh5b-lMmAbGcV_Y9Qr8VChk6_TY3EBtKWUzxyYGzJvYv2dzJjB8A6uelMqZykJIj9DixPJBOtFxPF39eBtrew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=Uep8RiYsVJwfdZBRcmMsaYChGvBqDffqs1E5mdn-LuLDOIkrK6bt77KEgNCGmlKkV_YtK4jTCDfk0l9ZKyAyYHR_selSOIGkgwPp20qtxfQTeKD7eaZYnpq48VwYyTdiubdSE_nASgi4Yx1jU9rHd3oO5G4Km05VL7LHmrf61paWZbK-8XgJmzsd7D91tLGNSIlJptCVZVfwbH0YDSDtaYxiSFgD8-TmQoKh5po7MZKFGJr2ceHrUM1-h0nKBtCWaVh5b-lMmAbGcV_Y9Qr8VChk6_TY3EBtKWUzxyYGzJvYv2dzJjB8A6uelMqZykJIj9DixPJBOtFxPF39eBtrew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rId872ff_eFodrPNyOFWk_r75LMeqrmPKIN0qkw-UXH-gBC61hgGuBxuQG8Gwo0ZEbSINesvUB3aYMQp8RCYH5ySyIUdjQ_kxyU3bvXwzlbzANUW3DaE0QJ84vcpLxvp7E6im2tuh7bLiSs7yTfUjD2N5FMHewqzPoKYx8wVKWb3iG6qtyOiYtjyPvlKowGvIoiUiL7vfHKgdnvfYn1Sau5ALSJ5wLNzTbHPldtd0jQE4OuE8lfLOlxZ6RsIV9PWfiJxK70VxIgxDSwqOVKIoFRDSDRXmciv4XHeWNyXYPwizRkt_3TvTyQ1klpdTN_OCYUpnj3M6nY7htnhzcy3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=kWDJex5S7xSFD2qL59-H0RCXnm8H0FmZPmILLDFrZdSv8M3NZFK411hAB-1K5TzH_eFE7xYu17PghucnemnA1BASHBTdRl1lUhs47oWndBEcINZC6-QNT4e51uKMD3skI0Fsk_LwoztMPV7On2ULRX23c-vBOcx24E5_HWdwGGW11oPxaiWtvq9BRSHL9b-ofxH5oTkUDKhQUCvK89gHwiuexpTvoD3Lc_WLuVqYLJtkdul-i1ncylJWzkdryom96o34Bvp9-IEh6EnXMX65aDclxgqMCvZ5-9HFzBtlolcPoOY1jLHJeLKSZtwmhrJguzHcDTky05bPRr7AHLPB3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=kWDJex5S7xSFD2qL59-H0RCXnm8H0FmZPmILLDFrZdSv8M3NZFK411hAB-1K5TzH_eFE7xYu17PghucnemnA1BASHBTdRl1lUhs47oWndBEcINZC6-QNT4e51uKMD3skI0Fsk_LwoztMPV7On2ULRX23c-vBOcx24E5_HWdwGGW11oPxaiWtvq9BRSHL9b-ofxH5oTkUDKhQUCvK89gHwiuexpTvoD3Lc_WLuVqYLJtkdul-i1ncylJWzkdryom96o34Bvp9-IEh6EnXMX65aDclxgqMCvZ5-9HFzBtlolcPoOY1jLHJeLKSZtwmhrJguzHcDTky05bPRr7AHLPB3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9eRuPjUup-DcKqp7Sr4oP3TR38gaPZkfDXt5tgi3S-L3brpuEYlrN_1Isb8QQJX4XpnKUXaZoCgVzVqQqCr0TfA_3x2BC0QCXB5HUWgEf15T8SjM77VhHOsapnfsMAJ5ZTE9jTUoJpI9M60yL-ca04mFsu5gcz7w4D9vU3Fv-iryhQ1ZcyNBZDnCpARpVO2nMRheS8hzwucsqVku9rI3rFuA0wSfR_wPaR87vC6-yrCVnB_VIHj_UAlvnRiAF34yVl80twbzsfTDjyaHmC0GblVEpey7cY44xrHuZpBbcjFacXjDVuhbgQhP_OeCtgMjtnKKlGya-UlAUfS_gEFlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KAmqBpCnfTT8GcwyTJhgElDpJV3VR3u4Af7IkIhTrrmayYTcp-N92wmylF2NYn8bVoD22334uF7sT1gQYQYqUtukZO167GDLbOy4QarL5y9zjUdwWq8IiEM6xm1Hr6IQ9EUUjBG7yLZIrzFDxFUbNMolLWjzcuWURp6Dpzh6CFBrqi_UoyfvJVg47L9xjl7IBhEV4jo0aiLVzD1QU_2vI_LBJ_02_3T43kCGH6iqaxlqC2tKAFt2hNwY7jRPe5eBJJAit5o90VMoB71ejaSc2ygletkTUX2wr-VAKOQh2qZiM3ze9ruMMAITfuJN71p0d1WkD8FB3r_Tpe9CpTCsew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HepDxdP1Yv2HLxgM-IBoQmQaCwTqOc4PunWWL9tlUOg_fuRIAKrK7f8R8L1or39CQr517EDbuxfqoFfkoKmBUnuXfX0xh8DsSL0wmIjxgVKXkWhAa8fLluyuC8KtzsIo6DjIUusLe_BxXDtFLryAOxMZp5ORG5qtJJKfcU5_uLSrM15QYxOAUU2PtpNX3ecjKtXgoSun_Tyhtzcbwvvnl72jsC-qHeP6uQ6thDJmaShRU2oo6_GCZkTt2pKhOZkxxwzLu4hwgz2fNE8siQCzlz94u5wSCnQDYHBmzkS9RIbJz0CZq6P5foxXUvymrITmWeoC_UViiKvg4_IZv_DXeg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H6nmN30wpFlFvx_xCuioBjAYBacazGtLtGlJBQuGi1e69uk29ngirOPDo33sHKcpwHhPXj0zTny9pnRWBd06W2PvLUYxcCxAQqPq6uvtEiF2tA81Sa3hjmy1BUj6i3S5sZyAIDovLRa3AcFjEDJMj50RGvzC9GtfSaGolsy5nCs3WVILUCAX4bJLU94WLezcQ31iNQUJ9POO5IK527MZ_ZcMNiunHH50jpitFqhTU9DOl30-9xmGxc_mk5J61ecNlO37-HbSI4PImkcDuu1ZPzTdrzQsUZE-Ih8iS3rf9TzWBpe4sG9jApF4TmTmjR8dsHfXgH9qjMwzpIfU0IhsLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=iJVAKqkJAmJg8nvGysaYMotSzDjyz6uzq9gee_k23HWdnbvSH2fRpoivrN1BDkk9XrcfSY9owTjWEBHQHgRJLb2UI5AzYlVBz2nkzW4tujiBqbpyT_wczp4wQEVR6hkqp0se7JNAN-O2hMdDm2qt3GLkS9e6tn-mxBUsys32XUfede35LQpLPW4HjfK_MQCA0V1bkFu46B2gTNgdyMesM3W-4t2sMS0pjgz44mpRj_y8MIiCR7y1GrrzftzpUkWaMvvhiX1EsOGxLRa6O9Qmaqf_BhVg3nmqBh4ujIpfKzBOdYsf1RmL_bitzITAZxkeWKxsWZmsv6xYH6_FTYqqcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=iJVAKqkJAmJg8nvGysaYMotSzDjyz6uzq9gee_k23HWdnbvSH2fRpoivrN1BDkk9XrcfSY9owTjWEBHQHgRJLb2UI5AzYlVBz2nkzW4tujiBqbpyT_wczp4wQEVR6hkqp0se7JNAN-O2hMdDm2qt3GLkS9e6tn-mxBUsys32XUfede35LQpLPW4HjfK_MQCA0V1bkFu46B2gTNgdyMesM3W-4t2sMS0pjgz44mpRj_y8MIiCR7y1GrrzftzpUkWaMvvhiX1EsOGxLRa6O9Qmaqf_BhVg3nmqBh4ujIpfKzBOdYsf1RmL_bitzITAZxkeWKxsWZmsv6xYH6_FTYqqcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsU9AEg872OZptDF2dMbdg0vYVJ8mZDtJBSxTBWlaaKnAmMM_6IJCHuFf-8F3vlSvRuZQvmhk7GQcYA4Wc3rHYPuj9fISK4qPj5QVxXnMcpevck4GbDmUOS7u-ehtM6egUjuyKEgCCKHcy_9bmCaP4pyoVMo-bx4Sg_aZ5mXY2iACMdk89UaMLUebz08JOTV4oFLqWueqK5rW0eeMTRih7EI0Q_47xDVKYs_FCdYjrDD3mZasywSun1z4oqi-3_2eiZyu9-Yk6AcPINs6_5i-eBm1-7n2EvanNLevIFO4mpvNv8206TwSm8DjvnlrkzBGjrvCgBSXvWSzEj5BYoYKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=cAB9SgdKgnUk1qoi1Tw9EOhN8WITzBiUubYehuBK3mB2lurDGW-xOkTE6CLrY6GV5AWlrvu8I8cvhAVbf8HvCy-0N_jRC9MZAjFqND33CV8SWNqFTCA9fGprtMxY8CYAQbgLkHB9xETMUJaAR0WjI00xW_k8v5l2229uX8dWbumVEA_v0erLDTp_dogeOkMuI-z1gvuT6Wo3UgATlFtSOreeNVVfH_2QisSBOvcGY372LAHXZrqUbnNGVpI0waLEuNxyyC_vAEXwx7iGvCkkn83DVSJNuSovCXkBCHZIfAd00jnPV42SReWT1IN3r39nEm3JTht04vMF-kq6YcK6Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=cAB9SgdKgnUk1qoi1Tw9EOhN8WITzBiUubYehuBK3mB2lurDGW-xOkTE6CLrY6GV5AWlrvu8I8cvhAVbf8HvCy-0N_jRC9MZAjFqND33CV8SWNqFTCA9fGprtMxY8CYAQbgLkHB9xETMUJaAR0WjI00xW_k8v5l2229uX8dWbumVEA_v0erLDTp_dogeOkMuI-z1gvuT6Wo3UgATlFtSOreeNVVfH_2QisSBOvcGY372LAHXZrqUbnNGVpI0waLEuNxyyC_vAEXwx7iGvCkkn83DVSJNuSovCXkBCHZIfAd00jnPV42SReWT1IN3r39nEm3JTht04vMF-kq6YcK6Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
