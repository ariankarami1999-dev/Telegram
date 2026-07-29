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
<img src="https://cdn5.telesco.pe/file/YY4PXxtnkFfUcBm438lPy88QxJ3ZB-XJtLVlCG_lRKQSEBd2FqDRQcc-sUXUprEtIgE3MPjP0iwB9cN8eDkvkwCzqFeArgeuUOnYLwvzOi6YEDTSjuj4SPH50psm_53PwGglGnnpbSH8ohTwHkmMrMP02yMWvr_BLHtnjeoaqL9fptQo6W4XhdQBz_xVMYlEPODUDd4qYDYOyEZUm2_CSVAd8NkmRKga-_tnE7fcZ8BSOoDbd6nekoCjqABj7ziGRuUxQvizQvjK0BXixec0B73jzrED1j8WbdybKgOYetKlH04szBqXt_Z-x9EEeNQpBaHjKN5TKwAMw0tjzp2xZg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 516K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 11:32:26</div>
<hr>

<div class="tg-post" id="msg-102225">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if7OArxvbxdfyf09eq-zoCgCpPfQTtIlRlqHtesszyQxSKEDJZMxv6_muof-40UQmhAUUlC3rFu3y13hQPN8xqFSgh24h03jGpsMPRtd-auhtbKybQ_96n5hhzbmLPYJ214VB0l8e292xf5kY3x52qd6Y0UFQ9Yx8lRgmE1oOzwMS5HtpytpT6ph3qR-_d62vVM3rN6caevaEBAph4ALf6_kRgppCLv9_zfPsJOfSfcJPRaDWekxiFJs72EHjANj2_aOaWP4PPljBkIg7Et3bg7QHEvs05WKI5bzeB84w8bhJUrsDjX3V4Kqm8GhCY1YyF5aeDYhIre3UYsG_ozaPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
▶️
رونالدو داره یه سریال به اسم "Day 1s" درباره پشت‌پرده زندگی و کار ایجنت‌های فوتبال می‌سازه.
غیر از خود رونالدو، چهره‌های معروفی مثل تیری آنری، دیمین لوئیس و یه رپر به اسم دیو تو این سریال بازی می‌کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.89K · <a href="https://t.me/Futball180TV/102225" target="_blank">📅 11:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102224">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s24POu1p364Fld25Gkpv31nag6jbOf5mA3wAktmghrf-XZcbF0vtkFUP2WUMcZkKhgEN3oUVEbbkboWw1ivOwrgrGB3R0EAHTSRaFJ-EayIalkq5khW83XmWnRX9lb0pnLZ1rDwwy6SYQ5rR8pDpUieNi5EA9Tb--eaE0fvS2gr4UuBCNBLngPu0kRjiBHmnyRWmA1KFDGsTpF0oY8DGTB-pZF8ZIdpuaGeZmoysApjES-bLPtScsrC6WeArJNc9K5iggC_x1BUYilglDqkGLbHfT0cixxb27jR3K29Pa2u-j98uz0kavQBp00X26-aFMwHB8bTGZO_-E1vYcWriNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب احتمالی فصل‌آینده لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/Futball180TV/102224" target="_blank">📅 11:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102223">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbgR0yK_UQq1pkMwkp2xltZUhOZ-3tY13-4gQbRWpfOxCDfnPVqFRXjr7Nb2hyqwCHJURT1QQDj0S5BRTa6Ue77lYKy6y-VNcWOtESgqmlI9gA6vjfLszc7oRn9mBGALKpQuPrnT1F_r18-aA93TJ1QtvK1d9FtopFcL5yCZAIZAIbVr8kwe9lhw6lRNqR2SF-n-gx33HwZ4OLBA0Vk2DofJVSnl0mOOKXiaENk0uSXobAc331mBzmz8K-8fiIMZ61_g7wMsgxV2hhPvxgp8epq51kkEl3cW42xLhriIjKKkGKZqGyiJ04yeXbaGmYbUFSy-NbbwQvoPtjX2MnjNqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
خبر فوری از فابریزیو رومانو: برای اولین بار و با موافقت فلورنتینو پرز، مذاکراتی بین رئال مادرید و منچسترسیتی برای جذب رودری در جریان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/102223" target="_blank">📅 11:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102222">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEdl9lTkuG0F0OMpka0GxT0O8KRRz_XvPoPb6pX84wy1ZzuQ3JaelnGC3MjDnZlcRV5mcATLAhhfGmBVVNsZzosv9XjTb1WRoglpTuJhRgp_-lhxR_QEe7Dqo3Ldlyiye3DLJ4IVRYJqp28529s9btZtFXQmIeXE6YbQ5ydUVsMa-6wBQf_rdpuZuhkSZWntwOmXrd-vQd99vifIa2mmC7R9k83CH70llXCJWON16EWelQushbEbxClQybyTBHNLZTikN7AsuzAGlS_xRzdfa2TWMkxTQ5FZQ8G_0Jwr67VMmDZ-EUGdBvKx7kZSgdUxpkcMLAR-IfcL2--HNJY2_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
💥
تعطیلات امباپه در کنار اکسپوزیتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/Futball180TV/102222" target="_blank">📅 10:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102221">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrQmflOXsXYL7rORrqGkv435A4QCEhey6U2q08qIzrcAcis7tRHIBdEyiHXOy8F8ONVFhDVmoxKxtIXNdDhkHXwQt5Smj1PLuXLm6ko-4K4eUsbNBF_4xFtd6jfrKcXbVfQ-2O14VBd0oFEdGZf4EkjkDwn_nPx-y8tGqyVRVCXL44Fj7giQ6bMuk9n7qLKko2o8f7T8l8i6FPCNX9zAoHc2V16qN-uHH9s8dzGO5XaiJdRtSaCvI52umSg0kXAuC3i7dqoS2l3E2egtznQNmy0dZJBEWR5f-qgDmDDjlN6GYQsArocFK1fgeNH_NeEVtpLj7kHKIPbP4NCKWqCgvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
6 سال پیش، هالند 20 ساله تنها 71 گل به ثمر رسانده بود، در حالی که در مقابل نیمار افسانه‌ای قرار می‌گرفت که در آن زمان 375 گل زده بود. این اختلاف 304 گلی، مانند یک پرتگاه غیرقابل عبور به نظر می‌رسید.
🤦
🗓
6 سال بعد، هالند 290 گل دیگر به ثمر رسانده و به رکورد 361 گل رسیده است. در همین مدت، نیمار تنها 84 گل دیگر به مجموع خود اضافه کرده است.
😳
یک ماشین گلزنی که به طور متوسط بیش از 48 گل در سال به ثمر می‌رساند، در مقایسه با یک نابغه که به نظر می‌رسد سرعت گلزنی‌اش به طور قابل توجهی کاهش یافته و دقیقاً 14 گل در سال است...
😭
و اکنون، در سن 26 سالگی، هالند کمتر از 100 گل با مجموع گل‌های دوران حرفه‌ای نیمار جونیور فاصله دارد – یکی از نمادهای بزرگ فوتبال.
🤯
واقعاً باورنکردنی است که هالند با چه سرعتی و ثبات فوق‌العاده‌ای گل به ثمر می‌رساند.
⚠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/Futball180TV/102221" target="_blank">📅 10:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102220">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=Ip_Ayb7f6LKOosE4c7AtiGRiN7Sol5YNcTKgVHbCs_CYn0elUXstMrh0VHmBtrmTkCz8ISycCf58TkBQKS58_ATZaL1lW11O6XTPe_5u0jyTFqdVPME9Fo-fcRiXfV-EfQFEaLoSU9nTa9Q2uE8E0vVyrJRv177Z3XOibBPPTvovt62wOAK2OTefedd9ApaqTjtNUmSbmMlOHrxy56yAfjTMQI9XXL0Yt-Yi6zH9cX8d-CD3_1ifqa1B5PEZa1V2oB48PM6dzJaSbN-VsCc4th0VKCTLbx9BGYqlu_lh6hEd4DLfa48E4l2XwGdewShy8svLOWPI3E9nzFxkOtc86A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f225d20c69.mp4?token=Ip_Ayb7f6LKOosE4c7AtiGRiN7Sol5YNcTKgVHbCs_CYn0elUXstMrh0VHmBtrmTkCz8ISycCf58TkBQKS58_ATZaL1lW11O6XTPe_5u0jyTFqdVPME9Fo-fcRiXfV-EfQFEaLoSU9nTa9Q2uE8E0vVyrJRv177Z3XOibBPPTvovt62wOAK2OTefedd9ApaqTjtNUmSbmMlOHrxy56yAfjTMQI9XXL0Yt-Yi6zH9cX8d-CD3_1ifqa1B5PEZa1V2oB48PM6dzJaSbN-VsCc4th0VKCTLbx9BGYqlu_lh6hEd4DLfa48E4l2XwGdewShy8svLOWPI3E9nzFxkOtc86A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مروری بر برخی گل‌های اسطوره کون برای سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/Futball180TV/102220" target="_blank">📅 10:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102219">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=lKmZymrPIkoNHjS9hyvDzhZQrv8tseePO4496JoFyV2l48Q7cMHfdizSjjMR8p68yECPaGTlLWotR0C2xtVKpS6-FnNfr0Hiofg19QslqUh-mqPIccH45gFjXUw1yPtkj4WMDr3hS_uzcx0_rxzKw2RjjG69jV_0vuV5J9k-HbxMmGpeBP9D67znfaE1bG0eBDNz7eOmcaJvN70QxvnENVkW3LtyS_XUudGzHxB0rU7Us5By1cfVEmhVf05nO6EIk67uzkvK78uAfzre5S-ljqNFaQcL0lTOJKmIlWyY8qKVQZ7sEXwgwIZXAzVyT-6Js4wY0WoA0aokaDtmJLllLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ef87c459.mp4?token=lKmZymrPIkoNHjS9hyvDzhZQrv8tseePO4496JoFyV2l48Q7cMHfdizSjjMR8p68yECPaGTlLWotR0C2xtVKpS6-FnNfr0Hiofg19QslqUh-mqPIccH45gFjXUw1yPtkj4WMDr3hS_uzcx0_rxzKw2RjjG69jV_0vuV5J9k-HbxMmGpeBP9D67znfaE1bG0eBDNz7eOmcaJvN70QxvnENVkW3LtyS_XUudGzHxB0rU7Us5By1cfVEmhVf05nO6EIk67uzkvK78uAfzre5S-ljqNFaQcL0lTOJKmIlWyY8qKVQZ7sEXwgwIZXAzVyT-6Js4wY0WoA0aokaDtmJLllLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا همه رو شکست داد جز ...
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/Futball180TV/102219" target="_blank">📅 10:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102218">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaW3RtUSN1vVrn-OXQkSxHYCRyGhw06O1cmjhc_4xID77rijl6j-SDOa5kW1Iqx7hBRrO3FxSUQO0jBwUkR1Mu-tV0xfgxpIGFDVTKfGQI4Q11GCKcxii_SAeYnFSZlY8dRmStTLXOrg7ge-5SzcPbSEfC8z9J7DrfU5JRu9Lb2-2Hj6CxCU3jmhGaZ9wnMfsvFG-BLF4PoAhAESxBJlc3bDZnQtZEKaYj_mnKmSwQ0mUQB3ALrb0IiF_inT0peFtsSvyFlU13Bc79GCoTT7isYcWG4jy2sm9zHf7WBjsBq4JqDGFgJpIFC1DCfsJPbJzzJ_gJyPXAdBnTh7oCJrMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
✍️
فابریزیو رومانو:
بایرن مونیخ در حال بررسی تمدید قرارداد با هری کین است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/Futball180TV/102218" target="_blank">📅 09:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102217">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=GgOlJrEMWjEkq-Qp5EQJXZJibfyhBieqaGL7GFn89cDbHc4boIK3cH2BWwq0uXjipuROi1AadrNGI5Tqanc2raSgRVtCxDfjIr01C3LSbuZ4mU30qurx-afa0V_7BEfxhw-icMfCGRYdMl9Gpgu0Djg92PN6oYtBqTkWGyxGB-8HRm3T8R0LRzWjJUUca_SdPlDsZCWW_8BmViJIIz9zts1Uvz35cjcviwgP_ZbUd_IObkmKvzCWw-xjmWVhefuhhG5gXBbOtsEXUMrvhOY9f3YMMIGSGpWMQwOTTejvE8LRssRdoju3_HKpiEsDP7KSO-9KDqki0m6l1jpqEAklwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5802c51b8.mp4?token=GgOlJrEMWjEkq-Qp5EQJXZJibfyhBieqaGL7GFn89cDbHc4boIK3cH2BWwq0uXjipuROi1AadrNGI5Tqanc2raSgRVtCxDfjIr01C3LSbuZ4mU30qurx-afa0V_7BEfxhw-icMfCGRYdMl9Gpgu0Djg92PN6oYtBqTkWGyxGB-8HRm3T8R0LRzWjJUUca_SdPlDsZCWW_8BmViJIIz9zts1Uvz35cjcviwgP_ZbUd_IObkmKvzCWw-xjmWVhefuhhG5gXBbOtsEXUMrvhOY9f3YMMIGSGpWMQwOTTejvE8LRssRdoju3_HKpiEsDP7KSO-9KDqki0m6l1jpqEAklwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
کاماوینگا بخاطر همین سطح عقلیشه که مورینیو میخواد دکمشو بزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/Futball180TV/102217" target="_blank">📅 09:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102216">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA8qm_YBVhiJDYwwt6RnLaAFkZSkjyPlQq3A_OAxRCCEJAskILLRwxVrH_wPkVg1d6JMzdw7mY4-5iO3qZmIqpfgOcMco9LaZ7ZY6DURB-gE4nEXu-muNeOTO695uWoVsw04KGy4kb7f0CuPlLkbqQTlLIyeN80V-_Gq1uooNpamMcBDhU69nNEVoRa6zIDWyRByJb4NEywwIbsECu8K0NYCjQrwpB9ccszyTfahnY-X9xb_yFKd3SpP0yY0uYP758c75QWD_gx8f8UjMaJsnuJ5bvPqxO5lk7jTig5DhFmfk7EN9RaaM--Sdsqe5yUQWkGqlaHabSJPIoRmNa0n2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف رفته زیر پست ویتینیا کامنت گذاشته که ناموسا تو جام‌جهانی 2030 به رونالدو جونیور (پسر رونالدو) پاس بده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/Futball180TV/102216" target="_blank">📅 09:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102215">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=VVzhT31bjP6cHZq0TuPbmYveRUb8W7_yyCQPrgWWG28y3qfNOjvkWofMLNFSHDG_FnPkoXsTtVJ290atSHPvQOKciGiRiM2Mq0ct7-rCJt_8T49bUq7KLYcqdZpZFAaOwKhDiThs2-THZy47JTOVOQAH3i-0rlbDzmqV9q58yB0dpfIIS3z4cig4r-889DKsUA8zChlgvxdvGxDvj-FCxR5AgVY-Bm5oYcLlsFR1vz5NFy2hURpe9QlgN4YxIJaJNHfMiOMhLKyi586pj9yLZfSvE0PwCZfNS9L92pecJQmdLho2ZY-cxQO3C1mInB7sDSjJiv3n7bPIk9S5z2-sow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4792b1fc1.mp4?token=VVzhT31bjP6cHZq0TuPbmYveRUb8W7_yyCQPrgWWG28y3qfNOjvkWofMLNFSHDG_FnPkoXsTtVJ290atSHPvQOKciGiRiM2Mq0ct7-rCJt_8T49bUq7KLYcqdZpZFAaOwKhDiThs2-THZy47JTOVOQAH3i-0rlbDzmqV9q58yB0dpfIIS3z4cig4r-889DKsUA8zChlgvxdvGxDvj-FCxR5AgVY-Bm5oYcLlsFR1vz5NFy2hURpe9QlgN4YxIJaJNHfMiOMhLKyi586pj9yLZfSvE0PwCZfNS9L92pecJQmdLho2ZY-cxQO3C1mInB7sDSjJiv3n7bPIk9S5z2-sow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
جانفداهای عزیز درحال حرکت به سمت مرز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102215" target="_blank">📅 09:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102214">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=t5kdTAXWtI5IkSnt8MSD4Yw9ufXqs7DOjDblKoA0Xv-nedz8ahQcJ7wTW2bwPL3AHkYqhCJl0Rtzk4iI6RhLtrJPsEDJhRTd9FB63UTjmnfC1ObJXTzimQXxKqisNffBw4BHlNgC6UFkU2LHKyDnYr2O07xAF0TNEbkVwlC4f6om33J9vJsYlmDNC24Y8NSnIb2sP_l7zTYMkcSiR2pXFiX2WzkpF2ooCTSGaOK_zmE69WZVCmoHCHVKR-Gdtjl-PJqAsglMcSUJaRIQIgqv3TIpDLMsnMpK7InXwT8NATqeiwWHzL6NQJl4zFYhndYYFT4tEElBy0lQVQG9jeG-3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c8836d3c9.mp4?token=t5kdTAXWtI5IkSnt8MSD4Yw9ufXqs7DOjDblKoA0Xv-nedz8ahQcJ7wTW2bwPL3AHkYqhCJl0Rtzk4iI6RhLtrJPsEDJhRTd9FB63UTjmnfC1ObJXTzimQXxKqisNffBw4BHlNgC6UFkU2LHKyDnYr2O07xAF0TNEbkVwlC4f6om33J9vJsYlmDNC24Y8NSnIb2sP_l7zTYMkcSiR2pXFiX2WzkpF2ooCTSGaOK_zmE69WZVCmoHCHVKR-Gdtjl-PJqAsglMcSUJaRIQIgqv3TIpDLMsnMpK7InXwT8NATqeiwWHzL6NQJl4zFYhndYYFT4tEElBy0lQVQG9jeG-3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇪🇸
پپ گواردیولا: "وقتی به بارسلونا رفتم، یه نظرسنجی گذاشته بودن که حدود ۸۶ یا ۸۷ درصد اصلاً منو نمیخواستن! نه هوادارا، نه رسانه‌ها... چون اون موقع از دسته چهارم اومده بودم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/102214" target="_blank">📅 09:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102213">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQ6cRKmXTlO-40eaYo3LnUu4SqHnuSG_4htMjmMM0jl5YOhEVDJ3Aq8C3PsKYELmMyCguPslhWudml4kUQU0Qfg13XnQJdU2u3xY-1paIvFQx9rEQBYr8l74LB32kfLxp8VY6ULYL0LPdy2HMkzAp-XYSV6PTAsIPJcf1cmtsvKl4swqEHHoliWaxq1djX0RIbNBUXNC3UhGK7GYXsd5JcSgcs8tOqJ9AGokdyKKhFGOEnQG-EL73Wt93UDP2JxsAmBtg4zT5G4wCspXSrZpZlbiSmJtUxZtGdcMTmFm_HF7EgDZSB3z7vDuUbXqzIg6UteHMAg3KIlcrfuw6N0fJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی‌ولبک از برایتون به چلسی
Here We Go
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/102213" target="_blank">📅 08:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102210">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-Gaghc-axHIFpW-T5kw5p2grAlnafSPQ4BQRcRa3HWhEj7-eTCDRstHZPHVBSgE8FuivToSA1g_9VojXnoy8oezZOBwE0Xw6xv7JkC7OVNXfQlY2XUxUapt6-okYcBR5L96Nv9KCyplAI4Ifp2RUgaLQf041cjUYuCVz6uyNc4Y5C31DzXEu6a-IM_aXjsAYu52C6bsIeE6WF62f9BpTzvcZeYcefOFmyNeX47xMFtAWhAzw5b4cMtq2Mg0oBhhElMpJdFcWOVSlwt34UwX5OSakUDZFNZ7xlxz4MQKGY-lKE2lSIEh8zGoRQEpe9w-33bizjDs1tEEsGQ_TW5opg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZJZ7D4OwIeHmvyvkm8rLI6jgY0pn-q8Q8DST3rSHt-9CG-5yrW1C-UpSzB57cOYiG88olJbygA-Rhk3DZaVYScJOJXCHc22N4i8K3SNHXDmsMiC7q267v9FHMwZmkxo9lqOTZBiXLF2UcICyAXJkLRHFeLw3S_QQKnBdA86LxU5D4Ui35w36U4_zbVKEmUeRJr24adqGwEvfdP6MQYUhrSVBTAfIR3LM9xEcCzwNFEKIgJaXQ2K2k-D_yDdfsOKDMXHWSwntq5kD9pCmlRqyrZEctedUybUAoeWmihHNDooO5PqFqh7k0m1ruvytZIR54I1dCVgZKUMUSznk686Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oP1PRC8o6UzS-GWHGUE2t66YLCoU7lHA1Pi08TMl86cwVyg0L3BkakogBDLJo1OJ_9e1kZe1d-ksfLQdXsqhaITuBsi3ALlhVBj7zah-Xjn2fIjpR1GHLsN21YtG_R4MJcDBhBBTxPEAznU7g9W-95dbKyaL1k8pzEaxFJcGAdEo-hE_QLaZZwpgz8fGzQgib9FTv4m0s7YnREArkGBDq53BZBApWtsfA1dBOy5DkD0F2keX4-_gPFYhMTeF-8x6skOKbKGkaWx362j0i1OV89oibzHeExaH2Ct1n_pvOwQqGXBlC_iQWLpjNdULd5B1pXEevL_h8_HPqTY1dvrgng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚽️
- کیت دوم فصل 2026/2027 باشگاه لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/102210" target="_blank">📅 03:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102209">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPpWjYqlfN886R4_0zc4R6xWBzgATAlgQXBxi4p7d1KuUZQoqXTBQiULXfbSq_Jcklq4ZBJtN6tHlqibk60Gosow3ppiz5hOLhL71owc8xFREollN0DTsjbBF1yu3UWedTW7O3W8Vyi05ghncg-D2J-4Et7atBCrAw2CWoqOf154Gs23UtChRbLpkwino7XsXB1rHEXrV4Ba1Rl3NWk1EQ1KX3Y8bexRDuPJ6r4O4ESOXdV9nkjkJhy8x3104FevKATurtIADa_ygUR8EMK-GshENrR4hm4-7XAVi2b0yF26xKIGVBQd0IHfuPudPH7YHm041loKzqfDkrkxbo_CbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛ سنتکام: سپاه قصد انجام عملیات غافلگیرکننده رو داشت که همه‌ی موشک هاشون رو رهگیری کردیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102209" target="_blank">📅 02:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102208">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qb_woRtMxNeO8IzlC79lqc2nQBCTm5ugo-YaExyuy_sh6FrAeR3HfqOW1NbwmNng1JsqG74TsVojKai639_KNb8XMNtk67MoKM8GXeF9BsgCr9r2J_nFvTlpoplRAo7-ILpus5twfar1pqfvRua-ZDL463pT46SuayXPBk1fFQLeHxJC8Sig9NixfC3FJt2q_Pa36iqGu813XRIGhTPDmdT6ck4d98cTA6Nv8z1IdfxKlzvuqfKgkG-KX1idKpzMbxjSkd7lEuNLtz0qEEkiUuBqYEhY6Li3SQtFXgRCB4UZf3MpOwmmqsu8x1TTdbGG1QUHm9rEPge9yMKlIDbrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
رومانو: هواداران رئال‌مادرید آروم باشید. روند تکمیل قرارداد دیومانده با سرعت داره جلو میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102208" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102207">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=CMTM8B9UgwkksILUDN-Pv1mujwFVm9DceTVKHttylRp760xurNu5ST_H4JWhHDsIz48ehKyIjwg7G6TuO4V5NSawFuT5UdNv7L2EkspsX3SB3cXGZXDzwmh-9JPHfcR0k_5iodWMX4Y5H2oO4gFhspoHsYm4rt3FR4AHyneXigoc6gz0hr1rR0jAtffxdyU4kHfWt1RBE-xvgHuO2XmzvNpvMSrzTB9fmDffa1u-KGLz7AiB-hXbDORsyHSSaYWeVQc48Hg1EoPs9gG9uFxTOlM0RrTMR2mdACg1kZ9AN37twrZ1Pr4XoR4KiW4Mkl3a1qYy_STaqdhUssFJlRqoeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=CMTM8B9UgwkksILUDN-Pv1mujwFVm9DceTVKHttylRp760xurNu5ST_H4JWhHDsIz48ehKyIjwg7G6TuO4V5NSawFuT5UdNv7L2EkspsX3SB3cXGZXDzwmh-9JPHfcR0k_5iodWMX4Y5H2oO4gFhspoHsYm4rt3FR4AHyneXigoc6gz0hr1rR0jAtffxdyU4kHfWt1RBE-xvgHuO2XmzvNpvMSrzTB9fmDffa1u-KGLz7AiB-hXbDORsyHSSaYWeVQc48Hg1EoPs9gG9uFxTOlM0RrTMR2mdACg1kZ9AN37twrZ1Pr4XoR4KiW4Mkl3a1qYy_STaqdhUssFJlRqoeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
انفجارهای شدید در اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102207" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102206">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ebFcqyT1HBpsUCPWPVxfaEYipPB_1jollD5myaXnWEj_CdWxS8YgCHjRXQO7C9Hiyn69fYpo4Wr8nme97rFBYikR2cw3unags0pJn84PBtge5vCoQ-OnWZsuyj17nmWxg5oB5YIz9QSudkCPTyz59koVU2RyVmtGjCMxy4Mx8qMifZ1RKeyaEvulI5zIw9kCdGZapFl8g6nsvTdPJMzzQnfldcIAPswNQ3x4Am_MabLihPR_DMrZX2qGAuHJQgw9Nob7gUbvp8yvxShmzW3Y_lFGEjBSFNI6xmTVsQtZBXpCM6l0DKEu02NOLZKyNdizmglc_k5P66xAVlEWnc4yKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102206" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102205">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VYLSIlkTW7x8G-q_MFkvIQQ5L_VZ7SYCukWCuLSG639wihnzS3egJ6EzNGntk6JO2o5-BRJ9BZPXE-AFMsZwXDHEVnS5X1fjsk52BL_lWKFVlHH-QliFW43R5_qH0KP8UCuxK9gphrzhRTC19knoZUsZE3yNh6lapN4jMRVDDYA_RoLDjHD-l4JoGj-KpQP0SoBYR4BygshbLjGWBZSUK8wqcYGLa4vspaKPDyA5cyuKv1P7xMKj1a_wYzGAS1oRFRa973RQTgZkAKo4agMCqPgFS9eZ0JgBZbeTlpDMcCaSdQob03Stis5Hh_Wwsm9j3VF5W3ZYumbT3Jmy_DjbFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
گویا ایران از چنتا شهر مختلف موشک ول داده سمت اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102205" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102204">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnOtMRuUazlIND2Nfe1n8Ik519f475isE_8wqJuk3feolsYCpmFiAPMAq7gzlC2vKbpfDhQVtKIFkv31mS_KN1xGnoeJBWB14qqXC94DSJ20Hmc_gW2hE4eKS7kfcwAzCppBHB_ILbL4UUkVJ5EkO1BUJ2TCuB2sX6eQFCHA_FCjeazNJcYBVSNvnN7wiUiqPcjfXoZpkk6fxIdFsEUyHmtfqpTd6YduUmxVFdvclI3GKey8pIb6B5vLT0eTcz71hG8Lk_wCM6nmS9mzv1XOWRA1tWNoMK9oXPZ9YJK9hbfvJ0S4M68nx3AIS2Qf0DSw7DWuZqYDbqQLDA8xwyIzeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🙂
👤
تعطیلات علیرضا فغانی بعد WC
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102204" target="_blank">📅 01:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102203">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=Yg1Se6m7dHMdiVq2-hOifCeR_SSfz9vU7m6vHOlvBioE-hXj9gq7b4ZqUbb5aMhHXOD_DdnTsikIz7tETZipfn8VCzTTQBe6zbVpi-nD8R1qqw4HHTvg5EqkzH2zgo5b2zGfqO6obluUVokKzBcC1UE4hsTRcrqG3U_Zkj1ti8pyGhy7szyn55h_-r76xdOOL1qBqdNO60ck-GWhqHKdZfMQIPlfnUUNOXLlawFrpwFnhsNZ4H6MbgDgqSgA5U_kkzvjCjuuTCq1ZynPUEEXSvdoWL702Qpw2npJ97DyRmztfSxt1eSE3VnPlGpxJDWFUwh9umF5jbv8tbt7pCe9Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7274faec3.mp4?token=Yg1Se6m7dHMdiVq2-hOifCeR_SSfz9vU7m6vHOlvBioE-hXj9gq7b4ZqUbb5aMhHXOD_DdnTsikIz7tETZipfn8VCzTTQBe6zbVpi-nD8R1qqw4HHTvg5EqkzH2zgo5b2zGfqO6obluUVokKzBcC1UE4hsTRcrqG3U_Zkj1ti8pyGhy7szyn55h_-r76xdOOL1qBqdNO60ck-GWhqHKdZfMQIPlfnUUNOXLlawFrpwFnhsNZ4H6MbgDgqSgA5U_kkzvjCjuuTCq1ZynPUEEXSvdoWL702Qpw2npJ97DyRmztfSxt1eSE3VnPlGpxJDWFUwh9umF5jbv8tbt7pCe9Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
بترسید از خونی که به ناحق ریخته شود
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102203" target="_blank">📅 01:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102202">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsL-b_CktLbfDSH7raj_E-DxZvWQchwTZZgM74xwxM8MF-NrheTburzUO4gLh2xa_APsjOZigI5kwhq6eq143M6S9b09QVT28bwfZbZ990yBUQFopmOhJxNJ8YhJ0uAnqsueCe3xN_Ws7IreJ_5zrEnZvD8yZjOUtUwEwxd8jUAWhAejbSSXLtbGa2pGsKbumsf6rmS_2UGd8WbQELoi3CpG4_mxpOPOEa1DeseSwkiyg60ine1RjdybCFgMlqJjN3JluV_PqmZD4ZsTPyWMRciGyEWkNzt8fOQYsFnKM5IOgXTDyvEV7ki4I3esKOftZVp32eP9KriH8emvyQlaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیوفیس جدید بوکایو ساکا
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102202" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102201">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102201" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102200">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=dYdyQknXqrHPrdJ-mtILbZ2GIg6bJCzO58oMwIeCPDTl1nT49B4s8gl7XffF0XGGQoK3vYUgMNo-LkPSCypxkOygdiEN77p6yfTEcmFC8IquS-rFMMQWj7AkF4sSggcLeQbc5vz730-Af7kWMYHcko_CdDy1JKT1M3gBHrXofSj7SntH1Qc8Q3ejyPaQNwzPksgwLzS8Tojzai87ljsXl0nbQwUkJhx-CdDkZE3jcrg0cC9axuT7TQ0_6oRURIvqef5D6SfMpdFChTUYsGeRt9ASOP5nkofs0gcYXN417U8FbCGsy-Sq3UXVYSUZPAjJZG6l1ke4TXKsoJf1kOgsTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=dYdyQknXqrHPrdJ-mtILbZ2GIg6bJCzO58oMwIeCPDTl1nT49B4s8gl7XffF0XGGQoK3vYUgMNo-LkPSCypxkOygdiEN77p6yfTEcmFC8IquS-rFMMQWj7AkF4sSggcLeQbc5vz730-Af7kWMYHcko_CdDy1JKT1M3gBHrXofSj7SntH1Qc8Q3ejyPaQNwzPksgwLzS8Tojzai87ljsXl0nbQwUkJhx-CdDkZE3jcrg0cC9axuT7TQ0_6oRURIvqef5D6SfMpdFChTUYsGeRt9ASOP5nkofs0gcYXN417U8FbCGsy-Sq3UXVYSUZPAjJZG6l1ke4TXKsoJf1kOgsTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102200" target="_blank">📅 00:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102199">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neRFup4ySqbFedhI5h9oyC-IUfKnOG1oSE1OxZ3r16VrqLUdgHU_RND9ItiDBY5MpisaxukWfsrktXsKqoY4coHuHcFd6hev1EC7COqlbgGEfXp6xKfHXQmo69zl5cbYhJBkb4boCTCg_iglKhpoewOFEvHopDjsMLYfD9h6DxqFGr5NgZm65THstxxST_9qTuC8wLfjWxyhEL9-DBk2NzNdk-gaHxxVThz448F5NnsRnqDcmYFA0KESNFqyyi-eH68uJG6jEBJry2BvHKxwil9HiijSubvOgx75Uvnzj9HzvsFwkDyzU_-glVMkSDP4mP27K-t076PXo1LiovXKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
رامون‌آلوارز: آسنسیو به سران رئال گفته تنها در صورتی جدا میشه که تیمی پیدا بشه و معادل حقوق‌فعلی خودش در رئال بهش دستمزد بده وگرنه تا آخر قراردادش قصدی برای جدایی از کهکشانی‌ها نداره
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102199" target="_blank">📅 00:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102198">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcnwMyhcOHi9s5dr3ZTqWTnMhUcP0WM_IARQRDSodWiHwxAHQxT5QoZkVRb_AI5ls5q7vSU8engF1X6wS-4A1PI8IthgLpaGh9DABVpFGJm7auj3lT6cGTRvTTI1-mrpUbZ0vDwW5y_VVDodT657d3o0SdVP2oDz3Z4b7A_wWAbthXda_wB6DWIpCBraYwLGi5Vbb79fnD311ilYB01rlj-PEUTHdgJDtL5aErstYxzpeU-llE032bWNPTo2X1jQ-3fys2A-oW_hFCOkOey3Bje4BhUmmsAncbNuagS4c8IUxJzJgxRoziAfIV2sUaHc-imoxlRB6YtsrwbpQIkZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
😍
دلیل آرامش‌خیال بارسایی‌ها در تمرینات:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102198" target="_blank">📅 00:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102197">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔵
▶️
ویدیو باشگاه استقلال به مناسب سالگرد دومین قهرمانی آبی‌پوشان در رقابت‌های آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102197" target="_blank">📅 00:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102196">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtQSvjKzxUm-MaTMTOsy3JnfzKKC2EPTKdrtN-CoDB5Go4fO427w9gpWyg_1hjU933m3AqJPQEJNI6vmxsShWu3ti_YuCfmyjuz1WJsYZoHwIB6ghv42qi8kWWViuX_WeYeMZ-IOJtso3G0gntyFKi2H-tZn77GMzhKr8YQ3iuAG7CIIiy0CyiA8GHvAhm7FMz5TyczWZGtDWDkBSLhrplfJsnjE7wyl-Ftilm-XtL4vQEv49Yx4w0kawwJNwOS1H3RfOD-q58KQ-aN0v5sL1H78QpaSLTmUwPisXkJYtLNpR3mXbBD0hegewf6zJYYDlF_0O6XkUWjqcPjLJebvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102196" target="_blank">📅 23:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102195">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NX3QnPgBXY0Lc8ilBAIF0H3f4tJfv-gfDBNcuj-LmZbjx_jayzh7TcgZwkWFxjcVQEHJyeJCvFwO7ZKASvtER6h7acxRnJOHsYGrF3eQd81AQXYWELjSnkd78JIJG_6MCZs-DHi9vQtLDoP8FoAKdQIRsM1IL_IOdu-vNOvTAVOYrd5qIVkMwtsbuwcqJXHkZIOvt23o4z7qIam1iaV4WA3BYVM-K2U_jg69PBNJezk-13G76mO-dx8j1Kv9JQ9mo-UxaPVkUfsuHT5xjmY6HlCt9VWGYnDp4q1WKknUfnthV1Ck11-c91Q6PplAn4VkXPID3UvE1XWcanxYIyyQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیلد:
نویر پایان فصل از فوتبال خداحافظی میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102195" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102194">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIqenKWIzIkAU1pzF6fI_oVenasn314IN7-5vgoOJ9Y7uAwpHBo72iFloVZuXX02qgGnGi8JQ8JzPHLRbQRmSIN1KXRUtJEX-xSUSV9-klupcxbN29Qwle43OFUYRvZANGdhk5eufK-Wd-9t_b_fAyO53QRpMECjr0gxugAR5nK-A8wvSLQQKoAi_ZZgefFjDkwUp6QM3B0rfMYIO53iDnk3Jhny_F-rna3M-JP5oUIjCaND_Ihm5YUhJfcpUdkdF-Sf_cqZZMnD4f3S06mz6Ce6OZZ9EtsbXYaUj9-wTDRKH8qzHrRaJf2Ffc3Dl5O-TxyknSJs4mFJNyTH4Eh7dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموسا یکی جلوی گذر زمانو بگیره
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102194" target="_blank">📅 22:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102192">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=Pz7ZO2jenldDJRqtZr7I8N8uMAR8m5vw2jSxlcJbAGBy5bUX_mEdaSYg9RvghLlRErhvozXipDgGiGX_hnoqyjbvJZco-CfYFcfthqzs706Jh39BZt-u2SQE2Wlupm-4yRLWI0esCLskdr9zIlU9rc9_AGXZfPL24JozlVZ5jHXKQNjZ-mBS0WXj_FJMa0Qg2rTNdlCp6t4ai1AEjtvWsvarUm4hkf4vd6hKAx193U48ixrHS4MkoP-5bVMBpVmkd3xtqsz-z2bvsAvURLd6qvlTZKrKXApwGD9YJveqoE8Pglm7nStKs1r4cw4muu-5_0lgFgUjkCMUuPa45R3fRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af48b4918a.mp4?token=Pz7ZO2jenldDJRqtZr7I8N8uMAR8m5vw2jSxlcJbAGBy5bUX_mEdaSYg9RvghLlRErhvozXipDgGiGX_hnoqyjbvJZco-CfYFcfthqzs706Jh39BZt-u2SQE2Wlupm-4yRLWI0esCLskdr9zIlU9rc9_AGXZfPL24JozlVZ5jHXKQNjZ-mBS0WXj_FJMa0Qg2rTNdlCp6t4ai1AEjtvWsvarUm4hkf4vd6hKAx193U48ixrHS4MkoP-5bVMBpVmkd3xtqsz-z2bvsAvURLd6qvlTZKrKXApwGD9YJveqoE8Pglm7nStKs1r4cw4muu-5_0lgFgUjkCMUuPa45R3fRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
کافو: وقتی پاتو اومد هیچکس نمی‌تونست تو تمرینات اونو بگیره؛ کالادزه، مالدینی، نستا، هیچکس نمی‌خواست اونو مهار کنه، دیگه ببینید چه سگی بود که می‌تونست به راست بره، به چپ، سر بزنه، با هر دو پا شوت بزنه، سرعتش به طور دیوانه‌واری تغییر میکرد، به سرژینیو گفتم یکی از بزرگ‌ترین مهاجمان تمام دوران‌ها به میلان اومده اما یهو همه چیز عوض شد...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/102192" target="_blank">📅 22:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102191">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6KfjnL6fczr1z8OutQ7Fcyem4UvuzuLpBR9Dqk7ziEamUadjkTuj8APgJyLISLKiRdTSa5wuFQ_kZgUKacTw8C1s6uWis06F6V1Vzvw5DhrGm_4DszucwHhfDTXKdcGDhd-ZlwEyfbXytanEl0P5okLhi2-XmJjDeIrxiGGurYlsFCgkFO3TlIzzScyvtawa_Q06ftw-xgjvLRCdaR7_Ov85L-HRNqnPvYKEKyz0IFkN3VEHAAGWdbcyTaq6JeI4AVJ4Y66RrlSiEtB_GF1zcIFc7LJ2Y-OWDK5I7YgpdsPvBjxEuRtj8metTZth-thLPmT0Unhbv_Lsjyggcv9vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستیان دریسن، مدیرعامل باشگاه بایرن مونیخ، درباره اولیسه:
هیچگونه ارتباطی از سوی باشگاه رئال مادرید وجود نداشته است، نه تماس تلفنی، نه نامه، نه فکس و نه ایمیل. بسیار شگفت‌انگیز است که چه چیزهایی منتشر می‌شود، در حالی که خودتان حقیقت را می‌دانید. این واقعاً حیرت‌انگیز است. او هنوز سه سال از قراردادش باقی مانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102191" target="_blank">📅 22:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102190">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=p1K4_-zabxe1nJDTmyKo_Nl2IBhlz_V8dWyayjO59LR1hmMBJ8OD6f2op4AYl3eXFHSYTi_kY2aHjX-GDwAmxTUIcC-9s4uzu9xM9qSXJ4rCmS4h-stW3ATE90lPrSvO-5t31pVKjg4VfFUfCqbukRtusoGkkHFYF2dQsIu3dQ9IqQUA7a9ojFYny1R2pYYR16C-ou0BXP88KocdsS-2aF2M0tOIdscYqKY5WZ1Z8ZLIaYHsWdR2CisyGWuS5rkhCz6MRwVupecS0CrLm9Ug63nZk2bKW_hyTpdhv8GA4Sehn84I6X1Hv0mc9SzYOZuJ6ctZaR-JZR_7M6a7qgWSki0qddCwJdVUMJhl9Hw29J5J8zvFL5OGyN0tQHb_rd2Mn_xLuecp_B1oZShaw7-mRGp_M0yMNhvqQoiRPiccAkAXghDOK_A8xuC_jg1Qsj7ob-9gjs87L124PpKoxve6h6q-9W0l4pUNhhW0feB3KPQANL2IbcmjOVKTzzaK88nGWaAlLawC68UYV-F7TcA5gK2RZvaXhnFqvZnZbgNb2Vy0t-0H2WkLTYaaAGRRAQBHBXqB_IPZ-wmzOWIKf9Vc0dqjeYkQ427o3gBd-RoQBq19YiWn3wDLKeBhPEoZ1ByW_lSe5hcDUaPDMA_LSewtjr41mJw5etAjM3mFebYcf30" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b8f5f5029.mp4?token=p1K4_-zabxe1nJDTmyKo_Nl2IBhlz_V8dWyayjO59LR1hmMBJ8OD6f2op4AYl3eXFHSYTi_kY2aHjX-GDwAmxTUIcC-9s4uzu9xM9qSXJ4rCmS4h-stW3ATE90lPrSvO-5t31pVKjg4VfFUfCqbukRtusoGkkHFYF2dQsIu3dQ9IqQUA7a9ojFYny1R2pYYR16C-ou0BXP88KocdsS-2aF2M0tOIdscYqKY5WZ1Z8ZLIaYHsWdR2CisyGWuS5rkhCz6MRwVupecS0CrLm9Ug63nZk2bKW_hyTpdhv8GA4Sehn84I6X1Hv0mc9SzYOZuJ6ctZaR-JZR_7M6a7qgWSki0qddCwJdVUMJhl9Hw29J5J8zvFL5OGyN0tQHb_rd2Mn_xLuecp_B1oZShaw7-mRGp_M0yMNhvqQoiRPiccAkAXghDOK_A8xuC_jg1Qsj7ob-9gjs87L124PpKoxve6h6q-9W0l4pUNhhW0feB3KPQANL2IbcmjOVKTzzaK88nGWaAlLawC68UYV-F7TcA5gK2RZvaXhnFqvZnZbgNb2Vy0t-0H2WkLTYaaAGRRAQBHBXqB_IPZ-wmzOWIKf9Vc0dqjeYkQ427o3gBd-RoQBq19YiWn3wDLKeBhPEoZ1ByW_lSe5hcDUaPDMA_LSewtjr41mJw5etAjM3mFebYcf30" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇪🇸
یادی‌کنیم از هافبک‌خلاق دهه گذشته بارسلونا ایوان راکیتیچ کروات که زیر سایه مودریچ دیده نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102190" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102189">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQ-xIvGh_0ZCc1aYujaqANm3bUXHfuj2sPMTDLF26dQZVaefwZj3TCKJf_h9xThxbZCPJq9muVvZB3KgBy0lJ9kaDf3t8-kSD0gPc9jbRpXYOhQ59HUhkT9EYeWsE_2eaqghFfu3qJ_d6Mn2iuw0O_ggpN046n9EEju33KOTIlYlWx6LjFM2LOqr1EohxELVnDN0086qhpmFNEQnVZWOfx7TVn0xZjI-i4T-GJUihmKh8ZihEaWivn_6WRLR67q0Nzdm6KPr8qo11xNHWaGPaEqcd5Q4-gqGC2ufV1UQtFTGoBTK2XM19dcA9098N3cWswX0QpHb1vwu-WqOF7bjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تیم‌ملی آلمان قصد داره درخواست میزبانی جام‌جهانی ۲۰۳۸ یا ۲۰۴۲ رو به فیفا ارائه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102189" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102188">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laOVYyDqNxCvrA_FRMWCeQW55KubQQ_Ty6fb2TIrcygAVoC7IRPd0EhaGFyinLBObq_rUuDCWt2uxcDnCFzGGgC1u1WaNsZs7Ju04uOvzOKfN6C5WjdYqgm9Oh_p5WQIGR0p77gm3cR3noYq6UfpOUmVh3kQbD7wEKgjoGqvVyFAKmSn6lazim-gsqOC1qIK50ogj0h0OR3Vkw8DTrSgHBjh0HyZvNydPm8l08jHzaWJHHfDHqEKeMH-CFDlPAj29AexhzqEk9swBvE-s-a7rE3TxUcUxbT0AH2ZnhZPvhgkawL5-wI4jAa4inA5_fS_VkbGjWo4jkks349Vl5_Eag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102188" target="_blank">📅 22:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102187">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzNhb7DqR_VgR_xxMysTMk3xsEKYJq_kKb4x51kGY20IiB0hq7FJruu6CFodKaAPkqjgXMwEqWFI--p_B7W4L2Ky6vBWk2G7Dfh9Y3jffev9uEjK6ZwFlX2DMAL5UGsmVt8Wri5dXOHVxOVnZwh1et_JkCicIXSNaaZF32CLxMii42-mnN4dFGq-0jLtZw-rJzKit5q_Aj-TnbaA3Zb3g5WzRVNh0oTSUmiBKHY_RTQM--8Nl7zvANTrve-W0qjczvypi163AXBIP_r4iih_ld7IQDB8t4ecdYxsk9fx6FNeHYoYfJAavdyCCmGa1aBk9rgEs00d4G7thojQYfXKVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🏆
زیدان و بازدید از افتخارات تیم ملی فرانسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102187" target="_blank">📅 22:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102186">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz3UNkk3rz3N7CX950Q8bMXqxAR4pG_gzCFE-VxvD6_hSCE0YH5wT8YAReyMxRL07E8Ww87JX5mwfLFxak5ZIM-XgEwNCaRBx5oS9GkHcEghX_lchZdwYHLi3UPOYsIjwslHrGuLxlhdJrWJHVWt5DB8Rh5EwoPiTy_y4xTD4O26SfBApuRhbaFWYHYRvfauMkEYTfgftb3XqzQwCXXAprfdR2qTlE6_z1e_h-KVxQMHv1MGw46rViFcPlor_Te1JyysFcfA-dzxuCiXCtCtmmbk3DUS_oKlRM44cBDC0Ei_9nEDgTIEw0KbEWwJ0fWt0aOLi-Y1RM-QsvZwwq5ZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔺
در سال 2020، بارسلونا تصمیم گرفت که دیگر به لوئیس سوارز نیازی ندارد و او را تنها با 6.5 میلیون به اتلتیکو مادرید فروختند.
🎙
سوارز : «تماس کومان برای گفتن اینکه روی من حساب نمی‌کند، 40 ثانیه طول کشید. این روش خداحافظی با یک اسطوره نیست. اول گفت در برنامه‌هایش نیستم، بعد گفت اگر قراردادم را حل نکنم، مقابل ویارئال بازی خواهم کرد. شخصیت کافی نداشت که واضح بگوید خودش مرا نمی‌خواهد یا تصمیم باشگاه است.
🔺
سوارز رفت،21 گل زد و اتلتیکو رو بعد از 7 سال قهرمان لالیگا کرد.
🔺
و وقتی مقابل بارسلونا گل زد، اون تماس 40 ثانیه‌ای رو فراموش نکرد. نه جشن گرفت، نه ذوق کرد. فقط نگاهش رو کرد به جایگاه مدیران باشگاه و با دست گوشی رو گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102186" target="_blank">📅 21:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102185">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpUkYef_MGxgaW0vmYUzYAe12hmhvL7Eq_8fyUGZOPTxsjTOMSU02bBk0EBrD0YF8fD0Y_YILrlKbFQY9XbULVYMF3jqRgbysgFHuEj-vSYNBHZ_CCli2Jh0lAO7OD-VpeDeCcqv0r_wSdqFdrFpn7merKtRfcNnWfcOTe9-8_R7S7HpVy9j0I_bb5bvTXcvCnW2kreKH4DhXME1Sejka2qdW__OWEeB_dc5pQZvap06M15OMDRcVohaVmV8BAYHEmGKzRYojB_z4JwyLRJ_2yKO2Zc5wclle633OoEYC0g9HUQGHcr-fUSLS2jc1kgYb96jSkO1pUiWxg02izk1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102185" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102184">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV6Z9umMzgfyuqDN4cBvHkMNNRt01EegHzbI_uQVioQTjPzA9IJA9AXmmPobZtWKHV2_ml3sdCgmJeMVnEU_inAD6xyPAPUgaybQnV3E6dBtd_VfyniPYN7PtD5Z73A7t0KcDNjcRg71MGIXK91JSVTfOh2hkxwTmQ6iYr8zDDu6-BAwysgibHiUtYMg8G4zcg2gY42-_2dy2s9Xn1bcFvlmrND8BtSs2DeZmi8pX8uBeMvLVqkxBAfgcHPSep3Bar3SSfZJ4_rTvt5EyX8QSG9TbZ38KuMUmRqEct1Q0aXo_psFN8iKV9xb0ztCwUBhIb97DuXDzYv4aFnE381GAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ کسری‌طاهری هم پس از مذاکرات ناموفق با پرسپولیس راهی نساجی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102184" target="_blank">📅 21:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102183">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aItq0w75KW08n0o3wFN25_1ka7ok2gxEEjYJOODNZQimCaiClK0upD4vTqiPYiuwB1aFI65qVvnD_LUyizwY71GRIQpu-iTWqFqrk8Jcrf_d0vEWGjDHDWsOIMPAdKLPdMl3dw1ZjtnKLY4yQ4OK0_MbATZvtkzeaYyiFNsD9hbSW5GIC2giqRpcBsPAuTHsvudlbGWGIB2trKH70qXjQELwRQNYVaBFmM6BIAF8Qpxu74_-UO0_XshIhNvX1KiK7Bzw7GbyE0vnh5mwg19s6vnIuLCgUKbzYrU1vNTnvO3qXGykW6t_S3QdRmrpm0ZSWfMhiLF0IgQlWzZKTwfIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست منچسترسیتی برای تور آسیایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102183" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102182">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=PD3ZQEMpVenL4UsDHdxIC98sbahZCiAMHoDzavtkluxpNej9NLs7q0DlTpq7TPAgW1vBufwjdYnZ5cEW-oqv5nXdiMU0UeglmoYuyvc0-nvmu2uF6hZd7359p17ejRwkUzQQ9T4Cs1nPfxcxJGR79qAGKCJENEPzdyYs19zs4ZncTizOc56BQ7S3J_G2_2AQqVVMimMXqFkbZ1avsghQMK3OAHaKksVGGbzAY0OpYYINfP1tmS540x5IJ9DCEwXxI7kP_b4zMZxPawJTfGUVKE3j2jfBbQ8--aDgpL1RRBO38Jp95KcXQmbT7ohNk1BBN_kL8AVVJz_tlCIii85tOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b71e2610e.mp4?token=PD3ZQEMpVenL4UsDHdxIC98sbahZCiAMHoDzavtkluxpNej9NLs7q0DlTpq7TPAgW1vBufwjdYnZ5cEW-oqv5nXdiMU0UeglmoYuyvc0-nvmu2uF6hZd7359p17ejRwkUzQQ9T4Cs1nPfxcxJGR79qAGKCJENEPzdyYs19zs4ZncTizOc56BQ7S3J_G2_2AQqVVMimMXqFkbZ1avsghQMK3OAHaKksVGGbzAY0OpYYINfP1tmS540x5IJ9DCEwXxI7kP_b4zMZxPawJTfGUVKE3j2jfBbQ8--aDgpL1RRBO38Jp95KcXQmbT7ohNk1BBN_kL8AVVJz_tlCIii85tOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
وضعیت صداوسیما رو؛ چهره شرکت کننده در برنامه عشق ابدی، مهمان برنامه صداوسیما شده و به ژیلا صادقی میگه شما همیشه با معلومات صحبت می‌کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102182" target="_blank">📅 20:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102181">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcRobxhuJr7Icc_Z5uXZM1Oi2JZZppFGG3PhP3Au0VmKGNUYA9fhalR_p27pg6RU7GlF3s4yB9Ix_1fV1zjW3QjuounzVCd0cOZS-emrwlPkIyzaMRAu7dn9NuRU6bhYON2rQ-SlCflDzAo6oddNJTEfOTsV-Vlq_udVbCH_F6vQ_MT1JWzVHw4b3zVXsvEFAFw6xY4cgCstutUNVGObE7hY_merN195ovqqrJ2QWWfL4a7DuxrfqVuucP8vhdx1j8W_T49Ad1jip7VWRxVkiUvo6TzxknWitEMlDJJrivqceTHk84t_Az2LVoK6Hbgyz_dKhn9xHTzASrvmFqOshw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری
🚨
🚨
🚨
🔴
🔻
باشگاه لیورپول در حال آماده‌سازی پیشنهادی به ارزش 94 میلیون پوند + 35 میلیون اضافات برای جذب بردلی بارکولا است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102181" target="_blank">📅 20:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102180">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=CyXEJLafMMr5SP1Wbf7d-rR-eiQrVIKTzXtA6KDazNLj1zywfOV4e0ZqSD4xMGX2uqtolrN_6gI7n8mTFfDdkmpIVHy9SJaE1X5ItCySbh5yOczIKpmbEyNFbixEDm6HrUIW2XhvlVcz-0FesoMq3YON2U_ItEl1GyPRYcOz72AlnLqn1Biw7-kc8GAMbKsZZKutZYrmMC6fWvsEy-1GsilPrhrhr4nByv16DHSurCdM5B2cYqhQ2qzkDJTMXeW7g_79d9lc1ammMqBnTt1VhBoua-hbUjXk1GfMQChfq7oYbiA31FJZ8UIpdOM3l8IpUjBElHLcMN2IqaHFGoEx3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be1bfab961.mp4?token=CyXEJLafMMr5SP1Wbf7d-rR-eiQrVIKTzXtA6KDazNLj1zywfOV4e0ZqSD4xMGX2uqtolrN_6gI7n8mTFfDdkmpIVHy9SJaE1X5ItCySbh5yOczIKpmbEyNFbixEDm6HrUIW2XhvlVcz-0FesoMq3YON2U_ItEl1GyPRYcOz72AlnLqn1Biw7-kc8GAMbKsZZKutZYrmMC6fWvsEy-1GsilPrhrhr4nByv16DHSurCdM5B2cYqhQ2qzkDJTMXeW7g_79d9lc1ammMqBnTt1VhBoua-hbUjXk1GfMQChfq7oYbiA31FJZ8UIpdOM3l8IpUjBElHLcMN2IqaHFGoEx3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادارای انگلیس با هر پاس گلی که آرنولد بده قطعا یه فحش حواله توخل میکنن
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102180" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102179">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=HnF2FKnQc6SKV_dFZbhLNJbeGmgsmBQfMFerp06SH5b7t-JSgllCK2sNsT5rAbeK_jPpmRCrMRmbjPGyXuYUNRcXDOUgajg-RgS5s2NY3Ygc-hwDacMu0N27NHB1DoJUy7tIUERT8fXjw2WHISvmI46n2zLI6bjn4F9a-3oeFK2iR920eRiQ2uHU1t2RX0rA8PAOEaaijCs51nYg3pBtGTNEfZGRK891A_fZZOzUGo5tqZ_yROnGH1aG8Dtg94DjbJjKAZp4cXoc4axScnm1EK_I3JFD8UhRMDN7q3JtckwBKEwnGmg7lZUDiwhxR1HoyFMHraOb0NjF2zVur8Xb0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5b1e0f9.mp4?token=HnF2FKnQc6SKV_dFZbhLNJbeGmgsmBQfMFerp06SH5b7t-JSgllCK2sNsT5rAbeK_jPpmRCrMRmbjPGyXuYUNRcXDOUgajg-RgS5s2NY3Ygc-hwDacMu0N27NHB1DoJUy7tIUERT8fXjw2WHISvmI46n2zLI6bjn4F9a-3oeFK2iR920eRiQ2uHU1t2RX0rA8PAOEaaijCs51nYg3pBtGTNEfZGRK891A_fZZOzUGo5tqZ_yROnGH1aG8Dtg94DjbJjKAZp4cXoc4axScnm1EK_I3JFD8UhRMDN7q3JtckwBKEwnGmg7lZUDiwhxR1HoyFMHraOb0NjF2zVur8Xb0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
کصنمک‌بازی مجری تلویزیون با تاریخ ۰۵/۰۵/۰۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102179" target="_blank">📅 20:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102177">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E9rrKcRZvlMATc9gx3uXanPggC8oPdY46-1Qr0KfNpvmEgGrLgKtAe6IPuSV9BoS3ezqkUk4S0ffpXX6WDhljwl9UTz4-GGLaz4h_VoRoPynEZn1R4u1GhSs_wqFZcO59LCGr2_w-hvD6UyoS0f193ZqzK_jrUQtQjYidgYwxjeNTwtFSxDHCsb-BweQ5r4GNOkWdkAAd-QJ6Nfny8oZ5JkoAXOg2LZYvOLgRHIIUdvOew-iOzT6wFEzCZYGk6FO576NGRm9u_RBRsk9f7m_vHKBlw2morLNUDgKW-GfRMjuyVhuG6NDKxy1Irj5q4yDqH5Y_kh3hQ0Esp6VXqq1zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsk-WUsHWM7uLk0Naao3XQ5hUPDUmdwlEAjwc-zsgCZlaa5j1ieXRa4L0EbQwpU3txcbK7zBIE53-BrJIOr4WYDmAynkA1VYGKkLpKrpxHVCq_8nasLziWmjB1q2Irzuce_Q32Sh7Wivo39KwZI-TZibt9LEEdwyiHjZMnxaOrdkHTI2ioA5Jr6LygN12jXzftZ3igpk74h1kVTiHLgfKUl_-N_FTDBgEpxd0Un1v3KVgrL-h5Fzl9xEJDqt4k2VXL9S825OBWMrdWRI98-1ztxQmI4BqgbxGUaQOAtKcf8xaEsvtIx2yB5iKng5A2VqQQ2WDwKjUnS990TJFSGZxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🇪🇸
فکت جالب: چلسی برای قهرمانی در جام جهانی باشگاه‌ها پول بیشتری از اسپانیا برای قهرمانی در جام جهانی گرفت!
💰
🏆
قهرمانی جام جهانی باشگاه‌ها: ۱۲۰ میلیون دلار
🏆
قهرمانی جام جهانی: ۵۰ میلیون دلار
یعنی قهرمانی چلسی در یک تورنمنت باشگاهی، بیش از دو برابر قهرمانی یک تیم ملی در بزرگ‌ترین تورنمنت فوتبال پاداش داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/102177" target="_blank">📅 20:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102176">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Of6oXoNr81IHWMPOOk7-70LS-eI4LNQX2Q9muAsMbxFQ_aChvp9_WKgJDM4zzhzyhD2ZH_bGI8iVI50SQ1OFnBOwoVD285kP1q4-PDqd1wCEX0JS_xtqXB-dTEBaC2ax7f2ypSWb6O0y3lAz83ghRbNbvlrp7UdO45-UoasISwg4ZbNochJ3IouSIZFxihGNGH5LlKOc81BuA4t5HfmX-bBH-AsP2HSDFbqfDPnsjKaBAtqYq0EXqs0V_O0O0ynxmuDekJ0xyxZsqKJV0Sd-HtU7flkFC7wxPoh-GYLZXG_f4kI4001FBvP_Y5r6vKOJsF9HWJf_swh2o8SqJKENhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#رسمیییییی
؛ با اعلام باشگاه نساجی، دانیال ایری، مدافع سابق ذوب‌آهن و ملوان به جمع شاگردان مجتبی حسینی اضافه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102176" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102175">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMGBECrsWuYesRGX3JKZh_Ky2M60XGhCl9KBP4U3Lmdml-UHKxe4azKG704Afwr0bHMQ8gQUOHvkoIbIkZqLnhEGWOrBC_5DfNMSot0KH87oSo2b2ZQ9bzRRf6fZuA9YF8C_SgQJqYdtW1fr5H2aWp42jNrYbgrIpBLCwgDbuncYrIjiu58WMwGYOBrRJ4Gm-n-TuLcKvIR7aL_28h5Y5P0wU4SJISmFwRZdbdSUgCucaL9VE5uPRVFCiIk6ux6D0bb4KyH9rNY3ppqQDMF0tjce5IWh006WyfjRUgT63t-ThdEMl87sI0LIRzsiBtS_qj-ZCFzpgJFgsMTNa7zUHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
#فوووووری
؛ اینفانتینو تصمیم گرفته که حق برگزاری مسابقات جام‌جهانی رو به سرمایه‌گذاران خصوصی با بالاترین رقم بفروشه. کوشنر داماد دونالد ترامپ از خریداران مطرح طرح اینفانتینو به شمار میره
❌
از طرفی یوفا به فیفا هشدار داده که اینکار نقض آشکار روح برگزاری فوتبال هست و باید به صورت جدی با عوامل این تصمیم برخورد بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102175" target="_blank">📅 19:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102174">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl4Xejz0tKUkZ1XxAHcL_so9UL94fECmrr-irsJBzmLU_tFFJTgDEsXhDyxyScs86QqWhkZNvQ9dmLjyNc2QkgZtMLkkq3ujsxVKD0O_B0aaqQAp2YsWXGdTsb2AgUGFWRBv1kIsTQnjgVOW-0t-a3QrsnLWZxnSNhpnSY7LQbzgcmiry1qAAAN9YSVO9GyQzoqAH07n_FpXWDJXy8v0VQgyUzOVE1WmtD2Of5TnSzHgP7gne4NFqiJFViEeSCqXcAXGXDgiqgQbNEmC2MPlQSBB60rZ-jBQet3DJxLhYw4XLNhDkXHWqoSP3U6Tnu8J3nUb-oPPcTQ1549dYkEmPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇪🇸
اسکای‌اسپورت: رئال‌مادرید به پیشنهاد آرسنال برای جذب وینیسیوس جواب رد میده و هرگز اجازه خروج ستاره برزیلی تیمش رو‌ نمیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/102174" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102173">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=kg_VaQp-YO6BbSys14rqrkN3LlYmXH7fqR8IC4QwhLHifiusWUWpBSSfzD0IjJ1qY09IdHzHC_1DBvPk-Rvcf6yi7A8yuihLHM_GTXhrC6yoHvw0NG-138Lv5fpOiIvT6xzEKXM4iMxixnyrabsgGb-skdn2KO5pU7uZThti61E1sMn4K3ao1o0wr00KBDwodOkuH6K0PgOa5zJsZbDXyHut3v63_r3oO7hJfzfGX9wtdoOuD333_J7wY5_shIOb83u88BQe7VxX7BmEyb9aZg-3KFe7HRNudqyyCcQiKa16CQdDVyodrJSz2QhdHdorYRmVt1QyoGfZp9OICCzDHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cb3c3fae0.mp4?token=kg_VaQp-YO6BbSys14rqrkN3LlYmXH7fqR8IC4QwhLHifiusWUWpBSSfzD0IjJ1qY09IdHzHC_1DBvPk-Rvcf6yi7A8yuihLHM_GTXhrC6yoHvw0NG-138Lv5fpOiIvT6xzEKXM4iMxixnyrabsgGb-skdn2KO5pU7uZThti61E1sMn4K3ao1o0wr00KBDwodOkuH6K0PgOa5zJsZbDXyHut3v63_r3oO7hJfzfGX9wtdoOuD333_J7wY5_shIOb83u88BQe7VxX7BmEyb9aZg-3KFe7HRNudqyyCcQiKa16CQdDVyodrJSz2QhdHdorYRmVt1QyoGfZp9OICCzDHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😆
تتو دلافوئنته روی بدن کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102173" target="_blank">📅 19:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102172">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QitpTL6fOT5Hf_RaRhedpE8Mpu66Z6xFBS834CXbwW7YrZwzJu5Kijt_kiZ3Ndp3RJqHiJyzFSHmyjYXGx6M-dOySpyfxxBQB_U470YUgrjK5Bnc_auptC9RoFov25Ok_TiUFbxkvSRVPHSw7i-ZugtDCsFl1H7vjK3xbqncpq3TDn1TQ9AagW78hEFOaTsCmdqRGtqEfdZvTXZKorGIjyVAsPvwayoZguULvOKFqc0yAFHdQml6w9KuR9ys4NYcEXswGWWp3WJbw6g4mhlwIkJ1WAPYjvgBjMMAUm3e3DpZJiS_1gBlXE-yOFYiprIZhDD-HNLorWD2xmI7vJJ46Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب رئال مادرید در اولین بازی تحت هدایت مورینیو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102172" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102171">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkijiHYzKFAesmAR5xX7yiSVkpv1PUtRWCEEeOgNikVaoRdQueaS4m-83JBH5CeloguGTzo1qPyswwiWIg1iWk6UQLh6KpFm986CiDtkQnIFPGqwDCYiHMps3lNUZNYhOmt36u0afDLtlM5G8u_75zOWMmfwWz-whoYuPcHvxUezPNmLnqyVulgscLH6z4RsyuP4ir4aLLXU5lnVtxBq6W924Q8BNGqX2ADOrFoGS2lZiq4sgf1EYLtT4gygLqJTjAGa-RtkJn27-mSe4J138Uz2L_br46aWAgzvCXeA-yqoCRDr074xISvRxBGFKla7sAbB67h-CEjw1GeS6B5OzNQ7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/164942a925.mp4?token=DPsAwkIYQP0L3sMg6jlVim1IfxUuzrSNX_nD6I3GjY90kbNI1iXWYPIgpphwvXcbeym_lxJTQJX9HzAvcZacf4GxWnn6iTH8HUQam0zp2_gxXGiTLp2hMgPc0KKFYUkU8X-7zCB5TJ6HtJYhsWK5Sj1HWhIYmGZZJnw86lZLFqHGLZq-jbU37a_VNqU0fRqjtnh7OYtImAUi_SFCo9hbjM_6nEnvgrMMCDzukbqnFr1RkaAXe12vdWm0TwlhSyQj_sbJGTmPG6kJLItcsGJ95Z2eLcbncXMIioBlRVB-9-iry4wZ-jKXvYve6nfDCoH6goQVUMnQlgIAxgd9GodkijiHYzKFAesmAR5xX7yiSVkpv1PUtRWCEEeOgNikVaoRdQueaS4m-83JBH5CeloguGTzo1qPyswwiWIg1iWk6UQLh6KpFm986CiDtkQnIFPGqwDCYiHMps3lNUZNYhOmt36u0afDLtlM5G8u_75zOWMmfwWz-whoYuPcHvxUezPNmLnqyVulgscLH6z4RsyuP4ir4aLLXU5lnVtxBq6W924Q8BNGqX2ADOrFoGS2lZiq4sgf1EYLtT4gygLqJTjAGa-RtkJn27-mSe4J138Uz2L_br46aWAgzvCXeA-yqoCRDr074xISvRxBGFKla7sAbB67h-CEjw1GeS6B5OzNQ7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
👀
برخی از سوپرگل‌های بیرون‌پا رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102171" target="_blank">📅 19:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102170">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfZzYJf5x2laBRqpRtHT1-2rSmbi9_F2BGE4dIVSYrCAu81F5EBuyahKfmdMbWhfJXsBwvvJeiA4BSgDuou0DfgeAr7rRc7bKbH8Tjz4y9FngItf621tET9jFzm_AISqGv6TuvG0LB5sjGcioOmIvGKLgQVq8KR40bvqYJwU1JqXfQUhitARSmmBt_hHkmMJFGmXzyEea0-hqPF4Y9snw35EWVriOeV7bnziA4eko6EbMiQdCpkkHqpbrC3Tl0mtzSU3WBMlypb85OAklamCYzDke3Nh6XoS0PBpx_cUKrzPEN8rJamtPPm4hnfcWgSruaByJjCCqkq5_YW_2dNnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
‼️
منتخب بازیکنانی که در پایان‌فصل‌آینده بازیکن آزاد می‌شوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102170" target="_blank">📅 18:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102169">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjb6-pnzDmprmuJk3LPiBPFtcL2cPuZU9SV5FkcUCfUfkMdOZ4zwgO5mL4fCkg67G3evqQdiCaCS9c7MEGzSOoHq5M8k5g2R8jCgMX-XHOG5ELhbkM2oj-wfBwntKToZIGkMPkaMeLFS9DwybAowiSBOu02CW86Fi8UvDQPK1fZcawtQOr7YwAjWSkuZFzIzeC9hx1hqXapSJeVJUY6tcw0Xop_h84JpWn6Oh4OQjbgdYC9ZW_85trPMt95sRb8-afWRYnxHAtYSBGZnpGu2lsbavCxB6PqWflzlWk1bLhu8MkwkrPKFtT20yTrQfm_Aln3gdQT-9WJ6Bwt7OMqhWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔎
🔵
ژابی آلونسو بعد از دو هفته حضور در چلسی سریع متوجه شده که تیمش برای قهرمانی خیلی جوان و کم‌تجربه‌ست.
‼️
اون گفته به بازیکن‌هایی نیاز داره که تجربه و شخصیت برنده داشته باشن.
🔺
جردن هندرسون — ۳۶ ساله
✅
۴۶۳ بازی در لیگ برتر
🔺
دنی ولبک — ۳۵ ساله
✅
۴۰۰ بازی در لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102169" target="_blank">📅 18:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102168">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYoBhxsxdKHAONZ3jtq_svla7rdRx1cSitgfTM4bXNxgaAX4LRw8A4VKYqAvIbH-HDcMrYUUmP_Qqh8LN5ZwPqO286BlyNgHOqj95M09AOG7lhP9JOnsvB5GPa62vN_fltwWJ-pFM1gnRxaggija6Ob0G-Ph9dIe5_ukw9fp-MaCTNyTAPczOy-rbCMW0qs-9gapCc7nWCeztL5spSudHxYm_8M4mTnKxSA0IC9m0LzNZ1HuEcVpYyfWdMjYoweNHm9ZjCPYeqbDzIY5HFaGyCDyx7twAeO592RKxwDFtFhL4IM6taQJ5fS4Ve4BSuuX5-tFVezVJ79StsF1hriFTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗞
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: ساوینیو به منچسترسیتی گفته که میخواد تابستون از این تیم جدا بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102168" target="_blank">📅 18:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102167">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVNKw5JVl66Szvb2AkjuukNI7zu_4_qDBxj6SEPkFRl-ecUQKSqIA09x7kh0t_5m0CUbTqWT8moSgjREbKKlGRdr3uqZwATffMISpJXunUjaNSGC1aQTjZuHgb_qZlP3kL5Isfn7bMytT0AaR8g4JWIlvalyrtq1znXVgeNnjVcYm8phHU2y75gdrsk7wHsqwp2U_gb5jfh4L6qjOX93Qsb6FpfvqL-UMLoVtES4e9JIKx2hfNV6z-AsbMXVZ3B97jamQBDGicJgXGnsWnMjTe0E2r4P0b--QGXd143fD0dJzO-gC-oAer_x_O8NapB6NbhefS_lF0yv2S69ZgVYTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نیمار جونیور درباره لیونل مسی:
من کنار مسی بازی کردم، مقابلش بازی کردم و باهاش تمرین کردم. باور کنید تلویزیون همه‌چیز رو نشون نمیده. سخت‌ترین بخشِ مهار مسی این نیست که جلوشو بگیری؛ سخت‌ترین بخش اینه که قبول کنی بعضی وقت‌ها واقعا هیچ کاری از دستت برنمیاد. از زمین بیرون میای و فکر میکنی خوب دفاع کردی، اما وقتی صحنه‌ها رو دوباره می‌بینی، متوجه میشی که اون کل بازی رو کنترل کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102167" target="_blank">📅 18:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102165">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vq0iXaaicdVpXAmuSld-PH3gH3h0pTysAdTFHR49jFwKC12aMFqcTRiw4QRx-CZqfvaA4e_1yVK9YJTnTbwujJyWWmMTxDS163rPcbFUvMWksQ2NQiWnjPlWQ1rD6ew2G3wpGuOdyHeBLdeDgAwdIJFeN8sMnRVGWrdzvybHN8MQaCdSJLhZ2cQMumeavPjg-97LI3nEtp7u04LsFZSD_U8Tb240-6ERuLUX3eWjr1AJ0WybnPHJ5gvVOxb9yh1ExdJeNN4YHMQZmIwd0twoRqlw1PhLIdrVyqhCcUMiF-R0gDQxVj0qTfnnrAe3Pyg2aLveumUsfOa4ki8I1Otjzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LD5ka-4F9pbmf4NfyxziuDhsldzHyeHdzv4vuzChAInisz0dTBMIwJ5ehhtSk8uIxVj48f8XhjlCO8GGTIONfADkmbWeYq2Jbc4goxc7uHdAQ3SnJozbPQTb3pX6UkqQGNacKYDPzhRYO2rKHvZKEzTz0nAE9uy7V3y0M-2Udd1nmUJ99aaPd8IUZzX27GoiSGE-pafIZcaE14CctrFJ1bVtq1vC1-8mXx9gnsA_Ih9Q9DF9ih6DZFa6TqAKP7z-621HHEfYhj2cR5aN7EGMNZyopzsrFomoOGmKalw7g95r6O5Ydn0jrcsjOoTTEE-iolNRfsyiaS3t_k4EI-ZpGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
🇦🇷
رودریگو دی‌پائول درباره اینکه کریستیانو رونالدو خودش رو بهترین بازیکن تاریخ میدونه:
این نظر خودشه! برای من، لئو مسی هنره. کریستیانو رونالدو یه ماشین گلزنی فوق‌العاده‌ست. اما شماره ۱۰، هنره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102165" target="_blank">📅 17:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102164">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WagISHqPqPD3xBhl3TjGbm53-h9acJ32rLFhXFHNSa328c3whBqZ2GnSaq7Rnzcne7Sa8vkl9ZgCeuokY7OWXxZj5Z1EwtU-ldNhQCxrJ_v_XvCfetbVntQfSyG4i6Xzo4b5Ut5N0PeXPU3FcMwmGuIABHSpAavpU0O6phUfk5g1Ro4iOIuSsWE-Wx80GZF94U3cR1U2tf4tIeZ30ktJMuuzDsnR1HkknEfcd3oydi7pKTEeHyWLbVaRLEy4onMa_pgpvCy4M1fV-MSw7hXjqxtQrDZ0-EHGlXW0uQVPJgFKPCovxsO3OaQegsAvamVOpBHza8FLG1SF_aVFLRIv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102164" target="_blank">📅 17:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102163">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/Futball180TV/102163" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚨
✔️
🏆
برنامه کامل فصل جدید لیگ برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102163" target="_blank">📅 17:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102162">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🔵
برنامه بازی‌های استقلال در نیم‌فصل اول:
🟠
🏘
هفته اول: مس شهر بابک
🤩
✈️
هفته دوم: نساجی
🟡
🏘
هفته سوم: سپاهان
🟠
✈️
هفته چهارم: فولاد
🔴
🏘
هفته پنجم: پرسپولیس
🟢
✈️
هفته ششم: آلومینیوم
🟢
🏘
هفته هفتم: پیکان
🔴
✈️
هفته هشتم: تراکتور
🔵
🏘
هفته نهم: گل گهر
🔵
✈️
هفته دهم: چادرملو
🟢
🏘
هفته یازدهم: شمس آذر
🔵
✈️
هفته دوازدهم: استقلال خوزستان
🟢
✈️
هفته سیزدهم: خیبر
🔴
🏘
هفته چهاردهم: صنعت نفت
🟢
✈️
هفته پانزدهم: ذوب آهن
🟡
🏘
هفته شانزدهم: فجر
⚪️
✈️
هفته هفدهم: ملوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102162" target="_blank">📅 17:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102161">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🔴
📊
حریفان پرسپولیس در نیم فصل اول:
🟣
هفته اول: شمس‌آذر
🔵
هفته دوم: اس‌خوزستان
🔴
هفته سوم: تراکتور
⚪️
هفته چهارم: ملوان
🔵
هفته پنجم: استقلال
🟢
هفته ششم: ذوب‌آهن
🟢
هفته هفتم: خیبر
🔴
هفته هشتم: صنعت نفت
🟠
هفته نهم: مس شهر بابک
🟠
هفته دهم: فولاد
🔴
هفته یازدهم: نساجی
🟡
هفته دوازدهم: فجر
🔴
هفته سیزدهم: پیکان
🔴
هفته چهاردهم: آلومینیوم
🔴
هفته پانزدهم: سپاهان
🔴
هفته شانزدهم: گلگهر
🤩
هفته هفدهم: چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/102161" target="_blank">📅 17:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102160">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh8Lpa7oqDcbDrBHgqnV7YMplTp5pAOR8R18k_GEIIU9hofSC7Km9fwO84c8qiaRFffBroXC38Nci9u9gXB_VGeOvhkvgNKEbR1HngON9JPkdDgu0C2kDTCpMaJwTzYxpsCqmnh-K7O3AvJQdUfDICiLHTkVAxGQYUqQJ0rooZquUzaTXqjOaygrGKU-iKsETIWPGumQNsPC3D3Zn_vwo08wtbZkdiFHhQZG3RZsYmEGT9wET4XP72ZwuCQHuTmxWrrZ9MUHYAwl5XGfBPLCpAJzI7dkpIz0T-L3cBRKqAq2ap-uPC8TivgYYHMk20qw65zLd_7xJqzdOUpgAydSWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
روبرتو مانچینی رسما به عنوان سرمربی تیم ملی ایتالیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102160" target="_blank">📅 17:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102159">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHsLAxrHn5An38Oe4DaOZVDrDjmBhPa_2_9wTtQwi4dvSHxQYjiRaZyJB0WRFb8aDTOZ82ayLKxd0lsqU3-E5izDYXo6gXhEQgHc1PVGjOz5lp6EWWqTMFbNZbA2dhkcP6_fgvMLX_f_jNGH8RGphL8MlJf7H487Biwotyjc0qr0ouZ5ZJ83dze2tDyD6pIK9vxkpti7HTit7DC3njIxmYAZmcQa5emHuzZ4MUq5r4x4URKbIy0Lg0-Ju_SOMWhQ8w4aBUrSQjSGGgTSSjpjVxBLkQydGCdCK2FzXk0v_NxfxaidGC9vPHi9k5mahPxLR_HYnVM-PuwaVCs9bkOMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗓
برنامه هفته‌اول لیگ‌برتر فوتبال ایران
🔵
استقلال - مس‌شهربابک
🔴
پرسپولیس - شمس‌آذر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102159" target="_blank">📅 17:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102157">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpC2eyjADYddrM7ryjTL_td8U-X2R3McUhiQXIBqwcdjaz1H_P7mvQCnaBKG3n8vzixOOl2jqKrPMnOhtqcrLoGyS0mVn8-BIMBqAYYVHUDQLVkYsiBqgEQeVKUXXN09lU6tmCC3SpfvtqtvLki56qrXXJAgTjsjMr1iamLOtbbULVp2vQvxcyDMw9SXge5Hj2sl1rQeRUv8zm5i5iXrjRR65dg_7EKOLZpr48HqjJZmE3h57vrfTuBdolb1jCbaXQEje8D_dbgfPN7AivMJrgikNtp6dXfn7CTQPosJSXqNnlH9UpQ2nu7jSjC6KmmRolHI2K7VPwaHEhLZ7irdmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=b-OGPmdXa6EiC0afWLDWDW9Og1dCmfXH_drXImH728wTuDmI3QjMpT_JidIX9lOqMVz4-WAdq06Sc3gKqHrqJ1CEwbOsN0ZmQXUIxiRkOdTtv-KmxO_6K_Ydtm5v5OlgWvRVXdKhvkeOa6NR6zhOhqv4jKqyszu8xykKx5bucy99NUf96-lrOzo2nFlRBFzK3mN8NzYoww6M43LWAU3yPOK6GttiHOeNw6UcBPat7Z-mtax7DSHQPfwH_Ejjee8bKQrpiNfp1ddJUIkW0S8ILJSi0KcgCG-9G-TDGBpm3rV7qbGo8c731lkmZoBgLfZkO4TGFP-HF_ifHl5cCKko_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c787f96db6.mp4?token=b-OGPmdXa6EiC0afWLDWDW9Og1dCmfXH_drXImH728wTuDmI3QjMpT_JidIX9lOqMVz4-WAdq06Sc3gKqHrqJ1CEwbOsN0ZmQXUIxiRkOdTtv-KmxO_6K_Ydtm5v5OlgWvRVXdKhvkeOa6NR6zhOhqv4jKqyszu8xykKx5bucy99NUf96-lrOzo2nFlRBFzK3mN8NzYoww6M43LWAU3yPOK6GttiHOeNw6UcBPat7Z-mtax7DSHQPfwH_Ejjee8bKQrpiNfp1ddJUIkW0S8ILJSi0KcgCG-9G-TDGBpm3rV7qbGo8c731lkmZoBgLfZkO4TGFP-HF_ifHl5cCKko_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول درباره جدایی از لامین یامال گفت:
من قبل از لامین هم توی کار خودم موفق بودم. این لامین بود که اول بهم پیام داد و با وجود اختلاف سنی ازم خواست وارد رابطه بشیم. حتی گفت ازم حمایت مالی میکنه و هفته‌ای ۲۰ هزار دلار بهم میده. همه‌چیز خوب پیش رفت، اما بعد از مدتی دیگه پیام نداد و منو بلاک کرد. الان با مدارکی که دارم، میخوام این موضوع رو از راه قانونی پیگیری کنم..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102157" target="_blank">📅 17:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102156">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/102156" target="_blank">📅 16:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102155">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFeDpBYsxHvJuVGRlGe3Om6oNhIJzcxffFUdGdsiro2yHttBWKGX0DIDih3xA2gO3-uWqoqU_7XeW8ZeOVkWYADJs7aywbMzmq4I3Wnkl9wZ7mhiTsbeY6mzmB4toGBuuiDX3BzsxZ5tPb4QvzHi5GZ9wjRXqq-1GQ1jWfk4_XX4Z9D2c-KpDIqWvyY_22Lq_K3xtElcwc1wFQllBMxqxoJABrvG_DaK7QnA7ffr1TwRh9HeYHbF784kUFFWwNpaC-76BlByUZC5GtJDPN0_Yw6grP6QeCBb8mHRND06-JvTxdewWG_kmsqD90HtK3jDhA0wdk1wsWBYcLlfu0g2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از نشریه لکیپ فرانسه: لیورپول با بردلی‌بارکولا به توافق اولیه رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102155" target="_blank">📅 16:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102154">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfvcn7JDkxksKmFLSKDrgTnzelUgbwVf71JKM_7937r8CJDjf4LCHYoFuYRMvoNcOHWChPQJDGgmsNFAkD__mWImoGlwKdZboTtD8FHj8pWoa-fv1Ei9i5Z4F5HdU7aHYfKegeQ2LFxGMuL5XnjQDjPmnCUNBpi4Ra-eVjho7YzQWbPhbswY-kU74artWFa8gYs65mfQXVqqhx_194BFFDnD8wyeCtThxWpAFbyRaIqef_7ULokSWXlNXqUHJ9_SoIw-DR7dTGLWx252biREUUoBxY6qxC2k3qfmGV-2qsvsLkkmdKZhW38pQfZAQ6jLuvDTgZs2x4Gu-xAOrP44Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
🔴
دربی پایتخت در هفته پنجم لیگ‌برتر برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102154" target="_blank">📅 16:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102153">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3lvaGmADwb9zbi0BIPWMiHnltaY0FTNH5A2mEOSvs9L84QBJ-GceisDs-x1uOiz3BUgPuNMoDz1SczSkMNZ6YU2KeBlv-yrk5gGsKb1qRiE-vM0h6PGKvIQh4PAJl-RGzuMQ1EVgOR8X0iWiAL1f_f8RzUR8pnkHtvMF3ioQ5PQeH8G8M-oD1igkXyas5Ojo2-Uid0FUe7XpJRH-C6_ukUtp3_WlQuDv0R1K-EE3Skzl3tPIJEym-djm-sjPbL_V9HQXsM_oqSB7q7KL47fMFcnQ7VpyuL9jHg7_q_tg12NVTJe7kdat4UNAt4JwGj_XhVQaVASk5CKO6Mn0B-rbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🤩
محمدمهدی‌محبی بازیکن فصل‌گذشته سپاهان به پرسپولیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102153" target="_blank">📅 16:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102152">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmEaFsHinbqsB1bsJgMJ1HufbGngA0jUkv4JOf0O4mHwKg1r6dbcz0cCgawNOVAgF-wp62EQ01__xMeL7fkaKLwWux7vEdWnUKiXIx13hGAiOHHWlJkpgsUeAWaeoRgMj8ZZrZOSeXNaVvnLlqbB5o_-gcOZqSr8sO8eo5GTpXQikaZ1KC8LxTUdqqixOhmQMDphLg5gsYWnFK7LGr9pRE0BfSsdnc_DOvRykI2CkDzCGGUTkcDeSbOkdr1dNwUjRsqdD2BSnKcQXDxbXlcSbU9i7nDHLi_wLjhTdvbZrxmTwl9XCWq15-P1xpV2amUFvVpSunKsZG_bEyhVtkyWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102152" target="_blank">📅 16:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102151">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLNqu3lvwlWcoDZQ5y3p4ZUHvMthCrQLebZdj2ELVWzcfiAje0Lj9Slj4q-kbSh0c3HCE58Lr7KNK-MysBFpNBpc2uHh1iGkWougRVYP4avQm6__ajhw7XvKoh71MfdzHNgCC_JoWOCiNw63qFqFl8O5PZP5ZKsa0kxPUcCUEBZi1AxeZuHaf7lSj8ZgLN6zTiAvLrlwDsACRZrVJzIYdrpY1SuwpHuEYBoGe9KqdzzyfcilqUYJjouDdo6IMOS4dVvPBGEQlYy9k4rci0KZd7wLJ8oKHVtg-31sP9UgI-c0d7K_8HRjT6h_O4y02EDAwORmg6bIIOTmrVbjp3eFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینترنت سیم‌کارتتون زود تموم‌ میشه؟
چون ایرانسل و همراه اول اومدن روی اینترنت بین الملل ضریب 4 اعمال کردن! یعنی شما 1 گیگ استفاده کنی 4 گیگ از حجمت میره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/102151" target="_blank">📅 16:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102150">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=D7n0uplerUCGhN2_UhgBrnkQiez1G0nxwaVNQczhrf6shwVlSOKabA6fmR_E2L3SS1prMSkmZ_ycP3NdAraHtHZnPqrWotUliNDDyKWMeEAhSINt3VSMGTDGiAAzC-SRbvtYsQdqT2NByZkTiOld-TfubrbY9C-HmAQwcfQrbpUCs2Kp6oN9-Yc-Nz1ol5K6lnmX4YICbuHOo6GTyLPoOI-kbC0Z220wbZ7eK7gI7eo15Cr_HIv2hSXR8LFQiLFGkC1ylCbouLq9pQPT91BSc0Rg4Cs_X4WLAYEQTdSe9-lT7iiIMC2AnmQ-HNJ8eq1kgGbnpH3Di4rJgcI4K_3pGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881c68dbcf.mp4?token=D7n0uplerUCGhN2_UhgBrnkQiez1G0nxwaVNQczhrf6shwVlSOKabA6fmR_E2L3SS1prMSkmZ_ycP3NdAraHtHZnPqrWotUliNDDyKWMeEAhSINt3VSMGTDGiAAzC-SRbvtYsQdqT2NByZkTiOld-TfubrbY9C-HmAQwcfQrbpUCs2Kp6oN9-Yc-Nz1ol5K6lnmX4YICbuHOo6GTyLPoOI-kbC0Z220wbZ7eK7gI7eo15Cr_HIv2hSXR8LFQiLFGkC1ylCbouLq9pQPT91BSc0Rg4Cs_X4WLAYEQTdSe9-lT7iiIMC2AnmQ-HNJ8eq1kgGbnpH3Di4rJgcI4K_3pGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
من بعد از اینکه توی مستر لیگ PES برای دهمین فصل پیاپی بدون باخت قهرمان چمپیونزلیگ شدم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102150" target="_blank">📅 16:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102149">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iN9I0CKIdehM5swr9SRmmd44sPUr30H4ExPAPaFyIcMgZRONaGNQC376IICnbLdfJMJ6J5tWxsvJT4Onu2Ej-xZ8idK4BOuElEA-0IaPzB0AruPYzO7hMriH9yNwhkEwQE2QsxeA9VZ5Bxcl-yoD0jJXMppYaOS8VHPezw6j0fYgvqG6F6xoJ7AA5GmEO9pOYImgsPOakifmTbNkoRhUCJaOYaRZ8-yx3x3SisNmPikVisqCXZBnmJnrspvBSOZSQL18rO3NGXAN7U3URqkDaxb85j-voCSwRNZtEFgLurNNr3TBg5ujrvxB6xJ9-fmbMv3pk_hdR-4JK-Si1H0ZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
✅
کوکوریا به قول خودش عمل کرد و بالاخره عکس دلافوئنته رو رو بدنش تتو زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102149" target="_blank">📅 15:43 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102148">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IqvjnfkpG6GW5g3AVCUqDgfCKLVPohIo3PfeKblSB8n_apwWwAajE6LqeoW2uv6urNtIaOnhr5LxG6r_xbCvuU66nBERTnV1884Ft1HOgd6IH8_w9MupcyaBwZ98oKzMA9xsQUdYhLjXzV77vUslN2aAJB-gfg54qtaOdLQiqHRu0os8qtDHEwkwjA_yDFldkbOJh9fSc5SVn6edLexKbLtdSK5L3An8pj4tBfzaBWiSxl35hjBZkZbK7opfwUMKFyF0r9gnN8WWEmhP0LUSV7OPq9__waJyUC9t7b0lcUgvWC0uUo0fvjbZ0vFSu3sw4d9-UgoMKiRs0rX9QqsziQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🔵
رسمی؛ قرارداد یوشکو گواردیول با منچسترسیتی تا 2031 تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102148" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102147">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=uM6D_zZgl0YorXbEL_YxxrKpNZRQ1D25DJgKwBQ4OwBId91pLARjzOcVZvF6sPnu2BnPRZ9WP5LlIh3UmCJCcotrKm64ID3rbV2qIaZ2Y80W4i569k7csSZUjNEUPy0HyEi5BTngm-ztYqko_Q1VuyVApFXQQFUzI94L4P8QvV4azZAUXAd-8a2oWBmnH4PFspLLApyOqrevRWWpHRy7_JQpHIiVDo5j7w_1ivWlXj6OpHFnOLKex_LkULbfaFmb8ntprg79wA5KWhVBLQdb4hTNkFvrz8Ak1rRdIOwQO9AhfeXbd0_GMWjw1sf0lsZaiGhylYV4R13B_ilFcihjFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f242c0afa.mp4?token=uM6D_zZgl0YorXbEL_YxxrKpNZRQ1D25DJgKwBQ4OwBId91pLARjzOcVZvF6sPnu2BnPRZ9WP5LlIh3UmCJCcotrKm64ID3rbV2qIaZ2Y80W4i569k7csSZUjNEUPy0HyEi5BTngm-ztYqko_Q1VuyVApFXQQFUzI94L4P8QvV4azZAUXAd-8a2oWBmnH4PFspLLApyOqrevRWWpHRy7_JQpHIiVDo5j7w_1ivWlXj6OpHFnOLKex_LkULbfaFmb8ntprg79wA5KWhVBLQdb4hTNkFvrz8Ak1rRdIOwQO9AhfeXbd0_GMWjw1sf0lsZaiGhylYV4R13B_ilFcihjFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال به دنبال جذب وینی.
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102147" target="_blank">📅 15:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102146">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=mFNaHEYDFxlXP-DqsmP1GY3eMe9i1zUMtVYBShbJ5Jl947wKfFBy26Og3sJD_puv9jXtmupN4XSWQuCutc10R-x8iQ1gcdpX2oFmHytfKilhaau4j_5-EUZUHo19LH1mG8LBJRET9bG7I8HK__bPgON3PhrJkvGYQ3FLAieXv03NgO2PZBROFYD2bktWX_eTJt3gta38KbICADXm6NYGdLn0G7Zjq65-QMobKyHjBh5vkyAIF9LM2WGgaA-ffb7PCRSSNqsH707SCsMGECRj5aY5Jxi55gNKnl6nyYegSMGezE8fmNbegd_56h5cl-fQL0DQSP-Ca2F_3rVJ859hPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ea2f2fd87.mp4?token=mFNaHEYDFxlXP-DqsmP1GY3eMe9i1zUMtVYBShbJ5Jl947wKfFBy26Og3sJD_puv9jXtmupN4XSWQuCutc10R-x8iQ1gcdpX2oFmHytfKilhaau4j_5-EUZUHo19LH1mG8LBJRET9bG7I8HK__bPgON3PhrJkvGYQ3FLAieXv03NgO2PZBROFYD2bktWX_eTJt3gta38KbICADXm6NYGdLn0G7Zjq65-QMobKyHjBh5vkyAIF9LM2WGgaA-ffb7PCRSSNqsH707SCsMGECRj5aY5Jxi55gNKnl6nyYegSMGezE8fmNbegd_56h5cl-fQL0DQSP-Ca2F_3rVJ859hPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇹
اولین‌بازی روبن‌آموریم با آث‌میلان:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102146" target="_blank">📅 15:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102145">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gbnk4Yp-MK30qxfEYZAF-IdrIM0qEenGTAvoW5SVZmYStz9NF-dcIUbV9GZ5tz0lWrwkx5Iw2x9ALSMQOffwknqveXhYFHXzd2H1b-Xnb_RmJWcFnwCh-a3ZUWzw8umb4FvfEcMoydBVZNIw48gMmiH6U8cZug1fQQdoyzvVLyhk_DH-RJEB_Cr8b2qYl5LRhdkU2s37IR_bNMNTRdJg7cMIxw6v9UcqN4LlBGzZ3bWPCsuHIzxXmN-7k4I9rZqilLyAqZIW-TKnWA1mWPiEQ-ajKcLLriaex57vURa9wynV6ri-v6XQmlGj39VRaT8AwS8Lv4DPfjBw9a3YArSRNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102145" target="_blank">📅 15:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102143">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TsNdpmtT4g32UahjUcQdHY2MXCCQWWTjO0gkjZ07-XF5fFRCWpCP09wWSpcghhfOjqSr157v4sG0_FFBHC8l6H9awmpVlSqfFzh8rir795rAHlxXFVRuReh4WdgOnr3vwDzR1_DPRw0yA5hrm9Z7gROAMmPIywjs352SyUa476eGfHwdhdBBdoIBOAuugOO700egBvyMIKFgQ4vejWe9Xi_j1mB7zozWwt1nD5aGTE39aTHsD_Y9z3JI57uPiqo6yAeO9_CidrYSyhUfpXKs7h7RMYAbR1DzsEdlblVGQI3R17dkKMbHJxbkVfZH49JJNwDFIg-w_iVKko2MenHSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WliYrqS6_bMiPwVqqyX-CmkJIsKS04rp9lwv7h3Sb-Pbnl04ckEQNLC1Zsi_7Xn5yDjMyTpK62h6-suhb2eZwAn7QJb_UBVqmz-z_UFw5mcXAaG1SOdFGh3-MYWZ22Vuly6gFFkri9z-w2RuYXwxfbYimbfp32AuavyZGBtmFZHQUDRDMsGE8TIkJ-ppWPuJF1ytVX1j9LyPSYjC5qHt-L_MU6GzyGWIp8I4CLZMJILQPWy3LvyCAUSE9GdXNCEuGzPapUVybawPBYDbCJL2WhFRKdvFZ1a6wJQzT_2mK1NtHacpRy454I_8vuW3vWd2XGECv3xohOKT6PlTUCBpwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
👀
مائورو ایکاردی گفت همسر سابقش در جریان طلاق درخواست کرده بود:
💰
۲۵۰ هزار یورو در ماه برای خودش
💰
۶۵ هزار یورو در ماه برای فرزندانش
💰
۱۰۰ هزار یورو هم به‌عنوان غرامت طلاق
اما قاضی این درخواست‌ها را رد کرد و سیستم قضایی ایتالیا هم درخواست تجدیدنظر را نپذیرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102143" target="_blank">📅 15:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102142">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqxjWpuz8mqoc9Ys7dUnEJ_EQHRDCncS9NBDczNlrvf8Ar85OwL4O5LNOHcc4NYd4s2WW2BUXvXKlD6BZz292sRGq4IAvW9jJP_Che2gDstezxDzrivowYGvPuGEar2oTVW3vGvn5JKHWhAmnm64ZZV9ZERL0o0S-lvWiqTmXgy6i1r5CrZGvvXUS5HAswYt1Mz4RNoIQkxGnb7xmT3vIG_Z2MZkrgRWoeukon_k9z0MimgamrJ8rnJkwMBZCVmGFmEuYsIHETsC3qH4H_PXg4ITyN5fBMSK9iwTmpX_sMxnxtowd9xpNBvTQ6YR4baA5l-BJtNc3Ul10SsJrvTbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
نیکولو شیرا
🚨
🚨
🚨
توافق حاصل شد: کلودیو رانیری، مدیر فنی جدید تیم ملی ایتالیا خواهد بود.
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102142" target="_blank">📅 14:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102141">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdvMZrXKJk8VA0su0VsFTTOEDz85kRNmtSDAL6oERuPnh_dYWKRmvBQC19otaHyfiDlVIsdG7f7DLRUUK_wplzvzLQ931nQJFEL9UpdeWeWH7dePB7S0mTyzdDiBf5qJQ_EhcvC66qBH2UArtDzR2hvkee228zUwbyK4bpzxt4AdBgoIOXp52VQtL1MNPUz6Flxh_QBhImwoWhBPmLQ1-CyRsG-mWTwORE4wo-glSK0s2zdqVHp_SyV9ezqgFreMx7Y4wHwZSotSbUJNkhYM_VzepDd4WljS067RjEa0ZNoXG9KDDmd2Sg6qEbceSQ0pS6LaBDqKILDjMu7LDTJZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
#فورییییییییی
از رومانو: مانچینی سرمربی تیم ملی ایتالیا شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102141" target="_blank">📅 14:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102140">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/922dff29be.mp4?token=HXNz3hloJFnIhWoVhxzFprPtADgp7g5bzkxbpN4snzisrPENvpmWuYPFq1jerDIJ708fYob02YEOamrY421GF4xkO0zgPqe9IBvI6jNEPsEHQe0kY7v6bIem1LlLRouxtDD2GbqIAde0U5hC90z_jAD3GDeDfDyvIy-GiI6Q0-Y0zoFSnZs9zZ6vNtVFqoIYOl8nOAhvJAEW-L02PthzbaBK5_H4NrYRy30T60WZMhSoe6p-l8iE-4LdndqT9yz8BgWzPWnpiIZwefSv7SeeoDBdxoZ7by05vltRNkng5Mwa3BlScsmYgws0A4HqlJO9H88JAgU-mY0E8sMlrOawWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/922dff29be.mp4?token=HXNz3hloJFnIhWoVhxzFprPtADgp7g5bzkxbpN4snzisrPENvpmWuYPFq1jerDIJ708fYob02YEOamrY421GF4xkO0zgPqe9IBvI6jNEPsEHQe0kY7v6bIem1LlLRouxtDD2GbqIAde0U5hC90z_jAD3GDeDfDyvIy-GiI6Q0-Y0zoFSnZs9zZ6vNtVFqoIYOl8nOAhvJAEW-L02PthzbaBK5_H4NrYRy30T60WZMhSoe6p-l8iE-4LdndqT9yz8BgWzPWnpiIZwefSv7SeeoDBdxoZ7by05vltRNkng5Mwa3BlScsmYgws0A4HqlJO9H88JAgU-mY0E8sMlrOawWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⭐️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برخی از سوپر‌گل‌های معرکه استیون‌جرارد اسطوره فوتبال انگلیس و لیورپول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102140" target="_blank">📅 14:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102139">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👀
▶️
💥
هایلایتی‌از تقابل تماشایی سه‌فصل پیش نیوکاسل و پاری‌سن‌ژرمن در لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102139" target="_blank">📅 14:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102138">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=hZxbYSF9DxzvDbK1DyvWYiaYTEFa0PQmsLiSjaeCcuZYRfWYhFpDI9_rRIyYiCzzaQxMpxP54TgTR4Kv1icjpb24lfJJJTqwmxKuGZQ4N3aZfnyXhOLXTY8otqpsfPzIjyEDd4hPzyHD9prpHSFyma84MRnzJWBttNQ4jbFo7BtWLCDtJ-0sF_MzN4IpdDjP1UOhbryya9OMdFF-PbknilcICffye7vU7QxwOr8OrqRjC6HptH4afU70TNPxd38UzNZn0Sgh59ieSzC0iPd2R9J-GwcUyO1VUziQNEiOdtc-WM9S1HoKBcyqHQQI2kKsO4Cmvm6Xbl4TcAHjJitrMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90f94a2bbd.mp4?token=hZxbYSF9DxzvDbK1DyvWYiaYTEFa0PQmsLiSjaeCcuZYRfWYhFpDI9_rRIyYiCzzaQxMpxP54TgTR4Kv1icjpb24lfJJJTqwmxKuGZQ4N3aZfnyXhOLXTY8otqpsfPzIjyEDd4hPzyHD9prpHSFyma84MRnzJWBttNQ4jbFo7BtWLCDtJ-0sF_MzN4IpdDjP1UOhbryya9OMdFF-PbknilcICffye7vU7QxwOr8OrqRjC6HptH4afU70TNPxd38UzNZn0Sgh59ieSzC0iPd2R9J-GwcUyO1VUziQNEiOdtc-WM9S1HoKBcyqHQQI2kKsO4Cmvm6Xbl4TcAHjJitrMoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
امیرحسین صادقی: از وزیر انتقاد کردم، به دادسرا احضار شدم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102138" target="_blank">📅 14:09 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102137">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iq9xXOy5fHxvjhV5g8NEUSFqcl0R1lnNGS-lMPLpR6jfeB8qP4Va32Ft088IrW5dXqyOoW_VajfBjmjLI2ZAM0FQDmpeiQPfuRuXwTBJ1zFtr52oBSk-D1870FdhZrWbU1VkdBOeRTDIUeBJ1tVKiaaYGz3HOe9BsZjpD6llxtRrUw65oNvo7Naz9HJsY5h8Qm0sbuBnF8rgpTQWdTGfk5F99APglnVEtn-EWKixd-QAjtrbeTKif5tIPoUbGdS1Jr81UXUBAPlnjKkPSGzrxU9jlclLQ351U35jByjynbVaeF4HlrAUQTUcu5gZs4rKbLPVfy5b6i33sBvyvDB_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از دیوید اورنشتین: وولتماده مهاجم نیوکاسل مورد توجه بارسا قرار گرفته و به صورت قرضی در دسترس کاتالان‌هاست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102137" target="_blank">📅 13:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102136">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔥
کنترل‌‌توپ‌های ستارگان که منجر به گلزنی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102136" target="_blank">📅 13:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102135">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iVP0Bv84DYr4UuHZWLxJW7d7j8SNO6kuE7THfXr_2BUfuh5RA9af9pVj5zDQ_fljhXomSdW8zv_YmQycrorLf2ARTi2Y27hc_qOFcGB974Kc2kvdeyigCh9OUc5_gASOEpmBoJpKFk2DU2QYBIZ-jL_1oXH9WcScFTMGELYrRZCVRabtfivcIRTzNTeVkrwo84R1cqVBOGJgBdeoi5rsUJcHlaxJ26zXqaLd3reeExWufMuzW5rLmsk1FgNy51cDGljZWKm7tAJJwmfi7-88lk5Ya4AC1swWojN-QxRHOJowwYmxJGIcpPi3PDipS61IshkQn99V0fkx6jDi3Gu28A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باشگاه بورنموث علاقه‌ای به فورش جونیور کروپی به بارسلونا ندارد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102135" target="_blank">📅 13:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102134">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_eoTA7U0A4WyqlUlkmuTi43pQ-_6Fcl-6x3K46oMysmTHHhRylnkl7DonBUwXbRIG0DMWcXC1kkBGl68vNUkUyr3XdGPIAkSPxPK8VpfOwu5wAAea3A7mfQayxuO-K5GQK3D5_GW37puWU0tOIguSAsAx_k0fSP_vCYvZ6Ns9tRTowHxmwTFggxVeIjfpwB7w6iSrcR2HgAJM8xanZ64bhhcStv6z_qNvVoODXwK_AjxMBoEIqASvBUP1Z4HtLn7E9AIXTSjct01M5YLeDFntoBkITgPKizQRrLC2jw6BMg7qrPC9ryFyPO1k4-vErAQ3eaSjPyngw9faQjX9Gk3iPTc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/792acb1bf3.mp4?token=HU5xeRkFhQJYTScjssOMLWveWDXYSXY6iFQUgXBhlmi-i3Jn_0NaaEys_EOBknkCcyDD7HqbMg_K4QNLei_V6p5D0pCABEMyCL78BC_NOhRj1SokEX1JQSyBXpSX-FU_8DbKU_lLXo1VsHri2A4dfubtVw1yobjA4QbUjEafUkjRRJsfzLUV6l7455bQOUn6pu2zJUMnsXUkS1uAbb64n6WPqxqU3Kl8Dr79TvZsyl84mlj0CLWBhrkWCTIj2zlwffBvbhoJRwu7t8vCCvk-rTSH8CbXkkwq_zG1RBVxoF6ZKNzDSnHyDOk0BAdIOfKVx4T-mCsqkSqL47bdJ9b_eoTA7U0A4WyqlUlkmuTi43pQ-_6Fcl-6x3K46oMysmTHHhRylnkl7DonBUwXbRIG0DMWcXC1kkBGl68vNUkUyr3XdGPIAkSPxPK8VpfOwu5wAAea3A7mfQayxuO-K5GQK3D5_GW37puWU0tOIguSAsAx_k0fSP_vCYvZ6Ns9tRTowHxmwTFggxVeIjfpwB7w6iSrcR2HgAJM8xanZ64bhhcStv6z_qNvVoODXwK_AjxMBoEIqASvBUP1Z4HtLn7E9AIXTSjct01M5YLeDFntoBkITgPKizQRrLC2jw6BMg7qrPC9ryFyPO1k4-vErAQ3eaSjPyngw9faQjX9Gk3iPTc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
امیر حسین صادقی: قلعه‌نویی هم مثل علی دایی جر زن است؛ کاش آن حرف را نمی زد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102134" target="_blank">📅 13:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102133">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=HdTbkF8rIYtKE7LWLTV5h3ANX9-Bsgt46BmicSILKJiJYjnJ0dGK0JqxnQsAb3SogwoZ2W8R1dQm7RBT05CPutpXb0uvK4vlLoVTm37OIeU2s-SXsWX57ZFcEnoDkeST4c9QSJORQ0ZoJWC5r5yzHhwO5DXOjHmcKbDtNktqdLMytdl_yjcZHLF899IHURcGpMKc-Xg2FBWQiJhBt2Xpl0VWHHm4D-GBEJ1DkPfT7OI8U41U0B3Cms5hSbJHQONb5e0YtXCFH3DFPsZU7iFlfa4OA1nI8htakGdm9waif1ZzDb9S8ZZRC3p0-iA--EXYDfJYo--FXmd7W4Az9_jP5RNQJWaLOaBy0qPzXbjkG9Gu1xWX6Rrq2_Zjbf2__yCTKn_svJiwnLDDLPItQF_6qZ4CfXzE1KCt6XIuuPKzb6Pz-nKdH0Pwu3vjaizCCu-3tjBvPectY95qAe8RI7Q14IOfDBP0Vua1ihiyjD540F6B8HAq9eYlHLGnqKWlyX8VOvupNUbFvsveK7SQsMqiCmwwTcKKrapaogvTWR03OpqCqHe_ubGY4vhP9g9aMzgv4lR13OlWdPOYEXJO5_joXPUPFRwvHBwFb_FSOBMpZbZ3ve-Non_vN8bM5fpnqL-SB9YRXUVzwgxHIp0n7eGNxdYXbsl2Gfdieo-38RPNcTs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9afeb8a4ca.mp4?token=HdTbkF8rIYtKE7LWLTV5h3ANX9-Bsgt46BmicSILKJiJYjnJ0dGK0JqxnQsAb3SogwoZ2W8R1dQm7RBT05CPutpXb0uvK4vlLoVTm37OIeU2s-SXsWX57ZFcEnoDkeST4c9QSJORQ0ZoJWC5r5yzHhwO5DXOjHmcKbDtNktqdLMytdl_yjcZHLF899IHURcGpMKc-Xg2FBWQiJhBt2Xpl0VWHHm4D-GBEJ1DkPfT7OI8U41U0B3Cms5hSbJHQONb5e0YtXCFH3DFPsZU7iFlfa4OA1nI8htakGdm9waif1ZzDb9S8ZZRC3p0-iA--EXYDfJYo--FXmd7W4Az9_jP5RNQJWaLOaBy0qPzXbjkG9Gu1xWX6Rrq2_Zjbf2__yCTKn_svJiwnLDDLPItQF_6qZ4CfXzE1KCt6XIuuPKzb6Pz-nKdH0Pwu3vjaizCCu-3tjBvPectY95qAe8RI7Q14IOfDBP0Vua1ihiyjD540F6B8HAq9eYlHLGnqKWlyX8VOvupNUbFvsveK7SQsMqiCmwwTcKKrapaogvTWR03OpqCqHe_ubGY4vhP9g9aMzgv4lR13OlWdPOYEXJO5_joXPUPFRwvHBwFb_FSOBMpZbZ3ve-Non_vN8bM5fpnqL-SB9YRXUVzwgxHIp0n7eGNxdYXbsl2Gfdieo-38RPNcTs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔥
چند ضربه کاشته تمرین‌شده و تماشایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102133" target="_blank">📅 13:03 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102132">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQSoQ1dC36CQxG-EnsozPcT7FLelMEYpU6MQ_Z1kJTINxHTsyPC4eM2ba-jJGGpABolbY0rYbh-n6ZuA2IJttxRDStNYZ-56xfDFg6Q8F7wBH1N0meySuf-IVo_u2MONAcHRM3zJfig9qxU25YCYFuaHZPc5yGg00jHFvMenNGXZcvjXZu_qsRalVgAn2KBRMk-Cxy2p8bq3MC6G1ON3hVKHVB9dOMwO7NZ2JC_88Ia5JaeJjWCTAErEajO5NOTlte8rAc7JsZ0tUi7hZfDgz4qPYW9HWp06YVjaDGG2x7l65xVSS2FDPhqpcu0i0VhKcDp3pxOOte3M3uL0-lzE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک خرید احتمالی چلسی در فصل گذشته پرمیر لیگ بیشتر از خریدهای جنجالی تیمای بزرگ گل زده!
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دنی ولبک: 13 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بنجامین ششکو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هوگو اکیتیکه: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برایان امبوئمو: 11 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتئوس کونیا: 10 گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102132" target="_blank">📅 12:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102131">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
✔️
#رسمیییییی؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102131" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102130">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJVtJ__POswtvwAy4HB8XfU-vFzHpAhx7LiFd8mCTwWrRn3XHxMMpU8EjO2IM2Qx82axcZxgwmB7ODQ668JCWzXAJntC53_r9zNaGUZTHLK2Pu1U3FDTg38qhVaItPllNmAC0b3mae8zpvXz4j9o_6fZWw6rrXYBKhrV1-pgPeRdD3kk-e6ASRk2ozsRAybuvOlL9Qmryy29rtmFdPkQNXXIdFRXapp4seyvTjlRcqIRRSvIjEGB2m5YWGK-OuVNVKtbZzy-WXOPImjXOHtDuUCpHqb-D4BHthnOph2g3eHt7XfeFZSvx30wCT-IIDS-PrmWinX2TUILANbZurPu9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
#رسمیییییی
؛ زین‌الدین زیدان تا سال ۲۰۳۰ سرمربی تیم‌ملی فرانسه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/102130" target="_blank">📅 12:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102129">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=G2PnJ1-U42yzJx3jq36JxErdpKvdV_eexZxXCDfltuTig7giNEgkx5To-mz1mAsRcQiURNB0u_an6PV1-AWGculyU8UQ4zVPQbCyBY-Yy8zqlklONz5Hf7gCOal7pP3it38yG80VK9V11f1BFhy0NquirLkR0aB4bXr5CjOOcp9cSC8cTroeGkFKttTnwJcTZ8fO-ivMPAIA5AvzhWUr08PGScOzvx8w7k2adqXLaEOi6KAdRj4KPaaUW_J0KyO0XnqnkTSr4FswpPZJduxNX1Yznqz1XxIef7Vbm5-Mfu-zjO7ajS6FVtqeMe45LInYmN5jWSbWVjuBFQqxWp4kOa9hV16A45MlSv2-dpZee3O8gU5PL56XjlIoJ03l_b1y5AwK0slyUtaeqnmGqK6eQnt9EdJrOSuEHwKaMsICZ0VssYwsK1vj7aCChAK9Ozr5_pCfTJALNXQmOVA7g5XkJUy5Q2Go4ScMqrd_P09F1AG0fMyac5oRKiQiR3A55dK5ZANC9HsPXL3WYgwGSAI2FV7U6AVhPacWF8thXA-aiT32OqL5v0mFcod2jLRGLll1mD5SYyHCKtrN2POUVD4lbQUHj2wOhZe4jqOg5k92RRA7ZNGoqhHaRtZx57F8uaE2Bb_U1NFZ9bMt-YbEd-N5We8IJfjnTJ3eYWweSN-jlpc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/496ccbf92e.mp4?token=G2PnJ1-U42yzJx3jq36JxErdpKvdV_eexZxXCDfltuTig7giNEgkx5To-mz1mAsRcQiURNB0u_an6PV1-AWGculyU8UQ4zVPQbCyBY-Yy8zqlklONz5Hf7gCOal7pP3it38yG80VK9V11f1BFhy0NquirLkR0aB4bXr5CjOOcp9cSC8cTroeGkFKttTnwJcTZ8fO-ivMPAIA5AvzhWUr08PGScOzvx8w7k2adqXLaEOi6KAdRj4KPaaUW_J0KyO0XnqnkTSr4FswpPZJduxNX1Yznqz1XxIef7Vbm5-Mfu-zjO7ajS6FVtqeMe45LInYmN5jWSbWVjuBFQqxWp4kOa9hV16A45MlSv2-dpZee3O8gU5PL56XjlIoJ03l_b1y5AwK0slyUtaeqnmGqK6eQnt9EdJrOSuEHwKaMsICZ0VssYwsK1vj7aCChAK9Ozr5_pCfTJALNXQmOVA7g5XkJUy5Q2Go4ScMqrd_P09F1AG0fMyac5oRKiQiR3A55dK5ZANC9HsPXL3WYgwGSAI2FV7U6AVhPacWF8thXA-aiT32OqL5v0mFcod2jLRGLll1mD5SYyHCKtrN2POUVD4lbQUHj2wOhZe4jqOg5k92RRA7ZNGoqhHaRtZx57F8uaE2Bb_U1NFZ9bMt-YbEd-N5We8IJfjnTJ3eYWweSN-jlpc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
رئیس مرکز ورزش و تربیت بدنی دانشگاه ازاد: علیرضا بیرانوند سال پیش فارغ‌التحصیل شده و الان دانشجوی دکتری نیست
+سربازی در کمین است؟
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/102129" target="_blank">📅 12:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102128">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_8GldjmhR_UrjSalcYjiOCZdKNyxNy5jQKVwp1eG_fSq6ftd-2fppjcJjADTAAznEjdlR-ZNE1ctwKc_t3iXoMB-m_11p0Hr6Fr4UbHrqLfFVFcCcbUjwAyUootFvGEgOMAiNx_QDhEWX5eGTByrHu3f2mvCeNEX262cLNQCI6OGxLE2sNAN9NC34nXllLjzvC6no_z21cljjLYWrjJ0lVpUxdAiluT5FXDDBKj9zD4gOrAKPJrwAoofGGjJe_MvRmii0ga1n-wI_x0sX4eyI6mkenfvVsC0BfTPmyNJMpNnkSMq5hGcI7YdTJjJgkx72j7dG6vUkvcqYoZ97X1Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بازی دوستانه|ترکیب تیم‌فوتبال چلسی مقابل وسترن‌سیدنی استرالیا؛ ساعت ۱۳:۱۵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102128" target="_blank">📅 12:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102127">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=n8fYfqKVFh_65uxLLp6fR4h1a9PS_Hcn4K3O31oREPzwvMMJuDnqSCz4WSZLL8iU1yMbxBCi35ghu1S3ZrESsYhXs6TysVsOo3yhsJtkeoxxfJ_E4SlraOt0dUz-wlqlS28FBuMVKzckDOwKL1j9lFB-NF0AWe9YyyVurGw96_FzY1pR-B1WuXEkP2Ghx_NB1vKdxguq-E4sGSdPIaSkToyHMOeqZGdJusTMRdbLzgC1CeloWdi_hzBy7k2ksBV4iWrukKMsxur-hyn2Jo5k0VMQXPnWIJv3RpdslqIHk6ti7PNw7IaLO7cgXaZXnZ_Q7LUDmusmgo2QGa5yrpHEbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04499b20cd.mp4?token=n8fYfqKVFh_65uxLLp6fR4h1a9PS_Hcn4K3O31oREPzwvMMJuDnqSCz4WSZLL8iU1yMbxBCi35ghu1S3ZrESsYhXs6TysVsOo3yhsJtkeoxxfJ_E4SlraOt0dUz-wlqlS28FBuMVKzckDOwKL1j9lFB-NF0AWe9YyyVurGw96_FzY1pR-B1WuXEkP2Ghx_NB1vKdxguq-E4sGSdPIaSkToyHMOeqZGdJusTMRdbLzgC1CeloWdi_hzBy7k2ksBV4iWrukKMsxur-hyn2Jo5k0VMQXPnWIJv3RpdslqIHk6ti7PNw7IaLO7cgXaZXnZ_Q7LUDmusmgo2QGa5yrpHEbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
خلاصه که نگاه کردن زیاد آخر و عاقبت نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102127" target="_blank">📅 12:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102126">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQ3hJwgL9XO4OmJuiNaPhW8QaAWn9qaJwdwD7YfxiZ_pswGyjngscl79I8aN7q_1nPAI9oV8Qlnl1BQTkJGMoajlg1SSXeTqxeukXBWrFvjEtSNUJ4GBuB52unTdwe78RqekTGt0mXHSxDQY_9ZmX4Q8iA1NgJjYa-uFgxhVS_N-Eep9wkLsNbVYS8-vvel3GY_hssaiw5Fo8IXJ7eJcldizSWwMh2EH9xt7X6Hgnj9fpfW90wXIpOe3TIgY0yxWBx-LsGuioKCSx_Xd6wxgKv1P2fgJUgKDzfXywNBsylnJyydQwXUJsB8FXj0yMGIlzXvw53dqnln2JQB-hxNCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😍
‼️
آپدیت جدید و عجیب اینستاگرام که شدیدا مخصوص ایرانی‌هاست..
شما میتونین در قسمت «یادبود» اینستاگرام یک نفر رو مشخص کنین که بتونه بعد مرگتون در پیجتون فعالیت کنه، و توی بیوی پیجتون هم میزنه «صفحه یادبود»..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102126" target="_blank">📅 12:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102125">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7A324zQNwkXgw3Uc0cN-IK0QzUoaQsGSOSXxXbOhoK9nZAUzFFN-Hd3Z4eV-vO1aMOaEj-BPgFZ6aTj7eUi_nEAxX0ijRMnJQigm6AfKKpsCO6Z44cANAJfy6lyVLMcqHYupxwICGs-GnmSsgPTom6vu2FzlMk_687XIufMhCo--9iCXSk2vCpcYegq13BXxZxIlxDmtLFEInyT5eTH5LjnojJkdipq4JTouzFpJ3KSIJojgSV7qcnQHI0cJax6eZaGgCisNL3GZ6KVo1Yvyl9CiliZdsLZm1w3PZsgx70votmWf_NbV6yxA9gbespQd0jKIS_TqA4oMzzJqyRlMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماتون بریزه که یامال تا الان که 19 سالش شده با همه اینا یه دور تو رابطه بوده
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102125" target="_blank">📅 11:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102124">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=iLbaITfVkZgVI8WwClUhFnMKavY8HEqedOlbTdL1-nOPbPeW0wC7LHyMkk_ZiWTp6PkZxZddvNS5NKqeQOgW8xuI9hpEZbi0S3QkgDSPAJsKfMzFugU8eZbX6Ul_KTOdGtS4H4vJCdJcc53MaXXNGm5phEChGOEMMHC5PcJwQK45iM8rgxWHZKKh_fBsn6HqSS4hjeasd-kbv2p3dztfHN1ZwEuk_8XqApepk4mK13MLdc4BJwA4i5IxOZka0L0ixqNzs8PNUaL_HXoTYJW7fI2kj6820SOPBTq1mmHdwHchDv4vVNwBH5OK0Z-Gw2i0p9I7UpRHq0iwG4m8GKobMA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/07378b8b26.mp4?token=iLbaITfVkZgVI8WwClUhFnMKavY8HEqedOlbTdL1-nOPbPeW0wC7LHyMkk_ZiWTp6PkZxZddvNS5NKqeQOgW8xuI9hpEZbi0S3QkgDSPAJsKfMzFugU8eZbX6Ul_KTOdGtS4H4vJCdJcc53MaXXNGm5phEChGOEMMHC5PcJwQK45iM8rgxWHZKKh_fBsn6HqSS4hjeasd-kbv2p3dztfHN1ZwEuk_8XqApepk4mK13MLdc4BJwA4i5IxOZka0L0ixqNzs8PNUaL_HXoTYJW7fI2kj6820SOPBTq1mmHdwHchDv4vVNwBH5OK0Z-Gw2i0p9I7UpRHq0iwG4m8GKobMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو با کیلومتر ها اختلاف آندرریتد ترین ویدیو سم تاریخ فوتبال ایرانه
دعوای علیرضا منصوریان و فیروز کریمی در یک قاب ، منصوریان میگه فیروز کریمی داره بهم فحش میده یهو فیروز کریمی از اون طرف داد میزنه :«گه میخوره»
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102124" target="_blank">📅 11:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102123">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=NbkxtABfTG7oZVbe8MxzP4H9c_NUYneI-J8G_yk0YtW2WKbWWf9icxc1G1AyZ08U0T9DB0u4xeLR9Hi0cobbQEQafZrA2VWY-Y_C8oWxhCpPqZwf4UshFHrfe8wRShCj3fUZnJYRTAMijbpS5e-2yiiHH6w1RmRvJh4Ac6xogTns09gwHWOblMyFHSAINdn0WM9aBewxNx6xiDvQ4RDl0wTOxqfQOL5W3diuR6QN6HUzrTjo0CC-YKvkotVJznOvRbhyfS2NfX9x4mLgb5hIvJ_Py3WCLoaetNID5oWVndlRK6Jl6wDk-pvWx1ApkZ3hjFqvwN0qSRrlviDyw3x2hgUJsTRXhRsfWBRpi0TqrpJXDK2hh4ShcqOGyPWI4g_Og_NYQRn3CcOimeZMpReC_zd1iB4UEWeRQ1rzmhUSa68GcqBBfT6mw4_wc-Dl17Ylo0NJ2r09YpMydewt-Ye2nWJtq7-SmBjINDUAW9nL1WWfksawQYnQ26cQctzFKREvTc2FqMN3iVFqeIoAimGz3ymb5xAhFvl_38TB-gmvMTRdFqAVsRMeDToFlg62UPPRw_h4lOnhwSDUVhhkDD69nkiyR4N3tUU-kOAJnZOZYCOI6pzXWcF9i8t-Yw_n-883kidrofuOINYibFSWLJQz45OHZAo0SGLYiWq7Hxw48vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeee92fd86.mp4?token=NbkxtABfTG7oZVbe8MxzP4H9c_NUYneI-J8G_yk0YtW2WKbWWf9icxc1G1AyZ08U0T9DB0u4xeLR9Hi0cobbQEQafZrA2VWY-Y_C8oWxhCpPqZwf4UshFHrfe8wRShCj3fUZnJYRTAMijbpS5e-2yiiHH6w1RmRvJh4Ac6xogTns09gwHWOblMyFHSAINdn0WM9aBewxNx6xiDvQ4RDl0wTOxqfQOL5W3diuR6QN6HUzrTjo0CC-YKvkotVJznOvRbhyfS2NfX9x4mLgb5hIvJ_Py3WCLoaetNID5oWVndlRK6Jl6wDk-pvWx1ApkZ3hjFqvwN0qSRrlviDyw3x2hgUJsTRXhRsfWBRpi0TqrpJXDK2hh4ShcqOGyPWI4g_Og_NYQRn3CcOimeZMpReC_zd1iB4UEWeRQ1rzmhUSa68GcqBBfT6mw4_wc-Dl17Ylo0NJ2r09YpMydewt-Ye2nWJtq7-SmBjINDUAW9nL1WWfksawQYnQ26cQctzFKREvTc2FqMN3iVFqeIoAimGz3ymb5xAhFvl_38TB-gmvMTRdFqAVsRMeDToFlg62UPPRw_h4lOnhwSDUVhhkDD69nkiyR4N3tUU-kOAJnZOZYCOI6pzXWcF9i8t-Yw_n-883kidrofuOINYibFSWLJQz45OHZAo0SGLYiWq7Hxw48vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
نوستالژی خاطره‌انگیز از دربی دلامادونینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102123" target="_blank">📅 11:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102122">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=C9aNCP5k8wS4xKlwU2WM9tbnaTfK7-6qR3cSqN9RQLu2ExVPLmLQzfsko86lj-sUu7M5h4hJ8862gllK9V2gTgVtKcTOiKzbhckcDNak-Mqs9Rz3Ja7YDnrfsui2X0JppCX9vtVax-X3MN0FpkZ4zIpJKKIHHESgwR0zcbncxN0EpQI2u6wdazCmhIj9nppIs11ndKxby4W4AiqPDsK9IrhsW2O6eelAv_lkD85rysgMuVzIpF5HUJixP2GRf5z5KOR84IMe2KPknfFdsgZYS4ni00fiTfsxtPzfMcMIiNCLGb5z5_XPZEIky8IwsN2FCPk1m6bNCEVfwPD0IyxFBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7aafdb5637.mp4?token=C9aNCP5k8wS4xKlwU2WM9tbnaTfK7-6qR3cSqN9RQLu2ExVPLmLQzfsko86lj-sUu7M5h4hJ8862gllK9V2gTgVtKcTOiKzbhckcDNak-Mqs9Rz3Ja7YDnrfsui2X0JppCX9vtVax-X3MN0FpkZ4zIpJKKIHHESgwR0zcbncxN0EpQI2u6wdazCmhIj9nppIs11ndKxby4W4AiqPDsK9IrhsW2O6eelAv_lkD85rysgMuVzIpF5HUJixP2GRf5z5KOR84IMe2KPknfFdsgZYS4ni00fiTfsxtPzfMcMIiNCLGb5z5_XPZEIky8IwsN2FCPk1m6bNCEVfwPD0IyxFBYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
۱۰ گل خوشکل زده شده از مدافعین فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102122" target="_blank">📅 11:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102121">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=cJweP29FG-BkcQjx4PhO2hPgewu0Mmk8XJyhudeum9Z6u_euD_4d7wdIYlqM1ybArPQQeGEW7NYcEMEA54oMQJv1SzsD8g8n86NiwnnE9T7Iv-H1UrPWEvA56SwXrGI7pf3Sr0K5XklG9zIAoVnzwLFI6ULpUGJpxh4qkqEqcLcG3u68cEDd3TUzmhmRgAS09Epswvck-PT5tneiDEF1D7_FNbDtUgIcHUzbw26djwkEr5aba-uwpBu3Rv7gqO7TJzK1np_mwGcwsDcJktOy2WrFDseGymoKE8iF2jX-e-Si6fYZLdAqM50KkYpm_IzEvlBL_nQRpU88MLAl43lYlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd7bc32139.mp4?token=cJweP29FG-BkcQjx4PhO2hPgewu0Mmk8XJyhudeum9Z6u_euD_4d7wdIYlqM1ybArPQQeGEW7NYcEMEA54oMQJv1SzsD8g8n86NiwnnE9T7Iv-H1UrPWEvA56SwXrGI7pf3Sr0K5XklG9zIAoVnzwLFI6ULpUGJpxh4qkqEqcLcG3u68cEDd3TUzmhmRgAS09Epswvck-PT5tneiDEF1D7_FNbDtUgIcHUzbw26djwkEr5aba-uwpBu3Rv7gqO7TJzK1np_mwGcwsDcJktOy2WrFDseGymoKE8iF2jX-e-Si6fYZLdAqM50KkYpm_IzEvlBL_nQRpU88MLAl43lYlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
خوشحالی‌گل‌های عجیب در لیگ‌های‌فوتبال ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102121" target="_blank">📅 10:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102120">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">▶️
رضا نوروزی؛ یک فصل طوفانی، یک عمر سکوت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102120" target="_blank">📅 10:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102119">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYiggS1s_O6NSqKJOvp5Rxn7p--7y5A-Zw1uYtQ_xbya5TeXDVQK_FQbS3FfDWhqjbEM7AqigkIsd_bvMCkq65CZL1zKhkcrqgCp9nHmdW_UBa2Xk0vmJ9IfIjRfXSB4emfxE-GCFimEiH5ukc_YYpBC4yy3bIjNVCpQvta2GV69fc-y7NYyk7dAuFNlC1THmlAqSJdxCacoKFcegBCpuHwd5uHf9W8gevpaQoUOfGAL5W3ogcRnoleL38P3t68QiW61YQ3zaMeyAsLsKwznxto3DMExCgdRYo5EYPpkoVI_Por12ObDnFXTVL5v6vOBbBRskl9o91we4zODycsAVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
😟
اینتر میلان به توافقی با تاتنهام برای جذب کریستین رومرو به مبلغ تقریبی 40 میلیون یورو رسیده است.
✅
⭕️
🇪🇸
اما این بازیکن منتظر بارسلونا است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102119" target="_blank">📅 10:06 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
