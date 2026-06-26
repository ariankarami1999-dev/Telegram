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
<img src="https://cdn4.telesco.pe/file/BTzqOyjUJdCc5XdnxlQ7zqFf2zaoV5tgStPezha8ou2xCAp3s5f4hss6muFsAW9u5yfdr0mBp-JJQLdFvIOIGviOzHT5W8CvNnM7TpRufMPJxgb8KSLvb13QB9xt8GjNKHc4wj3WVVX8V6OBfA37juzjG9iHyxDfRdGyQT-LU87GrMi1CxR5RIyd9J4Uy1nnUmkxEJ1cE2h7mP_5zzug5hiw67Va5v8mHTv9prEOeOCoQr84_y3Bh382olVZkmacHllkJ4DCDTlnKgqAB2tBLjbjZ5o-rLe7Ajfggbj5OO6N3F6UxyHVRfAVfOTGTgo0yzc9aMIwqpw4kPqahcVKeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 319K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 10:14:50</div>
<hr>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIuXlL90dLiwLBLKCz4pAMtc6tEX7B6anC0dM0JxSOi9zp5FF0Hk4aFHMRUzNtd7qC5nTgmqgly5W6hiZJHFUi-Kp6B3-9263WRY45AIRfiPjKtYDAbakuyFGaVNiklP-p1DgTwBeN0XHwoSpKMrYFmSoLFajcKwSC44VxBystIvmsdd5FBj2htGO7bJzk2O8T33OqgsRdkK9lWGd6fblVemCDi42d8PW4TPhF6pqDpx6LBm2AhBAxo-vBsZQGUpV3oi0gva_m3WQbESX1e5S-6U-_mv76UY9kDdSSQoOxPu36anIlBjj-EYc-9t6tMTXW_wdIFFN1zlClcg_SlcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/persiana_Soccer/24351" target="_blank">📅 09:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24350">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkO27mitCzqnQWUZx3avSOTS41KjPa8vuzJs4n-eK3t2AwJpHQwhGdOyq_ISO6jb0SVJobTNIBFi64M4NKaFXswABLjowlZN_ylQpaaRROWRJ0JYyGdbIJBI8vMJmqDXn6dxdq9vEtSFMiuh_9CfkP7JVwalL-Tei0g4PnfHyQF1S_4hvUIP2svQgTJaCvG2OfNyrFglQITorrad9s7yKYciei3BjCHy9HrOLl-rCAwffbCae1idSzoALihyF0wmgcdoKtige0CGbpbS6euoOL9QWlDJtety6pjodk8KyR7Anr7_1ZULtrumCf4kj_r0Gisb9VKk9fhyhnZfmuZIyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ برزیل در مرحله بعدی به ژاپن خورد. هلند به مراکش.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/24350" target="_blank">📅 09:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24349">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=XAMFHIYl8YspGSDwQo-nY-35iOH7hN2RlgejsdqWI7CZ7yW4pO7VIVlxAbI7e5GUDlLcmZbr9Fs0UaiI7aTCuPQXgDZb_G2UgreWMi6asX23FkwdncF0sLtCsU7liC9mKqrsIdxFZmZCLaoSDkEngIv6GSoxl1odole-FkHgkutG30LzmxE65m-V1pSEeIeWf_Q7kPHKdZVlwWadTJdWo0FUaDs6J7X68Uzm_JktbpKL_1Y0znH9CZ06eqhOsRg6YPd1m8udEUHGQbjzoq1KBSYFCOLf7LmJ26n8Ia4Cl-Pve_FKbJMvQh2FupkFbppKR2f8hWgOJ95_RogZRCyDvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=XAMFHIYl8YspGSDwQo-nY-35iOH7hN2RlgejsdqWI7CZ7yW4pO7VIVlxAbI7e5GUDlLcmZbr9Fs0UaiI7aTCuPQXgDZb_G2UgreWMi6asX23FkwdncF0sLtCsU7liC9mKqrsIdxFZmZCLaoSDkEngIv6GSoxl1odole-FkHgkutG30LzmxE65m-V1pSEeIeWf_Q7kPHKdZVlwWadTJdWo0FUaDs6J7X68Uzm_JktbpKL_1Y0znH9CZ06eqhOsRg6YPd1m8udEUHGQbjzoq1KBSYFCOLf7LmJ26n8Ia4Cl-Pve_FKbJMvQh2FupkFbppKR2f8hWgOJ95_RogZRCyDvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/24349" target="_blank">📅 08:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24348">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTHPvqqaQEzkpU_5XCTH--6VmCe1G-nYZN-hAqCMarG18lfjK8g7xJWWyc8QMPJ213z8GvADDnxPhh5UBlAeRHBe1DZlmP8oe-COx2Qpo4yhOIFMHabYEXsAaxVthRF4UoHVpFbn3RY-6RzCNAUbF1uBK-_JTSSmvzezk7rTV1td4c9xU0orqcBGHm4QY68qhI7Gs17osavhvFyXYNl034dYTYHBHHJYcK4lMrQw4eX4-8aLXY5EAaDooTUsm2Ht-2sYLhKxIQPUWv5osG1j4Emu0UjnHxH8a7dfyt7MPwqpnygLhz_KV3Wl3LhmTzGchF8KmEaYWuNXeMiQdii9sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ ۱۲ سال پیش در چنین روزی؛
آخرین حضور جانلوئیجی بوفون درجام‌جهانی؛ آتزوری فقط یک تساوی میخواست، اما ضربهٔ سر گودین در دقیقهٔ ۸۱ همه چیز را تمام کرد. کسی‌آن لحظه نمیدانست آن اشک‌ها اشک وداع همیشگی‌بابزرگترین‌صحنهٔ فوتباله. پنج جام جهانی، یک قهرمانی، و یک خداحافظی تلخ که هنوز از یاد نرفته. پایان یک اسطوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/24348" target="_blank">📅 08:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24345">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbEUg5P7EsUEQAiO7RuFEwc6K6dbF6zacQ__dqkdqaXigBOS_7Xtnvc6f2OoCG_0E_6FRboh0NffMKIMor-GserA441UkkE9JKVi3JHBcCf1WpV5KmDJnJ7mB_381BDn_Xt8qLHn8Xo4B4ybTqn1RwoPxtGRw-HJfwkyp58nrqr28enYX-CJLq7enrNIKE6CTMeOioXaebVxI8RIcffK87ZYztLAPhjAxVJis_AbHjaGX7xWpgy3_v72sazgjZUEx3M_fmLtmK1KpOLjvAOQyIj29GJ56THCu6g-Fv05eHecRNN-89u3rAUX6ppluYXE8W9CEhWnH5_fMkwaEApOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F و D رقابت‌های جام جهانی در پایان مرحله‌گروهی؛ترکیه‌بادرخشش آردا گولر سه بر دو آمریکا روشکست‌داد؛ پاراگوئه با استرالیا بدون گل شد؛ هلند سه بر یک از سد تونس گذشت. ژاپن هم با سوئد مساوی کرد ولی جفتشون رفتن بالا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/24345" target="_blank">📅 08:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24344">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCOuIosf9jTanOAaDHXR4yq7T0twHMa58BHW5jpg4HAABsN8FCJZA14P0PgME5HSgSjpYiOq0caLLnXmRYKy8eQ9KNj4LYFACyiweB0XaBubw5F4xKNl6TlYYw-YpTGsQJPUuBJqGAoWTnXi5RiCBokvQT_RQCuEToXm8fL5qsoxoKTqYNMoHT15XqKK77fkhW0BDQ6ZB4k_HC8itpVd1-hcwgeo4ep6falLLmGzF6xgNBD9dmpdCVgdNZuM59JG7s_CqpzzqnVLRBV-u-4neBZIaDUoV3pAPQqxn8KTcKG_4MMW5xa7m1W3Z-TI9Kol8X8J1QsunCMDb1kUkkteDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛ از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/24344" target="_blank">📅 08:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24343">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzqIUyoHgiGrkopBxXYB3SVApdySNzk2cUF9XBNErfFMDwYMaRNs3zb4qlJMcKoQ5UkJO_UeyNppkqOt44F0qRgMNOmLTJ_2NzaNSCLeFhSnOuUxShPJEjZjL7YtlOtWZsGzrIUhh_44HBmeq1judDs1-7Qft_iBmM8CQt8pHh9FuLOvoqOYp5F3sBH-FOOvB8DEZxzoJUCYCe_lEHTokl7aluymQBO_iMiU_7BsxQgvgbVgWWoThsU3qvVb-g8whu4b7KzmEsv6GGGPslSqfRK4eItSOW_wNlcRN05FCU2HBQDrjPP2SpYfTBRxJGQSMW1JoUnHWX7fWWerOpVDew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24343" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24341">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYzVpFjnivj-kyQN0mGZhaQosk6uYPcB_HB-1c1kRNE4VRpGwZ8yOu1LUeuEXUUHswVoTvOe-IX6vY2Q8BiYvPpLJbPn5R4BGLTyOO2P39YKCJOyGGXdhBJw-i4CfULQJKZLycgC0-qMPMe1rkq3VJphAh0_kzVCcoE5LFCpd0IH3SIESoLyfmzbUT-cWIWIfr7k-koRJayNAfH4jjQOzmljVh6ejHMRtIVRcJZJh40L2yorz0gsc-5AiFizrTtHYO7U6rRbl1fHL6w4ATquOLfjEC7WVO6rboh1AnxB6HqnNRAp98quSUP57mwQSgBvbS_U4W6M30IRkyqvErXM4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛
از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/24341" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24340">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oRgMwEUxYBSFfVY402tvp7tUgdfyMI5qiMP_AzAIG3u8AO0w_YNdUOjgZLGM1q9CK13CUf43B32r_uT-wy3ws1-RgoXNLryuL8G-Iv68teXq_QmrbzIm5p3qvtPHSIWCmhriTOhFjqNANZsILFZMuN6vhsKXa8CNdKtiL-3FohlPXWg66hUpc3RBKpHhZuPWvLSHq-pgwnrE9gbZpmK9NRu6f-ujjuj4e1wW8cV_T660Qc-RO69sU-e21NbsUClQJsGaS1gi7Smn_yWM35BZ5jiMktto-6UfB_U4l2XhaYwt0zx_rXSU5llxEfs_LV1T1KaGArpwujnK3foNszvbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌ دیروز؛
از نمایش خوب شاگردان آنجلوتی بادرخشش‌وینی تا برد دراماتیک اکوادوری‌ها مقابل مانشافت و جواز حضور در مرحله حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24340" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24337">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24337" target="_blank">📅 01:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24336">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edRwBUnrb59i9Et7pXImwkNoY7bM3afO-n8hzWI9Uv5XFbcgrKU-s1NmmsPN0JiVFPDkQcphbP4uSch0XdwucdrsxzCUnjBvxU9YGiZRbQaEgL-gVKvgXej0GLhpB8DaGd-Tjb7wbAjbyBRrvdnGZjPu1O2wxtGvz4FKXoQIRQ3GTHgZyUq_wnY54-4qnciSDvutkPVGVmqDjt5cjGr1lxeVXOhD_55l_AQpsXayQGIRvun-BudGuZQ2NsMOyeyD8hKY7k0-ownrYDs2QGLTxnNq97GeoRJ09rpHnPsYlBPZ-qNsJBLQMRiLQZX5FFfSSD_aB4fXCekn-fpnnECwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24336" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/accJl6ZcLaApOqI1KQfxiN8ZX8ceqVCV3XtZOH3XggpEJnpkRVHOF3fFgGMOiIeUKUTb9k4RvAA66-cN9v_5l9TFW7Q_UvoQBkQetVm273aAu2rGU1nZoXr8Pwco3C7T-11c-iPUo_WIK7df_uiwNeXOLXEHIsqE40C4POvCqvy2OPSy4WP7r7YvjpTmf91fUteT6OU1O1SSuxdslzM6rNxZY7KfTnP0U8fT3yrjMgiN89_wl0uUT3EnDdaC0MQXjxyjLA0SyFjWxg9BxWozNdH27kVY0cWk5nZ-KqOPuKtYPBD2PX-skCmY1TE0HZgF1zI-myIeAyYhh-UdSeY_Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/24335" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24334">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=e07V_Lb70uwZU1ItgT5GUfgpLhW8rJEbVf5KM4UuwvrWjB0TNqVo4G26G_biKvJvFiLQpLJcbZamAE03X2JpS6vnQ5GEW-sicRRYlWNEaOpVSnswLoqyIUbrUqnU-4_CO8wHG3Hx3hdIjri0q_2S969CfL10CiICIBSzCg_11SIdgpbgbyrdNjVpsts0LMufPmHSJs1DUyucJTCmaYLQsqtX04wp8F68PaLUSuozUMAEOm4UlPMO_nT4FJX9ye5XEx20nlDwvG-lR4QKylAJjQ3BqvkjCIxdUaET6Uyu5SPRjijG_hncsl7nDdQJhVEd9Qe4LsAxlpRsJDcfcqhiPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=e07V_Lb70uwZU1ItgT5GUfgpLhW8rJEbVf5KM4UuwvrWjB0TNqVo4G26G_biKvJvFiLQpLJcbZamAE03X2JpS6vnQ5GEW-sicRRYlWNEaOpVSnswLoqyIUbrUqnU-4_CO8wHG3Hx3hdIjri0q_2S969CfL10CiICIBSzCg_11SIdgpbgbyrdNjVpsts0LMufPmHSJs1DUyucJTCmaYLQsqtX04wp8F68PaLUSuozUMAEOm4UlPMO_nT4FJX9ye5XEx20nlDwvG-lR4QKylAJjQ3BqvkjCIxdUaET6Uyu5SPRjijG_hncsl7nDdQJhVEd9Qe4LsAxlpRsJDcfcqhiPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هوادار تیم ملی عراق که تو صفحه‌اش گفته دوتا از بازیکنان جوان اسپانیا بهش‌پیشنهاد رابطه داده‌اند‌. اسمشون رو نگفته ولی گفته جفتشون تو بارساست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/24334" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24333">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3KX-c_0WBLbYOIaXQcU-6YtoIP2N-2A_TO-14EUa-y2xk7-G9nMX-g002krofuL0wctCyq8UNB3Ig3U7cu4xkblSmrKrHOzh6Xa20HUMo89le4VzAGOPzOdp4BStyZ4LjzbuzEL7c5yYscZcNPUvud1Xotou-uj9xkxEsTpKfH-7wSAqr9qxIA9wUsSU0DnCpw9Z2CTEuKaTfRVjLnPEZww3fWOleEKwzDFJ_qGwEvkXDKkE4ueZ465cD3eAobgZwCcI5dVQz-hwhKsbdQDS_rwD8iZuOOoP6nzRpyOu_A2S66H2ZJ0pbRlRFtz8dSvLPDmDJhYsWDsk-UzEgz_AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
میخوای از مسابقات جام جهانی پول دربیاری
؟
✅
کانال
ورسوس بت
کارش تحلیل و پیش بینی مسابقات جام جهانی به صورت حرفه ای
🍑
⚠️
توم‌میتونی‌از پیش‌بینی جام جهانی خیلی راحت پول دربیاری فقط کافیه با کانال ورسوس بت همراه شی
📣
🌐
ادرس عضویت کانالشون4:
👇
🔪
https://t.me/+vEPd1hF2Y38yMWI0
🔪
https://t.me/+vEPd1hF2Y38yMWI0</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/24333" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFWG9fqbF9H03lsb-UoCOpW-CfkuBOt_-spxv4kyJYPAVh6U7sunwmWtPkcv_ddeyJudgqlE8qIS5KiHO_ZSUooS4dbzGsOGL9IHW5Lf2QnRcw5U3J7ZsB5gT_CrMraJMklDqesh9DkN9KisZoSjcr8JqA90ZJhl3LG11k2zGUNPhnjGd_X8CGxuduCiyRLbrVEYQ1J4a1Hz3UHyd_S5MRstCtaSr0fA0dkOdrr2gvkBFnz0jNq3UIgF_kl6WnIYP-HrDbwx5AHsd3xhmByv7mOzn-AImhG4-Ity9a184Omqrq3Edv06S0WSXsgGK90qDW71-uG1d_WErnVA3wnXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/persiana_Soccer/24332" target="_blank">📅 00:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6CBuK3cK43lwvm_qbdkxEbF0sbg-GrixjlC1nAGA8zdxEqSh9XRHz1c1CMxacrGyQfEJd9seMMnHUb6A2jaeAH4-WKrGFXSMZOWFJEhwOVOto9-XR1oK9uUCl7TuewAg5cJovZ4lY5XuY7XF8sXLRSJFQlIV8qhealf9gSBy1T8ZaWZMuQpYXuwiY7KCm9nEEb0tiqXrCWdyj2vXPsDEJNJOd-BSiKGVN3cpdCG8VluQsalQApBE0a5syFpC0eMCLBMuXtEiVEJd7T1VvFDj5VGgOj7cAUCw_qQsfVa8t5J136JiKnhVNOusrgVIWrkrS7ClorsxKdfVturmqEJbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24331" target="_blank">📅 00:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24330">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU4gfAY_0Iaa5O-jKCQQf07rKXiY0PBtO06p3Y4JOOyWP4AW__I8XG8cWCOK58_O1Rm-Wqm7QmWhc9PerUn-8A2ms4XJgxfIiwnXm_e_MY660Of1psmXmgi9e-H6zpHMpbTzC2uTVupQHPXpsnoz53doQVwqrr3kIsCS5qbpPykcv5PgAx57FfTGXHcY_d75qTYzWLoSFjIUtA_TpeMhFp6T6n5VSt2DvuMa6l_kXKB9GFtncNoKGYAnUO3s8XHnLbYtGluDT7MeDg5VyJa-8FY9HrHIa39SnWSci8M_uREHfLmwUCykRd0Ni3PWj6oHH0bg_seTCXcfZ4a6gvKW7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/24330" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24329">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL2ni4C0e9p-inf_x5YogIlGHgOeLymVQaXCwAGa4bQAUnylhpUcLqSY6h0_Mk5Yv-q_7adJ9tkWMKTjCYUcq1AYUj7-QP5CPDY71uh5bb8f1eiPwQ0PPZtp6MVIRUfU0DnVRBkVtmS4SFV4F75grmcReqzVOIEbF1DMmcp-YKKHVqfPDorlnb_jEj9uTleUFACd_f9tV68H3x7DCyHUDDRI1qe1c3-8XQ03xWL8ndQDvDYP2xfRnIztpc_7Zc4nTxuczTtl6m5TxMwofnyMcbS0IU9EZh_RbC0JmUv70Y48ONtYA4P1HRTi5z83eDzM3Nssl4fTXGyvNVg7V0m2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط ۱۲ تیم‌از ۴۸ تیم‌حاضر درجام جهانی بازیکن سیاهپوست‌توترکیبشون‌ندارند‌.حضور فرانسه بعنوان تیم اروپایی با ۲۰ بازیکن سیاهپوست از نکات جالبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/24329" target="_blank">📅 00:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24327">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=ZppTNQWpU_rrDNzfDGpEU0w5P41zFx5TljhzWPKLo57vp6LLPWhO7bEreDYzNIWruqFNvwxD6jzYBJjUGPmkMkvXUEY-8VKgEk_37dVlBoihNQDRcQ4Y5t98hvCQ48zgJutpyXlQWgGL7qepgNw0AmrlHVNiJj9d66usy4g90qcN_Y42H74Z6SPZL7x5_Uk9QE5JYYt3pF1Gyhbjqa3iqU_bIvnxOHnUE-3djvNVVgywTR_1XRT7C4TuNECTV9t4HNLWvVUByzbtuTd98Eapla0YL-3m--2IjQL96fk4oldw7M0udXHr5lQzKTOzufz4fUIENQ5Vt4GRIdVeisF0bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=ZppTNQWpU_rrDNzfDGpEU0w5P41zFx5TljhzWPKLo57vp6LLPWhO7bEreDYzNIWruqFNvwxD6jzYBJjUGPmkMkvXUEY-8VKgEk_37dVlBoihNQDRcQ4Y5t98hvCQ48zgJutpyXlQWgGL7qepgNw0AmrlHVNiJj9d66usy4g90qcN_Y42H74Z6SPZL7x5_Uk9QE5JYYt3pF1Gyhbjqa3iqU_bIvnxOHnUE-3djvNVVgywTR_1XRT7C4TuNECTV9t4HNLWvVUByzbtuTd98Eapla0YL-3m--2IjQL96fk4oldw7M0udXHr5lQzKTOzufz4fUIENQ5Vt4GRIdVeisF0bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/24327" target="_blank">📅 23:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24326">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO1IJxixU2pCstl14X75VHdUifvGLz4lMPJVc2c8hItBHCJs-Xrrc430s1vVd-ecTbCc-0f1-jEW267G92ucypEGO4P77tm3Nm1mkkN3hOvIFg3Lz1tdySMSEGm5uTvpQgLgjmDAOzPT2Wthg1SNy8wiBlCO_WUMsZh5BDRzxATKKfN8bW1ry4k3XGBIjxdzS7AEwny_Z2fH_OPWom9u2Bej92L8_dCNPG5QEZ7269AepESThiKtYmfP1VXN2jgJPYP6vMBlQKQKtHJbwoC23lb_ikY3ObEdanyiMVAY-v2HxUfmSZPEWWfIvFalAbv59hIZriHmb9uRY0GWMTiDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24326" target="_blank">📅 23:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24325">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR0WiekFz4jdqsXUCt3VDZk3E0FQj5nniBN3fsMqdm1oUiHci3KOw9v7qZrf5cbRzzjAaopvPSQ_vpjuBVjfEl-RzEWYNCfJSoSldtXnRYPY9tta4atlalcRA9kr2JY_UKsNZaaprCUhEtK0t0-ol1F2lsP8SHhV5IUPcNSCVthPQJylEY_WpRRzAVL621TdvK47r6pVGOlITvpn6WlUHdG4wU9uRQ8oW_5Wdf0YrWasbMW45wwX7mPmxCTvkfbeb51c3PVv1-ChicwMHik_CsUmdqD7RWa8C0LNH9mnhODurEk8J0hPcITSndhxe-W-2X7QHpFqiACld0vF8HKfhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دوست‌دختر ژائو نوس ستاره تیم ملی پرتغال هم امشب از نزدیکی شاهد درخشش CR7 بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24325" target="_blank">📅 23:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24324">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
🇧🇷
خوشحالی‌منشوری و برگ‌ریزن هواداران تیم ملی برزیل حین گلزنی وینیسیوس در بازی دیشب.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24324" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24323">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8l2ySwHLQk4diIzrQCq_dLoeBnaScaVGbXTWKMLVR_GqXayBmqYYDUfI4Y5YlbVm1soLjqvCU1s53drO7niunwf8-0IDpSHViVPtooISvTOs-Xb6YzVvjfc6t3Itt-sGuS_a7n08uMqNNr54Kxe4ruSNRXXQuutbSXyl5neUMeQDUUE1lePXaRixDZ6BUTRDrD05Fwo4kWILcuH6hm1hrbxmPmPlcrvSAvhxJQG0pujZ-1HosU78bMqR_ZDTdbUBIoULrI0ihDNKo30hhWq_YHYgc60QxmgHwsZWbp4aowQ7TA4inv8Asmbkbwr4ExbIJtUkSnzXf0wMnNOD5bw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/24323" target="_blank">📅 23:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24322">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-kuFEOxe7QQl2ZOlm2XnJlGd7jAPiLMP_6EKX6QjBT1sZAgCQoVFk9UyXaprrskVHnd-1GEPNQhWFeFXjLP3iLR519LKGnat5NDdGR7jaMpIsT5UWVh-RLcw52Q0Brp1oCQbU0HAACCW2pmUHl68lDZOWG_94rttqYP9q5tzLvWCPnr-7SDbzShpONFAUVD9y-cFiPLR_Q_dK12fqL_DXqMyzW2cKZwtnH-QWSgsCAfefaAnzToMLSEA7edRyuNGmDsRpGVyFdkU1V996CnIcAdiXj1_vc5L5JBy8zti0clQ4J4J0DifqcqaVsh9Xw4XuZQLCfC8otgjq6MCBkucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو: باشگاه رئال مادرید بند باز خرید یازده میلیون یورویی نیکو پاز رو فعال کرده و این بازیکن رسما به باشگاه رئال مادرید برگشته. حالا فلورنتینو پرز میخواد این بازیکن رو با رقمی بین 60 الی 80 میلیون یورو به تیم‌های انگلیسی بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/24322" target="_blank">📅 23:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24321">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=M6C2qDtfM5yXXMApyzR3TPnMV9BcXBLSl7SCedYsecwPRUEDnUrWq_y16RwBusW3JMPyxlNfkDoLEuj6GUVdQjS7TwOzb2WZUup_0VxT8TUthDNAHrCvseLsXLkD-fIVSsNgYRfoScnj6ml8mJqbKOLPgoqP2zuw2k8Bdpzn4pfhJ8jvW_kVB6cOYC94um8l0VRrGO-nvBXMbQ5Pd8yMqkFfsGM2mGnF9Z3C_CeMUnYWx7EzHyHek80lwGswWOx5-omzOF5APkDR3fEgNSs3vKBBCdrJVfuchDa7XWwc4XPypwxoxp7QnuowJO0dpf5gCIWXjZKpleqO267-Zjs9xKgfC4ViHmD4R3CjxtbkSmXjJzoDOvsQvpc0d-eu8GyKQMLGzpodlx_FZ_Y3L0JMAHn3sLrCo2f-r9oRHMyuBsn0sELSyQvHh5-GhznuRNyMFCtL_i8KSA9Nkzc8GqdumibJy0TVB0qQt8T1qOZFG5rgrHPYlNwAQWZd0Df6Wget2gJCz2r5c1ixJXFxLZxwHc4N7fQGFXh6Ohuq9pnFRIBSebwfRposunbE9Iy8UobtGekOmrpvo8wqblupk7t89fBTu4pk_pwmaa1fbMyi5dBzZFP_trX8tBG_OWq0YmCpUTOwSam-xgUJf7AYkQWnjqfNg3WKZDtSew8aGRuAB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=M6C2qDtfM5yXXMApyzR3TPnMV9BcXBLSl7SCedYsecwPRUEDnUrWq_y16RwBusW3JMPyxlNfkDoLEuj6GUVdQjS7TwOzb2WZUup_0VxT8TUthDNAHrCvseLsXLkD-fIVSsNgYRfoScnj6ml8mJqbKOLPgoqP2zuw2k8Bdpzn4pfhJ8jvW_kVB6cOYC94um8l0VRrGO-nvBXMbQ5Pd8yMqkFfsGM2mGnF9Z3C_CeMUnYWx7EzHyHek80lwGswWOx5-omzOF5APkDR3fEgNSs3vKBBCdrJVfuchDa7XWwc4XPypwxoxp7QnuowJO0dpf5gCIWXjZKpleqO267-Zjs9xKgfC4ViHmD4R3CjxtbkSmXjJzoDOvsQvpc0d-eu8GyKQMLGzpodlx_FZ_Y3L0JMAHn3sLrCo2f-r9oRHMyuBsn0sELSyQvHh5-GhznuRNyMFCtL_i8KSA9Nkzc8GqdumibJy0TVB0qQt8T1qOZFG5rgrHPYlNwAQWZd0Df6Wget2gJCz2r5c1ixJXFxLZxwHc4N7fQGFXh6Ohuq9pnFRIBSebwfRposunbE9Iy8UobtGekOmrpvo8wqblupk7t89fBTu4pk_pwmaa1fbMyi5dBzZFP_trX8tBG_OWq0YmCpUTOwSam-xgUJf7AYkQWnjqfNg3WKZDtSew8aGRuAB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مرتضی‌تبریزی‌مهاجم‌سابق‌استقلال
: گُل نمیزدم چون یک‌گلر مشهور برایم طلسم و جادو گرفته بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24321" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24320">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=S8Bgck5tQQ8rN0UyJouQ_stP6H0aUx9bSZ6Rw10xREmuK6ZjZ-mx28U-3OZs8KgTmIPxpPwVwpRE1cyUFeju7vaca6jMezteycl9hovK7oEbFKqFOLgW-V2HlslyKbw8WxPqu-XVhSVSKhHwQ5Go7qAqexacjYLZDsuo1siNGYvAWkDc8NShccbuh_Tf-kQ-KbbW6ecXd572II44hKtyjip8H6e9Vu9W4TAlZ9JrRGWVIBJ5QVtURIt91fxW_wP0mnT9WqXV5EuQULfwkSSfH91ZeryKN86MJeQJEXcqJWMIoXpyvQ8gsw3GoE9aRa9hIPpgKijG_2zLOYCMON0gEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=S8Bgck5tQQ8rN0UyJouQ_stP6H0aUx9bSZ6Rw10xREmuK6ZjZ-mx28U-3OZs8KgTmIPxpPwVwpRE1cyUFeju7vaca6jMezteycl9hovK7oEbFKqFOLgW-V2HlslyKbw8WxPqu-XVhSVSKhHwQ5Go7qAqexacjYLZDsuo1siNGYvAWkDc8NShccbuh_Tf-kQ-KbbW6ecXd572II44hKtyjip8H6e9Vu9W4TAlZ9JrRGWVIBJ5QVtURIt91fxW_wP0mnT9WqXV5EuQULfwkSSfH91ZeryKN86MJeQJEXcqJWMIoXpyvQ8gsw3GoE9aRa9hIPpgKijG_2zLOYCMON0gEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
صحبت‌های‌نیمارجونیور ستاره‌برزیلی‌سابق بارسا درباره لئو مسی فوق ستاره آرژانتین در روز تولدش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/24320" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24319">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPXqPtarPI_5FQaXJb_NbNp_ZYDvMzJogUh5GVmCHMhyw9_sZt3qSU0A_Ywity9aOeCPSPhvAfuYNX4ry6mPkPK_x05MsYZ7GVRBCvWV6ZJ65hh5oNl2Xii8Bb6dlWittZMEvSVVhd8pUHs56a_no1gfgDMybz8tZ4umEEdMVdelu9ja9I7OAVYfylWmoi9szqKOehtbUkWwtM-AtIkV6I3DrW_qU06aow18lOnjOn_8BGeMeikkm5s2TQjwJwojNSDR1I2Lbv6X6DBk4ZVo1DTJpi5i8AJHbEeR5jS3m7ulTfSOmnKIYLSjk-tjHAVHXrJQNTUt7eDnZJp6aL4Dew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/24319" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24318">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNLaXijyoNSyoEfmSp9XwBjWnkDzRVJVb13BBYX0hg5P8rnAE9tUiuE9ktT39AGBv1GuobbW85UH7gjZXy75nZE9lb7NLKJl61FtKreEtKwy_z6yD-Q4DTZtZ-rnSQXWeq3IAQnxymYgr2jYc2q46uOT9K5MoEIuphqspK28FmEMRfDgFhh0RZPSngN-cQbFd5NlWv6r_g8c966ZjUT3h4wrCXM4CNdQ11mL56lFAcyCe1dUdQghCUSnCVSLvPMaq3bR4P5lZonTRWa0D_Rv2CpMH4FfSckuWB1IMDkuz5YHk7szNSC4DITmcdbjBu7UZHzaHCyYoRtOEOq1Yei3Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24318" target="_blank">📅 22:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24317">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETK_WQIaaZmGaC-YHMvsYf7IJuWrMMQ0NONcwynL3Swb-ZMkU6MThYHJcgn6eh-DUx126bw4f95ftsRKFDAFFodAxC_k9MQRyB7oXD2SIz3J9EEvRNtaJVr0EP-S17BhY5QPwXSc2ZJgwBLByoSS7HjIENIpBuPtVtDkLcNSWFeoBLtF8bcmHt0FoJ3A07Phofu0i-NqSwa10eaQb8kmNq-TFtj5otU2EePRVbRArC3xbQllacy-g8e0DrOihptJosVm_Kv3g-bmUYgcvL-s2-u3QoNHLYivr-hr6q27lOqW2so9v5lbLg_yixn7M53BGwZnkcJYryNa87xYF6DYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24317" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24316">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=VhcSIeJO1ubB3Ih5axSRl9725rJ2Nks7kQqQmEi1lYyrAV02AUWgF2eM3bhY5rxmyw1pQaajLxg7bC9TfYcvaoNOO7NESQYBdz9PfgkWhsBtCqbxWd4cBJzadTt3ECI8-wXrqVwDWzZaFSfCBxDOeys1qCUTjvkhb3IDGfDyVCCqsX6Rc70nssoQviqACLazxvwZaWcuAccRiVjOfqDgMyDgiK5I1YoKVg101uVc0RqHyW8-XLieHWl_lfkYNNUaOtbzqyGrbAixMgN1TYptUZt3QcsYzDT2r54SV4egXyQb0DRgMUdOZI--PsVYCvbvWAkoLxJghO-Zb8TZXs-cGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=VhcSIeJO1ubB3Ih5axSRl9725rJ2Nks7kQqQmEi1lYyrAV02AUWgF2eM3bhY5rxmyw1pQaajLxg7bC9TfYcvaoNOO7NESQYBdz9PfgkWhsBtCqbxWd4cBJzadTt3ECI8-wXrqVwDWzZaFSfCBxDOeys1qCUTjvkhb3IDGfDyVCCqsX6Rc70nssoQviqACLazxvwZaWcuAccRiVjOfqDgMyDgiK5I1YoKVg101uVc0RqHyW8-XLieHWl_lfkYNNUaOtbzqyGrbAixMgN1TYptUZt3QcsYzDT2r54SV4egXyQb0DRgMUdOZI--PsVYCvbvWAkoLxJghO-Zb8TZXs-cGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌مرتضی‌تبریزی‌از زمان حضور فیروزکریمی در ذوب آهن: 3 روز مونده‌بود به پایان لیگ گفت تیم از نظرفنی‌اوکیه مارو برد ویلا یکی‌از دوستاش تو کرج باباکرم میذاشت کباب‌بازی‌میکردیم عشق‌وحال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/24316" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24315">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHXj5ya29cGNDp9nQrLlb6jmrfrYYYLu2fbWI5pGaljOLAWmcm0iE7S1aHVKtfltpIWA3cH-TiIH0fLCrrNuQJnFQvLbcCTrDhahXuizB1ZYkHuaJAo18wTjnNXGTvGsbLiYKFYY2jTzmXYWAbFXvsS3zdPam3xVZkW7HXjpBKiDRMi_N_6k0ZcWD2WKst3htdlowfx7sFy40fiqYMZ2KERV2Cj8aU4u6lbV6EUrKoBBIea71tT4KbkgTwHqc4Hzv9FK1BIwT0Tjl9vK9KQ4QVBKuKDaP28zMNV5cfBH0VTx1eS42etGnyNja6_Eo0mM0nTnO_W5zkf_yeUkcpeiQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24315" target="_blank">📅 22:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24314">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpVWLebVihNR9K77JY_av4-wRuQTTo7KAx91bZIt5lHt8dY5J9z7Sq2l-kcwxvQDb4DeYjyW6GvVtWjuteJHBIOdxBx4HimkNKGmPeCcb-16I-tDfRQQYjOYpWuF_tYzf4_sI8ijxBwlUTEBv-7Xqixpo3kSOhQKZiK2Hmktwx52_CAU5oZG_cmja4aML8aMUSJM7jJhcR1QsFFmBBbGSsQz11RKm3X3MP6K9_a8VcutlZtgJPo9j7PXS1PPcBFaFtMQkkwK1Krfkmi9gnoqsUlFM4HmQANMTwSmof3W6dFN4iXfi75zjf6G9aMXNSxNzqwr5T0CaP3kCQJOdEl8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
عملکرد خیره کننده اشرف حکیمی و وینیسیوس جونیور دو ستاره مراکش و برزیل در تمام دوران حرفه‌ایشون؛ رئال مادرید چقدر مفت حکیمی رو در اوج جوانی از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/24314" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24313">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvsnMv3vt4V0sOVR4Nr9raHMAU6qWv34dzBclTt68sX_Jbz70vwnsKJVXY9nDN8NTwuUV0Lu32kHeZaCIplUyC5z0rhnI4bItKEEUgc9r_3mkSFW5SJyp15SNgfn2t1I2UQ_F0BhiB0pvR5tpJn5ezoeyruCJS_FEEh0Dwo9QH-ap7OCttptwtL3416KBse2iKGxN4ia_3nWsQRnq6VxvQfT6h_5ZgFWc4gVK7r06zTyqeaq3UbCtzkGrBOrWmioISdbl3_MVJbik6ZAB0pUPRBRAR-2xsWrX1xzwkzBJCEgIWfjWD_DUdSkIzELeoRTYueP44VPK8jUO05UPCnUvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/24313" target="_blank">📅 21:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24312">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpi2wj3hQy4a1-8bHosTb0WESfuAt7ttdpNTjiSP2hdNxVO1KJrweoZdFESvvjmfIPAuZpHD4CYC6tHd4CusaOZQt2nlxlYAOtLarqF7QVhFfiAX_7jNXGJilHOSmorNNzDxoO_Hi1A7QMxpY7sR7uE1eHG8Irpm8YNlNOMqnCrAX-R_5qqmRr3s6fzELqBhtB33Ee7YD0srkr163igbVobehCqYGauagTdHhKlB8jdeMJlMrieO9bALnKdN0sA6X6-J_ZAzSRhSf3iG7JF44fIwZa2B6NWWYkNTC91GZCJD2sIPsJwL-ZyMlRPu5qVOriBiSLEcJsTC9giWoyh6Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24312" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24310">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RmyOoFANsiTVZjgBInoOoMGwUtF-6lxQW8_HORejoxJ2aoHpIuDKHj9Q_ZZxk3GJSX2c8RladVyvmAjBrcUyiLRTY6x3ZmOc3A7zGpqSh5qYorubvQR1xl2kkMpFXHAzKgqC8_qVc_AB6ccMgtRxVb1Zz43xcPMBpLOW5Nj5Q0N_Er2VVhIuM_LJMx81ojV5RKm0AbM8B71QuKW_a0SY8O3fQYg-Uu_ol7oA2ArKq-LbGwTZjr05GqsMJa26o80QRLr0o3aDwvxv6fCxxLgnDPfrpHNQqVdfUCgVjkyKbrHAwV_dUyVKGppOGidMtlEmNrZ0HI_8dsx8_LbEMHO9RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AET_kiXQx0WNOyqJWAd_5GVVWc8R9atSbGwM4slDFG-TVmk9Hz-KhDO4qMdg2neRYGrIYR-YHGFi29sfaVWNdsSyI10zege8hsMaC4UwlGdfi8f5HxUsatKT_iajIT70IgFTPKVQamrHCC6KqiR_5hc0G_dpCEJSWcwNqcPgkZkEjh1K2SjtwxTovEiRXtM0_yTN3TnXRgPAnwAD-s4xs8rXpPBqUq2sqb-29sWd7BTLyZuyKPcY8iu9wJQi7736fa7RTEAmV1ZpH6Ii89WXOB-GQA5G_MnBaNZ55KajBiWus8Pa-BBkNtH1zNH9Nh-olg9yrLPMablQQpVxutHNEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
🇧🇷
#تکمیلی؛ بازیکنیکه‌فقط برای کشورش خوب باشه ولی‌برای‌باشگاهش نه رو دیده بودیم. بازیکنی‌که فقط برای باشگاهش‌خوب باشه ولی برای کشورش نه رو هم‌دیده‌بودیم. ولی بازیکنی که فقط برای یه مربی خوب بوده باشه و زیر دست بقیه زاییده باشه ندیده بودیم که وینیسیوس جونیور…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24310" target="_blank">📅 21:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24309">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKZPDgLlZVgfb_PbUJu-DqOURd43zzDohtUOK_tXj0EUKyWGDDVJumYm5FKImw_Pe-HKdbPbU0NvxtLUtdakfzwVNb0kSZ41MYE8vGEeaIaz31n9jA6jMBTjwCpM2L48mB8obGtnzl-eokGwO3YNQtVxZF-46zlFYMXuM4abCUqv5yFEgTXY4G33WPaNNXA8DzdDrrXdJkrzLFfHfvoVD22A7ZLeHbP6y9xdvCyeX-Vcy_B3s9wXjYv1Hk8nWih7RtXB81Z7019XZGT1Nj-7jXZbiz7_CaxHBSu8sKgldlH1RSd5zRlS0uORwaQAZ9_b3Ibwaej0uWedDNLGS0pKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کواکو بونسام جادوگرغنایی: حالاهری‌کین کاملا آزاده که گل بزنه، من اصلا دشمن هری کین نیستم، خودم بزودی بچه‌دارمیشم و اسمشو کین میزارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24309" target="_blank">📅 20:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24308">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UI8MD9rEnQ_cv6QVTFA38_wfZQ-F8yYQXTa8E_8Ip7PzqT6MEjrfjcNOD7pFE1TU4S6yCAkCpTpZIwqhLu0SmAEAy7iZLS3H_Y-ez4Bfx1kL-4hNmjkaHfOh87n93zcgWw09Ft8dahXTzaTnL5Z6aCYOZ509r_KkEGw2B8KnMow3wQcguvdiijgS956F7DN6QSXvcbDx0NnUudq4vwB1TeuOWy67qsiPiBNIbp8aHOWAUi3dOorj5swnKTUJTsyKY8V0yhrNYnw6fwxbRTzIOSWkewUKDZYj5l8rZKLwaj_XobfuE7emF00cxwcPH2Wv1jkrar6SaQtxKItEJ44ppg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24308" target="_blank">📅 20:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24307">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n78irchaIkxL6clWkpPeO76zC2-fAHDlAq8ejpbgHuvBXg0BYPaL69dshjvyEQ8iD7pAPQiy5wKjZEEm7wTo-3QJZOW7xw1R6PYBFJR3DrzQLBfAVZdyCKIU2WLTNsbJlT42ftHAEcB0ScEw6ppe8bkuEOqPl2QYcsF9rdJUfN184hrDB24HBCu3HSm7PtxA-G7hviPGu1b27DiK9kaBhWNG7YiOICrRGMWTs48jhXQeiOCzW4O03jXzaMXR_bp8rYM94J_vK7JdIcckpGPyYaAeM5s5R20FBPcdqM9TtG2vtJiX4Qlg7ldKK82_lz6ZN8rar_hgM-1OxxhzXTJtVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
عملکردخیره‌کننده وینیسیوس‌جونیور در مرحله گروهی‌جام‌جهانی2026: سه بازی سه جایزه بهترین بازیکن‌زمین؛ بازی اول یه گل زد و مانع باخت تیمش شد. بازی دوم یه گل و یه پاس گل داد و سه امتیاز رو برای تیمش گرفت. بازی آخر هم دبل کرد و تیم روصدرنشین گروهش کرد و برد مرحله…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24307" target="_blank">📅 20:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24306">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=nKAp3VJ4_SQV7YBGFuen6ocw0VUhUQawJsowb0BHgKuGfi71YKG2ugu7k6rrQvTf5kLyEx3y391V9Zt7L5Y3UqVRILvXz_VT4HYRTSDja9xiY-ejz9X7CbpXPNmvBAGqsFrfl-qnn_LOk4n8qz7m5oK8Y9TJ6IJHub2_a4s_oMFtvckW9OA1KRPMnu5y2DOifQ8Br8mhOsidQnYiuI7rFIKTmBs_81sbFaMrHrCtz4LWFI2VHK3nohPydyAiLSFKemRQWhKIm09BM1wFMJJipi3tAmeEF6lrwzAkn_Os42GaWTxxCQKkyLT-GXRGKT14qGFpXb7k-rAJBX8-MBiu9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=nKAp3VJ4_SQV7YBGFuen6ocw0VUhUQawJsowb0BHgKuGfi71YKG2ugu7k6rrQvTf5kLyEx3y391V9Zt7L5Y3UqVRILvXz_VT4HYRTSDja9xiY-ejz9X7CbpXPNmvBAGqsFrfl-qnn_LOk4n8qz7m5oK8Y9TJ6IJHub2_a4s_oMFtvckW9OA1KRPMnu5y2DOifQ8Br8mhOsidQnYiuI7rFIKTmBs_81sbFaMrHrCtz4LWFI2VHK3nohPydyAiLSFKemRQWhKIm09BM1wFMJJipi3tAmeEF6lrwzAkn_Os42GaWTxxCQKkyLT-GXRGKT14qGFpXb7k-rAJBX8-MBiu9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
از زیبایی‌های فوتبال و جام‌جهانی 2026
؛ وقتی میگیم‌فوتبال‌فراتر از یه ورزشه دقیقا منظورمون اینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24306" target="_blank">📅 20:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24305">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-JPJeCOQYXk-mUl6a3AIRIqZNDqH4Nl5BgshT8V1uUxXrCEM-YiQUJKf2wB0QGbeN-K8Smp92MuQEZdzBCyWGx4YGHKEpXmUUnGTkCdxoYTNTyZ24fqoWUvsrmwA2pD2u_HUsFMsr7lkhXTwqxfW6lBPS0Iomy_j-sAX-YGuMpRhFEhUEbo-_Cw2Eag9uIIBBt0faWUThpFh7XFD7ijAfpH3CtD64TWsrUAcDBkA79tLw8kubze7FDDiJwrK2NI0euouJ9zXtTjDaUYMlgQ9fsGc745rJQlk153y2EmzS0GHN4RySb9MG_n7ShLezQaaB1Bsyc1Sor9rglO8aej6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کازویوشی میورا 58 ساله میخواد رکوردشکنی خود را تاچهل‌ویکمین‌فصلش با فوکوشیما ادامه بده و بار دیگر بازنشستگی‌اش را به تعویق بیندازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24305" target="_blank">📅 19:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24304">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtIONLK4QF_V2mO9ro4gqmsSsajAWt_3-u1Sr7ZhOhbOQHZizcsnIfrJ-jXIEa7--zJm5-fldIlFxfnTqhTbDvAf4oJEUgeewxqCUHULODvnJs2DHg8Y9p1Ipl6Y3D7HL33kyMuoojsyHUeBeLyWp9E_FbTlxP3BSgLaVhvg0n_tj_UYKlfGvnSowf9vxfRJE-qULILjAvSOAWscsRBrDZ9vhlqZ9FS1g3RBrGuJ4RryS1MhDlBC2Xm6c848lJ-zRUb14llE_f29HGXvbuB72VmV74nJG_rKjNc-xqWg71yitUfdMQ7SmmzTko1ase6THq9Rlh2nO-x2paoj0clLGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رونمایی‌دقیق‌از رقم‌قرارداد عجیب محمد دانشگر 33 ساله‌باشگاه‌تراکتور تبریز: فصل اول رقم پایه قرارداد 85 میلیارد تومان توافق شده‌‌. فصل دوم رقم پایه قرارداد 105 میلیارد تومان توافق شده. همین هفته میره دفترمحمدرضازنوزی رسمی میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24304" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24303">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBNw2gbBa6C-EPgtWczg6q8iPoRNiUDEBRouFUMkrufCF6TqDVOkFSu6QtqxBSP_M4Omf7wxYYZa-WyU-zqIdVpiH5_6jEFHDnAZ_JrfKXa01AI6a16RpYkfC-bA3p1elQarX4teLL5P9QACZ-9jUVH-iod14gMqVBlnIqSM7MprPlxPcaUChJWaHVRjXr4kf4jAJ3OIrjqcbERQqvZ_gVAnJurD6RMt042SMQf_0bty5bx5ZPXB52jIzTChll_nnSwure7aIKN-P9mEqhqMyeMTRwMGXFnSQdHwN86iFnCm4cydShwY01VzAu-JJyd4uHfo73C49vHarWbITPpXRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇹🇷
🇨🇲
#نقل‌انتقالات|بااتمام قرارداد قرضی‌اش با باشگاه ترابزون‌اسپور؛ آندره اونانا گلر کامرونی تیم منچستر یونایتد رسما به جمع شیاطین سرخ برگشت تا مایکل کریک نظر نهایی خود را در این باره بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24303" target="_blank">📅 19:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24302">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Es6vuOfYEmYQ7a1y5nvXaS7uCT4peL4RoITJtRMFgcZPOEMSq31r2T55qh_521ThpXOZ35xKoox67y4wKbuMRiNk-Cv4k0C6iP3A0ZbIoqA_a0t2i_kFvn0byZG_KMlANs9s_65c2VI-4Lc8fHLbItXCCeREySyzsVUUvVpEUlPkYg3RUJCNgMBvxDLgzLKIR1B5bPCvfS7_BFNdE42Bnjj7I6KiPZDUY7pXcYgvSd3TGDFOSUy_D0--YzKqfZ9ppVnOr0iV1gGNdFUIvcPy4vZF5iavgnA-6K6YGpACb1fQzkn9GDKFcw4XmvIQdHoFme-dsaIhA9Lm6IVriTdX2EcyytZJBSxgmqzktcdryIkH86LaOtdFcVno4NdiuQstedCUOnykiyRlkXJbb7nHECK3GaWMg9Gp8ZePyY9UaHbBmhPLtm78IbgiFBpiRJ5lO3Hp7fEpwgTJ0OmmWN8Q11O0quItxXWuJnCRV_NlVRaNz9prJXrdsxMWAMLE5BDwIsMR00_QnulqZwWAK1WKlXoCTWdH2ZWe7bPOeSiHu3jcI2Rs8nsgagupuJg3kjfEd06ytNXeJ1PnuUc49MHeIAPtZ4-CpJFzeNgeUBvUPtcWX7j09olZ8xtJw_C14iteO0lEkzb_cbGbnezeIJAH5np5lBNBr31fa9OeH4CXdo8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=Es6vuOfYEmYQ7a1y5nvXaS7uCT4peL4RoITJtRMFgcZPOEMSq31r2T55qh_521ThpXOZ35xKoox67y4wKbuMRiNk-Cv4k0C6iP3A0ZbIoqA_a0t2i_kFvn0byZG_KMlANs9s_65c2VI-4Lc8fHLbItXCCeREySyzsVUUvVpEUlPkYg3RUJCNgMBvxDLgzLKIR1B5bPCvfS7_BFNdE42Bnjj7I6KiPZDUY7pXcYgvSd3TGDFOSUy_D0--YzKqfZ9ppVnOr0iV1gGNdFUIvcPy4vZF5iavgnA-6K6YGpACb1fQzkn9GDKFcw4XmvIQdHoFme-dsaIhA9Lm6IVriTdX2EcyytZJBSxgmqzktcdryIkH86LaOtdFcVno4NdiuQstedCUOnykiyRlkXJbb7nHECK3GaWMg9Gp8ZePyY9UaHbBmhPLtm78IbgiFBpiRJ5lO3Hp7fEpwgTJ0OmmWN8Q11O0quItxXWuJnCRV_NlVRaNz9prJXrdsxMWAMLE5BDwIsMR00_QnulqZwWAK1WKlXoCTWdH2ZWe7bPOeSiHu3jcI2Rs8nsgagupuJg3kjfEd06ytNXeJ1PnuUc49MHeIAPtZ4-CpJFzeNgeUBvUPtcWX7j09olZ8xtJw_C14iteO0lEkzb_cbGbnezeIJAH5np5lBNBr31fa9OeH4CXdo8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24302" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24301">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utLlnLsez9Tae6gouCC6wADZT_ADoq5jdtn2wkIE4TNLkm53qNytDcsYRhL5ay-xAmbOYlX-mYC-HEiLuBQeR2LpeQXJ7rJMbKJGEW7Q99O_dDPjEcW8uSUkFz8ZIQS_h_t7L5F2j24djDYoNW62hJMM9syOOS_qklx3acDKKZbbhuQKU6nemrgthg3v8MAAHKaY3AXeKPKHoB8gmVW0-hQ19uxJhmztmPZPRM8KYQjt_rNqHuI96LEAtyaixih0AQg4DyARF9dcj2VggxrtZqCl6SnoD_sf2WVgn4dz7Q5-SuL90yK5nRdye5gnLP4lzg6xfJ7uIkXLXTBra8LZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
اگه پرتغال درهفته سوم کلمبیا رو ببره در مرحله یک سی‌ودوم بمصاف پاراگوئه میره، بعد بلژیک و اگه ببره دریک‌چهارم‌نهایی با آرژانتین بازی میکنه. اما اگه ببازه یا حتی‌مساوی‌کنه انگلیس، فرانسه و اسپانیا در مرحله حذفی رقابت ها در انتظارش خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/24301" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24299">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCnRBN80NdKFoeqUElnJWDig1T5MpvDAucp02BrpOyG-uDu-Lvp6_aSHYyPk4TwaETZekJn8W68EHK9xUsXM81B0WXwBw5K3s90CPvtPIP5PI8gyDAIjdFxtQQKhFEDvqMSSp-kXDtaU4d44x6Bj0Rc6hifc_sg9B5wFlM1LfFw3optASqNRU1WK0tPHiA9LPD7QGiePq_W3IPm_B4gpQ8S89vnIFvQmkbqJ6ZTvSjWkERvNHUR9fT_4Ih8Mg78Ium8vhzkxZ-qUcIf9sj_eFhlSBIBLIRE0aa5xCLWbyl4zmBpX-pZ33vxb09c-ebjvB20Dk8vZPcupnaAoCtWLUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24299" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24298">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5H_siho7x53SUwvS4hfc6TPCdgPSfVk2ugivzIa05_dQWOca_mRuJAAhTjjtz_1vmxikeyqVq6efbTPI5G0v4Np3xvwUCrWYnMHwHU2Ts7BJUkXz4MJj79pT2fFN_Uh2eHAWa517OzOi_P6d3Wg4kFLfhvdM3OyOgVECMuZXC-8a2CjGwU3MHAr5ektYksAGMGRft8BEZ0Q4kmGUtqliPUWtfAgpoCX0rl-eg8vgL8ZHo4HEzrN1qJG4L_nDWvzQFRtydefBu95KweXf376ntRr1o2I5itMfW_4FLYRGjaElQSYvhQziITnfsVXiK4_-f1qrhYxcQmCwt_M-GHt8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیماریزیو: رئال‌مادریدمیخواد بند فسخ قرارداد 60میلیون‌یورویی‌ نیکوپاز روبرای پیوستن‌به‌ تیم‌های لیگ‌جزیره صادر کنه. مورینیو گفته مشکلی با جدایی قطعی نیکو پاز نداره!!! دقیقا اتفاقی که برای اودگارد رخ داد و چند سال بعد رئال برای جذبش اقدام کرد و آرسنال گفت…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24298" target="_blank">📅 18:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24297">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvTjoRWXkNA1JrL6-7H-HkXB_zqbmfFlMWOy7rKsqkcsKzQGR1SQsZ1NkRTKPzPcRTYMTtQXJDKyYDpvA8fjaumBoxOnDvMn_Ub2wCujpT6VqG9bfbhl57euf4KUGxOcsaNsGSeJKVB43I3bcnlvuObfM4PlOXcGTbMBPRnOO94GmOrxrTHUOOnwyagjrvQ0qYtGKKcz8zJJwOcM9YIpUmA38rzYFgqEEUtG-l4S_jNLEHzoR09TyGgT5r2P2h_h6pa7m0QvEHWknYnwRDNyb7lKpYV7M5FcXdY4-oYC7bfY8U04NApoQWtKH-iQZd_XzO0shcNsVY_ndWoj1QKwKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کول‌پالمر تو یه‌پروژه‌دریایی تو صربستان 10 میلیون یورو سرمایه‌گذاری کرده ولی بعدش فهمیده صربستان دریا نداره و ازش کلاهبرداری شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24297" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24296">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIMv4Ww29uOrlMAj10zJgWxiXDX8gAfZZlM0NStZTU2XNAtTzYLunw4Bp94TSL1y7OivgzU5JguOrsTZTcorjfjPLYryoVblhj8rWvJ-Egn6KKi_vG5pteMlLCvsH5mZXE3LG5oDP6gZqNdnJzKA_LeWMkAbLPRwvBc0f8-RaqkG2yEOk9M4dBAM71ROMpO_wClMLjkaLbxGki9pJihMklzo639xLmlgBsGmJ1Z9Q07KWp_1JrLX6ZeLaXkEP4i9SAuqpMbXPxRSMGNJhMpAcRYiCe2RnNCAGBtAra-V_ELGkKX1dpSpQwYSfZBo1t7O9yWtC8Q5wMGcS7jSvgc2Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24296" target="_blank">📅 18:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24295">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quSX8VY3KdIpyXhwCYRcz5KVqjb5bqR30toV8BI4kDzGMXhPlBWxVlsoxGZo4wLwjC5BgtunzqZKLjP7A2pYJlQdnSyNukQqG9CfS2OuJGh6bGDEi6HpkzWaQemWojL_Pajdvfk72A2yFrfVNLZIjKRiGu7l7Uy2SHuRYqpbeQ4DLG7Tbebg_bXTHBYkrr4osVQmb-pfqYLddZ7hBFynJuavMz5CnVuf_IS6hwoLOT19vl39VYrmHhT4geGHLThfzGT904yjL4tMD4hCwC80x1qJdbKaN4o9hFJUq9tgUXyhDfnVScEzGR2S9Osk8CCDX7fnG1VvnvQ1RdKsgVhj-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24295" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYPkASfkGAuttxZlYtt4dke6oe3BwsEI_S3IEaFvfG6u22EOD00ziHQFLb8LE9mem2T3Ztbzriw96D2paQsMFQHkpeJMUs30hJEween-YBt0Xl2kO3SZTRoi_7VYBYOg_dFgGvEYaWYcnFnztf0ADMfQuwrA5sp5-s8ozw5oiY6KrMlnWMlRgVI45N8YGXrpA5I2FexH2Tjk-mHLlup4Q5iq2ZvN6k6Fd70gwkkfWV7bcAiwh4tInobGzmG-W5LRl4Ekb9xvDk9YNpe6inRcOfSYY1GUUKnA7VIp0NEEylvUhs-YqqspBgQbK1udSDf4Kk71XauzJ15wZEPDREAzxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uJ3xrmyW_jsJx_hrNlQpJsSe-9Kw_4lOfDv_SgS4Gm3b_7ToXDwGrO3NhptkhU5v0Kd0xk9gYm2iA57cWrp3EpAM0tx0hH221Py-pTpdjhtdR4WRXp5HTORRaqqUFnv7JUt6VARL1br4mxTCLqJbu4Jtox2Evhdf2iOCbw1F7sFPkgpk7O5xyr1SmFlSUnE2-0rxWVJjQXYWnfsD8O7PDItpVI8EUPlRB8cSm46rPfI3evKhknWD4C848-TlhEcf8bft8C-ww-9777l43aKi7fpSyJNyJzAI3bK6t_z9KaRXRnGyV62fMPYTr5HYdfYKLeAnUuSKuxaDpu1En-S4lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف بود هم بهش خیانت میکرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24293" target="_blank">📅 17:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlxwUyl_7LIfIXSIM2G-tN3WZew_CDSRk_HBex5rLVhjKn8C4J58znxeBE4ErsIBjQbzij06tqArZnPLkqdihpb0kpcNJQ5aMMglxiV6aOUnha-Qv0g_1fn60nj7Dlps7OF6thHMe0nG9S868TG0piYKYqMVp-E8UEDAPMV4G-16H7Nfw4djWLpRlLpQNH23hiJzx3RLYh2FjuYCguhWYWiRfPuOCYu0a09zRs6v2otv39diLye4OoALpsPWFtx5NJawzolgXlimWHVs6bpNOcJln94M1qQ5nXojVb_TjMRT8x5kwqDw5Dvlg65cCNNs4QYRx9St9XYxuSxPxXTaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24292" target="_blank">📅 17:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5VeMnqkCFBU6jnMZAr3CntyfS05X2Yq2JCijG4CPDINbZSbLQVqucwrLjLFFpWZZzlZvV0B-0P9LYhl24wDU6S8r8OT-4R0vVl1ZyZIGfiey90ECMYklV2UjQLogibDTp51v0viSSuiVHMdaYEqKu1l3RFpMguohcn--A-GB2aDWyD0vMgvGDDlO5MAlnuEYFNbRgfjySqpfcnfCmq2fGxgXykEiIAi60qkUda1mfc_bDsFiCqGVimwCCJhx0Jcqf2xWWXzrDnFXoVEQ6kk7iLPDie7j0_dzerBtXtihkIAQP9so29p1wi4Bpf3FPiowP4a6HcoiOPCdclZKzQ0nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری اوسمار ویرا سرمربی فعلی پرسپولیس درفاصله 24 ساعت تا دیدار مقابل چادرملو اردکان
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24291" target="_blank">📅 17:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=TfIVSQrU5-kjLloNaEBV1k7gg5-g3qN8vkrksOj_SZpDubR6VdYTR4MY3Brsr9NWkqWOOpmvTBQCRUOFCXxdeSJ4JmZoYn62uwTDqij1mzglCPEzvbvFIhW-02Qc0Ibjl11z9Na-mVK92jB73JGHnPpziGh0pfAfmf7c0SJeL8co4kCDlaIZ5Z33jDDGTzYt_LvOPZEhPiZVrfZ9UE54AuNvjDYyktVmMtQGsjqZbv8QlN_LujBboTHqhC5k1IUijvtdYfv8Vkb-9wLI9RnU8TWqjFk2viiy2a6_xgkXrmdRNPEQuJHgg7YJErF1q3Fd5w2-YGdxvkDLSnnBRBf9_qGx6cU8dijoZVLdXTylayjZiTGdsz9CyiEvl72tQUzFHBmZooBMp8Zbj8xGKS5wekwhZ5BC3fJR9KcGajddZj4PSXUpAzQ7z0XoP2-8qtrVGwccodIXxzBglbaEbPsaqxrcI-sHbsx7sAPI5A7eVEkdUJinqqnuU0mkS_P0MFIhcQWB1IQnsk0Z2FIJerfzAs-O_TQv4O8wHhHnLm5bBzJY7G2zCR_dy7sVcBCH5MmluqVoSDNasP8eawcOOXysvdn6ah8POEMup_oOgYE80gRhazssOJG7i5_hk6ir5QUKwQ7TeUBJxa-6NuWbyynXCLoGlgNMCNrorK4ED0-bbo4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=TfIVSQrU5-kjLloNaEBV1k7gg5-g3qN8vkrksOj_SZpDubR6VdYTR4MY3Brsr9NWkqWOOpmvTBQCRUOFCXxdeSJ4JmZoYn62uwTDqij1mzglCPEzvbvFIhW-02Qc0Ibjl11z9Na-mVK92jB73JGHnPpziGh0pfAfmf7c0SJeL8co4kCDlaIZ5Z33jDDGTzYt_LvOPZEhPiZVrfZ9UE54AuNvjDYyktVmMtQGsjqZbv8QlN_LujBboTHqhC5k1IUijvtdYfv8Vkb-9wLI9RnU8TWqjFk2viiy2a6_xgkXrmdRNPEQuJHgg7YJErF1q3Fd5w2-YGdxvkDLSnnBRBf9_qGx6cU8dijoZVLdXTylayjZiTGdsz9CyiEvl72tQUzFHBmZooBMp8Zbj8xGKS5wekwhZ5BC3fJR9KcGajddZj4PSXUpAzQ7z0XoP2-8qtrVGwccodIXxzBglbaEbPsaqxrcI-sHbsx7sAPI5A7eVEkdUJinqqnuU0mkS_P0MFIhcQWB1IQnsk0Z2FIJerfzAs-O_TQv4O8wHhHnLm5bBzJY7G2zCR_dy7sVcBCH5MmluqVoSDNasP8eawcOOXysvdn6ah8POEMup_oOgYE80gRhazssOJG7i5_hk6ir5QUKwQ7TeUBJxa-6NuWbyynXCLoGlgNMCNrorK4ED0-bbo4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی بال؛
تاکتیک آقای لیونل اسکالونی سرمربی تیم ملی آرژانتین که به شکل فوق‌ العاده‌ ای هم در حمله و هم دفاع بسیار عالی عمل میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24290" target="_blank">📅 16:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOqvRh9k540kzKOL3G4cicVwQI1w5C2gmf6wfc-_nDPMARYTuI4Ag9eMC3oi23wuzUVH_Kj3UoQMpGU--XP2LUWTG-4TLNLFrjgPuGSuJ-PASsV1zw1Hr3_-E8fNugb1EdGO7BqmRLLa1-T2Rkz7lafeNk_ngBHXTljAyC4l9tfcOcnrWzHT9vGEZyuiMUjUVLulDU2zY3wvN_OriyggZOmOnYuftxNTdtkU7GEvxyCbJWL92YqmC-CRMp9ltmiIKDBCDgtQ74_hBe-njTi5Fuvj1QJ4gedAVEnfzJzqViooR-RSRKEK-f5l-2Olm6G36xUlMoZD_D_-jmVNyUwSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24288" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=N_VNEUI5SzBuvJbSzu-O0tnFAmDPzvzuozR2dXgDKQB1B514rRS1WJM5ntvRVB-9DcC36rz-doRrapOrX7sYLSkFQGqN0BLXfXxq2ltrKMONkA8bPFT_g5W2v26g3Xm7hLY9UYyDg0BuBIgiKBdL7R-nJl6IPKI69AHABbJIJILyizg94awWFZk_3KSeGMmo2dwd6oCY3SiHk8xKuPCWt-63xCEYdBo_ytVXVluQ5XQ1rS-E-0qMooM4FfdNTuws5HzpIjjJHLQlRWZu4himAAM0NfSMkwSf1QGxM63qD-omgSSDx5osIkbcC16u-gAiYsnHDnf3v9bljQZMm-tvGbO2ADWcMRYdjb-Jw6dkwN0XylsslJlqYrUijwjV3FhoniL8G_-BLwO7DXYPect4e1zK95gR0AQxgc9OrCrX1VDvahG8IGB-Cr3fdfCwccNyLYqYhZ5zSXDovn2hlcKaGiQhk1Nb70xpdDMXijrd9cXWZTVlzVkTNzcq4KU5smjRVXIJD6DSr9rgk9p3u0E0cdMhiLLHC2l5Z9S5-JHkmmQjbA_F_UemBwg_vIfD8h95D3sqcMWp8HAd5cYWVwC7vCiur9TGsUscJuROIDY_jBIrlss7PA1bNdwVaH_An6C7fohP_cOjTLExcwc8Sj_4JmQYJlPtSxhaj0ROuQaogG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=N_VNEUI5SzBuvJbSzu-O0tnFAmDPzvzuozR2dXgDKQB1B514rRS1WJM5ntvRVB-9DcC36rz-doRrapOrX7sYLSkFQGqN0BLXfXxq2ltrKMONkA8bPFT_g5W2v26g3Xm7hLY9UYyDg0BuBIgiKBdL7R-nJl6IPKI69AHABbJIJILyizg94awWFZk_3KSeGMmo2dwd6oCY3SiHk8xKuPCWt-63xCEYdBo_ytVXVluQ5XQ1rS-E-0qMooM4FfdNTuws5HzpIjjJHLQlRWZu4himAAM0NfSMkwSf1QGxM63qD-omgSSDx5osIkbcC16u-gAiYsnHDnf3v9bljQZMm-tvGbO2ADWcMRYdjb-Jw6dkwN0XylsslJlqYrUijwjV3FhoniL8G_-BLwO7DXYPect4e1zK95gR0AQxgc9OrCrX1VDvahG8IGB-Cr3fdfCwccNyLYqYhZ5zSXDovn2hlcKaGiQhk1Nb70xpdDMXijrd9cXWZTVlzVkTNzcq4KU5smjRVXIJD6DSr9rgk9p3u0E0cdMhiLLHC2l5Z9S5-JHkmmQjbA_F_UemBwg_vIfD8h95D3sqcMWp8HAd5cYWVwC7vCiur9TGsUscJuROIDY_jBIrlss7PA1bNdwVaH_An6C7fohP_cOjTLExcwc8Sj_4JmQYJlPtSxhaj0ROuQaogG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
​​
طرفدارکوچولو و بامزه غنایی‌که با جان تری اسطوره چلسی و بلینگهام‌سلفی‌وفیلم‌ میگیره؛ گفته ازکی‌روش میخوام غنا رو قهرمان جام جهانی بکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24287" target="_blank">📅 16:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h3CGEHmhaQmYg5dSk1EdImUdxHykYwEO9vSfB1NTzny61mG64Hp7_KB8-oOIRc0dLkkI97LnhgqeqQzNiwX3L3hT_yFswVZgpdRoB5B_uwMaoa5AOXcRTEN7nQCnWYe0aWV2gHSC06vL5mTXfkjCt52W-kXS9kfQ17lP34CnrrEfd6scXMafOiJVxHoi0Ql5iJ02qpmDv1sh6qeFr26JBIkDo_UyJI2e8XbjPy4hQRcPNdyfp6RDWaNX4VeMHg3rcNzgiFtXMwRFbNw0ku1bQkPhc8GdiitEdyogfjM2Sc0n7PM5FXOlc8nSZ6oJlZ2TPlavpW62nCJGqj9B4r0p1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#فوری #اختصاصی_پرشیانا؛جلسه بین مدیران‌پرسپولیس و اوسمارویرا برای‌قطع‌همکاری دو طرفه به‌پایان‌رسید؛ اوسمار ویرا موافقت‌خود را برای جدایی از پرسپولیس با دریافت 900 هزار دلار اعلام کرده‌ قراره بزودی باشگاه‌این‌مبلع رو در دو مرحله به او پرداخت کنه و قراردادش…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24286" target="_blank">📅 15:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9q5sDnw4iAo0mMxfO7Obd81YSZpBdXnppn2-69DrUrI8eg5t9iFRpk8o5p1pWbWfiXW2Cq-TCQe2nxSXDNA0aIyMHmUgaH7lz04gBvp-xrYh1HiinTmkwC7_xPL-9NMb_3FTGt_Uf32OxMB-fZIMkYnlx0BeazAsDkOpGdW4QyddhvJDMS_b7VVZBc7nXEew58NVQcJ0i7JHYL_O7Lf90birPrUTHW6F9B1nEbywBfIAA6UKeNR84e_Vs1OfXbz94b1TnmXrolBekGRHqA6l1aHAPfZcerw5jeYnz1-bR2G-FklH_zB-dSwJaGzATjGsXsEtljsjQL9QMNTDHEtBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24285" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Te6z95D7IXMX1aoLie0vVVZnFUQgCGlQ_VH72njEtAYXxt5bJP2f99a2A0bh3oAgYp7hNykenWrMqf_rk83YvLdEqKAXHHcmjT-rSA6cgE4LpWn5uZWXqo6THqMwjIP4RhatOQEeppsTFolNLZcLDLnDFGQeyxZPMWJSJ3i4mXxx71vCEym_DFTOTR4dpzC8Mkdiu8pZ4IGsSq1bWLkZh6QEOFK4dG3QDRESWxIIcexyxv4MyxRG2TLYgydjsncmRPvY2-hjURr0obcLX-GzJCuOF5mbDSDuql9uSPnNfYWWIGn3lXy0uqgV1p05J-NE0SPmGcyekbu8rdtKQ6pP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛
علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24284" target="_blank">📅 15:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glbc0Es68fCkYP3Ruoq89qVKacBTTJgDa0T4FzCAjrhWmV0VI8azJMgEWZNYFcB4v5pxCFwRJLqbrbR7_Xi0PTaqCnKeDWm8hioYUDqJbGxok86-MvBXCNatf3gm4eOa6Rvij4p3amXvb13x0PDoDWgVKxUtCIwVa-C_RL7LiIwyIg6jnrDrLbmhC5PXMjeLwA3Qkq2C2jR9xKCOHtyn7BK1lvjvdNaN4vq6dnjBylClP4aXKu9gpYWitRBLs694899cSWllCSMTJYHfmJnA1N02gvqzN2WfKfFWpo7Kh6x-8s9NxFRteOJ6C_dNl3Pz9hVtJpN6-UVFbg8AM7d7Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24283" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QF8X3NtabNu2AKb6nzf3tKt9Ho9c0y5NOrgpxUvSNswEH0wq_IKiODGyKRBMFhk796zqpwSKC2VMCPPF07tApioCYMAdM6Wq9m4BfYG4MeKKSj1VT6atv-uKLn9Yj8Juc_uQmYi01WB3erVcRBByx5hi9mMgw1tKDFybdfeeVsgx9RIWqrs7jS7LM9OeH-2kB2y5exXhCn8aetsJ0low8NheuAzUA4GZbChfvStxwxkB72Xrn5SZDd9SgftQzFcPLyphtJBkVCpTkcLJkWpZOzdMzJ0xlAi_gY4MVlMBGLUiB5qUELyTtiAJrJU9D0W5ycasEGTI8RFL9emyWxmOoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
اگه شاگردان قلعه‌نویی به عنوان تیم سوم صعود کنه در مرحله بعد ممکنه به امباپه و رفقا بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24282" target="_blank">📅 15:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24281">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=muJALhoOz3HmsQ6yJ1_HdIkytYvhhj4sZT460XEJf-jIwKbJcelKdqI9FwDpWnlMcutrlxOXJN-2ui2S1h8rtSKU1vyGWXEwyACjaM1BWm3lb3jFyY6C9MM3Z-zsLag90TS8SDOYJNKxd3LzJvzL-7zkz0SCH5qBH_2asnREH3nGnF1lDFq6FqPU_x8-KJp67BUYEv5hY6AfaWDVe1xMO6ypwzWNXqD_c5_FLQMgKI-l66JXkA9v3Z6FCvAkiBLpZAP3ggl86_Zff9Q84IMfOUL0Br-XlcTzbXDnyJnbymFMMjx7Sjq0YUryQwqQlIG-gVjMw0p0Diw30IowEztKKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=muJALhoOz3HmsQ6yJ1_HdIkytYvhhj4sZT460XEJf-jIwKbJcelKdqI9FwDpWnlMcutrlxOXJN-2ui2S1h8rtSKU1vyGWXEwyACjaM1BWm3lb3jFyY6C9MM3Z-zsLag90TS8SDOYJNKxd3LzJvzL-7zkz0SCH5qBH_2asnREH3nGnF1lDFq6FqPU_x8-KJp67BUYEv5hY6AfaWDVe1xMO6ypwzWNXqD_c5_FLQMgKI-l66JXkA9v3Z6FCvAkiBLpZAP3ggl86_Zff9Q84IMfOUL0Br-XlcTzbXDnyJnbymFMMjx7Sjq0YUryQwqQlIG-gVjMw0p0Diw30IowEztKKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24281" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24280">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3i9kNguw7BEe2EK9IPrk1oc4icrpZqSYlejN-jQAdsvPwBVHRpCW6p90PF_Vle0o-aJMqXAOTM1uUcMgqYjmGVT7iYbxfHWH-c1TqNhLBRlIn1bGZBnnvumngJ43Xeeepy3wvl0oiABW8pLmRM1S7UE7JISZ2AHZ2H6NtbG4txvW5K7mJBhBj9jJVXusNcqDklau8z7abjALbzoJ4Wadia9nZVzD9J69cgkYj05l6OEr_i6s0EMQCGPCJQ-j6rSyEIRClvhc4427iaBDm0P_L4iIX-w_aTFhqBHX9mN0flhtsI1B3OFiarBDlOPRFUi2taTvpF2C-HGy8lSqlqtVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24280" target="_blank">📅 14:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24279">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJMLwd5JNcKtjZEhoUbCZdlLqrBQDFbIfUiyHX98beXkJ7U4-9ZMMbwh8enyowBQCURk8Q7XLOBuU388iU-jRtuo7On1l07DZL6RbH6cQq0scdHJYX5YsESazKwXLbedhhgPzPaAS0D0PnJJn5UhfKVkenC4STJG3gDJfe-ZMIwR3IW8lyh5ZYZ-kRHGS_mpFoVxLUX5hJ9gvo9eTe-MtgEJHgh9ovI_A-2969-oPEvTLFVhaMgOp5lI2AJvYYFihZG7TWgx9dMd4nXR1DNmyb-Y6f-TWaf8vpBh-HNCGgM1E4IYoO9ulprUKVjS-bAEw2bzJGGlNz5yOkombs-43A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جدول‌گروهA رقابت‌های جام‌جهانی در پایان مرحله‌گروهی؛مکزیک‌با 9 امتیاز مقتدرانه صعود کرد. آفریقای جنوبی نیز با شکست دادن کره دوم شد و کره نیز احتمالا بعنوان تیم سوم صعود میکنه اما قرعش سخت خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24279" target="_blank">📅 13:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24277">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZfpRsDHTPB7NGxYG4qnzrxvOahH3_Rq9T54vxY3G59gl4KF9B5zh33yVIxQdNqLgxLPY6aNO2xucq_J0bjstH7-Fw2KzP05fe4N56P3-u0rA5sfUksLx8OCltW2stWCChAuez-B7dfgW6YsjW0HrcIsfUp9lJgpCaRtMyNcRPHOMKHTmGvwb7OwwsZjdUdn5OWhv7cbFJ3ZoXLhbaKJShMeKPgZT9WfYEU9Y3h0-RiQfvswBV6FiblXy7QF9JgJeJ3vJIGLpD90swj3z89_xj9LiK7f0XYG8O1c4luXA2bkRgqRtub_Eog-A2dg0zQOoAYprkVKpw1boGNFF_VJlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24277" target="_blank">📅 13:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24276">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=Sj5Sf5kNCakD2VGLYNAnDnqsppcz1vXTLQ4hLjXJ2pAjsDg1VW5EwsKOApBw-tf_GcQatlXKKmY-HULPolaentn_H8tc8cU8asIX1FP53JB-u00XNQPmK1Uq5ugG1ZCKJTM-lTuXE8eiCL_dmkK7bi6pK57uxTWa2okz3rHA7WJGAw5zMHthZrUqIVD8u3US-fxtrqo9vy74raKnt9TRRk972puXvcJ3Xqb_bnahsCfmy_D_kdiCrVx4vpj2ysPZiXRUYK9F3JjF62DSnUMAeRWLt6BPUIZ8aUq3kthEI5rkH1CItQqfdcw18Lau4VUOqDzDWThwIuZ7fj92qwN3vwqMOSn9DEw_xcK4Z6XEJqfuEPzCgyMBveew9IVNAoUkexJrZlztWxYXbXU1ZvclCBU8j6Sihp9CJgGxmFvv2wvraF5k8eKzQErKIYOQCSB190HfBz-bq7pQ4GkWw_F7hwRrJK7-MhNohbEz_U5e2TT6Kz64kVL9gr_6pJb9-PPJlqCXNxGXU7v0_7y1ua3dxsLhIRw8Lboxr5bPTxxnHDWztcr9-GzUFMuUVU4iioYXFoSkaHSvZfdN3-YDAc5Cn2NjGBEoK29_QeXe6A3fxkruEG-Zd6b61Ei2ezvjJXHFjLX0OHD0dW0BRwjdMUEiv1lHhGSr_RuJp3BVZksq27w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=Sj5Sf5kNCakD2VGLYNAnDnqsppcz1vXTLQ4hLjXJ2pAjsDg1VW5EwsKOApBw-tf_GcQatlXKKmY-HULPolaentn_H8tc8cU8asIX1FP53JB-u00XNQPmK1Uq5ugG1ZCKJTM-lTuXE8eiCL_dmkK7bi6pK57uxTWa2okz3rHA7WJGAw5zMHthZrUqIVD8u3US-fxtrqo9vy74raKnt9TRRk972puXvcJ3Xqb_bnahsCfmy_D_kdiCrVx4vpj2ysPZiXRUYK9F3JjF62DSnUMAeRWLt6BPUIZ8aUq3kthEI5rkH1CItQqfdcw18Lau4VUOqDzDWThwIuZ7fj92qwN3vwqMOSn9DEw_xcK4Z6XEJqfuEPzCgyMBveew9IVNAoUkexJrZlztWxYXbXU1ZvclCBU8j6Sihp9CJgGxmFvv2wvraF5k8eKzQErKIYOQCSB190HfBz-bq7pQ4GkWw_F7hwRrJK7-MhNohbEz_U5e2TT6Kz64kVL9gr_6pJb9-PPJlqCXNxGXU7v0_7y1ua3dxsLhIRw8Lboxr5bPTxxnHDWztcr9-GzUFMuUVU4iioYXFoSkaHSvZfdN3-YDAc5Cn2NjGBEoK29_QeXe6A3fxkruEG-Zd6b61Ei2ezvjJXHFjLX0OHD0dW0BRwjdMUEiv1lHhGSr_RuJp3BVZksq27w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24276" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24275">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NttfWG7J3g3krN40_GZwoHSZm5tYAKebrplUvgS50A3fAtz_VV5AdBIEtZBykfEuQV1uPrZz1CviFsgphdg81PRsBTNegyhkAo8LJHJktQn89DiHaJT0n8tvadvNb6GUp4KjMDeZJW4zkXbAwleXbhjSi2lQHMS0N8jGwTxsyxtkitoc8YV1rP1qYlGjQVIT1vU3TBGgXX0zLCbFWFUFPFKoDYTo6hbn6BaLTAK36jHGSrIiKRA9onxE_wESJgSLYhtO0KHH9tubXs0RS2vHUwhTTJ6WeO6Mhxnf4dKf1ZLAYApvU7D6C7N-K-2QMBD9Qlj8axGk_AFBs_rfup9cIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
باشگاه اتلتیکو مادرید: ما خولیان آلوارز رو زیر500 میلیون یورو به بارسا نمیدیم. آلوارز زجه هم بزنه زیر این‌قیمت‌فروشی‌نیست. رومانو هم گفته مطمئنم 150 میلیون‌یورو بهشون بدن درجا رضایت نامه خولیان الوارز رو برای بارسا صادر میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24275" target="_blank">📅 12:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24274">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=PDjEB4ieHjPs7iR57NU21H3Irq6QENoyW0M7vcd1Rp171ejO8l5BAvoJQaCyXOFTSt7h3-XAuICc1ckY6R2OPm8i6GqxOYeMMpd9XO5lH_EodSFk-6Ni2DiM3xdp7ECesmh_F3_zOde67-DIGMQuXgvkoo_042OlFrEDBcsHdVBjaBFp4VjjqMhfb6RiIitVHGg-eSRYtWg2WAOxl3PZol2JJIIsacZkY0JVInqEKy6X9LMBPKqLq5rcwY2v3qD4aHHKvEgqUfRWkkHzYe53YojbLmZiXphZcjYNV6pd7BcT9OWHRgaYbk59oZuRAWZ-wytAWwBJjkyiaJs7wPgLkGjMqRnn6uEjMWn9ogTU9OsOt2Wi9vNSgldz84YxWKjkzl3qRP6CA8WPWQEtddHn2wShrSlvozh2Z5VRttXLYx_PMbprKYrlMWla4m6UdUSHVonK6AdXnFhy-O9tmUpkmXPEe17XC3BzNsLlRvd0hTfNFzAfds9GrcuPSK3vYxq6CAbqVkBqg5fo6kzuf3IvvODljL_Sqf78kYI6Fkgf7M4tICsiJJHjqtoXoQjgNtQh4CSUzzNMFtks-sKnOtms13joBG6kA4bz63WmeY19cDHVGQ3lKYWvNiZPEI95Fl1cg35DSpgAVB91j8sZwiHX9wA7tpQ_nYUCtlVLqlEPZ8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=PDjEB4ieHjPs7iR57NU21H3Irq6QENoyW0M7vcd1Rp171ejO8l5BAvoJQaCyXOFTSt7h3-XAuICc1ckY6R2OPm8i6GqxOYeMMpd9XO5lH_EodSFk-6Ni2DiM3xdp7ECesmh_F3_zOde67-DIGMQuXgvkoo_042OlFrEDBcsHdVBjaBFp4VjjqMhfb6RiIitVHGg-eSRYtWg2WAOxl3PZol2JJIIsacZkY0JVInqEKy6X9LMBPKqLq5rcwY2v3qD4aHHKvEgqUfRWkkHzYe53YojbLmZiXphZcjYNV6pd7BcT9OWHRgaYbk59oZuRAWZ-wytAWwBJjkyiaJs7wPgLkGjMqRnn6uEjMWn9ogTU9OsOt2Wi9vNSgldz84YxWKjkzl3qRP6CA8WPWQEtddHn2wShrSlvozh2Z5VRttXLYx_PMbprKYrlMWla4m6UdUSHVonK6AdXnFhy-O9tmUpkmXPEe17XC3BzNsLlRvd0hTfNFzAfds9GrcuPSK3vYxq6CAbqVkBqg5fo6kzuf3IvvODljL_Sqf78kYI6Fkgf7M4tICsiJJHjqtoXoQjgNtQh4CSUzzNMFtks-sKnOtms13joBG6kA4bz63WmeY19cDHVGQ3lKYWvNiZPEI95Fl1cg35DSpgAVB91j8sZwiHX9wA7tpQ_nYUCtlVLqlEPZ8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24274" target="_blank">📅 12:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24273">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=rbRlHeoZU6Ty0nxmS7bV2TChr-3F_L0kKeMEImvRJnk9XVFRLmEUfNNrfx2G_Vcz27VDfy2xyLpl95-LdSt8GEFV2J80T4JkLg585h80ZlTk3X7b5q5q0D1Wi7McOCd-YRvDc05zoccOV1g0AFmtPSdLqi55CiXpPDiqBfX92lUFLLpISomGNosv9Dc_ikIu6V7KejmJ7c-GBQ8j2mOQqosfILApVrCxEaMlMrNkap85OuB0reJ7ZrP0qRPSVPBovQqbrlklGPe8_dR_-W40DK6EZL0YGPnbtHNTJbT5JTVlmKMUutxeo3ekdXxuKB5HZ60T4fz9vU3g0y670wFjOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=rbRlHeoZU6Ty0nxmS7bV2TChr-3F_L0kKeMEImvRJnk9XVFRLmEUfNNrfx2G_Vcz27VDfy2xyLpl95-LdSt8GEFV2J80T4JkLg585h80ZlTk3X7b5q5q0D1Wi7McOCd-YRvDc05zoccOV1g0AFmtPSdLqi55CiXpPDiqBfX92lUFLLpISomGNosv9Dc_ikIu6V7KejmJ7c-GBQ8j2mOQqosfILApVrCxEaMlMrNkap85OuB0reJ7ZrP0qRPSVPBovQqbrlklGPe8_dR_-W40DK6EZL0YGPnbtHNTJbT5JTVlmKMUutxeo3ekdXxuKB5HZ60T4fz9vU3g0y670wFjOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24273" target="_blank">📅 12:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24272">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQJKJ0gEtTK7vYM4ZewPg7yLcUxFRMUHk7jq_x9_IqX04PHVBTuTAbOwCp_CtzAEK8MfG6RWepMRe8qJA0Zh3rvjrsaBP-YcRCmNT6DOKOugsa77C5fhRv1c6qxK7RxQKxOI0ugcat6d3OHIbet--bNiPllIs6Z4y3s4OpXFtL3fsfHGTp0zZ5E_Q6p5DKzN6Vl0j4QG9A5L-R9YgOKT8pILjcIvPzr2QWucbR1bDfin4tG39h4FiAxhnAbXtHRxm0P7bSXKlzxV1CBBHcfdoHWP7-N7FCpzYxXmXOjyevXoRkY0u_b_-0MEL-m709tz0sCLLnVthN8xjjskAzYnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعدادفالورهای وزینیا دروازه‌بان تیم‌کیپ ورد در کمتر از یک هفته از 50 هزار به 15.5 میلیون رسید. تعداد فالورهاش از 8 تاازبهترین بازیکنان حال حاضر فوتبال جهان بیشتر شد. عکس رو باز کنید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24272" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24271">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryPES6kXKN7R0yW6jcXmVEg5-bqcT3GcPnrqGA21BBhEdeqcptBs7DFN2T-SUDbpD1f96BCxWC2goy-o_Mv_yYVa5eSMJI4F8lQZ2hSeO_f79e3crqHUokcr2rklMa2lEauNatKK-ZrxX81o95-hyjTl16nzJ0OGcdNwRMaYcH3hMPZ9aoeRxyv349m4YDo4I8-sdjLksxCWonHHjUhllz7-Zl70pVJXfVQlrshLS9BEel76pEaPvpz2Et94KmpwUFQuhLRtRGjSCB3S8nmEkrs_dTBZCV3Lzl-GkgtxVId5oIAxmgpdSBohhOfvwxRFDSwqUASMqGJa0Vp6cBe3cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌ های دیدار امشب دو تیم برزیل
🆚
مراکش و دیدار دوتیم‌مراکش
🆚
هائیتی در هفته سوم جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24271" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24269">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcCqpZBngILNqotNKxjxLGPGU5x1yKvOdGkSuDNNroI0Cmtf--wqkourALEuwbEcJsg-RtPCdEI5TSW4ytUJm8vaHMk9S2KTpTEpx88PLDnNfj0BfGBTKVTpzrL5zTSRkTMbN-8ODqkkEA266-IbsV5wes_eBQ8uliNcGkmxOVbHHbBZuMcS2DNav7JPAdZlG4BnLOtRGqW5x5Jv8kb0JTzlBdJTMzDJEvpIIe4zUoSzbLhgq3exSmtcvC_HpyrqT3I2ZC2fkLWi47g6GG7N8F0KwSpoiQ6ZOqWFWw_hjn2o0KI4N0aULE9opPEZgIYaRB-jsbNAXxkq23af8A2-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24269" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24267">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DzvjwgyVForMCgyAZzSbaRv-htsqYa3LOqVpZkGl4WlzYOvGii47ZYx0VstskHugCare3DxHnRrrbCFFuurDlzPc_mx0-gi2jbvrB5V2TNJg7eYbdivfEd-nswPr2CaWhxuj5LQmFMAiVP8-eSmthLKJGeYKBaDLYMTzLHDpueFfCaZkUCqKZgD0sEt6ve_7GLpFl6hN7qwWQiLixb3_6pOdNYDqkGHiCPqBUeKuFpWFacWWl-b9UwWiFOhtmR_thn38PHr6Hm2P6nsF9YUd5LmNBLLhabykNra50scayRT_-ae73Gm4Lx5faA5Mi2S1LTZ5SLwZqbls6XaVf4XyOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M89bVyNN2jPBMLXWpkrYq6aAkH23jRK5xhbNFh695gqt9cKnN4Pc6zIEdSyIwI3-IzpGGJrMY5OF4PDsMhrA7ml_BNNeQKNLVGXPGyFxk9tYVUmfFt90BED1JDffj-ZPHtoHsgw0PR8AiiQPEWRvRr6k_-tHpNCfYH8G9iMHXmYrnJCDWxNh1cNb3UlupL7NEX8CjD4vmbmQAAOigc-tEq0bl6s-QTWm1jWvdl6FGMwwqqFQ4uvfVPiVZUlduvijjd0J-Jr38PMmjk-hsHz3bgy0Zm-ONu3iJfLjdv6pOPxqX2Y_1umM-siZFOIT4J9oEU1n-T3WfFyWVUbRLZ5yJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24267" target="_blank">📅 11:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24266">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCIhEiEU8KIrmQwKLnnW_Bjj67VwQE75JCy8HDG-QdGhzPDXOYWZ00-M2rlrD8SmBq0Y_hQBQNTmPTz1qdVVhT54z_TSTHnM8qz2GiESPG0aW2K6sqsLY5qh9nSmAlBiy6-8f4Flaej6z12FTxUzYS9KjK6yx8HKo9aZZv5lq7TN0dzS8Xd-Adn2HsEVp1nJRTKMOhi425YUS_7xye2CbtOz_VyRbGsDBoAvJedhu7t1se6Y6yLiBF0Srxnr5RGhinhzMrW1dx9PyrRWjPCeacMTohv3NgcqTfPaYpsRit9N2sDze-9jXwy4OkTI9Mknt5N1wgzceSxpZXNZLyLegw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24266" target="_blank">📅 11:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24265">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=f4aLCBebkVTBG5YgOBzDPqq_UAbcWlPyje4OutY38GRIKqcPK_jumaup7n_Rzf7OTFXqBEDk09dRncpUtyO9xjOpGkkr6fF6U1KEjVPZTcTEPg7nW5supUAnQfAf0yCv7viH0tOYibwBuCuf-iWTYUBQhPrg09eztSw9HJsLQOigpTRd_Pbi-3Y6n1HL31-wWBJvIqp1b7t8kmI1FAhWEIEl61vfTiHHcF_dLMfuqm7U8SPjN5BaWQG8-HX2Aex8H6IFMTLAHkqwgfcHvvNmoVQfqSbjb4o53nAmVgwR980x9adx4LnLk-dBTWcrG7YaOsB5EfulGEF6qVB32v7WLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=f4aLCBebkVTBG5YgOBzDPqq_UAbcWlPyje4OutY38GRIKqcPK_jumaup7n_Rzf7OTFXqBEDk09dRncpUtyO9xjOpGkkr6fF6U1KEjVPZTcTEPg7nW5supUAnQfAf0yCv7viH0tOYibwBuCuf-iWTYUBQhPrg09eztSw9HJsLQOigpTRd_Pbi-3Y6n1HL31-wWBJvIqp1b7t8kmI1FAhWEIEl61vfTiHHcF_dLMfuqm7U8SPjN5BaWQG8-HX2Aex8H6IFMTLAHkqwgfcHvvNmoVQfqSbjb4o53nAmVgwR980x9adx4LnLk-dBTWcrG7YaOsB5EfulGEF6qVB32v7WLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24265" target="_blank">📅 03:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24264">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24264" target="_blank">📅 03:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8gy4NOuVIOFZxVjArLJ8CwKZ6vujsQl3Blg7v2cbRejy6_78lCPf3ACvqPO4sC9hl6DClYLMnuEHnziZEdkhcrqh2EnEMikKytbEx-yl7Y7mSL0tfmOFkc_1zFxbuPy7cy6WPt_oj6nUIuAYJVVC-J5013_muNKiQcHk523dyjjjd4Y7289-hCt1RlSKI4SHVl7BD6IeEOBfQwybi_CKRuDcEMhGz1CHndTwZwX3TTl0S9KYqZz_C2mAQ1_H5qaDbNbSe9-392ctdu-gh-89geYX12MFUe4PSe8zjQdd7m4nU8M4umnzjHDgUbxCbSfxsEzBvPhcQY0ihVkSpetyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهB درپایان‌مرحله‌گروهی جام جهانی؛ سوئیس، کانادا و بوسنی راهی مرحله بعدی شدند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24263" target="_blank">📅 03:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24261">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQWoL05pLuvS4iZi4BDLehWZCy0bWTIQWQBc7M1mEdhFqgwVJPyDqiNMsZo0ReGzorEddNvx_ndRsErWju9lUva_aH4usAPcdhNTK3Vn8DNJyrWm3rXCAAzCwiu5oBo53uf-22xOePXbcBIKPBkkFqrx5X1nsESakOjAv6IUwt9c0-2rw5EJUZ2PLZ47YBje6eUBNAYgmz3zclP-lygpYfxPCxyLyj95b9oFepg0NHxVxGSi95x7TJpQAJFsbhC2MwXXeqlStuC0wyTSSRP1sdyvuTlvxEstq3NM0dv9bpjCKPA388ezvIb3YyewZ2QJ9UekFIIYlP9mEfAty_3OiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=hy6LEO3PzfIrnt19cJu7tLkB1c46HzojJ-IdDircAtAA_YCun8BJY5CDqT_4yRZ0xGdKG1XzGgO8Un9BgrWqhtBevT4T371DtWFrTJlnUrXQq5NBBrmTiKrfGEm_QCWChxarar1qvTyrrYHHrOUviYDiFOhJh0NvdQs9oknmO1wzmB_6vMG6t-wfNjLbDzkjgKsCUMo-DJ2P83BYGR1N5dbRT7OG3tKUmvhOc8INAJR7AtL6rJK1ftfnKHwTkSVQ9O-vGydBWeovjR_dmPIyxPchfcKF5SZmPqDN-FhivI-ic17I4j6nuuf3qH9yKDWoOqtqgYCMP9zsohRruOeuMJyvHDAaLIelXaoeRovtvtrUOwMVLIEQF3cOxSp20POWwf7aOFaOTWHHhyqMP73SRFcx_VrVXXLph0bHeYGEjaZZ451SO04P4ZJHtjgQ-1B5BKEukB1y2_i1cct2-0v9mYZvWrUls50omw33RdervnE54dFXyOggtmvkBMVZMXVJE7kuTDk97zvmAT080CvpdX3DLOgDyCbXjeDnk0BH4b4fezu5gI4msxu2UhtkTxDh0xCpZRjkVc17dkUbVx_3XKazH95PrxdRFV569MY-ao33Au6yNNkYvp5eXadijj9S9vReSzGXD-Tgt_cw6culhnm7J51TVVMl_bjnoQk0u3s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=hy6LEO3PzfIrnt19cJu7tLkB1c46HzojJ-IdDircAtAA_YCun8BJY5CDqT_4yRZ0xGdKG1XzGgO8Un9BgrWqhtBevT4T371DtWFrTJlnUrXQq5NBBrmTiKrfGEm_QCWChxarar1qvTyrrYHHrOUviYDiFOhJh0NvdQs9oknmO1wzmB_6vMG6t-wfNjLbDzkjgKsCUMo-DJ2P83BYGR1N5dbRT7OG3tKUmvhOc8INAJR7AtL6rJK1ftfnKHwTkSVQ9O-vGydBWeovjR_dmPIyxPchfcKF5SZmPqDN-FhivI-ic17I4j6nuuf3qH9yKDWoOqtqgYCMP9zsohRruOeuMJyvHDAaLIelXaoeRovtvtrUOwMVLIEQF3cOxSp20POWwf7aOFaOTWHHhyqMP73SRFcx_VrVXXLph0bHeYGEjaZZ451SO04P4ZJHtjgQ-1B5BKEukB1y2_i1cct2-0v9mYZvWrUls50omw33RdervnE54dFXyOggtmvkBMVZMXVJE7kuTDk97zvmAT080CvpdX3DLOgDyCbXjeDnk0BH4b4fezu5gI4msxu2UhtkTxDh0xCpZRjkVc17dkUbVx_3XKazH95PrxdRFV569MY-ao33Au6yNNkYvp5eXadijj9S9vReSzGXD-Tgt_cw6culhnm7J51TVVMl_bjnoQk0u3s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
یک پیش‌گویی عجیب و آخرالزمانی از یک پیشگوی برزیلی بنام «وو باهیانا» در فضای مجازی جنجال به پاکرده‌است؛ او با گریه و زاری مدعی شده که در جریان بازی برزیل و اسکاتلند در ورزشگاه هارد راک میامی، دو سفینه فضایی به استادیوم حمله خواهند کرد و در دقیقه ۳۸ نیمه دوم، یکی از این یوفوها اختصاصاً
نیمار
را با خود می‌برد، در حالی که سفینه بزرگ‌تر هزاران نفر از بازیکنان و تماشاگران دیگر را می‌رباید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24261" target="_blank">📅 01:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24260">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=SiNwcExGYTZc_QpGsqDZxJvWo12fdUmtPhXsJ4UYjWuG45KJDAuoO5wzgnNoEJhv__IDWKyf6V89_s6pobPEGWoDnbd2d9f2ozb_eOMcsupK255o3jgwNsqiBorKkj1k9ykitRZQJNedm5_XEXfx0kYrWEitYDJJ9qh5OE1JHIEhpKjuziwj3WRlNlxkymN2PLewLulnq1H19-RDOOSo89RWVjIwrAhe_nmgDwa6NHAHOpeENA3HAIBa34IhKhRTBigB92aOnWG4TdHUDPWY6LWsAw1JEpujXFzS1iY77UaXA1qVL3f_OTB0f-pmd4wwrn3XgrzjS1yrYRtpaAW00A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=SiNwcExGYTZc_QpGsqDZxJvWo12fdUmtPhXsJ4UYjWuG45KJDAuoO5wzgnNoEJhv__IDWKyf6V89_s6pobPEGWoDnbd2d9f2ozb_eOMcsupK255o3jgwNsqiBorKkj1k9ykitRZQJNedm5_XEXfx0kYrWEitYDJJ9qh5OE1JHIEhpKjuziwj3WRlNlxkymN2PLewLulnq1H19-RDOOSo89RWVjIwrAhe_nmgDwa6NHAHOpeENA3HAIBa34IhKhRTBigB92aOnWG4TdHUDPWY6LWsAw1JEpujXFzS1iY77UaXA1qVL3f_OTB0f-pmd4wwrn3XgrzjS1yrYRtpaAW00A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسمی فرهنگستان لغت فارسی:
آب درنگ جایگزین فارسی کلمه hydration break شد!
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24260" target="_blank">📅 01:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24257">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKuN3D9dC0MIg__HgSgKEFtNBUoewb3vmyH7r1fJQQXCeFuAPlDvOoDOiU9jW7fkl7spZDWCIaph3vBxwDFXIF6ksSENctiLdU1MQ2BhiWw2Y9q8EE1kqrD8EXkGm0cSSPngMLeCe87X9Rsnhbr0hOMdtlQcYkd-uGnwjYWFN8tRD5MdAFaemsE9EapKzdBrx7bfbrTB8ilSX_FVc8elwB5lkNWcXH6M29kQMrPKhtlIb6u_9PEcBXHm8M1dF4cnCSPwdYzx7c3BpnKmybEqFdSn2wJxohle2ZccvitkQPtOR_VTDBcxZSbP8t6zTmOPer2Hc7wn-s1r9v7D6pJJPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از تقابل حساس سلسائو با یاران اسکات مک‌تامینی تا جدال ژرمن‌ها با اکوادور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24257" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24256">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0Ov6TVE9DhAMnqNPRu_oYXKCyzb8c1UdgDnuoD5pjW27UtzPNrGoahaE6IDNxemmL6uFb-RbLJGK_yfewnJnP9JbVvEbzbXh6ZS41hKDkpZzwtWNNQP1YO_VOzdYFP1vmX0z5vNCfRikUW37_leLIHGsXNjz6720hEYuxBomyASJ3mxinJ673-_8dJwa4AXbRqtWPv9OcBFC9ljbIt0e51QckkBM3nj6Ra-kgGfjHDMQvssPBPcXRlR3SKIdq8l4ATUMJW-P8cc7dg3KiugjRhvoryaxSpICgvZJSoIZQJFT3OWyYFk2rM0DSsUIYhe1OfzI_TantmJ-tY7EwKmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌یاران لوکا مودریچ برابر پاناما تا صعودچهار تیم کلمبیا، سوئیس، کانادا و بوسنی به دور حذفی رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24256" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24254">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6LziwJ8DJbdgld7Q3q3AHYmvu5LUlc1tOETncOqX5IeZwe6aQRCnGUDEpM64PyW2YorJW95K25gSbPSxMjwVVjzxn8mX_W4vE-qgBkPuoBapTGPKbxQc4W-_D4ERcvb0JRkA6mFyTFQmC3hUfBS5zHCVz1ztRmMnEQczqC-A09PTlHFqvk-_NfB3gWeR1Eb4p3UuZhl_H8FwFN6ngNn5ebO_MrixdT2wrlM2M2VWGodlK_7Xa4rKcYu2iduavdy21OO-DO2OfopQNA0z5pBFeoWORcm7r2-evD5fBFiTqySzOdZK8FP-13vvpJPcST-5cDekGGExDOzsJTgVm44ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vPi8MicrJHu_QKDfSq8d-yzM3e1OsmHUDvMjCyRvEJm5Fsk9THBfVvGmBa4-BTwtrNyt7N4cAdOLxNdUKVq9ie_LLYy8qLds0rYcM_Fj5nFpPbHhPn2Btyr4XmEbYNDu1oFOrfY0EOWDhSeBwGN9_bgdf3CkUS8Q9ze0pbdZdHs0zzxoOAUkwS20MeEpl0kEiV2ABnUIVAODc4O_8VyNVmYox5aTeVQyZMKmLUdKPFXVwNHJ7DK8mbtcvnFJhd8LN5VCH8Ucyni_Uc0xqipLMnP1TYyq8ny2x5cVguhsO8jN9y5LkTdYNaHo-vA89WrdPS29PJ_UVRvMD91B9wBBLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر گابریل مارتینی ستاره تیم ملی برزیل که آماده دیدار امشب مقابل اسکاتلنده. جالبههه بدونید که همسر مارتینی پزشکان زنان است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24254" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24253">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ndsr6avApxlURDVuZCesM8ucJ30Wv_99qmBoV4LRvcNTvcmZgWCW-N-A9GBYOjqUExT73NKfyoN89y7aagk8pn2yJILwSyv2KLxtCA-BzOI3TJDzaoIxy2jJpfafy_S8mvZzkHmNgvtqMgHuJbaOruhfaJmgMM6JLmzMkgAW7HGAkdwGSyGjM755o_SY0Y2mckSP-LJgdsJ04XeMraoxii-fWVmpekakmlxrnruVU1Tl3AQu7aKibP5NMA3rTC9KMIs3bdq9Lk4kaLiCPs6L17F6xTYxAqJMiMT-xMHNu9mWMdw85lGIg1aONi_Kb6HjdJYr0mDuNsSG4O5sJbV--A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24253" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24251">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QNsdHvc4PAk_tzVqCWT7IGNx6gYdROxgsbLprLUY4CIz1sbhiO_6NcJQc1-5gl64t3eg0us90i6nlH0UmYNMI_RlYUzFSuLKH7AWtE9rahJ2cmXl4U6rE13YbMe7feIu_tWerkPSL7w6ci_SmkqEPQU7JRqgmZwenaW0IlrAOFR9yXYMXcb-tSokU8lQApT3J5JQ5GZKrTqRZCRBvLYKlQ1VK3cl9LpWZPZkKvl3C9KxdCjkuUl7EUjg3PsngCTyQsqRpHkTK3_ypqSFmha-E4sZP9V7s25kp4YzmhVb22wv2v0Ppd-Q6JRBVHav-GCsgEWTAaTZ1hXPx4dIdqzVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی برای دیدار با فرانسه؛ ساعت 22:00 از پرشیانا سه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24251" target="_blank">📅 00:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24250">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgXVmd57ovxcj1_3_447tNNIWpRmN7OkuIByQHoYoDQa3iE-wphrHf9IC2en14yXnktZ2d0BVY3nAfYPbRZwL_qG4jVDNy0hJpezb0ERfT1DuwLq4hxonjJqFqxX3xx_Zkf7aQCaFPDkO-lyynCCHmHGKYCAMZ0snd_dVsyzSwV8tFVkQvaT_ri3zJ12HNYp5ZARuJcwLIjRHL6XUgXtffLPKbqdbWqCUvL5NpkNJxysNxt5AszPD6mMzImW5jPYuptBd-vvJnaarHxpjWmgpzpI7cot1Tj2w-TfHYEnyG56Ne9pRa-dcLVcQFHmlrMC9QtqfOrlpaA1Auv9VRckAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌جهانی2026؛ شماتیک‌ترکیب تیم ملی برزیل برای‌دیدارمقابل اسکاتلند؛ ساعت 01:30
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24250" target="_blank">📅 00:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24249">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C73SjRaSB2enVw0b4pj0-ZwBbO_TFhta2Lx6_qVslzfEbYlfk9tWzFVLIfpxxpuNgjMuvegiRq-ocVoH6iJUvMAA__ArB6jBVelkVDcVLYvDpgif-iT2rB48jNF8G16fJ4NkLfx1RlaNnjaRs-GKx79gM9G0R-J73dzx2iAO7Saoh7hrytZ5av1vb_xxynBlConYTvldFoTIe4gdshRexiTEIVgPFzzqxNNUups4U-kqD3tXd3KNlR4eK4NNJJiYKTK15oUjNtNx-qvsXrlWsA0W4zEXKTPdgLw-ZLrEWXFAvo95QX4MiHKB4uymDUbOuBRRfOjNM9RqRuhuRAJV5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24249" target="_blank">📅 00:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24248">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=mcgvzJrfuFE_4tjYHIS7fGuEbAPe8geTV2jdOjmpoEty0atL1dONqUFjkzVdQRgMhi6jy0XlRw6jkAH_JrnVimMRQ8qe1J69fUf4-u6kGIejs9FtcMApt9ul4NMbNBbMHj5JMtWHn3k8awlYSlK6X4_VRHtm_VQaYNfSmQugsrGNP5C1b-qZj8J8PxNHkyholjSmnP7TksqWoEgq9MFuIKhrDPKUpoXJ566vApA8tZ8sySP_Rh6VpEkZ8NRQQJTWXbsRurpY4BDlA6IOrnEdE8j7PYuMaRYMG69d969drT9OWcfV4nX15iXC6tmwPAn_eIAJ9hIKwip24l3EGZSa2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=mcgvzJrfuFE_4tjYHIS7fGuEbAPe8geTV2jdOjmpoEty0atL1dONqUFjkzVdQRgMhi6jy0XlRw6jkAH_JrnVimMRQ8qe1J69fUf4-u6kGIejs9FtcMApt9ul4NMbNBbMHj5JMtWHn3k8awlYSlK6X4_VRHtm_VQaYNfSmQugsrGNP5C1b-qZj8J8PxNHkyholjSmnP7TksqWoEgq9MFuIKhrDPKUpoXJ566vApA8tZ8sySP_Rh6VpEkZ8NRQQJTWXbsRurpY4BDlA6IOrnEdE8j7PYuMaRYMG69d969drT9OWcfV4nX15iXC6tmwPAn_eIAJ9hIKwip24l3EGZSa2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏میگویند کیروش باعث‌شد فوتبال‌ما تدافعی شود. مگر قبل از کیروش فوتبال ایران چه آش دهن‌ سوزی بود که نگران دفاعی‌ شدنش هستید ؟ تیمی که حتی دو دوره متوالی نمی‌توانست به جام جهانی برود و در گروهی مقدماتی‌جام‌جهانی ۲۰۱۰ پایین‌تراز کره شمالی و عربستان قرارداشت…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24248" target="_blank">📅 00:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H2M_trIlmFoV0j3MnRs8oQB0LH7-HF-QGREFnL_XO_RexckwEFvWG9D2fQ7G2eaxNFcx_DZPoNgQeXg4tqkqwYaHs3Gtmcou35kNa1xfM6ojaThtoOR_Jmr7EuWH1jHdhNnJekRbOgE3f7Nx9IWJti6eIIpVd0jXBAgwa3Q2akBqah0waBie_Mk7g_3Gqg5_GgtLPpUdReH5869YpoSJbG8fN3v3001-fwKNtW2rWP1VfUE6CCn0TwZmzwdAQyEdv0JyKXteOrOUABSFIsaZay79l92VpTtWCHyjFn0lHnPWZZ-jREeJaJL9rUrKCQB_M4pSVcNILIey3vqAwdiP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با اعلام کادرپزشکی تیم ملی برزیل؛ نیمار جونیور از هفته سوم جام جهانی میتونه برای سلسائو به میدان بره و مقابل اسکاتلند بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24247" target="_blank">📅 00:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3kkSpjoJs5uldFVxnju_7MW43oThwz0JPzBLqkJiEWgiBIqStonPRrNnphxY71_sUNnJbXyb_fcEu2oF2G00dDBaLSBuJlKbbuMvaWvOc9goqHWY8XlcOhaGV20UDSxzCQZurc-SaNI0kCG50QO1h0d9GK5J4_MLLBOXf4T6RVYhRhk4hzTXc1L9_xFT8ZFlZNwLBiJqtHhJdh439-pSrCoennNA-2c8vzZBVcD2eMGkG4TUM02-LDbdHJJW5ANsHMEpgz0pbGCPrIfJLMPsP71kIn7VAKUgnHdxw3tSYxuQf9nfnuDqKcwbRqRoTDiI0W_-xBGA3W3-gbsORq5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇬🇭
#تکمیلی؛ عملکرد کارلوس کی‌روش در تیم‌ ملی غنا؛ پیش‌ازجام‌جهانی‌تموم بازی‌های دوستانه رو واگذارکرده‌بود امادرجام‌جهانی و درگروهی‌که دو ابر قدرت فوتبال‌اروپا توش حضور دارند دو کلین شیت کرده و باچهار امتیاز در صدرجدول گروه قرار داره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24246" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mqo7dPrwRlwDlN-qgAKnYzCD-K-YxNwuuV7xFS0BvdKdfMZ_rOpKlddxs-IqySI2_DjEzt7rEW6OoqyheZoyUmAj8mCpyJs-doDTS2n9JY7Lnhs7N_VsceGXXOnv7XEqnhgPzey9UC8y0NWERXPeWfKoJ3uKGQQrnmgNoP_DALy3zGgQLeCQSKqpLWubmPz6WkZnLq-7HrtRzpbVP2BMRNRJt9MSx3ziBfuKimU-dwuV4JV9Z8YjWE4Fk3H52u1O07fqBojSlMkde4wE8FN4Hx04yUp2DEaw3F_nCOp2wlquKLzb04_vzGEIdH-t11Vf7KJkKBcIhGk2X31whRUFgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛
محمدرضا آزادی از سه باشگاه گل گهر سیرجان، فولاد خوزستان و نساجی پیشنهاد رسمی دریافت کرده و درصورت موافقت سهراب بختیاری زاده از جمع آبی‌ها جدا میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24245" target="_blank">📅 23:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/na_JienphgB5JMxNvGv69zoQhfOPc3C4spIRBu-FkDX4xKOEKnpKd1tvOO0EBke-1Gox8QNZA4R42ILq_JqxEHIHjbl416x6__-F4sPWYI-JT47Lkw7OHgSkYonrXmEW3wCGVvYA0rj1l0PS5ng_VJWzOL8z6vMgRcltFInO05YRef0Hwoq639r6AI7UBzl8TOlHV5lG_-HAsL5LbNXbP_nEaXVYT4UeCPiFvxHwAkFq-4tS_mJMq89IP1HRgPfC8vy08HLJBlCxYTh4L9-l_QqVsNhdURRtYRnx_N1LzeCMzSeVEvCbYckxy-zjYM2baVVBp3jazAMslAiSmx-MCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستررسمی‌باشگاه‌کوردستانی دهوک عراق برای یحیی گلمحمدی سرمربی ایرانی و جدید این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24244" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hkp5ojnQeUuhX4XtRPbaIWuhfDCmmRyW7sw3CJg21Z7bEOQbTwTsAi5FedwhahB1DNAkZLJIBPgZmqCgfpFizH1vhYdEfcbE9uunp0WJMoVMmvly3BmTQQsvQiWRgl7OcL5SVsdnFQozSNQ2zK_LoLC5Ts1S-QxGG_0aI6ky7D5AdNpR2v8NOR9Y1pKu3Ww8qrINnci7ep5eXMHXu1qrxyu_CckutMlRfo6SU7KjtqOqF7bi8YIXXAaGZTSTfKRakQSGAXdXohhR4O_3HKd9P69ZLVUedckn8Lr3hiZyTtWhfEc5YoDTPMFZW4bH54rbFcG_rNOyb9xazqZz3iRPZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24243" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📹
این چه سمی بود دیدم؛
رونالدو، یامال و هالند درمدارس هند؛ ارزش دانلود 100000 از 10
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24242" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hwEWgmCwvr-bvcn6nfGvPAH_-VvHM8zUDOPEUkG2sO-x78vPOw_DM2478sdBag_skkkQkeJQNVmuwix_RAZuKKOz-r1O9irWxyVZ5g5miUOZwCgwLTidNeBtvXOgDhJeI4-TZx-yWcCr4QCmDO8i7XioH8cwCfCJ4nh724avX3uYw_yKrQE4_OShQ2OIqYQJt5XwBDOpXVrxAar1gIgA0Jqw-RifQYRwLJiufhxKLywY28yGldgWjzEgYsFUw4J34Gmsz5_RrxwNxO_p2LtMyflxM61XHwKkzPsFjfLTvOpGEKPtJoLLqP58NxfQQ65ubgE8BPsRmPueJ708IwWrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24241" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ef6iaM33ARa1n48LArXOki_dMw2guSX-ZughQn5n98hejCOxp2h-obv_eiJnkplLXRbXu4wXXOSwTqfP08fAmYqLvxMR5JPELiSoMuIKih5utIUfhOtwjeseb-a5Da_2ykRo8eJ8Kvr-v6EcHHUS7Zvi2awMeMRg41b_tEhwfz31fDRdGVn5mUs6yGdZcmIKHNuVyjfslXySHhbRNFSIZqbF_vqhQf6_hCmEyVlqtFwHyN3ZZx9iVhzDCMKvZCtXCU1E5qpGsL_kWg7ByLACoqT03mHuhAEaxcvBTTar7g0wldQRIgIzeWl44T5WpgG5gaGwQkDAwmAiTd9bJYG-sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g7rjw2nzdelm8eAqs1BgoogXqHTgdlL-kSD0joKsAKTSg2u3tiMjoDM-C_czWYmMqQtlMNHLHLrlWenGAlAhzTUn36FcwayQcBbXG2LlUv5HRI3iRHv-ySr-k351q4s4k4l6Zl2fysR-NEmWObJ2_HaKGvvDLF_ZgM6SbV41q1ixokrUiWMn4P91pbj4tcTbRpBGe1ANPmvSJo0yH0M-_cK65cAATaHUxU7f8uTQphHB_srKhhqYRosAWOeB9utUF5DUA8TF551cfmafy2NeWa3r3pnposCIDlFbkV0d-pYWUjL4pwgKlp18JjlbHkGUBWyPiIw6NKBVJW1NoxJO_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24239" target="_blank">📅 22:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=biBoPXUV1FgjAprtQUtEqnHVBXvTNGFL_Bkgw8X8ybrgEwyCfUUI6UO2A3DhlNqYAuBOoSoHyWvPqEX_2n7Nqqzuvy-mBwmHzt7vkjkb-5HI5iFYHsb3d6Eb9j18njul-YppYLusMjYdK9F0yzpsrdNs2n76BNfDVH7HCMkaz4SwuCHtRwIA7ZKzRRVeiqk98tmnwSuerThUTH0Y7i9iCxy2g4_xYFcZKgLpR-hxf5mUG7DJJVlBL9_1YdydHRVXNzN7qq2iNayEGAcQ6mRDgpjVgmrNF7RoJyGwWc3e-xMRfA1NftyUO6VcNwPK7AItu5Dwn_xjjriO4JnpeYo7aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=biBoPXUV1FgjAprtQUtEqnHVBXvTNGFL_Bkgw8X8ybrgEwyCfUUI6UO2A3DhlNqYAuBOoSoHyWvPqEX_2n7Nqqzuvy-mBwmHzt7vkjkb-5HI5iFYHsb3d6Eb9j18njul-YppYLusMjYdK9F0yzpsrdNs2n76BNfDVH7HCMkaz4SwuCHtRwIA7ZKzRRVeiqk98tmnwSuerThUTH0Y7i9iCxy2g4_xYFcZKgLpR-hxf5mUG7DJJVlBL9_1YdydHRVXNzN7qq2iNayEGAcQ6mRDgpjVgmrNF7RoJyGwWc3e-xMRfA1NftyUO6VcNwPK7AItu5Dwn_xjjriO4JnpeYo7aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب که لامین یامال ستاره اسپانیایی باشگاه‌بارسا امروز داداش کوچیک ترش منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24238" target="_blank">📅 22:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ue3W7yd6Kj8zfbT0SWbVhhxiZ2ns5AVOf30nkS-jo7JCg-yWRt6vpdV0IxOHPW7b5qw04p1j3vAb9jr46twk31WqR3BlQYTsaFCeCHxZ2qTrpaawUl0eY8PKKwS_-h89x9LD7jBota_bwMyFT-k7LOMdarctgrcK_6X1WtwOALwM7CROaUikUpJT55dr3Os196N49uFwXVT6nJ4P08yAIdoZpzJ_wqI7mk4GKfPgIFrZIaVIYH8huXCAby5MWzcq4XhbYMiP1eRxi9K0UCtDzCjqav26a4KqxLhcZ9dJxJT9kivoYfvPyyGIbfz4wn89ouDno7PmsGcrdNIEJBFqNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24237" target="_blank">📅 21:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZXDzJgBWD-WW6fUc7QimK6ZI9EwY8rayewMJ2HuOZ63TL8OOCVUVoqRxtlXD2djowyZdPPvNeTrg2t0DbhS3C7xdy9i1ZuXlCDTJhgm9PxUQC7Gt1hEV3PLZvQyu4rWUuQ0FDPxaqLeYDyfTytr7yyiZMuiCIgeuwqSvy6Yo3ivsCgL4dRMnw88G6y4pqFGe6K1riBZJ9UlCEEodWg79VGFLh8TxN2Va4C-rn2AQsVVATjjnX3Hqc95w77WoNpd4_qSNO2EdjAv-hcysh2_Yj3llEpWExVL00ZXuHHaZ0DQO8e4RiOo10t1t7bU_kwkP27HTZJ6-bbPLB4xsq5VxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌طارمی و سعیدالهویی، مربی تیم ایران به محض ورود به فرودگاه سیاتل آمریکا توسط پلیس بازداشت شده و هم‌اکنون در حال بازجویی هستند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24236" target="_blank">📅 21:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ka4vrTISVK9hL5mD4hu7hZyLHvXfovq60YvasUUft2kcEEdsRcCkh7KszoQYYwsAWiPdGfaZFbEJvny-g3j3Ab6lkBZHnrNuFl1gofU1GwseSRWgVxeW5_eem2pmaokqmrvLITr-5G4pMAx0YQNTtLHMs2c9LPSZ6KVHknmmEfZehYRcub5V0x9cg4HZLbl2nRwbhZyoHkAcKEATV7Nqqw-va5bLo4fPmMWcGOIOAo_OLOCumbdX9hpPK8vJ4D6hh5zUGV9dZq9BaKxkyQCQajuWwFOr5drFkuNlQD3XJ6t7wqQX4aFr6GJD-lXuhL19NL7LkgUeiSzRcrgYWxp8Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق‌ شنیده‌های‌رسانه‌ پرشیانا؛ مدیریت باشگاه استقلال ساعتی‌قبل به مدیربرنامه سید مجید حسینی اعلام‌کرده‌که درصورتیکه‌خودِ بازیکن رضایت نامه‌اش رو از کایسری‌اسپور بگیره و بازیکن آزاد بشه بااو قراردادی به مدت سه سال امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24235" target="_blank">📅 21:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9aKZVq5XtYyznWWUb-Sxy3xuHBM__PIes987dQh0CiSNE_txJ_bhFNeNZ__vdbjxuHCEZoof50SfidnSDAjWljeTCTSytC3q8qee-AhKYR0FJNtIW-wbLkKOVQw3Ph2g8BdxBxUbCEXEoYspNOVPYfh_xl_ITbIygpn3tJQAoKld-6ydWGNKTObQjIUqMij5gQjD0g0bPweQzSxd0GpacrpSydYqmyf3X6UUpZGP_TRDuUMvwHssqCLfTrdLii97eRVYn9Hah5vdm4poA-scHZm4CHAzctvREyPipENceSUWw0CbAFGxR1GMhYu_d5T4hyJ3MqqnFe5boft5VFEbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇵🇹
ژوزه مورینیو سرمربی جدید رئال مادرید:
رئال‌مادریدبهترین‌باشگاه‌دنیاست و بارسلونا هم بعد از باشگاه‌رئال‌مادرید یکی از بهترین باشگاه‌های دنیاست. درباره کریس رونالدو بارها گفته ام اگه از او متنفرید دوحالت بیشتر نداره یا او تیمتون رو به شدت تحقیر کرده یا از بازیکن مورد علاقه شما خیلی بهتره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24233" target="_blank">📅 20:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5fg2bzJWX7U9_ohwEn00voekNvrV7RMmzUDqC9LPhDBe8w-eZAWRbMaj4zXwWkhZ0l-lGLwvsZxYg2LVVzgyMYuBuZQX8B8-7KOYYqSeWAbo7r51SMMEubrtNcPn1U7EVskFL7IMh4n0GWZZyWUNzbIGACA6PGUg7Lgjx6WwOjkvVzr1Djm1fl6D3oMAxszhYplIG59G19e0As6HIaFROcOPYT97KAvxWlFkmLtplhT2Yt-gusqg_DqH7VU5lczP90Tr5zzc5JlboQ_TkRQPBNp8opENtIQumnBWvLoS2bGZiuFFO9AaPETX8BLSQFa9coyz6WIh0POceUQUmhx5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قاب زیبا از دواسطوره تاریخ فوتبال؛ واقعا هر دو بشدت دوست‌داشتنی و محبوبن. حداقل تو کانال خودمون برای این‌دو و تموم هواداران شون به شدت احترام‌قائلیم و تموم امار و ارقام و ویدیوهاشون رو به‌یک اندازه پوشش میدیم که سوتفاهمی پیش نیاد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24232" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
