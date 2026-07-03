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
<img src="https://cdn4.telesco.pe/file/P7nTMMYZW1uopl_LxhZtKZgHZpDaQ6rLs8PMneULNQ5ZkNWAMBJyePT2jv6Vx8xuFN3xTdc98P-GWwnWwmCzS2CugbgpEVkt9CUztCa0AWA1SooBI96HMX2MwS4I3WxHzuHkAUeas98vWhLiyHEb5GQAk4PMNF4QHQTU62TEerC53U_9sJq3rD0CbGgbYdUQ0VjjeDs9r_5qMF-wLKnk1SxVl-TAC0zBdVToHklHNpmuZauCXT63mQa0f0uZjx4ipF90BOtzxgDQ_zW1boo2ZVPPbCSXMT9IIC6gq_srQWqmx_nsvhpW-w0yxTvKHv9-Okdbtp6ppLRfsGeqH7-nDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 09:52:45</div>
<hr>

<div class="tg-post" id="msg-80661">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hNMbGTQ7rgLr_OJoSMpgLoRa5j6WpbCslmjoXOSZe6-ife5MfyCFO2HUBLimg8-3YxwVPxL5zWQ999jmjfhgo7ed6RsWgpDV1EFi7L4qvPpd4y7TtkCcTroUZ29H-i11DCmXVKe3bGYejrJZYKQx5yKos1q1qMCfKPKD2-naYjOEcbg5S7qIVo2_UtFd21Yag53RxYaWhWm0RkukhOkfNzD_bhzMmykKQ-vJuHjde5-gnlBeodukVcJkvkxWkPUlBT1HQ5KcySxaDiDizp8XO4Ai2aTKKhmPF-Kaa9zFm4hpK3aj7YPlQWQJqPC2ASUEEdum4VyGu6azkpT9r0J7MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9ks2X7PJSCVBs83beIi2-KN1szOkACqOrZBxycibZshtU6BLmXWEImUVdb2vJQwq97Hlb4DbbGi3AS0eLvT5RjflntdBTBilqzu1-QLb1-8oGLxn_r-8ovMyu9wffwxApG3gVhKJmZDI4eFIB8hc1ePEVfw4M-bBek4RKA4MmqXZZAMH1WUngn5nxaz3XdRrk_HIInYQz5yuhYfH_CHajAkzH0OjB3baz1LUvhqx2KjJhlCxY3dhoMuXxa5OusBAEdAeY9evWFqBo_YIw9xUOZzQWGglIpCBAemvqqllPkqY6bWmQAIqoX3yv8F7-5n4Hx3_ZZJUQpMFRt8npoH-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d006a5066e.mp4?token=v1T4NyO9irq41nM1zcYNXyCRN7kI-7LtGBRMW_kBejnwUJqq735Fed1kGG5JGVA6QZgIhZMSJR7wCoosqQ9N3frehKE0io545JIZii5eb8NYC3mOA0pj11USD8DZzzcYIK3lQWpI_EkpWBduMBMDQ1QrwA9WkGRdK14kiIVNW3wXHqFyIktmE04rs3nEycv6wXcFNJEuwp_P8FJ2oYCih4tXR3MNnJ4m6gKaLenrysx-2kLziyoVtblAwYaDLMP1dDnEVILiDwe3FJAZeM4f_bFNOx94HQdMlWcSBVRlfjCvyg5ulmdWOt1Df2h9H3QguXnanlhnDwRxtjnsCYyDHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d006a5066e.mp4?token=v1T4NyO9irq41nM1zcYNXyCRN7kI-7LtGBRMW_kBejnwUJqq735Fed1kGG5JGVA6QZgIhZMSJR7wCoosqQ9N3frehKE0io545JIZii5eb8NYC3mOA0pj11USD8DZzzcYIK3lQWpI_EkpWBduMBMDQ1QrwA9WkGRdK14kiIVNW3wXHqFyIktmE04rs3nEycv6wXcFNJEuwp_P8FJ2oYCih4tXR3MNnJ4m6gKaLenrysx-2kLziyoVtblAwYaDLMP1dDnEVILiDwe3FJAZeM4f_bFNOx94HQdMlWcSBVRlfjCvyg5ulmdWOt1Df2h9H3QguXnanlhnDwRxtjnsCYyDHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لقاء وزير الخارجية الإيراني عراقجي برئيس إقليم كردستان العراق</div>
<div class="tg-footer">👁️ 822 · <a href="https://t.me/naya_foriraq/80661" target="_blank">📅 09:47 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZjfloHN0B9pgNQHQc-KiZJxMdJtFr22SAM5cIiMbjZHO3LZ1l9F6JtBcPQ1CMRz2bA6lzKLZtFAzy9chhQxFvNx2IDnyBgGZn0WRMQ7WDwGo-188WmEL68GfuA_z3t0RkS4TUJlLl6l2BbuopNV8Jo3wXiMe1GOh8ni6pAZUHR2iI3-VHBLN1jKiHNNSsdn1A6mdFoq1gEvXkHB4qvt1jBCQIjuwmSe1qUsHgV2PUfxgCivqlS_7agSAzeJ-Crrn3lg8_ri8IX5QXxwiZCKZeREgUavLlwOQnK4BxhwWtr3JJ9b0kTpr3P-oboGqCxwK3-OKSpQLxe5yDb7ASgMqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قائد المقاومة الأفغانية أحمد مسعود يودع جثمان القائد الشهيد</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/naya_foriraq/80660" target="_blank">📅 09:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإمام الشهيد السيد علي الخامنئي</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af5a33e00.mp4?token=GYCVkyXs2IpaB8MEM6jlAFE8cMVJibLMi02kSHELiURuTUhVQUWfbuiJLsTFhEH-rQF6mxiUwAoqZrUJqED1vyjVl1GPpK6nLGBbgOKeogVkr-r5VFJuaz8LTEqibglcjjK7Of3be0oLq4atMfRTPkv55IenkgGhWbVDf9w_V8aoA44wBWmZypqf5UGFUiGCrghkNRHpaKONgzAnI7hnjNXMtZSgkXQGOVan4RcdfhtHUY04pw0V5AiDH0phP7mM0yxx2aTSGQebWJWR5ONSbr9_a2ZswXX26pycFT1m6OAdIExjteqD_TxBQWxK0CF1Zbu9izkaJ6pcUNTxUZ5tGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af5a33e00.mp4?token=GYCVkyXs2IpaB8MEM6jlAFE8cMVJibLMi02kSHELiURuTUhVQUWfbuiJLsTFhEH-rQF6mxiUwAoqZrUJqED1vyjVl1GPpK6nLGBbgOKeogVkr-r5VFJuaz8LTEqibglcjjK7Of3be0oLq4atMfRTPkv55IenkgGhWbVDf9w_V8aoA44wBWmZypqf5UGFUiGCrghkNRHpaKONgzAnI7hnjNXMtZSgkXQGOVan4RcdfhtHUY04pw0V5AiDH0phP7mM0yxx2aTSGQebWJWR5ONSbr9_a2ZswXX26pycFT1m6OAdIExjteqD_TxBQWxK0CF1Zbu9izkaJ6pcUNTxUZ5tGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
|
وفد حركة المقاومة «كتائب حزب الله» العراقية يؤدي الاحترام للجثمان الطاهر لقائد الثورة الإسلامية الشهيد. | 3/07/2026
🏴
#قوموا_لله
#تشييع_إمام_المستضعفين
➕
t.me/Khamenei_arabi</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/naya_foriraq/80659" target="_blank">📅 09:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">رئيس الجمهورية العراقي يغادر إلى طهران الان</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/naya_foriraq/80658" target="_blank">📅 09:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d463bb3a6.mp4?token=lCNTQjqnUeHzlaIuX4Y5sUZZFioiGXPnZ0YsddvVYsz75eYQDANyOegPG6ub5AFyXlrMWQESUGr_InRcVN2AYa1_YpFFil-E9N04aCyUnN-05XuP1Ptsmzrd_maS9TyTOpD1KGiT7gGKaj0cPVBhni6wzq_r-OuH0Chp1Cm4VFRyTW6Z-D3jUB6ssgMDpd6dTzvjydgOAZ2vVyu4e_hv3ZfMqj-QoZ5wGfTs5qAyLAQaghsPFzMgfxUDgjfPx4wgYLjh20ErWxandpOG8r4iYIeRjyMMtR7ZB9biUlpJEdwXHK-PHGCL8UwnWpdKh2U5DKye-5cW-erGNBIO1dghGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d463bb3a6.mp4?token=lCNTQjqnUeHzlaIuX4Y5sUZZFioiGXPnZ0YsddvVYsz75eYQDANyOegPG6ub5AFyXlrMWQESUGr_InRcVN2AYa1_YpFFil-E9N04aCyUnN-05XuP1Ptsmzrd_maS9TyTOpD1KGiT7gGKaj0cPVBhni6wzq_r-OuH0Chp1Cm4VFRyTW6Z-D3jUB6ssgMDpd6dTzvjydgOAZ2vVyu4e_hv3ZfMqj-QoZ5wGfTs5qAyLAQaghsPFzMgfxUDgjfPx4wgYLjh20ErWxandpOG8r4iYIeRjyMMtR7ZB9biUlpJEdwXHK-PHGCL8UwnWpdKh2U5DKye-5cW-erGNBIO1dghGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حركة أمل اللبنانية تصل لتوديع النعش الطاهر</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/naya_foriraq/80657" target="_blank">📅 09:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77e9cb4668.mp4?token=gczQ-HbkVoaDx96OzlYBZ0LSc6q-EWSGFOdTHxfTAiSI13Hefwd2wiaAWLtj-02-vKUiwRYbnmE_2skoho4jvpsLr1TlvQ6yyqUatkkQ57roMgywEKIVV7b3cLVd6prrZQgzW8AK-B8OiskBPcW9pqFJ8DrhgEKPggfP_rjwLjz_Fbjhzm7rE1US1oLoI-zOX4h5IE66xA-RYShEI0OOOdqEARKwyKSQrKoX2iL6p3SDSd8iMuyCeJJSLYAh-WxbN_1wt61pRFED7wwW8MsV9FHwDZNYiHvqbIYuSo_0KhT8kDRzznpsO6Wt0JqXh-c3bir3P978ixSriA4-9OgNqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77e9cb4668.mp4?token=gczQ-HbkVoaDx96OzlYBZ0LSc6q-EWSGFOdTHxfTAiSI13Hefwd2wiaAWLtj-02-vKUiwRYbnmE_2skoho4jvpsLr1TlvQ6yyqUatkkQ57roMgywEKIVV7b3cLVd6prrZQgzW8AK-B8OiskBPcW9pqFJ8DrhgEKPggfP_rjwLjz_Fbjhzm7rE1US1oLoI-zOX4h5IE66xA-RYShEI0OOOdqEARKwyKSQrKoX2iL6p3SDSd8iMuyCeJJSLYAh-WxbN_1wt61pRFED7wwW8MsV9FHwDZNYiHvqbIYuSo_0KhT8kDRzznpsO6Wt0JqXh-c3bir3P978ixSriA4-9OgNqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفود العراقية ضخمة جدا ومستمرة بالتوافد</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/naya_foriraq/80656" target="_blank">📅 09:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">وفود كبيرة جداً من المقاومة العراقية منهم السيد صلاح يصلون لتوديع الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/naya_foriraq/80655" target="_blank">📅 09:27 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/253b6da29e.mp4?token=XRNOCqpjJd3D-fFQPZv_9JMUnIixllS5phI0pWsNhCAkmdv7f6NLLh_MdByYIhzuqlahbeEN6Mi2IiUFNXotFX4p_q5u25I6s8uDPKTf9Zl8RPDVxGGyKxdE8efRX5CIb9sbPHoaTfSMlsTZ6WljCAPpHZ6ijJGTrMH4ipqUn2GkvHLntJFPqaJGt7RGW4mN6U-xZSel_l-fEVkS6R7KNK0T3hPNL96TKT9hNiMplPZICpM971kCcMPWkEw4iJcDybSIxuYUnA_DO2luTdbI8U2wh8Jr000BnM6Zk2CZlk26-5a7XZMhrQbA44rD_3RcnX8EhuxD0V2dEsdMH1Uj3Y2ItbUjf0cPYWT8JH8v9VagBeYciY5VuT4hyDmS0FrSuH8G1JqX76t2C_fGMHJvKjq2jsKU-LwGhU8PvX5WrUlDVSPWsYCSJ857bWtoPcjuijmK5H8x5DUnZv6aPed9oJ7yoKKtubjP9qoRjIvk0X54OpIMWq2INEwi0rUU77uGd7gKDczV_AYDGUCJTGQGnFoI8JAsAyIZdcN2u2wERHa2cNuspAd76pTGxx85t2DfQaq4I-DX_XDQTzi-2fLqEZytBebqQUdSYAiSqzk8E4l6U0Rz2k4qecHxlkFIYyvKEjhnmxYck_kXO8OONJXJ7TENJgmkqHv0C8tFPD7wqF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/253b6da29e.mp4?token=XRNOCqpjJd3D-fFQPZv_9JMUnIixllS5phI0pWsNhCAkmdv7f6NLLh_MdByYIhzuqlahbeEN6Mi2IiUFNXotFX4p_q5u25I6s8uDPKTf9Zl8RPDVxGGyKxdE8efRX5CIb9sbPHoaTfSMlsTZ6WljCAPpHZ6ijJGTrMH4ipqUn2GkvHLntJFPqaJGt7RGW4mN6U-xZSel_l-fEVkS6R7KNK0T3hPNL96TKT9hNiMplPZICpM971kCcMPWkEw4iJcDybSIxuYUnA_DO2luTdbI8U2wh8Jr000BnM6Zk2CZlk26-5a7XZMhrQbA44rD_3RcnX8EhuxD0V2dEsdMH1Uj3Y2ItbUjf0cPYWT8JH8v9VagBeYciY5VuT4hyDmS0FrSuH8G1JqX76t2C_fGMHJvKjq2jsKU-LwGhU8PvX5WrUlDVSPWsYCSJ857bWtoPcjuijmK5H8x5DUnZv6aPed9oJ7yoKKtubjP9qoRjIvk0X54OpIMWq2INEwi0rUU77uGd7gKDczV_AYDGUCJTGQGnFoI8JAsAyIZdcN2u2wERHa2cNuspAd76pTGxx85t2DfQaq4I-DX_XDQTzi-2fLqEZytBebqQUdSYAiSqzk8E4l6U0Rz2k4qecHxlkFIYyvKEjhnmxYck_kXO8OONJXJ7TENJgmkqHv0C8tFPD7wqF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود كبيرة جداً من المقاومة العراقية منهم السيد صلاح يصلون لتوديع الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/naya_foriraq/80654" target="_blank">📅 09:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80653">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eea18a41.mp4?token=S8TLP8hlmQaLom4xANmTxgKjEFhH7b-8ExlBafxm3HfrnnEKHG-_Ghz0koYTxqH1yIO47JNE03WvZTsqMoEa5Um3GMTRACW0jZGJmejhLfIIj_pBE0RyuCqDmBFTwM6VWBZ875Domu8nChkcx954hVWxs6I8RUpTM17KR17vvASGYVpfwtbR9WLAl-fhohMjq7L8hj0aNFV3lFmSyGp2gpXNkxA6ryAqcKVDgO8HjsH5cZanHrBdpvVPwwEIyPKju7T3aBlSWpcbvqlwB_QXdeIFXxnhzmRh2pvEtfJYxdeu7u9eQwVneSa3RuRMaulixpMut8oQc65HEd_6YaPDyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eea18a41.mp4?token=S8TLP8hlmQaLom4xANmTxgKjEFhH7b-8ExlBafxm3HfrnnEKHG-_Ghz0koYTxqH1yIO47JNE03WvZTsqMoEa5Um3GMTRACW0jZGJmejhLfIIj_pBE0RyuCqDmBFTwM6VWBZ875Domu8nChkcx954hVWxs6I8RUpTM17KR17vvASGYVpfwtbR9WLAl-fhohMjq7L8hj0aNFV3lFmSyGp2gpXNkxA6ryAqcKVDgO8HjsH5cZanHrBdpvVPwwEIyPKju7T3aBlSWpcbvqlwB_QXdeIFXxnhzmRh2pvEtfJYxdeu7u9eQwVneSa3RuRMaulixpMut8oQc65HEd_6YaPDyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يستمر الوفد العراقي الأكبر من قيادات الحشد الشعبي المقدس بالتوافد ؛</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/naya_foriraq/80653" target="_blank">📅 09:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80652">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c2840f4a.mp4?token=aPNiSD1egQ8svhbxygfVqVNtuda79G0Dyd1rTFDtPO2upjVQJyjnkce-_9rMnQ8aa2QdvX0FEpzl7MJNJWEV5A40o8pSkPPOjYeD26yKtrftcvisXv6HVJUPjoTtBSfAky1FGiPGawB8_232vS19mvAZ30JQmMnS_eplRuEcat0AcMMtZNiyX55vhuJxoEYMLxTIQUaMkM42jmtdWbG7wsdbB8ptUxKGMs0rPID02vKmi0T2YKAJ_iU8Zqb-f1n0-JDSkxRuhsqCpVSlOukuT9iW-nS1ItMhVdAr4wqvR89EJT-lIOKW14711IPeD23HpDsF004tytxyJQV8XJ04aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c2840f4a.mp4?token=aPNiSD1egQ8svhbxygfVqVNtuda79G0Dyd1rTFDtPO2upjVQJyjnkce-_9rMnQ8aa2QdvX0FEpzl7MJNJWEV5A40o8pSkPPOjYeD26yKtrftcvisXv6HVJUPjoTtBSfAky1FGiPGawB8_232vS19mvAZ30JQmMnS_eplRuEcat0AcMMtZNiyX55vhuJxoEYMLxTIQUaMkM42jmtdWbG7wsdbB8ptUxKGMs0rPID02vKmi0T2YKAJ_iU8Zqb-f1n0-JDSkxRuhsqCpVSlOukuT9iW-nS1ItMhVdAr4wqvR89EJT-lIOKW14711IPeD23HpDsF004tytxyJQV8XJ04aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الوفد العراقي هو الأكبر</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/naya_foriraq/80652" target="_blank">📅 09:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80651">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdbIJSWp5WogQ55REvVn6kpbTSmS2amUFIUpIlu_y4Af8if3SnLxWNa20yBMvie6XNNA8gsXO8xUSYCiBbVIWS_VeidEwSr2_iWLQvpfaIgv75D49TGqOE9iXu2bwu4P3f6pCVuLcEYecA-U3ge1eVukCROlhnbNacpf3Mq-hQJRd3MpHM0ddzUD_e5HiOT0hv6SPTZtcRQ45B7GlWGEK-0ixymilr0-fA3JXumAA0TL7Yl5KLToKHxro_CW4kHffNmJd9MXaS-aXiSVPDDDr6b_O413na8g7ZZouoi3RAkRCIhPeQrG3jZHWW0eELdNU5crDjr9fJOByqh1OEENAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاليباف يستقبل رئيس برلمان بلا روسيا اثناء مشاركتهم بالعزاء</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/naya_foriraq/80651" target="_blank">📅 09:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80650">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf31476a75.mp4?token=tbWhE1aNki0-yB8lMCsx87aZ6zrH9h9rs0aq0HhfxJPBrdFQNCTZjeLCGETj4UT96nzRNrdK2Zk-EJQ-RBIO308qi8AvMHr4mOK6yeXJkD4fq5sM4rXpgLCF8cO8Vhf2OqPXSFGtSq3t4CCPWmD979nx-0WrJ35d-R_z8NlnvKCE09GwtuON-gvNHQsOkxZryiDeo45_xaPZU0ij8eIWrcanj4IhncjuUoAhO3jraRXODE2wn7sV2WaQpJFERoiBoUmYaxhMreRWo29Btnpt4l7GiDZ1tDZNm8h06fct-xD_YrfGTfeNaln9nZPkp8MVwsGhC1RCcdYm-e-akDxN_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf31476a75.mp4?token=tbWhE1aNki0-yB8lMCsx87aZ6zrH9h9rs0aq0HhfxJPBrdFQNCTZjeLCGETj4UT96nzRNrdK2Zk-EJQ-RBIO308qi8AvMHr4mOK6yeXJkD4fq5sM4rXpgLCF8cO8Vhf2OqPXSFGtSq3t4CCPWmD979nx-0WrJ35d-R_z8NlnvKCE09GwtuON-gvNHQsOkxZryiDeo45_xaPZU0ij8eIWrcanj4IhncjuUoAhO3jraRXODE2wn7sV2WaQpJFERoiBoUmYaxhMreRWo29Btnpt4l7GiDZ1tDZNm8h06fct-xD_YrfGTfeNaln9nZPkp8MVwsGhC1RCcdYm-e-akDxN_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود أخرى من الحشد الشعبي العراقي تودع الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/naya_foriraq/80650" target="_blank">📅 09:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80649">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65354c2ec7.mp4?token=dBXiJTw7kPI5bzTW1cOTnOKEcu9h3sTDceWpdbW1iXbLG5MZIATLK1ZIDIHoQJjtTp9-O56TSII-FQQmzVJscuH5b1P4kFH6Csa72hvQM1HT75HBBCLU849iesL9XL9DpZbEA9n7yFDPmteTPfKu4s6NntBgLNrmitKBN5kW_DQIb5K-G1vavYxyIAvcdL-biXCfcQJhCk7ddcvajHTFnR1Un4V5s6YzSejySwGb4EjMD0fgkeqbOcPiGXFinX30bqzdXBcYZQmc9TWyQ15Dfv_1M28VugqYudFBfYgfCToF9ey-uoN7VxzHspnZ7vVKYMy7-qGp4T4burvgW9yD_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65354c2ec7.mp4?token=dBXiJTw7kPI5bzTW1cOTnOKEcu9h3sTDceWpdbW1iXbLG5MZIATLK1ZIDIHoQJjtTp9-O56TSII-FQQmzVJscuH5b1P4kFH6Csa72hvQM1HT75HBBCLU849iesL9XL9DpZbEA9n7yFDPmteTPfKu4s6NntBgLNrmitKBN5kW_DQIb5K-G1vavYxyIAvcdL-biXCfcQJhCk7ddcvajHTFnR1Un4V5s6YzSejySwGb4EjMD0fgkeqbOcPiGXFinX30bqzdXBcYZQmc9TWyQ15Dfv_1M28VugqYudFBfYgfCToF9ey-uoN7VxzHspnZ7vVKYMy7-qGp4T4burvgW9yD_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة وصول قادة الحشد الشعبي المقدس العراقي إلى توديع النعش الطاهر للسيد الشهيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/naya_foriraq/80649" target="_blank">📅 09:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80648">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حشدنا المقدس</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/naya_foriraq/80648" target="_blank">📅 09:08 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80647">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xxn2JCs37qJezjgtNA2FWYjDVQovF_dycsRR7339fhbcxKH07FAtGoCxfQgnPKoGKtSUqkzat--qsbQ_uYhVQwe-kGW9Bzkf8Z-qmL1HfuIiK5MyPtDpc0Kre_iIKFB9QQHfJbq3FOjUcMWQIzeqR4CInFvBDDsm3oWJ0mpjoivmrqiXQz-aHMeig3FtgoSnrokJIyDjurWjEso2eZKUtkCRr2DBKH0vg1XTkFq5jgjiPjn_oDkkv-S34cvbskq7wbfMso-t-HBr1P4-LUKlnisXeJiYhXP2NWJ5zpuBj8Pt8WZ-WGciOT3ceu48xHUGE16fqtp1D35kMFkUGvy-Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حشدنا المقدس</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/naya_foriraq/80647" target="_blank">📅 09:06 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80646">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efa0982f3.mp4?token=M8JLDOd3EX-MuALEX7Nf_8Ir9_VYzzwMfr-0o7rHqz3fF4sow_DcMvg-aNxHkbDh1kJMbRTQikErpDnfL0Gj0ot-r4pG7VJSRrVjtHtAVR57AKUsUNN4pmvudFWlHdUrBDKMk2ZknTuuC88ooQv87N1uPc4FcFklOfv7ihhxooy9oaZV_ustJI_NNgGGSN1tw1XmP1CW-FRkSiRMpxQVwNbrBCSlWQCOh1bqEpk2S7tHrNTI8k5ef5A4BnP4kzuu90sC_ADxnnbS9fEXjKkgokq_6wY1oIrS4EXh8o4pqPQ3xWbhv6HmK44cld7W4rsKcPXE9OVaW2lvYw99U4KxpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efa0982f3.mp4?token=M8JLDOd3EX-MuALEX7Nf_8Ir9_VYzzwMfr-0o7rHqz3fF4sow_DcMvg-aNxHkbDh1kJMbRTQikErpDnfL0Gj0ot-r4pG7VJSRrVjtHtAVR57AKUsUNN4pmvudFWlHdUrBDKMk2ZknTuuC88ooQv87N1uPc4FcFklOfv7ihhxooy9oaZV_ustJI_NNgGGSN1tw1XmP1CW-FRkSiRMpxQVwNbrBCSlWQCOh1bqEpk2S7tHrNTI8k5ef5A4BnP4kzuu90sC_ADxnnbS9fEXjKkgokq_6wY1oIrS4EXh8o4pqPQ3xWbhv6HmK44cld7W4rsKcPXE9OVaW2lvYw99U4KxpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود المقاومة في العالم أجمع تصل لتوديع جثمان السيد الشهيد الطاهر.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/naya_foriraq/80646" target="_blank">📅 09:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80645">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa5969afaf.mp4?token=rA0aWekh46NztkzVdDmsOwBP0YZ1y0Vd2bToKCr1hBgPHfaqr64fTqJA7RDe2GUe-RFVIMg4V7z7kZaIOTI-sn23PDjtba0z6L3jGY2g5ML1HNSf85rVbvXaGJBGzmeASSiy6lj_XNvDbugHWGzYeargPDt5j9pMODcR1HOX29dGPR0ffRYUOuJUZlCAM_MYO1Z0J6lHVcxgt_aN0qOpZf6L9Rr8zkSboLTxJMYmu6fv721vlWHXi_Ef4dN9xXW3eXMrVMgOQCcVA3i5KWx6a1h-tB5jIU1BB-6FjO_TQ20KJwkaGqmzCEaDXZ_1WNWrMK8LjWRZCbFHNuzoZO6KQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa5969afaf.mp4?token=rA0aWekh46NztkzVdDmsOwBP0YZ1y0Vd2bToKCr1hBgPHfaqr64fTqJA7RDe2GUe-RFVIMg4V7z7kZaIOTI-sn23PDjtba0z6L3jGY2g5ML1HNSf85rVbvXaGJBGzmeASSiy6lj_XNvDbugHWGzYeargPDt5j9pMODcR1HOX29dGPR0ffRYUOuJUZlCAM_MYO1Z0J6lHVcxgt_aN0qOpZf6L9Rr8zkSboLTxJMYmu6fv721vlWHXi_Ef4dN9xXW3eXMrVMgOQCcVA3i5KWx6a1h-tB5jIU1BB-6FjO_TQ20KJwkaGqmzCEaDXZ_1WNWrMK8LjWRZCbFHNuzoZO6KQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفد من حركة النجباء العراقية في حضرة الشهيد السيد علي الخامنئي لتوديعة.</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/naya_foriraq/80645" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80644">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">أكرم الكعبي الشجاع</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/naya_foriraq/80644" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80643">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88c60c851e.mp4?token=hYo9bhS0RslY3UhNu5TJjorPbzSvS6mfepVZZyGXeHxGzkJgGSqY0M8pmALfKQewUim5ZCEguBhiG3HsEj03iq-8H2gsCgDA17q1YPxmamqxuj_egkA5cmC0usHzzD_SzmJKCYA0txzLaNdYap8i4e1SYkivz_F9_m3MoauWYpK0LZd22PD_DxqpNdEBQZehPUdX2tLVp9FF9R22dURoXSEvy4QFYuQtEajgt_DZks4BG6_l78nkxNehxRFRvb0KWM1itp_xaiFy5900mwcJdDM4PSuuhxNn6izMc1y1FtTdQK2nVn8gqbGIJopSolZ7MVWk_XAq-ptUgOoKiBHMGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88c60c851e.mp4?token=hYo9bhS0RslY3UhNu5TJjorPbzSvS6mfepVZZyGXeHxGzkJgGSqY0M8pmALfKQewUim5ZCEguBhiG3HsEj03iq-8H2gsCgDA17q1YPxmamqxuj_egkA5cmC0usHzzD_SzmJKCYA0txzLaNdYap8i4e1SYkivz_F9_m3MoauWYpK0LZd22PD_DxqpNdEBQZehPUdX2tLVp9FF9R22dURoXSEvy4QFYuQtEajgt_DZks4BG6_l78nkxNehxRFRvb0KWM1itp_xaiFy5900mwcJdDM4PSuuhxNn6izMc1y1FtTdQK2nVn8gqbGIJopSolZ7MVWk_XAq-ptUgOoKiBHMGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شخصيات بارزة من المقاومة العراقية تصل لتوديع نعش القائد الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/naya_foriraq/80643" target="_blank">📅 08:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80642">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51ea1b8acb.mp4?token=ZoOimjnaRwusswK57aPsxp9ahzP5cWtHdcSrIQ_31AEXu3xrqDtQyQbwgafaA0P7XBUdK0qaI8H4-jsyJHuLGEXclfFvnrri9nyE9UxZQ0iDH6AytqF3xSOSCwAMniPzUwPXOh69gxdhiDcLi697JEd8UO6vNeo3puReZQLLwLz2BnbWNNJvsj7aq438toLEQ97nF7ED-gaTCpVmVIJ6RDOy9iVq6SsXnh32PLNA-xp59ehb4t6Ioi9zhGvtPpf9_8-0RLqI6xacp3qSSMi3bzPu1glISDojwfjb3WszZ8OMkw_tqMeHz4FGVlqYKdo83oLiiTmVniY91UbP6ljCWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51ea1b8acb.mp4?token=ZoOimjnaRwusswK57aPsxp9ahzP5cWtHdcSrIQ_31AEXu3xrqDtQyQbwgafaA0P7XBUdK0qaI8H4-jsyJHuLGEXclfFvnrri9nyE9UxZQ0iDH6AytqF3xSOSCwAMniPzUwPXOh69gxdhiDcLi697JEd8UO6vNeo3puReZQLLwLz2BnbWNNJvsj7aq438toLEQ97nF7ED-gaTCpVmVIJ6RDOy9iVq6SsXnh32PLNA-xp59ehb4t6Ioi9zhGvtPpf9_8-0RLqI6xacp3qSSMi3bzPu1glISDojwfjb3WszZ8OMkw_tqMeHz4FGVlqYKdo83oLiiTmVniY91UbP6ljCWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئيس إقليم كردستان العراق يصل إلى إيران لحضور مراسم تشييع الشهيد السيد علي الخامنئي</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/naya_foriraq/80642" target="_blank">📅 08:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80641">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔻
المتحدث باسم وزارة الخارجية الإيرانية:
▫️
يشارك في هذه المراسم ما يقارب مئة دولة، إما بوفود رسمية أو شخصيات عامة وجماعات شعبية. ولدينا وفود رفيعة المستوى من الدول المجاورة.
▫️
يحضر المراسم ثمانية رؤساء دول على الأقل، أي رؤساء أو رؤساء وزراء، بالإضافة إلى رؤساء برلمانات من اثنتي عشرة دولة. كما يحضرها وزراء خارجية ووزراء آخرون وممثلون خاصون من عدد كبير من الدول.
▫️
تشارك في هذه المراسم جماعات وشخصيات شعبية من نحو مئة دولة.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/naya_foriraq/80641" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80640">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tISa-8rtq32nqnLq8mQQrNIzaZjlzOt50ava41UMZrBAC9Q8t4Armq6QkLJX04P56h4laU-VsPFZ0lFB1VJnkwOiNxvs_avVtAS2jNpl2KI-8tc8lxzyKcVGjAwLMg8kG9V20GVgEDiWsh-7Uc8hTXPIKgdGfgPqfuaEthRrgf86jXhtup5mz4DUSPfy02oVatXa87cN8GpnwuRPYVKSUew2IJWdz1cgoA-kIAQC-BOq_RCD3VzH6uu7Z4CG7ItgL26LRb8kWzplkIASh6BA_l5afZizCanCITchzYIzmhQvnJW8O7AXJx7KqM5Z0jIMLxRz3YgLT1yxalhuu63Ibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاعلام العبري : ودّع قائد الحرس الثوري، وحيدي، جثمان (آية الله الشهيد السيد علي الحسيني) الخامنئي، القائد الأعلى الراحل، قبل مراسم التشييع.</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/naya_foriraq/80640" target="_blank">📅 08:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80639">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd6d86c458.mp4?token=ZfRvf5IRJ-vqUkS2-XVeuFcWkyx8kwe5RKO1TaGFisQtW2HobhF-DN7OmToVJog_zCd0ezK9LiY2hqnhqm7pVnoRumhnomDkYUyKSkN8g8WKDSDpwRubtkpO_aslNEpcMqMB1yz3bBKXcBNLiM1_isAFobBIBS9rQ__TMHgExGPeL_lfia94ECLpzCxv221bJ6FJC5Mx8AZijotaaGqrIG2eLrD9HxCuL1LRu6wx6t3EBlkgNmlXwezDLx_zY1fGVkidhkJ7a1ZKuWzyoESTKt6WfC1hpsVHpfydkg-BEAFF8wd5w6m70sBByOAqKl-BnbAZ2Y_J1J62tzALFOELwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd6d86c458.mp4?token=ZfRvf5IRJ-vqUkS2-XVeuFcWkyx8kwe5RKO1TaGFisQtW2HobhF-DN7OmToVJog_zCd0ezK9LiY2hqnhqm7pVnoRumhnomDkYUyKSkN8g8WKDSDpwRubtkpO_aslNEpcMqMB1yz3bBKXcBNLiM1_isAFobBIBS9rQ__TMHgExGPeL_lfia94ECLpzCxv221bJ6FJC5Mx8AZijotaaGqrIG2eLrD9HxCuL1LRu6wx6t3EBlkgNmlXwezDLx_zY1fGVkidhkJ7a1ZKuWzyoESTKt6WfC1hpsVHpfydkg-BEAFF8wd5w6m70sBByOAqKl-BnbAZ2Y_J1J62tzALFOELwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وفود من روسيا والصين تتقدم بتعازيها إلى قائد الثورة الإيرانية في وفاة الشهيد
#قوموا_لله</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/naya_foriraq/80639" target="_blank">📅 08:22 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80638">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الآن | وصول وفدٍ قيادي وسياسي وبرلماني و قادة الحشد الشعبي وفصائل المقاومة، إلى العاصمة طهران للمشاركة في مراسم العزاء وتوديع الشهيد الإمام السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/naya_foriraq/80638" target="_blank">📅 07:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80637">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvP0oJM21gdfkq9h0-V70Qln98pvxWoAvqmT5PMEx4u6fikvkLFhEmmcNwGV2cCAtLTnN9nKL1jDVA31RqzKkXemXAp3rPG3eKPBsGD9gldwCBtK3ecqsSu1rZtmlvlqL7mjA_wK8nknamKpnLkkc8kZF2hbHPDbRkFjZiXiA1irM50SBerFtNqlFHjesQ6Sd-phoI9O9KtYrfjg5iEkTrvPIUseSSudWkK28zXo_HdC3WIHnw3hps5kyOMTSdJDttW2TybTeJqSoJtrHgxCjQfGqC8BC1pRPPTZs5fEP1U8utpjlNy_bzR-U-DVj_EUk9G8tX6xYkcO7Mm0fiEqVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحاج قاسم جاء لزيارتكم...</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80637" target="_blank">📅 02:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80636">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔻
قوه تداهم منزل وكيل النفط علي معارج في ميسان.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80636" target="_blank">📅 02:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80635">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔻
قوه تداهم منزل وكيل النفط علي معارج في ميسان.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80635" target="_blank">📅 02:21 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80634">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7784288888.mp4?token=TdNVzSqKSoPMGAxwcP0hU6NqVTdLKH_xLvl857ILzCh_8nseLGK_puhb4LYy_zQFNA6bKaqpDTXmxIkCvGv1AK-Oat6zwA3PPS1GoIkcf1YJLK5vc-iweSQXPc20W2Tay2q6-ls5qB63vaUd80ili2m-VIUp_MMUEQFiRC2AIG2bD3_vel9LzEN5nEa_NA5-1Tnw-bFvFo4IED7d4hKe14_-ZP4ixk3TRIgTYWeeYpCi4NN_fl7Bbg4KktaS7HL8MvOKqqSvTwpDDqGjE831QRkE3PHeiR4KfNSwmFXshmwUhLUrHJwqNHrIadD1z5PV5ZQNZ5wD7HlHpJZ1i1jh6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7784288888.mp4?token=TdNVzSqKSoPMGAxwcP0hU6NqVTdLKH_xLvl857ILzCh_8nseLGK_puhb4LYy_zQFNA6bKaqpDTXmxIkCvGv1AK-Oat6zwA3PPS1GoIkcf1YJLK5vc-iweSQXPc20W2Tay2q6-ls5qB63vaUd80ili2m-VIUp_MMUEQFiRC2AIG2bD3_vel9LzEN5nEa_NA5-1Tnw-bFvFo4IED7d4hKe14_-ZP4ixk3TRIgTYWeeYpCi4NN_fl7Bbg4KktaS7HL8MvOKqqSvTwpDDqGjE831QRkE3PHeiR4KfNSwmFXshmwUhLUrHJwqNHrIadD1z5PV5ZQNZ5wD7HlHpJZ1i1jh6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحاج قاسم جاء لزيارتكم...</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80634" target="_blank">📅 02:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80632">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ONmyQfuqH6OWgAB1QGaMG1-rHQV2T811z8wTLehLOeogSMflD0vKMA0SCWU994Fzio22kgc_BlrhejqyocdiBYxvabd8CGyFegFb9GGn3SGSRH6Cr6_l4B4Ngfiu6DJHA3WaF2Dhovu_knYgFCtql4xlJqAQ8Rlwq13TXqO0lN9WgOHZ3ISpko3MDfCPV5FHCFtQxFhYfuPWRh_xu3kt4ZFs2pdO2tGGRUg2I3HNVYpCxiRNUtA2zhUJ_kRsIDdxuVkp15ZoRpPP6ci8Plw9R7Ew0C0NIvB4MJVxDTgVfEoKE2jU10CI-A1nlhMbmvw6F0Do-2e1Td8ydvGqrImw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UNiIf_oXaDgrF4Tvz1JwgYup2VHV95MOA2F97k19zixyL9vY8xt6SJYHTE81lMQA5w1wLjMCAcmpK1nUx2UEBfAWlj49Mrh5XBZxfH9NApizfobjkqGtxYpG9eR7mfBt9_zftJtgWrFG-mAaJEf42B0mcEIdnSaUlDmBuO1zjrKkF4_RdvLuzLo12AbDCRil1MfWHI9OV1dbm94xoO5vyJjkosAZ8xuor8zWcefBB53EP4BH0OPdXs6d3y1Y7pjgN1SlwLPAdBGhRjENMH07s0dsVDIxNbzxUQyyRslId7DdC_jSVB_rw_4di3jyRMeY1BulOnVcU95zoJWs2VUWuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
غارتين من مسيره اسرائيلية استهدفت المنطقة الواقعة بين بلدتي صديقين وجبال البطم جنوبي لبنان.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80632" target="_blank">📅 01:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80631">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔻
ترمب:
لا أبحث عن تغيير النظام في إيران بل منعه من امتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80631" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80630">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbhVVk9ITk6yjRWpRcQJc6YGThLr_ysQLJ2Pn_AhavW5HGXBoN5RgnwxAcr8-LaLgGinEjSF-W9KOmRq7ymcjlVjrsB-9YqWH9lx04zO8DNKs97KMBrwQi370-kK5FpBgt8szsUIpidFp_p75cEmJ2y2FMiE6lvuhNg6dznmhF40i4mv28xcgYEBQnnQdtFuOQkzMa_UyyzHAHgf3JhuaodyAok7KlO81s-7cTiI7wxnyqcZzAT2RIyR-rGYlf6sDgnWp6ymh-mC0j3nehW3_whYPk_VYWIhaRuxS85-TgTaIuWQgIasti9r0THnXV9LjqoevgPNI3fUGZLkNkUAug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
‏
هيئة الاعلام والاتصالات العراقية
تقرر فرض غرامة مالية تبلغ 5 مليون دينار على مقدمي البرامج الرياضية في العراق (حيدر زكي - عمر رياض - علي نوري) وتقديم اعتذار رسمي عن مخالفاتهم وحذفها</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80630" target="_blank">📅 00:14 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80626">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Omwo6zW1C-Ij6522n_sdPKm-nr4giKy0RfMlr0GiGWVZ8IUJzqZGt0b7KbiK9UuvFuQ0AdZ4tqlKN-tZMoJlyl89wL-eGKMwousQh5DoXAR2HQIewqAKEKP2LdkAk7UK5piiLFTG5rOONhbGrHpI6szSfM65Kdwf04qgNf2gb2H55gOBPfP6hAHwtiKnQZUoagO03Y_eslnr7mPrfxSbtzyou0udIsCWpGapRmZpx76hVVpbYkVl4sUMNFqYDkuMASung1eMnFy5JY5v6KhuMOErrdU33JGDGGwxgAADqb1x6SrdUB_9JNhN3oAnxb-ofhbu6m1NAQ3jFoXtUloJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AAL7D4uscQedsLANNhlML0qyh6UBvCWSabJoZuOEV_errhUemxSp8M3RXK024XpPc3xouNFYKOnBmxYpPyjT3YzGidCxYipBSxZai8lHcapm-p30nRVX0mYI9tyFilUMS75VwSjrpbTBR-O_j27X2Lr0bulPDE0JPVvhMiurLT0n7oVx224pMHY6rnCsZ1jbmZvEih1vnMA21VWbHeD-BSAK5rxYizZoiZ0BCToD1NNQa5diED2TUF-i5bH1M1UL783Cu9R91khi-R3M5L_hZEm6G8VsMWSft44pZ-NAhNF5e-R8jgqqaKydQjXIkb5EakL20vgMD6HHIn0mvCfOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k0CNJTtdFO1x6fYsaV5lQvdwheMiS4hlI27rz_0AG_pvjl67s-KY7XvskqJ2QPPCfn-XHsKJU1OXsuYTDlR7lU66tKPyOWZUGamDtC_BVDo6HMLKcADJDOyvWLPCizBeHnLaxO4jPGH4fjCYAmZab6ovolMrN1IzIqscYyNiWgZJUT2r3mv8d4b9TUszxNFRGUmyiiMb0nEXNKvgJtjvOn0JguualFori7TuPUYloxWyPTuNbj6pnFA1jkWlVVzf15xo3I_A-QILEAXBhJptp2EXrt-EPFuJeho8kP6mRkeOfKm7KSebvCiuOXapryEkoT_wnB1Y4Rm1BH43TjacBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icWZgEVr4mobws-r4Z0gi1BOop46xjRoR59stbiFzgnwkocdsRfUsgUFOwHp4pdvr9S99WQjw3eBZyGe5kNn2Z9vNCdsVqEAJc7Au2OzkDZdDnMz1paCqci3P7Tgs8CRSAJgzZTC1Sc92FN44H-xyImNL1W7CvvPaWw0K0MifLEGVGihIUItWSirfS--gljAN9ZTQJ8xTqFMHw34zwdhY2ygFwIEcIvHd0jJdDLV2y7PtfToqtjYtEMfxjgHpd9wtyyu2mMPlI_vH2A2ycxIvVgIrMmQHqHnzWnvZT-N_IPqZg1ReaRLv8CNyfmxCmsut8eKsL-00ObIzpvLajQ7GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
لحظة دخول جثمان القائد الشهيد للثورة الإسلامية الإمام الشهيد السيد علي الخامنئي (قدس الله نفسه الزكيّة) إلى مراسم الوداع بجوار حسينيّة الإمام الخميني (قده)</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80626" target="_blank">📅 23:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80625">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3396ef5ba6.mp4?token=MIrl7aZELY3tRE1R-i1AwdKiDyjPgq--pFIHMgUBNXxgAt5hakkZT9-8eG68-2lA8HeztipT_glTroksKjczEGolkh4d2UHseNe2YdP8Gt_wRcFkFZ0EU2ImkR0uu0Iem31ARgV6087LoYC8OkOT5nd0L42hIyPo7oefC9U6F-kLvs57EjlpHmOWP4XuJPg3dYcGCx1iLSMdiFUSu93tRyEbXyEun05fBG1y09Qun8L8SnYSpmoMfUqd2nTvvvt6ppjfxcVqKyTdigYTB2tPAxGLfTzyoXPOkGuhO7TwoEVeOBypk15W0CoXCwJI55sCqlOeZ3KFzsnjKrMzSDRJZLCiv29F8_8RsCSPK1LwHQlqQU2aiTeovnzukiKCa3aBYeENCUWIkMi_J4lX3oshPXy8btBAIg9uaSGHVXoxVdCC8fSE61q1NbB84FlNMk6FPV2QIX6pl7y6ZOlPq6LOVXgijglx28tNgr3LL0E2q5DKJFS0rUPR6DrvhVKU-ZuepqAc5VaQn7v_CkOR8qJ-2eemK729V_ahyK_yMXW-VUQ1I0K-VSa1FrcP7leONVTDL_ppABKQ0A0x40P1E0Asg5BP7AYjsPQNhaJ909RdbcNiDfjPrpMLy4609kExMugcQpj5bsE0weyAMuo_5D3HMyvJJ_CIZeMyYZ-wh76f1WI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3396ef5ba6.mp4?token=MIrl7aZELY3tRE1R-i1AwdKiDyjPgq--pFIHMgUBNXxgAt5hakkZT9-8eG68-2lA8HeztipT_glTroksKjczEGolkh4d2UHseNe2YdP8Gt_wRcFkFZ0EU2ImkR0uu0Iem31ARgV6087LoYC8OkOT5nd0L42hIyPo7oefC9U6F-kLvs57EjlpHmOWP4XuJPg3dYcGCx1iLSMdiFUSu93tRyEbXyEun05fBG1y09Qun8L8SnYSpmoMfUqd2nTvvvt6ppjfxcVqKyTdigYTB2tPAxGLfTzyoXPOkGuhO7TwoEVeOBypk15W0CoXCwJI55sCqlOeZ3KFzsnjKrMzSDRJZLCiv29F8_8RsCSPK1LwHQlqQU2aiTeovnzukiKCa3aBYeENCUWIkMi_J4lX3oshPXy8btBAIg9uaSGHVXoxVdCC8fSE61q1NbB84FlNMk6FPV2QIX6pl7y6ZOlPq6LOVXgijglx28tNgr3LL0E2q5DKJFS0rUPR6DrvhVKU-ZuepqAc5VaQn7v_CkOR8qJ-2eemK729V_ahyK_yMXW-VUQ1I0K-VSa1FrcP7leONVTDL_ppABKQ0A0x40P1E0Asg5BP7AYjsPQNhaJ909RdbcNiDfjPrpMLy4609kExMugcQpj5bsE0weyAMuo_5D3HMyvJJ_CIZeMyYZ-wh76f1WI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
لحظة دخول جثمان القائد الشهيد للثورة الإسلامية الإمام الشهيد السيد علي الخامنئي (قدس الله نفسه الزكيّة) إلى مراسم الوداع بجوار حسينيّة الإمام الخميني (قده)</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80625" target="_blank">📅 23:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80624">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5460badcf.mp4?token=UCX1x4L9oNJYWEWO0yIwlpcmiNzjops_3MGEVUs-oofb8uYtbOQeAdEyF3W67oE7e-rsAWybHc16AZHT0mjRjNl8KO_pWvcTbTH0OkNd7LCXCLdMonESjS5e6GgS1SXVGK6spp9pcz98cu8BWdMmn0AV0qmgA6Z6gjLUbaxmaLRs-pI5pffifElOFQkW9u-dAj_UQTTQP-wHxurIUFyUo_S-_PdlLpyg0tD3MN9c5U8Rmto9zCHE2R8HVuLVLwTjbFM7BtNHFygSjlAoteppmh19P8DfkMn1pBOhyGCv9Pql9nlp_97G2Leqxftqyr0eIT-OiDNhXVyOZ_D0d4v82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5460badcf.mp4?token=UCX1x4L9oNJYWEWO0yIwlpcmiNzjops_3MGEVUs-oofb8uYtbOQeAdEyF3W67oE7e-rsAWybHc16AZHT0mjRjNl8KO_pWvcTbTH0OkNd7LCXCLdMonESjS5e6GgS1SXVGK6spp9pcz98cu8BWdMmn0AV0qmgA6Z6gjLUbaxmaLRs-pI5pffifElOFQkW9u-dAj_UQTTQP-wHxurIUFyUo_S-_PdlLpyg0tD3MN9c5U8Rmto9zCHE2R8HVuLVLwTjbFM7BtNHFygSjlAoteppmh19P8DfkMn1pBOhyGCv9Pql9nlp_97G2Leqxftqyr0eIT-OiDNhXVyOZ_D0d4v82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المصلى الذي سوف يتم الصلاة على امامنا السيد الولي في العاصمة طهران.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80624" target="_blank">📅 23:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80623">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s57DxaAf_COalK3ySnMABh8Zx4zk-yY11pjSwVXdoc2YpHBlGgX8mn5NjfOy423fY-ARPCdKp7QR7eJOBb91PnsXvHRlUVKC_FxbRPkmzP1FbSpPj3yNqm7sfLYw4xL2OelNojxyWZXPEsBX8WQ-lOgo1TlG3RweKAuqk59PZn6qcahT_2jH_TR4wmL_k761YtbL6LrDJ8YpNvnB1d7RFmEq3BGbCxv1FbTIl4Ydmasw65I-ms4rvG6_kdQb3zxBnrdnTlJX2ZlG_-3h79h3mmm6ZkFadgcQFGTcg49irvLMRi-8LxpTi6ms1EFAPSebXvLQ5y0urPjqeoDprq6MIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بزشكيان:‏
الآن وقد أصبحت إيران، المليئة بالأحداث الملحمية، تستعد لتوديع الخادم الحقيقي للإسلام والثورة، أدعو جميع الناس من كل عرق ودين وذوق وتوجه سياسي إلى تصوير مظهر دائم للوحدة الوطنية والولاء للمثل العليا للنظام الإسلامي من خلال حضور شغوف وثابت وتاريخي.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80623" target="_blank">📅 23:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80622">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoWqjmQyc3y9gS72wABoPVsnYNNw6kkI98jNnr58ZeCMnt4cSMSwtZTkSxoGDPOfp1gus9H9sBEa97ArGbAlt4NQIqiDA4ySmNK-Q9mOa6d4jN6wwleCZqdpg8fx4g3RnTc5qZoL7Dbl-yT8trnVjaB5mcWCkDIRdLm2zI5sDsK_sc-rny5-HzIC6pGGUG1J2Whd_n9H2bzIJZD4Yy3AsNKhEIHlDn4TzCJqrsGDS3dK8vGb55Az-wO92dbnO1Wl4o_di22Cvgwf8E1jaZm33CPEHlcQVezhhB7SbRF1oI8f52WgKEwrQwuf_C97mFRpqtL2MF2KFk57Fy2a6uHFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
في الوقت الذي تقوم به حكومة الجولاني الإرهابية بهدم قرى الشيعة والتخلي عن قرى آخرى لإسرائيل.. استشهاد شابين من أبناء شيعة سوريا تحديداً "نبل والفوعة" واحتجاز جثمانيهما بعد معارك مع الكيان المحتل في محافظة درعا دفاعاً عن الجنوب السوري.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80622" target="_blank">📅 22:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80621">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">صوت مجلس محافظة واسط على تقليص الدوام الرسمي ساعة واحدة " من نهاية الدوام لشهري تموز وآب.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80621" target="_blank">📅 22:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80620">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔻
انباء عن انفجار في مدينة دير زور السورية المجاورة للحدود العراقية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/80620" target="_blank">📅 22:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80619">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6-Zhd5zReoRnat2_w4Wo8zPkkG7hDBxbc1ewwWmPDMcbLHnmQI-JuGKtSwvcg1flrgHeD7QEKQeEG_MjVjTD3EC4m-NM7plTJR8ze3-8eWO6UI0X8bq-uLfxipGKOTPOK46TgemX2EgORx-FsSrK-d5ewrepydy3w_By1YPlrJ596-DYBVJxqDdULUjTn1naWio9hXBGKoA8TosdY7l4ZglJkcc8w0eGKA_u_2B_VlmnXzfHREdsTS4vqX9N9rfp6IbeGlx1FgXVki8YSPB1G23lsIQG1vrxR5Yc4ANkBYradBxurdUgCRCE00tUU0xQfFdpTQJ1e9ZMfm8B3Wdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عراقجي
: ‏
هل جلبت القيادة المركزية الأمن أم انعدام الأمن إلى منطقتنا؟ الجواب واضح.
‏وبالمثل، أثبتت قواتنا المسلحة القوية أن الغرباء لا يستطيعون حتى حماية أنفسهم.
‏لا يمكن الحفاظ على السلام في منطقتنا إلا من خلال نهج شامل وجامع، دون أي تدخل خارجي.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/80619" target="_blank">📅 22:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80618">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">السفارة الأمريكية في بغداد سوف تجري تفجيرات وتدريبات بعد قليل بالعاصمة بغداد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80618" target="_blank">📅 22:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80617">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">السفارة الأمريكية في بغداد سوف تجري تفجيرات وتدريبات بعد قليل بالعاصمة بغداد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80617" target="_blank">📅 22:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80616">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇹🇷
🌟
وزير الخارجية التركي:
تبحث إسرائيل حاليًا عن عدو جديد.
طالما أن إسرائيل - أو أي طرف آخر - تتصرف بطرق تتعارض مع مصالحنا الوطنية والإقليمية، فليس لدينا أي سبب للخوف من أي شخص، أو التردد، أو التراجع.
لا نمانع المواجهة. إذا حدث ذلك، فهذا ليس مشكلة بالنسبة لنا.
إسرائيل ليست مشكلتي فقط؛ إنها مشكلة العالم.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80616" target="_blank">📅 21:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80614">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇫🇷
‏
الخارجية الفرنسية:
قوات التحالف الدولي ستنتشر في لبنان بدعم أميركي.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80614" target="_blank">📅 21:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80613">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d12f5ea17.mp4?token=gaBaIMMD2mTPLnaF8k_wRXgKXEM6-pSr8OaWUjM6mKyIsNjtnGH_zR4r5jDuwmNr2-J2naWUv7PfDPy3YF7iCOdvtbP2djiGk4GpDnkxskKQr8Dq60MJf1pj8rcSIcXjDZxGpjIlQGseetJQ0u3l_z3NUgFYa1YJuQ6zrWwbW4o5-pMXAY8gl7yKqbkyg06QLZcvugwbjDxCTzgwi77LwNeUgHoa-odQeLmF5A47E1mGYylXkzBPo3JpC99ZqlDQdcNk0v1g5PfkEmJy_BXfmslzxxzDLZHOvfpdNJ3HsIWimF9LUeYUzURTqmfJ7SIJOE10_CBYuar2luEJCyTh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d12f5ea17.mp4?token=gaBaIMMD2mTPLnaF8k_wRXgKXEM6-pSr8OaWUjM6mKyIsNjtnGH_zR4r5jDuwmNr2-J2naWUv7PfDPy3YF7iCOdvtbP2djiGk4GpDnkxskKQr8Dq60MJf1pj8rcSIcXjDZxGpjIlQGseetJQ0u3l_z3NUgFYa1YJuQ6zrWwbW4o5-pMXAY8gl7yKqbkyg06QLZcvugwbjDxCTzgwi77LwNeUgHoa-odQeLmF5A47E1mGYylXkzBPo3JpC99ZqlDQdcNk0v1g5PfkEmJy_BXfmslzxxzDLZHOvfpdNJ3HsIWimF9LUeYUzURTqmfJ7SIJOE10_CBYuar2luEJCyTh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
الرئيس الكوبي حول التهديدات الأمريكية:
إذا حدث هجوم، فإن الشعب الكوبي سيستجيب بوحدة ورسوخ ودفاعًا عن سيادتنا.
نحن لا نريد الحرب، لكننا لسنا خائفين منها.
ونحن نستعد حتى لا نُفاجأ أو نُهزم.
علمنا فيدل أنه لا يوجد أعداء لا يمكن إلحاق الهزيمة بهم.
قد تكون هناك جيوش قوية جدًا من الناحية التكنولوجية، لكن في الصراعات، هناك قناعات، والقرارات التي يتخذها الناس، والتضحيات التي هم على استعداد لتقديمها من أجل الدفاع عن سيادتهم.
قال الجنرال أنطونيو ماسايو: "كل من يحاول الاستيلاء على كوبا لن يتمكن من أخذ سوى غبار تربتها المغمورة بالدم".
هذا ليس مجرد شعار. إنها قناعة تم تبنيها من قبل ملايين الكوبيين.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80613" target="_blank">📅 21:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80612">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANblqj8TGl3H4Q9m59YBgYH2Z7FukyuDTekr9ZmcKUhA-Gyc4u2haXGHpbYwSd6CJOGsVIMQxMdoPvTxOw0iKkO7j8WeYxi29k8_2ySKJR_BFWqrskCXz5hVjMJLN1rL3xnmW9jCHgRU2lXHgz9aoCeVZxXsdsO9ykZvOKyc6_ZUCOoxrEwqub7cANkVUNEev0eJp1VSR7z6VvlZe7ssYpQy-ON9K95hC_Q-lRj5wXy_VWXkuF5GKM1_DZ5IHltpuBiWXgCh89bJWXWMeOznv5hm7vox4l5JA_-gNHzjOYYM-DXQkHcvfZDQ5mlFD9xZjbKr6YwbtvUtIdDVkyTwFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
أعلن اليوم يومًا وطنيًا للإسكالوب احتفالًا بإجراء اتخذته الإدارة الوطنية للمحيطات والغلاف الجوي (NOAA) والذي سيفتح الحافة الشمالية لبنك جورج لصيد الإسكالوب، محققًا حلم صيادينا العظماء الذين عوملوا معاملة سيئة للغاية من قبل إدارتي أوباما وبايدن، ومن قبل دولة كندا. هذا يعني ملايين الأرطال الإضافية من الإسكالوب البري الجميل سنويًا على مائدة مطابخ الأمريكيين، والمزيد من فرص العمل في نورفولك، وفرجينيا، وكيب ماي، ونيو جيرسي، ونيو بيدفورد، وماساتشوستس، وجميع أجزاء الساحل الشرقي تقريبًا. هذا بالإضافة إلى تحرير منطقة شاسعة قبالة الساحل الشرقي لصيادي جراد البحر العظماء لدينا، وغيرهم (نصب تذكاري بيئي أعلنه باراك حسين أوباما وجو بايدن النعسان، والذي قمتُ بإنهاءه!)، ونصف مليون ميل مربع من المحيط الهادئ الجميل، حيث سُمح لكل دولة بالصيد باستثناء صيادينا الأمريكيين العظماء! لقد فتحتُ المحيطات والأنهار والبحيرات والبحار أمام صيادينا، وحررتهم من القيود البيئية السخيفة التي سمحت لدول أخرى بالاستفادة من مياه الولايات المتحدة في عهد باراك حسين أوباما، وجو بايدن، والديمقراطيين. إنه لشرف عظيم لي أن أفعل ذلك لأني صديق الصيادين - اخرجوا وصوتوا للجمهوريين في انتخابات التجديد النصفي، لأنه إذا وصل الشيوعيون إلى السلطة، فلن تتمكنوا من الصيد مرة أخرى!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80612" target="_blank">📅 21:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80611">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c576dcf67b.mp4?token=udgbC1tc0dzJeQODUcXWdeelSD_egwkpJrFe9b6LOlWu9GcZDlhpe80E0Fn0FM-zX6RJKH_Qg0HnNC5Ic2jivhz082x4sPM1jzSjdicWTLS8SrNBe9KP-m9rYSwSTtz-AQw7ALFjPJXjWBVzaFAMlfakS1X1gpM7YJ72BeXyci2oP_uKEc6ozA72UO7RsomsHCZWYkhN0RYugaZT45xfMSdI0WbfyA-93-uMsnigEBIWqL5LchH3dKzA_jcpgAIwY9cp1DwtY_9UFPg6MJjnUBlgCaF0wzcmm0QpDClPioDLlkMRrvznE8Lx1dTb4NfvAKeHvpuw5Be30tCvP0SVbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c576dcf67b.mp4?token=udgbC1tc0dzJeQODUcXWdeelSD_egwkpJrFe9b6LOlWu9GcZDlhpe80E0Fn0FM-zX6RJKH_Qg0HnNC5Ic2jivhz082x4sPM1jzSjdicWTLS8SrNBe9KP-m9rYSwSTtz-AQw7ALFjPJXjWBVzaFAMlfakS1X1gpM7YJ72BeXyci2oP_uKEc6ozA72UO7RsomsHCZWYkhN0RYugaZT45xfMSdI0WbfyA-93-uMsnigEBIWqL5LchH3dKzA_jcpgAIwY9cp1DwtY_9UFPg6MJjnUBlgCaF0wzcmm0QpDClPioDLlkMRrvznE8Lx1dTb4NfvAKeHvpuw5Be30tCvP0SVbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
المواكب الحسينية تستعد لإستقبال المشيّعين وتقديم الخدمات خلال مراسيم تشييع قائد الثورة الإسلامية وعائلته في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80611" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80608">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65bb5c1cc2.mp4?token=QihV4F4_G9VyJ-3jgzQECgTr8TpIJfOtJPa9BWhnklcObzYZiRgaTYB7CVCA08XksnoSZM3ppahFLFeQ5wZQE0pPMprqeqS3gQigrjDvjEJLCieBknOfibcK-If4Zut_joHd18kVmei1BxENB80yD2FT-ib6a2wH2PSBr6OLS8dLl61dz-5xVtgVdAV5oeYvLOkLtEL-iHL2gYOC4OIt3KyKxs6zA-hodJsGMs6pWfAg9VDE4TqLaFmN_liiOwEKHp5pWiXuQYfs50BjFVb75F2gIotKexVVzd04UAjB7aKA5lisbkuf_Jp2yvv5ZxYH7YHPHZUCP-F2rKYIFefWAB87_ezK9-0pkeby3jqMemMAagGUC40ul2IKOPwNhTIlVA1hrUrT7uymNyZRZ5vLJSoLwCtA3WqoRUU7muopp9kMnzFsCkpcLacUrfCgms8tUY9qhf1em8rxi6eONKLV4BeFRbmGQ0rXbET-z2wNrXtogqSjk-dARIt5T4qaSSH7DoPyubijy25HnamYcYQGLy2gXu18100kwnBhsNYB9s2cHR4rGcjswpq5vywbAbWdixAE3TzHndZNtAe7XIeIez9EKsJxxxNN5XwetI4ba4x_gABNLaF98DaE3uYAY42zfeLBP6bO9eOuPHWIeDZrpQvjaI0ZlVWkBDyccBhxU4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65bb5c1cc2.mp4?token=QihV4F4_G9VyJ-3jgzQECgTr8TpIJfOtJPa9BWhnklcObzYZiRgaTYB7CVCA08XksnoSZM3ppahFLFeQ5wZQE0pPMprqeqS3gQigrjDvjEJLCieBknOfibcK-If4Zut_joHd18kVmei1BxENB80yD2FT-ib6a2wH2PSBr6OLS8dLl61dz-5xVtgVdAV5oeYvLOkLtEL-iHL2gYOC4OIt3KyKxs6zA-hodJsGMs6pWfAg9VDE4TqLaFmN_liiOwEKHp5pWiXuQYfs50BjFVb75F2gIotKexVVzd04UAjB7aKA5lisbkuf_Jp2yvv5ZxYH7YHPHZUCP-F2rKYIFefWAB87_ezK9-0pkeby3jqMemMAagGUC40ul2IKOPwNhTIlVA1hrUrT7uymNyZRZ5vLJSoLwCtA3WqoRUU7muopp9kMnzFsCkpcLacUrfCgms8tUY9qhf1em8rxi6eONKLV4BeFRbmGQ0rXbET-z2wNrXtogqSjk-dARIt5T4qaSSH7DoPyubijy25HnamYcYQGLy2gXu18100kwnBhsNYB9s2cHR4rGcjswpq5vywbAbWdixAE3TzHndZNtAe7XIeIez9EKsJxxxNN5XwetI4ba4x_gABNLaF98DaE3uYAY42zfeLBP6bO9eOuPHWIeDZrpQvjaI0ZlVWkBDyccBhxU4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترند_تركيا
🇹🇷
في تطور خطير بساحة التحرش والمضايقات
😆
..
امرأة تتجول منذ ثلاثة أيام في شوارع إسطنبول وتتحرش بالشباب حيث يتولى نشر فيديوات لها عبر كاميرات المراقبة في مواقع مختلفة.. منصة تركية: منذ ثلاثة أيام وهي تتجول ولم تترك شابًا إلا وتحرشت به، ورغم ذلك لم يتم اعتقالها. ماذا لو كان المتحرش رجلًا؟!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80608" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80607">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">⭐️
رشقة صاروخية من لبنان نحو الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80607" target="_blank">📅 20:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80606">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⭐️
رشقة صاروخية من لبنان نحو الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/80606" target="_blank">📅 20:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80605">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🌟
إعلام العدو: حدث أمني صعب في جنوب لبنان ومروحيات الجيش الإسرائيلي تنفذ عملية إخلاء لجنود قتلى وجرحى.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80605" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80604">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
إحكام السيطرة على الشريط الحدودي العراقي - الإيراني في هور الحويزة بعد إكمال سدة حدودية بطول 50 كيلومتراً.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/80604" target="_blank">📅 19:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80603">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjF0KtIjK2yJg5cg3nbW-1xXRBfTSeo_57nYLpnh5Rf0QS8HKVPkJzN84ZzBEk2pbw2RcGxiB1ps7aTLZSL7RfPTta6JzVtQsTHiBB3bJsxh_kDfp4S0-TuBkXuJHFou4VocVkii-cmc3lsu_MFX5vh5wjB3b3XznjEDqMzrQC80Yi_XaggPNGcXpFpzZ1kOMAu8ZeZ8UODUc8qiizBkkzAZ4SGfOXuf9rtb01KHxw2nIHWSnTa2z8QG4DB9KJzeUxgeeBtMwMQsRtg8RcbJA8pkDOTDJ-AKzhvV2OWIli3h_sUJghjIta1wxKyYIY0tWyW_NTZh2LpSq16PO9t_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
غارات للطيران المسير الإسرائيلي على النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80603" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80602">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb72d46ebc.mp4?token=lgWCm4JmoQcgUxxk_GoND3f0kRDYJH-noCu02FiBvTPSnf0enUQ2VzfxZZBXsVqUlPSaV3XGgAiPoXZPzzXq7Rx2w6Ck8oOyVCOiyUc1hhQwLtygm7OWuT3gQbB-oWC0ANDhAXvlGXp-Uox1GZKJLzGXx08xsUodLfOKkwXlroHryCFxH0ieBJ9YT957VZqT1u03Xdte-sE0Su7qE52f6v-JqP_NEtvcEbzODuyl2kDVD0ix01XQbzLM1cKW89-RoTYaQvfLLUZ15mBZ2diEhJgRTMiqfe_NZqq1FpLu6MPLI7T_PcvBYi3vqmJTHW7qk2nYQ4XVBi9jftRztfpiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb72d46ebc.mp4?token=lgWCm4JmoQcgUxxk_GoND3f0kRDYJH-noCu02FiBvTPSnf0enUQ2VzfxZZBXsVqUlPSaV3XGgAiPoXZPzzXq7Rx2w6Ck8oOyVCOiyUc1hhQwLtygm7OWuT3gQbB-oWC0ANDhAXvlGXp-Uox1GZKJLzGXx08xsUodLfOKkwXlroHryCFxH0ieBJ9YT957VZqT1u03Xdte-sE0Su7qE52f6v-JqP_NEtvcEbzODuyl2kDVD0ix01XQbzLM1cKW89-RoTYaQvfLLUZ15mBZ2diEhJgRTMiqfe_NZqq1FpLu6MPLI7T_PcvBYi3vqmJTHW7qk2nYQ4XVBi9jftRztfpiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إعلام العدو:
حدث أمني صعب في جنوب لبنان ومروحيات الجيش الإسرائيلي تنفذ عملية إخلاء لجنود قتلى وجرحى.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80602" target="_blank">📅 19:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80601">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d8bde8ed.mp4?token=YCGp0tgmZabqOLfETosRUEvq17Cg1olfABq-6K16ic2sDxRXvRGsMmnLBu_5SCD0ziP9uNFXmH0R_HAEryMlLIBhpRpagndkkyiYyQMzEZ22ncmFrHaieECsFKqCkQLsEhbFzuXPfF9d5J82gM5_vmLuvvaY3UZbZNeEmmknxSCUhot1YvbahA76RVxwBHZkaYa4CrIjFBbWsmksu47b4r_DMbEY0Fmht0NLN7zIwe_eLrrOObxc9Wv73zYkEVank8GiMiteNRvh0hHWEoLTsGVIa4tLAtsll4i68bhI-Jk8JzxcWjfn_WlgpS2cwsNW-z246ARC3fx9K7tMpK1U-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d8bde8ed.mp4?token=YCGp0tgmZabqOLfETosRUEvq17Cg1olfABq-6K16ic2sDxRXvRGsMmnLBu_5SCD0ziP9uNFXmH0R_HAEryMlLIBhpRpagndkkyiYyQMzEZ22ncmFrHaieECsFKqCkQLsEhbFzuXPfF9d5J82gM5_vmLuvvaY3UZbZNeEmmknxSCUhot1YvbahA76RVxwBHZkaYa4CrIjFBbWsmksu47b4r_DMbEY0Fmht0NLN7zIwe_eLrrOObxc9Wv73zYkEVank8GiMiteNRvh0hHWEoLTsGVIa4tLAtsll4i68bhI-Jk8JzxcWjfn_WlgpS2cwsNW-z246ARC3fx9K7tMpK1U-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد جوية من مصلى العاصمة الإيرانية طهران حيث سيتم فيها إقامة صلاة الجنازة لجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي وعائلته ثم مراسيم التشييع والتوديع.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80601" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80600">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇷
‏
مندوب إيران في الأمم المتحدة:
سنرد على أي انتهاك لمذكرة التفاهم.
‏الولايات المتحدة هي من تخون الدبلوماسية.‏
حرية الملاحة مكفولة دون رسوم بمضيق هرمز لمدة 60 يوما.‏
نحذر من استخدام مسارات خارج السيطرة الإيرانية في مضيق هرمز.
الهجمات الإيرانية على القواعد الأمريكية استندت إلى المادة 51 من الميثاق وشكلت دفاعاً مشروعاً عن النفس.
إن تقاعس مجلس الأمن عن أداء مسؤولياته عزز مناخ الإفلات من العقاب وشجّع على المزيد من الممارسات غير القانونية.
استهدفت القوات الدفاعية الإيرانية المنشآت والقواعد والأصول العسكرية الأمريكية في المنطقة التي انطلقت منها الهجمات ضد إيران.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80600" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80599">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
القوات الأمنية الإيرانية تتمكن من قتل 2 إرهابيين في مدينة تفتان بمحافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80599" target="_blank">📅 19:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80598">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">إلى عموم المؤمنين والمعزّين الكرام.. استعدّوا للمشاركة في مراسم تشييع السيد القائد علي الخامنئي (رض)
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80598" target="_blank">📅 18:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80597">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8425182b.mp4?token=hGjcgChSLVNVkXj4OBkRKklyNw1r9uUHBEAanpNeHrbIB2Tg98ZGx9JbvYumOp3KBUgASriWvPI85QS2Iv6aJTYC26TJUsV7rujrVT8YnuW-OXWD8IThKvTpGX3cDKY9NUJa07YoDy7CQDxIIvMUEc5g8kdXbJylCTwSDDa3DovD2oS-rJ_dv5_x0u3TfSXd06YXZ556rx8uTiN0Xfi5sZrNes5fvywzkB7XXvrCneOYTWcBgvfHeqKXxjFlarWoul7Z8c4uXj_CAituRLVTrMeU3ls_yohmbiiMA9S42s72vYgLagn4rvCOsuoiSGJj196ybWVI4SX9jbH0k7aBYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8425182b.mp4?token=hGjcgChSLVNVkXj4OBkRKklyNw1r9uUHBEAanpNeHrbIB2Tg98ZGx9JbvYumOp3KBUgASriWvPI85QS2Iv6aJTYC26TJUsV7rujrVT8YnuW-OXWD8IThKvTpGX3cDKY9NUJa07YoDy7CQDxIIvMUEc5g8kdXbJylCTwSDDa3DovD2oS-rJ_dv5_x0u3TfSXd06YXZ556rx8uTiN0Xfi5sZrNes5fvywzkB7XXvrCneOYTWcBgvfHeqKXxjFlarWoul7Z8c4uXj_CAituRLVTrMeU3ls_yohmbiiMA9S42s72vYgLagn4rvCOsuoiSGJj196ybWVI4SX9jbH0k7aBYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
وزير الصحة اللبناني:
البديل عن إتفاق الإطار هو الجرأة في الموقف والإستفادة من المفاوضات الإيرانية-الأميركية وليس الإنبطاح.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/80597" target="_blank">📅 18:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80596">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🌟
جيش الإحتلال الإسرائيلي:
لواء غفعاتي ينهي مهامه القتالية في جنوب لبنان.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80596" target="_blank">📅 18:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80595">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⭐️
بلومبرغ:
عدة دول في أوروبا توافق الآن على أن السفن التي تمر بمضيق هرمز ستدفع لإيران وعُمان.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80595" target="_blank">📅 18:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80594">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60dd59daab.mp4?token=XB_LEgFn3ozS-eg0lhduhFm839tvjYM8c3fpzZb10jGy0PxTL7D1lwQZ4B3sBrwBczx7mDEKTGLmf3DUo9dFcirwhTdj21gtCgwGLDKlJXK5aoDmXwJL-7D-NhqNXKMqgGKWdnZjyxLKPboty6h2NGk1Lh3UwylOHWrvuT1Fr_nODwgunt7ek1deeyoypuDNTFcBRJxjFwJrKt7tUx6b2Mzr0gK7w3NXqLOc-04FCNqc90oIKe8xKibNwqxqmnWzT-_GsW6iiqddji5no0XZ2GIk9hEw3uYsyxiF0_oYvuAtcla2gYmMuh3t7bwy4XStM5hGRkDobOz_5mQ8Oao1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60dd59daab.mp4?token=XB_LEgFn3ozS-eg0lhduhFm839tvjYM8c3fpzZb10jGy0PxTL7D1lwQZ4B3sBrwBczx7mDEKTGLmf3DUo9dFcirwhTdj21gtCgwGLDKlJXK5aoDmXwJL-7D-NhqNXKMqgGKWdnZjyxLKPboty6h2NGk1Lh3UwylOHWrvuT1Fr_nODwgunt7ek1deeyoypuDNTFcBRJxjFwJrKt7tUx6b2Mzr0gK7w3NXqLOc-04FCNqc90oIKe8xKibNwqxqmnWzT-_GsW6iiqddji5no0XZ2GIk9hEw3uYsyxiF0_oYvuAtcla2gYmMuh3t7bwy4XStM5hGRkDobOz_5mQ8Oao1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بعد إتفاق الإتحاد الوطني الكردستاني وحركة الجيل الجديد..
بافل جلال طالباني:
الاتفاق بين باك والجيل الجديد سيعيد توازن القوى. أصبحنا القوة رقم واحد هنا، في بغداد وحتى في جميع أنحاء كردستان.
شاسوار عبد الواحد:
احتكار حزب ما للمناصب خطر على بنية إقليم كوردستان. اليوم يوم تاريخي للشعب الكردي. اتفاقنا ليس ضد أي حزب أو شخص.يمكن للأحزاب الانضمام إلى ائتلافنا.الحياد يعني عدم التدخل.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80594" target="_blank">📅 18:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80593">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c843cb12.mp4?token=Ouauz2dXM_EIb6hlnauCJuFH9CY9PTIsqtBU7Ass4vXanhiBqTR3kvqIW4QeRxqV1BCAbSLMxtNq20iOjS25WhUajJV_eDq5-Cel3ceiICrAJQeO0Bv113r9jDgL6SYLrM0Q5CIaoweFD21IQQ1Alx3Y868Tc8cQF0d9lYRUffjDaIcyB5thWmTqItFSJF-LMyvXwsb4D-OGJ22yYaI02LB_Srb51yZyWSFpo_6bxqZltRWrCLmzqwZ0_KsYDkoDwwcfFtudMZ67YBrANXW_bUFlfo2N_pG1HwYil5Eltf9K-FVApg4WC0wZCbkHDY4JmDysESBxqkjaXxCShq-CYFtih6ojcfRrVAWxpswaVc_7IhJD0Rxg5fMfVWhp9Ryeed_4lNonZir5ztRMbp_k76BSiTpXA3dTGS56KnwOMsqX4PTNW78mpFYRKdQXgaYf9gCd3OhGNH6dNtv3DWhAxh92XpuS06cI6bTmel9z-mhnCw6uD1VcYGqCysUzCQvxOlAw6tZujBZ8Zv_dMDMxbUOq8SGnHHIoNP54QoxHKs1MJUBcPgjk2naBaxD4LhHwubIEmnK_AhTPu8uRU8TnYrQpLpKYWeYPUZvWi9KQwNefJdigF1m3g6iekMcxKjkigDM_i1wMJKNsl856nt4JH4kYcXcn5oBhwgUKjgKnY7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c843cb12.mp4?token=Ouauz2dXM_EIb6hlnauCJuFH9CY9PTIsqtBU7Ass4vXanhiBqTR3kvqIW4QeRxqV1BCAbSLMxtNq20iOjS25WhUajJV_eDq5-Cel3ceiICrAJQeO0Bv113r9jDgL6SYLrM0Q5CIaoweFD21IQQ1Alx3Y868Tc8cQF0d9lYRUffjDaIcyB5thWmTqItFSJF-LMyvXwsb4D-OGJ22yYaI02LB_Srb51yZyWSFpo_6bxqZltRWrCLmzqwZ0_KsYDkoDwwcfFtudMZ67YBrANXW_bUFlfo2N_pG1HwYil5Eltf9K-FVApg4WC0wZCbkHDY4JmDysESBxqkjaXxCShq-CYFtih6ojcfRrVAWxpswaVc_7IhJD0Rxg5fMfVWhp9Ryeed_4lNonZir5ztRMbp_k76BSiTpXA3dTGS56KnwOMsqX4PTNW78mpFYRKdQXgaYf9gCd3OhGNH6dNtv3DWhAxh92XpuS06cI6bTmel9z-mhnCw6uD1VcYGqCysUzCQvxOlAw6tZujBZ8Zv_dMDMxbUOq8SGnHHIoNP54QoxHKs1MJUBcPgjk2naBaxD4LhHwubIEmnK_AhTPu8uRU8TnYrQpLpKYWeYPUZvWi9KQwNefJdigF1m3g6iekMcxKjkigDM_i1wMJKNsl856nt4JH4kYcXcn5oBhwgUKjgKnY7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد جوية من مصلى العاصمة الإيرانية طهران حيث سيتم فيها إقامة صلاة الجنازة لجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي وعائلته ثم مراسيم التشييع والتوديع.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80593" target="_blank">📅 18:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80592">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🌟
رئيس الأركان الإسرائيلي "إيال زامير":
تظل إيران المحور الرئيسي لجاهزيتنا؛ ويحافظ جيش الدفاع الإسرائيلي على حالة اليقظة والاستعداد لتصعيد سريع وعودة فورية إلى القتال.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80592" target="_blank">📅 17:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80591">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
الخارجية البحرينة:
تعرضنا مؤخرا لعدوان إيراني غادر بصواريخ باليستية ومسيّرات.
‏إيران أطلقت أكثر من 200 صاروخ و600 مسيّرة تجاه أراضينا خلال الحرب.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80591" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80590">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏴‍☠️
المتحدث باسم جيش العدو:
أنباء أولية عن محاولة تنفيذ عملية دهس قرب بلدة بيت أمر شمال الخليل (ضمن منطقة لواء عتصيون)، قوات الجيش تبدأ عملية تمشيط واسعة ومطاردة للمشتبه بهم في المنطقة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80590" target="_blank">📅 17:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80589">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duR3XTqd7M4Bf8OlGYFDOrXnqSb8bS7vtQlNrRizJc8-zY2CSj342FAQ6AEvNzNFBYMQ9Iv4ja8CQEHgUOTD1XsjjfU4oNX9LDK0SGetFW716PwAuo7BfzkmIiLdl01DfrG_MMyvxTlfsBTLu0y4fSlBLcqQNSrthq9Oj-9SsDROv7l1w6F6NCKMsNqzQ52tv8iHJ5sY2JIhnml1cpXJDvaFcUOBjk5Vs2iKKGMan0Ujvz8w_Zt4aaWyWIXCmgC8zCtCreNMFD5aMy2lTPtFDPrxHe6GA8OwjLhXvP69id71-vo9M4YK-ha0hHpO_R2YXiMKgw--XaSoOU0sb0oicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▪️
إن تشييع جثمان الشـ ـ H ـيد القائد اية الله العظمى السيد علي الخـ ـ ـ|منئي (قدس سره)
جاء بناءً على طلب الحكومة العراقية، وبالتنسيق مع القوى السياسية
.
▪️
لنا الشرف مرةً أخرى أن نُسهم في خدمة تشييع رمزٍ من رموز الأمة والعالم.
⚫️
المدير العام لمديرية الإعلام العامة الدكتور مهند العقابي</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80589" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80588">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ارتفاع الاصابات الى 15</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80588" target="_blank">📅 16:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80587">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ارتفاع عدد الوفيات الى 5 والاصابات الى 11</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80587" target="_blank">📅 16:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80586">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏وكالة الانباء السورية: 4 قتلى و10 مصابين في انفجار مقهى وسط دمشق.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/80586" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80585">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏وكالة الانباء السورية: 4 قتلى و10 مصابين في انفجار مقهى وسط دمشق.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80585" target="_blank">📅 16:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80584">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هكذا يتم نقل الاصابات في سوريا بعد الانفجار في دمشق وسط غياب تام لسيارات الاسعاف</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/80584" target="_blank">📅 16:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80583">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42a8a6d0c.mp4?token=sizr8aIvuEFlyfDXMmousp6nLyciOtCFiEKDgrRv7dqdX7LYohvuuhPWxfj9SX4ILd-h0OBuulflcC4RNNVvlOmabw8mzbH4TNtclsMhG8tvqPNhhVadGN5amLCUfCN-gsBkYMgCa2EmKIJ7T6_uS-mQGPslQ05LzagaxOfJE0j7oxap8FZD3DBKbX_kr2-XfhpsgaA-G1NQ6g6dhwecpNa-C8RpCsUMhl1Gp71SCE_VIIGk4sHddpZGa9r_uSMsR7JtMO99a7srf4c1_cxh8VUVzmuiCG9OlC4lCh8d03wuIRha0222f9O06KizwB6XJ5B0lypzM0l1kzCdaksQzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42a8a6d0c.mp4?token=sizr8aIvuEFlyfDXMmousp6nLyciOtCFiEKDgrRv7dqdX7LYohvuuhPWxfj9SX4ILd-h0OBuulflcC4RNNVvlOmabw8mzbH4TNtclsMhG8tvqPNhhVadGN5amLCUfCN-gsBkYMgCa2EmKIJ7T6_uS-mQGPslQ05LzagaxOfJE0j7oxap8FZD3DBKbX_kr2-XfhpsgaA-G1NQ6g6dhwecpNa-C8RpCsUMhl1Gp71SCE_VIIGk4sHddpZGa9r_uSMsR7JtMO99a7srf4c1_cxh8VUVzmuiCG9OlC4lCh8d03wuIRha0222f9O06KizwB6XJ5B0lypzM0l1kzCdaksQzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من جبل حريري في محافظة اربيل بعد استهداف مقر للمعارضة الايرانية الكردية بطائرة مسيرة</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80583" target="_blank">📅 16:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOn37EwLvhZOOFBfftf5Aiz9Ms5Rjc_zFTgeoAg5CP5GO-Se1g12o48zPDHWIzpAcmwYoVXtj5ak2DtPUELdO4YzgQWC0Doq9DOf5eQOa9yQ9yqo58imTUhXa9Y0nhF-4XH9PDbpiat0xC8dXXN1nFqUFVWV3aR3huVaDYS1bKyiip3H50AL0WNA6oQjqHNo4EJTBFPD2yqtlUXTKIFbzSqQrnNEWNKX0LSsC6LOkpVPidVV6sh-BIbksD_d_AeHnufJujAHqFCmzC7KXzx9lNWgWIVB0QwHxyifdpjwbZRf9hANot5B_XfhI6h0eQExTNZyyOJzzjDMox0EqH4ohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام سوري: الانفجار وقع داخل قهوة المشيرية في محيط القصر العدلي</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80582" target="_blank">📅 16:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80581">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5487b8626e.mp4?token=tAUms2BsLXejaszZ1M4jH4nuXOJ5Ag6cSuREJEX1f28N8POZ9ZkNSHA0rBQL90hwhlpLy5vqsqqsZmG_zvaaKYPdT6lSI5SS8up15se6oYaUDRLf4MXpR2CqvXyvkUk8EVtjopnTseinqJQ9JoxEbbwGl8618Mqyyq3keJRtQP-EERyLJ3NGuquBxDM22S0xWexlAp_y9hFsw6-ewQjn9GU8xYExO1dPhc43pQFO3yXlkhCCAX9WIwhEmoikpLgOGXFTU7VvHZFZVZrMA8g156Ccf06HQnrSkdQq2f0jxv8i9Zff6UGtW41tvPBvDZoLQDrhkZ-NOXuk2ojQkHEe7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5487b8626e.mp4?token=tAUms2BsLXejaszZ1M4jH4nuXOJ5Ag6cSuREJEX1f28N8POZ9ZkNSHA0rBQL90hwhlpLy5vqsqqsZmG_zvaaKYPdT6lSI5SS8up15se6oYaUDRLf4MXpR2CqvXyvkUk8EVtjopnTseinqJQ9JoxEbbwGl8618Mqyyq3keJRtQP-EERyLJ3NGuquBxDM22S0xWexlAp_y9hFsw6-ewQjn9GU8xYExO1dPhc43pQFO3yXlkhCCAX9WIwhEmoikpLgOGXFTU7VvHZFZVZrMA8g156Ccf06HQnrSkdQq2f0jxv8i9Zff6UGtW41tvPBvDZoLQDrhkZ-NOXuk2ojQkHEe7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80581" target="_blank">📅 16:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80580">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80580" target="_blank">📅 16:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80579">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773ef443d.mp4?token=ez-i2u11KSwzO_tp3cF7f2obax1q1Jlaix6DZ33znePLArASxTTutRH7DABkI3zSLKa7keoHfsdLML7Y_KkukJ-2ObRtxQKZjBon3lMBqNrfWSq7v7GUmOyrSVujU6yR9N-UER8o2dZ84vHxCt_29BNhGLSSTLSWMyG5fPzbuZ96e5H2-1jk9IWTZ5aSmqftORi5oSMMW35BbwYCz6CzOIz-X2I1sh0BiMbihZ44NU_x1-SgXr7iqkdEvOHJKQD45e1L80hntTfckRdVK8629nYgbP9DMOXMQSdJvyFPs72yGvhEtN0RipwKYJzw2ONqcdwmFbIeULuTTyGQv52n7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773ef443d.mp4?token=ez-i2u11KSwzO_tp3cF7f2obax1q1Jlaix6DZ33znePLArASxTTutRH7DABkI3zSLKa7keoHfsdLML7Y_KkukJ-2ObRtxQKZjBon3lMBqNrfWSq7v7GUmOyrSVujU6yR9N-UER8o2dZ84vHxCt_29BNhGLSSTLSWMyG5fPzbuZ96e5H2-1jk9IWTZ5aSmqftORi5oSMMW35BbwYCz6CzOIz-X2I1sh0BiMbihZ44NU_x1-SgXr7iqkdEvOHJKQD45e1L80hntTfckRdVK8629nYgbP9DMOXMQSdJvyFPs72yGvhEtN0RipwKYJzw2ONqcdwmFbIeULuTTyGQv52n7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالات اغماء في صفوف المسافرين على متن احدى طائرات الخطوط الجوية العراقية خلال رحلة بغداد - بيروت بسبب غياب التبريد والاوكسجين طوال الرحلة</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80579" target="_blank">📅 16:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80578">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مشاهد من المقهى المستهدف</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80578" target="_blank">📅 15:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80577">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b37ae7cf1.mp4?token=YCvSYbo5QpVlPSYUwSWyEkBgmgGz2j3IMktGhWUxcx1H5dGszO7iKC9YvCSCxfHhGL5JoNDi1bQ2qBEzL7iOPCdpFJCg-C1LXjj4V5YN54R3jXxvbU0se6aeI1fJG7a0fl8R0gSxg-XfHcoTtA9oOIQ22ojw-j2P1124koTmZQvI6cMNrEQD9XIFDZAuH-acobrsUIsH4kFDJ2gK2PX4Vnqn7wtaZtnFXxerppSQpysmLnVlMPXqU7-2BZK75GXEXC6Oj2-sMy1G2GNuQOofcSU9LKnhhDZXJgPzcjfNAQs7pwVdWJzgsTO3H86IArDYUel2lU-9tRa4mgXzwMArLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b37ae7cf1.mp4?token=YCvSYbo5QpVlPSYUwSWyEkBgmgGz2j3IMktGhWUxcx1H5dGszO7iKC9YvCSCxfHhGL5JoNDi1bQ2qBEzL7iOPCdpFJCg-C1LXjj4V5YN54R3jXxvbU0se6aeI1fJG7a0fl8R0gSxg-XfHcoTtA9oOIQ22ojw-j2P1124koTmZQvI6cMNrEQD9XIFDZAuH-acobrsUIsH4kFDJ2gK2PX4Vnqn7wtaZtnFXxerppSQpysmLnVlMPXqU7-2BZK75GXEXC6Oj2-sMy1G2GNuQOofcSU9LKnhhDZXJgPzcjfNAQs7pwVdWJzgsTO3H86IArDYUel2lU-9tRa4mgXzwMArLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نقل عدد من القتلى والجرحى بعد الانفجار في دمشق</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/80577" target="_blank">📅 15:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80576">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afbe8efc5.mp4?token=cIyECsedckXzfVFcwDtxrgiP3uhGemz5CLRQZQdonbNoiNJclGFWNjGjxXX5Ry3rldLtTn5TLlGM0ILIdZxbCWtwVak7FdO6w90iER4cGcSUUZXb1smTDqT1RzOPz8ICqvyI0LvuiWLeBINKYTIvuHWI6kdOkns7Dl_-NrbmM6NtuDgveM3qoPaM4ixY3Xc58O7ysIZdHh7IRWNsNE9L4CgRP3naqPnhZ1f8wqOl6QaXbj7DzIok7CuUy6hf9gTL6c8SBWSq38pDsOpjNoDF0v6LONxEWW_sTtA9YcPduAfhqJsseLkRnLFCK7NnsEmdxGHY5xthNYyyxOzaFYiqeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afbe8efc5.mp4?token=cIyECsedckXzfVFcwDtxrgiP3uhGemz5CLRQZQdonbNoiNJclGFWNjGjxXX5Ry3rldLtTn5TLlGM0ILIdZxbCWtwVak7FdO6w90iER4cGcSUUZXb1smTDqT1RzOPz8ICqvyI0LvuiWLeBINKYTIvuHWI6kdOkns7Dl_-NrbmM6NtuDgveM3qoPaM4ixY3Xc58O7ysIZdHh7IRWNsNE9L4CgRP3naqPnhZ1f8wqOl6QaXbj7DzIok7CuUy6hf9gTL6c8SBWSq38pDsOpjNoDF0v6LONxEWW_sTtA9YcPduAfhqJsseLkRnLFCK7NnsEmdxGHY5xthNYyyxOzaFYiqeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من دمشق بعد الانفجار الذي استهدف مقهى في محيط القصر العدلي</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80576" target="_blank">📅 15:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80575">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21adf25199.mp4?token=REEN5-2_QxI1gDt4lsRKG7M1FPDEJ4Hq4taRA8zx3QEZx_ZRt_EUqdMMSkJ8AB9zhap907x4j2nZl4VdUCckMU6dgoJ4SbzeuRXUaqYQGnG2-nfLrhS05Ngug6-dDQ_3sd5T7zIRHTFOiI_iSvqOHIoGUESz9m3TKKseyCecYjmB4hVx8Y-5GBRYPP6TW3-vxcEVJzUW7xByH17EEBAFV4pXX12uL0ZTy_24lqALlt0qf2Sm4u7T5SSwyruSP3hErZEXG7giE1lxfgSgQI8_ygHmk2yEtfAun4ZYyufrvbBbD1HzysbpY9KKW05HGuIyGPUJN7se3co-TGwPlA_sD5kqTszehH5iGadNqXLa9nH9IvJJ9lTt6LK-Fymz9EPnxycIRy10vp2fulNlP_DbTLNEPMQpQkQkgu5GL1_UbgUXD07MwrfDUPajvA_m2NGGNPi4BrwOVDuN6zkwubxFuCP0Vnsq0yLvl15PoUVrzzPQwwHlrDLvv-v9uJZ5GC_h58HtnxfEM3Hmn1CnAvAQD7jjrnFsTM_7rF-mc5JzlDoQ2LsiIdajejP0ormO6UabT3wBGjnlgPyurA406NJ5nUl9A_LgkJscHGX-UPEwhLWQZxuGVVZq4nAdN2hUk86kjbhUwNO2XzDYkD90bYRLjst4TRS_fPZP0KKq4LsJmXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21adf25199.mp4?token=REEN5-2_QxI1gDt4lsRKG7M1FPDEJ4Hq4taRA8zx3QEZx_ZRt_EUqdMMSkJ8AB9zhap907x4j2nZl4VdUCckMU6dgoJ4SbzeuRXUaqYQGnG2-nfLrhS05Ngug6-dDQ_3sd5T7zIRHTFOiI_iSvqOHIoGUESz9m3TKKseyCecYjmB4hVx8Y-5GBRYPP6TW3-vxcEVJzUW7xByH17EEBAFV4pXX12uL0ZTy_24lqALlt0qf2Sm4u7T5SSwyruSP3hErZEXG7giE1lxfgSgQI8_ygHmk2yEtfAun4ZYyufrvbBbD1HzysbpY9KKW05HGuIyGPUJN7se3co-TGwPlA_sD5kqTszehH5iGadNqXLa9nH9IvJJ9lTt6LK-Fymz9EPnxycIRy10vp2fulNlP_DbTLNEPMQpQkQkgu5GL1_UbgUXD07MwrfDUPajvA_m2NGGNPi4BrwOVDuN6zkwubxFuCP0Vnsq0yLvl15PoUVrzzPQwwHlrDLvv-v9uJZ5GC_h58HtnxfEM3Hmn1CnAvAQD7jjrnFsTM_7rF-mc5JzlDoQ2LsiIdajejP0ormO6UabT3wBGjnlgPyurA406NJ5nUl9A_LgkJscHGX-UPEwhLWQZxuGVVZq4nAdN2hUk86kjbhUwNO2XzDYkD90bYRLjst4TRS_fPZP0KKq4LsJmXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتلى وجرحى في دمشق بعد انفجار في مقهى</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80575" target="_blank">📅 15:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80574">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سماع دوي انفجار في دمشق</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80574" target="_blank">📅 15:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80573">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سماع دوي انفجار في دمشق</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80573" target="_blank">📅 15:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80572">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_d8goudhKCNKJeuNTEP3og-QWAtBQuJx35fANrx1hvkaDZ5kfWzQi8aAelQDXSsFvwepsphYsfFfKSWlod4HKqwVoo8eyFOHjQV7QPEjE_lHuDv8lkIFenGSzwYP5pFwCUoYXLRJpMP1D2wQiaGISncgrdVaYhKZ05Mhg7pvcawo-7Ysw3cg_TzvXA7QeSBP2ElPL6xgyDCM_fE6iHW05fNG8q-LTb9fIdaY_ynuqMTRYwtgoRMyZvJtNjTNFpri1_ONrfdrvDegu3rm35Uw7hRe5mMioi_9DJsT7n3V_APDKdM9mVvUJtjNKYB4hqANFAQk96Vjx-hDz9aHiVEUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
ترامب:
تنفق الولايات المتحدة أموالاً على حلف الناتو أكثر بكثير من أي دولة أخرى لحمايته، دون أن تجني أي فائدة من ذلك: الولايات المتحدة 999 مليار دولار، المملكة المتحدة 90.5 مليار دولار، فرنسا 66.5 مليار دولار، إيطاليا 48.8 مليار دولار، بولندا 44.3 مليار دولار. أما دول أخرى، بما فيها ألمانيا، فتنفق مبالغ أقل بكثير. (2014-2025) أمرٌ سخيف!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/80572" target="_blank">📅 15:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80568">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzhaKR2bgmCFVwjyT3llGEhmtVTUdCpH9RFhwr7Q96EMTF0BiFTqQYW8prpV5KMGJp4Qkm1y3vj-ZDm8Nj1HSOTGdlP9i9e2fjJjDY5WdqLHXlh1ZSUln841KrwA5iWx5vk3dgrehxb846IqWDeeWpdnrMPFfVGI16fUFDsIceyNhO3MB-o7BFmV5JXF8sQ7wALSCqU3Mx908IwM_20sJhAcSiKoxZVARKaCUnfBjk8J4pjmBolkVUuAZW7AerhSKDBMl57MJfss4fFf8beqtzxheDshuEwG_hCgG93e5lPJ8c2445qvC-aqz7CyODkPC4QM_PTqq3_eiDv3o7YozQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ov_0gsBAFKiL3MHzFzxbmo_CDa6zw-vy-ik3lYOY3kqvPicqciatpioOSrLJsOKOAn2UoZomlwDha4_XSiLAjrXBXXuuLK5DUd0wHD1AiLEA5VYKd888PaQfLhA0Uc5SxLchrkC5JPJwOhVezUZChaRXBLslGqbZRw9YqxcNH9ZL4Y1Z_xwi7ivbZAl05ki9f0V3HvY9_YZoJw9JGVnOG_U36Rdp3akp4wJG4lvl7faWU3GBiVpP85X_F_L6ZQD8Qe4tYRR0vZaM_sbIUocfWp3oGb1HUbZVrFnmFHx9QvQ8zKQAcnCcuPwYv2obXU0R4Wqms0R15As-d9H1Mo01iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ce5BTLKo6N9mrIU1ICwRDaLAI5oEK7BthgRYTOsNXQ_53R2CYY0kFAaHAYAm9uvp0bW5QgYsvlKDbM7_KYyKLgWVLMXBNT9JvXN4XT9FNfGvH3stQY96sumxCyK2qOz2II4QzPBvZAHoip6HC2YwAME0BCmHKihhhrCxAr1OKwRvH0uPuc4C0otkpuSDjQ-VEu_1l65eGccbfnH8zjsECHd5wKCJWO5Dz6U9C77bxLD20QlyDqv4XvZTiLchxN8lHfTEwI8CJt73s7zTx6WwdXegCnBL2u5ctwn6wnMtew6SW1ZTS_TynlofB6OgbAV_FhPDRWDnn0_CAW0ZybLRCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bA4YQc-RKKUr0UWrBiuPnG0gnWspk_zzv7wzzNlU1_q5Ngeo0dlhyhlUHzOiy9I7EptOnc6C0lah5baC-SsCHuf8CDl0ASzsXmSDfgqZJJ4LxAIBDmbT6iAfeaDmaSSGAykcaVmF7DJvd922G_Te4knytM50-jog4YpOHYgxzNw0iS-VN3kjmkNmxz8cUqCVksICQlAyI9PW0lGfCVHdljNYc94_fl5YBHFc22EKFQ_HGTpw-ieRu6EseXGea2G5uXrE6_SE3T9uhsBAu4CqzodAy8RYJLPRy9_X6MB8TX4b54hCpDSUz5lZ0qNd4eUiY_7VKuCaqxdfl1o4UxpblQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
ضمن استعدادات التشييع..
الحشد الشعبي يواصل استكمال نشر المظاهر العزائية، ونصب الرايات واللافتات في المواقع المحددة</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80568" target="_blank">📅 15:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80567">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1ed8bed24.mp4?token=PHbyfPqPnHBrk5TbdO94V7gwAGHpTySwMhOs3rcQjfOidDf0kTbvH0kv62YjRT3baaq-454C4z9Zm2QnBX2-4ZoSL7IFeScblWHqlXhLSbBYumaWCAL1-_vb-DQGBiFohgyek7lYlo7chDMPRmfXjHfNOAJl5H0p-jKHCwn_dp97bI0K1q9PNeA-HmeBCHFxmUO4_pfIy4ykWObiu_SfQA2pBIX27KditTgvU-rmn541jtsdXswzEIWzwf_RAs7_APW-hW8JKFsnHX04chQ7hvOL2m106JOzq2nG9OPmb2rXXBFXrMX0muSdhDTxwDG6et2zekg9lBk0NWQGBjGgPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1ed8bed24.mp4?token=PHbyfPqPnHBrk5TbdO94V7gwAGHpTySwMhOs3rcQjfOidDf0kTbvH0kv62YjRT3baaq-454C4z9Zm2QnBX2-4ZoSL7IFeScblWHqlXhLSbBYumaWCAL1-_vb-DQGBiFohgyek7lYlo7chDMPRmfXjHfNOAJl5H0p-jKHCwn_dp97bI0K1q9PNeA-HmeBCHFxmUO4_pfIy4ykWObiu_SfQA2pBIX27KditTgvU-rmn541jtsdXswzEIWzwf_RAs7_APW-hW8JKFsnHX04chQ7hvOL2m106JOzq2nG9OPmb2rXXBFXrMX0muSdhDTxwDG6et2zekg9lBk0NWQGBjGgPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالات اغماء في صفوف المسافرين على متن احدى طائرات الخطوط الجوية العراقية خلال رحلة بغداد - بيروت بسبب غياب التبريد والاوكسجين طوال الرحلة</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80567" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80566">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39a62f24c.mp4?token=VgsHENFW_HmLRpJmMDn48kdUXb81yjj9DZhxX_QWvxmujByOH3jTBiQ31G5sp98d9J9cOFQPvtQoWE6gBdm3iCjAmMLcaGt_TeR3jdDIfwRMQJeMJyN_UzKiI4Bg-Zr4jMpt9qIsw7_UXv6tC6H9v1dQVgJ5fDWppTlTXT16b_raxyi9I0gSZfD7OnGXbEEwvvjW1tOleIzsv0ksKTprDYIQoLRQ5Z_SXOufOlgLQGFrJVrDd-41omJmQD-Tqxk4Hb1AAZ_kgLeB4TBl4UJ_woJ5KKUmmYsnFJJAdfPn9KHXEennPJ0xZlJ1yqEDWQfPG2v2yOMlMVhmCrERp_Ms0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39a62f24c.mp4?token=VgsHENFW_HmLRpJmMDn48kdUXb81yjj9DZhxX_QWvxmujByOH3jTBiQ31G5sp98d9J9cOFQPvtQoWE6gBdm3iCjAmMLcaGt_TeR3jdDIfwRMQJeMJyN_UzKiI4Bg-Zr4jMpt9qIsw7_UXv6tC6H9v1dQVgJ5fDWppTlTXT16b_raxyi9I0gSZfD7OnGXbEEwvvjW1tOleIzsv0ksKTprDYIQoLRQ5Z_SXOufOlgLQGFrJVrDd-41omJmQD-Tqxk4Hb1AAZ_kgLeB4TBl4UJ_woJ5KKUmmYsnFJJAdfPn9KHXEennPJ0xZlJ1yqEDWQfPG2v2yOMlMVhmCrERp_Ms0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من التعذيب الذي تعرض له الشبان الاكراد على يد جيش الاحتلال التركي</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80566" target="_blank">📅 15:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80560">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANhS6CxBrZOyDseRutJh9AlYmrV0fhP7gVBup0Uadde5cHlaLKN9WpSsmiMsxaJP3EZbUxEetrF7qWropSPfhPle9mhjg9IQ7WpuwHYYr0PLdUgCc1WdV9DHk9JSjv86VIpXdPuqpnxl21Sft44xTpAWlY5_q00IHby2sqcAtgVpGz2_Zu8ttMJdjWmLmlMWGICPZmobySz3SyYu5mxRk8_uTq_xXq02BpPJcbIvfE6Y2kpfNBaq0iRVYCTlUKWrLteDZ3I3ecrzmZ3kZf4Ne2jzWnsHWDUy60SScp2fmeSUR_GsX5p5858PGfUc9pOrYUZKb3nQZ3q6gOR9q8eVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZ7uM8T2hiGwrIwRKD6XcjWkiI2oqmccF5kdql0G8V9dQtPlp89hghzppfyQzrM6JvcZJkrLrPPVyAdmnnaImNoKsO276x2ETjDRSwCR7_VnOVERBB4JIIOtUTtFMnIR8LWZ-CvyIj2CuQ9iYT_HyI98bv5KSXgvQQG2cdzcTZwjWdIgNpGCCEceAwONODB_pE_cCinr4uzU2pDi3hirpc9WAYCAE_9UOUVZAK66ZJXKxbE7220HzUvZsegTuadaSXb4tsRweaSzu4pLNm10izG6_09LU9RKV-el2kufXGYYUadUMxGd5c-OkVXpkrTBOKbMY7unwDHeVrpD7l-GzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jHO-yhtv_CUTJvqvYiz3t1wkS_RGd_jiIk-oXwRFurm_LaxbZQP2HZnDVOpfXgbeocK6fgD5seBv-NLMBuljsqaSSBU16LpuaVvMFUQKAn-eCIVTcoucz1O1bW5-0giXKACu-vRLULZZMkrSFWNSLGppNyVkK7Q-bPIsBBt_3UVyGtjwR92mHwds2OdWWV4CeRd5X5Cgz9LD5oJUii3XzX5IaNgGlEJihvtL33KsFfCa0mpTKWVT-jwq4PjRaKF500lEA_6zJ5nhOpmyrbQptHeArelhLUu1kvVHZLVPIjkCUxWz2yzxkWqSdFb6jyqA2d7PMcaZWm2J7eOY6Skoag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BUcc2wopbaIgdpTpRpcjNTkfmgahkqXEK0CHD7wki71SNCoThQYWkEnfjB3gMzGGVE3MJ8EIrq6s7gMikeA11pFSOy3ZMYSE2tC93FaUH0ssB62ttCfpGs0JpjOjHw0vbAp8RX496t5OL8qM5bPX2SKqJ_lJb7xbY-oXHEs0w31Rs1d6nWdJaCKW6kpq0oyiMFOHVGoMUM_GBa8G2wB7aNvZK-NiA6vZkZpwhQrHToaGyPA5yevwvJIu5utkMR3GYvvVgdh22MFi5wuSQJtP-7J7RQcwwDoD6_NyqZ8reyVG8LX6ljoAOCyvIy-2AVxCpK8zH3quSuFqr-mFHZn9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUAAuvAAkCDn3oyeIMV4uszQNKrjtjibfZZf9BgLd0Ps8Vqoq80HRs-SNPeh3R-oWIMOm6OlAKuC6tw2AEFl5ZJHo3Oag1bVViEFwfttwAxIJfE7KyKM-UVitF6Rvwqf-lIqrxrybi2VmfifRcIkZa6BLJELLbUtf67zQpBTVeHjLLzVGpBv4X-tXKC4_zV8QurAek778bisIbgbt--Th0Npi7yuK0f9KeYN71dC_9TYW2mPzZwZL-8uTcN8--qWi113scQJfR2qEJOVyAYUxdVuB_RbG8wCaDkV4nTl2HZ_Aa7HVAf3RmNPNcVqC7dxaK4HXFOjnG_Bj8beMY0OIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYmEBbz6dFs-IiE0auTt1sltWPOZygyT8v4Z-fWiedb6Vki96mEiFak8rl-2AxgA_Zalqv0veZtm9cuK1_DHFOgA1nphM521TJe-oEYKQJn4Kj2wfGX26upfyf63SqUQaa2xbjRX1LROIogby88XX7VKat5I_9WOQm0BNIeiAeEq8iZwmisxv-6jQ69LhW8UOWBGYL3I3sy4OwN7ERxIi3UeRYowV865lFEsox6-3b_ZlHNM7tioT2wV5ICyCACL9pthsILKu4w88fwjMxilfF_5AI00em1otvjjg8BNnqQ5-I22av2q_afff3f-8NO2ihS3ornmKRgXvj23cv_hEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جيش الاحتلال التركي يلقي القبض على ستة شبان اكراد في قرية شيلادزه ضمن اقليم كردستان العراق ويطلق سراحهم بعد يوم من التعذيب</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/80560" target="_blank">📅 15:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80559">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">توقيف الإعلامي حيدر الحمداني في كربلاء المقدسة بعد شكوى رفعتها العتبة العباسية</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/80559" target="_blank">📅 14:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80557">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
أيدينا على الزناد، وأنظارنا مصوّبة نحو العدو، وآذاننا صاغية لأوامر القائد العام؛ فبمجرد صدور الأمر، سنخوض الحرب ضد العدو.
المفاوضات تقع على عاتق المسؤولين السياسيين؛ وهم يؤدون مهامهم.
التفاوض معركة تُخاض في خندق مختلف. ولا نواجه أي مشكلات تتعلق بالأمن.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80557" target="_blank">📅 14:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80556">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIYbhsKwo8bG7bPWQjw00NSmWcU3er-WxNLxYSuSLkKqcM4vgrZwxDfYutsulIamxVUAFrs_C7CYvSWcnNoekKcXdS1D-DE2WB864kb7qz4_oBuIq-bmaG_gIxVP2RprUw8yggwl3YQcV32_LdvY2HmrGL9tN-G7XwZM_kY1qxgyXdDHBvFVPz8Maxd9T1ei61AS3jFHmkrYVu0kx_kxcI8FUjCiWspMXTb7PI9NAUt4I8_blVr4nXPBL__8F_Ekh45KpcjvEUOwTBAXikXLQ0dtqWMIvD_cep3sRECOFGSyWFQuIiAg2QZWOHezFgkhRUvVRDf-FOeigFb6g1MX0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
السلطات المصرية تلقي القبض على الرادود الحسيني العراقي السيد مشتاق الأعرجي إلى جانب نحو 50 شخصًا من جنسيات مختلفة بينهم عراقيون ولبنانيون ومصريون وآخرون أثناء وجودهم بمنطقة السيدة زينب (ع) في القاهرة خلال احيائهم مراسم عاشوراء.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/80556" target="_blank">📅 14:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80555">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpRdlkDDkzvJUK5TSuoTXvu55ZAYXUE4AJeqF_LNIs7im9WdRLWA2i37H4C4Ln04MvM_el2XnInlGgqs57X6CplCjAKVTeN6chYTZkNawTq7pNBfGgV97nWYe7hzpASCilfVs77w1labdxXxLcGjel7wufmYtrz4xMHTFWAFXDYcnO6xosBsI4Aor_czRlUqs9CVA1h_uK4VALzopxDhRhsEhorh_NEO0GHeNKFDQiwrVXpeVuFd64zIKAWB5vV1Tk6gMeC_OLuCeyW-hb8xptHN83RAAWhFAn3pdtooOqEGeY2Zk3X4txeYBrY0E_TGqBXtEnZEcioiJqF0Rw5PQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
محكمة التمييز العراقية تصادق على حكم الإعدام شنقاً حتى الموت الصادر بحق المدان عجاج أحمد حردان التكريتي بعد إدانته بارتكاب جرائم إبادة جماعية وضد الإنسانية وأغتصاب وجرائم قتل بحق محتجزين من ضحايا عمليات الأنفال.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80555" target="_blank">📅 13:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80554">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
الجمهورية الإسلامية الإيرانية تعلن تعطيل الدوام الرسمي يوم الثلاثاء 7تموز في جميع أنحاء البلاد</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80554" target="_blank">📅 12:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80553">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">قناة خاصة باللجنة الاعلامية المركزية لتشيع الشهيد الامام السيد الخامنئي "قده" في العراق
https://t.me/KhameneiMediaIQ</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80553" target="_blank">📅 12:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80552">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/80552" target="_blank">📅 12:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80551">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">▫️
سيُعقد مؤتمر صحفي آخر يوم الأحد أو الاثنين، للإعلان عن تفاصيل تنظيم مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست نفسه الزكية).
▫️
الاجتماعات مستمرة مع جميع الجهات ذات العلاقة بمراسم تشييع الشهيد القائد السيد علي الخامنئي (قدس)، ونؤكد أن جميع الجهات…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/80551" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80550">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔻
سعد معن: التقديرات الأولية تشير إلى مشاركة ملايين الزائرين في مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست روحه الزكية) .
▫️
أُعِدَّت خطة متكاملة لتنظيم مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست روحه الزكية) .
▫️
نهيب بالمواطنين الكرام التعاون…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/80550" target="_blank">📅 12:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80549">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/80549" target="_blank">📅 12:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80548">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-Ck0msskXLHonimnDVTrmyh3U7dNkXshYENmJLzFtzWpbTCZGNcp3pPeRcq1dCDXlXgO_7zmXqaEupaeqXJa-XhMDYnoi9X9q4nLOrDG-0Ya3n7GUGix-aMS_qpVlCrMdbrNjCuj6V1TxK4Pi34UP0UWsoK18GBl7O1_4D0JEX-kPmyst41pHlRpB_9UD4KoBRwOUD677OEMvM9ga5rFvxf3nGFXgQT1sCIpLAIqJkSFkDtcHipZcJmdUMQS_YceWSMCvit7B9DTRc6PbQrNe0cwlPAbU9_AJWGGzUcI-h0C8kTIYiLVceGJO0An8kgDP74blGPQB-nzeIoe2xJJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80548" target="_blank">📅 12:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80547">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
الكيان الصهيوني يدعي إلقاء القبض على مواطن أجنبي من طاجيكستان يحمل جواز سفر روسي، بتهمة التجسس لصالح إيرانيين على الأراضي الإسرائيلية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/80547" target="_blank">📅 11:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80546">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔻
ترامب يُفاقم شعوره بجنون العظمة.. حيث نشر مقطع فيديو تم إنشاؤه بواسطة تقنيات الذكاء الاصطناعي قدم نفسه ك طبيب يقدم خطة علاجية لما وصفها ب"متلازمة هوس ترامب"</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/80546" target="_blank">📅 11:21 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
