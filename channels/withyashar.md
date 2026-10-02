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
<img src="https://cdn4.telesco.pe/file/mPl0kQ16Bnyj5Apm836lPyQyevfRa6TWgj8LUv8Y9V_YitnM2dalUzP8xzRqXkghJQ-pyClY7kZTXau95oHlGBt8iyHVTEy7UBzgPOlxT5Jvwp4ZLV7E2av6mU6DmKtTQlWid2aVqPGezFXN_dyogdvgNbuFVK652XTO554vD4ARXwRkNY4tSJRn5bZ3exmQVKOsCBzzExJIK9Jc1Q4eI27jRsT9AzjYe0kt7ajr_suNL26sNcJ8pCfJ7gYvzgY9UF9BcvOd4KYXqTq0a5KzPeNpeC7CvuTdxTqRKBP-1VKHKU1Gi-Mf7rJC-BL7MXPhprGSmbpTjLl6UURtr5qsaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 488K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/815c6ae3f3.mp4?token=VMgCTFDPxCySVF9gWhlTl9T0etAGnNWzmouB_vXGBfZYtZZc6nmLtU1Y3rG3lyYuK1Q9rKEaQY4yjecJJeDrVa8OCANHs_IgRJXOm9PrJ8STXollPHH1BvYEm2PvZDxaDRbRIWkVz-Z1OCEHxLDbU7uPIno2-UXrDVH8zYLFe_kf3Y9kJKAm_w5kQPsdHc_m0J_whPSvZUmZm1P5hbsJSsSsm1Y2WV6lP7PnB0ykZHpuNHQeprafxKCV1aqv6O8tNXUtUF9BeOvINzF5v-6NVxtMYE6XdJVYYdigJWlhWf4m9J8IZz3DRYAtaADtxT_4eSapz1Rp5Mqih8Bd567-4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/815c6ae3f3.mp4?token=VMgCTFDPxCySVF9gWhlTl9T0etAGnNWzmouB_vXGBfZYtZZc6nmLtU1Y3rG3lyYuK1Q9rKEaQY4yjecJJeDrVa8OCANHs_IgRJXOm9PrJ8STXollPHH1BvYEm2PvZDxaDRbRIWkVz-Z1OCEHxLDbU7uPIno2-UXrDVH8zYLFe_kf3Y9kJKAm_w5kQPsdHc_m0J_whPSvZUmZm1P5hbsJSsSsm1Y2WV6lP7PnB0ykZHpuNHQeprafxKCV1aqv6O8tNXUtUF9BeOvINzF5v-6NVxtMYE6XdJVYYdigJWlhWf4m9J8IZz3DRYAtaADtxT_4eSapz1Rp5Mqih8Bd567-4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الکس پیلیتساس
(
تحلیل‌گر امنیت ملی آمریکا، کارشناس ضدتروریسم و افسر سابق پنتاگون
) در سی‌ان‌ان بخوبی استراتژی جمهوری اسلامی رو توضیح میدهد
@WarRoom</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/24774" target="_blank">📅 18:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye7tUR5RATcocHNlsPPwQohkunab7oQEn5qFUpivxBo57p9pOeiXdHcRkUeymKG39voOksb0CRewuN4dqiq9uUudvlzAavZjsn9fdqkPOQXScx7B0izhhTO1VJ9PEZm1CgzfzeZIzvIhHrhRPtAgFagAFtEpzyNPRxbtYE28ClW3TKfUcj9w7JpFMhOSVdcluifkThuOCoIsyqV7wGPzUAULOuWA9-kKg94ABLuJnIRLEXaHRSqJ5_0_kTdL8_bWl6Ne1wn7uEOylDEGbL3FJZMadpgvkEtStOGHhaT43oTFNsT2liHcDzTNDQ3T45aNm5us4jQsfW6YnIyLQHP1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الناز شاکردوست به اتهام «فعالیت تبلیغی علیه نظام» به یک سال حبس و دو سال محرومیت محکوم شده است. وکیل او گفته این حکم صرفاً به دلیل انتشار یک استوری پس از حوادث دی‌ماه سال گذشته صادر شده و محتوای آن تنها بیان اندوه بابت جان‌باختن جوانان ایران بوده است. به گفته وکیل شاکردوست، در این نوشته هیچ اشاره‌ای به نظام، حکومت یا مسئولان و همچنین هیچ فراخوانی برای اقدام جمعی، فعالیت سازمان‌یافته یا براندازی وجود نداشته است.
@WarRoom</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/withyashar/24773" target="_blank">📅 18:02 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b731ebb6ee.mp4?token=R6u_w6rAPkQoFiXIgFJvLLdJPOf6PATWSZRQ3jkw_qMB2ObFc3Mr-WNWA2egCP0ktFTOcD4eyMR9O02Ztsc1PeAdqrwhGEd6722BhRqH2jYPYVtp_s7veI86obMVPP8-l0CxS8u3USLXvoHKVdzuLjhwRFjTcQUbkIqCVkdzgEnySiGIxrmTQ9FHMcBWaJwlsR5c-L4Gf7cpwuLVvm3pCzSRa3xHFgcLrP_QbdbdUTDC7-99baSI0eHNi2un2MY0vowzeP5LusXYjNGirp941j5ImA5LeInfzEhDhRlUMiZ0IbbbT8t1KOnZJARn8LdaQW9IH-zwShvQneXct04L50VLc3A2sM2x_BlgJLMKg9RsMyKVtQJAXhJA5Rpd_7ScLUMfDh4QQJuk5FlO2nUEfXMBwqOxZ7YXet2wNBohzdx6jWrRcrosgFIvnIK6rI-x3T404AxrqI6O4s2v7XaWgvNayIp4yq5BDl1vsYh2hPVwu16yEK_qDYF64QiXg1oEO_A3treyUcippRAUw-3KCgFx71v9PFih82fvI6T4J3qKNDzx89fmNsnci6u4zvAe0TTiXoIi0D-jAfhuE3-U2jmN585JS7txH5FlYgK398R-tNlj2MNeRVrCw90_OjsjmKWBWqlaq4O-2FCXXS0-4E4eXyssRcGmxOgTlAzebZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b731ebb6ee.mp4?token=R6u_w6rAPkQoFiXIgFJvLLdJPOf6PATWSZRQ3jkw_qMB2ObFc3Mr-WNWA2egCP0ktFTOcD4eyMR9O02Ztsc1PeAdqrwhGEd6722BhRqH2jYPYVtp_s7veI86obMVPP8-l0CxS8u3USLXvoHKVdzuLjhwRFjTcQUbkIqCVkdzgEnySiGIxrmTQ9FHMcBWaJwlsR5c-L4Gf7cpwuLVvm3pCzSRa3xHFgcLrP_QbdbdUTDC7-99baSI0eHNi2un2MY0vowzeP5LusXYjNGirp941j5ImA5LeInfzEhDhRlUMiZ0IbbbT8t1KOnZJARn8LdaQW9IH-zwShvQneXct04L50VLc3A2sM2x_BlgJLMKg9RsMyKVtQJAXhJA5Rpd_7ScLUMfDh4QQJuk5FlO2nUEfXMBwqOxZ7YXet2wNBohzdx6jWrRcrosgFIvnIK6rI-x3T404AxrqI6O4s2v7XaWgvNayIp4yq5BDl1vsYh2hPVwu16yEK_qDYF64QiXg1oEO_A3treyUcippRAUw-3KCgFx71v9PFih82fvI6T4J3qKNDzx89fmNsnci6u4zvAe0TTiXoIi0D-jAfhuE3-U2jmN585JS7txH5FlYgK398R-tNlj2MNeRVrCw90_OjsjmKWBWqlaq4O-2FCXXS0-4E4eXyssRcGmxOgTlAzebZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مرد فرهیخته ، ژنرال جک کین : مبارزان ایرانی در گروه‌های متعددی سازماندهی شدند و میخواهند مسلح شوند تا کشورشان را پس بگیرند ، هم مسلح کردن ایرانی‌ها لازم هست هم اقدام نظامی شدید در لحظه مناسب بخصوص بعد از فروپاشی اقتصادی
گزینه توافق و دیپلماسی کاملا کنسل است
‏این رژیم باید سرنگون شود..
@WarRoom</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/withyashar/24772" target="_blank">📅 18:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ در‌تروث : «اروپا به‌تازگی با آزادسازی حجم عظیمی از ذخایر بسیار زیاد دیزل خود موافقت کرده است. این روند بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم!»
@WarRoom</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/withyashar/24771" target="_blank">📅 17:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24770">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شبکه 14 اسرائیل: ما رهبر ایران رو وسط تهران کشتیم و هزینه خاصی هم پرداخت نکردیم. اون مرکز رنج ما بود.  ما فکر میکردیم ایران کار دیوانه واری انجام بده ولی فقط 40 روز جنگید و بعدشم به توقف جنگ رضایت داد. دو دهه الکی ترسیده بودیم.
@WarRoom</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/24770" target="_blank">📅 17:22 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ: مأموران سرویس مخفی به من گفتند به‌دلیل بدی آب‌وهوا احتمالاً باید سفر به اوکلاهما را لغو کنیم؛ نه هلیکوپتر می‌توانست پرواز کند و نه هواپیما. گفتند تنها راه، یک رانندگی طولانی است. از آنها پرسیدم «بیست با چه سرعتی می‌تواند حرکت کند؟» گفتند نزدیک به ۱۰۰ مایل بر ساعت.
گفتم: «پس سریع باسن تپلتون رو بزارین تو ماشین و راه بیفتید!»
این سفر آسانی نبود، اما نمی‌خواستم مردمی را که ساعت‌ها برای دیدنم در اوکلاهما منتظر مانده بودند، ناامید کنم.
@WarRoom
👏</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/24769" target="_blank">📅 17:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df4d8b2843.mp4?token=cXrBIdbRl0gE0fWw-MQEPq763JHFLig-_4I55Qy57AdCLB3aiLOlFhymdSmcezZVmyHHBsefdHEI6lCe2j1Yft8IYRZvs2v3dWhwTzuotWBalkW3ndmjSEemPz4WOvnb9z0RoNZsVbCdym2MhxOCzTzwvvheY-1S8VNlv5DKC0z-KRM8dSvERz48JmyD2S33HS9q32fo9JYIw9zphIMFRZ63STMJr-2d5MTJrVJhE3jWKL6-kXQlLLapi9cXtiAB-B3Ijp6txvXKtWQQ1co2ScJo4ZzZxhODLPpz2Nrzdh69t0JmdkgNH2X5M5brhE2h8TXJpW6xa3YZs8R1jBISPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df4d8b2843.mp4?token=cXrBIdbRl0gE0fWw-MQEPq763JHFLig-_4I55Qy57AdCLB3aiLOlFhymdSmcezZVmyHHBsefdHEI6lCe2j1Yft8IYRZvs2v3dWhwTzuotWBalkW3ndmjSEemPz4WOvnb9z0RoNZsVbCdym2MhxOCzTzwvvheY-1S8VNlv5DKC0z-KRM8dSvERz48JmyD2S33HS9q32fo9JYIw9zphIMFRZ63STMJr-2d5MTJrVJhE3jWKL6-kXQlLLapi9cXtiAB-B3Ijp6txvXKtWQQ1co2ScJo4ZzZxhODLPpz2Nrzdh69t0JmdkgNH2X5M5brhE2h8TXJpW6xa3YZs8R1jBISPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو:
«هر چه زمان می‌گذرد، تصویر واضح‌تر می‌شود. این عمل، نتیجه‌ی افراط‌گرایی اسلامی بود و هدف آن، سرنگون کردن هواپیما به همراه تمام مسافرانش بود.ما در حال بررسی این موضوع هستیم که آیا این فرد برای انجام این کار اعزام شده بود یا خیر، و هر کسی که مسئول این اقدام باشد، باید پاسخگوی عواقب بسیار سنگینی باشد.»
@WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/24768" target="_blank">📅 17:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فرمانده انتظامی رشت اعلام کرد یک روحانی در یکی از محله‌های این شهر توسط فردی ناشناس با سلاح سرد مجروح شده است. به گفته سرهنگ عیسی روشن‌قلب، پلیس در جریان تحقیقات به سرنخ‌های مهمی درباره ضارب دست یافته و تیم‌های تخصصی با هماهنگی مقام قضایی برای دستگیری او تلاش می‌کنند. وضعیت فرد مجروح مساعد اعلام شده و پلیس گفته علت و انگیزه حمله پس از دستگیری متهم و تکمیل تحقیقات مشخص خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/24767" target="_blank">📅 17:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رعد ‌و برق در تهران ، نترسید
@WarRoom
🫂</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/24766" target="_blank">📅 16:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ترامپ در ‌تروث: «با خوشحالی اعلام می‌کنم توافق با کره جنوبی هر روز بهتر می‌شود! ۸.۴ میلیارد دلار برای یک پروژه افزایش برداشت نفت اختصاص داده شده است. تولید بیشتر نفت و گاز یعنی تقویت سلطه انرژی آمریکا و تضمین امنیت انرژی در جهان برای آینده.»
@WarRoom</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/24765" target="_blank">📅 16:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نتانیاهو: ترامپ از من پرسید «این قدرت را از کجا می‌آوری؟» به او گفتم: «این قدرت، میراث پدران ماست که از پدران به پسران و نسل‌های آینده منتقل شده است.» @WarRoom</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/24764" target="_blank">📅 16:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c997284691.mp4?token=Wa8HU30BVJDiiorl5ShpC40RTMbACYDyaVGHN5dMp6ZBk72I2nHyC74s5ZLMoGQwrADZfv9VuNey-L-OA1ZjFOyxptRLr7ZmIoAwhKX80T4Nq3B0dvqDO1zMgyRyp4gbJi4KVk-ptqHcQTAwix7-HdY3ScpfFgrzQqtze4SY4iiOht-4rYUcx2fPVoSlFEKwwpO1g6ds9hErpju9NRPJMtwgMXZ5kUfRD2GFRTc_b7KeXaA1P78jQ8Ro3xh5-Y_6KNIO-HCOh5hoY2mc-gkVh2xD2ctN_v4tX_o0x5Grpca_uSkRseEYkEFVgD3oORwa--V9L6xENnSpJSfzeX2N5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c997284691.mp4?token=Wa8HU30BVJDiiorl5ShpC40RTMbACYDyaVGHN5dMp6ZBk72I2nHyC74s5ZLMoGQwrADZfv9VuNey-L-OA1ZjFOyxptRLr7ZmIoAwhKX80T4Nq3B0dvqDO1zMgyRyp4gbJi4KVk-ptqHcQTAwix7-HdY3ScpfFgrzQqtze4SY4iiOht-4rYUcx2fPVoSlFEKwwpO1g6ds9hErpju9NRPJMtwgMXZ5kUfRD2GFRTc_b7KeXaA1P78jQ8Ro3xh5-Y_6KNIO-HCOh5hoY2mc-gkVh2xD2ctN_v4tX_o0x5Grpca_uSkRseEYkEFVgD3oORwa--V9L6xENnSpJSfzeX2N5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: ترامپ از من پرسید «این قدرت را از کجا می‌آوری؟» به او گفتم: «این قدرت، میراث پدران ماست که از پدران به پسران و نسل‌های آینده منتقل شده است.»
@WarRoom</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/24763" target="_blank">📅 16:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">تتر ۲۶۳،۰۰۰ تومان (رکورد تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/24762" target="_blank">📅 15:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/24761" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41835d5d95.mp4?token=q6slaoe557jhrPX8ODEvU15nxDJBZvdTOWAYEPB_yPF1GvKCILtJgVezq0L4GR_WoC2qOxLj2Nr88l4iu18FAa2mjzt0LZ7xADlylL1yoXEMLxpN4ws5JH8uWe4oliTFQR5TT6hQr_6cRB--sDdwAYCwSeuHHz8hSTOw0d-Zf7GK3a9nUY3uWVAk-XubJZDK-RKlYKzoFDlCFwhVmnARx_6q7PFi9_OFMEF8Mv0X4iXjo_yXnKt0FLLRK3bDy7LERt91CMwemflkugSgRMulxGbwFzOyQ2l5NWAqO-VwBp0r5EUdpA6ghZ2PuvFULxjO4Q0zTZvBh81wmFQbrBQfeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41835d5d95.mp4?token=q6slaoe557jhrPX8ODEvU15nxDJBZvdTOWAYEPB_yPF1GvKCILtJgVezq0L4GR_WoC2qOxLj2Nr88l4iu18FAa2mjzt0LZ7xADlylL1yoXEMLxpN4ws5JH8uWe4oliTFQR5TT6hQr_6cRB--sDdwAYCwSeuHHz8hSTOw0d-Zf7GK3a9nUY3uWVAk-XubJZDK-RKlYKzoFDlCFwhVmnARx_6q7PFi9_OFMEF8Mv0X4iXjo_yXnKt0FLLRK3bDy7LERt91CMwemflkugSgRMulxGbwFzOyQ2l5NWAqO-VwBp0r5EUdpA6ghZ2PuvFULxjO4Q0zTZvBh81wmFQbrBQfeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار : دیگ به دیگ میگه باسن تو سیاهه
قیصر فرندلی فایر بیژنو میزنه
😂
این قشنگه
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/24760" target="_blank">📅 15:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24759">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حقیقت یاب
اتاق جنگ:
خبری که با عنوان «ارتش آمریکا رسماً تمرین تصرف و پاکسازی تأسیسات هسته‌ای زیرزمینی را انجام داد» در حال انتشار است،
خبر جدیدی نیست
و مربوط به ژوئن ۲۰۲۴ است. ارتش آمریکا اعلام کرده بود تیم «خنثی‌سازی هسته‌ای ۱» همراه با نیروهای
هنگ ۷۵ رنجر
در یک تمرین نظامی، یک تأسیسات هسته‌ای زیرزمینی شبیه‌سازی‌شده را در شرایط آتش شبیه‌سازی‌شده تصرف و پاکسازی کرده‌اند. این تمرین با هدف افزایش آمادگی برای شناسایی، ایمن‌سازی و خنثی‌سازی تهدیدهای هسته‌ای و پرتوی انجام شده بود. بنابراین انتشار دوباره این گزارش به‌عنوان یک
تحرک یا تمرین جدید آمریکا
نادرست است.
@WarRoom</div>
<div class="tg-footer">👁️ 90.2K · <a href="https://t.me/withyashar/24759" target="_blank">📅 15:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مرد خردمند ، مارک لوین : این جنگ هیچ‌وقت درباره تنگه هرمز نبوده؛ اگرچه حفظ جریان نفت دستاورد بزرگی است. فشار اقتصادی علیه جمهوری اسلامی بسیار موفق بوده و همچنین سایت‌های هسته‌ای و اورانیوم غنی‌شده دفن شده اند. اما تنها راه جلوگیری از دستیابی ایران به سلاح هسته‌ای، با داشتن هزاران موشک بالستیک و ادامه حمایتش از تروریسم، نابودی این رژیم است. هیچ راه خروج خوبی وجود ندارد. من همچنان خواستار
مسلح کردن
مردم ایران و
ارائه آموزش، پشتیبانی فنی و پوشش هوایی
مورد نیاز آن هستم. ما پیش از این در کشورهای دیگر چنین کاری کرده‌ایم و با توجه به ضربات واردشده به ایران، به‌ویژه فروپاشی اقتصادی، معتقدم زمان اقدام اکنون است یا دست‌کم به‌زودی فرا می‌رسد.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/24758" target="_blank">📅 14:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فایننشال تایمز: ترامپ در فکر حمله آخرالزمانی‌به ایران است
@WarRoom</div>
<div class="tg-footer">👁️ 95.3K · <a href="https://t.me/withyashar/24756" target="_blank">📅 14:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الجزیره  : بر اساس برنامه فعلی، نهایتاً تا پایان نوامبر ( هفته اول آذر ) آمریکا می‌تواند ۳ ناو هواپیمابر و ۲ گروه آبی‌خاکی در اطراف ایران داشته باشد.      البته خبرگزاری آسوشیتدپرس نظرش اواخر اکتبر (هفته اول آبان)است @WarRoom
⚠️
🚨</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24755" target="_blank">📅 13:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">جزئیات جدیدی از دولت
ترامپ
در گزارش مجله تایم :
گروک، چت‌بات هوش مصنوعی شرکت X
، تا حدی در متقاعد کردن ترامپ برای این دیدگاه نقش داشته که
ربودن نیکلاس مادورو، رئیس‌جمهور ونزوئلا، می‌تواند میراث سیاسی او را تثبیت کند
.
در بخشی دیگر تایم گفت ، ترامپ از سوی مقام‌های ارشد مستقیماً در جریان
مشکلات مربوط به ذخایر مهمات آمریکا
قرار نگرفته و این موضوع را از طریق گزارشی در
نیویورک‌تایمز
متوجه شده است. ترامپ سپس با
پیت هگست
، وزیر جنگ آمریکا، درباره این موضوع بحث کرد و هگست او را متقاعد کرد که این گزارش‌ها
«اخبار جعلی»
هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/24754" target="_blank">📅 13:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">در‌ انتظار تایید : قرائتی ، ورّاج صدا و سیما ، ریق رحمت را سر کشید
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24753" target="_blank">📅 13:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVM5xMtODKH8SlT8sq6cBKUPkMg_NWMTYmq0LdI1nCPdQg5XSDF9DHTeCticmaLnAWQ1OLUvIpH8wzRSQnYwVk9sV7OdxqPGJc4JLyRjOaXsXLMFlENkS4__pWr0TR5uvPZpZxOCN09wKmA0Gxr_8O5F6CS06j8-zYU-BZKXkwDYECBJhUhHO2BIOCjjR__RVysd-OJHAylCG4uzqIAE7vWa4R0-r_01X72GOAAZnKfJFAesIk3qr8yzdW_44S5sgNkfOWs-NHR9y7f3yi0m6_7i9A5Yw6Tou928sWu9WVoQBTFoIWVQ7z6FTZNVTlyDtq2BJYlwIrWda7CN-L0dHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلامیه خواهر عراقچی
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24752" target="_blank">📅 13:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بیژن مرتضوی: در جانفدا ثبت نام کردم
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24751" target="_blank">📅 13:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ترامپ:
اینا آدم‌های دیوانه‌ای هستند، که ۵۰ ساله  است فریاد می‌زنند «مرگ بر آمریکا».
جنگ با جمهوری اسلامی خیلی زود تمام می‌شود. ایران با تورم ۳۱۲ درصدی و سقوط ارزش پول روبه‌رو شده است، بخش بزرگی از رهبرانش هم دیگر نیستند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24750" target="_blank">📅 13:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الجزیره:
مایک والتز، سفیر آمریکا در سازمان ملل، گفت ایران همچنان اورانیوم را تا سطح ۶۰ درصد غنی‌سازی می‌کند
و حاضر نیست از جاه‌طلبی‌های هسته‌ای خود دست بکشد. والتز همچنین ایران را به نقض قوانین بین‌المللی و محدود کردن دسترسی بازرسان آژانس بین‌المللی انرژی اتمی متهم کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24749" target="_blank">📅 13:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پولیتیکو:
فرانسه و ترکیه بر سر توافق‌های جدید همکاری ناتو با آذربایجان و ارمنستان به بن‌بست رسیده‌اند.
فرانسه با توافق همکاری با آذربایجان مخالفت کرده و ترکیه در واکنش خواستار تصویب هم‌زمان توافق همکاری با ارمنستان شده است. این توافق‌ها شامل
رزمایش و آموزش نظامی و تقویت همکاری سیاسی و دفاعی
است و بیش از یک سال در ناتو بلاتکلیف مانده‌اند. دیپلمات‌های ناتو هشدار داده‌اند این بن‌بست می‌تواند روند نزدیک‌شدن ارمنستان و آذربایجان به غرب را دشوارتر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/24748" target="_blank">📅 13:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الجزیره  : بر اساس برنامه فعلی، نهایتاً تا پایان نوامبر ( هفته اول آذر ) آمریکا می‌تواند ۳ ناو هواپیمابر و ۲ گروه آبی‌خاکی در اطراف ایران داشته باشد.
البته خبرگزاری آسوشیتدپرس نظرش اواخر اکتبر (هفته اول آبان)است
@WarRoom
⚠️
🚨</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/24747" target="_blank">📅 12:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رویترز: عبور محموله‌های ال‌ان‌جی از تنگه هرمز در سپتامبر به بالاترین میزان از آغاز جنگ رسید. بر اساس داده‌های S&P Global، ۱۹ محموله شامل ۱۳ محموله از قطر و ۶ محموله از امارات از تنگه عبور کردند؛ داده‌های کپلر این رقم را ۲۱ محموله اعلام کرده است. با این حال،…</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/24746" target="_blank">📅 12:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">رویترز:
عبور محموله‌های ال‌ان‌جی از تنگه هرمز در سپتامبر به بالاترین میزان از آغاز جنگ رسید.
بر اساس داده‌های S&P Global، ۱۹ محموله شامل ۱۳ محموله از قطر و ۶ محموله از امارات از تنگه عبور کردند؛ داده‌های کپلر این رقم را ۲۱ محموله اعلام کرده است. با این حال، برخی کشتی‌های قطری برای عبور از منطقه، سامانه ردیابی خودکار خود را خاموش کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.4K · <a href="https://t.me/withyashar/24745" target="_blank">📅 12:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">درگیری مسلحانه میان نیروهای امنیتی رژیم و یک گروه مهاجم در یکی از روستاهای شهرستان راسک در جنوب سیستان‌وبلوچستان رخ داده است. @WarRoom
🚨</div>
<div class="tg-footer">👁️ 99.3K · <a href="https://t.me/withyashar/24744" target="_blank">📅 12:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">درگیری مسلحانه میان نیروهای امنیتی رژیم
و یک گروه مهاجم در یکی از روستاهای شهرستان راسک در جنوب سیستان‌وبلوچستان رخ داده است.
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/24743" target="_blank">📅 12:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57b1f32b3.mp4?token=h24vERQl7W8o6uVhCuOnCceYDsKHKzWQdsPcoxNvbgXZxYOjbwur4yY7xtdAL_eW5D28czKPqlD-IKoK-idvcxeiEoiRm0KUw6SmANZoc1HCpdUyK-FyQnkgkHaon9nHUdna-nQaFtM2MyJMolifEQxKa4RMJi6roaF9ocX41fCumPCknhhmlY5bKwGghrWUFCRF1iYSzVWshkqm7K3-D-7qjrbZpmjNSGqLzHQXs-IZR8xIHTNN22KX5SEliwK2_W8NhCIRbHTsP45l83tZeFxIG7HfqNi_OrUTs-gfZilfCDXsmGtBOUf_6nrPJClP9xFxJvl1q1K2OYHFEV1W-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57b1f32b3.mp4?token=h24vERQl7W8o6uVhCuOnCceYDsKHKzWQdsPcoxNvbgXZxYOjbwur4yY7xtdAL_eW5D28czKPqlD-IKoK-idvcxeiEoiRm0KUw6SmANZoc1HCpdUyK-FyQnkgkHaon9nHUdna-nQaFtM2MyJMolifEQxKa4RMJi6roaF9ocX41fCumPCknhhmlY5bKwGghrWUFCRF1iYSzVWshkqm7K3-D-7qjrbZpmjNSGqLzHQXs-IZR8xIHTNN22KX5SEliwK2_W8NhCIRbHTsP45l83tZeFxIG7HfqNi_OrUTs-gfZilfCDXsmGtBOUf_6nrPJClP9xFxJvl1q1K2OYHFEV1W-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گشت‌وگذار یک دانشجوی عراقی با خودروی آمریکایی دوج چارجر در همدان، در حالی که تصویر تروریستها؛ علی خامنه‌ای، قاسم سلیمانی و ابومهدی المهندس (جمال جعفر محمدعلی آل‌ابراهیم، معاون پیشین حشدالشعبی عراق) روی بدنه آن نقش بسته است.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24742" target="_blank">📅 11:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd60bc703d.mp4?token=PzB_4jDcGlSF2k7S7howBAohAjO6QEdLDnfo43UybFLAxpBPQIBMf9s1P8TAnUNd0GGx0OxMVODF34L-D8b58z-XmaWzezdsj-PecM4AiUdKl0nWCTCSP0SuuLzvrrF2eulZLjXMKr45_KtdOom2Yi-7hF9-LVFB8tvyKHknfuZ_9VGK4qjDzn9DFV6uuy9ZiR6mChrzr0YDHfofy48l-pZyAOGTVpWcbwMAUR4nPrsZkRCeizpLVa9q2y-0JCgkzuhbz5-b9qkMlf9LGEUv3iM1m-Vn42EyT2JW4z5l91kETQ3UI3Ci-ns6k0v7j7a6ecLJPWGSQQBRsgBDtmKcUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd60bc703d.mp4?token=PzB_4jDcGlSF2k7S7howBAohAjO6QEdLDnfo43UybFLAxpBPQIBMf9s1P8TAnUNd0GGx0OxMVODF34L-D8b58z-XmaWzezdsj-PecM4AiUdKl0nWCTCSP0SuuLzvrrF2eulZLjXMKr45_KtdOom2Yi-7hF9-LVFB8tvyKHknfuZ_9VGK4qjDzn9DFV6uuy9ZiR6mChrzr0YDHfofy48l-pZyAOGTVpWcbwMAUR4nPrsZkRCeizpLVa9q2y-0JCgkzuhbz5-b9qkMlf9LGEUv3iM1m-Vn42EyT2JW4z5l91kETQ3UI3Ci-ns6k0v7j7a6ecLJPWGSQQBRsgBDtmKcUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آکسیوس: به نقل از یک مقام آمریکایی گزارش داد که گروه آماده اعزام آبی‌خاکی Makin Island و یگان اعزامی تفنگداران دریایی آمریکا (MEU) سیزدهم، پایگاه دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند و انتظار می‌رود تا پایان نوامبر به منطقه…</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24741" target="_blank">📅 11:14 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ: ایران رادارهای پیشرفته‌ای ندارد و گاهی اوقات سعی می‌کند مین‌های دریایی کار بگذارد، اما ما معمولاً آنها را قبل از اینکه بتوانند مستقر شوند، از بین می‌بریم.
@WarRoom</div>
<div class="tg-footer">👁️ 97.3K · <a href="https://t.me/withyashar/24740" target="_blank">📅 10:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رویترز:
نیروهای دولت رسمی یمن اعلام کردند طی حدود سه ساعت،
۲۰ حمله هوایی
علیه مواضع، نیروها، خودروها و تجهیزات نظامی حوثی‌هادر استان تعز انجام داده‌اند. این درگیری‌ها یکی از شدیدترین تشدیدهای نبرد میان نیروهای مورد حمایت عربستان و حوثی‌های مورد حمایت ایران از زمان آتش‌بس ۲۰۲۲ محسوب می‌شود. حدود
۱۹ جاده منتهی به استان تعز
نیز به دلیل درگیری‌ها بسته و مناطق اطراف آنها منطقه عملیاتی نظامی اعلام شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24739" target="_blank">📅 10:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نیویورک‌تایمز: به نقل از یک مقام امنیتی غربی گزارش داد که ایران حدود
۱۰ موشک کروز ضدکشتی و ۳۰ پهپاد
به سمت تنگه هرمز شلیک کرده است. به گفته این مقام،
۴ نفتکش هدف قرار گرفته‌اند
؛ هرچند آمار فعلی سازمان عملیات تجارت دریایی بریتانیا (UKMTO)
۱۳ مورد
است. جنگنده‌ها و بالگردهای تهاجمی آمریکا برای مقابله با حملات ایران در آسمان تنگه هرمز فعال هستند، با این حال
برخی پرتابه‌ها همچنان به کشتی‌ها اصابت می‌کنند
.
@WarRoom</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/withyashar/24738" target="_blank">📅 10:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آکسیوس: به نقل از یک مقام آمریکایی گزارش داد که
گروه آماده اعزام آبی‌خاکی Makin Island
و
یگان اعزامی تفنگداران دریایی آمریکا (MEU) سیزدهم
، پایگاه دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند و انتظار می‌رود
تا پایان نوامبر
به منطقه برسند. این گروه شامل ناو تهاجمی آبی‌خاکی
USS Makin Island
از کلاس Wasp، ناو ترابری آبی‌خاکی
USS Anchorage
از کلاس San Antonio و ناو ترابری آبی‌خاکی
USS John P. Murtha
از همین کلاس است. این نیروها
۱۰ فروند جنگنده F-35B Lightning II
و حدود
۲۲۰۰ تفنگدار دریایی آمریکا
را به منطقه خواهند آورد.
@WarRoom</div>
<div class="tg-footer">👁️ 99.4K · <a href="https://t.me/withyashar/24737" target="_blank">📅 10:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">آکسیوس: به نقل از دو مقام آمریکایی و یک منبع در غرب آسیا گزارش داد که آمریکا برای حفاظت از زیرساخت‌های نفت و گاز،
یک سامانه پدافند هوایی MIM-104 پاتریوت
به قطر و یک سامانه نیز به عربستان سعودی ارسال کرده است. بر اساس این گزارش، یک سامانه پاتریوت در
یک تأسیسات کلیدی نفتی در عربستان سعودی
و یک سامانه دیگر در
یک تأسیسات گاز طبیعی در قطر
مستقر شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/24736" target="_blank">📅 10:11 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3218939c94.mp4?token=NeeGq2BWz3xAqjcUO2KHTrddVsLWiIUYmbVc3kbU6SMNGafgMXiKxIohkAhOT9l-lJjsWmvTy8vrht7-IjO43VxW5U97Zws-SNvudRxIPPggRkh2moXW0z1RZe4o2VvIN50nKZicyxVznLv47Pr1XoILCHtlJ61SwLIBLFCN-X27th-ZLr_bre8gFPIVEq5QxE49ONLCTYVIzwUlE44L9ps4Ie3lfsJZXxiuZ9M8zrM9mCOef41R_7togYDdyMNswIDiUb5kpIi2_-BR7mjwrBV-B88l__YsQgFnOwA51IAGpo72Nr1__KZrwFhWFrOJfEpykRHwzVEIH89XybcBwwgRXgKDZGSuHADH9McCKvpyMWRLMF3yJPixclVUN534XxHWLrAkFI2Zx31AaZLmj7QNpSkZ5899-BGakpxiVTcRxnaaipOyX2x2Wn5tHPIxp8lze6SaJc1EaPIJzESViOvkeBIm3pEUfMEB37OG8faaa8H4hdoRzTV3L3GFOpJVCDeD3gNjq3XUCneiVHigF8ilPETjnGky7cgIYGG6_Pn27IQ6sSMIX5rbRUlhv0xy8IF7SjKYF69DTOgsyBUXAIG7lvq_IODxC-urDgRhvuOH3yTCLjHY9XUma9X_EQDXG7hID7qpN7zLyRSLS3clNhVBWq5PDwmPlRytneaULD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3218939c94.mp4?token=NeeGq2BWz3xAqjcUO2KHTrddVsLWiIUYmbVc3kbU6SMNGafgMXiKxIohkAhOT9l-lJjsWmvTy8vrht7-IjO43VxW5U97Zws-SNvudRxIPPggRkh2moXW0z1RZe4o2VvIN50nKZicyxVznLv47Pr1XoILCHtlJ61SwLIBLFCN-X27th-ZLr_bre8gFPIVEq5QxE49ONLCTYVIzwUlE44L9ps4Ie3lfsJZXxiuZ9M8zrM9mCOef41R_7togYDdyMNswIDiUb5kpIi2_-BR7mjwrBV-B88l__YsQgFnOwA51IAGpo72Nr1__KZrwFhWFrOJfEpykRHwzVEIH89XybcBwwgRXgKDZGSuHADH9McCKvpyMWRLMF3yJPixclVUN534XxHWLrAkFI2Zx31AaZLmj7QNpSkZ5899-BGakpxiVTcRxnaaipOyX2x2Wn5tHPIxp8lze6SaJc1EaPIJzESViOvkeBIm3pEUfMEB37OG8faaa8H4hdoRzTV3L3GFOpJVCDeD3gNjq3XUCneiVHigF8ilPETjnGky7cgIYGG6_Pn27IQ6sSMIX5rbRUlhv0xy8IF7SjKYF69DTOgsyBUXAIG7lvq_IODxC-urDgRhvuOH3yTCLjHY9XUma9X_EQDXG7hID7qpN7zLyRSLS3clNhVBWq5PDwmPlRytneaULD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره عملیات«چکش نیم شب»: بمب‌افکن‌های ما از میزوری پرواز کردند، رفتند و برگشتند؛ ۳۷ ساعت در مسیر بودند و سوخت‌گیری می‌کردند. ساعت یک صبح، وقتی ماه نبود و هوا کاملاً تاریک بود، همه بمب‌ها را رها کردند و مستقیم رفتند پایین، روی این «کارخانه‌های مواد مخدر»… بمب‌ها مستقیماً از مسیرهای هوایی به داخل این، اِمم، کارخانه‌های مواد مخدر رفتند؛ واقعاً همین کاری بود که آنها انجام می‌دادند. آنها هسته‌ای و مواد مخدر بودند. آنها مواد مخدر تولید می‌کردند. این کارخانه‌های مواد مخدر/هسته‌ای به‌شدت هدف قرار گرفتند.»
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/24735" target="_blank">📅 10:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بیانیه وزارت امور خارجه ایران: تهران
محدودیت‌های اعمال‌شده بر تردد هوایی میان ایران و عراق
را محکوم کرد و مغایر با منافع و مصالح مشترک دو کشور دانست و اعلام کرد این محدودیت‌ها برای
هزاران مسافر، زائر، بیمار و دانشجو
مشکل ایجاد کرده است. ایران همچنین خواستار
رفع محدودیت‌ها و بازگشت پروازهای دو کشور به شرایط عادی
شد.
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/24734" target="_blank">📅 09:44 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">ترامپ: ما نمی‌خواهیم ایران را در هرج‌ومرج رها کنیم و بعد رئیس‌جمهور دیگری بیاید که شاید کاری را که ما انجام دادیم، انجام ندهد. رئیس‌جمهورهای قبلی باید خیلی وقت پیش به ایران رسیدگی می‌کردند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24733" target="_blank">📅 09:40 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزارت دادگستری آمریکا:
اشتون حامد الابودی، مهندس برق ۵۱ ساله و کارمند وزارت انرژی آمریکا، به اتهام تلاش برای ارائه حمایت مادی به
انصارالله یمن
( حوثی‌های تحت حمایت ایران ) بازداشت شد. او متهم است برای ارتقای ارتباطات این گروه، تهیه تجهیزات پهپادی و قطعات ساخت مواد منفجره اقدام کرده است. تحقیقات از دسامبر ۲۰۲۴ آغاز شد و در سپتامبر ۲۰۲۵، الابودی به مناطق تحت کنترل انصارالله در یمن سفر کرد. او همچنین با یک منبع محرمانه FBI که خود را عضو انصارالله معرفی کرده بود، درباره
ادغام سامانه‌های ارتباطی و راه‌اندازی یک مرکز ارتباطات سیار
همکاری و برای تهیه تجهیزات آن کمک کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24732" target="_blank">📅 02:33 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/24731" target="_blank">📅 02:29 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">😥</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24730" target="_blank">📅 02:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ درباره جنگ با ایران: شاید پیش از انتخابات پیروز شویم... آن‌ها موشک‌هایی دارند، اما ما می‌توانیم از پسِ آن برآییم. ما می‌توانیم از پسِ آن برآییم. آن‌ها موشک‌هایی دارند، اما تعداد بسیار کمی از آن‌ها باقی مانده است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24729" target="_blank">📅 02:16 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68630ecc4a.mp4?token=L1zFjwPxcfFx8uT6Om9Aedf6521bXXskimj_4zgYNzdj5j941GMF3WB67DeuZqoKhElhNp16ALD36SCe7OIWMyixIBwmMIH8Ni3qkYdNgv_ZzloObTutLU4YZ-prBFGVzCmzfdozB7ls6yT9Q5G8LZjun31_L-EeklCvvluZb9but9qmM9FwI6EneIcnWSr-tZyYpKEsei7PAF1WWUNY_dkK50ZhV7q5QaELMiUutr8lt_NWO0FgQ4HI0WzlYz7jrI6v1xXe_Cz_qDrHpx8M2uhP-K7FLmjszFX7aNrR8aVTQskIi429UmDZT8ZlKWoAWzKeGnTfCDEt1ErNezjACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68630ecc4a.mp4?token=L1zFjwPxcfFx8uT6Om9Aedf6521bXXskimj_4zgYNzdj5j941GMF3WB67DeuZqoKhElhNp16ALD36SCe7OIWMyixIBwmMIH8Ni3qkYdNgv_ZzloObTutLU4YZ-prBFGVzCmzfdozB7ls6yT9Q5G8LZjun31_L-EeklCvvluZb9but9qmM9FwI6EneIcnWSr-tZyYpKEsei7PAF1WWUNY_dkK50ZhV7q5QaELMiUutr8lt_NWO0FgQ4HI0WzlYz7jrI6v1xXe_Cz_qDrHpx8M2uhP-K7FLmjszFX7aNrR8aVTQskIi429UmDZT8ZlKWoAWzKeGnTfCDEt1ErNezjACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«
ایران در فوریه ۲۰۲۶، تنها سه تا چهار هفته با دستیابی به سلاح هسته‌ای فاصله داشت؛ شاید هم زودتر
»
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/24728" target="_blank">📅 02:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4cb6b4532.mp4?token=VsTXEa2Iep8HgI7KLfiFjyMXAsdZXzb9qzUOAVp8CP61L6h1Pv5D3HO81BcQqaf3hmQJzoMJBNm__4lUXufXcwwCsBlRXBmgM-w5hir8cpQ58YbwgezJX1UNNIfMNVng6n7gnPSE0Hac0X7s6zPe6P0tofoccvbvUEdUfNsJKskQQZS9tX7I63OeoXhYA9C3JNZpEisJ5EwBj0iRrJXPaVB5TZt4zy5EbKika-ouacCIA7SYypeP44Btqj8-vL-TZ4Hi2uGve-WLCZsGi3rhWfwgd9Vn3ok2B_2SFvPRkmS3JtZhJ24NT0PhlnPae0WoPVzpOGnAjHUxV2eCSds20Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4cb6b4532.mp4?token=VsTXEa2Iep8HgI7KLfiFjyMXAsdZXzb9qzUOAVp8CP61L6h1Pv5D3HO81BcQqaf3hmQJzoMJBNm__4lUXufXcwwCsBlRXBmgM-w5hir8cpQ58YbwgezJX1UNNIfMNVng6n7gnPSE0Hac0X7s6zPe6P0tofoccvbvUEdUfNsJKskQQZS9tX7I63OeoXhYA9C3JNZpEisJ5EwBj0iRrJXPaVB5TZt4zy5EbKika-ouacCIA7SYypeP44Btqj8-vL-TZ4Hi2uGve-WLCZsGi3rhWfwgd9Vn3ok2B_2SFvPRkmS3JtZhJ24NT0PhlnPae0WoPVzpOGnAjHUxV2eCSds20Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره اروپا:
«به آنچه برای
اروپا اتفاق افتاده
نگاه کنید. آنها دارند
زنده‌زنده خورده می‌شوند
.»
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24727" target="_blank">📅 02:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65aa2c1d6.mp4?token=ugpfaQqCJj_4OkzGbjq74SwMnxxmcogpfoQaupJJnNM3z4vKCxJxv9aEsxU7sRXnKRKjcG4Ok0qTaOg3bTyhFnjLdRFo-gWXnIrgyQ8hLE422kKRoq2lStEJ27lwvGh1eztdZfR5_lk6FbPnj_TQrgN8biaM9nmR35BT9pf-4XmMxgBSGpYURbYoKcjTGtp3zpm0VSfM6y_n3pwEXEzKl8G-k3Mi-1ek9Mr2vQWAnr_z-NtVyhfekM6fkmnWthkFfYsT1D_beFwvAlBlYVo48F1lQnHG1CKg7rSL0zzO_iBvbDu5foJnFrvh2UmgnQKKBQc350fE1kenjDhPkT6ATA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65aa2c1d6.mp4?token=ugpfaQqCJj_4OkzGbjq74SwMnxxmcogpfoQaupJJnNM3z4vKCxJxv9aEsxU7sRXnKRKjcG4Ok0qTaOg3bTyhFnjLdRFo-gWXnIrgyQ8hLE422kKRoq2lStEJ27lwvGh1eztdZfR5_lk6FbPnj_TQrgN8biaM9nmR35BT9pf-4XmMxgBSGpYURbYoKcjTGtp3zpm0VSfM6y_n3pwEXEzKl8G-k3Mi-1ek9Mr2vQWAnr_z-NtVyhfekM6fkmnWthkFfYsT1D_beFwvAlBlYVo48F1lQnHG1CKg7rSL0zzO_iBvbDu5foJnFrvh2UmgnQKKBQc350fE1kenjDhPkT6ATA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«آنها یا
کاری کاملاً درست و عاقلانه انجام خواهند داد
، یا
برای مدت زیادی دوام نخواهند آورد
.
وقتی با آنها
توافقی انجام می‌دهید
، این احتمال بسیار زیاد است که
به آن پایبند نمانند
.»
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/24726" target="_blank">📅 01:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24725">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9d52bcff0.mp4?token=qY3D1nXAKc0LIecOQoodTW0GTojL2nVUGME5Vd1cbIPnKrUa_7eVrUCcsebBJ-crUweKN7kMWYXYvsdUlEkgoQfeje32qtP3vZYvKlZ0w7Mf8aFKLsBjhYHaHyeegdGos_T6zOEmBpU_Vf8c41SJ4j8CD3W2IJoRbLChlR2cgiKtwW5AYrWQQVlwl-l0D-UiiwXpIyOked_EXF38guGD1c0ifLVnDGOyu0IAeeMlCQxBlJyH3OiVCpKQO4LG9Ehni4q8XXpLfaoxFOKcRnH8UJ9fk0rl8qSK9imxkrKt3Lxad6awZuBmCo52LayNWAbvKwEneFTAV0g6udy7fJ0ZOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9d52bcff0.mp4?token=qY3D1nXAKc0LIecOQoodTW0GTojL2nVUGME5Vd1cbIPnKrUa_7eVrUCcsebBJ-crUweKN7kMWYXYvsdUlEkgoQfeje32qtP3vZYvKlZ0w7Mf8aFKLsBjhYHaHyeegdGos_T6zOEmBpU_Vf8c41SJ4j8CD3W2IJoRbLChlR2cgiKtwW5AYrWQQVlwl-l0D-UiiwXpIyOked_EXF38guGD1c0ifLVnDGOyu0IAeeMlCQxBlJyH3OiVCpKQO4LG9Ehni4q8XXpLfaoxFOKcRnH8UJ9fk0rl8qSK9imxkrKt3Lxad6awZuBmCo52LayNWAbvKwEneFTAV0g6udy7fJ0ZOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
« کسی حاظر نیست آنجا رئیس جمهور شود ، رؤسای‌جمهور ایران
دیگر در کنار ما نیستند
، اما ما تلاش می‌کنیم با
فرد فعلی
با ملایمت برخورد کنیم.
(منظورش رهبر هست)
بالاخره در مقطعی باید
با یک نفر وارد مذاکره و تعامل شویم
، درست است؟»
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/24725" target="_blank">📅 01:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24724">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eaaf7693d.mp4?token=jnIqI68v-6O5RZ_W-mMSsV0JGJdCNuaYhp0oLUoXOZnOO4UVtGVL9-IHPxWpZ1C0P5IvknpLGpk3AoKm7X88gGWalLeduw22FCXEXTF-y-DJF0AXGM25lUNe-m5GSljOp8ajlfTDSHbE23kNIRdzrSKPLjD21pIP53s386wGjAGHrWjm9Y-IssVH9i9HTW2v-gRl7yEvKpRVXIkB59OsCX_zAXLE1c2tffsqsDToJbPipNDip6UQEVGCM23zoW8eGk2DX9hdZX-8xRhJPGbrbAw33b9e-Icr3fkPD2f2gyHsMbdv_WVhyOiKxDZ6LYM4LKg9_ZZ4zL1S5gTNk8Af04WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eaaf7693d.mp4?token=jnIqI68v-6O5RZ_W-mMSsV0JGJdCNuaYhp0oLUoXOZnOO4UVtGVL9-IHPxWpZ1C0P5IvknpLGpk3AoKm7X88gGWalLeduw22FCXEXTF-y-DJF0AXGM25lUNe-m5GSljOp8ajlfTDSHbE23kNIRdzrSKPLjD21pIP53s386wGjAGHrWjm9Y-IssVH9i9HTW2v-gRl7yEvKpRVXIkB59OsCX_zAXLE1c2tffsqsDToJbPipNDip6UQEVGCM23zoW8eGk2DX9hdZX-8xRhJPGbrbAw33b9e-Icr3fkPD2f2gyHsMbdv_WVhyOiKxDZ6LYM4LKg9_ZZ4zL1S5gTNk8Af04WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره ایران:
«ایران
آماده تسلیم شدن است
. ما همین حالا می‌توانیم
خیلی راحت پیروز شویم.
»
من یقین دارم درست بعد از انتخابات ، شاید هم قبلش
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24724" target="_blank">📅 01:50 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ویولن بیژن در قم فعال شد
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24723" target="_blank">📅 00:28 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a86dcf7b.mp4?token=oeJgOD4y7fwGvyE-lHKsPIUlxt5cXoV5NgAkYS88Tk2_968bADAIyK4gqDXMf6UMf0QK-xw_Ka5SaUvutmi3yGFsi3QyakWWml3iwxhFK6bWTXjofCndNp3-VUrbQoEE0uOXewXRlU2i_bdwjUjhubNdtLwlq24bURSoTOWHgzvTnK56R4tyaxqyl5AJEH-CE_5TC94mhkF4tqwXk4cd7VAT4DUJTlAtUTbaJEbJCjFI4FSm7e54WD0obIPumTxStN9Syk-u230ORN4Z1uuRF5dsy28K3IN9t9j7DL-7jGFBZT8P6WrWcpMt-1LXcgmtROOD7Sisg-z6T2ViDoB-Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a86dcf7b.mp4?token=oeJgOD4y7fwGvyE-lHKsPIUlxt5cXoV5NgAkYS88Tk2_968bADAIyK4gqDXMf6UMf0QK-xw_Ka5SaUvutmi3yGFsi3QyakWWml3iwxhFK6bWTXjofCndNp3-VUrbQoEE0uOXewXRlU2i_bdwjUjhubNdtLwlq24bURSoTOWHgzvTnK56R4tyaxqyl5AJEH-CE_5TC94mhkF4tqwXk4cd7VAT4DUJTlAtUTbaJEbJCjFI4FSm7e54WD0obIPumTxStN9Syk-u230ORN4Z1uuRF5dsy28K3IN9t9j7DL-7jGFBZT8P6WrWcpMt-1LXcgmtROOD7Sisg-z6T2ViDoB-Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری سان : پلیس ضدتروریسم بریتانیا یک شهروند ۲۷ ساله ایرانی سیتیزن بریتانیا را به ظن آماده‌سازی اقدامات تروریستی و ارتباط با توطئه برای هدف قرار دادن پایگاه هوایی RAF Fairford دستگیر کرد. یک مرد ۲۶ ساله بریتانیایی نیز تحت بازجویی قرار گرفته و دو ملک در…</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/24722" target="_blank">📅 00:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">رویترز:
قیمت نفت بیش از
۴ دلار در هر بشکه
افزایش یافت؛ پس از اعلام اعزام
سومین ناو هواپیمابر آمریکا
و تا
۱۰ هزار نیروی اضافی
به خاورمیانه، همزمان با توقف صادرات فرآورده‌های نفتی چین به خارج از هنگ‌کنگ و ماکائو، نگرانی‌ها درباره
کمبود جهانی سوخت
افزایش یافت.همزمان، محدودیت‌های صادرات گازوئیل از سوی
روسیه و چین
و تحولات مرتبط با ایران، فشار بیشتری بر بازار سوخت وارد کرده است.
قرارداد دسامبر نفت برنت با
۴.۳۷٪ افزایش
در
۱۰۲.۳۱ دلار
بسته شد. همچنین گزارش‌ها از
هدف قرار گرفتن سه نفتکش با پرچم لیبریا در تنگه هرمز
حکایت دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24721" target="_blank">📅 23:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WL5EdV2wd_kAxy0zr5rS1zzA_L2mUtDE6ZX88udhI9Ihmq32nHVeVvz0vSRkpg04WC6Ldhczss9nupft3IwgPCyDGsRhFy_w5wub978tcBlabypf87LB3C37V2byRnTuoqrWpbFZdQ13jb-ze1HN8asbKVDh1LuYiKgEfjstgtgeV_ZV9JiPcujZM34iU2zTM2XjybW-OuKCMfYhUeNnUocKdtcmulaNoXOthHoXufKWqybG_7X6N6RLp8t0xHiQlRqeaaoDoahcfLdeu3RZyrUWXYu8XM8569Q_XgKzm9YLJW7BUlRQgYILNiPFx4aDY_zgXW49jT4VMLsRqxuGWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجرات دریایی بریتانیا
:
یک نفتکش هنگام عبور از
تنگه هرمز
با یک پرتابه ناشناس برخورد کرده و در پی آن دچار آتش‌سوزی شده است. این گزارش از سوی یک منبع ثالث دریافت شده و
خدمه سالم هستند
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24720" target="_blank">📅 23:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">فاکس‌نیوز: ژنرال بازنشسته جک کین، تحلیلگر ارشد راهبردی این شبکه،
آغاز عملیات نظامی جدید پیش از انتخابات میان‌دوره‌ای آمریکا(۱۲ آبان) وجود دارد.
کین گفت ترامپ در حال بررسی زمان‌بندی چنین اقدامی است و عملیات می‌تواند پیش از انتخابات یا پس از آن آغاز شود. او همچنین گفت
عملیات مخفی موساد علیه ایران در حال انجام است.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/24719" target="_blank">📅 23:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacacbd314.mp4?token=fxmcHPIj9polNRKb-bJeiMAQGVRbssDnySi7ZZcl7XUXIhpJgJldgqIIsDbZAGhPAaslt5qF6cxSIlETAgCb1SraBHvQZBCk70J0GXcUEFFaBKXVuhNy7sUkjWM-LM3zxZRvzDUCWhhycRdu25vug5eg1HyEPYVyx_AALCKR9E3N9nosJFCL9g2_SOROZYb1obvp6dMWnDQNMnHlybqt2MaS2rW_xcvNaXsoOZ4FyU3vE7f63Fx0Mi8e9wN5SlqajdhVPz3ZCwpYmbm2nyRX-UH6KSAJQhbevKndrDen0aqckBlfYLN1cgbN7uEXFMW4ErF0L-_qd6n2CS5mpOix9Jk1fx-ENkdYI9-nx7UszgIk3sCliLcDOfs5431PtYXrDxa_AVqMXxs5_KcHtdUkueVjyHxTprsdfrZwzk_y3fjanLsEw5XoByZkEh79iz3ZN9D7zbz-xfuP6DjTaGRC3dPQQGpwmVoWeNMwlwnjtePEk65ih1xXEAawoKcrM48oPldvJNTeG9YNDI1hCYyQ_L7VORazVXVub-s8dl5Fyvdp8ALyi8WN940Y-jaSBD-bL3pGWCskK0iQVvyC0PP0GX8Z5WQ1WiqFQXDUBwsagnH4AifPrX_7fAFGoumxXZ3neK0RpknuqB27U_Cb6GdjRsY-qhzVu5C67m3UuPGl1pc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacacbd314.mp4?token=fxmcHPIj9polNRKb-bJeiMAQGVRbssDnySi7ZZcl7XUXIhpJgJldgqIIsDbZAGhPAaslt5qF6cxSIlETAgCb1SraBHvQZBCk70J0GXcUEFFaBKXVuhNy7sUkjWM-LM3zxZRvzDUCWhhycRdu25vug5eg1HyEPYVyx_AALCKR9E3N9nosJFCL9g2_SOROZYb1obvp6dMWnDQNMnHlybqt2MaS2rW_xcvNaXsoOZ4FyU3vE7f63Fx0Mi8e9wN5SlqajdhVPz3ZCwpYmbm2nyRX-UH6KSAJQhbevKndrDen0aqckBlfYLN1cgbN7uEXFMW4ErF0L-_qd6n2CS5mpOix9Jk1fx-ENkdYI9-nx7UszgIk3sCliLcDOfs5431PtYXrDxa_AVqMXxs5_KcHtdUkueVjyHxTprsdfrZwzk_y3fjanLsEw5XoByZkEh79iz3ZN9D7zbz-xfuP6DjTaGRC3dPQQGpwmVoWeNMwlwnjtePEk65ih1xXEAawoKcrM48oPldvJNTeG9YNDI1hCYyQ_L7VORazVXVub-s8dl5Fyvdp8ALyi8WN940Y-jaSBD-bL3pGWCskK0iQVvyC0PP0GX8Z5WQ1WiqFQXDUBwsagnH4AifPrX_7fAFGoumxXZ3neK0RpknuqB27U_Cb6GdjRsY-qhzVu5C67m3UuPGl1pc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : ناو یو‌اس‌اس جورج واشنگتن (CVN 73) در حین حرکت در آب‌های منطقه‌ای خاورمیانه، عملیات پروازی انجام می‌دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24718" target="_blank">📅 23:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترابری نظامی خیره‌کننده و عجیب آمریکا از ۲۴ ساعت گذشته تا همین لحظه… @WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/24717" target="_blank">📅 22:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24716">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b502de34b9.mp4?token=qnnvJ422C3ZNyV3UMrSvfUGFx1Uk1WXuaP2h3k9bdA3LSIUwECWi7930fHnmCsDZZPSkFq6A6hxXllbkmvfYTQWDvpqOIeBDCXaCyYnseXEUKJzKkMMkjbvuMRVKPbFcFYG3arjcbeJ-hBbBIdbSDBIeVyQtaMxgIdgaQW1t7gTKyjzHjPZ3kQbxiuWwFOADKjzJR1UQGMCWmdpgKP1ngWVquZb9JPATJYehEX0rhD8PF-Bhhhe9TgGfbkPueMlbFtkuZMVPBszc4YmISKLzfyhFmSqA_K2X8Wi-oQPYfe9MzRuSnezT6h3W3jTTimbmeqgUsrmzoli0y12Cnh6VwSQwc8JacyhNDWMBNQVpvEoT8-riy48LbP6OlT2cT8IQmcE-0r2mmjPHaSDQ_nu9GwNs-OBh5uXmd9scyfDkS2jokXXxNyuTfUtzGo5lY6YrgtWrfrOEWXPdFnW2Gpq-ZhAijgcV0O4drTJejsRW8bB5fcFc5gczz2IqqHmXaosBZujJnHNrCaFa32htJn9Y81j1wKl502O9CiyEkVZJJe4BxRgTGAnT1FtMB71G3LzdevBbB4fNTojyyy4UtbQi1ZcMQQ17338QvYSBwa-2naEyvtbIaQe5pQ14hFulxRQAxgV4_yLvdM9nome3Ml1GuatLoBM1mXzthLpIdyZe_iM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b502de34b9.mp4?token=qnnvJ422C3ZNyV3UMrSvfUGFx1Uk1WXuaP2h3k9bdA3LSIUwECWi7930fHnmCsDZZPSkFq6A6hxXllbkmvfYTQWDvpqOIeBDCXaCyYnseXEUKJzKkMMkjbvuMRVKPbFcFYG3arjcbeJ-hBbBIdbSDBIeVyQtaMxgIdgaQW1t7gTKyjzHjPZ3kQbxiuWwFOADKjzJR1UQGMCWmdpgKP1ngWVquZb9JPATJYehEX0rhD8PF-Bhhhe9TgGfbkPueMlbFtkuZMVPBszc4YmISKLzfyhFmSqA_K2X8Wi-oQPYfe9MzRuSnezT6h3W3jTTimbmeqgUsrmzoli0y12Cnh6VwSQwc8JacyhNDWMBNQVpvEoT8-riy48LbP6OlT2cT8IQmcE-0r2mmjPHaSDQ_nu9GwNs-OBh5uXmd9scyfDkS2jokXXxNyuTfUtzGo5lY6YrgtWrfrOEWXPdFnW2Gpq-ZhAijgcV0O4drTJejsRW8bB5fcFc5gczz2IqqHmXaosBZujJnHNrCaFa32htJn9Y81j1wKl502O9CiyEkVZJJe4BxRgTGAnT1FtMB71G3LzdevBbB4fNTojyyy4UtbQi1ZcMQQ17338QvYSBwa-2naEyvtbIaQe5pQ14hFulxRQAxgV4_yLvdM9nome3Ml1GuatLoBM1mXzthLpIdyZe_iM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولادیمیر پوتین: پیشنهاد انتقال اورانیوم غنی‌شده ایران به روسیه ارائه شده و این پیشنهاد
همچنان کاملاً روی میز است
. اما سپس آمریکا موضع خود را سخت‌تر کرد و گفت انتقال اورانیوم تنها باید به آمریکا انجام شود. از آنجا بود که ایران نیز تصمیم گرفت موضع خود را سخت‌تر کند.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24716" target="_blank">📅 22:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بلومبرگ:
عباس عراقچی، وزیر امور خارجه ایران،بطور غیر علنی پیشنهاد داده است که تهران در ازای
کاهش تحریم‌ها، دسترسی بازرسان آژانس بین‌المللی انرژی اتمی به تمامی تأسیسات هسته‌ای آسیب‌دیده ایران را از سر بگیرد
. این پیشنهاد در چارچوب تلاش‌های دیپلماتیک برای دستیابی به توافق میان ایران و آمریکا مطرح شده است
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/24715" target="_blank">📅 22:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24714" target="_blank">📅 22:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/24713" target="_blank">📅 22:08 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">گزارش زیاد از ایست بازرسی های پی در پی در شهر های ایران مخصوصا کرج
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24712" target="_blank">📅 21:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24711">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">(پدافند) بیژنه غرب ایران کرمانشاه فعال شد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/24711" target="_blank">📅 21:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60239b6687.mp4?token=d-4INJOiAgCu3rRX9mfL8Ca792LN28UNSi5r28MyoyQql2YCj4PQbsxUJRp5fEpBo7njUXZe4R-xZYm6HfN2H71dN1cuPVUIzY3pZ6U-lmgxqRRPinTqB2i8UTEBW4QtCwbUBgRiJuPMlzB6s_NU2zUzmHN6TG44YTuiLq4G-F48q28njJl7NIHFHPDvOzOVHffHblojtoNOSjzG9dGVPTK6N11biwKDk3DpVp1Oy-EXC_yvrKqp9n1PVexmjgNI214VlC-M_vbXsxDG6BegvEJVD-V_tQuois1N0h96Sk1WmDpEL6tmmos2zpoPLrzkrEHxnOA4iaYr6me5hkyU7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60239b6687.mp4?token=d-4INJOiAgCu3rRX9mfL8Ca792LN28UNSi5r28MyoyQql2YCj4PQbsxUJRp5fEpBo7njUXZe4R-xZYm6HfN2H71dN1cuPVUIzY3pZ6U-lmgxqRRPinTqB2i8UTEBW4QtCwbUBgRiJuPMlzB6s_NU2zUzmHN6TG44YTuiLq4G-F48q28njJl7NIHFHPDvOzOVHffHblojtoNOSjzG9dGVPTK6N11biwKDk3DpVp1Oy-EXC_yvrKqp9n1PVexmjgNI214VlC-M_vbXsxDG6BegvEJVD-V_tQuois1N0h96Sk1WmDpEL6tmmos2zpoPLrzkrEHxnOA4iaYr6me5hkyU7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در‌تروث پستی از اعتراضات ایران منتشر کرد که مردم در آن شعار میدهند «امسال سال خونه سید علی سرنگونه»
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/24710" target="_blank">📅 21:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24709" target="_blank">📅 21:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا: تحریم‌های جدید علیه ایران، بخش‌های خودروسازی و راه‌آهن و شبکه‌های تأمین‌کننده و حامی آنها را هدف قرار می‌دهد و با هدف خشکاندن منابع مالی جمهوری اسلامی اعمال شده است. وزارت خزانه‌داری آمریکا امروز ایران‌خودرو و سایپا و همچنین…</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/24708" target="_blank">📅 21:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وال‌استریت ژورنال:
دونالد ترامپ به دستیاران خود گفته است که انتظار دارد
پس از انتخابات میان‌دوره‌ای نوامبر، بمباران ایران از سر گرفته شود.
مقام‌های آمریکایی می‌گویند هنوز مشخص نیست حملات احتمالی در چه ابعادی انجام خواهد شد. در همین حال، آمریکا در حال تقویت نیروهای نظامی خود در منطقه است و یک گروه ناو هواپیمابر دیگر نیز در راه خاورمیانه است.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/24707" target="_blank">📅 21:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24706">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">BTC 85000$
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24706" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24705">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مقام اماراتی به کانال ۱۴ : ارزیابی‌ها درباره اینکه ایران این حمله را سازماندهی کرده، در حال تقویت است. کاپیتان هندیِ مجروح نیز برای درمان به امارات منتقل شده است
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24705" target="_blank">📅 21:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24704">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N95bHBBB9cOWSN_tG-CcGqjj9iDktkUIQptqHTRSds0mynKDYM9MMr2QvbP1ZJrxE5UMXEvUW0VSvCZt122iejjBd8TBl6Vvj4qj2PVa3Hoe6YMbCtVIzh6nnhRmrU2zNyQnWkUdhy9zOHb8v5QolaS3UFsQ9d-4Wse83ZERh0UsBd9Rgsl7mngJW0rgMgNtp-eEtcK0PoR9hH8UJOrfm6VEVeA3Y-DJdNune-EH7_D1Reig_7iyHVqOSfokmTJmHZf8UmDDzyyNbxj1MYi1ylxJ2qwCm_DPIk0Eq6mf-TNQa-oLqeisUGJ4H6NgqE7oXYeSzdqf2Qu7lz61z3mzWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث سوشال: من بارها اعلام کردم که از بین بردن
تهدید هسته‌ای ایران
۴ تا ۶ هفته زمان می‌برد، اما من این کار را در یک شب انجام دادم! بقیه این مدت فقط برای اطمینان از این است که وضعیت همین‌طور باقی بماند.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24704" target="_blank">📅 21:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا:
تحریم‌های جدید علیه ایران،
بخش‌های خودروسازی و راه‌آهن
و شبکه‌های تأمین‌کننده و حامی آنها را هدف قرار می‌دهد و با هدف
خشکاندن منابع مالی جمهوری اسلامی
اعمال شده است. وزارت خزانه‌داری آمریکا امروز
ایران‌خودرو و سایپا
و همچنین چندین شرکت خارجی مرتبط با تأمین قطعات، مواد اولیه و خدمات این صنایع را تحریم کرد. واشنگتن می‌گوید این اقدامات بخشی از کارزار
«عملیات طرد اقتصادی»
برای قطع منابع مالی حکومت ایران و افزایش فشار اقتصادی بر تهران است.
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/24703" target="_blank">📅 21:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8939ddc2f8.mp4?token=lAaJdkX7WvkPC_MhZdP3VfKL2ILQSPvqM9qTqk4iozgQ5HdW3FpuU-g807Tn-yUkKS6YjJS_WELf0NxnISNW3E0J_Kcn-1hfUblvES3_QiRAIZQlPTBkfh8D7rCC7d6Hqx7Qj6er15VN-XEjIlNj16GKgKNHYhzOIn8Aan5BBGgJCQ1IVh9ks5CMvL3JsA3q7Z-PcQNUYvuI7ppNvb8yStVBYNBhvVssVIZFAvEn7GU5ZYx9a1SFUfmr0LcPP9N6Vmf8dQEmgfESxZ9mVivso1eIMtYfCPDxWAMep8oIpE-ABbvlv_6sMNtI7Y54Qz0yXx3AjZSjiDogr1rs7F-9SU-bSDCwzhRI94SRcRcLN3wQlGjwo1_YvP5yhkwTb8MbB7voSFg__6jMlkPEm2u-9hdmc0jmmmr-iiTPOVm0AzE9GRdxZXZzyMl-Kqyn4uRk1OgYeJcmMl8T0msFL642Ikz1cyc-tCAhxn1Tv1hEUH6qJX52w5RDwomrpPbpYrLpcZme7_qeDJJa6JkndR4iCWVRqJmhdIkEp0_P6H367NU6QjyTxF1d8y0MIwGISvkueQApI8j593njnlRxZdJms_OgC5orNA16909yAUuBz7qcR-Ha9WGwHeMhEHIOJCTrymS8clYhgENH0HRJmxsD_9R-n6RCFIF-0aXev9l9Os0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8939ddc2f8.mp4?token=lAaJdkX7WvkPC_MhZdP3VfKL2ILQSPvqM9qTqk4iozgQ5HdW3FpuU-g807Tn-yUkKS6YjJS_WELf0NxnISNW3E0J_Kcn-1hfUblvES3_QiRAIZQlPTBkfh8D7rCC7d6Hqx7Qj6er15VN-XEjIlNj16GKgKNHYhzOIn8Aan5BBGgJCQ1IVh9ks5CMvL3JsA3q7Z-PcQNUYvuI7ppNvb8yStVBYNBhvVssVIZFAvEn7GU5ZYx9a1SFUfmr0LcPP9N6Vmf8dQEmgfESxZ9mVivso1eIMtYfCPDxWAMep8oIpE-ABbvlv_6sMNtI7Y54Qz0yXx3AjZSjiDogr1rs7F-9SU-bSDCwzhRI94SRcRcLN3wQlGjwo1_YvP5yhkwTb8MbB7voSFg__6jMlkPEm2u-9hdmc0jmmmr-iiTPOVm0AzE9GRdxZXZzyMl-Kqyn4uRk1OgYeJcmMl8T0msFL642Ikz1cyc-tCAhxn1Tv1hEUH6qJX52w5RDwomrpPbpYrLpcZme7_qeDJJa6JkndR4iCWVRqJmhdIkEp0_P6H367NU6QjyTxF1d8y0MIwGISvkueQApI8j593njnlRxZdJms_OgC5orNA16909yAUuBz7qcR-Ha9WGwHeMhEHIOJCTrymS8clYhgENH0HRJmxsD_9R-n6RCFIF-0aXev9l9Os0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانال 14 اسرائیل: «این عملیات برای دستیابی به سه هدف طراحی شده بود: کشتن تعداد زیادی از اسرائیلی‌ها، آسیب رساندن به روابط ما با امارات، و آسیب رساندن به خود امارات.»(زیرنویس فارسی)
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/24702" target="_blank">📅 21:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8e632d84.mp4?token=rxZ9wCrRRaq4u0PZXGYzDgl4gI35Mppo4r-WjvfS8GzK-PmR52M66U_URjuWHrIo0tHqy7feemv8lYu25MLQjW8ZJLwTLeQctfNU2tIf3sad3d8C4pcPR33v5_nHj3-2bVTliopmlxUrTqovIaweSFM2Y7iFsAkj7_cs-Pnhu-hBoIKJT5tZPENkZCLx2G4XZPgS-pt4ffr6tzS-N6dnCse8aZKfexCGV3Tn-i_BjgFq42HwK7ZOTizgbL3EgsHxxzKRlMNPUbWw093Pcmv6gPsaf1_HgQX_yjosWkJBbPxGZI4fhbL6gtyvoVAC3hBzncrv6lI3TWRyjoQSNokEGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8e632d84.mp4?token=rxZ9wCrRRaq4u0PZXGYzDgl4gI35Mppo4r-WjvfS8GzK-PmR52M66U_URjuWHrIo0tHqy7feemv8lYu25MLQjW8ZJLwTLeQctfNU2tIf3sad3d8C4pcPR33v5_nHj3-2bVTliopmlxUrTqovIaweSFM2Y7iFsAkj7_cs-Pnhu-hBoIKJT5tZPENkZCLx2G4XZPgS-pt4ffr6tzS-N6dnCse8aZKfexCGV3Tn-i_BjgFq42HwK7ZOTizgbL3EgsHxxzKRlMNPUbWw093Pcmv6gPsaf1_HgQX_yjosWkJBbPxGZI4fhbL6gtyvoVAC3hBzncrv6lI3TWRyjoQSNokEGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوکی از شبکه فاکس: این خلبان فلای دوبی ممکن است توسط سپاه پاسداران منصوب شده باشد، یا به نوعی دیگر افراطی شده باشد و سپس سعی کرده باشد هواپیما را سرنگون کند؟
ترامپ: ممکن است، بله.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/24701" target="_blank">📅 21:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee9e6e4bb.mp4?token=sfoi2qpct0toKSnGdXouChf3nSrCeFpj3GH9vDe4kfjnOMan_L4_r0f1sh_VDmjdwE4PRZoLe-XAN8nCoUwlnNhHA0G1mkvCeI8B8hsfN4jZz7Oozn9kcBeDR38dNd3U9UaHxuhlkQ1MO8jZAZ2gfJP1Yqnt-Hp8zLnJtGl413XiUzR76CoctaTfbBUrzszxL0jM5Hbi5NwzweZx3yE0P704EldDwa9A2ekiB16bn4uRRmQJTK9Pcos8mPL4bgusJu2V7EdfbB6GySDJRNdSioTDuT6ys2djdzfQVk3_TlsT3CuB9pudJok2QTB0Q28hhx1hXrJDRg8EAPlA3-6c6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee9e6e4bb.mp4?token=sfoi2qpct0toKSnGdXouChf3nSrCeFpj3GH9vDe4kfjnOMan_L4_r0f1sh_VDmjdwE4PRZoLe-XAN8nCoUwlnNhHA0G1mkvCeI8B8hsfN4jZz7Oozn9kcBeDR38dNd3U9UaHxuhlkQ1MO8jZAZ2gfJP1Yqnt-Hp8zLnJtGl413XiUzR76CoctaTfbBUrzszxL0jM5Hbi5NwzweZx3yE0P704EldDwa9A2ekiB16bn4uRRmQJTK9Pcos8mPL4bgusJu2V7EdfbB6GySDJRNdSioTDuT6ys2djdzfQVk3_TlsT3CuB9pudJok2QTB0Q28hhx1hXrJDRg8EAPlA3-6c6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در پاسخ به این سوال که آیا ایران در حادثه مربوط به هواپیمای فلاي‌دبي دخیل است یا خیر، گفت: "به نظر من، با توجه به اطلاعاتی که دارم، بله، اما ما در حال حاضر در این زمینه کار می‌کنیم."
@WarRoom</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/24700" target="_blank">📅 20:58 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5221c8193.mp4?token=a-ADrXwYPz-_JoRNRppgJsZ7n2lA-eVuUFW-fQTHBXeFYmAke_KcQ3EXLPXjmDpJ_7usPvGdAIQPq_fn5Jo5OW-nrDZkGU_RtP7O9Lwl8X_Rkeu40CzfTYqQqkefbd86UWqc9fMWXqbDLF4Sn3JEZl5KUSZeeO5mlGTSR9G0HWhtfPiPSlIwTMRmPhUOfr72guJpz3MD9pHmFAioLA52wGa7IKbRO8UFRCOfTjfFsGRRSwipnhE21mptJg2znW8V5-WzGruSyHksM7ETOVzde6g2ji9_nSlqQpB0GfPnEYLryJmzm__hmwCnTN15mqj9Ay6I150pGC1lSnQGVv_iww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5221c8193.mp4?token=a-ADrXwYPz-_JoRNRppgJsZ7n2lA-eVuUFW-fQTHBXeFYmAke_KcQ3EXLPXjmDpJ_7usPvGdAIQPq_fn5Jo5OW-nrDZkGU_RtP7O9Lwl8X_Rkeu40CzfTYqQqkefbd86UWqc9fMWXqbDLF4Sn3JEZl5KUSZeeO5mlGTSR9G0HWhtfPiPSlIwTMRmPhUOfr72guJpz3MD9pHmFAioLA52wGa7IKbRO8UFRCOfTjfFsGRRSwipnhE21mptJg2znW8V5-WzGruSyHksM7ETOVzde6g2ji9_nSlqQpB0GfPnEYLryJmzm__hmwCnTN15mqj9Ay6I150pGC1lSnQGVv_iww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ برای شرکت در گردهمایی انتخاباتی جمهوری‌خواهان عازم اوکلاهوما شد. دونالد ترامپ، رئیس‌جمهور آمریکا، پنجشنبه ۹ مهر برای حضور در یک تجمع انتخاباتی جمهوری‌خواهان در شهر دورانِت، اوکلاهوما، به این ایالت سفر کرد. این مراسم در چارچوب انتخابات میان‌دوره‌ای کنگره آمریکا برگزار می‌شود و ترامپ در حمایت از نامزدهای جمهوری‌خواه سخنرانی خواهد کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/24699" target="_blank">📅 20:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین تصاویر از خروج خلبان هندی زخمی پرواز فلای دوبی با بانداژ سنگین و کمک‌خلبان مهاجم با دست‌های بسته منتشر شد. نکته مهم درباره پرواز دبی–اسرائیل، هویت خلبانان دوم جایگزین است که عربستان آن را مخفی نگه داشته. هواپیما در آسمان اردن و نزدیک…</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/withyashar/24698" target="_blank">📅 20:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d65db6813.mp4?token=PvGZCPvC9ZnefR396PAWi6s1KtO7WSkdB9heibKPzH39hN66bVY-aN4_liGYf7_NyhbVd3TZpOjoMWt5EWZehyb_N7llVsUr1xCrXBZfIyV7A0DDNByDm_PafKptwP9FfsJioL7M9bOahvrY65-w4sXIsY1oPhbYPq37Rd2rfmdV_xW33pLdzA8X4ZPYefUEYRb9IeV-ZyBXIQx4sdC3T2f9RC-y-lvmbuUpqiT067-iyQ5JTixUAOXdLm82UUSHc6LtwXBrTBdZL_kAIjxQwQbfyayL3qlfC_FrHcb0pMdnUaiWtI4wjXzQET7Q1Xp-8wHtqUjH__Kg6E12qS9JGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d65db6813.mp4?token=PvGZCPvC9ZnefR396PAWi6s1KtO7WSkdB9heibKPzH39hN66bVY-aN4_liGYf7_NyhbVd3TZpOjoMWt5EWZehyb_N7llVsUr1xCrXBZfIyV7A0DDNByDm_PafKptwP9FfsJioL7M9bOahvrY65-w4sXIsY1oPhbYPq37Rd2rfmdV_xW33pLdzA8X4ZPYefUEYRb9IeV-ZyBXIQx4sdC3T2f9RC-y-lvmbuUpqiT067-iyQ5JTixUAOXdLm82UUSHc6LtwXBrTBdZL_kAIjxQwQbfyayL3qlfC_FrHcb0pMdnUaiWtI4wjXzQET7Q1Xp-8wHtqUjH__Kg6E12qS9JGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : «در مورد نیروهای نیابتی ایران، مثل حزب‌الله، چه نظری دارید؟»
ترامپ: «هر اتفاقی برای ایران بیفتد، برای نیروهای نیابتی آن هم همان اتفاق می‌افتد.»
@WarRoom</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/24697" target="_blank">📅 20:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7973c43baf.mp4?token=vvpkdmeZbT5xbt6NlNkgnbTkEizYcJD-Yb4JDsfFbXH0mBCq5uMYwxDwv5PUInITbQwAv2c1en5kJANLvjhZo6LwaacFn33fG7z0BCsJDjV8gtD36fpGK3-Wbgw28S3Fta6JppyYCuO_HLSmzECaFHruWRZHCy69EkrjUz8p-zgF4zx8GsO_3DKb4V5x_AeTbLijGOhEjMDo2vywRBRc8FxUeaL4v_iPOwUAMVKkVi0KzA27mW3mm2nctXdTPsL1etZyEtypkx7JCRHdphA3zeEZsrQFD9iPwB1VVsxKqKxfGxpvLg56Of8k3emdeD9POGi1P_aF-HudazEq2mb6gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7973c43baf.mp4?token=vvpkdmeZbT5xbt6NlNkgnbTkEizYcJD-Yb4JDsfFbXH0mBCq5uMYwxDwv5PUInITbQwAv2c1en5kJANLvjhZo6LwaacFn33fG7z0BCsJDjV8gtD36fpGK3-Wbgw28S3Fta6JppyYCuO_HLSmzECaFHruWRZHCy69EkrjUz8p-zgF4zx8GsO_3DKb4V5x_AeTbLijGOhEjMDo2vywRBRc8FxUeaL4v_iPOwUAMVKkVi0KzA27mW3mm2nctXdTPsL1etZyEtypkx7JCRHdphA3zeEZsrQFD9iPwB1VVsxKqKxfGxpvLg56Of8k3emdeD9POGi1P_aF-HudazEq2mb6gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: به جرئت می‌گویم که صددرصد مردم,  از جمله در سراسر جهان , با دستیابی ایران به سلاح هسته‌ای مخالف‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 90.6K · <a href="https://t.me/withyashar/24696" target="_blank">📅 20:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اتاق جنگ با یاشار : اولین تصاویر از خروج خلبان هندی زخمی پرواز فلای دوبی با بانداژ سنگین و کمک‌خلبان مهاجم با دست‌های بسته منتشر شد. نکته مهم درباره پرواز دبی–اسرائیل، هویت خلبانان دوم جایگزین است که عربستان آن را مخفی نگه داشته. هواپیما در آسمان اردن و نزدیک مرز اسرائیل بود، اما دو خلبان جایگزین تمرینی به‌جای فرود در مقصد ، مسیر را تغییر داده و بدون فرود حتی در اردن، هواپیما را به عربستان بردند. نتیجه این اقدام، نجات خلبان تروریست عمانی و جلوگیری از مشخص‌شدن اسناد این عملیات بود. یکی از دو خلبان بریتانیایی بوده و هویت خلبان دوم اعلام نشده؛ احتمالاً فرانسوی یا اسپانیایی باشد.
@WarRoom</div>
<div class="tg-footer">👁️ 93.6K · <a href="https://t.me/withyashar/24695" target="_blank">📅 20:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314c1f7963.mp4?token=QetqDsxA8L6xjXXgtxOnzLyl1cz4jyRChc861FP2G1CsdaAX3m6b9EYcwBY_GImTNFjPNgygZXSQOgr9uvH7rkFtZ3_a4gWR3EKijs3Qf6dk8FykzdeeBmjaiz9i-QNxGIir1ntPcWirId5JJsQifHbvlFtq8I7HsydtfaYkZEBFhKloS4boTDUT7JkTp4rYVj72nXmb8MQkU82jrRb0Y_jX2Vo8v49a4lyKaMNfIJ1lL6FbOEWlfZWXq_YqkmE6FiNBKUhP7sLyrM5-jLEJijWwO7yJRUAvyZvYXxfx-t993M9DU26rW1sU91bd8L9N9Lz07ZMYNfoZPbyrtdI61A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314c1f7963.mp4?token=QetqDsxA8L6xjXXgtxOnzLyl1cz4jyRChc861FP2G1CsdaAX3m6b9EYcwBY_GImTNFjPNgygZXSQOgr9uvH7rkFtZ3_a4gWR3EKijs3Qf6dk8FykzdeeBmjaiz9i-QNxGIir1ntPcWirId5JJsQifHbvlFtq8I7HsydtfaYkZEBFhKloS4boTDUT7JkTp4rYVj72nXmb8MQkU82jrRb0Y_jX2Vo8v49a4lyKaMNfIJ1lL6FbOEWlfZWXq_YqkmE6FiNBKUhP7sLyrM5-jLEJijWwO7yJRUAvyZvYXxfx-t993M9DU26rW1sU91bd8L9N9Lz07ZMYNfoZPbyrtdI61A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: اگر ایران پشت حمله به هواپیما باشد، آیا شما علیه آن اقدام تلافی‌جویانه خواهید کرد؟ آیا ایالات متحده تلافی خواهد کرد؟
ترامپ: آنها ضربه سختی خواهند خورد، نگران نباش. فقط از آنها بپرس؟ آنها می‌دانند چه اتفاقی می‌افتد.
@WarRoom</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/24694" target="_blank">📅 20:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcf1464cf.mp4?token=lVYaddGdkJzpv1LPWRUbHIQkDXiro_0BIJcqPXZJ-tRNTgni5LlyGyyRjbjn2U4yg4jL-fIdMCaZaY0d2m5nGWSD28MLLcKg9Qal3euH8Y2BQD5iFTV__LhyGplt76Q_fx8-DFV4xouzJrzdVfvnhDa5tgkeMwV3i2Ocglff6pAIJhdVhskSW5mllpu8o2i1mtC4sCvrBGZQhQlTIkIyotcVMB_oqZ41KPXcORA47eadWhT4tpbVA_6ryL_UhDDxX7V5h_IkBEX-Ji6WwMLGSqAOjJGQkFEpj1Y5j2C5uo4YhRNWI7-X3dhmSoDvLaADpxTspmhYmU4NWqjCsEXlNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcf1464cf.mp4?token=lVYaddGdkJzpv1LPWRUbHIQkDXiro_0BIJcqPXZJ-tRNTgni5LlyGyyRjbjn2U4yg4jL-fIdMCaZaY0d2m5nGWSD28MLLcKg9Qal3euH8Y2BQD5iFTV__LhyGplt76Q_fx8-DFV4xouzJrzdVfvnhDa5tgkeMwV3i2Ocglff6pAIJhdVhskSW5mllpu8o2i1mtC4sCvrBGZQhQlTIkIyotcVMB_oqZ41KPXcORA47eadWhT4tpbVA_6ryL_UhDDxX7V5h_IkBEX-Ji6WwMLGSqAOjJGQkFEpj1Y5j2C5uo4YhRNWI7-X3dhmSoDvLaADpxTspmhYmU4NWqjCsEXlNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: ایران نمی‌تواند سلاح هسته‌ای داشته باشد و نخواهد داشت؛ آن‌ها نیز پذیرفته‌اند که چنین سلاحی نداشته باشند.
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/24693" target="_blank">📅 20:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9e638a4cc.mp4?token=Uh93MjNOvGqDpOVU8EswxnFzAtnx-tqy1uKzDNXJ-3vGXChB3Xlczi6pWtHWpzofUCD4D5i_TNWEeFGqW3XI8-BBtOPNMuaztCzC5MoZIFGF7eWCdAZrGKbx4rL57VIASlsSrfRqJOt7Yn1IBMXxZOtWGMz6WNZjNH1cmakNanq8PZ87LZl-4PlpzDc2TCFrwjyafHlDvKV3S5owOrjQiCSL4sPbdKeqQLOKHKled3_-rKBlZxz7wheUYu7PoMEmvocanErL55IDeOpFCnNvK94tmIn_cEXnUuObunpBkgTvZDF-5zmbcAEWHuecYUbrPj4w2WGhMSPtTpP3LBLa6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9e638a4cc.mp4?token=Uh93MjNOvGqDpOVU8EswxnFzAtnx-tqy1uKzDNXJ-3vGXChB3Xlczi6pWtHWpzofUCD4D5i_TNWEeFGqW3XI8-BBtOPNMuaztCzC5MoZIFGF7eWCdAZrGKbx4rL57VIASlsSrfRqJOt7Yn1IBMXxZOtWGMz6WNZjNH1cmakNanq8PZ87LZl-4PlpzDc2TCFrwjyafHlDvKV3S5owOrjQiCSL4sPbdKeqQLOKHKled3_-rKBlZxz7wheUYu7PoMEmvocanErL55IDeOpFCnNvK94tmIn_cEXnUuObunpBkgTvZDF-5zmbcAEWHuecYUbrPj4w2WGhMSPtTpP3LBLa6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: نرخ‌های بهره می‌توانند رشد را کند کنند. ما خواهان رشد هستیم؛ و رشد موجب تورم نمی‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/24692" target="_blank">📅 20:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1487770b48.mp4?token=rkI2yqJi-fDr2t9KFwzbaGiSSKsmj8KxYX4MDqkoJeqoZMtjeNQ54pRHVQpMWNPY77xgoEcyzgbq7Zxg7H1hVb1Ib9r_2Ig89Ikyy34Jgbpp3uE0SElB591UovZWyMTXPGZWEnueQ3Xrr1lkIeXU_WsLab3s9RB-iKW_mdBoc8taKshNKwvanIJiufigz20pE0yIJwjclSH_SUssKhoJNeRO8HTU0sMZfi8_EZ5PblRh6tQZheaI2Yzw3oHZB5VrRzMlIraV4VNJLGo3EUT2dUKyjOHLjQfv6rk_LgOJ2JhbVfATWpSF5D5fQTWLUbejosykyrT4mOeo0N-M44blXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1487770b48.mp4?token=rkI2yqJi-fDr2t9KFwzbaGiSSKsmj8KxYX4MDqkoJeqoZMtjeNQ54pRHVQpMWNPY77xgoEcyzgbq7Zxg7H1hVb1Ib9r_2Ig89Ikyy34Jgbpp3uE0SElB591UovZWyMTXPGZWEnueQ3Xrr1lkIeXU_WsLab3s9RB-iKW_mdBoc8taKshNKwvanIJiufigz20pE0yIJwjclSH_SUssKhoJNeRO8HTU0sMZfi8_EZ5PblRh6tQZheaI2Yzw3oHZB5VrRzMlIraV4VNJLGo3EUT2dUKyjOHLjQfv6rk_LgOJ2JhbVfATWpSF5D5fQTWLUbejosykyrT4mOeo0N-M44blXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 96.7K · <a href="https://t.me/withyashar/24691" target="_blank">📅 20:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرگزاری سان : پلیس ضدتروریسم بریتانیا یک شهروند ۲۷ ساله
ایرانی سیتیزن بریتانیا
را به ظن آماده‌سازی اقدامات تروریستی و ارتباط با توطئه برای هدف قرار دادن پایگاه هوایی RAF Fairford دستگیر کرد. یک مرد ۲۶ ساله بریتانیایی نیز تحت بازجویی قرار گرفته و دو ملک در لندن بازرسی شده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 96.6K · <a href="https://t.me/withyashar/24690" target="_blank">📅 20:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 95K · <a href="https://t.me/withyashar/24689" target="_blank">📅 20:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24688">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: موضوع ایران می‌تواند به انتخابات میان‌دوره‌ای آسیب برساند
@WarRoom</div>
<div class="tg-footer">👁️ 98.2K · <a href="https://t.me/withyashar/24688" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24687">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ برای سومین بار اعلام کرد ایران موافقت کرده است سلاح هسته‌ای نداشته باشد
؛ او پیش‌تر در ۳ ژوئن گفته بود «آنها قبلاً موافقت کرده‌اند که سلاح هسته‌ای نداشته باشند» و در ۱۵ ژوئن نیز تأکید کرده بود ایران «کاملاً» با این موضوع موافقت کرده است. ترامپ امروز، اول اکتبر، بار دیگر در اظهارات خود درباره ایران تأکید کرد که تهران نباید به سلاح هسته‌ای دست پیدا کند.
@WarRoom
😂</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24687" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ: ایران موافقت کرده است که سلاح هسته‌ای نداشته باشد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24686" target="_blank">📅 20:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7423fb5452.mp4?token=ntGGA-ZHuxsJPPSLxCcmHZ6rgJsZGL_At1ZsBhqh42Pjf8rL2TxhaIPV-uEMu2GpxGTHm1o1EBDSwmCOJxegQ5h0KTfxdKd16BFnVG7KOiVHOiqcpDcq9Qiyh5dPTPev-6jDpUmpYh7CpVSF4SQay9KUDt3dbGywJyLm2-LDgbHqgrJQGUXf97sGSB_yg_ImHZu5nIE2UU4UW08S7AWwuTtnEs_GFtyLp4N-7cowtuucG4yUMHTsHIjf8-CISz0RdB51jqJhkeT6fCQkNlCIrYJc-GKvDn3SFq3uqqj3vw7rwZq5xEbW_1md0PQKSheikWsQjs6NPn8ogBovurh7KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7423fb5452.mp4?token=ntGGA-ZHuxsJPPSLxCcmHZ6rgJsZGL_At1ZsBhqh42Pjf8rL2TxhaIPV-uEMu2GpxGTHm1o1EBDSwmCOJxegQ5h0KTfxdKd16BFnVG7KOiVHOiqcpDcq9Qiyh5dPTPev-6jDpUmpYh7CpVSF4SQay9KUDt3dbGywJyLm2-LDgbHqgrJQGUXf97sGSB_yg_ImHZu5nIE2UU4UW08S7AWwuTtnEs_GFtyLp4N-7cowtuucG4yUMHTsHIjf8-CISz0RdB51jqJhkeT6fCQkNlCIrYJc-GKvDn3SFq3uqqj3vw7rwZq5xEbW_1md0PQKSheikWsQjs6NPn8ogBovurh7KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوتین , رئیس‌جمهور روسیه
: اگر صحبتی از حمله مستقیم به فدراسیون روسیه، به کالینینگراد برسد، استفاده از تمام تسلیحات موجود در زرادخانه ما، اجتناب‌ناپذیر و فوری خواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24685" target="_blank">📅 19:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">سخنگوی نیروهای ائتلاف: گروه حوثی با استفاده از یک پهپاد، ایستگاه توزیع برق "طیبه" در شهر مدینه منوره را مورد هدف قرار داد.
@WarRoom</div>
<div class="tg-footer">👁️ 98.3K · <a href="https://t.me/withyashar/24684" target="_blank">📅 19:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZo-QNwsIx3vyZ2rOEITR_uZVz3rlL2utede1XdrcqCnlTnAnuAPxIrB0OW7opNAYnP7lUP81ZT0OX0ABLj-zi9oC-nOSKIeU0sXETZcD3El-SHZIPY7I-aRTH7o__LQV80WswNAmj2Tqjy4W3HFReunJUA0a7r9ze8zgBsZFOPQRfeQkp0uAw-hpY61FPhFFOHRzruIFI-Be1jhzOD0Xb8-NWigZFBMqnf0g8rMk0UqwkeHPZJitibmntQME_550OHtDzEfaQcSCTSdLoyeD1-0NbsSIM0VA8LruwbM5RRo0CriErtQ8oWDlISNHfyd0fYweaga2Io3fSeRlbosIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏یک جنگنده‌ی A10 که از درگیری با ایران برگشته! نشان های پرتاب بمب‌های جیدم و sub به همراه کیل مارک«نشان نابودی» دو قایق تندرو سپاه را هم بر بدنه دارد!
@WarRoom
🔥</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24683" target="_blank">📅 19:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41488cbe9.mp4?token=AwvEJkJRYtOCerjcWQE_hJ9ScIw9DHeW55OSZDABPQTBS-Pd4bkx0Z_UI-JlOkzuk33ih0QqWrRhTo4WrIR2WBtuRCY1Er1pl4bgx5AZNUtUmUbcS8CahBf_ldOTvc2EdvhiOZ5WaegDIKaYJxO02DTTjNyxGhD056mzVkdZ0fcvgvkTf87UEsTzFjECxCPAZ3cSx4BE9R_SSG44USoPFR-uh-jM0r8MZW_gyCBQ9lDgn7ic8FJA5XhtENA2-qkHWCntq5OISSCDAg1MKy__15uziWpxGb0ESw0DpMuVyrHkqfWSZxq11k0Brr3Sgxv5vMpjg9480koHWpVxagO2bEIwLTdJmnqq7nxh_ZCZkncA22EmNNFeFEf74SDyZRRS_5mWAPj-_a4IZuPzv8UHYOFVoTGHDUvE40sDR_rnUPQJJpCq6voMIhT2opMPp58ExNINPUadm_vsb9Vd0YTWctBBNrn52Bap1N5Cz4_82xLhq5iQXFyxTBfC7zdYzFqbaUu-tAq0GXU3wRUGjRb9pEqOrfEHFnpqd-bgYU1dorol2ygRHGbBTc4xMdA1nIIQQUigeon6-OLgcpSTIKZbJF4Wv_rUIrx2CjQ7o-s3oiA44KAAy-56qgaeZUaSD5SbWiwOtkQk1Rcepyz50pOPgzaR27TMThpJNfgjUrRz9Os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41488cbe9.mp4?token=AwvEJkJRYtOCerjcWQE_hJ9ScIw9DHeW55OSZDABPQTBS-Pd4bkx0Z_UI-JlOkzuk33ih0QqWrRhTo4WrIR2WBtuRCY1Er1pl4bgx5AZNUtUmUbcS8CahBf_ldOTvc2EdvhiOZ5WaegDIKaYJxO02DTTjNyxGhD056mzVkdZ0fcvgvkTf87UEsTzFjECxCPAZ3cSx4BE9R_SSG44USoPFR-uh-jM0r8MZW_gyCBQ9lDgn7ic8FJA5XhtENA2-qkHWCntq5OISSCDAg1MKy__15uziWpxGb0ESw0DpMuVyrHkqfWSZxq11k0Brr3Sgxv5vMpjg9480koHWpVxagO2bEIwLTdJmnqq7nxh_ZCZkncA22EmNNFeFEf74SDyZRRS_5mWAPj-_a4IZuPzv8UHYOFVoTGHDUvE40sDR_rnUPQJJpCq6voMIhT2opMPp58ExNINPUadm_vsb9Vd0YTWctBBNrn52Bap1N5Cz4_82xLhq5iQXFyxTBfC7zdYzFqbaUu-tAq0GXU3wRUGjRb9pEqOrfEHFnpqd-bgYU1dorol2ygRHGbBTc4xMdA1nIIQQUigeon6-OLgcpSTIKZbJF4Wv_rUIrx2CjQ7o-s3oiA44KAAy-56qgaeZUaSD5SbWiwOtkQk1Rcepyz50pOPgzaR27TMThpJNfgjUrRz9Os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏امیر قاسمی و رو‌کردن نام کسانی که با سپاه در ارتباط کامل قرار دارند ، آیا نفر بعدی که در ایران خواهید دید معین است؟ گزارشهایی هم هست که در کنسرت اخیر معین اجازه ورود پرچم شیر و خورشید داده نشد و فقط آهنگی برای ایران خوانده شد و در نمایشگر هم پرچمی نمایش داده نشد و اشاره‌ای هم به انقلاب شیر و خورشید نشده
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24682" target="_blank">📅 19:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مرد خردمند ، مارک لوین : مردم ایران را مسلح کنید!!!
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24681" target="_blank">📅 19:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏آیا سنتکام در حال آخرین تمرینات آماده‌سازی برای هلی بورن در داخل ایران
ه
..!!؟
‏تصاویری از فرود دو فروند هواپیمای ترابری C-17 گلوب‌مستر III نیروی هوایی آمریکا روی یک باند خاکی غیرمتعارف در محدوده تمرینی نِلیس
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24680" target="_blank">📅 18:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الجزیره: ناو هواپیمابر روزولت به همراه گروه ضربت خود بعد از ترک اسکله سن دیگو همچنان به سمت خاورمیانه (غرب آسیا) در حرکت است
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/24679" target="_blank">📅 18:42 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">امشب مهلت ۴۵ روزه شورای عالی امنیت ملی برای برداشتن محاصره دریایی تموم میشه!
محسن رضایی اعلام کرده بود اگر در پایان این ۴۵ روز محاصره برداشته نشه، بصورت نظامی و با زور محاصره رو میشکنیم.
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24678" target="_blank">📅 18:37 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b70be8bbfa.mp4?token=p_eroFkEgn2Xld5Ydvgjq1_2XOB0_67VzjN34FmLNlp5_YlqzLWeTsywe4mCVQs_ZhhxC4L1JLir8nFlfG9vqkLc68S8J5sShsMTYwhGAKUfP4xQUzFqFqLM8BLBuooRxXV6AlA3_2VCuNgepaxEvkdVi82JY3IJmLVpnHut3doK9Ji0fBBnvvz1zzPPtqeZXN7ybQsl36aD7BKxhlfSvSlKt7Fl3yNk-XR-ChoUYzEN2PSh4QsOO67mMknBDhF2huk4JXoZBzFmC4OnCIbIbzvz1_sDg2AOsB1agR5JvyIRZyw-0yOfpgBb9A8JznJ5qhtzegDKBbor9iKT9m3ypTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b70be8bbfa.mp4?token=p_eroFkEgn2Xld5Ydvgjq1_2XOB0_67VzjN34FmLNlp5_YlqzLWeTsywe4mCVQs_ZhhxC4L1JLir8nFlfG9vqkLc68S8J5sShsMTYwhGAKUfP4xQUzFqFqLM8BLBuooRxXV6AlA3_2VCuNgepaxEvkdVi82JY3IJmLVpnHut3doK9Ji0fBBnvvz1zzPPtqeZXN7ybQsl36aD7BKxhlfSvSlKt7Fl3yNk-XR-ChoUYzEN2PSh4QsOO67mMknBDhF2huk4JXoZBzFmC4OnCIbIbzvz1_sDg2AOsB1agR5JvyIRZyw-0yOfpgBb9A8JznJ5qhtzegDKBbor9iKT9m3ypTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفحه فارسی وزارت امورخارجه اسرائیل با انتشار ویدیویی درباره ماجرای هواپیمای کیش‌ایر نوشت: حالا که بحث هواپیما داغه، بد نیست یادی کنیم از هواپیمای کیش‌ایر که ۳۱ سال پیش در مسیر تهران به کیش با ۱۷۴ سرنشین ربوده شد. وقتی سوخت هواپیما رو به اتمام بود و خطر سقوط وجود داشت، اسرائیل تنها کشوری بود که اجازه فرود به این هواپیما داد و جان سرنشینان رو نجات داد.جمهوری اسلامی هرگز نتونست پیوند میان دو ملت ایران و اسرائیل رو از بین ببره.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/24677" target="_blank">📅 18:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رویترز: آمریکا مصر را نقره داغ کرد
و به‌دلیل همکاری مصر در جنگ با ایران، شروط حقوق بشری (فراهم کردن شرایط نقض حقوق بشر) کمک نظامی به این کشور را کنار گذاشت. وزارت خارجه آمریکا تصمیم گرفته است شروط مربوط به رعایت حقوق بشر در مصر را برای تحویل تجهیزات نظامی به ارزش حدود ۳۰۰ میلیون دلار اعمال نکند. این تصمیم در پی نقشی اتخاذ شده که واشنگتن آن را «کمک‌کننده» توصیف کرده است؛ با این حال، جزئیات دقیق همکاری مصر مشخص نیست
@WarRoom</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/24676" target="_blank">📅 18:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عراقچی : سفیر بریتانیا در تهران به دلیل اتهاماتی که به ما در مورد حادثه در نزدیکی پایگاه ویرفورد وارد شده است، احضار شد.
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/24674" target="_blank">📅 17:31 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خبرنگار تایم:
پس از حملات حوثی‌ها گزارش‌هایی منتشر شد که عربستان از اینکه آمریکا از این کشور دفاع نکرده ناراضی بوده است. رابطه شما با سعودی‌ها چگونه است؟
ترامپ:
خوب است. رابطه‌ام با آنها بسیار خوب است و رابطه خوبی با ولیعهد دارم( پاسخ نمیدهد)
@WarRoom</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/24673" target="_blank">📅 17:05 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
