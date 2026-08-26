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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 23:53:56</div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKc0l2K6l13aEdQliPnwvI2yoAGKD8XqP414ax5EX-8Pos_myb1LT4cDG0Z4u86w-HNglTu4ncJvb8I-XiExMrZDufTcV6wFxspe5EZU_C9AIE2ASUcKFPcJCOAbWPspQ6v29ZyzZAWEJuK3syTypZ67cBO2OOvgXMnqp6NwkaM6kTmP2CqQ2IpTsXPEVoPRhaYP4RKcI59ubmJ0-ncACH4oCDqkEsPGPeZs2Od7zODeaNz5G6H9G3mUKm2faZDq1U5QZlVb2H41O3b7AN1peaURLU5vivZebOBKLFWJCLSQ21_vl6-qdDmOttIV5uXIiUqi1v5xWMbnuX3HaHeSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amIwKnkHQqmiDNirSRkbVKNe8tx3JmJ8z6ix3uK8_VpYrxPN33HzkdwiMvYnhGoqmnaa7MV1HYDIZq5N5B2PrckvaQI904ZC2ibEiI17G29KTHtU93OAZoK-jsKp1j5_Lvnhv9T77NY8KllPrmiK_ctGMEcWdd8YHA5_E_An4w3RBufYVZAopM2EjO1EJyFgJUdrJAadc9SYI7dDAV2YBsMheHLtdapf0ijII8M_a8Xc9DD1ZyqBN5MUPA6H36yptWpfQ5uddi-vYxPiOvR3DnQTjS0HDGoxl7q6WitW3Z7ayRvLs9oPdgSZT0n7R3gmhWht3KEPg6vtFqP0KuHb_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0VwMlhjGj-jCMtayS8xxHZ6puz4USywLVcywXIpKW7i1JAbu7vdDmBo3_OqgymdCEtpbq7D03LmD-uoMAGn8r4sU1A5_qaE_8H4FIn-LewBGe6BnGT395CwEvEHW8vs_i-vSr1vOoWvAESGVk1d56RnrzMLUa-1vwLqm-VlWGOvc-Cl1BvCUR-LWSWsYpyO9nf83MqpxUtu61HF4QDgn-K0WGGCrllMgOEOjMiBLZ1-PtoyZJxaWtAMcgwDEgwgUDND7UVgpq5OEi7cgu88-v2RfWWlYARJbrKlwaeBcBef35OkMIO0vBEhgprWXpR_aspn2Q4o2h5f6nJ7GYABwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnDS96C0VTe7J_t2fN3KZ81qFJgn3PTP7zIHzXt1H4shxFi51kF0EcAKPQzNHRrD0mNEeTTbAnAWEUfINB2RSj8rDwK-mY_3934vs0z-L6W8htQqmj3YO7xpiizqgjTZ_S89Pv2rxX9CO0b-l_m7xCPaK63_uU3quv44l7vuKioNhjXbgpAWRnOkfgRGFEEqN3wzU422WOEVYSbDRXaFC37-k3lYvNhzrhPmtxPFmyF3bol27C2NHxCPqUkrD0sz9QQ_TQPRB9sd61EtwC2NsXVS3EDKVBWaU-9SZLGldJwae38nNHVeGA4u5Fo12hbhbR0z61IwC9lKymwvFiRXMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSluHWiqg0kWPOeN4hwGD43U2bfExGS8t4Leu1r26KnsV6i8kBJ7xNsIEZxBTX9NamB092G-veqBqXcEQitoeoHjwuEgPXhXQGo5FS1Th-gelXMnPnTEXtMUXD1JzMHP54vwHHjrgA0Yu5mGDfKuFTGpzteoED-bhGfqykqII7wz8ANaH1HaHhYwEW-TfJJmP8VIgnwv48ndYg5YR4ujHpiElnjoQ4UXGRzoezbjSmE3PSTAvQwJ92T0PAEBJ1z8jHMxJt7MjIkgwXMpl4UikOihUy_vBXaA1U9UB0JAQeFGCMGSJAn-t3EjN1gEQZTMGTb1Da_evLB9SOCVwKJ5SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oe4YQKuxuHe4q6O1P6wAXLFuUz0mJ13jfp5hePVVc4V9Dvox9lpSgkWqzAwaNOPa3cepYWRloh8ub84sQ38eT7c8Jn9QWclTX8PTMTD4x-VGZz2BURS5reFGU6WKpGfIwPgcc11cEDV7qVn9sBmGxTiX2fM-WNwhp5k5OBXbMVTVzdVywIl5Zqc9OD5oidB94tLw6JbewqjbqvOihCb2jz1ABiXZMu0yujq4sFGmvdORvZnyob1q35sZouoZ4Fff1xQ6KOWw59xUIZHspeRkcuslGn_ywACRQUAjTNGdISV87CpXzpa1vZGdvBVeGWkBmYMUSNtUoCDa125H996Mjw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzQF5Y4xOMZr8LTkyEOJ57-AFwUVhaQzpxx9LOlTiq85prI09ygmAAA8RyEdfl4FA6aFBixFV3Y1CRZUglQ4nmn-j4jULcW__hkJsA2qlr9VHYagjeT860cjkGfJjI7SZaxoYi-znw_HehE4jh_wYoQkyhue_cXibcTxHL79OYRrsgd3-6IrVVryHeeUdZuHofjFd6LD0wJBXJ0aJHeIFU9dlGME3x54uptE_n7tVIXWfs0AWnSfebIW51y4VnGVl__7k7FULjcCZeBGysx5vUW-OxmCrc8bT6tlnS7ZeZQx0O63QvV6XEInFlF7OhrTTTv2txIcYOiHFX01zxIH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sy3D2iY9E-HR7E_pZYaPYdEZHDdNlHLbBpC-ALoE06qofe8h4wjOHDYP_rDKnCpvYRhDVptd9Zcc9chDifoEQD--ReVndYV1DTQ1MIVcR68WybUE02NVBBQpcM_Pfe8-orWxCzZSOQkQgDSPL6bfpqqZZKZzZD1kvETieuNBpQcqB9vxl_IM1ieT-qAmjPxNDeBm1isPhI2uCIEWZi2zpScAekEIgp85UDTGKxL5nLld6twV3VMrWQO2fzO5lvXgvTZFqBqazEDOUANuLkKf3i7RQmAVfrEW6WuVInE6FxMp2e7D-ilsqCUtD8-9vU5dxQcMvgkEgcyeBn1bFEyJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENeHNl0SiCrWqHFFmShshdzsjcZCFoGwTcb01Gig-V2HJdEGAFHXCLmY16IIJ9cZ1x8UyvMC4ty9sjM7Rj81rC1XjuSCoeN6iCrLDaTQdacStPndyaB37cTU5k0X5chc4NYoZ1dRPd63xTjTTcGAnB505o7VIHcBoM58olg_kWqlqV6lW6OR5UafXWcflGBWAPV5pXKSceG5ZRaTxy7D9rc8pKfn97anz5gdPSFzZyTJLA3oniM1p33MMY6CP5GJAkmD1x3RNs70-fgbLU0wjpParo2xCYG4OXPyImFR4kIBSk5fMxkDJUa-H__Qrce-RH8SdE_w_N1FHEaox1T3IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO4QLIbnwgCjvc6TG83htcsusfKBfaK1MSLytsyguP1v856dfKS-UtNaU7u0VDpUTttmYCHkPogYJPdBpcqfDrwKWT_Z1wYVvfS2G5waFmIdM5sdicr5Dd1JBD4byMog-9S8yVOcM9UyG3NW_KSi82PqOoGHbAfgwQLnKUZz-h3nG_UzcpGB39PmwJBiNmad17Hgl1Jx4DwWclt9lsDew-ECdHpro_CzQKqGacH0bE5TyBIgQTzeZOwEdHnd8FVIK3Pdtql3fGe6KvMqIAFUg1dAh-Mv2S3dT_EJC7VAZi9k4zxfrVgtrnaBayKQzjA7yScBEuP2KLcS8-_33EPXfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_lZajW6RZBty8VJdp_s1BvtQfDSRuOluz5vrT_vpYuekqvYDRxpPgBABCoU_PTfydLk9vBe1psxZDzWu43o29JJSStZwRpGSC2yZLhHG7Lb1vch67A5ETZROjB6wgdD3xjMiMNgGG3BHz94aS1JNHdFenGqSvVmc8UztqcU_YwTQ2-zr-AhKcXlfdrmCLpn-LJHKmL1hqirESjqH4EM6d8yfDIBDKy2QGBN-oEq100NJenWSmYoCaZRur87RHa1pMYyNTwlkcDRYjUWLy_CIq3em9Jcri4XqInbvUGqIJNv7uyZTnfFjc4824PYhrI2CPT3HkgNe_GeW0f4sUEuqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQ6L2hrOlpNxJaenI8uYaa7bw4c0of6xo4ptXc_1Chgs66I2NQVAqOHijp9sRtAzQzw17YhhdbLvqas8i7xBaDzPNjpvNn-zqpbJQkmh-ZzhZWkV_4D0dZyVBqO4wcP7ezh9j0fqYXIFqlTFI0FBmF8FD9EqxXyz6VYluPsoju4KM5xZhTjSa-wSwXyoJYjB8S5m0ShDcnkX-XyV9S0STPfKfaHspBRssaHK3fCycoZWJ1qtyRZVP8-HD3iF02vdQI-n-YAbNi6dfKoy4GFGv21RXsy7lPt1tsYhGycs-1SQ0Zf8iS-1dt3UHrT7LODSUXUIa80-q-op4loplyUdeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ5Zeh0h_vnUs8jRxcqAmb5MjFAqPDm0RYaRC5TK-CnnZPMWa-BTzZK-CNUvjgH4WtzXh6tLL_XuQAEQat44k3N1sMCNSFHIXrwlI2uCBXOqPLUKw5y7Jne89cD1QShGRt_g1zwwaN5RxaiHtlH2PG2yiUshOovuHtT3HlCV8lnwomyIx97qHZwV18jcxrobn34bc6kg1Xr1f7-e9JQrd6SgpQNGz_i1JI1NkwYmBBtWfwjgLC3DzDk_ZXuzxEAHwaPX5Ffj2hVZzTnMwQx0E6Lo7sG4eitWpJxy3lPE0elUCEnUeIkm3UsIbDNMHit9zcg6fmGps7zOyOpkAyCUQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faZSz7o_9EWT-yAWiAdUydViMoNTa_tR79TlhnHqv7ipOlcI21ctoas2vCoxsiDTVSBMUo4JfeyhvA6-359GSYB7YjQQqFXIuReUqJMQMMqEDYaleRx4OwX9dG4Co2cuoJKgval6PDA-bNcCtZcwNGVRd735r-J4OvdJSQoVDhwGzITR3vuwZz-CQDFJ0y_uvjv1UHCu6zmt6VvVDTVabanwkyV5qtEP8p-jM_wjeKVePzwVvWfcyCq6CfHiCzv2n_f-A7s92VapOcI0FSRaTtvTzC4xmYyT20p_or7lRyWOkt0BqrMoenLjPQ9oE2sTiZsyANn1SnRX2VyXriVjuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1ha2X1Z_6BLPKnzoFomxwtRGvNybOEnmuYU8y7o-5R2_ViwY6itkoWuvESKLqM4u8A12w0qyEdzWMpAvtWblRO46FlyNqJIUaaTePQ0DK9Hp6jB0mDgR5DXahBiro957HCjPUCq2JC3NljaoMTvlDqoRt0EFJgXqkBtpwLW0ZenHovtBk8edns0jGO5WXg4-UD1TrRqJe1jWIdpoIU3OYD3Nd6HF2hE42cnvH9_GdjCkE4F36hkMl3H78oeGWswtkMN7DITm6Rk2apIssZNwxEEB1YFUGb6rrYiebS6d7BXfUiT372m2gqfS39BB9NhyLc8tiJg4zgsRp20Xb7C2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heUnF3Tka34ev1RfumYjUkDPQ0blfiQktePfOxTF-nkg0zMmBVTo_feaxfDCWpuCjuVkr9K_JW-OWFo_NvKJUMBAMz5ilLepCZakGPNRWXKmxl68jS5NW-bRGDdkMGMqX4lZUZwcWTJy8FO-W29eQvHZat8McOA5cJL_TUvDKnUELDj0J3p_AMVsGTIrPP0q6O4M9GvkSB-UklewzAmj60SuqNbpaHvr3EjUNkLVVAk8l8-F7_S26hChoN-qQBoQFfBN8KyGx56IbtmlCzf_1KbfdXnfey62qpUBIuHJz7VHfViIYWe1EWbKVx_ZdicgrC4YZmoAxFfqhrmlXJU93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQxtqeaU1vniCsy3mXsBcINkHSOpjDPcTNYYZdtMJKa5C8-oTYv9oCIcpWhEuSF5hNOoplnbdpMXykwa75LcAiBRYkscJQ5744bCG65s_vkV_nXmvkktQv0Bq4fxNsJA12ZGuJTt8ZwsQi7j_0fmrGGVUeq3vQCyaLD7tNF3MI3BUzgqE5CuizJbQGkDno3oN9307CBlKzIoFV02ptbRmvETRxQPrZcNRJQ7aywJAZrvuoEKhNSun1MtJdPVZg5YhqvC3pQ23YJEuek40sqA8PvEoalQDwQeSC7wXgwcRFbF4XKNR00rC91tgkXVA3PHtEg1kKw1bpf93ZL8NuUNWw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbxSzMtCOrqgHneBWb_fMiT2E5JuACagbxxwZh_yxgjK9cn_qAPWnz3OWXOCB0wXLC4puaqj5wHCdrtkIY_trN0hTKPOM3G7XGS9d0bvt_YbB9PreyZvUox4dHdJPyRMJ3AN7Qja9yEpFOLYpYJcUPDtdkRd_A6i-mUH1TjYGPHO1jAGrpadLNfaP6Xu0OoFN-jJhyVtxiAXCyXZpBmignQw8KT3iM7iATAQx_3uB57yX25EuNBYjSU2k7W29aog6qzNR5GXifwrpCea1DcDUC_ru-hHSP2IDZdNDka7VtIA3OTWtxul42NUmZluxTzQaSav2BbufFNSUfDxpEb80Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HegauTsW6ZH5Ujlafvh1MUQl1iay_D4B2YWetTXJvKziClxBmczmgevWzsiOKFpnagZ9_YCfwiqmO4hI_-fV75h1Ntjp0bEytsYm57uG0vOHHFjNrQ80RUBRAgxIzhE9O1F5vd_pK7UjUKFqHa8boW2rm2LEbVxTihbDDm_yjhMbcKmRa16chJKobe1PET0oowSJBYwK1xhqGVG6JdXfaoZlZ2DE5V_sZeypsofr3lLXf5ofnZShiDOC2t8IuFz2san2xeHUNaYmX0NaiJNDxhk-BjDVtE5qZD1TrvoxHYNI1FYMUGcNOa6qYq69L6lsM1dFpf7GqTzStWn9R8Dn3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X17rvxs_6SLhqkHL4PNdqhVvJIeGDclrPUReJw6NfIWtyGXXTmwQHEtFMqCjkYxVE9WGZhVt0ZQoxq9h4CgpoXXPCbcv0W5HB3iBKiFZyn71cVu8hiuRthD7PvF8kzQrPSLzLe8J12WPi6i55Ew8q9iHADlw4T-l6Ejg1zwdaIXWqhxxOMWtB4sNp0XwvbuclzrhucqzWQyKPeU4KrJCUSZrsOvEWh1K2nTJhp6C-cNrBMJ5Ya3tSRiHutXuxPkYGJZDVUPLcps8eMvMv1tJgMnAvW4uOnvfS__b6jDi4sWVPY996JoZGQdYaa6zI8rHGoVqivOJRERiihjEgXrIlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XabWancfH7Pw-Gf8Uu39E4P7S20lStfC4l9BeDp_vWnOp_LaDgpACs2GPQKe3uM8IHAxtgIzv-SyboH8CpTOqseqBwptbu5RlXqE7Bl7_VFDx--A8GGyCyQ7kq_jCWTGe-8J-UDfmmuc2gknGXRyt--99-6whh7trD3rkHwkssynlFA0fNy_CXtVPWMTbSM0mmYcXLUaHneyGxST0UobYYTmHTHT5B7UEW5i0Qd3AlzCpk976R_HbekP4prP8wi4BalXq63BezBJe5Nb9hSG4GC5IIk5-iEYrCVdhWn3rjzHndpA-9aStDRjrWWQZCQcbiSVoni1eAljBpQCHAqABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRTXx7a37KjnHddCmvGkUna83zJtNYIC8Ekhp8eRp3T9NsjITZk0p1XhDm1ZrjHi4cQ3hF_pNC4Av8iIn0N0g9aN07sZkupd39NXbeqkgkPNbaX7GKuPVwyCypT7aF05ooamD0GyV_3fnPBaGnZlP9RXgJT_0KoGUPpi6sw4i8KKuCj7gTh9FpvSdgaGGq655P9YaDjNHmKv78UiqeI_G1eMa94R88yilFizH3smy1tipVqf0nG26IZmFSwslcqLmqjIwpzYf0kBasRzttl9SACvMDu8IO9lYbTwq0wGK9RIMqKu3BLg4-ZM2C6iRKI93x1ho9QcF_FxKB9ajpV4Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8mbwtuxLMxTl_u0XfaQvVIE8Gl3QTjnebPidnBQBuYJCo9kScmygJhgEjy1lYvKolyJvHWJKITn0iIDGtOY6jU2_C_R4JVQcyqkk7fH7D2tBighbHAB9VYKNOWvaDfZoNfau6vtSx9GAB5iERUHvy9iLaVMqMu_LnNFKQ2wiCR5eTeWJ1TVSVbFQsnJhGOnAh7K35vRCfWUwEwYhwkwhABmR4PMupyZ8Ryf_RNVhQ0G_EgaIUJYEkwUENXrIBzrwOz-R2xHtCWTSpoIfgE18AQcyKv-AvuvZ1CP7hGV3LWHLuZoyxsb6uaQs5IO-Yx415pV_mscTGb5C3j2eS0K8g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8WymfdLLGC_4RuH7CLaTnYh-O-nBwDGiZaugYuvIVMlTdsdCzpyNH8OE-HPV0rDj971NUtMdfog9vQ_4OS2ky_B8WL5nX4UDoqR5YOKSmLEF64L-gGbiL7RFYMOHJeKjWL9L8fdHLQxLO-nqpadeQbOe2Z4YYN2jWLrt3O_G1g6MzRAXskL1Udfc13Jx9cLiCOYSDJ44oY_kn8L0-rCXWkyJJDip7MM_RaltoXyGPuxvXr3ciQoN6zGKoy6e__7KMWWoCd58IHBVPzqCZS8NjSP_r0ewm7AXHq1B7izhHzMCxgUK88-3BDZKv_yQmcAZzSBs9Essns1D6zhHgsDQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmPMC5ApZIhtnjO9eIJ_s0wF7pF0EEtSCjmFTj2Zz6WFSmqAe4tUWlZmXjqSg-SfdEB8bqEPVK5-l-eWU4NJJeUa9ye3f5a9ytPPmHk39o66seK3DdCv_kq_Wv_jljYupwy0HsR1GutdUK-6pNlr6rhKBd6f8AfEHbJqIzfipNHdMBV-EdJ5LAYZ8LmvNrxjePsIwEFrA9sxA0A564ZM5G9azEPvNyeArkfuFBy1QJHLfagha_lUQYgqYh-mcaAOI4Wptj35A7VyI3vLVTAm-0MrglD4Oa7CWsGS9ySTV7tQXhi5fzKkH9HtVbOCFWHnV_pa90Fbe_x_HA700vsHlw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=gKxQuQ_9oyUaqrZZNxNQ_ie5PN4fM3yclfXN1iQIsJpxzewkWeH2RZASt9aQiJK8snxREO_RYlLG0EJZOdKCxAleTO6oCbOvfFnCu2hQOG8Veg2d7jW8EYyQ4g-SbZ5GPwSGKQQ3ts0WG5wosM3JUEx-7dui_fdvJ0Hy6Hm2JoqAriZ85SFl8B5hCx0BIqqmKBIVoX-cG-Ex-HA26rW_-K_XKLK6vgi6PL_iYh-7PFUxrRiDNta62_4vXbXUyjMCRX2Y_A0rJtqHjA_KhqFGhHVE3M9uHnVrvZfV5q-woOunC_eofCwKFuhqvs4mu082fF61s8d4EkzRchf4PLlQXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=gKxQuQ_9oyUaqrZZNxNQ_ie5PN4fM3yclfXN1iQIsJpxzewkWeH2RZASt9aQiJK8snxREO_RYlLG0EJZOdKCxAleTO6oCbOvfFnCu2hQOG8Veg2d7jW8EYyQ4g-SbZ5GPwSGKQQ3ts0WG5wosM3JUEx-7dui_fdvJ0Hy6Hm2JoqAriZ85SFl8B5hCx0BIqqmKBIVoX-cG-Ex-HA26rW_-K_XKLK6vgi6PL_iYh-7PFUxrRiDNta62_4vXbXUyjMCRX2Y_A0rJtqHjA_KhqFGhHVE3M9uHnVrvZfV5q-woOunC_eofCwKFuhqvs4mu082fF61s8d4EkzRchf4PLlQXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJav7GUk_3L0ETD_PUVioQMH2WFwDaEhNkAQUxW5Arlye34fStHZNr58tbS9JhkzUhtTMg6_l0ACV6zCRAPCmFvTOYUCp2yv3qUuoS4bmKCyP4I57Ul6Ne2GAQIpdIFi6K1RHaGJFXJev_bCfX395jNRh5wCvHPAbu87jTqYG_RPH8E_UlOYdiTbTxPHfgE_Su5gJ3ug9bUwKTDdYUut3pvZe1uQJpsSuGUFIKu4zzjvjHkJqun-AIxJjsrcdOIGY80m7yRb95nvvjXSqAmrUOBR-gNfDZ97NreLjBGTFoscHjglQoj1KhSvcxaZWUjBtu4u-hVxA_m4-HvvDhj1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqcxaCppnL-UBqXHmvTBr31iIRtNlGST2yxI5zjRftcbRBntD8GwbIDfeOjOXYM-Rc3sZHZEthMhr6UH8Eh0XhBsqFAOmwN222CKfTZW0UqSWMCiFcnyENe9FrBvRu8nNU-6U72etC0orrBhBpADXirCzv_ILlLJv_5xzEmCwdtLusmRd0BZwOnGHVfFhz7SNS9Tv_bd_QESRKXrMilYCt9uH8B9hcybyLx_wB023wJiEiWGsn7BweaoMKOJXmlWpv5L0LRUZyJf2DkFKOhoaGI_-P0kknhhzKRfgv8GOR5D8FCzwUoNe_pCI_rZAJs4UJO-wJ_3Q4r2un3KVlTuDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=WtFAPkksbefRJ0s_hqCcVY691trP31OXKi5qNUgJJOILGoNkKJRe33Y7gAOLgHBvGbKr5uBDfsxjxh8pVLrb8xwQHR4s9x9fuZVGjI0vlvm-HdMrpOLCbJvFbJ8dXk8k7zP-ez6Hip3YizeR2F4APt4cWK4eyiN-L6JrzVPuL4x8udp0angdYPFTf8nbNRs1m_lsglOPDsyCR83iia5ToeBeKDIrL7QL2qk0nLMb0LZqpyM1i_WU-pUr4_eVHUq0c5tlaHVmm88jQKJRr9u8ammdqaKI0qHpfG4BssZLs7YKuh3qhtv_2Wyb5LvNFlL2yRSFW8qrVBWUgoWleSeCeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=WtFAPkksbefRJ0s_hqCcVY691trP31OXKi5qNUgJJOILGoNkKJRe33Y7gAOLgHBvGbKr5uBDfsxjxh8pVLrb8xwQHR4s9x9fuZVGjI0vlvm-HdMrpOLCbJvFbJ8dXk8k7zP-ez6Hip3YizeR2F4APt4cWK4eyiN-L6JrzVPuL4x8udp0angdYPFTf8nbNRs1m_lsglOPDsyCR83iia5ToeBeKDIrL7QL2qk0nLMb0LZqpyM1i_WU-pUr4_eVHUq0c5tlaHVmm88jQKJRr9u8ammdqaKI0qHpfG4BssZLs7YKuh3qhtv_2Wyb5LvNFlL2yRSFW8qrVBWUgoWleSeCeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgv9dkKtcem-h6nFBP5dfApZDdvmCSoPwuY3gqB2eBaR5dxQ1ajuzYkr5tcs0FTHi89VqFBHnE5Aj0i3J1zGAeyXgaFQbS75LexNZyEisCM2hoDy_izl_C_Yofo3Uvqj3cIMxGx2wstPwYfeVTSmHExN2ZPX0rQhB-Vp_U5WikvP9cJEW4EMjFWiHS83ShYPSLQuUlwubaLjlaEcnDQiRymb0vXLxrzCZ8Z-1SpTaRhhRBDy8ScdmntXHQIpc3ZR3VC-IDcebD8n-XMc-zeVGSiT45fdC2ceVN5R7xmNVYv_ls6gPAJ1LhTNUSDV95jjh2G8iPYb8G-tfVL1172G6A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdTnGttcncaWk2oxpieejEGl4EhPLh0LEnbDt2X6gL7_AKk5O6QHzuIZFBGULAo80rakLCI_VFaBzvUFa1mGLQcXGGuAEykWRv0g5BFpDzT0HFp2Lm0soaiENMGrm1cjQJSmZIDmHT3rdLgUEfyraAMYUwhX5iQTAWl-AmQYQQ2t-V5MtL4AMeFEChXrT5mm2b1-g0PczYYn3Cn9CoKMjAANM5KduTw_80p4IOjtcVQHH7EcpTVwpxeEew36RpiSNzFxma9TY1a4Xh5cKdVeMh37NiqCK6EGNL-1yJgE7VcrVQCVkGc3_qfEwbzp9Bj4DNfda8CMZm8AegwiZMD5mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3HFfrMev-PGNdVp0hvffClOvRg2yMuWbxB-1S2ooWlPdzMwz7Z5l7en--O93RZcyFOoWetf9Onr8HtA6MK6FcO6qlPwcXUU0zWm4Nx9gYTOfppaCO5cruuV5EXgHvUaxDKKv4D9uVVaRx7nihNMf1PeQeDezi4Ne0BGBqxBymkSG-8k_sM5vYyqWL5iTYwioZ9aUdNmPC5lcz_MHRx16zVwgTvqkiLgT8ZSpNfe9ANM50XQi4AbQgaQbz6yDIYE-gTIXXMepc3vrD-E8QdFOQU7xHsdB-3-4aJJrIRQDeNqdPXsZELPZ4hALeV6cTxD0eE9cGUy8L-Ozaaihuu53g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=cAIAI_E3UHg9vIugLbwUaKCyLLP_oeNwWvs9czP3sp_MG0JJoJoVmj0PKDpdmwU-IOFjgXhZfjRW9qSxMzd8j7KizyzUI3VlRZ5ExNbOlhE6bpz3oKNkD0a0X5wTHOylbrj_ZoGKDW7I7IdYWSldY4qrJKzhJDcitUPAvRpdXO7QcbO4eZFCD3GgGKJsDejaBPK9r3PDw-v2Zej5BtdyzSv9899AorMflMEE_MC874tT39bQzeEuYilnipzAbEj47GykozJ2Ypt6I_6cuibgMS_x1LJ-n9_-93C7y8Ux8TbojbJ9HbL-5uv7Xf63CcaYtjAVrxhfECgjWisSt1vWSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=cAIAI_E3UHg9vIugLbwUaKCyLLP_oeNwWvs9czP3sp_MG0JJoJoVmj0PKDpdmwU-IOFjgXhZfjRW9qSxMzd8j7KizyzUI3VlRZ5ExNbOlhE6bpz3oKNkD0a0X5wTHOylbrj_ZoGKDW7I7IdYWSldY4qrJKzhJDcitUPAvRpdXO7QcbO4eZFCD3GgGKJsDejaBPK9r3PDw-v2Zej5BtdyzSv9899AorMflMEE_MC874tT39bQzeEuYilnipzAbEj47GykozJ2Ypt6I_6cuibgMS_x1LJ-n9_-93C7y8Ux8TbojbJ9HbL-5uv7Xf63CcaYtjAVrxhfECgjWisSt1vWSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=M0ZCdCkZvYG8lXFahDmjPDN-PNHBTa0-7D055Q8p5RsR4VQbu8h1HBGC7ogaQTRWE9GOP-5Aig7SaA2jui51J_Vcg8yPM-U78KMbNcwjAdAT2NwOB4ObC64m1VxCn-G4SoOtDWftL6JgyIg9iCIofZseZVVgndhc0FrZBNBkD1a-pxKmfuYDCh3PdbfA1rQggSjbpkhbzIGPptVWMi-D4AqcX6QvXQYpgRJwYRBMi6-h_xFBgkmMv4JU3EriZEwUtwMSBUkB3HFcLaj_6XHBTkD5J5kUFrOp0xvTdsjbWEGYtXuVkFJaUN3T4Uav5RMbKoFjUsf8nreUgxJiB9fKXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=M0ZCdCkZvYG8lXFahDmjPDN-PNHBTa0-7D055Q8p5RsR4VQbu8h1HBGC7ogaQTRWE9GOP-5Aig7SaA2jui51J_Vcg8yPM-U78KMbNcwjAdAT2NwOB4ObC64m1VxCn-G4SoOtDWftL6JgyIg9iCIofZseZVVgndhc0FrZBNBkD1a-pxKmfuYDCh3PdbfA1rQggSjbpkhbzIGPptVWMi-D4AqcX6QvXQYpgRJwYRBMi6-h_xFBgkmMv4JU3EriZEwUtwMSBUkB3HFcLaj_6XHBTkD5J5kUFrOp0xvTdsjbWEGYtXuVkFJaUN3T4Uav5RMbKoFjUsf8nreUgxJiB9fKXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2L9D8FWdVpfdH1hlXBQghvGa1fUrrsinaNGpbiOYxYaDIWTZ0ci1hfRD28ax3E9Dun6lCPiQgtzXjbXumAHl9lSYmXjOt21IvF_7g3_f2hvP7LIk2VYckvbXLVYojVd1Fg9GUgBsBGb_iqOHrTjOY-yLvCzH6aaNtWE8E-qwItj9V6CWSY6Oqvh_rtwniU0-cSpFr-LKk4itmUVUxQATFFZ68xHtXBK7gBXbNGOpEQVTKVIJbDgJBZl4mcKNOys-AzPUGiUNv8NdXNAxuC18kZTKPS7RVqFB6lwlGvRdaueaZQglgyWA19D3LpX7jAT25eV92prTBqhnSggJ1WGGA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srru7vdgbHSW6e0iJOB0hw_wxQ90stkKgeHUICscJr-ZAwLTg9duApUqo4fK9K2Z-p6vDQLmLu54-UZMbTc1lgsB7MY9z4gaqDn6MxpiiMtdE9USjg9qBv-Wz6jGcaKJIBsusHOSiGMeIfbEl1jMaEbhjDAGLE_nHLtNwbMv6R2F0ml5bAxnXokocDkl8og5ZNeI0mZlFRUklRww4rGCzHLVs5HpC9r8eVxEe27IhA8zlqIZmQpQRYv6rHduzLEkuILFPkRBhbbe4ttdbOmMCofTYWr2a01CI8WF0JGA8uG8Zup4ZiHW45BKEfC1_7fgHu0AqK3kc0bNeOG6kUwWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_wrLNCoNRIflgJ5o8SKM4CJCEooFlnN1vyW-EjGpbcc-XirGKqE7SRKF65im_Af-djcehrZh9SXvg2SdM93tJWpN3SlxVosLLqgpkr12lZt0Ca6BLir7dscqV7zbF5AJtU7ga_1KRJY_kkBb5lB3VTkKHvupCYLXf18VuVjool3weB5KZ1vzR8f4HSVyIYDXzVJyubZWgC2-c8GSi_UqB4qpYmtvOzAJUJ8b_eTKInnPBcif8QGjToMOb0FcTSvzEaYtztrWNEvBU5wL29dMKS0WOFm06W98PiZiYYcBraIouySUBN5vFettgUtAY1rZX-xgvCfS-kenAzCr85SJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJA1ExtAEZ9unO5emsMFMjh5XnB8tRJ2hZW2xcp7kgu8ZWyXUYBabnQywbvWqXjGGH42YOUDP_KofLcdv-NcHYHR819LX3plrnxVKsHoz8xoL2V98F8p0bxuI2ObhJnBD1IRnXGrd8F7Lo6fV_kVXT2vT_3f56dejHsoPZpIFaaD4_TWPcj5XTw2T6B4S8ThRv-W_Ca68CSvAdXu-WHRU5s0lzsQqGvn1uD1yuP0oaO_llb1KOpV9YelTDzOzd42_if0FPJpE0aztTZ51KUZrQD1bRw3AaMZkMWTMxurn_dDBvYhYg5gygk4-6o1nODp8fq5WDGQwGV8HrpF1EKoAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qACA4CjnbC6Z8nibwxlzCOF_TpdUi7VNGflkh3V-bPJITT4LmhNjFQ-YV3eQOwesSdn3n6xmrHclcRO0Yoo1B6G9GsLu7S9MMlOjJE3PNwThyQudcSZeJSEVsxPPH3Tz53zNJ87GbPNI3OP_4KLlZ24XH44D8Rp0WZBUyju7ooKLCpqMbq7iChw23QnBqS3uDfeEVxzaAEIrGvmeIzbp8MfNDs5l42ZwF7anRHvV6Q_BfrdVTe9xfnPwzfB71yO2zJRj5zJaEVTl7z3zi0kx2G7lUUcei_hghoV1WWIU3t-SWe_5Xyjolsb1rsQ3Jf23dYCrV6-76XGaTOIeq-yWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NA0oV1hNHcvVzC59d5KnV0USoafUn5DRj0slb2ts-hok9agx0oc3L5dBp1QRXE1fjz_9Vwr0MVab9_cLj7hTPMd8r37ZzHzbUKucNstzszoXeq_sVfIqHQW7mC1L8cIKWv2TeqgGf6DN5XtfWB6c8PR7B7qK5r4crhRJCMc0FPQu6UUiYoRlGv1WCfYWhGXiJpifPBWjKtrWevGprdjXStfBv_CeYE3-HA2PtC6ulA77czM3MVGPJmqp6fnpAlQeZ_pOJSxwG_xWimkv8FUmSRFkn_tRM27zm-5WyrlfHAni4aa4Lk-FlkQClAD8xt_6rk7bZ_DOP2lMmtb4FVR-zA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3keDU88Qscwg_KcOJe8tLgR3Jm_ZLkKdyXVYDY_kkCNqiwXvteveF_K1MxjiUrlpDl-H--12s6yQT_CYzvyNhPUPml_FMcKdmS7fx-xtGig17X5fwx_LyFWFA0X4ywpvkTKR5VjXIt9M3v7IXdaAy9tQyuCcj9vmRQoy9-1wwhbJD2Zt-FnUoj87cmNaNuforpwPxU-Q_DOGZiX-HZ1D1d6XD5BpS5ymjODG396WqVmVfQzv76rIslmJD6Mb9xoM5COZ9nqGBq3LSyPVdZxFp7Hbc7zx-2cuA8YTPh8wB1lranNZs27cNYZsBZKQEQo5IxeZBN4KbJA0jESaavQGQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=qD-WCOVJcDJ93ROB11_F9xYaxDtY09JRmjiZJkhwKpnWv9Sy-jnJ3V1NjVpjo0Aba6tWy-AAXS4ZrexNuX7oMo4OcX-HGb7rkBjZmS4lyIa4T15oavvp6XTUIiieYtc7TT9yEfgieLP7fUesLksrtwKbm7gwx2tJbE2jPDwKvBHyoiYx2wGZWdK8Jz1MYjzm01Bnug2Wu3QxAHz6oAO32KocG_OtvgXnrOZwg6er3l7muwe0p5dxKfGLC5L6NUEiZURDh6fyjs-Tjm56k6kT-TUegeqpi5GJYhYf7sWhc0nVmI9qOe_9-uy2asySCvYtx9QP5YTRwiq0QdFg8NQzPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=qD-WCOVJcDJ93ROB11_F9xYaxDtY09JRmjiZJkhwKpnWv9Sy-jnJ3V1NjVpjo0Aba6tWy-AAXS4ZrexNuX7oMo4OcX-HGb7rkBjZmS4lyIa4T15oavvp6XTUIiieYtc7TT9yEfgieLP7fUesLksrtwKbm7gwx2tJbE2jPDwKvBHyoiYx2wGZWdK8Jz1MYjzm01Bnug2Wu3QxAHz6oAO32KocG_OtvgXnrOZwg6er3l7muwe0p5dxKfGLC5L6NUEiZURDh6fyjs-Tjm56k6kT-TUegeqpi5GJYhYf7sWhc0nVmI9qOe_9-uy2asySCvYtx9QP5YTRwiq0QdFg8NQzPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=gmF1_N5qsNqXEOHmaH2aHT0Zot_gwLY_pvnOKNfpiIRYRb8W5Ru7mjTWtjCCOb3SQ-2AmbvFRn4lzzPcMptkEinsb_7gKiS4z0Cf-ZDHbgrAkwVEqre5wrTKiYT-EYCRDuATcNeOh8pl9BIgSLOoKdiB_AWBm092biKvCmumlfNqeIyvqqi59Zzhv4YNTbAGxxwYXqSZcMBNOfnTA3hO_Dy88BD-h8ZV7c8YNdHi4PSai9lrtiG7x_PA-18rjc-4pmAf6pWWpBCoKUlxtHXVrnjWzRcxh7hb39uiVU1hOwOuMoOg3ArdqBWr1rXT0WPg27Cx08eJW6_jfzoNClH64Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=gmF1_N5qsNqXEOHmaH2aHT0Zot_gwLY_pvnOKNfpiIRYRb8W5Ru7mjTWtjCCOb3SQ-2AmbvFRn4lzzPcMptkEinsb_7gKiS4z0Cf-ZDHbgrAkwVEqre5wrTKiYT-EYCRDuATcNeOh8pl9BIgSLOoKdiB_AWBm092biKvCmumlfNqeIyvqqi59Zzhv4YNTbAGxxwYXqSZcMBNOfnTA3hO_Dy88BD-h8ZV7c8YNdHi4PSai9lrtiG7x_PA-18rjc-4pmAf6pWWpBCoKUlxtHXVrnjWzRcxh7hb39uiVU1hOwOuMoOg3ArdqBWr1rXT0WPg27Cx08eJW6_jfzoNClH64Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=iS4otujOJiASKcIAbQ31u3yzAyBwQ7jdQYvCEsBwt8nVi1EZf17cuIgWZd576GIqXzv7wIvrfZaiJxbe8HMuJyhpwBKhS59uEUZl1X8tP9PLFQYu394XOmSm0KBtIcA96eN9d-l58DGkeUUaVavu7IKBfG_mCFnVSFuPLH_wE5N5rygCqABp11J_nkVw9aNjwdMc40jp7TrFvRzbHQLdvSeKWeGu0Mc6AExq7pTMua5vicvZEmfizG-flcehuDBRqOg3pnMEKTeCCozo-OJ-0ZHgjyCyWS0iWqI_bCsxb7MjA0IR-TEx2xPu2O8Rx_y9cUKSWXj17mXrlE5JuhZodA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=iS4otujOJiASKcIAbQ31u3yzAyBwQ7jdQYvCEsBwt8nVi1EZf17cuIgWZd576GIqXzv7wIvrfZaiJxbe8HMuJyhpwBKhS59uEUZl1X8tP9PLFQYu394XOmSm0KBtIcA96eN9d-l58DGkeUUaVavu7IKBfG_mCFnVSFuPLH_wE5N5rygCqABp11J_nkVw9aNjwdMc40jp7TrFvRzbHQLdvSeKWeGu0Mc6AExq7pTMua5vicvZEmfizG-flcehuDBRqOg3pnMEKTeCCozo-OJ-0ZHgjyCyWS0iWqI_bCsxb7MjA0IR-TEx2xPu2O8Rx_y9cUKSWXj17mXrlE5JuhZodA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=UPfxyK8FRMkRnxXlois2YNaPzsSDz95svVUU6YL-t6NM5P9QpJ6_9II3KfYuin22Oej-pFZcuj7XzZd9A9ZZjaWSZixm7GuSd1GDEG4SoDouP1VsCjN1bUKq2auyCz1bdN7aK_K1dVKH-CYo-3cngieVnyeVjpiCsWa_pjP4c1cJk6NOjs2eWwjhhuvwghLKkMoglC8anoNhTxqyuslzpxI2gac9DAeU7wFY4I9vghdhIZvAt77oKMuN1L4lDCjS1WEOAEHmoFpgHK-9HB6szoExmbTIqI2Gp7XHZU0jbizxtBy8RIW-7kRR_q6w2gcBiyJQkh-My7-zDxBE0yBnrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=UPfxyK8FRMkRnxXlois2YNaPzsSDz95svVUU6YL-t6NM5P9QpJ6_9II3KfYuin22Oej-pFZcuj7XzZd9A9ZZjaWSZixm7GuSd1GDEG4SoDouP1VsCjN1bUKq2auyCz1bdN7aK_K1dVKH-CYo-3cngieVnyeVjpiCsWa_pjP4c1cJk6NOjs2eWwjhhuvwghLKkMoglC8anoNhTxqyuslzpxI2gac9DAeU7wFY4I9vghdhIZvAt77oKMuN1L4lDCjS1WEOAEHmoFpgHK-9HB6szoExmbTIqI2Gp7XHZU0jbizxtBy8RIW-7kRR_q6w2gcBiyJQkh-My7-zDxBE0yBnrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=iCcfOyicryE-b69lPdJ5ae07fvEG8KxsP1XqHdkyasHiHEElPYmxBmeFc0PHxKZMtcSuVdLcZxWtNdaHB-QsGJsOUAwjlKohoqNJb32YI9OCm7j8Ahv3N-SmdXM8mRK6OR7Gd7dxs0eFx6-2Cf-LlfMgo_MQyEpduw9CtByeZtWshQHT3yMew4u_525zZ2wS8t2r-1pQPI-psIafNu5Cl7bfQ5IMLxfgEyoD9K2JPKMoRrVjqIZh85tk4GLrlfT6HBaxJZus3On96J0ijrfWrbXVgDBqQe-N8Fouzukse-XSbF3_lle6ovh-m2pv9uBUjklctuvsjhOvCDvVVjaahg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=iCcfOyicryE-b69lPdJ5ae07fvEG8KxsP1XqHdkyasHiHEElPYmxBmeFc0PHxKZMtcSuVdLcZxWtNdaHB-QsGJsOUAwjlKohoqNJb32YI9OCm7j8Ahv3N-SmdXM8mRK6OR7Gd7dxs0eFx6-2Cf-LlfMgo_MQyEpduw9CtByeZtWshQHT3yMew4u_525zZ2wS8t2r-1pQPI-psIafNu5Cl7bfQ5IMLxfgEyoD9K2JPKMoRrVjqIZh85tk4GLrlfT6HBaxJZus3On96J0ijrfWrbXVgDBqQe-N8Fouzukse-XSbF3_lle6ovh-m2pv9uBUjklctuvsjhOvCDvVVjaahg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=kDaPmcISbonA65cH4a0RLTCgQGQFPHg92niqPoiz324m00AXYGRpKWkKgLz4mRK6aafCr_le6IjkLNnsi6jEqQQojQ2pfMD4Efb8mtnOMW92w1C3yT25HtfcYMuljIaaSFjar0sGtii7_VIQuP4kx1H2cDxWP3shTH1crUQJ_KxnB_HpnXeuLy4NlHWCiJoGUIMDAqAe-frAg8PtThOXWwe3yCs735GSGoLN0LFJHeMnC6tn7MS4P9xi0eRjHgKdb6B9Wmdyv0eOe0wu1O-PgxuRGB7n2d5W_unEa-wiWZ0XfKAQYPrnXqtHCrZdyqu0JWBJ9oL3lwUjYTpf1-bJMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=kDaPmcISbonA65cH4a0RLTCgQGQFPHg92niqPoiz324m00AXYGRpKWkKgLz4mRK6aafCr_le6IjkLNnsi6jEqQQojQ2pfMD4Efb8mtnOMW92w1C3yT25HtfcYMuljIaaSFjar0sGtii7_VIQuP4kx1H2cDxWP3shTH1crUQJ_KxnB_HpnXeuLy4NlHWCiJoGUIMDAqAe-frAg8PtThOXWwe3yCs735GSGoLN0LFJHeMnC6tn7MS4P9xi0eRjHgKdb6B9Wmdyv0eOe0wu1O-PgxuRGB7n2d5W_unEa-wiWZ0XfKAQYPrnXqtHCrZdyqu0JWBJ9oL3lwUjYTpf1-bJMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=aiEIgx6I-VpifUf9_e6yWriG3x6KlshNDRYs9r7CurdnQjMJ1-ltMHk0_SmxSw2itvkpfddWqG_wLTVqm7bcJLfG_qqof-oU0uQErfhR1ERqvBG6TG4ORktaAAFY3wFzJkQpHPimEyhShzbs8hJ-I46JnvxlOPvQjXJ98cLfdU3qpD-LSZG4C3uluvgrHE05WpXFxjbwkINnfuT9akyTGZOhS8SjlySzBxDj4oCHPMkWyWlNDDzPb9XgMmjwVBpRvTr0bc0wIFkkVXRY4ARikqpDGFZm6Y50zRMzdibQ1DGkSi0APFWAYz5Ay3Gm7Ja-jSCjJBJCk8sIOVCO5Y9zyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=aiEIgx6I-VpifUf9_e6yWriG3x6KlshNDRYs9r7CurdnQjMJ1-ltMHk0_SmxSw2itvkpfddWqG_wLTVqm7bcJLfG_qqof-oU0uQErfhR1ERqvBG6TG4ORktaAAFY3wFzJkQpHPimEyhShzbs8hJ-I46JnvxlOPvQjXJ98cLfdU3qpD-LSZG4C3uluvgrHE05WpXFxjbwkINnfuT9akyTGZOhS8SjlySzBxDj4oCHPMkWyWlNDDzPb9XgMmjwVBpRvTr0bc0wIFkkVXRY4ARikqpDGFZm6Y50zRMzdibQ1DGkSi0APFWAYz5Ay3Gm7Ja-jSCjJBJCk8sIOVCO5Y9zyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PHGFoXdPD7AI0BVVwPK4JPV8TgB2opUcsYnfM_XBNeXEMk07qNjDNHOcN0BUVkKR9kzCmXfQo7kRACpfwaaYXcG3R46qZVXq6al4cckvmKPSH6qsHFJdiwDjO1kSrMOeYwqv2AOSqAg0RTctZQZpQbY6RsesA7J_clidyd5eKpHGzYCZ9sUq8X9peXP48zyMdA79dyDqr0axPEEtsWsA6DKAqXbgUEPNg19CNKPeJwnwjdF8lpdBxsPDE0ofAgZttnfkE2FozhDhSc0QtjfwwVEy7QkQIM4aO5ie-b85d4VK2WjziuBwRqmJq_6DZ6bIAtz7mLEkqghPbPsoXKAfxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=g1Jt68IBhohs-FV2n3OZpl7pBCfVstjDXbpd6_owG7jL6_cmL3gCqYMizRJrtkfqlYZxDwcpqtUfdfhHLjuyFxzfP3DZtVllY8ALeE2Cq3RUbU2k7WsZrgSCBX_ChHxQKf1AJ9KhAj7cEi23CQ7mcu4LLGAA7NWvW_hjMarzE4u3iV0VqIc0zu8-6LIzwwOewE4S1hG4mGxA7q_fBDIOcm2UVx1oCc9ghCT8fdiZgBtlA2hMiBSymvQnAuW__-JuVeEwiD3NCFNzgkPYHhu6cOaZqzOdvme2b5IhFQrB97z1x0I0GOt5RuAjx4j4-pJFkJihBpukOVEEd_6kRlwVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=g1Jt68IBhohs-FV2n3OZpl7pBCfVstjDXbpd6_owG7jL6_cmL3gCqYMizRJrtkfqlYZxDwcpqtUfdfhHLjuyFxzfP3DZtVllY8ALeE2Cq3RUbU2k7WsZrgSCBX_ChHxQKf1AJ9KhAj7cEi23CQ7mcu4LLGAA7NWvW_hjMarzE4u3iV0VqIc0zu8-6LIzwwOewE4S1hG4mGxA7q_fBDIOcm2UVx1oCc9ghCT8fdiZgBtlA2hMiBSymvQnAuW__-JuVeEwiD3NCFNzgkPYHhu6cOaZqzOdvme2b5IhFQrB97z1x0I0GOt5RuAjx4j4-pJFkJihBpukOVEEd_6kRlwVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTSNVl1UUGbxsNeFo5YkQjUE1QS7sQZHD0DwFrt1BuoziWYBwPUsETO-cQlRPcKPnvMN8gW1DjgOtzZmhWRVP_gCAxTypYe5HFDKMcHKM_aSaWH0wKdgD8kr-7ILUCpdrcyPu9LE1Qv8n0_hclxWozBThYIYkqdJ0Ve2YgVq5QcgLohYdJsGLQR0bn2tciilGI4L7CJ5kA_SdC49wHMbiaMSNl_MmkSgTYpkdxn7Yr8cMmKEjWvp5Yf4nFt5bLckEILK0-Cen7DMRlF66geK8tewK4wlW3knOVMelaAoeoo_buwvBIxWnwJNi1tSyZZ80khdC9IKL67PCs1cdQJaeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp-U6YzP1bpZviKEh2hNn2J1_KBs1_NFAChObbG537i_6XruNajti0At3L9Ub7C7BuwzsuJbld4QH73FZebbf6pqOA4kiGLiZPquY8-6hLJL9NbQ5eluUh5dNn6acdIdImovDPzH_LDTSqvT7Q50RO33rNt55NP9KjAAOYqo06Vk4YhG2xsLB2T8sN2v7TcDrg1l6dWhTcnTX7L56J0muLRiIJE0B6bxSC751LmgK24Touyqk_yPXyu4RmunE2ipIxqZQ277yHg8S-vr5uMM1ZYz5EaRn4OHA9WVr00r7-JssN7mco9gWfmlP-GEYJNaDC-cZRZSGnKeRdCTuGjffQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1mrfEd20NFI3CAUNH1vRyxWePWdHWmCfhVnCzV57CCZgUES3c07fpu5nI6xLpZCit5YQzLZKos4HxwS43i4uwjc7I-Wsa4sJ_VtTEiycEeTNSrEpR00TjsEP73FlYEQAyQttddj2yXTjblEotDldWK2i49f1TTKuuTXcqcywrf5Eks5FGEIVugSORhvYYLn-yipPDrJTbaeemrRNEXEUIlPrQtWyghT9lq0vNWOpEp_wv83CqPqUinkwmtaTOj-AWxobG7fcn8LO2Xv20H2L4JoM0oJpIl194RPY9Jfg2XG6qb--gQHfgOxpxC2v3DI9qAgS5G6gRHElCDQhcNVxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnH__UZwm8MMnJ2WzCnEkaRq9bCyQlE35lHa-J4GtF2r8zZBu_FHmiL2FqLBy5lqHm1_7UigEDTJyy15Vo3nv62DpUDTub4g6hJGbZuoWKP84b9mSD9FWlDSbc_j4YrnSpbyG9BugekLDBFUVKNILyZAquN_6yfF0H493bgvLJp7E5uZLDcct9mTg0X0O30_YASc3I0WefbJ5AlWyPxFL64TEdHhGcJTBochiaX90ehI7R4F5MR9kVAnQuHjNaxQozQt56atesYI_1W5SDoWaD2w3r9I_vBiPUkG4Xj48ixqUwtwBYA2l4ZLm7W4WrB-9IekD1ODRuoGQ6c1uTb1GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=MCAH73CwP-xv4rdNB6G6T8dJZaZD9r0hcstzq2j8n6Y37Lc-vWvnyaT-mo44DB1AYpUUKIMJT1S31tw9rrGDLvgPwn4iI0I1MYF3S_BBebnuD6DMFRGeGvTScFyBFnZR_IHuqIqylIUnXIE2LGplP3KLRcvd0mSGNrTGbfPLBws1b5t-i1coEJX32WNnP1WntRIOT4vVzVv8Hm3kir2NBQAuN2QlaYds1kHQzVzAgOFDPBjDQ-qkT1_WgpFQbPqcUgq_2K06iiukye-xi9bShGfAXG9AIO2TqItO5pzvJDgOMlHMylNbMLKwB47DyvoO_8UxxRsEepXvmWjsWiVjPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=MCAH73CwP-xv4rdNB6G6T8dJZaZD9r0hcstzq2j8n6Y37Lc-vWvnyaT-mo44DB1AYpUUKIMJT1S31tw9rrGDLvgPwn4iI0I1MYF3S_BBebnuD6DMFRGeGvTScFyBFnZR_IHuqIqylIUnXIE2LGplP3KLRcvd0mSGNrTGbfPLBws1b5t-i1coEJX32WNnP1WntRIOT4vVzVv8Hm3kir2NBQAuN2QlaYds1kHQzVzAgOFDPBjDQ-qkT1_WgpFQbPqcUgq_2K06iiukye-xi9bShGfAXG9AIO2TqItO5pzvJDgOMlHMylNbMLKwB47DyvoO_8UxxRsEepXvmWjsWiVjPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5TjgRgdxIByfpPxXjzuH2iuLMFcqyQEFyTG0xO9Ct3m8wHxjRjyLShByY0pR-HCPNDTlXOo_AO2UXOmnLLF0R5rKbmCZS4VudolIb8a2V5QsE_JaOpU50p5LI6ju7iQsHtV4dUkJUvNO7HBTWKlHP6SWeObMIac6cHcCqWg4Y_ZBiH0tSBRvh_hLob8YgI5GsNP0Vu9GA0KBr22O3aEyUJoXmW1fE8vz08cFHLWFGWCzlF_D4zuZhSyZTK6gfVfz35o3sZMSE7_UgZg9DpeypvNLk5XdsPKaLoRmO3Nj2zJbP4DB13mdBbNgwCZleNaku-bA6o2ZH4p-HLLSzVQXQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=kkdUxDprKwSTIveDwNjH5zPXD1mOAevZMszqQg0HP09aU6fn54gM3EKUhpWxDQ3zAwuhpLba23UXpggC0d7IETiUg8J-OB8n7KMweUrk0Nurq4Cgvx6T3naqSuExcauS7ZMuKMe86GAz-RtEwtrsCOA7p-RfXrGq70VMom1h6mYXbF-8mV2N7ZTaOHbsVrKeN30sbwevw3-hSBsRWxrIQ7NnycEzqJMKFVhLQ3teuBMINYaJ7LtCwVjawpGAOvIdohXVulT-y6zLXVfvWXEJ4P5jvHuGLTWQjyr8_h8ld0nWw7GwHU34fZ86USfs_TaHgO8u4He5ntsdJ4IQmDrXHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=kkdUxDprKwSTIveDwNjH5zPXD1mOAevZMszqQg0HP09aU6fn54gM3EKUhpWxDQ3zAwuhpLba23UXpggC0d7IETiUg8J-OB8n7KMweUrk0Nurq4Cgvx6T3naqSuExcauS7ZMuKMe86GAz-RtEwtrsCOA7p-RfXrGq70VMom1h6mYXbF-8mV2N7ZTaOHbsVrKeN30sbwevw3-hSBsRWxrIQ7NnycEzqJMKFVhLQ3teuBMINYaJ7LtCwVjawpGAOvIdohXVulT-y6zLXVfvWXEJ4P5jvHuGLTWQjyr8_h8ld0nWw7GwHU34fZ86USfs_TaHgO8u4He5ntsdJ4IQmDrXHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
