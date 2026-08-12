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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 17:44:53</div>
<hr>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9kM_hksh6LgTIi6Vp6GqAbNyWaND0nxhEzNctnoG3XROLX06ZEEkbTUEX-nt0GY8WHy7EYUkmCqCPypLNZvf_h_aeng-QcrPe-XZGVksrs2JIGHSrWsDKqkIzGL2ng8r1mUzqgHk4mM6U1spoZyO2AzIpklh1-UGRmMA1iO9Ce4AJ4LH4RGYn2RvmJSYQ6Zn02Ssz47zuRLoERp-K9XwKJ3tPideqxmbL6x7L_zVm_R7Ae5_1sr5g5lgShRpcoP47Iu8Uc0j-Awog7C06ErG_JgezXr49RDVuzPOxxxKbkIW6RvKL_3RrZETMED5ee4uPTKxNqG1_ffAEcXjA7Pag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFgTgBAaDE2Br7NXyrmnp5A7QvsRMXp2Ck7ehAh6P5elVRLqj4DKosPXIv5ny_gZodWWg5Vlp2w-2LdLpg6w8Ey9BOso-f_FOtcjTUS5LCCGQk12txvQ614Jvec3C1oK6_FJjC-JMMpFpqaOwzXq-j7MF8bvs4tqiztpIeR_i2ZGw78Gzgs-DSVzwgbNjCKM1kQOk_Q8twxYata4i2OS1XTBLxgfYLrGIn8PJWUA_vq_2FnvYdkIOqe942jVvaZJqta3eTKmdpUzVYwBDt_LCBn2nr-VsMuDAF4yQwpPthLwrxsBlB76FANGE3ai0AZPiF6hgVrNudc-oWl3gGYypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehRwrwTTfHTZEAAkuJ_fPFbkAduzwzO3PLrfBTEFOmt5BGOdngG8rBZIawftJ-uHzaXl7GFeHuKoijh_6O4IM8PYDEeGdR-li8aVgioYJtVRty9JWWYONpLs6vCiY4bCSkcKdX2mvQqp1jTUSHku-RIS24H46sJmIDySazYMPRFn0zgSasgib5KOJTAZ6xb6K3rtRzbGD3BHTGPZzdQuRHKctmL-vcZsWlW-ti7zrhI0eExQ1CwoQLT2nN6NMOUmSpo5Tt9Zzhj2w8Svl5AH5HMIfFPp5jQ43r5Qjs62h9eU3zAZAHlydCvYITWRaEJf9S-ekXkbgBRudTefZIkMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHmST5RLWGJmfjAQWAb1iXfv3Tjz2HUDKP9K_GvT4cuqb0eDShKRpG-dxB3GTSdld1koPqljudy4vBLbpWolcDJaivBdxF5DPKY6-KmvU7nAoQS_kveJaWRoOmUIipJoQGALbD_I7bxOeJvMiIQ49YnW7OD9SoIKBTgtnKjjpa8mWMGCXgFXd_SyEwTCzj0jWcCV0z4weyzl-2-wJdzzjtJefxqdF_Ej8I9lmGfug04FQ1IUIMrH7idWoNrWJxIyeygYO1KExQvN4lRoQk9CjaTwj7kp-9nRXif7uRjP8dZhLO4V8Rj8rvIcBaXRBhNZc4fP88moUg8XnyzUY6FzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=f76yVhF6o0FdNq6-sBbdzwb_6dYE_hropfzheEJ6c7txt9pu-6Gba8vZdLBD2SjZhpatT9GmgWYLa1KmEYUIFKYrmeD6dihoTytbreS0hYqyCtM9J9n35iHubtUvQUR76ZWldsNPb137a5hvWItzryn51lGsF1rEPuAq7_rkapkqetxuajxL6Nth9vX8XXcX1hzvTfoGHfiTOm6ae8vXtn1AI-pi11u5gdohx0eByLNILwFtfSfyZ04HKahnxGRMTdBidiICMroJ_bs_Q-TBWtzvXmGUiPOZmjBaj0obz7ZFoY_YJrRO_xNnZmi4M48psXsj1CjH7pjLqItRJd7Zgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=f76yVhF6o0FdNq6-sBbdzwb_6dYE_hropfzheEJ6c7txt9pu-6Gba8vZdLBD2SjZhpatT9GmgWYLa1KmEYUIFKYrmeD6dihoTytbreS0hYqyCtM9J9n35iHubtUvQUR76ZWldsNPb137a5hvWItzryn51lGsF1rEPuAq7_rkapkqetxuajxL6Nth9vX8XXcX1hzvTfoGHfiTOm6ae8vXtn1AI-pi11u5gdohx0eByLNILwFtfSfyZ04HKahnxGRMTdBidiICMroJ_bs_Q-TBWtzvXmGUiPOZmjBaj0obz7ZFoY_YJrRO_xNnZmi4M48psXsj1CjH7pjLqItRJd7Zgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn7E-ZJobfeTNH6AGrbUcLVU4xpDAQflfyxRmqaq4zthGf8XXJ_eJxunGEWa-w4MWiev1l5jMc_wVpqFXINVXW-xl2lOHB4yNmiAYehDikmNPiyLT_KgwEVnS1g-9oLE1ThqxWVmgJmnUXbwZietSRNa0FVtNAz08624GjD4ycxK4boMioW6HcZ6fXc-UwgkGVnhuOEp4cAVfUTZV7accw3kaY6EUVovM3YAu0aVnBct4u3Y02OJ1pxzgVQ0mYiLwFNsAOg-SRcL24K5ByK8nRelCVkBYKGJqBwvoFeRw3w_UvMBxhJZDTPJwxCpOASVujvckgr4nJLvQ0H3iACQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESrxsxZhqCdJgKjFQ42B4dVG2aeXpQlVwIRj5HoHDsNJXTVqPYanTXzQOVIrV_ywKRMNh5YU-5nPYIpN-SMXejObcSk8bp4YdcLM4qq3zgJuxkvtS8Z3TWpisMrmmheaZ0NkR9KsK4-4lkeF2J6X0l-tPL0bpanO1o3Ply4VnM1CN2Lq_nKO_PrnqQHxImyOMRvNzm9kDoPBbV7vEDvP34kF_ahTkFYJ_pzwSp5IKg6kR2JLBBbIoP9oxdLm4kHffQFR9dj2ZPTDoGYgslq3KyXxwjkZACSNkHWfPbSw8zQbqkrMEPKHmOSlHXH--ArLSIOqIlp1IQy46zEpuGgu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6524" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6523">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pwbvvx81aHTIw6ljkOHZuR6XdBWxRCsONTgRRTIoQTfpotpz_q6YVGkaEyXEkKMBvQhIBoCSa7w324a19U5YPgb8gPgjnsT9jhi7YokNzAO7RpRp_nv2L_fmOlwAaGXd7PyBV6e-jHthVDaiXUqcNlxPpHVmNpmOrAjaKnMIUy4fXFJrTQ_kL8k8hrD1jetXv4jC7XjXzwQ5e2W15vugBjY_G2dxkCppvtIU3qy7vBuc4wCQ2tAENixb_x-COIkZAr8cLPrbs2Ag9hThtDIs9T1ogE4gNElDqspehPuAD6NR4shBiNACGaPgMYD0Vmh3F-sqwh4cUlLMWjsBTAwhuA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=ZxrT51mV4AFmnUY3LDYXpmoavgcRHY4OmFpRbpw5KVV4iHvXFb8M1Ox-CQ4OJa9x5fQ5IxaHXr9L1TiGSOCExknEKwmcZ0oj2vV7kONuJidV3O7nqr2iXtY1lOpUjR2OiAgY_vpuR106NpW32qr-GH4usFkDLThDIc6OWT7ZWJpwEOqUYloazAzeQg428ghO8nT1rG9ziTJDqKxaUqZHxJTdw3dkChTKv7xP-S_T6TGLG5zZipZQJVKs2hIF1vPsyODlOWHdXXk3G-31a9sTcpuNxvttd3qSJM8_DGtovLvuLrf37VNhHrSfpkPS9Wa4bSfp_nH4LRKyqZ5ELGbK2Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=ZxrT51mV4AFmnUY3LDYXpmoavgcRHY4OmFpRbpw5KVV4iHvXFb8M1Ox-CQ4OJa9x5fQ5IxaHXr9L1TiGSOCExknEKwmcZ0oj2vV7kONuJidV3O7nqr2iXtY1lOpUjR2OiAgY_vpuR106NpW32qr-GH4usFkDLThDIc6OWT7ZWJpwEOqUYloazAzeQg428ghO8nT1rG9ziTJDqKxaUqZHxJTdw3dkChTKv7xP-S_T6TGLG5zZipZQJVKs2hIF1vPsyODlOWHdXXk3G-31a9sTcpuNxvttd3qSJM8_DGtovLvuLrf37VNhHrSfpkPS9Wa4bSfp_nH4LRKyqZ5ELGbK2Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOa-EOaj1SlTyYLiqyVUwmdn-nhgp__qHFMVSsEJoZPDbIZs6pHWMaeOezzggFqVU9akvULO0ZxywCpSsOhgwCb4y1EXadawoXkXmdlut9Y0h1FGZRfis132e7nZfqSAAlOK4CedQZx8ouYlz8L7yvAQ5pV0bD-2p15LsfFZiDLhY4yLbnDd9ZzhvczqQyvNigFHULdU7Yz9okNUaokAtwWN0eJeRXm3QkL6pdOSBi8aKNbpuRMj53Y4DeGLB6qhiIMwPTIXfs1E1cMuO63zvaimOFVglBXnuM7SkKmqOhwritIH9kbmhVkJR7NyEG9ClqpgpQYhPzXtnOiJF34xKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9t0t53r2rPFfbsJVsBsSbqbWDR70G3XvPaZ4yDa4FV2fOZvUlulMuFlbDspFmNBIxIpFpYfY5s8g2KjTN6OHf1eStKKOTUmrgIfVjMUI6OVEak6CmFyjXQMh-6Z3rq8jLMhgc5NFkEmbP4-VJjZOOR1eh0EtEMJCSE4PPv_LVmHUl99ey4ttTArg8iEj576G6fwdOcSzxpbUQaaPG1Z6Zcwbub4RmC7LbqXMh2maewn7FTiMnMmOkblrSETBwXWffM3J8Oh23dakdhrPyHbJw_TFXIhvQePg497JWtf0_tqa5j0F3iKjm5wFrb2dNZmXrPRFan5Dr62A_jdeBpttw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcimpV-_i6w_Zv9NXJnGbrJQlab5OyUXER58-dm_IcJOswmcqpbPEl6d13dwSBE5jtQVG6C94nYk4o7jXaCZipt2HHSmkoMZn7aepn1ClKxAOVyyl2WfapbMbKKlCtYtipQ7UoFI2AjD1PAorENa1WAd6hhPDF5BOVjQdvallRAfI-2wxYUjgSPhUsvu3TUXO_hPvkSQuNQUFbRxJt-ik0esI1LCBlHFBRW2a5fb74GKha5T6hI-eeR4ALqTF5A58vmD-Sy212JF3A8_vmOl4hbHTbKRymQ5vdPov81xTKt6VgyJ8X0moqanzuUNMGVczqWRGaUxkJRWHalC47fV-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ju1x6AIjPoPvJtcToMujPMQNoz00iRexqaP338TfQ1L2JY25el0mOR146SsgX-cMcVH7UWo_EndScWwzqVouW7NgnqQRUkt6XzJAlV-njDGlv0oYQsUCjKa1V9ByzSsQeZyjVOulWFEBZnE7r2T28jYw5JmzGaxf5O3dmcYZc0oxloxdx3SB-_OIslxXJAtD1duasD1yq4EMQabO6gkPkQmydx2knnect64AZbzsTjMSEyP93x6epQc1MRr9L5Y0sUuecizohG1_2w1t3zV7bdDdAvkGOWasjHAxUxB8QOieOP3nbfuHSAZP4SccvsJ6Gpac_5TwyVYQudPtrNgVxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5gdouI4r0-ivK282G-HDHrsGaLfIeukJx2RWFMwycCkVjjkUSpSIej7hjnhV0M_r5csDhWJwbTOYdn_uE2jZlFjnp5OuWvGPNxW4oFmM-BCppOq_2ZKSzd3e-_zrlN244aIRoQ06vXIK75YFiaQt37lFDWvHhVPo4H-RUxDxWjiAsU-cqKdCP60laBbjzZO88RHnJyH-FNXOsI41o7q_OflmHvJr5MYXpD9lNRx4uiTPflaWy_SpQKPbDPCg059t6-_3-Q-T-GdOKcnb4tmHffz8-z81MMdficw4wQPDfXngEFVLyWnYOrBK4_RVcOVqeEr8fr5MMpgerQIjsn-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKApDB-Qk4oi7SLRmXeDRCOTWZoW91aeQw_r8t1xHyQCKzpLCrrKniNZwwG5RMDVeO5iJcBKsWRNRYvhsun_S9TLiuWWitfBvt1lQjzyCaK2VN3xVkilAdZvtyR6-VmIzhgSJdKSjtlbVxOYjTC4ID4UwtJUI6PZFeujqI6sJflA_2VAGybMdgn9BvrGtcGEW3zvH3zZzcbKb7-mE0w3tyHDH4NDr27jliWJwNlo80mO3wGpMEajE509qduVCBSM-u9zGnpf_xouJENFTRsYbT8SiWuQqty2OnQre0DIXwf6v64QnQcVW8Av35g89W_MVLPmZgHt_-A4yldfAVuk5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cwidzwP9zGV_VHpRcq_7obIystw0BqBHdmi2HjThwfs9v1iA3HgA2cpLxBVy0xpWKElSP3t22aOWjBnKaNYmgqF_2rpKvg-Elnh6ei1TVFRiGsDN1Dz7mX12A1ZqarrGP3Itj5SpQ6fYcBJG6hqu1tZDN1f2CBnRPvMB3JzEawSkkUjjkX-V8HuEfQeHdRVZnXINXVz4YudEVDODA-dcz5e7dgrf7dakdmg9ImfgHCX7AKuuzPVrxdalyxcr5H03iNsY-3XCbmi1iQ9srz56TYrSDZ2fG9ANxLJzSZQsGW4KjC9Iew0e9kQmjNf1kyJeREc0WEqeniz6uZfO-pwl_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=h4SK1rZMb6VcjHjDABXoJselkoE0JLXajApl-LWLMzlTX59xVaNIYkKr9Xuec5q54xDUA1UXwcKq1OlnFL-MQA--J8ZwQ51qWJVyg1oUAYI1wvPnpc0SjNEJu8c9jXdmArg6xCQIEGWwUpU4pKLtpRtdqdLVakAvO1gtE_rGTIaIlrMBIJjN8DC72XlhVcMJqQzQVKRHW_2C0i_WvgBq9FzFK8CWi_Bxv0BV-CsAqcZpvO-HEiHYMrrtJ8tZd5dK0htmTwxbTBaIMuz3KcgY4ejP9E0sxa3IRKs94KEhNofBF0X1ks2_Pd7ULy8slOG9BsWxqC1Ysg-AqM4CKij7QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=h4SK1rZMb6VcjHjDABXoJselkoE0JLXajApl-LWLMzlTX59xVaNIYkKr9Xuec5q54xDUA1UXwcKq1OlnFL-MQA--J8ZwQ51qWJVyg1oUAYI1wvPnpc0SjNEJu8c9jXdmArg6xCQIEGWwUpU4pKLtpRtdqdLVakAvO1gtE_rGTIaIlrMBIJjN8DC72XlhVcMJqQzQVKRHW_2C0i_WvgBq9FzFK8CWi_Bxv0BV-CsAqcZpvO-HEiHYMrrtJ8tZd5dK0htmTwxbTBaIMuz3KcgY4ejP9E0sxa3IRKs94KEhNofBF0X1ks2_Pd7ULy8slOG9BsWxqC1Ysg-AqM4CKij7QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNG8-vd9caBhYRgTspnKDY8bDyaprzYizS1uuIaiePaIO08lvHWbzMrxCjERzuFce5hNxToLG7oHZo8inm7DsQlbDiMamKxnhEHHWwu5O6e17tsK98niBR141tg89qNgq6XZEstodO7AR-KJdEfaMnjZY3lBV7knvsG4io9W0_WydFWuV23MVvPcFdYmqKqrVqyK5DlWkf_3ZCD5gHOfSQyjJx6VXxC7Mjz_sazh2C_6fSm1JFgqAHywBZQ0O7kMGCXlF57ZR3O4EHWoDzZ1dRMzj37LlD3wQSHtrRJqmHaZTrisbhbauuOrRBbnbV4PeEw6nb_7zP96b2TMDIn3Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXJdHqgsQaGGXbaxBK-xwChkaPciCrI6vOnFufH3DzQOIvGu0LE0EJoEUBrIF4R0cRG9FNaBqVpWLv7JaXbtVLPB8oO-Ap11bbgp0HUd_D1p2drUHjF2AJoz7_IRvL9s16YtTLjkAxJGzgF4xnpfEyfG6r7y2qIfMMxVXJu3CbisQXLmEAWwvoxNmKIpRvTdg5QP5SCt_i6SLwiu6w9J_PEE2PKKPZGOjpQu0A0SU8xKKQX0A_E1bmYIurB5SBGP9fJoGwkOATlWOgfm3g1cZnNurJgC4h_A45CQxkw4LJgI6MLUAudLUe0-igJqheqeIhzm1tmhOQPP9DuQJugr-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=LVSMeS31G7yR-_yxuqT0jz_WMb6sRN0MBNc9KCACHKoBonsaFO0wqikghcj_MXIDvG29fP5wgMODVDLfCfRoFTrlyUGXtCwN1wqrN8qDg2t_e8W1gmB7UZf3PfNBUIrsD21gIm1R45_1sR1Vp-wDK2eH2HH2B-GdCdE4DWrY7qTl-JW26W4hqzPv7PW1-s22FOKVKt2jHdwyHcNxK-LvXT7Gafwe4jOHc_dhieTw12i_tceGOopv6MfF804jhyJbmKYyrOXg1YzldvQHJqkCZEGXQPWHmAxpDmRZdhn34x0T0M40ibHjKsITi51A1pUyhs3tW0NIZflV-kqH1bNV5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=LVSMeS31G7yR-_yxuqT0jz_WMb6sRN0MBNc9KCACHKoBonsaFO0wqikghcj_MXIDvG29fP5wgMODVDLfCfRoFTrlyUGXtCwN1wqrN8qDg2t_e8W1gmB7UZf3PfNBUIrsD21gIm1R45_1sR1Vp-wDK2eH2HH2B-GdCdE4DWrY7qTl-JW26W4hqzPv7PW1-s22FOKVKt2jHdwyHcNxK-LvXT7Gafwe4jOHc_dhieTw12i_tceGOopv6MfF804jhyJbmKYyrOXg1YzldvQHJqkCZEGXQPWHmAxpDmRZdhn34x0T0M40ibHjKsITi51A1pUyhs3tW0NIZflV-kqH1bNV5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ha-NMWbBWMNgqDDANqiO8TPK9HBu-Q_6U2igg4IMdN8ek8cFjP2WIW5i_v82M8Gw0z8vlkb-8mVB6mYp_ua-ANLlP9Q6aH7d7tje5u3YmVooTQnOqC6WUvwabE9dL06YCyBFtRER3M5LKIEH0ouzOigojcVZ5T4X6DwaAzNsLuhD3PMEeI64dBMVkLPcO7mKEP3eiTz-GgnltDl891XjitNdwJvJ27r5O-5ywgdqcoNwxpuLW9pa8UJhz_RF3zwJRMcXorxBCtzAKH3-rqznYo8e2XCY7E6Ax4-xOxcP7yBXasdA01KCb9746vq9ARDr51XneHnD12pmNGFbS856bQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABHhJ_1v0ndZufTcbNHBjelZ-FQ_q3XMidX_Se_Ehy8qoL9uGG9kRsYP58IUFWE8ejMWRz1g95PZVuV0S2txHhiSf0WYBMJrSBk5v7He8m1izVteEbz_spgEHITZpjW18i3juURE9g4sve6zdg01Wu3YY8IvUplF3_i0Jesldat-WIoUoFlFKAAsumhLsoyA4vhJXSYXKWYU4i_vIqCHJ1ygAfPoKbNtnQqsmRzcL7Er2d5GRhTtMRulFOvIGdCjv0ESAMFf24yhRK617FAh1tss4RyiGl5wz3Ec3acNfCJinD26D5NVjnSpcFJYr-I9qXMxyl26c7Da5JZ_Y2EC0g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=SSsvl3zMdacdX9CopRZppyk9mTIheHJSCz8pYXnHw25SGX7ZmtwVQxZcBovaf4duvJQbMvaeI592ONAc9KntzO12oEz_9PJwDfIJy5GDAS-_OOi1Jlczy_4zIvY90ao_O0XtEBR0J1eIROqooX6KME3lQwv4oEOpzH5WPdjbD5b6IyBbnvAtRldODdVznHamkX5-cmDI7qB0ZwB6uqg-JfrhBaNTZGyA6OEEIj_RKYK7XZYff4nP7-FiEB5TlNr7C4o8jW1hxvAgWq0HFsmldRgDEI3K2gFvlCrS3Xm9OkuGp6EBKmKXUaKMOhXOSWl_ob7EJ8v7DSZML9d8DEN8zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=SSsvl3zMdacdX9CopRZppyk9mTIheHJSCz8pYXnHw25SGX7ZmtwVQxZcBovaf4duvJQbMvaeI592ONAc9KntzO12oEz_9PJwDfIJy5GDAS-_OOi1Jlczy_4zIvY90ao_O0XtEBR0J1eIROqooX6KME3lQwv4oEOpzH5WPdjbD5b6IyBbnvAtRldODdVznHamkX5-cmDI7qB0ZwB6uqg-JfrhBaNTZGyA6OEEIj_RKYK7XZYff4nP7-FiEB5TlNr7C4o8jW1hxvAgWq0HFsmldRgDEI3K2gFvlCrS3Xm9OkuGp6EBKmKXUaKMOhXOSWl_ob7EJ8v7DSZML9d8DEN8zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=U0HjtptodMjhrJb3MuEgmo9rbzNLP2LMH-IAsudsaFw1J_kFtcPuN7d1XvdUB5Y4rwAwdlr13GCrdLZsouRwSRUSuymRfZokgJ_oPSVoQ0T536YM0DSru8nS7xFn-pnGidZ2pT_UZXGwmHFGv_H_qV9eqQ0AWlkuGZo1Ennyp6fqygwEAHcnVYcitGfd4xeNGgwcbYv-NsFXznX6K44sWsJaM9c1vjsgYdlxlaVu0zKr8m4gokn9Ba3OuTIGEY-pTUn5hG_FwBvncpkRrB4XX5tDZyaP2Z1dx_I6qNcOGCzFzMNe7vKURfbI3_cDa1tSBB5tVpPkEY7siHYvXT6yXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=U0HjtptodMjhrJb3MuEgmo9rbzNLP2LMH-IAsudsaFw1J_kFtcPuN7d1XvdUB5Y4rwAwdlr13GCrdLZsouRwSRUSuymRfZokgJ_oPSVoQ0T536YM0DSru8nS7xFn-pnGidZ2pT_UZXGwmHFGv_H_qV9eqQ0AWlkuGZo1Ennyp6fqygwEAHcnVYcitGfd4xeNGgwcbYv-NsFXznX6K44sWsJaM9c1vjsgYdlxlaVu0zKr8m4gokn9Ba3OuTIGEY-pTUn5hG_FwBvncpkRrB4XX5tDZyaP2Z1dx_I6qNcOGCzFzMNe7vKURfbI3_cDa1tSBB5tVpPkEY7siHYvXT6yXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlqmFK09p4fZUaZ0qzlaGAmH3NSWqBnSSyr3kBZp5s8V-rrhzA5WLKlDjStVy0GuGuX7Tzqc_cjCbhbnlah2XJ0G20kVLFOaGwJ7LpKEFRBC0zkY9hzcw8JzJ3dV48biOdiapqbL6_gJDdWT8np_4W7fv7_bLjsC6tV4RvUMyw3d9d9ofns-3PmuQ_NeAAeYbUvfqyn81FWJp6eym3Nw4okgo2xNpq6k8HIS_grwmO-OJL-j4URmfQ_T-cHnXN47iK4Ot8s0a2Du5BJNCn3CyPDwxtpGsIBsyLmA6_jyWZfor1jdjalLnWZFngZoplX_LqbzVbxQJVvY27yg7-p_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSeOAA9_i9P8sT2Z3VkSZqDu0BeadDSTJqQsjdobJhO1dQf551-QpGx10x1ALeA5KRZXvVHl3ILVvXySr8e5cY9bCOstCiU_A7V6HJfB0-oEO97bG6aBa3rL8yobXHziNu_j9IWzlBCnzRqgatgRdOS23OBhGl8mhYFz6gxiEdjknNYGC5A0NrlNRdgEPNn_vaCQguGl9H7Lw0UUvyFh3TBNG-nle1qwVt6P9U4H8Nruiv5Qe7Q_fE_w2oERw0G7IuUGail4ig1rMsY7nvTbhe-C54_-RxWFLzZ6LjfHLsQffMJfCdFVmQNQsdYBgnSgnbZ95i8hUVRWfC0Wj263nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggSMJMmiuUz6ZZBtZCKx6ipxScwpIJ2poWPXsUu-6F_jUp8X_338P0VhTha8OcYjjQAahTIEqY58nANQfv9DWnlYM5llEKJd0tN77jKvj6UAJQBiRnC820ojSy1Ljk2FU3fb2Gef46ohiKnHLKu8siJ0d8Z_akFYKYREExQIlMobYiBHWTdHmpH6cszUmoyax6qEXjqkrzK6uyRHJIp9n3z7UkcK3vOXvt5q-pQLkTZRHWRPAYiDKpwIMKMNxR7LVFeoj9buaCnVNDyezUdkg3nK7etE22uyDsoR_bHZbbq80OlV6qkgsUdBnjYi_ArWXkbCvbCSSdLW1Izkr97yHQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=Ljz3ZogJs41GtQi9EVpxGpAu_2LBDO6HEhCR2PSbk7qqGb1awwVC8BSKLfUU0wCmKFD3Sf5ihCAOc4xOOPzxjKqgPziCL7GdSUy8M4O7CC5_fFZEucNPmhGZRYg8Xt-p__t8kQrwhC80EaEg_Pwd382zdF52IegYz3yXWjOJNdwqK7BDGIfMOP3eQX7E3K-qlRXQmqQt9QFxHyTRKdqSpqrAP8sSItOQ-xItA9dQyvUpKTG2VMNdquEPR_3Z9XnjsqjF8XTpfYiC_g3mbDpHk6MDY_D1WqahIGEGw9gvFi8Oz1tGHDsnCcsDLcHAI5U6lekkwF7jtJk3BLCjF6Q0kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=Ljz3ZogJs41GtQi9EVpxGpAu_2LBDO6HEhCR2PSbk7qqGb1awwVC8BSKLfUU0wCmKFD3Sf5ihCAOc4xOOPzxjKqgPziCL7GdSUy8M4O7CC5_fFZEucNPmhGZRYg8Xt-p__t8kQrwhC80EaEg_Pwd382zdF52IegYz3yXWjOJNdwqK7BDGIfMOP3eQX7E3K-qlRXQmqQt9QFxHyTRKdqSpqrAP8sSItOQ-xItA9dQyvUpKTG2VMNdquEPR_3Z9XnjsqjF8XTpfYiC_g3mbDpHk6MDY_D1WqahIGEGw9gvFi8Oz1tGHDsnCcsDLcHAI5U6lekkwF7jtJk3BLCjF6Q0kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=IzbB9EfNKroxTiRtvoCZNgDgAvPzAgpu4IaGI3sMTopMNhOk7p0YvTi4KyI28I7rYDdI2EgK-KCqYMHROYf97GiB9tnb2jqZQ80pGkv80RN4GaWOaXumvbPvGKhU5QFTM0EMXwz5m3Epw4cC5cq17YrmCWZJmOYYbekZFYZFhIDesldv6sqMoYBukU2leWIX0xk1rPzUIOKG8bKp-FPFodepjLUpQts-IMktg7QIypMVMxrF8WkI7NoX5eBzq-qxdspPt_aW4LRse7YqkVRYpZu_3tZJ-Ta0rtC6L3fwGd0ROH2QjwGqCjuihEUOl14rnxil-js0mBl0aDoRC7na7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=IzbB9EfNKroxTiRtvoCZNgDgAvPzAgpu4IaGI3sMTopMNhOk7p0YvTi4KyI28I7rYDdI2EgK-KCqYMHROYf97GiB9tnb2jqZQ80pGkv80RN4GaWOaXumvbPvGKhU5QFTM0EMXwz5m3Epw4cC5cq17YrmCWZJmOYYbekZFYZFhIDesldv6sqMoYBukU2leWIX0xk1rPzUIOKG8bKp-FPFodepjLUpQts-IMktg7QIypMVMxrF8WkI7NoX5eBzq-qxdspPt_aW4LRse7YqkVRYpZu_3tZJ-Ta0rtC6L3fwGd0ROH2QjwGqCjuihEUOl14rnxil-js0mBl0aDoRC7na7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=WSWrlBKis1ffVhoEaqBzXbvrk9CqKdcW41bzwWjvrE-U9FeNF6RNMZkmsQ4mvPaVNE0akcgbUYYu-VmcALoLqDcx_MOab1NzgxYN8D2Ak7jAImpcpeGzqdtN8Fib5d1KpR_oZEulsNZu8Ek4fHCq9iuRCYhYWoZHvFUJO8yoCAKDj8oAaib7dsICU0XDiVWwI_KfQBQlLz2wRH174TrvyzlKQ6Ey9N38lZsk4QmWq-7zmtNtipMx6U9dV82oY011ShQHrQBYkjm9pBkCIWjC7dORAHG13fDkkJ1NWonP4heDWPgZFk5kIQXzgDzLUp1TryHmA_cTHnTF90WzR_foTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=WSWrlBKis1ffVhoEaqBzXbvrk9CqKdcW41bzwWjvrE-U9FeNF6RNMZkmsQ4mvPaVNE0akcgbUYYu-VmcALoLqDcx_MOab1NzgxYN8D2Ak7jAImpcpeGzqdtN8Fib5d1KpR_oZEulsNZu8Ek4fHCq9iuRCYhYWoZHvFUJO8yoCAKDj8oAaib7dsICU0XDiVWwI_KfQBQlLz2wRH174TrvyzlKQ6Ey9N38lZsk4QmWq-7zmtNtipMx6U9dV82oY011ShQHrQBYkjm9pBkCIWjC7dORAHG13fDkkJ1NWonP4heDWPgZFk5kIQXzgDzLUp1TryHmA_cTHnTF90WzR_foTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=j8ljf9teM_3A3fELI4I0N9JR86DK25vCsUivCixoaWZ4m8htgstpemyFowUPqBWvkCNAqB2c4xnZGAZlA1RO5b5xR0SxKVl723qK4q7yT60UDsIjO7pV2lYboBHT0yexgR06vygCYxaGMArBf4wrp8T-qXD_7ADKf8SrG1rNdZtG-Cz3jtjIGD_MhaSDpe4prNeNWLxRCN8WOASy7iY9u1T0R2JaNNRLEs2JgudITjRLV7w9jOmW08RHyywKl92ynahVONpyDTG9KEdOFqM1gZW9HB8NgbfmkDhps_FxjGamhqFAk-0A5J3aIeAzLaKXgQhcJ9c-g9sekh1on9gesg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ad02e26e.mp4?token=j8ljf9teM_3A3fELI4I0N9JR86DK25vCsUivCixoaWZ4m8htgstpemyFowUPqBWvkCNAqB2c4xnZGAZlA1RO5b5xR0SxKVl723qK4q7yT60UDsIjO7pV2lYboBHT0yexgR06vygCYxaGMArBf4wrp8T-qXD_7ADKf8SrG1rNdZtG-Cz3jtjIGD_MhaSDpe4prNeNWLxRCN8WOASy7iY9u1T0R2JaNNRLEs2JgudITjRLV7w9jOmW08RHyywKl92ynahVONpyDTG9KEdOFqM1gZW9HB8NgbfmkDhps_FxjGamhqFAk-0A5J3aIeAzLaKXgQhcJ9c-g9sekh1on9gesg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال گرم نیروهای نظامی مراکشی، از مراکشی‌هایی که از خاک اسپانیا (سئوتا) بیرون انداخته شدن :)</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6491" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6490">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gu1FbeCv1hWvXsbE5U47fmw9ixktafkPCNFZzMWvaKKngTOH-alIhww3QMbGIim4kA_v__SMbsJiaiaFVF-toKyvJhAJFX2onjs8k9kNvExNTJRODOemaCNNBm3--VAA-V56dqWw2VkgA_hHFcY9Y8_PPdlWBOS9a-92cmscuvn1-6KcECSX3ZzXWL98aglJcIHGfz-9kPmziz-jDKn0Q8Fdbk5iyU25JRYMG6P5BYk7Lj7DKLMudJkPuSfAubP56lmDg4ZELyJuTDmncHMu8YCC0HlJ9Jr6a7jh9_lG8m0o2e9TkdHTr_dU58EoFhT42xiTx-L7Oz6vg2Wblca3-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXqg_5dSxkWvX-nzCmVweI9XO90JpSS11DNRy9omvNw_qJDSVZFYH1YSC35w0iTASgz5UxDVOmDXYPnSYD5jcW0Wdjg8PMMxL-rpVdP-ACP-oYd8OKco4xHeBx-h8II1sHwdXqWnLTDjoaqWI_5S-xlhm9jrUnw_tOuGcJ9jXh6Behlr9XmDZneQ1u97DcoPW74YvBQGalZFJq-nawY6SnA_I-Mgf2gUb8PXvmFbZ98T5xIrwCcwDaH2Rrmjd1yus35Wld7ny9ED0SOFppJhW5jVTXhoL_m2U_CUCWf4Vh5Dq4gW-uysWB3-dwgJg3F_doDGthxSp73WRLG1KoIeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qelEiQ0ljurJEdFvF_IQvjrdId4wPIJBrIbILTKU9APPPmqeGzn_UnrEr9TL1SPdKyO_FpX3_9SKxoy1UIQFDr4hqE5Moi6PWoQCBtoH_thC-UKKLutf1WaxDmUqpwHaiFHsRx0N1ZL1LmoLm60Nh99cVWKFQnALAxhdn5j3k2LzJ-iG2aK1weTMjqSzY5c8Ck_H9R7pW8juX9e1UHaOvhBfGqrM9bW1WP5O1eHvqiuFKTf3ES7KFdQKII6SNMsAAm05bSVK8aMxNIy6issen0PT948V9gPmXXWpa7HEcO6Av0wc8pQxmwA5cWMejIhaN-cX6kOOQTt0BqtczwoNmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/grXrphux8_0dzrD2YQVih3u3_yHnBogxS_uk4PrcErkZVJSLs-IomRFYACu9LFFMNY-58RTHJClp4UFCdc0MVIyirh8-IwTQFw4rBWBjptfPnVnThSdP_Lu-ynb4UuYg8zD7fvMVOG_TMYyE00Dz9EwsSE2nJRiHOdUPQlbHYm_fBBkAJ3ZzygFBzPpi5zj8gjm6Gysf46WRVLaQ7PJwUx3w-FVQ2GYepLbkUCIDmHfzB6aZ_QSdinyHf2dEJjBBAu2j1naxP9uSMZ2fos2MjvChc6wN1QTo2iVG88Jolc3XU-dWTpEhLBRoId8t5uFa3X4JLgsl62yc5m92YZCk_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyH1bUM-X1jBNEl7JXbxcqeH9b_bYVKdvxsjWEOKPxAd34VMirU6mm0bcueHBfUjQCJ98megt4QpTbGNosqRfe2iniJDYPpZ60L0XD3AyOI-5rD6vPtDk5Xe-hKDy6UHIBMFgVnizE6zAT9Z-CvmzouSzgK64lurMaZfsN-Kjqdp6AvPhnvk9vCM-X-qaWfmNBwjadTtFBFY_c4FPi_RSyETUcLVFc6jei0ZPT1rL6l8m_iQ83svwS73KoPt4WOhJFdG4_8Ybi747ptE3VUL0HOmfZ9tagiqY1r1nDo-7u7-2X2i8DvcBBkicKiuM5zVegQYoYcf6cSIDJz5rUlUvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr2949FD5kGKk8H0Ozvnyh3c0q-kXlKVpusrkoW_-Q0tpI58xyK2Td0Gsc7qsNW6SiuDyBll0rTQFFzsFZtyj9ERTf98AB6GD71-1aIuhwrY_xNRK23EcnfAFVK9RLEDvITzY4P8ps06iJmeIJrq1RJCV0TC824kHW36DirxJGJhUK0mJFS9HUcBmGPCWZs6IHy5bxsEtaPuEbOFJMyhO-v6vK4112jFaGpf1J6E0Pcf1L7netdW_c_IsrUqApur62U4uzaL39SeGdO2v5AZjM-_gJviHCIRPeiTFRTwdxc_iBbZzguDKBPcBqMTph0egsIeLqjcNWow7eTrhE-3zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iITK-goKgZY9P7r2mYcOwLvFO3Ui-PQg6QcniETq3tmZSWJ6c5YICFAag8rBMMePZ2kphHj6skU9FtVKWLsO6ButJzxb_K80HAAS8i735TPAYqCtQBucC3thX5tm6Mq4PJdEN-RdvuqskVZlGTzJ5-mOLxEb4P4m7lT7NAVYhrS509MIXcGz8q-175HtBvruEgh4Xb0MB_L7KhSuWjAyFTdFAI-h7XXh_o0dhvR0UbIuoQ2-P1Hfz4E5BbxjicDnGxxXTVy9xH2wr36MJ7gThhdAeOgKr0gjygz7VnwiyU65dXFOz2TqEZ9FjcG1PWD7Z9IXEDKKnftkyjXoDtSUYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpcV7HJBPTTG92Q6f5LSlkhLKBESulxVFb9hIKchLcGTP8yru9b_wvKoQPJcJkVECmyRo7_7NLVjQ-SQfrz6IwCpXNpq8atBYb8PFLuxdOHdXyykz70AevF-u_Gsc92Wbtf8HIDH7fy68mXmXU3-klsDlsaNxvzY0QY_uDWO_bhtkr0XT-2cYiBGLDZwXmtFzldH3c4Xgn55yakkpo4UQVtKryfURv_fG2xeFOqeCugoDnoOCxq0JfV4UEyHiO1AAmHircQab8eDC--p5nYMfOHmp7T6_UPAC8LW1l-FP7PzjGOCL9yKEu90RrtIAUrxTS3hahYF7e0HAN60d4VVGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LS9Sej3fxomZAvKSxGsDGQ0dEpLtLJIfpqjR0oEUE8PKIaFIynmMpU0cfGxmqx0JfVtqTx_CNiKi0hvGCn9RwNAIVPOkvRtaJgf4ru7p0brwAzcko8k-0QJLHY6qns7nUy43kCWP7jvzJMmHxzJsCkFU7lpRZoJ2aiU_Gu40xdqGNDDsI7psSptukEl4pE0iK-PCpJaZSQM79J70XRynJeWzOePsRboHUubuLd_BcjrY1eaLvCdLX2ZZTL6ehfdhhlmQQz3IwAomnpaF1J92eXaL_a6sLITI4LyGTxv0C_c3_aPt17TRjjQ5dvLvbz3saAszZMceTFsQ-XW5EyKgVg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6481" target="_blank">📅 15:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6480">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHDOYmVA1exirM7HBA2KoM2Gjj2X_Xc8ly4ZCQ9yLMmfmSFGbCZK8zWiiy7fW2wF5kX-TBsaBwvLdfFeJjldMBlCM0GmLz3NHf6M8jOqzIBk3HdMnuPke_cFkiWrWlPF-0HigxgTAj-HXCabtVS3TzFlh9aeqLMHO33bxKnTAxfZLVFi_4FY9vgJENQ2WbtegSwV05qDSpRv4AQ7SAheLVQ8OAowf6sc2uj5v9xYCnSELBlHFooXdf8lwX4W4gUKR83IkGZg2aXWBWXbShtEmByLKlrxN_VOWJWBVs3fpXQOeA-k73m7MdJ8hGj76IDHsDe3hs0ytAsUF4DWQnmwJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXpC21JDBcqsKuum47Exb6C4_x84be_5UPOWiewIShUXaY2KgD_9Nyk26oamTW2mkRBZq5D2FLhYhNB1gMl-rq7hMn1mgNOKtQbhPH8EhCplzJHXOpI9VhA5pj6TC3Jl7pV6TGU2TlJfQ7GEf9VbwgKsO57zc2-Gz0HUUtBaSAGDiYt0TID-6yJLEHkPmAKqg9JMK8gWy1PK1txivjgBDEOZDg00r5v2mkKz6Oqqxl0IdigB3rpejm-EqHQjgW8ozuKZpgOok_kEt_W2vcvK5uRZGucYaMXWTInaSuB_VRlEdtYaVbaZ0G2I7fjcu7ZgGFER7vtqQzl2Gdz0QeOzww.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ae-nJxgK_bm1-VTsTNzMxbg0vhLh5xsFO7Tmn5iJbw_knjIegt3Wx1BtOx-p5nG4CT-_pFuxcbT0wKlGGDCIAj2qpLOAGcr8jdY6jFmuhXrkjyQB9QLjmkCSgTuBThOdn85WDfAS2U0KCM--y5hhdMlA5wEyHLCNZ8loKZ-1dRJdWKKzibx37HjpVLXCjxp7Aa4bnLpRmYtR1PA-HJbAGxI-hBgYWMUCclbqbMGvqBOqe8HRrPI2IqeecIildDgPPTojinX8FVefEKFqcBodbrekyliDLJgDWFlUID5g-4n0jdSIJIy99mKHgdaZNS9iYIgkaJHsUOzoM5RuMnVp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGGB0bmLuAFL0Vxh2COA-mUmYjNZrIxhmHB3uRjhZmAKq1C2CTiJRwHwX6k63VdxSP47kF_RIHndbAKVtpDSVP-LtdeS6DgyMbQ9AOKveBBlz2_Qnc-YcYWfGMqcSENgabsQw994HHqBi7geNbFgAAssmGMiMsxtZeHM4_z2T9zqLfz7dopkUloSKQ8dId3Z0EEWtuZ-OgG-WgE4ZGIG8ljV-sSLK8-QMJFNUTJURFTZKiQWpRV3qMKwVHmYFNNqM6drQ9Ybkl5JuDvV56rbAylGFFpgXoS82aqNRZ9y3oluWTAP5FFm-ybux0roeIiBRNDF5bJuhzXCqHYrViDO2g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tioD0XjAZW42lpQST0JfgWPeXHF-oK1QKjRh2Hv1HddHipaOIPxEXdX1dUqhxhQuZH_dncP5AfFofZAvvdYIJFIi5qjFEWuhMIAqZAAuUgWbVdz-MJTtTYNW4hJ7szcjtY4EhfyUyFTWLoUStU9iaXc9IU46RVfxOL6wzC-Ep34DQUdPfKPoGhFrfZbws0BhAs9z5HEHkvfnGxI2sDxENaLPi8k3rph3OxQVNkhUf8lA5wI8DSGYSMfLqxIllmKJjNirxSNmu03B-gdwWGCOdgPspncnR2h1ijg4IMGdbk74Olt683eoq4fDB_eL8xfzki28CuN62OShgXjRadTWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=OrdQEIxdo9lkSSoLn61XNfLuEVNq2VN3i9Yw6tyAOGrr1w6BOyq3zCUdaYI0a0BppXY306wbpSG8-z_wgVeot5967H62FNvD4vmeuyHuQNdVYB4ip4fQS8M5eERFjqjgmHBo3Bmmuq6t2Ce10EwBL1N24Kxvr6_v3PuAyFOuOreIPJwoStr2qd050QIhXDYYtin33V8smGrwOU8GEgWqidnkiPthUyDBoqw3b-caLiK-ZYUhK32WtHu0drpxQKiYQUuppWpd3osMQfKFOCVrQpJls7Wc8oJG0YD9z0H4V5IL4tsphU5UOvHLZJ2QJvA5NskN2unMxqqO0puy0R8nLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=OrdQEIxdo9lkSSoLn61XNfLuEVNq2VN3i9Yw6tyAOGrr1w6BOyq3zCUdaYI0a0BppXY306wbpSG8-z_wgVeot5967H62FNvD4vmeuyHuQNdVYB4ip4fQS8M5eERFjqjgmHBo3Bmmuq6t2Ce10EwBL1N24Kxvr6_v3PuAyFOuOreIPJwoStr2qd050QIhXDYYtin33V8smGrwOU8GEgWqidnkiPthUyDBoqw3b-caLiK-ZYUhK32WtHu0drpxQKiYQUuppWpd3osMQfKFOCVrQpJls7Wc8oJG0YD9z0H4V5IL4tsphU5UOvHLZJ2QJvA5NskN2unMxqqO0puy0R8nLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqQLrqNxATt-Cklc9BUZB22ROsw5LVl0s9eli1n5xzKiCk36NjxO77htfVcat2dfshFuROAcUVGPbxu7s5RQAeDBg04imPWRbw5ZttzdG2OJ7BWm4t5lfwn6V76V79pw39zrv1l_z0qVt3BbOlZ07O0bZIxYpztsk8IvYy8Tqlyj0lFQf5qKfjEL0Z4QUOKFoT-oGFoG3KqWUJupTaZTycOXNifrcFHA-OgwdQR8gR84ZH5wvqxmH1-kSkYxnbMrwawKL2TWDMSzlwC71WwmBdyfbSC4S-7gfPbKsH4a0GL17Nw2FCBBcrZupFSb6xnJfj0hXKgXgNDsCtzSMJ8UXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEJ4xdPzi_DdmnqwPprGj7z3g76hcARo9_4OmqmA7f78Hgr3djSExl4Xnb-v8HHJpeA1inB9oYiPD4uFeUNz-EFmQmrFIXYiKWw3S9zbUS7zpHTtjjKD-u1iPkfRiKcyJncT4GRf-smvEKGS36yQbRYgBzIc-5eT80K7YewtMroy46ULDmdgiPMRTeGC5wDQdh2OlhFo90cFjJoc9hWTkYLm6C3DC_aMc8IMD6dWohkfKUoTA-2qLpFgXGUkP7tlWylr527G2EHNkiP1rkm8t1D8q6TDWH1Mrr1wafKb6GuonUIpCOzylgQlogjzAYYwm8wKBeWOXXHW3xzom6mjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJr30bI-ttjP0nhJVkWx5pnG7rMpqJsXBv8L-8Y7wZ7zgW4tog7o60BljCphchyzPcz9mh6g7Xm3nZ6oOy_wuq9kmL6Rtcw7sSZmrOWkLy6Fa_X8kJJQAUsM6hx7hpIekYO2Hl_NpHzbgNCEDlJ1INpcIK3c_3rxWKzS7Sb3uEIifDGjRSqbWRexxYg6TL1ov1BH6smu2RmpRbXRp9iJkAWZz-N2E85bTUwjBa73JTdYSM38Z0TkHOHUdWbtb151nIa8jJxckHw30TbXPwgut_8MRgawaBXbu0ERv2CTDrhE-UhBAMgPlwD3fg95a4HI_4eLmvpWSmfC1vT0UqYt7g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwMAQTyLmZHLAYnKgi3qjCeno8aHUEfQNrOPZ2OCCU3guXBw_6a6shIGgEiJNcsTvMBAWSPbf7BLYaG7tHm4jYFxiaak5gh-qnRk3dJ8kNPyuIzGk7DHl49fDGOUnI_Vkokyn8QEEdrtLxgcz-H3WFClS19JFCdS2jPKHDrFOXe6RV_c06xecRs8drrhCc6PyWqgevMHkQ_EKX6_hP-QGKm3207aiqOVSICQ65Nxcb_-jQOpJObbgJJle3OUWhxJu1cPeq-c9lKQVPbR7NO_G4-K8kGPUfP_E1VvyF9Vl-R1WWwId_UMxyXBQUNHMURUPwK8TYxbWPEbRBIw6uPtJg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nigPWdICc5DHlYVDllnao9NLPknNVPti1ib0uHivpDdJExyq9PDBzzMzw43b8vDhCJZBKbiQR_Joqbxyi9xL2Wwzr3GiCw68X3NqzbnW_PqGL0z8JfU9F12tjd15OjwTG2t3DxaMfbVc7AWAuUxhKJcSfRX8YjEW5Cg9J0Lm174vTI_zdC0TxoYQlqNnvyhQCz7LFuemQy-p5ahVmZhWhmqvkcPD2N-F9cDCLQSaVimtU_9fGKvIJ6Gmhq5SDmqnHHh3FxASbdZ-ZgUvOm7Q_mT5ehiPfBzW3jwMpvE6Uj2_vbadr4jF_WICbVXBOJJXRmIMcBBlXWN9TLd9FXiAgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE-4djmS_mFwIf8ChnF54fYW4b1VtnX8J6uObLilnOmH7nWS95R11mBLJsRh43JmzM3K9jaC64diYyKvltHrnb7baEsyN80-n4UW3eSixW9ssf3qtzkYVIsRozYaGQ0xfleqiDFcxw0L8YHQomCbmTGSEaM_V02SkbiV2lb10q-CFFSIOdQd6W2G2zkTQTTu70FsKEA9fpGnVpiGorYgxSoxY_rXpEvab6Rz3vVW_N0CUGzKY4iKwxvfMDvYB7HAji-cIJdZ_5wMuMw8UJWy0DjkvC8id5taUDbqDkb6PXCJ6dQdYLT2Uiy6_NAxVCOnAoe9UizpPTLLxho5AZ3lQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Obc1R8oNzeioEsi9X2RiMVZld9IVVEpYBhqdmgw4tkxYtDW9NtyYcW87_YOuqATpkSqtgC_KCHHXgAApyDYMPm0v2SleLC5hAgEoTHWv1IqZ1jKC1LqDMWDGrjC1h-_xPfvub6rj0UXGyHH7P7X6vC5bbTFEDeAHmp9ISCMKZ6aSyjCWYT7-Zwa2GmpSXSUBF2Ad4axZOH31ZaDb0JRHLGglGJlK767suzdwuP1Sbsqrl6eD19dHssqX4135nU5BeRrfCHlHaZGYNhC4iVTE2WSGCX-kqsP9jr4LG_grKQlSjQou0l7PvgsoWQc2Moxs5lkNITGT_VVBaZ0MEnPhSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOcXDabuxz6xMq9_jX99ha8ceU-ymj5TMxL7VllUYRBglAytqRZ6xWHvh2HpDREMbGeDNXyWLqo-K4DY6Ye8WO93AvbBTtz0aV1wgnmvfYg2cMmSIri94gTsJ-AWmyBt1vz1JX2RtzfeB1nOK_CTHRUM3XJE3m8mx5zQr94O1Gc7AGv0oZyJDi1FCdz4-inFgsOy765i_lyQaJ0YBS0302PB-d2cszECvr51RRH0KCi1KHwjtiUIR_Yat3zgV5dbOqWktAoTIyCa1Jim9ZLTN8Q2aHevkM8oy1LB3Ck1XNl5RoxUQ0fo2wwv8ThY3DgZqyXW6qVRFIrqPEpgFvAG6Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=rONTSUa6H3jj9wqvyNu1G6tinss7JOBxLYBTvuPlDK47mqrwZ1ueKSEPuGJouNm4Tlkb4JZMgHX3vLO1XKWrf_KuGwkeoX88RMAgQaCvggS49gDRNFGsnWoAsCpUajpxqt4ttdCCMt8eKDAt518647TrwEE7jiasLsA-UWaEvQumVVI1EFtjQMU8PPOS3D2ASYla9QAYqctQ8HCwdAvJ_p5SgndoGaGeqJZ8Yi3kFurvRxex6m-_vdFiz3caG0pFNh2pJqZdedTTu_QeV4Q8JaJQp7Fapqtx7z4BzGSyY3PTop-AirY0pzItMSeOHAp6v6mIS_VeqwagdWR4rXHQBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=rONTSUa6H3jj9wqvyNu1G6tinss7JOBxLYBTvuPlDK47mqrwZ1ueKSEPuGJouNm4Tlkb4JZMgHX3vLO1XKWrf_KuGwkeoX88RMAgQaCvggS49gDRNFGsnWoAsCpUajpxqt4ttdCCMt8eKDAt518647TrwEE7jiasLsA-UWaEvQumVVI1EFtjQMU8PPOS3D2ASYla9QAYqctQ8HCwdAvJ_p5SgndoGaGeqJZ8Yi3kFurvRxex6m-_vdFiz3caG0pFNh2pJqZdedTTu_QeV4Q8JaJQp7Fapqtx7z4BzGSyY3PTop-AirY0pzItMSeOHAp6v6mIS_VeqwagdWR4rXHQBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_QipP6Ng0RzewaGjgTr7yJVRQ7ZKa7_Obr1DPf2234TQrArnyYT8lrKZRyZPWTTSUlLwumdBLdSV2JVvuAaXFKu0Ud52SsTESNglIwtohuHA_PdS0keqQCaH80NCiwC9fY15sS8Nh7_mh7NVxEPql4DF_tFYN3_brNtYsArZBwyELV9wiA0cNEt29Te00SffuxJqmLZ5qxlffaQ3Rtoh6-IIvPuGlSel-GzB0X30wuimMMMNVNOMLVjqDMiivAxucoCzE0bhuYtNN4t6qQDti_bVH1mponw7XRqLTHLUT60jh1Avi4po6wJLvJxMeQj8mvgV11m9Sz3nywi0ADgYg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNtsfpVBFQlJ7Xyr2tc-o5MBOyUrovjbFkCLJYkRSLOz-Ul_F6M9HKoj6UiKGI-fGDRH_tp545CkLSTdoZSA02nFR5uj_SYuUhGG1dWDQA4n8sAWoZmgHI7hwkil8JCvYRLje5WMmdosEEc_cgnbefeHFP0Ag_kq7yqcdWPTQgc_DRbJ2zz2Y79fN527dT8ZTjeVc2PbWo-nWePvZfmz1D9OPH2rF-RLdBfCNdOuEUPXsFxLNU-lbU2J1oceEGJFTdZ7yGRO0JkRDXQgb9zHQZ12-awzaX_Z8Sx_GJfXoEUFJgH65Iaw1jN0T4zI1Rb-QrZBmgzP_6S6pbwKDm5ajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2Q1A6CepYh-cigi3c2nCqIRDiOfbYZkqvqRgCH9PRKa_rI98Sn9RZOgIip_CRXtB5NEbSKRH1-BjPiTn4E6SMNnVPW65ufXCKk3Z06ztQMxK1PudAYICj6DyFBpPqpzb_7SvpXa1gmAIuj10h0fi5EqOdFqFriuAVbTBPDruWnDr1aj5Ajdah8ijy5uSTbY1UJks-sM-PJ_SInOtZUfLO-oHhlNFyQ8TGQKlPBiNJ3AtOA2EwWFaTDjIOQfrnJm2rooTnsYbZyou_KlyoIf14-vODevWWuUNIexaVPVuHZEQ3a5YNexodSCwB54xkL1YllU0ALGdMOLaQmtLSXsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFSbevwwJ2FsZD-lVdQxxa66pL1sGULc25psaclpCVKi60nU2CB6iOFDGzQRyHMtbqVtrr3Q70aWrGdqG2AyQsadmoalUCBOLucADn6PGvHQPa9UxccuAcJQFGMD5_JdVL7_qsStemVWE5sIyFaT1cCm918RIY9MYE516DQ2v_mmikHovumalkUJG0-nfk-NvpH3sCTETKFEimbwphaw-NUAo6vACkg4B3-7_wE9hkTG6_tPTwEMCjmzUYwvZZNss2vFyn9OD-Wdbz_BUviFLbpn7rBUU1T1TI9Rkq8Y_O3ogWfg-I6iqdkOcL3txa8mJtKnpmjWsTULEpM9erSOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBduFfX7eaUXQD1gZ_ZyqzClm7BuV47OzbEPIunhV7kiD5_4S2lbt3BAn066VwYcJbRDAfFy83EBafP7Z4LCSQpfHofd8FULHL33V5330cBY2XBtjRZHfzJfEpvsPV_Ls-rHmolGSBAGMyxK0DVYFA3SNRdI6vWTk977ZJW2ue-yNxJDqDrfqztZWYGy-rfFfGnsIElQz9G64mG5w582U4_5iY3m2GO43XgbBWn4VGsmRqe-R9QoFblpB__VHPG8VSVnhGnwyrV22a0fnCIHgoOtF7lfMwR6BJXZWUJTk6FSm6bB4Fko_ewSbGi6ijP8-hXNbOI-pIMIzOdU8IwoMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTpgW5sxtsrEobaauJliWnQgyRbhyD85dlgNzcKrb7Ovtd5epNdmp3z1DlHy11BTpR1QZVHOLdfKXk0d-zeTjoacUs0EZgyrwfRO7OUu1PXAze6qsb7xAFu0c_KhMnduHgFdlZoCYfTTXI9OzUHL4qF1iz4xd4VcWzB3pI357KhObDYtKAiCoY65Z8sQxN6AEqh7CMkLy-FYxH5jEVi1LCoT7fxwcPbd03eDr_SSIKJKld4edIhsIZSjlhggZytAVvtKkClCAn66Z_FM68WpkXsRIN0HR5y5tXHuqwiH1lADp6BSniR9PoW5ZpWhs77DL4O47D5WI6R3mIaREjjYbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMg58aSblK1bOx9ct6inbz3hA25dWn3hNbEwq2GIkitlwyTWXlfc2r168K2XeGOsHFenvqD7Eptz1h-BASq4Qf1sucKxhKWFTjXky6Bn3zgJA0ekQ-OYvH6C3rmDnlbz9YvdnqSM3cAJ_ufXphjVi0o4Z7REjlofvWvO286d8X2uKvLUrQZ6Rr_HyMQE0PNTajtiNHFJSl8NnUolZiG9jSAjT70CUqbysT5QxaWeIu5DbhjazI7lovEVjDwX3SyS09-P4dIbo573CmPCU3r8y3kQBOkubY5O5dN2LPF414JkMvXm0s38Wl1dbkm3KiWjOg711Sz8Hv-_zMUIItMYXw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=uSPhJKm8V1jVTtB_UfWRiuMIwYqE0rBVjXPut3GrZvPJx6udbTQ5qfoJ7mkKUrWwo8IqmxjZ88KVQfz0pTEX6LTwJqq0hbzu926KS1f0gQlBOmhg2ek64FGvtkUEc09KHQB7ynPE_BdTJe5L76wF6DMzQAoTaSgORFen69AHA5Air8PylGVDDX_Kg1Imn6DpwlLLuz-92K_Wgwcim714IB9e1MsaxLGVF8lzanalm1MlsuYQx60LG1bu8MnG9NWL5ZB_O0BqZyaYtg8R0rbptT-bKSpwxsf7KTLsH5rptAomHSHV-tk1zQI1yJafjKvJ4-gW2NRYYe-sAVu3bmLof6TWtINHvXKKdKvGLaIyPvlUt1aACMmrKnlDJDUGfow7Y0_z2GtzbO6sUwkuo5CXdxcozx3AOFx91ptAGtRshG5JvLHSHZNOM1tM5tRBzaACVNKzqeGkkh3w0bpyYcNr4UWQ0O_Q34qXkJQVsA3yXyryAUmqytWAINQrXz2MFRPz0ir8ko984y872gfQSfWeafeQKUd85tdVUyRFyUp1-C8GIdZUcFbgqq9e-Z7_GmZUiEpafAq6oqpV9E9qtt2hTzLAhuDlniNhpY-txCy0JCTXdnhOf5RCi9STPpIUSVkKVq-p4VMiy3WXzE2bcNaSQt41DS8v6WZfZ01x0ZTFlrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=uSPhJKm8V1jVTtB_UfWRiuMIwYqE0rBVjXPut3GrZvPJx6udbTQ5qfoJ7mkKUrWwo8IqmxjZ88KVQfz0pTEX6LTwJqq0hbzu926KS1f0gQlBOmhg2ek64FGvtkUEc09KHQB7ynPE_BdTJe5L76wF6DMzQAoTaSgORFen69AHA5Air8PylGVDDX_Kg1Imn6DpwlLLuz-92K_Wgwcim714IB9e1MsaxLGVF8lzanalm1MlsuYQx60LG1bu8MnG9NWL5ZB_O0BqZyaYtg8R0rbptT-bKSpwxsf7KTLsH5rptAomHSHV-tk1zQI1yJafjKvJ4-gW2NRYYe-sAVu3bmLof6TWtINHvXKKdKvGLaIyPvlUt1aACMmrKnlDJDUGfow7Y0_z2GtzbO6sUwkuo5CXdxcozx3AOFx91ptAGtRshG5JvLHSHZNOM1tM5tRBzaACVNKzqeGkkh3w0bpyYcNr4UWQ0O_Q34qXkJQVsA3yXyryAUmqytWAINQrXz2MFRPz0ir8ko984y872gfQSfWeafeQKUd85tdVUyRFyUp1-C8GIdZUcFbgqq9e-Z7_GmZUiEpafAq6oqpV9E9qtt2hTzLAhuDlniNhpY-txCy0JCTXdnhOf5RCi9STPpIUSVkKVq-p4VMiy3WXzE2bcNaSQt41DS8v6WZfZ01x0ZTFlrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=h8ICOrXUPi6YiEygCXf7o3H8RLf491_w3aWNjQpkUDdgHtcVm198IrVlWgBOSEAd_IlSSO3I7cy-yKA8JERCVcXe-qnZJcKT_iRNsFpsSN6q7vozEWwYBTR3gFlfujS8h3soOSxSklxTYAiFs1PoFigaF-6QX2c63EEhHDqk3tn08ZkZ5_VfLSjPWr9PPXqbXdVmlHoJPHiiS03FlI4PZk_I5AeO559x7-hUboFHjsNl4dTjZvlIupmLRJR8TQQjEwxO1fi9tmdwREzejFn0oCWSizEyWN2mV-2EG8NRjnwQxg4boqXrhJWfDkXNtkN8J8FGWwPde6k_WCKl_TvUXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=h8ICOrXUPi6YiEygCXf7o3H8RLf491_w3aWNjQpkUDdgHtcVm198IrVlWgBOSEAd_IlSSO3I7cy-yKA8JERCVcXe-qnZJcKT_iRNsFpsSN6q7vozEWwYBTR3gFlfujS8h3soOSxSklxTYAiFs1PoFigaF-6QX2c63EEhHDqk3tn08ZkZ5_VfLSjPWr9PPXqbXdVmlHoJPHiiS03FlI4PZk_I5AeO559x7-hUboFHjsNl4dTjZvlIupmLRJR8TQQjEwxO1fi9tmdwREzejFn0oCWSizEyWN2mV-2EG8NRjnwQxg4boqXrhJWfDkXNtkN8J8FGWwPde6k_WCKl_TvUXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYHF2YicU4AwECfYj47fuZfdfgkR2L5WMO98h7BwOjewSu0EdSdz4nNDnXyHtgls8ocbOELn3ARcbhpvqRMl7OJmQ0go2Cc565kMGZUR2Xce0HVRif6trjGooTN05efh8bW-ZO-MC04KGESAK5ywMqoBs-1J6LGI2a9grD-88eawY9VH5WfmcbttwJQPxAr5tt_uTDb687yeursmqMQ7NZBJTAi-IkiKW8vTFXeFE-UIXNM9YNPUJDeftjlm6LjF37dKjHuxpEpqwiaVL3SprUVzSn9cKemswzts5oW4wBbJjnOGiMxsOiglCY6mdFse_mwSfSmdOue8rN6f7eZ6FA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8aNMdKA6N9_ecqCEp8D8_Vba1siluHJnDoG7G28WZXuVPynbFpz4pj1Cmxcuuem4M6il_yuSlv5BFbvy29DACT9jWr7MzLEw1zrnH9TZ7e6g7fKSGdsHe1sGniyJLQeFRPAPrjMv_jCuBWv0cIvf_jGkyeJb64CxIFjn4ZU3PENWyp1RTnbQa_krKnhkj14MJEJcMCKkB_B1UxlKc3d4Gka4wuQ6uNkFtDUAymlThUlrld_9-XX_X_s2WPUrmauXibk3UsH1rK2QSqh8ZVw4s_PlCSnQC50QhEiL7PsGWTNe8cG171HkJ_ooOkBq1aP1zSji-67NJYj1zeibTIWRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=NjnuTPUfUQECEf01irbS7gjGMtotKI7ZHegW-HRsaVAjRvy-zgJGUMX5wjL7570nWZBQkkhnzGyQ3g3TN3qFspIQ8VHn74ZNi6CGSjFYqKtN3nT6xUF4oV_lfQ47BrAe38GXhvfsZ5nXsvnlR7X8_ZtkXKmtRhF1_dG3HEVJvQyCNfOEY_ScXpS295tpO22DJo8lkj7ysPppRA2cCGkDzU3r4452oHxa8vUoCXJ3M3RVAnVq53WSKfDjgR4I-7bubeXr-Ym1KbwsThONij7VxbbqARx6txvu2kmiuJYmNgRahpGC6OW_LC3T41mElUZszIugPT8pIvjOvgS2-7GfO4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=NjnuTPUfUQECEf01irbS7gjGMtotKI7ZHegW-HRsaVAjRvy-zgJGUMX5wjL7570nWZBQkkhnzGyQ3g3TN3qFspIQ8VHn74ZNi6CGSjFYqKtN3nT6xUF4oV_lfQ47BrAe38GXhvfsZ5nXsvnlR7X8_ZtkXKmtRhF1_dG3HEVJvQyCNfOEY_ScXpS295tpO22DJo8lkj7ysPppRA2cCGkDzU3r4452oHxa8vUoCXJ3M3RVAnVq53WSKfDjgR4I-7bubeXr-Ym1KbwsThONij7VxbbqARx6txvu2kmiuJYmNgRahpGC6OW_LC3T41mElUZszIugPT8pIvjOvgS2-7GfO4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzBTaKXRmH0cxDC-h8RWW5j5Z2MXZik9MNVTnvwgHbMzzcF7zMRfScfLcyEtDF8kZTQ3y3c1JVxT5GdfYg9OMJERnjiy4m_5hz4juA0uMOwGVrObcLU-IbCnX765HlkeHopHesn575kawQko8c1_QzbEfuRsBUbVyuB0iDd4LMdkIVQgTGAGredfsiPfJsdBD-UnV-diSc3viKQHM3etSoJs3QdSBzpiZdDVOi1za5_YLqVyQGYwR71nTLji1fAcxB2cMfZ_0RQh47k7VN0HjqtYM5ADVVT6_95_0d8cLnOaGlvMrvYRM1SdXliOLoSKA7N_GF-rVxUDEcFLTEnBpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ge3uUfFEBrX_m2AR6k4A6FGoTeBkWe_k_F44pAOXPW-Yp0abZBCNHMXRYiIoPVImPwPOcc1ta_wXOnUgk6Uw4vgw28zpVTg-KXF1lxgtMtoTs768zXOtJ5VSPeDsLdUm0JHnXSLhzjYR_fN-irdPpdTJEs6-Mng-2XPWFMVsoK270tjXXaH1r72wTGN8RuUZoDUueNQJ90TfXCNSdsaq94GW26RgASM67k9_Auw93jbMPM36tQP7mIPJ65RIW_M3HJi6oeYJ0M7-7-x1kXJQXaBBVGr2u86V8CJW9s3xJcmIAdVnoiIXEINNf-EHei-FyWzJSzTHy_Nv3kowJn7JWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIHYNC9p4VJSAcdspJoDVRuE94ywViTD9g6rUXfFJ2N-pmcseQ3Ky6usOt--NZIziuKf9Cn40rA17vO0zSNPsj_YRDs3WMJfWEWfW5iGlyTlZq2jjgLQEERXB9n1F-UdSGFoTjqO-1ArHAfOY8Zx-dQYrQd9OWsXi4A1mhhnpDd-QeID0FYwph1cCq2OZm9NoP1xDaTEGRXY_Nelr5M3NWzz-Ngxg0pmbrJjKdwyWLFKQQBTL3j4jJoXwDNoZtSuaiArtkuaxT2BbSONisSvW2RMuBB9Nxjcr_keNb5r_qMLbBR1TMcnD5AoOxwvDqMNIRfL8V2uw75dJC0XeJxCMg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH1YuwNtjcDyE8XUDaSjoKAZSBH5jLVydM2KU4uGR9qeNHcm0imyBU8BYQsOIzf83BeIdWmoVZ04PO_hdQhBf0WARUn_DhvzhSZJpxnzIpC8mtV3w-Dnm_PATL_iVnPR68kc8bwCYHaqfn1YpX5eExBmiTSTzQJxJTh8mDzWp_X_KvH2EY4OrBzoPLDBSvXxqe5oqj2wpshwbdunVt2ulJ5wuzfZJlcyEN4PxAo80JjLJt7MDD3yMaSsyAi7wyVlzNCaUiGaivd02Hv-alodp2FSZ5OzhDSrGeMqLnD2F08X1kE3pElJj1-_EqYv1ArSeITxsLMKzMgTxziLCFSANg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqJwgmpp01iphMQ-uIsfx5g3oej93iuqr0N0TfKJknXOSw3G3nV1xP4HmqFl1oQ63phCWmz6NJx2JM75C4FDqKRDipgjdMIO3_wQpPaKMkNczJ0cviRTWzIlr8lfy55j5FUFWLodl4C9EJ_33iYKmNNkqMMRjvBCysyWDKeLmJ_uEZkGIuxwaA3nvGvvRDICUf4Uyk5aY_oZhL2pHWzIc_TrImIxs-W5bmckvXWDvMO6DDAH5m_uunl0TSf6nJrWUNcSF_FLIUzFMmaoLHgBlkadyCHDD-DSR0JlXwiCLiT5WejdfEtb4tlBuBtKUTysWad-ZjszBXjoWfGnQExKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5axpvjjThgu7-twNZA8m4h69KBk7uTZFGhypHFuIuIkidjjw6h0uG8m0jlij4HpxSV98Gg_Pe6Cs1pEdbmLxEV7s9vDwsvau6JC3Q1wnORO8VEREuvi5KLwHXX6jXrJJ1_tiGCghLrO-JLekUg7lPUlaZOjTdPX4XrRSvIRZ7HJ20Kj8E5dpos5JnOroD0m6Myc56zkGRWXWn2AePzzbrjD2-2k3ma5y3pfjAkIAQIidVW99I5PqmJSRq58-YLvwcZ0BG8cZpRDI7IfeNthMpKqVabxW7i6NL6AkmVzarDXH3ROb-dIkAPM3VVpDrXci6tYstybZKznlkcEfQNRgTzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5axpvjjThgu7-twNZA8m4h69KBk7uTZFGhypHFuIuIkidjjw6h0uG8m0jlij4HpxSV98Gg_Pe6Cs1pEdbmLxEV7s9vDwsvau6JC3Q1wnORO8VEREuvi5KLwHXX6jXrJJ1_tiGCghLrO-JLekUg7lPUlaZOjTdPX4XrRSvIRZ7HJ20Kj8E5dpos5JnOroD0m6Myc56zkGRWXWn2AePzzbrjD2-2k3ma5y3pfjAkIAQIidVW99I5PqmJSRq58-YLvwcZ0BG8cZpRDI7IfeNthMpKqVabxW7i6NL6AkmVzarDXH3ROb-dIkAPM3VVpDrXci6tYstybZKznlkcEfQNRgTzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
