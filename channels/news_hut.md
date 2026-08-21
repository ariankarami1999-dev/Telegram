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
<img src="https://cdn4.telesco.pe/file/tDRykh1dHYFI9vmyAJfvFlfhv8CGXU5Nmo6RI4qy-WGSLWDTP2iLyVAwvESUPkAdynfVyojVtzE-nn-_ZYXCk59lHbBmq7C_2quJyCr7hEhc0ks9ZCqEFMLdb9fV2BeV9rhBXWhzA0h4NYywTi4dmLAzCLOEtELFzGivrjubcnczmCO4D-E5Ttw0WAXRTJSZrNdnFbkeF1hbCZnTX08VLnMIGm7BCTVEXRhDr1bDOScnjiUqVY_8bjIqtqYkgO7Fsidu3lbS7TsVA85VrP_3M8-ApdAk81iyPfSdU3lUzkOUCA2x3QQ6wFCREan1wcMtfjOnvEtn-c9WyCfygFR_2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 119K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 07:38:34</div>
<hr>

<div class="tg-post" id="msg-70346">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">📊
تحلیل فوتبال فقط حدس نیست؛ آمار، ترکیب، انگیزه و فرم تیم‌ها مهمه.  در کانال ما بازی‌های مهم ملی، لیگ‌ها و دوستانه‌ها رو با بررسی دقیق منتشر می‌کنیم.
🎯
انتخاب‌های پیشنهادی روی گل، BTTS و بازارهای مطمئن‌تر  عضو شو و قبل از شروع بازی‌ها، تحلیل رو ببین.
⚠️
…</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/70346" target="_blank">📅 00:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70345">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=tBNzbqloNAPuDrAubMYnpI95tB9qJycIwSuT-QNSMTYKQk59zaTKbayXQMKShYtc5l6MN2ppJJw4XOCuDVDIZciQz9pbzKJcE060AW_HPyi59VYDcl13CKsRNWony7qd19Q_QRe-LDT2kNjcuzU3ad-2r26drDv3zZ3xZIz55-RTcV856HfRRwSgs4COYYNkRMdymeChAWmzNWmJ_5yPgfA_QQ-jW0cv2e0zGUHcJOOSJDeodv-s3CnvnGywJ9O4-696hckkmBFE-e7xUc_hAezjEuQbS4J4OjDRsN8WtUi1BpaXbdOkAKfCAKS2LcplwthVgu6szjbD_mWhFMPOxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=tBNzbqloNAPuDrAubMYnpI95tB9qJycIwSuT-QNSMTYKQk59zaTKbayXQMKShYtc5l6MN2ppJJw4XOCuDVDIZciQz9pbzKJcE060AW_HPyi59VYDcl13CKsRNWony7qd19Q_QRe-LDT2kNjcuzU3ad-2r26drDv3zZ3xZIz55-RTcV856HfRRwSgs4COYYNkRMdymeChAWmzNWmJ_5yPgfA_QQ-jW0cv2e0zGUHcJOOSJDeodv-s3CnvnGywJ9O4-696hckkmBFE-e7xUc_hAezjEuQbS4J4OjDRsN8WtUi1BpaXbdOkAKfCAKS2LcplwthVgu6szjbD_mWhFMPOxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
تحلیل فوتبال فقط حدس نیست؛ آمار، ترکیب، انگیزه و فرم تیم‌ها مهمه.
در کانال ما بازی‌های مهم ملی، لیگ‌ها و دوستانه‌ها رو با بررسی دقیق منتشر می‌کنیم.
🎯
انتخاب‌های پیشنهادی روی گل، BTTS و بازارهای مطمئن‌تر
عضو شو و قبل از شروع بازی‌ها، تحلیل رو ببین.
⚠️
شرط‌بندی باید با مدیریت سرمایه و مسئولیت‌پذیری باشد.
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/news_hut/70345" target="_blank">📅 00:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70344">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=Lo8ENVl6msFMQbjftuqmkQM10VcjKSKAjBBNNltX-bOYf85jgKOOFhUWZIgS06GBEPM8pB6FSEm7YIPAaljBnFz6BlZUqRkZYhFWrWdHrD9zwyMNGPXBUKHLsZPmm_0_iZqFW8ftWQDNvtg0-_XmmStGw1_CZ_APaDIxPmhflkWnyUVE2qIG_Smc4KKNbOW_kLkmnmneQNF8A1XO_SIW3qyNme6hWiw4qap6J0NudxvEuq7PWIeCTWAv7PnqAvAxAaP7W_tGaZm6SfsTnRLT2mkfIgA6uMbvMgGwqZYO_qa_zwgaULtWQyx-E2XHN99TokB9e8HAeSTzz2DWvCZrHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7469eeed2.mp4?token=Lo8ENVl6msFMQbjftuqmkQM10VcjKSKAjBBNNltX-bOYf85jgKOOFhUWZIgS06GBEPM8pB6FSEm7YIPAaljBnFz6BlZUqRkZYhFWrWdHrD9zwyMNGPXBUKHLsZPmm_0_iZqFW8ftWQDNvtg0-_XmmStGw1_CZ_APaDIxPmhflkWnyUVE2qIG_Smc4KKNbOW_kLkmnmneQNF8A1XO_SIW3qyNme6hWiw4qap6J0NudxvEuq7PWIeCTWAv7PnqAvAxAaP7W_tGaZm6SfsTnRLT2mkfIgA6uMbvMgGwqZYO_qa_zwgaULtWQyx-E2XHN99TokB9e8HAeSTzz2DWvCZrHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
آیت‌الله جی‌دی ونس:
تنگه هرمز اصلی ترین اهرم فشار تهران هستش
موثر ترین چیزی که فعلا داریم فشار اقتصادی هستش که به ایران اعمال کردیم
اونا هم به ما فشار اقتصادی وارد میکنن
بهترین راه راه فشار اقتصادی هس نظامی چاره ساز نبود و اونا الان زیر فشارن
ترامپ خیلی واضح گفته ایران نباید سلاح هسته‌ای داشته باشد
تاسیسات هسته‌ای اونا نابود شده ولی آیا دارن بازسازی میکنن؟؟
ما میخوایم یکاری انجام بدیم تاسیسات هسته‌ای اونا نابود بشه حتی شانس بازسازی نداشته باشه
افزایش قیمت نفت گاز تو آمریکا طبیعیه ولی به زودی پایین میاد
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/70344" target="_blank">📅 00:19 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70343">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
لحظاتی پیش صدای دو انفجار در سیریک شنیده شد.
احتمالا موشک شلیک کردن به سمت تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/70343" target="_blank">📅 23:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70342">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM8VkJKxqtzDpk1IMUpa2BVnT31Gia_6NRjUd1s6CvRLbh3UU7wvygxIlFzzixyQZRBQaWf-HXLMBqadyZkX1wvxdyKTZUokrJbKaZpb5G4NW7VN2-VfhMqtfREpJwW-938Ux-JB9xgwXfYSGEP0XSG_rsU4iOUOXkU54a27YZ7o8ORmEZ-FHFzeAaxoyFzh2pDy0fk1BcpzhFGRIMsylubppvxaHpoSZvYYuMuJS0thoefgklLmBHr3i2RY2MbsUdKuWu6OzC9_peMk14hwhOhAjgIzUccBvs-PCMmbtTLjE5uezuSO2-v0nUaIMD71zTOxREuhS6jOr93XBXkoGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
پلتفرم X زیر توییت رئیس پارلمان عراق با عنوانی جعلی برای خلیج فارس، یادآوری کرده که «خلیج فارس »درسته
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70342" target="_blank">📅 22:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70341">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264b3e2171.mp4?token=Uo0uW5eFulWQ4QlWaNERjm5dTPLXuxCxlCZyvNXdjz2XelYYjP59jou-8OFU3YTJyItJr1PW2ESthCsLlWjuKRoz7pkQN08N0wmeuVEaCArC8z6v_XdeDPmnJCXHq4esNYkOw315S_fcLH-Lr5BsrHDaHP8UapVm5Pg6xmmpuWlolkNCY66cKGMYDSJMVuZMDi5cl6LtFF_lHSr9NwUNVecB0U-JZt9JTrNeo4Y1z1osdvyrY7cnZFUJHZGI7XUlAGjeS0jSBHv8J1h0LGs3NqYR_NTs6I8Wz20p4Yf2JUNt1WwOvafkZsZtg0l6X3PmjBUSrpY2fhszrImHEvl3IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264b3e2171.mp4?token=Uo0uW5eFulWQ4QlWaNERjm5dTPLXuxCxlCZyvNXdjz2XelYYjP59jou-8OFU3YTJyItJr1PW2ESthCsLlWjuKRoz7pkQN08N0wmeuVEaCArC8z6v_XdeDPmnJCXHq4esNYkOw315S_fcLH-Lr5BsrHDaHP8UapVm5Pg6xmmpuWlolkNCY66cKGMYDSJMVuZMDi5cl6LtFF_lHSr9NwUNVecB0U-JZt9JTrNeo4Y1z1osdvyrY7cnZFUJHZGI7XUlAGjeS0jSBHv8J1h0LGs3NqYR_NTs6I8Wz20p4Yf2JUNt1WwOvafkZsZtg0l6X3PmjBUSrpY2fhszrImHEvl3IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف، اوایل تیرماه:
خودم رفتم قطر، با امیر قطر صحبت کردم و 12 میلیارد دلار از پول‌های بلوکه شده ایران، طی تفاهم‌نامه اسلام‌آباد آزاد شدن.
🇮🇷
همتی، رئیس کل بانک مرکزی، دیشب:
هیچ‌کدوم از پول‌های بلوکه شده‌ی ایران هنوز آزاد نشده و همش شایعه‌ست.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70341" target="_blank">📅 21:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70340">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8w1-SudWDTF_rx3sZ5UyqwESDTSKo1BJRQPcrzH71WvkkIyizE2HkW2ZHVLsrMItE97cVWg73rsMH0Bdv42enZnvVOvM6-CgaTdPORiZoXsrhrSVvi8CRJvUrbX8oKd54f015Iqd-A82oWKZzsn-kduf9N_LjsQ8VFZv7BgxJDv5Ztet8s5_PprcE9iRn64evxrnvFOqR1ZX9-nqMCpXd7x8T1ZiEpxttQ1VgTTSw3cnQrDB7NVbrFYkVUyyecCbNxFZ_9oWe_AG6RFF-tRYk0dZBFy-U-owKxUTacbbOImN8olzF6RfhWksbDjJ8aftaVODfGJmHGvsYy_fffEOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بزرگسال‌ترین داوطلب کنکور ۱۴۰۵ با ۸۵ سال سن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70340" target="_blank">📅 21:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70339">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7149fa402e.mp4?token=iF2yPiTcY0OvX1vjdO_Np2l0ZAfPIdd1TT5yMNR4l3LBRWJaBzsFUf-34lFpJG_w0tKCJxjtsbsXRD23A-I34jijEmzDOi0YDCYE6K0Wm786HhaTcYgZIBZa6ie2_RvfjX9ZS7mu441lXKmtrqPDMDLRmHDuOAKJOqBW8Yo4nBBa-QqXu3NO7mxTtbLwBsSaY_wD1FryHJSA7-HAL0AqKLn2XJlfL8DbhNySe6l8eaZEQYRaAshiJdIpHYuT94gAPM3DTTBi_v2GWPuMGCGPeipl-HOVnhuxv6wKvS6VAwyXvEVQsz42ssAip5QpJ7xvHAFJLXEulGNpJg7-b15fJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7149fa402e.mp4?token=iF2yPiTcY0OvX1vjdO_Np2l0ZAfPIdd1TT5yMNR4l3LBRWJaBzsFUf-34lFpJG_w0tKCJxjtsbsXRD23A-I34jijEmzDOi0YDCYE6K0Wm786HhaTcYgZIBZa6ie2_RvfjX9ZS7mu441lXKmtrqPDMDLRmHDuOAKJOqBW8Yo4nBBa-QqXu3NO7mxTtbLwBsSaY_wD1FryHJSA7-HAL0AqKLn2XJlfL8DbhNySe6l8eaZEQYRaAshiJdIpHYuT94gAPM3DTTBi_v2GWPuMGCGPeipl-HOVnhuxv6wKvS6VAwyXvEVQsz42ssAip5QpJ7xvHAFJLXEulGNpJg7-b15fJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شهبازی مفعول :
نوید محمدزاده یه پست گذاشت زامبی ها ریختن سرش
فحش و ناسزا و تهدید و انفالو که چی ؟ حق نداری با این زامبی ها اختلاف نظر داشته باشی
این وضعیت زامبی هاست
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70339" target="_blank">📅 20:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70338">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e91c8463bd.mp4?token=korKnjF7wOIUgkJKszaQsSNuDs34VkEWqg-IZJYCXeeP85AYelYd47nQW_7F0KrFj0rd7ym66MpsBc3Z48f0VKQCmRONoRozBP9rKWokIst9wNRKZs-cf32TV5Fq9jpfH-bLEiDNyLjjw8YZIjfSUE2uAsGHK6k9EYZnN6UPcuYB6rFOYHcPJROYJEcyKga1870qsUx7u-eEI4jCN2VpLlzjTt6IZGweB2ylQ6_aoR_WHUAVVk6YFbrAm6Md42DC8FBk3UOEox0-xRyaCu_Obc1siAeW_VpXMcUN0Jc2nTS8HBuPAO4TcmNsYEBw6bRs2aQo659F6xLDRkYJhjTLRVRLRdYP_fQdZmcS11TRniLG3wj30QxFwHQ4xlAckMD3bYLTzMiwd62HYujxmAY9YYb3dIF-mAHCin0Vu-C4AcaRwMLqgZhAC9-Nhf9crarZ0hdOckewY1f_GmPKdYToL30iwU1t5UiZfqysVwdQGfYraplZt5ygXxv5iJkaHYyMxh0Q0KaEAfaZLDrchc3Y8T5bb_6HB-N2fjJFh6T47Bd0zkcEUIYnz_-AJcc9f3hwp752y2kOmRJpFICRKneB59GM3wvwpKTb5lCM1uLbB7jm_937ioPw_qW5eGKW9GWaW2IAc77yYVnGBeuMU0sRivcg5TZA9YKOZF0yLCOR55s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e91c8463bd.mp4?token=korKnjF7wOIUgkJKszaQsSNuDs34VkEWqg-IZJYCXeeP85AYelYd47nQW_7F0KrFj0rd7ym66MpsBc3Z48f0VKQCmRONoRozBP9rKWokIst9wNRKZs-cf32TV5Fq9jpfH-bLEiDNyLjjw8YZIjfSUE2uAsGHK6k9EYZnN6UPcuYB6rFOYHcPJROYJEcyKga1870qsUx7u-eEI4jCN2VpLlzjTt6IZGweB2ylQ6_aoR_WHUAVVk6YFbrAm6Md42DC8FBk3UOEox0-xRyaCu_Obc1siAeW_VpXMcUN0Jc2nTS8HBuPAO4TcmNsYEBw6bRs2aQo659F6xLDRkYJhjTLRVRLRdYP_fQdZmcS11TRniLG3wj30QxFwHQ4xlAckMD3bYLTzMiwd62HYujxmAY9YYb3dIF-mAHCin0Vu-C4AcaRwMLqgZhAC9-Nhf9crarZ0hdOckewY1f_GmPKdYToL30iwU1t5UiZfqysVwdQGfYraplZt5ygXxv5iJkaHYyMxh0Q0KaEAfaZLDrchc3Y8T5bb_6HB-N2fjJFh6T47Bd0zkcEUIYnz_-AJcc9f3hwp752y2kOmRJpFICRKneB59GM3wvwpKTb5lCM1uLbB7jm_937ioPw_qW5eGKW9GWaW2IAc77yYVnGBeuMU0sRivcg5TZA9YKOZF0yLCOR55s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
این مناقشه با ایران؛ ما از آن عبور خواهیم کرد. نمی‌دانیم چه زمانی.
🎙
خبرنگار:
آیا کارزار اقتصادی علیه ایران، چین را هم شامل می‌شود؟ چرا که چین شریک اصلی اقتصادی ایران است.
🔴
بِسِنت:
بسیاری از گفتگوها بهتر است به‌صورت خصوصی انجام شوند.
🚨
🚨
⭕️
بسنت درباره ایران:
ما شدیدترین تحریم‌های تاریخ را اعمال خواهیم کرد و به شما می‌گویم که این کار نتیجه خواهد داد.
این روش در ونزوئلا، پس از آنکه دست به محاصره زدیم، مؤثر واقع شد؛
هم‌اکنون در کوبا نیز کارساز است و در مورد ایران هم نتیجه خواهد داد؛
ما این رژیم را ساقط خواهیم کرد
!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70338" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70337">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">💎
میدونستین تو ویپاری
با شارژ بالاتر از ۱۰۰ دلار ۲۰٪ بیشتر حسابتون شارژ میشه
✅
🎁
برای مبالغ بالاتر از ده هزار دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ بالاتر از هزار دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70337" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70336">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/70336" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g29
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70336" target="_blank">📅 19:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70335">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47dcddfa33.mp4?token=EPyrP1BsReaV5SUf_E84zOZYpVtgAdB8kwU_NPiXM7qbHv7r-vt3R1NHgK23IBmmW0AtA4w8lxObsk2DpU6dS15uuCbrkjPwrekdxrF591pP6MuG4f55E4yWkpOh7lm1sjbvTkLnsR8vwkIgCa96f0DRUejgpKVUxHeyIlVPTM-FaKGUGO-6U47TPZ43OzBYoQ6iCIukpSMPwL6xl3o8sWBccQVVImhj4lzDWtZYkRi1_-fZzCuEqidTUxm6YAaypdYmT8WJTj3KMUcyoz94ptF6LPNsdkewEERFhgpC_ql1ljw68DLv-GGtTuFDiyIYVozd-JzP6XpFtj08VS03_ATWxCdKV6RJlUfWOH0ZjSgHStRodbV2P1LgAj1D6-rOy55yr-vSwRYCLdcRfNOm9xI5n_GAOb0b8uaY4-CRnE22Hb1SCCYohHtW6RbIzQQpYDPNJpYuSKrhVnnNEiw9sGZ0XSb82_mru2ZzGKQfmUZdL4FljpUwqidH4rD3CuUjlh3bUmA_dbFCMrFYyraFPMLUkJmHHQYlhJA0gmGBS9uU3JwRkBIgX1DdWtPzuiNJRNGD2VEcTKMUl_NFwJXeT6ephOr1_yu4deiJeZMeQcLpU6Ndt-3YNX6J-eAVyskrFuL-kopfLYcMb6uXCR33GF6SiE9kVmyp360h7LRd0_M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47dcddfa33.mp4?token=EPyrP1BsReaV5SUf_E84zOZYpVtgAdB8kwU_NPiXM7qbHv7r-vt3R1NHgK23IBmmW0AtA4w8lxObsk2DpU6dS15uuCbrkjPwrekdxrF591pP6MuG4f55E4yWkpOh7lm1sjbvTkLnsR8vwkIgCa96f0DRUejgpKVUxHeyIlVPTM-FaKGUGO-6U47TPZ43OzBYoQ6iCIukpSMPwL6xl3o8sWBccQVVImhj4lzDWtZYkRi1_-fZzCuEqidTUxm6YAaypdYmT8WJTj3KMUcyoz94ptF6LPNsdkewEERFhgpC_ql1ljw68DLv-GGtTuFDiyIYVozd-JzP6XpFtj08VS03_ATWxCdKV6RJlUfWOH0ZjSgHStRodbV2P1LgAj1D6-rOy55yr-vSwRYCLdcRfNOm9xI5n_GAOb0b8uaY4-CRnE22Hb1SCCYohHtW6RbIzQQpYDPNJpYuSKrhVnnNEiw9sGZ0XSb82_mru2ZzGKQfmUZdL4FljpUwqidH4rD3CuUjlh3bUmA_dbFCMrFYyraFPMLUkJmHHQYlhJA0gmGBS9uU3JwRkBIgX1DdWtPzuiNJRNGD2VEcTKMUl_NFwJXeT6ephOr1_yu4deiJeZMeQcLpU6Ndt-3YNX6J-eAVyskrFuL-kopfLYcMb6uXCR33GF6SiE9kVmyp360h7LRd0_M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از یکی زیباتر و حرفه ای تر:)
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/70335" target="_blank">📅 19:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70334">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e96e27ffe3.mp4?token=FhSbGXci9ccF_2oxUw7lfcXqXTJWBQb10MyEp0YGeViMZUlpvn7C7IoTkqnYzSLdxON65hk2XikHl-u1EjR4g8ksuaH29jUm_iWfA9aTnEq87Sqkc4aG26px6Hcnrnh6nbReLGSQ9dRGsPCG6l7Vj34QzYNCO0a7YS1c9-b4MxJkYGyqfSm-L2we4LgAYisyBYd_9vWqvzUskU9E3mDr-P4LvPaRvgzAMD-pD3pccXwrv8cuPPspsMZrki4_np6SS2LYt3ofOHSaohPs6meCGkEmsocTLTgKtW_NoEjtLYnlMcTaB86IHsw-2Jv7QwDIy3E6c1jbjY7izTBJ-jqeig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e96e27ffe3.mp4?token=FhSbGXci9ccF_2oxUw7lfcXqXTJWBQb10MyEp0YGeViMZUlpvn7C7IoTkqnYzSLdxON65hk2XikHl-u1EjR4g8ksuaH29jUm_iWfA9aTnEq87Sqkc4aG26px6Hcnrnh6nbReLGSQ9dRGsPCG6l7Vj34QzYNCO0a7YS1c9-b4MxJkYGyqfSm-L2we4LgAYisyBYd_9vWqvzUskU9E3mDr-P4LvPaRvgzAMD-pD3pccXwrv8cuPPspsMZrki4_np6SS2LYt3ofOHSaohPs6meCGkEmsocTLTgKtW_NoEjtLYnlMcTaB86IHsw-2Jv7QwDIy3E6c1jbjY7izTBJ-jqeig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
یه پسر دانشجوی ۲۱ ساله آمریکایی به کمک هوش مصنوعی یه مدل اونلی فنز به اسم «مایا» درست کرده و تونسته تو یه ماه اخیر ازش ۴۳ هزار دلار(۸ میلیارد تومن) درآمد داشته باشه
مایا اصلا وجود خارجی نداره این پسر از خودش فیلم و عکس میگیره و به کمک هوش مصنوعی به دخترِ لخت تبدیلش میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70334" target="_blank">📅 18:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70333">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3764b3347.mp4?token=JvpNCBHpq9bks-YZH4_HmPqALfUMlqLykzl2TU5jy0aVlZlw-L83NWRBYrSDjd3WQzpiMXLTdmpoqmlS11PofOiEKXDFCL98z14ccWhVd6-s5qhveSzx6KwSa11MQsiNV1aBYA2VWYvVnYzHpPTzIyqBVD_dMQu2YLFs1UEZgPcRemzEx7USlH4fZlNHCTcuRPiNafInospmLQw8E4-hUKsqztTDWU6pDXzqHp-HKiaKzUNh8vKS9Hlp1zkX_LzReZNg17thXaMgFBZyheKnze0O8jRIKGFUgDW2dwEFstwm0xrH0-Ic50J-qi4EzxCn1GfATHiaIW0x7xx90KzJzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3764b3347.mp4?token=JvpNCBHpq9bks-YZH4_HmPqALfUMlqLykzl2TU5jy0aVlZlw-L83NWRBYrSDjd3WQzpiMXLTdmpoqmlS11PofOiEKXDFCL98z14ccWhVd6-s5qhveSzx6KwSa11MQsiNV1aBYA2VWYvVnYzHpPTzIyqBVD_dMQu2YLFs1UEZgPcRemzEx7USlH4fZlNHCTcuRPiNafInospmLQw8E4-hUKsqztTDWU6pDXzqHp-HKiaKzUNh8vKS9Hlp1zkX_LzReZNg17thXaMgFBZyheKnze0O8jRIKGFUgDW2dwEFstwm0xrH0-Ic50J-qi4EzxCn1GfATHiaIW0x7xx90KzJzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر نقش ترامپو بهتر از خودش بازی میکنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70333" target="_blank">📅 18:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70332">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed854f2c03.mp4?token=W37gXMmAZux1j5OIo_9DBDD0JdmwGDYjo1GYvopqT3KlU9t1Tz3POek6hT3OJdpn-iG2hwjKvx3oWf4w2fBPESNpqlieQwAc-wJSWtv5DA9NEx-LBTAfmTfrZnrZFsJtnQDz75Z_Yhyt0K4266GOMbCsbrAV06K4Br7QTIc2RGMXv7gykSnZSxzMBUMGCC4qV7aRue39VkA4IKW_FMJybLu_RhZygEWsiio2yaGD_HtHMla5dH4hU5RcAKUhtCo_5PLJftsrzqwvJsrQeoTNbaN_DirdHGkIwZBCEHidAX5IMXXiQ1iMuAvLWcM3hSNIELXqnLSh6DnbXFQxvsiSZmFZE4_uYBefGFI3U31ht2F28HibmIPYJh6lVyRMpFuCAcjR7FM4-ZPJOUImqu5_Z2e7J9ym0qP3-DgHDq9K2-HyUZhJut4pSajCnLy2atbkMwTWEwBOZjqHai6bvHgSy8kWxEqyngQPiNjZt56Kk9Dm-liV82asWP-ixxnTilRy3oWphBSC8MR7s1NLvoxXJFaAypr8B8ZC3vOIcbNjhA7GuA24I1nl06ahgAiCx0x27OMl_m9OUMJ8oHAbCJMsV8T1XW3ZilvWJqCV2PtYwfQHGWtyRfwNrA9FbEKjWxF1KwIP0aXBMlL5aoazUKRtcVaPYbPrByuXXMX1HSPcrSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed854f2c03.mp4?token=W37gXMmAZux1j5OIo_9DBDD0JdmwGDYjo1GYvopqT3KlU9t1Tz3POek6hT3OJdpn-iG2hwjKvx3oWf4w2fBPESNpqlieQwAc-wJSWtv5DA9NEx-LBTAfmTfrZnrZFsJtnQDz75Z_Yhyt0K4266GOMbCsbrAV06K4Br7QTIc2RGMXv7gykSnZSxzMBUMGCC4qV7aRue39VkA4IKW_FMJybLu_RhZygEWsiio2yaGD_HtHMla5dH4hU5RcAKUhtCo_5PLJftsrzqwvJsrQeoTNbaN_DirdHGkIwZBCEHidAX5IMXXiQ1iMuAvLWcM3hSNIELXqnLSh6DnbXFQxvsiSZmFZE4_uYBefGFI3U31ht2F28HibmIPYJh6lVyRMpFuCAcjR7FM4-ZPJOUImqu5_Z2e7J9ym0qP3-DgHDq9K2-HyUZhJut4pSajCnLy2atbkMwTWEwBOZjqHai6bvHgSy8kWxEqyngQPiNjZt56Kk9Dm-liV82asWP-ixxnTilRy3oWphBSC8MR7s1NLvoxXJFaAypr8B8ZC3vOIcbNjhA7GuA24I1nl06ahgAiCx0x27OMl_m9OUMJ8oHAbCJMsV8T1XW3ZilvWJqCV2PtYwfQHGWtyRfwNrA9FbEKjWxF1KwIP0aXBMlL5aoazUKRtcVaPYbPrByuXXMX1HSPcrSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صنعت خودرو یه جوری داره پیشرفت میکنه که چین عملا داره سفینه می سازه
:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70332" target="_blank">📅 17:15 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70331">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1219ed44a7.mp4?token=kUgGKiyyJjLXOuIciLyMl29MvVi3oQbAxOIVPKqA2vpMEX8W_0Y8bGkLJoAfEO4CNbbE7hocuLvLNMHLwIpeBmctD0x3s8RsD1z2jfAeX-2-2KK_e-oNQFcwOh8Bo8XIfv5ukuCSy8BZfnr4Q0Mra3vGaXVT_vRtU-SeSpidhvA-VVp4GDq3Dzp-cfqK15B31dNndJ8z-KGmxf9uTmUPcqE4APD2OwNl4RJxnBo3UZ923zf6I1_27pVoOJoDNPQ9g75jT6U0HHuivc9z_3bGMYk3jkvqngN_hgOjtcqkd1e94w_iirpXHyXNRdpTzhHSo4HEMkF_N8qN3v0cT81New" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1219ed44a7.mp4?token=kUgGKiyyJjLXOuIciLyMl29MvVi3oQbAxOIVPKqA2vpMEX8W_0Y8bGkLJoAfEO4CNbbE7hocuLvLNMHLwIpeBmctD0x3s8RsD1z2jfAeX-2-2KK_e-oNQFcwOh8Bo8XIfv5ukuCSy8BZfnr4Q0Mra3vGaXVT_vRtU-SeSpidhvA-VVp4GDq3Dzp-cfqK15B31dNndJ8z-KGmxf9uTmUPcqE4APD2OwNl4RJxnBo3UZ923zf6I1_27pVoOJoDNPQ9g75jT6U0HHuivc9z_3bGMYk3jkvqngN_hgOjtcqkd1e94w_iirpXHyXNRdpTzhHSo4HEMkF_N8qN3v0cT81New" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇬🇧
🇺🇦
🇷🇺
پهپادهای تهاجمی ۱۰۰۰ کیلومتری بریتانیا، جنگ را به عمق روسیه می‌برند، مسکو به خروش آمده است
بریتانیا پهپادهای تهاجمی دوربردی را که قادر به دستیابی به ۱۰۰۰ کیلومتر هستند، در اختیار اوکراین قرار داده است، در حالی که طبق گزارش‌ها، پهپادهای ساخت بریتانیا اکنون در حملات عمیق علیه اهداف در داخل روسیه استفاده می‌شوند.
از جمله آنها می‌توان به نیان، یک پهپاد تهاجمی دقیق با موتور جت که توسط کالن لنز از شرکت BAE Systems توسعه یافته و طول بال‌های آن ۲.۹ متر است، اشاره کرد.
طبق گزارش‌ها، سایر سیستم‌های ارائه شده توسط بریتانیا برد بسیار طولانی‌تری دارند و تا حدود ۱۰۰۰ کیلومتر برد دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70331" target="_blank">📅 16:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70330">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4669764466.mp4?token=Rq5P_bWdqc7cvkqORstKBoSM_B-Orh4pDRRev4Joa-Du1Sd9kaXdq3h21uSBpOwgya3TDiVLvxKoARCHY7IqG2ZvD-jaquzh3pasMcfxR5RWQbyiKQ4YOHKryUa_PPjykw0RSgLsgUjctyKAX-zQ51dbfbTqlwDy7NMZ2oXq79xKhSpcYRBHN1j-ycoI9c7n8N_UPhMKzS4xLcaNdHAOj1qBnJKPa7KkGeWLlc8uICnjkClm8gKDP63_JA2JIV9YfxzR5VqtPiObTC7ws-lr4w97xh69eYOB_fY0MUHXl-G4jj-vMNO1bsCP_d50qOjTub1fU4LUi2JonuucvoblJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4669764466.mp4?token=Rq5P_bWdqc7cvkqORstKBoSM_B-Orh4pDRRev4Joa-Du1Sd9kaXdq3h21uSBpOwgya3TDiVLvxKoARCHY7IqG2ZvD-jaquzh3pasMcfxR5RWQbyiKQ4YOHKryUa_PPjykw0RSgLsgUjctyKAX-zQ51dbfbTqlwDy7NMZ2oXq79xKhSpcYRBHN1j-ycoI9c7n8N_UPhMKzS4xLcaNdHAOj1qBnJKPa7KkGeWLlc8uICnjkClm8gKDP63_JA2JIV9YfxzR5VqtPiObTC7ws-lr4w97xh69eYOB_fY0MUHXl-G4jj-vMNO1bsCP_d50qOjTub1fU4LUi2JonuucvoblJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
جوابتون به صحبتای ترامپ درباره تنگه هرمز چیه؟
🇮🇷
حداد عادل:
باید بگیم تنگه، تنگه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/70330" target="_blank">📅 16:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70329">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdYxfKnoA08a4I9YOMiELtYDR7NKrYZEKU0SWyKWQ_pUMBOmewuuXTtFJ8iJ7kjtM2OX5OnyOXdRzjhUB98jkQF2COgEnzVfxXGkcuCVg97Yuu5PrKwaon-l8IcimYGbKUM9IeP-nEIjW07wN8a2H6kugBbz3L0_GBE-n3PAnCQZ3SAa6I3zGOCtN4eCJy_sTb0sqljgA4VmxV3Ku9Hxnxu7D2u6CvUyEAujTO2XJtffOplCSw1ffVElH9IwbhQYEUPdFKbq9TEP9MBi8t42VJmFcli0YgTZwvlSuC4xUS-2rw2RI3tIXANlJp7Gl5dSeGqhBu1mSMXyxsTp5Re1KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
〰️
فرماندهی مرکزی ایالات متحده (سنتکام):ناوهواپیمابر جورج واشنگتن به منطقه عملیاتی سنت‌کام رسید.
ملوانان آمریکایی در تاریخ ۲۰ آگوست، همزمان با عبور ناو هواپیمابر جورج واشنگتن (CVN ۷۳)، بر روی عرشه پرواز آن کار می‌کنند. گروه ضربت ناو هواپیمابر جورج واشنگتن پس از ورود به صحنه فرماندهی مرکزی آمریکا (CENTCOM) دیروز، طبق برنامه در خاورمیانه فعالیت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70329" target="_blank">📅 15:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70328">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85771a2a65.mp4?token=OQXjLULgPH2UviH6BZaL7y9UZcl4FUxPKWM-6aT3IQ7fPAjD_DTzxNxvyngSABRaoqRJbJ7ktnZhR8TasJQZ7aEM2hb0HXRM9cQqIDCV5YCeVr3KpOABcUtfdzdp70qnl1l2u4v6VtdEZCjc8E4N8vSgatmRAFrwDhwLr5He-aUzlAyR_fDtmlA9VRhvq-dxpkvzT_X7Bi8R9xg5wKZzULUoTVMk8wB0KC9_oyH7CeAh5xhlmObk8sjbCDL1ppYNiB7L0-dHf8M19E8IkdbBZwP-NVlj1hbDOi1GbDhEcKUo4jiKGj63UzKXOlZF3LqvqB6cS4g_9CjKdgjBw07hpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85771a2a65.mp4?token=OQXjLULgPH2UviH6BZaL7y9UZcl4FUxPKWM-6aT3IQ7fPAjD_DTzxNxvyngSABRaoqRJbJ7ktnZhR8TasJQZ7aEM2hb0HXRM9cQqIDCV5YCeVr3KpOABcUtfdzdp70qnl1l2u4v6VtdEZCjc8E4N8vSgatmRAFrwDhwLr5He-aUzlAyR_fDtmlA9VRhvq-dxpkvzT_X7Bi8R9xg5wKZzULUoTVMk8wB0KC9_oyH7CeAh5xhlmObk8sjbCDL1ppYNiB7L0-dHf8M19E8IkdbBZwP-NVlj1hbDOi1GbDhEcKUo4jiKGj63UzKXOlZF3LqvqB6cS4g_9CjKdgjBw07hpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
‏همتی رئیس کل بانک مرکزی:
یکی از مسئولین رده بالا که نمی توانم اسمش را ببرم، چون ممکن است ناراحت شود در سفر خارجی به من گفت که آمریکایی ها فکر کردند ایران هم مثل ونزوئلا یا کشورهای آمریکای لاتین یا جاهای دیگر است.
ایشان به من گفت که شما در آینده نزدیک نقش جمهوری اسلامی را در منطقه خواهید دید، خواهیم دید که در واقع آن چیزی که آنها فکر می‌کردند نشد و یک چیز خلاف آن، عظمت ایران را خواهند دید.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70328" target="_blank">📅 15:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70326">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d602fb7461.mp4?token=dq69NtOmqC8Oy0stGBmckK4g6ALD6ur3yTVQszd_ejyF4maxz6z0NZFGPs_TCibdWj0U7WmgM_nbTco_K5BhWZcMgzVCNoT0WMqwr5wnP1l3dOnFwCRYgpJmWvvk7N2XiV9hEyeGepIhzATtZNMPVjePcTxP8ONL-UiIZMgIi544E-1CvRf6mfx5VzOa_Jac2eoUFSXtZj_c-ln2WLM6-gnwLetpNQqkAZI1PU8pejtzR4bKPYv9PAXmNlcwDkEJXBQUdj6Cx4Sd9vsOmpsU4qdPcPDm1GOqQleciCVaHbDDt_h6MnALDPu-JvW91ri7PAsK_xVbcSvTNA_6fdBl_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d602fb7461.mp4?token=dq69NtOmqC8Oy0stGBmckK4g6ALD6ur3yTVQszd_ejyF4maxz6z0NZFGPs_TCibdWj0U7WmgM_nbTco_K5BhWZcMgzVCNoT0WMqwr5wnP1l3dOnFwCRYgpJmWvvk7N2XiV9hEyeGepIhzATtZNMPVjePcTxP8ONL-UiIZMgIi544E-1CvRf6mfx5VzOa_Jac2eoUFSXtZj_c-ln2WLM6-gnwLetpNQqkAZI1PU8pejtzR4bKPYv9PAXmNlcwDkEJXBQUdj6Cx4Sd9vsOmpsU4qdPcPDm1GOqQleciCVaHbDDt_h6MnALDPu-JvW91ri7PAsK_xVbcSvTNA_6fdBl_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🤖
در جریان «کنفرانس جهانی رباتیک» در پکن، بر اثر نقص فنی در کنترل‌کننده‌های از راه دور، عملکرد برخی ربات‌ها مختل شد و از کنترل خارج شدند
😁
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70326" target="_blank">📅 14:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70322">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P1LGMADS68-sFLw5nc1kWd3ShGTkJrswHybfkO83s-mC8iM7YhDRYiR2U29jzpXKbRLkVo10Xex0Uoi3AZinq5TE7RV2-_VI_JTqvKG4Tsb7DmerPH5YmBnkxElqJUzhvwotMmNnd0aocEnrs_WJGNvgArYk2Sn3FdDw4QuB1y6SlnM1yY8Atx8Be8MWy9wR4umbkZsIi9K3TexpP2Sf5lniO0JyKl-PkIzmzyQ_1WkvvFbghtJqEntr44v-EHfePZdzUOneH9munE9uKpR3ADswKCv1oV7_cGT9s-vxUzSqsHJCMcRouD4PSaEuvuTddQT3KKrW2elMDP-iQjj6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9d122dfe.mov?token=pYEy0ArsoX1ymZ43Z8V_QM2aPvAROy4sbVtxd8I9dsgzFUt3wlxbOZNmqAhUt1oYOQ1xs5QvNCQ8pL-KeXt6GjF_Uc5NegACpLD-VH-FbtKf258DOEOA3ob4mzPzriXDeP2xsn2-L1Uw3wgG4aY9di0Viz_--NQUEuR-ZLl0HEXdSLqRqXsNFjcdUHAs1VMgslliNovSyq9s_j1YsyhBiW8MNeZXXVGrFE8ZJGcanKtW4wk1vbTMdkdh81lul-AWZgQAX9aoDLNtjRdGMp6-M9ALjdskMhRjDjywOZ_5e4KhHDijAicNlzrb4AA46jpCcsttG0cxlgevxIJ6i3r0lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9d122dfe.mov?token=pYEy0ArsoX1ymZ43Z8V_QM2aPvAROy4sbVtxd8I9dsgzFUt3wlxbOZNmqAhUt1oYOQ1xs5QvNCQ8pL-KeXt6GjF_Uc5NegACpLD-VH-FbtKf258DOEOA3ob4mzPzriXDeP2xsn2-L1Uw3wgG4aY9di0Viz_--NQUEuR-ZLl0HEXdSLqRqXsNFjcdUHAs1VMgslliNovSyq9s_j1YsyhBiW8MNeZXXVGrFE8ZJGcanKtW4wk1vbTMdkdh81lul-AWZgQAX9aoDLNtjRdGMp6-M9ALjdskMhRjDjywOZ_5e4KhHDijAicNlzrb4AA46jpCcsttG0cxlgevxIJ6i3r0lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حمله موشکی شب گذشته روسیه به کی‌یف منجر به کشته شدن شش نفر و زخمی شدن ۳۳ نفر دیگر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70322" target="_blank">📅 13:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70321">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hy4DeoKcuc61L_eOjfJTaYGs1P-XBIuUijn1plkqE_tpMT-cZIBC2tejLZZ5jEn03akjYFB72-hi_ojG5O5QGM8z1eAXqV75aXVCZ2kdgmHT0hBD7BZNqydujELf3haWJi3OpQZVCM3JLjT5L5dvHC66oVInJl8MBr_fAOxJuZX6ABWooYXIr2gqbC2En6nSRh5xvwRwAkFvBXUogmNeeFxmNKB_9-ubATW09_4OpzKE1x8rIECMhalFSiGZaZqruGXRb5fobd6jEyI5JC23z4MKaAHjhSj54L8C9eAs7iC6ig1MchOdw4zQf1Lgp0ubwCj6fKPiIhHFbTNq1tuZlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ابراهیم عزیزی:
ما تمام تحرکات شما را زیر نظر داریم. هرگونه اشتباه یا محاسبات غلطِ دیگر، پیامدهایی به‌مراتب سنگین‌تر از گذشته در پی خواهد داشت.
پیش از آنکه دیر شود، فوراً به حضور خود در منطقه پایان دهید و نظم منطقه‌ای جدید ایران را بپذیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/70321" target="_blank">📅 13:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70320">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70320" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/70320" target="_blank">📅 13:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70319">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emlGdGKMHyZZDmEmIMNULfYovT7Cv0KSuaVuuhWYCmriuSfx0c40r_MlqMdhB6Mc5Y4BMy6d5W-ykxGt8mfy7cSM0dOfTjnXXksJ8OpJCeNaltCeNNoRwjghZ2a5w8qG80O_Y-QM6SHXrll7yQIhFNzTmqzvKpYi6TQAnPnMyhc0EO2yeOtQESsJDwa25Nut3jDErjJ_MpJJreYDDCrcIY9Sf9TuLzN6fD6pOkTYbXWyTDp4xdQ--bNi8SMq2i0HPePhdaFGI63Jmk8h4XEmtsowouf-YDGeSjBnN0MTbVvhz9U78EUngkKyizr5GoBdCMl0v689rNcYIMhkAPP2cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r29
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/70319" target="_blank">📅 13:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70318">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeuiV91cXy2WI8I37y3F7huDF07NF_FL2eAh0sM6EUvsgCbyyDowjGLeWvF3DJTCxUuvihyd_jMYQFe2Pu_W62sQaOtxBJh53eELEqiJbsXJCBJjbnOivcUWpL99URq51iJrOw9kMP0G_MtC9HoopanjcIVMXfC4OeB8N6TyGVs4aGpo_nUVGTNB_6-lkJC3B0zZnzCetFRfOGynFQ-Ehx8Xs1bpq43HXSQRzr2nAMLlBemSxD4kivlIFQ8WeRChq3WdVOi2n9wzNbYopmI9Lh6Qc2oJZeo8p1rcu8AcdZ6b-twNN3EUIEVTIspyx6tUji_StMmpZu1w1xQXSljJ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇷
همتی رئیس بانک مرکزی:
درحال حاضر هیچگونه صادرات نفت نداریم
اما به حضرت آقا گفتم وسایل زیاده نگران نباشید
محاصره دریایی و تحریم ها شدیدا اقتصاد ما رو ضربه دار کرده
گرونی که بنظرم طبیعیه در شرایط جنگی هستیم
از مردم مبعوث شده درخواست همکاری داریم در این دوران سخت
این جنگ تموم بشه وضعیت آروم بشه خدا بخواد دلایل کاهش قدرت خرید مردم رو بررسی خواهیم کرد
ریالی از پول های بلوکه شده آزاد نشده
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70318" target="_blank">📅 12:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70317">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcfbcfa9f.mp4?token=jecHojBIY6oG2BIKcvocsDpX_bDwwLRw2rXVejXtNOy86TDkPkk7CfbcLaUSlBXQLKlsARUw_fmnosWBVYrHnaOkJ6lBcOIlhtTJ6HT28B_55rRvQ8SQDnnILoWvLhV4xzzum68FYG2b0Fn5TgpU14Q_GeETcLkndPGAJRU-nwOseWteyrL1M01-jPYOPXSxTOS4qQ266GMORsad02mrxyzf4UaDknPK6F-giha1JUJzBaHTp9y-nXC449zmDUIZbWXCt-kWj4mCM7bbnElHvkzki16ZyeOo_gwuRnITXS7R01ioNBXoFY-Md5FFZwGa7SWTlvnwRCWm1igoSlBp1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcfbcfa9f.mp4?token=jecHojBIY6oG2BIKcvocsDpX_bDwwLRw2rXVejXtNOy86TDkPkk7CfbcLaUSlBXQLKlsARUw_fmnosWBVYrHnaOkJ6lBcOIlhtTJ6HT28B_55rRvQ8SQDnnILoWvLhV4xzzum68FYG2b0Fn5TgpU14Q_GeETcLkndPGAJRU-nwOseWteyrL1M01-jPYOPXSxTOS4qQ266GMORsad02mrxyzf4UaDknPK6F-giha1JUJzBaHTp9y-nXC449zmDUIZbWXCt-kWj4mCM7bbnElHvkzki16ZyeOo_gwuRnITXS7R01ioNBXoFY-Md5FFZwGa7SWTlvnwRCWm1igoSlBp1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیشبینی زنده‌یاد مانوک خدابخشیان درباره ترکیه و اردوغان:
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70317" target="_blank">📅 12:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70316">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⏺
🇮🇷
محمدرضا نقدی، فرمانده ارشد سپاه:
رئیس‌جمهور آمریکا خیلی کوته‌فکره و کاراش بچه‌گونس
بنظرم مشکل داره و برنامه‌ای برای آینده نداره و حرفایی میزنه که شاید ۲۴ ساعت بعد خودش هم یادش نباشه
حرفاش باعث شده قدرت آمریکا زیر سوال بره و ما دیگه روی حرفاش حساب نکنیم
به نظرم رسانه‌ها هم نباید زیاد وارد جزئیات حرفای رئیس‌جمهور فعلی آمریکا بشن، چون خیلی از این حرفا اساساً بی‌محتواست
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70316" target="_blank">📅 11:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70315">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d971ab84f7.mp4?token=ckBPbgao8jow02HiwP7XTvnROlaoZJhfwfbHC0-P7qgd2InbFD36pKBwCbySeDcowSnfBSxDt4i8Frl2ogZaIgM6iu1w1qYAzq6O6aRGdgOclXf-Rsuk79dqFuf9rjE8ahRDaiEPD0kID3f829OTW8Sx7HCQ5Cn5ffLaC6hmuql2Gy3UWX3jFqdNhYH7r_E2j9DFJHm3-TPP0KtysEqpfXEV1wsSvU_1l3DPnW8oF5ltNBuD_qDIykrpubDDQOg9SXPvJI1Xmm7KRE8qtqEn1RObaWYraFE2WOc2dZyMovThgBgMp7kdrLcFLIRgxpCGV_1jNhQSopxj936nV7YYFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d971ab84f7.mp4?token=ckBPbgao8jow02HiwP7XTvnROlaoZJhfwfbHC0-P7qgd2InbFD36pKBwCbySeDcowSnfBSxDt4i8Frl2ogZaIgM6iu1w1qYAzq6O6aRGdgOclXf-Rsuk79dqFuf9rjE8ahRDaiEPD0kID3f829OTW8Sx7HCQ5Cn5ffLaC6hmuql2Gy3UWX3jFqdNhYH7r_E2j9DFJHm3-TPP0KtysEqpfXEV1wsSvU_1l3DPnW8oF5ltNBuD_qDIykrpubDDQOg9SXPvJI1Xmm7KRE8qtqEn1RObaWYraFE2WOc2dZyMovThgBgMp7kdrLcFLIRgxpCGV_1jNhQSopxj936nV7YYFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از دست هرکسی نوشیدنی نخورید
؛
فلونیترازپام که به «داروی تجاوز» معروف شده، یه آرام‌بخش بسیار قویه که مجرم‌ها واسه بی‌حال کردن قربانی‌ها ازش سوءاستفاده می‌کنن.
این ماده می‌تونه باعث گیجی شدید، خواب‌آلودگی، کاهش هوشیاری و حتی فراموشی موقت بشه.
ولی یه باور اشتباه توی فضای مجازی پخش شده؛
اینکه این دارو همیشه نوشیدنی رو شور می‌کنه!
شکل‌های جدیدتر و پنهانی‌تر این دارو میتونن بدون اینکه تغییری تو طعم و ظاهر نوشیدنی ایجاد کنن خورده بشن
پس به هیچ وجه از افرادی که بهشون اعتماد کافی ندارید نوشیدنی نگیرید مخصوصا دخترا بیشتر باید مواظب باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70315" target="_blank">📅 11:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70314">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41769ecb44.mp4?token=Mtl0uxvmFziZmRUak-X5SEfSWFeWwMYbxmrTk2pHG2XVNwfEo2w9knWU_Qh9t7kPRnpkSRwThhJRgAIelVP0Ga0SqFt8JVoHbsSRhMV9lqBjye73hNtPJeGCfK6efz5cPxE1jGMeIpWsijSxLJ9wuwGXwpH7tXYjCr5Ld3Skpw_jKii_c3sYvgmDjwp7bh8QGonpxs6zLih8H1hMqQ1K881UPFdZOatuxCova3pV10_XzGtkS96tacwHWri2D-LeAT1ML3WtEhCCVvNCDarGEuYpHvXSu368eZxQ3g3ZhUsjGXCrnAVZItFLcJHOc0Tuj2M4510G3dSVmtAxfLMFkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41769ecb44.mp4?token=Mtl0uxvmFziZmRUak-X5SEfSWFeWwMYbxmrTk2pHG2XVNwfEo2w9knWU_Qh9t7kPRnpkSRwThhJRgAIelVP0Ga0SqFt8JVoHbsSRhMV9lqBjye73hNtPJeGCfK6efz5cPxE1jGMeIpWsijSxLJ9wuwGXwpH7tXYjCr5Ld3Skpw_jKii_c3sYvgmDjwp7bh8QGonpxs6zLih8H1hMqQ1K881UPFdZOatuxCova3pV10_XzGtkS96tacwHWri2D-LeAT1ML3WtEhCCVvNCDarGEuYpHvXSu368eZxQ3g3ZhUsjGXCrnAVZItFLcJHOc0Tuj2M4510G3dSVmtAxfLMFkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تمسخر صحبت های خاتمی در صداوسیما
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70314" target="_blank">📅 10:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70313">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/670edf8121.mp4?token=CQ1e2d686ICGW9TdiFuxJBWo4kIk0UdcCMj04OZO_h1JMCalg38CnPeVJbmtSzERsWmXB4nhHARoDgNMLlaD_FCP7Da7aSq_CqabknQe6b9qvdYfJrfXFNULshBsAcjPgv45C9EyGA6MK53FJSjJyCwua_p4EMdFzZLRYN6uTWlq6fx-1zJsrsNdHPD2aLaiu7Oqpp7QvyOOv-B06LTFdgqspLjGNpPZOgsfsZkrI49P29i2l2mgvmshjhcOtNDWiVNtRUDZDkHSpGcmQElBL5j8QgogdEoM7bMlL9N-byoVZ_xpddzPimZbl4qH34TbedCXV0_IlHypn5S01h1NNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/670edf8121.mp4?token=CQ1e2d686ICGW9TdiFuxJBWo4kIk0UdcCMj04OZO_h1JMCalg38CnPeVJbmtSzERsWmXB4nhHARoDgNMLlaD_FCP7Da7aSq_CqabknQe6b9qvdYfJrfXFNULshBsAcjPgv45C9EyGA6MK53FJSjJyCwua_p4EMdFzZLRYN6uTWlq6fx-1zJsrsNdHPD2aLaiu7Oqpp7QvyOOv-B06LTFdgqspLjGNpPZOgsfsZkrI49P29i2l2mgvmshjhcOtNDWiVNtRUDZDkHSpGcmQElBL5j8QgogdEoM7bMlL9N-byoVZ_xpddzPimZbl4qH34TbedCXV0_IlHypn5S01h1NNIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خانم دکتر از یکی دیگه از فانتزی‌های آقایونِ ایرانی پرده برداشت؛
یه خانم اومده دکتر و گفته همسرش 3 تا گوجه‌سبز رو همزمان کرده تو واژنش ولی متاسفانه دیر جنبیدن و واژن هر 3 تا رو قورت داده، ولی خوشبختانه همه رو تِخ کرده و عفونتی درکار نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70313" target="_blank">📅 10:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70312">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e03e1f6f01.mp4?token=eoNIniJPoDHuAfUAXhGP-k3fgV_oUDSi0FnTZfheTOJis7aIhKgWmQRFfoSVsBF5cSeAihaohwZdOEEUwGM4deV4LHMPqfB95HSKIa1F2k08pF2UUGq8JQ8WCjBhci5udZ8jls2xhMUgXojj3W8mz_OgzWRO9EFIfGozS1e4jaOSZc8YUZ_Qo6Ew7yU2B2oWc2NpUUVi-9QS5GMJMh3brq2FvXqah4cgiXmfT-4bMB0O6nsUrg9E4wG4Wd00oWQVH0HYDAfR2yaoXbma1BZ3VHMjdGv8kMyzNNjqPWVs3baRS_VqTtAxrovDRZPlnlCnuRq2pUD3QIMCT8cq0evD1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e03e1f6f01.mp4?token=eoNIniJPoDHuAfUAXhGP-k3fgV_oUDSi0FnTZfheTOJis7aIhKgWmQRFfoSVsBF5cSeAihaohwZdOEEUwGM4deV4LHMPqfB95HSKIa1F2k08pF2UUGq8JQ8WCjBhci5udZ8jls2xhMUgXojj3W8mz_OgzWRO9EFIfGozS1e4jaOSZc8YUZ_Qo6Ew7yU2B2oWc2NpUUVi-9QS5GMJMh3brq2FvXqah4cgiXmfT-4bMB0O6nsUrg9E4wG4Wd00oWQVH0HYDAfR2yaoXbma1BZ3VHMjdGv8kMyzNNjqPWVs3baRS_VqTtAxrovDRZPlnlCnuRq2pUD3QIMCT8cq0evD1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش تو تبریز، یه پسره داشته مزاحم یه دختره می‌شده؛
کاسب‌های اونجا بهش تذکر میدن که نکن ولی پسره میگه به شما ربطی نداره!
اونا هم چند نفری می‌ریزن سرش و پسره رو میندازن تو سطل آشغال...
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70312" target="_blank">📅 09:34 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70309">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pawFlE9o-kPTZYgNFkHW6t71wd_LrjUYdqHNjkFNEHeX-UYwhrpHhycodq32n5qlvj4IWPMNH8WGqtaPg2XQ54Y5EKeIvgCZGWva0LblzNXB7Aic766h-rvAZ2Jd6rJhqClsQBcrwv9pkbHTABioOeE4RsDbZzCf0VRztG2OxNbwqd8hJJtccPT7dVbtXEYoclEs69vK3iqi_ELYMOMLhFx_Ie8-P9WpFGJqwAmb25TeXO2T08atVx6AFYGqW9wOxQ0j1pYwmvEXlQYTSz7kIPlRuEC1yR4BBL_cSiv6-lt9QGyE78aDPsEB0hRL00njdCHAdmqhZLsOV84JB926KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esZIlzrzhq3lmOeWuSSnNCAcMSS_lbY-1zN-TeaMUq2-eWRN0qMEyuy1_3tXu_DwmL7THQRMErfJoTJcbDyuHwVszkwAOjh6hwpWK9tte1PWPEOjw8rOKdd0qo3tVkp5syKFD4gSlfaHff0RhhxC642tLXfEVXkcfs8P3J5TIzefQb19Xn0ucHzeOkiW8GYkfjP8ddkjq8pEDIEyF5G_YZfpB2-KTvMqi514H9DLg0TO1-_MYGnSCeQywsi1uEaKt043ja_L0XBb_qTNLqNss0IZsnJYJHVFwBU-XhB6zglD6xsYnIZHD8JlAa1T-olHl633mI0ooeZfkq_yY5_3Ow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1fd6dc78.mp4?token=svnBGdX4pFM-ewj0gDyN2AnidDK5G_8ndt8Hi9Rgpt_MQyHBxEO2ojBtTvWJ8IoUGAytAXhSErgo26GHccPDWizUoXIPtPIZwRilvwef8IHsA7foYD5tOay1wP4iSTuvLXWVz_c1yaieA1uZmY2tQ4nfp9ON5PUqJ1Rfejb-SSfClxqp2NydoXNhfwmw3Wu0Z8-vRfdqqJ1GOLOQxWxK3P5EDSyEAENakDWeHzXwazUSFBw2FUArG0eNGncSGnyZDfYjhQfiGC5IxVo9EF8OTX2quYeb_45p0TbmwCe8_QLXdbF-iYcC2MHy5npcV6fM-oNZuwPvljc-vZnC57sGUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1fd6dc78.mp4?token=svnBGdX4pFM-ewj0gDyN2AnidDK5G_8ndt8Hi9Rgpt_MQyHBxEO2ojBtTvWJ8IoUGAytAXhSErgo26GHccPDWizUoXIPtPIZwRilvwef8IHsA7foYD5tOay1wP4iSTuvLXWVz_c1yaieA1uZmY2tQ4nfp9ON5PUqJ1Rfejb-SSfClxqp2NydoXNhfwmw3Wu0Z8-vRfdqqJ1GOLOQxWxK3P5EDSyEAENakDWeHzXwazUSFBw2FUArG0eNGncSGnyZDfYjhQfiGC5IxVo9EF8OTX2quYeb_45p0TbmwCe8_QLXdbF-iYcC2MHy5npcV6fM-oNZuwPvljc-vZnC57sGUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ظاهرا علی خامنه‌ای به یه شاعر سفارش داده که یه شعر تولید کنه که خامنه‌ای بعنوان سروده‌ خودش منتشر کنه، شاعر هم یه شعر کرده تو پاچش که اگه حروف اول مصرع‌ها رو به هم بچسبونی میشه:
"من علی خامنه‌ای زاده شیطانم"
🔴
حالا رسانه های حکومتی تازه متوجه گاف شدن و دارن شعر رو از سایتا پاک میکنن
👅
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70309" target="_blank">📅 09:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70308">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDMUAbiYOanEajcXFexkpykpYb-Rw_GyOpiaxgtyQ1zlJEU9WI1_Ay4styo4l1TXUXN5RJHpwOLjVrhzTSDG0Sdswz0fvXlXD-rUXwxPr6QCBShUAoDAicKTj0dTzEUQ52azt0woi1xspLX2dS88N5pk0DB0TtnXkn3nCl0LimBguNtU3u_xJ1aBvQ3jT3vax5DKRPQCjPEjINDtzPf04GsSjzRxkZXSrBVk6mSdb5yu_GPLVJ_POWO-Ry8e4VJFZrcPR8ZM8tPchif9FQeMrorgqr1O4kXBYK_qMJ70UIZtznSvUZAo1DR5PTnHvfL9bK1YMyP5ullwaRQdf-su1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⭕️
🇺🇸
#فوری
؛ترامپ درباره‌ایران:هیچ‌کس به اندازه من به جمهوری اسلامی ایران فرصت دستیابی به توافق نداده است. اما متأسفانه برای آن‌ها، این فرصت از دست رفت.
از این رو، امروز من خبر از اجرای «ویرانگرترین عملیات اقتصادی تاریخ علیه یک کشور» می‌دهم!
این اقدام، مصداق جنگ اقتصادی و انزوا در ابعادی بی‌سابقه خواهد بود.
نیروی دریایی‌شان از میان رفته، نیروی هوایی‌شان نابود شده، کارخانه‌های نظامی‌شان به تلی از خاکستر بدل گشته، ارزش پول ملی‌شان از بین رفته و کشورشان در آستانه فروپاشی کامل قرار دارد.
همچنین امروز اعلام می‌کنم هر کشوری که به مؤسسات مالی، شرکت‌های تجاری، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد تا هرگونه شریان حیاتی برای ایران فراهم کنند، خود با پیامدهای اقتصادی سهمگینی روبرو خواهد شد.
قاچاق نفت، خطوط سوآپ (معاوضه)، انتقال پول نقد، صرافی‌ها، ثبت کشتی‌ها و شرکت‌های پوششی؛ همه این فعالیت‌ها باید همین حالا متوقف شوند. شما خود می‌دانید که چه کسانی هستید.
این یک «روز سرنوشت‌ساز اقتصادی» (D-Day اقتصادی) خواهد بود و ما نیازمند آنیم که تمامی متحدانمان در کنار ایالات متحده آمریکا بایستند تا تهدید ایران را منزوی و خنثی کنند.
این دیوانگان در تنگنا گرفتار شده‌اند و این اقدامات تاریخی، آن‌ها و توانایی‌شان در گسترش تروریسم در سراسر جهان را فلج خواهد کرد.
ایران هرگز به سلاح هسته‌ای دست نخواهد
یافت.
از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور دونالد جی. ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70308" target="_blank">📅 08:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70307">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔥
امشب چه تیمی می‌درخشه؟
⚽
کدوم بازی گل‌دار می‌شه؟
📊
کدوم تیم ارزش اعتماد بیشتری داره؟  ما بازی‌ها رو قبل از شروع، با آمار و تحلیل بررسی می‌کنیم؛ نه با شانس و حدس!
📌
برای دنبال‌کردن تحلیل‌های روزانه فوتبال عضو شو:
🔗
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70307" target="_blank">📅 02:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70306">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=A6a3Hl5HuKOn8TZdtNMXPYWAsrCWI4F5j3DWauhJVIXv2z441ol1hmG82vhTlWY-ympfQY99iZLinq98nhasCyDya7LrM63wQURRG-fYEkIj8xdH99vOmCy6wVHK30rG_Xx-Oivt5DnJcNQZGt1bu8-AqkHCMbVIs-sn-bh61kbOT-934q7uup3r54HSlc-yuP2ZFsdLEVQCPAR_KUPcHLnUo-YnS4VfGsotcyHKpYxqKRdgd3lFZ-TSCrU5m6qSx6umdmMSfyzsNYOH0-jWyyNh35kLjaA3nhrMqOx9aV-yvZeQ3fXygHH4s_ZW514V6_xuhhj8qeuO-JWliyFnIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=A6a3Hl5HuKOn8TZdtNMXPYWAsrCWI4F5j3DWauhJVIXv2z441ol1hmG82vhTlWY-ympfQY99iZLinq98nhasCyDya7LrM63wQURRG-fYEkIj8xdH99vOmCy6wVHK30rG_Xx-Oivt5DnJcNQZGt1bu8-AqkHCMbVIs-sn-bh61kbOT-934q7uup3r54HSlc-yuP2ZFsdLEVQCPAR_KUPcHLnUo-YnS4VfGsotcyHKpYxqKRdgd3lFZ-TSCrU5m6qSx6umdmMSfyzsNYOH0-jWyyNh35kLjaA3nhrMqOx9aV-yvZeQ3fXygHH4s_ZW514V6_xuhhj8qeuO-JWliyFnIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
امشب چه تیمی می‌درخشه؟
⚽
کدوم بازی گل‌دار می‌شه؟
📊
کدوم تیم ارزش اعتماد بیشتری داره؟
ما بازی‌ها رو قبل از شروع، با آمار و تحلیل بررسی می‌کنیم؛ نه با شانس و حدس!
📌
برای دنبال‌کردن تحلیل‌های روزانه فوتبال عضو شو:
🔗
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70306" target="_blank">📅 02:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70302">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c25635056.mp4?token=gZvCZiGv2xWNauEWFVNV7xvC-sSVgBEmTzJuIO8zOYpTusvC0koGqzrLlbOktao3TdJj3v_qqus9iWeOn8U5MfsKXz3rXcTbOXEJZwanHPiPaavvXCPR17DpZ-GQOtHp4Mlnq8fwLjKiuOXfsaC86A8Q6R_Asj4cZebOr6rbFlc4yu-DmNXI9CBolx4WlCepp4PhVcn43LAq3ogtO_ik2akixCQmc4Uczd8WTZXETC4jV2RDIgnsoR5dCTN3V6QcWUmNb4BcvpkWpWrOjDMl86YlFhRJ0wHqd-DyeKK0Bk3KuxrruWaNrMZS8ExUsgXbXgafxkVb-SWhNi996Siphw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c25635056.mp4?token=gZvCZiGv2xWNauEWFVNV7xvC-sSVgBEmTzJuIO8zOYpTusvC0koGqzrLlbOktao3TdJj3v_qqus9iWeOn8U5MfsKXz3rXcTbOXEJZwanHPiPaavvXCPR17DpZ-GQOtHp4Mlnq8fwLjKiuOXfsaC86A8Q6R_Asj4cZebOr6rbFlc4yu-DmNXI9CBolx4WlCepp4PhVcn43LAq3ogtO_ik2akixCQmc4Uczd8WTZXETC4jV2RDIgnsoR5dCTN3V6QcWUmNb4BcvpkWpWrOjDMl86YlFhRJ0wHqd-DyeKK0Bk3KuxrruWaNrMZS8ExUsgXbXgafxkVb-SWhNi996Siphw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
حمله موشکی گسترده روسیه علیه کیف در حال انجام است
؛
بیش از ۲۵ موشک، از جمله موشک‌های اسکندر-ام، موشک‌های کره شمالی KN-۲۳ و زیرکون، به سمت کیف شلیک شده‌اند.
هفت بمب‌افکن استراتژیک Tu-۹۵MS و دو بمب‌افکن استراتژیک Tu-۱۶۰ در حال حاضر در هوا هستند و انتظار می‌رود به زودی موشک‌های Kh-۱۰۱ را شلیک کنند. همچنین انتظار می‌رود موشک‌های کروز کالیبر به زودی وارد حریم هوایی اوکراین شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70302" target="_blank">📅 01:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70301">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/443c91ecee.mp4?token=Y6VCPTYEAx4Gna3LEljSZu1EtN71IvmKXLPR_UL3zbFlpDG4bDmU4yM7D6YJ-o-8zDV1ceF8NcdKie2Nm-Dr5bO44RCiJbxkuj2icWbEh8M3tZGUx05u1KiOqo4dyq2wWu9fuBt3-bRO_UbwiSO6ejfM3sFrZK1wjMzShDZs9k5V7Ny6CZbK6utDSoXWTq5pL5Ok_cUR0y1Kb1TcWKxfB9UwoTFtSz8oKpYl0t0Xxqpr9eSOTc_khp_DAr1f3euWibXvyLEuhSMXVzzjpYTNUvj8UBJ_BORwoQp1oUTgzg-9mG_LiwOriKneo-DHTWQEdP4PgSefoaeVjX9IY6EFqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/443c91ecee.mp4?token=Y6VCPTYEAx4Gna3LEljSZu1EtN71IvmKXLPR_UL3zbFlpDG4bDmU4yM7D6YJ-o-8zDV1ceF8NcdKie2Nm-Dr5bO44RCiJbxkuj2icWbEh8M3tZGUx05u1KiOqo4dyq2wWu9fuBt3-bRO_UbwiSO6ejfM3sFrZK1wjMzShDZs9k5V7Ny6CZbK6utDSoXWTq5pL5Ok_cUR0y1Kb1TcWKxfB9UwoTFtSz8oKpYl0t0Xxqpr9eSOTc_khp_DAr1f3euWibXvyLEuhSMXVzzjpYTNUvj8UBJ_BORwoQp1oUTgzg-9mG_LiwOriKneo-DHTWQEdP4PgSefoaeVjX9IY6EFqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
تصاویری از یک سرباز اوکراینی که با استفاده از تیربار MG 3 (ارائه‌شده توسط آلمان)، یک پهپاد تهاجمی روسیِ در حال نزدیک‌شدن را از فاصله‌ای بسیار نزدیک سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70301" target="_blank">📅 01:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70300">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pk94sxpG9vmRhUw43YFy_9rKzQs9ALxk8hvsv9aoz0k5bCGL5-VNmpAFaGBKRlePvQWm0vlWLQ5PRW7-t7YvrOhjqWyj_axSBGOrpj7kP_5NXADZmPKUnCBUhKX0P8xgKiAKySQSlQPvbs_7kvBmCtDsJ8QUBnN88OpObx95xFEkgLAXhqBW76VGPetZ77MYAXWIMUonzQcqot8HAZNt6w5aD4yGvCw3KSLIdGIhmidMYY0HA7kxLgYtar_B855-xFFyGHW04qLH6oqbdx4SDyWx2HoTHiqzLLCYuCFGe5VFEW9iBhX9nTH5m4dUrEni3GVHYkzKzspj9ZOeEEfr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
علی قلهکی:
اگر آمریکا بتواند مسیر جنوبی تنگه هرمز در آب‌های عمان را برای عبور کشتی‌ها آماده و امن کند و انتقال نفت را از این مسیر انجام دهد، اهرم فشار تنگه هرمز تا حد زیادی کم‌اثر خواهد شد.
در این صورت، به گفته قهلکی، آمریکا ممکن است دیگر نیازی به رفع محاصره، لغو تحریم‌ها یا آزادسازی منابع مالی ایران نداشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70300" target="_blank">📅 00:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70299">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYG1PihFAgpbEkUZDkSHXCy6_IBnG-jLIfWjONIRu2ITugZKpoP5HocXFMMlwIIgKSKAE9CdimV8EyCHn3JO632mtvyBTHWkHylmpa0_ir-679DgRyqKFnmizmfhLRXHtCTOEYsXyhhMI44WBCkc7msToqLLCYDXgR_dkZB962D6VDmiPUnl6WiFjqr_G72iTHD2yYeOF1fdYh-WtJiHRg-cDXzhBq7aqqWxm3_gEVm-3vJth0K_s6xUsympLy6jJlNab8fGobwt91dxUPvixG5pBvZi5ZCbqac0mcQK9ZOzY-2Hb-mpfxyo7X4SUn1iMj55RzTjpIW_Wy0rR5XUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
هم قیمت بنزین تا ماه بعد و هم قیمت دلار و ماشین ایرانی رو تا اخر شهریور ماه گفته؛ این کانال تمام پیشبینی ها همراه تاریخ وقوع رو میگه:
👈
مشاهده بدون سانسور</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70299" target="_blank">📅 00:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAVM851hRTtNKmEu3F5OgQMm_vssb4_dwUN2gRC0NUhoukoJzFqZcEnkI5nHnks2bqaDehvmpH1FSTqNsv3JDjGgRCJxPwbc4OExUwdaMQ4Sw7YEFoq8O18hIHjsExSg0huoVJWAEUa9904T9dhyVLd9k15SeckKmTtFy6XNu0zNZeYWFWgh7o9mUEd-THnKVEcz6MDqxM0V7P8Xf8NOv9lakmySCv7fnxedPlTDZd7dRCTs_Qz_4qlAe5iE9vD72OVXlQOaf1plrr1dyWACU2ls6gvqeY9AcAtrIUs7HR-sa91B9UKlF-B1C_bVR8Kh5VbC3CUlv7oD1BuQna_CbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
📰
اکسیوس: ارتش ایالات متحده بی‌سروصدا یک کریدور کشتیرانی در بخش جنوبی تنگه هرمز ایجاد کرده است که به ۱۵ تا ۲۰ نفتکش اجازه می‌دهد هر شب در امتداد سواحل عمان وارد خلیج‌فارس شده و از آن خارج شوند.
مقامات آمریکایی می‌گویند که این عملیات اکنون امکان جابه‌جایی روزانه نزدیک به ۱۰ میلیون بشکه نفت را فراهم کرده است — که تقریباً معادل نیمی از حجم پیش از آغاز جنگ است — و در برخی شب‌ها میزان نفت منتقل‌شده به ۱۵ تا ۲۰ میلیون بشکه می‌رسد.
ایالات متحده هماهنگی‌های لازم را هم برای نفتکش‌های پر (در حال خروج از خلیج فارس) و هم برای شناورهای خالی (در حال ورود برای بارگیری نفت از امارات، بحرین و کویت) انجام می‌دهد. کشتی‌ها در قالب گروه‌های زمان‌بندی‌شده و تحت پوشش هوایی آمریکا حرکت می‌کنند و جنگنده‌ها برای رصد پهپادها و موشک‌های کروز ایران، عملیات پایش را انجام می‌دهند.
نیروهای آمریکایی تاکنون بارها حملات ایران را دفع کرده‌اند؛ از جمله در شامگاه دوشنبه که هشت پهپاد و دو موشک کروز را رهگیری و سرنگون کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70298" target="_blank">📅 00:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5dabd912.mp4?token=nH3piGovQQbdq1BkMnZ_hFuYca-U37Qa4jPr1FBLl6bxxNxlQsc5nPRK-J_q7P-yiU1DetZo6CXI_j1rT_PSiLRUYeVN7_IuOZZTRs3A6r1hhoaf1LmctTfOFw0_ZdZJuMAmPc0BKIJYhHXm5Agm9_aK3WbAj38Jnue_EmrMyV5soAgdhLH_Wdpj95GiSZgGwIv0Vyr68srXbdilFmlL-JGycV-UGNObubYvR6nSwzOyxoIAn6Gm1H-hMLE8Xs5AEX6Jw7RDa0ztHQ3jkSVxM_GN_CR__D_y1Kn7qjPItpKgi3mT-zXwh7NqW7MPJj95RaS2tHmbbvnAAbPJoTSGQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5dabd912.mp4?token=nH3piGovQQbdq1BkMnZ_hFuYca-U37Qa4jPr1FBLl6bxxNxlQsc5nPRK-J_q7P-yiU1DetZo6CXI_j1rT_PSiLRUYeVN7_IuOZZTRs3A6r1hhoaf1LmctTfOFw0_ZdZJuMAmPc0BKIJYhHXm5Agm9_aK3WbAj38Jnue_EmrMyV5soAgdhLH_Wdpj95GiSZgGwIv0Vyr68srXbdilFmlL-JGycV-UGNObubYvR6nSwzOyxoIAn6Gm1H-hMLE8Xs5AEX6Jw7RDa0ztHQ3jkSVxM_GN_CR__D_y1Kn7qjPItpKgi3mT-zXwh7NqW7MPJj95RaS2tHmbbvnAAbPJoTSGQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما مواردی داریم که می‌توانیم ایران را بابت آن‌ها تحریم کنیم. ما تحریم‌های بسیار سخت‌گیرانه‌ای در اختیار داریم و خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70297" target="_blank">📅 23:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf1eb3322.mp4?token=l042_3Qj2yxuIr9kS6K5CLsbETAJhRNLBWYiF7M9GqVUnd3kphhrzCizxuRxKzmfIYvqzzcjh41OB0UVVBYHiV2yq1_0s7mAp-RAB6o_EiuLKMUvxJe3zhNxj7uMpiA248fCrm6n4D7scr7faSqAG5VUHSg8tbho-gJ8DDNKoyGkABgHFW30mp6g6Slaf3M-c4eh3gXfxO-pIO1BvXIsI4ivkDeqbJPKC0GOg-GcKfpE_iWXVt8JPmhlknZVxPzUZJGlye8ewxWBodLCviTo1OiWQFH0_ZvDToLQpunFdDeaOSBwODykk_AkDSE4PQS1JY0Jj0vxjpDWpY7P1sUZ5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf1eb3322.mp4?token=l042_3Qj2yxuIr9kS6K5CLsbETAJhRNLBWYiF7M9GqVUnd3kphhrzCizxuRxKzmfIYvqzzcjh41OB0UVVBYHiV2yq1_0s7mAp-RAB6o_EiuLKMUvxJe3zhNxj7uMpiA248fCrm6n4D7scr7faSqAG5VUHSg8tbho-gJ8DDNKoyGkABgHFW30mp6g6Slaf3M-c4eh3gXfxO-pIO1BvXIsI4ivkDeqbJPKC0GOg-GcKfpE_iWXVt8JPmhlknZVxPzUZJGlye8ewxWBodLCviTo1OiWQFH0_ZvDToLQpunFdDeaOSBwODykk_AkDSE4PQS1JY0Jj0vxjpDWpY7P1sUZ5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سیدمحمد خاتمی:
فرصتی که در تفاهم‌نامه ایجاد شده اگر از دست بدهیم دچار مشکلات عجیب می‌شویم
تفاهم‌نامه نظیر ندارد
بعد از جنگ‌جهانی دوم هیچ سندی که به امضای رئیس جمهور آمریکا رسیده باشد اینقدر امتیاز به طرف مقابل نداده
ما در موضع عزت به این‌ تفاهم‌نامه رسیدیم
دست آقای پزشکیان را می‌بوسم که شجاعانه و فداکارانه این تفاهم‌نامه را امضا کرد
تقدیر می‌کنم از شعام که رای دادند و رهبری که تایید کردند
هر گامی که به سوی رفع جنگ و برداشتن محدودیت برای ایران و باز شدن راه به سوی آینده باشد را باید تایید کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70296" target="_blank">📅 23:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cii6lkYLc8ej4yDEo2Gd7Y0XR2rOfwIFgNV-M2OUQ3Xz2MczY991A8S30EvUEz1_CDQbi7UrQ-2pcP58O3HUaDhH6ZTqJpQsOIu7O1sMl23Y45yqMX87rxMS45A4rbmpuYx-8irabdLTXnymb0W8eMsdYEnisoEmwXL3ykc1DHeWWAXqw1utsXv9npXVp_DsWGhibPhnztEZ9WhILxv2qG1GmNRjzagYAwu-uimMjiMm4cuRGVpud9CqRTnrRu0MlJWxiK4v8cmVEw7H5Bzx5LB1APLm6YETehTJDXFXH_58rf-aeAmbXY1ig3bdQCmWU4IJF-x0j2okenH1ZQZn-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف در جواب ترامپ با کل‌ش تنگه هرمزو بست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70295" target="_blank">📅 22:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44e544df4f.mp4?token=bmerI1IxNj-1CtnFqTD-RnYIeI88InkIni9P33fvNEhGCwZELFWFKI4uc971SryJQbZAA6Jac4Paobak1fhs_f3T8Li-UXsEscyv1kC1jSQcl2OEhN8DZ59Nj2QZBH1nchljL6ZNlOdA0u6KcuZLxkZ3U0yk-Ub8Z1H46Jd78nlu3PcQ6IePKovGXUojI3bdAoxQV3tr5NkTu6AhyihtSAMlQGETlA59GO5TRUvz2ABHgbWIxOpVQJA7wwVvGFLlK4L9U9fIOqVs7JeUs84dcLas7mQCs7iIhtmGwC2VD7ggiwSJJvloPAMxfi5GQiBr6fAMfRbWSX-rXshLuKIZDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44e544df4f.mp4?token=bmerI1IxNj-1CtnFqTD-RnYIeI88InkIni9P33fvNEhGCwZELFWFKI4uc971SryJQbZAA6Jac4Paobak1fhs_f3T8Li-UXsEscyv1kC1jSQcl2OEhN8DZ59Nj2QZBH1nchljL6ZNlOdA0u6KcuZLxkZ3U0yk-Ub8Z1H46Jd78nlu3PcQ6IePKovGXUojI3bdAoxQV3tr5NkTu6AhyihtSAMlQGETlA59GO5TRUvz2ABHgbWIxOpVQJA7wwVvGFLlK4L9U9fIOqVs7JeUs84dcLas7mQCs7iIhtmGwC2VD7ggiwSJJvloPAMxfi5GQiBr6fAMfRbWSX-rXshLuKIZDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
قرار نیست بی‌نقص باشد، اما حجم عظیمی از نفت در حال عرضه است؛ خیلی زیاد.
همه شگفت‌زده‌اند.
🎙
خبرنگار: آیا مذاکرات با ایران را از سر خواهید گرفت؟
🇺🇸
ترامپ:
شاید زمانی این کار را بکنم، اما در حال حاضر وضعیت بسیار خوب است. با این حال، شاید زمانی این اتفاق بیفتد.
🇺🇸
ترامپ در ادامه:
ایران نمی‌تواند سلاح هسته‌ای داشته باشد. می‌دانید چرا؟ چون از آن استفاده خواهند کرد.
ما اجازه نخواهیم داد که از آن استفاده کنند.
مردم در حال یافتن جایگزین‌هایی برای هرمز هستند. شما این جایگزین‌ها را می‌شناسید: تگزاس، آلاسکا، لوئیزیانا.
مردم برای تأمین نفت به ایالات متحده روی می‌آورند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70294" target="_blank">📅 21:55 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f23583ef9.mp4?token=d9he3K8wWj3s6oDz19V8PVv2g_usQSb4Rnga5_p7fgZSqS3WI476OE4r3j6UaRKT0sVJdNRS1RrlFdxbnTDy7NFQwSQWJt_tztI05WHsAvUWC0wVA97rIB1WMR3S5dtlJQT6bstJU5QY-xkDcZzClV8XrfVzAaIK5kMV4fkougNVNIFFEDCPsZZWvt8vF648ExDmQ9_iRZGG5xOwxK-IQme8Kf5y6YrOzu5rSSHWO9tJnl3V0PMvwov49EG59Ag6IkuvnzsL998rvbXTXTqwUWL7iGPKY4gd9LCFtkh5SkGj40kw_9kPmiJPaGpShV_-aw1dsaaZg-OzzjaeKb8Q5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f23583ef9.mp4?token=d9he3K8wWj3s6oDz19V8PVv2g_usQSb4Rnga5_p7fgZSqS3WI476OE4r3j6UaRKT0sVJdNRS1RrlFdxbnTDy7NFQwSQWJt_tztI05WHsAvUWC0wVA97rIB1WMR3S5dtlJQT6bstJU5QY-xkDcZzClV8XrfVzAaIK5kMV4fkougNVNIFFEDCPsZZWvt8vF648ExDmQ9_iRZGG5xOwxK-IQme8Kf5y6YrOzu5rSSHWO9tJnl3V0PMvwov49EG59Ag6IkuvnzsL998rvbXTXTqwUWL7iGPKY4gd9LCFtkh5SkGj40kw_9kPmiJPaGpShV_-aw1dsaaZg-OzzjaeKb8Q5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عبدالملکی، وزیر اسبق کار در دولت سیزدهم:
به عنوان عضو تیم اقتصادی دولت رئیسی می‌گویم گرانی‌ها یک درصد هم به جنگ مربوط نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70293" target="_blank">📅 21:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0460292f9.mp4?token=smeqFkVs5Ws3f68YNBwcNqIEQhsEenMtq6MnNHcKDr1Zf_tECbbYEVReMxg1q0fYQyHoY2OzAvlP9NDn0djFa7YK4sUtl8f_t7rZmTfEtzKgMyiztsNjOLcHTDpNGgiVwbhWF7MCSVbKNsSqb2Ld852_oL8xh7C7CFfoTU4h8jp_x5GexKTOCelaBl5keCRRvBFp9ELKA4ZuGTv3Vx4BwmF1VIzjGafWVDs9FIupSnXliU0YxKl7xiefH8vS_Xa_3NmGKKGlElm13ipFz1ah14Mu4-Z8kU8ny6rAnlFn5OkSIg-1csbo4Gxb5uV0-MLsBAQ9uOND4jxf-hrL15dkOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0460292f9.mp4?token=smeqFkVs5Ws3f68YNBwcNqIEQhsEenMtq6MnNHcKDr1Zf_tECbbYEVReMxg1q0fYQyHoY2OzAvlP9NDn0djFa7YK4sUtl8f_t7rZmTfEtzKgMyiztsNjOLcHTDpNGgiVwbhWF7MCSVbKNsSqb2Ld852_oL8xh7C7CFfoTU4h8jp_x5GexKTOCelaBl5keCRRvBFp9ELKA4ZuGTv3Vx4BwmF1VIzjGafWVDs9FIupSnXliU0YxKl7xiefH8vS_Xa_3NmGKKGlElm13ipFz1ah14Mu4-Z8kU8ny6rAnlFn5OkSIg-1csbo4Gxb5uV0-MLsBAQ9uOND4jxf-hrL15dkOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بزرگترین هواپیمای برقی جهان برای اولین بار به پرواز درآمد
:
شرکت سوئدی-آمریکایی Heart Aerospace با موفقیت هواپیمای X1، یک هواپیمای تمام برقی با طول بال 32 متر و وزن بیش از 11 تن رو آزمایش کرد.
این پرواز در شهر نیویورک انجام شد، 27 دقیقه طول کشید و به ارتفاع تقریبی 335 متر رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70292" target="_blank">📅 20:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70289">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjDRmKa0Xvk5qrCV6YRZIl5gvkwYAeYCzQcgoXdghmHWWWRWDYiWx4BIa27_bO6b1zn4auGxzYncprZLOfSsYJHCyUSTH3QUXm6xCFg8PIdY9cb6ekAmQ6HWnsQlUV6vzcOclkxEqC09Oi64Ff6qFIY2BBfs1IEUKV9wMBLZx-6OlqzrotEBuOIeQ7cllmIYkDhxRN7Xeu2wMlaIjrLGC6wSBDuEnTmVjUNwpyO9eEjUtzeygzK-Ayg9LEXSsaBnbgNNZzXX10NWw3sRZaxqmnXAQQ8HvTYKbLHwLrm7o88-wd4TFnDhBSlK8puEKtpq9oRPro-g18vtnBgD3PzIlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsXOKrpbkrwnIGDhLgvASMEfCdIjQPu36_njwSuY76fvfJejeT2NCS6SENlqGvHHSC2kkw6o19K8GxsfpogSaNHn1GHLjl2OYaC3tVqBakK3krP3jm0j1-qD5cLRJZ-uWdpXFifeckMgeaSxl3vpbBur_cfwSss7nI8sv0TJT_HPHG-H-VtFR6qHvm5_rFJ58RO3cioqYna8-TW237GaMOKBa6sX5OcgBFadNQPUvCJuT7-Zi5MaixHRU8UQTe3qO2xLToUMiZH3fVfFIxi9At-KptVotxTkyYfNnKmBleQn8AMtXj51L_Zar9EZqAJ_GLhuy0MsveKjgOF2LiZ6Gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f8537b12e.mp4?token=DXdF9cKbd0QYXWKE_7cvVIEy3lKQIWCSHCUPT4zVBiMbd5jHAJviN06KZuojjQ6R1nAj_wAQVLxGce1_n8jAy5s8oLvaJNazg4ns9uw7clXckCZ_o58p5o1Shq-dhQ8lX5LOcPPKzu970HKjrksuTLGQ5HgVCm27WxC9HrywLoprLBSFgg9smR4k2ODi_92Upz-a-o9AqPZkj-Y-NPAhdQ0RUTe7k1RnFGIK0Askz-ClbxqnKw3yMd0cQA51IvYQovTerZOfVQKI_YZKmj7-8RL85Yor2_lGLzuM2efY54IEmIf1EYaU6rMLkzRys10KyA9YpkvrIvtcZhfat_dgZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f8537b12e.mp4?token=DXdF9cKbd0QYXWKE_7cvVIEy3lKQIWCSHCUPT4zVBiMbd5jHAJviN06KZuojjQ6R1nAj_wAQVLxGce1_n8jAy5s8oLvaJNazg4ns9uw7clXckCZ_o58p5o1Shq-dhQ8lX5LOcPPKzu970HKjrksuTLGQ5HgVCm27WxC9HrywLoprLBSFgg9smR4k2ODi_92Upz-a-o9AqPZkj-Y-NPAhdQ0RUTe7k1RnFGIK0Askz-ClbxqnKw3yMd0cQA51IvYQovTerZOfVQKI_YZKmj7-8RL85Yor2_lGLzuM2efY54IEmIf1EYaU6rMLkzRys10KyA9YpkvrIvtcZhfat_dgZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ پسر ایرانی برای سوپرایز کردن دوست دخترش، عکس چشاشو رو گردنش تتو کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70289" target="_blank">📅 19:53 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70288">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322a5e809d.mp4?token=j2YgBF-zsKAZNihws13qTDsZZ4K3PizSWUD6dmFoprdawc8x2bgJtmI2h355KE9ziN1NaqyXSwZy5YbjZqEgtH_IKkmHUEWwXZ8dWgenKLZpqxSK5IkavWMQ6Lyfniaj9C5LkTwl394ihUNsRualYiBV-ukEK6RTGZEcg1rI7JP308leizx4AwG73e4RTg53t4_IInqrmJK8uFFzWTrURB6e9SB3AlgwwugfKCeOX47QYC8MkqUUXkL4rvhrVoeyNsx33cLZICOt3J9M2BHf3UFDsZw0fs7C0V4TmQa9LjYNwZ8dO3iQcsPfsX23OoiNV1MQnhK4oieHgzUvVkwLSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322a5e809d.mp4?token=j2YgBF-zsKAZNihws13qTDsZZ4K3PizSWUD6dmFoprdawc8x2bgJtmI2h355KE9ziN1NaqyXSwZy5YbjZqEgtH_IKkmHUEWwXZ8dWgenKLZpqxSK5IkavWMQ6Lyfniaj9C5LkTwl394ihUNsRualYiBV-ukEK6RTGZEcg1rI7JP308leizx4AwG73e4RTg53t4_IInqrmJK8uFFzWTrURB6e9SB3AlgwwugfKCeOX47QYC8MkqUUXkL4rvhrVoeyNsx33cLZICOt3J9M2BHf3UFDsZw0fs7C0V4TmQa9LjYNwZ8dO3iQcsPfsX23OoiNV1MQnhK4oieHgzUvVkwLSjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ماجرای پیشنهاد قرار گذاشتن از طرف‌ دونالد ترامپ به بازیگر هالیوودی سلماهایک از زبان بازیگر:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70288" target="_blank">📅 19:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70287">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
قالیباف: مقاومت تنها راه پیروزی است و اگر آمادۀ جنگ نباشیم مذاکره هم ثمری نخواهد داشت
؛
از دولت و ملت عراق برای تشییع میلیونی رهبر شهید انقلاب کمال قدردانی را دارم همچنین از میزبانی شایسته ملت و دولت عراق از زائران اربعین حسینی تشکر می‌کنم.
مقصر تمامی مسائل و بحران‌های منطقه آمریکای جنایتکار و دخالت های آنهاست. همچنین غده سرطانی اسرائیل که توسط انگلیس در منطقه ما نهاده شد این خسارت‌ها را به بار آورد.
ملت ایران با مقاومت و وفاداری، با نیروهای نظامی و درایت فرماندهی کل قوا هیمنۀ آمریکا را شکسته و آنها را پشیمان کردند تا جایی که امروز آمریکا که در استیصال به سر می برد، هم با خروج از جنگ دچار بی اعتباری می‌شود و هم با ادامۀ آن ده‌ها مشکل برای خود ایجاد می کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70287" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70286">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/680c5f174f.mp4?token=eRvfQiQ1-dI8b-C28nvMQZRkvNp60Ykti-ouZkNHLYWj6Xu5U5NYkRCMUtiEXw-pn11H_dfBr9yh1kfEwCSUrnkkfGYGmexFL00LMxGgKDhy-F0tO0McJkw3nTt7NcIaRMBzz3WVg4nYNz2WgRNWNF5DsZKQTorjuVUCP1n9NVhG4HqeUy6AlKBoU2Jq2rNCx3H7quK8Yzafu1eLmv-J50vUcqF8Ux6JinGTd3piSkE_fry19A0Ef9rqIWMhIVWoAtvkwEiNJ-Ya0-eoiOXPikEKUu36JF5iUEb05n5lQuxnrcOGj0roym9CuBsEQWEqzJn_XoDxHV3UUjWqxsGuv6TA68kpIrykByTsC2wqut2yjg9z6OY091VSKnyQQftzqmPj032Joc50tQPtqjAkDyxCcj00yuLCfApUrn7taOiy7s7hyJLCtNEe_o10iDVwgF6eQgSKV9P9lPxps-TPTMiVUTERnNxY-SvQH2dWmHB5YW6A1BzsluhWlMCLYdADBOe97zbEApr0_pKr5cgsl7_jEWf9pzMZXAnLEF8UALSO2DNkWIhzH8QZ5xtg2CUBAYVKJfJN4AcvJxmyEFR7Z8YghABL6RAEfICyMDGFaFMUXRO_1mdjL9tF1G48gGgplpBtbd4ZnxNwBTZ48nWr8XZ00U5ofZGOcY4YMEhsdn4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/680c5f174f.mp4?token=eRvfQiQ1-dI8b-C28nvMQZRkvNp60Ykti-ouZkNHLYWj6Xu5U5NYkRCMUtiEXw-pn11H_dfBr9yh1kfEwCSUrnkkfGYGmexFL00LMxGgKDhy-F0tO0McJkw3nTt7NcIaRMBzz3WVg4nYNz2WgRNWNF5DsZKQTorjuVUCP1n9NVhG4HqeUy6AlKBoU2Jq2rNCx3H7quK8Yzafu1eLmv-J50vUcqF8Ux6JinGTd3piSkE_fry19A0Ef9rqIWMhIVWoAtvkwEiNJ-Ya0-eoiOXPikEKUu36JF5iUEb05n5lQuxnrcOGj0roym9CuBsEQWEqzJn_XoDxHV3UUjWqxsGuv6TA68kpIrykByTsC2wqut2yjg9z6OY091VSKnyQQftzqmPj032Joc50tQPtqjAkDyxCcj00yuLCfApUrn7taOiy7s7hyJLCtNEe_o10iDVwgF6eQgSKV9P9lPxps-TPTMiVUTERnNxY-SvQH2dWmHB5YW6A1BzsluhWlMCLYdADBOe97zbEApr0_pKr5cgsl7_jEWf9pzMZXAnLEF8UALSO2DNkWIhzH8QZ5xtg2CUBAYVKJfJN4AcvJxmyEFR7Z8YghABL6RAEfICyMDGFaFMUXRO_1mdjL9tF1G48gGgplpBtbd4ZnxNwBTZ48nWr8XZ00U5ofZGOcY4YMEhsdn4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
چگونگی تولید برق با اورانیوم:
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70286" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70285">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">💎
برداشت بدون محدودیت داره حتی ۱۰ میلیارد تومان هم برنده بشی بدون دردسر برداشت میکنی.
✅
🎁
برای مبالغ بالا ۱۰۰۰۰ دلار بیمه شرطبندی ۳۵٪ داره‌
و مبالغ ۱۰۰۰ دلار بیمه ۱۵٪ داره یعنی در صورت باخت مبالغ به حسابتون‌ دوباره واریز میشه.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/70285" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70284">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari (3).apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/70284" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر WEPARI
😀
😃
😄
😁
🔥
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 120% اولین واریز
‼️
🔥
بونوس برای 4 واریز اول
‼️
⚽️
بونوس ورزشی هر دوشنبه و چهار شنبه
‼️
🎁
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :
Gift
🔥
دانلود مستقیم اپلیکشن اندروید
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
📌
آموزش نصب برای IOS
g28
✔
https://t.me/WePariFarsi</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/70284" target="_blank">📅 18:30 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70283">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇱
نفتالی بنت رقیب نتانیاهو:
باید مطمئن بشیم رژیم ایران قبل سقوط هسته ای نباشه
هرچی در اختیار داشته باشیم از جمله بمب برای فروپاشی آیت الله ها استفاده خواهم کرد
شوروی بدون بمباران سقوط کرد آمریکا فشار آورد و اونا سقوط کردن
رژیم ایران از درون پوسیده و به سقوطش سرعت خواهیم داد
حزب الله یعنی ایران حماس یعنی ایران تروریست یعنی ایران
هر بازوی تروریستی ایران اقدامی در خاک اسرائیل انجام بده جوابش در ایرانه
اقدامات موثری انجام خواهم داد
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70283" target="_blank">📅 18:08 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70282">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65db328cdd.mp4?token=CkeXJNH6IU5Wb5lEUBo_2WFUofqLDn-ynBopDxvZcLuL1iOOIF1S9E9I-0PG1esggr_UodqFhi_t5cYW2rfCxB_rUa42vxpZ9x_b1HtocBnYLNR_1so0Sr-YNGeLiH9DIjOA3nRo5YDuaPo6H7hVD1hNiTm2aGibxhnZZ7FBNnMqbfF-rxOSE2kaBb0BQjf6-VJvSf2BOWBJz98AgSCC035igLtnzwXGsZFA9f1TthlHg_hZOTaAg2NiQ1ca4Z0TO5HTy60wtXjd-ia-Ceeqcfcj6SadwJ8SIU78pLQ_hrGNw5JM8wFw5fegBdInnIY4jFCKq2tWMIbehuc7KySlLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65db328cdd.mp4?token=CkeXJNH6IU5Wb5lEUBo_2WFUofqLDn-ynBopDxvZcLuL1iOOIF1S9E9I-0PG1esggr_UodqFhi_t5cYW2rfCxB_rUa42vxpZ9x_b1HtocBnYLNR_1so0Sr-YNGeLiH9DIjOA3nRo5YDuaPo6H7hVD1hNiTm2aGibxhnZZ7FBNnMqbfF-rxOSE2kaBb0BQjf6-VJvSf2BOWBJz98AgSCC035igLtnzwXGsZFA9f1TthlHg_hZOTaAg2NiQ1ca4Z0TO5HTy60wtXjd-ia-Ceeqcfcj6SadwJ8SIU78pLQ_hrGNw5JM8wFw5fegBdInnIY4jFCKq2tWMIbehuc7KySlLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه نفر می‌خواسته از یه دختر دزدی کنه، وقتی دختره مقاومت کرده این بلا رو سرش آورده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70282" target="_blank">📅 17:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70280">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/e_W4PPQyOwgRQxac_SVVbIvSh1jY3N1mEdF7G48HCYmPDqyRWjdRyIfXf6uFPni6yd4yLdOyCND5qxGul79CBUvZNjSg5VhCkJ3qd3brStZ2dgKEqIGtAChVcIpSmGbKXNbRyXRDTAuM6XEoUYAhEhCc6eQ2JMdvh7raFF6zk0WmL2p_82WzZKXi1samQcgJ6bIQyUiOeRoN0ptCvoXhROIVRavib9hB8guugqnClJPFl7C6iaDI3hT9wfyfUsbQHf9gk_WCyX7n5q_6wQOXD-QdtUhWBvJb-YUpZy4V8m7y3n4T2eI180JnGUV88dDWcL7A7llngJoEaaXpebFOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M6TLBJU4z3Ik-yWgEQPmLOEcOcEMuHxm_SJkZU1yrXaD7qVTS7pF8Xj4jqxu1M4u1NRAV6FTxauEfbIDId1zNbOdA7CQjYDWGKO0veiphc-KMeyAz6itRgJ8n3QzbHbZjNiFdsHIF6zrvM9CyGC2LxxFHe_kFyGbiLk-b-nCO6lp_uLQpgUT7u16i0p3RL70mhgYGN4N3Btp8oiBzPBUDhrKT2OlZ_W6LAnuKwQF3T48BeaJPntMaRwTdPXpXWOfsy6qgQANhMhmyOYMJI6lzXiU35z8ayMPPHbZlx7WRmcA4zbIZMQ6Ahzp3xOXkPe8RYdEdj-vGpDUIiRFPdKh8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
روبرتو کارلوس، اسطوره فوتبال برزیل مسلمان شد و با یه دختر به اسم سهیلا ازدواج کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70280" target="_blank">📅 17:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70279">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0a5de821a.mp4?token=vfPlE3UUUeGrd00C3nh_ADePBN43u18lx-2Mq2RpTzPyxeICkqxcJwn2euHml8QZH0HYCo82h7Z8oU2AGbtgdIDSc4GYQVvO9si2-0FS24LkD8LCZ9j07QKzJdx5T8zV5cJlEK0iSqwLgFJ-Z7YgO3eKumbiAxSYwhUNTFpxi_AuqsCx76aRzBZP7t6vhHu-j4tGcIpF-Zo7S745kzuGxaBnviKMyPWGfImosmJk0p8EreyoZnHhG-LYofcXgDXFJMG5gx5b9_WB79-UhBm0Q9c8xPwIcyFBbgHhH45xlmu5-dZ8kGqwnZLAZnO-mmibQd5amomkfyiYPnjalJIZv2YyZZvfoR3QgLGMUBOL3EC8Z-Tb4GHvwVHAB9hsWvDYq9IuvNUbAsTVSbYn9WiWJzkcRQif8Iaw_-KiRcaXXPAGig1u-2DeK80vZIsC2eLEoNchBrjhywej5leQCMxgDFhXLK6098yCg2s9ndwT3TOUxd7qOQE4WWgeeOg9Dv7VtKYQl_4vYFZQbNR5gscPtXk-KKlKjMq1CbctI4h33eO8C42Ic8jF90DYZWiPMEeAZpXnB-l0zXH_w-qW4WtoTYqGKQ_-PBB-e4t_Q8E6eHDYCkqSFqfYG5N9NK2ty37m8ILtVG0pOlj7tcPRA6j3pWpHfgm19qwNrm3vnHsRInw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0a5de821a.mp4?token=vfPlE3UUUeGrd00C3nh_ADePBN43u18lx-2Mq2RpTzPyxeICkqxcJwn2euHml8QZH0HYCo82h7Z8oU2AGbtgdIDSc4GYQVvO9si2-0FS24LkD8LCZ9j07QKzJdx5T8zV5cJlEK0iSqwLgFJ-Z7YgO3eKumbiAxSYwhUNTFpxi_AuqsCx76aRzBZP7t6vhHu-j4tGcIpF-Zo7S745kzuGxaBnviKMyPWGfImosmJk0p8EreyoZnHhG-LYofcXgDXFJMG5gx5b9_WB79-UhBm0Q9c8xPwIcyFBbgHhH45xlmu5-dZ8kGqwnZLAZnO-mmibQd5amomkfyiYPnjalJIZv2YyZZvfoR3QgLGMUBOL3EC8Z-Tb4GHvwVHAB9hsWvDYq9IuvNUbAsTVSbYn9WiWJzkcRQif8Iaw_-KiRcaXXPAGig1u-2DeK80vZIsC2eLEoNchBrjhywej5leQCMxgDFhXLK6098yCg2s9ndwT3TOUxd7qOQE4WWgeeOg9Dv7VtKYQl_4vYFZQbNR5gscPtXk-KKlKjMq1CbctI4h33eO8C42Ic8jF90DYZWiPMEeAZpXnB-l0zXH_w-qW4WtoTYqGKQ_-PBB-e4t_Q8E6eHDYCkqSFqfYG5N9NK2ty37m8ILtVG0pOlj7tcPRA6j3pWpHfgm19qwNrm3vnHsRInw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو بازار تهران مغازه نیم متری رو 15 میلیارد فروختن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70279" target="_blank">📅 16:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70278">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">⏸
نگاهی به تحلیل زنده‌یاد مانوک خدابخشیان درباره نتانیاهو(حدود ۸سال قبل)؛
از استراتژی‌های اطلاعاتی و ضد‌اطلاعاتی تا نفوذ در عمق برنامه هسته‌ای جمهوری اسلامی و دسترسی به اطلاعاتی که قرار بود محرمانه بمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70278" target="_blank">📅 16:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70277">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvc7xqZN5babCXHNyu-atWU_T3wkZLj5yfdcYXtKo_jrm3-sH4uEpKfv5Y5auEmJL6jL7CT9p15F6479uQMy7YTNytC5lA2zoS7Y8IwsVwEEUzzBcsHaWGWBxpkwCLSGpLRPtZPURdNRwaUoTmyFddCO_1T4Xh-FuJpcJSgoufoDEZNopFzGgDiJZGpgg6Z9XdyRVXGHfBW2wu8PMlChyLjmkocJxpB1AaQNW6YZfRtacU4ciASMjI2h46NUZf-n9hfpz8MXv-4tabJCuqBXj2FteA43o-zZFujltiOX78DKJqXgbBg_OgMv5eNQte82cp7y7gNHz9nFYQ3xx2AteQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
یاسر جبرائیلی:
کرمان، عملیات فریب بود.
بنزین: فعلا ۳۰ هزار تومان!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70277" target="_blank">📅 15:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70276">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029120d212.mp4?token=WhIbZHNJ_ydBKHRlbsegW3dTBAay4PHN2TqxRdhAwXBVjbukRCgnjAQKyecpKZxcu0pKJPCaGheLNy4e9lpv4nfEcqS35j76fuvY7lkSJubXS0Og759qtYaqASFIZPNE9ELgfDJ0TsKnh_0Pdu1c_bz1rPfoHPIrcfAGW1d7qaVus6modOTjuctXx1nc6AkEDGzxUz9JYLbn4W6X7a-E3e31FT89GRfIZUhYTI-j80ocJUhTQnCpVLSmCblppSBeRb2iCWXdH3m-ZH3E8guH9DkYF1kG74Xu1lNdF35gWk49sEIvN-2e4ADFKfEhzfR2oAyoX-CqUTZ6kyZtWPk_c5q4wNzA9gvm9belyLJqGzeHce_AeMRYu26iZqNEZzYIgIHZ0NYh77TkKnJBa90qpnqFgmOW6Y6gk4VtyTO_VhBuJqo-EUT0-fD6-wae62W1Oy3uVwiP86qIhriwDaIBywWMIq51PDgtbsWpeROqtMxwBSumUO-wvx0rQDOGdCyb3PFDkF7Dkt-tbrO1CrFKlu1tCrvb9Qo2JAvUjrsx1OvAOUIrpM2wDs0un8sRSfMubVA6Pe4urFSaaui6MV-q---bq2ykNzcg9-qso-B5_QxDdOsglNB3Z_Z-lvZZpTn2RapnrORkygwyWIuEasjcX6Bp35zW9FUCN7hAmDSxm3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029120d212.mp4?token=WhIbZHNJ_ydBKHRlbsegW3dTBAay4PHN2TqxRdhAwXBVjbukRCgnjAQKyecpKZxcu0pKJPCaGheLNy4e9lpv4nfEcqS35j76fuvY7lkSJubXS0Og759qtYaqASFIZPNE9ELgfDJ0TsKnh_0Pdu1c_bz1rPfoHPIrcfAGW1d7qaVus6modOTjuctXx1nc6AkEDGzxUz9JYLbn4W6X7a-E3e31FT89GRfIZUhYTI-j80ocJUhTQnCpVLSmCblppSBeRb2iCWXdH3m-ZH3E8guH9DkYF1kG74Xu1lNdF35gWk49sEIvN-2e4ADFKfEhzfR2oAyoX-CqUTZ6kyZtWPk_c5q4wNzA9gvm9belyLJqGzeHce_AeMRYu26iZqNEZzYIgIHZ0NYh77TkKnJBa90qpnqFgmOW6Y6gk4VtyTO_VhBuJqo-EUT0-fD6-wae62W1Oy3uVwiP86qIhriwDaIBywWMIq51PDgtbsWpeROqtMxwBSumUO-wvx0rQDOGdCyb3PFDkF7Dkt-tbrO1CrFKlu1tCrvb9Qo2JAvUjrsx1OvAOUIrpM2wDs0un8sRSfMubVA6Pe4urFSaaui6MV-q---bq2ykNzcg9-qso-B5_QxDdOsglNB3Z_Z-lvZZpTn2RapnrORkygwyWIuEasjcX6Bp35zW9FUCN7hAmDSxm3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش تو یکی از محله‌های تهران یکی از هموطنامون یادش میره که آیفون خونشو درست بزاره سرجاش و الان یه محل بخاطر این حواس پرتیش خواب از سرشون پریده:
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70276" target="_blank">📅 15:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70275">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6a9c2f6f7.mp4?token=JpK1idhnQg5O3yV7qLAHvFWvIaC0V7Ya1tV3MCg-mqteQE-7qrUSyv_FL8tOLlF1Wflrzq22mFSuU3P4UQmzCPBDbfub2ExOLrkm090KkcIQQzYyLUtgTgWlFGKM7vOHMQIY-5U17WS8mARdjK11GmIGUss1bhvI-X8GUvKijnIZqhO8UCM0kcMbcUALiQY0DcIxyIvFYczuKx3oyDGAF-9ATDAmOfnDjLyS6lDPSuze1woHHZymC1wc2TIN_E9lvTDjjuLCXq7ylUu-USV75B0uAZoWyJd3jTBL6Yku876-ua1kzn8fU3VoRFNT6BfxltXHrgT3qV7MZ6fX__lWGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6a9c2f6f7.mp4?token=JpK1idhnQg5O3yV7qLAHvFWvIaC0V7Ya1tV3MCg-mqteQE-7qrUSyv_FL8tOLlF1Wflrzq22mFSuU3P4UQmzCPBDbfub2ExOLrkm090KkcIQQzYyLUtgTgWlFGKM7vOHMQIY-5U17WS8mARdjK11GmIGUss1bhvI-X8GUvKijnIZqhO8UCM0kcMbcUALiQY0DcIxyIvFYczuKx3oyDGAF-9ATDAmOfnDjLyS6lDPSuze1woHHZymC1wc2TIN_E9lvTDjjuLCXq7ylUu-USV75B0uAZoWyJd3jTBL6Yku876-ua1kzn8fU3VoRFNT6BfxltXHrgT3qV7MZ6fX__lWGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
واکنش سرهنگ سعید راستی به ویدیویی که از او در اعتراضات دی‌ماه منتشر شد:
تو جمهوری اسلامی اگه دیدید دارن یکی رو می‌زنن و تخریبش می‌کنن، بدونید اون طرف کارشو درست انجام داده؛
تو 32 سال گذشته کار من فقط مبارزه با ارازل و اوباش بوده و غیر ازاین نبوده.
تو فضای مجازی اومدن با استفاده از هوش مصنوعی یه کلیپ از من ساختن که توش با مردم درگیر هستم؛ در حالی که اون کلیپ اصلاً مربوط به من نیست و سر من رو با سر یه شخص دیگه جابه‌جا کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70275" target="_blank">📅 14:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70271">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c3bSSTgzWphBhRaGmwK4OgOnuDivxpg5q9szALHWC5xTuQvDvqKq02DovqIAr8-sRI_2wDmlQ2dvbs0urKSZHU59RP38Kjf6-lolPlK04i34a3qygqdUbPGy8BI4mpEebzvZd4QxR05mPkm1BrGpHWf4s2uYNus8gvbZznNu7v_1GSwCCv97mqrDWEbMpUF2iwf9sztpue28RYgTnYyOrH2ifj_mDkWdl2VrQ5WPnB5L9ZsNt8xi_iI9YqFdBI1oQh7V18wyf2j8jig8brpYS8vaPUWrNoBT5K58Tspt8GT43TSuWGD9Mt51UAIoEUfgTipWfEnwFuaJnfeDM7BCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICp19H8xhIsvxgXsw37_wmhqaeQIgWB2SVbjScm8_utSv7ZTCOOy0Ok-IXtT3Ns6G1qRxpmQh-afz3tNT4ZX1n5DdojnYt79qhAhxLHSDB9qOp-puUyrl_rTpQXM1UuF2RoCU0Bc5Yg122tJVEYoTFdbAoGiVkS9O2kkyXxZYxyZoaG-1gZ4wt38e0yqa6pTSScTMDoVDyJ1TsFGLvgTFcoNYBCW7pGW0jU9PjU6rvrxmso4LfwDW8EhjvZ9zm3zvgPDuGD5s_s-scg0oi390CP3WYJBK8JYYwoUcfjH4OUw8o8Z_rixUe0NrYQZX8AAdsn1TZAketez_VYJK43p2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fc313b331.mp4?token=WiLKeWmNIbqHlImWKhyWLWk7ilEzbCMUezWrF4PpS79h7QAmyEgPlj8udxTuqJ_dfy0P-P4RJhT3Rb5b9BBDX02GfJOP_27tbX394vKqQNWsUu-6DJzZ_0vJF0GzG_HLRj3Nmv9NAGdxPYx9Vki5mX6EXt_Twok5ti-KMDz0ROkNvA-dmRshhe9CapFjpdbbjJZ3HfD_GMekkX2ELuAbjeLPEF_3InMZJkud04xfgsKQJk0worhAbM5oq5H-0dK5v8WLj-1Q-CF83OaRGawD3NPHKKa15Yr5ooRlIsAK9T21Oq0gZTb8xJMjvyhLOOn9yuY8qIfpg2HxIjVEE-cNDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fc313b331.mp4?token=WiLKeWmNIbqHlImWKhyWLWk7ilEzbCMUezWrF4PpS79h7QAmyEgPlj8udxTuqJ_dfy0P-P4RJhT3Rb5b9BBDX02GfJOP_27tbX394vKqQNWsUu-6DJzZ_0vJF0GzG_HLRj3Nmv9NAGdxPYx9Vki5mX6EXt_Twok5ti-KMDz0ROkNvA-dmRshhe9CapFjpdbbjJZ3HfD_GMekkX2ELuAbjeLPEF_3InMZJkud04xfgsKQJk0worhAbM5oq5H-0dK5v8WLj-1Q-CF83OaRGawD3NPHKKa15Yr5ooRlIsAK9T21Oq0gZTb8xJMjvyhLOOn9yuY8qIfpg2HxIjVEE-cNDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
امروز تولد جاویدنام مهرداد مشتاقی 27ساله‌ از اراک دانشجوی رشته معماری بود.
رتبه 200 کنکور سراسری
مهرداد 19دی تو اعتراضات اراک با گلوله جنگی از ناحیه سر مجروح و به بیمارستان منتقل میشه تو بیمارستان عمل میشه ولی به‌ دلیل مرگ مغزی جونشو از دست میده.
روحش شاد و یادش گرامی
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70271" target="_blank">📅 13:50 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70270">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHQo9k0OuAApm4ftkuJPlnpLHvKwRG08y9qn8Nf2D_J5LwUddM7Pul5XPcEYLrMw0l01F46AUXr7Lvw_NxanxwwKc1rq-kXLlgcfe_yDiXjDTkhLlN-NXR2pneYReDWUJVi_db80mrRgulPdM3_4xNDYMrfWOaEQreuUV1jFFYYJzp38csKNGFZx5yUXo0b7j0Ko-KIKlviYoP0CgCnBDStTiTwqrZWyznruvCDqtmjLO1NFq9P1WbVhfkcN6UpNMrPZPNYz_3ctiYM3EFGxefdOS2z0NJI_bMrna0JPu6WdR36atOxFGeJVPVk9rYN9DebzyxofZV2cjtj0ns8usg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استوری جدید رضا علیپور : جنوب لبنان که چیزی نیست تمام دنیا فدای یک وجب از خاک ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70270" target="_blank">📅 13:17 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70269">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuRAOSD2Y_D2euihxh12v6dr__5A8gjlXv73T4tknwhm0IpchwpMnp3upIrZYmV7r4m2Ldkr1FL-qbnLw0LpwFO47tCscBmLfSbNBPOQFdYvGCkMyyjXl2SX3xuC8GSd8Qab14uYS4PjBx7yp7DdDq-RZsNMYlk7bWMgfax7u2M3WhdaEOxksStGW1qwfoVaUokRWJbmP1NE0fGeudpii6tRVRH5sU-Hc_3P9r-DKuKfqoID-C0GWCY-mj_H5v6y_WrYa_KeFpe1UWlf9H4NOC7CXRuq8p5k8rMcNJCVk8yghimCLIQZulCoicbmd2nwvkDxEbFN1VTgZVA-54dHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فایشنال تایمز:
ایران در صورت تشدید جنگ از سوی واشنگتن، حمله به تأسیسات نظامی آمریکا در اروپا را مد نظر دارد.
اهداف احتمالی شامل پایگاه‌هایی در بلغارستان و قبرس و همچنین کابل‌های زیردریایی در تنگه هرمز است.
مقامات ایرانی به‌طور فزاینده‌ای وقوع درگیری مجدد را اجتناب‌ناپذیر می‌دانند و هشدار می‌دهند که حمله به زیرساخت‌های حیاتی ایران می‌تواند دامنه جنگ را به فراتر از خاورمیانه بکشاند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70269" target="_blank">📅 12:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70268">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=jjZT5bO79WOCDCO2YZLgY5oSyPdPeyJ3xwcjdIaouwHfUGHciaMCaZq7LDWoOAIWqZYgaykEjWJJzyO31l-OWdo8sXpnGMUbgF6xvdfG6pKiKLOjpnYqobU4RX1pi5dr0hEsiLxhKPqcADhY3HYGevhyo41klGiwFYlwMJSA-849a7Gf2ICglBuoY4uPJqzAYsov8L7FeNOIdjzKvBmpG5SiCzgF_yLsTN-ogZQnkNcQ8qIj-lEJJ4qZ2JJfXk3Z1awkoXoAppX0cOvwpAbGvPXAGZbG7oiCSdqf39Oz8sQ7MW-j2vDirIi40QXJANUJn1BJ1AOs-Oj-0BndHLeXPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bfbcb6f8.mp4?token=jjZT5bO79WOCDCO2YZLgY5oSyPdPeyJ3xwcjdIaouwHfUGHciaMCaZq7LDWoOAIWqZYgaykEjWJJzyO31l-OWdo8sXpnGMUbgF6xvdfG6pKiKLOjpnYqobU4RX1pi5dr0hEsiLxhKPqcADhY3HYGevhyo41klGiwFYlwMJSA-849a7Gf2ICglBuoY4uPJqzAYsov8L7FeNOIdjzKvBmpG5SiCzgF_yLsTN-ogZQnkNcQ8qIj-lEJJ4qZ2JJfXk3Z1awkoXoAppX0cOvwpAbGvPXAGZbG7oiCSdqf39Oz8sQ7MW-j2vDirIi40QXJANUJn1BJ1AOs-Oj-0BndHLeXPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جنسیس مدل 2013 در امارات: ۵۰۰ میلیون تومن
ارزان‌تر از پراید در ایران...
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70268" target="_blank">📅 12:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70267">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70267" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70267" target="_blank">📅 12:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70266">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Czl4Cg0l4sLXA3p54RELYWoptLk_Inaa8q_GwnK3_uClfkTkX56LFDFo4Tjv9HoYSFjpDHMFdtXGgKwauJ3heBaITvAsI7c75qVnijdjeWxjsapCn48_4TKGC5d4XQSt1bQZ_oz8Tr6C02v-hIxOqBlE-eXePSp4Wp3FhCtgCSH1HkGi6WgDMuK59-8PtZhC5rvC_93c4oGcr1xYE-OPR47k_SvwoAFd2TD0wSqo2TCP5WRmcthWkPjxujx2wi9NA3AhuL4ZijhltkmyQd56KYDaI-GEzyG4ZQw9cZhQLmfy6dbBhTjoQcH1sKXQbXD29WjJ9SiS_N2HAiiCNJqAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r28
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70266" target="_blank">📅 12:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70264">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/daabc799fd.mp4?token=ZoTu6thWUMgRZxMRaTYe2A6zjuuaJwQu3uY4Zpa9JgR_QoPPdZyN0BQr85PqI3hDrL4Pj2EkoaU-PJkKba4nDx3mdIPSyoeivInOE1Ep2GwoHgcaGi54CDq5gOEOofKnyFpoY5PhAJtVViaUOsCa1xWGub-bfxAUKdV9ERGrIIkgxc_A3KXT_otuSsRvYuyyoTMUUwAJw65jHsBY0IAwQB_uWii0DJNFPf82HyMRP4OCHFyggx5IsQF7iJAp2oaQDj_Yy3ubkKsv3DOAhxNfa7s4tAK1PFNd1EZezE_MWe2kCEgmepsKTmXPrDIo0Nw0PEtqx5xN7wPnNTt3BE5rNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/daabc799fd.mp4?token=ZoTu6thWUMgRZxMRaTYe2A6zjuuaJwQu3uY4Zpa9JgR_QoPPdZyN0BQr85PqI3hDrL4Pj2EkoaU-PJkKba4nDx3mdIPSyoeivInOE1Ep2GwoHgcaGi54CDq5gOEOofKnyFpoY5PhAJtVViaUOsCa1xWGub-bfxAUKdV9ERGrIIkgxc_A3KXT_otuSsRvYuyyoTMUUwAJw65jHsBY0IAwQB_uWii0DJNFPf82HyMRP4OCHFyggx5IsQF7iJAp2oaQDj_Yy3ubkKsv3DOAhxNfa7s4tAK1PFNd1EZezE_MWe2kCEgmepsKTmXPrDIo0Nw0PEtqx5xN7wPnNTt3BE5rNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی وایرال شده از بازار پروانه تهران:
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70264" target="_blank">📅 12:01 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70263">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6847afc8b4.mp4?token=aMVb8Xr8GjhjZGQmebah2rG79b66Ky5GhsG2i-SilGie4n_NCDSRa1xKdiLWC4m6413R6vjKD2XpngTtzc69QmJ2gXKOfBspkbldOkbms7PpOVYEKttB0ZmqUr0ByClX44FtPRbDFAXa2aGtXToBndiZg-zHnvYvSXEjbB9niYJKzZLtWI21FHMN-5D9DJ9U9x6Ei3fuqiz-zFSZLtopAwViS4LMcDyWKusoIw5wiPEnJVT2C7HY455N4SwqjbYIexnTkJpmgfIVhuEvUrOUe1b5DEEEsUxOIx7GhdQexVAxwZv3Fg4YsoiQnTgYTJ9Qwa8JNa1YLVDhzYJvcbopkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6847afc8b4.mp4?token=aMVb8Xr8GjhjZGQmebah2rG79b66Ky5GhsG2i-SilGie4n_NCDSRa1xKdiLWC4m6413R6vjKD2XpngTtzc69QmJ2gXKOfBspkbldOkbms7PpOVYEKttB0ZmqUr0ByClX44FtPRbDFAXa2aGtXToBndiZg-zHnvYvSXEjbB9niYJKzZLtWI21FHMN-5D9DJ9U9x6Ei3fuqiz-zFSZLtopAwViS4LMcDyWKusoIw5wiPEnJVT2C7HY455N4SwqjbYIexnTkJpmgfIVhuEvUrOUe1b5DEEEsUxOIx7GhdQexVAxwZv3Fg4YsoiQnTgYTJ9Qwa8JNa1YLVDhzYJvcbopkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن‌ رضایی:
محاصره دریایی ادامه پیدا کند از NPT خارج می‌شویم.
خودتان میدانید این یعنی چه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70263" target="_blank">📅 11:27 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee9c1ee83.mp4?token=VZtzcf-WDjlj-3Vf9tW3jMAoth0vWzTbDGUqkr548uu1I_P01L7zHlfmaqmSxQu5m-ldtuAPWaiikU3qCoWmkIaC4sdkLzjn1gT_WxQzj1t6WrKKb7aCzNWXfNtTt7ZG95hZx0IVIvO662aPNVcM-YgbAQ6xpehFjj5jnB6V26u3IVXUAk8UXyf462m1_5Lv5KoF_XpW8tc45AVL3xjAIzRN04xkJWuYeNdaYuE9g66ZvJJkQK1tGsw44pyGxqDHhRO7X3IF4nPlq1raV2dbYephbfqnVs5ukn5aV4_-epRgD4oxV30wdcDAKcrS28C8K_tgXikIfLcmZz7FEIShPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee9c1ee83.mp4?token=VZtzcf-WDjlj-3Vf9tW3jMAoth0vWzTbDGUqkr548uu1I_P01L7zHlfmaqmSxQu5m-ldtuAPWaiikU3qCoWmkIaC4sdkLzjn1gT_WxQzj1t6WrKKb7aCzNWXfNtTt7ZG95hZx0IVIvO662aPNVcM-YgbAQ6xpehFjj5jnB6V26u3IVXUAk8UXyf462m1_5Lv5KoF_XpW8tc45AVL3xjAIzRN04xkJWuYeNdaYuE9g66ZvJJkQK1tGsw44pyGxqDHhRO7X3IF4nPlq1raV2dbYephbfqnVs5ukn5aV4_-epRgD4oxV30wdcDAKcrS28C8K_tgXikIfLcmZz7FEIShPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
جدیداً تو روسیه گزارش‌هایی منتشر شده که بعضی از دخترها به‌صورت گروهی دنبال پسرها می‌افتن تا حتی برای یک شب هم که شده باهاشون وارد رابطه بشن!
گفته میشه؛ بیشتر این دخترها از قشر مرفه جامعه‌ان و اگه از پسری خوششون بیاد، حتی ممکنه چندنفری با یک پسر وارد رابطه بشن!
تا الان چند مورد آزار و سوءاستفاده جنسی از مردان توسط زنان هم به پلیس روسیه گزارش شده.
ظاهراً پسرهای بااصالت روس و همین‌طور خارجی‌ها، مخصوصاً آسیایی‌ها، بین بعضی از زنان ثروتمند روس طرفدار زیادی دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70260" target="_blank">📅 11:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00c416662f.mp4?token=hTSK91ALAif097IxCQ2sHt6L5z0liFMlx6OrNGZHKUviXv0nLdPupewsmxQxG9qwDGuUwyDrIYtVt0ds1KIXLLHdG2wJ-XFysFYnw6bxoe2yqmIbL9iIFBpkO_vOsE9CABxqiDwBPq7brkvlcomOTIeU4bjEC78GdCJb9tcQD5PUBK0fGrKcmICHfdAxvXM5IPLeOCrU5NO9tgJLUP0nRY8PBygE1-fnMA0qku1iqMZRpfrG0_YIgMqgMUHqVj3LxBuHCbUsL1MBSzH-uG6EfmToeKLiG5h-Do-Pmp2RYjIBAoj8LeyLwvlM0idhWLovheW5rcQhMd1rzE-a9qBi6Jh8nq5I2ogdPRGPoXXFzaR3FRoUdTTB7ApHtG0Vdhkwq3aEMSQNmI_eGNovVGYLRidlDTp471FeMYEaWhdtqjnC_sgK5ZiliUlpffTwm86REg8EEYC5N_3NoSm1L0QM3reTdRVo246VgebhCCILBAUxGXOmUzdsoT4yl1mqKzV6olJ2DYuhamca4I5FTnEGKzvTJUBF2-KuFkzxa1lT35QPojY6vwk3Z5p5ZXH92SpZxbDsseMMCJgvYAFbWrRGdI5d1M9lCbwZcG6YljdJUaNARz3NrInPVrPMQ46AXmpnaCThRZXnD4GtHQFhNWZvjmIbmGMnwUzweDXpA0uaLTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00c416662f.mp4?token=hTSK91ALAif097IxCQ2sHt6L5z0liFMlx6OrNGZHKUviXv0nLdPupewsmxQxG9qwDGuUwyDrIYtVt0ds1KIXLLHdG2wJ-XFysFYnw6bxoe2yqmIbL9iIFBpkO_vOsE9CABxqiDwBPq7brkvlcomOTIeU4bjEC78GdCJb9tcQD5PUBK0fGrKcmICHfdAxvXM5IPLeOCrU5NO9tgJLUP0nRY8PBygE1-fnMA0qku1iqMZRpfrG0_YIgMqgMUHqVj3LxBuHCbUsL1MBSzH-uG6EfmToeKLiG5h-Do-Pmp2RYjIBAoj8LeyLwvlM0idhWLovheW5rcQhMd1rzE-a9qBi6Jh8nq5I2ogdPRGPoXXFzaR3FRoUdTTB7ApHtG0Vdhkwq3aEMSQNmI_eGNovVGYLRidlDTp471FeMYEaWhdtqjnC_sgK5ZiliUlpffTwm86REg8EEYC5N_3NoSm1L0QM3reTdRVo246VgebhCCILBAUxGXOmUzdsoT4yl1mqKzV6olJ2DYuhamca4I5FTnEGKzvTJUBF2-KuFkzxa1lT35QPojY6vwk3Z5p5ZXH92SpZxbDsseMMCJgvYAFbWrRGdI5d1M9lCbwZcG6YljdJUaNARz3NrInPVrPMQ46AXmpnaCThRZXnD4GtHQFhNWZvjmIbmGMnwUzweDXpA0uaLTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیو وایرال شده از کسی که کره‌خر خونگی داره!
به گفته صاحابش این خر گرون ترین پنیر رو میخوره که کیلویی 100 میلیون تومنه!
حتی برای خرش موزیک میزاره
خرش رو هم مث بچه ها پوشک میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70259" target="_blank">📅 10:34 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">⚠️
امام جمعه حاجی آباد بندرعباس به خاطر افشاگری علیه مسئولین شهر به دادگاه کشیده شده و اون رو مجبور به عذرخواهی کردن
حالا اومده عذرخواهی کرده
این نوع عذرخواهی جالبه:
من از بانک های رباخوار و از قاضی ظالم  مسولین بی کفایت عذرخواهی می کنم
من از روحانیون ساکت که منفعت خود را مصلحت اسلام می دانند عذر می خواهم
ما گوسفندان از گرگ های درنده عذر می خواهیم اگر گوشتی به تن نداریم
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70258" target="_blank">📅 09:57 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbcd685b37.mp4?token=gYaacj8Tu_JerIt4mqP03-l16TIFN1LqoBu5d7QTW5wXelixobCSQzX2SEhtXE8ZPBxSxyjxlmxJz83W3tTXYnjQoA5ZTYI6rJ0WK0zmR7pK-xB3JdtDtEPCXCMpll9LCx-FJ-Fed3HcS-ZU_ivUehZRC02SmeaN1hDAGSzEBqAiDcVgLZxe3-9INyqkbx6IuyQdj91hgYIrY3JFMkCayVbZX2qWCP7jnlAtBanNeltcemaM81XYSL1Yhi0hq3lXiXVNst_AH8cxkRAHjQtICFV3oSTENEK923pzFFYRtIgqW0On2XOzIkiFGM_Z9Z_Jf9uff3ruza9ysVB0k87EWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbcd685b37.mp4?token=gYaacj8Tu_JerIt4mqP03-l16TIFN1LqoBu5d7QTW5wXelixobCSQzX2SEhtXE8ZPBxSxyjxlmxJz83W3tTXYnjQoA5ZTYI6rJ0WK0zmR7pK-xB3JdtDtEPCXCMpll9LCx-FJ-Fed3HcS-ZU_ivUehZRC02SmeaN1hDAGSzEBqAiDcVgLZxe3-9INyqkbx6IuyQdj91hgYIrY3JFMkCayVbZX2qWCP7jnlAtBanNeltcemaM81XYSL1Yhi0hq3lXiXVNst_AH8cxkRAHjQtICFV3oSTENEK923pzFFYRtIgqW0On2XOzIkiFGM_Z9Z_Jf9uff3ruza9ysVB0k87EWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
عراقچی :
رابطه ما تو این دوره با کردستان عراق و جمهوری آذربایجان خیلی خوب شده؛
می‌دونید چرا؟ چون پزشکیان هم ترکی بلده هم کردی، زنگ میزنه با زبون خودشون باهاشون چاق سلامتی میکنه، اونا هم خیلی خوششون میاد!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70257" target="_blank">📅 09:31 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70256">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f6a81c93a.mp4?token=qRjNu4-zcY3dHfRKa5SPkHmms7cHnGAQnCa1iFckiOrvtmItVx7hXMqg1WUt8X7J24-sbQrc-1r0vmvH9T29nFQ1Q2ai-RM6gvGT34Fb5gG4qSx6GOkGoHuUilIec53BAEBFybiMVQf5hyb5YGTO82Xh50CUZiUqllIo0Ns0R6YtNDL4U1XI9oHRSqmobMD-1jx2MUBtHL51mc0MHCcSQna8TJ9NlZT2NJqgHfZf9AyTuIzLXMLMIDYew3UA3TwfZEsdcg8modtR1H6CTeuYBIwJgycTvwHCEBVe6imPzRKZDKncPkdn_j5xWuszqehz5iffTYbiuMsnOnVmsmbMLg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f6a81c93a.mp4?token=qRjNu4-zcY3dHfRKa5SPkHmms7cHnGAQnCa1iFckiOrvtmItVx7hXMqg1WUt8X7J24-sbQrc-1r0vmvH9T29nFQ1Q2ai-RM6gvGT34Fb5gG4qSx6GOkGoHuUilIec53BAEBFybiMVQf5hyb5YGTO82Xh50CUZiUqllIo0Ns0R6YtNDL4U1XI9oHRSqmobMD-1jx2MUBtHL51mc0MHCcSQna8TJ9NlZT2NJqgHfZf9AyTuIzLXMLMIDYew3UA3TwfZEsdcg8modtR1H6CTeuYBIwJgycTvwHCEBVe6imPzRKZDKncPkdn_j5xWuszqehz5iffTYbiuMsnOnVmsmbMLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیشب میدان شهرداری گرگان در آتش سوخت و صدها نفر کسب و کارشون آتیش گرفت و نابود شد!
حالا دلیل اینکه آتش نشانی دیر رسید به محل چی بود؟ بخاطر موکب‌ها و تجمعات شبانه تو ترافیک گیر کردن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70256" target="_blank">📅 09:02 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70255">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">⚽️
فوتبال فقط ۹۰ دقیقه دویدن توی زمین نیست!  پشت هر گل، یک تفکر تاکتیکی و پشت هر باخت، یک اشتباه پنهان وجود داره!  اگه تو هم عاشق فوتبالی و دوست داری مسابقات رو مثل یک کارشناس حرفه‌ای ببینی، جای تو اینجاست!
👇
🔥
در کانال ما چه خبره؟
✅
تحلیل موشکافانه و تاکتیکی…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70255" target="_blank">📅 02:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70254">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=M4q7UJO1--PciM0zjOZNv6PMII8ZI62naMckYkoK6vQtQrqf4C94SvgTI3DA6cQIEWVvRlHG5qNz_NalbC-IdGkNukeXpxcRIrPXHQLBWlipUB4hGKUTtS3adGyPkIOILWoR9AOZ1Q1EQBqCHl3_Z0o4Apvr6Npt5BO2tUSSUIvH2HiXJnbbGNsXGC9ikUuhpHF2rNL0XniWG7HRknbAAm1MbnbV0Am08tp0NDlVHhYjPdXsWsefB_NQvShuYQR7vQLurwNZlFJbYAdih6fIZscQ3vOqwa3gjMHdzXviVkRLtf-V20Xgkhxwa6Ba5f0nWArWMTvXb3307RyYKpvWmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=M4q7UJO1--PciM0zjOZNv6PMII8ZI62naMckYkoK6vQtQrqf4C94SvgTI3DA6cQIEWVvRlHG5qNz_NalbC-IdGkNukeXpxcRIrPXHQLBWlipUB4hGKUTtS3adGyPkIOILWoR9AOZ1Q1EQBqCHl3_Z0o4Apvr6Npt5BO2tUSSUIvH2HiXJnbbGNsXGC9ikUuhpHF2rNL0XniWG7HRknbAAm1MbnbV0Am08tp0NDlVHhYjPdXsWsefB_NQvShuYQR7vQLurwNZlFJbYAdih6fIZscQ3vOqwa3gjMHdzXviVkRLtf-V20Xgkhxwa6Ba5f0nWArWMTvXb3307RyYKpvWmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
فوتبال فقط ۹۰ دقیقه دویدن توی زمین نیست!
پشت هر گل، یک تفکر تاکتیکی و پشت هر باخت، یک اشتباه پنهان وجود داره!
اگه تو هم عاشق فوتبالی و دوست داری مسابقات رو مثل یک کارشناس حرفه‌ای ببینی، جای تو اینجاست!
👇
🔥
در کانال ما چه خبره؟
✅
تحلیل موشکافانه و تاکتیکی بازی‌های مهم ایران و اروپا
✅
بررسی ترکیب تیم‌ها قبل از شروع مسابقه
✅
پوشش حواشی داغ و اخبار نقل و انتقالات
✅
پیش‌بینی‌ها و فکت‌های جذاب فوتبالی که هیچ‌جا نخوندی!
دیگه فقط بیننده نباش، فوتبال رو عمیق‌تر بفهم!
👁‍🗨
👇
عضویت در کانال:
https://t.me/+nbm7Tb2pz8VjMDlk
https://t.me/+nbm7Tb2pz8VjMDlk</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/70254" target="_blank">📅 02:33 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70253">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmw1ioU8f8T3uEg7IHhw_Q07EGIvfhZSfUyXaH-Rjqq_p31KtOgcz5Bqx1V_l3H-xtMgjgEm4Txl6Jh7fC01Sk-2uwibh2gFew097wuVezrmlIhWhqdW6iTPQL4j6I77WMYSO48FESNiK4A-8M5lTvSfde58bRGIgFwTZamHJP1MINm6t-796J5Vw0MuD5f_TYHxhZgeHdgYc_eCBXGFwGe9AsDTXv9OECtNuq7bHA-8A902-dOo11kN975Vf78RBV6MBq2aOFEXR19O5_gFgDysEj7d-Z3UiIYoCvzZiA79Vt3Z8uZHEotRMXbfsO7ATy2IbPZyXkB3CMMOoq3lUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه خواهر جاوید نام امیرکیادربندسری به خاطر سوگ از دست دادن برادرش نتونست دووم بیاره و دیشب سکته کرد.
روحشان شاد و یادشان گرامی
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/70253" target="_blank">📅 01:39 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70252">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-gcXwuHcamRKlBoj9QAGWOL-8rrrYaDRTe4ELH5QD0V3n1nMWYLZrf77qlySDLoQfWD3rDQD0_hNyaWmxaH2HL_ckFDcX52avnDnWsmCaQAJdVTV1w8QWKi6z5WUhhMtUzVJYGgXf80R329XbrlXkKpwv-Tih5Vajewc7kqBUMU0CeN0BKrtZ-JZ9MJDt8yMwzbkG1tMI2N2SeCKpyLSAVHwM5E-aLXF4QlxH6ghMj6i_p2_9aVoEN_VpflJXDRWo0b6fWhfiQUKpcK2ddixilAFbL6DV72tpRQPr5eeP98pSsOkU7HBpSAWbamFdZRcxOB9RW7PdUstJWZqmYO9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇺🇸
سی‌ان‌ان:
دونالد ترامپ به فرستادگان ارشد خود دستور داده است تا مذاکرات با ایران را متوقف کنند؛ اقدامی که نشان‌دهنده تغییری عمده در راهبرد دولت او در قبال تهران است.
بر این اساس، کاخ سفید دیگر به دنبال «ضربه زدن فوری و شدید به ایران» نیست، بلکه قصد دارد با اعمال فشار مداوم اقتصادی و نظامی، رویکردی بلندمدت را برای «خفه کردن» این کشور در پیش گیرد تا زمانی که ایران شرایط ترامپ را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70252" target="_blank">📅 00:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70250">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6093565f3b.mp4?token=mDz6_ayKfxQyttfYQuLvIwGnLpIchw2hu-bHubCH-6UG0iGWjnbNaHvQ_JvpgYDmxdcebS6HoQRnXsAZgx1ctCcstaQgxgKwhvT0kl70UBECSxZ8riF8gVEqCdkXg0i0NNz2pM1KsGEn934EUX_wjq-5EAxKZ12FLM1a3grWtouILeIwUyHZajp8zLxQsMKaoaH7g--OUDOb5XYArbYrpsWTwpdoJyV0Ge3yRJ9i81R6_ak9NdMRiqLIUnMKXtNIm9vryEAaOn1Tlf7c_IX6-QN1ppn8QZ3UVf1xJ6xliR8lF-gIfUrtME8Di0dFuVcnGprvlU5JrKc6a1hdQ7anPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6093565f3b.mp4?token=mDz6_ayKfxQyttfYQuLvIwGnLpIchw2hu-bHubCH-6UG0iGWjnbNaHvQ_JvpgYDmxdcebS6HoQRnXsAZgx1ctCcstaQgxgKwhvT0kl70UBECSxZ8riF8gVEqCdkXg0i0NNz2pM1KsGEn934EUX_wjq-5EAxKZ12FLM1a3grWtouILeIwUyHZajp8zLxQsMKaoaH7g--OUDOb5XYArbYrpsWTwpdoJyV0Ge3yRJ9i81R6_ak9NdMRiqLIUnMKXtNIm9vryEAaOn1Tlf7c_IX6-QN1ppn8QZ3UVf1xJ6xliR8lF-gIfUrtME8Di0dFuVcnGprvlU5JrKc6a1hdQ7anPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
اسرائیل اسکادران ۱۹۰ بالگردهای آپاچی خود را به‌طور دائم از پایگاه هوایی «رامون» در صحرای نگو به پایگاه «رمات دیوید» در نزدیکی حیفا منتقل کرد و بدین ترتیب حدود ۱۵ فروند بالگرد AH-64A را به شمال انتقال داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70250" target="_blank">📅 23:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70249">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28b668f3c8.mp4?token=Cr1glMiYzHPePM1G0dMHRyPLy0BS0BmUkEtN5iasNgV6ZU6p1lgMnl63l2hjBQOinxE8OpaZQnLqeNedo-SWwHUX9ObxOuKzCmGGVsV34SpCbjgQC41WggsVNbUymXIYLqZzec_XtJrZVyeCUnCLTGPW7ARrEZu--PQKCtAZwzsigq1D3ngGSRERi3r-JGz5L56Y-Hf7wxe8QiHleDwlnXbzErZD3be8L7nNvQ29H8qES09GxfFDtfBijx6Cx9xUiGtr4l-iIRhrAK_4c12FbDdz25unLVcCgC4UM14q5wgIwMtrp7JUSzFQGeDFVIYW99SYPpJEbMW6LOmD6N6wjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28b668f3c8.mp4?token=Cr1glMiYzHPePM1G0dMHRyPLy0BS0BmUkEtN5iasNgV6ZU6p1lgMnl63l2hjBQOinxE8OpaZQnLqeNedo-SWwHUX9ObxOuKzCmGGVsV34SpCbjgQC41WggsVNbUymXIYLqZzec_XtJrZVyeCUnCLTGPW7ARrEZu--PQKCtAZwzsigq1D3ngGSRERi3r-JGz5L56Y-Hf7wxe8QiHleDwlnXbzErZD3be8L7nNvQ29H8qES09GxfFDtfBijx6Cx9xUiGtr4l-iIRhrAK_4c12FbDdz25unLVcCgC4UM14q5wgIwMtrp7JUSzFQGeDFVIYW99SYPpJEbMW6LOmD6N6wjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طرف با قلیون رفته وسط دریا با یه دست داره شنا میکنه و قلیون میکشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/70249" target="_blank">📅 23:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70248">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Djof87exfajGWsUbyRcctYEbWtoeQhptbI-ZtrOA_oSIJRyi_ZL_yJG_7C8ixYw1QNM3hfRNLt9LbrMiTRroNpxPxCypVD1rX9FYBJydJa2XPXeV-W6N7XEUdJvFEFTEb8VlVCIbJ3YIrE-rLcIaHLeP-PY1Ptx5spYt7cQPvN_VBG6e6OIdI32kcOU4wqsNtula0EfEvwkjGgL3YsyhrbfgJYLUSC93NPz-gd6oaVhfqoKmUbQ7b_38EvD3BBYWjSx6g898DV1uUmXFGBMP18M5E22v_9d57WuMhXCMy74qbIEkwGHnJBRN62ZFKG7PM4Kx42vlZXyU9GQC9Gapjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی:
شکاف میان ناتوانی آمریکا در بازگشایی تنگه هرمز و ادعای مالکیت آن بر این تنگه، از فاصله ۷ هزار مایلی میان واشنگتن و خودِ تنگه نیز بیشتر است.
به نظمِ پساآمریکایی در خلیج فارس خوش‌آمدید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/70248" target="_blank">📅 22:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70247">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBJOIJR89FuSs9_TcrS1vzrQTp-nlh64GVLpQx3WkwTNMZSmR-fEcP78Wwo7TkIiNEEek1gMDzlwh486ncOOaD55zudF_uYdWR-NguAcCq8yGAvQzOWW5YLI6-CJxKQFlPxYd5EBiJUSYioH90IlVYTgyk-3rRHbrGTG06TwB0RPeM2LECNQcUNlQAb7LktIo4odZyxPsxQBBK5WV1qt4USBtHAEFIbafA20NrJzkMUxOjwNWn649rzlb_ADseitb7QXqPM0NVm_v1MBYxRjy9qLvZGLeg8W5TZ9X0KbzJI-lDkT4LyVw7Yj-8MwASCh98BaExe7_TlXSaYNwXw_TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نرخ های جدید کارمزد خدمات بانکی در سال ۱۴۰۵:
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/70247" target="_blank">📅 21:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70246">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MluRE-SR4uadmq-c_yQUA8yc7901Xx0aTYmwaT_Dl0iU-m3bNzvCEZ9NJ2GTFkBwJQvDuvKGEP_ggv9soFXZgLMzPRQAOcgCRbdtD4YXxQFHEVlYd4EhYoU33si_rP-stEdmoVAeu3FjFxlT6m13EXzBUWwmZiwPDG97IZYo8hk1DsXa0QSDuZcKItjFqWCHu6p3NDRf3FYuuLJge04cFpfXImXA0hcMAsOmv5_l79W2fxhf_y1NtGCmON6mVM5opUllwBSyZnQ0qvMPuwovtkgIn3aR3zLIv_l7sn73T0JUz9OcaXiVxXoi-bKzw4xUZiaDiWXId4YdVPBmvuqX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
آمریکایی‌ها تصور می‌کنند که با اعمال فشار شدیدتر بر ایران، می‌توانند امتیازاتی به دست آورند که هرگز بخشی از توافق نبوده‌اند.
بِسِنت و هگسِت اصلاً در حد و اندازه‌ی این کار نیستند.
دیگر منتظر نباشید که این گروهِ دلقک‌مآب خرگوشی از کلاهشان بیرون بیاورند و گندی را که خودتان زده‌اید، جمع‌وجور کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70246" target="_blank">📅 21:12 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70245">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df1fa3ba9c.mp4?token=j5iXgKeZCAc0FJfm7w5ns93juEZWUSq0KbzqQ2hZhMSnbk8vxcCo47e7mxtoKZS6UMchFQ4nIEs7M_-WVVC2mhyF1DlVRFTVHsfZkvUNnw-jPs8gdAZCCgPcH8deews-CwQuGQ5Arye5H6enVDao1l-8jiUNvdDjfADtcWT-Z-vdqvfI3RFB-6W9IYAzMSszXg-jShubTFQUH9_R0fCblXDrOdbSH3sPmrCbchszSBYLJ2yrGW8Bdn8AJHBFN2NReR3qJ0FZm5LYTC8ENdEbjHN-9A1J9P5nBIrR-5PAfE-mz7QKBXJyc1GvW87dI4b5KZtVlWZh81gv2CLvwNHM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df1fa3ba9c.mp4?token=j5iXgKeZCAc0FJfm7w5ns93juEZWUSq0KbzqQ2hZhMSnbk8vxcCo47e7mxtoKZS6UMchFQ4nIEs7M_-WVVC2mhyF1DlVRFTVHsfZkvUNnw-jPs8gdAZCCgPcH8deews-CwQuGQ5Arye5H6enVDao1l-8jiUNvdDjfADtcWT-Z-vdqvfI3RFB-6W9IYAzMSszXg-jShubTFQUH9_R0fCblXDrOdbSH3sPmrCbchszSBYLJ2yrGW8Bdn8AJHBFN2NReR3qJ0FZm5LYTC8ENdEbjHN-9A1J9P5nBIrR-5PAfE-mz7QKBXJyc1GvW87dI4b5KZtVlWZh81gv2CLvwNHM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخشی از مصاحبه اختصاصی دیوید فراست، با محمدرضا شاه پهلوی در سال1978
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70245" target="_blank">📅 20:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70244">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9BSqq6YI0SoxyO8pY6YmpXf58nIZI9ZjDkmbMbZkplASXfRhYKxG0Ki7ojO-gfTnrVPVVqSphGRvxBydE6xP--WG051HJMM-pc2OP9S0oIg2M5-6q_GlHwmcugH12k-AtjkPm1mH5xBzVLp81PVBq8xAYz_7f8lByOowaL8p6LcJFcNAGGgCQujlkaEPPHOknY6FcrtHBgDmF19soRP-C25inHz8FthxM3_W7vzKRFSwzLYnFbwaRwVbsVBfBXLZjE3VtL0zZMuoAbvlTQQchPmLfdghMLMA_j-QtE0r0pYr-XdVUYw81_xpeOsGTWpFbWz7IMtJjOkcuB3iQAi2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آلارم موشکی در امارات  @News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/70244" target="_blank">📅 20:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70243">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mx_1BisF5jMvqhwraa-94Wyl2QIJ4Y40IprXMKGi4xZrma6BXmp9V_KQrz_4ZbB9GQ3k8eMubz5kphB6m1P8aUrpFo8Nz-EeakCuLrU9KfKuQO1shiNzYnBv09EklacQv7QHWEIDe3fe_bvjnRG-IXPiCa2DneqUs87A-SzRCi4reBtAh-eV_-9qNc6UllnzcLFf7FZe71vX8X8LV0HJa_FpAOxc3GqU0y_kL46xAyU7xS8sW5AbFwe8noqzjdvuua6sbUF_qv4kZG1BCelNwwow4iTCxaeOaLK9B8twwhVpdcpHVjGQsZYSWbrg5THCNzvCVdmYi4t_NGICA0fBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مهلت ۶۰ روزه تمام شد؛ ایران و آمریکا در برزخ جنگ و توافق:
خبرنگار الجزیره می‌گوید مهلت ۶۰ روزه تفاهم‌نامه ایران و آمریکا به پایان رسیده، اما نه مذاکرات واقعی به نتیجه رسیده و نه جنگ تمام‌عیار از سر گرفته شده است؛ در این مدت، پیام‌ها و درگیری‌های محدود ادامه داشته‌اند.
به گفته مقام‌های ایرانی، این مهلت صرفاً برای مذاکرات توافق نهایی بوده و به معنای آتش‌بس یا پایان جنگ در همه جبهه‌ها، از جمله لبنان، نبوده است.
هم‌زمان، ترامپ از تمدید این مهلت سخن نمی‌گوید و مواضع تندی علیه ایران مطرح کرده؛ وضعیتی که به نوشته خبرنگار الجزیره، چشم‌انداز رسیدن دو طرف به توافق را مبهم‌تر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70243" target="_blank">📅 19:51 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70242">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2983ea6f26.mp4?token=lpkP4q3CYkrG3HRFXony63IY699kXIyAeQkURLjThzUitYckJrO9IuwVbEUvqzXetcwl_8P8D7JimhiUUyzLkTBgb6sFcQbs09moMVWrursol_93tUkorfZiR1k_Ehyl7TTrCAr-kh_fj6Mc9j8TmKyyd3TCVx70tL8s0v0FK3FsX7TUuXnkiNPfKmEttX3mBFWrNxm7ycK-P3RK29EGvJ_87Z3WpBQT2xlx2OpH1XTik2qy33y8UAGyYXf_5nnXCj-Q5OOZTXRZ3OQA96mKUPKE46AAMy1MwIge52IpSTP4x45LyxdtuFx4Vb6DF90nHXS5gwf4ZlLqZe_TyOZEZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2983ea6f26.mp4?token=lpkP4q3CYkrG3HRFXony63IY699kXIyAeQkURLjThzUitYckJrO9IuwVbEUvqzXetcwl_8P8D7JimhiUUyzLkTBgb6sFcQbs09moMVWrursol_93tUkorfZiR1k_Ehyl7TTrCAr-kh_fj6Mc9j8TmKyyd3TCVx70tL8s0v0FK3FsX7TUuXnkiNPfKmEttX3mBFWrNxm7ycK-P3RK29EGvJ_87Z3WpBQT2xlx2OpH1XTik2qy33y8UAGyYXf_5nnXCj-Q5OOZTXRZ3OQA96mKUPKE46AAMy1MwIge52IpSTP4x45LyxdtuFx4Vb6DF90nHXS5gwf4ZlLqZe_TyOZEZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
اولین جنگنده F-35A آلمان مراحل مونتاژ نهایی را پشت سر گذاشته و در تأسیسات «لاکهید مارتین» در «فورت‌ورث»، وارد مرحله تکمیل نهایی شامل رنگ‌آمیزی و اعمال پوشش رادارگریز شده است.
مراسم رونمایی برای ۱۸ سپتامبر برنامه‌ریزی شده و انتظار می‌رود نخستین پرواز آن در اواخر سال ۲۰۲۶ انجام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70242" target="_blank">📅 19:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70241">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">46.2 MB</div>
</div>
<a href="https://t.me/news_hut/70241" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/70241" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70240">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIsKN7zXjM338ZpUdadlJ4TKTTdozGHlLtON4VLusACZ1MrlrSvPr8yrdmt-qCo_wuveMVFBzoFDVCO__Ei3ALl8zDDZNZa3qCAqS9_aSvpiXNyvYAe5zW6--6WVerrP0n0HWCrrGUfJSVQZmVhnF_ZHhdnfaoGu7FL54_XBDWswV44mDk4crrqWLoQoQ0D_4cWR_Qm9LcLexJX18oOrFTGZYjOnKAZ_0ipFOv35Thp7ES2Cmd1TWB6xyvC6596PJWvKnu67iOuRBKIS74x54H0c2Us5VOmkorzBuR6MezsLPN-ewuph627_nQFgfsmF3Dd2NpoaDGaG4zN6DP39pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
سایت جهانی  و معتبر
#Melbet
🔴
بازی های مهم 27 مرداد
🆗
ثبت نام آسان و سریع کلیک کنید
🆗
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
پخش زنده ی تمام مسابقات
✅
درگاه اختصاصی برای کاربران
👍
پشتیبانی 24 ساعته فارسی
🎟
Promo Code: MELBET90
🇩🇪
دانلود اپلیکیشن MELBET
📱
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
g27
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/70240" target="_blank">📅 19:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70239">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avupc-avsEoEUewOZGMc70sHD1yvU3vvig0YBtUIcd_7hiQg18YYQfiKPvqSoa8tiTToqxWwEpAjA_qievo1owO57vLDoiklYNpsGV6chbTXykkeI90nEro5uedYNqryk5ESNxY2MArHcp_Y61qM8PZz_FtR7d2Ppxo2vdsgmhKeM2AqShjzyUpttD1qKRHxYIZqoYBmT-LUNVLvG60760NB8PlKCMXQ34kvrnPUHvn_oXL8rW7nN7EZjDlfdqmw6pu5E0qYTlleGjKNpjd9NiWCgprZlvi8clCRNbx2NvEe8DHegGQaybsaEQr4uJymaFwrKstcpbIOOBZ9TT4knw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فعال شدن آلارم موشکی در امارات
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70239" target="_blank">📅 19:08 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70238">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2f073a154.mp4?token=QLApkR3hsj_jVnqPse3TYHJW_M7mRH-pSjTwkfCp8KlwTFY8aJgdSUP62Pdl1Ck59fDfjQsg7_bwSVi2PJdO5uOqwdbXo2HYa5veexULyCx68cUJ5pgwfjaSq5EFB4vEq4c5ngrUIr1J_rpA1LOSiKLRrz6tAom7TQL3TCOte8PAN8NzSTTF7NZYFcaNMZ8LernUHIfJgl5QnPuRS75JUT6kb5YgU0AW6DdzWAiTl4R7hpByWSD_2OwexcGAm2G-WiIsEnobo2UDQk4K6hX-WYzjvPDvznyQJwSYpNGsJKXcFWegNKYaQoYzQWPQnK5oK4kFqwAgQLjTQKKD67vd6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2f073a154.mp4?token=QLApkR3hsj_jVnqPse3TYHJW_M7mRH-pSjTwkfCp8KlwTFY8aJgdSUP62Pdl1Ck59fDfjQsg7_bwSVi2PJdO5uOqwdbXo2HYa5veexULyCx68cUJ5pgwfjaSq5EFB4vEq4c5ngrUIr1J_rpA1LOSiKLRrz6tAom7TQL3TCOte8PAN8NzSTTF7NZYFcaNMZ8LernUHIfJgl5QnPuRS75JUT6kb5YgU0AW6DdzWAiTl4R7hpByWSD_2OwexcGAm2G-WiIsEnobo2UDQk4K6hX-WYzjvPDvznyQJwSYpNGsJKXcFWegNKYaQoYzQWPQnK5oK4kFqwAgQLjTQKKD67vd6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان خیلی جدی: در به در دنبال یکی میگردم مشکلات مردمو حل کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70238" target="_blank">📅 18:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70237">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tgj-A7F3hzFuXezsu6qP3AM7oa8Cx-B7yL3FUYwETQ0CUbyy0U74H0G8Bwg_ZESBy9Oqbw_js3Q0gblybiPchPxQU0sPY9Kjvw71J-i7Ur_tB72PW6C1VbapLJJ2pFcoZ0ynU76mTeA0SH44egVB_L5RJxfRT7BNWBl_IrwmVkSWqNbSl-tFnxzfda34tORgLlptkncPGF1My9EBgDMvR6Pv7vHzOHhD0pz-UTg588rflkNa86XjicSn9rnARXIYW3pCBUtOG3pUCC4GJcLGG4oJuJ-MAQZMZe5swGbeUEcqwjOUhqL1mb6kCZCFOj40-2MNtj-bF-34i3Ejxg8JuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
هیچ مذاکره یا گفت‌وگویی با جمهوری اسلامی ایران در جریان نیست و هیچ مذاکره یا گفت‌وگویی نیز برنامه‌ریزی نشده است.
محاصره دریایی همچنان با تمام قدرت برقرار است.
تنگه هرمز باز و فعال است.
همه مین‌های دریایی جمع‌آوری یا منفجر شده‌اند.
از توجه شما به این موضوع متشکرم!
رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70237" target="_blank">📅 18:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70236">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe8b4bd45.mp4?token=WxGAGWyYswQW_RMOo3NbXGaKZim3AEF5ToapSOzk_JS1cyKXDFMdaV6RSntPHHJvKs_rWPIDr_-AbPHzEFrfPNnRv-jxzK0Opx3Lhj-EH0jzVqIDaW_A8mvc7khIs349YL5d3WP_gAlindd5Ll6TfXs3aArv-aq2cbFwfYGNDGMdH-owF0-pctQshJap2JSvyTOdaNFcQ37haUnfklOf2aWauZVWcbtGWH8D0jLEG1T8hS2ETbrgvkNA_IjLvqHuCSCX6YOQiBu2n4cFFeRN4-vYKdXwVbUplBfBjlhcYr8ASQ9UdWopNPI_SUjIjiGvXEprCZWIi_30mje8ooYZwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe8b4bd45.mp4?token=WxGAGWyYswQW_RMOo3NbXGaKZim3AEF5ToapSOzk_JS1cyKXDFMdaV6RSntPHHJvKs_rWPIDr_-AbPHzEFrfPNnRv-jxzK0Opx3Lhj-EH0jzVqIDaW_A8mvc7khIs349YL5d3WP_gAlindd5Ll6TfXs3aArv-aq2cbFwfYGNDGMdH-owF0-pctQshJap2JSvyTOdaNFcQ37haUnfklOf2aWauZVWcbtGWH8D0jLEG1T8hS2ETbrgvkNA_IjLvqHuCSCX6YOQiBu2n4cFFeRN4-vYKdXwVbUplBfBjlhcYr8ASQ9UdWopNPI_SUjIjiGvXEprCZWIi_30mje8ooYZwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همینطور که قالیباف داشت از دستاورداش توی لبنان می‌گفت ،
شبکه خبر هم با زیرنویس جواب شو داد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70236" target="_blank">📅 17:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70235">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bff1d789.mp4?token=VgSOH10J2eRwNE9Y8dYznZiPl2l1NIwlVCp0ZVl5twr6x048qthYDlmwz4lWvDT9J_oRUQS4xQ98xCCHYDL9Lzi86ILEwfjRDVIKT13F8JQNdsFYno8b7hDp5RgJw0ii-u6uK-CdLcPDpH3-EULNK5w0pZK6uUg4VW1YoYUy4ULqY1BuN7P9M4KMzly2ALc_RWhXP3idmmgloahiqDsIhXi2pK_vHP-KELfDUve7VgKCT4VwqSO0XT2a1V0UnkaL8igagN3DZqhnUAWREgt6DkPnTpc73xtpP5u6TPk6v83ayXN9mK872RTiSmmuwx6QNnxD9_mdiLuCUBkdgtrxOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bff1d789.mp4?token=VgSOH10J2eRwNE9Y8dYznZiPl2l1NIwlVCp0ZVl5twr6x048qthYDlmwz4lWvDT9J_oRUQS4xQ98xCCHYDL9Lzi86ILEwfjRDVIKT13F8JQNdsFYno8b7hDp5RgJw0ii-u6uK-CdLcPDpH3-EULNK5w0pZK6uUg4VW1YoYUy4ULqY1BuN7P9M4KMzly2ALc_RWhXP3idmmgloahiqDsIhXi2pK_vHP-KELfDUve7VgKCT4VwqSO0XT2a1V0UnkaL8igagN3DZqhnUAWREgt6DkPnTpc73xtpP5u6TPk6v83ayXN9mK872RTiSmmuwx6QNnxD9_mdiLuCUBkdgtrxOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز هواپیما C-295W آمریکا در ارتفاع پایین برفراز اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70235" target="_blank">📅 16:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70233">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac96569c1.mp4?token=m2ddMAk126bmtTPcLTxJlCe-PfePiwoWUeVRYCIcV583aGa4TDby-8URGINm_LRTx7-Y56nbDDa7wN5q9W5oY0z31eBPhqtlnWSpqSS-A7K6N3LVYhAPQqfiXDAOPWOI6QDELWlOYLu5V8nmYKsyKVM-FGsAfozhappOfVlxXshGZ_yaKUqDLvumeX_WUlljddg2ze2bXN_4qS_RQsDK4ex-IdN65UQxlx-wn9ZqVOWayz_JMn0mAxQwUXpFRL0rkdI_GmbQkTMYExMPRv7LU_BEb1P15bpr_N-3o6pJQ7k_x_olrouse95zZqmyIxigIkSl1HfJmSMlLtC_q_XV0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac96569c1.mp4?token=m2ddMAk126bmtTPcLTxJlCe-PfePiwoWUeVRYCIcV583aGa4TDby-8URGINm_LRTx7-Y56nbDDa7wN5q9W5oY0z31eBPhqtlnWSpqSS-A7K6N3LVYhAPQqfiXDAOPWOI6QDELWlOYLu5V8nmYKsyKVM-FGsAfozhappOfVlxXshGZ_yaKUqDLvumeX_WUlljddg2ze2bXN_4qS_RQsDK4ex-IdN65UQxlx-wn9ZqVOWayz_JMn0mAxQwUXpFRL0rkdI_GmbQkTMYExMPRv7LU_BEb1P15bpr_N-3o6pJQ7k_x_olrouse95zZqmyIxigIkSl1HfJmSMlLtC_q_XV0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
هنگ سوم عملیات ویژه اوکراین، شهرک آندریوکا-کلوتسوو در منطقه دونتسک را آزاد کرد و تقریباً 30 سرباز روسی را به اسارت گرفت.
کسانی که به مقاومت ادامه دادند، کشته شدند.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70233" target="_blank">📅 16:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70232">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM_ClBfmczwkazgMN2xR0e-7FLCUajH4i7GwgeQcXj1eBpy7CA0SI1jHfwWcw6oorc6hJzNluQ3-w90Q4jnQZsEC_-LLy6PKpWfMKQ19TXzf7Yjedelp7p1tarJC87MlUFNI25544HJoEPfGgOKI6dxcWwDRtZw7I6DOSScqYo00rMO3nxZJwxnTlLiIMmHZwghfJqeO6KpPLX8R-1T28HSzvTrwtX8Bo51-5rzGS9NP1enua6pQvjUlEW80X0Z6OakrR1c_CRVNPM2RQjRfKSCCPR3CGs_g1IgtV6iTIjaG8Mc32MmyvaaGCAbcaPhbUpcliBx1wV7z2pAQ-ZkQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
معاون وزیرخارجه جمهوری اسلامی:
همانطور که ترامپ نام خلیج همیشگی فارس را به صورت صحیح نوشت، به زودی توهمش درخصوص تنگه هرمز یا اصلاح می شود یا توهمات این متوهم را اصلاح خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70232" target="_blank">📅 15:25 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70231">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMtQqMRyFCxMSBeGKi3GlEbqZ_lVxJ8Y4ycp8pAkA5sJqKFjkW-r-NCJXXpYzG_gTr-epgAvtNpH0ERGwAZ0IZAF-TvY0UQ1md2ZDefR684jhdSIgkwS7w8N61nC2lUfOxKsi7lLQnoQ8Q0Ouk7fCRAoXUsMiKSSz2N6JPhCqUBqFd3GjT2GkfR5FftpbQWp3cPJlLfpfC8fOp6Pb9MngBz7SQS7BzGwe3Oe_cxx1o9KWW54yhrQNj6r_utMQHykAp8rvoXUSi68EnL4WDFgIoTSkoQw9tjQVad_mK4xePLYDxnqgAh01nUVUo1vEjAtsccI1wp6WBC67wZ1YyX26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
پست جدید املاکی در تروث سوشال:
تنگه هرمز قلمرو جدید ایالات متحده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70231" target="_blank">📅 14:50 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70230">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06cc678393.mp4?token=Uez4cfLZrik8wStR81K3eEFJDDq4NmjXv15rWvoJmA1b_gc8saYEjdhL1H-2mJoRYVceqCP9PyIuVo5FEUJ73jurhyZdYv97UmckVihYKOakwLsnxksnb30Pe64AYX2q1DvsJx5_EwaVnFBrvpP_Zq_u_zUWb1vFEHciniKerxjm3tGe1fO7Ue7DGMyrIenDdWisHWuoC3_HwZMrCcSLRcVFpr6zN5DRU5Tn5y1l06rdbpdzTi2yH3U1jmwvKLnnq8hypsUu-9CbNicc5_2_BnGugWHI3Y47934b2GDUHg80r8NMhwJ702Wivti9BOYWlGSA99tr_SgtxdztXLy63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06cc678393.mp4?token=Uez4cfLZrik8wStR81K3eEFJDDq4NmjXv15rWvoJmA1b_gc8saYEjdhL1H-2mJoRYVceqCP9PyIuVo5FEUJ73jurhyZdYv97UmckVihYKOakwLsnxksnb30Pe64AYX2q1DvsJx5_EwaVnFBrvpP_Zq_u_zUWb1vFEHciniKerxjm3tGe1fO7Ue7DGMyrIenDdWisHWuoC3_HwZMrCcSLRcVFpr6zN5DRU5Tn5y1l06rdbpdzTi2yH3U1jmwvKLnnq8hypsUu-9CbNicc5_2_BnGugWHI3Y47934b2GDUHg80r8NMhwJ702Wivti9BOYWlGSA99tr_SgtxdztXLy63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
جعفرپور، مدیرعامل مخابرات:
قراره فیبر نوری کاملا جایگزین کابل مسی بشه که اینطوری سرعت اینترنت ثابت تا 80 برابر بیشتر میشه...
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70230" target="_blank">📅 14:33 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70229">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6829188988.mp4?token=Kwt70sWn-3x-e99iwMQueX1NBbalflOc3MABv-6jAS0SQ5qRcrUwE0-1IzgtXBMJIAfQqqeXbVU0aRzBNqVRjmDDhUdCdlYg1nMzUO71YOd2b19AVREDrqD1GJbICaSHxjQrwxZ46KUqcGnHhHhsxn-lQgQz8s8pO5SMHQ9RcKTqGftLc5mz6baCP2pvH6PiXeShMileo1emLT17z_JzFbe9ptBB9RHeM75eyJiyneiMFIYZwYtlYpMykFClN9mVTjaP1EGjqCOnTmJHu5xiS8uf3hmwUY7bVs0HqkIc8DioQf4jQCg93xfzNIS1mqBOGSZXCy_bcC5k183h5aHaEjlYkKWDgkVHy27KNdoCNjJHLdguUDExpfWAqbDqgLWBY0mv2_FZfuxRnaSJMh8Xa1g_NEPvWcjVGYDzU5UEseNt2UGOWEUSiQipyn12ZhHxnnx9AZmBzipTinPUeagHlyxN6h2UT0mVoSISAM2ugEMbkyneJ82EYA3l78oO3AXcKMnwtbjA8k4l6nTq4lq0MnnBCnj_-lxdWn44G_6bqqlwa2X0cxBlIZXl4ws2xPJUw7FR5krDdLDFLbHLC6NezxliwbFRSl_Vo0M_1yZaeYkGzyxICr6YAkOYGCWcvUtukhUvWMXiQ-sw2f0scIm8KqeTzMOslb3IajNSRmam7WY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6829188988.mp4?token=Kwt70sWn-3x-e99iwMQueX1NBbalflOc3MABv-6jAS0SQ5qRcrUwE0-1IzgtXBMJIAfQqqeXbVU0aRzBNqVRjmDDhUdCdlYg1nMzUO71YOd2b19AVREDrqD1GJbICaSHxjQrwxZ46KUqcGnHhHhsxn-lQgQz8s8pO5SMHQ9RcKTqGftLc5mz6baCP2pvH6PiXeShMileo1emLT17z_JzFbe9ptBB9RHeM75eyJiyneiMFIYZwYtlYpMykFClN9mVTjaP1EGjqCOnTmJHu5xiS8uf3hmwUY7bVs0HqkIc8DioQf4jQCg93xfzNIS1mqBOGSZXCy_bcC5k183h5aHaEjlYkKWDgkVHy27KNdoCNjJHLdguUDExpfWAqbDqgLWBY0mv2_FZfuxRnaSJMh8Xa1g_NEPvWcjVGYDzU5UEseNt2UGOWEUSiQipyn12ZhHxnnx9AZmBzipTinPUeagHlyxN6h2UT0mVoSISAM2ugEMbkyneJ82EYA3l78oO3AXcKMnwtbjA8k4l6nTq4lq0MnnBCnj_-lxdWn44G_6bqqlwa2X0cxBlIZXl4ws2xPJUw7FR5krDdLDFLbHLC6NezxliwbFRSl_Vo0M_1yZaeYkGzyxICr6YAkOYGCWcvUtukhUvWMXiQ-sw2f0scIm8KqeTzMOslb3IajNSRmam7WY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
قالیباف:
هرفردی که با تصمیمات خود باعث نارضایتی مردم بشه از دشمن هست و تغییر شیوه کالابرگ حتما در دستور کار قرار میگیره
ما خودمون نیز در میدان مشکلات اقتصادی درگیر هستیم و راحت ننشستیم
نیروهای نظامی با اقتدار مجتبی خامنه‌ای تودهنی بزرگی به دشمن زدند که همه تعجب کرد
دشمن از روی استیصال اومد مذاکره و مجدد شکست خورد
خیابان محل میتینگ های انتخاباتی و برخی کارهای غیراخلاقی به اسم تجمعات نیست
تا رفع محاصره و آزادی پول ها و رفع تحریم های نفت و پایان تهدید و توقف کل عملیات ها در سرتاسر جبهه مقاومت تنگه هرمز باز نمیشه
تفاهم نامه باعث شد تاب آوری مردم بالا بره و از نظر نظامی خودمونو بازسازی کنیم
افزایش قیمت بنزین تدبیر نیست آقایان دشمن بر آشوب و اغتشاش از روی بنزین حساب کرده مواظب باشید
صداوسیما دیگر قدرت سابق رو نداره و عملا در رسانه شکست خورده حساب میشیم
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70229" target="_blank">📅 13:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70228">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fcfe671f.mp4?token=Nxm1jx6YT1tNYoEZxi-q-NE1EVOQn3NTyVtiTjgDelYh5uyvm-MW_eZTX03CbhdxRNNvmKHbN5iVpRet_8SMLjyCkUCSZMd695AunsULBkhls2uR8TneX1SlVi4T-WQUaD31pzI3INrbL_wQXvQNPfMau3qGfhPUX4M6xH45UxKR_EKtec0qIlKDdPap6Nx_Zqhkvds7kvvGVap_DZA5Krjv1bS4OQLz6s6Fj3TLllwLumKQBERjXzID8CtSJafafbe0_6WrgHYy8PdbuhZwOsNA3J2XGImPNJbqIMotTcUvzk7GchnVMhbWgl_6IvlyevkyGfIIIJg2OQ0OmaN13Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fcfe671f.mp4?token=Nxm1jx6YT1tNYoEZxi-q-NE1EVOQn3NTyVtiTjgDelYh5uyvm-MW_eZTX03CbhdxRNNvmKHbN5iVpRet_8SMLjyCkUCSZMd695AunsULBkhls2uR8TneX1SlVi4T-WQUaD31pzI3INrbL_wQXvQNPfMau3qGfhPUX4M6xH45UxKR_EKtec0qIlKDdPap6Nx_Zqhkvds7kvvGVap_DZA5Krjv1bS4OQLz6s6Fj3TLllwLumKQBERjXzID8CtSJafafbe0_6WrgHYy8PdbuhZwOsNA3J2XGImPNJbqIMotTcUvzk7GchnVMhbWgl_6IvlyevkyGfIIIJg2OQ0OmaN13Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تفاوت وحشتناک قیمت گوشی ها در عرض یک سال:
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70228" target="_blank">📅 13:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-70227">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5264a79fd5.mp4?token=IF-n_9JtVYP--nO-Q1TAk8MVBC2XX5TrvWgpB6ttU0wELzGbtK6aVSKtx1Y1ZO2d0AVIZtL67-tNDUhW0XeAiY2WLYP2SmVus_6nHRh6yP1oF4ryFBdqWyniK2W39RiZ3lHbi2YnsV17o_M9SNwMljKWD6B9SlmbsF2gxGjhEWd2ViLN3T5rmY8W38DJErQLoTYZDUoc7XccleKelVjTX9OgHuXnuERKp8PjO2Q2Y6Jf4m_oeK3MJhZi3ZMPgh6wPD-8lKyf-92rolpZtyWRj5r2ogCYEC3q99LEff-frZCkghVNn6gKqzxbVHqnRdaUzqyh-cnDFYdMx_LvTx0PAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5264a79fd5.mp4?token=IF-n_9JtVYP--nO-Q1TAk8MVBC2XX5TrvWgpB6ttU0wELzGbtK6aVSKtx1Y1ZO2d0AVIZtL67-tNDUhW0XeAiY2WLYP2SmVus_6nHRh6yP1oF4ryFBdqWyniK2W39RiZ3lHbi2YnsV17o_M9SNwMljKWD6B9SlmbsF2gxGjhEWd2ViLN3T5rmY8W38DJErQLoTYZDUoc7XccleKelVjTX9OgHuXnuERKp8PjO2Q2Y6Jf4m_oeK3MJhZi3ZMPgh6wPD-8lKyf-92rolpZtyWRj5r2ogCYEC3q99LEff-frZCkghVNn6gKqzxbVHqnRdaUzqyh-cnDFYdMx_LvTx0PAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
محمد‌باقر قالیباف:
قبل از رفع محاصره، آزادی اموال بلوکه شده، رفع تحریم نفت و پایان تهدید و عملیات نظامی در همه جبهه ها و دیگر شروط تفاهم نامه، تنگه هرمز باز نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70227" target="_blank">📅 12:24 · 27 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
