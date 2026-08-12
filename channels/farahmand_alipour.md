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
<img src="https://cdn4.telesco.pe/file/fKRgIP8H5co8nNtTNDsRYeIYLIDGrydXzC59Zj2YKpugKek-J1vRIK18TL2zXCc_LGxY8AlVD6ox8bkliYgk03GNXitEpTZLoGWz2aOMPUlJyffBeAECHgB8tGJcU3GLHJYeOsmsmH-Cka5OIqnQ0cmkWOqL3i5p_T41E2RcRgpH83Zi5Ia2ei-qlG_QyDZGHPsxu84-TKpkCQ57EhRDBIgqYtjynQBEHtDnvtJNWVP-YM1BZ8GtGvUAKXdUeiko7c6HSvA78jMpHAMlMhzuZ3kKwrHg66NBT_Dt2F6-LPDnmEsfN-AMPQP9aKelMuZz0Xzh6FPjAJkuV1gJknaPRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 16:17:19</div>
<hr>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9kM_hksh6LgTIi6Vp6GqAbNyWaND0nxhEzNctnoG3XROLX06ZEEkbTUEX-nt0GY8WHy7EYUkmCqCPypLNZvf_h_aeng-QcrPe-XZGVksrs2JIGHSrWsDKqkIzGL2ng8r1mUzqgHk4mM6U1spoZyO2AzIpklh1-UGRmMA1iO9Ce4AJ4LH4RGYn2RvmJSYQ6Zn02Ssz47zuRLoERp-K9XwKJ3tPideqxmbL6x7L_zVm_R7Ae5_1sr5g5lgShRpcoP47Iu8Uc0j-Awog7C06ErG_JgezXr49RDVuzPOxxxKbkIW6RvKL_3RrZETMED5ee4uPTKxNqG1_ffAEcXjA7Pag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=am6fRNlu0r5ACpEc5XSS4ewyX_NjFCONV--BnoqADXV0bwOwFf4STsdKSWl9Khiwy8uBFgKH-Nm66B7BQ7mlqV0NEjQGMI6_o_RAIrp9lJnSa9yWdGbBDDm_NOYYGkQqTolJHZgxNYmuujDxyKLAvBvjISL9_2e6g3FPGuNHXdNoVK8c2NNXSyuMaq9G8_hVIaYTtAGs48ucus_uc572tFyX4qo_O2J79RjUvTdqy_QBgflAHd6yYW4N0qHl104E5VnJ738IBKAX2UHIO5J-LWYTuVs_q75p2R2sZ1O33LXPkOI10HmVA3FGxV7V83ieC9kHb5BevKSy24ytHo7EfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=am6fRNlu0r5ACpEc5XSS4ewyX_NjFCONV--BnoqADXV0bwOwFf4STsdKSWl9Khiwy8uBFgKH-Nm66B7BQ7mlqV0NEjQGMI6_o_RAIrp9lJnSa9yWdGbBDDm_NOYYGkQqTolJHZgxNYmuujDxyKLAvBvjISL9_2e6g3FPGuNHXdNoVK8c2NNXSyuMaq9G8_hVIaYTtAGs48ucus_uc572tFyX4qo_O2J79RjUvTdqy_QBgflAHd6yYW4N0qHl104E5VnJ738IBKAX2UHIO5J-LWYTuVs_q75p2R2sZ1O33LXPkOI10HmVA3FGxV7V83ieC9kHb5BevKSy24ytHo7EfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFgTgBAaDE2Br7NXyrmnp5A7QvsRMXp2Ck7ehAh6P5elVRLqj4DKosPXIv5ny_gZodWWg5Vlp2w-2LdLpg6w8Ey9BOso-f_FOtcjTUS5LCCGQk12txvQ614Jvec3C1oK6_FJjC-JMMpFpqaOwzXq-j7MF8bvs4tqiztpIeR_i2ZGw78Gzgs-DSVzwgbNjCKM1kQOk_Q8twxYata4i2OS1XTBLxgfYLrGIn8PJWUA_vq_2FnvYdkIOqe942jVvaZJqta3eTKmdpUzVYwBDt_LCBn2nr-VsMuDAF4yQwpPthLwrxsBlB76FANGE3ai0AZPiF6hgVrNudc-oWl3gGYypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Ojk1YGL9AKnaOd_HtUetvHBF04nt-0Kwm4bTBq1lhBZLzSdkFBK3-BT9dx0PZQT2iyZx-yTqJ4LayUq585gwZXX6_Q9Svi0ftgZVh_NrU_MQN5RqZWjIhjzSc6kl-o_xeyzoD42SByNx7ngY5DnA-wW-3wyIy84grrd09gVVOzkfXIm2tbFtYWCsX-VwwzBr7bjdxx7gskzAPf8D4e_HPMfZVdm489A8t21zy4G6y34OdZshMRGEIZ1mvZjItE5-rUVA5QP0kG-Kqr4syw3IlDH9MePCGosFZm4bDsb3ppWgsd3f7cJrCHpNOK4PczBwIIUwIwoHL3mUlkwC0KewcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=Ojk1YGL9AKnaOd_HtUetvHBF04nt-0Kwm4bTBq1lhBZLzSdkFBK3-BT9dx0PZQT2iyZx-yTqJ4LayUq585gwZXX6_Q9Svi0ftgZVh_NrU_MQN5RqZWjIhjzSc6kl-o_xeyzoD42SByNx7ngY5DnA-wW-3wyIy84grrd09gVVOzkfXIm2tbFtYWCsX-VwwzBr7bjdxx7gskzAPf8D4e_HPMfZVdm489A8t21zy4G6y34OdZshMRGEIZ1mvZjItE5-rUVA5QP0kG-Kqr4syw3IlDH9MePCGosFZm4bDsb3ppWgsd3f7cJrCHpNOK4PczBwIIUwIwoHL3mUlkwC0KewcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=YlRGKbWXW5LweJBTNg06_1JRxhVDklC5xOZU01AiADOEqUxOAhk5OvrzZuRuXQ8ND1f8D9HyhGDYt7j6PZgOXQocmQeqp_p4p02Jyx7ULXL1yJfHK6SXEZ0HbMx9qYC7_5cAHxkOuz-ylRYMCzrQeaqMhTzMwf91rcNxlzt53T49ncq-bDW6Ki1HjCfZIthSadgCQ8e7nTEqq2u9LBKzByXP1K43pDErwwyYsJhaKyNozsH-9Y-QVEq7mQuzZxApl3CxQ5hMYTRaQpW8R7KaN_lBGT06siez5treaz2v-S9sGliNnZ9UCwZ2NPVLH_JIPJXj-T_iwc9_NLK0NsCXhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=YlRGKbWXW5LweJBTNg06_1JRxhVDklC5xOZU01AiADOEqUxOAhk5OvrzZuRuXQ8ND1f8D9HyhGDYt7j6PZgOXQocmQeqp_p4p02Jyx7ULXL1yJfHK6SXEZ0HbMx9qYC7_5cAHxkOuz-ylRYMCzrQeaqMhTzMwf91rcNxlzt53T49ncq-bDW6Ki1HjCfZIthSadgCQ8e7nTEqq2u9LBKzByXP1K43pDErwwyYsJhaKyNozsH-9Y-QVEq7mQuzZxApl3CxQ5hMYTRaQpW8R7KaN_lBGT06siez5treaz2v-S9sGliNnZ9UCwZ2NPVLH_JIPJXj-T_iwc9_NLK0NsCXhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehRwrwTTfHTZEAAkuJ_fPFbkAduzwzO3PLrfBTEFOmt5BGOdngG8rBZIawftJ-uHzaXl7GFeHuKoijh_6O4IM8PYDEeGdR-li8aVgioYJtVRty9JWWYONpLs6vCiY4bCSkcKdX2mvQqp1jTUSHku-RIS24H46sJmIDySazYMPRFn0zgSasgib5KOJTAZ6xb6K3rtRzbGD3BHTGPZzdQuRHKctmL-vcZsWlW-ti7zrhI0eExQ1CwoQLT2nN6NMOUmSpo5Tt9Zzhj2w8Svl5AH5HMIfFPp5jQ43r5Qjs62h9eU3zAZAHlydCvYITWRaEJf9S-ekXkbgBRudTefZIkMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_RrAwsDMLyEYVlAP9O3cIHoqt1m6TKIwr2Vpb02KkW9oh8LmzojNCkuQwGHvp9eovnYJdvwq8BZPwwVkunlasHl2f49SMCXFYHFvPbADLSuE-5yEJZaGExpQGtrboXyfyKqB6xLwprqiXMFoB-Uf92VDhnaydsY2-HBlmEZWDlQMlG116xJnX6-KYtA4kJHQ3o_l3dKcR22aKyD32sXWJiSdTX-zkpzhDjKdFa-ZIIoP7sC0VfkW82JrvUkBcrO5BiKKLHdgRhvNarXGbyK1v7b-yBHqySLF3t3rDmWE0Yp2BnXcPQnPfiCJf6Tf9VmTyl5Z70tRZFQBivAK7ZwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHmST5RLWGJmfjAQWAb1iXfv3Tjz2HUDKP9K_GvT4cuqb0eDShKRpG-dxB3GTSdld1koPqljudy4vBLbpWolcDJaivBdxF5DPKY6-KmvU7nAoQS_kveJaWRoOmUIipJoQGALbD_I7bxOeJvMiIQ49YnW7OD9SoIKBTgtnKjjpa8mWMGCXgFXd_SyEwTCzj0jWcCV0z4weyzl-2-wJdzzjtJefxqdF_Ej8I9lmGfug04FQ1IUIMrH7idWoNrWJxIyeygYO1KExQvN4lRoQk9CjaTwj7kp-9nRXif7uRjP8dZhLO4V8Rj8rvIcBaXRBhNZc4fP88moUg8XnyzUY6FzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=gME6EU6JC0UaXNoWEdrPrNjMZE8y_N45Y4_xd6jtZCbQabyjv2F7cgKpbijJTf1qRvCPLfnPCien3zl9zlmTgSVrALFVdxv74zvM3fzhbqxytp5vC6YZ0tvNPfisgcnNzQOHC6N455cRgHrzh3xzzFlqyC5AOT8404fKvtRPfLmrEy1LVp5FwPptsvy_56jj7uLPYvdptg4LRCLNu262cOCyt6PvBCKftW-OnjIuL09LIMqY1lHbkq0wTrzON1cPy3DZEmvgn6oollVDw1j3huINMiOE47FMIvAC8mDEt8yxX-5xoq8ctd5pW4e1c92tXhJU3CBljmA-nx28qqGKLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=gME6EU6JC0UaXNoWEdrPrNjMZE8y_N45Y4_xd6jtZCbQabyjv2F7cgKpbijJTf1qRvCPLfnPCien3zl9zlmTgSVrALFVdxv74zvM3fzhbqxytp5vC6YZ0tvNPfisgcnNzQOHC6N455cRgHrzh3xzzFlqyC5AOT8404fKvtRPfLmrEy1LVp5FwPptsvy_56jj7uLPYvdptg4LRCLNu262cOCyt6PvBCKftW-OnjIuL09LIMqY1lHbkq0wTrzON1cPy3DZEmvgn6oollVDw1j3huINMiOE47FMIvAC8mDEt8yxX-5xoq8ctd5pW4e1c92tXhJU3CBljmA-nx28qqGKLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=NtJ0OltJTRbMBkHknwMqNljS-qqpfAHR-_hkc8p-_bTzV3pV_CPFUPbsfzZm7j1c8iLhIbDsSf7LgOSJQrdodc7en8TgiaGuVGW-bDAyThvs9jwLbo_v47DFDsaP03oP5c9yztj_OuKpI5dVhtaDkwpW1EvwoHIYPfVEGhyEhQv3Jld4cLI4SQV74Kpu0j7t71U4sC4m-TaoXK1MdSFOxE4olglemYvZVDWt9_0f9GihrdsLC2CGcgV4p0nCiPHabeX2ZfEfTzfg0c1WbtsZKSDUiZsJOSEpKpfCbm5e4oB7_VePK1nl5Ux58jzUuTGgEHn7j3CJjKdLUCo059EGvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=NtJ0OltJTRbMBkHknwMqNljS-qqpfAHR-_hkc8p-_bTzV3pV_CPFUPbsfzZm7j1c8iLhIbDsSf7LgOSJQrdodc7en8TgiaGuVGW-bDAyThvs9jwLbo_v47DFDsaP03oP5c9yztj_OuKpI5dVhtaDkwpW1EvwoHIYPfVEGhyEhQv3Jld4cLI4SQV74Kpu0j7t71U4sC4m-TaoXK1MdSFOxE4olglemYvZVDWt9_0f9GihrdsLC2CGcgV4p0nCiPHabeX2ZfEfTzfg0c1WbtsZKSDUiZsJOSEpKpfCbm5e4oB7_VePK1nl5Ux58jzUuTGgEHn7j3CJjKdLUCo059EGvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn7E-ZJobfeTNH6AGrbUcLVU4xpDAQflfyxRmqaq4zthGf8XXJ_eJxunGEWa-w4MWiev1l5jMc_wVpqFXINVXW-xl2lOHB4yNmiAYehDikmNPiyLT_KgwEVnS1g-9oLE1ThqxWVmgJmnUXbwZietSRNa0FVtNAz08624GjD4ycxK4boMioW6HcZ6fXc-UwgkGVnhuOEp4cAVfUTZV7accw3kaY6EUVovM3YAu0aVnBct4u3Y02OJ1pxzgVQ0mYiLwFNsAOg-SRcL24K5ByK8nRelCVkBYKGJqBwvoFeRw3w_UvMBxhJZDTPJwxCpOASVujvckgr4nJLvQ0H3iACQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESrxsxZhqCdJgKjFQ42B4dVG2aeXpQlVwIRj5HoHDsNJXTVqPYanTXzQOVIrV_ywKRMNh5YU-5nPYIpN-SMXejObcSk8bp4YdcLM4qq3zgJuxkvtS8Z3TWpisMrmmheaZ0NkR9KsK4-4lkeF2J6X0l-tPL0bpanO1o3Ply4VnM1CN2Lq_nKO_PrnqQHxImyOMRvNzm9kDoPBbV7vEDvP34kF_ahTkFYJ_pzwSp5IKg6kR2JLBBbIoP9oxdLm4kHffQFR9dj2ZPTDoGYgslq3KyXxwjkZACSNkHWfPbSw8zQbqkrMEPKHmOSlHXH--ArLSIOqIlp1IQy46zEpuGgu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgM4TV_MSqAszk4xLats3HQJTEwKYGra7YrFGVlmf0S2ZSdhPja-sotIb74QwSMQIXW0y4uOobeTeiroSgwA3tOxhZLAElX5FL7hH8woi311HjjszQWk9qjF0ivYk1Z3XNRqSe1-0183-Ych6Qn00LIVaCdf24ozGbWMvvHdM1kOjYXC6xefOT4pZwaW0EsLUzbn1IGSi1LaivGIYLKXgLPKgSYtQIYeW5oz11SQX6rFtoUjeAzHT5IIOJeREg0xiwCksv1eDW6Hl8ol99BeMBYg-XRymeuwrF_qgSBV2eDu2U4KuByurBMIEixS7YqllqjPfk928yJF4pVzcwp26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhcyjiqDZfLOMVtxhQAAW8n6mBWza5ozP1ZnlYpmSYILCTJJMCF-EDLQk1zcfEUiH4kmivYc0Jrn62A5xeKzkkHEtUujwsESJc8yKQDG9ZaZ6lq26Us5DPCk23J63pjnV7zVaLS25zD4i6F0xRTuGmdjZBU7A4WvGJXk6d-xddZBizENbgRrY0zTTKhe3htugHdONnp0W02SGYI1TdrRO_5pmNjPlgZojCLFpjgjeN4rEsUuX4tOh-GkCXfu2Y8rDrsb571S5WOSwJklPkBgNV7aS7jIwvp-sH6Y_c0EtYBlelK1ll2Zbh59tEDzJKJSQIeaHuTlud937JkcpqWGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSqpGwHmBb3GeuJCp-BI33rGJSyqkRp5NVU5Qgk1Cd_pYxOS6z6MZb2_VuqoxywU1jJ-h-jk9r1L7OmPjcjuPE7wTvJHOEqhNQn2SLOMrGUthtNz47wekX9i2BfnflaVF2V6XYdomII4vkI3Tve-7pbQqA3GALj8oAVXEB2aaaMLPn12PxnZV1EcfyeQmfJ63bi9A4_6OO1s_7q-BdTf_sGoI2_WI-YdzcuXfesUFKxnnKPvk8e9fAcycw0MqdFRij2-t9GamSZv6j-VTJKvnNndAoOnsq8JXM4MsEJ0cSjYpgtwOXgZZE02bYVL9CDn2Th8yUqVVhatuMoNpFDvBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6524">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9MCqNt4MonU4vd9jcpu5q_whEQYi3wo4Z9OA2bY9xqps33DYm-NUK4Ou32IwoRvYURvt1PfXr8Wd7ZSNwAYxYZETdZvHFRVVCRRMSG4pNZYMLB8tvYN1XlnOgtvESwR250lXrblM6QSj8_QHxbbFI-l-1IsRb1zPRhC1-MUhGceCWkMOIpafq9GBzOI4RkiCH2Pgwbbl9eWohMlbaQ1DdURp8h0cmCgZ8hnxO1EkVF-c71B_E1LFWR_EXpi8Okls67ZZUioDP-2cRnewXXHt_23OWJR_lkeNH_vHrgR3o3gB9f_Gjy0TFXHmQ71d2kxAyfcekvSzGIStUNhY2NcwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5dOmsEDSI38_fvdSNj0UcfjF_NkJANNYpBWGpt8kjgCy1fDTOv6j0GnG11KBueJGjfMbXTzgDxZaJJlTxJRwBMJjKyEe9AXg9DLQ-3D91aZ6MtUAv8iEcrnUkLSzpDxDcf8e2TgnbjAHxb-vCleoiO7aXxEPdkDM7uxvMtaQmzUQ3AHyFWFeN8Yb7T7OV9Na3P5nnzFzZRWnzjIF9cSa6KXdZEVPi1ix6l51a74QhM5D9p6iUFmElKOBD9tAJLSOU5r9GXrffd1GeoAZzlCJnO71z8Gv8mn70yHUd9Vv71WRLoxdpOh2_sHLrgskJqASLvF40hNwAkWsstfNkBNfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LMjISNzEZrxT5JjOC49sqKrkjNGokCeXJJcJMftXtqby_4XuUc87bm3w6Etf55uvxGTlNVUE14PfG3u0SqO9UhWmofceoG_nj1Cw69NROudyCBbHVWAi9fX4adzEpuAw4oVFxPO914Zx4A4euMsWKt6qiY4DK32aP6bcw8hRmfT4o2hzq_qYGXEUTgLUMSFKFzrz1jU7V0Ar33q5NqB0Qw2fJYyMXVEt91ZzC6wBVTRYfnUh-0dGvI2vWbZy72gIlkgM4cgkXK4URihGzyFPksVzwHK5l9-LI60t7NAuh4HrlER2tW7yqSveyoIK-xufJrMMecK1naUSz3TTAxmkGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خیرین مدرسه ساز در ایران،  ۶۲٪ از مسئولیت ساخت و ساز مدرسه  رو به عهده گرفتند. حدود هزار مدرسه.  فرض بگیریم همه اینها مدارس ۶ کلاسه هستند (برخی ها فقط ۲ کلاسه هستند)  اگه هر مدرسه ۶ کلاسه حدود ۱۲ میلیارد تومن هزینه داشته باشه، هزار تا از این مدرسه‌ها میشه…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ6BhYM9CqWjCe5rDukW-nvpnJLAkizvNq8KDnj5f03gaGLmBwhG9-YN8fsNgdE0OaxTcqiqSC52ZTp_Y_c9SB1Wc51tX7lxuP7-r28GAOOg9rEfAgjw61zlOEmGpxXpye71Q6qPQptLJ2CLkBmlEi-87qFyT2QHeK5dmfwlNtirzDeOtWUlQy68eoHdt6R1Ht2j26YhoAs7JC0bkZ92y_SIz1NDBkG9omrsOf-Om7_EEbXi3vYaUpwyXvf_Ny2j-E_y1biq-X42reTkdTp0Ua4iQBcQ_CoAV0-Fdcv7xh1h7dU8DVtV53J2fMO4STtrns3DatwyG2wJqfco1MiZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6522">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لطفا این متن با دقت بخونید
و قضاوت کنید:
پدر یک خانواده،
نیمی از درآمدش رو صرف مواد مخدر میکنه،
موضوعی که باعث فشار
و فقر در داخل خونه شده.
مادر خانواده ، چون بعد از اجاره و….
پولی براش نمی‌مونه،
معمولا از بقیه کمک میگیره
که پول پیاز و سیب زمینی و قبض آب و برق رو بده  برای سیر کردم شکم بچه‌ها و…..
هر روز هم دعواست که اگه پدر اعتیاد رو ترک کنه، هم پول بیشتری در خونه می‌مونه، هم کار آبرودارتری پیدا میکنه و پول بیشتری در میاره،
هم خانواده از این فشار و تلخی.
🔺
حالا سوال : به نظر شما افرادی
که به این خانم کمک می‌کنند، دارند کار خیر می‌کنند در سیر کردن شکم این بچه‌ها، یا دارند مسئولیت رو از دوش پدر بر میدارن،
و اون هم با فراغ بال بیشتر، با شنیدن غرهای کمتر، پول خرج اعتیادش میکنه
و در واقع کمک هست به پدر ناشایست؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=CytYLRmFw2H9RYk7s-wuLS4YmiFsbhEt1nd78CVlPgLeQwtORY1Fwj_c2fsvmyYks5dYaAz2tHbI6ENluBtkjBCsRUbDsPLfCbgshAjS0gJ_uXPrd0K7WXQSSqahdXX4OwQ5qD4gLl3cCp7M6AIjH_g_CaNzvqhmLaEoDuYWwgWNHDV1u6gVxKpbJSxuYoRr8U-61_pjIRfBlkvNvD_I6SnhYGLsD2UssP0WaNI7bJv7QPGxG3A09R7bLAK-1HqaLFtEppVBcSbLulbHj9eMN6PufQxCbMO6Hx8V9r4EPJXPZPFOBZnwXClAnqdy3F_LwyBR6J5ymBNlReK0AgSwWIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=CytYLRmFw2H9RYk7s-wuLS4YmiFsbhEt1nd78CVlPgLeQwtORY1Fwj_c2fsvmyYks5dYaAz2tHbI6ENluBtkjBCsRUbDsPLfCbgshAjS0gJ_uXPrd0K7WXQSSqahdXX4OwQ5qD4gLl3cCp7M6AIjH_g_CaNzvqhmLaEoDuYWwgWNHDV1u6gVxKpbJSxuYoRr8U-61_pjIRfBlkvNvD_I6SnhYGLsD2UssP0WaNI7bJv7QPGxG3A09R7bLAK-1HqaLFtEppVBcSbLulbHj9eMN6PufQxCbMO6Hx8V9r4EPJXPZPFOBZnwXClAnqdy3F_LwyBR6J5ymBNlReK0AgSwWIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOB-twWxtgvyt8AOVyzSTiEn4NY1P1NfdGOOeSGFv8dt30boIHyYzKfj2Ls02TeIq8HIVnl3mVXW1C3V_rZXJ8Ed4SXZaqGyDnBJz00QjlASXPDr74RQwWy9Dv7G0WM0q6RIvID3lcwSlk35bHvI6AfdnWF8OQiDHlnbq1sprdPgc3BRLRLd5LSx7nEpURINZzH0GOYgw1CzoVwCFBRmy7Q0C9H_5wBqNw2FvhFYacVXJXCQ2Ayj3z-pNUxRcVLKcdpnCxCoJx4fmSKVVASjM4X2x18fMu-tOTIjRmdBMp4XQ_KkkJlDGiPDj0cHBk2EiH5cDhbeU5SUzBp35hGPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugQADNpPlvH6nX9RGu4ISseW1Ay5dHCc6R30CDA83lZ8_i2qUfvUMKn-xd_wD8VCrJnO1-R8elhrhr4_n9zGNeZr9kSA6D0SKN1G8oeLcPpzx4UI3WK1HG1JSw1XTjaaJ5kZLO3-mUeDL6fE8JIEy7uA5jcoS43tZVw_EkPfbUXNhhC3257lwlCmtV328JJJP1q0Nzs3O7CRyYTiJ4OqkpRcj7amFUUUbDepn-BbPUcjxbQUfrRlSkF3MzM9P18Q5OeufhoCNHX9MZtCOMZmv2m97t5TaC6TIk3BrI3AJeeE2ZvbzpTFcNniTcrFEPfC-fL9QAS8qsrndAkRsUMJdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«حمله‌ای گسترده در راه است…
نه، صبر کنید، می‌خواهند مذاکره کنند.»
این یعنی «دیپلماسی نمایشی»
که مدام در حال تکرار است.
استفاده از زورگویی، وعده‌های شکسته
و اخبار جعلی به‌عنوان ابزار فشار،
راهبردی شکست‌خورده است.
واقعیت‌ها را بپذیرید و به تعهدات خود عمل کنید.  ما به نمایش‌های بیشتری نیاز نداریم.
- فهمیدن حمله به کشتی‌ها و زدن زیر تفاهم‌نامه نمی‌تونه براشون دستاوردی داشته باشه ، از ترامپ میخوان که مذاکره کنند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6519" target="_blank">📅 22:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6518">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5HUX8ZfuCXzOkeqEJIo0gn2L8kYyWcBLjUixX9LlGG2o424d0qwZwxDWQ3rdJ64eN5m8d3idCCZ_qdw8gwGJhTp_nZahu7f7Tcwg-CuiUkYFCEG93CZ-1gqN_44FKnfNjf3BsdogscxmUoenM-gSTI4HpD6iiyqYfW8MLzXhgE1q2d-sOQUjj4_ZldggIDSEZPtQsYGBrZMo8Jr7F8o0jdJQwsGcbasMg0f52j9VPEcKjUPP3w1KmeBnnTwK41RWy3TxqTgFLsNy242nBmk_Zw01R1j3qhKEs7RFs2sgUPZn7OTqn5cxyPBJz5omZfi8wsRr1YD8t1-PeNUBLGEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1bUFp-stgPU41FL6n24PoZj8Lwfva0mGkOlsxpPqoBhsYsudvzl_gYl0hxrUSaFKOov6P8IVOozOAPnafKO-u8LYRdQNoRdmQyNY2v7SjUHLmARO1--LJbjKkpjtlTjbmgtvAcKE0y6KY8hPM0Sk06OimoE0NZLtjqbyQtPDyZEcZqiadDpncsgmeqVTQQCHPhF4oUUhYHRr5-h-ilwJzvB5-SCs7b6w96sJ48GIJoioJWq3e6fPYxvg1tLuNHGpESeZYGbztPtjcMt1R6gdUdecomqosZI7i0HhyIcZPQsDi9hKK9HsFxw-yJ89j18RsyRVg0hbP8h3OEJGuOhbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTst4ET_b1j0eJGNTUlEOa9PGByqxrJXkWozfb_qa9dRt0uBlRweQuU8xGmeiY_rtzlRmJrDKrhS0VVOn8PhlnHSQPKLLESNnkntAqA6GP75qtPqdvsHWJQ3hZzwLOuTO-TT1cz_jh0Uwdy9ky2l794OHNevaT2nrrjwBWdSyiLHuBwZoNSrY-zaB_BUZC1GUCEjbnzxprywIgRqd7n3a1l7tvjlwBqda4sMhLRqcfMbOyLs7nKNp4belRxsAJDZkgR619rSHn-Qh21Xpnextw5NWkVzOXueY3d1AYRDjHt1ZPiJtxVeJR5jRu1I4m9_6STlw4iZITnk9s_tX0cfpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cZigJsFE60VZ5FKDzNWWt49Zh1HJbqxwRpkVbfKUD359q_y_IwUpQ7MczbBlrDdUdha3JklvuAzEJrDSsyvQc6yhkerG7tMa6uukITiVGIgf64asC8Y3nI3qNo2ozuBM5bhIiG-VvObHsM0_PtOhMX42kxUZtEPx37tcXdCsj4Z6CxurfkRUH6ifD7bMEEZFNIXLUXAODert-KiWXM6VBRLwlaFoT8B08P3hlz8TQKKmtKCOGIgf14AxZ5nlcLeeuw0eKuAIa2WcKI18y9MHNuHP1GuqWGk1cRu9R1_NbyRH47Jz5PeER1HUBqDWteb679GR_nZHpbAQpbFiZoXifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7nMyTdUZdGHm3AWj69YE_xskgdXJTd5724SGOF6GH2ZBKDQG0lSa_iQa34_3dLuSIJwWIPMYcyuxLsJk-xopCvZhzW7WyJaPtw0NmN1ZefULhDUQdJz1Qq7K8mRWHuXzt4fP2SBtGfXSr-FrhBo5v5Vi23tAMr6mz7nrfDJpQ-_X0k1P--W5MH4wu9qcyC-OFPgo_oyJ2zCqHdbDhtRQZyFi2Y6EX9VYG5VSx7fc1OtmoNQgEVsHVgQU6wHxiWYtRhVJMgKJhQ10tTZuc_R2_UKN1wxhChvUS1SXLYlP2InzBXVRLAI9V5lb_S0d_oL8HsaYkiWjscuZO0ALOJ_QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6513">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.  اینها دنبال «اتفاق مبارک» افزایش قیمت  نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.  اساسا با همین منظور شروع به حمله  به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6513" target="_blank">📅 15:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6512">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=tcpryUFf9xsXaXizdNTAJMHl1aDe2Hpx0J3YuC3Jvd1iL7dXPxVTyBYyWxpqVR5WNIxYTrTXoKHJ0mo38j07PYJWokTgxrf-VgFwzqhLwQV07NX2EnxeF2jZuZu8HXA9Y6zgkn-kJtU-bZ4RQzW7PDZm0l3qJ3w0_qpr5Kn-3R3d1cNSKirkF8uPwVKl6ntsQ5V327XE8yLPLF6mW4efm12UFOYQOO_EZCcrQqKbs7hnXy0OJGbAmIU1vc4vvf2l0Li9PnCx3n4oheJMbM4G8L1VtFSLjLlZ3WjwCLObW_1VjbUnxeOW9J5jXlHmWBWAxD5s8pXr8mIhUAwnoe7FeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=tcpryUFf9xsXaXizdNTAJMHl1aDe2Hpx0J3YuC3Jvd1iL7dXPxVTyBYyWxpqVR5WNIxYTrTXoKHJ0mo38j07PYJWokTgxrf-VgFwzqhLwQV07NX2EnxeF2jZuZu8HXA9Y6zgkn-kJtU-bZ4RQzW7PDZm0l3qJ3w0_qpr5Kn-3R3d1cNSKirkF8uPwVKl6ntsQ5V327XE8yLPLF6mW4efm12UFOYQOO_EZCcrQqKbs7hnXy0OJGbAmIU1vc4vvf2l0Li9PnCx3n4oheJMbM4G8L1VtFSLjLlZ3WjwCLObW_1VjbUnxeOW9J5jXlHmWBWAxD5s8pXr8mIhUAwnoe7FeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید تا یک نکته خدمتتون بگم.
اینها دنبال «اتفاق مبارک» افزایش قیمت
نفت در بازارهای جهانی هستند برای فشار به آمریکا و ترامپ.
اساسا با همین منظور شروع به حمله
به کشتی‌ها کردن …..</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6512" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6511">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.   خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.   او همچنین با اشاره به اعتراض‌ها…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6511" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6510">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=U9Rx4-VQSFbdsI2Dhq-iuayncWmsnN-7fbWC19Pfw2MIc6qbVFUABtKn7DIvnZvJ9ryFf-IgHlYrJtzAoE5UsfaDIINtB-aoO8nDzgMzbg5WARk2HuaIgus5Gt7gFYQkQk5ILUhTJLxgsxuS4SCSlWIo9N0TF7ZGRZBi0Cp5Ot_SAAY9j-F9uEFPd_W_pUMev7lHrJFg92EXQYzVpUg8cj2Y5MN_9lzybzjbWh2kNl-Jx2ABxTwvHsEH88GaUz31NrsT2Yb8WKUoUZ5QXDKt82NGx0IbNZ8olazdJOnT2zdvmXSoMvy7n0FwWKkxTWlkocskBusJqdK57ooIT5ngJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/effee93ecf.mp4?token=U9Rx4-VQSFbdsI2Dhq-iuayncWmsnN-7fbWC19Pfw2MIc6qbVFUABtKn7DIvnZvJ9ryFf-IgHlYrJtzAoE5UsfaDIINtB-aoO8nDzgMzbg5WARk2HuaIgus5Gt7gFYQkQk5ILUhTJLxgsxuS4SCSlWIo9N0TF7ZGRZBi0Cp5Ot_SAAY9j-F9uEFPd_W_pUMev7lHrJFg92EXQYzVpUg8cj2Y5MN_9lzybzjbWh2kNl-Jx2ABxTwvHsEH88GaUz31NrsT2Yb8WKUoUZ5QXDKt82NGx0IbNZ8olazdJOnT2zdvmXSoMvy7n0FwWKkxTWlkocskBusJqdK57ooIT5ngJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمدباقر خرازی، دبیرکل حزب‌الله ایران، در اظهاراتی درباره مجتبی خامنه‌ای گفت تفکرات رهبر کنونی جمهوری اسلامی «خیلی تندتر از پدرش» است.
خرازی افزود سال‌هاست با مجتبی خامنه‌ای رفاقت نزدیک دارد و جلسات خصوصی بسیاری با او داشته است.
او همچنین با اشاره به اعتراض‌ها و تجمع‌های خیابانی گفت دولت مسعود پزشکیان به پایان دوره خود نخواهد رسید.
@iranintltv</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZOznFgPIqOW3RdDYFNcW_mYOnJLYx6gjw2g63Mj_Enl4B5gpCe10xYfbjXHGXJ7uWgwcZv1YVokUTLQUxp1fmHpf9BZ3CdyPCjSM-ogr0tsAyXhXG0jCuP2oWOlzzHlcxh2mxkaWc0SqPr8BJtOE_LozknWE7kObd2i7k052Hl2BUQVI6w9eDzpIL52e7FGx3jRwLCW-F6zGUOwioS61O4wBSNFeGv0dlYrd4YORIZ59EjD5beokg8OmuI-0xIQXuIDZm3dK-t6rNIXPLJ9euzF5w_xp8akeKJSnCT25nZ9y1gr3Nv737WLumI7gB_60zfY83K4P4_v-pCroh7uhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fimxzb7IBWHAMij6URo9Dyoam6VwDxpVJA2dkCopHtWCLJaT7YnVrVjUKOx--FXi9S_CuVPNAZykrjJ34Ym53KDXt67xyHuU2o5KNDdksvvvJfUemFf5tf06F8K_C8nKY7nU9LwapeQVZbknuyfXScHCSFRaTKz7bgqzVZvOpmfxL32hKOjE5ILEjbmZOWq3u-YYV3dZZzNtou_zpTBUbdR5-2uubKCMgxJU4Ko084uOBM7-yRpShuclJdfpZZ_zTBnlmaiyKKglAomRGSaT9TAyGE9rjQi_BsJm_1Myr0MUKlhHZgs3qqBiOdiwYerMrWdEyma7pQKEI-qcEd_dIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=Af4aIq-b758mHCnz7QRutokk0RcSgMrm9zcT9z0XA2X2tOInibG4wKVeT9ma8-qsW3F2nAZnrleHPrbm8Zsu68YHsoNSWxZWdfUR1M8QGFdKxFGHJZdwl7bDRTxI65kxll198n5_yaEVyFjI4ma4eaHx2CC9Wdr7IXTSWlLtcYJECV3VHNBcaC10x34Ke-LjROtG2iUDV9wRUl7Lvq8HdxdFyql7TT8b9YohDoBhKPa0WNM3eMq26mZfXp6uK3feVhvmoZ1QxeAi_A66aX3_KlTGKWjLZck_5R63-EiSKO8uf4ho9T1Py2R3YxJHmMg2pQQLnRdn5LrDm9SQk6uR-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=Af4aIq-b758mHCnz7QRutokk0RcSgMrm9zcT9z0XA2X2tOInibG4wKVeT9ma8-qsW3F2nAZnrleHPrbm8Zsu68YHsoNSWxZWdfUR1M8QGFdKxFGHJZdwl7bDRTxI65kxll198n5_yaEVyFjI4ma4eaHx2CC9Wdr7IXTSWlLtcYJECV3VHNBcaC10x34Ke-LjROtG2iUDV9wRUl7Lvq8HdxdFyql7TT8b9YohDoBhKPa0WNM3eMq26mZfXp6uK3feVhvmoZ1QxeAi_A66aX3_KlTGKWjLZck_5R63-EiSKO8uf4ho9T1Py2R3YxJHmMg2pQQLnRdn5LrDm9SQk6uR-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uENIqeT9Ga-EdXy1sS-sE5UvRyBmuZgzcJHxG52ccsY82w73iScDvJagKiRi7C9Ab07Wx1IQocKNofsE-Zo3xzeEO2H-L9S5UOX8mDaFYwxOi8k4EZlFFQOQQgtoNZy-6pUEJVvhbHNVI5v6pHpPpwZau_HAtUVP1aU5J1TNbiRpp8CXYruktDSCzV98-k8DT4erKF1KNUjDUF-67Sm3PGtDMN2szunSl8Q3H_yxMEHXaK6iLu3vEMtxrZ7CnMgjJNeQn1iEE2wJ8XBhPirI0DZCXd_wlM6mb9C_II4413OtV54fwtSrFZZvkG2GPt0S6rZwX6exOC67JeH2x9YZmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FvntnHjzuhaZu18AhyMpFt0Z1paV1b7kuwyJoWDXy2ZcSZ3j3-Ks0Fhf6mIUOXpzfv2w4k27ze3QK6krZ3XE8jPBmnj1a5uhpho0u57-PibcM_48TrNrX03C5pqoA6hyXkKxC_3EDTzyYA8fzycHXT50H5qF0yFIs6kzkAfUKe80jt7l9CconQZcZkinV3Pv0HG1mJ5dOvUV40pck727byNriC378ZunD_qhqD_YVfd_SkWxIqD819M0SHedYDr25LB61tcqEFzgDUpomfKIzLkQntwcu1bS9izw-T2XOD0TKQ9l8NFWJL2tNEGuOVYXrcDA2QD8N-T6NYaKrKdmjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔻
سازمان عملیات تجارت دریایی بریتانیا می‌گوید یک گزارش باتاخیر از یک کشتی در فاصله ۹ مایل دریایی (تقریبا ۱۶ کیلومتر) از بندر «مخا» در یمن دریافت کرده است.
بنابر این گزارش، یک شهپاد به این کشتی در دریای سرخ برخورد کرد و باعث آتش‌سوزی شد اما خدمه و کارکنان همگی سالم هستند و نجات یافته‌اند.
به گفته این سازمان این کشتی اکنون غرق شده است.
جزئیات بیشتری منتشر نشده است. ساعاتی پیش حوثی‌های یمن که همسو با ایران هستند، اعلام کردند که با موشک بالستیک به یک نفتکش سعودی در دریای سرخ حمله کرده‌اند.
این هشتمین شناوری بود که از زمان آغاز محاصره دریایی علیه عربستان سعودی هدف قرار گرفته است.
سخنگوی نظامی حوثی‌ها به زمان حمله اشاره نکرد.
📷
Getty
@BBCPersian</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6503" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6502">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=MAntGqi0gG2AbBGlJ2ZwaWlpaxc53RDTl0szJL9ShsWPjBuru8N8tHQAwzWKPhFL1Nuxb1vq7umikeicZLfLVU7o5gK_n2x6X3juxaSy61cf_e929njRCda1eW3bwYgf4en4qjvE-0r4vZ1vGXrHp-tL-OYhWUknUulqQ1hl_3A3i4GQ7lYtK2BxWWiWGD8hKtQdNL6PZYL8IV6C7ZLh-PQNC60yQEFsZCY7iURM9vJ70g-RjCZb23HheYvWl_Z3JK_L_tSBC4x3s6j5XgQ2q9_wCRuCGcIJCVsty6vOc0qJRwBt5rVjQLHn13_W-1K55wV6fenefro4-E_SHx3vXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=MAntGqi0gG2AbBGlJ2ZwaWlpaxc53RDTl0szJL9ShsWPjBuru8N8tHQAwzWKPhFL1Nuxb1vq7umikeicZLfLVU7o5gK_n2x6X3juxaSy61cf_e929njRCda1eW3bwYgf4en4qjvE-0r4vZ1vGXrHp-tL-OYhWUknUulqQ1hl_3A3i4GQ7lYtK2BxWWiWGD8hKtQdNL6PZYL8IV6C7ZLh-PQNC60yQEFsZCY7iURM9vJ70g-RjCZb23HheYvWl_Z3JK_L_tSBC4x3s6j5XgQ2q9_wCRuCGcIJCVsty6vOc0qJRwBt5rVjQLHn13_W-1K55wV6fenefro4-E_SHx3vXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6501">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=jJJa9fiQ7it0-LUcFuTPVjq_pK7tS85HoM49oPXy9KRZ37xSVHCw4ZkwQK0RD9PvkjJ0eQEmm-ADsLPiXyau9USoNYYf-HhtfotULWdgwz-Blt4ZLxyXFaxFcllMIXtelLu-ztN_CxE3tcW_wqHwftFUW8C2NPr2-ufvek_E7OcXID9gWBPvX_VC5x1WxAj2g8GbtSHEpgqju7_GIwox2sI1bel8oxVsdusiGUOyXGU1JiKbop6UrpcCQjHxXSsVF2NmEvmINNpRbOD_kI4rB4sEMUU-bHM41Ldk2_KxCs5O9YMDWEjuvCQQInnv7--gGWDNtTMJBuAhNkUSOXu8aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a5730f1c.mp4?token=jJJa9fiQ7it0-LUcFuTPVjq_pK7tS85HoM49oPXy9KRZ37xSVHCw4ZkwQK0RD9PvkjJ0eQEmm-ADsLPiXyau9USoNYYf-HhtfotULWdgwz-Blt4ZLxyXFaxFcllMIXtelLu-ztN_CxE3tcW_wqHwftFUW8C2NPr2-ufvek_E7OcXID9gWBPvX_VC5x1WxAj2g8GbtSHEpgqju7_GIwox2sI1bel8oxVsdusiGUOyXGU1JiKbop6UrpcCQjHxXSsVF2NmEvmINNpRbOD_kI4rB4sEMUU-bHM41Ldk2_KxCs5O9YMDWEjuvCQQInnv7--gGWDNtTMJBuAhNkUSOXu8aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیلی منطقی بود!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6501" target="_blank">📅 12:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6500">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=NSfQ8sI9RVwazZQQY0WzsDAvvuqD0o84LFl5Z9S1cgC3twbkzcW1o-ZoqGDSqVmHiZjLSKfAt_uVh8tjIG0CcnQvgL6cNBA2zma1OOYSzKSSfRLQYxrfh7I_6bvfAeQF1kzbXw650JmylQmX0bDaUa5NVTi_EF9shugRwRCjn0T2VZoVaZ-QbmNpj49h8cn9uJbDygwwXZzENQqoZr22gvdI7-fBUtM4vRcuQr3_fvCIaxxX1IW60PIBS3ckeVznTMSORHXp-J30x8U2c1XQHWVAUBw63v1RnwYJYzmZEVfdMT2gQnKWvlcy8cJUAWk8EKB-VNVAM_1pe1Aanrb1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=NSfQ8sI9RVwazZQQY0WzsDAvvuqD0o84LFl5Z9S1cgC3twbkzcW1o-ZoqGDSqVmHiZjLSKfAt_uVh8tjIG0CcnQvgL6cNBA2zma1OOYSzKSSfRLQYxrfh7I_6bvfAeQF1kzbXw650JmylQmX0bDaUa5NVTi_EF9shugRwRCjn0T2VZoVaZ-QbmNpj49h8cn9uJbDygwwXZzENQqoZr22gvdI7-fBUtM4vRcuQr3_fvCIaxxX1IW60PIBS3ckeVznTMSORHXp-J30x8U2c1XQHWVAUBw63v1RnwYJYzmZEVfdMT2gQnKWvlcy8cJUAWk8EKB-VNVAM_1pe1Aanrb1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-A8pAwgdsgJZHVA1A7HETp5LZpMHd6GhaYcUI_tSCJ4Ehehh-2txHaxo5LnJM_gdKdL-zVE7Ktcq-ymnKN8aPeNIe0DS6N0Wt4vPhWpW57_ogISQ2M3v5sX5sD-ywJReKoeCBmZUfHYMeDooU0O7QNtR6e5c9qNsNLK4O1qqlftrE487ar470fB-7IqK-JcmAOsYCO5gE-TZfQ7SlGS8zLU54GISKAUAfWaTkbc4iKovVFLTh47vgKX_Izydn2Ox4K5jtcSUy1gKn8IshL5h9UhsVYXzYWkgkMAuhTbHJyf1b9gkS5A7_RAq2W3L_yDoABFQhew7PAjwDhCIueU1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHTAHBE_h5a4zOqAdiygN1OfNQn3jOtN1IsnnK9VGk66DsQlDN3c8iES_t9yLBesGI2AtF1F7Bj88D1QFWdeBmxhWpjDu1AOEDY_PavVF7C2N8e_Kta77iyxdIVI1C17oxv14tiEFjEPJ-JVINXmMRnvnN4Ji82wtHfzN1eCKvFrAnLfmuQ6MonFDMVDjmiIP71mMgNVFJayPbdYi-8G0sqKQanZEI_kVyUxjyjh1TnUMLsyYdKq_Se3gIUXZyoIP7AWFoEfocEJ8w0HhAme1ueowWnXpICOzLBplvInv8C6grqqGkeMmpgl29-7Q6EDrMtU6fWn4KGpQuA_ju69iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfVGSTxCJU69i412RM-D4a2kGOBwMJ3-A-bWahlX9QqIOC5p6Vs09Fu45JPy6AxrCQs_aRwC40fvG_bpQidFqzzgn-ixWJ8im4M7pDdJDmgrLHOtvNKXzFvEpI7VtdVA2-uOXHE7LajUVYmhwNZOvfPGZrWtLhFSlifAJ1jVIVBMSY15B06VXEi7fI4lu1t13hlL9QOQD8bjn4StbQ1qOniTw9RvQT8ZqBBp_ekqgss-jCFzVO4oHilDXRPRGZYuw5r4cHzH9FKOooU5IuGK_PhL8sgHRSl6z7zLANWlPXCqDbzTUKE_YCJljHLJDzUwL4ry7GEnk1OSbniYZGlxqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.
عراق : از طریق خط لوله انتقال نفت به ترکیه
کویت : خط لوله به عراق و ترکیه و همچنین به عربستان
بحرین : از طریق خاک عربستان و‌دریای سرخ
عربستان : صادرات از طریق سواحلش در دریای سرخ
(همین الان هم ۷۰٪ صادرات عربستان از دریای سرخه)
امارات : دور زدن تنگه و صادرات از  خلیج عمان)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6497" target="_blank">📅 17:38 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6496">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
امارات ورود هرگونه کشتی و لنج ایرانی به سواحل این کشور را ممنوع اعلام کرد و خواستار خروج فوری کشتی‌های ایرانی از سواحل این کشور شد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6496" target="_blank">📅 15:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6495">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=s7wSQxn32smK62-i-8amkYDERU8dWZbMiZmwDqmiBiCp9aiHrhQ0Gvx0fdixTMGEi4FkJHvgjGiOB_JXUYURdBXpD_UHkZnPBDSPJASGbtBlkNVfcJTp4SiSFXmDA23-Jt-1rEskI8qtg2IZBzC6I-pK6_HiUDStIPa-Y-V5NzbpKYEqzoxLCknBvK_CPdWsWgWbzO-fPKt0J8LWa5G32NHezeREssH2rRdDRO6dzn4C11VAJQ7ytEXw02WC18O40u8GOZwEz7jsQiv8iCu8fKnx-r1NaJoKyttQBUuoNWXtonf2WK-GMAao9ouzvCqRgK5pCUhG4a6wKslW2tG1cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=s7wSQxn32smK62-i-8amkYDERU8dWZbMiZmwDqmiBiCp9aiHrhQ0Gvx0fdixTMGEi4FkJHvgjGiOB_JXUYURdBXpD_UHkZnPBDSPJASGbtBlkNVfcJTp4SiSFXmDA23-Jt-1rEskI8qtg2IZBzC6I-pK6_HiUDStIPa-Y-V5NzbpKYEqzoxLCknBvK_CPdWsWgWbzO-fPKt0J8LWa5G32NHezeREssH2rRdDRO6dzn4C11VAJQ7ytEXw02WC18O40u8GOZwEz7jsQiv8iCu8fKnx-r1NaJoKyttQBUuoNWXtonf2WK-GMAao9ouzvCqRgK5pCUhG4a6wKslW2tG1cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم. می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر
همه مردم برای ایران سختی‌ها را تحمل می‌کنند!
[تحمل نکنند هم یا زندان یا کشته میشن]
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.»
اونهایی که به قول خودش بین ۳ هزار نفر رو کشتن، نامرد و وطن فروش نیستن، کسانی که به کشتار و ظلم معترض هستند، نامردن!!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6495" target="_blank">📅 12:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6494">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">جزئیات تازه از طرح تغییر رژیم ایران؛ قرار بود کردها «زیر پرچم شیروخورشید پیشروی کنند»
🔸
یک روزنامه‌نگار سرشناس اسرائیلی در گزارشی تازه نوشته که هدف حقیقی این کشور از جنگ ۴۰روزه با جمهوری اسلامی ایران، تغییر رژیم در تهران بود نه صرفاً نابودی برنامه هسته‌ای و موشکی‌اش.
🔸
نداو ایال مدعی است که ساقط کردن جمهوری اسلامی در حالی به‌عنوان هدف اصلی تعیین شده بود که نقشه راه حقیقی برای عملی کردن آن ترسیم نشده بود؛ تناسب این هدف با امکاناتی که اسرائیل در اختیار داشت به‌طور عمیق بررسی نشد، دولت بنیامین نتانیاهو هشدارهای ارتش این کشور در مورد مخاطرات این طرح را نادیده گرفت و به عواقب آن، مانند آسیب به جایگاه اسرائیل نزد آمریکا، فکر نکرده بود.
🔸
این روزنامه‌نگار در گزارشی که روز ۹ مرداد در مجلهٔ ضمیمه آخر هفتهٔ روزنامهٔ «یدیعوت آحرونوت» منتشر شد، جزئیاتی را از مباحثات کابینهٔ اسرائیل و اختلاف‌نظرها در میان مقامات ارشد سیاسی، اطلاعاتی و نظامی این کشور پیش و پس از جنگ‌های اخیر اسرائیل با ایران ارائه داده که خود آن را «اطلاعات تازه» خوانده است.
🔸
گزارش «رؤیاهای بزرگ؛ افشاگری‌های تازه دربارهٔ طرح تغییر رژیم ایران»، نتیجهٔ «یک تحقیق جامع» نداو ایال بر اساس گفت‌وگوهایش با ده منبع نظامی و سیاسی اسرائیل بوده است.
🔸
این روزنامه‌نگار مدعی است که تلاش او تصویری دقیق‌تر از پشت‌پرده‌ها در بالاترین سطوح امنیتی و سیاسی اسرائیل ترسیم می‌کند؛ فراتر از ادعاهای پیشین که دو روزنامهٔ «نیویورک‌تایمز» و «هاآرتص» در ماه‌های گذشته در خصوص تلاش دولت اسرائیل برای تغییر رژیم در ایران و جلب همکاری محمود احمدی‌نژاد، رئیس‌جمهور پیشین، به‌عنوان یک گزینهٔ رهبری منتشر کرده بودند و به‌شدت بحث‌برانگیز شد.
🔸
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، از بین بردن برنامهٔ هسته‌ای و مهار توان موشکی ایران را هدف‌های اول و دوم جنگ ۴۰ روزه اعلام کرده بود.
🔸
نتانیاهو اما از آغاز کار پنهان نکرد که هدف سوم جنگ هم فراهم کردن شرایطی برای مردم ایران است که بتوانند کار حکومت جمهوری اسلامی را یکسره کرده و اسرائیل نیز از وجود چنین رژیمی که نابودی این کشور را عملاً دنبال کرده و با تشکیل گروه‌های نیابتی در محور موسوم به «مقاومت» در اطراف اسرائیل «حلقه آتش» به پا کرده، رهایی یابد.
🔸
نداو ایال گزارش خود را حول این ادعا نوشته که «تغییر رژیم ایران» هدف واقعی جنگ بود، نه یک خواسته فرعی یا شعاری تبلیغاتی.
🔸
به نوشتهٔ او، چنین هدفی قرار بود بر اختلاف‌نظرها دربارهٔ ماهیت نهایی جنگ با ایران در میان مقام‌های اسرائیلی نقطه پایان بگذارد، در حالی که برخی از مقامات و نهادها همچنان خواهان محدود کردن جنگ به اهداف مشخص و معین نظامی بودند.
🔸
نسخه کامل این گزارش را در
وب‌سایت رادیوفردا
بخوانید.
@RadioFarda</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6494" target="_blank">📅 09:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6493">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=eH101KM-k9OO9TQFxQlq2c-lFJvv-kDK4CmqMqx8w8uB0Dut2hUi2a-ctowqY0dqhOh9sKijUI4bxIegCSGhCgXBTlHNaZ-U11k4ZGLaRn111hvskhSYM9fX3Ryf6fq2NEokOYADV_H1aPg30yMihFhd43xA1U-WRIQhpzqFuRiz8JJnN0bpCn8SkeeJAf14u7xv32j-wmQ0b3aRXg6P94w3lndRN_vePm6RTb5yAhG8qrLGdqNOxGT3bihQvyMJcLEsPEr-DUm2C3gYnpX_wn1h2B2j0KwWBDzrmf9uXrhj9dpMP16OYOXtl0qLhZ2LH4Kald7Jjg2ODLbfrJcIbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=eH101KM-k9OO9TQFxQlq2c-lFJvv-kDK4CmqMqx8w8uB0Dut2hUi2a-ctowqY0dqhOh9sKijUI4bxIegCSGhCgXBTlHNaZ-U11k4ZGLaRn111hvskhSYM9fX3Ryf6fq2NEokOYADV_H1aPg30yMihFhd43xA1U-WRIQhpzqFuRiz8JJnN0bpCn8SkeeJAf14u7xv32j-wmQ0b3aRXg6P94w3lndRN_vePm6RTb5yAhG8qrLGdqNOxGT3bihQvyMJcLEsPEr-DUm2C3gYnpX_wn1h2B2j0KwWBDzrmf9uXrhj9dpMP16OYOXtl0qLhZ2LH4Kald7Jjg2ODLbfrJcIbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای :
پزشکیان ۲۸ بار استعفا داده
و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6493" target="_blank">📅 00:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6492">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=JyVjc-vlO8_s4hqvDJe3kxWwAzC-RNK7fzed5Mvv6UiVetskxT5JCQPda1g06FEmOYU6OA6nxPiOlxSYsxcU0B9vaFM1r73TgrtcFRqPofLVlgBBSa_J4Yu9KGalLYKzKXagvbUHgrVLsnDPfdWMmTsDlDHzGEAsc5mxSEZioHzJ8hnHmYHtY8VUOv0r6tFk4vAqd8kWPQwAHWOk1tEUPEvlN_-Hh9nhX2IPFQ1hph299r5HErx_5ruTT_lS0LbjOopky46JZmgs3_KQDgFRGYtFuj2U5rYPUJN_R13uMqdtKPukrY2GRwF_CEul9kaRCauqmTMlO8dflSHmyWK7Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=JyVjc-vlO8_s4hqvDJe3kxWwAzC-RNK7fzed5Mvv6UiVetskxT5JCQPda1g06FEmOYU6OA6nxPiOlxSYsxcU0B9vaFM1r73TgrtcFRqPofLVlgBBSa_J4Yu9KGalLYKzKXagvbUHgrVLsnDPfdWMmTsDlDHzGEAsc5mxSEZioHzJ8hnHmYHtY8VUOv0r6tFk4vAqd8kWPQwAHWOk1tEUPEvlN_-Hh9nhX2IPFQ1hph299r5HErx_5ruTT_lS0LbjOopky46JZmgs3_KQDgFRGYtFuj2U5rYPUJN_R13uMqdtKPukrY2GRwF_CEul9kaRCauqmTMlO8dflSHmyWK7Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تبعیت از ولی‌فقیه بر مسئولان واجب است»
می‌دو‌نید شمر تا آخر عمرش
از اینکه در کربلا شرکت کرده بود
هیچ گونه پشیمانی نداشت!
شمر خودش از فرماندهان ارشد امام علی بود!
توی روایات اسلامی هم هست که
هر بار بحثی پیش می‌اومد دفاع می‌کرد از کارش! میگفت  تبعیت از حاکم اسلامی بر من واجبه !</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6492" target="_blank">📅 17:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6491">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=aKERpmy9PjJ44_yTq9bJsGglQEd5B_tossnZwpdgn-NDCIl6nrwu5aro5JLoZBCCW9z7r5Lc_jbYD96AaHjIo79z-y9AWEnnJZvPyGCzb1wEN02gWhOGRS4l20L0tKzGQTRXfPzs1uCPyUSKIEwy2BAyaaDlQwMlO0YEn0wBu5-v2cVYxb3YL_9u5KJmwKnoNSswizszFc739wSKBHCnrh-BS5pVNPTRIlez_hPJ59tKhJ34b5lg19RAofCPpXgqRy716Rl0UgV8nFGAvesFjtk94xr9SUL8ooybIm5tlxYtvGtvDehAjyE9jlL72LfrNvRN995_0MlIdS_z1fyjWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=aKERpmy9PjJ44_yTq9bJsGglQEd5B_tossnZwpdgn-NDCIl6nrwu5aro5JLoZBCCW9z7r5Lc_jbYD96AaHjIo79z-y9AWEnnJZvPyGCzb1wEN02gWhOGRS4l20L0tKzGQTRXfPzs1uCPyUSKIEwy2BAyaaDlQwMlO0YEn0wBu5-v2cVYxb3YL_9u5KJmwKnoNSswizszFc739wSKBHCnrh-BS5pVNPTRIlez_hPJ59tKhJ34b5lg19RAofCPpXgqRy716Rl0UgV8nFGAvesFjtk94xr9SUL8ooybIm5tlxYtvGtvDehAjyE9jlL72LfrNvRN995_0MlIdS_z1fyjWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IflRNldjjb_DV1uQrjgzw_g11gE6YWQKsOlk8tdDpnHzcgXbBF2zrIYveyUCPU_H977RnXz4_J0aEj5fNy8oSpFc7TjeYc3dzeLhpY95JVqGDPqohpUv4oZx6PgVtazEqyIAdbRteUpkamIFYF437DCYHhee1tj5F_1_TLL-JyFqgJ55hysivZtQNeO_lbtEPQN9-kXGFCya9DmVzYCbDbS3CZ9XTszGQDeEgJO8LHQ6OE8Lr0m0fbJCd2Iz7JvWtgoClMNq8xzItGEMhR1xQb2hvpeGvqNwyu99W9lwslsS30DH_XoOhoH1xnhxeKNZEcH0bPzodDn0GHnS7PfGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFyVJ7c9665f3-4tG05wGjBqhEDpNmsTGghoYNpjpA2IFotMbkyE5Zj3HWsTXeU7EwOazufFFGG72r9lHUIIktWj3r2k9CJPfI-I8KMW_F9_7nVm5MlgNqi6ckm36OVcTYnRuRnJsNNjdMT9F_p_-0uf08Im_4zVqu46_CWoZaiMsArqVUDj0sGF6qt0S_Evk3ujxeHf952XrGTtid2xsttVnvWHKHoEKg_2uY0Q6-W0o_AivcxhfRWIqdnfwNx6J0ugeyu-d5NJAhZPCuX2DVjuxiFIMGz2AT4RGLa1k65izQTaBxqAWLSBUWgK8uszs8CzeBN07qLU3tm-0IBaAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C9zmBgYTWWEgh9S_z5xZw1r0eGynz1YK3KSrT04NSXl7nee6xEvzFpsy9GskQV06yZEnassS1ob0GMcKRLOJbxhP7P2_Rr6ijBeSA8qHoWuLMG5HGAYtFn6RiyiByJUP03uiIZPywZNieDjv3eMOP5Trh00p77_7ZGKHBkz0zPcfRRWYua02dPiHNyLGuWqGmcD48fcAiVFD50BhFYY8KPqYrqzARCacOFqVUgcX06EwH6oeFkNH3A2NcfW7hCZvgWdMLhrObLjjfyS7TmMDczODntKNmEjalt0RQXMcoJtiG0kQjSOQ8GJv5WP70gbgpoav5Loy67FYSbsK3nb49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mNalE3Oq5W_YOwT3_Qq0h7jcpZ8yO18rn8OiHxmRYbkbO8QRvSSKvfiBorE5UgmyKQDyXUeqt-RI_c4Fh4g0_X2xUuthcNxtYqnSLJsxxJg_CvOG2bGDb8J_FjnRFlZBpscuAOukzvawdSfeOu6_tWA3YCaByAQCFpZCo8fnp6a3nRCc3jJbsvvVE_K77I9OxJRC_KF2UKq_xhEcB8fpM9VjWQqwQLVduO7SFqnT0rkBBfg8X4zTAbbwrmQUWCfiQnyIVfrSmmVBUnPwguaPBJDd2mUzmNSk3O0kQwi0jWXYdxlx4XsJ3M-ImTA2eG8uWeFJrtaQVdBEBWx2IHF4Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D16Aug1ZBkK8pdt9uq_bGFGwxE7wjcaYNbgwZ0GsHYqbum1h5bT7cGHC_IPkQeN7mzJhEG9D_xf92V-a0fry52M7vNnpcKPoAeXXz72excJjfbVZEES1fSCLZ1rrcbddpz2d8ZESPNxn_eiOgUWUp1op1413RROIlRRhYZekTaI9bkK_YMv_fbdcZ5ajlTMZ10-UWUhQOaC9K9_lD0kvD3iNv3ZFjblmhTOm1LUAUO0BtDWZwiHKG-9f8AEbgwqxw6MbentT9cb5ycUIP0T7cddjWOVmosqSog2zfX0v44XrIejHKQjrd17O3mWKQK5-Rgddffhd0fSc1gFyRgctPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBl89PXQp4zUT11z6qkTklfDXIlXkzQAED2hmTMyubZq0evGCUSX-exTFU8bhpk-srbHB68qiLtkQgiSD79_5F35hdHVhH5ywoMkulKe8n-ukg3vTYOuzxB5kXRUToTWiqotS8d5-v-d60Bc7okX_j6eXp17MD6QiP4qR3GaEQBnz68LkzDAmEPLzeuk9IYc0Y_4UWID8fCIqFC-EhvIAobUbcW43p69uKxezDM3DI7hgXx6gnoKjnS_6LqlDkXVGUwWjlLJrPKNrRlMZO0DWO8As0EBp6F0pGWkqdb9LyVOCtt5RC-4hHav_77nt1tdmBLp0kI-rUuSd1MyadclwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOg-ebaYOGcBxE9uMbDfZeNEkTmsikNdGBnrMh4z0ESYGI7k3DV25xQTagwOT3EejjBObdudbRffJyEg92Oggr7ZiMnmPYw_vEAPUh64c4S_XqaZJTuQ94KJEZ2kLREGJ5ZyGOMOSeJDLLiP3CiK47u34EP05HTkyH3X7enc4QpsAB-Y6YQ6UxSreyZkNiC_AX9f77LEdrQ0PUrESpr3qtBgn41DeysqgH7JxCoMN68gBgEq6o_P5tbEn1ivYAylsOjJNdULX4L0kWNVs_RVvMmMadG2sNTDGUHm-AJgopYTDkmnKgCxdd9Bzv9SwZVt9J_dTZZbe-z9FHEv04znqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gar5Hoi8-rC3eHnL4oqFW2emqxHGE3znZCx3ZFxqDlATrbQC7Wj9axcfxu5hAJCP2nJRdPFKfd3NBETQ-lvT7csud_Mhpw1a1tE-rzKdPzLsoB0mc--njOY_AjxZGMW9dHm0tAHW7860uG_QTYNUO4eJ4scJ69hCeGiOULBZAICUyO0nq-VpC5L1MdugNFwpDeAv05IYHSEkZIBM1ihrKs9qAhng-2p5KpzSfyh3CMcPFsoul6C7q7bk8fI6hJQXsyUNZvQgZr-JqAfI5xtww8o9ivoxuxt8KkVR0KqQ8M8i3DPy4bgPWaRC5ywhuaOyf09ttBv45qeKkuB52-3r0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjRarRSzYFfs0wGO41_pa4AlXxAdnNE-id0fCvs_vZAAbfdhPw0BaDlTpS2chr-T8M-h1_FbFPieQfOaHSG2CawA_U6uPE2rwm9XmM8rhtqzISwXpU4ckPfv-6_mHxtTjN7Q6COxsKS7-tLDbSVbY9nuSpPGHuIBbHK16MduH8t6ZpeN4uftZmbCtHyvs2GwVaU7XQ-g9N8vEwEo8bBB0Accq-g_27DcGAy7ItUheGK654_Ne3m51e2w7CMB2b5qFsQ_zf3Srzu3OA3fID_nzlo_p6Keceu9mzJo6fwMIhoMvG9iJjPU8DeHzpSh1NdXSt8H1boO8mG8WAYTL-0rGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرعون، جسد نخست زاده خود
را در دست دارد، زن فرعون گریه می‌کند
و موسی و هارون،
در گوشه‌ای از تصویر دیده می‌شوند.
برای مجازات فرعون، پسر او،
و نخست زادگان «همه مصری‌ها»،
«حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس
که در زندان بود.» همگی کشته شدند!
حتی! حتی نخست زادگان گاو و گوسفندهای مردم مصر!
و این تصمیم و اراده خدا بود!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox15mFMjvSnX1pnUzLPhJhzUSxv37u04H9ldWJaYU8BOI1BrODlIiAbw5Y5ZlcieuiI50Df7J0klq1Xu5v3NDAyDMS1aTQv8peCICa4E8Wd2NzILUIVxXwl-qPv3e7pErxzvAZ12ISexM5gYDXvQJ5qSW_-K5RcLQetwZWyewKhb2rBmlpyTol9iwXi-OssdVplb9GpUHKBChisbnFsI8QQnHYXhFLxbb3_V1Pp1JMUxjx2PQ8sljYWdTuMC-vb-PXNxGqZtxcv6aOIWa8jlNMoLSFEp3Ad_F1mDYStMWwwjyb_cEE0OQ99s2QCjnuIbqf5l49YB_xGTTWv-Jg2bdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWVc0ltH2-_wFkPRV6wMzasuQheTsh2XaqaZA3-e_zakNOl58XG5frZLUhZoG6aXerxUYnMrBnmp_pchPSBCrY-tsTJ1H9i3GcfrSqLS-qHr_UWAjnE-Sn_KAkXWlH897oxDkGdTAmpL_V07JntpQc6wL9fnh0VgsMRv__YC-00E3y-y1Hg00yqkVG3teFhGI6O131l6XnPlN4tLDvRuy-BQFSWIqEUprJ-pjzStNH6etwOC_59_B7-p7zOyNDnKNGivUyBGct3UxWCmV5fNc9P9st6H6gFEsg9axbqxZdmlcYVgLl79TlylK7bCq5Jt538YNJ5ls_h7obeuzV-keQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.
‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،
‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا بتونن بچه‌ دار بشن. این رو خود آل احمد نوشته،
‏او اما آنچنان ضد غرب بود، که میگفت باید از اسلام، از منبر، از مسجد، سلاح و سنگری ساخت برای مبارزه با غرب! تمام هم و غم او‌مبارزه با غرب بود. می‌گفت روحانیون تنها رهبران طبیعی مردم هستند.
‏اساسا دنبال این نبود که اسلام تقویت بشه تا مردم برن به بهشت! میگفت تقویت بشه تا با غرب مبارزه کنیم!
‏علی شریعتی و علی خامنه‌ای، از چهره‌های شاخص تحت تاثیر اندیشه‌های او بودند.
https://x.com/farahmandalipur/status/2083853984113054084?s=46</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6479" target="_blank">📅 13:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6478">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XOvtZPaxKgn7ZBjrl3f8K4Pr2HVlPWzFstDZzxu5aQ5b6hC2QyhVC0seKua1Dk6bZs51oMbvG9AsT1mtxfG2w-PYgH2cAcX1STjQLPIveu21NhZePrh6G46ICglb04a9ycZvMCQWJmPyJ9_lEV4TcU1Ict8zYQwsJBTRhrSwMhL3f1rTXNMn_AmmWg4ak6yqWrLuh9gKLt0OCr8c3Q8fPMmi7N0sQgQm1UvdHv7qf5_n4UoAiqXJ1UaBVsSVZjjJCyTUW5uS-CWhqwwwTFOg1kDxR3tobe1PtvjIJo5EmXM90P5d5_Rc3mAuhN49E0K4FCMylf2UySf2x2NkegB-pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlP4RVPEz5o9Seb3F8EaNWNHvWlESGH63e4m9QRtEE_QZr7hg0ihrag-y9ivGe9m3Y0nEwK-ERhp712angp6bL77By9xDpopvBBRSeMKCFL4Y-Yb_QqLmNkz3tW2-2_wCkthZQLzxsqToPaJvAekbo2T3pYim5TagGTVWVidXUTBU6NAEqpRorXmnINUDnZsaypwCoF9LntCzNkGHPys50apoUKsaGBjO1VYBw8no1nCv1yVNsdXG3Z2rO5qvI0FxQ22N5LFepHEM4QNqkzHd-3vXGqmdctsUQ5P1kGqtOas792mTn4_ImRNBLIJ8pFV-gqe0sB7rpDh6PheeC7-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -
سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!
تباه در تباه!
خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».
احمد شاملو - غلامحسین ساعدی - اسماعیل خوئی - منوچهر هزارخانی - هوشنگ گلشیری - باقر پرهام - محمد علی سپانلو
اینها روشنفکران ما بودن،
جامعه آرمانی اینها، ترکیب کمونیسم و اسلامگرایی بود!
از مسببان انقلاب تباه ۵۷.
از مسببان گمراهی یک نسل از ایرانیان،
از‌مسببان  تنبیه نسل‌هایی از ایرانیان که هنوز  به دنیا نیامده بودند!</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh991szoR1-pfJokKGIrAifMIlP6eCxyuIeUO2VR6UZF0nwK2GLFMHwTEO2j5S3baOGKvGgnJecFdZiokbKL92iYmrmhJEttj0FnyYtEu3Snvt2j7Rw7eBEi7bdof5St2D7rQWQ9SASllivpR3SUGMoUigZEki5HF8E8Nwk24lFeSoJChBaIfiNxSzdnL9Ozm81G3aRYlXITiZ7KXdULCiGRAJghHCmvPd-nawPjhChArDl5dr69S6hchSXdDajZHFyrDOE1g_k4rVO1TnylF3J1_8oexQ2eLr0dTnG43rZmdl2-YyyYv8tjAnQKjBGx_1i0NyWnhLIgtjXRMlW4jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=SWPysv4v-5beD_gp-nhZRxbWeJOFb-qlOoo8GMJp1BA6jF4rpWusaQD3NMUHH5z1IZIrp4qFE4XWJKyX_TUcA0rLemgF0t2hlaDgLa1O5LnmVkIqqodNFKdKV918nI1K15zqxZFrEO62Y83uuvkEUrdoedKlw8qrWHamJsy_iuxZObgBptJcd1mSaC2kXsD6jh6-wOAk1y02ij7ExUiiEgMt4yFk6CA2y9d0Jg4b9C7x6eKD3BaDZXG2wFXZo88hrGPrpLPLjrrX26ctdZD_QUxdT8Z9wyaN3WoKuK1vwbF5iCsenI89w8Bhvk4Nxp0pdN40-51-I8iZtR3a2XLJzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=SWPysv4v-5beD_gp-nhZRxbWeJOFb-qlOoo8GMJp1BA6jF4rpWusaQD3NMUHH5z1IZIrp4qFE4XWJKyX_TUcA0rLemgF0t2hlaDgLa1O5LnmVkIqqodNFKdKV918nI1K15zqxZFrEO62Y83uuvkEUrdoedKlw8qrWHamJsy_iuxZObgBptJcd1mSaC2kXsD6jh6-wOAk1y02ij7ExUiiEgMt4yFk6CA2y9d0Jg4b9C7x6eKD3BaDZXG2wFXZo88hrGPrpLPLjrrX26ctdZD_QUxdT8Z9wyaN3WoKuK1vwbF5iCsenI89w8Bhvk4Nxp0pdN40-51-I8iZtR3a2XLJzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyMVvpAjS6QcisnknLOv8tlNR_hPuOEvQQDe5Lt88qw1y991Ls5ry2GhcHxvNWy1XR_5V52PflMG3B6ufom5z7PHjCDtmeigZ8dILScfeTky_Skoy-W7k-Ln3pC0qD_DEduZtZz4WgFbdJno2--FYS_PueWaDWysBVjMBYjnWewyuCLllQwXNZ-Grh4ruXS3MQaqkFY8ZlUp2kjqG_olS5Ku0Bvs6zkcpmSz5LxQj3Op6q1PKKaru-ZUg__bwZQKGf-7t2BDZ3W1a4h8bpu2v8KhI_kmT3mDeDKTdRElcp8sHyos87jBb5AXzc7KGwyzrnHR3ddWfYQR5AhsylhAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8pMmiRe3cunZAmHhAH1ery2lwC8Pfpkqp87UpRyZBzVpJ0oOCkb46Xsw1vBlVum2VWrSLcXMcffXUSL3U1sCWQM7WxRudwEgEMVtlWSHP828YseYjFfi5G4NVanBN-nwoWhOwxbxAskAZATTKbhhShUvGC41N1n_OicrmLmgfFIwW9nuiZ34IMNiSyW7zxr3uEthzTp3Ft_C5V8PqFQ71NfjxhHDGNjlINgmDrFQHDhu7SJEJMlq8MMantqo3Ldgjf4PHfFjwZRRR9K-JsrztRwqqvYxHGlUx1QFOUzfRKAQ2cY3DweqH8tBXOqOp7TLhF6JamLFFIHeE6sm1B0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raYcR7eI-TQfCaSTbxrL9rQp5NL2BVdW3nf9NWxL40K4irRX0v36rEd-YBNmBdk70SQgSnnNXEFu33eT_kiGsrHFRUX8nU58X9rMfQE-zrYD-gSI2MDJ5NMiS2TXPrSG3cD1y6L6tHxZL9p_C82rtldg1cR92sZYBzjIRtp0tFSiWBM7FGrxay3Brr4AMxGN25zj2Vno1aflnmDRAP0Tkl6MZugIz7Elwk3DkHdTjbXl86HKVPwAEAGwUZLeLSBaSKSGX5kKKwvoMNYH5qGhhE8lCqOqWDyuzM6ViWAxuI5fJGk19bRRyMoLaisZR_wGJAAK3mEfZy7itlgYNUck4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه تنها بنزین گران شد بلکه سهمیه نیز کمتر شد.</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6472" target="_blank">📅 18:19 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6471">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏سفارت آمریکا در اسرائیل از شهروندان آمریکایی خواست خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6471" target="_blank">📅 14:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6470">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMTJPDQlhafuDVwiOCm-3DByPR1fvv7XPxMhf78shPn9v6i3vMcgINz-aMoI3SXqJy9xjoSLsYAnLopQn4eM-oRk3iIzAd8vo8GZG3mT3Gb6oaWpdyLmYDxgmeyD6VtLz80qk7H7LSRTuwFgPLj8f12XFGmyLJTvLs-RoX7k1pIuW5zdjUFYURWFhZo_JvsTA3505x4FACTlXrw9nITlhEa37ltuGnN9HuIm8wk9WhVuUxV53Sf6wojlF2G-Tqd738QGHVRIS6jIfBQ35enOqk6ti_IlkQTULFClen-CghdF8wYlJeBdKdVMl-ecH1c36-lCLAmqfWTFJko3hP5HwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6469">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‏فارس: شنیده‌شدن صدای انفجار از حوالی اسلام‌آباد غرب
🔺
دقایقی پیش صدای انفجار از حوالی اسلام‌آباد غرب شنیده شد. هنوز محل دقیق و علت وقوع این انفجار مشخص نیست.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6469" target="_blank">📅 13:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6468">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وقتی یک نماینده مجلس به‌جای سخن گفتن از پایان جنگ، حفظ جان مردم یا ساخت پناهگاه‌های عمومی، از ایجاد «شهرهای حکمرانی» در دل کوه برای حفاظت از مدیران و مسئولان سخن می‌گوید، این پرسش به‌طور طبیعی مطرح می‌شود که در این نگاه، جایگاه مردم کجاست؟
اگر قرار است منابع کشور صرف ساخت پناهگاه شود، بدیهی است که نخستین اولویت باید امنیت شهروندانی باشد که در زمان حملات، بی‌دفاع در خانه‌ها، محل کار و خیابان‌ها قرار دارند، نه مدیرانی که خود در جایگاه تصمیم‌گیری هستند. منتقدان می‌گویند این رویکرد، به‌جای آنکه دغدغه حفظ جان مردم را نشان دهد، بیش از هر چیز بر بقای ساختار قدرت متمرکز است.
مگر مردم تصمیم‌گیر آغاز یا ادامه جنگ بوده‌اند که اکنون باید بی‌پناه بمانند و سپر بلای پیامدهای آن شوند؟ اگر امنیت حق همگانی است، این حق پیش از هر چیز باید برای مردمی تضمین شود که بیشترین هزینه هر جنگ را با جان، خانه، معیشت و آینده خود می‌پردازند، نه برای حاکمانی که قرار است در «شهرهای حکمرانی» در دل کوه از خطر مصون بمانند.
اخبار جمهور</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6468" target="_blank">📅 13:21 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6467">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHNozAzmQjm8rUGFdSACCfv6iGVEO-Ov7GjXz0tH7YXJRlvfaJH6bqJTqRYdH8X2x5ikkb4ZO_Y2B24nX6YopRp5Nvd_6DS2IUdSGlhntP87qypuozdJsQXssm4p_wLvUtgiXr6v46aOTy3PYnpyJg60QmKMJ5Vln_0se9SZsLeWiYJBMwRDrRdZd6R9ejh0O_2xxovnwMCXxCpNczLBbWfKajEkiFWIbqW4vdRCNI8MuXAI7xHNEcYjLITYs4ZHQjxF9-e4ZBRIlYxn3Y3Ra7KsHfVBMe8fcb8eyqZlPPWs9hUsmdzIh0O1TNgUiEwBNGoTf53D7T3MyNGb67UEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfGbheXxPxyGQTr7fMlntXOmx6oe7rAZLIK78AB0OWqKk-wYPn9Z3mXOC0dbzqo4iny0UG9FksDKhNPM6fPQjCcb71fdEzEV3kggRttoDBD0gPBwQv4tSOB_vjpJbm-zK4y3IJIz29w81fsdiUXBWfSKf3aYGqjoQtCkgp5-c8IIZq4GSrUY0-TV2h9n1lT8agqEq2VaANfSWgw7Ib8tH6wkz38YwIsOw0Tlx0e8IgsYON-rNSho7qJuvRXXNS8r6PgbwrGI7A5lCM8j6LxghjCx3FKWeuLK9Fg-yz3AH823bBKusC7dLF4DYeUFQHortKaAKXzj8BEHl7l8tsevng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R08-3_pF4VgIjCPWeDbjJgbXmKa5PcCsT-c9Z06R3nObXfmI_V270EHa_9JF1rZSdk1qYbOF03LtuMkAsGp0xl5Ws2qpU_uYgqZpI3ydksJm9CohfPnd4bxOgsblVod9MAmmZKSH79JRSgA9Ij18N-hAkd2LtmoK6bqbquQUfVTamLdpMSuo55GzO3Boxf6Jb4MubPhbGEHDOS-Gj8XHwPKHfAegbyK_TyuY2ReIT7TgqcL0LzFD3naYJi3NZ_RdM31A43U-m1yDL5_8z5gj_hu093JqPUxT-DyesRZJaVCOcNY4PEfcsL3Opw5wJoJzzo5F4ohLpIFqtRJr61ONMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNVzFpB8pK8_k2kztvGLvvxQzCOgSegHVunacPOB79b7X3QjTUPIuX-O49xH_oIf2v7dzf9MUEskUKgU-8fMMy9O9ZVf_tjgvRf53ezeoUI8JDVCXVpReDwCet78GtHYvwmiRJlwXQLduveiJ6usHB56iaFIBFKWeowLVwjTJq-qLOWIwWKyr0fY_VyLA-IDxo8VF4HdKsYgRwWtZrGhZhzQxWNWnCDQVpkNvjzavjDfhXVSnEnbQ2HI58zr3TwF0csxvDpWoc0MqAtx0_0HFmU0u2CGnt4fnwCq6kbm49J-1KZKH2TCUIeAT_P9zVzmT_SpraYHuiklAynY7zHWyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
دولت ایتالیا آزادی رفت و آمد هوایی و دریایی
بین ایتالیا و اسپانیا رو به طور موقت لغو کرد!
این بدین معناست که تا اطلاع ثانوی،
پروازهایی که از اسپانیا به مقصد ایتالیا است،
دولت ایتالیا مسافران آن را کنترل خواهد کرد.
اقدام دولت راستگرای خانم ملونی،
فشار بر دولت چپگرای اسپانیا را افزایش می‌دهد.
دولت پدرو سانچز هم اکنون نیز دارای کمترین حمایت شده و پیش‌بینی‌ها حکایت از آن دارند که در انتخابات سال آینده از قدرت کنار خواهد رفت
گرچه برخی از راستگرایان امیدوارند با انجام انتخابات زودهنگام، انتقال قدرت سریعتر انجام شود.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6464" target="_blank">📅 23:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6463">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6463" target="_blank">📅 19:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6462">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
ترامپ : می‌گویند که حمله سایبری به سیستم آب مینه‌سوتا، کار جمهوری اسلامی بود، ولی من اینطوری فکر نمیکنم! فکر میکنم مقصر خود مقامات مینه‌سوتا باشن.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6462" target="_blank">📅 19:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6461">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا  نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6461" target="_blank">📅 18:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6460">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اعتراض اسپانیایی‌های ساکن سئوتا
نسبت به ورود گسترده مهاجرین به این شهر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6460" target="_blank">📅 18:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6459">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=E0cs7oE_vKnbNblp5drPVCgLEH-qxQ0EVLYOjirIuu9e8LIrumOjhq-ZuCdODPCudSDqMw5mhh88wb-Ch41FRSNy-q6opDSBPrIj9Omhicy9m60idng0tfaEMbqEy_3fUxprdgBJ-14mlT75NuBr0bTTBLFKUVYgr7B36LNAtBHUkOC3GeNgA2JID4XWWz8M30xPjzQUp5UZULdGGtCM8oF7zqxCqDGYneOKHdQGQTpCOMgYwgRU7QOGeIjiFPCoQx8l-QQWAWnRM74vmDyZRyLOzyrfCvcxl1aZ9Rduk04cB37gu6Kx_WEKs2OVC6xV6O2Ry_iJU4yeLkhhRwoI8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=E0cs7oE_vKnbNblp5drPVCgLEH-qxQ0EVLYOjirIuu9e8LIrumOjhq-ZuCdODPCudSDqMw5mhh88wb-Ch41FRSNy-q6opDSBPrIj9Omhicy9m60idng0tfaEMbqEy_3fUxprdgBJ-14mlT75NuBr0bTTBLFKUVYgr7B36LNAtBHUkOC3GeNgA2JID4XWWz8M30xPjzQUp5UZULdGGtCM8oF7zqxCqDGYneOKHdQGQTpCOMgYwgRU7QOGeIjiFPCoQx8l-QQWAWnRM74vmDyZRyLOzyrfCvcxl1aZ9Rduk04cB37gu6Kx_WEKs2OVC6xV6O2Ry_iJU4yeLkhhRwoI8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0zejsH78PFSnHtsYCQvpcms88m9wlp2B_eZShXQ5eyhMWBy3P2Xs71g4C-y-yl5xgv-FjatpmAw_8BWTtc1t1bosKg3nr9-uqTFBikzeyBXtol50HBTNSk7ipPixJTWo-Ul-Swv71eK0NXOZjmAACTsEWA6XeDi4zaUUQ-k2VJn32oT6modnxeHPWvHAuqMJHVcKf6TPGJD0HTA34m1valpyYl0zSb8Wtq3TKg9NetASELxk2-rRfOdCNIP2C3BITLyiMCZghIgHNmg-kYNwmJh1kTkTRjG0BSq1EM5Q3FDpgvLXLLgXkvu42BbAaM-Rr9Kc7Qle8zH79XjACspwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته مهم :  چرا از دولت سانچز انتقاد میشه؟  به خاطر اینکه این پرونده حدود ۲ سال باز بود و مشخص بود که یک «خلا قانونی» وجود داره! و رای دادگاه سئوتا، ۲ سال پیش این مورد رو عیان کرده بود!  دادگاه هم قرار نیست طرف دولت رو بگیره!  انتظاری ازش نمیره!   اصلا دادگاه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6458" target="_blank">📅 18:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6457">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اینها که رد شدن روی شبکه‌های اجتماعی نوشتن که پلیس هیچ کاری به ما نداشت!  و فهمیدن اگه از طریق دریا بیان، دیگه پلیس دستگیر نمیکنه و …..!  خبر سریعا از طریق شبکه‌های اجتماعی دست به دست شد، چند روز پیش مثلا یهو ۲۰۰ نفر وارد شدند، اینها هم نوشتن که آقا مسیر دریا…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6457" target="_blank">📅 18:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6456">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvGzLuCzn6mA7PvWB15lw_tr1zO_k9HC9q_ibDVwIHi0f4k7IKOvlbaCmfUpLDSn31AbCu5rqHqh1ATOMKKA9cMID14YGcny7p9mjpybNxCoTQiaBkwtgFgk99se3u6eUV5AeMrchfFEQyQdiviVtibrCxHXvoITZRnN-JTDaTDRMoT4LwXQgpKOxE1adADp1KPwI4FRbWw6ZSN75EK6vYCh5r244AA6_vytJmJGoYFuN9jrMpJTOd425wNA5a3NUiX1288GaMJ-EvtUJzeNeWx4YviCPNSq7ZjSt3cT8jHWubSxE9loteCKQQwuSq3NWNVqlGvOue0YlU1N_HZB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tMKI3d3Ojc1wDAdkj-bZ3Iy66wnFKGZ48WLqRmW6yEIQ_kj86d3gun80O4xA57hTO88-Gs4fg2qylyrz5qnWUm25xbtlM1ZebS6PstPodMQXfzj3D-c4whWGc2t43zPuSKGq24ROYIdmIOhHQQNtzELxJmxvabkAat9aBlE3zJsnWQN9wtG6QIMZyOKh4EO4ArhUEsoR9Bwlg7RqnsGpEmogZ0vBJgCN4jlkap5Z1XccOMRLQqeRJemYKW6JvQ-3vyyNwYTfJI3sSRyVE3LNdfGRXAU-JIKJ-JSM2DZqEJO_WmHbnE-L6yUxrewNxUI8yJ0c80i6-2KLcebenxBjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0_i8j9sNoJ525gcl8XNnBKgM_Sqw8XtipjtDQEAzXTyYYq7LOKaau8-JMvTVTTHJ-8qDvMzhXqvFkfiZEudNdgYMgoSFbEgos371csNqT7UfpdDkDslAllBgRE7OiQq-h6M6bu9hQyToSqTXckm8EicMU6rbAiQrkQoV1yxWchsHozc01Mt4znzxqzwy6jjVt43extuWTYOcd9PWJrdqtgQwfBpZxKhRXDSK58gJfo-03fqLrP46X8tqoTECXgVF5JyK1QYA2NjEtPD4hqXvJyFUqAf5buvjFPQLE25s2iVLJyEJer-PwkDx0jMjz2jDo9FsMN6vxpwDMU6QdoFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShK_xemJusyYVvVnX11WQsc-MIokJNEtL3gCU9hbtiVX9yZ-UcTHOmLyEYC0fq8gnQxNFtKLH7ndQ9JG441XQOKVG7B6pQ5xVLBHtT42KzJDYLnQhDjYGUHSUuaBz19QjJenPFsZSlZ5cFP-dYhXb4LFK8Xl0srY9xo0h7cpAVgcLSIyob6T5YYsoMscn-3hYrElPmco7Uzd4qjKyrwiZ9eF3ISuNSkaf-RxM2GrafXkHIYplygfjbXIPHU-bdkTnVisMZeak4V7Hlbxbvet5xBkHSEawtSLyW785z64QB-Vzs6yfPt5zSNFJzyS2KfWZVPIwwjbqewxyLWytAZocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-kqYd1saGlvk9hDsBNmMBHVk5adR904aQH2ge8WijDDld6mjTjQfhPAN6l1LeEnwd7DFOS2SWeX0dRmoaAoBH-A1FEtfN89Thc9PohTexi4gTE7RIzUhWJiOSExUZrICgsjj2pSDukc8kv4XcEaLy81SwHdUxR1SrMzzaqeAI3ZhUOQV1vOZ8xeY5F2eA48Ez1l-y3tnuXJ8PORQY3F0QPZ31fqtQqdLQ5ugO_yBFNmc0eQwczev2Fu9p0aIoPZeRG_6vlqtA3V15z7P-WvFkGFlRZ2A9A4sb7XLdBXJNJuRJqJNKOCwGKJYuKbUNQr_ysB1Jg94OLNhGO8QmyW8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIqfV-6TZ_8R_fHaNBG0KMbpnIZ8tKgEQwnZ-y21ToFH22jzvP5LKeHxXUusDocs6pidYjJ2UMekph8qcnDZM79VfAUXqQp3Pj45FKYsUAy6LCJEAXlMV9bQgZdzhC6Lx-YJK062LDl4TEMNLehFTBW6sg80As381L1loRY3B6Oe8PKW3H1ensjrhUO5wjbkPB69MMcExDiS-nQNGot6sY8vTUCVzRIj89-PshnWyDpKQOTf8w5k3RO1RpLW_dj-rc6Jk3I9Cq9a4WVtgnxtzoIc9ZcMEw9U3M9jX6ihfNUKFyGFG9vUgfW7KlvgGImEtdPfVr62dYaUCsWXZ8OJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا
دقیقا چیه؟ و مشکل از کجا شروع شده؟
چرا انتقادها به سمت دولت اسپانیا رفته؟
۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،
حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند.
این خبری که می‌بنید و تصویر هم مال همون سال ۲۰۲۱ است که پلیس اسپانیا مهاجران غیرقانونی رو دستگیر کرده.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6451" target="_blank">📅 17:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6450">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=nJxIWYUE6zVBYmsb6LNJ9go8FR0nm4p0OwYOiCNvjUlyi0aHPA7UT3qYnwF_eV0jiBPj9DScJA4Nn5O_QCCJnLOR1QrAoiwggLiNtMo3zTsXLQSBBrFBHTcBrGqht1QZYr9kMdCT5ZoR_ChMxXVEiLdWPOWEwYGZD0BXuzgHej_tNnsOSdHzvvyRZ00obe-7tgkwazp4A33M-BSNj27IEy-tEzkyjp_HS-evRTRxp4-ktAproPcUYlZ4Mzr6cbAxuUDNz2-rvP1hXOdFI8KfirbkHaKo0leN8KYH56gjQS6Ns1rLDY-NxJ1HtBJOwRIE7J7zuC2zgwPO87K2C9uEqn6eEgF3ZY802wPTbZTWsFpLt2--YnOSb7xtzGNlEa-WH-hp-rzEDvN2kRfGJEQd9UCe-5fPVn_h3LBhsmThs_YQw29dRPKoGfqmqKQGYEqGYNckbFmPLIqdg-yzJLVag78HsfHpI0k5_k_P4n0exLzsk-qrIihs7nyHDHeUnRI6dZRR4cNak3u38VwyF901tzPV75jYfslwsITvPNuUqR5qEPTfvU625oIl8lRPPQEteL1-wGeyMCJdSa3SZhbAhFi1Ofk8pvYh0gfH5MoFhq_xFENTGMOsG6KOYaZOz928RCu-S9C4p2SJheJu6-C4yTBOryETkYY6nWXWSVcxzVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=nJxIWYUE6zVBYmsb6LNJ9go8FR0nm4p0OwYOiCNvjUlyi0aHPA7UT3qYnwF_eV0jiBPj9DScJA4Nn5O_QCCJnLOR1QrAoiwggLiNtMo3zTsXLQSBBrFBHTcBrGqht1QZYr9kMdCT5ZoR_ChMxXVEiLdWPOWEwYGZD0BXuzgHej_tNnsOSdHzvvyRZ00obe-7tgkwazp4A33M-BSNj27IEy-tEzkyjp_HS-evRTRxp4-ktAproPcUYlZ4Mzr6cbAxuUDNz2-rvP1hXOdFI8KfirbkHaKo0leN8KYH56gjQS6Ns1rLDY-NxJ1HtBJOwRIE7J7zuC2zgwPO87K2C9uEqn6eEgF3ZY802wPTbZTWsFpLt2--YnOSb7xtzGNlEa-WH-hp-rzEDvN2kRfGJEQd9UCe-5fPVn_h3LBhsmThs_YQw29dRPKoGfqmqKQGYEqGYNckbFmPLIqdg-yzJLVag78HsfHpI0k5_k_P4n0exLzsk-qrIihs7nyHDHeUnRI6dZRR4cNak3u38VwyF901tzPV75jYfslwsITvPNuUqR5qEPTfvU625oIl8lRPPQEteL1-wGeyMCJdSa3SZhbAhFi1Ofk8pvYh0gfH5MoFhq_xFENTGMOsG6KOYaZOz928RCu-S9C4p2SJheJu6-C4yTBOryETkYY6nWXWSVcxzVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد یکی از سیاستمداران اسپانیایی
که مخالف  دولت پدرو سانچز است :
می‌دونید که پدرو سانچز بهترین دوست
آیت‌الله‌ها (جمهوری اسلامی) در اروپاست
و دوست خوب رژیم مادورو بود.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6450" target="_blank">📅 14:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6448">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=PS08zx5RA4Hb9hUPrRcxzLmkFo23fstE3uRV5XZ4KyR7fB_5SK1T6kTRx2opJ7oYR11rEnB_f7YLcqolSqXhtqQ0_cOyZzXF_HstwZpg8q6T-xhVD9b_7StTC-SxymgAatLETcPo7ttbIPHhKCNuQqLTtakp_D46Mahp_ZveLIT6F3cfz-nu-gWF1lXqI8kD7otOyLVXJ1ECnxDFyBWnxhSdwqGX1GCdok0DoDEa-2Q5OBKW2CUXjD17B--GO84fyyFKABUhtVgtnkRwqDTjWKATCn5D36yKHfzIVeVyM4sLOvmwS5-zn3qVfBXBNFp9fIAcqJiu2nSri-Dxg2B_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=PS08zx5RA4Hb9hUPrRcxzLmkFo23fstE3uRV5XZ4KyR7fB_5SK1T6kTRx2opJ7oYR11rEnB_f7YLcqolSqXhtqQ0_cOyZzXF_HstwZpg8q6T-xhVD9b_7StTC-SxymgAatLETcPo7ttbIPHhKCNuQqLTtakp_D46Mahp_ZveLIT6F3cfz-nu-gWF1lXqI8kD7otOyLVXJ1ECnxDFyBWnxhSdwqGX1GCdok0DoDEa-2Q5OBKW2CUXjD17B--GO84fyyFKABUhtVgtnkRwqDTjWKATCn5D36yKHfzIVeVyM4sLOvmwS5-zn3qVfBXBNFp9fIAcqJiu2nSri-Dxg2B_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MELyhal80V1TYXJxHnsXptdCBlI3iQgthdlgEQRDW_7C95dYWX7cDGuhNsjEEXqHGCRCsGONPMtmSu9AtIROPPp6_RfH_77cuwnZ9y_B0UlN2v2pC7AlIprqITM8KlVx5sc_p7-Y0tFSgezzimIY-KhTRxF7-zX-gLJ0-nh_L7q9wIKM8DgcNoAbrh255QVFCMQH6h6rsvvqckDzWyknjoSs94qMdHb0Vgc0mcVjBHXwHSQwlubAcJY_OiHVjXW8HuSZ2NInyVySUdodr79-vrYVmSRkWPPnVxaL-Cqwd6T_bAcrf7OCLH_xWny1EiSy5NYCuFox3h_Mll_KG2QATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟
دستاوردش برای انسان چی بود؟؟
به اندازه یک قرص سر درد،
تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟
اینها روشنفکرهای ما بودن!!
این‌ها بت‌های یک نسل از ایرانی‌ها بودن
که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6447" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6445">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGG5R9Qt5Qp2G0Hic6dicgLpKrnsiLyBQPdMbb8U2COuEuvGP3fDkS108G6yOINR_7-3F0tyF8YLAghyU1BhsMbcsyemSKBzbEezZB7wONcBrPNanwNbqOPooCYrbM2jibTVq711CVCZLCYKfhlhETZIjOx_o7hdyynz-hnHjvAPx_0jCFgxwcRZ1zPNG8sEu05NuNN1Y2fwnpbvp28F4xcJzRH-6LdnyqhGw4W7UK7_Seu6Fxy85dbWseJ8yc0y_nxqCZVrjnvLuZFITeCoRSqz3mrKn6jndp55JjKedpdf9ILDFuVE0CjAm_8gGCIC8ap2cXBpAkghSzneHGcEVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=RmIF5tXlwIWcJxn5rG6hjJoURKbW5PlwPAuZpH7pSJI_mTTerPJPmcQ7qgKNoXarMXjIpSx8fnL9WiJ4ZxN56PTmyfLqUOaNV3CkpQP1mb_epZf-49zo3lLIi8bfXBbWJ7mLkaYrD6NxYrCg9E6PgAbwQNByKn72nNONAAvUQkBWm_ASmBaFhB5As87N8qUdH2yfnVCu1lH_sj85urFAR5Jx7GttN4Ltro0mzgzfn4Dtc5z2cMDMb475CN21mY0gVabwcMGtWKLJfO1shg7CdwP1xpNHzoky8zvYd41_p09zWqVxTLHnnWJGL34rfbQ-KZFnaSf2M2a65ifNh6ULOYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=RmIF5tXlwIWcJxn5rG6hjJoURKbW5PlwPAuZpH7pSJI_mTTerPJPmcQ7qgKNoXarMXjIpSx8fnL9WiJ4ZxN56PTmyfLqUOaNV3CkpQP1mb_epZf-49zo3lLIi8bfXBbWJ7mLkaYrD6NxYrCg9E6PgAbwQNByKn72nNONAAvUQkBWm_ASmBaFhB5As87N8qUdH2yfnVCu1lH_sj85urFAR5Jx7GttN4Ltro0mzgzfn4Dtc5z2cMDMb475CN21mY0gVabwcMGtWKLJfO1shg7CdwP1xpNHzoky8zvYd41_p09zWqVxTLHnnWJGL34rfbQ-KZFnaSf2M2a65ifNh6ULOYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJSrDquuVqNCS7mhAB94aI7yMXzoeOZjztmWYhsOfQlWkCcJyk0pE6wYikZ0o0OEjsfOh1Mm3UyONDgW7Bm24ALDcqgIQfFZtf2DChCSF317YGO6xsPRu83ye1VynNRfl8c5SFpjCe12lElyoirQkwbA5ruWuZ49MdEYYlAXQ3cKqutMVuqVqvtD1zsjZz16PRAYPNAOojC5J2CVJlOnLvb97xKigSYV6zlC0wxSTUkKNgZ13SGbZrhWLA14UyKzRh8GjjnUtf9yCSnrObSszzgikwooDuazx5N5AihV1O0bMTqTTg871_SquLdYHnw5yjmQjV0k-2lsp0slL5f3vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس عراقچی ۶-۷ جمله نوشته که خط به خطش دروغه!
نوشته که مصر یک شریک مهم منطقه‌ای برای ماست و نمی‌دونم امنیتش برای ما فوق‌العاده مهمه!
در حالی که مصر و جمهوری اسلامی ۴۷ ساله هیچ رابطه‌ای ندارن و مصر حتی ویزای توریستی هم به شهروندان ایرانی نمیده!
همون موقع که پروازهای جهانی در اوج بود، حتی یک پرواز بین دو کشور هم نبود!
نوشته که اسرائیل علیه اتحاد و همبستگی اسلامی است!!
مصر حتی برای کشته شدن خامنه‌ای، یک خط تسلیت هم نفرستاد! براش این اندازه هم اهمیتی نداشت! کدوم همبستگی؟؟!
🔺
دیروز به دو کشتی حامل گاز مایع در مصر حمله پهپادی شد، دو تن از مقامات ج‌ا به روباز گفتن این فقط یک هشدار بوده از سوی ما.
دمپایی پوشان یمنی هم گفتن کار ما نبوده!
حالا این اومده میگه ما روابط مهمی داریم و همبستگی اسلامی!!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6444" target="_blank">📅 13:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6443">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKNLvElIeReHJ9WD9BAPf17jEmMjbf5MtKF81LJU6eimAvOSEXCF5bVyZ8bzeOj4dFAO-OG1mGr-eO87IW0ImG4eJvJC_FzpXk-FTfSsJgA0M2G5c5nRkDqCpqbqQlDHMkqhdaVBYbdsyoMyqkkqTgk6S5X4RLwZfGETQ552PW-U6eG8qDl1VdXs_R6-3WauiFHwVHkELjrSZZ8jrcRM4g4_H0YpqkaB5QZ6quZeglbP_BnXh_Lpp7eamGzBR-pZrlvDkO9I3AUw5qZkI0OERQkIsm2dOcDS4EGuUUIPFoQKLe-gV7xQZUPF9yLYrmbXs4XOdDCsX0J9M_twD44WmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgGz9eD7RG_1ylnQqx44Ig-r9pHA-j7o2jf_JIx88kENYT6nxnoZzR7XLGlUxP1cYevDhEkJecUkoyHYxAcwNDpGc-SnSvoXm9xvpwu-DD8GC8qKeGK_vVdeueVFVomU2t1mo5DmIOWVVhSICjxu3DJ80DfBx67vdr5_DNKAZE_QRKl4-82cO69XtKWPFot2FU0BBGDX907toJ9tXonG7sKtu-ioYl_x_cksofE6Ykf62Q-MuZc6vOmZtJvUx0JEu5MyZtPgcG5ZSv0bEcY2rorU-H_NFj848OrdwcHWSJ4_WySPVs9aEiMfjfg90w5SgDErSDCq1ZOLwaUmBJQWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵۰ هزار نفر عمدتا مردان جوان
در ۲۴ ساعت
گذشته وارد شهر ۸۰ هزار نفری
سئوتا در اسپانیا شدند.
🔺
احضار سفیر ایتالیا در مادرید.
در پی انتقادهای دولت ایتالیا به دولت چپگرای «سانچز» در عدم کنترل مرزها
و درخواست بستن فضای شینگن بر روی اسپانیا، موجب خشم دولت اسپانیا شده است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6442" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6441">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UEVpZKrmqWFj92K7sRCfvNpUVhN7dF9R6WD7x-74HK49zznkWJ2qzQcErH9rw6ZoYynbtc22DopQpcmio9bIFDFqqxfC5CBGixUieRJSUK-0IlaCsp8T6XKt6NioNv4VMpQqX4_OhuSRXSj5YN7Ms46sGwGZIbvrp-FFl1QVUHD5BlQhVJYoHYgpTl-OEsspR7DZl4a6XlLW85pz-SZPtKP6Fgx3TcC64Vr-T1PBbJkFbtpI5xQOnezTx-ygj2kMMySx27JDw8aFwaEdQWzngSE1dtldKehfjYzs0BsEza_0XY7reMdwqt375zeeOnvZBrJp-1MjQyPNoQelZn8W9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه بار هم درباره حجاب نوشتم،
در حالی که اکثر زنان جهان اسلام
(نمیگم همه‌شون، ولی اکثریتشون)
دوست دارند مثل زن‌های غربی لباس بپوشن و…..
زنان غربی هیچ تمایل و انگیزه ای
به لباس‌های زنان کشورهای اسلامی و چادر و مقنعه
و عبا و نقاب و برقع و پوشیه و ……. ندارند!
نیاز نیست حاصل تمدنی که اسلام
و جامعه‌ای که ساخته رو در ده تا کتاب قطور جستجو کرد! همینکه جمهوری اسلامی با حکم
«۷۰ ضربه شلاق» و «گشت ارشاد» و بگیر و ببند و پلمب، ظاهر حکومت و فرهنگ اسلامی رو حفظ میکنه، نشون میده، این تمدنی که میگن،  یک آدم برفی و یک توهم بیش نیست!  که به سرعت آب میشه و میره!
فعلا پول نفت پشت سرشه و بگیر و ببند!
حاصل ۱۴۰۰ سال عمر و ریختن ثروت و اموال مردم ده‌ها
کشور برای صدها سال به پای این درخت، هیچی نبوده!
نه هنر، نه علوم انسانی، نه صنعت، هیچی!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6441" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6440">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBpzEn4_-2FHcPKFzXwfQ8UprMLSNP8gl7b8WQUYCoSe9Z3HfeD9kMvHkGGaipXBvNwXTC_BPNu7oTMD758Z4aP4Jp1-D9-Xj2Yywh4QPwTZF10SnHK_CMpwWU_s8DdL_gNW6-5Y10Ph398YVGKy8xZV8Zwym_rh9xf5jVlpuCMhp1wjkaxM7-PYhSHznP63bE_fhMH5LqxJxaP3DCZpOYpMC4UhoC8SNAZ1S7zZ24rqlVS5_Us-B73kKH5WBQkRBO2t2hqeVM0McDR0F_8r5gDw1ob6Fx_XGz_1A5H_etInxC8X4EN79zrECYzwXZMnOLEDA5zjUx6e6RqsXrPHyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJWycIrn1FcNb57LDsZms4J34almQYJ7ChzdybDi8ddvls7fFVPJoc6gVQmJ3AmCwWtJJPawNvyndOAOYKV2_g2bNdsNg9EoSAWwitBbNaNkGYv0YpQdvVPKUz1vv1GsGDZWGMy-R8fVOS-V_FgTRkvtnRQ2KFZMo9C2LbEM2Ejg7Y2hHCKIvId8aIlmjNPDPLXoGJo6GXYe3h1cwo81D6b096r833njESkFXTFK7lUyewv8HRCQ1O4S6PALZEG9XALQk9NkfaBeyuyso6hgj2grsJv5A4B6v09i3C6FiRJTYeunPhq6AN9oMveZe5ziaUxAVJtrOFKDUXjX8MvU8rVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=DhXAyoJPTontX84o6DyJIAEe2y45_OTOi9ukfE80_TgXVT_nEob-JV7wWlOxYykNkC156oRQxW2GfXrXL6hztzArz4yBRPYxhVgU2rdf0CREtYBC1jwSH42CMwTV-4akA892dz3DhC0zI3ookcNXXS_ZyUfvV49pRM8g4zl_riQN-S9-jlV7wdXX56Fuk7SNt9b1Ht7x0DfKa1xt2vbFZcTq8Gm7f0I3JP0fjvIG0VrAiNexpkgPV49pfNXHvB6BnDph9HYL3mt367AJD39FepSPgvCz9AiJ54qAnTgHFyS-5opN3st8D8WmUmU548uLpkKkntW2wmlquc3BoMGaJWycIrn1FcNb57LDsZms4J34almQYJ7ChzdybDi8ddvls7fFVPJoc6gVQmJ3AmCwWtJJPawNvyndOAOYKV2_g2bNdsNg9EoSAWwitBbNaNkGYv0YpQdvVPKUz1vv1GsGDZWGMy-R8fVOS-V_FgTRkvtnRQ2KFZMo9C2LbEM2Ejg7Y2hHCKIvId8aIlmjNPDPLXoGJo6GXYe3h1cwo81D6b096r833njESkFXTFK7lUyewv8HRCQ1O4S6PALZEG9XALQk9NkfaBeyuyso6hgj2grsJv5A4B6v09i3C6FiRJTYeunPhq6AN9oMveZe5ziaUxAVJtrOFKDUXjX8MvU8rVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
