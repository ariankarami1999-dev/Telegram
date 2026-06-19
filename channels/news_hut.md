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
<img src="https://cdn4.telesco.pe/file/v8PzzxOhu63Ov8gWZOYVU5XEFB8I1Z4hdBsEm4_1oC0ucECtjQETqvyHUnSn_yVwAa34DdiKiE5xLQDaQVkD0w_biQgmBK4-BGx0zxBSOTfYOCN8v2-J-LyuJkdzLEmZ1ZNWBsIIpDlRZTbJitdfg-U4-n_XcFUq4EzlKYb1SAfDf-D8QJNFyCGABOtPDItlJ0r9MQNnaeNAQqrdFA-1Ok7e0ygyyPOEXfceZPvzYVSy7n-VdrhWts68XkcF_vOiweg5IWyhhzQzV6WV5Ise40vNrOTYsbwKan6TX5RYHX0AYx-y4mvnU4TMjmVTM6IboyhP_Ieer1YDDk53r-_QXg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 13:44:06</div>
<hr>

<div class="tg-post" id="msg-66484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=EJ9jEvEYK1F8H1zlYZtPq5Amtko_vCYclMkFQpKU3AOQo_vhz_czW9IVBiONveTr0D-U1Qx_eKsIjseLnn9uLMUbKXmj36eGKTjUU7rMx8Ko-QrFSIZKq7BpF-DkOIEGWvhe5DYx62QonE4adTvIiJr3X6rH_I1s2xyoOO2mA46-ofARD23wRyNud0mQAC96L9A8yrKtSx97tq5MbqpUxRZDyURLse_F8FczYA3H6sBtu5u8ZSGYBtFStj5njgBukUt5pCuGwcEchCjINpzFAm4nngPNVwkLweTA8jGQz08-wZw0GArNiOlPDwsgAAGQjoqnUBBw-c3rAKFScIOLMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddac5fcdb8.mp4?token=EJ9jEvEYK1F8H1zlYZtPq5Amtko_vCYclMkFQpKU3AOQo_vhz_czW9IVBiONveTr0D-U1Qx_eKsIjseLnn9uLMUbKXmj36eGKTjUU7rMx8Ko-QrFSIZKq7BpF-DkOIEGWvhe5DYx62QonE4adTvIiJr3X6rH_I1s2xyoOO2mA46-ofARD23wRyNud0mQAC96L9A8yrKtSx97tq5MbqpUxRZDyURLse_F8FczYA3H6sBtu5u8ZSGYBtFStj5njgBukUt5pCuGwcEchCjINpzFAm4nngPNVwkLweTA8jGQz08-wZw0GArNiOlPDwsgAAGQjoqnUBBw-c3rAKFScIOLMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکی در مراسم اعطای مدال هرکاری کرد نتونست گیره مدال رو بندازه داخل و گفت میخوام یک مدل دیگه برات ببندم و مدال رو گره زد و نزدیک بود طرف رو خفه کنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/news_hut/66484" target="_blank">📅 13:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66483">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
‼️
وزیر خارجه پاکستان: مذاکرات سوئیس بدلیل مشغله کاری مسئولان ایرانی در ایام محرم به تعویق افتاد
@News_Hut</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/news_hut/66483" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66482">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd02588050.mp4?token=rrU1vM-njbgI7s9NXpEVV68a4UMuQn1zLIPPcCBSu5qTX-IaAex4uTBGKS5FwtXfA3INDzVKUl3OzstkIUr3SxT-bQfg4-gH36JePkcMPW8qG1n1m0EeA09TT00RqZ1IQ9l03dgdffI4zFTKk1iV-dM-YHKRA48JJJXJ13znEVAPJ774YgR3amgiKVA6IgxkMhfT9__7UQ4zTlamrkcldDh5tbkJyj_sLgubTjDtJ-h46TIHx4Yx-cz4vdJPjpiir6LihVn4epPgRgUSHvo4SLqlXEMCEDLtRA1o8P0nXf46MOsbIM6uvyEJmQHvKT8A9y3AjerafEz_fy64m_VR0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd02588050.mp4?token=rrU1vM-njbgI7s9NXpEVV68a4UMuQn1zLIPPcCBSu5qTX-IaAex4uTBGKS5FwtXfA3INDzVKUl3OzstkIUr3SxT-bQfg4-gH36JePkcMPW8qG1n1m0EeA09TT00RqZ1IQ9l03dgdffI4zFTKk1iV-dM-YHKRA48JJJXJ13znEVAPJ774YgR3amgiKVA6IgxkMhfT9__7UQ4zTlamrkcldDh5tbkJyj_sLgubTjDtJ-h46TIHx4Yx-cz4vdJPjpiir6LihVn4epPgRgUSHvo4SLqlXEMCEDLtRA1o8P0nXf46MOsbIM6uvyEJmQHvKT8A9y3AjerafEz_fy64m_VR0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تلاش سربازان روس برای سرنگونی پهبادها
@News_Hut</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/news_hut/66482" target="_blank">📅 13:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66481">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=ayX_scmRwe86D4WGxqApORG0AXQdFuwW4JWRwgB6F8ejpZSArqq7XZ_715xy3u4mTdOAdEaIOg7gIdoXUDCLJA59UjZ_SldSpwFYdcTUOzHQgYmpTDsPaDVxamQU7lA1r-kgQLDIuhxf2MwGED7yofVbdoc-sWeAO6EsMZNEjSjmKt5QuvBFZeOCVkRQP9ZjUQ2SW4gAx_OojEXdh7FybFveeWLMC6UIZnP6VxuF8x6pFfjifrVpiPKIX4y0rDy7AhsmD237_57tl3UVYzn94EuAIZXuc4xGX-rjXiXHZKU29SxArKSfbcX0oYH9SZhx_s2hu2GK6LrDxuiT3zyxCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d70873ad.mp4?token=ayX_scmRwe86D4WGxqApORG0AXQdFuwW4JWRwgB6F8ejpZSArqq7XZ_715xy3u4mTdOAdEaIOg7gIdoXUDCLJA59UjZ_SldSpwFYdcTUOzHQgYmpTDsPaDVxamQU7lA1r-kgQLDIuhxf2MwGED7yofVbdoc-sWeAO6EsMZNEjSjmKt5QuvBFZeOCVkRQP9ZjUQ2SW4gAx_OojEXdh7FybFveeWLMC6UIZnP6VxuF8x6pFfjifrVpiPKIX4y0rDy7AhsmD237_57tl3UVYzn94EuAIZXuc4xGX-rjXiXHZKU29SxArKSfbcX0oYH9SZhx_s2hu2GK6LrDxuiT3zyxCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتز، وزیر دفاع اسرائیل، درباره سوریه:
ما آنجا می‌جنگیم. ما به الجولانی نیاز نداریم. الجولانی، تروریست کت و شلواری، نیازی ندارد که بیاید و به ما کمک کند.
ما سوریه را خوب می‌شناسیم. او قرار نیست در لبنان به ما کمک کند. او باید در سوریه بماند، در کار ما دخالت نکند و ما را مجبور به دخالت در کار خود نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/news_hut/66481" target="_blank">📅 12:55 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66480">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=u-6TnmKW1bn8sUlOZQ0OWmewyXxD_qeuhcJuhU1zKvrlk201_ewJFKNfA7cv6eGn8LSMCLwcUKd2SnGCqwUasqmP1QzqBWLOY7UtOONgpd7Ji0EeO422h_6sB8TbOmpGjGUxtTK0kDN3I5bEpmDqp9_xnKjH8gn6AsoTUU3lbQr1Q0Sy4gJ5QNXlYAdfZfo5E3F5k_fmVQ2lD4Mt_b4gYoInyS5TLq-13O48OARIZRygFaiMA-RJZUk19wQtqhaKoAnEnUth5Bd4rE5YIkhig8iT-kLJqJ00y7ZgKbAvnoTHuC9QOdtuwkI9sQELwaOsTxb3E1V7Wyfd8EwJVFKZrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15d1aff21.mp4?token=u-6TnmKW1bn8sUlOZQ0OWmewyXxD_qeuhcJuhU1zKvrlk201_ewJFKNfA7cv6eGn8LSMCLwcUKd2SnGCqwUasqmP1QzqBWLOY7UtOONgpd7Ji0EeO422h_6sB8TbOmpGjGUxtTK0kDN3I5bEpmDqp9_xnKjH8gn6AsoTUU3lbQr1Q0Sy4gJ5QNXlYAdfZfo5E3F5k_fmVQ2lD4Mt_b4gYoInyS5TLq-13O48OARIZRygFaiMA-RJZUk19wQtqhaKoAnEnUth5Bd4rE5YIkhig8iT-kLJqJ00y7ZgKbAvnoTHuC9QOdtuwkI9sQELwaOsTxb3E1V7Wyfd8EwJVFKZrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
حملات گسترده ارتش اسرائیل به مواضع حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/66480" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=SfEg6Vj54argJz21lxQGYDKm5qoThN3VhsTjA81fiaegLqRgVY78uf76oEPHK3CTo7ObyIUX2b2YLlIzh6NrX8077D-yJMDM60lo_AtDW7t0nAJKF0_WAWt-Xskedt6ZZ1h00eizCX0VE6-_aSJYD9YBRu_3kBBqaC9FPeorx3JKeVZTtz6fp5m2xbi4QvC7HPs7M2j_Z8yCatR6G2SvOR4ooYx26n2q0jtr7V5scYCxniOA7OiarAxk3k1Q97x2FgboDY63M6USapN38P9wrP2SDRaTl7X5nXvIcxVAk-jpB-fvk2aXna8Y4qs1JrSTybqfe5lsurkHGs0I_eNGTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae8db95bdf.mp4?token=SfEg6Vj54argJz21lxQGYDKm5qoThN3VhsTjA81fiaegLqRgVY78uf76oEPHK3CTo7ObyIUX2b2YLlIzh6NrX8077D-yJMDM60lo_AtDW7t0nAJKF0_WAWt-Xskedt6ZZ1h00eizCX0VE6-_aSJYD9YBRu_3kBBqaC9FPeorx3JKeVZTtz6fp5m2xbi4QvC7HPs7M2j_Z8yCatR6G2SvOR4ooYx26n2q0jtr7V5scYCxniOA7OiarAxk3k1Q97x2FgboDY63M6USapN38P9wrP2SDRaTl7X5nXvIcxVAk-jpB-fvk2aXna8Y4qs1JrSTybqfe5lsurkHGs0I_eNGTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر دفاع اسرائیل:
ارتش اسرائیل باید در آن سوی مرز، فراتر از مرز، از کشور اسرائیل در برابر سازمان‌های جهادی در لبنان، سوریه و غزه دفاع کند.
ما از «مناطق امنیتی» حرکت نخواهیم کرد، نه در سوریه، نه در غزه و نه در لبنان.
@News_Hut</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/news_hut/66479" target="_blank">📅 12:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-ivsGm8LTQv__VzsrQP6VUZ3zIELWIn7Z0QPdFC5Wohb998WqWr61iZ_CRlIgxpEAhd8s6b-77GIpiZBwp40rYofjl2KGlTu7rZnAISOtxllqWunNunFeMwGlvjH0n9iwOVliKO2kLt4y9HE2yTwnZE5ifSzAtaKvFvtr4gYWpgIDpHdAegaevOKxhHZ8eT_gVATyn1cQvsz9M4t8ErqYkgXVOGIjKeCgmWR2cGUUd1K-FJXT90Y-3JUYQnORspA3cEeijKZZjiwB0G_Bmj4TT0IVQHz2azYcrsnPgLGpTdKI__L3XbRfptAxwV-vzr8z8aBvPRhPjmxdVjNa6i1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
گوش‌بفرمانیم، وظیفهٔ محول‌شده به ما توسط مقام معظم رهبری پیگیری تحقق شروط و بندهای تفاهم است.
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/66478" target="_blank">📅 12:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=DILODUinwVd05yzzmsx9mFNWaRx-tDRd7grFsWign4kR4yr8FC30PUSaRlBdODffrzv82Pcs1ooT_j5Ji1pt6NaOMZTejTVsI9Sv-Bjr5n--vp1uXWg8U9HRHcauLSbdEcZNXV2_Ipah4qPp614o3W8AGtlZPTCd_k_wSzUdn3z0E3_LpvWFEHpohk_PHPFSXBo45kkYgZxpvplRDQ69mk6zDi5cAsoAooEX8AwxCjxLp0VIbzZg1olqss0XoiyJ3RwMFHKb40zPE-V-L78SyWNfdarDyMqzH-gNsFdE2EoXPkFLF1hOG-Ih7sbYVD41xnkx7ul12XjsbJK8M4FxAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c84fc04d4.mp4?token=DILODUinwVd05yzzmsx9mFNWaRx-tDRd7grFsWign4kR4yr8FC30PUSaRlBdODffrzv82Pcs1ooT_j5Ji1pt6NaOMZTejTVsI9Sv-Bjr5n--vp1uXWg8U9HRHcauLSbdEcZNXV2_Ipah4qPp614o3W8AGtlZPTCd_k_wSzUdn3z0E3_LpvWFEHpohk_PHPFSXBo45kkYgZxpvplRDQ69mk6zDi5cAsoAooEX8AwxCjxLp0VIbzZg1olqss0XoiyJ3RwMFHKb40zPE-V-L78SyWNfdarDyMqzH-gNsFdE2EoXPkFLF1hOG-Ih7sbYVD41xnkx7ul12XjsbJK8M4FxAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
بمباران شدید نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/66477" target="_blank">📅 12:23 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66476">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=I6m3E8-K1TF1VrwtsDBBdlwF2dfxfyiumNeQZzcha_iEFLpMAVuE9ZfbPZDxbFj8IaqZzR_BCERND5IBwtudqLlnnTeb4pypCyTOKP23d12IiDC9IsZjfNPJKaTODOd9GfiMPJkSugNbxq8aTD23zyUlhUCNOMZEcxSJ87E5XIA6mwZG0AR5952FjAEFiOJ4ailreSfKAHHweMe8KeKhP--_sRPyYOTpOC_XJH3nDRjAT81jaL40T8fST-SlPSGhxm69CxYmcDPb4-Cjs8L4TEPj1nExXtNU-XRPpUwrqTlOjny_3xUjKyW6pPUmn5qtWTN5HNNwu4fsgO7B2vfo3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cbfc5535.mp4?token=I6m3E8-K1TF1VrwtsDBBdlwF2dfxfyiumNeQZzcha_iEFLpMAVuE9ZfbPZDxbFj8IaqZzR_BCERND5IBwtudqLlnnTeb4pypCyTOKP23d12IiDC9IsZjfNPJKaTODOd9GfiMPJkSugNbxq8aTD23zyUlhUCNOMZEcxSJ87E5XIA6mwZG0AR5952FjAEFiOJ4ailreSfKAHHweMe8KeKhP--_sRPyYOTpOC_XJH3nDRjAT81jaL40T8fST-SlPSGhxm69CxYmcDPb4-Cjs8L4TEPj1nExXtNU-XRPpUwrqTlOjny_3xUjKyW6pPUmn5qtWTN5HNNwu4fsgO7B2vfo3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
اسرائیل کاتس، وزیر جنگ اسرائیل:«حتی اگر ترامپ چیز دیگری بگوید، هیچ‌کس نمی‌تواند به ما بگوید چه کار کنیم و ما قبلاً این را ثابت کرده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/66476" target="_blank">📅 12:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66474">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=Ad8G5iQRHfKX0fBQp1ZT12cQbYywwG9tHvrM3EksFGSd-tWsc4wwAKENTT5YhwwM8tACzaUe1aNUAIagXWiva5R2rdoKtg4pcry_8UpHU3bjxMBaLjuh6gHzYpvNDGejLNCTtA7bfQZR94SXkj3wUZ8eupy1gAWeuLZ8nDhTGIaxXgGgs9pC-0z4RLFpnnNgVAUzN151VHJ8Je80QcC6Bx9S1vDt7R_keP0D_f8vI6rE9Qz-9V4ShTeERgn8PM4rF8shzgKXO-f0ppi5mNRjenASlG-pdhL-aNMxsiD3Hd7neWCjtXE9pGP3uGK1kkLijETujv6pICqQMsAMYa6w2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba86fa7681.mp4?token=Ad8G5iQRHfKX0fBQp1ZT12cQbYywwG9tHvrM3EksFGSd-tWsc4wwAKENTT5YhwwM8tACzaUe1aNUAIagXWiva5R2rdoKtg4pcry_8UpHU3bjxMBaLjuh6gHzYpvNDGejLNCTtA7bfQZR94SXkj3wUZ8eupy1gAWeuLZ8nDhTGIaxXgGgs9pC-0z4RLFpnnNgVAUzN151VHJ8Je80QcC6Bx9S1vDt7R_keP0D_f8vI6rE9Qz-9V4ShTeERgn8PM4rF8shzgKXO-f0ppi5mNRjenASlG-pdhL-aNMxsiD3Hd7neWCjtXE9pGP3uGK1kkLijETujv6pICqQMsAMYa6w2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی شبا میری اعتراضات و روزا میری راهپیمایی:
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/66474" target="_blank">📅 12:04 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66473">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=eTxN4BmYeEv6UYfGotpkjaiDXAffNR0tS4102689Wdx_ZN8qG2tfn3O76GY_zN5Ukbc9CpxZmw9_RouCTMUtR-TTxlMS4BzUD96EZ-dockFHkaBT-YX9Jz2BNeGbtgDyKBS7wHCL2KMUnMVFcqaoalDo4WURhGinkWyyb_9ZJPs2vfvJbCDf5WukxQvCTP5KbDjYwmgMa7sE9ibKhod0yr_kqbkTkCWan3Wg3zrXHrl0XNY1RicC0TcDOK8Ev_YXxJDXnyKEH62III7UMVO6cTKkFVI8QCIeCv2wmdPK7peH_G8NChmDHybRtKFdCn2F0DpuLvAfCEbxH-Jwl50qDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0be5a6ce.mp4?token=eTxN4BmYeEv6UYfGotpkjaiDXAffNR0tS4102689Wdx_ZN8qG2tfn3O76GY_zN5Ukbc9CpxZmw9_RouCTMUtR-TTxlMS4BzUD96EZ-dockFHkaBT-YX9Jz2BNeGbtgDyKBS7wHCL2KMUnMVFcqaoalDo4WURhGinkWyyb_9ZJPs2vfvJbCDf5WukxQvCTP5KbDjYwmgMa7sE9ibKhod0yr_kqbkTkCWan3Wg3zrXHrl0XNY1RicC0TcDOK8Ev_YXxJDXnyKEH62III7UMVO6cTKkFVI8QCIeCv2wmdPK7peH_G8NChmDHybRtKFdCn2F0DpuLvAfCEbxH-Jwl50qDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نبوغ اوکراینی ها در شکار پهباد
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/66473" target="_blank">📅 11:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66469">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMn5mGkLwO0LZSNCD-q9sOL0Csh-GWIURAcyg0xwUrJoTBGebMqPusYpr4DhfoesZ0Ernh-SAmEhHmqTXhd1AwsYnOMIgTj62beYgJsRwIXASdpP9GEN5Ko1jzkWXVQkBBNwPitnQb6vEt3F_EdVos06Y_YvXcx24Sl_bRJuic31uWW-LzFaTlcm6XCEW0QlFuC6BcO8ORJDPuvJe9Y544ETBaoA0Ka2cqUe0ghOEwt_n67EEl4zhKY1_ATrbGLinRUSyM9sWNcWZH7O6cgzc5iPER0IrAk4Hq7FXn5mnUQda0ve8N-ngouZ-3_ZCDQbxfGik0tB-7kAWRQ_ba4qtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t93V6j_buzmEiid7DXcfqKo5sKkLWADHoiIdUYtz0NcOWLlJQDHTjMBSu_BdYaE2-3N-EWD3ZnqEkmC8ecgnQfGVBvlXyjfNWOy5JiJNap4bNC1ws8aNukWiZKbJbOkrPVfgIwQLGjRW9d5nzW-6eHqZvXAmDbdlmcX0V2AVJqSMeslpSKxassJeMsCfybHxdTMBDiSDUNG_gRmXLS-93Zja4CVWBCRRIXeVaUEdqd9kH4Yxpt2GHqGkJcK-mgIfJvQw7I_2SMjNIl-A6lVGHIM7Z6YXO47LxkXcDaXBeaIUJJIJX42OjqRZ9ilRic3oAHwo5gHtPYnwQin2BjK_xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUDTtfORbLwN1teAYxyB1LCQr6u876uFJNq6zKAvI2Jo7A1B23TBYVfDe3OS7ToMmAdLK9uefgMGDTwqb7viFdXQ66DWP34czze7NcK6PTK24lAI6LMB1eCH8JqEiZNQfCPZfnNjbLNepuunpUFkpIyl9GAwYGSPjc1xkDIZsRGDqhkFkW4ajqVQ66AltjlAyWNBe14wpgwBolMvjIKul59UVXcWg5nG-YrMbjXmNr5MkQRfuAz5TrOKvQJcJslSO9wkCcXerIg4P8jh3xNIdwaAZflA1Qm7V0MJiFK6Ap0TYTjlhRGQzTF8NGu3H4hdhz139zA4yBtxDMbbFJWB7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=to5gklNbuFoWoFykwN43rqBNvMNf9m2RVsD4xMoIv1GcwkuQQjfGfA2RnNTiV6dHrnCvdX5GG4c16NKsbnlroiLvjcF58B0GV27wv-yJvpBVvbsUaft5Vmgsh19W7FkL6BHb9i-tGGm56GTFf0dJWxIFpGpIG9xEvHQv9y09lHcB0alHQBm7VtyomqQRUZhQvUg-YUF94zEMokQDrwm1xbKxIP4G1kIxYz5cmKmS7F_inRrUsrfYZQQeD-xYkFTwioTP7xlftPuoTAmgT_3_W8lyOLpkyvi-rXRCt2ekAsh9B8MfjcOA_yY1ei2D_BahzdnHs_Bwqi-ZgVhgYKq-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cb0e601ac.mp4?token=to5gklNbuFoWoFykwN43rqBNvMNf9m2RVsD4xMoIv1GcwkuQQjfGfA2RnNTiV6dHrnCvdX5GG4c16NKsbnlroiLvjcF58B0GV27wv-yJvpBVvbsUaft5Vmgsh19W7FkL6BHb9i-tGGm56GTFf0dJWxIFpGpIG9xEvHQv9y09lHcB0alHQBm7VtyomqQRUZhQvUg-YUF94zEMokQDrwm1xbKxIP4G1kIxYz5cmKmS7F_inRrUsrfYZQQeD-xYkFTwioTP7xlftPuoTAmgT_3_W8lyOLpkyvi-rXRCt2ekAsh9B8MfjcOA_yY1ei2D_BahzdnHs_Bwqi-ZgVhgYKq-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به نقاط مختلف در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/66469" target="_blank">📅 11:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66468">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SynygNO0wOdv8Tj7qtrj2piCE3f43jXb991QztbkXbAnRwhG8dgM9Zqc3aG0LLlf6aP9W5ks2IXnLwCnKfRFN9N41NH7i3LPKBg3cEVLp_gy4Cb2PvGjP6_Ig4tt76RTqnr6pVjGDNuinqAag3cj4EeJ-8CSTyrRrbXXH1Vot2HslrahvLRA1dUYbVaVxyyVhSjax8xUGYhA7Ft5iBSRLBMy5FKa3V7FdhYwKtatEesg78hzqEx_VKP0sQOUUL3eHOcChBARRefwxM0xCVXFKCa0G-_6Vo8Zd2ndJ7u31LnwwErwAOLq-o5ee_9nlKuTj8O8dZbfRKt7Nhhral6h-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وضعیت ‏مسکو، روز ۱۵۷۶م عملیات نظامی ‌ویژه ۳ روزه پوتین در اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66468" target="_blank">📅 10:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66467">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7be955089.mp4?token=DB5AfxljcQNvQqVBoaZfZQM-1M6tSU28LPYlcZfb5VzkZrRUiWE9AE1DaUQjl3bAhblGva-cnxg_8wFxrTq4RjMatTeZfcwx7lCddbrqjO0isXNw47F7p1ej1pItdipOM-Bja5EL508ulDj1nXw7IMEQ0wv7uLCJGubAZryaJcRPgju6pmEB_TjhtiLf0CuBXR8nld25uUH_hIv1mCbbAFrHKjef-5J9dSsPQpdOkW-sugR1R7lUa-Z82AuwFTp6gw1i-q1Qj9mxX9ij1nXTuaZ_vlP8D4fGgnhybfHqePqLakOAJHDtGK1CFqrpcEHfXmtUd1jscy4mBNt22tPhig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7be955089.mp4?token=DB5AfxljcQNvQqVBoaZfZQM-1M6tSU28LPYlcZfb5VzkZrRUiWE9AE1DaUQjl3bAhblGva-cnxg_8wFxrTq4RjMatTeZfcwx7lCddbrqjO0isXNw47F7p1ej1pItdipOM-Bja5EL508ulDj1nXw7IMEQ0wv7uLCJGubAZryaJcRPgju6pmEB_TjhtiLf0CuBXR8nld25uUH_hIv1mCbbAFrHKjef-5J9dSsPQpdOkW-sugR1R7lUa-Z82AuwFTp6gw1i-q1Qj9mxX9ij1nXTuaZ_vlP8D4fGgnhybfHqePqLakOAJHDtGK1CFqrpcEHfXmtUd1jscy4mBNt22tPhig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری: شما گفته بودید که فقط تسلیم بی‌قیدوشرط را می‌خواهید. اما این تفاهم‌نامه شبیه تسلیم بی‌قیدوشرط به نظر نمی‌رسد.
ترامپ: خب، در واقع احتمالا تسلیم بی‌قیدوشرط است.
مجری: واقعا؟
ترامپ: من این‌طور فکر می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66467" target="_blank">📅 10:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66466">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=nmSS7UlnlS63COFEw9HslGpZYEqnSNDWHUsYdpiq_O7QsF9Q-bE2KnGiB3aEEO8WvqQrAOHuEkUpClbt8mNfyuKL9L9vV4v8iysRuv1yrXhhHJDTUxWhiygU8BjSAvwOJHDL4MYdwgHCvw6zVUKdV9p9teElUU_e0gXgAVZTwV7vYo_ZZ3zDmPiWrIWy_ZWwHMrMiEWro030Amfi6i9zopB4SuLr4n2uOmfLt9pZNPS27hFCw-85YcedT466bpo1xJDwjKiBl2h2Br286x5jiS4_ZIptY6f3LyVrsyKlzN3vnaBx7XgPdHxGCJipEdLMG0gUnMFMZpK3Rc25U0YkuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/040ce8f378.mp4?token=nmSS7UlnlS63COFEw9HslGpZYEqnSNDWHUsYdpiq_O7QsF9Q-bE2KnGiB3aEEO8WvqQrAOHuEkUpClbt8mNfyuKL9L9vV4v8iysRuv1yrXhhHJDTUxWhiygU8BjSAvwOJHDL4MYdwgHCvw6zVUKdV9p9teElUU_e0gXgAVZTwV7vYo_ZZ3zDmPiWrIWy_ZWwHMrMiEWro030Amfi6i9zopB4SuLr4n2uOmfLt9pZNPS27hFCw-85YcedT466bpo1xJDwjKiBl2h2Br286x5jiS4_ZIptY6f3LyVrsyKlzN3vnaBx7XgPdHxGCJipEdLMG0gUnMFMZpK3Rc25U0YkuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ به شیخ محمد بن زاید:
وقتی انقدر ثروتمند باشی، میتونی انقدر آروم صحبت کنی.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66466" target="_blank">📅 10:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66465">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=SudlrdPwSoLyQS5L7S6F_Mu7EAjrVD6Ceicu1vKonirdYcHblkKOBDWUE0u2FaHmb7Jzzp-1kwmo70avuN5I8wCFWiIN_WXTCc-mj37Wo6sXGFO0QDyywMeIWbW0FPNPamZ80RcWCwdXW8SCi7cnAMmEGdfw-hO1_4AonDi3zIzIqPFQOAyy0srzGruzL45BCW_iznAbB1adlpvjtpOsKfKNtjsPF6SqcFedXhhPYH9wdHNsDqslBfplGlJxW9cbKUn4cQdlB3L5-9t6ZXUJ0fJ5xeS4Ctx7HrLGmfOHkbCHzQIw0Z50ovWnBjFFCIGF8eQ_nLcjozUZ6suRUdb9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/635e862fe5.mp4?token=SudlrdPwSoLyQS5L7S6F_Mu7EAjrVD6Ceicu1vKonirdYcHblkKOBDWUE0u2FaHmb7Jzzp-1kwmo70avuN5I8wCFWiIN_WXTCc-mj37Wo6sXGFO0QDyywMeIWbW0FPNPamZ80RcWCwdXW8SCi7cnAMmEGdfw-hO1_4AonDi3zIzIqPFQOAyy0srzGruzL45BCW_iznAbB1adlpvjtpOsKfKNtjsPF6SqcFedXhhPYH9wdHNsDqslBfplGlJxW9cbKUn4cQdlB3L5-9t6ZXUJ0fJ5xeS4Ctx7HrLGmfOHkbCHzQIw0Z50ovWnBjFFCIGF8eQ_nLcjozUZ6suRUdb9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختران حاج گاسم
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/66465" target="_blank">📅 09:34 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66461">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/loJpZXIsV4RbvFgBTTWfC0Cq-OLfBWRZr-hdGo2A0a_6bkLp9mZCmkAUmYAZiKUHiIcaLSapjOEk_nwn4qLicPRXmGjYgGHTYsRG-68_jCpfkGzzu_1qD2E8O9YkAPLS0Gy2XUj1uiMkgA5_XIEX6-LfUI47CRdlxeVMy0ipHlmR6WxXm3nQO4DkIECP1ugo_fW7BF2p8sb8qj2mxflWZYwNjryFAc9p8vKvrb37fzSGASXYGdo8sIYHY0jE-sNTORyotIrswLwrBfkmLejCMnNQSEDSto74EAjtzaN0ynX-edk_kGOm0KRDMjZMMzysr5O3p2qtgM-nKOeI1XIZsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=OdtSxBVIUNqBTfTiR-Cd4SZo_MB2ZMWIN8bHfp40yYrpGDvWFOXKU_u_UEq-NVFVF6o-KMg7tyliNjswR3wgLW-HJbCFIiZJwk04UCe4Zx30mSAVRraCba-B99VBmvJ7SlVcEX-2vWI_vOtqwij2hUeyYAPlUR2fgJATAaN9FmWb_vIFzNEPssV4y3mA76wZs94cDpSZA5U9RRiIMc12x2HaenTluYfYdYgMLQwmAO9FNYQkit4FglaD922v6MDfFef8rsXSicAH2mdWAz8UCwjDrLW_tD-J9fnbzaFWS1ueKaCrxiBsKjU7GV0tGuLpt47Pi4jSDd_HFSLgfBeBVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a17f4667.mp4?token=OdtSxBVIUNqBTfTiR-Cd4SZo_MB2ZMWIN8bHfp40yYrpGDvWFOXKU_u_UEq-NVFVF6o-KMg7tyliNjswR3wgLW-HJbCFIiZJwk04UCe4Zx30mSAVRraCba-B99VBmvJ7SlVcEX-2vWI_vOtqwij2hUeyYAPlUR2fgJATAaN9FmWb_vIFzNEPssV4y3mA76wZs94cDpSZA5U9RRiIMc12x2HaenTluYfYdYgMLQwmAO9FNYQkit4FglaD922v6MDfFef8rsXSicAH2mdWAz8UCwjDrLW_tD-J9fnbzaFWS1ueKaCrxiBsKjU7GV0tGuLpt47Pi4jSDd_HFSLgfBeBVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات شبانه ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66461" target="_blank">📅 09:02 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66460">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66460" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66459">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IQyHMgKs7t0zIr58Ye0dJhONHaMPQJgbNJhpJQX-zPiPooZxGyR63EVKlNk7Td9pmumd_sXWY-KQZCc2gjg9_YD2g1och1f-EUNsXpsci7EjpfOx4UNTXRxZ79ZAFM4SXjEVXL46b2KesAlnsnQvUssuB6uaJMtbKeokEBREQ1N1aMJxFkUQ5uXNf2cdsaoc0cZFZ1-2_7OJJ3UzrgTxTt1lNsn-a2QCV3ma9EzDHVraAUVTOjOFLej7SDndfxf0EGXSX-BcHfqpcjR-FaevaUw8Y0W529aGL8mBpDVQXCLmHpLMcKeCYqPfQwYjuQwfoPOcBCvXLD26NwduRwFsAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66459" target="_blank">📅 01:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66458">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
‏به گزارش المیادین، هیات مذاکره‌کننده جمهوری اسلامی در پی تداوم حملات اسرائیل به جنوب لبنان، سفر خود به سوئیس را تعلیق کرده است
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66458" target="_blank">📅 00:42 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66457">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=I-27YFr5Dz-bFc-M1diPoqJ4r9Mm8xUM7F0OuhWFKLhuMmrQpZBuSYc_h3mzdB1E5KhCWgRAOXDZy4iATWgdc7IF__f8b3iiABi5GixZHIgYmN-DUBjxU2xPICzULlsgs-753J6KugoeyzbGFxCzL6zaV4zrQ4mYyqQxkTFZYkWNMF3GTakaOmAUUhDjlZPV9AX1xfUHYIqZ_9gbqY5xptawt3YyZ18gxAEC_7z-TPDAXnCpeVNL7doV7-X9ct0D5SH3jERuiSiGGZwU8ExaDTliJfsvo7yWPGVmT3a9MR9dxoPVroidQL8SOWLZ56Tl-MQa6-cOyEYvrxWnpw_mBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a4159b30.mp4?token=I-27YFr5Dz-bFc-M1diPoqJ4r9Mm8xUM7F0OuhWFKLhuMmrQpZBuSYc_h3mzdB1E5KhCWgRAOXDZy4iATWgdc7IF__f8b3iiABi5GixZHIgYmN-DUBjxU2xPICzULlsgs-753J6KugoeyzbGFxCzL6zaV4zrQ4mYyqQxkTFZYkWNMF3GTakaOmAUUhDjlZPV9AX1xfUHYIqZ_9gbqY5xptawt3YyZ18gxAEC_7z-TPDAXnCpeVNL7doV7-X9ct0D5SH3jERuiSiGGZwU8ExaDTliJfsvo7yWPGVmT3a9MR9dxoPVroidQL8SOWLZ56Tl-MQa6-cOyEYvrxWnpw_mBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آیا در جامعه اسرائیل افرادی هستند که بخواهند ایران را به لیبی تبدیل کنند، یعنی یک دولت شکست‌خورده با ۹۰ میلیون جمعیت؟ احتمالا بله.
اما نمی‌دانم که بی‌بی (نتانیاهو) چنین چیزی بخواهد.
من شخصا هیچ‌وقت چنین گفت‌وگویی با او نداشته‌ام. گفت‌وگوی جالبی هم می‌تواند باشد.
اما همین را الان می‌گویم: آیا تبدیل شدن ایران به یک «لیبی ایرانی» برای ایالات متحده آمریکا خوب است؟ قطعا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66457" target="_blank">📅 00:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66456">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=mZaG-04wNdO_m41zokPHQnqO3qY-fyYdzMHJhGEVQCS9J2ir7Dp4yGNt_AhxvX2rKdnyYJ7PZ-EKqYI2rxeka4IbYlmSxo8NbgPdutGz0B3uXkiwicj2dOTaQfGLP0ey6qS0yC1slRcRBiEJcfv11Qdi47z1pqi1AJ8s2yszM30irmwtGxAu-6_eIMIMKtXd8bixM08ruwpZUMbR8Jo1XFXbtGmbL8ZjA7RnKbrYbYiG7VCR4SyuePY21yndpAZLhWM-njNzmywKCDObuioiJMYUqEJr6LL-AaP1H-VuqSnkZ_b8g4JlERk5nlG_CZRm_TpfwnnLNMINDxk7HzCNUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47cfe42200.mp4?token=mZaG-04wNdO_m41zokPHQnqO3qY-fyYdzMHJhGEVQCS9J2ir7Dp4yGNt_AhxvX2rKdnyYJ7PZ-EKqYI2rxeka4IbYlmSxo8NbgPdutGz0B3uXkiwicj2dOTaQfGLP0ey6qS0yC1slRcRBiEJcfv11Qdi47z1pqi1AJ8s2yszM30irmwtGxAu-6_eIMIMKtXd8bixM08ruwpZUMbR8Jo1XFXbtGmbL8ZjA7RnKbrYbYiG7VCR4SyuePY21yndpAZLhWM-njNzmywKCDObuioiJMYUqEJr6LL-AaP1H-VuqSnkZ_b8g4JlERk5nlG_CZRm_TpfwnnLNMINDxk7HzCNUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس این انتقام ما چیشد؟
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66456" target="_blank">📅 23:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66455">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=W-q82WBLp6Pj7Zs85aubnjIHbflDwaiYoLvUfwi9l_Sm2lYCJoMCGdA7ykMV1-zFCYXkpjTu6dOrTyolMnSrw8eM1VSFwKuYbGDlqN3f8w0M10eoPD6klefgkHefxsAU273b0lU--NXNm9pOLgDq2axFIJhd2p-WAWa8D0YFpxXSNTdXXsLhnVG48lZvMtXLId7QFP9_JarfTh3v1lPyXZKJYaWg2QcTf3inFY18tw0ArwuIfUTIdOmeQqLhmq6ZLf8NTd97eQZNDkPpz5QQzN7BfilFsqRog5U1TVpBpXGPvU6AojEw08cJk136mYmWQ3mwKyRjIAtZv4CYbcJgpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad18edc1d.mp4?token=W-q82WBLp6Pj7Zs85aubnjIHbflDwaiYoLvUfwi9l_Sm2lYCJoMCGdA7ykMV1-zFCYXkpjTu6dOrTyolMnSrw8eM1VSFwKuYbGDlqN3f8w0M10eoPD6klefgkHefxsAU273b0lU--NXNm9pOLgDq2axFIJhd2p-WAWa8D0YFpxXSNTdXXsLhnVG48lZvMtXLId7QFP9_JarfTh3v1lPyXZKJYaWg2QcTf3inFY18tw0ArwuIfUTIdOmeQqLhmq6ZLf8NTd97eQZNDkPpz5QQzN7BfilFsqRog5U1TVpBpXGPvU6AojEw08cJk136mYmWQ3mwKyRjIAtZv4CYbcJgpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
آنچه من به برخی از منتقدان این توافق که شنیده‌ام می‌گویم این است که آن‌ها می‌گویند: “خب، ایران این همه منفعت به دست خواهد آورد.”
من دوباره همان چیزی را که قبلاً گفته‌ام تکرار می‌کنم و احتمالاً مجبور خواهم بود چندین بار دیگر هم تکرارش کنم: ایران دقیقاً چه منفعتی به دست می‌آورد که قبلاً نداشت؟ پاسخ این است: هیچ چیز.
آن‌ها هیچ چیزی به دست نمی‌آورند مگر اینکه رفتارشان را تغییر دهند. اگر رفتارشان را تغییر دهند، آن چیزی است که باید از آن استقبال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66455" target="_blank">📅 23:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66453">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
یسرائیل کاتز به کانال ۱۴:
ارتش اسرائیل دستورهایی دریافت کرده است تا در صورت لزوم، برای عملیات دیگری در ایران آماده شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66453" target="_blank">📅 22:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66452">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTVlotVuiXNnxDVvblT8Z3lNDwxnuRR8YoKA1pVLu-80osZ58mkvU8KOnXECqg_lEPTdgLqM8Hho38fyIXRYL5FubKwALcAK__IAKW3ovztCyTkeNBqEFSkxhmNJsFLHCpLX0VxlZyr7SSmTKz079_nq1VYfwIxLN37Q4i5O9KHncIbr3dvIglo0hI9PjZOUge4m48BogmZXEuVIleGoLBQBy5kJsa7Vwooqze713Sl8nssycvZuOIGsjLid7fBW7IOe6oRxvdT6pPlkpuVeCIOPx9GcwKiSkZK8zXsVLOdVrTozYb6KpM4P0lGqkqUptSXrLeMnTY5y4XrQ26abjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ در تروث سوشال:
ایالات متحده به صلح متعهد است و ما همه را در منطقه خاورمیانه تشویق می‌کنیم که به تعهد خود برای پیشبرد مذاکرات ما به زیبایی پایبند باشند. بازارها از آنچه که با کاهش قیمت نفت و افزایش سهام اتفاق می‌افتد، لذت می‌برند. ما انتظار آتش‌بس کامل در همه جبهه‌ها، از جمله لبنان، حزب‌الله و اسرائیل را داریم. از توجه شما به این موضوع متشکریم!
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66452" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66451">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هات نیوز | HotNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/news_hut/66451" target="_blank">📅 21:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66450">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66450" target="_blank">📅 21:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66449">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این پیام یعنی پایان پزشکیان و جریان اصلاح‌طلب در ایران، و آغاز حکومت نظامیان به سردستگی قالیباف #hjAly‌</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66449" target="_blank">📅 21:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66448">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66448" target="_blank">📅 21:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66447">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuKqE4XgAnVheHTz-hhBx-4qDOtttEy6SXgZOt99X_34CFsM0kxfgD6eaFpE5DdLUfHFNlTqtvYysL3HCVOQ3qqDv-Z11ODNpNCxIOybB_5umXsB_NXGmcUmvzPsFrJaSK5ITg_y_FfQl8724qr3vemeq-L1AQ1sJn5Oot9DaPxTxUECXNjyIyaZWrSG9yJhkhMKpRmT9gpTan4e-sp1Fvm6ugVyJep-TMnqd-Q_7PcDdKsAUM58SUvAaM8MXKaRUG-CoZ_R8jmTidCnuMZ4mcVQFsAJEOHPK58XyHt0vlPI-I2zU029RG9ho-L0izL5EMBUnEKCNdkVqapENdA4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
پیام جدید مجتبی خامنه ای درباره تفاهم‌نامه:من مخالف بودم اما چون بقیه تصمیم گرفته بودن منم موافقت کردم
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66447" target="_blank">📅 21:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66446">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJqKl6GDOaBqx-Vm_1tmwk8JyBykseYXOQIG4SZRF83vpN5-yOxjV_v6mkf2QI2FgXpkpqJ5KsYAmeH0d_lXIBzYwN5JqDQw95Z-OWCySeKURzy54jshuHCheG7lmhbOOCMGOeiHTuJ-Sn9aWxFO5-sdIEuNLtWd1UYOYPzX_t8RAEPTbASPbAzHzClxRUUdKz4qQYsUB1DN9mbSvliR_1T-Z1EB8WVuUi7a3R2gvZe30N2G6FxeVk2H97FnF3OSRiKk0Lp7_XWLm9Axk4URU7nhmz3QTnl9ssVvhWy-h0QYt9a3rBbWgckoHcm7oadRpFz5YBOKlnO4Qc7SMbzaAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ: آمریکا هیچ پولی به ایران نمی‌دهد. اخبار پرداخت 300 میلیارد دلار به ایران فیک است. تمام آنچه برای آمریکا وجود دارد، موفقیت، کاهش قیمت نفت و پیروزی است. وضعیت بازار سهام را بررسی کنید. پروپاگاندای دموکرات‌ها در کار است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66446" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66445">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‏
🚨
🚨
🚨
⭕️
سنتکام اعلام کرد، نیروهای آمریکایی محاصره اعمال‌شده بر تمامی ترددهای دریایی ورودی و خروجی به بنادر و مناطق ساحلی ایران را لغو کرده‌اند
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66445" target="_blank">📅 20:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66444">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=s_h0ZQe4QeuSVgFmvQ1KT940J64SJuhnrTA7RWtXqSnO9klua-pT0oo17XDPPaS9EqbxruY1clWIrWbmQU7I7v5SoCzNOTySS5SW2gO5EIFGMM8MozmOJxdyJuaNSHzxSjWgFRocGFp7FBmMt4AAjApvGBQCRDRmg4taJYPtuQCO_Uk9_Qy-PGIpptyBDZ_WkdUrb8o2UOK_tWGFWzg63bOfDKVz5FqIgzk8kgfZTVJCJ76EkNLJYmJRR6xrci2rHRaZH8wTmJEplfNumT-qQgHKgqAoERbePlN4BL1F59vfn6Sx1yUZ-jq6nWfzWAxhWhY_USm9ojkPyRHmapdR8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f51df7dfe.mp4?token=s_h0ZQe4QeuSVgFmvQ1KT940J64SJuhnrTA7RWtXqSnO9klua-pT0oo17XDPPaS9EqbxruY1clWIrWbmQU7I7v5SoCzNOTySS5SW2gO5EIFGMM8MozmOJxdyJuaNSHzxSjWgFRocGFp7FBmMt4AAjApvGBQCRDRmg4taJYPtuQCO_Uk9_Qy-PGIpptyBDZ_WkdUrb8o2UOK_tWGFWzg63bOfDKVz5FqIgzk8kgfZTVJCJ76EkNLJYmJRR6xrci2rHRaZH8wTmJEplfNumT-qQgHKgqAoERbePlN4BL1F59vfn6Sx1yUZ-jq6nWfzWAxhWhY_USm9ojkPyRHmapdR8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس در مورد اسرائیل:
در طول سه ماه گذشته، دو سوم سلاح‌های دفاعی که از اسرائیل محافظت کرده‌اند، توسط آمریکایی‌ها ساخته شده و با پول مالیات آمریکایی‌ها هزینه شده‌اند.
مشکل اسرائیل دونالد جی ترامپ نیست و هر کسی در اسرائیل که فکر می‌کند بزرگترین مشکلش رئیس جمهور ایالات متحده است، باید از خواب بیدار شود و واقعیت وضعیتی را که کشور در آن قرار دارد، ببیند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66444" target="_blank">📅 20:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66443">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=T7jda0zU4YP7dW746saTMccGSFuhT3XceqNyNR2Wc8zmRYo5SMASxgYZrUHki4bZOCnPTpuO_DF6FGQS-v_ZlwJtjD27iC5fS1pmmpva71g_Invwz4ODMGZmkO4cOZ6sCr2mFanL3yNtZUQ7ZtZ9SryE8X-uof1S0Vi_KTwsar7gKzqGC7Ek1LfNzFN-Efoo1MndNusve4OYeq0jXtiExmPGFqAulZgtjMREvGu0mt7gfKefaPvl65o2rvg2LPX6H-cgXgKTPZjuGqbx-Lzj8DnT7LsWAg-a8N49okPh5l3_YaL2Y4TfqGxdkw1tFNq3z6266_z6ReTH6Lt_qasxNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab365474cc.mp4?token=T7jda0zU4YP7dW746saTMccGSFuhT3XceqNyNR2Wc8zmRYo5SMASxgYZrUHki4bZOCnPTpuO_DF6FGQS-v_ZlwJtjD27iC5fS1pmmpva71g_Invwz4ODMGZmkO4cOZ6sCr2mFanL3yNtZUQ7ZtZ9SryE8X-uof1S0Vi_KTwsar7gKzqGC7Ek1LfNzFN-Efoo1MndNusve4OYeq0jXtiExmPGFqAulZgtjMREvGu0mt7gfKefaPvl65o2rvg2LPX6H-cgXgKTPZjuGqbx-Lzj8DnT7LsWAg-a8N49okPh5l3_YaL2Y4TfqGxdkw1tFNq3z6266_z6ReTH6Lt_qasxNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏جی دی ونس درباره ایران:
آنچه واقعاً اینجا اتفاق افتاد این بود که ما روز یکشنبه تفاهم‌نامه را امضا کردیم. این توافق‌نامه مفاد توافق‌نامه را تثبیت کرد.
چیزی که ایرانی‌ها پیش ما آمدند و گفتند این بود: «ما دوست داریم متن را تا جمعه منتشر نکنیم.» من واقعاً متوجه این موضوع نشدم - می‌خواستم متن را فوراً منتشر کنیم. اما برای اینکه با آنها کنار بیاییم، گفتیم: «مطمئناً، باشه، تا جمعه صبر می‌کنیم.»
و سپس آنچه در روزهای دوشنبه و سه‌شنبه، در حالی که رئیس جمهور در اجلاس گروه 7 بود، اتفاق افتاد این بود که شاید رهبران خارجی با ایرانی‌ها صحبت می‌کردند و آنها را به انجام این کار تشویق می‌کردند.
ما قطعاً به آنها می‌گفتیم: «ما تمایل شما را برای منتشر نشدن متن تا جمعه درک می‌کنیم، اما می‌دانید، ما در یک سیستم دموکراتیک زندگی می‌کنیم. مردم آمریکا می‌خواهند متن این توافق‌نامه را ببینند. ما مطمئناً دوست داریم هر چه زودتر آن را منتشر کنیم.»
و بنابراین آنها به این نتیجه رسیدند که رئیس جمهورشان آن را امضا کند، رئیس جمهور ما آن را امضا کند، و مهمتر از آن، شعار را تکرار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66443" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66442">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66442" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66441">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCXVpnwcva3sxycyN7Gsj5-4DaLzVssbgf4EoamQ8d7ieER0EQOdj5CHdWpATYYDLBvvL-5JpD-PEx4k-uKaNVQWqT35x1M13iFphk3whPF5VGf_8C7fWJ5tLu-Kn6SDte8mq3KWbkdvyuIblWnOf-hIxAqlMXG74CuwwBZphFwjlNmpWSoJTNC_KFmLJUe-sDbdCYucAS52MFDyJWvr8VznyGEMX_aJVRavgXMBvdiDKakXFrOI9j9ySwuCAqMcASIoM6Wz3um6WxNllf4y94D9zLiPVzkTULRQNWl7rinL_v5woCJ9xzVFYVZJHI4TR66uABOEKG6QQD6BdKIIcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/66441" target="_blank">📅 20:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66440">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=ll0RromCfnk1GaE_uELmZ3_LPQ-9etpyJvDHXevhsqg_Ti7ZiDXmOnSSooPyvLD1JzLHF7geHd5wPZ5Nd1SKZmAtR2N-6hAi-ZlozDca8jbe02dy16urOH5oAHuAG3B3YDlfpQiHNaiIAkVLYPsUyKQrquJqMKwz7CU8ISJm9Hc8lKr4i9RDzax7TcXF-ImdekRl91mVsofllGgSAaoGVcky-qC4VnPgZwhhny_YW6Bc_-N0kdYlSti5GG3K5DQefLpt2yO1ACSLZr62JWNqycBXqOthBTFKw0zBxt0QMFPIGpnaLWh8dMFgRjLYq3g-BioKux_ruTo44T7w8FormA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b31dd3b8.mp4?token=ll0RromCfnk1GaE_uELmZ3_LPQ-9etpyJvDHXevhsqg_Ti7ZiDXmOnSSooPyvLD1JzLHF7geHd5wPZ5Nd1SKZmAtR2N-6hAi-ZlozDca8jbe02dy16urOH5oAHuAG3B3YDlfpQiHNaiIAkVLYPsUyKQrquJqMKwz7CU8ISJm9Hc8lKr4i9RDzax7TcXF-ImdekRl91mVsofllGgSAaoGVcky-qC4VnPgZwhhny_YW6Bc_-N0kdYlSti5GG3K5DQefLpt2yO1ACSLZr62JWNqycBXqOthBTFKw0zBxt0QMFPIGpnaLWh8dMFgRjLYq3g-BioKux_ruTo44T7w8FormA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
جی‌دی‌ونس:
ایرانی‌ها برای دومین شب متوالی به هیچ کشتی‌ای در تنگه هرمز شلیک نکردند. تا این لحظه، آن‌ها به تعهد خود پایبند بوده‌اند.
سنتکام اجازه داده است دوازده کشتی از محاصره دریایی ما عبور کنند، بنابراین ما نیز به سهم خود به تعهدمان پایبند هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66440" target="_blank">📅 20:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66439">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL4TbgFNW0Aa7B1OlnbjkorOHFIRSIODuRSmlspQJt9FTCeTxfujmpcaqjaizOTrZylKICsWAPr1u-UR9N74MzXe_1Ixio13hGUdrXvdTVpibX9LKbSd2KJMo4sCWpf3V6VEpmB4L4IvioARBS5iIQ5jgvR18tT7RbWRLOBAkJPp2ZNbehg0h4NRoDlKPDe3vsEydF1OZ5Op3syA4GAN6X6OnSxCMtC0Rt-QxxqjdIHaIwNpBM1vXpnQYYORkBziWO5KbVI_W-wXNeJ9-yrEo2eYRArg3ttKGEiuaZcIHm7H63HyzxCS49Zsd6N82ODqPX3wlY1DzXHrJPytoMFbtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
فایننشال تایمز :
گزارش شده است که ایران به ۶ میلیارد دلار از دارایی‌های بلوکه‌شده خود دسترسی خواهد داشت تا کالاهای آمریکایی خریداری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66439" target="_blank">📅 20:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66438">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwCAb66GgvEF6QwVaRinA2ZxU863I1mSpUBJ37nHyKGMnMY7tAaKTzbN5iWVSpj768TI2ibPfNTCxBLiz7bdbpUQlTfqOJT665ZsznetsC6Uxt1RDouIyHhWOoM0Lq25GjS-ec8-FLMajJB7_49qySEcYRE38h7kNy3ynSHkrefXBq-iWB19Xa6uqoTr2x3ZL2-hrrWb4BmxWN4rn4GLp3GLvj5ei6JS9dmYhFO1H3EcikPU6twijKT3_DeJQHNw2pWRCAkrVnn4m4o94MlSJLGkuHylMn3vjNaPFK28oTIG4U2KoQXSMaKurGYTjRlL-r5j7LVnDousXaI1Hcrzww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
ونس: کجا می روی دونالد! «امام مجتبی» منتظر توست!
دونالد: از روی امام شرم دارم ونس! شرم! توان دیدن جراحات ایشان را ندارم!
ونس: تو هر کار توانستی کردی! تصمیم امام اصلح است بر ما!
دونالد:‌ چه کنم! چه کنم ونس! با این جماعت هزار رنگ٬ که دروغ را چون «رج قالی» میبافند! امام مان تنهای تنهاست! شرم بر من ونس! شرم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/66438" target="_blank">📅 19:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66437">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=SGE2kWZJUVHq2DJ85iqT3Y33tfexEtcDL272E-YR0o4xMGsCDkPA45kEENnmuS-wrBgquAQwTcyjdhe6GNLn2onpRvTYTkYNyEhWChHbkqzwBtZ5m0_Z5SjbSHuAlMuSBxPmKThyqSPO9T9xSV3sh32LgA45zfts_q_QgTYHTz6m7hv3eRSlmlF50GRlculIThLn7BZMRP438i1Ai0E7fhlBbt6insw88nEDqOGTFtpRjC_nQi8DEYRaFWfb8nyxLq34F6Q2H1EUMitisHCnJQCjaqobenOKwG0U7JFfWIXQ5T6xTBirYidpIStRSIhHfgR81Ku9gw3qin6byR7t6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4fb90d19.mp4?token=SGE2kWZJUVHq2DJ85iqT3Y33tfexEtcDL272E-YR0o4xMGsCDkPA45kEENnmuS-wrBgquAQwTcyjdhe6GNLn2onpRvTYTkYNyEhWChHbkqzwBtZ5m0_Z5SjbSHuAlMuSBxPmKThyqSPO9T9xSV3sh32LgA45zfts_q_QgTYHTz6m7hv3eRSlmlF50GRlculIThLn7BZMRP438i1Ai0E7fhlBbt6insw88nEDqOGTFtpRjC_nQi8DEYRaFWfb8nyxLq34F6Q2H1EUMitisHCnJQCjaqobenOKwG0U7JFfWIXQ5T6xTBirYidpIStRSIhHfgR81Ku9gw3qin6byR7t6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار:یه مرد دانا سال 2020گفت ایران هیچ جنگی رو نبرده اما در هیچ مذاکره ای هم شکست نخورده
ترامپ:کی اینو گفته؟
خبرنگار:دونالد ترامپ.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66437" target="_blank">📅 19:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66436">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euHBd9h744jvf3qMfX6ByN-ofPvhgzfZcuJuqtKFKFsHzWjzxEOyMyG4WFCZomBlAJAvcKvuzF_BgEtRRR-j-4ylMQYnNaNIyp3fqaXW2ykcIaG3jj8KWOO3uJnme52TfzxBjfQLfxO2X4Wn0Yo6Hzmnq0sYOcR_N-IhW4ej70VfbfL2PcUI2xO2SDvrqL7x_m45RBkZ87_Us04GBZsQqW20PWIm3P2L6sseh3SsxptCoO4I0v05-O89r4-Imff6Jtqu9g2AUt7rXFJA07d_phngJ_zUyvQMa0yT9j-eqUdj-wYMHcd2YnQS0YIWeZURyHTj2s0e692VOcYpmLYHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
الجزیره به نقل از تلویزیون پاکستان:
سفر برنامه ریزی شده شهباز شریف به سوییس بدون ذکر دلیل لغو شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66436" target="_blank">📅 18:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66435">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWwvslTdm7iDmlD7W2rjRIfAVoAY_mjdDiogv0LDJWZQeeTs42Xe0-rAaOQbfLDPE6vw4hW7ck-4GO6pbRB5T8prlq873Wet4bwsMnRDBmVZafpwm0JrhEGWLPcO9GNZEa1QzCPgGyvCvu9Nf-9vYXn13KdAL9tEW7VZ6Z3zq6YcUaQYq59VyX6LMJ_F_WGhtedwb2NWCLfgg0Rtvs4riVZfI-1S1D3ZNmRs8aTqLlMl0mvBGFY-aqYS0M3wWVF5wN2qQimTqVMbHMsZgyfRMAXicvh2UP9GMvJTpoXXw_sJ-940c6QJqP9DozfQEUNTqBCcduPCSf0KLiH0miTlDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
نفت جریان دارد، ایران هرگز نمی‌تواند سلاح هسته‌ای داشته باشد (جهان امن خواهد بود!)، بازارهای سهام در حال رونق هستند، مشاغل رکورد زده‌اند و قیمت‌ها در حال کاهش هستند (قابلیت خرید!). کشور ما قوی، امن و محترم‌تر از همیشه است. «خواهش می‌کنم!» رئیس جمهور دی‌جی‌تی
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66435" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66432">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-rxbPzbMwFReoQhsuJkTI6iOt0KhgGRFvksdFCJBrS57T899kHtVMHSXP5DbDgttmo_JE475IQvp_zlBqcHik3iP4cSO4GSIHyO7Z5KjPnirmkQiD0RuFU8nj5h-cpxOvZZtKPxGXX3ZBJ47OXRa1AhxqLQlv00vrVyi1IHcaC6TWQF8QZnr7XbQBVV8z3DT5USiC3HPm5JF8KRRl8Z42PoJlbW0I4jm2U3Dth1e9hZtjisYUWf0zPJrpd_7pOe_3H_Agrx5GSzWSpvxwkp1g8P240GtwM3moERTudo2zBSmwo3FoC4POLuyijjjIMtyda0v-jKoVwzOw7i9Q0IOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NABMbzahYcbJGWAy3dVHoTzng0mX4a7j3Y9hjPdWHNna0DVeHqMdUN4fvEWL_g_hmc_S-XzXa3f0yhNqec6IaGTOz9am1cdgZbrFbKknYpvMKcc8sIzd8Xr9i_wFhXVwwRvas2nQyBjweClIEpCZqf4UuG3Izstmh1tXWr-i2pEqM2ZoHlV5sFYyD1g8ebIbAbxc6pZZXnPEf2PECo_1DCsSh1KaS0jZDxxUoGv2WupfE4ad2Sz-1F_5VpAqAI3nDjtQajDJQqZyQhQ_jUYLguB3hGWD9EDYD9bysvM45oOm4cumwLzYJZmDFfSnE0wECVb7144jWHw2l6WqgqS3_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=pfCE-Bws-zf05_v465LWvuRKzqKwLfAzyzCEmhxBzG5RRaDXGwhOC4w59e2ToVY7jwW7Zkf-utFJZ7ALVOVMr-aSPSbJWjhy8o2YdC9p7H7t9Gymyo0ErJOhIWvX5OJ0R42nrYpwgIf4-P6ZTaOWs-s84HzYZKWec6k7_5IGIx6v1N7Dq9Cv6Z8jGmU6R1h-H21M2wZINb4mYYv_zI8XgQWtZaLr8zUThK_Wo5yzIJbk4WlUA3hJaRmRY8lVqUiVVHPhNKAdJzKPvmMe8UKjjTOyND749x85WxE7oEhuEREPYnTJXk2cV21qXZHAj6Qez3yu9mcJRyF07jMtCkMGlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13c6e64c5c.mp4?token=pfCE-Bws-zf05_v465LWvuRKzqKwLfAzyzCEmhxBzG5RRaDXGwhOC4w59e2ToVY7jwW7Zkf-utFJZ7ALVOVMr-aSPSbJWjhy8o2YdC9p7H7t9Gymyo0ErJOhIWvX5OJ0R42nrYpwgIf4-P6ZTaOWs-s84HzYZKWec6k7_5IGIx6v1N7Dq9Cv6Z8jGmU6R1h-H21M2wZINb4mYYv_zI8XgQWtZaLr8zUThK_Wo5yzIJbk4WlUA3hJaRmRY8lVqUiVVHPhNKAdJzKPvmMe8UKjjTOyND749x85WxE7oEhuEREPYnTJXk2cV21qXZHAj6Qez3yu9mcJRyF07jMtCkMGlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پختو پز اوکراین در مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66432" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66431">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=vZUxpe7PyLfvBzG1z8iMt9xYub7EIsXMNZ5kOthRxIw_4FZxrNWifLIhtjNkKf-xfjiIw3gyipIZu4X2CQyDkOkRglMFt7CbzRDrC-av_QXYqGBpjBVV1sI1r7CYM2vf3ALoBh7AnNAuE9f-6fRGsLuBv734YgDNKvfezRHyDs_eHbfvqA2f_StoeYcfl4V1j8WltpSC_GOsufhzhBOgZz5jZSlwil9PRkY0mu4xU1fCBid4eTheb7F8PIm6WWWKY8ZS8XWrhpbQsNHoV0MuZRDgvW774nATw3Ylz5wSxxsDJXZu_-va8WMsqksbXO5Pg0RQIzIFIBSeo9xco75J8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bf3ba597d.mp4?token=vZUxpe7PyLfvBzG1z8iMt9xYub7EIsXMNZ5kOthRxIw_4FZxrNWifLIhtjNkKf-xfjiIw3gyipIZu4X2CQyDkOkRglMFt7CbzRDrC-av_QXYqGBpjBVV1sI1r7CYM2vf3ALoBh7AnNAuE9f-6fRGsLuBv734YgDNKvfezRHyDs_eHbfvqA2f_StoeYcfl4V1j8WltpSC_GOsufhzhBOgZz5jZSlwil9PRkY0mu4xU1fCBid4eTheb7F8PIm6WWWKY8ZS8XWrhpbQsNHoV0MuZRDgvW774nATw3Ylz5wSxxsDJXZu_-va8WMsqksbXO5Pg0RQIzIFIBSeo9xco75J8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد کشتی ها در تنگه هرمز پس از امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66431" target="_blank">📅 17:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66430">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb0sEba2CLcOkyfuQqAI8RbWOiLZvl_zqWJJRu28h5jthqGtOAQIECkSJ_-MIQ6pVrK3V7NsRVE9SF6YDGT-e0GsuoA8Xd4I8jjUGIXWEmPfyLvQc8X9-otiBTftctb6TMFqiVJOFKBkcSvo7aEcVL-gkxsbv7BeA2mA_hGu3lZycmyceGfcyI5G42V-zUFl1Uf1V388AFEd1iG0XdDCyXPGs_24VOiskSi2u5FDa-OWza5a7advJRGPSpXvS7hODTOCXS3Pso6mWTlbPLz6H-rAIAyRR80fDEkLWZV3N9Gb3JCnbUzvyt9ChbfFr1u_7D9ENX1AxT_cj-lYofqxbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
ارتش اسرائیل؛منطقه امنیتی فوری در جنوب لبنان:
نقشه منطقه‌ای که نیروهای دفاعی اسرائیل در جنوب لبنان در آن فعالیت می‌کنند
بر اساس نیازهای عملیاتی، نیروهای دفاعی اسرائیل در منطقه امنیتی واقع در حدود 10 کیلومتری داخل خاک لبنان مستقر شده‌اند.
نیروهای ارتش اسرائیل در منطقه عملیاتی جنوب لبنان مستقر شده‌اند و به تلاش برای از بین بردن تهدیدها و بهبود دفاع از جمعیت شمالی ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66430" target="_blank">📅 16:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66429">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZtADAW4LbqjJrkTqAgwfZTnZyzt5hESbMFB043dXlaJ7LMvGUFm0OYJYTgaMG-hOU2HmnJlXlctyerNkuw-_AE_gEsZksZPCUfGjmmiMFJ-clbPiCzXto9VgwL7T2Xhxjemqm1nJxDHQ8fgw86PzqxdtoHKp34UnSlvNXBBi9ct-L2N98nbRgK5WQSpx-f0yDGMIdolie8eeSFg4PVBr0Z8j0a7-bHWGN_zEqlZ159Kd4naQAGB9xIASCcEiQDerRkzO5Z_HY2xLWxcUeX1HyeCcwybd2Wvcafv8G5csL2jFZLp-XLI3_DaGIGjNi7jSAZxmphZh2k-58N1tgFgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان؛این یک سند تاریخی و پیامی از ایران مقتدر است:
صلح در سایه احترام متقابل تحقق خواهد یافت.
جمهوری اسلامی ایران به صلح جهانی با حفظ عزت و استقلال، پیشرفت و همکاری منطقه‌ای همواره متعهد و پایبند است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66429" target="_blank">📅 16:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66428">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/622db6728d.mp4?token=tU-keTDiuuR4uyXRh7QTt9STiU7n1I5EkSDga-a8oWFWVPhykLji3FZk-tYON5gm7GWX--QC0525Ar0vJ3KBGm6yrpxbTcoPoxRuzCiMt-Z41vVE9RH_fWn_u5uI76eJXShkmUtk3coIPhq_DY712LQxQUi_KFv86ZDg67vQ_HIHwfsTGh3w55jNtEs4lpbAn84PbdNKuiFAVp-Y86oYXL4gS0EFbP2cBMMSeFDT1yyXhltnlC3hCTUk2MOW3r9Wi3HFuY7xYXk4Ol8EwURvWNbf8w4jo6k89gLDfN6f8H0jOtiFA0UKJ0ag9spbmJXGpQp9C2x8vuKkGc31KxXEdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/622db6728d.mp4?token=tU-keTDiuuR4uyXRh7QTt9STiU7n1I5EkSDga-a8oWFWVPhykLji3FZk-tYON5gm7GWX--QC0525Ar0vJ3KBGm6yrpxbTcoPoxRuzCiMt-Z41vVE9RH_fWn_u5uI76eJXShkmUtk3coIPhq_DY712LQxQUi_KFv86ZDg67vQ_HIHwfsTGh3w55jNtEs4lpbAn84PbdNKuiFAVp-Y86oYXL4gS0EFbP2cBMMSeFDT1yyXhltnlC3hCTUk2MOW3r9Wi3HFuY7xYXk4Ol8EwURvWNbf8w4jo6k89gLDfN6f8H0jOtiFA0UKJ0ag9spbmJXGpQp9C2x8vuKkGc31KxXEdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعد سه ماه هرشب توی خیابون موندن و پرچم تکون دادن ، بهت میگن اقلیتی تندرو و خون رهبرتم پایمال شده:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66428" target="_blank">📅 15:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=tWEs_Q69oq7IsEORAjFcoBG3A0zq9uZ9-X5xKT9C6s3oIXqse3sr380hqLUJFKntro6lFCb8AQoOChgEaduSDrfXmiZAI9ExVFwqK3bn7LnYmAlOXSu5twOk2kAuOFQqfErpO8igT1pALxmSiRxEke1xpJNcJa88Nlpd9bPXbgOJwWtFIOZZ6f4zS5rvlSCgt3xVc3CMtteSYeXmNchuR1DWN2LgK6MvVnMJiGGrJjml_hofJxbuy_a2ngbNh-3YviM1U1E76NVt8LacGicgPpiR7r2rla68FgBXHhEWBsazbaA9Zb6Th3mhLgPWIJt8rJYgcpGdGpJ4W2P6qtqNwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4faedc1ad.mp4?token=tWEs_Q69oq7IsEORAjFcoBG3A0zq9uZ9-X5xKT9C6s3oIXqse3sr380hqLUJFKntro6lFCb8AQoOChgEaduSDrfXmiZAI9ExVFwqK3bn7LnYmAlOXSu5twOk2kAuOFQqfErpO8igT1pALxmSiRxEke1xpJNcJa88Nlpd9bPXbgOJwWtFIOZZ6f4zS5rvlSCgt3xVc3CMtteSYeXmNchuR1DWN2LgK6MvVnMJiGGrJjml_hofJxbuy_a2ngbNh-3YviM1U1E76NVt8LacGicgPpiR7r2rla68FgBXHhEWBsazbaA9Zb6Th3mhLgPWIJt8rJYgcpGdGpJ4W2P6qtqNwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین اوکراین به مسکو پایتخت روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66425" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66424">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=TwatEt3XBAUzZAC1rJ7KplLAgGa90X1Gdmpk2Ph7CAGZp6N5-y9k20MAAdVJSbtM3c2SFEKRXH0ys2czd1OkrdlnlXRVwl5MDx-aY6XHyv0WpIqNV0mZSmBuV1VwOzoP5h2YqOmG_L9UA3fTcc7zpZy7SFNm2D4WGrDSRmPfbXHcpwDHpP1DRAjbHFK9bzFNe0mvZ9rdeoS0qyty-p2dnteRxidMxeC8Btf7VJLrqfI1oNghUergwuC5ZTErO10bPV4cA1szpwxoDeTped_MUCPZeEhObrC4dOjYEri6bxInERioa0Rzh6QqumOZaZYAVyMXmqJ_wlLA35L5SuJf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d92b0722cb.mp4?token=TwatEt3XBAUzZAC1rJ7KplLAgGa90X1Gdmpk2Ph7CAGZp6N5-y9k20MAAdVJSbtM3c2SFEKRXH0ys2czd1OkrdlnlXRVwl5MDx-aY6XHyv0WpIqNV0mZSmBuV1VwOzoP5h2YqOmG_L9UA3fTcc7zpZy7SFNm2D4WGrDSRmPfbXHcpwDHpP1DRAjbHFK9bzFNe0mvZ9rdeoS0qyty-p2dnteRxidMxeC8Btf7VJLrqfI1oNghUergwuC5ZTErO10bPV4cA1szpwxoDeTped_MUCPZeEhObrC4dOjYEri6bxInERioa0Rzh6QqumOZaZYAVyMXmqJ_wlLA35L5SuJf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏جی دی ونس در مورد مسلح کردن معترضان ایرانی:
در واقع تا حدودی دشوار است. می‌دانید، نمی‌توانید همین‌طوری از آسمان سلاح پرتاب کنید. واقعاً زیرساخت لازم برای رساندن سلاح به قلب مردم ایران وجود ندارد.
یکی از چیزهایی که رئیس جمهور خیلی نگرانش بود، همه این معترضان بی‌گناهی بودند که توسط افرادی که چند ماه پیش مسئول بودند، قتل عام می‌شدند.
آن افراد اکنون رفته‌اند. اما خواهیم دید: آیا این رهبران جدید با مردم متفاوت رفتار می‌کنند؟ مطمئناً امیدواریم که اینطور باشد.
و اگر اینطور نباشد، می‌توانیم وقتی رفتار واقعی آنها را ببینیم، بفهمیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66424" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66423">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BK81EQzxb7Z0G55n1p6PbfvKwBRqtstGPdrS_awzgh7CBB3pET54qOeq0B76_1Q0lNzLelzbY3KSf0UPc0RgXvktZACF1Jk3ujXc8BHX_-K5qLaDLFJ3o9d7dJ7D0hVbQn2GsTH6Kzc2u2gO25UlFcYb1RNcY6zmPT0WqswjJOqEWYmTTI2fsEklx-WP0gpN8hPGHoW6vyfIjNbzaUaCckDUGY8jBPezteRWcdW4HzKsJiHWIN91a3r_Ec5-UGLBUyqclwtn7tjXb_-FT3OY_mpTwNt_HaIOsEwV5nm4NkruH0SCEEmKQh-J0BE5C5Sb4U2F-rXaNLrKrGZTL69zpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حملات اسرائیل به جنوب لبنان همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66423" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66422">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66422" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66422" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1dGzn9jvlNkmAAl8lbDIDJaaONyWmRRxP5KqQbijg9xwDxpzfE30VSFGDXRNBKMtJncQXuFJtVUkwl8vuBYwL77PZqpeH5x6Uuz0HROUIFHpdlBLSgHo29ZFf3191Xs5PXxdGGJwwUcgGb0zQKZJCRnnXyPDdceomHseQ04Re3Rleim1jlcnHkuWEuNH9E6bEPHYJYqhhbYx4DS-JT6wtqHvbeNiw7MuoF6tB0pdIvtLSx9Y7F1PXQKSDD-i5jSa0rY7cgVh4T5I8asBh93jC5gYHoXjjcDULd--IHHIN_ILwMpOefidqj4X3EAMToHCYi63i3FuJLR7Ma79_nAYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66421" target="_blank">📅 14:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66420">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fF-Zk1q5TEj5pvjdcxd-UwBtZWOgUQjzP5SOxZx-9YljL80rXRtECqZNhO4o-Dz27VqthWBIl_H2Af9vdJyGQ4eWH7lXdt8YtMr8NfcgnNhscqXCvzmLnPNdlYko6rtf_W6xPjasTvXBJ2XNSzGl6Q1P4dWzT0UGtDjI_X7M5-ki4BuvlrG0PjZLpb6HONc-Uav5orkVQE3ojjLp7aftCiItFWF8Xp6F51pOU38_dSqvD-lFKxXGfAFhlILC6GFnyJLtcJHN97DRgb-M0MV9qtnwYHBFftguHhLHdZLRN_kOWyiKnEJXui6kc38kdmP07JVe8K2vLQuB_XpBiNrEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای پزشکیان از نزدیک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66420" target="_blank">📅 13:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66419">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=fyoGj_prmvmqw3UKSSlAsop8kUPkSc1PTS_n38Jv7W8duQskWFFK-TWFRXdK6Fm1gC5aCn91GlWffnjyAh65iuor5oVQGEMdLzkc8MKiwokKFgi3eUCmNthB8UrVwDzxS0zOuCFtxKgZGoKjMhs01-P5X_w-GYCri239YeBSYZI_O8jip0VFoBn4Rm86lqZaPzUx63XXEB3n_i1Dt4rzHUWo_EU1UW6uTK7YG2urMWg4xY-x1XMvRAla9FsK8ftIi6KknQ8-oTlBv0Jplyuqgw3CK3m7C_ttPFBZXI-NQcu-MLLkf-DsYJgNwx9An7yLRanJZLQylBoINK2mPXt-vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1890fc432.mp4?token=fyoGj_prmvmqw3UKSSlAsop8kUPkSc1PTS_n38Jv7W8duQskWFFK-TWFRXdK6Fm1gC5aCn91GlWffnjyAh65iuor5oVQGEMdLzkc8MKiwokKFgi3eUCmNthB8UrVwDzxS0zOuCFtxKgZGoKjMhs01-P5X_w-GYCri239YeBSYZI_O8jip0VFoBn4Rm86lqZaPzUx63XXEB3n_i1Dt4rzHUWo_EU1UW6uTK7YG2urMWg4xY-x1XMvRAla9FsK8ftIi6KknQ8-oTlBv0Jplyuqgw3CK3m7C_ttPFBZXI-NQcu-MLLkf-DsYJgNwx9An7yLRanJZLQylBoINK2mPXt-vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
لحظه امضای تفاهم‌نامه توسط شهباز شریف نخست وزیر پاکستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66419" target="_blank">📅 13:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66418">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=hUsQmGZ21p38Nn6wl8m9JdQpbMDjaP58IDWA3B9MECdc8TCyOvaA4K4TXyNnsW2Cm-TSHYEEh595CNcKceIL_J1TcoSeqmdAhHaUUmXpvIK4YSinwXokQvwxACqUOhDFndTTDedtr9PpcuWzIF0eN85OsOMoPlJ05DaMeHsBEsc0jBsxv0EHCXt7io4oTH0e3T7QOATeKMQ-inPEAJaZ904r-CBkDhxK4M1zttK-L80YFNmEIOoA-cPM7xF3wI9M5Dw273inIhNiBcuiQwCP_O0ryUsaQZXJZPAdjW-szc6GFQ2x393eh4sQpeLJHwbJSsEOIFruuN8TRUhRifw93Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50fdfa7aaf.mp4?token=hUsQmGZ21p38Nn6wl8m9JdQpbMDjaP58IDWA3B9MECdc8TCyOvaA4K4TXyNnsW2Cm-TSHYEEh595CNcKceIL_J1TcoSeqmdAhHaUUmXpvIK4YSinwXokQvwxACqUOhDFndTTDedtr9PpcuWzIF0eN85OsOMoPlJ05DaMeHsBEsc0jBsxv0EHCXt7io4oTH0e3T7QOATeKMQ-inPEAJaZ904r-CBkDhxK4M1zttK-L80YFNmEIOoA-cPM7xF3wI9M5Dw273inIhNiBcuiQwCP_O0ryUsaQZXJZPAdjW-szc6GFQ2x393eh4sQpeLJHwbJSsEOIFruuN8TRUhRifw93Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیرزن کسخل مکرون دیروز موقع عکس یادگاری سران گروه 7 نزدیک بود زمین بخوره و شانس آورد ترامپ بغل دستش بود گرفتش
😂
😐
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66418" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66417">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">قطار پیشرفت آموزش و پرورش کشور خدایا شکرت   @sammfoott</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66417" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66416">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfgRNcX_6XeqMd9dRHVv7XpnF3gqalR1Tx6xAH7t8zsA1pKjOHVKb2oAw6cAoXZzfnsVIulGmvBTzwZWHu-ViXl0Lva24lRXF41OYETJsU-097Pdu01zJFqIpZWM8ZIFZ_yt0htEtEwjFKCWoCPTvxbxGUNOnvahCWNTpziGKmiIBINoV0SvR2tSfsNFXLTcqeO4WgYG-1_TNW9MaDPd4XHagWEax4RWBhS8Sneq1u1JxntB7tYtm6OKVJW6qGQXyPK7GKnn9pdS2o4po86WheNil5n60VIXWVfgLzXNcKHDWeEJEIcJS3rQHr4mHSn_oN8RsUitSRdVRkdwdZWIHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«این احمق‌هایی که فکر می‌کنند من با ایران به اندازه کافی قاطع نبودم، در حالی که بازار سهام به تازگی به سطح بی‌سابقه‌ای رسیده و قیمت نفت در حال «سقوط» است، یا حسودند، یا آدم‌های بدی هستند، یا احمق. بیایید دوباره آمریکا را بزرگ کنیم!!!»
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66416" target="_blank">📅 12:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66415">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=MCbm_XjJ3bD5dfimFZ8cBVQ5idECJXL_mLl1WU4KFk4AzMDfT_l9j59d_ck6IMsGHpQ9Qpdv8KjOwOXHwtccnumGhxUnGQ5N9--t3QIQJ__HYxHy8ueVycrUQLTfQeTarX75sAL-fUvfmUBi3wAah-hG7S2wsjNy9uNYTdo93-M6iiZcO0pgIlqfByOPgZuFiOY4zWLSe_pJATDndD_8Q3fpCNGVftIkxWfytCSYXt3zRd6vh2Gy4YifVj1U4sHbEgnxzO25EeOdWBz2lJiFNQ_67czZOf8QC3L8qVoFnKxjcnAgnfT-Ww0HNJc9uT8Tr-03x2CEE0wRzacxfl2hyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16c0579b45.mp4?token=MCbm_XjJ3bD5dfimFZ8cBVQ5idECJXL_mLl1WU4KFk4AzMDfT_l9j59d_ck6IMsGHpQ9Qpdv8KjOwOXHwtccnumGhxUnGQ5N9--t3QIQJ__HYxHy8ueVycrUQLTfQeTarX75sAL-fUvfmUBi3wAah-hG7S2wsjNy9uNYTdo93-M6iiZcO0pgIlqfByOPgZuFiOY4zWLSe_pJATDndD_8Q3fpCNGVftIkxWfytCSYXt3zRd6vh2Gy4YifVj1U4sHbEgnxzO25EeOdWBz2lJiFNQ_67czZOf8QC3L8qVoFnKxjcnAgnfT-Ww0HNJc9uT8Tr-03x2CEE0wRzacxfl2hyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط اونجاش که یه موز و دوتا پرتقال بود
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/66415" target="_blank">📅 12:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66414">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=tPBPmMLKGnM16d44iU8_YePtMl-JQmUQaU2tUEIUSJjNp8jWFUu_xBCTNaN7L2BQK9wNP3sC8Z3QRSdxHwv7R8VdnineJ9hoZxoBFOfEonXTq-4bZcrujod7ez6wwpgGvNYRfMgR-Euypmi5f-Ntu60-577fjgvARpceQ2CO_t9NmjrhbgnwK-rj6ydZq-nxUA3fY44OrO8PdY5vNGz_hNzl0Hm0ya2nVgeJQOYX-Shl2uyPgoALgE5bNpps1c-TGPy49s6cgepiTk4G0aqF-8uWyKBQz9MX_DU6fRqmgPh0pVhx6SR188pE0Gd4nJpoKFOQuYpy7f2C5eVLEi0VGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb19ef0a8a.mp4?token=tPBPmMLKGnM16d44iU8_YePtMl-JQmUQaU2tUEIUSJjNp8jWFUu_xBCTNaN7L2BQK9wNP3sC8Z3QRSdxHwv7R8VdnineJ9hoZxoBFOfEonXTq-4bZcrujod7ez6wwpgGvNYRfMgR-Euypmi5f-Ntu60-577fjgvARpceQ2CO_t9NmjrhbgnwK-rj6ydZq-nxUA3fY44OrO8PdY5vNGz_hNzl0Hm0ya2nVgeJQOYX-Shl2uyPgoALgE5bNpps1c-TGPy49s6cgepiTk4G0aqF-8uWyKBQz9MX_DU6fRqmgPh0pVhx6SR188pE0Gd4nJpoKFOQuYpy7f2C5eVLEi0VGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
با همچین عزیزانی تو ممکلت هموطنیم :(
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66414" target="_blank">📅 11:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66413">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=Pz0ZCztaIzSjGJk6Bth3vq4PaSudlQuqQPkED5hkZYRgrIVh0VWojjzpeUPCNkBSOHp5XDGGEQGIKswm9hXX0lNMZryEZArUkbzpn_5siLn61EBTwS7Ze_ciqX5u8WhIzFifFy60ahC0uOBVP9hWuOF0eZey6AJ9D2ew20bVB6svXdBJwNyWAHIbcHLj8J89yyDl_OnSUrzh_oXaSWdRBgf0mO6hwz4K49HcptUN9T7FxU5rwcITVJNRS-tO7KN9wKrRvqQmGMOB8NhaBQ1cEvKYMTVlgOsDw_OOc-PYa1t2yyPl3kn_jKJ44t_RFG11kD2SB1rB-tkWh3ZuS-o5TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af0a234cf.mp4?token=Pz0ZCztaIzSjGJk6Bth3vq4PaSudlQuqQPkED5hkZYRgrIVh0VWojjzpeUPCNkBSOHp5XDGGEQGIKswm9hXX0lNMZryEZArUkbzpn_5siLn61EBTwS7Ze_ciqX5u8WhIzFifFy60ahC0uOBVP9hWuOF0eZey6AJ9D2ew20bVB6svXdBJwNyWAHIbcHLj8J89yyDl_OnSUrzh_oXaSWdRBgf0mO6hwz4K49HcptUN9T7FxU5rwcITVJNRS-tO7KN9wKrRvqQmGMOB8NhaBQ1cEvKYMTVlgOsDw_OOc-PYa1t2yyPl3kn_jKJ44t_RFG11kD2SB1rB-tkWh3ZuS-o5TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
برشی از سخنان تند شب‌گذشته قالیباف خطاب به ارزشی‌ها و تندروهای کسمغز
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66413" target="_blank">📅 11:03 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66412">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=ZpAXhlxJlFSHnZErIZu-IRQ7x-lxYyxWxMfEHSQD2qcnOnKGdktwpOXmctmJ7Zh-FS6vYdSZEieJH-Z0jt6j1hmJvOs10OQKjilhKJ4umqFkTLKQ2GTfu7qb7bG00swEW6tE95t-gptK2pvdrGn_hMBrBk_UwBNICnGIcGSdL4oBR17WcUo1Ki8EkSUSxHboozZivA77AeUc0MeU2ricJYlKJiyDDWDG3YQqVqw0MHxgDPVlMWg5eascvV3LEXMqLYOGiuIOt5qAlF0i9pdgE5qvRYkizTTCuf2JZBwCchx9GI7kqZdYMO1M_y7NZdeoxCmWnorNkxH_ttLZmUy4Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04da6f24fd.mp4?token=ZpAXhlxJlFSHnZErIZu-IRQ7x-lxYyxWxMfEHSQD2qcnOnKGdktwpOXmctmJ7Zh-FS6vYdSZEieJH-Z0jt6j1hmJvOs10OQKjilhKJ4umqFkTLKQ2GTfu7qb7bG00swEW6tE95t-gptK2pvdrGn_hMBrBk_UwBNICnGIcGSdL4oBR17WcUo1Ki8EkSUSxHboozZivA77AeUc0MeU2ricJYlKJiyDDWDG3YQqVqw0MHxgDPVlMWg5eascvV3LEXMqLYOGiuIOt5qAlF0i9pdgE5qvRYkizTTCuf2JZBwCchx9GI7kqZdYMO1M_y7NZdeoxCmWnorNkxH_ttLZmUy4Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو ببینید
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66412" target="_blank">📅 10:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66411">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=FFBBqom_d975p3yOpijqOzb_qLSJjw47zhDhVKPpUobmJoBkfDxJC5IszIUhdH-3FKjfQ3_z0JwVfink56IvPsmuxlJRKhoe-_7b3DzLzI8Kuc41IUhbh5oClMypg3ieJoiCtfgu5jetQ1PVuFo21B6XdLlz07hd0varv1sGT3NNSaKEYbrizckXvyX-umy9VdkfD1b7psX642BQ-66Swsq_qub03CwOVzxlrXTqwu_7IEWC1QGjCWDGyUckM-3dboYBWjfzu__tMg2855ScaADXqVra73QcZ8JseZsMLv5NXHufejPaH5pwviyyPqbuXxCQ9yerMSm8ryl-vAZQqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc5db481b.mp4?token=FFBBqom_d975p3yOpijqOzb_qLSJjw47zhDhVKPpUobmJoBkfDxJC5IszIUhdH-3FKjfQ3_z0JwVfink56IvPsmuxlJRKhoe-_7b3DzLzI8Kuc41IUhbh5oClMypg3ieJoiCtfgu5jetQ1PVuFo21B6XdLlz07hd0varv1sGT3NNSaKEYbrizckXvyX-umy9VdkfD1b7psX642BQ-66Swsq_qub03CwOVzxlrXTqwu_7IEWC1QGjCWDGyUckM-3dboYBWjfzu__tMg2855ScaADXqVra73QcZ8JseZsMLv5NXHufejPaH5pwviyyPqbuXxCQ9yerMSm8ryl-vAZQqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب دو سال قبل شاهین نجفی درباره قالیباف:
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66411" target="_blank">📅 10:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66410">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=twHioJdjxqEHTgw6EOhTixoV-vIYrxVtiKKqDwh-3T4BrJK0XFBbrqdw9k9VU28RcRIDObWnCIzUzqBm-gwOQL-PZs2d3Ss4ZkwjnlZNnzr_pCfd3PIEFr_GPuUa4U16EWP34i1GP8uj8_yfDBW7kZpPD_h5pEpaRbtu9MLyaE_qNHXWjzp9M40lUAIFCuFsyxThlLxE0a8lgIxHVggfnlLMyNcC_is2UgkqWlF8mhxHsF-G9clr9LOJ0vdUkR9dAtheGXeVahgInHTvahH_dcfNUMlNlF1UMcXUN93gVGMnOygid5kpxYNASN05imHoNCy8lbBA3wmG8v27gvX5Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f1770ac7.mp4?token=twHioJdjxqEHTgw6EOhTixoV-vIYrxVtiKKqDwh-3T4BrJK0XFBbrqdw9k9VU28RcRIDObWnCIzUzqBm-gwOQL-PZs2d3Ss4ZkwjnlZNnzr_pCfd3PIEFr_GPuUa4U16EWP34i1GP8uj8_yfDBW7kZpPD_h5pEpaRbtu9MLyaE_qNHXWjzp9M40lUAIFCuFsyxThlLxE0a8lgIxHVggfnlLMyNcC_is2UgkqWlF8mhxHsF-G9clr9LOJ0vdUkR9dAtheGXeVahgInHTvahH_dcfNUMlNlF1UMcXUN93gVGMnOygid5kpxYNASN05imHoNCy8lbBA3wmG8v27gvX5Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
10ثانیه تراپی روح و روان
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66410" target="_blank">📅 09:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66409">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=Y-ntjFhoqv7-KB6ukPnYU_RkijNSR51ji7m5cpd8Rr1XSQ_Aea2rxjQzht6fMWIgpKTOiGnyJRljVrM8lIPm0TL0A4t_VORBWAUUHs9hJLiVr45xGWgf3tXv5NgDtmNM_k6tppZVg5TrBdECTzt4SVf7VOf9v7Au9_VdLrsLwHwoto1WdZM2_ob2eZWJ_Nv-yiZN7m1aZQ6o6E78p5rujSsZq37W0LSpV_cHd9TZgDXI-tRpVTigRrFQW6fCnQqqaPXJZOzjLmjG06wHstXm8V9CE-2F5at1NNhRCjaDTJrKqESLkjX21wShOMdYHpOLPVGHtnzy0O30cCHvGSD_OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d95de07e4f.mp4?token=Y-ntjFhoqv7-KB6ukPnYU_RkijNSR51ji7m5cpd8Rr1XSQ_Aea2rxjQzht6fMWIgpKTOiGnyJRljVrM8lIPm0TL0A4t_VORBWAUUHs9hJLiVr45xGWgf3tXv5NgDtmNM_k6tppZVg5TrBdECTzt4SVf7VOf9v7Au9_VdLrsLwHwoto1WdZM2_ob2eZWJ_Nv-yiZN7m1aZQ6o6E78p5rujSsZq37W0LSpV_cHd9TZgDXI-tRpVTigRrFQW6fCnQqqaPXJZOzjLmjG06wHstXm8V9CE-2F5at1NNhRCjaDTJrKqESLkjX21wShOMdYHpOLPVGHtnzy0O30cCHvGSD_OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: چه مدت نیروهای نظامی آمریکا را در خلیج فارس نگه می‌دارید؟
ترامپ: هنوز به آن فکر نکرده‌ایم. احتمالاً برای مدتی، جای خوبی برای ماندن است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66409" target="_blank">📅 09:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66405">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8LtWslM7i54aR9KFjYfpL-ieo4jNKOLIjU03dHqCDJyq17xE6lhpzSiQmqkkODr_wveJXCwkCdVgdVLSr0vQKybl4Xj_wSa6hYwDheHPCCnPPP8tgIVlzfPfUEEmYfpYZWBT66VgzN3aCBMaen4kySujRPH1GfmrvkL6K4t8ayqIjKO-deRDTDQ6VJ_FijSTTNhA--CTgt8-Was2oJuMHBA1mnu_z00bvkfdqpfYhFA6_kY_uwyzfzLtdemmfALwhwLSQlBMFq1mI91nAQRYmzbBlxhQfSSHdkTvKqzohMSUynP-YHS4cOHAJqxmYqyrjgy-Fm5TIWcEO7thBhZ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRvF-WKN6QYD0ynFRQA6hrh5x8ECeWsP67ThbLt-mjaRv4Ytux16qMv2fHRVcRbgjfPwKfZ60kAT_Ud-uJEqn7RVnRWW9dqA-40AjiT9PqRXe2ZDDCldT9kXGenpWN1zJDC1nngDh_plAm6soRBzOZ943kfBWlAk0NacUb23AtSCe5Ria392wQ6yMDVYosNSF9ZN60rcpI_VWXGHX-Rj3PSmWJBGMKJmum4ei4cZdtIlEqN3MMMFd6u17nxXTDvnI8fXXf0oxQ_ITFYjOUIpLJh2wEpEc3rWJmihg-Ob_2w1f97PxWcQyECNjR-PGbG0xz9Zh08HZ9D0uGCQ8wecTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pR6DkCmE62WL0orLWNFKhXMln5PuYlAYu1BG398Z2lq6TAuZZfN-WP28ZVVBZ35HndZ6YAa8iiVFtBPKJQuSGS1JjJSwxLul0mQjES9A1l4JwajgUUH6XCP8mK_64ogHfVGPmvFKRs1Txnx0FjvyjF_NXlwvCvPl0dxWFWWRjg2RFWgizQyRVQQAYwNFidgvHot08YaLpDOZHyoWHrnOH3UnbpPQszZQQrhUdfI5RcTVoQJ_1fKVUrYigAfoXYcGdtskvvX6opkMyXeWckgER3ZIlxacOWFqE8Z7KbhFkElC6SFqHxtd7lpcFSLLBR-kizQb_t4rdgDIXmin0ije7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد  @News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/66405" target="_blank">📅 04:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66403">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8TIcdLFN8KXxYH9KShT_m4uEA7ij5dd76QXvhdJGRAupy8dY8O43SX99sZquoun0ySDZ_uvaGt_oZB5gql6oTe3grmQCtXwFD1rP2IJUA4a26-JbIgHZ3YM1V8ThrWqI_P67VZapzLSKh6bkpY9OpFWk7TYtfTg8_r7rB8w7Tf0Vy_PoR4fIPT1tKbthyiRBtFNufYAz_IHrJKn-pxDn0Oyz4hZCT9V7WvXFBex3x6Z1EaEvTd1L0laE8mF3xYH8WyAU3_wVQC8jlI3-MyYNq_6v6fRYj4CwA7DtPQxxYyFi65xrNGccyNmgEIRj3IEi5M4pmlxI9hbEGx7O1vcPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=cVgWa9-DasxwKSi62r-XGS3ThG0RfyzMgQVfX9JvgAgtZaPx5ghleF3S6VpBVhPu3NHXcOew8F-WFs6PNdvMoHaiUExcUfzYBBuDYrbgCVdV7jyZd4lbKy5DI_M9YF_6U0CNilzzQ-6FLLu1KtOr7sIUzhqgXBnp4I8nZQhUBM2joam3I_y7cWjs75Fk_coNE7ihtM4aMZ51ZwQnjjd9UtQ4dTA71P78ST24d12v6tb7Wd1M7G3RRpBiSxVT4B_TaLoxax-Q64eOiJdhG_Hxv3hBTAam5-Fb3VMVIDdoQa7oe64J5oJyBtaHrGtQNHMcIMlV3N2jYviarnm9y8Wvfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=cVgWa9-DasxwKSi62r-XGS3ThG0RfyzMgQVfX9JvgAgtZaPx5ghleF3S6VpBVhPu3NHXcOew8F-WFs6PNdvMoHaiUExcUfzYBBuDYrbgCVdV7jyZd4lbKy5DI_M9YF_6U0CNilzzQ-6FLLu1KtOr7sIUzhqgXBnp4I8nZQhUBM2joam3I_y7cWjs75Fk_coNE7ihtM4aMZ51ZwQnjjd9UtQ4dTA71P78ST24d12v6tb7Wd1M7G3RRpBiSxVT4B_TaLoxax-Q64eOiJdhG_Hxv3hBTAam5-Fb3VMVIDdoQa7oe64J5oJyBtaHrGtQNHMcIMlV3N2jYviarnm9y8Wvfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری
؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/66403" target="_blank">📅 04:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66402">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66402" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66401">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/YEdrG7jmZqTQ27KfKGYg-q3e2ENpx5ommJDxAb-EjDXTnANirnJsMER5iBl0H1d5Bi5Qwf1Ox5hG7n9xpiF-1UQwx0jqNsxqMnliuYswmQw-W31aMTuf0_Tz61xy4OhApDQJSOe5JOCfkbA_TdAzFkCQ-m7a7p3HwiyA1pe05o_G9s8uQTMtTMmcKRjoUpiUCCOPzbjmcJKAu8duGXGSCOzlO8FQ5hbIURMf8KaOu7cnVyX24d8kPyXrMvhX0FWEt-YiHXgLslY7xe9Z6en8b-79iVCcFC-ZHncJhKJjuU2D6uPODQ92ULBzkUiQi7JXK91PG0OvDOgcyQiz6SkNgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66401" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66400">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jboJG7acmEP_u1KFMfuX0uBr999eA34yWz50zL3vhLu4Hh5ZXx5Dasz8qTblg-oCeBY6CifZaPWIqMNqNjcJpiEArficogGLY0q0UyzaC8M3o8-Sg4I-UjOE1woKGus6YxPNVTqBiDcWqrXRKarDIcSFiPQzhuka1p2vRbpIovpol_knLlb2sUK4WtOocleehMqHhaV5nsk7NKsERHIHAjbTWJ8GeIoqQdWIZWhQDXbWXmLoHc3rj3ss7dYXu-JtQ_m7tmSEMTWOT3CM5lSPsNVIJEdSSN_UWMrMOFiruEWsGzlgtzOkiDtFCOB6RLz2kB-H7dtQDidjl3-_wDRVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/66400" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66399">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
متن تفاهمنامه جمهوری اسلامی و آمریکا:
🔴
1⃣
توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
🔴
2⃣
هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
🔴
3⃣
توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
🔴
4⃣
ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
🔴
5⃣
ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
🔴
6⃣
ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
🔴
7⃣
ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
🔴
8⃣
تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
🔴
9⃣
ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
🔴
🔟
تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
🔴
1⃣
1⃣
صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
🔴
2⃣
1⃣
دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
🔴
3⃣
1⃣
یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
🔴
4⃣
1⃣
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66399" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66398">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛بقایی سخنگوی وزارت خارجه:
تفاهم‌نامه به‌صورت الکترونیکی بین پزشکیان و ترامپ امضا شده. جمعه هم خبری از مراسم رسمی نیست و فقط هیئت‌های ایران و آمریکا به سرپرستی قالیباف و جی‌دی ونس تو سوئیس دور اول مذاکرات فنی 60 روزه برای اجرای تفاهم‌نامه رو شروع می‌کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66398" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66397">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
سخنگوی وزارت خارجه جمهوری اسلامی: متن توافق با آمریکا نهایی شده و به امضا رسیده
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/66397" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66396">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=GggZhE6c_yuJXSfy31nDHL8itSJiPjvvlowC8rsYdssGC-KIb3BaEOnH_dJFFaFKEmlDn2spPQfzaE5qH33oSsmqMb7cu6Q7dzs3UVs0kfT_13YMI8X77GJDcK4rtVQWAf00NLAC-3BHagEHluPqgcavlkS8DF52NLcj4swtA9rwsjuzHRt59fFgJ8ygFZHIaCtN28mX-IXho_bXvoO7yhfK8VAyLT39baXWpKo1pbipY895rwLAEFFNkbCewYQ2NMzT5Vfjgndjc_M2Ij9hbCoFobw5yVvtaZvSRM3ZCXrt06YRW_dEjsUVgByV5vwbi2ohu2_HZ5xyOlMzbsudQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=GggZhE6c_yuJXSfy31nDHL8itSJiPjvvlowC8rsYdssGC-KIb3BaEOnH_dJFFaFKEmlDn2spPQfzaE5qH33oSsmqMb7cu6Q7dzs3UVs0kfT_13YMI8X77GJDcK4rtVQWAf00NLAC-3BHagEHluPqgcavlkS8DF52NLcj4swtA9rwsjuzHRt59fFgJ8ygFZHIaCtN28mX-IXho_bXvoO7yhfK8VAyLT39baXWpKo1pbipY895rwLAEFFNkbCewYQ2NMzT5Vfjgndjc_M2Ij9hbCoFobw5yVvtaZvSRM3ZCXrt06YRW_dEjsUVgByV5vwbi2ohu2_HZ5xyOlMzbsudQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
به محض اینکه آتش‌بس برقرار شد، دیدید که دشمن در خلیج فارس اقداماتی انجام داد و ما بلافاصله پاسخ دادیم.
آخرین نمونه آن حادثه مربوط به بالگرد آمریکایی‌ها بود.
علاوه بر این، دو ناو جنگی دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند - موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن برخاسته بودند، هدف قرار می‌گرفت. همه این اتفاقات در حالی رخ داد که ما همزمان مشغول مذاکره بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66396" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66395">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=Ckps2UvQV8UPlPdhB191pj9qkcToL0PLAo9XIsjQDYgRiVB-u9lLy6GvBRknP3o0VLocOccBiF2nCFIh6hUwmnI3Yp2NQtRvdJVFOtuepOjfjqAVY-bArkP0RQeZwmJwYgz26_wnMUmH3z1kF4pYK2qfL_1Q5o7v3fq-I782RfS66gFWY2c2w2L-GTzbQXbYVbkyXrPX7FUiYJ-bHaxzWfnkMpMnfeycQ9nN2yDw3FKdkQdW-H3PqV2PMWxWU41JgQuXoveUeWScTY0Kj89HwqZodiBuPr7ofaN75LlizKkq3Cu1kL6T72TYEuKeUEs-7xth0fIWyu80ML4JfXz9ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=Ckps2UvQV8UPlPdhB191pj9qkcToL0PLAo9XIsjQDYgRiVB-u9lLy6GvBRknP3o0VLocOccBiF2nCFIh6hUwmnI3Yp2NQtRvdJVFOtuepOjfjqAVY-bArkP0RQeZwmJwYgz26_wnMUmH3z1kF4pYK2qfL_1Q5o7v3fq-I782RfS66gFWY2c2w2L-GTzbQXbYVbkyXrPX7FUiYJ-bHaxzWfnkMpMnfeycQ9nN2yDw3FKdkQdW-H3PqV2PMWxWU41JgQuXoveUeWScTY0Kj89HwqZodiBuPr7ofaN75LlizKkq3Cu1kL6T72TYEuKeUEs-7xth0fIWyu80ML4JfXz9ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏قالیباف:
نه تنها خودم برای حضور در تیم مذاکره‌کننده داوطلب نشدم، بلکه واقعاً از پذیرفتن آن هم اکراه داشتم. پیش از قبول مسئولیت مذاکرات، هر کاری از دستم برمی‌آمد انجام دادم تا این مسئولیت به من واگذار نشود.
یکی از دلایلی که نمی‌خواستم این مسئولیت را بپذیرم این بود که دونالد ترامپ طراح، فرمانده و ناظر ترور قاسم سلیمانی بود.
سردار سلیمانی برای کل جهان اسلام عزیز بود، اما برای من به‌طور شخصی معنای متفاوتی داشت. آیا فکر می‌کنید برای من آسان است که با چنین فردی بنشینم و متنی را نهایی کنم؟
با این حال، وقتی دیدم هیچ‌یک از مسئولان فرد دیگری را پیشنهاد نمی‌دهند و پیشنهادهای خودم هم پذیرفته نمی‌شود، مجبور شدم وظیفه‌ای را که به من محول شده بود انجام دهم.
ما قرار نیست فقط کاری را انجام دهیم که دوست داریم؛ بلکه باید کاری را انجام دهیم که وظیفه‌مان ایجاب می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66395" target="_blank">📅 23:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66394">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=skJd_3wpXs_CAPEeAKHC0XzfOs83382Av6kndeQhNeMbbKhtbQjzOtbbnTDd5vTQp0nUC-ba-63Mm0ziB4siG5VgCbGGB90d9Jns1ODh26odwVe800c_I1cDKlrt3dyPD2F0WzSkG4nWEmVy0mQT9Y3HBsk5loNI4vMppHoH4XkWT2dzcCT3CyStAMbW1hrcIK0rZ2PMWAHdd_N81wCKgQwirQcH8SDqKJNbsQwN6c-1YTMBKwJbEezteV2K3ahBhpuzFtvyZhP2TzBiLulufKvSq26_GmDVu16ugWmaj5Y0Epk5IYNjVRwDRIKNfLnHWScImKokszKo9dUaJKxyyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=skJd_3wpXs_CAPEeAKHC0XzfOs83382Av6kndeQhNeMbbKhtbQjzOtbbnTDd5vTQp0nUC-ba-63Mm0ziB4siG5VgCbGGB90d9Jns1ODh26odwVe800c_I1cDKlrt3dyPD2F0WzSkG4nWEmVy0mQT9Y3HBsk5loNI4vMppHoH4XkWT2dzcCT3CyStAMbW1hrcIK0rZ2PMWAHdd_N81wCKgQwirQcH8SDqKJNbsQwN6c-1YTMBKwJbEezteV2K3ahBhpuzFtvyZhP2TzBiLulufKvSq26_GmDVu16ugWmaj5Y0Epk5IYNjVRwDRIKNfLnHWScImKokszKo9dUaJKxyyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
لبنان بخشی از جبهه مقاومت است. طبق توافق، ایران از جبهه مقاومت حمایت می‌کند، در حالی که ایالات متحده حامی و متحد رژیم اسرائیل است.
بنابراین، طبیعی است که وقتی آتش‌بس برقرار می‌شود، باید در همه جبهه‌ها، به ویژه در لبنان، رعایت شود.
باید از مردم عزیز لبنان، به ویژه شیعیان و حزب‌الله، که در طول تجاوز آمریکا و اسرائیل به ایران ایستادگی کردند و نزدیک به ۴۰۰۰ شهید تقدیم کردند، تشکر کنم.
در حالی که ما در شرایط آتش‌بس بودیم، آنها به جنگ ادامه دادند و همچنان تلفات دادند.
وقتی رژیم اسرائیل ضاحیه را هدف قرار داد، ما ایالات متحده را تهدید کردیم و اولتیماتوم دادیم که خواسته‌های ما باید پذیرفته شود؛ در غیر این صورت، ما پاسخ خواهیم داد.
ترامپ مجبور شد در شبکه‌های اجتماعی پست بگذارد و به نتانیاهو بگوید که حملات باید متوقف شود و دیگر نمی‌توان ضاحیه را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66394" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66393">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=YHPmrhTxkCqL0ptH_cRHtzY3AO0-jsUa0S7pAw9p8qZgqB7QGkoxZmjK2JbKeRt-fCgmzgxzq_PAErkWF8DldSTkjcxHsFagN1IbJx9BY3lADoBiA07xFRE7-68bNe6QcPB4MlAIwaWf-MAxmv-2e-oLGIU-lzmcPTAD3TjWDIIWgrV5YOxnC_Jec-wFXnFZRo64-hTXAaa741RGO4PWlRYAHio5i0ZAEl9kmH-f9d9mOZYPefu4cckDMZEurOpNN3_Dkg5bmPncSsqAweTSztqV-HdGGWCWxpjBTiu4Dgql5PB4ooNRzh23Ks3GVMN7Tt_HDF9tmc4D6a1SKJ26yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=YHPmrhTxkCqL0ptH_cRHtzY3AO0-jsUa0S7pAw9p8qZgqB7QGkoxZmjK2JbKeRt-fCgmzgxzq_PAErkWF8DldSTkjcxHsFagN1IbJx9BY3lADoBiA07xFRE7-68bNe6QcPB4MlAIwaWf-MAxmv-2e-oLGIU-lzmcPTAD3TjWDIIWgrV5YOxnC_Jec-wFXnFZRo64-hTXAaa741RGO4PWlRYAHio5i0ZAEl9kmH-f9d9mOZYPefu4cckDMZEurOpNN3_Dkg5bmPncSsqAweTSztqV-HdGGWCWxpjBTiu4Dgql5PB4ooNRzh23Ks3GVMN7Tt_HDF9tmc4D6a1SKJ26yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
بدبینی و بی‌اعتمادی من به ایالات متحده از هر کس دیگری بیشتر است.
حتی اگر توافق نهایی حاصل شود و توسط قطعنامه شورای امنیت سازمان ملل متحد تأیید شود، باز هم قابل اعتماد نیست. تضمین ما قدرت ایران است
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/66393" target="_blank">📅 23:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66392">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb769475.mp4?token=EDSz8vcL7u9QFuqgBSzACx_jHP4q6Bhg41sdxfFfWLca0IPZelxpN5lkOf7DA_Ezr-l2mzVJ3aqFGmF5xRLD5ZjyV6wuYLtR_tfP67v93hgJ1JWe3HZL-J8Wx1Nt1Fzow7LeHA-9NtdxYEN1xWhdIKVWpPiStRAxHEQd-R-krma0NnE1yeE-35lN3Hmz3Q6yHW8H3LGPwPs-et3a6V8_9yfoEnuWO3Pbo3fIYUMQFKWQhOnCwqO7z9BSr0el_YbjHry2aLCUqDEZAq9q5nM3X9YLUrgCg00Dx9LSMM0Tc7frWy8g4TGgG9XfuoGRCofmjRC7wvpFq3ve11k-AqlO-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb769475.mp4?token=EDSz8vcL7u9QFuqgBSzACx_jHP4q6Bhg41sdxfFfWLca0IPZelxpN5lkOf7DA_Ezr-l2mzVJ3aqFGmF5xRLD5ZjyV6wuYLtR_tfP67v93hgJ1JWe3HZL-J8Wx1Nt1Fzow7LeHA-9NtdxYEN1xWhdIKVWpPiStRAxHEQd-R-krma0NnE1yeE-35lN3Hmz3Q6yHW8H3LGPwPs-et3a6V8_9yfoEnuWO3Pbo3fIYUMQFKWQhOnCwqO7z9BSr0el_YbjHry2aLCUqDEZAq9q5nM3X9YLUrgCg00Dx9LSMM0Tc7frWy8g4TGgG9XfuoGRCofmjRC7wvpFq3ve11k-AqlO-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
ما بر ایالات متحده و رژیم صهیونیستی، که قدرت‌های نظامی پیشرو در جهان هستند، پیروز شدیم و اجازه ندادیم که آنها به هیچ یک از 9 هدفی که اعلام کرده بودند، دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66392" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66391">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=iBoxZ11SZzLuFPQEDrrhJfTAonhxNtEYmK44LHDR3MNLd8uTUxn51fTXZXXFgmEUF08nRlCsxNuFss4nT9YUm3MVKMn8LpyUmCH0sTUBhLlnjLnQpJ9jaIdxzlh_rT1Vd45c3uFIJfErTU2InRZtN51bsOELv_YTXOrVhlz_T0pJX4fih-6SbaAx9QyYkDtfAtq1GOPQO4GT0QCWKTYSE9glu0wAw-HIxqh0WZwA3f988oIvtkR4SJpVWnjP8c2p9nBqaDaVqvqTI99FVBdpOB_9GC131xlFPtKw9HTr8ZXcbNmQrKihlFTYec186Tne9h8Rg7hHqN1do0C_ZH7inA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=iBoxZ11SZzLuFPQEDrrhJfTAonhxNtEYmK44LHDR3MNLd8uTUxn51fTXZXXFgmEUF08nRlCsxNuFss4nT9YUm3MVKMn8LpyUmCH0sTUBhLlnjLnQpJ9jaIdxzlh_rT1Vd45c3uFIJfErTU2InRZtN51bsOELv_YTXOrVhlz_T0pJX4fih-6SbaAx9QyYkDtfAtq1GOPQO4GT0QCWKTYSE9glu0wAw-HIxqh0WZwA3f988oIvtkR4SJpVWnjP8c2p9nBqaDaVqvqTI99FVBdpOB_9GC131xlFPtKw9HTr8ZXcbNmQrKihlFTYec186Tne9h8Rg7hHqN1do0C_ZH7inA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
تفاوت بین مذاکرات فعلی و دورهای قبلی این است که امروز دانش و دستاوردهای پیروزی در میدان نبرد به عنوان پشتوانه دیپلماسی عمل می‌کند.
در مذاکراتی که به عنوان نوعی مبارزه انجام می‌شود، نه تسلیم وجود دارد و نه شعارهای توخالی.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66391" target="_blank">📅 23:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOZNjC9SiIouc4vjrk604-cgYf8opleaDc4qNV4Zt1lJb9ZyjIYXQ2Jbw9UnkjH15LCRAWAMT53ymJdzSWHkUzA2nPMb0V6UwaZJ6xxXacelUNDHGe08CymU9mWOS1Ttzem3eO2yke_lw7R4i_CfJqNUIwGMzf5az_4zZr4DsjUM0RKeDYBiXlFOORI3Yx69GgBGr_D7sFGEOPPNNSszq5ZKX7rWQvs9AGrQjVDwMNP8smBYnY_mBWce3QS57_ROylS6iREtOqylCy2z4xLU663U8RnfHyQsG6dShlfJL4jGVKdNdovttDy_V0sC_csYvfr6cJY_aClb-KHAin2FzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شبکه خبر:
مصاحبه اختصاصی رئیس مجلس درباره تفاهم‌نامه پایان جنگ تا دقایقی دیگر
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66390" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66389">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=RcX2zRICNTAIcJ8rurgeyZ2pmcJs_F1e55kGBHknOm3hkfr0z9nSRl5Lq_pgb-lgAH1_8yCWiQJnkqNrJvfd6Q5nl82WQ_QRTCh0iAfZRFB0Yi_AQufbJ5lVsBp4_qAV_w1BieJsi3Qm5XI6taCL75UXh9SWwykIlFTKtaTIMWt4VOwNGjBtMPR7-8-YxEZXM5ChXUYE_nMZSFKjuR62Gpr8tmMIJveWcFQ6XL1RMoUs2yk2h1eJQB8hQ6gHfTubb3tpReP-j5jSX4hL5r_hukNAwpgO0kAEF3tHhwwJn9_HY07Z9zlLa4h1Dg8VU87z5bAif6CqecKl0fdp5cA2Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=RcX2zRICNTAIcJ8rurgeyZ2pmcJs_F1e55kGBHknOm3hkfr0z9nSRl5Lq_pgb-lgAH1_8yCWiQJnkqNrJvfd6Q5nl82WQ_QRTCh0iAfZRFB0Yi_AQufbJ5lVsBp4_qAV_w1BieJsi3Qm5XI6taCL75UXh9SWwykIlFTKtaTIMWt4VOwNGjBtMPR7-8-YxEZXM5ChXUYE_nMZSFKjuR62Gpr8tmMIJveWcFQ6XL1RMoUs2yk2h1eJQB8hQ6gHfTubb3tpReP-j5jSX4hL5r_hukNAwpgO0kAEF3tHhwwJn9_HY07Z9zlLa4h1Dg8VU87z5bAif6CqecKl0fdp5cA2Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی گسترده انباری در سن-سن-دنی، پاریس
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66389" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTsvtgaMrAoZK7CyMFsdbC0m2tzG0wKidLehPd94wITUdZ2OLaHYgIKRy2QBqRbis5MaqWOizB47EixDh-dTvQ1t-FvBlgUWUVLV9Y3gbGs8nqTlVwcudD8UdtgDDMn1eQP-kD0Hx_sbBccFTO59489R6BJc20bZnvdRVtC1GJzUqOZ08kqEHsx8bV-OnzPUT_ZA7yCKbcLmL_WGPXZcrIe-gomXMw5byLqd83g3HXHTBiAfHepYYblpyIGMHUiwlzQsPYLBxzI7ywFYlJ-IcJTM3d5ggdfm3b6ZdqwxvNuA7JJt9emDHx9jHZf95krrSss1gkRdDb1xGNYMjdHbvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیندزی گراهام: من همین الان یک بحث بسیار طولانی و سازنده با ویتکاف  در مورد ایران داشتم.
بعد از این بحث، به نظر من امضای تفاهم‌نامه برای ایالات متحده مفید خواهد بود، تا جایی که تنگه هرمز شروع به باز شدن کند و خصومت‌ها با ایران متوقف شود.اینکه آیا ایالات متحده می‌تواند در مورد برنامه هسته‌ای و سایر مسائل به یک توافق قابل قبول و قابل تأیید با ایران برسد یا خیر، هنوز مشخص نیست، اما من جنبه منفی کمی برای تلاش کردن می‌بینم
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66388" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=rafIiP2gWQIL1S73sRyfJCitxNbQR3AT7eqhPdt9Fz_bYFijWDuO0horZIjs9RxHGrc-3COFFS7sF0O5svBS_IJhpsYne2YexRYJB4hf7bpim6xJbCj1CrQdBwv9Fop4BnJKmpGeVdv02Pz86goz4p7qOGXklAx6NkkfYukjyIERCXprRYDc-p-6nupUKVLQ6kHaogwDSENyyfxjfbWO5_a603n3fuZbxTaCdgE9XoVbasuJukRAnHeuZ8IiTnq8vVQ6lmriM_higxFjPd5WbTrre5krj9Euv7gzXFEWwD1t7bl4PznCv439cl_o0NP6zqZVUPpkMAc0STkyIZjDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=rafIiP2gWQIL1S73sRyfJCitxNbQR3AT7eqhPdt9Fz_bYFijWDuO0horZIjs9RxHGrc-3COFFS7sF0O5svBS_IJhpsYne2YexRYJB4hf7bpim6xJbCj1CrQdBwv9Fop4BnJKmpGeVdv02Pz86goz4p7qOGXklAx6NkkfYukjyIERCXprRYDc-p-6nupUKVLQ6kHaogwDSENyyfxjfbWO5_a603n3fuZbxTaCdgE9XoVbasuJukRAnHeuZ8IiTnq8vVQ6lmriM_higxFjPd5WbTrre5krj9Euv7gzXFEWwD1t7bl4PznCv439cl_o0NP6zqZVUPpkMAc0STkyIZjDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف؛ آن روزی که من پا در میدان دیپلماسی گذاشتم گفتم:
من اینجا آمده‌ام که هم آبرو بدهم، هم خونِ دل بخورم و هم خون بدهم؛ اما اگر کسی فکر کند که از مسیر امام شهید، مسیر انقلاب و عقلانیت ذره‌ای فاصله می‌گیرم، هرگز!
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66387" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=CDhLRtLHpsn6-7nLTM2x5gfkRAKiagjKLvXe-fWNvC4pbJvAm45ySpMOKEgWyJHD-Hu5n0uDhRiJDGp7IYtY6kURy8tDL15-M5IOOJrd70Bm9-weY2_x1Tsi9_mPgyIooF-i7KBlXRwkU_DrwjOKjDn2QkKIo1ssUlap_faFlwPBjdGQUFv8Bz6qzABKnEnyxNJxZ_v2QCahs2mtihJ_cU-vbINjM2D6ozUlbNfFebUEEZSF3Yn9zY2qgI1KeTDcEj7YWt3i3sf3r9xT7QX3j71FX3rdnHHBVsIr9gQNsXE4972-ejQQ1hnqCfllolFvvKR8aeFRhqj5inYjv09OGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=CDhLRtLHpsn6-7nLTM2x5gfkRAKiagjKLvXe-fWNvC4pbJvAm45ySpMOKEgWyJHD-Hu5n0uDhRiJDGp7IYtY6kURy8tDL15-M5IOOJrd70Bm9-weY2_x1Tsi9_mPgyIooF-i7KBlXRwkU_DrwjOKjDn2QkKIo1ssUlap_faFlwPBjdGQUFv8Bz6qzABKnEnyxNJxZ_v2QCahs2mtihJ_cU-vbINjM2D6ozUlbNfFebUEEZSF3Yn9zY2qgI1KeTDcEj7YWt3i3sf3r9xT7QX3j71FX3rdnHHBVsIr9gQNsXE4972-ejQQ1hnqCfllolFvvKR8aeFRhqj5inYjv09OGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
وقتشه که سنگر رو از بچه های لانچر تحویل بگیریم و یه زندگی خوب برای مردم بسازیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66386" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=hxMwIfCPWbSstj3SgAeJWz4nomaJFXbtoaGSs1v2yzP6gPkK8QaXnpwCv49lA23G9T0BJbDJ8p8TgyuDW9NC2EugtmgN8CtaDSmulCGtDm5n9ywlr4qKbGh744fn3lvcjy8K_eSZECkJdddD4fY4QC9iFy7XNWcphLGK7o9yb-21vV2Nk1yTCiZOBMx98lDzuo1sI_OL83jjzH7E4NdiGpDliFw0n6w1t46DDocTOfQ8YZXddk256uniSo0FC4ZmM_7MHCqjeP0D2dwwZm8bNaDhTqMSRa61KjXYUrI346_5Eyl41QEcwlfNL2ofqzjoKI8WUhH0HkE-R6TlbDvzNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=hxMwIfCPWbSstj3SgAeJWz4nomaJFXbtoaGSs1v2yzP6gPkK8QaXnpwCv49lA23G9T0BJbDJ8p8TgyuDW9NC2EugtmgN8CtaDSmulCGtDm5n9ywlr4qKbGh744fn3lvcjy8K_eSZECkJdddD4fY4QC9iFy7XNWcphLGK7o9yb-21vV2Nk1yTCiZOBMx98lDzuo1sI_OL83jjzH7E4NdiGpDliFw0n6w1t46DDocTOfQ8YZXddk256uniSo0FC4ZmM_7MHCqjeP0D2dwwZm8bNaDhTqMSRa61KjXYUrI346_5Eyl41QEcwlfNL2ofqzjoKI8WUhH0HkE-R6TlbDvzNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد پرونده اپستین:
ما نمی‌توانیم فقط به این دلیل که فکر می‌کنیم چیزی اشتباه است، مردم را تحت پیگرد قانونی قرار دهیم.
شما فقط می‌توانید مردم را در صورتی تحت پیگرد قانونی قرار دهید که مدارکی برای اثبات تخلف آنها داشته باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66385" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66383">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه جمهوری اسلامی:
در یادداشت تفاهم ۳بار ذکر شده باید جنگ در همه جبهه ها از جمله لبنان پایان یابد.
همچنین بر حاکمیت لبنان تاکید شد و حضور ارتش اسرائیل با آن در تضاد است.ادامه اشغال اسرائیل از جنوب لبنان نقض تفاهم‌نامه است و اقدامات لازم را اتخاذ خواهیم کرد.
یکی از بندها تایید میکند که آغاز مذاکره و ادامه آن مشروط به اجرای تعهدات است ازجمله توقف جنگ که شامل لبنان هم میشود.جنگ بایددر همه جبهه ها از جمله لبنان متوقف شود تا مرحله مذاکره آغاز گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66383" target="_blank">📅 21:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66382">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=dcxA5bHNuWe_QkMS_81Ii6xIbvwnuxSXIGaRB0_CH4m9F4zPnxfi5oZP-pPcX1dh_UUX9DZz9_GarfQ2HMkYCTGoxEGQMH7E77HrHpl-KxqGCnbP69DHitIs574hG-vriW4jFX1L7zwK_YgoOEPv5QbXGjRbHEvpFyb0A17Oj1QuKGByGLqAPPwBDm8aHVpHu6wZbcfJatQoIiMtn3Nv2XqyzhHvrEwTOIEy5uioLrtp-x5NkW47ysmiX0qmg36LYsZs6YAJt98Z1DIcR5hy7kI3huJo714wJWzosG4GrWf9VclfHhgwiUAPiextL3HLHAIf1dHQjjO-6zTn7Tadvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=dcxA5bHNuWe_QkMS_81Ii6xIbvwnuxSXIGaRB0_CH4m9F4zPnxfi5oZP-pPcX1dh_UUX9DZz9_GarfQ2HMkYCTGoxEGQMH7E77HrHpl-KxqGCnbP69DHitIs574hG-vriW4jFX1L7zwK_YgoOEPv5QbXGjRbHEvpFyb0A17Oj1QuKGByGLqAPPwBDm8aHVpHu6wZbcfJatQoIiMtn3Nv2XqyzhHvrEwTOIEy5uioLrtp-x5NkW47ysmiX0qmg36LYsZs6YAJt98Z1DIcR5hy7kI3huJo714wJWzosG4GrWf9VclfHhgwiUAPiextL3HLHAIf1dHQjjO-6zTn7Tadvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره محمد بن زاید:
محمد در امارات متحده عربی یک جنگجوی باورنکردنی است.
هفته پیش بمب می‌ریخت، گفتم «کی داره این همه بمب می‌ندازه؟» امارات بود. او یک جنگجوی خوب است
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66382" target="_blank">📅 21:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66381">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTEc6h6TtthEmUqKZxJKMOWiWdtTz55HJeFsUkPBqw-JPnmnpqIwMiEkSxKAPgINjqW3zwftTez2nkY10rrFgK4oL8L5QkJ8Tmcv_Ce6_nL4eNeRjK6mZ7kokGUeAE2OfsRquv1CWQ5LO2Ft9KOahgpPSeklGTTU_VOxCPmxSobtus9n-3nCnkMw192EXf6H4g9P1h0zNSM-uSqzIKwGeKJr5FYOALj-muJU-THvhLvu_tJIainVOmQSJEP6yE6fMnjLhK6-bEqLAEnqptPGrJdKPz6Jrdys5A10pD5AfLBgiGfd8H8K43fU0-pc-vn44gZ_mFD4ZlWzRT8lypWRTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛الجزیره به نقل از وزارت امور خارجه ایران:
ما در حال حاضر در حال بررسی ایده امضای یادداشت تفاهم از راه دور توسط روسای جمهور ایران و ایالات متحده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66381" target="_blank">📅 21:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66380">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729c69207c.mp4?token=HM4uoM5-s5oWzlCcX6Lh7yiXCzwzfZNscxS-6S4NDiGhJP9dhTaNVo1IbwHK2H6YiH3sft_gurt8y92yyG4m7_kVOy13MpPUeubQiRTzWt_wv0IZroUTl2ZQVf87HF90ww94b30WcC1oq_84n8zDnwAZIwzfv6zC95YNlgxe2OkQ9p2rI8NmOnNkfm-buKYBnD5_pMUWcCJT8evUlhyUTLA2JiV20CwnK9nM6QDoUxgMfCQBvfColZz2tz6HBCj7tYMoA6WDrfvSEirPybHwqxsthS4QDpgF8YYr5wY9Wz5D1EWvS3E79dJyDt9hmYfAS3mcNG9wRKFoYfTIKZ9_ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729c69207c.mp4?token=HM4uoM5-s5oWzlCcX6Lh7yiXCzwzfZNscxS-6S4NDiGhJP9dhTaNVo1IbwHK2H6YiH3sft_gurt8y92yyG4m7_kVOy13MpPUeubQiRTzWt_wv0IZroUTl2ZQVf87HF90ww94b30WcC1oq_84n8zDnwAZIwzfv6zC95YNlgxe2OkQ9p2rI8NmOnNkfm-buKYBnD5_pMUWcCJT8evUlhyUTLA2JiV20CwnK9nM6QDoUxgMfCQBvfColZz2tz6HBCj7tYMoA6WDrfvSEirPybHwqxsthS4QDpgF8YYr5wY9Wz5D1EWvS3E79dJyDt9hmYfAS3mcNG9wRKFoYfTIKZ9_ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر آنها به توافق‌نامه پایبند نباشند، یا برخی موارد حتی در توافق‌نامه ذکر نشده باشد - این یک یادداشت تفاهم است، اما ما بدون نوشتن آن، از برخی موارد درک داریم - و، اگر آنها به آن پایبند نباشند، احتمالاً به بمباران آنها تا زمانی که به آن پایبند باشند، برمی‌گردیم.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کارهایی می‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66380" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66379">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
#مهم؛ پس از روی کار آمدن مجتبی خامنه‌ای به‌جای علی خامنه‌ای، #سعید‌_جلیلی نماینده‌ی سابق علی خامنه‌‌ای در شورای عالی امنیت ملی عزل شده و #علی_باقری‌کنی( برادر مصباح‌الهدی، داماد علی خامنه‌ای ) جایگزین وی شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66379" target="_blank">📅 21:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66378">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=PSyAQTe0O1vqYpQr14WxO6AlXkJSjm5sG-DkxiJfrKkl3o_pgTPivqj1ARCRFTp2DLB4ShHQT2gkFhQoQPWx-OKirXDwteSpJtwXz8OiBi_l34VvZnki4-ptA2KRl49FUPnNk00gIG-siqd3J8u6GlQyqjtTsxJxtHcYxVyTvVWDm9WJHfSR_mz45WvY7zkUCtu2HgDlR-2UCHuOG0-elc3J0HVpaE7s9jjyKj2VJhwTtCv0hh2nRRqPSZBwP5O2rEDclC9fEfQifuYDXVb_D2WFwGXdN6po2-PgQ2YnEsl5eSKF39Yck59JOPQzo2lnxro0hTp3GjHuBFDQMvo-ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=PSyAQTe0O1vqYpQr14WxO6AlXkJSjm5sG-DkxiJfrKkl3o_pgTPivqj1ARCRFTp2DLB4ShHQT2gkFhQoQPWx-OKirXDwteSpJtwXz8OiBi_l34VvZnki4-ptA2KRl49FUPnNk00gIG-siqd3J8u6GlQyqjtTsxJxtHcYxVyTvVWDm9WJHfSR_mz45WvY7zkUCtu2HgDlR-2UCHuOG0-elc3J0HVpaE7s9jjyKj2VJhwTtCv0hh2nRRqPSZBwP5O2rEDclC9fEfQifuYDXVb_D2WFwGXdN6po2-PgQ2YnEsl5eSKF39Yck59JOPQzo2lnxro0hTp3GjHuBFDQMvo-ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
مردم از من می‌خواهند پل‌ها را بمباران کنم.
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن ایران.
اما ما آن پل را بمباران کردیم، دیدید که
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66378" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66377">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=ql-vp2x3aucWJHm3i4zlG3i826j5uCCEns3FtTWvLAMtpnz3gQ2aaDyaBNrHGidQR2e_l0HKPh9-RUMwJi8jW0je9xsx68_Mw9UycgQ-eJu7gI2LMa9Napn_NsgzvbTDKwhnvk874hRmhuFne2mikE9UBQ3ck8g9hk1F19AOub8qsOzZiiJucKZCn4K2w0p5ufwbauVAb9JtTd9MmMunACvBVxjdVlOOihM3wtsgoQIsmJWGbwnab39HM6qH9MkVAsr7VrXQYUpvdgUC6x-_6cTES9Ebqsd8nsYxBcTpFcVKqDmtsO1VqgDXOEWCcTwR50J-5r2oDfIBbH0crtJGiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=ql-vp2x3aucWJHm3i4zlG3i826j5uCCEns3FtTWvLAMtpnz3gQ2aaDyaBNrHGidQR2e_l0HKPh9-RUMwJi8jW0je9xsx68_Mw9UycgQ-eJu7gI2LMa9Napn_NsgzvbTDKwhnvk874hRmhuFne2mikE9UBQ3ck8g9hk1F19AOub8qsOzZiiJucKZCn4K2w0p5ufwbauVAb9JtTd9MmMunACvBVxjdVlOOihM3wtsgoQIsmJWGbwnab39HM6qH9MkVAsr7VrXQYUpvdgUC6x-_6cTES9Ebqsd8nsYxBcTpFcVKqDmtsO1VqgDXOEWCcTwR50J-5r2oDfIBbH0crtJGiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
گسترش توافق‌نامه‌های ابراهیم چیز دیگری است که امیدواریم به آن دست یابیم.
و من فکر می‌کنم اگر عربستان سعودی پیشگام شود، لطف بزرگی به خودش می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66377" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66376">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=cCY-Jam8F6d3opQH1JyJwWyrzEFOQQCj5X2_fA24ye6aZCDidqrttRK4tUbhulP-JABAUyqhgbwif9o0pOVPhXwdSkAlx5dVphPL7gQ6MSyzDzI8jKwMojYCrSx2LqWgalFRaWbLKmXOWLfJJet6w6lBbY3223p6e5tahJAj4gS4ucBBkaOch6LF6Am3EZUP_F2ZNg29jUDERFa0ARMAnTVGerIyLUuT0qmqknqkiYNaKdKYNg6sWiQUSak3lTGiEkPXmBpNo4u3nU1f70GTcMKHADihJ5T2oJxSOKrxZS2wAEAqj3VDjy_JTus7YRdw7L71Ha1ZpXwWlm_fiYT_fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=cCY-Jam8F6d3opQH1JyJwWyrzEFOQQCj5X2_fA24ye6aZCDidqrttRK4tUbhulP-JABAUyqhgbwif9o0pOVPhXwdSkAlx5dVphPL7gQ6MSyzDzI8jKwMojYCrSx2LqWgalFRaWbLKmXOWLfJJet6w6lBbY3223p6e5tahJAj4gS4ucBBkaOch6LF6Am3EZUP_F2ZNg29jUDERFa0ARMAnTVGerIyLUuT0qmqknqkiYNaKdKYNg6sWiQUSak3lTGiEkPXmBpNo4u3nU1f70GTcMKHADihJ5T2oJxSOKrxZS2wAEAqj3VDjy_JTus7YRdw7L71Ha1ZpXwWlm_fiYT_fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد اورانیوم:
هیچ‌کس نمی‌تواند به آن دست یابد، بنابراین مهم نیست که ما این کار را به سرعت انجام دهیم، اما می‌توانیم آن را نسبتاً سریع انجام دهیم. هیچ‌کس نمی‌تواند این کار را انجام دهد. و اگر آنها این کار را انجام دهند، ما با موشک‌های پاتریوت به آنها ضربه خواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66376" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66375">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=kpZ1gJ1UlaGYi1bABZcqtHilSlkOId9lPIoT8aoZy-zNwMyOmwKqx40N-7WjBG6TviQlLBBWuvQ4dyGZm8pG2PDdB89nI_MoWtaEDZBqgKNLfjsfBBX8I8cESkHw_lJWGt3Pi2Z6fzJ1Cyk3qf_54msdWSqMQLpxDFIbK6ML3JT9EaxB8EeuUb_yXxcDLP-lvoIOSOJp-3tiu1mYHGgDMwxECF5h9GIrXzQmF5oOBVXyka8c8UGCvM6PbECN98qbi6ijBi9eXKTEO3CAhURTLXk20Gr1caiVMAUDQX1u4loIHg4BfqkEzGAq4gPkkSCi_KTbBkNVLLB0V21ABzDtdDey8BnxEjmfu69NAFUCF5WfxJaiUBO3PwubtCuGXSlHzOkYUYggXjAtjM-wJ5GTJTiPbdYh9C4JxdZf2VQwf3UixzrPytWz0H3QpMUJHd45iFE007mlt9fa_he_TySVR4RQzKJwOZy4uB6qQSJ1ZRvGMtN03CENIwo7ifrFJogU5Gaff3EcCsmppdW2mHk_uXfSgqwt83aW7dJD0Ttb0TR30WJuOs40hBxIAwIBrYNWva4FT6hpGX3VvvgEJfnMnTVEY-M-CigElksEn2i9gZY_VyWuEcbgHomoU1AMVLiAd6utD9cL3C9iJQ8tcHPtyOasto-p0Dtj0W7ieDn4LyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=kpZ1gJ1UlaGYi1bABZcqtHilSlkOId9lPIoT8aoZy-zNwMyOmwKqx40N-7WjBG6TviQlLBBWuvQ4dyGZm8pG2PDdB89nI_MoWtaEDZBqgKNLfjsfBBX8I8cESkHw_lJWGt3Pi2Z6fzJ1Cyk3qf_54msdWSqMQLpxDFIbK6ML3JT9EaxB8EeuUb_yXxcDLP-lvoIOSOJp-3tiu1mYHGgDMwxECF5h9GIrXzQmF5oOBVXyka8c8UGCvM6PbECN98qbi6ijBi9eXKTEO3CAhURTLXk20Gr1caiVMAUDQX1u4loIHg4BfqkEzGAq4gPkkSCi_KTbBkNVLLB0V21ABzDtdDey8BnxEjmfu69NAFUCF5WfxJaiUBO3PwubtCuGXSlHzOkYUYggXjAtjM-wJ5GTJTiPbdYh9C4JxdZf2VQwf3UixzrPytWz0H3QpMUJHd45iFE007mlt9fa_he_TySVR4RQzKJwOZy4uB6qQSJ1ZRvGMtN03CENIwo7ifrFJogU5Gaff3EcCsmppdW2mHk_uXfSgqwt83aW7dJD0Ttb0TR30WJuOs40hBxIAwIBrYNWva4FT6hpGX3VvvgEJfnMnTVEY-M-CigElksEn2i9gZY_VyWuEcbgHomoU1AMVLiAd6utD9cL3C9iJQ8tcHPtyOasto-p0Dtj0W7ieDn4LyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💥
پرزیدنت ترامپ:
هیچ‌کس سخت‌گیرتر از من نبود. هیچ‌کس سلیمانی را نشانه نرفت.
می‌دانید، وقتی من سلیمانی را هدف قرار دادم، مردم فکر می‌کردند این بزرگترین اتفاقی است که در خاورمیانه در ۵۰ سال گذشته رخ داده است. این بزرگترین رویداد بود.
او رئیس ایران بود و مورد احترام، اما او یک نابغه دیوانه بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66375" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66374">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=g5TuIcJuv9FCGEY8Va7mJq9uFw99fXmM8Rn7-r3gNP2oqRHKirzI3IcZ80B6TSG_O7OS7PT68KFAE3DlzeiMz78MmGXGqqi296FXa7aht-1WnJrA2z5cRlEOWeW4_1Um0zgB6APmTin-i5LMPw5omw6HSlRvpyP-awitDgyk4Nw3tmBJc6e1C2Ox89dgKgnkmH2sSE5n_EvT0OYmgehB62AAXeyIff3OsgjZDHWk4idmyYfBTsJHLT-lvaBtob80jOVpM0P_9WdBQFii9Vp_W0dzRVToGbxHSDDS0FjCh35gQAvMHiqKjzZJH0T3BJatiDAYVWF7v_5aM8n-dtGLYLB1GCAgsqV0BSh_KVosRnsaPi17fEkmu3SBbM5xRm1VBHD9j4Hh8zxW0nQS7a7S3v_o2r4-nFZV3zOspPkEuuv62gIv4CmcPXFKoFyKXroYs8XmP_H1qUOIPnabe1BnhXAbZHa8FHKA9hnzkFcdbKB3fwAG37gsmp4Q655An9O48pA4pnDhF4TF1ja14yZgw11nvG-OuXW6QPNf_l9gVcYazBZ6FRXWKI8iOdwuRGrfoDC2xuWI3wI1va8ujgeJB6feuMl8xlyIEu5PfHMoEGT9FUbeZ_a_pX6nXxtBjSkF01RlWQ-BkRG2ua57LYw5mqL4zmFVk6ZhLVLM6XREyuo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=g5TuIcJuv9FCGEY8Va7mJq9uFw99fXmM8Rn7-r3gNP2oqRHKirzI3IcZ80B6TSG_O7OS7PT68KFAE3DlzeiMz78MmGXGqqi296FXa7aht-1WnJrA2z5cRlEOWeW4_1Um0zgB6APmTin-i5LMPw5omw6HSlRvpyP-awitDgyk4Nw3tmBJc6e1C2Ox89dgKgnkmH2sSE5n_EvT0OYmgehB62AAXeyIff3OsgjZDHWk4idmyYfBTsJHLT-lvaBtob80jOVpM0P_9WdBQFii9Vp_W0dzRVToGbxHSDDS0FjCh35gQAvMHiqKjzZJH0T3BJatiDAYVWF7v_5aM8n-dtGLYLB1GCAgsqV0BSh_KVosRnsaPi17fEkmu3SBbM5xRm1VBHD9j4Hh8zxW0nQS7a7S3v_o2r4-nFZV3zOspPkEuuv62gIv4CmcPXFKoFyKXroYs8XmP_H1qUOIPnabe1BnhXAbZHa8FHKA9hnzkFcdbKB3fwAG37gsmp4Q655An9O48pA4pnDhF4TF1ja14yZgw11nvG-OuXW6QPNf_l9gVcYazBZ6FRXWKI8iOdwuRGrfoDC2xuWI3wI1va8ujgeJB6feuMl8xlyIEu5PfHMoEGT9FUbeZ_a_pX6nXxtBjSkF01RlWQ-BkRG2ua57LYw5mqL4zmFVk6ZhLVLM6XREyuo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ :
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آن‌ها بسیار کمتر تندرو شده‌اند. فکر می‌کنم آن‌ها خوب هستند و واقعاً کشورشان را دوست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66374" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66373">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=mY2pRtF9eztwNkCbCLktnTAS7w5FRAlgZfqptuf7q59SNq0bttkZ32Gb7WKjhNIqS8IW6bJDMtMMuw3Awmd8F8wODoEStGhDNuIjowdjiSqG1f8jWC4OB8rZjbSCumGm3_-OHu1h8YUJ8_NpacQey-jxrxVODTdtf_KuMtXCY8Os9Qpg95ynL4o8yW1kmQjFQ_t0LIPfUqEiGGowYenXo0fPJn2_rZ08VJc19N9UKh52SGKISMqNW856rm5923dUoDnOe84wYDMMwWbBmhQ9tN8vET7ohMuNY0eA5GkcQKGrIDjxfpUNZ47iK1yW55DZkpPkXhpJO3v0ZBV-yXsWSFSF9GddsqpJiPSDzxrR7bVvogFNGSXhST5RRb-ScyFrFi6DDjSYe1LvVzKplwskPKSsnLdBRGAuaP1If6DRQhpoGfVkfRc_So4ZSqdxc0-xXUaplbxY5Cij7Lprh0HoY6eu1TQ1GiZ1HIbexr5fv_9pCPHicdlzqeYhh4zBfNcjIcd9E_Lko73gOzS_M_HvL3FJFGv89WlubwulAA2wzyT7td7Qpqi11SXUM6CgcGYSY9b3HYw1hQ4GZsme3MTEGiu-kc76xYAxXlI2pN4IkxOn1BpO--Kwu-ZR7LJhpcY4Yf-h3utzQmKcG0Cg-PmYCcnhToKnlrtGj_Gsz--Bsn8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=mY2pRtF9eztwNkCbCLktnTAS7w5FRAlgZfqptuf7q59SNq0bttkZ32Gb7WKjhNIqS8IW6bJDMtMMuw3Awmd8F8wODoEStGhDNuIjowdjiSqG1f8jWC4OB8rZjbSCumGm3_-OHu1h8YUJ8_NpacQey-jxrxVODTdtf_KuMtXCY8Os9Qpg95ynL4o8yW1kmQjFQ_t0LIPfUqEiGGowYenXo0fPJn2_rZ08VJc19N9UKh52SGKISMqNW856rm5923dUoDnOe84wYDMMwWbBmhQ9tN8vET7ohMuNY0eA5GkcQKGrIDjxfpUNZ47iK1yW55DZkpPkXhpJO3v0ZBV-yXsWSFSF9GddsqpJiPSDzxrR7bVvogFNGSXhST5RRb-ScyFrFi6DDjSYe1LvVzKplwskPKSsnLdBRGAuaP1If6DRQhpoGfVkfRc_So4ZSqdxc0-xXUaplbxY5Cij7Lprh0HoY6eu1TQ1GiZ1HIbexr5fv_9pCPHicdlzqeYhh4zBfNcjIcd9E_Lko73gOzS_M_HvL3FJFGv89WlubwulAA2wzyT7td7Qpqi11SXUM6CgcGYSY9b3HYw1hQ4GZsme3MTEGiu-kc76xYAxXlI2pN4IkxOn1BpO--Kwu-ZR7LJhpcY4Yf-h3utzQmKcG0Cg-PmYCcnhToKnlrtGj_Gsz--Bsn8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پرزیدنت ترامپ:
روز یکشنبه، ما به توافقی با ایران دست یافتیم که به همه چیزهایی که در نظر داشتیم دست پیدا می کند - همه چیز و خیلی بیشتر. جلوگیری از دستیابی ایران به سلاح هسته ای همه چیز در مورد همین بود. این حدود 99 درصد بود. آنها نمی توانند آن را توسعه دهند یا بخرند. آنها هرگز نمی توانند سلاح هسته ای داشته باشند
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66373" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66372">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/66372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/66372" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66371">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsPWwzMscgTeqe0wDGTapagM9rgxVMBkwQgZXqQeEqCEjhzkLUHPCYt3KWskb0SUTT59R6qutEMlC7Cbpc5rJRYxc-s9YGcfuhf64e80p4kI2EJScEMab2NzEZcj_OQvadydE7FQn-a05EKEhyifGl-KqVcHNKtwSwXbd_ajKNrlFxYDPGx2JnsALKxSvX1KK-YfeEYr26fKI3InpCn9NzPqGmdf7dw8yOP9ERUl9dbcQkHifDa1zeI5VhtRRHsdZLaRiKooOckJ5qTsn7YIXUGpJQTVPYMLZ7G-n2D1M7fjlmRmyI3-fvElGUZzeAmugw9hxJzbCzSbT7LUYEZ3yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66371" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66369">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQVY1cHQuB4ZLliiwbdIOE4EAT8H5Cb8nmOS1cWPNEqmlpVplNtRufsTKOCeBt7uTXc7RKsGbdRnjicWzisCQYlaOo4Uuxi-a3C8htVc8QTU3_qaHpG5oJHysaRvEksJpOsu7pqIWrkefwBSHsfAOeSdKCCJBnBaClCfpG5DLZcufkWBVu1cEKXx9hNnHrDFyIT-L208JFgkLl9DcSsKHOpoHiOPY3N4L4EdVy9WL1KwIJxPX_AsPg4pW0DL0gGp_SSiV9WQspZb9G5I3aIyU40M0dBuV7IuyEyIygI1A-BIOAOb5oeyrdfOvFN-h3yH0jQK4JoYSDTZSD_lLXwhgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توییت قالیباف:
تعهد ایران به همکاری برد-برد که بر پایه مشارکت استراتژیک جامع با چین بنا شده، قاطع است.
در جلسه‌ام با اتاق بازرگانی ایران تأکید کردم: ما مصمم هستیم که اجماع استراتژیک خود را تحت GDI به نتایج عملی تبدیل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66369" target="_blank">📅 19:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66368">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53224e4497.mp4?token=iBFYU_BMtimyrxeARs5UzGLGOqkkJfNGnsGGraL2GAkVGxkCQwNoxu3pCeRGOW1WRG3cy09IQTuUDRN1MGRt75PD43KGGxxxBjDsDmw4eCzweeF_7ah6wyuFflJbGRrJPgLQWXxT9OTd21YQRALudf6BmkFBErMjoI6UdP1tG29BQb7O-u871DOY1_t4Wr56stNgLrP8fhHOzTt9AuVOuaaA2SW1jDNYvza2ftJ_DmHhv226zy0Jkj6uiKKVjnZZkWYoNPY_TRWEa9nkF27sD_XJ_5SYhZTqDG7LK3ScputsUqIC94rkeBIZoAAzX6LPH9EsLOAmo_tdHNGk1MCOpB5uhHMse79LGL5X-DMqgSXjXTkHF58zLjiBMIf_xRR2vwwhTIV4CwzmOx4TyGVch5auJKSs8Cce8rkII9D7dELET9Ishyq_kiwZtK8jDmv9kc4SWiDsPUm7nQQZkbs-d6njZ0axIzbVBbYpy80LOVMZL7ssbAgyfyNQVbcc3fECalvXV8pw3UvZ7ee-6TrRY3L8pozRtx_nR4mSeS8j9N16p4if8G-y3mrj4Q08HPxmWOuz6KCpfuPmS_fanhBLMYLJrufitAGJp9AKHr2eHvnwDIlzjh53AesaC5_smjUQJBl3Sec-aTUq_sk_BumWXSQkOwCoJUd3rW8jkJ8y9t4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53224e4497.mp4?token=iBFYU_BMtimyrxeARs5UzGLGOqkkJfNGnsGGraL2GAkVGxkCQwNoxu3pCeRGOW1WRG3cy09IQTuUDRN1MGRt75PD43KGGxxxBjDsDmw4eCzweeF_7ah6wyuFflJbGRrJPgLQWXxT9OTd21YQRALudf6BmkFBErMjoI6UdP1tG29BQb7O-u871DOY1_t4Wr56stNgLrP8fhHOzTt9AuVOuaaA2SW1jDNYvza2ftJ_DmHhv226zy0Jkj6uiKKVjnZZkWYoNPY_TRWEa9nkF27sD_XJ_5SYhZTqDG7LK3ScputsUqIC94rkeBIZoAAzX6LPH9EsLOAmo_tdHNGk1MCOpB5uhHMse79LGL5X-DMqgSXjXTkHF58zLjiBMIf_xRR2vwwhTIV4CwzmOx4TyGVch5auJKSs8Cce8rkII9D7dELET9Ishyq_kiwZtK8jDmv9kc4SWiDsPUm7nQQZkbs-d6njZ0axIzbVBbYpy80LOVMZL7ssbAgyfyNQVbcc3fECalvXV8pw3UvZ7ee-6TrRY3L8pozRtx_nR4mSeS8j9N16p4if8G-y3mrj4Q08HPxmWOuz6KCpfuPmS_fanhBLMYLJrufitAGJp9AKHr2eHvnwDIlzjh53AesaC5_smjUQJBl3Sec-aTUq_sk_BumWXSQkOwCoJUd3rW8jkJ8y9t4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
معامله‌ها شگفت‌انگیزند. من تمام عمرم معامله کرده‌ام. وارد معامله‌هایی شده‌ام که صد درصد قطعی بودند، اما اتفاق نیفتادند. وارد معامله‌هایی شده‌ام که هیچ شانسی برای انجام‌شان نبود، اما انجام شدند و به آسانی انجام شدند.
پس هرگز نمی‌توانی درباره معامله‌ها مطمئن باشی. اما خیلی زود متوجه خواهی شد. فکر می‌کنم انجام خواهد شد.
آنها می‌خواهند امضا کنند  می‌خواهند به زندگی عادی بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66368" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66367">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=Ci3cxV9XxPL6CYeXHFhcDN6oceMNDL6dmuMw1VwaZVMq4V4GPOQ7BmvcXsIsiKVqzqmqBzu1wUOZCwK1NTq7DqJ3w0r1k8eftg6lbl7h_LLGYTbVw5j20unCJQt5L0p4bbVHnOTtgaDdJGt_IKlM9pVuCr5BuRxVJTSxS53WgQzcHhIs3RyOZG6omm6CmZgNpMTC6vuw6OPiGipfZPd0UxpRrVJJlppJYqgRaQJOB6yC27meWzqsO4IdLNjXtsqD82Gyb3iczm6mD15UzHiI-Uq6AEYBeG-9ckCJ9i07pM6VpkfuZP6OR6etajz3WpEC3aAFSztTmZgpbs5HEhmjhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=Ci3cxV9XxPL6CYeXHFhcDN6oceMNDL6dmuMw1VwaZVMq4V4GPOQ7BmvcXsIsiKVqzqmqBzu1wUOZCwK1NTq7DqJ3w0r1k8eftg6lbl7h_LLGYTbVw5j20unCJQt5L0p4bbVHnOTtgaDdJGt_IKlM9pVuCr5BuRxVJTSxS53WgQzcHhIs3RyOZG6omm6CmZgNpMTC6vuw6OPiGipfZPd0UxpRrVJJlppJYqgRaQJOB6yC27meWzqsO4IdLNjXtsqD82Gyb3iczm6mD15UzHiI-Uq6AEYBeG-9ckCJ9i07pM6VpkfuZP6OR6etajz3WpEC3aAFSztTmZgpbs5HEhmjhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار: آیا می‌خواهید اروپایی‌ها مین‌روب‌ها را به هرمز بفرستند؟
ترامپ: ما به آن نیاز نداریم، اما اگر بخواهند بفرستند، خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66367" target="_blank">📅 18:33 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
