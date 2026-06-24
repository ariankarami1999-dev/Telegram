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
<img src="https://cdn5.telesco.pe/file/cv7jVK8Vl6vgifbZX9sOzIMHsn3Vr7zsBF3F20X6V7-0eXZ6wJSrZ_f68NCWpXY5SIRg45Er9-IDf04K7DMBUrYf1e4YCEo24aiU6t4kPcFKZ4xR772S-Sh8AMaPvyX8Tq1-DxwUhDTI-yizf2JtIk4eX2BD7ZaCG3R7BXzZjL7aI2ZiSA-M7UIsQsKdkb5A6grdABeHERZiwA2INKYW60qRPShAiaulEMKfb4ms8DiTs9ZC-0oICj1e9rVc6UPUUs6NKy_ZsvInR2Yk5OrQTu7jWbdFl8MnWQMEU0QeFsycjtiOAlDdXfzljTgFNaaVsjOLmlWJk1mKlG1STYgXQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 710K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 20:55:17</div>
<hr>

<div class="tg-post" id="msg-95657">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
؛ اخبار شنیده شده از اردوی تیم منتخب ایران خبر از بازداشت مهدی‌طارمی و سعید الهویی در فرودگاه شهر سیاتل آمریکا می‌دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/95657" target="_blank">📅 20:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95656">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlmY0DE0YcOxvkDD9m91f_9M5pV6lhS4G-RM_JRaWNvVhP_5MWEUC5yZQmg8QGH_-cElOSYKbwqlGdxo1GDj4MhObnKMDV8-ZGicqFESUkXqNM2NtdTwZGCVZ-V_A1l27gOVnSWSIDSItkJvpB8OXdCZcaCLtmGBUyIx6ghLOfZ4mliwlCYtcI4EwcqII2kyIPfzRfT3fwvoiTjGmhiB7QIwOzXttUD-RYPXypdhTTpqz-IdSW9fEcGIgvxWfMjyYa2DU3GHYXMorVamhf8dNAz0QyU6bV9qnHVa3qi5etrdIsg-IkR2r9Be1oPmb-M4fTYgramq6SEsQ7Iv5BrVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رومانو:
اتلتیکو آماده است تا مذاکرات را با هر باشگاه دیگری که آلوارز را به جز بارسلونا می خواهد آسان کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/Futball180TV/95656" target="_blank">📅 20:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRYNpnSLsp3RSJEFmf-6vb8cvsEojp8vPLj3IemW8-lYJynD53kFIO1KehjygoOSl0tR5U58ywAs5lbrLGTab-_Vpp-BwtwKOyVYvkV4OADINvesvWBwLLDT7C_ywPEHMCu4qb8pvw1-26QjDjIeRYLDiYqJoppBu0j7s28y2yFddx8BXZ8T1zIEVBbjIWBG3Hri2AvThTf09LJca3gSLjMGHHzH18Gu044-cpbZctCgb9hmo6_N9RMvIl9w2rUvDd8fVYDgu7iFnluZeQVuF6V2c3FbgVj2qzQYo6l6YucsdSUuKu1Ho6dlfELCX23W1A_i_frnt87QBjQ-fnsd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔻
رومانو:
🔴
خولیان آلوارز از رفتار باشگاه اتلتیکو مادرید با خود ناراضی است زیرا قبلاً به
مدیران اتلتیکو گفته بود که می‌خواهد جدا شود و آنها از این موضوع کاملا آگاه بودند
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/95655" target="_blank">📅 20:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddba5ecea3.mp4?token=XwvYeFRt4l3u2Y3cLQn-FjBCtBuS8UeQ-xP1eNJZX-vb2rCwGa-3YSKszLk96cyZupQsV8dkxKvftIXoE2YsSq_H5PGzaxeLoWmlnXhfBCA6xvUnxGPKfPVOYKIpjJqvacQnncKtevt0PCKST_1a2IqKBgi4d93tfsaRHbeGdb92uj8uO1WTqKRp_MU9yKbVtIaBzwXWfh-Azecc7pKG0ozXoZO1r-7eHhj6Vly_97HBX_6POxLIUwRoGs5it4CLXncGEjxK11MG6s_WxPdRcu7LpNxqlBUrlyW77wIKoKJa5ARQ3LKFqdQalbWFzWJYu96oroAHT4wsINGO_wnM7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddba5ecea3.mp4?token=XwvYeFRt4l3u2Y3cLQn-FjBCtBuS8UeQ-xP1eNJZX-vb2rCwGa-3YSKszLk96cyZupQsV8dkxKvftIXoE2YsSq_H5PGzaxeLoWmlnXhfBCA6xvUnxGPKfPVOYKIpjJqvacQnncKtevt0PCKST_1a2IqKBgi4d93tfsaRHbeGdb92uj8uO1WTqKRp_MU9yKbVtIaBzwXWfh-Azecc7pKG0ozXoZO1r-7eHhj6Vly_97HBX_6POxLIUwRoGs5it4CLXncGEjxK11MG6s_WxPdRcu7LpNxqlBUrlyW77wIKoKJa5ARQ3LKFqdQalbWFzWJYu96oroAHT4wsINGO_wnM7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای خار جبر جغرافیایی رو
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/95654" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdIQtAc5WZnkBBRsLV3Vsu3JftZDFOnC9Qkkxtpz1AFkBkYB_MyfQ3LwzgRLrdvT9VxcxTrrA7jutuVr0GAJHBciBfs3s7v3qzTrA9rem86KuWtcexN90MZ2ABtREvMd5FZ1Er81aM7_Gd5rTjLBfE8mYTM_yBqlXZ4eVhEyppadiFaTCNa2DIivclxvgyJm1PzoLUzM6ufRo_RdZcq7Uk74eJFWMQbeQEdATel2NvglnoP3DF2v-pfJyz7p3Gt605ILeQfOQeVjfoXb6vmGgv_rgrBvNrVvUFJ1xfl9PAVMEwZSliU1o7cKbY-iMp9h-jm4Vb9RhYYZx-e6y5Sp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رتبه‌بندی بهترین بازیکنان در تاثیر‌گذاری در حمله، پاس گل، خلق موقعیت، شوت خطرناک، دریبل‌های موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/95653" target="_blank">📅 20:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pf1wXLQ1pk7_h2H5tPfrhqFncvoVrB6FQ6im7T3LBXptBbAceZBHfnzeb5dLxr4xd0PhN7jcrSnf14dMFHF25D-CT2XNSWswmb3zCBhgDfUBE6_52X6wdv1ejYMYD9uC8x6VjlCSZxHKeHecp-I15KmYmjESX-bxigj8yiMOV7Z6V08byb8JR6wg593sAuWpFSyP122tykafTS6zOQSXWel1xrZ8E5oDsWM5QKFwQpRAVRnz0Oqj7cHsHByuPemg58sofJKgV8mXRIAOjzf0kJanskMsbBkg1eNeuIxn40MpwZTbgU2WsRUZAzK_g1KRVuL5QJ18PBSd79LG-D55rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد ملی زلاتان و هالند تو تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/95652" target="_blank">📅 19:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjn-6KQRpM2M-ZhahxjjmHYVFzvN3TDUxKd-9yDDwhxoyHbez1MfAtsjuwFg9OYrTKuEUDD-sZhIG2mnbMHmzqcfwjNlmFYl1b177A_WQ9mN_RRzGxl0hDYcSL5vhFgYqOa5pEZUfJudaNfke4j7hHBeq5wFiGZPFcrHeuIWCmo14a8b-aLNjaFTteJvjrLyJpuq6bultUXpd-LA-YkcrIqvkPRzqrl3qUJKFMcMMHr1MnYldSYIZWDMxR5EseJoxxhgbPkHwTVewLJEz45ILLRJBBDYaKV2iPp086m7Yct4f-79PaZYeN-H4Y479FIt12ZD1wsORi0f1qojlyKPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزی ۹۰ میلیون سود از جام جهانی
⚽️
برای پولدار شدن تو ایران چنل زیر فالو کنید
⭐
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک برمیدارم
❌
❌
❌
سریع بپیوندید
🖱
سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگادشون
💀
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/95651" target="_blank">📅 19:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHxD6zWSfMWOIWpVd0lJ_fEMeyO72JT49g8r1OE21D59F2iLSZbIxzWsiLrzZH9KxtkNqd4qVr7U1-MfGb9PkdW5232l8UqvG2XUJ7PvsrQzzU3j7TX4NIGbkr7igZZrbUKWvEU8JYIqq5LkPS4M3U0_W2UY5jSzXSBhCjwuVMiCXctdydWfh1WAEURl4TrL1Ljj_6AT4EWyO_BvqYjCuBOJIgSoKh0F9Xp5TRPg5_rTYZ9SwrAORNlWtnXsq4K_FzKIhQhU73Cy2fU-cIyPf6KQJnqZFzsbXn3VW1dc3CFawrCfoWnqWSIU_AnW4c-ys8HYlIfkYPEseHJl5M17ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام عکسو حاجی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/95650" target="_blank">📅 19:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/677deda53b.mp4?token=sKz88O7RjZLd1BZVbUiOvuiV4aWHNImBrzHJsDV6RHp5ypnHkgOzZRHoptHNC_0kRjGbre3VYuDuXhok5E72K9BQcpwqqdq8mjSBhYJjghODveDYB4cinH0BR48pARtHvl8PS6r8vEm75SQnWKmyJzL4giUMXACm5urjg9xernolk_tA9P6lmcobJ_e6sLaTyrjhshW55drCjtTmDB1ES5Mxv3AmlgxWldiobP0MEtD4fbLz1dUaYbQpsPDSlb0VGgjhEidCtu96NEUiUU_yv6OY_NPKzgmmAcBDbCv3AcVEyhkZiuhoby1mvXOjl69Ouj_MAmycV4ll7cxlCP5_Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/677deda53b.mp4?token=sKz88O7RjZLd1BZVbUiOvuiV4aWHNImBrzHJsDV6RHp5ypnHkgOzZRHoptHNC_0kRjGbre3VYuDuXhok5E72K9BQcpwqqdq8mjSBhYJjghODveDYB4cinH0BR48pARtHvl8PS6r8vEm75SQnWKmyJzL4giUMXACm5urjg9xernolk_tA9P6lmcobJ_e6sLaTyrjhshW55drCjtTmDB1ES5Mxv3AmlgxWldiobP0MEtD4fbLz1dUaYbQpsPDSlb0VGgjhEidCtu96NEUiUU_yv6OY_NPKzgmmAcBDbCv3AcVEyhkZiuhoby1mvXOjl69Ouj_MAmycV4ll7cxlCP5_Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">2 روز دیگه این شاهکار رو قراره ببینیم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/95649" target="_blank">📅 19:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV-hqtynlw93nWhnx7Rk0wNSBAM6grK6U6TdN5FQow3skAbN2KR2G4NHKvpOzz3k4zz7eFzGVf031Q41JN5uUnf0Rvl4L9xv-7tKV47WvwqPpZcR4Srxs_vg46UUHYbKq0FdbgD22bH7wkaYzkQl0aYD9g0NI9WBIXHofMPgi8OkLKR8QsMA1RXav1G8jiMbABzruepwYdfWkrTMf_TA45nYBRjnpa3eUV9UXSX-S31O4Udi4MPxjr7Sdx5siACUN-OgVM-JBAOSUR_LcQZlTATbzbWrv36kKACfPj3aWC6iqugeX22DA4TvnuWChpgymMqR57gjlG1UUe90fAoJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مورینیو:
من انکار نمیکنم که رئال مادرید را دوست دارم و دلیل بازگشتم هم همین است، اما اصلاً نسبت به بارسلونا احساس منفی ندارم.
🔹
من فقط از بازی مقابل آنها لذت میبرم، زیرا در فوتبال از بازی در برابر بهترین ها لذت میبری.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/95648" target="_blank">📅 19:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IervjgGvz9EJbsoAMjO4-uCtw11mByDrAWD2hROVofb_U1PNXhqgmFyyAoNjpvw0Cb9z0-oYQzVRgq1GIjOwHqYgdBSeaQ5cqwv51tCUDXS8xOg01t_TnyKBFW8TsdyYfoiBPuTQM-yNYZM64x_f6iC3GrP0ln1xNvHIgnoeZJuaj2QPrMfXlRgAmsCzdm8hzxpcZkS3ZCVuil8U5N8ZsjMFrGdqgZ0axwownvSDmqItCZIHo1po2uOt9Qxu_ocnNAbbS2SaLIf38bEWXE6LaoKbTavFFgdrW8qIlgOUZjJIMjHYaBo7ijmoZLQCcHkSlCfVGnkPF8FYySVEPMenLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از فابریزیو رومانو:
گریمالدو با 20 میلیون یورو به اتلتیکو مادرید؛ HERE WE GO !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/95647" target="_blank">📅 19:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95646">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3GtE6vojM5V1itM_fLMZ7G8dPtbgsvWd7yeMEc5BVb-AgdHGViqUh40NawcrVSzFR-oInUmsMvyGEkro9baK5AXcgADjlj8fqsnNM4VheZkaFaZAzD6LcNLqsBGqTk6WAZ1739xOIyEwX1sjrTjYzJSpip1TbPilNQ6GaWKamO62Wjt-R_F14fCk4QvVZQ0coWDzbgrxxSctZ9Q_sKx6Q1kNTeb5na-bBqHaNKvu5qxAps5ZHX4oD6L-4PYkbLNzO0t4FV7-tv31u8OVOH2DaOx08eaX63zmm2SXMFX3hT_WdSMl48Rr7rojRIOIPUSFxLJKMEPGPigQDEfOkDc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیونل مسی ۳۸ سالگی‌اش را پشت سر گذاشت و وارد ۳۹ سالگی شد. آمار او در ۳۸ سالگی:
⚽️
50 بازی
⚽️
50 گل
🎯
30 پاس گل  مسی در مجموع روی 80 گل در 50 بازی تأثیر مستقیم داشته است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/95646" target="_blank">📅 19:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95645">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vyb95vFPIDFgPI71ZQyCnczkhfQBhHEjigwRkrubEPgxgT-VWjkC_cH3RD6oBJC7ekbsmaoxQMKERWSB4eqqGf7PiV8-vH6QFnunAKMU5jmlhlL8GC6QkVSocP1pGrmBlM-t-BaprK1of_Yuxv-T2kP_Dw5TFuuWbgKA_chZomTvjwVzyseNq_h7dIPiEuSjp_FPXijcU6-TsDErg63xH_7TpyBd5JVtWXCxYV33ZF1eNbvnSoxceiq5WgB7cZUL8u-lhI1rq4tU1t3nUpQMtT6JqbkqORsIHJMNXZlDkoo5x_pnYSQyCCEqHdLyl3C0ci1uPjNymKMoZoL7et2jPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
رئال مادرید انتظار دارد در تابستان امسال تیمی حاضر شود که به وینیسیوس جونیور پیشنهاد بدهد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/95645" target="_blank">📅 19:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95644">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfmtbhz3izgR8XKpSjRERXfc1XWsM-WQ9rzuLZI6gGU4SeqCLn_H1LCXclJCzRLzZ4R_-Msf4dUs7cO3fTQFG3f9qbS1NGzSpt-Pe1jsAu9I-18GD3AiLoSbfwr8DrzAaXOSdjdwsZVxP_lYDiWm_AaPK6TEBnACvq0eGlPirCyadetC3fM4vmAWquAEwQkV5ksqEZahyCQuRbnKiryLWEBEXwa7LWWayxriJVtza-HdWUtfXWZA0egTTOHgeeN8lHOH7ESL09bQdeHYx2aXFO2WhcMzSr07Ts2rOGJf4e0PUg_lvQDbzIeIMQtpi9HsFH9Rtr57g8X3fDcPOHeo3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
5 رتبه برتر فیفا پس از پایان هفته دوم جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/95644" target="_blank">📅 19:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95643">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3u9b-DkyoI3z8V7ylIFzX6Mg3R41TDEj0u4zHF2twIyzkw1s8paMoZPvGdR8VuFY2cdNdonQ7nURmqtv4a9ek1V-ZYSgzWzjcLudteu-vvQJSUcAYJt-3GPl5wVXQo47EnUfnWksPGp0Vzx8DwyDg7IM1j4Dt4vs4ybUk9NtTxX2J2kazyL7ReNhG9kTq-6hsK0xNnPNf9DLJ1DyxwXRaaeHH4EqlV13IKmIOhOZlx7pmgX_nXlCI7xCkeNifd9n-oo9W6EyMhoCXhVEScZEBe1MlFQ9K_enaIPAS6cCwheWcUlRWHPpHgLYg_BxpTqaxAZZQqBM5BtrfCtSSy0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیونل مسی ۳۸ سالگی‌اش را پشت سر گذاشت و وارد ۳۹ سالگی شد. آمار او در ۳۸ سالگی:
⚽️
50 بازی
⚽️
50 گل
🎯
30 پاس گل
مسی در مجموع روی 80 گل در 50 بازی تأثیر مستقیم داشته است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95643" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95642">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOwwKOfBT_uwAEVt5aQZY35cOJsgAmnFfACtQHVGAL97f8XzbkVYvKVMATQbH7ExIIap_4PNjejZvisPqE3C9UluG2YgPazlkxL21i3HQnp4hKVOeHDSpHTTWuACTtbAa6r0-3LIkwJTTfN-GSM0ghanE4Gsr4pAbaWT1FvgwJiSI-MWUh_k8pj-sU0g272T5vbza827ehZbsojniL2OvdEw9n0jnM098RzESzvxhXEoaEybOsSP_qE3hi13np48KeOsWKsSn5DmqIHniw4p2UEu58XSnRgBQ05kNgq_Adxe_oaKeQR5OTOZjXJo3dfaXB0Rj1aTKPp7UiSSQAfhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانا کواکو بونسام (جادوگر غنایی)
: من، کواکو بونسام، قدرتمندترین جادوگر جهان هستم. هری کین را شکست دادم. دیشب بازی او را دیدید؟ او حتی توپ را هم ندید. چه برسد به اینکه بخواهد گل بزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/95642" target="_blank">📅 18:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95641">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/95641" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95641" target="_blank">📅 18:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95640">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=coKxj7yx4F5qIH-q0TL0qDlEOTyrIi6SqCkZfFVKj92u_LowBXK2NskndOKinWtzP3T0gaSPU8W8U7KaZpIOXJpwAScZANQgbz2rcZ2isX97u6N-RoyxAI_H8XDGGGO67C6RM91l2FA7l4pHUo5lIzAHhQac3LupBPCawg6HQjrhoXMC0XoVYHBpftw-z0Wut3Zuc4r2DGBNh_Qax-AahRePzBbesp6NWI8mMYzabIP_GkxJQ-1H7IbgupnP3CN7ZQ6DeRyaV8Bm4vQpTdkuqIHMZgfT4m-ERbphOL-aFnifUsNjxjPY7xJHtD6jbRYPuY4BtIXXGElqgSVz28tItpiBMGgoPTgMvAvpjDNx78V-2pzBpF0oGnBbIGlo68ZJzuFOVAlhuQEpwpbmGeA9JiyRfYXQnS92iQ41PH9yV-8ZPWKmuh6k5TwYzMDzdfkC37RDOeyPNRlEBc5hg-T6umXrzWHiRomaepRuqMiASbVVuLNUIIUHcgj-3JkzwQl8RdlDr9kD8gIJGVvqeg1--2wGZ9bHzd0MWK18B18CPGGONh08CGnArZkuqjgJY8H-V9HtbOUPy51Za1JUHDWg7tvI4e6RzoC_CiPDOmqu5m5lOnXkhhiJgSHPIOyhr0g0S-Yi4wylSsFLT55tIDj3TkUZZMD5BaPU6G4t7cvHwbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=coKxj7yx4F5qIH-q0TL0qDlEOTyrIi6SqCkZfFVKj92u_LowBXK2NskndOKinWtzP3T0gaSPU8W8U7KaZpIOXJpwAScZANQgbz2rcZ2isX97u6N-RoyxAI_H8XDGGGO67C6RM91l2FA7l4pHUo5lIzAHhQac3LupBPCawg6HQjrhoXMC0XoVYHBpftw-z0Wut3Zuc4r2DGBNh_Qax-AahRePzBbesp6NWI8mMYzabIP_GkxJQ-1H7IbgupnP3CN7ZQ6DeRyaV8Bm4vQpTdkuqIHMZgfT4m-ERbphOL-aFnifUsNjxjPY7xJHtD6jbRYPuY4BtIXXGElqgSVz28tItpiBMGgoPTgMvAvpjDNx78V-2pzBpF0oGnBbIGlo68ZJzuFOVAlhuQEpwpbmGeA9JiyRfYXQnS92iQ41PH9yV-8ZPWKmuh6k5TwYzMDzdfkC37RDOeyPNRlEBc5hg-T6umXrzWHiRomaepRuqMiASbVVuLNUIIUHcgj-3JkzwQl8RdlDr9kD8gIJGVvqeg1--2wGZ9bHzd0MWK18B18CPGGONh08CGnArZkuqjgJY8H-V9HtbOUPy51Za1JUHDWg7tvI4e6RzoC_CiPDOmqu5m5lOnXkhhiJgSHPIOyhr0g0S-Yi4wylSsFLT55tIDj3TkUZZMD5BaPU6G4t7cvHwbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/95640" target="_blank">📅 18:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95639">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaPji9fvB6bclTkdt32OZfvEdxOCqcCcxxy0GsAXOlC4l5no3Z0rHs094D_u5BEm4ExqjAxM0vRKBL998R034CFWQJg3b4jqrvuTXjV7f8zpvRtEyacYZsjJceogoJ5nyTJ3_DRShX4DT2SR7gF6zi-mZehUEtKPlZfAobZKhaBaNBHUvoXFgU3QF0KwHaz1TcEz1X6zrM-Ocy89t1GxNX3IKtAI5TR2OQJy5-VSqRqi5ZoDx_mrJuEiZ8ghM8Y5hOByCpRmoKaqri50Nq38SUN6Zgsp02rX_lYMYkTNaB1ulZYK8NiX21R7j-P2F0-_Tph01VZQFN85F17mrXK9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
فورییییی از کارلو آنچلوتی: نیمار کاملا بهبود یافته و آمادست تا 90 دقیقه برای برزیل بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/95639" target="_blank">📅 18:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95638">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d71eb644.mp4?token=PRfoRL9IaMW_lebkPnrscVIFyeUk1DTLiUP06lySVKD7ie5uBBK4QtnpRogJJtYD79wTXOD-p9OEPxX1w2J4wNheKmRDutz9UZZGGOuP7s0X_-odf64I3O7NcO00FdlZikhx0S-ZNXbeqOkZTUTKhIpzskJSIqNfaipniWOn0KBECaj9iKDVTZJ6CVE04vmCcfwVhn_zMSlnH7fbmkZag3WT-bEIQ2oHTv_FPldjhOD7qXLYtOpqsLSq30p-RiHEmLqR8QS8vL7jnyVw3LAHoYPc5DeXhwSDt3BMQIM3Fl5lUn80CIU-A4XK1NtN26Ge3jDMGGfIl2ZN-H5ioJnfPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d71eb644.mp4?token=PRfoRL9IaMW_lebkPnrscVIFyeUk1DTLiUP06lySVKD7ie5uBBK4QtnpRogJJtYD79wTXOD-p9OEPxX1w2J4wNheKmRDutz9UZZGGOuP7s0X_-odf64I3O7NcO00FdlZikhx0S-ZNXbeqOkZTUTKhIpzskJSIqNfaipniWOn0KBECaj9iKDVTZJ6CVE04vmCcfwVhn_zMSlnH7fbmkZag3WT-bEIQ2oHTv_FPldjhOD7qXLYtOpqsLSq30p-RiHEmLqR8QS8vL7jnyVw3LAHoYPc5DeXhwSDt3BMQIM3Fl5lUn80CIU-A4XK1NtN26Ge3jDMGGfIl2ZN-H5ioJnfPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
حالا این‌وسط بانکا چرا قطعه؟
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/95638" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95637">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028dc79cec.mp4?token=gCfhYKlxI30-c_hvPQnMyen1Ww3JCSjDqu_LpkIoARpQP1a_0ZCAhCsWRVSdbMwceddyrFoCXYVIpPretwsvTCwydnMf7sjlzYEiHQtYc4yQK5s_832XUWa_79KM3vG9Ljts4V4CUafO4NsYmZT92n-7d1tNWy-gU1bqIKpwTr7ipiC87ii1NINtV2t4Z8A0omaI1pBWx7WBl026EXLx5rsvlxFIwF8Biuhh6QTbIW7U58HElPh_iI5s4BiC3d5WaW0_mx7nTCpNITHz5n9uScLEu1ctnjwtbHulgv4SlS2_jt8Y-xwIe1Vvir8q8fxDKBriY_a6bd1HChuERHXeew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028dc79cec.mp4?token=gCfhYKlxI30-c_hvPQnMyen1Ww3JCSjDqu_LpkIoARpQP1a_0ZCAhCsWRVSdbMwceddyrFoCXYVIpPretwsvTCwydnMf7sjlzYEiHQtYc4yQK5s_832XUWa_79KM3vG9Ljts4V4CUafO4NsYmZT92n-7d1tNWy-gU1bqIKpwTr7ipiC87ii1NINtV2t4Z8A0omaI1pBWx7WBl026EXLx5rsvlxFIwF8Biuhh6QTbIW7U58HElPh_iI5s4BiC3d5WaW0_mx7nTCpNITHz5n9uScLEu1ctnjwtbHulgv4SlS2_jt8Y-xwIe1Vvir8q8fxDKBriY_a6bd1HChuERHXeew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هوادار انگلیسی تو بازی دیشب پشماش ریخته از حرکت مردم غنا و فکر میکنه دلیل نبردنشون سحر و جادو بوده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/95637" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95636">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXPy352SyxT67lJDeX4QpVlf0NxY5adY9WSrHjFQHFKVARNt2qv0y5o-LGMq0kOC3g-Zhs-9iEiIhJ0aGk9qtpJC9S-y06UBdp891ZrmQgOejW_ctpwmnx4CfYr5hZ_6uxsJaghd50tjnaoXujkFnHawScOE-5A9QB1FZ0Tvnle3qrXEFypydAHkCmChUCyIlqTYdTcqLgbmkNcrcneAPxGE8HNkKQhREp4C4kUeUYGc9rpXgVrR4wnNTnKoXH3gWmesocDLcI-4TK84lX2PKQ2lWIEOUxrRoEp-TK2NJ4HziSD2SQqpjy0g99_ap1ukWZuL7Lr5ne5WxHNjObmOOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
متئو مورتو:
🔺
پیشنهاد جدید بارسلونا به اتلتیکو برای خولیان آلوارز با پاداش به ۱۳۰-۱۴۰ میلیون یورو خواهد رسید؛ قراره مذاکرات بین بارسلونا و اتلتیکو مادرید تو این چند روز از سر گرفته بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95636" target="_blank">📅 17:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95635">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1224d3d31b.mp4?token=KruNV0Ke_h8CvJsCXmkd28ii3DuZYAq94JlvDDs_mZJ1KaIQYQRHE8jfgCQjCIw0ePx93tfQM1D4oAv0QBXCROV5BRMCQoMIEG-WgG9IFwazlK0MEE71wkdSEibDGcc18Ey0rXeNm_px9Bo4AxnA9uUI2XuLEKSqdi9VRKHs9jbQtBsxhYr3gxBaigQUS_4NIMg5f3hRL7kYiUkIe_cqZ17uLi3CTFfDbMSamqjrx-tgjkN1UnJ1kJumKmyA_-GuGrc8gElYd9BSUV6X82vVN_8KIa1mWPY-Qo5iPwF_dOYXbyFQJvS2kVItq4ferIVOARbrf8uaPgP-9T6qQj1AJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1224d3d31b.mp4?token=KruNV0Ke_h8CvJsCXmkd28ii3DuZYAq94JlvDDs_mZJ1KaIQYQRHE8jfgCQjCIw0ePx93tfQM1D4oAv0QBXCROV5BRMCQoMIEG-WgG9IFwazlK0MEE71wkdSEibDGcc18Ey0rXeNm_px9Bo4AxnA9uUI2XuLEKSqdi9VRKHs9jbQtBsxhYr3gxBaigQUS_4NIMg5f3hRL7kYiUkIe_cqZ17uLi3CTFfDbMSamqjrx-tgjkN1UnJ1kJumKmyA_-GuGrc8gElYd9BSUV6X82vVN_8KIa1mWPY-Qo5iPwF_dOYXbyFQJvS2kVItq4ferIVOARbrf8uaPgP-9T6qQj1AJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
لیونل‌مسی در اولین روز ۳۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95635" target="_blank">📅 17:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95634">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
‼️
هوادار خانم منتخب ایران با پرچم جمهوری‌ اسلامی خطاب به کسایی که پرچم شیر و خورشید دارن: همگی بیاید برید تو کونم
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95634" target="_blank">📅 17:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95633">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYoByDCWKdEcIn_uEsQQ34w6l5GGxqwPZQtLN4qG8ugayuo1ncLWtb2gO_l_Gs_04F_9S25ZQSXewFNog07Gxw9GzEnPt_RZoMEnJtp3SRcsKU_4RkAAKwq86NCvlpvQd4qaD8hhV1UFj41Un9gI2r1Ary49jnZufvgYFAnVNFF0UJU-_dlOSefkU9uTXK4MvL856U9YY0iGpQ9ZYyBoHB24BxuU-Mjs5CXkG5WG3jcrnqDzbWAPfGYjz0_-CULvCMRa9fLcM46PoXXc9gMbQKRFmg8R4Lio76a294_ILNG4GmD7yMH0xzSTCUtGoJVYF_psv2rF9sCxpWpJ2BZ5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علیرضا فغانی به عنوان داور دیدار پرتغال و کلمبیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95633" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95632">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b14e7b150.mp4?token=dy132QBnIfrBQEflAGRMUnOLh10Hz_NuJGZFveICfeAXReE5enMgZwUekcZdWQ1d_mplIEfP7jSudOnwneXubrFOc0yS0zA-KGKj4CLHwI_UjU9nrJaLBdW743-NjvV5xycbOvJY1j47eGf5TEf71oVN1fb2G_KyZ1sAuyWmHfv4qHA98o2At4gY2EsQnBFrQ7q3SmNhqY4qwxsKEbCCZzvQ0nMEE4eSvX495L1Mn26u5g9hdOy1v6SpTUQyET6mrS3lLV504vcTZCRqaDMw4rLKIuTDkKXAuT5trCjxB7xK7rOuIvTT1T1ZMCnF5twe3iabwF4yce_GlaxrEqBltg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b14e7b150.mp4?token=dy132QBnIfrBQEflAGRMUnOLh10Hz_NuJGZFveICfeAXReE5enMgZwUekcZdWQ1d_mplIEfP7jSudOnwneXubrFOc0yS0zA-KGKj4CLHwI_UjU9nrJaLBdW743-NjvV5xycbOvJY1j47eGf5TEf71oVN1fb2G_KyZ1sAuyWmHfv4qHA98o2At4gY2EsQnBFrQ7q3SmNhqY4qwxsKEbCCZzvQ0nMEE4eSvX495L1Mn26u5g9hdOy1v6SpTUQyET6mrS3lLV504vcTZCRqaDMw4rLKIuTDkKXAuT5trCjxB7xK7rOuIvTT1T1ZMCnF5twe3iabwF4yce_GlaxrEqBltg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
💥
پای شخصیت‌های وایکینگ‌ها هم به جام‌جهانی باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95632" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95631">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
ترامپ: بازرسان آمریکایی برای بازرسی سایت های هسته ای ایران به آژانس بین المللی انرژی اتمی می پیوندند‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95631" target="_blank">📅 16:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95630">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c083e67433.mp4?token=S-lXnlpNFl78pswweDggcx6NvWtitq_YtzWuktF_wsaRgqyyg-jmLqXdQky3msnpwn4Ib0j2DRSI1D9PzpO_W5rh-uAYFix1IIssqUybz9FcHSYFcqOsQRCNfCHaHs5vpbfY9c19sDyI7xW9oUSf-uZjBNHYF9Um3vzHs1pqmdVoxuYkt7OO3HzUGYym3s44BdauaNAkvnKLxuKbC3YkBKlW6PAlU-22FqcUXE5D20kd4UwFlMhwQL88yp-a3CSjZUxN5IqND9k5yMSC4EYz4XBsL_u1fueHC5ZFbf8TY11MxW887xpG2fNynqvcfm0CVfLNGLGyOj_NLQ-KXOrd0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c083e67433.mp4?token=S-lXnlpNFl78pswweDggcx6NvWtitq_YtzWuktF_wsaRgqyyg-jmLqXdQky3msnpwn4Ib0j2DRSI1D9PzpO_W5rh-uAYFix1IIssqUybz9FcHSYFcqOsQRCNfCHaHs5vpbfY9c19sDyI7xW9oUSf-uZjBNHYF9Um3vzHs1pqmdVoxuYkt7OO3HzUGYym3s44BdauaNAkvnKLxuKbC3YkBKlW6PAlU-22FqcUXE5D20kd4UwFlMhwQL88yp-a3CSjZUxN5IqND9k5yMSC4EYz4XBsL_u1fueHC5ZFbf8TY11MxW887xpG2fNynqvcfm0CVfLNGLGyOj_NLQ-KXOrd0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
این ویدیو خداستتتت. خداداد عزیزی مغزش از کسشرای خیابانی هنگ کرده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95630" target="_blank">📅 16:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95629">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvwkO3Zkx5nnM6oubKZ3BjYReoTZQ06owH8nRjRIpDWAuUje94aDjCq2ALIIbUWeb8Db4hMRJ0ApV20CqKiIYTTKEfhg20z7K03Rkvu4WE7lzQoPRD5wqGAUWDSyQCq_PNWEwpmT2X2fTJKmW0CxcaLgMD1wF8jCue1bc8nKpzDYfRC0oIFPLo7rSSYVAq6sy_v67fMg6Lm1VYA5m6WrY3YWAYo13FSYoEVAxst9AoOeF-5h_iXJ6lz3tXs_boq45zzXGHPfqtpFN_6IukXN7mkba5rIiT-rWOYCujx6aBf-ohWRmX8YsL5SN-QyoQW2tYnwSs22t6Oc9GgfDNIPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یان دیومندی بازیکن ساحل عاج در جام جهانی 2026 ، 16 دریبل ثبت کرد که بیش از هر بازیکن دیگری در دو هفته اول بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95629" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95628">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4e18637e.mp4?token=Ta-6TwD0Z3XFA5F2oryQK4-fF_KraXRwUtnjHXoN8PcP-X2Y7Kxm0ML-wVB3rIYgpfL36cZpjeMJK3CzuNNFr7i8A1of_hzthZCNDbuA6W7u55-BP67kfYo9ka9s4G7uEsKMrQTPb7-62oSSN9bEsQ_ye3oaOTrL0rAHvRavHvWCo20jmVmMwxtZpMiCiIXRTUVjjtcSmaiwJVD_VYc8ScDElrWdnzGgcVwS7OGKx0tvm_Q4Bo_ff_VEHJ06Rr5-ED3hT7EKbNkRJT_6uWDnKjZmyVoidb4KrCfU9CS-r9yxYOLM79x0FcThcV9DCWmXmYTltBdvrr3Hm-AwBikPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4e18637e.mp4?token=Ta-6TwD0Z3XFA5F2oryQK4-fF_KraXRwUtnjHXoN8PcP-X2Y7Kxm0ML-wVB3rIYgpfL36cZpjeMJK3CzuNNFr7i8A1of_hzthZCNDbuA6W7u55-BP67kfYo9ka9s4G7uEsKMrQTPb7-62oSSN9bEsQ_ye3oaOTrL0rAHvRavHvWCo20jmVmMwxtZpMiCiIXRTUVjjtcSmaiwJVD_VYc8ScDElrWdnzGgcVwS7OGKx0tvm_Q4Bo_ff_VEHJ06Rr5-ED3hT7EKbNkRJT_6uWDnKjZmyVoidb4KrCfU9CS-r9yxYOLM79x0FcThcV9DCWmXmYTltBdvrr3Hm-AwBikPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
جالبترین شادی‌معروف نروژی‌ها تا امروز
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95628" target="_blank">📅 15:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95627">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnEaAO2HsEuLgOWAFlZm7TVWVsn6y5CI8KxV0EUdj9ktWlQdJoIeV0FNzZAVjPU3P82D4ih2oD1QOTnnd2ak7pm4rlp1cwHyfrVGNVehQRIp8Q-73uxPMvmagggdgdC8-16yZYRkFrySuFuO-OBPM2cIwUYNk_NAd7CIbnmSXQek3YEJnL7HUx46f-n1e84uF799jh3yAKtu1-8NdKdQyvgJfTUak-cdWkMXSTkj4b916xYfnbhEWV2p_0r51kREJ1VbXcH35WXTzxMTnYuqPE23DRpL8hClCcJUKPvMfIZpCx3d1bETT08VEU0x27C3ycct02mVJvSuAuW31p635A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
بیشترین تعداد شوت در چارچوب در این جام جهانی توسط این بازیکنا انجام شده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95627" target="_blank">📅 15:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23666a9bc9.mp4?token=MwZwA2vjEAxxRW1I4Fv06J2cPz18_raYuIIM69M9M9jkMHO6TLVQnnjzZ0Py4WhErpsNpxRcq06NAD3H8kanmFrnzOiNPeoccPyBzW6knTkgSQGJ9uqwQ35uXK6WC2fJ-7ENd_qOWkUTqa8bTlwOy8nvi9Y7-2E-ba5Nsf0IQVmcBxKEcgzS2Qd2el9Yy5Y-RemI-an207hp6qJwQ1zwUqKOEh9I3vea6Pyh9dBBuAvu-d0LQihckuV4r2IN9_ck4L0ncstAGAQ1Cxq0K7p2U-TrjAw2NkpJ-RHfd4XEAjrUFXVfHKZdB4DVpVG7QY3-3-zXn7Slm9l_vlf4NJa1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23666a9bc9.mp4?token=MwZwA2vjEAxxRW1I4Fv06J2cPz18_raYuIIM69M9M9jkMHO6TLVQnnjzZ0Py4WhErpsNpxRcq06NAD3H8kanmFrnzOiNPeoccPyBzW6knTkgSQGJ9uqwQ35uXK6WC2fJ-7ENd_qOWkUTqa8bTlwOy8nvi9Y7-2E-ba5Nsf0IQVmcBxKEcgzS2Qd2el9Yy5Y-RemI-an207hp6qJwQ1zwUqKOEh9I3vea6Pyh9dBBuAvu-d0LQihckuV4r2IN9_ck4L0ncstAGAQ1Cxq0K7p2U-TrjAw2NkpJ-RHfd4XEAjrUFXVfHKZdB4DVpVG7QY3-3-zXn7Slm9l_vlf4NJa1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😛
آرژانتینی‌ جماعت وقتی میخواد فوتبال ببینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95626" target="_blank">📅 15:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95623">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbxKDvdjefgjz5Pr8N3Od-9dgvGPIEtfLCwjwJUn5t5mMs3wnMi-Yf7Hl2VcKQv3tD-FLFY8e97Ik4M1S4hnQb7mSIqY2bOxYy_ODy3-x_IQlC9nTSjxRrzbOtok-4PAtGZ6-dIeI-1B27LIOSXrBLOKOFhxVTNYsSaChzAKa-aCP_maakmCorPSwMZbuYKYdS9Q4yAz3EJLfDzPJUNYdMmMXeSvee6j0PAgOEduNBqZJPx0CaVBDi5Hg6U-xoycoau4FshG3WKpBePK5Xwoz3q4-SYpQM9LxznQrV4HhsimzX7S_vY9RvXCDYnAiHi96CyCpq8c8dSLoMpIJDCmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rmj3s_czz7Wud4uJqIdVMEGPXPqBVxcbiezd3tU5d2IcMr8xfAbrvdouu-Qc0dTXCklVz6y8inppctcdRKPJeRlO0V25Qj-rsbiOOTocs8TJPS7Z-PWwXpU229djcuxVj8q0cE3uw7ITusE345_jPnlx9CrG8YneJvWl9huey8rmBee4QhkctZz5VztnmqOVg5YAJ3lY9lkVL1o0eNAPsUNDRROz_W8GuqiFE8T1xhTqVQIK5qWZnW4hLU5LJM8oV_R8VNzkndSHrQmINajklw_IWDwYT66hsnwoZJpdIpRn6oV798bGwrquhTK6bVV42iTSMA1KtZ9q82q7fbZs_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBHYWjCy1S9IgMY3ynm5v6eh41rKJ335W4UCV3uR87a7dj6wJuiyOl5bwIZl61hIGcE1EuZGX7Mj2fHBHT6fM9CTC6sBRCpjT6m6xYGnvXDhwoKiqKKs3J0o7j7rWll1d_kWePPZy3uhQVM41RfnFOCrQ-jq4V99Tg8S5Yw_nVfpN_93qieC1ZcnAQOxsSa_5cH9cxat_U0t5OTTRFRmJZbZPYpF3hVRZLClXvKjPYlvsd5T7TL_mtUwIL3a99uQZv1gsR59z-powVKkLdMqcswAM2OqRK3thBsWNeAJhzHld1obfiZyJST4H6Ec-pG2fkn5fs9CFW7RzoAfLxThnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇮🇹
12 سال از این ابر شاهکار سوارز گذشت
😆
🔺
فیفا بعد بازی سوارز رو که دو بار دیگم سابقه گاز گرفتن داشت رو 4 ماه از فعالیت‌های فوتبالی محروم کرد.
🎙
مصاحبه کیه‌لینی تو سال 2020: من شیطنتش رو تحسین میکنم. نیازی نیست از من عذرخواهی کند چون من هم داخل زمین فوتبال یک پسر پفیوزم و بهش افتخار میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95623" target="_blank">📅 15:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95622">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a14dc199.mp4?token=etZ-y2msNAh7IV0PwG09FGLVL8_LNqqzKpZos7YX3go41IgKSYOe9OSPsIWv8huygI00ZwCC3bZcYXqauT-pAz4t5m4f-BtatGNm_Bc4hLtOrskqQ9gu6cKWXtqruSMTqvV9NrnMrznsG-_nh3eVXZ3PGdVDEQWhVIKu-nG9Lcv64c-N0MStVQdOWWYyONfAnDrIDDjPZulJd1ZaGzRXagbkWZ9ULLG08ZOwS6xhzd9GuTUr8o1FUl8Ys37viSzNg31MqSxssNB6sDrw2LQgVHqNekAbcniyeXjD8Je8zt3j3d5Rfx63zmokbTcCBSAVnl4id4_tsXGo153v-bWHOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a14dc199.mp4?token=etZ-y2msNAh7IV0PwG09FGLVL8_LNqqzKpZos7YX3go41IgKSYOe9OSPsIWv8huygI00ZwCC3bZcYXqauT-pAz4t5m4f-BtatGNm_Bc4hLtOrskqQ9gu6cKWXtqruSMTqvV9NrnMrznsG-_nh3eVXZ3PGdVDEQWhVIKu-nG9Lcv64c-N0MStVQdOWWYyONfAnDrIDDjPZulJd1ZaGzRXagbkWZ9ULLG08ZOwS6xhzd9GuTUr8o1FUl8Ys37viSzNg31MqSxssNB6sDrw2LQgVHqNekAbcniyeXjD8Je8zt3j3d5Rfx63zmokbTcCBSAVnl4id4_tsXGo153v-bWHOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیشب صداوسیما این نماهنگ رو برای تیم ملی پخش کرده و اینقدر شاهکار بوده که از آرشیو شبکه سه حذفش کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95622" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95621">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbHprvJj319ehSU5kIxDPcMGzjTmPbheFmiAk0qjVpuh-R1CmgtR-WwAlHSNHTwp7QrG9z1kKA8jjnkWhIOKTGBTFyidz0vQJ2lhW8GjS8Rrje7SPadEX9ts4r_9dCrbS1p6OcDYvYZvd6jMqzDwc46VX7hcq0mnWdGbmrmlSMoG7PD5IynacldwLnNOXOJd_MlHN97McHSpWpr60QbU7pQFZorHwOaRu6zZP4tC7zp1yKsPI7WtfzzBUmtU_68Upfry85TKQEV6BISMb7nxmlfTZl4gUvZQFTo39c36uMGDVFj30VS8cdef8PP8sqKDw3syJIGyhUN5DvM9iqSFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
بانوی‌ایرانی حاضر در استادیوم لس‌آنجلس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95621" target="_blank">📅 15:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95620">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e258c37c.mp4?token=mxHwVwU_fCOzsZjgcfyVl12bVyi8mWL87ZADdsGuVsMAxoIoKsr0hxefeY3eOR4yUHAEu8z3prwd3vMG-fv0GSyp_smPHChAq9_Ry5r3vgZzZaT5bAht7j2QwFb9BmitJNIkbTB53pRcfSboU5OvCJazs0w-o7nKmeFTdxprtsl1TpQkJ-I40pD0pPesp4dVdbwpLyw3e-pZ03ImTGlq4-Gd0y73nz6JNuJb_6G3QwOVYvIZAu5sjIittGyOiMZ-V2QVhs8pduWtu30ENoRVV0Iy_kt1PSRFiTqbPco5mh7vfo0aWclTKiIFMn0qoSH6VnlRKXuHJ_ikVIdGQQYFgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e258c37c.mp4?token=mxHwVwU_fCOzsZjgcfyVl12bVyi8mWL87ZADdsGuVsMAxoIoKsr0hxefeY3eOR4yUHAEu8z3prwd3vMG-fv0GSyp_smPHChAq9_Ry5r3vgZzZaT5bAht7j2QwFb9BmitJNIkbTB53pRcfSboU5OvCJazs0w-o7nKmeFTdxprtsl1TpQkJ-I40pD0pPesp4dVdbwpLyw3e-pZ03ImTGlq4-Gd0y73nz6JNuJb_6G3QwOVYvIZAu5sjIittGyOiMZ-V2QVhs8pduWtu30ENoRVV0Iy_kt1PSRFiTqbPco5mh7vfo0aWclTKiIFMn0qoSH6VnlRKXuHJ_ikVIdGQQYFgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده: ایرانی‌ها در خارج از کشور خیلی به ما لطف داشتند و جوری ما را تشویق کردند که شاید بشود گفت جو استادیوم لس‌آنجلس از ورزشگاه آزادی هم بهتر بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95620" target="_blank">📅 15:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95618">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFK9x0DqICrpQOZtJ1c4hyssjnuF0GUjFN71nx_CRYbPZjnvLO2u5AO2-Nc4hNnUX38hXzRBCPzhaUtMWZX0juQKya2ZIeXDtej2jrsejtt338i1gyCGc_xUt05KiyXqke_AASyfHCRFCbtw74uBJWAcwkjNmMOoMllJlzSKF8PP1viQJ1re6qUysndFhP3Y0fpLqAVduG6Huff7IL_XeqLgAOgNz87zSAhW58d5vHYvIfhOSQ8WWddl9On86u-TmmwDzmxFHzbKbGCDnfSiK7_Yogxi2zKRJTgN41svkQzHrwbT8aCirzsWtM4k0BCvyHi8KAOaB-C5fkI46eMTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
تیم منتخب هفته دوم مرحله گروهی جام جهانی از نگاه هواسکورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/95618" target="_blank">📅 15:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a274e0a122.mp4?token=sr67tATcCCIaa67LopO2jijFNr-dT7DrG1_C1ml5DzQFf9cH7Nm-nXrAbMuOZi1JswX6po1vJsOUjMh7wijKhxNTmDAUSzcOEYPCbLwsNNaIwP8dzXyslvrpeJGgoERdfNwtxWLzaUqz0WFf_paWlmHA7bu_cYKe2Bk8J6jjK3o-Zpj_rxODFzAEhjcm5FlU3GhciW76eYX46uEqqVD9bkLxZXi7dEG06QSq0qhnnedYqOXDP2kV-cIyRxAfLfJT2MWOPj7WgBzWlnWHlnAjOghEasIjkKVgRGNGTFqdPWkBvU0PXR2A0gcU0A-eIgn_U3tBi-cbmQaxqiojbCSx7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a274e0a122.mp4?token=sr67tATcCCIaa67LopO2jijFNr-dT7DrG1_C1ml5DzQFf9cH7Nm-nXrAbMuOZi1JswX6po1vJsOUjMh7wijKhxNTmDAUSzcOEYPCbLwsNNaIwP8dzXyslvrpeJGgoERdfNwtxWLzaUqz0WFf_paWlmHA7bu_cYKe2Bk8J6jjK3o-Zpj_rxODFzAEhjcm5FlU3GhciW76eYX46uEqqVD9bkLxZXi7dEG06QSq0qhnnedYqOXDP2kV-cIyRxAfLfJT2MWOPj7WgBzWlnWHlnAjOghEasIjkKVgRGNGTFqdPWkBvU0PXR2A0gcU0A-eIgn_U3tBi-cbmQaxqiojbCSx7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
خداداد: من خودم چک‌زن هستم ولی میترسم عابدزاده به من چک بزند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95617" target="_blank">📅 14:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9BbG04fCcPs7xwqeExwLtipz8aoQK5VKCzAcCKwb1ZlYCGJZgPFvXAsumST-Wyou6Bw0BFnFxCgRVJMdU4oWtuYlcliEavBvdy0K3mJB3NOmBIaDLjBUJn8_NmOf3spShvHWGiuhwoAne0cBCCsa9bTJLO9gVozp8Nx9ArQlDempZokPdOJtHsJWMIBUUnrkfhREVaEeVhH_NOzx-PkAqC4fldRzqw8_IVF1zOjBqxAJ1oeYUVli4EjivuYUU3xnsXNt9lyH9vXBzSliVXTIGBgvaUq2VgLy5jZ3V_LT08LC3mHhGK4_wenrPTu-JbZ4ZrG2sHGtMiElrZ_Y7ncOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
خبر پیشنهاد الهلال به دمبله صحت نداره و تیم عربستانی خواستار رافینیا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95616" target="_blank">📅 14:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3892238805.mp4?token=OLnKS0phTNxg-1AdAB-TuY0BvoIUD193tZ0oBhwcKnJOLMF5dnovc3L2dxsG6AcC6T1EYm3WlfA9ouQisxNVIjLdrfywEN_f2d2pBPOK_7FwiR21iL2u_Z3ebk8XkqlHjpVBPG_04SzACjp40S5g9iDtFd821DUO7DLe8LXCRrF1MEnqCEkuq0HLu3TsQfYSmCXS8b1WJYTDayHMUF8NoxZGmuNkMc5R0R022Y09hLNwa6865PVbUrcsBgLgSgt-exk-hJdxGNSGsBVSnhFUb0XeJcr2Dh4hWfb72eiQlZfGZA5rZ_1t14O0Eprcygw7yjaTQ51AO5z4HCMDXe1kHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3892238805.mp4?token=OLnKS0phTNxg-1AdAB-TuY0BvoIUD193tZ0oBhwcKnJOLMF5dnovc3L2dxsG6AcC6T1EYm3WlfA9ouQisxNVIjLdrfywEN_f2d2pBPOK_7FwiR21iL2u_Z3ebk8XkqlHjpVBPG_04SzACjp40S5g9iDtFd821DUO7DLe8LXCRrF1MEnqCEkuq0HLu3TsQfYSmCXS8b1WJYTDayHMUF8NoxZGmuNkMc5R0R022Y09hLNwa6865PVbUrcsBgLgSgt-exk-hJdxGNSGsBVSnhFUb0XeJcr2Dh4hWfb72eiQlZfGZA5rZ_1t14O0Eprcygw7yjaTQ51AO5z4HCMDXe1kHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم بنگلادش که بدبخت تر از ما ایرانیا هستن، این روزا تمام فکر و ذکرشون شده مسی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95615" target="_blank">📅 14:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRNDH8IpUKf6Og99R9SeLlUyY9tNXH5urBg1wgahTbXPvb-1mhCo1309mQ571_vywvNRvFoEfrewgU7Gg4CGd35jdZ2U-PZCfIrNl_JY33TluW1fZYNv7BZoLm8LDn8rckBkdd-4ELdp5EQLpOoP5QAJk0zVRVV3I-QdvlXjnMI4X9nThyE3hXl-E7yMvLAq7O_UMp-wtESQ9-5ojs-j0iLvXMH8q5ekXEnXrmKsIURZgJdM7PHz9lRzTWLypnfwmZL0k09L_pgIjMxhRsq0ihLfkzieBXWWaoPkmYGQV_UPaYlW-GW3-6cftalg1kCCpJfs8B39ywx4Kz6ZYsmNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💋
📊
لیونل مسی پس از پایان هفته دوم بیشترین شوت در چارچوب رو در جام جهانی ثبت کرده ؛ ۸ شوت که ۵ تاش گل شده
‼️
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/95614" target="_blank">📅 14:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95613">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8e892beb9.mp4?token=pKcL8XhfYZYrpqetMWjbnTvXMT1gkGz006CPzOX5dMZ3CTahNDlrpsnJ4dC1nH8PzXnow4Y08rWkF2LXWl0zCRGpJKLsUrgIlHwp7cl8j1Csf8Dfn9u_9r7vnAcoe311Cyi2wp1_HG064QpihHlHMOBoYh0GwuMfYM82ROdAq3JcR2iWQRDhBGQ680hORJD77jNnZp2u_B4ZMPxsrMgwo6p0UJDAcVREOkt5Ep6CbkrpBgMma8faBZObJYu75oLiobByZV_PHhsPEeEj3xg3rUSztOV-IZ130yyPX1FrGKPvJ2T5TufC1gW8Fa8DIV5OOf8UrTxZV7PgaIUQjcYGZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8e892beb9.mp4?token=pKcL8XhfYZYrpqetMWjbnTvXMT1gkGz006CPzOX5dMZ3CTahNDlrpsnJ4dC1nH8PzXnow4Y08rWkF2LXWl0zCRGpJKLsUrgIlHwp7cl8j1Csf8Dfn9u_9r7vnAcoe311Cyi2wp1_HG064QpihHlHMOBoYh0GwuMfYM82ROdAq3JcR2iWQRDhBGQ680hORJD77jNnZp2u_B4ZMPxsrMgwo6p0UJDAcVREOkt5Ep6CbkrpBgMma8faBZObJYu75oLiobByZV_PHhsPEeEj3xg3rUSztOV-IZ130yyPX1FrGKPvJ2T5TufC1gW8Fa8DIV5OOf8UrTxZV7PgaIUQjcYGZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی عجیب هوادار آرژانتین بعد گلزنی مسی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95613" target="_blank">📅 14:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95612">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013e39db64.mp4?token=PWHUJTOpjSrlT_pXSu85jI1XBT1OkFNfhleB9_NUWmVJxABLW0gh-2vxdFKYblkQuwRmIC1LBABTNJuCkQ26fd4GyzJdheJfE8uXYnbAHNqPBV_XGfE5aWJG94OX7IjeYw-kDCpNHKs0Ju1uF5rt3vE4JNPIxM325-f6WxLRc8okNzss89v3-rQKqmald2dB1GspyC99RrrK5XxzH0fI3-MCDOt_6QnSGUiPQmCn_Yv95K0qvUG-ts5H8QVWcqQ0ybkXobw8WwNET8xA02qKJwBJIsCJU4oLIzqSKp51nCs7qlPpzQcwT4dpjK06Wjk3MF_eh2TukDCcD_3IRbn54Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013e39db64.mp4?token=PWHUJTOpjSrlT_pXSu85jI1XBT1OkFNfhleB9_NUWmVJxABLW0gh-2vxdFKYblkQuwRmIC1LBABTNJuCkQ26fd4GyzJdheJfE8uXYnbAHNqPBV_XGfE5aWJG94OX7IjeYw-kDCpNHKs0Ju1uF5rt3vE4JNPIxM325-f6WxLRc8okNzss89v3-rQKqmald2dB1GspyC99RrrK5XxzH0fI3-MCDOt_6QnSGUiPQmCn_Yv95K0qvUG-ts5H8QVWcqQ0ybkXobw8WwNET8xA02qKJwBJIsCJU4oLIzqSKp51nCs7qlPpzQcwT4dpjK06Wjk3MF_eh2TukDCcD_3IRbn54Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بلاگرهای کف‌خیابونای جام‌جهانی رو می‌بینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95612" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95611">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gef3VwsZJyjTRS8LmsNrvtHDFgmbJsNo8UZtVJzYd990I-VR4FJhm0hO-D0QPZdgxVhgzangtmssRIn_RoNMeCqD7gng_2VzbSqDpP7aI0YQATZsnzbi5u-ElkrG-Ccp_njTjEZKpmxduODKSvOGSSW3i08hhU7zgjvQwxqWKTDyRNPjZI6H06H8B5iHln6fEMf6GDO986qWvNEKn4ZKXyKgKx-DyvRDVIHismG3Wqv_7rKzCUqrthhaYHIpqh1Hucwe-R1IpCjQeooZGse7lsf5C2EUNXBxKCsyejhxCn9CBg23u3ZiDOepMa_7dyugjMZ-uteOghcP1qMTdJiJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
آیا میخوای چند سال دیگر به بازی ادامه بدی؟
🎙
لیونل مسی: "بله، بله... مدتی ادامه خواهم داد، تا زمانی که بتوانم کمک کنم، احساس وضعیت بدنی خوبی داشته باشم و به هم‌تیمی‌هایم کمک کنم... به بازی ادامه خواهم داد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95611" target="_blank">📅 13:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95610">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbB5t5bvUxUtZPzzU-BuqyOh_H3e5GtYmwZWr9mhFfSsIDa5NYDYPBOiboqm8PUUYfHTNnc7dsMJXHQhqVV5IHGDSqiYeUhUBL5arwa2y9P1GR-18VN2xpAIMrTFbTOQx7rGeSYwQ5p0DQaxRCufpnZl6UPHneMoEEEG6D0ZbflOTox-gUSE1rY77CZySLdOobQrgfF5Je6bupgXc-dN0HMnYl15M-tL2aa6Sj0pcMoD-Pv_V4QJqg7ypu0UxVM_yu0j34OaWXd_YUKXDJV9gq71AoHvB9r_RB_4cSJPM6exKYZTFPCwrUvTsaBJFh_Vkiv9Zxb9pFVm1E-wL8ecYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
ماریو کورتیگانا:
مورینیو دوست دارد باشگاه رئال یک مهاجم نوک کلاسیک شبیه خوسلو جذب کند، اما این موضوع فعلا اولویت اصلی نیست و برای عملی شدنش، حداقل یک بازیکن باید از تیم جدا شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95610" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95609">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgivY98dYHu1aP4qO9WvICXDPSXjV3I-8J0bEYWD2QXqmtCe7u2ilpFgDtpfo4uunS7Ritz-JeRA1i1aFbcyPhki7HWgHMKLyG4lcOtoiJS_fCjONKxF-mAHbvf8owXRwpG0cMkQgjm4HwF0hFmwCSvDBF6DFGS9IcA0MX3LZhDn8QKNDUUSvAhNysaSForwzNb_DCDdek_eVHTe4cJhpwcNi2NkZhLN1RZyyOW6H-aEwYkARHaM6YDqBElh3SOGW2kDc-lyakG0hGWV2WrYpf7aijeN0NdpCwKapWYUyjcA1jdVgJM4XZ05_T0Gy1RRtuGNf6f3M0N7GpY5rkrp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7 بازی آخر مسی تو جام‌جهانی
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95609" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=BeWL7FsQDwb39M-4BLqEyhP8HEEZVIaLirm-qj5aPnwwvkucudC9n9od4BouFPT2lHz56ef84YR123Ol8MgEdoplBQWizkOfa6qKKDwmXsNmplb4wuenjzkxLa6jHTG_HidWXxiwpA0AxmV9oMvsVIZ1I5bV0shXOwjbuwArJEmAVdb7J2n6iqlgrGrOq4s_09Jzosfx1xmqUNxzeseALojwTj3eItRg1Oi3y-A2drGyWb8lq4s1nWe8Obk6XKf8dc-O4Z-jxZwR6VvUVFfD_j8h16x6oYOpJMiUb0yQQkTVIjSLpSjlHD7_exm6C2UQJfCXL6gKNF2Cv84d_ZWjSkMkPJ9pOqMQEVh1iw7m7_QxTMEAWYLwNpZP8_i2hkLDQ0JIc4zsFTWMrrcgIsPUq7tO0LFZsKm7R4ZsR0eontF_TBiFFAcoVPHOw_tqHCOKOSqDYsx5xNR6NuNEwABrNjsYY9FeLpCUa0XuOb602BgaqqjkgVRYo-KzT1N_Ledf64iKNrF4S__z7HbTMrjuH838ZXFx4AMpssgIHcI_G9T6-2e6Scax9-uXpRI4ZnMoSHGR6SnP6od1OXzMUZJ-f_o_L27_S9gOGe-gJu4_uVWnWPGPZ2c1xHIHBRNAlgx87Js2X2adywu-7DVjE1XaxsVI5aEMliqL1dwMXBV2ojs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=BeWL7FsQDwb39M-4BLqEyhP8HEEZVIaLirm-qj5aPnwwvkucudC9n9od4BouFPT2lHz56ef84YR123Ol8MgEdoplBQWizkOfa6qKKDwmXsNmplb4wuenjzkxLa6jHTG_HidWXxiwpA0AxmV9oMvsVIZ1I5bV0shXOwjbuwArJEmAVdb7J2n6iqlgrGrOq4s_09Jzosfx1xmqUNxzeseALojwTj3eItRg1Oi3y-A2drGyWb8lq4s1nWe8Obk6XKf8dc-O4Z-jxZwR6VvUVFfD_j8h16x6oYOpJMiUb0yQQkTVIjSLpSjlHD7_exm6C2UQJfCXL6gKNF2Cv84d_ZWjSkMkPJ9pOqMQEVh1iw7m7_QxTMEAWYLwNpZP8_i2hkLDQ0JIc4zsFTWMrrcgIsPUq7tO0LFZsKm7R4ZsR0eontF_TBiFFAcoVPHOw_tqHCOKOSqDYsx5xNR6NuNEwABrNjsYY9FeLpCUa0XuOb602BgaqqjkgVRYo-KzT1N_Ledf64iKNrF4S__z7HbTMrjuH838ZXFx4AMpssgIHcI_G9T6-2e6Scax9-uXpRI4ZnMoSHGR6SnP6od1OXzMUZJ-f_o_L27_S9gOGe-gJu4_uVWnWPGPZ2c1xHIHBRNAlgx87Js2X2adywu-7DVjE1XaxsVI5aEMliqL1dwMXBV2ojs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده: علیرضا بیرانوند وسیله بود و دست خدا بود که اجازه نداد شوت بازیکن بلژیک گل شود/ در حق بیرانوند خیلی نامهربانی کردند و حالا کل دنیا در خصوص بیرانوند صحبت می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95608" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95607">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYeUJCdcdHT0W_5ukCJPB42aIJYfnJRymqZKJzaX1J8hC0QrtDSxxsP5RA2emUPTAxxDJmueSDQTdHi9tOlEyjx30TxH4Fq2iNDgzYcZaEjKnvS2ksYzTbst0zU0Gs_4_GS8HS6hwUlJaXtBoh8WGt0Q4bnd-oylW5TV564RrLEaVOJD7FVF7nZaaflUqva6GoMGbQRBzU-hzKzKsvBfQ5Jsr-coLCiVFpBJtLuvNMRuF2d8r0RAcrhqx3fE1tZcwrRxpKGZckxXtXdqmJrz5oxII9_4l1kkG1pnql2np-PJ-3wBA0UOWiEtA8Vzkfz5cVc0bu6fIUwwOA0PFoXomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇦🇷
زوج آرژانتینی با یه بچه تو شکم اینجوری رفتن اسطورشون رو تشویق کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95607" target="_blank">📅 13:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95606">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b5dc5848.mp4?token=Cm28Cf7m_0AlW1m9HbAg6i_VjyQWLU5fb9pQu404ygraB7uDSzVbww6Tbopymo8p0JBm1YdwgBMDY6r22tTkzehxpaDb2tBr-3f3bvj1LtYnJd655TGsk5a3INhFRkiyCmFXoTtq1pZoXDdzIzh_zRd1CblCpOjCutZwp4uFJgWs75rcHtZUKjZnR65pwAtEXSfZ6V6GZhTG3Z4g5uhyb5Vpwod_xxK-j7g32NylrynpREmdO9Q-QLOuc-WV6gAG4-fWyb16GequGZr-9DjzzWeHSQu9hRA8ZKDXRxV0lu7f1PrcLFvCInOx0Qo9cCVgWwZhvdihDT1-CP6dpsPFw5hO5tPqqQySpsy8oFm5UEwwGFqqLNV__zsEB6qdAaMlb-pX8bmeOCZSB3fmlLTx_k_Jv_5Mh9EU11MW5bogXLAYrACszfjr67LQaLtkLI-4svD_aAaTKMeabxzScWjLE-xjl7n9gCxLsljJ50L6Ko51vv_crZ2L1gcfKUUbYsH46OuhjrG46g25N7mPXSR5skTXRXBbEsBGZKAjV-iJrn8l3qNuFN5QxcXyDcLve1bDRZK2jdNxZ0E9SzD2IzvXmYazGk0_Ko3BZgzb_rXQTZCmuFtuZ-Bik-xBcRjX4Qi5P-g8Wy-zWKVrcjQ46jAia7OsAtaf1mkGRXNXCmJj5Nc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b5dc5848.mp4?token=Cm28Cf7m_0AlW1m9HbAg6i_VjyQWLU5fb9pQu404ygraB7uDSzVbww6Tbopymo8p0JBm1YdwgBMDY6r22tTkzehxpaDb2tBr-3f3bvj1LtYnJd655TGsk5a3INhFRkiyCmFXoTtq1pZoXDdzIzh_zRd1CblCpOjCutZwp4uFJgWs75rcHtZUKjZnR65pwAtEXSfZ6V6GZhTG3Z4g5uhyb5Vpwod_xxK-j7g32NylrynpREmdO9Q-QLOuc-WV6gAG4-fWyb16GequGZr-9DjzzWeHSQu9hRA8ZKDXRxV0lu7f1PrcLFvCInOx0Qo9cCVgWwZhvdihDT1-CP6dpsPFw5hO5tPqqQySpsy8oFm5UEwwGFqqLNV__zsEB6qdAaMlb-pX8bmeOCZSB3fmlLTx_k_Jv_5Mh9EU11MW5bogXLAYrACszfjr67LQaLtkLI-4svD_aAaTKMeabxzScWjLE-xjl7n9gCxLsljJ50L6Ko51vv_crZ2L1gcfKUUbYsH46OuhjrG46g25N7mPXSR5skTXRXBbEsBGZKAjV-iJrn8l3qNuFN5QxcXyDcLve1bDRZK2jdNxZ0E9SzD2IzvXmYazGk0_Ko3BZgzb_rXQTZCmuFtuZ-Bik-xBcRjX4Qi5P-g8Wy-zWKVrcjQ46jAia7OsAtaf1mkGRXNXCmJj5Nc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال شاهکاره
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95606" target="_blank">📅 13:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srPT8VmAf76DxD_NR9BxmK5JmX-5mlvNPgBg-R6Dssa8s3mDrvuvmOY3kDygZOk87JeoW5FXdHEbiSFmqWMZ5-O7vCP8wddcRYEl0I0tn7yEMshFe6pzQQEGqoXjtvGo6eFoEe1tab73X6NtDtqypsL9qJfqKYyvplcs7Ansi3R7kJhVLd15blih-QT-u6mFuPeS3UOdVH1dbvptqVn7d40v7abbWTPbTeduUU_CkhQ-datFfQPXe6qdhGeO7tGZXldWeaqHRkzdh1TDfUSA83TaOqtHIAYyvI1GlgtpBr1YkB7d3ixBL3tq8VhfAl1lknWTE2HN9Jt-wttYW805Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد لیونل‌مسی به تفکیک هر دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95605" target="_blank">📅 13:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">💥
🙂
یه خانم ایرانی از مراحل استادیوم رفتنش در جام‌جهانی شامل حموم رفتن، لباس پوشیدن و ... برامون ویدیو گذاشته و گفته ببینید
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95604" target="_blank">📅 12:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb84abe0b.mp4?token=Jn9rxb-jDd5RCRKCydnV4X2U6gh3xlhvElPqWXpOV2FxBErMQA7Zgf509V1F54-onKlibYcpRsfPCBetiSAY9_CN_CBxBVVONQyke0z1QAEOd0x_zRjvuqXLassX2EkBmvXkewAcK8HJqcEFOXKQSNdK5i2p5AQJpdU3j_JkROk8cYgOHFLM5SlQzUr_k9sW5VLhSaj9jws65oAUIkQLbuGu4C70mU5NsQNzxF4DUh7DBqYY_i6bq1N2Fe2uKArqMFUZoPmFhZoE4-CeMY65gPlJHVGmbomRPe7LD_cianxst_J2gSyrxRazl15WhCYUph6GpgDEMK0aGGu2RcFFmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb84abe0b.mp4?token=Jn9rxb-jDd5RCRKCydnV4X2U6gh3xlhvElPqWXpOV2FxBErMQA7Zgf509V1F54-onKlibYcpRsfPCBetiSAY9_CN_CBxBVVONQyke0z1QAEOd0x_zRjvuqXLassX2EkBmvXkewAcK8HJqcEFOXKQSNdK5i2p5AQJpdU3j_JkROk8cYgOHFLM5SlQzUr_k9sW5VLhSaj9jws65oAUIkQLbuGu4C70mU5NsQNzxF4DUh7DBqYY_i6bq1N2Fe2uKArqMFUZoPmFhZoE4-CeMY65gPlJHVGmbomRPe7LD_cianxst_J2gSyrxRazl15WhCYUph6GpgDEMK0aGGu2RcFFmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای‌مسی ببین کاراتو دل کیارو بردی
💥
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95603" target="_blank">📅 12:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95602">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b24eddb0.mp4?token=oRdx6AJlCOfNnxsB-hpUX0EgFXeXC83wKsTQ2Hx8Zbg9adD2c_tGzCagNrn1ryZM5NKkwQpkHT4YauO3lTMpV7AX-BjE-OioI55s-bKHrwTaEVd9RU0wMPRzMxIQ0WcfhE9wH-IwsEaDBC3z9gNFkhOXMruMbbOeATm_WIezLhHry8Q0c0VDnG-8pGYWy_GZF8yAK2quLMCEy4rdLwVkpMJuBv2QVondwcU40nSaxp-jl-RWkG0htZ9kXayQNbrvsCfljN_WfpbbAoAElCN8059tn8BPMBbFt05PM5w31HwuhWoPzQjfw8lGRcqC-O6Yyd-MS8le-iwCK5rHTqezzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b24eddb0.mp4?token=oRdx6AJlCOfNnxsB-hpUX0EgFXeXC83wKsTQ2Hx8Zbg9adD2c_tGzCagNrn1ryZM5NKkwQpkHT4YauO3lTMpV7AX-BjE-OioI55s-bKHrwTaEVd9RU0wMPRzMxIQ0WcfhE9wH-IwsEaDBC3z9gNFkhOXMruMbbOeATm_WIezLhHry8Q0c0VDnG-8pGYWy_GZF8yAK2quLMCEy4rdLwVkpMJuBv2QVondwcU40nSaxp-jl-RWkG0htZ9kXayQNbrvsCfljN_WfpbbAoAElCN8059tn8BPMBbFt05PM5w31HwuhWoPzQjfw8lGRcqC-O6Yyd-MS8le-iwCK5rHTqezzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
توصیف عادل‌فردوسی‌پور از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95602" target="_blank">📅 12:01 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d01060f01.mp4?token=tUIb6pCb5016XgWJIUB0w2DyCJYZQdUTmmVj6H5ixBivB58AG2hN92K9vIdWSPAFwxkftld4BYEeiEgFNWoufk4Sz77AWRjtah7-FdZzBKg4P01BasH7H8LQBuOIKRbtXJfNL6YJhXQVAhRYo7WU25NCaeWNc2USj6Bml9Ugs9twlUk5b_d6GDxM6bHEEyCZuvy3DkdzorwqKEVAzTE-CsSWh_oFOEW9fr2bYWvIA4iOmdN51EUAbQ5QzInGg9JBCHgUrgxEJGt4ERHOXllfvaYiEN23T71kBVaIzxNxHt5Dk3VeR-o5Gyo3ZT-jQmPWN1e4uKjFzloC6sxOBZI-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d01060f01.mp4?token=tUIb6pCb5016XgWJIUB0w2DyCJYZQdUTmmVj6H5ixBivB58AG2hN92K9vIdWSPAFwxkftld4BYEeiEgFNWoufk4Sz77AWRjtah7-FdZzBKg4P01BasH7H8LQBuOIKRbtXJfNL6YJhXQVAhRYo7WU25NCaeWNc2USj6Bml9Ugs9twlUk5b_d6GDxM6bHEEyCZuvy3DkdzorwqKEVAzTE-CsSWh_oFOEW9fr2bYWvIA4iOmdN51EUAbQ5QzInGg9JBCHgUrgxEJGt4ERHOXllfvaYiEN23T71kBVaIzxNxHt5Dk3VeR-o5Gyo3ZT-jQmPWN1e4uKjFzloC6sxOBZI-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏆
اثرات‌هنری خیابانی در ایام جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95601" target="_blank">📅 11:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e418f52b9.mp4?token=T6lI7GwVmzf-mcKaM2-7uzXhdB-1dBWWg9triviatCvaP2oa7zkPR79wV5nPbS8IkocElhfJoPH9oVe3BWNutOmoALFZhPo2B8GoZ9R3CM3LorK_P7W-u7A6x1mljIsPXLguVapnRUTjv_Y78solvHZubH-kdQBOkEo3D07suneu5Qsf--OSJXfRaA3rJZoSr4hILu2kxuHhsFPSU-DNL0jT3Gm9s0INqWgpDxh3hB5zzbDZQ_vmKJiPAw-WtkhfFsbHzmOp16wU8Br7-A75SNh-EiEocPT3KE8YUHew-gb8AreNAYXqr0wMEsDbrhNwNVn3yssLDPxy8giIST4hew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e418f52b9.mp4?token=T6lI7GwVmzf-mcKaM2-7uzXhdB-1dBWWg9triviatCvaP2oa7zkPR79wV5nPbS8IkocElhfJoPH9oVe3BWNutOmoALFZhPo2B8GoZ9R3CM3LorK_P7W-u7A6x1mljIsPXLguVapnRUTjv_Y78solvHZubH-kdQBOkEo3D07suneu5Qsf--OSJXfRaA3rJZoSr4hILu2kxuHhsFPSU-DNL0jT3Gm9s0INqWgpDxh3hB5zzbDZQ_vmKJiPAw-WtkhfFsbHzmOp16wU8Br7-A75SNh-EiEocPT3KE8YUHew-gb8AreNAYXqr0wMEsDbrhNwNVn3yssLDPxy8giIST4hew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚠️
پاسخ پیروز قربانی به اظهارات یکی از اعضای کادر فنی ایران که گفته بود: «شانس آوردیم فجر سیاسی تو گروهمون نیست وگرنه کارمون برای صعود خیلی سخت می‌شد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95600" target="_blank">📅 11:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428b85f0a6.mp4?token=P2Y79AJLZXFyUaAlM3CesDnfg5SKKPnoh2CTD__2WEWp-VJt7CldJm9WotLdiZ6FTF2ehd0qDqzsZVC4TG9XB1E8MO6YvDXXmcNzEl34Nun5hJcJ9aFXI-Bgz9c1o9oae5eOgC_PutIuidpx1aaXE8y-xDiW90RY9wXrD2NtUWQBhBHcIpLO2HR_gxjj1c-MeMd89Cp9yJnWOEVKEGYFBJzYgIHMqiEJ8x3AzeKR9i6nKQioFZewk-fPUBfMavMCONng5zJs6EKe3tCwIlu-iy9GzsxzfkNXr4hZNrJSkKEy09JDA9cwYvh2W6C180jXBKc4XXMLly3tE-GmoA60jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428b85f0a6.mp4?token=P2Y79AJLZXFyUaAlM3CesDnfg5SKKPnoh2CTD__2WEWp-VJt7CldJm9WotLdiZ6FTF2ehd0qDqzsZVC4TG9XB1E8MO6YvDXXmcNzEl34Nun5hJcJ9aFXI-Bgz9c1o9oae5eOgC_PutIuidpx1aaXE8y-xDiW90RY9wXrD2NtUWQBhBHcIpLO2HR_gxjj1c-MeMd89Cp9yJnWOEVKEGYFBJzYgIHMqiEJ8x3AzeKR9i6nKQioFZewk-fPUBfMavMCONng5zJs6EKe3tCwIlu-iy9GzsxzfkNXr4hZNrJSkKEy09JDA9cwYvh2W6C180jXBKc4XXMLly3tE-GmoA60jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
خاطرات جالب کاکا از حضورش در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95599" target="_blank">📅 11:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95598">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da82d3a5fe.mp4?token=EIcQKramfZsaFPvPdzM2E6lbreFZflHTAPKtwrUkD0Wt6KtWlhiAfbtRZGeXjrgdrR1vA-OdUItbbW-T1C_YgfJ-5f5ncV7vb1aiW-BwbQYgYQx_hfnF0k6KJDwDsuVFcy7tEyQSC8k4N8Jerz8J0UVdbgMxQY-0y7hc6lQd08ZR-VXSLrJ681-3_bFTbRTQ7OGSb2NZ37HSjReaohiKQviik57Y3AEk7KVMhjUcpHMX_pjwQdmdSuDbjIGeExfhkk9xb3hFnlOO0KrZ_WU874oTzhRNK7nmS7lS6IgjRLuLNteBHVs94dmj8ARLIMDv1iqKe9e7EcMLjwBhxpMM7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da82d3a5fe.mp4?token=EIcQKramfZsaFPvPdzM2E6lbreFZflHTAPKtwrUkD0Wt6KtWlhiAfbtRZGeXjrgdrR1vA-OdUItbbW-T1C_YgfJ-5f5ncV7vb1aiW-BwbQYgYQx_hfnF0k6KJDwDsuVFcy7tEyQSC8k4N8Jerz8J0UVdbgMxQY-0y7hc6lQd08ZR-VXSLrJ681-3_bFTbRTQ7OGSb2NZ37HSjReaohiKQviik57Y3AEk7KVMhjUcpHMX_pjwQdmdSuDbjIGeExfhkk9xb3hFnlOO0KrZ_WU874oTzhRNK7nmS7lS6IgjRLuLNteBHVs94dmj8ARLIMDv1iqKe9e7EcMLjwBhxpMM7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای‌رونالدو بالاخره دختران سرزمین‌م خوشحال کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/95598" target="_blank">📅 10:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95597">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=JyPR4ZpsvcpaWA0AYDYas9NGFCZiiDp9vFAsOJL6G7_kLVT92tm4RGTu2grgPoiGNm6fprf7Y8rBiDnOFp86NOn_4HUMiqN2idlI2p_Nnwfw27msbsXPdWW-i_WzG27D3y9TUNO4RNM4oOwcrd9IfdYxLRktNDzHADoo3PonjmMglxNg5cQuKszJxtYbyP2FG_AjwiAdsJm59RaWIs9jgI28UqWEsRmcLXPdQI3BxWRTeDAdV222jCofK6PYPonbF1er2mNltyP0QRunuxo0LYvUKLKgSw9HYbq-nLQEXZ043yvw-iY7uaRi3C-qSDWekdTKizrbSqcqbyTzj3jPlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2607379b.mp4?token=JyPR4ZpsvcpaWA0AYDYas9NGFCZiiDp9vFAsOJL6G7_kLVT92tm4RGTu2grgPoiGNm6fprf7Y8rBiDnOFp86NOn_4HUMiqN2idlI2p_Nnwfw27msbsXPdWW-i_WzG27D3y9TUNO4RNM4oOwcrd9IfdYxLRktNDzHADoo3PonjmMglxNg5cQuKszJxtYbyP2FG_AjwiAdsJm59RaWIs9jgI28UqWEsRmcLXPdQI3BxWRTeDAdV222jCofK6PYPonbF1er2mNltyP0QRunuxo0LYvUKLKgSw9HYbq-nLQEXZ043yvw-iY7uaRi3C-qSDWekdTKizrbSqcqbyTzj3jPlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇶
#منهای‌ورزش
؛ ویدیو افشا شده در جهان از عیاشی و عشق بازی مدیرکل پروژه‌های نفتی شمال عراق با منشی خودش که مثل بمب تو جهان ترکونده. ظاهرا این فرد دستگیر شده و وزیر نفت عراق هم قراره اخراج بشه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/95597" target="_blank">📅 10:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95596">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6f6841f1.mp4?token=TKotApQPN7K5rR7pigk7iP2jeiIqnHa5VAbcQN98owedEFyZXKGNC4KkMI3hUNPbTctEwCP9qjTh0mp2k-RfW2SkcBXJ5g9TsGKR52R7XmvGGwtX9Yf2RaokWW2Lb_CNXWxww65HWUnUhMsI4VyJcJd_xJHQaN-K9L6XhZq4bvqzvKtX83OJeU3ts0KZlCAEqHTNNUX6ZEg8gTkzYYqZZmo9ahI7HzUf-Y69io9sXgTSy_kKjBy53aThu36UyclVGBtYYaqv5OWvy0LoZkpoZaym8WO4NSDqRqSDMBOGppg4cGe0ncAFc8Y4m74DNm7elc5EpUOLaLtzIIlTiS3Bkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6f6841f1.mp4?token=TKotApQPN7K5rR7pigk7iP2jeiIqnHa5VAbcQN98owedEFyZXKGNC4KkMI3hUNPbTctEwCP9qjTh0mp2k-RfW2SkcBXJ5g9TsGKR52R7XmvGGwtX9Yf2RaokWW2Lb_CNXWxww65HWUnUhMsI4VyJcJd_xJHQaN-K9L6XhZq4bvqzvKtX83OJeU3ts0KZlCAEqHTNNUX6ZEg8gTkzYYqZZmo9ahI7HzUf-Y69io9sXgTSy_kKjBy53aThu36UyclVGBtYYaqv5OWvy0LoZkpoZaym8WO4NSDqRqSDMBOGppg4cGe0ncAFc8Y4m74DNm7elc5EpUOLaLtzIIlTiS3Bkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
وضعیت بیرانوند دایرکت دخترا بعد بازی بلژیک:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95596" target="_blank">📅 10:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVSi-X9JX9Kueru6VzoZUa_1oAlaOf-2CBRWdmUtS-nv41Qu1x99YYtBf7wu-zBbFTNrBo6FVwlZJvCfd4w70erAt_-MlNyC21tjTX6ywpN8Trio8GP5jDBMfpQrDIlGh9rEMtq_uz-XsXncgpu-fg_qP4uy3knAlbTyDBHHqh5QCRx5s2-2TwA3VDjYQvAkteYXhcR4Ka0lFJJ0ptIjA2edxsWnQ53FksAW0fAJXU32MSLFF77Mf5ooduttdhR9JYIe60G0HqJnf7yHwmLM0uZchl4j6Lq6nyVRZTSv9TcsDAOVXmzFpSVb71jSq4QBr1BCrmc1hIRkTZk7DOtCmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تن و بدن بوفون تو گور لرزید
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95595" target="_blank">📅 10:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95594">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf00b678f.mp4?token=WN4n8FbLnWUS4dW6yvkB5C2Zug7MN4GpPmpCon55HKqxFCWmckjxnwpbRs7xIcQEdV59jbnQfJTpMDKyryPGIU_cuFybrWZY-ggnuPWm3L2gpquuxYHhQsVapBxRcKLjoY_B22PGouQYU957n1YFYkAgd6kNUfKjFyx8p4-Pxplhi_mGNrvNe_cC9xgTmxgJl9W0LgvUifOiNXajKSC2dJSsD3o6favrDLm-L6oBxYZtC3GtwpxQRMqiJBHiupU52n6guql4talzrb786iUSutCjixG8P3aovSYLniBv8U9Eu_VukalAkedThG7xsPQPt1IiROcdEZp3kNPTGNfMRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf00b678f.mp4?token=WN4n8FbLnWUS4dW6yvkB5C2Zug7MN4GpPmpCon55HKqxFCWmckjxnwpbRs7xIcQEdV59jbnQfJTpMDKyryPGIU_cuFybrWZY-ggnuPWm3L2gpquuxYHhQsVapBxRcKLjoY_B22PGouQYU957n1YFYkAgd6kNUfKjFyx8p4-Pxplhi_mGNrvNe_cC9xgTmxgJl9W0LgvUifOiNXajKSC2dJSsD3o6favrDLm-L6oBxYZtC3GtwpxQRMqiJBHiupU52n6guql4talzrb786iUSutCjixG8P3aovSYLniBv8U9Eu_VukalAkedThG7xsPQPt1IiROcdEZp3kNPTGNfMRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
حسین‌کعبی: از ابتدا استقلالی بودم.‌ پس از حضور در پرسپولیس با برادرم دعوا کردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95594" target="_blank">📅 09:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95593">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/413019d639.mp4?token=bHrN2tZwKe18_0xG5eKxYJb_PRFocv7JMtWlOEE7uDI6XetcqfgnXV8_4ZYPakjO250QVAZnsHaZde9tlfbnf6oOdFU75NTilb7T0HwCrbv0hBNPoSwcFD0MCau5960TBLK-UlcVpMNq8c5ypr6BCOr2VAJGYMKdb1h8mU3VqquQxosucK7b_6f03xnUvwrBSt_YkRstKCbUGr-MS1L6f1FQ8fZy08VpjQPGsYh-PHCtL1QFFit73mKdKndAawejO_yIEcIyBXm3sosxvhmc7h9yWPHnRMzftoubgO9yC5Nvfub8yjgKPjaISaakPMgI5HMsW-BDr1DxSIfW_I_n6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/413019d639.mp4?token=bHrN2tZwKe18_0xG5eKxYJb_PRFocv7JMtWlOEE7uDI6XetcqfgnXV8_4ZYPakjO250QVAZnsHaZde9tlfbnf6oOdFU75NTilb7T0HwCrbv0hBNPoSwcFD0MCau5960TBLK-UlcVpMNq8c5ypr6BCOr2VAJGYMKdb1h8mU3VqquQxosucK7b_6f03xnUvwrBSt_YkRstKCbUGr-MS1L6f1FQ8fZy08VpjQPGsYh-PHCtL1QFFit73mKdKndAawejO_yIEcIyBXm3sosxvhmc7h9yWPHnRMzftoubgO9yC5Nvfub8yjgKPjaISaakPMgI5HMsW-BDr1DxSIfW_I_n6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">8
سال قبل در چنین روزی؛ تونی کروس از زاویه بسته دروازه سوئد را باز کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/95593" target="_blank">📅 09:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cab47625ee.mp4?token=Up1sQ5kqMjI-xpi_ncMKK9B0BflXyedWqg2uDkGJaUKa3hFq4xzuCYDY2_aMdz_VqLbhqB6xXPsaeeT-J6nk0Fm2iKX6vPtJKLaoPvK9IjyXYYEnDbasY0T_VPtzO5eQMfPmt6ZFT5O96wnav54f1GnYLVceumvaoAgg9eilpJiP33La6x0keX9y52fQE9yhQSaWasWGluNTGmLiQdbG-qjdbgBWtqUv_IVfNQbwCDWpMuBgwU7fwTCt9tud09iEQrXxvQQ8QPhXUICBDENBsx38svwgvthahg715OQf2p-aSylS4Zu7Fqtu9aUicROdMcCsNqXK3yzTmEJ10ej4DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cab47625ee.mp4?token=Up1sQ5kqMjI-xpi_ncMKK9B0BflXyedWqg2uDkGJaUKa3hFq4xzuCYDY2_aMdz_VqLbhqB6xXPsaeeT-J6nk0Fm2iKX6vPtJKLaoPvK9IjyXYYEnDbasY0T_VPtzO5eQMfPmt6ZFT5O96wnav54f1GnYLVceumvaoAgg9eilpJiP33La6x0keX9y52fQE9yhQSaWasWGluNTGmLiQdbG-qjdbgBWtqUv_IVfNQbwCDWpMuBgwU7fwTCt9tud09iEQrXxvQQ8QPhXUICBDENBsx38svwgvthahg715OQf2p-aSylS4Zu7Fqtu9aUicROdMcCsNqXK3yzTmEJ10ej4DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
پشت‌صحنه بلاگرهای جام‌جهانی
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/95592" target="_blank">📅 09:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69b286c983.mp4?token=L9MxHHMSDHcIOV5BPLAaiS_S7cbn-UFIGz4Etott7cP85yxCHgfPWkxJWcLROD6aFNHsvN6rWvoC-KOJJhhWshnRTKGoehM2HQqzzSJBPRVQNmG3Asd0A7VPYI0BdUIbbYjsEoHVlRVrODsXQqn_QctkNoDAXZbf3ZUGDh9DRlPqX3xcmKFJzlwmoza1mvWgLzhXtSHYGQvVNh-qEkDTI9UOoiwlCKyAqAT-HfZOzOKUmp5AC92BInwXac9l2Wfy5v6NAsvcNAvY-viANx0LazzUHTpWzOwARtmGof17PyOpR5uSpxYE4qeLSboSbF477gs9O4IexhG9JrZzTYWinA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69b286c983.mp4?token=L9MxHHMSDHcIOV5BPLAaiS_S7cbn-UFIGz4Etott7cP85yxCHgfPWkxJWcLROD6aFNHsvN6rWvoC-KOJJhhWshnRTKGoehM2HQqzzSJBPRVQNmG3Asd0A7VPYI0BdUIbbYjsEoHVlRVrODsXQqn_QctkNoDAXZbf3ZUGDh9DRlPqX3xcmKFJzlwmoza1mvWgLzhXtSHYGQvVNh-qEkDTI9UOoiwlCKyAqAT-HfZOzOKUmp5AC92BInwXac9l2Wfy5v6NAsvcNAvY-viANx0LazzUHTpWzOwARtmGof17PyOpR5uSpxYE4qeLSboSbF477gs9O4IexhG9JrZzTYWinA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
دختر ایرونی عاشق مسی رو ببینید و بشنوید که یه ذره بی اعصابم هست
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/95591" target="_blank">📅 09:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkxiANOUy8z1wDctEaKeWnrr6HJ9taEdjHmNvHbM8gx5UgWPrCacKYW-J0q-fsXoyvMiAvPCB1MPp7mN1mW5P6cOP9PKQsV9UHUHSqxSHDj8X78kPD_iMWv5oExAKl7N4dv8v2NrOo0tKxvzNUU9ZZEGAfT-1NzgnSz59hag3gsdgeR_BIYO3INo-XXchTJgFGJAV32C40WmdIy1hBlBZUkr11VYn80YislvB8b8J06LV0QbPCmmq4glrjR7Kw--ySq59j1nuz1-HI158DJ6f4fvXSHj1UmLFmA_PodnZmbm3sYdknKe9QKd3VFK09LbcJ-1KaNOrnY5S7ynGh91Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو
: باشگاه چلسی طی ساعات آینده قرارداد مارک‌بالیسترا ستاره آتالانتا ایتالیا را به ارزش ۵۵ میلیون یورو نهایی خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95590" target="_blank">📅 08:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2zM8qciyUBOn3-DVmg7qvKCbLD2lKq4TcPQDkJbSlZk1H1jEhuXSwcP0u2ZmPOxmnukV-VlzdgASq3HrOG9gDSThHCAu6gzGrsv8oscYTlsXRkwnI9aQuJQ25p5slIbfcmGBazTP3FA_x0wO9T1uhApbIhq2kzJtYT9oJgRw12xvCctSK5QjCfOgesNIZr0QbdFrfKQ-3zc0hOaTVSnEQek7PCYdtB_5XC5Yvhfh3g57_fBSEcw6bNysYhEcznDI-Xr9ai5eY5UMJVuvQ24X-mmkniSk2KdWeCOmmH3ilDnJP3wYduzW3OAqAU8cFCDIswJsHVRCMpSTN9PxHB_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
📊
مروری بر ۱۲ گروه جام‌جهانی تا اینجا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95589" target="_blank">📅 07:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9Qhby6i-fqmmJCp35PTi0Q6TZdl3Et6j1jrJFRsRorLlRR6174vKDY5nmetGzS5edeM-VAWSXaPXNW3Igdz3FbXZkHO1B6sbh9T6OyQhcCnmLkx4-XJuBIWFjhuPAyEkFkH2vldFZnbYDJgr2a7WUyyQMA2U3qlK5ntRb0cHMMAiqTkiVli-MJ_nFzZ1uaXpyfCL2s73dthuihXJCsX00m2zAkfU854jPUBYJAKWg2VX8DerSDRzOKDwCdGoex7gMmRaPxmz43jJqOIHh4xqMuH8367rydrM-YE9GtAQweQkzURRN-2Rj06Pr27ckcMCHWFtglC-R7MAPgAincHEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول حساس و نفس‌گیر بهترین پاسورهای جام‌جهانی تا پایان هفته دوم مرحله‌گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95588" target="_blank">📅 07:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/awHckqrezM44acB4Ao2K9LTPx0-RmYVKePbTj90QifaE2MA53oF7HeY-fITonX67jNxtcEuChq3ct_kczZkgdeNG0k-VWndaEnQe7lA77sGqxmZpOAMAhf4FXF7i9GIDZI7LTBbZEkbdpBbjvRQIke-J8vrKA863vAFqwx9JF_zD3EGslPZbKqTQqFLaKn-BlCScIuR9QVqB1VOrH7Buk7rvmp9R-OLw11EPePy67IktSQ8FT8PB2O5nr7FDfa8v9-CncJFVQluF8SjnIfoBxhtyhsvD-MG-Ng6uzCnMHIJmx8Jo0F_GQvOivC7gHfU0DDfwJ8UgaOfNJQ23TM45dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
جدول داغ و جذاب بهترین گلزنان جام‌جهانی تا پایان هفته دوم مرحله‌گروهی
⚽️
لیونل‌مسی ۵گل
⚽️
ارلینگ هالند ۴گل
⚽️
کیلیان امباپه ۴ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/95587" target="_blank">📅 07:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95586">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gff9RsUv0Bv314kl5sLBDtRkuOGqJvNQQPvgkpCz4w8spO8o2M_JWriyBi4mZzkMEmN4u44r8Ad-2zsihUnUAjp4B_7d-9dLZNfeHqtPa5exjpclF67xIbCeyDWWhOloou66rAeikxRNjGbQanX0DsPhA3QF5mkS88kVAqy0Z_b6stZ8xgZMnyTS_Ng6xMED4SXdVE8Tyi0pn3XkixV3R22x-KN5N7J4bJfWRBXPKjwCzK9iH7gglT95vJFvQHTCe_iAnGLn0SdWbPG2SwZMoCxEfAoxSVzldI4eYeHjFJxnxztEq61kIE3KJlzYSGJby6x2ofQOjZeyI91ZYm_SAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
آپدیت تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95586" target="_blank">📅 07:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95585">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjVaCPNHX9F7Jg1auJsKDcLe2sLJ5rRAo08oYa3NDYIfu1V0M95xi6nWX9a-nWvFNUIsaJWYdz2656WdM8MXYel_yaCn25CkYnwg5amCVxYUzNWX2Ika2GU7WFo5FXNf572ztyXqdtshK_GfABVsanxSsKxT6YyjQlXN1hWtwlZI-WFXgewjWGJHgG-l2foEjwng8qXn-cFEZDHIUv8Ia6s_NILzzCKXM90aY4GTBfuUDvSQqiKOjvgS80W1Gt3fWoK1ytt_FbQSQOpApPcHkUTXXrrA6C43IfMPFHZHYSNGsWJk7j3hA1XZxFD5R_61tkMDz6PTUWWriF8TFzUDFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول رده‌بندی بهترین تیم‌های سوم جام‌جهانی پس از پایان هفته‌دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95585" target="_blank">📅 07:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95584">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HurPjxeFt5otzgVGu2BpE4AFUKUThEAwlmMO4LaG3dVHwqTe32TflrDN3gFnZVlkXrDTxyu2k60mZyqNzFfXQ9SNIJDmEQP5VVApI_KBMbVS1J8B93_A485f2frRU7uYdYRB5WB11PSU7S1lFSuOMOfJZL5rYtF69xXy5lBwbAZkLK_vuoRwFB1UTRWiow4CNQi2DtxIXnDt3vA4b2COWOEEWKvwMyP0T5JbeME7D2wJR73gUyZoEqk_ukkY5QqjnOlPAijHCiDgO6PyKniV1Fr4VOkTBofsktyYgJvDbyGSAcJAOZm1ohpHrJrLoFboNaOPseIUjUbOXIkuyAUILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
کلمبیا راهی مرحله حذفی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95584" target="_blank">📅 07:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95583">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYIQzRdX6poFRQZotemOInZXKOuOZUgRcy6X9K9HJ9KXcSB3QY0PvBmMW6DHfKezj6Cl4UkGRqdqJ1c2OtH8GLfbUwsPlxrTH0r9uma1VFL6BCDw1EIgqWzqw0jZMytbaNM44LvFazR61aiAG2jXPNVJUqS-RhN7FKK2889U_QBeo3veemJSnmsPzKAnS6fJveGLCzkTLs8Ay-oQ9bJ1z40XAGBO4GmypTU0HemvQLmknCuwc0COSH3qZb-BCHJvv5hbDLzxsf5QSdE5V579_gPexfZnaLih7-3sKcQbNM9frxaunfsKjQSL-w9Wf94gOa95nZMI0Sv_mivxc5FvZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
کلمبیا راهی مرحله حذفی جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95583" target="_blank">📅 07:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9fd0b47af9.mp4?token=E2Y0GzXJJ9OGtZf9ADzc8fpZlvTBR7R3Jlq5L1ie3Zzz1wFxGS3h1R5irxlKrsrVyM8P03XRu4ayTYBZKJRt2rPqy2yGIG9ZpqKL_FKHbotMxje2cJLhkl7V4ov-NiAUmwlQ-5CvKVlpkkwZoDdiceG56G7GptclJg9ZggoURRGNnAPzMcDqfKjnMEVpOgh64ktFJQkDXJSdbRcjD68-uVRa3FEZFzC7ULxUOT5EMxlxAebV457AgkGvKsTXoCadKS9ZJA5YgwSXFLrBokg3s17aUUiIFpzMaq7TXmzvGY8R2R9BB-I7Cp1w3h3Lq_NBBmjMcxi3eBNtA-Ze6LZKkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9fd0b47af9.mp4?token=E2Y0GzXJJ9OGtZf9ADzc8fpZlvTBR7R3Jlq5L1ie3Zzz1wFxGS3h1R5irxlKrsrVyM8P03XRu4ayTYBZKJRt2rPqy2yGIG9ZpqKL_FKHbotMxje2cJLhkl7V4ov-NiAUmwlQ-5CvKVlpkkwZoDdiceG56G7GptclJg9ZggoURRGNnAPzMcDqfKjnMEVpOgh64ktFJQkDXJSdbRcjD68-uVRa3FEZFzC7ULxUOT5EMxlxAebV457AgkGvKsTXoCadKS9ZJA5YgwSXFLrBokg3s17aUUiIFpzMaq7TXmzvGY8R2R9BB-I7Cp1w3h3Lq_NBBmjMcxi3eBNtA-Ze6LZKkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇴
گل‌اول کلمبیا به کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95582" target="_blank">📅 07:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G9cxkQn6brJOqI4oZ2tcJzEhCDmUkOx7ZOicJLXTZSpra4-0IGJXQiWIkssncs5dzxUN5cbONzltgjZ3WrH3H4nybnQWRZABIsWQ_gEmBFsPBGBwSFl7-v-RDNOr9AlG2Lvi9laxY8Y1XMQCXzO1BXkk3Rb9hUX6kjZS8DjleY1rqdN5tOxrZOGM64bf37Y219kTbVTQyZ1HXRL7rxH9Y8xI5Gn5yyHqutq3UnKbCQH4MDhPSQLUFDQOIoxZ28M46g_iRJGWb-3BsI223dn1y2PS3qz2HTEk_QHkZ03gekS8OxKNGllikE3FQ6goXib0eMo2Ok4HYFEZlofhpSYokg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lm_SIMI9OB-SGcZH8LZbaaP_DR1p45dbj7iDHRg--p_Yie-5GiIYPoirFD8lnwlCzDMw3CITk7Nfl_f4MEyYLImQuw5QmlfdzmvsSCgDZGCbowlky8SsJqxO04X_a5QKlnKUP66c3eo7BdAE0DT4CdHP2YIpq4h98QeGQOaFF0TPCKy6S2xwF_WrMtS8QyIhalYRa-KofYpmgo5eRNK89D4rxvpR84KvjsYWsQfE7jk4ccF2YTv799Hp-U9Mm1wCSuWJ83NsO4Vkbm7NC9ZPM_QnYtYlZFxKuz_KomKddScywlMxI1QZOCVoEKgpIdK-COlPLunZXuTJmw9lComNjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ti35eh1kOO6HwnGrRYKJGxWixlw5dDpaG6uJLCjhb_tDcagHHhiTDNBSkEO_k0me_pcAH-Rqp0tDIGNHrxE55c7Gw8x2PCnVjYmuzt7_eTYDME7y3HiwiIs3VuJaYbiY6K9rXn29suCwD2mZCsnc-EVZXoHB9nVTtK59qQFR7kPqmc7eCDLF-K3ctB8uYE6AjMRTVDMHu_TOo4IPVSRxUsZHLVp6eBzSSMXlQEW6VEPpB5iGKYIs2_2KylThndECre9V5a02xT8MQ4xOTQa9tS4_MKmDlI12BAb07p0k6mKVFE0tSMllDIpH2xW9Xl39IXHdJhOdaUKkb9KBOt40eA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ما که خیلی وقته بخاطر خامس طرفدار کلمبیا هستیم
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95579" target="_blank">📅 05:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رد شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95578" target="_blank">📅 05:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95577">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گللللللل کلمبیا زد.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95577" target="_blank">📅 05:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95574">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JW_G9q49vRylDZ_BtkLaredlJYjQCGSr_3cdVmUXO8P3XsXkg6fJuitgaZMaKk1OTJKQha4NdRwOrPgpiDw6OBF4ikr5AaDQzBTxGLz6dw5py_6pk0CIOZwbwWeYjCDAdRtS4jqRkiATeByXDJOeh9G3ULeGODmpRcQal6MEbNxAbN-MrX2lFfd9szB75pd4rfkgBIEL9exxTaevStNxzUb3_HlcAvy9e35I2cWkRfIfCLl-ONQEGP-1urIvG4gjTYw109JNe_StELdRrwDhA8kEYg1DYJ-bbKNdyu0sZIw66V__gNk65ZoVyvcOZXhRc6e_Kh9qNFPgpbRvrz9LWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ftFjQRRkm5M23i0PqHBu9bOrhZiK1B_WKe6w-7pJ8MSrjs4XSrg_zAblrYULla7qPiwkwv64zrQpNz9VBVIsUD5N8YOMImy0yvEFOqk1cm0YGf9HLVH-TQcJtNfcfui92oDtEq6kO_wQMxTV-fQDro3BmjcPOErHGghkdVpoTXgAGJPTX1ezlTKgqtdajuVPSUD-7FZxC9bGqKq6OEVI7gL8H_Ue5HZWMYS3Kdo2ddPaNJwq7RFAP7JWMzmjbt_OlXpwxGHPmB-eyJhNvV8id7H7sQhl3YlXej7At9PIIkKuTHfSzVXFo_oBdPNy5WnCodJsthulHTWXNwOQ8JRGKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXS7zhL4Zy_V5zlDQqZ2LsQ-tPcFjMufUHDujY2T9fY8_3-bHUoorNd5-7L9K-iHlLg6WdA18Hgg4cKBWPj79Omue6gvYRNXcI6Yb4fH3349n6_H6hsNseJkqcZn1d2fsSQlizFWGdmPe-Xg3E_W3znScdfuWiOvj0IFrR4VR4Wz2TQ-zImzbig8LQYdIl4VegDtI1-ckDT2vp07WAd0UaquwsIfF8Ewrok3SZMMH8Fu66Y8zmDKAAJEmrG9l_EsHjwK6UyHYBPJkuf3es8jMEiBaRRjWB2SHJg-g5hMmzOFK4HxNlrMu4WzxusE04BY_9-VT6xHZVbRvZkulEimsg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
🔥
جشن بازیکنای کرواسی به مناسبت رسیدن شراب ناب به 200 بازی ملی:
⚽️
200 بازی
⚽️
29 گل
🔥
31 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/95574" target="_blank">📅 05:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95573">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بریم سراغ بازی کلمبیا - کنگو
تنها نکته مثبت این بازی حضور فیکس خامسه.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95573" target="_blank">📅 05:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95572">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwiUMABL3wvqKlsjgSWR5UDESFpRHC0WL7wSMGtG-x37knZAU9oTbFTvf4ILuKpbzHSJVxFXw_Ss7EiI_x9vyMhKlf0_vxDTzKWx6SOgHHIV5_RGCn9TPbZiQXjrQRQBTan1ihTmmCg43eGK74vOa5pKd7DYKfYrvbyCxwDJRO0iQuxEtDGDAAqCt8ASRLrOTjEODks41QCjFGubONbq4J2V-zSImX-AHPSikD7Ew2D2vkZy1CdbT84EWZyBwH4UHZaUd2_VwNvTc3ZL1WAHxafnhacEkQFtopiIUu_zyQjhYe130D7HueBzabucd-A7Pgn5k0iFsXOWk_C3UBl8nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکراری ترین عکس این چند روز چنلای ورزشی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/95572" target="_blank">📅 05:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95568">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lhkr6zUa1UDhxcDRb0oabXVohRaLH3CeM-VTZL9A8mlimmrBnCg3tneLhed8HF4crC_0-TtMLF1rFvhww8DYei476TUtXL6tJAy-YV8D-tCzXM4LKSvcUYZQdtxyY8LcBOPI2E103fHABpErwlEZp17wy8YSuJxtNFEDW6T8CcTsKZd8fK0ojz8c2YS5G8tPbM7iTD4_EG-86JI039HAPc7QTS1p83W2PqDWvrxyUtNthl9OYF_l61BjOu_J7UueUi_A-1U244a6xgUitfOowuhRl9TYlqwlI-J0xL9XeH0HcYPCLiwyuKoJuyIfa14dQwlPkcQkH1LlAJjLsuQbiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7ucni8yvS1gZq8JCwaUxZgscLbjxpbx-ibSRp-cOQA-1UdjoA-sIeIzSj7qRYq1Aa01J3JEwVGA5sSdyAfz_MY48SdJJZx4uU2xzyPSjqrh3AE5nLMWj7dun3Oi8kV--UiJ2wgZeNFc4YqS75NiZUcuYzc8PqnvN5UzqnYvfKG6jN1WqV0UMQtierF3lW_bD_EOcFcnbLs5cu2RDnJS9_VMv-gJuU7Jx08w-dVwB_uKnaaqnHeQOVOzAIUvJzPFQbRlVNihlw6K-5WjoOBqyUNHj4NFPjHaRiNNE_LEBzt1j3QT8GGqcTpJO4jQK65-BNXYFTXCpCoisQaWke3xSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uUJFdF9xozdKkHhdXl-Ogpc0SctzifMBKD2s1catTOafgDWusaXoWwoAGlyS4YgJ9l8XygCYrqoUYTcFlPho3amQNoun3Cl9mTcATIQUfRGwHDSlbbhuRXYXB95pRVJWGXsl04fFvfNjvsvgrbrLlbasI-V3WVRS27mXLfL__NRX4jrpKEoXDSy3jF5JenShfg9RdXY16CoqtspSChzwmN36JzSAhSJ2KMn_LQVvykZLaDr0cV5zpgoC9lHon20LiGLNFKoNoVA9hjmCyvCS8bhldoN8P660t2a_Gw9QLhEYLfAcRRfdz6cl_E_ZuRcm78M8WHb9X2eDiY2EowjRCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YW9BT4RM1GnhH_9RQc6WQKf9tihzwNBaY_2-Ad3sBOCmJlVTfdFVk411DzEBmnXqV4fj0c1Wv72PieecJbSJjp4u-5RTwlXHaAbGXfWwXqg3UixoNMWZTBRkJyF5r8OGuP7fySzVm6uwWO61hVWaGK5S8-DDfnc9D1FKw4LnI8Bab5JBlCSuxZHS7XNfzWRWJmvZFSMyraLTCnUBuOQMSytM3gVQJQUVWJHR4eKnxEB2Y0xI9ANkz44I7TUHR916lKIHkosX4y8mmpYz9J6QPTSaxwJGghwiLVeoUJ5sRH5lQxFEk6b2bIxa_4-1tWcJJSeTUZ1JSzWsTdxttU1ulQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این عکسا چند سال دیگه می‌ره تو دل تاریخ
🍷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95568" target="_blank">📅 05:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95567">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSrkLU5RoUexsfXpYh2I3N-7pra1MR6b1gzvppmHU4NtxRacR4Dspi8lQV_cMXmfX9ijQWtziBF6hKh_ImYsqeb8jUNPx5Mvn-coz_xWNVAeHx73fuyoV5RWw7ceJb8fhVsG3GUT9raJ3f71_8VyEe3EvA0XACnxxusOxOywgC2dCE3mXviS7LKPWW1nmi7LTcpFVbLJjANdQRlzOH6wUXk3bhbkC8q6fTbYxMI24sIMVRYtkwPQmP2FwcAK7XMv1EH0u9wkEWo0qV-7XH6KmyTmVv9et6XD-kne-Xomw54Xbf1Pvg9BNlhyus544ae2L8_T-PeOkfRH27fLT6V4oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
فورییییی از کارلو آنچلوتی:
نیمار کاملا بهبود یافته و آمادست تا 90 دقیقه برای برزیل بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95567" target="_blank">📅 05:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95565">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oc8VAirnxonebGeAF384QhTNByCSfGpoa3org_bwP2DOqKylvv2KTnIAUNjZ1jZQgBwZvMnwdQzXUMQkcgP7A7EU5LxzGQmZlqfDewecoIRT8SzdxRak7eRsjv4LZhpZKPY5bdF2BgW0x4mON__RE14I3BaoetB94FHYL-M1nx8NA378aqaIhdFqplc2o3WvH8JsVvUuELnj4OFdG-PpvbFWvtvIdMqJlXe1bfLVdguQA5vl3ynzzmSH4bG5KuRH0Toagql8XUN6p2Y9ChSPF_EWBDwIhXhchDKhXzZ9Mq1CpJ8S-vXJoz9VzmqsYg9MsfBfFHglljuGh-sbxxDDNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZPZ70V4bmfFn9q2F6YTPbRSZicz_zmBRSB4jWm106qjLzRb2zS9ycwsoCQu5QMhbkChVlBwCk52UjIbcQrLmwBIbPS5i9jGq9Kbrf4kscLd5sEjJaNaiLCzmC1TTR98lg9v_N6Q1-ZV3cYGmD_O26zOHY4XWp7gi6XwPbvoW7YF9xdjrX5MUIqgeCK_3g7am1wvPkOmlHoiD_cTYBy5oNhwMJ3uVe2fXfJ0_jfGSqjtx9H3uIiLtlZnnXsoF_ISq4iIHBg6A1lx-jAb40-DO8gxRcDZmXMFOORTo4XE8cf3cSE6oBWSkyujnI9kcmfS6aUJNrrbUrSUR1qs4S8NoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇴
🇨🇩
ترکیب کلمبیا و کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95565" target="_blank">📅 05:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95564">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0lQsHMwzvlwK0VvWm7MYK5dZCJMxr_HPVljAYYV76vX6ZWxZKjy9VX58crgWAYkwTeLEVFtZGi4e-SFxh_zK_4UA8Ltab6UftYL5OpMd_-bLZOg0lhx2-A6BANflWgdnYYuv0Xf7k0gAkoBy57403Mv2d-Sjr0_ohwzanz8lvOqj9eeb1iVLGBxbD9E7poqBirahPZHy93p0X31yzCROm9eaPJlhtp0fNWENIHBo4H83cr_7o145O5GtRY_-BtPCRwKHZzXX0qtGbtZwYG0OMO7vAfwc90cjPOlqjZZrHq9Xz42qm7Tlce_gdAvh_Jl5PdLC__1O7uCS8gxIj-YPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
فقط ۴ تیم تاکنون در جام جهانی ۲۰۲۶ هیچ گلی دریافت نکرده‌اند:
🇬🇭
غنا - 0
🇦🇷
آرژانتین - 0
🇪🇸
اسپانیا - 0
🇲🇽
مکزیک - 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95564" target="_blank">📅 04:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95563">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WBMlP6gj-LlAtbPQexaToJeuaRhsLN_ZHY7R7UjulW7HHEAXnYK90r8SEaOvbO53X71_KUxs_1Ta41IFLMYnIc_kjSgGl7FeH4JW0mbokpWk5qQ03-4i0264cBs5R2AVbUV3j9NysQd4Mqz8PDT7HK-Eg-B2vL3kKfpYH60J0wDDJOUr4JbH7Qfu-eVceGoec2B3UOUw1gb22UJOoe1KDl6LwDUAfkgwMJ_y0K29krpCTmtPSwM1X_4QtLngyC2Jrb_1hm3V5fRVb1v3AacTEM4JyDVdjCkK9oXYF2PV0KC-sKB2ktSOzDhXTFB1olYEmn8p7hGV5YwE18XT_oY_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
❌
🏆
تیم‌های حذف شده از جام جهانی ۲۰۲۶ تاکنون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95563" target="_blank">📅 04:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95562">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGh8RBCWkpYOGgeaJmJpe5AHfcrFcJzdgLr1hne38jADVluRNrwupOUlSSn_AR36guZ5EDXdm3dTJvH5P_pA33AAYA0WOHDDe2sToWlJKbiVFGyOmtDMcEUumWoMdyF2Urr-hMqKhkZbegngqNLOQ9NoHdwlF2nXCTP52Hu5D_jiM_Kp8N4lFv0yWr9n_iqxRhUCwUcs1W866Vi6cW-xsB1EM1P9soy_5Mock61TmSfAWyjSTBGK9yMWdAfeTnrdFEHr6uHQicvxPY1qfXL3QFz6kZaC52zhgPRd4e0dyAn3rzF6XP41wdGMV4ctMk4lWFmQdYF49QgBy5pLZYqagA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه L جام‌جهانی با صدرنشینی انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95562" target="_blank">📅 04:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95561">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3QMhQmmwCkFumSf-9v1GztrFYlUtf3xO7GnnFAvlAtIC4kK_sz1s6d1ogvqt_eBN1uwJ9JD5vbU8I4SGvNV8Vwxy_1A5eOueNCY9-hZt7LbaSZYuOZXdZm47x9FZfvpiyCK93pmhyC4OXe612CIXwVbGS_4tJ0W4QUZeHtRKdZjVUPKov5CfwywwPU4pAefJvBOubrqP0wy0Pr7EUHr9l5Mn4WaY01IzCaTif_8OW0wXw7dwf7GprMXRI6LJudi0NlJfo75Nal972tUiy2Dk2zqg4il37g5Z6OxH591K1IK_XrYVzJID5_WKOpZ7ZlNSJSo4fubfj36clRCbAiPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | بای بای پاناما؛ زنده ماندن امید کروات‌ها به لطف تک گل بودیمیر
🇭🇷
کرواسی 1 -
🇵🇦
پاناما 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95561" target="_blank">📅 04:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54adb67650.mp4?token=deSpODA_FsOGAq_yniyk7slT7sk_sdeAtjQIuWvpY2LT6VCSVkJdpg8mjcHXw6LnBMvmAgev6qb8lULARXLzNjh2EyM7QNJ-8sok9IWfAmj1JcUtrRMQJfzG4iMofgH6xEZ5ivEguG90_Hz3bfQpM_r4usQ99GrRaL4nrLYn1beCUM-gH5vimX_IDHX3-e7oBt9I-5IYurOOqBUIgevsJ4MwsxXVYITuDt-xLvYeiykuAs4UyzO753g4jSogQXYyHhyJ2x1DJVAj3yAby8ON9tVoV2CXh7hlx1VRH5sNKoF-TD57_Mqgrp3Sky-dkvFZ401y42xo-pyYL1ipdXrajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54adb67650.mp4?token=deSpODA_FsOGAq_yniyk7slT7sk_sdeAtjQIuWvpY2LT6VCSVkJdpg8mjcHXw6LnBMvmAgev6qb8lULARXLzNjh2EyM7QNJ-8sok9IWfAmj1JcUtrRMQJfzG4iMofgH6xEZ5ivEguG90_Hz3bfQpM_r4usQ99GrRaL4nrLYn1beCUM-gH5vimX_IDHX3-e7oBt9I-5IYurOOqBUIgevsJ4MwsxXVYITuDt-xLvYeiykuAs4UyzO753g4jSogQXYyHhyJ2x1DJVAj3yAby8ON9tVoV2CXh7hlx1VRH5sNKoF-TD57_Mqgrp3Sky-dkvFZ401y42xo-pyYL1ipdXrajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بودیمیر به این شکل کون کرواسیو نجات داد و تک گل کرواسی به پاناما رو زد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95560" target="_blank">📅 04:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhepNtYebE6IZnIFTgzihO3sJjvFnYF-6HMXGgLzU5LXPHPglut6wKmrNvjA_BfAF3-pjRHSLm9rmxwrxXyh19SGsS34hyH4ZEeXomwFMIQhZWOogvIlVje71fUj3LozGSEGpluT3Kvrt_XgXfW-xbXlqotvOGUO0nP9VAoArrKQW64S_YvBbHcGX4amJKiBZw5i4zWIjl5apshODvYTXH12zPBM855OPOWs0ZCPs0fT_rNao3rSbm4-FN7PcxwxX14UveFURMCJyB4YwzADiav_HQJ6gayiJ9-5D52BKxFklaPkPCFIUCVfz6bksUXnd_W4xapM8huwU2gElF0Kwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رومانو:
جولیان آلوارز احساس میکند اتلتیکو مادرید به او خیانت کرده است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/95559" target="_blank">📅 02:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95558">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfXzNbABGiB2-GT1LMDNoQyyy3Rd-uWaZHcRuRd0-5wgE8_ODsNzkJPhdA_mwOe2_xJQ2COWJsh5jg0SlG3GNR_EMtSSuVGHTA7PrR2PY543Iila7utyFew1S1iNwR_XhQLjd-IY9uW5M3zE1YyCT-rMSgu16W1xGmfSFGhMPMoUulh_oPhT_0GGLUPR3iYLclOyL1SQHej-4K7x0sWF5WvXqU4TWFGPQcimPM7-T20qjwhpJxoEXQqgpHvo4-xIxZ6yRIe4_QveEZCF2T7jIQ2v7xe0VUfXd13vDUyaqkr2xmHjLJa4aZ7mzKeRt33pXBtBGUJCfJ_7N-GFAS-Ing.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
برونو فرناندز:
کریستیانو برای گل ها زندگی می کند و ما به او نیاز داریم که بیشتر گل بزند. او همیشه یک گلزن استثنایی بوده و همیشه تشنه گلزنی بوده است.
ما به مهاجمان خود خدمت می کنیم، نه فقط کریستیانو، اگرچه او سلاح اصلی ماست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/95558" target="_blank">📅 02:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95555">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iS1tozatBOqjEauLU05WnFQ6mh5AnOrNNJO7nVD_4T7Z6d6qa1lfy_PNJqAEhA9MP-qhIqvWmQ2_Im-EewtEBPMgyMsjMLsOKGCCoFpPgYHamWyzOBHi8wiWBvxySbteou0TcQ1k1hDf54KyBAs7BQ4zilEkQkXFb537-cntZ-S0ZDD9z-AA3kVV_3T26Hkz8NHfXQrLFFkEbLbvjLqH-CGl7_84GIKkz00gfew3pILR49HQiMFVJCW-TSygoustgwAk3ZinkqZIhZP4hozmv_KETucukhV6ASC8XFUd5OthzxDVWG5ZAfE1zVahg6rRwz509iI--VZh-mO53t1S4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qBRsWDxQJ1wzbgJUpk0GhKTfl_jwroSYV3tFZhBstFICwverMb7duRaoEZM0d52TIE_fJ8U6gd-3shjEAzZz9E-Bo3CYQ0nFpCGFIDgHPwjuikqaxkaNs-a9JorGXzY-JtSr-aM9FOA3yXXuymXRgP308eMuBmdo4RJgrbJFMRBQlEAVssCq08R0QwzyKlQ2DUsgpSwO0sWqWwJ4Pk_q5lgCRSQkrxy-mZLC1ttC1m1zdTLJNI9Utc0lsCxHTzFWmeVBs3vbcAxMwTDzsaiPxiBVkhg5JpQVPGU4DATvYxAbqlKYt2quZ-Lek3k5sTvoz0Dz0TcU1HmzK384zVGyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0fg8HN2rOuVhjVpsKQCoOLX1ClQBYAjUGduelUBV56hCkj9P5XYaPRpCFsOHGUGTsbisxJJEDsgjusCUZ_pYe3JrqTOOXuWSx0wcn5H9l9RnUSgxSws8uioc4SfvRSjfl1rmycc_SSW9L7uGOaTexv3nhZz-Cb_VHPLOx0aqcqYlMNdepKqGsRvz6PBbYyFJ4qOsU4zJZsnpUas-NAouEzWrzSEbvWxeYe97lj3OCiYknSwR42URd-lcZ6y21UL0qrATXoj9ex9kOPvqbG1irInHszHQYOYn1hojCiZs5XflZ2peY_fSFbRo5CtZgXHm1XEFa4M4DaeFTyyzfog_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو ایوانا برای حمایت از کرواسی تو ورزشگاه حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/95555" target="_blank">📅 02:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95554">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dfd384cab.mp4?token=JIh_arL34ddHtQYvkiBi0r3wCTH1yaIEI1bs3RKcj287fCzfGSWVij7HUr5PfZ_p1GPneYtoKnZoKe0wiq5zVEA6XVSFlThAJr7Zzhi0kurvoh5M1pZjx7uh0cA3FC_HfBl2E-FZvtbWo84OeKZjFhK7PBC7BlDKLDmLSZfEF1LjI7mexYkh6C-lMnMJWOGoryJKWoi70H8Uh1llCCyU-0ZviaQTsiODmLWv8lW8N3bySVcy6sR8r2H65bjBRbXH2OmO3Q_a2HCmlVmBUUjqnfZgICaNx1NISMi_mtAZwAyhKdJI-hs7M-vsti0adDivxxvDeNPOhOUmnZHhn4-05g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dfd384cab.mp4?token=JIh_arL34ddHtQYvkiBi0r3wCTH1yaIEI1bs3RKcj287fCzfGSWVij7HUr5PfZ_p1GPneYtoKnZoKe0wiq5zVEA6XVSFlThAJr7Zzhi0kurvoh5M1pZjx7uh0cA3FC_HfBl2E-FZvtbWo84OeKZjFhK7PBC7BlDKLDmLSZfEF1LjI7mexYkh6C-lMnMJWOGoryJKWoi70H8Uh1llCCyU-0ZviaQTsiODmLWv8lW8N3bySVcy6sR8r2H65bjBRbXH2OmO3Q_a2HCmlVmBUUjqnfZgICaNx1NISMi_mtAZwAyhKdJI-hs7M-vsti0adDivxxvDeNPOhOUmnZHhn4-05g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انگلیس در مقابل غنا 78.8% مالکیت توپ رو ثبت کرد
این بالاترین میزان مالکیت توپ ثبت شده (از سال 1966) توسط تیمی در یک مسابقه جام جهانی بدون زدن گل است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/95554" target="_blank">📅 01:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95553">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvJ6XGJtS9v7k8LjH0TSrYLwokXACJV1jugKemK6_BDGs7gtS3VQRLUW1z8gRWLnEg221uVp0bB3X91CxuO5poXFUBgwV0O4PWoej0y1Q75PoGfwHRcT68XiuAKxg9Pa4utsONBUSU3U0LxS8PWK1-wZcVVurLucLRwRg8zUPbJFNUTeSxziAUZBIi-aeSGPuoaJnQ8F88YDQ0MXtqiHMtaeLjT22e_qqUj3QXkNrd0t1xDkwwipj0NZ0YQIV4-_XP0bmh1e3LV2nz4r2RTzJ8mt3HrF-tK8eOhx6ChlozFzcN4tsdtR9qbzuaPUV_oiygmv2HuBnm2NwZHBSpPX6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی 39 ساله شد
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95553" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95552">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95552" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95551">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ThO-OcJTIOZgB8QF-ROC_E9PP3XNlSy9vqHNltewvmDNDeBo1GVSi_o8OE7hcjU3ePHvca4vcW8uSE2-YqvcawwKIZK6NbPITnGw408RnCrxAgyQsa2HCTVyutdipd6ULhphGGV0__swpGeMKYluNMog2UewuZE-Htrt7GT68h_ykxwSm573mhx2ZvkkgSH0XYoXSzb5Q9amBWLzwBJ3i8SO6NN46F2UMTCrwJdRcDvlWSYBcMwlqCSe_4Hu_L8P9MowYJVsYjbq_XTEGslSowAqJvN0BP90IzfMUgI_CxYU11_ge593WoejM41GInTCb7pfloQpJvTKDlA9gRXZ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/95551" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95550">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDXliIhSwEdAhquV43PgZbpNmgEs8z-Kglp_Bp6PQdkJW_BSKcRxrtyD1ffNgDNVaNfq_5I1WQ8ryBvguS506SM_tAxytIle9J-kferu0B1-e_TymKFxFm2yySoOnvScLFVikVhgfSklqQSUjabyvUQ-TNB_T715HL_XdtUggbh5ytoH2tLwCIVKNzdWNIhGhmz0sfKmI-vBuJzekwkI6IX2zoCrL2CQMvGgVt2ChDu2_Zju_F4OVM72gfixYaYAytj6Kiv7vQ3zI5FTl4ei3LJcHaEzM0up_KadYsfmWw4HQBW04uIf55CRLEq37loZZtG2oX93khZcP36D2SzTKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جود بلینگهام بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95550" target="_blank">📅 01:36 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95549">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKx0MzCAZYdD-UmRgQvKa8sl770pcpaCwXMX6mEKSisLIEqki05j8WmUW-dQxnBD747Xsu0GWNFMXxF9wuSoprfbqR5w9ybKjsCFkBYOPG64KNi32ESLzoivLnq0tEcRos0g8aqlw_CzW79Ctr8pW6-NH-ktEVWj4B0Pj5l6eeR4vWkDnqa4ktF6GP426ueBEFhKQHT3rhNNKdpBb-dvHzPQMu54t3zlnvzazXLPnODxF8UvEkc1TP89hj7b6xlINrr3XVGKKmax8r9pXrs9qSYImphWx2Ci_wDI0Hw2YvDvuRlRjJB8I4L4VTE4mKUpwS--gXf7PoozP2m_9O4q8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | شاگردان کی‌روش با اتوبوس از حریف قدرتمند خود امتیاز گرفتند
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس 0 -
🇬🇭
غنا 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/95549" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95548">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkdCDLZ49c-oetok_0TNWpApzbiQl6FfYl9P_nSgvuXAZ6q8m-3GTZBuvmnXPoyikjsx4LYDWUKUWug2aoRQybYHiPTaAyoWtx5Iec32wbhd1lSshH_wunJb9g5MxZXFDD_5L9pt5ijNEMvCHxXYfik41ettzmaFGADpiN25Kzt0IWyNumPgOL1a0d_rsRHfTIbmhWBhxfQ4jc92F0iAc7unDcCGrgJVWWJxoEUTy5zU2xCP4_RQVQY4MIgOGWvxEkDx8wPKJ9WqaIoiC7itcxAq7aRPUFnNyRCI4xy_vF9kbt7rGMubLQizuypSGZBw6YlbVtV9dRb9CI-sRt2Kmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موقعیتی که کین نزد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/95548" target="_blank">📅 01:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95547">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">چجوری این توپارو انگلیس گل نکرد</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/Futball180TV/95547" target="_blank">📅 01:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95546">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پشمام غنا چی رو گل نکرد</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/95546" target="_blank">📅 01:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95545">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U50Bz9qHDePsAwEKpXBJEsWgXyFADwmfP7X9WmOznvZWbRlDTRTM_x2VM3Qv5l9InkQvOUEPKsOCiQOjUijjVnCotAEFLtJnvLb4PbxikhHqtDj6VNhcpW3C86vZvPXeRz6I8lbIg1hEzy5OF8Kg0PWsSwUAVSqnRx7nnu3PvDzUpmbcV7oKJp6tNpDe2kI9nKPTfCIssXMukoO71GtaQo8jGTUX2tV9L6NG-WIT2ZpoEni-2aB7oo3XYmmXwACfKDsBljNNg_9NqVdUFMbtT1mjHX-6APsERCsBy89OCXktxSiFfeUoN5gF0lU60Nj6svyxWnFLUXOyD_3hT2yHVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇦
🇭🇷
ترکیب پاناما و کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/95545" target="_blank">📅 01:07 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
