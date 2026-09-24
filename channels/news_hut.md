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
<img src="https://cdn4.telesco.pe/file/hdrV6YhTaG3fbObnFoVwWOQcbpn2pSnz7kP9leXsXH0Qcg0znWe43TYQOx5Ljs7-qhiWJZQFsx3SNw6q7UsF2M-D_vVyGa5zJzh_jnGno238bl1tEyY4vL8M_Nuk606nHKwnkuDb4Hq_cxHwOkPnElC_joS5lO32q5P031YqL6NU26XWrRYtWELfacSkww775kKaSdYz0sDBBWq2PlXTKjE0ivLS1LNLYDQ0veo-m7S1VXQ8ZOqtl4_3_VHFFNkGixEtAOimlSm8OKh2uCTR41GihyVpKug3LpNDtpzkSZFAN9_CyhHTfxV5UznUsP0z6S-5K_6TOoE6inTTceKIng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-02 23:07:58</div>
<hr>

<div class="tg-post" id="msg-72229">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=YBLTEIlbgpeIEa1WQvFUzY-XHpxgzWYe_bvGAEkQ9ENiMzRR-0-1ISWlwEfwYq2dVDdOhpl-SI2e_q9grFzwWwMjPZT_4FILkArhsCoNAe7lsRJqUBdTQw68WC6_bi2BWsFFyoVFCBCt2_okSfyDowzaGyuVDZBg3BteTUzHhjHQGy1vXDJ-c-Ld8vofu7-Xhg0uDj0pB2nVmdk3d1kkqsjlA5JgMJFLn0khHkOrxEj8cmXcfWczB4yIrN8nA_OpwPHZWcVOuYb04J810gpl8S8Kq028RaZctwaja1xSNlmwW0JeBsnMswxTV97w2RmUjHaELVJebr1QZkoD8hGIpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=YBLTEIlbgpeIEa1WQvFUzY-XHpxgzWYe_bvGAEkQ9ENiMzRR-0-1ISWlwEfwYq2dVDdOhpl-SI2e_q9grFzwWwMjPZT_4FILkArhsCoNAe7lsRJqUBdTQw68WC6_bi2BWsFFyoVFCBCt2_okSfyDowzaGyuVDZBg3BteTUzHhjHQGy1vXDJ-c-Ld8vofu7-Xhg0uDj0pB2nVmdk3d1kkqsjlA5JgMJFLn0khHkOrxEj8cmXcfWczB4yIrN8nA_OpwPHZWcVOuYb04J810gpl8S8Kq028RaZctwaja1xSNlmwW0JeBsnMswxTV97w2RmUjHaELVJebr1QZkoD8hGIpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این تحرکات لجستیکی و نظامی آمریکا باید توافق رو قطعی بدونیم
@News_Hut</div>
<div class="tg-footer">👁️ 315 · <a href="https://t.me/news_hut/72229" target="_blank">📅 23:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72228">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">عجب دنیاییه، پزشکیان رفت سازمان ملل از مردم غزه حمایت کرد، نتانیاهو هم رفت از مردم ایران حمایت کرد
#hjAly‌</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/news_hut/72228" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72227">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
می‌خواهم از شما بخواهم که با دقت به حرف‌های من گوش دهید. روزی خواهد رسید، و ممکن است این روز خیلی دور نباشد، که مردم ایران آزاد خواهند شد.
این رژیم خبیث، به دلیل دروغ‌هایش، فسادش و ظلمش، سقوط خواهد کرد. این رژیم ستمگر فرو خواهد پاشید و همه ما در آن روز جشن خواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/news_hut/72227" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72226">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
این یک دستگاه ارتباطی استارلینک است که به مردم اجازه می‌دهد به حقیقت دسترسی داشته باشند، آزادی اندیشه و آزادی بیان را تجربه کنند.
به همین دلیل است که رژیم ایران میلیاردها دلار برای سانسور اینترنت هزینه می‌کند.
آقای رئیس جمهور، من این دستگاه را پیش شما می‌گذارم تا بتوانید آن را به هیئت ایرانی بدهید.
بنابراین، وقتی آنها ناگزیر به ترک کشور شدند، آنها نیز می‌توانند آزادانه داستان خود را در رسانه‌های اجتماعی بیان کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/news_hut/72226" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72224">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نتانیاهو: خدا باماست
سخنرانی تموم شد
#hjAly‌</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/news_hut/72224" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72223">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">نتانیاهو: روز آزادی مردم ایران رو باهم جشن می‌گیریم
#hjAly‌</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/news_hut/72223" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72222">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نتانیاهو: یه روزی که خیلی دیر نیست، مردم ایران آزاد می‌شن
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/news_hut/72222" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72221">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">نتانیاهو: نیروی مردم ایران، آخوند رو شکست می‌ده
#hjAly‌</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/72221" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72220">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: شما مدافعان قلابی حقوق بشرین
#hjAly‌</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/news_hut/72220" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72219">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: وقتی آخوندا هزاران معترض رو کشتن شماها کجاها بودین؟
#hjAly‌</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/news_hut/72219" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72218">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نتانیاهو: آخوندا می‌ترسن که مردمشون استارلینک داشته باشن
#hjAly‌</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/news_hut/72218" target="_blank">📅 22:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72217">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=O7x9uWHAL4sg6quFNtDsCfcSfHn_QcC9vRO_83Rhba_xFe54z0DT9gF7IdlCYB9l-Z0jRw2WZin929tQmPoWzD-_lnP_Aa3YYFjg8tf9UytDPKD6uKxlQzTD2yJTbTvwxJCAdkQXb6LblKHOD1WMi9l4sTzTzUsOra5QjfwaBH-t9g64lZxPpJ09ZaZYNNplJRcVt-9-Jx6yTm-Hid5HGe6Ufc90GBpYGxyiJF2AXrjqpILzN9cR09pjskjN1MyPxjDqu-6-wczizyOEvCNRz5wKNEZjLpJsUQnhk0NsXlNdfJ-65J_ckoxqJRpzW9Xyc9eA3CUQRNW3cIHe6T_nTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=O7x9uWHAL4sg6quFNtDsCfcSfHn_QcC9vRO_83Rhba_xFe54z0DT9gF7IdlCYB9l-Z0jRw2WZin929tQmPoWzD-_lnP_Aa3YYFjg8tf9UytDPKD6uKxlQzTD2yJTbTvwxJCAdkQXb6LblKHOD1WMi9l4sTzTzUsOra5QjfwaBH-t9g64lZxPpJ09ZaZYNNplJRcVt-9-Jx6yTm-Hid5HGe6Ufc90GBpYGxyiJF2AXrjqpILzN9cR09pjskjN1MyPxjDqu-6-wczizyOEvCNRz5wKNEZjLpJsUQnhk0NsXlNdfJ-65J_ckoxqJRpzW9Xyc9eA3CUQRNW3cIHe6T_nTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
اخلاقی‌ترین ارتش جهان؛ ارتش اسرائیل (IDF).»
@News_Hut</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/news_hut/72217" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72216">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نتانیاهو: هرگز نسل‌کشی نکردیم
#hjAly‌</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/news_hut/72216" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72215">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نتانیاهو: آقای ممدانی تلاش کردی من نیام نیویورک، دیدی کیر شدی؟
#hjAly‌</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/news_hut/72215" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72214">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نتانیاهو: کیرم تو ممدانی و زنش و دوستاش
#hjAly‌</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/news_hut/72214" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72213">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نتانیاهو: ما کلی واکسن و غذا به مردم غزه دادیم
#hjAly‌</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/news_hut/72213" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72212">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نتانیاهو: اردوغانِ جاکش، تو هیچوقت حاکم قدس نمی‌شی
#hjAly‌</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/news_hut/72212" target="_blank">📅 21:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72211">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نتانیاهو: کیرم تو ترکیه
#hjAly‌</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/news_hut/72211" target="_blank">📅 21:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72210">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نتانیاهو: کیرم تو قطر
#hjAly‌</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/news_hut/72210" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72209">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=u11Kd2tBJEZwrN_-fEgOZpVoIeJhKad94kTpcwYxZixK6ptbbgMTlAzGCjtI5KyaXD2Y-bhX4seGm21RJG41yWdPCeWe_rk6M4z0jE56zoNaM1B8J9PfAgDTeCQzSDihsa7XmwbIQUGYMGZsNY9BedhnZZwRI8uzkIgKdjaYB_lB8YPKiD6OhGwW-xiDovhSxaGAU4iNVXzpuhOGf0SkSPdBArKjWDmOwIyQP1n2tSp9xJ8K_KjAs9-VLQbGdOTDO6Wc_D406eO_Ac3sfPJ9VhTZ3AmWZhLvVnqYdi-ANeNhABQTClYyh0WmzUf3Gy4Xzr_0Y_MY1jQtqJDOIMbF8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d2b8c0864.mp4?token=u11Kd2tBJEZwrN_-fEgOZpVoIeJhKad94kTpcwYxZixK6ptbbgMTlAzGCjtI5KyaXD2Y-bhX4seGm21RJG41yWdPCeWe_rk6M4z0jE56zoNaM1B8J9PfAgDTeCQzSDihsa7XmwbIQUGYMGZsNY9BedhnZZwRI8uzkIgKdjaYB_lB8YPKiD6OhGwW-xiDovhSxaGAU4iNVXzpuhOGf0SkSPdBArKjWDmOwIyQP1n2tSp9xJ8K_KjAs9-VLQbGdOTDO6Wc_D406eO_Ac3sfPJ9VhTZ3AmWZhLvVnqYdi-ANeNhABQTClYyh0WmzUf3Gy4Xzr_0Y_MY1jQtqJDOIMbF8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
با دوستان آمریکایی خوبمان، ارتش، نیروی دریایی، نیروی هوایی و تأسیسات هسته‌ای ایران را در هم کوبیدیم
@News_Hut</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/news_hut/72209" target="_blank">📅 21:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72208">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=T4Vl3pYhiKrAyyUdtYo1CHG1YRCfOtrXieAeX8EQvMsjQnw3gzwdPJPIiTrWRMlzR5bkuHl3ri3MdXlX-pmV7N-Zu1yAyaBF48--vPnF3dXIHrrCy7xA7PqxfX9aJeUref-m-cFTsiMqvTbO6UJhEaxcr1H2_q8lMB51ekNqWFgOFxRzp9qiq4y-klNYHaHgZ0dnGYWWW1Wxr9hbjDTSXeIN3jUz_uqRW2uifXMhfEPqZLQn30y_ILkRHUHa2N8ZBZZLwM45_lBDCMiqakAhoakbZMjANAYgBSdrY8hR4PybwNoKIUs1uYT9yVcc2l7DvCge31DuxxAo0HIV1CvJm03kRcmO-YhMcO-hFbLUKBFpHZo2YYwpjo6Owzm8V4RrqGhK96ZAHKKVh5chQ_HkKUyOlBtN8nTEJnIlwu8xLF3KpdxQ6e7jGfBTSa3ST9ySGdlhdYPnI1MDZqo99jm7K2jxX0EP_kZad7JTNlawvNrmigWUF5T2dGleKu1h7LPZRAOKbxk8CQXxuMHBOE51Fvp8hu2hkHcXSFQ0Ra0uxG5lXIVEQWM8imJBhioSPin6n_A7IqVeT6zGOjH7UWMMMY59ruuAVZwOxFWT4ZVm9k3jaFx4qs1DLo29GCQZnBOvHXWdjLfSanWXWO5Yjt0rySY6hO0WyQYkpXWV-EvoYRI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6173f954c.mp4?token=T4Vl3pYhiKrAyyUdtYo1CHG1YRCfOtrXieAeX8EQvMsjQnw3gzwdPJPIiTrWRMlzR5bkuHl3ri3MdXlX-pmV7N-Zu1yAyaBF48--vPnF3dXIHrrCy7xA7PqxfX9aJeUref-m-cFTsiMqvTbO6UJhEaxcr1H2_q8lMB51ekNqWFgOFxRzp9qiq4y-klNYHaHgZ0dnGYWWW1Wxr9hbjDTSXeIN3jUz_uqRW2uifXMhfEPqZLQn30y_ILkRHUHa2N8ZBZZLwM45_lBDCMiqakAhoakbZMjANAYgBSdrY8hR4PybwNoKIUs1uYT9yVcc2l7DvCge31DuxxAo0HIV1CvJm03kRcmO-YhMcO-hFbLUKBFpHZo2YYwpjo6Owzm8V4RrqGhK96ZAHKKVh5chQ_HkKUyOlBtN8nTEJnIlwu8xLF3KpdxQ6e7jGfBTSa3ST9ySGdlhdYPnI1MDZqo99jm7K2jxX0EP_kZad7JTNlawvNrmigWUF5T2dGleKu1h7LPZRAOKbxk8CQXxuMHBOE51Fvp8hu2hkHcXSFQ0Ra0uxG5lXIVEQWM8imJBhioSPin6n_A7IqVeT6zGOjH7UWMMMY59ruuAVZwOxFWT4ZVm9k3jaFx4qs1DLo29GCQZnBOvHXWdjLfSanWXWO5Yjt0rySY6hO0WyQYkpXWV-EvoYRI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
آنها به زنان باردار تیراندازی می‌کنند و خانواده‌های کامل را هدف قرار می‌دهند. البته هیچ‌کدام از این موارد در رسانه‌های بین‌المللی یا شبکه‌های اجتماعی پوشش داده نمی‌شود؛ هیچ‌کدام!
آنچه پوشش داده می‌شود، گروهی حدود ۱۵۰ جوان کم‌سن‌وسال بزهکار هستند که می‌روند و سنگ پرتاب می‌کنند و درختان زیتون را قطع می‌کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/news_hut/72208" target="_blank">📅 21:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72207">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نتانیاهو: هدف فقط پیروزیه، همونطور که داداشم یونی گفت، ما مجبوریم پیروز بشیم
#hjAly‌</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/news_hut/72207" target="_blank">📅 21:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72205">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نتانیاهو: دم ترامپ گرم داداشیمه
#hjAly‌</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/news_hut/72205" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72204">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نتانیاهو: خامنه‌ای دیگه مرده
🔥
🔥
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/news_hut/72204" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72203">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نتانیاهو: این پیجر های تو دستم رو می‌بینید؟ حزب‌اللهیا که خوب یادشونه، با همینا دهنشونو گاییدم
#hjAly‌</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/news_hut/72203" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72202">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">نتانیاهو: خدایی کیو دیدین مث ما که تو هفت جبهه همزمان بجنگه؟
#hjAly‌</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/news_hut/72202" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72201">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نتانیاهو: مث شیر می‌جنگیم
#hjAly‌</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/news_hut/72201" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72200">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نتانیاهو: سال‌ها پیش داداشم یونی تو جنگ با اعراب بهم گفت ما پیروز می‌شیم، الان من همینو می‌گم، ما پیروز می‌شیم
#hjAly‌</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/news_hut/72200" target="_blank">📅 21:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72198">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نتانیاهو: اسرائیل کوچولوعه، انگلیسی های جاکش که خودشون استعمار رو اختراع کردن به ما می‌گن استعمارگر، کیرم دهنتون
#hjAly‌</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/news_hut/72198" target="_blank">📅 21:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72196">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">نتانیاهو: ما به کشورای زیادی کمک کردیم، یسری از همین جاکشایی که الان رفتن بیرون هم از ما تشکر کردن، کیر تو هرچی ریاکاره
#hjAly‌</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/news_hut/72196" target="_blank">📅 21:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72195">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">نتانیاهو: نابود کردن تاسیسات هسته‌ای جمهوری اسلامی سخت بود ولی انجامش دادم، اگه این کارو نکرده بودیم همه مرده بودیم
#hjAly‌</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/news_hut/72195" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72194">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">نتانیاهو: نمی‌زارم آخوندای قاتل به سلاح هسته‌ای برسن
#hjAly‌</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/72194" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72193">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">نتانیاهو: کیرم تو جمهوری اسلامی
#hjAly‌</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/72193" target="_blank">📅 21:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72192">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم
#hjAly‌</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/72192" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72190">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سخنرانی نتانیاهو از این لحاظ که قبل از انتخابات اسرائیله مهمه، می‌تونه از جنبه‌ی جنبه‌ی تبلیغاتی این تریبون استفاده کنه، کارهایی کرده و کارهایی که می‌خواد بکنه!  این سخنرانی تا دقایقی دیگه آغاز می‌شه #hjAly‌</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/news_hut/72190" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72189">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teFQhTuw61c7XPbiuxg3vrVTpUJcDKR9onR73Srpo4qdUbAeVi2wC1oVnC9Y6A8A_CxVwTFxU6_g2051vZIP2OKUbrL1TjV6x7PgO4SwKmJiT5NyDVwkWoLNdJ9Sk6II8e3AzihuYuDjjrHD-eyzLxDbgpqN2MsDAvy4sn0yfXqvV0qEwYEo0Pn3lNkt-RHfKHUmm3hghhM5RyPkp6yv5L1uh-O1Itq8OKIsh0QvG-wG1DaD9lqPn-9-9bU5euvLPGLD_xHsJwZCsl-moQcE23bn2ErYFzxwNxOKzp_T2B15ys6glJVI40920YUxKWyfXCErV99ZExCyrglBW4RpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان درحال مصاحبه با فاکس‌نیوز آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/news_hut/72189" target="_blank">📅 21:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72188">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7c569da6.mp4?token=kTcnO9GpZWTsbu2nvKRD0cA2NGQBYsHF18eZnSbubXBzUGdwSRSOf8YyFLPch8WuY1b4xBQELeyUiBhTatIJEmqmnxFy9ZSvQB8UhNGTXnshxch0ti6PRkQepyrlm_QHIX1UeVaryCvnljKQmweCiYgkLTnBvnnDisaeXfG1SNVijQyG4-TQ5rw_psq_1H-5sUP00jvMtChF47ozqdk3IF22nK-uqhD2e_ys8AvReZO-fR_3DyRc1E0Cnl_In3-DvFQ2j4e0INoJrTXv15wlnwQQTU_TmfFc_Dps2YHnAJlu99JBayVD1WqDDuT0Cu8OHFqhhjgTSXn64u4HOYODkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7c569da6.mp4?token=kTcnO9GpZWTsbu2nvKRD0cA2NGQBYsHF18eZnSbubXBzUGdwSRSOf8YyFLPch8WuY1b4xBQELeyUiBhTatIJEmqmnxFy9ZSvQB8UhNGTXnshxch0ti6PRkQepyrlm_QHIX1UeVaryCvnljKQmweCiYgkLTnBvnnDisaeXfG1SNVijQyG4-TQ5rw_psq_1H-5sUP00jvMtChF47ozqdk3IF22nK-uqhD2e_ys8AvReZO-fR_3DyRc1E0Cnl_In3-DvFQ2j4e0INoJrTXv15wlnwQQTU_TmfFc_Dps2YHnAJlu99JBayVD1WqDDuT0Cu8OHFqhhjgTSXn64u4HOYODkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حوزوی‌ها به روش خودشان برای بهبود چهره روحانیت در اقشار میانی جامعه کارزار به روز شدن راه انداخته‌اند؛ آنهم با «جوانگرایی»!
یک آخوند مبلغ، طلبه جوانی به نام «رضایی» را به شهربازی مشهد برده و از هر فرصتی برای مالش و ملعبه با او استفاده می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/news_hut/72188" target="_blank">📅 21:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72187">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcfa6b3480.mp4?token=SqTtSvw1wgdHNfT12gIbFrlnQ1q7AdTf3oC-4RqKM1flRPGppklMnbrFXB9kb7W7jQ88HjiURGv5EjX2x0aILDneipuFaNYfBx00zroFodjdWwqY2mnuJEr3MA_mREpUV17eTDtrwIQvlztHKQdcacgiQPe3G-rJNkOeTemSFT0SDSAQctKerRdf1AfcJBDg63pUEKEBYJsZwbXfLpjQF2MEQ6m_gc7AlWEFwyl3OlsJaNLAqTnRo5BzPIBGLjdYHbx3OzNP-OO9AI1GyIpS2yfZL5Q6FRYqbSIBYmVmWC5ouK---x2sCHhOh66ERJvg_x3jZpo15-b9i7C9acTJtYpcHsuLEDfNwAf2vVbDp639sxkETkN_QXvZelZDtqI96TsrvEb_m36B4cCGRmS-OkfWMSwEcyMQybaAHhH_tEhT1LAeKw55Pl-fTjfcceMvZdN4zyZoD2cYIXyshrAalIRl9gcttR5iqUxUIJujEjLltvA-DejwwrTcg00ENW3ELBllxV6zFftq84DMDCyYOyRhmtRlFrUXpP91YftjI03XlrnBRQy8dZMvWj1sbTVTf-Ra-FbwyRPhm4CmYiTrkLySPAciAvpZUaMvR3jh1liLxikMXKUM8sbWl3rKzMqEKCc6qCSSxXRBhsDJL8ZqC5ioMSXMTPMcBRbDpEtPRmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcfa6b3480.mp4?token=SqTtSvw1wgdHNfT12gIbFrlnQ1q7AdTf3oC-4RqKM1flRPGppklMnbrFXB9kb7W7jQ88HjiURGv5EjX2x0aILDneipuFaNYfBx00zroFodjdWwqY2mnuJEr3MA_mREpUV17eTDtrwIQvlztHKQdcacgiQPe3G-rJNkOeTemSFT0SDSAQctKerRdf1AfcJBDg63pUEKEBYJsZwbXfLpjQF2MEQ6m_gc7AlWEFwyl3OlsJaNLAqTnRo5BzPIBGLjdYHbx3OzNP-OO9AI1GyIpS2yfZL5Q6FRYqbSIBYmVmWC5ouK---x2sCHhOh66ERJvg_x3jZpo15-b9i7C9acTJtYpcHsuLEDfNwAf2vVbDp639sxkETkN_QXvZelZDtqI96TsrvEb_m36B4cCGRmS-OkfWMSwEcyMQybaAHhH_tEhT1LAeKw55Pl-fTjfcceMvZdN4zyZoD2cYIXyshrAalIRl9gcttR5iqUxUIJujEjLltvA-DejwwrTcg00ENW3ELBllxV6zFftq84DMDCyYOyRhmtRlFrUXpP91YftjI03XlrnBRQy8dZMvWj1sbTVTf-Ra-FbwyRPhm4CmYiTrkLySPAciAvpZUaMvR3jh1liLxikMXKUM8sbWl3rKzMqEKCc6qCSSxXRBhsDJL8ZqC5ioMSXMTPMcBRbDpEtPRmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇱
🇮🇱
شماری از نیویورکی‌ها در اعتراض به حضور بنیامین نتانیاهو در این شهر تظاهرات کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/news_hut/72187" target="_blank">📅 21:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72186">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سخنرانی نتانیاهو از این لحاظ که قبل از انتخابات اسرائیله مهمه، می‌تونه از جنبه‌ی جنبه‌ی تبلیغاتی این تریبون استفاده کنه، کارهایی کرده و کارهایی که می‌خواد بکنه!
این سخنرانی تا دقایقی دیگه آغاز می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/72186" target="_blank">📅 21:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72185">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90322c0135.mp4?token=W-O0XwwoZXFt6o-MkQCjFhwTYUrJEmM397zeYI2sVl3Mncp-Xs81P9tVpot69OspDBPeO-Svor87WN57CjHpuq0UamtPln6UgiFTWvcMeZWDHATxopCcIcJOTv_tHWfvbkRiozcGtWl5GbwuaoDM9HHoWbwjWe6ky_uDGsa8I8t_lcx15M7RpqmRvjYDhHfrXMm_-xGuabAYnh6vQuDP7NrZJibYZETdMlO-mCqKci_Rj6_Xk-Pgw0DNlipisfcjNz2_RzIDEEsGj5NNYPzWfDgoFnydfhwpIo2m1HwY5inG_YMB61LCuYelpauw3YITWzIIcs9HNCQLlBFzDwdqOTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90322c0135.mp4?token=W-O0XwwoZXFt6o-MkQCjFhwTYUrJEmM397zeYI2sVl3Mncp-Xs81P9tVpot69OspDBPeO-Svor87WN57CjHpuq0UamtPln6UgiFTWvcMeZWDHATxopCcIcJOTv_tHWfvbkRiozcGtWl5GbwuaoDM9HHoWbwjWe6ky_uDGsa8I8t_lcx15M7RpqmRvjYDhHfrXMm_-xGuabAYnh6vQuDP7NrZJibYZETdMlO-mCqKci_Rj6_Xk-Pgw0DNlipisfcjNz2_RzIDEEsGj5NNYPzWfDgoFnydfhwpIo2m1HwY5inG_YMB61LCuYelpauw3YITWzIIcs9HNCQLlBFzDwdqOTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇺🇸
🇺🇸
🇨🇳
دونالد ترامپ درباره شی جین‌پینگ: «شی در زمینه سنگ‌ها متخصص است و عاشق گرانیت باکیفیت است.»
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/72185" target="_blank">📅 21:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72184">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d872351dfc.mp4?token=kHq2nMCsraU0nKS0Hli0KcXBOBYWk3FzeCvCCCcRD9fjJBQU4YTcIOtJdDBVt469ros2VUXiGG-WPETNwY2uTGtRAbcHDbuqgDwaTgQ51x6j_DEkm8yOmPr8t_h_GizTJ0c2AkSkcvlLAD3rT1Us0rRxOs1hLfj_3GWfBhUB5b4F_6m910rcaMULr5Wl3J6zhGoo9-_jibts_ee0zKQAqaJr99x6mGLMPVAsQyC9SsBfQ9q8lxmYQn4wrNqWu3EfyPkP6tKFaEIFAvlr9nYqzTZDb0AstX28OUixvKArWPpCEjwtaVfKk0emHWkVyP5l0eWk7yMi4uu8Ui6xMVaul1jDR-HvF_T6UVhMsNWUCN6aM6reudjQL0wdKxv60pee5XsdtZ65eFjrjOaunKw4CKXdeQzJ_mLSEwDuUjrKQxKl2-CPdjt6aCidOQNDCxcDbZX0TRGWb0isMjG8X1bxE4N3ucRfLz2XSOHeoY-XrGHuXaMm8u5aX8bdciQQ85QBms90b0ufkIVjXfiGUmx4jSF3Jqckv7j56Z1jxRaRcz3u2lpV1HNB_UfgHuzr1PUlu9l71wvLMU17JSPjEwI4aouH8cc9CDfKN-5r18JKJvFbnPTNlQ32sHiv5BdrpSQ2uK9XQvM6ZUQP5LA4oJ0kz0pYQtEJHc9qzsFOvX8Niak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d872351dfc.mp4?token=kHq2nMCsraU0nKS0Hli0KcXBOBYWk3FzeCvCCCcRD9fjJBQU4YTcIOtJdDBVt469ros2VUXiGG-WPETNwY2uTGtRAbcHDbuqgDwaTgQ51x6j_DEkm8yOmPr8t_h_GizTJ0c2AkSkcvlLAD3rT1Us0rRxOs1hLfj_3GWfBhUB5b4F_6m910rcaMULr5Wl3J6zhGoo9-_jibts_ee0zKQAqaJr99x6mGLMPVAsQyC9SsBfQ9q8lxmYQn4wrNqWu3EfyPkP6tKFaEIFAvlr9nYqzTZDb0AstX28OUixvKArWPpCEjwtaVfKk0emHWkVyP5l0eWk7yMi4uu8Ui6xMVaul1jDR-HvF_T6UVhMsNWUCN6aM6reudjQL0wdKxv60pee5XsdtZ65eFjrjOaunKw4CKXdeQzJ_mLSEwDuUjrKQxKl2-CPdjt6aCidOQNDCxcDbZX0TRGWb0isMjG8X1bxE4N3ucRfLz2XSOHeoY-XrGHuXaMm8u5aX8bdciQQ85QBms90b0ufkIVjXfiGUmx4jSF3Jqckv7j56Z1jxRaRcz3u2lpV1HNB_UfgHuzr1PUlu9l71wvLMU17JSPjEwI4aouH8cc9CDfKN-5r18JKJvFbnPTNlQ32sHiv5BdrpSQ2uK9XQvM6ZUQP5LA4oJ0kz0pYQtEJHc9qzsFOvX8Niak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو به مقر سازمان ملل در نیویورک می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/72184" target="_blank">📅 20:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72183">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=d75cbENqfC4k8wlXZPWwkz0oYaB4_gEFKUauHPGKQwFb4k9c3xeiMbXmx84RVubv7Lf18JIelfX_Utdd27yexsCUxzW8U0uc58Ah2TdKdURWfFHTzQbE9gTS8luPZRco2QIeBL9PEWKFwCEKz8mbjZ-WX6liIanJmsZGENHSJHL3QfgNW43I0PZ6IrQaGPmCwgGjaZGzC-d0mONkr_TUCs5kU19rlPBhuXOpPLkT3Q0z9gDZ-qtRCZCOAyfUBZfz85OC6E5KAlYHGu12BW64nPMLJbbpfbv0YolQxKRMzad5vNkjcWNy6F8yAdHFWF1LN4cqMYrlm38i04coCjQzNKTzWvqYVO5Y4RWXMDRrE0uicTUxg7U6d0udctsqUdRc-cip_z39Fi8QhS3M4UzdNOwv787lNM1tRNjQioo3hNE8k_dOQpqilmbGEwttcC0Mw3jmCHDAQ3GKkb-zXPzQpW9D2aPYcZF1nHmBcUnPC1q4r6umFBACkw9SnHth90wI2Q2tXJQh5VdKZZD-D4eGcIly2Bt8OwLMXqRf0j8PFSmKGDWpJF1-zHFoJe27Ki2Knuu0TW35Cc-clVkhez-mI3UAj1qmBvNjUxLm7eugH2qrgbyzcWJtCqo0vCFseQDmKfzPrVOgBIhKCBe_YhICq1BHQ6B1Jjcr_8I0Gfvh-Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fcd656bf7.mp4?token=d75cbENqfC4k8wlXZPWwkz0oYaB4_gEFKUauHPGKQwFb4k9c3xeiMbXmx84RVubv7Lf18JIelfX_Utdd27yexsCUxzW8U0uc58Ah2TdKdURWfFHTzQbE9gTS8luPZRco2QIeBL9PEWKFwCEKz8mbjZ-WX6liIanJmsZGENHSJHL3QfgNW43I0PZ6IrQaGPmCwgGjaZGzC-d0mONkr_TUCs5kU19rlPBhuXOpPLkT3Q0z9gDZ-qtRCZCOAyfUBZfz85OC6E5KAlYHGu12BW64nPMLJbbpfbv0YolQxKRMzad5vNkjcWNy6F8yAdHFWF1LN4cqMYrlm38i04coCjQzNKTzWvqYVO5Y4RWXMDRrE0uicTUxg7U6d0udctsqUdRc-cip_z39Fi8QhS3M4UzdNOwv787lNM1tRNjQioo3hNE8k_dOQpqilmbGEwttcC0Mw3jmCHDAQ3GKkb-zXPzQpW9D2aPYcZF1nHmBcUnPC1q4r6umFBACkw9SnHth90wI2Q2tXJQh5VdKZZD-D4eGcIly2Bt8OwLMXqRf0j8PFSmKGDWpJF1-zHFoJe27Ki2Knuu0TW35Cc-clVkhez-mI3UAj1qmBvNjUxLm7eugH2qrgbyzcWJtCqo0vCFseQDmKfzPrVOgBIhKCBe_YhICq1BHQ6B1Jjcr_8I0Gfvh-Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرواز یک بمب‌افکن رادارگریز B-2 و چهار جنگنده F-35 Lightning II بر فراز کاخ سفید در جریان سفر رئیس‌جمهور شی.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72183" target="_blank">📅 18:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72182">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Wj1dZ-ZAPByxSVL8ldzaTGiBXc1ecNiXQ2pgVptn847DAjjufQVcNG5U9XnbDQB_qZWdw5-lbY1BfZM8SOePdEcgVTYHySNBuJr5bMK93DheqRpjDxFemmq2crerhOKVOdqYiQpCm-YXc2qIrmYacH6GGUFD8nS4hXhCIHWShRXFXvAUqUCQ_7pOa5nekfrTYyxeBX38SnGBiLyIpTBsHX3EwJgPoow3vNG_6SW9BICVRFIRRFwYtUc5rl-4BbykiRRSQZOCUhGM1bq2na-SU2OfimAzLY-rZpVqqTQJSl960TUyeckJ7ABKZjPb2mhJbNWTKW0Iiej-J4D8ilS20w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تانکر ترکرز گزارش داده است که نزدیک به شش میلیون بشکه نفت خام توقیف‌ شده ایران به ارزش حدود (600 میلیون دلار) در حال عبور از اقیانوس اطلس به سمت خاک آمریکا است!
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/72182" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72181">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=vqPXVLNbGG_4snu4VpeRNP-SnpDXBiXzyaQn5mW6EHgRr0B53izAtAZ0jwMNI9VkiNBWf668Xe6wKnbPrXHHd5RgtXKasvH_k8wX5MHhi85uqpRcT2u_px2SERWWFAAQctzfAM0eyvJx6tq0A-NNnL5MdQV0HdjUe5FyOkKKgPB50troSnjDeMbZCSWBrpn-6n-VefQTGCE0I-92HUC95TP9PZ6KsTFmjtKMmhm8LRSLsEi2q-iVP2yyApJ-js3VDIoF2fjRcR_Sqy_4J31VPHqszh8pfYmsS1xwMy5NCcNFWX9SYgSnkMRmci2NSx6HOnEhdzEROLhASr9ETsVzrATRS0kVdnwQw-T6ID73EHcHjhJUN2z3VNzJV72rhRW6WrHK8xGTYt_7wOOvt5MwpF-_TMouGG1nn-7OFNhcuhll0iTVdi3XJHeuJZo8Ru1LsjkNTVAimr8pcErkSCGsI3wnFqnK9LJycLgB1ZUabL6FLvowSiFXfcMWhJ-M3fS5qEGg9scvyv9WVDBONM1saszFGy2FSkNaqXUqpplio70HFZCG5qj52K6atTUz8cEYPUr6XAgaZyibz2qKUFbILkskgYJZ5w8BNRbhV7vJP2zPoTApJxj6L3pRLrJ7MvkW526eJUmkp4P79lSQ_TR1Zv5xzFi3KOJ_iAciIcZlWco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41a961ea41.mp4?token=vqPXVLNbGG_4snu4VpeRNP-SnpDXBiXzyaQn5mW6EHgRr0B53izAtAZ0jwMNI9VkiNBWf668Xe6wKnbPrXHHd5RgtXKasvH_k8wX5MHhi85uqpRcT2u_px2SERWWFAAQctzfAM0eyvJx6tq0A-NNnL5MdQV0HdjUe5FyOkKKgPB50troSnjDeMbZCSWBrpn-6n-VefQTGCE0I-92HUC95TP9PZ6KsTFmjtKMmhm8LRSLsEi2q-iVP2yyApJ-js3VDIoF2fjRcR_Sqy_4J31VPHqszh8pfYmsS1xwMy5NCcNFWX9SYgSnkMRmci2NSx6HOnEhdzEROLhASr9ETsVzrATRS0kVdnwQw-T6ID73EHcHjhJUN2z3VNzJV72rhRW6WrHK8xGTYt_7wOOvt5MwpF-_TMouGG1nn-7OFNhcuhll0iTVdi3XJHeuJZo8Ru1LsjkNTVAimr8pcErkSCGsI3wnFqnK9LJycLgB1ZUabL6FLvowSiFXfcMWhJ-M3fS5qEGg9scvyv9WVDBONM1saszFGy2FSkNaqXUqpplio70HFZCG5qj52K6atTUz8cEYPUr6XAgaZyibz2qKUFbILkskgYJZ5w8BNRbhV7vJP2zPoTApJxj6L3pRLrJ7MvkW526eJUmkp4P79lSQ_TR1Zv5xzFi3KOJ_iAciIcZlWco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از شی جین‌پینگ در کاخ سفید استقبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/72181" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72180">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72180" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/72180" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72179">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZndKmgMYnYTT-Xys8WjHP1lwRRjGXobczyKni3oWtMkDuVODfPghrAJUUydQlaVoTLrAyLZoGlPKhVLO6s_m853RZViI6WP_okn1OhUrtLv4itdnYS8Fup8QQLRK-ZfClong1vytTrKV4OYpJSLbNkaGFzekDENaJcZRZecKkmgljoLeIAJTLYbwnsrtwE4cG5_P24B9irNaqcawNpF2rqVUp0bNs17zbV3Pjo0_n7W52fgCttB7YpWxt_-Rpo0M4UDpVAcExzCoON7ufDHblfPVy3RgCGPlpLDnoE-EDuST9M6-bOqkTKdXIcnX-5I0Jrb2_GBT89aEWszZB9pkUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
ولز
🆚
پرتغال
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ولز: ۱ برد، ۳ تساوی، ۱ شکست و ۱۱ گل زده
پرتغال: ۲ برد، ۲ تساوی، ۱ شکست و ۸ کل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/72179" target="_blank">📅 18:14 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72178">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffI3scvaGt02E_-HTGpaXT8Np8q3Co7ld2eGIPctCpUBwJrJLBfk7Y9RYn3W_jNPPxbAqX6E5tCGuZsd8tWzZZmlgJItPWAqOQFnML5QSxoQBzKNqaS8ouNQ1_eOF8nGCD_wrhYFZiw4vDMNV5RC12CBkGxKUiG2-woVS3Qj94KSyUcrLlRHVwXJHxVWIutZWZjM74YILxIQZ_FfoQCvfWAC9WLZcGBb6isoG4myjoo1Cbt796v50cKN1dkL4wt-j0QiHdqxm-RQXqnWsBwPNNDZjaz0kvMu9_ThtKOF83UCv-ba65gTbGY4_zR2Brw-HXd9A5Y5h9sFPoIxOYDU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو برای شرکت در مجمع عمومی سازمان ملل وارد آمریکا شده است.
او قرار است امروز در نیویورک سخنرانی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72178" target="_blank">📅 17:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72175">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fibLwHkFfUHdlLIHUrct7gbRE2vlc9kNXGalZ5rkvb1bQKgZcbQP65zqkp8x8OglCuXV42V6TOP-OQDEOxqAbec9QKJeS1e7VQTUZrZN0HXF7a3l1JAkjT26cJaGyW5xf00Dzb8pyWypfQENOcpNqKijhfs8auTBrflxBmn30UYsMK3iVHvBz0q-cZLtKS32vOhuK2ltMjm18IwYfP_Kfa02nWVVQELn3XfDsO0s9hYOM1EF0O9ewqUBBt0UmyYUwi7WTiRNiarKHD9IB-8i4-fwp8HHKYpSW0KH7z0iwV4avhK4SA-u0qdqPWGExeuVceGxPA148KvZLKuMcuYhwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOg7OMcV7a1iJB14W-3MfQMKozDvOY_Yy9Jx4-f-7RJuAak_RBA09VIO-aS7MKXt_9mbK16sin_hPFRwISKdZVMv8TKAqYQt4kd5ZnMYpkHtgwkq68kw-G2F0HOqfXrwsQQ_J0WGcRxEz17pSou1cwDD-wM9-KnPbXiTfdcaSm2LpJImzf4HWTdd5Xy1XewK1zwhuzW7BFAmujI72wwuJiUNr1pyDpqT6RVENoeCQHxupbMk1dMc7DrE1BwEZWPa8e_ikiBflGMdThXpfqwaUw8s8j8gsb8FFBgUKstm6WkiUBZuHWlP7i_x_vLJ3u5Ega2UhjSx4la_2CHpyeLFtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=ZhguuaVX9jYQROVkWS7N2tFlrrKJL6lx8pN8zJRWH1w_LQbquK40SsEN_YZ3tZdk_hElCrVtx5MdYG9zUsP16rO2mXApwSbf2j1cYrXvdf4sbEtABnCXdWxU-UQB2FtckLxkB-pb8pTRFVaMdN7usPSfFxYbnBCAmqGhi5UO5iO6Sw7Y5O9hz7bvRzljTxEbKG6NDHPWIS0EbOMpJXq_BSAPmJ7dzRGQaxv3d7E9m6X-JSXsgAqvzKRFGHQPwcGq-e1EvjOkjDA3WGwidwlYcJ37DntuuA4OcPRUCjkWHrfTT0xkYyfgjfVUFquW7ec9b4kBRJCskjXgd-c2-yB_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e7959de70.mp4?token=ZhguuaVX9jYQROVkWS7N2tFlrrKJL6lx8pN8zJRWH1w_LQbquK40SsEN_YZ3tZdk_hElCrVtx5MdYG9zUsP16rO2mXApwSbf2j1cYrXvdf4sbEtABnCXdWxU-UQB2FtckLxkB-pb8pTRFVaMdN7usPSfFxYbnBCAmqGhi5UO5iO6Sw7Y5O9hz7bvRzljTxEbKG6NDHPWIS0EbOMpJXq_BSAPmJ7dzRGQaxv3d7E9m6X-JSXsgAqvzKRFGHQPwcGq-e1EvjOkjDA3WGwidwlYcJ37DntuuA4OcPRUCjkWHrfTT0xkYyfgjfVUFquW7ec9b4kBRJCskjXgd-c2-yB_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل منطقه «کفر تبنیت» در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72175" target="_blank">📅 16:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72174">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb1a6b62b.mp4?token=G1w0Ob23QLvbjIulKoZj6OijSZTMSHgjtzaFWTN3279uUjK0rUohF2po41ET-i2MC_NK-mMW9zVK0Snv7rtEAQl_PPpNipmNNZ_Iyob2SfX-5HzkL1o0APvr1UIVI7arZs14f-xNL1Nx-vy5bzih9N-JbIOG7pty1uuVl7VTitfpFrWVNeyIuuL4HKgM07A4JWV3qa78HYSZdBc9Oh7OqR6jlYJH82Q__DpKg1raq57ifuzeXIs39q4Ogljkd5P3-7VK2Acj7bYNkspeQWIaMDxKOIznj0huKF72cZcCoP5hdzsDtQT84RVvjUhvsMGFRReHYUoXoDDmylDpEMlyIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb1a6b62b.mp4?token=G1w0Ob23QLvbjIulKoZj6OijSZTMSHgjtzaFWTN3279uUjK0rUohF2po41ET-i2MC_NK-mMW9zVK0Snv7rtEAQl_PPpNipmNNZ_Iyob2SfX-5HzkL1o0APvr1UIVI7arZs14f-xNL1Nx-vy5bzih9N-JbIOG7pty1uuVl7VTitfpFrWVNeyIuuL4HKgM07A4JWV3qa78HYSZdBc9Oh7OqR6jlYJH82Q__DpKg1raq57ifuzeXIs39q4Ogljkd5P3-7VK2Acj7bYNkspeQWIaMDxKOIznj0huKF72cZcCoP5hdzsDtQT84RVvjUhvsMGFRReHYUoXoDDmylDpEMlyIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غذای مجلس ترحیم، اگر خود مرحوم. این نوع غذا رو خورده بود حداقل ده سال دیگه زنده می‌موند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72174" target="_blank">📅 16:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72173">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d6256f78.mp4?token=vebAuKPnK1yKOHVKN4cne0ZCx3PmGVudx2ln4tHbXZzgZHYWs77josXPUVIwTjBuBAvKXptVULs9l2vnBfz4NwEWBmy-3jo6zLCuGnT89Q88c-QkyKI_jh0sC1_v76vPpm9T0r8ClLigw2k0Jkh-bkmHgtpcE-v7EbNAEqQLgthjXpXIstADLwL_k-SamSZCXb3J5tFMueX5u4DFm_j3ATUhiJID_wtbSpCYSIsb9lY1l-4F75aMWdvDDi3tBaWa6ytldRQsaXgIp11lxiiXVzNfc49qyzTqnzsQlD485NfR2g8jLmqa7nSawwuKcQzEYRl7zF94AXz8Yu8oq3gwNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d6256f78.mp4?token=vebAuKPnK1yKOHVKN4cne0ZCx3PmGVudx2ln4tHbXZzgZHYWs77josXPUVIwTjBuBAvKXptVULs9l2vnBfz4NwEWBmy-3jo6zLCuGnT89Q88c-QkyKI_jh0sC1_v76vPpm9T0r8ClLigw2k0Jkh-bkmHgtpcE-v7EbNAEqQLgthjXpXIstADLwL_k-SamSZCXb3J5tFMueX5u4DFm_j3ATUhiJID_wtbSpCYSIsb9lY1l-4F75aMWdvDDi3tBaWa6ytldRQsaXgIp11lxiiXVzNfc49qyzTqnzsQlD485NfR2g8jLmqa7nSawwuKcQzEYRl7zF94AXz8Yu8oq3gwNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این آقا پسر برای تولد دوس دخترش ۲۰۶ خریده و اینجوری سورپرایزش میکنه :))
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/72173" target="_blank">📅 16:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72172">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a803db071d.mp4?token=iBBWkBBuJn6PxZkaHV-KYECtaPq9jmo3PqSpW-q3Mwxg5mLU64VeVsxxXgiMuA135YzizACNuQ8wFCgmzFGvjmjO_dVcs41j9jMUzWXF2EozSoZCwIunuD06xWwNHyrfmPBgpZ6VnBWKmvveDTV1F3amDyvTkGUB_5tiTkGyfhXT1UgLhO5aT2IwzmmCmkIbQBTR0gqJX4Cg7NcHDQvY4G12oRTIPReRvpTA16lsFSqOFEB_gek4C5h5QqJGE81It5ag9s06fdgAyaNHNO9Onsl0t3jioO3Q7-e5mQB956jvOdVwXfumgfVBozOg718YDVbS1X_bnPSITYck-RPuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a803db071d.mp4?token=iBBWkBBuJn6PxZkaHV-KYECtaPq9jmo3PqSpW-q3Mwxg5mLU64VeVsxxXgiMuA135YzizACNuQ8wFCgmzFGvjmjO_dVcs41j9jMUzWXF2EozSoZCwIunuD06xWwNHyrfmPBgpZ6VnBWKmvveDTV1F3amDyvTkGUB_5tiTkGyfhXT1UgLhO5aT2IwzmmCmkIbQBTR0gqJX4Cg7NcHDQvY4G12oRTIPReRvpTA16lsFSqOFEB_gek4C5h5QqJGE81It5ag9s06fdgAyaNHNO9Onsl0t3jioO3Q7-e5mQB956jvOdVwXfumgfVBozOg718YDVbS1X_bnPSITYck-RPuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور هائیتی در مجمع عمومی سازمان ملل خیلی جدی، از پارچ آب نوشید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/72172" target="_blank">📅 15:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72171">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b973e065b.mp4?token=sTBK3aRFn6995VS79-jW6V-ShDIoWrJAbHaxQ7j2BN9ePfpvUrLYmhdnlBdEl29EpxqZGy-3yiai_f1ZJtrWyenQ_oYzui83sOKLdnhkGIbLLKY1UzEfVOj1saP7xNxHerPEUblTqNf2-SOLibuOG-l1YrdyzgjiqhlMWtba2138babdedfFK2EoX2901oARIdXL7EygK8cZMDzVXNtmQgn_F-1jeGKSTZCuw84IHSuCVSwxkSB6RhlOPOoueD0t1BiJCgnb_U4ttAIXpE72lRR2z9EFR01qCuzR7oNG6DROFKH1QUf6-_VcWuYwGx_WkM838d2yjGdsvlQtY0GO7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b973e065b.mp4?token=sTBK3aRFn6995VS79-jW6V-ShDIoWrJAbHaxQ7j2BN9ePfpvUrLYmhdnlBdEl29EpxqZGy-3yiai_f1ZJtrWyenQ_oYzui83sOKLdnhkGIbLLKY1UzEfVOj1saP7xNxHerPEUblTqNf2-SOLibuOG-l1YrdyzgjiqhlMWtba2138babdedfFK2EoX2901oARIdXL7EygK8cZMDzVXNtmQgn_F-1jeGKSTZCuw84IHSuCVSwxkSB6RhlOPOoueD0t1BiJCgnb_U4ttAIXpE72lRR2z9EFR01qCuzR7oNG6DROFKH1QUf6-_VcWuYwGx_WkM838d2yjGdsvlQtY0GO7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماتون بریزه، ایران شده مهد عجایب خاورمیانه؛ این آقایی که می‌بينيد لاله گوشش رو سوراخ کرده و یه مار کرده توش.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72171" target="_blank">📅 15:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72170">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e89ab3721.mp4?token=u8jqRboLJloR6GpnBr-26clB11NqByNBEh2YFaZegHIM1MsQK5nXhEcRBSIoe_6glyN7Mjsj3J-sP9kuDFD9OxnEzeMJW_b4bOQ_Muxvw_XXpDLc68MdYVJItaLK8s8fQPcN5Wy28Nmeo0Txg4kpXQSK470TavN2Bh3T2bj2OttYQYs7Fdt71-4_hlGVsGKQBqT9LXAQ8Pt0sf8xc9OVRyCcOVdtuQ_C7BjUdX_xV_cwtyrSs9IQRtTJDRQDpr20WE895vSusIBev0836t27QXcygUpySsSsbf-xUNVw8RPPl2acNT0CWIIXTWKljx68Ymi1nJId8zNRMZHU3qTdvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e89ab3721.mp4?token=u8jqRboLJloR6GpnBr-26clB11NqByNBEh2YFaZegHIM1MsQK5nXhEcRBSIoe_6glyN7Mjsj3J-sP9kuDFD9OxnEzeMJW_b4bOQ_Muxvw_XXpDLc68MdYVJItaLK8s8fQPcN5Wy28Nmeo0Txg4kpXQSK470TavN2Bh3T2bj2OttYQYs7Fdt71-4_hlGVsGKQBqT9LXAQ8Pt0sf8xc9OVRyCcOVdtuQ_C7BjUdX_xV_cwtyrSs9IQRtTJDRQDpr20WE895vSusIBev0836t27QXcygUpySsSsbf-xUNVw8RPPl2acNT0CWIIXTWKljx68Ymi1nJId8zNRMZHU3qTdvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره ترامپ وقتی B-1 لنسر وحشیانه از بالای سرش رد شد دیدن داره
🤣
انگار اصلاً نمی‌دونست داره میاد
😂
قیافه شی رئیس جمهور چین دیدنیه
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72170" target="_blank">📅 14:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72169">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAGwXhtDlgzUiIgpEKR_YPVkOi2wQB3JL1pFxfwQOjwOkEOI-Ilfw71Q4p_WQaYaBu69BVPMP27t80DjfkJ_mRlvfoaY-4soWt9dDwMziGQ1umZgUYf51eSjOVAnne9CnKk7JLEIF0pHKMfL2rCTYhf4rZ-KX6i7DaVSz8M5SMCzrlo3oz3EKeJystCctFu5LxPZ_oZt6woO0FNFLRUPTWjmN8jf7K1NOOuvVHqooLyamMKpDBDl6KDs8lnFX-nV-h1wCHs-o4l2Q-C2tbFutW1-IKPhE-Ji_VP2YsoiId-butUXeniayZNWdn0cRtA9koVgNbIg0ZGs9tbr-6xB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش ایسنا و به نقل از سازمان هواپیمایی کشوری ایران، تمامی پروازهای شرکت‌های هواپیمایی ایرانی به مقصد امارات از نیمه‌شب لغو شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72169" target="_blank">📅 13:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72168">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=AO51_RrWOgivMK4hdVmIsL4TKMrLqZskGenuROzJ4xaL9yCjf1kO0Xr2U2XWFNLkR9XX9LG8qlHvA9t_cDl80uTXwwKhgRhJPv9MwqO8k9brSC4V6Y8uOQAxzRBescVbUXI_gWf901dwk1LYhH0tMRBAcECIvLUT3y1kBZWaSufnNxbSDgSSE-Lu8Wq5NVJ50fVJkkuGJD2cJW60ixyg-jH24PhFpxpSBkwURcPf2S_gpMgSxQnX5VuDZMfXFKAOwHkbm3n8P-WFxFdF_1Q6SA_dpb3SX2D2uq0JDUDFxebQJEA_xb9P6o8TzyxbXZEWpbLR3WKuojtFDsaRmbNyP173xWHKkagPR7sklOC0-U5CBBDgH6656RUqoUISP259Fon7VGUGFpuqP9NM05T3ebxPpFM6dO9lBlqbIWm7YkqFp-_Hdo2Zl0H0Bo_MobfZwsYTzNqelBUb30rvpE1_g_GGfYPB8c8oXYLmyZYeIEiYT1kNp98UKXZ9ZIw3CFMbdydT4wuVqMSLh_mKEZN40sbLnAF8BmxtCvtuI2zr3A2_RG4eGFEI20rd2mpgEslo6x094lZ2hTqUzR-G3EeQYrP-P3afV-VHzltGnyfl04dUPA8WNE1guvmtHLX8YY8WHli1_gr1FfEgb4_cxctyqAFP73ud1O4PtvM4nLBEGzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0e98c345.mp4?token=AO51_RrWOgivMK4hdVmIsL4TKMrLqZskGenuROzJ4xaL9yCjf1kO0Xr2U2XWFNLkR9XX9LG8qlHvA9t_cDl80uTXwwKhgRhJPv9MwqO8k9brSC4V6Y8uOQAxzRBescVbUXI_gWf901dwk1LYhH0tMRBAcECIvLUT3y1kBZWaSufnNxbSDgSSE-Lu8Wq5NVJ50fVJkkuGJD2cJW60ixyg-jH24PhFpxpSBkwURcPf2S_gpMgSxQnX5VuDZMfXFKAOwHkbm3n8P-WFxFdF_1Q6SA_dpb3SX2D2uq0JDUDFxebQJEA_xb9P6o8TzyxbXZEWpbLR3WKuojtFDsaRmbNyP173xWHKkagPR7sklOC0-U5CBBDgH6656RUqoUISP259Fon7VGUGFpuqP9NM05T3ebxPpFM6dO9lBlqbIWm7YkqFp-_Hdo2Zl0H0Bo_MobfZwsYTzNqelBUb30rvpE1_g_GGfYPB8c8oXYLmyZYeIEiYT1kNp98UKXZ9ZIw3CFMbdydT4wuVqMSLh_mKEZN40sbLnAF8BmxtCvtuI2zr3A2_RG4eGFEI20rd2mpgEslo6x094lZ2hTqUzR-G3EeQYrP-P3afV-VHzltGnyfl04dUPA8WNE1guvmtHLX8YY8WHli1_gr1FfEgb4_cxctyqAFP73ud1O4PtvM4nLBEGzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:جمهوری اسلامی در نهایت تسلیم خواهد شد.
نمی‌دانم یک هفته طول می‌کشد، یک ماه یا دو ماه، اما آن‌ها سرانجام تسلیم خواهند شد.
هدف در اینجا می‌تواند یکی از این سه حالت باشد:
اعضای رژیم به جان هم بیفتند؛
نوعی قیام مردمی در ایران شکل بگیرد؛
یا اینکه ایرانی‌ها را متقاعد کنیم که اگر خواهان توافق هستند، به آن پایبند بمانند.
این بار، اگر توافقی حاصل شود، تضمین می‌کنم که آن‌ها به آن پایبند خواهند ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72168" target="_blank">📅 13:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72167">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=VbF8QtOVr-jUZJIchRw-nV-2_NPYBIMvlzAXwT8UzWT3cTpNX2Xu2j-04fd2gSO2Ziu0sFOTnlR_N2nUJHgT6CfTFldJrkK7V5P74JpXNDvOwNf-YLBDQUY3Ftgex0WkjTQbGYC0fOG_0DSQVUa3vUHvUhzDb6QD-952ZKQxHslnwYSjl9Ua3cPADiCozNap-C5IU6mKdpO6upjhY8pnr234_mEct1V8m_BM9knSr5JnLzNtQ5kb6a_FsRWQgwCuQz-7q8oNOd9ICyo5qi2t76YN7UP1AcgN-kEeQIwF9C2FeRl4VDEaEiTNWk_yFy39S8RsKG1Ujoi_ZjyegBv87A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb27b8d8bc.mp4?token=VbF8QtOVr-jUZJIchRw-nV-2_NPYBIMvlzAXwT8UzWT3cTpNX2Xu2j-04fd2gSO2Ziu0sFOTnlR_N2nUJHgT6CfTFldJrkK7V5P74JpXNDvOwNf-YLBDQUY3Ftgex0WkjTQbGYC0fOG_0DSQVUa3vUHvUhzDb6QD-952ZKQxHslnwYSjl9Ua3cPADiCozNap-C5IU6mKdpO6upjhY8pnr234_mEct1V8m_BM9knSr5JnLzNtQ5kb6a_FsRWQgwCuQz-7q8oNOd9ICyo5qi2t76YN7UP1AcgN-kEeQIwF9C2FeRl4VDEaEiTNWk_yFy39S8RsKG1Ujoi_ZjyegBv87A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن رضایی دبیر شورای عالی امنیت ملی رسما فرودگاههای کشورهای همسایه را تهدید به موشک‌باران می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72167" target="_blank">📅 12:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72166">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=F8YSFgrhVwUNP9NQFtsiQGzbSdrUoS6GCSHAZp3tyrOVSMAvUJMWX5t92FAJ1v5Idhg8VP8o1Q91M3_VBRfkq6ZQn9zUvDZqS5jzHcABMh9t8Qlh15J3Sjiw0m2M9odQEz6iXLmdDJkY3epu4O72BG7CkFlKjs05zFxW3q9P8HVzgT6cHc9uGpBuwN6o2W8kTIwvi7ObUXOu0AsueGTbqign9vIMgK72u5d3E062eh2DhNL3tSWTU2JZBkR1UUt0W3EpM1KZiXZGLsbRMLmjdfefCEJMI7Z6zbL7H6cruxmsgtijVbOFyqU2JUn_5-AJkUop5dU_mkvOohbtEgAgHn_N9iBlADjdWozl2plaPkfnYzt-z78-XWfNPCXLTJDLLNPgCClJutRyD-3DAGOvTQ1TTDetETGDuiYc1OHShZQDmDKnmcKO5J-fRT4G2YbWOB72TFYXpKYjKcxZniQsgdRecZFKZTzE6UhrgSnPw-axux6Pk18PT0ibnoMrun4ABdGiXrWUggiIe748vMhaPAyQVtNx2kgVZYODsl48YN8KoFQ0tyjGK7Uqfys2JvZAtdKXYjqZpeFES2xJhIFap2HQj_a4wwt2GvWTmPqGLbmKtC3wndo2gHTAQAhx-WxU3sRgO7avP13segTlrba9S3-CP2lzq-zrHdsk2MGD9JE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd3cb8e2e.mp4?token=F8YSFgrhVwUNP9NQFtsiQGzbSdrUoS6GCSHAZp3tyrOVSMAvUJMWX5t92FAJ1v5Idhg8VP8o1Q91M3_VBRfkq6ZQn9zUvDZqS5jzHcABMh9t8Qlh15J3Sjiw0m2M9odQEz6iXLmdDJkY3epu4O72BG7CkFlKjs05zFxW3q9P8HVzgT6cHc9uGpBuwN6o2W8kTIwvi7ObUXOu0AsueGTbqign9vIMgK72u5d3E062eh2DhNL3tSWTU2JZBkR1UUt0W3EpM1KZiXZGLsbRMLmjdfefCEJMI7Z6zbL7H6cruxmsgtijVbOFyqU2JUn_5-AJkUop5dU_mkvOohbtEgAgHn_N9iBlADjdWozl2plaPkfnYzt-z78-XWfNPCXLTJDLLNPgCClJutRyD-3DAGOvTQ1TTDetETGDuiYc1OHShZQDmDKnmcKO5J-fRT4G2YbWOB72TFYXpKYjKcxZniQsgdRecZFKZTzE6UhrgSnPw-axux6Pk18PT0ibnoMrun4ABdGiXrWUggiIe748vMhaPAyQVtNx2kgVZYODsl48YN8KoFQ0tyjGK7Uqfys2JvZAtdKXYjqZpeFES2xJhIFap2HQj_a4wwt2GvWTmPqGLbmKtC3wndo2gHTAQAhx-WxU3sRgO7avP13segTlrba9S3-CP2lzq-zrHdsk2MGD9JE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«پرواز هواپیمایی وارش» از «تهران» به «دوشنبه» _پایتخت تاجیکستان_ از مرز هوایی لغو شد و به فرودگاه امام خمینی بازگشت.
این هواپیما سعی داشت از مسیر جایگزین و از سمت آذربایجان وارد تاجیکستان شود که مورد موافقت این کشور نیز قرار نگرفت
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72166" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72165">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72165" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72164">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAwMfgMjEonGIajxScOGkVoWN7AKj6e0-dn-lklao6PrGQruqIe4tWJRJsGRjEZV-EIY6ksQWShQfKjWVbzk1X6FrxeJt5GjB8d72w-QFH-fMEJAcWuZG5cbO1oiyxqRJ9jJgXo7sJwFeK-ioUgBoLn6P_d17md5Rxn5yhBgR7FR8kSKzwhJI_WbYPwkzx-KwWbJ9lOJUA8K8ffafyoFfo0jSI3c63DcBvDPUEj5_XaAzJyhypG4TdITzWPTum8HQxkwYogTkXUvm9e2TUqxpnLb9dfM2wn0tkll1S1mJ6z4V7yaER_58tEJPCsFV-zi44ym_EBKtxPZBXNZo3OiXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
هلند
دانمارک
🆚
نروژ
ولز
🆚
پرتغال
اروگوئه
🆚
ژاپن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72164" target="_blank">📅 12:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72163">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bbdedf07b.mp4?token=EzvTNuRqbsErtQhLAQarbSXwihbqt3tBqZ4qNIFM-o9rQaa-j-0vMQw2jsgKEyzJn9GkACjwaaI8UeEINs9awPt8TrMTH4Rs7aSaMxUL0y1z7AT6qBZlBtxlwRwdYZQYtdQn-czFiDA1ScTen7C7xzn8Cbub_xgB6TAux387GVpkp7M-Z_tTH5Rr0zVlz-eYtRs_FADfc8DIeUx02DloRPgZ1VlU9x-Vo5Bfgk4BeqFDseGs7OEo8tTS0L9g9bsdaDmOaV_eGfPsRk0KAbEqfuO5iIMnewnzGX2oq4Pd67BNkbDee32hrvAHEFUZ-GCkiIR5q5MU5B-YoSwXqOMRfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bbdedf07b.mp4?token=EzvTNuRqbsErtQhLAQarbSXwihbqt3tBqZ4qNIFM-o9rQaa-j-0vMQw2jsgKEyzJn9GkACjwaaI8UeEINs9awPt8TrMTH4Rs7aSaMxUL0y1z7AT6qBZlBtxlwRwdYZQYtdQn-czFiDA1ScTen7C7xzn8Cbub_xgB6TAux387GVpkp7M-Z_tTH5Rr0zVlz-eYtRs_FADfc8DIeUx02DloRPgZ1VlU9x-Vo5Bfgk4BeqFDseGs7OEo8tTS0L9g9bsdaDmOaV_eGfPsRk0KAbEqfuO5iIMnewnzGX2oq4Pd67BNkbDee32hrvAHEFUZ-GCkiIR5q5MU5B-YoSwXqOMRfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که یه پسر از روتینش قبل از رفتن به مدرسه منتشر کرده:
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72163" target="_blank">📅 11:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72162">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa04cd3fe8.mp4?token=jkAlnAIY0yhbw0pp9r86QDZJdwMuHwlU-3iOjUHX96cCNbUikxabycMOE1gi1peMqECsQoM9Ze-0_4pqPFSulWZYWk6fOVUcQQs1Bh0dF2cQrX5dCq-zZ_l5bkXcGIWC2JF61eLscEf2UBR8NvuT9DYVVNUJ1sxhlD16JuHV-K5S7zxxAcr84gdni-rXCLBgnu0BFHCqHmUkWj7dAbVm7PLVwNjfogBJmXXrOgd6rauRkBmviXeYPit5h5RotCubUr_ZJ68v4sV4DGYuK61CGzaz6T7axOfS2UqSVQlXCcow2TnOU39uYKrpOz4BAzLEugvTyM0aO30uuZk6bjXsSLtfcE_kIcRcWAOJrqoWZH-L0JleGEn4GUV0yxylBi98ljftbOC6RilH5mmBwCCf4qaHyKmVJ5eqPlrhK3-UDVt_WzBAr4z7h91PI6tBZaSHlj61_A1xec-W39-srsbJQe_g7NitLIxFqBgd-n22dG0wW7ltOLQP7PpsAc1y5JCrCkl-6or24WVawu0IpAbm7zbQgEuronXy4_wta5ZagW_3HXnC4dTw34dBiyl8J7EIkpiGuTl1tSGfSVyGbPeR_ZrDnt0xEOHqpwBi4QjRGEAY7HQLPlIWPaZhpahUMc84RtpVJZZYOd1Ls40KU0M2ZUZjH8G4SUIJTfPHMx11LQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa04cd3fe8.mp4?token=jkAlnAIY0yhbw0pp9r86QDZJdwMuHwlU-3iOjUHX96cCNbUikxabycMOE1gi1peMqECsQoM9Ze-0_4pqPFSulWZYWk6fOVUcQQs1Bh0dF2cQrX5dCq-zZ_l5bkXcGIWC2JF61eLscEf2UBR8NvuT9DYVVNUJ1sxhlD16JuHV-K5S7zxxAcr84gdni-rXCLBgnu0BFHCqHmUkWj7dAbVm7PLVwNjfogBJmXXrOgd6rauRkBmviXeYPit5h5RotCubUr_ZJ68v4sV4DGYuK61CGzaz6T7axOfS2UqSVQlXCcow2TnOU39uYKrpOz4BAzLEugvTyM0aO30uuZk6bjXsSLtfcE_kIcRcWAOJrqoWZH-L0JleGEn4GUV0yxylBi98ljftbOC6RilH5mmBwCCf4qaHyKmVJ5eqPlrhK3-UDVt_WzBAr4z7h91PI6tBZaSHlj61_A1xec-W39-srsbJQe_g7NitLIxFqBgd-n22dG0wW7ltOLQP7PpsAc1y5JCrCkl-6or24WVawu0IpAbm7zbQgEuronXy4_wta5ZagW_3HXnC4dTw34dBiyl8J7EIkpiGuTl1tSGfSVyGbPeR_ZrDnt0xEOHqpwBi4QjRGEAY7HQLPlIWPaZhpahUMc84RtpVJZZYOd1Ls40KU0M2ZUZjH8G4SUIJTfPHMx11LQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیداً دوست‌دخترای مردم دارن برای پارتنراشون آیفون 18 میخرن:
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72162" target="_blank">📅 11:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72161">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دیروز صبح، تو یکی از مدرسه‌هایِ اندرزگو تهران، شروع سال تحصیلی رو اینجوری شروع کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72161" target="_blank">📅 10:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72160">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c86f2846ed.mp4?token=Pyk-n_fcvGHOrG53xkFtt7KYHYk30nvAo8jGNy-UZWHEi2m70oWG6cWf97ApLZBYocpT0v4t4N8Y1FnDg6T_fMUPtj2YELWXMIRrhEGTOGzzANPaoINwP6_UE-jkDyKQy3q0KjEszvlPA7R2IVhoU_EiBL5cB5D4iNnpYfZUZORVpcXclqmKCxoovFmcFIMENC1CphyPXsNUCL9nHMmRBiDL1F22awE0N6ier1SkuSlEppAWrjdEssy_G403UqI0fGQus4A1XVMmPTOl-rngUbDUAzxAPWAuJjvdagce92Y99s3aY-0UK0K-RGkpE11qBaBNHS3cFlTeuwx3_2ZTlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c86f2846ed.mp4?token=Pyk-n_fcvGHOrG53xkFtt7KYHYk30nvAo8jGNy-UZWHEi2m70oWG6cWf97ApLZBYocpT0v4t4N8Y1FnDg6T_fMUPtj2YELWXMIRrhEGTOGzzANPaoINwP6_UE-jkDyKQy3q0KjEszvlPA7R2IVhoU_EiBL5cB5D4iNnpYfZUZORVpcXclqmKCxoovFmcFIMENC1CphyPXsNUCL9nHMmRBiDL1F22awE0N6ier1SkuSlEppAWrjdEssy_G403UqI0fGQus4A1XVMmPTOl-rngUbDUAzxAPWAuJjvdagce92Y99s3aY-0UK0K-RGkpE11qBaBNHS3cFlTeuwx3_2ZTlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسره از خروس میترسید و رفیقاش گفتن اگه بتونی 10 ثانیه نگهش داری، بهت آیفون 18 پرومکس میدیم.
و در نهایت این شاهکار خلق شد:
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72160" target="_blank">📅 10:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72159">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/034c3c71b1.mp4?token=Yc4eFmmtHy0byQBIlwmejDkAtwz6gL9XhJepo4YT03gR5joarSOpjZAqpRWfQYu-WavnMgAE7WMTSlgVhWlSf230MfLn1vnl6cQC18difKWRZaXXzfsXryvDF5Qq7tqmwXGw_d6xbgmxuYIg9TQAYtoH-u2iBYQPdNdj6C_T7lbjzfHs25gp37bWYJqiTCpG7XdMXjfqOXOmLax3Qy43CrcvoB6uFCIrcWavMxRwHaPMfn0Xu7QIoZIae2JDpQnX5CQv9lH7CVMgAg45UJONRyz7p7ofJbwH0nl5qNnkZAIlUbkNmQ8RcunGGUHuEo7rA3qEsJIk4HL-yRx-SBU8sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/034c3c71b1.mp4?token=Yc4eFmmtHy0byQBIlwmejDkAtwz6gL9XhJepo4YT03gR5joarSOpjZAqpRWfQYu-WavnMgAE7WMTSlgVhWlSf230MfLn1vnl6cQC18difKWRZaXXzfsXryvDF5Qq7tqmwXGw_d6xbgmxuYIg9TQAYtoH-u2iBYQPdNdj6C_T7lbjzfHs25gp37bWYJqiTCpG7XdMXjfqOXOmLax3Qy43CrcvoB6uFCIrcWavMxRwHaPMfn0Xu7QIoZIae2JDpQnX5CQv9lH7CVMgAg45UJONRyz7p7ofJbwH0nl5qNnkZAIlUbkNmQ8RcunGGUHuEo7rA3qEsJIk4HL-yRx-SBU8sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم لحظه سقوط یک جت آموزشی RAF Hawk T2 اندکی پس از برخاستن از دره RAF در انگلیس امروز را نشان می‌دهد.
هر دو خلبان به سرعت بیرون پریدند و زنده ماندند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72159" target="_blank">📅 09:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72158">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04b2935ddd.mp4?token=uuLkWkKHFNw_uS1OtESpYjYXBM13TslGTQhakO0fLGjlu_VVl24g6XZ7WvwBd3YA3K6moCbbKsuGeLkM8QvUHRM4z9kUQEbFZZqGCto4YVOeRgAJ4eLlnDI8teRuxuEUd9WhvgPCBigWA7g-bwAZ6B3i6xi07ftjDe_Low_pH4_EPLnePDXgsS_kUZmDh6jMvp-01WY1z7Ty34A3iv10ZhrDBE0sBjpEBL4qsFZncu9z8x9CGB3Rp8qmJwCY3gWwMdRApSIzAmUq3V-a3p2wdJ3-DG9q9U3qVyiyVK-XofPtuyNnxJm5YC3iTjWUMcE13QsvlWFyP2jXTlb8W5V31w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04b2935ddd.mp4?token=uuLkWkKHFNw_uS1OtESpYjYXBM13TslGTQhakO0fLGjlu_VVl24g6XZ7WvwBd3YA3K6moCbbKsuGeLkM8QvUHRM4z9kUQEbFZZqGCto4YVOeRgAJ4eLlnDI8teRuxuEUd9WhvgPCBigWA7g-bwAZ6B3i6xi07ftjDe_Low_pH4_EPLnePDXgsS_kUZmDh6jMvp-01WY1z7Ty34A3iv10ZhrDBE0sBjpEBL4qsFZncu9z8x9CGB3Rp8qmJwCY3gWwMdRApSIzAmUq3V-a3p2wdJ3-DG9q9U3qVyiyVK-XofPtuyNnxJm5YC3iTjWUMcE13QsvlWFyP2jXTlb8W5V31w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تعجب از  عکس‌العمل بی‌تفاوت نماینده جمهوری اسلامی در سازمان ملل، به تهدیدات ترامپ در یک برنامه تلویزیونی
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72158" target="_blank">📅 09:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72157">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad1a7d8580.mp4?token=dC6wV7ioKDLnuOcgdCXcNjVma_oVccbv8FLl_GfdeVNn8Z_FYx--_hSVVtihjnO9VpjU4H-n5Ye_GzKMm2jO5D9tl4bzwccYBgJg4pWMCR7fCmSxwp1id8-doSDsNtI1ccZ3IQKqkTTtZB4tzh_k3wuIa8W1F29VGBSuOwEydcRIHoH8WPQ0WNXTKPXFdDE_8eKQLIxYOrVco_QhQ3sSgpUvXyUpQikp61sc2vBvtBMrg1eGPq5MRaFDciy_NZSZ16mvytW23h6LCPV-H0X1MOSdNF0gdnvnbEyGVbGNhg6Jyd_FdRnj8pLRSupCdHVbu9o8YldP07BsrPke6eoA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad1a7d8580.mp4?token=dC6wV7ioKDLnuOcgdCXcNjVma_oVccbv8FLl_GfdeVNn8Z_FYx--_hSVVtihjnO9VpjU4H-n5Ye_GzKMm2jO5D9tl4bzwccYBgJg4pWMCR7fCmSxwp1id8-doSDsNtI1ccZ3IQKqkTTtZB4tzh_k3wuIa8W1F29VGBSuOwEydcRIHoH8WPQ0WNXTKPXFdDE_8eKQLIxYOrVco_QhQ3sSgpUvXyUpQikp61sc2vBvtBMrg1eGPq5MRaFDciy_NZSZ16mvytW23h6LCPV-H0X1MOSdNF0gdnvnbEyGVbGNhg6Jyd_FdRnj8pLRSupCdHVbu9o8YldP07BsrPke6eoA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
ممکن است به نفتکش‌ها حمله شود؛ اما بسیاری از آن‌ها به مسیر خود ادامه می‌دهند. آن‌ها صرفاً به حرکتشان ادامه می‌دهند.
ایرانی‌ها ممکن است ۳، ۴، ۵ یا ۶ پهپاد به سمت آن‌ها روانه کنند، اما نیروی دریایی قدرتمند ما مانع آن‌ها می‌شود.
با این حال، ما روزانه بین ۱۰، ۱۵ و گاهی ۱۷ میلیون بشکه نفت صادر می‌کنیم.
برای درک بهتر این ارقام باید گفت که پیش از آغاز درگیری‌ها، این میزان ۲۰ میلیون بشکه بود؛ ضمن اینکه احتمالاً ۳ میلیون بشکه دیگر نیز از طریق روش‌های جایگزین صادر می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72157" target="_blank">📅 07:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72156">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dfe7fd741.mp4?token=vDo6_6u9mdCdCJBJLsN-FBhlSGL6a2wfjuSVo576S7pr_9VUsZAvpeQ1tdGDLFBtBjymTSEIt8c2XFKJswdLw_Q2fS0Wqu8h0enCHmOKAI_ERB7XDTWLMagHWQgjMa8ursKGIR_tOfRQVaMwrc1bbn-14pGSKlo5HcLCWEOrASx6LBXqt97qyzfATYpSj0YSN0PSyqVkaTFeaCgaZ0W38sQcAR8UBZLDWLegAtlaKCszECoW3-GiKQVXpDWs2I03sTNHWq8YQo_3KiBXtm9TvzOWOn_SnKiujpzYVXvx-a99J9qJdxXh1wC5wK4RV7EsuPDZ5VZhHIgqFLslDH0uuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dfe7fd741.mp4?token=vDo6_6u9mdCdCJBJLsN-FBhlSGL6a2wfjuSVo576S7pr_9VUsZAvpeQ1tdGDLFBtBjymTSEIt8c2XFKJswdLw_Q2fS0Wqu8h0enCHmOKAI_ERB7XDTWLMagHWQgjMa8ursKGIR_tOfRQVaMwrc1bbn-14pGSKlo5HcLCWEOrASx6LBXqt97qyzfATYpSj0YSN0PSyqVkaTFeaCgaZ0W38sQcAR8UBZLDWLegAtlaKCszECoW3-GiKQVXpDWs2I03sTNHWq8YQo_3KiBXtm9TvzOWOn_SnKiujpzYVXvx-a99J9qJdxXh1wC5wK4RV7EsuPDZ5VZhHIgqFLslDH0uuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
احتمالاً بیش از ۸۰ یا ۹۰ درصد پروازهای خارجی از مبدأ ایران متوقف شده‌اند.
مطمئن نیستم نمایندگان ایران در سازمان ملل چگونه قرار است به کشورشان بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72156" target="_blank">📅 07:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72155">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72155" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72155" target="_blank">📅 01:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72154">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJWEPo8_ix7ICoDXgULGv7cgoqwfRVTjcxVi5j_KB5r8Q3ZJ1lw-sCa_-_mg_2RHlpj3gwayUMD5R_VE3q22ODdCZP91tSVJ2NhjZgylkmkbC1ti0FmDYbVaMrs46OuPcj8BsIbgInJ7w9VeK145CRugMM-AxFK4sR7IQJCOSqhXvXDAFADo9n6n4_T6iwj8bboZhsiexF6K8kcGQTPk53-_qhzFyvcfZ8j2F9NVsxiWUkFZJ5-BMblj_APhTbrOzzGIXbyH7oynUXGoecPLmtRRkvmNw6WH0l5yFxxPI12H4Iuaykghu9pHWskT-Lfz1uRJg5iC6DrtlhiZI5nwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72154" target="_blank">📅 01:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72153">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=CccEKfftWQf-xeyUiZzFmp5Db13b9i4ryAgJlsgW5IHN9BnhvkZM6-V6hUCZNSFE-kT-gqpWoF45zHEwiYZLLzz-a4YAab0-sIFPdVSAYLmMPEsWl8F23CmZdyE4GQ2YI23lw4tBhgMJw9kgY7VifNf3nrG9krkFZavPjoVf933Go4HabQVoy4lxE07d_Lnc0URaIRenpOIJR1kLLCDnfwzq2f53N8bYObOyCZlNYlnSARUP2CDEPbIYnjsa03zVz5XEKlrUj_GNWRBVVIA1i94hUSjRs5fnj0d-QylffqdwACje3Wf353zroLvGxc7eQZMoqcmPFyAUE0TeDivEaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c59219ac7.mp4?token=CccEKfftWQf-xeyUiZzFmp5Db13b9i4ryAgJlsgW5IHN9BnhvkZM6-V6hUCZNSFE-kT-gqpWoF45zHEwiYZLLzz-a4YAab0-sIFPdVSAYLmMPEsWl8F23CmZdyE4GQ2YI23lw4tBhgMJw9kgY7VifNf3nrG9krkFZavPjoVf933Go4HabQVoy4lxE07d_Lnc0URaIRenpOIJR1kLLCDnfwzq2f53N8bYObOyCZlNYlnSARUP2CDEPbIYnjsa03zVz5XEKlrUj_GNWRBVVIA1i94hUSjRs5fnj0d-QylffqdwACje3Wf353zroLvGxc7eQZMoqcmPFyAUE0TeDivEaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک فروند بمب‌افکن B-1 Lancer نیروی هوایی ایالات متحده، همزمان با استقبال پرزیدنت ترامپ از شی جین‌پینگ، رئیس‌جمهور چین، در واشنگتن، بر فراز این شهر پرواز کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72153" target="_blank">📅 01:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72152">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a5acb93e6.mp4?token=ZPOQdJ6Oto6EXoFztfqrf9qOdR7itaZ6EJhKpGzVr-sBgm1SXVY_rsj0GJI4vHnl4l02WTDeDb7u9eFnsji4Gpurz3Gz6qswTnF3nODopmEX9viZxpgn7wWD5KSEASEAlYO4qe4joXbVkdIN6KsBlEN1fBhPYENEPBNHsVQDKkJbcc4am-8gb4Uf9HYlE45HgvjW941QhwguMrYzAyb3a1hBcmfE3-n8UdPDczmheoFsfej71i7EZoMsciq-yMG6V9LzbWKdUdgU7PQDcA9K1dYkmITV6Mj451SowR504guiu9ov7GWx-89mL8bQ9rmMTihWzNBggZCQMXSlpSKkww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a5acb93e6.mp4?token=ZPOQdJ6Oto6EXoFztfqrf9qOdR7itaZ6EJhKpGzVr-sBgm1SXVY_rsj0GJI4vHnl4l02WTDeDb7u9eFnsji4Gpurz3Gz6qswTnF3nODopmEX9viZxpgn7wWD5KSEASEAlYO4qe4joXbVkdIN6KsBlEN1fBhPYENEPBNHsVQDKkJbcc4am-8gb4Uf9HYlE45HgvjW941QhwguMrYzAyb3a1hBcmfE3-n8UdPDczmheoFsfej71i7EZoMsciq-yMG6V9LzbWKdUdgU7PQDcA9K1dYkmITV6Mj451SowR504guiu9ov7GWx-89mL8bQ9rmMTihWzNBggZCQMXSlpSKkww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شنیده شدن صدای تیراندازی در جهاد‌آباد سراوان
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72152" target="_blank">📅 01:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72151">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4470cff685.mp4?token=dyg1yIyp8lY0LFnxSo8rD_hu7Ij1eujyfkX2noR8cvgCj_gr4tCfdLPglmcV18hiA0dNbOv0VJQLGOimcnXRu7o2AgGGXiw9qdPziiG_vz32z2NLAAZLFOnZNzesyVheXVD5Te9lJsoRzdLRCPAI4nmq1u1-FGkOZTtA9OaeFD3RlQt9TIkGYukUlT7NbYMdreA2IorjGX9Rk4BMGT_uSSHnBiI2kR5QYAaaaTAsIZyYF_cFDu_13BjTq-KYEUI7N7TB0wyTJBz5v_nBlXlBkdw3br0-M_SNoDupqtghyvAmvhvZglsRxHo0Lz1rn2Oela-5M-SUtxid1DYG6m-KXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4470cff685.mp4?token=dyg1yIyp8lY0LFnxSo8rD_hu7Ij1eujyfkX2noR8cvgCj_gr4tCfdLPglmcV18hiA0dNbOv0VJQLGOimcnXRu7o2AgGGXiw9qdPziiG_vz32z2NLAAZLFOnZNzesyVheXVD5Te9lJsoRzdLRCPAI4nmq1u1-FGkOZTtA9OaeFD3RlQt9TIkGYukUlT7NbYMdreA2IorjGX9Rk4BMGT_uSSHnBiI2kR5QYAaaaTAsIZyYF_cFDu_13BjTq-KYEUI7N7TB0wyTJBz5v_nBlXlBkdw3br0-M_SNoDupqtghyvAmvhvZglsRxHo0Lz1rn2Oela-5M-SUtxid1DYG6m-KXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شی جین‌پینگ رئیس جمهور چین وارد ایالات متحده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72151" target="_blank">📅 01:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72150">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رسانه‌ی حال‌وش :
دقایقی پیش تو محدوده‌ی جهادآبادِ سراوان تو سیستان و بلوچستان، درگیری مسلحانه‌ی سنگینی شکل گرفته به طوری که آرپی‌جی هم شلیک شده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72150" target="_blank">📅 01:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72147">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d2cde76e35.mp4?token=GtD1Qby88QVbBu5GPqW82YuwzOQyCkLNrJoejO21ndeIA0PGzJWaTGtgYnhwLua62SqM8XHMt1_O1dx61Kd4IfdCY-WXBo4s85GcZtwCurx6o0LCYYR_EDGjdnaBzuaLr45MwhfMK6HKV4xrqeN76_n1Uwe8WOjcZL_XypHnQ9-b0ufIBxbzdT_QV1EizOf14o8xxVS2_476kaFNYCCOK0MivYwBc9xDbqTkTLv_A2ZgSolfcvAL3RHtrKmSj7C1a77_fhOh02xAz7q4PO6RvTPzcH86vFGWhoMV1_3SUWkEty1VMweDpR77U_pcrT3mOcrmd4ouqwsZ32ZwDsId4g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d2cde76e35.mp4?token=GtD1Qby88QVbBu5GPqW82YuwzOQyCkLNrJoejO21ndeIA0PGzJWaTGtgYnhwLua62SqM8XHMt1_O1dx61Kd4IfdCY-WXBo4s85GcZtwCurx6o0LCYYR_EDGjdnaBzuaLr45MwhfMK6HKV4xrqeN76_n1Uwe8WOjcZL_XypHnQ9-b0ufIBxbzdT_QV1EizOf14o8xxVS2_476kaFNYCCOK0MivYwBc9xDbqTkTLv_A2ZgSolfcvAL3RHtrKmSj7C1a77_fhOh02xAz7q4PO6RvTPzcH86vFGWhoMV1_3SUWkEty1VMweDpR77U_pcrT3mOcrmd4ouqwsZ32ZwDsId4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«اتحادیه دریانوردان هند» (Forward Seamen's Union of India) خبر مرگ یک دریانورد هندی را بر اثر حمله نیروی دریایی سپاه پاسداران با دو موشک کروز ضدکشتی به عرشه C و موتورخانه کشتی فله‌بر «MV CAPE DAO» اعلام کرد.
کشتی «MV CAPE DAO» متعلق به شرکت «ForthMarin Corp Ltd» است که در امارات متحده عربی مستقر می‌باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72147" target="_blank">📅 23:35 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72146">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3ooH_jR1x0pgeAD_AgDfsMbk2lHw8Euf4cro23Al-vKP9wedfsujZTwY6LlKSlMVV-OlKx5qwydwGjKq2ngxSWR1hx1LGjKo_XwR__LpcgciAODeZmOnfKO61tRnIBV93wE8tOoLH5l9pzuYRSZo7DZaKDZ7wN8D8hv0r8GKGvln31E0Y1rQ2H7-cmpFYjwGE_9T13V5r5iBtGYAgrE8ifefWy8CHrZxsFpKT0dbZS9xw8tqVDmUqbv5E_VvG_KoWuWhJOJ9_HPFNrSBMHbtvx2aRcPHvsJpvMn2IKiFRE-7y8_MW5cDxDGFZWPi_mHNF8iXowsnp8p0jfS8fNr9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار ظریفی فرمانده سپاه شهرستان سراوانِ سیستان و بلوچستان، توسط افراد مسلح ناشناس کشته شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72146" target="_blank">📅 23:02 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72145">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=CBP27CNSxqX3LPBF_ZbPM1UDqOX0HJWRIvx49S3Ghkt_0L9fUT6uXJcBoL4-afE5PQ2mJ4X8Wh4-36ZaKg89NseNvLP09XJWpygdHJ59_ttGIc-RbiYfHWPNnEhJ1xD0rHesylo30WWkvlJ-wE9EpS1tpMAGDUlYuTipw1_NJ-dYk7ADocCHB_6nGoJwvWkwGA9o6WFqBuwDp6hsipa6hFjXy2S8_T7psnYIICftsj594-l-N6FgsKeYUAon_YdpdSdtkDcB9LJtKP4-yyPnM5--zhrNGtLnaSw1-xCD2ru8N50z5d3kSd3DClc_eDVjo_4UfcxTbQR21WLL9j94Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/223e8fa625.mp4?token=CBP27CNSxqX3LPBF_ZbPM1UDqOX0HJWRIvx49S3Ghkt_0L9fUT6uXJcBoL4-afE5PQ2mJ4X8Wh4-36ZaKg89NseNvLP09XJWpygdHJ59_ttGIc-RbiYfHWPNnEhJ1xD0rHesylo30WWkvlJ-wE9EpS1tpMAGDUlYuTipw1_NJ-dYk7ADocCHB_6nGoJwvWkwGA9o6WFqBuwDp6hsipa6hFjXy2S8_T7psnYIICftsj594-l-N6FgsKeYUAon_YdpdSdtkDcB9LJtKP4-yyPnM5--zhrNGtLnaSw1-xCD2ru8N50z5d3kSd3DClc_eDVjo_4UfcxTbQR21WLL9j94Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خواننده رپ آرمین رابر، برگزار کننده میتینگ های خیابانی رپ در اطراف تهران بازداشت شده است. او پیش تر نیز به دلیل اجرای قطعه آقازاده بازداشت و به حبس و جریمه نقدی محکوم شده بود...
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72145" target="_blank">📅 22:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72144">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تسنیم گرفت رو عراقچی:
تعامل عباس عراقچی، وزیر امور خارجه، با استیو ویتکاف، نماینده آمریکا، بدون مجوز یا هماهنگی با مقامات ذی‌ربط ایرانی، از جمله شورای عالی امنیت ملی، صورت گرفته است.
ادعاهایی مبنی بر اینکه این تعامل از پیش به تأیید نهادهای سیاست‌گذار ایران رسیده بوده، نادرست است.
بر این اساس ضروری است که آقای عراقچی درباره این اقدام غلط که مخالف مصالح و‌ منافع ملی است به نهادهای مربوط و ملت ایران پاسخگو باشد که با چه محاسبه‌ای این خطای بزرگ را مرتکب شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72144" target="_blank">📅 20:47 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72143">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=Tz6VT4IopafYc7PO_eptPRIwCWKhEHV3X6FKiRydv1njusuPUgD84fWWnFWbq2rpUyerV9kEiy48EUqDB4otbDaqVgXqnD_lUcZ5mdsYt8-ixH9vQM7OJF4QNiuS-NeZt9HH5nt4D2XvizMJdcC2zcQacwlXdEYBi6JFn9gLUbQllekvmOb40S3U0sAqXcbvSco_NwZWRYnUZtp2JE7eg-0gOyVtoDen9MbB3a-cEwTB-4GBcw6u83VZO2Akkra4Ce0E5jD_reSkNFcxUJLWLCgHFD5OnGTAJ1pl4Lwo9xigrmd6yXaXWmsziDaP21T9afAxkNQbmsgAu7jbxO2jVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d86a283f5.mp4?token=Tz6VT4IopafYc7PO_eptPRIwCWKhEHV3X6FKiRydv1njusuPUgD84fWWnFWbq2rpUyerV9kEiy48EUqDB4otbDaqVgXqnD_lUcZ5mdsYt8-ixH9vQM7OJF4QNiuS-NeZt9HH5nt4D2XvizMJdcC2zcQacwlXdEYBi6JFn9gLUbQllekvmOb40S3U0sAqXcbvSco_NwZWRYnUZtp2JE7eg-0gOyVtoDen9MbB3a-cEwTB-4GBcw6u83VZO2Akkra4Ce0E5jD_reSkNFcxUJLWLCgHFD5OnGTAJ1pl4Lwo9xigrmd6yXaXWmsziDaP21T9afAxkNQbmsgAu7jbxO2jVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنتاگون ۶ مورد دیگر از فایل هایی که در آن اشیا پرنده و ناشناس به اصطلاح UFO دیده میشه رو منتشر کرد که دو مورد اولی در خاورمیانه ثبت شده هست.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72143" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72142">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=CNZEO06M6N3SoRbP--Ejbf2NXtuUsd_TDe0yThM1N0z_8P5dutRByuft70BqtpubNmOzuMRP9_qjWPNbpxIzSlQMifudVYUeUosmocvo6oxAFT7pnWbJHr6t1uhQHy9fqTj_klLhKuRkZikhvjkLnzbFblr5hNlHs0jX18vUT1nH_-7gdw1L0yMTMfpEQY8GrmikmyB8ad2Jk6HinbXexJ46bYOPnoKyp4g4OUUOekxdUpqAj2wHjeCFoGmWp1XehAC0D9m1n8Qr9Rclq3HZTxc9EuBgi__Ilk0s00ViFVri4IzRQkg1q8RIfkCEW9r-CshDyeacW5voQenzoypmg4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9819ac349a.mp4?token=CNZEO06M6N3SoRbP--Ejbf2NXtuUsd_TDe0yThM1N0z_8P5dutRByuft70BqtpubNmOzuMRP9_qjWPNbpxIzSlQMifudVYUeUosmocvo6oxAFT7pnWbJHr6t1uhQHy9fqTj_klLhKuRkZikhvjkLnzbFblr5hNlHs0jX18vUT1nH_-7gdw1L0yMTMfpEQY8GrmikmyB8ad2Jk6HinbXexJ46bYOPnoKyp4g4OUUOekxdUpqAj2wHjeCFoGmWp1XehAC0D9m1n8Qr9Rclq3HZTxc9EuBgi__Ilk0s00ViFVri4IzRQkg1q8RIfkCEW9r-CshDyeacW5voQenzoypmg4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هموطن‌ها رفته یه مرسدس بنز خریده؛
همه منتظر بودن از خریدش ذوق کنه ولی صحبت‌هایی که بعدش کرد، جالب بود :
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72142" target="_blank">📅 20:37 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72141">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر  وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[لینک کانال] https://t.me/+fyrt-rnxFjNjMmQ0…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72141" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72140">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUWab2VIkEwC8IFhWG6MalsIn7yu1QFbaU6AEJrygbpRWoRghDTeWUqDlYj4UmLmfplPio3CUYgQEPFS7O82Ta731KgW2KhRjkZsqph0rB1V-VmxxxKAbmuMVHcyPuX3cBF-9fGgFPvUOLY-RBGfGaNKPM3zVVjjTz6hPuCVVSWbfMigIdMvW-xBsuLec1tcOiOf0mmdAWoWOiL8f1dAoTLw-pDlavDgddkxdsg8hVi0BxfWOFzvKpBPdtG4aJ1CQzAhmt6hzEOCJ_g_ZQpTCpZ9DjLfDxjAm2vMxd-eOcsXheJELksoiTvnX_WOhLBZza6hFuIAPxa3qZglX9I4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه هنوز دنبال یه کانال و گروهِ «واقعی» برای پیش‌بینی می‌گردی، درست اومدی!
👑
✅
تحلیل‌های اختصاصی و رایگان
✅
ضریب‌های طلایی
✅
گروهِ فعال برای تبادل نظر
وقتت رو با کانال‌های فیک تلف نکن. حرفه‌ای شو و با ما همراه باش.
👇
[
لینک کانال]
https://t.me/+fyrt-rnxFjNjMmQ0
[
لینک گروه
]
https://t.me/+jpSLBx8PcgBlMWI0
#TipsterPersian
#سود_تضمینی
#شرط_بندی_فوتبال
»</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72140" target="_blank">📅 20:36 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72139">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=N7fpbqjr6weAq1Stj2-iRY-4j55MS-_KWxcvDBg1ENp1ii6jB7IADIateWT5jkltiyymn0WYUr8GEA27kBrO0nZcQR1-Oljs_pOUX7c7NXHxhVswtyvG7Hah32kKp0XJJE6BZy2ZvTUIZv86F-C8UTA_sEO4Ui6MO6luiA23-VgJQEluk87wHGH-NhBsnGsAANBYkVl77BoismekwAANMVAkjaRvNibnK9fZde-R9G6lEhXnf4yrRJv0yi6RDia3NCg9Xqw1XKTJSzvfaQPlnWbn2O3M03-IJaVZzJzn3x30Ob_R7grPNiDwJEruSbKh0tsBYlW37lKwM2oh9F4xHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa977cc40.mp4?token=N7fpbqjr6weAq1Stj2-iRY-4j55MS-_KWxcvDBg1ENp1ii6jB7IADIateWT5jkltiyymn0WYUr8GEA27kBrO0nZcQR1-Oljs_pOUX7c7NXHxhVswtyvG7Hah32kKp0XJJE6BZy2ZvTUIZv86F-C8UTA_sEO4Ui6MO6luiA23-VgJQEluk87wHGH-NhBsnGsAANBYkVl77BoismekwAANMVAkjaRvNibnK9fZde-R9G6lEhXnf4yrRJv0yi6RDia3NCg9Xqw1XKTJSzvfaQPlnWbn2O3M03-IJaVZzJzn3x30Ob_R7grPNiDwJEruSbKh0tsBYlW37lKwM2oh9F4xHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتظار می‌رود سخنرانی نتانیاهو در سازمان ملل به شدت بر ایران متمرکز باشد و به گفته‌ی ایدز، این سخنرانی حاوی «غافلگیری‌های» نامشخصی خواهد بود.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72139" target="_blank">📅 20:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72138">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پزشکیان:
تو منطقه هیچ کشوری به تنهایی امنیت نخواهد داشت، یا باهم امنیت رو می‌سازیم یا باهم تو ناامنی زندگی می‌کنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/72138" target="_blank">📅 20:23 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72137">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15be798879.mp4?token=nfpuBopF-9Z8Q8Z6uXkY0epY4WFurA-RRkjngF0CYhbSrsqA5mLPtGdF2U23Z7pvZMFoDbMBkyILBp6YN6gcCtvAanVjInAa0TauXzrWbfrrF1LiItCDvyq9LGowOnGC7aCM2nlShLx0n1fN4HoHS84I3C0t3Ulloi180ywzX2kXI0zncN1kn0Bq_sIsHC5MirwjnrhUebHQdbeQQLRaUnmxZf6Pd40nxFjK94OkabJOMkt2cYmX1xgonCs4kN7fC7Gc1UjAUMZif76apboCzIrf5L-dS3WcLre7lOjjFOKwYCbhyWgBo1Yv2vO2Wq1FOmd8vGzR1BCoD8m15jL7dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15be798879.mp4?token=nfpuBopF-9Z8Q8Z6uXkY0epY4WFurA-RRkjngF0CYhbSrsqA5mLPtGdF2U23Z7pvZMFoDbMBkyILBp6YN6gcCtvAanVjInAa0TauXzrWbfrrF1LiItCDvyq9LGowOnGC7aCM2nlShLx0n1fN4HoHS84I3C0t3Ulloi180ywzX2kXI0zncN1kn0Bq_sIsHC5MirwjnrhUebHQdbeQQLRaUnmxZf6Pd40nxFjK94OkabJOMkt2cYmX1xgonCs4kN7fC7Gc1UjAUMZif76apboCzIrf5L-dS3WcLre7lOjjFOKwYCbhyWgBo1Yv2vO2Wq1FOmd8vGzR1BCoD8m15jL7dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم معلم قبل از شروع مدارس، برگشته به اولیای دانش‌آموزا میگه؛
بعضی از دانش‌آموزا هستن که پدر، مادر یا هر دو رو ندارن ؛
پس وقتی میاید بچه‌تون رو از مدرسه بردارید انقد قربون صدقه‌ش نرید که دل اون بچه یتیم بشکنه، برید یه جای خلوت‌تر بهش ابراز محبت کنید
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72137" target="_blank">📅 20:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72136">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bcb578f315.mp4?token=lmcG6NPnL2xy3Ya7hZQomI2pVzsmvRfTwo11d64IwRHji18WvN6tHUFtzZMtnpgR7Wj-_7lGZKzjQTZSAZPhLlLnOoW44gPD0W0Ut3crGbfiLCTLOdHsqL-Yrvof_6FjI1xYihidrCgIzHOebBRJMhYAVdGQudbf52fjWtGHhFmrC6QeuwVlIC4FksL7IS20TiWRGjX_6Q8liALWXT4rv_6Fto3xeXCitkG5cSCbuLggNdLbUvtg60JPJrzhXRd3zEQsBsDV15WZ3GtD7njHAOY3_rR066eG8TuaTnuAHBtED_06BC6FaHTZbwf5ebKtAgkRxIEfWB761d6SIjHuWg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bcb578f315.mp4?token=lmcG6NPnL2xy3Ya7hZQomI2pVzsmvRfTwo11d64IwRHji18WvN6tHUFtzZMtnpgR7Wj-_7lGZKzjQTZSAZPhLlLnOoW44gPD0W0Ut3crGbfiLCTLOdHsqL-Yrvof_6FjI1xYihidrCgIzHOebBRJMhYAVdGQudbf52fjWtGHhFmrC6QeuwVlIC4FksL7IS20TiWRGjX_6Q8liALWXT4rv_6Fto3xeXCitkG5cSCbuLggNdLbUvtg60JPJrzhXRd3zEQsBsDV15WZ3GtD7njHAOY3_rR066eG8TuaTnuAHBtED_06BC6FaHTZbwf5ebKtAgkRxIEfWB761d6SIjHuWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه زنه با شوهرش رفته بود خرید که شوهرش این حرکتو زد و آبرو برای زنش نذاشت :))
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72136" target="_blank">📅 19:33 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72135">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=A41me8n7onVDV6bVvK8RwNtd6pnny6T1Sj7ChglwR0eRS-4an22TiSlOowyueGZi8DJT0EjGLV3IRLWb9qaofdGIoqDcukzYgZmPpAhjeLaGOttXjjnpWqY1hB9rmNopTF8acTZlGiwQTwnTN25fBSzQBtwZJIzLiBM4snHDmBntCuHhoM-cnevq_3Nc-AiveIqhAdlcynh6oXbdB8Tt19CtBm5o1_OXdFF6i5aLVhQRisFeCHmLBsYFbvvm_nBO8j87EclwZJa9oecPwlJ0Y3dQHBC4OstiuNgPPpAknwmNqk2q_zqKfIp7F56n6xFkNzGLEfIsmtVyw2UmXxnI6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0aa24390.mp4?token=A41me8n7onVDV6bVvK8RwNtd6pnny6T1Sj7ChglwR0eRS-4an22TiSlOowyueGZi8DJT0EjGLV3IRLWb9qaofdGIoqDcukzYgZmPpAhjeLaGOttXjjnpWqY1hB9rmNopTF8acTZlGiwQTwnTN25fBSzQBtwZJIzLiBM4snHDmBntCuHhoM-cnevq_3Nc-AiveIqhAdlcynh6oXbdB8Tt19CtBm5o1_OXdFF6i5aLVhQRisFeCHmLBsYFbvvm_nBO8j87EclwZJa9oecPwlJ0Y3dQHBC4OstiuNgPPpAknwmNqk2q_zqKfIp7F56n6xFkNzGLEfIsmtVyw2UmXxnI6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
آقای ترامپ و کسانی که به دنبال زورگویی به ما هستند، باید ایران را بشناسند:
اینکه ما آماده گفتگو، دیپلماسی و مذاکره هستیم، اما زبان زور را نمی‌پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72135" target="_blank">📅 18:29 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72134">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=ejGnlk9z3ypL3UpeGsnZrfzCq-foN7pMkg_OxBsfcDPH6PC0491tsQuDmqjVCDNSKELk5uOEowsqKUVEgzIZg1pYFLs9b8FL5efatLj-iyYNuhEq14F9WaEMtT_-2A0oRClmGbRo4HxomIwa8TUtD0m-V5X9YF5p_kd1VKAVsgrN418zfLXEBxwuOmd74NexpFTmAtdW7sVOqDx9K6aijwFvyosSv5eC9MBqA9FTrBMPuaEUNmKRIrC3vDteIiYxrnodVHYSTc0_YeLlKKQY_rvp2N-9yZen041EmLiSIDc0lGrrnhQlGrV329Hp8FQwSYZZy9vIk7RZXE5vjByOBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80dd97167.mp4?token=ejGnlk9z3ypL3UpeGsnZrfzCq-foN7pMkg_OxBsfcDPH6PC0491tsQuDmqjVCDNSKELk5uOEowsqKUVEgzIZg1pYFLs9b8FL5efatLj-iyYNuhEq14F9WaEMtT_-2A0oRClmGbRo4HxomIwa8TUtD0m-V5X9YF5p_kd1VKAVsgrN418zfLXEBxwuOmd74NexpFTmAtdW7sVOqDx9K6aijwFvyosSv5eC9MBqA9FTrBMPuaEUNmKRIrC3vDteIiYxrnodVHYSTc0_YeLlKKQY_rvp2N-9yZen041EmLiSIDc0lGrrnhQlGrV329Hp8FQwSYZZy9vIk7RZXE5vjByOBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ترامپ باید بداند که مقاومت ملت ایران در برابر تحریم‌ها، افزایش فشارها و زورگویی‌ها، تنها بیشتر خواهد شد.
ما هرگز سر فرود نخواهیم آورد و زانو نخواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72134" target="_blank">📅 18:28 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72133">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مسعود پزشکیان:
بمب‌های اتمی و هسته‌ای در اختیار رژیم اسرائیل است، اما از بازرسان خواسته می‌شود که به ایران بیایند.
اسرائیل بیش از ۷۰ هزار انسان بی‌گناه را در غزه به شکلی وحشیانه به قتل رسانده است، اما ایران در حالی که پای میز مذاکره بود، هدف بمباران قرار گرفت.
اسرائیل بمب و سلاح‌های کشتار جمعی در اختیار دارد، عضو «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) نیست و در طول حیات ننگین خود حتی اجازه یک مورد بازرسی را هم نداده است؛ با این حال، همه امکانات لازم در اختیارش قرار می‌گیرد تا بتواند هر پایتختی در منطقه را که بخواهد، بمباران کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72133" target="_blank">📅 18:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72132">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=DnLOTBTEbajASfmWl5UBuF2EoLcj_MR4ooiDH6r6Ip3F3lv5ZhiTipyQYiBYAUdMafUDz8_VzRpoHpf3s8amG0AWfXlikIyhyNmwD4FKkz7xgzflkoQ54OaXqk-nV36skKpmqG0PiVfr1MudF2DFq51ugF2PutakMQmMu8s1vXZRwaVf757-GkIlG46f_6EEouk45GBrLD0Pgo7f97iPFWpn2fwoS2T1dH20ouTfKQKPXNgXBCasnNwNnZGUgwLtwZGmsvFr91GgAMPrudYAVETOdbDk0ju63QT56fOWDFRG8fXUL1WM1J8jqwb_FczbRsLFNvSdVkmtVWt--wpwXoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7f87b6f9.mp4?token=DnLOTBTEbajASfmWl5UBuF2EoLcj_MR4ooiDH6r6Ip3F3lv5ZhiTipyQYiBYAUdMafUDz8_VzRpoHpf3s8amG0AWfXlikIyhyNmwD4FKkz7xgzflkoQ54OaXqk-nV36skKpmqG0PiVfr1MudF2DFq51ugF2PutakMQmMu8s1vXZRwaVf757-GkIlG46f_6EEouk45GBrLD0Pgo7f97iPFWpn2fwoS2T1dH20ouTfKQKPXNgXBCasnNwNnZGUgwLtwZGmsvFr91GgAMPrudYAVETOdbDk0ju63QT56fOWDFRG8fXUL1WM1J8jqwb_FczbRsLFNvSdVkmtVWt--wpwXoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مسائل منطقه‌ای ما باید در درون منطقه و به دست کشورهای منطقه حل‌وفصل شود، بدون آنکه به ابزاری در دست متجاوزان خارجی بدل گردد.
هیچ‌گونه رابطه‌ای با یک قدرت خارجی نباید به ابزاری برای تهدید کشورهای همسایه در منطقه تبدیل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72132" target="_blank">📅 18:03 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72131">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=TGmCIeZk3BbmOiU2VANPB5BiiLzpD69EjkkAyt3VP14OKxXslYDmTuuvrG5CDoEvXDtINXuNzJIEu_Vrqa7hnS5Fccsubs1Y_hcxOvX0W5rJPMlpymRs6ZOs2aGsJXNrwN3hL9GuBn2NnxeewHPDRBN6JH6ZtaAdf9S9VVLrwCcOHrURLiEkdTYACcNSCRGhVFZRd95xRP6Qk1nDytw_zOs66P2_3a1SAtZJQOyLypdbTzZvbpU4nikGlaSnYO-s0ndZjq8fnPf5LbKklYOfQ9lCJOyOxrk3goKFmJH7zzJmV1kKTd6vTgV_dwOnnD5y-LgRTrePZekyKvvU3_gXGKnyuWcJhgYNhiFI4POSpBq7bm9JDIy59-ob99xXs2Y3wGKF-15ui-q7xxgJuHlWCiV89UAr5m9CAtgBSE_RpYqowE0IujBENb9iUvj8sXTZrdqf0dq87eg_X3G_wVyCQRUMZlcCVLL9YcfIykmDbXGTXnX3zXNjZl73fQwP4ZszrEzy3Ji6HyzNP81ddO6_ua9Zj51lEhUNZ1HxEWgf78kxYX9MZGr1OYjn9u9LL6x3ttCsspiogTL0x5QHbVzc2JVCTAbYZHD6ULHFbjlGKlCVoq1_uFajVelJRu9cHrQbkegf-QdQtqOn9X-uBv57QOfhXTEEiOANU5gkhvSg6xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4be5f428e4.mp4?token=TGmCIeZk3BbmOiU2VANPB5BiiLzpD69EjkkAyt3VP14OKxXslYDmTuuvrG5CDoEvXDtINXuNzJIEu_Vrqa7hnS5Fccsubs1Y_hcxOvX0W5rJPMlpymRs6ZOs2aGsJXNrwN3hL9GuBn2NnxeewHPDRBN6JH6ZtaAdf9S9VVLrwCcOHrURLiEkdTYACcNSCRGhVFZRd95xRP6Qk1nDytw_zOs66P2_3a1SAtZJQOyLypdbTzZvbpU4nikGlaSnYO-s0ndZjq8fnPf5LbKklYOfQ9lCJOyOxrk3goKFmJH7zzJmV1kKTd6vTgV_dwOnnD5y-LgRTrePZekyKvvU3_gXGKnyuWcJhgYNhiFI4POSpBq7bm9JDIy59-ob99xXs2Y3wGKF-15ui-q7xxgJuHlWCiV89UAr5m9CAtgBSE_RpYqowE0IujBENb9iUvj8sXTZrdqf0dq87eg_X3G_wVyCQRUMZlcCVLL9YcfIykmDbXGTXnX3zXNjZl73fQwP4ZszrEzy3Ji6HyzNP81ddO6_ua9Zj51lEhUNZ1HxEWgf78kxYX9MZGr1OYjn9u9LL6x3ttCsspiogTL0x5QHbVzc2JVCTAbYZHD6ULHFbjlGKlCVoq1_uFajVelJRu9cHrQbkegf-QdQtqOn9X-uBv57QOfhXTEEiOANU5gkhvSg6xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما سر خم نخواهیم کرد و از حقی که ذاتاً متعلق به ماست، دست نخواهیم کشید.
صریح می‌گوییم: نه سلاح هسته‌ای و نه هیچ‌گونه محدودیتی برای فناوری صلح‌آمیز هسته‌ای.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72131" target="_blank">📅 17:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72130">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2213909800.mp4?token=WTxXLLcEiTC5-lxNwdhMnzcCbHoEdo2mm3-OT91lgmPCj75w5Ojfdk4wdfkaP6D1Ii__UM0Sb1f_RpkRddAw9BpxaKWL1ZX8CnuzzSQqPbPSzhRXAXqTSkurqRMwwju4J_Y56FIK3k5jYN-5bYVsmc-0U_Zuy8nL0qtC7NMShuL5Wk5zDoDAAYX7HqRBc3tYQRVG6iOfBrQPzcyMP_hKuCPw-vy63UYvGWpTS6wrUpT2ak9Dh66ozg3W8x0SVTZoHxqH4V92KPVrcuQHkIJm3qAZnDAuI2u9f2oFjITzhm9WHxjNp5ES9DL4PqZcuYQPpyEaxaRUDLKElWpcnp1ESJd-PsvKBbKEDf_iLI_P_4accSCGcEQuqwPNy68DyNN2NC3f5V-4iatO-Lb2motPZxrYDp4UjbPjg63Kd7z9BGezoiGRCM84IK-jP9r_iekOqwf_KGEsEEt80k8-HSo9cvPUuAAFc05GnW-3pnqnXYPUlGSQu42pVID7Us4Fan-8bt_tROj_zpmrTgsuNseiqltQsbnRiTiUpPSy1jXp_AG5muC7gRa5pKcOwzGwU93IhQybWqRaEPBthkBW99Ey44-iEO8u12mtQMY4wfvg7EMg1D0Tfdtjt5sA1LSnQ_FhTjm6L-zS04ELZQqudSlFypxE5Uxy4Z0Fp_dPVHBq2b8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2213909800.mp4?token=WTxXLLcEiTC5-lxNwdhMnzcCbHoEdo2mm3-OT91lgmPCj75w5Ojfdk4wdfkaP6D1Ii__UM0Sb1f_RpkRddAw9BpxaKWL1ZX8CnuzzSQqPbPSzhRXAXqTSkurqRMwwju4J_Y56FIK3k5jYN-5bYVsmc-0U_Zuy8nL0qtC7NMShuL5Wk5zDoDAAYX7HqRBc3tYQRVG6iOfBrQPzcyMP_hKuCPw-vy63UYvGWpTS6wrUpT2ak9Dh66ozg3W8x0SVTZoHxqH4V92KPVrcuQHkIJm3qAZnDAuI2u9f2oFjITzhm9WHxjNp5ES9DL4PqZcuYQPpyEaxaRUDLKElWpcnp1ESJd-PsvKBbKEDf_iLI_P_4accSCGcEQuqwPNy68DyNN2NC3f5V-4iatO-Lb2motPZxrYDp4UjbPjg63Kd7z9BGezoiGRCM84IK-jP9r_iekOqwf_KGEsEEt80k8-HSo9cvPUuAAFc05GnW-3pnqnXYPUlGSQu42pVID7Us4Fan-8bt_tROj_zpmrTgsuNseiqltQsbnRiTiUpPSy1jXp_AG5muC7gRa5pKcOwzGwU93IhQybWqRaEPBthkBW99Ey44-iEO8u12mtQMY4wfvg7EMg1D0Tfdtjt5sA1LSnQ_FhTjm6L-zS04ELZQqudSlFypxE5Uxy4Z0Fp_dPVHBq2b8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ایران در دو قرن گذشته به هیچ کشور یا سرزمینی حمله نکرده، اما همواره با صلابت از خود دفاع کرده است.
با این حال، اکنون ما به ایجاد بی‌ثباتی در منطقه متهم می‌شویم و برچسب تروریست به ما می‌زنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72130" target="_blank">📅 17:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72129">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مسعود پزشکیان:
کسانی که خود تروریست هستند و تروریست‌ها را آموزش داده و از آن‌ها حمایت می‌کنند، ما را تروریست می‌خوانند. ما تنها از خود دفاع کرده‌ایم؛ ما تروریست نیستیم.
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با نهایت قدرت از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/72129" target="_blank">📅 17:55 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72128">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=jpjCqBPldr_6I8rgfGMhG1nGTdK8yRrwCz5ZK3-H3JgCAtBCYaazis4oVUtDHQVBf4eFx77uDu6G5z5npOEl17RLl6TqXICmwnCaUFm5rWewdVz9wryXtICb24Uj_F6vwKpbrXfX0l00CA-8PMVY_jtRGWzV3RCgfD_rXe8vg1hU_jiIyxtdPwieavDlHgBE-ACffL82WUT2AmYqLKF_YMnFY4qmAUA8vpo6WE7i7MkWGylTTJfTANGozo229vJaji-LOTd2giekK0vv3Fn3vO99C7O8JSJYRJ3uy2fE3OW_53HO93CbsSDtwUsas6hqdpnkL9TftQNlBUjRNv1nEFc9LQdpr0egPzh493ktZo7Q_dT4Y9QdW09D8sxg6Xh8kMT_0YPsNiBAPLViRgVM4ZEsvR-3Qp7AnTtuWcLeweTCFWWPOronrHF_q7a7NK0tjxIgNT6a9DzQ9KxyrJ8yC9uUxfeAYnkw4mEQH98XNPtmt1GmUi3ANJzojRaxWLcQDAGVLu09Vcz-Ua9ScAMyNU6S0hBnj04IvQHVIsQz17usV53kW-ji1PAy-ZIX4WWfG8RPps1-c6Z1FY88lIKXCHbCVsojBNHXBQhgSKMzEiPh5vfCrORBJ2uTHnbKEUBOgfmFsuNu-HiqL1gjaTISi9hPt_YnkKRfrXkWVXNjVUU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baa7d4e9f3.mp4?token=jpjCqBPldr_6I8rgfGMhG1nGTdK8yRrwCz5ZK3-H3JgCAtBCYaazis4oVUtDHQVBf4eFx77uDu6G5z5npOEl17RLl6TqXICmwnCaUFm5rWewdVz9wryXtICb24Uj_F6vwKpbrXfX0l00CA-8PMVY_jtRGWzV3RCgfD_rXe8vg1hU_jiIyxtdPwieavDlHgBE-ACffL82WUT2AmYqLKF_YMnFY4qmAUA8vpo6WE7i7MkWGylTTJfTANGozo229vJaji-LOTd2giekK0vv3Fn3vO99C7O8JSJYRJ3uy2fE3OW_53HO93CbsSDtwUsas6hqdpnkL9TftQNlBUjRNv1nEFc9LQdpr0egPzh493ktZo7Q_dT4Y9QdW09D8sxg6Xh8kMT_0YPsNiBAPLViRgVM4ZEsvR-3Qp7AnTtuWcLeweTCFWWPOronrHF_q7a7NK0tjxIgNT6a9DzQ9KxyrJ8yC9uUxfeAYnkw4mEQH98XNPtmt1GmUi3ANJzojRaxWLcQDAGVLu09Vcz-Ua9ScAMyNU6S0hBnj04IvQHVIsQz17usV53kW-ji1PAy-ZIX4WWfG8RPps1-c6Z1FY88lIKXCHbCVsojBNHXBQhgSKMzEiPh5vfCrORBJ2uTHnbKEUBOgfmFsuNu-HiqL1gjaTISi9hPt_YnkKRfrXkWVXNjVUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
مردم بی‌گناه ما هدف حملات بزدلانه‌ای قرار گرفتند که بر کشورمان تحمیل شد. ما با تمام توان از خود دفاع کردیم.
آمریکا و اسرائیل با پیشرفته‌ترین فناوری‌ها به ما حمله کردند. آن‌ها به ما ضربه زدند، اما ما سر تسلیم فرود نیاوردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72128" target="_blank">📅 17:53 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72127">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مسعود پزشکیان:
دیروز ترامپ ما را تروریست خواند؛ در حالی که ما خود قربانی تروریسم بوده‌ایم.
من از ایرانی می‌آیم که در آن، رهبر عالی‌قدر ما بدون هیچ‌گونه مبنای قانونی یا دلیلی ترور شد.
من از ایرانی می‌آیم که در آن، مدرسه‌ای بمباران شد. این کودکان را می‌بینید؟ این کودکان بر اثر بمباران با تسلیحاتی که توسط آمریکا و اسرائیل به کار گرفته شده بود، جان باختند.
آن‌ها بی‌گناه بودند و هیچ جرمی مرتکب نشده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72127" target="_blank">📅 17:50 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72126">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=CmEkHsoFgusMRsPXIsQE7X_FzA2RrJBUwurgzs1tFGm9NUoVWVyUQl00_58jcgHnTvV0KB4vFC1mVJbU3KvmifMRmxZGKG2f_HifwKTgIbvZaw70gH_MqNGbRTrAfnq_om0NElGvZ0xO6YucR6GoHnCIe3xi7pCywMJiUz48rnl4KlGQXB3sZJ9yG_3EzzQ1i5IpetNlFGscM2ztRHigOMBJxuJPGtT2MNKJwta80zvmGG7THO8KNs0ODp707kz0rNcpfx5bir8bfgp4M_U-ZawlsoWNm2wBLb2PGm5X0loy8fJse-Dnx7wDu7hQnbZhasf-1QlqnE4AKAhmQg2v7YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aca1a8c79.mp4?token=CmEkHsoFgusMRsPXIsQE7X_FzA2RrJBUwurgzs1tFGm9NUoVWVyUQl00_58jcgHnTvV0KB4vFC1mVJbU3KvmifMRmxZGKG2f_HifwKTgIbvZaw70gH_MqNGbRTrAfnq_om0NElGvZ0xO6YucR6GoHnCIe3xi7pCywMJiUz48rnl4KlGQXB3sZJ9yG_3EzzQ1i5IpetNlFGscM2ztRHigOMBJxuJPGtT2MNKJwta80zvmGG7THO8KNs0ODp707kz0rNcpfx5bir8bfgp4M_U-ZawlsoWNm2wBLb2PGm5X0loy8fJse-Dnx7wDu7hQnbZhasf-1QlqnE4AKAhmQg2v7YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت نمایندگی ایالات متحده هم‌زمان با سخنرانی رئیس‌جمهور ایران، پزشکیان، صحن مجمع عمومی سازمان ملل را ترک می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72126" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72125">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72125" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72125" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72124">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8DYaL3FggdBJYgm30E3nbGDYc1l5xAyO3pLvWwhdgUlOLz5FwTcI8mRAyQG1vXzeLq2F5lE-B-UXiui9i4O_IgwdszbXYmnRiKjsaJkTfnL3NFZzi3qMwrgKFW97c7dOTfPTx44skDcxZPU5R8a1h9uxH_NmhrTPZ5hZLyst-Oyy6gqZBG-4zWZPJAvrTRx4ABkBu2hN9xUNYeP7aSUqD_hox2UxoXKlxAFQ9oB_yyseQC0JWjoJv4HLTse_F6Ok44m2r9iZa2tlYg1w8tdupP65rsvGkCi1slYXoDSoPz-L1YCrMPxmlsj27aqjIwDuEX0HViJu4AHByShae1L2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72124" target="_blank">📅 17:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72123">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=jdFxIHn_hPNqaGrGCuwn1B4ZoVWvTpgJRjpGYWeiynr7u5E4anl6EKSDwj_mSVeyXkUzqFs6rI5PGDrqXJF569jHH1Hud9HRb4PYEeB3RpbdBGMWnRlq-1FI7U7cF0DzAbuvz9BO66a8G_wxcSeVGRrFYPkmpgtDdpvmHZ6saIOcXe6ZsSPgTxnWt-9ebE4wF3O-TZ60foLCB7vp3HhfKsFCVMRAEZPPB7J21EHNs361DEhn_YcuFXuXZ3WEOl8MgX2P09Dkr-U7mY9Rr0u8uwbPm--cffi6qa4RDtHOO5Y6voc-GrtZZ3gtDivSXMhaaLnB8kgff-07Xx4O7-2YZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4142dc5d8.mp4?token=jdFxIHn_hPNqaGrGCuwn1B4ZoVWvTpgJRjpGYWeiynr7u5E4anl6EKSDwj_mSVeyXkUzqFs6rI5PGDrqXJF569jHH1Hud9HRb4PYEeB3RpbdBGMWnRlq-1FI7U7cF0DzAbuvz9BO66a8G_wxcSeVGRrFYPkmpgtDdpvmHZ6saIOcXe6ZsSPgTxnWt-9ebE4wF3O-TZ60foLCB7vp3HhfKsFCVMRAEZPPB7J21EHNs361DEhn_YcuFXuXZ3WEOl8MgX2P09Dkr-U7mY9Rr0u8uwbPm--cffi6qa4RDtHOO5Y6voc-GrtZZ3gtDivSXMhaaLnB8kgff-07Xx4O7-2YZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قیمت کوکائین در تهران چند؟
پلیس مواد مخدر تهران بزرگ ، یک بار بزرگ کوکایین کلمبیایی را قبل از پخش در پایتخت ، کشف کرد .
این کوکایین ها بیش از ۵۵۰ میلیارد تومان ارزش گذاری شده است.
گویا داداشی ها سهم  مامورا رو ندادن اونا هم بار رو لو دادن
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72123" target="_blank">📅 17:34 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72122">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=dxa0wvHER6yweboIuQdF5ZZYQgvz2uiP_XitKf5ZSvP-OFJpp0JOtzv2M5-CCSBa59hlkuA_EecDWtimyB0IoNpEa4mBvAUFfz8cAPhhsqZNbjc7jKuNd9xQ5AfBnFruEWUIm7weCrJXs9wPwh6ZNIcPYaFznlq0w6tCNPtZ4UuFgMzgFYMyQn1RbBx3MViFDxSOhP3D82IDSttKOoP3sLAR035gVsKRWfTEVBz7rXGPdjXPNmAqay_fMEQHWgsgSXR2gEzSYCnJp-fTcUxiBERxpETehA72oxxl5m5UWDPe-U7dO5_rrxRypkpv2GcnF_RgynmmSHNpTrQgHh3jMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dadfb7a92.mp4?token=dxa0wvHER6yweboIuQdF5ZZYQgvz2uiP_XitKf5ZSvP-OFJpp0JOtzv2M5-CCSBa59hlkuA_EecDWtimyB0IoNpEa4mBvAUFfz8cAPhhsqZNbjc7jKuNd9xQ5AfBnFruEWUIm7weCrJXs9wPwh6ZNIcPYaFznlq0w6tCNPtZ4UuFgMzgFYMyQn1RbBx3MViFDxSOhP3D82IDSttKOoP3sLAR035gVsKRWfTEVBz7rXGPdjXPNmAqay_fMEQHWgsgSXR2gEzSYCnJp-fTcUxiBERxpETehA72oxxl5m5UWDPe-U7dO5_rrxRypkpv2GcnF_RgynmmSHNpTrQgHh3jMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه مادر توی کمد لباسای دخترش، کاستوم مخصوص سکس پیدا کرده، بعد دختره هم به این شکل مامانشو قانع کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72122" target="_blank">📅 17:01 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72121">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiF4KL4F82OllUzWTLud6w-PLfjLAT6geeDs85M4eu8PkSjSwS5RSrWskGFW55DxIigR7IureIjFuXPkH7TOFsUhGHO4GeLIL46CDKizZik7-Q9QwCtGXIRaRTVTZ_UjgZoZBFzF-rAyF88n78lBtVOhP60fY05ewWyitW4QMbazMwoBmvxMdQ8w7ZaPfS9JbKo-6jk8OBBttsjoqvk6DHfRMkNeSLyLhFITCu08gJ9t4QYVs47pmbaue4EarlUliFcE5Ea2goBJiEbXFEvQt2lXkKlS8jbz9qX-zEYRUakI95iCW4JsM1TAEPw_ywlrF6FBbWLNa2RrsK-de4orXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد که یک کشتی باری در تنگه هرمز هدف اصابت پرتابه‌ای ناشناس قرار گرفته است.
این کشتی دچار آتش‌سوزی شده و بر روی آب سرگردان است. خدمه کشتی تخلیه شده‌اند و گزارش‌هایی از دو مورد تلفات منتشر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72121" target="_blank">📅 16:34 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
