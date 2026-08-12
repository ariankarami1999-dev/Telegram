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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 20:55:21</div>
<hr>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9kM_hksh6LgTIi6Vp6GqAbNyWaND0nxhEzNctnoG3XROLX06ZEEkbTUEX-nt0GY8WHy7EYUkmCqCPypLNZvf_h_aeng-QcrPe-XZGVksrs2JIGHSrWsDKqkIzGL2ng8r1mUzqgHk4mM6U1spoZyO2AzIpklh1-UGRmMA1iO9Ce4AJ4LH4RGYn2RvmJSYQ6Zn02Ssz47zuRLoERp-K9XwKJ3tPideqxmbL6x7L_zVm_R7Ae5_1sr5g5lgShRpcoP47Iu8Uc0j-Awog7C06ErG_JgezXr49RDVuzPOxxxKbkIW6RvKL_3RrZETMED5ee4uPTKxNqG1_ffAEcXjA7Pag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFgTgBAaDE2Br7NXyrmnp5A7QvsRMXp2Ck7ehAh6P5elVRLqj4DKosPXIv5ny_gZodWWg5Vlp2w-2LdLpg6w8Ey9BOso-f_FOtcjTUS5LCCGQk12txvQ614Jvec3C1oK6_FJjC-JMMpFpqaOwzXq-j7MF8bvs4tqiztpIeR_i2ZGw78Gzgs-DSVzwgbNjCKM1kQOk_Q8twxYata4i2OS1XTBLxgfYLrGIn8PJWUA_vq_2FnvYdkIOqe942jVvaZJqta3eTKmdpUzVYwBDt_LCBn2nr-VsMuDAF4yQwpPthLwrxsBlB76FANGE3ai0AZPiF6hgVrNudc-oWl3gGYypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkO8g5sVoRGhJBARz9NkKWjqHnRSNw05EgAvZ40AUm4FF9iIvGhADF4FpmVRNG3cLpq6mzD66-yl7UTf_yV66LAPrGMgkuF6EhioQL3vJCXiZbptg9VNg0RHzVq_t0eUfcYgMu687pNj1Nys01jtfFTa9Yy260nwY2qaUAYayZka3RVhH8NfPWsaIJj3L-jbg-z9GTU5IJD0YL_vfRCsIaR45uwTR3IjiB3cMzJs2YtuHQv0xAYW0gAxVUd1M8-096pgZFMdkSSPEXOAsocdwulTZ62zrlklEXPTuwkRA_X0cgnIEHkocC6_H5Om9pzNKXVfBM-B45Nt6OwNxI5xJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzbfIfJVBG5eHvuGEkk3EUXFpAHgtdorrOCu5HVAwVzkxO8mv1QqADUPalsT7lYx5drAEUq6aj6zbI2ynfG6Sd1dtAVBFv4d_L_9hIKkiyhGWh2wWcVIX9M91IzIIuYQrXybG8KjnB1-HgE4hHUd9pCP9hoMKfRB4rcHuG3If1Y1JQ9x9Boti6WkYDJrrNMSiQaN-vcn0XmYOPiVixvA-t7EvRFrlUW6xlPUCH4B7gFVEoaxJ7nqsNFswua6O6p0AfAfJFKO62WDGx38hd8dNsR4oD84RX8KKdNldaqRitPv0b4-Rs7ETm1K4cEoaCfIPM6NWsgM7D5_0bRZjT7A3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHmST5RLWGJmfjAQWAb1iXfv3Tjz2HUDKP9K_GvT4cuqb0eDShKRpG-dxB3GTSdld1koPqljudy4vBLbpWolcDJaivBdxF5DPKY6-KmvU7nAoQS_kveJaWRoOmUIipJoQGALbD_I7bxOeJvMiIQ49YnW7OD9SoIKBTgtnKjjpa8mWMGCXgFXd_SyEwTCzj0jWcCV0z4weyzl-2-wJdzzjtJefxqdF_Ej8I9lmGfug04FQ1IUIMrH7idWoNrWJxIyeygYO1KExQvN4lRoQk9CjaTwj7kp-9nRXif7uRjP8dZhLO4V8Rj8rvIcBaXRBhNZc4fP88moUg8XnyzUY6FzlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qn7E-ZJobfeTNH6AGrbUcLVU4xpDAQflfyxRmqaq4zthGf8XXJ_eJxunGEWa-w4MWiev1l5jMc_wVpqFXINVXW-xl2lOHB4yNmiAYehDikmNPiyLT_KgwEVnS1g-9oLE1ThqxWVmgJmnUXbwZietSRNa0FVtNAz08624GjD4ycxK4boMioW6HcZ6fXc-UwgkGVnhuOEp4cAVfUTZV7accw3kaY6EUVovM3YAu0aVnBct4u3Y02OJ1pxzgVQ0mYiLwFNsAOg-SRcL24K5ByK8nRelCVkBYKGJqBwvoFeRw3w_UvMBxhJZDTPJwxCpOASVujvckgr4nJLvQ0H3iACQtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESrxsxZhqCdJgKjFQ42B4dVG2aeXpQlVwIRj5HoHDsNJXTVqPYanTXzQOVIrV_ywKRMNh5YU-5nPYIpN-SMXejObcSk8bp4YdcLM4qq3zgJuxkvtS8Z3TWpisMrmmheaZ0NkR9KsK4-4lkeF2J6X0l-tPL0bpanO1o3Ply4VnM1CN2Lq_nKO_PrnqQHxImyOMRvNzm9kDoPBbV7vEDvP34kF_ahTkFYJ_pzwSp5IKg6kR2JLBBbIoP9oxdLm4kHffQFR9dj2ZPTDoGYgslq3KyXxwjkZACSNkHWfPbSw8zQbqkrMEPKHmOSlHXH--ArLSIOqIlp1IQy46zEpuGgu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgM4TV_MSqAszk4xLats3HQJTEwKYGra7YrFGVlmf0S2ZSdhPja-sotIb74QwSMQIXW0y4uOobeTeiroSgwA3tOxhZLAElX5FL7hH8woi311HjjszQWk9qjF0ivYk1Z3XNRqSe1-0183-Ych6Qn00LIVaCdf24ozGbWMvvHdM1kOjYXC6xefOT4pZwaW0EsLUzbn1IGSi1LaivGIYLKXgLPKgSYtQIYeW5oz11SQX6rFtoUjeAzHT5IIOJeREg0xiwCksv1eDW6Hl8ol99BeMBYg-XRymeuwrF_qgSBV2eDu2U4KuByurBMIEixS7YqllqjPfk928yJF4pVzcwp26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhcyjiqDZfLOMVtxhQAAW8n6mBWza5ozP1ZnlYpmSYILCTJJMCF-EDLQk1zcfEUiH4kmivYc0Jrn62A5xeKzkkHEtUujwsESJc8yKQDG9ZaZ6lq26Us5DPCk23J63pjnV7zVaLS25zD4i6F0xRTuGmdjZBU7A4WvGJXk6d-xddZBizENbgRrY0zTTKhe3htugHdONnp0W02SGYI1TdrRO_5pmNjPlgZojCLFpjgjeN4rEsUuX4tOh-GkCXfu2Y8rDrsb571S5WOSwJklPkBgNV7aS7jIwvp-sH6Y_c0EtYBlelK1ll2Zbh59tEDzJKJSQIeaHuTlud937JkcpqWGkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS3zdNQYMJrlBOoL_VWmEYYq33k4i5-9C_EksMswnw3gxWgB0zNyEm4iA5G00HmjlVOuo7uAGm69BW_CL3W1CG8R4wzTkYAC9bcBg_YZ_BehZdQ2t2n8ZcholtbVy-Ti0b13q3Caf6oJgnDal1y3oN9SiEsfJHlXWCHD-MFoILbrCEdFCS9ywsTMZA9MqP1Kw9Y5IqRC3N7lDchEoUuxSP0IbwPiaEt7yZOpT757s0aEabLoaueSzthhO1X-qc6Jds57sdiLNGgOhA9VBpBwSsRh8tYnaL50HLwehww1NT3bm2zk0n5p-6V7bR2EzsFfped9mV7s3jxc9ntiR1zK_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا این متن با دقت بخونید و قضاوت کنید:    پدر یک خانواده،  نیمی از درآمدش رو صرف مواد مخدر میکنه،  موضوعی که باعث فشار  و فقر در داخل خونه شده.  مادر خانواده ، چون بعد از اجاره و….  پولی براش نمی‌مونه، معمولا از بقیه کمک میگیره که پول پیاز و سیب زمینی و…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6523" target="_blank">📅 14:26 · 16 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6522" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6521">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=h71zn4LhqmeSgRP1UqmCxTm9oml442lromGPwAhh5CCq44fcOARbZSHiYf5F64HxJUgJKH9C7HlXndR45TLzWei_wpytChRebgKqVO35o6_Cp5LCsQHzQU3J0y_xQa3megUeI4XvdIbdWoNr2W5bcLWH8K9mADt4kCSHnHHWjkfgI5ozxFiQytaiSNti59Vx7UNRTeVX-u-C1F4WdC7sCsQGT7hLsEYKbk-CE_igjT-msDA0WBPv4vF2RG9H-WIvagQVyp724GgxXPcF8P39NiaDlo9Z12aIFQ_0JNqg0ajBBoqWYVHKWaPBy68xcKeJWKpC3Vqp6hxNU0E8HyJ1IIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b591219d1e.mp4?token=h71zn4LhqmeSgRP1UqmCxTm9oml442lromGPwAhh5CCq44fcOARbZSHiYf5F64HxJUgJKH9C7HlXndR45TLzWei_wpytChRebgKqVO35o6_Cp5LCsQHzQU3J0y_xQa3megUeI4XvdIbdWoNr2W5bcLWH8K9mADt4kCSHnHHWjkfgI5ozxFiQytaiSNti59Vx7UNRTeVX-u-C1F4WdC7sCsQGT7hLsEYKbk-CE_igjT-msDA0WBPv4vF2RG9H-WIvagQVyp724GgxXPcF8P39NiaDlo9Z12aIFQ_0JNqg0ajBBoqWYVHKWaPBy68xcKeJWKpC3Vqp6hxNU0E8HyJ1IIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رجب صفروف، عضو تیم روسیه در مذاکرات رژیم حقوقی دریای خزر، مرداد ۹۷:
‏همه ما انتظار داشتیم ایران درخواست ۵۰ درصد بکند. قانونی هم بود. اما جلسه اول یکباره جمهوری اسلامی گفت تقسیم برابر بین ۵ کشور، یعنی کمتر از ۲۰درصد
‏برای ما عجیب‌وغریب بود که چجور ایران دارد از حقوق خودش گذشت می‌کند
‏این برای بقیه کشورها مثل هدیه الهی بود. از خوشحالی نمی‌دانستند چکار کنند</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6521" target="_blank">📅 13:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6520">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jorVtGZ0suwH-vPoa0xEV-kuOjM-dZAzAc6-iJfbM7FyfasR2_RKG43QZdTIFc9E8n4PbkQcsM4H958orgNYLGL8cBXF7X9RS6aZpBGG48udRH5lFjDi_ojStyyYSTbn4pxkDyKIblvjbn8aD-inTwR8gLHKi7FcTxG6EAEqMRIABm5_qmi9o_tZk3NWdq6qto1-CPYR1j8TnM5sr1yU4hjTORKaaoXpqq78sygEim6WB8GQ9PVO22EX7UbZzNnzixYfmKZMsBk5q1Kl8vhV2njwkc6GXuvJd7L0a1q1Wioh6B2J9q7boKmDUfB2Ah1yuADpfntygKErXaIVQrtrJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی به عنوان رئیس شورای عالی امنیت منصوب شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6520" target="_blank">📅 22:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6519">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5Ot2R57bQy05Q6_KkJo7VyhpwFQYt5LqUZPaq7hOUWoVdyppIzAd-Q4XBDg1xpVuaub2dmDnRTzktE-1TgwtkE51O4tEo2TjoW4F-JHNsufuUd-6bz-h7JASyKNhvyX9DilVyDQxbLqkx746WpM2TDsebcxMv8Ysj527j-24_3SYDH2ongP2YKhwD-LILzjRpa7CCOZ5N7cjW3KpRrTQ9jiQEUvq2LISCuJ21ypJk2xXCRpU2GRCuJgAGNpj4b2lFuJNajx9yJenDd94h8HdRTIqjLvDzDWflckYmnYBFXfXpAWysPNAvvbcSCmycYhdObKfKOvJFjrdRcoqvoHRQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HveGiTAm2lj-5BjA1tbdGhnEtYFHcOfn9-clEiXqHFqDcuVAqBYd_TqbuEEhbKZtE9y_QUjsoy0uFiPUuOytlztJrz2YZeJSFQeuQB-GVgqVF4Y_tuIuaD1tLcJcsDp0bNVEN7RU_Y5e-FhYH9T-KOVdEy3EeyDyovb6NdGKQEluCyivnuZXEwMe4lkVEPF2QsD5MQZRMVGTGlLaqrqKlMmlrhSgpBH5_r9bN6lJ4oeqL_oKC-eo5xPwfKQ6rqx9HCoW7AFcZVIY4poUqR5WqXtf1ABUEd4nU4zeKV9PUEW2f862jppPnJcpPHFQyDFcV6T9CWgdyTV_VXVthfUkSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی به امید بالا رفتن قیمت نفت و فشار به ترامپ، زد زیر تفاهم نامه  و حمله به کشتی‌ها،  که با اقدام به موقع دوستان خودشون  در حزب کمونیست چین،  نقشه‌هاشون نقش بر آب شد!  خدایا عظمتت رو شکر!  اما در عوض برنامه آمریکا در پاسخ  به اقدام جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6518" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6517">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQWnRMzOUcjm3DJMwNe2H0yEN1zOIPFOzpMBLqellRZp3cAFJLIWRHtV0JdF7_jOulv5g7y1K705lyLR8W-6I4LZliQU0YppF0t8gkAh1tErxLejM2sT8oTLEtaHUkXAYesWfUZRtER1mWG_dtt_Y7HJoyvCcVDRMBSgRuk8-I0GyY1E3-BBnJvKTur2NobdG1xy8Jvd2Emk4PyQGRI1-6c_HVPAjTQ8fGD_U0XNTgpXG6wJj4Y2h9VL20nQ4KevUaQXze_tNbpuTSKB3q393hNzLqj_a7hqNRHZlbhAFxRWLS1_vZxzCE5wKz520pQqT1zOkG59Mmq8N9AcjCIb_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکته دوم : افزایش تولید نفت کشورهایی چون امریکا (که رکورد تا یخی زد)، کانادا،  برزیل، قزاقستان، ونزوئلا و….. است!  نکته سوم ترامپ!  و به نحوه مدیریت ترامپ برمیگرده!  بازار نفت به شدت حساسه به اخبار  و به انفجار و ناامنی و جنگ و…..!  خیلی وقت‌ها قیمتش «روانی»…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6517" target="_blank">📅 15:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6516">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TW0kBNwRD7LNI1OtbUvkg_WDEjcXZrzCGD38oLs9B1KWmWqzl6cT7964CCh1coqGlqSxWStj8zhRaynhBomULCvL3JGswenG3H_hrmclf5EU1ZOdCKQxdX5B5B5VZWrcQDZBNg0C2kGHlXqMqEwAjjY7hUfBMvtUFKT_ST97CyUSfNsfuMsSMxXd8Nb-FK8kMPLm0js6sJmv_f989oxFIEy-XNjT1l0FBXfe7GIJ0LbHk4XcQz_eLkEFds3GduT7KYZGUnuWwcn4ZM9_-G1PdkpDDhx9faO0J8JL6sSSZ7lAgZ_5t4AjU53heYCSUhBOa350fG-8_Tf36WF_38cjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف نقشه‌ها و آرزوهای جمهوری اسلامی  قیمت نفت خیلی زیاد بالا نرفت!!  میانگین قیمت نفت در ماه اخیر با اینکه هر روز خبر حمله به کشتی‌ها رو منتشر میکنن، اما بین ۷۸-۸۰ دلار باقی موند!  یکی از مهم‌ترین دلایل اینکه قیمت نفت خیلی بابا نکشید دقیقا  «چین» بود! …</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6516" target="_blank">📅 15:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6514">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BB6MhF7SUK7TpYY_Gltq6RPgCpfFbIsRulwfLPv9I59yvgiDHInzdlLyMD3NY4-U71DHbyW3ofWyDz5qdXX69r-JdaY8XI6lNAmC4MM4FSB7Bv-SJEB7Saclatd72--EbRoO9WOzq5x8XxxG_0Elymf5mSXckoQIoTh7ShRNyZX-V9VFDzOQWRLf7R0fEGXQ3A0x2Kw20IM_xv3_v3nHnCvrI9C4JkTlNwwDh8HwYxyd7GO65M79f4HgvQ7Rv_fUMgNF4RR0gjj55N_yDKqOise67MLntbAqQ2pfHMuk5CdnhXMjJJG454BioPWL0vwf-68-fvxTwFWIcwAOKgttrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AEu5QJhWyDiBzvYJNo4rMVz47V4R_sU6DkeFEroY9xN1YtmYlEz-eiPp9oob84ORuN0awvjC4jYKS-ONlX1OLYVqMJwuW9tCvLDwI8ME1De9liFHTJ8joTSFks1YoC29cjrc3GuVY_tkYZPUxwfOeuMfsQVNjXokTvGW5HJwyTByoH1bzQgtCcQlZhdTAkOPVpCZi8SKa-hL_fmnGVj-3HJX-oY1njkDrcYxMmCcGjKLj6OZ5g_bVTMaLOyMQ55EmpsfZjcq99TaUkqJmp_xJmWbUGh23yc4cVTKU-iABxte1iA3nP2Q10UiOdGt_38ZOCl075GIQbnPwZldFEDPEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جمهوری اسلامی با امید به اینکه با حمله  به کشتی‌ها و کنار گذاشتن تفاهم نامه،  می‌تونه قیمت نفت رو ببره بالا و بر انتخابات داخلی آمریکا تاثیر بگذاره،  حمله به کشتی‌ها رو شروع کرد.  تا با ارسال پیام  «نا امن بودن» تنگه،  قیمت نفت رو به شدت ببره بالا،   حالا…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6514" target="_blank">📅 15:08 · 15 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=cNTUMr3ckFWuTNNs0mMBVNSXJHh5uaCT8Tyue-3IlBWWy45gcjtNXGsRh0OpllZN7lb-4950eByXoUHB1NvZBM6oQ24IPlBBhYMyGDBdRVecdrn_tJOlLgEHUqk_gdfegkyIUdsI7ZXi42gJC9aGo69YIxQVkOXhtQoOQaz-I6L9EYWjl9TM_CWkMOXQB7HMRLFPGdOj8RVj5FPJxL23DCoDrzKtG7C29w8lXQaw4MaUpLnmE3u1f3GvgLZQpE8icmHtYjDgakrbaVOh_5Qma6925WpTCuZeNt_Zw1fZYW_-HoQtzJXo1Bo-6MeVjmdxMaK3Xmi2wlqcGU0EGcNTcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07b72cf9ab.mp4?token=cNTUMr3ckFWuTNNs0mMBVNSXJHh5uaCT8Tyue-3IlBWWy45gcjtNXGsRh0OpllZN7lb-4950eByXoUHB1NvZBM6oQ24IPlBBhYMyGDBdRVecdrn_tJOlLgEHUqk_gdfegkyIUdsI7ZXi42gJC9aGo69YIxQVkOXhtQoOQaz-I6L9EYWjl9TM_CWkMOXQB7HMRLFPGdOj8RVj5FPJxL23DCoDrzKtG7C29w8lXQaw4MaUpLnmE3u1f3GvgLZQpE8icmHtYjDgakrbaVOh_5Qma6925WpTCuZeNt_Zw1fZYW_-HoQtzJXo1Bo-6MeVjmdxMaK3Xmi2wlqcGU0EGcNTcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6510" target="_blank">📅 14:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6509">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5OdMH_LYpdkomb8Bp66zIe09JYH9e6-0lKwKKCGOoe5CXW9hVAnB7e4a6a8nYwVi0ANA3uohz2Swc-A6pyjz2DA-QterYfichRi6kqO3NHh-Or2L3GeqOIbwGwoJ5kpxKY9fawiwEDAdeZnItG1Yn2V12pqSimo7B8rDjKxTi4fulTVAhy-ek70TULgDxDakB7WuhsgCI2I1EJIh_sjw_3UVfp6O_qDz8tLagA_9ms-3sWGNZ-uviA3htj-CZtyRMXYDxE8GolR1GtMUWqMeZOmD_blVn5Eb2K8m_s_VU9KB31skI01TJT7STbW5uefL8zesf9D2Y03AIVn3n2MZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب PD که همون نسخه حزب دمکرات آمریکا در ایتالیاست،  هم چند هفته پیش، چند مسلمان بنگلادشی  را به عنوان نامزد خود برای پارلمان ایتالیا  در ونیز انتخاب کرد!!  که آشکارا شعارهای اسلامگرایانه هم میدن!!  مشکل ملیت و مذهب این افراد نیست!  مشکل اینه که اینها آشکار…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6509" target="_blank">📅 12:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6508">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9BVmWqQcsTEyZeQOuuPTrvrqzqTshG-Y2dQfuoFobdY1JKAUFiyywMSVJiHxM0ZOlE9EeUBe7aRQsWQ6MlrbRP72jYzhkLCBYinkhvsp--Il1WEoRtRrseRUAILTtSpDENxLXnDD-zjCYxJua0yP7tkSAIgWi1zgvKSuQIcoN13LhixON8XJB6iCBuLedO0Ki1BKmaKVU_AV46qqtbWLWhlvaRAPKZHZgBmEdvF1nIlHNjLMPYZPzUcT6E_Q1Yhji4F31zuXK6qw_SfqexXwyiDvUyGDSAIAP4BKajSomse-i73YKC6xvXRAaZtPK_p-OdG7qX6elno_zAUJTuh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!  که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6508" target="_blank">📅 12:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6507">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=mOmxEpEff4ROEiKqMwKU6XXpprUPpK9Knu2ADYPtk_KK18ftgVqYbKvQkpwAAABrDelIVfWg_C3ZEtPQ27t9IhkhecPUW1oEA9seVZyu0GN_gCKkEnNbB51DjZlonmzWf0cAQ-cuRMmkgaBb6hziuCTdutE9Q8fwKcNM4N86b0YtHIoMhTeI0R5NwvtVS-d5NFRn03FcjH7DCNce36E9l1-fp0rJ8GZe_yH6dZRF8HSNihnKiDmUrH3kK9DpUvketGCOyZoii2H0STz2m0ZctmQFlWLzEf-t8kXJZHu9wSzTBZAgntp8fMfF8BuIfhaN1-azGPC7X2DlsghB7TzQhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e410a5f8.mp4?token=mOmxEpEff4ROEiKqMwKU6XXpprUPpK9Knu2ADYPtk_KK18ftgVqYbKvQkpwAAABrDelIVfWg_C3ZEtPQ27t9IhkhecPUW1oEA9seVZyu0GN_gCKkEnNbB51DjZlonmzWf0cAQ-cuRMmkgaBb6hziuCTdutE9Q8fwKcNM4N86b0YtHIoMhTeI0R5NwvtVS-d5NFRn03FcjH7DCNce36E9l1-fp0rJ8GZe_yH6dZRF8HSNihnKiDmUrH3kK9DpUvketGCOyZoii2H0STz2m0ZctmQFlWLzEf-t8kXJZHu9wSzTBZAgntp8fMfF8BuIfhaN1-azGPC7X2DlsghB7TzQhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عبدال السید» سوسیالیست مسلمان!
که حزب دمکرات اون رو نماینده خودش کرده در میشیگان و انتخابات مقدماتی پیروز شده
و در یک قدمی ورود به سنای آمریکاست!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6507" target="_blank">📅 12:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6506">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">محمد باقر خرازی ، برادر همسر مسعود خامنه‌ای : پزشکیان ۲۸ بار استعفا داده و دیگه «کاسه کوزه‌اش رو جمع کرد»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6506" target="_blank">📅 08:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6505">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7S32bTdkIH7fmFXWQSVggcWiFwjQFwzTBF_6SsR2kqz1OmHRk_trjikOy28hVmOwNYGKqX7h1ykMzHxJUmKDk3abRCaveesKv_Bv1lH16I-jnLw_wd2hFlFDjsgQuQ15uxzoKw9lcdqEEbLw6fcQgq71wU2ydSCCIGEILknlz4F7uCAZ9Y0Gw6q4b2dC0W1xNxWy4w5791uqwLb-UJ-BUnB0rfg999G7VlRu82udZOsQGCXaSE7YS_jSB-KNGYM1Cyd0jnmVUcT3v-L1KKVK4_K_JI9NSLmrzEx9ybuRPqlbZUKeim0Bu1cjX5akJ2jB-QEoUxrIDWCfh8RUYhzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توطئه است!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6505" target="_blank">📅 01:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6504">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آسوشیتدپرس: مذاکره‌کنندگان ایران و عمان پیش‌نویس توافق درباره تنگه هرمز را نهایی کرده‌اند؛ اقدامی که می‌تواند یک نقطه عطف احتمالی در بن‌بست مربوط به این مسیر حیاتی نفتی و کشتیرانی باشد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6504" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6503">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBBCPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZPdQ4fyfQRnfTEVCnA_zFniIHZ2PaLOs4mHIQEaP4DPAf8yhkoIxqxbmzjJyK39lDf7vBV8ON1hljrbyBl7oXTK8PAl9fVwbiDgAH-YJyEWfp7ovKuCqIBFc8nwRW75PX8MrMr9NlhU1Tvlu5wQd7tYSI_FtPFD1iPbF-tBLJW4iqq5rnbsqx_-tzBKKpbO7yw5EszzsWqpzNte2CIAFmddfpvLQuJiTg9-q7nE6lkZu9bjPSh5UimVx4MpclP3bXYSjTffXHSt-1VZJg2Dmnv040Ok3naK0w6WljZdJJHO5W3S5a7HR6G3pOdI0zYZIxbKRpknRASSf2Blg1b1LNg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f29785e012.mp4?token=Ywzfc9k8hgjvVOk-j5AltbA5_GpEvuodhiHq4BhaE4ZxMQmNfxp2eVEobkNIAd_Bh26r2Jusuq-iX28sBmPsYBW6u4Wspi9S6muUilHqL3ISs5o1DmU40gHdSIvV4zMjXSWKm3P0Tw4LZSYBkk41Vh1iaZ0PA0fLDQwOBey8ugyvvcrcqzZzFHC1qLVu3yqsaWZ6jRX17K0ooc-BltzUvhMO1HZOTZoLxfF8fZ8pn7Gfgloey4tfb48GMYBMN8Shu5YX-K71hc8st8kd69WsS47B8AUyVx9Ydp-KawqbLuwvL79dn027dX3jjOW8X5f9gKtrdVRoMpR1xghLhFQbrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f29785e012.mp4?token=Ywzfc9k8hgjvVOk-j5AltbA5_GpEvuodhiHq4BhaE4ZxMQmNfxp2eVEobkNIAd_Bh26r2Jusuq-iX28sBmPsYBW6u4Wspi9S6muUilHqL3ISs5o1DmU40gHdSIvV4zMjXSWKm3P0Tw4LZSYBkk41Vh1iaZ0PA0fLDQwOBey8ugyvvcrcqzZzFHC1qLVu3yqsaWZ6jRX17K0ooc-BltzUvhMO1HZOTZoLxfF8fZ8pn7Gfgloey4tfb48GMYBMN8Shu5YX-K71hc8st8kd69WsS47B8AUyVx9Ydp-KawqbLuwvL79dn027dX3jjOW8X5f9gKtrdVRoMpR1xghLhFQbrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اثر یک انفجار در جنوب لبنان ۲ سرباز ارتش اسرائیل کشته و ۷ تن زخمی شدند،
ارتش اسرائیل دست به حملات توپخانه‌ای زد
و سپس دستور تخلیه فوری روستای المنصورن را صادر کرد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6502" target="_blank">📅 16:30 · 14 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=bZZMsOn1XDNvHSLs1BC09uYhOheuBhwgNHKFQhdnZuT3N-FDlXuEYY78DsoYs_me9TVvXFspQfSPpyMuTjGfU561PjSHkuUY0bMrPLfJd6N7OdltyjfGvfxLR1nvL2-HTDSQ8SqQ9E_X_t_8Wb9jUpz3uBGr2wf329dvcDuUcHOnsahGSFwffQy4rIuTCx1mPcuuOAnU4no0Fwlw0gigoI9uOSr89qF-bj_GYIcYde16f6Xz3zDroJ7HubgfZrXTS7rrVAAvUGhcRfYLFJcAd1Amhy0kLCYLWGT5pycrEM5bXy1nlzFwj7qLmhy7REPDmDYH6gUbyokpz-SpML4umg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ac92640d.mp4?token=bZZMsOn1XDNvHSLs1BC09uYhOheuBhwgNHKFQhdnZuT3N-FDlXuEYY78DsoYs_me9TVvXFspQfSPpyMuTjGfU561PjSHkuUY0bMrPLfJd6N7OdltyjfGvfxLR1nvL2-HTDSQ8SqQ9E_X_t_8Wb9jUpz3uBGr2wf329dvcDuUcHOnsahGSFwffQy4rIuTCx1mPcuuOAnU4no0Fwlw0gigoI9uOSr89qF-bj_GYIcYde16f6Xz3zDroJ7HubgfZrXTS7rrVAAvUGhcRfYLFJcAd1Amhy0kLCYLWGT5pycrEM5bXy1nlzFwj7qLmhy7REPDmDYH6gUbyokpz-SpML4umg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمان مخالف اینه که از کشتی‌های  عبوری عوارضی گرفته بشه،  جمهوری اسلامی چند هفته است عمان رو گذاشته زیر فشار که باید بیایی با هم این کار رو انجام بدیم!  عمان گفت : تو توی بخش خودت اعمال کن!  در آب‌های سرزمینی من، رایگان خواهد بود!  که خب جمهوری اسلامی فهمید…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6500" target="_blank">📅 18:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6499">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcTSDhBInwNVwSfeSTCQAGV_WS71CFrg0pOWS3uUutNdNTcV368X23F6Csgj-uFn_YM-1tHL2aL8fFW8i7AuztBcqqADoblwdP2zys2emjrWODJgbdwm9uN2STbFaXddQ6aeUFi9Y1b6BWcoBG8epOLyGbGcQk85FhUt-eB9WgIFITRd76mMDTCj11zMnp0h2RoEBNaFkV4KgT5DDXUFQlUXEvKjGcL7cZrpWaHvM4bdhrS_0zNiRCgMgrMQbqyrjySM2gC2kV4vS-Qe7bDpTyBfGgPO1PRNkq8Dst1vod4MjZNNqeSKhiRxir33s4xs-0Z8N-XQfzpZEqylpwW2oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار انتقال گاز از ترکمنستان به پاکستان  و هند که چند سالی متوقف شده بود،  دوباره با شدت شروع شد.  کار انتقال گاز ترکمنستان از طریق دریای خزر به آذربایجان و ارسال به اروپا در دستور اقدام قرار گرفته.  قزاقستان هم در حال احداث یک خط لوله انتقال نفت مستقیم به…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6499" target="_blank">📅 17:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6498">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXaw_iMhaoXWgXP-nY3HFk79MNvoMEw_GCCuntqOofetGiFzwLbISBEtqieyH8kQwiW5dDGACZjba8pg2JWTcoDfOKrmgV5IqXOB0lPjjKAjkDzIMgWMevb9lIph133keKPL9zK9R9Apm8-OVTzvxwYdzF1TOX1jDHmzjGr9MxbWI_x_HwzrsVg14RsMf0Gc-uBjZeNEJqspfl-MxjtGqtd8FvzH-WcaEhpnBJyJ8Zcubv_41-NSEdUZLE-EYqpkJ6MZiiOAdp5gQIlkGvz-WMlBKH4QUNpS6w5ba4_i0LENpsiGuVVMX5juVznt31XXrFHH9HTrN4Ka_-xQOR_SRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌های بزرگی که کشورهای عربی برای دور زدن همیشگی تنگه هرمز در دست احداث دارند.  عراق : از طریق خط لوله انتقال نفت به ترکیه  کویت : خط لوله به عراق و ترکیه و همچنین به عربستان بحرین : از طریق خاک عربستان و‌دریای سرخ   عربستان : صادرات از طریق سواحلش در…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6498" target="_blank">📅 17:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6497">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmypP3a-NVfGMeBoQPhN1Bm9jgIGTcSBKDUAPLMhZRpcYs-Kh5cKFn1f_xzj6EYzXB3YeySzwOcql2Lx35lwFELHHil5vQwFCRvooSypFTsE1Hud8g_lLpwMttiX8aj28WsoFyt0zUPR0Jh3Trsnh_l8qKDcncqGN4Uy9CT1-3x_UR3MmZd9YkyTfCFMPxdGsvh7U66reOB41Jgq0nF0znxFtUSCPY744KoiiOph0f1lsyiY0nQipZI_Lj1E3v0HL0hhPwHQ5q5bPh2d2Bb9W2lf5JpxslYD5aHFQXexL6e1JZNlDtA-mabKkXFEI9u7CcciKtz1h-rInzfQtN41kg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=bfjXBPovtH3FDdYsxAqDSjGQ1ZM9UU_IWmrLYRquReYlYMOtTckUJ2U-pKExePKVGmUagRafD55j6BqIh7uaGVqWemjg9atICQz9P_M-fxk53rnOhe6XwcmoK1F-dC1iUzlGIJK8dByZmRFqPlyVJjYaudR5qka0ovXGSO5UdgV87QzrTQGmb_aPezTo3UrePVKvX_y7ESM32rooAwQt35suexIEiIun2i20CTUifkE0S7bv3edB11Z2ZzJ2Qq5-ejIT5m-6TK07QuhlJemAgDLza9Vni1rnfjTY7KdMbzbf3GMfhYxCRYeD3MQPhpye3q5qRAJaB2PdCchKhf-SNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8527f3a7.mp4?token=bfjXBPovtH3FDdYsxAqDSjGQ1ZM9UU_IWmrLYRquReYlYMOtTckUJ2U-pKExePKVGmUagRafD55j6BqIh7uaGVqWemjg9atICQz9P_M-fxk53rnOhe6XwcmoK1F-dC1iUzlGIJK8dByZmRFqPlyVJjYaudR5qka0ovXGSO5UdgV87QzrTQGmb_aPezTo3UrePVKvX_y7ESM32rooAwQt35suexIEiIun2i20CTUifkE0S7bv3edB11Z2ZzJ2Qq5-ejIT5m-6TK07QuhlJemAgDLza9Vni1rnfjTY7KdMbzbf3GMfhYxCRYeD3MQPhpye3q5qRAJaB2PdCchKhf-SNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=lLHGoOMCdasBv0uP8wJmVPQSkFLPbF-VE67U-T5HGiT3pydAaOgR0djUasv7IPEyxh0gVM3hhpDVLAxhPNCK-TNxPhCwNlKH592Qviz85YrcywHWbXi4CB0JJSYhWICbNMPtksMhkvLj5R-XNdsD7_KbUBSOWIxtZfv37Xkaaiqm-3farWPrFLtqvkT3tEZKQ_jt9S3QeKt205ka460GRByuVqB0XnMNFUr0wNsGQuYl0SYvj--lWfwzPO8qDcq4Qc4Bw0QhmTg7X0gbe9_pOrGwEytiIJcakggVYR-JY607Wl2SPcolniAuVCotIwZWiXIa4dPq_ZpIWWuJOY5ieA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d5918459d.mp4?token=lLHGoOMCdasBv0uP8wJmVPQSkFLPbF-VE67U-T5HGiT3pydAaOgR0djUasv7IPEyxh0gVM3hhpDVLAxhPNCK-TNxPhCwNlKH592Qviz85YrcywHWbXi4CB0JJSYhWICbNMPtksMhkvLj5R-XNdsD7_KbUBSOWIxtZfv37Xkaaiqm-3farWPrFLtqvkT3tEZKQ_jt9S3QeKt205ka460GRByuVqB0XnMNFUr0wNsGQuYl0SYvj--lWfwzPO8qDcq4Qc4Bw0QhmTg7X0gbe9_pOrGwEytiIJcakggVYR-JY607Wl2SPcolniAuVCotIwZWiXIa4dPq_ZpIWWuJOY5ieA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a204c96911.mp4?token=VsXDXRiXlDtsvV4Vm6tIyp0eqoNWihelaMfQ8yTSz5cgCK_xSLXYWyvM-v4vZ0d2RHsAra7rNOMUlYJ8CmPRzjAk0xnyO3sH-A4DxerztkoDZwV9psX2eB3LzdYIPfxzbIxHf8yLwHs_pF398jotil9UGzk5v2O_hPD812m6pz0uXkF7iWGGsx-BYcsi7COV3cgWHF5VeFQrGhHjff_deY42O1IeydoHAvfpgz0mEdd2ivPBPN8ipf9eEZ5SJibCofZGpWhi0uBuYNw-1aG_b6fZrf5h43gXtkUr-EHK1GUavFKiSDDFkr4e9LxgtOjQH0R3Pks9nXDecBFX4NlDHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a204c96911.mp4?token=VsXDXRiXlDtsvV4Vm6tIyp0eqoNWihelaMfQ8yTSz5cgCK_xSLXYWyvM-v4vZ0d2RHsAra7rNOMUlYJ8CmPRzjAk0xnyO3sH-A4DxerztkoDZwV9psX2eB3LzdYIPfxzbIxHf8yLwHs_pF398jotil9UGzk5v2O_hPD812m6pz0uXkF7iWGGsx-BYcsi7COV3cgWHF5VeFQrGhHjff_deY42O1IeydoHAvfpgz0mEdd2ivPBPN8ipf9eEZ5SJibCofZGpWhi0uBuYNw-1aG_b6fZrf5h43gXtkUr-EHK1GUavFKiSDDFkr4e9LxgtOjQH0R3Pks9nXDecBFX4NlDHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZVihLetKaxxSWVY5VOfiUjRuFkpRxNXuS1F4HrgSYiUquDXZoX134MMD7zPJW1NQhVBLuU_ceY4_0KPb5pJQ9sbkHLdI9MdBUFzvktmjovAqLq7DCaO9jZrG7ZIcuieIOREBjoMvuPIrUsowRCjlo_gXDWGDq1yFse1ydBDBxh73Zmg-iynYPxgyCRZEZr-D71nkkZk5mRcRpPY41EkV4Tp6vrw_idIWvCBH5A0B9hEwvo9QqRM8ZRp965R5-jUQHzFD9Q2A6h_G7LRlj0wTJyJnYS2lSja3RlrzhBw5a-7t-X4_Yw3QrRpJBResqbUgbSTsUq6ziKT46OlS2_-jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرگ نخست زادگان مصر اثر نقاش بریتانیایی «لاورنس آلما تادما» در ۱۸۷۲ تمرکزش به تصویر کشیدن  اندوه یک پدر است.  نقاش عامدانه موسی را مرکزیت نقاشی، آنگونه که سنت نقاشان بود، کنار زده،  و برخلاف نقاشانی که به خاطر آموزه‌های مذهبی،  روایتی یکسویه را ترویج می‌کنند،…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6490" target="_blank">📅 16:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6489">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDmslcMHLp1ytZ2Fxpd6CNRHiMWWe9jd3ua46BGxDJ3E8u0nq6fCMlreYFcSNOi1MECrl-RAuLEoDnZTVmsfwpkuNSp2kXbo9v-X6V6ciMb7RW-rCtLwRodyvxbl90LAjspBHyudnmDH5URRvw_VD0HSTgjZiiEiTRufPbEuIUPXJenDhyMP8IVhA45_DB2ntzOAuntyzDz33hw-pWA7-viGC7XfjlK2pTX5F4MI5TwiWnZOg_MHS8o5w2AzMwx5DrbijK-JXSt6REnMV2PicHMJ38z3lwZPxXctnYo_hCiYljSodYXQunR7Z0ISW0-vzqThkPGhkGIT8uvEHCODZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد چی میشه؟ بعد میرسیم به آیه ۲۳  که خدا از زبان موسی بهشون میگن وارد این سرزمین بشید و با ساکنان  اون مبارزه کنید و اونها رو بیرون کنید!  ولی بنی‌اسرائیل قبول نمیکنه که بره بجنگه!  و اونها رو بیرون کنه!  بنی اسرائیل مخالفت میکنه از این‌ دستور  موسی و خدا!…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6489" target="_blank">📅 16:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6487">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ObmPXB508F9c2hxakL4hCjeHwar65QE6UN1NctIe-J5y0ioiJ1p9ZnzZsmTEV9HIzkmzDl91mMPVFpeYJjIs98kpbm5zm0c9i0Tv_bCZHvqlzw41WF9tI2kcccKsCYHlQAJty0u-rumoSltkfraznsueQoPKmohLqQu96SwYn32EeoMiQ9wYiPGk7LegIn7L_db62ZYWKHuFokbpoiZfTcPGpE6wB1T3yZjy8-H4B3A2RY9QB3URaWBCLsrO8MW8fNnzzzrfGrQfafAaPBrXsaz0ijAqkPy6Xl9s4W1sA-1PxgcGW8TeLt8RX5DrKGVPfOQfxSQdz_jJVVCq5ZpVOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efywjA_gB6bEv0oMhY5kmJusonYIlh4r7neD3uJ9iflOCHWJb6JRkzzpXovRleaJ67PcJXAxX00EqUa1VpfltsKaelT4c1cICHmKLuwl9m6KvekfUQwNHeqzn8mGjNyrPdTgKPNhoIt4Olps5GJf3TsjUnCutGLPBxbuWpOe1oIBc8HNHRhbyS0vzeNsvmZH4T_seggPocOX8jaeo_xT4QfHXVWpWrE7M_i21yXx9Wlv_TPLzQLavdgoLJQyNCXZ2j0uHgzf36-qyMHL3iyCe8-fiarz9bzPqgu3i4pO_khxHYq2uLLmlEWFXacq-zZOVeoGchaVduw_lFYJ83phbQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هدف فقط رهایی قوم بنی‌اسرائیل  امر مصر بود و اسکان آنها در «سرزمین مقدس»،  سرزمینی که قرآن میگه :« کتب الله لکم»! «برایتان خدا مقرر کرده!» ثبت کرده! سند زده!   آیه ۲۱ سوره مائده  موسی خطاب به قوم بنی‌‌اسرائیل میگه :  «ای قوم! وارد سرزمین مقدس (کنعان - فلسطین)…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6487" target="_blank">📅 16:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6486">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UxiJ9w1DRPVbD2juPMi18YYF6fhqVcYbP5O1fCEctPWFYrWO6c9xsI0Am1Q-fM_EiKcIzBZFvvYm8ydEN8koB16fuHVc4Yfzs41zxcoWAgH1G1kbzsWSOdI29QuWztukGiVlXkcqU0kHJfvyxtzeM8Frt8S9fR0xeZ48hex_bals9sFaYbAlvwkJJR4tsARK9qnKc2BzpuB0Gj7qrQqjHbM6NjWni1d7i3uz2BKwAeUY02M1ACzIXVYPHSdhS68323CcL0AXXRDP58KVuY0qfDH9X3AsQhdDJOoKsC0x2rZwydu63w7QrIil8dRuYRVstTZTBGxPi9GO3f2IDDBEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همونطور که اشاره کردم، هیچ جای قرآن حتی  اشاره نشده که موسی رفته تا مردم مصر  رو از ظلم فرعون آزاد کنه!  هیچ جا اشاره نشده که رفته تا دین مردم رو عوض کنه و دین خدا رو تبلیغ کنه!  نه در قرآن و ته در تورات!  اتفاقا نه تنها مردم مصر، براش مسئله‌ای نبود  که در…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6486" target="_blank">📅 16:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6485">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaV3pA7WIr5vLkp_bpXOOiFfFo8XL4dFDM7AlEoN6OaW7upBnJAZllapep3hMEPalpoHJ04dIz4msnMJ5I3bQKWu3kpthw_3HJypB-exkF_-uJsAqigmBmyZureFJ0G4CBhVKJJJo0F7eN8pWMWEbnZ_XjCnueVM9a_v1oaRhncZ04igNJNGlq2eBUSbVhPmSIr3fnHSDhSix80B4vuMwFTmCGm5FRhH-czxl1R1OtVmakjQ5wmcmTsXpUMsY16RvO3UikvW0fz0jOcxZsK6XdA58wuK54Y0-SUDgGlwIilBwNXpfeILzLS9bNoSqRnplUUP6DttSE4wP2gxGL0vgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشتن همه نخست زادگان مصر در یک نیمه شب،  تنها مجازات عمومی خدا،  در برابر سرسختی فرعون نبود!  قبلش آب رود نیل را تبدیل به خون کرد تا کسی نتواند آب بنوشید،  نه انسان، نه گیاه و نه حیوان!  قبل تر از آن آفتی فرستاد تا همه مزارع مصری‌ها از بین برود و قحطی و گرسنگی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6485" target="_blank">📅 16:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6484">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUb3bwpodowe0_BmB6oeLyOl3gBZJx8aC9yNwflcJ4mxryK01MytFCnN0NgByTu95lKyxpKHseGleYylXAZjb1I92-Mqkrrdy69U0E18r6_uUc5VKCXbfDTzFMZrcDj003GO4aqI-frg7i1CUPg3mSQloxbfK2UTN0NOGPKiDK1vJYH-DzQj5zhKZtCIZ9LwrDg8BQZfPtpYH4iwuJhvuixQ8drCU0qGZchw4vWndqPwMrR9qCVr3zJY0E3BWpJ-w092HLTXikvkwzuQPFYEGdn4pep5k7FDn3GWXQ1J2vPI1GWN-Nuzig9H88Em4lU0A2aMedaAiVSVvd2XSbeGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا، موسی و برادرش هارون رو فرستاده بود پیش فرعون برای آزادی قوم برگزیده‌اش، «بنی‌اسرائیل»!  فقط برای همین منظور! موسی نه رفته بود مردم مصر را دعوت به دین خدا کند و ایمان آنها را تغییر دهد، نه ماموریتی داشت که علیه دین مصری‌ها حرفی بزند!  هیچ جای قرآن هم نیومده!…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6484" target="_blank">📅 16:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6483">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lr1q7A6xGAbp81QLgILwHVdlslCM1ls5dU5IwBFSIxgemFnAh6GSxDCfPnradRSTolnvcd5P9pQQRdrXRwHBHecjuRNjY8hobvkxygiVcXeIC8eGnVbuPraWYaSvlJt1CypzIyVPAeDouJl7z2fxQU3r-4GOW8Tn9x0EbZUHljL8c0cJXBrrBLzbArKJYfVsiOiZl8MZ9uA9VNftGHBh5_a1uJKuCfEuQ56XmARy70heeux1rnr_kYnCeu4xd2Lfuhak9YWSl7WRTWaXv_nXb1G40QnpAmrBCe9BdfqQ3X2JzEMQGGjhb9DnbhTMme5tgma1whTFStpH0gveK95YaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و همان نیمه شب …..  فرعون به هارون و به موسی گفت :  «برخیزید و از میان قوم من بیرون روید،  هم شما و هم بنی‌اسرائیل!»  ایرانیان زرتشتی، وقتی داستان‌های  کتاب‌های ادیان ابراهیمی را می‌خواندند،   دائم دچار شوک می‌شدند! و حیران می‌گفت : خدای ادیان ابراهیمی،  عجب…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6483" target="_blank">📅 15:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6482">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فرعون، جسد نخست زاده خود  را در دست دارد، زن فرعون گریه می‌کند و موسی و هارون،  در گوشه‌ای از تصویر دیده می‌شوند.  برای مجازات فرعون، پسر او، و نخست زادگان «همه مصری‌ها»،  «حتی آن زن کنیزی که پشت سنگ آسیاب نشسته بود، حتی نخست زاده آن کس  که در زندان بود.»…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6482" target="_blank">📅 15:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6481">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmBMiIlg3SIAetW8gmJhRCbrU30eGAanHVmpIQ5q2mAVJ01Vyu3QcUqq2jATosAdO4-AFgH4z4yOsM7n5g3VMj4SGqD9NnnDdQriM68A6XV_DO4WibOkmUlKFFAuAV1yZIGq6VeixV-0XbQxZQ0rgj84hAIfMud_bdHtFdUwf7JSNJIzgNBrPeWKK91hZZ04wCcnuv4pluJ4A0nP9K0bYE8Sen1K5HB-2d4lm90MkN_UEOlWyxCr0ht0XlB0JVqv7RiSR70LGNbA7B6yxL0LIo7nZwWHrBaYPxPGrKADCCQXDkVSbYT9gFPcVNd0e9lFiocTqjYSPiWS-zJBiUBQmQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixL5IedvTtZP6TGgFv4--kYqlKaETe4AzsTFLUGwmUzg3qO87tfaW0ahHAzOGO14KccrLVpMas9CF2xQ41eWhcJ0UHArqpNauNZs8cdG3I1Q7BgfvHQ98mPGnxdTWXC0dUcgvnNMDd883G4amxwH2s_uOymcHIheDMtg2AbBbpWlxEyr5WYBVSzLSJf2z5WccWah7phR7DquhGipDaqK7AhxqnwAb14fc5LCWKM2z9J0SqliRoQooR51DskXTi-CiZM4VzAmU4jALt37TeBtF9Ef0PEKhH5Nvx9xB1WWDC58LhdXZronVEvXTQ_QoEKib0R4Piag-3HoqatSj64UPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏جلال آل احمد، گرچه فرزند یک آیت‌الله بود، اما اساسا فرد مذهبی نبود و در دوره جوانی هم به حزب توده پیوست.  ‏اتفاقا اهل مشروب و کارهای دیگه‌ای هم‌بود که خودش توضیح داده در سفر به اروپا انجام میداد،  ‏حتی به زنش - سیمین دانشور - گفته بود بره با یکی بخوابه، تا…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6480" target="_blank">📅 13:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6479">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5NRI_K7bKEKHe3r-bPSYFulkVbTI6ohT1ujAY8WxWskoz1Fq_W-_MnCk6T1JLDa8zvrHaFi0QvNA6BCRihSpTlR03E319AXDTT7k5bvDbSeP9DiL1N7D3WoVbxZIIcHN1i-ab8Qo3DOwvwMmC3uuBIz8IZFGDFRRWuP-UGUBqACcOFKsxtmeh2ksFF_sFsXgC3DLZnG71ybHffZ8gJbZ3tBh_XUW4h3ss286NKu1jzg3M6-8KM0gl7kCDBbt2Rhn80M_rIHfi0aqVogrPqsWpf7Y0GBVIjzYMOi_3Nsj33FOqvtNOTE4Fw0sEWzD2B-yTiBTTUwTnZLoa3-bNqigg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjUHHkCM2J8K8P6srg0oV93jGNl9MF5u8BIXSW450RUyQLPkWq8awp4EzYa9TKnGqGdZaCfv_-GAHUtmwwuc672_H8X_MWP5i6Gs_4dlnm9GyW1ij4RlFyx6YbZqZExqgXDV-bkROdxnuACh1oSwjBphXzkZoMCyjKkUlexK1D9Icz6XIddP6UJqC7XZtpk2YnCvCAlqH0HQVtmLr3tk9MqidvdHuRE8-6f-eS9JsBM7qxmHTvQcVY-_ibG40X8Azq3-CqbnXdYtDBClUIf4MmfR-P2NZxZl36Kde2KkDfGTwdr2P6Ulqain25YIdQbW94kWD6ach0z42nFutCw6Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه شعرا و نویسندگان به مسعود رجوی  - سازمان مجاهدین خلق -  سازمانی که ترکیبی است  از اسلامگرایی افراطی و کمونیسم و مارکسیسم!  تباه در تباه!  خرداد ماه ۱۳۶۰ نامه نوشتن برای «تجدید عهد  با آرمان‌های زنان و مردانی که برای رهایی ایران پایه جنبشی انقلابی را گذاشتند».…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6478" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6477">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1qgGpoWm9hOuT6GJDolPN0gfutwyp2uiYexA7G6vwPTdbSmznj66UEx1ZRno69zf4AB6HHV_LhWPk5dVEnPg7wD58jFBdAMPgvsW6BgWiA-sT68951d0uyRtFua7jgOP_XVqt31UEjeA3WapDH3oBiaUYpmvxVcvZbc-52DcUs86ldF00-0tIjM6rvYmJ3gbSUBWJojopLqA81-B5oW-JRzI04A-Vfu-haSEJvMsLgx5pQ7mxGR3y9g0_QkC22CkziO_kqhG5ymI3zfw3UI1iT8Gf7BS0AUOWPYILes0VBJxsoy_dxqexro05yToQzdhqpJVfJJrIMKqDgZt1AOQA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6477" target="_blank">📅 12:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6475">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRRfVxClBj8zptfS5TzSN4dWlLwoyCiNKsMlUpM7grZ0q_bili4g6lrCOBqCvYbAwugw23fXgcRO9qszG88-pZq00wZCQyCSNKrKZD0iu74xRpwxAM0WwVvEKQdiPndyMLWabNFZN3sp4M9fAUI4uxg6NffQBmlJZIVvoDxhHsU5yePP7_96JPWNZJnws78m4HmBtBUwS7jqKcpzJKH9ArjPvInOwkoecTo3PifpsB1XbRbH9VwPKbB06MfIPlcA1cVk_Bf2HWdcSq8-2rK7pYx3BrRmKttRDpDfZpPozktcVieU1dAjCvGDYG6TEmr6zhdMwhcWyNAVQdUG1TLHvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=Zz3UljCz9oQvI2CsKkSJHNs9tKjVBq8Obr4NHLie_XrvPU3xFYkh_XYYNr4e9jOs0AquxFYYZO3SfArGjBBHSJPSXykxwLvlxUWFQV7Eb2HnhHEam6Us_TL-7M0RTHQdas-Son0WgL8oWE80uXuuWH8dXOmoXs6r7pHvqRuF9RZSKpFf7JmimqXq71-VI4iCZNML5hxKm_BkAMytqytfKMCYbH6HLckt0w_kreIjkiMi6_5fGAbE05w0F5EC39WefGUAp8_cBE3I3jC2_q9WrhNA745UGqF1ptZMl9YJE9PAHk0CtnQ5hFhRv0EVhMyfSj5HYqc9TyA9yfM7ZhZGfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c460b262.mp4?token=Zz3UljCz9oQvI2CsKkSJHNs9tKjVBq8Obr4NHLie_XrvPU3xFYkh_XYYNr4e9jOs0AquxFYYZO3SfArGjBBHSJPSXykxwLvlxUWFQV7Eb2HnhHEam6Us_TL-7M0RTHQdas-Son0WgL8oWE80uXuuWH8dXOmoXs6r7pHvqRuF9RZSKpFf7JmimqXq71-VI4iCZNML5hxKm_BkAMytqytfKMCYbH6HLckt0w_kreIjkiMi6_5fGAbE05w0F5EC39WefGUAp8_cBE3I3jC2_q9WrhNA745UGqF1ptZMl9YJE9PAHk0CtnQ5hFhRv0EVhMyfSj5HYqc9TyA9yfM7ZhZGfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدل برخورد سربازان مسلمان با مردم مسلمان.
نیروهایی امنیتی مراکش برای جلوگیری از خروج گسترده جوانان مراکشی در مرز مراکش - اسپانیا مستقر شدن و مشغول ممانعت از گریز جوانان مسلمان از کشور مسلمان مراکش هستند.
تصویر البته مشخصا با هوش مصنوعی درست‌شده.
https://x.com/farahmandalipur/status/2083837885224988931?s=46</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6475" target="_blank">📅 12:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6474">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBv4K96VkyBEkDNf1z5BoUOTdHuxVthz0Z8cHS-km1m-OZzQkr3eMp0KQRDOzVxEosA3gQB8RHrWEmKPAYC_itVyZ-Sx5vXROjAgw9oT2DFYxPSFUwgYkP7pFhGtfEJYIkSWgjMmd7CPe6Gon24qoaBcIBeyEhVeeYhpZx0-s8ptLyS46Zf0FCScSc_IHjQ1APw2tUXfst5TRk756fcjXVoHvTfe8WAeulTJ2vQs6gH1meqNbrIAd3pSLupiliDRF7r9Be8xSX7fpvsoiPacrBTT78gSnayJ1o3EOQS3EPjMAx-64hMkuvXoj7xv-VITJPJCMnWeGXwb3EmVMNKf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامپ : ایران و چند کشور خاورمیانه درخواست کرده‌اند که حمله متوقف شود چون چارچوب یک توافق شکل گرفته.. این توافق شامل بازگشایی کامل تنگه هرمز و پایان تهدید هسته‌ای ایران است و
به همین دلیل آمریکا و اسرائیل فعلاً حمله را لغو کرده‌اند
تا فرصت نهایی کردن توافق فراهم شود.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6474" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6473">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hx__j-narie00C-C0YjBIf6-PhQTdvgPMtxgCETvf1w4fYEc7a9T78iVXVjPiT35WCXrTD5ExfaknJ8rwO5qOeuHdrbTpG3XJqkBvpEpM-OTlhut0CJj6X14rcRmAnqjla5p7nBRfrv-Nn2JtE2a5H8v2rIpGDPSILmCHYJ-HxZCOs54coVrsVNe4PMmyKPUpHkHQ-I6xz4h9RtV2WwU84aFaxvVthHCLCEfyO91DyV9b4KyJE_fQBVqAiPFrK5NGOxJGUGDQMccjpPgSAoRZr6EYZQmeRZgEB2A8ZurvJ-nTG9JWw36OlcaGNVMEN5w_r0VREabWPUkP1wVc6U2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ در آستانه
احتمال شروع جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6473" target="_blank">📅 21:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6472">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrC29XE0T0OSDkL2sjusCJbHkyiABUJJW_GLZGX2HmZ0vmNaS5lKPL6UFlcx7_Xd4gGC7Sxf9CJlOsviV6n4u-YoFkGuqU0d6HLEX14GsU9X3W7N_Ly782ouk8KrGKjugw6dXE17PASkqbjG98_VVHEjdGAi2GALlOfR2o-QxjotZfkRSSU9OrJ0FmhgxmICx1ZNfvE4DzFwG0APkQbVKhkPLbtRtUVyg3AIQKDo6pEowEbnAOjlIhIGeOuSO_R4NEXaoQrLPWfrANEvI1SY2XVwhQGoNkG1dMrGZRM327WLxJ4C7dOimUJOfJve8HwjmscDj5WuRQeFNwkpbBlwHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDr1YmPYHzq7y3AE0J2mDcvR8enLWF_3JoSbO-asPEY5fKspoRBsPZmtdX76iYuYwA8iDlKeK0edVny_o_JittLV7OfzL-VgIISBWbC1hQxfckjwGnw8KlU3ZCKSQLE5spetBxuHICLiNA1Lekwiz2co11pdPqW6BgdE4EyBYDc-MciFqSIeGDVzDZ5aIhD3o5N0bErKukRuhGz-gV_re3FZLmLBDYfmtDU6eKk4FMgB8WMiMO9jLrwAp3IW2RMOmplti5nn7xRxUvv7iG6VcdvTSeBoso7tExE1JD9ItWCypOJt73c0q1AJisMjbjrX-2GexWNJwy_siD3FPPO2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرمین ۲۰ ساله و اهل شاهرود بود.
لعنت به جمهوری تبهکار اسلامی که هر روز ماندنش خسارت و زیان و هزینه به ایران و ایرانی است!</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6470" target="_blank">📅 14:14 · 10 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-6cMri7yO94UBCNILLajQqBkyjPrU10pnEwYmr9KkWf26RM4L0i3PHG26IBA48T5kK7bvln7xMAPsPdPP_i84yYmdrod_J0J2tvop1jyAmvrHDlVFM-VFEbhf6QT1yx-CJ95MlOPovJGfJfjOxTgcg0UKZNGzXfFtBdfShRqabSu4pzd_dNFM2ur_JqKwVqVcKWZ4VKLvVO8oBSBMGSIYZyh06hTbZY6V0TBLmljD3V3nkgLBntTmd3NweK1ir04ST3-Eg2HozeQmi1cvQ3thfNYpDw_HSIuiGKu9v4sFW0Rm7D0hxBKlzK-CVTHlNh5aGvmcrhJeNoWl4th6zOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«علی لاریجانی» !!
در زمانی که رئیس سازمان صدا و سیما بود، بزرگ‌ترین دستگاه پروپاگاندا و تبلیغی کشور!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6467" target="_blank">📅 13:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6466">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3reVCZ9UZkIKgbFQ2qoZpQux4RMkc_FENN8XCh0dfY13wrZPYvqprBsnnYcPmwpJbAaIghLqGRmdPC8x2HFCTJt5nDHZ_iqvZbfLK7rVuUCgZ23k9ZzKNufmTwJ0ozFAhm5ZYZ2QaFcW99so6kSv0ajXDK0fNRgjysRRMZ6a2YJ0eyzzPYqX6Um0Oq5dbFTfslRCqilS9ZabAZEehnVRS9OeqUrUMzcjyY9TXUKPr1OMXzVuzrXmjzhHCBY21H1wYGQyi4YU-7re8EOhZrZZRCvymc7-9ntFTuhSD-3XZq962x2LnpwjKeyauaFetR0pvOO_Cc9lImY2ZxOyMEdjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌‌ان پیش بینی کرده که حملات همین آخر هفته (همین امروز و فردا)
شروع بشه
ترامپ گفته راه دیپلماسی رو نمی‌بنده
و اگر ج‌ا کوتاه بیاد از برنامه هسته‌ای و…..
حملات رو متوقف میکنه.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6466" target="_blank">📅 11:03 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6465">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_rCUqU4kikKmrEajz2fRHzlzFCIKoyUr1W_86-_Ayg5acbqu7GsqLuL0XQUauRtnmb3uOHeKAkZDkvfjoaa-8TX5WEe3Y7U_xn0RuQPT4uwo7gdFP1NB_plCReGmbGGUUuLp0hPQIORYCHQF2VWh3jkn7hqsr1rvhUvx1Cq_0IhIss32TH0YhnT4Beitez1I6LGePP7meQDudvusKrGXX_l-y8m3djUvbQpzSC6N2ftaI09GIv8z3EAc-Mep1t4y25tdcpXJoBUFbTvIbKJ8hSkGjCkE98uiGTbyMBEtHRQkAFxewM-fYlsjCFXzQ1taIO5me9vJnt3JUB0C4pe2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ دستور حمله به ایران را صادر کرد. حملات احتمالا از آخر همین هفته شروع شوند و برای چند روز ادامه داشته باشند.
بخش انرژی ایران از جمله اهداف اصلی حملات خواهد بود.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6465" target="_blank">📅 01:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6464">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwS0KeUIaKtCC3klIIVuexs9n8B3P8eomIZsIVvH87oQs4KV6wVmRa020ydEzRMNvDy7yzunejmLPc9NO6bd1eWQlIW11b-RtemXti_6T0ljOvBf_kdwLeiYc074ZZGJDLEGQJnTkIbnuOLWC58j6STJI2BD449JCYevP5mLrd6Lhu5UAHeROFN90fgw0DtrZpV6KP21qBvEqMmXMKjXioXL8ty5ia3mm4DiLdB9H76Bm5d10ed0piD9qmPZWVz1HVSC1Depba9PibZMso9GSAuQ8Irh1qEsGhjV5_Z3orEt1xNwEHdxMXIEtE2KYKWVSffCQqihT4CFD4xFmIlCpQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=rDa4FhGAZGXMlP1jayPRABuutrfpOwttNt7wxBJdu5eaxydFRLsoAij4tcgIQ9tIVsFE9tc6uaaVyMDeIoiHyPbfGnM7XRcUTL7KSrYr4qJN7YYa9e-XDctRJOPS6nmkfke42wN2cms8eOJOOUTnHfEfxnRICZzZXxraHtc4lEKlhF4eahS9DPEA8_JdCJuBwav1XdBcxdEQ2LpMR7TZ2QUNF3VfZYxB9xIglHxmJmEVhv_nFPFbczv1vjMnSWu-a8eaSIX3-JGpvrKit1F5W68YzA8_S02xES5O7ZLxW8a_v6bB04kqUZP35IEPBwx_b7nazpuccOK-_-b20SoiWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a785c6a14.mp4?token=rDa4FhGAZGXMlP1jayPRABuutrfpOwttNt7wxBJdu5eaxydFRLsoAij4tcgIQ9tIVsFE9tc6uaaVyMDeIoiHyPbfGnM7XRcUTL7KSrYr4qJN7YYa9e-XDctRJOPS6nmkfke42wN2cms8eOJOOUTnHfEfxnRICZzZXxraHtc4lEKlhF4eahS9DPEA8_JdCJuBwav1XdBcxdEQ2LpMR7TZ2QUNF3VfZYxB9xIglHxmJmEVhv_nFPFbczv1vjMnSWu-a8eaSIX3-JGpvrKit1F5W68YzA8_S02xES5O7ZLxW8a_v6bB04kqUZP35IEPBwx_b7nazpuccOK-_-b20SoiWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سانچز در میان اعتراضات مردم سئوتا
وارد ساختمان فرمانداری شهر شد.
(این شهر خودمختاره)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6459" target="_blank">📅 18:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6458">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZezU-8kAHYjVQqgUzJ6WKIO6YAWPFntKbM3th4nVKCtJeFP2dziA0PgEKhJzjKv5y61BegAKFM2ZQmR0EY2kHqPQ87uzfL2JTq6bdM3EMDLxvU5UWq3JL-wQi2WUSk2e5Y3_vtJIb_rTELHtEd1aytgdeht6_roAw3YZNHFjEMLK6CtgFd5xlOdC-5wKogXrFBtz7gPx6u_q6_QLUAiN29jeR38xk0EAz7-ZWENeFPpPWO17KayESAUl3OqyJn0c2-4tTYY0ocNoG0sND4ue_apzNiMmpi76nDzYruiZeXVxHOoeTL1iZU1TrreL84RtuQZFlyM8PgrsJG1OtZH9xQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYUaNFoHqAggZME3W4DEA0P-8ymJAjbB3WP5lWn4hwN0RFN3eZnZPnMOHr16PlFlc5r8ex8UJ6T0-yjXLShs_Kg83G50F86KYMYxTkMybkCQ-1ibxoGznCmGMmJG8av9eKKmPeX9xrqQIrX-jJvtJ_Eg2eaJ5aoMzEJ75__diPOl6PpL0UcNxJrMa3meTIPhQr51HBwyp-xRZjpX2UMhNQOViWx9AQJ-fEmcAARihCLBpZrLm9u3Qxkn41Vm7BwPp32WMeQfAljyO6_9j7GMw3Kpf7Qh2erEesT1tUnUZRNnTOi49P5s__4n8tG1oEldnnrU9i_fKXJdhcoDRNuA0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادگاه سئوتا گفت حق با مرد الجزایری است!  در قانون اومده «موانع مرزی!»  دولت اسپانیا به رای دادگاه اعتراض کرد  (چون یک طرف شکایت پلیس بود دیگه،  و وزارت کشور و…..)  کار کشید به «دادگاه عالی» اسپانیا!  دادگاه عالی کی رای خودش رو داد؟  همین ۳ هفته پیش!  و گفت…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6456" target="_blank">📅 18:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6455">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqcIMrTTtuWctF6atPyeFZKIaE-jCDuFBqSh2GblDA_rc-oxOB-uhElzvBu0deEGUrHd8irMPXwap7VpYqcflXajH2S752MyDEFW4glbbwTV8ef6M06CFzREIveZyo-rPC8MsOPxExIyI2YckE6_A7nvwc7Pk2wXmFYp9sWV_XNiEvqdtIMYJRijGc2wSJ4zCYAMQVYwVr9VqFK_quwGL4urm6ZAmtBb-7A8Duty1cqsg0jSlP5_HrDpBWMud8AEcuyOKbrPZkSn1yVzHYhAldOCbcgwwt9PZN6cRJUs8LMcoJ08SgTc5Jb6n_pqq3fp52i1xX8Nimdeyh3pbx17pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داستان اینه :  حدود ۲ سال پیش یک مرد الجزایری  شنا کنان رفته بود «سئوتا» پلیس اسپانیا سریع دستگیرش کرد و تحویل پلیس مراکش دادش  (چون مرز بین اسپانیا و مراکشه، و اون از مرز مراکش وارد شده بود)،  این مرد الجزایری با کمک ۳ ان‌جی‌او اسپانیایی، شکایتی تنظیم کردند…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6455" target="_blank">📅 18:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6454">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZv5lwEsj3UEKFkR6F9_bROqEKBYKCcN84z_ak5fOgRkKRHnk7mNqhlxrHA1VSAJFmNIFQbl0covbUFIy2Ja6-iXKMNomcndMGIjQd5oKKeoUQwYEjfjwxtyQGhd6Do3XvyZX-wLVFM8Xg3uR274kDy67nCRkfCmRF1m97Dv5m9pE_QRE0wBCzI3SPSX8Z3GXJIN3E6MAHl-Bs6EH7ZeDQ0QR-yFXA0jZGKUp9HcwKYDVHefKeDZ0bmtQmry99TNx_sxMGk5BAA5jwNZDvhn2UTXND4whfi7VnyRAux3rPYQDRrxmpE8hOqdfOwJCrctLQ6WQp_JLCUsdV2lOikUPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایس نقشه رو نگاه کنید ۱ سانتیمتر برابر با یک کیلومتره!  اینقدر کوچیکه! با این وجود ۸۰ هزار اسپانیایی اینجا زندگی میکنن.  حالا چی شد که یهو این همه جمعیت روانه اونجا شدند؟ چی شد که پلیس کاری نکرد؟</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6454" target="_blank">📅 17:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6453">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCMnXrsvVkz9kv65moYAUmdH2fnX-gzI4bngOPd0llXofR4j1c_sUwg4Pj_hpmlj-gwPgqJoYSuM6BWFTj2FbXFUcCL8rkuE46F4Dm-bPIhE0iwyc8h6UFc0bhGh1EUPwi9USKG-2m9BN8imTqY_xbU8Lsln8otpBshlZGy617wnZRewrByYjSltLrA9Y53DrfM9xwduFyD596QFbueSLU5JSlxOkKg5TJMxszVOzYsbpn-1CzQrQcIC8qXGY1r7dUHVNdQlc-pAncPjlqCkeWz8X-bl8o9CiHXmnN2udja_pp4bH097hMO2k2qEJNCV6A50UNZiZk301Ix_wl9GWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲- دو تیکه بسیار کوچیک از خاک اسپانیا، از جمله سئوتا ، که خیلی کوچیکه!  اندازه مثلا ۳ برابر شهرک اکباتان تهرانه!  چسبیده به خاک مراکش.  و بین این سرزمین کوچک اسپانیا  و سرزمین اصلی اسپانیا، دریای مدیترانه  و تنگه جبل الطارقه. پس برای مهاجرین مراکشی خیلی ساده…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6453" target="_blank">📅 17:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6452">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cb0jtnsF4dQXmdSK-Y7EvBr0afM5YTjDy4ARnEQ1F5NivgClwgDo-1UY8DEc0O2QtF-h7wXPsEvsWtv6dea2ZIOZ0aYWijtiuSTfoupo28HeuTmbPjA3CaABz94sk6Kf5b2g_Uv-2gBv5FHwrkJp8xEB-2fMk82CZc92SFGpJ7ercuU6jukfbnOMIboeedQoKgICMHA1NPySkUij2DnrhtFF0WBLvAHYXlRg4hutxmIrYI-K7lBWrdywzwEVNFd1V6tAqLDqDjW8RY75Y1szsdLx_vsT9etDCvF7ephy2ip56KQhpxzL8Vrlh76-XKOpmGdzLbXowGZO1Ad5ULTZiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موضوع این مهاجرین و اسپانیا  دقیقا چیه؟ و مشکل از کجا شروع شده؟  چرا انتقادها به سمت دولت اسپانیا رفته؟   ۱- دوستان در جریان باشید که این منطقه از اسپانیا (شهر سئوتا) همیشه این مشکل مهاجرین رو داشته،  حتی سال ۲۰۲۱ هم یک موج ۸ هزار نفره یهو وارد شده شدند. …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6452" target="_blank">📅 17:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6451">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7LfOYekFpftnJesTiO2R2pNNvFaw2kK56_vQmr9UngybxlsjSrJJ1ZZUUF1JrYKjZ03cSWk2MhEc0c7UMAiaEAZ3VzIzKjZwhhEHplWascE3oB4PtvV6S6-rTjhqJV7NDjSaW4LdscSxBviG3sBx8pUcOuwFrnJ5Vrsf0G0FvmVRe_PGoH9_HC-3Z_sDsuPI5TvGcFsVywWT_jfMBCFli4t1ZpKobRO84SbxBhi42HdkiGe0GmmhzrAG5dFFUssk30bUHt3aEJraiHtn4QIluIyxCa_ftRYVh6IkPmnqTiZWeWhxbRrL4BGMmF8KldOt4yelox1zvyJEq6UfsWZiQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=tXYtIGvURdPRg9dze0lLonFk47scFer4jE5ixb2BGDHTbDB9awYDFnN5bpxhtpQtb5wDl529B8YcdQdRLYbWtt2UgFn_eC45a19raGfbH2ipsenPbEB2lZjH8ct54kGDptcG65BxZqveAITticUacmOQTTqIo-nUgFF_lsYEabEnLS8ctXyKi5U1SEZtZSfO87-i8mFOFa3C9RBhUJV1zkmGFSzSbtlR8pfIBMVUqyVgfRJcpmKg9fYEkVp2jTWDV6J936P9HCpWOUvew-iNJW6L819YbOi1fZGVFQR0RDPD1D67-vsu6tVtpgX2cgJ__k1yILSzwS5Pjn8xbuNfr0FLVW3RYjdINsVioETgxO2oQagofeRptnVVNAkbQVqcruUAH_w8Ca8Q0PIY1HYyI_GCMIcleyx5GH70N-ofUeqq8GzDnnvKc6Hruwg5sBh5qVxvI21VQhXRu1Ntf_AwrcVFJJOwSHMGr-BgKGFzTCLtaZ83SjUpfrSefNdbbYdO3NnsMU2zY03PBIp-UHvRDilXe9GdOspXJeCKKqlyhvVH1SabHV1CEeEttaGqLjdJmZQBPGO2Fe9KnSkot4U3hu5pAhtCHeo2Ljs5FGV-adx8pPJQvufQwidXecyieRdvJMsPvHFVlPu_MYDuwGFfeYM9b8K72PnlLH-TDx9umnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01e85bed45.mp4?token=tXYtIGvURdPRg9dze0lLonFk47scFer4jE5ixb2BGDHTbDB9awYDFnN5bpxhtpQtb5wDl529B8YcdQdRLYbWtt2UgFn_eC45a19raGfbH2ipsenPbEB2lZjH8ct54kGDptcG65BxZqveAITticUacmOQTTqIo-nUgFF_lsYEabEnLS8ctXyKi5U1SEZtZSfO87-i8mFOFa3C9RBhUJV1zkmGFSzSbtlR8pfIBMVUqyVgfRJcpmKg9fYEkVp2jTWDV6J936P9HCpWOUvew-iNJW6L819YbOi1fZGVFQR0RDPD1D67-vsu6tVtpgX2cgJ__k1yILSzwS5Pjn8xbuNfr0FLVW3RYjdINsVioETgxO2oQagofeRptnVVNAkbQVqcruUAH_w8Ca8Q0PIY1HYyI_GCMIcleyx5GH70N-ofUeqq8GzDnnvKc6Hruwg5sBh5qVxvI21VQhXRu1Ntf_AwrcVFJJOwSHMGr-BgKGFzTCLtaZ83SjUpfrSefNdbbYdO3NnsMU2zY03PBIp-UHvRDilXe9GdOspXJeCKKqlyhvVH1SabHV1CEeEttaGqLjdJmZQBPGO2Fe9KnSkot4U3hu5pAhtCHeo2Ljs5FGV-adx8pPJQvufQwidXecyieRdvJMsPvHFVlPu_MYDuwGFfeYM9b8K72PnlLH-TDx9umnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=e5-RBztcs3FBqO7DNIoNuWMMqWe9zyr02PBPwO9_Bxnh6BOFOi7MPsHVWrhkMVmDKm0HV_PMP1Bv-mVJ8d0mt4rPCI2LbI5AU7eMD-ac7KqJgzsrOTn_mmjIBRYoHJV_uhPRqb18bSoD8LneVLHPyccnRkR4Iwh7cUg5B62EGfw-n3CmoQx7zeL_LRAtpkYRNEw7OYd69eE9j_udNgKY-ich1-7ILoEHjFUlkbcfAEN_hNcOujGbCCVzj4IlrJj1Tc79uXYWPEVnOxtNJjC5VUi6IUT4Msuq6wuqOjLN9UdJcm1f1pGEJ9g3HBdDLNUxM2Gk95miO1kcXBJ2pIYCcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cabfb827a1.mp4?token=e5-RBztcs3FBqO7DNIoNuWMMqWe9zyr02PBPwO9_Bxnh6BOFOi7MPsHVWrhkMVmDKm0HV_PMP1Bv-mVJ8d0mt4rPCI2LbI5AU7eMD-ac7KqJgzsrOTn_mmjIBRYoHJV_uhPRqb18bSoD8LneVLHPyccnRkR4Iwh7cUg5B62EGfw-n3CmoQx7zeL_LRAtpkYRNEw7OYd69eE9j_udNgKY-ich1-7ILoEHjFUlkbcfAEN_hNcOujGbCCVzj4IlrJj1Tc79uXYWPEVnOxtNJjC5VUi6IUT4Msuq6wuqOjLN9UdJcm1f1pGEJ9g3HBdDLNUxM2Gk95miO1kcXBJ2pIYCcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان خاصیت ابوذر چی بود؟  دستاوردش برای انسان چی بود؟؟  به اندازه یک قرص سر درد،  تونست به بشریت خدمت برسونه که میگی هزار بوعلی و رازی و….. خدمت کنه؟  اینها روشنفکرهای ما بودن!!  این‌ها بت‌های یک نسل از ایرانی‌ها بودن که ثمره افکارشون رو داریم می‌بینیم!ً</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6448" target="_blank">📅 14:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6447">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqIHzIA1JqH9X8d0McbQYGNuT9lRIY_1S7sxouMiYf9RThkTHN6m-BBdcipJMWx_9nVMjVasqwMeC1YJi5KxYCV4cRScM7h97GwjDbgsDq3b1kY4kuskTEVmAYwi7VYgJG9gi45r8UCGZgn_4lksWMMtZRpoq8nXbpr9PgGY8EbpvJ4_Wn_kVBh0jk5UlFpsY2Hz2T3q2Bmi7gZTF5iGYRsz1XvpuAKlHDQ-Fgb13EbUdjza9kXhE9hR_VC8lxftI7tXoDlXHwh9oYvasbgnkYiSlXoK27QPWRTBBnV6yw5I0t6Cv_-ge1XayxmF-pU_sSvIiXNJPOl-pAfBUso7oQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgXg2lNwtXjJfOinubhLB9ELdT0iqDV33tSbUOtMfbPvHr8RiuTsuUf5WBVjCflRW1s7SHYBQVji6PULt64rSF7SHoKl1TAd3kCKNHeuKwpwkJ4U1RKIanSExnPPsvJTlYm_yR5MTgUiwRXOIzMNrYrYkaFANfGolrp96XtUv9AM51yqSd5X4zY662TNpCU3m93F5DRvPSi2tG7mAg7Ww456lNkg0qSQxuEBPc8XQfiOx4ZKaviULi1OlG-KREQiXFV1ic6UQS2X9uphHqjrVDfoZ1x0SBeuQZ_40_HzHwkOhEg-e9DstXcwPlYcIWdqACFEqDs2yLTO2Xu7zgpc7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=I0RvUkgdou9AxG8lbNVjrZ0aOcs45KxizWAci5f5q0jyHg9Kj0UqnAWp-GldZMB5VxIoVLtDQg3qBE1RfzjSfW2rX0DlQaWpTBfEZnH4nU3RpZmBqAaSvNCYZCrrMZP7iBTI4MYmXfELIyqVZJ8pva9oBlbSBbrXLm8hgGKBbHe_0Qtdsz637F8VnXbMnyceaEMGI90XVCgf5Rq8w5YgKDSbrsiZXITrNsYgjbqvTHh-ZReSSNfCyFTDMkRSy62kMw4bsViPOOo6ZlXUFqfUao5ArEvUIS-YUyD5jAskf8E8pBrYYM5Ufz685BHuD73NW7kO5Tra0lQUqxsdj-lEzIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1bde678e.mp4?token=I0RvUkgdou9AxG8lbNVjrZ0aOcs45KxizWAci5f5q0jyHg9Kj0UqnAWp-GldZMB5VxIoVLtDQg3qBE1RfzjSfW2rX0DlQaWpTBfEZnH4nU3RpZmBqAaSvNCYZCrrMZP7iBTI4MYmXfELIyqVZJ8pva9oBlbSBbrXLm8hgGKBbHe_0Qtdsz637F8VnXbMnyceaEMGI90XVCgf5Rq8w5YgKDSbrsiZXITrNsYgjbqvTHh-ZReSSNfCyFTDMkRSy62kMw4bsViPOOo6ZlXUFqfUao5ArEvUIS-YUyD5jAskf8E8pBrYYM5Ufz685BHuD73NW7kO5Tra0lQUqxsdj-lEzIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما مشکل کفش‌هاتون توی مسجد
رو حل کنید که پلاستیک به دست نچرخید،
نمیخواد نظم جهانی بسازید!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6445" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6444">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwn6re5IfoSotgkGn2AMr6DrvLZqITvjZjIeyEudgfI725uzgk2js7j-uCXLFSIdAgohyodXpN_3mX_zJG5TWxHlpaUehXIqrn2RCguGZ-Rwh6_tqVyROq7QhPgZdidt39scSv1FGpZ1IQAMDocHO2wDM6CEOOnZnkaYbcygz-V1A8LswGQQxmMWKrQFmNcI5V7a_7PM1rWkvfQ8onl4BJJiLvVmcs4cOdkY5q-PSoi5NaKVyivMGX_i8ALlLLrXQvdQVKoKQko6oldUz-aF8bpxsUgs3s-G4mITVLMl3BTUJMm_CdULvUTDrrDOT8I0qJJrNNtushos6P8wX4uOcg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dI4TfkmixZOTVPMRHZs4NBNBJQBYIZvzw5_91tIb_ALVoWMsS9tYolZrCTfzMFpfyKU6Khm7ASmdQQCmQn-Q9pgrBDKZIxUJ_lVucAGj5WVDTnfX_0otaJmzFPWM1TCFHUGhNqZirKgWSz_7qi-o3RIBDIYU37R49gA8NnzKg6nYnE9GdN7cGks6jM3HmbQ9K8PGhOw-cH9iNFLZkgI-kIwJzS5er3pFo1EYGNg_K0iH1KE65QlnHG_RBolq2C-SqKUmO1_KVGRIxEgMnc3TQqp_pwbbEeRHJKiOKiNy92O0CMg5NVJ92cVlwM7L_w6MqB8pQ8Ynm-6jBgrzvHCnRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه امروز هم اعلام کرده که به دو نفتکش در تنگه هرمز حمله کرده.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6443" target="_blank">📅 13:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6442">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KPVPpRJJZrvaXg7xGL1TJyQh_AGwHv-dXTi8b9wR7WgRhkaZ66oeWZqa8MnxA4K8XDps5SIeRSR3w_Y_Zi6qIK_-GQRGdkEmOgv0mBGCYBhGc-CXL09Gszbn0ew6lQa-omPnycA8Zpcx4d0yVH6zOMHGd1I02Ba3YgB8Vn92Avb9IwYY6A35bUOO2O9jJj0ZoZvmDCHUs0DgFXGGwWi1vkC4rvAWEiHcD1FMg_UvFOtmnunYuVhJErO9B7YOqqqFulSWTCcAgvHcLwyLQclASKD-nTot-Gn0plPqYGEbUFeui6SlMcXnrtkvqSmzRY12wGQu1a2K6SKT6FH9DEzH4Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCt-ZWa-vxox6UbyZx5vMtqH2bRbUdNKwK2dWlHK5oX31VtvQsZkaJwmZOCCLgKSanl2_KDItWhNKcyv57cjDjKYdOXEDa20q6BVQJgHiTWoopSEFylHJL-VQKgrCmofqfBgZVfqnYSR8-mcBTpKCPXyRhHiCsiBjNGW4mB0aZ49todwgrF20OXZS6Hs_1WrYZBaI8GDBPWoUlAMDmkHrDFXG-aXPzCYM6BMZaFEXMVfDLKKVJlrMKzonjIkduwIWPwBoXVJy5J1CLDuh2w7_nQLVBim8c2WIB2opoNyqZd9mTprniCfXKTN0rvbk033ActEzp-_gOMP1v7bh5Ubsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8IarzrtWbQkGCCsP__Z2wsYWSKdUCp7ubiBHKcOHA-xjGGz9zSTtSl8coEr7kU-5dGlxzumiBg_Z-77N7EilrGMGVTh6cPo4uhHjTlx7LBtidb2Gk2Ny7pWHSKKQPnWFMbdCUGz9kJDO2La7UlYYelnVP4aF0L6kJGq7QpHWR9YaRPUORgpO9Aj1FMler1oMKo22qCF_-EHjSi_A_FkbwuA4_SId22yE0-5aRG6KGO-ufQp_kMLw0bTQyrABTQj1xjvVD2PXkGfIjBDoXHbUBKhRKHNsBkaO7YY-yHbahn1MoxX0Kqp09IrXWJXrMVo7h6w4QN4CDHOjbh0pmMmUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقه‌ای در شمال مراکش نوشته :« راه سخت است، اما رؤیا ارزشش را دارد.» پرچم اسپانیا</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6440" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6439">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5WUVfmuFDfe5wYMLSOU80YfUZw50-nbw6gdMjKzkELYjCGkmzstQ-cr0p8UDbwyuJ0yCSgorgheiSjCeMJ4r9yvedqWd-6aakER2LEX6ZUMQin6gcQUO3a_5nbAD5HeMSrmyDQjGu2dsB46_6xtuSeuYL81XG5Jkr--REJlIKqgvNjwlf_AvevlV-Dni54IFe9ioua-sLXBKAhT3CNDF6dFJI4xXJQTOUk1Jp9zQbw5nAVWQQaWquFb7iUQwKVNBFcNMnis0s4nCOi9SisovRCuSUhxLGLydrUGKPnlM5WGYLmMg6YBfr5MuytqpMOcmHgJ5ZlEOrkuQL69RuIC2EX0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f328eb8c.mp4?token=gClhvqRqodctA9oP9Pdg0bqJBgE_BCfgcHbtvNgTtfmIldMlzZPGRcHqbHDjl7IGBJDTdEifUYQsnJPLmoXwFqmjvXNpLK08mXhY69pro91iN_TCFVJgexzQLt-5CKm6YvU4eC_Uqu9hUsLUQUFjlIACD7R_lB0Z0JzkNBdi6C1qw61iC-wYwprJyi-UFWSSi9GK8le9SrSqBFXNYV9A1H8ChUR3T-El7hG6ccmLJrP0THsOM7VkRZHCRF_rkFFS5c7A2Ti1WuKf7IcUXbM9s41VoX0kZFFAR0M_b3x-Nz7_abTVpBSEsbeyUh7hJJegsHRcxTe0cDerVN0Imlyx5WUVfmuFDfe5wYMLSOU80YfUZw50-nbw6gdMjKzkELYjCGkmzstQ-cr0p8UDbwyuJ0yCSgorgheiSjCeMJ4r9yvedqWd-6aakER2LEX6ZUMQin6gcQUO3a_5nbAD5HeMSrmyDQjGu2dsB46_6xtuSeuYL81XG5Jkr--REJlIKqgvNjwlf_AvevlV-Dni54IFe9ioua-sLXBKAhT3CNDF6dFJI4xXJQTOUk1Jp9zQbw5nAVWQQaWquFb7iUQwKVNBFcNMnis0s4nCOi9SisovRCuSUhxLGLydrUGKPnlM5WGYLmMg6YBfr5MuytqpMOcmHgJ5ZlEOrkuQL69RuIC2EX0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت دیشب سئوتا  خامنه‌ای هم نیست که بیاد همدردی کنه با جوانان غیور و به پاخواسته مسلمان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6439" target="_blank">📅 10:17 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
