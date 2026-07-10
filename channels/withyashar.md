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
<img src="https://cdn4.telesco.pe/file/H4bqKjD4rdv_c84_ZlYevoNSNt5Fbx56UKNzSnNDexAwB1uzk08dXaCerJV5s8WXWYgntjm-lSDZga0IL0uM88ref8ablTkhJ5niu3LgjILmiPhWJma3IlZW1JdByzkdoLOiLWjxuFnTqkmHlkP6djCOtkRxZqMJ6aeQZqRcX4KiVexo6tSTJtjj9sXtGcNm8O0RpXt5vWT3oImsjpRGxbI2Pg47vP5yEQ64ax_UGtGcHvej7wqs3q3GevQ5Mt1jli29MSBRZbOooOIJ4UWWLV-oUj7WJO1kv-MwgXX_xOfFuDljjiFnzQfAA0Zvirb8rGilM5VpxPpqqHc9D78tOA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 362K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 18:56:49</div>
<hr>

<div class="tg-post" id="msg-17306">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbd4b57ad.mp4?token=LTmFWoJ7Gmdht_E4KcGAI2-Z6qBgR1aRfRG9wpziK1OihbLDTje541jt3351WNh6cQWZslJs2uWuLH1J8qSQbeVxVXpIPEVJLGpmTwJYh8p4prFriiobNeUtJ4BKxE-FnxHSmG1WCCVQqgqMZW1N_f9cBS4LQRB9q9Mt7FtrOSNcZFRhlxD-uyByu90QQUX221NcRuff-H2uawzwONoZaK7SEV8K2ADJd9ZfDaw-rFiUoQYGYlYGIJZitdPV43zke8gEUaeWvHccdx4Ip2YbHnyVYSoSab-PhtADIC30q6a0XJiP_a3roES_Kq3cp-NQ0xJgxsX_RFbLZFL03TKGpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbd4b57ad.mp4?token=LTmFWoJ7Gmdht_E4KcGAI2-Z6qBgR1aRfRG9wpziK1OihbLDTje541jt3351WNh6cQWZslJs2uWuLH1J8qSQbeVxVXpIPEVJLGpmTwJYh8p4prFriiobNeUtJ4BKxE-FnxHSmG1WCCVQqgqMZW1N_f9cBS4LQRB9q9Mt7FtrOSNcZFRhlxD-uyByu90QQUX221NcRuff-H2uawzwONoZaK7SEV8K2ADJd9ZfDaw-rFiUoQYGYlYGIJZitdPV43zke8gEUaeWvHccdx4Ip2YbHnyVYSoSab-PhtADIC30q6a0XJiP_a3roES_Kq3cp-NQ0xJgxsX_RFbLZFL03TKGpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای، خسارات ناشی از حمله موشکی اخیر آمریکا به پایگاه موشکی ضدهوایی بوشهر در جنوب ایران را تأیید می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/withyashar/17306" target="_blank">📅 18:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17305">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در مصاحبه‌ای اختصاصی با روزنامه نیویورک پست: «اگه مردم ، امیدوارم دلتان برایم تنگ شود.»
@withyashar</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/withyashar/17305" target="_blank">📅 18:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17304">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سی‌بی‌اس: ونس، ویتکاف و کوشنر در تماس با مقامات قطری در چارچوب تلاش‌ها برای تقویت دیپلماسی با ایران هستند
@withyashar</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/withyashar/17304" target="_blank">📅 18:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17303">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVO_3p3B8Ryv1oshFP7hdESKcNfEQRdkWXWNnDCNlOwCpXKeNSaVSZ3-xkBt_OlzO2I1-E1BXuU2DeL3_EnkEhXvyO9pygESfmc-xM_34pRwRsmOCCDnMOoW5GfNzLtJVmLwsCBGvwJDgb9PRFUrMB7NnrD14XpM8k3whkvU17rIQZl_ahK8-CdHhLQeqZuDvROuXL4_tWhGbAoJ4gy7SDlrW821w-lF_3pO-MF6QC8VvLaEpKjfC-ctkewyoDwSSSzEiCo_058uSIf8K18LRbc4pPGiJYQwhzLr2osefDhGj7dB6MqMBxtZG8CDIhc0e5vAaMaMZnyBpkg8_b6CDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر ماهواره جدیدی که منتشر شده نشان میدهد ناو هواپیمابر جورج بوش و گروه ناوشکنهایش به فاصله(۲۲۰ کیلومتری)  از چابهار قرار گرفته  حتی نزدیک تر از ناو لینکلن
@withyashar</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/withyashar/17303" target="_blank">📅 18:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17302">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/withyashar/17302" target="_blank">📅 18:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17301">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ62biSsUA9_Qy3W8DvoQBiP7zKUn0KStB7PUzGcLcsq1erMiQUKOseV1tNH5U91nbchXqD-VrVEmcRi92jEcUvTlnTK1VF01102ZOU1zZDpfOFqIUhlpyKBT3Iq6BVn2Et3Q0tiLLFWaspikG8TDUnUHQwDfpmWliNRNTtmpnJI1n5rj2MDoQU6tauHkJkkYcoDFng7OIkkdsdQd-CqlAc2FrLRMo-stfNqtcILUI3hSLTb7FTvrIYTcJNXi5OO6oXC_rtRIEBd2MxvodsZuDLZxGChj9958xHJfuWIF7R1X7akLm-k-k1GazF1VBh2vWAhlJZI3yUzuLpUdVgNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهراً پایگاه دریایی ارتش در کنارک هدف حمله قرار گرفته. @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/withyashar/17301" target="_blank">📅 18:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17300">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش تایید نشده شنیده شده ۳ انفجار کنارک  @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/17300" target="_blank">📅 18:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17299">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">زدننننننن
🚨
🚨
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/17299" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17298">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گزارش انفجار بندر عباس
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/withyashar/17298" target="_blank">📅 18:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17297">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/withyashar/17297" target="_blank">📅 18:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17296">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">گزارش تایید نشده شنیده شده ۳ انفجار کنارک
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/17296" target="_blank">📅 18:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17295">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUu7YnF7K7HODRNZ7Q6oMdAw1VAJBta-pGWtEfsym2MMXJ9p5r3T0OowPEcKRO7dGrH06JBiIPXtQmYMYr2E2IXRBK1p6YDcuQZ9SyySXouRhZh0Gz7-GqpnLH4tn0dRDkoYOxFX3JOVo4t4wxvjDRdyBEykkKMOPGY4bvRJOFrjUPgmJ8Qcacz0kKkZII3jSgyqo6elVZ5LJ6jiAuu1GQdT8MlHF2zfWawlCA8DowvvVdgcBHCHEScNJs4b2Ziao-NbF1tQ90udBmlTY-GiGLKHxTGFS86fQ5eJakgC3W2gSbbRpkmhD16a8wa_Cel4es2KWP18w-SZuYzCklBjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد هواپیماهای نیروی هوایی ایالات متحده که امروز در پایگاه هوایی شاهزاده سلطان در عربستان سعودی مستقر هستند، به کمترین میزان خود از زمان آغاز این استقرار در اوایل ماه فوریه رسیده است. آخرین هواپیمای نظارتی E-3 در اوایل این هفته از آنجا خارج شد. در حال حاضر، یک فروند E-11 و ۹ فروند تانکر در آنجا باقی مانده‌اند. به نظر می‌رسد که ارتش ایالات متحده بار دیگر فشار خود را بر ایران افزایش داده است، و به همین دلیل، بسیاری از تجهیزات حیاتی مورد نیاز برای انجام عملیات‌های بزرگ، از این منطقه خارج شده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/17295" target="_blank">📅 18:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17294">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ترامپ: اگر جمهوری اسلامی در ترور من موفق بشه، از قبل دستورالعمل‌هایی گذاشته‌ام و در اون صورت، ایران به هدف شماره یک آمریکا تبدیل خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/withyashar/17294" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17293">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBAsyOOTyn_jiCoehga6J43u_6_WPPE6aUmjrgkjERkduZac-LWMkylu7JaJAw6fTJUwIBhvHfx4n4tWxKXozQRHdIyvmwQRJO4eeaApTECBB4Lvjg6UjxYc0GWA4nFHLZKfwdE87Gp6glPhWzOE4OeLde6MXf_VDkMmmduPQRiy_9ADN0aI9vyTLSlNbC_yZ1TkpNU9eP854dXo5S21iD2DBPVpJIsGiVf1zKa3DK0knX_1KiLdE0lIv06_2WtkU-4cIeSrBKoC5L6EUHoHoZUI8-blHqPeLE_Kryvfnk2aUg_-db5-QjXoofj6t5ZQqvLFHfs9IH6kyOflDjMJ2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ایران از ما خواسته است که به «مذاکرات» ادامه دهیم. ما با این کار موافقت کرده‌ایم،
اما ایالات متحده به صراحت به آنها اعلام کرده است که آتش‌بس پایان یافته است!
از توجه شما به این موضوع متشکرم. رئیس جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/withyashar/17293" target="_blank">📅 18:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17292">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwN_u7LX7pTQCYdDPS7HY9JmyjLoLab1yOwaOqm4ZWCDllFRfZtg3wtZ1QgJ8hLCEHJcUsvk-_aLN0AmxeHQzruaoUuLDNUVtHIm1sH1pUBbVa4HXKS7PP5HPefSm4Imq9TrKwn4n9tYwpXHR1LZszS04i5WzaNCp6OLUhq9Tn4KOm3Z1sesxeiOJDUzsOB95P_6p3fZs7IEU5ies06kYLPcOlSRNBAw_nA65STtXQoWM-LcEg86pPRDgEiNvGWzPFsjz7PShPgSxzJj1MSDH1Z3tJnf3SVWiyAKByCo9AaPyHK2fVZiMafc5sPDUMsAKNO41GdFpaYFbzo90dhf8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق تصاویر ماهواره ای منتشر شده؛ ایران مسیر های منتهی به سایت هسته ای فردو با تپه های خاک مسدود کرده تا مانع حرکت سریع با خودرو به سمت این تاسیسات شود.
@withyashar</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/withyashar/17292" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17291">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9KvzKPaTbqi9eNL_khl0wJYyFitwKo9Uh5hpnO2XOQUTcuIXQAvqxt2XDIXHhQGMh1FkJmfwF-unF3YGXRFg1AxNwLuV4KVMYhISZYa_5d7q-lvTddz4ooI-5ys1fr-_ZSOra8CVgPCJGVqWC15F05FRXNtesOiTYvreUdJFpZtBQGcZsr1tca1rtqyJZ6SbmGSDcRZxf3u4YW3-nKjCLLD-cFkk-zjf2Y3r3TPXxhCYYb6z6ecAMZ2FDahOuSip46kezwFUTx0PaAvGbNe1QRipZDxRBLYwLf4pMn77DD4ny_LgL5A9RHjDGcQaiMxRO5R1OK4L_vHqAv6ytpApQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر‌ ماهواره ای گروه رزمی ناو هواپیمابر آبراهام اینکلن و ناوشکنه های گروه ضربت ناو هواپیمابر ۳ در نزدیکی چابهار که شامل :
* USS Spruance – کلاس آرلی برک (Flight IIA)
* USS O’Kane – کلاس آرلی برک (Flight IIA)
* USS Frank E. Petersen Jr. – کلاس آرلی برک (Flight III)
میشوند
@withyashar</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/withyashar/17291" target="_blank">📅 18:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17290">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بازهم روسیه و چین با طرح بحث درباره برنامه هسته‌ای ایران در شورای امنیت سازمان ملل متحد مخالفت کردند.
@withyashar</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/17290" target="_blank">📅 17:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17289">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOR8ijD0rqSh545076G32AtxELtf0nFzKNjsQEzM_ImvzerTOxHji0CR4dh6NFGyaPK3ZfZ1_NAno4GSEoONNHYIfPkI1Sdz3QIIMnGPfTHxE_cfc75mLHLsTvEZzDkHFwpH5_zZH0btWOZZoF_bqu5gKckV2_rWgzTRalDnRDxCmRWgSDrF3DHlzUpkDU1MSMWUg1zc02Xsj2tuRrlc9yMIczdhzvmHlPlt46yzEkJIpJ8xwHFVskMMsiO3IV3hxAM9MV9R1TpgLj6jwB3EnIrdJOtu_EVpc5w2WYdEfTt3BOeMhlBgRWQNPtgVcrSqY7vDxtyk6S9J1vU4gy5MjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناو هواپیمابر آبراهام لینکلن (CVN-72) و چندین ناوشکن مجهز به موشکهای کروز تاماهاک در خلیج عمان، ۲۵۰ کیلومتری چابهار آمداند ، همچنین دو فروند هواپیمای P-8A Poseidon نیروی دریایی ایالات متحده از جیبوتی از صبح امروز در حال اسکورتش‌در این مسیر بودند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/17289" target="_blank">📅 17:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17288">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/withyashar/17288" target="_blank">📅 17:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17287">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تسنیم:یک هیئت قطری به منظور تلاش برای تثبیت جایگاه میانجی‌گری قطر، بعد از حوادث روزهای اخیر به ایران سفر کرده است.
گفته می‌شود هدف اصلی این سفر، تلاش برای تثبیت جایگاه میانجی‌گری قطر، بعد از حوادث روزهای سه شنبه یا پنجشنبه باشد که در جریان آن متعاقب اتهام زنی قطر به ایران در رابطه با یک حادثه ادعایی در تنگه هرمز، ارتش آمریکا حملات گسترده‌ای را طی روزهای چهارشنبه و پنجشنبه علیه مجموعه‌ای از اهداف نظامی و غیرنظامی ایران انجام داد.
@withyashar</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/17287" target="_blank">📅 17:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17286">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خبرگزاری CNN :
دولت ترامپ در حال بررسی آغاز مجدد محاصره دریایی علیه ایران است.
@withyashar</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/17286" target="_blank">📅 17:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17285">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">https://t.me/boost/withyashar</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/17285" target="_blank">📅 17:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17284">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/17284" target="_blank">📅 17:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17283">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ce7bfbd.mp4?token=Ai1qGIeszbZnSKcwdn3d8ob7xQRVFKaERP5g7-BcRLi9PRhhWqUx_mMLqddIBNP9cmbU5CiiqozWB1plpGascFBNAsVBeYd-lfBLR9zhRWNUxZZx5BJ3yPc00IjeCnTI3JkSA2y2wb1nJD2oRQ4Z3Ps67wjCZITJg-Yudp-0YsNE8liTEEi4HMIhWcpledDihV__TUzLeQNloVy6s2m-7sbb1EKp6me4CyzqQSiZLEp1ciBPEi0PuZ2T2iXWiEmloUaCGLQLMIDL1jB_1mrd49awgA8yx-fjuq1jt6F1qy4QVwOyHIIi53pBcY-bUYgJV7M4M_qPMZsr2mO5G-2KWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ce7bfbd.mp4?token=Ai1qGIeszbZnSKcwdn3d8ob7xQRVFKaERP5g7-BcRLi9PRhhWqUx_mMLqddIBNP9cmbU5CiiqozWB1plpGascFBNAsVBeYd-lfBLR9zhRWNUxZZx5BJ3yPc00IjeCnTI3JkSA2y2wb1nJD2oRQ4Z3Ps67wjCZITJg-Yudp-0YsNE8liTEEi4HMIhWcpledDihV__TUzLeQNloVy6s2m-7sbb1EKp6me4CyzqQSiZLEp1ciBPEi0PuZ2T2iXWiEmloUaCGLQLMIDL1jB_1mrd49awgA8yx-fjuq1jt6F1qy4QVwOyHIIi53pBcY-bUYgJV7M4M_qPMZsr2mO5G-2KWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اولین تصاویر از قبر علی خامنه ای
@withyashar</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/withyashar/17283" target="_blank">📅 17:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گیلا گملیل وزیر وزیر علوم، نوآوری و فناوری مصاحبه با اسرائیل هیوم:
"شاهزاده رضا پهلوی و من، «پیمان‌های کوروش» را آماده کرده‌ایم؛ آنها آماده‌ی امضا هستند و نتانیاهو با سقوط رژیم شرور در ایران، این پیمان‌های صلح را به خواست یزدان امضا خواهد کرد.
رژیم ایران درگیر جنگ‌های داخلی است،
و هیچ شکی نیست که این رژیم سقوط خواهد کرد!"
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/17282" target="_blank">📅 16:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17281">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d923ee58.mp4?token=HjAcIMW8QMuPFXhZsPoGFOxP4ltr4UfqFdDfWB-MUiRCgmDwtfyezwaQxI7vE1vdWzuzp_4TYepwaPiQLFV5HaFm3mQvxTq0iJvqENFfxysKXf0rTNNmirtaHmwRa3Rp0EW-KslZ_bqYXu1UskpDb9IUHzdSDzBmONBH5mtnVN1nIbx-mg1DJ38sbg1xiEFhfYg7enP5nqD5_7LBs_kXvOotrPYhWwCLWud5W5KqEMQALJ4HtH_aWDWqQLC0gZfUghXQjgqx5uGB5S1uzeWnDpwBJHmKinPWRWrYkmUVIatE8__i_XbPWwtdANZX86HoEgwMD1fMux62LNzeGZ-BNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d923ee58.mp4?token=HjAcIMW8QMuPFXhZsPoGFOxP4ltr4UfqFdDfWB-MUiRCgmDwtfyezwaQxI7vE1vdWzuzp_4TYepwaPiQLFV5HaFm3mQvxTq0iJvqENFfxysKXf0rTNNmirtaHmwRa3Rp0EW-KslZ_bqYXu1UskpDb9IUHzdSDzBmONBH5mtnVN1nIbx-mg1DJ38sbg1xiEFhfYg7enP5nqD5_7LBs_kXvOotrPYhWwCLWud5W5KqEMQALJ4HtH_aWDWqQLC0gZfUghXQjgqx5uGB5S1uzeWnDpwBJHmKinPWRWrYkmUVIatE8__i_XbPWwtdANZX86HoEgwMD1fMux62LNzeGZ-BNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو آفریقا جنازه خامنه‌ای رو بدین شکل تشییع کردن
@withyashar
🤣</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/17281" target="_blank">📅 16:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17280">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سی‌ان‌ان به نقل از مقامات اسرائیلی:
دولت ترامپ تمایلی نداره که اسرائیل در عملیات نظامی علیه ایران شرکت کنه.
@withyashar</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/withyashar/17280" target="_blank">📅 16:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17279">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرنگار آکسیوس:
به گفته یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و در تلاش برای کاهش تنش‌ها و ایجاد شرایط برای از سرگیری مذاکرات باشند.
این دیپلمات گفت که جلسات در تهران بین مقامات قطری و ایرانی هنوز ادامه دارد «اما واضح است که هر دو طرف می‌خواهند به یادداشت تفاهم بازگردند».
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/17279" target="_blank">📅 16:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17278">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miz0KTB0MD3cNPJa9uzCyjZDV25zUsbJCvl8lxbXfm16wqVMxJ5fgS5HbI0YZkDdJ3a2dHqdV3JjllYJz5UvCfKqr-PUjCPxCfKJaH1PGkaZ-fCYMzoNncv33_Rls7AddBhqoaTjyBLS6dTsalBuTY3K-PZPRhzrrcAprzRozzq0o4k6pZg6ZRuUuiSRZ0n7hYX72RzQ1UdTGDCSaR4hVjDcdqJ_j_eDdgYyANGpAAHvcQzFbinESssDGeMMF5kOZSgxueFAS_KCbSnkmpEqGtGATypzvauFHW_hOHPneU84uWUdI6WBis5T9JfjNbQcAyOcyQx89_HRMjp-AU_iPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همکنون  گزارش های زیاد از ستون دود عظیم تهران فکر میکنم سمت شرق(بزرگراه امام رضا-جاده مشهد)
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/17278" target="_blank">📅 16:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfFb19cjUR9o4aCZBJ_w4lqwp2e9QhcPMCt4m6aZQDrb1pi4aLVqsU2vR8McAALu0bPfdRSdJuKi6MVvyn50dQzHzM2qOuEbthEiJY-_gOD3k85exnQ6bKPhdRd38DDaRMEP_7KcbiQtvg9ASCd84bEbcOAFslOvWS8FaOc461vUXvaPHy2FnJH6whjXJ_Lag0D1q866iLk4dtJ9DdwxtEHDcXX9JBIayuUCfqgauKP4NMP2GxihwP92eQDChciJinTlf2DXpI3qwMNraEuuv13S5abXFnHmYVVD_31obVwDC35sJk98ZfWFaAM_G0Wn_XCOKW3AjszUeJUnW_hS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏دستگیری 8 جوان امریکایی باتهام تلاش برای ترور ونس و ترامپ در هنگام بازی بوکس UFC در محوطه کاخ سفید . این طرح از ماه مه شروع شده بود . یکی از این جوانها    Tycen C. Proper, 19, of Danville,  تایسون کوپر 19 ساله هست و عضو گروه ازادی 250 سال -هست . این طرح خیلی خام بوده . امنیتی ها هم اجازه دادند اینها کارهایشان را بکنند 4 روز قبل از مراسم ، با شواهد دستگیرشان کردند که به ترامپ نشان بدهند تهدید برای وی جدی هست . این 8 نفر از 8 نقطه امریکا بودند
@withyashar
حقیقت یاب اتاق جنگ : خبر پخش شده مبنی بر ترور نرامپ در‌ امروز و دستگیری ۸ نفر فیک نیوز است</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/17277" target="_blank">📅 16:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترور ترامپ</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/17276" target="_blank">📅 16:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17275">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">منابع آمریکایی به شبکه CNN: آمادگی‌ها برای حملات بیشتر به ایران تکمیل شده است. در حال حاضر، واشنگتن فرصت نهایی را برای مذاکرات دیپلماتیک با میانجی‌گری پاکستان و قطر فراهم می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/17275" target="_blank">📅 15:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17274">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">محمد باقر ذوالقدر، دبیر شورای عالی امنیت ملی جمهوری اسلامی هشدار داد اسرائیل پشت این اقدامات خصمانه قرار دارد، آنها از پاسخ ما در امان نخواهد بود. در صورت وقوع حملات اسرائیل به زیرساخت‌هایمان ، انتقام خواهیم گرفت و به آنها حمله خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/17274" target="_blank">📅 15:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH2932qhrBIvQbG-Gg2X_XLQOxF1XLldtxmTJ0lapHM-G_A9gaBKat4yWJsr1llt2LJhOiPMT-d8kDygdW-IrjNBWEmcUQDnFU2Uj5N0crqJWZAkqVw1wkFNa7sQLHh1UM_T5VVyIVmbr4Q4WNsFjq6r0gBDYBemkhOgYaFZEyKJMTZLCL4jGn3v3wX25FB5_4oamoFA73dME6QsiV62LOQX54YKF55WYbovNylFQJlwylbRTGZWp5WOtwYUWGm-OHQpjJvqJ_O_B1XrRrkGZvbgLx8dmAu5wqPzjcJNtmEMsr2XaIwU61AwdAVfUHcYcjzheTQY5jWOw008DEQ15g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۲ فروند اف-۲۲ امروز صبح پایگاه هوایی عوودا اسرائیل را ترک کرده و به بریتانیا بازگشتند (در حین پرواز توسط KC-135R مستقر در رومانی سوخت‌گیری مجدد شدند)
چگونه باید این را تفسیر کنیم؟ فعلا جنگ نمیشه؟ یا محافظت از مهم‌ترین دارایی‌ها قبل از هرگونه حمله بزرگ احتمالی؟ زمان همه چیز را مشخص خواهد کرد..
@withyashar</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/17273" target="_blank">📅 15:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17272">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce7054159d.mp4?token=Qsw12dxvDYIG9StK5MV71qF3gSv79TVWWGhDA6I7DkZS8eUJNX_AHiFUkb2xsdWa-mmkJaGtYqbByDeNDSRVWqDvsfY4XyZ50VqMW9OpAnvVMCQq737PeezhyDmC_b4i1C0sjFtmWNiXXt0X1z7wW34CVGgfF77I8QRcDoZrWq50VrRaRmTH28hf0ozNjqUwtx72KbZgQTOlMlyePuuBk3JPUOmom_zNNOjk6qs8pKUd3DSh2QHhHZhIiMVWtx7nFy_rtllatpeg5JVsstRgC13sorvUhYdqFjXNia3KFC0STnIbQoHxVHMAagFqJOzOTfcKuN4UtBBT-xAjFS80T4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce7054159d.mp4?token=Qsw12dxvDYIG9StK5MV71qF3gSv79TVWWGhDA6I7DkZS8eUJNX_AHiFUkb2xsdWa-mmkJaGtYqbByDeNDSRVWqDvsfY4XyZ50VqMW9OpAnvVMCQq737PeezhyDmC_b4i1C0sjFtmWNiXXt0X1z7wW34CVGgfF77I8QRcDoZrWq50VrRaRmTH28hf0ozNjqUwtx72KbZgQTOlMlyePuuBk3JPUOmom_zNNOjk6qs8pKUd3DSh2QHhHZhIiMVWtx7nFy_rtllatpeg5JVsstRgC13sorvUhYdqFjXNia3KFC0STnIbQoHxVHMAagFqJOzOTfcKuN4UtBBT-xAjFS80T4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی مراسم خامنه‌ای در قم یکی از محافظان سعی داشت مثل اسپایدرمن، جلوی ماشینی که تابوب خامنه‌ای رو حمل میکرد، بگیره
@withyashar
😂</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17272" target="_blank">📅 15:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17271">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به‌گزارش یسرائیل هیوم، دونالد ترامپ به‌دلیل نگرانی از کاهش شدید محبوبیت خود در آستانه انتخابات میان‌دوره‌ای، قصد ندارد جنگ با ایران را ازسر بگیرد.
@withyashar</div>
<div class="tg-footer">👁️ 92.5K · <a href="https://t.me/withyashar/17271" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17270">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وزیر خارجه ترکیه: آتش‌بس میان ایران و آمریکا پایان نیافته است /دو طرف واقعاً می‌خواهند به سوی یک توافق صلح‌آمیز پیش بروند /امروز با همتای ایرانی‌ام تماس داشتم و آنچه رخ داد، سوءتفاهمی درباره سازوکار عبور از تنگه هرمز بود
@withyashar</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/17270" target="_blank">📅 14:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17269">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2511809773.mp4?token=YfGrYkhj9zqI5XxCUnBEZcWS6-DGexpMeEgqhWZryOjDLG7mcJzwBKsEQWMJ2ElLJpGXRqoiuhiKfwO9SrOgLL_1RBGUsXcBPfozc_i9jIKQPbkbbpHptyFodasoKk-L8_6rdz561p6AWEh3RfLeL-tThTRq3QM2puonUsLa30sR6UyuibKBLhbMUvHbsRzxc_6QkGPVjFuQy6Pad-VnuupkqDcK9c-lDtSc_jHnwHHCvNN5Tt309rMeHLfkfMUkJqgYbAFBLwJUIPL5ts2L0cVX51vBCdvq0Fd4dpz0q3WkewpXKu0nVvvpxFgjA9647uHt0WeuoP_EceKbzkrYgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2511809773.mp4?token=YfGrYkhj9zqI5XxCUnBEZcWS6-DGexpMeEgqhWZryOjDLG7mcJzwBKsEQWMJ2ElLJpGXRqoiuhiKfwO9SrOgLL_1RBGUsXcBPfozc_i9jIKQPbkbbpHptyFodasoKk-L8_6rdz561p6AWEh3RfLeL-tThTRq3QM2puonUsLa30sR6UyuibKBLhbMUvHbsRzxc_6QkGPVjFuQy6Pad-VnuupkqDcK9c-lDtSc_jHnwHHCvNN5Tt309rMeHLfkfMUkJqgYbAFBLwJUIPL5ts2L0cVX51vBCdvq0Fd4dpz0q3WkewpXKu0nVvvpxFgjA9647uHt0WeuoP_EceKbzkrYgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سخنگوی ارتش اسرائیل اعلام کرد یحیی سعید محمد حمدان، فرمانده تروریست یک تیم «نخبه» در شاخه نظامی سازمان تروریستی حماس، در حمله‌ای هوایی در جنوب نوار غزه به هلاکت رسیده است
.
او در حمله ۷ اکتبر به پایگاه رعیم مشارکت داشت و طی هفته‌های اخیر نیز برای طراحی حملات تروریستی علیه نیروهای ارتش اسرائیل و بازسازی توانمندی‌های حماس تلاش می‌کرد.
@withyashar</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17269" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">کارخانه فولکس‌واگن در ولفسبورگ در معرض خطر تعطیلی و صدها کارمند در معرض اخراج قرار دارند، زیرا صندوق سرمایه‌گذاری قطر، از توافقی بین این کارخانه و شرکت رفا جلوگیری کرده است. این توافق برای تولید قطعات مورد نیاز برای سیستم دفاعی "گنبد آهنین" بود. صندوق سرمایه‌گذاری قطر، سومین سهامدار بزرگ فولکس‌واگن است و با اعمال حق وتو، از انجام این معامله با رفا جلوگیری کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/17268" target="_blank">📅 14:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17267">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سی ان ان:اوضاع به شدت متغیر است؛ احتمال از سرگیری گفتگو ها وجود دارد اما احتمال جنگ هم همینطور
فرمانده ناو هواپیمابر آبراهام لینکلن در دریای عرب به خدمه خود دستور داده است که آمادگی خود را حفظ کنند و منتظر هر دستوری باشن
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/17267" target="_blank">📅 14:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">جواد لاریجانی : باید لیست افرادی که در ترور رهبری دست داشتند را صادر و اعلام کنیم که از نظر ما مهدورالدم هستند
این جنگ به پایان نمی رسد مگر انتقام گرفته شود.
@withyashar</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/17266" target="_blank">📅 14:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کانال 14 اسرائیل: اگر مجتبی زنده باشه از ناحیه دو پا آسیب جدی دیده و روی صندلی چرخداره، به همین دلیل مقامات نمیتونن اونو در انظار عمومی نشون بدن
@withyashar
یاشار : اینو خوب گفت
😂
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/17265" target="_blank">📅 14:04 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17264">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">با تمام حالات چراغ اتاق جنگ امشب روشنه و ما امشب رو بیدارم
🙌🏾
همیشه احتمال هست مخصوصا وسط مذاکرات اینشکلی اونم اخر هفته که مارکت بسته میشه</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/17264" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17263">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اکسیوس:  ایران و آمریکا از طریق میانجی‌ها توافق کردن فعلاً به همدیگه حمله نکنن و برای حل اختلاف‌هاشون، به‌خصوص درباره تنگه هرمز، دوباره پای میز مذاکره برن
@withyashar</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/17263" target="_blank">📅 13:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17262">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بابک زنجانی: در خصوص (راه آهن) آق قلا حرف و حدیث‌هایی از خرابکاری به جای حمله دشمن البته وجود دارد.
@withyashar</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/17262" target="_blank">📅 13:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17261">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">@withyashar
امتحانات ۲</div>
<div class="tg-footer">👁️ 94.5K · <a href="https://t.me/withyashar/17261" target="_blank">📅 13:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17260">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اتاق جنگ با یاشار : عمو اگه امتحان دار‌ی خواهش میکنم درست رو بخون
🙌🏾
این خودش ضد خواسته رژیمه اونا میخوان تو بیسواد باشی ، این خودش گارد جاویدان بودنه ، ترس رو تو وجودت راه نده سنگر رو نگهدار ، ترمیناتور باش مثل شیررررر باش نسل بعدی ما نباید روح و روان خراب…</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/17260" target="_blank">📅 13:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17259">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">زیرنویس شبکه خبر: ازمون های نهایی بدون تغییر و طبق برنامه ابلاغی از 21 تیر شروع میشه @withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/17259" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17258">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یکی از کشته های تیراندازی در مشهد
🚨
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.7K · <a href="https://t.me/withyashar/17258" target="_blank">📅 13:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17257">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسرائیل‌هیوم گزارش داد آمریکا، اسرائیل و برخی کشورهای منطقه در حال بررسی گزینه‌های سرنگونی جمهوری اسلامی هستن
و ازسرگیری هرچه سریع‌تر محاصره اقتصادی ایران رو یکی از راه‌های رسیدن به این هدف می‌دانند
یکی از مقام‌هایی که اسرائیل‌هیوم اونو آگاه از تحولات داخلی ایران معرفی کرده، گفته اختلافات داخلی در جمهوری اسلامی تشدید شده و سپاه ممکنه کنترل رهبری غیرنظامی رو در دست بگیرد
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17257" target="_blank">📅 13:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17256">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نیویرک تایمز : محدودیت‌های تصاویر ماهواره‌ای ایالات متحده، روزنامه‌نگاران را در پوشش جنگ ایران با مشکل مواجه کرده است. اما منابع دیگر راه‌حل‌هایی ارائه می‌دهند که پنهان کردن اقدامات ارتش‌ها را دشوارتر می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/17256" target="_blank">📅 13:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17255">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بلومبرگ: روسیه به دلیل فروش نفت در جریان جنگ ایران، کسری بودجه نادر خود را جبران کرد
پس از امضای تفاهم‌نامه بین ایران و آمریکا قیمت نفت خام روسیه از ۸۶.۵۲ دلار در ماه مه به ۶۳.۵۲ دلار در هر بشکه کاهش یافت
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17255" target="_blank">📅 12:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17254">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTFSE8OAO1GZD_6CFrFBXdoOW9UMMQmglaooR6YXOipPBdimZuzCJqCy4pcfT-9kAdlV9-fmdGNrSRVTdNJJnYc-JgAI-7KteAhF7cmqrX2Nyqv30wrE7Jx8IKIN-W4i5e8yLgXePa8CYFhxzFsa7Le2srDj29ApEUmDfdqSpbj4NPhOAhG6ITaJJarqTuhtB5mzjpUM3jazlKNPHqIFXgjbjH8GahiMerl8K_AWDD-3qtBTIrySw4_YCm9auj-Cu56m-S4WLh8zcrjhAtnWLA_7Z1tCz7yt-_xDpZEawcCGj7jwJpA4DgQIFSZnTqDWUYu-hiI-HMC1g11hcVb-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیرنویس شبکه خبر: ازمون های نهایی بدون تغییر و طبق برنامه ابلاغی از 21 تیر شروع میشه
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17254" target="_blank">📅 12:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17253">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سیتی ژورنال: وزارت خارجه آمریکا جلوی دیدار مقام ارشد تیم زهران ممدانی با سفیر ایران در سازمان ملل را گرفت
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17253" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17252">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترکیه برای دریافت جنگنده F35 آمریکا، پدافند های S400 روسی خود را فروخت منابع ترکیه‌ای مدعی هستند که ترکیه سامانه‌های دفاع هوایی اس۴۰۰ ساخت روسیه را به یک کشور ثالث فروخته است و نام کشور امروز اعلام خواهد شد. پیشتر آمریکا به عنوان شرط فروش F35 به ترکیه اعلام…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17252" target="_blank">📅 12:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17251">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رویترز: جنگ ایران، جهان را تا آستانه یک بحران غذایی پیش برد
درگیری بعدی در خلیج فارس نیز می‌تواند همین پیامد را داشته باشد.
کشاورزی مدرن به کودهای شیمیایی ارزان‌ قیمت وابسته است. این جنگ با گرفتار شدن کشتی‌ها، تعطیلی کارخانه‌های تولید کود، هراس کشاورزان و افزایش شدید بهای کودهای شیمیایی، تولید جهانی غذا را در معرض خطری جدی قرار داد
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17251" target="_blank">📅 11:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17250">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سی‌ان‌ان به نقل از یک مسئول آمریکایی: واشنگتن عمداً حملات متناوب را انجام می‌دهد و سپس متوقف می‌شود تا از تشدید تنش‌ها جلوگیری کند و فرصتی برای دیپلماسی فراهم شود.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17250" target="_blank">📅 11:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17249">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJ_igjkJp6UfhXMgjllDXBMvAj-tLvRkqGALozVzOaBOwybYhwTjTegZVnBJ0_CltwqpqPg3Ibm_feufjQszyqA3ix8wDxk8zZZjQD8N4pN2TtRxtQdTd8zjcZT_V4TlI0HaQVinprLIE7QoQRjEeFApt4xyZcsEwhoIHqcWadkS_1BxnoBoEgzZheVMZhB3IpsvA-pdQmz6LWx-KWxY88BdqlM_F9xTOeCLkRKO8YpeKw77Ur3O6hLuqe9J97lAm60TRqarCjr65k_-Dq2gNUodzPo_VfMcteiPpYxpf3hT9yooC6oWuaT61DRzypkwPU-k5eo2gWODModRo-Ep6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدیه اردوغان به سران کشورهای ناتو که در اجلاس آنکارا شرکت کرده بودند.
@withyashar</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17249" target="_blank">📅 11:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17248">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">یاشار : خیلی از‌ اخبار که امروز پخش میشه من دیشب پست کردم
🤒
قبل فرستادن خبر‌ در ‌دایرکت چنل رو کامل اسکرول کنید و ببینید
😩
❤️‍🩹</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17248" target="_blank">📅 11:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17247">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkXBJTon6Cd9X8CIwNze049INk-enKvrbq-QVD_GohQjW-gxWn5nJqPArRdwtFAp-Vd60o7PcYF1o1d7KatJgKcwm7fx7q62op9sPNII0nnWQIRiSKGDZCXUNzwLZGCP2S9Ksik3gnN5IkROeB_n9V9xJsRQzy996aDPAKG4RPmmkYMAM0KcE-_T35rKPLS5tXe6AxUog87spzUAnTy6Ezu8QfXsmkcGbVg_tqA87IOGr-D_LIZZrG1tuQyR_WUGHGYlXy2eDJ8mqPZOsOyhQe1ey-EpMudIv02DV9u5rew3hjmfYQNWEBxCpxEINpL9pO9NXDFtIivlqK9donoVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ اسرائیل: ایران با جذب شهروندان و اتباع خارجی، اطلاعات و تصاویر مراکز حساس از جمله اطراف وزارت جنگ و مجموعه نظامی‌«کریا» را جمع‌آوری کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17247" target="_blank">📅 11:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17246">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwraGLRofR68gvSatYyiycctgLiGHXsI3KIUAEZkTRmIsqqWiKU79xxcFJ8kAAVnwsYvsedMwGPFI5KRFrppvJ4py7BHqWv89S2htiUwqkSO3LFAVKKu_AJlQ8U2yM6qb_ZAHpGMZ1ix2YwuqnCjYnf758b420q8Bl40nZERPYM9jQ08kJzsxph61MZUfkmo36CAqtUGZD3vkuLDfZb_lGEa6DgW5kQ4aGhFsnd0KjOjymAF0CA4u8W8ZfNHfSvZ5Ua-zWibbmiEXk7pLnGXoz2skMrroW4PtvnZaACTNRBB51GBj3TdOk2D-XBLwMceMMSnLxlFuUlLby_eEikUgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه برای دریافت جنگنده F35 آمریکا، پدافند های S400 روسی خود را فروخت
منابع ترکیه‌ای مدعی هستند که ترکیه سامانه‌های دفاع هوایی اس۴۰۰ ساخت روسیه را به یک کشور ثالث فروخته است و نام کشور امروز اعلام خواهد شد.
پیشتر آمریکا به عنوان شرط فروش F35 به ترکیه اعلام کرده بود که برای خرید F35 باید سامانه های پدافندی S400 روسی را نداشته باشد
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17246" target="_blank">📅 11:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17245">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">شبکه اسرائیلی کان: اسرائیل میخواد به ایران حمله کنه اما منتظر چراغ سبز ترامپه. مقامات در اورشلیم برآورد می‌کنن حملات متقابل میان آمریکا و جمهوری اسلامی در چند روز آینده ادامه پیدا کنه.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17245" target="_blank">📅 11:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17244">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">احمد وحیدی، فرمانده کل سپاه پاسداران، در پیامی به مناسبت خاکسپاری علی خامنه‌ای رهبر پیشین جمهوری اسلامی نوشت خونخواهی علی خامنه‌ای و مجازات عاملان و آمران آن، مطالبه‌ای «قطعی، مشروع و فراموش‌نشدنی» خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17244" target="_blank">📅 11:11 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17243">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ در ‌تروث: امروز روز بسیار مهمی در پالم بیچ، فلوریدا بود، و افتخار بزرگی برای من بود که فرودگاه بین‌المللی پالم بیچ، با رأی قاطع، به نام "فرودگاه بین‌المللی دونالد جی. ترامپ" تغییر نام داد. به زودی این یکی از بزرگترین و باشکوه‌ترین فرودگاه‌های جهان خواهد بود
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17243" target="_blank">📅 10:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17242">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یک مقام آمریکایی: ناو هواپیمابر آبراهام لینکلن در دریای عرب در حالت آماده‌باش کامل قرار گرفته؛ واشنگتن تأکید کرد در صورت لزوم، حملات از سر گرفته خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17242" target="_blank">📅 10:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17241">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الجزیره: تردد کشتیرانی در هرمز به دلیل ازسرگیری درگیری‌های آمریکا و ایران متوقف شده
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17241" target="_blank">📅 10:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17240">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اکسیوس : ایران و امریکا دوباره باهم توافق کردن که همدیگه رو نزنن و فعلا دست نگه دارن.
@withyashar</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17240" target="_blank">📅 10:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">lسی‌ان‌ان به نقل از مقامات آمریکایی ادعا کرد: در صورت نیاز
،همکنون مقدمات حمله به ایران در حال انجام است، اما تمرکز در حال حاضر بر دیپلماسی است.
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17239" target="_blank">📅 10:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17238">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">وال استریت ژورنال : ایران قصد داشته تو ترکیه، ترامپ ترور کنه که نتانیاهو میفهمه و سریع اطلاع میده
همین باعث میشه ترامپ عصبی بشه و تنش ها شکل بگیره
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17238" target="_blank">📅 10:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17237">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">خبرنگار فاکس نیوز: یک مقام آمریکایی به من گفت مذاکرات با ایران در هفته پیش رو ادامه خواهدیافت
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17237" target="_blank">📅 10:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17236">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اکسیوس: ترامپ روز پنجشنبه بعدازظهر با تیم ارشد امنیت ملی خود درباره تنش‌ها با ایران و مسیر پیش‌رو جلسه برگزار کرد
پس از این جلسه، یک مقام آمریکایی گفت دولت ترامپ «همچنان متعهد به یافتن یک راه‌حل است و مذاکرات در سطح فنی برای رسیدن به یک توافق هسته‌ای ادامه دارد.»
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17236" target="_blank">📅 10:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17235">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpmv2l3MsPQiAQ7kyz5XyQ5vH6b3ctSaSZfIfUIRdoZa7IwNgdQy1FUUCfRKammtHyo2ZjSYHHx1ei0BbdM_vPGLzx9q9yCYvwehZ41I4FBHNfTpSQqt750NoLxmg8ZoEU3aN29jZUwx1jhuLZLPBd_TICyNTZUstz3tWbCDZDisfSpC-skpb5kXssItgykyVEc0QJ_MBLvSfMpwjKCtcuuPwQai6EDl2GKohc05zrCS45Uq7TLacM2TGRaIkKVoUmjWr2CmchfSYpH9o0h_r1erLLJowA8NhONRslrIzECUEMh10Zkxehs6l4ux_NmDoS_tpl1ftts9RcGd-bB9sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سوشی را مجانی میکنیم حتی برای طبقه‌ی سامورایی ها.
@withyashar
🍱</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17235" target="_blank">📅 04:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17234">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75f4d1ccf4.mp4?token=PQwggdAog1XATj4oHgP7qjrZAr0ZNaC0HpUpz3YVK2jhpEvf0NSSENyEcvuCI7cw9iRxr1nZXw5zRLfmv9kfserEzaVHHEO8nN6pypbpH5v_UlWynh6oHtXFLWL5eXuRh0TV1Id1luHfoXrcldLtxMmqogtAjb24IfJY8NYMtkxFYee6H1NRiUhzSmx8B0eehU4-cUF9IvmTbmchcnJCplJg8pbqCn0Z3-Pe4joy4oKuECJ5QeEjvyRd0hug3_TMQ_4TUZJ4RlkKiP69FYNsrT9NNbcpQsMIV9Awtrv8lO66Qp2FgImkfnzxVY9dJAKFvND9b1rFBg7LKAuJ0GhkVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75f4d1ccf4.mp4?token=PQwggdAog1XATj4oHgP7qjrZAr0ZNaC0HpUpz3YVK2jhpEvf0NSSENyEcvuCI7cw9iRxr1nZXw5zRLfmv9kfserEzaVHHEO8nN6pypbpH5v_UlWynh6oHtXFLWL5eXuRh0TV1Id1luHfoXrcldLtxMmqogtAjb24IfJY8NYMtkxFYee6H1NRiUhzSmx8B0eehU4-cUF9IvmTbmchcnJCplJg8pbqCn0Z3-Pe4joy4oKuECJ5QeEjvyRd0hug3_TMQ_4TUZJ4RlkKiP69FYNsrT9NNbcpQsMIV9Awtrv8lO66Qp2FgImkfnzxVY9dJAKFvND9b1rFBg7LKAuJ0GhkVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دقیقا رأس ساعت ۳ صبح هم زمان با مشاهده این پهپاد در سمت غرب تهران و کرج، صدای جنگنده هم بسیار گزارش شد. که ممکنه به هم ربط داشته باشند و جنگنده به دنبال پهپاد آمده باشد
@withyashar</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/17234" target="_blank">📅 03:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17233">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک مقام امریکایی در گفتگو با آکسیوس:
حملات اخیر ایران به کشتی‌های تجاری در تنگه هرمز، توسط گروه‌هایی در داخل ایران صورت گرفته است که با تفاهم نامه شدیدا مخالفت دارند و قصد دارند آن را تضعیف کنند
@withyashar</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/17233" target="_blank">📅 03:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17232">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بر اساس گزارش نشریه "اکسیوس"، یک مقام آمریکایی اعلام کرد که عدم انجام حملات جدید توسط ارتش آمریکا به ایران در امروز ، نتیجه تلاش‌های منطقه‌ای برای کاهش تنش‌ها بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/17232" target="_blank">📅 02:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17231">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/17231" target="_blank">📅 02:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17230">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">وال‌استریت ژورنال: اسرائیل اخیراً اطلاعات جدیدی را با ایالات متحده به اشتراک گذاشت که به گفته این کشور، نشان‌دهنده یک طرح جدید سپاه برای ترور رئیس‌جمهور ترامپ است.
ترامپ روز چهارشنبه، در سخنرانی خود در اجلاس ناتو در آنکارا، ترکیه، به تهدیدهای ایران علیه جان خود اشاره کرد و گفت: «آنها می‌خواهند رهبر آمریکا—من—را از بین ببرند... من در تمام لیست‌های آنها هستم.
@withyashar</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/17230" target="_blank">📅 01:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17229">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حکومت رمال ها  ، بت لگویی ترامپ را آتش زد !
@withyashar</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/17229" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17228">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باقیمانده خامنه ای دفن شد
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/17228" target="_blank">📅 01:20 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17227">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnOzVf5fzuxkEreKA2Kd98JkxclDCulnCWApFu6_44oG-MbmnRHBW8KgpfyzrPv51G-lnAgB8I4B3O_vOkJQeEFq-uzeVK2EAZHBA3XU0gepPOm2XisRruZQmLLehQSnsR12uG_SwEzLvef2FrAEKN0_y_LXnFW3K46WQH25xuM1_Ps3-ewyKwhaxf6utbx3wdzK21Bcm1wAzFy7aI699xUMi0id_yS9AjaPdX5ijW7WBny_K26Vu5Ji9rIftsclQJ4gCpbo6aMqRiR21QQUMz0ga2nJkj8krY3FsUf0U2TYefiq1CfXb8lCp5UvYcgK86IezG-asD4kknQVw-qqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حقیقت یاب اتاق جنگ
⚠️
این عکس هم هوش مصنوعی است !
@withyashar</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/17227" target="_blank">📅 01:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17226">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حقیقت یاب اتاق جنگ
⚠️
این عکس هوش مصنوعی است !
@withyashar</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/17226" target="_blank">📅 01:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17224">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بیانیه جدید سنتکام:
ادعا: رسانه‌های دولتی ایران مدعی هستند که عبور و مرور از تنگه هرمز فقط از مسیرهایی مجاز است که ایران تعیین کرده است.
واقعیت: ایران کنترل تنگه هرمز را در اختیار ندارد. از اوایل ماه مه، نیروهای ایالات متحده به عبور موفقیت‌آمیز بیش از ۸۰۰ کشتی تجاری و ۳۸۰ میلیون بشکه نفت خام از این گذرگاه حیاتی تجارت بین‌المللی کمک کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17224" target="_blank">📅 01:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17223">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6EaISfVcBgH8L0T5Etxe3rTDt-2EnxTD_468amIid34wfWES2af5A2t0BB3LVzqgTHmXr_R3ik8sf_0IRA1D91VVtGcpDcMYhDPOV5oyqMAvWaTcisSsIKTxx9RSIqK91FWNssDIHwC_oFASyi9ZNCjC6B4rrPCiprkyBNEmjYxi0O_FOCm6FWcSp6L9APfYjBBqO7UaDIneZOrX1mCbozDWWHxMz7-k39r2EvsQ4H-BFYmEuFsKhx941Ffv0E_X1FMxqm-2l5PyBnUp64ypVg4r9PHHcgbA3Lyi_7hlRvTqSmDGTqiEnxh5wFxm7s_JnfTKrNeyoYd9UTNqjQNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای آواکس به همراه ۱۰ سوخترسان  ، فقط نشونه اینه که منتظر تایید نهایی هستند… یک جرقه
💥
@withyashar</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/17223" target="_blank">📅 01:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17222">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اومدن گلگی کنم گیفت و استار نمیاد دیدم نه بعضی ها هستن که روحیه بدم بهم هنوز
🙌🏾
دمتون گرم حواسم هست بهتون روز آزادی پیغام میدم تک تکتون جمع میشیم
😭
❤️‍🩹
🫱🏼‍🫲🏽</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17222" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17221">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شرحه واقعه از یک شاهد بیار‌ عرزشی :
شهیدان علوی و هنرور به ضارب مشکوک میشوند که او هم با لباس بسیجی بوده و قصد انجام یک ترور را داشته است، بعد از نزدیک شدن به تروریست دست به اسلحه می‌برد و به سمت شهدا شلیک می‌کند و به سرعت از محل متواری میشود
@withyashar</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/17221" target="_blank">📅 00:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17219">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به گزارش رسانه های‌ رژیم:
بر اساس اطلاعات، دو فرد ناشناس با لباس نظامی‌و با استفاده از اسلحه کمری، شماری از بسیجیان را مورد هدف قرار دادند که طی این اقدام، یکی از بسیجیان در صحنه و دیگری در بیمارستان به هلاکت رسید
ضاربین متواری هستند تلاش نیروهای امنیتی برای شناسایی و دستگیری عوامل این اقدام ادامه دارد.
@withyashar</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/17219" target="_blank">📅 00:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17218">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارشها ۸-۱۰ نفر در‌ تیر اندازی های مشهد کشته شدند
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/17218" target="_blank">📅 00:46 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17216">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یکی از کشته های تیراندازی در مشهد
🚨
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/17216" target="_blank">📅 00:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17215">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دیدبان اتاق جنگ : من دور حرمم نیرو های بسیج و سپاهی دارن خیابونارو ول میکنن میرن با موتور سرعتشونم زیاده
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/17215" target="_blank">📅 00:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17214">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مشهد - ایست‌بازرسی منطقه سرفرازان  توسط افراد ناشناس به رگبار بسته شد
یک درگیری مسلحانه در اطراف حرم امام رضا.... و دومی افرادی که امشب به ایست بازرسی مشهد حمله کردن لباس نظامی به تن داشتند و بعد از زدن نیروهای امنیتی فرار کردن.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/17214" target="_blank">📅 00:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17213">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYdNrc5Kd9w6tbDxwtTwzVxUVjF9qG-j44UZkoopA5jFbw5ADvuiL0PuguXrxlFKw4SLf4QhTOfl2wu19OXmAWxio_xEs_-qU18WnWIqzZMYD_MG0Kfd1YZpFyIqdvhHUXKgU5nrj7Es8dFPCa81sF8AZ66i1VxkDIhRhQ6t7kOzZOaoVNVnABZlivPZDUp4VhSNNqewp2Gu0WlXb4rtYS1Xsx9D3p7DECP7aQwnHzCaR1Q4g5-lRokhxhOGufO35UaYrEUCZ-ND9NUHj7F9uCUdwwTPCmQTXr5rHVYL7B3kJOgruLSG3kROXHdVo1BA3OUe1Aq2sWagsmNUuif6yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از کشته های تیراندازی در مشهد
🚨
@withyashar
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 171K · <a href="https://t.me/withyashar/17213" target="_blank">📅 00:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17212">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNrim8RN_QtApTv_ody8eh52oawaDxyzGL4K66AzgGa7xXkIq_xHqrgSRYjmsFMChkS3WxtAA0FE1JhkklvjbGNgZcc990h9pMvf5UR9oBuubKaieCLRWHWkU5XN1T3ZyKTGBnSC-ZWEAOz37ZrryVq57tCNHQZKQIG5mIrxEceoEaNQN3Hylz4GdB91gLRyi2dUxrVoalprL1Wd_ixu02RXRHAFrt9bo2NhjwdlmNXn4utwTjQjsrOG6oIyOTYrsQj-Z7SqkIktEzLRpKWeFKRr2AXsQpngI7TYIAF3YCI-m7JxAWndax1iu9GBpqwcTRccUD1IKCt274SZrtJD7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری در ‌مشهد از حجازی از چهره های مخوف علی خامنه ای در کنار ممباقر ، بیگلی بیگلی هم او پشته
@withyashar
🤣</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/17212" target="_blank">📅 00:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17211">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گزارشاتی از حمله به یک ایست بازرسی در مشهد
@withyashar</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/17211" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17210">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رسانه های عربی: یک فرد مسلح به سمت اعضای سپاه پاسداران آتش گشود.
@withyashar</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/17210" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17209">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آی۲۴ عبری:  عربستان سعودی در تلاش است تا اسرائیل را از پروژه کریدور اقتصادی هند -خاورمیانه-اروپا (IMEC) کنار گذاشته و مسیر آن را به سمت سوریه و ترکیه تغییر دهد
@withyashar</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/17209" target="_blank">📅 00:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17208">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وزیر عمور خارجه ترکیه
فیدان: با آقای عراقچی صحبت کردم و ایشان نیز با من موافق بودند که آتش‌بس هنوز به پایان نرسیده است
@withyashar</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/17208" target="_blank">📅 00:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17207">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSadeq</strong></div>
<div class="tg-text">پهپاد هم داره میچرخه توی آسمون
مشهد</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/17207" target="_blank">📅 00:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17206">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommaryam</strong></div>
<div class="tg-text">از وکیل اباد هم شنیده شد</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/17206" target="_blank">📅 00:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17205">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐀𝐦𝐢𝐫𝐬𝐚𝐥𝐚𝐫</strong></div>
<div class="tg-text">یاشار منم مشهدم، صدای تیراندازی از سمت میدون پارک‌ملت میومد</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/17205" target="_blank">📅 00:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17204">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">گزارش تایید نشده ((تیر اندازی در مشهد))
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/17204" target="_blank">📅 23:57 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
